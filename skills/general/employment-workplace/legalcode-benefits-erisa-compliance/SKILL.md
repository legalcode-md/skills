---
name: legalcode-benefits-erisa-compliance
description: Assess ERISA compliance for US employee benefit plans — fiduciary duties, prohibited transactions,
  plan document requirements, SPDs, Form 5500, COBRA, HIPAA portability, ACA employer mandate (IRC § 4980H),
  Mental Health Parity (MHPAEA), and retirement plan qualification (401(k), 403(b), defined benefit).
  Covers recent DOL and IRS guidance including SECURE 2.0 Act, MHPAEA 2024 Final Rule enforcement status,
  Cunningham v. Cornell (April 2025), DOL Fiduciary Rule vacatur, and current indexed thresholds for 2025/2026.
  Use when auditing benefit plan compliance, responding to DOL or IRS inquiries, preparing for plan sponsor
  due diligence, analyzing M&A benefit plan exposure, assessing fiduciary liability, or building an annual
  compliance calendar for ERISA-governed health, welfare, or retirement plans.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode ERISA Benefits Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted ERISA compliance
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified ERISA attorney, enrolled actuary (for defined benefit plans), or certified
> employee benefits professional before reliance. Laws change, thresholds adjust annually,
> and regulatory guidance evolves — verify all cited provisions against current DOL, IRS,
> and PBGC publications before acting. Statutory and regulatory references carry
> hallucination risk; verify against authoritative sources. Dollar thresholds (IRC §§
> 402(g), 415, 4980H, 4980B, 4980D) change annually and must be confirmed for the
> current plan year.

---

## Purpose and Scope

This skill assesses ERISA compliance for US employer-sponsored benefit plans across two
major regulatory tracks: **health and welfare plans** and **retirement plans**.

**Covers:**

- Fiduciary duty analysis under ERISA §§ 401–414 (prudence, loyalty, diversification,
  plan documents; settlor vs. fiduciary function distinction)
- Prohibited transaction screening (ERISA § 406, IRC § 4975) with exemption analysis
  (ERISA § 408, DOL class PTEs)
- Plan document compliance (ERISA § 402; SECURE 2.0 amendment requirements)
- Summary Plan Descriptions and required notices (ERISA § 102; 29 C.F.R. § 2520.102-3)
- Form 5500 filing compliance (ERISA § 104; DFVCP penalty relief)
- COBRA continuation coverage (ERISA §§ 601–608; IRC § 4980B)
- HIPAA portability, special enrollment, and wellness programs
- ACA employer mandate (IRC § 4980H) — ALE determination, penalties, and safe harbors
- Mental Health Parity (MHPAEA, 29 U.S.C. § 1185a) including NQTL comparative analysis
- Retirement plan qualification: 401(k) ADP/ACP testing, 403(b) universal availability,
  defined benefit minimum funding (IRC § 412), contribution limits (IRC §§ 402(g), 415)
- Current DOL and IRS guidance: SECURE 2.0, Cunningham v. Cornell, DOL Fiduciary Rule
  vacatur, MHPAEA 2024 Final Rule enforcement pause
- Excise tax and civil penalty quantification with correction program identification

**Does not:**

- Provide legal advice or replace qualified ERISA counsel
- Conduct actuarial certifications for defined benefit plans (refer to an enrolled actuary)
- Address non-ERISA benefit programs (governmental plans, church plans with ERISA
  exemption) unless specifically in scope
- Cover multiemployer plan withdrawal liability (ERISA §§ 4201–4225) in depth
- Replace DOL or IRS audits — findings are preliminary and require professional review

**Jurisdiction**: United States federal law only. ERISA preempts most state laws relating
to employee benefit plans (ERISA § 514(a)), subject to the savings clause for state
insurance regulation (§ 514(b)(2)(A)) and the deemer clause (§ 514(b)(2)(B)).
State-specific requirements for fully insured plans are noted where material.

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **⟁ CLARIFY**) at key decision
points. Rather than assuming the user's intent, the workflow pauses and asks when:

- Employer size or controlled group composition changes the applicable regulatory regime
- The plan type (health/welfare vs. retirement; individual account vs. defined benefit)
  determines which compliance tracks apply
- ERISA coverage status (church plan, governmental plan exemption) is uncertain
- The scope of assessment (full ERISA stack vs. targeted compliance review) must be
  defined before proceeding

If the user has already provided this information, skip the question and proceed.

---

## Regulatory Framework

### Governing Statutes and Primary Regulations

| Source                 | Statute                                      | Primary Subject                                         |
| ---------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **DOL/EBSA (Title I)** | ERISA §§ 401–514; 29 U.S.C. §§ 1001–1461     | Fiduciary duties, reporting, disclosure, enforcement    |
| **IRS (Title II)**     | IRC §§ 401–420, 4975, 4980B, 4980D, 4980H    | Tax qualification, prohibited transactions, ACA mandate |
| **PBGC (Title IV)**    | ERISA §§ 4001–4402                           | DB plan termination insurance and premiums              |
| **DOL Regulations**    | 29 C.F.R. §§ 2520–2590                       | ERISA procedural and substantive requirements           |
| **IRS Regulations**    | 26 C.F.R. §§ 1.401–1.415; 54.4980B; 54.4980H | Tax qualification and excise tax                        |
| **SECURE 2.0 Act**     | P.L. 117-328 (Dec. 29, 2022)                 | 90+ provisions; staggered effective dates through 2027+ |

### Dual-Regulator Structure

ERISA and the IRC are parallel statutes enforced by **different agencies**. Every finding
must attribute the correct regulatory authority:

- **DOL/EBSA** → Title I fiduciary breaches, reporting violations, disclosure failures,
  COBRA and HIPAA portability, MHPAEA
- **IRS** → Tax qualification failures, plan disqualification, ACA employer mandate
  (IRC § 4980H), COBRA excise taxes (IRC § 4980B), PT excise taxes (IRC § 4975)
- **PBGC** → DB plan termination, PBGC premiums, reportable events

Conflating ERISA § 404 (fiduciary duty) with IRC § 404 (deductibility limits), or ERISA
§ 401 (coverage) with IRC § 401 (qualified plan), is a common and consequential error.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Plan description narrative**: Employer name, number of employees, plan types,
  industry, ownership structure, description of compliance concern
- **Plan document set**: Plan document(s), SPD(s), trust agreement, investment policy
  statement, service provider contracts, Form 5500 filings, prior audit findings
- **Incident trigger**: A specific compliance concern (missed filing, late deferral
  deposits, prohibited transaction, failed nondiscrimination test, DOL audit letter)
- **M&A due diligence scope**: Target company benefit plans requiring compliance review
- **Annual compliance calendar build**: Employer with no structured compliance workflow

**Minimum required context before proceeding**: Employer name (or description), plan
type(s) in scope, approximate number of employees, and purpose of the assessment.

### Step 2: Context Gathering

**⟁ CLARIFY — Plan Sponsor Profile**

The map of applicable ERISA requirements depends entirely on employer size, plan types,
and the employer's role. Gather the following before proceeding:

1. **Employer size and structure**:
   - _Single employer, <20 employees_: COBRA does not apply; ACA mandate not triggered
   - _20–49 employees_: COBRA applies; ACA mandate not yet triggered
   - _50+ FTEs (Applicable Large Employer — ALE)_: ACA § 4980H mandate applies;
     Forms 1094-C/1095-C required
   - _100+ plan participants at beginning of plan year_: Form 5500 large-plan audit required
   - _Controlled group / affiliated service group (IRC § 414(b), (c), (m), (o))_:
     Aggregation required for ALE determination, nondiscrimination testing, and top-heavy
   - _Why this matters_: Size drives the complete map of ERISA requirements.

2. **Plan types in scope** (select all that apply):
   - _Health and welfare only_: COBRA, HIPAA, ACA, MHPAEA, SPD/claims procedures
   - _Retirement plans only_: Qualification, fiduciary, Form 5500, prohibited transactions
   - _Both_: Full ERISA stack
   - _Specific plan type_: [401(k), 403(b), DB, ESOP, group health, FSA, HRA, NQDC]
   - _Why this matters_: Divides the assessment into separate compliance tracks.

3. **Plan sponsor role**:
   - _Plan administrator (most common)_: Full ERISA § 402 fiduciary obligations
   - _Named fiduciary only, with separate plan administrator_: Scope to specific duties
   - _Participating employer in MEP/PEP_: Employer-level obligations vs. pooled provider
   - _Church or governmental employer_: Determine ERISA coverage first
   - _Why this matters_: ERISA § 4 exemptions can eliminate the entire framework.

4. **Assessment purpose**:
   - Annual compliance review, M&A due diligence, DOL/IRS audit response, specific
     incident investigation, or new plan setup
   - _Why this matters_: Determines depth, urgency framing, and remediation focus.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve current legal authority. Save the most
relevant results to `/tmp/erisa-assessment-authority.md`, structured as:

```markdown
# ERISA Compliance Authority — [Employer / Plan Name]

## Assessment Date: [YYYY-MM-DD]

## Plan Year: [YYYY]

### Statutory Authority

- [Citation, section, relevance]

### Current Indexed Thresholds (verify annually)

- 402(g) elective deferral limit: [amount] (Source: IRS Notice [YYYY-NN])
- 415(c) annual additions: [amount]
- 4980H(a) penalty: [amount/FTE]
- 4980H(b) penalty: [amount/FTE]
- [Additional thresholds as applicable]

### Recent Guidance (DOL/IRS/PBGC)

- [Guidance title, date, relevance to this assessment]

### Case Law

- [Case, citation, holding relevant to assessment]
```

**If legalcode-mcp is not connected:**

- Mark all statutory dollar amounts and indexed thresholds with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all thresholds require
current-year verification"`
- Proceed with the assessment using the most recently known figures as indicative only

**Key thresholds to always verify for current plan year** (all change annually — see
Citation Quality Gate 4):

- IRC § 402(g): 2025 = $23,500; 2026 = $24,500 [VERIFY current year via IRS Notice]
- IRC § 415(c): 2025 = $70,000; 2026 = $72,000 [VERIFY]
- IRC § 401(a)(17) comp cap: 2025 = $345,000; 2026 = $350,000 [VERIFY]
- IRC § 414(q) HCE threshold: 2025 = $160,000; 2026 = $160,000 [VERIFY]
- IRC § 4980H(a) penalty: 2025 = $2,900/FTE; 2026 = $3,340/FTE [VERIFY]
- IRC § 4980H(b) penalty: 2025 = $4,350/FTE; 2026 = $5,010/FTE [VERIFY]
- ACA affordability %: 2025 = 9.02%; 2026 = 9.96% [VERIFY]
- PBGC flat-rate premium: 2025 = $101/participant [VERIFY via PBGC premium notice]
- PBGC variable-rate: 2025 = $52/$1,000 unfunded vested benefits [VERIFY]

### Step 4: ERISA Coverage Scope Gate

**Binary gate: Determine whether ERISA applies and at what level BEFORE assessing any
substantive requirement.**

Apply ERISA § 4 analysis:

- Does the employer maintain a plan for the purpose of providing benefits to employees?
- Is the employer an agency or instrumentality of a government? (§ 4(b)(1) — governmental
  plan — exempt from ERISA Title I; may still be subject to IRC)
- Is the plan established or maintained by a church or church-controlled organization?
  (§ 4(b)(2) — church plan under IRC § 414(e); _Advocate Health Care Network v.
  Stapleton_, 137 S. Ct. 1652 (2017) governs church plan status for nonprofit hospitals)
- Is the plan an "excess benefit plan" for top hat employees? (§ 4(b)(5) — exempt from
  most of Title I but must file a one-time top hat exemption statement under 29 C.F.R.
  § 2520.104-23)

**⟁ CLARIFY** — If the employer is a nonprofit, religious organization, hospital, school,
government contractor, or tribal government, pause here and clarify ERISA coverage status
before proceeding. Proceeding with ERISA fiduciary analysis for an exempt plan wastes
effort and may produce materially wrong conclusions.

### Step 5: Health and Welfare Plan Compliance Assessment

**Activate this step if the employer maintains group health plans.**

Assess in this sequence:

#### 5a. ACA Employer Mandate (IRC § 4980H)

- **ALE determination**: Average 50+ full-time equivalent employees (FTEs) in the
  prior calendar year. Full-time = 30+ hours/week (or 130 hours/month). FTE equivalents
  = aggregate part-time hours ÷ 120.
- **Controlled group aggregation**: Apply IRC § 414(b)/(c)/(m)/(o) — all related
  entities are treated as a single employer for ALE determination. Acquisition errors
  here are extremely common.
- **Coverage offer**: Must offer Minimum Essential Coverage (MEC) to ≥95% of full-time
  employees (and their dependents).
- **Minimum Value**: Coverage must pay at least 60% actuarial value.
- **Affordability**: Employee premium for self-only coverage ≤ applicable percentage
  of household income. Three safe harbors: W-2, Rate of Pay, Federal Poverty Level.
- **Current affordability percentage**: 9.96% (2026); 9.02% (2025) [VERIFY].
- **Penalty exposure**:
  - § 4980H(a) "no offer" sledgehammer: [VERIFY current year] — 2026 = $3,340/FTE
    annually (minus first 30 employees)
  - § 4980H(b) "unaffordable/not MV" tack hammer: [VERIFY] — 2026 = $5,010/FTE who
    receives marketplace premium tax credit
- **Reporting**: Forms 1094-C and 1095-C filed with IRS; Form 1095-C furnished to
  employees by March 31.
- **IRS audit trigger**: IRS Letter 226-J (preliminary penalty assessment) — employer
  has 30 days to respond via Form 14764/14765.

#### 5b. COBRA (ERISA §§ 601–608; IRC § 4980B; 26 C.F.R. § 54.4980B)

Applies to employers with 20+ employees.

**Qualifying events and maximum coverage periods**:

| Qualifying Event                                        | Covered Individuals                    | Max Duration |
| ------------------------------------------------------- | -------------------------------------- | ------------ |
| Termination (non-gross misconduct) / Reduction in hours | Employee + spouse + dependents         | 18 months    |
| Social Security disability (SSA-determined)             | Employee + spouse + dependents         | 29 months    |
| Death of covered employee                               | Spouse + dependents                    | 36 months    |
| Divorce or legal separation                             | Spouse + dependents                    | 36 months    |
| Medicare entitlement of employee                        | Spouse + dependents                    | 36 months    |
| Loss of dependent status                                | Dependent child                        | 36 months    |
| Employer bankruptcy (retiree coverage)                  | Retired employee + spouse + dependents | Lifetime     |

**Notice chain** (each link must be timely for the next to be triggered):

| Notice                  | Who Sends                                  | Timing                                                                               | Authority              |
| ----------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------- |
| Initial General Notice  | Plan administrator → participant           | Within **90 days** of coverage                                                       | 29 C.F.R. § 2590.606-1 |
| Qualifying event notice | Employer → plan administrator              | Within **30 days** of employer-known QE                                              | 29 C.F.R. § 2590.606-2 |
| Qualifying event notice | Employee/dependent → plan administrator    | Within **60 days** for divorce/disability/dependent loss                             | 29 C.F.R. § 2590.606-3 |
| Election notice         | Plan administrator → qualified beneficiary | Within **14 days** of receiving QE notice (44 days if employer = plan administrator) | 29 C.F.R. § 2590.606-4 |

**Election period**: 60 days from later of: date of QE or date election notice provided.
**Premium**: ≤ 102% of applicable cost; 150% during disability extension (months 19–29).
**Penalty**: IRC § 4980B — $100/day/qualified beneficiary; minimum $2,500/participant/
occurrence; $15,000 minimum in egregious cases. [VERIFY current indexed amounts]

#### 5c. HIPAA Portability (ERISA §§ 701–734; IRC §§ 9801–9806; 29 C.F.R. §§ 2590.701 et seq.)

- **Pre-existing condition exclusions**: Eliminated for all group health plans effective
  for plan years beginning on or after January 1, 2014 (ACA). No additional analysis
  needed for plans established after that date.
- **Special enrollment rights** (29 C.F.R. § 2590.701-6):
  - Loss of other group coverage: 30-day enrollment window
  - Marriage, birth, or adoption: 30 days (60 days for Medicaid/CHIP events)
  - Loss of Medicaid or CHIP eligibility or gain of Medicaid/CHIP eligibility: 60 days
- **Wellness programs** (29 C.F.R. § 2590.702(f)):
  - _Participatory programs_ (no health standard required): No reward limit
  - _Health-contingent programs_: Reward ≤ 30% of employee-only coverage cost (50%
    for tobacco-cessation programs)
  - GINA (Pub. L. 110-233) prohibits using genetic information (including family medical
    history) as a condition of program participation or for adjusting rewards
- **Penalty**: IRC § 4980D — $100/day/individual; minimum $2,500/occurrence;
  maximum $500,000/plan year. [VERIFY current indexed amounts]

#### 5d. MHPAEA (29 U.S.C. § 1185a; IRC § 9812; 29 C.F.R. § 2590.712)

Mental Health Parity and Addiction Equity Act of 2008, as amended by CAA 2021.

**Current regulatory status (as of March 2026)**:

- The MHPAEA 2024 Final Rule (89 Fed. Reg. 61,596, September 9, 2024) was issued with
  an effective date of January 1, 2025.
- **Enforcement pause**: DOL, HHS, and Treasury announced on May 15, 2025 that they
  would immediately halt enforcement of the 2024 Final Rule pending litigation resolution,
  plus an additional 18-month enforcement pause. The pre-2024 NQTL standards under CAA
  2021 and Technical Release 2023-01 remain the operative compliance framework.
  [VERIFY current enforcement status — subject to change]

**Parity analysis structure**:

Apply within six benefit **classifications**: (1) inpatient in-network; (2) inpatient
out-of-network; (3) outpatient in-network; (4) outpatient out-of-network; (5) emergency
care; (6) prescription drugs.

Two types of treatment limitations (TLs):

1. **Quantitative Treatment Limitations (QTLs)** — visit limits, day limits, frequency
   limits. QTL parity test: a QTL may apply to MH/SUD benefits in a classification only
   if it applies to **substantially all** (≥ two-thirds by plan payments) medical/surgical
   (M/S) benefits in that classification and does not exceed the **predominant** level
   (applicable to more than half of M/S benefits subject to the limit).

2. **Nonquantitative Treatment Limitations (NQTLs)** — prior authorization, step
   therapy, medical necessity criteria, network admission standards, fail-first protocols,
   out-of-network reimbursement rates, formulary design. Required analysis:
   - Plan must develop and maintain a **written NQTL comparative analysis** demonstrating
     that NQTLs applied to MH/SUD benefits are no more restrictive in design or
     application than comparable NQTLs for M/S benefits in the same classification.
   - Analysis must include factor-by-factor comparison (not a checkbox template).
   - Data collection and outcomes evaluation is required under the 2024 rule (currently
     in enforcement pause — apply pre-2024 standards for current plan years; [VERIFY]).
   - Plans must provide the analysis to DOL, state regulators, or participants on request.

**⟁ CLARIFY** — Has the plan sponsor (not just the TPA or insurer) obtained and reviewed
the NQTL comparative analysis for the current plan year? Self-insured plans relying
entirely on TPA analyses without review are a leading MHPAEA non-compliance pattern.

#### 5e. Health Plan Document and SPD Compliance

- Written plan document: Every group health plan must have one (ERISA § 402).
- SPD: Must be provided within 90 days of participant coverage; updated every 5 years
  (material amendments) or 10 years (otherwise); SMM within 210 days after plan year end
  (or 60 days for material reductions in covered services).
- Claims and appeals procedures: Must comply with ACA internal claims and appeals
  regulations (29 C.F.R. § 2590.715-2719) and external review requirements.
- **Gag clause prohibition attestation** (CAA 2021): Employers must annually attest to
  the DOL/HHS through the HIOS portal that they have not entered gag clauses on price
  and quality data with service providers. [VERIFY current filing deadline]
- **RxDC Reporting** (CAA 2021): Annual pharmacy benefit and health care cost reporting.
  [VERIFY current-year submission deadline and reporting period]
- **Electronic disclosure**: DOL's 2020 final rule (29 C.F.R. § 2520.104b-31) permits
  "notice and access" safe harbor for electronic delivery with required initial paper
  notice, annual availability notification, and paper copy on request.

### Step 6: Retirement Plan Compliance Assessment

**Activate this step if the employer maintains retirement plans.**

Assess in this sequence:

#### 6a. Fiduciary Structure and Governance (ERISA §§ 401–414)

**Core fiduciary duties** (ERISA § 404(a)(1)):

- **Prudence**: "Prudent expert" standard — care, skill, prudence, and diligence of a
  prudent person familiar with such matters. Process standard, not outcome standard.
  _Tibble v. Edison International_, 575 U.S. 523 (2015): ongoing duty to monitor
  (statute of limitations runs from last breach, not initial selection).
- **Loyalty**: Exclusive benefit rule — act solely in the interest of participants
  and beneficiaries.
- **Diversification**: Diversify plan investments to minimize risk of large losses
  (unless clearly prudent not to — e.g., ESOP employer securities within § 407 limits).
- **Plan documents**: Act in accordance with plan documents to the extent consistent
  with ERISA.

**Fiduciary status analysis** — Who is a functional fiduciary?

- ERISA § 3(21)(A): Any person who (i) exercises discretionary authority or control over
  plan management or plan assets, (ii) renders investment advice for compensation, or
  (iii) has discretionary authority or responsibility in plan administration.
- Named fiduciaries, investment committee members, HR personnel with discretion over
  benefit determinations, and recordkeepers with discretionary authority are all potential
  fiduciaries regardless of title.
- **DOL Fiduciary Rule — Current Status (March 2026)**: The 2024 Retirement Security
  Rule (89 Fed. Reg. 32,122, April 25, 2024) was vacated. Two Texas federal district
  courts (N.D. Tex. and E.D. Tex.) enjoined and vacated the rule; the Fifth Circuit
  dismissed the DOL's appeal on November 28, 2025. Final judgments vacating the rule
  were entered in March 2026; the Federal Register published a Notice of Court Vacatur
  on March 20, 2026. **The pre-2024 Five-Part Test** (29 C.F.R. § 2510.3-21 (1975))
  now governs investment advice fiduciary status. [VERIFY — regulatory landscape
  continues to evolve]

**Settlor vs. fiduciary function distinction** (_Lockheed Corp. v. Spink_, 517 U.S. 882
(1996)): Plan design decisions (amending the plan, terminating the plan, changing benefit
levels) are **settlor acts** not subject to ERISA § 404 fiduciary standards. Implementing
those decisions is a fiduciary act. Always characterize the nature of the act before
applying fiduciary analysis.

**Investment committee assessment**:

- Investment Policy Statement (IPS) exists, is current, and is followed?
- Meeting minutes documenting prudent process for each plan year?
- Monitoring log for all investment options — _Tibble_ ongoing duty?
- Service provider selection documentation (RFP process, fee benchmarking)?
- ERISA § 3(38) investment manager delegation vs. § 3(21) co-fiduciary arrangement?

**ERISA § 404(c) compliance** (29 C.F.R. § 2550.404c-1):
To shift investment loss risk to participants for their own choices, the plan must:

- Offer at least three diversified investment alternatives;
- Provide the ability to change investments at least quarterly;
- Provide required disclosures (prospectuses, fund descriptions, financial statements);
- Allow participant direction of investments with sufficient investment education.

**ERISA § 412 fidelity bond**: Each plan official handling plan funds must be bonded.
Minimum = 10% of prior-year funds handled; minimum $1,000; maximum $500,000 ($1,000,000
for plans holding employer securities). Bond is a mandatory legal requirement.

#### 6b. Prohibited Transactions (ERISA § 406; IRC § 4975)

Assess transactions between the plan and "parties in interest" (§ 3(14)) or "disqualified
persons" (IRC § 4975(e)(2)). Prohibited transactions are per se violations — fair market
value terms do not prevent a PT if the structural prohibition applies.

**Category A PTs** (§ 406(a)): Sale/exchange; loans/credit extensions; provision of
goods, services, or facilities; transfer or use of plan assets; acquisition of employer
securities/real property above § 407 limits.

**Category B PTs** (§ 406(b)): Fiduciary self-dealing; acting on behalf of an adverse
party; receiving consideration from a third party in connection with a plan transaction.

**Statutory exemptions** (§ 408 / IRC § 4975(d)) — self-executing, no DOL application
needed:

- § 408(b)(1): Loans to participants (plan loan program must satisfy § 408(b)(1) and
  29 C.F.R. § 2550.408b-1)
- § 408(b)(2): Reasonable contracts for necessary services — if no more than reasonable
  compensation, no interest in the transaction adverse to the plan, and services are
  necessary. **408(b)(2) disclosure obligation**: Covered plan service providers (CSPs)
  receiving $1,000+ annually must disclose direct and indirect compensation before
  contract execution (29 C.F.R. § 2550.408b-2).
- § 408(e): Acquisition of employer securities/real property by eligible individual account
  plans within § 407 limits

**Class PTEs** (DOL-issued, self-executing if conditions met):

- PTE 84-14 (QPAM exemption): Qualified professional asset manager
- PTE 2020-02 (investment advice): As originally issued December 18, 2020, after the
  2024 amendment was vacated. Impartial Conduct Standards apply to investment advice
  fiduciaries under the restored Five-Part Test.
- PTE 96-23 (INHAM): In-house asset manager

**Excise taxes** (IRC § 4975):

- Initial tax: **15%** of the "amount involved" per year during the taxable period
- Correction tax: **100%** if not corrected after IRS notice
- _Cunningham v. Cornell University_, 604 U.S. \_\_\_ (April 17, 2025): The Supreme Court
  held unanimously that § 408 exemptions are **affirmative defenses** that defendants must
  plead and prove — plaintiffs need only allege the elements of § 406. This substantially
  lowers the pleading bar and increases litigation exposure.

**Late deferral deposits** — Most-audited PT in DOL audits:

- Employee 401(k) deferrals must be deposited "as soon as they can reasonably be
  segregated from the employer's general assets" (29 C.F.R. § 2510.3-102).
- Safe harbor for small plans (< 100 participants): 7 business days from pay date.
- Each late deposit is a prohibited transaction (loan from plan to employer) — not a
  minor administrative error.
- Correction: DOL Voluntary Fiduciary Correction Program (VFCP), including lost-earnings
  calculation using DOL VFCP online calculator. VFCP eliminates § 502(l) civil penalties
  upon approval.

**⟁ CLARIFY** — For each of the past three plan years, has the employer compared the
**earliest date** it could have segregated employee deferrals from general assets against
the **actual deposit date** for each payroll period? If not, this analysis is required
before concluding the PT assessment.

#### 6c. Qualification Requirements — 401(k) Plans

**IRC §§ 401(a), 401(k), 401(m), 402(g), 415**

**Nondiscrimination testing**:

- **ADP test**: Elective deferrals of NHCEs cap HCE deferrals (1.25× or 2×/2% rules)
  (IRC § 401(k)(3))
- **ACP test**: Employer matching contributions and after-tax contributions (IRC § 401(m))
- **Coverage test**: IRC § 410(b) — ratio percentage or average benefits test
- **General nondiscrimination**: IRC § 401(a)(4) — benefits, rights, and features

**Safe harbor design (avoids ADP/ACP testing)**:

- _Traditional safe harbor_: 100% match on first 3% of compensation + 50% match on
  next 2%; OR 3% nonelective contribution. Requires 30–90 day advance notice.
- _QACA (Qualified Automatic Contribution Arrangement)_: Auto-enroll at 3% with
  escalation to 10–15%; 100% match on first 1% + 50% match on next 5%.

**Contribution limits** [VERIFY current year via IRS annual notice]:
| Limit | 2025 | 2026 |
|-------|------|------|
| Elective deferral (IRC § 402(g)) | $23,500 | $24,500 |
| Age 50+ catch-up (IRC § 414(v)) | $7,500 | $8,000 |
| Age 60–63 enhanced catch-up (SECURE 2.0 § 109) | $11,250 | $11,250 |
| Annual additions (IRC § 415(c)) | $70,000 | $72,000 |
| Compensation cap (IRC § 401(a)(17)) | $345,000 | $350,000 |

**Top-heavy analysis** (IRC § 416):

- Plan is top-heavy if key employees hold > 60% of plan balances.
- Required minimum employer contribution for non-key employees: **3% of compensation**
  (or the percentage contributed for the highest-key-employee, if less).
- Accelerated vesting: 3-year cliff or 2–6-year graded.

**Vesting — SECURE 2.0 § 110**:

- Employer matching contributions: 2-year cliff vesting for contributions in plan years
  beginning after December 31, 2023 (reduced from 3-year cliff).
- Graded schedule: 2–6-year (unchanged).

**Long-Term Part-Time (LTPT) Employees — SECURE 2.0 § 125**:

- Employees with **2 consecutive years of 500+ hours** must be eligible to make elective
  deferrals beginning with plan years starting after December 31, 2024.
  (SECURE Act 1.0 required 3 years; SECURE 2.0 reduced to 2.)
- LTPT employees need not receive employer matching contributions.

**Hardship distributions**: 2019 final regulations (Treas. Reg. § 1.401(k)-1(d)(3))
eliminated the 6-month contribution suspension requirement and expanded safe harbor
expense categories. Plans still applying the suspension or using pre-2019 expense
categories are operating outside current law — a qualification failure.

**Required Minimum Distributions (RMDs)**:

- SECURE Act 2.0: RMD age is 73 for individuals turning 73 after December 31, 2022;
  75 for individuals turning 75 after December 31, 2032.
- SECURE Act 2.0 also eliminated lifetime RMDs for Roth accounts in DC plans.

#### 6d. SECURE 2.0 Act Implementation Status

**⟁ CLARIFY — SECURE 2.0 Mandatory Provisions**

SECURE 2.0 (P.L. 117-328, December 29, 2022) has 90+ provisions. Confirm which are
operationally adopted and which require plan amendment:

| Provision                                        | Effective Date                          | Plan Applies? | Operationally Adopted? | Document Amended? |
| ------------------------------------------------ | --------------------------------------- | ------------- | ---------------------- | ----------------- |
| Mandatory auto-enrollment (§ 101, IRC § 414A)    | Plan years after 12/31/2024             | Yes/No        | Yes/No                 | Yes/No            |
| LTPT 2-year rule (§ 125)                         | Plan years after 12/31/2024             | Yes/No        | Yes/No                 | Yes/No            |
| RMD age to 73 (§ 107)                            | Individuals turning 73 after 12/31/2022 | Yes/No        | Yes/No                 | Yes/No            |
| Roth catch-up ≥$145K wages (§ 603)               | January 1, 2026 [IRS Notice 2023-75]    | Yes/No        | By 2026                | By 2026           |
| Student loan matching (§ 127)                    | Plan years after 12/31/2023             | Yes/No        | Yes/No                 | Yes/No            |
| Emergency savings accounts (§ 127)               | Plan years after 12/31/2023             | Yes/No        | Yes/No                 | Yes/No            |
| Enhanced catch-up age 60–63 (§ 109)              | Plan years after 12/31/2024             | Yes/No        | Yes/No                 | Yes/No            |
| Emergency personal expense distributions (§ 115) | Plan years after 12/31/2023             | Yes/No        | Yes/No                 | Yes/No            |
| Domestic abuse distributions (§ 314)             | Plan years after 12/31/2023             | Yes/No        | Yes/No                 | Yes/No            |

**Amendment deadline**: Most qualified plan SECURE 2.0 amendments must be adopted by
**December 31, 2026** for calendar-year plans (IRS Notice 2025-19). Plans must operate
in compliance with each provision as of its effective date even before formal amendment.
SIMPLE IRA and IRA amendments: December 31, 2027 (IRS Notice 2026-9). [VERIFY]

**EPCRS under SECURE 2.0**: SECURE 2.0 § 305 expanded self-correction for **Eligible
Inadvertent Failures (EIFs)** — failures despite adequate procedures and controls have
no time limit on self-correction if discovered before IRS examination (IRS Notice 2023-43
provides interim guidance). Pending formal update to Rev. Proc. 2021-30 (not yet
published as of early 2026; Notice 2023-43 remains operative). [VERIFY]

#### 6e. Qualification Requirements — 403(b) Plans

**IRC § 403(b); Treas. Reg. § 1.403(b)**

- **Universal availability rule**: All employees must be permitted to make elective
  deferrals (with narrow exceptions — students, non-resident aliens, employees expected
  to work < 20 hours/week, certain church plan employees).
- **Written plan document**: Required since 2009 for non-governmental 403(b) plans.
- **15-year catch-up**: Up to $3,000/year additional for employees with 15+ years of
  service with qualifying organizations (IRC § 402(g)(7)) — separate from age-based
  catch-up; applies to eligible employers (schools, hospitals, churches, home health
  agencies, certain tax-exempt organizations).
- **Same contribution limits** as 401(k): [VERIFY current year — see Step 6c table]
- **Nondiscrimination testing**: 403(b) plans are generally not subject to ADP/ACP
  testing for elective deferrals but are subject to IRC § 403(b)(12)(A)(ii) (universal
  availability is a nondiscrimination substitute). Employer contributions remain subject
  to coverage and nondiscrimination testing.

#### 6f. Qualification Requirements — Defined Benefit Plans

**IRC §§ 412, 415(b); ERISA §§ 302–305; PBGC Title IV**

- **Minimum funding standards** (IRC § 412/ERISA § 302): Plan must satisfy minimum
  required contribution each year. Funding shortfall triggers additional contribution
  requirements and benefit accrual/payment restrictions.
- **Actuarial certification** (ERISA § 302(d)(9)): Single-employer plans must be
  certified by an enrolled actuary annually. [Refer all funding calculations to an
  enrolled actuary — outside this skill's scope]
- **PBGC premiums** [VERIFY current year via PBGC annual premium rate notice]:
  - Flat-rate (per participant): 2025 = $101; 2026 = [VERIFY]
  - Variable-rate (per $1,000 of unfunded vested benefits): 2025 = $52
  - Cap on variable-rate per-participant: [VERIFY]
- **Benefit limit** (IRC § 415(b)): Lower of dollar limit ($275,000 in 2025; [VERIFY])
  or 100% of participant's average compensation for high-3 years.
- **Mortality tables**: Rev. Proc. 2023-29 updated mortality improvement scale for
  funding purposes effective plan years beginning January 1, 2024. [VERIFY for
  subsequent updates]
- **PBGC reportable events** (ERISA § 4043): Plan must notify PBGC of certain events
  (active participant reductions, missed contributions, extraordinary dividends, etc.)
  within prescribed timeframes.

#### 6g. Form 5500 Compliance (ERISA § 104; 29 C.F.R. § 2520.103)

**Filing requirements**:

- **Large plans** (100+ participants at beginning of plan year): Full Form 5500 with
  all required schedules and **independent qualified public accountant (IQPA) audit**.
- **Small plans** (< 100 participants): Form 5500-SF; no audit required for most small
  plans.
- **80-120 rule**: A plan with 80–120 participants may continue filing in the same
  category as the prior year.

**Filing deadline**: 7 months after plan year end.

- Calendar year plans: July 31.
- Automatic 2.5-month extension: File DOL Form 5558 by the regular due date → October 15.

**Key schedules**:

- **Schedule A**: Insurance contract information
- **Schedule C**: Service providers receiving $5,000+ (including indirect compensation)
- **Schedule H**: Financial information for large plans (must reconcile to trust statements)
- **Schedule I**: Financial information for small plans
- **Schedule R**: Retirement plan information (actuarial data, RMD, coverage)
- **Schedule SB**: Single-employer DB actuarial certification
- **Schedule MB**: Multiemployer DB actuarial certification

**Penalties**:

- ERISA § 502(c)(2): $250/day up to $150,000 per plan year
- Plus separate IRS penalty for late/non-filing of Form 5500 under IRC § 6058:
  $250/day up to $150,000

**DFVCP (Delinquent Filer Voluntary Compliance Program) — reduced penalty caps**:

- Small plans: $10/day accrual; capped at **$750 per late filing** / $4,000 per plan
  regardless of number of late filings submitted together
- Large plans: $10/day accrual; capped at **$2,000 per late filing** / $4,000 per plan
  [Per Federal Register update December 31, 2025]
- DFVCP eligibility: Must apply before a DOL investigation commences.
- EFAST2 electronic filing mandatory for all Form 5500 submissions.

### Step 7: Excise Tax and Penalty Exposure Quantification

Estimate penalty and excise tax exposure for each finding. Use the following reference:

| Deficiency                         | Authority                       | Rate / Amount                                                                |
| ---------------------------------- | ------------------------------- | ---------------------------------------------------------------------------- |
| Late deferral deposits             | IRC § 4975(a)/(b) + ERISA § 409 | 15% of amount involved/year; 100% if not corrected                           |
| COBRA notice failure               | IRC § 4980B                     | $100/day/qualified beneficiary; min $2,500; min $15,000 (egregious) [VERIFY] |
| ACA 4980H(a) — no offer            | IRC § 4980H(a)                  | 2026: $3,340/FTE annually (minus 30) [VERIFY]                                |
| ACA 4980H(b) — unaffordable/not MV | IRC § 4980H(b)                  | 2026: $5,010/FTE receiving marketplace credit [VERIFY]                       |
| HIPAA/ACA group health violation   | IRC § 4980D                     | $100/day/individual; min $2,500/participant; max $500,000/year [VERIFY]      |
| Form 5500 late filing (DOL)        | ERISA § 502(c)(2)               | $250/day; max $150,000/plan year                                             |
| Form 5500 late filing (IRS)        | IRC § 6058                      | $250/day; max $150,000/plan year                                             |
| SPD/document failure               | ERISA § 502(c)(1)               | Up to $110/day [VERIFY — indexed]                                            |
| PT excise (initial)                | IRC § 4975(a)                   | 15% of amount involved per year                                              |
| PT excise (correction)             | IRC § 4975(b)                   | 100% if not corrected                                                        |
| ERISA § 502(l) civil penalty       | ERISA § 502(l)                  | 20% of applicable recovery amount                                            |

**Important**: Always flag exposure amounts with [VERIFY current indexed amount] —
IRS adjusts many penalties annually for inflation under 29 C.F.R. Part 2575.

### Step 8: Correction and Remediation Pathway Analysis

For each finding, identify the applicable correction vehicle:

| Deficiency Type                      | Correction Vehicle                               | Key Conditions                                                                                                                              |
| ------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Late deferral deposits               | DOL VFCP                                         | Voluntary; before DOL investigation; lost-earnings calculation required                                                                     |
| Qualification failures (operational) | EPCRS-SCP (self-correction)                      | Within SCP eligibility period; "significant" failures: substantially complete within 3 years; EIFs: no time limit if before IRS examination |
| Qualification failures (document)    | EPCRS-VCP or Audit CAP                           | VCP for pre-audit voluntary correction; Audit CAP if in examination                                                                         |
| Late Form 5500 filings               | DFVCP                                            | Before DOL investigation; reduced penalty caps as above                                                                                     |
| COBRA notice failures                | Retroactive correction + belated election rights | Cannot eliminate already-accrued § 4980B excise tax                                                                                         |
| MHPAEA failures                      | Plan amendment + prospective compliance          | No formal correction program; potential litigation exposure                                                                                 |
| PT — other categories                | VFCP (if eligible transaction type)              | See VFCP schedule of eligible transactions                                                                                                  |
| Fiduciary breach                     | ERISA § 409 personal liability + DOL settlement  | Counsel required; ERISA § 502(l) 20% civil penalty on recovery                                                                              |

**EPCRS resources**:

- Rev. Proc. 2021-30 governs EPCRS (SCP, VCP, Audit CAP)
- SECURE 2.0 § 305 expanded SCP for EIFs (IRS Notice 2023-43 interim guidance)
- IRS EPCRS fee schedule and correction methodologies at Rev. Proc. 2021-30
- DOL VFCP online calculator for lost-earnings computation

### Step 9: Fiduciary Personal Liability Assessment

For any finding with fiduciary liability implications:

- **Map the functional fiduciaries**: Who actually exercises discretion? Not just named
  fiduciaries on the plan document.
- **Co-fiduciary liability** (ERISA § 405(a)): A fiduciary is liable for a co-fiduciary's
  breach if: (i) they participate in or undertake to conceal the breach; (ii) by their
  own breach they enable the breach; or (iii) they have knowledge of the breach and do
  not make reasonable efforts to remedy it.
- **ERISA § 409 remedies**: Make-whole damages (restore losses to the plan), disgorge
  profits, "other equitable or remedial relief" — plus the DOL's § 502(l) 20% civil
  penalty on any "applicable recovery amount."
- **Plan-paid indemnification prohibited**: ERISA § 410 prohibits the plan from paying
  for insurance that indemnifies fiduciaries against fiduciary breaches. Personal
  fiduciary liability insurance must be personally paid or employer-paid (not plan-paid).
- **Fiduciary liability insurance vs. fidelity bond**: The § 412 fidelity bond (mandatory)
  protects the plan against dishonesty of plan officials. Fiduciary liability insurance
  (best practice) covers liability for fiduciary breaches and is purchased by the employer.

### Step 10: Annual Compliance Calendar Build

For ongoing compliance, document the following calendar items:

**Quarterly / Ongoing**:

- Employee 401(k) deferral deposit deadlines (7 business days for small plans;
  earliest practicable date for large plans — compare each payroll period)
- COBRA qualifying event notification tracking (30-day employer → administrator chain)
- QDRO receipt, acknowledgment, and determination process (ERISA § 206(d)(3))

**Annual — Retirement Plans**:

- ADP/ACP nondiscrimination testing completion and correction deadlines
  (March 15 following plan year end for standard correction method; December 31 for
  excess contributions returned within 2.5 months of plan year end)
- Top-heavy determination and minimum contribution calculation
- IRC § 415 limit monitoring per participant
- ERISA § 412 fidelity bond renewal (verify adequacy against prior-year funds handled)
- Form 5500 filing deadline (July 31 for calendar-year; October 15 with extension)
- Investment committee meeting (at least annually; quarterly recommended)
- Investment lineup review against IPS (Tibble ongoing monitoring obligation)
- 404a-5 participant fee disclosure update (14-month rule)
- SECURE 2.0 provision effective-date tracking

**Annual — Health and Welfare Plans**:

- ACA measurement period close and stability period commencement (variable-hour tracking)
- ACA affordability percentage update (monitor October IRS Revenue Procedure)
- Forms 1094-C/1095-C filing and employee furnishing deadlines (March 31 / January 31)
- HIPAA wellness program reward cap verification
- MHPAEA NQTL comparative analysis update (before each plan year) [subject to current
  enforcement status — VERIFY]
- CAA gag clause prohibition attestation (annual HIOS portal filing)
- RxDC pharmacy reporting (annual) [VERIFY current deadline]
- SPD/SMM updates for plan amendments during prior year

**October/November — Monitor IRS Annual Notice**:

- Updated indexed limits for IRC §§ 402(g), 415(c), 401(a)(17), 414(q), 416(i), 4980H
- Updated PBGC premium rates (via PBGC annual notice)
- Updated ACA affordability percentage

### Step 11: Assess Controlled Group and Special Structural Issues

**Controlled group and affiliated service group** (IRC § 414(b), (c), (m), (o)):

- All members of a controlled group (parent-subsidiary or brother-sister under IRC §1563)
  are treated as a single employer for nondiscrimination testing, top-heavy, coverage,
  and ACA ALE determination.
- Affiliated service groups (management companies, A-B organizations) are similarly
  aggregated.
- M&A transactions: Acquirer must immediately reanalyze ALE status, controlled group
  membership, and plan nondiscrimination testing post-closing.

**Leased employees** (IRC § 414(n)):

- A leased employee working primarily for the recipient employer on a substantially
  full-time basis under an agreement with a leasing organization must be treated as the
  recipient's employee for certain qualified plan testing purposes.

**Multiple Employer Plans (MEPs) / Pooled Employer Plans (PEPs)**:

- SECURE Act 2.0 expanded PEP availability. Assess pooled plan provider (PPP)
  obligations vs. participating employer obligations separately.

**⟁ CLARIFY** — If the employer has undergone an acquisition, merger, divestiture, or
ownership structure change in the past 3 plan years, pause here and confirm the controlled
group composition before completing nondiscrimination and ACA analyses.

### Step 12: Generate Compliance Assessment Report

Compile all findings into the structured output template below. Apply the Glass Box audit
trail for traceability.

---

## Severity and Status Classification

Apply the four-tier system, calibrated to ERISA/IRC enforcement reality:

### CRITICAL — Correct Immediately (Active or Imminent Enforcement Risk)

**Indicators**: Plan disqualification exposure; active DOL or IRS audit; uncorrected
material prohibited transaction; personal fiduciary liability imminent; participant harm
occurring now; DFVCP or VFCP or EPCRS window at risk of closing.

**Examples**:

- Late deferral deposits continuing for 3+ payroll periods with no VFCP filing and DOL
  investigation imminent
- Uncorrected PT after DOL or IRS notice (100% correction tax exposure under § 4975(b))
- Form 5500 unfiled for 2+ years without DFVCP protection; IRS penalty accruing
- ADP/ACP testing failure with correction window closing within 30 days
- Self-insured plan operating without a written plan document
- MHPAEA NQTL analysis not in existence when DOL has made a formal document request
- ERISA § 412 fidelity bond entirely absent — per se violation

**Output signal**: ⛔ CRITICAL — Immediate remediation required. Engage ERISA counsel
within 5 business days.

### HIGH — Correct Within 60 Days (Material Exposure; No Active Investigation)

**Indicators**: Significant excise tax or penalty exposure; qualification risk; correctable
but time-sensitive; participant claims risk; personal fiduciary liability exposure not yet
triggered but building.

**Examples**:

- Late deferral deposits correctable through VFCP within remaining window
- COBRA election notices not timely sent; IRC § 4980B accruing per qualified beneficiary
- SPD not updated for plan amendments adopted 12+ months ago
- ACA Forms 1094-C/1095-C not filed; IRS Letter 226-J unanswered
- Investment policy statement not reviewed in 3+ years; no documented _Tibble_ monitoring
- ERISA § 408(b)(2) disclosures received from CSPs but never reviewed or documented
- ERISA § 412 fidelity bond insufficient for current plan size

**Output signal**: 🟠 HIGH — Remediation plan required within 60 days.

### MEDIUM — Address This Plan Year

**Indicators**: Best-practice gaps; moderate exposure if left unaddressed; correction
available without penalty; not currently on DOL/IRS radar.

**Examples**:

- SECURE 2.0 provisions operationally adopted but plan document not yet formally amended
  (amendment deadline December 31, 2026)
- Named fiduciaries not trained on ERISA fiduciary standards in past 2 years
- Form 5500 Schedule C indirect compensation disclosures not verified against actual
  service provider arrangements
- No documented investment committee meeting minutes for prior plan year
- Wellness program not formally analyzed for HIPAA participatory vs. health-contingent
  classification
- MHPAEA NQTL comparative analysis received from TPA but never reviewed by the plan
  sponsor

**Output signal**: 🟡 MEDIUM — Include in annual compliance calendar; resolve before
next plan year end.

### LOW — Monitor and Document

**Indicators**: Informational; emerging regulatory risk; no current violation; policy or
documentation should be improved.

**Examples**:

- DOL Fiduciary Rule regulatory status — monitor for replacement rulemaking
- MHPAEA 2024 Final Rule enforcement pause — track litigation and regulatory developments
- CAA 2021 RxDC reporting filed but data quality not independently verified
- Potential church plan status re-analysis — document analysis even if conclusion is
  ERISA-covered

**Output signal**: 🔵 LOW — Monitor; document current position; include in next annual
review.

---

## Quality Frameworks

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Fail any gate → revise before
delivery.

| Gate                      | Rule                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Fail Action                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| **Jurisdiction**          | Every finding precisely attributes the governing authority: DOL/EBSA for Title I (fiduciary, reporting, disclosure); IRS for qualification and excise taxes; PBGC for DB termination. Never conflate ERISA § 404 (fiduciary duty) with IRC § 404 (deductibility), or ERISA § 401 (coverage) with IRC § 401 (qualified plans). Every citation must identify "ERISA §" or "IRC §" explicitly.                                                                  | Correct attribution and re-state citation   |
| **Code accuracy**         | ERISA section numbers track the public law (29 U.S.C. Chapter 18). IRC section numbers track the Internal Revenue Code (26 U.S.C.). The two numbering schemes diverge — always specify the statute.                                                                                                                                                                                                                                                          | Rewrite with correct statute identification |
| **Source tier**           | Classify citations by binding force: (1) Statutory text (binding); (2) Final regulations in 29 C.F.R. / 26 C.F.R. (binding); (3) Proposed regulations (not final — mark "[PROPOSED — NOT FINAL]"); (4) DOL FABs, Information Letters, Advisory Opinions — mark "[DOL GUIDANCE — not regulation]"; (5) IRS Rev. Rulings, Rev. Procs., Notices — mark "[IRS GUIDANCE]". Adjust confidence level to match source tier.                                          | Add tier marker; adjust confidence          |
| **Currency — thresholds** | Every dollar-denominated threshold (§§ 402(g), 415(c), 401(a)(17), 414(q), 416(i), 4980H(a)/(b), ACA affordability %, PBGC premiums, 4980B, 4980D) must be flagged: `[THRESHOLD — verify current year amount via IRS Notice / PBGC premium notice]`. These change annually. Never state a threshold as current without this flag unless the current plan year has been confirmed and verified.                                                               | Replace bare threshold with the flag        |
| **Confidence / finality** | Uncertainty is explicit. Proposed rules ≠ final rules. Sub-regulatory guidance ≠ regulations. Novel interpretive questions (MHPAEA NQTL analysis methodology, crypto in plan assets, novel investment structures) are flagged "[INTERPRETIVE — professional judgment required; consult ERISA counsel]". The DOL Fiduciary Rule status is always noted with "[VERIFY current regulatory status — rule has been vacated; monitor for replacement rulemaking]". | Add qualifier and basis for uncertainty     |

### Self-Interrogation for High-Severity Findings

For any finding classified **CRITICAL** or **HIGH** (personal fiduciary liability, plan
disqualification risk, active excise tax, participant harm), apply this 3-pass review:

**Pass 1 — Liability Attribution and Penalty Chain**

Who bears the legal consequence?

- **Fiduciary personally** (ERISA § 409 — make-whole damages, profit disgorgement,
  § 502(l) 20% civil penalty, possible removal)?
- **Plan as entity** (trust losses)?
- **Employer/plan sponsor** (excise tax under IRC § 4975 or § 4980H)?
- **Service provider / party in interest** (IRC § 4975 excise tax falls on the
  disqualified person, not the plan)?

State the liability chain explicitly. Does the finding create personal exposure for
named fiduciaries? Is the consequence regulatory/civil (ERISA enforcement), tax (IRS
enforcement), or both? Is there a § 502(l) civil penalty overlay?

**Pass 2 — Correction Programs and Mitigation**

Is voluntary correction available and does it materially change urgency?

- **VFCP eligibility**: Is the specific transaction type listed in the VFCP schedule of
  eligible transactions? Verify — not all PTs are VFCP-eligible.
- **EPCRS eligibility**: Is this an operational failure (SCP/VCP) or a plan document
  failure (VCP/Audit CAP)? Is the plan in an IRS examination? SCP eliminates the VCP
  submission requirement for EIFs under SECURE 2.0 § 305 (no time limit if before exam).
- **DFVCP**: Is this a Form 5500 delinquency and is the plan not yet under DOL
  investigation? Confirm DFVCP caps apply.
- **Correction availability → severity adjustment**: If correction is immediately available
  and eliminates penalty exposure, reduce urgency framing accordingly and state:
  "Correct via [VFCP/EPCRS-SCP/DFVCP] within [timeframe] to eliminate penalty exposure."

**Pass 3 — Challenge: Strongest Counter-Position**

What is the strongest argument that this finding is not a violation, or severity is lower?

- **Settlor function?** Could the challenged action be an employer plan design decision
  (settlor act) rather than a fiduciary implementation act? (_Lockheed v. Spink_)
- **Statutory exemption?** Is there a § 408 or IRC § 4975(d) statutory exemption that
  applies without requiring a PTE? Distinguish self-executing statutory exemptions from
  class PTEs (self-executing if conditions met) from individual PTEs (DOL application
  required).
- **Document vs. operational failure?** Characterize correctly — different EPCRS tracks
  and different amendment mechanics apply to each.
- **Anti-cutback rule?** Could a proposed plan amendment correcting the failure itself
  violate ERISA § 204(g)/IRC § 411(d)(6) by reducing an accrued benefit or eliminating
  an optional form?

Mark the audit trail: `self_interrogation_result: "PASS"` (finding confirmed) or
`"REVISED"` (classification/severity adjusted, with explanation).

### Confidence Scoring

| Level                  | Range     | Meaning                                                               | ERISA Example                                                                                                                                                                                                                             | Action                                                                |
| ---------------------- | --------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Definite**           | 0.95–1.0  | Settled statutory rule or final regulation                            | COBRA election notice must be sent within 14 days of plan administrator receiving QE notice (29 C.F.R. § 2590.606-4(b)(2)); 401(k) plans must satisfy ADP testing or qualify as safe harbor                                               | State with confidence; cite the regulation                            |
| **High**               | 0.80–0.94 | Strong regulatory basis; minor interpretation question on application | Whether a specific investment lineup satisfies § 404(c) given particular disclosure and control facts; whether a service provider fee arrangement is "reasonable" under § 408(b)(2) given plan size and market comparables                | State with brief caveat on fact-specific elements                     |
| **Probable**           | 0.60–0.79 | Good authority; reasonable practitioners could differ                 | Whether a particular custodial arrangement between the plan and an affiliated entity is a PT under § 406(b) absent a clear exemption; whether contribution timing satisfies "earliest practicable" standard given specific payroll system | State with full reasoning; contra-arguments; recommend ERISA counsel  |
| **Possible**           | 0.40–0.59 | Genuinely uncertain; active regulatory change; undeveloped facts      | Fiduciary status of a financial institution under the restored Five-Part Test; MHPAEA NQTL comparability analysis for a specific utilization management protocol given enforcement pause                                                  | Flag for ERISA attorney review; do not state as compliance conclusion |
| **Unlikely/Uncertain** | 0.0–0.39  | Novel question; conflicting or absent authority; speculative          | Novel cryptocurrency investment prudence analysis under ERISA § 404 given DOL 2022 supplemental release and absence of subsequent definitive guidance                                                                                     | Do not assert a position; state "[UNCERTAIN — consult ERISA counsel]" |

---

## ERISA-Specific Guardrails

Surface these warnings proactively when the relevant facts are present:

**G-1: Small/large plan bifurcation.** Plans < 100 participants have different rules:
7-business-day safe harbor for deferral deposits; Form 5500-SF option; DFVCP small-plan
penalty caps. Do not apply large-plan standards to small plans or vice versa.

**G-2: Church plans and governmental plans.** ERISA § 3(32)/(33) and § 4(b)(1)/(2)
exemptions can eliminate Title I fiduciary, reporting, and disclosure requirements
entirely. Confirm ERISA coverage status before any Title I analysis — church-affiliated
hospitals (_Advocate Health Care_), state universities, tribal governments, and
governmental contractors each have distinct treatment.

**G-3: Individual account vs. defined benefit.** DB plans require minimum funding (IRC
§ 412/ERISA § 302), PBGC insurance, and enrolled actuary certification — none of which
apply to DC plans. Apply DB-specific requirements only to DB plans.

**G-4: Controlled group and affiliated service group aggregation.** All § 414(b)/(c)/
(m)/(o) members are treated as a single employer for nondiscrimination testing, coverage,
top-heavy, and ACA ALE determination. Always ask whether the employer is part of a
controlled group before completing these analyses.

**G-5: QDRO compliance.** QDROs trigger non-delegable, time-bound obligations (ERISA
§ 206(d)(3)/IRC § 414(p)): acknowledge receipt, notify participant and alternate payees,
determine qualification within 18 months, segregate alternate payee's share pending
determination. Plans must have written QDRO procedures.

**G-6: Fiduciary vs. settlor function.** Not every employer action is a fiduciary act.
Settlor functions (amending, terminating, design changes) are not subject to ERISA § 404.
Always characterize the nature of the act before applying fiduciary analysis.

**G-7: Plan document vs. operational compliance.** These are distinct dimensions:
(1) plan document compliance — the document itself satisfies statutory requirements;
(2) operational compliance — the plan is operated according to its terms. Each type has
different EPCRS correction mechanics and amendment procedures.

**G-8: Form 5500 — DFVCP availability before penalty assessment.** Before stating full
§ 502(c)(2) exposure, always assess whether DFVCP eligibility applies and compute the
capped penalty. Full statutory penalty ($250/day, max $150,000) applies only if DFVCP is
unavailable (because a DOL investigation has commenced) or not used.

**G-9: Multiemployer plan distinctions.** Multiemployer plans (union trust funds) operate
under additional ERISA provisions including withdrawal liability (§§ 4201–4225), zone
status funding, joint board governance, and distinct PBGC multiemployer insurance rules.
Do not apply single-employer DB rules to multiemployer plans.

**G-10: ERISA preemption scope.** ERISA § 514(a) broadly preempts state laws relating to
employee benefit plans, with a savings clause for state insurance regulation (§ 514(b)(2)
(A)) and a deemer clause preventing self-insured plans from being deemed insurers
(§ 514(b)(2)(B)). Self-insured and fully insured plans have different state law exposure —
flag this when state health mandates, surprise billing laws, or mental health parity laws
may apply.

---

## Anti-Patterns

What NOT to do in ERISA compliance assessment and practice:

1. **Treating the recordkeeper as the fiduciary.** Recordkeepers typically disclaim
   fiduciary status entirely. The employer/plan sponsor is the plan administrator and
   investment fiduciary unless formally and validly delegated in writing under the plan
   document. "Our recordkeeper handles it" is not a defense.

2. **Late deferral deposits as administrative oversight.** Each late deposit is a
   prohibited transaction — a loan from the plan to the employer — subject to IRC § 4975
   excise taxes and requiring VFCP correction with lost-earnings payment. Payroll
   "timing issues" are legally material.

3. **Assuming § 404(c) protection applies automatically.** Section 404(c) requires active
   compliance with every element of 29 C.F.R. § 2550.404c-1 (3 diversified options,
   90-day frequency, required disclosures, participant control). Non-compliance means the
   plan sponsor remains liable for participant investment losses regardless of participant
   choice.

4. **Delegation without monitoring.** ERISA § 405(c) permits delegation, but the
   delegating fiduciary retains a duty to monitor the delegate. Co-fiduciary liability
   under § 405(a) applies when a breach is known and not cured. "We hired a consultant"
   is not a defense when the consultant's misconduct was discoverable.

5. **MHPAEA NQTL checklist analysis.** A template NQTL analysis that lists factors
   without substantive factor-by-factor comparison of MH/SUD and M/S benefits in the
   same classification is insufficient. Self-insured plan sponsors must obtain and review
   the TPA's analysis — they cannot merely rely on TPA representations.

6. **Retroactive plan amendments that violate the anti-cutback rule.** ERISA § 204(g)
   and IRC § 411(d)(6) prohibit amendments reducing accrued benefits or eliminating
   optional forms of benefit. Attempting to "clean up" distribution options that should
   never have been offered can create a more serious qualification failure than the
   original error.

7. **Hardship distribution procedures frozen in 2018.** The 2019 final regulations
   eliminated the 6-month contribution suspension requirement and expanded safe harbor
   expense categories. Plans still applying the suspension are operating outside current
   law — a qualification failure correctable through EPCRS but commonly discovered only
   in audits.

8. **The "we have a plan document" defense without operational verification.** DOL
   auditors compare plan document terms against payroll records. A plan that says
   "compensation" includes bonuses but has never included bonuses in deferral calculations
   has an operational failure. The plan document is only the starting point.

9. **SPD silence on subrogation interpreted as waiver.** Self-insured plans need
   aggressive and clearly drafted subrogation and reimbursement clauses in both the plan
   document and SPD. Courts may deny unarticulated subrogation rights.

10. **COBRA employer size miscounted.** The 20-employee test counts employees on each
    working day in each of 20+ calendar weeks in the current or preceding year — not a
    snapshot headcount. Employers near the 20-employee boundary frequently miscalculate
    using snapshot counts.

11. **Leased employees and the § 414(n) trap.** Leased employees working primarily for
    the recipient employer on a substantially full-time basis must be treated as the
    recipient's employees for certain qualified plan testing purposes. PEO and staffing
    arrangements frequently ignore this, causing nondiscrimination test failures.

12. **Cafeteria plan § 125 election changes outside permitted events.** Allowing mid-year
    election changes for events not listed in the plan document — even to accommodate
    employees — is a § 125 qualification failure that renders all benefits taxable to all
    participants.

13. **Plan disqualification as remote risk.** A disqualified 401(k) causes all accrued
    benefits to become immediately taxable to all participants, the trust to lose
    tax-exempt status, and prior employer deductions to be potentially reversed. EPCRS
    audit CAP settlements can run into millions of dollars. The SCP self-correction window
    is often missed because failures are not discovered until an IRS examination.

14. **ACA aggregation errors in M&A.** Acquirers must immediately reanalyze ALE status
    post-closing. ACA compliance is a Day 1 issue, not a Day 2 integration item. IRS has
    issued limited transition relief, but it must be specifically identified and applied.

15. **Fiduciary liability insurance purchased by the plan.** ERISA § 410 prohibits the
    plan from paying for insurance that indemnifies fiduciaries against fiduciary breaches.
    Fiduciary liability insurance must be employer-paid or personally paid, not plan-paid.
    The § 412 fidelity bond (mandatory) is distinct — protects the plan against dishonesty
    and may be plan-paid.

16. **Overlooking the Cunningham v. Cornell impact on PT pleading.** After _Cunningham v.
    Cornell University_, 604 U.S. \_\_\_ (April 17, 2025), plaintiffs need only allege the
    elements of § 406 to survive a motion to dismiss — § 408 exemptions are affirmative
    defenses. Plan sponsors must be able to document their exemption reliance, not just
    assert it.

17. **SECURE 2.0 operational adoption without amendment.** Plans must operate in
    compliance with SECURE 2.0 provisions as of each provision's effective date even
    before formal plan amendment. But the converse problem — planning to adopt new
    SECURE 2.0 provisions but never operationally implementing them — is an equally
    common failure. Verify operational status, not just document status.

18. **Ignoring ERISA § 412 fidelity bond size as the plan grows.** The bond must cover
    10% of prior-year plan funds handled (minimum $1,000; maximum $500,000; $1,000,000
    for plans holding employer securities). Plans with rapid asset growth or newly acquired
    employer security holdings frequently find their bond insufficient. This is a per se
    ERISA violation, not a best-practice gap.

---

## Writing Standards

Apply these standards before delivering any assessment output:

1. **Identify the regulator**: Every finding must state whether it is a DOL/ERISA Title I
   issue, an IRS/IRC qualification issue, or a PBGC issue. Never state "ERISA requires"
   when the requirement is actually in the IRC (or vice versa).

2. **Quantify the exposure**: Always estimate or range the penalty/excise tax exposure
   per finding. "This could result in significant penalties" is insufficient. State the
   applicable rate, the estimated amount involved, and the resulting estimate — followed
   by [VERIFY current indexed amount] where applicable.

3. **Identify the correction vehicle**: Every finding above LOW severity must include an
   identified correction pathway (VFCP, EPCRS-SCP, EPCRS-VCP, DFVCP, plan amendment,
   SPD update, or "no formal correction program — prospective compliance only").

4. **Flag thresholds explicitly**: Every indexed dollar amount must carry [VERIFY current
   year amount via IRS Notice / PBGC premium notice]. Stale thresholds produce wrong
   conclusions.

5. **Distinguish plan types**: Never apply DB-specific requirements (funding, PBGC) to
   DC plans or health/welfare provisions (COBRA, HIPAA) to retirement plans without
   explicit scoping.

6. **One finding per block**: Use the structured finding format — not narrative paragraphs
   that bury multiple issues together.

7. **State assumptions explicitly**: If context was not provided (controlled group
   composition, plan participant count, plan document terms), state the assumption you
   are making and note its impact on the analysis.

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Step 3: Search for current-year indexed thresholds (IRS annual limits Notice, PBGC
  premium notice), recent DOL/IRS guidance on open issues (SECURE 2.0 guidance, MHPAEA
  enforcement status, DOL Fiduciary Rule status), and ERISA case law (especially
  _Tibble_, _Dudenhoeffer_, _Cunningham_).
- Save results to `/tmp/erisa-assessment-authority.md`.
- Mark citations sourced from legalcode-mcp as VERIFIED in the Glass Box.

**Without legalcode-mcp**:

- Mark all indexed threshold amounts with [VERIFY].
- Note in Glass Box: `legalcode_mcp: "Not connected — all thresholds require current-year
verification against IRS Notice and PBGC premium notice"`
- Proceed with assessment using the most recently known figures as indicative values only.
- Focus analytical depth on structural compliance (plan document provisions, operational
  procedures, notice chains) rather than threshold-dependent analyses.

---

## Output Format Template

````
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ERISA COMPLIANCE ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Employer: [Name]                      Plan Year: [YYYY]
Plan(s) Assessed: [List]             Assessment Date: [YYYY-MM-DD]
Prepared for: [Plan Administrator / ERISA Counsel / HR Leadership / M&A Team]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## I. EXECUTIVE SUMMARY

Overall Compliance Posture: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

Findings by Severity:
  ⛔ CRITICAL:  [N]
  🟠 HIGH:      [N]
  🟡 MEDIUM:    [N]
  🔵 LOW:       [N]

Estimated Aggregate Penalty/Excise Tax Exposure: $[low] – $[high] [VERIFY all thresholds]
Highest-Priority Action: [One sentence — the most urgent item and its deadline]

Assessment Limitations:
  - [e.g., Plan document not reviewed — operational compliance assessed against stated
    practices only]
  - [e.g., Controlled group composition not confirmed — nondiscrimination analysis may
    be incomplete]
  - All dollar thresholds require current-year verification — see Glass Box.

---

## II. SCOPE AND METHODOLOGY

Plans assessed:
| Plan Name | Plan Type | Plan # | EIN | Plan Year |
|-----------|-----------|--------|-----|-----------|
| [...]     | [...]     | [...]  | [...]| [...] |

Documents reviewed: [List or "Not provided — assessment based on information described"]
Periods covered: [Plan years]
Analytical approach: [Document review / Narrative description / Checklist-based]
Disclaimer: This assessment is AI-assisted and does not constitute legal advice. Verify
all findings and indexed thresholds with qualified ERISA counsel before taking action.

---

## III. FINDINGS REGISTER

FINDING [#]: [Short Title — e.g., "Late 401(k) Deferral Deposits — Prohibited Transaction"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Severity:            ⛔ CRITICAL | 🟠 HIGH | 🟡 MEDIUM | 🔵 LOW
Regulator:           DOL/ERISA Title I | IRS/IRC | PBGC | Multiple
Topic Area:          Fiduciary | Prohibited Transaction | Qualification | Health/Welfare |
                     Reporting/5500 | SPD/Notice | SECURE 2.0 | ACA | COBRA | HIPAA |
                     MHPAEA | Defined Benefit | Other
Legal Authority:     [Primary citation — statute, regulation, guidance tier]
Finding:             [One paragraph: what the problem is; what was observed or reported]
Risk:                [Specific exposure: excise tax estimate, disqualification risk,
                     personal liability, participant harm. Mark all $ amounts [VERIFY]]
Correction Vehicle:  [VFCP / EPCRS-SCP / EPCRS-VCP / DFVCP / Plan Amendment / SPD
                     Update / No formal correction program — prospective compliance |
                     Correction deadline: [date or timeframe]]
Responsible Party:   [Plan Administrator | Employer | HR | Payroll | TPA |
                     Investment Committee | Plan Counsel]
Deadline:            [Specific date or timeframe — ASAP / 30 days / 60 days /
                     December 31, 2026 / Plan year end]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Repeat for each finding]

---

## IV. PENALTY AND EXCISE TAX EXPOSURE SUMMARY

| Finding # | Topic | Authority | Estimated Exposure | Severity |
|-----------|-------|-----------|-------------------|----------|
| 1         | [...]  | [...]     | $[X] – $[Y] [VERIFY] | ⛔ CRITICAL |
| 2         | [...]  | [...]     | $[X] – $[Y] [VERIFY] | 🟠 HIGH |
| ...       | ...    | ...       | ...               | ...      |
| **Total** |        |           | **$[X] – $[Y]**   |          |

Note: All amounts marked [VERIFY] require current-year confirmation against IRS/DOL/PBGC
publications before any reliance. Ranges represent indicative estimates only.

---

## V. REMEDIATION ACTION PLAN

**Immediate (0–30 days)**
- [ ] [Action] — [Responsible party] — [Deadline] — [Correction vehicle]

**Near-Term (30–90 days)**
- [ ] [Action] — [Responsible party] — [Deadline]

**This Plan Year / By December 31, 2026**
- [ ] SECURE 2.0 plan amendments — Plan counsel — December 31, 2026 deadline [VERIFY]
- [ ] [Other plan year-end actions]

**Annual Compliance Calendar — Recurring Items**
- [ ] 401(k) deferral deposit monitoring: Every payroll period
- [ ] ADP/ACP testing: Complete by March 15 (standard) or December 31 (EACA/QACA)
         following plan year end
- [ ] Form 5500 filing: July 31 (calendar year); October 15 with extension
- [ ] ERISA § 412 fidelity bond renewal: [Date] — verify adequacy vs. prior-year funds
- [ ] ACA measurement period / IRS updated penalty amounts: October/November each year
- [ ] ACA Forms 1094-C/1095-C: File by March 31; furnish to employees by January 31
- [ ] MHPAEA NQTL comparative analysis update: Before each plan year [VERIFY
         enforcement status]
- [ ] CAA gag clause prohibition attestation: Annual HIOS filing [VERIFY deadline]
- [ ] COBRA qualifying event tracking: Ongoing — 30-day employer notification chain
- [ ] Investment committee meeting and monitoring documentation: At least annually
- [ ] 404a-5 participant fee disclosure: At least annually (14-month rule)
- [ ] IRS indexed limits update: Monitor October IRS Notice each year

---

## VI. GLASS BOX — AUTHORITY AND VERIFICATION LOG

```yaml
glass_box:
  skill_name: "legalcode-benefits-erisa-compliance"
  assessment_date: "[YYYY-MM-DD]"
  entity_name: "[Employer / plan sponsor name]"
  tax_year_assessed: "[YYYY — confirm thresholds verified for this year]"

  plan_inventory:
    plan_types_assessed: "[List all: 401(k) / 403(b) / DB / Group Health / etc.]"
    plan_document_vintage: "[Most recent restatement or amendment date]"
    secure_2_0_amendment_status: "[Adopted: Yes/No/Partial — list provisions; Deadline: 12/31/2026]"

  employer_profile:
    employer_type: "[For-profit / Nonprofit / Government / Church]"
    erisa_title_i_applicable: "[Yes / No — exempt: [reason] / Partial]"
    controlled_group_confirmed: "[Yes — [members] / No / Unknown — [VERIFY]]"
    affiliated_service_group_confirmed: "[Yes / No / Unknown — [VERIFY]]"
    ale_status: "[ALE (50+ FTEs) / Non-ALE / Unknown]"

  participant_count:
    total_participants_beginning_of_year: "[number]"
    size_category: "[Large plan (100+) / Small plan (<100) / Not determined]"
    form_5500_type: "[Full Form 5500 with audit / Form 5500-SF / Not determined]"
    audit_required: "[Yes / No / Not determined]"

  scope_assessed:
    fiduciary_compliance: "[Yes / No]"
    prohibited_transactions: "[Yes / No]"
    tax_qualification: "[Yes / Partial — specify / No]"
    form_5500: "[Yes / No]"
    spd_notices: "[Yes / No]"
    cobra: "[Yes / No / N/A — <20 employees]"
    hipaa_portability: "[Yes / No]"
    aca_employer_mandate: "[Yes / No / N/A — Non-ALE]"
    mhpaea: "[Yes / No]"
    defined_benefit_funding: "[Yes / No / N/A — DC plan]"
    secure_2_0_provisions: "[Yes / No]"

  regulatory_authority_vintage:
    dol_guidance_current_as_of: "[Date]"
    irs_guidance_current_as_of: "[Date]"
    pbgc_premium_notice_used: "[Year]"
    dol_fiduciary_rule_status: "[VACATED — March 20, 2026 Federal Register Notice; Five-Part Test (1975) governs; monitor for replacement rulemaking]"
    mhpaea_2024_final_rule_status: "[Enforcement paused May 15, 2025; pre-2024 CAA 2021 / Technical Release 2023-01 standards operative; VERIFY current status]"
    secure_2_0_guidance_used: "[IRS Notice 2024-2; IRS Notice 2023-75 (Roth catch-up delay); IRS Notice 2023-43 (EPCRS EIF); IRS Notice 2025-19 (amendment deadline); IRS Notice 2026-9 (IRA amendment deadline)]"
    cunningham_v_cornell: "[Decided April 17, 2025 — § 408 exemptions are affirmative defenses; § 406 pleading bar lowered]"

  correction_programs:
    epcrs_applicable: "[Yes — [failure type: SCP / VCP / Audit CAP] / No / Not assessed]"
    vfcp_applicable: "[Yes — [transaction type] / No / Not assessed]"
    dfvcp_applicable: "[Yes — [filings delinquent] / No / Not assessed]"
    correction_window_risk: "[IMMEDIATE — window closing / Moderate / Low / N/A]"

  findings_summary:
    critical_count: "[N]"
    high_count: "[N]"
    medium_count: "[N]"
    low_count: "[N]"
    self_interrogation_applied_to: "[Finding #s, or 'None']"
    self_interrogation_result: "[PASS / REVISED — explanation / N/A]"

  citations:
    legalcode_mcp_connected: "[Yes / No]"
    research_reference_file: "[/tmp/erisa-assessment-authority.md / Not created]"
    citations_verified_count: "[N VERIFIED via legalcode-mcp]"
    citations_unverified_count: "[N marked [VERIFY]]"
    threshold_flags_issued: "[N thresholds flagged for current-year verification]"
    citation_quality_gates: "[PASSED — all 5 gates / FLAGGED — [gate: issue]]"

  confidence_overall: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Controlled group not confirmed — nondiscrimination analysis may be incomplete]"
    - "[Plan document not reviewed — operational compliance assessed against stated practices]"
    - "[All dollar thresholds require current-year verification before reliance]"
    - "[DOL Fiduciary Rule: monitor for replacement rulemaking]"
    - "[MHPAEA 2024 Final Rule: enforcement pause — verify current status before reliance]"
    - "[legalcode-mcp not connected — all statutory/regulatory citations unverified]"
  reviewer: "AI-assisted — requires review by qualified ERISA attorney (all findings), enrolled actuary (DB plan funding), and ERISA compliance professional before plan-level reliance"
````

---

## Localization Notes

This skill covers **US federal law only**. ERISA preempts most state laws relating to
employee benefit plans (ERISA § 514(a)).

**Fully insured vs. self-insured plans**: State insurance mandates (additional benefit
requirements, state mental health parity laws stronger than federal MHPAEA, surprise
billing state laws) apply to **fully insured** group health plans but **not** to
self-insured plans (the deemer clause, § 514(b)(2)(B)). Flag which plan type applies
before citing state health insurance requirements.

**California**: California has additional employer obligations for state disability
insurance, paid family leave (CFRA/FMLA interaction), and health plan requirements.
State mini-COBRA applies to employers with 2–19 employees.

**Multi-state operations**: For employers operating across multiple states, note that
state insurance mandates and state COBRA equivalents apply only to fully insured
arrangements. Self-insured plans governed by ERISA are exempt from most state mandates.

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis created via Mode A (Create New
Skill) workflow. Research inputs: 2-agent parallel research pipeline (Structural Analysis
Agent analyzing workflow design, severity classification, anti-patterns, and output
template; Prompt Engineering and Quality Agent designing ERISA-specific Citation Quality
Gates, Self-Interrogation, Confidence Scoring, guardrails, and Glass Box YAML; Legal
Research Agent conducting comprehensive web-backed research across 10 ERISA compliance
domains with verified current data through Q1 2026). Legal authority sourced via agent
web research including: DOL EBSA publications; Federal Register (March 20, 2026, Fiduciary
Rule Notice of Court Vacatur); DOL MHPAEA enforcement pause statement (May 2025); IRS
Notice 2024-80 (2025 limits); IRS Notice 2025-67 (2026 limits); IRS Notice 2026-9 (IRA
amendment deadline); IRS Notice 2023-43 (EPCRS EIF guidance); IRS Notice 2025-19
(SECURE 2.0 amendment deadlines); Cunningham v. Cornell University, 604 U.S. (April 17,
2025); DFVCP update (Federal Register, December 31, 2025); 26 C.F.R. §§ 54.4980B/H;
29 C.F.R. §§ 2520, 2550, 2590; ERISA §§ 102, 104, 302, 401–414, 502, 601–608; IRC §§
401–416, 4975, 4980B, 4980D, 4980H. All statutory and regulatory citations marked
[VERIFY] pending legalcode-mcp verification. All indexed thresholds marked [VERIFY current
year]. Quality: 18/18 required quality elements; 5-gate ERISA-specific Citation Quality
Gates; 3-pass Self-Interrogation; 5-level Confidence Scoring with ERISA examples; 18
anti-patterns; 12-step workflow with 5 CLARIFY points; 10 ERISA-specific guardrails;
complete Output Format Template; Glass Box YAML with ERISA-specific fields.
