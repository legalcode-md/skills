---
name: legalcode-obligation-tracker
description: >
  Extract, normalize, prioritize, and monitor post-signature contract obligations across
  executed agreements, amendments, renewals, and incorporated documents. Use when legal,
  procurement, finance, sales operations, vendor management, and compliance teams need an
  auditable obligation register with owners, trigger logic, due-date computation,
  escalation pathways, and confidence-scored outputs. Supports single-contract and
  portfolio modes, jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Obligation Tracker

> **Disclaimer**: This skill provides a framework for AI-assisted obligation extraction,
> tracking, and escalation from executed contracts. It does not constitute legal advice.
> All outputs should be reviewed by qualified legal professionals before operational use.
> Laws change and contract interpretation can vary by jurisdiction and facts; verify
> enforceability-sensitive conclusions before relying on them.

## Purpose and Scope

Use this skill to transform executed contracts into an operational obligation system that is
traceable, risk-aware, and updateable over time.

**Covers:**
- Post-signature obligation extraction from main agreements, schedules, exhibits, and amendments.
- Trigger and deadline computation (absolute dates, relative notice windows, recurring cadences).
- Owner mapping (primary, backup, approving function) and escalation routing.
- Risk/status classification with remediation actions.
- Audit-ready output package (register, alert queue, assumptions, confidence, evidence links).
- Portfolio mode for prioritizing obligations across many contracts.

**Does not:**
- Replace counsel for disputed interpretation or litigation positions.
- Guarantee legal enforceability in any jurisdiction.
- Draft complete agreements from scratch.
- Operate as a calendar system by itself; it prepares tracking-ready outputs for systems of record.

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default. Determine governing law from each contract
and localize enforceability-sensitive rules where required.

Use **[JURISDICTION-SPECIFIC]** markers for jurisdiction-dependent areas, including:
- Notice validity requirements (method, recipient, timing, deemed-delivery rules).
- Auto-renewal and cancellation constraints.
- Limits on liability for missed obligations and cure rights.
- Mandatory consumer, employment, public-sector, or regulated-industry obligations.
- Record retention and evidence standards for compliance obligations.

If governing law is missing or conflicting, flag it as high-risk and escalate.

---

## Interactive Clarification

Use **CLARIFY** prompts whenever the answer changes extraction logic, deadlines, severity,
or ownership decisions.

Ask before proceeding when:
- Represented side is unclear.
- The system of record (CLM/ticketing/calendar) is unknown.
- Renewal and notice horizons are not defined.
- Amendment ingestion scope is uncertain.
- Risk tolerance and escalation SLAs are not provided.

If context is incomplete, proceed with explicit assumptions and list each one in the output.

---

## Workflow

### Step 1: Accept Input Corpus
Accept all relevant artifacts:
- Executed base agreement.
- Amendments/addenda/change orders.
- Statements of work/order forms.
- Incorporated policies/online terms.
- Existing obligation logs (if available).

If incorporated documents are missing, create a blocker list and classify associated
obligations as provisional.

### Step 2: Gather Operating Context
**CLARIFY**:
1. Represented side (customer/buyer, vendor/supplier, licensor/licensee, other).
2. Tracking objective (compliance assurance, commercial value protection, renewal control, all).
3. Operating mode (single contract vs. portfolio).
4. System of record (CLM, ERP, ticketing, spreadsheet, mixed).
5. Alert strategy (daily, weekly, milestone-based) and escalation SLA.

Record answers as hard constraints.

### Step 3: Determine Governing Law and Contract Topology
- Identify governing law, jurisdiction, and dispute venue.
- Build a dependency map showing parent agreement and all related artifacts.
- Detect supersession language that deactivates older obligations.

**CLARIFY** when multiple governing-law clauses conflict.

### Step 4: Extract Obligation Candidates
Extract obligations from all sections, including boilerplate where relevant.

Minimum extraction fields:
- Obligation text (normalized statement).
- Performing party.
- Benefiting party.
- Trigger event.
- Due date rule.
- Frequency/recurrence.
- Cure period (if any).
- Survival flag.
- Source citation (document + section).

### Step 5: Normalize Triggers and Dates
Convert timing logic into machine-actionable rules:
- Absolute date (`YYYY-MM-DD`).
- Relative date (`X days after event`).
- Window (`no later than X days before renewal date`).
- Recurrence (`monthly`, `quarterly`, `annually`, `upon request`).

If an anchor date is missing, mark as `UNRESOLVED_DATE` and require manual completion.

### Step 6: Deduplicate and Consolidate
- Merge semantically equivalent obligations repeated across exhibits.
- Keep provenance links to every source clause.
- Preserve stricter term if conflict exists, unless superseded.

### Step 7: Classify Obligation Type and Business Impact
Map each obligation into taxonomy buckets:
- Legal/compliance notice.
- Payment/billing.
- Service-level/performance.
- Security/privacy.
- Audit/reporting.
- Insurance/certification.
- Change-control/governance.
- Renewal/termination.
- Survival/post-termination.

Assign impact dimensions:
- Legal/regulatory exposure.
- Financial exposure.
- Operational continuity.
- Relationship/reputational impact.

### Step 8: Assign Owners and Controls
For each obligation assign:
- Primary owner (role, not person-only).
- Backup owner.
- Approver/escalation owner.
- Evidence artifact expected on completion.

**CLARIFY** if owners are ambiguous across legal/procurement/operations.

### Step 9: Severity and Status Scoring
Score each obligation for tracking intensity and escalation urgency using the framework
below, then classify status.

### Step 10: Build Alert and Escalation Queue
Generate alert schedule and escalation actions:
- T-30/T-14/T-7/T-1 for major obligations (configurable).
- Immediate escalation for overdue critical obligations.
- Legal escalation for ambiguous interpretation or conflicting clauses.

### Step 11: Validate with Quality Frameworks
Run Citation Quality Gates, Self-Interrogation, and Confidence Scoring before delivery.

### Step 12: Deliver Obligation Package
Output register, alert queue, assumptions, unresolved issues, remediation plan, and
Glass Box audit trail.

---

## Deep Obligation Analysis Framework

### A. Obligation Record Specification

| Field | Required Content |
|---|---|
| Obligation ID | Stable unique ID (`CTR-<contract>-OBL-###`) |
| Contract Link | Contract identifier and artifact path |
| Clause Citation | Source section and excerpt anchor |
| Obligation Statement | Normalized imperative statement |
| Trigger Type | Date/event/recurrence/dependency |
| Trigger Anchor | Source event/date for computation |
| Due Logic | Exact timing rule |
| Owner | Primary + backup |
| Evidence Required | Proof artifact (invoice, certificate, notice copy, report) |
| Cure Logic | Cure period + consequences |
| Survival | Active after termination? yes/no |
| Confidence | Definite/High/Probable/Possible/Unlikely |

### B. Trigger Normalization Rules
- Preserve legal meaning; do not simplify away qualifiers.
- If clause uses ambiguous terms (`promptly`, `commercially reasonable`), keep original
  wording and attach interpretation note.
- Convert notice windows into explicit date math when anchor exists.
- Store both original clause and normalized rule for auditability.

### C. Renewal and Notice Logic
For renewal-related obligations, always derive:
- Renewal type: auto-renew/fixed-term/manual extension.
- Non-renewal notice window(s): earliest/latest valid send date.
- Permitted notice channels and recipients.
- Required content elements if specified.

Flag high-risk if any of the above are missing.

### D. Amendment and Supersession Handling
- Evaluate whether amendment replaces, modifies, or adds obligations.
- Maintain historical lineage with `effective_from` and `effective_to`.
- Never delete retired obligations; archive with status `SUPERSEDED`.

---

## Severity and Status Classification

Use both **Status** (current state) and **Severity** (impact if missed).

### Status
| Status | Meaning | Default Action |
|---|---|---|
| ON_TRACK | Due logic resolved, owner assigned, not near breach | Routine monitoring |
| WATCH | Due soon or dependency unresolved | Increase alert frequency |
| AT_RISK | Potential miss due to ambiguity/capacity/data gap | Owner + manager intervention |
| BREACHED | Deadline missed or obligation incomplete past due | Immediate remediation + escalation |
| SUPERSEDED | Replaced by amendment/new instrument | Archive with lineage |

### Severity
| Severity | Criteria | Required Escalation |
|---|---|---|
| LOW | Limited operational effect, no legal exposure | Team-level tracking |
| MEDIUM | Moderate operational/financial impact | Functional manager review |
| HIGH | Material legal, financial, or service impact | Legal + business owner escalation |
| CRITICAL | Regulatory breach risk, major liability, or strategic harm | Executive + legal immediate escalation |

---

## Actionable Output per Finding

For every `AT_RISK`, `BREACHED`, or `HIGH/CRITICAL` obligation provide:
- Why this matters (legal/commercial rationale).
- Exact remediation action.
- Owner and deadline.
- Required evidence artifact.
- Escalation path and fallback option.
- Residual risk if unresolved.

Example action format:
- `Issue`: Non-renewal notice window opens in 12 days; owner unassigned.
- `Action`: Assign owner today; prepare notice draft; verify delivery channel.
- `Deadline`: `YYYY-MM-DD` (latest safe send date minus internal approval buffer).
- `Escalation`: Legal ops lead at T-7 if owner remains unassigned.

---

## Prioritization Framework

| Tier | Label | Trigger | Execution Standard |
|---|---|---|---|
| Tier 1 | Must-Act Now | CRITICAL severity or BREACHED status | Same-day escalation and remediation plan |
| Tier 2 | Time-Bound Control | HIGH severity or WATCH/AT_RISK within 30 days | Managed action plan with weekly review |
| Tier 3 | Routine Governance | LOW/MEDIUM and ON_TRACK | Standard cadence monitoring |

Portfolio prioritization score:

`PriorityScore = (SeverityWeight * Impact) + (UrgencyWeight * TimeProximity) + (ConfidencePenalty)`

Default weights:
- `SeverityWeight = 0.5`
- `UrgencyWeight = 0.4`
- `ConfidencePenalty = 0.1`

---

## Citation Quality Gates

Run these gates before delivering obligation outputs.

| Gate | Rule | Fail Action |
|---|---|---|
| Source | Every obligation links to a clause citation | Mark `SOURCE_MISSING` and escalate |
| Format | Citation format is consistent and parseable | Normalize citation syntax |
| Currency | Latest amendment version is applied | Recompute with current effective text |
| Domain | Interpretation stays within governing-law scope | Add [JURISDICTION-SPECIFIC] note or [VERIFY] |
| Confidence | Uncertainty explicitly labeled | Downgrade confidence and add review task |

---

## Self-Interrogation (High-Risk Items)

For `HIGH`/`CRITICAL` obligations run three passes:

1. **Text Integrity Pass**
- Did extraction preserve legal qualifiers and conditions?
- Could a different clause interpretation change due logic?

2. **Completeness Pass**
- Are all dependencies captured (amendments, exhibits, notices section, definitions)?
- Is recipient/channel logic complete for notice obligations?

3. **Challenge Pass**
- What is the strongest argument that severity is overstated?
- What evidence would downgrade risk, and is it available?

If challenge succeeds, revise status/severity and explain the change.

---

## Confidence Scoring

| Level | Range | Meaning | Delivery Rule |
|---|---|---|---|
| Definite | 0.95-1.00 | Unambiguous clause + complete context | State directly |
| High | 0.80-0.94 | Strong extraction with minor assumptions | Include concise caveat |
| Probable | 0.60-0.79 | Reasonable but contestable | Include assumptions and alternatives |
| Possible | 0.40-0.59 | Material ambiguity or missing input | Require legal review task |
| Unlikely | 0.00-0.39 | Weak support or conflicting text | Do not finalize; escalate as unresolved |

---

## Glass Box Audit Trail (Template)

```yaml
glass_box:
  skill_name: "legalcode-obligation-tracker"
  contract_scope: "single | portfolio"
  governing_law: "[jurisdiction or unknown]"
  represented_side: "[customer/vendor/etc]"
  artifacts_ingested: "[count + list summary]"
  obligations_extracted: "[count]"
  unresolved_dates: "[count]"
  high_or_critical_count: "[count]"
  breached_count: "[count]"
  legalcode_mcp: "Connected | Not connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md or Not created"
  citation_gate_failures: "[count]"
  confidence_distribution:
    definite: "[n]"
    high: "[n]"
    probable: "[n]"
    possible: "[n]"
    unlikely: "[n]"
  assumptions:
    - "[assumption]"
  limitations:
    - "[missing schedule / missing amendment / ambiguous clause]"
  reviewer: "AI-assisted; qualified legal review required"
```

---

## Anti-Patterns (What Not to Do)

1. Track only expiration dates and ignore notice windows.
2. Ignore incorporated documents referenced by URL or schedule.
3. Assign obligations to individuals only (no role-based backup owner).
4. Convert ambiguous clauses into false precision without marking uncertainty.
5. Drop superseded obligations without retaining audit history.
6. Treat all obligations equally instead of risk-tiering.
7. Skip evidence requirements for "completed" obligations.
8. Fail to recalculate obligations after amendments/change orders.
9. Use a single reminder date for all obligations regardless of severity.
10. Treat governing law as irrelevant for notice validity.
11. Merge duplicate clauses without preserving provenance links.
12. Mark obligations complete based on intent rather than objective evidence.
13. Hide confidence levels and assumptions from stakeholders.
14. Deliver a register without explicit escalation owners and SLAs.
15. Ignore dependencies on third-party approvals, certifications, or system data.

---

## Writing Standards

Before delivery:
- Use plain language and operational verbs.
- Keep each obligation statement singular and testable.
- Separate interpretation notes from extracted clause content.
- Show computed dates and the formula used.
- Avoid absolute certainty unless confidence is Definite.
- Mark unverified enforceability statements as `[VERIFY]`.

Reject output that is:
- Missing source citations.
- Missing owner assignment for high/critical items.
- Missing remediation for breached obligations.

---

## External Tool Integration (legalcode-mcp)

When legalcode-mcp is connected:
- Verify jurisdiction-specific notice and renewal constraints.
- Confirm statutory/regulatory obligations linked to contract performance.
- Validate enforceability-sensitive interpretations in high-severity items.
- Mark validated items as `VERIFIED` in audit trail.

When legalcode-mcp is not connected:
- Continue with structural extraction and operational tracking.
- Mark enforceability-sensitive points as `[VERIFY]`.
- Record `legalcode_mcp: "Not connected"` in Glass Box.

---

## Multi-Stakeholder Mapping

Align outputs to stakeholder decisions:
- `Legal`: enforceability, notice validity, breach posture, and exception approval.
- `Procurement/Vendor Management`: renewal strategy, service performance, and supplier accountability.
- `Finance`: payment milestones, invoice dependencies, and financial exposure from missed obligations.
- `Security/Privacy`: incident clocks, certification duties, and data-handling obligations.
- `Business Owner`: operational readiness, delivery dependencies, and escalation ownership.

For each high/critical item, identify primary decision-maker and backup approver.

---

## Localization Notes

[JURISDICTION-SPECIFIC] Localize these controls before production rollout:
- Notice-window legality and delivery method requirements.
- Consumer vs. B2B applicability for auto-renewal constraints.
- Public-sector and regulated-industry overlays.
- Business-day and holiday calendar conventions for deadline math.
- Statutory retention requirements for completion evidence.

If any localization element is unresolved, keep item status at least `PARTIAL` and mark `[VERIFY]`.

---

## Output Format Template

```markdown
# Contract Obligation Tracker Output

## 1) Engagement Snapshot
- Contract ID:
- Counterparty:
- Represented Side:
- Governing Law:
- Review Mode: single | portfolio
- Artifacts Ingested:

## 2) Executive Summary
- Obligations Extracted: [n]
- High/Critical: [n]
- Breached: [n]
- Unresolved Dates: [n]
- Top 5 Immediate Actions:
  - [action]

## 3) Assumptions and Constraints
- [assumption]

## 4) Obligation Register
| Obligation ID | Clause Citation | Obligation | Owner | Trigger | Due Rule | Next Due Date | Status | Severity | Confidence | Evidence Required | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 5) Alert and Escalation Queue
| Priority Tier | Obligation ID | Reason | Action Owner | Deadline | Escalation Path |
|---|---|---|---|---|---|

## 6) Breach and Remediation Plan
| Obligation ID | Breach Detail | Remediation Steps | Residual Risk | Target Closure |
|---|---|---|---|---|

## 7) Renewal and Notice Calendar
| Contract | Renewal Type | Notice Window | Safe Send Date | Channel/Recipient | Status |
|---|---|---|---|---|---|

## 8) Unresolved Items Requiring Legal Review
- [item]

## 9) Quality and Confidence Summary
- Citation Gate Failures: [n]
- Confidence Distribution: Definite [n], High [n], Probable [n], Possible [n], Unlikely [n]

## 10) Glass Box Audit Trail
YAML payload:
`[glass_box yaml from the template above]`
```

## Provenance

Legalcode original, created from the high-value gap entry in `SKILL_CREATION_TASKS.md`
(`legalcode-obligation-tracker`, Use=9), then enhanced using:
- In-repo standards (`legalcode-contract-review`, `legalcode-contract-risk-scorer`).
- Parallel structural and prompt-quality analysis.
- Web-backed research via Perplexity and agent-browser source exploration.
