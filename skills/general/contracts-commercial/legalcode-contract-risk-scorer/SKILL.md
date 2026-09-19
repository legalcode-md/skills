---
name: legalcode-contract-risk-scorer
description: Score contract risk clause-by-clause against organizational playbooks using a weighted model,
  classify results as GREEN/YELLOW/RED, and produce escalation-ready remediation guidance with confidence
  scoring and audit traceability. Use when reviewing vendor, customer, SaaS, procurement, licensing, partnership,
  and services agreements before approval or signature. Supports single-contract and portfolio scoring
  modes, jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Contract Risk Scorer

> **Disclaimer**: This skill provides a framework for AI-assisted contract risk scoring and
> prioritization. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws change;
> verify current applicability before relying on any provision described here.

## Purpose and Scope

Use this skill to assign defensible, repeatable risk scores to contracts by combining:

- Clause-level deviation analysis versus playbook standards.
- Weighted aggregation into a composite risk score.
- Severity classification (GREEN / YELLOW / RED).
- Action packages for negotiation, remediation, and escalation.

**Covers:**

- Playbook-based and general-standard scoring.
- Single-contract and portfolio scoring.
- Clause interactions (e.g., uncapped indemnity + weak liability cap mismatch).
- Confidence-scored outputs with traceable rationale.
- Escalation routing based on thresholds and materiality.

**Does not:**

- Replace legal counsel or delegated approval authority.
- Guarantee legal enforceability in any jurisdiction.
- Perform actuarial or financial-risk simulation.
- Draft full contracts from scratch.

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Determine governing law from the agreement and adapt
scoring assumptions accordingly.

[JURISDICTION-SPECIFIC] Localize and verify at minimum:

- Limits on exclusion/limitation of liability.
- Indemnity enforceability and public-policy carveouts.
- Data protection contract requirements.
- Mandatory consumer protections and unfair terms controls.
- Penalty/liquidated damages treatment.
- Forum selection and arbitration enforceability.

If governing law is missing, treat this as a material risk and escalate.

---

## Interactive Clarification

Use **CLARIFY** gates when an answer changes scoring outcomes or escalation.

Required context questions:

1. **Represented side**: customer/buyer, vendor/supplier, licensor/licensee, other.
2. **Contract type**: SaaS, MSA, procurement, license, partnership, employment, other.
3. **Risk appetite**: conservative, moderate, aggressive.
4. **Decision deadline**: urgent, standard, flexible.
5. **Scoring mode**: strict playbook, hybrid, market baseline.
6. **Focus areas** (optional): data/IP/liability/termination/payment/disputes.

If information is missing, continue with explicit assumptions and flag assumption risk.

---

## Workflow

### Step 1: Intake and Classification

- Accept contract via file, pasted text, or link.
- Identify contract family, parties, represented side, and governing law.
- Detect schedules/incorporated terms and include or flag exclusions.

### Step 2: Context Calibration

**CLARIFY** represented side, risk appetite, and scoring mode.

- Conservative: lower tolerance, escalate earlier.
- Moderate: balanced thresholds.
- Aggressive: escalate only material deviations.

### Step 3: Load Baseline Standards

- Prefer organizational playbook (preferred/fallback/walk-away positions).
- If no playbook exists, use market-baseline defaults and label results accordingly.

### Step 4: Build Legal-Authority Context

- If legalcode-mcp is available, gather governing-law authority for core enforceability dimensions.
- If unavailable, continue with structural scoring and mark legal assertions `[VERIFY]`.

### Step 5: Clause Extraction and Mapping

Map terms into the scoring taxonomy:

- Limitation of liability
- Indemnity
- Data protection/security
- IP ownership and licenses
- Confidentiality
- Payment/commercial terms
- Term/termination and renewal
- Warranty/disclaimer
- SLA/service credits
- Dispute resolution/governing law
- Assignment/change of control
- Compliance/sanctions/export/anti-bribery

### Step 6: Per-Clause Scoring

Score each clause using this model:

`ClauseScore_i = round(((0.45*Deviation) + (0.30*LegalExposure) + (0.25*BusinessImpact)) * 20)`

Where each input is 0-5:

- `Deviation`: distance from playbook preference.
- `LegalExposure`: enforceability/regulatory/litigation exposure.
- `BusinessImpact`: expected commercial or operational impact.

Output each clause score as 0-100.

### Step 7: Weighted Aggregation

Apply configurable weights (default below) and compute:

`CompositeScore = sum(ClauseScore_i * Weight_i) / sum(Weight_i)`

Default weights:

| Clause Group                       | Default Weight |
| ---------------------------------- | -------------: |
| Limitation of Liability            |             15 |
| Indemnity                          |             15 |
| Data Protection + Security         |             13 |
| IP Ownership + License Scope       |             12 |
| Termination + Renewal              |             10 |
| Payment + Commercials              |              8 |
| Warranty + Disclaimer              |              7 |
| Confidentiality                    |              6 |
| SLA / Service Credits              |              5 |
| Dispute Resolution + Governing Law |              5 |
| Assignment + Change of Control     |              2 |
| Compliance Clauses                 |              2 |

### Step 8: Cross-Clause Interaction Adjustments

Apply additive adjustments to avoid false comfort from averages:

- `+10` if uncapped indemnity + low/no liability cap.
- `+8` if strict data obligations without matching security commitments.
- `+6` if broad termination for convenience + heavy committed spend.
- `+5` if governing-law/venue mismatch increases enforcement friction.
- `+4` if assignment restrictions conflict with likely M&A path.

Cap final composite at 100.

### Step 9: Severity Classification and Escalation

- **GREEN (0-29)**: acceptable with routine review.
- **YELLOW (30-59)**: negotiate targeted changes; legal review required.
- **RED (60-79)**: significant exposure; senior legal escalation.
- **CRITICAL RED (80-100)**: hold signature pending executive/legal decision.

### Step 10: Actionable Remediation Package

For every material issue, provide:

- Deviation summary.
- Why it matters (legal + business).
- Proposed redline language.
- Fallback position(s).
- Escalation owner and target response time.

### Step 11: Quality Checks and Delivery

Run citation gates, self-interrogation, and confidence scoring before final output.

---

## Deep Topic Analysis

### Calibration by Contract Family

Adjust weights by agreement type:

- **SaaS/vendor**: increase data/security and SLA weights.
- **Licensing/IP-heavy**: increase IP and indemnity weights.
- **Procurement/supply**: increase delivery, SLA, and termination weights.
- **Strategic partnership**: increase governance, exclusivity, and change-of-control sensitivity.

### Portfolio Mode

When scoring many contracts:

- Normalize by contract family.
- Compare percentile ranking inside each family.
- Flag outliers where a clause score is >2 SD above family mean.
- Prioritize contracts with both high score and high business criticality.

### False-Positive Controls

- Do not auto-escalate minor textual deviations that preserve legal effect.
- Penalize ambiguity only when it changes exposure materially.
- Require explicit rationale for every YELLOW/RED classification.

---

## Severity Classification

| Level        | Score Range | Meaning                       | Required Action                             |
| ------------ | ----------- | ----------------------------- | ------------------------------------------- |
| GREEN        | 0-29        | Within tolerance              | Proceed with standard approval flow         |
| YELLOW       | 30-59       | Material but negotiable risk  | Negotiate targeted edits, legal review      |
| RED          | 60-79       | High risk                     | Senior counsel review, formal fallback plan |
| CRITICAL RED | 80-100      | Potentially unacceptable risk | Signature hold, exec/legal decision         |

---

## Prioritization Framework

| Tier   | Name                  | Trigger                          | Default Response                  |
| ------ | --------------------- | -------------------------------- | --------------------------------- |
| Tier 1 | Must-Have / Walk-Away | RED or CRITICAL RED              | Require fix or approved exception |
| Tier 2 | Should-Have           | High YELLOW or recurring pattern | Negotiate fallback language       |
| Tier 3 | Nice-to-Have          | Low YELLOW / GREEN optimization  | Accept if timeline-sensitive      |

---

## Citation Quality Gates

Run these 5 gates before delivery:

| Gate       | Rule                                                                   | Fail Action                       |
| ---------- | ---------------------------------------------------------------------- | --------------------------------- |
| Source     | Legal claims reference identifiable authority or are marked `[VERIFY]` | Add source or mark uncertainty    |
| Format     | Citation format is consistent for stated jurisdiction                  | Normalize format                  |
| Currency   | References checked for amendment/repeal where possible                 | Mark `[CHECK CURRENCY]`           |
| Domain     | Analysis matches stated governing-law scope                            | Remove jurisdictional bleed       |
| Confidence | Uncertainty is explicit, not implied certainty                         | Lower confidence, escalate review |

---

## Self-Interrogation (High Severity)

For each RED/CRITICAL RED issue, run 3 passes:

1. **Chain Integrity**: Does classification follow from text + authority?
2. **Completeness**: Are key countervailing clauses/facts considered?
3. **Challenge Test**: What is the strongest argument for downgrading severity?

If challenge is persuasive, revise score and explain why.

---

## Confidence Scoring

| Level    | Range     | Meaning                           | Delivery Rule               |
| -------- | --------- | --------------------------------- | --------------------------- |
| Definite | 0.95-1.00 | Strong text + authority support   | State directly              |
| High     | 0.80-0.94 | Strong support with minor caveats | Add concise caveat          |
| Probable | 0.60-0.79 | Reasonable but contestable        | Include counterarguments    |
| Possible | 0.40-0.59 | Significant uncertainty           | Flag for counsel review     |
| Unlikely | 0.00-0.39 | Weak support                      | Do not assert as conclusion |

---

## Glass Box Audit Trail (Template)

```yaml
glass_box:
  skill_name: "legalcode-contract-risk-scorer"
  contract_name: "[name or identifier]"
  contract_type: "[SaaS/MSA/license/etc]"
  governing_law: "[jurisdiction or unknown]"
  represented_side: "[customer/vendor/etc]"
  scoring_mode: "[playbook/hybrid/market]"
  risk_appetite: "[conservative/moderate/aggressive]"
  clause_count_scored: "[n]"
  composite_score: "[0-100]"
  severity: "[GREEN/YELLOW/RED/CRITICAL RED]"
  top_risk_drivers:
    - "[driver 1]"
    - "[driver 2]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[/tmp/legalcode-enhancement-research.md or Not created]"
  citations_verified: "[n verified] / [n unverified]"
  confidence: "[Definite/High/Probable/Possible/Unlikely]"
  limitations:
    - "[assumptions, missing schedules, missing governing law, etc.]"
  reviewer: "AI-assisted; qualified legal review required"
```

---

## Anti-Patterns (Do Not Do)

1. Treat averages as sufficient when a single clause is catastrophic.
2. Score without identifying represented side.
3. Apply one fixed weight model to every contract type.
4. Ignore cross-clause interactions.
5. Hide assumptions about missing annexes or incorporated terms.
6. Mark legal assertions as certain without verification.
7. Downgrade risk to meet business pressure without rationale.
8. Produce RAG labels without numeric traceability.
9. Escalate everything as RED (destroys triage value).
10. Treat market prevalence as legal validity.
11. Ignore survival clauses when assessing termination risk.
12. Miss auto-renewal windows in score impact.
13. Ignore change-of-control constraints in strategic deals.
14. Provide redlines without fallback positions.
15. Deliver output without confidence level and review caveat.

---

## Writing Standards

- Write in plain legal-operational language.
- State assumptions explicitly.
- Separate observed contract text from inferred risk.
- Tie every RED/CRITICAL RED to concrete remediation.
- Keep findings concise, decision-oriented, and auditable.

Delivery gate before final answer:

- No unexplained score jumps.
- No missing rationale for YELLOW+ findings.
- No unmarked legal uncertainty.

---

## External Tool Integration

Preferred:

- Use legalcode-mcp for governing-law validation and enforceability-sensitive issues.

Fallback:

- If legalcode-mcp is unavailable, continue scoring structurally and mark legal points `[VERIFY]`.
- Note fallback mode in Glass Box trail.

Optional research support:

- Use web-backed research for market practices and calibration benchmarks.
- Do not treat secondary web summaries as primary legal authority.

---

## Output Format Template

````markdown
# Contract Risk Scoring Report

## 1) Executive Summary

- Contract: [name]
- Type: [type]
- Represented side: [side]
- Governing law: [jurisdiction]
- Composite score: [0-100]
- Severity: [GREEN/YELLOW/RED/CRITICAL RED]
- Confidence: [level]

## 2) Scoring Configuration

- Scoring mode: [playbook/hybrid/market]
- Risk appetite: [conservative/moderate/aggressive]
- Weight profile: [default or customized]
- Key assumptions:
  - [...]

## 3) Clause-Level Scorecard

| Clause Group | Weight | Clause Score (0-100) | Weighted Contribution | Severity | Key Issue |
| ------------ | -----: | -------------------: | --------------------: | -------- | --------- |
| ...          |    ... |                  ... |                   ... | ...      | ...       |

## 4) Cross-Clause Adjustments

| Adjustment Trigger                      | Applied (Y/N) | Points | Rationale |
| --------------------------------------- | ------------- | -----: | --------- |
| Uncapped indemnity + weak liability cap |               |        |           |
| ...                                     |               |        |           |

## 5) Top Risk Drivers (Prioritized)

1. [Tier + issue + score impact]
2. [Tier + issue + score impact]
3. [Tier + issue + score impact]

## 6) Action Plan

| Priority Tier | Finding | Recommended Redline | Fallback Position | Owner | SLA |
| ------------- | ------- | ------------------- | ----------------- | ----- | --- |
| Tier 1        | ...     | ...                 | ...               | ...   | ... |

## 7) Escalation Decision

- Recommended path: [standard review / senior legal / executive hold]
- Reason: [...]

## 8) Verification Notes

- `[VERIFY]` items:
  - [...]
- `[CHECK CURRENCY]` items:
  - [...]

## 9) Glass Box Audit Trail

```yaml
[populate template]
```
````

---

## Provenance

Legalcode original (2026-02-28). Created from `SKILL_CREATION_TASKS.md` priority item
`legalcode-contract-risk-scorer` and enhanced using a two-track analysis workflow:

- Structural analysis: `/tmp/legalcode-contract-risk-scorer-structural-analysis.md`
- Prompt-quality analysis: `/tmp/legalcode-contract-risk-scorer-prompt-analysis.md`

Supplementary market-practice research performed via Perplexity Sonar Pro Search and saved
in `/tmp/perplexity-contract-risk-scoring.json`,
`/tmp/perplexity-contract-risk-calibration.json`, and
`/tmp/perplexity-high-risk-clauses.json`.
