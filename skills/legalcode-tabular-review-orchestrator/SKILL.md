---
name: legalcode-tabular-review-orchestrator
description: >
  Orchestrate citation-backed tabular review over one or more local folders by turning a
  user-supplied question list into a review matrix with one row per document and one
  column per question. Use when the user wants Codex to actually run the workflow inside
  this repository: discover files, convert PDFs and DOCX to reviewable text, fan out
  cheap extraction workers, normalize answers, assemble CSV / Markdown / JSON / XLSX
  outputs, and preserve cell-level provenance. Prefer this skill over ad hoc scripting
  whenever the task involves repeated questions across many documents, portfolio review,
  diligence matrices, or side-by-side extraction from folders.
---

# Legalcode Tabular Review Orchestrator

This is the **Codex operator skill** for tabular review work in this repository.

Use it together with the user-facing legal workflow skill:

- `skills/general/workflows/legalcode-tabular-review/SKILL.md`

That skill defines the semantic contract for the review. This skill defines how Codex
should execute it pragmatically in the current environment.

## Core Contract

Given:

- one or more folders or file lists,
- a set of review questions / columns,
- and an output preference,

produce:

- a corpus inventory,
- a citation-backed review table,
- JSON / CSV / Markdown outputs,
- optional XLSX workbook,
- and a short summary of unresolved cells and follow-up actions.

## First Actions

1. Confirm the actual corpus inputs from the user prompt.
2. Read the user-facing workflow skill at:
   - `skills/general/workflows/legalcode-tabular-review/SKILL.md`
3. Detect whether the user already specified:
   - folder path(s),
   - exact columns,
   - output format,
   - and whether the review is purely factual or partly legal / evaluative.
4. If the request is underspecified, make conservative defaults explicit and proceed.

## Execution Principles

1. **Prefer deterministic tooling first.**
   - Use shell and conversion tools to inventory and extract text before using model calls.
2. **Treat every document-question answer as an auditable unit.**
   - Never emit freeform portfolio conclusions without preserving the cell-level evidence.
3. **Scale by decomposition.**
   - Use small extraction jobs in parallel instead of one giant prompt.
4. **Never hide uncertainty.**
   - Use explicit statuses: `VERIFIED`, `PROBABLE`, `CONFLICT`, `NOT_FOUND`, `UNREADABLE`.
5. **Checkpoint long runs.**
   - Persist manifests and partial outputs so reruns are resumable.
6. **Default to local processing.**
   - Do not send raw document corpora to external services unless the environment and user request clearly allow it.

## Tool Detection

Check availability early with `exec_command`:

- `claude`
- `python3`
- `magic-pdf`
- `pdftotext`
- `ocrmypdf`
- `pandoc`
- `markitdown`

Record the result in the run summary.

### Preferred Conversion Order

| Format | Preferred | Fallback |
|---|---|---|
| born-digital PDF | `magic-pdf` | `pdftotext` |
| scanned PDF | `ocrmypdf` then `magic-pdf` | mark `UNREADABLE` if still unusable |
| DOCX | `pandoc` | `markitdown` |
| mixed / unknown | `markitdown` trial pass | manual routing |

## Runtime Modes

### Mode A: Claude CLI available

Use this when `claude` exists and the corpus is medium or larger.

Pattern:

1. inventory files,
2. convert to markdown / text,
3. create a document manifest,
4. batch extraction jobs,
5. run `claude -p --model haiku` workers in parallel,
6. normalize and merge outputs,
7. run Sonnet- or Opus-class QA pass,
8. emit final artifacts.

Use CLI workers for extraction because they are:

- cheaper,
- more parallelizable,
- and easier to resume.

### Mode B: No Claude CLI

Use Codex's own reasoning plus sub-agents when available.

Pattern:

1. inventory and convert with shell tools,
2. split document work into small independent tasks,
3. use agent team delegation for parallel extraction / QA when the environment supports it,
4. otherwise process in explicit batches,
5. normalize results centrally,
6. emit the same output schema as Mode A.

## Agent Team Design

Spawn or simulate this team whenever the corpus is non-trivial.

| Agent | Purpose | Notes |
|---|---|---|
| `inventory-router` | find documents, classify types, dedupe paths, produce manifest | deterministic-first |
| `extractor` | answer 3-8 related questions for one document | use Haiku-class model when available |
| `row-normalizer` | standardize dates, amounts, booleans, and source anchors | central merge point |
| `conflict-reviewer` | inspect inconsistent candidates and set `CONFLICT` when needed | never paper over contradictions |
| `qa-auditor` | spot-check important cells and overall schema completeness | run before delivery |

### Delegation Rules

- Use an agent team when the user explicitly asks for sub-agents, agent team, or parallel review.
- Keep extractor prompts narrow and typed.
- Prefer one document x small question bundle as the extraction unit.
- Do not delegate final synthesis until all worker outputs are normalized.

## File Discovery

Prefer fast local discovery:

- `rg --files <path>` for broad listings when applicable
- `find` for extension filtering or deeper directory control

Collect:

- absolute path,
- extension,
- size,
- modified time,
- source folder,
- probable document type.

Build a manifest like:

```json
[
  {
    "path": "/abs/path/doc1.pdf",
    "ext": "pdf",
    "source_folder": "/abs/path/contracts",
    "document_type": "msa",
    "status": "pending"
  }
]
```

## Output Workspace

Create a dedicated run workspace under a deterministic temp directory, for example:

```text
/tmp/legalcode-tabular-review-YYYYMMDD-HHMMSS/
```

Recommended files:

- `manifest.json`
- `columns.json`
- `converted/<doc-id>.md`
- `raw-extractions/<doc-id>.json`
- `normalized/rows.json`
- `review-table.csv`
- `review-table.json`
- `review-summary.md`
- `review-table.xlsx` when available

## Column Schema

Before extraction, normalize the user's questions into a schema:

```json
[
  {
    "name": "Governing Law",
    "type": "text",
    "question": "What governing law clause appears in the document?",
    "normalization": "short-string",
    "legal_interpretation": false
  }
]
```

Do not begin extraction until the column schema is stable enough to avoid rework.

## Extraction Prompt Contract

Each extractor must return machine-readable JSON only.

Minimum shape:

```json
{
  "document": "doc1.pdf",
  "path": "/abs/path/doc1.pdf",
  "results": [
    {
      "column": "Governing Law",
      "value": "Delaware",
      "status": "VERIFIED",
      "confidence": 0.93,
      "citation": {
        "page": 12,
        "section": "10.6",
        "quote": "This Agreement shall be governed by the laws of the State of Delaware."
      },
      "notes": ""
    }
  ]
}
```

Rules:

- no Markdown wrappers,
- no prose outside the JSON,
- no invented values,
- and no missing citation for non-empty answers unless the status is explicitly downgraded.

## Normalization Rules

Centralize normalization after extraction.

Normalize:

- dates to ISO where reliable,
- currencies to code + amount,
- booleans to `yes` / `no` / `unclear`,
- and long textual answers to concise comparable forms.

Preserve original nuance in:

- `notes`,
- `support_quote`,
- or a source register artifact.

## Status Policy

Use these exact statuses:

| Status | Meaning |
|---|---|
| `VERIFIED` | clear answer with source anchor |
| `PROBABLE` | likely answer with caveat |
| `CONFLICT` | competing or contradictory answers |
| `NOT_FOUND` | no answer identified in reviewed text |
| `UNREADABLE` | conversion / OCR prevented reliable review |

Never silently coerce `CONFLICT` or `UNREADABLE` into an answer string.

## Quality Gates

Before delivery, verify:

1. every requested document appears in the final output or is explicitly marked failed,
2. every requested column exists in the final schema,
3. every non-empty cell has:
   - a status,
   - a confidence,
   - and a citation or explanation,
4. row counts match manifest counts,
5. no document was dropped during merge,
6. and Tier 1 cells were surfaced in the summary.

## Export Rules

### Always produce

- `review-table.json`
- `review-table.csv`
- `review-summary.md`

### Produce XLSX when feasible

If `python3` and spreadsheet support are available, generate:

- `review-table.xlsx`

Workbook expectations:

- frozen header row,
- autofilter,
- color-coded status cells,
- source comments or a dedicated `Sources` sheet,
- and a `Summary` sheet with cell counts by status.

If XLSX is not feasible, say so and fall back to CSV + Markdown without blocking completion.

## Legal Interpretation Guardrail

If a user column asks for legal interpretation rather than factual extraction:

- keep the factual basis and legal conclusion separate,
- state the governing law assumption,
- and if external legal research is truly needed, route that research through the repository's legal research pattern rather than improvising from memory.

## Failure Handling

| Failure | Response |
|---|---|
| document unreadable | mark `UNREADABLE`, retry OCR once if appropriate, then escalate |
| weak extraction confidence | downgrade to `PROBABLE` |
| contradictory clauses | mark `CONFLICT` and cite both |
| missing annexes | ask whether to expand scope |
| spreadsheet export unavailable | ship CSV + JSON + Markdown |
| corpus too large for one pass | stage by subset or document type |

## Delivery Format

When the run completes, present:

1. what corpus was reviewed,
2. how many documents and columns were processed,
3. which runtime mode was used,
4. status counts,
5. where the artifacts were written,
6. and the top unresolved review items.

Always keep the close-out concise. The user does not need a changelog of every intermediate file.

## Anti-Patterns

1. Running extraction before the column schema is stable.
2. Treating the table as a narrative report instead of a structured artifact.
3. Letting one failed document silently disappear from the output.
4. Using one generic prompt across incompatible document types.
5. Normalizing away clause qualifiers that matter.
6. Writing XLSX first and discovering data errors later.
7. Hiding uncertainty behind confident wording.
8. Re-reading large files serially when conversion outputs can be reused.
9. Ignoring deduplication in folders with drafts and copies.
10. Forgetting to checkpoint batch results on large corpora.

## Provenance

Created in response to a Legalcode request to design a Legora-style tabular review workflow
 with explicit agent-team and sub-agent support, alongside a companion user-facing skill.
Design sources include:

- `docs/brainstorms/2026-04-09-legora-tabular-review-agentic-design.md`
- `skills/general/workflows/imported-lawvable-tabular-review/SKILL.md`
- `skills/general/workflows/imported-iura-plugins--iura-pl-skills-tabular-review/SKILL.md`
- `skills/general/workflows/legalcode-precedent-analyzer/SKILL.md`
- `skills/general/litigation/legalcode-case-timeline-builder/SKILL.md`
