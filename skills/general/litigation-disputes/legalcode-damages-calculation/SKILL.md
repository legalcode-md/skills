---
name: legalcode-damages-calculation
description: Structure and calculate damages across economic, non-economic, punitive, and statutory categories
  for civil litigation, arbitration, and settlement negotiations. Use when quantifying harm, building
  damages models, preparing expert briefings, evaluating settlement ranges, or supporting early case assessment
  with defensible exposure analysis. Covers lost profits, consequential damages, diminution in value,
  pain and suffering, emotional distress, punitive/exemplary multipliers, statutory penalties, and fee-shifting.
  Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for US federal/state, England & Wales, and
  Australia. Integrates with legalcode-early-case-assessment for case-level exposure modeling and legalcode-brief-analyzer
  for damages-section persuasiveness review.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Damages Calculation

> **Disclaimer**: This skill provides a framework for AI-assisted damages analysis and
> calculation in civil matters. It does not constitute legal advice, expert testimony, or
> a substitute for forensic accounting or economic expert opinions. All outputs should be
> reviewed by qualified legal counsel and, where applicable, testifying experts licensed
> in the relevant jurisdiction before use in litigation, arbitration, or settlement
> negotiations. Damages law varies significantly by jurisdiction, claim type, and
> procedural posture; verify current applicability before relying on any methodology or
> figure described here. Statutory and case law references cited from memory carry
> hallucination risk -- verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill structures and calculates damages for civil litigation matters, producing
defensible, jurisdiction-aware exposure models suitable for:

- Early case assessment (pre-discovery damages framing)
- Settlement negotiation (BATNA/WATNA corridor analysis)
- Expert briefing (organizing inputs for economic/damages experts)
- Motion practice (damages-related dispositive motions and Daubert challenges)
- Trial preparation (damages proof checklist and presentation strategy)

**Covers:**

- **Economic damages**: Lost profits, lost revenue, diminution in value, out-of-pocket
  expenses, cost of repair/replacement, cost of cover, lost wages, lost earning capacity,
  medical expenses, future care costs
- **Non-economic damages**: Pain and suffering, emotional distress, loss of consortium,
  loss of enjoyment of life, hedonic damages, reputational harm
- **Punitive/exemplary damages**: Multiplier analysis, constitutional limits (US),
  availability and thresholds (UK/AU), aggravated damages distinction
- **Statutory damages**: Per-violation penalties, minimum/maximum ranges, willfulness
  multipliers, fee-shifting and cost awards
- **Prejudgment/postjudgment interest**: Calculation methodologies, statutory rates,
  compounding conventions
- **Mitigation**: Duty to mitigate analysis, avoidable consequences, collateral source
  offsets
- **Discounting and present value**: Time-value adjustments for future damages streams

**Does not:**

- Replace qualified forensic accountants, economists, or vocational experts
- Provide binding legal conclusions on recoverability or causation
- Generate final expert reports or sworn declarations
- Apply to criminal restitution (different framework)
- Cover equitable remedies (injunctions, specific performance) -- see separate skills

**Related skills:**

- `legalcode-early-case-assessment` -- Overall litigation exposure and strategy
- `legalcode-brief-analyzer` -- Persuasiveness of damages arguments in briefs
- `legalcode-case-timeline-builder` -- Chronology supporting damages causation
- `legalcode-privilege-review` -- Protecting damages analysis work product

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the governing substantive law
and forum procedural rules first, then localize all damages analysis accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Damages caps (statutory or common law)
- Punitive damages availability and constitutional/common law limits
- Non-economic damages caps (medical malpractice, tort reform statutes)
- Prejudgment interest rules (mandatory vs. discretionary, rate source, start date)
- Collateral source rule (traditional, modified, or abolished)
- Mitigation duty scope and burden of proof
- Expert testimony standards (Daubert, Frye, relevance-reliability)
- Fee-shifting and costs rules
- Statutory damages ranges for specific claim types
- Currency and exchange rate treatment for cross-border matters

**Reference anchors frequently needed:**

**United States (Federal):**

- Contract damages: UCC 2-706, 2-708, 2-712, 2-713, 2-714, 2-715; Restatement (Second)
  Contracts 347-356 [VERIFY]
- Tort damages: Restatement (Third) Torts: Liability for Physical and Emotional Harm
  [VERIFY]
- Punitive damages limits: BMW of N. Am. v. Gore, 517 U.S. 559 (1996); State Farm v.
  Campbell, 538 U.S. 408 (2003); Philip Morris USA v. Williams, 549 U.S. 346 (2007)
  [VERIFY]
- Expert standards: Daubert v. Merrell Dow, 509 U.S. 579 (1993); Kumho Tire v.
  Carmichael, 526 U.S. 137 (1999); FRE 702 (as amended) [VERIFY]
- Prejudgment interest: 28 U.S.C. 1961 (federal); state statutes vary [VERIFY]

**United States (State-specific common issues):**

- Tort reform caps: CA, TX, OH, FL, and many others have non-economic or total damages
  caps in certain claims [VERIFY STATE LAW]
- Comparative/contributory fault: Pure comparative (CA, NY), modified comparative (most
  states), contributory fault bar (AL, DC, MD, NC, VA) [VERIFY STATE LAW]
- Punitive damages caps: Many states cap punitives as multiple of compensatories or
  absolute dollar amount [VERIFY STATE LAW]

**England & Wales:**

- Contract damages: Hadley v. Baxendale (1854) 9 Exch 341; Victoria Laundry v. Newman
  (1949) 2 KB 528; Transfield Shipping v. Mercator [2008] UKHL 48 [VERIFY]
- Tort damages: Smith v. Manchester (1974) 17 KIR 1 (loss of earning capacity);
  Heil v. Rankin [2001] QB 272 (non-pecuniary damages tariff) [VERIFY]
- Exemplary/aggravated damages: Rookes v. Barnard [1964] AC 1129; Kuddus v. Chief
  Constable [2001] UKHL 29 [VERIFY]
- Interest: Senior Courts Act 1981 s.35A; Judgments Act 1838 s.17 (8% post-judgment)
  [VERIFY]
- Guidelines: Judicial College Guidelines for the Assessment of General Damages in
  Personal Injury Cases (16th ed.) [VERIFY]

**Australia:**

- Contract damages: Commonwealth v. Amann Aviation (1991) 174 CLR 64; Tabcorp Holdings
  v. Bowen Investments (2009) 236 CLR 272 [VERIFY]
- Tort damages: Todorovic v. Waller (1981) 150 CLR 402 (discount rate); Malec v. JC
  Hutton (1990) 169 CLR 638 (loss of chance) [VERIFY]
- Statutory caps: Civil Liability Acts in each state/territory (NSW CLA 2002, Vic WRCA
  2003, etc.) [VERIFY STATE/TERRITORY LAW]
- Exemplary damages: Gray v. Motor Accidents Commission (1998) 196 CLR 1 [VERIFY]
- Interest: Various state/territory Supreme Court Acts [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would materially change the damages model structure
- Multiple valid calculation methodologies exist and the user's preference matters
- Jurisdiction-specific rules create forks in the analysis
- Risk tolerance or settlement posture affects the range to present

Use the structured-options pattern wherever marked with **CLARIFY** below. If the user has
already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Matter Inputs

Accept matter information in any of these formats:

- **Pleadings/claims**: Complaint, statement of claim, demand letter, or arbitration notice
- **Case summary**: Narrative description of the dispute and claimed harms
- **Financial documents**: P&L statements, invoices, contracts, medical bills, wage records
- **Expert materials**: Draft or final expert reports, deposition transcripts
- **Prior damages analysis**: Earlier exposure models or settlement evaluations

If insufficient information is provided to structure damages, prompt the user to supply:

- Nature of the claims (contract, tort, statutory, mixed)
- Plaintiff/claimant identity (individual, business entity, class)
- Key harm categories alleged
- Available supporting documentation

### Step 2: Gather Damages Context

**CLARIFY** -- Before beginning the analysis, ask the user these questions:

1. **What is the purpose of this damages analysis?**
   - Options: `Early case assessment (pre-discovery)`, `Settlement negotiation corridor`,
     `Expert briefing/organization`, `Motion practice support`, `Trial preparation`,
     `Appellate damages review`, `Insurance coverage evaluation`
   - _Why this matters_: Purpose determines precision requirements and output emphasis.

2. **Which side are you on?**
   - Options: `Plaintiff/Claimant`, `Defendant/Respondent`, `Neutral evaluator`
   - _Why this matters_: Determines whether to emphasize maximizing or minimizing exposure,
     or presenting balanced ranges.

3. **What is the governing substantive law?**
   - Options: `US federal`, `US state (specify)`, `England & Wales`, `Australia
(specify state/territory)`, `Other (specify)`, `Multiple/uncertain`
   - _Why this matters_: Damages rules vary dramatically by jurisdiction.

4. **What claim types are involved?**
   - Options: `Contract breach`, `Tort/negligence`, `Statutory violation`, `Fraud`,
     `Employment/discrimination`, `IP infringement`, `Antitrust`, `Securities`,
     `Personal injury`, `Professional malpractice`, `Other (specify)`
   - Allow multiple selections.
   - _Why this matters_: Different claim types have different damages rules, caps, and
     available categories.

5. **What is the procedural posture?**
   - Options: `Pre-suit`, `Early litigation (pre-discovery)`, `Active discovery`,
     `Expert discovery`, `Summary judgment phase`, `Trial imminent`, `Post-trial/appeal`,
     `Arbitration`, `Mediation/settlement`
   - _Why this matters_: Affects data availability and precision expectations.

6. **Are experts already retained or contemplated?**
   - Options: `Yes - economist/damages expert`, `Yes - vocational/medical expert`,
     `Yes - industry expert`, `Multiple experts`, `None yet`, `Considering retention`
   - _Why this matters_: Determines whether this analysis is initial framing or expert
     support.

If the user provides partial context, proceed with reasonable defaults but **state
assumptions explicitly** before the analysis.

### Step 3: Identify Governing Damages Framework

Based on the claim types and jurisdiction identified:

1. **Map claim types to damages categories**:
   | Claim Type | Typical Damages Categories |
   |------------|---------------------------|
   | Contract breach | Expectation, reliance, restitution, consequential, incidental |
   | Tort/negligence | Compensatory (economic + non-economic), punitive (if available) |
   | Fraud | Out-of-pocket, benefit of bargain, consequential, punitive |
   | Employment/discrimination | Back pay, front pay, emotional distress, punitive, statutory |
   | IP infringement | Actual damages, infringer's profits, statutory, enhanced/willful |
   | Antitrust | Actual damages (trebled), injunctive, costs/fees |
   | Personal injury | Medical, lost wages, future care, pain/suffering, loss of consortium |

2. **Identify jurisdiction-specific constraints**:
   - Caps on non-economic damages
   - Caps on punitive damages
   - Mandatory trebling or other multipliers
   - Fee-shifting rules
   - Prejudgment interest availability and rate

3. **Document the framework** in the Glass Box audit trail.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to build a working legal reference file for this
damages analysis.

**Research process:**

1. **Identify controlling statutes and case law** for each damages category in the
   governing jurisdiction.

2. **Search legalcode-mcp** for:
   - Damages calculation standards for the claim types involved
   - Caps, floors, and multipliers applicable in the jurisdiction
   - Leading cases on foreseeability, certainty, and mitigation
   - Expert testimony standards for damages evidence
   - Prejudgment interest rules and rates

3. **Save results** to a local temporary reference file:

   ```markdown
   # Legal Authority Reference -- [Matter Name] Damages Analysis

   ## Governing Law: [Jurisdiction]

   ## Date Gathered: [date]

   ### Damages Standards by Claim Type

   - [Claim type]: [Controlling statute/case, damages measure]

   ### Caps and Limits

   - [Category]: [Cap amount, statutory reference]

   ### Key Case Law

   - [Case name, citation, holding on damages calculation]

   ### Interest Rules

   - Prejudgment: [Rate, source, start date rule]
   - Postjudgment: [Rate, source]
   ```

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with general damages principles but flag verification requirements

### Step 5: Structure the Damages Model

Build a comprehensive damages model covering all applicable categories.

**CLARIFY** -- For complex matters with multiple claim types:

- "This matter involves [N] claim types with potentially overlapping damages. Should I
  build a single integrated model, or separate models by claim type with a reconciliation
  summary?"
- "Some damages categories may be duplicative (e.g., lost profits under contract and
  tort). How should I handle overlap -- conservative (no double-counting), aggressive
  (present full amount under each theory), or present both views?"

#### 5a. Economic Damages

For each economic damages category, build a calculation framework:

**Lost Profits / Lost Revenue**

| Element             | Data Needed                                         | Calculation Method       | Notes                                |
| ------------------- | --------------------------------------------------- | ------------------------ | ------------------------------------ |
| **But-for revenue** | Historical financials, growth trends, industry data | Projection from baseline | Before-and-after or yardstick method |
| **Actual revenue**  | Post-breach financials                              | Actual recorded          | Document collection required         |
| **Lost revenue**    | [But-for] minus [Actual]                            | Subtraction              | Gross number before expenses         |
| **Avoided costs**   | Variable costs saved                                | Cost analysis            | Deducted from lost revenue           |
| **Lost profits**    | [Lost revenue] minus [Avoided costs]                | Subtraction              | Net figure for recovery              |

**[JURISDICTION-SPECIFIC]** Lost profits requirements:

- **US**: Must prove with "reasonable certainty" -- not speculative. New business rule may
  limit recovery for enterprises without track record [VERIFY]
- **UK**: Must satisfy "contemplation of the parties" test (Hadley v. Baxendale) and be
  within "reasonable contemplation" as a "serious possibility" [VERIFY]
- **AU**: Must be within "reasonable contemplation" under Hadley principles as received in
  Australia [VERIFY]

**Diminution in Value**

| Element                      | Method                                           | Application              |
| ---------------------------- | ------------------------------------------------ | ------------------------ |
| **Fair market value before** | Comparable sales, income approach, cost approach | Establish baseline       |
| **Fair market value after**  | Same methodology, post-harm condition            | Establish impaired value |
| **Diminution**               | [Before] minus [After]                           | Measure of harm          |

**Out-of-Pocket / Reliance Expenses**

- Catalog all expenses incurred in reliance on the breached promise or tortious conduct
- Document each expense with supporting evidence (invoices, receipts, contracts)
- Distinguish between wasted expenditure and recoverable costs

**Medical Expenses and Future Care Costs (Personal Injury)**

| Category                       | Past/Incurred | Future/Projected | Documentation     |
| ------------------------------ | ------------- | ---------------- | ----------------- |
| Hospital/surgical              | $             | $                | Bills, records    |
| Physician/specialist           | $             | $                | Bills, records    |
| Medication                     | $             | $                | Pharmacy records  |
| Physical therapy               | $             | $                | Treatment records |
| Home care/assistance           | $             | $                | Caregiver records |
| Medical equipment              | $             | $                | Invoices          |
| Life care plan (if applicable) | N/A           | $                | Expert report     |

**[JURISDICTION-SPECIFIC]** Medical damages requirements:

- **US**: Collateral source rule varies by state -- some allow offset for insurance
  payments, others do not [VERIFY STATE LAW]
- **UK**: NHS treatment generally not recoverable as private cost; private treatment
  recoverable if reasonable [VERIFY]
- **AU**: State/territory civil liability acts may cap or modify recovery [VERIFY]

**Lost Wages and Earning Capacity**

| Element                 | Past                             | Future           | Calculation          |
| ----------------------- | -------------------------------- | ---------------- | -------------------- |
| **Base wage/salary**    | $ per period                     | $ per period     | Employment records   |
| **Benefits value**      | $                                | $                | Benefits summary     |
| **Lost periods**        | [dates]                          | [years]          | Work-life expectancy |
| **Mitigation earnings** | $                                | $                | Post-harm income     |
| **Net lost wages**      | [Base + Benefits] - [Mitigation] | Discounted to PV | Sum                  |

**[JURISDICTION-SPECIFIC]** Earning capacity considerations:

- **US**: Work-life expectancy tables, discount rate debates, tax gross-up may apply
  [VERIFY]
- **UK**: Smith v. Manchester award for handicap on labor market; Ogden Tables for
  multipliers [VERIFY]
- **AU**: 5% discount rate under Todorovic v. Waller; 3% under some state statutes
  [VERIFY STATE LAW]

#### 5b. Non-Economic Damages

**CLARIFY** -- Non-economic damages vary dramatically by jurisdiction and claim type:

- "Non-economic damages are available but may be capped in [jurisdiction]. The current
  cap is [amount] for [claim type]. Should I calculate uncapped amounts and then apply
  the cap, or work within the cap from the start?"

**Pain and Suffering**

| Approach                | Method                      | Application                        |
| ----------------------- | --------------------------- | ---------------------------------- |
| **Per diem**            | Daily rate x duration       | Common in US plaintiff arguments   |
| **Multiplier**          | [Economic damages] x factor | Common defense/settlement approach |
| **Comparable verdicts** | Similar cases, adjusted     | Jury research, verdict databases   |
| **Judicial guidelines** | Published tariffs           | UK Judicial College Guidelines     |

**Emotional Distress**

- Distinguish between:
  - Parasitic emotional distress (accompanying physical injury)
  - Stand-alone emotional distress claims (IIED, NIED)
- Document manifestations: medical treatment, therapy, impact on daily life
- [JURISDICTION-SPECIFIC]: Stand-alone emotional distress claims have varying
  requirements (physical impact rule, zone of danger, Dillon factors) [VERIFY]

**Loss of Consortium / Loss of Society**

- Available to spouse, sometimes children/parents
- [JURISDICTION-SPECIFIC]: Not available in all jurisdictions or for all claims [VERIFY]

**Non-Economic Damages Caps Summary**

| Jurisdiction      | Cap Type | Amount    | Claim Types | Source    |
| ----------------- | -------- | --------- | ----------- | --------- |
| [State/Territory] | [Type]   | $[Amount] | [Claims]    | [Statute] |

#### 5c. Punitive / Exemplary Damages

**CLARIFY** -- Punitive damages availability varies significantly:

- "Punitive damages may be available under [jurisdiction] law for [claim type] if
  [standard] is met. What is the evidence of [malice/willfulness/gross negligence]?
  Should I include a punitive damages estimate in the model?"

**US Punitive Damages Analysis**

| Factor                   | Assessment                                                | Support                  |
| ------------------------ | --------------------------------------------------------- | ------------------------ |
| **Availability**         | Is punitive available for this claim type?                | Statute/common law       |
| **Standard**             | Malice, willfulness, gross negligence, reckless disregard | Jurisdiction-specific    |
| **Evidence of conduct**  | What supports the required mental state?                  | Document record          |
| **Reprehensibility**     | Gore factor 1 -- degree of reprehensibility               | Five subfactors          |
| **Ratio**                | Gore factor 2 -- ratio to compensatory damages            | Single digit presumptive |
| **Comparable penalties** | Gore factor 3 -- civil/criminal sanctions                 | Statutory comparisons    |
| **Net worth**            | Defendant's financial condition                           | Discovery required       |
| **Statutory cap**        | State-specific cap if applicable                          | [VERIFY STATE LAW]       |

**[JURISDICTION-SPECIFIC]** Punitive damages limits:

- **US Federal (constitutional)**: Single-digit ratio presumptively valid; double-digit
  ratios rarely appropriate; low compensatories may justify higher ratio (State Farm v.
  Campbell) [VERIFY]
- **US States**: Many cap punitives at 2-4x compensatories or fixed dollar amounts
  [VERIFY STATE LAW]
- **UK**: Exemplary damages available only in narrow categories (Rookes v. Barnard):
  oppressive government action, calculated profit-seeking, statutory authorization;
  aggravated damages more broadly available [VERIFY]
- **AU**: Exemplary damages available for intentional torts, outrageous conduct; some
  statutory restrictions in civil liability legislation [VERIFY STATE LAW]

#### 5d. Statutory Damages

For claims with statutory damages provisions:

| Statute   | Violation Type | Minimum | Maximum | Willfulness Multiplier | Fee-Shifting |
| --------- | -------------- | ------- | ------- | ---------------------- | ------------ |
| [Statute] | [Type]         | $[Min]  | $[Max]  | [Multiplier]           | [Yes/No]     |

**[JURISDICTION-SPECIFIC]** Common statutory damages schemes:

- **US Copyright Act** (17 U.S.C. 504): $750-$30,000 per work; willful up to $150,000;
  innocent down to $200 [VERIFY]
- **US Lanham Act** (15 U.S.C. 1117): Actual damages or profits; trebling for willful;
  statutory up to $2M for cyberpiracy [VERIFY]
- **US FCRA** (15 U.S.C. 1681n): $100-$1,000 per violation; punitives available [VERIFY]
- **US TCPA** (47 U.S.C. 227): $500 per violation; trebled for willful [VERIFY]
- **UK Data Protection Act 2018 / UK GDPR**: No statutory damages per se; actual damages
  - distress; ICO fines separate [VERIFY]
- **AU Privacy Act 1988**: No statutory damages; compensation for loss/damage [VERIFY]

#### 5e. Interest Calculations

**Prejudgment Interest**

| Element          | Value                                     | Source                  |
| ---------------- | ----------------------------------------- | ----------------------- |
| **Availability** | Mandatory / Discretionary / Not available | [Jurisdiction rule]     |
| **Rate**         | [%]                                       | [Statute or court rule] |
| **Start date**   | [Date of harm / Date of demand / Other]   | [Jurisdiction rule]     |
| **End date**     | Judgment date                             | Standard                |
| **Compounding**  | Simple / Compound                         | [Jurisdiction rule]     |
| **Calculation**  | Principal x Rate x Time                   |                         |

**[JURISDICTION-SPECIFIC]** Prejudgment interest rules:

- **US Federal**: 28 U.S.C. 1961 (T-bill rate, post-judgment); prejudgment varies by
  claim type and state law applied [VERIFY]
- **US States**: Highly variable -- statutory rates, discretionary awards, different start
  dates [VERIFY STATE LAW]
- **UK**: Senior Courts Act 1981 s.35A -- discretionary, typically 1-2% above base rate
  for commercial, 2% simple for PI; special damages from date of loss [VERIFY]
- **AU**: State/territory Supreme Court Acts -- typically discretionary, rates vary
  [VERIFY STATE LAW]

**Postjudgment Interest**

- US Federal: 52-week T-bill rate, compounded annually (28 U.S.C. 1961) [VERIFY]
- UK: 8% simple (Judgments Act 1838 s.17) [VERIFY]
- AU: Varies by state/territory [VERIFY STATE LAW]

### Step 6: Build the Damages Range

Construct a three-point estimate for each damages category:

| Category                   | Low | Base | High | Assumptions/Drivers |
| -------------------------- | --- | ---- | ---- | ------------------- |
| [Category 1]               | $   | $    | $    | [Key assumptions]   |
| [Category 2]               | $   | $    | $    | [Key assumptions]   |
| ...                        |     |      |      |                     |
| **Subtotal: Economic**     | $   | $    | $    |                     |
| **Subtotal: Non-Economic** | $   | $    | $    |                     |
| **Subtotal: Punitive**     | $   | $    | $    |                     |
| **Subtotal: Statutory**    | $   | $    | $    |                     |
| **Prejudgment Interest**   | $   | $    | $    |                     |
| **TOTAL**                  | $   | $    | $    |                     |

**Range construction principles:**

- **Low**: Conservative assumptions, defense-favorable positions, caps applied, maximum
  mitigation credit
- **Base**: Reasonable middle-ground assumptions, likely outcome
- **High**: Aggressive but defensible assumptions, plaintiff-favorable positions, minimum
  mitigation offset

**CLARIFY** -- For settlement purposes:

- "Should the range account for litigation risk (probability-weighted values) or present
  gross damages subject to separate liability risk assessment?"
- "What discount factor for verdict uncertainty would you apply? Options: None (present
  gross), 25% (strong case), 50% (balanced), 75% (weak case)"

### Step 7: Mitigation and Offsets Analysis

#### 7a. Duty to Mitigate

| Question                                             | Assessment       | Impact                |
| ---------------------------------------------------- | ---------------- | --------------------- |
| Did the plaintiff take reasonable steps to mitigate? | [Yes/No/Partial] |                       |
| What mitigation was possible?                        | [List options]   |                       |
| What mitigation was undertaken?                      | [List actions]   |                       |
| What mitigation credit should defendant receive?     | $[Amount]        | Deducted from damages |

**[JURISDICTION-SPECIFIC]** Mitigation principles:

- **US**: Avoidable consequences doctrine -- plaintiff cannot recover damages that
  reasonable efforts would have prevented [VERIFY]
- **UK**: Duty to take reasonable steps -- burden on defendant to prove failure to
  mitigate [VERIFY]
- **AU**: Similar to UK -- plaintiff must act reasonably but not required to take
  extraordinary steps [VERIFY]

#### 7b. Collateral Source Offsets

| Collateral Source    | Amount | Offset Rule | Impact             |
| -------------------- | ------ | ----------- | ------------------ |
| Insurance payments   | $      | [Rule]      | [Offset/No offset] |
| Government benefits  | $      | [Rule]      | [Offset/No offset] |
| Employer benefits    | $      | [Rule]      | [Offset/No offset] |
| Third-party payments | $      | [Rule]      | [Offset/No offset] |

**[JURISDICTION-SPECIFIC]** Collateral source rule:

- **US**: Traditional rule (no offset) modified in many states by tort reform [VERIFY
  STATE LAW]
- **UK**: Various statutory schemes require recoupment (CRU for NHS/benefits) [VERIFY]
- **AU**: State civil liability acts modify traditional rule [VERIFY STATE LAW]

#### 7c. Comparative/Contributory Fault

If fault allocation applies:

| Plaintiff fault % | System                                       | Impact on Recovery |
| ----------------- | -------------------------------------------- | ------------------ |
| [%]               | [Pure comparative / Modified / Contributory] | [Reduction / Bar]  |

### Step 8: Present Value Calculations

For future damages streams, apply appropriate discounting:

| Future Damages Stream   | Duration | Discount Rate | Present Value |
| ----------------------- | -------- | ------------- | ------------- |
| Future lost wages       | [years]  | [%]           | $             |
| Future medical care     | [years]  | [%]           | $             |
| Future earning capacity | [years]  | [%]           | $             |

**[JURISDICTION-SPECIFIC]** Discount rate approaches:

- **US**: Market rate debate -- risk-free rate vs. market rate; inflation adjustment
  (total offset method) [VERIFY]
- **UK**: Discount rate set by Lord Chancellor (currently -0.25% for PI, subject to
  change) [VERIFY]
- **AU**: 5% under Todorovic v. Waller; some states have statutory rates (e.g., NSW 5%,
  Vic 5%) [VERIFY STATE LAW]

### Step 9: Sensitivity Analysis

Identify key variables and test sensitivity:

| Variable                 | Base Case | Sensitivity Range | Impact on Total |
| ------------------------ | --------- | ----------------- | --------------- |
| Lost profits growth rate | [%]       | [Low-High]        | $[Low]-$[High]  |
| Work-life expectancy     | [years]   | [Low-High]        | $[Low]-$[High]  |
| Discount rate            | [%]       | [Low-High]        | $[Low]-$[High]  |
| Punitive multiplier      | [X]       | [Low-High]        | $[Low]-$[High]  |
| Non-economic multiplier  | [X]       | [Low-High]        | $[Low]-$[High]  |

**Tornado chart** (conceptual): List variables by impact magnitude to identify which
assumptions drive the model most.

### Step 10: Quality Verification

Before delivering the analysis, run the quality checks:

#### 10a. Citation Quality Gates

| Gate           | Rule                                             | Status    |
| -------------- | ------------------------------------------------ | --------- |
| **Source**     | Every legal claim cites statute/case or [VERIFY] | Pass/Fail |
| **Format**     | Citations follow jurisdiction convention         | Pass/Fail |
| **Currency**   | Caps, rates, and rules checked for current law   | Pass/Fail |
| **Domain**     | Analysis stays within governing law              | Pass/Fail |
| **Confidence** | Uncertainty explicitly stated                    | Pass/Fail |

#### 10b. Self-Interrogation for High-Severity Items

For any damages category over $1M or any punitive/statutory multiplier:

**Pass 1 -- Legal Chain Integrity**:

- Does the damages calculation methodology follow from the cited legal standards?
- Would a court in this jurisdiction award this category and amount?
- What is the strongest challenge to this calculation?

**Pass 2 -- Completeness**:

- Have all potentially applicable damages categories been considered?
- Have all offsets, caps, and limitations been applied?
- Are there additional damages theories not yet modeled?

**Pass 3 -- Challenge**:

- What is the strongest defense argument against this damages figure?
- How would a defense expert attack this calculation?
- Is this figure within the range of comparable verdicts/awards?

#### 10c. Confidence Scoring

Assign confidence to each material calculation:

| Level        | Range     | Meaning                                        | Action                        |
| ------------ | --------- | ---------------------------------------------- | ----------------------------- |
| **Definite** | 0.95-1.0  | Clear documentation, settled methodology       | State with confidence         |
| **High**     | 0.80-0.94 | Strong support, minor interpretation questions | State with caveat             |
| **Probable** | 0.60-0.79 | Reasonable methodology, data gaps              | State with reasoning          |
| **Possible** | 0.40-0.59 | Significant uncertainty, multiple approaches   | Flag for expert review        |
| **Unlikely** | 0.0-0.39  | Speculative, weak support                      | Do not rely; note uncertainty |

### Step 11: Generate Deliverables

Produce the damages analysis using the output format template below, tailored to the
purpose identified in Step 2.

---

## Damages Classification System

### SUPPORTED -- Well-Documented

The damages category has strong evidentiary support, clear legal basis, and defensible
calculation methodology.

**Characteristics:**

- Documentary evidence supports each input
- Calculation methodology follows accepted standards
- Legal recoverability is clear in the jurisdiction
- Within range of comparable awards/verdicts

**Action**: Include in core damages model with high confidence.

### PROBABLE -- Reasonable Support

The damages category has reasonable support but some gaps in evidence or methodology
debates.

**Characteristics:**

- Some documentation gaps exist but can be addressed
- Methodology is reasonable but alternatives exist
- Legal recoverability is likely but not certain
- Some comparable verdict support

**Action**: Include in damages model with medium confidence; note assumptions.

### SPECULATIVE -- Weak Support

The damages category has significant evidentiary or legal obstacles.

**Characteristics:**

- Material documentation gaps
- Methodology requires significant assumptions
- Legal recoverability is uncertain
- Limited comparable support

**Action**: Include as sensitivity upside only; flag for expert evaluation; may not
survive Daubert/admissibility challenge.

### NOT RECOVERABLE -- Legal Bar

The damages category is not recoverable under the governing law.

**Characteristics:**

- Statutory cap bars or limits recovery
- Jurisdictional rule excludes category
- Causation chain is broken
- Damages are too speculative to recover

**Action**: Exclude from damages model; document the legal bar for record.

---

## Actionable Output Per Finding

For each damages category analyzed, provide:

```
**Category**: [Damages category name]
**Classification**: [SUPPORTED / PROBABLE / SPECULATIVE / NOT RECOVERABLE]
**Confidence**: [0.XX -- Level]

**Calculation Summary**:
- Low estimate: $[amount]
- Base estimate: $[amount]
- High estimate: $[amount]

**Legal Basis**: [Statute/case supporting recoverability]

**Key Assumptions**:
1. [Assumption 1]
2. [Assumption 2]

**Evidence Required**:
- [Document/testimony needed]

**Challenges/Risks**:
- [Potential defense argument]

**Expert Support Needed**: [Yes/No -- type of expert]
```

---

## Prioritization Framework

### Tier 1 -- Core Damages (High Confidence)

Categories that are clearly recoverable, well-documented, and form the floor of any
settlement or judgment:

- Out-of-pocket economic damages with documentation
- Lost wages with employment records
- Medical expenses with bills
- Statutory damages within clear minimums

**Strategy**: Lead negotiations with these figures; form the baseline.

### Tier 2 -- Material Damages (Medium Confidence)

Categories that are likely recoverable but require additional proof or expert support:

- Lost profits with reasonable projection methodology
- Future damages with present value calculation
- Non-economic damages within guideline ranges
- Prejudgment interest under favorable calculation

**Strategy**: Include in damages model; prepare for defense challenges.

### Tier 3 -- Upside Damages (Lower Confidence)

Categories that may be recoverable if the case goes well but face obstacles:

- Punitive damages (requires meeting heightened standard)
- Enhanced statutory damages (requires willfulness proof)
- Non-economic damages above guideline ranges
- Speculative future damages

**Strategy**: Include in high-end range; use as negotiation leverage; prepare for
aggressive defense attacks.

---

## Citation Quality Gates

Run these gates silently before delivering any output:

| Gate           | Rule                                                                | Fail Action                   |
| -------------- | ------------------------------------------------------------------- | ----------------------------- |
| **Source**     | Every damages rule cites statute/case or established methodology    | Add citation or mark [VERIFY] |
| **Format**     | Citations follow jurisdiction convention                            | Fix format                    |
| **Currency**   | Caps, interest rates, and statutory amounts checked for current law | Flag [CHECK CURRENCY]         |
| **Domain**     | Analysis stays within governing law; no jurisdiction bleed          | Remove or flag                |
| **Confidence** | Uncertainty explicitly stated; not masked by precision              | Add qualifier                 |

---

## Self-Interrogation for Material Calculations

For any damages category exceeding $500K or any multiplier (punitive, treble, statutory
enhancement), apply this 3-pass review:

**Pass 1 -- Methodology Integrity**:

- Does the calculation methodology follow from the cited legal standard?
- Would an expert in this field use this approach?
- What are the alternative methodologies and why was this one chosen?

**Pass 2 -- Data Completeness**:

- Are all inputs documented or documented-assumption?
- What data gaps exist and how were they addressed?
- Would additional discovery materially change the number?

**Pass 3 -- Challenge Resistance**:

- How would opposing counsel attack this figure?
- How would a defense expert critique the methodology?
- Would this calculation survive a Daubert/admissibility challenge?

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                  | Action                        |
| ------------ | --------- | ---------------------------------------- | ----------------------------- |
| **Definite** | 0.95-1.0  | Clear documentation, settled methodology | State with confidence         |
| **High**     | 0.80-0.94 | Strong support, minor questions          | State with brief caveat       |
| **Probable** | 0.60-0.79 | Reasonable but debatable                 | State with reasoning          |
| **Possible** | 0.40-0.59 | Genuinely uncertain                      | Flag for expert review        |
| **Unlikely** | 0.0-0.39  | Speculative                              | Do not rely; note [UNCERTAIN] |

---

## Glass Box Audit Trail

Every damages analysis MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-damages-calculation"
  matter: "[Matter name/identifier]"
  purpose: "[ECA / Settlement / Expert briefing / Trial prep]"
  side: "[Plaintiff / Defendant / Neutral]"
  governing_law: "[Jurisdiction]"
  claim_types: "[List]"
  procedural_posture: "[Stage]"
  damages_categories_analyzed:
    - "[Category 1]"
    - "[Category 2]"
  total_range:
    low: "$[amount]"
    base: "$[amount]"
    high: "$[amount]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute 1 -- VERIFIED or [VERIFY]]"
  case_law_consulted:
    - "[Case 1 -- VERIFIED or [VERIFY]]"
  citations_verified: "[N VERIFIED] / [N [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW -- [rationale]"
  key_assumptions:
    - "[Assumption 1]"
    - "[Assumption 2]"
  data_gaps:
    - "[Gap 1]"
  limitations:
    - "[Limitation 1]"
  expert_support_recommended: "[Yes/No -- type]"
  reviewer: "AI-assisted -- requires qualified legal and expert review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in damages analysis:

1. **Single-point estimates without ranges** -- Damages calculations are inherently
   uncertain. Presenting a single number without a range masks uncertainty and reduces
   credibility. Always provide low/base/high.

2. **Precision beyond data support** -- Calculating damages to the penny when inputs are
   estimates creates false precision. Match output precision to input reliability.

3. **Ignoring mitigation** -- Failing to account for the plaintiff's duty to mitigate or
   presenting gross damages without offset analysis. Courts expect mitigation to be
   addressed.

4. **Jurisdiction bleed** -- Applying US punitive damages concepts in UK analysis, or
   using UK Judicial College guidelines in US jury trials. Keep frameworks jurisdiction-
   appropriate.

5. **Double-counting** -- Recovering the same harm twice under different theories (e.g.,
   lost profits under both contract and tort without reconciliation). Address overlap
   explicitly.

6. **Ignoring caps** -- Calculating uncapped damages when statutory or constitutional
   caps apply. Always check for and apply applicable caps.

7. **Speculative future damages without discounting** -- Presenting future damages
   streams at face value without present-value adjustment. Always discount future
   amounts.

8. **Punitive damages without predicate** -- Calculating punitive damages without
   establishing that the conduct meets the jurisdiction's standard for punitives.
   Punitives require a legal gateway.

9. **Comparable verdict cherry-picking** -- Selecting only the highest verdicts as
   comparables while ignoring lower ones. Use median/range from representative sample.

10. **Expert methodology without foundation** -- Presenting calculations using expert
    methodologies without documenting the methodology or why it applies. If using an
    expert approach, cite it.

11. **Ignoring the record** -- Calculating damages based on claimed amounts rather than
    documented amounts. Use documented figures; note where documentation is needed.

12. **Conflating liability and damages** -- Presenting damages as if liability is
    established when it is contested. Separate damages analysis from liability
    probability unless explicitly probability-weighting.

13. **Static analysis without sensitivity** -- Failing to identify which assumptions
    drive the model and how changes affect the total. Always include sensitivity
    analysis for key variables.

14. **Missing interest** -- Calculating damages through trial date but ignoring
    prejudgment interest, which can add significant value in long-running matters.

15. **Assumptions without documentation** -- Making assumptions without stating them.
    Every assumption should be explicit and in the audit trail.

---

## Writing Standards

Apply plain-language discipline to all output:

**For damages summaries** (may be shared with clients, executives, insurers):

- Plain language accessible to non-lawyers
- Clear separation of facts, assumptions, and conclusions
- Ranges rather than false precision
- Key drivers highlighted

**For expert briefings**:

- Technical terminology appropriate
- Full documentation of inputs and methodology
- Clear statement of what expert needs to provide
- Areas for expert judgment identified

**For litigation support**:

- Cite-ready format for briefs and motions
- Record citations for factual assertions
- Challenges and counterarguments anticipated
- Suitable for Daubert/admissibility preparation

**Quality gates before delivery**:

1. Can a business stakeholder understand the total exposure range?
2. Are all material assumptions stated?
3. Is every legal claim backed by citation or flagged [VERIFY]?
4. Does precision match data quality?
5. Have caps, offsets, and limitations been addressed?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-specific damages caps, interest rates, and calculation
  standards
- Verify statutory damages amounts are current
- Pull recent case law on methodology challenges (Daubert, admissibility)
- Check comparable verdicts in the jurisdiction
- Mark legalcode-mcp-sourced citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structuring the damages model; flag legal verification needs
- Use web search for publicly available caps and rates

**Integration with related skills:**

- **legalcode-early-case-assessment**: This skill provides the damages component for
  overall exposure modeling. ECA provides the liability probability; damages calculation
  provides the magnitude.
- **legalcode-brief-analyzer**: Use brief analyzer to evaluate the persuasiveness of
  damages arguments in motions and briefs before filing.

---

## Output Format Template

Structure the final deliverable based on purpose:

### For Early Case Assessment / Settlement

```markdown
# Damages Analysis Summary

**Matter**: [Name/identifier]
**Date**: [Date]
**Purpose**: [ECA / Settlement corridor / Insurance evaluation]
**Side**: [Plaintiff / Defendant / Neutral]
**Governing Law**: [Jurisdiction]

---

## Executive Summary

**Total Damages Range**:
| | Low | Base | High |
|--|-----|------|------|
| **Economic** | $ | $ | $ |
| **Non-Economic** | $ | $ | $ |
| **Punitive** | $ | $ | $ |
| **Statutory** | $ | $ | $ |
| **Interest** | $ | $ | $ |
| **TOTAL** | $ | $ | $ |

**Key Drivers**: [Top 3 variables affecting the range]

**Critical Assumptions**: [Top 3 assumptions to validate]

---

## Damages by Category

### Economic Damages

#### [Category 1] -- [Classification] | Confidence: [Level]

[Detailed calculation and support]

[Repeat for each category]

### Non-Economic Damages

[Detailed analysis]

### Punitive Damages

[Availability analysis and calculation if applicable]

### Statutory Damages

[If applicable]

### Interest Calculations

[Prejudgment and postjudgment]

---

## Mitigation and Offsets

[Analysis of duty to mitigate, collateral sources, comparative fault]

---

## Sensitivity Analysis

[Key variables and impact on range]

---

## Comparables

[Comparable verdicts/settlements if available]

---

## Data Gaps and Next Steps

| Gap     | Impact   | Recommended Action | Priority       |
| ------- | -------- | ------------------ | -------------- |
| [Gap 1] | [Impact] | [Action]           | [High/Med/Low] |

---

## Glass Box Audit Trail

[YAML block]
```

### For Expert Briefing

```markdown
# Expert Damages Briefing

**Matter**: [Name]
**Expert Type Needed**: [Economist / Forensic accountant / Vocational / Medical]
**Date**: [Date]

---

## Scope of Engagement

[What the expert is being asked to opine on]

---

## Claim Types and Damages Theories

[Legal framework for damages recovery]

---

## Key Documents Provided

| Document | Bates Range | Relevance        |
| -------- | ----------- | ---------------- |
| [Doc 1]  | [Range]     | [Why it matters] |

---

## Preliminary Calculations (Subject to Expert Refinement)

[Structured calculations with methodology notes]

---

## Questions for Expert

1. [Question requiring expert judgment]
2. [Methodology question]
3. [Data sufficiency question]

---

## Anticipated Defense Challenges

[How the defense will attack the damages; what the expert should address]

---

## Daubert/Admissibility Considerations

[Methodological foundation needs]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with hardcoded local rules
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific caps, rates, and limitations tables
4. Add local expert testimony standards
5. Add jurisdiction-specific anti-patterns
6. Update frontmatter to reference the specific jurisdiction

**Recommended jurisdiction variants:**

- `legalcode-damages-calculation-us-federal` -- Federal law with state law markers
- `legalcode-damages-calculation-ew` -- England & Wales specific
- `legalcode-damages-calculation-au-federal` -- Australian federal with state markers

---

## Provenance

Created by Legalcode (2026-02-28). Original synthesis combining:

- Damages calculation methodologies from forensic economics and litigation practice
- US, UK, and Australian damages law frameworks with jurisdiction markers
- Quality assurance frameworks from legalcode-contract-review reference standard
- Integration points with legalcode-early-case-assessment and legalcode-brief-analyzer
- Anti-patterns and writing standards adapted for damages-specific context

This skill is Task #36 from SKILL_CREATION_TASKS.md, complementing the litigation
toolkit alongside legalcode-early-case-assessment and legalcode-brief-analyzer.
