---
name: legalcode-contract-playbook-builder
description: >
  Build and continuously improve organization-specific contract negotiation playbooks with
  approved clause positions, fallback ladders, escalation triggers, approval matrices, and
  KPI instrumentation. Use when legal, procurement, sales, or commercial teams need a
  governed system for reviewing and negotiating NDAs, MSAs, SaaS agreements, procurement
  terms, partner agreements, and other commercial contracts at scale. Supports green/yellow/
  red/black positioning, clause-library governance, and auditable decision trails.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Contract Playbook Builder

> **Disclaimer**: This skill provides a framework for AI-assisted contract governance and
> negotiation playbook design. It does not constitute legal advice. All outputs must be
> reviewed by qualified legal professionals licensed in the relevant jurisdiction before
> implementation. Laws and regulatory expectations change; verify current applicability of
> every legal claim before relying on it.

## Purpose and Scope

Build, validate, and maintain an operational contract playbook that legal and business
teams can execute consistently.

**Covers:**
- Playbook design for recurring commercial agreements (NDA, MSA, SaaS, procurement, partner)
- Clause-level position ladders (preferred, fallback, escalation, walk-away)
- Approval routing by risk, value, data sensitivity, and jurisdiction
- Governance controls (versioning, ownership, exception logging, review cadence)
- KPI instrumentation (cycle time, fallback acceptance, escalation, deviation trends)
- Auditability via Glass Box trace

**Does not:**
- Replace qualified legal review for jurisdiction-specific enforceability
- Draft a complete negotiated contract from zero (use drafting skills for that)
- Provide client-specific legal advice
- Guarantee acceptance by counterparties

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default and must localize any enforceability-sensitive
playbook rule.

Use **[JURISDICTION-SPECIFIC]** markers where local law may alter:
- Limitation-of-liability enforceability
- Indemnity structure and anti-indemnity limits
- Liquidated damages / penalty-clause treatment
- Data processing and transfer obligations
- Consumer-protection and unfair-terms rules
- Employment/IP ownership defaults and assignment formalities

When legal authority is not verified, mark as **[VERIFY]** and downgrade confidence.

## Interactive Clarification

Use structured clarification at decision points that materially change playbook output.

Ask before proceeding when:
- Risk tolerance is unknown
- Contract families differ in material ways
- Approval authority is unclear
- Jurisdiction mix is broad or conflicting
- KPI success criteria are undefined

If user input is partial, proceed with explicit assumptions and state each assumption in
"Assumptions and Constraints".

## Workflow

### Step 1: Accept Inputs

Accept any combination of:
- Existing playbook (if available)
- Standard templates and historical redlines
- Approval/signatory matrix or delegation policy
- Matter metadata (contract type, value, region, business owner)
- Post-signature data (exceptions, renewal outcomes, disputes, claims)

If no artifacts are provided, proceed with a baseline framework and mark all organization-
specific terms as placeholders.

### Step 2: Gather Operating Context

**CLARIFY**:
1. Primary objective
   - Options: Faster cycle time, tighter risk control, delegation to business teams, all three
2. Contract families in scope
   - Options: NDA only, NDA+MSA, full commercial portfolio
3. Tolerance profile
   - Options: Conservative, balanced, growth-oriented
4. Implementation channel
   - Options: CLM-integrated, spreadsheet/manual, phased migration
5. Decision rights
   - Options: Central legal, distributed legal + business, executive-gated

Record these as hard constraints for all downstream decisions.

### Step 3: Build Corpus and Pattern Map

Normalize source contracts and redlines into a comparable structure:
- Clause family
- Original position
- Counterparty ask
- Accepted fallback
- Escalation path
- Final disposition

Produce a "Negotiation Pattern Map" showing high-friction clauses and recurrent concessions.

### Step 4: Define Clause Taxonomy and Risk Axes

Create a standard taxonomy across contract families.

Minimum clause families:
- Definitions and interpretation
- Scope and service levels
- Fees and payment
- Term and termination
- Limitation of liability
- Indemnification
- IP ownership and licenses
- Confidentiality
- Data protection and security
- Audit and compliance
- Subcontracting/assignment/change of control
- Dispute resolution and governing law

Define risk axes for each family:
- Financial exposure
- Regulatory exposure
- Operational continuity
- Data/IP exposure
- Litigation/enforcement exposure

### Step 5: Draft Position Ladders (Core)

For each clause family, define four levels:
- **GREEN (Standard)**: Preferred language; can be accepted without escalation.
- **YELLOW (Conditional)**: Acceptable with conditions and documented rationale.
- **RED (Escalate)**: Not accepted without legal leadership approval.
- **BLACK (Walk-away/Prohibited)**: Unacceptable under current policy.

Each position must include:
- Business rationale
- Legal rationale ([JURISDICTION-SPECIFIC] + [VERIFY] as needed)
- Example language
- Fallback sequence
- Required approver(s)

### Step 6: Build Approval Matrix and Escalation Rules

Map approval routing using all factors, not value alone:
- Contract family
- Deal value band
- Data classification (public/internal/confidential/restricted)
- Jurisdiction risk profile
- Deviations from GREEN baseline

Define SLA by tier:
- Tier 1 (GREEN-only): <= 1 business day
- Tier 2 (YELLOW present, no RED/BLACK): <= 3 business days
- Tier 3 (RED/BLACK present): <= 5-7 business days with named escalation owner

### Step 7: Integrate Clause Library Governance

For each clause entry, store metadata:
- Clause ID
- Owner
- Effective date
- Last legal validation date
- Jurisdiction coverage
- Retirement trigger
- Related policy references

Require versioned change logs and explicit reason codes for every modification.

### Step 8: Run Legal/Regulatory Validation

Use legalcode-mcp when available to verify enforceability-sensitive rules for prioritized
jurisdictions.

Research targets:
- Liability cap limits and carve-out constraints
- Indemnity enforceability and statutory constraints
- Data/privacy obligations affecting contractual minimums
- Mandatory clause obligations by sector
- Choice-of-law and dispute forum constraints

If legalcode-mcp is unavailable:
- Continue with structure-first design
- Mark enforceability-sensitive items **[VERIFY]**
- Flag output as requiring legal validation before operational rollout

### Step 9: Stress-Test with Scenario Simulation

Simulate at least five scenarios:
- Enterprise procurement with strict data processing terms
- High-value MSA with broad indemnity ask
- Cross-border SaaS deal with transfer restrictions
- Small recurring deal where speed outweighs negotiation depth
- Renewal negotiation with legacy unfavorable terms

For each scenario, test:
- Routing correctness
- Position consistency
- Escalation trigger accuracy
- SLA feasibility

### Step 10: Publish Playbook Package

Publish all artifacts together:
- Playbook master table
- Approval matrix
- Escalation runbook
- Clause library metadata table
- KPI dashboard definition
- Governance calendar

### Step 11: Operate and Improve

Run monthly KPI review + quarterly playbook governance review.

Required governance checks:
- Drift from GREEN baseline
- Escalation bottlenecks
- Recurring exception patterns
- Jurisdiction updates requiring clause changes
- Decommission outdated fallback language

## Deep Clause Playbook Analysis Framework

Use this framework for each clause family.

| Field | Required Content |
|---|---|
| Business intent | What objective this clause protects |
| Legal constraint | Mandatory or likely enforceability limits [JURISDICTION-SPECIFIC] [VERIFY] |
| GREEN position | Preferred language and threshold |
| YELLOW fallbacks | Ordered fallback alternatives with conditions |
| RED triggers | Conditions requiring legal escalation |
| BLACK triggers | Absolute no-go criteria |
| Counterparty signals | Common asks and why they appear |
| Negotiation rationale | Why fallback is acceptable or not |
| KPI hooks | Metrics affected (cycle time, leakage, risk score, dispute likelihood) |

## Position Status Classification

Apply this status model to each clause decision.

| Status | Meaning | Required Action |
|---|---|---|
| GREEN | Approved baseline | Auto-approve if no conflicting signals |
| YELLOW | Conditional fallback | Require rationale + approved fallback ID |
| RED | Material risk deviation | Escalate to legal lead and record decision memo |
| BLACK | Prohibited/walk-away | Reject or renegotiate before signature |

## Actionable Output Per Finding

For every RED/BLACK or repeated YELLOW pattern, output:
- Finding ID
- Clause family
- Current position vs target position
- Risk impact (financial/regulatory/operational)
- Recommended remediation language
- Owner
- Deadline
- Escalation path if unresolved

## Prioritization Framework

| Priority Tier | Definition | Response Window | Typical Examples |
|---|---|---|---|
| Tier 1 (Must Fix) | BLACK or unresolved RED with major exposure | Immediate | Unlimited liability, prohibited data transfer model |
| Tier 2 (Should Fix) | Material YELLOW/RED patterns causing repeated friction | Current cycle | Chronic fallback misuse, missing escalation owner |
| Tier 3 (Optimize) | Quality improvements with lower immediate risk | Next governance cycle | Metadata cleanup, KPI enrichment |

## Multi-Stakeholder Mapping

Map recommendations across primary decision groups to avoid single-function bias.

| Stakeholder | Primary Concern | Typical Red-Line Sensitivity | Decision Role |
|---|---|---|---|
| Legal | Enforceability, liability, precedent setting | Liability caps, indemnity carve-outs, dispute forum | Policy owner and final escalation authority |
| Procurement | Commercial terms, supplier leverage, cycle speed | Pricing mechanics, renewal controls, service credits | Negotiation lead for buy-side deals |
| Sales/Commercial | Revenue velocity, customer acceptance | Limitation language, termination rights, SLA commitments | Negotiation lead for sell-side deals |
| Security/Privacy | Data handling and breach exposure | DPA terms, security controls, audit rights, subprocessors | Mandatory approver for data-sensitive deals |
| Finance | Exposure, payment certainty, margin protection | Payment terms, tax allocation, credits/penalties | Financial risk approver |
| Executive Sponsor | Strategic alignment and risk appetite | Non-standard RED/BLACK exceptions | Final override authority |

## Localization Notes

Localize the playbook before production use in any jurisdiction mix above one legal system.

- Keep global baseline language in GREEN/YELLOW ladders.
- Convert enforceability-sensitive rules to jurisdiction variants with `[JURISDICTION-SPECIFIC]`.
- Maintain a jurisdiction override register tied to clause IDs and validation dates.
- Mark unverified legal assertions with `[VERIFY]` and block auto-approval for those entries.
- Revalidate local legal assumptions at least annually or on major regulatory change.

## Citation Quality Gates

Run these gates silently before final delivery.

| Gate | Rule | Fail Action |
|---|---|---|
| Source | Every legal claim cites statute/regulation/case or is marked [VERIFY] | Add citation or mark [VERIFY] |
| Format | Citations use recognizable jurisdiction format | Normalize format |
| Currency | Authority is still current | Add [CHECK CURRENCY] |
| Domain | Claim matches specified jurisdiction scope | Remove jurisdiction bleed |
| Confidence | Uncertainty is explicit | Downgrade confidence + add caveat |

## Self-Interrogation (High-Risk Items)

Apply for RED and BLACK outcomes.

**Pass 1 — Chain Integrity**
- Does classification follow from actual legal/commercial constraints?

**Pass 2 — Completeness**
- Are we missing a plausible fallback that preserves risk controls?

**Pass 3 — Challenge Test**
- What is the strongest argument for relaxing this position?
- Under what conditions could that be acceptable?

## Confidence Scoring

| Level | Range | Meaning | Required Communication |
|---|---|---|---|
| Definite | 0.95-1.00 | Strong authority + repeated internal validation | State directly |
| High | 0.80-0.94 | Strong support with minor caveats | State with short caveat |
| Probable | 0.60-0.79 | Reasonable basis with competing interpretations | Explain alternatives |
| Possible | 0.40-0.59 | Significant uncertainty | Mark for counsel review |
| Unlikely | 0.00-0.39 | Weak basis | Do not operationalize; mark [UNCERTAIN] |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-contract-playbook-builder"
  topic: "Contract playbook creation and governance"
  jurisdiction: "Jurisdiction-agnostic"
  enhancement_type: "Legalcode original synthesis + enhancement"
  legalcode_mcp: "Not connected / Connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  source_skills_analyzed: "3"
  citations_verified: "[N VERIFIED] / [N VERIFY]"
  confidence: "HIGH / MEDIUM / LOW"
  assumptions:
    - "[Assumption 1]"
  limitations:
    - "[Limitation 1]"
  reviewer: "AI-assisted; legal review required"
```

## Anti-Patterns (Do Not Do)

1. Treating value-only thresholds as approval logic while ignoring data sensitivity.
2. Allowing fallback clauses without rationale or reason code.
3. Embedding jurisdiction-specific legal claims in a global baseline without markers.
4. Using unlimited fallback options that create negotiator paralysis.
5. Storing playbook clauses without owner/version/effective-date metadata.
6. Allowing ad hoc exceptions without central logging.
7. Keeping BLACK positions undefined and relying on subjective judgment.
8. Measuring cycle time only while ignoring risk leakage and exception growth.
9. Failing to retire outdated fallback language after law/regulatory changes.
10. Treating template language as policy without validating against real negotiation outcomes.
11. Escalating too late (post-commercial commitment) because triggers are vague.
12. Designing playbooks for legal only instead of legal + business execution.
13. Copying competitor/law-firm sample language without organizational fit analysis.
14. Ignoring renewal negotiations where legacy concessions persist silently.
15. Publishing the playbook without training, SLA ownership, or governance cadence.

## Writing Standards

Before finalizing output:
- Use plain language and define jargon once.
- Keep each finding atomic and actionable.
- Avoid contradictory guidance across clause families.
- Separate facts, assumptions, and recommendations clearly.
- Mark unknowns explicitly with [VERIFY], [CHECK CURRENCY], or [UNCERTAIN].

## External Tool Integration

Use legalcode-mcp for jurisdiction verification when available.

Recommended sequence:
1. Identify top jurisdictions by contract volume and risk.
2. Query enforceability topics per clause family.
3. Record verified sources in an authority file.
4. Update playbook status from [VERIFY] to verified only after check.

Graceful degradation when unavailable:
- Continue governance design
- Keep enforceability notes marked [VERIFY]
- Require human legal validation before deployment

## Output Format Template

````markdown
# Contract Playbook Package — [Organization]

## 1. Executive Summary
- Objective:
- Scope:
- Jurisdictions:
- Risk posture:
- Implementation mode:

## 2. Clarification Decisions
| Decision Area | Selected Option | Why It Matters |
|---|---|---|

## 3. Assumptions and Constraints
- Assumption 1
- Constraint 1

## 4. Clause Position Matrix
| Clause Family | GREEN | YELLOW Fallback A | YELLOW Fallback B | RED Trigger | BLACK Trigger | Required Approver |
|---|---|---|---|---|---|---|

## 5. Approval Matrix
| Tier | Trigger Criteria | Required Approvers | SLA | Escalation Owner |
|---|---|---|---|---|

## 6. Exception and Escalation Rules
- Exception logging fields:
- Escalation conditions:
- Required decision memo fields:

## 7. Clause Library Governance Metadata
| Clause ID | Owner | Version | Effective Date | Jurisdictions | Last Validation | Retirement Trigger |
|---|---|---|---|---|---|---|

## 8. KPI Framework
| KPI | Definition | Baseline | Target | Review Cadence |
|---|---|---|---|---|
- Mandatory KPIs: cycle time, fallback acceptance rate, escalation rate, deviation rate, leakage proxy.

## 9. Priority Findings and Remediation
| Finding ID | Severity (GREEN/YELLOW/RED/BLACK) | Impact | Remediation | Owner | Due Date |
|---|---|---|---|---|---|

## 10. Implementation Backlog
| Task | Priority Tier | Owner | Dependency | Target Date |
|---|---|---|---|---|

## 11. Glass Box Audit
```yaml
[populate glass_box template]
```

## 12. Sources and Verification Notes
- Verified sources:
- [VERIFY] items:
- [CHECK CURRENCY] items:
```
````

## Provenance

Created by Legalcode (2026-02-28). Initial scaffold produced with legal-skill-creator
workflow, then upgraded via legalcode-skill-enhancement methodology (dual analysis tracks,
quality-bar verification, and source-backed refinement).

Research inputs used in this enhancement:
- WorldCC Contracting Principles (Oct 2022):
  https://www.worldcc.com/Portals/IACCM/WorldCC%20Contracting%20Principles%20-%20October%202022.pdf
- CLOC Core 12 maturity references:
  https://cloc.org/core-12-maturity-assessment-playbook/
- ACC contracting approval governance references:
  https://www.acc.com/resource-library/contract-review-and-approval-and-signatory-authority-policy-matrix-signature
  https://www.acc.com/resource-library/systematic-approach-streamlining-contracting-approvals
- Supplemental CLM operational KPI/library governance references [VERIFY]:
  https://www.sirion.ai/library/contract-analytics/contract-lifecycle-management-kpi-metrics/
  https://www.sirion.ai/library/contract-insights/fallback-clauses-ai-playbooks-reduce-redlines/
