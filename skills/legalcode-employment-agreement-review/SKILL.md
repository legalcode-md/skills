---
name: legalcode-employment-agreement-review
description: Review employment agreements clause-by-clause against market standards or an organizational
  playbook. Use when evaluating new hire offer packages, executive employment agreements, promotion agreements,
  or renegotiated employment terms.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review employment agreements clause-by-clause against market standards or an organizational playbook. Use when evaluating new hire offer packages, executive employment agreements, promotion agreements, or renegotiated employment terms. Covers compensation structure (base, bonus, commission, clawback), equity compensation (options, RSUs, vesting schedules, acceleration triggers, post- termination exercise windows), restrictive covenants (non-compete with US state-by-state enforceability matrix, non-solicitation of employees and customers, non-disclosure, garden leave), intellectual property assignment and pre-existing IP carve-outs (with jurisdiction-specific moral rights treatment), termination provisions (cause definition, notice periods, severance triggers), change-of- control provisions (single vs. double trigger, IRC § 280G golden parachute analysis), clawback provisions (SEC Rule 10D-1, Dodd-Frank § 954, SOX § 304), dispute resolution and forum selection (arbitration enforceability under Ending Forced Arbitration of Sexual Assault and Sexual Harassment Act), and post- employment cooperation obligations. GREEN/YELLOW/RED classification with confidence-scored redline suggestions. Jurisdictions: US (all 50 states for non-compete; federal clawback/arbitration/IP), UK (ERA 1996/ERA 2025, garden leave, CDPA 1988 moral rights), EU (Germany § 74 HGB, France droit de non-concurrence, EU Trade Secrets Directive), Australia (Fair Work Act NES, Copyright Act moral rights), India (Contract Act s.27, Niranjan Shankar Golikari). Evaluates enforceability under evolving state non-compete bans post-FTC rule vacatur (Ryan LLC v. FTC, Aug 20 2024). Usefulness: 9/10.


# Legalcode Employment Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted employment agreement
> review. It does not constitute legal advice. All outputs require review by a qualified
> employment lawyer licensed in the relevant jurisdiction before relying on them for any
> employment, negotiation, or compliance decision. Laws — especially state non-compete
> law — change frequently; verify current applicability before acting. Statutory and
> case law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them. This skill does not substitute for
> individual legal advice regarding your specific employment situation.

---

## Purpose and Scope

This skill reviews employment agreements clause-by-clause against market standards or
an organizational playbook. It classifies deviations, assesses enforceability of
restrictive covenants, generates confidence-scored redline suggestions, and produces
an auditable analysis tailored to the reviewing party's perspective (employee, employer,
or HR counsel).

**Covers:**

- Full clause-by-clause review of any employment, offer letter, or executive compensation agreement
- GREEN / YELLOW / RED deviation classification with dual-perspective framing
- Enforceability analysis of non-compete, non-solicitation, and NDA covenants across US states and major international jurisdictions
- Equity compensation review (vesting, acceleration, post-termination exercise windows)
- Clawback provision analysis (SEC Rule 10D-1, Dodd-Frank § 954, SOX § 304)
- Change-of-control trigger analysis and IRC § 280G golden parachute screening
- IP assignment scope and pre-existing IP carve-out assessment
- DTSA whistleblower immunity notice compliance check
- Arbitration clause analysis including Ending Forced Arbitration Act applicability
- Jurisdiction-specific governing law and forum selection assessment
- Confidence-scored redline suggestions with fallback positions
- Glass Box audit trail for traceability

**Does not:**

- Draft new employment agreements from scratch (see legalcode-saas-agreement-drafter or consult drafting specialists)
- Provide personal legal advice or substitute for qualified employment counsel
- Guarantee enforceability determinations — courts apply multi-factor tests that vary by jurisdiction and fact pattern
- Cover labor union / collective bargaining agreement (CBA) review
- Perform comprehensive equity plan or tax analysis (IRC § 83(b), AMT, QSBS) — flag issues for specialist review

**Related skills:** `legalcode-nda-triage` (standalone NDA review), `legalcode-contract-review`
(general commercial contract review), `legalcode-employee-handbook-review` (handbook compliance audit).

---

## Jurisdiction and Governing Law

This is a jurisdiction-aware skill. The agreement's governing law clause determines which
legal framework applies, but the **employee's work location jurisdiction** may override
the choice of law for restrictive covenant and wage payment purposes in many US states
and in the EU.

**Jurisdiction detection:** At Step 4, identify:

1. The stated choice of law in the agreement
2. The employee's primary work location
3. Where the employer is incorporated

**Jurisdiction override analysis:**

- California, Minnesota, Oklahoma, and North Dakota: voids non-competes **regardless**
  of the chosen governing law if the employee works in (or sometimes merely resides in)
  those states
- EU member states: Posted Workers Directive (96/71/EC as amended by 2018/957) — host
  country employment law applies to posted workers regardless of choice of law
- Australia: Fair Work Act 2009 (Cth) — NES cannot be contracted out of regardless of
  any contrary choice of law

[JURISDICTION-SPECIFIC] For each non-US jurisdiction, research:

- Mandatory employment law provisions that override contractual choice of law
- Local language requirements for employment agreements
- Registration or filing requirements for employment agreements
- Mandatory notice periods and redundancy payment schemes
- Collective bargaining agreement (CBA) or enterprise agreement overlay requirements

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked **⟁ CLARIFY**.
Rather than assuming context, the workflow pauses to ask when:

- The answer materially changes the direction or depth of analysis
- Multiple valid interpretations exist that only the user can resolve
- Jurisdiction selection is ambiguous (affecting entire non-compete analysis)
- Equity terms require confirmation before complex acceleration analysis

Present clarification questions as structured options with brief "Why this matters"
explanations. If the user has already provided the information in their initial prompt,
skip the question and proceed — state your assumption explicitly.

**Batch/non-interactive default**: Proceed with these defaults and state them at the
start of the analysis:

- Perspective: Employee (reviewing for personal use)
- Seniority: Salaried professional / mid-level
- Context: New hire / offer stage
- Equity: Assume equity present if agreement references any equity, stock, or options
- Jurisdiction: Use the stated governing law; note if work location override may apply

---

## Workflow

### Step 1: Accept the Agreement

Accept the employment agreement in any format:

- **File**: PDF, DOCX, TXT, or image scan
- **URL**: Link to a document management system, Google Drive, or Dropbox
- **Pasted text**: Full or partial text pasted directly into the conversation

If no agreement is provided, prompt: "Please share the employment agreement text or file
you would like me to review."

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the following questions. Present each
as structured options with descriptions:

1. **Your perspective** — Who are you in this transaction?
   - Options: Employee (being offered the agreement), Employer / HR (reviewing before
     sending to candidate), Candidate (evaluating a pending offer with negotiation
     leverage in mind), Legal / compliance counsel (audit or compliance review)
   - _Why this matters_: The entire analysis flips depending on perspective. A broad
     non-compete protects the employer but harms the employee; framing and recommendations
     differ completely.

2. **Role seniority** — What is the employee's level?
   - Options: Hourly / entry-level IC, Salaried professional / manager, Senior management
     / VP, C-suite executive (CEO, CFO, COO, CTO, GC), Director / board-level advisor
   - _Why this matters_: Seniority affects non-compete enforceability thresholds (many
     states require salary above a threshold), whether 280G applies, equity acceleration
     analysis, and whether cause definitions reflect market executive standards.

3. **Review context** — What triggered this review?
   - Options: New hire offer (pre-signing), Promotion or renegotiation (mid-employment),
     Acquisition or change-of-control scenario, Separation / termination scenario (reviewing
     existing agreement), Equity grant or amendment
   - _Why this matters_: Changes the analytical focus — new hire reviews emphasize
     negotiating positions; separation reviews emphasize severance triggers and release
     scope; acquisition reviews emphasize change-of-control triggers.

4. **Equity component** — Does this agreement include equity compensation?
   - Options: No equity component, Stock option grant (ISO or NQSO), RSU or RSA grant,
     Profit interest or synthetic equity, Multiple equity vehicles
   - _Why this matters_: Triggers detailed vesting cliff, acceleration trigger, post-
     termination exercise window, and (for public companies) Dodd-Frank clawback analysis.

5. **Jurisdiction** — Which jurisdiction's law governs?
   - Options: Single US state (specify which — non-compete law varies dramatically
     by state), Multiple US states (distributed team or multi-state employer), United
     Kingdom, EU member state (specify which — France, Germany, Netherlands, etc.),
     Australia, India, Other / unknown
   - _Why this matters_: The most consequential question in the review. A non-compete
     that is fully enforceable in Florida is void as a matter of law in California.
     Moral rights treatment of IP, notice periods, and garden leave depend entirely
     on jurisdiction.

If the user provides partial context, proceed with stated assumptions. Do not silently
assume — declare every assumption explicitly.

### Step 3: Load Playbook (Optional)

**⟁ CLARIFY** — Does the user have an organizational playbook or standard position sheet
to review against?

- Options: Yes — I will upload or paste our standard positions, No — review against
  market standards for the applicable jurisdiction and seniority tier, No playbook but
  I have specific concerns to focus on (specify)
- _Why this matters_: A playbook-based review is more precise. Without one, the review
  uses market-standard positions calibrated to the seniority tier and jurisdiction.

If no playbook is provided, apply these defaults (state them explicitly at the start
of the analysis):

- Non-compete duration: 6-12 months for professionals; 12-24 months for executives
- Non-compete geographic scope: narrowly defined business territory or customer-facing scope
- Non-solicitation of employees: 12 months, limited to direct reports and colleagues with
  whom the employee worked
- Severance: 1 week per year of service (general market); 6-18 months for executives
- Equity vesting: 4-year / 1-year cliff as market standard
- Equity post-termination exercise window: 90 days (ISO standard); extended window RED flag
  only if ISO conversion implications are unexplored

### Step 4: Identify Governing Law and Jurisdiction

Before any clause analysis, extract and verify:

1. The stated choice of law clause (which state / country)
2. The stated choice of venue / forum (which courts)
3. The employee's primary work location (if stated; ask if not)
4. The employer's state of incorporation (if relevant for 280G analysis)
5. Any arbitration clause or class action waiver

**Non-compete jurisdiction override check:** If the governing law is any state other
than California, Minnesota, Oklahoma, or North Dakota, but the employee works in one
of these states:

- Flag immediately as **[JURISDICTION OVERRIDE — HIGH PRIORITY]**
- State the specific ban applicable to the employee's work location
- Advise the clause may be void regardless of the contractual choice of law

**⟁ CLARIFY** — If the work location is not stated in the agreement:

- Ask: "Where will the employee primarily work? State non-compete law follows the work
  location in most jurisdictions, and several states (California, Minnesota, Oklahoma,
  North Dakota) ban non-competes regardless of governing law."

### Step 5: Structural Completeness Assessment

Before clause-by-clause analysis, assess structural completeness. Identify which of
the following standard sections are **present**, **absent**, or **deficient**:

| Section                             | Status | Priority if Missing                      |
| ----------------------------------- | ------ | ---------------------------------------- |
| Job title and duties                |        | YELLOW                                   |
| Compensation (base salary)          |        | RED — essential                          |
| Bonus / incentive compensation      |        | YELLOW if role expects bonus             |
| Equity compensation                 |        | YELLOW if equity was represented         |
| At-will / termination provision     |        | RED — defines employment security        |
| Non-compete / restrictive covenants |        | Note if absent (favorable to employee)   |
| Non-solicitation                    |        | Note if absent (favorable to employee)   |
| Non-disclosure / confidentiality    |        | YELLOW — nearly universal                |
| IP assignment                       |        | RED for technology roles                 |
| Dispute resolution / arbitration    |        | YELLOW                                   |
| Choice of law / venue               |        | YELLOW                                   |
| Governing law                       |        | RED — needed for enforceability analysis |
| Severance terms                     |        | YELLOW — absence = no commitment         |
| Change-of-control provisions        |        | YELLOW for executive roles               |
| Benefits                            |        | YELLOW                                   |
| Post-employment cooperation         |        | YELLOW — note if present (burdensome)    |

Produce a completeness table as the first section of the output.

### Step 6: Clause-by-Clause Analysis

Conduct deep analysis of each present clause using the frameworks in **Section: Clause
Analysis Frameworks** below. For each clause:

1. Extract the operative language (key phrases, defined terms)
2. Compare to market standard and/or playbook position
3. Classify: **GREEN** (acceptable), **YELLOW** (negotiate), **RED** (reject / escalate)
4. Assign confidence score (Definite 0.95-1.0 / High 0.80-0.94 / Probable 0.60-0.79 /
   Possible 0.40-0.59 / Unlikely 0.0-0.39)
5. Generate redline suggestion with fallback position
6. Assess business impact (Low / Medium / High / Critical)
7. Flag any jurisdiction-specific enforceability concerns

Work through clauses in this order:

1. Compensation and base salary
2. Bonus and incentive pay
3. Equity compensation (if present)
4. Clawback provisions
5. Non-compete
6. Non-solicitation (employees)
7. Non-solicitation (customers)
8. Non-disclosure / confidentiality
9. IP assignment
10. At-will status and termination for cause
11. Notice periods and PILON
12. Severance and separation pay
13. Change-of-control provisions
14. Dispute resolution and arbitration
15. Choice of law and venue
16. Benefits continuation
17. Post-employment cooperation

### Step 7: Non-Compete Enforceability Deep Dive

For any non-compete clause present, apply the full Non-Compete Enforceability Matrix
from **Section: Non-Compete Enforceability Matrix** below.

Apply the **three-prong test** applicable in most US common law jurisdictions:

1. **Protectable interest**: Does the employer have a legitimate business interest
   (trade secrets, confidential information, customer relationships, specialized
   training) that justifies the restriction?
2. **Reasonableness**: Is the scope (activities restricted), geographic area, and
   duration no broader than necessary to protect the legitimate interest?
3. **Consideration**: Is there adequate consideration for the covenant?
   - New employment = generally sufficient consideration
   - Mid-employment = may require independent consideration (garden leave payment,
     bonus, promotion) in many jurisdictions

Apply the state-specific override if the work location jurisdiction bans non-competes.

**⟁ CLARIFY** — For executive-level reviews involving equity acceleration:

- Ask: "Does the company have a 280G tax gross-up obligation in the agreement? If so,
  I will analyze golden parachute exposure."

### Step 8: IP Assignment Deep Dive

For any IP assignment or PIIA (Proprietary Information and Inventions Assignment) clause,
apply the IP Assignment Framework from **Section: Clause Analysis Frameworks — 9. IP
Assignment** below.

Critical mandatory checks:

- [ ] DTSA whistleblower immunity notice present (18 U.S.C. § 1836(b)(3)(C)) — if absent,
      employer forfeits right to recover attorney fees and exemplary damages in any trade
      secret misappropriation claim against the employee
- [ ] Pre-existing IP schedule (Exhibit A or equivalent) included or offered
- [ ] Employee invention carve-out language (California Labor Code § 2870 equivalent for
      applicable state) present
- [ ] Moral rights treatment addressed for UK/AU/EU employees

### Step 9: Clawback and 280G Analysis (Public Company / Executive Roles)

For C-suite, named executive officers, or any agreement at a SEC reporting company:

**Clawback (SEC Rule 10D-1):**

- Trigger: accounting restatement (Big-R restatement OR little-r restatement — both
  covered under Rule 10D-1 as of October 2, 2023)
- Covered period: 3 fiscal years preceding the restatement determination date
- Recovery: excess incentive compensation (the portion attributable to the restated
  metric); not misconduct-based
- No-indemnification: agreement must not indemnify the executive against clawback recovery
- If the employer is a NYSE/Nasdaq listed company, the clawback policy must be filed as
  an exhibit to Form 10-K — flag if the employment agreement conflicts with the policy

**280G golden parachute screening:**

- Screen for: CIC-conditioned cash payments, equity acceleration, benefits continuation
- If aggregate present value of CIC-conditioned payments exceeds 3x base amount (as
  defined in IRC § 280G) → flag for specialist 280G calculation
- Gross-up provisions: if present, flag as strongly employer-unfavorable (rare in current
  market; majority shifted to "best-net" calculations post-2010)
- Market standard: double trigger for equity acceleration; excise tax protection via
  best-net (not gross-up)

### Step 10: Self-Interrogation for RED Items

For each finding classified as RED, apply three-pass adversarial review before confirming:

**Pass 1 — Legal Chain Integrity**: Does the RED classification follow logically from the
applicable legal standard? Would a court or regulator actually find this problematic?
Could the clause be blue-penciled or narrowed rather than voided?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and cases been
considered? Is there a jurisdiction where this clause would not be RED?

**Pass 3 — Challenge**: What is the employer's strongest argument for this clause? Under
what circumstances might a reasonable employment lawyer advise the employer to insist on
it? What is the employee's realistic negotiating leverage?

Revise the classification if any pass reveals a weaker basis for RED. Downgrade to YELLOW
with explanation if appropriate.

### Step 11: Prioritization and Negotiation Strategy

After all clauses are analyzed, produce a Prioritization Framework (see Output Format
Template) that ranks issues by:

- **Tier 1 — Must Address**: RED items where the risk is irreversible or where clause
  is likely unenforceable as written, creating false security
- **Tier 2 — Should Address**: YELLOW items that deviate materially from market standard
  or that create meaningful risk over the employment lifecycle
- **Tier 3 — Nice to Have**: YELLOW items that are suboptimal but acceptable; GREEN items
  worth flagging for awareness

Calibrate by perspective:

- **Employee perspective**: Tier 1 = clauses that restrict post-employment freedom or
  create unexpected financial liability
- **Employer perspective**: Tier 1 = clauses that leave valuable IP, customer relationships,
  or competitive position unprotected

### Step 12: Quality Assurance

Before delivering the output:

1. Run Citation Quality Gates (see **Section: Citation Quality Gates**)
2. Confirm all [VERIFY] items are flagged for professional review
3. Confirm all jurisdiction-specific items are marked [JURISDICTION-SPECIFIC]
4. Confirm all anti-patterns from **Section: Anti-Patterns** have been avoided
5. Apply Writing Standards (see **Section: Writing Standards**)
6. Complete Glass Box Audit Trail template (see **Section: Glass Box Audit Trail**)

### Step 13: Deliver Output

Produce the full output using the template in **Section: Output Format Template**.
Lead with the executive summary and tier 1 priorities so the user can make immediate
decisions without reading the full report.

---

## Clause Analysis Frameworks

### 1. Compensation and Base Salary

**What to assess:**

- Is base salary stated as an annual amount or hourly rate?
- Is there a currency and payment frequency?
- Is there a salary review commitment (annual review, merit increase schedule)?
- Are there any pay reduction provisions? Under what conditions?

| Classification | Criteria                                                                                                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Stated salary; annual review commitment; no employer discretion to reduce without notice; payment frequency clear                         |
| **YELLOW**     | No review commitment; discretionary review language; unusual payment schedule                                                             |
| **RED**        | Employer unilateral right to reduce salary without notice or employee consent; salary stated as "up to" (illusory); no base salary stated |

**Redline for RED (unilateral reduction):**

> _"The Company shall not reduce Employee's Base Salary without Employee's written
> consent, except as part of a documented, proportionate, across-the-board reduction
> affecting all similarly-situated employees, with not less than [30/60] days' prior
> written notice."_

[JURISDICTION-SPECIFIC] UK: ERA 1996 s.13 — unlawful deductions from wages; any pay
reduction requires employee consent or contractual right. AU: Fair Work Act 2009 s.50 —
modern award and NES provisions cannot be reduced.

---

### 2. Bonus and Incentive Compensation

**What to assess:**

- Is the bonus discretionary or contractual (target amount, formulaic calculation)?
- What are the conditions for earning (employment at payment date, performance criteria)?
- Clawback / repayment trigger on early departure?
- Timing of payment?

| Classification | Criteria                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Target bonus defined; formula or objective criteria stated; good leaver payment on termination before payment date; reasonable clawback window (≤12 months)                                                                     |
| **YELLOW**     | "Discretionary" bonus with no minimum or formula; employment-at-payment-date condition (common but means forfeiture if terminated the day before payment); clawback window 12-24 months                                         |
| **RED**        | No bonus description despite representations; indefinitely discretionary with no floor; clawback on resignation at any time with no temporal limit; bonus forfeited on termination for any reason including no-fault redundancy |

**Redline for RED (forfeiture on termination):**

> _"If Employee's employment is terminated by the Company without Cause, or Employee
> resigns for Good Reason, prior to the annual bonus payment date, Employee shall receive
> a pro-rated annual bonus for the portion of the performance year completed, paid at
> the time bonuses are paid to other similarly-situated employees."_

---

### 3. Equity Compensation

**What to assess:**

- Type of equity: ISO (Incentive Stock Option), NQSO/NSO, RSU, RSA, SAFE participation
- Vesting schedule: duration, cliff period, acceleration triggers
- Post-termination exercise window
- Acceleration: single trigger vs. double trigger vs. no acceleration
- Equity plan incorporation by reference — obtain and review the plan itself

**Vesting market standard (US):** 4-year vest / 1-year cliff / monthly thereafter.
Deviation in either direction requires analysis.

| Classification | Criteria                                                                                                                                                                                                                |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | 4-year / 1-year cliff; double-trigger full acceleration on CIC + involuntary termination; 90-day post-termination exercise window for options; plan available for review                                                |
| **YELLOW**     | Cliff > 1 year; single-trigger acceleration (employer concern for acquisitions); exercise window < 90 days or requires board discretion; plan incorporated but not provided                                             |
| **RED**        | No vesting schedule defined; all-cliff vesting (100% after X years, zero before); post-termination window < 30 days; no acceleration in CIC for C-suite; plan terms that supersede this agreement in ways not disclosed |

**Post-termination exercise window — tax trap:**
ISOs must be exercised within 90 days of termination to maintain ISO status. If the
agreement grants an extended exercise window (12 months, 24 months, 10 years), the
options automatically convert to NQSOs for the portion exercised after day 90, with
immediate ordinary income tax implications. Flag for tax counsel if window > 90 days.

**Redline for missing CIC double-trigger acceleration:**

> _"In the event of a Change in Control, if Employee's employment is terminated without
> Cause or Employee resigns for Good Reason within [12] months following the Change in
> Control, 100% of Employee's then-unvested equity awards shall immediately accelerate
> and become fully vested and exercisable."_

[JURISDICTION-SPECIFIC] UK/EU: Equity participation in UK/EU employment agreements may
trigger securities law disclosure obligations and employee information/consultation
requirements under TUPE (Transfer of Undertakings (Protection of Employment) Regulations
2006). [VERIFY local securities and employee consultation requirements]

---

### 4. Clawback Provisions

**What to assess:**

- Does the employer have a written clawback/recoupment policy?
- Does this agreement incorporate or reference the policy?
- Is the trigger for clawback: (a) misconduct, (b) accounting restatement, or (c) other?
- Does the agreement indemnify the executive against clawback? (forbidden under SEC Rule
  10D-1 for listed companies)

**Regulatory framework (US):**

- **SEC Rule 10D-1** (17 CFR 240.10D-1, eff. Oct 2, 2023): Applies to listed companies.
  Requires clawback of incentive compensation from current and former PEO/PFO + named
  executive officers (NEOs) upon accounting restatement. Covers both Big-R (material
  misstatement requiring filing amendment) and little-r (error correction in current
  period) restatements. 3-year look-back. No fault / no misconduct required. Exchange
  listing rules require listed company to adopt a compliant policy.
- **Dodd-Frank § 954** (15 U.S.C. § 78j-4): Enabling statute for Rule 10D-1.
- **SOX § 304** (15 U.S.C. § 7243): CEO and CFO only; covers willful misconduct leading
  to restatement; 1-year look-back; SEC enforcement action required.

| Classification | Criteria                                                                                                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **GREEN**      | References board-adopted clawback policy compliant with applicable exchange rules; trigger limited to accounting restatement; no indemnification of executive against recovery                                                                   |
| **YELLOW**     | Broad discretionary clawback trigger (e.g., "any conduct detrimental to Company"); long look-back period (>5 years); individual agreement purports to supersede or limit the board policy                                                        |
| **RED**        | Employer indemnifies executive against clawback recovery (violates SEC Rule 10D-1 for listed companies); clawback applies to non-incentive compensation (base salary) without legal basis; trigger is subjective and employer-sole-determination |

---

### 5. Non-Compete

**What to assess:**

- Duration (months post-termination)
- Geographic scope (US national, state, radius, customer-facing territory)
- Activity scope (all competitive activity vs. employee's specific role vs. specific
  customers or business lines)
- Adequate consideration (especially for mid-employment amendments)
- Governing law choice and work location override risk

Apply the **Non-Compete Enforceability Matrix** below for jurisdiction-specific analysis.

| Classification | Criteria                                                                                                                                                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **GREEN**      | Duration ≤ 6 months; limited to employee's actual activities and specific customers; legitimate protectable interest clearly stated; adequate independent consideration; garden leave payment (UK/EU/AU/IL)                                                                                                        |
| **YELLOW**     | Duration 6-12 months; US national scope without geographic limitation (overbroad but potentially blue-pencilable); consideration is continuation of employment only                                                                                                                                                |
| **RED**        | Duration > 24 months (unenforceable in most jurisdictions); activity scope = "any competing business" regardless of employee's actual role; work location in ban state regardless of choice of law; no adequate consideration for mid-employment amendment; employer has no legitimate protectable interest stated |

**Redline for overbroad scope:**

> _"Employee's obligations under this Section shall be limited to activities directly
> competitive with [specifically named business lines] and shall apply only within
> the geographic territory in which Employee actively conducted business during the
> [12] months preceding termination."_

**Critical carve-out for ban-state employees:**

> _"Notwithstanding anything to the contrary, to the extent Employee's primary place
> of employment is located in a jurisdiction that prohibits enforcement of post-
> employment non-competition restrictions, this Section shall not apply to Employee."_

---

### 6. Non-Solicitation of Employees

**What to assess:**

- Duration (12-24 months is market range)
- Scope: "solicit" only vs. "hire" vs. "assist in hiring" vs. "encourage to leave"
- Whether restricted to direct reports or extends to all Company employees
- Activity restriction: active solicitation vs. passive (responding to inbound requests)

| Classification | Criteria                                                                                                                                                    |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Duration ≤ 12 months; limited to direct reports / employees employee had material contact with; active solicitation only (not passive hiring)               |
| **YELLOW**     | Duration 12-24 months; extends to all Company employees including those employee had no contact with; includes passive hiring                               |
| **RED**        | Duration > 24 months; restricts employee from working for a company that happens to hire another ex-employee; extends to contract workers, advisors broadly |

[JURISDICTION-SPECIFIC] California: Non-solicitation of employees is also highly restricted
under § 16600. _AMN Healthcare, Inc. v. Aya Healthcare Services, Inc._, 28 Cal. App. 5th 923
(2018) held that non-solicitation of co-workers is subject to the same § 16600 analysis
as non-competes. [VERIFY current CA non-solicitation case law]

[JURISDICTION-SPECIFIC] UK post-_Egon Zehnder International Ltd v Tillman_ [2019] UKSC 32:
Severance is available — courts may sever an unenforceable part of a restrictive covenant
to make the remainder enforceable, applying modified blue-pencil doctrine.

---

### 7. Non-Solicitation of Customers

**What to assess:**

- Definition of "customer": current only, or also "prospective" (overbroad)
- Material contact requirement: restricted to customers employee personally served
- Duration: 12-24 months typical

| Classification | Criteria                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **GREEN**      | Limited to customers employee had material contact with in the 12 months preceding termination; duration ≤ 12 months; "solicit business" scope (not "have any contact")                                      |
| **YELLOW**     | Extends to prospective customers employee presented to; duration 12-24 months; broad "contact" restriction rather than "solicit"                                                                             |
| **RED**        | Restricts contact with all Company customers regardless of employee's relationship; duration > 24 months; restricts mere responses to inbound inquiries from customers who independently sought out employee |

---

### 8. Non-Disclosure / Confidentiality

**What to assess:**

- Scope of "Confidential Information" — is it defined or is it the entire universe of
  employer information?
- Standard carve-outs present: public domain, independently developed, third-party
  disclosure, required by law
- Duration: indefinite for trade secrets (appropriate); time-limited for general
  confidential information
- DTSA whistleblower immunity notice (18 U.S.C. § 1836(b)(3)(C)) — mandatory
- Disclosure to government / regulators: must not restrict

| Classification | Criteria                                                                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Confidential information defined with carve-outs; perpetual for trade secrets; time-limited (3-5 years) for general confidential info; DTSA notice present; government disclosure explicitly permitted                                                                    |
| **YELLOW**     | Overly broad definition without carve-outs; indefinite duration for all confidential information (trade secret + general); no DTSA notice                                                                                                                                 |
| **RED**        | Purports to restrict disclosure to EEOC, NLRB, OSHA, SEC, or other regulators; prohibits truthful communications in government investigations; prevents employee from retaining their own attorney; NLRA § 7 rights chilled post-_McLaren Macomb_ (372 NLRB No. 58, 2023) |

**DTSA Whistleblower Immunity Notice (mandatory for any agreement with misappropriation
claim potential):**

> _"An individual shall not be held criminally or civilly liable under any Federal or
> State trade secret law for the disclosure of a trade secret that is made: (i) in
> confidence to a Federal, State, or local government official, either directly or
> indirectly, or to an attorney, solely for the purpose of reporting or investigating
> a suspected violation of law; or (ii) in a complaint or other document filed in a
> lawsuit or other proceeding, if such filing is made under seal. See 18 U.S.C.
> § 1836(b)(3)(C)."_
> If the agreement is missing this notice, the employer cannot recover attorney fees
> or exemplary damages in any subsequent trade secret misappropriation claim, even if
> the employer prevails.

---

### 9. Intellectual Property Assignment

**What to assess:**

- Scope: all inventions or only those made in scope of employment?
- Pre-existing IP schedule (Exhibit A / prior inventions disclosure) — present?
- Employee invention carve-out (California Labor Code § 2870 and state equivalents)
- Moral rights treatment (UK, EU, AU only)
- Work-for-hire coverage: written agreement required for independent contractors

**US Framework:**

- Copyright Act 17 U.S.C. § 101: Works created by employees within scope of employment
  are automatically works made for hire — employer owns without assignment. For independent
  contractors, assignment requires a written agreement in one of nine specified categories.
- 35 U.S.C. § 262: Joint patent ownership — each joint owner may exploit the patent
  without consent of the other. If multiple employees contribute to an invention, all
  are joint owners absent a valid assignment.
- California Labor Code § 2870 (and equivalents in DE, IL, MN, NC, WA, NV [VERIFY
  all state equivalents]): Employee inventions are carved out of employer assignment
  requirements if: (1) made outside working hours; (2) without using employer equipment,
  supplies, facilities, or trade secrets; (3) not related to employer's business or
  actual/demonstrably anticipated R&D.

**Pre-existing IP Schedule:** The agreement should include (or offer to attach) a schedule
listing IP employee owns or has developed before employment. Without this, all pre-
employment IP arguably falls within the "developed by Employee" language of broad
assignment clauses. A blank schedule is not adequate — it implies employee had nothing
to disclose.

| Classification | Criteria                                                                                                                                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Scope limited to IP developed in scope of employment and/or using company resources; employee invention carve-out language present and jurisdiction-compliant; DTSA notice included; prior inventions schedule attached or offered; work-for-hire for employee works stated correctly |
| **YELLOW**     | No employee invention carve-out; prior inventions schedule missing but clause permits attachment; IP assignment extends to off-duty work remotely related to company's business                                                                                                       |
| **RED**        | Assignment of all inventions employee ever conceives regardless of time, resources, or relevance (common in startup boilerplate — void to the extent it violates § 2870); no DTSA notice; purports to assign pre-existing IP without acknowledgment                                   |

[JURISDICTION-SPECIFIC] **UK (CDPA 1988 s.11 and Patents Act 1977 s.39-42):** Employer
automatically owns copyrights and inventions made by employees in the course of employment.
Employee retains moral rights (integrity right and attribution right) but may consent to
waivers — waivers must be specific and written. General blanket moral rights waivers
are common in UK employment agreements and generally enforceable as written.

[JURISDICTION-SPECIFIC] **France (droit moral):** Moral rights are inalienable under
French intellectual property law — they cannot be waived even by contract. The economic
rights (droits patrimoniaux) are automatically assigned to the employer for software
created by employees but must be expressly assigned for other works.

[JURISDICTION-SPECIFIC] **Australia (Copyright Act 1968 s.35(6), Patents Act 1990):**
Employer automatically owns employee works made in the course of employment (copyright)
and inventions (patents Act 1990 s.15(1)(b)). Moral rights under Part IX of the
Copyright Act cannot be waived — only consent to specific acts can be given; consent
must be informed and specific (De Garis v. Neville Jeffress Pidler Pty Ltd [1990]).
General blanket moral rights waivers purporting to waive all moral rights forever are
of uncertain effect.

[JURISDICTION-SPECIFIC] **India (Copyright Act 1957 s.17):** Employer owns works
made by employees in the course of employment. Patent inventorship follows the inventor,
not the employer — assignment must be express and in writing; Patents Act 1970 s.6
requires the inventor's name regardless of assignment.

---

### 10. At-Will Employment and Termination for Cause

**What to assess:**

- At-will statement present and unambiguous (US)
- Cause definition: subjective (employer sole discretion) vs. objective (enumerated
  criteria with materiality threshold)
- Cure right for curable cause (reasonable prior notice + opportunity to cure)
- Double-cause requirement (misconduct + board determination)
- Constructive dismissal / good reason triggers

**US "Cause" market standard for executives:**
At a minimum: (a) conviction or plea to felony or crime of moral turpitude; (b) material
breach of agreement after written notice and 30-day cure opportunity; (c) willful failure
to perform material duties after written notice and 30-day cure opportunity; (d) fraud,
embezzlement, or material misappropriation against the company.

**Absent an express definition, "Cause" is typically construed narrowly in favor of the
employee in equity-trigger analyses.**

| Classification | Criteria                                                                                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | At-will with clear disclaimer; cause defined with objective criteria; cure right for curable breaches; constructive termination / good reason defined at executive level                                                              |
| **YELLOW**     | Cause defined but includes "conduct materially detrimental to Company" (overbroad); no cure right for performance-based cause; no good reason trigger for executive                                                                   |
| **RED**        | No at-will disclaimer (creating implied contract risk via progressive discipline policy); cause definition = employer sole discretion with no standards; cause includes minor policy violations; no cure right for any cause category |

[JURISDICTION-SPECIFIC] **UK:** "Dismissal" follows the ERA 1996 / Employment Rights Act
2025 framework. Day-1 unfair dismissal protection under ERA 2025 (Royal Assent Dec 18, 2025) removes the prior 2-year qualifying period requirement [VERIFY commencement date
of ERA 2025 Day-1 unfair dismissal provisions]. Cause equivalent = "potentially fair
reasons" under ERA 1996 s.98 (conduct, capability, redundancy, statutory restriction,
some other substantial reason). ACAS Code of Practice (revised) requires investigation
and disciplinary procedure before dismissal for misconduct.

[JURISDICTION-SPECIFIC] **Australia:** Fair Work Act 2009 s.385 — unfair dismissal
available after minimum employment period (1 year for small business; 6 months for
others). "Serious misconduct" (Fair Work Regulations 2009 r.1.07) bypasses notice but
must be genuine and documented.

[JURISDICTION-SPECIFIC] **India:** Industrial Disputes Act 1947 applies to "workmen"
(non-managerial/non-supervisory). Senior/managerial employees are typically excluded.
Indian courts have generally held that restrictive post-employment covenants are void
under Contract Act 1872 s.27 — non-compete covenants operative _during_ employment
are enforceable per Niranjan Shankar Golikari v. Century Spinning and Manufacturing Co.
Ltd., [1967] 3 SCR 490.

---

### 11. Notice Periods and Payment in Lieu of Notice (PILON)

**What to assess:**

- Mutual vs. unilateral notice periods
- PILON clause: explicit right to pay in lieu of notice?
- Garden leave clause: right to require employee to work notice period without duties?
- Post-termination pay during restrictive covenant period (EU/UK requirement)

**Jurisdiction-specific notice requirements:**

| Jurisdiction             | Statutory Minimum                                                    | Notes                                      |
| ------------------------ | -------------------------------------------------------------------- | ------------------------------------------ |
| US                       | None (at-will default)                                               | Contractual notice, if any, governs        |
| UK (ERA 1996 s.86)       | 1 week per year of service (1-12 weeks max)                          | Contractual notice supersedes if longer    |
| EU — France              | 1-3 months (varies by collective agreement and seniority)            | See applicable collective agreement        |
| EU — Germany             | 4 weeks minimum; up to 7 months for 20+ years (§ 622 BGB)            | Statutory minimum                          |
| Australia (FW Act s.117) | 1-5 weeks depending on years of service (+ 1 week for 45+ years old) | Award/enterprise agreement may supersede   |
| India                    | Varies; typically 1-3 months; varies by state, industry, role        | Shops & Establishments Act varies by state |

| Classification | Criteria                                                                                                                                                                                             |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Mutual notice; PILON clause present (avoiding breach of contract risk); garden leave clause if employee is in sensitive role                                                                         |
| **YELLOW**     | Asymmetric notice (longer obligation on employee than employer); PILON absent (garden leave of full notice period is common but requires explicit clause)                                            |
| **RED**        | Notice period < statutory minimum for jurisdiction; no PILON but employer routinely uses PILON (creating tax and breach risk); notice period > 6 months for non-executive (restraint of trade issue) |

---

### 12. Severance and Separation Pay

**What to assess:**

- Explicit severance commitment or statement that no severance applies
- Conditions for severance eligibility (termination without cause vs. any termination)
- Amount formula (weeks per year of service, fixed lump sum, continuation)
- Release requirement: general release of claims a condition?
- ADEA / OWBPA compliance for employees 40+ (US): 21 days to consider + 7-day revocation
- Non-disparagement and cooperation conditions attached to severance

| Classification | Criteria                                                                                                                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Severance defined and payable without cause; release requirement explicitly stated; ADEA-compliant consideration period for 40+ employees; good leaver/bad leaver distinction for equity treatment on termination             |
| **YELLOW**     | Severance conditioned on signing broad release without advance disclosure of release terms; non-disparagement attached to severance conflicts with NLRA § 7 post-_McLaren Macomb_                                             |
| **RED**        | Severance paid only if employee cooperates for indefinite period at employer's discretion; release purports to waive EEOC/NLRB/OSHA charge-filing rights (void under law); ADEA-governed employee given < 21 days to consider |

[JURISDICTION-SPECIFIC] UK: Statutory redundancy pay (ERA 1996 ss.162-164) + any
contractual enhanced redundancy. Settlement agreements (formerly compromise agreements)
must be in writing, signed by both parties, and employee must have received advice from
an independent qualified adviser (ERA 1996 s.203). Under ERA 2025, review for any
changes to redundancy payment scheme [VERIFY].

---

### 13. Change-of-Control Provisions

**What to assess:**

- Definition of "Change in Control" — stock sale, asset sale, merger, board change,
  50% ownership threshold vs. other percentage
- Single trigger: CIC alone triggers severance and/or equity acceleration
- Double trigger: CIC + involuntary termination (without cause or good reason) required
- Benefits continuation post-CIC termination
- 280G golden parachute exposure

**Market standard evolution (US):**
Pre-2010: Single trigger equity acceleration + gross-up were common. Current market:
double trigger strongly preferred by acquirers; gross-ups replaced by "best-net" (employee
keeps the amount that results in the highest after-tax value — either full payment with
excise tax or reduced payment below 280G threshold, whichever is greater).

**IRC § 280G screening:**
Excess parachute payment = aggregate present value of CIC-conditioned payments exceeds
3x the executive's average compensation over the 5 preceding years (Base Amount).
Payments exceeding 1x Base Amount = excess parachute payment. Consequence: (1) executive
owes 20% excise tax on the excess (IRC § 4999); (2) employer loses the deduction for
the excess. If present value of total parachute payments < 3x Base Amount, no 280G
exposure. This calculation requires forensic compensation data — flag for specialist.

| Classification | Criteria                                                                                                                                                                                                                                                                    |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Double trigger for equity acceleration and severance; best-net calculation (not gross-up); CIC definition captures stock sale, asset sale, and board change; benefits continuation 12-18 months                                                                             |
| **YELLOW**     | Single trigger for equity acceleration only (not cash); no best-net or gross-up (leaves excise tax unaddressed); CIC definition omits board change (common gap)                                                                                                             |
| **RED**        | Single trigger for all payments (acquirer concern — may discourage acquisition); gross-up provision (tax inefficient and now market-disfavored); no CIC provision for executive despite representations; CIC definition requires 100% acquisition (misses merger-of-equals) |

---

### 14. Dispute Resolution and Arbitration

**What to assess:**

- Mandatory vs. voluntary arbitration for employment claims
- Governing arbitration rules (AAA Employment, JAMS, FINRA for registered reps)
- Class action waiver
- Scope of claims submitted to arbitration
- Ending Forced Arbitration of Sexual Assault and Sexual Harassment Act analysis
- Jury trial waiver
- Fee allocation (employees cannot be required to pay employer's filing fees or AAA
  administrative fees as a condition of bringing claims — _Green Tree Financial Corp.-
  Ala. v. Randolph_, 531 U.S. 79 (2000); AAA Employment Arbitration Rules § 38)

**Ending Forced Arbitration of Sexual Assault and Sexual Harassment Act of 2022
(Pub. L. 117-90, 9 U.S.C. §§ 401-402, eff. March 3, 2022):**

- Any predispute arbitration agreement (including this employment agreement) cannot
  compel arbitration of: (a) sexual assault disputes, or (b) sexual harassment disputes
  as defined in Title VII (42 U.S.C. § 2000e-2(a)(1)) or other applicable law
- The **claimant alone** decides whether to invoke arbitration for such claims
- Applies **retroactively** to existing arbitration agreements — the clause is voidable
  at the employee's election for these claim types even if signed before March 3, 2022
- Class/collective action waivers for these claim types are also voided

| Classification | Criteria                                                                                                                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Arbitration clause contains explicit carve-out for sexual harassment/assault claims per Ending Forced Arbitration Act; employer bears arbitration fees; AAA Employment or JAMS rules; individual arbitration (not class waiver for non-excluded claims acceptable if clear)                                               |
| **YELLOW**     | No explicit Ending Forced Arbitration Act carve-out (clause is de-facto voided for these claims but employer may not know it, creating ambiguity); fee allocation unclear; JAMS/AAA rules not specified                                                                                                                   |
| **RED**        | Mandatory arbitration for all employment claims with no Ending Forced Arbitration Act carve-out and no acknowledgment of the 2022 law; employee required to pay employer's costs; forum in distant jurisdiction making arbitration impractical; class action waiver as condition of employment with no meaningful opt-out |

---

### 15. Choice of Law and Venue

**What to assess:**

- Choice of law jurisdiction: favorable or hostile to enforcement?
- Venue: convenient for employee or only for employer?
- Possibility of work-location override rendering choice of law ineffective for
  restrictive covenants (California, Minnesota, etc.)
- Conflict with mandatory employment law of work location

| Classification | Criteria                                                                                                                                                                                                          |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Choice of law is the employee's actual work location or a neutral, convenient jurisdiction; forum is within reasonable travel distance; restrictive covenant and employment law analysis consistent               |
| **YELLOW**     | Choice of law is employer's state of incorporation (disadvantages employee but not unusual); forum is employer's principal office (travel burden on employee)                                                     |
| **RED**        | Choice of law designed to circumvent employee's work-location employment protections; venue requires international travel for dispute; choice of law conflicts with mandatory applicable law of work jurisdiction |

---

### 16. Benefits Continuation

**What to assess:**

- COBRA notice and election rights (US — if employer offers group health)
- Benefits continuation during notice period
- Vesting and benefit plan rights on termination
- Disability and life insurance coverage during leave

[JURISDICTION-SPECIFIC] US: COBRA (29 U.S.C. §§ 1161-1168) — employer must offer
18 months continuation coverage for qualifying events (termination without gross misconduct,
reduction in hours). Employer must provide election notice within 14 days of administrator
being notified. Failure to provide timely COBRA notice = statutory penalty of $110/day.

| Classification | Criteria                                                                                                                                       |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | COBRA rights referenced; benefits continue through notice period; plan documents provided or referenced                                        |
| **YELLOW**     | Benefits terminate immediately on notice (rather than at end of notice period); COBRA not mentioned; no reference to plan documents            |
| **RED**        | Benefits condition on signing broad release (unlawful — COBRA rights cannot be conditioned on release); purports to deny COBRA election rights |

---

### 17. Post-Employment Cooperation Obligations

**What to assess:**

- Duration: indefinite or time-limited?
- Scope: litigation support only or general business cooperation?
- Compensation for time: is the employee paid for cooperation time post-termination?
- Expense reimbursement?
- Travel obligations?

| Classification | Criteria                                                                                                                                                                                |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Time-limited (18-24 months); reasonable scope (litigation involving period of employment); employee compensated at daily rate for time; expenses reimbursed                             |
| **YELLOW**     | Indefinite duration; no compensation for cooperation time; broad scope (any company business, not just matters employee had personal involvement with)                                  |
| **RED**        | Indefinite, uncompensated obligation that effectively extends employment obligations; travel required at employee's expense; used as leverage to deny severance if cooperation withheld |

---

## Non-Compete Enforceability Matrix

Apply this matrix whenever a non-compete clause is present. Work location governs
regardless of contractual choice of law in most ban states.

| Jurisdiction      | Status                               | Key Law                                                            | Duration Limit                                                                         | Compensation Required                                                | Threshold / Conditions                                                                                                                                             | Key Cases                                                        |
| ----------------- | ------------------------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **California**    | **BAN**                              | Cal. Bus. & Prof. Code §§ 16600-16600.5                            | N/A — void                                                                             | N/A                                                                  | Any employee in CA or CA-resident employee                                                                                                                         | _Edwards v. Arthur Andersen_, 44 Cal.4th 937 (2008)              |
| **Minnesota**     | **BAN** (post-7/1/2023)              | Minn. Stat. § 181.988                                              | N/A for new/amended agreements after July 1, 2023                                      | N/A                                                                  | New employment or agreements after July 1, 2023                                                                                                                    | None yet — law new                                               |
| **Oklahoma**      | **BAN**                              | 15 Okla. Stat. § 219A                                              | N/A (exception: sale of business)                                                      | N/A                                                                  | All employees; sale of business exception                                                                                                                          | —                                                                |
| **North Dakota**  | **BAN**                              | NDCC § 9-08-06                                                     | N/A                                                                                    | N/A                                                                  | All employees; narrow exceptions                                                                                                                                   | —                                                                |
| **FTC Rule**      | **VACATED**                          | 16 CFR Part 910                                                    | N/A — never took effect                                                                | N/A                                                                  | Vacated: _Ryan LLC v. FTC_, N.D. Tex. Aug. 20, 2024; FTC abandoned appeal Sept. 5, 2025                                                                            | —                                                                |
| **Washington**    | Restricted                           | RCW 49.62 (eff. Jan 1, 2020)                                       | 18 months                                                                              | Yes — garden leave or equivalent during restriction period           | $100K+ salary; advance notice before acceptance required; no geographic limit if scope limited to employee's work                                                  | —                                                                |
| **Colorado**      | Restricted                           | CRS § 8-2-113 (eff. Aug 10, 2022)                                  | 12 months (professional roles)                                                         | Yes — garden leave required                                          | Tiered thresholds: $123,750+/yr for non-compete; $60,750+/yr for non-solicitation [VERIFY current thresholds]                                                      | —                                                                |
| **Illinois**      | Restricted                           | 820 ILCS 90/10 (eff. Jan 1, 2022)                                  | 2 years                                                                                | Yes — garden leave (at least 14 days) or adequate consideration      | $75K+/yr for non-compete; $45K+/yr for non-solicitation [VERIFY current thresholds — adjust for inflation]                                                         | —                                                                |
| **Oregon**        | Restricted                           | ORS 653.295 (eff. 2022)                                            | 12 months                                                                              | Yes — garden leave or base salary equivalent                         | $100,533+/yr [VERIFY]; written agreement required; advance notice                                                                                                  | —                                                                |
| **Nevada**        | Restricted                           | NRS 613.195                                                        | No specified limit                                                                     | No                                                                   | Specialized roles with access to trade secrets; no damages for first violation                                                                                     | —                                                                |
| **Massachusetts** | Restricted                           | M.G.L. c. 149, § 24L (eff. Oct 1, 2018)                            | 12 months                                                                              | Yes — garden leave (50% base) OR other mutually agreed consideration | 7 days advance notice; written agreement; employee/garden-leave-eligible                                                                                           | —                                                                |
| **New York**      | Evolving                             | NYCPLR Art. 4-C (signed Jan 2024 — implementation status [VERIFY]) | 1 year (if enacted)                                                                    | Not required in statute                                              | Hourly rate above threshold; no consideration for existing employees                                                                                               | [VERIFY — Governor signed but challenged]                        |
| **Texas**         | Permitted (with limits)              | Tex. Bus. & Com. Code § 15.50                                      | Reasonable                                                                             | No                                                                   | Ancillary to otherwise enforceable agreement; consideration (employment alone insufficient for existing employees post-_Light v. Centel_); "reasonable" limitation | _Light v. Centel Cellular Co. of Texas_, 883 S.W.2d 642 (1994)   |
| **Florida**       | Employer-Friendly                    | Fla. Stat. § 542.335                                               | Presumptively reasonable: ≤ 6 months (employee); ≤ 3 years (professional/trade secret) | No                                                                   | Blue-pencil mandatory; employee bears burden to prove overbreadth                                                                                                  | —                                                                |
| **UK**            | Garden Leave + Reasonableness        | Common law; ERA 1996                                               | Typically 3-12 months (reasonableness test)                                            | Garden leave payment = full salary during restriction                | Legitimate business interest; reasonable in scope, geography, duration                                                                                             | _Tullett Prebon plc v. BGC Brokers LP_ [2011] IRLR 420           |
| **Germany**       | Restricted                           | §§ 74-75f HGB                                                      | 2 years maximum                                                                        | Yes — 50% of last compensation (Karenzentschädigung) mandatory       | Commercial employees; employee must sign in writing; must reference specific business area                                                                         | —                                                                |
| **France**        | Restricted                           | Common law; Cour de Cassation                                      | Reasonable (typically ≤ 2 years)                                                       | Yes — typically 30-60% of salary during restriction period           | Legitimate interest; specific geographic and activity scope; compensation or void                                                                                  | Soc. 14 mai 1992 (landmark on compensated non-competes)          |
| **Australia**     | Permitted (reasonableness)           | Common law; Restraint of Trade Act 1976 (NSW)                      | Reasonable (cascade clause technique)                                                  | No                                                                   | Legitimate business interest; reasonable scope, duration, geography; cascade clause if NSW                                                                         | _Cactus Imaging Pty Ltd v. Peters_ [2006] NSWSC 717              |
| **India**         | **Near-total BAN** (post-employment) | Contract Act 1872 s.27                                             | Not applicable                                                                         | N/A                                                                  | Sale of business exception only; in-employment clauses enforceable per _Niranjan Shankar Golikari_ [1967]; post-employment void                                    | _Niranjan Shankar Golikari v. Century Spinning_ [1967] 3 SCR 490 |

---

## Prioritization Framework

### Tier 1 — Must Address (Escalate or Reject Without Resolution)

**For employees:**

- Non-compete in ban state (California, Minnesota, Oklahoma, North Dakota) regardless
  of governing law clause — void by operation of law but creates chilling effect
- IP assignment of pre-existing work and off-duty inventions with no carve-out
- Arbitration clause with no Ending Forced Arbitration Act carve-out (creates ambiguity
  on sexual harassment claims)
- Cause definition as employer's sole discretion with no standards
- DTSA whistleblower immunity notice absent (employer loses fee recovery right — flag
  because absence may signal broadly adversarial drafting)
- At-will disclaimer absent where progressive discipline policy is cross-referenced
  (implied contract risk)

**For employers:**

- Non-compete clause unenforceable in employee's work jurisdiction (false security;
  trade secrets unprotected by clause that will not be enforced)
- IP assignment missing DTSA notice (forfeits fee recovery and exemplary damages)
- Employee invention carve-out absent in California / carve-out state (violates Labor
  Code § 2870; agreement void to that extent)
- Clawback clause conflicts with SEC Rule 10D-1 (exchange compliance risk)
- Arbitration clause missing Ending Forced Arbitration Act carve-out (clause
  unenforceable for those claim types; dispute over scope at worst time)

### Tier 2 — Should Address (Material Deviations Worth Negotiating)

- Non-compete duration > 12 months for non-executive employee
- Non-compete scope extending to activities unrelated to employee's actual role
- Bonus forfeiture on any termination without pro-rata provision
- Equity acceleration: single trigger rather than double trigger (executive level)
- Post-termination exercise window unexplored where ISO conversion risk present
- Severance conditioned on unusually broad release without advance review opportunity
- Non-solicitation of employees extending to all employees (not just direct contacts)
- Good reason / constructive dismissal definition absent for executive
- Change-of-control definition missing board change (incomplete CIC trigger)

### Tier 3 — Nice to Have (Worth Flagging; Acceptable If Unchanged)

- Annual salary review commitment absent (common; not a market baseline)
- Benefits plan details incorporated by reference without copy provided
- Post-employment cooperation with no compensation provision (common;
  courts rarely enforce onerous cooperation obligations against departed employees)
- Garden leave provision absent (UK/EU — advisable but not always present)
- Dispute resolution forum slightly inconvenient
- No liquidated damages clause for breach (employer relies on injunctive relief)

---

## Citation Quality Gates

Run these five gates before delivering any output. If any gate fails, revise or flag
before delivering.

| Gate           | Rule                                                                                                                                                             | Fail Action                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Source**     | Every enforceability determination cites a specific statute, case, or regulatory authority                                                                       | Add citation or mark "[UNVERIFIED]"                                              |
| **Format**     | All citations follow a consistent citation format appropriate to the jurisdiction (Bluebook for US; OSCOLA for UK; etc.)                                         | Fix format                                                                       |
| **Currency**   | Every cited statute / regulation checked for amendments, repeal, or supersession                                                                                 | Flag "[CHECK CURRENCY]" for any provision that may have changed post-August 2025 |
| **Domain**     | Analysis stays within the agreement's governing law scope; no jurisdiction bleed (do not state US law as applicable to UK agreement without noting the conflict) | Remove or flag jurisdictional bleed                                              |
| **Confidence** | Uncertainty explicitly stated; probability scores attached to enforceability determinations                                                                      | Add confidence qualifier per Confidence Scoring framework                        |

---

## Self-Interrogation for RED Items

For any finding classified as RED, apply this three-pass review before confirming
the classification:

**Pass 1 — Legal Chain Integrity**: Does the RED classification follow logically from
the cited authority? Would a court or regulator actually find the clause problematic?
Has blue-penciling / severance been considered? Could the clause be partially enforced?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, case law, and
regulatory guidance been considered? Is there a forum or jurisdiction where the same
clause would be GREEN? Would the classification change if the employee's seniority
were different?

**Pass 3 — Challenge**: What is the drafter's strongest argument for the clause as
written? Under what business circumstances would a reasonable employment lawyer advise
insisting on it? What is the realistic enforcement risk (courts rarely enjoin employees
who have already left)?

Revise to YELLOW if any pass reveals that the RED classification overstates the risk.
Retain RED if all three passes confirm the classification. Document the self-interrogation
result in the Glass Box audit trail.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                 | Action                                                |
| ------------ | --------- | ------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law; clear statute; no jurisdictional ambiguity | State with confidence; no caveat required             |
| **High**     | 0.80-0.94 | Strong authority; minor questions on application        | State with brief caveat noting remaining questions    |
| **Probable** | 0.60-0.79 | Good arguments; outcome could differ                    | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuinely uncertain; could go either way                | Flag for professional review; present both sides      |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                 | Do not assert as legal conclusion; mark "[UNCERTAIN]" |

Employment law enforceability determinations are inherently fact-specific — no analysis
under this skill should exceed **High (0.80-0.94)** confidence for non-compete
enforceability questions without verified current case law for the specific jurisdiction.

---

## Glass Box Audit Trail

Include this YAML block at the end of every review output:

```yaml
glass_box:
  skill_name: "legalcode-employment-agreement-review"
  review_date: "[ISO date]"
  agreement_type: "[offer letter / employment agreement / executive agreement / amendment]"
  perspective: "[employee / employer / HR counsel / candidate]"
  seniority_tier: "[hourly / professional / senior management / C-suite / board]"
  review_context: "[new hire / promotion / acquisition / separation / equity grant]"
  governing_law: "[stated governing law jurisdiction]"
  work_location: "[employee primary work location jurisdiction]"
  jurisdiction_override: "[yes — non-compete void by work location law / no / unknown]"
  equity_present: "[yes / no / unknown]"
  public_company: "[yes / no / unknown — affects clawback and 280G analysis]"
  clawback_rule_10d1_applicable: "[yes / no / unknown]"
  ftc_rule_reliance: "N/A — FTC Non-Compete Rule vacated Aug 20 2024; FTC abandoned appeal Sept 5 2025"
  playbook_provided: "[yes / no — market standards applied]"
  clauses_analyzed: "[number]"
  red_findings: "[number]"
  yellow_findings: "[number]"
  green_findings: "[number]"
  dtsa_notice_present: "[yes / no — triggers fee recovery forfeiture if absent]"
  ending_forced_arb_act_analyzed: "[yes / no]"
  self_interrogation_applied: "[yes — N RED items reviewed / not applicable]"
  legalcode_mcp: "[Connected — citations verified / Not connected — citations marked VERIFY]"
  confidence_aggregate: "HIGH / MEDIUM / LOW — [1-sentence rationale]"
  limitations:
    - "[Any scope limitations, key assumptions, or caveats specific to this review]"
  reviewer: "AI-assisted — requires review by qualified employment attorney in [jurisdiction]"
```

---

## Anti-Patterns

What NOT to do when reviewing employment agreements:

1. **Stating the FTC Rule as authority.** The FTC Non-Compete Rule (16 CFR Part 910) was
   vacated by the Northern District of Texas on August 20, 2024 and never took effect.
   The FTC abandoned its appeal on September 5, 2025. Do not cite it as operative law.
   State law governs entirely.

2. **Blanket non-compete voiding without work-location analysis.** Non-competes are void
   in California, Minnesota, Oklahoma, and North Dakota — but _only for employees in those
   jurisdictions_. Do not apply California § 16600 to a Texas employee because the
   agreement happens to be drafted broadly.

3. **Assuming California § 16600 bars all IP-related restrictions.** California voids
   non-competes but not properly scoped non-disclosure agreements, customer non-solicitation
   (in some contexts), and trade secret protections under CUTSA. Do not conflate the
   non-compete ban with a total ban on post-employment restrictions.

4. **Ignoring work-location law when governing law differs.** Choice of law clauses
   cannot override California § 16600.5, Minnesota § 181.988, or other ban-state
   statutes for employees working in those states. Always identify both the stated
   governing law and the employee's work location.

5. **Missing the DTSA whistleblower immunity notice requirement.** 18 U.S.C.
   § 1836(b)(3)(C) requires that every agreement with a misappropriation claim element
   include the immunity notice. Without it, the employer forfeits attorney fees and
   exemplary damages in any subsequent trade secret claim — a significant litigation
   disadvantage. Do not overlook this even in boilerplate NDAs.

6. **Applying the same non-compete market standard to all seniority levels.** State
   law thresholds vary dramatically. Illinois and Colorado require minimum salary
   thresholds for enforcement. An executive-level non-compete analysis differs
   from a general professional analysis on duration, geographic scope, and consideration.

7. **Treating EU/UK garden leave as equivalent to US non-compete.** Garden leave
   (employee on payroll during restriction period) and post-employment non-competes are
   distinct legal mechanisms. In Germany, failing to provide Karenzentschädigung (50%
   compensation) during the restriction period voids the clause. In France, an
   uncompensated non-compete clause is void and the employee may claim compensation.

8. **Skipping the 280G analysis for executive agreements.** IRC § 280G exposure arises
   whenever CIC-conditioned payments exceed 3x the executive's 5-year average
   compensation. The screening is simple — do not skip it for C-suite agreements.
   Gross-up provisions are now rare in the market; flag them as RED for employer review.

9. **Missing double-trigger vs. single-trigger distinction.** Single-trigger equity
   acceleration (CIC alone, without termination) is material for acquisitions — acquirers
   dislike it because it creates immediate vesting cost. Failing to flag it deprives
   the employer of a critical negotiation point.

10. **Confusing "discretionary" and "contractual" bonus.** "Discretionary" bonus language
    may create no enforceable rights at all. Do not classify it as GREEN simply because
    it is standard practice to pay it — the legal obligation may be zero.

11. **Applying ADEA / OWBPA analysis only to formal severance agreements.** Any
    employment agreement that includes a release of claims for employees 40 or older
    must comply with ADEA's 21-day consideration period and 7-day revocation right.
    An agreement with an embedded release (common in executive agreements) triggers
    OWBPA requirements regardless of whether it is labeled "severance."

12. **Ignoring the Ending Forced Arbitration of Sexual Assault and Sexual Harassment
    Act.** This 2022 statute (Pub. L. 117-90) retroactively voids predispute arbitration
    clauses for sexual assault and sexual harassment claims at the claimant's election.
    It applies to employment agreements signed before March 3, 2022. Failing to note
    this in arbitration clause analysis produces a materially incomplete review.

13. **Treating IP assignment as a one-way analysis.** IP assignment clauses harm employees
    (overbroad assignment of pre-existing and off-duty IP) and harm employers (missing
    DTSA notice; absent assignment of patentable inventions; joint patent ownership
    default under 35 U.S.C. § 262 if assignment is ambiguous). Analyze from both
    directions.

14. **Conflating at-will disclaimers with cause definitions.** At-will employment means
    the employer can terminate for any reason; it does not define what "Cause" means for
    equity vesting acceleration, severance triggers, or non-compete activation. A strong
    at-will disclaimer does not substitute for a clear cause definition in executive
    agreements.

15. **Applying Australian moral rights waiver case law from memory without verification.**
    De Garis v. Neville Jeffress Pidler is commonly cited for the proposition that blanket
    moral rights waivers are of uncertain effect. Current Australian law post-2000
    amendments to the Copyright Act 1968 requires review. [VERIFY with current AU cases]

16. **Overlooking the California employee invention carve-out in non-California agreements.**
    Eight states (Delaware, Illinois, Minnesota, North Carolina, Washington, Nevada, and
    others — [VERIFY full list]) have equivalents to California Labor Code § 2870. A
    standard broad IP assignment clause may be void in the employee's work state even
    if the agreement is governed by another state's law.

17. **Using duration alone to classify non-compete severity.** Duration is one factor.
    A 24-month non-compete restricted to the employee's actual specialty in a small
    geographic area may be more enforceable than a 6-month clause that bars all
    competitive activity globally. Activity scope and geographic scope are often
    more dispositive.

18. **Missing post-termination exercise window ISO tax trap.** Any extension of the
    ISO exercise window beyond 90 days of separation automatically converts options
    to NQSOs for the extended period — the employee pays ordinary income tax on exercise
    rather than capital gains on sale. This is a significant economic difference. Do not
    evaluate extended exercise windows as purely favorable to the employee without
    flagging the tax characterization change.

19. **Classifying absence of non-compete as a gap.** The absence of a non-compete is
    not a gap from the employee's perspective — it is favorable. From the employer's
    perspective, it leaves competitive protection to trade secret law alone, which is
    appropriate in ban states. Do not recommend adding a non-compete where the work
    location prohibits it.

20. **Applying UK ERA 2025 Day-1 unfair dismissal protection without verifying
    commencement.** ERA 2025 received Royal Assent on December 18, 2025, but many
    provisions require commencement orders before taking effect. Do not state that
    Day-1 unfair dismissal protection is in force without verifying the commencement
    date. [VERIFY current commencement status]

21. **Skipping post-employment cooperation clause analysis.** Post-employment cooperation
    clauses (requiring the former employee to assist with litigation, regulatory
    investigations, etc.) can impose significant burdens. If indefinite and uncompensated,
    they may be restraints of trade. Do not treat them as boilerplate without analysis.

22. **Applying a single enforceability standard to non-solicitation and non-compete.**
    In California post-AMN Healthcare (2018), employee non-solicitation is subject to
    the same § 16600 analysis as non-competes. In most other jurisdictions, non-
    solicitation is analyzed under a more lenient standard than non-compete. Apply
    jurisdiction-specific case law to each covenant separately.

---

## Writing Standards

Before delivering any employment agreement review:

1. **Lead with actionable items.** The executive summary must identify the top three
   issues requiring immediate attention, not begin with background on the agreement type.

2. **Separate employee vs. employer framing.** State the perspective at the top of every
   section. A sentence that is advisory to an employee is the opposite of advisory to
   an employer.

3. **State assumptions explicitly.** Every time the analysis proceeds without confirmation
   from the user, declare the assumption and its effect (e.g., "Assuming employee will
   work primarily in California — if incorrect, the non-compete analysis changes entirely").

4. **Never assert unenforceable as guaranteed.** Courts apply multi-factor tests. Use
   "likely unenforceable," "substantial enforceability risk," and "should be reviewed by
   local counsel" rather than "void" unless the jurisdiction has a statutory ban.

5. **Mark [JURISDICTION-SPECIFIC] items.** Any analysis that depends on jurisdiction-
   specific law that has not been verified for the specific work location should be marked.

6. **Mark [VERIFY] items.** Any statute, case, or regulatory provision cited from memory
   should be marked [VERIFY] unless confirmed via legalcode-mcp or authoritative source.

7. **Avoid generic advice.** Do not write "consult an employment attorney" without identifying
   what specific question to ask and why it matters (e.g., "Consult California employment
   counsel on whether the IP assignment clause complies with Labor Code § 2870 given the
   employee's history of prior inventions").

8. **Redlines, not just criticisms.** Every RED or YELLOW finding must include a proposed
   redline or direction of redline, not just an identification of the problem. The goal
   is actionable output, not a list of problems.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current non-compete case law in the specific work-location jurisdiction
- Verify current state statutory thresholds (salary floors for enforceability in IL/CO/WA/OR)
- Confirm current status of ERA 2025 commencement orders (UK)
- Verify current AU moral rights case law
- Search for recent NLRB decisions affecting non-disparagement and confidentiality clauses
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with analysis using statutory citations and case law in this skill
- Mark all jurisdiction-specific enforceability determinations with [VERIFY]
- Specifically flag: NY NYCPLR Art. 4-C status, ERA 2025 commencement, Colorado/Illinois
  current salary thresholds, and recent California non-solicitation case law
- Note in Glass Box: `legalcode_mcp: "Not connected — citations marked VERIFY"`

---

## Output Format Template

````markdown
# Employment Agreement Review

**Date**: [Review date]
**Agreement**: [Agreement type and parties]
**Perspective**: [Employee / Employer / HR / Counsel]
**Governing Law**: [Stated governing law]
**Work Location**: [Employee primary work location — jurisdiction for restrictive
covenant analysis]
**Jurisdiction Override**: [Yes — [specific ban applies] / No / Unknown]

---

## Executive Summary

**Overall Assessment**: [One sentence: low / moderate / high risk; negotiation priority]

**Tier 1 — Must Address (N items)**:

1. [Issue] — [one line reason]
2. [Issue] — [one line reason]
   ...

**Tier 2 — Should Address (N items)**:

1. [Issue] — [one line reason]
   ...

**Tier 3 — Nice to Have (N items)**:

1. [Issue] — [one line reason]
   ...

---

## Structural Completeness

| Section       | Status                       | Priority                   |
| ------------- | ---------------------------- | -------------------------- |
| [Clause name] | Present / Absent / Deficient | RED / YELLOW / GREEN / N/A |
| ...           |                              |                            |

---

## Clause Analysis

### [Clause Name]

**Classification**: 🔴 RED / 🟡 YELLOW / 🟢 GREEN
**Confidence**: [Level] ([score])
**Business Impact**: [Critical / High / Medium / Low]

**Current Language** (key phrase):

> _"[Extracted operative language]"_

**Issue**: [1-2 sentences describing the problem or strength]

**Market Standard**: [What market-standard language looks like]

**Redline**:

> _"[Proposed replacement or addition language]"_

**Fallback Position** (if employer resists full redline):

> _"[Minimum acceptable alternative]"_

**Jurisdiction Note** (if applicable):
[Any jurisdiction-specific enforceability concern, marked [JURISDICTION-SPECIFIC]]

---

## [Repeat for each clause]

## Non-Compete Enforceability Summary

| Element                | Finding                                                       | Classification       |
| ---------------------- | ------------------------------------------------------------- | -------------------- |
| Duration               | [X months]                                                    | GREEN / YELLOW / RED |
| Geographic scope       | [description]                                                 | GREEN / YELLOW / RED |
| Activity scope         | [description]                                                 | GREEN / YELLOW / RED |
| Consideration          | [finding]                                                     | GREEN / YELLOW / RED |
| Work location override | [jurisdiction — ban applies / does not apply]                 | —                    |
| Overall enforceability | [Definite / High / Probable / Possible / Unlikely] confidence | —                    |

---

## Prioritized Negotiation Checklist

### Tier 1 — Must Resolve

- [ ] [Item] — Redline direction: [one line]
- [ ] ...

### Tier 2 — Should Negotiate

- [ ] [Item] — Redline direction: [one line]
- [ ] ...

### Tier 3 — Monitor

- [ ] [Item]
- [ ] ...

---

## Assumptions

[Numbered list of every assumption made in the absence of clarification]

---

## Glass Box Audit Trail

```yaml
[Completed YAML from Glass Box template above]
```
````

---

## Professional Review Recommendations

[Specific questions to raise with employment counsel, identified by name and jurisdiction]

```

---

## Localization Notes

### United States — Key Cross-State Issues
- Non-compete salary thresholds in IL/CO/WA/OR are adjusted periodically — [VERIFY
  current figures before applying the matrix]
- California AB 1076 required employers to notify employees with void non-competes by
  February 14, 2024 — if employer missed this deadline, civil penalty exposure persists
- New York NYCPLR Art. 4-C legislative history: signed by Governor Hochul but status
  contested — [VERIFY current enforcement status before applying]

### United Kingdom
- ERA 2025 (Royal Assent December 18, 2025): Multiple provisions require commencement
  orders. Day-1 unfair dismissal and zero-hours contract changes are announced but
  commencement dates vary. [VERIFY current commencement status at time of review]
- IR35 / off-payroll rules: If the agreement involves a personal service company, the
  determination of employment status (for tax and employment law) may differ from the
  contractual characterization

### European Union
- Posted Workers Directive 96/71/EC (as amended 2018/957): Employees posted to EU
  member states for more than 12 months are entitled to host-country employment law
  including minimum wages, maximum working time, and holiday pay
- EU Trade Secrets Directive 2016/943 — Art. 5 exceptions: Reverse engineering, disclosure
  for reporting unlawful activity, and freedom of expression all override NDA obligations
  regardless of contractual terms
- Non-compete financial compensation requirements: Germany (50% salary), France (30-60%
  salary), Netherlands (debate ongoing on abolition for fixed-term employees) —
  [VERIFY current NL law for fixed-term contracts]

### Australia
- Fair Work Act 2009 Modern Award interaction: Check whether applicable Modern Award
  imposes conditions that supersede the employment agreement (minimum wages, penalty
  rates, allowances)
- Restraint of Trade Act 1976 (NSW): Cascade clause technique — draft multiple
  restrictions of decreasing severity so courts can select the enforceable portion
  (e.g., 24 months / 12 months / 6 months with corresponding geographic reductions)

### India
- New Labour Codes: Four labour codes (Code on Wages, Industrial Relations Code, Social
  Security Code, Occupational Safety Code) have received Presidential assent but state
  implementation varies — [VERIFY current implementation status in the specific state]
- Senior/managerial exclusions: Industrial Disputes Act 1947 protections generally do
  not apply to "supervisors" earning above a salary threshold — threshold varies by state

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis. Research methodology: 2-agent
pipeline — Agent 1 (structural analysis: gold standard pattern extraction from
legalcode-contract-review, legalcode-nda-triage, legalcode-master-services-agreement,
legalcode-employee-handbook-review; 13-step workflow design; 17-clause architecture;
GREEN/YELLOW/RED classification system; dual-perspective framing; Tier 1/2/3 prioritization;
22 anti-patterns; output template) + Agent 2 (deep legal research: US non-compete —
FTC Rule vacatur Ryan LLC v. FTC (N.D. Tex. Aug 20, 2024) + FTC abandonment of appeal
Sept 5 2025; California § 16600/16600.1/16600.5 + Edwards v. Arthur Andersen 44 Cal.4th
937 (2008); Minnesota § 181.988 (eff. July 1, 2023); Oklahoma 15 Okla. Stat. § 219A;
North Dakota NDCC § 9-08-06; Washington RCW 49.62; Colorado CRS § 8-2-113; Illinois
820 ILCS 90/10; Oregon ORS 653.295; Nevada NRS 613.195; Massachusetts M.G.L. c. 149
§ 24L; New York NYCPLR Art. 4-C status; Texas Tex. Bus. & Com. Code § 15.50; Florida
Fla. Stat. § 542.335; UK ERA 1996 + ERA 2025 + CDPA 1988 + Patents Act 1977 + Tullett
Prebon; EU — Germany §§ 74-75f HGB; France droit de non-concurrence Soc. 14 mai 1992;
EU Trade Secrets Directive 2016/943; AU — Fair Work Act 2009 NES + Copyright Act 1968
s.35(6) + Restraint of Trade Act 1976 (NSW) + Cactus Imaging; IN — Contract Act 1872
s.27 + Niranjan Shankar Golikari [1967] 3 SCR 490; SEC Rule 10D-1 (17 CFR 240.10D-1
eff. Oct 2, 2023) + Dodd-Frank § 954 + SOX § 304; IRC § 280G/§ 4999; Ending Forced
Arbitration of Sexual Assault and Sexual Harassment Act 2022 Pub. L. 117-90; Viking River
Cruises 596 U.S. 639 (2022); McLaren Macomb 372 NLRB No. 58 (2023) non-disparagement;
DTSA 18 U.S.C. § 1836(b)(3)(C) whistleblower immunity; Copyright Act 17 U.S.C. § 101
work for hire; California Labor Code § 2870 employee invention carve-out; COBRA 29
U.S.C. §§ 1161-1168; ADEA/OWBPA consideration period requirements). ~1,350 lines.
```
