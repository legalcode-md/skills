---
name: legalcode-severance-agreement-review
description: Reviews severance and separation agreements for legal sufficiency, OWBPA/ADEA compliance,
  and employer liability exposure. Use when evaluating a severance, separation, settlement, release, or
  departure agreement for any employee aged 40+ (OWBPA/ADEA waiver compliance), any group or RIF-related
  separation (45-day period, group informational disclosure), or any individual termination requiring
  release of claims.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews severance and separation agreements for legal sufficiency, OWBPA/ADEA compliance, and employer liability exposure. Use when evaluating a severance, separation, settlement, release, or departure agreement for any employee aged 40+ (OWBPA/ADEA waiver compliance), any group or RIF-related separation (45-day period, group informational disclosure), or any individual termination requiring release of claims. Covers: OWBPA 7-factor knowing-and-voluntary analysis (29 U.S.C. § 626(f)); 21-day vs. 45-day consideration period determination; non-waivable 7-day revocation window; group termination age/title disclosure requirements; ADEA-specific release language; release scope and overbreadth (Title VII, ADA, ADEA, FLSA, state law); consideration adequacy (earned wages, ERISA vested benefits, additional value); non-compete and non-solicitation enforceability in the post-employment context (CA/MN/ND/OK bans, FTC rule vacatur Aug 2024); non-disparagement and confidentiality compliance under NLRB McLaren Macomb (2023) and SEC Rule 21F-17(a) whistleblower anti-impediment rules; protected-rights carve-out completeness (EEOC charge filing, SEC/CFTC whistleblower awards, workers' compensation, unemployment, ERISA vested benefits); cooperation obligation scope and duration; return of property; reference provisions; state-specific restrictions on NDA/non-disparagement for harassment and discrimination claims (CA SB 331, WA HB 1795, NY S.B. 4516, NJ Supreme Court 2024, IL HB 3638). Produces GREEN/YELLOW/RED classification with confidence-scored employer-exposure findings and Glass Box audit trail. Jurisdiction: US-primary with [JURISDICTION-SPECIFIC] markers for UK, Australia, EU, and Canada.


# Legalcode Severance Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of severance
> and separation agreements. It does not constitute legal advice. All outputs require
> review by a qualified employment lawyer licensed in the relevant jurisdiction(s) before
> relying on them for any employment, compliance, enforcement, or litigation decision.
> Employment law — especially OWBPA consideration-period rules, state non-compete bans,
> and NLRB guidance — changes frequently; verify current applicability before acting.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources, including EEOC guidance and applicable state statutes,
> before relying on them. This skill does not substitute for individual legal advice
> about a specific employee's situation or an employer's specific severance program.

---

## Purpose and Scope

This skill reviews severance, separation, release, and departure agreements clause by
clause. It identifies provisions that create employer liability, invalidate the ADEA
waiver, or conflict with mandatory legal requirements. It classifies each issue as
GREEN (legally sufficient), YELLOW (legally questionable / needs revision), or RED
(legally invalid / creates liability), produces actionable remediation language, and
generates a Glass Box audit trail.

**Covers:**

- OWBPA/ADEA compliance analysis — the full 7-factor knowing-and-voluntary test
  (29 U.S.C. § 626(f)); 21-day vs. 45-day consideration period determination;
  non-waivable 7-day revocation period; group termination written disclosure
  (ages and job titles of all selected and non-selected employees in the decisional unit)
- Release of claims scope — breadth, overbreadth, EEOC/government agency carve-outs,
  California § 1542 unknown-claims waiver, future-claims prohibition, FLSA waivers
- Consideration adequacy — separation pay vs. wages already owed, ERISA vested benefits,
  timing of execution (pre- vs. post-termination), and additional value analysis
- Non-compete and non-solicitation enforceability in the severance context — ban-state
  screening (CA, MN, ND, OK), separate-consideration requirement, FTC rule status,
  blue-pencil / reformation doctrine, garden leave
- Non-disparagement and confidentiality provisions — McLaren Macomb (NLRB 2023)
  compliance, defamation-standard limitation, protected-activity carve-outs, SEC Rule
  21F-17(a) anti-impediment requirements, state NDA restrictions for discrimination
  and harassment claims (CA, WA, NY, NJ, IL)
- Protected-rights carve-out completeness — EEOC charge filing, SEC/CFTC/FINRA
  whistleblower rights and award entitlement, workers' compensation, unemployment,
  vested ERISA benefits, NLRA Section 7 rights
- Cooperation obligations — scope, duration, compensation, privilege protection
- Return of property and reference provisions
- Governing law, forum selection, and dispute resolution enforceability
- Employer exposure quantification — aggregate risk from defective provisions

**Does not:**

- Draft severance agreements from scratch (this skill reviews; for drafting see
  `legalcode-employment-agreement-review` or specialist drafting tools)
- Provide legal advice or replace qualified employment counsel
- Guarantee enforceability — courts apply multi-factor tests that vary by jurisdiction
  and specific facts
- Assess WARN Act compliance, payroll tax, or Section 409A deferred compensation
  treatment in detail (flag for specialist review)
- Cover collective bargaining agreement (CBA) separation provisions

**Related skills:** `legalcode-employment-agreement-review` (full employment agreement
review including severance triggers), `legalcode-non-compete-enforceability`
(standalone 50-state non-compete enforceability matrix), `legalcode-employee-handbook-
review` (handbook-level severance policy audit), `legalcode-internal-investigation`
(investigations that may lead to separation agreements).

---

## Jurisdiction and Governing Law

**Primary jurisdiction: United States.** This skill contains detailed US federal and
state analysis. Core OWBPA/ADEA requirements apply to all US employers with 20 or more
employees covering employees aged 40 and older.

**US jurisdiction determination (perform at Step 4):**

1. Identify the agreement's stated choice of law
2. Identify the employee's primary work state
3. Identify where the employer is incorporated
4. Note: For restrictive covenants and NDA restrictions, the employee's work state
   typically overrides the contractual choice of law in most US jurisdictions

[JURISDICTION-SPECIFIC] **United Kingdom**: Severance agreements are called "settlement
agreements" (Employment Rights Act 1996 s.111A). Statutory minimum notice (ERA 1996
ss.86-91) and statutory redundancy pay (ERA 1996 ss.135-145) must be paid regardless
of any contractual release. A settlement agreement must be in writing, relate to a
particular complaint, be signed by both parties, and the employee must receive
independent legal advice from a qualified adviser. Research: ERA 1996, ACAS Code of
Practice on Settlement Agreements.

[JURISDICTION-SPECIFIC] **Australia**: Unfair dismissal settlement (Fair Work Act 2009
(Cth) ss.388-399); general protections conciliation (FWA ss.365-374). Minimum
entitlements under the National Employment Standards (FWA ss.61-131) cannot be
contracted out of. Research: Fair Work Commission guidance.

[JURISDICTION-SPECIFIC] **European Union**: Employment termination agreements vary by
member state. EU minimum notice, collective dismissal consultation (Directive 98/59/EC),
and transfer of undertakings (TUPE Directive 2001/23/EC) rights cannot be waived.
Research applicable member state employment law.

[JURISDICTION-SPECIFIC] **Canada**: Federal employees (Canada Labour Code) and
provincially regulated employees have separate statutory frameworks. Quebec requires
French-language agreements. Research: applicable provincial employment standards acts.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer changes which OWBPA track applies (21-day individual vs. 45-day group)
- The employee's age determines whether OWBPA requirements apply at all
- The perspective (employer drafting/reviewing vs. employee evaluating) changes the
  framing of every classification
- Jurisdiction determines applicable state-law restrictions on releases, non-competes,
  and NDAs

Mark each pause point in the workflow with **⟁ CLARIFY**. If the user has already
provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Agreement

Accept the severance or separation agreement in any format:

- **File**: PDF, DOCX, or other document
- **URL**: Link to a document in a CLM, cloud storage, or document management system
- **Pasted text**: Agreement text pasted directly into the conversation

If no document is provided, prompt: "Please share the severance or separation agreement
text or file you'd like reviewed."

---

### Step 2: Gather Initial Context

**⟁ CLARIFY** — Before beginning, gather context with these structured questions (skip
questions already answered by the user's initial prompt):

1. **Your perspective:**
   - Options: **Employer (drafting or reviewing the offer)**, Employee (evaluating
     whether to sign), Legal counsel (audit or litigation review), HR compliance audit
   - _Why this matters_: Every classification flips depending on which side you represent.
     What protects an employer creates risk for an employee and vice versa.

2. **Separation type:**
   - Options: **Involuntary termination / RIF / layoff**, Involuntary — performance /
     cause, Voluntary resignation with severance, Change of control / acquisition,
     Mutual separation / negotiated departure, Early retirement program
   - _Why this matters_: Determines whether the OWBPA 45-day group track or 21-day
     individual track applies; whether WARN Act obligations are triggered.

3. **Employee age:**
   - Options: **Age 40 or older (OWBPA applies)**, Under 40 (OWBPA does not apply),
     Age unknown or multiple employees with varying ages
   - _Why this matters_: OWBPA requirements only apply to employees aged 40+. If the
     employee is under 40, many of the most technical requirements (consideration periods,
     revocation window, group disclosure) do not apply, though a valid general release
     still requires adequate consideration and proper scope.

4. **Individual vs. group program:**
   - Options: **Single employee (individual termination)**, Group of two or more
     employees offered same program (RIF/exit incentive), Exit incentive / early
     retirement program offered to a class of employees, Uncertain
   - _Why this matters_: Group or exit incentive programs trigger the **45-day**
     consideration period and detailed written group disclosure requirements under
     29 U.S.C. § 626(f)(1)(H). Individual terminations trigger only the 21-day period.

5. **Primary jurisdiction(s):**
   - Options: **Single US state (specify which)**, Multiple US states (specify which),
     US federal contractor, United Kingdom, Australia, EU member state, Canada,
     Multi-jurisdictional / global
   - _Why this matters_: State choice of law governs non-compete enforceability, NDA
     restrictions for harassment/discrimination claims, and state-specific consideration
     requirements for releases.

---

### Step 3: Load Organizational Playbook (Optional)

**⟁ CLARIFY** — If reviewing from an employer perspective:
"Do you have an organization-standard severance template, playbook, or market-position
document for severance terms? If so, provide it and I will compare this agreement against
your standard positions."

If no playbook provided, proceed using:

- OWBPA statutory minimums as the floor (not the market standard)
- General market practice for each provision type, described below
- State the assumption explicitly: "Reviewing against legal requirements and general
  US market practice. No organization-specific playbook was provided."

---

### Step 4: Initial Scan — Trigger Identification

Before clause-by-clause analysis, scan the document and identify:

**OWBPA trigger check:**

- [ ] Is any releasing party aged 40 or older? → OWBPA analysis is MANDATORY
- [ ] Are two or more employees being offered the same program? → 45-day track applies
- [ ] Is an "exit incentive or other employment termination program" referenced? → 45-day track
- [ ] Note the exact consideration period stated in the agreement
- [ ] Identify the revocation period language (or absence thereof)

**Key provisions inventory:**

- [ ] Release of claims — identify scope (specific claims enumerated vs. general)
- [ ] Consideration — identify what is being provided (amount, benefits, services)
- [ ] Non-compete / non-solicitation — identify duration, geographic scope, activity scope
- [ ] Non-disparagement — identify breadth, carve-outs, directional scope (mutual vs. one-way)
- [ ] Confidentiality — identify scope, duration, permitted disclosures
- [ ] Cooperation obligation — identify scope, duration, compensation
- [ ] Return of property — identify scope and certification requirement
- [ ] Reference provision — identify commitment (neutral, letter, factual only)
- [ ] Protected rights carve-outs — identify which carve-outs are present or absent
- [ ] Governing law and forum — identify choice of law state and dispute resolution mechanism
- [ ] Section 409A compliance language — flag if structured as deferred compensation

**⟁ CLARIFY** — If the employee's age is not clear from the agreement and the user
indicated uncertainty in Step 2: "Is the releasing employee aged 40 or older? This
determines whether OWBPA requires a specific consideration period and 7-day revocation
right."

---

### Step 5: OWBPA / ADEA Compliance Analysis

_This is the highest-risk analysis step. A defective OWBPA waiver renders the entire
ADEA release void — the employer has paid severance but retains full ADEA exposure.
Under Oubre v. Entergy Operations, 522 U.S. 422 (1998), the employee need not tender
back the severance before suing._

Skip this step only if the employee is confirmed under age 40.

#### 5A: Individual vs. Group Track Determination

**Individual track (21-day consideration period):**
Applies when a single employee — not part of a standardized exit incentive or employment
termination program — is offered the agreement.

**Group track (45-day consideration period + written group disclosure):**
Applies when an "exit incentive or other employment termination program" is offered to a
"group or class of employees." In practice: two or more employees offered the same
standardized program.

- An "exit incentive program" includes voluntary early retirement windows
- An "other employment termination program" includes standardized RIF severance packages
- Whether a one-employee-at-a-time RIF triggers the group track is fact-specific;
  consult EEOC guidance and 29 C.F.R. § 1625.22(f)

**If the agreement states the wrong period:** Classify as RED — the ADEA waiver is void.

#### 5B: The Seven Statutory Factors (29 U.S.C. § 626(f)(1))

Evaluate each factor. Any single failure renders the ADEA waiver void.

**Factor 1 — Plain language:**
Is the waiver written "in a manner calculated to be understood by the individual, or by
the average individual eligible to participate"? Flag complex legalese that an average
non-lawyer would not understand.

- GREEN: Agreement uses plain, clear language; defined terms explained
- YELLOW: Moderate legalese; potentially confusing to lay reader
- RED: Dense legal jargon with no plain-language explanation; technical terms undefined

**Factor 2 — ADEA-specific reference:**
Does the waiver "specifically refer to rights or claims arising under the [Age
Discrimination in Employment Act of 1967]"? The EEOC requires the full statutory name
or at minimum clear identification of the ADEA. Generic language releasing "all
discrimination claims" is insufficient.

- GREEN: ADEA identified by full name or statute citation in release clause
- YELLOW: Age discrimination referenced but ADEA not named; potentially insufficient
- RED: No ADEA reference; only generic "all claims" or "all discrimination claims"

**Factor 3 — No future-claims waiver:**
Does the release carve out "rights or claims that may arise after the date the waiver
is executed"? Any language releasing future claims violates OWBPA.

- GREEN: Explicit carve-out for claims arising after signing date
- YELLOW: Ambiguous — release of "all claims through the date of this Agreement" may
  or may not be read as limiting to past claims; recommend explicit future-claims carve-out
- RED: Release purports to cover future claims or has no temporal limitation at all

**Factor 4 — Adequate consideration:**
Is the waiver "in exchange for consideration in addition to anything of value to which
the individual already is entitled"? Wages already earned, accrued vacation in states
that mandate payout (CA, IL, CO, MA), and vested ERISA benefits are not adequate
consideration. See Step 7 for full consideration adequacy analysis.

- GREEN: Provides separation pay, extended benefits, or other value beyond statutory
  minimums and any amounts already owed
- YELLOW: Consideration is borderline (e.g., only an amount close to what the employee
  might argue they were owed under a disputed bonus); needs analysis of employment agreement
- RED: Consideration consists entirely of wages already earned or benefits already vested

**Factor 5 — Written advice to consult attorney:**
Does the waiver "advise the individual in writing to consult with an attorney prior to
executing the agreement"? This language must appear in the agreement itself, not just
be communicated verbally.

- GREEN: Clear written statement in the agreement advising the employee to consult counsel
- YELLOW: Advisory language buried in fine print or in a cover letter (not the agreement)
- RED: No written advice to consult attorney appears anywhere in the document

**Factor 6 — Consideration period:**

- Individual termination: at least **21 calendar days** to consider
- Group / exit incentive / other employment termination program: at least **45 calendar
  days** to consider
- Period runs from date of employer's final offer; material changes restart the clock
- Employee may choose to sign early (voluntarily), but employer may not pressure or
  condition benefits on early signing

Classify:

- GREEN: Correct period (21 or 45 days) stated; no indication of coercion to sign early
- YELLOW: Period is correct but agreement includes incentive to sign early (e.g., bonus
  for signing within 10 days); creates coercion risk
- RED: Incorrect period (e.g., 21 days stated in a group RIF, or 14 days stated for
  an individual termination); no period stated at all

**Factor 7 — 7-day revocation period:**
The agreement must provide that "for a period of at least 7 days following the execution
of such agreement, the individual may revoke the agreement, and the agreement shall not
become effective or enforceable until the revocation period has expired."

- This 7-day period is **non-waivable and cannot be shortened** — even at the employee's
  own request (29 C.F.R. § 1625.22(e)(6); confirmed post-Oubre)
- The agreement may not become effective or effective before day 8
- Classify:
  - GREEN: 7-day revocation right stated; effective date conditioned on expiration;
    revocation period not subject to waiver
  - YELLOW: 7-day revocation stated but effective date language is ambiguous
  - RED: Revocation period is less than 7 days; revocation period is waivable; no
    revocation right stated at all; agreement purports to be effective upon signing

#### 5C: Group Termination Informational Disclosure (29 U.S.C. § 626(f)(1)(H))

_This section applies only to group / exit incentive / RIF programs._

The employer must provide written disclosure — at the commencement of the consideration
period — containing all of the following:

1. **Decisional unit**: Description of the class, unit, or group of employees covered
   (e.g., "All employees in the Marketing Department at the Austin, TX office")
2. **Eligibility factors**: Criteria used to select employees for the program
   (e.g., "Selection based on performance ratings and business needs")
3. **Time limits**: Applicable time limits (45-day consideration period, 7-day revocation)
4. **Selected employees — job titles and ages**: Of all individuals within the decisional
   unit who were selected for the program (or who are eligible for the exit incentive)
5. **Non-selected employees — job titles and ages**: Of all individuals within the
   decisional unit who were NOT selected for the program

**Critical nuances:**

- If the RIF draws from a subset of a larger unit, disclosure must cover the **entire
  decisional unit** — not just those selected (Kruchowski v. Weyerhaeuser Co.)
- Non-U.S. citizen employees working outside the U.S. need not be included (EEOC, 2021)
- The disclosure must be provided at the start of the period; it cannot be provided later
  to cure a defect in the original agreement (no post-hoc cure)
- Failure to identify the decisional unit or the eligibility factors is a common, fatal
  error (Pagilio v. Guidant Corp.; Kruchowski v. Weyerhaeuser Co.)

Classify each required disclosure element:

- GREEN: Disclosure present, complete, properly identifies all required elements
- YELLOW: Disclosure present but incomplete (e.g., decisional unit unclear, or job
  titles provided without ages)
- RED: Required disclosure missing entirely; decisional unit not identified; ages or
  titles of non-selected employees absent

---

### Step 6: Release of Claims Scope Analysis

#### 6A: Scope Breadth Review

Identify which claims are released. Common release scope:

- Federal discrimination claims: Title VII, ADA, ADEA (must be OWBPA-compliant for age
  40+ employees), GINA, Pregnancy Discrimination Act, Rehabilitation Act
- Federal wage claims: FLSA (contested — see below)
- State employment claims: State anti-discrimination statutes, state wage payment laws,
  wrongful discharge in violation of public policy
- Contract claims: Breach of employment agreement, promissory estoppel
- Tort claims: Defamation, negligent supervision, intentional infliction of emotional distress

**FLSA release — high-risk area [VERIFY — evolving]:**
The traditional rule (Lynn's Food Stores v. United States, 679 F.2d 1350 (11th Cir.
1982)) requires DOL supervision or court approval for a valid FLSA release. Without this,
private waiver of FLSA claims is unenforceable in most circuits. Flag FLSA waiver
language for specialist review and advise that court-approved or DOL-supervised
settlement may be needed to extinguish FLSA claims.

**Unknown claims waiver (California):**
If any California nexus exists (California employee, California employer, California
choice of law), the agreement must include an express waiver of California Civil Code
§ 1542 to release unknown claims. The 2019-amended statutory language must be used
verbatim. Absence of § 1542 language means unknown claims are not released under
California law. Classify missing § 1542 waiver in any California-nexus agreement as RED.

#### 6B: Required Carve-Outs — Non-Waivable Rights

The following rights cannot be released. Classify the absence of these carve-outs as
RED if the agreement's release language is broad enough to encompass them without an
express reservation:

| Right                                                | Authority                                         | Classification if Absent                                       |
| ---------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| Right to file EEOC charge                            | 42 U.S.C. § 2000e-5; EEOC guidance                | RED — release of EEOC charge-filing right is void              |
| Right to participate in EEOC proceedings             | EEOC guidance                                     | RED — conditioning severance on non-participation is void      |
| Right to testify/assist in EEOC/agency investigation | EEOC guidance                                     | RED                                                            |
| SEC/CFTC/FINRA whistleblower reporting rights        | Dodd-Frank § 922; Rule 21F-17(a)                  | RED — see Step 9                                               |
| Right to receive SEC/CFTC/FINRA whistleblower award  | Rule 21F-17(a); SEC enforcement actions 2023-2024 | RED — award waiver is an independent violation                 |
| Workers' compensation claims                         | State statutes (state-specific)                   | RED in states prohibiting waiver; [JURISDICTION-SPECIFIC]      |
| Unemployment compensation rights                     | State UI statutes                                 | YELLOW → RED (conditioning on forfeiture)                      |
| Vested ERISA pension/retirement benefits             | ERISA, 29 U.S.C. § 1001                           | RED                                                            |
| Claims arising after signing date                    | OWBPA § 626(f)(1)(C)                              | RED (OWBPA-specific for ADEA; also general contract principle) |
| NLRA Section 7 rights (current law)                  | McLaren Macomb, 372 NLRB No. 58 (2023)            | YELLOW → RED depending on breadth; see Step 9                  |

**Note on EEOC monetary recovery:** An employee CAN waive the right to individual
monetary recovery in a private EEOC-related lawsuit — the carve-out is specifically
for the right to FILE a charge or participate in agency proceedings. The agreement may
state that the employee waives any personal monetary award from claims the EEOC files
on their behalf, provided the right to participate in EEOC proceedings is preserved.
Per EEOC v. Waffle House, 534 U.S. 279 (2002), the EEOC is not bound by the private
release in any event.

#### 6C: Temporal Limitations and Future Claims

Any general release should be limited to claims "through the date of the Agreement" or
"through the Termination Date." Language purporting to release future conduct or claims
is unenforceable for ADEA claims (OWBPA violation) and of questionable enforceability
for other claims under general public policy principles.

---

### Step 7: Consideration Adequacy Analysis

#### 7A: What Constitutes Adequate Consideration

For a release to be enforceable, the employee must receive something of value they are
**not already entitled to receive**. Classify inadequate consideration as RED.

**Adequate consideration (examples):**

- Separation pay in excess of any contractually or policy-guaranteed severance
- COBRA premium subsidy beyond statutory minimum
- Outplacement services
- Extended equity vesting or extended post-termination exercise windows
- Neutral reference agreement (if not otherwise owed)
- Non-disparagement from the employer (if mutual)
- Continued health or life insurance

**Insufficient consideration — classify as RED:**

- Wages already earned for hours worked (cannot be withheld to coerce signing)
- Accrued vacation pay that state law requires to be paid out (California, Illinois,
  Colorado, Massachusetts, and others — [JURISDICTION-SPECIFIC] verify per state)
- Vested ERISA pension benefits, 401(k) employer match already vested
- Benefits the employee was already entitled to under a written policy that did not
  condition payment on signing a release
- Amounts already owed under a prior employment agreement's severance formula

**OWBPA additional consideration requirement (age 40+ employees):**
OWBPA Factor 4 expressly requires that ADEA-waiver consideration be "in addition to
anything of value to which the individual already is entitled." This is a statutory
requirement, not merely a general contract law principle. Failure results in RED/void
ADEA waiver even if the consideration would be adequate for non-ADEA releases.

#### 7B: Timing Considerations

**Pre-termination signing:**
If the employee signs the agreement before their last day of employment, the release
typically covers conduct through the signing date. Any discrimination or other claims
arising after signing but before the termination date are not released.

- Recommend: A reaffirmation provision (employee reaffirms the release after the
  termination date, with a new consideration period)
- Alternatively: Ensure the signing date is on or after the last day of employment

**At-will employees:**
For at-will employees, the promise of severance pay constitutes valid consideration
even without a contractual right to severance — because the employer could have
terminated without paying anything.

**Section 409A caution [flag for specialist]:**
Severance structured as salary continuation over more than two years, or conditioned
on signing within 90 days of termination with a specific payment schedule, may implicate
26 U.S.C. § 409A deferred compensation rules. Flag for tax counsel review.

---

### Step 8: Restrictive Covenants Analysis

_In the severance context, non-compete and non-solicitation obligations introduced
at termination require special analysis. If the employee already agreed to these
covenants in their employment agreement, this step verifies enforceability of that
prior agreement's terms given termination._

#### 8A: State Enforceability — Ban State Screening

Screen first for absolute ban states. Any non-compete or non-solicitation clause
subject to these states' laws (or where the employee works) is presumptively void:

| State            | Authority                   | Effective Date                                    | Key Rule                                                                                                                                                                                                         |
| ---------------- | --------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **California**   | Bus. & Prof. Code § 16600   | Longstanding; strengthened AB 1076 (Jan. 1, 2024) | Near-total ban; non-competes in any agreement are void; choice-of-law clauses designed to circumvent CA law also void; SB 699 (Jan. 1, 2024) allows employees to sue for damages if employer attempts to enforce |
| **Minnesota**    | Minn. Stat. § 181.988       | July 1, 2023                                      | Prohibits non-competes in all employment-related agreements including separation/severance; employee may recover attorneys' fees; choice-of-law clauses cannot circumvent                                        |
| **North Dakota** | N.D.C.C. § 9-08-06          | Longstanding                                      | Non-competes void except narrow sale-of-business exception                                                                                                                                                       |
| **Oklahoma**     | Okla. Stat. tit. 15, § 219A | Longstanding                                      | Non-competes void; non-solicitation may be limited                                                                                                                                                               |

For other states, apply `legalcode-non-compete-enforceability` for the full 50-state
enforceability matrix. Summarize key findings here:

- Duration: assess reasonableness (6-12 months generally more defensible; 24+ months
  increasingly disfavored)
- Geographic scope: narrower is more defensible; nationwide restrictions face heightened
  scrutiny for most roles
- Activity scope: "competitive business" is overbroad; narrow by product line, role,
  or customer contact

**FTC Non-Compete Rule [current status — vacated]:**
The FTC's April 2024 final rule banning nearly all non-competes was vacated on August 20,
2024 (Ryan LLC v. FTC, N.D. Tex.). The FTC has pivoted to case-by-case enforcement
targeting low-wage workers. Non-competes remain governed by state law as of March 2026.

#### 8B: Separate Consideration Requirement

When a non-compete or non-solicitation obligation is first introduced (or materially
strengthened) in a severance agreement that the employee did not previously agree to,
courts in most states require "separate" or "independent" consideration beyond the
right to receive severance. The consideration supporting the release does not
automatically support a new restrictive covenant.

Classify a new restrictive covenant introduced in the severance agreement without
identified separate consideration as YELLOW in most states, RED in states that have
addressed this explicitly.

**Massachusetts additional requirement:**
Under Mass. G.L. c. 149 § 24L (eff. October 1, 2018), non-competes must be supported
by "garden leave" (at least 50% of base salary for the restricted period) or
"other mutually agreed upon consideration." A separation-only payment may not satisfy
this requirement.

#### 8C: Reformation Doctrine

- **Blue-pencil states** (NY, TX, and others): Courts strike overbroad terms and enforce
  the remainder. Overbroad covenants may be partially enforced.
- **Red-pencil states** (CA, MT, ND, and others): Courts void overbroad covenants
  entirely. No reformation.
- **Reformation/modification states** (GA, FL, and others): Courts may rewrite overbroad
  covenants to make them reasonable.

---

### Step 9: Non-Disparagement and Confidentiality Analysis

#### 9A: McLaren Macomb Compliance (Current Law — See Footnote)

**Current law:** McLaren Macomb, 372 NLRB No. 58 (Feb. 21, 2023) holds that the
**mere proffer** of a severance agreement with broad non-disparagement or confidentiality
provisions violates Section 8(a)(1) of the NLRA if those provisions have a "reasonable
tendency" to interfere with Section 7 rights.

**Lawful (per GC Memo GC 23-05, March 2023):**

- Non-disparagement clauses limited to statements meeting the **defamation standard**:
  statements made with knowledge of falsity or reckless disregard for truth
  ("maliciously untrue" statements)
- Confidentiality clauses "narrowly-tailored to restrict the dissemination of
  proprietary or trade secret information for a period of time based on legitimate
  business justifications"
- Provisions applicable only to supervisors and managers (who generally lack Section 7
  rights — [VERIFY: supervisory status is fact-specific])

**Unlawful — classify as RED under current law:**

- Broad non-disparagement clause prohibiting "any statements" that could "harm the image"
  of the employer, without carve-out for protected activity
- Confidentiality clause prohibiting disclosure of the agreement's existence or terms
  without permitting disclosure to union representatives, NLRB, government agencies,
  or for purposes of enforcing the agreement itself
- Any clause that conditions receipt of severance on employee refraining from
  assisting coworkers in concerted activity or NLRB proceedings

**Political trajectory footnote:** The Trump administration's NLRB Acting General
Counsel rescinded GC 23-05 in early 2025. The Board currently lacks a full quorum
needed to formally overrule McLaren Macomb. As of March 2026, McLaren Macomb remains
binding Board precedent. Employers and employee-side counsel should monitor for formal
reversal; agreements tendered in 2023–2025 without McLaren Macomb carve-outs carry
heightened unfair labor practice risk under current law.

#### 9B: SEC Whistleblower Rule 17 C.F.R. § 240.21F-17(a)

"No person may take any action to impede an individual from communicating directly
with the Commission staff about a possible securities law violation, including enforcing
or threatening to enforce a confidentiality agreement."

**2023–2024 SEC enforcement sweep:** Seven companies simultaneously charged in September
2024; combined penalties exceeded $3 million. The SEC found violations where:

- The agreement required the employee to waive the right to receive an SEC whistleblower
  award (even if the right to "participate" in SEC proceedings was preserved)
- The agreement required the employee to notify the employer **before** contacting any
  government agency (the prior-notification requirement itself impedes reporting)
- The agreement included broad "no pending claims" representations inconsistent with
  pending or contemplated government reporting

**Required analysis:**

- [ ] Does the agreement require prior employer notification before SEC/CFTC/FINRA contact?
      → RED (impedes reporting)
- [ ] Does the agreement waive the right to receive a government whistleblower award?
      → RED (award waiver = independent violation per 2023-2024 enforcement actions)
- [ ] Does the agreement contain a broad confidentiality clause that could be read to
      prohibit SEC/CFTC/FINRA reporting? → YELLOW without carve-out; RED if enforced
- [ ] Is an affirmative carve-out present permitting reporting to government agencies?
      → GREEN if present and covers both participation AND award eligibility

#### 9C: State-Specific NDA Restrictions for Discrimination / Harassment Claims

Screen for any nexus with the following jurisdictions:

| Jurisdiction   | Authority                                                        | Key Rule                                                                                                                                                                                                                                                              |
| -------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **California** | SB 331 ("Silenced No More Act," eff. Jan. 1, 2022)               | NDAs prohibited for all claims of workplace harassment, discrimination, or retaliation on any protected basis; non-disparagement provisions must include mandatory carve-out language; employee must have at least 5 business days to consider a settlement agreement |
| **Washington** | HB 1795 ("Silenced No More Act," eff. June 9, 2022)              | Broadest state law — prohibits NDAs covering harassment, discrimination, sexual assault, AND wage/hour violations; civil penalty: minimum $10,000 per violation plus additional damages; no exception for post-dispute negotiated settlements                         |
| **New York**   | S.B. 4516, amending Gen. Oblig. Law § 5-336 (eff. Nov. 17, 2023) | 21 days to consider; 7-day revocation; right to consult attorney; agreements cannot require employee to keep confidential the underlying facts of discrimination/harassment; if confidentiality is required, it must be the employee's choice, not the employer's     |
| **New Jersey** | Savage v. Township of Neptune (NJSC, May 2024)                   | Non-disparagement provisions cannot have the effect of concealing details about discrimination, retaliation, or harassment claims; must be "narrowly drafted and limited to matters unrelated" to such claims                                                         |
| **Illinois**   | HB 3638 (eff. Jan. 1, 2026)                                      | Expanded Illinois Workplace Transparency Act; broadened employee speech protections; strengthened restrictions on choice-of-law clauses designed to circumvent IL protections                                                                                         |
| **Federal**    | Speak Out Act (Pub. L. 117-228, Dec. 7, 2022)                    | Pre-dispute NDAs and non-disparagement clauses covering **sexual assault and sexual harassment** are unenforceable for claims under the Act; does not cover post-dispute settlement NDAs                                                                              |

**Classify:**

- An agreement with broad non-disparagement or confidentiality covering discrimination/
  harassment in any of these jurisdictions without the required carve-outs: RED
- An agreement that conditions severance payment on maintaining confidentiality about
  underlying harassment/discrimination facts in California or Washington: RED
- An agreement reviewed under NY law that gives the employee fewer than 21 days to
  consider: YELLOW (mirrors OWBPA; may be independent violation)

---

### Step 10: Cooperation Obligations Analysis

Review the cooperation clause scope:

**Duration:** Does the clause have a defined end date?

- GREEN: Defined duration (12-24 months) or limited to specifically identified pending matters
- YELLOW: Broad cooperation obligation without time limit but scoped to matters the
  employee was personally involved in
- RED: Indefinite, unlimited cooperation obligation with no defined scope

**Scope:** What is the employee required to do?

- Typical and generally enforceable: Provide information, sit for interviews, assist
  with business transition for matters the employee personally handled
- Potentially overbroad: Required to attend trials, hearings, or depositions without
  adequate expense reimbursement or compensation; required to cooperate with matters
  wholly unrelated to the employee's former responsibilities

**Compensation:** Is the employee compensated for cooperation time?

- GREEN: Reasonable hourly rate or day rate for time spent beyond information calls;
  all reasonable expenses reimbursed
- YELLOW: Expenses reimbursed but no compensation for time; acceptable for
  lower-seniority employees but problematic for executives
- RED: No expense reimbursement provision; employee bears own costs

**Privilege protection:** Does the clause explicitly exclude protected attorney-client
communications?

- GREEN: Express carve-out for privileged communications
- YELLOW: No mention of privilege (common); flag but not per se fatal
- RED: Clause purports to require disclosure of privileged communications

---

### Step 11: Return of Property and Reference Provisions

**Return of property:**

- [ ] Scope: Does the clause identify what property must be returned (laptops, badges,
      client lists, confidential information, company credit cards)?
- [ ] Timing: Is a specific return date or process stated?
- [ ] Certification: Does the employee certify they have returned all property and
      have not retained copies of confidential information?
- GREEN: Scope defined, timing clear, certification included
- YELLOW: Property return obligation stated but timing ambiguous; no certification
- RED: No return of property provision where the employee had significant access to
  confidential information or physical property

**Reference provision:**

- [ ] What commitment does the employer make? (Neutral reference — title/dates/salary
      only; positive reference; reference letter)
- [ ] Is the reference commitment mutual? Does the employee agree to direct inquiries
      to a specific contact?
- [ ] Does the employer's commitment bind only HR or also the employee's former manager?
- GREEN: Specific reference commitment with named contact; employee obligation stated
- YELLOW: Vague "best efforts" to provide neutral reference; no enforcement mechanism
- RED: No reference provision in circumstances where the employer's negative verbal
  references could constitute actionable defamation or tortious interference

---

### Step 12: Protected Rights Carve-Out Completeness Check

Perform a final carve-out completeness scan against this checklist:

| Required Carve-Out                                        | Present | Classification if Absent                          |
| --------------------------------------------------------- | ------- | ------------------------------------------------- |
| Right to file EEOC/NLRB/DOL/state agency charge           | ☐       | RED                                               |
| Right to participate in agency investigations/proceedings | ☐       | RED                                               |
| Right to communicate with/report to SEC/CFTC/FINRA        | ☐       | RED                                               |
| Right to receive SEC/CFTC/FINRA whistleblower award       | ☐       | RED                                               |
| Workers' compensation rights (state-specific)             | ☐       | RED                                               |
| Unemployment compensation rights                          | ☐       | YELLOW→RED                                        |
| Vested ERISA pension/retirement benefits                  | ☐       | RED                                               |
| Future claims (claims arising after signing)              | ☐       | RED (ADEA) / YELLOW (general)                     |
| NLRA Section 7 rights (current law)                       | ☐       | RED (McLaren Macomb)                              |
| Rights that may not be waived by law                      | ☐       | YELLOW (catch-all; confirm jurisdiction-specific) |

---

### Step 13: Governing Law and Dispute Resolution

**Choice of law:**

- Identify the chosen state law
- Determine whether the chosen state permits choice-of-law override for restrictive
  covenant enforcement
- California, Minnesota, and Washington generally override contractual choice-of-law
  clauses for non-competes and NDA restrictions when the employee works in those states

**Arbitration clause:**

- Assess whether the arbitration clause is mutual
- Check whether the **Ending Forced Arbitration of Sexual Assault and Sexual Harassment
  Act** (Pub. L. 117-90, eff. March 3, 2022) applies — if the employee is releasing
  sexual assault or sexual harassment claims, a pre-dispute arbitration clause is
  unenforceable for those claims (the employee may elect to bring those claims in court)
- Assess whether the arbitration clause impermissibly restricts government agency charge
  filing rights

**Forum selection:**

- Note whether the chosen forum is in a ban state for restrictive covenants
- Note whether venue is distant from the employee's home location (potential
  enforcement burden)

---

### Step 14: Employer Exposure Assessment

Synthesize findings into an employer-exposure summary:

**ADEA/OWBPA exposure (if any OWBPA factor failed):**
Under Oubre v. Entergy, 522 U.S. 422 (1998), a defective OWBPA waiver is void. The
employer has paid severance but retained full ADEA liability. The employee need not
tender back the severance before suing. Quantify:

- Potential remedies: back pay, front pay, liquidated damages (double back pay for
  willful violations), attorneys' fees, reinstatement
- Statutory period: 180 days to file EEOC charge (300 days in deferral states)

**Non-disparagement/confidentiality NLRA exposure:**
Under McLaren Macomb, the mere proffer of a noncompliant agreement is an unfair labor
practice. Remedies include cease-and-desist order, posting notice, potential
modification/rescission of executed agreements. Cannot condition severance payment
on a void clause.

**SEC Rule 21F-17 exposure:**
Civil penalty per violation. SEC has levied penalties of $175,000–$750,000 per company
in 2023-2024 enforcement actions. Analysis of the agreement against the SEC's enforcement
patterns produces a High / Medium / Low 21F-17 exposure signal.

**State NDA restriction exposure:**
Washington HB 1795: minimum $10,000 civil penalty per violation, plus actual damages.
California SB 331: agreement is unenforceable; employee may obtain injunctive relief
and attorneys' fees.

---

### Step 15: Quality Verification

Before delivering output, apply the Citation Quality Gates, Self-Interrogation, and
Confidence Scoring frameworks (see below). Ensure all RED findings survive the
3-pass Self-Interrogation. Confirm all [JURISDICTION-SPECIFIC] markers are correctly
placed.

---

## OWBPA Quick Reference Matrix

| OWBPA Requirement                              | Individual Termination                        | Group / RIF / Exit Incentive                                               |
| ---------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------- |
| **Consideration period**                       | 21 calendar days                              | 45 calendar days                                                           |
| **Revocation period**                          | 7 days (non-waivable)                         | 7 days (non-waivable)                                                      |
| **Written advice to consult attorney**         | Required                                      | Required                                                                   |
| **ADEA named by statute in release**           | Required                                      | Required                                                                   |
| **No future-claims waiver**                    | Required                                      | Required                                                                   |
| **Adequate consideration beyond already owed** | Required                                      | Required                                                                   |
| **Group informational disclosure**             | Not required                                  | Required (job titles + ages: selected AND non-selected in decisional unit) |
| **Material change restarts clock**             | Yes                                           | Yes                                                                        |
| **Revocability**                               | Non-waivable                                  | Non-waivable                                                               |
| **Effective date**                             | Day 8 (after 7-day revocation period expires) | Day 8 (after 7-day revocation period expires)                              |

---

## GREEN / YELLOW / RED Classification System

### GREEN — Legally Sufficient

All of the following apply:

- All applicable OWBPA factors satisfied (if employee is age 40+)
- Required carve-outs for non-waivable rights are present and complete
- Consideration is genuinely additional to anything already owed
- Non-disparagement and confidentiality provisions comply with current NLRB precedent
  and SEC Rule 21F-17(a)
- Release scope is appropriate (not overbroad, does not include future claims)
- No restrictive covenant in a ban state or without adequate consideration
- Cooperation obligations are scoped, time-limited, and reasonably compensated
- Governing law and forum selection are appropriate for the parties' locations

### YELLOW — Legally Questionable / Requires Revision

Any of the following:

- OWBPA consideration period is correct but agreement creates early-signing incentive
  (coercion risk)
- Required carve-out language is present but buried or ambiguous
- Consideration is borderline — close to what the employee may have been owed; could
  be challenged if a prior agreement or policy promised certain severance
- Non-disparagement clause is broader than the defamation standard but may survive
  judicial scrutiny in the current political climate given McLaren Macomb uncertainty
- Non-compete lacks independent consideration but is in a blue-pencil state where it
  may be partially enforced
- FLSA claims within the scope of the general release without DOL/court approval
- Reference provision is vague (best efforts only) rather than a specific commitment
- Cooperation obligation is indefinite but limited to the employee's personal involvement

### RED — Legally Invalid / Creates Liability

Any one of the following:

- Any OWBPA factor not satisfied for an employee age 40+ → ADEA release is void
- Required group informational disclosure missing or materially incomplete
- Release of EEOC charge-filing right → void; EEOC enforcement not blocked (Waffle House)
- Consideration consists entirely of wages already earned or vested benefits
- California § 1542 waiver absent in a California-nexus agreement
- Non-compete in a ban state (CA, MN, ND, OK) subject to those states' laws
- Non-disparagement clause that would prevent employee from filing NLRB charge or
  participating in agency proceedings (McLaren Macomb)
- Confidentiality clause prohibiting disclosure to union representatives or in
  connection with NLRB proceedings (McLaren Macomb)
- SEC Rule 21F-17(a) violation: award waiver, prior-notification requirement, or
  clause that could be enforced to impede SEC reporting
- State NDA restriction violated (CA, WA, NY, NJ, IL) for discrimination/harassment claims
- Release purports to cover future claims without temporal limitation
- 7-day revocation period waived, shortened, or absent

---

## Prioritization Framework

**Tier 1 — Must Address Before Agreement Is Executed**

- Any failed OWBPA factor (the ADEA release is void until cured)
- Missing 7-day revocation right
- EEOC carve-out absent from an overbroad release
- SEC Rule 21F-17(a) violations (award waiver, prior-notification requirement)
- State NDA restriction violations (CA SB 331, WA HB 1795)
- Non-compete in a ban state for an employee in that state

**Tier 2 — Address Before Agreement Is Finalized**

- McLaren Macomb non-disparagement/confidentiality defects
- Missing group informational disclosure (group program)
- Consideration adequacy issues
- Missing California § 1542 waiver
- FLSA claims within release without DOL/court approval
- Indefinite or unpaid cooperation obligations

**Tier 3 — Market Practice Improvements**

- Reference provision specificity
- Certification of return of property
- Section 409A technical compliance review
- Minor clarifications to defined terms

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                               | Fail Action                                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, case, or established principle                                             | Add citation or mark "[UNVERIFIED]"                                                                                                                             |
| **Format**     | All citations follow a consistent, recognizable format (29 U.S.C. § 626(f); 372 NLRB No. 58; 17 C.F.R. § 240.21F-17)               | Fix format                                                                                                                                                      |
| **Currency**   | Every cited provision verified as current law as of March 2026                                                                     | Flag "[CHECK CURRENCY]" — especially for McLaren Macomb (pending reversal), FLSA waiver law (circuit split), NY No Severance Ultimatums Act (pending enactment) |
| **Domain**     | Analysis stays within US employment and compliance law; jurisdiction-specific content stays behind [JURISDICTION-SPECIFIC] markers | Remove or flag jurisdictional bleed                                                                                                                             |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                                          | Add confidence qualifier — especially for McLaren Macomb status, FLSA waiver enforceability, state NDA expansion                                                |

---

## Self-Interrogation for High-Severity Items

For any item classified as RED, apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity:**
Does the RED classification follow logically from the cited authority? Would a court or
the EEOC, NLRB, or SEC actually reach this conclusion based on these facts? Check:

- Is the statutory/regulatory citation accurate?
- Is the case holding correctly characterized?
- Does the specific agreement language actually trigger the cited violation?

**Pass 2 — Completeness:**
Have all relevant statutes, regulations, and enforcement standards been considered?

- For OWBPA: Did you check all 7 factors AND the group disclosure requirements (if applicable)?
- For McLaren Macomb: Did you consider whether the employee is a supervisor who lacks Section 7 rights?
- For state NDA restrictions: Did you confirm the applicable state has a nexus to this agreement?
- For SEC Rule 21F-17: Did you check for both the prior-notification provision AND the award-waiver provision?

**Pass 3 — Challenge:**
What is the strongest argument that this is not RED?

- For OWBPA: Is the employee under 40 (OWBPA inapplicable)?
- For McLaren Macomb: Is the Board about to overrule this? (Yes, likely — but as of March
  2026, it has not been overruled.)
- For non-competes: Is the ban state's law actually triggered? (Consider choice-of-law,
  employee's work location, enforceability analysis.)

Conclude: After all three passes, confirm the RED classification or downgrade to YELLOW
with explanation.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                 | Action                                                    |
| ------------ | --------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statutory requirement                                                | State with confidence                                     |
| **High**     | 0.80-0.94 | Strong authority, minor questions                                                       | State with brief caveat                                   |
| **Probable** | 0.60-0.79 | Good arguments but could differ by jurisdiction or fact pattern                         | State with reasoning and contra-indicators                |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., McLaren Macomb reversal timeline; FLSA waiver circuit split) | Flag for professional review with both sides of the issue |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                                                 | Do not assert; flag "[UNCERTAIN]"                         |

**Specific areas requiring Probable or Possible confidence only:**

- McLaren Macomb enforcement pending formal reversal (Probable — law is binding but may
  change; enforce against current law while flagging political risk)
- FLSA private waiver in a jurisdiction with no circuit ruling (Possible — circuit split
  exists; treat as high risk without DOL/court approval)
- New York No Severance Ultimatums Act applicability (Possible — pending enactment as of
  March 2025; [VERIFY] before citing as live law)
- Whether a specific one-employee RIF triggers the 45-day group track (Possible —
  fact-specific; flag and advise conservative approach)

---

## Glass Box Audit Trail

Include the following YAML block in every output:

```yaml
glass_box:
  skill_name: "legalcode-severance-agreement-review"
  review_date: "[DATE]"
  perspective: "[Employer / Employee / Counsel / HR Audit]"
  separation_type: "[Involuntary termination / RIF / Voluntary / COC / Mutual]"
  owbpa_track: "[21-day Individual / 45-day Group / Not applicable — under 40]"
  employee_age_40_plus: "[Yes / No / Unknown]"
  jurisdiction_primary: "[State]"
  jurisdictions_assessed: ["[State 1]", "[State 2]"]
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-severance-research.md or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  owbpa_factors_passed: "[X]/7 (Individual) or [X]/8 (Group — includes group disclosure)"
  red_findings_count: "[N]"
  yellow_findings_count: "[N]"
  green_findings_count: "[N]"
  self_interrogation_applied: "[Yes — [N] RED items reviewed / No]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED / [VERIFY]]"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  mclaren_macomb_current_law: "Yes — binding as of [DATE]; pending potential reversal"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "FLSA waiver enforceability: treat as high-risk without DOL/court approval"
    - "McLaren Macomb: current law; monitor for NLRB Board reversal"
  reviewer: "AI-assisted — requires review by qualified employment counsel"
```

---

## Anti-Patterns

The following are the most common errors and failures in severance agreement review —
what a skilled employment attorney would look for and what this skill is designed to catch:

1. **Assuming OWBPA compliance without reading the clock language**: Many agreements
   state "21 days" in the header but allow the employer to shorten the period by
   offering enhanced consideration for early signing. This is coercive and potentially
   invalidates the period.

2. **Missing full-name ADEA citation**: Releasing "all discrimination claims" or
   "all claims under federal law" without specifically naming the Age Discrimination in
   Employment Act is a common, often-fatal defect. Shorthand (e.g., "ADEA") without
   explanation may be insufficient under strict EEOC interpretation.

3. **Applying the 21-day individual track to a group RIF**: Employers who terminate
   multiple employees simultaneously using the same severance formula but present
   agreements one-at-a-time to avoid the 45-day requirement violate OWBPA. Courts
   look at the program structure, not the signing process.

4. **Incomplete or inaccurate group informational disclosure**: The most litigated
   OWBPA defect. Employers frequently (a) fail to identify the decisional unit correctly,
   (b) omit job titles and ages of non-selected employees, (c) use an HR unit rather
   than the actual operational decisional unit, or (d) exclude employees from the list
   whose exclusion is itself the discrimination alleged.

5. **Attempting to waive the 7-day revocation period**: This is non-waivable by statute.
   Agreement language stating the employee "agrees to irrevocably execute" the agreement
   or waives any right to revoke is void on its face.

6. **Consideration is wages already owed**: Employers sometimes include in the
   "consideration" amounts that are accrued but unpaid wages or accrued vacation pay
   that state law mandates must be paid out regardless. This is not additional
   consideration — it is payment of an existing obligation.

7. **Using old California Civil Code § 1542 language**: The § 1542 waiver language was
   amended effective January 1, 2019. Agreements using the pre-2019 language may not
   effectively release unknown claims in California. Always use the current statutory
   text verbatim.

8. **Broad non-disparagement clause without McLaren Macomb carve-outs**: Agreements
   drafted before February 2023 routinely contain language that now (under current law)
   constitutes an unfair labor practice. Even where the employee has signed and accepted
   payment, the NLRB may find the proffer itself was unlawful.

9. **Award-waiver language in the context of SEC reporting**: An agreement that permits
   the employee to "participate" in government agency proceedings but waives the right
   to receive any monetary award is a Rule 21F-17(a) violation per the September 2024
   SEC enforcement actions. The award entitlement and the participation right are both
   protected separately.

10. **Pre-notification-of-employer requirement for government contact**: Any clause
    requiring the employee to notify or obtain consent from the employer before
    contacting the SEC, CFTC, FINRA, DOL, or EEOC independently violates Rule 21F-17
    and the EEOC's charge-filing protections.

11. **Non-compete in a ban state with California choice-of-law override analysis skipped**:
    Employers frequently insert a favorable choice-of-law clause (e.g., Delaware) to
    circumvent California law. California SB 699 (Jan. 1, 2024) expressly renders this
    choice-of-law clause void — California employees' non-competes are unenforceable
    regardless of the chosen governing law.

12. **Introducing a new non-compete without separate consideration in the severance agreement**:
    The severance pay is consideration for the release of claims. A new post-employment
    restriction introduced for the first time at termination requires its own, separately
    identified consideration in most states. Relying on the severance pay to support
    both is a common drafting error.

13. **Applying the Speak Out Act to post-dispute settlement NDAs**: The Speak Out Act
    (Pub. L. 117-228) voids pre-dispute NDAs covering sexual assault and harassment
    claims. It does not affect post-dispute negotiated settlement agreements, which may
    still include confidentiality provisions. Conflating the two creates unnecessary
    concern in post-dispute settlement review.

14. **Failing to include express future-claims carve-out**: Some agreements purport to
    release "any and all claims of any kind" without a temporal limitation. For ADEA
    waivers this is a fatal OWBPA defect. For other claims, it is of uncertain
    enforceability and creates a misleading document — employees cannot release claims
    they do not yet have.

15. **Cooperation clause with no time limit or compensation**: An indefinite, uncompensated
    cooperation obligation in a senior executive's severance agreement creates ongoing
    obligation and resentment risk, may implicate employment law in some jurisdictions,
    and does not bind the employer to any corresponding obligation (e.g., no obligation
    to give reasonable notice or schedule around the employee's new employment).

16. **Reference provision says "best efforts" without naming a contact**: "Best efforts
    to provide a neutral reference" is meaningless if the employer has no internal
    mechanism to route reference calls. A named HR contact or a reference-line vendor
    (Talentwise, The Work Number) is a more defensible commitment. Vague reference
    provisions frequently lead to post-separation disputes when former managers deviate.

17. **Signing before the last day of employment without a reaffirmation provision**:
    If the employee signs before the termination date, the release covers only conduct
    through the signing date. Any claim arising in the gap between signing and termination
    is not released. Sophisticated plaintiff's counsel routinely assert claims arising
    in this window. A reaffirmation clause (re-execute after the termination date with
    a new consideration period) closes this gap.

18. **Section 409A non-compliance in salary-continuation severance**: Employers frequently
    overlook that certain severance structures (salary continuation exceeding the short-
    term deferral exception; installment payments that cross tax years) may trigger
    Section 409A. Failure to include compliant elections and payment triggers in the
    agreement creates both tax exposure (20% excise tax plus interest) and employer
    withholding liability.

19. **Tender-back provision for ADEA waiver challenge**: Some employers include a clause
    requiring the employee to tender back all severance before bringing an ADEA claim.
    This directly conflicts with 29 C.F.R. § 1625.22(i) (the tender-back rule
    post-Oubre). Including a void tender-back provision does not prevent an ADEA claim;
    it may, however, be read by a court as evidence of an attempt to evade OWBPA
    protections.

20. **Failing to restart the clock after a material change to the offer**: If the
    employer makes a material change to the severance offer after the consideration
    period has begun (e.g., increases the amount, changes key terms), the consideration
    period restarts. Immaterial changes (formatting corrections, administrative updates)
    do not restart the clock. The agreement should specify who determines materiality
    to avoid a post-signing dispute.

---

## Writing Standards

Before delivering output:

- Use active, directive language in recommendations: "Add the ADEA full name to the
  release clause" not "The ADEA could be added to the release clause"
- Quantify exposure where possible: "If the ADEA waiver is void, the employer retains
  full ADEA exposure, including potential back pay, liquidated damages (double back pay
  for willful violations under 29 U.S.C. § 626(b)), and attorneys' fees under
  29 U.S.C. § 216(b)"
- Distinguish between current law and uncertain/evolving law: "Under current NLRB
  precedent (McLaren Macomb, binding as of [date]), this clause is unlawful. Note that
  the Board's political composition may result in a formal reversal — monitor."
- Do not use Latin or legal jargon without plain-language explanation
- Where an issue is contested or circuit-split, present both sides: do not assert the
  minority view as the rule
- Flag [VERIFY] for every statutory citation made from memory without cross-referencing
  an authoritative source in this session

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
Search for:

- 29 U.S.C. § 626(f) (current text)
- 29 C.F.R. § 1625.22 (current text)
- McLaren Macomb, 372 NLRB No. 58 (2023)
- Rule 21F-17(a), 17 C.F.R. § 240.21F-17 (current text)
- Applicable state statutes for the employee's work state
- Recent EEOC/NLRB/SEC enforcement guidance

Save results to `/tmp/legalcode-severance-research.md` and mark citations VERIFIED
where confirmed against authoritative source.

**Without legalcode-mcp:**
Proceed with research-backed analysis from this skill. Mark all statutory and case law
citations with [VERIFY] unless verified in the current session via web search. Note in
the Glass Box: `legalcode_mcp: "Not connected"`.

---

## Localization Notes

This skill is US-primary. When applying to non-US agreements:

1. **United Kingdom**: Replace OWBPA analysis with the Employment Rights Act 1996 s.111A
   settlement agreement framework. The "independent legal advice" requirement is mandatory
   — an unadvised settlement agreement is void. Statutory minimum notice (ss.86-91) and
   statutory redundancy (ss.135-145) cannot be released without payment. Research: ACAS
   Code of Practice on Settlement Agreements, 2013.

2. **Australia**: Fair Work Commission unfair dismissal conciliation; general protections
   settlement; minimum entitlements under the NES cannot be contracted out. Research:
   Fair Work Act 2009 (Cth), Fair Work Commission procedural requirements.

3. **European Union**: Member state employment law governs termination agreements.
   Collective dismissal consultation (Directive 98/59/EC) rights cannot be waived by
   individual agreement. GDPR consent is not a valid legal basis for processing employee
   personal data in a severance context — the power imbalance makes consent involuntary
   (EDPB Guidelines 05/2020).

4. **Canada**: Federal (Canada Labour Code) and provincial frameworks vary. Quebec
   requires French-language agreements. Ontario requires Employment Standards Act
   statutory minimums to be paid regardless of any general release.

---

## Output Format Template

```markdown
# Severance Agreement Review

**Agreement:** [Title or description]
**Reviewing Party:** [Employer / Employee / Counsel]
**Date of Review:** [Date]
**Employee Age 40+:** [Yes / No / Unknown]
**OWBPA Track:** [21-Day Individual / 45-Day Group / Not Applicable]
**Jurisdiction:** [Primary state / governing law state]
**Overall Risk Classification:** [GREEN — Legally Sufficient / YELLOW — Requires
Revision / RED — Legally Invalid / High Employer Exposure]

---

## Executive Summary

[2-4 sentence executive summary: overall assessment, most critical findings, immediate
action required.]

---

## OWBPA/ADEA Compliance Analysis

_[Applicable only for employees age 40+]_

| Factor                                        | Status             | Findings   | Remediation         |
| --------------------------------------------- | ------------------ | ---------- | ------------------- |
| Factor 1: Plain Language                      | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Factor 2: ADEA Named                          | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Factor 3: No Future Claims                    | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Factor 4: Adequate Consideration              | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Factor 5: Written Advice to Consult Attorney  | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Factor 6: Consideration Period ([21/45] days) | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Factor 7: 7-Day Revocation                    | [GREEN/YELLOW/RED] | [Findings] | [Required language] |
| Group Disclosure (if applicable)              | [GREEN/YELLOW/RED] | [Findings] | [Required language] |

**OWBPA Overall Assessment:** [All 7/8 factors satisfied — ADEA release VALID / [N] factors failed — ADEA release VOID]

---

## Release of Claims Analysis

**Scope:** [Summary of claims released]
**EEOC Carve-Out:** [Present and adequate / Missing / Defective]
**FLSA Claims:** [Not within scope / Within scope — flag for DOL/court approval]
**California § 1542 Waiver:** [Not applicable / Present — current language / Missing — RED]
**Temporal Limitation:** [Adequate / Missing]

---

## Consideration Adequacy

**Consideration Provided:** [List: separation pay amount/duration, benefits, services]
**Classification:** [GREEN — adequate additional consideration / YELLOW — borderline /
RED — consists of wages/benefits already owed]
**Notes:** [Analysis of adequacy, timing issues, Section 409A flag if applicable]

---

## Restrictive Covenants

**Non-Compete:** [Present / Absent]
**State Enforceability:** [GREEN — enforceable / YELLOW — questionable / RED — ban state or void]
**Non-Solicitation:** [Present / Absent] [GREEN/YELLOW/RED]
**Separate Consideration:** [Adequate / Inadequate]
**FTC Rule Status:** Vacated August 20, 2024 — state law governs

---

## Non-Disparagement and Confidentiality

**Non-Disparagement:** [One-way employer → employee / Mutual / Absent]
**McLaren Macomb Compliance:** [GREEN — limited to defamation standard / YELLOW — broad
but ambiguous / RED — facially violates Section 8(a)(1)]
**SEC Rule 21F-17:** [GREEN — compliant carve-out / YELLOW — partial / RED — award waiver
or notification requirement present]
**State NDA Restrictions:** [Not applicable / [State] — COMPLIANT / [State] — NON-COMPLIANT]

---

## Protected Rights Carve-Outs

| Carve-Out                        | Status           | Classification |
| -------------------------------- | ---------------- | -------------- |
| EEOC charge filing               | [Present/Absent] | [GREEN/RED]    |
| Government agency participation  | [Present/Absent] | [GREEN/RED]    |
| SEC/CFTC/FINRA reporting + award | [Present/Absent] | [GREEN/RED]    |
| Workers' compensation            | [Present/Absent] | [GREEN/RED]    |
| Unemployment compensation        | [Present/Absent] | [GREEN/YELLOW] |
| Vested ERISA benefits            | [Present/Absent] | [GREEN/RED]    |
| Future claims                    | [Present/Absent] | [GREEN/RED]    |
| NLRA Section 7 rights            | [Present/Absent] | [GREEN/RED]    |

---

## Cooperation, Property Return, and Reference

**Cooperation:** [Scope] | [Duration] | [Compensation] | [Classification]
**Return of Property:** [Adequate / Partial / Absent]
**Reference:** [Commitment type] | [Classification]

---

## Governing Law and Dispute Resolution

**Choice of Law:** [State] — [Assessment of validity / override risk]
**Arbitration:** [Present / Absent] | [Speak Out Act applicability]

---

## Employer Exposure Summary

| Exposure Area                | Level             | Basis                                          |
| ---------------------------- | ----------------- | ---------------------------------------------- |
| ADEA/OWBPA (void release)    | [HIGH/LOW — N/A]  | [Failed factors, if any]                       |
| NLRB (McLaren Macomb)        | [HIGH/MEDIUM/LOW] | [Non-disparagement/confidentiality assessment] |
| SEC Rule 21F-17              | [HIGH/MEDIUM/LOW] | [Whistleblower clause assessment]              |
| State law (NDA restrictions) | [HIGH/MEDIUM/LOW] | [Applicable state law]                         |
| Non-compete (ban state)      | [HIGH/MEDIUM/LOW] | [State enforceability]                         |

---

## Prioritized Action Items

### Tier 1 — Must Address Before Execution

1. [Action] — [Specific provision to revise] — [Suggested replacement language]

### Tier 2 — Address Before Finalization

1. [Action] — [Provision] — [Recommendation]

### Tier 3 — Market Practice Improvements

1. [Action] — [Provision] — [Recommendation]

---

## Notes for Legal Counsel

[Any issues flagged for specialist review: Section 409A, FLSA waiver, WARN Act,
EEOC interaction, pending state legislation, McLaren Macomb reversal monitoring]

---

[Glass Box YAML block — see template above]
```

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis. Research sources:
29 U.S.C. § 626(f) (OWBPA); 29 C.F.R. § 1625.22; Oubre v. Entergy Operations, Inc.,
522 U.S. 422 (1998); EEOC v. Waffle House, Inc., 534 U.S. 279 (2002); McLaren Macomb,
372 NLRB No. 58 (2023); Rule 21F-17(a), 17 C.F.R. § 240.21F-17; SEC enforcement
actions September 2024; EEOC Q&A on Waivers of Discrimination Claims; Lynn's Food Stores
v. United States, 679 F.2d 1350 (11th Cir. 1982); Cal. Civ. Code § 1542 (as amended
2019); Cal. Bus. & Prof. Code § 16600 (as amended AB 1076, Jan. 1, 2024); Minn. Stat.
§ 181.988 (eff. July 1, 2023); CA SB 331 (eff. Jan. 1, 2022); WA HB 1795 (eff. June 9,
2022); NY Gen. Oblig. Law § 5-336 (as amended S.B. 4516, eff. Nov. 17, 2023); Savage
v. Township of Neptune (NJSC, May 2024); Speak Out Act, Pub. L. 117-228 (Dec. 7, 2022);
Pagilio v. Guidant Corp.; Kruchowski v. Weyerhaeuser Co.; Mass. G.L. c. 149 § 24L.
Structural patterns adapted from legalcode-contract-review, legalcode-employment-
agreement-review, and legalcode-non-compete-enforceability reference skills.
