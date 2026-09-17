---
name: legalcode-us-section-409a-valuation-review
description: Review nonqualified deferred compensation arrangements for IRC Section 409A compliance —
  assess valuation methodologies, verify safe harbor qualification (independent appraisal, illiquid startup
  presumption, formula method), analyze stock option pricing, audit permissible payment events, evaluate
  the short-term deferral exception, apply the six-month delay rule, identify operational and documentary
  failures, assess correction program eligibility, and model penalty exposure. Use when conducting 409A
  compliance audits, granting stock options or SARs, reviewing deferred compensation plan documents, preparing
  for M&A transactions involving executive compensation, advising on employment or separation agreements
  with deferred pay, or evaluating IRS correction program eligibility for prior violations. US federal
  law only (IRC § 409A and 26 CFR § 1.409A).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode US Section 409A Valuation & Compliance Review

> **Disclaimer**: This skill provides a framework for AI-assisted 409A compliance review.
> It does not constitute legal or tax advice. All outputs must be reviewed by a qualified
> attorney or tax professional before relying on them for planning, filing, or compliance
> purposes. Tax law changes frequently; verify current applicability before acting on any
> provision described here. Statutory and regulatory references cited from memory carry
> hallucination risk — verify against IRS.gov and authoritative tax sources before relying
> on them.

---

## Purpose and Scope

This skill reviews nonqualified deferred compensation (NQDC) arrangements for compliance
with IRC § 409A and the final regulations under 26 CFR § 1.409A-1 through 1.409A-6.

**Covers:**

- Classification of arrangements as covered or exempt from § 409A
- Safe harbor valuation analysis for stock options and SARs
- Option/SAR grant compliance (FMV pricing, no deferral features)
- Permissible payment event audit (all six triggers)
- Short-term deferral exception (2.5-month rule)
- Six-month delay rule for specified employees of public companies
- Documentary compliance (written plan requirements)
- Operational failure identification and severity assessment
- IRS correction program eligibility (Notice 2008-113, Notice 2010-6)
- Penalty exposure modeling (income inclusion + 20% excise tax + interest)
- M&A 409A considerations (change-in-control definitions, acceleration, cash-outs)
- State-law overlay (California 20% additional penalty)

**Does not:**

- Provide tax advice or substitute for qualified counsel
- Cover qualified plans (§ 401(k), § 403(b), defined benefit plans) — those are exempt
- Cover ISOs under § 422 or ESPPs under § 423 — those are automatically exempt
- Apply to non-US deferred compensation arrangements
- Address § 457A (offshore deferred compensation) — separate analysis required

---

## Jurisdiction and Governing Law

**United States federal tax law only.** This skill applies IRC § 409A (enacted by § 885
of the American Jobs Creation Act of 2004, effective January 1, 2005), the final
regulations under 26 CFR §§ 1.409A-1 through 1.409A-6, and associated IRS guidance.

Key authorities:

- **IRC § 409A** — the governing statute
- **26 CFR §§ 1.409A-1 through 1.409A-6** — the final regulations (effective 2008)
- **IRS Notice 2008-113** — operational failure correction program
- **IRS Notice 2010-6** — documentary failure correction program
- **IRS Notice 2010-80** — modifications to both correction programs
- **Rev. Rul. 2008-13** — separation from service and specified employees
- **26 CFR § 1.409A-3(i)(2)** — change-in-control definitions

**State law overlay:**

- California imposes an **additional 20% penalty** on 409A violations (Cal. Rev. & Tax.
  Code § 17501) — **the combined state + federal excise tax can reach 40%+ for
  California taxpayers.**
- [VERIFY] Other states may have conforming or separate penalty regimes.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The scope of arrangements to review is unclear
- Whether a specific exception or safe harbor applies requires facts not yet provided
- Multiple corrections paths exist and the user's risk tolerance matters
- An arrangement sits on the border between covered and exempt

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

### Step 1: Accept the Engagement

Accept input in any of these formats:

- **Plan documents**: Deferred compensation plan, stock option plan/agreement, employment
  agreement, separation agreement, SAR plan, phantom equity plan, bonus plan, change-in-
  control agreement
- **Cap table or option register**: List of option grants with grant dates, exercise prices,
  vesting schedules, and contemporaneous 409A valuations
- **Existing 409A valuation report**: Third-party appraisal or internal valuation memo
- **Description of arrangement**: Summary of compensation structure for initial analysis

**⟁ CLARIFY** — Before beginning, confirm scope:

1. **What type of arrangement is under review?**
   - Options: Stock option plan (NSOs), Stock appreciation rights (SARs), Deferred bonus/
     salary deferral plan, Supplemental executive retirement plan (SERP), Employment/
     separation agreement with deferred pay, Change-in-control/golden parachute arrangement,
     Multiple arrangement types (full audit), Other
   - _Why this matters_: Each arrangement type triggers different 409A sub-rules.

2. **What is the purpose of this review?**
   - Options: New grant compliance check, Annual plan audit, Pre-M&A due diligence,
     IRS audit defense, Post-violation correction analysis, Drafting review of new plan
     documents
   - _Why this matters_: Pre-M&A review emphasizes change-in-control definitions and
     acceleration; correction analysis focuses on penalty calculation and remediation paths.

3. **Is the entity publicly traded or private?**
   - Options: Public (stock trades on an established securities market), Private (venture-
     backed, PE-owned, or founder-owned), Non-profit or tax-exempt organization, Unknown
   - _Why this matters_: The six-month delay rule and specified-employee analysis apply only
     to publicly traded companies. Safe harbor valuation options differ for public/private.

### Step 2: Screen for Exemptions

Before applying 409A requirements, check whether the arrangement falls within an
exemption. An exempt arrangement is not subject to the statute at all.

#### 2a. Excluded Plans and Arrangements

| Arrangement                                                                                       | Exemption                     | Basis                       |
| ------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------- |
| Qualified retirement plans (§ 401(k), § 403(b), pension)                                          | Fully exempt                  | 26 CFR § 1.409A-1(a)(2)     |
| Incentive stock options (ISOs) qualifying under § 422                                             | Fully exempt                  | 26 CFR § 1.409A-1(b)(5)(ii) |
| Employee stock purchase plans (ESPPs) under § 423                                                 | Fully exempt                  | 26 CFR § 1.409A-1(b)(5)(ii) |
| Tax-qualified annuities (§ 403(b))                                                                | Fully exempt                  | 26 CFR § 1.409A-1(a)(2)     |
| Arrangements providing only vacation, sick leave, disability, death benefits, or medical benefits | Fully exempt                  | 26 CFR § 1.409A-1(a)(5)     |
| Short-term deferrals (paid by 2.5-month deadline)                                                 | Exempt if requirements met    | 26 CFR § 1.409A-1(b)(4)     |
| Certain foreign plans and offshore arrangements                                                   | Partial/conditional exemption | 26 CFR § 1.409A-1(a)(3)     |

#### 2b. The Short-Term Deferral Exception (2.5-Month Rule)

An arrangement qualifies for the short-term deferral exception if:

1. The deferred amount becomes vested (no longer subject to substantial risk of forfeiture)
   in a given taxable year, AND
2. The amount is **actually paid** no later than the 15th day of the third month following
   the end of the service provider's taxable year in which vesting occurs.

**For calendar-year service providers:** Payment must be made **by March 15** of the year
following the year in which compensation vests.

**Critical traps:**

- The payment must **actually be made** within the window — a commitment to pay is not
  sufficient
- If no payment date is specified in the agreement, the arrangement qualifies only if
  payment actually occurs within the window
- Missing the March 15 deadline by even one day forfeits the exception for the entire
  arrangement for that year

**⟁ CLARIFY** — If reviewing deferred bonuses or annual incentive awards, ask:

- "When do the bonus amounts vest (i.e., when is the right to payment no longer subject
  to forfeiture)? And when are they actually paid?"
- "Is there a written plan that specifies the payment date? If so, does the specified date
  fall within the 2.5-month window?"

#### 2c. Exempt Stock Rights (NSOs and SARs)

NSOs and SARs are exempt from 409A **only if all four requirements are met**:

1. **Exercise price ≥ FMV on grant date** — This is the critical requirement. Options
   granted with an exercise price even $0.01 below FMV become NQDC subject to 409A.
2. **No deferral feature** — The option must not include a feature permitting further
   deferral of income recognition beyond the exercise date (e.g., no right to defer
   receipt of shares upon exercise).
3. **Not granted in exchange for deferred compensation** — The option must be a new grant,
   not a replacement for previously deferred compensation.
4. **Issued with respect to service recipient stock** — The stock underlying the option
   must be stock of the employer or a related entity.

If any of these four requirements is not met, the option is treated as NQDC and must comply
with the full 409A framework.

**⟁ CLARIFY** — For stock option review:

- "Was the exercise price set at, above, or below the then-current FMV of the underlying
  common stock on the grant date?"
- "How was FMV determined? Via independent appraisal, internal formula, or informal
  estimate?"
- "Does the option agreement include any deferral feature (e.g., right to defer share
  delivery after exercise)?"

### Step 3: Assess Valuation Compliance

For every NSO or SAR grant not meeting the ISO/ESPP exemption, verify that the exercise
price was set at no less than FMV using one of the three recognized safe harbor methods.

#### 3a. Safe Harbor Method 1 — Independent Appraisal (Most Common)

**Requirements for safe harbor presumption under 26 CFR § 1.409A-1(b)(5)(iv)(B)(2):**

| Requirement              | Standard                                                                                                                               | Red Flag                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Valuation date           | Within **12 months** before the option grant date                                                                                      | Appraisal older than 12 months on grant date                                       |
| Appraiser independence   | Appraiser must have no financial interest in the outcome, no equity in the company, no compensation contingent on valuation conclusion | Founder, officer, employee, or investor performs valuation                         |
| Appraiser qualifications | At least 5 years of relevant experience in business valuation, mergers and acquisitions, or similar financial analysis                 | No documented valuation credentials (ABV, CVA, ASA, CFA with valuation experience) |
| Written report           | Documented report including methodology, comparable companies, adjustments, and conclusion                                             | Verbal appraisal or one-page memo                                                  |
| Methodology              | Market approach (comps/precedent transactions), income approach (DCF), or asset approach (NAV) as appropriate                          | Single method with no documentation of alternatives considered                     |

**Effect of safe harbor:** IRS bears the burden of proving the valuation was "grossly
unreasonable" — a high threshold. The company and grantees are substantially protected.

**Effect of no safe harbor:** The burden shifts to the company to demonstrate FMV was
reasonable. IRS can challenge the valuation using any standard; the probability of audit
adjustment increases significantly.

#### 3b. Safe Harbor Method 2 — Illiquid Startup Presumption

**Available only to companies meeting all of these conditions (26 CFR § 1.409A-1(b)(5)(iv)(B)(3)):**

1. Company was incorporated (or organized) **within the 10 years prior to** the grant date
2. Company has **no publicly traded stock**
3. Company does not **reasonably anticipate** a change in control or an IPO within 12 months
   of the grant date
4. Valuation is performed by someone with significant knowledge, experience, education, or
   training relevant to valuing similarly situated companies

**Note:** This method allows an internal person (e.g., CFO or experienced founder) to
perform the valuation — but that person must genuinely have relevant qualifications. Less
rigorous than the independent appraisal method and carries higher audit risk.

**Disqualifying conditions:** If the company anticipates an IPO, an acquisition, or a
substantial funding round that would fundamentally change its value within 12 months, this
safe harbor is unavailable.

#### 3c. Safe Harbor Method 3 — Binding Formula

**Available only if all of these conditions are met:**

1. The stock is valued under a formula that applies consistently to **all transfers** of the
   stock (not just option grants) — typically book value or a multiple of earnings
2. The formula is used under a **binding buyback commitment** by the company applicable
   to all equity transactions
3. The formula is established in a **legally binding agreement** with the service provider

**Note:** This method is rarely used because the binding consistency requirement is difficult
to maintain as a company grows and conducts arm's-length transactions at negotiated prices.

#### 3d. Non-Safe-Harbor Valuation

If none of the three safe harbors are used, the company bears the burden of proving the
valuation was reasonable. Acceptable approaches still include:

- Market approach (recent comparable company transactions or revenue multiples)
- Income approach (DCF using supportable projections)
- Asset approach (liquidation or NAV basis)

**⟁ CLARIFY** — When reviewing a valuation report:

- "Is the appraiser a third-party firm or an internal person?"
- "Was the report dated within 12 months before each option grant it covers?"
- "Has the company had any material events since the valuation (funding rounds, revenue
  inflections, acquisition offers, significant customer wins or losses) that would
  require an updated valuation?"

**Material events requiring updated valuation:**

- Completion of a new equity financing round
- Receipt of a written acquisition offer
- Loss of a major customer representing ≥ 10% of revenue
- Signing of a major contract significantly affecting projected revenue
- Regulatory approval or denial of key product
- Change in business model

### Step 4: Audit Permissible Payment Events

For any covered NQDC arrangement, deferred compensation may only be paid — and the plan
must specify payment — upon one or more of the **six permissible payment triggers** under
26 CFR § 1.409A-3.

| #     | Payment Trigger                      | Key Requirements                                                                                                                                                                                                                                                  | Common Pitfalls                                                                                                                                                                             |
| ----- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Separation from service**          | Service provider's termination of employment or other service relationship. 26 CFR § 1.409A-1(h). For employees of public companies: six-month delay applies to specified employees.                                                                              | Using "termination" without defining it consistently with the § 409A regs; not distinguishing between voluntary and involuntary; no definition of "service recipient" for affiliated groups |
| **2** | **Disability**                       | Service provider must be unable to engage in any substantial gainful activity by reason of medically determinable physical or mental impairment expected to result in death or lasting ≥ 12 months. 26 CFR § 1.409A-3(i)(4).                                      | Defining disability to track a short-term disability policy rather than the § 409A standard; broader definitions do not automatically trigger payment rights                                |
| **3** | **Death**                            | Payment may be made at any time within the period beginning on date of death and ending on last day of the first calendar year following the year of death                                                                                                        | No designated beneficiary in plan; payment period not specified                                                                                                                             |
| **4** | **Specified time or fixed schedule** | Date or schedule elected before deferral becomes irrevocable, or established in the plan at time of initial deferral                                                                                                                                              | Lack of specificity (e.g., "upon retirement"); no irrevocable election before deferral; subsequent modification of schedule                                                                 |
| **5** | **Change in control**                | A change in ownership of the corporation (>50% within 12 months), effective control (>30% voting power or majority board change within 12 months), or ownership of assets (>40% of assets within 12 months). 26 CFR § 1.409A-3(i)(5).                             | Using a definition inconsistent with the § 409A regs (e.g., >20% ownership triggers); not limiting to the service recipient's shares; applying to affiliates incorrectly                    |
| **6** | **Unforeseeable emergency**          | Severe financial hardship resulting from illness, accident, casualty loss not covered by insurance, or other extraordinary circumstances beyond the participant's control. Must be limited to amount necessary to satisfy the emergency. 26 CFR § 1.409A-3(i)(3). | Overly broad definition; no documented hardship review process; no distribution limit tied to need; allowing emergency distributions for predictable events                                 |

**Missing payment trigger:** If a plan specifies a payment event not listed above (e.g.,
"upon reaching a performance milestone" or "when the employee's oldest child starts
college"), the entire arrangement is non-compliant.

**⟁ CLARIFY** — For each arrangement under review, ask:

- "What events trigger payment under the plan? List all of them."
- "Are all payment triggers in the plan documents, or are some based on informal
  arrangements or side letters?"
- "For employment or separation agreements: does the agreement allow acceleration or
  changes to timing?"

### Step 5: Six-Month Delay Rule Analysis

The six-month delay rule applies **only** when all of these conditions are met:

1. **The entity is publicly traded** (stock trades on an established US or non-US securities
   market) [VERIFY — See 26 CFR § 1.409A-1(i) for the definition of established securities
   market]
2. **The participant is a "specified employee"** — defined as:
   - Any of the **top 50 most highly compensated officers** of the entity and its related
     entities, OR
   - Any person who **owns more than 5%** of the employer, OR
   - Any person who **owns more than 1%** of the employer and has annual compensation
     exceeding **$150,000** [VERIFY annual indexed threshold]
3. **The payment is on account of separation from service** (not on account of change in
   control, disability, death, or other triggers — those are not subject to the delay)

**Required delay:** Payment to a specified employee on account of separation from service
may not be made until **the date that is 6 months after the separation date** (or the
date of death, if earlier).

**Lump-sum payment option:** The plan may provide that all payments that would have been
made during the 6-month delay are paid in a lump sum on the first permissible date.

**Documentation requirement:** The six-month delay **must be specified in the plan
document** for a public company. If it is required but not in the document, the plan has
a documentary failure.

**Interaction with change-in-control:** A change in control does **not** trigger the
six-month delay, even for specified employees. The delay applies only to separation from
service.

### Step 6: Assess Documentary Compliance

Review the written plan documents against the § 409A documentary requirements. Every
covered NQDC arrangement must be set forth in a written plan that includes all required
terms.

#### Required Written Plan Elements

| Element                            | Requirement                                                                                    | Deficiency Flag                                         |
| ---------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Payment events                     | All triggers listed; no impermissible events                                                   | Trigger not listed in § 1.409A-3; impermissible trigger |
| Form of payment                    | Lump sum or installment schedule specified                                                     | "To be determined"; discretion reserved                 |
| Timing of payment                  | Specific date or objectively determinable schedule                                             | "As soon as practicable"; ambiguous                     |
| Separation from service definition | Must track 26 CFR § 1.409A-1(h)                                                                | Inconsistent with regs; missing definition              |
| Change-in-control definition       | Must track 26 CFR § 1.409A-3(i)(5)                                                             | Inconsistent thresholds (e.g., >20% instead of >50%)    |
| Six-month delay (public cos.)      | Specified for specified employees                                                              | Missing entirely for public company                     |
| Anti-acceleration rule             | No provision permitting acceleration except in specified cases                                 | Broad "company may accelerate" language                 |
| Initial deferral election timing   | Election made before services performed; or for fiscal-year compensation, within first 30 days | Late election permitted by terms                        |
| Subsequent deferral election       | Not operative until 12 months after election; extends payment at least 5 years                 | Change of payment date without required delay           |

**⟁ CLARIFY** — If plan documents are incomplete or unavailable:

- "Are there any written documents that set out the payment terms, vesting schedule, and
  triggering events for this arrangement? This includes employment agreements, offer
  letters, board resolutions, or plan summary documents."
- "Has the arrangement ever been modified? If so, were the modifications documented?"

### Step 7: Identify Operational Failures

Operational failures occur when the plan is administered in a way that is inconsistent
with its terms or with § 409A, even if the plan document itself is compliant.

#### Common Operational Failure Patterns

| Failure Type                                    | Description                                                                                  | Severity |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------- | -------- |
| **Early payment**                               | Compensation paid before a permissible payment event occurs                                  | CRITICAL |
| **Late payment**                                | Compensation paid after the deadline specified in the plan                                   | HIGH     |
| **Wrong form**                                  | Paid as lump sum when installments required, or vice versa                                   | HIGH     |
| **Impermissible acceleration**                  | Payment accelerated beyond permitted acceleration exceptions                                 | CRITICAL |
| **Short-term deferral window missed**           | Bonus paid after March 15 deadline                                                           | HIGH     |
| **Excess deferral**                             | More compensation deferred than the plan permits                                             | MEDIUM   |
| **Six-month delay not applied**                 | Specified employee of public company paid within 6 months of separation                      | CRITICAL |
| **Unforeseeable emergency improperly approved** | Distribution approved without documented hardship review                                     | HIGH     |
| **Change-in-control definition mismatch**       | Plan uses different definition than § 409A; payment triggered improperly                     | HIGH     |
| **Option backdating**                           | Exercise price set at a date earlier than the actual grant date to achieve below-FMV pricing | CRITICAL |
| **Option modification**                         | Exercise price reduced or other material modification made after grant                       | CRITICAL |
| **Stale valuation**                             | Option granted more than 12 months after the supporting 409A appraisal                       | HIGH     |

### Step 8: Classify Findings

Classify each finding using the four-tier system below. Adapt to the specific risk profile
of the arrangement and the entity.

#### Compliance Classification System

**COMPLIANT** — The arrangement meets § 409A requirements in this dimension.

- No action required
- Note for awareness in the Glass Box audit trail

**AT-RISK** — A technical deficiency exists that does not yet constitute a violation,
or a gray-area interpretation creates potential exposure.

- Examples: Valuation appraisal approaching 12-month limit with no update scheduled;
  plan language that technically complies but could be challenged; unforeseeable emergency
  definition broader than ideal
- **Action**: Document the risk, recommend correction or plan amendment, monitor

**NON-COMPLIANT** — A clear violation of § 409A has occurred or exists in the plan.

- Examples: Plan lists an impermissible payment event; NSO exercise price set below FMV;
  short-term deferral window missed; six-month delay omitted from public company plan
- **Action**: Identify applicable correction program (see Step 9); calculate penalty
  exposure; implement remediation within correction window

**CRITICAL** — A violation that is either not correctable under any IRS program, or
that has already triggered (or imminently will trigger) the full § 409A penalty.

- Examples: Option backdating with knowledge; acceleration of payment outside permitted
  exceptions; violation discovered after the two-year correction window has expired
- **Action**: Engage tax counsel immediately; calculate full penalty exposure (income
  inclusion + 20% excise tax + interest); evaluate whether state law additional penalties
  apply; consider voluntary disclosure options

#### Automatic CRITICAL Triggers

Flag the following as CRITICAL without further analysis:

1. NSO granted with an exercise price below FMV on the grant date (without immediate
   correction under Notice 2008-113 in the same year)
2. Payment made outside all six permissible payment events (unauthorized distribution)
3. Specified employee of public company paid within 6 months of separation on account of
   separation — with no correction in same year
4. Payment accelerated without qualifying under a § 409A-permitted acceleration exception
5. Any arrangement where § 409A penalties have already been assessed by the IRS or state
   taxing authority
6. Option backdating (exercise price set retroactively to achieve below-FMV pricing)

### Step 9: Correction Program Analysis

If NON-COMPLIANT findings are identified, assess eligibility for IRS correction.

#### Notice 2008-113 — Operational Failure Corrections

Covers failures to **administer** a deferred compensation arrangement in accordance with
the plan and § 409A.

| Failure Category                                                         | Correctable? | Correction Method                                  | Penalty Relief                                           |
| ------------------------------------------------------------------------ | ------------ | -------------------------------------------------- | -------------------------------------------------------- |
| Same-year operational failure (payment in wrong period, excess deferral) | Yes          | Payment in same year; income inclusion of excess   | Full relief if corrected in year of failure              |
| Prior-year operational failure (excess deferral, incorrect payment)      | Partial      | Return of excess/payment in correct form           | Reduced penalty: 50% of income inclusion (no 20% excise) |
| Stock option exercise price error                                        | Partial      | Correct in same year if discovered before exercise | Relief depends on when error discovered and corrected    |

**Two-year correction window:** For violations not corrected in the year of failure, full
penalty applies after 2 calendar years from the year of the violation. Timely correction
within 2 years reduces penalties.

**Limitations:**

- The correction program does not apply to violations that were willful or egregious
- The service provider must include certain amounts in income as part of the correction
- The correction must be formally documented and reported on Form W-2 or 1099

#### Notice 2010-6 — Documentary Failure Corrections

Covers failures in the **written plan document** itself (not operational failures).

| Failure Category                                                       | Correctable? | Deadline                                                                       | Income Inclusion                                              |
| ---------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Document fails to include permissible payment event                    | Yes          | By end of calendar year in which failure occurred, if corrected before payment | Partial or no income inclusion depending on timing            |
| Document includes impermissible payment event that was never triggered | Yes          | Prospectively by plan amendment                                                | Reduced income inclusion for at-risk amounts                  |
| Missing six-month delay provision (if never implicated)                | Yes          | By end of calendar year                                                        | Prospective fix; no income inclusion if event hasn't occurred |
| Impermissible acceleration provision (never exercised)                 | Yes          | Prospective amendment                                                          | No income inclusion if amendment before exercise              |

**Notice 2010-80** modified both programs to expand eligible failures and clarify
correction procedures.

**⟁ CLARIFY** — For each NON-COMPLIANT finding:

- "When did the failure first occur? What calendar year?"
- "Has the failure already been identified by the IRS or reported to the service provider?"
- "Has the correction window (2 years from year of failure) expired?"
- "Was the violation willful or the result of an inadvertent error?"

### Step 10: M&A and Change-in-Control Analysis

When the review is triggered by an M&A transaction, apply the following additional analysis.

#### Change-in-Control Definition Compliance

The plan's change-in-control definition must track 26 CFR § 1.409A-3(i)(5) exactly.
Verify the plan's definition against the regulatory thresholds:

| CiC Type                                   | Regulatory Threshold                                                                   | Common Plan Deficiency                                            |
| ------------------------------------------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Change in ownership                        | More than **50%** of total fair market value or voting power acquired within 12 months | Uses >20% or >30% threshold (too low; creates phantom CiC events) |
| Change in effective control (voting power) | Acquisition of **30% or more** of total voting power within 12 months, OR              | Omits the voting power prong or uses wrong percentage             |
| Change in effective control (board)        | Majority of board replaced within 12-month period without incumbent-board approval     | No board-replacement prong                                        |
| Change in ownership of assets              | **40% or more** of total gross fair market value of assets acquired within 12 months   | Uses 50% threshold (too high; misses qualifying events)           |

#### Permitted Acceleration in M&A

Acceleration of deferred compensation is prohibited under § 409A except for specifically
permitted exceptions. In an M&A context, the following accelerations are permitted:

1. **Termination and liquidation of the plan** — The plan may be terminated and amounts
   paid out within 12 months of the change in control, provided: (a) all plans of the
   same type are terminated; (b) no new NQDC plans are established for 3 years following
   the termination.
2. **Payment upon change-in-control event** — If the plan specifies change in control
   as a payment trigger (using the § 409A definition), payment at closing is permitted.
3. **Cashout of options** — Cash payment for NSOs and SARs at merger closing is
   permissible if payment is made at or following change of control consistent with § 409A.

**Prohibited in M&A context:**

- Accelerating payment of NQDC more than 30 days before a change in control to avoid
  the 409A restriction
- Modifying the plan to change payment triggers without using a permissible subsequent
  deferral election
- Substituting new awards with different vesting or payment terms without ensuring 409A
  compliance of the substitute awards

#### Substituted/Assumed Options in M&A

If NSOs are being assumed or substituted in an M&A transaction:

1. The substitute option must have an exercise price ≥ FMV of the underlying stock **at
   the time of substitution** (not the original grant date)
2. The original and substitute options must have the same economic terms except for
   adjustments to reflect the exchange ratio
3. If the substituted option has a lower intrinsic value than the original, the transaction
   is not considered a modification for § 409A purposes
4. A new 409A valuation of the acquirer's stock may be required if NSOs are being issued
   with the acquirer's stock as the underlying security

**⟁ CLARIFY** — In M&A context:

- "Will any NSOs or SARs be assumed, substituted, or cashed out in the transaction?"
- "Does the plan permit acceleration upon change in control? If so, is the change-in-
  control definition in the plan consistent with the § 409A regulatory definition?"
- "Is the acquirer publicly traded? If so, the six-month delay rule may newly apply to
  employees who were not previously subject to it."

### Step 11: Calculate Penalty Exposure

For each NON-COMPLIANT or CRITICAL finding, model the full § 409A penalty exposure.

#### Penalty Structure (IRC § 409A(a)(1))

For a § 409A violation, the service provider (employee or independent contractor) — not the
employer — is subject to a three-part penalty:

| Component            | Amount                                                                                                                                                   | Notes                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Income inclusion** | All deferred compensation under the plan for the taxable year AND all prior years' deferrals, to the extent vested and not previously included in income | Can be significantly larger than the current-year deferral; cascades to include all prior years' accruals |
| **20% excise tax**   | 20% of the amount included in income under § 409A                                                                                                        | On top of regular income tax; not deductible by the employer                                              |
| **Interest**         | Underpayment rate + **1 percentage point**, calculated as if amounts were included in income in the year they should have been                           | Runs from the year of first deferral, compounding annually                                                |

**Illustrative calculation (calendar-year individual, 37% marginal tax rate):**

| Item                                              | Amount                    |
| ------------------------------------------------- | ------------------------- |
| Deferred amount included in income                | $200,000                  |
| Regular federal income tax (37%)                  | $74,000                   |
| 20% § 409A excise tax                             | $40,000                   |
| Interest (5 years at ~9%)                         | ~$72,000                  |
| **Approximate total federal tax cost**            | **~$186,000 on $200,000** |
| California additional 20% penalty (if applicable) | $40,000                   |
| **Approximate total with CA overlay**             | **~$226,000 on $200,000** |

**Notes on cascading income inclusion:**

- If the plan covers multiple years of deferred salary or bonus, the income inclusion
  covers **all years' deferred amounts** (not just the current year in which the
  violation occurred)
- This is especially severe for SERPs and multi-year bonus deferral plans where years
  of accrued deferrals may all be pulled into income in one year

#### Who Bears the Penalty

The § 409A excise tax and income inclusion obligation falls on the **service provider**
(the employee or contractor), not the employer. However:

- The employer is required to withhold income taxes on the included amount (IRC § 3402)
- The employer may be liable for failure-to-withhold penalties if it knew or should have
  known of the violation
- The employer may have indemnification obligations to the employee under the plan
  documents or employment agreement

---

## Deviation Classification Reference

### COMPLIANT

The arrangement meets § 409A requirements for this dimension. No remediation needed.
The finding is noted in the audit trail for completeness.

### AT-RISK

A technical exposure or gray-area condition exists that does not currently constitute a
violation but could ripen into one under foreseeable circumstances.
**Examples:**

- 409A appraisal is 10 months old with two months remaining before expiration and a new
  grant round is planned
- Unforeseeable emergency definition is broader than ideal but no distributions have been
  made under it
- Plan lacks a clear definition of "separation from service" but has never been triggered

**Action**: Document the risk. Draft and implement a remediation before the risk matures.
Monitor for triggering events.

### NON-COMPLIANT

A clear violation of § 409A exists in the plan documents or in how the arrangement has
been administered.
**Examples:**

- NSO granted with exercise price $1.50 below FMV on grant date
- Plan specifies an impermissible payment event (e.g., "upon IPO" — not a permissible
  § 409A payment event without being structured as a change-in-control event)
- Six-month delay omitted from public company SERP

**Action**: Identify the applicable correction program. Quantify penalty exposure.
Implement correction within the correction window. Document the correction on Form W-2.

### CRITICAL

An uncorrectable violation or one where the penalty has already been incurred (e.g.,
the two-year correction window has expired, or the IRS has already identified the
failure).
**Examples:**

- Option backdating where the grant was recorded as occurring prior to the actual
  approval date to achieve a favorable exercise price
- Compensation paid during a six-month delay period with no same-year correction
- Full § 409A penalty has been assessed

**Action**: Engage qualified tax counsel immediately. Calculate full penalty exposure.
Evaluate voluntary disclosure options. Do not attempt self-correction without counsel.

---

## Prioritization Framework

### Tier 1 — Critical (Immediate Action Required)

Issues where penalty exposure is large, correction windows may be closing, or violations
are uncorrectable:

- Option backdating (exercise price retroactively set to achieve below-FMV pricing)
- Unauthorized distributions outside permissible payment events
- Six-month delay violations for specified employees of public companies
- Multiple-year cascading income inclusion exposure (e.g., long-running SERP)
- Impermissible acceleration of deferred compensation in M&A context
- Any finding where the two-year correction window is expiring

### Tier 2 — High (Correct Within 90 Days)

Issues that create material NON-COMPLIANT findings with available correction paths:

- NSO exercise price set below FMV (correctable if within same calendar year)
- Impermissible payment event in plan documents (correctable under Notice 2010-6)
- Short-term deferral window missed for current-year bonuses
- Missing six-month delay provision in public company plan (correctable by year-end)
- Plan modification deemed a new deferral without proper election timing
- Stale 409A valuation with upcoming option grants

### Tier 3 — Medium (Address Within 12 Months)

Issues that create AT-RISK exposure with no immediate penalty:

- Appraisal approaching expiration; needs refresh before next grant
- Ambiguous payment event definitions needing clarification
- Unforeseeable emergency definition broader than § 409A standard
- Plan lacks adequate change-in-control definition relative to regs
- Missing subsequent deferral election timing provisions

### Tier 4 — Low (Monitoring and Documentation)

Issues that are currently compliant but benefit from enhanced documentation:

- Ensure 409A appraisals are systematically retained
- Confirm appraiser independence is re-evaluated before each engagement
- Implement material event triggers for valuation updates
- Confirm plan documents are fully integrated with equity management system

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                            | Fail Action                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Source**     | Every § 409A compliance position cites a specific IRC provision, regulation, or IRS guidance document           | Add citation or mark "[UNVERIFIED — counsel to confirm]"                                |
| **Format**     | Citations follow standard US tax citation format (IRC § 409A; 26 CFR § 1.409A-1(b)(5); IRS Notice 2008-113)     | Fix format for consistency                                                              |
| **Currency**   | Every cited provision checked for amendments or superseding guidance                                            | Flag "[CHECK CURRENCY — may have been amended or superseded]"                           |
| **Domain**     | Analysis stays within US federal tax law. No assumptions from state law leaked in except where explicitly noted | Remove or flag non-federal claims; label state law separately                           |
| **Confidence** | Uncertainty explicitly stated, not hidden. If interpretation is unsettled, say so                               | Add confidence qualifier; do not assert uncertain positions with unwarranted confidence |

---

## Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the § 409A violation follow logically from the cited provision and the facts?
- Would the IRS actually assess a penalty here, or is there a bona fide defense?
- Is there an exception or safe harbor that has not yet been considered?

**Pass 2 — Completeness:**

- Have all relevant regulations, notices, and Revenue Rulings been considered?
- Has the applicable correction program been assessed, even if the window is narrow?
- Are there state-law overlays (particularly California) that compound the exposure?

**Pass 3 — Challenge:**

- What is the strongest argument that no violation occurred?
- Under what circumstances might the IRS accept the position or decline to assess?
- Is the CRITICAL classification proportionate, or should this be downgraded to NON-
  COMPLIANT with an available correction path?

If any pass reveals a weakness, revise the analysis before delivery. Mark the Glass Box
audit trail with `self_interrogation: "PASS"` or `self_interrogation: "REVISED"`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                              | Action                                                    |
| ------------ | --------- | -------------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory or regulatory requirement; no interpretive ambiguity | State with confidence                                     |
| **High**     | 0.80–0.94 | Strong authority (reg or IRS notice); minor edge-case questions      | State with brief caveat                                   |
| **Probable** | 0.60–0.79 | Reasonable interpretation; IRS has not directly addressed the facts  | State with explicit reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; no directly on-point guidance                   | Flag for tax counsel review with both arguments           |
| **Unlikely** | 0.0–0.39  | Speculative; weak legal basis                                        | Do not assert; flag "[UNCERTAIN — tax counsel to advise]" |

---

## Glass Box Audit Trail

Include the following YAML block at the end of every 409A compliance output:

```yaml
glass_box:
  skill_name: "legalcode-us-section-409a-valuation-review"
  entity_name: "[Name of company or plan sponsor]"
  arrangement_type: "[NSO plan / SERP / Deferred bonus / SAR plan / Multiple]"
  entity_type: "[Public / Private / Non-profit]"
  review_purpose: "[New grant / Annual audit / Pre-M&A / Correction analysis / Draft review]"
  tax_year_in_scope: "[Year(s) under review]"
  arrangements_reviewed: "[number]"
  compliant_findings: "[number]"
  at_risk_findings: "[number]"
  non_compliant_findings: "[number]"
  critical_findings: "[number]"
  safe_harbor_method: "[Independent appraisal / Illiquid startup / Formula / None / Mixed]"
  appraisal_current: "[Yes / No / N/A — date of most recent appraisal]"
  payment_events_compliant: "[Yes / Partial / No]"
  six_month_delay_applicable: "[Yes / No — basis]"
  correction_program_available: "[Notice 2008-113 / Notice 2010-6 / Both / None / N/A]"
  correction_window_status: "[Open (year[s] remaining) / Closed / N/A]"
  penalty_exposure: "[None / Low / Medium / High / Very High — estimated range if quantifiable]"
  california_overlay: "[Yes / No / Unknown]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "IRC § 409A — [VERIFIED / UNVERIFIED]"
    - "26 CFR §§ 1.409A-1 through 1.409A-6 — [VERIFIED / UNVERIFIED]"
    - "IRS Notice 2008-113 — [VERIFIED / UNVERIFIED]"
    - "IRS Notice 2010-6 — [VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., plan documents not provided; valuation report not reviewed]"
    - "[Any factual assumptions made]"
  reviewer: "AI-assisted — requires qualified tax attorney or CPA review before reliance"
```

---

## Anti-Patterns

Topic-specific catalogue of what NOT to do when reviewing or advising on § 409A compliance.

1. **Treating ISO exemption as automatically available for all options** — ISOs require
   strict qualification under § 422 (employee-only, ISO cap, grant limits, holding periods).
   Nonqualified options that do not meet all § 422 requirements are NSOs subject to 409A.

2. **Relying on informal FMV estimates for NSO pricing** — An informal estimate by a
   founder, CFO, or board member who lacks valuation credentials and independence is not
   a safe harbor valuation. The IRS will challenge it, and the burden of proof rests with
   the company, not the IRS.

3. **Allowing the 12-month appraisal to expire before new grants** — A 409A appraisal is
   only a safe harbor for 12 months from the valuation date. Granting options one day after
   expiry removes the safe harbor protection for those options.

4. **Failing to update valuation after material events** — A material funding round, an
   acquisition offer, or a major revenue event can make a recent appraisal stale even
   within the 12-month window. Failing to refresh in these circumstances creates audit risk.

5. **Confusing common stock value with preferred stock value** — In a VC-backed startup, the
   preferred stock is worth more than common stock due to liquidation preferences. A 409A
   valuation of common stock must account for this discount (often calculated using the OPM
   or PWERM method). Using preferred stock pricing for common stock option grants is a
   serious error.

6. **Drafting payment triggers that fall outside the six permissible events** — "Upon IPO,"
   "when the company reaches $100M in revenue," or "at the company's discretion" are not
   permissible payment events. Every payment trigger in the plan must be mapped to one of
   the six enumerated triggers.

7. **Overlooking the separation-from-service definition** — § 409A defines separation from
   service based on hours of service thresholds (80% presumed continuing; 20% presumed
   separated; 50% gray zone). Employment agreements that use "termination" without
   referencing these standards can create definitional mismatches.

8. **Applying the six-month delay rule incorrectly to private companies** — The six-month
   delay applies only to publicly traded companies. Advisors sometimes apply it to private
   companies out of overcaution; this is unnecessary and may create unintended plan
   complications.

9. **Missing the two-year correction window** — Operational failures under Notice 2008-113
   can be corrected within two years of the year in which the failure occurs. After the
   window closes, full § 409A penalties apply. Many companies discover violations only
   during M&A due diligence — often after the window has closed.

10. **Treating deferred compensation plan termination as a free escape** — § 409A permits
    plan termination and lump-sum payout only in limited circumstances (e.g., within 12
    months of a change in control, or in a corporate dissolution). Purporting to "terminate
    the plan" and pay out without meeting the conditions is an impermissible acceleration.

11. **Assuming change-in-control definitions are interchangeable** — The § 409A change-in-
    control thresholds (>50% ownership; >30% voting; >40% assets) are specific regulatory
    thresholds. Using a plan definition that differs — even slightly — can result in either
    (a) payments triggered when § 409A doesn't permit them, or (b) § 409A-permitted payments
    being blocked by a plan condition. These definitions must be surgically aligned.

12. **Failing to analyze the income inclusion cascade** — When a § 409A violation is
    discovered, the income inclusion is not limited to the current year's deferral. All
    prior years' deferrals under the plan may be pulled into current-year income. In a SERP
    with 10 years of accruals, the violation exposure can be enormous relative to the
    current-year amount.

13. **Overlooking California's additional 20% penalty** — For employees subject to
    California tax, a § 409A violation triggers an additional 20% penalty under Cal. Rev. &
    Tax. Code § 17501, potentially in addition to the federal 20% excise tax. Total excise
    burden can reach 40% or more before regular income tax.

14. **Substituting new options in M&A without re-valuing** — When acquirer options are
    substituted for target options, the substituted option must be re-priced at the FMV of
    the acquirer's stock at the time of substitution. Using the original exchange ratio
    without verifying FMV compliance is a frequent M&A 409A error.

15. **Drafting subsequent deferral elections without the 12-month/5-year rule** — A
    subsequent election to change the timing or form of payment under a § 409A plan
    (a) may not be effective for at least 12 months after it is made, and (b) must defer
    the payment by at least 5 years from when it would otherwise have been paid. Plans that
    allow informal or ad hoc changes to payment timing violate these rules.

16. **Ignoring phantom equity and SARs** — Stock-settled SARs are treated the same as NSOs
    and must meet the same FMV requirements. Cash-settled SARs and phantom equity units are
    covered NQDC and must comply with the full § 409A framework. Many founders treat phantom
    equity informally without any written plan — a significant documentary failure.

17. **Failing to coordinate 409A with § 280G golden parachute analysis** — In M&A, 409A
    and § 280G analysis must be coordinated. 409A violations can affect the timing of income
    inclusion and the calculation of parachute payments under § 280G. Running 280G analysis
    without confirming 409A compliance of underlying deferred compensation can produce
    incorrect results.

---

## Writing Standards

Apply plain-language discipline to all § 409A compliance output.

**For compliance findings and recommendations:**

- Lead with the conclusion: `[COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL]`
- State the specific provision at issue: "26 CFR § 1.409A-3(i)(5) requires..."
- Describe the gap concisely: "The plan's change-in-control definition uses a 20%
  threshold but the regulation requires >30%."
- State the consequence: "This mismatch means a 20% ownership acquisition would trigger
  payment even though § 409A does not permit it — creating an impermissible acceleration."
- Provide the remedy: "Amend the plan to adopt the regulatory threshold of >30%."

**For penalty exposure analysis:**

- Present numbers clearly (table format preferred for large computations)
- Distinguish federal and state components
- Flag the cascading income inclusion issue explicitly
- Note who bears each penalty component

**Quality gates before delivery:**

1. Every statutory/regulatory citation includes the specific section (not just "IRC § 409A")
2. Every quantitative threshold is flagged [VERIFY — may be indexed annually]
3. Every CRITICAL finding has been through Self-Interrogation (3 passes)
4. Correction program eligibility is assessed for every NON-COMPLIANT finding
5. California overlay is noted wherever relevant

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for current versions of IRC § 409A and 26 CFR §§ 1.409A-1 through 1.409A-6
- Verify the current indexed thresholds (six-month delay compensation amounts)
- Search for recent IRS guidance, Revenue Rulings, and PLRs on 409A topics
- Confirm that correction programs (Notice 2008-113, Notice 2010-6, Notice 2010-80)
  have not been superseded
- Save verified authority to `/tmp/legalcode-409a-research.md` for reference throughout
  the analysis
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the review on structural compliance, plan design analysis, and qualitative risk
  assessment rather than specific indexed threshold values
- Recommend that the user independently verify all threshold figures (compensation amounts,
  ownership percentages, correction program procedures) before acting

---

## Output Format Template

Structure the final 409A compliance deliverable as follows:

```markdown
## Section 409A Compliance Review

**Entity**: [Company name]
**Arrangement(s) Reviewed**: [NSO plan / SERP / Deferred bonus plan / etc.]
**Entity Type**: [Public / Private]
**Review Purpose**: [New grant compliance / Annual audit / Pre-M&A / etc.]
**Tax Year(s) in Scope**: [Year(s)]
**Date of Review**: [Date]
**Reviewer**: AI-assisted — requires qualified tax attorney or CPA review before reliance

---

## Executive Summary

[2–4 sentences summarizing the overall compliance posture, number of findings by tier,
most significant issues, and recommended immediate actions]

**Overall Compliance Posture**: [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL]

---

## Findings Summary Table

| Area                       | Classification                                   | Issue               | Priority   |
| -------------------------- | ------------------------------------------------ | ------------------- | ---------- |
| Valuation — Safe Harbor    | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| Option Pricing (NSOs)      | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| Payment Events             | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| Short-Term Deferral        | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| Six-Month Delay            | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| Plan Documentation         | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| Operational Administration | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |
| M&A / Change in Control    | [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL] | [Brief description] | [Tier 1-4] |

---

## Detailed Findings

### Finding [N]: [Area] — [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL]

**Confidence**: [Definite / High / Probable / Possible / Unlikely]

**Issue**: [Description of the compliance position or failure]

**Legal Basis**: [Specific provision: 26 CFR § 1.409A-[x]; IRC § 409A(a)(1); Notice [year]-[number]]

**Facts**: [Specific facts from the plan documents, option records, or arrangement terms]

**Risk/Consequence**: [What happens if uncorrected — penalty exposure, income inclusion risk]

**Correction Path** (if applicable):

- **Program**: [Notice 2008-113 / Notice 2010-6 / Not correctable]
- **Correction window**: [Open — expires [year] / Closed / N/A]
- **Required action**: [Specific steps]
- **Penalty relief available**: [Full / Partial — describe / None]

**Estimated Penalty Exposure** (if NON-COMPLIANT or CRITICAL):

- Income inclusion: $[amount]
- Federal 20% excise tax: $[amount]
- Interest: $[estimated]
- California additional penalty (if applicable): $[amount]
- Total estimated exposure: $[range]

[Repeat for each finding]

---

## Prioritized Remediation Plan

**Tier 1 — Immediate (within 30 days):**

- [Action item]

**Tier 2 — High Priority (within 90 days):**

- [Action item]

**Tier 3 — Medium Priority (within 12 months):**

- [Action item]

**Tier 4 — Monitoring:**

- [Ongoing monitoring item]

---

## Valuation Compliance Summary

| Grant Date | # Options | Exercise Price | 409A Value | Safe Harbor Method | Appraisal Date | Status                      |
| ---------- | --------- | -------------- | ---------- | ------------------ | -------------- | --------------------------- |
| [Date]     | [#]       | $[amount]      | $[amount]  | [Method]           | [Date]         | [COMPLIANT / NON-COMPLIANT] |

---

## Next Steps

1. [Immediate action with owner and deadline]
2. [Plan amendment or correction filing]
3. [Engagement of tax counsel for CRITICAL items]
4. [Schedule next valuation refresh]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

Section 409A is a **US federal statute**. It applies uniformly across all US states,
but the following state-level overlays are material:

- **California (Cal. Rev. & Tax. Code § 17501)**: Additional 20% penalty on top of the
  federal 20% excise tax — total excise can reach 40% for California taxpayers. Apply this
  overlay whenever the service provider is a California resident or California-domiciled
  entity. [VERIFY current statute]
- **Other states**: Some states conform to the federal § 409A penalty regime; others have
  independent nonqualified deferred compensation rules. [VERIFY state-by-state conformity]
- **State wage payment laws**: In some states (e.g., California, New York), unauthorized
  delay of compensation may trigger separate wage-and-hour claims independent of § 409A.
- **Non-US service providers**: § 409A can apply to deferred compensation paid to non-US
  persons for services performed in the US. Foreign service providers may also have
  concurrent obligations under § 457A (offshore deferred compensation). Separate analysis
  required.

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis via Mode A skill creation.
Research basis: IRC § 409A; 26 CFR §§ 1.409A-1 through 1.409A-6; IRS Notice 2008-113;
IRS Notice 2010-6; IRS Notice 2010-80; 2-agent parallel research pipeline (Legal Research
Agent: web research on 409A safe harbor valuations, permissible payment events, short-term
deferral, six-month delay rule, correction programs, M&A implications, and California
overlay; Structural Analyst Agent: calibration against legalcode-contract-review 18-element
quality framework). Skill structure calibrated against legalcode-contract-review as the
gold standard. All statutory and regulatory citations marked [VERIFY] pending legalcode-mcp
verification. Not legal or tax advice — qualified professional review required.
