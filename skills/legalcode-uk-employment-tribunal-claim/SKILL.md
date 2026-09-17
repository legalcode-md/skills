---
name: legalcode-uk-employment-tribunal-claim
description: Guide UK Employment Tribunal proceedings in England and Wales from ACAS early conciliation
  through to final remedy calculation.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Guide UK Employment Tribunal proceedings in England and Wales from ACAS early conciliation through to final remedy calculation. Use for ET1 claim drafting, ET3 response review, time limit analysis, preliminary hearing preparation, disclosure strategy, witness statement advice, hearing tactics, costs risk assessment, and remedy quantification (unfair dismissal basic/compensatory awards, discrimination Vento bands, whistleblowing, equal pay, unlawful deductions). Covers the full tribunal lifecycle: ACAS early conciliation (12-week period from 1 December 2025), ET1/ET3 forms, case management orders, disclosure, Polkey reductions, ACAS uplift/reduction, and Employment Rights Bill 2024-25 reforms. Jurisdiction-specific to England and Wales under the Employment Tribunal (Constitution and Rules of Procedure) Regulations 2013 (SI 2013/1237) and Employment Rights Act 1996. Does not cover Scottish or Northern Irish tribunals, civil court employment litigation, or non-employment discrimination (EHRC/county court routes).


# Legalcode — UK Employment Tribunal Claim (England & Wales)

> **Disclaimer**: This skill provides a framework for AI-assisted Employment Tribunal
> guidance. It does not constitute legal advice. All outputs must be reviewed by a
> qualified solicitor or barrister authorised by the SRA or BSB before use. Employment
> law changes frequently — financial limits and procedural rules are updated annually
> (typically 6 April). Verify current rates before relying on any figure stated here.
> Statutory and case law references carry hallucination risk — cross-check against
> legislation.gov.uk and authoritative case law databases before relying on them.

---

## Purpose and Scope

This skill guides AI-assisted analysis of UK Employment Tribunal proceedings in England
and Wales from ACAS early conciliation through to final remedy calculation.

**Covers:**

- ACAS early conciliation: mandatory first step, EC certificate, time limit extension
- ET1 claim form: drafting, particulars of claim, grounds checklist
- ET3 response form: 28-day deadline, default judgment risk, counterclaims
- Time limit analysis: claim-specific limits, ACAS extension formula, extension tests
- Preliminary hearings: case management, strike out (Rule 37), deposit orders (Rule 39)
- Disclosure: standard obligations, specific applications, electronic materials
- Witness statements: format, exchange procedure, stand-as-evidence-in-chief
- Hearing preparation: bundle structure, opening/closing submissions, burden of proof
- Costs risk: Rule 76 grounds, costs cap, wasted costs, preparing party orders
- Remedy calculation: unfair dismissal (basic and compensatory awards, Polkey, ACAS
  uplift), discrimination (Vento bands, aggravated damages, interest), whistleblowing
  (interim relief), equal pay, unlawful deductions
- Employment Rights Act 1996 / Equality Act 2010 claim elements
- Employment Rights Bill 2024-25 reforms (day-one rights, cap removal)

**Does not:**

- Cover Scottish or Northern Irish Employment Tribunal procedure (different rules apply)
- Provide legal advice or replace qualified employment counsel
- Cover civil court employment litigation (High Court / County Court track)
- Draft actual tribunal submissions without qualified legal review
- Cover ACAS arbitration scheme (separate to ET proceedings)

---

## Jurisdiction and Key Legal Framework

This skill is jurisdiction-specific to **England and Wales** under the following legal
framework:

| Source                                                                | Key Provisions                                                                                                                                             |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Employment Rights Act 1996 (ERA 1996)                                 | Unfair dismissal (ss.94-98), whistleblowing (ss.43B, 47B, 103A), unlawful deductions (ss.13-27), redundancy (ss.135-155)                                   |
| Equality Act 2010 (EqA 2010)                                          | Protected characteristics (s.4), direct discrimination (s.13), indirect discrimination (s.19), harassment (s.26), victimisation (s.27), equal pay (Part 5) |
| Employment Tribunals Act 1996 (ETA 1996)                              | Tribunal constitution, jurisdiction, enforcement                                                                                                           |
| ET Rules 2013 (SI 2013/1237)                                          | Procedure: ET1/ET3 (Rules 1-4, 16-26), preliminary hearings (Rules 53-56), costs (Rules 74-84), remedies (Rules 61-72)                                     |
| ACAS Early Conciliation Regs (SI 2014/254, as amended 2025)           | Mandatory EC, 12-week period (from 1 December 2025), EC certificate, time limit extension formula                                                          |
| ACAS Code of Practice on Disciplinary and Grievance Procedures (2015) | 25% uplift/reduction on compensatory award                                                                                                                 |
| Working Time Regulations 1998 (SI 1998/1833)                          | Rest breaks, holiday pay claims                                                                                                                            |
| National Minimum Wage Act 1998                                        | NMW enforcement claims                                                                                                                                     |
| TULRCA 1992                                                           | Collective redundancy, trade union detriment, TUPE interaction                                                                                             |

**Key Annual Updates** (effective 6 April each year):

- Weekly pay cap for basic award: **£719** (from 6 April 2025; previously £700 in 2024)
- Maximum basic award: **£21,570** (from 6 April 2025; previously £21,000)
- Maximum compensatory award: lower of **£118,223** or 52 weeks' gross pay (from 6 April
  2025; previously £115,115) — **[VERIFY: cap being removed from 1 January 2027 per
  Employment Rights Bill 2024-25]**
- Vento bands (from 6 April 2025): Lower £1,200–£12,100 | Middle £12,100–£36,400 |
  Upper £36,400–£60,700 | Exceptional: above £60,700

**[VERIFY: Always check current GOV.UK/ACAS/Presidential Guidance for latest figures]**

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Time limit issues could make or break the claim
- Multiple valid tactical approaches exist
- The severity of a risk depends on facts not yet provided

Use the **⟁ CLARIFY** pattern (structured options with "Why this matters") wherever
marked below. Skip the question if the user has already provided the information.

---

## Workflow

### Step 1: Accept the Matter

Accept tribunal-related instructions in any format:

- **File**: ET1 / ET3 / Particulars of Claim / witness statements / correspondence
- **Pasted text**: Factual narrative, draft documents, correspondence
- **Query**: A legal question about the tribunal process, time limits, or remedy
- **Request**: Draft a specific document or analyse a specific issue

**If no matter is provided**, prompt the user:

> "Please provide the facts of the employment dispute, any documents (ET1/ET3/correspondence),
> and your specific question or task. I'll then guide the analysis."

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning analysis, ask the user the following. Present as structured
options where possible. Skip any question already answered.

1. **Role — which side are you on?**
   - Options: Claimant (employee/worker), Respondent (employer), Both (advising on both)
   - _Why this matters_: The entire analysis flips — an ET1 weakness is a respondent
     strength; ACAS uplift is a claimant's benefit but an employer's risk.

2. **Stage of proceedings?**
   - Options: Pre-ACAS (not yet started EC), ACAS early conciliation in progress, ET1
     filed, ET3 due or filed, Preliminary hearing ordered, Final hearing approaching, Post-judgment
   - _Why this matters_: Determines which procedural steps are immediate and which time
     limits apply.

3. **Primary claim type(s)?**
   - Options: Unfair dismissal, Discrimination (specify characteristic), Wrongful
     dismissal, Unlawful deduction from wages, Whistleblowing detriment/dismissal, Equal
     pay, Redundancy pay, TUPE, Breach of contract, Other
   - Allow multiple selections.
   - _Why this matters_: Different time limits, qualifying conditions, extension tests,
     remedy regimes, and burden of proof rules apply to each.

4. **Key dates** (provide or estimate):
   - Date of dismissal / last discriminatory act / last deduction
   - Date ACAS EC was notified (if applicable)
   - Date EC certificate issued (if issued)
   - Current date / tribunal deadline
   - _Why this matters_: Time limits are jurisdictional bars — a 1-day error can be fatal
     to a claim and cannot be retrospectively cured.

5. **Qualifying period met (for unfair dismissal)?**
   - Options: Yes (2+ years' continuous employment), No, Unsure, Claim does not require
     it (e.g., whistleblowing, discrimination)
   - _Why this matters_: Standard unfair dismissal requires 2 years' continuous employment
     (ERA 1996 s.108). If not met, the claim is jurisdictional and the ET cannot hear it
     unless an exception applies (automatic unfair dismissal or discrimination).

6. **Representation?**
   - Options: Legally represented (solicitor/barrister), Trade union rep, McKenzie friend,
     Litigant in person, Not yet decided
   - _Why this matters_: Affects costs risk, sophistication of analysis required, and
     whether wasted costs orders are available.

7. **Settlement context?**
   - Options: No settlement discussions yet, ACAS conciliation ongoing, Without prejudice
     discussions underway, COT3 or settlement agreement being considered, Tribunal has
     ordered mediation
   - _Why this matters_: Affects strategy — a viable claim may settle before hearing; COT3
     payments affect remedy calculation.

If the user provides partial context, proceed with what is provided and **state
assumptions explicitly**: e.g., "Assuming claimant side — let me know if that's wrong."

---

### Step 3: ACAS Early Conciliation Assessment

**Mandatory prerequisite check**: Before an ET1 can be submitted, ACAS early conciliation
must ordinarily be completed (subject to exemptions).

#### 3a. Check EC Exemptions

Confirm whether EC is required. EC is **not** required if:

- The claim involves **multiple claimants raising the same complaint** (group claims can
  proceed with a single EC or without)
- The respondent **has already contacted ACAS** about the same matter
- The claim is for **interim relief** (s.128 or s.161 ERA 1996; Rule 95 ET Rules 2013)
  — 7-day deadline makes EC impractical
- The claim involves the **Security Service, SIS, or GCHQ**
- The claim is a **mixed-proceedings application** (both relevant and non-relevant claims)
- The claim is an **employer's contract counterclaim** (ET3 cross-claim — no EC needed)

**⟁ CLARIFY** — If EC status is unclear: "Has the claimant notified ACAS for early
conciliation? If yes, what date was ACAS notified and has the EC certificate been issued?"
_Why this matters_: An ET1 submitted without a valid EC certificate number (where EC was
required) will be rejected by the tribunal. This is a jurisdictional defect that cannot
be cured after the fact.

#### 3b. EC Procedure (12-Week Period — From 1 December 2025)

The EC procedure (as amended by the Employment Tribunals (Early Conciliation: Exemptions
and Rules of Procedure) (Amendment) Regulations 2025) runs as follows:

1. **Claimant notifies ACAS** (online or by phone) — this is "Day A" for time limit
   purposes
2. **ACAS contacts both parties** separately and attempts to facilitate settlement
3. **Conciliation period**: Up to **12 weeks** from notification (extended from 6 weeks
   before 1 December 2025)
4. **EC certificate issued**: Either when agreement is reached or after 12 weeks if no
   settlement
5. **Certificate number** must be entered on the ET1

#### 3c. EC Time Limit Extension Formula

Once the claimant notifies ACAS **within the original limitation period**, the clock
pauses. The final deadline for filing the ET1 is calculated as:

```
Final ET1 deadline = Date of EC certificate + 1 month
                     (provided ACAS was notified within the original time limit)
```

**Critical rules:**

- If ACAS was notified on the **last day** of the limitation period, the claimant still
  gets one full month after the EC certificate
- If ACAS was notified **after** the original limitation period expired, the extension
  **does not apply** — the limitation period has already passed
- If the one-month post-certificate period would expire **before** the original limitation
  date, the original date governs (whichever is later)

**Example**: Dismissal on 1 January 2026 (EDT). Unfair dismissal time limit: 31 March
2026 (3 months minus 1 day). Claimant notifies ACAS 20 March 2026 (within time). EC
certificate issued 12 June 2026 (12 weeks later). Final ET1 deadline: **12 July 2026**
(1 month after certificate). [VERIFY: always recalculate based on actual dates]

---

### Step 4: Time Limit Analysis

Time limits in Employment Tribunals are **jurisdictional** — a late ET1 deprives the
tribunal of jurisdiction and there is no discretion beyond the specific extension tests.

#### 4a. Claim-by-Claim Time Limits

| Claim Type                                         | Limitation Period | Runs From                                                 | Extension Test             |
| -------------------------------------------------- | ----------------- | --------------------------------------------------------- | -------------------------- |
| Unfair dismissal                                   | 3 months − 1 day  | Effective Date of Termination (EDT)                       | Not reasonably practicable |
| Constructive dismissal                             | 3 months − 1 day  | Date of resignation (EDT)                                 | Not reasonably practicable |
| Automatic unfair dismissal (whistleblowing s.103A) | 3 months − 1 day  | EDT                                                       | Just and equitable         |
| Discrimination (all types)                         | 3 months − 1 day  | Date of act (or last act in a series)                     | Just and equitable         |
| Wrongful dismissal (ET jurisdiction)               | 3 months − 1 day  | EDT                                                       | Not reasonably practicable |
| Wrongful dismissal (County Court)                  | 6 years           | Date of breach                                            | N/A (court rules)          |
| Equal pay                                          | 6 months − 1 day  | Last date of employment in stable employment relationship | Just and equitable         |
| Unlawful deductions from wages                     | 3 months − 1 day  | Date of last deduction (in a series)                      | Not reasonably practicable |
| Statutory redundancy pay                           | 6 months − 1 day  | EDT                                                       | Not reasonably practicable |
| Working time (WTR 1998)                            | 3 months − 1 day  | Date of the act/failure                                   | Not reasonably practicable |
| TUPE detriment                                     | 3 months − 1 day  | Date of detriment                                         | Not reasonably practicable |

**Effective Date of Termination (EDT)**: For unfair dismissal, the EDT is:

- **Summary dismissal**: Date notice of dismissal given (or, if pay in lieu, date of
  termination)
- **Notice dismissal**: Date the **notice expires** (not when notice was given)
- **Constructive dismissal**: Date of the employee's resignation

**Series of acts (discrimination)**: Where a claimant relies on a series of discriminatory
acts, the 3-month period runs from the last act in the series. Whether acts form a series
is a factual question — check whether they share a common theme or policy.

#### 4b. "Not Reasonably Practicable" Extension Test

Applies to: unfair dismissal, wrongful dismissal (ET), unlawful deductions, redundancy pay.

**Test**: The tribunal extends time only if:

- It was **not reasonably practicable** to present the claim in time, AND
- The claim was presented within a **further reasonable period** after the time limit expired

**Standard**: Strict — the claimant must show genuine inability to comply. The following
do **not** ordinarily satisfy the test:

- Ignorance of the time limit (unless the claimant could not reasonably have been expected
  to know)
- Negligence of the claimant or their adviser (adviser error does not transfer to the
  claimant in the way it might in civil courts — see _Dedman v British Building and
  Engineering Appliances_ [1974])
- Emotional distress, unless it amounted to clinical incapacity
- Waiting for internal appeal outcome (except in narrow circumstances)

**⟁ CLARIFY** — If the time limit appears to have expired: "The limitation period appears
to have passed. Please confirm: (a) Was there ACAS early conciliation and if so, when was
ACAS notified and when was the certificate issued? (b) Is there any reason the claim could
not have been presented in time (e.g., illness, fraud concealing the claim, employer
obstruction)? The extension test is strict — it's important to know the reason for delay
before assessing whether an extension is arguable."

#### 4c. "Just and Equitable" Extension Test

Applies to: discrimination claims (all types), equal pay.

**Test**: The tribunal may extend time if it considers it **just and equitable** to do so.

**Factors considered** (non-exhaustive list — tribunals have broad discretion):

- Length of delay and reasons for delay
- Conduct of both parties
- Merits of the claim (_Kumari v Greater Manchester Mental Health NHS Foundation Trust_
  [2022] EAT 132 — merits relevant but not determinative)
- Whether cogent evidence is still available
- Prejudice to the respondent
- Whether the claimant knew of the limitation period

**Standard**: More flexible than "not reasonably practicable" but not a guarantee —
tribunals regularly refuse extensions where there is no good reason for delay.

---

### Step 5: Claim Analysis — Elements, Strengths, and Gaps

Analyse each claim type systematically. For each, assess the elements required and
classify the strength of the claimant's case.

#### 5a. Claim Classification System

Classify each element of each claim on the following scale:

| Classification | Meaning                                                                | Action                                                               |
| -------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **STRONG**     | Element clearly satisfied on the facts; supporting evidence available  | Note as strength; proceed                                            |
| **ADEQUATE**   | Element made out but evidence is thin or counterarguments exist        | Note; gather further evidence                                        |
| **VULNERABLE** | Element arguable but likely to be challenged; real risk of failure     | Flag for reinforcement; consider whether to plead or omit            |
| **WEAK**       | Element poorly supported or likely to fail; risk of strike out / costs | Flag RED; advise on whether to abandon this element                  |
| **NOT MET**    | Jurisdictional requirement clearly not satisfied                       | Claim will fail; advise claimant (or advise respondent to challenge) |

#### 5b. Unfair Dismissal — Required Elements

**Qualifying conditions** (threshold — must be met before substantive analysis):

1. Employee status (not worker or contractor) — s.230 ERA 1996
2. Continuous employment ≥ 2 years at EDT — s.108 (exceptions: automatic UD claims;
   whistleblowing; protected characteristic dismissals)
3. Dismissal occurred (actual dismissal, constructive dismissal, or expiry of fixed-term
   contract without renewal) — s.95

**Substantive unfairness analysis — tribunal applies** (_Iceland Frozen Foods v Jones_
[1982] ICR 438):

- Was there a potentially fair reason (capability, conduct, redundancy, SOSR, illegality)?
  — s.98(1)-(2)
- Did the employer act **reasonably** in treating that reason as sufficient for dismissal,
  considering equity and the substantial merits of the case? — s.98(4)
- Apply the **range of reasonable responses** test: would a reasonable employer in the
  same circumstances have dismissed?
- Where dismissal follows disciplinary action, apply the _Burchell_ test (_BHS v
  Burchell_ [1980] ICR 303) for conduct dismissals: genuine belief, reasonable
  investigation, reasonable grounds

**Procedural fairness** (ACAS Code of Practice):

- Written notice of disciplinary hearing
- Right to be accompanied (ERA 1999 s.10)
- Opportunity to respond
- Appeal offered
- Proportionate sanction

**Polkey v AE Dayton Services** [1987] UKHL 8: Even a procedurally unfair dismissal may
result in reduced compensation if the tribunal finds the employer would have dismissed
fairly had proper procedure been followed.

**Constructive dismissal** (_Western Excavating (ECC) Ltd v Sharp_ [1978] EWCA):

- Employer committed a sufficiently serious breach of contract (typically implied term of
  trust and confidence — _Malik v BCCI_ [1997] UKHL 23)
- Employee resigned in response to that breach (not after delay affirming the contract)
- Employee did not delay acceptance of breach

#### 5c. Discrimination Claims — Required Elements (Equality Act 2010)

**Protected characteristics** (s.4 EqA 2010): age, disability, gender reassignment,
marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual
orientation.

**Direct discrimination** (s.13): Treatment **because of** a protected characteristic that
is **less favourable** than treatment of a real or hypothetical comparator without that
characteristic. No justification defence.

**Indirect discrimination** (s.19): A provision, criterion or practice (PCP) that is
applied equally to all but puts those with a protected characteristic at a **particular
disadvantage**. Can be justified if the PCP is a **proportionate means of achieving a
legitimate aim**.

**Harassment** (s.26): Unwanted conduct related to a protected characteristic that has
the **purpose or effect** of creating an intimidating, hostile, degrading, humiliating, or
offensive environment, or violating dignity.

**Victimisation** (s.27): Subjecting a person to a detriment because they have done a
**protected act** (e.g., brought discrimination proceedings, given evidence, made an
allegation in good faith).

**Burden of proof** (_Igen Ltd v Wong_ [2005] EWCA Civ 142; _Hewage v Grampian Health
Board_ [2012] UKSC 37):

- **Stage 1**: Claimant must establish primary facts from which the tribunal could decide,
  in the absence of any other explanation, that the respondent committed the act. Facts
  must establish a **prima facie case**.
- **Stage 2**: The burden shifts to the respondent to show the treatment was **in no sense
  whatsoever** on grounds of the protected characteristic. If no explanation, tribunal
  must find discrimination.

#### 5d. Whistleblowing — Required Elements (ERA 1996 ss.43A-47B, 103A)

1. **Worker** (not just employee — s.230(3) ERA 1996; includes some categories of
   contractor)
2. **Qualifying disclosure**: Disclosure of information (not mere expression of opinion)
   **tending to show** one of the six categories (criminal offence, legal breach,
   miscarriage of justice, H&S endangerment, environmental damage, concealment of above)
   — s.43B
3. **Reasonable belief**: Worker reasonably believed the information tended to show the
   above — _Gallacher v Abellio Scotrail_ [2020] EAT (belief need not be correct; must be
   objectively reasonable)
4. **Public interest**: Since ERA 1996 s.43B(1) amendment — worker reasonably believed
   the disclosure was in the **public interest** (_Chesterton Global v Nurmohamed_ [2017]
   EWCA Civ 979)
5. **Proper disclosure route** (see disclosure types above, Step 2 of research): internal,
   legal professional, prescribed regulator, or wider disclosure (s.43G) where conditions
   met
6. **Detriment/dismissal**: Suffered detriment (s.47B) or was dismissed (s.103A) **because
   of** the protected disclosure
7. **Causation**: The protected disclosure was the **reason or principal reason** for
   dismissal (s.103A) or a **material reason** for detriment (s.47B)

**No qualifying period**: Whistleblowing claims (s.103A) have no service threshold.

**Interim relief (Rule 95)**: Application must be made **within 7 days of EDT**
(strictly enforced). Threshold: claimant "likely to succeed" (= "pretty good chance" —
high bar). Rarely granted. Order: reinstatement or continuation of contract on full pay
until merits decided.

#### 5e. Unlawful Deductions from Wages (ERA 1996 ss.13-27)

Elements:

1. Claimant is a **worker** (broad category)
2. Employer made a **deduction** from wages (or accepted partial payment)
3. Deduction was **not authorised** by:
   - Relevant statutory provision
   - Express written provision in the employment contract agreed before the deduction
   - Written consent of the worker given before the deduction

**Series of deductions**: If the ET1 covers a series of unlawful deductions, the 3-month
time limit runs from the last in the series (provided there is no significant gap between
deductions — _Delaney v Staples_ [1992] UKHL 2 principle applied).

**Retail workers**: Special rules under ss.17-22 ERA 1996 limit deductions from wages
of retail workers to 10% of gross wages per pay period.

---

### Step 6: ET1 Drafting and Review

#### 6a. ET1 — Mandatory Content (Rule 1, ET Rules 2013)

The ET1 claim form must include:

| Field                 | Content                                      | Notes                                            |
| --------------------- | -------------------------------------------- | ------------------------------------------------ |
| Claimant details      | Full name, address, NI number, date of birth | All mandatory                                    |
| Respondent details    | Employer's legal name and address            | Must match EC certificate respondent             |
| EC certificate number | Individual ACAS EC number                    | One per respondent; claim rejected if missing    |
| Employment dates      | Start date, end date (or ongoing)            | Affects qualifying period and time limit         |
| Claim type            | Tick all applicable boxes                    | Must correctly identify claim; affects procedure |
| Particulars of claim  | Factual basis for each claim                 | See Meek principle below                         |

**[RED RISK]** Mismatch between the respondent named in the ET1 and the respondent named
in the EC certificate is a common defect that leads to rejection or jurisdictional
challenge.

#### 6b. Particulars of Claim — Meek Principle

_Meek v City of Birmingham District Council_ [1987] IRLR 250: Particulars must:

- Set out the **factual basis** for the claim (not mere assertions)
- Identify the **statutory provision** or contractual term relied on
- Give the respondent **fair notice** of the case being advanced
- Not be so deficient that the respondent cannot know the nature of the claim

**Structuring particulars for an unfair dismissal claim:**

1. Employment dates and job title
2. Nature of dismissal (summary / with notice / constructive) and EDT
3. Reason given by employer for dismissal
4. Why the dismissal was unfair (procedural failures + substantive unreasonableness)
5. Loss suffered (earnings from EDT to date of ET1)
6. Remedy sought (reinstatement / re-engagement / compensation)

**Structuring particulars for a discrimination claim:**

1. Protected characteristic
2. Comparator (real or hypothetical) and relevant circumstances
3. Specific acts of less favourable treatment / harassment / victimisation / PCP
4. Facts from which discrimination can be inferred (stage 1 burden of proof)
5. Why the employer's explanation is inadequate (anticipating stage 2)
6. Loss suffered (loss of earnings, injury to feelings, medical evidence)

**⟁ CLARIFY** — If particulars are vague or incomplete: "The current particulars may not
satisfy the Meek standard for [reason]. Would you like me to:

- (A) Identify the specific gaps and draft additional particulars?
- (B) Provide a full redraft of the particulars?
- (C) Simply flag the issues and leave redrafting to counsel?
  _Why this matters_: Inadequate particulars can result in a strike-out application (Rule
  37), a deposit order (Rule 39), or adverse inferences at the final hearing."

#### 6c. ET3 — Response Form (Rule 16, ET Rules 2013)

**Deadline**: **28 days from the date the tribunal sends the ET1 to the respondent** —
strictly enforced.

**Late ET3 consequences**: The tribunal may issue a **default judgment** (Rule 21):

- Finding for the claimant without hearing the respondent
- Tribunal proceeds to remedy-only hearing
- Respondent can apply to set aside default judgment but must show good reason for delay

**Extension**: Must be requested in writing **within the 28-day period** with full
reasons. Not automatic — tribunal must grant it.

**[RED RISK]** Failure to file ET3 within 28 days without an approved extension is one
of the most serious respondent errors — it can result in judgment without a hearing on
the merits.

**ET3 content requirements:**

- State which allegations are admitted and which are denied
- Set out the factual basis for any defence
- If contesting jurisdiction (e.g., time limit, qualifying period), state this explicitly
- Include any jurisdictional challenge as the **first point** in the ET3 — the tribunal
  may dispose of jurisdictional issues at a preliminary hearing

**Employer's contract counterclaim**: Under the Employment Tribunals Extension of
Jurisdiction (England and Wales) Order 1994, an employer may counterclaim for breach of
contract arising from the same employment. Jurisdiction is limited to claims **not
exceeding £25,000**.

---

### Step 7: Pre-Hearing Case Management

#### 7a. Case Management Order (CMO) — Typical Contents

Following a preliminary case management hearing (typically by phone or video), the
tribunal issues a CMO setting out:

| Item                              | Typical Timescale        |
| --------------------------------- | ------------------------ |
| Disclosure of documents           | 4-6 weeks after CMO      |
| Exchange of witness statements    | 2-4 weeks before hearing |
| Agreed bundle preparation         | 1-2 weeks before hearing |
| Hearing date and estimated length | Fixed at CMO stage       |

**Consequences of CMO non-compliance:**

- Adverse inferences (tribunal may draw negative inferences from non-disclosure)
- Strike out of evidence (Rule 37)
- Costs order (Rule 76)
- Application to adjourn (which itself carries costs risk)

#### 7b. Preliminary Hearings — Rule 53

**Case management preliminary hearings**: Procedural orders only. Usually conducted by
a single Employment Judge. May be by phone/CVP.

**Substantive preliminary hearings**: Determine preliminary issues including:

- Employment status (employee vs. worker vs. self-employed)
- Jurisdiction (time limits, qualifying period, territorial scope)
- Protected characteristic status (e.g., whether a belief is a protected philosophical
  belief under EqA 2010 — _Grainger plc v Nicholson_ [2010] EAT five-stage test)
- Whether claims form part of a series

**Strike out (Rule 37)**: Tribunal may strike out at any stage where a claim/response:

- Has **no reasonable prospect of success**
- Is **scandalous, vexatious, or unreasonably conducted**
- Has **not been actively pursued**
- Involves **non-compliance** with rules/orders
- Makes **a fair hearing no longer possible**
  Safeguard: The affected party must be given reasonable opportunity to make representations
  before strike out.

**Deposit order (Rule 39)**: If an allegation or argument has "little reasonable prospect
of success," the tribunal may order a party to pay up to **£1,000** as a condition of
continuing. If the deposit-payer ultimately loses on those grounds, the deposit is forfeited
and the party is deemed to have acted unreasonably (relevant to costs).

**⟁ CLARIFY** — If there is a potential jurisdictional issue: "I've identified a potential
jurisdictional issue with [time limits / qualifying period / employment status]. Do you
want me to:

- (A) Analyse this issue in full and assess the prospect of success at a preliminary hearing?
- (B) Identify what evidence would be needed to resist a jurisdictional challenge?
- (C) Advise on the tactical choice of whether to raise it proactively?
  _Why this matters_: A jurisdictional issue resolved early can save significant costs; a
  missed jurisdictional defence can be waived."

#### 7c. Disclosure Obligations

**Standard disclosure** in Employment Tribunals (Rule 31 ET Rules 2013 cross-referencing
CPR 31.6):

Parties must disclose documents that:

- They **intend to rely on**
- **Adversely affect** their own case
- **Adversely affect** another party's case
- **Support** another party's case

**Continuing duty**: Disclosure obligations continue throughout the proceedings.

**Electronic disclosure**: Email chains, instant messages (Teams, Slack, WhatsApp), HR
system records, and CCTV footage are all potentially disclosable. Parties should apply
proportionality — unusually burdensome searches can be challenged.

**Withholding documents**: Legitimate grounds to withhold include:

- Legal professional privilege (advice privilege and litigation privilege)
- Without prejudice communications (protected — _Rush & Tompkins v GLC_ [1988] UKHL 7)
- National security public interest immunity
- Third-party confidentiality (but usually not an absolute bar — redaction or confidentiality
  ring available)

**Specific disclosure application**: A party may apply for specific disclosure of named
documents or categories under Rule 31. The applicant must show relevance and that the
documents cannot be obtained otherwise.

**⟁ CLARIFY** — If there are documents of uncertain status: "You've mentioned
[communications / investigations / HR records]. Before including them in disclosure, I
need to confirm:

- Are any of these subject to legal professional privilege?
- Are any marked 'without prejudice' or part of settlement discussions?
- Are there any third-party privacy concerns?
  _Why this matters_: Inadvertently disclosing privileged documents can waive privilege;
  failing to disclose adverse documents can result in adverse inferences and costs."

#### 7d. Witness Statements

**Format requirements:**

- Typed, paragraphs numbered consecutively
- Minimum 12-point font, 1.5 line spacing
- Chronological narrative in first person
- Cross-references to bundle pages
- Statement of truth at end

**Exchange**: **Simultaneous exchange** — both parties exchange at the same time on the
ordered date. A party cannot change their statement after seeing the opponent's version.

**Standing as evidence in chief**: The witness statement serves as the witness's
examination-in-chief. The witness then faces:

1. Cross-examination by the opposing party
2. Brief re-examination on matters arising
3. Questions from the tribunal panel

**Practical checklist for a strong witness statement:**

- [ ] Directly addresses each element of the claim
- [ ] Explains contemporaneous documents (don't assume documents speak for themselves)
- [ ] Deals with adverse documents — explain rather than ignore
- [ ] Avoids legal argument (factual narrative only)
- [ ] Avoids hearsay where possible (or identifies it clearly where it cannot be avoided)
- [ ] Ends with statement of truth

---

### Step 8: Hearing Preparation and Strategy

#### 8a. Bundle Preparation

The **agreed bundle** is the single bundle of documents all parties and the tribunal will
use at the hearing.

**Standard structure:**

1. ET1 and Particulars of Claim
2. ET3 and any response particulars
3. Case Management Orders
4. Chronology of events (agreed or each party's version)
5. Cast list (parties and witnesses)
6. Documents in date order
7. Expert reports (if any)

**Pagination**: All pages numbered sequentially. Every page reference in witness statements
must correspond to the bundle page number.

**⟁ CLARIFY** — If there are disputed documents: "The parties appear to disagree on
whether [document X] should be included. The options are:

- (A) Include it in the agreed bundle (both parties have access)
- (B) Each party serves their own bundle of reliance documents
- (C) Apply to the tribunal for a ruling on admissibility
  _Why this matters_: Excluding a relevant document can limit what evidence the tribunal
  considers; including harmful documents may strengthen the opponent's case."

#### 8b. Opening Submissions

Employment Tribunals generally do not require formal opening statements, but the parties
(or their representatives) may provide:

- A brief opening note summarising the issues
- An agreed list of issues (preferable — helps focus the hearing)
- A chronology (if not already agreed)

**Best practice**: Agree a list of issues with the opposing party before the hearing. A
tribunal that receives an agreed list of issues can focus the hearing more effectively and
is less likely to decide on grounds neither party anticipated.

#### 8c. Closing Submissions

**Format**: Written or oral, as directed by the tribunal.

**Written closings** (submitted in advance): Preferred for complex or multi-day hearings.
Follow this structure:

1. Summary of issues to be decided
2. Summary of relevant evidence on each issue
3. Application of law to facts on each issue
4. Remedy (with calculation if liability found)
5. Costs application (if applicable)

**Oral closings**: Allow 20-40 minutes per side depending on complexity. Have a skeleton
argument ready even if delivering orally.

**Burden of proof reminder:**

- Unfair dismissal: employer bears burden of showing potentially fair reason (s.98(1)-(2));
  reasonableness assessed neutrally thereafter (s.98(4))
- Discrimination: claimant bears initial burden (Stage 1 _Igen v Wong_); shifts to
  respondent if prima facie case established
- Wrongful dismissal: claimant bears burden of proving breach
- Whistleblowing: claimant bears burden of proving protected disclosure; employer must
  show dismissal/detriment not because of it

#### 8d. Costs Risk Assessment (Rule 76)

**Starting position**: No automatic costs order. Costs are exceptional.

**Grounds for costs order (Rule 76)**:

1. A party or representative **acted vexatiously, abusively, disruptively, or otherwise
   unreasonably** in bringing or conducting proceedings
2. A claim or response had **no reasonable prospect of success**
3. A party **breached any tribunal order**
4. A hearing was **postponed or adjourned** on a party's application

**Costs cap**: Costs orders without detailed assessment: typically up to **£20,000**
(summary assessment). Beyond that amount: detailed assessment required (Rule 78).
[VERIFY: Current cap may be higher under updated Rules]

**Preparing party orders**: Where a party is a litigant in person, they may recover
preparation time at the applicable hourly rate (currently £45/hour [VERIFY]) for time
spent preparing for and attending the tribunal. This is separate from legal costs.

**Wasted costs**: Against a **representative personally** for improper, unreasonable, or
negligent conduct that caused another party to incur costs. Representative must be heard
before any wasted costs order is made.

**Costs warning**: A party can be warned at a preliminary hearing that if they persist
with a weak case, costs may be ordered. Proceeding after a costs warning is a relevant
factor in any subsequent costs application.

**⟁ CLARIFY** — Where the opposing party's conduct has been unreasonable: "Based on
[specific conduct], there may be grounds for a costs application under Rule 76. Do you
want me to:

- (A) Assess the strength of a costs application?
- (B) Draft a letter before costs application?
- (C) Advise on the tactical timing of a costs application?
  _Why this matters_: A successful costs application can significantly alter the economics of
  the litigation; an unsuccessful one may be perceived as tactical harassment and damage
  the applying party's standing with the tribunal."

---

### Step 9: Remedy Calculation

#### 9a. Unfair Dismissal — Basic Award

**Formula**: Completed years of continuous employment × multiplier × weekly pay (capped)

**Multiplier by age:**

- Under 22: **0.5** weeks' pay per year of service
- 22 to 40: **1** week's pay per year of service
- 41 and over: **1.5** weeks' pay per year of service

**Weekly pay cap** (from 6 April 2025): **£719** per week [VERIFY annually]

**Maximum service**: 20 years' continuous employment

**Maximum basic award** (from 6 April 2025): **£21,570** (= 20 years × 1.5 × £719)
[VERIFY annually]

**Reductions to the basic award:**

- Contributory fault (if the employee's conduct contributed to the dismissal)
- Receipt of redundancy payment (reduced pound for pound to avoid double recovery)
- Employee's refusal of an offer of reinstatement (discretionary reduction)

**Example calculation:**

```
Employee: Age 38, 12 years' service, actual weekly pay £650 (within cap)
Basic award: 12 years × 1 week × £650 = £7,800
```

#### 9b. Unfair Dismissal — Compensatory Award

**Purpose**: To compensate actual financial loss caused by the unfair dismissal (ERA 1996
s.123).

**Components:**

| Head of Loss                        | Calculation Method                                                          |
| ----------------------------------- | --------------------------------------------------------------------------- |
| Immediate loss of earnings          | Net weekly pay × weeks from EDT to hearing/settlement                       |
| Future loss of earnings             | Net weekly pay × estimated weeks until new employment (or reduced earnings) |
| Loss of pension rights              | Tribunal's discretion — simplified or actuarial approach                    |
| Loss of benefits                    | Specific valuation of lost benefits (car, healthcare, etc.)                 |
| Loss of statutory employment rights | Conventional award of ~£350-£500 (difficulty finding equivalent role)       |
| Expenses incurred in seeking work   | Actual documented expenses                                                  |

**Maximum compensatory award** (from 6 April 2025): **lower of £118,223 or 52 weeks'
gross pay** [VERIFY: Employment Rights Bill 2024-25 removes the cap from 1 January 2027]

**Reductions to the compensatory award:**

| Reduction                 | Basis                                                                     | Typical Range                      |
| ------------------------- | ------------------------------------------------------------------------- | ---------------------------------- |
| **Polkey reduction**      | Tribunal's assessment of likelihood employer would have dismissed fairly  | 0%–100%                            |
| **Contributory fault**    | Conduct of the claimant contributed to dismissal                          | 0%–100% (discretionary)            |
| **Failure to mitigate**   | Claimant failed to take reasonable steps to find work                     | By period of unreasonable inaction |
| **ACAS uplift/reduction** | Employer breached ACAS Code (uplift) / Claimant breached Code (reduction) | Up to ±25%                         |
| **Ex gratia payment**     | Employer made without-prejudice payment                                   | Deducted from award                |

**Polkey v AE Dayton Services** [1987] UKHL 8:

The tribunal applies a percentage probability that:

- (A) The employer would have dismissed fairly at some point regardless (reducing by the
  probability of inevitable dismissal), or
- (B) The employer would have followed proper procedure and the claimant would still have
  been dismissed anyway

**⟁ CLARIFY** — For Polkey assessment: "To calculate the Polkey reduction, I need to know:

- If proper procedure had been followed, what is the realistic probability the claimant
  would still have been dismissed?
- Were there substantive grounds for dismissal (even if the procedure was defective)?
  _Why this matters_: A 100% Polkey finding means compensation is reduced to nil (basic
  award only). Even a 50% Polkey finding halves the compensatory award."

**ACAS Code uplift/reduction calculation:**

- Uplift (employer breach): Compensatory award × up to 1.25 (i.e., +25%)
- Reduction (claimant breach): Compensatory award × as low as 0.75 (i.e., −25%)
- Applies to the compensatory award **after** other reductions (except contributory fault)

#### 9c. Discrimination — Remedy

**Injury to feelings — Vento bands** (effective 6 April 2025):

| Band             | Range             | When Applied                                                                                                                        |
| ---------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Lower Vento**  | £1,200 – £12,100  | Less serious cases: one-off acts, brief period of unfair treatment, single discriminatory remark without significant impact         |
| **Middle Vento** | £12,100 – £36,400 | Cases that do not merit the upper band: sustained discrimination over weeks/months, serious impact on health, pattern of harassment |
| **Upper Vento**  | £36,400 – £60,700 | Most serious cases: lengthy campaigns, significant psychiatric injury, severe impact on career or health over extended period       |
| **Exceptional**  | Above £60,700     | Exceptional gravity only: courts use sparingly                                                                                      |

[VERIFY Vento bands annually against Presidential Guidance Addendum each April]

**Aggravated damages**: Awarded where the respondent's conduct in litigation or in response
to the complaint was particularly offensive (e.g., retaliating against the claimant for
bringing proceedings, making untrue allegations of misconduct in response). Assessed
separately from Vento.

**Psychiatric/personal injury**: If clinical psychiatric harm is caused (not mere distress
— requires medical evidence), additional damages may be awarded beyond Vento bands.

**Loss of earnings**: Uncapped. Calculated on the same basis as unfair dismissal (actual
loss to hearing + future loss) but **without the compensatory award cap**.

**Interest**: Applicable to discrimination awards at the Employment Tribunals (Interest on
Awards in Discrimination Cases) Regulations 1996 — currently 8% simple interest
[VERIFY current rate]. Runs from midpoint of discrimination act(s) to date of judgment
for non-pecuniary losses; from date each loss accrued for financial losses.

**Multiple heads of claim**: A claimant dismissed for a discriminatory reason may claim:

- Injury to feelings (Vento)
- Loss of earnings (uncapped)
- Aggravated damages (if applicable)
- Reinstatement / re-engagement (rare in practice)
- Declaration of rights
- Recommendation (discontinued by Enterprise Act 2016 [VERIFY])

#### 9d. Whistleblowing — Remedy

- **No qualifying period**: Day-one right
- **Compensation**: Uncapped (unlike unfair dismissal compensatory award — no £118,223 limit)
- **Contributory fault**: May apply to dismissal award but is **more restricted** — the
  tribunal cannot apply contributory fault to the basic award in s.103A dismissal
- **Detriment claims (s.47B)**: Compensate for the specific detriment suffered, assessed
  as general damages; no cap
- **Interim relief**: Apply within 7 days of EDT (Rule 95); threshold is "likely to
  succeed"; rarely granted

#### 9e. Equal Pay — Remedy

- 6-year back pay period (stable employment relationship up to last date of employment)
- Arrears: Difference between claimant's pay and comparator's pay × hours worked over the
  6-year period
- Interest at 8% [VERIFY]
- No cap
- Pension equalisation where applicable

#### 9f. Reinstatement and Re-Engagement

**Reinstatement** (s.114 ERA 1996): Claimant returns to the same job on the same terms.
Tribunal must consider this remedy first if claimant seeks it.

**Re-engagement** (s.115 ERA 1996): Claimant employed by the same employer (or associated
employer) in a comparable job.

**When tribunals order reinstatement/re-engagement**: Rare in practice. Factors include:

- Whether practicable for employer to comply
- Whether claimant contributed to dismissal
- Whether it is just and equitable

**Additional award**: If employer fails to comply with a reinstatement/re-engagement
order, an **additional award** of 26–52 weeks' pay [VERIFY current limits] is made on
top of the unfair dismissal compensation.

---

### Step 10: Quality Verification

Before delivering any analysis, apply these quality checks:

#### 10a. Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                          | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific ERA/EqA section, ET Rule, ACAS Code provision, or named case                               | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow English legal citation conventions (case name, year, court; statute section)                             | Fix format                                               |
| **Currency**   | Every financial figure (weekly pay cap, Vento band, compensatory cap) verified for current annual period (check April update) | Flag "[CHECK CURRENCY — verify against current year]"    |
| **Domain**     | Analysis stays within England & Wales Employment Tribunal jurisdiction; no civil court, Scottish, or NI rules imported        | Remove or flag                                           |
| **Confidence** | Uncertainty explicitly stated, not hidden; where the law is unclear or contested, say so                                      | Add confidence qualifier                                 |

#### 10b. Self-Interrogation for HIGH-RISK Findings

For any finding classified as **WEAK** or **NOT MET**, or for any **RED procedural risk**,
apply this 3-pass review:

**Pass 1 — Jurisdictional Chain Integrity**:

- Does the time limit analysis follow precisely from the EDT and ACAS EC dates?
- Are there any arguments (not reasonably practicable / just and equitable extension)
  that have not been considered?
- Is the qualifying period analysis correct — are there any gap-in-service arguments that
  affect continuity?

**Pass 2 — Completeness**:

- Have all potentially applicable causes of action been considered? (A claimant dismissed
  for a discriminatory reason may have both unfair dismissal and discrimination claims)
- Have all heads of remedy been identified? (Claimants routinely underestimate loss of
  pension and statutory employment rights)
- Have all defences available to the respondent been identified?

**Pass 3 — Challenge**:

- What is the strongest argument that the WEAK element is actually arguable?
- Could additional evidence or disclosure change the classification?
- If the classification stands, what is the tactical recommendation — abandon this element,
  seek more evidence, or plead it subject to amendment?

Mark the audit trail `self_interrogation: PASS` or `self_interrogation: REVISED`.

#### 10c. Confidence Scoring

Assign a confidence level to each material finding:

| Level        | Range     | Meaning                                     | Action                                                |
| ------------ | --------- | ------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear facts                    | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor questions           | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but counterarguments exist   | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain — competing authorities | Flag for qualified legal review with both sides       |
| **Unlikely** | 0.00–0.39 | Weak basis, speculative                     | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

Apply at minimum to: time limit analysis, qualifying period assessment, each claim
classification, Polkey reduction estimate, and Vento band allocation.

---

## Severity Classification Summary

The skill uses two classification systems in parallel:

### Claims and Elements (5-tier)

| Tier | Label          | Description                                              |
| ---- | -------------- | -------------------------------------------------------- |
| 🟢   | **STRONG**     | Element clearly made out; supporting evidence present    |
| 🔵   | **ADEQUATE**   | Element arguable; evidence thin or subject to challenge  |
| 🟡   | **VULNERABLE** | Element arguable but genuinely at risk of failure        |
| 🔴   | **WEAK**       | Element poorly supported; risk of costs/strike out       |
| ⛔   | **NOT MET**    | Jurisdictional or substantive requirement clearly absent |

### Procedural Risks (3-tier)

| Tier | Label      | Trigger                                                                            |
| ---- | ---------- | ---------------------------------------------------------------------------------- |
| 🟢   | **GREEN**  | Procedural step correctly completed; no risk                                       |
| 🟡   | **YELLOW** | Potential procedural issue; action needed to avoid risk                            |
| 🔴   | **RED**    | Serious procedural defect; immediate action required to preserve the claim/defence |

**RED automatic triggers (escalate immediately):**

- ET1 filed without valid EC certificate (where EC was required)
- ET3 not filed within 28 days and no extension requested
- ACAS not notified within the original limitation period (no extension available)
- IT1 cross-referring to wrong respondent (mismatch with EC certificate)
- Interim relief application not made within 7 days of EDT (whistleblowing dismissal)
- Tribunal order not complied with (CMO breach risking strike out)

---

## Remedy Calculation Quick Reference

| Claim                               | Cap                                                 | Key Deductions                               | Uncapped?          |
| ----------------------------------- | --------------------------------------------------- | -------------------------------------------- | ------------------ |
| Unfair dismissal — basic award      | £21,570 (2025)                                      | Contributory fault, redundancy pay received  | No                 |
| Unfair dismissal — compensatory     | £118,223 or 52wks (2025) [cap removal pending 2027] | Polkey, contributory fault, mitigation, ACAS | No (until 2027)    |
| Discrimination — loss of earnings   | None                                                | Mitigation                                   | Yes                |
| Discrimination — injury to feelings | None                                                | N/A                                          | Yes (Vento guides) |
| Whistleblowing s.103A               | None                                                | Limited contributory fault                   | Yes                |
| Wrongful dismissal (ET)             | £25,000 (ET jurisdiction limit) [VERIFY]            | Mitigation                                   | No                 |
| Redundancy pay                      | £21,570 (2025)                                      | None (statutory formula)                     | No                 |

---

## Anti-Patterns

What NOT to do in Employment Tribunal work:

1. **Filing ET1 without checking the EC certificate** — The most common defect causing
   immediate rejection of the claim. Always verify the ACAS certificate number is on the
   ET1 and that the respondent named matches the EC certificate respondent exactly.

2. **Miscalculating the time limit by using the wrong start date** — The EDT for notice
   dismissal is the date the notice **expires**, not the date it was given. For
   constructive dismissal, the EDT is the date of resignation. One wrong assumption can
   make the ET1 two weeks too late.

3. **Failing to notify ACAS before the limitation period expires** — The EC extension only
   applies if ACAS was notified **within** the original limitation period. Late notification
   does not restart the clock.

4. **Confusing "not reasonably practicable" with "just and equitable"** — These are
   different tests with very different thresholds. Applying the more generous "just and
   equitable" test to an unfair dismissal claim (which uses "not reasonably practicable")
   is an error of law.

5. **Treating the qualifying period as 1 year** — The qualifying period for unfair
   dismissal is **2 years** (since 6 April 2012). Claiming with under 2 years' service
   without identifying an exception (whistleblowing, discrimination dismissal, etc.) will
   result in a jurisdictional bar.

6. **Drafting vague particulars that fail the Meek standard** — "The claimant was
   unlawfully dismissed" tells the respondent nothing. Particulars must set out the
   specific acts and statutory provisions relied on. Vague particulars invite a strike-out
   application and delay proceedings.

7. **Ignoring the respondent named in the ET1** — The employer's legal entity (not its
   trading name, not an individual manager, not the parent company) must be the respondent.
   Getting this wrong requires amendment proceedings and, if the limitation period has
   passed, may be fatal to the claim.

8. **Applying the compensatory award cap to discrimination loss of earnings** — Loss of
   earnings in a discrimination claim is **uncapped**. Applying the unfair dismissal cap
   (£118,223) to a discrimination claim is a material error of law.

9. **Forgetting the Polkey question in every unfair dismissal** — Even a grossly unfair
   procedure can result in a 100% Polkey reduction if the employer would have dismissed
   on the same substantive grounds anyway. Failing to address Polkey leaves the
   compensatory award overstated.

10. **Missing the ACAS uplift in unfair dismissal** — Where the employer failed to follow
    the ACAS Code of Practice on Disciplinary and Grievance Procedures, the tribunal may
    uplift the award by up to 25%. This is frequently overlooked in remedy calculations.

11. **Over-claiming on injury to feelings without placing acts in the right Vento band** —
    Claiming £50,000 injury to feelings for a single discriminatory remark risks a costs
    warning and undermines the claimant's credibility. Place the acts in the correct Vento
    band based on the nature, duration, and impact of the discrimination.

12. **Missing the 7-day interim relief deadline for whistleblowing dismissals** — The
    application must be made within 7 days of the EDT. There is no extension. If the
    adviser is not instructed within 7 days, this remedy is permanently lost.

13. **Not applying for a deposit order against a weak respondent case** — Where the
    respondent's defence has little prospect of success, a deposit order application can
    significantly strengthen the claimant's negotiating position and signals to the
    tribunal that the defence is weak.

14. **Pleading too many claims in the ET1** — Adding speculative claims (e.g., a
    discrimination claim with no factual basis alongside a strong unfair dismissal claim)
    increases the respondent's costs risk assessment to nil. Weak claims bundled with
    strong ones can attract costs orders against the claimant at the end of proceedings.

15. **Filing ET3 on day 28 without extension** — The 28-day period is strict. Filing on
    the last day is permissible, but leaving it to the last day carries high risk. If
    technical issues arise (system outage, postal delay), there is no safety margin and
    default judgment will follow.

16. **Calculating Vento bands using outdated figures** — Vento bands are updated every
    April. Using the prior year's bands can result in under- or over-valuation. Always
    check the current Presidential Guidance Addendum.

17. **Ignoring the Employment Rights Bill 2024-25** — The removal of the compensatory
    award cap (expected 1 January 2027) and the introduction of day-one unfair dismissal
    rights (after a 9-month initial period) are material changes to employment law.
    Advising on cases that will be decided after these changes take effect requires
    awareness of the transitional provisions.

18. **Failing to address mitigation** — Claimants have a duty to mitigate their loss from
    the date of dismissal. Failing to seek comparable employment, or turning down suitable
    offers, will reduce or extinguish the compensatory award from the date mitigation
    failed. Respondents should always investigate the claimant's post-dismissal employment
    history.

19. **Conflating detriment and dismissal claims under s.47B/103A** — Section 47B (detriment)
    and s.103A (dismissal) are different claims with different contributory fault rules.
    Do not apply the same deductions to both.

20. **Assuming all settlement agreements are valid COT3s** — A settlement of Employment
    Tribunal claims must either be a **COT3** (ACAS-conciliated) or a **qualifying
    compromise agreement / settlement agreement** that meets the statutory requirements
    (independent legal advice, written, signed, etc.). An informal settlement letter does
    not bar future tribunal claims unless it meets these requirements.

---

## Writing Standards

Apply these plain-language standards to all tribunal output (ET1 particulars, witness
statements, closing submissions, advice letters):

**For tribunal documents (ET1 particulars, skeleton arguments):**

- Plain English. The tribunal includes lay members who are not lawyers — write to be
  understood, not to impress.
- Active voice: "The employer failed to investigate the grievance" not "The grievance was
  not investigated by the employer"
- Numbered paragraphs. Every paragraph in a tribunal document should be numbered.
- One allegation per paragraph where possible — this makes cross-examination and response
  easier and clearer.
- Avoid Latin maxims — employment tribunals do not require them.
- Use the specific statutory language where it matters: "The claimant was subjected to a
  detriment" not "The claimant was treated badly"; "The effective date of termination" not
  "when the claimant was sacked".

**For legal analysis output (advice, remedy schedules):**

- Confidence qualifiers where appropriate: "likely", "arguable", "uncertain" — not false
  certainty
- Financial figures presented as tables with working shown
- Legal citations in correct form (case name, year in square brackets, court; statute
  with section)
- [VERIFY] markers on any figure that changes annually or any case that may have been
  overruled

**Quality gates before delivery:**

1. Can a non-lawyer claimant or HR manager understand the advice summary?
2. Does the ET1 particulars narrative tell a clear chronological story?
3. Is every financial figure in the remedy calculation verifiable (source and date shown)?
4. Are any phrases vague or hedged without reason? If yes, state the reason for
   uncertainty explicitly.
5. Has every claim element been addressed — not just the easy ones?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool
for statutory text, current case law, and regulatory guidance.

**With legalcode-mcp connected (preferred):**

- Search for current ET Rules provisions (SI 2013/1237 as amended)
- Verify current Vento bands, weekly pay caps, and compensation limits
- Search for recent EAT and Court of Appeal decisions on the relevant claim type
- Verify the current status of the Employment Rights Bill 2024-25 provisions
- Save results to `/tmp/legalcode-et-research.md` for use throughout the analysis
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Verify financial limits manually against GOV.UK Employment Tribunal statistics or
  ACAS guidance at acas.org.uk
- Check Presidential Guidance at judiciary.uk for current Vento bands

---

## Output Format Template

Deliver findings in this structured format:

---

````markdown
## Employment Tribunal Analysis — [Matter Reference]

**Claimant**: [Name or "Claimant"]
**Respondent**: [Name or "Respondent"]
**Your role**: [Claimant / Respondent / Neutral]
**Stage**: [Pre-ACAS / EC in progress / ET1 filed / Preliminary hearing / Final hearing]
**Primary claim(s)**: [List]
**Date of analysis**: [Date]

---

## Time Limit Assessment

| Claim     | EDT / Act Date | Limitation Expires | ACAS Notified | EC Certificate | ET1 Deadline | Status                                   |
| --------- | -------------- | ------------------ | ------------- | -------------- | ------------ | ---------------------------------------- |
| [Claim 1] | [date]         | [date]             | [date/N/A]    | [date/N/A]     | [date]       | ✅ In time / ⚠️ At risk / ❌ Out of time |
| [Claim 2] | ...            | ...                | ...           | ...            | ...          | ...                                      |

[If any claim is at risk or out of time, state the extension argument and its strength]

---

## Claim Analysis

### [Claim Type 1] — Overall Assessment: [STRONG / ADEQUATE / VULNERABLE / WEAK / NOT MET]

Confidence: [Definite / High / Probable / Possible / Unlikely]

**Elements:**
| Element | Classification | Notes |
|---------|---------------|-------|
| [Element 1] | 🟢 STRONG / 🔵 ADEQUATE / 🟡 VULNERABLE / 🔴 WEAK / ⛔ NOT MET | [explanation] |
| [Element 2] | ... | ... |

**Key risks**: [Specific risks to this claim]
**Evidence gaps**: [What additional evidence would strengthen or resolve vulnerable elements]
**Recommended actions**: [Numbered list]

[Repeat for each claim]

---

## Procedural Checklist

| Item                         | Status       | Action Required |
| ---------------------------- | ------------ | --------------- |
| ACAS EC completed            | ✅ / ⚠️ / ❌ |                 |
| EC certificate obtained      | ✅ / ⚠️ / ❌ |                 |
| ET1 filed within time        | ✅ / ⚠️ / ❌ |                 |
| ET3 filed within 28 days     | ✅ / ⚠️ / ❌ |                 |
| Disclosure completed         | ✅ / ⚠️ / ❌ |                 |
| Witness statements exchanged | ✅ / ⚠️ / ❌ |                 |
| Bundle agreed                | ✅ / ⚠️ / ❌ |                 |

[Flag any RED items immediately above the checklist table]

---

## Remedy Calculation

### Unfair Dismissal (if applicable)

**Basic Award:**

- Years of service: [X] | Age bracket: [under 22 / 22-40 / 41+] | Multiplier: [0.5 / 1 / 1.5]
- Weekly pay (actual / capped at £719): £[X]
- Basic award (before reductions): £[X × multiplier × weekly pay]
- Reductions: [contributory fault X%] / [redundancy payment received £Y]
- **Basic award (net)**: £[figure]

**Compensatory Award:**
| Head of Loss | Period | Amount |
|-------------|--------|--------|
| Immediate loss of earnings (net) | [dates] | £[X] |
| Future loss of earnings | [weeks estimate] × £[weekly net] | £[X] |
| Loss of pension | [method] | £[X] |
| Loss of statutory rights | [conventional] | £[X] |
| Benefits (car, healthcare etc.) | [specific] | £[X] |
| **Sub-total** | | £[X] |
| Polkey reduction ([Y]%) | | −£[X] |
| Contributory fault ([Z]%) | | −£[X] |
| Failure to mitigate | | −£[X] |
| ACAS uplift/reduction ([%]) | | ±£[X] |
| **Compensatory award (net)** | | £[X] |
| **Cap check** (lower of £118,223 or 52 weeks' gross £[Y]) | | ✅ / ⚠️ Capped at £[X] |

**Total unfair dismissal remedy**: £[basic + compensatory]

---

### Discrimination (if applicable)

| Head                             | Band / Basis                      | Amount                            |
| -------------------------------- | --------------------------------- | --------------------------------- |
| Injury to feelings               | [Lower / Middle / Upper] Vento    | £[X]–£[Y] range; recommended £[Z] |
| Aggravated damages               | [If applicable — specify conduct] | £[X]                              |
| Loss of earnings (uncapped)      | [same as UD loss table above]     | £[X]                              |
| Interest on non-pecuniary losses | [8%] × [months]                   | £[X]                              |
| **Total discrimination remedy**  |                                   | £[X]                              |

---

## Costs Risk Assessment

**Claimant's exposure**: [Low / Medium / High — with reasons]
**Respondent's exposure**: [Low / Medium / High — with reasons]
**Recommended steps**: [e.g., "Serve written warning of costs application", "Advise client
of costs risk if proceeding with [weak claim]", "Consider deposit order application"]

---

## Negotiation / Settlement Assessment

**Overall claim strength**: [Strong / Moderate / Weak]
**Realistic remedy range**: £[low] – £[high]
**ACAS COT3 recommendation**: [Yes — realistic settlement range / No — proceed to hearing]
**Key settlement factors**: [leverage, evidence, costs risk, reputational risk]

---

## Next Steps (Priority Order)

1. **[Immediate — deadline]**: [Action]
2. **[Urgent — within X days]**: [Action]
3. **[Standard — before [date]]**: [Action]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-uk-employment-tribunal-claim"
  jurisdiction: "England and Wales"
  procedural_framework: "Employment Tribunal (Constitution and Rules of Procedure) Regulations 2013 (SI 2013/1237)"
  user_role: "[Claimant / Respondent / Neutral]"
  stage: "[Pre-ACAS / EC / ET1 filed / Preliminary / Final hearing]"
  claims_analysed:
    - claim: "[claim type]"
      overall_classification: "[STRONG / ADEQUATE / VULNERABLE / WEAK / NOT MET]"
      confidence: 0.XX
      elements_assessed: X
      elements_strong: X
      elements_vulnerable: X
      elements_not_met: X
  time_limit_findings:
    - claim: "[claim type]"
      limitation_period: "[X months from Y]"
      edt_or_act_date: "[date]"
      expiry_date: "[date]"
      acas_notified: "[date / N/A]"
      ec_certificate: "[date / Not yet issued / N/A]"
      final_et1_deadline: "[date]"
      status: "[In time / At risk / Out of time]"
  remedy_calculated: "[Yes / No / Partial]"
  compensation_figures_date: "[April YYYY limits applied — VERIFY for current year]"
  vento_bands_date: "[April YYYY bands applied — VERIFY for current year]"
  legalcode_mcp: "Connected / Not connected"
  statutes_cited:
    - "[ERA 1996 ss.94-98 — VERIFIED / UNVERIFIED]"
    - "[EqA 2010 ss.13, 19, 26, 27 — VERIFIED / UNVERIFIED]"
    - "[ET Rules 2013 Rules 1, 16, 21, 37, 39, 53, 76 — VERIFIED / UNVERIFIED]"
  cases_cited:
    - "[Case name, citation — VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / N/A (no WEAK/NOT MET findings)"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  employment_rights_bill_status: "[Date of analysis — verify current status of ERB 2024-25]"
  limitations:
    - "Financial limits verified as of April 2025 — verify for current year before relying"
    - "Does not constitute legal advice — qualified legal review required before use"
    - "Employment Rights Bill provisions not yet in force — transitional rules apply"
  reviewer: "AI-assisted — requires qualified solicitor or barrister review"
  verify_flags:
    - item: "[any figure or authority flagged VERIFY]"
      source_needed: "[GOV.UK / ACAS / Presidential Guidance / ET Rules 2013]"
```
````

```

---

## Localization Notes

This skill is specific to **England and Wales**. Significant differences apply in:

| Jurisdiction | Key Differences |
|-------------|----------------|
| **Scotland** | Employment Tribunal Scotland — same substantive law (ERA 1996, EqA 2010) but separate tribunal administration; Scottish civil procedure rules apply to related court proceedings |
| **Northern Ireland** | Separate Employment Tribunal system under Industrial Tribunals Act (Northern Ireland) 1996; Industrial Tribunal and Fair Employment Tribunal; different rules and remedy limits |
| **Republic of Ireland** | Workplace Relations Commission (WRC), not Employment Tribunal; entirely different statutory framework; non-EU (UK) rules post-Brexit do not apply |

**Post-Brexit considerations**: UK employment law is no longer directly governed by EU
law, but retained EU law continues to apply (Equality Act 2010 derives from EU Directives).
The Retained EU Law (Revocation and Reform) Act 2023 may affect some EU-derived employment
law provisions over time [VERIFY current status of specific provisions].

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep research into the
Employment Tribunal (Constitution and Rules of Procedure) Regulations 2013 (SI 2013/1237),
Employment Rights Act 1996, Equality Act 2010, ACAS Early Conciliation Regulations (as
amended December 2025), and case law including *Polkey v AE Dayton Services* [1987] UKHL 8,
*Western Excavating v Sharp* [1978] EWCA, *Igen v Wong* [2005] EWCA Civ 142, *Vento v
Chief Constable of West Yorkshire* [2002] EWCA Civ 1871, and *Meek v City of Birmingham
District Council* [1987] IRLR 250. Financial limits reflect the April 2025 annual update.
Employment Rights Bill 2024-25 developments noted with [VERIFY] markers. Research
conducted via web search and structural analysis of legalcode-contract-review reference
standard. Not legal advice.
```
