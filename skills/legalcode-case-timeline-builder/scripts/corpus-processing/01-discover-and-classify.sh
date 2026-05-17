#!/usr/bin/env bash
# ==============================================================================
# 01-discover-and-classify.sh
#
# Scans a directory tree and classifies files by type, generating a manifest
# in JSON or CSV format with metadata (size, hash, MIME type, timestamps).
#
# Usage:
#   ./01-discover-and-classify.sh /path/to/documents [--format json|csv] [--output manifest.json]
#
# Compatibility: macOS (BSD) and Linux (GNU)
# Dependencies: file, shasum (or sha256sum), jq (for JSON output)
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'

# ---------------------------------------------------------------------------
# Portability shims: macOS (BSD) vs Linux (GNU)
# ---------------------------------------------------------------------------
_stat_size() {
    if stat --version >/dev/null 2>&1; then
        stat -c '%s' "$1"          # GNU
    else
        stat -f '%z' "$1"          # BSD / macOS
    fi
}

_stat_mtime() {
    if stat --version >/dev/null 2>&1; then
        stat -c '%Y' "$1"          # GNU  (epoch)
    else
        stat -f '%m' "$1"          # BSD / macOS (epoch)
    fi
}

_sha256() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    else
        shasum -a 256 "$1" | awk '{print $1}'
    fi
}

_realpath() {
    if command -v realpath >/dev/null 2>&1; then
        realpath "$1"
    elif command -v grealpath >/dev/null 2>&1; then
        grealpath "$1"
    else
        # Portable fallback using Python
        python3 -c "import os,sys; print(os.path.realpath(sys.argv[1]))" "$1"
    fi
}

_iso_date() {
    # Convert epoch seconds to ISO-8601
    if date --version >/dev/null 2>&1; then
        date -d "@$1" -u '+%Y-%m-%dT%H:%M:%SZ'    # GNU
    else
        date -r "$1" -u '+%Y-%m-%dT%H:%M:%SZ'      # BSD / macOS
    fi
}

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
SCAN_DIR=""
OUTPUT_FORMAT="json"
OUTPUT_FILE=""
FOLLOW_SYMLINKS=false
COMPUTE_HASH=true
MAX_DEPTH=""
EXCLUDE_PATTERNS=()
INCLUDE_EXTENSIONS=()

# ---------------------------------------------------------------------------
# Known document type categories
# ---------------------------------------------------------------------------
classify_extension() {
    local ext
    ext="$(echo "$1" | tr '[:upper:]' '[:lower:]')"
    case "$ext" in
        pdf)                          echo "document/pdf" ;;
        doc|docx)                     echo "document/word" ;;
        xls|xlsx|xlsm)                echo "document/spreadsheet" ;;
        ppt|pptx)                     echo "document/presentation" ;;
        odt|ods|odp)                  echo "document/openoffice" ;;
        rtf)                          echo "document/rtf" ;;
        txt|text|log)                 echo "text/plain" ;;
        csv|tsv)                      echo "text/tabular" ;;
        json|jsonl|ndjson)            echo "text/json" ;;
        xml|xhtml|html|htm)           echo "text/markup" ;;
        md|markdown|rst|adoc)         echo "text/markup" ;;
        msg)                          echo "email/outlook" ;;
        eml)                          echo "email/mime" ;;
        mbox)                         echo "email/mbox" ;;
        pst|ost)                      echo "email/archive" ;;
        jpg|jpeg|png|gif|bmp|tiff|tif|webp|heic)
                                      echo "image/raster" ;;
        svg)                          echo "image/vector" ;;
        mp4|avi|mov|mkv|wmv|flv)      echo "video/general" ;;
        mp3|wav|aac|flac|ogg|wma)     echo "audio/general" ;;
        zip|tar|gz|bz2|xz|7z|rar)    echo "archive/compressed" ;;
        *)                            echo "unknown" ;;
    esac
}

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
    cat <<'USAGE'
Usage: 01-discover-and-classify.sh <directory> [OPTIONS]

Options:
  --format json|csv       Output format (default: json)
  --output FILE           Output file path (default: stdout)
  --follow-symlinks       Follow symbolic links during scan
  --no-hash               Skip SHA-256 hash computation (faster)
  --max-depth N           Maximum directory depth to scan
  --exclude PATTERN       Glob pattern to exclude (repeatable)
  --include-ext EXT       Only include files with this extension (repeatable)
  -h, --help              Show this help

Examples:
  ./01-discover-and-classify.sh ./documents
  ./01-discover-and-classify.sh ./documents --format csv --output manifest.csv
  ./01-discover-and-classify.sh ./documents --no-hash --max-depth 3
  ./01-discover-and-classify.sh ./documents --exclude '*.tmp' --exclude '.git/*'
USAGE
    exit 0
}

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)        usage ;;
        --format)         OUTPUT_FORMAT="$2"; shift 2 ;;
        --output)         OUTPUT_FILE="$2"; shift 2 ;;
        --follow-symlinks) FOLLOW_SYMLINKS=true; shift ;;
        --no-hash)        COMPUTE_HASH=false; shift ;;
        --max-depth)      MAX_DEPTH="$2"; shift 2 ;;
        --exclude)        EXCLUDE_PATTERNS+=("$2"); shift 2 ;;
        --include-ext)    INCLUDE_EXTENSIONS+=("$2"); shift 2 ;;
        -*)               echo "Unknown option: $1" >&2; exit 1 ;;
        *)
            if [[ -z "$SCAN_DIR" ]]; then
                SCAN_DIR="$1"
            else
                echo "Error: unexpected argument '$1'" >&2; exit 1
            fi
            shift
            ;;
    esac
done

if [[ -z "$SCAN_DIR" ]]; then
    echo "Error: no directory specified." >&2
    usage
fi

if [[ ! -d "$SCAN_DIR" ]]; then
    echo "Error: '$SCAN_DIR' is not a directory." >&2
    exit 1
fi

SCAN_DIR="$(_realpath "$SCAN_DIR")"

# ---------------------------------------------------------------------------
# Build the find command
# ---------------------------------------------------------------------------
FIND_ARGS=("$SCAN_DIR")

if [[ "$FOLLOW_SYMLINKS" == true ]]; then
    FIND_ARGS=("-L" "${FIND_ARGS[@]}")
fi

if [[ -n "$MAX_DEPTH" ]]; then
    FIND_ARGS+=("-maxdepth" "$MAX_DEPTH")
fi

FIND_ARGS+=("-type" "f")

# Add exclude patterns
for pattern in "${EXCLUDE_PATTERNS[@]+"${EXCLUDE_PATTERNS[@]}"}"; do
    FIND_ARGS+=("!" "-path" "*${pattern}*")
done

# ---------------------------------------------------------------------------
# Discover files
# ---------------------------------------------------------------------------
SEEN_HASHES=()
DUPLICATE_COUNT=0
FILE_COUNT=0
ERROR_COUNT=0

# Temporary file for collecting JSON objects
TMPFILE="$(mktemp)"
trap 'rm -f "$TMPFILE"' EXIT

echo "Scanning: $SCAN_DIR" >&2
echo "Format:   $OUTPUT_FORMAT" >&2
echo "Hashing:  $COMPUTE_HASH" >&2
echo "" >&2

while IFS= read -r -d '' filepath; do
    # Get extension
    filename="$(basename "$filepath")"
    if [[ "$filename" == *.* ]]; then
        ext="${filename##*.}"
    else
        ext=""
    fi

    # Filter by extension if --include-ext was specified
    if [[ ${#INCLUDE_EXTENSIONS[@]} -gt 0 ]]; then
        matched=false
        for inc_ext in "${INCLUDE_EXTENSIONS[@]}"; do
            if [[ "$(echo "$ext" | tr '[:upper:]' '[:lower:]')" == "$(echo "$inc_ext" | tr '[:upper:]' '[:lower:]')" ]]; then
                matched=true
                break
            fi
        done
        if [[ "$matched" != true ]]; then
            continue
        fi
    fi

    FILE_COUNT=$((FILE_COUNT + 1))

    # Progress indicator every 100 files
    if (( FILE_COUNT % 100 == 0 )); then
        echo "  ... processed $FILE_COUNT files" >&2
    fi

    # Gather metadata (with error handling for unreadable files)
    if ! size="$(_stat_size "$filepath" 2>/dev/null)"; then
        echo "  WARN: cannot stat '$filepath'" >&2
        ERROR_COUNT=$((ERROR_COUNT + 1))
        continue
    fi

    mtime_epoch="$(_stat_mtime "$filepath")"
    mtime_iso="$(_iso_date "$mtime_epoch")"
    mime_type="$(file --brief --mime-type "$filepath" 2>/dev/null || echo "application/octet-stream")"
    category="$(classify_extension "$ext")"

    # Compute hash + detect duplicates
    hash=""
    is_duplicate=false
    if [[ "$COMPUTE_HASH" == true ]]; then
        hash="$(_sha256 "$filepath")"
        for seen in "${SEEN_HASHES[@]+"${SEEN_HASHES[@]}"}"; do
            if [[ "$seen" == "$hash" ]]; then
                is_duplicate=true
                DUPLICATE_COUNT=$((DUPLICATE_COUNT + 1))
                break
            fi
        done
        SEEN_HASHES+=("$hash")
    fi

    # Detect if symlink
    is_symlink=false
    if [[ -L "$filepath" ]]; then
        is_symlink=true
    fi

    # Relative path from scan root
    rel_path="${filepath#"$SCAN_DIR"/}"

    # Emit record
    if [[ "$OUTPUT_FORMAT" == "json" ]]; then
        jq -n \
            --arg path "$rel_path" \
            --arg abs_path "$filepath" \
            --arg filename "$filename" \
            --arg ext "$ext" \
            --arg category "$category" \
            --arg mime "$mime_type" \
            --argjson size "$size" \
            --arg modified "$mtime_iso" \
            --arg sha256 "$hash" \
            --argjson is_duplicate "$is_duplicate" \
            --argjson is_symlink "$is_symlink" \
            '{
                path: $path,
                absolute_path: $abs_path,
                filename: $filename,
                extension: $ext,
                category: $category,
                mime_type: $mime,
                size_bytes: $size,
                modified: $modified,
                sha256: $sha256,
                is_duplicate: $is_duplicate,
                is_symlink: $is_symlink
            }' >> "$TMPFILE"
    else
        # CSV
        echo "\"$rel_path\",\"$filename\",\"$ext\",\"$category\",\"$mime_type\",$size,\"$mtime_iso\",\"$hash\",$is_duplicate,$is_symlink" >> "$TMPFILE"
    fi

done < <(find "${FIND_ARGS[@]}" -print0 2>/dev/null | sort -z)

# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
echo "" >&2
echo "=== Discovery Summary ===" >&2
echo "  Total files:   $FILE_COUNT" >&2
echo "  Duplicates:    $DUPLICATE_COUNT" >&2
echo "  Errors:        $ERROR_COUNT" >&2
echo "  Scan root:     $SCAN_DIR" >&2
echo "" >&2

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
output_content() {
    if [[ "$OUTPUT_FORMAT" == "json" ]]; then
        # Build summary + file array
        jq -n \
            --argjson total "$FILE_COUNT" \
            --argjson duplicates "$DUPLICATE_COUNT" \
            --argjson errors "$ERROR_COUNT" \
            --arg scan_root "$SCAN_DIR" \
            --arg generated_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
            --slurpfile files "$TMPFILE" \
            '{
                manifest: {
                    generated_at: $generated_at,
                    scan_root: $scan_root,
                    total_files: $total,
                    duplicate_files: $duplicates,
                    scan_errors: $errors
                },
                files: $files
            }'
    else
        # CSV header + rows
        echo '"path","filename","extension","category","mime_type","size_bytes","modified","sha256","is_duplicate","is_symlink"'
        cat "$TMPFILE"
    fi
}

if [[ -n "$OUTPUT_FILE" ]]; then
    output_content > "$OUTPUT_FILE"
    echo "Output written to: $OUTPUT_FILE" >&2
else
    output_content
fi
