---
name: legalcode-guaranty-agreement-review
description: Review guaranty and surety agreements for scope, suretyship defenses, subrogation, contribution,
  and enforceability risks. Use when reviewing personal guaranties, parent company guaranties, corporate
  guaranties, bank guaranties, bad boy carve-out guaranties, keepwell agreements, or comfort letters in
  connection with commercial lending, real estate finance, lease transactions, construction finance, or
  supply chain credit support.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review guaranty and surety agreements for scope, suretyship defenses, subrogation, contribution, and enforceability risks. Use when reviewing personal guaranties, parent company guaranties, corporate guaranties, bank guaranties, bad boy carve-out guaranties, keepwell agreements, or comfort letters in connection with commercial lending, real estate finance, lease transactions, construction finance, or supply chain credit support. Covers continuing vs. specific guaranty analysis, waiver of suretyship defenses (RSG §§ 37-49 / UCC § 3-605), anti-deficiency statute exposure (California CCP §§ 580a-580d, one-action rule CCP § 726), subrogation deferral mechanics, contribution rights among co-guarantors, financial covenants and keepwell provisions, notice requirements, dollar cap and burn-off structures, and reinstatement clause risk. Also covers corporate authority, ultra vires risk, spousal/community property exposure, and UK Etridge undue influence protocol. Produces GREEN/YELLOW/RED/CRITICAL deviation classification with redlines, negotiation priority tiers, and Glass Box audit trail. Jurisdiction-agnostic with localization markers for US (NY/CA/AZ/TX), UK (England & Wales), and EU civil law systems.


# Legalcode Guaranty Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted guaranty and surety
> agreement review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use.
> Laws change; verify current applicability before relying on any provision described here.
> Suretyship law varies significantly by state — anti-deficiency statutes, the one-action
> rule, and waiver enforceability are highly jurisdiction-dependent. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill reviews guaranty and surety agreements across all commercial contexts. It
identifies scope risks, suretyship defense waivers, subrogation and contribution mechanics,
and enforceability issues, then generates confidence-scored, redlined analysis with an
auditable Glass Box trail.

**Covers:**

- Continuing vs. specific/limited guaranty analysis
- Payment vs. performance vs. collection guaranty classification
- Absolute/unconditional vs. conditional guaranty assessment
- Suretyship defense waiver review (RSG §§ 37-49; UCC § 3-605)
- Anti-deficiency and one-action rule exposure (US state-by-state)
- Subrogation rights — deferral vs. permanent waiver
- Contribution rights among co-guarantors
- Notice of default requirements and waivers
- Dollar cap, burn-off, and duration limitation analysis
- Reinstatement clause and bankruptcy clawback risk
- Corporate authority, ultra vires, and financial assistance restrictions
- Keepwell agreement and comfort letter vs. guaranty distinction
- Bad boy carve-out guaranty (non-recourse real estate)
- Financial covenants and reporting obligations for corporate guarantors
- Spousal/community property exposure
- UK Etridge undue influence protocol compliance
- Jurisdiction, governing law, and jury trial waiver

**Does not:**

- Draft new guaranty agreements from scratch (see drafting-specific skills)
- Provide legal advice or replace qualified counsel
- Substitute for jurisdiction-specific legal research — flag [JURISDICTION-SPECIFIC] items
  for local counsel review

**Related skills:**

- `legalcode-loan-agreement-review` — for the underlying credit agreement
- `legalcode-indemnification-analysis` — for indemnification obligations within guaranties
- `legalcode-commercial-lease-review` — for lease guaranties in real estate transactions
- `legalcode-contract-review` — for general commercial agreement review

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The guaranty's own governing law clause determines
the applicable legal framework. Identify governing law early and adapt analysis accordingly.

[JURISDICTION-SPECIFIC] Key jurisdiction variations to research:

**United States:**

- **California (most restrictive)**: CCP § 726(a) one-action rule; CCP §§ 580a, 580b,
  580d anti-deficiency statutes; Cal. Civil Code § 2856 waiver safe harbor (purchase money
  § 580b protection for owner-occupied 1-4 unit dwellings CANNOT be waived); sham guaranty
  doctrine; strictissimi juris construction [VERIFY current statute text]
- **New York**: No commercial real estate anti-deficiency statutes; N.Y. G.O.L. §§ 5-1401
  and 5-1402 enforce choice of law and forum clauses for transactions ≥ $250,000/$1M;
  broad enforcement of waiver provisions [VERIFY]
- **Arizona**: A.R.S. § 33-814 anti-deficiency for residential ≤ 2.5 acres; guarantors
  may waive § 33-814(G) protection per _Arizona Bank & Trust v. Barrons Trust_ (2015);
  fair value credit under § 33-814(A) CANNOT be waived [VERIFY]
- **Texas**: Property Code Ch. 51 non-judicial foreclosure; deficiency permitted after
  appraisal; strong homestead protections [VERIFY]
- **Nevada/Oregon**: One-action rule applies to varying degrees [VERIFY]

**United Kingdom (England & Wales):**

- Statute of Frauds 1677 s.4: guaranty must be evidenced in writing and signed
- _Royal Bank of Scotland v Etridge (No 2)_ [2001] UKHL 44: lender must ensure guarantors
  in non-commercial relationships receive independent legal advice (Etridge protocol)
- Companies Act 2006 §§ 678-680: financial assistance prohibition for public companies
- Companies Act 2006 §§ 172, 174: directors' duty to consider benefit to company

**EU Civil Law Systems:**

- France: Civil Code Arts. 2288-2320; Loi Dutreil consumer guaranty handwritten language
  requirement; proportionality principle for individual guarantors
- Germany: BGB §§ 765-778; BGB § 771 Einrede der Vorausklage (right to require exhaustion
  of principal remedies first, unless waived); BGH case law on disproportionate family
  guaranties as unconscionable under BGB § 138

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The user's side (guarantor vs. beneficiary) affects the entire risk framing
- Guaranty type or deal context is unclear and would materially affect classification
- Jurisdictional questions require resolution before analysis can proceed

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

### Step 1: Accept the Guaranty

Accept the guaranty document in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a document in a CLM or cloud storage system
- **Pasted text**: Guaranty text pasted directly into the conversation

If no guaranty is provided, prompt the user to supply one. If a keepwell agreement or
comfort letter is provided instead of a guaranty, flag the distinction early (see
Keepwell vs. Guaranty analysis in Step 5).

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask:

1. **Which side are you on?**
   - Options: **Guarantor** (reviewing for enforceability, exposure, and suretyship
     defenses), **Lender/Beneficiary** (reviewing for enforceability and gap coverage),
     **Neutral review** (due diligence, M&A, restructuring)
   - _Why this matters_: The entire risk framing flips. What is dangerous for a guarantor
     (broad scope, no defenses) is desirable for a lender.

2. **What type of transaction underlies the guaranty?**
   - Options: Commercial loan / credit facility, Real estate loan (recourse), Real estate
     loan (non-recourse with bad boy carve-outs), Lease guaranty, Construction guaranty,
     Supply chain / trade credit, Other
   - _Why this matters_: Bad boy carve-out review is a completely different analytical
     framework from a commercial loan guaranty review.

3. **What type of guarantor?**
   - Options: Individual (personal guaranty), Domestic corporation or LLC, Parent company
     (corporate guaranty of subsidiary's debt), Foreign entity, Trust, Multiple
     co-guarantors
   - _Why this matters_: Individual guarantors raise anti-deficiency, community property,
     and Etridge concerns. Corporate guarantors raise authority, fraudulent transfer, and
     financial assistance issues.

4. **Jurisdiction of the property/collateral (if real estate)?**
   - Options: California, Arizona, Texas, New York, Other US state (specify), England and
     Wales, Other (specify)
   - _Why this matters_: Anti-deficiency and one-action rule analysis is entirely
     state-specific.

5. **Deadline and deal context?**
   - Free text. Note deal size, whether there are co-guarantors, and any known concerns.
   - _Why this matters_: A guaranty for a $10M SBA loan gets different treatment than a
     $500M syndicated credit facility guaranty.

If partial context is provided, proceed with stated assumptions. Always state assumptions
explicitly at the top of the analysis.

### Step 3: Classify the Guaranty Type

Before clause-by-clause analysis, classify the guaranty along four dimensions. This
classification drives the severity framework.

**Dimension 1 — Scope:**

- **Continuing**: covers all obligations now existing or hereafter arising (maximum risk
  for guarantor)
- **Specific/Limited**: covers only an identified, discrete obligation

**Dimension 2 — Conditionality:**

- **Absolute/Unconditional (Guaranty of Payment)**: lender may pursue guarantor directly
  on default without exhausting principal or collateral
- **Conditional (Guaranty of Collection)**: lender must first exhaust remedies against
  principal before pursuing guarantor

**Dimension 3 — Nature of the Obligation:**

- **Payment guaranty**: guarantees monetary payment only
- **Performance guaranty**: guarantees non-monetary performance
- **Completion guaranty**: specific to construction — guarantees project completion by a
  specified date
- **Payment and performance guaranty**: covers both

**Dimension 4 — Instrument Type:**

- **Contractual guaranty**: governed by contract/suretyship law (this skill's primary focus)
- **Bank guaranty / Standby Letter of Credit**: governed by UCP 600 or ISP98 —
  independence principle applies; bank pays against complying documents, not on general
  default principles

**⟁ CLARIFY** — If the guaranty is labeled or appears to be a Standby Letter of Credit
or demand guarantee governed by UCP 600/ISP98, flag this to the user: "This instrument
appears to be an independent demand guarantee / standby letter of credit rather than a
contractual guaranty. The independence principle applies — enforcement is against
compliant documents, not the underlying contract. Shall I continue the analysis on that
basis?"

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law clause and use **legalcode-mcp** to gather applicable legal
authority before analyzing clauses.

**Research priorities:**

1. **Anti-deficiency statutes** in the collateral/property jurisdiction (if real estate
   security is involved): Are they applicable? Can the guarantor waive them?
2. **One-action rule** in the collateral/property jurisdiction
3. **Waiver enforceability** under the governing law: Which suretyship defenses can be
   waived? Are any non-waivable as a matter of public policy?
4. **Statute of Frauds** formality requirements in the governing jurisdiction
5. **Corporate authority** — any financial assistance or ultra vires rules applicable to
   the guarantor entity
6. **Consumer protection** — any guarantor-protection statutes applicable to individuals
   (FTC Credit Practices Rule [VERIFY]; Dodd-Frank implications [VERIFY])

Save results to `/tmp/legalcode-guaranty-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural risk assessment rather than legal certainty

**⟁ CLARIFY** — If the guaranty's governing law is unusual for the transaction type
(e.g., a California real estate loan governed by New York law), flag it: "The guaranty
selects New York governing law, but the collateral is California real estate. California's
anti-deficiency statutes (CCP §§ 580a, 580b, 580d) and the one-action rule (CCP § 726)
may apply regardless of the choice of governing law. Flag for local counsel review?"

### Step 5: Clause-by-Clause Analysis

Analyze all 13 clause categories below. Read the full guaranty before flagging issues —
provisions interact (e.g., a broad scope clause may be partially mitigated by a dollar
cap; a sweeping waiver-of-defenses provision may have carveouts).

| #   | Clause Category                              | Depth        | Key Review Points                                                                      |
| --- | -------------------------------------------- | ------------ | -------------------------------------------------------------------------------------- |
| 1   | Scope of Guaranteed Obligations              | Deep         | Continuing vs. specific; "hereafter arising" language; default interest/fees inclusion |
| 2   | Guaranty Type and Conditionality             | Deep         | Absolute vs. conditional; payment vs. performance vs. collection                       |
| 3   | Waiver of Suretyship Defenses                | Deep         | Which defenses waived; non-waivable protections; jurisdiction-specific limits          |
| 4   | Subrogation and Exoneration                  | Deep         | Deferral vs. permanent waiver; bankruptcy subrogation mechanics                        |
| 5   | Contribution Rights                          | Deep         | Co-guarantor allocation; contribution agreement; joint and several structure           |
| 6   | Notice Requirements                          | Standard     | Notice of default waived?; demand procedure; address and method                        |
| 7   | Dollar Cap and Duration Limits               | Deep         | Fixed cap; burn-off/step-down; sunset date; surviving obligations                      |
| 8   | Reinstatement Clause                         | Standard     | Clawback coverage; settlement vs. court order distinction                              |
| 9   | Corporate Authority and Representations      | Standard     | Board resolution; ultra vires; financial assistance (UK); fraudulent transfer risk     |
| 10  | Financial Covenants and Reporting            | Standard     | Minimum net worth; leverage ratios; reporting obligations; MAC triggers                |
| 11  | Keepwell / Financial Support Provisions      | Standard     | Keepwell vs. guaranty distinction; third-party beneficiary status; enforceability      |
| 12  | Bad Boy Carve-Out Provisions                 | Deep (if RE) | Type 1 (losses) vs. Type 2 (full recourse) triggers; third-party act risk              |
| 13  | Governing Law, Jurisdiction, and Jury Waiver | Standard     | Antideficiency forum shopping; New York choice; jury waiver enforceability             |

### Step 6: Missing Provision Detection

After analyzing present provisions, check for material absent provisions:

- **No Statute of Frauds compliance**: Writing and signature requirements met? [RED if not]
- **No limitation on guaranteed amount** in a continuing guaranty [RED]
- **No termination right** for guarantor in a continuing guaranty with no sunset [YELLOW]
- **No notice of default** to guarantor — waived without negotiation [YELLOW]
- **No contribution agreement** where multiple co-guarantors exist [YELLOW]
- **No reinstatement clause** — lender gap [RED for lenders; benefit for guarantors]
- **No carveout for fraud/gross negligence by lender** in a broad waiver-of-defenses clause
  [YELLOW for guarantors]
- **No corporate authority representation** for corporate guarantor [RED for lenders]
- **No governing law clause** [RED — flag jurisdiction uncertainty]

**⟁ CLARIFY** — Where severity depends on deal context not yet provided:

- "There is no dollar cap on this continuing guaranty. Is the underlying obligation a
  revolving credit facility that may grow over time? If yes, this is RED. If it is a fixed-
  term amortizing loan, it may be YELLOW."
- "There are multiple co-guarantors but no contribution agreement. Do you want me to treat
  this as a material gap (YELLOW) or draft contribution provisions for your review?"

### Step 7: Classify Deviations

Classify each issue using the four-tier framework in **Deviation Severity Classification**
below. For each:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate redline language, provide fallback position, estimate business impact.
- **RED**: Explain specific risk with legal basis; provide market-standard alternative
  language; estimate exposure; recommend escalation path.
- **CRITICAL**: Issue that must be resolved before the guaranty is executed / relied upon.

**⟁ CLARIFY** — For borderline classifications:

- "The waiver-of-defenses clause waives impairment of collateral defenses but does not
  specifically address the California one-action rule. Given the California collateral,
  should I treat the missing one-action waiver as RED (significant gap for lender) or YELLOW
  (may be covered by the general suretyship defense waiver)?"

### Step 8: Generate Redlines

For each YELLOW and RED deviation, produce a redline using the format in
**Redline Format** below.

**⟁ CLARIFY** — Before generating redlines, confirm negotiation posture:

- "For this review, should I produce (A) lender-favorable language, (B) guarantor-favorable
  language, or (C) market-standard balanced language?"

### Step 9: Business Impact Summary

Summarize:

- **Overall guarantor exposure**: Maximum liability amount (if determinable); key risks
- **Enforceability assessment**: Any provisions that may be unenforceable under governing law
- **Top 3 issues**: Most critical deviations with one-line summaries
- **Negotiation strategy**: Tiered priorities per the Negotiation Priority Framework
- **Anti-deficiency / one-action risk**: State-specific exposure summary (if applicable)

### Step 10: Quality Verification

Before delivering:

1. Run the 5 Citation Quality Gates silently.
2. For every RED/CRITICAL item, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each material analysis.
4. Verify all 13 clause categories addressed (present or flagged as missing).
5. Generate the Glass Box Audit Trail.

---

## Clause Analysis Reference

### 1. Scope of Guaranteed Obligations

**Key elements:**

- Does the scope clause say "all obligations, now existing or hereafter arising"? That
  creates a continuing guaranty regardless of the title of the document.
- Does it include: principal, interest at contract rate, interest at default rate, fees,
  costs, expenses, attorneys' fees, and indemnification obligations?
- Does it cover obligations under future loan documents not yet in existence?
- Is there a dollar cap on the maximum guaranteed amount?

**Common issues:**

- "Including without limitation" scope language — signals non-exhaustive list
- Coverage of swap/hedging obligations that may not be part of the primary credit facility
- No carveout for obligations arising after guarantor's exit from borrower entity
- Guaranty explicitly broader than the underlying principal obligation

**[JURISDICTION-SPECIFIC]** In California: Civil Code § 2837 requires strict construction
of guaranty agreements in favor of the guarantor — ambiguity in scope resolved for
guarantor. [VERIFY]

---

### 2. Guaranty Type and Conditionality

**Key elements:**

- Is the guaranty an unconditional guaranty of payment (lender proceeds directly on
  default) or a guaranty of collection (lender must first exhaust principal/collateral)?
- Does it include a completion guaranty or performance component?
- Is there a demand/presentment mechanism, or are all such requirements waived?

**Common issues:**

- Title says "Guaranty of Payment" but operative language conditions payment on demand —
  may be interpreted as conditional. Substance controls over label.
- Performance guaranty without a clear measure of damages for non-performance

**RED flag:** A guaranty that fails to specify whether it is a payment or collection
guaranty, and whose governing law defaults to collection — the lender must exhaust
principal remedies first, which may take years in a judicial foreclosure state.

---

### 3. Waiver of Suretyship Defenses — Deep Analysis

This is the most critical and most litigated provision. Analyze each category of
defense separately.

**Tier A — Standard Commercial Waivers (Lender-Standard):**

| Defense                                              | Waivable? | Notes                                              |
| ---------------------------------------------------- | --------- | -------------------------------------------------- |
| Notice of acceptance of guaranty                     | Yes       | Routinely waived                                   |
| Notice of default/nonpayment                         | Yes       | Routinely waived; guarantors resist                |
| Diligence, presentment, demand, protest              | Yes       | Routinely waived                                   |
| Exhaustion of remedies against principal             | Yes       | Critical: makes guaranty of payment vs. collection |
| Marshaling of collateral                             | Yes       | Routinely waived in commercial lending             |
| Impairment of collateral (RSG § 42 / UCC § 3-605(d)) | Yes       | Highly negotiated                                  |
| Modification of underlying obligation (RSG § 39)     | Yes       | Routinely waived; see _Greenwalt_ caveat           |
| Extension of time to pay (RSG § 40)                  | Yes       | Routinely waived                                   |
| Release of co-guarantor (RSG § 43-49)                | Yes       | Important in multi-guarantor structures            |
| Consent to enter new credit extensions               | Yes       | Often included in continuing guaranty              |

**Tier B — Jurisdiction-Specific Waivers:**

| Defense                                                                         | Waivable?                        | Notes                                          |
| ------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------- |
| California anti-deficiency CCP § 580d (non-judicial foreclosure)                | **Yes** — Cal. Civil Code § 2856 | Safe harbor language required; see § 2856(d)   |
| California anti-deficiency CCP § 580b (purchase money, 1-4 unit owner-occupied) | **No**                           | Statutory prohibition on waiver; public policy |
| California one-action rule CCP § 726(a)                                         | Yes — Cal. Civil Code § 2856     | Safe harbor language required                  |
| Arizona anti-deficiency A.R.S. § 33-814(G)                                      | Yes — per _Barrons Trust_ (2015) | Explicit language required                     |
| Arizona fair value credit § 33-814(A)                                           | **No**                           | Cannot be waived                               |

**Tier C — Non-Waivable Protections (Universal):**

| Defense                                              | Notes                                                                                                                 |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Lender's own fraud against the guarantor             | May not be waived as against public policy in most jurisdictions [VERIFY]                                             |
| Void underlying obligation                           | If the principal obligation is void (not merely voidable), the guaranty may fail for lack of an underlying obligation |
| UK Etridge undue influence                           | Cannot be prospectively waived; must be procedurally addressed                                                        |
| German family guaranty unconscionability (BGB § 138) | Non-waivable for economically dependent family members [VERIFY]                                                       |

**CRITICAL — Indiana Greenwalt Caveat:** In _First Federal Bank v. Greenwalt_ (Ind. Ct.
App. 2015), the court held that a guarantor was discharged by a material loan modification
(conversion of revolving LOC to installment loan) despite broad waiver language, finding
the waiver did not specifically cover that modification type. [VERIFY current status]
**Practical implication**: General waivers may not be fully reliable for subsequent material
modifications. Lenders should obtain reaffirmation letters from guarantors concurrent with
each material modification of the credit agreement.

**RED flags for guarantors:**

- Waiver of ALL suretyship defenses with no carveouts for lender misconduct
- California § 2856 waiver of all anti-deficiency protections on residential property
- Permanent (not merely deferred) waiver of subrogation rights

**RED flags for lenders:**

- Absence of impairment of collateral waiver when UCC-1 financing statements are involved
- Absence of modification/extension defense waiver in a revolving or multi-draw facility
- Missing California Civil Code § 2856 "safe harbor" language for California real property

---

### 4. Subrogation and Exoneration Rights

**What subrogation provides:** Upon paying the guaranteed obligation, the guarantor is
subrogated to the lender's entire claim against the principal — including security
interests, priority in bankruptcy, and all collection remedies.

**Market structure:**

- **Lender-standard**: Subrogation rights deferred until the entire principal obligation
  is fully and finally paid (protects lender in principal's bankruptcy from guarantor's
  competing priority claim)
- **Guarantor-preferred**: Subrogation preserved immediately upon payment; at minimum,
  pro-rata subrogation upon partial payment

**Bankruptcy mechanics:**
Under 11 U.S.C. § 509, a co-debtor/guarantor who pays part of a claim is subrogated only
after the creditor is fully paid. A contractual deferral of subrogation reinforces this
statutory position. [VERIFY]

**Exoneration right (RSG §§ 17-25):** A guarantor may seek a court order requiring the
principal to pay the creditor, thereby avoiding the guarantor's need to pay and then seek
reimbursement. This right exists independently of the guaranty and may not be waivable.
[VERIFY jurisdiction-specific treatment]

**RED flags:**

- **Permanent waiver** of subrogation rights (not merely deferral until full payment)
- Permanent subrogation waiver combined with a reinstatement clause — guarantor pays, is
  clawed back, and has no subrogation remedy
- Subrogation deferral that persists indefinitely with no clear release mechanism after
  full repayment

---

### 5. Contribution Rights Among Co-Guarantors

**Key elements:**

- Are multiple guarantors jointly and severally liable?
- Is there a contribution agreement allocating pro-rata liability?
- What is the allocation methodology — equal shares, ownership percentage, net worth?
- Is there a waterfall or priority among guarantors?
- Does the contribution right trigger automatically upon payment, or require a separate
  claim?

**Common issues:**

- Multiple guarantors, each jointly and severally liable for 100% of the debt, with no
  contribution agreement — the paying guarantor must sue co-guarantors under equitable
  contribution principles, which may be expensive and uncertain
- Release of one co-guarantor without reserving contribution rights of remaining
  co-guarantors
- Contribution obligation not waivable by lender without all guarantors' consent

**RED flag for guarantors:** Joint and several guaranty with no contribution agreement
and co-guarantors of unequal creditworthiness — the solvent guarantor bears the entire
debt if co-guarantors are insolvent.

---

### 6. Notice Requirements

**Key elements:**

- Is the guarantor entitled to receive copies of default notices sent to the principal?
- Has the right to demand/notice been waived entirely?
- How is demand made — written demand to guarantor's address? email? through lender's
  counsel?
- What triggers the guarantor's payment obligation — principal's default, acceleration,
  written demand on guarantor, expiry of cure period?

**Common issues:**

- Guaranty waives all notice, meaning guarantor learns of default only when sued
- Demand mechanism ambiguous — guarantor argues no valid demand was made
- No address update obligation — notice sent to stale address is ineffective

**YELLOW flag for guarantors:** Waiver of all notice of default without any concurrent
notification requirement removes the guarantor's ability to: (a) cure the principal's
default; (b) negotiate a workout; (c) exercise rights against the principal before value
deteriorates.

**Negotiation point:** Guarantors should seek at minimum a concurrent copy of any
notice of default sent to the principal, with a short cure period (5-10 business days)
before the lender can demand from the guarantor.

---

### 7. Dollar Cap and Duration Limitations

**Dollar cap structures:**

| Structure                  | Description                                                                | Risk Level            |
| -------------------------- | -------------------------------------------------------------------------- | --------------------- |
| No cap, unlimited          | Guarantor bears full exposure including default interest, fees, costs      | Highest for guarantor |
| Fixed cap (principal only) | Cap equals original principal amount, excluding default interest and costs | Moderate              |
| Cap + defined costs        | Cap equals principal + defined additional amount for interest and fees     | Market standard       |
| Burn-off/step-down         | Cap reduces as loan is amortized or milestones achieved                    | Guarantor-favorable   |
| Springing cap              | Cap increases upon specified events (construction loan conversion)         | Watch carefully       |

**Duration structures:**

| Structure                  | Description                                                            | Risk Level                      |
| -------------------------- | ---------------------------------------------------------------------- | ------------------------------- |
| No expiration, continuing  | Guaranty remains in force until full payment of all obligations        | Highest for guarantor           |
| Fixed sunset date          | Guaranty expires on a specified date regardless of outstanding balance | Guarantor-favorable             |
| Milestone termination      | Terminates on project completion, lease expiry, or loan payoff         | Common in specific transactions |
| Ownership exit termination | Terminates when guarantor ceases to own equity in principal            | Heavily negotiated              |

**RED flags:**

- Unlimited continuing guaranty with no dollar cap and no duration limit — maximum
  guarantor risk
- Attorneys' fees and enforcement costs within the guaranteed amount with no cap
- "Springing" cap that increases beyond the originally disclosed guaranteed amount
- Duration that survives past loan maturity due to guaranty's coverage of
  "all obligations including indemnification and expense reimbursement"

---

### 8. Reinstatement Clause

**What it does:** Provides that if a principal payment is rescinded or avoided in
bankruptcy (preferential transfer under 11 U.S.C. § 547 or fraudulent transfer under
§ 548), the guarantor's obligation is automatically reinstated as if the payment had
never been made.

**Why it matters:**

- **For lenders**: Critical gap protection — without it, a clawback of the principal's
  payment may permanently extinguish the guaranty
- **For guarantors**: Creates ongoing exposure even after the principal debt is paid;
  exposure persists until the Bankruptcy Code's look-back periods expire (2 years for
  constructive fraud under § 548; up to 10 years for actual fraud under state law
  via § 544 [VERIFY])

**Scope analysis:**

| Coverage                            | Market Practice                                                 |
| ----------------------------------- | --------------------------------------------------------------- |
| Court-ordered return of payment     | Clearly covered by standard reinstatement clause                |
| Settlement-based return (voluntary) | Check expressly — some clauses cover only court-ordered returns |
| Partial payment avoidance           | Reinstatement should be proportionate to amount returned        |

**RED flag for lenders:** No reinstatement clause in a guaranty where the principal is
a financially distressed entity.

**YELLOW flag for guarantors:** Reinstatement clause covers settlements (voluntary
returns) — guarantor should verify the clause is limited to court-ordered avoidance
actions.

---

### 9. Corporate Authority and Representations

**Key elements:**

- Has the guarantor's board of directors authorized the guaranty by resolution or written
  consent?
- Does the guarantor's charter or operating agreement restrict the giving of guaranties
  to affiliates?
- Do any existing debt agreements (credit agreements, indentures) contain negative
  covenants restricting the guarantor from giving additional guaranties?
- For upstream/cross-stream guaranties: does the guarantor receive "reasonably equivalent
  value" for the guaranty (fraudulent transfer analysis)?

**UK-specific:**

- Companies Act 2006 §§ 678-680: a public company (plc) may not give financial assistance
  — including a guaranty — in connection with the acquisition of its own shares [VERIFY
  current exemptions]
- Independent directors must document their consideration of the company's benefit

**Fraudulent transfer risk (11 U.S.C. § 548 / § 544):**
An upstream guaranty (subsidiary guarantees parent's debt) or cross-stream guaranty
(affiliate guarantees affiliate's debt) may be avoided in bankruptcy if:
(a) The guarantor received less than reasonably equivalent value, AND
(b) The guarantor was insolvent, rendered insolvent, or left with unreasonably small capital

Mitigation: Document corporate benefit — e.g., guarantor benefits from parent's ability
to draw on the credit facility for group-wide needs, creating a direct economic benefit
to the subsidiary.

**CRITICAL flags:**

- No board resolution authorizing the guaranty for a corporate guarantor
- Guaranty that appears to violate negative covenants in existing debt instruments
- UK public company guaranty in connection with a share acquisition — may be void

---

### 10. Financial Covenants and Reporting Obligations

**Key elements (corporate guarantors):**

- Minimum tangible net worth maintained at all times
- Maximum leverage ratio (total debt / EBITDA or debt / equity)
- Minimum liquidity (unrestricted cash and equivalents)
- Restrictions on dividends, distributions, and related-party transfers
- Restrictions on additional indebtedness
- Annual audited financial statements (typically within 90-120 days of fiscal year end)
- Quarterly unaudited financials
- Prompt notification of material adverse change

**Common issues:**

- Financial covenants in the guaranty that mirror the borrower's covenants — any
  breach of either set triggers a default
- MAC event of default that accelerates the guaranty on mere financial deterioration —
  extremely broad and subjective trigger
- Financial covenant breach that triggers an obligation to cash collateralize or post
  substitute collateral — liquidity disruption
- No EBITDA add-backs for non-cash items — artificially restricts headroom

**YELLOW flag:** MAC definition in the guaranty that is broader or less defined than the
MAC definition in the underlying credit agreement creates divergent default triggers.

---

### 11. Keepwell and Financial Support Provisions

**Keepwell vs. Guaranty — Critical Distinction:**

| Instrument               | Direct Payment Obligation?                   | Enforcement                    | Risk Level |
| ------------------------ | -------------------------------------------- | ------------------------------ | ---------- |
| Guaranty                 | Yes — guarantor pays on demand               | Lender enforces directly       | Highest    |
| Keepwell Agreement       | No — parent maintains subsidiary's solvency  | Breach of contract action only | Moderate   |
| Equity Commitment Letter | No — parent contributes equity on conditions | Breach of contract action only | Moderate   |
| Comfort Letter           | No — statement of intent only                | Non-binding; no legal remedy   | Lowest     |

**Where keepwell provisions appear alongside a guaranty:**
Review whether the keepwell provisions impose obligations consistent with the guaranty
scope, or whether they create divergent obligations. If a keepwell breach also constitutes
a guaranty default, document the trigger mechanism.

**Chinese keepwell deed warning:** For transactions involving PRC-domiciled keepwell
obligors, enforceability in PRC courts is highly uncertain. Courts may characterize the
keepwell deed as an unregistered foreign guaranty requiring SAFE approval.
[VERIFY current PRC regulatory status] Flag for specialist PRC counsel.

**RED flag:** A document labeled "Guaranty" that contains only keepwell-type general
support covenants and no direct payment obligation may not be enforceable as a guaranty —
the lender could be left with only a breach of contract action for damages. [VERIFY
against the operative language, not the label]

---

### 12. Bad Boy Carve-Out Provisions (Non-Recourse Real Estate)

This section applies only to non-recourse commercial real estate loans with guaranty
carve-outs. Skip if not applicable.

**Two-tier carve-out structure:**

**Type 1 — Losses/Indemnity Triggers (Guarantor Pays Actual Losses Only):**
Guarantor liable for actual loss caused by:

- Fraud or material misrepresentation to lender
- Misappropriation of rents, security deposits, insurance proceeds, or condemnation awards
- Gross negligence or willful misconduct
- Intentional physical waste of the property
- Failure to pay property taxes (causing a tax lien ahead of the mortgage)
- Arson or willful destruction
- Environmental contamination

**Type 2 — Full Recourse Triggers (Entire Loan Balance Becomes Recourse):**
Guarantor liable for the entire outstanding loan balance upon:

- Voluntary bankruptcy filing by the borrower/SPE
- Collusive or consented-to involuntary bankruptcy petition
- Violation of Single Purpose Entity (SPE) / separateness covenants
- Unauthorized transfer of the property or ownership interests
- Unauthorized subordinate debt or encumbrances
- Material interference with lender's exercise of remedies
- Violation of "prohibited transfers" provisions

**Critical case law:**

- _Cherryland Mall_ (Michigan): Court enforced full-recourse trigger when borrower became
  insolvent due to market deterioration — not a "bad act." Michigan legislature responded
  with MCL § 445.1591 prohibiting solvency covenant triggers [VERIFY other states]
- _CP III Rincon Towers_ (N.Y.): Courts interpret carve-outs narrowly based on commercial
  intent; carve-outs will not be expanded by implication

**RED flags for guarantors:**

- Type 2 full-recourse triggers for administrative/technical separateness violations
  rather than intentional misconduct
- No notice-and-cure right for Type 2 triggers
- Full-recourse trigger for solvency covenant violation (Cherryland risk)
- Type 2 triggers that can be activated by third parties (mezzanine lenders after equity
  foreclosure) outside the guarantor's control — guarantor loses control but retains
  liability
- Aggressive definition of "voluntary bankruptcy" that includes consenting to an
  involuntary petition without actual cooperation

**YELLOW flags for lenders:**

- Type 2 trigger list does not cover unauthorized subordinate debt
- No "material" qualifier on separateness covenant violations — minor administrative
  breaches should not trigger full recourse
- No provision for liability to pass to successor controlling party after equity
  foreclosure by mezzanine lender

---

### 13. Governing Law, Jurisdiction, and Jury Waiver

**Key elements:**

- What governing law applies to the guaranty? Same as the underlying credit agreement?
- Is the choice of law clause broad (covering formation, interpretation, enforcement,
  and defenses) or narrow?
- Is the forum selection clause exclusive or permissive?
- Is there a jury trial waiver? Is it mutual?
- Does the governing law choice effectively contract out of mandatory state anti-deficiency
  protections?

**New York governing law:**
N.Y. G.O.L. § 5-1401 allows parties to select New York governing law for transactions
≥ $250,000 regardless of nexus; § 5-1402 allows New York courts for transactions ≥ $1M.
New York has no anti-deficiency statutes for commercial real estate — lenders prefer New
York for this reason. [VERIFY current thresholds]

**Anti-deficiency jurisdiction shopping risk:**
A New York choice of law clause does not necessarily override California anti-deficiency
protections for California real property collateral. California courts have held that
CCP §§ 580a-580d are mandatory statutory protections that apply regardless of the
parties' choice of law. [VERIFY current status — subject to ongoing litigation]

**RED flag:** A New York choice of law provision in a guaranty securing California real
estate, without California Civil Code § 2856 waiver language — the anti-deficiency
defense may survive despite the New York choice.

---

## Deviation Severity Classification

### CRITICAL — Must Resolve Before Execution

Issues that make the guaranty defective or unenforceable as drafted, or that expose a
party to catastrophic unintended liability:

- Guaranty not in writing and signed by guarantor (Statute of Frauds violation)
- No corporate authority documentation for a corporate guarantor
- UK public company financial assistance violation (Companies Act 2006 §§ 678-680)
- Guaranty scope clearly different from the obligation actually intended to be guaranteed
- Guaranty appears to be a standby letter of credit or demand guarantee but is being
  treated as a contractual guaranty (fundamental misclassification)
- Missing reinstatement clause in a guaranty for a financially distressed principal
  (lender side)

### RED — Escalate

Material risk requiring senior counsel review:

**For guarantors:**

- Unlimited continuing guaranty (no dollar cap, no duration limit)
- Complete and permanent waiver of all suretyship defenses including impairment of
  collateral and fraud/gross negligence by lender
- Permanent (not deferred) waiver of subrogation rights
- California § 2856 waiver of § 580b purchase money protection for owner-occupied
  residential property (non-waivable — void provision)
- Type 2 bad boy triggers that include solvency covenant violations (_Cherryland_ risk)
- No notice of default, no cure period, and no concurrent notification to guarantor
- Joint and several guaranty with no contribution agreement and financially unequal
  co-guarantors

**For lenders:**

- Guaranty of collection (not payment) when guaranty of payment was intended
- No reinstatement clause for distressed principal
- Missing impairment-of-collateral waiver where UCC filings are critical
- California real estate collateral without California Civil Code § 2856 waiver language
- No corporate authority representation from corporate guarantor

### YELLOW — Negotiate

Outside preferred position but within negotiable range:

- Fixed dollar cap that excludes default interest and enforcement costs (negotiate to
  include with a cap on costs)
- No termination right for guarantor in a continuing guaranty (negotiate: right to
  terminate with 30-90 days' notice)
- Notice of default waived without concurrent notification right (negotiate: concurrent
  copy of any principal default notice)
- Subrogation deferred with no clear release mechanism after full repayment (negotiate:
  express release upon final payment certificate)
- No contribution agreement among co-guarantors (negotiate: separate contribution letter)
- MAC event of default in guaranty that is broader than in the credit agreement (negotiate:
  align with credit agreement MAC definition)

### GREEN — Acceptable

- Dollar cap at or above the total committed principal, including defined costs provision
- Subrogation deferred (not permanently waived) until full repayment — market standard
- Concurrent copy of default notices to guarantor alongside waiver of exhaustion
- Contribution agreement expressly documented
- Corporate authority confirmed by board resolution
- New York governing law with jury trial waiver for a commercial lending transaction

---

## Redline Format

For each YELLOW or RED deviation:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote]"
**Issue**: [One-sentence description of the specific problem]
**Proposed redline**: "[Specific alternative language]"
**Rationale**: [1-2 sentences, suitable for external sharing with counterparty's counsel]
**Legal basis**: [Specific statute, RSG section, case, or market standard — or "General
  commercial practice" — mark [VERIFY] if unverified]
**Priority**: [Tier 1 (must-have) / Tier 2 (should-have) / Tier 3 (nice-to-have)]
**Fallback**: [Alternative position if primary redline is rejected]
**Confidence**: [Definite / High / Probable / Possible]
```

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

**For guarantors:**

- Dollar cap or removal of "hereafter arising" language in continuing guaranty
- Preservation of non-waivable statutory protections (CCP § 580b; Arizona fair value)
- Removal of solvency covenant as Type 2 bad boy trigger
- Carveout for lender's own fraud/gross negligence from defense waivers
- Corporate authority confirmed before execution

**For lenders:**

- Guaranty of payment (not collection)
- Reinstatement clause for distressed borrower situations
- Impairment-of-collateral waiver where UCC security interests are critical
- California § 2856 safe harbor language for California collateral
- Concurrent corporate authority documentation

### Tier 2 — Should-Haves (Strong Preferences)

**For guarantors:**

- Termination right upon notice (continuing guaranty)
- Concurrent notification of default (with short cure period)
- Contribution agreement among co-guarantors
- Subrogation deferral (not permanent waiver) with express release mechanism
- Limitation of Type 2 bad boy triggers to intentional acts with notice/cure

**For lenders:**

- Modification/extension defense waiver (key for revolving/multi-draw facilities)
- Co-guarantor cross-default provisions
- Financial covenant reporting obligations for corporate guarantors
- Reserve rights language in any release of principal or co-guarantor

### Tier 3 — Nice-to-Haves (Concession Candidates)

**For guarantors:**

- Automatic termination upon exit from borrower entity
- MAC definition aligned with credit agreement
- Limitation of reinstatement clause to court-ordered avoidance (not voluntary settlement)
- No-notice setoff period (negotiate: 3-5 business days' notice)

**For lenders:**

- Specific acknowledgments of each waived defense by the guarantor
- Annual reaffirmation letters for long-term continuing guaranties
- Additional representation regarding guarantor's no-litigation/no-dispute status

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before
delivering.

| Gate           | Rule                                                                                        | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, RSG section, case, or established principle     | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                 | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal (suretyship law evolves frequently)  | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the guaranty's governing law. No assumptions from other jurisdictions | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                   | Add confidence qualifier                                 |

### Self-Interrogation for RED/CRITICAL Items

For any clause classified as RED or CRITICAL, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity:** Does the risk assessment follow logically from the
cited statute/principle? Would a court in this jurisdiction actually reach this conclusion?
What will the counterparty's counsel argue?

**Pass 2 — Completeness:** Have all relevant statutes and suretyship principles been
considered? Are there state-specific defenses not yet addressed?

**Pass 3 — Challenge:** What is the strongest argument that this provision is acceptable?
Under what commercial circumstances might a reasonable lawyer accept this risk?

Mark the audit trail `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute                       | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments, could differ by jurisdiction     | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review                               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every guaranty review output MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-guaranty-agreement-review"
  document: "[Guaranty title, parties, and date]"
  guaranty_type: "[Continuing/Specific; Payment/Performance/Collection; Absolute/Conditional]"
  reviewing_party: "[Guarantor / Lender / Neutral]"
  underlying_transaction: "[Loan / Lease / Construction / Other]"
  governing_law: "[Jurisdiction identified from the guaranty]"
  collateral_jurisdiction: "[Jurisdiction where collateral/property is located]"
  clauses_reviewed: 13
  clauses_present: "[number]"
  clauses_missing: "[number] — [list with severity]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  market_standards_applied:
    - "[RSG (Third) / UCC 3-605 / LSTA standard / LMA standard]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED/CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  anti_deficiency_jurisdiction: "[State — applicable statutes and waivability assessed]"
  limitations:
    - "[Any scope limitations, missing schedules, jurisdiction-specific caveats]"
  reviewer:
    "AI-assisted — requires qualified legal review, especially for jurisdiction-
    specific anti-deficiency, one-action rule, and waiver enforceability analysis"
```

---

## Multi-Stakeholder Mapping

Identify all affected stakeholders — not just the guarantor and lender:

| Stakeholder                         | Role        | Affected Provisions                                | Impact                               | Action Required                                |
| ----------------------------------- | ----------- | -------------------------------------------------- | ------------------------------------ | ---------------------------------------------- |
| Guarantor                           | Primary     | All                                                | Signs guaranty; maximum exposure     | Full review; obtain independent counsel        |
| Lender/Beneficiary                  | Primary     | All                                                | Enforces guaranty                    | Ensure authority; confirm defenses waived      |
| Co-guarantors                       | Secondary   | Contribution, joint liability                      | Contribution risk                    | Confirm contribution agreement                 |
| Principal Obligor                   | Secondary   | Scope, subrogation, notice                         | Guarantor may subrogate against them | Informed consent of principal advisable        |
| Non-signing spouse                  | Third party | Community property scope                           | Personal property exposed            | Require signature in community property states |
| Principal's bankruptcy estate       | Third party | Reinstatement, subrogation, fraudulent transfer    | Clawback risk                        | Fraudulent transfer analysis                   |
| Existing creditors of guarantor     | Third party | Financial covenants, negative pledge               | Covenant conflict risk               | Review guarantor's existing debt covenants     |
| Regulatory approvals (cross-border) | Regulator   | SAFE approval (PRC); financial assistance (UK plc) | Void guaranty risk                   | Confirm regulatory compliance pre-execution    |

---

## Anti-Patterns

What NOT to do in guaranty agreement review:

1. **Reviewing label, not substance** — Courts look to operative language, not titles. A
   document titled "Guaranty of Collection" may be an absolute guaranty of payment; a
   document titled "Support Agreement" may be an enforceable guaranty. Always read the
   operative language.

2. **Applying governing law without checking mandatory state rules** — A New York choice
   of law clause does not override California anti-deficiency statutes for California
   collateral. Mandatory forum rules apply regardless of choice-of-law provisions.

3. **Treating all suretyship defense waivers as equally valid** — Waivability depends
   on jurisdiction. California CCP § 580b purchase money protection cannot be waived for
   owner-occupied 1-4 unit dwellings. The fair value credit requirement in Arizona cannot
   be waived. Check each jurisdiction before confirming a waiver's validity.

4. **Assuming a continuing guaranty terminates upon asset sale or ownership transfer** —
   Unless the guaranty expressly provides for termination upon guarantor exit, a guarantor
   who sells their equity stake may remain bound by obligations that arose before the sale
   for the remainder of the guaranty's term.

5. **Missing the subrogation deferral / permanent waiver distinction** — Deferral until
   full repayment is market standard. Permanent waiver strips the guarantor of reimbursement
   rights entirely. Confusing the two is a significant analytical error.

6. **Ignoring co-guarantor contribution mechanics** — Joint and several guaranties always
   require contribution analysis. When one guarantor pays the full debt, the contribution
   right against co-guarantors may be the only recourse. An absent contribution agreement
   is a material gap.

7. **Overlooking the reinstatement clause for distressed credits** — In any transaction
   where the principal's financial condition is challenged, the reinstatement clause
   determines whether a bankruptcy clawback reinstates the guaranty. Treating this as
   boilerplate is a serious analytical error.

8. **Failing to verify corporate authority** — A guaranty signed by an officer who lacks
   authority under the corporation's governing documents or whose signing creates a
   covenant violation under existing credit agreements may be void or voidable. This is
   one of the most common guaranty enforcement failures.

9. **Bad boy carve-out analysis without the bankruptcy implications** — Type 2 full-
   recourse triggers activate when the SPE/borrower files voluntary bankruptcy. This
   creates a paradox: the guarantor cannot consent to bankruptcy without triggering personal
   full recourse, but refusing to consent may breach fiduciary duties owed to the entity.
   Guarantors must understand this tension before signing.

10. **Ignoring community property exposure** — In California, Texas, Arizona, Nevada,
    Washington, Idaho, Louisiana, New Mexico, and Wisconsin, a personal guarantor's
    community property may be reachable even without the non-signing spouse's consent to
    the guaranty. Lenders should require both spouses' signatures to maximize recovery.
    Guarantors should understand their community property is at risk.

11. **Treating the Etridge protocol as a formality** — A UK lender who fails to ensure a
    non-commercial guarantor (spouse, family member, nominal shareholder) received proper
    independent legal advice will be unable to enforce the guaranty against that guarantor.
    This is not merely a compliance checkbox — it is an enforceability prerequisite.

12. **Drafting or reviewing keepwell agreements as though they are guaranties** — Keepwell
    agreements do not give the lender a direct claim for payment. If the transaction
    requires a credit support instrument enforceable on demand, a guaranty is required.
    Lenders who accept keepwell agreements instead of guaranties may find themselves with
    only a breach of contract damages claim that requires litigation.

13. **Missing the Greenwalt caveat on general waiver provisions** — Broad general waivers
    of "all suretyship defenses" may not reliably cover every subsequent material
    modification of the credit agreement in all jurisdictions. For any revolving or
    multi-draw facility, obtain specific modification acknowledgments from guarantors upon
    each material amendment.

14. **Not analyzing the guaranty's relationship to the underlying obligation** — A
    guaranty may be broader, narrower, or identical to the principal obligation. Guaranty
    provisions broader than the underlying obligation are generally unenforceable to the
    extent of the excess. Check scope alignment carefully.

15. **Skipping the fraudulent transfer analysis for upstream/cross-stream guaranties** —
    An affiliate or subsidiary guaranty given without adequate consideration may be avoided
    as a fraudulent transfer in bankruptcy. In multi-guarantor structures, document the
    corporate benefit each guarantor receives from the underlying credit facility.

16. **Ignoring PRC keepwell deed enforceability** — For transactions involving Chinese
    entities, keepwell deeds have been extensively used as credit support but face
    significant enforceability risk in PRC courts, particularly post-2021 real estate
    sector defaults. Treat PRC keepwell deeds with substantially more skepticism than
    their equivalent in US/UK law.

17. **Not checking for cross-default provisions** — Many guaranties include cross-default
    provisions that trigger the guaranty upon a default by the guarantor under any other
    obligation to the lender. These can be activated by defaults entirely unrelated to
    the guaranteed transaction, creating unexpected liability.

---

## Writing Standards

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon. One point per sentence.
- Active voice: "The guaranty waives the guarantor's right to notice" not "The right to
  notice is waived by the guaranty."
- Name the actor: "The lender may set off the guarantor's accounts without notice" not
  "Accounts may be subject to setoff."
- Specific: cite the relevant provision rather than vague enforceability references.
- Jurisdiction-aware: flag where the issue is jurisdiction-specific.

**For internal analysis:**

- Same plain-language standards; may include more technical legal analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Is every legal claim backed by a specific citation or flagged [VERIFY]?
3. Is every suretyship defense waiver assessed for jurisdiction-specific waivability?
4. Are any phrases vague or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-specific anti-deficiency statutes, one-action rule
  status, and waiver enforceability cases in the applicable collateral jurisdiction
- Search for the latest suretyship case law in the governing law jurisdiction
- Verify RSG sections cited are current (ALI has not issued amendments, but check [VERIFY])
- For bad boy guaranties, verify current Michigan MCL § 445.1591 and any similar
  legislation in other states
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural risk assessment and commercial issues rather than legal certainty
- Recommend that the user obtain state-specific legal advice for jurisdiction-specific
  issues (anti-deficiency, waiver enforceability, bad boy trigger validity)

---

## Localization Notes

### United States — Jurisdiction-Specific Checklist

Before completing any US guaranty review involving real property security:

| Item                      | CA               | AZ                | TX        | NY                | NV         | OR         |
| ------------------------- | ---------------- | ----------------- | --------- | ----------------- | ---------- | ---------- |
| Anti-deficiency statutes  | §§ 580a-580d     | § 33-814          | Limited   | None (commercial) | NRS 40.430 | ORS 86.770 |
| One-action rule           | § 726(a)         | Yes               | No        | No                | Yes        | Partial    |
| Waiver of anti-deficiency | § 2856 (limited) | Yes (§ 33-814(G)) | N/A       | N/A               | Partial    | Varies     |
| Sham guaranty doctrine    | Yes              | Potential         | Potential | No                | Unknown    | Unknown    |
| Community property        | Yes              | Yes               | Yes       | No                | Yes        | No         |

### United Kingdom — Etridge Compliance Checklist

For any UK guaranty involving a non-commercial guarantor (spouse, family member,
nominal company officer):

- [ ] Lender has required guarantor to be advised by a separate solicitor
- [ ] Lender has provided the guarantor's solicitor with full facility information
- [ ] Solicitor has confirmed in writing that independent legal advice was given
- [ ] Transaction does not involve financial assistance for a plc share acquisition

### EU Civil Law — Key Distinguishing Features

| Feature               | France                       | Germany                          | Spain                  | Italy         |
| --------------------- | ---------------------------- | -------------------------------- | ---------------------- | ------------- |
| Guaranty type default | Simple (collection)          | Collection unless waived (§ 771) | Presumed joint/several | Varies        |
| Consumer protection   | Loi Dutreil handwritten req. | BGH family guaranty doctrine     | LGDCU                  | Codice Civile |
| Written requirement   | Yes                          | BGB § 766                        | Yes                    | Yes           |
| Proportionality       | Yes — disproportionate void  | Yes — unconscionable void        | Varies                 | Varies        |

---

## Output Format Template

```markdown
## Guaranty Agreement Review

**Document**: [Guaranty title, parties, and date]
**Guaranty Type**: [Continuing/Specific; Payment/Performance/Collection; Absolute/Conditional]
**Your Side**: [Guarantor / Lender / Neutral]
**Governing Law**: [Jurisdiction]
**Collateral/Property Jurisdiction**: [Jurisdiction — anti-deficiency analysis required]
**Deal Context**: [Transaction type and size]
**Review Basis**: [Organizational playbook / General commercial and suretyship standards]
**Date of Review**: [date]

---

## Risk Profile: [HIGH / MEDIUM / LOW] — from [Guarantor/Lender]'s perspective

---

## CRITICAL Items (Resolve Before Execution)

[List any CRITICAL items with one-line summaries]

---

## Key Findings — RED (Escalate)

[Top RED issues with severity classification and one-line summaries]

---

## Issues to Negotiate — YELLOW

[YELLOW items organized by priority tier]

---

## Guaranty Type Classification

**Scope**: [Continuing / Specific]
**Conditionality**: [Absolute/Payment / Conditional/Collection]
**Nature**: [Payment / Performance / Completion / Both]
**Anti-deficiency risk**: [Applicable state statutes and waivability analysis]

---

## Missing Provisions

[List of absent provisions with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED / CRITICAL] | Confidence: [Level]

**Guaranty says**: [Summary of provision]
**Market standard**: [Applicable market standard — lender or guarantor form]
**Issue**: [Specific deviation]
**Business impact**: [Practical consequence]
**Redline** (if YELLOW or RED):

> [Specific proposed language]
> **Legal basis**: [Citation or principle — VERIFIED or [VERIFY]]
> **Priority**: [Tier 1/2/3]
> **Fallback**: [Alternative if primary rejected]

[Repeat for all 13 clause categories]

---

## Suretyship Defense Waiver Analysis

[Table: each waived defense, whether waivable in governing jurisdiction, and any limits]

---

## Anti-Deficiency and One-Action Rule Exposure

[State-specific analysis of anti-deficiency statutes and one-action rule applicability]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [Sequencing, tone, key trades]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps

[Specific actions, owners, and deadlines if applicable]

---

## Glass Box Audit Trail

[YAML block per Glass Box template]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on deep web research across
15 targeted queries covering: Restatement (Third) of Suretyship and Guaranty §§ 16,
37-49; UCC §§ 3-605, 9-207, 9-610, 9-627; 11 U.S.C. §§ 362, 509, 544, 547, 548, 1301;
Cal. Civil Code § 2856; Cal. Code Civ. Proc. §§ 580a, 580b, 580d, 580e, 726; Arizona
A.R.S. § 33-814; N.Y. G.O.L. §§ 5-1401, 5-1402; Companies Act 2006 §§ 172, 174, 678-680;
Statute of Frauds 1677 (UK) s.4; _Royal Bank of Scotland v Etridge (No 2)_ [2001] UKHL 44;
BGB §§ 138, 765-778; _Cherryland Mall_ (Mich.); _CP III Rincon Towers_ (N.Y.); _Extended
Stay of America_ (2009); _First Federal Bank v. Greenwalt_ (Ind. App. 2015); _Arizona Bank
& Trust v. Barrons Trust_ (Ariz. App. 2015). Structural patterns adapted from the
legalcode-contract-review reference standard and legalcode-loan-agreement-review skill.
