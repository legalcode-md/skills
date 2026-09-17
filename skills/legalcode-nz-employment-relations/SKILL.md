---
name: legalcode-nz-employment-relations
description: Assess New Zealand employment law compliance and disputes under the Employment Relations
  Act 2000 (ERA) — good faith obligations, personal grievances, unjustified dismissal, 90-day trial periods,
  breaks and minimum entitlements (Holidays Act 2003), restructuring and redundancy protections, triangular
  employment, restraints of trade, and ERA/Employment Court proceedings. Use when advising on NZ employment
  disputes, reviewing NZ employment agreements, assessing restructuring processes, conducting HR compliance
  audits, or preparing for mediation and ERA proceedings.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess New Zealand employment law compliance and disputes under the Employment Relations Act 2000 (ERA) — good faith obligations, personal grievances, unjustified dismissal, 90-day trial periods, breaks and minimum entitlements (Holidays Act 2003), restructuring and redundancy protections, triangular employment, restraints of trade, and ERA/Employment Court proceedings. Use when advising on NZ employment disputes, reviewing NZ employment agreements, assessing restructuring processes, conducting HR compliance audits, or preparing for mediation and ERA proceedings. Covers the Employment Relations Act 2000, Holidays Act 2003, Minimum Wage Act 1983, Parental Leave and Employment Protection Act 1987, Health and Safety at Work Act 2015 (HSWA) employment intersection, Human Rights Act 1993 discrimination grounds, Privacy Act 2020 employment obligations, and KiwiSaver Act 2006 employer duties. Includes 2024–2026 reforms: high-income dismissal threshold (NZD $200,000+), pay secrecy protections, wage theft criminalisation, and contractor gateway test.


# Legalcode NZ Employment Relations

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of New Zealand
> employment law. It does not constitute legal advice. All outputs should be reviewed by a
> qualified employment lawyer or consultant licensed in New Zealand before reliance. Laws
> and regulations change; verify current applicability before acting on any provision
> described here. Statutory and case law references cited from memory carry hallucination
> risk — verify against authoritative sources (legislation.govt.nz, employmentcourt.govt.nz,
> era.govt.nz) before relying on them.

---

## Purpose and Scope

This skill analyses New Zealand employment law compliance, employment disputes, and
employment agreement obligations across the full lifecycle of the employment relationship.

**Covers:**

- Employment Relations Act 2000 — good faith (ss 3–4), personal grievances (ss 103–103A),
  unjustified dismissal test (s 103A), 90-day trial periods (s 67A), collective agreements,
  and individual employment agreement (IEA) mandatory content
- Holidays Act 2003 — annual leave (4 weeks), sick leave (10 days), public holidays,
  bereavement leave, calculation methodology, and the Employment Leave Bill reform
- Minimum Wage Act 1983 — adult, starting-out, and training wage rates
- Rest and meal breaks — Employment Relations Act 2000 ss 69ZD–69ZI
- Parental leave — Parental Leave and Employment Protection Act 1987 (26-week primary carer
  leave, extended leave, keeping-in-touch days)
- Restructuring and redundancy — consultation obligations, vulnerable employee protections
  (ERA Schedule 1A), redeployment duty, and Transfer of Undertakings
- Triangular employment — ERA amendments 2020 enabling claims against controlling third parties
- Restraints of trade and garden leave — enforceability under NZ common law
- KiwiSaver employer obligations — minimum 3% contribution, auto-enrolment, ESCT
- Health and Safety at Work Act 2015 (HSWA) — employment intersection (PCBU duties,
  worker participation, illness/disability dismissal)
- Human Rights Act 1993 — discrimination on 14 protected grounds in employment
- Privacy Act 2020 — employee monitoring, reference checks, health data handling
- ERA and Employment Court proceedings — mediation, ERA authority process, remedies,
  personal grievance time limits, appeal paths
- 2024–2026 reforms — high-income dismissal threshold (NZD $200,000+), pay secrecy
  protections, wage theft criminalisation, contractor gateway test, Employment Leave Bill

**Does not:**

- Provide legal advice or replace qualified NZ employment counsel
- Cover accident compensation under ACC (Accident Compensation Act 2001)
- Cover personal injury tort claims (barred by ACC)
- Cover immigration and work visa requirements (Immigration Act 2009)
- Cover tax law except KiwiSaver/ESCT obligations
- Cover non-NZ jurisdictions

---

## Jurisdiction and Governing Law

**Jurisdiction:** New Zealand (national statute; no sub-jurisdictions)
**Legal system:** Common law (English common law tradition)
**Primary employment court:** Employment Relations Authority → Employment Court → Court of Appeal

**Key statutes applicable in this skill:**

| Statute                                           | Short Name          | Key Relevance                                                                       |
| ------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------- |
| Employment Relations Act 2000                     | ERA 2000            | Good faith, dismissal, personal grievances, collective bargaining, IEA requirements |
| Holidays Act 2003                                 | HA 2003             | Annual leave, sick leave, public holidays, bereavement leave                        |
| Minimum Wage Act 1983                             | MWA 1983            | Minimum wage rates; adult/starting-out/training                                     |
| Parental Leave and Employment Protection Act 1987 | PLEP Act            | Primary carer leave (26 weeks), extended leave, keeping-in-touch days               |
| Health and Safety at Work Act 2015                | HSWA 2015           | PCBU duties; worker participation; illness-related employment decisions             |
| Human Rights Act 1993                             | HRA 1993            | Discrimination on 14 protected grounds; interaction with ERA PG                     |
| Privacy Act 2020                                  | PA 2020             | Employee monitoring; health data; reference checks; pre-employment screening        |
| KiwiSaver Act 2006                                | KSA 2006            | 3% employer contribution; auto-enrolment; ESCT                                      |
| Crimes (Theft by Employer) Amendment Act 2025     | Wage Theft Act 2025 | Criminalises unauthorised wage deductions (effective March 14, 2025)                |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the legal analysis
- Multiple valid frameworks apply (ERA vs. HRA vs. HSWA)
- Threshold facts are missing (employer size, tenure, dismissal date)
- The user's perspective (employer / employee / neutral) affects the output framing

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

### Step 1: Accept the Employment Matter

Accept the matter in any of these formats:

- **Scenario description**: Facts of an employment dispute or compliance question
- **Document**: Employment agreement, restructuring notice, disciplinary letter, ERA claim
- **Compliance question**: A specific question about NZ employment law obligations
- **Agreement review**: Request to review an individual employment agreement or policy

If no facts are provided, prompt the user to describe the employment situation.

### Step 2: Gather Core Facts

**⟁ CLARIFY** — Before proceeding, ask the user these questions. Skip any already answered
by the input:

1. **Perspective — whose interests are you advising?**
   - Options: Employer, Employee, Both/Neutral (HR audit or dispute overview), Specific
     perspective stated in the document
   - _Why this matters_: The entire framing of risk, recommendations, and remedies shifts
     depending on which side you represent.

2. **Type of matter**
   - Options: Dismissal / disciplinary, Restructuring / redundancy, Personal grievance —
     discrimination/harassment, Personal grievance — unjustifiable disadvantage, Minimum
     entitlements compliance, Employment agreement drafting or review, ERA or Employment
     Court proceeding, KiwiSaver / wage compliance audit, Other
   - _Why this matters_: Determines which statutory framework and thresholds to apply first.

3. **Key dates** (provide all that are known):
   - Employment start date
   - Date of alleged conduct/event
   - Date employee raised grievance with employer (if applicable)
   - Date personal grievance was or will be lodged with ERA (if applicable)
   - _Why this matters_: Personal grievance time limits (90 days to raise; 3 years to lodge
     with ERA) are strict and threshold-determinative.

4. **Employee tenure and remuneration**
   - How long has the employee worked for this employer? (months/years)
   - Is the employee's annual remuneration NZD $200,000 or more?
   - _Why this matters_: Tenure affects qualifying periods; the high-income threshold (NZD
     $200,000+) limits unjustified dismissal personal grievances for employees hired after
     February 21, 2026 (or from February 21, 2027 for existing employees).

5. **Employer size** (number of employees in NZ)
   - Not needed for trial period eligibility (expanded to all employers from December 2023),
     but relevant for KiwiSaver compliance thresholds and ERA hearing fee bands.

If the user provides partial context, proceed with available facts and **state assumptions
explicitly** before proceeding.

### Step 3: Identify the Applicable Legal Framework

Based on the core facts, identify the primary and secondary legal frameworks:

| Scenario                        | Primary Framework        | Secondary Frameworks to Check                                                            |
| ------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------- |
| Dismissal (cause / performance) | ERA 2000 ss 103, 103A    | HRA 1993 (discrimination?), HSWA 2015 (health dismissal?), PA 2020 (privacy in process?) |
| 90-day trial dismissal          | ERA 2000 s 67A           | HRA 1993 (dismissal still invalid if discriminatory), HSWA 2015                          |
| Restructuring / redundancy      | ERA 2000 ss 4, 103(1)(b) | ERA Schedule 1A (vulnerable employees), PLEP Act (parental leave protection)             |
| Harassment or discrimination    | ERA 2000 s 103(1)(d)–(e) | HRA 1993 (parallel claim), PA 2020 (if investigation involved privacy breaches)          |
| Minimum entitlements            | HA 2003, MWA 1983        | ERA 2000 s 4 (good faith), Wage Theft Act 2025                                           |
| KiwiSaver compliance            | KSA 2006                 | MWA 1983 (correct contribution base)                                                     |
| Employment agreement review     | ERA 2000 ss 63–65        | HA 2003, MWA 1983, PLEP Act                                                              |
| Contractor vs. employee         | ERA 2000 s 6             | 2024 contractor gateway test                                                             |
| Privacy / surveillance          | PA 2020                  | HSWA 2015, ERA 2000 s 4                                                                  |
| Parental leave dispute          | PLEP Act 1987            | ERA 2000 (return rights, disadvantage), HRA 1993 (sex/pregnancy discrimination)          |

### Step 4: Threshold Analysis

Before conducting substantive analysis, check all applicable threshold conditions. A failed
threshold changes the available remedies or defences dramatically.

#### 4a. Personal Grievance Time Limits (ERA 2000 ss 114–115)

| Grievance Type                        | Time to Raise with Employer                                        | Time to Lodge with ERA                     |
| ------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------ |
| Standard PG (dismissal, disadvantage) | **90 days** from date action occurred or came to employee's notice | **3 years** from date raised with employer |
| Sexual harassment PG                  | **12 months** from occurrence or when known                        | **3 years** from date raised with employer |

**⟁ CLARIFY** — If any of the following apply, confirm with the user before proceeding:

- Dates are unclear or disputed
- Employee claims not to have known about the action until later (discovery rule)
- Extension application may be needed (ERA has discretion to extend 90-day period;
  discretion is narrow — employer must not be unduly prejudiced)

Classify:

- **COMPLIANT**: PG raised within 90 days (or 12 months for sexual harassment)
- **AT RISK**: Raised within 90 days but close to deadline; lodgement with ERA approaching
  3-year limit
- **NON-COMPLIANT**: PG raised outside 90-day period with no extension application;
  claim is likely time-barred

#### 4b. 90-Day Trial Period Eligibility (ERA 2000 s 67A)

A valid 90-day trial period requires ALL of the following:

| Requirement                                                                                      | Verification Check                                        |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| Agreement signed **before** work commenced                                                       | Confirm execution date vs. start date                     |
| Employee had reasonable time to seek independent advice before signing                           | Agreement not produced minutes before start               |
| Employee has **not previously worked** for that employer in any capacity                         | Check for prior casual, temporary, or related-entity work |
| Trial period clause specifies an **exact number of days** (not "three months")                   | Read clause text precisely                                |
| Trial period is **no more than 90 days**                                                         | Count calendar days from start date                       |
| Agreement clearly states employer may dismiss and employee cannot raise unjustified dismissal PG | Read clause text                                          |

If the trial period clause is **invalid** (any requirement failed), dismissal during the
trial period is treated as ordinary dismissal and must meet the s 103A justification test.

**Important**: Even a valid 90-day trial dismissal does NOT bar:

- Personal grievances based on **discrimination** under ERA s 103(1)(d)
- Personal grievances based on **harassment** under ERA s 103(1)(e)–(f)
- Personal grievances based on **HSWA** or **HRA** grounds
- Enforcement of minimum entitlements (wages, leave, breaks)

#### 4c. High-Income Dismissal Threshold (ERA 2000 s 103 — Feb 2026 Reform)

Employees earning **NZD $200,000+ per annum**:

- If **hired after February 21, 2026**: barred from raising unjustified dismissal PG (all
  other PG grounds remain available — disadvantage, discrimination, harassment)
- If **existing employees at February 21, 2026**: threshold applies from February 21, 2027
  (12-month transitional period)
- **Employer and employee may jointly opt out** of the threshold provision

This threshold does NOT affect claims for:

- Discrimination or harassment
- Unjustifiable disadvantage (non-dismissal)
- Unpaid wages or minimum entitlements
- Breach of good faith

#### 4d. Qualifying Periods for Minimum Entitlements

| Entitlement                                  | Qualifying Period                                                                                                                                                     |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Annual leave (4 weeks)                       | 12 months continuous employment                                                                                                                                       |
| Sick leave (10 days/year)                    | 6 months continuous employment OR meeting the "work test" (average ≥10 hrs/week over 6 months, or ≥1 hr every week for 6 months, or ≥40 hrs every month for 6 months) |
| Parental leave — primary (26 weeks)          | 6-month averaging test OR 12-month qualifying period                                                                                                                  |
| Parental leave — extended (further 26 weeks) | 12-month qualifying period                                                                                                                                            |
| KiwiSaver auto-enrolment                     | First day of employment (ages 18–65)                                                                                                                                  |

### Step 5: Good Faith Obligations Assessment (ERA 2000 ss 3–4)

Good faith is the foundational principle of NZ employment law. It applies to all parties
throughout the employment relationship — including during hiring, performance management,
restructuring, and termination.

#### Core Good Faith Requirements (s 4(1A))

Assess whether the party (usually employer) has:

| Requirement                                        | Assessment Questions                                                                                                                                                                                                     |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Active and constructive relationship**           | Did the employer proactively communicate with the employee? Was the employee kept informed?                                                                                                                              |
| **Responsive and communicative**                   | Were the employee's questions and concerns acknowledged and addressed?                                                                                                                                                   |
| **Information provision before adverse decisions** | Before making a decision that adversely affects the employee's employment, did the employer: (a) provide relevant information, (b) give the employee an opportunity to comment, and (c) genuinely consider the response? |
| **Mutual trust and confidence**                    | Were there any actions that destroyed the foundation of the employment relationship?                                                                                                                                     |

#### Section 4A Penalties

Breach of good faith (standalone, not resulting in PG) is enforceable:

- Individuals: up to **NZD $10,000** per breach
- Companies / organisations: up to **NZD $20,000** per breach

**⟁ CLARIFY** — If the facts suggest a standalone good faith claim (no dismissal), ask
whether the user wants to analyse: (a) good faith breach as the primary cause of action,
(b) unjustifiable disadvantage incorporating good faith failures, or (c) both.

### Step 6: Ground-Specific Analysis

Conduct a deep analysis based on the primary ground identified in Step 3.

#### 6a. Unjustified Dismissal (ERA 2000 ss 103, 103A)

**The Justification Test (s 103A):**
Apply the objective standard: _whether the employer's actions, and how the employer acted,
were what a fair and reasonable employer could have done in all the circumstances at the
time the dismissal occurred._

**Two-limb analysis — both required:**

**Limb 1 — Substantive Justification**

| Question                                                                              | Yes                    | No                       |
| ------------------------------------------------------------------------------------- | ---------------------- | ------------------------ |
| Was there a genuine, documented reason for dismissal?                                 | Supports justification | Undermines justification |
| Was the reason serious enough to warrant dismissal (as opposed to a lesser sanction)? | Supports justification | Undermines justification |
| Had the employee been warned about the conduct/performance issue?                     | Supports justification | Undermines justification |
| Did the employer have a genuine belief the misconduct occurred?                       | Supports justification | Undermines justification |
| Was dismissal within the range of responses available to a reasonable employer?       | Supports justification | Undermines justification |

**Limb 2 — Procedural Fairness**

| Procedural Step                                                 | Present | Absent     |
| --------------------------------------------------------------- | ------- | ---------- |
| Employee notified of specific allegations                       | ✅      | 🔴 RED     |
| Reasonable investigation conducted before conclusion            | ✅      | 🔴 RED     |
| Employee given opportunity to respond to allegations            | ✅      | 🔴 RED     |
| Support person / representative permitted to attend             | ✅      | 🔴 RED     |
| Employee response genuinely considered                          | ✅      | 🔴 RED     |
| Decision-maker was not the investigator (where possible)        | ✅      | 🟡 AT RISK |
| Employee notified of right to seek legal advice before meetings | ✅      | 🟡 AT RISK |
| Written outcome provided                                        | ✅      | 🟡 AT RISK |

**Note on employee contribution (2024 reform):**

- Where the employee's own conduct contributed to the dismissal, remedies may be reduced:
  - **Serious misconduct**: ERA may reduce compensation or reinstatement to zero
  - **Non-serious misconduct**: Contribution reduces remedy (potentially to nil)

#### 6b. Unjustifiable Disadvantage (ERA 2000 s 103(1)(b))

Covers employer actions (short of dismissal) that cause unjustifiable disadvantage —
e.g., demotion, removal of duties, adverse reference, change in shift patterns, public
humiliation.

Apply the same s 103A objective test to the employer's conduct and procedure.

Common disadvantage scenarios: [VERIFY currency of case law]

- Failure to follow disciplinary process for non-dismissal sanctions
- Removing duties during restructuring without adequate process
- Negative references that go beyond factual accuracy
- Involuntary transfer to a less desirable role

#### 6c. Constructive Dismissal (ERA 2000 s 103(1)(a))

Constructive dismissal occurs where the employer's conduct is so serious that the employee
is entitled to resign and treat themselves as dismissed.

Elements required:

1. Employer's conduct fundamentally breached the employment relationship
2. The employee resigned (or was effectively forced to resign) as a result
3. A reasonable employee in the same position would have done the same

Common bases for constructive dismissal claims in NZ: [VERIFY]

- Sustained workplace bullying or harassment
- Significant HSWA safety breaches left unaddressed
- Significant breach of good faith (e.g., deliberate exclusion, humiliation, salary
  withholding without lawful cause)
- Demotion without consent or justification

#### 6d. Discrimination Personal Grievance (ERA 2000 s 103(1)(d); HRA 1993 s 21)

**Protected grounds (Human Rights Act 1993 s 21):**

| Ground                                  | Notes                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------- |
| Sex (including pregnancy, childbirth)   | Includes parental leave-related adverse action                         |
| Sexual orientation                      |                                                                        |
| Gender identity                         | Recognized as encompassed within sex discrimination                    |
| Age (16+)                               |                                                                        |
| Race, colour, ethnic or national origin |                                                                        |
| Disability                              | Includes mental and physical disability; reasonable accommodation duty |
| Religious belief / ethical belief       |                                                                        |
| Family / marital status                 |                                                                        |
| Employment status                       | Includes casual/part-time status in some circumstances                 |
| Political opinion                       |                                                                        |

**ERA vs. HRA dual-pathway:**

- Discrimination in employment may be brought as an ERA personal grievance (preferred for
  speed and reinstatement remedy) OR as an HRA complaint (broader remedies but slower)
- Both pathways may be available; elect the preferred forum

#### 6e. Sexual Harassment (ERA 2000 ss 103(1)(e)–(f), 108)

**12-month** limitation period (not the standard 90 days).

Elements: (a) request for sexual activity or conduct of a sexual nature; (b) such request
or conduct was either a condition of employment, linked to reward/sanction, or created an
offensive/hostile environment; (c) was unwelcome or offensive.

Employer liability: employer is vicariously liable for sexual harassment by a manager.
For peer harassment, employer liability attaches if the employer knew (or ought to have
known) of the harassment and failed to take reasonable steps to address it.

#### 6f. Restructuring and Redundancy

**Consultation obligations (ERA 2000 s 4 + common law):**

| Step                                         | Required Actions                                                                                                             |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1. Notice of proposed change                 | Inform affected employees (and union if collective agreement applies) of the proposed restructuring and its potential impact |
| 2. Provision of relevant information         | Provide genuinely useful information about the business reason, options considered, and likely timetable                     |
| 3. Opportunity to comment                    | Give employees adequate time to consider and respond — not a rubber-stamp exercise                                           |
| 4. Genuine consideration of feedback         | Consider responses on their merits; document consideration                                                                   |
| 5. Redeployment before redundancy            | Actively consider whether the employee can be redeployed to a suitable alternative role                                      |
| 6. Fair selection process (where applicable) | Where selecting among roles for redundancy, use objective, defensible criteria                                               |
| 7. Final decision and outcome letter         | Communicate the final decision and provide written notice                                                                    |

**Redundancy compensation:**

- **Not statutorily mandated** in NZ (unlike some jurisdictions)
- Contractual redundancy provisions bind the employer
- Good faith may require fair compensation reflecting tenure; failure to offer any compensation
  in long-tenured redundancies may support a PG for unjustifiable disadvantage
- Market practice: 2–4 weeks per year of service (no legislative formula)

**Vulnerable employees (ERA 2000 Schedule 1A):**
Employees in specified service categories (cleaning, caretaking, food catering, orderly
services, hospital workers, airport/aviation, education sector support) have protected
transfer rights when the service is contracted out or transferred:

- Right to **transfer to the new employer** with continuity of service and same terms
- Alternatively, right to **terminate** with notice if they do not wish to transfer
- Employers must notify affected employees before the transfer occurs

### Step 7: Minimum Entitlements Compliance Check

#### 7a. Minimum Wage (Minimum Wage Act 1983) — April 2025 Rates [VERIFY for current year]

| Category                                                                                 | Rate (NZD/hour) |
| ---------------------------------------------------------------------------------------- | --------------- |
| Adult minimum wage (16+, not starting-out/training)                                      | $23.50          |
| Starting-out wage (16–17 yr olds; or ≤6 months continuous service with current employer) | $18.80          |
| Training minimum wage (20+, in 60+ credit/year industry training)                        | $18.80          |

**Common compliance errors:**

- Applying starting-out rate to workers who no longer qualify (over 6 months tenure)
- Applying training rate without verifying qualifying training enrolment
- Failing to update payroll when minimum wage rate changes annually (effective 1 April each year)

**Wage theft criminalisation (effective March 14, 2025):**
Unauthorised deductions from wages and non-payment without reasonable excuse are now
treated as theft under the Crimes Act 1961 (as amended). Ensure wage deductions are
expressly authorised in the employment agreement or by law.

#### 7b. Annual Holidays (Holidays Act 2003 ss 16–43) [VERIFY for Employment Leave Bill reform status]

| Entitlement          | Requirement                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum annual leave | 4 weeks paid per 12 months of continuous employment                                                                                               |
| Timing               | Employer must allow leave to be taken in agreement with employee; cannot be unreasonably withheld                                                 |
| Leave in advance     | Employer may agree to advance leave; recovery provisions apply on termination                                                                     |
| Payment calculation  | The greater of: (a) ordinary weekly pay at the time leave is taken, OR (b) average weekly earnings (AWE) over the 12 months before leave is taken |

**Holidays Act 2003 calculation complexity:**

- The AWE calculation (particularly for variable-hours and irregular-pay employees) has
  caused widespread payroll non-compliance across NZ employers, including major public
  and private sector organisations
- Carry-over and public holiday interaction calculations are a known compliance risk
- **Employment Leave Bill (introduced March 2026):** proposes to replace the current model
  with hours-based accrual from day 1 and 12.5% leave-in-lieu for additional/casual hours
  — monitor for enactment [VERIFY status]

#### 7c. Sick Leave (Holidays Act 2003 ss 63–72A — as amended 2021)

| Entitlement        | Requirement                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum sick leave | 10 days per year (increased from 5 days, effective July 24, 2021)                                                                         |
| Qualifying period  | 6 months continuous employment OR work test (see Step 4d)                                                                                 |
| Carry-over         | Up to 10 unused days carry over to the following year                                                                                     |
| Maximum accrual    | 20 days at any time (10 current year + up to 10 carried over)                                                                             |
| Employee use       | For employee's own illness/injury OR illness/injury of a spouse, partner, dependent child, or dependent member of household               |
| Proof of illness   | Employer may require proof (e.g., medical certificate) if absence ≥3 consecutive days or if employer has reasonable grounds to request it |

#### 7d. Public Holidays (Holidays Act 2003 ss 44–58)

11 statutory public holidays in NZ, including Waitangi Day, ANZAC Day, Christmas Day, and
Boxing Day. Key obligations:

- If a public holiday falls on a day the employee would otherwise work: **paid day off**
- If worked on a public holiday: **time-and-a-half pay + alternative holiday (day in lieu)**
- If a public holiday falls on a day the employee would not otherwise have worked: no entitlement

#### 7e. Rest and Meal Breaks (ERA 2000 ss 69ZD–69ZI)

| Work Period  | Minimum Entitlement                                                      |
| ------------ | ------------------------------------------------------------------------ |
| 2–4 hours    | One 10-minute **paid** rest break                                        |
| 4–6 hours    | One 10-minute **paid** rest break + one 30-minute **unpaid** meal break  |
| 6–8 hours    | Two 10-minute **paid** rest breaks + one 30-minute **unpaid** meal break |
| Over 8 hours | Additional paid rest break for each further 4-hour block                 |

- Breaks must be spread **evenly** across the work period
- Employer may not substitute additional pay for breaks (except in very narrow essential
  service exemptions)
- Employer and employee may agree on timing but not on elimination of entitlement

#### 7f. KiwiSaver Employer Obligations (KiwiSaver Act 2006)

| Obligation                                      | Requirement                                                                                       |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Minimum employer contribution                   | 3% of employee's **gross salary/wages** per pay period                                            |
| Employee auto-enrolment                         | Employees aged 18–65 auto-enrolled unless opt-out occurs within 2–8 weeks of starting             |
| ESCT (Employer Superannuation Contribution Tax) | Withheld from employer contribution before remitting to IRD; rate depends on employee income band |
| Record retention                                | KiwiSaver records retained for minimum 7 years                                                    |
| Contribution base                               | Gross ordinary time earnings (not superannuation, redundancy payments, or reimbursements)         |
| Penalties                                       | Late/missed contributions: NZD $50/month (small employers); NZD $250/month (large employers)      |

#### 7g. Parental Leave (PLEP Act 1987)

| Leave Type                                    | Duration                         | Eligibility                           | Payment                                                                |
| --------------------------------------------- | -------------------------------- | ------------------------------------- | ---------------------------------------------------------------------- |
| Primary carer leave                           | 26 weeks                         | 6-month or 12-month qualifying period | Government-funded up to NZD $754.87 gross/week (2024–25 rate [VERIFY]) |
| Extended leave (secondary carer / additional) | Further 26 weeks unpaid          | 12-month qualifying period            | Unpaid                                                                 |
| Partner/paternity leave                       | 2 weeks                          | 6-month qualifying period             | Government-funded; partner rate                                        |
| Keeping-in-touch (KIT) days                   | Up to 64 hrs during leave period | By agreement                          | Normal pay for KIT work                                                |

**Employment protection:** Return to same or equivalent role is protected. Dismissal or
redundancy of an employee on parental leave is presumed to be connected to the leave
unless the employer can prove otherwise.

### Step 8: Secondary Statute Checks

#### 8a. Health and Safety at Work Act 2015 (HSWA) — Employment Intersection

HSWA imposes duties on the PCBU (person conducting a business or undertaking) that
interact with employment relations in key scenarios:

| Scenario                                | HSWA Obligation                                                             | ERA Implication                                                       |
| --------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Employee dismissed for health condition | Employer must have considered reasonable accommodation before dismissal     | Failure to accommodate supports unjustified dismissal PG              |
| Employee raising safety concerns        | PCBU must not take adverse action against a worker for raising H&S concerns | Adverse action is unjustifiable disadvantage under ERA                |
| Workplace bullying                      | PCBU must manage psychosocial hazards                                       | Failure to act supports PG for disadvantage or constructive dismissal |
| Fitness for work assessment             | Must be conducted fairly and with employee consent                          | Privacy Act 2020 and good faith obligations apply                     |

PCBU obligations under HSWA (so far as reasonably practicable):

- Provide and maintain safe work environment, plant, and systems
- Provide adequate facilities for worker welfare
- Monitor health and workplace conditions
- Provide information, training, instruction, and supervision

#### 8b. Human Rights Act 1993 — Employment Discrimination

Discrimination in employment is prohibited under HRA 1993 ss 22–35. Covers hiring,
conditions, pay, promotion, training, transfer, demotion, and dismissal.

**Dual pathway note:** A discrimination PG under ERA s 103(1)(d) is processed through
ERA/Employment Court. A separate HRA complaint may be made to the Human Rights Commission;
if unresolved, proceeds to Human Rights Review Tribunal. Choose the preferred pathway
(or both where permitted) based on remedies sought and urgency.

**Reasonable accommodation:**

- For disability and religious/ethical belief grounds, employer must provide reasonable
  accommodation unless it causes **unjustifiable hardship** to the employer
- Failure to accommodate supports both an HRA complaint and an ERA disadvantage PG

#### 8c. Privacy Act 2020 — Employment Applications

**Employee monitoring and surveillance:**

- Employers may monitor workplace activity (cameras, computer/network monitoring, email)
  but must:
  1. Collect only for a **lawful purpose** connected to employment
  2. Notify employees of monitoring in a reasonably practicable way
  3. Keep data **no longer than necessary**
  4. Ensure proportionality — no excessive or covert surveillance without justification

**Reference checks and pre-employment screening:**

- Must be limited to information reasonably necessary for the employment decision
- Health information (medical records, criminal history) collected only for legitimate purpose
- Employee has right to access and correct personal information held by the employer

**Privacy breaches in disciplinary proceedings:**

- Sharing disciplinary or health information without consent may amount to a privacy
  interference actionable before the Privacy Commissioner or Human Rights Review Tribunal
- A Privacy Act 2020 breach in a dismissal process does not itself void the dismissal, but
  may support a disadvantage PG or provide leverage in settlement negotiations

#### 8d. Contractor vs. Employee Classification (ERA 2000 s 6 + 2024 Contractor Gateway Test)

NZ retains the statutory test under ERA s 6: employment status determined by the **real
nature** of the relationship (not just how the contract labels it). Factors include:

- Level of control and direction
- Integration into the business
- Economic dependence
- Requirement to provide equipment

**2024 Contractor Gateway Test (contractor status protected if ALL 5 apply):**

1. Written agreement specifying the person is engaged as an **independent contractor**
2. Person is **free to work for others** while providing services
3. Person is **free to accept or decline specific engagements**
4. **Remuneration is not** based solely on time worked
5. Person provides **services to multiple clients** in the relevant period

If ANY gateway condition fails, the real-nature test under s 6 reverts as the primary
test. Misclassification as a contractor when the person is an employee exposes the
employer to liability for all minimum entitlements (back-pay for Holidays Act, KiwiSaver,
minimum wage shortfalls, plus interest).

### Step 9: ERA and Employment Court Proceedings

#### 9a. Dispute Resolution Pathway

```
Problem arises
     ↓
Raise PG with employer (within 90 days for most PG types)
     ↓
Employer responds / attempts resolution (good faith requires genuine effort)
     ↓
Employment Mediation Services (free; confidential; voluntary but strongly encouraged)
     ↓ (if unresolved)
Employment Relations Authority (ERA) — formal investigation
     ↓ (if appealing or on questions of law)
Employment Court — de novo appeal or direct referral
     ↓
Court of Appeal (questions of law only)
```

#### 9b. Employment Relations Authority (ERA)

- Independent tribunal; adjudicates unresolved employment relationship problems
- Inquisitorial process — Authority investigates and makes a determination
- Hearings are less formal than Court but evidence and submissions are required
- **Jurisdiction:** Personal grievances, wages/holiday disputes, breach of employment
  agreement, good faith penalties, breach of collective agreement

**Remedies available from ERA:**

- Compensation (lost wages, humiliation, loss of dignity, injury to feelings)
- Reinstatement (primary remedy for unjustified dismissal if practicable and reasonable)
- Declaration
- Penalty for good faith breach (up to NZD $20,000 per breach for companies)
- Injunction (limited circumstances)

**Note on compensation for humiliation, loss of dignity, injury to feelings:**
Historically capped but amounts increasing — NZD $25,000–$50,000 for serious cases is now
regularly awarded; exceptional cases exceed this. [VERIFY current ceiling guidance]

#### 9c. Employment Court

- Primary appeal body from ERA determinations (28 days to file)
- Also has original jurisdiction for certain matters (industrial action, injunctions,
  declarations on employment status)
- De novo appeal means evidence is reheard (not just a review of the ERA record)
- Higher standard of legal argument required

#### 9d. Mediation

- Provided by the Ministry of Business, Innovation and Employment (MBIE)
- Free of charge
- Confidential — statements in mediation are inadmissible in ERA proceedings
- Settlement reached in mediation is enforceable as an ERA consent order
- Parties are strongly encouraged (but not strictly compelled) to attempt mediation before
  lodging with ERA
- ERA may decline to investigate if mediation has not been attempted (ERA s 159(7))

#### 9e. Pay Secrecy Protections (August 26, 2025)

Under the Employment Relations (Employee Remuneration Disclosure) Amendment Act 2025,
employers must not take adverse action against an employee for:

- Discussing their own remuneration with a colleague
- Comparing pay with other employees
- Requesting pay transparency from the employer

An employer who takes adverse action in response to pay disclosure discussions commits
an unjustifiable disadvantage under ERA s 103.

---

## Severity and Risk Classification

Apply this three-tier classification to each issue identified:

### 🔴 NON-COMPLIANT — Active Legal Exposure

The issue represents a clear statutory breach or strong arguable personal grievance.
Immediate remediation or legal advice required.

**Examples:**

- Personal grievance raised within 90 days; dismissal lacked substantive and/or procedural
  justification
- Trial period clause invalid (not signed before work; vague period stated; employee
  previously worked for employer)
- Employee paid below minimum wage for category
- KiwiSaver employer contributions not made
- Redundancy selected employee not consulted
- Vulnerable employee not given transfer rights
- Dismissal of employee on parental leave (rebuttable presumption of connection)
- Wage deduction without express authorisation (now potentially criminal — Wage Theft Act 2025)

### 🟡 AT RISK — Material Procedural Gap or Arguable Claim

The issue involves a procedural gap, ambiguous clause, or scenario where an employment
claim is arguable but not certain. Remediation is strongly recommended.

**Examples:**

- Dismissal procedure partially followed but missing key steps (e.g., no written outcome)
- 90-day trial dismissal where employee had only brief time to consider agreement
- Restructuring consultation occurred but depth of information provided may be challenged
- Restraint of trade clause potentially overbroad for the employee's actual role
- Privacy Act breach in disciplinary process (no consent for sharing health data)
- No garden leave clause but employer directing employee to stay home on notice
- Holidays Act calculation not recently audited for variable-hours workers
- Discrimination risk where performance management disproportionately affected an employee
  with a protected characteristic

### 🟢 COMPLIANT — No Apparent Exposure

The relevant obligation is met, or the issue is not applicable to this employment
situation.

**Examples:**

- Personal grievance raised more than 90 days after the event; claim likely time-barred
- Trial period clause valid on its face, properly signed before commencement
- Minimum wage correctly calculated and current rate applied
- Consultation process well-documented with genuine engagement

---

## Prioritisation Framework

When multiple issues are identified, address in this order:

| Tier         | Issue Types                                                                                                                        | Action                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Critical** | Active personal grievance within time limit; statutory breach with immediate penalty exposure; wage theft risk; illegal deductions | Address before ERA lodgement; seek legal advice immediately |
| **High**     | Arguable PG or good faith breach; Holidays Act calculation errors; KiwiSaver non-payment                                           | Remediate within 30 days; review payroll and consult        |
| **Medium**   | Procedural gaps in disciplinary records; questionable restraint clauses; IEA content missing optional-but-recommended provisions   | Remediate at next review cycle                              |
| **Low**      | Documentation improvements; monitoring policy updates; keeping-in-touch day policy absence                                         | Address in annual HR compliance audit                       |

---

## Citation Quality Gates

Run these 5 gates before delivering any statutory or case law citation. If any gate fails,
revise or flag before delivering.

| Gate           | Rule                                                                                                                                                                                    | Fail Action                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **Source**     | Every legal claim cites a specific section of ERA, HA 2003, HRA 1993, or another NZ statute                                                                                             | Add citation or mark "[UNVERIFIED]"     |
| **Format**     | Citations use standard NZ statutory format: "ERA 2000 s 103A", "HA 2003 s 16", "HRA 1993 s 21"                                                                                          | Fix format                              |
| **Currency**   | Statutory provisions checked for 2024–2026 amendments (trial period expansion Dec 2023; high-income threshold Feb 2026; sick leave 2021; Wage Theft Act Mar 2025; pay secrecy Aug 2025) | Flag "[CHECK CURRENCY]"                 |
| **Domain**     | Analysis stays within NZ employment law — no bleed of UK, Australian, or US employment concepts                                                                                         | Remove or flag cross-jurisdiction bleed |
| **Confidence** | Uncertainty (especially on case law) explicitly stated; no fabricated citations                                                                                                         | Add confidence qualifier or "[VERIFY]"  |

---

## Self-Interrogation for NON-COMPLIANT Classifications

For any issue classified as NON-COMPLIANT, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:** Does the NON-COMPLIANT classification follow logically
from the cited statutory provision and the facts? Would the ERA or Employment Court actually
reach this conclusion on these facts?

**Pass 2 — Completeness:** Have all defences and mitigating factors been considered? For
example: Was the trial period clause actually invalid, or was it merely informal? Did the
employer have an arguable business justification? Is a time bar available?

**Pass 3 — Challenge:** What is the strongest argument for the employer (if advising
employee) or employee (if advising employer) that this is not NON-COMPLIANT? Under what
circumstances might a reasonable ERA authority member reach a different conclusion?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                          | Action                                           |
| ------------ | --------- | ---------------------------------------------------------------- | ------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled NZ statute; clear and unambiguous provision              | State with confidence                            |
| **High**     | 0.80–0.94 | Strong statutory authority; minor interpretive questions         | State with brief caveat                          |
| **Probable** | 0.60–0.79 | Good arguments on the facts; outcome could differ on other facts | State with reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; case law developing or unresolved           | Flag for professional advice; present both sides |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative; no clear statutory or case law anchor | Do not assert; mark "[UNCERTAIN]"                |

**NZ employment law confidence anchors:**

- _Definite_: 90-day PG time limit (ERA s 114); 4-week annual leave minimum (HA 2003 s 16);
  KiwiSaver 3% minimum contribution; adult minimum wage rate
- _High_: Trial period requirements (ERA s 67A); high-income threshold (ERA s 103 — Feb
  2026 reform); garden leave requires express contractual provision
- _Probable_: Whether restructuring consultation was sufficient on the specific facts;
  whether a restraint of trade is reasonable; constructive dismissal elements on unusual facts
- _Possible_: Remedies quantum in novel harassment cases; application of contractor
  gateway test to atypical arrangements
- _Unlikely_: Predicting precise ERA compensation award; applying speculative future case law

---

## Anti-Patterns

What NOT to do when analysing NZ employment law:

1. **Treating the 90-day trial period as an absolute defence.** A valid trial period bars
   an unjustified _dismissal_ PG, but the employee can still raise PGs for discrimination,
   harassment, minimum entitlement breaches, and HSWA violations during the trial period.
   A valid trial period is not a blanket immunity clause.

2. **Using vague duration language in trial period clauses.** "Three months" or "the first
   quarter of employment" fails the ERA s 67A requirement for an exact number of days.
   Invalid clauses expose the employer to unjustified dismissal claims even if the dismissal
   was substantively fair.

3. **Failing to sign the employment agreement before day 1.** The most common trial period
   invalidity. Sending the agreement on the morning the employee starts, or after the employee
   has already commenced work, invalidates the trial period regardless of other compliance.

4. **Treating the 90-day personal grievance limit as the lodgement deadline.** The 90-day
   deadline is to _raise_ the PG with the _employer_, not to lodge with the ERA. The ERA
   lodgement deadline is 3 years from the date the PG was raised with the employer. Advising
   an employee that they are out of time because it has been more than 90 days since
   termination (without checking whether the PG was raised with the employer) is an error.

5. **Assuming good faith consultation is a rubber-stamp.** "We told them, they responded,
   we proceeded" is not sufficient. Genuine consultation requires that employee input be
   capable of influencing the outcome. If the decision was final before consultation began,
   good faith has been breached regardless of the process followed.

6. **Overlooking redeployment before redundancy.** NZ good faith obligations require
   genuine consideration of redeployment alternatives. Failure to identify and offer suitable
   alternative roles before selecting redundancy is a common basis for PG success even
   where the redundancy is otherwise genuine.

7. **Applying the starting-out wage beyond the eligibility window.** The starting-out wage
   applies to 16–17-year-olds _and_ to employees in their first 6 months of continuous
   service with a particular employer. After 6 months, the adult minimum wage applies.
   Continuing to apply the starting-out rate after the 6-month threshold is a statutory
   breach.

8. **Confusing restraints of trade with confidentiality obligations.** Confidentiality
   clauses protect specific confidential information and are generally enforceable. Restraints
   of trade prohibit competing or soliciting clients/employees and must satisfy the
   reasonableness test (legitimate interest + no wider than necessary). Treating an overbroad
   non-compete as enforceable because it is labelled "confidentiality" is an error.

9. **Directing garden leave without an express contractual provision.** NZ employers have
   no automatic right to withhold work from an employee on notice. Without an express garden
   leave clause, sending an employee home during their notice period may constitute a breach
   of contract (and potentially unjustifiable disadvantage). Always check the employment
   agreement for an express garden leave term before directing a departing employee to stay home.

10. **Ignoring the Privacy Act 2020 in dismissal processes.** Sharing an employee's health
    information, disciplinary records, or personal data without consent in the course of a
    disciplinary process (e.g., disclosing the reason for dismissal to other staff) may
    constitute a privacy interference. While a PA 2020 breach does not void a dismissal, it
    can be used as leverage in ERA proceedings and may attract separate complaints to the
    Privacy Commissioner.

11. **Assuming the high-income threshold (NZD $200,000+) exempts all personal grievance
    types.** The February 2026 reform bars only _unjustified dismissal_ PGs for high-income
    employees. Claims for unjustifiable disadvantage, discrimination, harassment, minimum
    entitlement breaches, and good faith violations remain available regardless of salary.

12. **Failing to track Holidays Act calculation methodology for variable-hours employees.**
    The HA 2003 AWE calculation is notoriously complex for employees with irregular hours,
    variable bonus pay, or commissions. Many large NZ employers have faced significant
    back-pay liabilities due to systematic underpayment. Employers with non-standard pay
    structures should conduct regular Holidays Act audits — not just at termination.

13. **Treating vulnerable employee protections as optional in outsourcing or sale-of-business
    transactions.** ERA Schedule 1A creates mandatory transfer rights for employees in
    specified service categories. Failing to notify and offer transfer to eligible vulnerable
    employees before the service transfer is a statutory breach, not merely a best practice.

14. **Not checking whether triangular employment applies in labour-hire or secondment
    arrangements.** Since the 2020 ERA amendments, an employee placed by a labour-hire
    agency or seconded to a host business can bring PG claims against _either_ the employer
    _or_ the controlling third party. The host business is exposed to PG liability even
    though it is not the direct employer.

15. **Ignoring KiwiSaver ESCT in payroll modelling.** The 3% employer KiwiSaver
    contribution is subject to ESCT (Employer Superannuation Contribution Tax) before
    remittance to IRD. The ESCT rate depends on the employee's income band. Treating the
    3% contribution as a net cost without accounting for ESCT produces incorrect payroll
    calculations and potential underpayment to the employee's KiwiSaver account.

16. **Assuming conduct during mediation is usable in ERA proceedings.** Statements,
    admissions, and settlement offers made during Employment Mediation Services proceedings
    are confidential and inadmissible in ERA hearings. Quoting from mediation in ERA
    submissions is prohibited and may invite sanctions.

17. **Overlooking wage theft criminalisation as a changed compliance threshold.** The Crimes
    (Theft by Employer) Amendment Act 2025 (effective March 14, 2025) elevates wage
    non-payment from a civil employment matter to a potential criminal offence. Deductions
    without express authorisation and deliberate non-payment of wages are no longer merely
    ERA violations. Compliance advice pre-March 2025 may be outdated on this point.

---

## Writing Standards

Before delivering any output under this skill, apply these quality gates:

1. **Name the statute and section**: not "the Act says" — write "ERA 2000 s 103A" or
   "HA 2003 s 16"
2. **Use NZ legal terminology**: "personal grievance", "unjustifiable disadvantage",
   "Employment Relations Authority", "PCBU", "ERA" — not UK/Australian equivalents
3. **Distinguish advice perspectives**: always identify whether the analysis is employer-
   facing (risk mitigation) or employee-facing (enforcement and remedies)
4. **Flag uncertainty explicitly**: where case law is developing or quantum is uncertain,
   say so — do not confabulate precise dollar figures for ERA compensation awards
5. **Check time limits first**: always verify whether the PG time limit is still open
   before analysing the merits of a claim
6. **Plain language with technical accuracy**: "the employer must have a genuine reason
   for dismissal and must follow a fair process" is better than "the substantive and
   procedural elements of s 103A require..."
7. **Mark unverified citations**: all statutory references to rate figures, compensation
   amounts, and penalty maxima should be marked [VERIFY] if sourced from memory rather
   than live authoritative sources

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal authority
source.

**With legalcode-mcp connected (preferred):**

- Search for current ERA 2000 amendments, Holidays Act 2003 reform status, and recent
  Employment Court and ERA determinations on the relevant topic
- Verify current minimum wage rates, KiwiSaver contribution rates, and parental leave
  payment maxima
- Look up recent Employment Court decisions on the specific ground (e.g., unjustified
  dismissal, constructive dismissal, discrimination)
- Save the 5–10 most relevant cases and statutory provisions to a local reference file:
  `/tmp/legalcode-nz-employment-research.md`
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all specific rate figures, compensation amounts, and case citations with [VERIFY]
- Rely on the statutory framework in this skill for the analytical structure
- Direct the user to verify current rates at employment.govt.nz and current legislation
  at legislation.govt.nz
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

**Authoritative NZ sources to reference users to:**

- legislation.govt.nz — Acts and regulations
- employment.govt.nz — MBIE guidance and tools
- era.govt.nz — Employment Relations Authority decisions
- employmentcourt.govt.nz — Employment Court judgments
- worksafe.govt.nz — HSWA guidance

---

## Output Format Template

Deliver the analysis in the following structure. Adapt sections to the matter type.

```markdown
# NZ Employment Relations Analysis

**Matter type:** [Dismissal / Compliance / Agreement Review / etc.]
**Perspective:** [Employer / Employee / Neutral]
**Key dates:** [Employment start; Event date; PG raised date (if applicable)]
**Primary statute(s):** [ERA 2000; HA 2003; HRA 1993; etc.]

---

## Threshold Assessment

| Threshold             | Finding                                | Implication                                       |
| --------------------- | -------------------------------------- | ------------------------------------------------- |
| PG time limit         | [Within 90 days / Expired / Uncertain] | [Claim available / Time-barred / Check extension] |
| Trial period validity | [Valid / Invalid / Not applicable]     | [Bars dismissal PG / No bar / N/A]                |
| High-income threshold | [Applies / Does not apply]             | [Dismissal PG barred / Available]                 |
| Qualifying period     | [Met / Not met / N/A]                  | [Entitlement available / Not yet accrued / N/A]   |

---

## Key Findings

### 🔴 NON-COMPLIANT Issues

**[Issue 1 title]**

- **Statutory basis:** [ERA 2000 s XX / HA 2003 s XX]
- **Facts:** [What the employer/employee did or failed to do]
- **Legal analysis:** [Why this is non-compliant]
- **Risk:** [Likely outcome if challenged; estimated exposure]
- **Recommended action:** [What must happen now]

### 🟡 AT RISK Issues

**[Issue 2 title]**

- **Statutory basis:** [ERA 2000 s XX]
- **Facts:** [What the employer/employee did or failed to do]
- **Legal analysis:** [Why this creates exposure]
- **Risk:** [Outcome if challenged; estimated exposure range]
- **Recommended action:** [What should happen]

### 🟢 COMPLIANT Items

- [Item 1]: [Brief note confirming compliance]
- [Item 2]: [Brief note confirming compliance]

---

## Prioritised Action List

| Priority | Action   | Deadline                      | Owner                         |
| -------- | -------- | ----------------------------- | ----------------------------- |
| Critical | [Action] | [Date / Before ERA lodgement] | [Employer / Employee counsel] |
| High     | [Action] | [Within 30 days]              | [HR / Legal]                  |
| Medium   | [Action] | [Next review cycle]           | [HR]                          |
| Low      | [Action] | [Annual audit]                | [HR]                          |

---

## Remedies Assessment (if applicable)

| Remedy                                  | Availability                                     | Notes                                                 |
| --------------------------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| Reinstatement                           | [Primary remedy — if practicable and reasonable] | [Any obstacles to reinstatement?]                     |
| Lost wages compensation                 | [Available if dismissal unjustified]             | [Estimated period; mitigation obligation applies]     |
| Humiliation/distress compensation       | [Available; quantum varies]                      | [Range: NZD XX,000–XX,000 based on severity [VERIFY]] |
| Good faith penalty                      | [If standalone s 4 breach]                       | [Up to NZD $20,000 per breach for companies]          |
| Back-pay for minimum entitlement breach | [Statutory; plus interest]                       | [Period of underpayment]                              |

---

## Limitations and Notes

- [Any scope limitations: e.g., "This analysis is based on facts as provided — documentary
  review of the employment agreement and disciplinary correspondence would be required
  before lodging with ERA"]
- [Any areas of genuine legal uncertainty marked with [UNCERTAIN] or [VERIFY]]
- [Recommended next steps: seek specialist employment lawyer, MBIE mediation, etc.]

---
```

_Glass Box audit trail appended below._

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-nz-employment-relations"
  analysis_date: "[ISO 8601 date]"
  mode: "Created from scratch — Legalcode original"
  jurisdiction: "New Zealand"
  perspective: "[Employer / Employee / Neutral]"
  matter_type: "[Dismissal / Compliance audit / Agreement review / etc.]"
  primary_statutes:
    - "Employment Relations Act 2000"
    - "Holidays Act 2003"
    - "[Other statutes engaged]"
  threshold_findings:
    pg_time_limit: "[Within limit / Expired / Not applicable]"
    trial_period_valid: "[Valid / Invalid / Not applicable]"
    high_income_threshold: "[Applies / Does not apply]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-nz-employment-research.md / Not created]"
  citations_verified: "[Number VERIFIED] / [Number UNVERIFIED — marked [VERIFY]]"
  findings_summary:
    non_compliant: "[Count]"
    at_risk: "[Count]"
    compliant: "[Count]"
  confidence: "[HIGH / MEDIUM / LOW] — [brief rationale]"
  key_statutes_cited:
    - "ERA 2000 s [XX]: [VERIFIED / UNVERIFIED]"
    - "HA 2003 s [XX]: [VERIFIED / UNVERIFIED]"
  pending_legal_developments:
    - "Employment Leave Bill (introduced March 2026) — Holidays Act reform pending enactment [VERIFY]"
    - "[Any other pending reforms noted in the analysis]"
  limitations:
    - "[Scope limitations or fact gaps]"
    - "All statutory rate figures should be verified at employment.govt.nz before reliance"
    - "Case law citations require verification at era.govt.nz and employmentcourt.govt.nz"
  reviewer: "AI-assisted — requires review by a qualified NZ employment lawyer before reliance"
```

---

## Localization Notes

This skill is jurisdiction-specific to **New Zealand** and should not be applied to
Australian, UK, or other employment law contexts. Key NZ distinctions:

- **No general statutory redundancy payment**: Unlike Australia (NES redundancy pay) and
  the UK (statutory redundancy pay), NZ has no statutory formula for redundancy
  compensation. Good faith requires fair treatment, but the quantum is contractual or
  discretionary.
- **Unique ACC accident compensation bar**: All work-related personal injury claims are
  channelled through ACC (Accident Compensation Act 2001). Tort-based personal injury
  claims are effectively barred. Employment law covers the employment relationship aspects
  of workplace injuries (e.g., whether a health-related dismissal was unjustified).
- **No mandatory notice periods in statute**: Notice periods are contractual. If the
  employment agreement is silent, reasonable notice is implied. The ERA imposes no minimum
  statutory notice period (unlike UK's ERA 1996 s 86).
- **Inquisitorial ERA process**: Unlike adversarial UK employment tribunals, the ERA
  conducts its own investigation. Parties submit information and the ERA determines the
  facts and outcome — a significant procedural difference from UK/Australian processes.
- **Good faith as a pervasive standard**: NZ's ERA 2000 s 4 good faith obligation is
  broader and more demanding than good faith duties in most comparable jurisdictions. It
  is an active, substantive duty — not merely a requirement to act honestly.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep web research (NZ
legislation, Employment Court decisions, MBIE guidance, ERA determinations) and structural
patterns from the Legalcode skill reference standard (legalcode-contract-review) and
legalcode-de-kuendigungsschutz comparative patterns. Covers the Employment Relations Act
2000 as amended through February 2026, including the 90-day trial period expansion (December
2023), high-income dismissal threshold (February 2026), pay secrecy protections (August 2025),
and wage theft criminalisation (March 2025). Also covers Holidays Act 2003 (with 2021 sick
leave amendment and 2026 Employment Leave Bill), Minimum Wage Act 1983, PLEP Act 1987,
HSWA 2015, HRA 1993, Privacy Act 2020, and KiwiSaver Act 2006. Attribution: Legalcode
original synthesis.
