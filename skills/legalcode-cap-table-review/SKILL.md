---
name: legalcode-cap-table-review
description: Review, audit, and model cap tables for US startups at any stage — covering SAFE mechanics
  (post-money vs. pre-money conversion, MFN, pro-rata), convertible note conversion (discount, valuation
  cap, shadow preferred, interest accrual), option pool sizing and the option pool shuffle, anti-dilution
  adjustments (broad-based weighted average, full ratchet, narrow-based, pay-to-play, NVCA carve-outs),
  liquidation waterfall modeling (non-participating, participating, participation cap, liquidation multiples),
  and dilution scenario modeling across rounds.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review, audit, and model cap tables for US startups at any stage — covering SAFE mechanics (post-money vs. pre-money conversion, MFN, pro-rata), convertible note conversion (discount, valuation cap, shadow preferred, interest accrual), option pool sizing and the option pool shuffle, anti-dilution adjustments (broad-based weighted average, full ratchet, narrow-based, pay-to-play, NVCA carve-outs), liquidation waterfall modeling (non-participating, participating, participation cap, liquidation multiples), and dilution scenario modeling across rounds. Identifies cap table errors, missing shadow preferred mechanics, incorrect fully diluted counts, and structural red flags. Benchmarks against NVCA October 2025 model documents and current market standards. Also triggers on: SAFE overhang, option pool shuffle, anti-dilution down-round modeling, founder dilution analysis, fully diluted share count, pre-money and post-money ownership, 409A cap table implications, QSBS eligibility check, warrant overhang, shadow series mechanics, liquidation preference overhang, Series A cap table review, cap table due diligence, Carta / Pulley export review, and conversion scenario modeling ahead of a priced round, M&A, or secondary transaction.


# Legalcode Cap Table Review

> **Disclaimer**: This skill provides a framework for AI-assisted cap table analysis. It does not
> constitute legal, tax, securities, or financial advice. All outputs must be reviewed by a
> qualified attorney, tax advisor, and securities counsel licensed in the relevant jurisdiction
> before any reliance or action. Cap table arithmetic, conversion formulas, and dilution models
> are AI-generated and require independent verification — errors in cap table math can have
> material legal and economic consequences. Market benchmarks reflect Q4 2025 data and should be
> verified against current sources. References to statutes (DGCL, IRC §§ 409A/1202, Securities
> Act Reg D/Rule 701), model documents (NVCA October 2025, YC SAFE v1.1), and market data carry
> currency risk — verify the latest version before relying on them. Nothing here constitutes
> investment advice or an offer or solicitation to buy or sell securities. Cap table structures
> may implicate securities law in multiple jurisdictions simultaneously; securities counsel review
> is mandatory before any equity issuance or transfer.

---

## Purpose and Scope

This skill reviews and audits startup cap tables end-to-end. It identifies structural errors,
models conversion and exit scenarios, benchmarks terms against market standards, and flags
issues with classified severity for founders, investors, and counsel.

**Covers:**

- SAFE mechanics: post-money vs. pre-money conversion, MFN clause triggers, pro-rata rights,
  SAFE overhang analysis, and aggregate dilution modeling
- Convertible note conversion: discount rate mechanics, valuation cap mechanics, lower-of
  selection, interest accrual, and shadow preferred stock structuring
- Option pool: sizing, the option pool shuffle and its founder dilution impact, Rule 701
  compliance thresholds, and vesting schedule review
- Anti-dilution: broad-based weighted average (BBWA) formula verification, narrow-based
  weighted average, full ratchet detection, pay-to-play provisions, and NVCA carve-out
  completeness
- Liquidation waterfall: non-participating preferred, participating preferred (with and without
  cap), liquidation preference multiples, cumulative vs. non-cumulative dividends, and exit
  scenario modeling
- Dilution modeling: fully diluted share count verification, pre-money / post-money ownership
  calculations, multi-round dilution projections, and conversion scenario analysis
- Regulatory flags: 409A cap table implications, QSBS eligibility check (IRC § 1202),
  Rule 701 threshold monitoring, Reg D documentation status
- Cap table hygiene: documentation gaps, warrant overhang, SAFE-to-cap-table reconciliation,
  and pre-diligence clean-up requirements

**Does not:**

- Draft or amend equity instruments — see drafting-specific skills
- Provide a full term sheet analysis — route to `legalcode-term-sheet-analysis`
- Select the right financing instrument (SAFE vs. note vs. priced round) — route to
  `legalcode-venture-financing-suite`
- Review convertible note terms in detail — route to `legalcode-convertible-note-review`
- Perform a full M&A due diligence — route to `legalcode-ma-due-diligence-checklist`
- Advise on securities exemption compliance — route to `legalcode-private-placement-memo-review`

**Relationship to other skills:**

| Task                                            | Use This Skill | Route To                                  |
| ----------------------------------------------- | -------------- | ----------------------------------------- |
| Cap table audit + dilution modeling             | ✅ This skill  | —                                         |
| Instrument selection (SAFE vs. note vs. priced) | ❌             | `legalcode-venture-financing-suite`       |
| Term sheet clause review                        | ❌             | `legalcode-term-sheet-analysis`           |
| Convertible note clause-by-clause review        | ❌             | `legalcode-convertible-note-review`       |
| M&A diligence (including equity)                | ❌             | `legalcode-ma-due-diligence-checklist`    |
| Securities exemption (Reg D filing)             | ❌             | `legalcode-private-placement-memo-review` |

---

## Jurisdiction and Governing Law

**Primary jurisdiction: United States (Delaware C-Corporation).**

This skill is calibrated for US startups incorporated in Delaware, which is the dominant
formation choice for venture-backed companies. The legal framework draws on:

- Delaware General Corporation Law (DGCL), primarily §§ 151, 242
- Internal Revenue Code §§ 409A (option pricing), 1202 (QSBS)
- Securities Act of 1933, Regulation D (Rule 506(b)/506(c)), and Rule 701
- NVCA October 2025 model documents (CoI, SPA, IRA, VA, ROFR)
- YC Post-Money SAFE v1.1 standard form

[JURISDICTION-SPECIFIC] For non-US structures, adapt as follows:

- **UK**: Companies Act 2006; share classes defined in articles of association; EMI options
  under ITEPA 2003; SEIS/EIS structural constraints; advance subscription agreement (ASA)
  mechanics. Route to `legalcode-venture-financing-suite` for UK-specific SAFE/ASA/EMI guidance.
- **EU**: Local corporate law governs share class rights; no equivalent to US preferred stock
  in some civil law jurisdictions; convertible bonds (obligations convertibles) rather than
  SAFEs in France/Germany/Nordics.
- **Cayman Islands**: Class A / Class B ordinary shares; no preferred stock concept absent
  specific charter provisions; common holding structure for US-listed companies.
- **Singapore**: Companies Act 2006 (Singapore); MAS Regulation; specific structures for
  13H/13O/13U/13X incentive schemes.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would materially change the analysis or calculations
- Multiple valid modeling approaches exist and user preference matters
- The review purpose (financing, exit, employee offer, diligence) changes what to prioritize
- Mathematical inputs are ambiguous and the error would compound

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

### Step 1: Accept the Cap Table

Accept the cap table in any of these formats:

- **File**: CSV or Excel export from Carta, Pulley, AngelList, Eqvista, or other cap table
  software; raw spreadsheet
- **Pasted content**: Tab-separated or comma-separated cap table data
- **Verbal description**: Stakeholder listing with share counts and instrument types
- **Partial data**: Founders ask for help modeling; provide best analysis with stated assumptions

If no cap table is provided, prompt the user to supply one — or offer to create a template
structure based on stated stakeholder information.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask these questions. Present structured options
where possible:

1. **Purpose of this review:**
   - Options: Upcoming priced round (Series Seed / A / B), Exit / M&A analysis, Employee
     equity offer (confirming ownership %), Investor due diligence, QSBS eligibility check,
     409A preparation, General audit / clean-up, Other
   - _Why this matters_: Determines which sections receive the deepest analysis and which
     output format applies.

2. **Your role:**
   - Options: Founder, Lead investor, Existing preferred investor, New investor (diligence),
     Employee (confirming grant), Counsel, Other
   - _Why this matters_: Founder analysis focuses on dilution and founder economic outcomes;
     investor analysis focuses on preference mechanics and anti-dilution; employee analysis
     focuses on fully diluted ownership and exit proceeds.

3. **Stage and round history:**
   - Options: Pre-seed (no priced round), Seed preferred, Series A, Series B, Series C+, Other
   - Free text for round amounts and dates if known.
   - _Why this matters_: Determines which SAFE conversion mechanics apply, what option pool
     sizing is appropriate, and which anti-dilution provisions are likely present.

4. **Focus areas:** Any specific concerns?
   - Options: SAFE conversion math, Convertible note conversion, Founder dilution, Option
     pool / employee equity, Anti-dilution provisions, Liquidation waterfall, QSBS eligibility,
     Pre-round diligence clean-up, No specific focus — full audit
   - Allow multiple selections.
   - _Why this matters_: Focuses analysis on the user's highest-priority concerns.

If the user provides partial context, proceed with reasonable defaults and **state assumptions
explicitly** in the output.

### Step 3: Parse and Validate Cap Table Structure

Extract and organize the following information from the submitted cap table:

**3a. Share classes and series:**

- Common stock (founders, early employees)
- Each series of preferred stock (Seed, Series A, A-1 shadow, B, etc.)
- SAFEs and convertible notes (recorded as off-balance-sheet obligations)
- Stock options and restricted stock units (granted and ungranted from pool)
- Warrants (each separately with exercise price and expiration)

**3b. Key counts:**

| Count Type             | Formula                                                                                          | Notes                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| Issued and outstanding | Sum of all currently issued shares                                                               | Common + all preferred (converted basis)              |
| Fully diluted          | Issued + unissued option pool + unexercised options/warrants + SAFEs/notes on as-converted basis | The correct basis for investor ownership calculations |
| SAFE overhang          | Sum of all unconverted SAFEs on as-converted basis at each relevant scenario price               | Appears off-balance-sheet until conversion            |

**3c. Structural flags on intake:**

- Verify that issued and outstanding ≤ authorized shares (check charter authorizations)
- Flag any share class without a corresponding board resolution or executed purchase agreement
- Identify any SAFEs or notes not yet recorded in the cap table
- Check for expired or near-expiry warrants

**⟁ CLARIFY** — If share counts are ambiguous (e.g., pre- or post-split basis unclear, options
on outstanding vs. fully diluted basis unclear), ask before proceeding:

- "The option pool percentage — is this stated as a percentage of issued and outstanding or
  fully diluted shares? The difference can be significant."
- "I see [X] SAFEs in the table. Are there any additional SAFEs or convertible notes outstanding
  that are not reflected here?"

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve current legal authority for:

- DGCL § 151 (preferred stock creation and terms)
- DGCL § 242 (charter amendment requirements, class voting)
- IRC § 409A (fair market value requirements for option pricing)
- IRC § 1202 current thresholds (QSBS) — note $75M gross asset threshold under OBBBA effective
  July 4, 2025 for new issuances; $50M threshold still applies to pre-July 4, 2025 issuances
- Securities Act Rule 701 (enhanced disclosure threshold at $10M per 12-month period)
- NVCA October 2025 model documents (latest charter and anti-dilution provisions)

Save key authority to `/tmp/legalcode-cap-table-authority.md`.

**If legalcode-mcp is not connected:**
Mark all statutory references with [VERIFY] and note in the Glass Box:
`legalcode_mcp: "Not connected — all citations require manual verification"`

### Step 5: SAFE Analysis

For each outstanding SAFE, analyze the following:

**5a. Post-money vs. pre-money determination:**

| Feature               | Post-Money                                      | Pre-Money (Legacy)               |
| --------------------- | ----------------------------------------------- | -------------------------------- |
| Conversion formula    | Investment ÷ Post-Money Cap = fixed ownership % | Not fixed until conversion event |
| SAFE-to-SAFE dilution | Founders only                                   | Spreads across all prior holders |
| YC v1.1 standard      | ✅ Yes                                          | ❌ Older form — flag for review  |
| Ownership certainty   | Fixed at signing                                | Unknown until conversion         |

**Flag**: Any pre-money SAFE should be marked FLAG — it creates cross-dilution confusion and
is non-standard since 2018. Consider whether conversion to post-money form is appropriate.

**5b. Post-money SAFE conversion formula verification:**

```
Investor Ownership % = Investment Amount / Post-Money Valuation Cap

SAFE Shares (at priced round) = (SAFE % / (1 - Total SAFE %)) × Founder Shares
```

Verify that:

1. The fixed ownership percentage is correctly stated in the SAFE instrument
2. Aggregate SAFE ownership percentages sum correctly (cross-SAFE dilution)
3. Conversion triggers are defined (Qualified Financing threshold specified)
4. Conversion occurs into shadow preferred with correct original issue price

**5c. MFN clause analysis (if present):**

- Identify all SAFEs with MFN provisions
- Check whether any subsequent SAFEs were issued with more favorable terms (lower cap or
  higher discount) without notifying prior MFN holders
- Verify MFN lapse provisions (typically lapses on first priced equity round)

**Flag**: Any failure to notify an MFN holder of a subsequent SAFE with better terms is a
CRITICAL issue — it may give the MFN holder a contractual claim.

**5d. Pro-rata rights analysis:**

- Identify which SAFEs include pro-rata rights
- Calculate aggregate pro-rata exercise demand as a percentage of next round size
- Flag if aggregate pro-rata demand exceeds 30% of next round — this can block institutional
  lead investors and delay or prevent the next round

**5e. Shadow preferred mechanics:**

- Verify that each SAFE converts into a sub-series of preferred (shadow series) with an
  original issue price equal to the conversion price, not the Series A original issue price
- Absence of shadow preferred creates liquidation preference overhang — CRITICAL flag

**5f. SAFE overhang modeling:**

- Calculate total dilution from all outstanding SAFEs at each conversion scenario
- Model conversion at: (a) at the valuation cap, (b) at a Series A above the cap, (c) at
  a down-round scenario
- Compound dilution must be calculated multiplicatively, not additively

### Step 6: Convertible Note Analysis

For each outstanding convertible note, analyze:

**6a. Conversion price calculation (lower-of rule):**

```
Discount Price = Series A Price Per Share × (1 - Discount %)
Cap Price = Series A Price Per Share × (Valuation Cap / Pre-Money Valuation)
Conversion Price = min(Discount Price, Cap Price)
```

**Example verification:** $1M note, 20% discount, $8M cap, Series A at $10M pre-money with
$1.00/share:

- Discount Price: $1.00 × (1 - 0.20) = $0.80/share
- Cap Price: $1.00 × ($8M / $10M) = $0.80/share
- Applied Price: $0.80/share (tie — cap becomes relevant at higher valuations)

**6b. Interest accrual and conversion:**

```
Total Converting Amount = Principal + (Principal × Rate × Years)
Note Shares = Total Converting Amount / Conversion Price
```

Verify that: (a) interest is calculated as simple (not compound) unless the note specifies
compound; (b) accrued interest is added to principal before conversion arithmetic; (c) the
conversion date is used, not the issuance date.

**6c. Shadow preferred stock check:**
Same as SAFE analysis — each note should convert into a shadow sub-series with OIP equal to
the note conversion price. Flag absence as CRITICAL.

**6d. Maturity date and overhang:**
Flag any note within 60 days of maturity without a confirmed conversion event or extension —
maturity risk is a CRITICAL structural issue. [Cross-reference to `legalcode-convertible-note-review`
for full note clause analysis.]

### Step 7: Option Pool and Employee Equity Analysis

**7a. Option pool shuffle identification:**

The option pool shuffle occurs when investors require the pool be created or expanded on a
pre-money basis, causing only existing shareholders (not new investors) to bear pool dilution.

```
Effective Pre-Money Valuation = Stated Pre-Money Valuation - (Pool Size × PPS)
```

Where PPS = price per share implied by the stated pre-money valuation.

**Example:**

- Investor offers $8M pre-money, requires 20% post-money pool
- Shares outstanding: 6M; Pool expansion needed: 1.5M shares pre-money
- Each pool share costs: $8M / (6M + 1.5M pool) ≈ $1.07
- Effective pre-money value to founders: $8M - (1.5M × $1.07) ≈ $6.4M

**Flag as FLAG**: Any pre-money pool expansion where founders appear unaware of the effective
valuation haircut. Suggest founder model the effective valuation before accepting terms.

**7b. Option pool sizing:**

- Verify the current authorized pool as a percentage of fully diluted shares
- Benchmark: 10–20% post-money fully diluted at Series A (NVCA October 2025)
- For context, model pool size vs. planned 12-month hiring: if pool is substantially larger
  than hiring plan requires, flag the excess as unnecessary founder dilution

**7c. Rule 701 compliance:**

Rule 701 exempts compensatory equity grants. Enhanced disclosure is triggered when securities
issued in any 12-month period exceed:

- $10M aggregate [VERIFY — threshold increased from $5M in 2018 rules]

**Flag as FLAG**: Any company approaching the $10M threshold without financial disclosure
infrastructure in place.

**7d. Vesting schedule:**

- Standard: 4-year vesting, 1-year cliff, monthly thereafter (NVCA standard)
- Flag any vesting schedule shorter than 4 years for founder shares as FLAG
- Flag any accelerator vesting provisions (single trigger) without board approval as FLAG
- Double-trigger acceleration is standard (requires both change of control AND termination)

**7e. Early exercise and 83(b) elections:**

- Identify options issued to early employees before the 83(b) election window has closed
- Early exercise + 83(b) election within 30 days of option grant date enables QSBS clock-start
- Failure to advise employees of 83(b) timing: FLAG

### Step 8: Anti-Dilution Analysis

For each series of preferred stock with anti-dilution provisions:

**8a. Type classification:**

| Type                                | Investor Protection Level                       | Market Standard?                   |
| ----------------------------------- | ----------------------------------------------- | ---------------------------------- |
| Broad-based weighted average (BBWA) | Moderate                                        | ✅ NVCA standard, ~95% of US deals |
| Narrow-based weighted average       | Stronger than BBWA                              | Limited — flag if present          |
| Full ratchet                        | Maximum (investor) / Maximum dilutive (founder) | ❌ Flag — rare, aggressive         |
| None                                | No protection                                   | Requires notation                  |

**8b. BBWA formula verification:**

```
CP2 = CP1 × (A + B) / (A + C)

Where:
  CP1 = Current conversion price
  CP2 = New conversion price after adjustment
  A   = Total shares deemed outstanding before issuance (BBWA: all common + all preferred as-
        converted + all options/warrants as-exercised + full ungranted option pool)
  B   = Consideration received ÷ CP1 (hypothetical shares at old price)
  C   = Actual new shares issued
```

Verify the charter's definition of "Additional Shares of Common Stock" or equivalent to
confirm broad-based vs. narrow-based treatment. Key indicators:

- **Broad-based**: "A" includes the entire authorized and unissued option pool
- **Narrow-based**: "A" includes only issued shares of the specific protected series

**8c. Down-round modeling:**
For any recent or anticipated down round, calculate the adjusted conversion prices for each
protected preferred series and restate fully diluted share count. Show impact on each series'
as-converted common share count.

**8d. Anti-dilution carve-outs (NVCA standard):**
Verify the charter includes standard carve-outs excluding from anti-dilution triggers:

1. Shares reserved under approved equity incentive plans (option pool)
2. Shares issued as acquisition consideration approved by the board
3. Shares for strategic transactions approved by the board
4. Stock splits, dividends, and recapitalizations
5. Pro-rata rights offerings
6. Issuances waived by majority of protected preferred holders

**Flag as CRITICAL**: Missing carve-outs could mean routine option pool grants trigger
anti-dilution adjustments inadvertently.

**8e. Pay-to-play provisions:**
Identify any pay-to-play requirement. Explain that investors who do not participate pro rata
in a down round may lose anti-dilution protection or convert to common.

### Step 9: Liquidation Waterfall Analysis

For each series of preferred stock:

**9a. Structure classification:**

| Structure                      | Description                                     | Market Prevalence (2025) |
| ------------------------------ | ----------------------------------------------- | ------------------------ |
| Non-participating preferred    | Choose higher of preference OR as-converted     | ~95%+ US Series A        |
| Participating preferred (full) | Take preference AND as-converted ("double dip") | Aggressive — flag        |
| Participating with cap         | Double dip up to N× multiple, then convert      | Compromise               |

**Flag as FLAG**: Participating preferred (no cap) — aggressive structure, uncommon at US
Series A. Explain founder dilution impact explicitly.
**Flag as FLAG**: Liquidation preference above 1× — uncommon at Series A; 2× and above
should be flagged as CRITICAL unless specific risk context (bridge round, late stage).

**9b. Waterfall modeling:**

Model exit proceeds allocation across at least three scenarios:

**Scenario A — Distressed exit** (e.g., 0.5× total invested capital):

1. Senior preferred holders take preferences (in seniority order)
2. Junior preferred and common receive remainder (may receive nothing)

**Scenario B — Moderate exit** (e.g., 2×–3× total invested capital):

1. Each preferred series takes preference or converts (whichever is higher)
2. Remaining to common

**Scenario C — Strong exit** (e.g., 5×+ total invested capital):

1. All preferred converts to common (as-converted is higher than preference)
2. Common and converted preferred share proceeds pro rata

For participating preferred, recalculate each scenario with participation.

**9c. Crossover point calculation:**
For non-participating preferred, calculate the exit value at which each series converts
to common rather than taking its preference:

```
Crossover Valuation = Liquidation Preference / (Series Ownership % on as-converted basis)
```

Below crossover: take preference. Above crossover: convert to common.

**9d. Liquidation seniority:**

- Verify seniority structure (later series typically senior to earlier)
- Check for pari passu provisions between series
- Identify any series with seniority carve-outs or participation clawbacks

**9e. Cumulative vs. non-cumulative dividends:**

- Standard: 8% non-cumulative dividends, declared but rarely paid before liquidity
- Cumulative dividends compound and increase the liquidation overhang over time
- Flag as FLAG: Cumulative dividends in early-stage financing (non-standard)

### Step 10: Dilution Scenario Modeling

**10a. Pre-money / post-money ownership calculations:**

```
Price Per Share = Pre-Money Valuation / Pre-Money Fully Diluted Shares
New Shares Issued = Investment Amount / Price Per Share
Post-Money FD Shares = Pre-Money FD Shares + New Shares Issued + Pool Expansion
New Investor Ownership = New Shares / Post-Money FD Shares
Founder Ownership (post-round) = Founder Shares / Post-Money FD Shares
```

**10b. Multi-round dilution projection:**
Project ownership through at least two additional hypothetical rounds (e.g., Series A → B → C):

- Apply typical dilution per round (Series A: 20–25%; Series B: 15–20%; Series C: 10–15%)
- Show compound effect: 80% × 80% × 85% = 54.4%, not 85% - 40% = 45%
- Include option pool refreshes (typically 5–10% at each round) in dilution calculation

**10c. SAFE conversion scenarios at Series A:**

| Scenario  | Series A Pre-Money | SAFE Conversion Price            | Founder Dilution from SAFEs |
| --------- | ------------------ | -------------------------------- | --------------------------- |
| At cap    | $10M (= SAFE cap)  | Cap price                        | [calculated]                |
| Above cap | $15M               | Cap price (cap binds)            | [calculated]                |
| Below cap | $8M                | Effective price (no cap benefit) | [calculated]                |

**10d. Fully diluted share count verification:**

```
Fully Diluted = Common (founders + employees + early grants)
              + All preferred shares (on as-converted basis)
              + All outstanding options and warrants (on as-exercised basis)
              + Unissued but reserved option pool
              + All unconverted SAFEs and notes (on as-converted basis at relevant scenario price)
```

Flag any discrepancy between the cap table's stated fully diluted count and this formula.

**10e. QSBS eligibility quick check:**

| Requirement                                                                                           | Check                                                            |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| C-corporation (domestic Delaware)                                                                     | Verify entity type                                               |
| Gross assets ≤ $50M at issuance date (pre-July 4, 2025) / ≤ $75M (post-July 4, 2025) [VERIFY — OBBBA] | Check total assets per balance sheet at each round               |
| Original issuance only (not secondary)                                                                | Verify shares not purchased on secondary                         |
| 5-year holding period                                                                                 | Calculate from grant date                                        |
| Active business test: ≥ 80% qualifying trade/business                                                 | Flag if professional services, finance, hospitality, real estate |

Flag as FLAG: Any round where gross assets approach the applicable QSBS threshold — counsel
should confirm eligibility for all instruments issued before and after.

### Step 11: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates (see Quality Assurance Framework).
2. For each CRITICAL item, run the 3-pass Self-Interrogation.
3. Verify all arithmetic independently: recalculate every formula in the review.
4. Confirm all fully diluted share counts reconcile to zero (sum of parts = total).
5. State assumptions explicitly for any modeled scenario.
6. Assign a Confidence Score to each section.
7. Generate the Glass Box Audit Trail.

### Step 12: Deliver Output

Structure the output using the Output Format Template at the end of this skill.

---

## Cap Table Analysis Reference

### SAFE Mechanics Deep Reference

**Post-money SAFE conversion (YC v1.1 standard):**

The post-money SAFE locks in the investor's ownership percentage at signing:

```
Fixed Ownership % = Investment Amount / Post-Money Valuation Cap
```

This percentage is fixed regardless of subsequent SAFEs issued at the same cap —
subsequent SAFEs only dilute founders. Cross-SAFE dilution does not occur between
post-money SAFE holders at the same cap.

At conversion to a priced round, the SAFE converts into a sub-series of preferred stock.
The conversion price equals the lower of:
(a) the price per share of the new financing, or
(b) the price per share derived from the valuation cap

```
Cap Derived Price = Investment Amount / (Post-Money Cap - Investment Amount) × (Shares outstanding + Option Pool)
```

Or simplified: the SAFE holder receives shares such that their fixed percentage is
preserved on a post-conversion basis.

**Pre-money SAFE conversion:**
Under the legacy pre-money SAFE, the investor's ownership percentage is not fixed at signing.
The denominator (Company Capitalization) excludes converting SAFEs, so the final ownership
percentage depends on how many SAFEs are outstanding — it is not deterministic until conversion.
Each new pre-money SAFE dilutes all prior holders proportionally.

**MFN trigger conditions:**

1. Company issues a subsequent SAFE or convertible note with a lower valuation cap or higher
   discount rate
2. Company must promptly notify all MFN holders with full documentation of the new instrument
3. MFN holder has [typically 10–30 days] to elect to match the new terms
4. One election opportunity only; lapses at first priced equity financing round

### Convertible Note Conversion Reference

**Lower-of rule verification:**
The investor converts at the price that produces the most shares (i.e., the lowest per-share
price):

```
Applied Conversion Price = min(Discount Price, Cap Price)

Where:
  Discount Price = Next Round PPS × (1 - Discount%)
  Cap Price      = Next Round PPS × (Valuation Cap / Next Round Pre-Money)
```

If no round occurs and the note matures: the note converts at a pre-negotiated maturity
price (often the same formula applied to a deemed valuation) or is repaid as debt with the
maturity conversion option.

**Shadow preferred stock — critical mechanic:**
When a SAFE or note converts at a price below the Series A PPS, if the company issues
all converters a standard Series A preferred share (OIP = $1.00), each early investor
receives a $1.00/share liquidation preference despite paying only $0.50/share.

Solution — shadow preferred (Series A-1):

- Converters receive a sub-series (A-1) with OIP equal to their actual conversion price
- Identical rights in all other respects (liquidation seniority pari passu with Series A)
- Each investor's liquidation preference equals their actual capital invested, not the
  Series A OIP

**Absence of shadow preferred is a CRITICAL red flag** in any cap table where SAFEs or
notes convert below the new round price.

### Anti-Dilution Formula Reference

**BBWA formula (NVCA standard):**

```
CP2 = CP1 × (A + B) / (A + C)

Where:
  A = Total shares of common stock outstanding on an as-converted, as-exercised basis
      immediately before the new issuance. Under BBWA: includes all authorized/reserved
      shares in the option pool (issued AND unissued).
  B = Consideration received ÷ CP1 (shares that would have been issued at old CP)
  C = Actual shares issued in the new round
```

**Narrow-based weighted average:**
Same formula but A excludes unissued option pool shares. Stronger protection for investors,
more dilutive to founders than BBWA.

**Full ratchet:**

```
CP2 = New Issuance Price (regardless of the number of shares issued)
```

A single share issued at $0.01 in a down round resets the entire series conversion price
to $0.01. Uncommon in US venture; red flag.

**Numerical BBWA example:**

- CP1 = $2.00/share; A = 10M shares; New issuance: 2M shares at $1.00/share
- Consideration = 2M × $1.00 = $2M; B = $2M / $2.00 = 1M
- CP2 = $2.00 × (10M + 1M) / (10M + 2M) = $2.00 × 11/12 = **$1.833/share**

**Three-way comparison for the same down round:**

| Type            | Adjusted CP | Existing holder's new share count (5M shares) |
| --------------- | ----------- | --------------------------------------------- |
| BBWA            | $1.833      | 5M × ($2.00 / $1.833) = 5.45M                 |
| Narrow-based WA | ~$1.67      | ~6.0M                                         |
| Full ratchet    | $1.00       | 10.0M                                         |

### Liquidation Waterfall Reference

**Crossover point (when non-participating preferred converts):**

```
Crossover = Liquidation Preference / As-Converted Ownership %
```

Above this exit value, investors maximize returns by converting to common rather than
taking their preference.

**Participating preferred — exit math:**

1. Senior series takes preference (1× or stated multiple)
2. Then all holders (common + preferred as-converted) share remaining proceeds pro rata
3. If capped: participating preferred cannot exceed N× total return; above cap, convert
   to common

**Impact comparison for $5M Series A investment at 20% ownership:**

| Exit Value            | Non-Participating        | Participating                         |
| --------------------- | ------------------------ | ------------------------------------- |
| $10M (return of pref) | $5M                      | $7M ($5M pref + 20% × $5M)            |
| $20M                  | $5M (or $4M if converts) | $8M ($5M + $3M participation)         |
| $50M                  | $10M (converts to 20%)   | $10M (converts if cap) or $14M (full) |

---

## Finding Classification

Every issue identified receives a classification:

### PASS — No Issue

The item is correct, consistent with market standards, and presents no risk.
No action required.

### FLAG — Material Issue — Should Address

The item deviates from market standard, creates meaningful risk, or requires attention before
the next financing or transaction event.

**Examples:**

- Pre-money SAFE in use (non-standard since 2018)
- Option pool shuffle: founder appears unaware of effective valuation haircut
- Pro-rata rights exceed 30% of projected next round (potential round blockage)
- Participating preferred (without cap) at Series A
- Narrow-based (rather than broad-based) anti-dilution
- Rule 701 approaching the enhanced disclosure threshold
- Unexercised warrants not tracked in cap table
- Cap table in spreadsheet form for a company with 5+ stakeholders
- QSBS gross assets approaching threshold

**Action**: Explain the deviation, quantify the economic impact, recommend specific remediation.

### CRITICAL — Deal-Threatening Issue — Must Address

The item creates material legal risk, financial error, or potential breach of an equity
instrument or charter obligation.

**Examples:**

- Shadow preferred mechanics absent (liquidation preference overhang)
- MFN holder not notified of subsequent SAFE with better terms (potential breach of contract)
- Anti-dilution carve-outs missing from charter (routine grants trigger adjustments)
- Convertible note maturing within 60 days without confirmed conversion event
- Fully diluted share count error in the cap table
- Charter authorizations exceeded (issued shares > authorized shares)
- Anti-dilution adjustment not applied after a prior down round
- Missing board resolution or executed grant agreement for option grants
- 409A grant made below FMV (IRC § 409A excise tax risk)

**Action**: Escalate to counsel immediately. Explain the specific risk with legal basis,
quantify the exposure, and recommend the remediation path.

---

## Prioritization Framework

### Tier 1 — Must Fix Before Next Round / Transaction (Deal-Breakers)

Issues that will surface in institutional investor diligence and either block the round or
require cure as a closing condition:

- Shadow preferred mechanics absent
- Anti-dilution carve-outs missing from charter
- Convertible note maturity risk
- Charter authorization exceeded
- Cap table arithmetic error (wrong fully diluted count)
- Missing equity grant documentation (board resolutions)
- 409A option pricing below FMV

### Tier 2 — Should Fix in Current Quarter (Strong Preferences)

Issues that create risk but are fixable with counsel engagement:

- Pre-money SAFEs → convert to post-money form with investor consent
- Option pool shuffle: model and disclose to affected parties
- QSBS pre-flight check before large funding rounds
- Warrant registry clean-up
- Excel cap table migration to Carta / Pulley

### Tier 3 — Clean Up in Ordinary Course (Optimization)

Issues that improve hygiene but are not urgent:

- Pro-rata right aggregation modeling
- Option vesting schedule standardization
- 83(b) election reminder to recently granted early-exercisers
- Participation cap negotiation for future rounds

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify cap table stage, purpose, and user role. Classify complexity (early-stage
with SAFEs only vs. multi-series with multiple preferred classes). Identify which legal
provisions are engaged.

**DO**: Parse cap table structure. Analyze each instrument type systematically. Model
scenarios. Classify findings.

**CHECK**: Run Citation Quality Gates. For each CRITICAL item, run Self-Interrogation.
Verify all arithmetic (recompute totals, check formula inputs). Confirm fully diluted
count reconciles.

**ACT**: Flag any identified patterns for market standard comparison. Note if terms have
shifted from the NVCA October 2025 baseline.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                 | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, model document, or established principle                 | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent recognizable format (DGCL § 151; NVCA October 2025; YC SAFE v1.1)  | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, noting OBBBA changes effective July 4, 2025 for QSBS   | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within US law and charter mechanics unless explicitly flagged [JURISDICTION-SPECIFIC] | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. Arithmetic assumptions stated explicitly                  | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL Items

For any finding classified as CRITICAL, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the risk assessment follow logically from the cited statute, charter provision, or
  instrument term?
- Would counsel reviewing this specific charter and instrument reach the same conclusion?
- Is there a counter-argument that the issue is actually harmless?

**Pass 2 — Completeness:**

- Have all relevant provisions been considered (charter, instrument, board resolutions,
  and applicable statutory authority)?
- Are there carve-outs or exceptions that mitigate the risk?
- Have all affected instrument series been analyzed, not just the one triggering the issue?

**Pass 3 — Challenge:**

- What is the strongest argument that this classification is overcautious?
- Under what circumstances might a reasonable attorney accept this cap table structure?
- Is CRITICAL proportionate, or is this actually FLAG with counsel guidance?

If any pass reveals a weakness, revise the finding before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each section of analysis, assign a confidence level:

| Level        | Range     | Meaning                                              | Action                                                |
| ------------ | --------- | ---------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Arithmetic verified; clear charter / instrument term | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong basis; minor ambiguity in input data          | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good analysis but input data incomplete or ambiguous | State with explicit assumptions                       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations       | Flag for counsel; present both interpretations        |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                              | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every cap table review output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-cap-table-review"
  review_date: "[date]"
  company: "[company name or 'Redacted']"
  stage: "[Pre-seed / Seed / Series A / Series B / etc.]"
  review_purpose: "[Upcoming round / Exit / Diligence / Audit / etc.]"
  user_role: "[Founder / Investor / Counsel / Employee]"
  instrument_types_reviewed:
    - "[e.g., Post-money SAFEs: N]"
    - "[e.g., Convertible notes: N]"
    - "[e.g., Preferred series: N]"
    - "[e.g., Option pool: N% of FD]"
    - "[e.g., Warrants: N]"
  fully_diluted_share_count: "[number — verified or estimated]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-cap-table-authority.md or 'Not created']"
  statutes_consulted:
    - "DGCL § 151 — [VERIFIED or UNVERIFIED]"
    - "IRC § 1202 — [VERIFIED or UNVERIFIED]"
    - "IRC § 409A — [VERIFIED or UNVERIFIED]"
    - "Securities Act Rule 701 — [VERIFIED or UNVERIFIED]"
  documents_benchmarked:
    - "NVCA October 2025 model documents — [VERIFIED or UNVERIFIED]"
    - "YC Post-Money SAFE v1.1 — [VERIFIED or UNVERIFIED]"
  findings_summary:
    critical: "[number]"
    flag: "[number]"
    pass: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  arithmetic_verified: "YES / NO — [notes]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[e.g., Cap table submitted as verbal description — arithmetic subject to input accuracy]"
    - "[e.g., Charter not reviewed — anti-dilution carve-outs not verified against charter text]"
  reviewer: "AI-assisted — requires qualified legal and financial review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in cap table review:

1. **Confusing issued/outstanding with fully diluted.** Analyzing ownership on issued and
   outstanding basis misrepresents actual economic dilution. Always calculate and present
   on a fully diluted basis. The only exception is voting analysis, which uses actual
   outstanding shares.

2. **Summing dilution additively.** Applying 20% dilution in round 1 and 20% in round 2
   does not yield 40% total dilution — it yields 36% (80% × 80% = 64% retention, not 60%).
   Always compound multiplicatively.

3. **Ignoring SAFE overhang in the pre-round cap table.** Outstanding SAFEs are not shares,
   but they are real dilutive obligations. A cap table showing "founders own 80%" that omits
   SAFE conversion effects is materially misleading. Model SAFEs on an as-converted basis at
   every scenario.

4. **Accepting pre-money SAFE structures without identifying them.** Pre-money SAFEs create
   cross-dilution between SAFE holders — each new SAFE dilutes prior holders, not just founders.
   Identify the SAFE form before modeling.

5. **Skipping shadow preferred verification.** Shadow preferred mechanics prevent liquidation
   preference overhang. Their absence is one of the most common and consequential cap table
   errors in SAFE/note conversion. Always check the conversion provisions, not just the share
   counts.

6. **Modeling anti-dilution adjustment without verifying the charter's "A" definition.**
   The difference between broad-based and narrow-based weighted average is entirely in the
   definition of "A" in the BBWA formula. Two cap tables can look identical but have materially
   different anti-dilution exposure depending on whether unissued option pool shares are included
   in "A." Always read the charter definition.

7. **Treating option pool as cost-free to existing investors.** The option pool shuffle means
   that pre-money pool expansion dilutes only existing shareholders, not the new investor. A
   "20% pool" required by an investor effectively reduces the investor's cost basis. Model
   the effective valuation when presenting terms to founders.

8. **Ignoring anti-dilution carve-outs.** Routine option grants, strategic issuances, and
   stock splits should not trigger anti-dilution adjustments. If the charter is missing NVCA
   standard carve-outs, every routine equity event may trigger adjustment obligations —
   a critical structural error.

9. **Failing to calculate the liquidation waterfall crossover point.** Presenting a liquidation
   preference without calculating the exit value at which investors prefer to convert to common
   (the crossover point) leaves founders unable to evaluate the real impact of the preference
   structure across exit scenarios.

10. **Modeling participating preferred as non-participating.** Participation doubles (or more)
    investor returns at moderate exit values. A cap table analysis that omits participation
    mechanics dramatically underestimates investor economics and overestimates founder proceeds.

11. **Treating valuation caps as floor prices.** A valuation cap is a ceiling on the conversion
    price (maximum valuation at which the SAFE converts), not a floor. Above the cap, the
    investor gets a better deal. Below the cap, the discount rate may produce an even better
    price. Always apply the lower-of-cap-vs.-discount rule.

12. **Missing maturity overhang in convertible notes.** Unconverted notes approaching maturity
    create an obligation to repay or convert. A cap table that treats an unmatured note as an
    indefinite equity obligation — rather than modeling maturity risk — misrepresents the
    company's capital structure.

13. **Not tracking warrant expiration.** Warrants issued to bridge lenders, banks, or advisors
    expire on a schedule. Expired warrants must be removed from the fully diluted count. Near-
    expiry warrants must be flagged as potential near-term share issuance events. Untracked
    warrants cause reconciliation errors in every subsequent financing.

14. **Using a spreadsheet cap table for a multi-series company.** Spreadsheets introduce version
    control errors, formula dependency risks, and audit failures. Cap tables for any company with
    more than 3 stakeholders or complex instruments should be maintained in Carta, Pulley, or
    equivalent software.

15. **QSBS analysis without checking gross assets at each round.** The QSBS eligibility test
    applies at the moment of issuance, not retroactively. A company that raises a large round
    pushing gross assets above the threshold (pre-July 4, 2025: $50M; post-July 4, 2025: $75M
    [VERIFY — OBBBA § 1202]) disqualifies shares issued after that event from QSBS treatment,
    while prior shares retain their eligibility. Track the threshold crossing date.

16. **Ignoring 409A timing for new grants.** Material cap table events (new funding round,
    significant new contract, key executive change) require a fresh 409A valuation before
    subsequent option grants. Grants made after a material event but before a new 409A
    valuation carry IRC § 409A excise tax risk.

17. **Omitting documentation audit from cap table review.** Share counts can be correct while
    the underlying documentation is deficient. Every equity event requires an executed grant
    agreement, board resolution, and cap table entry — all within 24 hours of the event. Missing
    documentation is a closing condition risk at every institutional round.

---

## Writing Standards

Apply plain-language discipline to all output:

**For founder-facing summaries:**

- Active voice: "Your SAFEs will convert at $0.80/share" not "The conversion price is $0.80/share."
- State the implication: "At $0.80/share, SAFE investors receive 12.5% of the company —
  more than the 10% stated in the SAFE, due to interest accrual."
- Arithmetic must be shown: never present a conclusion without showing the formula and inputs.

**For investor / counsel output:**

- Same plain-language standards with technical precision added
- Show formula, inputs, and intermediate results for all calculations
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a founder with no finance training understand the executive summary?
2. Can counsel verify every arithmetic step from the inputs shown?
3. Is every legal claim backed by a specific citation (or marked [VERIFY])?
4. Are all modeled scenarios labeled as scenarios (not predictions)?
5. Is every assumption stated explicitly — especially for verbal descriptions with incomplete data?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal authority tool.

**With legalcode-mcp connected:**

- In Step 4, search for current DGCL provisions, IRC § 1202 and § 409A thresholds, and Rule 701
  disclosure requirements — verify all thresholds against current authority
- Confirm NVCA October 2025 model document provisions for anti-dilution carve-outs and charter
  mechanics
- Save verified authority to `/tmp/legalcode-cap-table-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and model-document references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require manual verification"`
- Focus the analysis on structural issues, arithmetic verification, and market standard
  benchmarking rather than statutory precision
- Do not create the local authority reference file

**Cap table software integration:**

- If a Carta or Pulley export is provided, parse the export format and flag any differences
  between the software's fully diluted count and the calculated fully diluted count
- Nota bene: Cap table software applies its own conversion assumptions for SAFEs —
  verify that the platform's assumptions match the actual SAFE instrument terms

---

## Localization Notes

This skill is calibrated for US Delaware C-Corp structures. When reviewing a non-US cap table:

1. **UK (England and Wales)**: Share classes defined in articles of association (not a
   separate charter). No concept of "preferred stock" — ordinary shares and preference shares
   governed by Companies Act 2006. EMI options under ITEPA 2003. SAFEs replaced by ASAs.
   Route to `legalcode-venture-financing-suite` for UK mechanics.

2. **Cayman Islands holding structure**: C-corps often use a Cayman holding company with Class A
   and B ordinary shares for international investors. No preferred stock without specific charter
   provisions. Analyze under Cayman Islands Companies Act.

3. **EU (France/Germany/Nordics)**: Civil law systems — shareholder rights agreements and
   preference mechanics are contractual (in shareholders' agreements) rather than in the
   corporate charter. Convertible bonds (obligations convertibles) rather than SAFEs. Seek
   local corporate law counsel.

4. **Singapore / India**: Refer to `legalcode-venture-financing-suite` for MAS-specific and
   FEMA/RBI-specific equity structuring guidance.

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Cap Table Review Summary

**Company**: [name or "Redacted"]
**Stage**: [Pre-seed / Seed / Series A / etc.]
**Review Purpose**: [Upcoming financing / Exit / Diligence / Audit]
**Your Role**: [Founder / Investor / Counsel]
**Review Date**: [date]
**Cap Table as of**: [date of submitted cap table]

---

### Ownership Summary (Fully Diluted)

| Stakeholder Group       | Shares  | % Fully Diluted | Notes                                     |
| ----------------------- | ------- | --------------- | ----------------------------------------- |
| Founders                | [N]     | [X%]            |                                           |
| SAFE investors          | [N]     | [X%]            | On as-converted basis (assumed price: $X) |
| [Series A preferred]    | [N]     | [X%]            |                                           |
| Option pool (granted)   | [N]     | [X%]            |                                           |
| Option pool (unissued)  | [N]     | [X%]            |                                           |
| Warrants                | [N]     | [X%]            |                                           |
| **Total fully diluted** | **[N]** | **100%**        |                                           |

---

### Findings

#### CRITICAL Issues [N]

**[Issue 1 — e.g., Shadow Preferred Mechanics Absent]**

- **What**: [Clear statement of the issue]
- **Why it matters**: [Legal and economic impact]
- **Legal basis**: [Statute / model document / charter provision]
- **Recommended action**: [Specific step with timeline]
- **Confidence**: [Level] — [brief rationale]

#### FLAG Issues [N]

**[Issue 1 — e.g., Pre-Money SAFE in Use]**

- **What**: [Clear statement of the deviation]
- **Market standard**: [What NVCA / YC standard requires]
- **Economic impact**: [Quantified if possible]
- **Recommended action**: [Specific step]

#### PASS [N items confirmed compliant]

- [Item 1 — e.g., BBWA anti-dilution provisions present and carve-outs complete]
- [Item 2 — e.g., Option pool: 15% of post-money FD — within NVCA standard range]

---

### SAFE Analysis

[For each SAFE:]
**SAFE: [Investor / Amount / Date]**

- Type: [Post-money / Pre-money]
- Valuation cap: $[X]M
- Discount: [N%] / None
- MFN: [Present / Absent]
- Pro-rata: [Present / Absent]
- Fixed ownership %: [X%] (post-money) or [TBD at conversion] (pre-money)
- Shadow preferred: [Present / Absent — FLAG/CRITICAL if absent]
- Conversion at Series A ($[X]M pre-money): [X] shares at $[X]/share

---

### Convertible Note Analysis

[For each note:]
**Note: [Holder / Amount / Maturity Date]**

- Principal: $[X]
- Rate / Accrual: [X%] [simple/compound]
- Discount: [X%]
- Valuation cap: $[X]M
- Maturity: [date] — [days remaining / CRITICAL if < 60 days]
- Conversion scenario (at $[X]M Series A): [discount: $X/share] vs. [cap: $X/share] → applied: $[X]/share
- Shadow preferred: [Present / Absent]

---

### Option Pool Analysis

- Authorized pool: [N] shares = [X%] of fully diluted
- Granted options: [N] shares = [X%] of fully diluted
- Ungranted (reserved): [N] shares = [X%] of fully diluted
- Option pool shuffle impact (if upcoming round): [explain founder dilution from pool expansion]
- Rule 701 12-month issuance: $[X] — [X%] of $10M threshold

---

### Anti-Dilution Summary

| Series     | Type   | BBWA Formula "A" Definition   | Standard?                |
| ---------- | ------ | ----------------------------- | ------------------------ |
| [Series A] | [BBWA] | [Broad-based incl. full pool] | [PASS / FLAG / CRITICAL] |

Down-round scenario (if applicable):

- Existing conversion price: $[X]
- Down-round price: $[X]
- Adjusted conversion price (BBWA): $[X]
- Impact on as-converted share count: [+X shares]

---

### Liquidation Waterfall

**Exit scenarios:**

| Exit Value          | [Series A preferred] | Founders + Common | Notes                       |
| ------------------- | -------------------- | ----------------- | --------------------------- |
| $[X]M (distressed)  | $[X]                 | $[X]              | Preference taken            |
| $[X]M (moderate)    | $[X]                 | $[X]              | [Convert / Take preference] |
| $[X]M (strong exit) | $[X]                 | $[X]              | Converts to common          |

Crossover point (Series A converts to common): **$[X]M exit**

---

### Dilution Scenario Modeling

**Current fully diluted ownership:**
| Party | Current % FD |
|-------|-------------|
| Founders | [X%] |
| SAFE investors | [X%] |
| [Others] | [X%] |

**Post-Series A (illustrative — $[X]M at $[X]M pre-money + [X%] pool):**
| Party | Post-Series A % FD |
|-------|-------------------|
| Founders | [X%] |
| SAFE investors (converted) | [X%] |
| Series A | [X%] |
| Option pool | [X%] |

---

### Regulatory Flags

- 409A status: [Current / Refresh needed — last valuation: date]
- QSBS eligibility: [All series eligible / Series [X] at risk — gross assets $[X]M vs. threshold]
- Rule 701: [Below threshold / Approaching — monitor]

---

### Prioritized Action Plan

**Tier 1 — Address Before Next Round:**

1. [Action + responsible party + timeline]

**Tier 2 — Address in Current Quarter:**

1. [Action + responsible party + timeline]

**Tier 3 — Ordinary Course Clean-Up:**

1. [Action + responsible party + timeline]

---

[Glass Box Audit Trail — YAML block as specified in the Quality Assurance Framework]
```

---

## Provenance

Created by Legalcode (2026-03-22). Original synthesis drawing on:

- Y Combinator Post-Money SAFE Primer v1.1 and standard forms (ycombinator.com/documents)
- NVCA October 2025 model documents (nvca.org) — Certificate of Incorporation, Stock Purchase
  Agreement, Investors' Rights Agreement, Voting Agreement, Right of First Refusal and Co-Sale
- DGCL §§ 151, 242 (Justia 2025)
- IRC §§ 409A, 1202 including One Big Beautiful Budget Act (OBBBA) amendments effective
  July 4, 2025 (gross asset threshold increase from $50M to $75M and exclusion limit from
  $10M to $15M per investor) [VERIFY currency]
- Securities Act Rule 701 (SEC.gov, 2018 rule raising threshold to $10M)
- Carta State of Pre-Seed Q3 2025 market data
- Fenwick & West, Wilson Sonsini, Cooley, Pillar Legal market practice commentary
- Venture Hacks option pool shuffle analysis
- FundersClub convertible note numerical examples
