---
name: legalcode-dpia-generator
description: >
  Build and review Data Protection Impact Assessments (DPIAs) for high-risk processing
  under GDPR/UK GDPR and aligned privacy regimes. Use when launching new products,
  AI features, profiling, surveillance, large-scale special-category processing, or new
  cross-border data uses that may materially impact individuals' rights and freedoms.
  Produces a defensible trigger decision, risk register, mitigation plan, prior-consultation
  recommendation, and executive-ready approval package.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode DPIA Generator

> **Disclaimer**: This skill provides a framework for AI-assisted legal/privacy analysis.
> It does not constitute legal advice. All outputs should be reviewed by qualified counsel
> or privacy professionals licensed or operating in the relevant jurisdiction before use.
> Laws, regulator guidance, and enforcement posture change; verify currency before relying
> on any legal conclusion.

## Purpose and Scope

Use this skill to generate a complete DPIA package for planned processing that may create
high risk to individuals' rights and freedoms.

This skill does:
- Decide whether a DPIA is required.
- Produce structured necessity/proportionality analysis.
- Build inherent/residual risk scoring with mitigation controls.
- Determine whether prior consultation is required.
- Generate approval-ready outputs for legal, privacy, security, and product stakeholders.

This skill does not:
- Replace legal sign-off from qualified counsel.
- Guarantee regulatory approval.
- Convert unresolved high residual risk into automatic go-live clearance.

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic with EU/UK default framing.

Primary references:
- GDPR Article 35 (DPIA trigger and content)
- GDPR Article 36 (prior consultation)
- UK GDPR Articles 35/36 and ICO guidance

[JURISDICTION-SPECIFIC] Before final output, localize:
- Mandatory trigger lists issued by the competent supervisory authority.
- Sector-specific rules (health, children, biometrics, finance, employment, public sector).
- Cross-border transfer restrictions and consultation expectations.
- Any national derogations that alter GDPR baseline mechanics.

## Interactive Clarification

Use **CLARIFY** prompts when answers materially change the outcome. Do not proceed on
assumptions if risk classification depends on missing facts.

CLARIFY topics:
1. Processing objective and launch deadline.
2. Data sensitivity (special-category, children, vulnerable groups, location, biometrics).
3. Automation profile (scoring, ranking, significant effects decisions).
4. Scale and geography (data volume, user count, jurisdictions, cross-border flows).
5. Risk appetite and escalation threshold (conservative vs pragmatic).

## Workflow

### Step 1: Intake and Scope Lock

Collect:
- Processing purpose and user/business objective.
- Controller/processor roles and accountable owner.
- Data lifecycle map (collect, transform, share, retain, delete).
- Systems/vendors involved.
- Intended go-live date.

**CLARIFY** if any of these are unclear:
- Is this a new processing activity or a material change to existing processing?
- Is production deployment imminent or exploratory only?

### Step 2: DPIA Trigger Screening

Assess whether the activity is likely high risk.

Minimum trigger checks:
- Systematic/profiling decisions with legal or similarly significant effects.
- Large-scale processing of special-category or criminal-offence data.
- Large-scale systematic monitoring of publicly accessible areas.
- Novel technology use with uncertain privacy harm profile.
- Combination of multiple high-risk indicators from supervisory guidance.

Decision outputs:
- `DPIA_REQUIRED`
- `DPIA_NOT_REQUIRED_WITH_RATIONALE`
- `INSUFFICIENT_FACTS`

**CLARIFY** if there is disagreement on scale, novelty, or effect severity.

### Step 3: Processing and Data-Flow Mapping

Document:
- Data categories and data-subject categories.
- Processing operations and purposes.
- Storage/transfer locations.
- Internal and external recipients.
- Retention/deletion mechanics.

Output: canonical data-flow summary usable across legal, security, and engineering review.

### Step 4: Necessity and Proportionality Analysis

Test each processing objective against:
- Lawful basis suitability.
- Purpose limitation.
- Data minimization.
- Retention proportionality.
- Access and transparency controls.
- Availability of less intrusive alternatives.

Fail conditions:
- Objective can be met with materially less intrusive data use.
- High-sensitivity data is used without clear necessity.
- Retention is open-ended without legal justification.

### Step 5: Rights-and-Freedoms Risk Identification

Build a risk universe across at least:
- Confidentiality harms (unauthorized access/disclosure).
- Integrity harms (incorrect data causing adverse decisions).
- Availability harms (loss/inaccessibility affecting rights exercise).
- Fairness harms (discriminatory profiling, opaque automation).
- Chilling effects (surveillance perception, behavior suppression).
- Downstream harms (secondary use beyond expectation).

### Step 6: Risk Scoring and Classification

Score each risk using inherent and residual dimensions.

Use this severity model:
- `COMPLIANT`: controls are sufficient; residual risk low.
- `PARTIAL`: meaningful gaps remain; remediation required pre-launch.
- `NON_COMPLIANT`: material GDPR/UK GDPR deficits; launch blocked until fixed.
- `CRITICAL`: unacceptable residual risk likely requiring consultation or processing redesign.

### Step 7: Mitigation and Remediation Design

For every `PARTIAL`, `NON_COMPLIANT`, or `CRITICAL` item, define:
- Control action (technical/organizational/contractual/process).
- Owner.
- Due date.
- Evidence artifact required for closure.
- Fallback if control fails.

### Step 8: Prior Consultation Decision

Evaluate whether residual high risk remains after planned mitigations.

Decision outputs:
- `CONSULT_SUPERVISORY_AUTHORITY_REQUIRED`
- `CONSULTATION_NOT_REQUIRED`
- `CONSULTATION_RECOMMENDED_PENDING_COUNSEL`

Reference points:
- GDPR Article 36 / UK GDPR equivalent.
- Local supervisory authority list/guidance where applicable.

### Step 9: Stakeholder Review and Approval Pack

Prepare role-specific summary for:
- Legal/privacy.
- Security.
- Engineering/product.
- Executive approver.

Include explicit go/no-go recommendation and conditions precedent.

### Step 10: Final Delivery and Monitoring Hooks

Deliver final DPIA package plus post-launch checkpoints:
- Reassessment triggers (scope change, new data source, model change, transfer change).
- Control verification cadence.
- Incident-response linkage.

## Deep Topic Analysis Framework

### A. Trigger Matrix

| Trigger Family | Indicator | Typical DPIA Outcome |
|---|---|---|
| Automated decisioning | Profiling with significant effect | Usually required |
| Sensitive data | Special-category/criminal large-scale use | Usually required |
| Surveillance | Systematic monitoring in public/semi-public contexts | Usually required |
| Novelty | New technology with uncertain impact | Often required |
| Aggregation | Combining multiple datasets for inference | Often required |
| Vulnerability | Children/employees/patients or power imbalance | Often required |

### B. Necessity-Proportionality Stress Test

For each processing purpose, force answers to:
- Why this data, not less?
- Why this retention period, not shorter?
- Why this model/logic, not less intrusive logic?
- What rights can be impacted, and how are those impacts reduced?

### C. Control Catalog Baseline

Minimum control domains to evaluate:
- Identity/access control and least privilege.
- Encryption/tokenization/pseudonymization.
- Logging and monitoring.
- Secure development and change control.
- Vendor/subprocessor governance.
- Data-subject-rights operations.
- Breach response and notification readiness.

## Actionable Output per Finding

Every finding must include:
- Finding ID.
- Legal/control basis.
- Severity state.
- Business impact if unresolved.
- Remediation action.
- Owner and deadline.
- Evidence required.
- Escalation path.

## Prioritization Framework

Use these implementation priorities:
- `Priority 1 (Must Before Launch)`: any `CRITICAL` or `NON_COMPLIANT` finding.
- `Priority 2 (Must in Fixed Window)`: `PARTIAL` findings with medium/high impact.
- `Priority 3 (Continuous Improvement)`: low-impact hardening tasks.

## Citation Quality Gates

Before final delivery, silently pass all five gates:
1. `Source`: each legal claim maps to statute/regulator guidance or is marked `[VERIFY]`.
2. `Format`: citations use consistent jurisdiction-aware format.
3. `Currency`: confirm no known supersession/repeal; otherwise mark `[CHECK CURRENCY]`.
4. `Domain`: avoid mixing jurisdiction-specific rules as universal.
5. `Confidence`: uncertainty is explicit, never implied certainty.

## Self-Interrogation (High-Severity Items)

For every `CRITICAL` or `NON_COMPLIANT` item, run 3 passes:
1. `Legal chain`: does conclusion logically follow from cited authority?
2. `Completeness`: were alternatives, safeguards, and exceptions fully considered?
3. `Adversarial challenge`: strongest argument against this severity; does it hold?

If challenge succeeds, downgrade with rationale; if not, keep severity and escalate.

## Confidence Scoring

| Level | Range | Meaning | Required Action |
|---|---|---|---|
| Definite | 0.95-1.00 | settled rule + confirmed facts | proceed with clear recommendation |
| High | 0.80-0.94 | strong support, minor uncertainty | proceed with concise caveat |
| Probable | 0.60-0.79 | meaningful ambiguity | include alternate interpretation + review note |
| Possible | 0.40-0.59 | significant uncertainty | escalate for legal review before approval |
| Unlikely | 0.00-0.39 | weak basis | do not rely; mark `[UNCERTAIN]` |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-dpia-generator"
  topic: "Data Protection Impact Assessment"
  jurisdiction: "Jurisdiction-agnostic (EU/UK defaults)"
  source_skills_analyzed: "5 + reference standard"
  enhancement_type: "Upgrade + synthesis"
  legalcode_mcp: "Not connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  quality_score: "37/40"
  completeness: "18/18 elements"
  citations_verified: "Primary authority URLs captured; local-law specifics may require [VERIFY]"
  confidence: "HIGH — based on GDPR/ICO/EDPB/CNIL primary guidance plus repository patterns"
  limitations:
    - "Not a substitute for jurisdiction-specific legal advice"
    - "Sector-specific national rules must be localized"
  reviewer: "AI-assisted — requires qualified legal/privacy review"
```

## Anti-Patterns (Do Not Do)

1. Treating DPIA as a post-launch checkbox.
2. Declaring "no high risk" without evidence.
3. Reusing stale DPIA templates without project-specific facts.
4. Ignoring changes in model logic or data sources after approval.
5. Confusing security risk-only assessment with rights-and-freedoms assessment.
6. Omitting vendor/subprocessor data flows from scope.
7. Failing to test less intrusive alternatives.
8. Leaving high-risk items without owner/deadline/evidence.
9. Treating anonymization claims as fact without technical validation.
10. Hiding uncertainty instead of using `[VERIFY]` / `[CHECK CURRENCY]`.
11. Mixing EU and UK transfer assumptions without explicit legal basis.
12. Closing mitigations based on policy statements only, no implementation evidence.
13. Ignoring vulnerable-group impacts (children, employees, patients).
14. Skipping prior-consultation analysis when residual high risk remains.
15. Approving go-live when legal/privacy/security sign-off conditions are unmet.

## Writing Standards

Before final delivery:
- Use plain language and define acronyms once.
- Separate facts, assumptions, and recommendations.
- Keep every conclusion traceable to evidence or citation.
- Prefer specific remediation instructions over abstract guidance.
- Mark uncertain legal points with `[VERIFY]`.

## External Tool Integration

Preferred: use `legalcode-mcp` to validate jurisdiction-specific statutory and case-law references.

With `legalcode-mcp`:
- Pull applicable local trigger lists and consultation requirements.
- Record verified citations in the audit trail.

Without `legalcode-mcp`:
- Proceed with repository + web primary sources.
- Mark non-verified local references with `[VERIFY]`.
- State limitation explicitly in Glass Box.

## Output Format Template

```markdown
# DPIA Assessment — [Project Name]

## 1. Executive Summary
- DPIA requirement decision: [Required / Not Required / Insufficient Facts]
- Prior consultation decision: [Required / Not Required / Recommended]
- Go-live recommendation: [Go / Conditional Go / No-Go]
- Top risk themes: [...]

## 2. Processing Overview
- Controller/processor roles:
- Processing purpose(s):
- Data categories:
- Data subject categories:
- Systems/vendors:
- Cross-border transfers:
- Retention/deletion:

## 3. Trigger Assessment (Art. 35)
| Trigger | Evidence | Outcome |
|---|---|---|

## 4. Necessity and Proportionality
| Test | Finding | Status |
|---|---|---|

## 5. Risk Register
| ID | Risk Description | Inherent Risk | Residual Risk | Severity |
|---|---|---|---|---|

## 6. Remediation Plan
| Risk ID | Action | Owner | Due Date | Evidence Required | Priority |
|---|---|---|---|---|---|

## 7. Prior Consultation Analysis (Art. 36)
- Residual high-risk rationale:
- Consultation recommendation:
- Required submission materials:

## 8. Decision and Conditions
- Approval status:
- Conditions precedent:
- Reassessment triggers:

## 9. Confidence and Verification Notes
- Confidence score:
- [VERIFY] items:
- [CHECK CURRENCY] items:

## 10. Glass Box Audit Trail
```yaml
[insert completed glass_box block]
```
```

## Provenance

Legalcode original (2026-02-28). Created from high-priority uncreated item in
`SKILL_CREATION_TASKS.md` and enhanced using:
- Repository analysis of existing compliance/privacy skills.
- Reference quality pattern from `legalcode-contract-review`.
- Primary-source research notes in `/tmp/legalcode-enhancement-research.md`
  (EUR-Lex GDPR text, EDPB endorsed WP29 materials, ICO DPIA guidance, CNIL DPIA guidance,
  EDPS necessity/proportionality toolkit).
