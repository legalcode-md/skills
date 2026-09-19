#!/usr/bin/env bash
# ==============================================================================
# 03-aggregate-results.sh
#
# Merges per-file JSON results from the parallel processing step into a single
# consolidated output. Generates summary statistics, handles deduplication,
# and produces both detailed and summary reports.
#
# Usage:
#   ./03-aggregate-results.sh \
#       --results-dir ./results \
#       --output consolidated.json \
#       [--summary-output summary.json] \
#       [--sort-by field] \
#       [--dedup-key field] \
#       [--format json|jsonl|csv]
#
# Compatibility: macOS (BSD) and Linux (GNU)
# Dependencies: jq
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
RESULTS_DIR=""
OUTPUT_FILE="consolidated.json"
SUMMARY_FILE=""
SORT_BY=""
DEDUP_KEY=""
FORMAT="json"
INCLUDE_ERRORS=false
MANIFEST_FILE=""

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
    cat <<'USAGE'
Usage: 03-aggregate-results.sh [OPTIONS]

Required:
  --results-dir DIR       Directory containing per-file JSON results

Options:
  --output FILE           Consolidated output file (default: consolidated.json)
  --summary-output FILE   Separate summary statistics file
  --sort-by FIELD         Sort results by this JSON field (e.g., "file", "risk_score")
  --dedup-key FIELD       Deduplicate results by this JSON field
  --format json|jsonl|csv Output format (default: json)
  --include-errors        Include error results in output (default: skip)
  --manifest FILE         Cross-reference with original manifest for completeness check
  -h, --help              Show this help

The script expects each .json file in results-dir to contain a single JSON object.
Files named *.error.json are treated as error results.
USAGE
    exit 0
}

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)           usage ;;
        --results-dir)       RESULTS_DIR="$2"; shift 2 ;;
        --output)            OUTPUT_FILE="$2"; shift 2 ;;
        --summary-output)    SUMMARY_FILE="$2"; shift 2 ;;
        --sort-by)           SORT_BY="$2"; shift 2 ;;
        --dedup-key)         DEDUP_KEY="$2"; shift 2 ;;
        --format)            FORMAT="$2"; shift 2 ;;
        --include-errors)    INCLUDE_ERRORS=true; shift ;;
        --manifest)          MANIFEST_FILE="$2"; shift 2 ;;
        *)                   echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

if [[ -z "$RESULTS_DIR" ]]; then
    echo "Error: --results-dir is required." >&2
    exit 1
fi

if [[ ! -d "$RESULTS_DIR" ]]; then
    echo "Error: results directory not found: $RESULTS_DIR" >&2
    exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq is required but not installed." >&2
    exit 1
fi

# ---------------------------------------------------------------------------
# Count and validate result files
# ---------------------------------------------------------------------------
echo "Aggregating results from: $RESULTS_DIR" >&2

RESULT_FILES=()
ERROR_FILES=()

while IFS= read -r f; do
    if [[ "$(basename "$f")" == *.error.json ]]; then
        ERROR_FILES+=("$f")
    else
        RESULT_FILES+=("$f")
    fi
done < <(find "$RESULTS_DIR" -maxdepth 1 -name '*.json' -type f | sort)

echo "  Result files: ${#RESULT_FILES[@]}" >&2
echo "  Error files:  ${#ERROR_FILES[@]}" >&2

if [[ ${#RESULT_FILES[@]} -eq 0 ]]; then
    echo "Error: no result files found in $RESULTS_DIR" >&2
    exit 1
fi

# ---------------------------------------------------------------------------
# Validate JSON files (skip malformed ones)
# ---------------------------------------------------------------------------
VALID_FILES=()
MALFORMED=0

for f in "${RESULT_FILES[@]}"; do
    if jq empty "$f" 2>/dev/null; then
        VALID_FILES+=("$f")
    else
        echo "  WARN: malformed JSON, skipping: $(basename "$f")" >&2
        MALFORMED=$((MALFORMED + 1))
    fi
done

echo "  Valid results: ${#VALID_FILES[@]}" >&2
echo "  Malformed:     $MALFORMED" >&2

# ---------------------------------------------------------------------------
# Merge all valid JSON results into a single array
# ---------------------------------------------------------------------------
TMPMERGED="$(mktemp)"
trap 'rm -f "$TMPMERGED"' EXIT

echo "Merging ${#VALID_FILES[@]} result files..." >&2

# Use jq --slurp on concatenated input (memory-efficient for moderate corpora)
# For very large corpora (100k+ files), switch to streaming approach below
if [[ ${#VALID_FILES[@]} -lt 50000 ]]; then
    # Standard approach: slurp all at once
    cat "${VALID_FILES[@]}" | jq -s '.' > "$TMPMERGED"
else
    # Streaming approach for very large result sets
    echo "[" > "$TMPMERGED"
    first=true
    for f in "${VALID_FILES[@]}"; do
        if [[ "$first" == true ]]; then
            first=false
        else
            echo "," >> "$TMPMERGED"
        fi
        cat "$f" >> "$TMPMERGED"
    done
    echo "]" >> "$TMPMERGED"
fi

# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------
if [[ -n "$DEDUP_KEY" ]]; then
    BEFORE="$(jq 'length' "$TMPMERGED")"
    jq --arg key "$DEDUP_KEY" '
        [group_by(.[$key])[] | first]
    ' "$TMPMERGED" > "${TMPMERGED}.dedup"
    mv "${TMPMERGED}.dedup" "$TMPMERGED"
    AFTER="$(jq 'length' "$TMPMERGED")"
    DEDUPED=$((BEFORE - AFTER))
    echo "  Deduplicated by '$DEDUP_KEY': removed $DEDUPED duplicates" >&2
fi

# ---------------------------------------------------------------------------
# Sorting
# ---------------------------------------------------------------------------
if [[ -n "$SORT_BY" ]]; then
    echo "  Sorting by: $SORT_BY" >&2
    jq --arg key "$SORT_BY" '
        sort_by(.[$key] // "")
    ' "$TMPMERGED" > "${TMPMERGED}.sorted"
    mv "${TMPMERGED}.sorted" "$TMPMERGED"
fi

# ---------------------------------------------------------------------------
# Include error results if requested
# ---------------------------------------------------------------------------
if [[ "$INCLUDE_ERRORS" == true && ${#ERROR_FILES[@]} -gt 0 ]]; then
    echo "  Including ${#ERROR_FILES[@]} error results..." >&2
    ERROR_TMP="$(mktemp)"
    cat "${ERROR_FILES[@]}" | jq -s '.' > "$ERROR_TMP"
    jq -s '.[0] + .[1]' "$TMPMERGED" "$ERROR_TMP" > "${TMPMERGED}.with-errors"
    mv "${TMPMERGED}.with-errors" "$TMPMERGED"
    rm -f "$ERROR_TMP"
fi

# ---------------------------------------------------------------------------
# Generate summary statistics
# ---------------------------------------------------------------------------
echo "Generating summary statistics..." >&2

SUMMARY="$(jq '
{
    total_results: length,

    # Count by status field (if present)
    by_status: (
        [.[].status // "unknown"] |
        group_by(.) |
        map({key: .[0], value: length}) |
        from_entries
    ),

    # Count by category field (if present)
    by_category: (
        [.[].category // "uncategorized"] |
        group_by(.) |
        map({key: .[0], value: length}) |
        from_entries
    ),

    # Count by risk_level field (if present)
    by_risk_level: (
        [.[].risk_level // .[].classification // "unclassified"] |
        group_by(.) |
        map({key: .[0], value: length}) |
        from_entries
    ),

    # Numeric field stats (if present): risk_score, confidence, etc.
    score_stats: (
        [.[].risk_score // .[].score // .[].confidence // empty | select(type == "number")] |
        if length > 0 then {
            count: length,
            min: min,
            max: max,
            avg: (add / length),
            median: (sort | .[length / 2 | floor])
        } else null end
    ),

    # File size stats (if present)
    size_stats: (
        [.[].size_bytes // .[].file_size // empty | select(type == "number")] |
        if length > 0 then {
            total_bytes: add,
            avg_bytes: (add / length),
            min_bytes: min,
            max_bytes: max
        } else null end
    )
}
' "$TMPMERGED")"

echo "" >&2
echo "=== Summary ===" >&2
echo "$SUMMARY" | jq '.' >&2

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
write_output() {
    case "$FORMAT" in
        json)
            jq -n \
                --arg generated_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
                --argjson summary "$SUMMARY" \
                --argjson total_input "${#RESULT_FILES[@]}" \
                --argjson total_errors "${#ERROR_FILES[@]}" \
                --argjson malformed "$MALFORMED" \
                --slurpfile results "$TMPMERGED" \
                '{
                    metadata: {
                        generated_at: $generated_at,
                        total_input_files: $total_input,
                        total_error_files: $total_errors,
                        malformed_skipped: $malformed
                    },
                    summary: $summary,
                    results: $results[0]
                }'
            ;;
        jsonl)
            # One JSON object per line (for streaming consumers)
            jq -c '.[]' "$TMPMERGED"
            ;;
        csv)
            # Auto-detect columns from first result, flatten to CSV
            jq -r '
                (.[0] | keys_unsorted) as $keys |
                ($keys | @csv),
                (.[] | [.[$keys[]]] | map(
                    if type == "object" or type == "array" then tostring
                    elif type == "null" then ""
                    else .
                    end
                ) | @csv)
            ' "$TMPMERGED"
            ;;
    esac
}

echo "" >&2
echo "Writing output to: $OUTPUT_FILE" >&2

write_output > "$OUTPUT_FILE"

# ---------------------------------------------------------------------------
# Write summary to separate file if requested
# ---------------------------------------------------------------------------
if [[ -n "$SUMMARY_FILE" ]]; then
    echo "$SUMMARY" | jq '.' > "$SUMMARY_FILE"
    echo "Summary written to: $SUMMARY_FILE" >&2
fi

# ---------------------------------------------------------------------------
# Cross-reference with manifest for completeness check
# ---------------------------------------------------------------------------
if [[ -n "$MANIFEST_FILE" && -f "$MANIFEST_FILE" ]]; then
    echo "" >&2
    echo "=== Completeness Check ===" >&2
    MANIFEST_COUNT="$(jq '.files | length' "$MANIFEST_FILE")"
    RESULT_COUNT="$(jq 'length' "$TMPMERGED")"
    MISSING=$((MANIFEST_COUNT - RESULT_COUNT - ${#ERROR_FILES[@]}))

    echo "  Manifest files:   $MANIFEST_COUNT" >&2
    echo "  Successful:       $RESULT_COUNT" >&2
    echo "  Errored:          ${#ERROR_FILES[@]}" >&2
    echo "  Missing/skipped:  $MISSING" >&2

    COMPLETION_PCT="$(echo "scale=1; $RESULT_COUNT * 100 / $MANIFEST_COUNT" | bc 2>/dev/null || echo "N/A")"
    echo "  Completion:       ${COMPLETION_PCT}%" >&2
fi

echo "" >&2
echo "Done." >&2
