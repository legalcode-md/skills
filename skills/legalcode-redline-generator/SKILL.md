---
name: legalcode-redline-generator
description: >
  Generate negotiation-ready contract redlines with primary and fallback language,
  playbook alignment, risk-tiered priorities, and auditable rationale for each edit.
  Use when reviewing third-party paper, preparing response markups, or standardizing
  first-pass legal edits across procurement, sales, and legal teams. Supports Word
  track-changes workflows and clause-by-clause redline strategy under jurisdiction-
  agnostic guidance with localization markers.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Redline Generator

> **Disclaimer**: This skill provides a framework for AI-assisted contract redline
> generation. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws and
> market norms evolve; verify current applicability before relying on any legal proposition.

## Purpose and Scope

Generate high-quality, negotiation-ready redlines that are:
- aligned to organizational playbook positions (or clearly labeled market defaults),
- prioritized by legal and commercial impact,
- paired with fallback language and escalation guidance,
- traceable through a structured audit trail.

**Covers:**
- first-pass and response-pass redlining for commercial agreements,
- per-clause issue detection and replacement text,
- negotiation rationale for legal + business stakeholders,
- priority-based redline packaging (must-have vs tradeable).

**Does not:**
- replace full legal opinion or jurisdiction-specific advice,
- finalize signatures or execute agreements,
- guarantee enforceability in any jurisdiction without local counsel review.

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default. Determine governing law from the contract
before proposing jurisdiction-sensitive language.

Use `[JURISDICTION-SPECIFIC]` markers for:
- liability-cap enforceability limits,
- indemnity scope and anti-indemnity restrictions,
- liquidated damages vs penalty doctrine,
- data transfer and processor obligations,
- forum/arbitration constraints,
- mandatory consumer or employment protections.

If governing law is unclear, flag as a RED issue and require user confirmation.

## Interactive Clarification

Use **CLARIFY** checkpoints whenever answers materially change draft language, risk rating,
or concession strategy.

At minimum, collect:
1. Side represented: `Customer / Vendor / Licensor / Licensee / Other`
2. Contract type: `MSA / SaaS / Services / Procurement / Other`
3. Leverage profile: `High / Balanced / Low`
4. Deadline: `Urgent / Standard / Flexible`
5. Risk posture: `Conservative / Balanced / Commercially pragmatic`
6. Redline package preference: `All findings / Top material findings only`

If the user omits context, proceed with explicit assumptions.

## Workflow

### Step 1: Intake Draft and Baseline
- Accept source as `.docx`, pasted text, or extracted text.
- Identify whether this is:
  - `First-pass markup` (counterparty template), or
  - `Response markup` (counterparty already redlined your form).
- Normalize clause numbering and heading map.

### Step 2: CLARIFY Deal Context
Ask required context questions from the Interactive Clarification section.
Capture any hard constraints (e.g., non-negotiable deal terms, revenue dependency, board pressure).

### Step 3: Load Playbook Positions
- Look for organization playbook references (e.g., `legal.local.md`, clause library docs).
- If unavailable, state: `Using general market standards (not org-approved playbook).`

**CLARIFY** if no playbook:
- Build minimum playbook now,
- Continue with default market positions,
- Continue and collect preferences issue-by-issue.

### Step 4: Identify Clause Universe
Map clauses into core redline families:
1. Limitation of liability
2. Indemnities
3. IP ownership and licensing
4. Data privacy and security
5. Payment and pricing mechanics
6. Term, termination, suspension
7. Warranties and disclaimers
8. Governing law, venue, dispute resolution
9. Assignment/change of control
10. Compliance (sanctions, anti-corruption, export)

### Step 5: Detect Deviations and Gaps
For each family, identify:
- adverse language,
- missing protections,
- internal inconsistencies,
- hidden dependencies between clauses.

### Step 6: Classify Severity
Assign each finding as `GREEN / YELLOW / RED` using the framework below.

### Step 7: Draft Primary and Fallback Redlines
For each YELLOW/RED item, produce:
- clean replacement text,
- fallback position,
- rationale,
- business impact,
- likely counterparty pushback.

### Step 8: Build Negotiation Sequence
Group edits into negotiation tiers:
- Tier 1 (must-have),
- Tier 2 (should-have),
- Tier 3 (tradeables).

Sequence asks to maximize close probability while preserving core protections.

### Step 9: Run Quality Controls
Apply Citation Quality Gates, Self-Interrogation, and Confidence Scoring.

### Step 10: Produce Deliverables
Output:
- redline findings table,
- markup-ready language blocks,
- negotiation brief for internal stakeholders,
- escalation list for unresolved RED issues.

## Deep Redline Analysis Framework

Use this table to structure findings.

| Clause Family | What to Test | Common Red Flags | Redline Output Requirement |
|---|---|---|---|
| Limitation of Liability | Cap basis, carve-outs, symmetry | uncapped exposure, asymmetry, broad carve-outs | cap formula + mutuality fallback |
| Indemnity | trigger scope, defense/control, exclusions | one-way indemnity, duty-to-defend without control | narrowed trigger + control-of-defense language |
| IP | ownership of deliverables, residual rights, license-back | blanket assignment, no customer license, broad residuals | ownership clarity + use-rights fallback |
| Data/Security | controller/processor roles, breach timing, subprocessors | undefined roles, weak security standard, no notice SLA | role-specific obligations + notice timeline |
| Payment | net terms, disputes, auto-increase, currency/tax | short payment window, unilateral fee rise | payment flexibility + dispute-safe harbor |
| Termination | convenience rights, cure periods, transition duties | vendor lock-in, no exit support, immediate termination rights | balanced termination + wind-down fallback |
| Warranties | scope, duration, exclusive remedies | sweeping disclaimers, no performance warranty | minimum service assurance + remedy clarity |
| Disputes | law/venue/arbitration, injunctive relief, fee shifting | one-sided venue, jury waiver surprises | neutral forum + staged dispute escalation |
| Assignment | consent standards, affiliate transfers, change of control | unrestricted assignment to competitor | consent-protective transfer language |
| Compliance | sanctions, anti-bribery, export, audit rights | vague obligations, unilateral audit overreach | risk-based compliance + bounded audit terms |

## Severity Classification

| Level | Meaning | Default Action |
|---|---|---|
| **GREEN** | Acceptable or low-impact variance | Note only; optional polish edits |
| **YELLOW** | Material but negotiable risk | Propose redline + fallback |
| **RED** | High exposure, legal/commercial blocker, or unresolved ambiguity | Escalate + propose primary/fallback + walk-away position |

## Actionable Output Per Finding

For every YELLOW or RED finding, provide this exact payload:
- **Issue**: concise problem statement
- **Why it matters**: legal + business risk in one paragraph
- **Proposed redline (primary)**: insertion-ready text
- **Fallback redline**: second-best position preserving core protection
- **Counterparty likely response**: probable objection
- **Negotiation answer**: concise rebuttal/compromise path
- **Priority tier**: Tier 1 / 2 / 3
- **Escalation trigger**: when internal approval is required

## Prioritization Framework

| Tier | Label | Use Rule | Examples |
|---|---|---|---|
| **Tier 1** | Must-Have | Non-negotiable risk controls | uncapped liability, IP grab, missing data security obligations |
| **Tier 2** | Should-Have | Strong preference; acceptable fallback exists | liability carve-out narrowing, termination mechanics |
| **Tier 3** | Tradeable | Useful optimizations with low downside | notice method refinement, formatting or boilerplate cleanup |

## Multi-Stakeholder Mapping

Map outputs to decision owners before sending a redline package:

| Stakeholder | What They Need | Delivery Style |
|---|---|---|
| Legal counsel | legal risk basis, enforceability concerns, escalation rationale | clause-level precision with assumptions explicit |
| Sales / revenue owner | close risk, concession sequence, commercial alternatives | short risk-impact bullets + fallback sequence |
| Procurement | price/term levers, vendor obligations, operational protections | matrix view of asks vs concessions |
| Security / privacy | control obligations, incident timelines, audit rights | requirement-level checklist |
| Finance | payment, credits, liability cap economics | quantified exposure and downside scenarios |
| Executive approver | Tier 1 blockers and go/no-go summary | one-page decision brief |

If stakeholders disagree, prioritize Tier 1 legal-risk controls and explicitly log unresolved trade-offs.

## Citation Quality Gates

Run silently before outputting legal assertions:
1. **Source Gate**: legal assertions must identify source type (statute/case/principle/playbook).
2. **Format Gate**: citation format is consistent and readable.
3. **Currency Gate**: outdated authority is flagged `[CHECK CURRENCY]`.
4. **Domain Gate**: jurisdiction-specific claims are marked `[JURISDICTION-SPECIFIC]`.
5. **Confidence Gate**: uncertain claims are marked `[VERIFY]` or downgraded in confidence.

If a gate fails, revise before delivery.

## Self-Interrogation (For RED Items)

Run a 3-pass challenge on every RED classification:

**Pass 1 — Legal Chain Integrity**
- Does the risk conclusion follow from contract language and known legal principles?

**Pass 2 — Commercial Proportionality**
- Is the proposed edit commercially realistic for this leverage profile?

**Pass 3 — Adversarial Challenge**
- What is the strongest counterargument and what fallback still protects core risk?

## Confidence Scoring

| Level | Range | Interpretation | Required Behavior |
|---|---|---|---|
| **Definite** | 0.95-1.00 | settled principle and clear drafting logic | state directly |
| **High** | 0.80-0.94 | strong support, minor uncertainty | state with short caveat |
| **Probable** | 0.60-0.79 | reasonable but contestable | include rationale + fallback |
| **Possible** | 0.40-0.59 | uncertain posture | mark `[VERIFY]`, recommend counsel check |
| **Unlikely** | 0.00-0.39 | weakly supported | do not assert as recommendation |

## Glass Box Audit Trail

Include this YAML block in deliverables:

```yaml
glass_box:
  skill_name: "legalcode-redline-generator"
  task_type: "contract redline generation"
  governing_law: "[Extracted law or Unknown]"
  jurisdiction_mode: "Jurisdiction-agnostic with markers"
  source_contract_type: "[MSA/SaaS/etc.]"
  playbook_basis: "[Org playbook / General market standards]"
  leverage_profile: "[High/Balanced/Low]"
  findings_total: "[N]"
  findings_by_severity:
    green: "[N]"
    yellow: "[N]"
    red: "[N]"
  redlines_generated: "[N]"
  fallback_pairs_generated: "[N]"
  citations_verified: "[N]"
  citations_unverified: "[N]"
  confidence_summary: "[Definite/High/Probable/Possible mix]"
  external_tools_used: "None (manual) / legalcode-mcp / other"
  legalcode_mcp: "Not connected / Connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  reviewer_note: "AI-assisted output; qualified legal review required"
```

## Anti-Patterns (Do Not Do)

1. Redlining without identifying which side you represent.
2. Returning only deletions with no alternative language.
3. Treating every issue as RED (signal inflation).
4. Ignoring clause interdependence (e.g., indemnity vs LoL).
5. Proposing impossible positions for low-leverage deals.
6. Using jurisdiction-specific assertions as universal rules.
7. Skipping version-control protocol and change-tracking discipline.
8. Writing negotiation rationale that is adversarial instead of persuasive.
9. Omitting escalation triggers for true blocker issues.
10. Leaving undefined terms inside proposed replacement text.
11. Referencing unverified law without `[VERIFY]`.
12. Failing to provide fallback language for YELLOW findings.

## Writing Standards

- Write in plain legal English with short, actionable sentences.
- Prefer concrete language over abstract warnings.
- Keep per-finding rationale under 120 words unless RED.
- Avoid rhetorical commentary; focus on decision support.
- Use consistent terminology for severity and priority tiers.

Pre-delivery checks:
- all YELLOW/RED findings include primary + fallback text,
- no unresolved placeholders in final language,
- escalation list is complete and non-duplicative.

## External Tool Integration

Preferred:
- legalcode-mcp for statutes/case-law validation by governing law.

Fallback when unavailable:
- proceed with structural/legal-principle analysis,
- mark uncertain legal claims `[VERIFY]`,
- keep recommendations conservative on jurisdiction-dependent issues.

## Localization Notes

When localizing for a specific governing law:
- replace generic assumptions with jurisdiction-verified wording,
- keep any unresolved legal proposition marked `[VERIFY]`,
- document any mandatory overrides that supersede playbook defaults,
- state where local counsel confirmation is required before sending markup externally.

[JURISDICTION-SPECIFIC] Localize at minimum for:
- liability cap carve-out enforceability,
- indemnity and defense-control constraints,
- data protection transfer/processor duties,
- dispute forum and interim-relief availability.

## Output Format Template

~~~markdown
# Redline Package — [Agreement Name]

## 1. Context Snapshot
- Side represented:
- Contract type:
- Governing law:
- Leverage profile:
- Risk posture:
- Review basis: [Playbook / Market standard]

## 2. Executive Summary
- Total findings: [N]
- RED: [N] | YELLOW: [N] | GREEN: [N]
- Tier 1 asks: [N]
- Deal blockers requiring escalation: [N]

## 3. Redline Findings Table
| # | Clause | Severity | Priority | Issue | Primary Redline | Fallback | Rationale | Confidence |
|---|---|---|---|---|---|---|---|---|

## 4. Negotiation Sequence
### Tier 1 — Must-Haves
- [Issue + ask + fallback + escalation trigger]

### Tier 2 — Should-Haves
- [Issue + ask + fallback]

### Tier 3 — Tradeables
- [Issue + optional ask]

## 5. Escalation Queue
- [RED item]
- Decision needed:
- Impact if accepted/rejected:
- Deadline:

## 6. Open Verification Items
- [JURISDICTION-SPECIFIC or legal reference marked VERIFY]

## 7. Glass Box Audit Trail
```yaml
[Insert completed glass_box block]
```
~~~

## Provenance

Created by Legalcode on 2026-02-28 from a new high-value skill task in
`SKILL_CREATION_TASKS.md`, then enhanced using repository reference patterns,
parallel structural/prompt analysis, and web-backed research notes in
`/tmp/legalcode-enhancement-research.md`.
