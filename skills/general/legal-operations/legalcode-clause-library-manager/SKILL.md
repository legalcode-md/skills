---
name: legalcode-clause-library-manager
description: Build, govern, and continuously improve contract clause libraries and negotiation playbooks
  for legal teams. Use when standardizing preferred clauses, fallback ladders, approval thresholds, and
  version control across MSAs, SaaS agreements, DPAs, procurement templates, and other recurring commercial
  contracts. Supports greenfield library creation, library cleanup, merger harmonization, and ongoing
  clause governance operations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Clause Library Manager

> **Disclaimer**: This skill provides a framework for AI-assisted legal operations,
> contract governance, and clause management. It does not constitute legal advice. All
> outputs should be reviewed by qualified legal professionals before implementation.
> Statutory and case-law statements carry hallucination risk if not independently verified.

## Purpose and Scope

Use this skill to design, operationalize, and govern a reusable clause library and
negotiation playbook that legal, procurement, sales, and contract operations teams can use
at scale.

**Covers:**

- Clause inventory creation and normalization from existing templates and redlines
- Clause taxonomy and metadata design for searchability and automation
- Preferred and fallback position ladders by clause family
- Governance workflows (proposal, review, approval, publication, retirement)
- Version control, auditability, and release management
- KPI-driven optimization using negotiation outcome data

**Does not:**

- Replace legal advice for transaction-specific enforceability questions
- Determine local-law validity without jurisdiction-specific legal review
- Draft final bespoke transaction documents without matter-level counsel review

## Invocation

Use this skill when asked to:

- Build a clause library from scratch
- Refactor an inconsistent or duplicate-heavy library
- Merge clause libraries after M&A or team consolidation
- Add fallback ladders and escalation rules to playbooks
- Establish review cadence, ownership, and quality controls

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic management skill. It governs clause operations, not final
legal enforceability outcomes. Mark jurisdiction-sensitive content as
`[JURISDICTION-SPECIFIC]` and require local counsel verification before publishing clauses
as "approved" for that jurisdiction.

[JURISDICTION-SPECIFIC] Common divergence areas to flag:

- Limitation-of-liability restrictions and mandatory carve-outs
- Penalty / liquidated damages enforceability
- Employment and contractor classification constraints
- Data transfer and privacy obligations
- Mandatory consumer protection and unfair terms rules
- Dispute resolution / arbitration enforceability limits

---

## Interactive Clarification

This skill uses **CLARIFY checkpoints** whenever user decisions materially affect clause
architecture or governance outcomes.

Use structured option questions where marked **CLARIFY**. Skip a question only when the
answer is already provided in the user's context.

---

## Workflow

### Step 1: Intake Objectives and Operating Context

Capture the target operating model.

**CLARIFY**:

1. Primary goal:
   - Build new library
   - Repair existing library
   - Merge multiple libraries
   - Prepare for CLM automation
2. Primary users:
   - Legal only
   - Legal + Procurement
   - Legal + Sales
   - Enterprise cross-functional
3. Target contract families:
   - MSA/SaaS
   - Procurement/Vendor
   - DPA/Privacy
   - Employment/HR
   - Other

### Step 2: Collect Inputs and Source Corpus

Gather current materials:

- Existing templates
- Negotiation playbooks
- Most-frequent redlines
- Approved fallback language in email/wiki/notes
- Escalation matrices and signature authority policies

If no corpus exists, bootstrap from current template set and recent negotiated deals.

### Step 3: Normalize and Deduplicate Clause Inventory

Create a normalized clause catalog:

- Decompose full contracts into clause units
- Remove exact/near duplicates
- Identify semantically equivalent variants
- Preserve historical references for auditability

Output: Canonical clause inventory draft.

### Step 4: Define Clause Taxonomy and Data Model

Assign each clause to a stable taxonomy.

Minimum taxonomy families:

- Commercial (fees, payment, term)
- Risk (liability, indemnity, warranty)
- Regulatory (privacy, sanctions, anti-bribery)
- Operational (SLA, support, change control)
- Dispute and boilerplate (governing law, notices, assignment)

Define required metadata schema (see Clause Data Model below).

### Step 5: Build Fallback Ladders and Escalation Logic

For each clause family, encode position ladder:

- Position A: Preferred
- Position B: Acceptable fallback
- Position C: Last-resort / high-risk fallback
- Position D: Prohibited (never accept)

**CLARIFY**:

- Should fallback depth be 3 levels (A/B/C) or 4 levels (A/B/C/D with explicit prohibited)?
- Should escalation be value-based, risk-based, or both?

### Step 6: Map Approval and Governance Ownership

Set ownership using RACI model:

- Responsible: Clause steward / legal ops analyst
- Accountable: Practice lead / senior counsel
- Consulted: Procurement, Security, Privacy, Finance
- Informed: Sales operations and business stakeholders

Define change request workflow:

- Proposal -> legal review -> stakeholder review -> approval -> publication -> retirement plan.

### Step 7: Encode Versioning and Release Management

Adopt release semantics:

- Major: Structural or policy-shifting clause changes
- Minor: Substantive but bounded language updates
- Patch: Typo/non-substantive clarifications

Require changelog entry per release:

- Why changed
- What changed
- Who approved
- Effective date
- Migration impact on active templates

### Step 8: Run Library Quality Gate Review

Evaluate every clause record against quality standards:

- Legal correctness (subject to local verification)
- Drafting clarity and ambiguity risk
- Negotiation usability (practical fallback)
- Playbook alignment and escalation mapping
- Metadata completeness

### Step 9: Pilot with Live Negotiations

Test on representative matters:

- Track acceptance rates per clause position
- Measure cycle-time impact
- Record escalation frequency and causes
- Capture counterparty pushback patterns

**CLARIFY**:

- Pilot window: 2 weeks, 30 days, or 60 days?
- Pilot contract families: one family or multi-family?

### Step 10: Publish Governance Baseline

Publish:

- Approved clause library
- Fallback matrix
- Escalation matrix
- Usage guidelines and owner directory
- Review cadence calendar

### Step 11: Operate Continuous Improvement Loop

Set recurring cadence (monthly or quarterly):

- Retire low-use or high-friction clauses
- Promote successful fallback variants
- Split overloaded clause categories
- Add new variants for recurring emerging issues

---

## Clause Data Model (Deep Topic Analysis)

Use this minimum record schema for each clause entry.

| Field                | Required    | Description                                       |
| -------------------- | ----------- | ------------------------------------------------- |
| `clause_id`          | Yes         | Stable unique identifier (immutable)              |
| `title`              | Yes         | Human-readable clause name                        |
| `family`             | Yes         | Taxonomy family (risk/commercial/regulatory/etc.) |
| `position_level`     | Yes         | A/B/C/D ladder tier                               |
| `jurisdiction_scope` | Yes         | Global or specific jurisdiction tags              |
| `approved_text`      | Yes         | Canonical clause wording                          |
| `fallback_text`      | Conditional | Alternative wording for next position             |
| `risk_rating`        | Yes         | Low/Medium/High/Critical                          |
| `escalation_trigger` | Yes         | Trigger conditions for legal escalation           |
| `owner`              | Yes         | Clause steward                                    |
| `approver`           | Yes         | Final legal approver                              |
| `version`            | Yes         | Semantic version                                  |
| `effective_date`     | Yes         | Go-live date                                      |
| `review_due_date`    | Yes         | Next scheduled review                             |
| `status`             | Yes         | Draft/Approved/Deprecated/Retired                 |
| `change_rationale`   | Yes         | Why this version exists                           |

## Clause Status Classification

Classify each candidate clause variant before publication:

| Status                       | Meaning                                      | Required Action                             |
| ---------------------------- | -------------------------------------------- | ------------------------------------------- |
| **APPROVED**                 | Ready for routine use without extra approval | Publish in active library                   |
| **APPROVED-WITH-CONDITIONS** | Usable only when specified conditions apply  | Add explicit escalation and condition notes |
| **DRAFT**                    | Under review / not yet approved              | Keep out of production templates            |
| **REJECTED**                 | Unacceptable clause pattern                  | Record rationale and prohibit usage         |
| **DEPRECATED**               | Superseded clause variant                    | Retain for audit history only               |

## Actionable Output per Finding

For each identified issue in the library, provide:

- Finding summary
- Affected clause IDs
- Severity and business impact
- Remediation step (exact)
- Owner and due date
- Proposed replacement text (if applicable)

## Prioritization Framework

Prioritize remediation using three tiers.

| Tier       | Priority        | Typical Issues                                                                        | Expected Action                    |
| ---------- | --------------- | ------------------------------------------------------------------------------------- | ---------------------------------- |
| **Tier 1** | Must-fix now    | Missing escalation triggers, prohibited language in active templates, broken metadata | Block release until fixed          |
| **Tier 2** | Should-fix soon | Weak fallback coverage, inconsistent taxonomy, unclear negotiation notes              | Fix in current cycle               |
| **Tier 3** | Improve later   | Cosmetic standardization, legacy alias cleanup, optional tags                         | Queue for next optimization sprint |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these gates silently before delivering final output:

| Gate           | Rule                                                                              | Fail Action                                             |
| -------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Source**     | Any legal/regulatory claim ties to identifiable authority or is marked `[VERIFY]` | Add source or mark `[VERIFY]`                           |
| **Format**     | References are consistently formatted                                             | Normalize reference style                               |
| **Currency**   | Time-sensitive standards and links are checked for recency                        | Flag `[CHECK CURRENCY]`                                 |
| **Domain**     | Keep management guidance distinct from enforceability advice                      | Move enforceability claims to `[JURISDICTION-SPECIFIC]` |
| **Confidence** | Uncertainty is explicit                                                           | Add confidence statement                                |

### Self-Interrogation (for Tier 1 items)

For each Tier 1 item, run 3 passes:

1. **Integrity pass**: Is the issue materially real or a classification artifact?
2. **Completeness pass**: Did we capture every affected template/clause ID?
3. **Challenge pass**: What argument could justify not fixing now, and why is that insufficient?

### Confidence Scoring

| Level        | Range     | Meaning                                    | Action                         |
| ------------ | --------- | ------------------------------------------ | ------------------------------ |
| **Definite** | 0.95-1.00 | High evidence and clear controls           | Proceed                        |
| **High**     | 0.80-0.94 | Strong evidence with minor gaps            | Proceed with brief caveat      |
| **Probable** | 0.60-0.79 | Reasonable evidence, unresolved edge cases | Proceed + targeted review      |
| **Possible** | 0.40-0.59 | Material uncertainty                       | Flag for legal ops lead review |
| **Unlikely** | 0.00-0.39 | Weak basis                                 | Do not publish recommendation  |

---

## Glass Box Audit Trail

Use this template for every substantial library update.

```yaml
glass_box:
  skill_name: "legalcode-clause-library-manager"
  run_date: "YYYY-MM-DD"
  scope: "Build / Cleanup / Merge / Optimization"
  contract_families:
    - "[Family 1]"
    - "[Family 2]"
  source_materials_count: 0
  clause_records_processed: 0
  quality_findings:
    tier1: 0
    tier2: 0
    tier3: 0
  approvals:
    accountable_owner: "[Name/Role]"
    approved_at: "[Timestamp]"
  legalcode_mcp: "Not connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  confidence: "HIGH / MEDIUM / LOW"
  limitations:
    - "[Example: Jurisdiction-specific enforceability not fully validated]"
  reviewer: "AI-assisted output; qualified legal review required"
```

---

## Anti-Patterns

Avoid these failure modes:

1. Publishing clauses without clear owner and approver metadata.
2. Treating one negotiated outcome as universal policy.
3. Storing fallback language in email threads instead of canonical library records.
4. Mixing jurisdiction-specific constraints into global default clauses without markers.
5. Skipping explicit "prohibited" positions for high-risk topics.
6. Running updates without changelogs or version IDs.
7. Allowing duplicate clauses to diverge silently over time.
8. Ignoring negotiation analytics when revising fallback ladders.
9. Classifying too many issues as high severity (alert fatigue).
10. Publishing clause records with missing escalation triggers.
11. Retiring clauses without migration notes for active templates.
12. Using generic labels that hide legal significance (for example, "general liability text").
13. Building a library that legal can use but commercial teams cannot understand.
14. Treating template text and clause-library text as separate uncontrolled sources of truth.
15. Failing to revalidate library content after major regulatory change.

---

## Writing Standards

Apply these rules before final delivery:

- Use plain, concrete language and avoid vague process verbs.
- Distinguish recommendations from hard requirements.
- Tie each remediation to owner, deadline, and measurable outcome.
- Avoid pseudo-authority language; use `[VERIFY]` when needed.
- Keep tables normalized and terminology consistent across sections.

Pre-delivery checks:

- Every Tier 1 issue has an explicit remediation owner.
- Every proposed clause action references clause IDs.
- Every jurisdiction-sensitive claim is marked `[JURISDICTION-SPECIFIC]` or `[VERIFY]`.

---

## External Tool Integration

### With legalcode-mcp connected

Use legalcode-mcp to validate jurisdiction-sensitive clause enforceability assumptions and
regulatory constraints before marking a clause as `APPROVED` for a jurisdiction-specific
scope.

### Without legalcode-mcp

Proceed with structural/governance optimization and mark legal assertions `[VERIFY]`.
Record in audit trail:

- `legalcode_mcp: "Not connected"`

### Web research guidance

For operational standards and market practice, use high-quality sources and tag uncertain
claims as `[VERIFY]`.

---

## Output Format Template

## Clause Library Governance Summary

- **Objective**: [Build/Cleanup/Merge/Optimize]
- **Scope**: [Families / business units / jurisdictions]
- **Confidence**: [Definite/High/Probable/Possible/Unlikely]

## Current-State Findings

| Finding ID | Severity Tier | Affected Clauses | Issue   | Business Impact |
| ---------- | ------------- | ---------------- | ------- | --------------- |
| F-001      | Tier 1        | [IDs]            | [Issue] | [Impact]        |

## Recommended Remediation Plan

| Priority | Action   | Owner   | Deadline | Success Metric |
| -------- | -------- | ------- | -------- | -------------- |
| Tier 1   | [Action] | [Owner] | [Date]   | [Metric]       |

## Fallback Matrix (Updated)

| Clause Family | Position A | Position B | Position C | Position D (Prohibited) |
| ------------- | ---------- | ---------- | ---------- | ----------------------- |
| [Family]      | [Summary]  | [Summary]  | [Summary]  | [Summary]               |

## Governance and Release Decisions

- **Approvals required**: [Roles]
- **Release type**: [Major/Minor/Patch]
- **Effective date**: [Date]
- **Review cadence**: [Monthly/Quarterly]

## Glass Box Audit Trail

```yaml
[Paste completed glass_box object]
```

## Localization Notes

If publishing jurisdiction-specific variants:

- Replace `[JURISDICTION-SPECIFIC]` markers with validated local-law language.
- Keep global baseline and local variants separately versioned.
- Add local counsel sign-off requirement before status changes to `APPROVED`.

## Provenance

Created by Legalcode (2026-02-28) as a high-priority skill from
`SKILL_CREATION_TASKS.md` (`legalcode-clause-library-manager`).

Enhanced from initial scaffold using:

- parallel structural and prompt-quality analysis (agent-team method)
- in-repo reference standards (`legalcode-contract-review`, `legalcode-review-contract`)
- web-backed research via Perplexity/OpenRouter (`perplexity/sonar-pro-search`)
- research log at `/tmp/legalcode-enhancement-research.md`

Research references used for operational framing are marked `[VERIFY]` where independent
verification is still required.
