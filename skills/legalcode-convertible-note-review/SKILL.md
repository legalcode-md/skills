---
name: legalcode-convertible-note-review
description: Review convertible notes and convertible loan notes (CLNs) for founders, investors, and counsel
  — covering interest accrual and compounding mechanics, maturity and redemption risk, qualified financing
  definition and threshold, conversion mechanics (discount rate, valuation cap, shadow preferred stock,
  post-money formula), MFN clause analysis, pro-rata rights, prepayment and subordination provisions,
  events of default, and amendment consent thresholds. Use when reviewing or negotiating a convertible
  note, convertible loan note, bridge note, or demand note convertible instrument at any stage (pre-seed
  through Series A bridge).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review convertible notes and convertible loan notes (CLNs) for founders, investors, and counsel — covering interest accrual and compounding mechanics, maturity and redemption risk, qualified financing definition and threshold, conversion mechanics (discount rate, valuation cap, shadow preferred stock, post-money formula), MFN clause analysis, pro-rata rights, prepayment and subordination provisions, events of default, and amendment consent thresholds. Benchmarks every material term against current market standards (NVCA 2025, Carta Q1 2025, Fenwick/Cooley market data) with dual-perspective framing (founder view and investor view for every economic term). Models cap table dilution from interest accrual and conversion across multiple scenarios. Produces confidence-scored, jurisdiction-aware analysis with COMPLIANT / FLAG / NON-COMPLIANT classification, prioritized redlines, and a Glass Box audit trail. Use when reviewing or negotiating a convertible note, convertible loan note, bridge note, or demand note convertible instrument at any stage (pre-seed through Series A bridge). Jurisdiction-agnostic base with deep tracks for US (Delaware / IRC § 409A) and UK (Companies Act 2006 / SEIS-EIS). Also triggers on: SAFE comparison, shadow preferred mechanics, qualified financing threshold, valuation cap vs. discount analysis, MFN clause triggering, pro-rata side letter, maturity extension mechanics, subordination to senior debt, 409A FMV timing, QSBS eligibility path, EIS/SEIS incompatibility, FEMA constraints on convertible instruments, convertible note overhang, and bridge-to-Series-A scenario planning.


# Legalcode Convertible Note Review

> **Disclaimer**: This skill provides a framework for AI-assisted convertible note analysis. It
> does not constitute legal, tax, securities, or financial advice. All outputs must be reviewed
> by a qualified attorney, tax advisor, and securities counsel licensed in the relevant
> jurisdiction before any reliance or action. Market benchmarks reflect general trends as of
> Q1 2025 and should be verified against current data sources before relying on them. References
> to statutes (IRC § 409A, Securities Act Reg D, ITEPA 2003, FEMA, Companies Act 2006), model
> documents (NVCA 2025, BVCA February 2025 edition), and market benchmarks carry currency risk —
> verify the latest edition before relying on them. AI-generated cap table arithmetic and dilution
> modeling require independent verification. Qualified financing thresholds, conversion mechanics,
> and maturity date risk are highly fact-specific — do not generalize beyond the specific note
> reviewed. Nothing here constitutes investment advice or an offer or solicitation to buy or sell
> securities. Convertible note terms may implicate securities law in multiple jurisdictions
> simultaneously; securities counsel review is mandatory before issuance or transfer.

---

## Purpose and Scope

This skill reviews convertible notes and convertible loan notes clause-by-clause. It benchmarks
every material term against current market standards, identifies founder-unfavorable or
investor-unfavorable deviations, models cap table impact, and generates prioritized redlines
with dual-perspective framing.

**Covers:**

- Conversion mechanics deep analysis: qualified financing definition, discount rate, valuation
  cap, shadow preferred stock, post-money formula, conversion price arithmetic
- Interest and maturity analysis: accrual method (simple vs. compound), rate benchmarking,
  maturity date risk modeling, redemption mechanics, extension provisions
- Investor protections: MFN clause mechanics, pro-rata rights, prepayment consent requirements,
  anti-dilution carve-outs, information rights
- Subordination and priority: senior debt ranking, intercreditor arrangements, pari passu
  treatment of multiple notes
- Events of default: trigger catalogue, grace periods, cure rights, acceleration mechanics,
  waiver consent requirements
- Amendment provisions: consent thresholds, individual-holder carve-outs, majority-in-interest
  mechanics
- Cap table dilution modeling: conversion scenarios, interest accrual impact, option pool
  interaction, pro-rata dilution
- Tax and regulatory flags: US IRC § 409A timing, QSBS eligibility (IRC § 1202), UK SEIS/EIS
  incompatibility, India FEMA constraints
- Market benchmarking against NVCA 2025, Carta Q1 2025, Fenwick/Cooley/Wilson Sonsini data
- Dual-perspective findings (founder view and investor view for every economic term)
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft a convertible note from scratch — see a drafting-specific skill
- Review priced equity term sheets — route to `legalcode-term-sheet-analysis`
- Select the right financing instrument (SAFE vs. note vs. ASA vs. priced round) — route to
  `legalcode-venture-financing-suite`
- Advise on securities exemption compliance (Reg D 506(b)/(c), UK s.86 FSMA) — route to
  `legalcode-private-placement-memo-review`
- Provide legal, tax, or investment advice, or replace qualified counsel

**Relationship to other skills:**

| Task                                         | Use This Skill         | Route To                                  |
| -------------------------------------------- | ---------------------- | ----------------------------------------- |
| Note clause-by-clause review + redlines      | ✅ This skill          | —                                         |
| Instrument selection (SAFE vs. ASA vs. note) | Summary flag only      | `legalcode-venture-financing-suite`       |
| Full term sheet analysis at conversion       | Hand-off on conversion | `legalcode-term-sheet-analysis`           |
| Securities exemption / PPM review            | Cross-reference flag   | `legalcode-private-placement-memo-review` |
| Equity incentive plan interaction            | Flag only              | `legalcode-equity-incentive-plan-review`  |
| Startup formation documents                  | Flag only              | `legalcode-startup-formation`             |

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at the base layer with three deep-coverage tracks:

| Track             | Legal Framework                                                                      | Key Instruments                                                                        | Tax Implications                                                                      | Securities                                                             |
| ----------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **US (Delaware)** | DGCL; IRC; Securities Act 1933; UCC Art. 9                                           | Convertible note (NVCA model); post-money SAFE (YC)                                    | IRC § 409A (FMV timing); IRC § 1202 QSBS; IRC § 483 / OID rules                       | Reg D 506(b)/(c); Form D 15-day filing; Rule 144 restricted securities |
| **UK**            | Companies Act 2006 ss.549-551 (allotment authority); ITA 2007 (EIS/SEIS); ITEPA 2003 | Convertible Loan Note (CLN); Advance Subscription Agreement (ASA)                      | SEIS/EIS incompatibility for CLNs; HMRC Advance Assurance (ASA only); EMI interaction | FSMA 2000 s.86 exemptions; FCA financial promotion rules               |
| **India**         | FEMA NDI Rules 2019; Companies Act 2013                                              | CCPS (Compulsorily Convertible Preference Shares); convertible notes (FEMA-restricted) | FEMA pricing guidelines (DCF/NAV floor); RBI approval risks                           | SEBI AIF regulations; automatic vs. FIPB route                         |

[JURISDICTION-SPECIFIC] When analyzing notes outside these three tracks, research and apply:

- Whether the jurisdiction treats convertible notes as equity or debt for regulatory purposes
- Mandatory disclosure requirements for note issuances (filing, registration, notification)
- Usury or interest-rate caps that may limit contractual interest rates
- Tax treatment of interest accrual and conversion gain/loss for both parties
- Securities law implications of conversion (new share issuance authority)
- Foreign investment restrictions on convertible instruments issued to non-residents

**US Track — Key Statutory Anchors:**

[JURISDICTION-SPECIFIC] For US-governed notes:

- **IRC § 409A**: Conversion of a note into equity may constitute a "deferral of compensation" for
  employees if structured incorrectly; the conversion price may affect FMV for option grant purposes.
  New equity grants made after a large note conversion at a deep discount may require a new 409A
  valuation before option grants. [VERIFY current IRS guidance on note-to-equity conversion events.]
- **IRC § 1202 QSBS**: Note holders who receive equity at conversion may qualify for up to 100%
  capital gains exclusion if the shares are "qualified small business stock" (§ 1202 applies;
  requires C-Corp, active business, original issue, holding period 5+ years, $50M asset test at
  issuance — OBBBA 2025 raised cap to $15M in some proposals [VERIFY]). The clock for the 5-year
  holding period starts at conversion, not at note issuance.
- **Reg D 506(b)**: Most convertible notes are issued under Rule 506(b) (no general solicitation;
  up to 35 non-accredited sophisticated investors; unlimited accredited investors; Form D 15-day
  filing required). Verify accredited investor status of each note holder.
- **Rule 144**: Convertible notes and the shares issuable on conversion are "restricted securities."
  Resale restrictions apply; typical holding period 6-12 months depending on reporting status.

**UK Track — Key Issues:**

[JURISDICTION-SPECIFIC] For UK-governed notes:

- **SEIS/EIS Incompatibility**: Convertible Loan Notes are almost always **incompatible** with
  SEIS/EIS tax relief because HMRC treats the note as giving investors the right to recover their
  original capital (a "right to be repaid" disqualification). If investors are relying on SEIS or
  EIS relief, an **Advance Subscription Agreement (ASA)** is the correct instrument, not a CLN.
  Flag this incompatibility as a NON-COMPLIANT issue whenever UK tax relief is relevant.
- **Companies Act 2006 s.549-551**: When notes convert, directors need authority to allot new
  shares. Verify the company's articles and any s.551 shareholder resolution have been obtained
  in advance (or are obtainable quickly). Insufficient allotment authority at conversion is a
  common closing risk.
- **BVCA Model Documents (February 2025)**: Updated to reflect CLN and convertible instrument
  interaction with Series A subscription agreements. Anti-dilution treatment for convertible note
  holders clarified.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming context,
the workflow pauses and asks when:

- The answer changes the direction of the analysis
- Dual-perspective framing requires knowing whose interests the reviewer serves
- Business context is needed to assess maturity date risk accurately
- Multiple existing notes interact with the note under review
- Tax relief or regulatory constraints are relevant

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

### Step 1: Accept the Convertible Note

Accept the note in any of these formats:

- **File**: PDF, DOCX, or plain text of the executed or draft note
- **Term sheet**: Convertible note term sheet (pre-execution)
- **URL**: Link to a document in a CLM, cloud storage, or document system
- **Pasted text**: Note or selected provisions pasted into the conversation

If no note is provided, prompt the user to supply one. If only a term sheet is provided (rather
than the executed note), note this distinction — term sheets lack operative legal language and
the review will be of indicative terms only, not final commitments.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask:

1. **Whose perspective?**
   - Options: **Founder/Company** (reviewing the note for fairness and risk), **Investor/Note
     Holder** (reviewing for adequacy of protections), **Both** (produce dual-perspective analysis),
     **Legal counsel** (comprehensive review for closing)
   - _Why this matters_: The entire risk classification flips. A high discount rate is a RED
     flag for founders but a GREEN item for investors.

2. **Company stage and round context:**
   - Options: **Pre-seed** (first institutional money), **Seed bridge** (between seed and Series A),
     **Series A bridge** (maturity is imminent), **Other** — describe
   - _Why this matters_: Market benchmarks vary significantly by stage. Maturity risk assessment
     depends on how far away a Series A realistically is.

3. **Investor type:**
   - Options: **Angel / individual investor**, **Micro-VC / seed fund**, **Institutional VC (lead)**,
     **Strategic investor / corporate VC**, **Multiple mixed investors**
   - _Why this matters_: Pro-rata rights, MFN scope, and covenant sophistication vary by investor type.

4. **Other notes on the cap table:**
   - Free text. Are there other outstanding convertible notes or SAFEs? If yes, do they have MFN
     clauses that could be triggered by this note's terms?
   - _Why this matters_: MFN cascade risk and cap table overhang are often the most consequential
     issues and require awareness of the full note stack.

5. **Tax relief relevance:**
   - Options: **UK SEIS/EIS relief sought by investors** (flag incompatibility), **US QSBS
     planning** (flag § 1202 implications), **Neither / unknown**, **India FEMA-regulated investor**
   - _Why this matters_: Changes the threshold for certain classifications from FLAG to
     NON-COMPLIANT.

6. **Focus areas** (optional, allow multiple selections):
   - Conversion mechanics, Interest and maturity risk, Investor protections (MFN/pro-rata),
     Events of default, Subordination, Cap table dilution modeling, Tax and regulatory flags,
     No specific focus — full review

If the user provides partial context, proceed with stated assumptions. Never silently assume
the reviewer's perspective; always state it explicitly at the start of the output.

### Step 3: Load Market Benchmarks

Before analyzing individual provisions, load the current market benchmark reference. This skill
uses these primary benchmarks (verify currency before each use):

**US Convertible Note Market Benchmarks (Q1 2025 / NVCA October 2025 update):**

| Term                          | Typical Range             | Market Median                        | Trend                                              |
| ----------------------------- | ------------------------- | ------------------------------------ | -------------------------------------------------- |
| Interest rate (simple)        | 3–8% p.a.                 | 7%                                   | Declining from 8% peak (2024 Fed rate environment) |
| Maturity date                 | 12–36 months              | 18–24 months                         | Stable                                             |
| Qualified financing threshold | $500K–$5M                 | $1–2M                                | Rising with round sizes                            |
| Discount rate                 | 15–30%                    | 20%                                  | Stable                                             |
| Valuation cap                 | Stage-dependent           | 2–4× most recent institutional round | Rising in hot markets                              |
| Amendment threshold           | >50% principal            | Majority (>50%)                      | Standard                                           |
| Prepayment                    | Investor consent required | Yes (majority consent)               | Stable                                             |

**UK Convertible Loan Note Market Benchmarks (BVCA February 2025):**

| Term                          | Typical Range | Market Median   | Notes           |
| ----------------------------- | ------------- | --------------- | --------------- |
| Interest rate                 | 4–8% p.a.     | 5–7%            | Lower than US   |
| Maturity date                 | 18–36 months  | 24 months       | Longer than US  |
| Qualified financing threshold | £500K–£3M     | £1–2M           | Stage-dependent |
| Discount rate                 | 15–25%        | 20%             | Stable          |
| Valuation cap                 | £2–10M        | Stage-dependent | Rising          |

**Pre-Seed Benchmarks (Carta Q1 2025):**

- Median convertible note raise: $500K–$1M
- Valuation caps (pre-seed): $2–5M median
- MFN clauses present: ~70% of seed notes
- Pro-rata rights negotiated: ~40% of seed notes (usually via side letter)

If benchmarks appear outdated (more than 6 months old), flag the specific data point with
[CHECK BENCHMARK CURRENCY] and advise the user to verify against a current source.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the note's governing law clause and identify the applicable jurisdiction. Then use
**legalcode-mcp** to gather legal authority for this review.

**Research targets:**

- State usury law or statutory interest rate caps for the applicable jurisdiction
- Securities exemption requirements (Reg D 506(b) Form D filing requirements; UK FSMA exemptions)
- Insolvency law treatment of convertible notes as debt (priority in liquidation)
- Tax authority on convertible note OID, IRC § 409A interaction, QSBS holding period start
- Any jurisdiction-specific mandatory disclosure requirements for convertible instruments

**If legalcode-mcp is not connected:**

- Proceed using general knowledge and web research results
- Mark all statutory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`

**⟁ CLARIFY** — If the governing law clause is absent or unexpected (e.g., a US company using
Cayman Islands law), ask the user before proceeding:

- "I cannot find a governing law clause. Which jurisdiction's law should govern the analysis?"
- "The note states [unusual governing law]. Should I analyze under that law, or flag the absence
  of a US/UK governing law choice as an issue?"

### Step 5: Conversion Mechanics Analysis

This is the highest-variance section of any convertible note. Small differences in the qualified
financing definition and conversion formula have outsized dilution impact.

#### 5.1 Qualified Financing Definition

Analyze the definition of "Qualified Financing" (or equivalent term used) against market standard:

**Elements to assess:**

- **Minimum aggregate proceeds threshold**: Is it $[X] or £[X]? Is it gross or net of expenses?
  Is it per-closing or cumulative? Compare to market median for the stage.
- **Instrument type restrictions**: Does the definition require a "priced equity round"? Or does
  it allow any financing (including another SAFE or note round)? Broad definitions that allow
  non-priced rounds may trigger conversion prematurely at an unfavorable price.
- **Timing and conditions**: Are there conditions precedent to a "Qualified Financing" beyond the
  minimum raise (e.g., board approval, investor type requirement)?
- **Exclusions**: Are SAFEs, other convertible notes, debt, government grants, or secondary sales
  explicitly excluded from the calculation? Standard practice excludes these.

**Common issues:**

- Threshold too low: Triggers conversion on a friends-and-family round at an artificially high
  or low valuation. Flag if threshold is below $500K (US) / £500K (UK) for a seed-stage company.
- Threshold too high: Company raises $1.5M Series A but threshold is $2M; notes remain
  outstanding as debt overhang. Flag any threshold materially above current target round size.
- Vague instrument-type definition: Could arguably include a SAFE-only round or debt facility,
  forcing conversion on unfavorable terms.
- No explicit exclusion of prior notes: If existing note holders also invest in the "Qualified
  Financing," does their reinvestment count toward the threshold? This can be manipulated.

#### 5.2 Conversion Price Mechanics: Discount and Cap

Analyze how the conversion price is determined when a Qualified Financing occurs:

**Discount rate analysis:**

- Confirm the note uses **simple discount** (not compound) — standard market practice
- Formula: Conversion price = Qualified Financing price per share × (1 − discount rate)
- Example: $1.00/share in Series A × (1 − 20%) = $0.80 conversion price
- Assess whether the discount applies to the price paid by new investors or the post-money price
  (they differ if there is an option pool shuffle at the Qualified Financing)

**Valuation cap analysis:**

- Formula: Conversion price = MIN(cap conversion price, discount conversion price)
- Cap conversion price = Valuation cap ÷ fully diluted pre-money share count
- Confirm "fully diluted" includes or excludes: (a) shares issuable on conversion of other notes
  and SAFEs; (b) the option pool as sized before or after the Qualified Financing; (c) warrant
  shares. These choices significantly affect the cap conversion price.
- Flag if the note is "uncapped" (discount only): Uncommon; consider a NON-COMPLIANT flag from
  the investor's perspective if the company's upside is plausible.

**Lower-of mechanic:**

- Confirm the note specifies the investor receives shares at the **lower** of the discount price
  and the cap price (i.e., more shares for the investor). This is standard.
- Flag any deviation from "lower of": e.g., notes that use only cap (no discount) or only
  discount (no cap) unless that was explicitly agreed as a concession.

**⟁ CLARIFY** — If conversion formula is ambiguous (e.g., unclear whether "pre-money" or
"post-money" valuation cap applies), present the interpretation options to the user:

- "The cap is stated as '$5M' without specifying pre-money or post-money. At a $10M post-money
  valuation, the pre-money interpretation gives [X] shares while post-money gives [Y] shares.
  Which did the parties intend?"

#### 5.3 Shadow Preferred Stock

Assess whether the note provides for **shadow preferred stock** (also called "Series A-1" or
"Note Conversion Stock") upon conversion:

**What it is**: A separate preferred share class whose liquidation preference per share equals
the actual note conversion price, not the Series A price paid by new investors.

**Why it matters**: Without shadow preferred, an investor who converts a $100K note at $0.80/share
(20% discount to $1.00/share) receives Series A shares with a $1.00/share liquidation preference —
giving them 25% more shares AND full Series A liquidation preference. Shadow preferred corrects
this windfall by pegging the liquidation preference to the actual price paid.

**Flag as:**

- COMPLIANT: Shadow preferred is specified, with liquidation preference = note conversion price
- FLAG: Note is silent on shadow preferred (may default to full Series A terms — verify)
- NON-COMPLIANT (founder perspective): Note explicitly grants full Series A liquidation preference
  to note holders (windfall at founder/new investor expense)

#### 5.4 Maturity Conversion (Non-Qualified Financing Conversion)

Assess what happens if the note reaches maturity without a Qualified Financing:

**Options to check (classify each as founder-favorable, market-standard, or investor-favorable):**

| Maturity Mechanism                                 | Classification     | Notes                                    |
| -------------------------------------------------- | ------------------ | ---------------------------------------- |
| Note becomes immediately due and payable           | Investor-favorable | Can force bankruptcy if cash unavailable |
| Automatic conversion at cap (no cash repayment)    | Founder-favorable  | Removes repayment risk                   |
| Investor option to convert or demand repayment     | Investor-favorable | Creates leverage at maturity             |
| Mandatory extension (e.g., 6-month auto-extension) | Founder-favorable  | Reduces maturity default risk            |
| Conversion at a company-board-determined valuation | Ambiguous          | Conflict of interest risk                |
| Senior investor right to set valuation at maturity | Investor-favorable | Can result in punitive dilution          |

Flag: Notes that give investors unilateral right to demand repayment at maturity without a
mandatory conversion option create existential risk for early-stage companies without cash reserves.

### Step 6: Interest and Maturity Analysis

#### 6.1 Interest Rate Assessment

Assess the stated interest rate against market benchmarks:

- **Rate level**: Compare to market median (7% simple p.a. as of Q1 2025). Flag rates above 10%
  as potentially usurious (check jurisdiction-specific limits) and rates below 3% as potentially
  below applicable AFR (check IRS Applicable Federal Rate for US notes, HMRC official rate for UK).
- **Simple vs. compound**: Confirm simple interest (standard) vs. compound interest (investor-
  favorable deviation). Flag compound interest as a FLAG item from founder perspective.
- **Day count convention**: 365/Actual is standard. 360/30 is slightly investor-favorable
  (higher effective rate); flag if used.
- **Accrual period**: Confirm interest begins accruing on the funding date, not the signing date.
  If multiple fundings occur in tranches, confirm per-tranche accrual is clear.
- **Payment timing**: Interest should accrue and be added to the conversion amount (standard) rather
  than paid in cash periodically. Cash interest payments at pre-Series A stage are unusual and
  typically founder-unfavorable.

**Impact modeling**: Calculate the total interest accrual impact at conversion:

- At median 7% simple interest on a $500K note over 24 months: $70K accrued
- Total converting amount: $570K
- Additional shares from accrued interest at $0.80 conversion price: 87,500 shares
- Dilution contribution from interest alone: [calculate based on capitalization if provided]

#### 6.2 Maturity Date Risk Assessment

**⟁ CLARIFY** — Ask if not provided:

- "When is the note's maturity date? And when does the company expect to close a Qualified
  Financing? This gap determines the maturity risk level."

Classify maturity risk as:

| Risk Level   | Criteria                                                                    |
| ------------ | --------------------------------------------------------------------------- |
| **LOW**      | Series A expected well before maturity; extension mechanics present         |
| **MEDIUM**   | Series A timing uncertain; maturity is 12–18 months away; no auto-extension |
| **HIGH**     | Maturity is within 6 months; no extension mechanism; no conversion fallback |
| **CRITICAL** | Note has already matured or matures within 90 days; no signed extension     |

For MEDIUM, HIGH, or CRITICAL: Generate a specific redline adding (or strengthening) extension
mechanics — e.g., automatic 6-month extension if no Qualified Financing has closed by maturity,
exercisable at company's election or triggered automatically.

#### 6.3 Prepayment Provisions

Assess the prepayment mechanics:

- Standard: Company may not prepay the note without consent of holders of majority of outstanding
  principal amount
- Flag as investor-unfavorable: Any prepayment right that allows the company to repay without
  investor consent at less than a pre-agreed premium (investors accepted below-market interest
  for equity upside; early cash repayment defeats this bargain)
- Flag as company-unfavorable: Prohibition on repayment even in connection with an acquisition
  (should have a carve-out for change-of-control cash repayment at a negotiated multiple,
  typically 1.0–2.0× principal + accrued interest)

### Step 7: Investor Protection Analysis

#### 7.1 MFN Clause (Most Favored Nation)

**What to assess:**

**Triggering mechanism:**

- Does the MFN apply to subsequent notes issued before the Qualified Financing? (Standard scope)
- Does it apply to SAFEs as well? (Broader scope — investor-favorable)
- Is it automatic or does the investor need to affirmatively elect? (Automatic is investor-favorable)
- Is there a materiality threshold (only triggers if terms are more than X% better)?

**Scope of terms covered:**

- Standard: Valuation cap, discount rate, interest rate
- Broader (flag as investor-favorable): All economic terms including maturity date and covenants
- Narrowest (flag as potentially inadequate): Only valuation cap

**Operational mechanics:**

- Notice requirement: Standard is that the company notifies existing MFN holders within [X]
  business days of issuing a new note
- Cure period: Does the company have a period to cure a failure to notify?
- Cap table complexity risk: Multiple MFN triggers can create a "race to the bottom" on terms
  — flag if the company has or is likely to issue multiple tranches

**Classify:**

- COMPLIANT: MFN present, standard scope (cap, discount, interest), automatic or notice-triggered
- FLAG: MFN present but scope limited (cap only) or trigger mechanism is unclear
- NON-COMPLIANT (investor perspective): No MFN when investor is not the lead/first note holder

#### 7.2 Pro-Rata Rights

**What to assess:**

- Are pro-rata rights included in the note or reserved to a side letter?
- Do they apply to the Qualified Financing itself (the conversion round) or future rounds after
  conversion?
- Standard: Pro-rata rights apply to future equity financings after the Qualified Financing
  (not to the conversion round itself)
- Is there a minimum investment threshold for pro-rata to apply (e.g., $25K+)?
- Are they assignment-assignable (pro-rata rights survive transfer of the note)?

**⟁ CLARIFY** — If pro-rata rights are absent and the investor is an institutional investor:
"Pro-rata rights are absent from the note. Institutional investors typically negotiate these via
side letter. Should I flag the absence as FLAG (common for smaller checks) or NON-COMPLIANT
(unusual for institutional investors above $100K)?"

#### 7.3 Information Rights and Covenants

Assess any affirmative or negative covenants included in the note:

**Light-touch covenants** (market standard for seed-stage):

- Quarterly financial statements
- Prompt notice of material adverse events
- Access to books and records on reasonable notice

**Restrictive covenants** (flag as FLAG or NON-COMPLIANT depending on severity):

- Headcount caps or hiring restrictions: Flag as NON-COMPLIANT (operational restriction)
- Expansion/new product restrictions: Flag as NON-COMPLIANT (operational restriction)
- Minimum cash runway requirements: Flag as FLAG (can trigger default unexpectedly)
- Approval required for contracts above $[X]: Flag as FLAG (threshold and process matter)
- Daily cash balance reporting: Flag as NON-COMPLIANT (excessive burden)

**Standard permitted covenants:**

- Negative covenant against incurring additional debt above $[threshold] without consent
- Negative covenant against asset sales above $[threshold] without consent
- Prohibition on paying dividends without consent

### Step 8: Subordination and Default Analysis

#### 8.1 Subordination Provisions

**Assess:**

- Does the note contain a subordination clause? (Standard: yes)
- Is it subordinated to "all senior indebtedness" or to specifically named senior creditors?
- Is "senior indebtedness" defined? Does it include venture debt, equipment financing, and
  bank revolving credit? Does it include trade payables? (Usually no)
- Are all convertible notes pari passu with each other? (Standard: yes, absent explicit
  waterfall among note tranches)
- Is there an intercreditor agreement referenced or required? (Flag as FLAG if senior debt
  exists and no intercreditor mechanics are specified)

**[JURISDICTION-SPECIFIC]** In the UK, convertible loan notes ranking behind secured creditors
(typically banks with charges over assets) is standard. For US notes, subordination to Silicon
Valley Bank-style venture lending facilities with a customary "standstill period" (typically 180
days post-insolvency) is market standard.

#### 8.2 Events of Default

Analyze the events of default (EoD) catalogue:

**Standard EoDs** (classify as COMPLIANT if present):

- Payment default (failure to pay principal or interest at maturity) with 5–10 business days
  cure period
- Insolvency events: voluntary or involuntary bankruptcy filing, appointment of receiver or
  liquidator, general assignment for benefit of creditors
- Material breach of note representations and covenants not cured within 30 days of notice

**Non-standard EoDs** (classify as FLAG — evaluate severity in context):

- Change of control without investor consent (can block acquisitions)
- Cross-default below $[threshold] of other debt (threshold matters — $50K is too low for a
  company with a small credit line)
- Failure to close Qualified Financing by a specified date (can be investor-favorable; creates
  pressure but also risk of forced default)
- Departure of named founders or key employees

**Acceleration mechanics:**

- Confirm that upon an EoD, the **majority of holders** (not any single holder) can declare the
  note immediately due and payable. Single-holder acceleration rights are an investor-favorable
  deviation; flag as FLAG if present.
- Confirm waiver mechanics: Holders of majority of outstanding principal can waive any EoD on
  behalf of all holders. This prevents minority holdouts from forcing insolvency.

#### 8.3 Amendment Provisions

Assess the consent thresholds for amendments and waivers:

**Standard:**

- Written consent of the company AND holders of majority of outstanding principal (>50%)
- Carve-outs requiring individual-holder consent for: shortening of maturity date; reduction in
  principal; reduction in interest rate; change to conversion price materially adverse to that
  holder; change to repayment mechanics

**Flag as FLAG (investor perspective):**

- Amendment by simple majority with no individual-holder carve-outs: Creates risk that majority
  investors can amend away minority investor protections

**Flag as FLAG (company perspective):**

- Super-majority requirement (75% or unanimous) for all amendments: Creates holdout risk; one
  small investor can block a necessary extension or amendment

### Step 9: Cap Table Dilution Modeling

Model the dilution impact of the note conversion. This step requires knowing the company's
current fully diluted capitalization; if not provided, estimate based on stage norms.

**⟁ CLARIFY** — Ask if not provided:
"To model dilution accurately, I need the company's current fully diluted cap table (common shares
outstanding, option pool size including available-for-grant, any outstanding warrants, and any
other convertible instruments). Can you provide this, or should I use stage-typical estimates?"

**Scenarios to model:**

| Scenario                                   | Conversion Price                | Dilution Note                          |
| ------------------------------------------ | ------------------------------- | -------------------------------------- |
| **A: Conversion at cap**                   | Cap ÷ fully diluted shares      | Highest dilution for founders          |
| **B: Conversion at discount**              | Series A price × (1 − discount) | Lower dilution if cap > discount price |
| **C: Maturity conversion (if applicable)** | Per note's maturity mechanic    | Varies                                 |
| **D: SAFE/Note stack conversion**          | Blended across all instruments  | Full overhang view                     |

For each scenario, calculate:

- Note principal + accrued interest at conversion date
- Shares issued to note holder = (principal + accrued interest) ÷ conversion price
- Pre-conversion vs. post-conversion founder ownership (%)
- Effective post-money valuation implied by cap or discount
- Option pool dilution interaction (if option pool refresh required at Series A)

**Flag** if: Accrued interest alone adds more than 5% to the note conversion amount over the
stated term (material interest-driven dilution risk at current interest rate).

### Step 10: Tax and Regulatory Flags

#### 10.1 US Tax Flags

**IRC § 409A Interaction:**

- Note conversion to equity does not itself typically trigger § 409A issues for investors
- However, if option grants are made to employees soon after a note conversion at a deep discount,
  the implied company valuation from the conversion price may require a fresh 409A valuation
  before grants are made to avoid the 20% penalty tax [VERIFY: seek qualified 409A counsel]
- Flag: Notes with very low conversion prices (implying low company valuation) near the time of
  anticipated option grants

**IRC § 1202 QSBS Eligibility Path:**

- If the company is a C-Corp and otherwise QSBS-eligible, note holders who receive shares at
  conversion start their **5-year QSBS holding period from the conversion date** (not note
  issuance date)
- The $50M gross assets test must be satisfied at the time of conversion, not note issuance
  [VERIFY § 1202 current asset limit; OBBBA 2025 proposals in flux]
- Flag: Any provision allowing note-to-note conversion (rolling the note forward) rather than
  equity conversion — this resets QSBS holding period and may forfeit tax benefits

**OID Rules (IRC §§ 1272-1275):**

- If the note is issued with "original issue discount" (OID) — i.e., the conversion price is
  below the face amount of the note — IRC § 483 or OID rules may require the investor to
  recognize phantom income annually. This is uncommon in standard convertible notes but can
  arise in highly discounted structures. [VERIFY with qualified tax counsel if discount > 25%]

#### 10.2 UK Tax Flags

[JURISDICTION-SPECIFIC]

- **SEIS/EIS Incompatibility**: As noted in the Jurisdiction section, CLNs disqualify investors
  from SEIS/EIS relief. If any investor has mentioned SEIS/EIS expectations, this is a
  NON-COMPLIANT flag that should be presented at the top of the review summary.
- **HMRC Advance Assurance**: If switching from CLN to ASA, note that HMRC Advance Assurance
  must be obtained before issuing the ASA (not retrospectively). The ASA must have a longstop
  conversion date no more than 6 months from investment.
- **Stamp Duty**: Transfer of notes may attract UK stamp duty (0.5%). Verify with UK tax adviser.

#### 10.3 India FEMA Flags

[JURISDICTION-SPECIFIC]

- Standard convertible notes (pure debt with repayment right) are **generally not permitted**
  under FEMA for foreign investment in Indian companies. The standard instrument for convertible
  foreign investment is **CCPS (Compulsorily Convertible Preference Shares)** which must convert
  within a set period and cannot give investors an "assured return."
- Any note that guarantees a fixed return (interest) and includes a repayment right may breach
  FEMA's pricing guidelines for foreign investment. Flag as NON-COMPLIANT if the investor is a
  non-resident and the company is an Indian entity.
- FEMA-compliant structuring requires DCF-based pricing floor for conversion; advise FEMA-
  qualified counsel review before issuance. [VERIFY: current RBI circulars on ECB regulations]

### Step 11: Classify All Findings

After completing Steps 5–10, classify each finding using the three-tier system below. For dual-
perspective analysis, assign a separate classification for founder and investor perspective.

**Single-perspective classification (when user specified one side):**

| Class             | Definition                                                                                                                             | Action                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **COMPLIANT**     | Meets or exceeds market standard for the stated stage and jurisdiction                                                                 | Note for record; no redline needed                                                                         |
| **FLAG**          | Below market standard or unusual; represents a negotiation opportunity; not an absolute deal-breaker                                   | Generate redline with rationale and fallback; estimate dilution or risk impact                             |
| **NON-COMPLIANT** | Materially founder-unfavorable (or investor-unfavorable); legal risk; creates existential risk at maturity; or violates applicable law | Explain specific risk with legal basis; provide market-standard alternative language; recommend escalation |

**Dual-perspective classification (when user requested both sides):**

| Finding                           | Founder View          | Investor View         | Market Standard Assessment                                    |
| --------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------- |
| Discount > 25%                    | FLAG or NON-COMPLIANT | COMPLIANT             | Above market median (20%); flag to founder                    |
| No valuation cap                  | NON-COMPLIANT         | FLAG                  | Uncapped notes uncommon; investor risk if high-growth company |
| Interest > 8%                     | FLAG                  | COMPLIANT             | Above current market; founder should push back                |
| Maturity < 18 months              | FLAG                  | COMPLIANT             | Below market; founder risk                                    |
| No MFN clause                     | COMPLIANT             | FLAG or NON-COMPLIANT | Flag to investor if not lead                                  |
| Compound interest                 | NON-COMPLIANT         | COMPLIANT             | Non-standard; founder should reject                           |
| No shadow preferred               | COMPLIANT             | FLAG                  | Windfall risk to new investors; flag                          |
| Full-ratchet anti-dilution        | NON-COMPLIANT         | COMPLIANT             | Extremely rare; founder should reject                         |
| Restrictive operational covenants | NON-COMPLIANT         | FLAG                  | Non-standard; founder should reject                           |
| Uncapped note (discount only)     | FLAG                  | NON-COMPLIANT         | Unusual if company has high growth trajectory                 |

### Step 12: Generate Redlines

For each FLAG and NON-COMPLIANT finding, generate a redline using this format:

```
**Clause**: [Section reference and clause name]
**Current language**: "[Exact or paraphrased language from the note]"
**Issue**: [One sentence stating the specific risk or deviation]
**Market standard**: [What market standard looks like for this stage]
**Proposed redline**: "[Specific alternative language]"
**Rationale**: [1–2 sentences suitable for sending to counterparty]
**Fallback**: [Alternative position if primary redline is rejected]
**Priority**: Tier 1 / Tier 2 / Tier 3 (see Prioritization Framework below)
**Founder view**: [COMPLIANT / FLAG / NON-COMPLIANT]
**Investor view**: [COMPLIANT / FLAG / NON-COMPLIANT]
**Confidence**: [Definite / High / Probable / Possible]
```

**⟁ CLARIFY** — If the review identifies more than 8 FLAG/NON-COMPLIANT items, ask:
"I found [N] items worth addressing. Do you want redlines for all of them, or should I focus
on the top [5–6] most material items? Too many redlines can slow a negotiation."

### Step 13: Quality Verification

Before delivering the analysis, run the quality checks in the **Quality Assurance Framework**
section:

1. Run all 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every NON-COMPLIANT item, run the 3-pass Self-Interrogation. Revise if any pass fails.
3. Apply Confidence Scoring to every material finding. No finding should be delivered without
   a confidence level.
4. Verify the cap table dilution arithmetic independently.
5. Verify that all tax and regulatory flags are marked [VERIFY] unless confirmed via legalcode-mcp.

### Step 14: Deliver Output

Produce the structured output using the **Output Format Template** below. Append the Glass Box
audit trail at the end.

---

## Deep Topic Analysis Reference

### A. Conversion Mechanics Deep Dive

The conversion of a convertible note into equity is the economic heart of the instrument. The
following issues are the most commonly negotiated and most commonly misunderstood:

**The "lower of" formula explained:**
If a note has both a valuation cap and a discount, the investor converts at whichever price is
lower (i.e., whichever gives more shares). This is almost always stated in the note but may be
buried in a definition or formula.

**Common formula errors to watch for:**

- Cap denominator: "Fully diluted capitalization" should be specified as immediately prior to
  the Qualified Financing, before the Series A option pool is created. Post-option-pool-shuffle
  fully diluted share counts inflate the denominator and reduce the cap benefit to note holders.
- Pre-money vs. post-money cap: A $5M "post-money cap" is materially less protective than a
  $5M "pre-money cap" when the Qualified Financing is $2M+. Always confirm which is intended.
- Interest inclusion: Confirm that accrued interest is included in the conversion principal.
  A note that converts only principal (not interest) at the discount or cap price and pays
  interest in cash at conversion is unusual and potentially adverse.

**Shadow preferred — worked example:**

- New Series A investors pay $1.00/share for 1,000,000 Series A Preferred shares
- Series A Preferred has $1.00/share liquidation preference
- Note holder converts at $0.80/share (20% discount), receiving 125,000 shares
  - WITHOUT shadow preferred: 125,000 Series A Preferred with $1.00/share liquidation preference
    = $125,000 effective liquidation preference (25% windfall above amount invested)
  - WITH shadow preferred: 125,000 "Shadow Preferred" shares with $0.80/share liquidation
    preference = $100,000 effective liquidation preference (matching amount invested)
- Shadow preferred eliminates the windfall and is standard practice for notes with significant
  discounts or caps where the conversion price materially differs from the Series A price.

### B. Interest and Maturity Risk

**Simple interest calculation:**
Interest = Principal × Rate × (Days ÷ 365)

For a $500K note at 7% simple interest over 24 months:

- Accrued interest = $500,000 × 7% × 2 = $70,000
- Total conversion amount = $570,000
- At $0.80/share: 712,500 total shares (87,500 attributable to interest accrual)

**Maturity date management best practices:**

- Standard maturity: 18–24 months, aligned with typical Series A timeline
- Automatic extension: Company should negotiate an automatic 6-month extension right (at company
  election or automatic upon no-fault failure to close)
- Maturity conversion at cap: If no Qualified Financing has occurred, the cleanest founder-
  protective mechanic is automatic conversion at the valuation cap (removes debt overhang;
  prevents forced repayment)
- Investor protective approach: Investor option to convert or demand repayment at maturity
  (balanced if paired with a reasonable cap-conversion default)

### C. MFN Mechanics

**How MFN triggers in practice:**

Wave 1 note: Investor A — $200K, $5M cap, 20% discount
Wave 2 note: Investor B — $150K, $4M cap, 25% discount

If Investor A has an MFN clause covering cap and discount:

- Investor A's cap automatically adjusts to $4M
- Investor A's discount automatically adjusts to 25%
- Investor A's effective economics improve retroactively

**Operational complexity with multiple MFN holders:**
If notes are issued in multiple tranches with MFN clauses, each new (better) term set triggers
all prior MFN holders. This can be costly for founders and administratively burdensome. Flag if
the company is issuing to multiple investors in tranches over time without a fixed note round
close — this is a classic MFN cascade risk.

### D. Events of Default — Practical Analysis

**Most dangerous EoDs for early-stage companies:**

1. **Cross-default clause**: If the company defaults on $50K of equipment financing, the
   convertible note accelerates. This threshold is often too low for pre-Series A companies.
   Flag any cross-default threshold below $100K as a FLAG.

2. **Material adverse change (MAC) trigger**: If the note includes a MAC EoD, analyze what
   constitutes a MAC. Broad MAC definitions (including market conditions or competitive changes)
   are investor-favorable and should be narrowed to operational/financial metrics only.

3. **Key person departure as EoD**: If the note treats departure of a named founder as an EoD,
   this creates outsized leverage for the investor and is typically non-market for seed-stage
   notes. Flag as FLAG.

---

## Deviation Severity Classification

### COMPLIANT — Meets Market Standard

The provision is within the range of what market participants routinely accept at this stage.
No redline needed. Note for the record.

**Examples:**

- 20% discount rate on a seed bridge note
- 7% simple interest, accruing to conversion
- Majority-in-interest (>50%) amendment and waiver threshold
- Light-touch covenants (quarterly reporting, notice of material events)

### FLAG — Below Market Standard / Negotiation Opportunity

The provision deviates from what market participants would typically accept, creates meaningful
dilution risk, or is unusual enough to warrant attention. Negotiate.

**Examples:**

- Discount above 25% (above market median; founder-unfavorable)
- Interest accruing as compound rather than simple interest
- No MFN clause when investor is not the sole note holder
- Qualified financing threshold above $3M (may prevent conversion on realistic raise sizes)
- No extension mechanism at maturity
- Individual-holder (not majority) acceleration right on EoD

### NON-COMPLIANT — Material Risk / Must Address

The provision creates existential company risk, material legal exposure, inappropriate windfall,
or violates applicable law. Escalate and resolve before signing.

**Examples:**

- Note is a CLN and investor is relying on UK SEIS/EIS relief (incompatible instrument)
- Convertible note issued by an Indian entity to a foreign investor (likely FEMA violation)
- No qualified financing conversion mechanic at all (pure demand note with equity option)
- Full-ratchet anti-dilution on conversion price adjustment
- Operational covenants restricting hiring, product development, or new contracts
- Maturity date has passed with no extension or conversion (immediate legal risk)
- Compound interest without cap on accrual (can result in principal-doubling effect)

---

## Prioritization Framework

### Tier 1 — Must Resolve Before Signing

Issues that create legal exposure, violate applicable law, create existential cash risk at
maturity, or result in a materially unfair economic outcome that will damage the relationship.

**Typical Tier 1 items for convertible notes:**

- SEIS/EIS incompatibility (UK notes where tax relief is expected)
- FEMA compliance issues (India-related foreign investment)
- Missing qualified financing definition or conversion mechanics
- Maturity date in the past or within 90 days with no extension
- Compound interest without cap on accrual
- Restrictive operational covenants (hiring/product restrictions)

### Tier 2 — Important / Negotiate Before Signing

Issues that have material dilution impact, create meaningful risk, or represent below-market
terms. Worth negotiating; may concede strategically.

**Typical Tier 2 items:**

- Discount rate above 25% or below 15% (depending on perspective)
- Missing valuation cap (from investor perspective) or unduly low cap (from founder perspective)
- No MFN clause for institutional investor
- No shadow preferred mechanics
- No maturity extension mechanism
- Interest above 8% or compound interest

### Tier 3 — Advisory / Concession Candidates

Issues that are sub-optimal but not deal-breaking. Can be accepted as concessions in exchange
for Tier 1 and Tier 2 wins.

**Typical Tier 3 items:**

- Pro-rata rights absent (smaller checks)
- Information rights lighter than preferred
- Prepayment consent threshold set at 66% rather than 50%
- Minor definitional ambiguities in qualified financing definition

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivery.

| Gate           | Rule                                                                                                                                                                                   | Fail Action                                                                     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Source**     | Every benchmark claim cites a specific, dated data source (NVCA, Carta, BVCA, Fenwick, or jurisdiction-specific authority)                                                             | Add citation or mark "[BENCHMARK UNVERIFIED — verify before relying]"           |
| **Format**     | All benchmarks and legal references use consistent citation format                                                                                                                     | Fix format                                                                      |
| **Currency**   | Every cited market benchmark confirmed not more than 6 months old; statutory references checked for amendment or repeal                                                                | Flag "[CHECK BENCHMARK CURRENCY]" or "[CHECK CURRENCY — may have been amended]" |
| **Domain**     | Analysis stays within convertible note territory. No priced-equity term sheet mechanics applied to note mechanics. No SAFE mechanics applied to note mechanics unless explicitly noted | Remove or flag instrument-type bleed                                            |
| **Confidence** | Uncertainty about market practice or legal requirements explicitly stated, not hidden. All NON-COMPLIANT classifications supported by specific authority or clear market consensus     | Add confidence qualifier or reduce classification to FLAG                       |

### Self-Interrogation for NON-COMPLIANT Findings

For every NON-COMPLIANT finding, apply this 3-pass review:

**Pass 1 — Market Integrity**: Does the NON-COMPLIANT classification follow logically from
market data? Would a well-advised counterparty at this stage and geography routinely accept
(or reject) this term? Is the market benchmark cited current and directly applicable?

**Pass 2 — Completeness**: Have all relevant dimensions been considered? Is the issue truly
as severe as classified, or does another provision in the note mitigate it? Are there
compensating terms (e.g., a low interest rate compensating for a higher discount)?

**Pass 3 — Challenge**: What is the strongest argument that this provision is actually acceptable?
Under what circumstances (deal type, investor type, stage, jurisdiction) might a reasonable
practitioner accept it without flagging? Is the NON-COMPLIANT classification proportionate
to the actual risk?

### Confidence Scoring

| Level        | Range     | Meaning                                                                              | Action                                                |
| ------------ | --------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear market consensus; settled practice; >95% of notes include/exclude this term    | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong market practice; minor stage/geography variation; 80–95% prevalence           | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Market practice leans this way but reasonable notes deviate; 60–79% prevalence       | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely contested; competing market practices exist                                | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Speculative; limited data; primarily one jurisdiction's practice stated as universal | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every completed review must include this audit trail as the final section of the output:

```yaml
glass_box:
  skill: "legalcode-convertible-note-review"
  note_identifier: "[Company name] Convertible Note [date or series identifier]"
  note_type: "[Convertible Note / Convertible Loan Note / Bridge Note / Demand Note]"
  review_perspective: "[Founder / Investor / Both / Legal Counsel]"
  governing_law: "[Jurisdiction]"
  date_of_review: "[YYYY-MM-DD]"

  context:
    company_stage: "[Pre-seed / Seed bridge / Series A bridge / Other]"
    investor_type: "[Angel / Micro-VC / Institutional VC / Strategic / Mixed]"
    principal_amount: "[Amount]"
    interest_rate: "[Rate and type (simple/compound)]"
    maturity_date: "[Date]"
    discount_rate: "[%]"
    valuation_cap: "[Amount or 'Uncapped']"
    other_notes_on_cap_table: "[Yes — describe / No / Unknown]"
    tax_relief_relevance: "[UK SEIS/EIS / US QSBS / India FEMA / None / Unknown]"

  benchmarks_used:
    - "NVCA Model Convertible Note — October 2025 update"
    - "Carta State of Pre-Seed Q1 2025"
    - "BVCA Model Documents — February 2025 (for UK track)"
    - "[Any other benchmarks cited]"

  legal_research:
    legalcode_mcp: "[Connected / Not connected]"
    authority_reference_file: "[/tmp/path or 'Not created']"
    statutes_consulted:
      - "[Statute — VERIFIED (legalcode-mcp) / UNVERIFIED]"
    tax_flags_verified: "[Yes (counsel consulted) / No — marked [VERIFY]]"

  analysis_scope:
    sections_reviewed:
      - conversion_mechanics: "[Reviewed / Partially reviewed / Not in note]"
      - interest_and_maturity: "[Reviewed / Partially reviewed]"
      - investor_protections: "[Reviewed / Partially reviewed]"
      - events_of_default: "[Reviewed / Partially reviewed / Not in note]"
      - subordination: "[Reviewed / Partially reviewed / Not in note]"
      - amendment_provisions: "[Reviewed / Partially reviewed]"
      - cap_table_modeling: "[Modeled / Estimated (no cap table provided) / Skipped]"
      - tax_regulatory_flags: "[Reviewed / Skipped]"

  quality_assurance:
    citation_quality_gates: "[All 5 PASSED / Gate [X] flagged and corrected]"
    self_interrogation: "[All NON-COMPLIANT items reviewed / N items reviewed]"
    confidence_scoring: "[All material findings scored]"
    cap_table_arithmetic_verified: "[Yes / No — user to verify independently]"

  findings_summary:
    compliant: "[N items]"
    flag: "[N items]"
    non_compliant: "[N items]"
    tier_1_critical: "[N items — list briefly]"
    tier_2_important: "[N items]"
    tier_3_advisory: "[N items]"

  limitations:
    - "[Note reviewed in draft vs. executed form — terms may change]"
    - "[No cap table provided — dilution modeled on stage-typical estimates]"
    - "[Tax flags marked [VERIFY] — not confirmed by qualified tax counsel]"
    - "[Benchmark data reflects Q1 2025 market conditions — verify currency]"
    - "[AI-generated analysis — all findings require review by qualified legal/tax/securities counsel]"

  reviewer: "AI-assisted — requires review by qualified legal, tax, and securities counsel"
```

---

## Anti-Patterns

What NOT to do when reviewing or advising on convertible notes:

1. **Treating the qualified financing definition as boilerplate.** The definition of "Qualified
   Financing" is the most consequential provision in the note — it determines when conversion
   happens, at what price, and whether it can be manipulated. Never accept vague or non-standard
   language in this definition without analysis.

2. **Ignoring maturity date risk.** Notes that mature before a Qualified Financing become
   immediately due and payable, potentially forcing an early-stage company into insolvency. Always
   assess the timeline realistically and flag MEDIUM or higher risk explicitly.

3. **Applying SAFE post-money mechanics to convertible notes.** SAFEs and notes use fundamentally
   different conversion price calculations (SAFEs use the fully diluted post-money cap table
   denominator; notes typically use the pre-money pre-option-pool denominator). Conflating these
   produces materially wrong dilution calculations.

4. **Ignoring accrued interest in dilution modeling.** Accrued interest converts to shares just
   like principal. On a $500K note at 7% simple interest over 24 months, $70K of additional
   conversion principal accrues — materially increasing dilution. Never model conversion without
   including accrued interest.

5. **Accepting "uncapped" notes from an investor's perspective without analysis.** An uncapped
   note with only a discount provides the investor with no floor on the conversion price if
   the company grows rapidly — the 20% discount on a $100M Series A valuation is minimal
   compared to a $5M cap. Always flag the absence of a cap for investor-perspective reviews.

6. **Missing the shadow preferred issue.** Notes with significant discounts or low caps often
   create a liquidation preference windfall if shadow preferred is not specified. The windfall
   affects both new investors (who are diluted) and founders (who bear the excess liquidation
   preference). Flag the absence of shadow preferred mechanics whenever the conversion discount
   exceeds 15%.

7. **Misclassifying compound interest as acceptable.** Compound interest on a convertible note
   is non-standard, significantly increases the conversion amount, and is almost universally
   flagged by experienced counsel. Compound interest at 7% over 24 months adds approximately
   14.5% more to the conversion principal than simple interest — not immaterial.

8. **Overlooking MFN cascade risk.** If the company is issuing notes in multiple tranches or
   waves and each note has an MFN clause, later (better) terms trigger all prior MFN holders.
   This can make fundraising negotiations extremely complicated and costly. Flag the overhang
   risk whenever multiple-tranche issuance is indicated.

9. **Treating "majority of holders" and "majority of principal" as equivalent.** A company
   with one large note holder ($1M) and five small note holders ($50K each) may find that
   the single large holder controls all majority-of-principal decisions. "Majority of holders
   by count" and "majority of principal by value" produce dramatically different governance
   outcomes. Always identify which metric the note uses.

10. **Failing to identify SEIS/EIS incompatibility early for UK investors.** This is often
    the single most valuable finding in a UK convertible note review. If the investor is relying
    on SEIS or EIS relief and the instrument is a CLN (not an ASA), the tax relief is lost.
    This should be surfaced at the very start of the review — not buried in Section 10.

11. **Applying US benchmarks to UK convertible loan notes.** UK CLN terms, market norms,
    maturity dates, and qualification thresholds differ from US norms. UK notes also interact
    with BVCA model documents at Series A in ways that US notes do not. Always apply the correct
    jurisdiction's benchmarks.

12. **Ignoring the interaction between the note and the option pool at the Qualified Financing.**
    At Series A, investors typically require an option pool to be created or expanded before
    the pre-money valuation is set (the "option pool shuffle"). This can materially dilute the
    conversion price for note holders if the cap is expressed as pre-money pre-shuffle. Model
    both scenarios.

13. **Accepting operational covenants without analysis.** Covenants restricting hiring, product
    development, entering new markets, or incurring any debt create severe operational constraints
    on early-stage companies. These are non-market at seed stage and should always be flagged as
    NON-COMPLIANT from a founder's perspective.

14. **Treating single-holder acceleration rights as a minor drafting point.** An EoD acceleration
    right exercisable by any single holder (regardless of principal amount) is a significant
    threat to company stability. A $25K investor could, theoretically, declare a technical default
    and demand immediate repayment. Always confirm that acceleration requires majority-of-principal
    consent.

15. **Forgetting the FEMA constraint for India-related structures.** Standard convertible notes
    (debt with repayment right) are not a permissible foreign investment instrument for Indian
    companies under FEMA. Issuing what looks like a standard convertible note to foreign investors
    in an Indian entity is a significant FEMA compliance risk. Always flag this as NON-COMPLIANT
    and route to FEMA-qualified counsel.

16. **Relying on stale market benchmarks.** The convertible note market is sensitive to macroeconomic
    conditions (interest rate environment, venture funding climate). Benchmarks from 2023 differ
    materially from Q1 2025 benchmarks. Always state the benchmark date and flag if the note
    appears to use terms from a different market environment.

17. **Skipping the cap table dilution model because the cap table wasn't provided.** If the user
    cannot or does not provide cap table data, use stage-typical estimates and clearly label the
    model as estimated. Even an approximate dilution model is far more useful than no model at all.

---

## Writing Standards

Before delivering the analysis, apply these writing standards:

1. **State the reviewer's perspective explicitly in the opening line.** Never let the user
   guess whose interests are being served. "This review is from the founder's perspective." or
   "This is a dual-perspective review."

2. **Lead with material issues.** Place Tier 1 NON-COMPLIANT items in the Executive Summary,
   not buried in Section 9. If SEIS/EIS incompatibility is present, it appears first.

3. **Quantify dilution impact wherever possible.** "This discount rate results in [X] additional
   shares vs. market standard" is more useful than "the discount rate is above market."

4. **Distinguish findings by jurisdiction.** Never state a US market standard as applicable
   to a UK-governed note or vice versa.

5. **Mark all unverified legal citations with [VERIFY].** Do not state tax code provisions,
   statutory thresholds, or regulatory requirements as verified facts unless confirmed via
   legalcode-mcp or cited to a primary source.

6. **Use precise language for conversion mechanics.** "Lowest price" (more shares) is
   investor-favorable; "highest price" (fewer shares) is founder-favorable. Always specify
   direction.

7. **Do not conflate SAFE and note mechanics.** If the user has submitted a SAFE for review
   under this skill, flag the instrument type mismatch and note that SAFE mechanics differ
   in material ways. Route to the appropriate SAFE analysis workflow.

8. **End every redline with a fallback position.** A redline without a fallback leaves the
   reviewer with no room to negotiate. Every YELLOW and RED redline must include an alternative
   the reviewer could accept if the primary redline is rejected.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

Use legalcode-mcp in Step 4 to:

- Verify current Applicable Federal Rate (AFR) for US notes (relevant to minimum interest
  rate requirements; notes below AFR may have OID or imputed interest implications)
- Verify current FEMA guidelines on ECB (External Commercial Borrowings) for India-related
  structures
- Verify SEIS/EIS incompatibility guidance (HMRC VCM12025 and VCM33025)
- Check any recent changes to Reg D 506(b) accredited investor definition
- Verify current IRC § 1202 QSBS asset limit (potential OBBBA 2025 changes in flux)

Save research results to `/tmp/legalcode-convertible-note-authority.md` for reference throughout
the review. Structure it as:

```markdown
# Legal Authority — Convertible Note Review

## Date Gathered: [YYYY-MM-DD]

## Governing Law: [Jurisdiction]

### Key Statutes and Regulatory Provisions

- [Statute, section, current version, relevance]

### Tax Authority

- [IRC section or HMRC guidance, current version, relevance]

### Recent Developments

- [Any recent amendments or proposed changes affecting convertible notes]
```

Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**

- Proceed with research-based general knowledge
- Mark all statutory and tax code references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed with market benchmarking and structural analysis, flagging legal authority uncertainty

---

## Output Format Template

Use this template for the final deliverable:

---

```markdown
# Convertible Note Review — [Company Name] [Note Date/Series]

> **Review Perspective**: [Founder / Investor / Both / Legal Counsel]
> **Instrument**: [Convertible Note / Convertible Loan Note / Bridge Note]
> **Governing Law**: [Jurisdiction]
> **Date of Review**: [YYYY-MM-DD]

---

## ⚠️ Priority Alerts

[List any Tier 1 NON-COMPLIANT items here at the top — e.g., SEIS/EIS incompatibility, FEMA
violation, maturity date in the past. If none, write "No Tier 1 Critical issues identified."]

---

## Executive Summary

| Item                          | Value                            | Assessment                                                        |
| ----------------------------- | -------------------------------- | ----------------------------------------------------------------- |
| Principal                     | $[X]                             | —                                                                 |
| Interest rate                 | [X]% ([simple/compound])         | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| Maturity date                 | [Date]                           | [LOW / MEDIUM / HIGH / CRITICAL] risk                             |
| Discount rate                 | [X]%                             | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| Valuation cap                 | $[X] or Uncapped                 | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| Qualified financing threshold | $[X]                             | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| MFN clause                    | [Present / Absent / Partial]     | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| Pro-rata rights               | [Present / Absent / Side letter] | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| Shadow preferred              | [Specified / Not specified]      | [COMPLIANT / FLAG / NON-COMPLIANT]                                |
| Overall assessment            | —                                | [COMPLIANT (N FLAG)] / [FLAG (N NON-COMPLIANT)] / [NON-COMPLIANT] |

**Top 3 Issues:**

1. [Highest priority issue — one sentence]
2. [Second priority — one sentence]
3. [Third priority — one sentence]

---

## Section 1: Conversion Mechanics Analysis

### 1.1 Qualified Financing Definition — [COMPLIANT / FLAG / NON-COMPLIANT]

**Current language**: "[Relevant language from note]"
**Analysis**: [Assessment of threshold, instrument type restrictions, exclusions]
**Market benchmark**: [Relevant benchmark with source]
**Issues** (if any): [Specific risk]
**Proposed redline**: "[Alternative language]"
**Rationale**: [1–2 sentences]
**Fallback**: [Alternative]
**Priority**: [Tier 1 / 2 / 3]
**Confidence**: [Level]

### 1.2 Discount Rate — [COMPLIANT / FLAG / NON-COMPLIANT]

[Same format]

### 1.3 Valuation Cap — [COMPLIANT / FLAG / NON-COMPLIANT]

[Same format]

### 1.4 Shadow Preferred Stock — [COMPLIANT / FLAG / NON-COMPLIANT]

[Same format]

### 1.5 Maturity / Non-Qualified Financing Conversion — [COMPLIANT / FLAG / NON-COMPLIANT]

[Same format]

---

## Section 2: Interest and Maturity Analysis

### 2.1 Interest Rate and Accrual Method — [COMPLIANT / FLAG / NON-COMPLIANT]

[Same format]

### 2.2 Maturity Date Risk Assessment — [LOW / MEDIUM / HIGH / CRITICAL]

**Maturity date**: [Date]
**Expected Qualified Financing**: [Date or "Unknown"]
**Risk level**: [Assessment with rationale]
**Extension mechanism**: [Present / Absent / Inadequate]
**Recommended action**: [Specific steps]

### 2.3 Interest Accrual Impact Modeling

| Scenario                   | Principal | Accrued Interest | Total Converts | Conversion Price | Shares Issued |
| -------------------------- | --------- | ---------------- | -------------- | ---------------- | ------------- |
| Cap path (Scenario A)      | $[X]      | $[X]             | $[X]           | $[X]             | [N]           |
| Discount path (Scenario B) | $[X]      | $[X]             | $[X]           | $[X]             | [N]           |

---

## Section 3: Investor Protections

### 3.1 MFN Clause — [COMPLIANT / FLAG / NON-COMPLIANT]

[Analysis and redline if needed]

### 3.2 Pro-Rata Rights — [COMPLIANT / FLAG / NON-COMPLIANT]

[Analysis and redline if needed]

### 3.3 Prepayment Provisions — [COMPLIANT / FLAG / NON-COMPLIANT]

[Analysis and redline if needed]

---

## Section 4: Subordination and Default Analysis

### 4.1 Subordination Ranking — [COMPLIANT / FLAG / NON-COMPLIANT]

[Analysis]

### 4.2 Events of Default — [COMPLIANT / FLAG / NON-COMPLIANT]

[Catalogue of EoDs with individual assessment of each]

### 4.3 Amendment and Waiver Consent — [COMPLIANT / FLAG / NON-COMPLIANT]

[Analysis of consent thresholds and individual-holder carve-outs]

---

## Section 5: Cap Table Dilution Model

**Assumptions**: [State any assumptions about cap table if not provided]

| Scenario                         | Conversion Price | Shares to Note Holder | Founder Ownership Before | Founder Ownership After |
| -------------------------------- | ---------------- | --------------------- | ------------------------ | ----------------------- |
| Scenario A (cap path)            | $[X]             | [N]                   | [X]%                     | [X]%                    |
| Scenario B (discount path)       | $[X]             | [N]                   | [X]%                     | [X]%                    |
| Scenario C (maturity conversion) | $[X]             | [N]                   | [X]%                     | [X]%                    |

[Note: All dilution calculations require independent verification by legal/financial counsel.]

---

## Section 6: Tax and Regulatory Flags

### 6.1 US Tax Flags [VERIFY — not confirmed by qualified tax counsel]

[IRC § 409A interaction, QSBS eligibility path, OID issues]

### 6.2 UK Tax Flags [VERIFY — not confirmed by qualified tax/HMRC adviser]

[SEIS/EIS incompatibility, stamp duty, HMRC compliance]

### 6.3 India FEMA Flags [VERIFY — not confirmed by qualified FEMA counsel]

[Only if applicable]

---

## Prioritized Redlines

### Tier 1 — Must Resolve Before Signing

[For each Tier 1 item, full redline format as defined in Step 12]

### Tier 2 — Important / Negotiate Before Signing

[For each Tier 2 item, full redline format]

### Tier 3 — Advisory

[For each Tier 3 item, abbreviated format: clause, issue, proposed language, rationale]

---

## Next Steps

1. [Specific action — e.g., "Obtain SEIS Advance Assurance before proceeding if UK tax relief
   is required"]
2. [Specific action — e.g., "Confirm cap table for dilution modeling before signing"]
3. [Specific action — e.g., "Request maturity extension mechanism be added to final form"]
4. [Specific action — e.g., "Verify current AFR rate before finalizing interest rate clause"]
5. [Any other action items]

---

## Glass Box Audit Trail

[Insert YAML audit trail here]
```

---

## Localization Notes

This skill is jurisdiction-agnostic at the base layer. Three deep-coverage tracks are built
in: US (Delaware), UK (Companies Act 2006 / SEIS-EIS), and India (FEMA).

**Creating jurisdiction-specific variants:**

1. Replace all [JURISDICTION-SPECIFIC] markers with verified local content
2. Replace [VERIFY] tags with verified statutory references (via legalcode-mcp)
3. Add jurisdiction-specific mandatory disclosure requirements
4. Update the benchmark table with local market data
5. Add jurisdiction-specific anti-patterns (e.g., state usury laws for specific US states)

**Key jurisdictional divergences to be aware of:**

| Jurisdiction  | Standard Instrument                                                      | Key Constraint                                                      | SEIS/EIS/Tax                 |
| ------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------- |
| US (Delaware) | Post-money SAFE (YC) dominant; convertible note for bridge/institutional | IRC § 409A option grant timing; QSBS holding period from conversion | QSBS from conversion date    |
| UK            | ASA for SEIS/EIS-eligible investors; CLN for non-EIS investors           | Companies Act s.549 allotment authority at conversion               | CLN disqualifies SEIS/EIS    |
| India         | CCPS (not CLN) for foreign investment                                    | FEMA NDI Rules; DCF pricing floor; no "assured return"              | FEMA approval required       |
| EU (various)  | National variants; no dominant standard model                            | EU Prospectus Regulation exemptions; national securities law        | National schemes vary        |
| Singapore     | Convertible notes with MAS compliance                                    | MAS Reg D equivalent; Singapore Companies Act                       | Singapore sections 13H/O/U/X |

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis — Mode A (created from scratch).
Research pipeline: 2-agent structural and legal research analysis (Structural Agent: pattern
extraction from legalcode-contract-review gold standard, legalcode-term-sheet-analysis, and
legalcode-venture-financing-suite; Legal Research Agent: comprehensive web research synthesizing
NVCA Model Convertible Note October 2025 update, Carta State of Pre-Seed Q1 2025, Fenwick
"Convertible Notes & SAFEs: Still Popular, But Terms Are Tightening" 2024/2025, Cooley GO
Convertible Debt Primer, Wilson Sonsini Convertible Note Term Sheet Generator, BVCA Model
Documents February 2025, British Business Bank CLN guidance, DWF Group CLN Rationale and Key
Negotiation Points 2024/2025, Orrick Shadow Preferred Stock glossary, Pillsbury Pro-Rata Rights
guide, Efficient Capital Labs Convertible Note Guide 2025, Sprintlaw UK CLN understanding guide,
Securities Act Reg D 506(b), IRC § 409A, IRC § 1202 QSBS (OBBBA 2025 proposals), FEMA NDI
Rules 2019, ITEPA 2003 / ITA 2007 SEIS/EIS incompatibility, Companies Act 2006 s.549-551).
Covers US (Delaware) and UK deep tracks, India FEMA flag track, and jurisdiction-agnostic base
with [JURISDICTION-SPECIFIC] markers. Features: 14-step workflow with 8 CLARIFY decision points;
dual-perspective framing (founder and investor view); interest accrual impact modeling with
3-scenario cap table output; qualified financing definition deep analysis; shadow preferred
mechanics; MFN cascade risk analysis; maturity risk classification (LOW/MEDIUM/HIGH/CRITICAL);
COMPLIANT/FLAG/NON-COMPLIANT severity classification; Tier 1/2/3 prioritization framework;
17 anti-patterns; 5-gate Citation Quality Gates; 3-pass Self-Interrogation; 5-level Confidence
Scoring; Glass Box YAML audit trail; Writing Standards; legalcode-mcp integration with graceful
degradation; Output Format Template.
