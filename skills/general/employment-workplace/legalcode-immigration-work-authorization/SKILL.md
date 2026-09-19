---
name: legalcode-immigration-work-authorization
description: Guide employer-side immigration and work authorization compliance across the United States,
  United Kingdom, European Union, Australia, and Canada. Use when advising on or auditing work visa sponsorship
  (US H-1B, L-1, O-1, TN, E-3; UK Skilled Worker, Global Business Mobility; EU Blue Card, Posted Workers,
  ICT; Australia SID 482, ENS 186, SESR 494; Canada LMIA, CUSMA, IMP), employment eligibility verification
  (US I-9/E-Verify; UK right-to-work checks; Australian visa work conditions), employer sponsorship obligations,
  compliance audits, site visit preparedness, penalty exposure assessment, and immigration data protection.
  Also triggers for employee mobility planning, cross-border assignment structuring, immigration program
  design, and workforce compliance reviews. Jurisdiction-specific with multi-jurisdiction comparative
  analysis.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Immigration & Work Authorization

> **Disclaimer**: This skill provides a framework for AI-assisted immigration and work
> authorization compliance guidance. It does not constitute legal advice. Immigration law
> is highly fact-specific, jurisdiction-dependent, and changes rapidly. All outputs must be
> reviewed by a qualified immigration attorney or advisor licensed in the relevant
> jurisdiction before any reliance. Statutory and regulatory references are drawn from
> research current through early 2026 and carry hallucination risk — verify against
> authoritative government sources before acting. This skill covers employer-side compliance
> only; it does not substitute for individual immigration counsel.

---

## Purpose and Scope

This skill guides employer-side immigration and work authorization compliance analysis,
program design, and audit preparation across five major jurisdictions.

**Covers:**

- Visa category selection and employer sponsorship requirements (US/UK/EU/AU/CA)
- Employment eligibility verification and right-to-work compliance
- Employer obligation audits and compliance gap analysis
- Penalty exposure assessment and remediation planning
- Cross-border assignment structuring and posted worker compliance
- Immigration program governance and documentation frameworks
- Compliance classification (COMPLIANT / PARTIAL / NON-COMPLIANT) with remediation steps

**Does not:**

- Provide individual immigration advice or represent individual visa applicants
- Substitute for qualified immigration legal counsel
- Cover refugee/asylum processes, citizenship, or family-based immigration
- Apply beyond the five covered jurisdictions without explicit [JURISDICTION-SPECIFIC] adaptation
- Guarantee immigration outcomes — all determinations rest with the relevant government authority

---

## Jurisdiction and Governing Law

This skill covers five major jurisdictions. When operating within a specific jurisdiction,
apply its legal framework. When conducting multi-jurisdictional analysis, note where
frameworks diverge.

| Jurisdiction       | Primary Statute / Framework                                                                                                                                | Regulator                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **United States**  | Immigration and Nationality Act (INA); 8 U.S.C. § 1101 et seq.; 8 CFR; 20 CFR Part 655                                                                     | USCIS, DOL, DOJ Civil Rights Div.                      |
| **United Kingdom** | Immigration Act 1971; Immigration Rules (HC 395); Points-Based System                                                                                      | Home Office / UKVI                                     |
| **European Union** | Blue Card Directive 2021/1883/EU; Posted Workers Dir. 96/71/EC (amend. 2018/957/EU); ICT Dir. 2014/66/EU; Single Permit Dir. 2011/98/EU (recast 2024/1233) | National competent authorities (Member State-specific) |
| **Australia**      | Migration Act 1958 (Cth); Migration Regulations 1994 (Cth); Migration Amendment (Skills in Demand) Act 2024                                                | Department of Home Affairs (DoHA); ABF                 |
| **Canada**         | Immigration and Refugee Protection Act (IRPA), S.C. 2001, c. 27; IRPR SOR/2002-227                                                                         | IRCC, ESDC/Service Canada                              |

[JURISDICTION-SPECIFIC] When localizing for EU Member States, always verify the national
transposition statute, as Directives are implemented unevenly across Member States and
individual national law controls. The EU Blue Card Directive 2021/1883 transposition was
required by 18 November 2023 but was missed by several Member States (e.g., France
transposed only in May 2025).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The jurisdiction is unclear (affects the entire analysis)
- The visa category is ambiguous (different obligations apply to each)
- The employer's compliance posture is unknown (audit vs. design vs. incident response)
- Facts that would materially change severity classification are absent

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

---

## Workflow

### Step 1: Accept Input and Identify the Engagement Type

Accept input in any of these formats:

- **Audit request**: "Review our H-1B compliance" or "Audit our right-to-work program"
- **Specific scenario**: "We want to sponsor a foreign national for X visa"
- **Incident response**: "We received an ICE/UKVI/DoHA inspection notice"
- **Program design**: "Build our immigration compliance framework"
- **Comparison**: "Compare our options for relocating an employee from [Country A] to [Country B]"

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user (skip questions already answered):

1. **Jurisdiction(s)**: Which countries/regions does this engagement cover?
   - Options: United States only, United Kingdom only, EU (specify Member State), Australia only,
     Canada only, Multiple jurisdictions (specify which), All five jurisdictions
   - _Why this matters_: Legal requirements, penalties, and workflows differ fundamentally.

2. **Engagement type**: What is the primary goal?
   - Options: Compliance audit (review existing program), Visa sponsorship (new hire/transfer),
     Incident response (inspection, investigation, violation), Program design (build from scratch),
     Immigration planning (workforce expansion), Other
   - _Why this matters_: Determines depth of analysis and output format.

3. **Employer profile**: Tell me about the sponsoring employer.
   - Prompt: Company size, industry, existing visa categories used, number of sponsored workers,
     whether the employer holds a sponsor licence (UK) or is an approved sponsor (AU).
   - _Why this matters_: Cap-exempt status (US), sponsor licence tier (UK), SAF levy calculation (AU).

4. **Specific concern or trigger**: What prompted this engagement?
   - Examples: upcoming government inspection, internal audit, new hire offer, employee complaint,
     attorney recommendation, M&A transaction, new office opening.
   - _Why this matters_: Incident response requires a different priority order than proactive audit.

5. **Desired output format**:
   - Options: Executive compliance summary, Detailed audit report with remediation steps,
     Visa category comparison and recommendation, Quick risk snapshot (top 5 issues only)
   - _Why this matters_: Determines level of detail and structure.

### Step 3: Identify Applicable Visa Categories and Compliance Programs

Based on the context gathered, identify which immigration categories and compliance programs
are in scope. Use the **Jurisdiction Reference Tables** below to determine the applicable
framework.

**⟁ CLARIFY** — For multi-jurisdictional engagements, confirm which visa categories are
active or under consideration in each jurisdiction before proceeding to analysis.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) or web research to confirm the current state of
relevant statutes, regulations, and policy guidance for the identified visa categories.
Pay particular attention to:

- **Effective date changes**: Immigration regulations change frequently; confirm that the
  version you are applying is currently in force.
- **Salary thresholds**: Nearly all sponsorship categories have annual salary threshold
  updates. Always verify the current threshold before advising on compliance.
- **Policy guidance memos**: USCIS policy manual, Home Office sponsor guidance, DoHA
  guidance, IRCC operational instructions — these frequently supplement or clarify the
  formal regulations.

Save key findings to a local temporary reference file (e.g.,
`/tmp/immigration-authority.md`) structured as:

```markdown
# Immigration Authority Reference

## Jurisdictions: [list]

## Date: [current date]

### Statutes and Regulations

### Policy Guidance (current)

### Salary Thresholds (current fiscal year)

### Recent Changes (last 12 months)
```

**If legalcode-mcp is not connected:**

- Mark all threshold figures and regulatory citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the framework below but instruct the user to verify all figures against
  official government sources before acting

### Step 5: Compliance Analysis

Apply the appropriate analysis framework for each jurisdiction in scope. See the detailed
**Jurisdiction Analysis Frameworks** section below.

For each identified compliance area, assess:

1. Current status: COMPLIANT / PARTIAL / NON-COMPLIANT / NOT APPLICABLE
2. Severity: CRITICAL / HIGH / MEDIUM / LOW
3. Specific gap or issue
4. Required remediation action with timeline

**⟁ CLARIFY** — For long-form audits covering multiple visa categories:

- Ask whether to perform a **comprehensive audit** (all categories, all obligations) or a
  **priority audit** (top-risk areas identified by the employer or triggered by an incident)
- If a specific employee situation is involved, confirm whether the analysis should be
  employee-specific or program-wide

### Step 6: Apply the Self-Interrogation Framework

For every item classified as CRITICAL (highest severity), apply the 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the compliance gap directly violate a specific
statutory or regulatory provision? What would the enforcement authority's position be?

**Pass 2 — Completeness**: Have all related obligations been checked? (e.g., a US H-1B
wage violation must also check Public Access File obligations and LCA attestation accuracy)

**Pass 3 — Challenge**: Is there a reasonable argument that this is compliant? Under what
interpretation? Document the counter-argument even when classifying as non-compliant.

### Step 7: Prioritize and Build the Remediation Plan

Apply the **Prioritization Framework** to order findings:

**Tier 1 — Immediate (act within 30 days)**

- Active civil penalty exposure (ongoing violation)
- Criminal liability risk
- Immediate deportation or visa revocation risk for workers
- Government inspection imminent or in progress

**Tier 2 — Near-Term (act within 90 days)**

- Statutory deadlines approaching (renewal, re-registration, certification)
- Systematic documentation gaps (I-9 errors, missing right-to-work records)
- Sponsor licence / approved sponsor status at risk

**Tier 3 — Ongoing (remediate within 6 months, establish standing processes)**

- Process design gaps (no formal compliance program)
- Training gaps (HR/manager not trained on compliance obligations)
- Audit trail gaps (records not organized for inspection readiness)

### Step 8: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates (silently)
2. For every CRITICAL item, run the 3-pass Self-Interrogation
3. Verify all salary/fee figures are marked [VERIFY] if not confirmed from official source
4. Confirm [JURISDICTION-SPECIFIC] markers are correctly placed
5. Confirm no jurisdiction-specific rule is stated as universally applicable

### Step 9: Deliver Output

Produce output using the **Output Format Template** at the end of this skill. Adapt the
template to the engagement type (audit report, sponsorship advisory, incident response,
or program design).

---

## Jurisdiction Analysis Frameworks

---

### UNITED STATES

#### US Visa Category Reference

| Visa       | Statutory Basis                             | Annual Cap          | Max Initial Stay          | Key Employer Obligations                                   |
| ---------- | ------------------------------------------- | ------------------- | ------------------------- | ---------------------------------------------------------- |
| **H-1B**   | INA § 101(a)(15)(H)(i)(b); 8 CFR § 214.2(h) | 85,000 (65K + 20K)  | 3 years (6 total)         | LCA, prevailing wage, Public Access File, no benching      |
| **L-1A**   | INA § 101(a)(15)(L); 8 CFR § 214.2(l)       | No cap              | 3 years (7 total)         | Qualifying relationship, 1-yr abroad, no LCA               |
| **L-1B**   | Same                                        | No cap              | 3 years (5 total)         | Specialized knowledge, 1-yr abroad                         |
| **O-1A/B** | INA § 101(a)(15)(O); 8 CFR § 214.2(o)       | No cap              | 3 years (1-yr extensions) | Advisory/peer consultation, extraordinary ability evidence |
| **TN**     | INA § 101(a)(15)(E)(iii); USMCA Ch. 16      | No cap              | 3 years (CA citizens)     | USMCA qualifying profession, no LCA required               |
| **E-3**    | INA § 101(a)(15)(E)(iii)                    | 10,500/yr (AU only) | 2 years (renewable)       | LCA required, specialty occupation, Australian citizen     |
| **H-1B1**  | FTAs (Chile/Singapore)                      | 6,800/yr            | 18 months                 | LCA required, specialty occupation                         |

#### US H-1B Deep Analysis

**Employer Compliance Obligations — Checklist**

| Obligation                              | Regulatory Basis                                       | Compliance Standard                                       |
| --------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| File certified LCA before I-129         | 20 CFR § 655.730                                       | LCA must precede petition; 6-month lookback max           |
| Post LCA notice at worksite             | 20 CFR § 655.734                                       | 10 consecutive business days; physical or electronic      |
| Maintain Public Access File             | 20 CFR § 655.760                                       | Available within 1 business day; retained 1 year post-LCA |
| Pay the required wage                   | 20 CFR § 655.731                                       | Greater of actual wage or prevailing wage (OEWS-based)    |
| No benching / unpaid status             | 20 CFR § 655.731(c)(6)                                 | Required wage continues regardless of work availability   |
| File H-1B amendment for material change | 8 CFR § 214.2(h)(2)(i)(E); Matter of Simeio (AAO 2015) | New MSA = new LCA + amendment before move                 |
| Cooperate with FDNS site visits         | Modernization Rule (Jan 2025)                          | Refusal may result in denial or revocation                |
| Retain records post-termination         | 20 CFR § 655.760                                       | 1 year after expiration/withdrawal of LCA                 |

**H-1B Wage Level Compliance**

Prevailing wages are set by DOL's OEWS survey, updated July 1 annually. Four wage levels apply:

| Level     | Description                          | Percentile | Risk if Used Incorrectly                                         |
| --------- | ------------------------------------ | ---------- | ---------------------------------------------------------------- |
| Level I   | Entry-level; limited use of judgment | 17th       | Over-use triggers DOL wage investigation; augments FY audit risk |
| Level II  | Qualified; some use of judgment      | 34th       | Appropriate for most mid-level hires                             |
| Level III | Experienced; full use of judgment    | 50th       | Appropriate for senior staff                                     |
| Level IV  | Fully competent; senior/expert       | 67th       | Required for highly experienced specialists                      |

**Common H-1B Compliance Failures (Severity-Ranked)**

| Failure                                   | Severity | Penalty Exposure                                            | Remediation                                      |
| ----------------------------------------- | -------- | ----------------------------------------------------------- | ------------------------------------------------ |
| Wage level understated                    | CRITICAL | Up to $56,575 per violation (DOL; 2024 levels) + back wages | Correct LCA, pay back wages, document correction |
| No Public Access File                     | HIGH     | Up to $56,575 per violation                                 | Create retroactively; document gap               |
| Failure to file amendment after site move | HIGH     | Status invalid; petition revocable                          | File nunc pro tunc amendment immediately         |
| Benching (non-productive status, unpaid)  | CRITICAL | Back wages + civil penalty                                  | Pay accrued back wages immediately               |
| No LCA notice posting                     | MEDIUM   | DOL investigation trigger                                   | Document cure; improve process                   |
| FDNS site visit refusal/obstruction       | CRITICAL | Petition denial/revocation                                  | Cooperate immediately; attorney involvement      |

**H-1B Lottery / Registration — FY 2027 Onward**

From FY 2027: **wage-based weighted lottery** — registrations at higher DOL wage levels
receive proportionally greater selection probability. Employers offering Level IV wages
receive the highest weight. This creates a structural incentive to offer above-prevailing
wages for specialty occupations.

**AC21 Portability — Employer Checklist**

When an H-1B worker is porting to your organization:

- [ ] Confirm the prior employer's H-1B petition was filed in valid status
- [ ] File new H-1B petition (portability begins upon filing if all conditions met)
- [ ] Confirm the position is in the "same or similar occupational classification"
- [ ] If the worker has a pending I-485 > 180 days, confirm green card portability eligibility

#### US I-9 / E-Verify Compliance

**I-9 Foundation**

| Requirement                                                                     | Rule                           | Common Failure Mode                                       |
| ------------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------------------- |
| Complete Section 1 by **first day of work**                                     | 8 C.F.R. § 274a.2(b)(1)(i)     | Completed too early (before acceptance) or too late       |
| Complete Section 2 by **end of 3rd business day**                               | 8 C.F.R. § 274a.2(b)(1)(ii)    | Completed on day 4+                                       |
| Retain for 3 years from hire OR 1 year after termination (whichever is later)   | 8 C.F.R. § 274a.2(b)(2)        | Purged too early; never destroyed (over-retained)         |
| Re-verify time-limited work authorization before expiration                     | 8 C.F.R. § 274a.2(b)(1)(vii)   | Missed re-verification deadline = constructive violation  |
| Do NOT re-verify status of US citizens, LPRs, or List A docs with no expiration | INA § 274B anti-discrimination | Over-verification triggers DOJ Civil Rights investigation |
| Accept any facially valid document                                              | INA § 274B                     | Demanding specific documents = illegal                    |

**List A / List B+C Reference**

| List A (Identity + Work Auth)                   | List B (Identity only)  | List C (Work Auth only)                                   |
| ----------------------------------------------- | ----------------------- | --------------------------------------------------------- |
| US Passport                                     | Driver's license        | Social Security Card (unrestricted)                       |
| Passport Card                                   | State ID card           | Birth certificate                                         |
| Permanent Resident Card (I-551)                 | School ID with photo    | US Citizen ID Card (I-197)                                |
| EAD (I-766)                                     | Voter registration card | Native American tribal document                           |
| Foreign passport + I-94 with work authorization | Military ID             | I-94 with unexpired foreign passport (certain categories) |

**I-9 Error Classification**

| Error Type                              | Correctable                                                  | How to Correct                                       |
| --------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| Missing information in Section 1 or 2   | Yes (if discovered in audit)                                 | Line through, correct, initial/date                  |
| Wrong date of document expiration       | Yes                                                          | Line through, correct, initial/date                  |
| Section 2 not completed by employer rep | No (but document discovery and correction reduces penalties) | Create contemporaneous remediation memo              |
| Backdated I-9                           | No (criminal issue)                                          | Legal counsel immediately                            |
| Missing I-9 for active employee         | No (but immediate cure reduces penalty)                      | Complete new I-9 immediately; document gap           |
| Section 1 signed by wrong person        | Depends; employer should have employee certify               | Notate file; obtain correct signature where feasible |

**Civil Monetary Penalties (2024 Levels, adjusted annually)**

| Violation                                       | Per-Form Range   |
| ----------------------------------------------- | ---------------- |
| Paperwork violations (incomplete/incorrect I-9) | $272 – $2,728    |
| First-time knowingly hiring unauthorized alien  | $698 – $5,579    |
| Second violation                                | $5,579 – $13,946 |
| Third or subsequent violation                   | $8,369 – $27,894 |

**E-Verify**

- **Voluntary** at the federal level; **mandatory** for federal contractors (FAR clause) and
  employers in many states (AZ, AL, FL, GA, MS, NC, SC, TN, UT, and others require it)
- **Process**: Employer enters I-9 data into E-Verify within **3 business days** of hire;
  system checks SSA and DHS databases; issues either Employment Authorized, Tentative
  Nonconfirmation (TNC), or Final Nonconfirmation (FNC)
- **TNC process**: Employer must provide the employee with a **Further Action Notice**
  (FAN) and allow the employee to **contest** within **8 federal business days**. Employer
  may NOT terminate during the contest period
- **Anti-discrimination**: Using E-Verify selectively (only for certain workers) is illegal
  under INA § 274B

**ICE Audit Process**

1. **Notice of Inspection (NOI)** served on employer → 3 business days minimum to produce
   I-9 forms (may be extended)
2. **ICE audit team** reviews I-9s for substantive and technical violations
3. **Notice of Intent to Fine (NIF)** issued if violations found
4. Employer may request a **hearing** before an Administrative Law Judge (OCAHO)
5. **Voluntary self-audit** prior to NOI is the strongest mitigation tool:
   - Conduct audit of all active employee I-9s
   - Correct technical errors immediately with line-through/initial/date method
   - Create a remediation memo for substantive violations

---

### UNITED KINGDOM

#### UK Work Visa Framework

| Route                               | Governing Rules                            | Key Requirements                                                | Duration                                      |
| ----------------------------------- | ------------------------------------------ | --------------------------------------------------------------- | --------------------------------------------- |
| **Skilled Worker**                  | Immigration Rules Appendix Skilled Worker  | 70 points, sponsor licence, CoS, salary ≥ £26,200 or going rate | Up to 5 years; ILR eligible                   |
| **Senior or Specialist Worker**     | Appendix Senior or Specialist Worker (GBM) | Intra-corporate transfer; 12 months with group                  | Up to 5 years                                 |
| **Graduate Trainee**                | Appendix Graduate Trainee (GBM)            | Corporate trainee programme; degree required                    | Up to 1 year                                  |
| **UK Expansion Worker**             | Appendix UK Expansion Worker (GBM)         | No UK entity yet established                                    | Up to 2 years (no extension)                  |
| **High Potential Individual (HPI)** | Appendix HPI                               | Degree from global top 50 university (within 5 years)           | 2 years (3 for PhDs)                          |
| **Scale-up**                        | Appendix Scale-up                          | Scale-up sponsor; fast-growing company; £33,000 minimum         | 2 years (first 6 months sponsored; then open) |
| **Global Talent**                   | Appendix Global Talent                     | Endorsement from approved body (UKRI, BA, TechNation, etc.)     | Up to 5 years                                 |

#### UK Skilled Worker — Points Assessment

| Points Component                     | Points | Requirement                                                      |
| ------------------------------------ | ------ | ---------------------------------------------------------------- |
| Offer from approved sponsor          | 20     | Sponsor holds A-rated sponsor licence + CoS assigned             |
| Job at appropriate skill level       | 20     | SOC 2020 occupation code at RQF Level 3+                         |
| English language                     | 10     | B1 level or above (SELT, degree in English, or passport country) |
| Salary ≥ £26,200 p.a. OR ≥ £10.75/hr | 20     | **Mandatory threshold** (April 2024 increase)                    |
| Salary ≥ going rate for occupation   | 20     | **OR** salary at or above the going rate for the SOC code        |
| **Total**                            | **70** | **All mandatory points must be met**                             |

**Key April 2024 Salary Changes (Immigration Rules)**:

- General minimum: £26,200/year (increased from £26,000)
- New entrant rate: £20,960/year (for workers under 26 or recent graduates — 20% discount)
- **Immigration Salary List (ISL)**: replaced the Shortage Occupation List; workers on the ISL
  no longer receive a 20% going-rate discount (as of 4 April 2024)
- Care workers: minimum £23,200 with additional restrictions on overseas recruitment

#### UK Right to Work Compliance

**Legal Duty**: Under the **Immigration Act 2014** and the **Immigration, Asylum and
Nationality Act 2006 s.15**, employers have a statutory duty to conduct right-to-work
checks and maintain a statutory excuse against civil penalty.

**Civil Penalty (2024 increase)**:
| Offence | Civil Penalty per Illegal Worker |
|---|---|
| First offence | Up to **£45,000** per worker (increased from £15,000 in Feb 2024) |
| Repeat offence | Up to **£60,000** per worker (increased from £20,000 in Feb 2024) |
| Knowingly employing | Criminal conviction, up to **5 years' imprisonment** |

**Check Types**

| Method                                               | Applicable Workers                                                               | Provides Statutory Excuse?                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Manual check** (original documents in person)      | British/Irish passport holders; indefinite leave holders                         | Yes (List A = unlimited excuse; List B = time-limited)          |
| **Online Home Office check** (Share Code)            | Workers with a BRP, BRC, or digital immigration status (e.g., EU settled status) | Yes — but employer must record check date and Share Code result |
| **IDVT (Identity Document Verification Technology)** | British/Irish passport holders only (from April 2022)                            | Yes, if certified IDVT provider used                            |

**List A vs List B**

| List       | Documents                                                                          | Follow-Up Required?                                             |
| ---------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **List A** | Unrestricted right to work (British passport, Irish passport, settled status, ILR) | No — once checked, no further check needed                      |
| **List B** | Time-limited right to work (visa, BRP with expiry, pre-settled status)             | Yes — must re-check before expiry; failure = criminal liability |

**Brexit — EU Workers**

- EU, EEA, and Swiss nationals who arrived in the UK before **31 December 2020** may have
  either **settled status** (ILR equivalent) or **pre-settled status** (limited leave)
- Physical EU passports and national ID cards are **no longer valid** for right-to-work
  checks (ceased 1 July 2021 for new checks)
- Employers must use the **online Home Office Employer Checking Service** to verify EU
  workers' settled/pre-settled status

**Sponsor Licence Compliance — A-Rating Obligations**

| Duty                                      | Description                                                                                                                        |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Track and monitor workers**             | Monitor attendance, report unexplained absence of 10+ consecutive working days                                                     |
| **Report significant changes**            | Worker stops working, goes missing, or changes role materially — within **10 working days**                                        |
| **Maintain records**                      | Passport copy, DBS (where applicable), contact details, NI number, employment contract — for duration of employment + 1 year after |
| **Cooperate with UKVI compliance visits** | Announced and unannounced; refusal = licence suspension/revocation                                                                 |
| **Keep SMS up to date**                   | Sponsor Management System must reflect current employee details                                                                    |

**Consequences of Licence Loss**:

- All sponsored workers' visas become liable for curtailment (typically 60 days to find new sponsor or leave)
- Employer cannot sponsor new workers
- Can apply to reinstate after a period

---

### EUROPEAN UNION

#### EU Blue Card — Directive 2021/1883/EU

**Key Requirements (as transposed in Member States from Nov 2023)**

| Requirement                                        | Standard                                                                    | Note                                                                         |
| -------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Higher education qualification**                 | Degree requiring ≥ 3 years of study                                         | OR 5 years' relevant professional experience (e.g., IT sector)               |
| **Salary threshold**                               | 1.0x–1.6x average gross annual salary (Member State sets level within band) | Updated annually; verify current figure                                      |
| **Valid employment contract or binding job offer** | Duration ≥ 6 months remaining                                               | Must be for a highly qualified position                                      |
| **Regulated profession**                           | Professional recognition in place (if applicable)                           | Doctor, lawyer, engineer, etc. must meet host state recognition requirements |

**Current Salary Thresholds (2025/2026 — [VERIFY] against Member State sources)**

| Member State        | Standard Threshold                  | Notes                                                 |
| ------------------- | ----------------------------------- | ----------------------------------------------------- |
| Germany             | €50,700/year                        | [VERIFY] — updated annually by BMAS                   |
| France              | €53,836.50/year                     | [VERIFY] — pending update post-May 2025 transposition |
| Spain               | ~€38,844/year                       | [VERIFY] — approximately 1.5x national average        |
| Netherlands         | [VERIFY]                            | Updated annually by IND                               |
| Other Member States | [VERIFY] against national authority | Significant variation across 27 Member States         |

**Intra-EU Mobility Rights (Key Improvement Over 2009 Directive)**

After **12 months** holding a Blue Card in Member State 1:

- Move to Member State 2 with notification (not new application) for stays up to 90 days
- Apply for a second Blue Card in Member State 2 for stays over 90 days (streamlined procedure)
- Time in multiple Member States counts toward the **5-year** permanent residence threshold

#### EU Posted Workers Compliance

**Directive 96/71/EC as amended by 2018/957/EU — Employer Obligations**

| Obligation                                                                    | Requirement                                                                               | Risk if Missed                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Prior notification** to host Member State authority                         | Before or at start of posting; format varies by country                                   | Fine per worker in host MS (up to €30,000 per worker in Germany) |
| **Appoint a liaison person** in host MS                                       | Must be contactable during posting                                                        | Enforcement consequence varies by MS                             |
| **Make documents available** in host MS                                       | Employment contract, payslips, timesheets, A1 certificate — accessible throughout posting | Fine; no defense to wage underpayment claims                     |
| **A1 certificate** from home country social security authority                | Obtain before posting begins                                                              | Dual social security liability risk                              |
| **Pay host country remuneration** (not just minimum wage post-2018 amendment) | All mandatory pay components under host country law or erga omnes CBA                     | Wage underpayment liability; fines                               |

**The 12-Month Rule**

| Posting Period                            | Obligations                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------------------- |
| **0–12 months**                           | Hard nucleus of host country rights (§3 Dir. 96/71 as amended)                        |
| **12–18 months** (with notification)      | All host country employment law applies (bar private int'l law rules on contract law) |
| **Beyond 12 months without notification** | Full host country employment law triggers automatically from month 13                 |

**A1 Certificate — Process**

1. Employer applies to home country social security authority before posting
2. Authority issues **Portable Document A1** (PD A1) confirming continued home-country coverage
3. Worker carries A1 during the posting (required at worksite inspections)
4. Duration: up to **24 months** without bilateral agreement extension
5. If extension needed (beyond 24 months): bilateral application between home and host state authorities

#### EU Intra-Corporate Transfers (ICT) — Directive 2014/66/EU

| Category                     | Max Duration | Salary Requirement                                |
| ---------------------------- | ------------ | ------------------------------------------------- |
| **Managers and Specialists** | 3 years      | At least comparable to host MS equivalent workers |
| **Trainee Employees**        | 1 year       | At least comparable                               |

**Qualifying Conditions**:

- Sending and receiving entity must belong to the same **undertaking or group of undertakings**
- Transferee must have been employed by the group for at least **3 months** before transfer
- Permit is entity-specific and employer-specific within the group

**Short-term mobility** (up to 90 days per MS): ICT holder may work in a second MS based
on the first MS permit with notification only — no second work permit required.

---

### AUSTRALIA

#### Skills in Demand (SID) Visa — Subclass 482

_(Effective 7 December 2024; replaced the TSS visa)_

**Three-Stream Structure**

| Stream                | Salary Floor (2025)                          | Occupation Requirement                                                     | Duration      |
| --------------------- | -------------------------------------------- | -------------------------------------------------------------------------- | ------------- |
| **Specialist Skills** | AUD **$141,210**/year                        | No occupation list — high-earning specialists (tech, AI, fintech, finance) | Up to 4 years |
| **Core Skills**       | AUD **$76,515**/year (CSIT from 1 July 2025) | Must be on Core Skills Occupation List (CSOL) — 456+ occupations           | Up to 4 years |
| **Labour Agreement**  | Per agreement                                | Government-approved Labour Agreement                                       | Per agreement |

**CSIT (Core Skills Income Threshold) — Index-Linked**

| Date         | CSIT                                             |
| ------------ | ------------------------------------------------ |
| 1 July 2023  | AUD $70,000                                      |
| 1 July 2024  | AUD $73,150                                      |
| 1 July 2025  | AUD **$76,515** (AWOTE-indexed)                  |
| Future years | Indexed annually to AWOTE — [VERIFY] each July 1 |

**The Three-Step Sponsorship Process**

1. **Standard Business Sponsorship (SBS) approval** — employer applies to DoHA to become
   an approved sponsor (validity 5 years; renewable)
2. **Nomination** — employer nominates a specific position, occupation (CSOL code), and
   worker; must satisfy Labour Market Testing (LMT) in most cases
3. **Visa application** — worker lodges the visa application; can be lodged concurrently
   with nomination in some cases

**Labour Market Testing Requirements (LMT)**

- Must advertise for at least **28 days**
- Use at least **2 advertising methods** (Seek, LinkedIn, company website, etc.)
- LMT must be conducted no more than **4 months** before nomination
- Retain advertising evidence (screenshots, invoices, response statistics)

**Skilling Australians Fund (SAF) Levy — Mandatory, Non-Refundable**

| Employer Annual Turnover | Levy per Year of Nomination |
| ------------------------ | --------------------------- |
| < AUD $10 million        | AUD **$1,200** per year     |
| ≥ AUD $10 million        | AUD **$1,800** per year     |

Paid upfront for the full nomination period at lodgement. Non-refundable if visa is refused.

**Permanent Residence Pathways from 482 SID**

| Pathway                           | Requirements                                                                                                  |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **ENS 186 (TRT stream)**          | 2 years' employment with sponsoring employer in nominated occupation; sponsor must remain approved throughout |
| **ENS 186 (Direct Entry stream)** | Skills assessment; age < 45 (exceptions apply); CSOL occupation                                               |
| **SESR 494 → subclass 191**       | 5-year provisional; then 3 years work + residency in regional area + income above CSIT                        |

**Australian Employer Sponsorship Obligations — Critical Obligations Matrix**

| Obligation                                                                                                     | Regulatory Basis | Breach Consequence                                            |
| -------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------- |
| **Pay Annual Market Salary Rate (AMSR)** — market rate for equivalent Australian worker, never below CSIT      | Reg 2.79(a)      | Civil penalty up to AUD $396,000; sponsor debarment           |
| **No transfer of costs to worker** — SAF levy, nomination fees, migration agent fees must be borne by employer | Reg 2.79(b)      | Civil penalty; criminal charges for systematic exploitation   |
| **Nominated occupation only**                                                                                  | Reg 2.80         | Visa cancellation risk for worker; civil penalty for employer |
| **Record keeping** — 7 years post-sponsorship                                                                  | Reg 2.84         | Inability to defend compliance audit                          |
| **Notify DoHA of changes** — employment cessation, role change within **28 days**                              | Reg 2.82         | Civil penalty; late notification evidence in audits           |
| **Cooperate with DoHA/ABF inspections**                                                                        | Reg 2.83         | Sponsorship suspension; debarment                             |

**Prohibition on Cost Recovery — Common Breach**

The following are expressly prohibited (civil penalty applies):

- Requiring workers to contribute to SAF levy or nomination fees
- Requiring workers to repay migration agent fees
- "Clawback" agreements that require reimbursement of migration costs if the employee resigns
- Any deduction from wages that relates to sponsorship

**2024 Criminal Offences (Migration Amendment Act 2024)**

Three new criminal offences effective **1 July 2024**:

1. Coercing a temporary visa holder to breach their work-related visa conditions
2. Coercing a non-citizen without a valid visa to accept a work arrangement
3. Using a worker's temporary visa status to **exploit** them in the workplace (imprisonment up to 2 years)

---

### CANADA

#### Canadian Work Authorization Framework

| Category                          | LMIA Required? | Statutory Basis            | Key Characteristics                                   |
| --------------------------------- | -------------- | -------------------------- | ----------------------------------------------------- |
| **TFWP High-Wage LMIA**           | Yes            | IRPA + IRPR Part 11        | Transition plan required; up to 2 years               |
| **TFWP Low-Wage LMIA**            | Yes            | IRPA + IRPR Part 11        | 10% workforce cap; 1-year limit                       |
| **CUSMA/TN Professional**         | No             | IRPR R187; CUSMA Ch. 16    | 63 listed professions; POE application (US citizens)  |
| **CUSMA ICT**                     | No             | IRPR R204(a); CUSMA Ch. 16 | Manager/exec/specialized knowledge; 1 yr with group   |
| **IMP — Intra-Company (R205(a))** | No             | IRPR R205(a)               | C61/C62/C63 codes; physical presence required         |
| **IMP — Reciprocal (R205(b))**    | No             | IRPR R205(b)               | IEC, co-op, international exchange programs           |
| **Open Work Permits**             | No             | IRPR R206                  | Spouse/CLP of skilled worker; PGWP; refugee claimants |

#### LMIA — High-Wage Stream

**Advertising Requirements (as of September 2025)**:

- **Minimum 4 weeks** active advertising on at least **3 methods**
- **Government of Canada Job Bank (mandatory)** — must enable **Direct Apply** and keep it
  active throughout the advertising period
- Download and review all Job Bank Direct Apply applications within **21 days** of receipt
- Additional methods: professional organizations, trade journals, LinkedIn, Indeed, Workopolis
- Must advertise to reach **underrepresented groups**: Indigenous peoples, youth, newcomers,
  persons with disabilities

**Transition Plan Requirements (High-Wage)**:
The Transition Plan must describe:

- Specific activities to recruit Canadians and permanent residents (timeline + metrics)
- Training and skills development initiatives for Canadian workers
- Measurable goals to reduce reliance on the TFWP over time
- Submitted with the LMIA application; reviewed for authenticity by ESDC assessors

**Current LMIA Application Fee**: CAD **$1,000** per position requested (non-refundable)

#### CUSMA / USMCA Work Permits

**TN Professional (US Citizens)**:

- Apply at Canadian **Port of Entry** with:
  - Job offer letter specifying the CUSMA profession and duties
  - Credentials/degree documentation
  - Passport
- No LMIA required; no employer Portal registration required
- Duration: **up to 1 year**; renewable indefinitely from outside Canada
- **63 qualifying professions** — [VERIFY] current list in CUSMA Annex 16-A

**Intra-Company Transferee (CUSMA)**:

- Must be employed by the company for at least **1 year** within the preceding 3 years
- Must transfer to parent, subsidiary, or affiliate in Canada
- Must be in managerial, executive, or **specialized knowledge** capacity
- **2024 Policy Tightening**: Physical Canadian location required; fully remote
  arrangements face heightened scrutiny and likely refusal

#### International Mobility Program (IMP) — Employer Obligations

**Employer Portal Registration (Mandatory)**:

1. Register as an employer on the IRCC **Employer Portal** before hiring IMP workers
2. Submit offer of employment through the Portal (generates **OE number** used in visa application)
3. Pay **CAD $230 compliance fee** per offer of employment
4. Meet and maintain the conditions committed to in the offer

**IMP Compliance Conditions**:

- Worker employed in the **same occupation** as stated in the offer
- Wages are **not substantially different** (DOL: no more than 5% below is generally tolerated; [VERIFY])
- Working conditions not substantially different from the offer
- Reasonable steps taken to **prevent abuse** of the worker

**Canadian Employer Compliance — Penalty Matrix**

| Outcome                                   | Penalty                                                         |
| ----------------------------------------- | --------------------------------------------------------------- |
| **Warning letter** (minor, first-time)    | No AMP; not published                                           |
| **Administrative monetary penalty (AMP)** | Up to CAD $100,000 per violation per worker                     |
| **Aggregate annual cap**                  | CAD $1,000,000 per employer                                     |
| **Banning period**                        | 2 years (first offence) to **permanent ban** (serious/repeated) |
| **Non-compliant employer list**           | Published on IRCC website (for AMP outcomes)                    |
| **LMIA revocation**                       | ESDC may revoke existing positive LMIAs                         |

**Inspection Process**:

1. Notice of inspection issued → employer must produce employment contracts, payroll,
   proof of operations
2. Preliminary non-compliance → **Notice of Preliminary Finding (NOPF)**
3. Employer has **30 days** to respond with explanation and remediation evidence
4. Final determination issued; AMP and banning decisions are published

---

## Compliance Classification System

Classify each finding using the three-tier system:

### COMPLIANT

- All statutory and regulatory requirements met
- Records complete and organized for inspection
- Obligations current (no approaching deadlines missed)
- _Action_: Document for audit trail; no remediation needed

### PARTIAL

- Core requirement is substantially met but with gaps
- Documentation incomplete but obligation is being discharged in substance
- Approaching deadline not yet missed but at risk
- _Action_: Remediate gaps within 30–90 days depending on severity; document cure

### NON-COMPLIANT

- Statutory or regulatory violation exists
- Documentation missing or demonstrably incorrect
- Required action not taken (no LCA, no right-to-work check, etc.)
- _Action_: Immediate remediation; legal counsel involvement for CRITICAL items

### Severity Tiers

| Tier         | Definition                                                                  | Examples                                                                                                  |
| ------------ | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **CRITICAL** | Active violation with immediate penalty exposure or worker status risk      | H-1B benching; no I-9 for active worker; employing illegal worker with knowledge                          |
| **HIGH**     | Material violation; will result in penalties if discovered in audit         | Wage level mismatch on LCA; Public Access File missing; UK right-to-work check never conducted            |
| **MEDIUM**   | Procedural gap; not immediately penalizable but creates audit vulnerability | I-9 Section 2 minor completion error; Australian notification delay; Canadian Employer Portal not updated |
| **LOW**      | Best-practice gap; unlikely to result in penalty but should be remediated   | Missing documentation for a self-corrected I-9; outdated internal policy document                         |

---

## Prioritization Framework

### Tier 1 — Immediate (act within 30 days)

- Workers in active employment without valid work authorization documentation
- Ongoing wage violations (H-1B, Australian AMSR, Canadian LMIA conditions)
- Government inspection in progress or notice received
- Criminal liability exposure identified

### Tier 2 — Near-Term (act within 90 days)

- I-9/right-to-work check gaps for active employees
- Sponsor licence / SBS conditions potentially breached
- Annual salary threshold increases affecting existing sponsored workers
- H-1B amendment filings pending for completed moves
- Posted worker A1 certificates expired or not obtained

### Tier 3 — Ongoing (remediate within 6 months)

- I-9 records organization for inspection readiness
- Internal training programs for HR/management
- Compliance calendar creation (renewal dates, threshold updates, deadline tracking)
- Policy and procedure documentation
- Self-audit cadence establishment (recommend annually)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                | Fail Action                                        |
| -------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Source**     | Every compliance claim cites a specific statute, regulation, or official guidance                   | Add citation or mark "[UNVERIFIED]"                |
| **Format**     | All citations follow jurisdiction-appropriate format (USC, CFR, SI, EU instrument, IRPR regulation) | Fix format                                         |
| **Currency**   | Salary thresholds, fee amounts, and penalty figures checked against current fiscal year             | Flag "[CHECK CURRENCY — figures updated annually]" |
| **Domain**     | Analysis stays within the jurisdiction(s) in scope; no jurisdiction bleed                           | Remove or mark cross-jurisdiction reference        |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                           | Add confidence qualifier                           |

### Self-Interrogation for CRITICAL Items

For any item classified at CRITICAL severity, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the violation assessment follow logically from
the cited statute/regulation? Would the relevant enforcement authority (DOL, UKVI, DoHA,
IRCC/ESDC) actually classify this as a violation? What standard of proof applies?

**Pass 2 — Completeness**: Have all related obligations been checked? (e.g., US H-1B
wage violation also requires checking Public Access File, LCA notice, benching analysis)

**Pass 3 — Challenge**: What is the strongest argument that this is compliant or mitigated?
Is there a "good faith" or "technical error" defense? Document it even when classifying
as non-compliant.

### Confidence Scoring

| Level        | Range     | Meaning                                                      | Action                                            |
| ------------ | --------- | ------------------------------------------------------------ | ------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory violation; enforcement authority would agree | State with confidence; cite provision             |
| **High**     | 0.80–0.94 | Strong basis; minor interpretive questions possible          | State with brief caveat                           |
| **Probable** | 0.60–0.79 | Good arguments; could differ under agency interpretation     | State with reasoning and note contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; fact-dependent                          | Flag for legal counsel review; present both sides |
| **Unlikely** | 0.0–0.39  | Speculative basis                                            | Do not assert as violation; flag "[UNCERTAIN]"    |

---

## Anti-Patterns

What NOT to do in immigration and work authorization compliance work:

1. **Using outdated salary thresholds**: Most salary thresholds update annually (CSIT in
   Australia every July 1; OEWS-based LCA wages update July 1; UK minimum salary subject
   to Immigration Rules changes; EU Blue Card thresholds vary by Member State). Always
   verify the current-year figure before advising.

2. **Assuming H-1B cap-exempt status without verification**: Not every educational
   institution, nonprofit, or research entity qualifies for cap exemption. The affiliation
   must be genuine and meet the USCIS standard. Confirming cap-exempt status incorrectly
   means skipping the lottery — making the entire sponsorship void.

3. **Ignoring the AC21 portability requirements**: Advising that an H-1B worker can
   immediately port to a new employer on the day of filing the new petition, without
   confirming the worker was in valid H-1B status at filing, is a common error.

4. **Conflating right-to-work checks with background checks (UK)**: UK right-to-work
   checks must be conducted **before employment begins**. A background check or CRB/DBS
   check is separate and does not satisfy the right-to-work obligation.

5. **Accepting a photocopy or scan for a UK right-to-work check (manual method)**: Manual
   checks require **original documents** to be reviewed in person or via live video call
   (under COVID-adjusted rules), not photocopies or emailed scans. Photocopies do not
   create a statutory excuse.

6. **Failing to re-verify List B I-9 documents before expiration**: Time-limited work
   authorization documents must be re-verified **before expiration** (not on expiration
   day, and never after). Missed re-verification is a constructive knowingly-hiring
   violation.

7. **Over-verifying US citizens or lawful permanent residents**: Demanding a specific
   document (e.g., US passport, green card) from a US citizen or LPR, or asking for more
   or different documents than permitted, violates INA § 274B anti-discrimination
   provisions. The employee may present any combination of acceptable documents from the
   I-9 lists.

8. **Backdating I-9 forms**: Correcting an I-9 by backdating the date of hire, document
   inspection, or completion is a criminal falsification. Line-through corrections with
   initials and current date are the only permitted correction method.

9. **Passing migration costs to sponsored workers (Australia)**: Requiring an Australian
   482/SID visa holder to repay SAF levy, nomination fees, or migration agent costs —
   including via salary deduction or "clawback" agreement — is an explicit civil penalty
   breach. These agreements are unenforceable and constitute a sponsorship violation even
   if the employee signed voluntarily.

10. **Failing to file an H-1B amendment after an MSA move**: Under Matter of Simeio
    (AAO 2015), moving an H-1B worker to a new worksite in a different Metropolitan
    Statistical Area requires a new LCA **and** an H-1B amendment **before** the move
    (or concurrent with it). Moving the worker first is a violation of the petition's
    terms. The 2024 Modernization Rule eliminated the itinerary requirement but did not
    eliminate the amendment obligation for new-MSA moves.

11. **Ignoring the UK sponsor SMS reporting deadlines**: Sponsor licence holders must
    report significant changes (worker cessation, unexplained absence, role change) within
    **10 working days** via the Sponsor Management System. Missing this deadline is a
    compliance failure that UKVI can use to suspend or revoke the licence.

12. **Treating all EU Member States as having the same Blue Card rules**: The 2021 Blue
    Card Directive was transposed unevenly. France did not transpose until May 2025.
    Salary thresholds vary significantly across Member States. Always verify the specific
    Member State's national law rather than relying on the EU Directive text alone.

13. **Overlooking the posted workers A1 certificate**: Employers frequently arrange cross-
    border postings without securing the A1 certificate. Without it, the worker may be
    subject to **dual social security contributions** in both the home and host countries —
    a significant unexpected cost and a compliance failure detectable at any EU border
    crossing or worksite inspection.

14. **Using a CUSMA/TN permit for a permanent role**: TN status is by definition temporary
    and is not a pathway to permanent residence. Structuring a role as TN when the intent
    is for the worker to remain permanently creates dual intent issues and may constitute
    misrepresentation. Consider PERM/green card sponsorship or Canadian PR pathways early
    in the employment relationship.

15. **Failing to maintain Canadian IMP Employer Portal registration currency**: IMP
    employers must update the Employer Portal when employment conditions change. Failing
    to reflect wage changes, occupation changes, or work location changes in the Portal
    is a standalone compliance violation under IRPR R209.2 — separate from whether the
    worker's permit reflects those conditions.

16. **Relying on verbal authorization or implied permission for E-Verify TNC contests**:
    During a US E-Verify Tentative Nonconfirmation process, the employer must provide the
    employee with the official **Further Action Notice** in writing and allow a full **8
    federal business days** to contest. Verbal notification is not sufficient; terminating
    before the contest period expires is unlawful.

17. **Assuming an Australian 482/SID visa holder can change jobs freely**: The 482/SID
    visa is employer-specific and occupation-specific. The worker must be employed by the
    nominating employer in the nominated occupation. Any change requires a new nomination
    (and possibly a new visa application). Internal promotions or role changes may require
    a new nomination even without a change of employer.

---

## Localization Notes

When operating in a specific jurisdiction, supplement with:

**United States**: State-level E-Verify mandates vary. State labor laws may impose
additional pay obligations for sponsored workers. California, New York, and Illinois have
specific anti-discrimination rules affecting I-9 practices. [VERIFY] current state E-Verify
mandate status for the employer's operating states.

**United Kingdom**: Scotland, Wales, and Northern Ireland generally apply the same
Immigration Rules but have devolved health and social care sectors with different right-
to-work check requirements in some contexts. Channel Islands and Isle of Man are outside
the UK immigration system entirely.

**EU Member States**: Always verify national transposition legislation. Key sources:
Germany — Bundesamt für Migration und Flüchtlinge (BAMF); France — OFII; Netherlands —
IND; Spain — Secretaría de Estado de Migraciones; Italy — Sportello Unico Immigrazione.

**Australia**: State and territory-based offences may overlap with Commonwealth obligations
for worker exploitation. Fair Work Ombudsman has concurrent jurisdiction to DoHA for
wage-related compliance. The Northern Territory and Western Australia have special regional
rules for some visa categories.

**Canada**: Significant provincial variation in LMIA thresholds (median wage varies by
province), PNP streams, and sector-specific programs. Employers operating in multiple
provinces must check the applicable median wage for each work location. Quebec has a
separate immigration system with the **Arrimage** provincial program replacing some
federal TFWP streams.

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for jurisdiction-specific statute text and current regulatory thresholds
- Retrieve recent policy guidance memos (USCIS Policy Manual, Home Office sponsor guidance)
- Verify current salary thresholds against government sources
- Retrieve case law on immigration violations (OCAHO decisions, UK Immigration Tribunal)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all threshold figures with [VERIFY — check current fiscal year amount]
- Mark all penalty amounts with [VERIFY — adjusted annually]
- Refer user to official government sources for verification:
  - US: USCIS.gov, dol.gov/agencies/whd, ice.gov
  - UK: gov.uk/sponsor-management-system, gov.uk/legal-right-to-work
  - EU: home-affairs.ec.europa.eu; national authority websites
  - Australia: immi.homeaffairs.gov.au; fairwork.gov.au
  - Canada: canada.ca/en/immigration-refugees-citizenship; canada.ca/en/employment-social-development
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`

---

## Writing Standards

Before delivering any output, apply these quality gates:

1. **No jurisdiction bleed**: Do not state a rule from one jurisdiction as if it applies
   universally. Always attribute jurisdiction: "Under US law...", "In the UK...",
   "Australian sponsors must...", "Canadian IMP employers are required to..."

2. **Threshold currency**: Any salary floor, fee amount, or penalty figure must be
   accompanied by a [VERIFY] tag unless confirmed from a current official source. Figures
   change annually and are high-stakes; confidently stating an outdated figure causes
   direct harm.

3. **Plain language for actionable steps**: Remediation steps must be stated as clear
   actions: "File a new LCA and H-1B amendment before the worker relocates", not "LCA
   and amendment compliance should be considered".

4. **Proportionality**: Calibrate detail to severity. CRITICAL findings get full
   self-interrogation, legal citation, and remediation roadmap. LOW findings get one line
   with a recommended action.

5. **No legal advice disclaimer in body**: The disclaimer is at the header. Do not repeat
   "this is not legal advice" on every finding — it undermines clarity. Instead, add
   attorney referral only where a CRITICAL or novel issue requires specialized counsel.

---

## Output Format Template

````markdown
# Immigration & Work Authorization Compliance Analysis

**Prepared for**: [Company / Engagement]
**Date**: [Date]
**Jurisdictions covered**: [List]
**Engagement type**: [Audit / Sponsorship Advisory / Incident Response / Program Design]
**Skill version**: legalcode-immigration-work-authorization

---

## Executive Summary

[2–4 sentences: overall compliance posture, number of findings by severity, top 3 priorities]

---

## Findings by Jurisdiction

### [Jurisdiction 1, e.g., United States — H-1B]

| #   | Area                 | Status        | Severity | Issue                                                                                   | Required Action                                 | Timeline  |
| --- | -------------------- | ------------- | -------- | --------------------------------------------------------------------------------------- | ----------------------------------------------- | --------- |
| 1   | H-1B Prevailing Wage | NON-COMPLIANT | CRITICAL | Workers in Level I wage classifications for positions that require Level III experience | Correct LCA wage levels; pay back wages         | Immediate |
| 2   | Public Access File   | PARTIAL       | HIGH     | PAF exists but missing prevailing wage determination documentation                      | Add prevailing wage source documentation to PAF | 30 days   |
| ... |                      |               |          |                                                                                         |                                                 |           |

### [Jurisdiction 2, e.g., United Kingdom — Right to Work]

| #   | Area                   | Status        | Severity | Issue                                                      | Required Action                                                                    | Timeline  |
| --- | ---------------------- | ------------- | -------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------- |
| 1   | List B Re-verification | NON-COMPLIANT | CRITICAL | [N] workers with expired visas; no re-verification on file | Conduct immediate right-to-work checks; legal counsel for any unauthorized workers | Immediate |
| ... |                        |               |          |                                                            |                                                                                    |           |

---

## Priority Action Plan

### Tier 1 — Immediate (within 30 days)

1. [Most critical action]
2. [Second critical action]

### Tier 2 — Near-Term (within 90 days)

1. [High-priority action]

### Tier 3 — Ongoing (within 6 months)

1. [Process/program action]

---

## Detailed Findings

[For each CRITICAL and HIGH finding, provide:]

### Finding [#]: [Short title]

- **Jurisdiction**: [Jurisdiction]
- **Regulatory basis**: [Statute/regulation]
- **Issue**: [Specific gap or violation]
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **Confidence**: [Score + rationale]
- **Counter-argument**: [Strongest argument for compliance — document even if overridden]
- **Remediation steps**:
  1. [Action 1]
  2. [Action 2]
- **Evidence required**: [What documentation the employer should gather/create]
- **Penalty exposure**: [Approximate range if violation confirmed in audit]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: legalcode-immigration-work-authorization
  mode: Created from scratch
  engagement_type: "[audit / advisory / incident / design]"
  jurisdictions_analyzed: "[list]"
  visa_categories_analyzed: "[list]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or Not created]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Any limitations, assumptions, or scope constraints]"
    - "[Salary thresholds require annual verification against official sources]"
  reviewer: "AI-assisted — requires qualified immigration attorney review before action"
```
````

```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis drawing on:
- 2-agent research pipeline covering US/UK/EU/AU/CA immigration frameworks
- US sources: INA, 8 CFR § 214.2, 20 CFR Part 655, USCIS Policy Manual,
  AC21 (Pub. L. 106-313), USCIS H-1B Modernization Rule (Jan 2025),
  FY 2027 wage-weighted lottery final rule, Matter of Simeio Solutions (AAO 2015)
- UK sources: Immigration Act 1971, Immigration Rules Appendix Skilled Worker,
  Immigration, Asylum and Nationality Act 2006 s.15, February 2024 civil penalty increases,
  April 2024 salary threshold reforms (£26,200 minimum, ISL replacing SOL)
- EU sources: Blue Card Directive 2021/1883/EU; Posted Workers Directive 96/71/EC as
  amended by 2018/957/EU; Enforcement Directive 2014/67/EU; ICT Directive 2014/66/EU;
  Single Permit Directive 2011/98/EU (recast 2024/1233, effective May 2026);
  Long-Term Residents Directive 2023/2584; Regulation 883/2004 (A1 certificates)
- Australia sources: Migration Act 1958 (Cth); Migration Regulations 1994 Sch 2;
  Migration Amendment (Skills in Demand and Other Measures) Act 2024 (effective 7 Dec 2024);
  Migration Amendment (Strengthening Employer Compliance) Act 2024 (effective 1 Jul 2024);
  CSIT July 2025 ($76,515); SAF levy structure; Migrant Workers' Taskforce (2019)
- Canada sources: IRPA S.C. 2001, c. 27; IRPR SOR/2002-227 R187–R209.992;
  CUSMA Chapter 16 Annex 16-A; IRCC IMP Employer Portal compliance regime;
  ESDC Job Bank Direct Apply mandatory requirements (September 2025);
  IRCC ICT guidelines October 2024 update (physical location requirement);
  Canada federal 2025–2027 levels plan (PNP reduction to 55,000)
```
