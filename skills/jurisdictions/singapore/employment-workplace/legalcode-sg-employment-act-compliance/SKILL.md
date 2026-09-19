---
name: legalcode-sg-employment-act-compliance
description: Assess Singapore Employment Act (Cap. 91) compliance for employers and employees. Covers
  scope and coverage thresholds, Part IV protections (hours, overtime, rest days), salary payment and
  itemised payslip obligations, leave entitlements (annual, sick, maternity, paternity, shared parental,
  childcare), notice periods, termination and wrongful dismissal, retrenchment notification, MOM enforcement,
  Employment Claims Tribunals (ECT), TADM mediation, National Wages Council guidelines, tripartite guidelines
  on flexible work arrangements, and Workplace Fairness Act 2025. Use when auditing employment practices
  in Singapore, reviewing employment contracts for EA compliance, advising on employee rights or employer
  obligations under Singapore law, or preparing for a Ministry of Manpower inspection. Covers the 2019
  major amendments (PME coverage expansion), Platform Workers Act 2024, Workplace Fairness Act 2025, and
  the April 2025 paternity/shared parental leave increases.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Singapore Employment Act Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted compliance assessment
> under the Singapore Employment Act (Cap. 91) and related legislation. It does not
> constitute legal advice. All outputs should be reviewed by a qualified Singapore-licensed
> employment lawyer before reliance. Laws change frequently; verify current provisions
> against Singapore Statutes Online (sso.agc.gov.sg) and MOM guidance (mom.gov.sg) before
> acting. Statutory and regulatory references carry hallucination risk — verify every
> citation against authoritative sources.

---

## Purpose and Scope

This skill assesses compliance with the Singapore Employment Act 1968 (Cap. 91, "EA") and
its surrounding statutory ecosystem for employers in Singapore.

**Covers:**

- EA scope and coverage analysis (Part IV vs. core provisions; PME thresholds)
- Salary payment obligations, permissible deductions, and itemised payslip requirements
- Part IV protections: hours of work, overtime calculation, rest day entitlements
- Leave entitlements: annual, sick, maternity, paternity, shared parental, childcare
- Notice periods, termination grounds, and wrongful dismissal exposure
- Retrenchment obligations and MOM notification requirements
- Employment Claims Tribunals (ECT) and TADM mediation procedure
- National Wages Council (NWC) 2024/2025 wage guidelines
- Tripartite Guidelines on Flexible Work Arrangement (FWA) requests (effective 1 Dec 2024)
- Workplace Fairness Act 2025 (Workplace Fairness Bill passed 8 January 2025)
- Platform Workers Act 2024 (effective 1 January 2025)

**Does not:**

- Provide legal advice or replace Singapore-qualified employment counsel
- Cover public sector employees (governed by separate legislation)
- Cover domestic workers (Employment of Foreign Manpower Act)
- Cover seafarers (Merchant Shipping Act)
- Perform CPF contribution rate calculations (use CPF Board calculator)
- Address income tax obligations (consult IRAS)

---

## Jurisdiction and Governing Law

**Jurisdiction**: Singapore (Republic of Singapore)
**Legal system**: Common law (inherited from English law, adapted by statute)
**Primary legislation**:

- Employment Act 1968 (Cap. 91) — principal statute
- Employment Claims Act 2016 — ECT jurisdiction and procedure
- Child Development Co-Savings Act 2001 (Cap. 38A) — maternity and paternity leave
- Employment of Foreign Manpower Act 1990 (Cap. 91A) — foreign workers
- Workplace Safety and Health Act 2006 (Cap. 354A)
- Workplace Fairness Act 2025 (not yet in force; Royal Assent 8 Jan 2025; commencement TBC)
- Platform Workers Act 2024 (effective 1 January 2025)
- Central Provident Fund Act 1953 (Cap. 36) — CPF contributions

**Authoritative sources**:

- Singapore Statutes Online: sso.agc.gov.sg
- Ministry of Manpower: mom.gov.sg
- Employment Claims Tribunals: judiciary.gov.sg/civil/employment-claims
- Tripartite Alliance for Dispute Management (TADM): tal.sg/tadm

---

## Key Legislative Framework

### The 2019 Amendment — Landmark Coverage Expansion

The Employment (Amendment) Act 2019 (effective 1 April 2019) was a landmark reform:

- Extended EA core provisions to **all employees** (removed the S$4,500 salary ceiling for
  basic protections)
- Approximately 430,000 additional Professionals, Managers and Executives (PMEs) gained
  Employment Act protection for the first time
- Expanded wrongful dismissal remedy to all EA-covered employees (previously only available
  to workmen and lower-paid non-workmen)

### Part IV Coverage Thresholds (Hours, Overtime, Rest Days)

Part IV of the EA (working hours, overtime, rest days) applies only to:

| Employee Type                               | Basic Monthly Salary Cap                         |
| ------------------------------------------- | ------------------------------------------------ |
| **Workmen** (manual labour)                 | Up to **S$4,500/month**                          |
| **Non-workmen** (non-manual, rank-and-file) | Up to **S$2,600/month**                          |
| Managers and Executives                     | **Excluded from Part IV** (regardless of salary) |

> [VERIFY] The "non-workmen" threshold of S$2,600 as at March 2026. MOM periodically revises
> these thresholds; confirm current figures at mom.gov.sg before advising.

### 2024–2025 Key Legislative Developments

| Development               | Effective Date        | Impact                                                                                              |
| ------------------------- | --------------------- | --------------------------------------------------------------------------------------------------- |
| Platform Workers Act 2024 | 1 January 2025        | Platform operators liable for work injury compensation for delivery riders and private hire drivers |
| Workplace Fairness Bill   | Passed 8 January 2025 | Statutory anti-discrimination framework; commencement date TBC                                      |
| Paternity leave doubled   | 1 April 2025          | Mandatory paternity leave increased from 2 weeks to 4 weeks                                         |
| Shared parental leave     | 1 April 2025          | 6 weeks shared parental leave introduced (increasing to 10 weeks April 2026)                        |
| FWA Tripartite Guidelines | 1 December 2024       | Employers must have fair process for flexible work arrangement requests                             |
| Workplace safety fines    | 1 June 2024           | Maximum monetary fines for safety breaches raised from S$20,000 to S$50,000                         |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the scope of the compliance assessment
- The employee's coverage tier (Part IV vs. core provisions only) is unclear
- Whether the entity is an employer or employee perspective matters
- The assessment involves complex scenarios (e.g., retrenchment, wrongful dismissal)

Use the structured option pattern wherever marked with **⟁ CLARIFY** below. Skip questions
already answered by the user's initial context.

---

## Workflow

### Step 1: Accept Input

Accept the compliance assessment request in any of these forms:

- **Employment contract**: PDF, DOCX, or pasted text for review against EA requirements
- **HR policy document**: Leave policy, salary policy, disciplinary procedure, etc.
- **Employer audit request**: Assess an employer's overall EA compliance posture
- **Employee rights enquiry**: Determine an employee's entitlements or rights
- **Specific issue**: A targeted question (e.g., "is our overtime policy compliant?")
- **Termination / retrenchment scenario**: Assess compliance with termination obligations

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions (skip any already answered):

1. **Perspective**: Who is the user?
   - Options: **Employer** (assessing compliance posture), **Employee** (understanding rights),
     **HR professional**, **Legal counsel**, **Other**
   - _Why this matters_: Employer perspective focuses on obligations and risk; employee
     perspective focuses on entitlements and remedies.

2. **Employee type**: What type of employee is involved?
   - Options: **Workmen** (manual labour, e.g., factory worker, delivery driver), **Non-workman
     rank-and-file** (non-manual, non-manager), **Professional/Manager/Executive (PME)**,
     **Foreign worker on Employment Pass/S Pass/Work Permit**, **Platform worker**
   - _Why this matters_: Determines whether Part IV protections apply and which statutory
     entitlements are in scope.

3. **Salary level**: What is the employee's basic monthly salary?
   - _Why this matters_: Determines Part IV coverage thresholds (S$4,500 for workmen;
     S$2,600 for non-workmen) and overtime rate calculation caps.

4. **Issue area**: What is the primary focus?
   - Options: **Full compliance audit**, **Salary and payroll**, **Hours and overtime**,
     **Leave entitlements**, **Termination or wrongful dismissal**, **Retrenchment**,
     **FWA requests**, **Workplace fairness/discrimination**
   - Allow multiple selections.
   - _Why this matters_: Scopes the analysis to the most material areas.

5. **Organisation size**: Number of employees?
   - _Why this matters_: Retrenchment notification threshold applies to employers with
     10+ employees retrenching 5+ employees in a 6-month period.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly. Do not silently assume a coverage tier.

### Step 3: Determine EA Coverage Tier

Before assessing compliance, establish which tier of EA protection applies.

**Coverage Analysis:**

```
Tier 1 — FULL EA PROTECTION (Core + Part IV):
  - Workmen with basic monthly salary ≤ S$4,500
  - Non-workmen with basic monthly salary ≤ S$2,600

Tier 2 — CORE PROTECTION ONLY (No Part IV):
  - All other employees under a contract of service
  - PMEs regardless of salary (post-April 2019)
  - Workmen earning > S$4,500
  - Non-workmen earning > S$2,600

Tier 3 — EXCLUDED (EA does not apply):
  - Public servants
  - Domestic workers (Employment of Foreign Manpower Act applies)
  - Seafarers (Merchant Shipping Act applies)
  - Self-employed contractors (no contract of service)
```

**⟁ CLARIFY** — If coverage tier is genuinely ambiguous (e.g., worker claims to be a
contractor but facts suggest employment), ask:

- "The worker appears to be engaged as an independent contractor. Does the engagement
  exhibit employment indicators? (Control over how work is done, integration into
  business, exclusive engagement, provision of equipment) If so, a misclassification
  risk analysis is warranted."

### Step 4: Assess Salary and Payroll Compliance

Assess the employer's compliance with EA salary obligations:

#### 4a. Salary Payment Timing (Section 21)

| Obligation     | Statutory Requirement                                          |
| -------------- | -------------------------------------------------------------- |
| Regular salary | Within **7 days** after end of salary period                   |
| Overtime pay   | Within **14 days** after end of overtime salary period         |
| Payment method | Cash, cheque, or bank transfer (with employee written consent) |

**Red flags**: Late payment, withholding salary as leverage, informal payment arrangements.

#### 4b. Permissible Salary Deductions (Section 27)

Only the following deductions are lawful:

- Absence from work (proportionate deduction)
- Accommodation, amenities, or services provided by employer (employee consent in writing)
- Recovery of loans or salary advances
- CPF contributions (employee and employer portions)
- Skills Development Levy (SDL): **0.25% of monthly wages**, capped at **S$11.25/employee/month**
- SHG fund contributions (for certain employee groups)
- Court-ordered salary deductions
- Deductions authorised in writing by the employee

> **Total deduction cap**: All deductions (excluding CPF) must not exceed **50% of salary**
> in any one salary period.

**Red flags**: Unauthorised deductions, deductions exceeding 50% cap, deducting for business
losses or property damage not caused by wilful act.

#### 4c. Itemised Payslip Requirements (Mandatory since 1 April 2016)

Every payslip must be issued within **3 working days** of salary payment and include:

| Required Field                            | Notes                                  |
| ----------------------------------------- | -------------------------------------- |
| Employee full name                        | As per NRIC/passport                   |
| Date(s) of payment                        |                                        |
| Basic salary                              |                                        |
| Start and end date of salary period       |                                        |
| All allowances (itemised individually)    | Cannot be lumped as "other allowances" |
| Overtime hours worked                     | Separate line item                     |
| Overtime pay                              | Separate line item                     |
| All deductions (itemised, purpose stated) |                                        |
| CPF employee contribution                 |                                        |
| CPF employer contribution                 |                                        |
| SDL deduction                             |                                        |
| Net pay                                   |                                        |

**Penalties for payslip non-compliance**: Fine up to **S$5,000** and/or imprisonment up
to **6 months** per offence (first conviction). [VERIFY current penalty schedule]

**⟁ CLARIFY** — If reviewing an existing payslip template, ask whether:

- The employer issues payslips electronically or in hard copy
- The template was last reviewed after April 2016 (when requirement was introduced)
- The employer can produce payslip records for the past 2 years (MOM may request these)

### Step 5: Assess Hours of Work, Overtime and Rest Days (Part IV Employees Only)

This section applies **only to Tier 1 (Part IV) employees**. Skip for PMEs and other
Tier 2 employees, but note that Part IV protections do not apply to them.

#### 5a. Working Hours (Section 38)

| Limit                                      | Statutory Maximum                                            |
| ------------------------------------------ | ------------------------------------------------------------ |
| Normal hours per day                       | **8 hours**                                                  |
| Normal hours per week                      | **44 hours**                                                 |
| Maximum hours per day (including overtime) | **12 hours**                                                 |
| Rest break                                 | Minimum break required after **6 consecutive hours** of work |

#### 5b. Overtime (Sections 37–38)

| Rule                  | Requirement                                                |
| --------------------- | ---------------------------------------------------------- |
| Overtime rate         | Minimum **1.5× the basic hourly rate** of pay              |
| OT cap (normal)       | **72 hours/month**                                         |
| Exceeding OT cap      | Requires **MOM written approval**                          |
| OT payment deadline   | Within **14 days** after end of salary period              |
| Time-off substitution | **Not permitted** for Part IV employees (must pay in cash) |

**Overtime Calculation Formula (Monthly-Rated Employees):**

```
Hourly Basic Rate = Monthly Basic Salary ÷ (26 × Normal Daily Hours)
Overtime Pay      = Hourly Basic Rate × 1.5 × Overtime Hours
```

**Example**: Employee on S$2,000/month, 8-hour normal day:

- Hourly rate: S$2,000 ÷ (26 × 8) = S$9.62/hour
- OT rate: S$9.62 × 1.5 = **S$14.42/hour**

> **Non-workmen OT cap**: For non-workmen, overtime rate is calculated based on a capped
> salary of S$2,600/month (i.e., S$13.60/hour maximum for OT rate purposes), even if the
> employee earns above S$2,600 (but still qualifies for Part IV).

#### 5c. Rest Days (Section 36)

| Entitlement         | Rule                                 |
| ------------------- | ------------------------------------ |
| Minimum rest days   | **1 rest day per week** (unpaid)     |
| Rest day definition | 1 whole day (midnight to midnight)   |
| Public holidays     | **11 paid public holidays** per year |

**Work on Rest Day (at employer's request):**

| Hours Worked                           | Pay Entitlement                            |
| -------------------------------------- | ------------------------------------------ |
| Half day or less                       | **1 day's pay**                            |
| More than half day, up to normal hours | **2 days' pay**                            |
| Beyond normal hours                    | 2 days' pay + **OT rate** for excess hours |

**Work on Public Holiday:**

- Normal day's pay + extra full day's pay
- If hours exceed normal working hours: additional OT rate applies

**⟁ CLARIFY** — If the employer operates shift work or irregular hours, ask:

- "Does the employer use shift schedules? Overtime is calculated over a 2-week reference
  period (3 weeks for shift workers). Confirm the scheduling pattern."

### Step 6: Assess Leave Entitlements

#### 6a. Annual Leave (Section 43)

| Years of Service | Annual Leave Entitlement                |
| ---------------- | --------------------------------------- |
| Less than 1 year | Pro-rated (eligible after 3 months)     |
| 1 year           | **7 days**                              |
| 2 years          | **8 days**                              |
| 3 years          | **9 days**                              |
| 4 years          | **10 days**                             |
| 5 years          | **11 days**                             |
| 6 years          | **12 days**                             |
| 7 years          | **13 days**                             |
| 8+ years         | **14 days** (maximum statutory minimum) |

> Contracts may provide more generous entitlements; the EA provides the floor.
> Leave accrual begins from 3 months of service.

#### 6b. Sick Leave (Section 89)

| Entitlement           | After 3–6 Months Service | After 6 Months Service                          |
| --------------------- | ------------------------ | ----------------------------------------------- |
| Outpatient sick leave | Pro-rated                | **14 days/year**                                |
| Hospitalisation leave | Pro-rated                | **60 days/year** (inclusive of outpatient days) |

- Entitlement requires a medical certificate from a government-approved medical practitioner
- Employer may require the employee to see a company-designated medical professional

#### 6c. Maternity Leave (Child Development Co-Savings Act)

| Scenario                                   | Entitlement                                                     |
| ------------------------------------------ | --------------------------------------------------------------- |
| **Singapore Citizen child**                | **16 weeks** fully paid                                         |
| Non-citizen child (1st or 2nd confinement) | 8 weeks employer-paid + 4 weeks unpaid = 12 weeks               |
| Third child and beyond (citizen)           | Government pays all 16 weeks (employer reimburses from govt)    |
| 1st and 2nd citizen child                  | Employer pays first 8 weeks; government reimburses next 8 weeks |

**Eligibility**: Minimum **90 days of service** before the expected date of confinement.

**Protection against dismissal**: Employer cannot dismiss an employee without notice during
pregnancy and 4 weeks after confinement (for eligible employees).

#### 6d. Paternity Leave (effective 1 April 2025)

| Entitlement         | Detail                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------------- |
| Duration            | **4 weeks** (mandatory, government-paid)                                                  |
| Child eligibility   | Singapore Citizen child born **on or after 1 April 2025**                                 |
| Service requirement | Minimum **3 months** of service at child's birth                                          |
| Timing              | Must be taken within the period from child's birth to end of the 16-week maternity period |
| Prior rule          | 2 weeks paternity leave (for children born before 1 April 2025)                           |

#### 6e. Shared Parental Leave (effective 1 April 2025)

| Period            | Shared Leave Entitlement                              |
| ----------------- | ----------------------------------------------------- |
| From 1 April 2025 | **6 weeks** shared parental leave (parents may share) |
| From 1 April 2026 | Increasing to **10 weeks** shared parental leave      |

Applicable to Singapore Citizen children born on or after 1 April 2025.

#### 6f. Childcare Leave

| Child's Citizenship             | Annual Entitlement per Parent |
| ------------------------------- | ----------------------------- |
| Singapore Citizen child under 7 | **6 days/year**               |
| Non-citizen child under 7       | **2 days/year**               |

**Eligibility**: Employee must have at least 3 months of service with the same employer.

**⟁ CLARIFY** — When assessing maternity/paternity leave compliance, ask:

- "What is the citizenship status of the employee and their child? This determines the
  leave duration and whether government reimbursement applies."
- "Is the employee employed by an employer with fewer than 10 employees? If so,
  government reimbursement rules may differ."

### Step 7: Assess Termination Compliance

#### 7a. Notice Periods (Section 10)

Statutory minimum notice periods (contract may provide longer):

| Length of Service   | Minimum Notice |
| ------------------- | -------------- |
| Less than 26 weeks  | **1 day**      |
| 26 weeks to 2 years | **1 week**     |
| 2 years to 5 years  | **2 weeks**    |
| Over 5 years        | **4 weeks**    |

- Payment in lieu of notice is permissible at the equivalent salary rate
- The notice period in the employment contract prevails if **longer** than the statutory minimum
- Employer cannot contract out of the statutory minimum

#### 7b. Dismissal Without Notice — Due Inquiry (Section 14)

An employer may dismiss an employee without notice only for **misconduct** following a
**due inquiry** conducted by the employer. Requirements:

- Conduct a fair inquiry before dismissal
- Give the employee a reasonable opportunity to be heard
- Ensure the decision is based on evidence
- Document the inquiry proceedings

> An employer may pay wages in lieu of notice instead of conducting a due inquiry, but
> only with the employee's **agreement**. Absent agreement, due inquiry is required before
> dismissal without notice.

#### 7c. Wrongful Dismissal

**Definition**: Dismissal without just cause or excuse.

This includes:

- Dismissal that is arbitrary, capricious, or mala fide
- Dismissal based on protected characteristics (under Workplace Fairness Act 2025 when
  in force)
- Constructive dismissal (where employer's conduct leaves employee with no reasonable
  alternative but to resign)
- Dismissal in breach of contractual notice requirements

**Tripartite Guidelines on Wrongful Dismissal** identify what generally constitutes
just cause: genuine redundancy, proven misconduct after due inquiry, credible performance
management process. [VERIFY current guidelines at mom.gov.sg]

**Wrongful Dismissal Remedies (via ECT):**

- Reinstatement to former position + back wages; OR
- Compensation in lieu of reinstatement (amount determined by tribunal)

**Claim window**: Lodge at TADM within **1 month** from last date of employment.
Exception: Dismissal during pregnancy — any time after last employment date, within
**2 months** of delivery date.

#### 7d. Retrenchment Obligations

| Obligation                       | Threshold / Rule                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| MOM notification required        | Employers with **10+ employees** retrenching **5+ employees** within any 6-month period |
| Notification timing              | Notify MOM before or as soon as practicable after serving notice                        |
| Retrenchment benefit (statutory) | Employees with at least **2 years of continuous service**                               |
| Retrenchment benefit amount      | No statutory fixed rate — determined by contract or collective agreement                |
| Market norm                      | **2 weeks to 1 month's salary per year of service**                                     |
| Re-employment priority           | Employer should consider retraining and redeployment before retrenchment                |
| Fair retrenchment practices      | Follow Tripartite Advisory on Managing Excess Manpower and Responsible Retrenchment     |

**⟁ CLARIFY** — For retrenchment scenarios, ask:

- "How many employees are being retrenched in total and over what time period? This
  determines the MOM notification obligation."
- "Are any retrenched employees union members? Unionised employees have additional
  protections under the Industrial Relations Act."
- "Are any retrenched employees pregnant or on maternity leave? Special protections apply."

### Step 8: Assess ECT and TADM Dispute Resolution Compliance

#### 8a. TADM Mandatory Pre-Mediation

All employment disputes (salary claims and wrongful dismissal) must go through
**mandatory TADM mediation** before filing at the ECT.

**Process:**

1. Lodge claim at TADM (within applicable limitation period)
2. TADM schedules mediation session
3. If mediated settlement reached → enforceable as settlement agreement
4. If mediation unsuccessful → TADM issues "claim referral certificate"
5. Present certificate to ECT to file tribunal claim

#### 8b. Employment Claims Tribunals (ECT) Jurisdiction

| Claim Type                                              | Jurisdiction Cap                          |
| ------------------------------------------------------- | ----------------------------------------- |
| Salary-related claims (general)                         | Up to **S$20,000** per claim              |
| With Tripartite Mediation Framework or union assistance | Up to **S$30,000** per claim              |
| Wrongful dismissal claims                               | Same limits; reinstatement also available |

**Procedure**: No legal representation in ECT. Parties appear in person. Tribunal
magistrate hears unresolved disputes after Case Management Conference.

**Limitation periods**:

- Salary claims: within **1 year** from the date the salary became due
- Wrongful dismissal: within **1 month** from last date of employment

**⟁ CLARIFY** — For ECT claim scenarios, ask:

- "What is the quantum of the claim? Claims above S$20,000 require union involvement or
  the Tripartite Mediation Framework to access the S$30,000 cap."
- "Is the employee represented by a union? This may affect the claim limit and available
  remedies."

### Step 9: Assess National Wages Council and Tripartite Guidelines Compliance

#### 9a. NWC 2024/2025 Wage Guidelines (Effective 1 December 2024 – 30 November 2025)

| Employee Category                                                             | Recommended Wage Increase                                |
| ----------------------------------------------------------------------------- | -------------------------------------------------------- |
| Lower-wage workers (gross monthly wage ≤ S$2,500) — employers performing well | **5.5–7.5% or S$100–S$120** (whichever is higher)        |
| General workforce                                                             | Wage increases tied to productivity and firm performance |

> NWC guidelines are **advisory**, not legally binding, for non-unionised employers.
> However, MOM monitors compliance and non-adherence can attract scrutiny.

**Flexible Wage System (FWS):**

- Annual Variable Component (AVC): variable year-end bonus component (adjustable downward
  in difficult years, but only with proper advance notice per tripartite guidelines)
- Monthly Variable Component (MVC): variable monthly component adjustable with business
  conditions

#### 9b. FWA Tripartite Guidelines (Effective 1 December 2024)

Employers must have a **documented, fair process** for considering flexible work arrangement
(FWA) requests, covering:

| Obligation            | Requirement                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| FWA request process   | Must exist and be communicated to employees                                 |
| Response timeline     | Must respond to FWA requests within a reasonable period                     |
| Grounds for rejection | Must be business-justified; cannot be arbitrary                             |
| Anti-retaliation      | Cannot dismiss or disadvantage an employee solely for making an FWA request |

**⟁ CLARIFY** — For FWA compliance, ask:

- "Does the employer have a written FWA policy or process document? This is required
  as of 1 December 2024."
- "Has any employee been dismissed or disadvantaged following an FWA request? This would
  be an immediate compliance concern."

#### 9c. Workplace Fairness Act 2025 (Pre-Commencement Compliance Planning)

The Workplace Fairness Bill was passed on **8 January 2025**. Commencement date pending.

**Key provisions to prepare for:**

- Prohibition on discrimination in hiring, employment terms, and dismissal based on
  protected characteristics (age, nationality, sex, religion, race, disability, and others)
- Mandatory grievance handling process for discrimination complaints
- New tribunal modelled on ECT for workplace discrimination claims
- Employer obligation to keep records of hiring decisions

> Employers should review current hiring practices, job advertisements, and dismissal
> procedures against Workplace Fairness Act requirements now, ahead of commencement.

### Step 10: Classify Compliance Findings and Generate Output

Apply the Compliance Classification System (below) to each area assessed. For each
NON-COMPLIANT or PARTIAL finding, generate actionable remediation steps.

Before delivering the output:

1. Run the 5 **Citation Quality Gates** (below) silently. Revise any failures.
2. For every CRITICAL-severity finding, run the **3-pass Self-Interrogation** (below).
3. Score confidence levels using the **Confidence Scoring Scale** (below).
4. Complete the **Glass Box Audit Trail** template.

---

## Compliance Classification System

Classify each compliance area using this three-tier system:

| Status            | Colour    | Meaning                                                                                               |
| ----------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| **COMPLIANT**     | 🟢 GREEN  | Employer meets or exceeds the statutory requirement                                                   |
| **PARTIAL**       | 🟡 YELLOW | Employer partially meets the requirement; gaps exist but risk is manageable with prompt remediation   |
| **NON-COMPLIANT** | 🔴 RED    | Clear statutory violation; immediate remediation required; MOM enforcement risk or ECT claim exposure |

---

## Severity Classification

Combine compliance status with severity for prioritisation:

| Tier         | Label                      | Criteria                                                                                                                                                                                          | Action                                   |
| ------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **CRITICAL** | 🔴 NON-COMPLIANT           | Statutory violation with direct criminal/civil penalty exposure (e.g., salary non-payment, payslip non-issuance, illegal deductions, failure to conduct due inquiry for dismissal without notice) | Immediate remediation; seek legal advice |
| **HIGH**     | 🔴 NON-COMPLIANT           | Clear statutory violation affecting employee rights (e.g., underpayment of overtime, failure to pay retrenchment benefit, unlawful dismissal)                                                     | Address within 5 business days           |
| **MEDIUM**   | 🟡 PARTIAL                 | Partial compliance; statutory floor met but gaps in policy documentation or process (e.g., FWA policy missing, NWC wage increase not applied for lower-wage workers)                              | Address within 30 days                   |
| **LOW**      | 🟢 COMPLIANT with advisory | Compliant but best-practice improvements available (e.g., payslip template could be clearer, leave policy could be more generous)                                                                 | Address in next policy review cycle      |

---

## Prioritisation Framework

Prioritise remediation in this order:

| Priority           | Category                               | Examples                                                                                                          |
| ------------------ | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **P1 — Immediate** | Criminal / regulatory penalty exposure | Salary non-payment; illegal deductions; payslip non-compliance; failure to notify MOM of mass retrenchment        |
| **P2 — Urgent**    | Employee claim exposure (ECT / TADM)   | Overtime underpayment; unlawful dismissal; failure to pay retrenchment benefit; maternity/paternity leave denials |
| **P3 — Important** | Policy and documentation gaps          | Missing FWA policy; AVC/MVC not properly documented; annual leave pro-ration errors                               |
| **P4 — Advisory**  | Best practice improvements             | NWC non-compliance (advisory); employment contract terms below market; informal payslip format                    |

---

## Deep Compliance Analysis: Topic Reference

### Topic A — Employment Contract Basics

Every employment relationship under the EA should have a written contract or key employment
terms (KETs) document. While not strictly mandatory for all employees, MOM strongly
encourages issuance of written KETs. Review against:

| Clause                         | EA Requirement                                        |
| ------------------------------ | ----------------------------------------------------- |
| Salary amount and payment date | Must be documented; salary paid within 7 days         |
| Notice period                  | Must meet statutory minimums (Section 10)             |
| Working hours                  | Must not exceed Part IV limits for eligible employees |
| Leave entitlements             | Must meet or exceed statutory minimums                |
| Probation period               | No statutory limit; market norm 3–6 months            |
| Job scope / duties             | Should be clearly defined                             |

**Red flags**: Notice period below statutory minimum; leave entitlement below statutory
minimum; unilateral variation clause without reasonable notice; penalty clause for early
resignation beyond reasonable bounds.

### Topic B — Foreign Worker Compliance

Singapore employers with foreign employees must also comply with:

| Obligation                         | Details                                                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Valid work pass                    | Employment Pass (EP), S Pass, Work Permit, etc. — check MOM pass portal                                                                    |
| Work pass conditions               | Employee may only work for sponsoring employer in approved occupation                                                                      |
| Foreign Worker Levy                | Applies to Work Permit and S Pass holders; rate depends on sector and quota                                                                |
| Fair Consideration Framework (FCF) | Employers must fairly consider Singaporeans before hiring foreigners; job vacancies must be posted on MyCareersFuture for at least 14 days |
| FCF Watchlist                      | MOM publishes a watchlist of employers with discriminatory hiring patterns                                                                 |

> [VERIFY] FCF job advertisement requirements against current MOM guidelines, as these
> are periodically updated.

### Topic C — Workplace Safety Obligations

While not part of the EA itself, workplace safety obligations interact with employment
compliance:

| Obligation                           | Key Rule                                                                                                              |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Workplace Safety and Health Act 2006 | Employer has duty to ensure safe working environment                                                                  |
| WSH fines (from 1 June 2024)         | Maximum fine raised from S$20,000 to **S$50,000** for breaches causing death, serious injury, or dangerous occurrence |
| Mandatory accident reporting         | Workplace accidents must be reported to MOM within prescribed timelines                                               |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                               | Fail Action                               |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Source**     | Every EA compliance claim cites a specific section of the Employment Act, a subsidiary regulation, or an official MOM/tripartite guidance document | Add citation or mark [UNVERIFIED]         |
| **Format**     | Citations follow Singapore statutory format: "Employment Act (Cap. 91), s [section]" or "EA s [section]"                                           | Fix format                                |
| **Currency**   | Verify that the cited provision reflects post-2019 amendment text and 2024–2025 legislative changes                                                | Flag [CHECK CURRENCY]                     |
| **Domain**     | Analysis stays within Singapore law; do not apply English or other common law employment principles without verifying applicability in Singapore   | Remove or flag jurisdictional assumptions |
| **Confidence** | Uncertainty is explicitly stated, not hidden                                                                                                       | Add confidence qualifier                  |

### Self-Interrogation for CRITICAL Findings

For any CRITICAL-severity finding, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from
the cited statutory provision? Would MOM or an ECT tribunal actually reach this conclusion?
Is the statutory provision clearly applicable to the employee type and situation?

**Pass 2 — Completeness**: Have all relevant EA provisions been considered? Are there any
defences, exceptions, or savings provisions that could affect the finding? (e.g., Are there
collective agreements that vary the statutory minimum? Has MOM granted any exemption?)

**Pass 3 — Challenge**: What is the strongest argument that the employer IS compliant?
Under what circumstances might a reasonable employment lawyer advise that this does not
constitute a violation?

### Confidence Scoring Scale

| Level        | Range     | Meaning                                              | Action                               |
| ------------ | --------- | ---------------------------------------------------- | ------------------------------------ |
| **Definite** | 0.95–1.0  | Clear statutory text, no ambiguity                   | State as compliance requirement      |
| **High**     | 0.80–0.94 | Strong statutory basis, minor interpretive questions | State with brief caveat              |
| **Probable** | 0.60–0.79 | Good arguments, some interpretive uncertainty        | State reasoning and contra-arguments |
| **Possible** | 0.40–0.59 | Genuine legal uncertainty                            | Flag for professional review         |
| **Unlikely** | 0.0–0.39  | Speculative; weak basis                              | Do not assert; flag [UNCERTAIN]      |

---

## Glass Box Audit Trail

Complete this template and include it in every compliance assessment output:

```yaml
glass_box:
  skill_name: "legalcode-sg-employment-act-compliance"
  mode: "Singapore Employment Act compliance assessment"
  jurisdiction: "Singapore"
  legislation_verified_against:
    - "Employment Act 1968 (Cap. 91) — as amended to 2025"
    - "Employment Claims Act 2016"
    - "Child Development Co-Savings Act 2001"
    - "Workplace Fairness Act 2025 (passed; commencement TBC)"
    - "Platform Workers Act 2024 (effective 1 Jan 2025)"
  employee_coverage_tier: "[Tier 1 / Tier 2 / Tier 3 — state which and why]"
  assessment_scope:
    - "[List areas assessed: salary, overtime, leave, termination, etc.]"
  legalcode_mcp: "[Connected / Not connected]"
  web_research_conducted: "[Yes / No — date and sources]"
  citations_verified: "[n VERIFIED / n UNVERIFIED]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  critical_findings: "[n — list finding titles]"
  high_findings: "[n]"
  medium_findings: "[n]"
  low_findings: "[n]"
  limitations:
    - "NWC guidelines are advisory; compliance with wage recommendations cannot be assessed without wage data"
    - "Workplace Fairness Act 2025 commencement date is not yet confirmed; pre-commencement planning guidance only"
    - "CPF contribution rate calculations not performed — use CPF Board calculator"
    - "Foreign worker levy calculations not performed — consult MOM pass portal"
    - "All statutory references should be verified against Singapore Statutes Online (sso.agc.gov.sg)"
  reviewer: "AI-assisted — requires review by Singapore-qualified employment lawyer"
```

---

## Anti-Patterns

What NOT to do when assessing Singapore Employment Act compliance:

1. **Conflating Part IV and core EA protections** — Assuming that all employees are
   covered by Part IV (hours, overtime, rest days) when PMEs and higher-earning non-workmen
   are excluded. Part IV is salary-threshold-gated; always check first.

2. **Treating the EA as exhaustive** — The EA interacts with multiple other statutes
   (Child Development Co-Savings Act for parental leave, CPF Act for contributions, Workplace
   Safety and Health Act, EFMA for foreign workers). Do not advise on EA in isolation.

3. **Ignoring the 2019 coverage expansion** — Advising that PMEs earning above S$4,500
   are unprotected by the EA. This was the pre-2019 position. Post-April 2019, all employees
   are covered for core provisions.

4. **Confusing statutory minimums with market norms** — The EA sets the floor, not the
   ceiling. Annual leave of 7 days is the statutory minimum; most employers provide more.
   Advising that 7 days is "standard" market practice is misleading.

5. **Advising that time-off substitutes for overtime pay** — For Part IV employees,
   overtime must be paid in cash at 1.5x rate. Substituting time-off is not permitted
   under the EA, even with employee consent.

6. **Miscalculating overtime for non-workmen** — The overtime rate for non-workmen is
   capped based on a salary of S$2,600/month (S$13.60/hour), not the employee's actual
   salary if higher. This cap often results in lower overtime rates than employees expect.

7. **Overlooking the 72-hour monthly overtime cap** — Advising employers that they can
   require unlimited overtime. The 72-hour monthly cap applies; exceeding it without MOM
   written approval is a violation.

8. **Missing the TADM mandatory mediation step** — Advising employees to file directly
   at the ECT without first going through mandatory TADM mediation. All EA employment
   claims require TADM mediation before ECT referral.

9. **Applying the wrong claim limitation period** — Salary claims: 1 year from when
   salary became due. Wrongful dismissal: 1 month from last employment date (2 months for
   dismissal during pregnancy). Confusing these time limits can cause claims to be
   time-barred.

10. **Advising that retrenchment benefit is always legally required** — Statutory
    retrenchment benefit applies only to employees with at least **2 years** of continuous
    service. Employees with shorter service have no statutory entitlement (though contract
    or collective agreement may provide otherwise).

11. **Ignoring the due inquiry requirement for dismissal without notice** — Advising
    employers they can dismiss for misconduct without a due inquiry simply by paying wages
    in lieu of notice. Payment in lieu of notice does not replace the due inquiry requirement
    for misconduct dismissal; it only replaces the notice period for non-misconduct
    terminations.

12. **Treating NWC wage guidelines as legally binding** — NWC guidelines are advisory
    (tripartite recommendations), not statutory requirements. Non-compliance does not carry
    direct legal penalty, but persistent non-compliance attracts MOM scrutiny, particularly
    for lower-wage workers.

13. **Underestimating payslip penalties** — Failure to issue compliant itemised payslips
    is a criminal offence (fine up to S$5,000 and/or imprisonment up to 6 months per
    offence). Many employers underestimate this risk by treating payslip issuance as
    administrative rather than legal compliance.

14. **Advising on fixed-term contracts without caution** — Fixed-term employees who are
    regularly renewed may be re-characterised as permanent employees under the EA. Multiple
    consecutive fixed-term contracts without genuine operational justification carry
    reclassification risk.

15. **Overlooking the Workplace Fairness Act 2025 transition** — Advising that no
    anti-discrimination statutory framework exists in Singapore. The WFA was passed in
    January 2025 and will come into force once commenced. Employers should begin compliance
    preparation now, including reviewing hiring practices and establishing grievance
    procedures.

16. **Not updating for April 2025 parental leave changes** — The paternity leave
    increase from 2 weeks to 4 weeks (mandatory) and the new 6-week shared parental leave
    took effect 1 April 2025 for citizen children born on or after that date. Advice based
    on pre-April 2025 rules is outdated.

---

## Writing Standards

Before delivering the compliance assessment, verify these writing quality gates:

- [ ] **Terminology**: Use correct Singapore statutory terminology — "salary" (not "wages"
      except when directly quoting the EA), "employment contract" (not "employment agreement"),
      "MOM" not "Ministry of Labour", "ECT" not "Labour Court"
- [ ] **Statute citations**: Follow the format "Employment Act (Cap. 91), s X" or "EA s X"
      for brevity; "Child Development Co-Savings Act, s X" for parental leave provisions
- [ ] **No false certainty**: Mark all provisions that may have been amended post-March
      2026 with [VERIFY CURRENCY]
- [ ] **Active voice and imperative form** for recommendations: "Issue itemised payslips
      within 3 working days" — not "Itemised payslips should be issued"
- [ ] **Table format** for statutory thresholds — these are clearest as tables, not prose
- [ ] **Plain language** for employee-facing advice; legal precision for employer
      compliance assessment
- [ ] **No generic employment law** — every recommendation must be Singapore EA-specific,
      not generic UK/US/Australian employment law imported without verification

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current text of Employment Act (Cap. 91) sections referenced in this skill
- Verify that the 2024–2025 legislative changes are correctly captured
- Search for recent ECT decisions on overtime calculation, wrongful dismissal, and
  retrenchment benefit disputes
- Search for current MOM administrative guidelines and practice circulars
- Save verified authority to `/tmp/legalcode-sg-ea-research.md` for use throughout
  the assessment

**Without legalcode-mcp:**

- Mark every statutory reference with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — verify all provisions at sso.agc.gov.sg"`
- Direct user to MOM website (mom.gov.sg) for current guidance
- Proceed with the assessment framework; flag that statutory thresholds should be
  independently verified before reliance

---

## Output Format Template

Produce the compliance assessment in this format:

---

# Singapore Employment Act Compliance Assessment

**Prepared for**: [Employer name or "Confidential"]
**Date**: [Date]
**Employee / Scenario**: [Brief description]
**Coverage Tier**: [Tier 1 — Full (Part IV) / Tier 2 — Core only]
**Assessment Scope**: [Areas assessed]

---

## Executive Summary

| Overall Status                                 | Critical Findings | High Findings | Medium Findings | Low Findings |
| ---------------------------------------------- | ----------------- | ------------- | --------------- | ------------ |
| [🔴 NON-COMPLIANT / 🟡 PARTIAL / 🟢 COMPLIANT] | [n]               | [n]           | [n]             | [n]          |

**Top 3 Issues Requiring Immediate Attention:**

1. [Finding title — severity — one-line description]
2. [Finding title — severity — one-line description]
3. [Finding title — severity — one-line description]

---

## Detailed Findings

### [Area Name, e.g., "Overtime Compliance"]

**Status**: 🔴 NON-COMPLIANT / 🟡 PARTIAL / 🟢 COMPLIANT
**Severity**: CRITICAL / HIGH / MEDIUM / LOW
**Statutory basis**: [EA s X; EA s Y]

**Finding**: [Specific description of what was found]

**Gap / Violation**: [Specific description of the gap or violation]

**Legal exposure**:

- [Specific penalty or claim exposure, citing EA section]
- Confidence: [Definite / High / Probable / Possible]

**Remediation steps**:

1. [Specific action — by whom — by when]
2. [Specific action — by whom — by when]

**[Repeat for each finding]**

---

## Compliance Summary Table

| Area                            | Status   | Severity | EA Reference          | Remediation Priority |
| ------------------------------- | -------- | -------- | --------------------- | -------------------- |
| Employment contract basics      | 🟢/🟡/🔴 |          | EA s X                | P1/P2/P3/P4          |
| Salary payment timing           | 🟢/🟡/🔴 |          | EA s 21               |                      |
| Itemised payslips               | 🟢/🟡/🔴 |          | EA s 96A              |                      |
| Salary deductions               | 🟢/🟡/🔴 |          | EA s 27               |                      |
| Working hours (Part IV)         | 🟢/🟡/🔴 |          | EA s 38               |                      |
| Overtime rate and cap           | 🟢/🟡/🔴 |          | EA ss 37–38           |                      |
| Rest days                       | 🟢/🟡/🔴 |          | EA s 36               |                      |
| Annual leave                    | 🟢/🟡/🔴 |          | EA s 43               |                      |
| Sick leave                      | 🟢/🟡/🔴 |          | EA s 89               |                      |
| Maternity leave                 | 🟢/🟡/🔴 |          | CDCSA                 |                      |
| Paternity leave (from Apr 2025) | 🟢/🟡/🔴 |          | CDCSA                 |                      |
| Notice periods                  | 🟢/🟡/🔴 |          | EA s 10               |                      |
| Termination due inquiry         | 🟢/🟡/🔴 |          | EA s 14               |                      |
| Retrenchment notification       | 🟢/🟡/🔴 |          | EA / MOM              |                      |
| FWA policy (from Dec 2024)      | 🟢/🟡/🔴 |          | Tripartite Guidelines |                      |
| NWC wage guidelines             | 🟢/🟡/🔴 |          | NWC 2024/25           |                      |

---

## Recommended Actions

### P1 — Immediate (within 5 business days)

- [ ] [Action item]

### P2 — Urgent (within 30 days)

- [ ] [Action item]

### P3 — Important (within 90 days)

- [ ] [Action item]

### P4 — Advisory (next policy review)

- [ ] [Action item]

---

## Glass Box Audit Trail

```yaml
[Completed Glass Box YAML from the template above]
```

---

> _This assessment is AI-assisted. All findings should be verified by a Singapore-qualified
> employment lawyer before reliance. Statutory references are current as of the knowledge
> cut-off and may have been amended. Verify all provisions at sso.agc.gov.sg and mom.gov.sg._

---

---

## Localization Notes

This skill is **Singapore-specific** and should not be applied to other jurisdictions.
Adjacent Singapore employment compliance topics not covered by this skill:

| Topic                                          | Relevant Skill or Resource                           |
| ---------------------------------------------- | ---------------------------------------------------- |
| PDPA data breach notification                  | `singapore-pdpa-data-breach-notification-operations` |
| CPF contribution rate calculations             | CPF Board calculator at cpf.gov.sg                   |
| Foreign worker levy                            | MOM pass portal at mom.gov.sg/passes-and-permits     |
| Workplace Safety and Health Act                | WSH Council at wshc.sg                               |
| Industrial Relations Act (unionised employees) | Consult NTUC or Singapore-qualified labour lawyer    |
| Income tax (IRAS)                              | IRAS at iras.gov.sg                                  |
| Competition Act                                | Competition and Consumer Commission of Singapore     |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Singapore Ministry of Manpower (MOM) official guidance at mom.gov.sg
- Singapore Statutes Online (sso.agc.gov.sg) — Employment Act 1968 (Cap. 91)
- Employment Claims Act 2016
- Child Development Co-Savings Act 2001 (Cap. 38A)
- Workplace Fairness Bill (passed 8 January 2025)
- Platform Workers Act 2024
- NWC 2024/2025 Wage Guidelines (SNEF)
- Tripartite Guidelines on Flexible Work Arrangement Requests (1 December 2024)
- Tripartite Guidelines on Wrongful Dismissal
- Seyfarth Shaw, "2024 Year in Review: Singapore Employment Law" (2025)
- Mayer Brown, "Singapore Employment 2024 Highlights and 2025 Outlook" (2024)
- SingaporeLegalAdvice.com — Employment Act and ECT guides
- 2-agent research pipeline (structural analysis + deep legal topic research)
