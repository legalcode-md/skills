---
name: legalcode-contract-comparison
description: >
  Compare two contract versions or compare a contract against an approved template/playbook
  to detect textual and semantic legal changes, classify risk by clause family, and produce
  remediation-ready recommendations with fallback language and audit traceability. Use when
  reviewing counterparty markups, renewal amendments, template drift, procurement paper,
  M&A diligence batches, or any scenario requiring defensible contract delta analysis.
allowed-tools: Read, Bash(grep:*), Glob, WebSearch, WebFetch
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Contract Comparison

> **Disclaimer**: This skill provides a framework for AI-assisted contract comparison and
> risk triage. It does not constitute legal advice. All outputs must be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws,
> regulations, and market standards change; verify currency before relying on any legal
> assertion. If legal authority cannot be independently verified, mark it `[VERIFY]`.

## Purpose and Scope

Use this skill to compare:
- **Version-vs-Version**: two iterations of the same agreement.
- **Contract-vs-Template**: third-party paper against approved internal baseline.

Deliverables include:
- Clause-level and semantic-change analysis
- Risk classification (`GREEN / YELLOW / RED`)
- Materiality-ranked findings
- Suggested remediation + fallback language
- Executive summary + full audit trail

**Does:**
- Detect legal-effect drift, not only wording differences
- Separate cosmetic edits from material obligation shifts
- Map findings to negotiation and approval workflows

**Does not:**
- Replace full legal advice
- Guarantee enforceability outcomes
- Substitute for jurisdiction-specific counsel review

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default. Determine governing law from the document,
and localize where required.

Use `[JURISDICTION-SPECIFIC]` markers for:
- Liability-cap and exclusion enforceability limits
- Indemnity scope restrictions
- Data protection and transfer obligations
- Penalty/liquidated damages doctrine
- Forum/arbitration constraints
- Mandatory consumer/employment rules

If governing law is absent or conflicting, classify as `RED` and escalate.

## Interactive Clarification

Use **CLARIFY** prompts where answers change analysis direction.

Required CLARIFY set:
1. **Comparison mode**: `Version-vs-Version` or `Contract-vs-Template`
2. **Represented side**: `Customer/Buyer`, `Vendor/Supplier`, `Other`
3. **Risk posture**: `Conservative`, `Balanced`, `Commercial`
4. **Review depth**: `Full`, `Material-only`, `Priority clause families`
5. **Deadline**: `Urgent`, `Standard`, `Flexible`
6. **Baseline authority**: `Approved template vX`, `Playbook clause library`, `Counterparty precedent`, `Unknown`

If context is missing, proceed with explicit assumptions and log them in the audit trail.

## Workflow

### Step 1: Intake and Document Integrity
- Accept files/text/links.
- Confirm readability and completeness (schedules, exhibits, incorporated URLs).
- If partial content is detected, flag analysis scope limits.

### Step 2: CLARIFY Context
- Collect required CLARIFY inputs.
- Confirm represented side and risk tolerance before scoring.
- If baseline authority is unknown, ask whether to pause for baseline selection or continue with general market baseline.

### Step 3: Normalize Structure
- Align heading hierarchy, clause numbering, and defined-term indexes.
- Build a clause map keyed by logical family + section reference.
- Build a document-precedence map (for example: `Order Form > MSA > SOW > Policies`) and flag conflicts.

### Step 4: Execute Two-Layer Diff
- **Layer A: Text diff** (added/deleted/moved text).
- **Layer B: Semantic diff** (changed legal effect, burden, timeline, remedy, cap, trigger).

### Step 5: Classify Change Type
Assign each delta:
- `COSMETIC` (no legal/commercial effect)
- `CLARIFYING` (precision improvement)
- `RISK_INCREASE`
- `RISK_DECREASE`
- `AMBIGUITY_INTRODUCED`
- `OBLIGATION_SHIFT`

### Step 6: Map to Clause Families
Use this family map:
1. Limitation of liability
2. Indemnity
3. IP ownership/licensing
4. Data protection/security
5. Payment/commercial terms
6. Termination/renewal
7. Warranties/disclaimers
8. Governing law/dispute resolution
9. Assignment/change of control
10. Compliance obligations
11. Confidentiality
12. Boilerplate and interpretation controls

### Step 7: Risk Scoring and Severity
Score each material change on three dimensions (0-5):
- **Legal Exposure**
- **Business Impact**
- **Deviation from Preferred Position**

`RiskScore = round(((0.4*LegalExposure)+(0.35*BusinessImpact)+(0.25*Deviation))*20)`

Severity:
- `GREEN` (0-29): acceptable/no material increase
- `YELLOW` (30-59): material but negotiable
- `RED` (60-100): high risk/blocker or unresolved ambiguity

### Step 8: Generate Action Package per Finding
For every `YELLOW/RED` item produce:
- Issue summary
- Why it matters
- Primary remediation language
- Fallback language
- Negotiation note
- Escalation owner
- Confidence score

### Step 9: Prioritize and Sequence
Apply priority tiers:
- **Tier 1 (Must-Fix)**: RED or legal blocker
- **Tier 2 (Should-Fix)**: high YELLOW and recurring risk patterns
- **Tier 3 (Can-Trade)**: low YELLOW optimization items

### Step 10: Quality Controls and Delivery
Run Citation Quality Gates, Self-Interrogation, and Confidence rules, then render output template.

For portfolio/batch mode (3+ documents), also:
- Normalize findings by contract family before ranking.
- Prioritize by `risk_score x business_criticality`.
- Output top systemic drift patterns across the set.

## Deep Comparison Analysis Framework

| Dimension | What to Compare | Material Risk Signals |
|---|---|---|
| Obligations | Who must do what, by when | New absolute duties, tighter SLAs, removed cure rights |
| Remedies | Breach consequences | Expanded indemnity, unilateral termination, fee shifting |
| Economic Terms | Price, credits, caps | Uncapped liability, one-way credits, pricing ambiguity |
| Data/IP | Use, ownership, transfer | Broad data-use rights, IP assignment drift, weak security |
| Disputes | Venue, governing law, procedure | One-sided forum, mandatory arbitration shifts, class waivers |
| Durational Terms | Term, renewal, survival | Auto-renewal traps, shortened termination windows |
| Operational Controls | Notice, audit, reporting | Excessive audit reach, compressed notice deadlines |

## Precedence Conflict Protocol

When multiple documents govern the same deal (e.g., MSA, order form, SOW, policy URL):
1. Extract explicit precedence language from each document.
2. Resolve hierarchy conflicts; if unresolved, classify as `RED`.
3. If a lower-precedence document attempts to override a higher-precedence protection, flag `RISK_INCREASE`.
4. Route unresolved precedence disputes to legal escalation with proposed harmonizing language.

## Severity Classification

| Level | Meaning | Default Handling |
|---|---|---|
| GREEN | No meaningful risk increase | Log only |
| YELLOW | Material and negotiable | Propose primary + fallback fix |
| RED | High risk or uncertainty blocker | Escalate and hold approval pending disposition |

## Actionable Output Per Finding

Use this payload schema:
- `change_id`
- `section_reference`
- `change_type`
- `summary`
- `legal_effect_change`
- `severity`
- `risk_score`
- `recommended_primary_text`
- `recommended_fallback_text`
- `business_tradeoff_note`
- `escalation_trigger`
- `confidence`

## Prioritization Framework

| Tier | Label | Trigger | Action |
|---|---|---|---|
| Tier 1 | Must-Fix | RED or core risk transfer | Escalate immediately |
| Tier 2 | Should-Fix | High YELLOW | Negotiate strongly |
| Tier 3 | Can-Trade | Low YELLOW | Trade if needed for close |

## Multi-Stakeholder Mapping

| Stakeholder | Primary Concern | Required Output Slice |
|---|---|---|
| General Counsel / Legal | Enforceability and risk transfer | RED/YELLOW findings with authority/confidence tags |
| Business Owner | Deal velocity and commercial concessions | Tiered tradeoff summary + close-impact notes |
| Procurement | Operational obligations and SLA economics | Payment/SLA/termination deltas and fallback options |
| Security / Privacy | Data handling and incident obligations | Data/security clause deltas with remediation text |
| Finance | Exposure and payment leakage | Liability-cap economics + pricing/credit changes |

## Citation Quality Gates

Run silently before delivery:
1. **Source Gate**: each legal assertion has source type or `[VERIFY]`
2. **Format Gate**: citation format is consistent
3. **Currency Gate**: potentially outdated sources marked `[CHECK CURRENCY]`
4. **Domain Gate**: jurisdictional scope is explicit
5. **Confidence Gate**: uncertainty is disclosed

If any gate fails, revise output before finalizing.

## Self-Interrogation (For RED Findings)

Apply 3 passes to each RED item:
1. **Chain Integrity**: does severity logically follow from text + authority?
2. **Completeness**: did analysis account for balancing clauses elsewhere?
3. **Adversarial Challenge**: strongest downgrade argument and whether it holds.

If downgrade is justified, adjust severity and explain rationale.

## Confidence Scoring

| Level | Range | Meaning | Required Behavior |
|---|---|---|---|
| Definite | 0.95-1.00 | Clear authority + clear text impact | State directly |
| High | 0.80-0.94 | Strong support, minor uncertainty | Add caveat |
| Probable | 0.60-0.79 | Reasonable but contestable | Include counterview |
| Possible | 0.40-0.59 | Significant ambiguity | Flag for counsel review |
| Unlikely | 0.00-0.39 | Weakly supported | Do not assert as recommendation |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-contract-comparison"
  task_type: "contract comparison"
  comparison_mode: "Version-vs-Version | Contract-vs-Template"
  jurisdiction: "[Extracted governing law or Unknown]"
  represented_side: "[Customer/Vendor/Other]"
  risk_posture: "[Conservative/Balanced/Commercial]"
  source_documents_count: "[N]"
  sections_mapped: "[N]"
  changes_detected_total: "[N]"
  changes_by_type:
    cosmetic: "[N]"
    clarifying: "[N]"
    risk_increase: "[N]"
    risk_decrease: "[N]"
    ambiguity_introduced: "[N]"
    obligation_shift: "[N]"
  findings_by_severity:
    green: "[N]"
    yellow: "[N]"
    red: "[N]"
  priority_distribution:
    tier_1: "[N]"
    tier_2: "[N]"
    tier_3: "[N]"
  citations_verified: "[N]"
  citations_unverified: "[N]"
  external_tools_used: "legalcode-mcp/WebSearch/None"
  confidence_summary: "[Definite/High/Probable/Possible mix]"
  assumptions:
    - "[List explicit assumptions]"
  limitations:
    - "[List scope or evidence limitations]"
  reviewer: "AI-assisted; requires qualified legal review"
```

## Anti-Patterns (What Not To Do)

1. Treat textual diff as full legal analysis.
2. Ignore moved clauses that alter interpretation context.
3. Miss defined-term drift that changes obligations globally.
4. Downgrade unilateral risk transfer as merely stylistic.
5. Compare against wrong baseline template or outdated playbook.
6. Mix jurisdictions without marking `[JURISDICTION-SPECIFIC]`.
7. Skip schedules/exhibits incorporated by reference.
8. Ignore cross-clause interactions (e.g., indemnity + liability cap).
9. Present certainty without confidence qualifiers.
10. Deliver red flags without remediation options.
11. Escalate everything and collapse prioritization signal.
12. Fail to document assumptions and scope boundaries.

## Writing Standards

- Use plain, precise language.
- Distinguish observed text from inferred legal effect.
- Keep finding titles specific and non-generic.
- Avoid conclusory statements without rationale.
- Keep recommendations executable by legal/business stakeholders.

## Localization Notes

For jurisdiction-specific deployment:
- Replace `[JURISDICTION-SPECIFIC]` markers with verified local authority.
- Keep universal workflow logic unchanged; localize only legal-effect interpretation and remediation language.
- Add local citation format examples in the output template appendix.
- If authority cannot be verified for the jurisdiction, mark `[VERIFY]` and downgrade confidence.

## External Tool Integration

Preferred path:
- Use legalcode-mcp for jurisdiction-specific legal authority validation.
- Use web search for current standards and guidance updates.

If legalcode-mcp is unavailable:
- Continue structural comparison.
- Mark jurisdiction-bound legal assertions `[VERIFY]`.
- Record limitation in Glass Box trail.

## Output Format Template

~~~markdown
# Contract Comparison Report

## 1. Executive Summary
- Comparison mode:
- Governing law:
- Represented side:
- Overall risk posture:
- Materiality snapshot (GREEN/YELLOW/RED counts):
- Top 5 changes to resolve before approval:

## 2. Scope and Assumptions
- Documents compared:
- Missing sections / excluded artifacts:
- Assumptions:

## 3. Material Findings (Tiered)
### Tier 1 (Must-Fix)
| Change ID | Section | Summary | Severity | Risk Score | Primary Fix | Fallback | Confidence |
|---|---|---|---|---:|---|---|---|

### Tier 2 (Should-Fix)
| Change ID | Section | Summary | Severity | Risk Score | Primary Fix | Fallback | Confidence |
|---|---|---|---|---:|---|---|---|

### Tier 3 (Can-Trade)
| Change ID | Section | Summary | Severity | Risk Score | Suggested Position | Confidence |
|---|---|---|---|---:|---|---|

## 4. Full Change Log
| Change ID | Section | Change Type | Legal Effect Change | Severity | Risk Score |
|---|---|---|---|---|---:|

## 5. Clause Family Heatmap
| Clause Family | GREEN | YELLOW | RED | Notes |
|---|---:|---:|---:|---|

## 6. Open Questions / CLARIFY Follow-Ups
- [Question]

## 7. Escalation Routing
- Legal owner:
- Business owner:
- Security/Privacy owner:
- Approval hold triggers:

## 8. Decision Log
| Decision | Chosen Option | Why | Owner |
|---|---|---|---|

## 9. Unresolved Ambiguities
- [Ambiguity and why it blocks certainty]

## 10. Glass Box Audit Trail
    [Insert completed glass_box block in YAML format]
~~~

## Quality Verification Checklist

Before delivery, verify:
- 18/18 Legalcode quality elements present.
- Prompt score >= 35/40 or explain gap and remediation.
- All jurisdiction-bound claims are tagged `[JURISDICTION-SPECIFIC]` or `[VERIFY]`.
- Every RED finding includes primary + fallback language.
- Output includes Decision Log and Unresolved Ambiguities.

## Provenance

Legalcode original skill created 2026-02-28 from high-priority backlog item in
`SKILL_CREATION_TASKS.md`, scaffolded with legal-skill-creator workflow, then enhanced via
parallel structural + prompt-quality analysis aligned to Legalcode quality frameworks and
current external guidance references.
