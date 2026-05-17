#!/usr/bin/env bash
# ==============================================================================
# 02-parallel-process.sh
#
# Processes files from a manifest in parallel using one of three strategies:
#   1. xargs -P (POSIX, works everywhere)
#   2. GNU parallel (rich features, job logging)
#   3. Bash background jobs with wait (no dependencies)
#
# Each file is processed by a user-supplied "processor" script/command that
# receives the file path and writes a JSON result to a results directory.
#
# Usage:
#   ./02-parallel-process.sh \
#       --manifest manifest.json \
#       --processor ./my-processor.sh \
#       --results-dir ./results \
#       --jobs 8 \
#       --strategy xargs|parallel|background \
#       [--timeout 300] \
#       [--retry 2] \
#       [--resume]
#
# Compatibility: macOS (BSD) and Linux (GNU)
# Dependencies: jq (for manifest parsing), and optionally GNU parallel
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
MANIFEST=""
PROCESSOR=""
RESULTS_DIR="./results"
JOBS=4
STRATEGY="xargs"       # xargs | parallel | background
TIMEOUT=300             # seconds per file
MAX_RETRIES=0
RESUME=false
LOG_DIR=""
DRY_RUN=false

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
    cat <<'USAGE'
Usage: 02-parallel-process.sh [OPTIONS]

Required:
  --manifest FILE         Path to manifest.json from discovery step
  --processor CMD         Command/script to process each file
                          Receives: $1=filepath $2=results_dir $3=file_id

Options:
  --results-dir DIR       Directory for per-file JSON results (default: ./results)
  --jobs N                Number of parallel jobs (default: 4)
  --strategy STR          Parallelism strategy: xargs, parallel, background (default: xargs)
  --timeout SECS          Timeout per file in seconds (default: 300)
  --retry N               Max retries on failure (default: 0)
  --resume                Skip files that already have results
  --log-dir DIR           Directory for logs (default: results-dir/logs)
  --dry-run               Print what would be processed without running
  -h, --help              Show this help

Processor contract:
  Your processor script receives three arguments:
    $1 = absolute path to the file
    $2 = results directory
    $3 = unique file ID (safe filename derived from path hash)

  It MUST:
    - Write a JSON file to: $2/$3.json
    - Exit 0 on success, non-zero on failure

  Example processor:
    #!/usr/bin/env bash
    echo '{"file":"'"$1"'","status":"ok","extracted":"..."}' > "$2/$3.json"
USAGE
    exit 0
}

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)        usage ;;
        --manifest)       MANIFEST="$2"; shift 2 ;;
        --processor)      PROCESSOR="$2"; shift 2 ;;
        --results-dir)    RESULTS_DIR="$2"; shift 2 ;;
        --jobs)           JOBS="$2"; shift 2 ;;
        --strategy)       STRATEGY="$2"; shift 2 ;;
        --timeout)        TIMEOUT="$2"; shift 2 ;;
        --retry)          MAX_RETRIES="$2"; shift 2 ;;
        --resume)         RESUME=true; shift ;;
        --log-dir)        LOG_DIR="$2"; shift 2 ;;
        --dry-run)        DRY_RUN=true; shift ;;
        *)                echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
if [[ -z "$MANIFEST" || -z "$PROCESSOR" ]]; then
    echo "Error: --manifest and --processor are required." >&2
    exit 1
fi

if [[ ! -f "$MANIFEST" ]]; then
    echo "Error: manifest file not found: $MANIFEST" >&2
    exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq is required but not installed." >&2
    exit 1
fi

mkdir -p "$RESULTS_DIR"
[[ -z "$LOG_DIR" ]] && LOG_DIR="$RESULTS_DIR/logs"
mkdir -p "$LOG_DIR"

# ---------------------------------------------------------------------------
# Generate file ID from path (portable, no md5sum dependency issues)
# ---------------------------------------------------------------------------
file_id() {
    # Create a safe filename from the file path using shasum
    echo -n "$1" | shasum -a 256 | cut -c1-16
}

# ---------------------------------------------------------------------------
# Extract file list from manifest
# ---------------------------------------------------------------------------
echo "Loading manifest: $MANIFEST" >&2

FILELIST="$(mktemp)"
trap 'rm -f "$FILELIST" 2>/dev/null' EXIT

# Extract absolute paths from manifest JSON
jq -r '.files[]?.absolute_path // empty' "$MANIFEST" > "$FILELIST"

TOTAL_FILES="$(wc -l < "$FILELIST" | tr -d ' ')"
echo "Total files in manifest: $TOTAL_FILES" >&2

# ---------------------------------------------------------------------------
# Filter for resume (skip already-processed files)
# ---------------------------------------------------------------------------
if [[ "$RESUME" == true ]]; then
    FILTERED="$(mktemp)"
    SKIPPED=0
    while IFS= read -r fpath; do
        fid="$(file_id "$fpath")"
        if [[ -f "$RESULTS_DIR/${fid}.json" ]]; then
            SKIPPED=$((SKIPPED + 1))
        else
            echo "$fpath" >> "$FILTERED"
        fi
    done < "$FILELIST"
    mv "$FILTERED" "$FILELIST"
    REMAINING="$(wc -l < "$FILELIST" | tr -d ' ')"
    echo "Resume mode: skipping $SKIPPED already-processed, $REMAINING remaining" >&2
else
    REMAINING="$TOTAL_FILES"
fi

if [[ "$REMAINING" -eq 0 ]]; then
    echo "Nothing to process." >&2
    exit 0
fi

# ---------------------------------------------------------------------------
# Dry run
# ---------------------------------------------------------------------------
if [[ "$DRY_RUN" == true ]]; then
    echo "" >&2
    echo "=== DRY RUN ===" >&2
    echo "Would process $REMAINING files with:" >&2
    echo "  Strategy:  $STRATEGY" >&2
    echo "  Jobs:      $JOBS" >&2
    echo "  Timeout:   ${TIMEOUT}s" >&2
    echo "  Retries:   $MAX_RETRIES" >&2
    echo "  Processor: $PROCESSOR" >&2
    echo "" >&2
    echo "First 10 files:" >&2
    head -10 "$FILELIST" | while read -r f; do
        echo "  $f" >&2
    done
    exit 0
fi

# ---------------------------------------------------------------------------
# Progress tracking setup
# ---------------------------------------------------------------------------
PROGRESS_FILE="$LOG_DIR/progress.log"
ERROR_FILE="$LOG_DIR/errors.log"
TIMING_FILE="$LOG_DIR/timing.log"

echo "0" > "$PROGRESS_FILE"
: > "$ERROR_FILE"
: > "$TIMING_FILE"

START_TIME="$(date +%s)"

# ---------------------------------------------------------------------------
# Wrapper that handles timeout, retry, logging, and progress
# ---------------------------------------------------------------------------
WRAPPER_SCRIPT="$(mktemp)"
cat > "$WRAPPER_SCRIPT" << 'WRAPPER_EOF'
#!/usr/bin/env bash
set -uo pipefail

FILEPATH="$1"
PROCESSOR="$2"
RESULTS_DIR="$3"
TIMEOUT="$4"
MAX_RETRIES="$5"
LOG_DIR="$6"
TOTAL="$7"

# File ID
FILE_ID="$(echo -n "$FILEPATH" | shasum -a 256 | cut -c1-16)"

# Retry loop
attempt=0
success=false
while [[ $attempt -le $MAX_RETRIES ]]; do
    attempt=$((attempt + 1))

    file_start="$(date +%s)"

    # Run processor with timeout
    if command -v timeout >/dev/null 2>&1; then
        # GNU timeout available
        timeout "$TIMEOUT" "$PROCESSOR" "$FILEPATH" "$RESULTS_DIR" "$FILE_ID" \
            > "$LOG_DIR/${FILE_ID}.stdout" 2> "$LOG_DIR/${FILE_ID}.stderr"
        exit_code=$?
    else
        # macOS: use perl-based timeout
        perl -e '
            alarm shift @ARGV;
            $SIG{ALRM} = sub { kill 9, $pid; exit 124 };
            $pid = fork;
            if ($pid == 0) { exec @ARGV; die "exec failed: $!" }
            waitpid($pid, 0);
            exit($? >> 8);
        ' "$TIMEOUT" "$PROCESSOR" "$FILEPATH" "$RESULTS_DIR" "$FILE_ID" \
            > "$LOG_DIR/${FILE_ID}.stdout" 2> "$LOG_DIR/${FILE_ID}.stderr"
        exit_code=$?
    fi

    file_end="$(date +%s)"
    duration=$((file_end - file_start))

    if [[ $exit_code -eq 0 && -f "$RESULTS_DIR/${FILE_ID}.json" ]]; then
        success=true
        echo "${FILE_ID}|${FILEPATH}|${duration}s|attempt=${attempt}|ok" >> "$LOG_DIR/timing.log"
        break
    fi

    if [[ $exit_code -eq 124 ]]; then
        echo "${FILE_ID}|${FILEPATH}|TIMEOUT after ${TIMEOUT}s|attempt=${attempt}" >> "$LOG_DIR/errors.log"
    else
        echo "${FILE_ID}|${FILEPATH}|exit=${exit_code}|attempt=${attempt}" >> "$LOG_DIR/errors.log"
    fi

    if [[ $attempt -le $MAX_RETRIES ]]; then
        # Exponential backoff: 1s, 2s, 4s ...
        sleep_time=$((1 << (attempt - 1)))
        sleep "$sleep_time"
    fi
done

# Update progress counter (atomic-ish with file lock)
if command -v flock >/dev/null 2>&1; then
    flock "$LOG_DIR/progress.lock" bash -c "
        count=\$(cat '$LOG_DIR/progress.log')
        count=\$((count + 1))
        echo \$count > '$LOG_DIR/progress.log'
        echo -ne \"\\r  Progress: \$count / $TOTAL\" >&2
    "
else
    # macOS fallback: no flock, accept minor race condition on display
    count="$(cat "$LOG_DIR/progress.log")"
    count=$((count + 1))
    echo "$count" > "$LOG_DIR/progress.log"
    echo -ne "\r  Progress: $count / $TOTAL" >&2
fi

if [[ "$success" != true ]]; then
    exit 1
fi
WRAPPER_EOF
chmod +x "$WRAPPER_SCRIPT"

# ---------------------------------------------------------------------------
# Strategy 1: xargs -P
# ---------------------------------------------------------------------------
run_xargs() {
    echo "" >&2
    echo "=== Running with xargs -P $JOBS ===" >&2
    echo "" >&2

    cat "$FILELIST" | xargs -P "$JOBS" -I {} \
        bash "$WRAPPER_SCRIPT" {} "$PROCESSOR" "$RESULTS_DIR" "$TIMEOUT" "$MAX_RETRIES" "$LOG_DIR" "$REMAINING"

    echo "" >&2
}

# ---------------------------------------------------------------------------
# Strategy 2: GNU parallel
# ---------------------------------------------------------------------------
run_parallel() {
    if ! command -v parallel >/dev/null 2>&1; then
        echo "Error: GNU parallel not installed. Install with:" >&2
        echo "  macOS:  brew install parallel" >&2
        echo "  Debian: sudo apt install parallel" >&2
        exit 1
    fi

    echo "" >&2
    echo "=== Running with GNU parallel -j $JOBS ===" >&2
    echo "" >&2

    JOB_LOG="$LOG_DIR/parallel-joblog.tsv"

    parallel \
        --jobs "$JOBS" \
        --bar \
        --joblog "$JOB_LOG" \
        --resume-failed \
        --retries "$MAX_RETRIES" \
        --timeout "$TIMEOUT" \
        --halt soon,fail=10% \
        bash "$WRAPPER_SCRIPT" {} "$PROCESSOR" "$RESULTS_DIR" "$TIMEOUT" "$MAX_RETRIES" "$LOG_DIR" "$REMAINING" \
        :::: "$FILELIST"

    echo "" >&2
    echo "Job log written to: $JOB_LOG" >&2
}

# ---------------------------------------------------------------------------
# Strategy 3: Bash background jobs with wait
# ---------------------------------------------------------------------------
run_background() {
    echo "" >&2
    echo "=== Running with bash background jobs (max $JOBS concurrent) ===" >&2
    echo "" >&2

    ACTIVE_PIDS=()
    FAILED_COUNT=0

    while IFS= read -r fpath; do
        # Throttle: if we have $JOBS active, wait for one to finish
        while [[ ${#ACTIVE_PIDS[@]} -ge $JOBS ]]; do
            # Wait for any one child
            NEW_PIDS=()
            for pid in "${ACTIVE_PIDS[@]}"; do
                if kill -0 "$pid" 2>/dev/null; then
                    NEW_PIDS+=("$pid")
                else
                    wait "$pid" || FAILED_COUNT=$((FAILED_COUNT + 1))
                fi
            done
            if [[ ${#NEW_PIDS[@]} -ge $JOBS ]]; then
                # All still running, brief sleep to avoid busy-wait
                sleep 0.1
            fi
            ACTIVE_PIDS=("${NEW_PIDS[@]+"${NEW_PIDS[@]}"}")
        done

        # Launch in background
        bash "$WRAPPER_SCRIPT" "$fpath" "$PROCESSOR" "$RESULTS_DIR" "$TIMEOUT" "$MAX_RETRIES" "$LOG_DIR" "$REMAINING" &
        ACTIVE_PIDS+=($!)

    done < "$FILELIST"

    # Wait for all remaining
    for pid in "${ACTIVE_PIDS[@]+"${ACTIVE_PIDS[@]}"}"; do
        wait "$pid" || FAILED_COUNT=$((FAILED_COUNT + 1))
    done

    echo "" >&2
    echo "Background jobs completed. Failures: $FAILED_COUNT" >&2
}

# ---------------------------------------------------------------------------
# Run selected strategy
# ---------------------------------------------------------------------------
case "$STRATEGY" in
    xargs)      run_xargs ;;
    parallel)   run_parallel ;;
    background) run_background ;;
    *)
        echo "Error: unknown strategy '$STRATEGY'. Use: xargs, parallel, background" >&2
        exit 1
        ;;
esac

# ---------------------------------------------------------------------------
# Final summary
# ---------------------------------------------------------------------------
END_TIME="$(date +%s)"
ELAPSED=$((END_TIME - START_TIME))

COMPLETED="$(find "$RESULTS_DIR" -maxdepth 1 -name '*.json' | wc -l | tr -d ' ')"
ERRORS="$(wc -l < "$ERROR_FILE" | tr -d ' ')"

echo "" >&2
echo "=== Processing Summary ===" >&2
echo "  Total files:     $REMAINING" >&2
echo "  Completed:       $COMPLETED" >&2
echo "  Errors:          $ERRORS" >&2
echo "  Elapsed:         ${ELAPSED}s" >&2
echo "  Results dir:     $RESULTS_DIR" >&2
echo "  Error log:       $ERROR_FILE" >&2
echo "  Timing log:      $TIMING_FILE" >&2

if [[ "$ERRORS" -gt 0 ]]; then
    echo "" >&2
    echo "  Failed files (first 10):" >&2
    head -10 "$ERROR_FILE" | while IFS='|' read -r fid fpath detail attempt_info; do
        echo "    $fpath ($detail)" >&2
    done
fi

# Cleanup wrapper
rm -f "$WRAPPER_SCRIPT"

echo "" >&2
echo "Done." >&2
