---
name: legalcode-jp-labor-standards-compliance
description: 'Assess compliance with Japanese labor law for employers operating in Japan. Covers the Labor
  Standards Act (労働基準法, LSA), work rules (就業規則 shugyo kisoku), Article 36 overtime agreements (三六協定),
  annual paid leave mandatory designation (年次有給休暇), dismissal restrictions and the abuse of right doctrine
  (解雇権濫用法理), fixed-term employment 5-year conversion rule (無期転換申込権, Labor Contract Act Article 18), Work
  Style Reform Act (2018) overtime caps and equal pay for equal work obligations, minimum wage compliance,
  childcare and family care leave (育児・介護休業法), workplace harassment prevention obligations, and social
  insurance enrollment. Use when conducting a Japan HR compliance audit, reviewing employment practices
  for a Japan market entry, assessing risk before dismissal actions, or advising on work rule drafts.
  Triggers on: Japan labor law, rodo kijun ho, 36 agreement, sangyo kyotei, shugyo kisoku, mukitenkan,
  karoshi compliance, Work Style Reform, Japan overtime caps, Japan employment compliance.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — Japan Labor Standards Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted assessment of Japanese
> labor law compliance. It does not constitute legal advice. All outputs must be reviewed
> by a qualified Japanese labor attorney (弁護士) or labor/social insurance consultant
> (社会保険労務士) before use. Japanese labor law is dense, rapidly amended, and
> enforcement-intensive — the stakes of errors are high. Statutory and case law references
> carry hallucination risk; verify every citation against authoritative sources (e-Gov,
> MHLW, japaneselawtranslation.go.jp) before relying on them.

---

## Purpose and Scope

This skill assesses an employer's compliance posture against core Japanese labor law
obligations. It produces a findings report classifying each area as COMPLIANT, PARTIAL,
or NON-COMPLIANT, with actionable remediation steps and priority rankings.

**Covers:**

- Working hours, rest periods, and statutory overtime limits
- Article 36 overtime agreements (36 kyōtei) — execution, filing, and adherence
- Annual paid leave — accrual, mandatory 5-day designation, and record-keeping
- Work rules (shugyo kisoku) — existence, content, filing, and currency
- Dismissal restrictions — notice, prohibited periods, and the abuse of right doctrine
- Fixed-term employment — 5-year conversion rule and cooling-off period traps
- Work Style Reform Act — overtime caps as hard law and equal pay for equal work
- Minimum wage — regional and industry-specific compliance
- Childcare and family care leave obligations (including 2022 amendments)
- Workplace harassment prevention — power, sexual, and maternity harassment
- Social insurance enrollment — health, pension, employment, and accident insurance
- Document retention requirements

**Does not:**

- Provide legal advice or substitute for counsel
- Cover individual dispute resolution strategy (see litigation skills)
- Cover immigration or work permit compliance
- Address tax, corporate, or customs compliance

---

## Jurisdiction and Governing Law

**Jurisdiction**: Japan (国内法)

**Primary statutes** (all JAPAN-SPECIFIC):

- Labor Standards Act (労働基準法, Act No. 49 of 1947, as amended)
- Labor Contract Act (労働契約法, Act No. 128 of 2007, as amended)
- Minimum Wage Act (最低賃金法, Act No. 137 of 1959)
- Act on Childcare Leave and Family Care Leave (育児・介護休業法, Act No. 76 of 1991, as amended 2022)
- Act on Comprehensive Promotion of Labor Policies (労働政策総合推進法, as amended 2020) — harassment prevention
- Act on the Arrangement of Related Acts to Promote Work Style Reform (働き方改革関連法, Act No. 71 of 2018)
- Social Insurance Acts: Health Insurance Act, Employees' Pension Insurance Act, Employment Insurance Act, Workers' Accident Compensation Insurance Act

**Legal system**: Civil law (Continental European tradition), supplemented by Labor Tribunal and court-developed doctrine. The abuse of right doctrine (解雇権濫用法理) is codified in the Labor Contract Act following decades of Supreme Court precedent development.

**Enforcement authority**: Ministry of Health, Labour and Welfare (MHLW, 厚生労働省) and its network of 321+ Labor Standards Inspection Offices (労働基準監督署, rōdō kijun kantoku-sho) nationwide.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- Employer size, industry, or workforce composition changes which rules apply
- The assessment requires document review that has not been provided
- Remediation options depend on business constraints not yet stated
- Recent statutory amendments may or may not apply depending on effective dates

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

### Step 1: Accept the Assessment Scope

Accept scope in any of these formats:

- **Questionnaire responses**: Employer's answers to a structured HR compliance questionnaire
- **Document set**: Work rules, 36 Agreement, time records, payroll data, employment contracts, leave ledgers
- **Verbal description**: Description of current practices provided in conversation
- **Partial scope**: Focus on one or more specific compliance areas

If no scope or documents are provided, proceed to Step 2 to gather context.

### Step 2: Gather Employer Context

**⟁ CLARIFY** — Ask the user these questions before beginning. Skip any already answered:

1. **Employer type and size**:
   - Options: Fewer than 10 employees | 10-29 employees | 30-99 employees | 100-299 employees | 300+ employees | Publicly listed company
   - _Why this matters_: Work rules are mandatory only at 10+. Some obligations have SME phase-in dates. Harassment law applied to 50+ employers from 2020 and all employers from April 2022.

2. **Industry**:
   - Options: Construction | Transportation/logistics | Healthcare/medical | Manufacturing | IT/technology | Retail/hospitality | Financial services | Other
   - _Why this matters_: Construction and transport were previously exempt from 36 Agreement caps — that exemption ended April 1, 2024. Medical professionals have special overtime rules. Industry-specific minimum wages may apply.

3. **Workforce composition**:
   - Options: Regular full-time only | Mix of regular and fixed-term/part-time | Significant use of fixed-term contracts | Workers approaching 5-year cumulative threshold
   - _Why this matters_: Fixed-term rules, equal pay obligations, and indefinite conversion risk depend on workforce composition.

4. **Assessment trigger**:
   - Options: Routine compliance audit | Pre-dismissal risk assessment | Market entry preparation | LSIO inspection follow-up | M&A due diligence | Other
   - _Why this matters_: Determines which areas to assess most deeply and what remediation urgency applies.

5. **Documents available**:
   - Options: Full document set | Partial (specify) | No documents — verbal description only
   - _Why this matters_: Document gaps are themselves a compliance finding; affects depth of analysis.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** if connected to retrieve:

- Current text of Labor Standards Act, Labor Contract Act, and relevant regulations
- Recent MHLW guidance and enforcement priorities
- Relevant Supreme Court and Labor Tribunal decisions on dismissal, overtime, and conversion

Save results to `/tmp/jp-labor-compliance-authority.md`.

If legalcode-mcp is not connected:

- Mark all statutory citations [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using authoritative English translations at japaneselawtranslation.go.jp [VERIFY for currency]

### Step 4: Compliance Assessment

Assess each of the 14 compliance areas below (Steps 4a–4n). For each:

- Classify as COMPLIANT, PARTIAL, or NON-COMPLIANT
- State the specific legal requirement and cite the governing provision
- Identify any gap between requirement and actual practice
- Assign a remediation priority (CRITICAL / HIGH / MEDIUM / LOW)

**⟁ CLARIFY** — For assessments based on verbal description without documents:
Ask the user to confirm key facts before classifying any area as NON-COMPLIANT:

- "You mentioned overtime work happens regularly. Has a valid 36 Agreement been filed with the LSIO, and do you have a copy?"
- "You mentioned you have 12 employees. Do written work rules exist, even if informal?"
- "You have fixed-term workers with more than 3 years' service. Has any conversion request been received or anticipated?"

### Step 5: Apply Severity Classification

Apply the three-tier classification defined in **Compliance Severity Classification** below
to each finding. For NON-COMPLIANT findings, apply Self-Interrogation before delivery.

### Step 6: Generate Remediation Actions

For each PARTIAL or NON-COMPLIANT finding, produce a specific remediation action using
the **Remediation Action Format** below.

**⟁ CLARIFY** — For findings with multiple remediation paths, present options:

- "The 36 Agreement is missing. You can file a standard agreement (no special overtime) or a special-circumstance agreement (higher caps with additional requirements). Which better fits your business needs?"
- "Three fixed-term employees have crossed the 5-year threshold. Have they received conversion offers? If not, you must provide them. Do you want draft language for the conversion offer?"

### Step 7: Produce Priority Action Plan

Organize all NON-COMPLIANT and PARTIAL findings into a prioritized remediation roadmap
using the **Prioritization Framework** below.

### Step 8: Quality Verification

Before delivering the assessment:

1. Run the 5 Citation Quality Gates silently.
2. For every NON-COMPLIANT finding, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to all material findings.
4. Generate the Glass Box Audit Trail and append it to the output.

---

## Compliance Assessment Reference

### 4a. Working Hours and Rest Periods

**Governing law**: LSA Articles 32, 34, 35 [VERIFY currency]

**Requirements**:

- Standard working hours: Maximum 40 hours per week, 8 hours per day (Art. 32)
- Exception: Variable hour systems (変形労働時間制) may spread hours over reference periods (1-week, 1-month, or 1-year flexible hour systems) with proper agreement
- Mandatory rest breaks: 45 minutes for shifts exceeding 6 hours; 60 minutes for shifts exceeding 8 hours (Art. 34)
- Mandatory days off: At least one full rest day per week, or four days per four weeks (Art. 35)
- Any hours beyond the statutory limits require a valid 36 Agreement (see 4b)

**Documents to review**:

- Time records (actual hours worked, not just scheduled hours)
- Payroll records (to cross-check premium pay)
- Employment contracts (stated working hours)
- Variable hour system agreements, if used

**Common compliance failures**:

- Employees working systematically beyond statutory limits without a valid 36 Agreement
- Rest breaks not actually taken (common in retail/hospitality)
- Time records showing only scheduled hours, not actual hours
- "Off the clock" work (サービス残業, unpaid overtime) — a criminal violation

**LSIO enforcement note**: Unpaid overtime (サービス残業) is a priority enforcement target. Inspectors commonly request the past 2 years of time records and compare them to payroll.

---

### 4b. Article 36 Agreement (36 協定, San-roku Kyōtei)

**Governing law**: LSA Article 36; Ordinance for Enforcement of LSA [VERIFY currency]

**Requirements**:

- No employer may legally require overtime or holiday work without a valid 36 Agreement [VERIFY]
- The agreement must be between the employer and a **properly elected worker representative** (過半数代表者) or, where a majority union exists, the majority union
- Worker representative must: (a) not be a manager or supervisor, (b) be elected through a democratic process free from employer influence, (c) represent the majority of workers at the workplace
- The signed agreement must be **filed with the competent LSIO** — unfiled agreements have no legal effect
- Standard overtime limits: **45 hours/month, 360 hours/year** (Art. 36(4)) [VERIFY]
- Special provisions (時間外労働の上限規制の特別条項) — allowed for extraordinary circumstances only:
  - Absolute cap: **100 hours/month** (including holiday work) [VERIFY]
  - Annual cap: **720 hours/year** (overtime only, excluding holiday work) [VERIFY]
  - Average across any 2-6 month reference period: **80 hours/month** (including holiday work) [VERIFY]
  - Special provisions cannot be used for every month — they are reserved for genuine extraordinary circumstances (e.g., seasonal peak, unexpected large order)

**2024 industry note**: Construction, transportation/logistics, and healthcare industries — previously exempt — became subject to the same caps effective April 1, 2024 (the "2024 Problem"). Employers in these sectors must now have fully compliant agreements. [VERIFY]

**Documents to review**:

- Current 36 Agreement signed by employer and worker representative
- LSIO filing receipt (受理印 or electronic receipt)
- Evidence of worker representative election (voting record or election notice)
- Actual overtime records vs. agreed limits

**Common compliance failures**:

- No 36 Agreement filed at all (makes all overtime work illegal)
- 36 Agreement filed but worker representative was appointed by management rather than independently elected — voids the agreement
- Actual overtime hours exceed the caps stated in the agreement
- Special provisions invoked every month (not permissible — reserved for genuine extraordinary circumstances)
- Agreement filed but not renewed (typically required annually)

**⟁ CLARIFY** — If the employer uses special provisions but operates in a previously exempt industry (construction, transport, healthcare), ask: "Did your 36 Agreement update to comply with the April 1, 2024 changes? This affects your current legal exposure."

---

### 4c. Overtime Premium Pay

**Governing law**: LSA Article 37 [VERIFY currency]

**Premium rates**:
| Circumstance | Minimum Premium |
|---|---|
| Ordinary overtime (legal limits exceeded) | +25% above regular wage |
| Night work (22:00–05:00) | +25% above regular wage |
| Holiday work (法定休日) | +35% above regular wage |
| Monthly overtime exceeding 60 hours | +50% above regular wage (all companies from April 1, 2023) [VERIFY] |
| Night work + overtime | +50% cumulative |
| Holiday work at night | +60% cumulative |

**Notes**:

- The 50% rate for 60+ hours/month previously applied only to large companies but was extended to SMEs effective April 1, 2023 [VERIFY]
- "Fixed overtime allowance" (固定残業代) systems are permissible only if: (a) the base amount and included hours are clearly stated, (b) actual overtime hours are tracked, and (c) additional pay is made when actual overtime exceeds the fixed allowance
- Employers cannot waive premium pay obligations through employment contracts or work rules

**Common compliance failures**:

- No tracking of overtime hours, making premium calculation impossible
- Fixed overtime allowances that cover all overtime with no top-up when hours are exceeded
- Failure to apply the 50% rate for monthly overtime exceeding 60 hours
- Night work premium not applied to late-shift or on-call workers

---

### 4d. Annual Paid Leave (年次有給休暇)

**Governing law**: LSA Article 39 [VERIFY currency]

**Accrual schedule**:
| Continuous service (with 80% attendance rate) | Days granted |
|---|---|
| 6 months | 10 days |
| 1 year 6 months | 11 days |
| 2 years 6 months | 13 days |
| 3 years 6 months | 14 days |
| 4 years 6 months | 16 days |
| 5 years 6 months | 18 days |
| 6 years 6 months or more | 20 days (maximum) |

**Mandatory 5-day designation** (effective April 1, 2019):

- Employers must **ensure each eligible employee takes a minimum of 5 days of annual paid leave per year** [VERIFY]
- This applies to all employees who have been granted 10 or more days of leave
- If an employee has not taken 5 days by year-end, the employer must designate the remaining days
- **Penalty**: Up to ¥300,000 fine per affected employee [VERIFY]

**Record-keeping**:

- Employers must maintain an **Annual Paid Leave Ledger** (年次有給休暇管理簿) per employee showing: standard accrual date, days taken, and remaining balance
- Records must be retained for **3 years** [VERIFY]

**Hourly leave option**:

- Up to 5 days/year can be taken in hourly increments, but only if a labor-management agreement is established
- Hourly leave cannot satisfy the 5-day mandatory designation requirement if taken entirely in hourly increments

**Common compliance failures**:

- No Annual Paid Leave Ledger per employee
- Employees with 10+ days accrued but fewer than 5 days taken — employer has not designated the remainder
- Incorrect accrual calculation (particularly for part-time and fixed-term employees)
- Leave records not retained for the required 3 years

---

### 4e. Work Rules (就業規則, Shugyo Kisoku)

**Governing law**: LSA Articles 89–93 [VERIFY currency]

**Requirements**:

- Employers with **10 or more regular employees** at a single workplace must have written work rules [VERIFY]
- Work rules must cover **mandatory items** including: start/end times, rest periods, holidays, leave, wages (calculation method, payroll period, payment timing, increases), and dismissal grounds
- Discretionary items include: retirement allowance, bonus, welfare benefits — if the employer provides these, they must be stated
- Employers must **consult with the worker representative or majority union** before establishing or amending rules (consultation, not consent, is required)
- Work rules must be **filed with the LSIO** to be legally binding
- Rules must be **made accessible to all employees** (posting, intranet, or individual distribution)
- Work rules serve as the **binding floor** of employment conditions — individual contracts cannot provide less than the rules

**Documents to review**:

- Current work rules (全文)
- LSIO filing receipt and any amendment filings
- Evidence of worker representative consultation

**Common compliance failures**:

- No work rules despite having 10+ employees (frequent among fast-growing startups)
- Work rules exist but are not filed with the LSIO (no legal effect for certain provisions)
- Mandatory items (dismissal grounds, wage calculation method) missing from the rules
- Rules amended without worker representative consultation
- Rules not updated to reflect statutory changes (e.g., overtime caps, childcare leave amendments)
- Rules contradict statutory minimums (automatically void under LSA Art. 93)

---

### 4f. Dismissal Restrictions

**Governing law**: LSA Articles 19–20; Labor Contract Act Articles 16–18 [VERIFY currency]

**Notice requirements** (LSA Art. 20):

- Minimum **30 calendar days' advance notice** of dismissal, OR
- Payment of **average wages for 30 days** (解雇予告手当) in lieu of notice, OR
- A combination (e.g., 15 days' notice + 15 days' wages)
- Exception: Employees dismissed for serious misconduct with LSIO approval may be dismissed without notice

**Prohibited dismissal periods** (LSA Art. 19):

- Cannot dismiss during **work-related injury/illness leave** and for **30 days after** the leave ends
- Cannot dismiss during **maternity leave** and for **30 days after** the leave ends
- Exception: Employer pays compensation for business discontinuation (Art. 81) or business continuation is objectively impossible due to natural disaster

**Abuse of right doctrine** (Labor Contract Act Art. 16):
_"A dismissal that lacks objectively reasonable grounds and is not considered appropriate in light of social norms is invalid as an abuse of right."_

Courts assess validity using four factors:

1. **Business necessity** (整理解雇の必要性): Genuine, documented business reason for the dismissal
2. **Efforts to avoid dismissal** (解雇回避努力): Demonstrated good-faith efforts to find alternatives (retraining, reassignment, reduction of working hours, elimination of overtime, hiring freeze, directors' pay cut)
3. **Objective selection criteria** (被解雇者選定基準の合理性): Fair, documented criteria for selecting which employee(s) to dismiss in redundancy scenarios
4. **Prior consultation** (手続の相当性): Meaningful consultation with the union or employee representative before the decision is finalized

**Practical note**: Japanese courts set an exceptionally high bar for valid dismissal. Even well-documented redundancy dismissals are frequently found invalid if the employer cannot demonstrate all four factors. [VERIFY with current case law]

**Documents to review**:

- Notice of dismissal and any payments made
- Evidence of 30-day calculation
- Leave records (to verify no dismissal during protected period)
- Business necessity documentation (for redundancy dismissals)
- Consultation records

**Common compliance failures**:

- Dismissal during injury/illness or maternity leave
- Failure to provide 30-day notice or equivalent payment
- No documentation of the four abuse-of-right factors
- Fixed-term contract not renewed solely to avoid indefinite conversion — treated as de facto dismissal

---

### 4g. Fixed-Term Employment and 5-Year Conversion Rule

**Governing law**: Labor Contract Act Article 18; Ordinance implementing LCA [VERIFY currency]

**Core rule**: An employee on repeated fixed-term contracts who has accumulated **5 or more years of cumulative employment** with the same employer acquires the **right to request conversion to an indefinite-term contract** (無期転換申込権). Once the request is made, the employer **must accept** — refusal is not permitted. [VERIFY]

**Triggering the right**:

- The right accrues on the first day of the contract period that **crosses the 5-year cumulative threshold**
- Cumulative calculation includes all fixed-term periods that are **not separated by a cooling-off gap**
- Cooling-off gap rule: if the gap between contracts exceeds the longer of (a) 6 months or (b) 50% of the preceding contract length (for contracts under 1 year), the cumulative count resets to zero
- Special rule for academic institutions: 10-year threshold instead of 5 years [VERIFY]

**Employer obligations**:

- Must not terminate fixed-term employment solely to avoid the 5-year conversion obligation
- Advance waiver of conversion rights by the employee is not valid
- Must proactively inform fixed-term workers of their conversion right (MHLW guidance) [VERIFY]
- After conversion, the indefinite contract terms default to the terms of the preceding fixed-term contract unless otherwise agreed

**Documents to review**:

- Fixed-term employment contracts for all fixed-term employees
- Cumulative service records (start dates, contract renewal history, gap periods)
- Any conversion requests received and responses

**Common compliance failures**:

- No tracking system for cumulative service of fixed-term employees — employer unaware of who has crossed (or is approaching) the 5-year threshold
- Terminating fixed-term employees just before the 5-year mark (legally risky — courts may treat this as abuse of the employer's right not to renew)
- Advance waivers of conversion rights embedded in fixed-term contracts (void)
- Failing to provide proper working conditions upon conversion

**⟁ CLARIFY** — If the employer has fixed-term employees with 3+ years of service: "Can you confirm the start dates and contract renewal history for these employees? Several may be approaching or have passed the 5-year threshold."

---

### 4h. Work Style Reform — Overtime Caps and Equal Pay

**Governing law**: Act No. 71 of 2018 (Work Style Reform Act); LSA as amended [VERIFY currency]

**Overtime caps (see also 4b)**:

- Overtime caps are now **mandatory legal obligations** (not administrative guidance) with criminal sanctions for violations
- Implementation: April 1, 2019 (large companies); April 1, 2020 (SMEs); April 1, 2024 (construction, transport, healthcare)

**Equal pay for equal work (同一労働同一賃金)**:

- Employers must not treat non-regular workers (part-time, fixed-term, dispatched) differently from regular workers in wages, bonuses, allowances, and welfare benefits **unless the difference is based on objective differences in job content, responsibility, or transfer/assignment scope** [VERIFY]
- Employers must explain the basis for any wage differentials when requested by a non-regular worker
- Implementation: April 1, 2020 (large companies); April 1, 2021 (SMEs)

**Documents to review**:

- Comparison of wage components (base pay, allowances, bonuses) for regular vs. non-regular workers doing similar work
- Employer's written rationale for any differentials (if non-regular workers have requested explanations)

**Common compliance failures**:

- Non-regular workers excluded from commuting allowances, family allowances, or welfare benefits available to regular workers — hardest position to defend
- No documented analysis of whether wage differentials are justified
- Failure to provide explanations when requested

---

### 4i. Minimum Wage Compliance

**Governing law**: Minimum Wage Act; regional minimum wage orders issued annually [VERIFY currency]

**Structure**:

- Japan operates **47 prefectural (regional) minimum wages** (地域別最低賃金), updated each October
- Some industries have **industry-specific minimum wages** (特定最低賃金) that typically exceed the regional rate; the higher rate always governs
- As of October 2024: national average ¥1,055/hour; highest Tokyo ¥1,163/hour; lowest Akita ¥951/hour [VERIFY — rates change annually]
- Minimum wage applies to all employers regardless of size; no phase-in for SMEs

**Documents to review**:

- Payroll records for the lowest-paid employees
- Applicable regional minimum wage order for the relevant prefecture
- Any applicable industry-specific minimum wage order

**Common compliance failures**:

- Hourly rate below the applicable regional rate (especially after October annual increases)
- Wage components improperly included in minimum wage calculation (only specified allowances count — transport allowance, family allowance, overtime pay are excluded from the comparison)
- Employees in multi-prefecture operations subject to different rates — only the rate for the prefecture where work is performed applies

---

### 4j. Childcare and Family Care Leave

**Governing law**: Act on Childcare Leave and Family Care Leave (育児・介護休業法) as amended 2022 [VERIFY currency]

**Employee entitlements (childcare leave)**:

- Up to **1 year of childcare leave per child** (extendable to 1 year 6 months, and further to 2 years if childcare placement is unavailable)
- **Postnatal paternity leave** (産後パパ育休, "Childcare at Birth Leave"): Up to **4 weeks** within 8 weeks of birth, taken in up to 2 blocks — effective October 1, 2022 [VERIFY]
- Fixed-term employees are now immediately eligible for childcare leave regardless of service length (amended April 1, 2022) [VERIFY]

**Employer obligations**:

- May not dismiss or disadvantage employees for taking or requesting childcare/family care leave (maternity harassment — マタハラ — is prohibited)
- Must establish an environment that makes employees comfortable taking leave (mandatory effort obligation)
- Companies with 1,000+ employees must **publicly disclose male childcare leave uptake rates** [VERIFY]

**Family care leave**:

- Up to 93 days of family care leave per family member requiring long-term care, taken in up to 3 blocks

**Common compliance failures**:

- Work rules not updated to reflect 2022 amendments (postnatal paternity leave provisions)
- HR staff unaware of immediate eligibility for fixed-term employees
- Implicit discouragement of leave-taking constitutes maternity harassment
- No policy for the postnatal paternity leave system

---

### 4k. Workplace Harassment Prevention

**Governing law**: Act on Comprehensive Promotion of Labor Policies (as amended 2020); Equal Employment Opportunity Act; Childcare/Family Care Leave Act [VERIFY currency]

**Mandatory obligations** (for all employers from April 1, 2022):

1. Establish and disseminate a **clear anti-harassment policy** covering: (a) power harassment, (b) sexual harassment, and (c) maternity/paternity harassment
2. Provide **employee education and training**
3. Implement **confidential complaint investigation procedures**
4. Take **corrective and preventive measures** when harassment is identified
5. **Protect complainants from retaliation**

**Power harassment (パワーハラスメント)** — six types:

1. Physical aggression (assaults, throwing objects)
2. Psychological aggression (threats, defamation, abusive language)
3. Isolation (exclusion from information, social ostracism)
4. Excessive demands (impossible workloads, tasks outside job scope)
5. Underemployment (menial tasks far below an employee's capability)
6. Personal violations (excessive intrusion into private life)

**Note on enforcement**: The harassment prevention Act does not impose criminal penalties or direct administrative fines for violation. However, MHLW can issue public recommendations and name non-compliant employers. Violations enable civil litigation by affected workers and generate significant reputational risk. [VERIFY]

**Documents to review**:

- Written harassment prevention policy
- Training records
- Complaint investigation procedure documentation
- Records of complaints received and investigated

**Common compliance failures**:

- No written policy despite legal obligation
- Policy exists but training has not been conducted
- No independent complaint channel (employees cannot complain to HR if HR is implicated)
- No documentation of investigation outcomes and corrective actions

---

### 4l. Social Insurance Enrollment

**Governing law**: Health Insurance Act; Employees' Pension Insurance Act; Employment Insurance Act; Workers' Accident Compensation Insurance Act [VERIFY currency]

**Mandatory enrollment** for employees who meet ALL of:

- Work more than **20 hours per week** and
- Monthly wages at least **¥88,000** (~¥1.056M annually) and
- Expected employment duration exceeds **2 months**

**Registration obligations**:

- Employers must register new employees with health and pension insurance **within 5 days** of employment start [VERIFY]
- Workers' accident insurance enrollment is required from day 1 of employment, before any work begins [VERIFY]
- Failure to enroll eligible employees is a serious violation; retroactive penalties and back-premium obligations apply

**Common compliance failures**:

- Part-time employees meeting the 20-hour/¥88,000 threshold not enrolled — common in retail and hospitality
- Workers classified as independent contractors to avoid enrollment — misclassification liability
- Failure to enroll employees within the 5-day deadline
- "Day laborers" in construction or events not enrolled before work commences

---

### 4m. Wage Payment Rules

**Governing law**: LSA Articles 24, 25 [VERIFY currency]

**Five wage payment principles**:

1. **Currency** (通貨払い): Wages must be paid in legal currency (exceptions exist for bank transfer with employee consent, now standard practice)
2. **Direct payment** (直接払い): Must be paid directly to the employee
3. **Full payment** (全額払い): Must be paid in full — unauthorized deductions are prohibited; only deductions authorized by law (tax, social insurance) or written employee agreement are permissible
4. **Monthly payment** (毎月払い): Must be paid at least once per month
5. **Fixed payment date** (一定期日払い): Must be paid on a specified, regular date

**Emergency payment**: Employees may demand advance payment for wages already earned in case of emergency (childbirth, illness, disaster) [VERIFY]

**Common compliance failures**:

- Unauthorized deductions from wages (training costs, equipment damage, uniform costs) — illegal without a specific written agreement satisfying legal conditions
- Wages paid late or irregularly
- Deductions for absence at a daily rate that results in the remaining wage falling below the minimum wage

---

### 4n. Document Retention

**Governing law**: LSA Article 109; Enforcement Ordinance [VERIFY currency]

**Retention periods** (from the date of last entry):

- Wage ledgers, attendance records, agreements with worker representatives: **3 years** (extended from 2 years effective 2020) [VERIFY]
- Employment contracts: **3 years after termination**
- Annual paid leave ledgers: **3 years** [VERIFY]
- Work-related injury/illness records: up to **5 years** depending on the nature of the claim [VERIFY]

**Common compliance failures**:

- Records retained only 2 years (pre-2020 practice, no longer sufficient)
- Attendance records showing scheduled hours only, not actual hours worked
- Leave ledgers per employee not maintained at all

---

## Compliance Severity Classification

### COMPLIANT

The employer meets the applicable statutory requirement. Documentation is adequate.
No action required, but periodic review recommended.

### PARTIAL

The employer substantially meets the requirement but has material gaps: documentation
is incomplete, practices deviate in a non-critical way, a requirement applies due to
recent amendments and has not yet been implemented, or the employer cannot demonstrate
compliance because records are absent.

**Action**: Remediate identified gaps within a defined timeframe. Assign HIGH or MEDIUM
priority depending on whether the gap creates immediate enforcement exposure.

### NON-COMPLIANT

The employer has a clear, current violation of a statutory obligation. Criminal penalties,
administrative orders, or civil liability exposure is present.

**Action**: Immediate remediation required. Assign CRITICAL or HIGH priority.

---

## Remediation Action Format

For each PARTIAL or NON-COMPLIANT finding:

```
**Area**: [Compliance area, e.g., "4b. Article 36 Agreement"]
**Classification**: [PARTIAL / NON-COMPLIANT]
**Finding**: [Specific gap or violation]
**Legal basis**: [Governing statute and article — with [VERIFY] if unconfirmed]
**Risk**: [Specific enforcement risk: fine amount, criminal penalty, civil liability]
**Action required**: [Specific, actionable step]
**Owner**: [HR / Legal / Management]
**Deadline**: [Immediate / 30 days / 60 days / Next review cycle]
**Notes**: [Any preconditions, dependencies, or practical guidance]
```

---

## Prioritization Framework

### CRITICAL — Immediate Remediation (within 7 days)

Violations exposing the employer to criminal sanctions, administrative orders, or
imminent litigation:

- No 36 Agreement while overtime work is occurring (criminal liability under LSA)
- Dismissal during a protected period (injury/illness leave, maternity leave) — automatic invalidity + potential damages
- Wages below minimum wage
- Failing to pay wages at all or unauthorized deductions
- Enrolling no employees in workers' accident compensation insurance

### HIGH — Priority Remediation (within 30 days)

Significant legal risk with clear statutory basis:

- 36 Agreement lacks proper worker representative — agreement has no legal effect
- Overtime hours exceeding the caps in a filed 36 Agreement
- No work rules despite 10+ employees
- Fixed-term employees past the 5-year threshold without conversion offer
- No Annual Paid Leave Ledger; fewer than 5 days designated for eligible employees
- Failure to enroll eligible employees in health and pension insurance

### MEDIUM — Planned Remediation (within 90 days)

Material compliance gaps that create exposure but do not pose immediate criminal risk:

- Work rules not filed with LSIO or not updated after recent amendments
- Equal pay analysis not conducted or documented
- No harassment prevention policy or training
- Document retention periods not updated to 3 years
- Childcare leave work rules not updated for 2022 amendments

### LOW — Improvement (next review cycle)

Good-practice improvements or areas where the employer is substantially compliant
but could strengthen documentation:

- Annual review and renewal of the 36 Agreement
- Harassment training frequency (annual best practice)
- Proactive communication to fixed-term employees of conversion rights before 5-year threshold

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                         | Fail Action                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, article number, or established doctrine                          | Add citation or mark "[UNVERIFIED — counsel to confirm]"                          |
| **Format**     | All citations follow consistent Japanese law citation format (law name, Act number, article)                 | Fix format                                                                        |
| **Currency**   | Every cited provision checked for 2018-2024 amendments (Work Style Reform changes are extensive)             | Flag "[CHECK CURRENCY — may have been amended by Work Style Reform Act or later]" |
| **Domain**     | Analysis stays within Japanese labor law. No EU, US, or other system concepts imported                       | Remove or flag any non-Japanese legal concept presented as Japanese law           |
| **Confidence** | Uncertainty explicitly stated, not hidden. Flag any area where the correct application is genuinely disputed | Add confidence qualifier; flag for qualified Japan labor counsel                  |

### Self-Interrogation for NON-COMPLIANT Findings

For any finding classified NON-COMPLIANT, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**:

- Does the violation finding follow logically from the cited statute and the facts?
- Would the LSIO or a court reach the same conclusion on these facts?
- Is there a credible counter-argument (e.g., an industry exemption, a transition period) that has not been considered?

**Pass 2 — Completeness**:

- Have all relevant statutes and recent amendments been considered?
- Is the applicable enforcement penalty correctly stated?
- Are there any MHLW guidance documents that modify the strict statutory requirement?

**Pass 3 — Challenge**:

- What is the strongest argument that this finding is actually PARTIAL rather than NON-COMPLIANT?
- Does the severity of the finding change if the employer's description of facts is taken at face value?
- Is the CRITICAL priority warranted, or is HIGH more appropriate given the actual enforcement context?

If any pass reveals a weakness, revise the finding before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                            | Action                                                |
| ------------ | --------- | -------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory text, unambiguous application      | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions   | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; reasonable counsel could differ    | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on facts not provided | Flag for qualified Japan labor counsel review         |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every assessment output MUST include this block at the end:

```yaml
glass_box:
  skill_name: "legalcode-jp-labor-standards-compliance"
  employer_size: "[stated employee count]"
  industry: "[stated industry]"
  assessment_scope: "[areas assessed]"
  documents_reviewed: "[list or 'Verbal description only']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/jp-labor-compliance-authority.md or 'Not created']"
  statutes_consulted:
    - "Labor Standards Act (Act No. 49 of 1947) — [VERIFIED / UNVERIFIED]"
    - "Labor Contract Act (Act No. 128 of 2007) — [VERIFIED / UNVERIFIED]"
    - "Work Style Reform Act (Act No. 71 of 2018) — [VERIFIED / UNVERIFIED]"
    - "Act on Childcare Leave and Family Care Leave — [VERIFIED / UNVERIFIED]"
  compliance_areas_assessed: "[number out of 14]"
  findings:
    compliant: "[number]"
    partial: "[number]"
    non_compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — verbal description only, documents not provided, etc.]"
    - "[2024 industry-specific overtime cap changes may apply — verify for construction/transport/healthcare employers]"
  reviewer: "AI-assisted — requires qualified Japan labor attorney (弁護士) or labor/social insurance consultant (社会保険労務士) review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when assessing Japanese labor compliance:

1. **Assuming the 36 Agreement is automatically valid** — A signed 36 Agreement is not valid unless it has been filed with the LSIO and the worker representative was independently and democratically elected. Management-appointed representatives invalidate the agreement entirely.

2. **Confusing the standard and special overtime caps** — The 45-hour monthly and 360-hour annual limits are the standard. The 100-hour and 720-hour limits are the absolute ceiling for special circumstances — they are not the standard operating limit. Presenting the higher caps as the normal limit creates serious compliance exposure.

3. **Ignoring the 50% premium rate** — Since April 1, 2023, all employers (not just large companies) must pay a 50% premium for monthly overtime exceeding 60 hours. Missing this rate creates retroactive wage liability.

4. **Treating the 5-day leave designation as the employee's responsibility** — The obligation to ensure employees take at least 5 days of annual leave falls on the employer. If an employee refuses to take leave, the employer must designate days. Blaming the employee does not cure the violation.

5. **Relying on an unfiled 36 Agreement** — An agreement that is not filed with the LSIO has no legal effect, even if signed by both parties. The filing receipt is the proof of validity.

6. **Applying Western dismissal concepts** — Japanese dismissal law is not analogous to US at-will employment or even to UK unfair dismissal. The abuse of right doctrine sets a far higher bar for valid dismissal. Do not import common law "for cause" / "at-will" reasoning into a Japan analysis.

7. **Calculating cumulative service incorrectly for the 5-year rule** — The 5-year count does not reset just because there is any gap between contracts. The cooling-off period rules are specific: gaps must exceed 6 months (or 50% of the prior contract for contracts under 1 year) to reset the count.

8. **Missing the April 1, 2024 industry transition** — Construction, transportation, and healthcare employers were previously exempt from overtime caps. That exemption ended April 1, 2024. Treating these employers as exempt is a critical error in post-April 2024 assessments.

9. **Confusing minimum wage calculation components** — Not all wage components count toward minimum wage compliance. Overtime pay, family allowances, transport allowances, and certain other allowances are excluded from the comparison calculation. Only the "basic wage" and certain allowances are counted. Verify the MHLW exclusion list [VERIFY].

10. **Treating consultation as consent for work rule changes** — The employer must consult with the worker representative before establishing or amending work rules, but does not need their agreement. However, changes that unilaterally worsen employees' conditions are subject to the Labor Contract Act's prohibition on disadvantageous unilateral change (Art. 9-10). These are distinct legal questions.

11. **Assuming small employers are fully exempt** — Many obligations apply at 10 employees (work rules), others at any size (minimum wage, 36 Agreement if overtime occurs, workers' accident insurance, harassment policy from April 2022). "Small company" is not a blanket exemption.

12. **Confusing the Article 36 agreement annual renewal with the LSIO registration** — Even if an employer has a 36 Agreement on file, it typically needs to be renewed annually. An expired agreement is equivalent to no agreement — all overtime worked under it is unauthorized.

13. **Presenting fixed overtime allowances as a cure-all** — "Minashi zangyō" (fixed overtime) arrangements are valid only if structured correctly: the fixed hours and amount are clearly stated, actual hours are tracked, and top-up pay is made when actual overtime exceeds the fixed amount. Poorly structured fixed overtime arrangements are challenged regularly by the LSIO.

14. **Ignoring the harassment law for employers with under 50 employees** — The power harassment prevention Act applied to large employers from June 2020 but extended to all employers (including those with 1 employee) from April 1, 2022. It is no longer a large-company obligation.

15. **Failing to distinguish between the 4-factor test for redundancy dismissals and the standard for individual dismissals** — The 4-factor test (business necessity, avoidance efforts, selection criteria, consultation) applies primarily to redundancy/restructuring dismissals (整理解雇). Individual dismissals for performance, conduct, or incapacity have their own abuse-of-right analysis. Applying the redundancy test to an individual performance dismissal (or vice versa) produces incorrect conclusions.

16. **Overlooking the cooling-off trap** — Employers sometimes believe that deliberately leaving a short gap between fixed-term contracts resets the 5-year clock. Courts have scrutinized this. If the gap is manufactured specifically to avoid indefinite conversion obligations, it may be treated as abuse of right and the cumulative count preserved.

---

## Writing Standards

Apply plain-language discipline to all assessment output:

**For remediation actions** (likely shared with HR and management):

- Active voice: "The employer must file a 36 Agreement with the LSIO" not "A 36 Agreement filing is required"
- Name the specific obligation: cite the article number, not just "statutory requirement"
- One action per bullet; avoid combining multiple steps
- Avoid Japanese legal jargon without translation; provide both the Japanese term and English gloss on first use

**For finding rationales**:

- State the requirement, then the gap, then the risk — in that order
- Quantify penalties where known (e.g., "up to ¥300,000 fine per employee")
- Flag uncertainty explicitly — do not present a probable violation as a definite one
- Reference the relevant compliance area number (4a–4n) for cross-referencing

**Quality gates before delivery**:

1. Can an HR manager without a law degree understand every finding and action?
2. Is every NON-COMPLIANT finding backed by a specific statutory citation (or flagged [VERIFY])?
3. Has the Self-Interrogation been run for every NON-COMPLIANT finding?
4. Are all priorities (CRITICAL/HIGH/MEDIUM/LOW) justified with reference to the enforcement risk?
5. Does the Glass Box Audit Trail accurately reflect what documents were reviewed and what was not reviewed?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred)**:

- In Step 3, search for current text of LSA, LCA, and recent MHLW enforcement guidance
- Verify statutory citations against current e-Gov text
- Check for 2023–2024 amendments not yet reflected in widely available English translations
- Search for recent Labor Tribunal decisions on dismissal, 5-year conversion disputes, and 36 Agreement violations
- Save results to `/tmp/jp-labor-compliance-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp**:

- Mark all statutory citations [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Use japaneselawtranslation.go.jp as the reference for LSA and LCA text [VERIFY for currency against latest amendments]
- Refer to MHLW's official English-language publications for Work Style Reform and leave law guidance
- Focus the assessment on structural and process compliance rather than fine-grained statutory interpretation

**Recommended external resources** (for follow-up verification):

- Japanese Law Translation database: japaneselawtranslation.go.jp
- MHLW English labor law resources: mhlw.go.jp/english/policy/employ-labour/labour-standards/
- JETRO employment law guide: jetro.go.jp/en/invest/setting_up/section4/
- LSIO office locator: mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/location.html

---

## Output Format Template

Structure every assessment deliverable as:

```markdown
## Japan Labor Standards Compliance Assessment

**Employer**: [name or description]
**Industry**: [stated industry]
**Employee count**: [approximate]
**Assessment date**: [date]
**Scope**: [areas covered]
**Document basis**: [documents reviewed or "Verbal description only"]

---

## Executive Summary

**Overall posture**: [COMPLIANT / SUBSTANTIALLY COMPLIANT / MATERIAL GAPS / SIGNIFICANT VIOLATIONS]
**CRITICAL findings**: [count]
**HIGH priority findings**: [count]
**MEDIUM priority findings**: [count]
**Immediate actions required**: [yes/no; summary of most urgent steps]

---

## Findings by Area

### [4a. Working Hours and Rest Periods] — [COMPLIANT / PARTIAL / NON-COMPLIANT] | Priority: [level] | Confidence: [level]

**Requirement**: [brief statement of the obligation and governing provision]
**Current practice**: [what the employer actually does or documents show]
**Gap**: [specific gap if PARTIAL or NON-COMPLIANT]
**Risk**: [enforcement risk — fine, criminal liability, civil claim]
**Action**: [specific remediation step]
**Owner**: [HR / Legal / Management]
**Deadline**: [timeframe]

[Repeat for each area assessed]

---

## Priority Action Plan

### CRITICAL — Immediate (within 7 days)

- [ ] [Action] | Owner: [X] | Legal basis: [Y]

### HIGH — Priority (within 30 days)

- [ ] [Action] | Owner: [X] | Legal basis: [Y]

### MEDIUM — Planned (within 90 days)

- [ ] [Action] | Owner: [X] | Legal basis: [Y]

### LOW — Next review cycle

- [ ] [Action] | Owner: [X] | Legal basis: [Y]

---

## Next Steps

[Specific follow-up: documentation to gather, counsel to engage, LSIO filing deadlines]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill covers **Japan national law only**. Within Japan, note:

- **Minimum wage**: Rates differ by prefecture and by industry. Always verify the applicable rate for the specific prefecture where work is performed and whether an industry-specific minimum wage applies (the higher rate governs).
- **LSIO jurisdiction**: 36 Agreements and work rules must be filed with the LSIO that has jurisdiction over the specific workplace location — not a central national office. Multi-location employers must file separately per location.
- **Language**: All work rules, 36 Agreements, and LSIO filings are in Japanese. Japanese-language versions govern. English translations are for reference only and have no legal effect.
- **Foreign national employees**: Japanese labor law applies to all employees working in Japan regardless of nationality or the nationality of their employer. Employment contracts choosing foreign law as governing law do not override mandatory provisions of Japanese labor law. [VERIFY for specific provisions]
- **Dispatched workers**: Workers dispatched by staffing agencies (派遣労働者) are subject to additional rules under the Worker Dispatch Act (労働者派遣法). This skill does not cover dispatch-specific compliance in detail — flag for separate assessment if dispatch workers are used.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Ministry of Health, Labour and Welfare (MHLW) official English-language publications on Work Style Reform, overtime caps, annual paid leave, and childcare leave
- Japanese Law Translation database (japaneselawtranslation.go.jp) — Labor Standards Act, Labor Contract Act
- JETRO investment guidance on Japanese employment law
- Chambers & Partners Employment 2025 Japan trending developments
- Published research on Work Style Reform Act implementation and 2024 industry-specific transitions
- Authoritative commentary from Japanese law firms (Anderson Mori & Tomotsune, Ogletree, Littler)

All statutory citations require verification against current e-Gov text before reliance. Japan's labor law is actively amended — verify currency of every provision before use.
