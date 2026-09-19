#!/usr/bin/env bash
#
# Stage 5: Timeline Synthesis (Opus Agent)
#
# The Opus orchestrator agent receives:
#   1. Consolidated events and entities
#   2. Validation report (contradictions, gaps)
#   3. Matter frame (config.yaml context)
#
# It produces the final defensible litigation chronology with:
#   - Contradiction resolution
#   - Issue-threaded timelines
#   - Entity-specific timelines
#   - Strategic assessment
#   - Deadline calendar
#
# This is the most expensive stage but runs only once per pipeline execution.

run_stage_5_synthesize() {
  stage "5" "Timeline Synthesis (Opus Agent)"

  local consol_dir="${TIMELINE_DIR}/consolidated"
  local valid_dir="${TIMELINE_DIR}/validated"
  local output_dir="${TIMELINE_DIR}/output"
  local prompts_dir="${TIMELINE_DIR}/prompts"
  local log_file="${TIMELINE_DIR}/logs/stage-5.log"
  ensure_dir "$output_dir"
  ensure_dir "${TIMELINE_DIR}/logs"

  local opus="${OPUS_MODEL}"

  # Verify inputs
  if [[ ! -f "${consol_dir}/events.json" ]]; then
    fail "No consolidated events found. Did Stage 3 complete?"
    return 1
  fi

  # Build matter frame from config
  local case_name
  case_name="$(config_get case_name '(not set)')"
  local case_number
  case_number="$(config_get case_number '')"
  local forum
  forum="$(config_get forum '')"
  local governing_law
  governing_law="$(config_get governing_law '')"
  local case_stage
  case_stage="$(config_get stage '')"
  local objective
  objective="$(config_get objective 'case strategy')"
  local side
  side="$(config_get side 'plaintiff')"
  local date_start
  date_start="$(config_get date_range_start '')"
  local date_end
  date_end="$(config_get date_range_end '')"
  local issues
  issues="$(config_get issues '')"
  local contradiction_policy
  contradiction_policy="$(config_get contradiction_policy 'material-only')"
  local timezone_baseline
  timezone_baseline="$(config_get timezone_baseline 'source-local')"

  log "Case: $case_name"
  log "Model: $opus"
  log "Objective: $objective"

  # Load consolidated data
  local events_json
  events_json="$(cat "${consol_dir}/events.json")"
  local entities_json
  entities_json="$(cat "${consol_dir}/entities.json")"

  # Load validation report (may not exist if validation was skipped/failed)
  local validation_json="{}"
  if [[ -f "${valid_dir}/validation.json" ]]; then
    validation_json="$(cat "${valid_dir}/validation.json")"
  else
    warn "No validation report found -- synthesizing without validation data"
  fi

  # Build the Opus synthesis prompt
  # This is the most complex prompt in the pipeline. The Opus agent
  # must reason about contradictions, build issue threads, and produce
  # a structured chronology.

  local user_prompt
  user_prompt="$(cat <<SYNTHEOF
You are synthesizing a defensible litigation chronology for:

## Matter Frame

- Case name: ${case_name}
- Case number: ${case_number}
- Forum: ${forum}
- Governing law: ${governing_law}
- Procedural stage: ${case_stage}
- Objective: ${objective}
- Side represented: ${side}
- Date range: ${date_start} to ${date_end}
- Issues: ${issues}
- Contradiction policy: ${contradiction_policy}
- Timezone baseline: ${timezone_baseline}

## Instructions

1. Review all consolidated events and resolve contradictions using source reliability
   hierarchy: original document > copy > sworn testimony > unsworn recollection > hearsay.

2. Build a master chronology sorted by date with confidence scores.

3. Create issue-specific timelines for each issue listed (or infer key issues from events).

4. Create entity-specific timelines for the most important actors.

5. Build a gap register: periods where events are expected but missing.

6. Build a deadline calendar for any procedural deadlines found.

7. Provide a strategic assessment: strengths, vulnerabilities, recommended actions.

8. For each contradiction, provide a resolution or mark as DISPUTED.

9. Every event MUST cite its source document(s).

10. Return ONLY valid JSON matching the synthesis schema in your system instructions.

## Consolidated Events

${events_json}

## Entity Registry

${entities_json}

## Validation Report

${validation_json}

Produce the final timeline synthesis as JSON.
SYNTHEOF
)"

  info "Running Opus synthesis (this may take several minutes)..."

  # The Opus synthesis is the most expensive single call.
  # We allow a higher budget and no turn limit on this one.
  local raw_output
  raw_output=$(claude -p \
    --model "$opus" \
    --output-format json \
    --max-turns 1 \
    --max-budget-usd 10.00 \
    --system-prompt-file "${prompts_dir}/opus-synthesis.md" \
    "$user_prompt" \
    2>> "$log_file")

  local claude_exit=$?

  if [[ $claude_exit -ne 0 ]]; then
    fail "Opus synthesis failed (exit code $claude_exit)"
    fail "Check log: $log_file"
    return 1
  fi

  # Parse and save the synthesis output
  python3 - "$raw_output" "${output_dir}/timeline.json" <<'PYEOF'
import json, sys

raw = sys.argv[1]
out_file = sys.argv[2]

try:
    # Try parsing as claude --output-format json envelope
    data = json.loads(raw)
    result = data.get("result", raw)
    parsed = json.loads(result)
except (json.JSONDecodeError, KeyError, TypeError):
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        # Save raw output for debugging
        with open(out_file + '.raw', 'w') as f:
            f.write(raw)
        print("ERROR: Could not parse synthesis output as JSON", file=sys.stderr)
        sys.exit(1)

with open(out_file, 'w') as f:
    json.dump(parsed, f, indent=2)

# Print summary
mc = parsed.get('master_chronology', [])
it = parsed.get('issue_timelines', {})
et = parsed.get('entity_timelines', {})
cr = parsed.get('contradiction_resolutions', [])
gr = parsed.get('gap_register', [])

print(f'Synthesis complete:')
print(f'  Master chronology: {len(mc)} events')
print(f'  Issue timelines: {len(it)} issues')
print(f'  Entity timelines: {len(et)} entities')
print(f'  Contradictions resolved: {len(cr)}')
print(f'  Gaps identified: {len(gr)}')
PYEOF

  local parse_exit=$?

  if [[ $parse_exit -ne 0 ]]; then
    fail "Synthesis output could not be parsed"
    fail "Raw output saved to ${output_dir}/timeline.json.raw"
    return 1
  fi

  ok "Stage 5 complete: timeline synthesized"
  return 0
}
