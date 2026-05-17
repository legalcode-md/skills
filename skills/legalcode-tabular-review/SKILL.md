---
name: legalcode-tabular-review
description: >
  Perform a high-volume, citation-backed tabular review across one or more document folders,
  VDR exports, DMS exports, or mixed document sets. Turn PDFs, DOCX files, scans, and related
  legal materials into a spreadsheet-style review where each document is a row and each user
  question is a column. Use when the user wants to compare agreements side by side, run a due
  diligence matrix, extract structured terms from a portfolio, build a red-flag table, answer
  a fixed list of questions across many documents, or generate Excel-ready review outputs with
  source citations, confidence, and verification states. Supports dual execution paths:
  Claude Code CLI workers (`claude -p --model haiku`) for scale, or Task sub-agents when CLI
  is unavailable. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers.
allowed-tools: Read, Bash(grep:*), Bash(ls:*), Bash(find:*), Bash(wc:*), Bash(claude:*), Bash(sh:*), Bash(bash:*), Bash(python3:*), Bash(pandoc:*), Bash(pdftotext:*), Bash(ocrmypdf:*), Bash(markitdown:*), Glob, Task
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Tabular Review

> **Disclaimer**: This skill provides a framework for AI-assisted multi-document review. It
> does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional before use in negotiations, diligence, litigation, compliance, or advice to
> clients. AI-extracted answers, citations, and summaries may be incomplete or wrong. Verify
> critical findings against the original documents before relying on them. Any legal authority
> stated from memory carries hallucination risk and must be independently confirmed.

## Purpose and Scope

This skill turns document corpora into a governed review grid:

- One document per row
- One question, field, or assessment per column
- One citation-backed answer per cell

It is designed for lawyers and legal ops teams who need spreadsheet-speed review without
giving up source visibility, verification discipline, or workflow control.

**Covers:**
- Folder-based and multi-folder document intake
- PDF, DOCX, scan, and mixed-format review
- User-defined extraction questions and standard field schemas
- Parallel extraction using low-cost workers
- Cell-level citations, quotes, confidence, and verification states
- Portable static HTML reports plus Excel, CSV, JSON, and markdown summary outputs
- Portfolio analytics and follow-up questioning on the resulting table

**Does not:**
- Replace clause-by-clause bespoke legal review of a single critical document
- Determine final legal acceptability without human review
- Guarantee OCR quality on poor scans
- Eliminate the need to verify missing, conflicting, or low-confidence answers

### Relationship to Nearby Skills

| Skill | Use This Skill Instead When |
|------|-----------------------------|
| `legalcode-contract-review` | The user needs a deep review of one document, not a portfolio matrix |
| `legalcode-contract-metadata-extractor` | The user only needs generic metadata extraction rather than custom questions |
| `legalcode-precedent-analyzer` | The goal is corpus analytics and playbook mining, not an answer table |
| `legalcode-case-timeline-builder` | The core output is chronology rather than a spreadsheet review grid |

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default. It can review portfolios spanning multiple
governing laws, but it must avoid collapsing jurisdiction-specific legal conclusions into a
single universal answer.

[JURISDICTION-SPECIFIC] When the user includes legal-risk or compliance columns, localize at
minimum:
- Governing law or jurisdiction source for each document
- Mandatory statutory rules that affect the answer
- Local terminology, date conventions, and execution formalities
- Consumer, employment, privacy, or regulated-industry overlays
- Language and translation issues where the source is not in English

If the corpus mixes jurisdictions, preserve jurisdiction as an explicit column and avoid
treating cross-jurisdiction answers as directly comparable unless the user asks for that.

---

## Interactive Clarification

Use interactive clarification whenever the answer changes extraction logic, table design, or
cost materially. If the user has already supplied the information, skip the question and
proceed.

**CLARIFY 1: Corpus source**
- Options: `single folder`, `multiple folders`, `specific file list`, `VDR export`, `DMS export`, `mixed`
- Why it matters: Controls inventory, dedupe, and provenance grouping.

**CLARIFY 2: Review objective**
- Options: `metadata extraction`, `due diligence matrix`, `red-flag table`, `compliance check`, `playbook comparison`, `custom`
- Why it matters: Changes default columns, answer style, and escalation thresholds.

**CLARIFY 3: Column design**
- Options: `I have exact questions`, `propose columns from corpus type`, `use playbook-driven columns`, `mixed`
- Why it matters: Prevents vague columns that produce low-value answers.

**CLARIFY 4: Output format**
- Options: `xlsx + markdown`, `csv + json`, `full export`, `markdown only`
- Default: `xlsx + markdown`
- Why it matters: Controls rendering and downstream usability.

**CLARIFY 5: Execution mode**
- Options: `auto-detect`, `Claude CLI workers`, `Task sub-agents only`
- Default: `auto-detect`
- Why it matters: Changes throughput, batching, and checkpointing behavior.

**CLARIFY 6: Confidence policy**
- Options: `surface only strong answers`, `include uncertain answers with flags`, `capture all possible answers`
- Default: `include uncertain answers with flags`
- Why it matters: Balances recall against noise.

**CLARIFY 7: Portfolio size**
- Options: `small (<25 docs)`, `medium (25-250)`, `large (250-2500)`, `very large (2500+)`
- Why it matters: Controls batch size, worker count, and whether to recommend staging.

**CLARIFY 8: Review posture**
- Options: `neutral extraction only`, `include risk labels`, `include playbook deviations`, `include legal commentary`
- Default: `neutral extraction only`
- Why it matters: Determines whether cells stay factual or include evaluative analysis.

---

## Dual-Path Architecture

This skill supports two execution paths with a shared schema.

### Path A: Claude Code CLI Workers

Preferred when `claude` CLI is available and the corpus is medium or large.

- Convert and normalize documents with deterministic shell tools
- Use `claude -p --model haiku` workers for extraction
- Use Sonnet or Opus for adjudication and synthesis
- Checkpoint every stage to support resume and retry

### Path B: Task Sub-Agent Fallback

Use when the CLI is unavailable.

- Convert documents with the same deterministic shell tools when possible
- Launch parallel Task sub-agents for extraction
- Use a stronger validation agent for low-confidence or conflicting cells
- Preserve the same output schema and review states

### Runtime Detection

At the start of every run:

```bash
HAVE_CLAUDE=false
HAVE_PDFTOTEXT=false
HAVE_PANDOC=false
HAVE_OCRMYPDF=false
HAVE_MARKITDOWN=false
HAVE_PYTHON3=false

command -v claude >/dev/null 2>&1 && HAVE_CLAUDE=true
command -v pdftotext >/dev/null 2>&1 && HAVE_PDFTOTEXT=true
command -v pandoc >/dev/null 2>&1 && HAVE_PANDOC=true
command -v ocrmypdf >/dev/null 2>&1 && HAVE_OCRMYPDF=true
command -v markitdown >/dev/null 2>&1 && HAVE_MARKITDOWN=true
command -v python3 >/dev/null 2>&1 && HAVE_PYTHON3=true
```

Select the path using user preference first, then tool availability, then corpus size.

---

## Workflow

### Step 1: Accept the Corpus

Accept documents as:
- Folder path
- Multiple folder paths
- Explicit file list
- VDR or DMS export directory
- Mixed collection of PDFs, DOCX, text files, and scans

Build an initial inventory:
- Absolute path
- File name
- Folder or source bucket
- Extension
- Size
- Hash if feasible
- Last modified time
- Approximate page count where available

If the corpus contains fewer than 2 documents, recommend a single-document review skill
unless the user explicitly wants a one-row table.

### Step 2: Define the Table Schema

Normalize every requested column into a structured extraction spec.

| Field | Meaning |
|------|---------|
| `column_name` | Final table header |
| `question` | Exact extraction prompt |
| `answer_type` | text, date, money, yes_no, enum, list, risk, citation_only |
| `format_rule` | normalization rule such as ISO date or currency format |
| `comparison_rule` | how values should align across documents |
| `required_evidence` | page, section, quote, or all |
| `review_policy` | auto-accept, verify-if-low-confidence, always-human-check |

If the user gives vague questions such as "important risks," rewrite them into answerable
cell prompts before extraction.

### Step 3: Build the Inventory and Dedupe Layer

Create a manifest that records:
- Document identity
- Source grouping
- Suspected duplicates
- Suspected superseded versions
- Document type guess
- Language guess
- Parse strategy

**If duplicates or version families exist:**
- Preserve both, but mark them clearly
- Prefer executed or final versions where the user wants one answer per deal
- Add optional columns such as `version_status` or `superseded_by`

### Step 4: Convert Documents to Reviewable Text

Prefer deterministic conversion before model extraction:

| File Type | Preferred Path | Fallback |
|----------|----------------|----------|
| PDF with selectable text | `pdftotext` | model reads pages directly |
| Scanned PDF | `ocrmypdf` then `pdftotext` | model vision path |
| DOCX | `pandoc` or `markitdown` | raw XML-aware fallback |
| Plain text / markdown | read directly | none |

Preserve page anchors and section cues. The extractor must be able to cite the answer source.

### Step 5: Create the Batch Plan

Plan work before launching workers:
- Group related columns together to reduce repeated reads
- Split long documents into stable chunks
- Assign short documents in bundles
- Separate high-risk evaluative columns from simple metadata columns

**Recommended pattern:**
- Batch A: identity and metadata
- Batch B: economics and dates
- Batch C: legal/risk or playbook columns
- Batch D: bespoke follow-up columns

### Step 6: Launch Parallel Extraction Workers

Use low-cost workers for first-pass extraction.

#### CLI worker pattern

```bash
claude -p --model haiku --max-turns 1 --output-format json
```

#### Task worker pattern

Launch a Task sub-agent per document or per document batch with instructions to return:
- normalized answer
- page or section
- quote snippet
- confidence
- extraction notes

Each worker must return JSON that conforms to the shared schema below.

### Step 7: Verification and Adjudication

Run a second pass for cells that are:
- low confidence
- missing evidence
- contradictory
- evaluative and high impact
- derived from poor OCR

Verification agent tasks:
- compare answer against source quote
- confirm page or section
- detect overclaiming beyond the source
- mark unresolved conflicts

### Step 8: Assemble the Review Grid

Render the main table with one row per document and one column per question. Include:
- normalized cell value
- verification state
- confidence
- source pointer
- optional comment or note

Recommended workbook sheets:
- `Review`
- `Sources`
- `Summary`
- `Extraction Parameters`
- `Conflicts` when needed

### Step 9: Portfolio Synthesis

After the table is assembled, optionally add:
- frequency counts
- missing-clause or missing-answer rates
- red-flag totals
- playbook deviation counts
- folder or jurisdiction rollups

Keep synthesis separate from extraction facts. Do not collapse uncertainty silently.

### Step 10: Deliver and Preserve Reusability

Deliver:
- review-data JSON payload
- portable report HTML
- review workbook
- machine-readable JSON or CSV
- markdown summary
- manifest/checkpoint reference

Treat the resulting table as a reusable knowledge source for follow-up questions. If the user
asks a second-order question, prefer using the verified table plus source register before
re-reading the entire corpus.

---

## Deep Review Model

### Column Types

| Type | Example | Normalization Rule |
|------|---------|--------------------|
| `text` | Governing law | concise factual answer |
| `date` | Effective date | `YYYY-MM-DD` when known |
| `money` | Liability cap | currency + amount + basis |
| `yes_no` | Termination for convenience | `Yes`, `No`, `Unclear` |
| `enum` | NDA type | controlled vocabulary |
| `list` | Carveouts | semicolon-separated items |
| `risk` | Data processing risk | risk label + short rationale |
| `citation_only` | Key indemnity section | source pointer only |

### Cell Schema

```json
{
  "document_id": "DOC-00124",
  "document_name": "msa-acme-final.pdf",
  "column_name": "Liability Cap",
  "answer": "Fees paid in prior 12 months",
  "answer_type": "text",
  "confidence": "high",
  "verification_state": "verified",
  "source": {
    "page": 14,
    "section": "10.2",
    "quote": "liability shall not exceed the fees paid in the twelve months..."
  },
  "notes": "cap excludes IP indemnity and confidentiality breach"
}
```

### Verification States

| State | Meaning |
|------|---------|
| `verified` | Answer matched source and passed review |
| `needs_review` | Answer plausible but not yet confirmed |
| `conflict` | Competing answers or inconsistent evidence |
| `not_found` | No support located after reasonable search |
| `failed` | Document or extraction failure prevented answer |

### Risk States for Evaluative Columns

If the user requests risk analysis, use a topic-appropriate scale and make the basis explicit.

| Skill Mode | Scale |
|-----------|-------|
| neutral extraction | no risk label |
| contract review | `GREEN / YELLOW / RED` |
| compliance check | `COMPLIANT / PARTIAL / NON-COMPLIANT` |
| diligence | `PASS / FLAG / FAIL` |

Never mix evaluative labels with factual answers without telling the user which columns are
interpretive.

---

## Actionable Output Rules

For every flagged or non-standard cell, provide:
- what was found
- where it was found
- how certain the extraction is
- what follow-up action is recommended

Recommended follow-up actions:
- verify source manually
- escalate to deeper document review
- add a bespoke follow-up column
- exclude from aggregate comparison
- treat as missing data

## Prioritization Framework

Use three priority tiers for follow-up work:

| Tier | Use |
|------|-----|
| `Tier 1` | broken extraction, major conflict, high-impact unanswered column |
| `Tier 2` | medium-confidence or ambiguous cells affecting analysis |
| `Tier 3` | polish, normalization, formatting improvements |

## Citation Quality Gates

Run these silently before final delivery:

| Gate | Rule | Fail Action |
|------|------|-------------|
| Source | Every answer cites a real document location or is marked `not_found` | re-run or flag |
| Format | Citation format is consistent across cells | normalize |
| Support | Answer does not overstate the quote | downgrade confidence or revise |
| Domain | Legal conclusions do not outrun factual extraction | separate fact from interpretation |
| Confidence | Uncertainty is explicit | add flag |

## Self-Interrogation for High-Impact Cells

For critical columns or red-flag findings, run three passes:

**Pass 1 - Source integrity**
- Does the answer actually appear in the cited text?

**Pass 2 - Alternative reading**
- Could a reasonable reviewer read the clause differently?

**Pass 3 - Portfolio consistency**
- Is this answer inconsistent with nearby documents, amendments, or schedules?

## Confidence Scoring

| Level | Meaning | Action |
|------|---------|--------|
| `definite` | exact answer with clean evidence | accept |
| `high` | strong answer with minor ambiguity | accept with citation |
| `probable` | answer likely correct but should be checked if important | verify if material |
| `possible` | weak support or OCR noise | surface with flag |
| `unlikely` | insufficient support | use `not_found` or `needs_review` |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-tabular-review"
  corpus_type: "[folder | multi-folder | VDR export | DMS export | mixed]"
  execution_path: "[cli | task]"
  document_count: "[count]"
  columns_count: "[count]"
outputs:
    - "report.html"
    - "review-data.json"
    - "review.xlsx"
    - "review.json"
    - "summary.md"
  verification_state_counts:
    verified: "[count]"
    needs_review: "[count]"
    conflict: "[count]"
    not_found: "[count]"
    failed: "[count]"
  jurisdiction_mode: "[single | mixed | unknown]"
  confidence: "[HIGH | MEDIUM | LOW]"
  limitations:
    - "[OCR quality, missing attachments, unsupported formats, or scope limits]"
  reviewer: "AI-assisted; human legal review required"
```

## Anti-Patterns

1. Treating vague prompts as executable columns without rewriting them.
2. Reading every column separately instead of batching related questions.
3. Returning answers without page, section, or quote support.
4. Collapsing conflicting versions into one row without marking the conflict.
5. Treating OCR output as reliable when the scan quality is poor.
6. Mixing factual extraction and legal advice in the same cell without labeling it.
7. Leaving blanks instead of `not_found`, `conflict`, or `failed`.
8. Comparing multi-jurisdiction documents without preserving jurisdiction metadata.
9. Ignoring schedules, exhibits, or incorporated terms that control the answer.
10. Re-running the whole corpus when only a few failed cells need retry.
11. Failing to preserve a machine-readable manifest and checkpoint trail.
12. Using summary-only outputs that cannot be audited back to the source document.

## Writing Standards

- Keep cell values short and comparable across rows.
- Prefer normalized answers over long prose.
- Put interpretation in notes or synthesis, not in factual cells.
- Use the same value style across the whole table.
- State uncertainty plainly.

## External Tool Integration

Use external tools opportunistically, not as hidden dependencies:

| Tool | Use |
|------|-----|
| `pdftotext` | selectable-text PDFs |
| `ocrmypdf` | scanned PDFs |
| `pandoc` | DOCX conversion |
| `markitdown` | mixed-format markdown conversion |
| `claude -p --model haiku` | first-pass extraction workers |
| Task sub-agents | fallback extraction and verification |
| `node path/to/legalcode-tabular-review/scripts/generate-report.mjs` | render a portable self-contained review report from `review-data.json` |

If tools are unavailable, degrade gracefully and record the limitation in the audit trail.

## Output Format Template

````markdown
# Tabular Review Summary

## 1. Review Snapshot
- Corpus type: [multi-folder / VDR / mixed]
- Documents processed: [count]
- Columns answered: [count]
- Execution path: [CLI / Task]
- Overall confidence: [HIGH / MEDIUM / LOW]

## 2. Corpus Summary
| Metric | Value |
|-------|-------|
| Documents inventoried | |
| Documents processed | |
| Duplicate families | |
| Mixed jurisdictions | |
| Extraction failures | |

## 3. Verification Summary
| State | Count |
|------|------:|
| verified | |
| needs_review | |
| conflict | |
| not_found | |
| failed | |

## 4. Priority Follow-Ups
### Tier 1
| Document | Column | Issue | Recommended action |
|---------|--------|-------|--------------------|

### Tier 2
| Document | Column | Issue | Recommended action |
|---------|--------|-------|--------------------|

## 5. Portfolio Findings
| Column | Most common value | Notes |
|-------|-------------------|-------|

## 6. Deliverables
- `report.html`
- `review-data.json`
- `review.xlsx`
- `review.json`
- `summary.md`

## 7. Glass Box Audit Trail
```yaml
[populate glass_box]
```
````

## Provenance

Created by Legalcode on 2026-04-09 as a Legalcode-original workflow skill informed by:
- Legora product research on Tabular Review and Workflows
- In-repo prior art from imported Lawvable and IURA tabular-review skills
- Dual-path execution patterns from `legalcode-case-timeline-builder`
- Corpus and playbook analytics patterns from `legalcode-precedent-analyzer`
