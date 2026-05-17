---
name: legalcode-case-timeline-builder
description: >
  Build defensible litigation chronologies from document corpora using a dual-path
  multi-agent pipeline. Process PDFs, Word documents, emails, images, and other
  evidence formats at scale — converting to markdown, extracting dates, events,
  entities, and relationships using Claude Haiku workers in parallel, validating
  sequences with Sonnet, and synthesizing final timelines with Opus.
  Supports two execution paths: (1) Claude Code CLI scripts (`claude -p --model haiku`)
  for maximum throughput on large corpora, and (2) in-skill sub-agent fallback via
  the Task tool when CLI is unavailable. Produces citation-linked master timelines,
  issue timelines, entity timelines, deadline calendars, and court-ready outputs
  (FRCP Rule 56 statements, proposed findings of fact) across jurisdictions.
  Handles 10K+ document corpora with automatic chunking, deduplication, privilege
  screening, protective order designations, and conflict resolution.
allowed-tools: Read, Bash(grep:*), Bash(ls:*), Bash(find:*), Bash(wc:*), Bash(claude:*), Bash(sh:*), Bash(bash:*), Bash(python3:*), Bash(pandoc:*), Bash(magic-pdf:*), Bash(pdftotext:*), Bash(ocrmypdf:*), Bash(markitdown:*), Glob, WebSearch, WebFetch, Task
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Case Timeline Builder

> **Disclaimer**: This skill provides a framework for AI-assisted litigation chronology
> construction. It does not constitute legal advice. All outputs must be reviewed by
> qualified legal counsel licensed in the relevant jurisdiction before use. Procedural
> and evidentiary statements may be incomplete or outdated; verify authoritative sources
> before relying on any conclusion. AI-extracted dates and events may contain errors;
> verify all critical facts against original sources. Any cited authority marked
> `[VERIFY]` has not been independently validated and must be confirmed before reliance.

---

## Purpose and Scope

This skill builds comprehensive, defensible litigation chronologies from heterogeneous
document corpora using a **dual-path multi-agent pipeline**. It processes raw documents
at scale, converts them to markdown, extracts temporal and entity information using
parallel Haiku workers, validates sequences, resolves contradictions, and produces
multiple timeline views optimized for different litigation phases and use cases.

The skill supports two execution architectures:

1. **CLI Path** (preferred for large corpora): Shell scripts that invoke `claude -p --model haiku`
   workers in parallel, orchestrated by `timeline-build.sh` and stage scripts in
   `scripts/corpus-processing/`. Maximum throughput, cost tracking, resumable.

2. **Sub-Agent Path** (fallback): When the `claude` CLI is not installed or not available,
   the skill falls back to launching Task tool sub-agents with `model: "haiku"` from within
   the skill execution context. Same extraction logic, same prompts, lower throughput.

**Covers:**
- **Document conversion**: PDF, DOCX, MSG, EML, PST, HTML, images, transcripts, spreadsheets to markdown
- **Multi-agent extraction**: Parallel date/event/entity/relationship extraction using Haiku workers
- **Coreference resolution**: Cross-document entity linking, alias tables, name normalization
- **Timeline construction**: Master chronology, issue timelines, entity timelines, relationship maps
- **Quality assurance**: Contradiction detection, sequence validation, gap analysis, confidence auditing
- **Privilege screening**: Privilege log integration, redacted timeline entries, parallel privilege chronology
- **Court-ready outputs**: FRCP Rule 56 statements of fact, proposed findings, trial exhibits
- **Output generation**: Markdown, JSON, CSV, HTML interactive timeline, EDRM XML, CaseMap TLF
- **Regulatory patterns**: MDL/class action timelines, regulatory investigation chronologies
- **Cross-border matters**: Timezone normalization, multi-jurisdiction deadline tracking

**Does not:**
- Replace jurisdiction-specific legal advice or counsel judgment
- Determine witness credibility as a final legal finding
- Draft final pleadings without human review
- Authenticate documents for court submission
- Make privilege determinations (flags for review only)
- Waive any privilege (redacts rather than excludes)

**Related skills:**
- `legalcode-early-case-assessment` — Pre-discovery case evaluation
- `legalcode-privilege-review` — Privilege classification for productions
- `legalcode-breach-severity-assessment` — Incident timeline construction
- `litigation-hold-notice` — Preservation workflows

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify governing law, forum, and
procedural track first, then localize timeline treatment and admissibility implications.

**[JURISDICTION-SPECIFIC]** Localize at minimum:
- Discovery/disclosure scope and scheduling controls
- Evidence authentication and admissibility thresholds (FRE 901, 1002 or equivalent) [VERIFY]
- Witness statement/deposition practice and contradiction use
- Preservation and spoliation standards (sanctions framework)
- Deadline-calculation rules (business days, holidays, service method adjustments)
- Court-specific filing requirements and local rules
- Date format conventions (MM/DD vs DD/MM vs YYYY-MM-DD)
- Privilege doctrines (attorney-client, work product, joint defense)
- Protective order standard designations

**Reference anchors frequently needed:**
- **U.S. federal**: FRCP Rules 16, 26, 34, 37, 56; FRE 901, 1002; ESI proportionality (Rule 26(b)(1)) [VERIFY]
- **England & Wales**: CPR Part 31 and/or PD 57AD track; Civil Evidence Act 1995; Technology and Construction Court Guide [VERIFY]
- **Australia (Federal)**: Federal Court Rules 2011 (Cth), Federal Court Act 1976 (Cth) s 37M, CPN-1 and GPN-TECH [VERIFY]
- **Canada**: Provincial rules vary; Federal Courts Rules SOR/98-106; Sedona Canada Principles [VERIFY]
- **EU (GDPR context)**: Regulation (EU) 2016/679 (GDPR) for data processing timelines; cross-border transfer chronologies [VERIFY]

---

## Interactive Clarification

Use interactive clarification whenever the answer materially changes scope, processing
strategy, or timeline outputs. If information is already provided, skip the question.
Proceed with stated defaults when the user does not respond.

**CLARIFY block 1: Timeline objective**
- Options: `case strategy`, `summary judgment`, `deposition prep`, `trial prep`, `settlement`, `regulatory response`, `MDL coordination`, `class certification`
- Default: `case strategy`
- Why it matters: Changes event granularity, output emphasis, filtering criteria, and court-ready format.

**CLARIFY block 2: Side represented**
- Options: `claimant/plaintiff`, `defendant/respondent`, `regulatory/enforcement`, `class counsel`, `mixed/neutral`
- Default: `mixed/neutral`
- Why it matters: Changes contradiction framing, priority issues, narrative direction, and burden analysis.

**CLARIFY block 3: Document corpus**
- Options: `file paths provided`, `directory to scan`, `document manifest`, `incremental update`
- Sub-options for formats: PDF, DOCX, MSG/EML/PST, images, transcripts, spreadsheets, mixed
- Default: `directory to scan` with `mixed` formats
- Why it matters: Determines document processing pipeline configuration and tool selection.

**CLARIFY block 4: Corpus size and budget**
- Options: `small (<100 docs)`, `medium (100-1000)`, `large (1000-10000)`, `enterprise (10K+)`
- Budget tolerance: `strict ($X cap)`, `moderate (flag at $X)`, `flexible`
- Default: `medium` with `moderate` budget
- Why it matters: Controls batch sizing, parallelization degree, model selection, and whether to use CLI or sub-agent path.

**CLARIFY block 5: Execution path preference**
- Options: `auto-detect`, `CLI scripts only`, `sub-agents only`
- Default: `auto-detect` (check for `claude` CLI, fall back to sub-agents)
- Why it matters: Determines whether to use `timeline-build.sh` pipeline or in-skill Task tool agents.

**CLARIFY block 6: Date precision policy**
- Options: `exact date required`, `allow month-only`, `allow approximate`, `preserve all with precision markers`
- Default: `preserve all with precision markers`
- Why it matters: Prevents false certainty for incomplete records; affects timeline visualization.

**CLARIFY block 7: Contradiction policy**
- Options: `strict (flag all)`, `material-only`, `strategy-filtered`
- Default: `material-only`
- Why it matters: Controls noise vs. issue focus in output. Strategy-filtered requires side/issues context.

**CLARIFY block 8: Privilege handling**
- Options: `skip privilege screening`, `flag potential privilege`, `integrate with privilege log`, `parallel privilege chronology`
- Default: `flag potential privilege`
- Why it matters: Prevents inadvertent privilege waiver; determines whether privileged content enters timeline.

**CLARIFY block 9: Protective order designations**
- Options: `none`, `standard confidential/highly-confidential`, `custom designation scheme`
- Default: `none`
- Why it matters: Controls output labeling, redaction requirements, and distribution restrictions.

**CLARIFY block 10: Timezone baseline**
- Options: `source-local`, `single normalized timezone (specify)`, `dual-view`
- Default: `source-local` with notation
- Why it matters: Avoids timeline distortion in cross-border matters.

**CLARIFY block 11: Output formats**
- Options: `markdown only`, `JSON + markdown`, `full export (all formats)`, `trial-ready`, `EDRM XML`
- Default: `JSON + markdown`
- Why it matters: Determines post-processing and export pipeline; trial-ready adds FRCP-formatted outputs.

---

## Dual-Path Architecture

This skill operates in one of two execution modes, detected automatically at runtime.
Both paths produce identical outputs. The CLI path is preferred for large corpora
(>100 documents) because it offers true OS-level parallelism, cost tracking, and
resumable execution.

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     RUNTIME DETECTION                                   │
│                                                                         │
│   if command -v claude &>/dev/null; then                                │
│       → CLI PATH (timeline-build.sh pipeline)                           │
│   else                                                                  │
│       → SUB-AGENT PATH (Task tool with model: "haiku")                  │
│   fi                                                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
              ▼                                   ▼
┌──────────────────────────┐        ┌──────────────────────────┐
│     CLI PATH             │        │   SUB-AGENT PATH         │
│                          │        │                          │
│ timeline-build.sh        │        │ Task tool orchestration  │
│   ├── Stage 1: Convert   │        │   ├── Bash: Convert docs │
│   ├── Stage 2: Extract   │        │   ├── Task(haiku): Extract│
│   │   └── claude -p      │        │   │   └── per-document   │
│   │       --model haiku   │        │   ├── Task(haiku): Merge │
│   │       --max-turns 1   │        │   ├── Task(sonnet): Valid│
│   │       --output-format │        │   ├── Task(opus): Synth  │
│   │           json        │        │   └── Bash: Output gen   │
│   ├── Stage 3: Consolidate│       │                          │
│   ├── Stage 4: Validate   │       │ Lower throughput but     │
│   │   └── claude -p       │       │ works without CLI install│
│   │       --model sonnet  │       │                          │
│   ├── Stage 5: Synthesize │       └──────────────────────────┘
│   │   └── claude -p       │
│   │       --model opus    │
│   └── Stage 6: Output     │
│                           │
│ OS-level parallelism      │
│ Cost tracking built-in    │
│ Resumable on failure      │
└───────────────────────────┘
```

### CLI Path: Script Pipeline

**Location**: `scripts/corpus-processing/`

**Master orchestrator**: `timeline-build.sh`
```bash
# Initialize pipeline workspace for a document corpus
./scripts/corpus-processing/timeline-build.sh init /path/to/documents

# Run full pipeline (all 6 stages)
./scripts/corpus-processing/timeline-build.sh run

# Run specific stages
./scripts/corpus-processing/timeline-build.sh run --from 2 --to 4

# Check pipeline status
./scripts/corpus-processing/timeline-build.sh status

# Retry failed items
./scripts/corpus-processing/timeline-build.sh retry --stage 2

# Clean pipeline state
./scripts/corpus-processing/timeline-build.sh clean
```

**Stage scripts** (in `scripts/corpus-processing/stages/`):

| Stage | Script | Model | Cost | Purpose |
|-------|--------|-------|------|---------|
| 1 | `stage-1-convert.sh` | None (local) | $0 | Document conversion to markdown |
| 2 | `stage-2-extract.sh` | Haiku | ~$3-5/1K docs | Parallel date/event/entity extraction |
| 3 | `stage-3-consolidate.sh` | None (Python) | $0 | Merge, deduplicate, assign IDs |
| 4 | `stage-4-validate.sh` | Sonnet | ~$1-3/1K docs | Contradiction/sequence/gap detection |
| 5 | `stage-5-synthesize.sh` | Opus | ~$2-5 total | Final timeline construction |
| 6 | `stage-6-output.sh` | None (Python) | $0 | Format export (MD, JSON, CSV, HTML) |

**Supporting scripts**:
| Script | Purpose |
|--------|---------|
| `01-discover-and-classify.sh` | File discovery, SHA-256 hashing, manifest generation |
| `02-parallel-process.sh` | Generic parallel worker dispatch |
| `03-aggregate-results.sh` | Result merging across workers |
| `04-resilient-runner.sh` | Retry logic, exponential backoff, checkpoint/resume |
| `05-cost-tracker.sh` | Per-worker and cumulative cost tracking with budget caps |
| `example-processor.sh` | Template for custom processing scripts |
| `patterns-reference.sh` | CLI flag patterns and reference examples |

**CLI extraction command pattern** (Stage 2 core):
```bash
claude -p \
  --model haiku \
  --output-format json \
  --max-turns 1 \
  --max-budget-usd 0.50 \
  --no-session-persistence \
  --tools "" \
  --system-prompt-file "$PROMPTS_DIR/haiku-date-extraction.md" \
  "Extract all dates, events, and temporal references from this document:

$(cat "$converted_markdown_file")"
```

Key CLI flags explained:
- `--model haiku` — Use Haiku for cost-efficient high-volume extraction
- `--output-format json` — Get structured JSON with `result` field
- `--max-turns 1` — Single response, no agentic loop (extraction only)
- `--max-budget-usd 0.50` — Cost cap per worker invocation
- `--no-session-persistence` — Don't save session state (batch worker)
- `--tools ""` — Disable all tools (pure extraction, no file access needed)
- `--system-prompt-file` — Load extraction system prompt from file

**Parallel execution** (background job pool):
```bash
MAX_PARALLEL=8
running_pids=()

for doc in "${documents[@]}"; do
  # Wait for a slot if pool is full
  while [[ ${#running_pids[@]} -ge $MAX_PARALLEL ]]; do
    for i in "${!running_pids[@]}"; do
      if ! kill -0 "${running_pids[$i]}" 2>/dev/null; then
        wait "${running_pids[$i]}" || true
        unset 'running_pids[$i]'
      fi
    done
    running_pids=("${running_pids[@]}")
    sleep 0.5
  done

  # Spawn Haiku worker in background
  run_haiku_extraction "$doc" &
  running_pids+=($!)
done

# Wait for all remaining workers
wait "${running_pids[@]}" 2>/dev/null || true
```

### Sub-Agent Path: Task Tool Fallback

When `claude` CLI is not available, the skill uses the Task tool to launch sub-agents.
This path mirrors the CLI pipeline stage-by-stage but executes within the skill context.

**Runtime detection** (execute at the start of every workflow run):
```bash
# Check if claude CLI is available
if command -v claude &>/dev/null; then
  EXECUTION_PATH="cli"
  # Verify it actually works
  if claude --version &>/dev/null 2>&1; then
    echo "CLI path: claude $(claude --version 2>&1 | head -1)"
  else
    EXECUTION_PATH="subagent"
    echo "CLI found but not functional. Falling back to sub-agent path."
  fi
else
  EXECUTION_PATH="subagent"
  echo "claude CLI not found. Using sub-agent path."
fi
```

**Sub-agent extraction pattern** (replaces Stage 2 CLI workers):

For each document, launch a Haiku Task tool sub-agent:

```
Task tool call:
  subagent_type: "general-purpose"
  model: "haiku"
  description: "Extract dates and events from [DOC-00001]"
  prompt: |
    You are a Date and Event Extraction Agent for legal documents.

    Extract ALL dates, events, and temporal references from the following document.
    [... full extraction system prompt ...]

    Document content:
    [... markdown content of the document ...]

    Return a JSON object with the extraction results.
```

**Sub-agent validation pattern** (replaces Stage 4 CLI workers):
```
Task tool call:
  subagent_type: "general-purpose"
  model: "sonnet"
  description: "Validate timeline segment [CHUNK-001]"
  prompt: |
    You are a Timeline Validation Agent.
    [... validation system prompt ...]
    [... consolidated events JSON ...]
```

**Sub-agent synthesis pattern** (replaces Stage 5):
```
Task tool call:
  subagent_type: "general-purpose"
  model: "opus"
  description: "Synthesize final timeline for [Matter Name]"
  prompt: |
    You are a Litigation Timeline Synthesis Agent.
    [... synthesis system prompt ...]
    [... all consolidated + validated data ...]
```

**Parallelism in sub-agent path**: Launch multiple Task tool calls in the same
message to process documents concurrently. The Task tool supports concurrent
execution when calls are independent.

**Throughput comparison**:
| Metric | CLI Path | Sub-Agent Path |
|--------|----------|----------------|
| Max parallel workers | OS limit (typically 8-16) | ~4-6 concurrent Tasks |
| Cost tracking | Built-in (`05-cost-tracker.sh`) | Manual estimation |
| Resume on failure | Checkpoint files | Re-run from last output |
| Best for | >100 documents | <100 documents |
| Setup required | `claude` CLI installed | None (works in any skill context) |

### Model Selection Strategy

| Model | Role | Use Case | Approximate Cost/MTok |
|-------|------|----------|-----------------------|
| **Claude Haiku 4.5** | Extraction workers | High-volume date/event/entity extraction | Input: $0.80 / Output: $4.00 |
| **Claude Sonnet 4.5** | Validation agents | Contradiction detection, quality checks | Input: $3.00 / Output: $15.00 |
| **Claude Opus 4.5** | Orchestrator/Synthesis | Planning, conflict resolution, complex reasoning | Input: $15.00 / Output: $75.00 |

**Cost estimation for typical corpora:**

| Corpus Size | Haiku Extraction | Sonnet Validation | Opus Synthesis | Total |
|-------------|------------------|-------------------|----------------|-------|
| 50 docs | ~$1-2 | ~$0.50 | ~$2 | ~$3-5 |
| 500 docs | ~$5-10 | ~$2-4 | ~$3-5 | ~$10-20 |
| 5,000 docs | ~$30-50 | ~$10-20 | ~$5-10 | ~$45-80 |
| 50,000 docs | ~$300-500 | ~$50-100 | ~$10-15 | ~$360-615 |

---

## Workflow

### Phase 0: Runtime Detection and Pipeline Selection

Before any processing begins, detect the execution environment and select the
appropriate pipeline path.

**Step 0.1: Check execution environment**

```bash
# Detect available tools
HAVE_CLAUDE=false
HAVE_MAGIC_PDF=false
HAVE_PANDOC=false
HAVE_PDFTOTEXT=false
HAVE_OCRMYPDF=false
HAVE_PYTHON3=false
HAVE_MARKITDOWN=false

command -v claude    &>/dev/null && HAVE_CLAUDE=true
command -v magic-pdf &>/dev/null && HAVE_MAGIC_PDF=true
command -v pandoc    &>/dev/null && HAVE_PANDOC=true
command -v pdftotext &>/dev/null && HAVE_PDFTOTEXT=true
command -v ocrmypdf  &>/dev/null && HAVE_OCRMYPDF=true
command -v python3   &>/dev/null && HAVE_PYTHON3=true
command -v markitdown &>/dev/null && HAVE_MARKITDOWN=true
```

**Step 0.2: Select execution path**

| Condition | Path Selected | Rationale |
|-----------|---------------|-----------|
| `claude` available + corpus >100 docs | CLI Path | Maximum throughput |
| `claude` available + corpus ≤100 docs | Either (user preference) | Both viable |
| `claude` NOT available | Sub-Agent Path | Only option |
| User explicitly selects | Respect user choice | Override auto-detect |

**Step 0.3: Verify minimum requirements**

For CLI path:
- [ ] `claude` CLI is installed and functional
- [ ] At least one PDF converter (magic-pdf, pandoc, or pdftotext)
- [ ] `python3` available (for consolidation and output stages)
- [ ] Sufficient disk space for converted documents (~2-5x corpus size)

For sub-agent path:
- [ ] Task tool is available in allowed-tools
- [ ] At least one PDF converter OR willingness to use sub-agent vision for PDFs
- [ ] `python3` available (or fallback to sub-agent for consolidation)

**Step 0.4: Report environment to user**

Present a summary of detected tools and selected path. Example:

```
Pipeline Environment:
  Execution path: CLI (claude detected)
  PDF conversion: magic-pdf (MinerU)
  DOCX conversion: pandoc
  Email parsing: markitdown
  OCR: ocrmypdf
  Python: 3.12.1
  Parallel workers: 8

Estimated processing:
  Corpus: 1,247 documents (mixed formats)
  Estimated cost: $15-25
  Estimated time: 20-40 minutes
```

---

### Phase 1: Matter Frame Definition

**Step 1.1: Capture matter context**
- Case name, forum, governing law, procedural stage
- Timeline objective (strategy, deposition, trial, summary judgment, regulatory, MDL)
- Key parties and their roles (plaintiff, defendant, third party, class, regulator)
- Date range of interest
- Key issues for issue-threaded timelines
- Side represented (affects narrative framing)

**Step 1.2: Define scope boundaries**
- Issues to include/exclude
- Custodians in scope
- Document types to process
- Confidence thresholds for inclusion
- Privilege screening rules
- Protective order designation scheme

**Step 1.3: Configure pipeline parameters**

**Output**: `matter_frame.yaml` (also serves as `config.yaml` for CLI path)
```yaml
matter_frame:
  case_name: "[Matter Name]"
  case_number: "[Case No.]"
  forum: "[Court/Tribunal]"
  governing_law: "[Jurisdiction]"
  stage: "[Pleadings | Discovery | Motion | Trial | Appeal]"
  objective: "[strategy | deposition | trial | settlement | regulatory | mdl]"
  side: "[plaintiff | defendant | class_counsel | regulatory | mixed]"
  date_range:
    start: "YYYY-MM-DD"
    end: "YYYY-MM-DD"
  issues:
    - id: "ISS-001"
      label: "[Issue 1]"
      keywords: ["keyword1", "keyword2"]
    - id: "ISS-002"
      label: "[Issue 2]"
      keywords: ["keyword3", "keyword4"]
  parties:
    - name: "[Party Name]"
      role: "[Plaintiff | Defendant | Third Party | Class Member]"
      aliases: ["[Alternative Name]", "[DBA]"]
  custodians:
    - name: "[Custodian Name]"
      role: "[Executive | Counsel | Witness]"
      date_range: "[optional scope limitation]"
  scope_exclusions:
    - "[Excluded issue or topic]"

pipeline:
  execution_path: "auto"  # auto | cli | subagent
  max_parallel: 8
  max_budget_usd: 50.00
  haiku_budget_per_doc: 0.50
  date_precision_policy: "preserve_all"
  contradiction_policy: "material-only"
  privilege_handling: "flag_potential"
  protective_order: "none"
  timezone_baseline: "source-local"
  output_formats: "markdown json"

quality:
  min_ocr_confidence: 0.85
  min_extraction_confidence: 0.40
  validation_sample_rate: 1.0  # 1.0 = validate all; 0.1 = 10% sample
  require_source_citation: true
```

---

### Phase 2: Document Inventory and Conversion

This phase runs entirely locally with no API costs.

**Step 2.1: Build document inventory**

**CLI path**: Use `01-discover-and-classify.sh`:
```bash
./scripts/corpus-processing/01-discover-and-classify.sh /path/to/documents
```

**Sub-agent path**: Use Bash tool within the skill:
```bash
find /path/to/documents -type f \
  \( -name "*.pdf" -o -name "*.docx" -o -name "*.doc" \
     -o -name "*.msg" -o -name "*.eml" -o -name "*.pst" \
     -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \
     -o -name "*.tiff" -o -name "*.html" -o -name "*.htm" \
     -o -name "*.txt" -o -name "*.csv" -o -name "*.xlsx" \) \
  | sort
```

For each document, capture:
- Unique `source_id` (e.g., `DOC-00001`)
- Original file path
- File type (extension-based + magic byte validation)
- File size in bytes
- SHA-256 hash (for deduplication and integrity)
- Creation/modification dates from filesystem metadata
- Custodian (from directory structure or manifest)
- Bates range (if available from production metadata)

**Step 2.2: Detect and handle duplicates**

Compute SHA-256 for each file. Group by hash. For duplicates:
- Keep earliest custodian copy as primary
- Record all duplicate paths in manifest
- Track cross-custodian overlap (discovery significance)

**Step 2.3: Convert documents by type**

#### PDF Processing Pipeline

**Tool fallback chain**:
1. **MinerU** (`magic-pdf`) — Best for complex layouts, tables, multi-column
2. **MarkItDown** (`markitdown`) — Good for simpler PDFs
3. **Pandoc** (`pandoc`) — Acceptable quality
4. **pdftotext** (poppler) — Basic text extraction fallback
5. **OCR pipeline** (`ocrmypdf` → `pdftotext`) — For scanned/image PDFs

```bash
# MinerU (preferred)
magic-pdf -p "$pdf_file" -o "$output_dir" -m auto

# MarkItDown fallback
markitdown "$pdf_file" > "$output_file"

# pdftotext fallback
pdftotext -layout "$pdf_file" "$output_file"

# Scanned PDF: OCR first, then extract
ocrmypdf --force-ocr "$pdf_file" "$ocr_output" && pdftotext "$ocr_output" "$output_file"
```

**Quality checks for PDFs**:
- [ ] OCR confidence > 85% (or flag for manual review)
- [ ] All pages extracted (page count matches original)
- [ ] Tables properly formatted (detect garbled table text)
- [ ] Images referenced with position markers
- [ ] No truncation at page boundaries

#### Word Document Processing

**Primary**: Pandoc with track changes preservation (critical for litigation):
```bash
# Preserve track changes, comments, and metadata
pandoc --from=docx --to=markdown --track-changes=all "$docx_file" -o "$output_file"
```

**Track changes treatment**: Track changes are critical evidence in contract disputes.
The `--track-changes=all` flag preserves insertions, deletions, and comments as
visible markup in the markdown output.

**Metadata extraction**: Extract author, creation date, modification history,
comments, and custom properties from DOCX metadata.

#### Email Processing (MSG/EML/PST)

**Extract for each email:**
- Sender, recipients (To/CC/BCC) — all are potential custodians/witnesses
- Date/time with timezone (use header Date, not file system date)
- Subject line
- Body (plain text preferred; HTML converted to markdown)
- Attachments (process each as separate document with parent linkage)
- Threading information (Message-ID, In-Reply-To, References headers)
- Transport headers (for authenticity, routing analysis)

**Tool fallback chain**:
1. **MarkItDown** — Handles MSG and EML formats
2. **extract-msg** (Python) — For MSG files specifically
3. **Python email stdlib** — For EML files
4. **readpst** — For PST archive extraction to individual EML files

**Email markdown format:**
```markdown
---
source_id: EMAIL-00001
type: email
sender: john.smith@company.com
recipients:
  to: [jane.doe@vendor.com]
  cc: [legal@company.com]
  bcc: []
date: 2025-01-15T09:45:00-05:00
subject: "RE: Contract Negotiation"
thread_id: "<abc123@mail.company.com>"
in_reply_to: "<xyz789@mail.vendor.com>"
attachments:
  - name: Contract_Draft_v3.docx
    source_id: EMAIL-00001-ATT-001
    size_bytes: 245000
custodian: "John Smith"
---

# Email: RE: Contract Negotiation

**From:** john.smith@company.com (John Smith)
**To:** jane.doe@vendor.com (Jane Doe)
**CC:** legal@company.com
**Date:** January 15, 2025 at 9:45 AM EST
**Subject:** RE: Contract Negotiation

---

[Email body content in markdown]

---

**Attachments:**
1. Contract_Draft_v3.docx → see EMAIL-00001-ATT-001
```

#### Image Processing (Vision Model)

Images (exhibits, photographs, screenshots, diagrams) require vision model analysis.

**CLI path**: Use Claude with vision via piping:
```bash
# Claude CLI can read image files directly
claude -p --model haiku \
  --max-turns 1 \
  --max-budget-usd 0.25 \
  --system-prompt "You are a litigation document analyst. Describe this image for timeline purposes. Extract any visible dates, people, locations, text, and events. Output structured JSON." \
  "Analyze this image: $(base64 < "$image_file")"
```

**Sub-agent path**: Use Task tool with the image file path:
```
Task tool call:
  subagent_type: "general-purpose"
  model: "haiku"
  description: "Analyze image [IMG-00001]"
  prompt: |
    Read the image file at [path] and analyze it for litigation timeline purposes.
    Extract: dates, people, locations, text, events, objects, metadata.
    Output structured JSON.
```

#### Transcript Processing

Deposition transcripts, hearing transcripts, and recorded interview transcripts:
- Parse page:line citation format (e.g., "125:14-126:3")
- Extract witness name, date, and examining counsel
- Preserve Q&A structure for contradiction analysis
- Link exhibits referenced in testimony to document manifest

#### Spreadsheet Processing

For Excel/CSV files containing structured data (financial records, logs, inventories):
- Extract column headers as field names
- Preserve date columns with format detection
- Flag monetary columns for amount extraction
- Convert to markdown table or JSON depending on size

**Step 2.4: Generate document manifest**

**Output**: `document_manifest.json`
```json
{
  "manifest_id": "MAN-2026-00001",
  "generated_at": "2026-02-28T14:30:00Z",
  "corpus_path": "/path/to/documents",
  "documents": [
    {
      "source_id": "DOC-00001",
      "original_path": "/productions/batch1/document.pdf",
      "converted_path": ".timeline/converted/DOC-00001.md",
      "document_type": "pdf",
      "page_count": 15,
      "file_size_bytes": 245000,
      "sha256": "a1b2c3...",
      "created_date": "2024-03-15",
      "modified_date": "2024-03-20",
      "custodian": "John Smith",
      "bates_range": "ACME_000001-000015",
      "processing_status": "converted",
      "conversion_tool": "magic-pdf",
      "ocr_applied": true,
      "ocr_confidence": 0.92,
      "duplicate_of": null,
      "attachments": [],
      "parent_id": null
    }
  ],
  "summary": {
    "total_documents": 1500,
    "by_type": {"pdf": 800, "docx": 200, "email": 450, "image": 50},
    "by_custodian": {"John Smith": 300, "Jane Doe": 450},
    "processing_complete": 1485,
    "processing_failed": 15,
    "duplicates_found": 42,
    "total_pages": 12500,
    "total_size_mb": 3400
  }
}
```

---

### Phase 3: Multi-Agent Extraction

This is the core extraction phase. Each converted document is processed by a Haiku
worker to extract dates, events, entities, and relationships. Both execution paths
produce the same JSON output schema.

**Step 3.1: Prepare extraction prompts**

Write system prompt files to `.timeline/prompts/` (CLI path) or embed in Task
tool prompts (sub-agent path).

#### Date/Event Extraction System Prompt

```markdown
You are a Date and Event Extraction Agent specialized in legal documents.

## Task
Extract ALL dates, events, and temporal references from the document provided.
Return a JSON object matching the schema below. Extract exhaustively — it is
better to over-extract than to miss events.

## Extraction Rules

1. **Explicit dates**: "January 15, 2025", "01/15/2025", "2025-01-15", "15th January 2025"
2. **Relative dates**: "two weeks later", "the following month", "the next day"
   - Anchor to the nearest explicit date in the document
   - If no anchor available, mark precision as "relative" with anchor_text
3. **Fuzzy dates**: "early 2024", "around March", "Q3 2023", "mid-year"
4. **Date ranges**: "from January to March 2025", "between 2020 and 2022"
5. **Deadlines**: "within 30 days", "90-day notice period", "no later than June 1"
6. **Recurrence**: "every Monday", "quarterly", "annually on the anniversary date"
7. **Implicit dates**: References to known events ("after the IPO", "pre-merger")

## Event Types
- meeting, call, communication, negotiation
- transaction, payment, transfer, delivery
- filing, motion, order, ruling, judgment
- signing, execution, amendment, termination
- deadline, notice, demand, breach
- investigation, audit, inspection, review
- testimony, deposition, hearing, trial
- other

## Output Schema
{
  "source_id": "string — document source_id from frontmatter",
  "extraction_model": "haiku",
  "extracted_at": "ISO-8601 timestamp",
  "events": [
    {
      "raw_text": "original text as it appears in document",
      "normalized_date": "YYYY-MM-DD or YYYY-MM or YYYY or ~YYYY-MM-DD",
      "date_end": "for ranges: YYYY-MM-DD (null if point-in-time)",
      "precision": "exact|day|week|month|quarter|year|approximate|relative|range",
      "anchor_text": "for relative dates: the anchor reference text",
      "confidence": 0.0-1.0,
      "timezone": "IANA timezone if detectable, else null",
      "event_type": "one of the event types above",
      "description": "1-2 sentence normalized description of the event",
      "actors": ["names of people/orgs involved"],
      "location": "location if mentioned, else null",
      "source_location": "page X, paragraph Y or section heading",
      "is_deadline": false,
      "deadline_trigger": "for deadlines: what triggers the deadline",
      "deadline_days": null
    }
  ]
}

## Examples

Input: "On March 15, 2024, Smith and Jones met at Acme headquarters to discuss the proposed merger."
Output event:
{
  "raw_text": "On March 15, 2024, Smith and Jones met at Acme headquarters to discuss the proposed merger.",
  "normalized_date": "2024-03-15",
  "date_end": null,
  "precision": "exact",
  "anchor_text": null,
  "confidence": 0.98,
  "timezone": null,
  "event_type": "meeting",
  "description": "Smith and Jones met at Acme headquarters to discuss proposed merger",
  "actors": ["Smith", "Jones"],
  "location": "Acme headquarters",
  "source_location": "page 3, paragraph 2",
  "is_deadline": false,
  "deadline_trigger": null,
  "deadline_days": null
}

Input: "The Company shall provide notice within thirty (30) days of the Closing Date."
Output event:
{
  "raw_text": "The Company shall provide notice within thirty (30) days of the Closing Date.",
  "normalized_date": null,
  "date_end": null,
  "precision": "relative",
  "anchor_text": "the Closing Date",
  "confidence": 0.90,
  "timezone": null,
  "event_type": "deadline",
  "description": "Company must provide notice within 30 days of closing",
  "actors": ["The Company"],
  "location": null,
  "source_location": "Section 4.2",
  "is_deadline": true,
  "deadline_trigger": "Closing Date",
  "deadline_days": 30
}

Extract ALL events. Do not skip events because they seem minor.
Return ONLY the JSON object. No commentary.
```

#### Entity Extraction System Prompt

```markdown
You are an Entity Extraction Agent for legal documents.

## Task
Extract all entities and relationships from the document provided.
Return a JSON object matching the schema below.

## Entity Types (3-Tier Taxonomy)

### Tier 1 — Core (always extract):
- **PERSON**: Individual humans (full names, partial names, titles+names)
- **ORGANIZATION**: Companies, law firms, government agencies, courts, funds
- **DATE**: Temporal references (covered by date extraction — skip here)
- **INSTRUMENT**: Contracts, agreements, amendments, exhibits, orders
- **EVENT_REF**: References to specific events ("the March meeting", "the closing")

### Tier 2 — Enrichment (extract when present):
- **LOCATION**: Physical addresses, cities, jurisdictions, venues, states, countries
- **MONETARY**: Financial amounts ($1,000,000, EUR 500K, "the purchase price")
- **DEADLINE**: Contractual or procedural deadlines (may overlap with date extraction)
- **STATUTE**: Legal citations (15 U.S.C. § 78j(b), FRCP 26, GDPR Art. 17)
- **CASE_REF**: Case numbers, docket numbers, citations (Smith v. Jones, 2024 WL 12345)

### Tier 3 — Contextual (extract if straightforward):
- **CLAIM**: Legal claims referenced (breach of contract, negligence, fraud)
- **EVIDENCE**: Evidence references (Exhibit A, Bates ACME_00001, Deposition Tr. 125:14)
- **ROLE**: Legal roles attributed to entities (plaintiff, defendant, witness, counsel, judge, expert, custodian)
- **PRIVILEGE_FLAG**: Phrases suggesting privilege ("attorney-client", "work product", "legal advice", "in anticipation of litigation")

## Coreference Resolution

Identify when different text strings refer to the same entity:
- "Acme Corporation", "Acme Corp.", "Acme", "the Company", "Defendant" → same entity
- "John Smith", "Mr. Smith", "Smith", "JS", "he" (when referent is clear) → same entity
- "the Agreement", "this Contract", "the SPA", "Exhibit 1" → may be same instrument

For each entity, provide:
- A canonical (normalized) form
- All alias forms found in the document
- Confidence in the coreference link

## Output Schema
{
  "source_id": "string",
  "extraction_model": "haiku",
  "extracted_at": "ISO-8601 timestamp",
  "entities": [
    {
      "entity_id": "local entity ID (e.g., E-001)",
      "text": "as it appears in document",
      "type": "PERSON|ORGANIZATION|INSTRUMENT|etc.",
      "tier": 1|2|3,
      "normalized": "canonical form",
      "aliases": ["other forms found"],
      "role": "legal role if applicable (plaintiff, defendant, etc.)",
      "context": "sentence where entity appears",
      "confidence": 0.0-1.0
    }
  ],
  "relationships": [
    {
      "source_entity": "E-001",
      "target_entity": "E-002",
      "relationship_type": "employed_by|party_to|counsel_for|signed|filed|witness_in|etc.",
      "context": "sentence establishing the relationship",
      "confidence": 0.0-1.0
    }
  ],
  "privilege_flags": [
    {
      "text": "flagged text",
      "flag_type": "attorney_client|work_product|joint_defense|other",
      "source_location": "page/section",
      "confidence": 0.0-1.0
    }
  ]
}

Extract ALL entities. Return ONLY the JSON object. No commentary.
```

**Step 3.2: Chunk documents for processing**

Documents exceeding Haiku's context window must be chunked:

| Document Size | Strategy |
|---------------|----------|
| < 8K tokens (~6K words) | Process as single unit |
| 8K-50K tokens | Split by page/section with 500-token overlap |
| 50K-200K tokens | Hierarchical: section → subsection with overlap |
| > 200K tokens | Split into ~6K-token chunks by paragraph boundary |

**Chunking rules:**
- Preserve structural boundaries (pages, sections, paragraphs)
- Include 500-token overlap for context continuity at chunk boundaries
- Prepend document frontmatter (source_id, custodian, date) to every chunk
- Track chunk position (chunk N of M) for result merging
- Never split mid-sentence

**Step 3.3: Execute extraction**

**CLI path**: Stage 2 script handles parallel dispatch automatically:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 2 --to 2
```

**Sub-agent path**: Launch parallel Task tool agents (batch by available concurrency):

```
# For each document (or chunk), launch a Haiku extraction agent:
# Launch multiple in parallel when documents are independent

Task(model: "haiku", description: "Extract dates from DOC-00001"):
  [date extraction prompt + document content]

Task(model: "haiku", description: "Extract dates from DOC-00002"):
  [date extraction prompt + document content]

# ... up to 4-6 concurrent Task calls

# Then entity extraction pass:
Task(model: "haiku", description: "Extract entities from DOC-00001"):
  [entity extraction prompt + document content]
```

**Two-pass extraction**: Run date/event extraction first, then entity extraction.
This prevents exceeding Haiku's output capacity with too many entity types per pass.
Each pass uses 6-8 output fields maximum for reliable structured extraction.

**Step 3.4: Validate extraction outputs**

For each extraction result, verify:
- [ ] Valid JSON (parse without error)
- [ ] Required fields present (source_id, events/entities array)
- [ ] Dates are parseable (ISO 8601 or recognized format)
- [ ] Confidence scores are in [0.0, 1.0] range
- [ ] No hallucinated source_ids (match against manifest)

**Failed extractions**: Log the failure, increment failure counter, and either:
- Retry with a different prompt (add "Be more careful with JSON formatting")
- Flag for manual review
- Skip if non-critical document

**Step 3.5: Merge chunk results**

For documents processed in multiple chunks:
1. Collect all extraction results by source_id
2. Merge events across chunks (union of all events)
3. Deduplicate events from overlapping regions (same date + event type + similar text)
4. Merge entity mentions across chunks
5. Resolve coreferences across chunk boundaries
6. Assign final per-document event count

---

### Phase 4: Consolidation

This phase merges per-document extractions into unified timeline data structures.
No API calls — runs locally with Python.

**CLI path**: Stage 3 script:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 3 --to 3
```

**Sub-agent path**: Execute Python consolidation inline or via Bash tool.

**Step 4.1: Build candidate event table**

Load all per-document extraction JSON files and merge into a single event list:

```json
{
  "event_id": "EVT-00001",
  "source_id": "DOC-00123",
  "raw_text": "On January 15, 2025, Smith met with Jones",
  "normalized_date": "2025-01-15",
  "date_end": null,
  "date_precision": "exact",
  "timezone": "America/New_York",
  "event_type": "meeting",
  "description": "Smith met with Jones to discuss contract terms",
  "actors": ["PERSON-001", "PERSON-002"],
  "location": "Acme headquarters",
  "source_reference": "DOC-00123, page 5, paragraph 2",
  "bates_reference": "ACME_000065",
  "confidence": 0.95,
  "extraction_method": "haiku_cli",
  "corroboration_count": 1,
  "issue_tags": [],
  "disputed": false,
  "privilege_flag": null,
  "protective_designation": null
}
```

**Step 4.2: Normalize dates and timezones**

| Input | Precision | Normalized | Range Start | Range End |
|-------|-----------|------------|-------------|-----------|
| "January 15, 2025" | exact | 2025-01-15 | — | — |
| "early March 2025" | approximate | ~2025-03-05 | 2025-03-01 | 2025-03-10 |
| "Q1 2025" | quarter | 2025-Q1 | 2025-01-01 | 2025-03-31 |
| "2025" | year | 2025 | 2025-01-01 | 2025-12-31 |
| "within 30 days of closing" | relative | null | [closing] | [closing+30] |

**Relative date resolution**: Attempt to anchor relative dates to known events:
1. Search for the anchor event in the event table (e.g., "the Closing Date")
2. If anchor found with exact date, compute the relative date
3. If anchor not found, mark as `unresolved_relative` with the anchor text

**Timezone normalization**:
- Detect timezone from email headers (most reliable)
- Detect timezone from document metadata (creation timezone)
- Apply jurisdiction-based timezone default for legal filings
- Normalize to baseline timezone if specified in matter frame
- Always preserve original timezone alongside normalized time

**Step 4.3: Deduplicate events**

Group by `(normalized_date, event_type, text_signature)` where text_signature is
the first 50 characters of the normalized description.

For duplicates:
- Keep the highest-confidence extraction
- Merge all source references into `source_references` array
- Set `corroboration_count` to number of independent source documents
- If descriptions differ materially, flag for contradiction review

**Step 4.4: Build unified entity registry**

Merge all per-document entity extractions:
1. Normalize entity names (case-insensitive, strip titles/suffixes)
2. Match entities across documents by normalized name
3. Merge alias lists
4. Resolve conflicting roles (e.g., "John Smith" is both "Plaintiff" and "Former Employee")
5. Assign stable entity IDs (e.g., PERSON-001, ORG-001)
6. Build entity relationship graph

**Step 4.5: Link entities to events**

For each event, resolve actor names to entity IDs:
- Exact match on normalized name → link
- Alias match → link with confidence note
- Ambiguous match → flag for review (e.g., "Smith" when multiple Smiths exist)

**Step 4.6: Tag events with issues**

Apply issue tagging based on matter frame keywords:
- For each issue, scan event descriptions and raw text for keywords
- Apply issue tags to matching events
- Events may belong to multiple issues
- Untagged events go into "general" issue bucket

**Step 4.7: Screen for privilege indicators**

If privilege handling is not "skip":
- Check privilege_flags from entity extraction
- Scan for attorney-client communication patterns (attorney → client or vice versa)
- Scan for work product indicators ("in anticipation of litigation", "attorney work product")
- Flag events sourced from potentially privileged documents
- Do NOT exclude — flag for human review with `privilege_flag` field

**Outputs**:
- `consolidated/events.json` — All events with stable IDs
- `consolidated/entities.json` — Entity registry with relationships
- `consolidated/summary.json` — Processing statistics

---

### Phase 5: Validation and Quality Assurance

This phase uses Sonnet agents for intelligent quality checking.

**CLI path**: Stage 4 script:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 4 --to 4
```

**Sub-agent path**: Launch Sonnet Task tool agents for validation:
```
Task(model: "sonnet", description: "Validate timeline segment"):
  [validation prompt + events JSON chunk]
```

**Step 5.1: Contradiction detection**

Submit timeline segments to Sonnet for contradiction analysis.

**Contradiction types:**

| Type | Description | Example | Severity |
|------|-------------|---------|----------|
| **DIRECT** | Same event, conflicting dates | "Meeting on March 15" vs "Meeting on March 18" | HIGH |
| **SEQUENCE** | Events in impossible order | Response filed before complaint served | HIGH |
| **OVERLAP** | Person in two places simultaneously | Deposition in NY while at meeting in LA | HIGH |
| **DURATION** | Implausible time spans | 500-page contract drafted in 1 hour | MEDIUM |
| **WITNESS** | Conflicting witness accounts | Smith says X happened; Jones says not X | MEDIUM-HIGH |
| **AMOUNT** | Inconsistent financial figures | "$1M in Exhibit A" vs "$1.5M in Exhibit B" | MEDIUM |
| **PARTY** | Conflicting party attributions | "Smith signed" vs "Jones signed" | MEDIUM |

**Step 5.2: Sequence validation**

Apply causal ordering rules. These represent logical dependencies where one event
must precede another:

| Cause Event | Effect Event | Rule |
|-------------|--------------|------|
| contract_drafted | contract_signed | Draft precedes signature |
| contract_signed | contract_breached | Execution precedes breach |
| invoice_sent | payment_received | Invoice precedes payment |
| complaint_filed | complaint_served | Filing precedes service |
| complaint_served | answer_filed | Service precedes answer |
| motion_filed | motion_heard | Filing precedes hearing |
| deposition_noticed | deposition_taken | Notice precedes deposition |
| discovery_request | discovery_response | Request precedes response |
| verdict_entered | appeal_filed | Verdict precedes appeal |
| breach_occurred | notice_sent | Breach precedes notice (usually) |
| termination_notice | termination_effective | Notice precedes effective date |

**Step 5.3: Gap analysis**

Identify unexplained time periods where activity is expected but absent:

```yaml
gap_register:
  - gap_id: GAP-001
    period_start: "2024-02-15"
    period_end: "2024-03-01"
    description: "No events during key negotiation period"
    expected_activity: "Contract negotiation communications"
    relevant_issues: ["ISS-001"]
    relevant_custodians: ["John Smith", "Jane Doe"]
    impact: HIGH
    possible_explanations:
      - "Documents not yet produced"
      - "Oral communications not documented"
      - "Privileged communications withheld"
    recommended_action: "Request supplemental production from Defendant for Feb 15-Mar 1, 2024 communications between Smith and Doe re: contract negotiation"
    owner: "eDiscovery team"
```

**Step 5.4: Confidence auditing**

Flag events where confidence and evidence quality are misaligned:
- High confidence (>0.80) but single source → downgrade or add corroboration note
- Multiple corroborating sources but low confidence → investigate extraction quality
- Critical events (tied to core claims) with <0.60 confidence → escalate

**Step 5.5: Apply citation quality gates**

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every event has at least one source pointer | Mark `[UNSOURCED]` |
| **Format** | Citations use consistent format (doc ID + locator) | Normalize format |
| **Currency** | Procedural references checked for current rules | Add `[CHECK CURRENCY]` |
| **Domain** | Jurisdiction-specific statements limited to selected forum | Flag jurisdiction bleed |
| **Confidence** | Certainty aligned to source quality | Downgrade and flag |
| **Privilege** | No privileged content in timeline without review | Redact pending review |

**Validation output**: `validated/validation.json`
```json
{
  "validation_id": "VAL-001",
  "validated_at": "ISO-8601 timestamp",
  "validation_model": "sonnet",
  "event_count": 1234,
  "contradictions": [...],
  "sequence_violations": [...],
  "gaps": [...],
  "confidence_issues": [...],
  "privilege_flags": [...],
  "quality_score": 0.87,
  "summary": "..."
}
```

---

### Phase 6: Timeline Synthesis

This phase uses an Opus agent to produce the final defensible chronology.

**CLI path**: Stage 5 script:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 5 --to 5
```

**Sub-agent path**: Launch a single Opus Task tool agent:
```
Task(model: "opus", description: "Synthesize final timeline for [Matter Name]"):
  [synthesis prompt + consolidated events + validation report + matter frame]
```

The Opus agent receives all consolidated data and validation results, then:

**Step 6.1: Resolve contradictions**

For each contradiction flagged in Phase 5:
- Assess materiality (does it affect a core claim/defense?)
- Determine which version has stronger evidentiary support
- If resolvable: choose the better-supported version, note the conflict
- If unresolvable: present both versions with `disputed: true`
- Generate a contradiction resolution note for the audit trail

**Step 6.2: Build master chronology**

All material events in chronological order with full citation:

```markdown
## Master Chronology

| # | Date | Prec. | Event | Actors | Sources | Issues | Disp. | Conf. |
|---|------|-------|-------|--------|---------|--------|-------|-------|
| 1 | 2024-01-15 | exact | Initial meeting between Smith and Jones | Smith, Jones | DOC-001 p.5; DOC-015 p.2 | Formation | — | 0.95 |
| 2 | ~2024-02-01 | approx | Oral representations re: revenue | Jones | Smith Decl. ¶8 | Fraud | **Yes** | 0.60 |
| 3 | 2024-02-15 | exact | Draft SPA circulated | Smith | EMAIL-034 | Formation | — | 0.92 |
```

**Step 6.3: Build issue chronologies**

For each issue in the matter frame, produce a filtered timeline showing only events
tagged with that issue:

```markdown
### Issue: Contract Formation (ISS-001)

| # | Date | Event | Support | Sources | Deposition Topics |
|---|------|-------|---------|---------|-------------------|
| 1 | 2024-01-15 | Initial contact re: acquisition | Strong (3 sources) | DOC-001, DOC-015, EMAIL-003 | Circumstances of first meeting |
| 2 | 2024-02-01 | Draft SPA circulated | Strong | EMAIL-034 | Who drafted, what terms |
| 3 | 2024-03-01 | SPA executed | Definitive | ACME_050 | Authority, understanding of terms |
```

**Step 6.4: Build entity chronologies**

Per-actor timelines for deposition preparation:

```markdown
### Entity Timeline: John Smith (Plaintiff, CEO of Acme)

Aliases: Mr. Smith, JS, "the CEO"
Documents involving Smith: 145 of 1,247 total

| # | Date | Event | Document Basis | Contradictions | Deposition Topics |
|---|------|-------|----------------|----------------|-------------------|
| 1 | 2024-01-15 | Met with Jones at HQ | DOC-001 p.5 | — | Circumstances, who present, what discussed |
| 2 | 2024-02-15 | Received revenue reps | **Disputed** (Smith Decl. vs Jones Dep.) | CONTRADICTION-003 | What was said, by whom, in what context |
| 3 | 2024-03-01 | Signed SPA on behalf of Acme | ACME_050 | — | Authority, reliance, understanding |
```

**Step 6.5: Build deadline risk calendar**

Procedural timeline with risk indicators:

```markdown
### Deadline Calendar

| # | Trigger Event | Rule/Order | Deadline | Status | Risk | Mitigation |
|---|---------------|------------|----------|--------|------|------------|
| 1 | Complaint filed 2025-06-15 | FRCP 12(a)(1) [VERIFY] | Answer: 2025-07-06 | Complete | — | — |
| 2 | Initial disclosures | FRCP 26(a)(1) [VERIFY] | 2025-08-15 | Pending | MEDIUM | Prepare disclosure checklist |
| 3 | Fact discovery cutoff | Scheduling Order ¶4 | 2026-04-01 | Active | Track | Priority depositions by Feb |
| 4 | Expert reports | Scheduling Order ¶6 | 2026-05-15 | Upcoming | HIGH | Retain expert by March |
| 5 | Summary judgment | FRCP 56 [VERIFY] | 2026-07-01 | Future | Plan | Begin fact statement drafting |
```

**Step 6.6: Build relationship map**

Entity-to-entity relationships for understanding case dynamics:

```markdown
### Key Relationships

| Entity A | Relationship | Entity B | Sources | Significance |
|----------|-------------|----------|---------|-------------|
| Smith | CEO of | Acme Corp | ACME_001 | Plaintiff's authority |
| Jones | VP Sales at | Acme Corp | ACME_002 | Made alleged representations |
| Smith | Negotiated with | Doe (Vendor) | EMAIL-034 | Contract formation |
| Baker LLP | Counsel for | Acme Corp | Engagement letter | Privilege boundary |
```

---

### Phase 7: Output Generation

This phase runs locally — no API calls.

**CLI path**: Stage 6 script:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 6 --to 6
```

**Sub-agent path**: Use Bash tool to run Python output generation.

**Step 7.1: Markdown timeline pack**

Primary working document for legal team. Full template below in Output Format section.

**Step 7.2: JSON export**

Structured data for system integration:
```json
{
  "metadata": {
    "matter_name": "Smith v. Acme Corp",
    "matter_number": "1:25-cv-00123",
    "generated_at": "2026-02-28T14:30:00Z",
    "version": "1.0",
    "baseline_timezone": "America/New_York",
    "execution_path": "cli",
    "total_cost_usd": 18.45
  },
  "events": [...],
  "entities": {...},
  "relationships": [...],
  "contradictions": [...],
  "gaps": [...],
  "deadlines": [...],
  "privilege_flags": [...],
  "sources": [...],
  "quality": {
    "score": 0.87,
    "events_total": 1234,
    "events_sourced": 1220,
    "events_disputed": 15,
    "contradictions_resolved": 8,
    "contradictions_open": 7,
    "gaps_identified": 12
  }
}
```

**Step 7.3: CSV export**

For spreadsheet analysis and bulk operations. One row per event with flattened fields.

**Step 7.4: HTML interactive timeline**

Self-contained HTML file with:
- Zoomable timeline visualization (year → month → day → hour)
- Color-coded event types
- Issue filter toggles
- Entity filter toggles
- Contradiction highlights
- Gap indicators
- Click-to-expand event details with source citations

**Step 7.5: Court-ready formats**

#### FRCP Rule 56 Statement of Undisputed Facts

For summary judgment motions, generate a numbered statement of facts where each
fact is supported by citation to admissible evidence:

```markdown
## Statement of Undisputed Material Facts

1. On January 15, 2024, Defendant Smith and Plaintiff Jones met at Acme Corporation
   headquarters in New York to discuss the proposed acquisition. (DOC-001 at 5;
   Smith Dep. 45:12-46:3; Jones Decl. ¶ 5.)

2. On February 15, 2024, Defendant circulated a draft Stock Purchase Agreement to
   Plaintiff via email. (EMAIL-034; DOC-034 (draft SPA).)

3. The Stock Purchase Agreement was executed on March 1, 2024 by Smith on behalf of
   Acme Corporation and by Jones individually. (ACME_050 at signature page.)
```

Criteria for inclusion:
- Only events with confidence ≥ 0.80
- Only events with `disputed: false`
- Only events supported by admissible evidence (not hearsay-only)
- Sorted chronologically
- Each fact cites specific document and locator

#### Proposed Findings of Fact

For bench trials, generate proposed findings with evidentiary basis and legal
significance:

```markdown
## Proposed Findings of Fact

### A. Formation of the Agreement

1. The Court finds that on January 15, 2024, the parties first met to discuss the
   proposed transaction. (Trial Ex. 1 at 5; Tr. 45:12-46:3 (Smith); Tr. 120:5-15 (Jones).)

2. The Court finds that during the period February 1-15, 2024, the parties exchanged
   multiple draft agreements. (Trial Exs. 34-38; Tr. 78:3-80:12 (Smith).)
```

**Step 7.6: EDRM XML export** (optional)

For integration with eDiscovery platforms (Relativity, DISCO, Everlaw):
- EDRM XML 2.0 format for load file generation
- Map events to document production metadata
- Preserve Bates references and custodian linkage

**Step 7.7: CaseMap/TrialLine import** (optional)

- CaseMap TLF (Timeline Linked Facts) format
- TrialLine JSON import format
- Generic timeline tool CSV with standardized column headers

---

## Specialized Timeline Patterns

### MDL / Class Action Timelines

For Multi-District Litigation and class actions, the timeline requires additional
structure:

**MDL coordination timeline**:
- Transfer/consolidation events (28 U.S.C. § 1407) [VERIFY]
- Bellwether selection and scheduling
- Common discovery vs. case-specific discovery
- Class certification milestones
- Settlement class events

**Class certification timeline**:
- Named plaintiff events (typicality, adequacy)
- Commonality events (shared facts across class)
- Class definition events (who is in/out)
- Notice events (opt-in/opt-out deadlines)

**Multi-plaintiff structure**:
```yaml
timeline_structure:
  master_docket: "MDL No. 1234"
  transferee_court: "S.D.N.Y."
  common_timeline:
    - "[events common to all cases]"
  bellwether_timelines:
    - case_number: "1:24-cv-001"
      plaintiff: "Smith"
      events: ["[case-specific events]"]
    - case_number: "1:24-cv-002"
      plaintiff: "Jones"
      events: ["[case-specific events]"]
```

### Regulatory Investigation Timelines

For government investigations (SEC, DOJ, FTC, state AG):

**Key differences from private litigation**:
- Voluntary vs. compulsory process distinction
- Tolling agreements and statute of limitations events
- Wells notices and response deadlines
- Parallel proceedings (civil + criminal + regulatory)
- Cooperation credit events
- Consent decree/settlement negotiation milestones

**Regulatory-specific event types**:
- subpoena_issued, subpoena_response, voluntary_production
- wells_notice, wells_response
- consent_decree_draft, consent_decree_final
- monitor_appointment, monitor_report
- cooperation_meeting, proffer_session

### Cross-Border Timeline Considerations

For matters spanning multiple jurisdictions:

**Timezone management**:
- Store all times in UTC internally
- Display in source-local timezone with UTC offset
- Flag events where timezone affects legal deadline (e.g., filing at 11:59 PM in one timezone vs. next day in another)

**Multi-jurisdiction deadline tracking**:
- Track deadlines per jurisdiction separately
- Flag conflicts (e.g., U.S. discovery deadline vs. EU blocking statute)
- Note Hague Convention service timing vs. domestic service
- Track data transfer timeline (GDPR adequacy, SCCs, derogations)

**Language and date format**:
- Preserve original language text alongside English translation
- Use ISO 8601 (YYYY-MM-DD) as canonical format
- Note source format conventions (US MM/DD, EU DD/MM, ISO YYYY-MM-DD)

---

## Privilege and Confidentiality Handling

### Privilege Screening

This skill does NOT make privilege determinations. It flags potential privilege
for human review and ensures privileged content does not enter the final timeline
without attorney sign-off.

**Privilege flag triggers**:
- Communication between attorney and client (check entity roles)
- Documents marked "Attorney-Client Privileged" or "Work Product"
- Communications referencing legal advice ("counsel advised", "per our attorney")
- Documents created "in anticipation of litigation"
- Joint defense communications

**Treatment of flagged items**:
1. Events sourced solely from flagged documents: mark `privilege_flag: "pending_review"`
2. Events sourced from both flagged and non-flagged documents: include with non-flagged citation only
3. Never include privileged document content in timeline text
4. Generate parallel privilege chronology for privilege log support

**Parallel privilege chronology**:
```markdown
### Privilege Chronology (For Privilege Log — NOT for production)

| # | Date | Communication Type | Participants | Subject (Redacted) | Flag Type | Review Status |
|---|------|-------------------|--------------|-------------------|-----------|--------------|
| P-1 | 2024-02-20 | Email | Smith → Baker LLP | [Re: potential claims] | AC | Pending |
| P-2 | 2024-03-05 | Memo | Baker LLP | [Litigation assessment] | WP | Pending |
```

### Protective Order Designations

If a protective order is in effect:
- Tag each event and source with its highest designation level
- Filter outputs by designation for different audiences
- Generate designation-specific timeline views:
  - "Confidential" view (for outside counsel eyes only)
  - "Highly Confidential — Attorneys' Eyes Only" view
  - Public/undesignated view

---

## Deep Timeline Analysis Framework

Evaluate each event and chronology segment across these 14 dimensions:

| # | Dimension | What to Assess | Evidence Signals | Red Flags |
|---|-----------|----------------|------------------|-----------|
| 1 | **Event authenticity** | Event tied to reliable source | Original doc, transcript, metadata | No source pointer |
| 2 | **Temporal precision** | Exactness of date/time | Timestamp, filing date, signature | Approximate treated as exact |
| 3 | **Sequence integrity** | Coherent ordering | Cross-source consistency | Circular/impossible sequence |
| 4 | **Actor attribution** | Who performed the act | Named sender/speaker/author | Unknown actor |
| 5 | **Documentary support** | Corroboration depth | Multiple independent sources | Single unverified source |
| 6 | **Testimonial alignment** | Witness consistency | Page-line aligned testimony | Direct contradiction |
| 7 | **Contradiction materiality** | Case impact of conflict | Links to core claim/defense | Immaterial conflict flagged as critical |
| 8 | **Admissibility sensitivity** | Likely evidentiary treatment | Authentication chain | Hearsay-heavy anchors |
| 9 | **Procedural relevance** | Relation to deadlines | Trigger events linked to rules | Missed trigger event |
| 10 | **Gap severity** | Importance of missing periods | Missing records in key window | Unknown bridging event |
| 11 | **Preservation posture** | Evidence integrity | Custody records, immutable logs | Missing custody chain |
| 12 | **Strategic leverage** | Utility for case theory | Supports/disrupts narrative | Timeline exists but not issue-mapped |
| 13 | **Entity linkage** | People/orgs properly connected | Clear actor-event relationships | Orphan entities |
| 14 | **Timezone coherence** | Cross-border time consistency | Normalized timestamps | Date shift across timezones |

---

## Chronology Finding Classification

| Class | Meaning | Typical Response |
|-------|---------|------------------|
| **LOW** | Minor inconsistency; limited case impact | Track and monitor |
| **MEDIUM** | Material ambiguity requiring clarification | Assign follow-up action |
| **HIGH** | Significant contradiction or unsupported core event | Escalate to matter lead |
| **CRITICAL** | Timeline defect threatens position or sanctions exposure | Immediate escalation; 24-72h remediation |

---

## Actionable Output Per Finding

For each `MEDIUM/HIGH/CRITICAL` finding, provide:

| Field | Content |
|-------|---------|
| **Finding summary** | One-sentence description |
| **Why it matters** | Legal + strategic impact |
| **Source basis** | `VERIFIED` or `[VERIFY]` |
| **Recommended action** | Specific task (e.g., "Subpoena Doe's phone records for Feb 15-Mar 1") |
| **Owner role** | Legal, eDiscovery, forensic, business, expert |
| **Due window** | `24h`, `72h`, `7d`, `14d+` |
| **Expected effect** | Uncertainty reduction, conflict resolution, gap closure |

---

## Prioritization Framework

| Tier | Label | Criteria | Deadline |
|------|-------|----------|----------|
| **Tier 1** | Immediate | `CRITICAL` defects, sanctions risk, deadline impact | 0-72 hours |
| **Tier 2** | Near-term | `HIGH` conflicts affecting merits/strategy | 3-14 days |
| **Tier 3** | Programmatic | `MEDIUM/LOW` improvements and completeness | 2+ weeks |

---

## Confidence Scoring

| Level | Range | Interpretation | Action |
|-------|-------|----------------|--------|
| **Definite** | 0.95-1.00 | Multiple consistent primary sources | Use as anchor event |
| **High** | 0.80-0.94 | Strong support with limited ambiguity | Use with brief caveat |
| **Probable** | 0.60-0.79 | Competing readings remain | Present both readings |
| **Possible** | 0.40-0.59 | Material uncertainty | Flag for collection/interview |
| **Unlikely** | 0.00-0.39 | Weak support/speculative | Exclude from core timeline; note in appendix |

---

## Date Precision Levels

| Precision | Format | Example | Timeline Treatment |
|-----------|--------|---------|-------------------|
| **EXACT_DATETIME** | YYYY-MM-DDTHH:MM:SS±HH:MM | 2024-03-15T14:30:00-05:00 | Plot at exact point |
| **EXACT_DATE** | YYYY-MM-DD | 2024-03-15 | Plot at date |
| **WEEK** | YYYY-Www | 2024-W11 | Show as week range |
| **MONTH** | YYYY-MM | 2024-03 | Show as month range |
| **QUARTER** | YYYY-Qn | 2024-Q1 | Show as quarter range |
| **YEAR** | YYYY | 2024 | Show as year range |
| **APPROXIMATE** | ~YYYY-MM-DD | ~2024-03-15 | Plot with uncertainty indicator |
| **RANGE** | YYYY-MM-DD/YYYY-MM-DD | 2024-03-01/2024-03-31 | Show as span |
| **BEFORE** | <YYYY-MM-DD | <2024-03-15 | Plot as terminus ante quem |
| **AFTER** | >YYYY-MM-DD | >2024-03-15 | Plot as terminus post quem |
| **RELATIVE** | +Nd from [anchor] | +30d from Closing Date | Resolve when anchor known |

---

## Entity Taxonomy

### Tier 1 — Core Entities (Always Extract)

| Type | Description | Examples | Coreference Patterns |
|------|-------------|----------|---------------------|
| **PERSON** | Individual humans | John Smith, Dr. Jane Doe | Mr. Smith, Smith, JS, "he" |
| **ORGANIZATION** | Companies, firms, agencies | Acme Corp., Smith & Jones LLP | Acme, the Company, Defendant |
| **INSTRUMENT** | Legal documents | SPA, NDA, Employment Agreement | the Agreement, this Contract, Exhibit 1 |
| **EVENT_REF** | Named events | the Closing, the IPO, the Merger | the transaction, the deal |

### Tier 2 — Enrichment Entities

| Type | Description | Examples |
|------|-------------|----------|
| **LOCATION** | Physical places | 123 Main St., New York, Delaware |
| **MONETARY** | Financial amounts | $1,000,000, EUR 500K, "the purchase price" |
| **DEADLINE** | Time-bound obligations | "within 30 days", "no later than June 1" |
| **STATUTE** | Legal citations | 15 U.S.C. § 78j(b), FRCP 26, GDPR Art. 17 |
| **CASE_REF** | Case identifiers | Case No. 1:25-cv-00123, Smith v. Jones |

### Tier 3 — Contextual Entities

| Type | Description | Examples |
|------|-------------|----------|
| **CLAIM** | Legal claims | Breach of contract, fraud, negligence |
| **EVIDENCE** | Evidence references | Exhibit A, Bates ACME_00001, Tr. 125:14 |
| **ROLE** | Legal roles | Plaintiff, Defendant, Witness, Counsel |
| **PRIVILEGE_FLAG** | Privilege indicators | "attorney-client", "work product" |

### Legal-Specific Roles

| Role Category | Subtypes |
|---------------|----------|
| **PARTY** | Plaintiff, Defendant, Petitioner, Respondent, Intervenor, Third-Party |
| **LEGAL** | Counsel, Judge, Magistrate, Arbitrator, Mediator, Special Master |
| **WITNESS** | Fact Witness, Expert Witness, Designated Corporate Representative (30(b)(6)) |
| **DISCOVERY** | Custodian, Producing Party, Requesting Party |
| **COURT** | Federal District, State Trial, Appellate, Supreme, Bankruptcy, Administrative |

---

## Self-Interrogation (For HIGH/CRITICAL Findings)

Apply three passes before finalizing high-impact timeline findings:

**Pass 1 — Legal Chain Integrity**
Does the claimed sequence logically follow from the cited records? Would a court/regulator
actually reach this conclusion from the cited evidence alone?

**Pass 2 — Completeness**
What missing sources could reverse this finding? Are there documents not yet produced,
witnesses not yet deposed, or records not yet subpoenaed that would change the picture?

**Pass 3 — Adversarial Challenge**
What is the strongest opposing timeline interpretation? Which citations support the
alternative reading? Would a reasonable attorney on the other side accept this chronology?

If unresolved after Pass 3, classify as uncertain and escalate to counsel.

---

## Citation Quality Gates

Apply these gates before delivery. If any fail, revise output.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every material event has ≥1 concrete source pointer | Add source or mark `[UNSOURCED]` |
| **Format** | Citations use consistent format (doc ID + locator) | Normalize citation format |
| **Currency** | Rule/procedural references checked for current version | Add `[CHECK CURRENCY]` |
| **Domain** | Jurisdiction-specific statements limited to selected forum | Remove jurisdiction bleed |
| **Confidence** | Certainty aligned to source quality and contradiction status | Downgrade confidence and flag |
| **Privilege** | No potentially privileged content without review clearance | Redact or flag `[PRIVILEGE REVIEW]` |
| **Designation** | Protective order designations properly applied | Add designation or restrict distribution |

---

## Anti-Patterns

Avoid these failure modes in timeline construction:

### Pipeline Anti-Patterns

1. **No CLI detection** — Assuming `claude` CLI is available without checking; always test and fall back
2. **No budget tracking** — Running extraction without cost caps; use `--max-budget-usd` per worker
3. **Sequential when parallel is possible** — Processing documents one-by-one when batch parallel is available
4. **No checkpoint/resume** — Starting over on failure instead of resuming from last successful stage
5. **Ignoring failed extractions** — Not retrying or flagging documents that failed extraction

### Document Processing Anti-Patterns

6. **Skipping OCR quality validation** — Using garbled text extraction without verification
7. **Ignoring document metadata** — Missing creation dates, authors, revision history
8. **Losing attachment relationships** — Orphaning email attachments from parent emails
9. **Single-format assumption** — Failing to handle mixed document types in corpus
10. **Ignoring track changes** — Not using `--track-changes=all` for DOCX in litigation context

### Extraction Anti-Patterns

11. **Date conflation** — Using document creation date instead of event occurrence date
12. **Chunk boundary blindness** — Missing events that span chunk boundaries
13. **Over-trusting extraction** — Accepting low-confidence extractions without verification
14. **Entity resolution failures** — Treating "John Smith" and "Mr. Smith" as different people
15. **Too many entity types per pass** — Asking Haiku for >8 entity types degrades quality; use two passes
16. **No few-shot examples** — Extraction prompts without examples produce inconsistent output

### Timeline Construction Anti-Patterns

17. **Building from document dates** — Timeline based on when documents were created, not events
18. **Treating inferred events as facts** — No source citations for extracted events
19. **Merging contradictory events** — Hiding conflicts by averaging conflicting versions
20. **Omitting precision metadata** — Presenting approximate dates as exact
21. **Timezone amnesia** — Ignoring timezone differences for cross-border events

### Privilege and Confidentiality Anti-Patterns

22. **Including privileged content** — Putting attorney-client communications in timeline without review
23. **Missing protective designations** — Distributing confidential-designated content without labeling
24. **Waiving privilege by disclosure** — Including privilege log content in produced timeline

### Quality Anti-Patterns

25. **Ignoring chain-of-custody gaps** — No tracking of digital evidence integrity
26. **Overweighting recollection** — Preferring testimony when documents conflict
27. **Marking legal conclusions as facts** — Confusing legal characterization with events
28. **Single-view delivery** — Providing only master chronology without issue-specific views
29. **High confidence for single sources** — Not flagging corroboration requirements
30. **No audit trail** — Missing Glass Box documentation for defensibility

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-case-timeline-builder"
  skill_version: "3.0"
  topic: "litigation chronology construction"
  jurisdiction: "[selected jurisdiction or jurisdiction-agnostic]"

  # Execution metadata
  execution_path: "cli | subagent"
  pipeline_run_id: "[UUID]"
  pipeline_started: "[ISO timestamp]"
  pipeline_completed: "[ISO timestamp]"

  # Document corpus
  corpus_summary:
    corpus_path: "[path]"
    total_documents: "[count]"
    documents_converted: "[count]"
    documents_failed_conversion: "[count]"
    duplicates_found: "[count]"
    total_pages: "[count]"
    by_type:
      pdf: "[count]"
      docx: "[count]"
      email: "[count]"
      image: "[count]"
      other: "[count]"

  # Extraction metrics
  extraction_summary:
    events_extracted_raw: "[count]"
    events_after_dedup: "[count]"
    entities_extracted: "[count]"
    relationships_found: "[count]"
    privilege_flags: "[count]"
    extraction_failures: "[count]"
    extraction_retries: "[count]"

  # Model usage
  models_used:
    orchestrator: "claude-opus-4-5-20251101"
    extraction: "claude-haiku-4-5-20241022"
    validation: "claude-sonnet-4-5-20250514"
  worker_count: "[count]"
  total_api_calls: "[count]"
  estimated_cost_usd: "[amount]"

  # Quality metrics
  validation_summary:
    contradictions_found: "[count]"
    contradictions_resolved: "[count]"
    contradictions_open: "[count]"
    sequence_violations: "[count]"
    gaps_identified: "[count]"
    events_unsourced: "[count]"
    events_low_confidence: "[count]"
    privilege_items_flagged: "[count]"
    quality_score: "[X]/100"

  # Confidence assessment
  overall_confidence: "HIGH | MEDIUM | LOW"
  confidence_rationale: "[explanation]"

  # Limitations
  limitations:
    - "AI extraction may miss implicit or context-dependent dates"
    - "OCR quality affects accuracy for scanned documents"
    - "Jurisdiction-specific procedural rules require counsel validation"
    - "Cross-document entity resolution is probabilistic"
    - "Privilege screening is indicative only — attorney review required"
    - "Protective order designations require counsel confirmation"

  # Review status
  reviewer: "AI-assisted; human legal review required"
  review_status: "PENDING | IN_PROGRESS | COMPLETE"
  reviewed_by: "[name]"
  reviewed_at: "[ISO timestamp]"
```

---

## Writing Standards

- Use plain, direct, verb-first instructions
- Separate facts, assumptions, and inferences with explicit markers
- State uncertainty explicitly; do not hide weak support behind confident language
- Use consistent citation syntax across all tables (doc_id at locator)
- Prefer concise, scan-friendly tables for events and findings
- Keep executive summary focused on decision-impacting issues
- Mark disputed facts clearly with visual indicators (bold, color, icon)
- Preserve original date text alongside normalized versions
- Include Bates references alongside document IDs where available
- Never present AI extraction confidence as legal certainty

---

## External Tool Integration

### Document Processing Tools

| Tool | Purpose | Install | Fallback |
|------|---------|---------|----------|
| **MinerU** (`magic-pdf`) | PDF → markdown with OCR, tables, layout | `pip install magic-pdf` | markitdown, pdftotext |
| **MarkItDown** (`markitdown`) | Multi-format → markdown | `pip install markitdown` | pandoc |
| **Pandoc** | DOCX → markdown with track changes | `brew install pandoc` | python-docx |
| **pdftotext** (poppler) | Basic PDF text extraction | `brew install poppler` | — |
| **ocrmypdf** | OCR for scanned PDFs | `pip install ocrmypdf` | tesseract |
| **extract-msg** | MSG email parsing | `pip install extract-msg` | markitdown |
| **readpst** | PST archive extraction | `brew install libpst` | — |

### Claude Code CLI

| Command | Purpose |
|---------|---------|
| `claude -p --model haiku` | Non-interactive extraction worker |
| `claude -p --model sonnet` | Validation worker |
| `claude -p --model opus` | Synthesis/orchestration |
| `--output-format json` | Structured JSON output |
| `--max-turns 1` | Single response (no tool use) |
| `--max-budget-usd X` | Per-worker cost cap |
| `--no-session-persistence` | Don't save session state |
| `--system-prompt-file` | Load extraction prompt from file |
| `--tools ""` | Disable all tools (pure extraction) |
| `--json-schema '{...}'` | Validate output against JSON schema |
| `--fallback-model sonnet` | Auto-fallback when Haiku overloaded |

### legalcode-mcp Integration

When `legalcode-mcp` is available:
- Validate jurisdiction-specific procedural and evidentiary references
- Verify statutory/rule statements used in deadline calculations
- Pull current case law on timeline-relevant doctrines
- Mark validated items as `VERIFIED` in output and audit trail

When `legalcode-mcp` is not available:
- Continue with repository and web sources
- Mark jurisdiction-sensitive assertions with `[VERIFY]`
- Record verification limitations in Glass Box output

### Case Management Integration

Export formats compatible with:

| Platform | Format | Export Method |
|----------|--------|--------------|
| **Relativity** | DAT load files, EDRM XML | Stage 6 EDRM export |
| **DISCO** | CSV import | Stage 6 CSV export |
| **Everlaw** | CSV/JSON | Stage 6 JSON export |
| **CaseMap** | TLF timeline import | Stage 6 TLF export |
| **TrialLine** | JSON import | Stage 6 JSON export |
| **TimelineJS** | JSON/Google Sheets | Stage 6 HTML export |
| **Generic** | JSON, CSV, Markdown | Default Stage 6 outputs |

---

## Output Format Template

````markdown
# Case Timeline Pack — [Matter Name]

## 1. Executive Snapshot
- **Matter**: [Case name and number]
- **Objective**: [strategy | deposition | trial | settlement | regulatory]
- **Side represented**: [plaintiff | defendant | class | regulatory | neutral]
- **Governing forum/law**: [jurisdiction]
- **Date range**: [start] to [end]
- **Chronology confidence**: [HIGH | MEDIUM | LOW]
- **Execution path**: [CLI | Sub-Agent]
- **Processing cost**: $[amount]
- **Top timeline risks**:
  1. [Risk 1 — e.g., 14-day gap in key negotiation period]
  2. [Risk 2 — e.g., 3 unresolved contradictions on breach date]
  3. [Risk 3 — e.g., 5 events rely on single disputed source]

## 2. Processing Summary
- **Documents in corpus**: [count]
- **Documents converted**: [count] ([count] failed)
- **Duplicates detected**: [count]
- **Events extracted (raw)**: [count]
- **Events after deduplication**: [count]
- **Entities identified**: [count]
- **Relationships mapped**: [count]
- **Contradictions found**: [count] ([count] resolved, [count] open)
- **Gaps identified**: [count]
- **Privilege flags**: [count] (pending review)

## 3. Source Register
| source_id | type | custodian | date_range | bates_range | pages | reliability | privilege |
|-----------|------|-----------|------------|-------------|-------|-------------|-----------|

## 4. Master Chronology
| # | date | prec. | event | actors | sources | issues | disp. | conf. |
|---|------|-------|-------|--------|---------|--------|-------|-------|

## 5. Issue Timelines

### 5.1 [Issue Name] (ISS-001)
| # | date | event | support | sources | deposition_topics |
|---|------|-------|---------|---------|-------------------|

### 5.2 [Issue Name] (ISS-002)
[...]

## 6. Entity Timelines

### 6.1 [Entity Name] ([Role])
Aliases: [list]
Documents: [count] of [total]

| # | date | event | document_basis | contradictions | deposition_topics |
|---|------|-------|----------------|----------------|-------------------|

## 7. Relationship Map
| entity_a | relationship | entity_b | sources | significance |
|----------|-------------|----------|---------|-------------|

## 8. Contradiction Register
| id | type | severity | events | materiality | sources_for | sources_against | status | resolution |
|----|------|----------|--------|-------------|-------------|-----------------|--------|------------|

## 9. Gap Register
| id | period | missing_info | impact | custodians | recommended_action | owner |
|----|--------|-------------|--------|------------|--------------------| ------|

## 10. Deadline Risk Calendar
| # | trigger_event | rule_or_order | deadline | status | risk | mitigation |
|---|---------------|---------------|----------|--------|------|------------|

## 11. Priority Actions

### Tier 1 — Immediate (0-72h)
| action | finding | owner | due | expected_outcome |
|--------|---------|-------|-----|------------------|

### Tier 2 — Near-term (3-14d)
| action | finding | owner | due | expected_outcome |
|--------|---------|-------|-----|------------------|

### Tier 3 — Programmatic (2+ weeks)
| action | finding | owner | due | expected_outcome |
|--------|---------|-------|-----|------------------|

## 12. Privilege Chronology (For counsel review — NOT for production)
| # | date | type | participants | subject_redacted | flag_type | review_status |
|---|------|------|--------------|-----------------|-----------|--------------|

## 13. QA and Confidence Notes
- **Citation gate exceptions**: [list]
- **Self-interrogation outcomes**: [summary for HIGH/CRITICAL findings]
- **Items marked [VERIFY]**: [count and list]
- **Items marked [UNSOURCED]**: [count]
- **Confidence rationale**: [explanation]

## 14. Glass Box Audit Trail
```yaml
[Populate glass_box template from above]
```
````

---

## Localization Notes

When localizing for specific jurisdictions:

1. **Date format conventions** — US (MM/DD/YYYY) vs. international (DD/MM/YYYY) vs. ISO (YYYY-MM-DD)
2. **Procedural deadlines** — Jurisdiction-specific calculation rules (business days, holidays, service method)
3. **Evidence authentication** — Local requirements for admissibility (FRE vs. Civil Evidence Act vs. local)
4. **Privilege treatment** — Jurisdiction-specific privilege doctrines (legal professional privilege, solicitor-client, etc.)
5. **Court terminology** — Local names for filings, procedures, courts, tribunals
6. **Language requirements** — Multilingual documents, certified translation needs
7. **Discovery/disclosure scope** — Varies dramatically between common law and civil law systems
8. **Data protection** — GDPR, CCPA, PIPEDA, and other data privacy law timeline implications
9. **Cross-border service** — Hague Convention timing, letters rogatory, bilateral treaty service
10. **Sanctions frameworks** — Spoliation standards vary by jurisdiction (inherent power vs. statutory)

---

## Incremental Update Workflow

For ongoing matters where new documents are produced periodically:

**Step 1**: Add new documents to corpus directory
**Step 2**: Run discovery stage to identify new/changed files:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 1 --to 1  # Re-inventory
```
**Step 3**: Run extraction on new documents only:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 2 --to 2  # Only processes unconverted/unextracted
```
**Step 4**: Re-run consolidation and validation on full dataset:
```bash
./scripts/corpus-processing/timeline-build.sh run --from 3 --to 6
```
**Step 5**: Diff the new timeline against previous version:
- New events added
- Events with changed confidence (new corroboration or contradiction)
- Gaps closed or opened
- New contradictions surfaced

The pipeline is idempotent — already-processed documents are skipped based on
source_id tracking in the manifest.

---

## Provenance

**Created by Legalcode** (2026-02-28) — Comprehensive multi-agent timeline construction
skill with dual-path architecture (CLI + sub-agent fallback).

**Enhancement methodology:**
- Large Opus agent team research across 6 parallel research tracks
- Claude Code CLI batch processing patterns and `-p` mode documentation
- Document conversion tool evaluation (MinerU, MarkItDown, pandoc, pdftotext, ocrmypdf)
- Entity extraction and coreference resolution patterns for legal NER
- Litigation chronology professional standards (EDRM, ABA, FRCP)
- Shell scripting patterns for parallel processing (xargs, background job pools)
- Multi-agent orchestration design (pipeline stages, dual-path architecture)

**Pipeline scripts**: `scripts/corpus-processing/`
- `timeline-build.sh` — Master orchestrator
- `stages/stage-1-convert.sh` through `stages/stage-6-output.sh`
- `01-discover-and-classify.sh` through `05-cost-tracker.sh`

**Research artifacts**:
- `skills/CLAUDE-CLI-BATCH-PROCESSING.md` — CLI flag reference and batch patterns
