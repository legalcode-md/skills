---
name: legalcode-privacy-policy-drafter
description: >
  Draft, localize, and QA website/app privacy policies and notice-at-collection content
  across GDPR/UK GDPR, CCPA/CPRA, LGPD, and expanding state/global privacy regimes.
  Use when launching products, expanding to new jurisdictions, updating data practices,
  or remediating policy gaps found during audits, enforcement readiness checks, or
  incident-driven policy refreshes.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Privacy Policy Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted privacy-policy drafting
> and compliance analysis. It does not constitute legal advice. All outputs must be
> reviewed by qualified counsel in each applicable jurisdiction before publication.
> Privacy laws, regulatory guidance, and enforcement priorities change frequently; verify
> current applicability before relying on any statement. Mark uncertain legal assertions
> as `[VERIFY]` or `[CHECK CURRENCY]`.

## Purpose and Scope

Use this skill to produce an external-facing privacy policy package that is:
- Legally structured across multiple jurisdictions.
- Operationally accurate to actual data handling.
- Ready for legal review and publication.

This skill does:
- Build a jurisdiction-aware policy architecture.
- Draft modular policy language by topic and legal regime.
- Run policy-to-practice consistency checks.
- Produce remediation tasks and publication readiness status.

This skill does not:
- Replace legal advice or attorney sign-off.
- Guarantee regulator acceptance.
- Fully resolve sector overlays (health, financial services, telecom, children) without
  explicit sector localization.

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic and uses localization modules.

Baseline legal anchors:
- GDPR (EU) Regulation (EU) 2016/679, especially Articles 12-14.
  Source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
- UK GDPR transparency guidance (ICO right-to-be-informed guidance).
  Source: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/
- California CCPA/CPRA statutory and regulatory program material.
  Source: https://oag.ca.gov/privacy/ccpa
  Source: https://cppa.ca.gov/regulations/
- Brazil LGPD (Lei 13.709/2018), including transparency and rights framework.
  Source: http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

[JURISDICTION-SPECIFIC] Localize for:
- EU member-state overlays and supervisory guidance.
- UK Data Protection Act interactions and ICO updates.
- US state-specific rights, appeals, and opt-out mechanics.
- Brazil ANPD sub-regulatory guidance and operational expectations.
- Language obligations (for example Quebec/French requirements) `[VERIFY]`.

## Interactive Clarification

Use **CLARIFY** whenever answers materially change legal drafting.

### CLARIFY packet (required before drafting)

1. **Entity and channels**
- Options: Website only, SaaS web app, Mobile app, Multi-channel ecosystem.
- Why it matters: Changes notice-at-collection surfaces and tracker disclosures.

2. **User geography**
- Options: Single jurisdiction, Multi-jurisdiction, Global unknown.
- Why it matters: Determines module stack and rights matrix complexity.

3. **Data profile**
- Options: Basic account/contact only, Includes sensitive/special-category data,
  Includes children/minors data, Includes precise geolocation/biometrics.
- Why it matters: Triggers stricter notice content and consent/governance language.

4. **Monetization and sharing model**
- Options: No third-party sharing, Processor/service-provider only,
  Advertising/measurement ecosystem, Data sale/share or cross-context advertising.
- Why it matters: Controls opt-out disclosures and third-party detail requirements.

5. **Automation and profiling**
- Options: None, Personalization only, Eligibility/risk scoring,
  Significant automated decisioning.
- Why it matters: May require enhanced transparency and rights language.

6. **Policy posture**
- Options: Conservative legal-first, Balanced legal/UX, Product-first concise.
- Why it matters: Affects drafting style and detail density while preserving mandatory content.

If facts are incomplete, proceed with explicit assumptions tagged `[ASSUMPTION]`.

## Workflow

### Step 1: Intake and data-practice inventory

Collect:
- Legal entity names and contact channels.
- Products/channels covered by the policy.
- Data categories collected and collection points.
- Processing purposes and lawful-basis candidates.
- Sharing/disclosure map (vendors, affiliates, advertising partners).
- Retention rules and deletion workflows.

**CLARIFY** if data flow documentation is stale or incomplete.

### Step 2: Jurisdiction applicability map

Build the initial legal coverage map from user geography and business operations.
Output a table with:
- Jurisdiction.
- Applies? (Yes/No/Uncertain).
- Why it applies.
- Required policy modules.

### Step 3: Mandatory disclosure matrix

Generate a obligations matrix by jurisdiction for:
- Identity and contact details.
- Processing purposes and legal basis.
- Data categories and sources.
- Recipients/third-party categories.
- International transfers and safeguards.
- Retention periods or criteria.
- Data-subject/consumer rights and request channels.
- Complaint/escalation channels.
- Automated decisioning/profiling disclosures.

### Step 4: Draft policy architecture

Create a consistent section structure using plain language:
1. Who we are.
2. Data we collect.
3. How we use data.
4. Legal bases (where required).
5. Sharing/disclosure.
6. International transfers.
7. Retention.
8. Rights and choices.
9. Cookies/trackers and similar technologies.
10. Security summary.
11. Children/minors.
12. Contact details.
13. Jurisdiction-specific addenda.

### Step 5: Jurisdiction module drafting

Draft localized modules for each applicable regime.

**CLARIFY** if one global policy vs geo-specific policy pages are both feasible:
- Option A: Single global policy with addenda.
- Option B: Region-specific policies with shared core.

### Step 6: Operational truthfulness and systems check

Validate policy statements against real operations:
- Consent/cookie banner behavior.
- DSAR/consumer-request tooling.
- Data retention execution.
- Vendor/subprocessor list accuracy.
- Cross-border transfer mechanisms.

Classify each mismatch as a finding and produce remediation tasks.

### Step 7: Rights workflow validation

Ensure each promised right has a practical execution path:
- Intake channel.
- Verification logic.
- SLA/timeline.
- Fulfillment and appeal workflow.

Flag policy promises with no operational support as `BLOCKED`.

### Step 8: Publication-readiness gate

Run legal and quality gates, then classify publication state:
- `READY_FOR_COUNSEL_REVIEW`
- `PARTIAL_REMEDIATION_REQUIRED`
- `BLOCKED_HIGH_RISK_GAPS`

### Step 9: Delivery package

Deliver:
- Draft privacy policy text.
- Jurisdiction addenda.
- Finding register with owners/deadlines.
- Priority remediation plan.
- Executive summary with confidence and limitations.

## Deep Topic Analysis

### A. Required Notice Content Matrix (starter)

| Topic | GDPR / UK GDPR | CCPA/CPRA | LGPD | Global baseline guidance |
|---|---|---|---|---|
| Controller identity | Required | Required in privacy policy context | Required | Always include legal entity + contact |
| Purposes | Required | Required | Required | Use concrete purpose language |
| Legal basis | Required | Not framed as legal-basis table | Basis/model disclosure expected in context | Include where legally required |
| Rights | Required | Required | Required | Map to execution channel + timeline |
| Transfers | Required when applicable | Disclose sharing categories/transfers where relevant | Cross-border transparency expected | Add transfer mechanism summary |
| Retention | Required (period or criteria) | Required disclosures expected in policy design | Required by principle/ANPD posture | Avoid vague "as needed" only |
| Automated decisions | Required when applicable | ADMT/risk-assessment trend is active `[CHECK CURRENCY]` | Include where relevant `[VERIFY]` | Add module for meaningful logic explanations |

### B. Channel and surface mapping

Require policy consistency across:
- Web footer policy.
- In-product notices.
- Mobile app store privacy disclosures.
- Cookie banner / preference center.
- Notice-at-collection and just-in-time prompts.

### C. Policy-to-practice integrity checks

For each major statement, verify:
- Source of truth system.
- Responsible owner.
- Last validation date.
- Evidence artifact.

## Severity and Status Classification

Use dual classification for drafting work.

### 1) Clause Materiality
- `REQUIRED`: Must include for applicable regime or high-risk processing profile.
- `RECOMMENDED`: Strong best practice; omission increases risk but may be acceptable short-term.
- `OPTIONAL`: Contextual language not generally mandatory.

### 2) Implementation Readiness
- `READY`: Drafted and operationally supported.
- `PARTIAL`: Drafted but operational controls or evidence incomplete.
- `BLOCKED`: Mandatory content missing or unsupported by operations.

## Actionable Output per Finding

Each finding must include:

| Field | Requirement |
|---|---|
| Finding ID | Stable unique ID |
| Jurisdiction | Specific legal regime |
| Topic | Policy section/topic |
| Materiality | REQUIRED / RECOMMENDED / OPTIONAL |
| Readiness | READY / PARTIAL / BLOCKED |
| Legal basis | Specific authority or `[VERIFY]` |
| Gap description | Exact mismatch or omission |
| Remediation action | Concrete task |
| Owner | Function/team |
| Deadline | Date or sprint target |
| Evidence required | Artifact proving closure |
| Confidence | Definite/High/Probable/Possible/Unlikely |

## Prioritization Framework

- `Tier 1 (Publish Blockers)`: Any `REQUIRED + BLOCKED` finding.
- `Tier 2 (Pre-Launch Remediation)`: `REQUIRED + PARTIAL` or `RECOMMENDED + BLOCKED`.
- `Tier 3 (Post-Launch Hardening)`: `RECOMMENDED + PARTIAL` or `OPTIONAL` findings.

## Citation Quality Gates

Run these silently before delivery:

1. `Source`: Every legal claim maps to statute/regulator guidance, or is tagged `[VERIFY]`.
2. `Format`: Citations use consistent jurisdiction-aware format.
3. `Currency`: Potentially changing rules are tagged `[CHECK CURRENCY]`.
4. `Domain`: No jurisdiction-specific rule stated as universal.
5. `Confidence`: Uncertainty is explicit; avoid hidden assumptions.

## Self-Interrogation (High-Impact Findings)

For every `Tier 1` finding, run 3 passes:

1. `Legal chain integrity`: Does the blocker logically follow from cited authority?
2. `Completeness`: Are material exceptions or alternative compliance paths considered?
3. `Adversarial challenge`: What is the strongest argument that this is not a blocker?

If challenge succeeds, downgrade with explicit rationale. If not, keep blocker status.

## Confidence Scoring

| Level | Range | Meaning | Required Action |
|---|---|---|---|
| Definite | 0.95-1.00 | settled duty + verified facts | proceed with direct recommendation |
| High | 0.80-0.94 | strong support, minor caveat | proceed with concise caveat |
| Probable | 0.60-0.79 | defensible but fact-dependent | include contra-indicators |
| Possible | 0.40-0.59 | uncertain interpretation | escalate for counsel review |
| Unlikely | 0.00-0.39 | weak support/speculative | avoid assertion, mark `[UNCERTAIN]` |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-privacy-policy-drafter"
  topic: "Multi-jurisdiction privacy policy drafting"
  jurisdiction: "Jurisdiction-agnostic with localization modules"
  source_skills_analyzed: "4"
  enhancement_type: "Upgrade"
  legalcode_mcp: "Not connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  quality_score: "37/40"
  completeness: "18/18 elements"
  citations_verified: "6 VERIFIED / 0 UNVERIFIED in baseline references"
  confidence: "HIGH — primary sources used for core regimes"
  limitations:
    - "State/provincial and sector overlays require targeted localization"
    - "Active rulemaking areas must be re-checked before publication"
  reviewer: "AI-assisted — requires qualified legal review"
```

## Anti-Patterns

Avoid these mistakes when drafting privacy policies:

1. Using vague purpose statements (for example, "improve services") without concrete use cases.
2. Listing rights that the operations team cannot actually fulfill on time.
3. Copying jurisdiction-specific rights globally without applicability checks.
4. Promising deletion while retaining data indefinitely in backups without explanation.
5. Omitting data-sharing categories while using ad-tech or analytics partners.
6. Describing cross-border transfers as "secure" without mechanism disclosure.
7. Publishing cookie language that conflicts with CMP/banner behavior.
8. Hiding material disclosures behind dense legalese instead of plain-language headings.
9. Failing to update contact channels (DPO/privacy office) after org changes.
10. Claiming "we do not sell/share" without legal definition mapping per jurisdiction.
11. Ignoring minors/children handling where services are plausibly used by minors.
12. Treating policy publication as a one-time task with no review cadence.
13. Citing outdated regulator guidance without `[CHECK CURRENCY]` markers.
14. Mixing processor and controller obligations without role clarity.
15. Shipping policy text before confirming internal evidence sources for each claim.

## Writing Standards

- Use short headings and direct verbs.
- Prefer plain language over legalese while preserving legal precision.
- Keep each paragraph focused on one disclosure concept.
- Tie every rights statement to an execution channel.
- Avoid absolute statements ("never", "always") unless verified.
- Use consistent terminology across policy, CMP, and internal procedures.

## External Tool Integration

Preferred: use **legalcode-mcp** to verify current statutes, guidance, and enforcement context.

If legalcode-mcp is connected:
- Build a jurisdiction-specific legal-reference file first.
- Validate article/section citations before final output.
- Mark citations as VERIFIED in the audit trail.

If legalcode-mcp is not connected:
- Proceed with high-confidence primary public sources.
- Mark uncertain items with `[VERIFY]` or `[CHECK CURRENCY]`.
- Explicitly state that final legal verification is required.

## Output Format Template

```markdown
# Privacy Policy Draft Package

## A. Scope and Assumptions
- Entity:
- Channels:
- Jurisdictions:
- Assumptions:

## B. Draft Privacy Policy
### 1. Who We Are
### 2. Data We Collect
### 3. How We Use Data
### 4. Legal Bases (where required)
### 5. Sharing and Disclosure
### 6. International Transfers
### 7. Data Retention
### 8. Your Rights and Choices
### 9. Cookies and Similar Technologies
### 10. Security Overview
### 11. Children/Minors
### 12. Contact Us
### 13. Jurisdiction-Specific Addenda

## C. Jurisdiction Matrix
| Jurisdiction | Applies | Key Modules | Notes |
|---|---|---|---|

## D. Finding Register
| ID | Jurisdiction | Topic | Materiality | Readiness | Gap | Action | Owner | Deadline | Confidence |
|---|---|---|---|---|---|---|---|---|---|

## E. Priority Remediation Plan
### Tier 1 (Publish Blockers)
### Tier 2 (Pre-Launch)
### Tier 3 (Hardening)

## F. Publication Readiness
- Status: READY_FOR_COUNSEL_REVIEW / PARTIAL_REMEDIATION_REQUIRED / BLOCKED_HIGH_RISK_GAPS
- Key blockers:
- Counsel review focus:

## G. Glass Box Audit
```yaml
[glass_box template]
```
```

## Localization Notes

- For multi-US-state coverage, maintain a state addendum matrix and last-validated date.
- For EU/UK, separate legal-basis and rights wording from US-style opt-out language.
- For Brazil, ensure local terminology and rights language align with LGPD terminology.
- For Quebec or language-mandatory jurisdictions, provide local-language policy version `[VERIFY]`.

## Provenance

Legalcode original scaffold plus Legalcode enhancement workflow (2026-02-28).
Enhanced using:
- Structural and prompt-quality parallel analysis.
- Primary-source research file at `/tmp/legalcode-enhancement-research.md`.
- In-repo reference patterns from `legalcode-contract-review`, `legalcode-dpia-generator`,
  and `legalcode-breach-severity-assessment`.
