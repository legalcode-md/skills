---
name: legalcode-breach-severity-assessment
description: Run multi-jurisdiction personal-data breach severity assessments for legal/privacy and incident-response
  teams. Use when triaging a security incident to decide whether it is notifiable, who must be notified,
  when clocks start, and how to produce a defensible regulator-ready and executive-ready decision package.
  Covers global incidents, parallel regulator duties, confidence-scored findings, and auditable timeline
  logic.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Breach Severity Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted legal/privacy incident
> analysis. It does not constitute legal advice. All outputs require review by qualified
> counsel in the relevant jurisdiction(s). Laws, regulator guidance, and timelines change.
> Any unverified legal statement must be marked `[VERIFY]` or `[CHECK CURRENCY]`.

## Purpose and Scope

Use this skill to produce a defensible breach-severity decision and notification action plan
for incidents involving personal data.

This skill does:

- Normalize incident facts and clock start dates.
- Assess harm likelihood and legal notification triggers across jurisdictions.
- Classify severity and required urgency.
- Produce finding-level remediation and evidence requirements.
- Generate an auditable decision package with confidence scoring.

This skill does not:

- Replace forensic root-cause analysis.
- Replace legal privilege strategy or litigation counsel.
- Promise regulatory outcome.
- Resolve sector-specific reporting regimes in full (telecom, finance, health, critical
  infrastructure) without explicit localization.

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic and must be localized per incident.

### Baseline authorities for global operations

| Jurisdiction                       | Baseline trigger/timing anchor                                                                                                                        | Source status |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| EU (GDPR)                          | Art. 33 authority notice within 72 hours where feasible once aware, unless unlikely risk; Art. 34 individual notice without undue delay for high risk | VERIFIED      |
| UK (UK GDPR)                       | Retained Art. 33/34 framework, with ICO as supervisory authority                                                                                      | VERIFIED      |
| Australia (Privacy Act Part IIIC)  | Assess suspected breach expeditiously and within 30 days; notify OAIC/individuals as soon as practicable after eligible-breach threshold              | VERIFIED      |
| Brazil (LGPD + ANPD Res. 15/2024)  | LGPD Art. 48 + Res. 15/2024 Art. 6/9 operational timeline in business days                                                                            | VERIFIED      |
| Singapore (PDPA + NDB Regulations) | Notifiability assessment and PDPC notification timing framework                                                                                       | [VERIFY]      |
| United States                      | State-specific laws; no single comprehensive federal personal-data breach statute                                                                     | [VERIFY]      |

[JURISDICTION-SPECIFIC] Always confirm current law, regulator guidance, and statutory clock
rules before issuing final advice.

## Interactive Clarification

Use **CLARIFY** blocks where answers materially change legal outcomes.

### CLARIFY packet (required before legal conclusions)

1. **Entity role**

- Options: Controller/Business, Processor/Service Provider, Joint Controllers, Unknown.
- Why it matters: Notification duties differ by role.

2. **Incident state**

- Options: Suspected, Confirmed technical event, Confirmed personal-data compromise,
  Ongoing/active.
- Why it matters: Determines whether legal clock starts on suspicion, awareness, or
  confirmation under local regime.

3. **Geographic footprint**

- Options: Single jurisdiction, Multi-jurisdiction, Unknown residency mix.
- Why it matters: May trigger parallel notifications and strictest-clock governance.

4. **Data profile**

- Options: Contact data only, Identity/government IDs, Financial, Health/sensitive,
  Children/vulnerable groups, Mixed/unknown.
- Why it matters: Harm likelihood and urgency thresholds change materially.

5. **Risk posture**

- Options: Conservative notify-early, Threshold-strict, Regulator-engagement-first.
- Why it matters: Resolves borderline risk classifications.

If answers are incomplete, proceed with explicit assumptions and mark dependencies
`[ASSUMPTION]`.

## Workflow

### Step 1: Intake and evidence freeze

Collect canonical incident facts:

- discovery timestamp(s)
- affected systems and data stores
- access/disclosure/loss mechanism
- containment status
- current confidence level

Output: `Incident Fact Sheet v1`.

### Step 2: Scope and role mapping

Map controller/processor relationships, vendors, and jointly-held data.

**CLARIFY** if controller identity or data ownership is disputed.

Output: `Role and Responsibility Map`.

### Step 3: Jurisdiction map and legal universe

Build affected-jurisdiction matrix using:

- entity establishment/operations
- data-subject location
- governing contractual commitments
- sector overlays

Output: `Jurisdiction Applicability Matrix`.

### Step 4: Trigger-date normalization

For each jurisdiction, determine legal “clock start” event:

- awareness of incident
- awareness of likely personal-data impact
- completion of statutory assessment window

Output: `Clock Normalization Table` with source citation per rule.

### Step 5: Harm and impact assessment

Score risk dimensions:

- identity theft/fraud risk
- physical or psychological harm risk
- discrimination or reputational harm risk
- rights-denial or service-interruption impact

Output: `Harm Vector Scorecard`.

### Step 6: Notification trigger test

Apply jurisdiction-specific trigger tests and classify each jurisdiction as:

- `NOTIFIABLE`
- `LIKELY_NOTIFIABLE`
- `NOT_NOTIFIABLE`
- `INSUFFICIENT_FACTS`

**CLARIFY** when material facts are missing and deadline impact is imminent.

Output: `Notification Duty Register`.

### Step 7: Cross-jurisdiction conflict resolution

When standards conflict, apply strictest-safe sequence:

1. Earliest defensible deadline.
2. Highest protective communication standard.
3. Most complete notice-content requirements.

Output: `Unified Action Clock`.

### Step 8: Remediation and communications package

For each material finding, define:

- legal basis
- action owner
- deadline
- evidence artifact
- fallback action

Output: `Finding Action Pack` + draft regulator/data-subject notice instructions.

### Step 9: Quality assurance and adversarial review

Run Citation Quality Gates, Self-Interrogation, and confidence scoring before final output.

Output: `QA Validation Log`.

### Step 10: Final delivery and monitoring triggers

Deliver final package and define reassessment triggers (new facts, new jurisdictions,
forensic updates, regulator feedback).

Output: `Final Breach Severity Assessment Report`.

## Deep Topic Analysis

### A. Harm Vector Model

| Vector           | Low signal                | High signal                                      |
| ---------------- | ------------------------- | ------------------------------------------------ |
| Data sensitivity | public/basic contact data | IDs, financial, health, children, credentials    |
| Exposure quality | encrypted/inaccessible    | plain text, exfiltrated, publicly exposed        |
| Actor capability | accidental limited access | malicious actor with reuse/fraud capability      |
| Affected scale   | minimal                   | mass impact or vulnerable cohorts                |
| Recoverability   | reversible quickly        | persistent compromise or irreversible disclosure |

### B. Trigger-date normalization logic

Use this deterministic order:

1. Record technical incident discovery time.
2. Record first evidence of personal-data involvement.
3. Record first legally supportable awareness point under each regime.
4. Record statutory assessment window end (if applicable).
5. Use earliest controlling legal deadline for global coordination.

### C. Multi-jurisdiction baseline matrix (starter)

| Jurisdiction | Trigger standard                                | Regulator timing                                                   | Individual timing                                                      |
| ------------ | ----------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| EU GDPR      | risk to rights/freedoms                         | within 72h where feasible (Art. 33)                                | without undue delay for high risk (Art. 34)                            |
| UK GDPR      | risk to rights/freedoms                         | within 72h where feasible (Art. 33 UK GDPR)                        | without undue delay for high risk (Art. 34 UK GDPR)                    |
| Australia    | likely serious harm + eligible breach framework | as soon as practicable after threshold met; 30-day assessment duty | as soon as practicable                                                 |
| Brazil       | incident may cause relevant risk or damage      | 3 business days under Res. 15/2024, subject to sector law          | 3 business days baseline under Res. 15/2024                            |
| Singapore    | notifiable breach framework under PDPA          | [VERIFY] use current PDPC timing guidance                          | [VERIFY] typically same sequence or immediately after authority notice |
| US states    | statute-specific                                | [VERIFY] state-by-state deadlines                                  | [VERIFY] state-by-state deadlines                                      |

### D. Evidence baseline for defensibility

Minimum artifacts:

- incident timeline (UTC + local)
- affected data schema snapshot
- forensic confidence note
- role allocation memo
- jurisdiction trigger analysis log
- notice-decision rationale memo
- approval and sign-off record

## Severity and Status Classification

Use this single taxonomy across all findings:

- `COMPLIANT`: No present notification duty or duty satisfied with adequate controls.
- `PARTIAL`: Plausible duty or documentation/control gaps; remediation required.
- `NON_COMPLIANT`: Clear legal duty not met or deadline at risk.
- `CRITICAL`: Ongoing or imminent high-harm exposure with urgent statutory action needed.

Escalation rules:

- Any `CRITICAL` finding triggers immediate legal lead + executive notification.
- Any `NON_COMPLIANT` deadline <24h triggers war-room coordination.

## Actionable Output per Finding

Each finding must include:

| Field             | Requirement                              |
| ----------------- | ---------------------------------------- |
| Finding ID        | Stable unique identifier                 |
| Jurisdiction      | Specific legal regime                    |
| Legal basis       | Article/section/regulatory provision     |
| Status            | COMPLIANT/PARTIAL/NON_COMPLIANT/CRITICAL |
| Clock trigger     | Date-time and rationale                  |
| Deadline          | Date-time + timezone + legal source      |
| Required action   | Concrete next action                     |
| Owner             | Named function/team                      |
| Evidence required | Artifact that proves completion          |
| Confidence        | Definite/High/Probable/Possible/Unlikely |
| Verification tag  | VERIFIED / [VERIFY] / [CHECK CURRENCY]   |

## Prioritization Framework

- `Priority 1 (Immediate)`: CRITICAL findings, missed or near-missed statutory deadlines.
- `Priority 2 (Urgent)`: NON_COMPLIANT findings with deadlines inside 72 hours.
- `Priority 3 (Planned)`: PARTIAL findings requiring control/documentation hardening.
- `Priority 4 (Monitor)`: COMPLIANT findings with reassessment triggers only.

## Citation Quality Gates

Silently pass all gates before delivery:

1. **Source Gate**: every legal claim references statute/regulator guidance or is marked
   `[VERIFY]`.
2. **Format Gate**: citations use consistent jurisdiction-aware format.
3. **Currency Gate**: recent amendment checks performed or marked `[CHECK CURRENCY]`.
4. **Domain Gate**: no jurisdiction-specific rule presented as universal.
5. **Confidence Gate**: uncertainty explicitly surfaced.

## Self-Interrogation (High-Severity Findings)

Apply to each `CRITICAL` or `NON_COMPLIANT` finding:

1. **Legal Chain Integrity**: Does the deadline/trigger conclusion directly follow from the
   cited authority?
2. **Completeness Challenge**: Could any exception/safe harbor change this conclusion?
3. **Adversarial Counterview**: What is the strongest argument against this severity and why
   is it rejected or accepted?

## Confidence Scoring

| Level    | Range     | Meaning                                  | Required action                               |
| -------- | --------- | ---------------------------------------- | --------------------------------------------- |
| Definite | 0.95-1.00 | settled rule + confirmed facts           | proceed with direct instruction               |
| High     | 0.80-0.94 | strong support, minor uncertainty        | proceed with concise caveat                   |
| Probable | 0.60-0.79 | likely correct, fact dependencies remain | provide alternatives + confirm facts          |
| Possible | 0.40-0.59 | material uncertainty                     | escalate to counsel before irreversible steps |
| Unlikely | 0.00-0.39 | insufficient basis                       | do not assert as conclusion                   |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-breach-severity-assessment"
  topic: "multi-jurisdiction personal-data breach severity and notification triage"
  jurisdiction: "Jurisdiction-agnostic"
  source_skills_analyzed: 5
  enhancement_type: "Upgrade"
  legalcode_mcp: "Not connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  agent_analysis_files:
    - "/tmp/legalcode-breach-severity-structural-analysis.md"
    - "/tmp/legalcode-breach-severity-prompt-analysis.md"
  quality_target: "35+/40 prompt score"
  completeness_target: "18/18 required elements"
  citations_verified: "Track per run"
  confidence: "MEDIUM-HIGH pending jurisdiction updates"
  limitations:
    - "US state-law matrix intentionally high-level unless localized"
    - "Singapore section-level extraction marked [VERIFY] in this environment"
  reviewer: "AI-assisted; qualified legal review required"
```

## Anti-Patterns

1. Treating technical detection time as legal awareness without jurisdiction analysis.
2. Applying one jurisdiction’s deadline globally without conflict mapping.
3. Ignoring processor-to-controller notice duties.
4. Assuming “no exfiltration proof” means no notifiable risk.
5. Omitting timezone normalization in deadline calculations.
6. Failing to document why a breach was classified as non-notifiable.
7. Not reassessing classification when forensic facts change.
8. Treating regulator guidance as binding statute without labeling.
9. Using severity labels without actionable owner/deadline/evidence fields.
10. Sending broad public notices before mandatory direct notices where feasible.
11. Failing to preserve privilege strategy and decision logs.
12. Presenting `[VERIFY]` items as settled conclusions.
13. Assuming US law is uniform across states.
14. Copying prior incident outcomes without re-running trigger tests.

## Writing Standards

Before delivery:

- Prefer plain language, short sentences, and explicit verbs.
- Separate facts, assumptions, and legal conclusions.
- Put deadlines in ISO timestamp plus local timezone.
- Avoid speculative language unless tagged with confidence and verification state.
- Keep jurisdiction-specific conclusions in their own table rows.

## External Tool Integration

Preferred research source: legalcode-mcp (when available).

With legalcode-mcp connected:

- Pull statute text, regulator guidance, and recent updates per jurisdiction.
- Mark citations `VERIFIED`.

Without legalcode-mcp:

- Use official regulator/statute pages where accessible.
- Mark unverifiable points `[VERIFY]`.
- Record gap in Glass Box output.

## Output Format Template

````markdown
# Breach Severity Assessment Report

## 1) Executive Outcome

- Incident ID:
- Global severity:
- Go/No-go notification posture:
- Immediate Priority 1 actions:

## 2) Incident Facts

- Discovery timeline:
- Affected systems/data:
- Confirmed vs. unconfirmed facts:
- Assumptions:

## 3) Jurisdiction Applicability Matrix

| Jurisdiction | Applicable | Role | Trigger rule | Verification |
| ------------ | ---------- | ---- | ------------ | ------------ |

## 4) Notification Duty Register

| Finding ID | Jurisdiction | Legal basis | Status | Clock trigger | Deadline | Required action | Owner | Confidence | Verification |
| ---------- | ------------ | ----------- | ------ | ------------- | -------- | --------------- | ----- | ---------- | ------------ |

## 5) Conflict Resolution Summary

- Earliest deadline selected:
- Strictest communication standard selected:
- Rationale:

## 6) Priority Action Plan

- Priority 1:
- Priority 2:
- Priority 3:
- Priority 4:

## 7) Draft Notice Requirements

- Regulator notice content checklist:
- Data-subject notice content checklist:
- Pending evidence before dispatch:

## 8) QA and Confidence

- Citation Quality Gates status:
- Self-Interrogation outcomes:
- Confidence distribution:

## 9) Glass Box Audit Trail

```yaml
[Insert glass_box block]
```

## 10) Open Items

- [VERIFY] items:
- [CHECK CURRENCY] items:
- Reassessment trigger events:
````

## Provenance

- Created as Legalcode original scaffold on 2026-02-28 from `SKILL_CREATION_TASKS.md`
  item 95.
- Enhanced on 2026-02-28 using the legalcode-skill-enhancement workflow with:
  - structural analysis: `/tmp/legalcode-breach-severity-structural-analysis.md`
  - prompt analysis: `/tmp/legalcode-breach-severity-prompt-analysis.md`
  - legal research notes: `/tmp/legalcode-enhancement-research.md`
- Primary reference anchors consulted:
  - EU GDPR text (EUR-Lex)
  - UK GDPR retained Article 33 text (legislation.gov.uk)
  - OAIC NDB guide + Privacy Act Part IIIC references
  - ANPD incident communication guidance + Resolution 15/2024 references
  - PDPC breach-reporting resources `[VERIFY]` where section extraction was unavailable
