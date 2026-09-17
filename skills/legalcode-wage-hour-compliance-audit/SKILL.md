---
name: legalcode-wage-hour-compliance-audit
description: Audits wage and hour compliance under the Fair Labor Standards Act (FLSA) and state equivalents.
  Use when assessing exempt vs. non-exempt employee classification under duties tests (executive, administrative,
  professional, computer employee, outside sales, highly compensated), salary threshold compliance (including
  the post-2024 Texas-court-vacated DOL rule, current operative $684/week threshold), overtime calculation
  methodology (regular rate inclusions/exclusions, fluctuating workweek, piece rate, blended rates), meal
  and rest break requirements by state, timekeeping adequacy and off-the-clock risk, tip credit and tip
  pooling rules (2018 CAA and 2021 DOL final rule), child labor compliance (29 CFR Part 570), predictive/fair
  scheduling obligations, and pay stub and record-keeping requirements. Produces classification findings
  by violation tier, quantified exposure estimates, and prioritized remediation recommendations. US federal
  + state jurisdictions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Wage and Hour Compliance Audit

> **Disclaimer**: This skill provides a framework for AI-assisted wage and hour compliance
> analysis. It does not constitute legal advice. All outputs should be reviewed by a
> qualified employment attorney licensed in the relevant jurisdiction(s) before any
> remediation, litigation, or regulatory filing. Federal and state wage and hour laws
> change frequently — verify current salary thresholds, minimum wage rates, and
> regulatory guidance before relying on any figure cited here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> DOL, WHD, and state labor agency sources before relying on them.

---

## Purpose and Scope

This skill conducts a structured audit of an organization's wage and hour compliance
posture under the Fair Labor Standards Act (FLSA), 29 U.S.C. §§ 201–219, applicable
Department of Labor (WHD) regulations (29 CFR Parts 516, 531, 570, 778, 785), and
state wage and hour laws.

**Covers:**

- Exempt vs. non-exempt classification under all six white-collar exemption categories
  (executive, administrative, professional, computer, outside sales, HCE) — duties tests
  and salary basis/level
- Salary threshold compliance with the operative 2020 DOL threshold ($684/week) and
  the status of the vacated 2024 rule
- Overtime calculation methodology — regular rate of pay, inclusions/exclusions,
  fluctuating workweek, piece rate, blended/weighted rate
- Meal and rest break compliance — federal framework plus state-specific requirements
  (CA, NY, WA, CO, IL, OR, and others)
- Timekeeping adequacy — records under 29 CFR Part 516, off-the-clock risk, continuous
  workday doctrine, remote work exposures
- Tip credit and tip pooling — 29 CFR Part 531, 2018 CAA amendments, 2021 DOL final
  rule on dual jobs, back-of-house inclusion
- Child labor compliance — 29 CFR Part 570 hours restrictions and prohibited occupations
- Predictive/fair scheduling obligations — Oregon statewide, plus NYC, Chicago, Seattle,
  LA, Philadelphia, San Francisco, and other city/county ordinances
- Pay stub and record-keeping requirements — California Labor Code § 226, NY Wage Theft
  Prevention Act, FLSA 29 CFR Part 516
- Exposure quantification — back pay formulas, liquidated damages, statutes of
  limitations, PAGA, class and collective action risk

**Does not:**

- Provide legal advice or replace qualified employment counsel
- Draft employment agreements, arbitration clauses, or settlement agreements
- Conduct prevailing wage / Davis-Bacon / Service Contract Act analysis (government
  contract labor standards — see a separate skill if available)
- Perform payroll tax analysis (FICA, withholding — a tax compliance domain)
- Apply outside the United States; for UK/EU wage matters see jurisdiction-specific skills
- Substitute for WHD audit response strategy — that is litigation/regulatory support work

**Related skills:**

- `legalcode-independent-contractor-classification` — worker classification IC vs. employee
- `legalcode-employment-agreement-review` — employment contract clause review
- `legalcode-employee-handbook-review` — handbook policy compliance review
- `legalcode-non-compete-enforceability` — restrictive covenant analysis

---

## Jurisdiction and Governing Law

This skill is **US-centric** with a federal-floor / state-ceiling architecture:

- **Federal baseline**: FLSA sets minimum requirements. States and localities may
  (and often do) impose stricter requirements — higher minimum wages, daily overtime,
  mandatory breaks, scheduling notice — that preempt the FLSA floor.
- **Multi-jurisdiction analysis**: Most employers must comply with the law most protective
  of the employee. This skill identifies the applicable state law for each audit area.

[JURISDICTION-SPECIFIC] States with the most significant additional requirements:

- **California**: Daily overtime (Labor Code § 510), IWC Wage Orders (17 industry-specific
  orders), mandatory meal and rest breaks (Brinker Restaurant Corp. v. Superior Court,
  53 Cal. 4th 1004 (2012)), AB 1228 minimum wage for fast food ($20/hr effective Apr 2024),
  PAGA exposure, pay stub requirements (Labor Code § 226)
- **New York**: NY Minimum Wage Act, WTPA pay notice requirements, spread-of-hours premium,
  call-in pay rules
- **Colorado**: COMPS Order No. 38 — daily overtime (over 12 hrs/day or 12 consecutive
  hrs), mandatory rest breaks
- **Alaska**: Daily overtime (over 8 hrs/day)
- **Washington**: Rest period requirements, paid sick leave interplay
- **Oregon**: Statewide predictive scheduling (ORS 653.450 et seq.)
- **Illinois**: Chicago Fair Workweek Ordinance, One Day Rest in Seven Act

[JURISDICTION-SPECIFIC] For each state where the employer operates, identify:

- State minimum wage (and any locality minimum wages)
- Whether the state has daily overtime
- State meal/rest break requirements
- State-specific salary basis tests for exemptions
- State pay stub and record-keeping requirements
- Predictive scheduling ordinances if in a covered city/county

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the direction or scope of the analysis
- The employer's industry, size, or operating geography creates audit forks
- Multiple valid compliance approaches exist and employer preferences matter
- Incomplete records or ambiguous facts create forks

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

### Step 1: Accept Input Materials

Accept the audit inputs in any of these formats:

- **Employee census data**: Job titles, classifications (exempt/non-exempt), pay rates,
  FLSA exemption basis claimed, FLSA status, pay period, geographic location
- **Payroll records**: Sample pay stubs, overtime calculations, regular rate computations
- **Job descriptions**: Written duties for each position being audited
- **Policies**: Timekeeping policy, off-the-clock policy, meal/rest break policy, tip
  policy, scheduling policy
- **Prior audit findings or WHD investigation results**
- **Narrative description**: The user describes the workforce, industry, and known risk areas

If no materials are provided, prompt the user to supply what is available and note that
analysis without records will be limited to identifying structural risks.

### Step 2: Gather Audit Context

**⟁ CLARIFY** — Before beginning, gather the following context:

1. **Industry and workforce type**:
   - Options: Retail, Food service / hospitality, Healthcare / home care, Technology /
     professional services, Staffing / temp workers, Manufacturing / warehouse,
     Construction, Transportation, Other
   - _Why this matters_: Industry determines which IWC Wage Order applies in California,
     whether tip credit is available, whether DOT motor carrier exemptions apply, and
     what prohibited hazardous work applies to minors.

2. **Operating geography** (which states and cities does the employer operate in?):
   - _Why this matters_: Determines which state and local minimum wages, daily overtime
     rules, break requirements, and predictive scheduling ordinances apply.

3. **Workforce composition**:
   - Options: Primarily hourly non-exempt, Primarily salaried exempt, Mixed hourly and
     salaried, Tipped employees present, Piece-rate workers present, Remote workers
   - _Why this matters_: Tip credit analysis, fluctuating workweek applicability,
     remote work timekeeping risks, and piece-rate overtime methodology each depend
     on workforce composition.

4. **Audit scope**:
   - Options: Full audit across all 9 categories, Priority audit (specific risk areas),
     Pre-litigation exposure quantification, WHD investigation response preparation,
     Pre-M&A due diligence
   - _Why this matters_: Scopes the depth of analysis and the output format.

5. **Known risk areas or prior violations**:
   - Free text. Prompt: "Have there been prior WHD investigations, employee complaints,
     litigation, or internal audit findings? If so, describe the issues."
   - _Why this matters_: Prior violations create willful violation risk (3-year SOL and
     double liquidated damages) and escalate exposure.

6. **Time period for audit**:
   - Default: 3 years (covers both the standard 2-year and willful 3-year SOL)
   - _Why this matters_: Back pay exposure window is bounded by the applicable SOL.

Proceed with reasonable defaults and state them explicitly if the user provides partial context.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

**Research process:**

1. Identify all states and localities where the employer has employees. For each:
   - Current minimum wage rate (check for any locality rates higher than state)
   - Whether state has daily overtime requirements
   - State meal and rest break law
   - State-specific salary basis/level tests (some states have higher thresholds)
   - Predictive scheduling ordinances if in a covered jurisdiction

2. **Use legalcode-mcp** (if connected) to retrieve:
   - Current FLSA salary thresholds (confirm operative threshold post-Texas vacatur)
   - Current state minimum wage rates for relevant states
   - WHD opinion letters and field assistance bulletins relevant to the audit topics
   - Recent WHD enforcement statistics for the employer's industry

3. **Save research results** to `/tmp/legalcode-wage-hour-authority.md`:

   ```markdown
   # Legal Authority Reference — Wage and Hour Audit

   ## Date: [date]

   ### Operative FLSA Thresholds

   - Standard exemption salary basis: $[amount]/week ($[annualized])
   - HCE threshold: $[amount]/year
   - Status of 2024 DOL rule: [Vacated Nov. 15, 2024 — Texas E.D. — operative rule is 2020 rule]

   ### State Minimum Wages (as of [date])

   - [State]: $[amount]/hour [effective date] [any locality overrides]

   ### State Overtime Rules

   - [State]: [daily overtime threshold, if any]

   ### State Break Requirements

   - [State]: [meal break], [rest break]

   ### Predictive Scheduling Jurisdictions

   - [Jurisdiction]: [advance notice], [industries covered], [predictability pay]
   ```

**If legalcode-mcp is not connected:**

- Proceed with general knowledge; mark all threshold figures with [VERIFY CURRENT]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — verify all thresholds"`
- Cross-reference DOL WHD website (dol.gov/agencies/whd) before relying on any figure

### Step 4: Exemption Classification Audit

This is the highest-stakes audit area. FLSA exemption misclassification drives the
largest back pay exposure and is the most common WHD focus.

**⟁ CLARIFY** — For each exempt position being audited:

- "Does a written job description exist? Can you provide it?"
- "How does the employee actually spend their time day-to-day (vs. what the job
  description says)?" [Duties test is based on actual work, not job title or description]

#### 4a. Salary Basis Test

For all white-collar exemptions except outside sales, the employee must be paid on a
salary basis (29 CFR § 541.602):

**Salary basis requirements:**

- [ ] Paid a predetermined, fixed amount each pay period (not reduced based on quality
      or quantity of work)
- [ ] Amount is at least $684/week ($35,568/year) — the **current operative threshold**
      after the November 15, 2024 Texas E.D. vacatur of the 2024 DOL Final Rule
  - [VERIFY CURRENT] The 2024 DOL Final Rule (84 Fed. Reg. 51230) raised the threshold
    to $844/week effective July 1, 2024 and $1,128/week HCE effective Jan 1, 2025.
    The entire 2024 Final Rule was vacated by _State of Texas v. DOL_, E.D. Tex.
    (Nov. 15, 2024). The operative threshold reverts to the 2020 rule: $684/week /
    $35,568/year standard; $107,432/year HCE.
- [ ] Salary not subject to impermissible deductions (check payroll records for deductions
      for partial-day absences, disciplinary suspensions less than a week, etc.)
- [ ] If deductions have occurred: determine whether they constitute a "window of
      correction" situation or a loss of exemption for the affected period

[JURISDICTION-SPECIFIC] Several states set higher salary thresholds:

- **California**: $1,320/week ($68,640/year) as of Jan 1, 2024; $1,560/week ($81,120)
  for computer software employees under Labor Code § 515.5 [VERIFY CURRENT]
- **New York**: Varies by region and employer size — check NYCRR Part 141 [VERIFY CURRENT]
- **Alaska**: $684+/week [VERIFY for any state updates]
- **Colorado**: Check COMPS Order No. 38 for current threshold [VERIFY CURRENT]

**Common salary basis violations:**

| Risk Pattern             | Description                                                            | Classification                     |
| ------------------------ | ---------------------------------------------------------------------- | ---------------------------------- |
| Partial-day docking      | Salary reduced for arriving late or leaving early                      | VIOLATION — destroys exemption     |
| Disciplinary pay docking | Salary reduced for disciplinary reasons without suspension ≥1 week     | VIOLATION                          |
| PTO exhaustion docking   | Salary reduced when PTO is exhausted (not merely PTO account adjusted) | VIOLATION if actual salary reduced |
| Variable salary          | Amount varies week to week based on hours or productivity              | VIOLATION                          |
| State threshold gap      | Salary meets FLSA threshold but not state threshold                    | AT-RISK under state law            |

#### 4b. Executive Exemption Duties Test (29 CFR § 541.100)

An executive exempt employee must:

- [ ] Have a **primary duty** of managing the enterprise or a department/subdivision
- [ ] **Customarily and regularly direct** the work of at least 2 full-time employees
      (or equivalent — can be FTE aggregate)
- [ ] Have authority to hire/fire OR whose recommendations as to hiring, firing,
      advancement, promotion, or other status change are **given particular weight**

**Primary duty analysis** (29 CFR § 541.700):

- Primary duty = the "principal, main, major or most important duty" — not merely
  performed most often
- Consider: relative importance, time spent (50%+ is "strong indicator" but not required),
  relative freedom from supervision, relationship between salary and wages paid to others

**Common executive exemption misclassification patterns:**

| Risk Pattern             | Description                                                       | Classification                             |
| ------------------------ | ----------------------------------------------------------------- | ------------------------------------------ |
| Working supervisors      | Employee manages but spends >50% on non-managerial tasks          | AT-RISK — primary duty may fail            |
| Paper authority only     | Authority to hire/fire exists on paper but never exercised        | AT-RISK — recommendations not given weight |
| Insufficient headcount   | Fewer than 2 FTE direct reports                                   | VIOLATION                                  |
| Retail working manager   | Classified exempt but primarily ringing registers or stocking     | VIOLATION if non-exempt work predominates  |
| Rotating "manager" label | Hourly employees take turns with a "manager" title for scheduling | VIOLATION                                  |

#### 4c. Administrative Exemption Duties Test (29 CFR § 541.200)

An administrative exempt employee must:

- [ ] Have a **primary duty** of office/non-manual work directly related to management
      or general business operations of the employer or the employer's customers
- [ ] **Primary duty includes the exercise of discretion and independent judgment**
      with respect to **matters of significance**

**Discretion and independent judgment analysis:**

- Must compare alternatives and make a choice — not merely apply established techniques
  or procedures
- Must relate to "matters of significance," not routine clerical or ministerial tasks
- Distinguishable from **skilled work** (skilled technician who applies expertise but
  doesn't exercise judgment about significant matters)

**Common administrative exemption misclassification patterns:**

| Risk Pattern                    | Description                                                              | Classification            |
| ------------------------------- | ------------------------------------------------------------------------ | ------------------------- |
| Clerical labeled admin          | Data entry, scheduling, filing classified as "administrative"            | VIOLATION — no discretion |
| Production vs. admin            | Manufacturing, retail sales, or production work lacks admin character    | VIOLATION                 |
| Discretion without significance | Employee makes routine decisions within highly prescribed limits         | AT-RISK                   |
| Customer service reps           | Scripted customer service with no real discretion                        | AT-RISK to VIOLATION      |
| Insurance adjusters             | Context-dependent — some qualify, some don't (see _Hines v. State Room_) | [VERIFY — complex]        |

#### 4d. Learned Professional Exemption (29 CFR § 541.301)

Requires:

- [ ] **Primary duty** is work requiring advanced knowledge in a **field of science
      or learning**
- [ ] Advanced knowledge **customarily acquired** by a prolonged course of specialized
      intellectual instruction (degree or equivalent)
- [ ] Work must be **predominantly intellectual** as opposed to routine/mechanical

[JURISDICTION-SPECIFIC] Note: Registered nurses, dental hygienists, and licensed
practical nurses may qualify depending on state licensure and degree requirements.
Paralegals generally do not qualify (no advanced degree requirement). [VERIFY]

#### 4e. Creative Professional Exemption (29 CFR § 541.302)

Requires:

- [ ] **Primary duty** is work requiring invention, imagination, originality, or talent
- [ ] In a recognized field of artistic or creative endeavor

Note: Journalism — routine reporting does NOT qualify; investigative/analytical work may.

#### 4f. Computer Employee Exemption (29 CFR § 541.400)

Requires:

- [ ] Salary basis: $684/week **or** hourly rate of at least **$27.63/hour**
      (computer exemption uniquely allows hourly payment — 29 U.S.C. § 213(a)(17))
- [ ] Primary duty in one of: systems analysis, design/development/creation of computer
      programs/systems, machine operating, or related work requiring same level of skill

**Common computer exemption misclassification patterns:**

| Risk Pattern              | Description                                          | Classification |
| ------------------------- | ---------------------------------------------------- | -------------- |
| Help desk / IT support    | Hardware maintenance, end-user support — not covered | VIOLATION      |
| Data entry operators      | Routine data entry — not covered                     | VIOLATION      |
| Technicians               | Equipment maintenance without programming/analysis   | VIOLATION      |
| Non-computer-related tech | Engineers without computer systems focus             | AT-RISK        |

[JURISDICTION-SPECIFIC] California has a **separate** computer software employee
exemption (Labor Code § 515.5) requiring $53.20/hour [VERIFY CURRENT 2024/2025 rate]
and specific duties requirements. Narrower than federal.

#### 4g. Outside Sales Exemption (29 CFR § 541.500)

Requires:

- [ ] **Primary duty** is making sales or obtaining orders or contracts for services
- [ ] **Customarily and regularly engaged away from employer's place of business**
      (i.e., at customers' locations)
- **No salary requirement** — outside sales exemption has no salary basis or level test

**Common outside sales misclassification patterns:**

| Risk Pattern                      | Description                                                        | Classification |
| --------------------------------- | ------------------------------------------------------------------ | -------------- |
| Inside/telephone sales            | Sales made by phone or email from office                           | VIOLATION      |
| Mix of inside and outside         | Inside sales portion dominates — fails "customarily and regularly" | AT-RISK        |
| Delivery drivers labeled as sales | Deliveries made incidentally to route — not primarily sales        | AT-RISK        |
| Mixed function employees          | Substantial non-sales duties — primary duty analysis required      | AT-RISK        |

#### 4h. Highly Compensated Employee Exemption (29 CFR § 541.601)

Requires:

- [ ] Total annual compensation of at least **$107,432** (post-vacatur of 2024 rule;
      the vacated 2024 rule would have set $132,964/year then $151,164/year) [VERIFY CURRENT]
- [ ] Receives **at least $684/week** on salary or fee basis
- [ ] **Customarily and regularly performs** any one or more of the duties of an exempt
      executive, administrative, or professional employee

Note: Lower duties bar — does not need to meet the primary duty test for the underlying
exemption. Requires only customary and regular performance of any one qualifying duty.

#### 4i. Special Exemption Categories (Industry-Specific)

**⟁ CLARIFY** — Ask whether any of these apply given the employer's industry:

| Exemption                | Who It Covers                                              | Key Conditions                                                    |
| ------------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------- |
| Motor carrier / DOT      | Truck drivers affecting interstate commerce                | Motor Carrier Act overtime exemption (but state laws still apply) |
| Seasonal amusement parks | Amusement/recreational establishments open < 7 months/year | § 213(a)(3)                                                       |
| Retail service 7(i)      | Commission retail employees                                | ≥ 1.5× minimum wage + >50% of earnings from commissions           |
| Agricultural workers     | Farm workers                                               | Various exemptions under § 213(a)(6)                              |
| Domestic service live-in | Live-in domestic workers                                   | § 213(a)(15)                                                      |
| Companionship services   | Home care workers providing companionship                  | Post-2015 DOL rule — most professional caregivers NOT exempt      |
| Seamen / maritime        | Sailors on American vessels                                | § 213(a)(12)                                                      |
| Taxicab drivers          | Taxicab establishments                                     | § 213(b)(17)                                                      |
| Radio/TV employees       | Small-market stations                                      | § 213(b)(9)                                                       |

### Step 5: Overtime Calculation Methodology Audit

#### 5a. Regular Rate of Pay Analysis (29 CFR Part 778)

The regular rate is the foundation of overtime calculations. Errors here multiply across
all overtime pay periods.

**Regular rate = Total remuneration / Total hours worked in workweek** (29 CFR § 778.109)

**Must be INCLUDED in regular rate:**

| Compensation Type                      | Regulatory Basis | Common Error                                                 |
| -------------------------------------- | ---------------- | ------------------------------------------------------------ |
| Non-discretionary bonuses              | § 778.208        | Treating production bonuses as discretionary                 |
| Shift differentials                    | § 778.207        | Omitting from regular rate calculation                       |
| On-call pay                            | § 778.223        | Omitting required standby pay                                |
| Commissions                            | § 778.117        | Allocating to single week vs. spreading across earned period |
| Piece-rate earnings                    | § 778.418–.419   | Not incorporating into overtime premium                      |
| Non-cash remuneration (meals, lodging) | § 778.116        | Omitting when provided as compensation                       |
| Hazard pay / dirty work premiums       | § 778.207        | Treating as excludable gift                                  |
| Longevity pay                          | § 778.215        | Omitting from base rate                                      |

**May be EXCLUDED from regular rate:**

| Compensation Type                       | Regulatory Basis | Conditions for Exclusion                                                                     |
| --------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------- |
| True discretionary bonuses              | § 778.211        | Amount and grant not determined until after period; announced in advance = NOT discretionary |
| Gifts on special occasions              | § 778.212        | Must not be tied to performance or hours                                                     |
| Vacation/holiday/sick pay               | § 778.216        | Must not represent payment for work                                                          |
| Employer profit-sharing plans           | § 778.214        | Must meet § 7(e)(4) criteria                                                                 |
| True overtime premiums for excess hours | § 778.201        | Premium paid at ≥1.5× bona fide rate — very narrow                                           |
| Expense reimbursements                  | § 778.217        | Must be bona fide reimbursements (not disguised compensation)                                |

**⟁ CLARIFY** — If any of the following exist, ask for details before classifying:

- "Does the employer pay any bonuses, commissions, or incentive pay?"
- "Are there any shift differentials, hazard pay, or premium rates?"
- "Are there expense reimbursements or per diems — are they tied to actual expenses?"

#### 5b. Overtime Premium Calculation

For non-exempt hourly employees:

```
Overtime rate = Regular rate × 1.5
Overtime pay = Overtime rate × OT hours
```

For non-exempt salaried (fluctuating workweek — 29 CFR § 778.114):

- Requirements: (1) salary covers all hours worked in week; (2) hours genuinely
  fluctuate; (3) employer and employee have clear mutual understanding; (4) salary
  sufficient for minimum wage at maximum expected hours
- Overtime premium = Regular rate × 0.5 × OT hours (half-time method)
- [JURISDICTION-SPECIFIC] Several states do not permit fluctuating workweek — California
  expressly prohibits it. [VERIFY state-by-state]

For piece-rate employees:

- Regular rate = (piece-rate earnings + other compensation) / total hours worked
- Overtime = Regular rate × 0.5 × OT hours (if piece-rate earnings already compensate
  for all hours worked at straight time)

For employees working at two or more rates (29 CFR § 778.115):

- **Weighted average method** (default): Regular rate = total earnings at all rates /
  total hours worked
- **Rate in effect method** (by agreement): OT rate tied to rate in effect when OT
  occurs — must be predetermined agreement

**Common overtime calculation errors:**

| Error Pattern                           | Description                                                               | Classification |
| --------------------------------------- | ------------------------------------------------------------------------- | -------------- |
| Non-discretionary bonus omitted         | Regular rate not recalculated when bonus paid                             | VIOLATION      |
| Commission omitted                      | Commission earnings excluded from regular rate                            | VIOLATION      |
| Workweek manipulation                   | Workweek definition shifted to avoid OT                                   | VIOLATION      |
| Half-time applied without FWW agreement | FWW half-time used without written agreement and fluctuating hours        | VIOLATION      |
| Multiple rates — no agreement           | Rate-in-effect method applied without prior agreement                     | VIOLATION      |
| 80-hour biweekly payroll                | Biweekly payroll used to average away OT — workweek is 7 consecutive days | VIOLATION      |
| Comp time for private sector            | Private employers substituting comp time for OT pay                       | VIOLATION      |

#### 5c. Workweek Definition Audit

- [ ] Is a fixed 7-consecutive-day workweek established? (29 CFR § 778.105)
- [ ] Is the workweek documented and communicated to employees?
- [ ] Has the workweek been changed? (Must have FLSA-compliant purpose, not to
      avoid overtime liability — _Seymore v. Metro. Life Ins. Co._, 932 F.3d 400 (6th Cir. 2019) [VERIFY])
- [ ] Are pay periods longer than weekly? (Must still calculate OT on workweek basis)

### Step 6: Meal and Rest Break Compliance Audit

#### 6a. Federal Framework

FLSA does not require meal or rest breaks but regulates how breaks must be **compensated**:

- **Short breaks (5–20 minutes)**: Must be counted as compensable time — employer cannot
  deduct from hours worked (29 CFR § 785.18)
- **Bona fide meal periods (30+ minutes)**: Not compensable if employee is completely
  relieved of duties — must truly be duty-free (29 CFR § 785.19)
  - If employee is required to remain at work site or is frequently interrupted →
    compensable working time

#### 6b. State-Specific Break Requirements

**⟁ CLARIFY** — Confirm which states the employer operates in, then apply state rules:

**California** (most protective — IWC Wage Orders):

- Meal break: 30-minute unpaid meal period for shifts > 5 hours; second 30-min meal
  for shifts > 10 hours (may waive second meal by mutual consent for shifts ≤ 12 hrs)
- Rest break: 10-minute net paid rest per 4 hours worked (or major fraction thereof);
  no rest required for shifts < 3.5 hours
- Premium pay for missed breaks: 1 hour of pay at regular rate per missed meal or
  rest break (_Donohue v. AMN Services_, 11 Cal. 5th 58 (2021) [VERIFY])
- _Brinker Restaurant Corp. v. Superior Court_, 53 Cal. 4th 1004 (2012): Employer must
  "provide" breaks — relieve of duty — but need not "ensure" they are taken [VERIFY]

**New York**:

- 30-minute meal break for shifts > 6 hours between 11 am and 2 pm (factory workers:
  60 minutes)
- Noontime meal break additional to any other

**Colorado** (COMPS Order No. 38):

- 30-minute unpaid meal break for shifts of 5+ consecutive hours
- 10-minute paid rest for every 4 hours of work

**Washington**:

- 30-minute meal break for shifts > 5 hours
- 10-minute paid rest for every 4 hours of work

**Oregon**:

- Meals: 30-minute unpaid for shifts ≥ 6 hours (or 20-min paid if work is uninterruptable)
- Rest: 10-minute paid per 4 hours

**Illinois**:

- 20-minute meal break for shifts > 7.5 hours (One Day Rest in Seven Act, 820 ILCS 140)

**Common meal and rest break violations:**

| Risk Pattern                          | Description                                               | Classification                                       |
| ------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------- |
| "Automatic deduction" timekeeping     | System deducts 30 min for meal regardless of interruption | VIOLATION if employees frequently work through meals |
| On-duty meal periods (uncompensated)  | Employees required to remain available during meals       | VIOLATION                                            |
| Rest breaks > 20 min uncompensated    | Rest breaks between 20–30 min treated as unpaid           | VIOLATION                                            |
| No second CA meal for 10+ hour shifts | Second meal period not provided in California             | VIOLATION                                            |
| Manager-managed break denial          | Supervisors pressure employees to skip breaks             | VIOLATION                                            |
| Travel time as meal period            | Compensable work time disguised as meal break             | VIOLATION                                            |

### Step 7: Timekeeping Adequacy Audit

#### 7a. FLSA Recordkeeping Requirements (29 CFR Part 516)

Every employer must maintain for **3 years** (payroll records, collective bargaining
agreements, sales and purchase records) or **2 years** (supplementary basic records,
time cards, wage rate tables, work schedules):

| Record                                                 | Retention |
| ------------------------------------------------------ | --------- |
| Employee name, address, birthdate (if under 19)        | 3 years   |
| Sex and occupation                                     | 3 years   |
| Time of day and day of week workweek begins            | 3 years   |
| Regular hourly pay rate                                | 3 years   |
| Total straight-time and overtime earnings per workweek | 3 years   |
| Total wages per period                                 | 3 years   |
| Additions/deductions from wages                        | 3 years   |
| Total hours worked per workweek                        | 3 years   |
| Date of payment and pay period                         | 3 years   |
| Time cards, wage rate tables, work/time schedules      | 2 years   |

[JURISDICTION-SPECIFIC] California requires longer retention in some cases — Labor Code
§ 1174 requires 3-year retention. New York WTPA requires records for 6 years.

#### 7b. Off-the-Clock Work Audit

The **continuous workday doctrine** requires compensation for all time from the first
principal activity to the last (IBP, Inc. v. Alvarez, 546 U.S. 21 (2005) [VERIFY]):

**Pre/post-shift activities**:

- _Integrity Staffing Solutions v. Busk_, 574 U.S. 27 (2014): Security screenings held
  not compensable because not integral/indispensable to principal work [VERIFY]
- Donning/doffing protective gear, specialized uniforms → may be compensable
- Boot-up time for mandatory work-computer logins → compensable if required (WHD opinion)

**Remote work risks**:

- Employees working outside scheduled hours without authorization
- Late-night emails, after-hours messaging on company platforms
- Employer "knows or should know" standard — actual or constructive knowledge
  (_Elwell v. Univ. Hospitals Home Care Servs._, 276 F.3d 832 (6th Cir. 2002) [VERIFY])

**Common timekeeping violations:**

| Risk Pattern                              | Description                                                                              | Classification                        |
| ----------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------- |
| Rounding errors (systematic bias)         | Rounding rules that systematically benefit employer                                      | VIOLATION                             |
| Manager time edits without worker consent | Managers reducing clocked hours                                                          | VIOLATION                             |
| Pre-shift setup uncompensated             | Required equipment setup before clock-in                                                 | AT-RISK to VIOLATION                  |
| Remote employee off-hours email           | Employer aware of after-hours work, does nothing                                         | AT-RISK to VIOLATION                  |
| "Voluntary" overtime                      | Employer says overtime requires approval; employee works overtime; employer accepts work | VIOLATION                             |
| Donning/doffing not compensated           | Specialized protective gear required for work                                            | AT-RISK (fact-specific)               |
| Security screening (integral)             | Security screening integral to principal work duties                                     | AT-RISK (post-Busk analysis required) |

### Step 8: Tip Credit and Tip Pooling Audit

_(Apply only if the employer employs tipped employees or takes a tip credit)_

**⟁ CLARIFY** — "Does the employer take a tip credit (pay tipped employees less than
the standard minimum wage)? If yes, which states?"

#### 8a. FLSA Tip Credit Mechanics (29 CFR Part 531)

- Federal minimum wage: $7.25/hour; federal tipped minimum wage: $2.13/hour
- Maximum tip credit: $5.12/hour (must notify employees before taking credit)
- Tip credit condition: Employee must retain all tips (except valid tip pools)
- If tips + cash wage < minimum wage → employer must make up the difference

**Tip credit prerequisites:**

- [ ] Employer provided notice to employees about tip credit (amount, type of work,
      tip retention right, that tip credit = wage supplement only)
- [ ] Employee's actual tips + cash wage ≥ minimum wage for every workweek
- [ ] Tipped employee works in a "tipped occupation" (regularly receives > $30/month in tips)

#### 8b. Dual Jobs Rule and Tip Credit

Current DOL approach reverts to the "dual jobs" analysis following the September 2021
Final Rule that eliminated the 80/20 rule, subsequently reinforced by 2023 litigation
developments [VERIFY current status]:

**The current framework:**

- Employer may take tip credit for time spent on duties **related** to the tipped
  occupation (related side work, setup, pre/post-shift tasks related to tipped work)
- Employer may **not** take tip credit for work in a **separate, non-tipped occupation**
  (e.g., a server who also works as a cook for part of their shift)
- [VERIFY] Confirm current Fifth Circuit and DOL positions on the dual jobs rule given
  continued litigation

#### 8c. Tip Pooling Rules (Post-2018 CAA)

The 2018 Consolidated Appropriations Act (CAA) and the 2021 DOL Final Rule established:

| Scenario                                                  | Rule                                                                                                         |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Employer takes tip credit                                 | Tip pools may include **only other tipped employees** (servers, bartenders, bussers, food runners)           |
| Employer does NOT take tip credit, pays full minimum wage | Tip pools may include **any employee** except managers, supervisors, and the employer                        |
| Managers / supervisors                                    | May **never** retain tips, regardless of whether employer takes tip credit                                   |
| Service charges                                           | Service charges that go to management are **not tips** — employer-controlled distribution of service charges |

**Common tip credit and pooling violations:**

| Risk Pattern                       | Description                                                                                      | Classification              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------- |
| Notice not provided                | Tip credit taken without prior employee notice                                                   | VIOLATION — tip credit lost |
| Tip pool includes managers         | Supervisors keeping or sharing in tip pool                                                       | VIOLATION                   |
| Back-of-house excluded (no credit) | Employer not taking tip credit but excludes BOH from pool — may be permissible; forced exclusion | Review specific pool terms  |
| Service charge treated as tip      | Mandatory service charges distributed as tips (w/o FICA treatment)                               | AT-RISK                     |
| Credit taken for "non-tipped" work | Tip credit applied to hours in a non-tipped occupation                                           | VIOLATION                   |
| Makeup not paid                    | Employee's tips fall short of minimum wage; employer doesn't supplement                          | VIOLATION                   |

### Step 9: Child Labor Compliance Audit

_(Apply if the employer employs or may employ workers under 18)_

**⟁ CLARIFY** — "Does the employer employ any workers under 18? What is the youngest
age? Are they employed in any manufacturing, warehouse, or hazardous environments?"

#### 9a. Age and Hours Restrictions (29 CFR Part 570)

**Employees 14–15 years old:**

- [ ] Hours comply: Max **3 hrs/day on school days**, **8 hrs/day on non-school days**
- [ ] Hours comply: Max **18 hrs/week during school**, **40 hrs/week outside school**
- [ ] Hours comply: Work performed only between **7 am – 7 pm** (7 am – 9 pm June 1–Labor Day)
- [ ] Work limited to permitted occupations (office, retail sales, food service excluding
      hazardous equipment, etc.)

**Employees 16–17 years old:**

- [ ] No restriction on hours (federal law)
- [ ] Not employed in **17 Hazardous Occupations Orders (HOs)** (29 CFR § 570.50–.68):
      Manufacturing explosives, mining, logging, power-driven woodworking machines, wrecking
      demolition, roofing, excavation, power-driven hoisting apparatus, power-driven circular
      saws/band saws, power-driven metal forming, slaughtering/meatpacking, power-driven bakery
      machines, power-driven paper products machines, manufacturing brick/tile, operating
      power-driven elevators, coal mining, forest firefighting

[JURISDICTION-SPECIFIC] Many states have stricter requirements — California, New York,
and others restrict hours for 16–17 year olds and have additional prohibited occupations.

#### 9b. 2023–2024 DOL Enforcement Context

The DOL significantly increased child labor enforcement:

- FY 2023: 955 employers cited; approximately 5,800 children identified in violations
- Focus on exploitative conditions, undocumented minor workers, hazardous environment placements
- Expanded use of civil monetary penalties (up to $15,625 per violation under 29 CFR Part 579)
- [VERIFY] Check current civil monetary penalty amounts — subject to annual inflation adjustments

**Common child labor violations:**

| Risk Pattern                   | Description                                                  | Classification       |
| ------------------------------ | ------------------------------------------------------------ | -------------------- |
| Hours in excess (school weeks) | 14–15 year olds exceeding 18 hrs/week during school          | VIOLATION            |
| Prohibited occupations (16–17) | Minors operating power-driven equipment in HO categories     | VIOLATION            |
| No age documentation           | No employment certificate or proof of age for minors         | AT-RISK              |
| Hazardous site placements      | Minors placed in warehouse, construction, or food processing | AT-RISK to VIOLATION |
| Late-night work (14–15)        | Work after 7 pm during school year                           | VIOLATION            |

### Step 10: Predictive Scheduling Compliance Audit

_(Apply if the employer operates in any covered jurisdiction)_

**⟁ CLARIFY** — Confirm exact operating locations to identify applicable ordinances.

**Covered jurisdictions as of early 2026** [VERIFY CURRENT for amendments]:

| Jurisdiction       | Industries Covered                                               | Advance Notice                         | Predictability Pay          |
| ------------------ | ---------------------------------------------------------------- | -------------------------------------- | --------------------------- |
| Oregon (statewide) | Retail, hospitality, food service (500+ employees)               | 14 days                                | Varies by notice given      |
| New York City      | Retail (20+ US locations), fast food (5+ NYC locations)          | 72 hours (retail); 14 days (fast food) | Varies                      |
| Chicago            | Retail (100+ employees globally)                                 | 14 days                                | 1 hr pay per < 24-hr notice |
| Seattle            | Manufacturing, retail, hospitality, food service (500+ globally) | 14 days                                | 1/2 pay per cancelled hr    |
| San Francisco      | Formula retail (40+ global locations)                            | 2 weeks                                | Varies                      |
| Philadelphia       | Retail (250+ employees globally)                                 | 2 weeks                                | 1 hr pay per change         |
| Emeryville, CA     | Retail, hospitality (56+ globally)                               | 2 weeks                                | Varies                      |
| Los Angeles County | Retail (300+ employees globally)                                 | 14 days                                | Varies                      |
| Berkeley, CA       | Retail, hotel, healthcare, warehouse (56+)                       | 2 weeks                                | Varies                      |
| Denver, CO         | Retail, food service, hospitality                                | 14 days                                | Varies                      |

[VERIFY CURRENT] This table was compiled as of early 2026. Ordinances are frequently
amended; confirm effective dates, industry scopes, and employer size thresholds.

**Common predictive scheduling violations:**

| Risk Pattern                              | Description                                                          | Classification |
| ----------------------------------------- | -------------------------------------------------------------------- | -------------- |
| No advance schedule posting               | Schedule not posted 14 days in advance in covered jurisdiction       | VIOLATION      |
| Last-minute changes without premium       | Schedule changed < 24–72 hrs before shift without predictability pay | VIOLATION      |
| Right to rest violations                  | Employee required to work < 10 hours after prior shift ends          | VIOLATION      |
| No good faith offer to existing employees | Hours added without offering to current employees first              | VIOLATION      |
| No written schedule documentation         | No records of schedule posting dates                                 | AT-RISK        |

### Step 11: Pay Stub and Record-Keeping Compliance Audit

#### 11a. Federal FLSA Recordkeeping (29 CFR Part 516)

_(Reviewed in Step 7a — cross-reference for completeness)_

Check that all required records are:

- [ ] Complete (all 14 required data elements present)
- [ ] Accessible and organized for WHD review
- [ ] Retained for the required periods (2–3 years as above)

#### 11b. State Pay Stub Requirements

**California** (Labor Code § 226 — most stringent):

Required on every wage statement:

1. [ ] Gross wages earned
2. [ ] Total hours worked (exempt employees excluded only from hours worked, not from
       other required items)
3. [ ] Number of piece-rate units earned and applicable rate (if applicable)
4. [ ] All deductions
5. [ ] Net wages earned
6. [ ] Dates of pay period
7. [ ] Employee name and last four digits of SSN or employee ID
8. [ ] Employer name and address
9. [ ] All applicable hourly rates and corresponding hours worked (including any different
       rates for overtime, double time, etc.)

Violation: $50 per employee per pay period for initial violations; $100 per pay period
for subsequent violations; up to $4,000 per employee aggregate + PAGA exposure.

**New York** (NY Labor Law Art. 6 — WTPA):

- Wage statement: regular rate, OT rate, regular hours, OT hours, gross wages, deductions,
  net wages, dates of pay period, employer name/address/phone
- Annual written notice of wage rate (at hiring and any change)

**Texas** (Texas Payday Law):

- Itemized pay stub showing earnings and deductions [VERIFY]
- No specific itemization requirement at federal level beyond FLSA records

[JURISDICTION-SPECIFIC] For all other states: identify the specific pay stub statute and
enumerate required elements.

---

## Severity Classification System

Apply one of three classifications to each finding:

### COMPLIANT

**Definition**: Practice meets all applicable federal and state requirements without
any identified risk.
**Response**: Note for audit record. No remediation required.

### AT-RISK

**Any one of:**

- Practice meets a technical requirement but creates meaningful litigation or WHD
  audit risk given current enforcement trends
- Insufficient documentation to verify compliance
- Practice acceptable under federal law but may violate a state-specific rule
  (confirm state applicability)
- Ambiguous fact pattern where reasonable classification is difficult — requires
  legal review before confirmation

**Response**: Flag for legal review. Implement documentation improvements. Monitor for
regulatory developments. Estimate contingent exposure.

### VIOLATION

**Any one of:**

- Clear failure to comply with a specific FLSA or applicable state wage and hour requirement
- Incorrect classification that would result in unpaid overtime or minimum wage liability
- Missing required records, pay stub elements, or advance schedule notice in covered jurisdiction
- Regulatory requirement not being met — regardless of whether a claim has been filed

**Response**: Immediate remediation. Calculate back pay exposure. Implement policy and
system changes. Evaluate voluntary disclosure vs. defensive posture.

### Severity Tiers Within Classification

For VIOLATION findings, apply a priority tier:

| Tier                       | Scope                                                                                    | Examples                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Tier 1 — Immediate**     | Systemic violations affecting large populations; high per-period exposure; ongoing harm  | Widespread exempt misclassification; regular rate omission for non-discretionary bonus  |
| **Tier 2 — High Priority** | Significant violations with quantifiable back pay; limited to specific groups or periods | Missing meal break premium for one work group; tip credit notice not given to one class |
| **Tier 3 — Standard**      | Technical violations with lower financial exposure; documentation gaps; single-incident  | Single pay stub missing required element; workweek not formally documented              |

---

## Exposure Quantification Framework

For each VIOLATION finding, calculate exposure using the following framework:

### Back Pay Calculation

```
For hourly non-exempt overtime underpayment:
  Back pay = Underpaid overtime premium per week × Affected weeks × Affected employees

  Where: Underpaid OT premium = (Correct regular rate × 1.5 × OT hours)
                                 - (Actual OT rate × OT hours)

For exempt misclassification:
  Back pay = Actual overtime hours worked × (Regular rate × 0.5 or 1.5 depending on method)

  Where: Regular rate = Total compensation / Total hours worked
  And: OT method = Half-time (fluctuating) or time-and-a-half
  Conservative approach: Use 1.5× on all OT hours until FWW agreement is established
```

### Liquidated Damages

Under 29 U.S.C. § 216(b): **Equal amount of back pay** as liquidated damages, unless
the employer demonstrates good faith and reasonable grounds for believing no violation
occurred (29 U.S.C. § 260 — court discretion).

**Practical approach**: Budget **2× back pay** as conservative exposure estimate (back
pay + equal liquidated damages).

Note: The Trump DOL has signaled reduced emphasis on liquidated damages in WHD
investigations [VERIFY current DOL enforcement policy as of audit date].

### Statutes of Limitations

| SOL Period                       | Applies When                                                                                                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2 years** (29 U.S.C. § 255(a)) | Non-willful FLSA violations                                                                                                                                          |
| **3 years** (29 U.S.C. § 255(a)) | Willful violations — employer knew or recklessly disregarded whether its conduct violated the FLSA (_McLaughlin v. Richland Shoe Co._, 486 U.S. 128 (1988) [VERIFY]) |

[JURISDICTION-SPECIFIC] State SOLs may be longer:

- California: 3 years for California Labor Code claims (CCP § 338); PAGA: 1 year for
  filing LWDA notice + 65 days before filing suit
- New York: 6 years for NY Labor Law violations
- New Jersey: 6 years
- **Use the longer SOL** when both federal and state claims apply

### Class and Collective Action Exposure

- **FLSA collective action** (§ 216(b)): Opt-in mechanism; employees with similar
  situations to the named plaintiff
- **State class action** (Rule 23 or state equivalent): Opt-out; typically broader reach
- **PAGA** (California): Civil penalty action on behalf of LWDA; no class certification
  required; penalties flow primarily to LWDA (75%) with 25% to aggrieved employees

**PAGA penalties** [VERIFY current amounts post-2024 PAGA reforms]:

- Per pay period per aggrieved employee: $100 (initial) / $200 (subsequent)
- 2024 PAGA reform (SB 92, effective July 1, 2024): Caps on penalties, cure mechanism,
  increased LWDA involvement [VERIFY current penalty cap and cure provisions]

### Exposure Estimate Template

For each VIOLATION finding, complete:

```
Finding: [description]
Affected population: [number of employees]
Average hours of underpayment per week: [hours]
Average regular rate: $[rate]/hour
Back pay per employee per week: $[calculation]
Audit period weeks: [weeks] ([SOL period] × 52)
Total estimated back pay exposure: $[total]
Liquidated damages (1× back pay): $[total]
Attorney fees and costs (estimate): $[estimate]
State penalties (if applicable): $[estimate]
TOTAL ESTIMATED EXPOSURE: $[grand total]
Confidence: [HIGH / MEDIUM / LOW]
Note: [assumptions, limitations, factors that could increase or decrease exposure]
```

---

## Prioritization Framework

Prioritize findings as follows:

| Priority           | Criteria                                                                                                                       | Action                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **P1 — Immediate** | Ongoing violation affecting 10+ employees; >$100K estimated exposure; willful violation risk; regulatory investigation pending | Immediate remediation plan; legal escalation; voluntary disclosure analysis |
| **P2 — High**      | Moderate population affected; $25K–$100K exposure; clear violation but good faith defense possible                             | Remediation within 30 days; policy and system changes; document good faith  |
| **P3 — Standard**  | Technical violation; <$25K exposure; documentation gap; single-group issue                                                     | Remediation within 90 days; implement preventive controls                   |
| **P4 — Watch**     | AT-RISK (no current violation); exposure contingent on regulatory shift; fact-specific analysis needed                         | Monitor; legal review recommended; maintain documentation                   |

---

## Citation Quality Gates

Run these 5 gates silently before delivering audit output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                              | Fail Action                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific FLSA provision, 29 CFR section, DOL guidance, or established state law                                         | Add citation or mark "[UNVERIFIED]"                              |
| **Format**     | All citations follow a recognizable format (e.g., "29 CFR § 778.109", "29 U.S.C. § 207(a)")                                                       | Fix format                                                       |
| **Currency**   | Every threshold figure (salary threshold, minimum wage, penalty amount) flagged as [VERIFY CURRENT] or confirmed against current DOL/state source | Flag all figures not confirmed from current authoritative source |
| **Domain**     | Analysis stays within wage and hour law — does not stray into tax, ERISA, or other domains without noting the scope shift                         | Remove or flag out-of-domain content                             |
| **Confidence** | Uncertainty is stated explicitly — no disguised speculation                                                                                       | Add confidence qualifier                                         |

---

## Self-Interrogation for Tier 1 Violations

For any finding classified as **VIOLATION — Tier 1**, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the violation follow logically from the cited
statute or regulation? Would a WHD investigator or plaintiffs' attorney actually reach
this conclusion on these facts? Are there affirmative defenses (good faith, de minimis,
administrative exemption nuance) that could change the analysis?

**Pass 2 — Completeness**: Have all relevant exemptions, exceptions, and safe harbors
been considered? Does the fact pattern trigger any industry-specific exemption that might
apply? Is the state law correctly identified and applied?

**Pass 3 — Challenge**: What is the strongest argument that this is NOT a violation?
Under what circumstances could a reasonable employer — applying the same facts — have
reached a different conclusion in good faith? Does this change the Tier classification
or the exposure estimate?

---

## Confidence Scoring

Apply to each finding:

| Level        | Range     | Meaning                                                                       | Action                                                |
| ------------ | --------- | ----------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory or regulatory violation on undisputed facts                   | State as VIOLATION with full confidence               |
| **High**     | 0.80–0.94 | Strong basis; minor factual ambiguity or emerging legal question              | State as VIOLATION with brief caveat                  |
| **Probable** | 0.60–0.79 | Good argument for violation; fact-dependent; reasonable minds could differ    | State as AT-RISK with analysis of both sides          |
| **Possible** | 0.40–0.59 | Genuine uncertainty — depends on courts or regulator position not yet settled | Flag for legal review; present both sides             |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; facts may distinguish                                | Do not classify as violation; note as background risk |

---

## Anti-Patterns

What NOT to do when conducting a wage and hour compliance audit:

1. **Relying on job titles** — FLSA exemptions turn on actual duties performed, not job
   title or job description. "Manager" does not mean exempt. "Administrative Coordinator"
   does not mean administrative exemption. Audit actual work performed.

2. **Using the 2024 DOL salary thresholds** — The November 2024 Texas court vacatur
   restored the 2020 rule ($684/week, $107,432 HCE). Using the vacated $844/week
   threshold as the operative rule would produce incorrect compliance conclusions.

3. **Assuming discretionary bonus exclusion** — The "discretionary" exclusion from the
   regular rate is narrow. If the bonus is announced in advance, tied to performance,
   or regularly paid, it is almost certainly non-discretionary and must be included in
   the regular rate.

4. **Applying a biweekly or semi-monthly overtime calculation** — FLSA overtime is
   calculated by workweek (a fixed 7-consecutive-day period), not by the pay period.
   Biweekly pay periods may average away overtime that accrued in the higher week.

5. **Treating comp time as lawful for private employers** — Compensatory time off in lieu
   of overtime is unlawful for private sector employers under the FLSA. Only state and
   local government employers may offer comp time (29 U.S.C. § 207(o)).

6. **Ignoring state law preemption** — FLSA is a floor, not a ceiling. Auditing only
   federal law in California or New York will miss most of the real exposure. Always
   identify the more protective state or local law and apply it.

7. **Accepting FWW without checking prerequisites** — Fluctuating workweek overtime is
   not universally available. It requires: genuine fluctuation in hours, clear mutual
   understanding, salary sufficient for minimum wage, and is prohibited outright in some
   states (California, Alaska [VERIFY]).

8. **Missing the regular rate recalculation for retroactive bonuses** — When a
   non-discretionary bonus is paid after the workweek it relates to, the employer must
   retroactively recalculate the regular rate and pay additional overtime premiums for
   every workweek covered by the bonus. Many employers miss this step.

9. **Confusing "service charges" with "tips"** — Mandatory service charges added by the
   employer to customer bills are not tips under the FLSA. They belong to the employer
   unless voluntarily distributed as wages. Tax treatment differs. Misclassification
   distorts regular rate calculations and tip credit analysis.

10. **Failing to track the dual jobs / non-tipped work** — An employer taking a tip
    credit must track when tipped employees work in a second, non-tipped occupation
    and pay full minimum wage for those hours. Failure to track this is a frequent
    WHD audit finding in the food service industry.

11. **Treating automatic time deductions as legally safe** — Automatic meal break
    deduction policies are facially lawful but create systematic violations when employees
    regularly work through breaks. The practice must be paired with an affirmative policy
    for employees to report interrupted breaks and with manager training.

12. **Underestimating child labor exposure** — The 2023–2024 WHD enforcement surge
    dramatically increased child labor penalties and investigations. Employers using
    staffing agencies or subcontractors should be alert to joint employer liability for
    any child labor violations by their staffing partners.

13. **Ignoring "constructive knowledge" of off-the-clock work** — An employer cannot
    benefit from overtime work and then deny compensation by claiming it did not authorize
    the work. If the employer knew or should have known off-the-clock work was occurring,
    it is compensable regardless of authorization policies.

14. **Applying one-size-fits-all remediation** — Different violations have different
    remediation paths. Misclassification may require reclassification + back pay + system
    changes. Regular rate errors require recalculation + retroactive payment. Break
    violations require premium pay + policy revision. Do not apply the same fix to
    structurally different violations.

15. **Forgetting the 3-year SOL for willful violations** — If the employer had prior
    WHD investigations, received DOL opinion letters about the practice, or internal
    legal advice flagging the issue, the 3-year willful SOL likely applies — doubling
    the exposure calculation for the extra year.

16. **Neglecting predictive scheduling jurisdictions in retail or food service** —
    Employers in covered cities who don't post advance schedules face per-violation
    predictability pay penalties that accumulate quickly across a large hourly workforce.

17. **Assuming compliance because no claims have been filed** — Private litigation
    underrepresents actual wage violations. WHD can initiate investigations without
    a complaint, and class counsel actively investigates high-value sectors. No claims
    filed ≠ compliant.

18. **Using state minimum wage as the regular rate floor** — The regular rate must be
    at least the applicable minimum wage, but it is determined by actual compensation
    paid — not by the minimum wage. A higher actual rate does not "wash" against an
    improper overtime calculation.

19. **Missing the joint employer analysis** — Where an employer uses staffing agencies,
    contractors, or franchise arrangements, joint employer status under the FLSA may
    expose the primary employer to liability for the staffing entity's wage violations.
    DOL's January 2024 independent contractor final rule (29 CFR Part 795) [VERIFY
    current status under Trump administration] is relevant here.

20. **Failing to document good faith efforts** — Employers who are actively trying to
    comply — documented legal opinions, regular audits, prompt remediation when errors
    found — may defeat or reduce liquidated damages. Document the compliance program;
    it is an asset in any WHD investigation or litigation.

---

## Writing Standards

Before delivering any audit output, apply these quality gates:

1. **Specificity**: Every finding cites the specific statutory or regulatory provision.
   "Violation of the FLSA" is insufficient — specify "Violation of 29 U.S.C. § 207(a)(1)
   and 29 CFR § 778.208 — non-discretionary bonus excluded from regular rate."

2. **Quantification**: Every VIOLATION finding includes an exposure estimate or explains
   clearly why quantification is not possible with available information.

3. **Remediation**: Every VIOLATION finding includes at least one specific remediation
   action — not just identification of the problem.

4. **Hedging accuracy**: [VERIFY CURRENT] tags appear on all threshold figures (minimum
   wages, salary thresholds, penalty amounts) where currency cannot be independently
   confirmed in the current session.

5. **State law specificity**: "State law may vary" is never sufficient. Identify the
   specific state law and its specific requirement.

6. **Plain language**: Legal conclusions stated in plain language alongside technical
   citations. Avoid acronym chains without initial definition.

7. **Actionability**: The audit report is a remediation roadmap, not just a list of
   problems. Each section concludes with "What to do."

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for: current FLSA salary thresholds, state minimum wage schedules,
  WHD opinion letters, current civil monetary penalty amounts, recent WHD enforcement
  statistics, state predictive scheduling ordinance text
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Save research to `/tmp/legalcode-wage-hour-authority.md`

**Without legalcode-mcp:**

- Mark all threshold figures, minimum wages, and penalty amounts with [VERIFY CURRENT]
- Recommend that the user cross-reference:
  - DOL WHD website: dol.gov/agencies/whd
  - State labor agency websites for each operating state
  - DOL Wage and Hour Division opinion letters database
- Note in Glass Box: `legalcode_mcp: "Not connected — all thresholds require verification"`

---

## Localization Notes

When conducting the audit for states beyond California, New York, Colorado, Alaska,
Washington, Oregon, and Illinois, conduct state-specific research for:

1. **Minimum wage**: State and any applicable local (city/county) rates — check DOL
   state minimum wage chart and confirm with state labor agency
2. **Daily overtime**: Only a few states (CA, CO, AK) mandate daily overtime — confirm
3. **Meal and rest breaks**: Identify statute and any industry-specific exceptions
4. **Salary basis test**: Some states have higher thresholds than federal — NY, CA, CO
5. **Pay stub requirements**: Enumerate required elements under state law
6. **Record-keeping retention**: State-specific retention periods may exceed federal
7. **PAGA-equivalent statutes**: Some states have similar private enforcement mechanisms
8. **Predictive scheduling**: Confirm whether any city/county ordinance covers employer

Use [JURISDICTION-SPECIFIC] markers throughout the audit output for elements that require
state-specific verification.

---

## Output Format Template

Deliver the audit report in the following format:

```markdown
# Wage and Hour Compliance Audit Report

## [Employer / Audit Scope]

**Audit Date**: [date]
**Audit Period**: [period covered by SOL analysis]
**Jurisdictions Reviewed**: [list]
**Prepared by**: AI-assisted (legalcode-wage-hour-compliance-audit) — requires attorney review

---

## Executive Summary

| Category              | Finding                 | Tier   |
| --------------------- | ----------------------- | ------ |
| Exempt Classification | [summary]               | [Tier] |
| Overtime Calculation  | [summary]               | [Tier] |
| Meal/Rest Breaks      | [summary]               | [Tier] |
| Timekeeping           | [summary]               | [Tier] |
| Tip Credit/Pooling    | [summary if applicable] | [Tier] |
| Child Labor           | [summary if applicable] | [Tier] |
| Predictive Scheduling | [summary if applicable] | [Tier] |
| Pay Stubs/Records     | [summary]               | [Tier] |

**Total Estimated Exposure**: $[range]
**Highest Priority Finding**: [description]

---

## Detailed Findings

### [Category 1] — Exempt Classification

#### Finding [#]: [Title]

**Classification**: VIOLATION / AT-RISK / COMPLIANT
**Tier**: 1 / 2 / 3 (if Violation)
**Legal Basis**: [statute/regulation]
**Confidence**: [level] — [rationale]

**Facts**: [description of the specific practice or position audited]

**Analysis**: [explanation of why this is or is not a violation]

**Exposure Estimate**:

- Affected employees: [#]
- Back pay exposure: $[amount] ([calculation basis])
- Liquidated damages: $[amount]
- State penalties: $[amount if applicable]
- Total estimated exposure: $[amount]
- SOL applied: [2/3 years — rationale]

**Remediation**:

1. [Specific action — immediate]
2. [Specific action — 30-day]
3. [Specific action — systemic/preventive]

**What to do**: [Plain-language summary of the remediation path]

---

[Repeat for each finding]

---

## Remediation Roadmap

| Priority | Finding   | Action   | Owner             | Deadline  |
| -------- | --------- | -------- | ----------------- | --------- |
| P1       | [finding] | [action] | [suggested owner] | Immediate |
| P2       | [finding] | [action] | [suggested owner] | 30 days   |
| P3       | [finding] | [action] | [suggested owner] | 90 days   |

---

## Total Exposure Summary

| Violation Category | Back Pay  | Liquidated Damages | State Penalties | Total     |
| ------------------ | --------- | ------------------ | --------------- | --------- |
| [Category]         | $[amount] | $[amount]          | $[amount]       | $[amount] |
| **TOTAL**          | $[amount] | $[amount]          | $[amount]       | $[amount] |

**Conservative estimate**: $[low range]
**Aggressive plaintiff estimate**: $[high range]
**Recommended reserve**: $[suggested reserve]

---

## Recommended Next Steps

1. [Immediate priority action]
2. [Legal engagement recommendation]
3. [Payroll system or policy change]
4. [Future audit schedule]
5. [Voluntary disclosure analysis if applicable]
```

---

## Glass Box Audit Trail

Complete this template and include in every audit output:

```yaml
glass_box:
  skill_name: "legalcode-wage-hour-compliance-audit"
  audit_date: "[date]"
  jurisdiction: "US federal + [states listed]"
  industry: "[employer industry]"
  workforce_composition: "[description]"
  audit_scope: "[full / priority / pre-litigation / due diligence]"
  audit_period_years: "[number]"
  sol_applied: "[2-year standard / 3-year willful — rationale]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-wage-hour-authority.md / Not created"
  operative_flsa_salary_threshold: "$684/week ($35,568/year) — 2020 DOL rule post-2024-vacatur [VERIFY CURRENT]"
  operative_hce_threshold: "$107,432/year — 2020 DOL rule post-2024-vacatur [VERIFY CURRENT]"
  total_findings: "[number]"
  violations: "[number]"
  at_risk: "[number]"
  compliant: "[number]"
  tier_1_violations: "[number]"
  estimated_exposure_range: "$[low] – $[high]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED / VERIFY CURRENT]"
  limitations:
    - "All salary thresholds and minimum wage rates require verification against current DOL and state sources"
    - "State law analysis limited to states identified in Step 2 — confirm complete operating geography"
    - "Exposure estimates based on information provided — actual exposure may differ based on complete payroll records"
    - "PAGA exposure (if California) highly variable — consult California employment counsel before settlement"
    - "[Any additional scope limitations or assumptions]"
  reviewer: "AI-assisted — requires qualified employment attorney review before any remediation, filing, or disclosure"
```

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis drawing on:

- FLSA statutory text (29 U.S.C. §§ 201–219)
- DOL WHD regulations (29 CFR Parts 516, 531, 570, 778, 785)
- DOL Field Operations Handbook and WHD opinion letters
- _State of Texas v. U.S. DOL_, E.D. Tex. (Nov. 15, 2024) — vacating 2024 Final Rule
- _McLaughlin v. Richland Shoe Co._, 486 U.S. 128 (1988) — willful violation SOL
- _IBP, Inc. v. Alvarez_, 546 U.S. 21 (2005) — continuous workday doctrine
- _Integrity Staffing Solutions v. Busk_, 574 U.S. 27 (2014) — preliminary/postliminary
- _Brinker Restaurant Corp. v. Superior Court_, 53 Cal. 4th 1004 (2012) — CA meal breaks
- 2018 Consolidated Appropriations Act — tip pooling amendments
- DOL Final Rule on tip regulations (September 2021)
- California Labor Code §§ 226, 510, 515, 515.5, 1174; IWC Wage Orders
- NY Labor Law Art. 6 (WTPA); Colorado COMPS Order No. 38
- Oregon ORS 653.450 et seq. (predictive scheduling)
- 2024 California PAGA reform (SB 92, effective July 1, 2024)
- Legalcode reference standard: `legalcode-contract-review` quality framework
- Legalcode related skills: `legalcode-independent-contractor-classification`,
  `legalcode-employment-agreement-review`, `legalcode-employee-handbook-review`

All citations carry [VERIFY] risk — verify against current authoritative sources.
