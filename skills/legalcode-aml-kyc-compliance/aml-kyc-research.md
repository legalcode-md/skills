# AML/KYC Compliance Skill — Agent 2 Research Output
## Workflow Design & Prompt Engineering Analysis

**Research Date**: 2026-03-02
**Agent**: Agent 2 — Workflow Design & Prompt Engineering Analyst
**Purpose**: Research findings, workflow design, quality frameworks, anti-patterns, and output template for the `legalcode-aml-kyc-compliance` skill.

---

## PART 1: REGULATORY FRAMEWORK OVERVIEW

### 1.1 US Regulatory Landscape

**Primary Statute**: Bank Secrecy Act (BSA), 31 U.S.C. §§ 5311-5336

**Key Regulations**:
- 31 C.F.R. Chapter X (FinCEN regulations)
- 31 C.F.R. § 1020.210 (recordkeeping — banks)
- 31 C.F.R. § 1020.220 (Customer Identification Program — banks)
- 31 C.F.R. § 1010.230 (Beneficial Ownership / CDD Rule — May 2018)
- 31 C.F.R. § 1020.320 (SAR filing — banks)
- 31 C.F.R. § 1010.311 (CTR reporting)
- 31 C.F.R. § 1010.314 (structuring prohibition)
- Anti-Money Laundering Act of 2020 (AMLA 2020), enacted in National Defense Authorization Act

**Supervisory Authorities**:
- FinCEN — rulemaking, enforcement, SAR/CTR receipt
- OCC — national banks and federal savings associations
- FDIC — state non-member banks
- Federal Reserve Board (FRB) — bank holding companies, state member banks
- NCUA — credit unions
- SEC/FINRA — broker-dealers, investment advisers (FinCEN 2028 RIA rule pending)
- CFTC — futures commission merchants
- State banking regulators — state-chartered institutions

**2024–2025 Developments**:
- FinCEN Proposed Rule (July 2024) — replaces checklist compliance with "effective, risk-based, and reasonably designed" standard; adds risk assessment as mandatory fifth program element
- TD Bank $3.09 billion penalty (October 2024) — largest AML penalty ever; $18.3 trillion in transactions left unmonitored; 92% of transaction volume
- OCC Cease-and-Desist against Bank of America (December 2024) — failure to timely file SARs, CDD process deficiencies
- AMLA 2020 implementation continuing — national AML/CFT priorities (June 2024), beneficial ownership database (FinCEN BOI)
- Corporate Transparency Act beneficial ownership reporting: as of 2025, US domestic entities exempt; foreign companies must report by April 25, 2025

### 1.2 EU Regulatory Landscape

**Key Instruments**:
- AMLD6 (Directive 2024/1624/EU, adopted May 30, 2024) — replaces AMLD5; transposition deadline July 10, 2027
- AMLR (Anti-Money Laundering Regulation (EU) 2024/1624) — directly applicable, no transposition needed
- AMLA (Anti-Money Laundering Authority) — operational July 1, 2025; direct supervisory powers over highest-risk entities
- EBA Draft RTS (March 2025) — harmonized CDD methodology, entity risk assessment, AMLA selection criteria
- FATF Recommendations — EU baseline; FATF fourth mutual evaluation round

**Key EU Requirements**:
- Risk-based approach to CDD
- Beneficial ownership register (national registers per Directive)
- PEP identification (expanded to include domestic PEPs — new per AMLD6)
- Enhanced due diligence for high-risk third countries
- AML officer at senior management level
- Internal controls, policies, procedures, training
- Internal audit/independent review

### 1.3 UK Regulatory Landscape

**Post-Brexit Framework**:
- Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (MLR 2017), as amended
- Proceeds of Crime Act 2002 (POCA) — offences, SARs regime
- Terrorism Act 2000 (TACT)
- Financial Services and Markets Act 2000 (FSMA)

**UK Supervisors**:
- FCA — financial services firms
- HMRC — estate agents, accountants, trust/company service providers, money service businesses
- ICAEW, ACCA, Law Society — professional body supervisors

**Key UK Differences from US**:
- "Suspicious Activity Reports" filed with the NCA (not FinCEN)
- Consent regime — "defence against money laundering" (DAML)
- Tipping-off offence (POCA s. 333A)
- No $10,000 threshold equivalent for cash reports (general duty to report all suspicion)
- Politically Exposed Persons — domestic PEPs added with lower risk weighting

---

## PART 2: THE FIVE PILLARS OF BSA/AML COMPLIANCE

The five-pillar model derives from the FFIEC BSA/AML Examination Manual and is the standard framework used by federal bank examiners. Each pillar is assessed independently; failure in any one pillar can constitute a program deficiency.

### Pillar 1: Internal Controls (Policies, Procedures, and Controls)

**Regulatory Basis**: 31 C.F.R. § 1020.210; FFIEC BSA/AML Manual; FinCEN Proposed Rule (2024)

**Required Elements**:
1. **Written AML/BSA Compliance Policy**: Board-approved; reviewed and updated at least annually; describes program scope, reporting obligations, escalation paths
2. **Procedures**: Operational step-by-step procedures for each BSA/AML function (CIP, CDD, EDD, SAR, CTR, record retention)
3. **Internal Controls Structure**:
   - Risk assessment conducted at program outset and periodically updated
   - Customer due diligence processes for onboarding and ongoing monitoring
   - Transaction monitoring controls (automated + manual)
   - Sanctions screening controls (OFAC, EU, UN, UK lists)
   - SAR and CTR reporting workflows
   - Recordkeeping and data retention (5 years minimum under BSA)
4. **Risk Assessment**: Comprehensive institutional risk assessment covering products/services, customers, geographies, and transaction channels; used to calibrate monitoring intensity
5. **Technology Controls**: Automated transaction monitoring system configuration and governance; sanctions screening system logic documented; alert disposition audit trails

**Common Deficiencies** (from 2024 enforcement actions):
- Static risk assessments not updated when business model changes (TD Bank — grew 300% without updating monitoring)
- Transaction monitoring thresholds calibrated too high or never back-tested
- Monitoring system "blacklist" — designed to reduce alerts rather than identify risks
- CDD files incomplete at onboarding; not updated on periodic review
- No documented decision rationale for SAR no-file determinations

### Pillar 2: BSA/AML Compliance Officer

**Regulatory Basis**: 31 C.F.R. § 1020.210(a)(1); FFIEC Manual; FinCEN Proposed Rule (2024)

**Required Elements**:
1. **Designation**: Individual named as BSA/AML Compliance Officer; documented in board minutes or resolution
2. **Seniority and Authority**:
   - Sufficient authority to direct and manage the AML program
   - Direct access to senior management and board
   - Not subordinated to revenue-generating functions where conflicts arise
3. **Qualifications**: Knowledge of BSA/AML regulations, institution's products/services, customer types, geographic risk profile
4. **Independence**: Actual independence from operational and business lines (avoid dual-hatting with revenue functions)
5. **Resources**: Adequate staffing, budget, and technology resources to fulfill compliance obligations
6. **Reporting Line**: Clear reporting to board/audit committee; regular board reports on program status, identified risks, and open findings

**Common Deficiencies**:
- BSA Officer dual-hatted with lending or operations — compromised independence
- BSA Officer without sufficient authority to halt onboarding or exit high-risk customers
- No succession plan or backup designated person
- BSA Officer excluded from new product approval processes
- Insufficient budget/staffing relative to institutional size and risk profile

### Pillar 3: Training Program

**Regulatory Basis**: 31 C.F.R. § 1020.210(a)(3); FFIEC BSA/AML Examination Manual

**Required Elements**:
1. **Scope**: Training for all applicable personnel, tailored by role
2. **Role-Based Curriculum**:
   - **Board of Directors/Senior Management**: BSA/AML obligations, regulatory environment, tone at the top, program oversight responsibilities, enforcement risk
   - **BSA/AML Officer**: Advanced regulatory training; external conferences, seminars, designations (CAMS, CFCS); ongoing education on emerging threats
   - **Front-line/Teller Staff**: Red flag recognition, structuring detection, cash transaction reporting, escalation procedures
   - **Relationship Managers/Account Officers**: CDD requirements, high-risk customer identification, EDD triggers, suspicious activity recognition
   - **Loan Officers**: BSA obligations in lending context, beneficial ownership, SAR obligations
   - **IT/Technology Staff**: System configuration responsibilities, data integrity, audit trail requirements
3. **Timing**:
   - New hire training: within 30–60 days of hire (institution-specific policy; FFIEC best practice)
   - Annual refresher: for all applicable personnel
   - Event-triggered: when significant regulatory changes, new products, or audit findings require update
4. **Documentation**: Attendance records, course materials, test scores, date of completion; retained minimum 5 years
5. **Testing and Assessment**: Knowledge assessments to verify comprehension; remediation for failures

**Common Deficiencies** (2024 enforcement actions):
- Generic training not tailored to institution-specific risks or products
- No training on AML typologies specific to institution's business lines (e.g., trade finance, crypto, MSB relationships)
- Failure to train on specific red flags for institution's customer base
- Training materials outdated — not reflecting recent regulatory changes
- No documentation of board training or board acknowledgment of BSA obligations
- No training records — inability to demonstrate compliance to examiners

### Pillar 4: Independent Testing / Audit

**Regulatory Basis**: 31 C.F.R. § 1020.210(a)(2); FFIEC BSA/AML Manual

**Required Elements**:
1. **Independence**: Auditor must be independent of day-to-day BSA/AML compliance functions; internal audit department with direct board/audit committee access, or qualified external firm
2. **Frequency**: No statutory minimum, but industry standard is annual or 12–18 months based on risk profile; more frequently for high-risk or growing institutions
3. **Scope** (FFIEC-required coverage):
   - Policies, procedures, and controls (written program adequacy)
   - Risk assessment methodology and currency
   - Customer identification program (CIP) compliance
   - Customer due diligence files (sampling — size based on risk profile)
   - Enhanced due diligence files (PEPs, high-risk customers)
   - Sanctions screening system and alert adjudication
   - Transaction monitoring system: rule logic, threshold calibration, alert rates, false positive rates, closure documentation
   - SAR and CTR filings: timeliness, completeness, quality
   - Record retention
   - Training records
   - BSA Officer qualifications and authority
4. **Transaction Testing**: Mandatory — examines actual customer files, monitoring alerts, SAR decisions; sample size should be risk-proportionate
5. **Report and Findings**:
   - Written report to board/audit committee
   - Findings rated by severity
   - Management response and remediation commitments with timelines
   - Follow-up testing to verify closure of prior findings
6. **Work Papers**: Sufficient to permit regulator reliance; examiners may rely on audit work if scope/quality adequate

**Common Deficiencies**:
- Auditor lacks independence (subordinated to BSA function or CCO)
- Insufficient scope — transaction testing absent or sample too small
- Testing covers only policy review, not actual transaction files
- No follow-up to verify remediation of prior findings
- Work papers inadequate — examiner cannot determine testing methodology

### Pillar 5: Customer Due Diligence (CDD) and Ongoing Monitoring

**Regulatory Basis**: 31 C.F.R. § 1010.230 (CDD Final Rule, effective May 11, 2018); FFIEC Manual; FinCEN CDD Rule FAQ

**Four Core Elements of CDD**:
1. **Customer Identification and Verification (CIP)**: Collect and verify name, date of birth, address, identification number (SSN/ITIN/passport/EIN); confirm identity via documentary or non-documentary methods
2. **Beneficial Ownership Identification and Verification**: For legal entity customers — identify and verify natural persons owning 25%+ equity; identify one control prong person (regardless of ownership); use FinCEN Certification of Beneficial Ownership form
3. **Nature and Purpose Understanding**: Develop customer risk profile — expected account activity, products used, transaction types and volumes; business type and industry
4. **Ongoing Monitoring**: Monitor transactions for activity inconsistent with the established risk profile; update customer information when risk-based triggers occur

**FinCEN 2024 Relief**: Institutions need not re-collect beneficial ownership at each new account opening for existing customers — only at periodic review or when risk-based trigger occurs.

---

## PART 3: CDD/KYC ONBOARDING WORKFLOW

### 3.1 Individual Customer Onboarding

**Step 1: Pre-Screening**
- Confirm product/service applicability (is onboarding required? exemptions apply?)
- Initial name check against OFAC SDN and related designations list
- Initial PEP screening
- Adverse media screening

**Step 2: Identity Documentation Collection**
Required (US CIP — 31 C.F.R. § 1020.220):
- Government-issued photo ID (passport, driver's license, national ID)
- Date of birth
- Residential address (utility bill, bank statement < 90 days if address differs from ID)
- Taxpayer Identification Number (SSN, ITIN, or foreign equivalent)

**Step 3: Identity Verification**
Two methods available:
- **Documentary**: Review original or certified copy of government-issued ID; confirm authenticity markers
- **Non-documentary / Electronic**: Database checks (credit bureau, identity verification vendors — Jumio, Onfido, IDEMIA, LexisNexis); biometric liveness check; phone/email verification

**Step 4: Risk Profile Development**
- Source of funds / source of wealth (employment, business, investments, inheritance)
- Expected transaction patterns (frequency, amounts, geographic scope)
- Products/services requested
- Occupation and employer
- Initial risk tier assignment: Low / Medium / High / Very High

**Step 5: PEP and Sanctions Rescreening**
- Confirm clear sanctions hit adjudication
- PEP status determination: Yes/No; if Yes → EDD required
- Document PEP determination in file

**Step 6: Onboarding Decision**
- Standard CDD: Low/Medium risk — proceed to onboarding
- Enhanced CDD: High/Very High risk — senior management approval; additional document collection
- Decline: OFAC true match, adverse determination, or insufficient information

**Step 7: Account Setup with Risk Tier**
- Risk tier recorded in customer management system
- Monitoring parameters set per tier
- Next periodic review date scheduled

### 3.2 Legal Entity Onboarding

**Step 1: Entity Verification**
- Registered name; jurisdiction of incorporation
- Articles of incorporation / certificate of good standing
- Operating/partnership agreement (if LLC/partnership)
- State business registration search (Secretary of State)

**Step 2: Beneficial Ownership Collection (31 C.F.R. § 1010.230)**
- FinCEN Certification of Beneficial Ownership form
- Identify all natural persons owning 25%+ of equity interests
- Identify one control prong person (any executive/officer/director with control)
- Collect for each BO: name, date of birth, address, SSN/passport, percentage ownership
- Verify BO identity using CIP-equivalent procedures
- Aggregate ownership through entity layers — apply OFAC 50% rule logic

**Step 3: Business Purpose Documentation**
- Nature of business (industry, SIC/NAICS code)
- Years in operation; key customers and suppliers (if high-risk industry)
- Anticipated transaction activity (volume, frequency, currencies, geographic scope)
- Business relationships with foreign correspondents or jurisdictions

**Step 4: Authorized Signatories / Officers**
- Resolution authorizing account opening
- Government-issued ID for each authorized signatory
- CIP verification for signatories

**Step 5: Entity-Level Risk Assessment**
Risk factors to evaluate:
- Industry risk (cash-intensive, MSB, cannabis [where legal], real estate, crypto/VASP)
- Geographic risk (high-risk jurisdictions, FATF greylist/blacklist countries)
- Ownership structure complexity (layered entities, offshore jurisdictions, nominee shareholders)
- Business model transparency (clear vs. opaque)
- Source of funds (equity investment, debt, revenue)

**Step 6: Senior Management Approval (for High-Risk Entities)**
Required for:
- PEP-owned or PEP-controlled entities
- Entities with beneficial owners in sanctioned jurisdictions
- High-risk industries: MSBs, casinos, cannabis, arms dealers, precious metals dealers
- Shell companies / holding companies with no discernible operational activity

**Step 7: EDD Package Completion (if High-Risk)**
Additional materials:
- Financial statements or audited accounts
- Professional references (legal counsel, accountant)
- Contracts with major customers/suppliers
- Source of wealth documentation for owners
- Senior management approval memorandum

---

## PART 4: RISK-BASED CUSTOMER RISK SCORING

### 4.1 Risk Tier Definitions

| Tier | Description | Review Frequency | Monitoring Intensity |
|------|-------------|-----------------|----------------------|
| Low | Individual, domestic, salaried/W-2, low transaction volume, known employer | 36 months | Standard automated monitoring |
| Medium | Small business, moderate complexity, limited geographic diversity | 24 months | Standard monitoring + periodic manual review |
| High | Cash-intensive business, high transaction volume, cross-border activity, adverse media, foreign beneficial owner | 12 months | Enhanced monitoring, lower alert thresholds |
| Very High | PEP, high-risk jurisdiction, MSB, cannabis, correspondent banking, sanctioned-jurisdiction nexus | 6 months | Intensive monitoring, relationship manager review, senior management oversight |
| Prohibited | OFAC SDN / blocked person, designated terrorist, established criminal nexus | N/A — no relationship | No account; report as appropriate |

### 4.2 Risk Factor Matrix

**Geography Risk (25–35% weight)**
- Country of residence / incorporation
- Counterparty jurisdictions
- FATF greylist countries: elevated risk
- FATF blacklist / OFAC sanctioned countries: very high / prohibited
- Basel AML Index score
- Corruption Perceptions Index (Transparency International)
- EU high-risk third country list

High-risk geographic indicators:
- Iran, North Korea, Syria, Cuba, Russia (sanctions programs) — very high
- Myanmar, Democratic Republic of Congo, Panama (FATF greylist — verify current list)
- Offshore financial centers (BVI, Cayman, Seychelles) — elevated
- Jurisdictions with bank secrecy laws that impede UBO disclosure — elevated

**Customer Type Risk (20–30% weight)**
- Natural person, employed, domestic — low
- Self-employed / sole proprietor — medium
- Private company / LLC — medium to high (depends on complexity)
- Public company (listed) — low-medium (disclosure obligations apply)
- Non-profit / NGO — medium to high (terrorist financing risk)
- PEP / PEP-connected — high to very high
- Money Service Business — high
- Cash-intensive business (restaurant, retail, car wash) — medium to high
- Cannabis-related business (legal state) — high
- Virtual asset service provider (VASP) — high
- Correspondent bank / foreign bank — high

**Products / Services / Channels Risk (15–20% weight)**
- Checking/savings accounts — low
- Wire transfers (international) — medium to high
- Cash deposits / currency exchange — high
- Prepaid cards / digital wallets — medium to high
- Trade finance / letters of credit — medium to high
- Private banking / wealth management — high
- Correspondent banking — high
- Cryptocurrency on/off ramps — high

**Transaction Pattern Risk (15–20% weight)**
- Volume consistent with stated business purpose — low
- Transactions approaching $10,000 CTR threshold — high (structuring indicator)
- Large, infrequent wire transfers — medium
- Round-dollar transactions — elevated
- Rapid movement of funds (funds-in, immediately funds-out) — very high
- Transactions with high-risk jurisdictions — high
- Unusual geographic dispersion — medium to high

**Customer Behavior Risk (10–15% weight)**
- Minimal adverse media — low
- Adverse media hits: criminal activity, corruption, fraud — high to very high
- Reluctance to provide information — high
- Inconsistent information between application and documentation — high
- Prior SAR filings — high
- Prior account closures at other institutions — high (if known)

### 4.3 Risk Score Calculation

Approach: Weighted additive model

```
Risk Score = (Geography Weight × Geography Score)
           + (Customer Type Weight × Customer Type Score)
           + (Product/Channel Weight × Product Score)
           + (Transaction Pattern Weight × Transaction Score)
           + (Behavior Weight × Behavior Score)
```

Each factor scored 1–5 (1 = lowest risk, 5 = highest risk).
Composite score maps to tier:
- 1.0–2.0 → Low
- 2.1–3.0 → Medium
- 3.1–4.0 → High
- 4.1–5.0 → Very High

**Override Rules**:
- Confirmed OFAC match → Prohibited (regardless of score)
- Confirmed PEP → Minimum High (regardless of other factors)
- Beneficial owner in sanctioned jurisdiction → Minimum High
- Prior OFAC enforcement action against customer → Very High
- Adverse media: criminal conviction → High (minimum)

### 4.4 Periodic Review Triggers

**Time-Based Reviews**:
- Low: every 36 months
- Medium: every 24 months
- High: every 12 months
- Very High / PEP: every 6 months

**Event-Based Review Triggers**:
- Adverse media or negative news involving the customer
- Sanctions list hit (new designation or name variant match)
- Transaction pattern materially inconsistent with established profile
- SAR filed on the customer
- Change in beneficial ownership or control structure
- Customer informs institution of material business change
- Geographic relocation to higher-risk jurisdiction
- Regulatory inquiry or law enforcement order regarding the customer
- Change in customer relationship manager with knowledge of unusual activity
- Account becomes dormant then suddenly reactivates

---

## PART 5: SANCTIONS SCREENING WORKFLOW

### 5.1 Lists to Screen

**OFAC Lists (US)**:
- Specially Designated Nationals and Blocked Persons (SDN) List — primary list
- Foreign Sanctions Evaders (FSE) List
- Sectoral Sanctions Identifications (SSI) List
- Non-SDN Menu-Based Sanctions List (NS-MBS)
- Palestinian Legislative Council List
- Consolidated Sanctions List (all OFAC programs combined)

**Other US Lists**:
- Bureau of Industry and Security (BIS) Entity List, Denied Persons List, Unverified List
- State Department Debarred Parties List
- FinCEN 314(a) requests (shared confidentially; not public)

**EU Lists**:
- EU Consolidated Financial Sanctions List (CFSP)
- EU Asset Freeze and Travel Ban Lists
- EU Sectoral Sanctions (Russia — Regulations 833/2014, 269/2014)

**UK Lists**:
- OFSI UK Consolidated List of Financial Sanctions Targets
- UK Russia Regulations lists

**UN Lists**:
- UN Security Council Consolidated Sanctions List (maintained by 1267/1988/2253 Committee — Al-Qaida/Taliban)

**Other Lists**:
- World Bank Debarment List
- INTERPOL Red Notices (not legally binding, risk-based consideration)
- National law enforcement watchlists (institution-specific)

### 5.2 OFAC 50 Percent Rule

**Rule**: Any entity owned 50% or more in the aggregate by one or more SDN-designated persons is itself treated as blocked, even if the entity itself is not listed on the SDN.

**Aggregation**:
- If SDN-A owns 25% and SDN-B owns 25% of Entity X → Entity X is blocked (50% aggregate)
- Ownership is traced through multiple layers (indirect ownership counts)
- Must look through each ownership layer

**Compliance Requirements**:
- Institutions must have procedures to trace beneficial ownership to identify 50% rule application
- Screening tools must support ownership structure visualization
- Where uncertainty exists, escalate to Compliance for determination
- OFAC FAQ No. 398 addresses 50% rule implementation

### 5.3 Screening Process

**Onboarding Screening**:
1. Screen customer name (all name variants, aliases, DBA names) against all applicable lists
2. Screen all beneficial owners (all individuals meeting CDD thresholds)
3. Screen all authorized signatories and directors
4. Screen registered addresses against geographic embargoes (OFAC country-based programs: Iran, Cuba, Syria, North Korea, Crimea/Donetsk/Luhansk)
5. Apply fuzzy matching logic — account for:
   - Name transliteration variants (Arabic, Cyrillic, Chinese character transliterations)
   - Name reordering (First/Last name swap)
   - Common spelling variations and nicknames
   - Maiden name / previous names

**Ongoing Screening**:
- At-event screening: trigger screening on any transaction involving a newly-listed party
- Periodic rescreening: full screening against current lists at minimum annually; higher frequency for high-risk customers
- Real-time transaction screening for wire transfers and payments

**Alert Adjudication**:
1. **True Match**: SDN designated party confirmed → block transaction; contact OFAC (if blocking required); file OFAC blocked property report within 10 business days; contact legal counsel
2. **False Positive**: Name similarity but different person confirmed → document determination with supporting evidence (DOB, nationality, address differentiates); close alert with rationale
3. **Potential Match / Insufficient Information**: Escalate to senior Compliance; request additional information from customer; withhold transaction until resolved
4. **OFAC License**: Where blocking required but license may be available → apply to OFAC for specific or general license as appropriate

### 5.4 Hit Adjudication Documentation Requirements

For each alert:
- Alert ID and date generated
- List(s) that generated the hit
- Name(s) that generated the hit
- Screening analyst name and date of review
- Determination: True Match / False Positive / Inconclusive
- Supporting rationale (specific differentiating factors for false positive)
- Escalation chain if applicable
- Senior Compliance sign-off for any inconclusive determination
- Retention: minimum 5 years

---

## PART 6: PEP IDENTIFICATION AND EDD PROCESS

### 6.1 PEP Categories

**Category 1: Current Heads of State and Government**
- President, Prime Minister, Monarch, Head of Government
- Members of national legislative bodies (parliament, congress, senate)
- Members of supreme courts, constitutional courts
- Senior military officials (general officer grade)
- Senior government officials: ministers, deputy ministers, ambassadors
- Members of governing bodies of central banks, audit courts

**Category 2: Senior Party Officials**
- Senior officials of political parties (not just ruling party)
- Senior officials of international organizations (UN, World Bank, IMF, EU institutions, regional development banks)

**Category 3: State-Owned Enterprise Executives**
- Board members and senior management of SOEs
- Country-specific definition varies; EU AMLD6 requires consistent identification

**Category 4: Family Members and Close Associates**
- Spouse/domestic partner (legal and de facto)
- Children and their spouses/partners
- Parents
- "Close associates": business partners with significant joint assets; trusted advisors; known associates in business dealings

**AMLD6 Change** (effective July 2027): Both foreign and domestic PEPs subject to EDD (AMLD5 allowed lower-risk treatment for domestic PEPs); domestic PEPs may have risk reassessment downward based on demonstrated lower risk profile.

### 6.2 PEP Screening Database Vendors (Commercial)

| Vendor | Product | Coverage | Notes |
|--------|---------|----------|-------|
| LSEG (formerly Refinitiv) | World-Check | Global; ~3.5M profiles | Most widely used |
| LexisNexis Risk Solutions | WorldCompliance | Global; integrated with news | Strong US coverage |
| Dow Jones Risk & Compliance | Dow Jones Risk Center | Global; includes adverse media | Strong SOE/government data |
| Moody's (GRID/Orbis) | GRID, Orbis Watchlist | Corporate ownership + PEP | Strong UBO tracing |
| ComplyAdvantage | ComplyAdvantage | Dynamic/ML-enriched | Real-time adverse media |
| Acuris/Mergermarket | Acuris Risk Intelligence | M&A/news focus | |
| Trulioo | GlobalGateway | Identity verification + PEP | |

**Important**: No PEP database is exhaustive. Institutions should:
- Use at least one commercial database
- Supplement with public source searches for high-risk individuals
- Document database version and search date
- Perform periodic re-screening against updated databases

### 6.3 EDD Requirements for PEPs

**Documentation Required**:
1. Source of Wealth (SOW): Origin of the customer's entire accumulated wealth (e.g., employment, inheritance, business, investments)
   - Documentation: employment/income verification, business ownership documents, inheritance records, investment account statements
   - Verification: assess plausibility against known information about public sector salary/wealth in relevant jurisdiction
2. Source of Funds (SOF): Origin of specific funds being deposited or used in the transaction
   - Documentation: recent pay stubs, bank statements, business accounts, sale proceeds documentation
3. Anticipated Transaction Activity: Detailed expected transaction profile
4. Public Role Confirmation: Confirm current or former public role from public sources
5. Nature of Public Role: Duration, scope, authority level
6. Corroboration of No Derogatory Information: Comprehensive adverse media search; PEP database screening; regulatory enforcement database check

**Process Requirements**:
- Senior Management Approval: Required before establishing relationship with PEP or PEP-related entity
- Ongoing Enhanced Monitoring: More frequent transaction reviews; lower alert thresholds
- Annual EDD Refresh: Update SOW/SOF documentation and re-confirm no adverse developments

### 6.4 De-PEP Timeline

**General Rule**: Former PEPs retain elevated risk status for a period after leaving public office.

**Market Practice / Regulatory Guidance**:
- FATF: Countries should assess risk when PEP leaves position; no mandatory universal timeline
- UK FCA: De-PEP assessment after minimum 12 months post-departure from public role
- EU AMLD6: Risk-based de-PEP — consider level of influence; 12–18 months typical minimum
- US: No specific timeline; risk-based approach

**De-PEP Criteria (must evaluate all)**:
1. Time since departure from public role (minimum 12 months; typically 18–24 months)
2. Nature and seniority of former role
3. Ongoing political influence or connections
4. Ongoing source of wealth related to public role (e.g., government contracts post-office)
5. Adverse media developed since departure
6. Any formal investigation or prosecution arising from public role

**Documentation**: De-PEP determination must be documented in the customer file with rationale; sign-off by senior Compliance.

---

## PART 7: TRANSACTION MONITORING

### 7.1 Rule-Based Monitoring Scenarios

**Structuring and Cash Activity**:
- **Structuring Detection Rule**: Cash transactions in multiple amounts each below $10,000, totaling >$10,000 in a defined period (typically 7-day rolling or 30-day rolling), occurring at same branch or across branches with knowledge
- **Near-Threshold Rule**: Cash transactions between $9,000–$9,999 in rolling 30-day period
- **Large Cash Deposit Rule**: Any single cash deposit exceeding $10,000 (triggers CTR review)
- **Rapid Cash Cycling**: Multiple cash deposits followed by immediate wire transfer out

**Wire Transfer Activity**:
- **High-Volume Wire Rule**: Total wire transfers (in or out) exceeding defined threshold (e.g., $50,000 USD equivalent) in 30-day rolling period — threshold should be risk-calibrated per customer tier
- **Geographic Concentration Rule**: Wire transfers to/from FATF greylist or high-risk jurisdictions
- **Round-Dollar Wire Rule**: Wire transfers in exact round amounts (e.g., $50,000.00, $100,000.00) with no cents — indicator of negotiated or pre-arranged amounts
- **Pass-Through Activity**: Funds in and funds out within 24–72 hours, same or similar amounts, no apparent business purpose (layering indicator)
- **Multiple Small Wires (Smurfing)**: Multiple wire transfers just below SWIFT reporting thresholds

**Account Activity Rules**:
- **Dormant Account Reactivation**: Account with <3 transactions in prior 12 months suddenly shows high activity
- **Velocity Spike**: Transaction count or value increases >200% compared to 90-day baseline
- **Geographic Mismatch**: ATM withdrawals or card transactions in jurisdiction inconsistent with customer's residence/business location
- **Business Account Mismatch**: Transaction types inconsistent with stated business purpose (e.g., restaurant account receiving large wire transfers from overseas)

**Correspondent and Payment Activity**:
- **Nested Correspondent Activity**: Funds flows showing characteristics of nested accounts (payments on behalf of undisclosed third parties)
- **Trade Finance Red Flags**: Over/under-invoicing indicators; unusual payment terms; payments to countries not associated with stated trade route

**Automated System Configuration**:
- Thresholds should be calibrated to the institution's customer population and risk profile
- Back-testing required: alert rate and false positive rate should be documented
- Model risk governance: annual model validation for key monitoring rules
- Exception-based escalation: high-volume false positives should trigger threshold review, not suppression

### 7.2 L1/L2 Alert Investigation Process

**Level 1 (L1) Review — AML Analyst**:
1. Receive alert assignment from case management system
2. Review alert details: customer profile, transaction history, alert rule triggered
3. Review customer file: CDD information, expected activity profile, prior alerts/SARs
4. Conduct additional research: adverse media search, sanctions rescreen, regulatory database
5. Decision matrix:
   - **Close (False Positive)**: Alert does not indicate suspicious activity; rationale documented in 3–5 sentences; no SAR required
   - **Escalate to L2**: Cannot determine benign or suspicious at L1; requires additional investigation
   - **Recommend SAR**: Suspicious activity identified; document findings; escalate to L2 for SAR determination
6. **SLA**: L1 review complete within 5 business days of alert generation (institution-specific)

**Level 2 (L2) Review — Senior Analyst / AML Investigator**:
1. Review L1 finding and supporting documentation
2. Conduct enhanced investigation: customer interview (if appropriate), internal data mining, public records research
3. If pattern review required: review full transaction history for 12–24 months
4. **SAR Decision**:
   - **File SAR**: Suspicious activity confirmed or cannot be ruled out; file within 30 calendar days of initial detection (60 days if ongoing investigation requires additional time — one extension maximum per FinCEN guidance)
   - **No File — Document**: Suspicious activity determined to be absent or explainable; document rationale in compliance with FinCEN no-file guidance; retain for 5 years
   - **Continue Investigation**: New information expected within 30 days; extend timeline (document extension reason)
5. **Ongoing Monitoring Flag**: If no SAR filed but activity warrants enhanced monitoring, flag account for heightened surveillance

### 7.3 SAR Decision Tree

```
ALERT GENERATED
     ↓
L1 Analyst Review
     ↓
Is activity consistent with customer profile and known business purpose?
  YES → Close as False Positive (document rationale, retain 5 years)
  NO → Escalate to L2
     ↓
L2 Investigator Review
     ↓
Is additional information needed?
  YES → Request info / conduct enhanced research (document, set 30-day deadline)
  NO → Continue to SAR determination
     ↓
Can suspicious activity be explained by legitimate means?
  YES → No SAR; document "no file" rationale thoroughly
  NO → Proceed to SAR filing
     ↓
Does activity meet SAR threshold (transaction ≥ $5,000 for banks; ≥ $2,000 for MSBs)?
  YES → File SAR (within 30 days; 60 days if ongoing)
  NO → Consider whether FinCEN voluntary SAR appropriate
     ↓
SAR Preparation
  → 5 Ws narrative (Who, What, When, Where, Why/How)
  → Check all applicable SAR checkboxes
  → Senior Compliance review and approval
  → File via FinCEN BSA E-Filing System
  → Retain copy + retain records of related transactions (5 years)
     ↓
TIPPING-OFF PROHIBITION: Do not disclose SAR filing or existence to subject
     ↓
Post-Filing: Continue monitoring; file continuing SARs every 90-120 days if activity continues
```

---

## PART 8: SAR AND CTR FILING PROCESS

### 8.1 SAR Filing Requirements

**Statutory Basis**: 31 U.S.C. § 5318(g); 31 C.F.R. § 1020.320 (banks)

**Filing Thresholds**:
- Banks: $5,000 or more (or $25,000 where no suspect identified — VERIFY current thresholds)
- MSBs: $2,000 or more
- Casinos: $5,000 or more
- Securities broker-dealers: $5,000 or more

**Filing Deadline**:
- Initial SAR: 30 calendar days from the date of initial detection of the suspicious transaction
- Extended deadline: 60 calendar days if additional evidence needed for complex cases; must document extension reason
- Continuing activity: File continuing SAR every 90-day period after prior SAR filing (FinCEN FAQ guidance: every 90 days with filing deadline of 120 days from prior SAR)

**Mandatory SAR Scenarios** (FFIEC Manual guidance):
- Insider abuse: any amount
- Violations involving $5,000+ where suspect can be identified
- Violations involving $25,000+ regardless of suspect identification
- Transactions involving known or suspected terrorist financing: any amount
- Computer intrusion: any amount
- Money laundering activity: threshold applies

**SAR Narrative Quality Standards — The 5 Ws**:
- **WHO**: Complete description of subject (name, address, DOB, ID number, account number, occupation, position in company if entity); known associates
- **WHAT**: Detailed description of the suspicious activity; specific transaction types, amounts, counterparties, instruments used; the pattern as a whole
- **WHEN**: Date range of suspicious activity; specific dates of key transactions; relationship to triggering events
- **WHERE**: Accounts, branches, geographic locations; jurisdictions involved; wire transfer corridors
- **WHY / HOW**: Why the activity is suspicious — what makes it inconsistent with the customer's legitimate business or profile; the theory of the suspicious activity (layering, structuring, fraud, etc.)

**Narrative Quality Anti-Patterns**:
- "Unusual activity" without specific description — insufficient
- Copy-paste of transaction data without explanation of why suspicious — insufficient
- Failure to describe the pattern; focus only on individual transactions — insufficient
- No connection drawn between transactions and money laundering typology
- Missing subject identifying information when available

**Tipping-Off Prohibition** (31 U.S.C. § 5318(g)(2)):
- SAR existence and contents are confidential
- Do not tell the customer a SAR has been or may be filed
- Do not respond to customer inquiries about SAR filings
- Safe harbor for good-faith SAR filing: 31 U.S.C. § 5318(g)(3)
- UK equivalent: POCA s. 333A tipping-off offence

**SAR Lookback**:
- When new information is received about a subject on whom a prior SAR was filed, assess whether the new information requires an amended SAR or a new SAR
- Lookback reviews (required under some consent orders): retrospective review of transactions over defined period to identify SAR filing misses

### 8.2 CTR Filing Requirements

**Statutory Basis**: 31 U.S.C. § 5313; 31 C.F.R. § 1010.311

**Filing Threshold**: Cash transactions (currency in or out) exceeding $10,000 in a single business day

**Aggregation Rule**: Multiple transactions by or on behalf of the same person in a single business day must be aggregated; institution must have "knowledge" that transactions are by or for the same person (same bank teller, same account, transaction presented for same customer)

**Filing Deadline**: 15 calendar days after the date of the transaction (electronic filing required since July 2012)

**CTR Exemptions** (31 C.F.R. § 1020.315):
- Phase I Exempt Persons: Banks, government agencies, listed public companies, subsidiaries of public companies (automatic exemption)
- Phase II Exempt Persons: Non-listed businesses, payroll customers (requires filing of FinCEN Form 110 to designate exemption)

**Currency Transaction Review Process**:
1. Teller/cashier identifies cash transaction exceeding $10,000
2. Collect customer identification (for non-account holders: name, address, ID)
3. Aggregate with any other cash transactions in same business day
4. Complete FinCEN Form 112 electronically via BSA E-Filing
5. File within 15 days

**Common CTR Errors**:
- Failure to aggregate related transactions across tellers/branches
- Exemption file not maintained or expired
- Incorrect customer information in CTR
- Filing delay beyond 15-day deadline
- Failure to file CTR for cash equivalent transactions (monetary instruments, money orders) — note: thresholds differ by transaction type

---

## PART 9: INDEPENDENT AUDIT / TESTING

### 9.1 Audit Program Design

**Frequency**: Annually (best practice); 12–18 months maximum for risk-based approach; more frequently for high-risk or rapidly changing institutions

**Independence Requirements**:
- Internal audit: must report directly to board/audit committee; BSA/AML Officer cannot direct or control audit scope or conclusions
- External audit: qualified independent firm with demonstrated BSA/AML expertise; engagement partner not from operational team; no operational consulting relationship that creates conflict
- Prohibited: BSA Officer performing self-assessment and calling it "independent testing"

**Audit Scope (FFIEC-Required Coverage)**:

1. **Program Adequacy**
   - Written AML policy: current, board-approved, comprehensive
   - Procedures: complete, operational, accurate
   - Risk assessment: current, comprehensive, basis for program calibration

2. **Customer Identification Program (CIP)**
   - CIP procedures vs. regulatory requirements
   - File review sample: completeness of ID documentation
   - Verification method documentation
   - Exception tracking and clearing

3. **Customer Due Diligence**
   - CDD procedures adequacy
   - File review sample: beneficial ownership documentation complete
   - EDD files for high-risk customers: complete, approved, current
   - PEP identification and EDD documentation

4. **Transaction Monitoring**
   - System documentation: rule descriptions, threshold logic, parameters
   - Alert volume and false positive rate analysis
   - L1/L2 process compliance: timeliness, documentation quality
   - SAR/no-file determination documentation
   - Back-testing: are thresholds calibrated appropriately?

5. **Sanctions Screening**
   - Lists screened vs. all applicable lists
   - Fuzzy matching configuration
   - Alert adjudication documentation
   - 50% rule implementation

6. **SAR Filing**
   - SAR timeliness: measured against 30-day / 60-day deadline
   - SAR quality: narrative completeness per 5 Ws standard
   - Continuing SAR tracking
   - No-file documentation
   - Lookback completeness

7. **CTR Filing**
   - CTR timeliness and completeness
   - Aggregation procedures
   - Exemption file maintenance

8. **Training**
   - Training materials: content adequacy, currency
   - Training records: completeness, all applicable staff included
   - New hire training timeliness
   - Board training documentation

9. **BSA Officer Qualification and Authority**
   - Role documented; reporting line appropriate
   - Training and continuing education documented
   - Resources: staffing and budget

10. **Recordkeeping**
    - Retention policy: 5-year minimum compliance
    - Document retrieval capability

### 9.2 Audit Report Components

1. **Executive Summary**: Overall program assessment; key findings; ratings
2. **Methodology**: Scope, testing approach, sample sizes, date of fieldwork, auditor qualifications
3. **Findings by Area**:
   - Finding description
   - Regulatory/policy reference
   - Risk rating: Critical / High / Medium / Low / Informational
   - Root cause analysis
   - Recommended remediation
4. **Management Response**: For each finding — agree/disagree, remediation plan, responsible owner, target completion date
5. **Prior Period Follow-Up**: Status of prior audit findings
6. **Work Papers**: Sufficient detail for examiner reliance
7. **Distribution**: Board/Audit Committee; BSA/AML Officer; Senior Management; (as applicable) external auditors

### 9.3 Regulatory Examination Preparation

**Documents to Prepare**:
- Current risk assessment
- AML policy and procedures (current versions)
- Organizational chart (BSA/AML function, reporting lines)
- BSA Officer resume and training records
- Independent audit reports (current and prior 3 years)
- Audit management responses and remediation tracking
- Training materials and completion records
- CDD file samples (examiner will select; prepare to retrieve quickly)
- SAR log (do not provide SAR contents without legal counsel review — SAR confidentiality)
- CTR records and exemption file
- Transaction monitoring system documentation: rule descriptions, thresholds, alert metrics
- False positive rate analysis
- Sanctions screening program documentation
- Model validation reports (if applicable)
- Board minutes approving AML policy; board AML report

**Exam Hot Topics (2024–2025)**:
1. **Crypto/VASP Customer CDD**: Documentation for virtual asset service providers; VASP registration status; travel rule compliance
2. **Trade-Based Money Laundering**: Monitoring for trade finance transactions; invoice validation; shipping document review
3. **Beneficial Ownership / CTA**: Implementation of CDD Rule; coordination between CDD Rule and CTA BOI database
4. **AI-Based Monitoring**: Model risk governance for ML-based monitoring; explainability; validation; human review requirements
5. **BaaS / Fintech Partnerships**: Sponsor bank oversight of fintech AML programs; contractual requirements; oversight testing
6. **Cannabis Banking**: CDD for cannabis-related businesses; state law compliance documentation; risk-based approach
7. **Real Estate / Geographic Targeting Orders**: Implementation of FinCEN GTOs for cash real estate purchases
8. **Elder Financial Exploitation**: SAR filing for suspected elder financial exploitation; coordination with Adult Protective Services
9. **Correspondent Banking**: Correspondent account due diligence; nested accounts; payable-through accounts
10. **Investment Adviser Rule (FinCEN 2028)**: RIA AML program development and implementation

---

## PART 10: TRAINING PROGRAM DESIGN

### 10.1 Role-Based Training Curricula

**Curriculum Tier 1: Board of Directors and C-Suite (Annual; 2–3 hours)**
- BSA/AML regulatory environment and key requirements
- Institution's AML risk profile summary
- Recent enforcement actions and industry trends
- Board's fiduciary oversight responsibilities
- Culture of compliance and tone at the top
- Summary of program status: open findings, SAR/CTR metrics, training completion rates
- Material changes to program since last board report

**Curriculum Tier 2: BSA/AML Officer (Ongoing; advanced external training minimum annually)**
- Advanced BSA/AML regulation (FinCEN guidance, agency guidance, case law)
- Emerging typologies and red flags (FinCEN SARs activity review, FinCEN advisories)
- Sanctions programs — OFAC/OFSI/EU sanctions updates
- FATF mutual evaluation outcomes and typologies
- AML technology developments (AI/ML monitoring, identity verification)
- Regulatory exam priorities
- Certifications: ACAMS (Certified Anti-Money Laundering Specialist), CFCS (Certified Financial Crime Specialist), ACFCS, ICA (International Compliance Association)
- External: ACAMS conferences, FFIEC training, regional banking association events

**Curriculum Tier 3: Relationship Managers / Account Officers (Annual; 2–3 hours)**
- CDD and beneficial ownership requirements: what must be collected; when to update
- High-risk customer types: identification and escalation
- EDD triggers and process
- Red flags for suspicious activity in customer interactions
- SAR referral process: how to make an internal referral
- How to handle customer questions about reporting (avoid tipping-off)
- New products/services red flag recognition
- Specific typologies for institution's business lines

**Curriculum Tier 4: Front-Line / Teller / Branch Staff (Annual; 1–2 hours)**
- BSA overview: why it matters; penalties for violations
- Cash transaction reporting: when and how to file CTR
- Structuring: identification and prohibition against participation
- Customer identification: CIP requirements for transactions
- Red flag recognition: unusual behavior, evasiveness, questions about reporting thresholds
- Escalation: how to escalate a concern to BSA/Compliance
- Suspicious activity referral process
- Specific red flags for branch-level products

**Curriculum Tier 5: IT / Technology Staff (Annual; 1–2 hours)**
- Data integrity requirements: BSA records must be accurate and retrievable
- System change management: impact on monitoring and reporting
- Audit trail requirements: what system logs must be retained
- Incident response: data breaches affecting AML systems
- Alert suppression prohibition: not authorized to suppress monitoring alerts

### 10.2 Documentation Requirements

- Training completion records: name, date, course, version, score (if tested)
- Attendance logs for in-person sessions
- Course materials version control (to demonstrate content at time of training)
- Exception tracking: employees who missed training; remediation plans
- Exam-ready: complete records for all employees for at least prior 5 years (or length of employment)
- Board training: board minutes or signed acknowledgment; materials distributed
- New hire training: specific records confirming completion within required timeframe

---

## PART 11: SKILL WORKFLOW DESIGN

### 11.1 Overview

The `legalcode-aml-kyc-compliance` skill operates in one of three modes:
1. **Assessment Mode**: Review an existing AML program against the five-pillar framework and produce a gap report
2. **Build Mode**: Design an AML program from scratch for a new or unregulated entity
3. **Deep-Dive Mode**: Focused review of one specific component (e.g., CDD procedures, transaction monitoring, SAR quality)

### 11.2 Detailed Workflow (12 Steps)

**STEP 1: Accept Input**

Inputs accepted:
- Plain text description of entity and existing program
- File references (CDD policy, AML policy, training records, audit report)
- URL to publicly available regulatory order or consent decree
- User-described scenario

On input receipt, identify:
- Entity name (or type description)
- Input type: (a) existing program for assessment, (b) new program to build, (c) specific component review
- Geographic scope: US-only, EU-only, UK-only, multi-jurisdictional
- Regulatory context: type of regulated entity (bank, MSB, broker-dealer, RIA, non-bank FI)

---

**STEP 2: Interactive Context Gathering [CLARIFY Checkpoint]**

Before proceeding, gather structured context using targeted questions:

**CLARIFY Set A — Entity Classification**
```
Q1: What type of financial institution or regulated entity is this?
   (a) Federally chartered or state-chartered bank (national bank, state bank, savings association)
   (b) Credit union
   (c) Money Service Business (MSB): money transmitter, currency exchanger, check casher, prepaid card issuer
   (d) Broker-dealer or investment adviser (securities)
   (e) Futures commission merchant or introducing broker
   (f) Insurance company (life insurance, annuities)
   (g) Non-bank fintech / payment company
   (h) Casino or card club
   (i) Other (describe)
   Why this matters: Applicable regulations, thresholds, and supervisory authority differ significantly by entity type.
```

```
Q2: What is the primary jurisdiction?
   (a) United States only
   (b) United States + EU operations
   (c) United States + UK operations
   (d) EU Member State only (specify country)
   (e) United Kingdom only
   (f) Multi-jurisdictional (specify)
   Why this matters: Regulatory framework, PEP definitions, sanctions lists, and filing requirements differ by jurisdiction.
```

```
Q3: What is the approximate asset size / transaction volume?
   (a) Community / small: < $1B assets or < $5B annual transactions
   (b) Mid-size: $1B–$50B assets or $5B–$100B annual transactions
   (c) Large: > $50B assets or > $100B annual transactions
   Why this matters: Program sophistication expectations and examiner scrutiny scale with size.
```

**CLARIFY Set B — Products/Services Risk Profile**
```
Q4: What are the primary products and services?
   [Select all that apply]
   (a) Retail deposit accounts / consumer banking
   (b) Commercial / business banking
   (c) Wire transfer services (domestic and/or international)
   (d) Cash services (significant cash deposits/withdrawals)
   (e) Trade finance / letters of credit
   (f) Correspondent banking
   (g) Private banking / wealth management
   (h) Securities brokerage / investment advisory
   (i) Cryptocurrency / digital asset services
   (j) Prepaid cards / digital wallets
   (k) International remittance
   (l) Other (describe)
```

**CLARIFY Set C — Customer Base**
```
Q5: What is the primary customer base?
   [Select all that apply]
   (a) Individual retail customers (domestic)
   (b) Small and medium businesses (domestic)
   (c) Large corporate / institutional
   (d) Money Service Businesses (MSBs)
   (e) Foreign financial institutions / correspondent accounts
   (f) Cannabis-related businesses (state-legal)
   (g) Politically Exposed Persons (significant percentage)
   (h) Non-profit organizations
   (i) Foreign nationals / non-resident customers
   (j) Cryptocurrency businesses / VASPs
```

**CLARIFY Set D — Current Program Status**
```
Q6: Is there an existing AML program?
   (a) Comprehensive written program exists; review requested
   (b) Basic written policy exists; gaps suspected
   (c) No formal written program (new program needed)
   (d) Program under regulatory action / consent order (specify)
```

```
Q7: When was the last independent AML audit conducted?
   (a) Within past 12 months
   (b) 12–24 months ago
   (c) More than 24 months ago / never
   (d) Unknown
```

---

**STEP 3: Regulatory Framework Determination**

Based on inputs, determine:

1. **Primary regulatory framework**: US BSA/FFIEC | EU AMLD6/AMLR | UK MLR 2017 | Multi-jurisdictional
2. **Applicable regulations by component**:
   - CDD: 31 C.F.R. § 1010.230 (US) | AMLR Art. X (EU) | MLR 2017 Part 3 (UK)
   - SAR: 31 C.F.R. § 1020.320 (banks) | POCA s. 330 (UK) | EU AMLD6 Art. XX
   - Training: FFIEC Manual | EU AMLD6 | UK MLR 2017 Reg. 24
3. **Primary supervisor**: OCC / FDIC / FRB / NCUA / FinCEN (US) | National competent authority / AMLA (EU) | FCA / HMRC (UK)
4. **Applicable sanctions programs**: OFAC (US) + EU + UN | OFSI (UK) + EU + UN | All
5. **PEP definition source**: US (no statutory definition — institution-defined) | EU AMLD6 Annex | UK MLR 2017 Schedule 2
6. **Special overlay programs**:
   - Investment Adviser: FinCEN 2028 proposed rule status [VERIFY current implementation date]
   - Cryptocurrency: FinCEN guidance on VASPs; state BitLicense where applicable
   - Cannabis: FinCEN 2014 guidance on marijuana-related businesses
   - Correspondent Banking: FFIEC Correspondent Banking guidance
   - Trade Finance: FATF Guidance on Trade-Based ML (2024 update [VERIFY])

Output: One-page regulatory framework summary with applicable rules, supervisors, and key deadlines.

---

**STEP 4: Pillar-by-Pillar Program Gap Assessment**

For each of the five pillars, assess against documented requirements:

**Pillar 1 Assessment — Internal Controls**
- [ ] Written AML policy: existence, board approval, last review date
- [ ] Procedures library: complete coverage of CIP, CDD, EDD, SAR, CTR, record retention
- [ ] Institutional risk assessment: existence, currency, methodology adequacy
- [ ] Technology: transaction monitoring system documented; sanctions screening documented
- [ ] Record retention: 5-year retention implemented and tested
- **Classification**: COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY

**Pillar 2 Assessment — Compliance Officer**
- [ ] BSA/AML Officer formally designated (documented in board resolution or policy)
- [ ] Qualifications adequate for institution's risk profile
- [ ] Reporting line: direct access to board/audit committee
- [ ] Independence: not subordinated to revenue functions
- [ ] Adequate staffing and budget resources
- **Classification**: COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY

**Pillar 3 Assessment — Training**
- [ ] Role-based curriculum exists for all required groups
- [ ] Training materials current (reflects recent regulatory changes)
- [ ] New hire training: policy and timing documented
- [ ] Annual refresher: documented and completed for all applicable personnel
- [ ] Training records: complete and retrievable
- [ ] Board training: documented
- **Classification**: COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY

**Pillar 4 Assessment — Independent Testing**
- [ ] Independent audit conducted within required timeframe
- [ ] Auditor independence confirmed
- [ ] Scope adequate: covers all FFIEC-required areas
- [ ] Transaction testing: included with adequate sample size
- [ ] Report issued to board/audit committee
- [ ] Prior findings tracking: management responses documented; remediation tracked
- **Classification**: COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY

**Pillar 5 Assessment — CDD**
- [ ] CIP procedures: complete; all required elements collected and verified
- [ ] Beneficial ownership: form and procedures for legal entities; 25% threshold; control prong
- [ ] Customer risk profiling: methodology documented; applied at onboarding
- [ ] Periodic review schedule: implemented; event-based triggers documented
- [ ] EDD: triggers identified; procedures for PEPs, high-risk customers documented
- [ ] Ongoing monitoring: transaction monitoring linked to customer risk profile
- **Classification**: COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY

---

**STEP 5: CDD / EDD Procedures Deep Dive**

Evaluate:
1. **CDD File Completeness** (sample review if files provided):
   - All four CDD elements documented
   - Beneficial ownership form collected for legal entities
   - Risk score assigned and documented
   - Source of funds / source of wealth documented for high-risk

2. **EDD Trigger Clarity**:
   - Written criteria for EDD trigger (PEP status, industry type, geographic risk, adverse media)
   - Process: who collects EDD, who approves, what documentation required

3. **PEP Identification Process**:
   - Database vendor(s) used
   - Screening frequency
   - EDD procedures for PEPs: SOW/SOF documentation requirement, senior management approval, monitoring frequency

4. **Periodic Review Process**:
   - Time-based review schedule by tier
   - Event-based trigger identification and escalation
   - Documentation of review decisions

5. **Customer Exit Process**:
   - When is a customer exited?
   - Who approves customer exit for AML reasons?
   - How is the exit documented?
   - Does exit trigger SAR consideration?

---

**STEP 6: Sanctions and PEP Screening Review**

Evaluate:
1. **Lists Coverage**: Are all applicable lists screened? (OFAC SDN, FSE, SSI, EU, UN, UK as applicable)
2. **50 Percent Rule**: Is the 50% rule implemented? Does screening tool support ownership chain analysis?
3. **Fuzzy Matching**: Is name variant matching configured? Are transliteration rules documented?
4. **Screening Frequency**: At onboarding + ongoing rescreening schedule documented?
5. **Hit Adjudication Process**: Documented decision workflow; audit trail for each determination
6. **True Match Process**: Escalation path; OFAC reporting and blocking obligations documented
7. **False Positive Rate**: Tracked? Are excessive false positives leading to analyst fatigue / inadequate review?
8. **OFAC License Program**: Process for requesting specific/general licenses documented?

---

**STEP 7: Transaction Monitoring Framework Review**

Evaluate:
1. **Rule Coverage**: Are all applicable typologies covered? (structuring, velocity, geographic concentration, round-dollar, pass-through, dormant account)
2. **Threshold Calibration**: Are thresholds documented? When were they last back-tested?
3. **Alert Management Process**: L1/L2 process documented; SLA standards set; adherence measured
4. **Alert Disposition Documentation**: Standard for closing alerts; documentation retained for 5 years
5. **SAR Referral Rate**: Is referral rate plausible given institution's risk profile?
6. **False Positive Rate**: Is false positive rate tracked? High rates may indicate threshold miscalibration
7. **Model Validation**: Has monitoring system been validated? Model risk governance in place?
8. **New Products / Channels**: When new products launched, were monitoring rules updated?
9. **Lookback Process**: Is there a lookback protocol for when new information surfaces about prior transactions?

---

**STEP 8: SAR / CTR Filing Procedures Review**

Evaluate:
1. **SAR Internal Workflow**: Referral → L1/L2 review → SAR determination → senior approval → filing; each step documented
2. **Filing Timeliness**: SAR within 30 days; CTR within 15 days; metrics tracked and reported
3. **SAR Narrative Quality**: 5 Ws standard applied? Quality review by senior Compliance?
4. **Continuing SAR Process**: 90-day / 120-day continuing SAR workflow documented?
5. **No-File Documentation**: Standard for documenting non-suspicious determinations?
6. **CTR Aggregation**: Procedures for intra-day aggregation across tellers/branches?
7. **CTR Exemption File**: Exempt persons file maintained and current?
8. **Tipping-Off Controls**: Staff aware of tipping-off prohibition? Procedures for customer inquiries documented?
9. **SAR Confidentiality**: Access controls for SAR records; legal hold procedures?

---

**STEP 9: Training Program Review**

Evaluate:
1. **Curriculum Completeness**: All five role tiers covered?
2. **Content Currency**: Last update date; does content reflect recent regulatory changes and typologies?
3. **New Hire Process**: Policy exists; timing requirement defined and met?
4. **Annual Training Completion Rate**: % of applicable personnel completing training; exceptions tracked?
5. **Board Training**: Documented?
6. **BSA Officer Advanced Training**: External training and certifications documented?
7. **Training Records**: Complete; retrievable; cover 5-year period?
8. **Testing / Assessment**: Knowledge checks included? Remediation for failures documented?

---

**STEP 10: Independent Audit / Testing Review**

Evaluate:
1. **Audit Frequency**: Within 12–18 months?
2. **Independence**: Auditor independence documented; no conflicts with BSA function?
3. **Scope Adequacy**: All FFIEC-required areas covered?
4. **Transaction Testing**: Included? Sample size documented and appropriate?
5. **Report Quality**: Findings clearly described; risk-rated; root cause analyzed?
6. **Management Response**: Documented for each finding; responsible owner; target date?
7. **Remediation Tracking**: Prior findings tracked to closure; follow-up testing done?
8. **Board Reporting**: Audit report provided to board/audit committee?
9. **Work Papers**: Sufficient for examiner reliance?

---

**STEP 11: Findings Classification**

For each finding across all pillars:

**COMPLIANT**: Element meets regulatory requirements; evidence supports conclusion; no gaps identified.

**PARTIAL**: Element exists but has identifiable gaps; partial compliance; remediation required to achieve full compliance.

**NON-COMPLIANT**: Required element is absent, inadequate, or materially fails to meet regulatory requirements; significant remediation required.

**CRITICAL DEFICIENCY**: Failure constitutes immediate regulatory risk; likely examination finding; possible enforcement exposure; immediate escalation and remediation required.

**Prioritization**:
- **Immediate** (Critical Deficiency or Non-Compliant in core pillars): Address within 30 days; senior management and board notification required
- **Near-Term** (Non-Compliant in procedural or supporting areas): Address within 60–90 days
- **Background / Enhancement** (Partial; operational improvement): Address within 6–12 months as resources permit

---

**STEP 12: Output — Compliance Gap Report and Remediation Roadmap**

Produce the structured output template (see Part 13 below).

---

## PART 12: QUALITY FRAMEWORKS

### 12.1 Severity Classification System

**COMPLIANT**
- Definition: Element or practice fully meets applicable regulatory requirements. Controls are documented, implemented, and operating effectively. No gaps identified.
- Evidence Standard: Policy/procedure exists + implementation evidence + testing confirmation (where applicable)
- Report Notation: [COMPLIANT — evidence: ...]

**PARTIAL**
- Definition: Element exists in some form but has identifiable material gaps. Risk is present but mitigated. Remediation required to achieve regulatory compliance.
- Evidence Standard: Existence documented but gap in implementation, scope, currency, or documentation
- Report Notation: [PARTIAL — gap: ... | risk: ... | remediation: ...]

**NON-COMPLIANT**
- Definition: Required element is absent or materially fails to meet regulatory requirements. Significant remediation required. Regulatory examination finding probable.
- Evidence Standard: Absence of required element; or element exists but is inadequate per regulatory standard
- Report Notation: [NON-COMPLIANT — requirement: ... | gap: ... | regulatory citation: ... | remediation: ...]

**CRITICAL DEFICIENCY**
- Definition: Failure that creates immediate regulatory or legal risk. Examples: active OFAC true match not blocked; SAR filing deadlines systematically missed; no AML program in place; transaction monitoring non-functional for material transaction volume.
- Evidence Standard: Documented failure + immediate regulatory citation + potential enforcement exposure
- Report Notation: [CRITICAL DEFICIENCY — immediate action required | regulatory risk: ... | escalation: board notification | remediation deadline: 30 days]

### 12.2 Confidence Scoring for Regulatory Risk Determinations

Each finding is scored:

**Confidence Level A — High Confidence** (>85% confidence in determination)
- Explicit regulatory text clearly applies
- Industry standard practice unambiguous
- Examiner guidance (FFIEC Manual, FinCEN FAQ) directly addresses scenario
- Cite: [CITE: 31 C.F.R. § 1010.230(a); FFIEC Manual pp. X; FinCEN FAQ No. X]

**Confidence Level B — Medium Confidence** (65–85% confidence)
- Regulatory text applies but interpretation is not completely settled
- Agency guidance exists but is non-binding or dated
- Cite: [CITE: [VERIFY] — based on FFIEC Manual guidance as of [date]; note: verify against current agency guidance]

**Confidence Level C — Lower Confidence** (<65% confidence)
- Emerging regulatory area; guidance pending
- Institution-specific facts would significantly affect analysis
- Competing regulatory positions or recent developments not fully settled
- Cite: [CITE: [VERIFY CAREFULLY] — area of regulatory uncertainty; consult qualified AML counsel]

### 12.3 Citation Quality Gates

All regulatory citations in skill output must:
1. Include the specific provision: statute (31 U.S.C. § ...), regulation (31 C.F.R. § ...), examination manual chapter, FinCEN guidance number
2. Include [VERIFY] if not confirmed against authoritative source during session
3. Include date of guidance if citing non-statutory guidance (FinCEN guidance, FFIEC Manual updates frequently)
4. Not cite enforcement actions as binding precedent (they are persuasive only)
5. Distinguish between mandatory requirements and best practices

**Citation Anti-Pattern**: "Regulators require X" without citing the specific regulatory source → insufficient; must include specific citation.

**Self-Interrogation Protocol** (adapted from legalcode-contract-review):
Before finalizing each finding, ask:
1. "Have I cited the specific regulatory provision, not just described it?"
2. "Is this a mandatory requirement or a best practice? Have I distinguished clearly?"
3. "Is my severity classification (COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY) supported by the specific facts provided?"
4. "Have I considered alternative explanations for apparent gaps before classifying as non-compliant?"
5. "Is there a [VERIFY] flag needed — am I citing from training knowledge, not a confirmed source?"
6. "Have I recommended specific, actionable remediation steps, not just flagging the problem?"
7. "Have I considered the institution's size and risk profile in my determination? (Small community bank vs. large global bank have different program sophistication expectations.)"

---

## PART 13: AML/KYC ANTI-PATTERNS CATALOGUE

The following 20 anti-patterns represent the most common and significant AML/KYC program failures. The skill should warn against each of these explicitly.

### AP-01: Static Risk Assessment
**Description**: The institutional risk assessment is completed once (often at program inception or during an examination) and not updated as the institution's business, customer base, products, or geographic footprint changes.
**Regulatory Impact**: CRITICAL — risk assessment is the foundation of the entire risk-based approach; stale assessment means monitoring is calibrated to a business model that no longer exists.
**Real-World Example**: TD Bank's monitoring system calibrated for 2014 transaction volumes despite growing to $18.3 trillion in transactions by 2022 — 92% unmonitored.
**Remediation Pattern**: Risk assessment reviewed annually (minimum) and updated whenever material business changes occur; board-approved; BSA Officer certifies currency.

### AP-02: Monitoring System Designed to Suppress Alerts
**Description**: Transaction monitoring thresholds set at levels known to generate few or no alerts; rules configured to exclude categories of transactions for operational convenience; parameters never back-tested; alert suppression to reduce workload.
**Regulatory Impact**: CRITICAL DEFICIENCY — systemic monitoring failure; OCC identified this pattern as treating monitoring as a "box-checking exercise."
**Real-World Example**: OCC Cease-and-Desist against Bank of America — monitoring controls that appeared designed to minimize operational burden.
**Remediation Pattern**: Documented justification for each threshold; annual back-testing; independent validation; prohibit suppression without documented senior approval and board notification.

### AP-03: Incomplete Beneficial Ownership Collection
**Description**: CDD beneficial ownership form not collected for legal entity customers; not updated when entity structure changes; 25% threshold applied inconsistently; control prong not collected.
**Regulatory Impact**: NON-COMPLIANT — direct violation of 31 C.F.R. § 1010.230.
**Remediation Pattern**: Systematic file review; procedure requiring BO form before account opening; exception report tracking; periodic verification.

### AP-04: PEP Screening Limited to One Database
**Description**: Relying on a single commercial PEP database without supplemental research; not screening for domestic PEPs (historically EU institutions' blind spot); not screening family members and close associates.
**Regulatory Impact**: PARTIAL to NON-COMPLIANT — single database has known gaps; domestic PEPs now required under AMLD6.
**Remediation Pattern**: Use two or more commercial databases for high-risk jurisdictions; supplement with open-source research for senior PEPs; apply to domestic PEPs.

### AP-05: SAR Narrative Quality Deficiency
**Description**: SAR narratives describe transactions in generic terms ("unusual activity," "transactions below reporting threshold") without explaining WHY the activity is suspicious, WHAT theory of money laundering applies, or HOW the activity connects to known typologies.
**Regulatory Impact**: NON-COMPLIANT — poor narrative quality reduces law enforcement utility; can result in examiner criticism; FinCEN guidance emphasizes 5 Ws.
**Remediation Pattern**: 5 Ws checklist applied before SAR submission; senior Compliance quality review; training on narrative writing; sample good/bad narratives in training materials.

### AP-06: Training Not Tailored to Institution-Specific Risks
**Description**: Using off-the-shelf generic BSA training without customizing for the institution's specific customer types, products, typologies, and geographic risks; same training for tellers as for relationship managers; no training on specific red flags for institution's customer base.
**Regulatory Impact**: NON-COMPLIANT — FFIEC requires training tailored to individual responsibilities; 2024 enforcement actions specifically cited failure to tailor training.
**Remediation Pattern**: Role-based curricula; institution-specific scenarios and typologies; update materials when new products launched or new typologies identified.

### AP-07: No-File Decision Not Documented
**Description**: Closing transaction monitoring alerts or SAR investigations without documenting the rationale for the non-suspicious determination; treating "no-file" as the default with no documentation requirement.
**Regulatory Impact**: NON-COMPLIANT — FinCEN and FFIEC require documentation of no-file decisions with supporting rationale; inability to demonstrate decision-making process is a significant examination finding.
**Remediation Pattern**: Standard no-file documentation template requiring: specific facts considered, why activity is not suspicious, customer information reviewed, analyst and supervisor sign-off; retain 5 years.

### AP-08: BSA Officer Without Independence or Authority
**Description**: BSA/AML Officer dual-hatted with revenue-generating function (head of lending, COO); subordinated to business line head; insufficient authority to refuse or exit high-risk customers; no direct board reporting channel.
**Regulatory Impact**: CRITICAL DEFICIENCY — compromises independence of the compliance function; examiner concern that compliance is subordinated to revenue interests.
**Remediation Pattern**: BSA Officer reports to board/audit committee (or in small institutions, to CEO directly with documented board access); written authority to decline onboarding; budget and staffing control.

### AP-09: Independent Audit Lacking Actual Transaction Testing
**Description**: Audit reviews policies and procedures but does not test actual customer files, monitoring alerts, or SAR/CTR records; sample sizes too small; audit findings limited to "policies appear adequate" without operational verification.
**Regulatory Impact**: NON-COMPLIANT — FFIEC requires thorough transaction testing; regulator cannot rely on policy-only audit.
**Remediation Pattern**: Written audit methodology specifying minimum sample sizes by area; risk-based sampling protocol; documented results of each sample test; auditor representations on testing scope.

### AP-10: Sanctions Screening Not Covering All Applicable Lists
**Description**: OFAC SDN screened but FSE, SSI, EU, UN, or UK lists not screened; new sanctions programs (e.g., Russia sectoral sanctions, Nicaragua, DPRK) not added to screening system; 50% rule not implemented.
**Regulatory Impact**: CRITICAL DEFICIENCY for certain programs — potential OFAC violation; strict liability under OFAC regulations.
**Remediation Pattern**: Complete list inventory mapped against all applicable programs; quarterly review to add new programs; 50% rule ownership tracing capability confirmed; documented list coverage.

### AP-11: Periodic Review Schedule Not Enforced
**Description**: Customer risk ratings assigned at onboarding but never updated; high-risk customers not reviewed annually; adverse media or sanctions hits not triggering event-based reviews; review "backlog" accumulates without correction.
**Regulatory Impact**: NON-COMPLIANT — CDD Rule requires periodic review; failure to update information means customer profiles reflect stale information that cannot support accurate monitoring.
**Remediation Pattern**: Automated review reminder system; BSA Officer report on review completion rates; escalation process for overdue reviews; board metrics including review backlog.

### AP-12: Fintech/BaaS Sponsor Bank AML Delegation Without Oversight
**Description**: Sponsor banks contract fintech/BaaS partners to perform customer-facing AML functions (CDD, screening) without adequate contractual requirements, training oversight, or ongoing testing; fintech program not tested as part of sponsor bank audit.
**Regulatory Impact**: CRITICAL DEFICIENCY for sponsor banks — sponsor bank is legally responsible for BSA/AML compliance of the relationship; 2024 FDIC enforcement actions focused specifically on this gap.
**Remediation Pattern**: Written program requirements for fintech partners; contractual audit rights; annual testing of fintech partner AML program; integration into sponsor bank's independent testing.

### AP-13: Structuring Not Monitored for Known Customers
**Description**: Structuring detection rules not applied to business accounts; monitoring rules exclude known high-volume customers from structuring detection on the basis that they are "known" customers; failure to monitor structuring by employees or insiders.
**Regulatory Impact**: CRITICAL DEFICIENCY — structuring is a federal crime (31 U.S.C. § 5324) regardless of the legitimacy of the underlying funds; institution must monitor and report regardless of customer relationship.
**Remediation Pattern**: Structuring rules applied universally; exceptions require documented senior approval and regulatory review; insider monitoring program applied to all personnel with cash handling access.

### AP-14: Cannabis/High-Risk Industry CDD Without Enhanced Procedures
**Description**: Institution accepts cannabis-related business (CRB) deposits or accounts without implementing FinCEN 2014 guidance-compliant enhanced procedures; no verification of state license status; no ongoing monitoring for license compliance; standard CDD applied to CRBs as if low-risk.
**Regulatory Impact**: NON-COMPLIANT — FinCEN 2014 guidance (FIN-2014-G001) requires specific enhanced procedures for CRBs including license verification, monitoring for state law compliance, and specific SAR filing requirements (Marijuana Limited / Priority / Termination SAR types).
**Remediation Pattern**: Dedicated CRB CDD procedure; state license verification at onboarding and annually; monitoring for changes in state law; specific SAR filing protocol; senior management approval for CRB relationships.

### AP-15: AML Program Not Updated for New Products or Services
**Description**: Institution launches new products (cryptocurrency exchange, peer-to-peer payments, BNPL) without conducting AML risk assessment for the new product; transaction monitoring rules not updated; CDD procedures not amended; training not updated.
**Regulatory Impact**: NON-COMPLIANT — new product risk assessment is expected by FFIEC; monitoring gaps created by uncovered transaction types.
**Remediation Pattern**: BSA/AML compliance sign-off required in new product approval process; pre-launch risk assessment; monitoring rules designed before launch; training updated within 60 days of launch.

### AP-16: Correspondent Account Due Diligence Not Conducted
**Description**: Foreign correspondent bank accounts opened without completing correspondent account due diligence (CADD) as required by 31 C.F.R. § 1010.610; no enhanced due diligence for correspondent accounts in high-risk jurisdictions; payable-through account risk not identified.
**Regulatory Impact**: CRITICAL DEFICIENCY — correspondent banking is highest-risk category; specific regulatory requirements exist under 31 C.F.R. § 1010.610; FATF Recommendation 13.
**Remediation Pattern**: Dedicated CADD procedures; due diligence questionnaire; annual refresh for high-risk correspondents; nested correspondent account detection.

### AP-17: SAR Filing Deadline Missed Without Detection
**Description**: No tracking system for SAR filing deadlines; 30-day deadline exceeded without detection; no metrics on SAR timeliness reported to management or board; discovery only when examiner reviews SAR log.
**Regulatory Impact**: CRITICAL DEFICIENCY — late SAR filing is a direct regulatory violation; 2024 Bank of America cease-and-desist cited "failure to timely file suspicious activity reports."
**Remediation Pattern**: SAR deadline tracking system with automated alerts before deadline; weekly BSA Officer review of open investigations; board-reported metric: SAR filing timeliness rate; target: 100% within deadline.

### AP-18: Low SAR Quality Due to Copy-Paste or Template Overuse
**Description**: SAR narratives generated by copying transaction data from the monitoring system without analysis; generic descriptions repeated across many SARs; typology identification ("possible structuring") without supporting analysis; copy-paste of prior SAR narrative for continuing SARs.
**Regulatory Impact**: NON-COMPLIANT — defeats the law enforcement utility of SARs; FinCEN guidance emphasizes SAR quality; examiners review SAR narrative quality as indicator of program effectiveness.
**Remediation Pattern**: Narrative writing standard with checklist; peer review or supervisor review before filing; periodic quality review by BSA Officer; training component on high-quality narrative writing with examples.

### AP-19: EDD Approval Not Documented or Obtained from Wrong Level
**Description**: High-risk customer relationships established without required senior management approval; approval obtained from BSA analyst (not senior management); approval email not retained in customer file; approval process not defined in procedures.
**Regulatory Impact**: NON-COMPLIANT — CDD Rule and internal policy require senior management approval for high-risk relationships; inability to demonstrate approval process is examination finding.
**Remediation Pattern**: Define "senior management" in procedure (minimum level: BSA Officer or SVP); approval must be in writing; retained in customer file; audited as part of EDD file review.

### AP-20: Training Records Not Maintained or Incomplete
**Description**: Training completion records not retained beyond 1–2 years; records not linked to specific course version; no record of board training; inability to confirm specific employee completed specific training at specific date; records stored in non-retrievable format.
**Regulatory Impact**: NON-COMPLIANT — FFIEC expects training records available for examination; inability to produce records results in presumption of non-compliance.
**Remediation Pattern**: LMS (Learning Management System) or equivalent records; minimum 5-year retention; linked to employee record; annual audit of training completion rates; report to board.

---

## PART 14: OUTPUT TEMPLATE — AML/KYC COMPLIANCE PROGRAM ASSESSMENT REPORT

```
═══════════════════════════════════════════════════════════════════════════
AML/KYC COMPLIANCE PROGRAM ASSESSMENT REPORT
Generated by legalcode-aml-kyc-compliance
═══════════════════════════════════════════════════════════════════════════

CONFIDENTIAL — PREPARED AT THE DIRECTION OF LEGAL COUNSEL
[ATTORNEY-CLIENT PRIVILEGE AND WORK PRODUCT MAY APPLY — SEE NOTES BELOW]

DISCLAIMER: This report is AI-assisted and does not constitute legal advice
or a legal opinion. It does not create an attorney-client relationship. All
findings, regulatory citations, and recommendations should be reviewed by
qualified AML counsel and compliance professionals before use. Regulatory
requirements change frequently; verify all citations against current
authoritative sources. Statutory and regulatory citations from AI training
knowledge carry hallucination risk; each citation marked [VERIFY] must be
confirmed before reliance.

═══════════════════════════════════════════════════════════════════════════
SECTION 1: EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════════════════

ENTITY: [Entity name / description]
ASSESSMENT DATE: [Date]
REGULATORY FRAMEWORK: [US / EU / UK / Multi-jurisdictional]
ENTITY TYPE: [Bank / Credit Union / MSB / Broker-Dealer / Other]
ASSESSMENT MODE: [Full Assessment / Build Mode / Deep-Dive — specify component]

OVERALL PROGRAM STATUS:
  [ ] SUBSTANTIALLY COMPLIANT — Minor gaps; no immediate regulatory risk
  [ ] PARTIALLY COMPLIANT — Material gaps requiring remediation; moderate
      regulatory risk
  [ ] NON-COMPLIANT — Significant gaps; high regulatory risk; examination
      findings probable
  [ ] CRITICAL PROGRAM FAILURE — Immediate regulatory and legal risk;
      board notification required

FIVE-PILLAR SUMMARY TABLE:

  Pillar                          | Status               | Priority
  --------------------------------|----------------------|------------------
  1. Internal Controls            | [status]             | [priority]
  2. Compliance Officer           | [status]             | [priority]
  3. Training Program             | [status]             | [priority]
  4. Independent Testing          | [status]             | [priority]
  5. Customer Due Diligence       | [status]             | [priority]

FINDINGS COUNT:
  Critical Deficiencies:   [N] — Immediate action required
  Non-Compliant:           [N] — Address within 60–90 days
  Partial:                 [N] — Address within 6–12 months
  Compliant:               [N] — No action required
  Total Findings:          [N]

TOP 3 IMMEDIATE PRIORITIES:
1. [Finding title] — [One-line description] — [Remediation deadline]
2. [Finding title] — [One-line description] — [Remediation deadline]
3. [Finding title] — [One-line description] — [Remediation deadline]

═══════════════════════════════════════════════════════════════════════════
SECTION 2: REGULATORY FRAMEWORK APPLICABLE
═══════════════════════════════════════════════════════════════════════════

PRIMARY JURISDICTION: [US / EU / UK / Multi-jurisdictional]

APPLICABLE REGULATIONS:

  US Framework (if applicable):
  - Bank Secrecy Act, 31 U.S.C. §§ 5311–5336
  - 31 C.F.R. § 1020.210 — BSA/AML Program Requirements (banks)
  - 31 C.F.R. § 1020.220 — Customer Identification Program
  - 31 C.F.R. § 1010.230 — CDD / Beneficial Ownership Rule
  - 31 C.F.R. § 1020.320 — SAR Filing (banks)
  - 31 C.F.R. § 1010.311 — CTR Filing
  - [Add entity-specific regulations]
  - FFIEC BSA/AML Examination Manual [VERIFY current version date]

  EU Framework (if applicable):
  - AMLD6 (Directive 2024/1624/EU) — transposition by July 10, 2027
  - AMLR (Regulation 2024/1624/EU) — directly applicable
  - EBA Guidelines on Risk Factors [VERIFY current version]
  - AMLA supervision framework (operational July 1, 2025)

  UK Framework (if applicable):
  - MLR 2017, as amended
  - POCA 2002
  - FCA Financial Crime Guide [VERIFY current version]
  - JMLSG Guidance [VERIFY current edition]

SUPERVISORY AUTHORITY: [Specify]

SPECIAL OVERLAYS:
  [List any product/customer-specific overlays: FinCEN cannabis guidance,
   VASP/crypto requirements, correspondent banking, trade finance, etc.]

═══════════════════════════════════════════════════════════════════════════
SECTION 3: PILLAR-BY-PILLAR FINDINGS
═══════════════════════════════════════════════════════════════════════════

══════════════════════════════════
PILLAR 1: INTERNAL CONTROLS
Overall Status: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
══════════════════════════════════

1.1 WRITTEN AML POLICY
  Status: [status]
  Finding: [Description of gap or confirmation of compliance]
  Regulatory Basis: [Citation]
  Confidence: [A/B/C]
  Remediation: [Specific action required]
  Priority: [Immediate / Near-Term / Background]

1.2 PROCEDURES LIBRARY
  Status: [status]
  Finding: [...]
  [...]

1.3 INSTITUTIONAL RISK ASSESSMENT
  Status: [status]
  Finding: [...]
  [...]

1.4 TECHNOLOGY CONTROLS
  Status: [status]
  Finding: [...]
  [...]

1.5 RECORDKEEPING
  Status: [status]
  Finding: [...]
  [...]

══════════════════════════════════
PILLAR 2: BSA/AML COMPLIANCE OFFICER
Overall Status: [...]
══════════════════════════════════

2.1 OFFICER DESIGNATION AND DOCUMENTATION
  [As above format]

2.2 QUALIFICATIONS AND COMPETENCE
  [...]

2.3 INDEPENDENCE AND REPORTING LINE
  [...]

2.4 RESOURCES AND AUTHORITY
  [...]

══════════════════════════════════
PILLAR 3: TRAINING PROGRAM
Overall Status: [...]
══════════════════════════════════

3.1 CURRICULUM COMPLETENESS AND ROLE-BASED TAILORING
  [...]

3.2 TRAINING CONTENT CURRENCY
  [...]

3.3 NEW HIRE TRAINING PROCESS
  [...]

3.4 ANNUAL TRAINING COMPLETION
  [...]

3.5 TRAINING RECORDS
  [...]

3.6 BOARD TRAINING
  [...]

══════════════════════════════════
PILLAR 4: INDEPENDENT TESTING
Overall Status: [...]
══════════════════════════════════

4.1 AUDIT FREQUENCY AND TIMING
  [...]

4.2 AUDITOR INDEPENDENCE
  [...]

4.3 AUDIT SCOPE ADEQUACY
  [...]

4.4 TRANSACTION TESTING
  [...]

4.5 FINDINGS AND MANAGEMENT RESPONSES
  [...]

4.6 PRIOR FINDINGS REMEDIATION
  [...]

══════════════════════════════════
PILLAR 5: CUSTOMER DUE DILIGENCE
Overall Status: [...]
══════════════════════════════════

5.1 CUSTOMER IDENTIFICATION PROGRAM (CIP)
  [...]

5.2 BENEFICIAL OWNERSHIP PROCEDURES
  [...]

5.3 CUSTOMER RISK PROFILING
  [...]

5.4 ENHANCED DUE DILIGENCE — PEPs
  [...]

5.5 ENHANCED DUE DILIGENCE — HIGH-RISK CUSTOMERS
  [...]

5.6 PERIODIC REVIEW PROCESS
  [...]

5.7 ONGOING MONITORING LINKAGE
  [...]

═══════════════════════════════════════════════════════════════════════════
SECTION 4: SANCTIONS AND PEP SCREENING FINDINGS
═══════════════════════════════════════════════════════════════════════════

6.1 LIST COVERAGE
  Lists Required: [List based on jurisdiction]
  Lists Currently Screened: [Based on information provided]
  Gap: [Any lists not screened]
  Status: [status]

6.2 OFAC 50 PERCENT RULE IMPLEMENTATION
  Status: [status]
  Finding: [...]

6.3 FUZZY MATCHING CONFIGURATION
  Status: [status]
  Finding: [...]

6.4 ONGOING RESCREENING FREQUENCY
  Status: [status]
  Finding: [...]

6.5 HIT ADJUDICATION PROCESS
  Status: [status]
  Finding: [...]

6.6 FALSE POSITIVE RATE
  [Metric if provided; assessment of adequacy]

═══════════════════════════════════════════════════════════════════════════
SECTION 5: TRANSACTION MONITORING FINDINGS
═══════════════════════════════════════════════════════════════════════════

7.1 MONITORING RULE COVERAGE
  Coverage by typology:
  [ ] Structuring / near-threshold cash activity
  [ ] High-volume wire transfer activity
  [ ] Geographic concentration (high-risk jurisdictions)
  [ ] Round-dollar transaction detection
  [ ] Pass-through / rapid fund movement
  [ ] Dormant account reactivation
  [ ] Business account activity mismatch
  [ ] [Institution-specific rules]
  Gaps identified: [...]

7.2 THRESHOLD CALIBRATION AND BACK-TESTING
  Status: [status]
  Finding: [...]

7.3 L1/L2 INVESTIGATION PROCESS
  Status: [status]
  Finding: [...]

7.4 ALERT DISPOSITION DOCUMENTATION
  Status: [status]
  Finding: [...]

7.5 MODEL VALIDATION
  Status: [status]
  Finding: [...]

7.6 ALERT METRICS
  Alert Volume (if provided): [...]
  False Positive Rate (if provided): [...]
  SAR Referral Rate (if provided): [...]
  Assessment: [...]

═══════════════════════════════════════════════════════════════════════════
SECTION 6: SAR AND CTR FILING FINDINGS
═══════════════════════════════════════════════════════════════════════════

8.1 SAR INTERNAL WORKFLOW
  Status: [status]
  Finding: [...]

8.2 SAR FILING TIMELINESS
  Metric (if available): [X% filed within 30 days]
  Status: [status]
  Finding: [...]

8.3 SAR NARRATIVE QUALITY
  Quality Assessment: [Based on sample review or description]
  Status: [status]
  Common Deficiencies Found: [...]

8.4 CONTINUING SAR PROCESS
  Status: [status]
  Finding: [...]

8.5 CTR TIMELINESS AND ACCURACY
  Status: [status]
  Finding: [...]

8.6 CTR AGGREGATION PROCEDURES
  Status: [status]
  Finding: [...]

8.7 TIPPING-OFF CONTROLS
  Status: [status]
  Finding: [...]

═══════════════════════════════════════════════════════════════════════════
SECTION 7: ANTI-PATTERNS IDENTIFIED
═══════════════════════════════════════════════════════════════════════════

The following AML/KYC anti-patterns have been identified in this program
assessment:

[For each identified anti-pattern:]

AP-XX: [Anti-Pattern Name]
  Identified: YES / NO
  Evidence: [Specific evidence from information provided]
  Risk Level: [Critical / High / Medium / Low]
  Remediation: [Specific steps]

═══════════════════════════════════════════════════════════════════════════
SECTION 8: REMEDIATION ROADMAP
═══════════════════════════════════════════════════════════════════════════

PHASE 1: IMMEDIATE (0–30 DAYS)
  Priority: Address Critical Deficiencies and immediate regulatory risk

  Item 1.1: [Finding reference — short title]
    Owner: [Role title, not individual name]
    Deadline: [Date]
    Action Required: [Specific steps]
    Success Criterion: [How completion is verified]
    Regulatory Basis: [Citation]

  [Additional items]

PHASE 2: NEAR-TERM (30–90 DAYS)
  Priority: Address Non-Compliant findings; prevent examination findings

  Item 2.1: [...]
  [...]

PHASE 3: BACKGROUND ENHANCEMENT (90 DAYS – 12 MONTHS)
  Priority: Address Partial findings; enhance program maturity

  Item 3.1: [...]
  [...]

REMEDIATION TRACKING TABLE:

  Finding | Pillar | Status | Owner | Deadline | Completion Date | Verified
  --------|--------|--------|-------|----------|-----------------|----------
  [...]   | [...]  | [...]  | [...] | [...]    | [...]           | [...]

═══════════════════════════════════════════════════════════════════════════
SECTION 9: EXAMINATION PREPARATION NOTES
═══════════════════════════════════════════════════════════════════════════

DOCUMENT PREPARATION CHECKLIST:

Documents to Prepare Before Examination:
[ ] Current institutional risk assessment (board-approved)
[ ] Current AML policy and procedures
[ ] AML/BSA organizational chart
[ ] BSA Officer resume and training records
[ ] Independent audit reports (current + prior 3 years)
[ ] Audit management responses and remediation tracking log
[ ] Training materials and completion records (5 years)
[ ] CDD file samples (prepare rapid retrieval for examiner selection)
[ ] SAR filing log (do NOT provide SAR contents without legal counsel review)
[ ] CTR filing records and exemption file
[ ] Transaction monitoring system documentation
[ ] Sanctions screening program documentation
[ ] Model validation reports
[ ] Board minutes approving AML policy
[ ] New product risk assessments
[ ] [Entity-specific items]

EXAM HOT TOPICS TO PREPARE FOR:
[ ] Cryptocurrency / VASP customer CDD and monitoring
[ ] Trade-based money laundering detection
[ ] Beneficial ownership implementation (CDD Rule + CTA coordination)
[ ] AI/ML monitoring model validation and explainability
[ ] BaaS/Fintech partner oversight (if applicable)
[ ] Cannabis banking (if applicable)
[ ] Correspondent banking due diligence (if applicable)

═══════════════════════════════════════════════════════════════════════════
SECTION 10: REGULATORY CITATIONS AND VERIFICATION NOTES
═══════════════════════════════════════════════════════════════════════════

The following regulatory citations appear in this report. Citations marked
[VERIFY] are drawn from AI training knowledge and must be confirmed against
current authoritative sources before reliance in compliance decisions or
regulatory submissions.

Key Citations:
- 31 U.S.C. §§ 5311–5336 — Bank Secrecy Act [VERIFY current version]
- 31 C.F.R. § 1010.230 — CDD/Beneficial Ownership Rule [VERIFY]
- 31 C.F.R. § 1020.220 — Customer Identification Program [VERIFY]
- 31 C.F.R. § 1020.320 — SAR Filing (banks) [VERIFY]
- 31 C.F.R. § 1010.311 — CTR Filing [VERIFY]
- FFIEC BSA/AML Examination Manual [VERIFY current version — updated periodically]
- FinCEN CDD Final Rule FAQ [VERIFY current FAQ version]
- AMLD6 (Directive 2024/1624/EU) [VERIFY transposition status in relevant Member State]
- MLR 2017 [VERIFY current amendment version]

For current authoritative sources, consult:
- FinCEN: https://www.fincen.gov/
- FFIEC BSA/AML Manual: https://bsaaml.ffiec.gov/
- OFAC: https://ofac.treasury.gov/
- OCC BSA/AML resources: https://www.occ.treas.gov/topics/supervision-and-examination/bsa/
- EBA AML/CFT: https://www.eba.europa.eu/
- FCA Financial Crime: https://www.fca.org.uk/firms/financial-crime

═══════════════════════════════════════════════════════════════════════════
IMPORTANT NOTES ON PRIVILEGE AND CONFIDENTIALITY
═══════════════════════════════════════════════════════════════════════════

If this assessment was conducted at the direction of legal counsel in
connection with providing legal advice, it may be protected by attorney-
client privilege and/or work product doctrine. Consult with legal counsel
before:
- Disclosing this report to regulators (even in response to an examination
  request) — assert privilege and consult counsel
- Sharing this report with third parties outside the institution
- Referencing this report in regulatory submissions or board materials
  without stripping sensitive privileged analysis

SAR CONFIDENTIALITY REMINDER: Any SAR filed by the institution, or any
information that could reveal whether a SAR has been filed, is confidential
under 31 U.S.C. § 5318(g)(2). Do not disclose SAR contents or SAR filing
status to any person, including in examination responses, without advice
of counsel.

═══════════════════════════════════════════════════════════════════════════
END OF REPORT
Generated by legalcode-aml-kyc-compliance
AI-assisted analysis | Requires human professional review before use
═══════════════════════════════════════════════════════════════════════════
```

---

## PART 15: KEY SOURCE REFERENCES

### US Primary Sources
- FinCEN: https://www.fincen.gov/
- FFIEC BSA/AML Examination Manual: https://bsaaml.ffiec.gov/
- OFAC: https://ofac.treasury.gov/
- 31 C.F.R. § 1010.230 (CDD Final Rule): https://www.federalregister.gov/documents/2016/05/11/2016-10567/customer-due-diligence-requirements-for-financial-institutions
- FinCEN CDD Rule resources: https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule
- FinCEN Proposed Rule (July 2024): https://www.fincen.gov/system/files/shared/Program-NPRM-FactSheet-508.pdf
- OCC BSA/AML: https://www.occ.treas.gov/topics/supervision-and-examination/bsa/

### EU Primary Sources
- EBA AML/CFT: https://www.eba.europa.eu/
- AMLA: https://www.amla.europa.eu/ [VERIFY — new authority]
- EUR-Lex (AMLD6, AMLR): https://eur-lex.europa.eu/

### UK Primary Sources
- FCA Financial Crime Guide: https://www.fca.org.uk/firms/financial-crime
- JMLSG Guidance: https://www.jmlsg.org.uk/
- HMRC AML supervision: https://www.gov.uk/guidance/money-laundering-regulations-registration

### Research Sources Used (Web Searches Conducted 2026-03-02)
- Five Pillars: https://www.abrigo.com/blog/blog-the-5-pillars-of-bsa-why-they-are-important-for-your-aml-program/
- Five Pillars detail: https://www.capitalcomplianceexperts.com/compliance-news/the-five-5-pillars-of-bsa-aml-ofac-compliance/
- FinCEN Proposed Rule (2024): https://www.cov.com/en/news-and-insights/insights/2024/07/fincen-issues-proposed-rule-requiring-financial-institutions-to-maintain-effective-risk-based-aml-programs-six-things-to-know
- CDD Rule: https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule
- CDD Rule BO update (2024): https://eclerx.com/insights/a-new-era-for-cdd-fincen-eases-beneficial-ownership-requirements/
- OFAC 50% Rule: https://complyadvantage.com/insights/ofac-50-rule/
- OFAC FAQs: https://ofac.treasury.gov/faqs
- PEP EDD guidance: https://www.thirdfort.com/insights/peps-law-updates-january-2024/
- SAR requirements: https://www.fincen.gov/suspicious-activity-reports-sars
- Transaction monitoring: https://www.sanctions.io/blog/anti-money-laundering-aml-transaction-monitoring-rules-and-best-practices
- Independent testing: https://bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/03_ep
- Training: https://bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/05
- 2024 enforcement actions (K&L Gates): https://www.klgates.com/Lessons-From-2024-Bank-Secrecy-Act-Anti-Money-Laundering-Enforcement-Actions-2-12-2025
- 2024 enforcement (Gibson Dunn): https://www.gibsondunn.com/top-year-end-developments-in-anti-money-laundering-in-2024/
- TD Bank penalty: https://bankingjournal.aba.com/2024/11/td-bank-agrees-to-pay-3-1-billion-to-resolve-aml-allegations/
- Bank of America cease-and-desist: https://www.sanctions.io/blog/occ-orders-bank-of-america-to-overhaul-aml-and-sanctions-compliance-programs
- EU AMLD6/AMLR: https://www.dlapiper.com/en-us/insights/publications/global-anti-corruption-perspective/new-eu-anti-money-laundering-rules-what-to-know
- EBA consultation (March 2025): https://www.eba.europa.eu/publications-and-media/press-releases/eba-consults-new-rules-related-anti-money-laundering-and-countering-financing-terrorism-package
- AML failures 2024: https://consilient.com/aml-failures-and-lessons-learned
- EDD for MSBs: https://alessa.com/blog/enhanced-due-diligence-in-high-risk-sectors/
- Risk scoring methodology: https://www.tookitaki.com/compliance-hub/building-an-effective-aml-risk-rating-system-best-practices
- Customer risk factors: https://alessa.com/blog/anti-money-laundering-risk-scoring-factors/
