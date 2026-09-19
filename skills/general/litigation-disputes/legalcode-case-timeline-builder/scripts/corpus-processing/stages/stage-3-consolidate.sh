#!/usr/bin/env bash
#
# Stage 3: Consolidation
#
# Merges per-document extraction results into unified timeline data:
#   1. Merge all date/event extractions into a single event table
#   2. Merge all entity extractions into a unified entity registry
#   3. Deduplicate events (same date + type + similar text)
#   4. Assign stable event IDs
#   5. Cross-reference entities with events
#
# This stage runs locally using Python -- no API calls.

run_stage_3_consolidate() {
  stage "3" "Consolidation (merge and deduplicate)"

  local extract_dir="${TIMELINE_DIR}/extractions"
  local consol_dir="${TIMELINE_DIR}/consolidated"
  local log_file="${TIMELINE_DIR}/logs/stage-3.log"
  ensure_dir "$consol_dir"
  ensure_dir "${TIMELINE_DIR}/logs"

  # Count available extraction files
  local date_files
  date_files=$(find "${extract_dir}/dates" -name "*.json" -type f 2>/dev/null | wc -l | tr -d ' ')
  local entity_files
  entity_files=$(find "${extract_dir}/entities" -name "*.json" -type f 2>/dev/null | wc -l | tr -d ' ')

  log "Date extraction files: $date_files"
  log "Entity extraction files: $entity_files"

  if [[ "$date_files" -eq 0 && "$entity_files" -eq 0 ]]; then
    fail "No extraction files found. Did Stage 2 complete?"
    return 1
  fi

  # Run consolidation via Python script
  python3 - \
    "${extract_dir}/dates" \
    "${extract_dir}/entities" \
    "${consol_dir}" \
    > "$log_file" 2>&1 <<'PYEOF'
import json
import os
import sys
import hashlib
from datetime import datetime
from collections import defaultdict

dates_dir = sys.argv[1]
entities_dir = sys.argv[2]
output_dir = sys.argv[3]

# ─── Load all date/event extractions ──────────────────────────────────

all_events = []
event_id_counter = 0

for fname in sorted(os.listdir(dates_dir)):
    if not fname.endswith('.json'):
        continue
    fpath = os.path.join(dates_dir, fname)
    try:
        with open(fpath) as f:
            data = json.load(f)
        source_id = data.get('source_id', fname.replace('.json', ''))
        items = data.get('items', [])
        for item in items:
            event_id_counter += 1
            evt = {
                'event_id': f'EVT-{event_id_counter:05d}',
                'source_id': source_id,
                'raw_text': item.get('raw_text', ''),
                'normalized_date': item.get('normalized_date'),
                'precision': item.get('precision', 'unknown'),
                'confidence': item.get('confidence', 0.5),
                'context': item.get('context', ''),
                'event_type': item.get('event_type', 'other'),
                'event_description': item.get('event_description', ''),
                'actors': item.get('actors', []),
                'source_location': item.get('source_location', ''),
                'source_references': [source_id],
                'corroboration_count': 1,
            }
            all_events.append(evt)
        print(f'Loaded {len(items)} events from {fname}')
    except (json.JSONDecodeError, KeyError) as e:
        print(f'WARNING: Failed to parse {fname}: {e}')

print(f'\nTotal raw events: {len(all_events)}')

# ─── Deduplicate events ──────────────────────────────────────────────
# Group by (normalized_date, event_type, text_signature)

def text_signature(text):
    """Normalize text for dedup comparison."""
    t = text.lower().strip()
    # Remove common noise words
    for w in ['the', 'a', 'an', 'of', 'in', 'on', 'at', 'to', 'for']:
        t = t.replace(f' {w} ', ' ')
    return t[:80]

groups = defaultdict(list)
for evt in all_events:
    key = (
        evt['normalized_date'] or 'none',
        evt['event_type'],
        text_signature(evt.get('event_description', '') or evt.get('raw_text', ''))
    )
    groups[key].append(evt)

deduped_events = []
dedup_id = 0
for key, group in groups.items():
    dedup_id += 1
    if len(group) == 1:
        evt = group[0]
        evt['event_id'] = f'EVT-{dedup_id:05d}'
        deduped_events.append(evt)
    else:
        # Merge: take highest confidence, merge sources
        best = max(group, key=lambda e: e.get('confidence', 0))
        best['event_id'] = f'EVT-{dedup_id:05d}'
        best['source_references'] = list(set(
            ref for e in group for ref in e.get('source_references', [e['source_id']])
        ))
        best['corroboration_count'] = len(group)
        best['confidence'] = min(1.0, best['confidence'] + 0.05 * (len(group) - 1))
        # Merge actors
        all_actors = []
        for e in group:
            for a in e.get('actors', []):
                if a not in all_actors:
                    all_actors.append(a)
        best['actors'] = all_actors
        deduped_events.append(best)

print(f'After deduplication: {len(deduped_events)} events (removed {len(all_events) - len(deduped_events)} duplicates)')

# Sort by date
def sort_key(evt):
    d = evt.get('normalized_date') or ''
    # Handle approximate dates
    d = d.replace('~', '').replace('<', '').replace('>', '')
    return d

deduped_events.sort(key=sort_key)

# ─── Load all entity extractions ─────────────────────────────────────

all_entities = []
all_relationships = []

for fname in sorted(os.listdir(entities_dir)):
    if not fname.endswith('.json'):
        continue
    fpath = os.path.join(entities_dir, fname)
    try:
        with open(fpath) as f:
            data = json.load(f)
        source_id = data.get('source_id', fname.replace('.json', ''))
        entities = data.get('entities', [])
        for ent in entities:
            ent['source_id'] = source_id
            all_entities.append(ent)
        rels = data.get('relationships', [])
        for rel in rels:
            rel['source_id'] = source_id
            all_relationships.append(rel)
        print(f'Loaded {len(entities)} entities, {len(rels)} relationships from {fname}')
    except (json.JSONDecodeError, KeyError) as e:
        print(f'WARNING: Failed to parse {fname}: {e}')

print(f'\nTotal raw entities: {len(all_entities)}')
print(f'Total raw relationships: {len(all_relationships)}')

# ─── Deduplicate entities ─────────────────────────────────────────────

entity_registry = {}  # normalized_name -> entity record
for ent in all_entities:
    normalized = (ent.get('normalized') or ent.get('text', '')).strip()
    key = normalized.lower()
    if key in entity_registry:
        existing = entity_registry[key]
        # Merge aliases
        for alias in ent.get('aliases', []):
            if alias not in existing.get('aliases', []):
                existing.setdefault('aliases', []).append(alias)
        # Merge sources
        existing.setdefault('source_ids', [])
        if ent.get('source_id') not in existing['source_ids']:
            existing['source_ids'].append(ent['source_id'])
        existing['mention_count'] = existing.get('mention_count', 1) + 1
        # Keep highest confidence
        if ent.get('confidence', 0) > existing.get('confidence', 0):
            existing['confidence'] = ent['confidence']
    else:
        entity_registry[key] = {
            'entity_id': f'ENT-{len(entity_registry) + 1:05d}',
            'text': ent.get('text', normalized),
            'type': ent.get('type', 'UNKNOWN'),
            'normalized': normalized,
            'aliases': ent.get('aliases', []),
            'confidence': ent.get('confidence', 0.5),
            'source_ids': [ent.get('source_id', '')],
            'mention_count': 1,
        }

entities_deduped = list(entity_registry.values())
print(f'After entity dedup: {len(entities_deduped)} unique entities')

# ─── Write consolidated outputs ──────────────────────────────────────

# Events
events_output = {
    'consolidated_at': datetime.utcnow().isoformat() + 'Z',
    'total_events': len(deduped_events),
    'total_raw_events': len(all_events),
    'duplicates_removed': len(all_events) - len(deduped_events),
    'events': deduped_events,
}
with open(os.path.join(output_dir, 'events.json'), 'w') as f:
    json.dump(events_output, f, indent=2)

# Entities
entities_output = {
    'consolidated_at': datetime.utcnow().isoformat() + 'Z',
    'total_entities': len(entities_deduped),
    'total_raw_entities': len(all_entities),
    'entities': entities_deduped,
    'relationships': all_relationships,
}
with open(os.path.join(output_dir, 'entities.json'), 'w') as f:
    json.dump(entities_output, f, indent=2)

# Summary
summary = {
    'consolidated_at': datetime.utcnow().isoformat() + 'Z',
    'events': {
        'raw': len(all_events),
        'deduplicated': len(deduped_events),
        'duplicates_removed': len(all_events) - len(deduped_events),
    },
    'entities': {
        'raw': len(all_entities),
        'deduplicated': len(entities_deduped),
    },
    'relationships': len(all_relationships),
    'date_files_processed': int(sum(1 for f in os.listdir(dates_dir) if f.endswith('.json'))),
    'entity_files_processed': int(sum(1 for f in os.listdir(entities_dir) if f.endswith('.json'))),
}
with open(os.path.join(output_dir, 'summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print(f'\n--- Consolidation Summary ---')
print(f'Events: {len(all_events)} raw -> {len(deduped_events)} deduplicated')
print(f'Entities: {len(all_entities)} raw -> {len(entities_deduped)} deduplicated')
print(f'Relationships: {len(all_relationships)}')
print(f'Output written to {output_dir}/')
PYEOF

  local py_exit=$?

  if [[ $py_exit -ne 0 ]]; then
    fail "Consolidation script failed (see ${log_file})"
    cat "$log_file"
    return 1
  fi

  # Verify outputs exist
  if [[ -f "${consol_dir}/events.json" && -f "${consol_dir}/entities.json" ]]; then
    local event_count
    event_count=$(python3 -c "import json; d=json.load(open('${consol_dir}/summary.json')); print(d['events']['deduplicated'])")
    local entity_count
    entity_count=$(python3 -c "import json; d=json.load(open('${consol_dir}/summary.json')); print(d['entities']['deduplicated'])")

    ok "Stage 3 complete: $event_count events, $entity_count entities consolidated"
  else
    fail "Expected output files not found"
    return 1
  fi

  return 0
}
