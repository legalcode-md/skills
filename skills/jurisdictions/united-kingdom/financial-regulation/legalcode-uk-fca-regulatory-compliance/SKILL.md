---
name: legalcode-uk-fca-regulatory-compliance
description: 'Assess, audit, and remediate Financial Conduct Authority (FCA) regulatory compliance for
  UK-regulated firms across the full FCA Handbook: authorization under FSMA 2000 s.19 and the Regulated
  Activities Order 2001 (RAO), Principles for Businesses (PRIN 1–12 including Consumer Duty Principle
  12), Senior Managers and Certification Regime (SM&CR — SYSC 2–4, COCON), Consumer Duty (FCA PS22/9 —
  four outcomes, cross-cutting rules, annual board report), Conduct of Business Sourcebook (COBS — client
  categorisation, suitability, best execution, MiFID II/UK MiFIR transaction reporting), Client Assets
  Sourcebook (CASS 6 custody, CASS 7 client money), financial promotions (FSMA 2000 s.21, FP Gateway February
  2024, COBS 4), prudential requirements (MiFIDPRU ICARA, IFPR, legacy BIPRU/GENPRU), regulatory reporting
  (RegData/Gabriel, CMAR), Systems and Controls (SYSC — governance, risk management, compliance function,
  operational resilience), and financial crime controls (SYSC 6 AML/KYC, sanctions screening).'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess, audit, and remediate Financial Conduct Authority (FCA) regulatory compliance for UK-regulated firms across the full FCA Handbook: authorization under FSMA 2000 s.19 and the Regulated Activities Order 2001 (RAO), Principles for Businesses (PRIN 1–12 including Consumer Duty Principle 12), Senior Managers and Certification Regime (SM&CR — SYSC 2–4, COCON), Consumer Duty (FCA PS22/9 — four outcomes, cross-cutting rules, annual board report), Conduct of Business Sourcebook (COBS — client categorisation, suitability, best execution, MiFID II/UK MiFIR transaction reporting), Client Assets Sourcebook (CASS 6 custody, CASS 7 client money), financial promotions (FSMA 2000 s.21, FP Gateway February 2024, COBS 4), prudential requirements (MiFIDPRU ICARA, IFPR, legacy BIPRU/GENPRU), regulatory reporting (RegData/Gabriel, CMAR), Systems and Controls (SYSC — governance, risk management, compliance function, operational resilience), and financial crime controls (SYSC 6 AML/KYC, sanctions screening). Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE gap analysis with prioritised remediation roadmap, SMCR governance templates, Consumer Duty board report scaffold, and Glass Box audit trail suitable for FCA correspondence. Use when assessing existing FCA compliance posture, building a compliance programme for newly authorised firms, preparing for FCA supervisory visits or enforcement action, conducting pre-acquisition FCA due diligence, reviewing SM&CR governance arrangements, assessing Consumer Duty implementation, or auditing financial promotions approval processes. Applies to all FCA-authorised firms and appointed representatives (deposit-takers, investment firms, AIFM/UCITS managers, consumer credit firms, mortgage lenders, insurance intermediaries, payment institutions, e-money institutions). Jurisdiction: England and Wales (primary); Scotland and Northern Ireland share the same FCA Handbook but have separate court and regulatory referral routes. Dual-regulated firms (banks, insurers) should supplement this skill with a separate PRA prudential assessment.


# UK FCA Regulatory Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance with FCA
> regulatory requirements under the Financial Services and Markets Act 2000 (FSMA 2000) and the
> FCA Handbook. It does not constitute legal advice, regulatory guidance, or a compliance
> certification. FCA rules are applied on a facts-and-circumstances basis; no compliance
> framework guarantees immunity from enforcement. All FCA Handbook citations, enforcement
> examples, and regulatory guidance referenced here carry hallucination risk — verify against
> current FCA Handbook text at fca.org.uk/handbook, FCA Dear CEO letters, Final Notices, and
> primary legislation at legislation.gov.uk before relying on them. FCA Handbook rules are
> amended frequently; confirm currency before use. This skill does not replace advice from a
> qualified solicitor or FCA compliance professional. The FCA's supervisory approach and
> enforcement priorities evolve; verify current FCA expectations before use.

---

## Purpose and Scope

This skill assesses an FCA-regulated firm's compliance posture across the FCA Handbook,
identifies regulatory gaps, classifies their severity, and produces a prioritised remediation
roadmap with board-level governance recommendations.

**Covers:**

- FCA authorisation status and scope (FSMA 2000 s.19, RAO 2001, threshold conditions)
- All 12 Principles for Businesses (PRIN 1–12) including Consumer Duty (Principle 12)
- Senior Managers and Certification Regime (SM&CR): SMFs, Conduct Rules, Prescribed
  Responsibilities, Statements of Responsibility, annual Fit and Proper assessments
- Consumer Duty (FCA PS22/9): all four outcomes, cross-cutting rules, annual board report
- Conduct of Business Sourcebook (COBS): client categorisation, suitability, best execution,
  UK MiFIR transaction reporting, inducements, information and disclosure
- Client Assets Sourcebook (CASS 6 and 7): client money segregation, custody safeguarding,
  CMAR reporting, resolution pack requirements
- Financial promotions: FSMA 2000 s.21 restriction, FP Approval Gateway (February 2024),
  COBS 4 financial promotion rules, social media and digital promotions
- Systems and Controls (SYSC): governance, risk management, compliance function, internal audit,
  operational resilience, outsourcing (SYSC 8), remuneration policies
- Prudential requirements: MiFIDPRU ICARA (IFPR firms), legacy BIPRU/GENPRU
- Financial crime: SYSC 6 AML/KYC, sanctions screening, PEP identification, SAR obligations
- Regulatory reporting: RegData/Gabriel submissions, CMAR, transaction reporting
- Outsourcing and third-party oversight (SYSC 8)
- COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE classification
- Prioritised remediation roadmap (IMMEDIATE / NEAR-TERM / BACKGROUND tiers)
- Glass Box audit trail for board and counsel use

**Does not:**

- Certify FCA compliance — that determination rests with the FCA
- Provide legal opinions on specific enforcement risk
- Constitute legal advice or replace qualified FCA compliance counsel
- Fully assess PRA prudential requirements for dual-regulated firms (banks, insurers) — those
  require a separate PRA assessment (IFPRU capital, CRR, Solvency II/PRA rules)
- Assess Markets in Financial Instruments Directive (MiFID II/UK MiFID) in full depth for
  investment firms operating under complex market structure arrangements
- Apply to non-FCA regulated activities (e.g., professional firms regulated by SRA, ICAEW)

**Related skills:**

- `legalcode-uk-bribery-act-compliance` — Bribery Act 2010 adequate procedures assessment;
  use alongside this skill for anti-bribery risk
- `legalcode-aml-kyc-compliance` — jurisdiction-agnostic AML/KYC programme builder; use
  when AML is the primary focus (this skill covers FCA AML at a programme level)
- `legalcode-dora-compliance-assessment` — DORA operational resilience for EU-nexus firms;
  UK FCA operational resilience uses SS1/21 and PS21/3 framework

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: England and Wales under FSMA 2000, as amended by FSMA 2023, the
Financial Services Act 2021, the Financial Services and Markets Act 2023, and secondary
legislation made under each.

**FCA Handbook authority**: The FCA Handbook is made by the FCA under its rulemaking powers
in FSMA 2000 Part 9A. Rules (marked "R") are binding; guidance (marked "G") indicates how
rules may be interpreted; evidential provisions (marked "E") create a rebuttable presumption.

**Scotland and Northern Ireland**: Share the same FSMA 2000 framework and FCA Handbook. Court
proceedings and certain regulatory referrals may differ (Court of Session, COPFS; PPS NI).

**Dual-regulated firms**: Banks, insurers, and certain investment firms are regulated by both
the FCA (conduct) and the PRA (prudential). This skill covers FCA conduct obligations only;
PRA obligations require a separate assessment.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming firm
context, the workflow pauses and asks when:

- The answer would change which FCA Handbook modules apply
- The firm's SM&CR tier or authorisation scope is uncertain
- Severity classification requires knowing the firm's risk appetite or compliance maturity
- A regulatory issue has recently changed and the firm's position is unclear

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked below. If
the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input and Establish Scope

Accept input in any of these formats:

- **Assessment brief**: Description of the firm, its regulated activities, FCA authorisation
  reference number (FRN), and what compliance areas to assess
- **Documentation**: Compliance programme policies, SMCR maps, Consumer Duty board reports,
  financial promotion files, CASS audit reports, or regulatory correspondence
- **Specific focus area**: A single module or topic (e.g., "assess our Consumer Duty board
  report" or "review our financial promotions approval process")
- **Enforcement context**: FCA supervisory notice, skilled person review, or investigation

If no input is provided, prompt the user to supply the firm's name, FRN, and regulated
activities before proceeding.

### Step 2: Gather Firm Context

**⟁ CLARIFY** — Before beginning, ask the following questions. Present as structured options
where possible. Skip questions already answered by the input.

1. **Assessment mode** — What is the primary purpose?
   - **Compliance Audit**: Assess existing compliance posture and identify gaps
   - **Programme Build**: Design a compliance programme for a newly authorised firm
   - **Pre-Supervision Preparation**: Prepare for an FCA supervisory visit, ARROW review, or
     Dear CEO letter response
   - **Enforcement Response**: Respond to a Warning Notice, Decision Notice, or s.166 skilled
     person review
   - **Acquisition Due Diligence**: Assess FCA compliance of a target regulated firm
   - **Targeted Review**: Focus on one module (e.g., Consumer Duty only, CASS only)
   - _Why this matters_: Determines whether to assess for violations or design from scratch;
     enforcement context requires privilege considerations and may need external counsel.

2. **Firm type** — What type of FCA-regulated firm?
   - Deposit-taker (bank or building society)
   - Investment firm (MIFIDPRU firm — advice, discretionary management, execution)
   - AIFM (Alternative Investment Fund Manager)
   - UCITS Management Company
   - Consumer credit firm (CONC)
   - Mortgage lender or broker (MCOBS)
   - Insurance intermediary (ICOBS)
   - Payment institution or e-money institution
   - Appointed representative (AR) or Introducer Appointed Representative (IAR)
   - Other (specify)
   - _Why this matters_: Determines which FCA Handbook modules apply and which SM&CR tier.

3. **SM&CR scope** — What is the firm's SMCR classification?
   - **Enhanced firm** (major banks, building societies, significant investment firms)
   - **Core firm** (most FCA solo-regulated firms)
   - **Limited scope firm** (smaller firms with limited permissions)
   - **Not yet assessed** — assess during the review
   - _Why this matters_: Enhanced firms have additional SMCR requirements (Individual
     Accountability functions, Prescribed Responsibilities, handover procedures).

4. **Compliance maturity** — Current state of compliance programme?
   - No formal programme in place
   - Basic policies exist but inconsistently applied
   - Structured programme with partial FCA Handbook integration
   - Full programme in place — seeking gap assessment
   - Programme under remediation following an FCA finding or internal failure
   - _Why this matters_: Determines whether to audit against the standard or design
     from scratch; remediation programmes need different output format.

5. **Consumer Duty status** — Has the firm implemented Consumer Duty (effective July 2023)?
   - Fully implemented with board report in place
   - Partially implemented (open-ended products done; closed book outstanding)
   - Implementation in progress
   - Not yet assessed
   - _Why this matters_: Consumer Duty (Principle 12, PS22/9) is now a core FCA obligation;
     non-implementation is a CRITICAL EXPOSURE finding for retail-facing firms.

If the user provides partial context, proceed with stated assumptions. State assumptions
explicitly at the start of the assessment.

### Step 3: Establish the Regulatory Baseline

Before assessing compliance, map the applicable FCA Handbook modules to the firm.

**Core modules applicable to all FCA-authorised firms:**

| Module    | Description                                      | Applicability                         |
| --------- | ------------------------------------------------ | ------------------------------------- |
| **PRIN**  | Principles for Businesses (1–12)                 | All authorised firms                  |
| **SYSC**  | Systems and Controls                             | All authorised firms                  |
| **COCON** | Code of Conduct Sourcebook (SM&CR Conduct Rules) | All authorised firms                  |
| **FIT**   | Fit and Proper Test (for approved persons)       | All approved persons                  |
| **COND**  | Threshold Conditions                             | All authorised firms                  |
| **DEPP**  | Decision Procedure and Penalties                 | All authorised firms                  |
| **GEN**   | General Provisions                               | All authorised firms                  |
| **DISP**  | Dispute Resolution (Complaints)                  | All firms dealing with retail clients |

**Sector-specific modules — apply based on firm type:**

| Module           | Description                                      | Applies To                                   |
| ---------------- | ------------------------------------------------ | -------------------------------------------- |
| **COBS**         | Conduct of Business Sourcebook                   | Investment firms                             |
| **ICOBS**        | Insurance: Conduct of Business                   | Insurance intermediaries                     |
| **MCOBS**        | Mortgages and Home Finance                       | Mortgage lenders/brokers                     |
| **CONC**         | Consumer Credit Sourcebook                       | Consumer credit firms                        |
| **CASS**         | Client Assets Sourcebook                         | Investment firms holding client money/assets |
| **COLL**         | Collective Investment Schemes                    | UCITS managers                               |
| **FUND**         | Investment Funds Sourcebook                      | AIFM                                         |
| **MiFIDPRU**     | Prudential sourcebook for MiFID investment firms | Investment firms (IFPR)                      |
| **BIPRU/GENPRU** | Legacy prudential (pre-IFPR investment firms)    | Legacy firms                                 |
| **MAR**          | Market Conduct                                   | Investment firms, benchmark administrators   |
| **BCOBS**        | Banking Conduct of Business                      | Deposit-takers                               |

**⟁ CLARIFY** — If the firm is dual-regulated (FCA + PRA), ask:

- Should the assessment cover FCA conduct obligations only, or include a PRA prudential overlay?
- If PRA is included, note that this skill does not cover PRA Rulebook (CRR, Solvency II);
  a separate PRA-specific assessment should be conducted.

**Use legalcode-mcp** (if connected) to:

- Retrieve current FCA Handbook text for the identified modules
- Search for recent FCA enforcement actions against firms in this sector
- Retrieve relevant Dear CEO letters and thematic review findings
- Save to `/tmp/fca-regulatory-baseline.md`

**If legalcode-mcp is not connected:**

- Mark all FCA Handbook rule citations with [VERIFY against fca.org.uk/handbook]
- Note in Glass Box: `legalcode_mcp: "Not connected — FCA Handbook currency verification required"`
- Focus on structural quality and programme assessment; note that specific rule text
  has not been independently verified against current Handbook

### Step 4: FCA Authorisation and Permissions Assessment

Verify that the firm's authorisation status and permissions are appropriate for its activities.

**4a. Authorisation Status Check**

| Check                                   | Rule           | Assessment Questions                                                                                                                        |
| --------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| FCA authorisation current               | FSMA 2000 s.19 | Is the firm currently FCA-authorised (check FCA Register at register.fca.org.uk)?                                                           |
| Regulated activities within permissions | RAO 2001       | Are all regulated activities the firm carries out within its FCA permissions?                                                               |
| Appointed representative arrangements   | FSMA 2000 s.39 | If the firm has ARs/IARs, are they registered on the FCA Register?                                                                          |
| Threshold conditions met                | COND           | Does the firm continue to meet threshold conditions (legal status, location, effective supervision, appropriate resources, business model)? |

**The General Prohibition (FSMA 2000 s.19)**

Every regulated activity carried on in the UK by a person who is not authorised or exempt
constitutes a criminal offence (up to 2 years' imprisonment + unlimited fine). Breach also
voids contracts with consumers (s.26–28 FSMA 2000). Assess:

- Does the firm carry out any activities outside its Part 4A permissions?
- Has the firm expanded its business model without updating its permissions?
- Are any appointed representatives conducting activities beyond their principal's permissions?

**⟁ CLARIFY** — If the firm has recently changed its business model, launched a new product,
or expanded into a new activity:

- "Have FCA permissions been updated to reflect the new activity? An application for variation
  of permissions (VOP) is required before commencing an additional regulated activity."

**4b. Consumer Duty Scope Assessment**

Consumer Duty (Principle 12, PS22/9) applies to firms that:

- Have a direct customer relationship with retail customers, OR
- Are in the distribution chain for products or services to retail customers (even without
  direct customer contact)

Assess whether the firm has correctly identified whether Consumer Duty applies to it and,
if so, which products and services are in scope (including the closed book of legacy products
from 31 July 2024).

**Classification:**

- Firm correctly identifies Consumer Duty scope: COMPLIANT
- Firm has assessed scope but incorrectly excluded some products: PARTIAL
- Firm has not assessed Consumer Duty scope at all: NON-COMPLIANT (for retail-facing firms)

### Step 5: SYSC Governance and Systems Assessment

The Systems and Controls sourcebook (SYSC) is the foundation of FCA regulatory compliance.
Assess governance, risk management, compliance, internal audit, and operational resilience.

**5a. Senior Management Governance (SYSC 2.1)**

| Element                        | FCA Standard | Assessment                                                                                                                    |
| ------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Board oversight                | SYSC 2.1.1R  | Does the board exercise effective oversight of compliance? Is compliance a standing board agenda item?                        |
| Reporting lines                | SYSC 2.1.1R  | Are reporting lines clear from business functions → risk function → compliance → board?                                       |
| Governance committee structure | SYSC 2.1.1R  | Do governance committees (Audit, Risk, Compliance) meet regularly with appropriate membership?                                |
| Compliance reporting to board  | SYSC 6.1.4R  | Does the compliance function have direct access to the board or a board committee?                                            |
| Management information         | SYSC 6.1.4R  | Does the board receive adequate MI on compliance matters (regulatory breach log, complaints data, training completion rates)? |

**5b. Compliance Function (SYSC 6.1)**

| Element                    | FCA Standard | Assessment                                                                                                                 |
| -------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Existence and independence | SYSC 6.1.1R  | Is there a dedicated compliance function or compliance officer? Is compliance genuinely independent of business functions? |
| Compliance remuneration    | SYSC 6.1.4R  | Is the compliance function's remuneration not tied to business performance?                                                |
| Compliance authority       | SYSC 6.1.4R  | Does the compliance function have authority to conduct testing, investigations, and access all business areas?             |
| Compliance reporting       | SYSC 6.1.4R  | Does compliance produce a regular compliance report to senior management/board?                                            |
| Proportionality            | SYSC 6.1     | Is the compliance function proportionate to the firm's size, complexity, and risk profile?                                 |

**5c. Risk Management (SYSC 3/7)**

| Element                 | FCA Standard | Assessment                                                                                                           |
| ----------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------- |
| Risk appetite statement | SYSC 7.1     | Is there a documented risk appetite statement approved by the board?                                                 |
| Risk identification     | SYSC 7.1     | Is there a process for identifying, measuring, and monitoring all material risks?                                    |
| Three lines of defence  | SYSC 7.1     | Is the Three Lines of Defence model implemented (business = 1st line, risk/compliance = 2nd line, audit = 3rd line)? |
| Risk register           | SYSC 7.1     | Is there a risk register? Is it reviewed and updated regularly?                                                      |
| Risk reporting          | SYSC 7.1     | Does risk management report to the Risk Committee / board on at least a quarterly basis?                             |

**5d. Internal Audit (SYSC 3.2/6.2)**

| Element                 | FCA Standard | Assessment                                                                                       |
| ----------------------- | ------------ | ------------------------------------------------------------------------------------------------ |
| Internal audit function | SYSC 6.2.1R  | Is there an internal audit function (or appropriate proportionate equivalent for smaller firms)? |
| Audit plan              | SYSC 6.2.1R  | Is there a risk-based audit plan covering all significant activities on a rolling basis?         |
| Audit independence      | SYSC 6.2.1R  | Is the internal audit function independent of business functions?                                |
| Audit reporting         | SYSC 6.2.1R  | Does internal audit report to the Audit Committee or board? Are findings tracked to closure?     |

**5e. Operational Resilience (SYSC 15A — from March 2022)**

| Element                                | FCA Standard   | Assessment                                                                                              |
| -------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| Important business services identified | SS1/21, PS21/3 | Has the firm identified its important business services (IBS)?                                          |
| Impact tolerances set                  | SS1/21, PS21/3 | Has the firm set impact tolerances for each IBS?                                                        |
| Mapping                                | SS1/21, PS21/3 | Has the firm mapped the people, processes, technology, facilities, and information supporting each IBS? |
| Scenario testing                       | SS1/21, PS21/3 | Has the firm tested its ability to remain within impact tolerances through scenario tests?              |
| Self-assessment                        | SS1/21, PS21/3 | Has the firm completed an operational resilience self-assessment (deadline: March 2025)?                |

**Classification guidance for SYSC:**

- All elements present and effective → COMPLIANT
- Most elements present; minor gaps in MI or committee structure → PARTIAL
- Compliance function lacks independence, or key governance elements absent → NON-COMPLIANT
- No compliance function, no board oversight, no governance framework → CRITICAL EXPOSURE

### Step 6: SM&CR Assessment

The Senior Managers and Certification Regime (SM&CR) replaced the Approved Persons Regime
for most firms. Assess all three tiers.

**6a. Senior Manager Functions (SMFs)**

Assess whether all required Senior Manager Functions are filled and the holders are FCA-approved.

**Core SMFs applicable to most FCA solo-regulated firms (SYSC 2.2.10R):**

| SMF    | Function                                  | Key Assessment Points                                                  |
| ------ | ----------------------------------------- | ---------------------------------------------------------------------- |
| SMF 1  | Chief Executive                           | CEO/MD is FCA-approved? Statement of Responsibilities in place?        |
| SMF 3  | Executive Director                        | Any executive director with significant influence is FCA-approved?     |
| SMF 16 | Compliance Oversight                      | Compliance officer is FCA-approved? Sufficient seniority and resource? |
| SMF 17 | Money Laundering Reporting Officer (MLRO) | MLRO is FCA-approved? Annual report to board?                          |
| SMF 27 | Partner (for partnerships)                | Applicable partners approved?                                          |
| SMF 29 | Chief Finance Function (larger firms)     | CFO is FCA-approved? [VERIFY: scope of SMF 29 application]             |

**Enhanced firm additional SMFs (SYSC 2.2.7R):**

| SMF    | Function                     |
| ------ | ---------------------------- |
| SMF 2  | Chief Finance Function       |
| SMF 4  | Chief Risk Officer           |
| SMF 5  | Head of Internal Audit       |
| SMF 7  | Group Entity Senior Manager  |
| SMF 18 | Other Overall Responsibility |
| SMF 22 | Other Local Responsibility   |
| SMF 24 | Chief Operations Function    |

**⟁ CLARIFY** — For enhanced firms:

- "Have all Prescribed Responsibilities (PRs) under SYSC 24 been allocated to named SMFs?
  Are the PRs documented in each SMF's Statement of Responsibilities?"

**6b. Statements of Responsibility (SoR)**

| Element                              | FCA Standard | Assessment                                                                        |
| ------------------------------------ | ------------ | --------------------------------------------------------------------------------- |
| SoR in place for all SMFs            | SYSC 25.2    | Does every SMF holder have a written, current Statement of Responsibilities?      |
| SoR reflects actual responsibilities | SYSC 25.2    | Does the SoR accurately describe the SMF's responsibilities (not boilerplate)?    |
| SoR updated on change                | SYSC 25.2    | Are SoRs updated when responsibilities change (within 7 business days of change)? |
| SoR approved at board level          | SYSC 25.2    | Are SoRs approved by the board or an appropriate governance committee?            |

**6c. Certification Regime (SYSC 5.2/27)**

| Element                      | FCA Standard | Assessment                                                                                                                                             |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Certified persons identified | SYSC 27      | Has the firm identified all staff performing Certification Functions (e.g., significant influence functions, client-dealing roles, investment advice)? |
| Annual certification         | SYSC 27.2    | Are all certified persons certified (and re-certified annually) as Fit and Proper?                                                                     |
| Fit and Proper assessment    | FIT 1.3      | Does the annual Fit and Proper assessment cover honesty/integrity, competence/capability, and financial soundness?                                     |
| Criminal record checks       | SYSC 27.2    | Are criminal record checks conducted as part of F&P assessment?                                                                                        |
| Regulatory references        | SYSC 22      | Are regulatory references obtained from previous employers for new SMF and certified persons?                                                          |

**6d. Conduct Rules (COCON)**

| Element                       | FCA Standard | Assessment                                                                                          |
| ----------------------------- | ------------ | --------------------------------------------------------------------------------------------------- |
| Conduct Rules communicated    | COCON 1      | Are Individual Conduct Rules and Senior Manager Conduct Rules communicated to all applicable staff? |
| Training on Conduct Rules     | COCON 1      | Have all applicable staff received training on Conduct Rules relevant to their role?                |
| Breach recording              | COCON 1      | Are Conduct Rule breaches recorded and reported to the FCA within required timeframes?              |
| Annual Conduct Rules training | COCON 1      | Is Conduct Rules training refreshed annually or when rules change?                                  |

**Classification guidance for SM&CR:**

- All SMF holders approved, all SoRs in place, all certified persons identified and certified,
  Conduct Rules trained → COMPLIANT
- SMF holders approved but SoRs incomplete or out of date; certification partially done → PARTIAL
- Senior manager without SMF approval, material gaps in certification regime → NON-COMPLIANT
- No SM&CR implementation; firm continuing activities without SMF approval where required → CRITICAL EXPOSURE

### Step 7: Consumer Duty Assessment (Principle 12, PS22/9)

Consumer Duty (effective 31 July 2023 for open products; 31 July 2024 for closed books) is
now a central FCA supervisory priority. Assess all four outcomes and the cross-cutting rules.

**7a. Cross-Cutting Rules (PRIN 2A.2)**

The three cross-cutting rules underpin all four outcomes:

| Rule                                            | Content      | Assessment                                                                                                               |
| ----------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Act in good faith                               | PRIN 2A.2.1R | Does the firm act in good faith toward retail customers? Are there examples of exploitation, opacity, or sharp practice? |
| Avoid foreseeable harm                          | PRIN 2A.2.2R | Does the firm actively identify and prevent foreseeable harm to retail customers?                                        |
| Enable customers to pursue financial objectives | PRIN 2A.2.3R | Does the firm support customers in achieving their financial objectives (not just sell products)?                        |

**7b. Four Consumer Duty Outcomes**

**Outcome 1: Products and Services (PRIN 2A.3)**

| Element                      | FCA Standard | Assessment                                                                                                    |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------- |
| Product approval process     | PRIN 2A.3.2R | Is there a documented product approval or review process?                                                     |
| Target market identification | PRIN 2A.3.2R | Has the firm identified the target market for each product (including negative target market)?                |
| Product review frequency     | PRIN 2A.3.5R | Are products reviewed to ensure they continue to meet consumer needs (at least annually for retail products)? |
| Distribution strategy        | PRIN 2A.3    | Is the distribution strategy appropriate for the identified target market?                                    |

**Outcome 2: Price and Value (PRIN 2A.4)**

| Element                                      | FCA Standard | Assessment                                                                   |
| -------------------------------------------- | ------------ | ---------------------------------------------------------------------------- |
| Value assessment                             | PRIN 2A.4.1R | Has the firm conducted a price and value assessment for its products?        |
| Price transparency                           | PRIN 2A.4.1R | Are all costs and charges clear and transparent to customers?                |
| Fair value monitoring                        | PRIN 2A.4.4R | Is fair value monitored on an ongoing basis (not just at product launch)?    |
| Manufacturer/distributor information sharing | PRIN 2A.4    | Is relevant price and value information shared along the distribution chain? |

**Outcome 3: Consumer Understanding (PRIN 2A.5)**

| Element                            | FCA Standard | Assessment                                                                                               |
| ---------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| Communications appropriateness     | PRIN 2A.5.1R | Are customer communications clear, fair, and not misleading? Are they tested for consumer comprehension? |
| Vulnerable customer identification | PRIN 2A.5.2R | Does the firm identify and make adjustments for vulnerable customers?                                    |
| Consumer testing                   | PRIN 2A.5    | Has the firm tested communications and disclosures with representative customers?                        |
| Digital channel review             | PRIN 2A.5    | Are digital journeys (apps, websites, online processes) reviewed for consumer understanding?             |

**Outcome 4: Consumer Support (PRIN 2A.6)**

| Element                     | FCA Standard | Assessment                                                                     |
| --------------------------- | ------------ | ------------------------------------------------------------------------------ |
| Accessible support          | PRIN 2A.6.1R | Can customers access the support they need without unreasonable barriers?      |
| Complaints handling         | DISP 1.3.1R  | Are complaints acknowledged within 1 business day and resolved within 8 weeks? |
| Switching and cancellation  | PRIN 2A.6    | Are switching and cancellation processes as easy as joining?                   |
| Vulnerable customer support | PRIN 2A.6    | Are additional support channels available for vulnerable customers?            |

**7c. Consumer Duty Board Report (PS22/9)**

FCA rules require a Consumer Duty board report to be completed annually (from 31 July 2024):

| Element                       | FCA Standard | Assessment                                                                        |
| ----------------------------- | ------------ | --------------------------------------------------------------------------------- |
| Report completed              | PS22/9       | Has the annual Consumer Duty board report been completed?                         |
| Four outcomes assessed        | PS22/9       | Does the report address all four outcomes with specific data and evidence?        |
| Approved by board             | PS22/9       | Has the board reviewed and approved the report?                                   |
| Actions arising               | PS22/9       | Has the board identified actions arising from the report (if deficiencies found)? |
| Retained as regulatory record | PS22/9       | Is the report retained as a regulatory record accessible to FCA?                  |

**Classification guidance for Consumer Duty:**

- All four outcomes assessed, board report in place, cross-cutting rules embedded → COMPLIANT
- Two or more outcomes partially assessed, board report drafted but not board-approved → PARTIAL
- One or more outcomes not assessed; board report not in place for a retail-facing firm → NON-COMPLIANT
- Consumer Duty not implemented at all for an open-book retail firm (post July 2023) → CRITICAL EXPOSURE

**⟁ CLARIFY** — If the firm has a closed book of legacy products:

- "Were closed-book products included in the Consumer Duty board report by 31 July 2024?
  The FCA extended the deadline for closed books to 31 July 2024; failure to meet this
  extension is a material compliance failure."

### Step 8: Conduct of Business Assessment (COBS / ICOBS / MCOBS / CONC)

Assess the conduct of business rules applicable to the firm's sector.

**8a. COBS — Investment Firms**

| Area                       | Key Rules           | Assessment                                                                                                                                          |
| -------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client categorisation      | COBS 3              | Are clients correctly categorised (retail, professional, eligible counterparty)? Are opt-up/opt-down procedures in place and documented?            |
| Information and disclosure | COBS 4 and 6        | Are required disclosures provided to clients at the right time (pre-sale information, key investor information, ongoing reporting)?                 |
| Suitability                | COBS 9              | For advised services: Is a suitability assessment completed before every recommendation? Are suitability reports provided?                          |
| Appropriateness            | COBS 10             | For non-advised services in complex instruments: Is an appropriateness assessment completed? Are warnings given where appropriate?                  |
| Best execution             | COBS 11             | Is a Best Execution Policy in place? Does it consider all execution factors (price, cost, speed, likelihood of execution)? Is it reviewed annually? |
| Order handling             | COBS 11             | Are client orders handled in a way that prioritises client interests? Is there an order aggregation policy?                                         |
| Inducements and conflicts  | COBS 2.3            | Are inducement rules complied with? Are all commissions and soft dollar benefits disclosed or eliminated?                                           |
| Transaction reporting      | COBS 16A / UK MiFIR | Are reportable transactions reported to an ARM or Trade Repository within required timeframes (T+1)?                                                |

**8b. ICOBS — Insurance Intermediaries**

| Area                        | Key Rules | Assessment                                                                                                                       |
| --------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Organisational requirements | ICOBS 2   | Are FCA organisational requirements for insurance distribution met (including product oversight and governance)?                 |
| Customer information        | ICOBS 4   | Is required pre-sale information provided to customers (including insurance product information document for general insurance)? |
| Advised sales               | ICOBS 4.5 | For advised sales: Is a needs assessment conducted? Is a suitability report provided?                                            |
| Cancellation rights         | ICOBS 7   | Are customers informed of their right to cancel? Are cancellation periods correct for the product type?                          |
| Claims handling             | ICOBS 8   | Are claims handled promptly, fairly, and transparently? Are claim denials communicated with reasons?                             |

**8c. MCOBS — Mortgage Lenders and Brokers**

| Area                 | Key Rules       | Assessment                                                                                                                      |
| -------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Responsible lending  | MCOBS 11        | Is an affordability assessment conducted before each mortgage recommendation? Is income and expenditure verified appropriately? |
| Suitability          | MCOBS 4.7       | Is a mortgage recommendation based on assessed customer needs? Is a suitability statement provided?                             |
| ESIS                 | MCOBS 5A        | Is a European Standardised Information Sheet (ESIS) provided at the appropriate stage?                                          |
| Vulnerable customers | MCOBS / PRIN 12 | Are vulnerable customer procedures in place throughout the mortgage application and servicing process?                          |

**8d. CONC — Consumer Credit Firms**

| Area                        | Key Rules | Assessment                                                                                                       |
| --------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| Responsible lending         | CONC 5    | Is a creditworthiness assessment conducted before each credit agreement? Is it proportionate to the credit risk? |
| Pre-contractual information | CONC 4    | Is required pre-contractual information (SECCI, pre-contract credit information) provided?                       |
| Persistent debt             | CONC 6.7  | Are customers in persistent debt identified? Are appropriate interventions made?                                 |
| Collection practices        | CONC 7    | Are debt collection practices fair? Are customers in financial difficulty treated with forbearance?              |

**Classification guidance for COBS/ICOBS/MCOBS/CONC:**

- All applicable rules met with documented compliance evidence → COMPLIANT
- Required procedures in place but inconsistently applied or partially documented → PARTIAL
- Material breaches of conduct rules (e.g., suitability reports missing, best execution not monitored) → NON-COMPLIANT
- Systematic breach of conduct rules affecting customers (e.g., no suitability assessments for advised sales) → CRITICAL EXPOSURE

### Step 9: Client Assets Assessment (CASS)

CASS applies to investment firms that hold client money (CASS 7) or custody assets (CASS 6).
CASS breaches are treated with particular severity by the FCA.

**9a. CASS 7 — Client Money**

| Element                                     | FCA Standard | Assessment                                                                                              |
| ------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| Segregation                                 | CASS 7.13    | Is client money held in segregated client bank accounts, separate from firm money?                      |
| Client bank account acknowledgement letters | CASS 7.14    | Have acknowledgement letters been obtained from all banks holding client money?                         |
| Daily reconciliation                        | CASS 7.15    | Is a daily internal and external client money reconciliation conducted?                                 |
| Shortfall resolution                        | CASS 7.15    | Are shortfalls identified in reconciliation resolved the same business day?                             |
| Client money calculation                    | CASS 7.16    | Is the client money resource calculated correctly (normal approach vs. alternative approach)?           |
| Third-party agents                          | CASS 7.12    | If client money is passed to third-party agents, are appropriate agreements and due diligence in place? |

**9b. CASS 6 — Custody Assets (Safe Custody)**

| Element                             | FCA Standard | Assessment                                                                                           |
| ----------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| Segregation of custody assets       | CASS 6.2     | Are custody assets held separately from firm assets?                                                 |
| Third-party custodian due diligence | CASS 6.3     | Has due diligence been conducted on all third-party custodians? Are appropriate agreements in place? |
| External reconciliation             | CASS 6.6     | Are custody records reconciled against third-party custodian records at appropriate frequency?       |
| Title transfer arrangements         | CASS 6.4     | Are any title transfer collateral arrangements (TTCAs) documented and disclosed to clients?          |

**9c. CASS Operational Oversight**

| Element                    | FCA Standard | Assessment                                                                                     |
| -------------------------- | ------------ | ---------------------------------------------------------------------------------------------- |
| CASS Operational Oversight | CASS 1A.3    | Has a CASS Operational Oversight function been designated (required for CASS large firms)?     |
| CMAR reporting             | CASS 1A.2    | Is the Client Money and Assets Return (CMAR) submitted to RegData at required frequency?       |
| CASS resolution pack       | CASS 10      | Is there a CASS resolution pack in place to enable rapid return of client assets in wind-down? |
| External CASS audit        | CASS 1A.2.5  | Has an annual CASS audit been conducted by an independent external auditor?                    |

**Classification guidance for CASS:**

- Full segregation, daily reconciliation, CMAR current, external audit done → COMPLIANT
- Minor reconciliation gaps, CMAR late but submitted, CASS resolution pack incomplete → PARTIAL
- Material reconciliation failures, third-party agreements absent, CMAR not submitted → NON-COMPLIANT
- Client money commingled with firm money; no segregation; ongoing CASS breach → CRITICAL EXPOSURE

**Note**: CASS breaches — particularly client money commingling — are among the most severely
enforced FCA rules. CRITICAL EXPOSURE in CASS requires immediate remediation and likely
notification to the FCA.

### Step 10: Financial Promotions Assessment

Financial promotions are regulated under FSMA 2000 s.21 and the Financial Promotion Order (FPO).
Since February 2024, a new FCA financial promotion gateway requires third-party promotions
approvers to be specifically authorised for this function.

**10a. Section 21 FSMA 2000 — The Financial Promotion Restriction**

| Element                                                 | FCA Standard                 | Assessment                                                                                                                                                                   |
| ------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Promotions only issued or approved by authorised person | FSMA 2000 s.21               | Are all financial promotions either issued by the firm itself (as an authorised firm) or approved by an authorised person with s.21 approval permission?                     |
| FP Gateway compliance                                   | FSMA 2000 s.21 / FCA PS23/13 | If the firm approves financial promotions for unauthorised persons: has the firm obtained specific FCA permission for this activity (FP Gateway, effective 7 February 2024)? |
| FPO exemptions correctly applied                        | FPO 2005                     | If relying on FPO exemptions (e.g., certified high net worth investor, sophisticated investor), are the exemption conditions fully met?                                      |

**10b. COBS 4 Financial Promotion Rules**

| Element                         | FCA Standard | Assessment                                                                                                                     |
| ------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Fair, clear, and not misleading | COBS 4.2.1R  | Are all financial promotions fair, clear, and not misleading? Is there a documented review/approval process?                   |
| Risk warnings                   | COBS 4.5     | Do financial promotions include appropriate risk warnings (e.g., capital at risk warnings for investment products)?            |
| Performance claims              | COBS 4.6     | Do past performance claims comply with COBS 4.6 requirements (prominent warnings, representative periods)?                     |
| Real-time vs. non-real-time     | COBS 4.8     | Are different rules applied appropriately to real-time (telephone, in-person) and non-real-time (written, digital) promotions? |

**10c. Digital and Social Media Financial Promotions**

| Element                             | FCA Standard                            | Assessment                                                                                                                                                          |
| ----------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Social media compliance             | FCA Financial Promotion Guidance FG24/1 | Are social media posts reviewed against COBS 4 standards before publication?                                                                                        |
| Influencer and affiliate promotions | FG24/1                                  | If influencers or affiliates promote the firm's products: are the promotions approved by an authorised person? Are they clearly identified as financial promotions? |
| Platform-specific rules             | FG24/1                                  | Are short-form promotions (Instagram, TikTok, Twitter/X) assessed for compliance given character limits and their impact on disclosures?                            |
| Cryptoasset promotions              | COBS 4.14 (from October 2023)           | If the firm promotes qualifying cryptoassets: are enhanced rules (risk warnings, 24-hour cooling-off, appropriateness) applied?                                     |

**Classification guidance for Financial Promotions:**

- Documented approval process, compliant promotions, FP Gateway obtained if needed → COMPLIANT
- Approval process exists but inconsistently applied; minor disclosure gaps → PARTIAL
- Material COBS 4 breaches (misleading promotions, missing risk warnings) → NON-COMPLIANT
- Unlicensed approval of third-party promotions (post-February 2024 FP Gateway) → CRITICAL EXPOSURE

### Step 11: Prudential Requirements Assessment

Assess the firm's compliance with applicable prudential rules.

**11a. Investment Firms — MiFIDPRU / IFPR (from 1 January 2022)**

The Investment Firms Prudential Regime (IFPR) replaced BIPRU for most FCA investment firms.

| Element                         | FCA Standard | Assessment                                                                                                                                                    |
| ------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ICARA completed                 | MiFIDPRU 7   | Has the firm completed an Internal Capital Adequacy and Risk Assessment (ICARA) at least annually?                                                            |
| Own funds requirement met       | MiFIDPRU 4   | Does the firm hold own funds at least equal to the higher of: Permanent Minimum Requirement (PMR), Fixed Overhead Requirement (FOR), or K-factor requirement? |
| Liquid assets threshold met     | MiFIDPRU 6   | Does the firm hold liquid assets at least equal to one-third of the FOR?                                                                                      |
| Wind-down planning              | MiFIDPRU 7.5 | Has the firm completed a wind-down plan as part of ICARA?                                                                                                     |
| Overall Financial Adequacy Rule | MiFIDPRU 7.4 | Does the firm's ICARA assess whether it has adequate own funds and liquid assets to wind down in an orderly manner?                                           |
| Regulatory reporting            | MiFIDPRU 9   | Is required prudential regulatory reporting submitted to RegData on time?                                                                                     |

**11b. Legacy Firms — BIPRU/GENPRU**

[VERIFY: Legacy BIPRU/GENPRU firms pre-dating IFPR — confirm current status. Most investment
firms should have migrated to IFPR by now. Confirm with firm whether they remain in the legacy
regime and why.]

**11c. Deposit-Takers and Dual-Regulated Firms**

Capital requirements for banks and building societies are set by the PRA (CRD/CRR framework).
This skill does not cover PRA prudential rules. Note this limitation in the Glass Box.

**Classification guidance for Prudential:**

- ICARA completed, own funds and liquidity requirements met, reporting current → COMPLIANT
- ICARA conducted but outdated or wind-down plan incomplete → PARTIAL
- Own funds below regulatory minimum; ICARA not completed → NON-COMPLIANT
- Firm operating below permanent minimum own funds requirement → CRITICAL EXPOSURE

### Step 12: Financial Crime Controls Assessment

**12a. AML/KYC Programme (SYSC 6.3, Money Laundering Regulations 2017)**

| Element                           | FCA Standard         | Assessment                                                                                                                  |
| --------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| MLRO appointed and approved       | SYSC 6.3.9R          | Is an MLRO designated as SMF 17? Are they FCA-approved?                                                                     |
| Customer due diligence            | MLR 2017 Reg. 28     | Is CDD conducted at onboarding? Are standard, enhanced, and simplified CDD procedures applied based on risk?                |
| Beneficial ownership verification | MLR 2017 Reg. 28(10) | Is beneficial ownership verified for corporate clients?                                                                     |
| Ongoing monitoring                | MLR 2017 Reg. 28(11) | Is ongoing monitoring of customer transactions and relationship conducted?                                                  |
| PEP identification                | MLR 2017 Reg. 35     | Are politically exposed persons identified and subject to enhanced due diligence?                                           |
| SAR submissions                   | POCA 2002 s.330      | Is there a Suspicious Activity Report (SAR) procedure? Are SARs submitted to the National Crime Agency (NCA) when required? |
| MLRO annual report                | SYSC 6.3.9R          | Does the MLRO submit an annual report to the board covering ML/TF risk and AML programme effectiveness?                     |

**12b. Sanctions Screening (SYSC 6, FSMA 2000 s.146)**

| Element                           | Assessment                                                                                  |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| Customer screening at onboarding  | Are customers screened against UK sanctions lists (OFSI), EU lists, and OFAC at onboarding? |
| Ongoing screening                 | Are customers re-screened when sanctions lists are updated?                                 |
| Transaction screening             | Are transactions screened for sanctions exposure?                                           |
| PEP/sanctions screening for staff | Are new employees and business partners screened?                                           |

**Classification guidance for Financial Crime:**

- Documented AML programme, MLRO in place, CDD applied consistently, SAR process active → COMPLIANT
- MLRO in place but CDD applied inconsistently; SAR process exists but alerts are low → PARTIAL
- Material CDD gaps; beneficial ownership not verified; no ongoing monitoring → NON-COMPLIANT
- No AML programme; no MLRO; ongoing business with high-risk customers without CDD → CRITICAL EXPOSURE

### Step 13: Complaints Handling Assessment (DISP)

| Element                    | FCA Standard | Assessment                                                                                                        |
| -------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Complaint identification   | DISP 1.2.1R  | Are complaints correctly identified (oral and written expressions of dissatisfaction from eligible complainants)? |
| Acknowledgement            | DISP 1.6.1R  | Are complaints acknowledged promptly (within 1 business day of receipt)?                                          |
| Investigation              | DISP 1.6.2R  | Are complaints investigated fairly and objectively?                                                               |
| Resolution timeline        | DISP 1.6.2R  | Are complaints resolved within 8 weeks (3 weeks for payment services complaints)?                                 |
| Final response content     | DISP 1.6.4R  | Do final responses include: outcome, reasoning, and FOS referral rights (if not upheld)?                          |
| FOS escalation information | DISP 1.6.7R  | Are complainants informed of their right to refer to the Financial Ombudsman Service?                             |
| Complaint record-keeping   | DISP 1.9.1R  | Are all complaints and their outcomes recorded for at least 3 years (5 years for MiFID business)?                 |
| Regulatory reporting       | DISP 1.10.1R | Are half-yearly complaint data returns submitted to the FCA via RegData?                                          |

**Classification guidance for DISP:**

- All elements compliant, regular FOS data submitted → COMPLIANT
- Minor timeline delays (within days); FOS referral information occasionally missing → PARTIAL
- Systematic complaint handling delays; FOS rights not communicated → NON-COMPLIANT
- No complaint handling process; complaints suppressed or unacknowledged → CRITICAL EXPOSURE

### Step 14: Quality Verification

Before delivering the assessment, run all quality assurance checks.

1. **Run the 5 Citation Quality Gates** silently. Revise any failures before delivery.
2. **For every CRITICAL EXPOSURE item**, run the 3-pass Self-Interrogation. Revise if any
   pass reveals a weakness.
3. **Assign a Confidence Score** to each material finding.
4. **Verify completeness**: confirm all applicable modules have been assessed (or documented
   as out of scope with reasons).
5. **Generate the Glass Box Audit Trail** and append it to the output.

### Step 15: Deliver Assessment Report

Generate the final output using the **Output Format Template** below. Tailor the depth
to the firm's size and risk profile — a sole-trader AR does not need the same report
depth as a large investment manager.

---

## Deviation Severity Classification

### COMPLIANT — Green

The firm's policies, procedures, and controls meet or exceed the FCA Handbook standard for its
type, size, and risk profile. Evidence of effective implementation is present.

**Examples:**

- Best execution procedures exceed COBS 11 minimum and include venue analysis and annual review
- Client money is fully segregated with daily reconciliation and current CMAR submissions
- Consumer Duty board report completed on time with all four outcomes addressed
- SM&CR certification conducted annually with documented F&P assessments

**Action**: Note for awareness; include in next periodic assessment. No immediate action needed.

---

### PARTIAL — Amber

The firm's approach is broadly in the right direction but falls short of full compliance. Policies
exist but have gaps, are inconsistently applied, or lack monitoring evidence. Non-material breaches
may have occurred but are remediable without immediate escalation.

**Examples:**

- SMCR certifications completed but not annually reviewed; last review 18 months ago
- Complaints acknowledged but final response letters do not consistently include FOS referral rights
- Consumer Duty board report drafted but not yet board-approved
- Best execution policy exists but annual review not documented
- AML CDD conducted for new customers but ongoing monitoring is not documented

**Action**: Generate specific remediation steps; assign NEAR-TERM (30–90 days) timeline;
explain regulatory risk if issue remains unaddressed.

---

### NON-COMPLIANT — Red

The firm's policies, procedures, or controls fall materially short of FCA Handbook requirements.
A breach of FCA rules is present or imminent. Escalation to the board and senior compliance
counsel is recommended.

**Examples:**

- No documented complaints procedure despite DISP 1 requirement
- Consumer Duty not implemented for an open-book retail firm (post July 2023)
- MLRO not appointed or not FCA-approved (SMF 17)
- No client money segregation review conducted; clients' money held in general account
- Financial promotions issued without s.21 approval or FCA authorisation
- SM&CR Statements of Responsibility not in place for any SMF holder
- Best execution obligations not monitored for 12+ months

**Action**: Escalate immediately to board and Audit/Risk Committee; explain specific Handbook
rule breached; provide market-standard remediation language; recommend IMMEDIATE timeline
(0–30 days); assess whether FCA notification is required under FSMA 2000 s.64A/COND.

---

### CRITICAL EXPOSURE — Red (Escalate Immediately)

A serious, ongoing, or systemic breach of core FCA rules. FCA enforcement action is probable
absent immediate remediation. The firm's regulatory licence may be at risk. Emergency
intervention required. Legal privilege should be considered.

**Examples:**

- Client money commingled with firm money (ongoing CASS breach)
- Continuing unauthorised regulated activity (FSMA 2000 s.19 breach)
- No SM&CR framework at all (no SMF approvals, no certifications, no Conduct Rules training)
- Systematic misleading of customers through financial promotions
- Third-party financial promotions approved without FP Gateway permission (post February 2024)
- Systemic failure to submit SARs despite known suspicious transactions
- Evidence of customer harm at scale (e.g., unsuitable products sold systematically)
- Failure of regulated activity continuity following key person departure (no cover for SMF 16/17)

**Action**: IMMEDIATE escalation to board, senior management, and external legal counsel. Consider
FCA notification obligations (breach notification under COND and PRIN 11 — duty to be open with
the FCA). Consider voluntary self-disclosure to the FCA and cooperation. Emergency remediation
required; may require suspension of non-compliant activity. Self-disclosure significantly
mitigates FCA enforcement risk.

---

## Prioritisation Framework

| Priority       | Timeline    | Examples                                                                                            | Escalation                                                        |
| -------------- | ----------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **IMMEDIATE**  | 0–30 days   | Client money commingling; unapproved regulated activity; no MLRO; systematic customer harm          | Board + FCA Legal Counsel + consideration of voluntary disclosure |
| **NEAR-TERM**  | 30–90 days  | Missing policies; incomplete SMCR certifications; Consumer Duty board report outstanding; CMAR late | Board + Audit Committee + Compliance Committee                    |
| **BACKGROUND** | 90–180 days | Policy updates following new Dear CEO letter; training refreshes; process automation; enhanced MI   | Compliance function monthly review                                |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before delivery.

| Gate           | Rule                                                                                                                                                                   | Fail Action                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Source**     | Every FCA Handbook claim cites the specific rule (Module + Chapter + Rule number + status letter, e.g., "COBS 2.1R" or "SYSC 6.1.4R")                                  | Add citation or mark "[UNVERIFIED — consult FCA Handbook directly]"             |
| **Format**     | All FCA Handbook citations follow the format: Module Chapter.Section.SubsectionStatus (e.g., "COBS 2.1R", "SYSC 6.1.4R", "PRIN 2A.2.1R")                               | Fix format; mark Guidance (G) vs. Rule (R) vs. Evidential (E) correctly         |
| **Currency**   | Every cited FCA Handbook rule checked against current Handbook at fca.org.uk/handbook for amendments, supersession, or withdrawal                                      | Flag "[CHECK CURRENCY on fca.org.uk/handbook]" if relying on training knowledge |
| **Domain**     | Analysis stays within FCA Handbook; PRA rules (CRR, Solvency II, PRA Rulebook) not applied to FCA-solo firms; FCA conduct rules not confused with PRA prudential rules | Remove or flag PRA-specific rule if firm is FCA-only regulated                  |
| **Confidence** | Uncertainty stated explicitly; rule interpretation stated as interpretation, not settled fact; emerging areas flagged                                                  | Add confidence qualifier; flag "[VERIFY — FCA interpretation not yet settled]"  |

---

## Self-Interrogation for Critical Exposure Items

For every item classified CRITICAL EXPOSURE, apply this 3-pass review before delivery.

**Pass 1 — Legal Chain Integrity**

- Does the claimed breach follow logically from the specific FCA Handbook rule cited?
- Has the FCA published enforcement action or a Dear CEO letter that specifically addresses this issue?
- Would the FCA Enforcement Division treat this as a breach (or might they treat it as a supervisory rather than enforcement matter)?
- Is there a reasonable alternative interpretation of the rule that a well-advised firm could assert?

**Pass 2 — Completeness**

- Have all related Handbook rules been considered (cross-references, definitions, overlap with PRIN)?
- Have recent FCA Handbook amendments or FCA Guidance Consultations affected this rule?
- Are there Regulatory Technical Standards or FCA Dear CEO letters that clarify the requirement?
- Has recent FCA enforcement action in this area been reviewed for the current FCA position?

**Pass 3 — Proportionality and Mitigation**

- Has the firm already self-disclosed the breach? (Self-disclosure significantly mitigates FCA enforcement risk)
- Are there proportionality arguments based on the firm's size, risk profile, or complexity?
- Is this a one-off incident or a systemic failure? (Systemic failures attract higher FCA enforcement priority)
- What is the strongest argument a defence counsel would make for the firm?
- If there is a genuine ambiguity, should the classification be revised downward with a note?

If any pass reveals a weakness in the classification, revise to NON-COMPLIANT (with note) or
add a recorded mitigation factor in the Glass Box audit trail.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                                            | Action                                                                       |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Core FCA Handbook rule; no material ambiguity; settled by enforcement action or court                              | State with confidence; citation included                                     |
| **High**     | 0.80–0.94 | Clear Handbook rule; minor interpretation questions; consistent with FCA Dear CEO letter or Final Notice           | State with brief caveat; note supporting FCA publication                     |
| **Probable** | 0.60–0.79 | Good arguments but reasonable alternative interpretations exist; rule applies but proportionality questions remain | State with explicit reasoning; flag alternative interpretation               |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing FCA guidance or emerging rule; reasonable minds could differ                        | Flag for qualified counsel review; present both interpretations              |
| **Unlikely** | 0.0–0.39  | Weak basis; rule probably does not apply or interpretation is speculative                                          | Do not assert; flag "[UNCERTAIN — consult qualified FCA compliance counsel]" |

---

## Glass Box Audit Trail

Append this YAML block to every assessment output.

```yaml
glass_box:
  assessment_date: "[YYYY-MM-DD]"
  firm_name: "[Firm name and FRN]"
  assessment_type: "[Compliance Audit / Programme Build / Pre-Supervision Preparation / Enforcement Response / Acquisition Due Diligence / Targeted Review]"
  fca_handbook_modules_reviewed:
    - "PRIN"
    - "SYSC [Level: Core / Enhanced / Limited Scope]"
    - "[List all modules reviewed: COBS, ICOBS, MCOBS, CONC, CASS, COLL, FUND, MiFIDPRU, MAR, DISP, etc.]"
  firm_profile:
    firm_type: "[Deposit-taker / Investment firm / AIFM / UCITS / Consumer credit / Mortgage / Insurance intermediary / Payment institution / Other]"
    smcr_scope: "[Enhanced / Core / Limited Scope]"
    dual_regulated: "[Yes — PRA prudential not assessed / No]"
    consumer_duty_applicable: "[Yes / No / Partial (closed book)]"
  assessment_scope: "[Full-scope / Specified modules only]"
  legalcode_mcp: "[Connected / Not connected]"
  handbook_reference_file: "[/tmp/fca-regulatory-baseline.md / Not created]"
  handbook_rules_consulted: "[number of specific rules reviewed]"
  rules_verified_against_current_handbook: "[number verified via fca.org.uk] / [number relying on training knowledge with [VERIFY] markers]"
  dear_ceo_letters_reviewed: "[List applicable Dear CEO letters by date and topic, or 'None — verify against current FCA publications']"
  recent_enforcement_actions_reviewed: "[number reviewed / sector]"
  findings_summary:
    compliant: "[number of areas]"
    partial: "[number of areas]"
    non_compliant: "[number of areas]"
    critical_exposure: "[number of areas]"
  self_interrogation_applied: "[Yes — all CRITICAL items / Not applicable (no CRITICAL items)]"
  board_escalation_recommended: "[Yes / No]"
  fca_self_disclosure_recommended: "[Yes — CRITICAL items present / No]"
  overall_confidence: "[HIGH / MEDIUM / LOW] — [Rationale: e.g., 'HIGH — core Handbook rules apply clearly; no emerging/contested rule interpretation areas']"
  limitations:
    - "[FCA Handbook currency: rules checked against knowledge base; verify current text at fca.org.uk/handbook]"
    - "[PRA prudential rules not assessed — dual-regulated firms require separate PRA assessment]"
    - "[Assessment based on information provided; additional undisclosed activities may affect findings]"
    - "[Self-disclosure considerations should be reviewed with qualified external FCA counsel]"
  reviewer: "AI-assisted — requires review by qualified FCA compliance solicitor or FCA-authorised compliance professional before use in FCA correspondence or board escalation"
```

---

## Anti-Patterns

What NOT to do when assessing FCA regulatory compliance. Every item on this list represents a
recurring mistake that leads to incomplete, misleading, or dangerous assessments.

1. **Reviewing SYSC without sector-specific modules** — SYSC sets the governance framework
   but the substantive conduct obligations are in the sector modules (COBS, ICOBS, MCOBS,
   CONC). Assessing only SYSC gives a misleadingly positive picture of compliance posture.

2. **Treating SM&CR as a one-time exercise** — SMCR is not a paper exercise at authorisation.
   Statements of Responsibility must be updated when responsibilities change; certifications
   must be renewed annually; Conduct Rules training must be refreshed. A firm that completed
   SMCR onboarding in 2020 and has not reviewed it since is likely NON-COMPLIANT.

3. **Ignoring Consumer Duty for firms in the distribution chain** — Consumer Duty applies to
   any firm in the distribution chain for retail products, not just the product manufacturer.
   A firm that believes Consumer Duty does not apply because it "doesn't deal directly with
   customers" may be incorrect if it is a distributor or intermediary.

4. **Confusing FCA and PRA rules for dual-regulated firms** — FCA conduct rules and PRA
   prudential rules are distinct. Applying IFPRU or CRR capital rules to an FCA-solo investment
   firm, or assuming MiFIDPRU applies to a PRA-regulated bank, produces incorrect findings.

5. **Treating best execution as a pricing exercise** — COBS 11 best execution requires analysis
   of multiple execution factors (price, costs, speed, likelihood of execution, settlement, size,
   nature of the order). A firm that focuses only on getting the best price while ignoring other
   factors breaches COBS 11. Best execution must be reviewed annually and applied systematically.

6. **Assuming absence of FCA enforcement = compliance** — Firms that have not been subject to
   FCA enforcement action may assume they are compliant. The FCA's supervisory resources are
   limited; the absence of enforcement is not evidence of compliance.

7. **Treating CASS as an accounting exercise** — CASS 7 requires daily reconciliation,
   proper segregation in protected accounts, and acknowledgement letters from banks.
   A firm that maintains correct accounting records but holds client money in a general
   current account (not a client bank account) has a CRITICAL CASS breach regardless of
   the accuracy of its records.

8. **Applying financial promotion rules only to advertising** — FSMA 2000 s.21 applies to all
   financial promotions in any medium, including social media posts, influencer content, email,
   and verbal promotions in the course of business. Firms that focus promotion compliance on
   brochures and ignore digital channels are systematically non-compliant.

9. **Assuming the FP Gateway does not apply** — Since February 2024, authorised firms that
   approve financial promotions for third parties (unauthorised persons) must have specific FCA
   permission to do so (the FP Gateway). Firms that were approving promotions before February
   2024 and have not obtained this permission are in breach of FSMA 2000 s.21.

10. **Ignoring "Dear CEO letters" as guidance only** — While Dear CEO letters are not FCA
    Handbook rules, they represent the FCA's supervisory expectations and frequently precede
    enforcement action. Firms that receive a Dear CEO letter and take no action are at
    significantly elevated enforcement risk.

11. **Reviewing complaints handling without checking FOS reporting** — DISP requires firms
    to submit half-yearly complaints data returns to the FCA via RegData. A firm with a
    functional internal complaints process that is not submitting these returns is in
    breach of DISP 1.10.

12. **Treating outsourcing agreements that reference "equivalent regulation" as SYSC 8 compliant**
    — SYSC 8 requires documented due diligence before outsourcing critical functions, not just a
    contractual reference to equivalent standards. If the due diligence has not been documented,
    the SYSC 8 obligation is not met.

13. **Assuming "not retail" means Consumer Duty does not apply** — Consumer Duty applies to
    a firm's retail customer-facing business. A firm that serves both retail and professional
    clients cannot ignore Consumer Duty for its retail client segment because the professional
    client segment is more prominent.

14. **Reviewing ICARA only at authorisation** — The Internal Capital Adequacy and Risk Assessment
    (ICARA) under MiFIDPRU must be conducted at least annually and updated whenever material
    changes occur to the firm's activities, business model, or risk profile. An ICARA from
    the firm's initial authorisation that has never been updated is not compliant.

15. **Assuming an MLRO annual report satisfies SYSC 6 AML obligations** — The MLRO annual
    report is one element of an AML programme. The programme also requires policies and
    procedures, a risk assessment, training, ongoing monitoring, and SAR procedures. An
    MLRO annual report without an underlying AML programme does not satisfy SYSC 6.

16. **Treating all financial promotion exemptions as self-certifying** — FPO exemptions
    (e.g., certified high net worth investor, certified sophisticated investor) require the
    investor to meet specific criteria and to self-certify correctly. Firms that distribute
    promotions on the basis of exemptions without verifying that investors qualify are
    in breach of s.21 FSMA 2000.

17. **Ignoring the closed-book Consumer Duty deadline** — The FCA extended Consumer Duty
    to closed-book products from 31 July 2024. Firms that completed Consumer Duty
    implementation for open products in July 2023 but have not reviewed their closed book
    since are NON-COMPLIANT.

18. **Reviewing SM&CR without checking criminal record disclosures** — The Fit and Proper
    assessment for SMFs and certified persons must include criminal record checks as part
    of the honesty and integrity assessment. Firms that conduct F&P assessments without
    criminal record disclosures are not meeting FIT Sourcebook requirements.

19. **Assuming regulatory reporting to RegData is functioning without checking** — RegData
    (formerly Gabriel) submission failures are a common source of FCA supervisory engagement.
    Confirm that the firm's reporting obligations are identified, that submissions are made
    on time, and that no submissions have lapsed following system changes or staff turnover.

20. **Assessing COBS suitability without checking suitability reports** — COBS 9 requires
    a suitability report to be provided in writing before or after every personal recommendation
    in relation to a relevant investment. Firms that assess suitability but do not produce
    suitability reports are in breach of COBS 9.5.2R, regardless of the quality of the
    underlying suitability assessment.

21. **Ignoring Operational Resilience self-assessment obligations** — The FCA's operational
    resilience framework (PS21/3, SS1/21) required firms to complete their self-assessments
    of important business services and impact tolerances by March 2025. Firms that have not
    completed the self-assessment are in breach of SYSC 15A.

22. **Treating Consumer Duty board report as a compliance department exercise** — The Consumer
    Duty board report must be reviewed and approved by the board. A compliance department
    report that has not been presented to the board and formally approved does not satisfy
    the PS22/9 requirement.

23. **Assuming CASS resolution packs are optional for smaller firms** — CASS resolution packs
    (CASS 10) are required for any firm subject to CASS (except CASS-RP1 small firms). A firm
    that believes it is too small to need a resolution pack should verify the applicable CASS
    category and whether the CASS resolution pack obligation applies.

24. **Reviewing AML/KYC without checking ongoing monitoring** — Customer due diligence at
    onboarding is only part of the AML obligation. MLR 2017 also requires ongoing monitoring
    of customers and transactions throughout the relationship. A firm with strong onboarding
    CDD but no ongoing monitoring programme has a material AML gap.

---

## Writing Standards

**For board-level and FCA correspondence outputs:**

- **Plain language**: Write for a non-specialist board member, not a regulatory lawyer.
  "The firm failed to verify beneficial ownership for 40% of corporate clients" is better
  than "Beneficial ownership verification deficiencies identified across a material proportion
  of the corporate client cohort."
- **Active voice**: "The Compliance Committee must approve the revised CDD procedures within
  30 days" — not "Revised CDD procedures must be approved."
- **Specific, not vague**: Cite the exact Handbook rule (e.g., "COBS 9.5.2R") — not
  "conduct of business requirements." Vagueness in regulatory correspondence creates risk.
- **Name the responsible person**: "The Chief Compliance Officer (SMF 16) must certify…"
  — not "Compliance must certify…"
- **One action per sentence**: Remediation actions should be single, unambiguous steps.
- **Calibrated confidence**: Do not assert FCA positions with more certainty than is warranted.
  Where the FCA's position is based on Guidance (G) or Dear CEO letters rather than binding
  Rules (R), say so.

**Quality gates before delivering output:**

1. Can a non-lawyer board member understand the executive summary in 5 minutes?
2. Can the Audit Committee identify which Handbook rule each finding relates to?
3. Is every CRITICAL EXPOSURE item supported by a specific, verifiable Handbook rule?
4. Are any sentences so technical or hedged as to obscure the action required?
5. Does the remediation roadmap name a responsible person and a timeline for every item?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Step 3: Search for current FCA Handbook text, Dear CEO letters, and Final Notices
- Step 6: Verify SM&CR requirements against current SYSC 2–4 and COCON Handbook text
- Step 7: Retrieve current Consumer Duty guidance (PS22/9 and FCA implementation updates)
- Step 10: Verify financial promotion rules against COBS 4 and FCA Guidance Note FG24/1
- Save all retrieved authority to `/tmp/fca-regulatory-baseline.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all specific FCA Handbook rule citations with [VERIFY against fca.org.uk/handbook]
- Note in Glass Box: `legalcode_mcp: "Not connected — FCA Handbook currency verification required"`
- Focus assessment on structural and programme quality; acknowledge that specific rule text
  has not been independently verified
- Recommend that the user verify currency of all Handbook citations before board presentation
  or FCA correspondence

---

## Localization Notes

This skill is specific to the UK FCA regulatory framework. To extend or adapt:

**PRA-regulated firms (banks, insurers):** Add PRA prudential assessment covering CRD/CRR
capital requirements, Internal Capital Adequacy Assessment Process (ICAAP), Individual
Liquidity Adequacy Assessment Process (ILAAP), stress testing, and PRA supervisory statements.

**Scotland and Northern Ireland:** Same FCA Handbook applies. Court proceedings in Scotland
use Court of Session; criminal prosecution in Scotland is by COPFS. Northern Ireland uses
PPS NI. Regulatory referrals follow the same FCA process.

**EU-nexus firms (post-Brexit):** UK firms operating in EU member states may require
authorisation under EU MiFID II, AIFMD, Solvency II, or other EU directives in addition
to FCA authorisation. This skill covers FCA/UK obligations only; EU obligations are separate.

**Appointed Representatives:** An AR's compliance obligations flow partly from its principal's
permissions and supervision obligations under FSMA 2000 s.39. The principal is responsible for
the AR's conduct. When assessing an AR, also assess the principal's AR oversight obligations.

---

## Output Format Template

```markdown
# FCA Regulatory Compliance Assessment

**Firm**: [Name and FRN]
**Assessment Type**: [Compliance Audit / Programme Build / Pre-Supervision / Enforcement Response / Acquisition Due Diligence / Targeted Review]
**Assessment Date**: [YYYY-MM-DD]
**FCA Handbook Modules Reviewed**: [PRIN, SYSC, COBS, CASS, DISP, etc.]
**SM&CR Scope**: [Enhanced / Core / Limited Scope]
**Dual Regulated**: [Yes — PRA prudential not assessed / No]

---

## Executive Summary

[1-page summary: Overall compliance posture, top 3 findings with severity classification,
recommended immediate actions, and overall confidence level in assessment.]

---

## Assessment Findings

### 1. FCA Authorisation and Permissions

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[Findings, evidence, and remediation for each element assessed]

---

### 2. SYSC — Systems and Controls

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

#### 2a. Senior Management Governance

[Finding | Rule | Classification | Confidence | Action]

#### 2b. Compliance Function

[Finding | Rule | Classification | Confidence | Action]

#### 2c. Risk Management

[Finding | Rule | Classification | Confidence | Action]

#### 2d. Internal Audit

[Finding | Rule | Classification | Confidence | Action]

#### 2e. Operational Resilience

[Finding | Rule | Classification | Confidence | Action]

---

### 3. SM&CR Assessment

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

#### 3a. Senior Manager Functions

[Assessment per SMF, including approval status and SoR]

#### 3b. Certification Regime

[Number certified, F&P assessment quality, criminal record check status]

#### 3c. Conduct Rules

[Training completion, breach recording, annual refresh]

---

### 4. Consumer Duty (Principle 12 / PS22/9)

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

#### 4a. Cross-Cutting Rules

[Good faith, foreseeable harm, financial objectives assessment]

#### 4b. Four Outcomes

[Products & Services | Price & Value | Consumer Understanding | Consumer Support]

#### 4c. Annual Board Report

[Status: Completed / In progress / Outstanding | Board approval status]

---

### 5. Conduct of Business [COBS / ICOBS / MCOBS / CONC]

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[Assessment per applicable module with findings and remediation]

---

### 6. Client Assets (CASS) [if applicable]

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[CASS 7 client money and CASS 6 custody assessment]

---

### 7. Financial Promotions

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[s.21 FSMA, FP Gateway, COBS 4, digital/social media assessment]

---

### 8. Prudential Requirements [MiFIDPRU / IFPR]

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[ICARA, own funds, liquidity, wind-down plan, RegData reporting]

---

### 9. Financial Crime Controls

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[AML programme, MLRO, CDD, sanctions, SAR obligations]

---

### 10. Complaints Handling (DISP)

**Overall**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]
**Confidence**: [Definite / High / Probable / Possible]

[Identification, acknowledgement, investigation, FOS referral, regulatory reporting]

---

## Prioritised Remediation Roadmap

| Finding   | Handbook Rule | Classification    | Priority  | Timeline | Owner                | Success Metric                                                                 |
| --------- | ------------- | ----------------- | --------- | -------- | -------------------- | ------------------------------------------------------------------------------ |
| [Finding] | [COBS 9.5.2R] | NON-COMPLIANT     | IMMEDIATE | 30 days  | CCO                  | Suitability reports in place for all advised clients; documented review        |
| [Finding] | [CASS 7.13]   | CRITICAL EXPOSURE | IMMEDIATE | 14 days  | Finance + Compliance | Client money segregated; acknowledgement letters obtained; FCA notified        |
| [Finding] | [PS22/9]      | PARTIAL           | NEAR-TERM | 60 days  | CCO + Board          | Consumer Duty board report approved; four outcomes documented                  |
| [Finding] | [SYSC 27.2]   | PARTIAL           | NEAR-TERM | 90 days  | HR + Compliance      | All certified persons re-certified; F&P records updated                        |
| [Finding] | [SYSC 15A]    | PARTIAL           | NEAR-TERM | 90 days  | COO                  | Operational resilience self-assessment completed; impact tolerances documented |

---

## FCA Regulatory Watchpoints

| Recent FCA Development                            | Date            | Impact on This Firm                                                   |
| ------------------------------------------------- | --------------- | --------------------------------------------------------------------- |
| Consumer Duty closed-book extension               | 31 July 2024    | Closed-book products must now be included in Consumer Duty assessment |
| FP Approval Gateway                               | 7 February 2024 | Third-party promotion approval requires specific FCA permission       |
| Operational resilience self-assessment deadline   | March 2025      | Self-assessment of IBS and impact tolerances required                 |
| [Any Dear CEO letters relevant to this firm type] | [Date]          | [Specific expectation]                                                |

---

## Board Governance Recommendations

1. [Specific board action, e.g., "Establish a quarterly FCA regulatory compliance dashboard
   presented at board level"]
2. [SMCR, e.g., "Require annual board review and approval of all SMF Statements of Responsibility"]
3. [Consumer Duty, e.g., "Formally adopt and approve the Consumer Duty board report at the next
   board meeting; delegate action tracking to the Audit Committee"]
4. [External audit, e.g., "Commission an independent external CASS audit before the next
   financial year-end"]

---

## Limitations

- This assessment is AI-assisted and requires review by a qualified FCA compliance solicitor
  or FCA-authorised compliance professional before use in FCA correspondence or board materials
- FCA Handbook rules verified against knowledge base; verify current text at fca.org.uk/handbook
  before relying on specific rule citations
- PRA prudential obligations (for dual-regulated firms) are not assessed — a separate PRA
  assessment is required
- Assessment is based on information provided; undisclosed activities may affect findings
- Self-disclosure recommendations require advice from qualified external FCA counsel

---

## Glass Box Audit Trail

[Insert YAML audit trail here — see Glass Box Audit Trail section above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis covering the full FCA regulatory
compliance framework under FSMA 2000, the FCA Handbook, and current FCA supervisory priorities.
Research conducted via:

- Agent 1 (Structural/Legal Research): Deep research on FCA Handbook modules, FSMA 2000
  provisions, SM&CR, Consumer Duty PS22/9, COBS, CASS, MIFIDPRU/IFPR, financial promotions
  (FP Gateway PS23/13), and FCA enforcement landscape
- Agent 2 (Prompt Engineering/Quality): Structural analysis of legalcode-contract-review
  reference standard and legalcode-uk-bribery-act-compliance for patterns; blueprint design
  for 12-step workflow, classification system, quality frameworks, and output template
- Repository context: legalcode-uk-bribery-act-compliance (CRITICAL DEFICIENCY pattern
  adapted), legalcode-contract-review (Citation Quality Gates, Self-Interrogation, Confidence
  Scoring, Glass Box adapted for regulatory context)

Legal references verified against knowledge base as of March 2026. All Handbook citations
marked [VERIFY] where currency is uncertain. Verify against current FCA Handbook at
fca.org.uk/handbook before use.
