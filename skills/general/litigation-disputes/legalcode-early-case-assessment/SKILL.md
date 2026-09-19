---
name: legalcode-early-case-assessment
description: Run a litigation early case assessment (ECA) to evaluate merits, evidence strength, procedural
  leverage, expected spend, and settlement posture before major discovery spend. Use when legal teams
  need a defensible go/no-go recommendation, phase-based budget, risk-adjusted strategy branches, and
  executive-ready decision support for civil disputes across U.S., UK, AU, and other jurisdictions with
  localization markers.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Early Case Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted early case assessment in
> civil disputes. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Procedural
> and case-law statements may be incomplete or outdated; verify authoritative sources before
> relying on any conclusion.

## Purpose and Scope

Use this skill to produce a structured, defensible assessment of litigation position before
full-scale discovery or trial preparation spend.

This skill does:

- Build an evidence-grounded merits assessment for claims and defenses
- Classify risk and uncertainty across liability, damages, procedure, and enforcement
- Estimate budget, cycle time, and leverage by case phase
- Generate decision-ready strategy branches (litigate, settle, mixed)
- Provide a transparent audit trail for assumptions and legal sources

This skill does not:

- Replace jurisdiction-specific legal advice from licensed counsel
- Guarantee litigation outcomes
- Draft final pleadings, witness statements, or expert reports

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. Start by identifying governing law, forum, and
procedural regime, then localize all outcome-significant analysis.

[JURISDICTION-SPECIFIC] Always localize:

- Pleading sufficiency and early-disposition standards
- Disclosure/discovery scope and proportionality rules
- Evidence preservation/spoliation sanctions framework
- Pre-action obligations, ADR expectations, and cost-shifting rules
- Interim-relief standards and timing

Reference anchors frequently needed for ECA:

- U.S. federal: FRCP 16, 26, 37(e) [VERIFY]
- UK commercial: CPR, Pre-Action Conduct, PD 57AD, CPR Part 3 costs management [VERIFY]
- Australia federal: Federal Court Act 1976 (Cth) s 37M, Federal Court Rules 2011, CPN-1 [VERIFY]

## Interactive Clarification

Use interactive clarification whenever answers change risk classification or strategy.
If the user already provided the information, skip that question.

**CLARIFY block 1: Assessment objective**

- Options: `go/no-go decision`, `settlement posture`, `board update`, `budget control`, `full ECA`
- Why it matters: Controls depth, format, and prioritization.

**CLARIFY block 2: Side and role**

- Options: `claimant`, `defendant`, `respondent`, `third-party`, `mixed`
- Why it matters: Changes burden framing and procedural leverage.

**CLARIFY block 3: Time and spend constraints**

- Options: `urgent (<=7 days)`, `standard (2-4 weeks)`, `phased (30+ days)`
- Budget input: preferred cap or phase budget range.
- Why it matters: Determines acceptable uncertainty and scope.

**CLARIFY block 4: Risk appetite**

- Options: `conservative`, `balanced`, `aggressive`
- Why it matters: Changes settlement recommendations and escalation thresholds.

**CLARIFY block 5: Data readiness**

- Options: `high (organized corpus)`, `medium`, `low (fragmented/uncertain)`
- Why it matters: Drives confidence scoring and immediate remediation tasks.

## Workflow

### Step 1: Confirm Matter Frame

- Capture dispute type, procedural stage, forum, governing law, and strategic objective.
- Output: `matter frame` + `scope statement`.

### Step 2: Collect Core Inputs

- Gather pleadings/demand letters, key contracts/policies, chronology, and known evidence.
- Record missing critical inputs.
- Output: `input inventory` with quality status.

### Step 3: Build Issue-Element Map

- Map each claim and defense to legal elements and burden ownership.
- Associate each element with supporting and contradicting facts.
- Output: `element matrix` (supported / weak / missing).

### Step 4: Run Evidence Sufficiency Review

- Rate source reliability, admissibility risk, and contradiction risk.
- Identify documents, witnesses, and expert inputs required to close gaps.
- Output: `evidence sufficiency matrix`.

### Step 5: Evaluate Procedural Leverage

- Identify threshold motions, jurisdiction/venue issues, disclosure burden points,
  preservation risk, and timetable pressure points.
- Output: `procedural leverage map`.

### Step 6: Model Exposure and Recovery

- Build damages/exposure range (low/base/high) with assumptions and sensitivity drivers.
- Include legal spend, business disruption, regulatory/reputational spillover.
- Output: `exposure model`.

### Step 7: Assess Settlement Posture

- Estimate settlement corridor and BATNA/WATNA assumptions.
- Identify leverage events (motion decisions, disclosure milestones, expert deadlines).
- Output: `settlement scenario set`.

### Step 8: Classify Findings and Priorities

- Apply the risk classification and prioritization frameworks below.
- Convert each material finding into an assigned action owner and due date.
- Output: `risk register` + `action register`.

### Step 9: Quality-Assure Conclusions

- Apply Citation Quality Gates, Self-Interrogation, and Confidence Scoring.
- Flag every weakly supported conclusion as uncertain.
- Output: `QA log`.

### Step 10: Deliver Decision Pack

- Produce final report using the output template.
- Include strategy branches with explicit tradeoffs.
- Output: `ECA decision pack`.

## Deep ECA Analysis Framework

Evaluate all 12 domains unless explicitly scoped down.

| Domain                          | What to Assess                                | Evidence Signals                                         | Common Red Flags                           |
| ------------------------------- | --------------------------------------------- | -------------------------------------------------------- | ------------------------------------------ |
| 1. Claim viability              | Element-by-element strength                   | Contemporaneous documents, admissions, expert support    | Narrative only, no element coverage        |
| 2. Defense viability            | Legal/factual defenses and offsets            | Contract carveouts, statutory defenses, conduct evidence | Boilerplate defenses unsupported by facts  |
| 3. Counterclaim risk            | Potential counter-exposure                    | Reciprocal obligations, prior breach history             | Ignoring plausible counterclaims           |
| 4. Forum and procedure          | Venue, jurisdiction, track assignment         | Forum clauses, procedural posture, judicial guidance     | Wrong track assumptions                    |
| 5. Preservation posture         | Scope of hold and data integrity              | Hold notices, repository map, deletion controls          | Late/partial preservation                  |
| 6. Disclosure/discovery burden  | Cost and volume projections                   | Custodian count, systems map, document volume estimates  | Unbounded data requests                    |
| 7. Witness landscape            | Fact/expert witness quality                   | Consistency, credibility, availability                   | Key witness dependency                     |
| 8. Damages/exposure             | Liability magnitude and confidence            | Contracts, financial records, causal chain analysis      | Single-point estimates without sensitivity |
| 9. Insurance/indemnity recovery | Coverage and transfer options                 | Policy wording, notice, indemnity triggers               | Late notice, exclusions overlooked         |
| 10. Settlement leverage         | Negotiation timing and anchors                | Milestone events, opponent constraints                   | No BATNA/WATNA analysis                    |
| 11. Cost/timeline realism       | Phase budget and cycle assumptions            | Historical benchmarks, jurisdiction norms                | Optimistic schedules                       |
| 12. Business collateral impact  | Operational, regulatory, reputational effects | Regulatory triggers, key customer dependencies           | Narrow legal-only framing                  |

## Risk Classification (Litigation-Specific)

Classify each material finding as:

| Class      | Meaning                                                           | Typical Response                                        |
| ---------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| `LOW`      | Limited legal or business impact; manageable with routine action  | Track in normal cadence                                 |
| `MEDIUM`   | Material issue requiring tactical adjustment                      | Assign owner and near-term remediation                  |
| `HIGH`     | Significant impact on outcome, cost, or leverage                  | Escalate to matter lead; execute mitigation plan        |
| `CRITICAL` | Case-threatening issue or severe sanctions/irreversible loss risk | Immediate escalation and executive/counsel intervention |

## Actionable Output Per Finding

For each `MEDIUM/HIGH/CRITICAL` finding, provide:

- Finding summary (one sentence)
- Why it matters (legal + business impact)
- Evidence basis and citation status (`VERIFIED` or `[VERIFY]`)
- Recommended action (specific step)
- Owner role (legal, outside counsel, IT, finance, business lead)
- Due window (`24h`, `72h`, `7d`, `14d+`)
- Expected effect (risk reduction or leverage gain)

## Prioritization Framework

Use these tiers for implementation sequencing:

| Tier     | Label        | Criteria                                                                       | Deadline   |
| -------- | ------------ | ------------------------------------------------------------------------------ | ---------- |
| `Tier 1` | Immediate    | `CRITICAL` items, sanctions risk, limitation deadline risk, evidence loss risk | 0-72 hours |
| `Tier 2` | Near-term    | `HIGH` items likely to shift outcome, budget, or settlement corridor           | 3-14 days  |
| `Tier 3` | Programmatic | `MEDIUM/LOW` improvements and data-quality upgrades                            | 2+ weeks   |

## Citation Quality Gates

Before delivery, run these gates on every legal proposition:

| Gate       | Rule                                                            | Fail Action                        |
| ---------- | --------------------------------------------------------------- | ---------------------------------- |
| Source     | Link to authoritative rule/statute/case or mark `[VERIFY]`      | Add source or downgrade confidence |
| Format     | Use recognizable jurisdiction citation format                   | Normalize citation                 |
| Currency   | Check for amendments or superseding authority                   | Add `[CHECK CURRENCY]`             |
| Domain     | Keep analysis within selected jurisdiction and procedural track | Remove jurisdiction bleed          |
| Confidence | Align claim strength with evidentiary/legal support             | Reduce certainty and escalate      |

## Self-Interrogation (For HIGH/CRITICAL Findings)

Apply a three-pass challenge before finalizing:

1. **Legal Chain Integrity**

- Does conclusion follow from authority and facts, or from assumptions?

2. **Completeness Test**

- What contrary facts/authorities would alter the classification?

3. **Adversarial Challenge**

- What is the strongest opposing argument and when might it win?

If unresolved after pass 3, classify as uncertain and escalate.

## Confidence Scoring

| Level      | Range     | Interpretation                          | Action                            |
| ---------- | --------- | --------------------------------------- | --------------------------------- |
| `Definite` | 0.95-1.00 | Strong authority + strong evidence      | Present as primary conclusion     |
| `High`     | 0.80-0.94 | Strong support with minor uncertainties | Present with caveat               |
| `Probable` | 0.60-0.79 | Competing interpretations remain        | Present both sides                |
| `Possible` | 0.40-0.59 | Material uncertainty                    | Flag for counsel review           |
| `Unlikely` | 0.00-0.39 | Weak support/speculative                | Do not rely; gather more evidence |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-early-case-assessment"
  topic: "litigation early case assessment"
  jurisdiction: "[jurisdiction selected by user]"
  enhancement_type: "Legalcode original + enhancement"
  legalcode_mcp: "Not connected / Connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  source_skills_analyzed: "1 scaffold + legalcode reference standard"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  confidence: "HIGH | MEDIUM | LOW"
  key_assumptions:
    - "[assumption 1]"
    - "[assumption 2]"
  limitations:
    - "No legalcode-mcp connection in this run"
    - "Jurisdiction-specific case law requires counsel validation"
  reviewer: "AI-assisted; human legal review required"
```

## Anti-Patterns

Avoid these failure modes:

1. Starting with a recommendation before mapping element-level merits
2. Treating allegations as proven facts
3. Ignoring missing or contradictory evidence
4. Giving single-point damages estimates with no sensitivity range
5. Underestimating disclosure/discovery burden and timeline
6. Failing to model counterclaims and third-party claims
7. Ignoring preservation risk until after data loss events
8. Mixing jurisdictions without explicit localization
9. Treating settlement as binary instead of phased leverage strategy
10. Presenting high-certainty conclusions with weak authority
11. Omitting owner and due date for material actions
12. Hiding uncertainty instead of escalating it
13. Skipping insurer/indemnity recovery analysis where relevant
14. Producing legal-only recommendations without business impact context
15. Reusing stale procedural assumptions without currency check

## Writing Standards

- Use plain, direct language and verb-first instructions.
- Separate facts, assumptions, and legal conclusions.
- Quantify uncertainty; do not mask it.
- Avoid absolutist terms (`certain`, `guaranteed`) unless confidence is `Definite`.
- Prefer tables for risk/action output.
- Keep executive summary to decision-relevant points.

## External Tool Integration (legalcode-mcp)

When `legalcode-mcp` is available:

- Pull governing procedural rules and recent leading authorities for the selected forum.
- Validate high-severity findings against primary sources.
- Mark citations `VERIFIED` in the output.

When `legalcode-mcp` is not available:

- Continue with web and repository sources.
- Mark non-verified legal propositions with `[VERIFY]`.
- Explicitly state verification limitations in the audit trail.

## Output Format Template

````markdown
# Early Case Assessment — [Matter Name]

## 1. Executive Snapshot

- Objective:
- Side represented:
- Governing law/forum:
- Recommended strategy branch: `Litigate` / `Settle` / `Hybrid`
- Overall confidence: `[0.00-1.00 + label]`

## 2. Case Posture

- Procedural stage:
- Deadlines and timing constraints:
- Key assumptions:

## 3. Merits Matrix

| Issue | Burden Side | Evidence Strength | Risk Class | Confidence | Notes |
| ----- | ----------- | ----------------- | ---------- | ---------- | ----- |

## 4. Evidence and Data Gaps

| Gap | Impact | Required Action | Owner | Due |
| --- | ------ | --------------- | ----- | --- |

## 5. Procedural Leverage

- Potential threshold motions:
- Disclosure/discovery leverage points:
- Preservation/spoliation risk notes:

## 6. Exposure and Cost Model

- Damages/exposure range (low/base/high):
- Legal spend forecast by phase:
- Key sensitivity drivers:

## 7. Settlement Analysis

- BATNA:
- WATNA:
- Settlement corridor:
- Trigger events likely to move corridor:

## 8. Priority Action Register

| Tier | Action | Owner | Due | Expected Outcome |
| ---- | ------ | ----- | --- | ---------------- |

## 9. QA and Confidence

- Citation Quality Gates status:
- Self-Interrogation summary:
- Confidence rationale:

## 10. Glass Box Audit Trail

```yaml
[insert glass_box block]
```
````

```

## Provenance

Legalcode original skill created on 2026-02-28 and enhanced to Legalcode quality using:
- Initial in-repo scaffold (`legalcode-early-case-assessment`)
- Reference standard (`legalcode-contract-review`)
- Parallel enhancement analyses:
  - `/tmp/legalcode-eca-structural-analysis.md`
  - `/tmp/legalcode-eca-prompt-analysis.md`
- Web-backed research artifacts from Perplexity Sonar Pro Search:
  - `/tmp/legalcode-eca-research-us.json`
  - `/tmp/legalcode-eca-research-uk.json`
  - `/tmp/legalcode-eca-research-au.json`
- Curated legal research notes: `/tmp/legalcode-enhancement-research.md`
```
