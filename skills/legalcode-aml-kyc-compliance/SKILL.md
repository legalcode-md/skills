---
name: legalcode-aml-kyc-compliance
description: >
  Design, assess, and gap-analyse Anti-Money Laundering and Know Your Customer compliance
  programs covering: Customer Due Diligence (CDD) and Enhanced Due Diligence (EDD)
  procedures; beneficial ownership identification (FinCEN CDD Final Rule 31 C.F.R.
  § 1010.230, Corporate Transparency Act, EU AMLD/AMLR, UK MLR 2017); sanctions
  screening (OFAC SDN/50% rule, EU Consolidated List, UK OFSI, UN Security Council);
  Politically Exposed Person (PEP) identification and risk rating; Suspicious Activity
  Report (SAR) filing procedures (30/60-day deadlines, tipping-off prohibition);
  Currency Transaction Report (CTR) filing ($10,000 threshold, structuring rules);
  transaction monitoring rule design (velocity, structuring, behavioral alerts);
  enterprise risk assessment methodology; BSA/AML five-pillar program governance;
  employee training requirements; independent audit/testing procedures; and regulatory
  examination preparation. Aligned with BSA/AML (US), EU AML Package 2024 (AMLR
  Reg. 2024/1624, Dir. 2024/1640), AMLD6 (Dir. 2018/1673), POCA 2002 / MLR 2017
  (UK), and FATF 40 Recommendations. Use when building a new AML/KYC program,
  assessing an existing program against regulatory expectations, preparing for a
  regulatory examination, remediating a consent order, or designing a risk-based
  customer due diligence framework. Produces compliance gap assessments with
  COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY classifications,
  remediation action plans with prioritized timelines, and board-ready program
  assessment documentation. Jurisdiction-agnostic core with US/EU/UK markers.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode AML/KYC Compliance Program Designer & Assessor

> **Disclaimer**: This skill provides a framework for AI-assisted anti-money laundering
> and know-your-customer compliance program design and assessment. It does not constitute
> legal advice and does not create an attorney-client relationship. All outputs should be
> reviewed by qualified AML counsel and compliance professionals licensed in the relevant
> jurisdictions before use. AML/KYC regulations are subject to frequent amendment; verify
> current applicability before relying on any provision described here. Statutory and
> regulatory references cited from training-data knowledge carry hallucination risk —
> always verify against authoritative sources (FinCEN.gov, EUR-Lex, FCA Handbook,
> FATF-GAFI.org) before relying on them in compliance decisions or enforcement matters.
> Sanctions lists change daily — always verify against current OFAC, OFSI, EU, and
> UN lists rather than relying on any cached data.

---

## Purpose and Scope

This skill designs and assesses AML/KYC compliance programs against the major global
regulatory frameworks: the US Bank Secrecy Act / FinCEN rules, EU Anti-Money Laundering
Directives and the 2024 AML Package, UK Proceeds of Crime Act 2002 and Money Laundering
Regulations 2017, and FATF 40 Recommendations. It operates across three modes:

- **Build**: Construct a new AML/KYC program from scratch for a financial institution
  or obliged entity
- **Assess**: Gap-analyse an existing program against regulatory expectations and
  enforcement benchmarks
- **Remediate**: Design a remediation roadmap following a consent order, examination
  finding, or internal audit deficiency

**Covers:**
- Enterprise AML/KYC risk assessment (inherent risk → controls → residual risk)
- Customer Due Diligence (CDD) program design — Standard / Simplified / Enhanced tiers
- Beneficial ownership identification (25% threshold, control prong, certification)
- Sanctions screening framework (OFAC SDN + 50% rule, EU/UK/UN lists, hit adjudication)
- PEP identification, risk rating, and ongoing monitoring
- Transaction monitoring rule design (rule-based alerts + red flag typologies)
- Suspicious Activity Report (SAR) and Currency Transaction Report (CTR) filing procedures
- BSA/AML program five-pillar assessment (+ FinCEN 2024 proposed sixth pillar)
- Employee training program design (BSA Officer, front-line, senior management)
- Independent testing / audit program requirements
- Regulatory examination preparation and documentation readiness
- High-risk customer category management (MSBs, PEPs, correspondent banks, crypto VASPs)
- FATF Travel Rule compliance for wire transfers and virtual assets (R.16)
- Multi-jurisdiction regulatory framework mapping (US / EU / UK / FATF)

**Does not:**
- Constitute legal advice or substitute for qualified AML counsel or certified AML
  specialist (CAMS/CFCS)
- Replace a fully documented AML/KYC policy suite — produces frameworks and gap analyses,
  not final policy documents
- Guarantee regulatory compliance or immunity from enforcement action
- Cover tax compliance, securities regulation, or FCPA/anti-bribery programs in depth
  (see `legalcode-compliance-program-builder`)
- Perform live sanctions screening — always use current authoritative list sources
- Cover sector-specific BSA exemption calculations in full depth

**Related skills:**
- `legalcode-compliance-program-builder` — enterprise compliance program governance and
  anti-bribery/anti-corruption program design
- `legalcode-regulatory-change-tracker` — ongoing AML/KYC regulatory change monitoring
- `legalcode-dpia-generator` — GDPR data protection overlay for customer data collected
  in KYC processes
- `legalcode-breach-severity-assessment` — data breach response for KYC data breaches
- `legalcode-incident-response-plan-builder` — operational incident response integration

---

## Jurisdiction and Governing Law

This is a multi-jurisdiction skill designed to work across US, EU, and UK frameworks
simultaneously. The applicable regulatory overlay(s) are determined in Step 2.

[JURISDICTION-SPECIFIC: United States] When the entity is subject to US BSA/AML:
- Primary statute: Bank Secrecy Act (31 U.S.C. §§ 5311–5336), as implemented by
  FinCEN and federal banking regulators
- CDD obligations: FinCEN CDD Final Rule (31 C.F.R. § 1010.230, effective May 11, 2018)
  — four core elements: (1) customer identification/verification, (2) beneficial ownership
  identification/verification (25% ownership prong + control prong), (3) understanding
  nature/purpose to develop customer risk profile, (4) ongoing monitoring
- SAR reporting: 31 C.F.R. § 1020.320 (banks); parallel rules for other covered
  institutions. Threshold: $5,000 (known suspect) / $25,000 (no suspect). Deadline:
  30 calendar days from detection; 60-day maximum with ongoing suspect identification
- CTR reporting: 31 C.F.R. § 1010.311 — $10,000 cash transaction threshold; aggregation
  rules for same-day, same-person transactions; structuring prohibition (31 U.S.C. § 5324)
- OFAC sanctions: OFAC SDN List + other blocked/restricted party lists; 50% Rule
  (entities 50%+ owned by blocked parties are themselves blocked)
- Corporate Transparency Act (CTA): 31 U.S.C. § 5336 — BOI reporting to FinCEN for
  most US corporations/LLCs; CTA BOI reporting and FinCEN CDD Rule are separate
  obligations [VERIFY current CTA enforcement status — subject to litigation in 2025]
- FinCEN 2024 Proposed Rule (June 2024, 89 FR 55508): Would require all covered
  financial institutions to maintain "effective, risk-based, and reasonably designed"
  programs, adding a mandatory enterprise risk assessment as an explicit program element
  [VERIFY if finalized before relying on this as binding]
- Investment Advisers Final Rule (August 2024): RIAs and ERAs now subject to AML/CFT
  program and SAR requirements; compliance date extended [VERIFY current compliance date]
- Sector-specific rules: OCC, FDIC, FRB, NCUA, SEC, CFTC, FINRA also enforce BSA
  requirements for their regulated entities; FFIEC BSA/AML Examination Manual is the
  primary operational reference

[JURISDICTION-SPECIFIC: European Union] When the entity is subject to EU AML law:
- Sixth Anti-Money Laundering Directive (AMLD6, Dir. (EU) 2018/1673): Harmonizes
  criminal liability for ML offenses across member states; extends predicate offenses
- EU AML Package 2024 (in force July 2024, phased application from 2027):
  - AMLR (Reg. (EU) 2024/1624): Directly applicable EU regulation replacing 4AMLD/5AMLD
    for private-sector AML obligations; effective from July 2027 [VERIFY application dates]
  - Directive (EU) 2024/1640: Replaces 4AMLD/5AMLD supervisory provisions
  - Reg. (EU) 2024/1620: Establishes AMLA (Authority for Anti-Money Laundering and
    Countering the Financing of Terrorism) as new EU AML supervisor based in Frankfurt
- Beneficial ownership: UBO registers required per Art. 30 (legal entities) and Art. 31
  (trusts/similar) of AMLD4 as amended; 25% direct/indirect ownership threshold
- PEP treatment: Both domestic and foreign PEPs require EDD under AMLR; source of
  wealth and source of funds documentation required; senior management approval needed
- Travel Rule: Regulation (EU) 2023/1113 (Transfer of Funds Regulation) extends wire
  transfer obligations to crypto-asset transfers; EBA Travel Rule Guidelines apply
  from December 30, 2024 [VERIFY]
- National implementations: Until AMLR applies (2027), national transpositions of AMLD4/5
  remain operative; significant variation exists across member states

[JURISDICTION-SPECIFIC: United Kingdom] When the entity is subject to UK AML law:
- Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer)
  Regulations 2017 (MLR 2017, SI 2017/692): Primary CDD/AML obligations for regulated
  sector firms; FCA is primary AML supervisor for most financial institutions
- Proceeds of Crime Act 2002 (POCA 2002): Three primary ML offenses (ss. 327-329):
  (1) concealing/disguising/converting criminal property; (2) arranging — facilitating
  acquisition/retention/use/control of criminal property; (3) acquisition/use/possession
  of criminal property. Penalties: up to 14 years imprisonment
- Failure to disclose (s. 330 POCA): Nominated officers in regulated sector must report
  suspicious activity; up to 5 years imprisonment for failure to report
- Tipping-off offense (ss. 333A-333E POCA): Disclosing a SAR or that one has been made
  is a criminal offense; up to 2 years imprisonment
- National Crime Agency (NCA) as UK Financial Intelligence Unit: Suspicious Activity
  Reports (SARs) filed via the SAR Online system
- Domestic PEPs: Since January 2024 regulatory update, UK domestic PEPs must be treated
  as starting from a position of lower risk than foreign PEPs (MLR 2017 reg. 35A as
  amended) [VERIFY current MLR 2017 version]
- Companies House reforms: Economic Crime and Corporate Transparency Act 2023 (ECCTA)
  introduces enhanced ID verification, PSC register reforms, and new powers to challenge
  false filings — significantly affects corporate KYC for UK entities
- FCA enforcement: Unlimited fines; criminal prosecution available for MLR 2017 breaches

[JURISDICTION-SPECIFIC: Global / FATF] For all jurisdictions, the FATF 40
Recommendations provide the underlying international standard:
- R.10 (CDD): Customer identification and verification obligations
- R.12 (PEPs): Enhanced due diligence for politically exposed persons
- R.15 (New Technologies / VASPs): AML/CFT obligations for virtual asset service providers
- R.16 (Wire Transfers / Travel Rule): Originator and beneficiary information with transfers
- R.20 (Suspicious Transactions): Obligation to report suspicious transactions to FIU
- R.21 (Tipping-off and Confidentiality): Prohibition on disclosing SAR filing
- FATF Mutual Evaluation Reports: Assess country-level technical compliance and
  effectiveness; poor ratings can affect de-risking decisions and correspondent banking

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
scope and context, the workflow pauses and asks when:

- The applicable regulatory framework (US/EU/UK/all) is unclear
- The entity type determines different obligations (bank vs. MSB vs. fintech vs. VASP)
- The operating mode (build/assess/remediate) affects the workflow direction
- The user's risk appetite or business context is needed to calibrate findings

Use the ⟁ CLARIFY pattern wherever marked below. If the user has already provided the
information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Entity description**: Type of financial institution or obliged entity, jurisdiction(s),
  products/services, customer base
- **Existing program documents**: AML policy, CDD procedures, training materials,
  audit reports, SAR filing records — pasted text or file paths
- **Regulatory examination findings**: Consent order, examination report, MOU/MRA
- **Gap analysis request**: Specific areas to assess (e.g., "review our transaction
  monitoring framework" or "assess our beneficial ownership procedures")
- **Build request**: "Build an AML program for a [entity type] in [jurisdiction]"

If no input is provided, prompt the user to describe their entity and the task they need.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask these questions. Skip any already answered:

1. **Operating Mode** — What is the primary objective?
   - **Build**: Design an AML/KYC program from scratch (the user has no existing program
     or is launching a new regulated entity)
   - **Assess**: Gap-analyse an existing program (the user has a program and wants to
     know where it falls short)
   - **Remediate**: Design a remediation roadmap following a specific finding (consent
     order, exam finding, internal audit)
   - *Why this matters*: Build mode produces frameworks and templates; assess mode
     compares current state to regulatory expectations; remediate mode prioritizes
     speed and regulator-facing communication.

2. **Entity Type** — What type of entity is this?
   - US Bank (OCC/FDIC/FRB-regulated)
   - US Non-Bank Financial Institution (MSB, broker-dealer, insurance, fintech, VASP)
   - US Investment Adviser (subject to FinCEN 2024 Final Rule)
   - EU Obliged Entity (credit institution, payment institution, crypto-VASP, etc.)
   - UK FCA-Regulated Firm (bank, payment institution, e-money institution)
   - Multi-jurisdictional (operates in 2+ of the above)
   - *Why this matters*: Entity type determines which specific regulations apply, which
     regulator will examine the program, and which specific obligations attach.

3. **Jurisdictions** — Which regulatory frameworks apply?
   - US only (BSA/AML + OFAC)
   - EU only (AMLD/AMLR)
   - UK only (POCA/MLR 2017/FCA)
   - US + EU + UK (multinational)
   - Other combination
   - *Why this matters*: Multi-jurisdiction entities must satisfy the highest standard
     across all applicable regimes simultaneously.

4. **Program Maturity** — If assessing an existing program:
   - **Nascent**: AML policies exist on paper but not operationalized
   - **Developing**: Core elements in place but significant gaps
   - **Established**: Full program in place; seeking assurance and fine-tuning
   - **Enforcement-context**: Under consent order, MRA, or MOU
   - *Why this matters*: Determines the depth of gap analysis and the urgency of
     remediation recommendations.

5. **Risk Profile** — What is the entity's core ML risk exposure?
   - High-risk customers (PEPs, MSBs, cash-intensive businesses, legal/real estate)
   - High-risk products (private banking, correspondent banking, crypto, trade finance)
   - High-risk geographies (FATF grey/black list countries, sanctions nexus)
   - Low-risk profile (retail banking, consumer lending, low-risk payment processing)
   - *Why this matters*: Determines whether Enhanced Due Diligence frameworks are needed
     and how the transaction monitoring rules should be calibrated.

If the user provides partial context, proceed with reasonable professional defaults and
state assumptions explicitly.

---

### Step 3: Determine Applicable Regulatory Framework

Map the entity to its specific regulatory obligations:

| Regulatory Dimension | US | EU | UK |
|---------------------|-----|-----|-----|
| **Primary AML statute** | BSA (31 U.S.C. §§ 5311-5336) | AMLD6/AMLR | POCA 2002 + MLR 2017 |
| **Implementing rule** | FinCEN CFR Part 1010-1030 | National AMLD transpositions / AMLR (2027) | SI 2017/692 |
| **Primary supervisor** | FinCEN + federal banking regulator | National CA / AMLA (2026+) | FCA / HMRC / others |
| **CDD standard** | 31 C.F.R. § 1010.230 | AMLD4/AMLR Art. 16-40 | MLR 2017 regs. 27-38 |
| **BO threshold** | 25% ownership + control prong | 25% direct/indirect | 25% PSC threshold |
| **SAR filing** | FinCEN via BSA E-Filing | National FIU | NCA via SAR Online |
| **Sanctions authority** | OFAC (Treasury) | EU Common Foreign & Security Policy | OFSI (HM Treasury) |
| **PEP treatment** | Risk-based (no formal domestic PEP category) | EDD required for all PEPs (AMLR) | Domestic PEP = lower risk starting point |

For multi-jurisdiction entities, apply the most stringent requirement in each area unless
the entity has a reasoned written position supporting a different approach.

---

### Step 4: Assess Enterprise AML/KYC Risk Profile

Before assessing specific program elements, establish the entity's inherent risk profile.
The risk assessment is the foundation that justifies every program calibration decision.

**⟁ CLARIFY** — Ask the user to describe the following risk drivers, or extract from
any provided risk assessment document:

**Inherent Risk Factors:**

| Risk Category | Low | Medium | High | Very High |
|--------------|-----|--------|------|-----------|
| **Customer types** | Retail consumers, W-2 employees | SME business owners | Cash businesses, legal/accounting professionals | PEPs, MSBs, shell companies, correspondent banks |
| **Products/services** | Consumer deposits, standard lending | Business banking | Private banking, trade finance, prepaid cards | Correspondent banking, crypto, digital assets, cross-border remittance |
| **Geographic reach** | Domestic only, low-risk state | Multi-state domestic | Countries with moderate FATF ratings | FATF grey/black list countries, OFAC-sanctioned jurisdictions |
| **Delivery channels** | In-person branch | Online banking | Mobile/digital-first | Fully anonymous/pseudonymous, agent networks |
| **Transaction volume** | Low volume, large transactions | Moderate | High volume, varied sizes | High frequency, small transactions (structuring risk) |

**Risk Assessment Output:**
- Overall inherent risk: LOW / MEDIUM / HIGH / VERY HIGH
- Key risk drivers: [list top 3-5]
- Mitigating controls currently in place: [summarize]
- Residual risk: [assessment]

**⟁ CLARIFY** — If the risk assessment reveals a high-risk profile but the entity
claims only standard CDD is needed, pause and present the conflict:
"Your customer base includes [X] which is classified as high-risk. This typically
requires Enhanced Due Diligence procedures. Should I treat this as requiring EDD
for these customer categories?"

---

### Step 5: Assess the Five-Pillar AML Program Structure

Assess the entity's program against the five required pillars of an effective BSA/AML
compliance program (31 C.F.R. § 1020.210(a)(2) and parallel rules for other entity
types; FinCEN 2024 Proposed Rule adds a mandatory enterprise risk assessment):

---

#### Pillar 1: Internal Controls — Policies, Procedures, and Controls

**What is required:**
- Written AML/KYC policy approved by senior management or board
- Comprehensive written procedures for each program element
- Controls to prevent, detect, and report suspicious activity
- Controls to ensure record retention (SAR: 5 years; CTR: 5 years; CDD: 5 years from
  account closure per 31 C.F.R. §§ 1020.320, 1010.311, 1010.230)
- Annual policy review and update cycle

**Assessment checklist:**

| Control Element | Present | Quality | Gap |
|----------------|---------|---------|-----|
| Written AML Policy (board/senior mgmt approved, dated) | | | |
| CDD Procedure — Individual Customers | | | |
| CDD Procedure — Legal Entity Customers + BO identification | | | |
| EDD Procedure — High-risk customer categories | | | |
| Sanctions Screening Procedure (OFAC/EU/UK as applicable) | | | |
| PEP Identification and EDD Procedure | | | |
| Transaction Monitoring Procedure (alert investigation workflow) | | | |
| SAR Filing Procedure (internal referral → Compliance → FinCEN/FIU) | | | |
| CTR Filing Procedure (US: $10K threshold, structuring prohibition) | | | |
| Record Retention Schedule (5-year retention confirmed) | | | |
| High-Risk Customer Category Management Procedure | | | |
| Third-Party Reliance Procedure (if applicable) | | | |
| De-risking / Account Closure Procedure | | | |
| Annual Policy Review and Update Process | | | |

**Classification criteria:**
- **COMPLIANT**: All key policies present, reviewed within 12 months, senior management
  approved, operationalized (not just paper)
- **PARTIAL**: Most policies present but missing key elements, not recently updated,
  or not operationalized in practice
- **NON-COMPLIANT**: Core policies missing (e.g., no CDD procedure, no SAR procedure)
- **CRITICAL DEFICIENCY**: No written AML policy; controls are absent rather than weak

---

#### Pillar 2: BSA/AML Compliance Officer

**What is required:**
- Designated individual responsible for day-to-day BSA/AML compliance
  (31 C.F.R. § 1020.210(a)(2)(iii))
- Sufficient authority, independence, and resources to perform the function
- Expertise in AML/KYC law and the entity's specific risk profile
- Direct reporting line to senior management or board on material compliance matters
- Succession planning / designated backup

[JURISDICTION-SPECIFIC: US] The BSA Officer does not need to be a C-suite title but
must have sufficient authority to effect change; FinCEN and banking regulators have
cited institutions where the BSA Officer lacked resources or authority.

[JURISDICTION-SPECIFIC: EU/AMLR] AMLR (Art. 9) requires the appointment of a
compliance officer at management level who is not personally liable for ML unless they
have facilitated or enabled it. [VERIFY applicable AMLR article in final text]

[JURISDICTION-SPECIFIC: UK/MLR 2017] Regulation 21A requires appointment of a Money
Laundering Reporting Officer (MLRO) for most regulated firms; the MLRO must be a
"nominated officer" responsible for internal disclosures and external SARs to NCA.

**Assessment checklist:**

| Element | Present | Quality | Gap |
|---------|---------|---------|-----|
| Named BSA Officer / MLRO designated in writing | | | |
| Appropriate seniority and authority (can escalate to board) | | | |
| Dedicated resources for AML function (headcount/budget) | | | |
| Direct access to board/risk committee | | | |
| Qualified (CAMS, CFCS, or equivalent experience) | | | |
| Annual performance review includes AML function metrics | | | |
| Succession plan / backup MLRO designated | | | |

---

#### Pillar 3: Employee Training Program

**What is required:**
- Ongoing training program for all relevant employees
  (31 C.F.R. § 1020.210(a)(2)(iv))
- Training tailored to each employee's role and ML risk exposure
- New hire training + periodic refresher (minimum annual for most roles)
- Documentation of training completion (name, date, content, pass/fail)
- Tailored content for: BSA Officer, front-line staff, senior management, board

**Training content by audience:**

| Audience | Required Content | Frequency |
|---------|-----------------|-----------|
| **BSA Officer / AML Staff** | Full regulatory framework; typologies; SAR/CTR filing; exam preparation; enforcement trends | Annual + upon material regulatory change |
| **Front-Line (Tellers, Relationship Managers)** | Red flag recognition; structuring prohibition; SAR internal referral; CDD documentation requirements; escalation protocol | New hire + annual |
| **Senior Management** | Culture of compliance; tone from the top; program oversight responsibility; enforcement exposure | Annual |
| **Board of Directors** | Program oversight; regulatory environment; material metrics; enforcement landscape | Annual |
| **Operations / Back-Office** | CTR filing; wire transfer documentation; record retention | Role-specific at onboarding + annual |

**Assessment checklist:**

| Element | Present | Quality | Gap |
|---------|---------|---------|-----|
| Role-tailored training program in place | | | |
| Training content reflects current regulations and typologies | | | |
| Training completion records maintained (5 years) | | | |
| New hire training completed before customer-facing work | | | |
| Annual refresher completed for all relevant staff | | | |
| Board-level training documented | | | |
| Training tests/assessments with pass thresholds | | | |

**Common 2024 exam findings on training:**
- Training not tailored to specific business lines or product risks
- Off-the-shelf training modules not customized for the entity's risk profile
- Front-line staff unable to describe red flags specific to the entity's customers
- Board members with no documented AML training
- No training on specific high-risk areas (crypto, correspondent banking, trade finance)

---

#### Pillar 4: Independent Testing / Audit

**What is required:**
- Independent testing (audit) of the AML/KYC program
  (31 C.F.R. § 1020.210(a)(2)(ii))
- "Independent" means the testing function should not be the BSA Officer reviewing
  their own work — can be internal audit (if sufficiently independent), external audit,
  or third-party consultant
- Annual testing is the general standard; high-risk entities may require more frequent
- Scope must cover all five pillars: policies, CDD quality, transaction monitoring,
  SAR/CTR filing, training

**Assessment checklist:**

| Element | Present | Quality | Gap |
|---------|---------|---------|-----|
| Annual independent audit/testing conducted | | | |
| Auditor independence confirmed (not BSA Officer self-review) | | | |
| Audit scope covers all five pillars | | | |
| Transaction monitoring system logic and threshold tested | | | |
| CDD file quality reviewed (sample of customer files) | | | |
| SAR/CTR filing accuracy and timeliness tested | | | |
| Prior audit findings tracked to resolution | | | |
| Audit findings reported to board/senior management | | | |
| Management responses with corrective action timelines documented | | | |

**⟁ CLARIFY** — If the audit was last conducted more than 18 months ago, or if the
audit scope excluded transaction monitoring, present this as a gap:
"The most recent audit is [X] months old / excluded transaction monitoring. This
creates examination risk. Should I classify this as PARTIAL or NON-COMPLIANT?"

---

#### Pillar 5: Customer Due Diligence (CDD)

This is the most complex pillar and is assessed in depth in Step 6.

---

### Step 6: Assess Customer Due Diligence (CDD/EDD)

#### 6a. CDD Tier Framework

Assess whether the entity has correctly designed its CDD tier system:

| Tier | Trigger Criteria | Required Elements |
|------|----------------|-----------------|
| **Simplified Due Diligence (SDD)** | Low-risk customers where ML risk is minimal (e.g., public sector entities, regulated financial institutions in low-risk jurisdictions, employee payroll accounts) | Identity verification; limited ongoing monitoring |
| **Standard CDD** | Default tier for most customers | Full identity verification; beneficial ownership (entities); customer risk profile; ongoing monitoring |
| **Enhanced Due Diligence (EDD)** | Mandatory for: PEPs; high-risk countries; correspondent banking; complex/unusual ownership structures; high-risk business types; customer behavior triggers | All CDD elements PLUS source of wealth; source of funds; senior management approval; more frequent monitoring; additional adverse media screening |

**EDD must be applied — not optional — for:**
- All PEPs and their family members and close associates
- Customers from or with significant connections to FATF grey/black list jurisdictions
- Correspondent banking relationships (PATRIOT Act § 312 for US banks)
- [JURISDICTION-SPECIFIC: US] Shell companies with complex ownership chains where
  beneficial owners cannot be identified
- [JURISDICTION-SPECIFIC: EU/AMLR] High-risk third countries identified by the
  European Commission per AMLR Art. 29 [VERIFY current list]
- [JURISDICTION-SPECIFIC: UK/MLR 2017] High-risk third countries per reg. 33(1)(a);
  also required when a transaction has no apparent economic/legal purpose (reg. 33(1)(b))

#### 6b. CDD Onboarding — Individual Customers

**Identity verification requirements:**

| Element | Minimum Standard | EDD Enhancement |
|---------|-----------------|----------------|
| Legal name | Government-issued photo ID (passport, driver's license, national ID) | Cross-reference with PEP/sanctions database at onboarding |
| Date of birth | Same photo ID | — |
| Residential address | Photo ID + utility bill / bank statement / government letter (≤ 3 months) | Confirm via independent source (credit bureau, commercial database) |
| Nationality | Passport / national ID | Screen against sanctions/PEP lists for all nationalities |
| ID number | SSN (US) / national ID number | — |
| Purpose/expected activity | Transaction profile at onboarding | Detailed business purpose; expected transaction volumes |
| Source of funds (EDD) | Not required for SDD/CDD | Bank statement; payroll record; asset sale documentation |
| Source of wealth (EDD) | Not required for SDD/CDD | Employment history; business activities; inheritance documentation |

**Electronic identity verification:**
- Electronic ID verification (eIDV) tools (e.g., Jumio, Onfido, LexisNexis) are
  accepted in most jurisdictions but must meet minimum standards for reliability
- FATF has endorsed biometric verification for remote onboarding where supported by
  government-issued ID verification
- [JURISDICTION-SPECIFIC: UK/MLR 2017] Electronic verification is explicitly permitted
  under reg. 28(10) if reliable; combination of databases providing assurance equivalent
  to documentary verification

#### 6c. CDD Onboarding — Legal Entity Customers

**Entity verification checklist:**

| Element | Required Information | Source |
|---------|---------------------|--------|
| Legal name and type | Full legal name; entity type (LLC, Corp., Ltd., etc.) | Certificate of incorporation; commercial register |
| Registered address | Registered agent address or principal office | Formation documents |
| Jurisdiction of formation | State/country of incorporation | Certificate of incorporation |
| Principal place of business | Actual operating address | Client certification; utility bill |
| Business purpose | Nature of business; industry; products/services | Client certification; website; business license |
| Expected activity | Expected transaction volume; types; counterparties | Client certification |
| Authorized signatories | Names; identification of individuals authorized to act | Board resolution; corporate authority documents |
| Beneficial ownership | All natural persons owning ≥ 25% + control person | FinCEN Beneficial Ownership Certification (US) or equivalent |

[JURISDICTION-SPECIFIC: US/FinCEN CDD Rule] Collect and verify the identity of all
natural persons owning 25%+ equity interest AND one individual who controls/manages the
legal entity (control prong), using FinCEN's standardized Beneficial Ownership
Certification form or equivalent. Key 2024 FinCEN relief: firms may rely on prior BO
certification for existing customers opening new accounts (verify current approach is
risk-based updating rather than blanket re-certification at each new account).

[JURISDICTION-SPECIFIC: EU/AMLR] Verify through the applicable national beneficial
ownership register (Art. 30 AMLD4 / AMLR) AND direct client documentation. Where a
discrepancy exists between register data and client-provided data, investigate and
report to the national register if appropriate.

[JURISDICTION-SPECIFIC: UK/MLR 2017] Verify using Companies House PSC (People with
Significant Control) register and additional documentation. ECCTA 2023 significantly
enhanced Companies House verification requirements; obtain confirmation that director
ID verification has been completed if required.

**⟁ CLARIFY** — For legal entity customers with complex ownership structures (multiple
layers of holding companies, nominee arrangements, trust/foundation ownership):
"This entity has a [X]-layer ownership structure. Standard CDD procedures may be
insufficient to identify the ultimate beneficial owner. Should I treat this as
requiring EDD and document the enhanced ownership analysis?"

#### 6d. PEP Identification and Enhanced Due Diligence

**PEP categories (apply to all jurisdictions as minimum):**

| Category | Examples |
|---------|---------|
| **Head of State / Government** | Presidents, prime ministers, monarchs |
| **Legislative** | National parliament/congress/senate members |
| **Judicial (senior)** | Supreme Court justices; appellate court judges |
| **Military (senior)** | Generals, admirals, chiefs of defense |
| **Senior government officials** | Cabinet ministers; departmental secretaries |
| **Senior political party officials** | Party executives; general secretaries |
| **Senior state-owned enterprise executives** | CEOs, CFOs, board members of SOEs |
| **International organization executives** | Senior officials of UN, IMF, World Bank, NATO, etc. |
| **Immediate family members** | Spouse, registered partner, children, parents, siblings |
| **Known close associates** | Business partners with personal/financial connections to PEP |

[JURISDICTION-SPECIFIC: UK/MLR 2017] As of January 2024, domestic PEPs carry a lower
risk starting point than foreign PEPs (reg. 35A as amended). However, EDD must still
be applied and cannot be automatically reduced to CDD without a documented risk
assessment demonstrating lower ML risk. [VERIFY current MLR 2017 reg. 35A position]

**PEP screening tools:**
- Commercial screening databases: LexisNexis World-Check, Refinitiv Screening,
  Dow Jones Risk & Compliance, Moody's, ComplyAdvantage, LSEG, Acuris
- Government lists: OFAC SDN, US State Dept., EU targeted financial sanctions, OFSI
- Screening should occur at: (1) onboarding, (2) periodic review, (3) real-time on
  material change, (4) immediately on new screening list update

**EDD requirements for PEPs (all jurisdictions):**

| Element | Standard CDD | PEP EDD Addition |
|---------|-------------|------------------|
| Identity verification | Standard | Same; cross-reference multiple sources |
| Beneficial ownership | Standard 25% | Full ownership mapping; identify all associated entities |
| Source of funds | Not required | Required — documented; corroborated |
| Source of wealth | Not required | Required — career/business history; asset acquisition timeline |
| Business purpose | General | Specific justification for each product/service |
| Transaction monitoring | Standard thresholds | Enhanced thresholds; tailored rules; frequent manual review |
| Review frequency | Annual or risk-based | 6-monthly or more frequent |
| Senior management approval | Not required | Required — documented; named approver |
| Ongoing adverse media | Periodic | Continuous / real-time |

**De-PEPing procedure:**
- A former PEP should retain EDD treatment for a minimum period after leaving office
  (typically 12–18 months; some jurisdictions require indefinite if ML risk remains)
- [JURISDICTION-SPECIFIC: EU/AMLR] Obliged entities must assess whether risk has
  reduced sufficiently to move to standard CDD — this requires documented risk assessment
  and cannot be automatic
- [JURISDICTION-SPECIFIC: UK/FCA] FCA guidance does not specify a fixed de-PEP timeline;
  risk assessment required on a case-by-case basis

---

### Step 7: Assess Sanctions Screening Framework

**⟁ CLARIFY** — Determine which sanctions lists the entity must screen against:
- OFAC (US entities, and all USD transactions clearing through US correspondent banks)
- EU Consolidated List (EU entities; extraterritorial effect on EU persons worldwide)
- UK OFSI Consolidated List (UK entities; note post-Brexit divergence from EU list)
- UN Security Council Sanctions Lists (universally applicable)
- Sector-specific lists (CISADA, CAATSA, etc. for specific industries/countries)

**Screening framework assessment:**

| Element | Required Standard | Assessment |
|---------|-----------------|------------|
| Lists screened | Applicable jurisdiction list(s) + any correspondent bank requirements | |
| Screening at onboarding | All new customers; all related parties (UBOs, directors, guarantors) | |
| Ongoing screening | Re-screen all customers when list updates (automated preferred) | |
| Transaction screening | Wire transfers and other high-risk transactions | |
| OFAC 50% Rule | Aggregate indirect ownership to screen through legal entity layers | |
| Name matching algorithm | Fuzzy matching; transliteration variants; nickname handling | |
| Hit adjudication | Documented process for true match vs. false positive | |
| True match escalation | Blocking/rejecting transactions; OFAC reporting; account review | |
| OFAC specific license | Process for requesting specific license when required | |
| Record retention | Sanctions screening records (5 years minimum) | |
| Vendor management | Sanctions screening tool validation; regular threshold testing | |

**OFAC 50% Rule — critical compliance element:**
OFAC considers entities owned 50% or more in the aggregate by one or more blocked
persons to themselves be blocked, even if not named on the SDN list. This means:
- Screen through corporate ownership chains to identify entities meeting this threshold
- Document the ownership analysis supporting the conclusion that an entity is not
  blocked under the 50% Rule
- This is a frequent examination finding when institutions screen entity names but do
  not analyze ownership structures

**Sanctions screening quality gates:**
- False positive rate: Document and review; excessive false positives often indicate
  threshold issues that may also suppress true positives
- False negative testing: Conduct periodic testing with known-positive test names to
  verify the tool is functioning correctly
- List currency: Verify the tool updates lists on OFAC's publication schedule
  (OFAC updates SDN list on an ad hoc basis, sometimes multiple times per day)

---

### Step 8: Assess Transaction Monitoring Framework

**⟁ CLARIFY** — Determine the transaction monitoring approach:
- Manual monitoring only (suitable only for very small, low-risk entities)
- Rule-based automated system (most common for small/mid-sized institutions)
- Hybrid: Rule-based + behavioral analytics / ML-based detection
- Name the system vendor or confirm it is a proprietary build

**Transaction monitoring rule assessment:**

| Rule Type | Purpose | Key Design Considerations |
|-----------|---------|--------------------------|
| **High-value cash** | CTR threshold; large cash activity | $10,000 US threshold; aggregate same-day related transactions |
| **Structuring detection** | Identify deliberate below-threshold transactions | Pattern of transactions just below $10K; velocity over 24-72 hours |
| **Wire transfer velocity** | Unusual wire activity | Volume and frequency vs. expected activity baseline |
| **Round-dollar transactions** | Layering indicator | High frequency of transactions in exact round amounts |
| **Geographic anomaly** | Transactions to/from high-risk countries | FATF grey/black list; OFAC country overlays |
| **Dormant account activation** | Sudden activity on previously inactive accounts | Define dormancy threshold; investigate reactivation triggers |
| **Rapid fund movement** | Funds in/out same business day | Layering typology |
| **Inconsistent activity** | Transactions inconsistent with customer profile | Compare to expected activity profile established at onboarding |
| **High-risk business type** | Specific rules for MSBs, crypto, real estate | Tailored thresholds for entity risk category |
| **PEP-specific rules** | Enhanced monitoring for PEP accounts | Lower alert thresholds; manual review triggers |

**Alert investigation process:**

```
Alert Generated → L1 Review (analyst) → True alert or False Positive?
    │
    ├── False Positive → Document disposition; tune rule if systematic
    │
    └── True Alert → L2 Review (senior analyst / BSA Officer)
              │
              ├── No SAR required → Document reasoning; continue to monitor
              │
              └── SAR filing warranted → Internal SAR referral → Compliance review
                        │
                        └── Management approval → File SAR (within 30 days of detection)
```

**Transaction monitoring calibration — common failures:**
- Off-the-shelf rules not tailored to the entity's specific business, products, or
  customer types (cited in TD Bank $3.1B penalty and multiple 2024 consent orders)
- Alert thresholds set too high to avoid operational burden (cited in 2024 enforcement)
- No periodic threshold testing to validate effectiveness
- No documentation that rules have been reviewed and tuned based on alert outcomes
- Monitoring system not updated as business grows (TD Bank: $18.3T unmonitored)
- Alert backlogs that prevent timely investigation and SAR filing

**Transaction monitoring adequacy test:**
- Pull a sample of filed SARs and trace back to the alert that triggered them — is
  the alert → investigation → SAR pipeline functioning as designed?
- Conduct a reverse review: identify known ML patterns and test whether current rules
  would have detected them

---

### Step 9: Assess SAR and CTR Filing Procedures

#### 9a. SAR Filing (All Jurisdictions)

**US SAR — key parameters (31 C.F.R. § 1020.320):**
- Threshold: $5,000 (known or suspected suspect) / $25,000 (no suspect identified)
- Deadline: 30 calendar days from initial detection; 60-day maximum where no suspect
  identified at detection
- Filing: FinCEN via BSA E-Filing system (FinCEN SAR, previously FinCEN Form 111)
- Tipping-off: Strictly prohibited — disclosing a SAR or its existence to any person
  named in the SAR or their associates is a federal offense (31 U.S.C. § 5318(g)(2))
- Safe harbor: Filing in good faith provides complete protection from civil liability
  (31 U.S.C. § 5318(g)(3))
- Record retention: Copy of SAR + supporting documentation, 5 years from filing date

[JURISDICTION-SPECIFIC: UK/POCA] SAR filed with NCA via SAR Online; consent SAR
available where a firm wants to proceed with a transaction but seeks NCA consent first;
NCA has 7 working days to respond (consent or moratorium period of 31 days). Filing
a SAR without tipping off requires careful management of client communications.

[JURISDICTION-SPECIFIC: EU] SARs (or Suspicious Transaction Reports) filed with
national FIU; specific deadlines and formats vary by member state. AMLR (from 2027)
will harmonize some procedural elements [VERIFY].

**SAR narrative quality standards (5 Ws framework):**
- **Who**: Full identification of subject(s) — name, address, ID, account numbers,
  role in the suspicious activity
- **What**: Description of the suspicious activity — specific transactions, amounts,
  dates, accounts involved
- **When**: Timeline of the activity — specific dates, pattern over time
- **Where**: Accounts, locations, correspondent banks, systems involved
- **Why/How**: Explanation of why the activity is suspicious — how it deviates from
  expected activity; what ML typology it resembles; what red flags were identified
- **Note**: Do not include a conclusion that a crime has occurred; describe facts and
  explain the basis for suspicion

**SAR narrative common deficiencies:**
- Generic boilerplate language not specific to the transaction pattern
- Missing customer identification information
- Failing to explain what made the activity suspicious (just describing what happened)
- Not linking specific transactions to specific red flags
- Omitting prior SAR history on the same subject

#### 9b. CTR Filing (US)

**CTR key parameters:**
- Threshold: Cash transactions exceeding $10,000 in a single business day
- Aggregation: Must aggregate multiple cash transactions by the same person in the same
  day at the same institution, even across different branches
- Filing deadline: 15 calendar days after the day of the transaction
- Structuring prohibition (31 U.S.C. § 5324): It is a federal crime to structure
  transactions to avoid CTR filing — even when the underlying funds are lawful
- CTR exemptions: Available for certain customers (Phase I and Phase II exemptions per
  31 C.F.R. § 1020.315) — must be documented and periodically reviewed

**⟁ CLARIFY** — If the entity processes a significant number of cash transactions,
ask: "Does your institution have a CTR filing workflow with clear aggregation rules
and a defined exemption program? This is an area of frequent examination findings."

---

### Step 10: Assess Governance, Training, and Examination Readiness

#### 10a. Governance and Culture

**Board and senior management responsibilities:**
- Board must approve the AML policy annually and receive meaningful AML program
  reporting (not just "no SARs filed" — qualitative metrics are required)
- Senior management must ensure adequate resources — staffing, technology, budget
- "Tone from the top" is explicitly evaluated in FFIEC examinations and DOJ enforcement

**AML program metrics to present to board:**
- SAR filings: Volume; amounts; typologies; disposition of declined SARs
- CTR filings: Volume; exemptions granted
- CDD quality: Sample review results; backlog if any
- Transaction monitoring: Alert volume; L1/L2 closure rates; open alerts aging
- Audit findings: Open items; closure status; new findings
- Training: Completion rates; pass rates; open remediation
- Regulatory environment: Material changes in the past year

#### 10b. Regulatory Examination Preparation

**Documentation readiness checklist:**

| Document Category | Exam Ready? | Location |
|------------------|-------------|----------|
| AML Policy (current, board-approved) | | |
| BSA/AML Officer designation (written) | | |
| Enterprise AML/KYC Risk Assessment (≤ 12 months old) | | |
| CDD Procedures (current version with revision history) | | |
| Beneficial Ownership Procedures and Certification Forms | | |
| Sanctions Screening Procedure + tool configuration documentation | | |
| PEP Procedure + current PEP list/inventory | | |
| Transaction Monitoring Rule Inventory (thresholds, rationale, last review date) | | |
| SAR Filing Log (5 years; searchable by subject/date) | | |
| Declined SAR Log (with documented reasoning) | | |
| CTR Filing Log + Exemption Register | | |
| Independent Audit Report (most recent) | | |
| Open Audit Findings + Corrective Action Plans | | |
| Training Records (5 years; completions by role) | | |
| Board AML Reporting (minutes confirming board review) | | |

**⟁ CLARIFY** — If any of the above documents are missing or more than 18 months old,
flag the gap: "Your [document] appears to be [X] months old / absent. Regulators
expect this to be [frequency]. This should be addressed before an examination."

**2024-2025 examination hot topics:**
- Beneficial ownership adequacy (FinCEN CDD Rule vs. CTA BOI — regulators evaluating
  whether institutions understand the distinction)
- Crypto/VASP relationships — adequate CDD and transaction monitoring for crypto
  customers and correspondent crypto exchange relationships
- Trade-based money laundering (TBML) — awareness and detection
- AI/machine learning in transaction monitoring — model validation and explainability
- Derisking — regulators are scrutinizing whether de-risking decisions are well-documented
  and whether institutions are derisking rather than managing risk
- Third-party/fintech partnerships — BSA responsibility cannot be delegated; the covered
  institution remains responsible for AML compliance for fintech partner customers

---

### Step 11: Classify Findings and Generate Compliance Assessment

#### Severity Classification System

Apply this four-tier classification to each program element assessed:

| Classification | Definition | Regulatory Risk |
|---------------|-----------|----------------|
| **COMPLIANT** | The element meets or exceeds regulatory expectations; no material gaps identified; documented, current, and operationalized | Low — this element should not be cited in an examination |
| **PARTIAL** | The element exists but has identifiable gaps: missing documentation, outdated content, incomplete implementation, or limited effectiveness | Moderate — could be cited as an "area for improvement" in examination; monitor and remediate |
| **NON-COMPLIANT** | A required element is materially deficient: significantly outdated, not operationalized, not tailored to the entity's risk, or demonstrably ineffective | High — examination finding expected; voluntary remediation reduces penalty risk |
| **CRITICAL DEFICIENCY** | A required element is absent or completely non-functional; immediate regulatory risk; possible basis for consent order, civil money penalty, or criminal referral | Immediate — requires emergency remediation; consider voluntary disclosure to regulator |

#### Prioritization Framework

Prioritize remediation by regulatory and operational risk:

| Priority | Criteria | Action |
|----------|---------|--------|
| **IMMEDIATE** (0-30 days) | CRITICAL DEFICIENCY findings; any element that could constitute a BSA/AML criminal violation (failure to file required SARs; structuring facilitation); OFAC blocking violations; regulatory examination scheduled | Halt operations if legally required; remediate immediately; brief board; consider voluntary disclosure |
| **NEAR-TERM** (30-90 days) | NON-COMPLIANT findings; multiple PARTIAL findings in the same pillar; gaps that would likely be cited in an examination | Assign remediation owner; document corrective action plan; report to board |
| **BACKGROUND** (90-180 days) | PARTIAL findings that do not create immediate regulatory risk; enhancements that improve program effectiveness beyond the minimum required standard | Include in annual program enhancement roadmap |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any compliance assessment. If any gate
fails, revise before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every regulatory claim cites a specific statute, regulation, or authoritative guidance | Add citation or mark "[VERIFY — source not identified]" |
| **Format** | All citations follow consistent format appropriate to the jurisdiction (31 C.F.R., SI 2017/692, etc.) | Fix format |
| **Currency** | Each cited provision checked for amendments or replacement | Flag "[CHECK CURRENCY]" — especially for AMLR application dates |
| **Domain** | Analysis stays within the applicable regulatory framework; no cross-jurisdiction contamination without appropriate labeling | Remove or flag |
| **Confidence** | Uncertainty explicitly stated, not hidden; sanctions list data acknowledged as current only if freshly queried | Add confidence qualifier |

### Self-Interrogation for CRITICAL DEFICIENCY Classifications

For any element classified as CRITICAL DEFICIENCY, apply this 3-pass review before
delivering the assessment:

**Pass 1 — Regulatory Chain Integrity**: Does the deficiency classification follow
logically from the cited regulatory requirement? Would a BSA examination actually
cite this deficiency, or is this an over-classification? What specific regulatory
provision has been violated?

**Pass 2 — Completeness**: Have all relevant regulations and guidance been considered?
Is there a safe harbor, exception, or alternative compliance mechanism that could
address the deficiency without the finding being as severe?

**Pass 3 — Challenge**: What is the strongest argument that this element is actually
COMPLIANT or PARTIAL rather than CRITICAL DEFICIENCY? Under what circumstances might
a reasonable regulator accept the current state? Is there compensating control evidence?

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled regulatory requirement; cited provision confirmed | State with confidence |
| **High** | 0.80-0.94 | Strong regulatory expectation; minor interpretive questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good regulatory arguments but some interpretive uncertainty | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuine regulatory uncertainty | Flag for legal review with both sides of argument |
| **Unlikely** | 0.0-0.39 | Weak basis; speculative | Do not assert; flag "[UNCERTAIN — verify with AML counsel]" |

---

## Anti-Patterns: What Not to Do

Topic-specific AML/KYC compliance anti-patterns. Identify and flag these wherever found.

1. **Checkbox compliance, not risk-based compliance** — Treating AML/KYC as a documentation
   exercise rather than a genuine risk management program; collecting forms without
   understanding the customer or the risk. Regulators are explicitly looking for programs
   that work in practice, not just on paper.

2. **Off-the-shelf transaction monitoring** — Using vendor-provided default monitoring rules
   without customizing thresholds or scenarios to the entity's specific customer types,
   products, and risk profile. Cited in TD Bank enforcement action (2024) and multiple
   2024 consent orders.

3. **Static risk assessment** — Completing an enterprise risk assessment once and never
   updating it. Risk assessments must be updated at least annually and upon material
   business change (new product launch, new customer segment, acquisition, regulatory change).

4. **Treating FinCEN CDD Rule and CTA BOI as the same thing** — The FinCEN CDD Rule
   (31 C.F.R. § 1010.230) requires financial institutions to collect beneficial ownership
   information from customers. The CTA (31 U.S.C. § 5336) requires companies themselves
   to report to FinCEN. These are distinct, parallel obligations; confusing them creates
   compliance gaps in both.

5. **The 25% trap** — Identifying beneficial owners only at the 25% ownership threshold
   and ignoring the control prong. The CDD Rule requires identification of both the
   ownership prong (25%+) AND a control person, regardless of their ownership percentage.

6. **Passive PEP programs** — Screening for PEPs at onboarding but not conducting ongoing
   screening as customers or their family members become PEPs post-onboarding. PEP status
   can change; monitoring must be continuous.

7. **De-PEP without documentation** — Removing a customer from EDD treatment after they
   leave a PEP position without conducting and documenting a formal risk assessment.
   No fixed de-PEP timeline should be applied automatically.

8. **OFAC 50% Rule blindspot** — Screening entity names against the SDN list but failing
   to trace ownership chains to identify entities that are blocked under the 50% Rule
   (owned 50%+ in aggregate by SDN-listed persons). This is a common examination finding.

9. **Poor SAR narrative quality** — Filing SARs with generic boilerplate language ("customer
   engaged in activity that may constitute money laundering") rather than specific, factual
   5-W narrative. Regulators and law enforcement cannot act on generic SARs.

10. **Tipping off by omission** — Failing to train customer-facing staff on the tipping-off
    prohibition, resulting in staff inadvertently disclosing that a SAR has been filed or
    that an account is under review, simply by being evasive or changing behavior around
    a customer.

11. **Structuring facilitation** — Front-line staff advising customers how to structure
    transactions to avoid CTR filing, or not recognizing and reporting structuring as
    suspicious. This can constitute a criminal offense for the institution and the employee.

12. **Insufficient beneficial ownership refreshing** — Collecting beneficial ownership
    information at account opening and never updating it. The CDD Rule requires updating
    on a risk-based basis; the entity must have a process for triggering refreshes upon
    material change events (ownership change, adverse media, sanctions hit, annual review).

13. **Training theater** — Providing annual compliance training that is generic, not role-
    specific, and tested only by a click-through acknowledgment. Regulators expect training
    to be tailored to the employee's specific role and risk exposure, and effective (tested
    and competency-verified).

14. **Prioritizing growth over compliance** — Onboarding high-risk customers without
    completing CDD, or opening accounts before beneficial ownership is fully resolved,
    to avoid losing business. This is the pattern identified in the TD Bank $3.1B enforcement
    action (2024): "the bank prioritized growth and profit over complying with the law."

15. **Alert backlog management** — Closing transaction monitoring alerts without adequate
    investigation, or batching closures en masse, to reduce alert backlog. Each alert must
    be investigated on its own facts.

16. **Derisking without documentation** — Exiting customer relationships (derisking) without
    documenting the specific ML risk basis for the decision. Regulators are scrutinizing
    derisking, and unexplained exits of entire customer categories (all MSBs, all cannabis
    businesses) without individual risk assessments can itself be cited.

17. **Third-party reliance without oversight** — Relying on a third party for CDD performance
    (e.g., fintech partner, introducers) without maintaining legal responsibility and conducting
    ongoing oversight. Under BSA and MLR 2017, the covered institution cannot delegate its
    compliance obligation; third-party reliance is permitted but the institution remains liable.

18. **Single-point BSA Officer dependency** — Building the entire AML program around one
    individual with no succession plan. When the BSA Officer departs, programs frequently
    collapse. Also: BSA Officers who wear too many hats and lack adequate resources to
    perform the function effectively.

19. **Ignoring correspondent banking risk** — Banks providing correspondent services to
    foreign financial institutions without conducting PATRIOT Act § 312 enhanced due
    diligence and maintaining current knowledge of the respondent's AML program and
    customer base.

20. **No look-back process** — Failing to conduct SAR look-back reviews when new information
    reveals that previously unreported transactions may have been suspicious. Regulators
    require look-back reviews in many enforcement contexts; not having a defined process
    for triggering them is itself a gap.

21. **Crypto/VASP risk blindspot** — Failing to assess and manage the ML risk of
    cryptocurrency and virtual asset customers and counterparties. VASPs operating without
    adequate KYC (or in unregulated jurisdictions) present heightened risk; correspondent
    banking relationships with crypto exchanges require EDD under FATF R.15 and emerging
    national rules.

22. **Board reporting quality** — Providing board-level AML reporting that is superficial
    (e.g., "no issues identified," "program is operational") without meaningful metrics,
    trend analysis, or risk insights. Board members must understand the program's actual
    performance to provide effective oversight.

---

## Writing Standards

Apply these standards when producing any compliance assessment deliverable:

1. **Precision over generality**: Write "The entity's CDD procedure (v2.1, dated March 2024)
   does not address the control prong of the FinCEN CDD Rule" rather than "CDD procedures
   may need improvement."

2. **Severity language alignment**: CRITICAL DEFICIENCY findings must use urgent language;
   PARTIAL findings must not be overstated as NON-COMPLIANT.

3. **Regulatory citation completeness**: Every finding must cite the specific regulatory
   provision it is assessed against.

4. **Actionable remediation**: Every finding must include at least one specific remediation
   action with a suggested timeline (IMMEDIATE / NEAR-TERM / BACKGROUND).

5. **Confidence qualification**: Any regulatory interpretation that is not settled law must
   be qualified with the applicable confidence level and a recommendation to verify with
   AML counsel.

6. **[VERIFY] discipline**: Mark every statutory/regulatory citation that has not been
   independently verified against current authoritative sources.

7. **Tone**: Findings should be factual and professional — not alarmist and not dismissive.
   The goal is to help the entity understand and remediate its risk, not to create
   unnecessary alarm or false reassurance.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- Search for current FinCEN guidance, FCA notices, and FATF publications related to
  the entity's specific risk areas
- Verify current OFAC, EU, and UK sanctions list currency
- Research recent enforcement actions relevant to the entity's risk profile
- Look up current AMLR/AMLD6 application dates and national implementing legislation
- Mark all legalcode-mcp-verified citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Proceed with training-data knowledge and mark all regulatory citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Direct the user to verify: FinCEN.gov, FATF-GAFI.org, FCA Handbook online,
  EUR-Lex for AMLR/AMLD texts

---

## Localization Notes

This skill is calibrated for US/EU/UK regulatory frameworks. For other jurisdictions:

- **Canada (PCMLTFA / FINTRAC)**: Apply FATF-aligned framework; replace FinCEN with
  FINTRAC; note different STR thresholds and LCTR requirements [JURISDICTION-SPECIFIC]
- **Australia (AML/CTF Act 2006)**: AUSTRAC-supervised; Know Your Customer rules;
  threshold transactions at AUD 10,000; suspicious matter reports [JURISDICTION-SPECIFIC]
- **Singapore (CDSA / MAS Notice SFA04-N02)**: MAS AML requirements for financial
  institutions; specific CDD and EDD standards [JURISDICTION-SPECIFIC]
- **UAE / DIFC / ADGM**: CBUAE, DFSA, FSRA supervision; significant recent FATF
  improvements; real estate and gold sector ML risk [JURISDICTION-SPECIFIC]

---

## Output Format Template

Produce the AML/KYC Compliance Program Assessment in this structure:

---

```markdown
# AML/KYC Compliance Program Assessment
**Entity**: [Entity Name and Type]
**Jurisdiction(s)**: [US / EU / UK / Multi-jurisdictional]
**Assessment Date**: [Date]
**Operating Mode**: [Build / Assess / Remediate]
**Prepared by**: AI-assisted — requires review by qualified AML counsel

---

## Executive Summary

**Overall Program Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Critical Deficiencies**: [N findings requiring immediate action]
**Non-Compliant Elements**: [N findings requiring near-term remediation]
**Partial Compliance**: [N findings requiring background attention]
**Compliant Elements**: [N elements meeting regulatory expectations]

### Top 3 Priority Actions
1. [Most urgent finding with specific remediation step and deadline]
2. [Second priority]
3. [Third priority]

---

## Applicable Regulatory Framework

| Framework | Applicable | Primary Supervisor | Key Rules |
|-----------|-----------|-------------------|-----------|
| US BSA/AML | [Yes/No] | [FinCEN + banking regulator] | [31 C.F.R. §§ ...] |
| EU AMLD/AMLR | [Yes/No] | [National CA / AMLA] | [Directive/Regulation] |
| UK POCA/MLR 2017 | [Yes/No] | [FCA / other] | [SI 2017/692] |
| FATF Standards | [Yes] | N/A — international standard | [Relevant recommendations] |

---

## Enterprise Risk Assessment

**Inherent Risk**: [LOW / MEDIUM / HIGH / VERY HIGH]
**Key Risk Drivers**:
- [Driver 1]
- [Driver 2]
**Residual Risk**: [Assessment]

---

## Program Assessment — Five Pillars

### Pillar 1: Internal Controls

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Confidence**: [0.X] — [rationale]

| Control Element | Status | Finding | Remediation |
|----------------|--------|---------|-------------|
| Written AML Policy | [✅/⚠️/❌/🚨] | [Specific finding] | [Specific action] |
| CDD Procedure — Individuals | [✅/⚠️/❌/🚨] | | |
| CDD Procedure — Entities + BO | [✅/⚠️/❌/🚨] | | |
| ... (all checklist items) | | | |

**Summary**: [2-3 sentence narrative on Pillar 1 overall status]

### Pillar 2: BSA/AML Compliance Officer / MLRO

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

[Assessment table]

### Pillar 3: Training Program

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

[Assessment table]

### Pillar 4: Independent Testing / Audit

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

[Assessment table]

### Pillar 5: Customer Due Diligence

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

#### CDD Tier Framework
[Assessment of SDD / CDD / EDD tier design]

#### Individual Customer Onboarding
[Assessment with specific findings]

#### Legal Entity Onboarding and Beneficial Ownership
[Assessment with specific findings]

#### PEP Identification and EDD
[Assessment with specific findings]

---

## Sanctions Screening Assessment

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
[Detailed findings on lists screened, OFAC 50% Rule, hit adjudication]

---

## Transaction Monitoring Assessment

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
[Rule inventory assessment; alert investigation process; tuning documentation]

---

## SAR/CTR Filing Assessment

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
[SAR narrative quality; CTR aggregation; structuring awareness; tipping-off controls]

---

## Remediation Roadmap

### IMMEDIATE (0-30 days)
| Finding | Remediation Action | Owner | Deadline |
|---------|-------------------|-------|----------|
| [Critical deficiency] | [Specific action] | [Role] | [Date] |

### NEAR-TERM (30-90 days)
| Finding | Remediation Action | Owner | Deadline |
|---------|-------------------|-------|----------|
| [Non-compliant item] | [Specific action] | [Role] | [Date] |

### BACKGROUND (90-180 days)
| Finding | Remediation Action | Owner | Deadline |
|---------|-------------------|-------|----------|
| [Partial finding] | [Enhancement action] | [Role] | [Date] |

---

## Regulatory Examination Readiness

**Documentation Readiness**: [X/14 documents examination-ready]
**Key Gaps**: [List]
**Estimated Time to Examination Readiness**: [Assessment]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-aml-kyc-compliance"
  mode: "Assess / Build / Remediate"
  entity_type: "[Entity type]"
  jurisdiction: "[US / EU / UK / Multi]"
  assessment_date: "[Date]"
  legalcode_mcp: "Connected / Not connected"
  research_reference: "Not created"
  critical_deficiencies: [N]
  non_compliant_findings: [N]
  partial_findings: [N]
  compliant_elements: [N]
  citations_verified: "[N VERIFIED] / [N marked [VERIFY]]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Assessment based on information provided; complete program review requires
      access to all current policy documents, CDD files, SAR/CTR logs, and audit reports"
    - "Sanctions list currency not verified — always check current OFAC/OFSI/EU lists"
    - "Regulatory interpretation requires verification with qualified AML counsel"
    - "[Any other specific limitations]"
  reviewer: "AI-assisted — requires review by qualified AML counsel (CAMS/CFCS recommended)"
```

---

*This assessment is AI-assisted and does not constitute legal advice. All findings should
be reviewed by qualified AML counsel and an experienced compliance professional before
use in regulatory submissions or board reports. Regulatory requirements change frequently;
verify current applicability of all cited provisions.*
```

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis for the Legalcode compliance skill
collection. No existing skill on this topic in the repository; created from scratch using
2-agent research pipeline covering: US BSA/AML (31 C.F.R. Part 1010-1030, FinCEN CDD
Final Rule, FinCEN 2024 Proposed Rule, OFAC SDN + 50% Rule, FinCEN Investment Adviser
Final Rule 2024), EU AML Package 2024 (AMLR Reg. 2024/1624, Dir. 2024/1640, AMLD6 Dir.
2018/1673, AMLA Reg. 2024/1620), UK framework (POCA 2002, MLR 2017 SI 2017/692, ECCTA
2023, MLR 2017 domestic PEP amendment January 2024), FATF 40 Recommendations (R.10,
R.12, R.15, R.16, R.20, R.21), FATF Travel Rule June 2024 update, EU EBA Travel Rule
Guidelines (December 2024), 2024 enforcement actions including TD Bank $3.1B penalty,
Bank of America OCC consent order, ICBC BSA/AML consent orders, USAA FSB consent order,
and K&L Gates analysis of 2024 BSA/AML enforcement action patterns.
