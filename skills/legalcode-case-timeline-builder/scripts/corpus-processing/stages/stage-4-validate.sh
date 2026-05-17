#!/usr/bin/env bash
#
# Stage 4: Validation (Sonnet Agent)
#
# Sends consolidated timeline data to a Sonnet agent for quality validation:
#   - Contradiction detection (conflicting dates/descriptions)
#   - Sequence violation detection (impossible causal ordering)
#   - Gap analysis (unexplained missing periods)
#   - Confidence auditing (high-confidence claims with weak support)
#
# The consolidated events are chunked into segments if the corpus is large,
# with each segment sent to a separate Sonnet worker.
# Small corpora (<500 events) are validated in a single pass.

run_stage_4_validate() {
  stage "4" "Validation (Sonnet Agent)"

  local consol_dir="${TIMELINE_DIR}/consolidated"
  local valid_dir="${TIMELINE_DIR}/validated"
  local log_dir="${TIMELINE_DIR}/logs/stage-4"
  local prompts_dir="${TIMELINE_DIR}/prompts"
  ensure_dir "$valid_dir"
  ensure_dir "$log_dir"

  local sonnet="${SONNET_MODEL}"

  # Check consolidated data exists
  if [[ ! -f "${consol_dir}/events.json" ]]; then
    fail "No consolidated events found. Did Stage 3 complete?"
    return 1
  fi

  local event_count
  event_count=$(python3 -c "import json; print(len(json.load(open('${consol_dir}/events.json'))['events']))")
  log "Events to validate: $event_count"

  # Determine chunking strategy
  local chunk_size=200  # events per validation chunk
  local chunks_needed=$(( (event_count + chunk_size - 1) / chunk_size ))

  if [[ $chunks_needed -le 1 ]]; then
    # Small corpus: single validation pass
    info "Single-pass validation ($event_count events)"
    run_sonnet_validation \
      "${consol_dir}/events.json" \
      "${consol_dir}/entities.json" \
      "${valid_dir}/validation.json" \
      "${log_dir}/validation.log" \
      "${prompts_dir}/sonnet-validation.md" \
      "$sonnet" \
      "all"
  else
    # Large corpus: chunk and validate in parallel
    info "Chunked validation: $chunks_needed chunks of ~$chunk_size events"

    # Split events into chunks
    python3 - "${consol_dir}/events.json" "${valid_dir}" "$chunk_size" <<'PYEOF'
import json, sys, math
events_file = sys.argv[1]
output_dir = sys.argv[2]
chunk_size = int(sys.argv[3])

with open(events_file) as f:
    data = json.load(f)
events = data['events']
n_chunks = math.ceil(len(events) / chunk_size)

for i in range(n_chunks):
    chunk = events[i * chunk_size : (i + 1) * chunk_size]
    chunk_data = {
        'chunk_index': i,
        'total_chunks': n_chunks,
        'events': chunk,
    }
    with open(f'{output_dir}/chunk-{i:03d}.json', 'w') as f:
        json.dump(chunk_data, f, indent=2)
    print(f'Wrote chunk {i} with {len(chunk)} events')
PYEOF

    # Validate each chunk (parallel)
    local running_jobs=0
    local job_pids=()
    local max_jobs="${MAX_PARALLEL}"

    for chunk_file in "${valid_dir}"/chunk-*.json; do
      local chunk_name
      chunk_name="$(basename "$chunk_file" .json)"

      while [[ $running_jobs -ge $max_jobs ]]; do
        wait -n 2>/dev/null || true
        running_jobs=$((running_jobs - 1))
        [[ $running_jobs -lt 0 ]] && running_jobs=0
      done

      run_sonnet_validation \
        "$chunk_file" \
        "${consol_dir}/entities.json" \
        "${valid_dir}/${chunk_name}-validated.json" \
        "${log_dir}/${chunk_name}.log" \
        "${prompts_dir}/sonnet-validation.md" \
        "$sonnet" \
        "$chunk_name" &

      job_pids+=($!)
      running_jobs=$((running_jobs + 1))
    done

    # Wait for all validation jobs
    local val_succeeded=0
    local val_failed=0
    for pid in "${job_pids[@]}"; do
      wait "$pid" 2>/dev/null
      if [[ $? -eq 0 ]]; then
        val_succeeded=$((val_succeeded + 1))
      else
        val_failed=$((val_failed + 1))
      fi
    done

    ok "Chunk validation: $val_succeeded succeeded, $val_failed failed"

    # Merge chunk validations into single report
    merge_validation_results "$valid_dir"
  fi

  # Verify output
  if [[ -f "${valid_dir}/validation.json" ]]; then
    local contradiction_count gap_count quality
    contradiction_count=$(python3 -c "import json; d=json.load(open('${valid_dir}/validation.json')); print(len(d.get('contradictions', [])))" 2>/dev/null || echo "?")
    gap_count=$(python3 -c "import json; d=json.load(open('${valid_dir}/validation.json')); print(len(d.get('gaps', [])))" 2>/dev/null || echo "?")
    quality=$(python3 -c "import json; d=json.load(open('${valid_dir}/validation.json')); print(d.get('quality_summary', {}).get('overall_quality', '?'))" 2>/dev/null || echo "?")

    ok "Stage 4 complete: $contradiction_count contradictions, $gap_count gaps, quality=$quality"
  else
    warn "Validation output not found -- continuing with unvalidated data"
  fi

  return 0
}

# ─── Sonnet Validation Worker ──────────────────────────────────────────────

run_sonnet_validation() {
  local events_file="$1"
  local entities_file="$2"
  local out_file="$3"
  local worker_log="$4"
  local system_prompt_file="$5"
  local model="$6"
  local chunk_label="$7"

  log "  Validating ${chunk_label}..."

  # Build user prompt with the event data
  local events_json
  events_json="$(cat "$events_file")"

  local entities_json=""
  if [[ -f "$entities_file" ]]; then
    entities_json="$(cat "$entities_file")"
  fi

  # Load matter context from config
  local case_name
  case_name="$(config_get case_name '')"
  local objective
  objective="$(config_get objective 'case strategy')"

  local user_prompt
  user_prompt="$(cat <<VALEOF
Validate this litigation timeline for contradictions, sequence violations, and gaps.

Matter: ${case_name}
Objective: ${objective}

--- EVENTS DATA ---
${events_json}

--- ENTITIES DATA ---
${entities_json}

Analyze all events for the contradiction types in your instructions.
Return ONLY valid JSON matching the validation schema.
VALEOF
)"

  # Sonnet validation worker
  local raw_output
  raw_output=$(claude -p \
    --model "$model" \
    --output-format json \
    --max-turns 1 \
    --max-budget-usd 2.00 \
    --system-prompt-file "$system_prompt_file" \
    "$user_prompt" \
    2>> "$worker_log")

  local claude_exit=$?

  if [[ $claude_exit -ne 0 ]]; then
    fail "  Sonnet validation failed for ${chunk_label}"
    return 1
  fi

  # Parse and validate JSON output
  python3 - "$raw_output" "$out_file" <<'PYEOF'
import json, sys
raw = sys.argv[1]
out_file = sys.argv[2]
try:
    data = json.loads(raw)
    result = data.get("result", raw)
    parsed = json.loads(result)
    with open(out_file, 'w') as f:
        json.dump(parsed, f, indent=2)
except (json.JSONDecodeError, KeyError, TypeError):
    try:
        parsed = json.loads(raw)
        with open(out_file, 'w') as f:
            json.dump(parsed, f, indent=2)
    except json.JSONDecodeError:
        with open(out_file + '.raw', 'w') as f:
            f.write(raw)
        sys.exit(1)
PYEOF

  local parse_exit=$?
  if [[ $parse_exit -ne 0 ]]; then
    fail "  Validation output for ${chunk_label} was not valid JSON"
    return 1
  fi

  ok "  ${chunk_label} validated"
  return 0
}

# ─── Merge Chunk Validations ──────────────────────────────────────────────

merge_validation_results() {
  local valid_dir="$1"

  log "Merging validation chunks..."

  python3 - "$valid_dir" <<'PYEOF'
import json, os, sys
from datetime import datetime

valid_dir = sys.argv[1]
merged = {
    'validation_run_id': f'VAL-{datetime.utcnow().strftime("%Y%m%d%H%M%S")}',
    'validated_at': datetime.utcnow().isoformat() + 'Z',
    'events_checked': 0,
    'contradictions': [],
    'sequence_violations': [],
    'gaps': [],
    'quality_summary': {
        'total_events': 0,
        'high_confidence_events': 0,
        'low_confidence_events': 0,
        'contradictions_found': 0,
        'gaps_found': 0,
        'overall_quality': 'MEDIUM',
    }
}

for fname in sorted(os.listdir(valid_dir)):
    if not fname.endswith('-validated.json'):
        continue
    fpath = os.path.join(valid_dir, fname)
    try:
        with open(fpath) as f:
            chunk = json.load(f)
        merged['contradictions'].extend(chunk.get('contradictions', []))
        merged['sequence_violations'].extend(chunk.get('sequence_violations', []))
        merged['gaps'].extend(chunk.get('gaps', []))
        cs = chunk.get('quality_summary', {})
        merged['events_checked'] += cs.get('total_events', 0)
        merged['quality_summary']['total_events'] += cs.get('total_events', 0)
        merged['quality_summary']['high_confidence_events'] += cs.get('high_confidence_events', 0)
        merged['quality_summary']['low_confidence_events'] += cs.get('low_confidence_events', 0)
    except (json.JSONDecodeError, KeyError) as e:
        print(f'WARNING: Could not merge {fname}: {e}')

merged['quality_summary']['contradictions_found'] = len(merged['contradictions'])
merged['quality_summary']['gaps_found'] = len(merged['gaps'])

# Determine overall quality
c = merged['quality_summary']['contradictions_found']
if c == 0:
    merged['quality_summary']['overall_quality'] = 'HIGH'
elif c <= 5:
    merged['quality_summary']['overall_quality'] = 'MEDIUM'
else:
    merged['quality_summary']['overall_quality'] = 'LOW'

with open(os.path.join(valid_dir, 'validation.json'), 'w') as f:
    json.dump(merged, f, indent=2)

print(f'Merged validation: {merged["events_checked"]} events, '
      f'{len(merged["contradictions"])} contradictions, '
      f'{len(merged["gaps"])} gaps')
PYEOF
}
