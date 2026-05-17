---
name: legalcode-case-timeline-generator
description: >
  Codex orchestration skill for designing or running a case timeline over one or more local
  folders. Use when the user wants a chronology, event map, or investigative timeline from
  PDFs, DOCX files, emails, scans, or mixed evidence and wants a canonical JSON plus a
  portable static HTML report rendered locally.
disable-model-invocation: true
---

# Codex Case Timeline Orchestrator

> This is a project-local Codex tool skill. It is not the end-user legal skill in `skills/`.
> Use it to execute, prototype, or refine the timeline workflow in this repository.

## Purpose

This skill tells Codex how to run a case timeline locally:
- inventory and normalize evidence files
- extract events and obligations into a stable schema
- preserve contradictions instead of flattening them
- render a portable HTML chronology from JSON

Use the paired legal skill at:
- `skills/general/litigation/legalcode-case-timeline-builder/SKILL.md`

Use this Codex skill when the user wants:
- an implementation plan
- a local prototype or script
- a corpus run over folders in the workspace
- a Codex-native execution recipe rather than a pure Claude skill definition

## Core Principle

Separate the workflow into two planes:

1. **Deterministic plane**
   - file discovery
   - hashing and dedupe
   - conversion and OCR
   - schema validation
   - HTML rendering

2. **Model plane**
   - first-pass event extraction
   - obligation extraction
   - contradiction detection
   - gap explanation
   - optional narrative synthesis

Do not blur those planes. When a shell tool can do the work reproducibly, keep it out of the
reasoning layer.

## First Actions

1. Confirm the requested folders or files.
2. Confirm whether the user wants design-only or an actual corpus run.
3. Inspect the environment for conversion and render tools.
4. Decide whether to use:
   - Codex-native execution only
   - Claude CLI extraction workers
   - a hybrid path

## Environment Check

Run this early:

```bash
command -v claude >/dev/null 2>&1 && echo HAVE_CLAUDE=1 || echo HAVE_CLAUDE=0
command -v pdftotext >/dev/null 2>&1 && echo HAVE_PDFTOTEXT=1 || echo HAVE_PDFTOTEXT=0
command -v pandoc >/dev/null 2>&1 && echo HAVE_PANDOC=1 || echo HAVE_PANDOC=0
command -v ocrmypdf >/dev/null 2>&1 && echo HAVE_OCRMYPDF=1 || echo HAVE_OCRMYPDF=0
command -v markitdown >/dev/null 2>&1 && echo HAVE_MARKITDOWN=1 || echo HAVE_MARKITDOWN=0
command -v python3 >/dev/null 2>&1 && echo HAVE_PYTHON3=1 || echo HAVE_PYTHON3=0
command -v node >/dev/null 2>&1 && echo HAVE_NODE=1 || echo HAVE_NODE=0
```

Report the tool picture before launching larger work.

## Recommended Working Directory Layout

```text
.tmp/case-timeline/<run-id>/
  manifest.json
  converted/
  extractions/
  consolidated/
  outputs/
    timeline-data.json
    report.html
    timeline.md
  logs/
```

If the user only wants skill design, describe this structure but do not create it unless needed.

## Input Contract

Normalize every request into:

```json
{
  "sources": [
    {
      "path": "/abs/path/to/folder-or-file",
      "label": "optional user-facing group"
    }
  ],
  "objective": "case_strategy",
  "output_dir": "/abs/path/to/.tmp/case-timeline/run-id",
  "render_html": true
}
```

Use `scripts/case-timeline-report/schema.md` as the canonical output contract.

## Execution Paths

### Path A: Hybrid Codex + Claude CLI

Use when `claude` exists and the user wants low-cost extraction at scale.

Pattern:
1. Codex inventories and converts files.
2. Codex writes or feeds stable extraction prompts.
3. `claude -p --model haiku` handles first-pass extraction.
4. Codex consolidates and validates JSON.
5. Codex renders outputs deterministically.

### Path B: Codex-Native

Use when:
- `claude` CLI is unavailable
- the corpus is small
- the user wants a pure Codex flow

Pattern:
1. Codex inventories and converts files.
2. Codex uses sub-agents only if the user explicitly asked for agent-team work.
3. Codex validates the returned event and obligation JSON.
4. Codex renders outputs locally.

### Path C: Design-Only

Use when the user wants the skill and architecture without executing a corpus run.

Outputs:
- skill files
- schema
- report generator
- example JSON
- implementation notes

## Canonical Timeline Contract

Keep `timeline-data.json` as the single source of truth.

Required top-level sections:
- `meta`
- `events`
- `obligations`

Recommended sections:
- `entities`
- `contradictions`
- `gaps`

Each event should carry:
- date
- date precision
- evidence type
- status
- confidence
- provenance

Do not let summary prose exist only inside the HTML renderer.

## Agent Decomposition

If the user explicitly wants agent-team execution, use disjoint roles:

| Agent | Responsibility | Output |
|------|----------------|--------|
| inventory agent | enumerate files, hash duplicates, classify types | manifest fragment |
| conversion agent | convert documents into reviewable text | normalized files |
| extraction agent | extract events and obligations for assigned files | extraction JSON |
| verification agent | review weak or conflicting events | verified JSON |
| synthesis agent | produce matter-level summaries and issues | summary markdown |

Do not duplicate ownership. Each agent should own a bounded write surface or result set.

## Workflow

### Step 1: Inventory

Build a manifest with:
- document id
- absolute path
- extension
- size
- hash where feasible
- source bucket

Prefer `rg --files`, `find`, and local hashing tools. Keep discovery deterministic.

### Step 2: Incremental extraction

Before launching fresh extraction:
- inspect the run directory for prior extraction artifacts
- skip unchanged documents when the mapping is deterministic

This prevents duplicate work on reruns.

### Step 3: Conversion

Use deterministic converters first:
- `pdftotext`
- `pandoc`
- `markitdown`
- `ocrmypdf`

Persist converted text before asking a model to reason about it.

### Step 4: Extraction

Per document, extract:
- events
- obligations
- people and organizations
- knowledge events
- contradiction candidates

Return parserable JSON whenever possible.

### Step 5: Consolidation

Merge into canonical JSON with these rules:
- sort by date
- preserve precision markers
- normalize category and issue labels
- keep contradictory items as separate events with `contradictionIds`
- attach source metadata to every material event

### Step 6: Verification

Escalate:
- low-confidence events
- missing dates
- unsupported summaries
- orphan contradictions
- orphan obligations

Prefer a smaller verified timeline over a larger unverifiable one.

### Step 7: Render

Generate the portable HTML from JSON only:

```bash
node scripts/case-timeline-report/generate-report.mjs \
  /abs/path/to/timeline-data.json \
  /abs/path/to/report.html \
  --title "Matter timeline"
```

The renderer is local and self-contained. No external assets or network requests.

## HTML Framework Expectations

The renderer should preserve the core UX patterns from the prototype:
- timeline rail
- filter chips
- contradiction visibility
- gap visibility
- obligation lane
- detail drawer

Do not treat the HTML as an editable source artifact. It is a render target.

## Guardrails

Do not:
- embed data manually in HTML and drift from JSON
- overwrite contradictions to make the story cleaner
- omit page or document references for material points when available
- mix locale-specific presentation labels into the canonical schema unless requested
- state legal conclusions as facts without provenance

## Deliverables

When the task is complete, report:
- execution path used
- output paths
- corpus size
- contradiction count
- gap count
- weak-confidence hotspots
