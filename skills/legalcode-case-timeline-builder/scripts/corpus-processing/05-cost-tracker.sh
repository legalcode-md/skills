#!/usr/bin/env bash
# ==============================================================================
# 05-cost-tracker.sh
#
# Standalone cost tracking and budget management for API-based document
# processing pipelines. Can be used independently or integrated with the
# parallel processing scripts.
#
# Usage:
#   # Initialize cost tracking for a run
#   ./05-cost-tracker.sh init --budget 100.00 --cost-per-file 0.03 --total-files 5000
#
#   # Record a processing event
#   ./05-cost-tracker.sh record --file-id abc123 --tokens-in 1500 --tokens-out 800
#
#   # Check current spend and remaining budget
#   ./05-cost-tracker.sh status
#
#   # Check if budget allows continuing
#   ./05-cost-tracker.sh check
#
#   # Generate cost report
#   ./05-cost-tracker.sh report
#
# Compatibility: macOS (BSD) and Linux (GNU)
# Dependencies: jq, bc
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
COST_DB="${COST_TRACKER_DB:-./cost-tracker.json}"

# API pricing (defaults for Claude API as of early 2025, override via env)
PRICE_INPUT_PER_1K="${PRICE_INPUT_PER_1K:-0.015}"       # $/1K input tokens
PRICE_OUTPUT_PER_1K="${PRICE_OUTPUT_PER_1K:-0.075}"      # $/1K output tokens
PRICE_PER_FILE="${PRICE_PER_FILE:-}"                     # Flat per-file cost (overrides token pricing)

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
    cat <<'USAGE'
Usage: 05-cost-tracker.sh <command> [OPTIONS]

Commands:
  init      Initialize a new cost tracking session
  record    Record a processing event (file processed)
  status    Show current spend and remaining budget
  check     Check if budget allows continuing (exit 0=ok, 1=exceeded)
  report    Generate detailed cost report
  estimate  Estimate cost before starting

Global options:
  --db FILE               Cost database file (default: ./cost-tracker.json or $COST_TRACKER_DB)

Init options:
  --budget AMOUNT         Total budget in dollars
  --cost-per-file AMOUNT  Flat cost per file (alternative to token pricing)
  --total-files N         Total files to process (for estimation)
  --model NAME            Model name (for logging)

Record options:
  --file-id ID            Unique file identifier
  --tokens-in N           Input tokens used
  --tokens-out N          Output tokens used
  --cost AMOUNT           Override: explicit cost for this file
  --duration SECS         Processing duration
  --status ok|error       Processing status

Estimate options:
  --total-files N         Number of files to estimate for
  --avg-tokens-in N       Average input tokens per file
  --avg-tokens-out N      Average output tokens per file

Environment variables:
  COST_TRACKER_DB         Path to cost database (default: ./cost-tracker.json)
  PRICE_INPUT_PER_1K      Price per 1K input tokens (default: 0.015)
  PRICE_OUTPUT_PER_1K     Price per 1K output tokens (default: 0.075)
  PRICE_PER_FILE          Flat per-file price (overrides token pricing)

Examples:
  # Set up budget for a run
  ./05-cost-tracker.sh init --budget 50.00 --total-files 2000

  # Record after processing each file
  ./05-cost-tracker.sh record --file-id doc_001 --tokens-in 2000 --tokens-out 500

  # Check budget before processing next batch
  ./05-cost-tracker.sh check && echo "Budget OK" || echo "Budget exceeded"

  # Estimate before starting
  ./05-cost-tracker.sh estimate --total-files 5000 --avg-tokens-in 3000 --avg-tokens-out 1000
USAGE
    exit 0
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
calc() {
    echo "scale=6; $1" | bc 2>/dev/null || echo "0"
}

calc_round() {
    echo "scale=2; $1" | bc 2>/dev/null || echo "0"
}

now_iso() {
    date -u '+%Y-%m-%dT%H:%M:%SZ'
}

# ---------------------------------------------------------------------------
# INIT: Create a new cost tracking session
# ---------------------------------------------------------------------------
cmd_init() {
    local budget=""
    local cost_per_file=""
    local total_files=""
    local model_name=""

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --budget)         budget="$2"; shift 2 ;;
            --cost-per-file)  cost_per_file="$2"; shift 2 ;;
            --total-files)    total_files="$2"; shift 2 ;;
            --model)          model_name="$2"; shift 2 ;;
            --db)             COST_DB="$2"; shift 2 ;;
            *)                echo "Unknown option for init: $1" >&2; exit 1 ;;
        esac
    done

    [[ -n "$cost_per_file" ]] && PRICE_PER_FILE="$cost_per_file"

    # Estimate total cost if we can
    local estimated_total="null"
    if [[ -n "$total_files" ]]; then
        if [[ -n "$PRICE_PER_FILE" ]]; then
            estimated_total="$(calc "$total_files * $PRICE_PER_FILE")"
        fi
    fi

    jq -n \
        --arg created "$(now_iso)" \
        --arg budget "${budget:-unlimited}" \
        --arg model "${model_name:-unknown}" \
        --arg price_in "$PRICE_INPUT_PER_1K" \
        --arg price_out "$PRICE_OUTPUT_PER_1K" \
        --arg price_file "${PRICE_PER_FILE:-null}" \
        --argjson total_files "${total_files:-null}" \
        --argjson estimated_total "$estimated_total" \
        '{
            session: {
                created_at: $created,
                budget_limit: $budget,
                model: $model,
                pricing: {
                    input_per_1k_tokens: ($price_in | tonumber),
                    output_per_1k_tokens: ($price_out | tonumber),
                    per_file: (if $price_file == "null" then null else ($price_file | tonumber) end)
                },
                total_files_expected: $total_files,
                estimated_total_cost: $estimated_total
            },
            totals: {
                files_processed: 0,
                files_succeeded: 0,
                files_failed: 0,
                total_input_tokens: 0,
                total_output_tokens: 0,
                total_cost: 0,
                last_updated: $created
            },
            events: []
        }' > "$COST_DB"

    echo "Cost tracker initialized: $COST_DB" >&2

    if [[ -n "$budget" && "$estimated_total" != "null" ]]; then
        local would_exceed
        would_exceed="$(echo "$estimated_total > ${budget}" | bc 2>/dev/null || echo "0")"
        if [[ "$would_exceed" == "1" ]]; then
            echo "WARNING: Estimated cost \$${estimated_total} exceeds budget \$${budget}" >&2
        else
            echo "Estimated cost: \$${estimated_total} (budget: \$${budget})" >&2
        fi
    fi
}

# ---------------------------------------------------------------------------
# RECORD: Log a processing event
# ---------------------------------------------------------------------------
cmd_record() {
    local file_id=""
    local tokens_in=0
    local tokens_out=0
    local explicit_cost=""
    local duration=0
    local status="ok"

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --file-id)    file_id="$2"; shift 2 ;;
            --tokens-in)  tokens_in="$2"; shift 2 ;;
            --tokens-out) tokens_out="$2"; shift 2 ;;
            --cost)       explicit_cost="$2"; shift 2 ;;
            --duration)   duration="$2"; shift 2 ;;
            --status)     status="$2"; shift 2 ;;
            --db)         COST_DB="$2"; shift 2 ;;
            *)            echo "Unknown option for record: $1" >&2; exit 1 ;;
        esac
    done

    if [[ -z "$file_id" ]]; then
        echo "Error: --file-id is required for record" >&2
        exit 1
    fi

    if [[ ! -f "$COST_DB" ]]; then
        echo "Error: cost database not found: $COST_DB (run init first)" >&2
        exit 1
    fi

    # Calculate cost for this event
    local event_cost
    if [[ -n "$explicit_cost" ]]; then
        event_cost="$explicit_cost"
    elif [[ -n "$PRICE_PER_FILE" ]]; then
        event_cost="$PRICE_PER_FILE"
    else
        local input_cost output_cost
        input_cost="$(calc "$tokens_in * $PRICE_INPUT_PER_1K / 1000")"
        output_cost="$(calc "$tokens_out * $PRICE_OUTPUT_PER_1K / 1000")"
        event_cost="$(calc "$input_cost + $output_cost")"
    fi

    # Append event and update totals
    jq \
        --arg file_id "$file_id" \
        --argjson tokens_in "$tokens_in" \
        --argjson tokens_out "$tokens_out" \
        --argjson cost "$event_cost" \
        --argjson duration "$duration" \
        --arg status "$status" \
        --arg ts "$(now_iso)" \
        '
        .events += [{
            file_id: $file_id,
            timestamp: $ts,
            input_tokens: $tokens_in,
            output_tokens: $tokens_out,
            cost: ($cost | tonumber),
            duration_seconds: $duration,
            status: $status
        }] |
        .totals.files_processed += 1 |
        .totals.total_input_tokens += $tokens_in |
        .totals.total_output_tokens += $tokens_out |
        .totals.total_cost += ($cost | tonumber) |
        .totals.last_updated = $ts |
        if $status == "ok" then .totals.files_succeeded += 1
        else .totals.files_failed += 1 end
        ' "$COST_DB" > "${COST_DB}.tmp" && mv "${COST_DB}.tmp" "$COST_DB"
}

# ---------------------------------------------------------------------------
# STATUS: Show current spend
# ---------------------------------------------------------------------------
cmd_status() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --db) COST_DB="$2"; shift 2 ;;
            *)    shift ;;
        esac
    done

    if [[ ! -f "$COST_DB" ]]; then
        echo "Error: cost database not found: $COST_DB" >&2
        exit 1
    fi

    jq '
    {
        budget_limit: .session.budget_limit,
        total_cost: (.totals.total_cost | . * 100 | round / 100),
        files_processed: .totals.files_processed,
        files_succeeded: .totals.files_succeeded,
        files_failed: .totals.files_failed,
        total_input_tokens: .totals.total_input_tokens,
        total_output_tokens: .totals.total_output_tokens,
        remaining_budget: (
            if .session.budget_limit == "unlimited" then "unlimited"
            else ((.session.budget_limit | tonumber) - .totals.total_cost) | . * 100 | round / 100
            end
        ),
        budget_used_pct: (
            if .session.budget_limit == "unlimited" then "N/A"
            else (.totals.total_cost / (.session.budget_limit | tonumber) * 100) | . * 10 | round / 10 | tostring + "%"
            end
        ),
        avg_cost_per_file: (
            if .totals.files_processed > 0 then
                (.totals.total_cost / .totals.files_processed) | . * 10000 | round / 10000
            else 0 end
        ),
        estimated_remaining_cost: (
            if .session.total_files_expected != null and .totals.files_processed > 0 then
                ((.session.total_files_expected - .totals.files_processed) *
                 (.totals.total_cost / .totals.files_processed)) | . * 100 | round / 100
            else null end
        )
    }' "$COST_DB"
}

# ---------------------------------------------------------------------------
# CHECK: Budget gate (exit 0 = ok, exit 1 = exceeded)
# ---------------------------------------------------------------------------
cmd_check() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --db) COST_DB="$2"; shift 2 ;;
            *)    shift ;;
        esac
    done

    if [[ ! -f "$COST_DB" ]]; then
        echo "Error: cost database not found: $COST_DB" >&2
        exit 1
    fi

    local budget
    budget="$(jq -r '.session.budget_limit' "$COST_DB")"

    if [[ "$budget" == "unlimited" ]]; then
        echo "OK: no budget limit set" >&2
        exit 0
    fi

    local current_cost
    current_cost="$(jq '.totals.total_cost' "$COST_DB")"

    local exceeded
    exceeded="$(echo "$current_cost >= $budget" | bc 2>/dev/null || echo "0")"

    if [[ "$exceeded" == "1" ]]; then
        echo "EXCEEDED: \$${current_cost} >= \$${budget}" >&2
        exit 1
    fi

    # Warn at 80%
    local pct
    pct="$(calc_round "$current_cost / $budget * 100")"
    local is_warning
    is_warning="$(echo "$pct >= 80" | bc 2>/dev/null || echo "0")"

    if [[ "$is_warning" == "1" ]]; then
        echo "WARNING: ${pct}% of budget used (\$${current_cost} / \$${budget})" >&2
    else
        echo "OK: ${pct}% of budget used (\$${current_cost} / \$${budget})" >&2
    fi

    exit 0
}

# ---------------------------------------------------------------------------
# ESTIMATE: Project costs before starting
# ---------------------------------------------------------------------------
cmd_estimate() {
    local total_files=""
    local avg_tokens_in=2000
    local avg_tokens_out=500

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --total-files)    total_files="$2"; shift 2 ;;
            --avg-tokens-in)  avg_tokens_in="$2"; shift 2 ;;
            --avg-tokens-out) avg_tokens_out="$2"; shift 2 ;;
            --db)             COST_DB="$2"; shift 2 ;;
            *)                echo "Unknown option for estimate: $1" >&2; exit 1 ;;
        esac
    done

    if [[ -z "$total_files" ]]; then
        echo "Error: --total-files is required" >&2
        exit 1
    fi

    local per_file_input per_file_output per_file_total
    local total_input_cost total_output_cost total_cost

    if [[ -n "$PRICE_PER_FILE" ]]; then
        per_file_total="$PRICE_PER_FILE"
        total_cost="$(calc "$total_files * $PRICE_PER_FILE")"

        jq -n \
            --argjson files "$total_files" \
            --argjson per_file "$per_file_total" \
            --argjson total "$total_cost" \
            '{
                estimate: {
                    total_files: $files,
                    cost_per_file: ($per_file | . * 10000 | round / 10000),
                    total_estimated_cost: ($total | . * 100 | round / 100),
                    pricing_model: "per_file"
                }
            }'
    else
        per_file_input="$(calc "$avg_tokens_in * $PRICE_INPUT_PER_1K / 1000")"
        per_file_output="$(calc "$avg_tokens_out * $PRICE_OUTPUT_PER_1K / 1000")"
        per_file_total="$(calc "$per_file_input + $per_file_output")"

        total_input_cost="$(calc "$total_files * $per_file_input")"
        total_output_cost="$(calc "$total_files * $per_file_output")"
        total_cost="$(calc "$total_input_cost + $total_output_cost")"

        local total_tokens
        total_tokens="$(calc "$total_files * ($avg_tokens_in + $avg_tokens_out)")"

        jq -n \
            --argjson files "$total_files" \
            --argjson avg_in "$avg_tokens_in" \
            --argjson avg_out "$avg_tokens_out" \
            --argjson per_file_in "$per_file_input" \
            --argjson per_file_out "$per_file_output" \
            --argjson per_file_total "$per_file_total" \
            --argjson total_in_cost "$total_input_cost" \
            --argjson total_out_cost "$total_output_cost" \
            --argjson total_cost "$total_cost" \
            --argjson total_tokens "$total_tokens" \
            --arg price_in "$PRICE_INPUT_PER_1K" \
            --arg price_out "$PRICE_OUTPUT_PER_1K" \
            '{
                estimate: {
                    total_files: $files,
                    pricing_model: "per_token",
                    pricing: {
                        input_per_1k: ($price_in | tonumber),
                        output_per_1k: ($price_out | tonumber)
                    },
                    per_file: {
                        avg_input_tokens: $avg_in,
                        avg_output_tokens: $avg_out,
                        input_cost: ($per_file_in | . * 10000 | round / 10000),
                        output_cost: ($per_file_out | . * 10000 | round / 10000),
                        total_cost: ($per_file_total | . * 10000 | round / 10000)
                    },
                    totals: {
                        input_cost: ($total_in_cost | . * 100 | round / 100),
                        output_cost: ($total_out_cost | . * 100 | round / 100),
                        total_cost: ($total_cost | . * 100 | round / 100),
                        total_tokens: ($total_tokens | floor)
                    }
                }
            }'
    fi
}

# ---------------------------------------------------------------------------
# REPORT: Detailed cost report
# ---------------------------------------------------------------------------
cmd_report() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --db) COST_DB="$2"; shift 2 ;;
            *)    shift ;;
        esac
    done

    if [[ ! -f "$COST_DB" ]]; then
        echo "Error: cost database not found: $COST_DB" >&2
        exit 1
    fi

    jq '
    {
        session_info: {
            created: .session.created_at,
            model: .session.model,
            budget: .session.budget_limit,
            expected_files: .session.total_files_expected
        },
        cost_summary: {
            total_cost: (.totals.total_cost | . * 100 | round / 100),
            avg_per_file: (
                if .totals.files_processed > 0 then
                    (.totals.total_cost / .totals.files_processed) | . * 10000 | round / 10000
                else 0 end
            ),
            total_input_tokens: .totals.total_input_tokens,
            total_output_tokens: .totals.total_output_tokens,
            avg_input_tokens: (
                if .totals.files_processed > 0 then
                    (.totals.total_input_tokens / .totals.files_processed) | floor
                else 0 end
            ),
            avg_output_tokens: (
                if .totals.files_processed > 0 then
                    (.totals.total_output_tokens / .totals.files_processed) | floor
                else 0 end
            )
        },
        processing_summary: {
            total_files: .totals.files_processed,
            succeeded: .totals.files_succeeded,
            failed: .totals.files_failed,
            success_rate: (
                if .totals.files_processed > 0 then
                    ((.totals.files_succeeded / .totals.files_processed * 100) | . * 10 | round / 10 | tostring + "%")
                else "N/A" end
            )
        },
        budget_status: (
            if .session.budget_limit == "unlimited" then
                { status: "no_limit", remaining: "unlimited" }
            else {
                status: (
                    if .totals.total_cost >= (.session.budget_limit | tonumber) then "exceeded"
                    elif .totals.total_cost >= (.session.budget_limit | tonumber) * 0.8 then "warning"
                    else "ok" end
                ),
                limit: (.session.budget_limit | tonumber),
                spent: (.totals.total_cost | . * 100 | round / 100),
                remaining: (((.session.budget_limit | tonumber) - .totals.total_cost) | . * 100 | round / 100),
                used_pct: ((.totals.total_cost / (.session.budget_limit | tonumber) * 100) | . * 10 | round / 10)
            } end
        ),
        cost_distribution: {
            p50_cost: (
                [.events[].cost] | sort |
                if length > 0 then .[length / 2 | floor] | . * 10000 | round / 10000
                else null end
            ),
            p90_cost: (
                [.events[].cost] | sort |
                if length > 0 then .[(length * 0.9) | floor] | . * 10000 | round / 10000
                else null end
            ),
            p99_cost: (
                [.events[].cost] | sort |
                if length > 0 then .[(length * 0.99) | floor] | . * 10000 | round / 10000
                else null end
            ),
            max_cost: (
                [.events[].cost] |
                if length > 0 then max | . * 10000 | round / 10000
                else null end
            )
        },
        timing_distribution: {
            avg_duration_seconds: (
                [.events[].duration_seconds | select(. > 0)] |
                if length > 0 then (add / length) | . * 10 | round / 10
                else null end
            ),
            max_duration_seconds: (
                [.events[].duration_seconds] |
                if length > 0 then max
                else null end
            )
        },
        top_expensive_files: (
            [.events[] | {file_id, cost, input_tokens, output_tokens}] |
            sort_by(-.cost) | .[0:10]
        )
    }' "$COST_DB"
}

# ---------------------------------------------------------------------------
# Main dispatch
# ---------------------------------------------------------------------------
COMMAND="${1:-}"
shift || true

case "$COMMAND" in
    init)     cmd_init "$@" ;;
    record)   cmd_record "$@" ;;
    status)   cmd_status "$@" ;;
    check)    cmd_check "$@" ;;
    estimate) cmd_estimate "$@" ;;
    report)   cmd_report "$@" ;;
    -h|--help|"") usage ;;
    *)
        echo "Unknown command: $COMMAND" >&2
        echo "Run with --help for usage" >&2
        exit 1
        ;;
esac
