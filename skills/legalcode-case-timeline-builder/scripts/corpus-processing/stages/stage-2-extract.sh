#!/usr/bin/env bash
#
# Stage 2: Parallel Extraction (Haiku Workers)
#
# Spawns parallel claude -p --model haiku workers to extract:
#   - Dates and events
#   - Entities and relationships
#
# Each worker processes one document and writes structured JSON output.
# Workers are controlled via:
#   --max-turns 1        (single response, no tool use)
#   --max-budget-usd     (cost cap per worker)
#   --output-format json (structured output)
#   --system-prompt      (extraction-specific instructions)
#
# Concurrency is managed by a simple job pool (background processes).

run_stage_2_extract() {
  stage "2" "Parallel Extraction (Haiku Workers)"

  local extract_dir="${TIMELINE_DIR}/extractions"
  local log_dir="${TIMELINE_DIR}/logs/stage-2"
  local prompts_dir="${TIMELINE_DIR}/prompts"
  ensure_dir "${extract_dir}/dates"
  ensure_dir "${extract_dir}/entities"
  ensure_dir "$log_dir"

  local haiku="${HAIKU_MODEL}"
  local budget="${MAX_BUDGET_USD}"
  local max_jobs="${MAX_PARALLEL}"

  log "Extraction model: $haiku"
  log "Budget per worker: \$${budget}"
  log "Max parallel workers: $max_jobs"

  # Collect converted documents
  local doc_list=()
  while IFS=$'\t' read -r source_id original_path converted_path; do
    if [[ -n "$converted_path" && "$converted_path" != "null" && "$converted_path" != "None" ]]; then
      doc_list+=("${source_id}|${converted_path}")
    fi
  done < <(manifest_get_by_status "status" "converted")

  local total=${#doc_list[@]}
  if [[ $total -eq 0 ]]; then
    warn "No converted documents found for extraction."
    return 0
  fi

  log "Documents to process: $total"
  divider

  # ─── Date/Event Extraction Pass ────────────────────────────────────────

  info "Pass 1/2: Date and Event Extraction"

  local date_succeeded=0
  local date_failed=0
  local running_jobs=0
  local job_pids=()

  for entry in "${doc_list[@]}"; do
    local source_id="${entry%%|*}"
    local converted_path="${entry##*|}"
    local out_file="${extract_dir}/dates/${source_id}.json"

    # Skip if already extracted
    if [[ -f "$out_file" ]]; then
      date_succeeded=$((date_succeeded + 1))
      continue
    fi

    # Wait for a job slot if pool is full
    while [[ $running_jobs -ge $max_jobs ]]; do
      wait_for_job_slot
    done

    # Spawn Haiku worker in background
    run_haiku_extraction \
      "$source_id" \
      "$converted_path" \
      "$out_file" \
      "${log_dir}/${source_id}-dates.log" \
      "${prompts_dir}/haiku-date-extraction.md" \
      "dates_events" \
      "$haiku" \
      "$budget" &

    job_pids+=($!)
    running_jobs=$((running_jobs + 1))
  done

  # Wait for all remaining date extraction jobs
  for pid in "${job_pids[@]}"; do
    wait "$pid" 2>/dev/null
    local exit_code=$?
    if [[ $exit_code -eq 0 ]]; then
      date_succeeded=$((date_succeeded + 1))
    else
      date_failed=$((date_failed + 1))
    fi
  done

  ok "Date extraction: $date_succeeded succeeded, $date_failed failed"

  # ─── Entity Extraction Pass ────────────────────────────────────────────

  info "Pass 2/2: Entity Extraction"

  local entity_succeeded=0
  local entity_failed=0
  running_jobs=0
  job_pids=()

  for entry in "${doc_list[@]}"; do
    local source_id="${entry%%|*}"
    local converted_path="${entry##*|}"
    local out_file="${extract_dir}/entities/${source_id}.json"

    if [[ -f "$out_file" ]]; then
      entity_succeeded=$((entity_succeeded + 1))
      continue
    fi

    while [[ $running_jobs -ge $max_jobs ]]; do
      wait_for_job_slot
    done

    run_haiku_extraction \
      "$source_id" \
      "$converted_path" \
      "$out_file" \
      "${log_dir}/${source_id}-entities.log" \
      "${prompts_dir}/haiku-entity-extraction.md" \
      "entities" \
      "$haiku" \
      "$budget" &

    job_pids+=($!)
    running_jobs=$((running_jobs + 1))
  done

  for pid in "${job_pids[@]}"; do
    wait "$pid" 2>/dev/null
    local exit_code=$?
    if [[ $exit_code -eq 0 ]]; then
      entity_succeeded=$((entity_succeeded + 1))
    else
      entity_failed=$((entity_failed + 1))
    fi
  done

  ok "Entity extraction: $entity_succeeded succeeded, $entity_failed failed"

  # Update manifest for successfully extracted docs
  for entry in "${doc_list[@]}"; do
    local source_id="${entry%%|*}"
    local date_file="${extract_dir}/dates/${source_id}.json"
    local entity_file="${extract_dir}/entities/${source_id}.json"
    if [[ -f "$date_file" && -f "$entity_file" ]]; then
      manifest_update_status "$source_id" "extraction_status" "complete"
    elif [[ -f "$date_file" || -f "$entity_file" ]]; then
      manifest_update_status "$source_id" "extraction_status" "partial"
    else
      manifest_update_status "$source_id" "extraction_status" "failed"
    fi
  done

  divider
  ok "Stage 2 complete"
  return 0
}

# ─── Haiku Worker Function ─────────────────────────────────────────────────
#
# Invokes claude -p --model haiku for a single document extraction.
#
# This is the core multi-agent pattern:
#   1. Read the document content
#   2. Pipe it to claude with a system prompt
#   3. Capture structured JSON output
#   4. Validate the output is parseable JSON

run_haiku_extraction() {
  local source_id="$1"
  local converted_path="$2"
  local out_file="$3"
  local worker_log="$4"
  local system_prompt_file="$5"
  local extraction_type="$6"
  local model="$7"
  local budget="$8"

  log "  [${source_id}] Starting ${extraction_type} extraction..."

  # Build the user prompt: document content + extraction request
  local user_prompt
  user_prompt="$(cat <<USREOF
Source ID: ${source_id}
Extraction type: ${extraction_type}

--- DOCUMENT CONTENT BEGINS ---

$(cat "$converted_path" 2>/dev/null || echo "(failed to read document)")

--- DOCUMENT CONTENT ENDS ---

Extract all ${extraction_type} from this document. Return ONLY valid JSON matching the schema in your system instructions.
USREOF
)"

  # Core multi-agent CLI pattern:
  #   claude -p              : non-interactive (print) mode
  #   --model haiku          : use the fast/cheap model
  #   --output-format json   : structured JSON output
  #   --max-turns 1          : single response, no tool loops
  #   --max-budget-usd 0.50  : hard cost cap
  #   --system-prompt-file   : extraction-specific system prompt
  #
  # The document content is passed as the user message argument.

  local raw_output
  raw_output=$(claude -p \
    --model "$model" \
    --output-format json \
    --max-turns 1 \
    --max-budget-usd "$budget" \
    --system-prompt-file "$system_prompt_file" \
    "$user_prompt" \
    2>> "$worker_log")

  local claude_exit=$?

  if [[ $claude_exit -ne 0 ]]; then
    fail "  [${source_id}] Claude exited with code $claude_exit"
    echo "EXIT_CODE=$claude_exit" >> "$worker_log"
    return 1
  fi

  # The --output-format json wraps the response in a JSON envelope.
  # Extract the assistant's text content from it.
  local extracted_text
  extracted_text=$(python3 - "$raw_output" <<'PYEOF'
import json, sys
try:
    data = json.loads(sys.argv[1])
    # claude --output-format json returns: {"type":"result","subtype":"success","result":"..."}
    result = data.get("result", sys.argv[1])
    # Try to parse the result as JSON to validate it
    parsed = json.loads(result)
    # Pretty-print the validated JSON
    print(json.dumps(parsed, indent=2))
except (json.JSONDecodeError, KeyError, TypeError):
    # If the output is already valid JSON or not in envelope format
    try:
        parsed = json.loads(sys.argv[1])
        print(json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        # Last resort: write raw output and let consolidation handle it
        print(sys.argv[1])
        sys.exit(1)
PYEOF
  )

  local parse_exit=$?

  if [[ $parse_exit -ne 0 ]]; then
    fail "  [${source_id}] Output was not valid JSON -- saved raw output"
    echo "$raw_output" > "${out_file}.raw"
    echo "PARSE_FAILED=true" >> "$worker_log"
    return 1
  fi

  # Write validated JSON to output file
  echo "$extracted_text" > "$out_file"
  ok "  [${source_id}] ${extraction_type} extraction complete"
  return 0
}

# ─── Job Pool Helper ───────────────────────────────────────────────────────
# Wait for at least one background job to finish, freeing a slot.

wait_for_job_slot() {
  wait -n 2>/dev/null || true
  running_jobs=$((running_jobs - 1))
  [[ $running_jobs -lt 0 ]] && running_jobs=0
}
