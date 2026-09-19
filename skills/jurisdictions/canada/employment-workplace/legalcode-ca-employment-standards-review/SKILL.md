---
name: legalcode-ca-employment-standards-review
description: Reviews employment standards compliance across all Canadian jurisdictions — federal Canada
  Labour Code (Part III) and all 13 provincial/territorial Employment Standards Acts. Covers minimum wage,
  hours of work, overtime, vacation entitlements, statutory holidays, termination notice, severance pay,
  leaves of absence (maternity, parental, sick, family violence, compassionate care, bereavement), and
  equal pay obligations. Produces a jurisdiction-mapped compliance gap report with COMPLIANT/PARTIAL/NON-COMPLIANT
  classifications, remediation actions, and prioritized risk register. Use when auditing employment practices
  for a Canadian workforce, onboarding a new employer entity in Canada, reviewing employment contracts
  or HR policies for Canadian legal minimums, or advising on multi-provincial employment operations. Covers
  federally regulated employers (banks, telecoms, rail, air, federal Crown) and all provincial/territorial
  workforces. Jurisdiction-specific with province-by-province mapping.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — Canadian Employment Standards Review

> **Disclaimer**: This skill provides a framework for AI-assisted employment standards
> compliance review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified Canadian employment lawyer licensed in the relevant jurisdiction before
> reliance or action. Employment standards legislation changes frequently — minimum wage
> rates, leave entitlements, and notice periods are updated regularly. Verify all rates and
> thresholds against current official government sources before acting. Statutory and
> regulatory references carry hallucination risk — verify against authoritative sources
> (Canada.ca, provincial government portals, CanLII) before relying on them.

---

## Purpose and Scope

This skill reviews an employer's employment practices, HR policies, employment contracts,
and workforce structure against the mandatory minimums set by Canadian employment standards
legislation across all jurisdictions.

**Covers:**

- Federal: Canada Labour Code, Part III (CLC), Canada Labour Standards Regulations (CLSR)
- Ontario: Employment Standards Act, 2000 (ESA 2000, SO 2000, c 41)
- British Columbia: Employment Standards Act (BC ESA)
- Alberta: Employment Standards Code (ESC, RSA 2000, c E-9)
- Quebec: Act respecting labour standards (Loi sur les normes du travail, CQLR c N-1.1)
- Saskatchewan: The Saskatchewan Employment Act (SS 2013, c S-15.1)
- Manitoba: Employment Standards Code (CCSM c E110)
- Nova Scotia: Labour Standards Code (SNS 1972, c 10)
- New Brunswick: Employment Standards Act (SNB 1982, c E-7.2)
- Prince Edward Island: Employment Standards Act (RSPEI 1988, c E-6.2)
- Newfoundland & Labrador: Labour Standards Act (RSNL 1990, c L-2)
- Northwest Territories: Employment Standards Act (SNWT 2007, c 13)
- Nunavut: Labour Standards Act (RSNWT (Nu) 1988, c L-1)
- Yukon: Employment Standards Act (RSY 2002, c 72)

**Review dimensions (12 standard areas):**

1. Minimum wage compliance
2. Hours of work and maximum hours
3. Overtime eligibility and calculation
4. Vacation entitlement and vacation pay
5. Statutory/general holidays
6. Termination notice requirements
7. Severance pay (where applicable)
8. Leaves of absence (maternity, parental, sick, family violence, compassionate care, bereavement, critical illness)
9. Equal pay and pay equity obligations
10. Employment records and pay statement requirements
11. Employment information obligations (written statements)
12. Group termination/mass layoff obligations

**Does not:**

- Provide legal advice or replace qualified Canadian employment counsel
- Cover human rights, occupational health and safety, or labour relations (unionized workplaces)
- Cover pension or benefits legislation beyond statutory minimums
- Draft employment contracts (see legalcode-employment-agreement-review for drafting analysis)
- Substitute for payroll audits or actuarial analysis

---

## Jurisdiction and Governing Law

Canada has a split jurisdictional system. Employment standards are governed by one of
14 regimes depending on the employer's industry:

**Federally regulated employers** (Canada Labour Code, Part III) include:

- Banks and federal financial institutions (all Schedule I and II banks)
- Telecommunications carriers (radio, TV, internet, satellite, broadcasting)
- Interprovincial and international transportation (rail, air, marine, road freight)
- Postal and courier services (Canada Post, federal carriers)
- Grain elevators, feed mills, seed cleaning plants, feed warehouses
- Uranium mining and processing; atomic energy (AECL, Ontario Power)
- Federal Crown corporations and departmental corporations
- Any work, business, or undertaking "vital, essential, or integral" to the above

**All other employers** are governed by the province or territory in which the employee
performs work — NOT the province of the employer's head office.

**Key principle — provincial minimum applies if higher:** Where a provincial minimum wage
or standard exceeds the federal minimum, the provincial rate governs even for federally
regulated employers whose operations fall within that province.

**Multi-provincial workforces:** An employer with employees in multiple provinces must
comply with each province's ESA for employees working in that province. A single set of
HR policies is typically insufficient.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The applicable jurisdiction is unclear or the employer operates in multiple provinces
- The employment classification (federal vs. provincial) is not obvious
- Policies or contracts are provided but are incomplete or ambiguous
- A compliance gap's severity depends on facts the user must provide

Use the **⟁ CLARIFY** pattern (structured options with context) wherever marked below.
If the user has already provided the information, skip the question and proceed. State any
assumptions you make explicitly so the user can correct them.

---

## Workflow

### Step 1: Accept the Input

Accept input in any of these formats:

- **Employment policies / HR handbook**: A PDF, DOCX, or pasted text of existing policies
- **Employment contract(s)**: Individual or template contracts for review
- **Payroll/compensation summary**: Rates, hours, and deductions for a workforce
- **Description of practices**: Free-text description of what the employer currently does
- **Specific question**: "Does our [province] overtime policy comply with ESA minimums?"

If no input is provided, prompt the user to supply materials and confirm which jurisdiction(s)
to analyze.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask:

1. **Jurisdiction(s) in scope:**
   - Options: Federal (CLC), Ontario, British Columbia, Alberta, Quebec, Saskatchewan,
     Manitoba, Nova Scotia, New Brunswick, PEI, Newfoundland, NWT, Nunavut, Yukon,
     Multiple (list them), All Canadian
   - _Why this matters_: Each jurisdiction has different minimums. The review must be
     scoped correctly — a policy valid in Alberta may be non-compliant in Ontario.

2. **Employer's industry/sector (for federal vs. provincial determination):**
   - Options: Banking, Telecommunications, Interprovincial transportation, Crown corporation,
     Other federally regulated, Retail, Hospitality, Technology, Healthcare, Construction,
     Professional services, Other provincial (specify)
   - _Why this matters_: Determines which legislative regime applies. A road freight company
     crossing provincial borders is federally regulated; a local trucking company is not.

3. **Workforce composition:**
   - Options: All full-time employees, Mix of full-time/part-time/casual, Includes
     contractors (risk of misclassification), Multi-provincial workforce, Unionized
     employees (collective agreement governs — ESA minimums still apply)
   - _Why this matters_: Part-time, casual, and contractor classifications affect which
     standards apply and whether misclassification liability exists.

4. **Review objective:**
   - Options: Full compliance audit (all 12 areas), Specific area only (specify which),
     New entity setup/onboarding, Pre-acquisition due diligence, Specific complaint/incident,
     Policy refresh/update
   - _Why this matters_: Determines the depth and breadth of analysis needed.

5. **Documents provided:**
   - Confirm which documents are available: employment contract templates, HR handbook,
     payroll records, pay stubs, existing policies (overtime, vacation, leaves)
   - _Why this matters_: A policy review without payroll data cannot verify actual compliance
     — flag this limitation if payroll data is absent.

If the user provides partial context, proceed with stated assumptions and flag any
limitations on the analysis at the start of the output.

### Step 3: Determine Jurisdictional Scope

Based on Step 2 inputs, confirm:

1. **Primary legislative regime:** Federal (CLC) or provincial/territorial (specify which)
2. **Multi-provincial map:** If operations span multiple provinces, list each province
   and the number of employees subject to each ESA
3. **Collective agreement overlay:** If any employees are unionized, note that the
   collective agreement governs wages/hours above ESA minimums, but ESA minimums remain
   the floor that collective agreements cannot contract below

**⟁ CLARIFY** — If the jurisdictional determination is unclear:

- "Your company operates trucks that cross provincial borders. If these are interprovincial
  routes, your drivers are federally regulated under the CLC, not the provincial ESAs.
  Can you confirm whether these routes cross provincial boundaries?"
- "Your employee's contract says 'governed by Ontario law' but they work from home in BC.
  The ESA of the province where the employee works applies — BC Employment Standards Act
  governs. Please confirm the province of work for each employee category."

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve current:

- Minimum wage rates for each in-scope jurisdiction
- Key statutory sections for any areas under review
- Recent amendments and coming-into-force dates
- Regulatory guidance from ESDC (federal) or provincial labour authorities

Save findings to `/tmp/legalcode-ca-esa-authority.md`.

If legalcode-mcp is not connected, proceed using the reference frameworks in this skill
(current as of 2026-03-21). Mark all rates and thresholds with [VERIFY CURRENT RATE]
where figures may have changed.

### Step 5: Run the 12-Area Compliance Review

Analyze each of the 12 standard areas below. For each area, assess the employer's
current practice against the applicable statutory minimum, classify the gap, and generate
an actionable finding.

**⟁ CLARIFY** — For a full 12-area review, confirm: "This will be a comprehensive review
covering all 12 employment standards areas. This is the most thorough approach. Alternatively,
I can focus on a specific subset — for example, hours/overtime and leaves are the highest
risk areas for most employers. Which approach do you prefer?"

See the **Deep Analysis Framework** section for detailed analysis guidance per area.

### Step 6: Classify Each Finding

Apply the three-tier classification system (COMPLIANT / PARTIAL / NON-COMPLIANT) defined
in the **Compliance Classification** section to each finding. For NON-COMPLIANT items,
apply Self-Interrogation (3-pass review) before finalizing.

**⟁ CLARIFY** — For borderline classifications, ask rather than assume:

- "Your overtime policy exempts all 'managers' from overtime pay. Under the CLC, the
  manager exemption is narrow — it requires significant autonomous decision-making authority,
  not just a managerial title. Can you describe the actual duties of these roles? This
  determines whether the exemption is valid or a NON-COMPLIANT misclassification."

### Step 7: Generate Remediation Actions

For each PARTIAL or NON-COMPLIANT finding, generate a specific remediation action with:

- The exact change required to achieve compliance
- Suggested policy or contract language (where appropriate)
- Retroactive liability exposure estimate (where calculable)
- Timeline recommendation (immediate / 30 days / 90 days)

### Step 8: Build the Prioritized Risk Register

Rank all findings by the **Prioritization Framework** (Critical / High / Medium / Low) and
produce the final output using the **Output Format Template**.

### Step 9: Quality Verification

Before delivering:

1. Run the 5 Citation Quality Gates silently
2. Apply Self-Interrogation to all NON-COMPLIANT items
3. Verify all minimum wage rates and notice periods are current
4. Confirm no jurisdiction-specific concept bleeds into another jurisdiction's analysis

---

## Deep Analysis Framework — 12 Standard Areas

### Area 1: Minimum Wage

**What to review:** Compare the employer's lowest wage rates against the applicable
statutory minimum wage for each in-scope jurisdiction.

**Current minimum wage rates (as of 2026-03-21) [VERIFY CURRENT RATES]:**

| Jurisdiction                | Minimum Wage                                       | Effective Date       | Indexation                      |
| --------------------------- | -------------------------------------------------- | -------------------- | ------------------------------- |
| **Federal (CLC)**           | $17.75/hr (April 1 2025); $18.10/hr (April 1 2026) | Annually April 1     | CPI-linked                      |
| **Ontario**                 | $17.60/hr                                          | October 1, 2025      | Annual CPI                      |
| **British Columbia**        | $17.85/hr                                          | June 1, 2025         | Annual CPI                      |
| **Alberta**                 | $15.00/hr                                          | Unchanged since 2018 | None (legislative)              |
| **Quebec**                  | $16.10/hr                                          | May 1, 2025          | Annual CPI                      |
| **Saskatchewan**            | $15.35/hr                                          | October 1, 2025      | Annual CPI (Oct 1)              |
| **Manitoba**                | $16.00/hr                                          | October 1, 2025      | Annual CPI                      |
| **Nova Scotia**             | $16.50/hr                                          | October 1, 2025      | CPI + 1%                        |
| **New Brunswick**           | $15.65/hr                                          | April 1, 2025        | Annual CPI                      |
| **PEI**                     | $17.00/hr                                          | April 1, 2025        | Annual                          |
| **Newfoundland & Labrador** | $16.00/hr                                          | April 1, 2025        | Annual CPI                      |
| **Northwest Territories**   | $16.95/hr                                          | September 1, 2025    | CPI (Yellowknife) + wage growth |
| **Nunavut**                 | $19.75/hr                                          | September 1, 2025    | CPI (Iqaluit) + wage growth     |
| **Yukon**                   | $17.94/hr                                          | April 1, 2025        | Annual CPI                      |

**Alberta sub-minimums [VERIFY]:**

- Students under 18: $13.00/hr (first 28 hours/week when school is in session)
- Domestic employees: $2,848/month minimum
- Commission salespersons: $598/week minimum

**Key analytical steps:**

- Identify the lowest hourly wage paid by the employer per province
- Compare against the applicable statutory minimum (and sub-minimums where relevant)
- Check whether wage rates are reviewed and updated each time statutory minimums change
- Note: Employers paying at or close to minimum wage carry ongoing non-compliance risk
  as rates change annually — a policy of "staying current" should be documented

**Red flags:** Tip credits (generally prohibited in Canada except limited Quebec/NS rules);
deductions that reduce effective pay below minimum wage; salaries for irregular hours that
yield sub-minimum effective rates; Alberta "management" exemptions applied too broadly.

---

### Area 2: Hours of Work and Maximum Hours

**Standard hours and maximum hours per jurisdiction:**

| Jurisdiction      | Standard Hours             | Maximum Hours    | Daily Max       | Notes                           |
| ----------------- | -------------------------- | ---------------- | --------------- | ------------------------------- |
| **Federal (CLC)** | 40 hrs/week                | 48 hrs/week      | —               | Averaged over scheduling period |
| **Ontario**       | 8 hrs/day or employer norm | No statutory cap | 8 hrs + OT      | With agreement, can exceed      |
| **BC**            | 8 hrs/day; 40 hrs/week     | No hard cap      | 8 hrs/day       | Daily AND weekly thresholds     |
| **Alberta**       | 8 hrs/day; 44 hrs/week     | No hard cap      | 8 hrs + OT      | Daily threshold unique          |
| **Quebec**        | 40 hrs/week                | —                | No daily max    | Less prescriptive               |
| **Saskatchewan**  | 40 hrs/week                | —                | —               |                                 |
| **Manitoba**      | 40 hrs/week                | —                | —               |                                 |
| **Nova Scotia**   | 48 hrs/week                | —                | —               | Highest threshold in Canada     |
| **New Brunswick** | 40 hrs/week                | —                | —               |                                 |
| **PEI**           | 48 hrs/week                | —                | —               |                                 |
| **Newfoundland**  | 40 hrs/week                | —                | —               |                                 |
| **NWT/Nunavut**   | 40 hrs/week                | 10 hrs/day       | 60 hrs/week cap | Ministerial approval for more   |
| **Yukon**         | 40 hrs/week                | —                | —               |                                 |

**What to review:**

- Do employment contracts accurately state standard hours?
- Are "flexible" schedules structured to avoid maximum hours violations?
- Federal employers: Are averaging agreements properly established (30-day notice,
  posted in workplace, copied to unions, comply with 40/48 week limits within averaging period)?
- Are hours recorded daily (required under CLC s.169; CLSR ss.9-11)?

**⟁ CLARIFY** — If the employer uses shift scheduling, variable hours, or on-call
arrangements: "Averaging agreements under the CLC allow flexible scheduling, but require
30 days' prior written notice and cannot exceed 48 hours/week on average. Does your company
use any formal averaging or modified work arrangements? If so, please share the documentation
so I can assess its compliance."

---

### Area 3: Overtime Eligibility and Calculation

**Overtime thresholds and rates:**

| Jurisdiction      | Weekly OT Threshold | Daily OT  | OT Rate                               | Time Off in Lieu                   |
| ----------------- | ------------------- | --------- | ------------------------------------- | ---------------------------------- |
| **Federal (CLC)** | 40 hrs/week         | —         | 1.5×                                  | By written agreement               |
| **Ontario**       | 44 hrs/week         | —         | 1.5×                                  | By written agreement (1.5:1)       |
| **BC**            | 40 hrs/week         | 8 hrs/day | 1.5× (8-12 hrs/day); 2× (12+ hrs/day) | By written agreement               |
| **Alberta**       | 44 hrs/week         | 8 hrs/day | 1.5×                                  | Banked OT (1:1 ratio by agreement) |
| **Quebec**        | 40 hrs/week         | —         | Regular wage (check agreement/policy) | —                                  |
| **Saskatchewan**  | 40 hrs/week         | —         | 1.5×                                  | By agreement                       |
| **Manitoba**      | 40 hrs/week         | —         | 1.5×                                  | By agreement (1.5:1)               |
| **Nova Scotia**   | 48 hrs/week         | —         | 1.5×                                  | —                                  |
| **New Brunswick** | 44 hrs/week         | —         | 1.5×                                  | —                                  |
| **PEI**           | 48 hrs/week         | —         | 1.5×                                  | —                                  |
| **Newfoundland**  | 40 hrs/week         | —         | 1.5×                                  | —                                  |
| **NWT/Nunavut**   | 40 hrs/week         | —         | 1.5×                                  | —                                  |
| **Yukon**         | 40 hrs/week         | —         | 1.5×                                  | —                                  |

**Key analytical steps:**

- Identify which employees are classified as overtime-exempt (managers, professionals)
  and assess whether the exemption is legally defensible
- **Federal CLC manager exemption**: Narrow — requires genuine management function with
  significant autonomous decision-making authority; title alone is insufficient; apply
  the Management Function Questionnaire standard
- **Ontario ESA**: Managers/supervisors whose work is not "routinely performed" may be
  exempt; IT professionals who primarily troubleshoot may qualify for ESA exemption
- **BC ESA**: Managers, supervisors, and professionals (lawyers, doctors, engineers,
  architects) are exempt; but must actually exercise managerial discretion
- Assess whether overtime buy-outs (flat daily rate, salary absorption) are structured
  to comply or constitute underpayment
- Review whether time-off-in-lieu agreements are properly documented in writing

**Red flags:** Blanket "salaried exempt" policy applied without analysis; using
"averaging" informally without a proper written agreement; misclassifying workers as
independent contractors to avoid overtime obligations.

---

### Area 4: Vacation Entitlement and Vacation Pay

**Vacation entitlements by jurisdiction:**

| Jurisdiction      | Year 1–4         | Year 5–9                   | Year 10+          | Vacation Pay % | Notes          |
| ----------------- | ---------------- | -------------------------- | ----------------- | -------------- | -------------- |
| **Federal (CLC)** | 2 weeks          | 3 weeks                    | 4 weeks           | 4% / 6% / 8%   | CLC ss.206-218 |
| **Ontario**       | 2 weeks          | 3 weeks (5+ yrs)           | —                 | 4% / 6%        | ESA 2000       |
| **BC**            | 2 weeks          | 3 weeks (5+ yrs)           | —                 | 4% / 6%        | BC ESA         |
| **Alberta**       | 2 weeks          | 3 weeks (5+ yrs)           | —                 | 4% / 6%        | ESC            |
| **Quebec**        | 2 weeks (1+ yr)  | 3 weeks (3+ yrs)           | —                 | 4% / 6%        | LSST           |
| **Saskatchewan**  | 3 weeks          | 3 weeks                    | 4 weeks (10+ yrs) | 6% / 8%        | Consecutive    |
| **Manitoba**      | 2 weeks          | 3 weeks (5+ yrs)           | —                 | 4% / 6%        | CCSM c E110    |
| **Nova Scotia**   | 2 weeks          | 2 weeks (8+ yrs extra day) | —                 | 4% / 6%        | SNS 1972       |
| **New Brunswick** | 2 weeks          | 2 weeks (8+ yrs gets 6%)   | —                 | 4% / 6%        | SNB 1982       |
| **PEI**           | 3 weeks (always) | 3 weeks                    | —                 | 6% (always)    | RSPEI 1988     |
| **Newfoundland**  | 2 weeks          | 2 weeks                    | 3 weeks (15+ yrs) | Varies         | RSNL 1990      |
| **NWT/Nunavut**   | 2 weeks          | 3 weeks (5+ yrs)           | —                 | 4% / 6%        |                |
| **Yukon**         | 2 weeks          | 2 weeks (no increase)      | —                 | 4% (always)    | RSY 2002       |

**Quebec note:** Vacation entitlement steps up at 3 years (not 5 years as in most provinces).
**Saskatchewan note:** Minimum vacation is 3 consecutive weeks (unusual requirement for
vacation to be taken consecutively); 4 weeks after 10 years.
**PEI note:** Always 3 weeks and 6% regardless of tenure — most generous base vacation.
**Newfoundland note:** Prohibits "use-it-or-lose-it" policies — employees must take earned
vacation; forfeiture clauses are void.

**What to review:**

- Are vacation entitlements in employment contracts at or above the statutory minimums?
- Is vacation pay calculated correctly (as a % of gross wages, not just base salary)?
  Gross wages typically includes commissions, bonuses, overtime pay, and other remuneration —
  not just base hourly/salary amounts. [VERIFY per jurisdiction]
- Federal (CLC): Minimum 2 weeks' advance notice required before scheduling vacation
- Are vacation accruals tracked and paid out upon termination?
- Are "use-it-or-lose-it" policies used? Note NL prohibition; other provinces may have
  similar protections under general ESA principles

---

### Area 5: Statutory / General Holidays

**Holiday entitlements by jurisdiction:**

| Jurisdiction      | No. of Holidays  | Pay Formula                                                         | Working on Holiday                       |
| ----------------- | ---------------- | ------------------------------------------------------------------- | ---------------------------------------- |
| **Federal (CLC)** | 10               | 1/20th wages in prior 4-week period                                 | 1.5× + holiday pay                       |
| **Ontario**       | 9                | Regular wages ÷ days worked (3-week look-back / 5-week alternative) | 1.5× for hours OR regular pay + lieu day |
| **BC**            | 11               | Varies by eligibility; 1/20th average formula                       | 1.5× (hrs 0-12) + 2× (hrs 12+)           |
| **Alberta**       | 9                | Total wages in 4-week period ÷ days worked                          | 1.5× + day's pay OR lieu day             |
| **Quebec**        | Varies by sector | Collective agreement / employer policy                              | Subject to agreement                     |
| **Saskatchewan**  | 10               | 5% of regular wages in prior 28 days                                | 5% holiday pay + 1.5× wages              |
| **Manitoba**      | 9                | Regular day's pay (or 5% of 4-week wages for irregular hours)       | Regular day's pay + 1.5× for hours       |
| **Nova Scotia**   | 6                | Regular day's wages                                                 | 1.5× for hours + regular day's pay       |
| **New Brunswick** | 8                | Regular day's pay                                                   | Regular day's pay + 1.5×                 |
| **PEI**           | 8                | Regular day's pay                                                   | 1.5× for hours                           |
| **Newfoundland**  | 6                | Average day's pay (3-week average)                                  | 2× OR lieu day + day's pay               |
| **NWT/Nunavut**   | Varies           | Varies                                                              | Premium pay                              |
| **Yukon**         | 11               | Regular rate for normal hours                                       | Regular pay + 1.5× OT OR lieu day        |

**Eligibility conditions to check:**

- **Federal**: Employee scheduled to work AND reports to work on the holiday
- **BC**: Worked 30+ calendar days AND earned wages for 15+ days in prior 30 days
- **Alberta**: Worked 30+ workdays in prior 12 months for that employer
- **New Brunswick**: 90+ calendar days of employment + worked scheduled shift before
  and after the holiday

**What to review:**

- Does the employer recognize all required holidays for each province?
- Is holiday pay calculated using the correct formula? (Province-specific — often a % of
  wages in prior weeks, not a flat "one day's pay")
- Are employees who work on holidays compensated at the correct premium rate?
- Does the employer use substitution for holidays? Verify substitution is permitted and
  the substitute day is properly designated
- BC-specific: Daily overtime rates apply even on holidays for hours over 12

---

### Area 6: Termination Notice Requirements

**Individual termination notice by jurisdiction:**

| Jurisdiction                         | 3 mos–1 yr                  | 1–2 yrs         | 2–3 yrs          | 3+ yrs          | Max    |
| ------------------------------------ | --------------------------- | --------------- | ---------------- | --------------- | ------ |
| **Federal (CLC)** (as of Feb 1 2024) | 2 wks                       | 2 wks           | 3 wks            | +1 wk/yr        | 8 wks  |
| **Ontario ESA**                      | 1 wk                        | 1 wk/yr         | 1 wk/yr          | 1 wk/yr         | 8 wks  |
| **BC ESA**                           | 1 wk (3 mos) / 2 wks (1 yr) | 2 wks           | 3 wks (3 yrs)    | +1 wk/yr        | 8 wks  |
| **Alberta ESC**                      | 2 wks (90 days–2 yrs)       | 2 wks           | 4 wks            | +1 wk/yr        | 8 wks  |
| **Quebec LSST**                      | 1 wk (3 mos–1 yr)           | 2 wks           | 3 wks            | +1 wk/yr        | 8 wks  |
| **Saskatchewan SEA**                 | 1 wk (13 wks–1 yr)          | 2 wks (1–5 yrs) | 2 wks            | 4 wks (5+ yrs)  | 4 wks  |
| **Manitoba ESC**                     | 2 wks (3 mos–2 yrs)         | 2 wks           | 4 wks (2+ yrs)   | varies          | 4+ wks |
| **Nova Scotia**                      | 1 wk (3 mos–2 yrs)          | 2 wks (2–5 yrs) | 4 wks (5–10 yrs) | 8 wks (10+ yrs) | 8 wks  |
| **New Brunswick**                    | 2 wks (6 mos+)              | 2 wks           | 4 wks (5+ yrs)   | varies          | varies |
| **PEI**                              | 2 wks (6 mos+)              | 2 wks           | 4 wks            | —               | —      |
| **Newfoundland**                     | 1 wk (3 mos+)               | varies          | varies           | varies          | —      |

**Critical CLC update (February 1, 2024 — Bill C-86):**
The federal graduated termination notice schedule was significantly increased. For employees
with 5+ years of CLC service, notice requirements now step up 1 week per year of employment
to a maximum of 8 weeks. This is a common compliance gap for federally regulated employers
who did not update their termination processes.

**What to review:**

- Do termination letters and practices provide ESA minimum notice (or pay in lieu)?
- Is notice correctly calculated for the province of employment (not the province of
  head office)?
- Are pay-in-lieu calculations based on the employee's regular wages? (Cannot use average
  of irregular weeks if the employee had a regular rate)
- Do termination packages give the employee all accrued vacation, outstanding wages,
  and a written statement of entitlements (required under CLC since July 9, 2023)?
- Does the employer have a "just cause" termination practice? (ESA notice not required
  for just cause, but the bar for "just cause" that avoids all entitlements is high)

**Note:** ESA minimums are floors only. Common law/civil law notice obligations are
typically significantly longer (1–24 months depending on age, seniority, position, and
availability of comparable employment). ESA non-compliance is the regulatory exposure;
common law compliance is the litigation exposure.

---

### Area 7: Severance Pay

Severance pay is distinct from termination notice and only applies in specific circumstances:

**Federal (CLC) — Section 235:**

- Eligibility: 12+ consecutive months of continuous employment, terminated without just cause
- Calculation: Greater of (2 days' regular wages × completed years of service) OR 5 days'
  regular wages (minimum floor)
- Example: 5-year employee = max(10 days, 5 days) = 10 days' pay
- Note: Separate from and in addition to termination notice

**Ontario ESA 2000 — Most complex provincial severance:**

- Eligibility: 5+ years of employment AND employer has $2.5M+ in global annual payroll
  OR the termination is part of a mass layoff (50+ employees within 6 months due to
  permanent closure)
- Calculation: 1 regular week's wages per completed year of employment (+ pro-rated
  fraction), maximum 26 weeks
- Note: Payable in addition to ESA termination notice (employee can receive up to 8 weeks
  notice + 26 weeks severance = 34 weeks total under the ESA alone)
- Critical: The $2.5M payroll threshold includes global affiliates, not just Ontario payroll

**All other provinces:** No statutory severance formula under the ESA — governed by
common law. Statutory obligation is termination notice (or pay in lieu) only.

**What to review:**

- For federally regulated employers: Is severance calculated and paid correctly on every
  termination (12+ months service, without just cause)?
- For Ontario employers: Is the $2.5M payroll threshold tracked? Most employers with
  meaningful Ontario operations will exceed it.
- Are severance and termination notice clearly separated in termination documentation?
- Are Ontario severance calculations based on regular weekly wages (not a reduced or
  averaged figure)?

---

### Area 8: Leaves of Absence

This is typically the highest-risk area for mid-size employers. Review each leave type
applicable in the jurisdiction(s) in scope.

#### 8A. Maternity Leave

| Jurisdiction        | Duration           | Pay                               | Eligibility               |
| ------------------- | ------------------ | --------------------------------- | ------------------------- |
| **Federal (CLC)**   | 17 weeks           | Unpaid (EI: 15 wks at 55%)        | All pregnant employees    |
| **Ontario**         | 17 weeks           | Unpaid (EI available)             | 13 weeks prior employment |
| **BC**              | 17 weeks           | Unpaid (EI available)             | Connected to employer     |
| **Alberta**         | 16 weeks           | Unpaid (EI available)             | 90 days prior employment  |
| **Quebec**          | 18 weeks           | Unpaid (QPIP: income replacement) | QPIP-eligible             |
| **Saskatchewan**    | 18 weeks           | Unpaid (EI available)             | —                         |
| **Manitoba**        | 17 weeks           | Unpaid (EI available)             | 7 months prior            |
| **Other provinces** | Typically 17 weeks | Unpaid (EI available)             | Varies                    |

**Quebec Parental Insurance Plan (QPIP):** Quebec is unique — QPIP replaces federal EI
maternity/parental benefits for Quebec employees. QPIP provides up to 55-75% of average
insurable earnings (max ~$1,319/week in 2025) and operates independently of federal EI.

#### 8B. Parental Leave

| Jurisdiction      | Standard                               | Extended/Shared               | Notes                               |
| ----------------- | -------------------------------------- | ----------------------------- | ----------------------------------- |
| **Federal (CLC)** | Up to 63 weeks                         | Up to 86 weeks (with sharing) | 5 weeks non-transferable per parent |
| **Ontario**       | 61 wks (if mat taken); 63 wks (if not) | —                             | 13 weeks prior employment           |
| **BC**            | 61 wks (if mat taken); 62 wks (if not) | —                             | Job restoration guaranteed          |
| **Alberta**       | 62 wks (if mat taken)                  | —                             | 90 days prior employment            |
| **Quebec**        | 65 weeks parental                      | + 5 wks paternity (unique)    | QPIP income replacement             |
| **Manitoba**      | Up to 66 weeks                         | —                             | —                                   |

**Quebec paternity leave (unique in Canada):** Quebec provides 5 weeks of dedicated
paternity leave for the father/non-birthing partner. This entitlement is separate from
general parental leave and is not available in any other Canadian jurisdiction under ESA.

#### 8C. Sick / Medical Leave

| Jurisdiction            | Statutory Minimum           | Pay                                                          | Notes                                  |
| ----------------------- | --------------------------- | ------------------------------------------------------------ | -------------------------------------- |
| **Federal (CLC)**       | 10 days/year                | Paid (accrual: 3 days after 30 days; +1/month after 60 days) | Bill C-3 (Dec 2021)                    |
| **Ontario**             | 3 days/year (2025)          | Unpaid (3 days) + Long-term illness leave (27 wks, 2025)     | Previously 3 days unpaid only          |
| **BC**                  | 5 days paid + 3 days unpaid | Paid (5 days); Unpaid (3)                                    | 90 days employment; highest in Canada  |
| **Alberta**             | 0 days                      | None                                                         | No statutory paid sick leave           |
| **Quebec**              | 2 days/year                 | Paid (by employer, based on wages)                           | LSST s.79.16                           |
| **Saskatchewan**        | 0 days                      | None                                                         | No statutory minimum                   |
| **Manitoba**            | 0 days                      | None                                                         | No statutory minimum                   |
| **PEI**                 | 1 day/year (after 5 years)  | Paid                                                         | Limited entitlement                    |
| **All other provinces** | 0 days typically            | None                                                         | Common law may imply sick day policies |

**BC employer obligation (since January 1, 2022):** 5 paid sick days + 3 unpaid sick days
for employees with 90+ days of employment. Employers cannot require medical notes for
absences of 5 days or fewer if it is the employee's first or second absence in the
calendar year.

**Federal CLC paid medical leave accrual:** 3 days paid after 30 days of continuous
employment, then 1 additional day per completed month of employment after 60 days, up to
a maximum of 10 days/year. Accrued days carry forward.

#### 8D. Family Violence / Domestic Violence Leave

| Jurisdiction      | Duration                       | Pay                                       | Notes       |
| ----------------- | ------------------------------ | ----------------------------------------- | ----------- |
| **Federal (CLC)** | 10 days/calendar year          | First 5 days paid (3+ months' employment) | CLC s.206.7 |
| **Ontario**       | 10 days + 15 weeks             | First 5 days paid; then unpaid            | ESA 2000    |
| **BC**            | 10 days                        | First 5 days paid (90 days' employment)   | BC ESA      |
| **Alberta**       | 10 days                        | First 5 days paid (90 days' employment)   | ESC         |
| **Saskatchewan**  | Included in protected leaves   | Varies                                    | —           |
| **PEI**           | 3 days (3+ months' employment) | Paid                                      | RSPEI 1988  |
| **Nunavut**       | 5 days                         | Paid                                      | —           |
| **Yukon**         | 5 days                         | Paid (90 days' employment)                | RSY 2002    |

#### 8E. Compassionate Care / Critical Illness Leave

**Federal (CLC):**

- Compassionate care leave: 28 weeks within a 52-week period (to care for family member
  with serious medical condition and significant risk of death); unpaid (EI available)
- Critical illness leave — child: 37 weeks within 52-week period; unpaid
- Critical illness leave — adult: 17 weeks within 52-week period; unpaid
- Multiple family members may take sequential leaves subject to combined time limits

**Provincial equivalents:** Most provinces provide comparable leaves under their ESA
(typically 8–28 weeks). Check each province's specific provisions.

#### 8F. Bereavement Leave

| Jurisdiction        | Duration                                       | Pay                                       | Notes        |
| ------------------- | ---------------------------------------------- | ----------------------------------------- | ------------ |
| **Federal (CLC)**   | Up to 10 days                                  | Subject to collective agreement or policy | Amended 2025 |
| **Ontario**         | 2 days                                         | Unpaid                                    | ESA 2000     |
| **BC**              | 3 days (immediate family); longer (child loss) | First 3 days paid (90 days' employment)   | BC ESA       |
| **Alberta**         | 3 days                                         | Unpaid                                    | ESC          |
| **Quebec**          | 1 day paid + bereavement rights                | 1 day at full pay; additional unpaid      | LSST         |
| **PEI**             | 3 days                                         | Unpaid                                    | —            |
| **Other provinces** | 1–5 days                                       | Typically unpaid                          | Varies       |

**What to review for all leaves:**

- Do HR policies acknowledge and provide all required leave types for each province?
- Are job restoration obligations being honoured? (Employee must be reinstated to same
  position with same or equivalent pay and benefits upon return)
- Are employees being penalized (demotion, reduced hours, discipline) for taking
  protected leave? (This is a prohibited act under all Canadian employment standards regimes)
- Are leave policies distinguishing between the protected leave (ESA minimum) and any
  enhanced employer benefits?

---

### Area 9: Equal Pay and Pay Equity

**Federal framework:**

- **Pay Equity Act** (in force September 2021): Applies to federally regulated employers
  with 10+ employees. Requires proactive pay equity analysis comparing predominantly
  female and male job classes of equal value. Pay equity plans must be posted and
  updated every 5 years.
- **Canadian Human Rights Act, s.11**: Applies to all federally regulated employers
  regardless of size — prohibits wage discrimination based on sex for work of equal value.
- **CLC equal pay for employment status** (coming into force late 2025/early 2026):
  Prohibits paying different wages based on employment status (full-time vs. part-time,
  permanent vs. casual) when employees perform substantially the same work under similar
  conditions. Permitted differentials: red-circling, recruitment/retention difficulties,
  geographic/hardship premiums, travel status pay, development/training programs.

**Provincial pay equity:**

- **Ontario Pay Equity Act**: Applies to employers with 10+ employees in Ontario. Requires
  gender-neutral job evaluation and maintenance of pay equity. Annual reviews for employers
  with 100+ employees.
- **Quebec LSST**: Prohibits wage discrimination based on sex; CNESST administers
- Other provinces: Equal pay provisions within ESA or human rights legislation; generally
  prohibit discrimination in wages

**What to review:**

- Federal employers (10+ employees): Is a Pay Equity Plan in place? Has it been posted?
  Is it up to date?
- Ontario employers (10+ employees): Has a pay equity assessment been conducted?
- Are part-time, casual, or contract workers paid differently than full-time comparators
  doing the same work? (Increasing risk under new CLC employment-status equal pay rule)
- Are tip-sharing practices (where applicable) structured in compliance with provincial
  tip protection rules?

---

### Area 10: Employment Records and Pay Statement Requirements

**Federal (CLC) — Mandatory:**

- **Pay statements**: Required with every payment of wages, including: employee name,
  pay period, regular and overtime hours, regular and overtime pay rates, gross pay,
  itemized deductions, net pay, year-to-date totals
- **Employment information statement** (effective July 9, 2023, Bill C-86):
  - For existing employees: Written statement provided within 90 days of July 9, 2023
  - For new employees: Within 30 days of start date
  - On material change: Within 30 days of any change
  - Content: Job title, occupational classification, regular rate of wages, hours of
    work, vacation entitlement, conditions of employment
- **Record retention**: 36 months after work is completed (ongoing employees: current
  records + 36 months after separation)
- **Record content**: Full name, address, SIN, occupational classification, sex, rate
  of wages, wage change dates, daily hours, overtime hours

**Provincial requirements** vary but generally require:

- Pay statements with each payment showing gross pay, deductions, net pay, pay period
- Record retention of 2-7 years depending on province
- Access by employees to their own records on request

**What to review:**

- Are pay statements being issued with every payment and do they include all required
  fields for each province?
- Federal employers: Have employment information statements been issued to all existing
  employees (post-July 9, 2023 obligation) and to all new hires within 30 days?
- Are payroll records retained for the required period?
- Are employees informed of their overtime rates and entitlements as required?

---

### Area 11: Employment Information and Contract Obligations

**Key obligations:**

- Federal employers must provide written employment information statements (see Area 10)
- Several provinces require written employment contracts or term disclosures before work
  begins or within prescribed periods of commencement
- BC, Ontario, and other provinces require specific disclosures for temporary agency workers

**What to review:**

- Do employment contracts accurately reflect statutory entitlements? (A contract clause
  providing less than the ESA minimum is void — the statutory minimum applies)
- Are employment contracts expressly linked to applicable provincial ESA to allow updates
  without contract amendment where legally permissible?
- Are temporary/agency worker arrangements properly documented per provincial requirements?

---

### Area 12: Group Termination / Mass Layoff

**Federal (CLC):**

- Group termination: 50+ employees terminated within a 4-week period
- Minimum 16 weeks' notice to the Minister of Labour
- Notice of the group termination must be posted in the workplace
- Individual ESA notice and severance rights remain in addition to group notice

**Ontario ESA 2000:**

- Mass termination: 50+ employees terminated within 4 weeks
- 8 weeks' notice (50-199 employees), 12 weeks (200-499), 16 weeks (500+)
- Termination pay in lieu can be substituted
- Does not eliminate individual termination notice/severance rights

**BC ESA:**

- Group termination: 50+ employees within 2 months
- Written notice to Minister required; varies by group size

**Saskatchewan (Bill 5, January 1, 2026):**

- Group termination threshold raised from 10 to 25 employees
- Notice requirements apply to affected group

**What to review:**

- Does the employer have a mass layoff protocol that identifies the applicable threshold
  for each province?
- Are group termination notices to the Ministry/Minister properly filed?
- Are affected employees receiving both group notice and their individual entitlements?

---

## Compliance Classification

Classify each finding using this three-tier system:

| Classification    | Meaning                                                                                                                  | Response Required                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **COMPLIANT**     | Practice meets or exceeds the statutory minimum                                                                          | Document for audit trail               |
| **PARTIAL**       | Practice partially meets the minimum; gaps exist but not fully non-compliant                                             | Remediation within 90 days recommended |
| **NON-COMPLIANT** | Practice fails to meet a statutory minimum; employer is exposed to regulatory enforcement, back-pay claims, or penalties | Immediate remediation required         |

**NON-COMPLIANT — automatic triggers (always classify at this level):**

- Any wage rate below the applicable statutory minimum wage
- Failure to pay required overtime for non-exempt hours
- Denial of a protected leave to an eligible employee
- Failure to reinstate an employee after a protected leave
- Failure to provide required termination notice or severance pay
- Calculation of vacation pay as a percentage of base salary only (where gross wages
  definition is broader)
- Applying "just cause" termination without a legally defensible basis and withholding
  notice/severance

**PARTIAL — typical indicators:**

- Policy exists but contains incorrect thresholds (e.g., using 40-hour OT threshold
  in Ontario where it is 44 hours)
- Leave policy exists but does not cover all required leave types
- Pay statements issued but missing required fields
- Vacation entitlement correct but vacation pay % calculation methodology uncertain

---

## Actionable Output Per Finding

For each PARTIAL or NON-COMPLIANT finding, generate:

```
Finding [#]: [Area] — [Jurisdiction]
Classification: PARTIAL / NON-COMPLIANT
Statutory Basis: [Statute, section]
Issue: [Specific description of the gap or non-compliance]
Employer's Current Practice: [What the employer currently does]
Required Standard: [What the statute requires]
Retroactive Exposure: [Estimate of back-pay or penalty exposure, if calculable]
Remediation: [Specific corrective action required]
Suggested Language (if applicable): [Draft policy or contract clause]
Timeline: IMMEDIATE / 30 DAYS / 90 DAYS
```

**Retroactive exposure calculation guidance:**

- Back wages: (Required rate − Actual rate) × hours worked × affected employees × months
  of non-compliance
- Vacation shortfall: (Required % − Applied %) × gross wages × affected employees × years
- Termination underpayment: (Required notice weeks − Provided weeks) × regular weekly wages
  × affected terminations
- Note: Employment Standards Officers may order back payment for up to 2-5 years of
  underpayment depending on jurisdiction

---

## Prioritization Framework

Rank each finding using this four-tier priority framework:

| Priority     | Criteria                                                                                                                         | Typical Timeline                   | Examples                                                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL** | Ongoing statutory violation; employees being underpaid below minimum wage or denied protected leave; regulatory enforcement risk | Immediate (within 5 business days) | Wages below minimum wage; denial of maternity/parental leave; failure to pay overtime to non-exempt employees                                     |
| **HIGH**     | Significant regulatory gap; material retroactive exposure; class-action or complaint risk                                        | 30 days                            | Incorrect overtime calculation; vacation pay % applied to base only; incorrect severance formula; CLC employment information statement not issued |
| **MEDIUM**   | Policy gaps that may become violations; incorrect thresholds that have not yet produced underpayments                            | 90 days                            | Policy refers to wrong overtime threshold; leave policy missing a required leave type; record retention policies below requirement                |
| **LOW**      | Best-practice gaps or administrative deficiencies that do not currently produce statutory violations                             | 180 days                           | Pay stubs missing a non-material field; contracts silent on a permissible practice; vacation scheduling notice below recommended period           |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering the output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                               | Fail Action                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Source**     | Every compliance finding cites a specific statutory provision (statute + section)                                  | Add citation or mark "[UNVERIFIED — CONFIRM PROVISION]"     |
| **Format**     | Statutory citations follow the Canadian standard (e.g., "CLC s.230"; "ESA 2000, s.50(1)"; "CQLR c N-1.1, s.79.16") | Fix format                                                  |
| **Currency**   | Every rate and threshold confirmed as current to the date of review                                                | Flag "[VERIFY CURRENT RATE — ESA minimums change annually]" |
| **Domain**     | Analysis stays within the applicable jurisdiction's regime; no bleed from Ontario ESA into federal analysis        | Remove or flag jurisdictional bleed                         |
| **Confidence** | Uncertainty stated explicitly, not hidden in confident-sounding language                                           | Add confidence qualifier                                    |

### Self-Interrogation for NON-COMPLIANT Findings

For any NON-COMPLIANT finding, apply this 3-pass review before finalizing:

**Pass 1 — Legal Chain Integrity:** Does the finding follow logically from the cited
statutory provision? Would an Employment Standards Officer applying this statute actually
reach this conclusion? Is there an exemption or exception that might apply?

**Pass 2 — Completeness:** Have all relevant provisions been considered, including any
regulations, ministerial orders, or interpretive guidance? Are there 2024-2026 amendments
that affect this analysis?

**Pass 3 — Challenge:** What is the employer's strongest argument that this is compliant?
Under what circumstances might a reasonable employment lawyer accept the current practice?
(Preserve this challenge in the output so the user can make an informed decision.)

### Confidence Scoring

| Level        | Range     | Meaning                                        | Action                                                    |
| ------------ | --------- | ---------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory text, settled interpretation   | State compliance finding with confidence                  |
| **High**     | 0.80–0.94 | Strong authority, minor interpretive questions | State finding with brief caveat                           |
| **Probable** | 0.60–0.79 | Good arguments, could be read differently      | State finding with reasoning and note uncertainty         |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on facts          | Flag for qualified legal review; present both sides       |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                        | Do not assert; flag "[UNCERTAIN — LEGAL REVIEW REQUIRED]" |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-ca-employment-standards-review"
  review_date: "[date]"
  jurisdictions_analyzed: "[list all jurisdictions reviewed]"
  employer_industry: "[federally regulated / Ontario / BC / multi-provincial / etc.]"
  documents_reviewed: "[list of documents provided by user]"
  documents_absent: "[list of documents not provided that would improve analysis]"
  areas_covered: "[list of 12 areas reviewed; note any excluded]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-ca-esa-authority.md or 'Not created'"
  rates_verified_to: "[date of last rate verification or 'Not verified — use VERIFY CURRENT RATE markers']"
  total_findings: "[number]"
  by_classification:
    compliant: "[number]"
    partial: "[number]"
    non_compliant: "[number]"
  by_priority:
    critical: "[number]"
    high: "[number]"
    medium: "[number]"
    low: "[number]"
  retroactive_exposure_estimate: "[dollar estimate or 'Not calculable from available information']"
  confidence: "HIGH / MEDIUM / LOW — [brief rationale]"
  limitations:
    - "[Any scope limitations — e.g., payroll data not provided; analysis based on policies only]"
    - "[Rates not independently verified — marked with [VERIFY CURRENT RATE] throughout]"
    - "[Common law termination obligations (beyond ESA minimums) not assessed]"
    - "[Human rights, health and safety, and labour relations not in scope]"
  reviewer: "AI-assisted — requires review by qualified Canadian employment lawyer"
```

---

## Anti-Patterns

What NOT to do when applying Canadian employment standards:

1. **"Head office province governs" fallacy** — The ESA of the province where the employee
   physically performs work applies — not where the employer is incorporated or has its
   head office. Remote workers in BC are governed by BC law, even if the employer is
   headquartered in Ontario.

2. **Federal/provincial confusion on jurisdiction** — Not all nationally operating
   employers are federally regulated. A retail chain operating coast to coast is
   provincially regulated in each province. Only specific industries listed in the
   Constitution Act (banking, telecoms, interprovincial transport, etc.) are federal.

3. **"Salaried exempt" blanket application** — Canada has no US-style salary-basis
   overtime exemption. A salaried employee who is not a genuine manager, supervisor, or
   listed professional is entitled to overtime. Many Canadian employers wrongly assume
   salary = exempt.

4. **Overtime threshold misidentification** — Ontario's overtime threshold is 44 hours/week
   (not 40). Federal, BC, Quebec, Saskatchewan, Manitoba, NL, NWT, Nunavut, and Yukon
   are 40 hours. Nova Scotia and PEI are 48 hours. Alberta and BC have daily thresholds
   in addition to weekly. Using the wrong threshold creates systematic underpayment.

5. **Vacation pay on base salary only** — Vacation pay is typically calculated on "gross
   wages," which includes commissions, bonuses, and overtime pay — not just base salary
   or base hourly wages. Applying the percentage only to base pay is a systemic undercount
   of the vacation pay obligation.

6. **Ontario severance eligibility blind spot** — Many Ontario employers do not track
   whether their total global payroll exceeds $2.5M and therefore miss the ESA severance
   obligation. The threshold applies to global payroll, not Ontario payroll alone.

7. **"Use-it-or-lose-it" vacation policies** — While common in the US, blanket forfeiture
   of unused vacation is prohibited or legally questionable in most Canadian jurisdictions.
   Newfoundland expressly prohibits it. Employers should structure vacation scheduling
   obligations rather than forfeiture clauses.

8. **Averaging agreements without documentation** — Federal employers who implement
   flexible work schedules without a properly documented averaging agreement (including
   30-day advance notice, workplace posting, and union copy) are in breach of CLC
   hours-of-work requirements. The arrangement must be documented before it begins.

9. **Common law note confusion** — ESA minimums are regulatory floors. A termination
   package that meets the ESA minimum notice and severance is NOT immune from common law
   wrongful dismissal claims. Employers who conflate "ESA compliant" with "legally
   protected" create litigation risk.

10. **Job restoration failure after protected leave** — The obligation is to reinstate the
    employee to the same position (or comparable equivalent) with the same wages and
    benefits. Offering a lesser role, reducing hours, or changing reporting relationships
    upon return from maternity, parental, or medical leave is a prohibited act and triggers
    personal liability for HR managers and supervisors in some provinces.

11. **Independent contractor misclassification** — Workers who are economically dependent
    on a single employer, work under the employer's direction, and use employer tools are
    likely employees under most Canadian ESAs regardless of contract label. Misclassification
    denies workers their statutory minimums and creates significant retroactive exposure.

12. **Federal CLC termination notice schedule pre-February 2024** — Many federally regulated
    employers still apply the old termination notice schedule. The February 1, 2024
    amendments significantly increased the graduated notice periods (up to 8 weeks for
    employees with 8+ years of service). Using the old schedule underpays termination
    notice for long-service employees.

13. **BC daily overtime threshold ignored** — BC is one of only two jurisdictions (with
    Alberta) that has a daily overtime threshold in addition to a weekly one. Hours over
    8 in a day attract 1.5× overtime; hours over 12 in a day attract 2× overtime. Employers
    scheduling 10-hour days without overtime compensation are in breach of the BC ESA.

14. **Quebec paternity leave and QPIP omission** — Quebec employees (and their employers)
    interact with the Quebec Parental Insurance Plan rather than federal EI for parental
    benefits. Both partners are entitled to receive distinct parental benefits under QPIP.
    The father/non-birthing partner's 5-week paternity entitlement is a protected leave
    under the LSST. Employers who do not recognize this leave violate the statute.

15. **Ignoring federal CLC employment information statement obligation** — Federally
    regulated employers must have issued written employment information statements to
    all existing employees (by October 7, 2023) and to new employees within 30 days of
    hiring. Failure to comply constitutes a breach of the CLC since July 2023.

16. **Saskatchewan consecutive vacation requirement** — Saskatchewan's ESA requires that
    annual vacation be taken consecutively (not scattered individual days), unless the
    employee agrees otherwise. Employers who allow/require piecemeal vacation without
    written employee agreement are non-compliant with the SEA.

17. **BC sick leave documentation restrictions** — BC employers cannot request medical
    documentation for an employee's first or second illness-related absence of 5 days or
    fewer in a calendar year. Requiring a doctor's note in these circumstances violates
    the BC ESA and may give rise to a complaint.

18. **Pay Equity Act complacency (federal)** — The federal Pay Equity Act has been in force
    since September 2021. Federally regulated employers with 10+ employees must have a
    pay equity plan in place, posted, and maintained. The obligation is proactive —
    employers cannot wait for a complaint.

---

## Writing Standards

Before delivering the compliance report:

1. **Lead with the risk register** — Present CRITICAL and HIGH findings first. Users need
   to know the most urgent issues immediately.

2. **Use plain English** — Employment standards compliance reports are used by HR
   professionals and business operators, not just lawyers. Explain each finding in terms
   of what the employer must do, not just what the statute says.

3. **Be specific about jurisdiction** — Every finding must identify the jurisdiction (e.g.,
   "BC ESA — not applicable to your Ontario operations"). Multi-province analyses must
   segregate findings clearly.

4. **Quantify exposure where possible** — Regulatory findings without exposure estimates
   are less actionable. Even rough estimates ("approximately $X per year for affected
   employees") are valuable.

5. **Do not hedge uniformly** — Reserve uncertainty language for genuinely uncertain
   points. Stating "this may or may not comply" for a clear statutory violation understates
   the risk. Distinguish confident findings from uncertain ones.

6. **Flag rate change risk** — Minimum wages and leave entitlements change annually in
   most Canadian provinces. The compliance report should note any upcoming scheduled
   changes the employer should prepare for.

7. **Self-review before delivery:**
   - [ ] Every NON-COMPLIANT finding has a specific statutory citation
   - [ ] All minimum wage rates are flagged as current-to-date or marked [VERIFY]
   - [ ] Every jurisdiction-specific analysis is labelled with its jurisdiction
   - [ ] Anti-patterns have been checked against the employer's practices
   - [ ] The Glass Box audit trail is complete
   - [ ] Retroactive exposure is estimated or the data gap is noted

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for current minimum wage rates per province (updated annually; always verify
  current rates before delivery)
- Retrieve the full text of relevant CLC, ESA, and ESC provisions under review
- Identify recent amendments and their coming-into-force dates
- Search for ESDC or provincial Labour Ministry interpretive guidance on contested points
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Use the reference frameworks in this skill (current as of 2026-03-21)
- Mark all minimum wage rates with [VERIFY CURRENT RATE]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Direct user to verify rates at:
  - Federal: canada.ca/federal-labour-standards
  - Ontario: ontario.ca/document/your-guide-employment-standards-act-0
  - BC: gov.bc.ca/employment-standards
  - Alberta: alberta.ca/employment-standards
  - Quebec: cnesst.gouv.qc.ca
  - All provinces: CanLII (canlii.org) for statutory text

---

## Localization Notes

This skill is designed for Canadian employment standards only. When operating in
multi-national contexts:

- Employees working in Canada but employed by non-Canadian parent companies are still
  governed by the Canadian ESA of their province of work — the employment standards
  cannot be contracted out by choosing a foreign governing law
- The skill does not cover employment standards in other countries (US, UK, EU, etc.)
  — use jurisdiction-specific skills for those analyses
- Indigenous employment on reserves may be governed by federal law or band governance
  — seek specialized advice

---

## Output Format Template

```markdown
# Canadian Employment Standards Compliance Report

**Employer:** [Employer name]
**Date of Review:** [Date]
**Jurisdictions Reviewed:** [List]
**Documents Reviewed:** [List]
**Prepared by:** Legalcode AI-Assisted Analysis (not legal advice)

---

## Executive Summary

**Overall Compliance Status:** [COMPLIANT / REQUIRES ATTENTION / NON-COMPLIANT]
**Total Findings:** [N] findings ([N] CRITICAL, [N] HIGH, [N] MEDIUM, [N] LOW)
**Estimated Retroactive Exposure:** [$ estimate or "Not calculable from available information"]

### Top 3 Priority Issues

1. [CRITICAL/HIGH finding 1 — one sentence]
2. [CRITICAL/HIGH finding 2 — one sentence]
3. [CRITICAL/HIGH finding 3 — one sentence]

---

## Jurisdictional Determination

| Employee Group | Province of Work | Governing Legislation | Notes                              |
| -------------- | ---------------- | --------------------- | ---------------------------------- |
| [Group 1]      | [Province]       | [Statute]             | [Federal/provincial determination] |

---

## Risk Register

| #   | Area   | Jurisdiction | Classification         | Priority | Statutory Basis | Summary          |
| --- | ------ | ------------ | ---------------------- | -------- | --------------- | ---------------- |
| 1   | [Area] | [Province]   | CRITICAL/NON-COMPLIANT | CRITICAL | [Statute, s.X]  | [One-line issue] |
| 2   | [Area] | [Province]   | NON-COMPLIANT          | HIGH     | [Statute, s.X]  | [One-line issue] |
| ... |        |              |                        |          |                 |                  |

---

## Detailed Findings

### Finding 1: [Area] — [Jurisdiction]

**Classification:** NON-COMPLIANT / PARTIAL / COMPLIANT
**Priority:** CRITICAL / HIGH / MEDIUM / LOW
**Statutory Basis:** [Statute, section number]
**Confidence:** [Definite / High / Probable / Possible]

**Issue:** [Specific description of the gap]

**Employer's Current Practice:** [What the employer currently does]

**Required Standard:** [What the statute requires]

**Retroactive Exposure:** [Dollar estimate or description of exposure]

**Remediation:**

- [Specific action 1]
- [Specific action 2]

**Suggested Policy/Contract Language (where applicable):**

> [Draft language]

**Timeline:** IMMEDIATE / 30 DAYS / 90 DAYS

**Employer's Strongest Counter-Argument:** [Pass 3 of Self-Interrogation — circumstances
where a reasonable lawyer might accept the current practice]

---

## Jurisdiction-by-Jurisdiction Summary

### [Province/Federal]

| Area                   | Classification | Finding                                              |
| ---------------------- | -------------- | ---------------------------------------------------- |
| Minimum Wage           | COMPLIANT      | Current rate: $X.XX/hr; Employer pays: $X.XX/hr      |
| Hours of Work          | COMPLIANT      | —                                                    |
| Overtime               | NON-COMPLIANT  | See Finding [#]                                      |
| Vacation               | PARTIAL        | See Finding [#]                                      |
| Statutory Holidays     | COMPLIANT      | —                                                    |
| Termination Notice     | COMPLIANT      | —                                                    |
| Severance Pay          | N/A            | Not applicable (province has no statutory severance) |
| Leaves                 | PARTIAL        | See Finding [#]                                      |
| Equal Pay              | COMPLIANT      | —                                                    |
| Records/Pay Statements | COMPLIANT      | —                                                    |
| Employment Information | NON-COMPLIANT  | See Finding [#]                                      |
| Group Termination      | N/A            | No group termination events in scope                 |

---

## Upcoming Changes to Monitor

| Jurisdiction | Change                                        | Effective Date | Action Required         |
| ------------ | --------------------------------------------- | -------------- | ----------------------- |
| [Province]   | [Rate change / new leave / amended provision] | [Date]         | [What employer must do] |

---

## Limitations of This Analysis

- [Document gap: payroll data not provided — rates could not be verified against actual pay]
- [Minimum wage rates marked [VERIFY] should be confirmed against current government sources]
- [Common law wrongful dismissal obligations not assessed — ESA minimums only]
- [Human rights, occupational health and safety, and labour relations legislation not in scope]
- [This analysis does not constitute legal advice — review with qualified employment counsel]

---

## Glass Box Audit Trail

[Complete YAML block from the Glass Box section above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis. Research conducted via
web-backed analysis of official government sources (Canada.ca, ESDC, provincial labour
ministry portals, CanLII), law firm practice advisories (McCarthy Tétrault, Fasken,
Stikeman Elliott, Norton Rose Fulbright, McMillan, Borden Ladner Gervais, DLA Piper,
Cox & Palmer, Miller Thomson), and employment standards guidance published under Bill C-3
(2021) and Bill C-86 (2023). Rates current to 2026-03-21 — verify all rates before use.
