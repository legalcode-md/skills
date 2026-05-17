# Legalcode Tabular Review Research

> Research date: 2026-04-09
>
> Scope: official product pages, help pages, and release notes for Legora and nearby products,
> plus in-repo skill precedents that already model parts of the workflow.

## Executive View

Legora's current tabular-review pattern is best understood as a governed spreadsheet for legal
review: rows are documents, columns are prompts, each cell can expand into reasoning and source
documents, and review collaboration is part of the product, not an afterthought. The strongest
design lesson is that the table is not just a report. It is the operating surface for review,
verification, and follow-up analysis.

The closest comparison points as of April 9, 2026 are:
- Legora for spreadsheet-first review UX
- Harvey for review-table verification states and workflow reuse
- Thomson Reuters CoCounsel for answer tables and export discipline
- Kira for bulk ingest, dedupe, and governed diligence workflows
- LEGALFLY for playbook-driven multi-review across data rooms
- Luminance for broader agentic contract-lifecycle orchestration

## Product Comparison

| Vendor | Input model | Output model | Trust / transparency | Collaboration / verification | Scale / parallelism | Workflow / agentic positioning | Implication for Legalcode |
|------|-------------|--------------|----------------------|------------------------------|---------------------|-------------------------------|---------------------------|
| Legora | DMS, databases, VDRs, chat-created reviews from mentioned files | Searchable spreadsheet-like table; rows are docs; prompts become columns | Each cell can expand to show reasoning and source documents | Mark as Reviewed, Lock Cells, Review Mode, comments, activity tracking, real-time collaboration | Product pages say thousands of documents | Workflows connects Tabular Review, Legal Research, Translation, Drafting, and database search in one system | Build the table as a governed review surface, not just a final export |
| Harvey | Desktop uploads or a single vault source | Review tables with filtering, flags, export, and reusable table-as-knowledge-source patterns | Reasoning, sentence-level citations, verification metadata | Multi-color flags, verified states, workflow insertion | Help and release notes describe up to 10k docs and 100 questions | Review tables live inside Assistant, Vault, Knowledge Bases, and Workflow Builder | Reuse the verified table as a second-pass knowledge source |
| CoCounsel | File uploads and document review skill inputs | Answer table with short answer, longer explanation, and export to Word or Excel | Page citations in fuller analysis and clear verification messaging | Editable question list, follow-up questioning | Public help states large-batch support and later workflow reuse | Skills, prompts, and workflows | Keep question normalization and export discipline tight |
| Kira | Bulk import, data room integrations, many file types | Analysis Grid plus exports to Word, Excel, and PDF | Linked citations, concept search, smart summaries | Tagging, grouping, assignments, governance controls | High-volume diligence positioning | Kira plus Lito AI legal agent | Add manifest, dedupe, classification, and analysis-grid concepts |
| LEGALFLY | Data rooms, SharePoint, mixed contract sets | Structured tables and diligence packs | Source links and audit trail | Playbooks, governed review patterns | Public marketing describes dozens to hundreds of docs, with explicit FAQ caps in some flows | Agentic legal operating system | Make playbook-driven review a first-class mode |
| Luminance | Contract repositories and contract workflow data | Clause/risk analysis, model comparisons, redrafts | Source visibility and audit trail | Multi-agent and institutional-memory positioning | Enterprise-wide positioning | Broader legal workflow operating system | Keep our scope narrower: spreadsheet review first, broader workflow second |

## Legora-Specific Observations

### What Legora appears to do especially well

1. Spreadsheet-first mental model
   - The product page describes importing documents so that each document becomes a row and
     prompts become columns.
2. Per-cell transparency
   - Cells can be expanded into reasoning and source-document support.
3. Review-state controls
   - Collaboration is structured through review mode, mark-reviewed, and lock-cell controls.
4. Workflow adjacency
   - Tabular Review is not isolated; it sits beside research, drafting, and translation.
5. Reusable expertise
   - Product copy emphasizes reusable templates and institutionalized legal knowledge.

### What Legora does not publicly spell out clearly

1. A hard public file cap on current product pages
2. A public native Excel-export description on the tabular-review page
3. Public details on retry semantics, checkpointing, or failure recovery
4. Public details on version-family handling across duplicates or amendments

## Nearby Product Signals

### Harvey

The strongest Harvey signal is that a review table can become a workflow source rather than a
one-off artifact. That supports a Legalcode design where the extracted table becomes the basis
for second-order questions, rollups, or issue escalation without forcing a full re-read of the
corpus.

### CoCounsel

CoCounsel's public help emphasizes table output, concise questions, and exportable results with
citation-aware analysis. That is a strong argument for strict question normalization before
extraction starts.

### Kira

Kira's product positioning reinforces the need for:
- bulk ingest
- dedupe
- classification and grouping
- explicit exports

This argues for a manifest-and-grid architecture rather than a loose collection of prompts.

### LEGALFLY

LEGALFLY reinforces playbook-driven review and portfolio treatment of data rooms. It is a
useful reference for aligning extraction with negotiated positions or compliance baselines.

### Luminance

Luminance is broader than tabular review. The useful lesson is not its exact UX, but its
platform framing: multi-agent assistance, institutional memory, and portfolio-wide analysis.

## Repo Precedents

| Local skill | What it contributes |
|------------|---------------------|
| `skills/general/workflows/imported-lawvable-tabular-review/SKILL.md` | basic row-column extraction flow, background-agent pattern, Excel output |
| `skills/general/workflows/imported-iura-plugins--iura-pl-skills-tabular-review/SKILL.md` | better review taxonomy, Excel sheet design, risk labeling, explicit source handling |
| `skills/general/workflows/legalcode-precedent-analyzer/SKILL.md` | corpus inventory, segmentation, document typing, statistics mindset |
| `skills/general/litigation/legalcode-case-timeline-builder/SKILL.md` | dual-path CLI versus sub-agent architecture, runtime detection, conversion tool ladder, checkpoints |

## Design Decisions for Legalcode

### 1. Shared schema first

Both runtime variants should use the same:
- manifest schema
- column/question schema
- cell evidence schema
- verification-state model
- output sheet layout

### 2. Deterministic normalization before LLM extraction

Do not make OCR, PDF cleanup, or DOCX conversion part of the reasoning layer when a deterministic
tool can do it first. Reasoning should start from normalized text with page anchors where
possible.

### 3. Haiku for extraction, stronger model for adjudication

Use cheap workers for first-pass extraction. Escalate only:
- low-confidence cells
- contradictory cells
- poor-OCR cells
- evaluative columns with material downstream impact

### 4. Verification state must be first-class

Every cell should carry a clear state:
- verified
- needs_review
- conflict
- not_found
- failed

### 5. Reusable knowledge source

The produced table should support follow-up queries and portfolio rollups without restarting the
entire pipeline.

### 6. Multiple folders should be native

Do not flatten source folders away. Preserve source grouping so users can filter by matter, deal
room, client, or repository.

## Proposed Shared Output Contract

### Main workbook sheets

1. `Review`
2. `Sources`
3. `Summary`
4. `Extraction Parameters`
5. `Conflicts` when needed

### Cell evidence contract

```json
{
  "answer": "Fees paid in prior 12 months",
  "confidence": "high",
  "verification_state": "verified",
  "source": {
    "page": 14,
    "section": "10.2",
    "quote": "liability shall not exceed the fees paid in the twelve months..."
  }
}
```

## Recommended Architecture

| Stage | Component | Default model / tool | Reason |
|------|-----------|----------------------|--------|
| Intake | orchestrator | stronger reasoning model | normalize scope and questions |
| Inventory | scanner | deterministic | file system truth first |
| Conversion | document normalizer | `pdftotext`, `ocrmypdf`, `pandoc`, `markitdown` | lower cost and higher reproducibility |
| Extraction | per-doc workers | Haiku | cheapest scalable cell extraction layer |
| Verification | adjudicator | stronger model | resolve ambiguity and weak support |
| Rendering | deterministic renderer | Python or spreadsheet writer | keep tables stable and testable |
| Synthesis | optional summary | stronger model | executive summary only |

## Open Gaps

1. No in-repo generic batch runner currently dedicated to tabular review
2. No shared JSON schema file yet for review cells
3. No repository-standard Excel renderer for this workflow yet
4. No explicit review-state UI layer in repo-native tooling today

## Sources

### Legora

- Tabular Review: https://legora.com/product/tabular-review
- Workflows: https://legora.com/product/workflows
- Portal announcement: https://legora.com/newsroom/portal-announcement
- Addleshaw Goddard announcement mentioning large-scale tabular review use: https://legora.com/newsroom/addleshaw-goddard-enhances-legal-services-by-adopting-legora-platform

### Harvey

- Review Tables in Custom Workflows: https://eu.help.harvey.ai/release-notes/review-tables-in-custom-workflows
- Multi-Color Flagging for Review Tables: https://help.harvey.ai/release-notes/multi-color
- Folder Uploads and One-Way Sync: https://help.harvey.ai/release-notes/folder-uploads

### Thomson Reuters / CoCounsel

- Review Documents help: https://www.thomsonreuters.com/en-us/help/cocounsel/legal/skills/skills-prompts-workflows/review-documents
- March 2026 CoCounsel Monthly Insider: https://www.thomsonreuters.com/en-us/posts/innovation/cocounsel-legal-monthly-insider-march-2026/

### Litera / Kira

- Kira product page: https://www.litera.com/products/kira

### LEGALFLY

- Review: https://www.legalfly.com/products/review
- Multi Review: https://www.legalfly.com/products/multi-review
- Playbooks: https://www.legalfly.com/platform/playbooks
- Legal Radar: https://www.legalfly.com/products/legal-radar

### Luminance

- Main site: https://www.luminance.com/
- Negotiate: https://www.luminance.com/negotiate/
- Institutional-memory release: https://www.luminance.com/press/luminance-launches-new-legal-ai-with-institutional-memory-addressing-enterprise-amnesia-and-giving-legal-teams-30-of-their-time-back/

