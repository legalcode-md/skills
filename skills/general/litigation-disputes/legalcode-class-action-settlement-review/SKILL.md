---
name: legalcode-class-action-settlement-review
description: Review and analyze class action settlements for judicial approval under FRCP Rule 23(e),
  Australian Part IVA representative proceedings (Federal Court of Australia Act s.33V), and Canadian
  provincial class proceedings acts. Use when preparing or opposing a preliminary approval motion, final
  approval motion, fairness hearing submission, or settlement adequacy analysis for any class or representative
  action proceeding.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review and analyze class action settlements for judicial approval under FRCP Rule 23(e), Australian Part IVA representative proceedings (Federal Court of Australia Act s.33V), and Canadian provincial class proceedings acts. Evaluates fund adequacy, attorney fee award methodology (lodestar vs. percentage-of-fund, cross-check), claims administration and distribution plan, notice plan adequacy, opt-out mechanics, objections framework, cy pres doctrine (US circuit standards, Ontario 2020 statutory provisions, AU equivalents), CAFA coupon settlement restrictions (28 USC § 1712), and overall fairness under Rule 23(e)(2) four-factor test. Applies circuit-specific standards for Ninth, Second, Third, and Eighth Circuits. Produces element-by-element PASS/FLAG/FAIL classification, actionable remediation guidance, prioritized approval risk assessment, and Glass Box audit trail. Use when preparing or opposing a preliminary approval motion, final approval motion, fairness hearing submission, or settlement adequacy analysis for any class or representative action proceeding. Jurisdiction-specific coverage for US (federal and CAFA), Australia (federal representative proceedings), and Canada (provincial class proceedings).


# Legalcode Class Action Settlement Review

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of class action
> and representative proceeding settlements. It does not constitute legal advice. All outputs
> must be reviewed by a qualified attorney or solicitor licensed in the relevant jurisdiction
> before use in any court filing, fairness hearing submission, or settlement approval motion.
> Class action settlement law evolves rapidly through circuit decisions, Supreme Court review,
> and statutory amendment; verify current authority before relying on any doctrinal statement.
> Statutory and case law references cited from memory carry hallucination risk — verify against
> Westlaw, Lexis, ALR, CanLII, or authoritative court databases before citing in any submission.
> This skill covers US federal procedure primarily; Australian and Canadian coverage is
> comprehensive but requires local counsel verification.

---

## Purpose and Scope

Use this skill to produce a structured settlement adequacy analysis for class actions and
representative proceedings at any stage of the approval process: pre-filing review of
proposed terms, preliminary approval briefing, fairness hearing preparation, or post-objection
response. The skill evaluates every material element of the settlement with element-level
classification and delivers prioritized approval risk assessment across three jurisdictions.

**Covers:**

- Rule 23(e) settlement review — all four statutory approval factors (2018 amendments codified)
- Rule 23(e)(1) preliminary approval standard — "likely to approve and certify" threshold
- Rule 23(e)(2) final approval four-factor analysis (adequate representation, arm's-length
  negotiations, adequacy of relief, equitable treatment of class members)
- Fund adequacy analysis (total fund, per-member recovery, claims rate, admin cost ratio)
- Attorney fee award methodology — lodestar, percentage-of-fund, and mandatory cross-check
- Circuit-specific fee standards (Ninth, Second, Third, Eighth Circuit benchmarks)
- Notice plan adequacy under Rule 23(c)(2) "best practicable notice" standard
- Opt-out mechanics, deadline adequacy, and opt-out rate significance thresholds
- Objections framework — grounds, procedural requirements, professional objectors
- Cy pres doctrine — residual fund distribution, nexus requirement, circuit standards
- CAFA coupon settlement restrictions — 28 USC § 1712 attorney fee calculation rules
- Australian Part IVA representative proceedings settlement (s.33V Federal Court Act)
- Australian litigation funding approval and funder fee reasonableness analysis
- Canadian provincial class proceedings settlement approval (Ontario, BC, and analogous)
- Ontario 2020 cy-près statutory amendments (Class Proceedings Act)
- Amchem/settlement class heightened scrutiny overlay for settlements structured to achieve
  certification only through settlement

**Does not:**

- Draft the settlement agreement itself (see `legalcode-settlement-agreement-drafter`)
- Analyze class certification prerequisites (see `legalcode-class-certification-analysis`)
- Calculate damages ranges or probability-weighted outcomes (see `legalcode-damages-calculation`)
- Build litigation risk or settlement authority analysis (see `legalcode-litigation-risk-assessment`,
  `legalcode-settlement-negotiation`)
- Cover criminal plea agreements, consent decrees in regulatory proceedings, or NLRB settlements
- Apply to individual (non-class) settlement agreements
- Provide legal advice or substitute for licensed class action counsel

**Related skills:**

- `legalcode-class-certification-analysis` — Run before this skill when reviewing a settlement
  class proposed for certification only through settlement (Amchem heightened scrutiny applies)
- `legalcode-settlement-agreement-drafter` — Draft the settlement agreement; this skill reviews it
- `legalcode-litigation-risk-assessment` — Four-dimensional risk framing for settlement authority
- `legalcode-damages-calculation` — Damages modeling to benchmark fund adequacy

---

## Jurisdiction and Governing Law

This skill covers three primary jurisdictional frameworks. Identify the applicable framework
in Step 3 before proceeding with substantive analysis.

| Framework                    | Triggers                                                | Approval Authority                | Core Standard                                                                                              |
| ---------------------------- | ------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **US Federal (Rule 23)**     | Federal class action; CAFA removal to federal court     | District court                    | "Fair, reasonable, and adequate" — Rule 23(e)(2) four-factor test                                          |
| **Australian Part IVA**      | Representative proceeding in Federal Court of Australia | Federal Court                     | "Fair and reasonable" — s.33V(1) Federal Court of Australia Act 1976 (Cth)                                 |
| **Australian State**         | State court class actions (VIC, NSW, QLD)               | Relevant state court              | State-specific procedures [VERIFY current state legislation]                                               |
| **Canadian Federal**         | Federal Court class action (rare)                       | Federal Court of Canada           | Federal Courts Rules — applies provincial class proceedings standards by analogy                           |
| **Ontario CPA**              | Class proceeding in Ontario                             | Ontario Superior Court of Justice | "Fair, reasonable, and in the best interests of the class" — Class Proceedings Act, 1992 (as amended 2020) |
| **BC CPA**                   | Class proceeding in BC                                  | BC Supreme Court                  | Class Proceedings Act, RSBC 1996 c.50 — "fair, reasonable, and in the best interests of the class"         |
| **Other Canadian Provinces** | Class proceedings in AB, QC, MB, SK, NS, PEI, NB, NL    | Respective provincial courts      | Analogous provincial legislation [VERIFY: province-specific provisions]                                    |

[JURISDICTION-SPECIFIC] US analysis is circuit-specific. Identify the governing circuit in
Step 3 — approval standards, fee benchmarks, cy pres nexus requirements, and collusion
indicators differ materially between the Ninth, Second, Third, and Eighth Circuits.

[JURISDICTION-SPECIFIC] Australian class actions may also proceed in state Supreme Courts
(Victoria under Part 4A of the Supreme Court Act 1986; NSW under Part 10 of the Civil
Procedure Act 2005; Queensland under Part 13A of the Civil Proceedings Act 2011). These
state regimes have analogous but not identical approval procedures. [VERIFY current state
legislation and practice notes before relying on state court procedures.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would materially change the analysis direction
- Multiple valid analytical frameworks apply
- Circuit-specific standards are outcome-determinative
- Settlement structure creates a fork only the user can resolve

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

### Step 1: Accept Settlement Materials

Accept the settlement for review in any of these formats:

- **Settlement agreement**: Full executed or draft settlement agreement
- **Preliminary approval motion**: Motion papers, memorandum, supporting declarations
- **Notice plan and claim form**: Proposed notice documents and distribution plan
- **Fairness hearing submission**: Any brief or declaration submitted for court approval
- **Summary**: A structured description of settlement terms if documents are unavailable

If no settlement documents are provided, prompt the user to supply them or provide the key
terms: total fund amount, class size estimate, claims structure, notice plan, fee request,
cy pres terms, and release scope.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, gather this context. Skip questions already answered:

1. **Jurisdiction and court:**
   - Options: US federal (specify district and circuit), Australian Federal Court, Australian
     state court (specify state), Ontario Superior Court, BC Supreme Court, other Canadian
     province (specify), multiple jurisdictions
   - _Why this matters_: Determines the applicable approval standard, fee benchmark, cy pres
     requirements, and notice rules — these differ significantly across jurisdictions.

2. **Perspective:**
   - Options: Class counsel (seeking approval), Defense counsel (supporting approval),
     Objector (opposing settlement), Named plaintiff (assessing adequacy), Court-appointed
     consultant, Neutral analysis (no side)
   - _Why this matters_: Determines which risks to prioritize and how to frame recommendations.

3. **Approval stage:**
   - Options: Pre-filing review (settlement not yet submitted), Preliminary approval
     (seeking order authorizing notice), Post-notice / fairness hearing preparation,
     Post-objection response, Appeal analysis
   - _Why this matters_: Different stages require different analytical depth — preliminary
     approval requires less detail than final approval.

4. **Settlement structure:**
   - Options: Common fund (class members claim from a fixed fund), Claims-made with floor
     (minimum guaranteed payout), Coupon settlement (class receives vouchers/coupons),
     Injunctive relief only, Mixed cash + injunctive, Reversionary fund (unclaimed funds
     revert to defendant), Non-reversionary fund with cy pres
   - _Why this matters_: Each structure has different adequacy tests and scrutiny levels.
     Coupon settlements trigger CAFA § 1712. Reversionary funds raise collusion flags.

5. **Settlement class or certified class:**
   - Options: Certified class settling after certification, Settlement class only (no
     prior certification — Amchem heightened scrutiny applies), Both certified class and
     alternative settlement class definition proposed
   - _Why this matters_: Amchem heightened scrutiny applies to settlement-only classes;
     run `legalcode-class-certification-analysis` if settlement class certification is contested.

6. **Litigation funding (Australian and Canadian matters):**
   - Options: Self-funded litigation / no third-party funder, Third-party litigation funder
     (specify if known), Conditional fee / no-win-no-fee arrangement
   - _Why this matters_: Australian courts supervise funder fee approvals as part of settlement
     adequacy; funder fee proportion is a primary factor in reasonableness review.

_Batch default_: US federal; class counsel perspective; fairness hearing preparation; common
fund; certified class settling; no third-party funder.

### Step 3: Identify Jurisdiction and Legal Framework

Based on context gathered, determine the applicable legal framework. Build a working
authority reference for this review:

**US matters:**

1. Identify the governing circuit. Check for published circuit-specific approval guidelines:
   - _Ninth Circuit_: "Heightened exacting review" standard; _In re Bluetooth_ collusion
     indicators; 25% percentage-of-fund benchmark [VERIFY applicability to specific settlement type]
   - _Second Circuit_: Rule 23(e)(2)(C)(iii) fee-to-recovery proportion analysis even for
     segregated fee funds (_Kurtz v. Kimberly-Clark Corp._, 2024 [VERIFY citation])
   - _Third Circuit_: Cy pres recipient affiliation disclosure requirement; cy pres limited to
     small percentage of fund
   - _Eighth Circuit_: Cy pres nexus requirement (_Jones v. Monsanto Co._ [VERIFY citation]);
     lodestar multiplier limits (9.6x held unreasonable [VERIFY])
   - _Other circuits_: Apply general Rule 23(e)(2) four-factor test; note circuit-specific
     variations [VERIFY controlling circuit precedent]

2. Screen for CAFA coupon settlement: Does the settlement provide coupons, vouchers, or
   certificates redeemable for goods or services? If yes, 28 USC § 1712 applies — flag
   immediately and proceed to Step 13.

3. Use **legalcode-mcp** (if connected) to search for:
   - Controlling circuit precedent on settlement approval and fee awards
   - Any district-specific procedural guidance (e.g., N.D. Cal. Procedural Guidance for
     Class Action Settlements, W.D. Wash. local rules)
   - Recent decisions in the same subject-matter area affecting approval standards

**Australian matters:**

1. Confirm the proceeding is in the Federal Court of Australia (Part IVA framework) or
   identify the applicable state court and legislation.
2. Review the Class Actions Practice Note (GPN-CA) for current procedural requirements.
   [VERIFY current version at fedcourt.gov.au]
3. Identify whether a litigation funder is involved — court supervision of funder fee
   approval is mandatory where a funder is present.
4. Note: The Federal Court requires court-approved notice to class members before
   determining a settlement approval application.

**Canadian matters:**

1. Identify the governing province. Ontario CPA (1992, as amended 2020) or BC CPA are the
   most developed; other provinces have analogous legislation.
2. Note the 2020 Ontario amendments for cy-près: explicit statutory framework codified in
   the Ontario CPA for the first time. [VERIFY whether the specific province has equivalent provisions]
3. Confirm opt-out procedures: all Canadian provinces are opt-out regimes — opt-out deadline
   and procedure must appear in the approved notice.

**⟁ CLARIFY** — If governing circuit (US) or governing province (Canada) cannot be
determined from the materials provided, ask before proceeding. Circuit assignment is
outcome-determinative for fee benchmarks and cy pres standards.

### Step 4: Settlement Structure Overview

Before element-by-element analysis, map the settlement structure:

| Element                            | Extracted Value | Notes                                              |
| ---------------------------------- | --------------- | -------------------------------------------------- |
| Total settlement fund              |                 |                                                    |
| Fund type                          |                 | Common fund / claims-made / coupon / injunctive    |
| Reversionary?                      |                 | Yes (FLAG) / No                                    |
| Estimated class size               |                 | Source: notice list / defendant records / estimate |
| Estimated claimants                |                 | Claims submitted or projected                      |
| Attorney fee request               |                 | Amount and methodology stated                      |
| Fee as % of total fund             |                 | Calculate: fee ÷ (fee + class fund)                |
| Administrative costs               |                 | Estimated total                                    |
| Named plaintiff incentive payments |                 | Per plaintiff and aggregate                        |
| Cy pres allocation                 |                 | Amount, recipient, selection rationale             |
| Litigation funder fee (AU/CA)      |                 | If applicable                                      |
| Net recovery per claimant          |                 | Total fund minus fees, admin, incentive, funder    |

**⟁ CLARIFY** — If the fee is segregated from the class fund (defendant pays separately),
ask whether the user wants the analysis to treat this as a percentage of total consideration
(fee + class fund) per Rule 23(e)(2)(C)(iii) or only as a percentage of the class fund.
_Note: The Second Circuit requires courts to evaluate proportion of fees to total recovery
even when structurally segregated._

### Step 5: Fund Adequacy Analysis

Assess whether the total settlement fund provides adequate relief to the class.

**Primary adequacy measures:**

1. **Expected value comparison**: Compare total fund to the probability-weighted expected
   value of the class's best-case recovery at trial. If no damages model is available:
   - Flag the absence as a gap — courts expect comparisons to estimated class-wide damages
   - Request or estimate gross potential recovery (class size × average individual harm)
   - Apply a discount for litigation risk (trial probability × damages if successful)

2. **Per-member recovery**: Calculate net recovery per claiming member:
   - Gross fund − attorney fees − administration costs − incentive payments − funder fees
   - Divide by projected number of claimants (or total class if claims-made with minimum floor)
   - Flag if net per-member recovery is de minimis (courts scrutinize settlements where
     individual recovery is negligible compared to stated class injury)

3. **Claim participation rate**: Assess whether the claims process is structured to maximize
   or minimize claims:
   - Note: Empirical research shows even with direct notice, 90%+ of class members do not
     submit claims. A high-barrier claims process combined with a reversionary fund is a
     collusion signal.
   - Identify any unnecessary submission hurdles (notarization, proof of purchase from
     long-past dates, multiple-step verification)

4. **Administrative cost ratio**: Flag if administrative costs exceed 15% of total fund
   (threshold for concern); flag prominently if administrative costs exceed 25% (courts
   may require competitive bidding evidence).

5. **Reversionary fund analysis**: If unclaimed funds revert to defendant:
   - Classify as FLAG or FAIL depending on circuit — Ninth Circuit treats reversion as a
     collusion indicator (_In re Bluetooth_ [VERIFY])
   - Calculate maximum and minimum total cost to defendant (best and worst case from
     defendant's perspective)
   - Determine whether the structure provides defendant a financial incentive to minimize
     claims (collusion signal)

**Classification:**

- **PASS**: Fund provides meaningful per-member recovery; adequacy is supported by comparison
  to potential recovery at trial; no reversionary structure or reversion is immaterial
- **FLAG**: Per-member recovery is modest; claims process presents barriers; adequacy
  comparison to potential recovery is incomplete or unfavorable
- **FAIL**: Fund is demonstrably inadequate compared to potential class-wide recovery; de
  minimis per-member recovery; reversionary structure combined with barriers to claiming;
  no damages model or adequacy comparison available

### Step 6: Attorney Fee Award Analysis

Evaluate the attorney fee request against applicable standards. This is consistently the
most scrutinized element of class settlement approval.

**Determine the methodology:**

| Method                 | When Applied                                                                                                             | Key Standard                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Percentage-of-fund** | Common fund settlements where attorneys recover from the class fund                                                      | Percentage must be reasonable as a share of total consideration; cross-check against lodestar |
| **Lodestar**           | Statutory fee-shifting cases (civil rights, employment, consumer statutes); where work predates discovery of common fund | Hours × reasonable rate; adjusted by multiplier for risk/success                              |
| **Hybrid**             | Mixed settlements (partial common fund + statutory claims)                                                               | Apportion and apply each method to the relevant portion                                       |
| **CAFA coupon method** | Coupon settlements — 28 USC § 1712                                                                                       | Fees attributable to coupons calculated on _redeemed_ coupon value only — see Step 13         |

**Percentage-of-fund analysis:**

1. **Calculate the fee percentage**: Fee ÷ total consideration (including the class fund,
   not just cash to class members). Include the value of injunctive relief only if
   independently quantifiable.

2. **Apply circuit benchmark**:
   - _Ninth Circuit_: 25% benchmark [VERIFY applicability]; courts must make reasoned findings
     that fees are proportional to actual (not anticipated) value of settlement; "exacting
     review" required; fee awards at 9.6x lodestar have been held unreasonable [VERIFY]
   - _Second Circuit_: Rule 23(e)(2)(C)(iii) requires fee-to-recovery proportion analysis
     regardless of structural segregation; no fixed benchmark but proportionality required
   - Other circuits: Generally 25-33% is market range; courts vary on benchmarks [VERIFY
     controlling circuit authority]

3. **Lodestar cross-check** (required in most circuits):
   - Request the lodestar figure (hours × rate) from class counsel's records or estimate
   - Calculate the implied multiplier: fee request ÷ lodestar
   - Flag if multiplier exceeds 4x (elevated scrutiny); escalate to FAIL if multiplier
     exceeds 9x without exceptional justification
   - Courts increasingly require cross-check even when fee fund is structurally segregated

4. **Clear sailing arrangement screen**: Does the settlement contain a provision where
   defendant agrees not to oppose class counsel's fee request?
   - If yes: flag as collusion indicator (_In re Bluetooth_ [VERIFY])
   - A clear sailing arrangement alone does not defeat approval but requires heightened
     scrutiny of the fee amount

5. **Incentive payment review**: Named plaintiff incentive payments are under increased
   scrutiny post-_Johnson v. NPAS Solutions_ (11th Cir., restrictions on incentive
   payments to class representatives [VERIFY current circuit consensus]).
   - Note circuit split on permissibility of incentive payments [VERIFY]
   - Flag payments exceeding $10,000 per plaintiff for elevated review
   - Flag disproportionate payments where the named plaintiff receives significantly more
     than average class member recovery

**Australian funder fee analysis** (where applicable):

- The Federal Court supervises funder fee approval as part of s.33V adequacy review
- Key factors: percentage of settlement allocated to funder, risks undertaken by funder,
  obligations assumed, total amount to funder relative to class recovery
- Flag if funder fee percentage leaves class members with inadequate net recovery
- Common fund orders: courts may use equitable jurisdiction to impose common fund orders
  requiring all class members (including opt-outs) to contribute to litigation costs
  [VERIFY: status of High Court authority on common fund orders — _BMW Australia v. Brewster_
  [2019] HCA 45 limits Federal Court's power; [VERIFY current position]]

**Canadian fee analysis:**

- Class counsel fees subject to court approval as part of settlement approval
- Courts assess reasonableness against: contingency fee agreement terms, hours worked,
  complexity of issues, results achieved, risk undertaken
- Funder fees subject to same court approval process in Ontario and BC

**Classification:**

- **PASS**: Fee request is proportionate to total consideration; lodestar cross-check within
  acceptable multiplier range; no clear sailing arrangement; incentive payments proportionate
- **FLAG**: Fee percentage is above-benchmark; multiplier is elevated (4-9x); clear sailing
  arrangement present; incentive payments require justification
- **FAIL**: Fee request is disproportionate to actual class benefit; multiplier exceeds 9x
  without exceptional justification; fee structure obscures true percentage through
  structural segregation; CAFA coupon rules violated

### Step 7: Notice Plan Adequacy

Evaluate whether the proposed notice satisfies the "best practicable notice" standard under
Rule 23(c)(2)(B) (US), the Federal Court's GPN-CA requirements (AU), or provincial CPA
notice requirements (CA).

**Notice content requirements (US):**

Required elements under Rule 23(c)(2)(B):

- [ ] Clear definition of the class and subclasses (if any)
- [ ] Description of the claims, issues, or defenses
- [ ] That a class member may enter an appearance through an attorney
- [ ] That the court will exclude from the class any member who requests exclusion
- [ ] Opt-out procedure and deadline (Rule 23(b)(3) classes only)
- [ ] That the judgment will bind all class members who do not opt out
- [ ] Settlement terms, including: total fund, fee request, named plaintiff incentive
- [ ] Fairness hearing date, time, and location (or instruction to check for date)
- [ ] How to object and the deadline for objections
- [ ] How to submit a claim (if claims-made settlement)
- [ ] Contact information for settlement administrator

**Notice dissemination plan:**

Evaluate whether the dissemination method achieves "best practicable notice":

- **Individual notice** (required where class members are identifiable): Direct mail, email,
  or text message to known class members
- **Publication notice** (where individual notice not practicable): National newspaper,
  trade publication, or digital advertising
- **Settlement website**: Required in most districts; must contain all notice content plus
  downloadable documents
- **Toll-free number**: Required in complex settlements with claim submission

Apply the following adequacy thresholds:
| Dissemination Rate | Classification |
|-------------------|---------------|
| 70%+ class members receive individual notice | PASS |
| 50-70% individual notice with publication supplement | FLAG — assess whether combined reach is adequate |
| Below 50% individual notice | FAIL — publication alone rarely satisfies Rule 23(c)(2) for identifiable classes |

**Opt-out mechanics:**

- Opt-out deadline: Must allow adequate time (courts generally require 30-90 days from
  notice; N.D. Cal. guidance requires minimum 35 days [VERIFY])
- Opt-out procedure: Must be simple — any requirement beyond a signed written statement
  with identification information is potentially excessive (some courts reject requirements
  for notarized opt-outs or documentation of damages)
- Flag any opt-out procedure that makes opting out more burdensome than submitting a claim

**Australian notice requirements:**

- Court must approve the wording of the settlement notice before distribution
- Settlement approval proceedings are not private — notice and proceeding are public
- Notice must explain: settlement terms, right to opt out, how to participate in settlement
  distribution, fairness hearing date [VERIFY current GPN-CA requirements]

**Canadian notice requirements:**

- Court approval of notice content and manner of dissemination required before distribution
- Notice must include: opt-out procedures and deadline, how to deliver objections, approval
  hearing date, settlement terms summary
- Opt-out window: typically 90-120 days in Ontario; may vary by court order

**Classification:**

- **PASS**: Notice reaches identified class members by direct means; all required content
  present; opt-out procedure is simple and deadline adequate
- **FLAG**: Notice plan relies heavily on publication for identifiable class; opt-out
  procedure has minor barriers; one or two required content elements absent
- **FAIL**: Individual notice not provided for identifiable class; opt-out deadline is
  unreasonably short; required content elements missing; opt-out procedure is unduly
  burdensome

### Step 8: Claims Administration Review

Evaluate the claims process design, administrator selection, and distribution plan.

**Claims process design:**

1. **Claim submission requirements**: Are documentary proof requirements proportionate to
   the amount recoverable? Flag requirements that make claims burdensome relative to
   individual recovery amounts.
2. **Claim deadline**: Is there adequate time after notice to submit claims? Minimum 45-60
   days from notice is typical; shorter deadlines without strong justification are a FLAG.
3. **Administrator selection**: Was the administrator selected through competitive bidding?
   Courts increasingly require evidence of competitive bidding for administrators in large
   settlements. Flag if administrator was selected without competitive process.
4. **Distribution plan**: Does the plan allocate recovery proportionally to class members'
   claims or injuries? Flag per-capita distributions in cases where individual damages
   varied significantly (unequal treatment of class members is a FAIL under Rule 23(e)(2)(D)).
5. **Unclaimed funds**: How are residual unclaimed funds treated?
   - Reversion to defendant: FLAG (collusion indicator; courts may reject or require cy pres)
   - Additional distribution to claimants: Generally acceptable
   - Cy pres distribution: Acceptable with proper nexus analysis (see Step 9)
   - Escheat to state: Acceptable in some circumstances

**Class member subgroup treatment:**

- **⟁ CLARIFY** — If the class includes multiple subgroups with different injury types or
  damages (e.g., employees vs. consumers; purchasers in different years), ask whether the
  allocation plan was reviewed for intraclass conflicts. Disparate treatment of subgroups
  without adequate justification is a Rule 23(e)(2)(D) FAIL.

**Classification:**

- **PASS**: Administrator competitively selected; claims process proportionate to recovery;
  adequate claim deadline; distribution proportional to class members' claims
- **FLAG**: Administrator selection process unclear; some claims requirements are burdensome;
  distribution plan rationale not fully explained
- **FAIL**: No competitive bidding for administrator; claims process unduly burdensome relative
  to per-member recovery; distribution disparities not justified; no disclosure of unclaimed
  fund treatment

### Step 9: Cy Pres Analysis

Evaluate any proposed cy pres distribution of residual or undistributed settlement funds.

**US cy pres framework:**

Cy pres distributions of unclaimed class action settlement funds may be approved when:

1. Further direct distribution to class members is not feasible or practical (because class
   members cannot be identified, the per-member amount is negligible, or administrative cost
   exceeds the residual)
2. The proposed recipient(s) satisfy the nexus requirement

**Nexus requirement (US):**

| Circuit            | Standard                                                                                                                        | Key Authority                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Eighth Circuit** | Recipient must "relate directly to the injury alleged in the lawsuit and settled by the parties"                                | _Jones v. Monsanto Co._ [VERIFY]                                                               |
| **Third Circuit**  | (a) Nexus to class injury; (b) Disclosure and review of any prior affiliations between recipient and parties, counsel, or court | Third Circuit cy pres standards [VERIFY controlling case]                                      |
| **Ninth Circuit**  | Recipient's work must be related to the objectives of the underlying statute or claims                                          | _Dennis v. Kellogg Co._ [VERIFY]; _Frank v. Gaos_ Supreme Court review [VERIFY current status] |
| **Second Circuit** | General nexus to class; court review of affiliate connections                                                                   | Second Circuit cy pres standards [VERIFY]                                                      |
| **Other circuits** | Apply general nexus principle; circuit-specific variations [VERIFY]                                                             |                                                                                                |

**Cy pres-only settlements:**
Courts have recognized cy pres-only settlements (entire fund to cy pres rather than class members)
as appropriate only when: (a) class members cannot be identified; OR (b) per-member amounts are
negligible and distribution would be consumed by administrative costs. Cy pres-only settlements
receive heightened scrutiny and may be rejected where individual distribution is feasible but
administratively inconvenient.

**Affiliation disclosure requirement:**
Any prior relationship between proposed cy pres recipients and parties, class counsel, or the
presiding judge must be disclosed. Non-disclosure of affiliations is an objection ground that
can defeat settlement approval.

**⟁ CLARIFY** — If cy pres is proposed, ask:

- Who are the proposed recipients?
- What is the connection between the recipient's work and the class's alleged harm?
- Do any recipients have prior affiliations with class counsel, defense counsel, or the court?
- What circumstances make direct distribution to class members impractical?

**Australian cy pres equivalents:**
Australian law does not have a developed cy pres doctrine equivalent to US law. Undistributed
funds in Australian class actions are typically handled through the Settlement Distribution
Scheme (SDS) approved by the court. The SDS may provide for:

- Additional distribution to claiming class members
- Reversion to defendant in certain circumstances (subject to court approval)
- Payment to Australian charities with a connection to the subject matter
  [VERIFY: current Federal Court practice on undistributed residual funds; review recent GPN-CA
  and relevant Federal Court decisions on SDS mechanisms]

**Canadian cy pres framework:**

- Ontario CPA (2020 amendments): First explicit statutory cy-près provisions in Ontario's
  class action legislation
  - Eligible recipients: registered charities (Income Tax Act definition), non-profit
    organizations agreed by parties, or Legal Aid Ontario (fallback)
  - Court must be satisfied that direct compensation is not practical or possible using
    best reasonable efforts
  - Recipient must be expected to directly or indirectly benefit the class or subclass members
- BC and other provinces: Different reception to cy pres; specific provisions [VERIFY
  current status in applicable province]

**Classification:**

- **PASS**: Cy pres recipient has clear nexus to class injury; all affiliations disclosed;
  direct distribution impractical for stated reason; recipient is eligible under applicable
  framework (US/AU/CA)
- **FLAG**: Nexus is indirect; partial disclosure of affiliations; feasibility of direct
  distribution not fully addressed; recipient selection rationale unclear
- **FAIL**: No nexus to class injury; undisclosed affiliation between recipient and parties/
  counsel/court; cy pres used where direct distribution is feasible; recipient ineligible
  under applicable statutory framework (CA); entire fund directed to cy pres without
  adequate justification

### Step 10: Objections Analysis

Evaluate the objections framework and any known or anticipated objections.

**Who may object (US):**

- Any class member who has not opted out may object
- Objection must state: (a) whether it applies to objector only, to a subclass, or to
  the entire class; (b) specific grounds for objection with specificity
- Objectors who opt out cannot subsequently object — opting out severs the binding
  relationship (flag if any objector has both opted out and filed an objection)

**Procedural requirements for valid objections (US):**

- [ ] Filed by deadline specified in the notice
- [ ] States the objector's class membership (name, address, transaction information)
- [ ] Specifies grounds with particularity
- [ ] Served on all parties
- [ ] States whether objector intends to appear at fairness hearing

**Common grounds for objection:**
| Objection Ground | Scrutiny Level | Typical Strength |
|-----------------|---------------|-----------------|
| Excessive attorney fees | HIGH — courts scrutinize | Strong if supported by fee/recovery proportion analysis |
| Collusion / conflicts of interest | HIGH — can defeat approval | Strong with _In re Bluetooth_ factors present |
| Inadequate settlement fund | MEDIUM | Requires damages model comparison |
| Improper allocation methodology | MEDIUM | Strong with intraclass conflict evidence |
| Inadequate notice plan | MEDIUM | Requires showing actual inadequacy |
| Cy pres nexus failure | MEDIUM | Strong with clear affiliation or no nexus |
| Professional objector | LOW on its own | Must show underlying substantive defect |

**Professional objectors:**
Courts are increasingly skeptical of professional objectors — attorneys who solicit class
members to raise objections, typically hoping to extract a payment in exchange for
withdrawal. Indicators of professional objector status:

- Counsel represents objectors in multiple unrelated class actions
- Objection is filed near the deadline with minimal supporting detail
- Prior payment received by counsel to withdraw objections in other cases

Rule 23(e)(5)(B) requires court approval before any payment may be made in connection
with an objection's withdrawal, forgoing, or abandonment. Flag any proposed payment to
an objector counsel that has not received court approval.

**⟁ CLARIFY** — If the settlement faces pending objections, ask for the objection texts.
The analysis should address each objection's likely strength and recommend a response
strategy for class counsel or a scrutiny framework for courts.

**Classification:**

- **PASS**: Objections, if any, are procedurally defective, substantively weak, or
  attributable to professional objectors without meritorious grounds; settlement is
  structured to withstand scrutiny on all objected-to elements
- **FLAG**: One or more objections raise legitimate concerns about fee proportionality,
  cy pres nexus, or allocation; response is available but requires supporting evidence
- **FAIL**: Objections expose structural defects (collusion, inadequate fund, improper
  allocation) that courts are unlikely to overlook at final approval; settlement
  modification likely required

### Step 11: Opt-Out Analysis

Evaluate the opt-out rate and its implications for settlement approval.

**Opt-out rate significance:**
Courts consider the opt-out rate as one indicator of settlement adequacy, but in context —
high opt-out rates among members with high-value individual claims may signal inadequacy,
while low opt-out rates among mass-harm plaintiffs with low individual damages are expected.

| Opt-Out Rate                          | Class Characteristics                            | Interpretation                                                                                  |
| ------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| < 1%                                  | Typical consumer / data breach / mass-harm class | Normal — does not affect approval                                                               |
| 1-5%                                  | Typical range                                    | Low — supports approval                                                                         |
| 5-10%                                 | Elevated                                         | Requires analysis of who is opting out and why                                                  |
| > 10%                                 | High                                             | Significant — examine whether sophisticated class members with high-value claims are opting out |
| Mass opt-out by sophisticated parties | Any class                                        | Strong signal of inadequacy — courts may require enhanced scrutiny                              |

**⟁ CLARIFY** — If opt-out data is available, ask:

- What percentage of the class has opted out?
- Are opt-outs concentrated among a particular subgroup or geographic area?
- Do any opt-outs include large institutional parties or law firms representing groups
  of claimants (signal of inadequacy for high-value claims)?

**Classification:**

- **PASS**: Opt-out rate is within expected range for class type; no unusual concentration
  of opt-outs among high-value claimants
- **FLAG**: Elevated opt-out rate; opt-outs include identifiable subgroups; no analysis
  of opt-out profile available
- **FAIL**: Opt-out rate is significantly elevated; sophisticated high-value claimants
  opting out en masse; pattern consistent with inadequate fund for material portion of class

### Step 12: Fairness Factors Analysis

Apply the full applicable approval framework to render an overall settlement adequacy
assessment.

**US — Rule 23(e)(2) Four-Factor Test (2018 amendments):**

| Factor                                      | Analysis Required                                                                                                                                                                                                                    | Classification     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **(A) Adequate representation**             | Were class representatives and class counsel adequate throughout? Any conflicts of interest between named plaintiffs and absent class members?                                                                                       | PASS / FLAG / FAIL |
| **(B) Arm's-length negotiation**            | Was the settlement reached through genuine adversarial bargaining? Any mediator involvement? Any _In re Bluetooth_ collusion indicators: disproportionate fee to class recovery ratio; clear sailing arrangement; reversionary fund? | PASS / FLAG / FAIL |
| **(C) Adequate relief** — four sub-factors: |                                                                                                                                                                                                                                      |                    |
| (C)(i) Costs, risks, and delay of trial     | Compare settlement to probability-weighted expected recovery at trial                                                                                                                                                                | PASS / FLAG / FAIL |
| (C)(ii) Effectiveness of distribution       | Will class members actually receive relief? What is the projected claim rate and per-member recovery?                                                                                                                                | PASS / FLAG / FAIL |
| (C)(iii) Attorney fees                      | Are proposed fees proportionate to total consideration? (Key Second Circuit focus even for segregated fee funds)                                                                                                                     | PASS / FLAG / FAIL |
| (C)(iv) Other agreements                    | Any side agreements between parties not disclosed to the court? Rule 23(e)(3) requires disclosure of all agreements made in connection with the settlement                                                                           | PASS / FLAG / FAIL |
| **(D) Equitable treatment**                 | Does the settlement treat class members equitably relative to each other? Disparate treatment of similarly situated subgroups without justification?                                                                                 | PASS / FLAG / FAIL |

**In re Bluetooth collusion indicators (Ninth Circuit) [VERIFY]:**
Flag if two or more of the following are present:

- [ ] Counsel receives a disproportionate fee compared to class recovery
- [ ] Clear sailing arrangement (defendant agrees not to oppose fee request)
- [ ] Reversionary fund (unclaimed amounts revert to defendant)

Presence of multiple collusion indicators requires heightened scrutiny and may require
independent analysis of the negotiating history.

**Pre-2018 multi-factor tests:**
Many circuits developed multi-factor tests before the 2018 Rule 23(e)(2) amendments
(_Girsh_ factors in the Third Circuit, _Bluetooth_ factors in the Ninth). These pre-existing
tests remain relevant but should be applied in conjunction with the Rule 23(e)(2) four-factor
test. [VERIFY: whether controlling circuit requires both analyses]

**Australian — s.33V(1) "Fair and Reasonable" Standard:**

Courts apply an active protective standard — not passive acceptance. Key factors:

- Claims made on behalf of group members and their prospects of success if litigated
- Risks of loss if the case proceeded, including evidentiary and legal hurdles
- Interests of group members as a whole (not just the named applicant and defendant)
- Adequacy of the class notice and group member participation opportunity
- Where appointed: assessment by the contradictor (independent counsel for group members)
- Court may require a fairness report from an independent expert in complex cases

**Canadian — "Fair, Reasonable, and in the Best Interests of the Class" Standard:**

Apply the four-factor Canadian approval analysis:

1. **Counsel competence and investigation**: Have class counsel conducted sufficient investigation?
2. **Absence of collusion**: Is there reason to believe collusion or extraneous considerations
   influenced negotiations?
3. **Cost-benefit analysis**: Is the class better served by this settlement than by litigation?
4. **Class member information and disposition**: Were class members sufficiently informed?
   Are they generally favourably disposed (low objection rate)?

Courts adopt a policy favouring settlement — settlements will be approved if within "a range
of reasonableness," not requiring the optimal outcome.

**Overall classification:**

- **PASS**: All Rule 23(e)(2) factors (or AU s.33V / CA "fair, reasonable, best interests"
  factors) weigh in favor of approval; no material collusion indicators; no structural defects
- **FLAG**: One or more factors require additional evidence or clarification; minor structural
  concerns addressable through modification or supplemental disclosure
- **FAIL**: One or more factors presents a structural defect likely to lead to denial of
  approval; collusion indicators present; intraclass conflicts unresolved; fund demonstrably
  inadequate

### Step 13: CAFA Coupon Settlement Analysis

_(Skip this step if the settlement does not provide coupons, vouchers, or redeemable certificates.)_

**CAFA coupon settlement definition:**
28 USC § 1712 applies when class members receive "coupons" — typically vouchers, promotional
codes, or certificates redeemable for goods or services from the defendant. The court must
determine whether the settlement is a "coupon settlement" for § 1712 purposes.

**Attorney fee calculation rules under § 1712:**

| Scenario                               | Fee Calculation Rule                                                                                              |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Coupon recovery only                   | Fees based on the value of coupons **actually redeemed** — not face value, not potential value                    |
| Mixed: coupon recovery + lodestar work | Coupon-based portion: redeemed value basis. Non-coupon portion: lodestar with multiplier                          |
| Coupon + injunctive relief             | Fee for coupon portion: redeemed value basis. Fee for injunctive portion: lodestar with hours reasonably expended |
| Cy pres from unredeemed coupons        | Unredeemed coupon proceeds distributed as cy pres **may not** be used to calculate attorney fees                  |

**Heightened scrutiny requirement:**
Under § 1712(e), courts must apply "heightened scrutiny" when approving coupon settlements.
The Ninth Circuit specifically requires heightened scrutiny for pre-certification and coupon
settlements.

**Key risks in coupon settlements:**

1. Face value inflation: Class counsel may cite face value of all coupons (not redemption rate)
   to justify high fees. Screen carefully for this.
2. Redemption rate manipulation: Settlement structures that make coupons easy to quantify but
   difficult to redeem inflate apparent class benefit.
3. Cy pres substitution: Routing unredeemed coupon value to cy pres and counting it toward
   fee calculation violates § 1712(e).
4. Non-coupon label: Defendants and class counsel occasionally structure coupon-equivalent
   relief with non-coupon labels (credit toward future purchase, etc.) to avoid § 1712.
   Courts look to substance over label. [VERIFY controlling circuit authority on what
   constitutes a "coupon" under § 1712]

**Classification:**

- **PASS**: Settlement is not a coupon settlement; or if it is, fees are calculated on
  redeemed coupon value; heightened scrutiny applied; no fee double-counting through cy pres
- **FLAG**: Coupon characterization is borderline; fee calculation methodology needs
  clarification; redemption rate assumptions require verification
- **FAIL**: Settlement is a coupon settlement but fee request is based on face value or
  unredeemed cy pres value in violation of § 1712; heightened scrutiny indicators present
  but not applied

### Step 14: Quality Verification

Before delivering the analysis, run these quality checks:

1. Run all 5 Citation Quality Gates (silently). Revise failures before delivery.
2. For every FAIL classification, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign Confidence Scores to each material classification.
4. Verify all 13 analysis elements have been addressed (present or flagged as not applicable).
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Classification System

### Element-Level Classification: PASS / FLAG / FAIL

Every element of the settlement receives one of three classifications:

| Classification | Meaning                                                                             | Approval Impact                     |
| -------------- | ----------------------------------------------------------------------------------- | ----------------------------------- |
| **PASS**       | Meets applicable legal standards; likely to survive scrutiny                        | Supports approval                   |
| **FLAG**       | Raises concerns; requires attention, modification, or supplemental disclosure       | May affect approval — addressable   |
| **FAIL**       | Does not meet applicable standards; likely to cause denial or require renegotiation | Jeopardizes approval — must address |

### Overall Settlement Assessment

Aggregate element classifications into an overall settlement risk rating:

| Rating                   | Criteria                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **APPROVAL LIKELY**      | All elements PASS; no FAIL; ≤ 2 FLAGS addressable by supplemental disclosure                                                         |
| **APPROVAL CONDITIONAL** | No FAIL; 3+ FLAGS; or 1-2 FLAGS requiring settlement modification                                                                    |
| **APPROVAL AT RISK**     | 1 FAIL in any element; or 3+ FLAGS in core elements (fund adequacy, fees, arm's-length)                                              |
| **APPROVAL UNLIKELY**    | 2+ FAIL classifications; or FAIL in adequacy of representation or arm's-length negotiation; or multiple collusion indicators present |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivery.

| Gate           | Rule                                                                                                       | Fail Action                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, rule, case, or established principle                           | Add citation or mark "[UNVERIFIED — cite before filing]"   |
| **Format**     | All citations follow a consistent, recognizable format (Fed. R. Civ. P.; USC §; case name, reporter, year) | Fix format                                                 |
| **Currency**   | Every cited provision checked for 2018+ Rule 23 amendments; circuit precedent verified as current          | Flag "[CHECK CURRENCY — verify against current authority]" |
| **Domain**     | Analysis stays within applicable jurisdiction's framework; no cross-jurisdictional bleed                   | Remove or flag cross-jurisdictional assumptions            |
| **Confidence** | Uncertainty explicitly stated; circuit splits flagged; [VERIFY] markers applied                            | Add confidence qualifier; add [VERIFY] tag                 |

### Self-Interrogation for FAIL Classifications

For any FAIL classification, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the FAIL classification follow logically from the
cited authority? Would a court actually deny approval on this ground? Is there a counter-argument
that would allow a modified settlement to be approved?

**Pass 2 — Completeness**: Have all relevant factors been considered? Are there affirmative
factors (process quality, risk of litigation, class member reaction) that partially offset the
defect? Are there circuit-specific safe harbors or approval techniques not yet considered?

**Pass 3 — Challenge**: What is the strongest argument class counsel could make for approval
despite this defect? Under what circumstances would a court accept the settlement as-is?
Does the defect require settlement restructuring or can it be addressed through disclosure?

### Confidence Scoring

| Level        | Range     | Meaning                                                          | Action                                                    |
| ------------ | --------- | ---------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law; clear statutory text; controlling circuit precedent | State with confidence                                     |
| **High**     | 0.80-0.94 | Strong authority; minor uncertainty                              | State with brief caveat                                   |
| **Probable** | 0.60-0.79 | Good arguments; circuit split possible                           | State with reasoning and contra-indicators                |
| **Possible** | 0.40-0.59 | Genuinely uncertain; circuit split confirmed                     | Flag for professional review with both sides              |
| **Unlikely** | 0.0-0.39  | Weak basis; jurisdiction not verified                            | Do not assert; flag "[UNCERTAIN — verify before relying]" |

### Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-class-action-settlement-review"
  matter_identifier: "[Assigned matter ID or anonymized description]"
  jurisdiction: "[US federal (circuit) / AU Federal Court / CA province]"
  approval_stage: "[Pre-filing / Preliminary / Final / Post-objection / Appeal]"
  settlement_structure: "[Common fund / Claims-made / Coupon / Injunctive / Mixed]"
  settlement_class: "[Yes / No — if yes, Amchem scrutiny applied]"
  legalcode_mcp: "[Connected — citations verified / Not connected — [VERIFY] markers applied]"
  cafa_coupon_screen: "[Triggered / Not triggered / Borderline — see Step 13]"
  elements_analyzed:
    fund_adequacy: "[PASS / FLAG / FAIL]"
    attorney_fees: "[PASS / FLAG / FAIL]"
    notice_plan: "[PASS / FLAG / FAIL]"
    claims_administration: "[PASS / FLAG / FAIL]"
    cy_pres: "[PASS / FLAG / FAIL / N/A]"
    objections: "[PASS / FLAG / FAIL / None filed]"
    opt_out_analysis: "[PASS / FLAG / FAIL / Data unavailable]"
    fairness_factors: "[PASS / FLAG / FAIL]"
    cafa_coupon: "[PASS / FLAG / FAIL / N/A]"
  collusion_indicators_present: "[Yes (list indicators) / No]"
  overall_rating: "[APPROVAL LIKELY / CONDITIONAL / AT RISK / UNLIKELY]"
  citations_verified: "[N verified via legalcode-mcp] / [N marked [VERIFY]]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "[Circuit precedent not verified if legalcode-mcp not connected]"
  reviewer: "AI-assisted — requires qualified class action counsel review before any court filing"
```

---

## Deep Reference: Legal Standards by Jurisdiction

### US — Rule 23(e) Settlement Approval Framework

**Statutory text (Rule 23(e)(2), post-2018 amendments):**
The court may approve a settlement that would bind class members only after a hearing and
only on finding that it is fair, reasonable, and adequate after considering whether:
(A) the class representatives and class counsel have adequately represented the class;
(B) the proposal was negotiated at arm's length;
(C) the relief provided for the class is adequate, taking into account:
(i) the costs, risks, and delay of trial and appeal;
(ii) the effectiveness of any proposed method of distributing relief to the class,
including the method of processing class-member claims;
(iii) the terms of any proposed award of attorney's fees, including timing of payment; and
(iv) any agreement required to be identified under Rule 23(e)(3); and
(D) the proposal treats class members equitably relative to each other.

**Rule 23(e)(1) Preliminary approval standard:**
To obtain court approval to send notice, parties must demonstrate that the court will
"likely" be able to approve the settlement and certify the class for purposes of judgment.
The 2018 amendments require parties to submit substantial supporting information at the
preliminary approval stage — front-loading that previously was deferred to final approval.

**Amchem heightened scrutiny for settlement classes:**
Where a class is proposed for certification only for purposes of settlement (no prior
certification), courts apply heightened scrutiny to class certification requirements
(_Amchem Products v. Windsor_, 521 U.S. 591 (1997) [VERIFY]). The settlement's
existence cannot be used to satisfy Rule 23 requirements that would not otherwise be met,
EXCEPT that the settlement structure may inform the manageability inquiry (which is
inapplicable for settlement-only classes) and cohesion of the class may be judged in
part by the settlement's treatment of different subgroups.

**Rule 23(e)(3) — disclosure of related agreements:**
Parties must file a statement identifying any agreement made in connection with the settlement.
Undisclosed side agreements (e.g., defendant's non-opposition to future attorney fee claims
in other matters; most-favored-nation provisions) that are not disclosed are grounds for
denial and potential sanctions.

**Rule 23(e)(4) — new opt-out opportunity:**
If the court requires further opt-out opportunity in connection with settlement approval
(e.g., where original certification notice did not provide opt-out rights, or where the
settlement materially alters class members' rights), courts may order a second opt-out period.

**Rule 23(e)(5) — objections:**
Objections must be filed with the court and served on all parties. Court approval is required
before any payment or consideration may be provided to an objector or objector's counsel in
connection with: (B)(i) forgoing or withdrawing an objection; or (B)(ii) forgoing, dismissing,
or abandoning an appeal from an order approving the proposal.

### Australian — Part IVA Settlement Framework

**Governing statute**: Federal Court of Australia Act 1976 (Cth), Part IVA
**Key provision**: Section 33V(1) — a representative proceeding may not be settled or
discontinued without the approval of the Court.

**Approval procedure (Class Actions Practice Note, GPN-CA):**

1. Application filed seeking approval with supporting materials (settlement agreement,
   supporting affidavits, counsel's advice on prospects, independent assessment where complex)
2. Court approves notice and orders its distribution — wording and distribution method
   subject to judicial approval
3. Fairness hearing — active judicial scrutiny; courts cannot passively accept settlements
4. Court determines whether settlement is "fair and reasonable" having regard to:
   - Claims made on behalf of group members
   - Interests of group members as a whole
   - Advice from counsel on prospects of success
   - Risks of litigation
   - Any funding arrangements and funder fee amounts (where litigation funder is present)

**Contradictors:**
In complex settlements or where fairness concerns arise, courts may appoint contradictors —
independent counsel to represent group member interests at the approval hearing. The role of
the contradictor has expanded in recent Australian practice.

**Litigation funding supervision:**
Where a litigation funder is party to the settlement arrangement, courts review:

- Total fee to funder as a percentage of settlement
- Risk undertaken and obligations assumed by the funder
- Whether the funder fee leaves class members with adequate net recovery
- Whether a common fund order is appropriate (subject to High Court limitations on
  Federal Court power — [VERIFY current position post-_BMW Australia v. Brewster_
  [2019] HCA 45])

### Canadian — Provincial Class Proceedings Settlement Framework

**Core standard (all provinces)**: "Fair, reasonable, and in the best interests of the class"

**Procedural sequence (Ontario CPA as reference):**

1. Settlement reached and filed with the court
2. Court issues order approving notice and setting approval hearing date
3. Notice distributed to class members (content and manner approved by court)
4. Opt-out period runs (typically 90-120+ days in Ontario; varies by court order)
5. Approval hearing: four-factor analysis applied
6. Court approves or rejects; conditions may be imposed

**Ontario cy-près provisions (2020 amendments — Class Proceedings Act, 1992):**
Section 32.1 (approximately): Court may approve settlement terms providing for payment to
cy-près recipient if satisfied that:
(a) using best reasonable efforts, it is not practical or possible to compensate class or
subclass members directly; AND
(b) proposed recipient is a registered charity, agreed non-profit, or (fallback) Legal Aid Ontario;
(c) the recipient would reasonably be expected to directly or indirectly benefit the class members

[VERIFY: exact section numbers in the 2020-amended Ontario CPA and whether other provinces
have enacted analogous provisions]

---

## Prioritization Framework

Prioritize findings for the user based on their impact on approval probability:

**Tier 1 — Approval-Determinative (address immediately):**
Any FAIL classification; collusion indicators (two or more present); undisclosed Rule 23(e)(3)
agreements; settlement class with Amchem certification defects; CAFA § 1712 violation

**Tier 2 — Material (address before final approval):**
Any FLAG in fund adequacy, attorney fees, or arm's-length negotiation; elevated opt-out rates;
legitimate objections raising intraclass conflict or inadequacy; cy pres nexus gaps; funder
fee disproportionality (AU)

**Tier 3 — Process Quality (address before or at fairness hearing):**
Minor notice content gaps addressable by revised notice; claims process technical barriers
correctable by amendment; undisclosed but harmless agreements; low-risk professional objectors

---

## Anti-Patterns

What NOT to do when reviewing or structuring class action settlements:

1. **Valuing injunctive relief at full list price**: Courts reject fee requests based on
   inflated injunctive relief valuations (e.g., "the injunction is worth $500M to the class")
   unless the valuation is independently supported. Use conservative or conservative-to-moderate
   estimates and flag unsupported valuations.

2. **Treating face value as redeemed value for coupon settlements**: Under 28 USC § 1712,
   attorney fees attributable to coupon recovery must be based on coupons _actually redeemed_,
   not face value or issuance value. Face-value fee calculations in coupon settlements violate
   CAFA and will be disallowed.

3. **Ignoring the lodestar cross-check**: In most circuits, a lodestar cross-check is
   required for percentage-of-fund fee requests. Omitting the cross-check does not prevent
   approval but creates an objection target. High multipliers (4x+) without cross-check
   explanation are a recurring approval problem.

4. **Assuming circuit-neutral analysis**: Cy pres nexus standards, fee benchmarks, collusion
   indicators, and preliminary approval thresholds differ significantly between circuits.
   Applying the Ninth Circuit's 25% benchmark in the Second Circuit (or vice versa) produces
   unreliable analysis. Always identify the governing circuit first.

5. **Missing the Rule 23(e)(3) disclosure requirement**: Side agreements made in connection
   with the settlement must be disclosed to the court. "Connected with" is interpreted broadly —
   any arrangement affecting the settlement value or attorney fees is probably covered. Missed
   disclosures are an objection ground that can derail an otherwise approvable settlement.

6. **Reversionary fund without scrutiny**: Unclaimed funds reverting to the defendant creates
   a collusion signal in most circuits — defendant has an incentive to structure a low-claims
   process. Flag every reversionary fund and evaluate whether the claims barriers explain the
   reversion structure.

7. **Cy pres without nexus analysis**: Proposing a cy pres recipient without explaining the
   connection to the class's alleged harm is a standard objection point. Every cy pres
   distribution needs a documented nexus analysis before submission.

8. **Clear sailing arrangement with no explanation**: Defendant's agreement not to oppose
   class counsel's fee request (_clear sailing_) is an _In re Bluetooth_ collusion indicator
   in the Ninth Circuit. If a clear sailing arrangement is present, be prepared to address
   it in the approval papers with evidence of genuine adversarial negotiation.

9. **Opt-out hurdles that exceed the claim submission burden**: If filing a claim requires
   less effort than opting out, courts will scrutinize the opt-out design. Opt-out procedures
   must be at least as simple as claim submission — notarization requirements for opt-outs
   have been rejected.

10. **Conflating settlement class approval with prior class certification**: Where a class
    was never certified before settlement (settlement-only class), Amchem heightened scrutiny
    applies. The settlement cannot manufacture class cohesion that would not otherwise exist —
    intraclass conflicts that would defeat certification must still be addressed through
    subclasses or exclusions.

11. **Incentive payment disproportionality**: Named plaintiff incentive payments that
    substantially exceed the average class member recovery require careful justification.
    Circuit split on permissibility of incentive payments exists (Eleventh Circuit restrictions
    in _Johnson v. NPAS Solutions_ [VERIFY current status]). Do not assume incentive payments
    are routinely approved without circuit-specific research.

12. **Australian cy pres without checking Federal Court practice**: Australian courts do not
    have the same developed cy pres doctrine as US courts. Proposing cy pres-style distributions
    in Australian class actions requires analysis under the court's supervisory power over
    Settlement Distribution Schemes, not by analogy to US cy pres doctrine.

13. **Canadian cy pres without checking provincial statute**: Only Ontario has explicit 2020
    statutory cy-près provisions. Other Canadian provinces may handle undistributed funds
    differently. Do not assume Ontario's framework applies to BC, Quebec, or other provinces
    without provincial legislation verification.

14. **Omitting the litigation funder from the Australian approval analysis**: Where a funder
    is present, the funder fee is part of the settlement approval analysis in Australia — not
    a separate matter. Courts review funder fees as part of the overall fairness determination.
    Omitting funder fee analysis from the Australian approval submission is a procedural error.

15. **Single-pass settlement review without adversarial pressure-testing**: A settlement that
    looks adequate on its face may fail under the objector's lens. Before submitting any
    approval motion, stress-test the settlement against the strongest available objection
    grounds: Is the fee proportionate by circuit benchmark? Would an _In re Bluetooth_
    analysis reveal collusion signals? Does the cy pres have a documented nexus?

16. **Relying on opt-out silence as proof of class approval**: The fact that few class members
    opted out does not by itself establish settlement adequacy — empirical research shows that
    90%+ of class members take no action (neither opting out nor submitting claims) regardless
    of settlement quality. Courts evaluate the substance of the settlement, not just the
    absence of opt-outs.

---

## Writing Standards

Apply these standards before delivering any output:

**Precision:**

- Cite specific rules, statutes, and cases — never just "applicable law"
- Identify the governing circuit (US) or province (CA) explicitly
- Distinguish between what is required by law and what is recommended as best practice
- Use exact fee calculation numbers, not ranges, when amounts are available

**Uncertainty discipline:**

- Mark all unverified statutory and case law references with [VERIFY]
- Mark circuit-split areas explicitly with [CIRCUIT-SPLIT]
- State confidence level for every material FAIL classification
- Do not assert that a settlement "will" be approved or denied — state "is likely to" or
  "faces material risk of denial" with supporting analysis

**Structure:**

- Lead every element analysis with the classification (PASS/FLAG/FAIL) before the explanation
- Use tables for multi-factor analyses
- Separate findings (what the settlement does) from analysis (whether that satisfies the standard)

**Plain language:**

- Explain technical terms on first use (e.g., "lodestar — the product of reasonable hours
  times a reasonable hourly rate")
- Avoid unexplained Latin (cy pres = "as near as possible")
- Translate CAFA provisions into plain operational terms before applying them

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
In Step 3, search for:

- Controlling circuit precedent on settlement approval, fee awards, and cy pres
- District-specific procedural guidance (N.D. Cal., S.D.N.Y., etc.)
- Any pending Supreme Court review affecting class settlement standards [VERIFY]
- Current Australian GPN-CA requirements
- Current provincial CPA statutory text for the relevant Canadian province

Save verified results to `/tmp/legalcode-settlement-research.md`. Cite legalcode-mcp
sourced references as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — [VERIFY] markers applied throughout"`
- Focus the analysis on structural quality, workflow design, and identification of issues —
  do not assert specific legal standards without [VERIFY] markers
- Recommend that class action counsel verify all cited authority before filing

---

## Localization Notes

**US circuit-specific adjustments:**
When switching between circuits, adjust:

- Fee benchmark (Ninth Circuit 25%; other circuits vary — [VERIFY controlling circuit])
- Collusion indicator framework (_In re Bluetooth_ is Ninth Circuit; analogous tests exist
  in other circuits — [VERIFY])
- Cy pres nexus standard (Third Circuit affiliation disclosure; Eighth Circuit direct-nexus
  requirement; etc.)
- Preliminary approval threshold language

**Australian state courts:**
Victoria, NSW, and Queensland have state class action regimes with their own procedural
rules. Verify applicable legislation and practice notes for state court proceedings.

**Canadian provinces outside Ontario and BC:**
Alberta, Quebec, Manitoba, Saskatchewan, and Atlantic provinces have analogous class action
legislation. Verify current provisions before applying Ontario or BC analysis to other provinces.

---

## Output Format Template

Structure the final output as follows:

```markdown
# Class Action Settlement Review

**Matter:** [matter identifier or anonymized description]
**Settlement:** [brief description — party names anonymized or placeholder]
**Court / Jurisdiction:** [court and circuit/province]
**Approval Stage:** [Preliminary / Final / Post-objection]
**Analysis Date:** [date]
**Overall Rating:** [APPROVAL LIKELY / CONDITIONAL / AT RISK / UNLIKELY]

---

## Settlement Structure Summary

| Element                   | Value                                       |
| ------------------------- | ------------------------------------------- |
| Total fund                | $[X]                                        |
| Fund type                 | [Common fund / Claims-made / Coupon / etc.] |
| Reversionary              | [Yes / No]                                  |
| Estimated class size      | [N]                                         |
| Attorney fee request      | $[X] ([X]% of total consideration)          |
| Lodestar cross-check      | $[X] lodestar → [X]x multiplier             |
| Named plaintiff incentive | $[X] per plaintiff                          |
| Cy pres                   | $[X] to [recipient]                         |
| Net per-member recovery   | $[X] (if all [N] claims submitted)          |

---

## Element-by-Element Analysis

### 1. Fund Adequacy — [PASS / FLAG / FAIL]

**Confidence:** [0.XX]
[Analysis — 2-5 sentences]
**Remediation (if FLAG or FAIL):** [Specific action required]

### 2. Attorney Fees — [PASS / FLAG / FAIL]

**Confidence:** [0.XX]
[Analysis — 2-5 sentences]
**Remediation (if FLAG or FAIL):** [Specific action required]

### 3. Notice Plan — [PASS / FLAG / FAIL]

**Confidence:** [0.XX]
[Analysis]
**Remediation (if FLAG or FAIL):** [Specific action required]

### 4. Claims Administration — [PASS / FLAG / FAIL]

**Confidence:** [0.XX]
[Analysis]
**Remediation (if FLAG or FAIL):** [Specific action required]

### 5. Cy Pres — [PASS / FLAG / FAIL / N/A]

**Confidence:** [0.XX]
[Analysis]
**Remediation (if FLAG or FAIL):** [Specific action required]

### 6. Objections — [PASS / FLAG / FAIL / None filed]

**Confidence:** [0.XX]
[Analysis]
**Remediation (if FLAG or FAIL):** [Specific action required]

### 7. Opt-Out Analysis — [PASS / FLAG / FAIL / Data unavailable]

**Confidence:** [0.XX]
[Analysis]

### 8. Fairness Factors (Rule 23(e)(2) / AU s.33V / CA Standard) — [PASS / FLAG / FAIL]

**Confidence:** [0.XX]
[Factor-by-factor analysis table]
**Overall fairness assessment:** [1-2 sentences]

### 9. CAFA Coupon Screen — [PASS / FLAG / FAIL / N/A]

**Confidence:** [0.XX]
[Analysis if applicable]

---

## Prioritized Remediation Plan

### Tier 1 — Approval-Determinative (resolve before submission)

1. [Issue — specific action required]
2. [Issue — specific action required]

### Tier 2 — Material (resolve before final approval)

1. [Issue — specific action required]

### Tier 3 — Process Quality (address before fairness hearing)

1. [Issue — best practice improvement]

---

## Overall Assessment

[2-4 sentence summary of settlement adequacy, primary risks, and recommended next steps]

---

[Glass Box Audit Trail — YAML block from template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep research into FRCP Rule
23(e) (2018 amendments), US circuit court precedent on settlement approval and fee awards,
Australian Part IVA representative proceedings framework (Federal Court Act s.33V(1), GPN-CA),
Canadian provincial class proceedings legislation (Ontario CPA as amended 2020, BC CPA),
28 USC § 1712 CAFA coupon settlement restrictions, and the _In re Bluetooth_ collusion
indicator framework. Informed by structural patterns from `legalcode-class-certification-analysis`,
`legalcode-settlement-agreement-drafter`, `legalcode-litigation-risk-assessment`, and
`legalcode-contract-review` reference skills. Research conducted via web search covering
2024-2025 circuit developments in attorney fee scrutiny, cy pres doctrine, and class notice
standards. All case law citations should be independently verified before filing; statutory
citations reflect law as of 2026-03-21.
