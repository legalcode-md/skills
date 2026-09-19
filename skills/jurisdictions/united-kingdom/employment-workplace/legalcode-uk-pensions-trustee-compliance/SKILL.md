---
name: legalcode-uk-pensions-trustee-compliance
description: 'Assess UK occupational pension scheme trustee compliance across all core regulatory obligations:
  trustee duties and governance under the Pensions Act 1995 and 2004, trustee knowledge and understanding
  (TKU) requirements, member-nominated trustee (MNT) elections, auto-enrolment obligations under the Pensions
  Act 2008, DB funding and actuarial requirements under the Pension Schemes Act 2021 and the 2024 DB Funding
  Code, TPR General Code of Practice (March 2024), ESG/TCFD climate risk reporting under the Occupational
  Pension Schemes (Climate Change Governance and Reporting) Regulations 2021, GMP equalisation obligations
  post-Barber [1990], transfer value regime under the Pension Schemes Act 2021 (red/amber/green flag),
  pensions dashboards connection obligations, IDRP dispute resolution, data protection under UK GDPR,
  and member disclosure requirements under the Disclosure of Information Regulations 2013.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess UK occupational pension scheme trustee compliance across all core regulatory obligations: trustee duties and governance under the Pensions Act 1995 and 2004, trustee knowledge and understanding (TKU) requirements, member-nominated trustee (MNT) elections, auto-enrolment obligations under the Pensions Act 2008, DB funding and actuarial requirements under the Pension Schemes Act 2021 and the 2024 DB Funding Code, TPR General Code of Practice (March 2024), ESG/TCFD climate risk reporting under the Occupational Pension Schemes (Climate Change Governance and Reporting) Regulations 2021, GMP equalisation obligations post-Barber [1990], transfer value regime under the Pension Schemes Act 2021 (red/amber/green flag), pensions dashboards connection obligations, IDRP dispute resolution, data protection under UK GDPR, and member disclosure requirements under the Disclosure of Information Regulations 2013. Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE gap analysis with a prioritised remediation roadmap, governance document templates, and a Glass Box audit trail suitable for TPR correspondence. Use when advising trustees, pensions managers, sponsoring employers, pension committees, or professional trustees on scheme governance and regulatory risk. Applies to occupational pension schemes in England and Wales (both DB and DC).


# Legalcode UK Pensions Trustee Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted pensions trustee compliance
> assessment. It does not constitute legal advice. All outputs should be reviewed by a qualified
> pensions solicitor or adviser licensed to practise in England and Wales before use. Pensions
> law is complex, frequently amended, and scheme-specific — provisions that apply to one scheme
> type may not apply to another. Statutory and case law references cited from research carry
> hallucination risk; verify against authoritative sources (legislation.gov.uk, TPR website,
> The Pensions Ombudsman decisions) before relying on them.

---

## Purpose and Scope

This skill assesses occupational pension scheme trustee compliance against regulatory obligations
in England and Wales. It identifies compliance gaps, classifies their severity, generates
actionable remediation recommendations, and produces an auditable analysis with a Glass Box
audit trail.

**Covers:**

- Trustee duties, governance, and conflicts of interest
- Trustee knowledge and understanding (TKU) under PA 2004 ss.247–249
- Member-nominated trustee (MNT) elections under PA 1995 ss.16–21
- Auto-enrolment compliance under the Pensions Act 2008
- DB funding, actuarial valuations, and recovery plans under PA 2004 ss.224–227 and the 2024 DB Funding Code
- TPR General Code of Practice (in force March 2024) own risk assessments
- ESG reporting and TCFD climate risk governance under the 2021 Regulations
- GMP equalisation obligations
- Transfer value compliance under PSA 2021 (red/amber/green flag regime)
- Pensions dashboards connection obligations
- Internal Dispute Resolution Procedure (IDRP) under PA 1995 s.50
- Data protection and UK GDPR for pension scheme administrators
- Member communications and disclosure under the Disclosure of Information Regulations 2013

**Does not:**

- Advise on individual member benefit entitlements or pension calculations
- Assess HMRC registration, relief at source, or tax treatment of pension contributions in depth (flag for specialist tax advice)
- Cover personal pension schemes (SIPPs, stakeholder pensions) or public sector schemes
- Apply to occupational pension schemes governed by Scottish law without adaptation
- Constitute legal advice or replace qualified pensions counsel

**When to use this skill:**

- Trustee governance audit (annual or triggered by change of trustee board composition)
- Scheme risk assessment (pre-valuation, post-regulatory development)
- New trustee onboarding (identify TKU gaps and governance deficiencies)
- Sponsoring employer covenant assessment integration (alongside DB funding review)
- Pre-TPR engagement preparation
- Preparation for scheme merger, buyout, or wind-up

---

## Jurisdiction and Governing Law

**Jurisdiction**: England and Wales. Primary regulatory framework:

- Pensions Act 1995 (PA 1995)
- Pensions Act 2004 (PA 2004)
- Pension Schemes Act 2021 (PSA 2021)
- Pensions Act 2008 (PA 2008) — auto-enrolment
- Occupational Pension Schemes (Investment) Regulations 2005 (SI 2005/3377)
- Occupational Pension Schemes (Disclosure of Information) Regulations 2013 (SI 2013/2734)
- Occupational Pension Schemes (Climate Change Governance and Reporting) Regulations 2021 (SI 2021/839)
- Occupational Pension Schemes (Scheme Administration) Regulations 1996 (SI 1996/1715)
- The Pensions Regulator's General Code of Practice (in force 28 March 2024)
- PPF (Pension Protection Fund) Regulations 2005 and related legislation
- UK GDPR and Data Protection Act 2018

**Key regulatory bodies:**

- The Pensions Regulator (TPR) — primary occupational pensions regulator
- The Pensions Ombudsman (PO) — complaint resolution
- HM Revenue and Customs (HMRC) — tax regime
- Financial Conduct Authority (FCA) — DC investment regulation, pensions dashboards ISPs

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer changes which regulatory requirements apply to the scheme
- Multiple valid approaches exist and scheme-specific context determines which applies
- Scope decisions affect whether to flag an issue or treat it as not applicable
- TPR regulatory posture or enforcement risk depends on scheme-specific facts

Use the ⟁ **CLARIFY** convention throughout. Present structured options where possible and
state why the answer matters. If the user has already provided the information, skip the
question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept trustee compliance assessment input in any of these formats:

- **Scheme documents**: Trust deed and rules, SIP, Chair's Statement, actuarial valuation report,
  TCFD report, transfer value analysis, pensions dashboards connection statement
- **Audit questionnaire responses**: Trustee self-assessment completed by the trustee board
- **Narrative description**: User describes the scheme, its current governance arrangements,
  and areas of concern
- **Specific issue flagged**: User identifies a specific compliance risk (e.g., "our GMP
  equalisation project is stalled") for targeted analysis

### Step 2: Gather Scheme Context

⟁ **CLARIFY** — Before beginning, ask the user these questions. Skip questions already answered:

1. **Scheme type**:
   - Options: Defined Benefit (DB) only, Defined Contribution (DC) only, Hybrid (DB and DC
     sections), Career Average Revalued Earnings (CARE), Cash Balance, Collective Defined
     Contribution (CDC — post PSA 2021)
   - _Why this matters_: Different regulatory regimes apply. DB schemes have funding code,
     actuary, and employer covenant obligations not applicable to DC. DC schemes have chair's
     statement and value-for-money requirements. CDC is a new regime with specific requirements.

2. **Scheme size (total assets)**:
   - Options: Under £100m, £100m–£1bn, £1bn–£5bn, Over £5bn
   - _Why this matters_: TCFD/ESG reporting thresholds, certain TPR Code obligations, and
     PPF levy bands vary by size. TCFD mandatory reporting applies from £1bn (full TCFD from
     £5bn+). Some TPR Code Own Risk Assessment obligations scale by size.

3. **Trustee board composition**:
   - Options: Lay trustees only, Professional trustee board, Corporate trustee (sole professional),
     Mixed (lay + professional), Employer-only nominated (no MNT elections yet conducted)
   - _Why this matters_: MNT election obligations and TKU requirements differ. Corporate sole
     trustee structures trigger specific TPR Code requirements. Lay trustees require more
     training support.

4. **DB funding status** (if DB or hybrid):
   - Options: In surplus (fast track eligible), In deficit with recovery plan in place,
     In deficit with recovery plan not in place / lapsed, Scheme closed to accrual, Scheme
     in PPF assessment period, Not applicable (DC only)
   - _Why this matters_: DB funding code compliance path (Fast Track vs. Bespoke), recovery
     plan obligations, and TPR enforcement risk all depend on funding status.

5. **Assessment scope**:
   - Options: Full governance audit (all 13 assessment areas), Priority areas only (specify),
     Specific issue investigation (describe), Pre-valuation readiness (DB funding focus),
     Pre-TPR engagement preparation, New trustee onboarding
   - _Why this matters_: Determines depth of review and which assessment areas to prioritise.

6. **Known concerns or recent events**:
   - Free text. Prompt: "Any recent regulatory changes, trustee board changes, employer
     covenant events, member complaints, or TPR correspondence worth flagging?"
   - _Why this matters_: Focuses the assessment on the issues most likely to drive
     non-compliance risk.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly (e.g., "I'm assuming this is a DB scheme with assets under £1bn — let me know
if that's wrong").

### Step 3: Load Regulatory Baseline

Use **legalcode-mcp** to retrieve current regulatory requirements for the scheme type
and size identified in Step 2.

**Search priorities:**

1. TPR General Code of Practice — current version (in force March 2024)
2. TPR DB Funding Code — current version (in force 2024)
3. DWP / TPR guidance on TCFD/ESG for applicable asset threshold
4. PSA 2021 transfer value provisions and TPR transfer guidance
5. Pensions Dashboards Programme staging schedule — current dates (check for updates)
6. TPR enforcement data and recent fines for calibrating severity classifications
7. Recent TPR Annual Funding Statements and DB funding outlook

Save the most relevant results to `/tmp/legalcode-pensions-baseline.md`:

```markdown
# Pensions Regulatory Baseline — [Scheme Name]

## Date: [date]

## Scheme Type: [DB/DC/Hybrid]

## Asset Size: [band]

### Applicable Statutory Framework

- [Act, section, current requirement]

### TPR Code Requirements (March 2024 Code)

- [Module, requirement, applicable to this scheme type/size]

### DB Funding Code Requirements (if applicable)

- [Fast Track / Bespoke threshold, funding requirement]

### TCFD/ESG Requirements (if applicable)

- [Applicable threshold, reporting requirements, deadlines]

### Pensions Dashboards Connection Deadline

- [Current staging deadline for this scheme size]

### Recent TPR Enforcement / Guidance

- [Relevant enforcement action, Dear Trustee letter, regulatory statement]
```

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using research-based knowledge of the current regulatory framework
- Recommend independent verification before any trustee board action

### Step 4: Classify Scheme Regulatory Profile

Before beginning the assessment, classify the scheme's regulatory obligations matrix:

| Area                | Applicable?                          | Specific Requirements                    | Key Deadlines                          |
| ------------------- | ------------------------------------ | ---------------------------------------- | -------------------------------------- |
| DB Funding Code     | DB / Hybrid only                     | Fast Track or Bespoke; FIS required      | Next valuation date                    |
| TCFD Reporting      | £1bn+                                | Full (£5bn+) or partial (£1bn–£5bn)      | Annual: 7 months after scheme year end |
| Auto-Enrolment      | All schemes with eligible jobholders | Ongoing re-enrolment every 3 years       | Next re-enrolment date                 |
| Pensions Dashboards | Staging applies                      | Connection by deadline                   | [Check current PDP staging dates]      |
| GMP Equalisation    | Pre-1997 DB with GMP liabilities     | Equalisation method, data remediation    | No fixed deadline — ongoing            |
| PSA 2021 Transfers  | All schemes with transfer rights     | Red/amber/green flag system              | Immediate — already in force           |
| TPR General Code    | All occupational schemes             | Own Risk Assessment (ORA)                | Annual ORA recommended                 |
| IDRP                | All occupational schemes             | Written internal procedure               | Immediate if not in place              |
| TKU                 | All trustees                         | Annual assessment, 6-year training cycle | Ongoing                                |
| MNT                 | 2+ members                           | Election cycle, 3–6 year term            | Per trust deed / PA 1995 ss.16–21      |

⟁ **CLARIFY** — If scheme type or size is unclear, or if the trust deed contains unusual
provisions affecting regulatory classification, ask the user before proceeding.

### Step 5: Conduct 13-Area Trustee Compliance Assessment

Assess the scheme systematically across all 13 areas. Read all available documents before
flagging issues — obligations interact (e.g., a lapsed SIP affects both the investment
framework and the TCFD requirement).

⟁ **CLARIFY** — For a full audit (all 13 areas) vs. a targeted review (specific areas),
confirm scope before proceeding. For targeted reviews, state which areas are out of scope.

#### Area 1 — Trustee Duties and Governance

**Statutory framework**: PA 1995 s.33 (duty of care, investment functions); PA 2004 s.241
(general code duty to act in members' interests); Trustee Act 2000 (duty of care, delegation,
investment powers); TPR General Code of Practice (March 2024) — Module: Governing body.

**Assess:**

- Is there a written scheme governance framework or trustee handbook?
- Does the trustee board meet at least quarterly (TPR Code expectation)?
- Are trustee decisions recorded in minutes with sufficient detail to evidence reasoning?
- Does each trustee understand their fiduciary duty to act in members' best interests?
- Are there any trustees disqualified under PA 1995 s.29 (bankruptcy, criminal conviction,
  disqualification order)?
- Is the trustee board of appropriate size (TPR Code: minimum 3, recommended 5–7)?
- Has the board conducted an own risk assessment (ORA) as recommended by the TPR Code?
- Are conflicts of interest managed with a written policy (TPR Code requirement)?

**Common non-compliance failures:**

- Minutes that record conclusions without reasoning, making decisions unchallengeable by TPR
- Corporate trustee boards with only employer-nominated directors and no member voice
- ORA not completed since the March 2024 Code took effect
- No written conflicts policy or policy that predates the March 2024 Code requirements

#### Area 2 — Trustee Knowledge and Understanding (TKU)

**Statutory framework**: PA 2004 ss.247–249; Occupational Pension Schemes (Trustees'
Knowledge and Understanding) Regulations 2006 (SI 2006/686); TPR Code — Module: Trustee
knowledge and understanding.

**Assess:**

- Has each trustee completed a TKU assessment within the last 6 years?
- Is a log of individual trustee TKU assessments and training maintained?
- Does trustee knowledge cover: trust law, pensions law, investments, scheme funding, and
  administration?
- Are there documented plans to address TKU gaps?
- Has new trustee onboarding been completed within 6 months of appointment?
- For professional trustees: does the individual meet the Professional Trustee Standards
  (accreditation requirement from the Accreditation Body from 2023)?

**Professional trustee accreditation (from 2023):**

- Professional trustees must be accredited by an approved accreditation body (PASA
  Accreditation Board or equivalent). Non-accredited professional trustees serving from
  October 2025 carry increasing regulatory and professional risk [VERIFY current deadline].

#### Area 3 — Member-Nominated Trustees (MNT)

**Statutory framework**: PA 1995 ss.16–21 (as amended); Occupational Pension Schemes
(Member-nominated Trustees and Directors) Regulations 2006 (SI 2006/714).

**Assess:**

- Does the trustee board include at least one-third member-nominated trustees (or MND for
  corporate trustees)?
- Have MNT elections been conducted in compliance with the statutory process?
- Is the MNT term within 3–6 years (or as specified in the trust deed)?
- Are MNT vacancies being filled within a reasonable period?
- Has the employer exercised any improper influence over MNT elections?

**Common non-compliance failures:**

- Schemes where MNT elections were run but members were "selected" rather than properly
  elected by member vote
- MNT terms rolling over without re-election beyond the maximum permitted period

#### Area 4 — Auto-Enrolment Compliance

**Statutory framework**: Pensions Act 2008; the Automatic Enrolment (Miscellaneous Amendments)
Regulations 2012 and subsequent amending regulations; Workplace Pensions Regulations (various).

**Current thresholds (2025/26)** [VERIFY with DWP/TPR for current year]:

- Earnings trigger: £10,000 per year (worker must be enrolled if earnings exceed this)
- Lower qualifying earnings (QEL): £6,240 per year
- Upper qualifying earnings (QEU): £50,270 per year
- Qualifying earnings = pay between QEL and QEU

**Minimum contribution rates (DC auto-enrolment):**

- Employer minimum: 3% of qualifying earnings
- Worker minimum: 5% of qualifying earnings (total minimum 8%)

**Assess:**

- Are all eligible jobholders being enrolled at the correct point (first day of eligibility)?
- Are qualifying earnings calculated correctly across pay reference periods?
- Is the re-enrolment cycle being operated every 3 years (within a 6-month window around
  the 3rd anniversary of the employer's staging date)?
- Are opt-out requests being processed within the statutory 1-month window?
- Are postponement periods being applied correctly (maximum 3 months)?
- Are contribution rates meeting minimum thresholds?
- Is the scheme a qualifying scheme (benefit test or contribution test passed)?
- Are records maintained per the TPR record-keeping guidance?

**Common non-compliance failures:**

- Incorrect earnings period for contribution calculation (using weekly pay annualised
  incorrectly)
- Missing re-enrolment (3-year cycle overlooked)
- Opt-outs not processed within 1 month, leading to over-contribution refund obligations
- Postponement periods not properly communicated to workers in writing

#### Area 5 — DB Funding and Actuarial Requirements

**Statutory framework**: PA 2004 ss.221–233 (scheme funding); Occupational Pension Schemes
(Scheme Funding) Regulations 2005 (SI 2005/3377); TPR DB Funding Code of Practice (2024).

**Two compliance routes under the 2024 Code:**

**Fast Track** (for well-funded schemes):

- Technical provisions: assumptions must meet Fast Track parameters
- Recovery plan: maximum 6 years from effective date if in deficit (reduced from 10 years)
- Funding and Investment Strategy (FIS): must demonstrate journey plan to low dependency
- Low Dependency Investment Allocation (LDIA): by significant maturity (typically 20 years
  to full funding)
- Employer covenant: must be classified as Strong

**Bespoke route**:

- Actuarial certification of compliance with the scheme-specific funding standard
- Must demonstrate equivalent or better outcome than Fast Track
- Integrated risk management (IRM) required
- TPR may scrutinise bespoke valuations more heavily post-2024 Code

**Assess (DB schemes):**

- Has a triennial actuarial valuation been completed within the statutory 15-month deadline
  (PA 2004 s.224)?
- Is a Statement of Funding Principles (SFP) in place and current?
- Is a Funding and Investment Strategy (FIS) in place (new requirement under 2024 Code)?
- If in deficit, is a recovery plan in place and being implemented?
- Are schedule of contributions payments being made on time?
- Is the employer covenant being monitored (at least annually, with formal assessment at
  valuation)?
- Has the actuary provided a s.228 certificate (Chair of Trustees certification if applicable)?
- Have any events triggering a s.75 debt occurred (employer insolvency, employment of last
  active member)?

⟁ **CLARIFY** — If the valuation is more than 15 months old, ask whether the trustees
have engaged with the actuary on timing, or whether there are known reasons for delay.

#### Area 6 — TPR General Code of Practice (March 2024)

**Framework**: TPR General Code of Practice (in force 28 March 2024), consolidating 10
previous codes into a single framework covering all occupational schemes.

**Key modules applicable to all schemes:**

- **Governing body**: Trustee numbers, skills, meetings, decision-making, records
- **Conflicts of interest**: Written policy, register of interests, managing conflicts
- **Own Risk Assessment (ORA)**: Annual written assessment of effectiveness of risk
  management systems (TPR Code requirement for all schemes)
- **Scheme administration**: Records, data quality, administration standards
- **Advisers and service providers**: Selection, appointment, ongoing oversight of
  professional advisers
- **Managing conflicts of interest**: Policy, register, individual declarations

**Assess:**

- Has an Own Risk Assessment been conducted and documented since March 2024?
- Is there a conflicts of interest policy (compliant with March 2024 Code Module)?
- Is there a register of trustee interests?
- Does the scheme have a documented scheme administration policy?
- Are professional advisers reviewed at least every 3 years (TPR Code expectation)?
- Is there a cyber security policy and incident response plan (TPR Code — cyber module)?

#### Area 7 — ESG and TCFD Climate Risk Governance

**Statutory framework**: Occupational Pension Schemes (Climate Change Governance and Reporting)
Regulations 2021 (SI 2021/839); DWP Statutory Guidance on governance and reporting of climate
change risk; Occupational Pension Schemes (Investment) Regulations 2005 reg.2 (SIP requirements).

**Mandatory reporting thresholds** (by relevant assets):

- **Full TCFD reporting**: Schemes with relevant assets of £5bn+ — in force from 1 October 2021 (reporting from 2022)
- **TCFD reporting (extended)**: Schemes with relevant assets of £1bn–£5bn — in force from 1 October 2022 (reporting from 2023)
- **ESG SIP requirements**: All schemes — Statement of Investment Principles must include ESG policy

**TCFD four pillars (for applicable schemes):**

- **Governance**: Board oversight of climate risk; management role
- **Strategy**: Actual and potential climate risk impacts; scenario analysis
- **Risk Management**: Process for identifying, assessing, managing climate risks
- **Metrics and Targets**: Climate metrics (emissions data); targets set against metrics

**SIP ESG requirements (all schemes):**

- Written policy on financially material ESG considerations
- Policy on stewardship (engagement, voting)
- Non-financial factors policy (if applicable)
- Annual review and update

**Assess:**

- Is the SIP current and does it include an ESG policy?
- For applicable schemes: has a TCFD report been published within 7 months of scheme year end?
- Does the TCFD report cover all four TCFD pillars?
- Has scenario analysis been conducted (at least 2 climate scenarios, including one 1.5°C)?
- Are climate metrics (including at least one Scope 1 and 2 metric) being collected?
- Are targets set and being tracked?
- Is the TCFD report publicly available on a website free to access?
- Are investment managers providing climate data as required by the SIP?

#### Area 8 — GMP Equalisation

**Legal basis**: Barber v Guardian Royal Exchange Assurance Group [1990] ECJ (C-262/88)
— equal pay obligations applied to occupational pension scheme benefits from 17 May 1990.
Pre-Barber GMP benefits (accrued before 17 May 1990) are outside the equalisation requirement
for pension purposes, but GMPs must still be equalised for the period 17 May 1990 to 5 April
1997 (when GMP accrual ended).

**Equalisation methods:**

- **Method C2** (Conversion with Blending — preferred by TPR): Converts GMP into scheme
  pension on a gender-neutral actuarial basis; eliminates future GMP complexity
- **Method D** (Dual record keeping): Pays the higher of the member's own GMP or opposite
  sex GMP at each payment date; operationally complex
- **Method B**: Retrospective recalculation — actuarially complex
- **Method A**: Not recommended (ignores anti-franking)
- TPR and industry guidance (November 2020 joint industry guidance) recommends C2 or D

**Assess:**

- Has the scheme identified its GMP equalisation obligation?
- Has a GMP equalisation project been commenced?
- Has a GMP equalisation method been selected and documented?
- Have top-up payments to underpaid members been calculated and communicated?
- Are deceased members' estates and beneficiaries identified for retrospective uplift?
- Has the actuary signed off the equalisation methodology?
- Have the scheme rules been amended to reflect the equalisation (if using Method C2)?
- Is data remediation (GMP reconciliation with HMRC) complete?

**Common failures:**

- Schemes that acknowledged the Barber obligation in 1990 but have taken no formal
  equalisation steps since then — all are in breach of equal pay law
- GMP data not reconciled with HMRC, making equalisation impossible to calculate

#### Area 9 — Transfer Values

**Statutory framework**: PA 1995 ss.93–101 (statutory transfer rights); PSA 2021 ss.125–127
(transfer red/amber/green flag regime — in force from 30 November 2021); Occupational and
Personal Pension Schemes (Transfer Values) Regulations 1996 (as amended).

**Red/amber/green flag regime (PSA 2021):**

- **Red flag**: Automatic block on transfer — e.g., member has received unsolicited third-party
  financial advice, overseas transfer (unless registered abroad with HMRC), employer financial
  incentive, transfer value exceeds statutory ceiling without actuary's confirmation
- **Amber flag**: Transfer must be paused; member must take MoneyHelper guidance before
  proceeding — e.g., high transfer value (DB schemes), unclear or unusual destination scheme,
  any concerns about receiving scheme
- **Green flag**: Transfer can proceed normally

**For DB transfers specifically:**

- No transfer without Appropriate Independent Advice (AIA) if transfer value exceeds £30,000
- Trustees must check AIA has been received before making a DB-to-DC transfer
- Suspension powers: trustees can suspend transfers if the scheme funding level is at risk
  or employer is under financial stress (PA 2004 s.95)

**Assess:**

- Is the transfer value process (including flag checks) documented and implemented?
- Are statutory transfer requests being acknowledged within 3 months of request?
- Is the Discharge Notice being provided before transfer?
- Are flag checks being conducted for every transfer?
- For DB transfers: are AIA checks completed and documented?
- Is there a defined process for handling amber flags (directing to MoneyHelper)?
- Are transfer value assumptions actuarially certified (DB)?
- Is there a transfer suspension policy and have trustees considered whether suspension
  is appropriate given current scheme funding?

#### Area 10 — Pensions Dashboards

**Statutory framework**: Pension Schemes Act 2021 ss.238–240; Pensions Dashboards
Regulations 2022 (SI 2022/1220); PDP (Pensions Dashboards Programme) staging deadlines.

**Connection requirements:**

- Schemes must connect to the pensions dashboards ecosystem by their staging deadline
- Staging deadlines are set by scheme size (number of relevant members):
  - Largest schemes (>10,000 members): Earliest staging — [VERIFY current schedule from PDP website; deadlines have been revised]
  - Smaller schemes: Later staging dates — [VERIFY from PDP website]
- Once connected, schemes must respond to pensions dashboards finds requests within
  the required response timescales

**Data quality requirements:**

- Pension Identifier (PeI): must match HMRC records for each member
- Annual Benefit Statement (ABS) data must be current
- Deferred/preserved benefit data must be accurate

**Assess:**

- Is the scheme's staging deadline known?
- Has the scheme appointed an ISP (Integrated Service Provider) for connection?
- Is data quality remediation underway (Pension Identifier matching)?
- Is there a project plan in place for dashboards connection?
- Has the trustee board received a dashboards project update?

⟁ **CLARIFY** — If the staging deadline is unknown or the user believes the scheme has
been exempted, ask for clarification before classifying compliance.

#### Area 11 — Data Protection and UK GDPR

**Statutory framework**: UK General Data Protection Regulation (UK GDPR); Data Protection
Act 2018; ICO Guidance on data protection for pension schemes.

**Assess:**

- Is the scheme registered with the ICO as a data controller?
- Is there a current Privacy Notice for scheme members?
- Is there a Records Retention Policy covering pension scheme data?
- Are data subject access requests (DSARs) being handled within 30 days?
- Are data breach incidents reported to the ICO within 72 hours (if required)?
- Is member data stored securely (encryption, access controls)?
- Are data processing agreements in place with all third-party administrators?

#### Area 12 — Member Communications and Disclosure

**Statutory framework**: Occupational Pension Schemes (Disclosure of Information)
Regulations 2013 (SI 2013/2734); Occupational Pension Schemes (Charges and Governance)
Regulations 2015 (DC schemes — Chair's Statement); Occupational Pension Schemes (Annual
Member Meeting) Regulations (as applicable).

**Key annual disclosure requirements:**

| Document                                      | Applicable Schemes                   | Frequency                   | Key Content                                                                                                         |
| --------------------------------------------- | ------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Chair's Statement                             | DC (including DC sections of hybrid) | Annual                      | 6 areas: default strategy, investment returns, charges, member engagement, advisers, illustrative retirement income |
| Annual Benefit Statements                     | DC — Defined contribution            | Annual                      | Projected retirement income, contribution history, transfer value                                                   |
| Summary Funding Statement                     | DB                                   | Annual (between valuations) | Funding level, changes, PPF levy                                                                                    |
| Statutory Money Purchase Illustrations (SMPI) | DC and hybrid DC                     | Annual                      | Retirement income projection                                                                                        |
| Statutory Funding Objective (SFO) — updates   | DB                                   | As required                 | Funding changes, deficits                                                                                           |

**Assess (DC schemes):**

- Is the Chair's Statement produced and approved by the trustee board annually?
- Does the Chair's Statement cover all 6 statutory areas?
- Are Annual Benefit Statements sent within 3 months of the scheme year end?
- Are SMPI projections using current assumptions (DWP prescribed rates)?
- Are default fund reviews conducted at least every 3 years (DC governance requirement)?

**Assess (DB schemes):**

- Is a Summary Funding Statement sent to members annually?
- Are individual benefit statements available on request?
- Are scheme accounts audited within 7 months of the scheme year end?

#### Area 13 — IDRP and Dispute Resolution

**Statutory framework**: PA 1995 s.50/s.50B; Occupational Pension Schemes (Internal
Dispute Resolution Procedures Consequential and Miscellaneous Amendments) Regulations 2008.

**Assess:**

- Is there a written IDRP procedure?
- Does the IDRP provide for a two-stage process?
- Are members notified of the IDRP in their member booklet and annual statements?
- Are IDRP decisions made within the required timeframes (Stage 1: 2 months; Stage 2: at
  trustee's reasonable discretion)?
- Are members advised of their right to escalate to The Pensions Ombudsman?
- Are IDRP decisions communicated in writing?

### Step 6: Identify Missing or Lapsed Obligations

After assessing present documentation, check for obligations that are entirely absent:

- No SIP (or SIP more than 3 years old without review): **NON-COMPLIANT**
- No IDRP: **NON-COMPLIANT**
- No written conflicts of interest policy: **NON-COMPLIANT** (post March 2024 Code)
- No TKU records for any trustee: **NON-COMPLIANT**
- DB scheme with no actuarial valuation in more than 3 years and 3 months: **NON-COMPLIANT** / **CRITICAL EXPOSURE**
- No auto-enrolment re-enrolment conducted within last 3 years + 6 months: **NON-COMPLIANT**
- GMP equalisation not commenced for pre-1997 DB with GMP: **NON-COMPLIANT** (Barber obligation dates from 1990)
- Pensions dashboards staging deadline passed without connection: **NON-COMPLIANT** / **CRITICAL EXPOSURE**

⟁ **CLARIFY** — When a missing obligation might be explained by scheme type or an exemption
the user hasn't mentioned (e.g., "the scheme has no GMP because it never contracted out"),
ask before flagging.

### Step 7: Classify Each Finding

Apply the four-tier severity system:

**COMPLIANT** — Green

- Trustee meets or exceeds the regulatory standard
- Documentation is in place, current, and reviewed
- No material risk of TPR enforcement
- _Action_: Note for awareness; include in ongoing monitoring; no immediate action required

**PARTIAL** — Amber

- Broadly compliant but with identifiable gaps
- Documentation exists but is outdated, incomplete, or not consistently applied
- Non-material breach may have occurred but is remediable without escalation
- _Action_: Generate specific remediation steps; assign NEAR-TERM timeline (30–90 days);
  note regulatory risk if left unaddressed

**NON-COMPLIANT** — Red

- Materially falls short of statutory or TPR Code requirements
- Breach of a regulatory duty is present or imminent
- _Action_: Escalate to trustee board immediately; identify specific statutory breach; provide
  standard remediation approach; recommend IMMEDIATE timeline (0–30 days); consider whether
  TPR should be notified

**CRITICAL EXPOSURE** — Red (Escalate Immediately)

- Serious, ongoing, or systemic breach of core pensions law
- TPR investigation, enforcement action, or prosecution is a real risk absent immediate action
- Member harm may be occurring
- _Action_: IMMEDIATE escalation to trustee board and legal counsel; consider voluntary
  disclosure to TPR (PA 2004 s.70 whistleblowing duty); emergency remediation required;
  may require suspension of certain scheme activities

**Examples by classification:**

| Classification    | Example                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| COMPLIANT         | Actuarial valuation completed within 15-month deadline; TKU assessed for all trustees; Chair's Statement approved and covers all 6 areas                                                                                                                                     |
| PARTIAL           | SIP in place but ESG policy section added 4 years ago and not reviewed since 2021 Regulations; ORA not conducted since March 2024 Code; TCFD report published late (9 months after year end, not 7)                                                                          |
| NON-COMPLIANT     | DB scheme 4 years without actuarial valuation; no GMP equalisation project despite 1990–1997 GMP liabilities; Chair's Statement not approved by trustee board; MNT elections never conducted for scheme with 10+ members                                                     |
| CRITICAL EXPOSURE | Employer contributions not paid for 3+ consecutive months (TPR notifiable event); DB scheme in deficit with employer in administration and no PPF assessment period notification; GMP data irrecoverable — members have received materially incorrect benefits for 10+ years |

⟁ **CLARIFY** — For borderline classifications where scheme-specific context would change
the classification (e.g., a late TCFD report where the delay was caused by a data provider
failure, properly documented), ask the user before finalising severity.

### Step 8: Generate Remediation Recommendations

For each PARTIAL, NON-COMPLIANT, or CRITICAL EXPOSURE finding, provide:

1. **Specific remediation action**: What the trustees must do, not just what is wrong
2. **Statutory basis**: Which provision or Code module creates the obligation
3. **Priority timeline**: IMMEDIATE / NEAR-TERM / BACKGROUND
4. **Evidence of completion**: What documentation demonstrates the gap has been remediated
5. **Escalation triggers**: When to involve external legal counsel, TPR notification, or
   the Pensions Ombudsman

**Remediation timeline tiers:**

| Tier           | Timeframe   | Applies When                                                                       |
| -------------- | ----------- | ---------------------------------------------------------------------------------- |
| **IMMEDIATE**  | 0–30 days   | CRITICAL EXPOSURE; ongoing member harm; notifiable events; criminal liability risk |
| **NEAR-TERM**  | 30–90 days  | NON-COMPLIANT; material regulatory breach; approaching TPR deadline                |
| **BACKGROUND** | 90–180 days | PARTIAL; governance improvement; policy updates; training programmes               |

### Step 9: TPR Notifiable Events Check

Review whether any findings trigger a TPR notifiable event duty (PA 2004 s.69; Pensions
Schemes Act 2021 notifiable events — new regime from April 2023 [VERIFY]):

**Employer-related notifiable events (PA 2004 s.69):**

- Decision to cease business in the UK
- Decision to relinquish control of an employer group company
- Change in credit rating (where applicable)
- Certain redundancies

**Scheme-related notifiable events:**

- Failure to pay contributions for 60+ days
- Actuary resignation without replacement within 30 days
- Scheme auditor resignation without replacement within 30 days
- Failure to produce scheme accounts within 7 months of year end
- Any event that is materially detrimental to the scheme under PSA 2021

**Employer-related notifiable events (PSA 2021 — new regime, from 2023):**
[VERIFY current scope of PSA 2021 notifiable events regime; staged implementation]

⟁ **CLARIFY** — If any finding involves a potential notifiable event, flag it explicitly
and ask whether trustees have already notified TPR or whether notification should be
considered as part of the remediation plan.

### Step 10: Quality Verification

Before delivering the assessment, run these quality checks:

#### Citation Quality Gates (run silently — revise failures before delivery)

| Gate           | Rule                                                                               | Fail Action                                                      |
| -------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every statutory obligation cites a specific Act, section, and statutory instrument | Add citation or mark [VERIFY — counsel to confirm]               |
| **Format**     | All statutory references follow consistent format (e.g., PA 2004 s.224(2))         | Fix format                                                       |
| **Currency**   | Every cited provision verified as current law (not repealed or amended)            | Flag [CHECK CURRENCY]                                            |
| **Domain**     | Analysis stays within England and Wales occupational pension scheme law            | Remove or flag any Scottish, SIPP, or public sector regime bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden                                          | Add confidence qualifier                                         |

#### Self-Interrogation for CRITICAL EXPOSURE Classifications

Apply this 3-pass test to every CRITICAL EXPOSURE finding:

**Pass 1 — Legal Chain Integrity**: Does the obligation follow logically from the cited
statute? Would TPR or a court reach this conclusion? What is the strongest counter-argument?

**Pass 2 — Completeness**: Have all relevant exemptions or transitional provisions been
considered? Are there scheme-specific facts that change the analysis?

**Pass 3 — Challenge**: Under what circumstances could a reasonable pensions adviser accept
this position? Is CRITICAL EXPOSURE proportionate, or should this be NON-COMPLIANT?

Record outcome: `self_interrogation: "PASS / REVISED / NOT APPLICABLE"`

#### Confidence Scoring

| Level        | Range     | Meaning                                                            | Action                                                        |
| ------------ | --------- | ------------------------------------------------------------------ | ------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no room for doubt                      | State with confidence                                         |
| **High**     | 0.80–0.94 | Strong authority, minor points of detail uncertain                 | State with brief caveat                                       |
| **Probable** | 0.60–0.79 | Good basis but scheme-specific facts could change outcome          | State with reasoning and contra-indicators                    |
| **Possible** | 0.40–0.59 | Genuinely uncertain — competing arguments or TPR has not clarified | Flag for professional pensions adviser review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                            | Do not assert; flag [UNCERTAIN — pensions counsel to advise]  |

---

## Assessment Areas Reference

### 13-Area Assessment Matrix

| #   | Area                                | Tier               | Primary Legislation                      | TPR Code Module                |
| --- | ----------------------------------- | ------------------ | ---------------------------------------- | ------------------------------ |
| 1   | Trustee Duties and Governance       | Deep               | PA 1995 s.33; PA 2004 s.241              | Governing body                 |
| 2   | Trustee Knowledge and Understanding | Deep               | PA 2004 ss.247–249; SI 2006/686          | TKU                            |
| 3   | Member-Nominated Trustees           | Standard           | PA 1995 ss.16–21; SI 2006/714            | Governing body                 |
| 4   | Auto-Enrolment                      | Deep               | Pensions Act 2008; SI 2012               | N/A (employer duty via scheme) |
| 5   | DB Funding and Actuarial            | Deep (DB only)     | PA 2004 ss.221–233; 2024 DB Funding Code | DB funding code                |
| 6   | TPR General Code (March 2024)       | Deep               | PA 2004; SI 2005; General Code 2024      | All modules                    |
| 7   | ESG / TCFD Reporting                | Deep (£1bn+)       | SI 2021/839; DWP Guidance                | Investment governance          |
| 8   | GMP Equalisation                    | Deep (pre-1997 DB) | Barber [1990]; PA 1995 s.62              | N/A                            |
| 9   | Transfer Values                     | Deep               | PA 1995 ss.93–101; PSA 2021 ss.125–127   | Member transactions            |
| 10  | Pensions Dashboards                 | Standard           | PSA 2021 ss.238–240; SI 2022/1220        | N/A                            |
| 11  | Data Protection                     | Standard           | UK GDPR; DPA 2018                        | Administration                 |
| 12  | Member Communications               | Standard           | SI 2013/2734; SI 2015 (DC)               | Administration                 |
| 13  | IDRP                                | Standard           | PA 1995 s.50; SI 2008                    | Administration                 |

---

## Prioritisation Framework

Prioritise remediation findings using three tiers:

**Tier 1 — Immediate Action (Must-Fix)**

- CRITICAL EXPOSURE classifications
- NON-COMPLIANT findings with statutory deadlines passed
- Findings where member harm is occurring or imminent
- Any TPR notifiable event not yet reported
- Examples: Unvalued DB scheme; contributions not paid; GMP data irrecoverable;
  no IDRP; pensions dashboards deadline missed

**Tier 2 — Near-Term Action (Should-Fix within 90 days)**

- NON-COMPLIANT findings without immediate member harm
- PARTIAL findings where a statutory deadline is approaching
- Governance gaps exposed by the March 2024 TPR Code
- Examples: ORA not completed since March 2024; SIP not reviewed in 3+ years;
  TCFD report overdue; Chair's Statement incomplete

**Tier 3 — Background Action (Good Practice, 90–180 days)**

- PARTIAL findings representing governance improvement rather than regulatory breach
- Training updates, policy refreshes, process automation
- Examples: TKU log not fully maintained; conflicts register not formally reviewed;
  professional adviser review overdue; data quality improvements for dashboards

---

## Quality Assurance Framework

### PDCA Quality Cycle for Pensions Compliance Assessment

**PLAN**: Identify scheme type, size, and applicable regulatory requirements. Establish
the assessment scope. Identify likely compliance risk areas based on scheme context.

**DO**: Conduct the 13-area assessment. Flag deviations. Classify severity. Generate
remediation recommendations. Check notifiable events.

**CHECK**: Run 5 Citation Quality Gates. Apply Self-Interrogation to all CRITICAL EXPOSURE
findings. Confirm all 13 assessment areas reviewed (or explicitly noted as out of scope).
Verify classifications are consistent with the four-tier system.

**ACT**: Record new compliance patterns identified. Flag regulatory developments that
should update future assessments. Note whether a follow-up assessment is recommended.

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-uk-pensions-trustee-compliance"
  assessment_date: "[date]"
  scheme_type: "[DB / DC / Hybrid / CDC]"
  scheme_size: "[assets band]"
  trustee_board_type: "[Lay / Professional / Corporate sole / Mixed]"
  assessment_scope: "[Full 13-area / Targeted: specify areas]"
  areas_assessed: "[list]"
  areas_out_of_scope: "[list, with reason]"
  legalcode_mcp: "Connected / Not connected"
  regulatory_baseline_file: "[path or 'Not created']"
  statutes_consulted:
    - "[PA 1995 — VERIFIED / UNVERIFIED]"
    - "[PA 2004 — VERIFIED / UNVERIFIED]"
    - "[PSA 2021 — VERIFIED / UNVERIFIED]"
    - "[SI 2021/839 — VERIFIED / UNVERIFIED]"
    - "[SI 2013/2734 — VERIFIED / UNVERIFIED]"
    - "[TPR General Code March 2024 — VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "[Barber v Guardian Royal Exchange [1990] — VERIFIED / UNVERIFIED]"
  tpr_guidance_consulted:
    - "[TPR DB Funding Code 2024 — VERIFIED / UNVERIFIED]"
    - "[TPR transfer guidance — VERIFIED / UNVERIFIED]"
    - "[PDP staging schedule — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  findings_summary:
    critical_exposure: "[number]"
    non_compliant: "[number]"
    partial: "[number]"
    compliant: "[number]"
  notifiable_events_identified: "Yes / No / Possible — [detail]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL EXPOSURE items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[e.g., Trust deed not reviewed — scheme-specific modifications to statutory defaults not assessed]"
    - "[e.g., Actuarial data not available — DB funding assessment based on trustee-provided summary]"
    - "[e.g., Pensions dashboard staging deadlines: PDP has revised schedules — [VERIFY current dates]]"
  reviewer: "AI-assisted — requires qualified pensions solicitor review before trustee action"
```

---

## Anti-Patterns

Catalogue of what NOT to do when advising on UK pensions trustee compliance:

1. **Treating the TPR General Code as aspirational** — The March 2024 Code is the primary
   compliance framework for all occupational schemes. Modules set the expected standard
   against which TPR will assess governance. Treating the Code as "best practice" rather
   than the regulatory floor understates compliance risk.

2. **Equating DB and DC obligations** — DB and DC schemes have materially different regulatory
   regimes. DB has funding, actuary, employer covenant, and PPF obligations that simply do not
   apply to DC. DC has Chair's Statement, value-for-money, and auto-enrolment investment
   governance obligations that are DC-specific. Applying DB analysis to a DC scheme or vice
   versa produces incorrect results.

3. **Ignoring GMP equalisation because "it happened a long time ago"** — The Barber judgment
   is from 1990 but the obligation is still live and still accruing. Every month that passes
   without equalisation in a pre-1997 DB scheme is an additional month of potential underpayment.
   Schemes that have not commenced equalisation are NON-COMPLIANT, not merely behind.

4. **Assuming DB funding is compliant because a recovery plan exists** — A recovery plan
   that was agreed under the pre-2024 Code may not comply with the 2024 DB Funding Code
   requirements (Fast Track or Bespoke FIS). The existence of an old recovery plan does not
   immunise the scheme from the 2024 Code requirements at the next valuation.

5. **Treating professional trustee accreditation as optional** — From October 2025 [VERIFY],
   professional trustees are expected to hold accreditation from an approved accreditation body.
   Non-accredited professional trustees create regulatory and governance risk for the scheme
   and for the trustee organisation itself.

6. **Overlooking the PSA 2021 transfer red/amber/green flag system** — This system has been
   in force since November 2021. Schemes that are still making transfers without conducting
   flag checks are in breach of the PSA 2021 transfer provisions. The absence of a documented
   flag-checking process is NON-COMPLIANT.

7. **Treating pensions dashboards as a future problem** — Staging deadlines are active and
   schemes of all sizes will be affected. A scheme that has not identified its staging deadline
   and begun a connection project is already at risk of missing its statutory deadline.

8. **Conflating TKU assessment with trustee training** — TKU is a statutory obligation under
   PA 2004 ss.247–249. Training is the remedy for TKU gaps, but the obligation is to assess
   TKU (knowledge and understanding), maintain records, and have a plan to address gaps. A
   scheme with a training programme but no TKU assessments is still non-compliant.

9. **Assessing TCFD only for largest schemes** — TCFD mandatory reporting applies from £1bn
   (not just £5bn). Schemes between £1bn and £5bn must publish TCFD-aligned reports. The
   ESG SIP requirement applies to all schemes regardless of size.

10. **Ignoring auto-enrolment re-enrolment cycles** — Re-enrolment must be conducted every
    3 years. Many employers and trustees treat this as a one-time event. Missing a re-enrolment
    cycle means workers who opted out have not been re-enrolled as required. This is a TPR
    enforcement priority area.

11. **Applying a uniform transfer delay window without checking flags** — The PSA 2021 regime
    requires specific flag checks for every transfer request. Delay cannot be justified simply
    by scheme policy: trustees must conduct the flag assessment and, where an amber flag is
    raised, direct the member to MoneyHelper guidance. Systematic delay without flag assessment
    is a breach.

12. **Treating the Chair's Statement as a formality** — The Chair's Statement is a regulatory
    document that must be approved by the trustee board (not just drafted by the administrator),
    cover all 6 statutory areas, and be published by the statutory deadline (7 months after
    scheme year end). A Chair's Statement that is not board-approved, or that omits required
    content, is NON-COMPLIANT.

13. **Assuming conflicts of interest are managed informally** — The TPR General Code (March 2024) requires a written conflicts of interest policy and a register of trustee interests.
    Informal management of conflicts without a written policy is NON-COMPLIANT under the
    current Code.

14. **Missing notifiable event obligations** — Notifiable events under PA 2004 s.69 and the
    expanded PSA 2021 regime must be reported to TPR within prescribed periods. Trustees who
    identify notifiable events but fail to report them risk personal liability and TPR
    enforcement action under the criminal offence provisions of PSA 2021.

15. **Treating pensions Ombudsman decisions as non-binding** — PO determinations are binding
    on the respondent (trustee or administrator) unless appealed to the High Court. Failure
    to comply with a PO determination exposes trustees to enforcement action. PO decisions
    are also TPR intelligence and can trigger regulatory scrutiny.

16. **Conflating the employer's auto-enrolment duty with the scheme's governance duty** —
    Auto-enrolment is primarily the employer's statutory duty, but the scheme must be a
    qualifying scheme for the employer's duty to be discharged. Trustees of an employer's
    chosen scheme share responsibility for ensuring the scheme qualifies (contribution test
    or benefit test). A scheme that fails the qualifying test exposes both employer and
    trustees to TPR enforcement.

17. **Overlooking GMP data quality as a prerequisite for equalisation** — GMP equalisation
    cannot proceed without accurate GMP data reconciled with HMRC records. Many pre-1997
    schemes have years of data gaps. Treating equalisation as a single actuarial exercise
    without first completing GMP reconciliation and data cleansing leads to equalisation
    exercises that are actuarially incomplete.

18. **Not distinguishing Fast Track from Bespoke under the 2024 DB Funding Code** — The
    2024 Code introduced two compliance pathways. Schemes that assume they can continue
    with the prior approach without actively choosing Fast Track or Bespoke will find their
    valuation methodology is not aligned to either pathway, creating a breach risk at the
    next valuation.

---

## External Tool Integration

### legalcode-mcp (Primary Legal Research Tool)

**With legalcode-mcp connected (preferred):**

- In Step 3, search for:
  - Current text of PA 1995, PA 2004, PSA 2021 relevant sections
  - TPR General Code of Practice (March 2024) — current version
  - 2024 DB Funding Code — current requirements
  - DWP TCFD guidance — applicable thresholds and reporting requirements
  - Current PDP staging schedule (pensions dashboards)
  - Recent TPR enforcement decisions (for calibrating severity)
  - Recent TPR Dear Trustee letters
- Mark all legalcode-mcp-sourced references as VERIFIED in the Glass Box audit trail
- Save to `/tmp/legalcode-pensions-baseline.md`

**Without legalcode-mcp:**

- Mark all statutory and TPR Code references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus assessment on governance framework and workflow analysis rather than
  asserting specific legislative provisions with confidence
- Recommend trustee board obtain independent pensions legal advice on statutory citations

---

## Writing Standards

Apply these standards to all trustee-facing and employer-facing output:

**For remediation recommendations (shared with trustee board):**

- Plain language — pensions advisers use jargon; trustees often do not
- Active voice: "Trustees must review the SIP" not "The SIP is required to be reviewed"
- Name specific actors: "The Chair of Trustees must sign the Chair's Statement"
- Specific timelines: "Within 30 days" not "as soon as possible"
- Cite the obligation: "under TPR Code Module — Trustee governance" or "per PA 2004 s.247"

**For legal analysis (internal / legal adviser facing):**

- Statutory precision — cite Act, section, and subsection
- Confidence qualification where applicable
- Acknowledge scheme-specific limitations
- Flag where the trustees' own legal counsel should advise

**Quality gates before delivery (check all 5):**

1. Can a lay trustee understand the executive summary and priority actions?
2. Can a pensions solicitor follow the statutory basis for each finding?
3. Is every obligation backed by a specific statutory or regulatory citation, or marked [VERIFY]?
4. Have all vague or hedging phrases been removed or qualified?
5. Is each remediation action specific enough to assign to an individual and track to completion?

---

## Output Format Template

Deliver the assessment using this template:

```markdown
## UK Pensions Trustee Compliance Assessment

**Scheme Name**: [name]
**Assessment Date**: [date]
**Scheme Type**: [DB / DC / Hybrid / CDC]
**Trustee Board**: [composition]
**Scope**: [13-area full audit / targeted — specify areas]
**Prepared for**: [Trustee board / Chair / Legal adviser / Sponsoring employer]

---

## Executive Summary

**Overall Compliance Status**: [RAG rating — e.g., AMBER — material gaps identified]
**Critical Exposures**: [number] | **Non-Compliant**: [number] | **Partial**: [number] | **Compliant**: [number]

**Priority Actions (Top 3):**

1. [Most urgent action — CRITICAL EXPOSURE or highest-priority NON-COMPLIANT]
2. [Second priority]
3. [Third priority]

---

## Findings Summary Table

| Area                        | Status                                     | Severity       | Priority                         | Key Issue        |
| --------------------------- | ------------------------------------------ | -------------- | -------------------------------- | ---------------- |
| Trustee Duties & Governance | [COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL] | [HIGH/MED/LOW] | [IMMEDIATE/NEAR-TERM/BACKGROUND] | [1-line summary] |
| TKU                         | [status]                                   | ...            | ...                              | ...              |
| MNT Elections               | [status]                                   | ...            | ...                              | ...              |
| Auto-Enrolment              | [status]                                   | ...            | ...                              | ...              |
| DB Funding                  | [status / N/A]                             | ...            | ...                              | ...              |
| TPR Code (March 2024)       | [status]                                   | ...            | ...                              | ...              |
| ESG / TCFD                  | [status / N/A below £1bn]                  | ...            | ...                              | ...              |
| GMP Equalisation            | [status / N/A if no GMP]                   | ...            | ...                              | ...              |
| Transfer Values             | [status]                                   | ...            | ...                              | ...              |
| Pensions Dashboards         | [status]                                   | ...            | ...                              | ...              |
| Data Protection             | [status]                                   | ...            | ...                              | ...              |
| Member Communications       | [status]                                   | ...            | ...                              | ...              |
| IDRP                        | [status]                                   | ...            | ...                              | ...              |

---

## Detailed Findings

### Area 1 — Trustee Duties and Governance — [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE]

**Confidence**: [Level]
**Statutory basis**: [PA 1995 s.33; PA 2004 s.241; TPR Code — Governing body module]
**Finding**: [Specific finding — what the trustees are/are not doing]
**Regulatory standard**: [What the law or Code requires]
**Gap**: [Specific gap between actual and required]
**Impact**: [Practical risk — enforcement, member harm, liability]
**Remediation action**: [Specific steps trustees must take]
**Priority**: [IMMEDIATE / NEAR-TERM / BACKGROUND]
**Evidence of completion**: [What documents or actions will close this finding]

[Repeat for all 13 areas]

---

## TPR Notifiable Events Check

| Event                                      | Triggered?         | Action Required |
| ------------------------------------------ | ------------------ | --------------- |
| Employer contributions not paid (60+ days) | Yes / No / Unknown | [action or N/A] |
| Actuary resignation                        | Yes / No / Unknown | [action or N/A] |
| DB scheme deficit (s.75 triggered)         | Yes / No / Unknown | [action or N/A] |
| PSA 2021 materially detrimental event      | Yes / No / Unknown | [action or N/A] |

---

## Remediation Roadmap

### IMMEDIATE (0–30 days)

- [ ] [Action 1] — Owner: [trustee board / chair / administrator] — Deadline: [date]
- [ ] [Action 2]

### NEAR-TERM (30–90 days)

- [ ] [Action 3]
- [ ] [Action 4]

### BACKGROUND (90–180 days)

- [ ] [Action 5]
- [ ] [Action 6]

---

## Glass Box Audit Trail

[YAML block from template above]
```

---

## Localization Notes

This skill is specific to England and Wales occupational pension law. For related
jurisdictions, note the following variations:

- **Scotland**: Many provisions of PA 1995 and PA 2004 apply equally to Scotland; however,
  trust law in Scotland differs (no rule against perpetuities; different land law). Adapt
  for Scots law with a Scottish pensions specialist.
- **Northern Ireland**: Separate but parallel pensions legislation exists; provisions are
  broadly equivalent but the Pensions Regulator (Northern Ireland) functions separately
  [VERIFY current NI regulatory structure post-Brexit].
- **Public sector**: Public sector pension schemes (NHS, LGPS, Teachers, Armed Forces,
  Civil Service) are governed by separate statutory frameworks and are outside the scope
  of this skill.
- **SIPPs and personal pension schemes**: Regulated by the FCA under FSMA 2000 (not TPR
  for most purposes); this skill does not apply.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Pensions Act 1995, 2004, 2008; Pension Schemes Act 2021 (primary legislation)
- TPR General Code of Practice (March 2024) — published text
- TPR DB Funding Code (2024) — published text
- DWP TCFD Guidance for occupational pension schemes
- Pensions Dashboards Programme (PDP) connection requirements
- Barber v Guardian Royal Exchange [1990] ECJ case law
- GMP equalisation joint industry guidance (November 2020)
- PSA 2021 transfer red/amber/green flag regime — implemented November 2021
- Legalcode original research pipeline (2-agent structural + legal research team)
- Reference standard: legalcode-uk-fca-regulatory-compliance + legalcode-contract-review
