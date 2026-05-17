#!/usr/bin/env bash
# ==============================================================================
# example-processor.sh
#
# Example processor script that demonstrates the contract expected by
# 02-parallel-process.sh. Replace the body with your actual processing logic
# (e.g., calling an LLM API, running OCR, extracting text, etc.).
#
# Contract:
#   $1 = absolute path to the file to process
#   $2 = results directory (write your JSON output here)
#   $3 = unique file ID (use as the output filename stem)
#
#   MUST write: $2/$3.json
#   MUST exit 0 on success, non-zero on failure
#
# ==============================================================================
set -euo pipefail

FILEPATH="$1"
RESULTS_DIR="$2"
FILE_ID="$3"

OUTPUT="$RESULTS_DIR/${FILE_ID}.json"
ERROR_OUTPUT="$RESULTS_DIR/${FILE_ID}.error.json"

# ---------------------------------------------------------------------------
# Example 1: Basic metadata extraction
# ---------------------------------------------------------------------------
extract_metadata() {
    local filepath="$1"
    local filename
    filename="$(basename "$filepath")"
    local ext="${filename##*.}"
    local mime
    mime="$(file --brief --mime-type "$filepath" 2>/dev/null || echo "unknown")"
    local size
    if stat --version >/dev/null 2>&1; then
        size="$(stat -c '%s' "$filepath")"
    else
        size="$(stat -f '%z' "$filepath")"
    fi

    # Page/word count heuristics (extend per type)
    local page_count=0
    local word_count=0

    case "$(echo "$ext" | tr '[:upper:]' '[:lower:]')" in
        pdf)
            # Extract page count from PDF (requires no extra dependencies)
            page_count="$(strings "$filepath" 2>/dev/null | grep -c '/Type\s*/Page' || echo "0")"
            ;;
        txt|md|csv)
            word_count="$(wc -w < "$filepath" | tr -d ' ')"
            ;;
    esac

    jq -n \
        --arg file "$filepath" \
        --arg filename "$filename" \
        --arg ext "$ext" \
        --arg mime "$mime" \
        --argjson size "$size" \
        --argjson pages "$page_count" \
        --argjson words "$word_count" \
        --arg processed_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
        --arg status "ok" \
        '{
            file: $file,
            filename: $filename,
            extension: $ext,
            mime_type: $mime,
            size_bytes: $size,
            page_count: $pages,
            word_count: $words,
            processed_at: $processed_at,
            status: $status
        }'
}

# ---------------------------------------------------------------------------
# Example 2: API-based processing with cost tracking integration
# (Uncomment and adapt for your use case)
# ---------------------------------------------------------------------------
# process_with_api() {
#     local filepath="$1"
#     local file_id="$2"
#
#     # Extract text content (adapt per file type)
#     local content
#     content="$(cat "$filepath" | head -c 100000)"  # First 100KB
#
#     # Call API (example with curl to Claude/OpenAI-compatible API)
#     local response
#     response="$(curl -s --max-time 120 \
#         -H "Authorization: Bearer $API_KEY" \
#         -H "Content-Type: application/json" \
#         -d "$(jq -n \
#             --arg content "$content" \
#             '{
#                 model: "claude-sonnet-4-20250514",
#                 max_tokens: 4096,
#                 messages: [{
#                     role: "user",
#                     content: ("Analyze the following document and extract: 1) document type, 2) key parties, 3) key dates, 4) risk level (low/medium/high), 5) brief summary.\n\nDocument:\n" + $content)
#                 }]
#             }')" \
#         "https://api.anthropic.com/v1/messages")"
#
#     # Extract usage for cost tracking
#     local input_tokens output_tokens
#     input_tokens="$(echo "$response" | jq '.usage.input_tokens // 0')"
#     output_tokens="$(echo "$response" | jq '.usage.output_tokens // 0')"
#
#     # Record cost (integrates with 05-cost-tracker.sh)
#     if [[ -n "${COST_TRACKER_DB:-}" ]]; then
#         ./05-cost-tracker.sh record \
#             --file-id "$file_id" \
#             --tokens-in "$input_tokens" \
#             --tokens-out "$output_tokens" \
#             --status "ok"
#     fi
#
#     # Extract and structure the analysis
#     local analysis
#     analysis="$(echo "$response" | jq -r '.content[0].text // "extraction_failed"')"
#
#     jq -n \
#         --arg file "$filepath" \
#         --arg analysis "$analysis" \
#         --argjson input_tokens "$input_tokens" \
#         --argjson output_tokens "$output_tokens" \
#         --arg status "ok" \
#         '{
#             file: $file,
#             analysis: $analysis,
#             tokens: { input: $input_tokens, output: $output_tokens },
#             status: $status,
#             processed_at: (now | todate)
#         }'
# }

# ---------------------------------------------------------------------------
# Main: process the file and write output
# ---------------------------------------------------------------------------
main() {
    # Validate input
    if [[ ! -f "$FILEPATH" ]]; then
        jq -n \
            --arg file "$FILEPATH" \
            --arg error "File not found" \
            '{ file: $file, status: "error", error: $error }' > "$ERROR_OUTPUT"
        exit 1
    fi

    # Process (swap in your processor function here)
    local result
    if result="$(extract_metadata "$FILEPATH")"; then
        echo "$result" > "$OUTPUT"
        exit 0
    else
        jq -n \
            --arg file "$FILEPATH" \
            --arg error "Processing failed" \
            '{ file: $file, status: "error", error: $error }' > "$ERROR_OUTPUT"
        exit 1
    fi
}

main
