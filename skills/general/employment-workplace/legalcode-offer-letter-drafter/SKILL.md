---
name: legalcode-offer-letter-drafter
description: Drafts and reviews US employment offer letters that are state-compliant across all 50 states.
  Covers at-will language, base salary and variable compensation, equity grants (options/RSUs/restricted
  stock), benefits summary, contingency clauses (background check, drug testing, I-9), confidentiality
  and IP assignment references, non-compete disclosures, and mandatory pay-transparency language for California
  (SB 1162), New York City (Local Law 32), Colorado (EPEWA / COMPS Order 38), Washington State (SB 5761),
  New York State (§194-b), and Illinois (SB 2038). Use when onboarding a new hire, extending an offer,
  converting a contractor, or reviewing a draft offer letter for compliance issues. Also covers offer
  rescission risk, implied-contract traps, 83(b) election notices, and state-specific IP assignment restrictions
  (CA, DE, IL, MN, NC, WA). US employers only — for international employment offers use jurisdiction-specific
  skills.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Offer Letter Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted offer letter drafting and
> review. It does not constitute legal advice. All outputs should be reviewed by a qualified
> employment attorney licensed in the applicable state(s) before use. Employment law changes
> rapidly; verify current applicability before relying on any provision described here.
> Statutory and case law references carry hallucination risk — verify against authoritative
> sources before relying on them. This skill covers US employment only.

---

## Purpose and Scope

This skill drafts and reviews US employment offer letters for salaried, hourly, and
equity-compensated employees across all 50 states. It generates state-compliant letter text,
identifies compliance gaps in existing drafts, and flags jurisdiction-specific requirements
the drafter must address.

**Covers:**

- At-will employment language (state-specific variants)
- Compensation: base salary, hourly rate, target bonus, commission plan disclosure
- Equity grants: stock options (ISO/NSO), RSUs, restricted stock, and related disclosures
- Benefits summary and integration references
- Contingency clauses: background check (FCRA-compliant), drug testing, I-9, license verification
- Confidentiality and IP assignment references (state restrictions on employee IP carve-outs)
- Non-compete and non-solicitation disclosures (advance notice requirements)
- Mandatory pay transparency language (CA, NYC, CO, WA, NY State, IL — with others flagged)
- Integration clauses and at-will preservation
- Offer rescission risk management
- Prohibited inquiries and discriminatory language screening

**Does not:**

- Draft the underlying CIIA/NDA/IP assignment agreement (reference it; don't reproduce it)
- Draft commission plan agreements (Cal. Labor Code § 2751 requires a separate signed plan)
- Provide tax advice on equity compensation or 83(b) elections
- Cover international employment offers (non-US)
- Constitute legal advice or replace qualified employment counsel

---

## Jurisdiction and Governing Law

This skill covers US employment law. Offer letters are governed by the law of the state
where the employee primarily works — not the employer's state of incorporation.

**Critical jurisdiction principle**: The employer's headquarters state does not govern.
A New York employer hiring a California-based employee must follow California law.
A Delaware-incorporated company hiring a Texas employee follows Texas law for employment
purposes.

State law governs:

- At-will employment doctrine and exceptions
- Pay transparency disclosure requirements
- Non-compete enforceability and advance notice requirements
- IP assignment restrictions (employee invention carve-outs)
- Drug testing permissibility
- Background check "ban the box" restrictions
- Wage payment timing (final pay, advance notice of pay rate)

Federal law governs:

- FCRA background check process (15 U.S.C. §§ 1681 et seq.)
- I-9 / IRCA work authorization verification (8 U.S.C. § 1324a)
- Title VII / ADA / ADEA / PWFA prohibited inquiries
- NLRA § 7 rights (restrictions on confidentiality clauses covering wages)
- FLSA classification (exempt/non-exempt) and minimum wage

[JURISDICTION-SPECIFIC] Every offer letter must identify the primary work location state
and apply that state's requirements. Remote roles must identify the "home state" the
employee primarily works from.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The applicable state(s) are not yet determined
- Compensation structure requires knowing equity vs. cash components
- Contingency conditions and sequencing are ambiguous
- Non-compete / IP assignment requirements depend on role and state
- Multiple states are involved (remote employee, multi-state employer)

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

### Step 1: Accept Input

Accept input in any of these formats:

- **New draft request**: User provides employee name, role, state, and compensation details
- **Review of existing draft**: User pastes or uploads a draft offer letter for compliance review
- **Partial information**: User provides some details — gather the rest via CLARIFY questions

**⟁ CLARIFY** — If in draft mode and information is incomplete, ask:

1. **Mode**: Are you drafting a new offer letter from scratch, or reviewing an existing draft?
   - Options: Draft new, Review existing draft, Both (draft and then review)

2. **Employee work state**: What US state will the employee primarily work in?
   - If remote: what is the employee's home state?
   - _Why this matters_: This single answer drives most compliance requirements.
   - If multi-state or unclear, ask whether the role is office-based, remote, or hybrid.

3. **Role level**: What is the role?
   - Options: Individual contributor (non-exempt hourly), Individual contributor (exempt
     salaried), Manager/director, Senior executive (SVP+/C-suite), Other
   - _Why this matters_: FLSA exemption classification, equity grant type, non-compete
     enforceability thresholds, and pay transparency triggers vary by level.

### Step 2: Gather Offer Details

**⟁ CLARIFY** — Gather the specific offer terms needed to draft or review:

**Compensation:**

- Base salary or hourly rate (amount and pay period)
- Sign-on bonus (amount, repayment clawback terms, vesting period)
- Target annual bonus: percentage, triggering conditions, discretionary vs. formula-based
- Commission: yes/no — if yes, a separate commission plan agreement is required (CA mandatory)
- Other variable pay

**Equity (if applicable):**

- Equity type: Stock options (ISO/NSO), RSUs, Restricted stock, SAFE/Warrant, No equity
- Grant amount (number of units/shares or target value)
- Vesting schedule (cliff + ratable, or custom)
- For options: exercise price (or "at FMV at grant date"), expiration, ISO vs. NSO
- For restricted stock: repurchase price, 83(b) election deadline flag needed?
- Plan name (e.g., "2024 Equity Incentive Plan") and board approval status

**Benefits:**

- Health/dental/vision: employer contribution percentage or "as described in plan documents"
- 401(k) or other retirement: employer match formula
- PTO/vacation: accrual rate or unlimited PTO (note: CA and other states treat accrued PTO
  as wages — "unlimited" PTO requires specific language)
- Other benefits referenced

**Start date and contingencies:**

- Proposed start date
- Background check: yes/no (if yes, FCRA pre-adverse action process applies)
- Drug test: yes/no (note state restrictions — CA, NY, NJ limit pre-employment marijuana)
- Reference check: yes/no
- I-9 / work authorization verification
- Signing of CIIA/NDA/IP assignment agreement as condition of employment
- Professional license or security clearance verification

**Non-compete / IP:**

- Will a non-compete or non-solicitation agreement be presented?
- What state is the employee working in? (determines enforceability and notice requirements)
- Is the employee an exempt salaried professional? (minimum earnings thresholds apply in
  IL, CO, WA, ME, and other states)

### Step 3: Identify Applicable Compliance Requirements

Based on the employee's primary work state, compile the compliance checklist:

#### Pay Transparency Requirements

| State            | Law                                                  | Threshold          | Requirement                                                                                                      | Effective Date              |
| ---------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------- | --------------------------- |
| California       | SB 1162 (Lab. Code § 432.3)                          | 15+ employees      | Salary range in job postings; disclose on employee request; pay scale in offer if requested                      | Jan 1, 2023                 |
| Colorado         | EPEWA / COMPS Order 38                               | All employers      | Salary range + benefits description in job postings; disclose pay range to applicants on request or before offer | Jan 1, 2021 (enhanced 2024) |
| Connecticut      | PA 21-30                                             | All employers      | Salary range to applicants upon request and to employees upon request                                            | Oct 1, 2021                 |
| Hawaii           | HRS § 378-2.4                                        | All employers      | Pay range in job listings with stated threshold or upon applicant request                                        | Jan 1, 2024                 |
| Illinois         | SB 2038 (820 ILCS 112/12)                            | All employers      | Pay scale and benefits in job postings                                                                           | Jan 1, 2025                 |
| Maryland         | MD Code Lab. & Empl. § 3-304.1                       | All employers      | Wage range on applicant request                                                                                  | Oct 1, 2020                 |
| Massachusetts    | MA Pay Transparency Act (M.G.L. c. 149 § 105A)       | 25+ employees      | Pay range in job postings; disclose on applicant/employee request                                                | Oct 29, 2025                |
| Minnesota        | Minn. Stat. § 181.173                                | 30+ employees      | Pay range in job postings                                                                                        | Jan 1, 2025                 |
| Nevada           | NRS 613.133                                          | All employers      | Wage range to applicants upon request after interview; on promotion                                              | Oct 1, 2021                 |
| New Jersey       | NJ Pay Transparency Law (N.J.S.A. 34:6B-1.1 et seq.) | 10+ employees      | Pay range and general benefits description in job postings                                                       | Jun 1, 2025                 |
| New York City    | NYC Admin. Code § 8-107(32) (Local Law 32)           | 4+ employees       | Salary range in job postings                                                                                     | Nov 1, 2022                 |
| New York State   | NY Lab. Law § 194-b                                  | 4+ employees       | Pay range in job postings statewide; extends Local Law 32 concept state-wide                                     | Sep 17, 2023                |
| Rhode Island     | RI Pay Equity Act (RI Gen. Laws § 28-6-21)           | All employers (1+) | Pay range to applicants before discussing compensation; at time of offer                                         | Jan 1, 2023                 |
| Washington D.C.  | D.C. Code § 32-1451 et seq.                          | All employers (1+) | Minimum and maximum salary/hourly pay in job postings; healthcare benefits description                           | Jun 30, 2024                |
| Washington State | RCW 49.58.110 (SB 5761)                              | 15+ employees      | Pay range + benefits description in job postings                                                                 | Jan 1, 2023                 |

**Important**: Pay transparency laws primarily apply to job postings. However, disclosing
the pay range in the offer letter is best practice and required in several states when
the applicant requests it. For any state with a posting requirement, include the range
in the offer letter to ensure consistency.

**⟁ CLARIFY** — For states with posting requirements (CA, CO, NY, NYC, WA, IL):

- Confirm whether a job posting was made and whether the range disclosed matches the offer
- If the offer salary falls outside the posted range, flag as a compliance risk (RED)

#### Non-Compete and Non-Solicitation Disclosures

| State            | Status                                              | Advance Notice Requirement                                                                      | Key Restrictions                                                                                                                                                          |
| ---------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| California       | Total ban (Bus. & Prof. Code § 16600)               | Not applicable — void ab initio; AB 1076 (2024) requires notice to existing employees           | Cannot present or enforce any non-compete for CA employees; SB 699 extraterritorial reach                                                                                 |
| Colorado         | Restricted (HB 22-1317, C.R.S. § 8-2-113)           | 14 days before start date OR before offer of promotion                                          | Only for earnings ≥ $123,750 (2024, adjusted annually); trade secret protection only                                                                                      |
| Illinois         | Restricted (IEPPA, 820 ILCS 90)                     | 14 calendar days advance notice; 10-day review; attorney advisement language required           | Non-compete: annual earnings > $75,000 (2027: $90,000); Non-solicit: annual earnings > $45,000                                                                            |
| Maine            | Restricted (26 M.R.S.A. § 599-A)                    | 3 business days before signing                                                                  | Non-exempt workers cannot be bound                                                                                                                                        |
| Massachusetts    | Restricted (M.G.L. c. 149 § 24L)                    | 10 business days before start OR material changed; garden leave or other consideration required | Maximum 1 year; geographic area must be reasonable; no non-competes for non-exempt, students, or terminated without cause employees                                       |
| Minnesota        | Total ban (Minn. Stat. § 181.988, eff. Jul 1, 2023) | Not applicable — void                                                                           | No post-employment non-competes; non-solicitation of employees/customers still permitted                                                                                  |
| New Hampshire    | Restricted (RSA 275:70-a)                           | Must be disclosed before accepting offer                                                        | Only for "highly compensated employees" [VERIFY threshold]                                                                                                                |
| Oklahoma         | Near-ban (Okla. Stat. tit. 15 § 219A)               | N/A                                                                                             | Only for software or technology; very narrow                                                                                                                              |
| North Dakota     | Near-ban (N.D. Cent. Code § 9-08-06)                | N/A                                                                                             | Voidable, narrow exception for sale of business                                                                                                                           |
| Oregon           | Restricted (ORS § 653.295)                          | 2 weeks advance notice before employment begins                                                 | Must be exempt employee earning ≥ $100,533/year (inflation-adjusted [CHECK CURRENCY]); maximum 12 months; employer must provide signed copy within 30 days of termination |
| Virginia         | Restricted (Va. Code § 40.1-28.7:8)                 | N/A                                                                                             | Cannot enforce against "low wage employees" (below average weekly wage)                                                                                                   |
| Washington State | Restricted (RCW 49.62)                              | 10 business days before start OR before offer of promotion                                      | Earnings ≥ $100,000+/yr; 18-month maximum; customer non-solicitation for earnings ≥ $250,000                                                                              |
| All other states | Varies                                              | Check state law [VERIFY]                                                                        | Most require reasonableness; some have minimum consideration requirements                                                                                                 |

**Federal context**: The FTC Non-Compete Rule (April 2024) was vacated by Ryan LLC v. FTC
(N.D. Tex. Aug. 20, 2024, aff'd on appeal). As of 2026, no federal non-compete ban is in
effect. NLRB GC 23-08 memo (2023) treated broad non-competes as NLRA § 7 violations for
most workers — withdrawn by NLRB GC 25-01 (Feb. 2025, Abruzzo successor). [VERIFY current
NLRB position]

#### IP Assignment Restrictions (Employee Invention Carve-Outs)

Several states prohibit employers from requiring employees to assign inventions made
entirely on the employee's own time without using employer resources, unless related
to employer's business:

| State          | Statute                   | Key Carve-Out Language                                                                                       |
| -------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| California     | Cal. Lab. Code § 2870     | Own time + own resources + not related to employer's business or anticipated R&D; also § 2872 notice in CIIA |
| Delaware       | Del. Code tit. 19 § 805   | Substantially identical to CA § 2870                                                                         |
| Illinois       | 765 ILCS 1060/2 (IIPA)    | Own time + own resources + not related to employer's business or anticipated R&D                             |
| Minnesota      | Minn. Stat. § 181.78      | Substantially identical; CIIA must include notice                                                            |
| North Carolina | N.C. Gen. Stat. § 66-57.1 | Substantially identical; § 66-57.2 notice requirement                                                        |
| Washington     | RCW 49.44.140             | Own time + own resources + not related to employer's business or R&D; also RCW 49.44.150 notice              |

**Required action for CA, IL, MN, NC, WA employees**: The offer letter (or accompanying
CIIA) must contain a statutory notice disclosing the employee's carve-out rights. Failure
to include this notice may render the IP assignment unenforceable in those states.
Reference the CIIA in the offer letter and confirm the CIIA includes the required notice.

#### Background Check and Drug Testing State Restrictions

**Background check / "ban the box" laws** (restrict when criminal history inquiries can
be made):

- **California**: AB 1008 (eff. 2018) — cannot inquire until conditional offer extended;
  must do individualized assessment; 5-day response period before adverse action
- **New York City**: NYC Fair Chance Act (Intro 318-A) — rigorous fair chance process;
  Article 23-A analysis required; 3-day waiting period after written assessment
- **New York State**: Correction Law Article 23-A — statewide Article 23-A analysis required
- **Massachusetts**: G.L. c. 151B — fair chance restrictions; CRA must use CORI process
- **Illinois**: 820 ILCS 75 (JOBSETA) — conditional offer before background check inquiry;
  7-business-day response period; individualized assessment required
- **Washington**: RCW 49.94 — similar conditional offer requirement; [VERIFY]
- Many municipalities have additional requirements [VERIFY applicable ordinances]

**Drug testing — marijuana-specific restrictions** (pre-employment marijuana testing):

- **California**: Cal. Gov. Code § 12954 (AB 2188, eff. Jan 1, 2024) — cannot discriminate
  based on off-duty marijuana use; cannot use positive tests for THC metabolites (non-psychoactive)
  for most positions; safety-sensitive positions and federal contractors exempt
- **New York City**: NYC Admin. Code § 8-107(31) (Intro 1445-A) — prohibits pre-employment
  drug tests for marijuana for most positions; safety-sensitive positions and certain
  regulated roles exempt
- **New Jersey**: N.J. Cannabis Regulatory, Enforcement Assistance, and Marketplace
  Modernization Act — employer cannot take adverse action solely for off-duty cannabis use;
  cannot refuse to hire based on positive test without reasonable suspicion of workplace
  impairment
- **Illinois**: Cannabis Regulation and Tax Act (410 ILCS 705) — cannot decline to hire
  based solely on positive cannabis test; reasonable suspicion of impairment standard
- **Minnesota**: Minn. Stat. § 181.953 (off-duty cannabis, eff. Aug 1, 2023) [VERIFY scope]
- **Montana, Nevada, New Mexico, Pennsylvania, Rhode Island**: Various protections [VERIFY]

**⟁ CLARIFY** — For roles in CA, NYC, NJ, or IL:

- Is this a safety-sensitive position (operates heavy machinery, handles firearms, drives
  commercially, works with children, handles controlled substances)?
- If yes, pre-employment drug testing and marijuana testing may be permissible — confirm
  with employment counsel and verify the specific exemption.

### Step 4: Draft the Offer Letter

Draft the offer letter using the following component framework. Mark each section with
its compliance status: **REQUIRED** (legally mandatory or essential for enforceability),
**RECOMMENDED** (strongly advised, omission creates risk), or **OPTIONAL** (common practice
but not legally required).

---

#### Component 1: Header and Parties — REQUIRED

```
[Company letterhead]
[Date]

[Candidate Full Name]
[Candidate Address]

Dear [First Name],

[Company Name] ("Company") is pleased to offer you employment in the position of
[Position Title] in our [Department/Group], reporting to [Manager Title], [Manager Name].
Your primary work location will be [City, State]. [If remote: This is a remote position;
your primary work location will be [City, State], where you reside.]
```

**Compliance notes:**

- Specify the primary work location city and state — this determines applicable law
- For remote employees, state that the employee's home state is the primary work location
- Do not describe the role as a "guaranteed" position or create permanent employment language

---

#### Component 2: At-Will Employment Statement — REQUIRED

For most states:

```
Your employment with the Company will be "at-will," meaning that either you or the
Company may terminate the employment relationship at any time, with or without cause,
and with or without notice. No statement in this letter, in any Company policy or
handbook, or by any employee or representative of the Company creates a contract of
employment for any specified term or limits the at-will nature of your employment.
This at-will status can be altered only by a written agreement signed by the CEO.
```

**State-specific at-will variations:**

- **Montana**: Montana Wrongful Discharge from Employment Act (Mont. Code § 39-2-901 et seq.)
  provides a "good cause" discharge requirement after the probationary period (default 6 months,
  or as defined in writing). At-will language is accurate during probation but must be
  supplemented with Montana-specific language for post-probation rights. [VERIFY current
  Montana practice with MT employment counsel]

- **All states**: Do NOT include "permanent employment," "job security," "as long as
  you perform well," or "we expect this to be a long relationship" — these phrases have been
  found by courts to create implied contracts in some states.

**⟁ CLARIFY** — Is this offer for a fixed-term engagement or project-based role?
If yes, fixed-term language creates contract claims and eliminates at-will protection.
Consult employment counsel before using fixed-term language.

---

#### Component 3: Compensation — REQUIRED

```
**Base Salary**: Your annual base salary will be $[AMOUNT], payable in
[bi-weekly / semi-monthly / weekly] installments in accordance with the Company's
standard payroll schedule, less applicable withholdings and deductions.
```

For hourly roles:

```
**Hourly Rate**: Your hourly rate of pay will be $[AMOUNT] per hour, for an anticipated
[HOURS] hours per week, less applicable withholdings and deductions.
```

**Pay transparency compliance** — include where the applicable state or city requires it:

For California (SB 1162, Lab. Code § 432.3, employers with 15+ employees):

```
The pay scale for this position is $[MINIMUM] to $[MAXIMUM] annually. Your offered
salary of $[AMOUNT] falls within this range.
```

For Colorado (EPEWA / COMPS Order 38):

```
The salary range for this position is $[MINIMUM] to $[MAXIMUM] annually. A description
of benefits is provided below.
```

For New York City / New York State (NYC Local Law 32 / NY Lab. Law § 194-b, employers
with 4+ employees):

```
The pay range for this position is $[MINIMUM] to $[MAXIMUM] annually.
```

For Washington State (RCW 49.58.110, employers with 15+ employees):

```
The pay range for this position is $[MINIMUM] to $[MAXIMUM] annually. A description of
the benefits offered with this position is set forth below.
```

For Illinois (SB 2038 / 820 ILCS 112/12, all employers, eff. Jan 1, 2025):

```
The pay scale for this position is $[MINIMUM] to $[MAXIMUM] annually. Benefits for this
position are described below.
```

**⟁ CLARIFY** — What is the salary range for this role (for states with pay transparency
requirements)? The offer salary must fall within the posted range if a job posting was made.
If no range was defined for the posting, this is a compliance gap to address prospectively.

---

#### Component 4: Bonus and Variable Compensation — RECOMMENDED

```
**Target Bonus**: You will be eligible to participate in the Company's annual bonus
program, with a target bonus of [X]% of your annual base salary, subject to the terms
and conditions of the bonus program as in effect from time to time. The actual bonus paid,
if any, will be determined in the Company's discretion based on individual and Company
performance. Bonus eligibility requires active employment on the payment date.
```

**Critical drafting notes:**

- Use "target" and "eligible to participate" — do not use "will receive" or "guaranteed"
- Specify payment conditionality (active employment on payment date is common and enforceable
  in most states)
- California warning: "active employment" forfeiture provisions may conflict with CA Labor
  Code if the bonus is characterized as a wage. Earned wages cannot be forfeited. Consult
  CA employment counsel for formula-based bonuses.
- Commission plans: If the employee is entitled to commission, do NOT describe it in the
  offer letter alone. California Labor Code § 2751 requires a separate signed written
  commission plan agreement. For other states, a separate commission agreement is best
  practice.

---

#### Component 5: Equity Compensation — RECOMMENDED (if applicable)

```
**Equity Grant**: Subject to approval by the Company's Board of Directors (or its
Compensation Committee), you will be granted [NUMBER] [shares of restricted stock /
stock options / RSUs] under the Company's [PLAN NAME] (the "Plan"). [For options: The
exercise price will be the fair market value of the Company's common stock on the grant
date, as determined by the Board.] The grant will vest [VESTING SCHEDULE, e.g., 25% after
twelve months of continuous service from your vesting commencement date, with the
remaining 75% vesting monthly over the following 36 months, subject to continued
employment]. The grant will be subject to the terms and conditions of the Plan and the
applicable grant agreement, which you will be required to execute as a condition of
the grant.
```

**Component-specific disclosures by equity type:**

**Stock Options (ISO/NSO):**

```
The options will be [incentive stock options ("ISOs") / nonqualified stock options
("NSOs") / a combination], subject to applicable tax rules. ISOs are subject to the
requirements of Section 422 of the Internal Revenue Code and may be subject to
alternative minimum tax (AMT). The options will expire [10 years / 5 years] from the
grant date (or sooner upon termination, per the Plan). You are encouraged to consult
a tax advisor regarding the tax treatment of your options.
```

**RSUs:**

```
The RSUs will be settled in shares of Company common stock upon vesting. Settlement
will be subject to applicable income and employment tax withholding. You are encouraged
to consult a tax advisor regarding the tax treatment of your RSUs.
```

**Restricted Stock with 83(b) election opportunity:**

```
**IMPORTANT — 83(b) ELECTION**: If you are granted restricted stock subject to a
vesting schedule and/or repurchase rights, you may be eligible to file an election
under Section 83(b) of the Internal Revenue Code within 30 DAYS of the grant date to
be taxed on the current fair market value rather than the value at vesting. This
election is irrevocable and has significant tax consequences. You should consult a
tax advisor IMMEDIATELY upon receiving any restricted stock grant to determine whether
to make this election. Failure to file within 30 days forfeits this option permanently.
```

**Required disclosures:**

- Confirm board approval is pending (not yet approved) — "subject to Board approval" is essential
- Do not promise a specific grant amount if board approval has not been obtained
- Do not state a specific exercise price if the grant date is in the future
- State that the grant is subject to the Plan and grant agreement — the offer letter terms
  do not override Plan documents

---

#### Component 6: Benefits Summary — RECOMMENDED

```
**Benefits**: You will be eligible to participate in the Company's standard employee
benefit programs, subject to their terms and conditions, including [health, dental, and
vision insurance / 401(k) plan with employer matching of X% up to Y% of base salary /
life and disability insurance / [X] days of paid time off per year (or: unlimited PTO) /
other benefits]. A full description of benefits will be provided during onboarding.
```

**PTO / unlimited PTO state considerations:**

- **California, Colorado, Illinois, Maine, Massachusetts, Montana, Nebraska, North Dakota,
  Rhode Island**: In these states, accrued vacation is typically treated as earned wages
  that cannot be forfeited. "Use it or lose it" PTO policies may be unlawful.
  "Unlimited PTO" policies eliminate accrual but require careful drafting to ensure no
  cap is implied and no forfeiture claim arises.
- For CA employees on unlimited PTO: include explicit language that "no vacation accrues
  and no payout is owed upon separation." Consult CA counsel on current DLSE position.

---

#### Component 7: Contingencies — REQUIRED (if conditions apply)

```
**Conditions of Employment**: This offer is contingent upon your satisfaction of the
following conditions prior to or on your start date:

[Include all applicable:]

(a) **Background Check**: Satisfactory completion of a background check conducted
    in accordance with the Fair Credit Reporting Act, 15 U.S.C. § 1681 et seq., and
    applicable state law. You will receive a separate FCRA disclosure and authorization.
    [For CA employees: This check will not be conducted until after a conditional offer
    of employment has been extended, in accordance with Cal. Govt. Code § 12952 (AB 1008).]

(b) **Work Authorization**: Verification of your legal authorization to work in the
    United States through the I-9 employment eligibility verification process. You must
    provide acceptable documentation on or before your first day of work.

(c) **Drug Test**: Satisfactory completion of a pre-employment drug test [where
    permissible under applicable state law — confirm state restrictions before including].

(d) **Non-Disclosure / IP Agreement**: Execution of the Company's Confidential
    Information and Invention Assignment Agreement ("CIIA"), a copy of which accompanies
    this letter.

(e) **Non-Compete Agreement**: Execution of the Company's Non-Competition and
    Non-Solicitation Agreement [omit entirely for CA employees; include state-required
    advance notice language for IL, CO, WA, MA, ME employees].

(f) **Professional License Verification**: Verification of [specific license or
    credential required for the role].
```

**FCRA pre-adverse action process**: If a background check results in potential adverse
action (decline or rescission), the employer must: (1) provide a pre-adverse action notice
with a copy of the report and CFPB Summary of Rights; (2) wait a reasonable time (typically
5 business days; CA requires a specific waiting period); (3) provide a final adverse action
notice. Failure to follow this process creates FCRA liability.

**Ban the Box compliance**: For employees in ban-the-box jurisdictions (see § 3 above),
do NOT include criminal history inquiry language in the initial offer letter. A conditional
offer must be extended first; background check inquiry comes after.

**Drug testing — marijuana note**: For CA, NYC, NJ, IL employees, omit general pre-employment
drug testing unless the role qualifies for the safety-sensitive exemption. State the
exemption basis explicitly if relying on it.

**Non-compete advance notice**: For the following states, the non-compete agreement must
be provided as a separate document before or concurrently with the offer letter, with
the required advance notice period:

- Illinois: at least 14 calendar days before start date; include the statutory advisement
  language from 820 ILCS 90/10: "The employee may have the agreement reviewed by an attorney
  before signing."
- Colorado: at least 14 days before start date or before a promotion
- Washington State: at least 10 business days before start date
- Massachusetts: at least 10 business days before start date or before resignation from
  prior employer
- Maine: at least 3 business days before signing
- Oregon: at least 2 weeks before start date [VERIFY current Oregon practice]

---

#### Component 8: Confidentiality and IP Reference — REQUIRED

```
**Confidential Information and IP Assignment**: As a condition of your employment, you
will be required to sign the Company's Confidential Information and Invention Assignment
Agreement ("CIIA"), a copy of which is enclosed. The CIIA governs your obligations with
respect to the Company's confidential information, trade secrets, and any inventions,
works, or other intellectual property you create during your employment.

[For CA, IL, MN, NC, WA employees — add:]
As required by [applicable state law], the CIIA contains a notice that it does not apply
to inventions that you develop entirely on your own time without using the Company's
equipment, supplies, facilities, or trade secret information, except for inventions
that (i) relate to the Company's business or anticipated research and development, or
(ii) result from work performed for the Company. Please review the CIIA carefully.
```

**State notice obligations:**

- California: Cal. Lab. Code § 2872 requires that a CIIA include a verbatim statement of
  the § 2870 carve-out rights. Referencing this in the offer letter is insufficient alone.
  The CIIA must contain the notice.
- Illinois, Minnesota, North Carolina, Washington: Similar notice obligations apply. Confirm
  the CIIA includes the required notice for the employee's state.

**NLRA § 7 compliance**: Confidentiality clauses that could be interpreted as restricting
employees from discussing wages, hours, or working conditions with colleagues may constitute
an unlawful interference with NLRA § 7 rights. The CIIA (and any reference to it in the
offer letter) should not characterize wages or working condition information as confidential.

---

#### Component 9: Start Date and Offer Expiration — RECOMMENDED

```
**Start Date**: We anticipate your start date will be [DATE], subject to the satisfaction
of the conditions set forth above. Please confirm your start date no later than [DATE].

**Offer Expiration**: To accept this offer, please sign and return this letter by
[EXPIRATION DATE]. If we do not receive your acceptance by this date, this offer will
be deemed withdrawn.
```

**Reliance damage risk**: A specific start date combined with the employee resigning from
a prior employer creates reliance damage exposure if the offer is rescinded. Manage by:

- Using "anticipated" start date language (not a guaranteed date)
- Including a force majeure / business condition reservation clause for later rescissions
- For key roles, obtaining WARN Act counsel if a mass layoff or plant closing might affect
  the role

---

#### Component 10: Integration and Entire Agreement — REQUIRED

```
**Entire Agreement**: This letter, together with the CIIA [and any other agreements
referenced herein], constitutes the entire agreement between you and the Company with
respect to the terms of your employment, and supersedes all prior discussions,
representations, and understandings, whether oral or written, relating to your employment.
This offer letter may not be modified except by a written instrument signed by both you
and an authorized officer of the Company.

**At-Will Reaffirmation**: Nothing in this letter, in any handbook or Company policy,
or in any prior or subsequent oral or written representation alters the at-will nature
of your employment as described above.
```

**⟁ CLARIFY** — Are there any side letters, verbal commitments, or other written promises
made to this candidate outside this offer letter? If yes, they must either be incorporated
into this letter or superseded by the integration clause. Undisclosed promises create
contract claims.

---

#### Component 11: Signature Block — REQUIRED

```
Please sign and return a copy of this letter to indicate your acceptance of this offer
on the terms described above.

Very truly yours,

[COMPANY NAME]

By: ________________________________
    [Name]
    [Title]
    [Date]

I have read, understand, and accept the foregoing offer of employment on the terms
described above.

________________________________    ________________
[Candidate Name]                     Date
```

---

### Step 5: Compliance Review Pass

After drafting (or when reviewing an existing draft), run this systematic compliance
checklist:

#### 5a. At-Will Language Audit

- [ ] At-will statement is present and clear
- [ ] No language creating implied contract (guaranteed, permanent, as long as you perform,
      long-term position)
- [ ] Modification only by signed writing from authorized officer
- [ ] Integration clause preserves at-will status
- [ ] For MT employees: Montana WDA considerations addressed

**Classification**: COMPLIANT / ISSUE FOUND / MISSING

#### 5b. Pay Transparency Compliance

- [ ] Identify employee's primary work state
- [ ] Determine if state/city has pay transparency obligations
- [ ] If yes: is salary range included? Does it match the posted range?
- [ ] If range was posted and offer falls outside range: FLAG as RED compliance issue

**Classification**: COMPLIANT / ISSUE FOUND / NOT APPLICABLE

#### 5c. Non-Compete / Non-Solicitation Compliance

- [ ] Is a non-compete to be presented?
- [ ] Identify employee's primary work state
- [ ] For CA: non-compete is void — is it absent from the offer package? (REQUIRED)
- [ ] For IL, CO, WA, MA, ME, OR: is required advance notice period being honored?
- [ ] For IL: is the required advisement language included in the non-compete document?
- [ ] For WA: does employee's compensation meet the applicable earnings threshold?
- [ ] Does the non-compete reference the CIIA properly?

**Classification**: COMPLIANT / ISSUE FOUND / NOT APPLICABLE

#### 5d. IP Assignment Compliance

- [ ] Does the offer letter reference the CIIA?
- [ ] For CA, IL, MN, NC, WA employees: is the CIIA enclosed and does it include the
      required statutory carve-out notice?
- [ ] Does the offer letter avoid characterizing wages as confidential information?

**Classification**: COMPLIANT / ISSUE FOUND / NOT APPLICABLE

#### 5e. Contingency Compliance

- [ ] For ban-the-box jurisdictions: is criminal history inquiry deferred until conditional
      offer stage?
- [ ] For CA, NYC, NJ, IL: is marijuana drug testing omitted (unless safety-sensitive
      exemption applies)?
- [ ] FCRA disclosure and authorization referenced (not embedded in offer letter)?
- [ ] I-9 verification referenced (but not requesting work authorization documents in
      the offer letter — that triggers IRCA discrimination risk)

**Classification**: COMPLIANT / ISSUE FOUND / NOT APPLICABLE

#### 5f. Equity Disclosures

- [ ] Equity described as "subject to Board approval" if not yet approved
- [ ] Plan name referenced
- [ ] Grant agreement execution required as a condition of the grant
- [ ] 83(b) election notice flag included for restricted stock
- [ ] No specific exercise price stated if grant date is future
- [ ] No "guaranteed" equity language

**Classification**: COMPLIANT / ISSUE FOUND / NOT APPLICABLE

#### 5g. Discriminatory Language Screen

Review the offer letter for any language that could constitute a prohibited inquiry or
discriminatory condition:

- Age-related language (e.g., "young, energetic team" — potential ADEA issue)
- Physical requirements not directly related to the role (potential ADA issue)
- Request for documentation of national origin or citizenship before I-9 process (IRCA)
- References to protected characteristics (race, sex, religion, national origin — Title VII)
- Disability-related inquiries or medical conditions (ADA pre-offer prohibition)
- Pregnancy-related language (PWFA — 42 U.S.C. § 20000gg et seq., eff. June 27, 2023)
- Genetic information requests (GINA — 42 U.S.C. § 2000ff — prohibits requesting genetic information at any stage)

**Classification**: COMPLIANT / ISSUE FOUND

---

### Step 6: Severity Classification

Classify each issue found in Step 5:

| Classification            | Definition                                                                                                     | Action Required                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **REQUIRED — MISSING**    | Legally mandated language absent; creates statutory liability, void provisions, or unenforceable agreements    | Must fix before sending; do not send without correction              |
| **REQUIRED — INCORRECT**  | Required language present but incorrectly stated; creates compliance risk                                      | Must fix before sending                                              |
| **RECOMMENDED — MISSING** | Not legally mandated but standard practice; absence creates legal exposure                                     | Fix before sending; acceptable to send if employer acknowledges risk |
| **OPTIONAL — CONSIDER**   | Common practice; inclusion would improve the offer package                                                     | Consider adding; not blocking                                        |
| **PROHIBITED**            | Language that violates a statute, creates discriminatory implications, or creates unintended legal obligations | Must remove before sending                                           |

---

### Step 7: Generate Remediation Actions

For each REQUIRED — MISSING, REQUIRED — INCORRECT, or PROHIBITED item, provide:

```
**Issue**: [Description of the compliance problem]
**Severity**: [REQUIRED — MISSING / REQUIRED — INCORRECT / PROHIBITED]
**State/Law**: [Applicable state and statute]
**Current language** (if reviewing): "[Exact quote from the draft]"
**Required fix**: "[Specific replacement language or instruction]"
**Legal basis**: [Statute or principle, with [VERIFY] if not independently confirmed]
**Risk if not fixed**: [Specific legal consequence — void provision, statutory penalty,
                        discrimination claim, contract claim, etc.]
```

---

### Step 8: Quality Verification

Before delivering the draft or review, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For any REQUIRED — MISSING or PROHIBITED item, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each state-law conclusion.
4. Confirm that all 11 offer letter components have been addressed (present or flagged
   as not applicable for this role).
5. Generate the Glass Box Audit Trail.

---

## Deviation Severity Classification

### REQUIRED (Must Include / Must Fix)

Language or provisions that are legally mandatory or whose absence voids key provisions:

- At-will statement (fundamental to at-will employment defense)
- Pay transparency salary range (CA, CO, NY, NYC, WA, IL employers with qualifying headcount)
- Non-compete advance notice disclosure for IL, CO, WA, MA, ME employees
- IP assignment CIIA carve-out notice for CA, IL, MN, NC, WA employees
- FCRA disclosure and authorization (separate from offer letter, but must be referenced)
- 83(b) election notice for restricted stock grants

**Action**: Do not send the offer letter without correcting REQUIRED items. The absence
creates statutory exposure, voids provisions, or creates unintended legal obligations.

### RECOMMENDED (Strong Best Practice)

Provisions that materially reduce legal risk but are not mandated by statute:

- Integration clause and at-will reaffirmation
- Equity "subject to Board approval" language
- Commission plan reference + separate plan agreement (CA mandatory; best practice everywhere)
- Start date qualified as "anticipated" to manage rescission risk
- Offer expiration date to manage timing uncertainty
- Specific benefits summary or reference to plan documents

**Action**: Include unless there is a specific business reason not to. Note the risk if
omitting.

### OPTIONAL (Common Practice)

Items that are helpful but not required:

- Sign-on bonus with repayment schedule
- References to company handbook and acknowledgment of receipt
- Arbitration agreement reference (if separately documented)
- Paid leave balance or PTO information

**Action**: Include if appropriate for the role and company practice.

### PROHIBITED (Must Remove)

Language that creates liability, discrimination risk, or unintended obligations:

- Implied permanent employment language
- Criminal history inquiry before conditional offer in ban-the-box jurisdictions
- Marijuana drug testing for non-safety-sensitive CA, NYC, NJ, IL employees
- Non-compete for CA employees (void ab initio; AB 1076 2024)
- IRCA: requesting work authorization documents in the offer letter text
- Any language that could suppress discussion of wages/working conditions (NLRA § 7)
- Age, disability, pregnancy, or other protected characteristic references

**Action**: Remove before sending. No exceptions without employment counsel review.

---

## Prioritization Framework

### Tier 1 — Must-Fix Before Sending

Non-compliance items that create statutory penalties, void provisions, or discrimination
claims:

- Missing at-will statement
- Pay transparency range missing in CA, CO, NYC/NY, WA, or IL
- Non-compete for CA employee included in offer package
- Non-compete advance notice not honored in IL, CO, WA, MA, ME
- CIIA carve-out notice missing for CA, IL, MN, NC, WA employee
- Criminal history inquiry before conditional offer in ban-the-box jurisdiction
- Prohibited marijuana drug testing for CA, NYC, NJ, IL non-safety-sensitive roles
- Discriminatory language or prohibited inquiry in the offer letter

### Tier 2 — Fix Before Sending (Strong Preference)

Items that create legal exposure but do not automatically void provisions:

- Missing integration clause or at-will reaffirmation
- Equity language without Board approval qualification
- Commission compensation described without reference to separate plan
- Start date described as guaranteed (rescission reliance damage risk)
- PTO / vacation described without addressing state wage-treatment rules (CA etc.)
- Restricted stock issued without 83(b) election notice

### Tier 3 — Consider Adding (Best Practice)

- Benefits plan documents referenced
- Sign-on bonus repayment clawback terms
- Offer expiration date specified
- Reference to arbitration agreement (if company uses one)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output:

| Gate           | Rule                                                                                           | Fail Action                                                           |
| -------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Source**     | Every state compliance requirement cites a specific statute or regulation                      | Add citation or mark "[UNVERIFIED — confirm with employment counsel]" |
| **Format**     | All citations follow consistent format: state abbreviation, statute, section                   | Fix format                                                            |
| **Currency**   | State law changes frequently (effective dates, annual salary thresholds). Flag pending changes | Mark "[CHECK CURRENCY — law may have changed]"                        |
| **Domain**     | Analysis applies the correct state's law. Do not apply CA law to a TX employee                 | Remove or flag jurisdictional bleed                                   |
| **Confidence** | Uncertainty explicitly stated. Do not present uncertain legal positions as settled             | Add confidence qualifier                                              |

### Self-Interrogation for REQUIRED — MISSING / PROHIBITED Items

For any issue classified as REQUIRED — MISSING or PROHIBITED, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the compliance requirement follow logically from
the cited statute? Would the Labor Commissioner or a court actually apply this requirement
to this employer / this employee / this state?

**Pass 2 — Completeness**: Have all applicable state and local laws been checked for this
requirement? Are there overlapping federal requirements? Is there a pending law or recent
amendment that changes the analysis?

**Pass 3 — Challenge**: What is the argument that this requirement does not apply here?
Is there an exemption (size, role type, industry) that could apply? Under what circumstances
would a reasonable employment attorney conclude this requirement is not triggered?

If any pass reveals a weakness, revise the analysis. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                            | Action                                     |
| ------------ | --------- | -------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled statutory requirement, clear text          | State with confidence                      |
| **High**     | 0.80–0.94 | Strong authority, threshold calculations correct   | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good authority but threshold or scope is ambiguous | State with explicit reasoning and [VERIFY] |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations     | Flag for employment counsel review         |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative application              | Do not assert; mark "[UNCERTAIN]"          |

**Special note on salary thresholds**: State law salary thresholds for non-compete
enforceability (CO, IL, WA) and pay transparency (number of employees) are adjusted
annually. Always confirm current thresholds via official state sources before advising.
Mark with [CHECK CURRENCY] when citing a threshold.

---

## Glass Box Audit Trail

Every offer letter draft or review MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-offer-letter-drafter"
  mode: "Draft / Review"
  employee_name: "[Name or role title if name not provided]"
  position_title: "[Role]"
  primary_work_state: "[State]"
  employer_hq_state: "[State]"
  equity_type: "[ISO / NSO / RSU / Restricted Stock / None]"
  non_compete_presented: "Yes / No"
  pay_transparency_applicable: "Yes / No — [applicable law if yes]"
  legalcode_mcp: "Connected / Not connected"
  components_reviewed: "[N of 11 components]"
  tier1_issues_found: "[N — list]"
  tier2_issues_found: "[N — list]"
  tier3_suggestions: "[N — list]"
  statutes_cited:
    - "[Statute — VERIFIED or UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., state law currency not verified]"
    - "[Any role-specific limitations — e.g., safety-sensitive exceptions not assessed]"
  reviewer: "AI-assisted — requires qualified employment attorney review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when drafting or reviewing US employment offer letters:

1. **Using employer headquarters state instead of employee work state** — The governing
   law for employment terms follows the employee's primary work location, not where the
   company is incorporated or headquartered. A Delaware-incorporated CA-based employee
   is subject to California employment law.

2. **Including non-compete language for California employees** — Cal. Bus. & Prof. Code
   § 16600 voids non-competes. AB 1076 (Jan 2024) requires employers to notify employees
   in writing that any non-compete they previously signed is void. Presenting a non-compete
   to a CA employee in an offer letter is a violation, not merely unenforceable.

3. **Omitting the at-will disclaimer or weakening it with permanence language** — Phrases
   like "this is a permanent position," "you can keep your job as long as you perform,"
   "we hope this will be a long-term relationship" have created enforceable implied
   contracts in multiple states. Every positive statement about tenure must be paired with
   a clear at-will disclaimer.

4. **Failing to honor non-compete advance notice periods** — Presenting a non-compete
   on the first day of work (or after offer acceptance) in IL, CO, WA, MA, ME, or OR
   may void the agreement under those states' advance notice requirements. The agreement
   must be provided the required number of days before the start date.

5. **Embedding FCRA authorization in the offer letter** — The Fair Credit Reporting Act
   requires a standalone written disclosure that a background check may be obtained. It
   may not be included in the offer letter or combined with other waivers. Embedding it
   creates a federal FCRA violation.

6. **Including pay transparency salary ranges that conflict with the posted range** — If
   a job posting listed a salary range and the offer letter states a different (higher or
   lower) range, this creates a pay equity compliance issue and may violate CA, CO, WA,
   or NY requirements. The offer salary must fall within the posted range.

7. **Promising equity before Board approval** — Stating "you will receive X shares" when
   the Board has not approved the grant creates a breach of contract claim if the Board
   reduces or denies the grant. Always use "subject to Board approval."

8. **Failing to include the 83(b) election notice for restricted stock** — The 30-day
   deadline for filing an 83(b) election under IRC § 83(b) is absolute and cannot be
   extended. Employees who miss this deadline face potential tax consequences that cannot
   be undone. Including the notice in the offer letter is a critical protection.

9. **Describing unlimited PTO without CA-specific language** — California treats accrued
   vacation as earned wages. An "unlimited PTO" policy must include express language that
   no vacation accrues and no payout is owed at separation. Silence creates a claim for
   reasonable vacation accrual.

10. **Pre-employment marijuana drug testing for CA, NYC, NJ, or IL non-safety-sensitive roles** —
    Since 2022-2024, these states and cities have restricted or prohibited using off-duty
    marijuana use against applicants. Testing for marijuana in these jurisdictions without
    applying the safety-sensitive exemption creates discrimination claims.

11. **Requesting work authorization documents in the offer letter** — IRCA prohibits
    pre-employment requests for specific I-9 documents. The offer letter may note that
    I-9 verification is a condition of employment but must not specify which documents the
    employee should bring. Requesting a "green card" or "Social Security card" in the
    letter is an IRCA violation.

12. **Omitting the CIIA carve-out notice for CA/IL/MN/NC/WA employees** — States with
    employee IP carve-out statutes require a specific written notice informing the employee
    of their rights. Failing to include this notice may render the IP assignment
    unenforceable in those states.

13. **Incorporating the handbook by reference as if it creates obligations** — Handbooks
    frequently contain language that could create implied contract claims. If referencing
    a handbook in the offer letter, include an explicit statement that the handbook does
    not create a contract and can be modified at any time.

14. **Setting a firm start date without a reservation clause** — A specific start date
    combined with an employee's reliance (resigning from a prior job) creates potential
    promissory estoppel or contract claims if the offer is rescinded. Use "anticipated"
    language and include a business condition reservation where appropriate.

15. **Describing commissions in the offer letter without a separate plan agreement** —
    California Labor Code § 2751 requires a signed written commission plan. Using the offer
    letter as the commission plan creates an argument that the vague offer letter terms
    govern, not the detailed plan. Always execute a separate commission plan agreement.

16. **Using age-stereotyping language** — "Young, energetic" or "digital native" in an
    offer letter or accompanying materials can be used as direct evidence of age
    discrimination under ADEA (29 U.S.C. § 623) if the employer later makes adverse
    decisions affecting the employee.

17. **Applying a pay range in a state that requires it but using an implausibly wide band** —
    Several states and localities are beginning to scrutinize salary ranges that are so
    broad (e.g., $50,000–$500,000) as to be meaningless. A "reasonably expected" range
    under CA SB 1162 requires genuine specificity to the role.

18. **Treating the offer letter as the controlling equity document** — The equity grant
    is controlled by the Plan and the grant agreement. If the offer letter and grant
    agreement conflict, disputes arise. The offer letter should describe the grant in
    summary and explicitly state that the grant is "subject to the terms of the Plan and
    grant agreement."

---

## Writing Standards

Apply these standards to every offer letter draft and analysis:

**For offer letter text (shared with the candidate):**

- Plain language. Legal precision without legalese.
- Active voice: "Your salary will be $X" not "A salary of $X will be paid to you"
- Specific and concrete: "annual base salary of $95,000" not "competitive compensation"
- Contingency conditions listed as a numbered list, not buried in a paragraph
- Equity described accurately: "subject to Board approval" is non-negotiable

**For compliance analysis (internal review output):**

- Lead with the issue, then the legal basis
- State the specific statute — not "applicable law may require"
- Name the specific action required: "Add the following language before the contingencies section"
- For borderline issues, provide both the risk position and the acceptable alternative
- Confidence qualifiers where analysis is not settled

**Quality gates before delivery:**

1. Can an HR professional draft a compliant letter from this output without needing to
   research anything further (other than state-specific verification)?
2. Can a candidate understand every term in the offer letter without a legal dictionary?
3. Is every compliance requirement backed by a specific citation (or flagged [VERIFY])?
4. Are all state thresholds (employee headcount, salary minimums) confirmed as current?
5. Is the at-will statement clear and not contradicted anywhere in the letter?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current statutory text for applicable state laws
- Verify current salary thresholds for non-compete enforceability (CO, IL, WA) — these
  are adjusted annually
- Verify current employer headcount thresholds for pay transparency laws
- Check for any new state laws or amendments enacted since training cutoff
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Save research to `/tmp/legalcode-offer-letter-research.md` for use throughout the analysis

**Without legalcode-mcp:**

- Mark all salary thresholds and headcount triggers with [CHECK CURRENCY]
- Mark all state statutes with [VERIFY] where the provision is drawn from training knowledge
- Focus the compliance analysis on well-established requirements (CA, CO, NYC, WA, NY)
  and flag emerging states with extra uncertainty notices
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require verification"`

---

## Localization Notes

This skill covers all 50 US states and the District of Columbia. The compliance matrix
in Step 3 covers the most material state requirements as of early 2026.

**Highest-complexity states** (requiring the most careful treatment):

- **California**: Most employer-hostile employment state; broadest employee protections;
  at-will doctrine largely intact but multiple carve-outs; SB 1162 pay transparency;
  § 16600 non-compete ban; § 2870 IP carve-out; AB 2188 marijuana; Lab. Code § 2751
  commission plan; unlimited PTO accrual issues; AB 1008 ban the box
- **New York**: NYC is more restrictive than NY State; Local Law 32 pay transparency;
  Article 23-A background check; NYC Intro 1445-A marijuana; NY State § 194-b pay
  transparency applies statewide
- **Illinois**: IEPPA non-compete advance notice and earnings thresholds; SB 2038 pay
  transparency; 820 ILCS 75 JOBSETA ban the box; Illinois IIPA IP carve-out
- **Washington State**: SB 5761 pay transparency; RCW 49.62 non-compete earnings threshold;
  RCW 49.44.140 IP carve-out; RCW 49.94 ban the box

**States with no pay transparency requirements** (as of 2026): Alabama, Alaska, Arizona,
Arkansas, Florida, Georgia, Idaho, Indiana, Iowa, Kansas, Kentucky, Louisiana, Michigan,
Mississippi, Missouri, Nebraska, New Hampshire, North Carolina, North Dakota, Ohio,
Oklahoma, Pennsylvania, South Carolina, South Dakota, Tennessee, Texas, Utah, West Virginia,
Wisconsin, Wyoming [VERIFY — this list changes as new laws are enacted]

**States with near-total non-compete bans** (in addition to California): Minnesota
(eff. Jan 1, 2023), North Dakota (very limited), Oklahoma (limited). [VERIFY current
state of each]

**Federal contractor notes**: Federal contractors subject to OFCCP (Executive Order 11246,
as amended) have additional obligations regarding equal employment opportunity language.
OFCCP-covered contractors should include standard EEO tagline and may have additional
disclosure requirements.

---

## Output Format Template

Structure the final deliverable as follows:

---

### Option A: New Draft Offer Letter

```markdown
## EMPLOYMENT OFFER LETTER — [COMPANY NAME]

### Prepared for: [Candidate Name] | [Position] | [State] | [Date]

---

[Full offer letter text per Components 1–11]

---

## Compliance Summary

**Employee Work State**: [State]
**Pay Transparency**: [Law / Compliant / Not Applicable]
**Non-Compete Status**: [Compliant / Not Applicable / Issue Found]
**IP Assignment Notice**: [Required / Included / Not Applicable]
**At-Will Language**: [Present / Issue Found]

## Items Requiring Action Before Sending

### Tier 1 (Must-Fix)

[List]

### Tier 2 (Should-Fix)

[List]

## Tier 3 (Consider)

[List]

[Glass Box YAML]
```

---

### Option B: Compliance Review of Existing Draft

```markdown
## Offer Letter Compliance Review

**Document**: [Document name / date]
**Employee Work State**: [State]
**Review Date**: [Date]
**Reviewer**: AI-assisted (legalcode-offer-letter-drafter) — requires employment attorney review

---

## Critical Issues (Tier 1 — Must Fix Before Sending)

### Issue 1: [Issue Title] — REQUIRED — MISSING / PROHIBITED

**Issue**: [Description]
**Current language**: "[Quote from draft]"
**Required fix**: "[Replacement language or specific action]"
**Legal basis**: [Statute / [VERIFY]]
**Risk**: [Specific legal consequence]

[Repeat for each Tier 1 issue]

---

## Tier 2 Issues (Should Fix)

### Issue N: [Issue Title] — RECOMMENDED — MISSING

[Same format]

---

## Tier 3 Suggestions

[Brief list with explanations]

---

## Components Checklist

| Component              | Status                             | Notes |
| ---------------------- | ---------------------------------- | ----- |
| At-will language       | ✅ PRESENT / ⚠️ ISSUE / ❌ MISSING |       |
| Pay transparency range | ✅ / ⚠️ / ❌ / N/A                 |       |
| Compensation (base)    | ✅ / ⚠️ / ❌                       |       |
| Bonus / variable pay   | ✅ / ⚠️ / ❌ / N/A                 |       |
| Equity grant           | ✅ / ⚠️ / ❌ / N/A                 |       |
| Benefits summary       | ✅ / ⚠️ / ❌                       |       |
| Contingencies          | ✅ / ⚠️ / ❌ / N/A                 |       |
| CIIA reference         | ✅ / ⚠️ / ❌                       |       |
| IP carve-out notice    | ✅ / ⚠️ / ❌ / N/A                 |       |
| Non-compete notice     | ✅ / ⚠️ / ❌ / N/A                 |       |
| Integration clause     | ✅ / ⚠️ / ❌                       |       |
| Signature block        | ✅ / ⚠️ / ❌                       |       |

---

[Glass Box YAML]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A (create from scratch)
using deep research on US employment law applicable to offer letters, drawing on:

- California SB 1162 (Lab. Code § 432.3), AB 1008 (Gov. Code § 12952), AB 2188
  (Gov. Code § 12954), Lab. Code §§ 2751/2870/2872, Bus. & Prof. Code § 16600 /
  AB 1076 / SB 699
- Colorado EPEWA / COMPS Order 38, HB 22-1317 (C.R.S. § 8-2-113)
- Illinois IEPPA (820 ILCS 90), SB 2038 (820 ILCS 112/12), JOBSETA (820 ILCS 75), IIPA
  (765 ILCS 1060/2)
- New York City NYC Admin. Code § 8-107(32) (Local Law 32), Intro 1445-A
- New York State NY Lab. Law § 194-b
- Washington State RCW 49.58.110 (SB 5761), RCW 49.62, RCW 49.44.140, RCW 49.94
- Massachusetts G.L. c. 149 § 24L
- Minnesota Minn. Stat. §§ 181.78 / 181.988
- Fair Credit Reporting Act (15 U.S.C. §§ 1681 et seq.)
- IRCA (8 U.S.C. § 1324a)
- NLRA § 7 (29 U.S.C. § 157)
- IRC § 83(b) restricted stock election
- Ryan LLC v. FTC (N.D. Tex. Aug. 20, 2024) — FTC non-compete rule vacatur
- NLRB GC 23-08 (2023); NLRB GC 25-01 (2025) withdrawal
- Montana Wrongful Discharge from Employment Act (Mont. Code §§ 39-2-901 et seq.)
- Reference standard: `skills/general/contracts/legalcode-contract-review/SKILL.md`

All state citations should be verified against current official sources. Annual thresholds
(non-compete earnings floors in CO, IL, WA; employer size thresholds for pay transparency)
change each calendar year.
