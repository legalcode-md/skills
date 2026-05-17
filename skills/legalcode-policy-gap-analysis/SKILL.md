---
name: legalcode-policy-gap-analysis
description: >
  Compares organizational policies and procedures against applicable regulatory
  requirements, industry standards, and best practices to identify gaps, conflicts,
  and areas requiring update. Builds a complete policy inventory; maps required
  policies across privacy (GDPR Arts. 5/24/32/33/35, CCPA/CPRA, LGPD, DPDP Act 2023,
  PIPL), cybersecurity (NIS2 Directive 2022/2555 Art. 21, ISO 27001:2022, NIST CSF 2.0,
  HIPAA Security Rule 45 C.F.R. Part 164, DORA Reg. 2022/2554), financial crime
  (BSA 31 U.S.C. §5318(h), FATF 40 Recommendations, EU AMLR 2024/1624), anti-corruption
  (FCPA 15 U.S.C. §78dd-1, UK Bribery Act 2010 s.7, OECD Convention), financial
  reporting (SOX §302/§404/§806, SEC whistleblower Rule 21F), employment/labor
  (FLSA, NLRA, EU Platform Work Directive, FTC non-compete vacatur landscape), and
  ESG/supply chain (UK Modern Slavery Act 2015 s.54, German LkSG, EU CSDDD Directive
  2024/1760). Evaluates each policy across seven adequacy dimensions: existence,
  currency, completeness, specificity, accessibility, training integration, and
  enforcement/attestation. Identifies three gap types: (1) required policies that are
  entirely absent, (2) existing policies with materially inadequate coverage or outdated
  provisions, and (3) policies conflicting with current regulatory requirements.
  Quantifies gaps using a 5×5 inherent risk matrix, five-level design-vs-operational
  effectiveness model, and residual risk formula with design-execution gap multiplier.
  Classifies gaps as CRITICAL/HIGH/MEDIUM/LOW with remediation owners, timelines, and
  success metrics. Supports eight operating modes: annual enterprise assessment, focused
  domain assessment, pre-regulatory examination preparation, M&A policy diligence,
  ISO 37301/ISO 27001 certification preparation, post-incident root cause analysis,
  board governance review, and regulatory change impact assessment. Produces policy gap
  register, domain heat map (policy area × jurisdiction), prioritized remediation
  roadmap (IMMEDIATE/NEAR-TERM/BACKGROUND tiers), board governance accountability
  assessment, and Glass Box audit trail. Jurisdiction-agnostic core with
  [JURISDICTION-SPECIFIC] markers for US, EU, UK, Australia, Canada, Brazil, India,
  and Singapore.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Policy Gap Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted policy gap analysis.
> It does not constitute legal advice and does not create an attorney-client relationship.
> All outputs should be reviewed by qualified legal counsel and compliance professionals
> licensed in the relevant jurisdictions before use. This skill does not replace a formal
> policy review or compliance audit conducted by a qualified professional. It produces a
> structured framework to support a human-led review — not a substitute for one.
> All CRITICAL and HIGH gap classifications require validation through primary evidence and
> stakeholder interviews before board presentation. Laws, regulations, and enforcement
> priorities change; verify current applicability before relying on any provision described
> here. Statutory references, regulatory citations, and enforcement data cited from memory
> carry hallucination risk — always verify against authoritative sources before using in
> regulatory submissions, audit documentation, or board reporting. ISO standards referenced
> here require licence purchase for full text; consult official ISO publications for
> authoritative requirements.

## Purpose and Scope

This skill systematically compares an organization's policy library against applicable
regulatory requirements, industry standards, and enforcement priorities. It identifies
where policies are absent, inadequately written, operationally ineffective, or in conflict
with current law — and produces a prioritized, evidence-based remediation roadmap.

Policy gap analysis sits at the foundation of every compliance program. Regulators
worldwide increasingly distinguish between organizations with documented, implemented
compliance frameworks and those with "paper compliance" — policies that exist but are
not followed. The DOJ Evaluation of Corporate Compliance Programs (September 2024) asks
three questions of every program: Is it well-designed? Is it adequately resourced and
empowered? Does it work in practice? This skill addresses all three.

**Covers:**
- Complete policy inventory development and gap identification across 8 regulatory domains
- Regulatory obligation mapping: required policies per applicable framework and jurisdiction
- Seven-dimension policy adequacy assessment (existence, currency, completeness, specificity,
  accessibility, training, enforcement/attestation)
- Three gap type classification: absent, inadequate, conflicting
- Inherent risk quantification using 5×5 likelihood-impact matrix per policy domain
- Policy design effectiveness vs. operational effectiveness (five-level maturity model)
- Residual risk calculation with design-execution gap multiplier
- CRITICAL / HIGH / MEDIUM / LOW gap severity classification
- Policy change trigger analysis (regulatory change, audit finding, M&A, certification prep)
- Policy ownership and governance accountability assessment
- Prioritized remediation roadmap (IMMEDIATE / NEAR-TERM / BACKGROUND tiers)
- Board governance report with policy gap heat map and investment case
- Glass Box audit trail for regulator and auditor traceability

**Does not:**
- Design or build compliance program architecture (see `legalcode-compliance-program-builder`)
- Conduct deep domain-specific compliance assessments — use domain specialists:
  - AML/KYC: `legalcode-aml-kyc-compliance`
  - HIPAA: `legalcode-hipaa-compliance-assessment`
  - NIS2: `legalcode-nis2-compliance-assessment`
  - NIST CSF: `legalcode-nist-csf-mapping`
  - GDPR: `legalcode-gdpr-legal-basis-assessment`, `legalcode-dpia-generator`
  - Data Processing Agreements: `legalcode-dpa-review-and-negotiation`
- Provide legal advice or substitute for qualified compliance counsel
- Guarantee regulatory immunity — gap analysis does not eliminate enforcement risk
- Perform technical control testing (penetration testing, vulnerability scanning)
- Replace a formal audit or examination conducted by a licensed professional

**Related skills:**
- `legalcode-compliance-risk-assessment` — enterprise risk assessment; complements this
  skill by quantifying residual risk across compliance domains (not policy-specific)
- `legalcode-compliance-program-builder` — builds the full compliance program framework
  (governance + policies + training + third-party DD + investigation + monitoring)
- `legalcode-regulatory-change-tracker` — monitors regulatory changes; feeds into this
  skill's policy currency assessment
- `legalcode-employee-handbook-review` — deep review of employment-specific policies
- `legalcode-vendor-privacy-assessment` — third-party vendor policy and controls assessment

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The organization's operational jurisdictions
determine which regulatory frameworks apply. Content is applicable globally; jurisdiction-
specific requirements are marked throughout.

[JURISDICTION-SPECIFIC: United States] Apply DOJ ECCP September 2024 three-question
framework. Privacy: CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.); US state privacy law
matrix (Colorado, Connecticut, Virginia, Texas, Florida, Montana, Oregon, Nevada + 8
additional states 2026); GLBA Safeguards Rule (16 C.F.R. Part 314, effective June 2023
for non-bank financial institutions). Financial crime: BSA 31 U.S.C. §5318(h); FinCEN
CDD Final Rule 31 C.F.R. §1010.230; SAR 31 C.F.R. §1020.320. Cybersecurity: NYDFS
23 NYCRR Part 500 (updated Nov 2023 for Class A companies); SEC cybersecurity incident
disclosure rules (effective Dec 2023). Employment: NLRA Section 7 rights; FLSA;
Title VII/ADA/ADEA; FTC non-compete landscape (vacatur Aug 2024 in Texas but Section 5
unfair method enforcement continues per *Gateway Services* Sept 2025). Anti-corruption:
FCPA 15 U.S.C. §78dd-1 et seq. ESG: SEC climate disclosure rules [VERIFY current
status after litigation challenges].

[JURISDICTION-SPECIFIC: European Union] Privacy: GDPR Reg. 2016/679 + EDPB Guidelines
(ongoing 2024–2025 guidance on consent, cross-border transfers, AI automated decisions);
ePrivacy Directive 2002/58/EC (Art. 5(3) cookie consent). Cybersecurity: NIS2 Directive
2022/2555 (Oct 2024 transposition deadline; COMPLIANT/NON-COMPLIANT varies by member
state). Financial: EU AML Regulation 2024/1624 (effective July 2027); Whistleblower
Protection Directive 2019/1937 (transposed by Dec 2021 deadline — verify national
implementations). ESG: CSRD Directive 2022/2464 (ESRS sustainability reporting);
CSDDD Directive 2024/1760 (supply chain due diligence, phased effective 2027–2029);
German LkSG Supply Chain Act (effective Jan 2023 for 3,000+ employees; June 2024 for
1,000+ employees). AI: EU AI Act 2024/1689 (GPAI provider obligations from Aug 2025;
high-risk system obligations Aug 2026). Compliance management: ISO 37301:2021.

[JURISDICTION-SPECIFIC: United Kingdom] UK GDPR (retained EU law post-Brexit) + DUA
Act 2025; UK Bribery Act 2010 s.7 "adequate procedures" doctrine (six MoJ principles);
note: no facilitation payments exception (unlike US FCPA). Financial crime: POCA 2002;
MLR 2017 SI 2017/692; ECCTA 2023 (Companies House reforms, failure to prevent fraud
Pt.4). ESG: UK Modern Slavery Act 2015 s.54 transparency statement. Employment:
Employment Rights Act 1996 + ERA 2025. Cybersecurity: NIS Regulations 2018 (SI 2018/506)
+ NIS2 [VERIFY UK NIS2-equivalent status post-Brexit].

[JURISDICTION-SPECIFIC: Australia] Privacy Act 1988 (Cth) + Privacy and Other Legislation
Amendment Act 2024 (mandatory DPO for large organizations; civil penalties up to AUD 50M);
Australian Privacy Principles (APPs) — 30-day breach notification SLA (vs. GDPR 72-hour).
Modern slavery: Modern Slavery Act 2018 (Cth) + NSW Modern Slavery Act 2018. Competition:
CCA 2010.

[JURISDICTION-SPECIFIC: Canada] PIPEDA (federal); Quebec Law 25 (fully effective Sept
2023); provincial health data protection acts. Anti-corruption: CFPOA 1998.

[JURISDICTION-SPECIFIC: Brazil] LGPD Lei 13.709/2018 + ANPD Resolution 15/2024 (Brazil
SCCs for international transfers, mandatory Aug 2025). Anti-corruption: Lei 12.846/2013
(Clean Company Act) + CGCC compliance guidelines.

[JURISDICTION-SPECIFIC: India] DPDP Act 2023 (Digital Personal Data Protection Act);
DPDP Rules 2025 (compliance deadline May 2027 [VERIFY]). Companies Act 2013 (S.177
audit committee; S.135 CSR for large companies).

[JURISDICTION-SPECIFIC: Singapore] PDPA 2012 (Personal Data Protection Act) + 2020
amendments (mandatory breach notification 72-hour; advisory guidelines 2021). MAS
notices for financial institutions.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points using the ⟁ CLARIFY
pattern. The skill pauses and asks when:

- The answer would change which frameworks and policies are in scope
- Multiple valid assessment approaches exist and the user's priority matters
- Policy inventory data is missing and needs to be clarified before analysis begins
- Risk tolerance or organizational context is needed to classify gap severity correctly

When you reach a **⟁ CLARIFY** block, ask the user before proceeding — do not silently assume
defaults. Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4 questions per
  call, 2–4 options each, header ≤ 12 characters. Pass the CLARIFY options as the `options`
  array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a `canUseTool`
  callback):** emit the CLARIFY questions as numbered plain text and **stop until the user
  replies**. Do not proceed with assumed answers.

Skip any CLARIFY question the user has already answered in the initial prompt or prior
conversation. When you proceed with partial context, state every assumption explicitly so the
user can correct it.

For batch/non-interactive runs, use these defaults:
- Operating mode: Annual Enterprise Assessment
- Risk profile: Regulated (tech/energy/manufacturing)
- Geographic footprint: Multi-jurisdiction (EU + US at minimum)
- Jurisdiction: Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Board risk appetite: Conservative defaults (lowest acceptable residual)

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Policy document set**: PDF, DOCX, or other format — one or multiple policies
- **Policy list**: A list of policy names/titles indicating what exists (without full text)
- **Gap request**: A description of the organization and a request to identify required policies
- **Regulatory change trigger**: A specific regulation change requiring policy review
- **M&A / integration scenario**: A description of an acquisition requiring policy diligence

Minimum required context to proceed:
- Organization sector (financial, healthcare, technology, manufacturing, professional services, etc.)
- Approximate size (headcount or revenue tier)
- Primary operational jurisdiction(s)
- Whether a policy library already exists (yes, partial, no)

If no input is provided, ask the user to supply organizational context.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, answer these questions (skip any already answered;
use defaults for batch runs):

1. **Operating Mode** (determines output scope and focus):
   - Annual Enterprise Assessment — full policy library review + heat map + roadmap
   - Focused Domain Assessment — single domain deep-dive (privacy, cybersecurity, AML, etc.)
   - Pre-Regulatory Examination — exam-ready evidence package + Glass Box
   - M&A Policy Diligence — acquirer / target policy gap and integration risk analysis
   - Certification Preparation — ISO 37301 / ISO 27001 / SOC 2 policy documentation audit
   - Post-Incident Root Cause Analysis — trace incident to underlying policy failure
   - Board Governance Review — board-ready policy accountability report
   - Regulatory Change Impact Assessment — specific regulation change → policy update map
   - *Why this matters*: Each mode produces different outputs and focuses on different domains.

2. **Organization Risk Profile** (determines regulatory obligation depth):
   - Highly-regulated (financial services, healthcare, defense, pharma, energy utilities)
   - Regulated (technology, professional services, manufacturing, retail/e-commerce)
   - General business (professional/creative services, non-profit, startup pre-scale)
   - *Why this matters*: Regulatory risk profile drives the policy requirement scope.
     A bank requires AML, GLBA, SOX, and SEC policies; a SaaS startup primarily needs
     privacy, cybersecurity, and employment policies.

3. **Geographic Footprint** (determines jurisdiction count):
   - Single country — specify which
   - Multi-jurisdiction, 2–5 countries — specify primary
   - Multi-jurisdiction, 5+ countries / global operations
   - *Why this matters*: Multi-jurisdiction operations require policy harmonization analysis
     and jurisdiction-specific overlays at each [JURISDICTION-SPECIFIC] marker.

4. **Policy Library Status** (determines starting point):
   - No policies — greenfield build required
   - Partial policies — existing policies provided for gap analysis
   - Full policies — existing library; assess currency and adequacy
   - Unknown — help identify what should exist before assessing gaps
   - *Why this matters*: Determines whether the output is a "what's missing" list vs.
     a "what needs updating" analysis vs. both.

5. **Assessment Trigger** (provides enforcement context):
   - Routine / annual review
   - Regulatory change (specify which regulation)
   - Audit finding or enforcement inquiry
   - M&A transaction (specify: acquirer, target, or integration)
   - Certification preparation (specify standard)
   - Post-incident remediation
   - Board mandate or investor requirement
   - *Why this matters*: Regulatory examinations and board mandates require different
     output confidence levels and documentation standards.

If the user provides partial context, proceed with stated defaults and note assumptions.

### Step 3: Build the Policy Inventory

Create or validate the organization's policy inventory. For each policy identified or
provided:

**3a. Assign a Policy Reference ID** (format: `POL-[DOMAIN]-[NUMBER]`):
- POL-PRV = Privacy and Data Protection
- POL-SEC = Information Security and Cybersecurity
- POL-FIN = Financial Crime (AML/KYC/Sanctions)
- POL-ACP = Anti-Corruption and Ethical Conduct
- POL-EMP = Employment and Labor
- POL-FRP = Financial Reporting and Internal Controls
- POL-ESG = ESG, Supply Chain, and Sustainability
- POL-SEC-SECT = Sector-Specific

**3b. Capture policy metadata** for each policy:

| Field | Description |
|-------|-------------|
| Policy ID | POL-[DOMAIN]-[N] |
| Policy Name | Full name as titled |
| Version | Version number if documented |
| Last Review Date | Date of last substantive review (not just re-approval) |
| Next Scheduled Review | If documented |
| Policy Owner | Named individual (role + name if available) |
| Approval Authority | Who approves (CEO, Board, CCO, etc.) |
| Distribution | Who has access (all staff, specific roles, publicly available) |
| Training Program | Whether staff training exists (yes, partial, no) |
| Attestation Program | Whether staff attest to compliance (yes, partial, no) |

**3c. Identify missing policies** by comparing the inventory against the Required Policy
Library (Section: Policy Requirements Reference Library below). For each identified gap:
- Mark as Gap Type 1 (entirely absent)
- Note the triggering regulatory framework
- Note the applicable jurisdiction(s)

**⟁ CLARIFY** — If the policy library is large (20+ policies), ask:
- Should I assess all policies comprehensively, or focus on the highest-risk domains first?
- Default: Prioritize by inherent risk score (Step 5) — domains with highest inherent risk
  receive deepest assessment.

### Step 4: Map Regulatory Obligations to Required Policies

For each applicable jurisdiction and operating sector, map regulatory obligations to
specific policy requirements. Use the Policy Requirements Reference Library as the
baseline. For each obligation:

**4a. Determine applicability** using this screening:

| Factor | MANDATORY | CONDITIONAL | NOT APPLICABLE |
|--------|-----------|-------------|----------------|
| Statutory requirement | Law explicitly requires policy | Regulation recommends or implies | Jurisdiction not applicable |
| Regulatory expectation | Regulators expect in examination | Frequently examined | Not an enforcement focus |
| Certification requirement | Required for certification | Recommended | Certification not sought |
| Contractual requirement | Customer/partner contract requires | Often required | No contractual obligation |

**4b. Produce a Regulatory Obligation Matrix** for the organization:

| Policy Domain | Policy Name | Required By | Applicability | Highest-Penalty Provision | Current Enforcement Focus | Last Updated |
|---------------|-------------|-------------|---------------|--------------------------|--------------------------|--------------|
| Privacy | Data Privacy Policy | GDPR Art. 24 | MANDATORY | €20M or 4% turnover | Consent + cross-border transfers 2024–2025 | [VERIFY] |
| Privacy | DPIA Procedure | GDPR Art. 35 | MANDATORY (high-risk) | Same as above | AI automated decisions, profiling | [VERIFY] |
| Cybersecurity | Incident Response Policy | NIS2 Art. 21(2)(b) | MANDATORY (essential/important) | €10M or 2% turnover | 24h/72h/1-month reporting chain | Oct 2024 |
| [Continue for all applicable rows] | | | | | | |

**4c. Identify conflicts** — compare existing policies against current regulatory requirements:
- Mark as Gap Type 3 (conflicting) where existing policy language contradicts applicable law
- Note the specific conflict (e.g., "Policy states 5-year retention; GDPR storage limitation
  principle requires minimum necessary retention — conflict with Art. 5(1)(e)")
- Note the effective date of the conflicting requirement

### Step 5: Assess Inherent Policy Gap Risk

For each policy domain, quantify **Inherent Policy Gap Risk** before considering current
policies. This measures the exposure if no effective policy existed for this domain.

**5a. Likelihood scale (1–5):**

| Score | Label | Definition |
|-------|-------|-----------|
| 1 | Rare | Domain presents negligible regulatory risk; no material penalties possible |
| 2 | Unlikely | Domain regulated; organization profile creates low exposure |
| 3 | Possible | Domain regulated; exposure if gaps found is moderate; enforcement periodic |
| 4 | Likely | Domain actively enforced; organization has characteristics regulators target |
| 5 | Almost Certain | High-profile enforcement area; organization is a likely examination target |

**5b. Impact scale (1–5):**

| Score | Label | Definition |
|-------|-------|-----------|
| 1 | Negligible | No regulatory consequence; administrative cleanup only |
| 2 | Minor | Enforcement notice; minor fine; limited operational disruption |
| 3 | Moderate | Regulatory warning; moderate fine (up to 1% revenue); short-term disruption |
| 4 | Major | Significant fine (1–5% revenue); operations disrupted; reputational exposure |
| 5 | Catastrophic | Criminal exposure; license revocation; existential fine; personal liability |

**Inherent Risk Score = Likelihood × Impact (range: 1–25)**

**5c. Written rationale requirement** — every score must include:
- The specific regulatory provision driving the likelihood score
- The enforcement data or precedent supporting the impact score
- A [VERIFY] marker where the rationale relies on unconfirmed assumptions
- Confidence level (VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED)

**Example:**
```
Policy Domain: Data Privacy Policy (GDPR compliance)
Jurisdiction: EU operations — 40,000+ data subjects

Likelihood: 4 (Likely)
  Rationale: GDPR actively enforced by all 27 member state DPAs. European Data
  Protection Board 2024 work program identifies consent, cross-border transfers,
  and AI automated decisions as priority enforcement areas. Organization processes
  sensitive employment + customer data across 6 EU countries. [VERIFY: confirm
  data subject count and cross-border transfer scope]

Impact: 4 (Major)
  Rationale: GDPR maximum penalty €20M or 4% global annual turnover. Recent
  enforcement benchmarks: Italian SA €5M (2024, analytics provider); CNIL fines
  in 2023–2024 averaging €3M for consent violations. [VERIFY: confirm current
  fine levels with primary source]

Inherent Risk Score: 4 × 4 = 16 (HIGH)
Confidence: LIKELY (0.75) — GDPR applicability confirmed; enforcement pattern
  verified from public EDPB enforcement tracker; data subject count [VERIFY]
```

### Step 6: Evaluate Policy Adequacy — 7-Dimension Assessment

For each policy in the inventory (prioritize MEDIUM+ inherent risk domains), evaluate
adequacy across seven dimensions. This is the core analytical step distinguishing
a shallow "does it exist?" check from a professional adequacy assessment.

#### The 7 Adequacy Dimensions

| # | Dimension | What to Assess | Key Questions |
|---|-----------|----------------|---------------|
| 1 | **Existence** | Does the policy exist as a standalone document or in a code of conduct? | Is the policy named, findable, and officially adopted? |
| 2 | **Currency** | When was it last substantively reviewed? Is it current with applicable regulations? | Does it reference current regulatory versions? Does it predate major regulatory changes? |
| 3 | **Completeness** | Does it cover all required elements under applicable regulations? | Which required elements are missing? Are there placeholder sections? |
| 4 | **Specificity** | Is it specific enough to guide action, or just a vague statement of intent? | Can an employee make a compliant decision using this policy alone? |
| 5 | **Accessibility** | Is it available to the personnel who need it? In the required languages? | Is it posted on intranet, LMS, or equivalent? Translated? |
| 6 | **Training Integration** | Have affected personnel been trained on the policy? Evidence of training? | Is there an LMS completion record? Is training current (annual)? |
| 7 | **Enforcement / Attestation** | Is there a mechanism to monitor compliance and attest to adherence? | Annual attestation? Policy exception process? Consequence framework? |

#### Design Effectiveness (DE) vs. Operational Effectiveness (OE)

Assess each policy on two separate axes:

**Design Effectiveness (DE):** Is the policy well-written to address the regulatory requirement?
Is it fit-for-purpose on paper?

**Operational Effectiveness (OE):** Is the policy actually implemented? Is there evidence of
consistent execution (training completion, attestations, monitoring data, exception records)?

| Level | Design Effectiveness | Operational Effectiveness |
|-------|---------------------|--------------------------|
| 1 | Policy absent — no document exists | No evidence of awareness, communication, or training |
| 2 | Policy exists but materially incomplete; fundamental provisions missing | Policy communicated (published); no training program; no attestation evidence |
| 3 | Policy covers requirements partially; notable gaps or outdated provisions | Staff trained via periodic sessions; inconsistent attestation; exception rate unknown |
| 4 | Policy well-designed; addresses regulatory requirements; regularly reviewed | Staff trained annually; formal attestation program; exception tracking; <5% violation rate |
| 5 | Policy exceeds requirements; integrates with workflows; best-in-class | Continuous monitoring; zero-tolerance consequence model; policy integrated into hiring/procurement/performance; <1% exception rate |

#### MINIMUM Policy Adequacy Score

**Domain Policy Score = MINIMUM(DE, OE)**

This prevents false assurance from well-written policies that are not followed. A policy
with DE=4 (well-written) but OE=1 (never communicated or trained) has a domain score of 1.
This is intentional: a policy on paper that no one knows about provides zero protection —
and in some enforcement contexts creates greater liability (it shows management was aware
of the requirement but failed to operationalize it).

#### Design-Execution Gap

**Design-Execution Gap = DE − OE**

A gap of 2+ points is a regulatory red flag. It indicates management designed adequate
procedures but failed to resource their operation — a pattern regulators identify as
management indifference or systemic resource failure.

Apply the **Design-Execution Gap Multiplier** to residual risk: × 1.25 if DE − OE ≥ 2.

**⟁ CLARIFY** — For policies where Design or Operational Effectiveness cannot be assessed
from available materials, ask:
- "I cannot assess operational effectiveness for [Policy Name] without evidence of
  training records, attestation programs, or monitoring data. Can you provide this, or
  should I flag as [VERIFY] with ASSUMED OE=2 (Initial/Ad Hoc)?"
- Default: ASSUMED OE=2 with [VERIFY] marker and lower confidence score.

### Step 7: Calculate Residual Policy Gap Risk

Combine inherent risk and policy adequacy to calculate residual policy gap risk.

**Residual Policy Gap Risk = Inherent Risk Score × (1 − OE/5) × Gap Multiplier**

Where:
- Inherent Risk Score = L × I from Step 5 (1–25)
- OE = Operational Effectiveness (1–5) from Step 6
- Gap Multiplier = 1.25 if DE − OE ≥ 2; otherwise 1.00

**Examples:**

```
Policy Domain: Anti-Corruption Policy (FCPA + UK Bribery Act)
Inherent Risk: 20 (CRITICAL — Likelihood 4, Impact 5: criminal + unlimited fine)
OE: 2 (Policy exists; not communicated; no training evidence)
DE: 4 (Policy well-drafted; covers FCPA gifts/entertainment, government officials)
Gap Multiplier: 1.25 (DE − OE = 4 − 2 = 2, triggers multiplier)
Residual: 20 × (1 − 2/5) × 1.25 = 20 × 0.6 × 1.25 = 15.0 (CRITICAL)

Policy Domain: Data Retention Policy
Inherent Risk: 12 (HIGH — Likelihood 3, Impact 4: GDPR enforcement)
OE: 4 (Policy published; annual training; LMS records; 97% completion)
DE: 4 (Well-drafted; references GDPR Art. 5(1)(e); retention schedules attached)
Gap Multiplier: 1.00 (DE − OE = 0)
Residual: 12 × (1 − 4/5) × 1.00 = 12 × 0.2 × 1.00 = 2.4 (LOW)
```

**Residual Gap Risk Classification:**

| Score Range | Tier | Meaning | Regulatory Analogy |
|-------------|------|---------|-------------------|
| ≥ 15 | **CRITICAL** | Immediate enforcement-ready deficiency; regulators could act now | "Significant weakness" in examination; voluntary disclosure risk |
| 9–14 | **HIGH** | Material gap requiring near-term remediation; elevated enforcement exposure | "Identified deficiency" requiring remediation plan |
| 5–8 | **MEDIUM** | Notable gap; tolerable with enhanced monitoring and 90-day remediation | "Observation" in regulatory examination; low likelihood of immediate action |
| 1–4 | **LOW** | Minor gap; routine remediation acceptable; minimal regulatory risk | Housekeeping item; acceptable risk given other controls |

**Aggregation Rule:**
- Overall domain policy tier = LOWEST residual risk tier across all policies in domain
- This prevents a well-rated policy from masking a critical gap elsewhere in the same domain
- Example: AML domain has 5 required policies; 4 score LOW but SAR Procedure is CRITICAL
  → Overall AML domain tier = CRITICAL

### Step 8: 3-Pass Self-Interrogation for CRITICAL and HIGH Gaps

For every gap classified CRITICAL or HIGH, apply this adversarial 3-pass review before
delivering the finding. This prevents false-positive classifications and grounds findings
in enforcement reality.

**Pass 1 — Policy Chain Integrity:**
Does the CRITICAL/HIGH classification follow logically from the inherent risk score and
adequacy evidence? Is the scoring based on verified evidence or primarily assumptions?

*Single-weakest-evidence test*: State the single piece of evidence most critical to this
classification. If it is ASSUMED rather than VERIFIED, what would the score be under the
opposite assumption? If the classification changes significantly, lower confidence.

**Pass 2 — Compensating Controls:**
Have all relevant policies and governance controls been considered? Is there a compensating
policy, process, or governance mechanism that could lower the residual score?

Examples of compensating controls:
- A Privacy Policy may be outdated, but a strong DPO function with quarterly EDPB guidance
  reviews may compensate for limited currency
- An Anti-Corruption Policy may be OE=2, but a robust expense approval workflow with
  manager review at every level may partially compensate for lack of formal training

If a meaningful compensating control exists, document it and lower the residual score
accordingly. Do not ignore it.

**Pass 3 — Regulatory and Enforcement Context:**
Is this gap a known area of regulatory examination or enforcement focus for this industry
and jurisdiction? Is there a documented enforcement pattern supporting the CRITICAL
classification?

- If enforcement is HIGH in this area: maintain or elevate classification
- If enforcement is LOW or theoretical: consider lowering to HIGH from CRITICAL
- Cite specific enforcement precedents where available; mark [VERIFY] where not confirmed

### Step 9: Build the Policy Gap Register

Compile all findings into a structured Policy Gap Register. For each gap identified:

| Field | Description |
|-------|-------------|
| Gap ID | GAP-[DOMAIN]-[N] (sequential) |
| Gap Type | 1 = Absent; 2 = Inadequate; 3 = Conflicting |
| Policy Domain | Domain from policy reference ID |
| Policy Name | Name of the affected/missing policy |
| Required By | Regulatory framework(s) requiring this policy |
| Jurisdiction(s) | Applicable jurisdictions |
| Gap Description | Specific description of what is missing or inadequate |
| Inherent Risk Score | L × I |
| Policy Adequacy Score | MINIMUM(DE, OE) |
| Design-Execution Gap | DE − OE |
| Residual Risk Score | Calculated per formula |
| Gap Tier | CRITICAL / HIGH / MEDIUM / LOW |
| Confidence Level | VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED |
| Remediation Action | Specific action required |
| Recommended Owner | Named role (CCO, DPO, CISO, General Counsel, etc.) |
| Target Timeline | Days from assessment date |
| Success Metric | How completion will be verified |
| 3-Pass Result | Summary of self-interrogation findings |

**Gap Type Definitions:**

**Gap Type 1 — Absent Policy:**
The regulatory framework requires a specific policy and no such policy exists in any form
(not even embedded within a broader document). This represents the highest inherent
risk — no protection at all.

**Gap Type 2 — Inadequate Policy:**
A policy exists but is materially deficient in one or more of the 7 adequacy dimensions.
Common inadequacies:
- Currency: Predates regulatory changes > 18 months (for fast-moving areas like privacy, AI)
- Completeness: Missing required elements (e.g., data retention schedule absent from privacy policy)
- Specificity: Policy is aspirational but provides no operational guidance
- Training: Policy exists but staff unaware or untrained
- Enforcement: No attestation, no exception process, no monitoring

**Gap Type 3 — Conflicting Policy:**
Existing policy language directly contradicts current regulatory requirements. Examples:
- Policy permits retention of personal data for 10 years as a standard; GDPR storage
  limitation principle requires deletion when purpose served (conflict with Art. 5(1)(e))
- Policy prohibits employees from reporting externally; conflicts with SEC whistleblower
  Rule 21F and EU Whistleblower Protection Directive 2019/1937
- Policy permits agents to pay facilitation payments as a standard practice; UK Bribery Act
  2010 s.1 prohibits all such payments (unlike US FCPA which has a narrow exception)

### Step 10: Policy Change Trigger Analysis

Identify whether the gaps are driven by regulatory change, organizational change, or
policy lifecycle failure.

**10a. Regulatory Change Drivers:**

For each CRITICAL or HIGH gap, identify the triggering regulatory event:
- New law or regulation (cite: name + effective date + [VERIFY] if uncertain)
- Amended regulation (cite: original + amendment + effective date)
- New regulatory guidance (cite: regulator + guidance + date)
- Enforcement trend shift (cite: enforcement action or public statement)

This analysis serves a strategic purpose: organizations facing regulatory change triggers
can defend a gap as "recently identified and in remediation" — whereas gaps predating
applicable law by years face greater scrutiny.

**10b. Organizational Change Drivers:**

Identify whether organizational changes created policy gaps:
- Merger or acquisition (acquired company policies not yet integrated)
- New business line or product (existing policy didn't contemplate new activity)
- Geographic expansion (existing policy doesn't cover new jurisdiction)
- Technology adoption (existing policy predates AI, cloud, or remote work)
- Headcount threshold crossed (law applies above 50 / 250 / 1,000 employees)

**10c. Policy Lifecycle Failure:**

Identify gaps from inadequate policy management:
- No scheduled review cadence (most dangerous — regulatory changes go unnoticed)
- Policy owner turnover without handoff (orphaned policies deteriorate)
- No version control (unclear which version is current)
- No sunset / retirement process (obsolete policies create confusion)

### Step 11: Prioritize and Build the Remediation Roadmap

Translate the Policy Gap Register into an actionable remediation roadmap.

**Priority Tiers:**

| Tier | Score / Criteria | Timeline | Example |
|------|------------------|----------|---------|
| **IMMEDIATE** | Residual ≥ 15 (CRITICAL) OR policy directly required by active enforcement focus | 0–30 days | SAR procedure absent; active FinCEN examination scheduled |
| **NEAR-TERM** | Residual 9–14 (HIGH) OR policy cited in prior audit finding or enforcement notice | 31–90 days | Data Retention Policy 5 years old; GDPR storage limitation changes since adoption |
| **BACKGROUND** | Residual 5–8 (MEDIUM) OR policy exists but adequacy improvements needed | 91–180 days | Travel & Expense Policy currency improvement; AML training refresh |
| **WATCH** | Residual 1–4 (LOW) OR future regulatory change will require update | Next annual review cycle | UK GDPR policy update for DUA Act 2025; CSRD applicability in 2–3 years |

**Remediation roadmap format for each gap:**

```
GAP ID: GAP-PRV-003
Gap: Data Subject Rights Procedure — absent for California residents (CCPA)
Tier: IMMEDIATE
Timeline: 30 days from assessment date
Owner: Chief Privacy Officer / General Counsel
Actions:
  1. Draft California-specific DSR intake form and acknowledgment template (Days 1–10)
  2. Legal review of CPRA compliance: confirm 45-day response SLA, opt-out
     linkages, deletion workflow, contractor notice requirements (Days 5–15)
  3. Train customer support team on procedure (Days 15–25)
  4. Publish to privacy center and intranet (Day 28)
  5. Board/CCO sign-off (Day 30)
Success Metric: Published procedure + 100% customer support training completion
  + test submission of CCPA rights request + documented response within 45 days
Effort Estimate: 40–60 hours (legal + operations + training)
Dependencies: Legal counsel (CPRA expertise), operations team (intake system)
```

**11b. Investment Case:**

For board presentation, aggregate the remediation roadmap into an investment case:

| Tier | Number of Gaps | Total Effort Est. | Estimated Timeline | Risk Reduction |
|------|----------------|-------------------|--------------------|---------------|
| IMMEDIATE | [N] | [hours] | 30 days | CRITICAL → MEDIUM |
| NEAR-TERM | [N] | [hours] | 90 days | HIGH → LOW |
| BACKGROUND | [N] | [hours] | 180 days | MEDIUM → LOW |
| **Total** | **[N]** | **[hours]** | **180 days** | **[Overall risk tier]** |

Include:
- External counsel cost estimate (if specialist engagement required)
- Internal resource hours (legal, compliance, HR, IT, operations)
- Technology/tooling costs (LMS platform, policy management software)
- Certification costs (if applicable — ISO 37301 certification audit fees)

### Step 12: Board Governance and Accountability Assessment

Assess the policy governance framework itself — not just individual policy content.

**12a. Board/Leadership Accountability:**

| Element | Present | Quality | Evidence |
|---------|---------|---------|---------|
| Board-approved policy governance framework | | 1–5 | |
| Named policy owner for each domain | | 1–5 | |
| Regular CCO/DPO/CISO reporting to board | | 1–5 | |
| Board review of policy gap register | | 1–5 | |
| Board-approved policy review schedule | | 1–5 | |
| Documented risk appetite for policy gaps | | 1–5 | |

**12b. Policy Lifecycle Management:**

Assess whether the organization has a functioning policy lifecycle:
- Policy inventory maintained and current (yes / partial / no)
- Defined review cadence per policy (all / some / none)
- Trigger-based review process for regulatory changes (yes / partial / no)
- Version control and retirement process (yes / partial / no)
- Policy conflict resolution process (two contradictory policies) (yes / no)

**12c. Board Decisions Required:**

Present the following for board decision (adapt to specific findings):
1. Accept CRITICAL residual policy risk in [Domain] until [Date], OR authorize
   immediate remediation budget of [$X] and [N] hours internal resources?
2. Approve new policy governance framework with named domain owners and quarterly
   CCO reporting to Board Risk Committee?
3. Approve annual policy review schedule with the following categories and cadences:
   - Tier 1 (highly regulated: privacy, cybersecurity, AML): annual
   - Tier 2 (regulatory: anti-corruption, employment, financial reporting): biennial
   - Tier 3 (general: ESG, procurement, operational): triennial with trigger-based review

---

## Policy Requirements Reference Library

This reference library maps required policies to applicable regulatory frameworks across
8 domains. Use this as the baseline for Step 4 (Regulatory Obligation Mapping).

### Domain 1: Privacy and Data Protection

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements | [JURISDICTION-SPECIFIC] Notes |
|-------------|------------------------|---------------------|-----------------|-------------------------------|
| Privacy Policy / Privacy Notice | GDPR Art. 13/14; CCPA §1798.100; LGPD Art. 9; DPDP Act 2023 | Any personal data processing | Data types collected, purpose, legal basis, rights, retention, contact | [EU] Layered privacy notice required (EDPB Guidelines 2018); [CA] "Do Not Sell" / "Do Not Share" link mandatory |
| Data Retention and Deletion Policy | GDPR Art. 5(1)(e); CCPA §1798.105; LGPD Art. 16; HIPAA §164.530(j) | Any personal data processing | Retention schedule per data category; deletion triggers; legal hold exceptions | [EU] "Storage limitation" principle; specific hold cannot exceed purpose; [US-Health] HIPAA 6-year retention for PHI |
| Data Subject Rights Procedure | GDPR Arts. 15–22; CCPA §§1798.100–115; CPRA Arts. 1798.110–135 | EU/UK/CA/BR personal data | Access, rectification, erasure, portability, objection, automated decision opt-out | [EU] 30-day + 2-month extension SLA; [CA] 45-day + 45-day extension; [VERIFY CA timeline] |
| Data Protection Impact Assessment (DPIA) Procedure | GDPR Art. 35; UK GDPR Art. 35; EDPB Guidelines 09/2022 | High-risk processing, new technology, profiling, special categories | DPIA trigger criteria; methodology (consultation, risk assessment); DPO involvement | [EU] Prior consultation with supervisory authority if high residual risk (Art. 36) |
| Cross-Border Data Transfer Policy | GDPR Chapter V; UK GDPR Chapter V; LGPD Chapter V; PIPL Arts. 38–43 | Any international personal data transfer | Transfer mechanism selection (SCCs, BCRs, adequacy decision); TIA requirement | [EU] SCCs 2021 Modules 1–4; Schrems II TIA required; [UK] IDTA March 2022; [CN] PIPL Art. 38 government approval for key sectors |
| Data Breach Incident Response Procedure | GDPR Arts. 33–34; UK GDPR; CCPA §1798.150; LGPD Art. 48; AU Privacy Act NDB | Any breach of personal data | Breach detection, severity assessment, notification timelines, regulator reporting | [EU] 72-hour DPA notification; [AU] 30 days; [CA] CCPA: "expedient" = 72 hours in practice; [VERIFY] |
| Cookie and Tracking Technology Policy | ePrivacy Directive Art. 5(3); GDPR consent; CCPA GPC signal; CPRA | Any website with EU/CA users | Cookie categories; consent mechanism; GPC signal compliance | [EU] Prior consent for non-essential; [CA] GPC signal = opt-out right; CNIL analytics exemption July 2025 |
| Data Processing Agreements / Vendor Assessment Policy | GDPR Art. 28; CCPA §1798.140(ag) contractor requirements | Any third-party data processor | DPA requirements; processor screening; sub-processor clause; audit rights | [EU] GDPR Art. 28(3) mandatory 10 provisions; [VERIFY latest EDPB guidance on DPA adequacy] |
| Record of Processing Activities (ROPA) Procedure | GDPR Art. 30; UK GDPR Art. 30 | Organizations >250 employees OR high-risk processing | Maintain ROPA; review cadence; DPO involvement | [EU] Supervisory authority may request ROPA on demand; [UK] ICO expects ROPA even for smaller orgs |
| AI and Automated Decision-Making Policy | GDPR Art. 22; EU AI Act 2024/1689; NYC Local Law 144; CO SB 24-205 | Any automated/AI-assisted decisions affecting individuals | Opt-out rights; human review process; bias audit (NYC); meaningful explanation | [EU] AI Act requires high-risk system documentation + conformity assessment by Aug 2026; [US-NYC] Annual bias audit mandatory for AEDT |

### Domain 2: Information Security and Cybersecurity

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements |
|-------------|------------------------|---------------------|-----------------|
| Information Security Policy | ISO 27001:2022 Clause 5.2; NIS2 Art. 21(2)(a); HIPAA §164.308(a)(1) | Any organization with IT systems | Scope, objectives, risk management approach, roles, review cadence |
| Access Control Policy | ISO 27001:2022 A.5.15–5.18; NIS2 Art. 21(2)(j); HIPAA §164.312(a) | Any organization with IT systems | Least-privilege principle; role-based access; privileged access controls; review frequency |
| Vulnerability Management Policy | NIS2 Art. 21(2)(e); NIST CSF PR.IP-12; HIPAA §164.308(a)(1) | Any organization with external-facing systems | Scanning cadence; CVSS severity thresholds; patching SLAs; zero-day response |
| Incident Response Policy | NIS2 Art. 21(2)(b); ISO 27001:2022 A.5.25–5.26; HIPAA §164.308(a)(6) | Any organization (mandatory for NIS2-scope) | Incident classification; response team; escalation; regulator notification timelines |
| Cryptography Policy | NIS2 Art. 21(2)(f); ISO 27001:2022 A.8.24; HIPAA §164.312(a)(2)(iv) | Any organization encrypting personal or sensitive data | Approved algorithms (AES-256, TLS 1.3+, RSA-2048+); key management; prohibited algorithms (MD5, SHA-1, RC4) |
| Business Continuity / Disaster Recovery Policy | NIS2 Art. 21(2)(b); ISO 22301; HIPAA §164.308(a)(7); DORA Art. 11 | Any regulated entity; NIS2 essential/important entities | RTO/RPO targets; backup requirements; BCP testing cadence; succession planning |
| Third-Party / Supplier Security Policy | NIS2 Art. 21(2)(d); ISO 27001:2022 A.5.19–5.22; NIST CSF GV.SC | Any organization using third-party IT services | Vendor risk tier; security questionnaire; contractual security requirements; incident notification; right to audit |
| Change Management Policy | NIS2 Art. 21; ISO 27001:2022 A.8.32; SOX ITGC | IT systems affecting financial reporting or critical services | Change classification; approval workflow; testing requirements; rollback plan |
| Penetration Testing Policy | NIS2 Art. 21(2)(e); PCI DSS Req. 11; NYDFS 23 NYCRR §500.5 | Financial, healthcare, NIS2 entities; PCI scope | Testing frequency; scope; use of qualified testers; remediation tracking |
| Security Awareness and Training Policy | NIS2 Art. 21(2)(g); HIPAA §164.308(a)(5); ISO 27001:2022 A.6.3 | Any organization with IT systems | Minimum training requirements; frequency; phishing simulation; role-based depth |
| Physical and Environmental Security Policy | ISO 27001:2022 A.7.1–7.14; NIS2 Art. 21 | Any organization with physical infrastructure | Clean desk; visitor access; CCTV retention; data center physical controls |
| Network Security Policy | NIS2 Art. 21; ISO 27001:2022 A.8.20–8.23; NIST CSF PR.AC | Organizations with network infrastructure | Segmentation; firewall rules; remote access (VPN/Zero Trust); Wi-Fi security |

### Domain 3: Anti-Corruption and Ethical Conduct

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements |
|-------------|------------------------|---------------------|-----------------|
| Anti-Corruption and Anti-Bribery Policy | FCPA 15 U.S.C. §78dd-1; UK Bribery Act 2010 s.7; OECD Convention; Brazilian Clean Company Act | Any organization with international operations or UK nexus | Prohibition on improper payments; government official definition; agent/third-party obligations; facilitation payments position |
| Code of Conduct / Code of Ethics | DOJ ECCP Sept 2024; US Sentencing Guidelines §8B2.1; ISO 37301:2021 Clause 8.1 | All organizations | Expected standards of behavior; conflict of interest; confidentiality; reporting obligations |
| Gifts, Entertainment, and Hospitality Policy | FCPA; UK Bribery Act; EU member state implementations | Any organization with government or commercial relationships | Per-gift and annual thresholds; pre-approval requirements; government official restrictions; hospitality documentation |
| Third-Party Due Diligence Policy | DOJ FCPA guidance; UK MoJ Bribery Act guidance; ISO 37301:2021 Clause 8.3 | Any organization using agents, intermediaries, or JV partners in high-risk markets | Risk-based tiering (Level 1/2/3); questionnaire requirements; adverse news search; renewal cadence |
| Whistleblower / Ethics Reporting Policy | EU Whistleblower Protection Directive 2019/1937; SOX §806; Dodd-Frank Rule 21F; UK PIDA 1998 | All organizations (EU: organizations with 50+ employees mandatory channel) | Reporting channels; anonymity options; non-retaliation prohibition; investigation process | [EU] Organizations 50–249 employees: Dec 2023 deadline; 250+ employees: Dec 2021 [VERIFY national transpositions] |
| Political Contributions Policy | FCPA; various state campaign finance laws; UK Political Parties, Elections and Referendums Act 2000 | Organizations with any political activity | Prohibition or process for corporate political contributions; PAC separation |
| Conflict of Interest Policy | DOJ ECCP; ISO 37301:2021; state fiduciary duties | All organizations | Disclosure process; recusal requirements; annual declaration; outside employment / board seat conflicts |
| Government Official Interaction Policy | FCPA §§78dd-1 to 78dd-3; UK Bribery Act ss.1–6; local anti-corruption laws | Any organization with government contracts or regulated operations | Definition of "foreign official"; permissible vs. prohibited interactions; pre-approval workflow; documentation requirements |

### Domain 4: Financial Crime (AML / KYC / Sanctions)

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements |
|-------------|------------------------|---------------------|-----------------|
| Anti-Money Laundering (AML) Program Policy | BSA 31 U.S.C. §5318(h); EU AMLR 2024/1624; UK MLR 2017 SI 2017/692 | Banks, MSBs, broker-dealers, investment advisers (US); all AMLR-covered entities | Four pillars (written program, BSA officer, training, independent testing); risk-based approach |
| Customer Due Diligence (CDD) / Know Your Customer (KYC) Policy | BSA 31 C.F.R. §1010.230; FATF R.10; EU AMLR Ch. 3; UK MLR 2017 Reg. 28 | All AML-covered entities | Customer identification; beneficial ownership (25% threshold); risk rating; ongoing monitoring |
| Enhanced Due Diligence (EDD) Policy | FATF R.12 (PEPs); BSA §1010.230(e); EU AMLR Arts. 29–30 | Entities with PEPs, high-risk countries, complex structures | PEP identification; three-tier EDD (domestic/foreign/international); de-PEPing process |
| Suspicious Activity Reporting (SAR) Procedure | BSA 31 C.F.R. §1020.320; FinCEN Form 111; EU AMLR Art. 69 | All BSA-covered entities | SAR trigger criteria; 30-day (initial) / 60-day (extended) filing deadlines; tipping-off prohibition; documentation |
| Currency Transaction Reporting (CTR) Procedure | BSA 31 C.F.R. §1010.311; FinCEN Form 112 | US banks and MSBs | $10K threshold; aggregation rules; structure detection; CTR completion requirements |
| OFAC / Sanctions Screening Policy | OFAC SDN list; Executive Orders; EU restrictive measures; UK Financial Sanctions | Any entity conducting business / financial transactions | Real-time screening at onboarding + transaction; 50% rule (indirect ownership through designated persons); blocked asset procedures |
| Politically Exposed Person (PEP) Policy | FATF R.12; EU AMLR Arts. 29–30; UK MLR 2017 Reg. 35 | Any AML-covered entity | PEP definition (domestic + foreign + international); risk management; enhanced monitoring; de-PEPing timeline (12–18 months post-role) |
| Record Retention Policy (BSA) | BSA 31 C.F.R. §1010.430 | US BSA-covered entities | 5-year retention for CDD records, SARs, and supporting documentation |

### Domain 5: Employment and Labor

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements |
|-------------|------------------------|---------------------|-----------------|
| Equal Employment Opportunity (EEO) Policy | Title VII (42 U.S.C. §2000e); ADA 42 U.S.C. §12101; ADEA 29 U.S.C. §621; EU Equal Treatment Directive | Organizations with employees in applicable jurisdictions | Protected characteristics; complaint procedure; investigation process; poster requirements |
| Harassment and Discrimination Prevention Policy | EEOC guidance; Title VII; state equivalents (CA FEHA; NY HRL); EU Directive 2000/78/EC | All employers | Definition of harassment; prohibited conduct examples; reporting process; investigation; non-retaliation |
| Whistleblower / Non-Retaliation Policy | SOX §806; Dodd-Frank Rule 21F; OSHA Section 11(c); EU Directive 2019/1937 | All employers (especially SEC reporters) | Channels; non-retaliation; anonymity; investigation; escalation to board audit committee |
| Worker Classification Policy (Employee vs. Contractor) | IRS Rev. Rul. 87-41; California AB 5 / ABC test; FLSA economic reality test; EU Platform Work Directive 2024 | Employers using independent contractors | Classification criteria (behavioral, financial, type of relationship); misclassification risk scoring; reclassification protocol |
| Wage and Hour / Working Time Policy | FLSA 29 U.S.C. §§201–219; state wage laws; EU Working Time Directive 2003/88/EC | All employers | Overtime eligibility (FLSA $684/week salary threshold [VERIFY current FLSA threshold post-litigation]); recordkeeping; break requirements |
| Workplace Health and Safety Policy | OSHA 29 U.S.C. §654; UK Health and Safety at Work Act 1974; EU Framework Directive 89/391/EEC | All employers with physical workplaces | General duty clause compliance; hazard identification; incident reporting (OSHA 300 log); training |
| Employee Data Privacy Policy | GDPR Arts. 6(1)(b)/9 (employment); UK GDPR; CCPA employee notices | Any employer processing employee personal data | Employee personal data scope; basis for processing; monitoring disclosure; records retention |
| AI-Assisted Hiring Policy | NYC Local Law 144 (AEDT bias audit); CO SB 24-205 (effective June 2026); EU AI Act Annex III | NYC employers using automated hiring tools; CO employers (2026+) | Annual bias audit (NYC); data notice to candidates; opt-out rights; impact ratio reporting |
| Remote Work / Flexible Working Policy | FLSA off-duty connectivity; EU telework framework; UK ERA 2023 flexible working right | Employers with remote workers | Working hours; expense reimbursement; equipment policy; data security for remote access; eligibility |

### Domain 6: Financial Reporting and Internal Controls

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements |
|-------------|------------------------|---------------------|-----------------|
| Records Retention and Destruction Policy | SOX §802 (7-year for audit work papers); FLSA (3 years payroll); IRS (3–7 years); SEC Rule 17a-4 | SEC registrants; all organizations with tax / audit obligations | Retention schedules by record type; litigation hold process; authorized destruction; metadata retention |
| Conflict of Interest and Related Party Policy | SOX §406 (Code of Ethics disclosure); SEC Form 8-K disclosure; NYSE/NASDAQ listing requirements | SEC registrants; listed companies | Board + executive disclosure; related-party transaction approval; audit committee review |
| Insider Trading Policy | SEC §10(b) and Rule 10b-5; SEC Rule 10b5-1; FINRA rules | Any organization with material non-public information | Trading blackout windows; pre-clearance for executives; 10b5-1 plan requirements; training |
| Expense and Travel Reimbursement Policy | FCPA (proper accounting provisions); SOX internal controls; IRS accountable plan rules | All organizations | Documented business purpose; approval thresholds; prohibited expense categories; non-reimbursable items |
| Anti-Fraud Policy | COSO ERM; SOX §301 (audit committee whistleblower); Fraud Act 2006 (UK) | All organizations | Definition of fraud; reporting channel; investigation; board audit committee escalation; clawback provisions (SOX §304, Dodd-Frank §954) |
| Financial Disclosure / Certification Procedure | SOX §302 (quarterly/annual CEO/CFO certification); SOX §906 (criminal certification) | SEC registrants | Internal disclosure controls documentation; sub-certifications; ICFR testing scope |
| Clawback / Compensation Recovery Policy | SEC Rule 10D-1 (clawback rule, effective Oct 2023); Dodd-Frank §954; NASDAQ/NYSE listing requirements | NASDAQ/NYSE listed companies (mandatory as of Oct 2023) | Recovery trigger (material restatement); 3-year lookback; covered officers; no indemnification |

### Domain 7: ESG, Supply Chain, and Sustainability

| Policy Name | Required/Recommended By | Jurisdiction Trigger | Key Requirements |
|-------------|------------------------|---------------------|-----------------|
| Modern Slavery and Human Trafficking Statement | UK Modern Slavery Act 2015 s.54; Australia Modern Slavery Act 2018 (Cth); CA SB 657 | UK/AU organizations >£36M/AUD 100M turnover or CA suppliers | Annual statement; 6 topic areas (structure, business, supply chains, due diligence, risk indicators, training); board approval and sign-off |
| Supply Chain Due Diligence Policy | German LkSG (effective Jan 2023, ≥1,000 employees from June 2024); EU CSDDD Directive 2024/1760 (phased 2027–2029); Norwegian Transparency Act 2021 | German companies at thresholds; EU companies (phased by size) | Risk analysis; preventive measures; grievance mechanism; reporting; remediation | [DE] LkSG requires public annual report; grievance mechanism established; [EU] CSDDD: Tier 1 direct suppliers and selected Tier 2 |
| Environmental and Climate Policy | EU Taxonomy Regulation 2020/852; CSRD Directive 2022/2464 (ESRS E1–E5); SEC Climate Disclosure Rules [VERIFY current status] | Large EU companies (CSRD); SEC registrants | GHG scope 1/2/3 accounting; climate targets; transition plan; TCFD-aligned disclosure |
| Responsible AI / Ethical Technology Policy | EU AI Act 2024/1689; NIST AI RMF 1.0; ISO/IEC 42001:2023 | Organizations deploying AI systems | AI system inventory; risk classification; prohibited use cases; human oversight; bias testing |
| Diversity, Equity, and Inclusion Policy | EU Pay Transparency Directive 2023/970; CA pay data reporting SB 1162; Norway gender balance reporting | EU employers (250+ employees from June 2026); large CA employers; certain NO employers | Pay gap reporting; diversity targets; board gender balance requirements |

### Domain 8: Sector-Specific Policy Requirements

| Sector | Policy Name | Required By | Key Requirements |
|--------|-------------|-------------|-----------------|
| **Healthcare (US)** | HIPAA Privacy Rule Policy | 45 C.F.R. Part 164 Subpart E | Minimum necessary standard; PHI uses and disclosures; patient rights; Notice of Privacy Practices |
| **Healthcare (US)** | HIPAA Security Rule Policies | 45 C.F.R. §§164.308–316 | Administrative safeguards (10 required + addressable); physical safeguards; technical safeguards; policies required for each standard |
| **Healthcare (US)** | HIPAA Breach Notification Procedure | 45 C.F.R. §§164.400–414 | 60-day notification to HHS; business associate breach notification; media notice for >500 in state |
| **Financial Services (US)** | GLBA Information Security Program (Written ISP) | GLBA Safeguards Rule 16 C.F.R. §314.4 | Qualified individual; risk assessment; 9 administrative/technical/physical safeguard categories; annual board reporting |
| **Financial Services (EU)** | ICT Risk Management Policy | DORA Reg. 2022/2554 Arts. 5–16 | ICT risk management framework; internal audit function; business continuity testing; ICT incident classification |
| **Defense (US)** | Cybersecurity Maturity Model Certification Policies | CMMC 2.0 (32 C.F.R. Part 170); NIST SP 800-171 | 110 security requirements; System Security Plan (SSP) required; Plan of Action & Milestones (POAM) |
| **Financial Services (US)** | NYDFS Cybersecurity Policy | 23 NYCRR Part 500 (Nov 2023 amendments) | Penetration testing; vulnerability scanning; asset management; CISO designation; board reporting; Class A company requirements |
| **Payment Card** | PCI DSS Information Security Policy | PCI DSS v4.0 Req. 12 | Comprehensive information security policy; annual review; awareness program; all 12 requirements documented |
| **Energy/Utilities (EU)** | NIS2 Sector-Specific Policies | NIS2 Directive 2022/2555 Annex I; ACER sector guidance | All 10 Art. 21 measures; essential entity obligations; cross-border coordination with national CSIRT |

---

## Gap Classification System

### CRITICAL — Residual Score ≥ 15

**Definition:** Policy is absent or so materially deficient that a regulatory examination
would find an enforcement-ready deficiency. Immediate action required.

**Characteristics:**
- Regulatory framework explicitly requires this policy AND it is absent (Gap Type 1)
- OR Policy exists but conflicts with current law in a way creating immediate legal exposure
  (Gap Type 3)
- OR Policy exists on paper but is entirely unimplemented (DE≥3, OE=1) in an active
  enforcement domain

**Regulatory analogy:** "Significant weakness" in a bank examination; basis for formal
enforcement action; criminal exposure possible.

**Required action:** Escalate to board/CEO within 48 hours; engage qualified legal counsel;
interim remediation plan within 7 days; substantive remediation within 30 days.

### HIGH — Residual Score 9–14

**Definition:** Policy materially inadequate or significantly outdated; elevated enforcement
exposure. Near-term remediation required.

**Characteristics:**
- Policy exists but missing fundamental provisions required under applicable regulation
- Policy predates material regulatory changes by > 18 months (fast-moving areas: privacy,
  AI, cybersecurity, financial crime)
- Design-Execution Gap ≥ 2 (well-written but largely unimplemented)
- In a current regulatory enforcement priority area

**Regulatory analogy:** "Identified deficiency" in examination; regulators will expect
documented remediation plan; standalone finding in audit report.

**Required action:** Notify CCO/GC within 5 business days; 30–60 day remediation; interim
monitoring measures while remediating.

### MEDIUM — Residual Score 5–8

**Definition:** Policy adequately covers core requirements but has notable gaps in scope,
specificity, or operational effectiveness.

**Characteristics:**
- Policy covers the required topic but missing supporting elements (e.g., retention
  schedule absent from privacy policy; training program exists but no attestation)
- Policy modestly outdated (12–18 months since last review) in a moderately active area
- Design-Execution Gap = 1 (slight implementation lag)

**Regulatory analogy:** "Observation" in examination; low probability of standalone
enforcement action; expected to be addressed in next annual review.

**Required action:** Document remediation plan with 90-day target; no emergency escalation
required.

### LOW — Residual Score 1–4

**Definition:** Policy substantially complete; minor improvements needed.

**Characteristics:**
- Policy well-designed and operationally effective; minor drafting improvements possible
- Slight currency gap (6–12 months since review in stable regulatory area)
- No active regulatory enforcement focus

**Regulatory analogy:** Management letter comment; "housekeeping" finding; acceptable
risk given other controls.

**Required action:** Add to next scheduled policy review cycle; document as known risk.

---

## Prioritization Framework

### IMMEDIATE (0–30 Days)

Applicable when:
- Residual score ≥ 15 (CRITICAL) in any domain
- Active regulatory examination, audit, or investigation underway
- Policy gap directly cited in prior audit finding or enforcement notice
- Regulatory effective date has passed and policy remains non-compliant
- Criminal exposure identified (AML/FCPA/sanctions)

*Board-level decision required to proceed or accept risk.*

### NEAR-TERM (31–90 Days)

Applicable when:
- Residual score 9–14 (HIGH)
- Policy gap creates material enforcement exposure in an active enforcement domain
- Regulatory effective date approaching within 90 days
- M&A integration requires policy harmonization before close or within integration period
- Certification deadline requires policy documentation within 90 days

*CCO/GC decision; board notification recommended.*

### BACKGROUND (91–180 Days)

Applicable when:
- Residual score 5–8 (MEDIUM)
- Policy improvement needed but no immediate enforcement trigger
- Regulatory change in future (6–18 months) will require update
- Training / attestation improvements required but current compliance demonstrated

*CCO/compliance team ownership; periodic progress reporting.*

### WATCH (Next Annual Review)

Applicable when:
- Residual score 1–4 (LOW)
- Future regulatory development will require update (monitor regulatory change tracker)
- Policy is effective; currency check sufficient in annual review cycle

*Compliance team monitoring; no escalation needed.*

---

## Citation Quality Gates

Run these five gates silently before delivering any finding in the policy gap register.
If any gate fails, revise before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **1. Source Gate** | Every policy gap finding cites a specific regulatory provision, guidance document, or recognized standard requiring the policy | Add citation or mark "[UNVERIFIED — policy requirement not traced to specific authority]" |
| **2. Currency Gate** | Every cited provision checked for amendments, repeal, or supersession since the date cited | Flag "[CHECK CURRENCY — verify this provision was not amended]" with effective date |
| **3. Jurisdiction Gate** | Policy requirement applies to this organization given its jurisdiction, size, sector, and activities | Flag "[JURISDICTION-SPECIFIC — verify applicability to this organization]" |
| **4. Adequacy Gate** | Assessment of policy adequacy is based on documented evidence (policy text, training records, attestation data) not assumption | Where evidence is absent, mark "[VERIFY — assumed adequacy level; requires confirmation]" |
| **5. Confidence Gate** | Confidence scoring explicitly states evidence basis; uncertainty is surfaced, not hidden | Add confidence qualifier (VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED) to every finding |

---

## Self-Interrogation for CRITICAL and HIGH Gaps

For every CRITICAL or HIGH gap, apply this 3-pass adversarial review (per Step 8 above).

**Pass 1 — Policy Chain Integrity**

Does the CRITICAL/HIGH classification follow logically from the inherent risk score and
policy adequacy evidence?

> *Ask:* What is the strongest argument that this gap is actually MEDIUM, not CRITICAL/HIGH?
> If no good counter-argument exists, the classification holds.
> If a plausible counter-argument exists, lower the confidence level and note it.

**Pass 2 — Compensating Controls**

Are there any policies, processes, or governance mechanisms that compensate for this gap
and should lower the residual score?

Common compensating factors:
- Strong DPO function (compensates for minor privacy policy currency gaps)
- Robust third-party vendor contracts (compensates for weak internal supply chain policy)
- Active audit committee with quarterly CCO briefings (compensates for whistleblower policy gaps)
- Manual approval workflows (compensates for absent formal policy if documented and consistent)

> *Ask:* Would a regulator examining this gap accept [specific compensating control] as
> partial mitigation? If yes, lower OE by 1 level and recalculate.

**Pass 3 — Enforcement Reality Check**

Is this gap a documented regulatory enforcement priority for this industry and jurisdiction?

> *Evidence required:* Cite at least one enforcement action, regulatory guidance, or public
> examination finding supporting the CRITICAL classification in this domain and jurisdiction.
> If no enforcement precedent exists, lower from CRITICAL to HIGH and note "[VERIFY
> enforcement pattern — no specific precedent found]".

---

## Confidence Scoring

Assign a confidence level to every policy gap assessment based on the quality of underlying
evidence.

| Level | Score Range | Definition | Prescribed Action |
|-------|-------------|-----------|-------------------|
| **VERIFIED** | 0.90–1.00 | Evidence independently confirmed: policy text reviewed, training records inspected, attestation data obtained | State with confidence; no qualification needed |
| **LIKELY** | 0.70–0.89 | Evidence from reliable source (prior audit, compliance memo, documented review) but not independently verified | State with brief caveat: "Based on [source]; recommend verification" |
| **POSSIBLE** | 0.50–0.69 | Good-faith inference from available indicators; not fully confirmed | State with explicit reasoning and contra-indicators; flag for verification |
| **VERIFY** | 0.30–0.49 | Assumption made; placeholder pending information gathering | Flag prominently as "[VERIFY]" before board presentation |
| **ASSUMED** | < 0.30 | No evidence; placeholder based on organizational profile defaults | Do not include in board presentation without verification; internal working assumption only |

**Default Confidence Levels by Evidence Source:**
- Policy text reviewed by AI during session: LIKELY (0.75)
- Policy existence confirmed by inventory list without review: POSSIBLE (0.55)
- Policy reported by client without documentation: VERIFY (0.40)
- Policy assumed absent based on typical organizational profile: ASSUMED (0.25)

---

## Glass Box Audit Trail

Every policy gap assessment must include a YAML audit trail enabling an auditor, regulator,
or board member to trace every decision to its supporting evidence.

```yaml
glass_box:
  skill_name: "legalcode-policy-gap-analysis"
  assessment_date: "[YYYY-MM-DD]"
  assessed_by: "[Role — AI-assisted; must be validated by qualified professional]"
  organization: "[Name or anonymized identifier]"
  operating_mode: "[Mode from Step 2]"
  jurisdictions_assessed: "[List]"
  period_covered: "[From — To]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/policy-gap-research.md or Not created]"
  total_gaps_identified: "[N CRITICAL / N HIGH / N MEDIUM / N LOW]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"

  policy_domain_assessments:
    - domain: "[Policy Domain Name]"
      policies_assessed: [N]
      inherent_risk_score: [N]
      inherent_likelihood: [1-5]
      inherent_likelihood_rationale: |
        [Specific regulatory citation + enforcement data + [VERIFY] markers]
      inherent_impact: [1-5]
      inherent_impact_rationale: |
        [Specific penalty provision + precedent + [VERIFY] markers]
      worst_policy_adequacy_score: [1-5]
      design_effectiveness: [1-5]
      operational_effectiveness: [1-5]
      design_execution_gap: [DE - OE]
      gap_multiplier: [1.00 or 1.25]
      residual_risk_score: [calculated]
      residual_risk_tier: "[CRITICAL / HIGH / MEDIUM / LOW]"
      pass_1_integrity_check: |
        [Does classification follow from evidence? Strongest counter-argument?]
      pass_2_compensating_controls: |
        [Any compensating policies or governance mechanisms? Impact on score?]
      pass_3_enforcement_context: |
        [Enforcement precedent cited; enforcement focus confirmed or [VERIFY]]
      confidence_score: [0.00-1.00]
      confidence_level: "[VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED]"
      confidence_rationale: |
        [What evidence was reviewed; what was assumed; what needs verification]
      key_gaps:
        - gap_id: "GAP-[DOMAIN]-[N]"
          type: [1 / 2 / 3]
          description: "[Specific gap description]"
          tier: "[CRITICAL / HIGH / MEDIUM / LOW]"
          remediation_owner: "[Role]"
          target_days: [N]

  assumptions:
    - "[Assumption 1 — what was assumed and why]"
    - "[Assumption 2]"

  limitations:
    - "[Scope limitation 1]"
    - "[What was not assessed]"

  reviewer_note: "AI-assisted — all CRITICAL and HIGH findings require validation
    by qualified legal counsel and compliance professionals before board presentation."
```

---

## Anti-Patterns for Policy Gap Analysis

What NOT to do when conducting a policy gap analysis:

1. **"Policy exists" equals compliance** — The most dangerous anti-pattern. Treating the
   existence of a policy document as evidence of compliance. Regulators explicitly test
   whether policies are implemented, trained, and followed — a shelf-ware policy can
   worsen enforcement outcomes by showing management knew the requirement but ignored
   operationalization.

2. **Averaging adequacy scores across a domain** — If a domain has five required policies
   and four are excellent (DE=4, OE=4) but one is absent (DE=1, OE=1), the domain score
   is CRITICAL — not the average of 3.4. Use the MINIMUM score rule consistently.

3. **Treating "we have a code of conduct" as covering all ethical conduct requirements** —
   A code of conduct is not an anti-corruption policy, gifts/entertainment policy,
   conflicts of interest policy, or whistleblower policy. Each requires standalone treatment
   under regulatory scrutiny.

4. **Ignoring policy conflicts (Gap Type 3)** — Many organizations focus exclusively on
   absent or incomplete policies and miss existing policies that actively contradict
   applicable law. A confidentiality agreement prohibiting external reporting may violate
   SEC Rule 21F (anti-retaliation); a data sharing policy may contradict GDPR Art. 5.

5. **Currency assessment by year only** — A policy reviewed last year may be critically
   outdated if the review predates a major regulatory change (e.g., EDPB consent guidance
   update, FTC Safeguards Rule effective date, NIS2 transposition). Assess currency by
   regulatory event, not calendar year.

6. **Skipping the enforcement context check** — Classifying every gap as CRITICAL based
   on regulatory text without checking whether regulators actually enforce this requirement.
   Paper requirements with low enforcement priority should be MEDIUM, not CRITICAL. The
   self-interrogation Pass 3 exists to prevent over-classification.

7. **One policy for all jurisdictions** — Treating a US privacy policy as covering GDPR
   requirements, or an EU-compliant policy as covering CCPA. The two frameworks have
   fundamentally different consent models (opt-in vs. opt-out) and rights frameworks.
   Multi-jurisdiction organizations need jurisdiction-specific supplements or layered policies.

8. **Ignoring compensating controls** — Classifying a policy gap as CRITICAL without
   considering whether other processes compensate for the gap. A company without a formal
   written AML program policy may have strong de facto controls through daily monitoring
   and transaction review. Document and consider compensating controls.

9. **Board reporting without evidence validation** — Presenting CRITICAL gaps to the board
   based on assumed or VERIFY-level evidence. Board presentations require VERIFIED or LIKELY
   confidence levels. Flag VERIFY-level findings as "pending confirmation" rather than
   presenting them as confirmed deficiencies.

10. **Missing the design-execution gap** — The most common finding in regulatory enforcement
    actions is organizations with well-designed policies that simply aren't followed. A policy
    with DE=4 but OE=1 (known, documented, not operationalized) may be treated as worse
    than no policy in enforcement — it demonstrates management indifference. The
    design-execution gap multiplier (1.25×) captures this elevated risk.

11. **Not assigning policy owners** — Conducting a gap analysis and producing a remediation
    roadmap without named owners creates no accountability and results in deferral. Every
    gap must have a named owner (role + person if possible) with authority to execute.

12. **Under-scoping sector-specific requirements** — Focusing on horizontal frameworks
    (GDPR, ISO 27001) while missing sector-specific overlays. A healthcare organization
    must have all HIPAA §164.308 administrative safeguard policies in addition to general
    privacy policies. A financial institution must have GLBA, AML, and SEC-specific policies.
    The Policy Requirements Reference Library lists sector-specific requirements for this reason.

13. **Static policy review without regulatory change monitoring** — Completing the gap
    analysis and declaring the policy library "current" without establishing a regulatory
    change monitoring process. Policies become outdated within months in fast-moving areas
    (AI, privacy, financial crime). Use `legalcode-regulatory-change-tracker` to establish
    continuous monitoring.

14. **Over-engineering small organization policy libraries** — Applying enterprise-scale
    policy requirements to a 25-person startup. A small organization with limited regulatory
    exposure (no EU customers, no financial products, no regulated industry) needs a lean
    policy library covering employment, data security, and basic ethics — not 40 policies.
    Match policy scope to actual regulatory exposure.

15. **Missing the "conflicting policies" sweep** — Running the gap analysis only forward
    (what should exist but doesn't?) without checking for internal conflicts (do existing
    policies contradict each other?). Two policies from different eras may create compliance
    confusion or regulatory exposure by giving contradictory instructions.

16. **Policy gap analysis as a one-time project** — Treating the gap analysis as a project
    with an end date rather than a continuous program. The output should include a policy
    governance framework and review schedule — not just a list of gaps to close.

17. **Ignoring the human factor in operational effectiveness** — Assuming training = a
    compliance module completed. Regulators assess whether staff can actually make compliant
    decisions, not whether they clicked through an LMS module. OE assessment should include
    spot-check interview findings where available.

18. **Conflating policy with procedure** — Identifying the absence of a written procedure
    as a policy gap. Policies set principles; procedures set steps. Regulatory requirements
    sometimes mandate procedures (e.g., GDPR Art. 33 requires a documented breach
    notification procedure) rather than just policies. This skill assesses both.

19. **No review of policy exceptions and waivers** — A policy library with excellent
    adequacy scores may have a large shadow compliance problem through undocumented
    exceptions. If there is no exception management process, exceptions become de facto
    policy. Assess whether an exception management framework exists as part of the
    enforcement/attestation dimension.

20. **Skipping the board governance assessment** — Completing a detailed technical gap
    analysis but never asking whether the board has approved the policy governance framework,
    receives regular CCO updates, or has reviewed the gap register. Under DOJ ECCP and ISO
    37301:2021, board engagement with the compliance program is itself a compliance requirement.

---

## Writing Standards

Follow these standards when producing policy gap analysis outputs:

1. **Evidence-first assertions** — Every finding begins with evidence: "Policy last reviewed
   [date]; GDPR consent requirements updated [date] — policy predates change." Never assert
   a gap without citing the specific provision requiring the policy.

2. **Active voice, imperative form** — Write "Update the Data Retention Policy to add a
   retention schedule" not "The Data Retention Policy should perhaps be updated to potentially
   include a retention schedule."

3. **Specificity in gap descriptions** — "Privacy Policy does not address cross-border data
   transfer mechanisms required under GDPR Chapter V — specifically, no reference to SCCs
   2021, BCRs, or adequacy decisions; no transfer impact assessment (TIA) process documented"
   is better than "Privacy Policy has GDPR gaps."

4. **One finding per gap** — Do not bundle multiple gaps into a single finding. Separate
   GAP-PRV-001 (Privacy Policy currency) from GAP-PRV-002 (DPIA procedure absent). This
   enables precise ownership assignment and progress tracking.

5. **Confidence transparency** — Every finding must show its confidence level (VERIFIED /
   LIKELY / POSSIBLE / VERIFY / ASSUMED). Do not present ASSUMED findings as fact.

6. **Glass Box inline** — Reference the Glass Box YAML data for every CRITICAL or HIGH gap
   in the executive summary. The Glass Box is not an appendix — it is the audit trail
   supporting every finding.

7. **Regulatory citation format** — Use consistent citation: [Instrument] [Provision] ([Short
   form]). Example: GDPR Art. 35(1) (DPIA obligation for high-risk processing).

8. **[VERIFY] markers inline** — Place [VERIFY] immediately after any unconfirmed claim,
   not in a footnote. Reviewers must see it where the claim appears.

9. **Board-ready summary** — The Executive Summary must be written for a board member
   with no technical compliance background: 3–5 bullet points on critical findings,
   the risk tier, the investment case, and the decisions required. No jargon.

10. **No false precision** — When residual scores are based on ASSUMED evidence, express
    as a range: "Estimated residual risk: 12–16 (HIGH to CRITICAL depending on verification
    of [specific assumption])" rather than a precise 14.2.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When legalcode-mcp is available, use it in Step 4 (Regulatory Obligation Mapping) to:

1. Search for current versions of all cited statutes and regulations
2. Verify effective dates of amendments (especially for rapidly changing areas: AI policy,
   privacy, NIS2 transpositions)
3. Search for recent enforcement actions and examination findings in the relevant domain
   and jurisdiction — these inform inherent risk scoring and Pass 3 enforcement context
4. Confirm penalty provisions and most-recent fine levels for impact scoring

Save research results to `/tmp/legalcode-policy-gap-research.md` and note in Glass Box:
`legalcode_mcp: "Connected — research file at [path]"`

### Without legalcode-mcp

Proceed with built-in reference tables (Policy Requirements Library above) and mark all
statutory references with [VERIFY]. Note in Glass Box:
`legalcode_mcp: "Not connected — references require independent verification"`

Apply downward confidence adjustments:
- Statutory citations: LIKELY → POSSIBLE
- Penalty amounts: LIKELY → VERIFY
- Enforcement trend data: POSSIBLE → VERIFY

### Related Skills Integration

| Trigger | Invoke This Skill |
|---------|------------------|
| AML policy gaps identified | `legalcode-aml-kyc-compliance` for deep AML assessment |
| HIPAA policy gaps identified | `legalcode-hipaa-compliance-assessment` for HIPAA deep dive |
| NIS2 policy gaps identified | `legalcode-nis2-compliance-assessment` for Art. 21 assessment |
| GDPR policy gaps identified | `legalcode-dpia-generator` or `legalcode-gdpr-legal-basis-assessment` |
| Compliance program rebuild needed | `legalcode-compliance-program-builder` |
| Regulatory changes need monitoring | `legalcode-regulatory-change-tracker` |
| Risk heat map + enterprise risk view | `legalcode-compliance-risk-assessment` |

---

## Output Format Template

### 1. Executive Summary

```
## Policy Gap Analysis — Executive Summary

Organization: [Name]
Assessment Date: [Date]
Assessment Mode: [Mode]
Jurisdictions Covered: [List]
Policy Domains Assessed: [N] domains / [N] policies

### Overall Policy Library Gap Tier: [CRITICAL / HIGH / MEDIUM / LOW]

**Critical Finding(s):**
1. [GAP-DOMAIN-001] [One-sentence description] — CRITICAL — [Owner] — 30 days
2. [GAP-DOMAIN-002] [One-sentence description] — CRITICAL — [Owner] — 30 days

**Key Statistics:**
- CRITICAL gaps: [N] (requiring immediate board action)
- HIGH gaps: [N] (requiring 30–90 day remediation)
- MEDIUM gaps: [N] (90-day window)
- LOW gaps: [N] (routine review cycle)

**Investment Case:**
- Estimated remediation effort: [N] hours / $[X] external counsel
- Timeline to LOW or better: [N] months
- Primary risk reduction: [Domain] from [Tier] to [Tier]

**Board Decisions Required:**
1. Authorize $[X] / [N] hours for IMMEDIATE remediation
2. Approve policy governance framework with named domain owners
3. Approve annual policy review schedule
```

### 2. Regulatory Obligation and Policy Applicability Matrix

[Table from Step 4b — all applicable policy requirements per domain, jurisdiction,
applicability tier, penalty exposure, enforcement focus]

### 3. Policy Inventory Assessment

[Table with all policies assessed: Policy ID, Name, Last Review, DE, OE, Domain Score,
Gap Tier, Confidence]

### 4. Policy Gap Register

[Complete register from Step 9 — all gaps with ID, type, description, tier, owner,
timeline, success metric]

### 5. Policy Domain Heat Map

```
| Policy Domain          | CRITICAL | HIGH | MEDIUM | LOW | Overall Tier | Confidence |
|------------------------|----------|------|--------|-----|--------------|------------|
| Privacy & Data         | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| Information Security   | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| Financial Crime        | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| Anti-Corruption        | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| Employment / Labor     | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| Financial Reporting    | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| ESG / Supply Chain     | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| Sector-Specific        | [N]      | [N]  | [N]    | [N] | [Tier]       | [Level]    |
| **OVERALL**            | **[N]**  | **[N]** | **[N]** | **[N]** | **[Tier]** | **[Level]** |
```

### 6. Prioritized Remediation Roadmap

[Table from Step 11 — all gaps with tier, timeline, owner, actions, success metric,
effort estimate, dependencies]

### 7. Board Governance Assessment

[Assessment from Step 12 — board accountability scorecard, policy lifecycle management
assessment, board decisions required]

### 8. Glass Box Audit Trail

[YAML template from Glass Box section — populated with assessment data]

---

## Localization Notes

When adapting this skill for a specific jurisdiction:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local requirements
2. Confirm transposition status of EU directives (NIS2, Whistleblower Directive,
   CSDDD) for the specific member state — transposition timing and scope vary
3. For US state privacy laws (CA, CO, CT, TX, FL, MT, OR, NV, and 8+ more in 2025–2026):
   use `legalcode-us-state-privacy-comparison` to confirm applicability thresholds
   (consumer data thresholds, employee exemptions, commercial B2B exemptions)
4. For non-listed jurisdictions: use `legalcode-multi-jurisdiction-privacy-comparison`
   as the reference point for privacy obligations; research local AML/anti-corruption
   frameworks separately
5. Mark all locally-researched provisions with [VERIFY] and confidence scoring
6. Note in Glass Box the jurisdiction-specific research conducted and sources consulted

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis based on:
- 2-agent structural and legal research pipeline
- Agent 1 structural analysis of `legalcode-nist-csf-mapping`, `legalcode-compliance-risk-assessment`,
  `legalcode-compliance-program-builder`, and `legalcode-nis2-compliance-assessment` reference skills
- Legalcode compliance skill family patterns (Design vs. Operational Effectiveness distinction;
  MINIMUM Control Score rule; Design-Execution Gap Multiplier; 3-Pass Self-Interrogation;
  Glass Box Audit Trail; 5-level Confidence Scoring) — derived from `legalcode-compliance-risk-assessment`
- DOJ Evaluation of Corporate Compliance Programs September 2024 three-question framework
- ISO 37301:2021 Compliance Management Systems — Clause 7.5 documented information requirements
- OCEG GRC Capability Model (Red Book 3.5) policy management guidance
- GDPR Arts. 5/24/32/33/35; ePrivacy Directive Art. 5(3); NIS2 Art. 21; BSA 31 U.S.C. §5318(h);
  FCPA 15 U.S.C. §78dd-1; UK Bribery Act 2010 s.7; SOX §302/§404/§806; DORA Reg. 2022/2554;
  UK Modern Slavery Act 2015 s.54; German LkSG; EU CSDDD Directive 2024/1760
- All statutory and regulatory references carry hallucination risk and should be verified
  against authoritative sources before use in regulatory submissions or board reporting
