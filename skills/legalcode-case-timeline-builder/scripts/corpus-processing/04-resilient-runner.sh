#!/usr/bin/env bash
# ==============================================================================
# 04-resilient-runner.sh
#
# Production-grade orchestrator that wraps the discover -> process -> aggregate
# pipeline with comprehensive error handling, signal trapping, resume support,
# log rotation, and monitoring.
#
# Usage:
#   ./04-resilient-runner.sh \
#       --input-dir /path/to/documents \
#       --processor ./my-processor.sh \
#       --work-dir ./pipeline-run \
#       [--jobs 8] \
#       [--timeout 300] \
#       [--retry 2] \
#       [--budget-limit 50.00] \
#       [--cost-per-file 0.02] \
#       [--resume]
#
# Compatibility: macOS (BSD) and Linux (GNU)
# Dependencies: jq, shasum
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
INPUT_DIR=""
PROCESSOR=""
WORK_DIR="./pipeline-run-$(date +%Y%m%d-%H%M%S)"
JOBS=4
TIMEOUT=300
MAX_RETRIES=1
RESUME=false
STRATEGY="xargs"
BUDGET_LIMIT=""
COST_PER_FILE=""
COST_PER_TOKEN=""
MAX_LOG_SIZE_MB=50
LOG_ROTATE_COUNT=5
NOTIFY_CMD=""              # Optional command to run on completion/failure
CHECKPOINT_INTERVAL=60     # Write checkpoint every N seconds

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
    cat <<'USAGE'
Usage: 04-resilient-runner.sh [OPTIONS]

Required:
  --input-dir DIR         Directory of documents to process
  --processor CMD         Processing command (see 02-parallel-process.sh)

Options:
  --work-dir DIR          Working directory for all pipeline artifacts
  --jobs N                Parallel jobs (default: 4)
  --timeout SECS          Per-file timeout (default: 300)
  --retry N               Max retries per file (default: 1)
  --strategy STR          xargs|parallel|background (default: xargs)
  --resume                Resume from last checkpoint
  --budget-limit AMOUNT   Maximum total cost in dollars (abort if exceeded)
  --cost-per-file AMOUNT  Estimated cost per file (for budget projection)
  --cost-per-token AMOUNT Cost per token (for API-based processors)
  --max-log-size N        Max log file size in MB before rotation (default: 50)
  --notify CMD            Command to run on completion (receives exit code as $1)
  -h, --help              Show this help

Directory structure created:
  work-dir/
    manifest.json           Discovery manifest
    results/                Per-file JSON results
    results/logs/           Processing logs
    consolidated.json       Merged results
    summary.json            Summary statistics
    checkpoint.json         Resume checkpoint
    costs.json              Cost tracking
    pipeline.log            Main pipeline log
USAGE
    exit 0
}

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)           usage ;;
        --input-dir)         INPUT_DIR="$2"; shift 2 ;;
        --processor)         PROCESSOR="$2"; shift 2 ;;
        --work-dir)          WORK_DIR="$2"; shift 2 ;;
        --jobs)              JOBS="$2"; shift 2 ;;
        --timeout)           TIMEOUT="$2"; shift 2 ;;
        --retry)             MAX_RETRIES="$2"; shift 2 ;;
        --strategy)          STRATEGY="$2"; shift 2 ;;
        --resume)            RESUME=true; shift ;;
        --budget-limit)      BUDGET_LIMIT="$2"; shift 2 ;;
        --cost-per-file)     COST_PER_FILE="$2"; shift 2 ;;
        --cost-per-token)    COST_PER_TOKEN="$2"; shift 2 ;;
        --max-log-size)      MAX_LOG_SIZE_MB="$2"; shift 2 ;;
        --notify)            NOTIFY_CMD="$2"; shift 2 ;;
        *)                   echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

if [[ -z "$INPUT_DIR" || -z "$PROCESSOR" ]]; then
    echo "Error: --input-dir and --processor are required." >&2
    exit 1
fi

# ---------------------------------------------------------------------------
# Directory setup
# ---------------------------------------------------------------------------
mkdir -p "$WORK_DIR/results/logs"

LOG_FILE="$WORK_DIR/pipeline.log"
CHECKPOINT_FILE="$WORK_DIR/checkpoint.json"
COST_FILE="$WORK_DIR/costs.json"
PID_FILE="$WORK_DIR/pipeline.pid"

# Store our PID for monitoring
echo $$ > "$PID_FILE"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
log() {
    local level="$1"
    shift
    local msg="$*"
    local ts
    ts="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo "[$ts] [$level] $msg" | tee -a "$LOG_FILE" >&2
}

rotate_log() {
    local logfile="$1"
    local max_size_bytes=$((MAX_LOG_SIZE_MB * 1024 * 1024))

    if [[ ! -f "$logfile" ]]; then
        return
    fi

    local current_size
    if stat --version >/dev/null 2>&1; then
        current_size="$(stat -c '%s' "$logfile")"
    else
        current_size="$(stat -f '%z' "$logfile")"
    fi

    if [[ "$current_size" -gt "$max_size_bytes" ]]; then
        log "INFO" "Rotating log: $logfile (${current_size} bytes > ${max_size_bytes} limit)"

        # Rotate existing logs
        for ((i = LOG_ROTATE_COUNT - 1; i >= 1; i--)); do
            local prev=$((i - 1))
            if [[ -f "${logfile}.${prev}" ]]; then
                mv "${logfile}.${prev}" "${logfile}.${i}"
            fi
        done

        # Move current to .0
        mv "$logfile" "${logfile}.0"
        : > "$logfile"
    fi
}

# ---------------------------------------------------------------------------
# Signal handling and cleanup
# ---------------------------------------------------------------------------
PIPELINE_STAGE="init"
CLEANUP_DONE=false

cleanup() {
    if [[ "$CLEANUP_DONE" == true ]]; then
        return
    fi
    CLEANUP_DONE=true

    local exit_code="${1:-1}"
    log "WARN" "Cleanup triggered (exit_code=$exit_code, stage=$PIPELINE_STAGE)"

    # Write checkpoint for resume
    write_checkpoint "interrupted" "$exit_code"

    # Kill any child processes
    jobs -p 2>/dev/null | while read -r pid; do
        kill "$pid" 2>/dev/null || true
    done

    # Remove PID file
    rm -f "$PID_FILE"

    # Notify if configured
    if [[ -n "$NOTIFY_CMD" ]]; then
        eval "$NOTIFY_CMD" "$exit_code" 2>/dev/null || true
    fi

    log "INFO" "Cleanup complete"
}

trap 'cleanup $?' EXIT
trap 'log "WARN" "Received SIGINT"; exit 130' INT
trap 'log "WARN" "Received SIGTERM"; exit 143' TERM
trap 'log "WARN" "Received SIGHUP"; exit 129' HUP

# ---------------------------------------------------------------------------
# Checkpoint management
# ---------------------------------------------------------------------------
write_checkpoint() {
    local status="$1"
    local exit_code="${2:-0}"

    jq -n \
        --arg stage "$PIPELINE_STAGE" \
        --arg status "$status" \
        --arg timestamp "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
        --argjson exit_code "$exit_code" \
        --arg input_dir "$INPUT_DIR" \
        --arg work_dir "$WORK_DIR" \
        --arg processor "$PROCESSOR" \
        --argjson jobs "$JOBS" \
        --argjson timeout "$TIMEOUT" \
        --argjson max_retries "$MAX_RETRIES" \
        '{
            checkpoint: {
                stage: $stage,
                status: $status,
                timestamp: $timestamp,
                exit_code: $exit_code
            },
            config: {
                input_dir: $input_dir,
                work_dir: $work_dir,
                processor: $processor,
                jobs: $jobs,
                timeout: $timeout,
                max_retries: $max_retries
            }
        }' > "$CHECKPOINT_FILE"
}

read_checkpoint() {
    if [[ -f "$CHECKPOINT_FILE" ]]; then
        jq -r '.checkpoint.stage' "$CHECKPOINT_FILE"
    else
        echo "none"
    fi
}

# ---------------------------------------------------------------------------
# Cost tracking
# ---------------------------------------------------------------------------
init_cost_tracking() {
    jq -n \
        --arg start "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
        --arg budget_limit "${BUDGET_LIMIT:-unlimited}" \
        --arg cost_per_file "${COST_PER_FILE:-unknown}" \
        '{
            started_at: $start,
            budget_limit: $budget_limit,
            estimated_cost_per_file: $cost_per_file,
            total_files_processed: 0,
            total_cost_estimate: 0,
            total_tokens_used: 0,
            cost_log: []
        }' > "$COST_FILE"
}

update_cost() {
    local files_done="$1"
    local tokens_used="${2:-0}"

    if [[ ! -f "$COST_FILE" ]]; then
        init_cost_tracking
    fi

    local cost_estimate=0
    if [[ -n "$COST_PER_FILE" ]]; then
        cost_estimate="$(echo "$files_done * $COST_PER_FILE" | bc 2>/dev/null || echo "0")"
    elif [[ -n "$COST_PER_TOKEN" && "$tokens_used" -gt 0 ]]; then
        cost_estimate="$(echo "$tokens_used * $COST_PER_TOKEN" | bc 2>/dev/null || echo "0")"
    fi

    jq \
        --argjson files "$files_done" \
        --argjson cost "$cost_estimate" \
        --argjson tokens "$tokens_used" \
        --arg ts "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
        '.total_files_processed = $files |
         .total_cost_estimate = $cost |
         .total_tokens_used = $tokens |
         .last_updated = $ts |
         .cost_log += [{timestamp: $ts, files: $files, cost: $cost}]' \
        "$COST_FILE" > "${COST_FILE}.tmp" && mv "${COST_FILE}.tmp" "$COST_FILE"

    echo "$cost_estimate"
}

check_budget() {
    if [[ -z "$BUDGET_LIMIT" ]]; then
        return 0
    fi

    local current_cost
    current_cost="$(jq -r '.total_cost_estimate' "$COST_FILE" 2>/dev/null || echo "0")"

    local exceeded
    exceeded="$(echo "$current_cost >= $BUDGET_LIMIT" | bc 2>/dev/null || echo "0")"

    if [[ "$exceeded" == "1" ]]; then
        log "ERROR" "Budget limit exceeded: \$${current_cost} >= \$${BUDGET_LIMIT}"
        return 1
    fi

    # Warn at 80%
    local warning
    warning="$(echo "$current_cost >= ($BUDGET_LIMIT * 0.8)" | bc 2>/dev/null || echo "0")"
    if [[ "$warning" == "1" ]]; then
        log "WARN" "Approaching budget limit: \$${current_cost} / \$${BUDGET_LIMIT}"
    fi

    return 0
}

estimate_total_cost() {
    local total_files="$1"

    if [[ -n "$COST_PER_FILE" ]]; then
        local estimated
        estimated="$(echo "$total_files * $COST_PER_FILE" | bc 2>/dev/null || echo "unknown")"
        log "INFO" "Estimated total cost: \$${estimated} ($total_files files x \$${COST_PER_FILE}/file)"

        if [[ -n "$BUDGET_LIMIT" ]]; then
            local would_exceed
            would_exceed="$(echo "$estimated > $BUDGET_LIMIT" | bc 2>/dev/null || echo "0")"
            if [[ "$would_exceed" == "1" ]]; then
                log "ERROR" "Estimated cost \$${estimated} exceeds budget \$${BUDGET_LIMIT}"
                log "ERROR" "Reduce file count or increase budget. Aborting."
                return 1
            fi
        fi
    fi
    return 0
}

# ---------------------------------------------------------------------------
# Background monitoring (cost + log rotation + progress)
# ---------------------------------------------------------------------------
start_monitor() {
    (
        while true; do
            sleep "$CHECKPOINT_INTERVAL"

            # Rotate logs if needed
            rotate_log "$LOG_FILE"
            rotate_log "$WORK_DIR/results/logs/errors.log"

            # Update cost tracking from completed results
            if [[ -d "$WORK_DIR/results" ]]; then
                local done_count
                done_count="$(find "$WORK_DIR/results" -maxdepth 1 -name '*.json' 2>/dev/null | wc -l | tr -d ' ')"
                update_cost "$done_count" > /dev/null 2>&1

                # Check budget
                if ! check_budget 2>/dev/null; then
                    # Signal the main process to stop
                    kill -USR1 $$ 2>/dev/null || true
                fi
            fi

            # Write periodic checkpoint
            write_checkpoint "in_progress" 0

        done
    ) &
    MONITOR_PID=$!
    log "INFO" "Background monitor started (PID=$MONITOR_PID, interval=${CHECKPOINT_INTERVAL}s)"
}

stop_monitor() {
    if [[ -n "${MONITOR_PID:-}" ]]; then
        kill "$MONITOR_PID" 2>/dev/null || true
        wait "$MONITOR_PID" 2>/dev/null || true
    fi
}

# Budget exceeded signal handler
trap 'log "ERROR" "Budget limit exceeded, stopping pipeline"; stop_monitor; exit 2' USR1

# ===========================================================================
# MAIN PIPELINE
# ===========================================================================

log "INFO" "============================================"
log "INFO" "Pipeline starting"
log "INFO" "  Input:     $INPUT_DIR"
log "INFO" "  Work dir:  $WORK_DIR"
log "INFO" "  Processor: $PROCESSOR"
log "INFO" "  Jobs:      $JOBS"
log "INFO" "  Strategy:  $STRATEGY"
log "INFO" "  Timeout:   ${TIMEOUT}s"
log "INFO" "  Retries:   $MAX_RETRIES"
log "INFO" "  Resume:    $RESUME"
log "INFO" "============================================"

# ---------------------------------------------------------------------------
# Determine resume point
# ---------------------------------------------------------------------------
LAST_STAGE="none"
if [[ "$RESUME" == true ]]; then
    LAST_STAGE="$(read_checkpoint)"
    log "INFO" "Resume mode: last completed stage = $LAST_STAGE"
fi

# ---------------------------------------------------------------------------
# STAGE 1: Discovery
# ---------------------------------------------------------------------------
MANIFEST="$WORK_DIR/manifest.json"

if [[ "$RESUME" == true && -f "$MANIFEST" && "$LAST_STAGE" != "none" ]]; then
    log "INFO" "STAGE 1 [SKIP]: Manifest already exists, reusing"
else
    PIPELINE_STAGE="discovery"
    log "INFO" "STAGE 1 [START]: File discovery and classification"

    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    if [[ -f "$SCRIPT_DIR/01-discover-and-classify.sh" ]]; then
        bash "$SCRIPT_DIR/01-discover-and-classify.sh" \
            "$INPUT_DIR" \
            --format json \
            --output "$MANIFEST"
    else
        log "ERROR" "01-discover-and-classify.sh not found in $SCRIPT_DIR"
        exit 1
    fi

    write_checkpoint "discovery_complete" 0
    log "INFO" "STAGE 1 [DONE]: Discovery complete"
fi

# Validate manifest
if ! jq empty "$MANIFEST" 2>/dev/null; then
    log "ERROR" "Manifest is not valid JSON: $MANIFEST"
    exit 1
fi

TOTAL_FILES="$(jq '.manifest.total_files // (.files | length)' "$MANIFEST")"
log "INFO" "Total files in manifest: $TOTAL_FILES"

# ---------------------------------------------------------------------------
# Pre-flight: Cost estimation and budget check
# ---------------------------------------------------------------------------
init_cost_tracking

if ! estimate_total_cost "$TOTAL_FILES"; then
    exit 2
fi

# ---------------------------------------------------------------------------
# STAGE 2: Parallel processing
# ---------------------------------------------------------------------------
PIPELINE_STAGE="processing"
log "INFO" "STAGE 2 [START]: Parallel processing"

# Start background monitor
start_monitor

PROCESS_ARGS=(
    --manifest "$MANIFEST"
    --processor "$PROCESSOR"
    --results-dir "$WORK_DIR/results"
    --jobs "$JOBS"
    --strategy "$STRATEGY"
    --timeout "$TIMEOUT"
    --retry "$MAX_RETRIES"
    --log-dir "$WORK_DIR/results/logs"
)

if [[ "$RESUME" == true ]]; then
    PROCESS_ARGS+=(--resume)
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "$SCRIPT_DIR/02-parallel-process.sh" ]]; then
    PROCESS_EXIT=0
    bash "$SCRIPT_DIR/02-parallel-process.sh" "${PROCESS_ARGS[@]}" || PROCESS_EXIT=$?

    if [[ "$PROCESS_EXIT" -ne 0 ]]; then
        log "WARN" "Processing completed with errors (exit=$PROCESS_EXIT)"
    fi
else
    log "ERROR" "02-parallel-process.sh not found in $SCRIPT_DIR"
    stop_monitor
    exit 1
fi

# Stop monitor before aggregation
stop_monitor

# Final cost update
DONE_COUNT="$(find "$WORK_DIR/results" -maxdepth 1 -name '*.json' -not -path '*/logs/*' 2>/dev/null | wc -l | tr -d ' ')"
FINAL_COST="$(update_cost "$DONE_COUNT")"
log "INFO" "Final cost estimate: \$${FINAL_COST} for $DONE_COUNT files"

write_checkpoint "processing_complete" 0
log "INFO" "STAGE 2 [DONE]: Processing complete"

# ---------------------------------------------------------------------------
# STAGE 3: Aggregation
# ---------------------------------------------------------------------------
PIPELINE_STAGE="aggregation"
log "INFO" "STAGE 3 [START]: Result aggregation"

if [[ -f "$SCRIPT_DIR/03-aggregate-results.sh" ]]; then
    bash "$SCRIPT_DIR/03-aggregate-results.sh" \
        --results-dir "$WORK_DIR/results" \
        --output "$WORK_DIR/consolidated.json" \
        --summary-output "$WORK_DIR/summary.json" \
        --manifest "$MANIFEST" \
        --format json
else
    log "ERROR" "03-aggregate-results.sh not found in $SCRIPT_DIR"
    exit 1
fi

write_checkpoint "complete" 0
log "INFO" "STAGE 3 [DONE]: Aggregation complete"

# ---------------------------------------------------------------------------
# Final report
# ---------------------------------------------------------------------------
PIPELINE_STAGE="complete"

END_COST="$(jq -r '.total_cost_estimate' "$COST_FILE" 2>/dev/null || echo "N/A")"

log "INFO" "============================================"
log "INFO" "Pipeline complete"
log "INFO" "  Manifest:       $MANIFEST"
log "INFO" "  Results:        $WORK_DIR/results/"
log "INFO" "  Consolidated:   $WORK_DIR/consolidated.json"
log "INFO" "  Summary:        $WORK_DIR/summary.json"
log "INFO" "  Costs:          $COST_FILE"
log "INFO" "  Total cost:     \$${END_COST}"
log "INFO" "  Pipeline log:   $LOG_FILE"
log "INFO" "============================================"

# Notify on success
if [[ -n "$NOTIFY_CMD" ]]; then
    eval "$NOTIFY_CMD" 0 2>/dev/null || true
fi
