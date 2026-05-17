#!/usr/bin/env bash
#
# timeline-build.sh — Multi-agent litigation timeline pipeline
#
# Orchestrates a 6-stage pipeline for processing litigation document corpora
# into defensible case timelines using Claude Code CLI multi-agent patterns:
#
#   Stage 1: Document conversion        (local tools, no API)
#   Stage 2: Parallel extraction         (Haiku workers)
#   Stage 3: Consolidation              (merge results)
#   Stage 4: Validation                 (Sonnet checks)
#   Stage 5: Timeline construction      (Opus synthesis)
#   Stage 6: Output generation          (format export)
#
# Usage:
#   ./timeline-build.sh init <corpus_dir>                 # Initialize pipeline
#   ./timeline-build.sh run [--from <stage>] [--to <stage>]  # Run pipeline
#   ./timeline-build.sh status                            # Show pipeline status
#   ./timeline-build.sh retry [--stage <N>]               # Retry failed items
#   ./timeline-build.sh clean                             # Remove pipeline state
#
# Configuration:
#   Set TIMELINE_DIR to override the working directory (default: .timeline/)
#   Set TIMELINE_CONFIG to override the config file (default: .timeline/config.yaml)
#   Set MAX_PARALLEL to control worker concurrency (default: 4)
#
# Environment:
#   OPUS_MODEL      Override Opus model   (default: opus)
#   SONNET_MODEL    Override Sonnet model (default: sonnet)
#   HAIKU_MODEL     Override Haiku model  (default: haiku)
#   MAX_PARALLEL    Max concurrent workers (default: 4)
#   MAX_BUDGET_USD  Per-worker budget cap  (default: 0.50)

set -uo pipefail

# ─── Paths ─────────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# Pipeline working directory
TIMELINE_DIR="${TIMELINE_DIR:-.timeline}"
TIMELINE_CONFIG="${TIMELINE_CONFIG:-${TIMELINE_DIR}/config.yaml}"

# ─── Models ────────────────────────────────────────────────────────────────

OPUS_MODEL="${OPUS_MODEL:-opus}"
SONNET_MODEL="${SONNET_MODEL:-sonnet}"
HAIKU_MODEL="${HAIKU_MODEL:-haiku}"
MAX_PARALLEL="${MAX_PARALLEL:-4}"
MAX_BUDGET_USD="${MAX_BUDGET_USD:-0.50}"

# ─── Colors ────────────────────────────────────────────────────────────────

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

# ─── Logging ───────────────────────────────────────────────────────────────

ts()      { date '+%H:%M:%S'; }
log()     { echo -e "${CYAN}[$(ts)]${NC} $*"; }
info()    { echo -e "${BLUE}[$(ts)]${NC} ${BOLD}$*${NC}"; }
ok()      { echo -e "${GREEN}[$(ts)] OK${NC} $*"; }
warn()    { echo -e "${YELLOW}[$(ts)] WARN${NC} $*"; }
fail()    { echo -e "${RED}[$(ts)] FAIL${NC} $*"; }
stage()   { echo -e "\n${MAGENTA}[$(ts)] === STAGE $1 ===${NC} ${BOLD}$2${NC}"; }
divider() { echo -e "${DIM}$(printf '%.0s-' {1..70})${NC}"; }

# ─── Helpers ───────────────────────────────────────────────────────────────

require_cmd() {
  if ! command -v "$1" &>/dev/null; then
    fail "Required command not found: $1"
    echo "  Install it or adjust PATH before running this pipeline."
    exit 1
  fi
}

ensure_dir() {
  mkdir -p "$1"
}

# Read a value from config.yaml (simple grep-based, no yq dependency)
config_get() {
  local key="$1"
  local default="${2:-}"
  if [[ -f "$TIMELINE_CONFIG" ]]; then
    local val
    val="$(grep "^${key}:" "$TIMELINE_CONFIG" 2>/dev/null | head -1 | sed "s/^${key}:[[:space:]]*//" | sed 's/[[:space:]]*$//' | sed 's/^"//' | sed 's/"$//')"
    if [[ -n "$val" ]]; then
      echo "$val"
      return
    fi
  fi
  echo "$default"
}

# Write pipeline state checkpoint
checkpoint_write() {
  local stage_num="$1"
  local status="$2"  # running | complete | failed
  local checkpoint_file="${TIMELINE_DIR}/checkpoints/stage-${stage_num}.json"
  ensure_dir "${TIMELINE_DIR}/checkpoints"
  cat > "$checkpoint_file" <<EOF
{
  "stage": ${stage_num},
  "status": "${status}",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "hostname": "$(hostname)",
  "pid": $$
}
EOF
}

# Read pipeline state checkpoint
checkpoint_read() {
  local stage_num="$1"
  local checkpoint_file="${TIMELINE_DIR}/checkpoints/stage-${stage_num}.json"
  if [[ -f "$checkpoint_file" ]]; then
    grep '"status"' "$checkpoint_file" | sed 's/.*"status": *"//' | sed 's/".*//'
  else
    echo "pending"
  fi
}

# ─── Manifest Management ──────────────────────────────────────────────────

manifest_path() {
  echo "${TIMELINE_DIR}/manifest.json"
}

# Initialize manifest from a corpus directory
manifest_init() {
  local corpus_dir="$1"
  local manifest
  manifest="$(manifest_path)"

  log "Scanning corpus directory: $corpus_dir"

  local docs=()
  local doc_id=0

  # Find all processable files
  while IFS= read -r file; do
    doc_id=$((doc_id + 1))
    local ext="${file##*.}"
    local basename_file
    basename_file="$(basename "$file")"
    local file_size
    file_size="$(stat -f%z "$file" 2>/dev/null || stat --printf="%s" "$file" 2>/dev/null || echo 0)"

    docs+=("{
      \"source_id\": \"DOC-$(printf '%05d' $doc_id)\",
      \"original_path\": \"$file\",
      \"filename\": \"$basename_file\",
      \"extension\": \"$ext\",
      \"file_size_bytes\": $file_size,
      \"status\": \"pending\",
      \"converted_path\": null,
      \"extraction_status\": \"pending\",
      \"validation_status\": \"pending\"
    }")
  done < <(find "$corpus_dir" \
    -type f \( \
      -iname "*.pdf" -o \
      -iname "*.docx" -o \
      -iname "*.doc" -o \
      -iname "*.msg" -o \
      -iname "*.eml" -o \
      -iname "*.txt" -o \
      -iname "*.rtf" -o \
      -iname "*.html" -o \
      -iname "*.htm" -o \
      -iname "*.png" -o \
      -iname "*.jpg" -o \
      -iname "*.jpeg" -o \
      -iname "*.tiff" -o \
      -iname "*.tif" \
    \) | sort)

  # Build JSON manifest
  local joined
  joined="$(printf ',\n    %s' "${docs[@]}")"
  joined="${joined:6}" # Remove leading comma+newline+spaces

  cat > "$manifest" <<EOF
{
  "manifest_id": "MAN-$(date +%Y%m%d-%H%M%S)",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "corpus_dir": "$corpus_dir",
  "pipeline_version": "1.0.0",
  "total_documents": $doc_id,
  "documents": [
    $joined
  ]
}
EOF

  ok "Manifest created with $doc_id documents"
}

# Update a document's status in the manifest
manifest_update_status() {
  local source_id="$1"
  local field="$2"
  local value="$3"
  local manifest
  manifest="$(manifest_path)"

  # Use python3 for reliable JSON update (always available on macOS)
  python3 - "$manifest" "$source_id" "$field" "$value" <<'PYEOF'
import json, sys
manifest_file, source_id, field, value = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
with open(manifest_file, 'r') as f:
    data = json.load(f)
for doc in data['documents']:
    if doc['source_id'] == source_id:
        if value in ('null', 'None'):
            doc[field] = None
        elif value in ('true', 'false'):
            doc[field] = value == 'true'
        else:
            doc[field] = value
        break
with open(manifest_file, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
}

# Get documents by status
manifest_get_by_status() {
  local field="$1"
  local status="$2"
  local manifest
  manifest="$(manifest_path)"

  python3 - "$manifest" "$field" "$status" <<'PYEOF'
import json, sys
manifest_file, field, status = sys.argv[1], sys.argv[2], sys.argv[3]
with open(manifest_file, 'r') as f:
    data = json.load(f)
for doc in data['documents']:
    if doc.get(field) == status:
        print(doc['source_id'] + '\t' + doc.get('original_path', '') + '\t' + doc.get('converted_path', ''))
PYEOF
}

# ─── Stage 1: Document Conversion (Local Tools) ───────────────────────────
# No API calls. Uses local tools: magic-pdf (MinerU), pandoc, python-docx,
# extract-msg, or simple text extraction.

source "${SCRIPT_DIR}/stages/stage-1-convert.sh"

# ─── Stage 2: Parallel Extraction (Haiku Workers) ─────────────────────────
# Spawns claude -p --model haiku workers for date/event/entity extraction.

source "${SCRIPT_DIR}/stages/stage-2-extract.sh"

# ─── Stage 3: Consolidation ───────────────────────────────────────────────
# Merges extraction results, deduplicates events, resolves entity aliases.

source "${SCRIPT_DIR}/stages/stage-3-consolidate.sh"

# ─── Stage 4: Validation (Sonnet) ─────────────────────────────────────────
# Sonnet agent checks for contradictions, sequence violations, gaps.

source "${SCRIPT_DIR}/stages/stage-4-validate.sh"

# ─── Stage 5: Timeline Construction (Opus) ─────────────────────────────────
# Opus synthesizes final timeline with conflict resolution and analysis.

source "${SCRIPT_DIR}/stages/stage-5-synthesize.sh"

# ─── Stage 6: Output Generation ───────────────────────────────────────────
# Produces markdown, JSON, CSV, HTML outputs.

source "${SCRIPT_DIR}/stages/stage-6-output.sh"

# ─── Command: init ─────────────────────────────────────────────────────────

cmd_init() {
  local corpus_dir="${1:?Usage: timeline-build.sh init <corpus_dir>}"

  if [[ ! -d "$corpus_dir" ]]; then
    fail "Corpus directory not found: $corpus_dir"
    exit 1
  fi

  info "Initializing litigation timeline pipeline"
  divider

  # Create directory structure
  ensure_dir "${TIMELINE_DIR}"
  ensure_dir "${TIMELINE_DIR}/converted"
  ensure_dir "${TIMELINE_DIR}/extractions"
  ensure_dir "${TIMELINE_DIR}/extractions/dates"
  ensure_dir "${TIMELINE_DIR}/extractions/entities"
  ensure_dir "${TIMELINE_DIR}/extractions/events"
  ensure_dir "${TIMELINE_DIR}/consolidated"
  ensure_dir "${TIMELINE_DIR}/validated"
  ensure_dir "${TIMELINE_DIR}/output"
  ensure_dir "${TIMELINE_DIR}/checkpoints"
  ensure_dir "${TIMELINE_DIR}/logs"
  ensure_dir "${TIMELINE_DIR}/prompts"

  ok "Directory structure created"

  # Write default config if none exists
  if [[ ! -f "$TIMELINE_CONFIG" ]]; then
    cat > "$TIMELINE_CONFIG" <<'CFGEOF'
# timeline-build.sh configuration
# ---------------------------------
# Edit these values before running the pipeline.

# Matter identification
case_name: ""
case_number: ""
forum: ""
governing_law: ""
stage: ""
objective: "case strategy"
side: "plaintiff"

# Date scope
date_range_start: ""
date_range_end: ""

# Processing parameters
date_precision_policy: "preserve all with precision markers"
contradiction_policy: "material-only"
timezone_baseline: "source-local"

# Output
output_formats: "markdown json"

# Model overrides (or leave blank to use env defaults)
opus_model: ""
sonnet_model: ""
haiku_model: ""

# Cost controls
max_budget_per_worker_usd: "0.50"
max_parallel_workers: "4"

# Issues to track (comma-separated)
issues: ""

# Key parties (one per line, format: Name | Role)
parties: ""
CFGEOF
    ok "Default config written to $TIMELINE_CONFIG"
    warn "Edit $TIMELINE_CONFIG before running the pipeline."
  else
    ok "Config already exists at $TIMELINE_CONFIG"
  fi

  # Write system prompts to .timeline/prompts/
  write_system_prompts

  # Build document manifest
  manifest_init "$corpus_dir"

  # Initialize checkpoints
  for s in 1 2 3 4 5 6; do
    checkpoint_write "$s" "pending"
  done

  divider
  info "Pipeline initialized."
  log "Directory: ${TIMELINE_DIR}/"
  log "Config:    ${TIMELINE_CONFIG}"
  log "Manifest:  $(manifest_path)"
  echo ""
  log "Next steps:"
  log "  1. Edit ${TIMELINE_CONFIG} with matter details"
  log "  2. Run: ./timeline-build.sh run"
}

# ─── Write System Prompts ──────────────────────────────────────────────────
# Pre-writes all agent system prompts to .timeline/prompts/ so they can be
# reviewed and customized before execution.

write_system_prompts() {
  local prompts_dir="${TIMELINE_DIR}/prompts"
  ensure_dir "$prompts_dir"

  # --- Haiku: Date/Event Extraction ---
  cat > "${prompts_dir}/haiku-date-extraction.md" <<'SYSEOF'
You are a Date and Event Extraction Agent specialized in legal documents.

Extract ALL dates, events, and temporal references from the provided document.

## Extraction Rules

1. **Explicit dates**: "January 15, 2025", "01/15/2025", "2025-01-15"
2. **Relative dates**: "two weeks later", "the following month" (resolve if anchor date available)
3. **Fuzzy dates**: "early 2024", "around March", "Q3 2023"
4. **Date ranges**: "from January to March 2025"
5. **Deadlines**: "within 30 days", "90-day notice period"
6. **Recurrence**: "every Monday", "quarterly"

## Output Schema (strict JSON)

Return ONLY a JSON object with this structure:

```json
{
  "source_id": "<provided in user message>",
  "extraction_type": "dates_events",
  "extracted_at": "<ISO timestamp>",
  "items": [
    {
      "raw_text": "Original text as it appears",
      "normalized_date": "YYYY-MM-DD or YYYY-MM-DD/YYYY-MM-DD for ranges",
      "precision": "exact|day|week|month|quarter|year|approximate",
      "confidence": 0.95,
      "context": "Full surrounding sentence",
      "event_type": "meeting|deadline|transaction|communication|filing|execution|other",
      "event_description": "Brief description of what happened",
      "actors": ["Person or Organization names involved"],
      "source_location": "Page X, paragraph Y or section reference"
    }
  ],
  "document_metadata": {
    "apparent_document_type": "contract|email|memo|filing|transcript|other",
    "apparent_date_range": "earliest to latest date found",
    "language": "en"
  }
}
```

## Rules

- Extract EVERY temporal reference, even uncertain ones.
- For uncertain dates, set confidence < 0.6 and precision to "approximate".
- Do NOT infer dates not present in the text.
- Preserve original text exactly in raw_text.
- Normalize dates to ISO 8601 where possible.
- If a relative date cannot be resolved, set normalized_date to null and note in context.
- Return valid JSON only. No markdown fencing. No commentary outside the JSON.
SYSEOF

  # --- Haiku: Entity Extraction ---
  cat > "${prompts_dir}/haiku-entity-extraction.md" <<'SYSEOF'
You are an Entity Extraction Agent specialized in legal documents.

Extract ALL named entities and their relationships from the provided document.

## Entity Types

1. **PERSON**: Individual names (full, partial, title+name)
2. **ORGANIZATION**: Companies, firms, agencies, courts, government bodies
3. **LOCATION**: Addresses, cities, jurisdictions, venues
4. **ROLE**: Legal roles (plaintiff, defendant, witness, counsel, judge, expert)
5. **DOCUMENT**: Document references (Exhibit A, Bates 00001-00015, Attachment 1)
6. **CASE**: Case numbers, docket numbers, matter references
7. **STATUTE**: Legal citations (15 U.S.C. 78j(b), FRCP 26, CPR Part 31)
8. **MONETARY**: Financial amounts ($1,000,000, EUR 500K, GBP 2.5M)

## Output Schema (strict JSON)

Return ONLY a JSON object:

```json
{
  "source_id": "<provided in user message>",
  "extraction_type": "entities",
  "extracted_at": "<ISO timestamp>",
  "entities": [
    {
      "text": "As it appears in document",
      "type": "PERSON|ORGANIZATION|LOCATION|ROLE|DOCUMENT|CASE|STATUTE|MONETARY",
      "normalized": "Standardized canonical form",
      "aliases": ["Other names for same entity in this document"],
      "context": "Sentence where found",
      "confidence": 0.95
    }
  ],
  "relationships": [
    {
      "source_entity": "Normalized entity name",
      "relationship": "employs|represents|filed_against|signed|authored|received|sent_to",
      "target_entity": "Normalized entity name",
      "context": "Sentence establishing relationship",
      "confidence": 0.90
    }
  ],
  "coreferences": [
    {
      "pronoun_or_reference": "he|she|the company|defendant",
      "resolved_entity": "Normalized entity name",
      "context": "Sentence with coreference",
      "confidence": 0.80
    }
  ]
}
```

## Rules

- Extract every named entity, even mentioned in passing.
- Perform coreference resolution: link pronouns to named entities.
- Normalize names (remove titles for matching, keep for display).
- Flag when identity is ambiguous (confidence < 0.6).
- Return valid JSON only. No markdown fencing. No commentary.
SYSEOF

  # --- Sonnet: Validation ---
  cat > "${prompts_dir}/sonnet-validation.md" <<'SYSEOF'
You are a Timeline Validation Agent for litigation chronologies.

You will receive a consolidated timeline (JSON array of events) and must check for:

1. **Contradictions**: Same event with conflicting dates or descriptions
2. **Sequence violations**: Events in impossible causal order
3. **Temporal impossibilities**: Person in two places at once, implausible durations
4. **Confidence issues**: High-confidence claims with weak sourcing
5. **Gap detection**: Missing expected events in critical periods

## Contradiction Types

| Type        | Description                        |
|-------------|----------------------------------- |
| DIRECT      | Same event, different dates         |
| SEQUENCE    | Events in impossible order          |
| OVERLAP     | Actor at two places simultaneously  |
| DURATION    | Implausible time spans              |
| WITNESS     | Conflicting accounts of same event  |

## Output Schema (strict JSON)

```json
{
  "validation_run_id": "<UUID>",
  "validated_at": "<ISO timestamp>",
  "events_checked": 0,
  "contradictions": [
    {
      "type": "DIRECT|SEQUENCE|OVERLAP|DURATION|WITNESS",
      "severity": "LOW|MEDIUM|HIGH|CRITICAL",
      "event_ids": ["EVT-00001", "EVT-00002"],
      "description": "What the contradiction is",
      "evidence_for": "Source supporting version A",
      "evidence_against": "Source supporting version B",
      "recommended_resolution": "Specific action to resolve",
      "confidence": 0.85
    }
  ],
  "sequence_violations": [
    {
      "cause_event_id": "EVT-00001",
      "effect_event_id": "EVT-00002",
      "rule": "Cause must precede effect",
      "description": "What is wrong",
      "severity": "HIGH"
    }
  ],
  "gaps": [
    {
      "gap_id": "GAP-001",
      "period_start": "YYYY-MM-DD",
      "period_end": "YYYY-MM-DD",
      "description": "What is missing",
      "expected_activity": "What should have happened",
      "impact": "LOW|MEDIUM|HIGH|CRITICAL",
      "recommended_action": "What to do"
    }
  ],
  "quality_summary": {
    "total_events": 0,
    "high_confidence_events": 0,
    "low_confidence_events": 0,
    "contradictions_found": 0,
    "gaps_found": 0,
    "overall_quality": "HIGH|MEDIUM|LOW"
  }
}
```

## Rules

- Check EVERY event pair where dates are close or actors overlap.
- Apply causal ordering rules (filing before response, notice before action).
- Flag any event with confidence < 0.5 that is used as an anchor.
- Identify periods with zero events between known activity clusters.
- Return valid JSON only.
SYSEOF

  # --- Opus: Timeline Synthesis ---
  cat > "${prompts_dir}/opus-synthesis.md" <<'SYSEOF'
You are the Timeline Synthesis Agent for litigation chronology construction.

You receive:
1. A validated consolidated timeline (events, entities, relationships)
2. A validation report (contradictions, gaps, quality issues)
3. A matter frame (case context, objectives, parties, issues)

Your task is to produce the final defensible litigation chronology.

## Responsibilities

1. **Resolve contradictions**: For each contradiction, determine the best-supported
   version and mark alternatives. Use source reliability, corroboration count, and
   document type hierarchy (original > copy > testimony > hearsay).

2. **Fill narrative gaps**: Where gaps are identified, note them explicitly as
   information requests or discovery needs. Do NOT fabricate events.

3. **Build issue threads**: Map each event to the case issues it bears on.
   An event may be relevant to multiple issues.

4. **Assess strategic significance**: For each event, note whether it supports
   or undermines the represented side's position.

5. **Generate confidence-scored chronology**: Every event gets a final confidence
   score reflecting source quality, corroboration, and contradiction status.

## Output

Produce a JSON object with this top-level structure:

```json
{
  "metadata": {
    "case_name": "",
    "case_number": "",
    "generated_at": "",
    "timeline_version": "1.0",
    "baseline_timezone": "",
    "confidence_overall": "HIGH|MEDIUM|LOW"
  },
  "master_chronology": [...events sorted by date...],
  "issue_timelines": {
    "issue_name": [...filtered events...]
  },
  "entity_timelines": {
    "entity_name": [...filtered events...]
  },
  "contradiction_resolutions": [...],
  "gap_register": [...],
  "deadline_calendar": [...],
  "strategic_assessment": {
    "strengths": [...],
    "vulnerabilities": [...],
    "recommended_actions": [...]
  }
}
```

## Rules

- Every event MUST have at least one source citation.
- Mark unresolved contradictions as DISPUTED.
- Preserve original date text alongside normalized dates.
- Separate facts from inferences. Label inferences explicitly.
- Do not present approximate dates as exact.
- Return valid JSON only.
SYSEOF

  ok "System prompts written to ${prompts_dir}/"
}

# ─── Command: run ──────────────────────────────────────────────────────────

cmd_run() {
  local from_stage=1
  local to_stage=6

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --from) from_stage="$2"; shift 2 ;;
      --to)   to_stage="$2"; shift 2 ;;
      *)      fail "Unknown argument: $1"; exit 1 ;;
    esac
  done

  # Validate prerequisites
  require_cmd claude
  require_cmd python3

  if [[ ! -f "$(manifest_path)" ]]; then
    fail "Pipeline not initialized. Run: timeline-build.sh init <corpus_dir>"
    exit 1
  fi

  info "Litigation Timeline Pipeline"
  divider
  log "Config:     ${TIMELINE_CONFIG}"
  log "Case:       $(config_get case_name '(not set)')"
  log "Objective:  $(config_get objective 'case strategy')"
  log "Stages:     ${from_stage} through ${to_stage}"
  log "Models:     Opus=${OPUS_MODEL} Sonnet=${SONNET_MODEL} Haiku=${HAIKU_MODEL}"
  log "Parallel:   ${MAX_PARALLEL} workers"
  log "Budget cap: \$${MAX_BUDGET_USD}/worker"
  divider

  local pipeline_start=$SECONDS
  local run_log="${TIMELINE_DIR}/logs/run-$(date +%Y%m%d-%H%M%S).log"
  ensure_dir "${TIMELINE_DIR}/logs"

  # Execute stages
  for s in $(seq "$from_stage" "$to_stage"); do
    local stage_status
    stage_status="$(checkpoint_read "$s")"

    if [[ "$stage_status" == "complete" ]]; then
      log "Stage $s already complete, skipping"
      continue
    fi

    checkpoint_write "$s" "running"

    case "$s" in
      1) run_stage_1_convert ;;
      2) run_stage_2_extract ;;
      3) run_stage_3_consolidate ;;
      4) run_stage_4_validate ;;
      5) run_stage_5_synthesize ;;
      6) run_stage_6_output ;;
    esac

    local exit_code=$?
    if [[ $exit_code -ne 0 ]]; then
      checkpoint_write "$s" "failed"
      fail "Stage $s failed (exit code $exit_code)"
      fail "Fix the issue and run: timeline-build.sh run --from $s"
      exit $exit_code
    fi

    checkpoint_write "$s" "complete"
  done

  local pipeline_elapsed=$(( SECONDS - pipeline_start ))

  echo ""
  divider
  info "Pipeline Complete"
  divider
  log "Duration: $((pipeline_elapsed / 60))m $((pipeline_elapsed % 60))s"
  log "Output:   ${TIMELINE_DIR}/output/"
  log "Run log:  $run_log"
  divider
}

# ─── Command: status ───────────────────────────────────────────────────────

cmd_status() {
  info "Pipeline Status"
  divider

  if [[ ! -f "$(manifest_path)" ]]; then
    warn "Pipeline not initialized."
    exit 0
  fi

  local stage_names=("" "Document Conversion" "Parallel Extraction" "Consolidation" "Validation" "Timeline Synthesis" "Output Generation")

  for s in 1 2 3 4 5 6; do
    local status
    status="$(checkpoint_read "$s")"
    local icon
    case "$status" in
      complete) icon="${GREEN}DONE${NC}" ;;
      running)  icon="${YELLOW}RUNNING${NC}" ;;
      failed)   icon="${RED}FAILED${NC}" ;;
      *)        icon="${DIM}PENDING${NC}" ;;
    esac
    printf "  Stage %d: %-25s [%b]\n" "$s" "${stage_names[$s]}" "$icon"
  done

  echo ""

  # Document counts from manifest
  if [[ -f "$(manifest_path)" ]]; then
    python3 - "$(manifest_path)" <<'PYEOF'
import json, sys
with open(sys.argv[1]) as f:
    data = json.load(f)
docs = data['documents']
total = len(docs)
converted = sum(1 for d in docs if d.get('status') == 'converted')
extracted = sum(1 for d in docs if d.get('extraction_status') == 'complete')
validated = sum(1 for d in docs if d.get('validation_status') == 'complete')
failed = sum(1 for d in docs if d.get('status') == 'failed')
print(f"  Documents: {total} total | {converted} converted | {extracted} extracted | {validated} validated | {failed} failed")
PYEOF
  fi
  divider
}

# ─── Command: retry ────────────────────────────────────────────────────────

cmd_retry() {
  local stage=""
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --stage) stage="$2"; shift 2 ;;
      *)       fail "Unknown argument: $1"; exit 1 ;;
    esac
  done

  if [[ -n "$stage" ]]; then
    info "Retrying failed items in stage $stage"
    checkpoint_write "$stage" "pending"
    cmd_run --from "$stage" --to "$stage"
  else
    # Find the first failed stage and retry from there
    for s in 1 2 3 4 5 6; do
      local status
      status="$(checkpoint_read "$s")"
      if [[ "$status" == "failed" ]]; then
        info "Retrying from failed stage $s"
        checkpoint_write "$s" "pending"
        cmd_run --from "$s"
        return
      fi
    done
    warn "No failed stages found."
  fi
}

# ─── Command: clean ────────────────────────────────────────────────────────

cmd_clean() {
  if [[ -d "$TIMELINE_DIR" ]]; then
    warn "This will delete: ${TIMELINE_DIR}/"
    echo -n "  Continue? [y/N] "
    read -r confirm
    if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
      rm -rf "$TIMELINE_DIR"
      ok "Pipeline state removed."
    else
      log "Cancelled."
    fi
  else
    log "No pipeline state to clean."
  fi
}

# ─── Main Dispatch ─────────────────────────────────────────────────────────

main() {
  local cmd="${1:-}"
  shift || true

  case "$cmd" in
    init)   cmd_init "$@" ;;
    run)    cmd_run "$@" ;;
    status) cmd_status "$@" ;;
    retry)  cmd_retry "$@" ;;
    clean)  cmd_clean "$@" ;;
    -h|--help|help|"")
      echo "Usage: timeline-build.sh <command> [options]"
      echo ""
      echo "Commands:"
      echo "  init <corpus_dir>    Initialize pipeline from document corpus"
      echo "  run [--from N] [--to N]  Run pipeline stages"
      echo "  status               Show pipeline status"
      echo "  retry [--stage N]    Retry failed items"
      echo "  clean                Remove pipeline state"
      echo ""
      echo "Environment:"
      echo "  OPUS_MODEL       Opus model name   (default: opus)"
      echo "  SONNET_MODEL     Sonnet model name  (default: sonnet)"
      echo "  HAIKU_MODEL      Haiku model name   (default: haiku)"
      echo "  MAX_PARALLEL     Worker concurrency (default: 4)"
      echo "  MAX_BUDGET_USD   Per-worker cost cap (default: 0.50)"
      ;;
    *)
      fail "Unknown command: $cmd"
      echo "Run: timeline-build.sh --help"
      exit 1
      ;;
  esac
}

main "$@"
