---
name: legalcode-venture-financing-in
description: 'India venture financing skill covering the full lifecycle from pre-seed to IPO exit. Use
  when a founder, investor, counsel, or finance professional needs to: structure a venture financing round
  under Indian law; analyze iSAFE vs. CCPS vs. CCD instrument selection; review FEMA compliance for foreign
  investor participation; assess DPIIT recognition strategy; evaluate Section 80-IAC or SEBI AIF eligibility;
  analyze a term sheet for an Indian startup; plan an IPO, secondary transaction, or reverse flip exit;
  or draft FC-GPR/FC-TRS filing strategy.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

India venture financing skill covering the full lifecycle from pre-seed to IPO exit. Deep analysis of India-specific instruments and regulatory frameworks: iSAFE (structured as CCPS under Companies Act 2013), Compulsorily Convertible Preference Shares (CCPS), Compulsorily Convertible Debentures (CCD), and priced equity rounds. Covers FEMA/NDI Rules 2019 pricing and reporting (Form FC-GPR, Form FC-TRS), SEBI Alternative Investment Fund (AIF) Category I angel fund regulations (including September 2025 restructuring), angel tax abolition (Finance Act 2024, effective FY 2025-26), Section 80-IAC startup tax holiday (3-year profit exemption), DPIIT recognition requirements and benefits, RBI External Commercial Borrowing (ECB) automatic route for startups, and SEBI ICDR IPO eligibility. Covers standard India term sheet terms: 1x non-participating liquidation preference, broad-based weighted average (BWAA) anti-dilution, ROFR/ROFO/co-sale/drag-along mechanics, founder vesting norms, ESOP pool sizing, board composition, and exit waterfall analysis. Use when a founder, investor, counsel, or finance professional needs to: structure a venture financing round under Indian law; analyze iSAFE vs. CCPS vs. CCD instrument selection; review FEMA compliance for foreign investor participation; assess DPIIT recognition strategy; evaluate Section 80-IAC or SEBI AIF eligibility; analyze a term sheet for an Indian startup; plan an IPO, secondary transaction, or reverse flip exit; or draft FC-GPR/FC-TRS filing strategy. Also triggers on: India SAFE note, iSAFE 100X.VC, CCPS conversion mechanics, FEMA FDI pricing, NDI Rules Rule 21, Form FC-GPR 30-day deadline, FIRMS portal, angel tax abolished, Section 56(2)(viib) repeal, 80-IAC IMSC committee, DPIIT startup recognition, SEBI AIF Category I, angel fund corpus, RBI ECB automatic route startups, SEBI ICDR eligibility, IPO lock-up India, reverse flip fast-track.


# Legalcode India Venture Financing

> **Disclaimer**: This skill provides a framework for AI-assisted venture financing
> analysis under Indian law. It does not constitute legal, tax, securities, or
> financial advice. All outputs must be reviewed by a qualified attorney, tax advisor,
> Company Secretary, and securities counsel licensed in India before any reliance or
> action. Indian laws, FEMA regulations, SEBI rules, RBI circulars, and income tax
> provisions change frequently — verify current applicability against authoritative
> sources. References to statutes (Companies Act 2013, FEMA NDI Rules 2019, Income Tax
> Act 1961, SEBI AIF Regulations), regulatory thresholds, and market benchmarks carry
> currency risk — verify the latest RBI circular, SEBI notification, and Finance Act
> amendment. AI-generated cap table arithmetic and FEMA compliance analysis require
> independent verification. Nothing here constitutes investment advice or an offer or
> solicitation to buy or sell securities.

---

## Purpose and Scope

This skill analyses India venture financing decisions end-to-end — from instrument
selection at pre-seed through to exit via IPO, strategic sale, or secondary transaction.
It incorporates India's unique regulatory framework: FEMA constraints on foreign
investment, DPIIT recognition as a gateway to tax benefits, and the distinctive
iSAFE/CCPS/CCD instrument landscape.

**Covers:**

- Instrument selection: iSAFE vs. CCPS vs. CCD vs. priced equity round, with
  India-specific regulatory analysis
- iSAFE deep dive: legal structure as CCPS, 100X.VC standard terms, conversion
  mechanics, FEMA treatment, tax treatment under Section 47
- CCPS analysis: mandatory conversion triggers, liquidation preference tiers,
  anti-dilution (BWAA formula), voting rights, dividend rights, redemption
- CCD analysis: debt vs. equity classification, FEMA capital instrument treatment,
  pre-conversion interest deductibility, conversion mechanics
- FEMA/NDI Rules pricing: Rule 21 fair market value certification, 90-day freshness
  rule, Form FC-GPR (30-day filing deadline), Form FC-TRS, FIRMS portal, AD bank role
- SEBI AIF Category I angel funds: corpus requirements, accredited investor criteria,
  per-company investment limits, September 2025 restructuring, quarterly NAV reporting
- Angel tax abolition: Finance Act 2024 repeal of Section 56(2)(viib), effective
  FY 2025-26, practical implications for resident and foreign investors
- Section 80-IAC tax holiday: 3-year profit exemption, eligibility criteria, DPIIT
  recognition prerequisite, extended eligibility window to April 1, 2030
- DPIIT recognition: application process, eligibility criteria (including deep tech
  20-year window), documentation, benefits matrix
- RBI ECB guidelines: automatic route for DPIIT-recognized startups, eligible
  borrowers/lenders, minimum average maturity, end-use rules, ECB vs. FEMA equity
- India term sheet analysis: liquidation preference, anti-dilution, information
  rights, board composition, ROFR/ROFO/co-sale/drag-along, founder vesting, ESOP pool
- Exit analysis: SEBI ICDR IPO eligibility, lock-up periods, reverse flip mechanics,
  secondary share transactions, FEMA pricing on exit

**Does not:**

- Provide legal, tax, or investment advice or replace qualified Indian counsel or a
  Company Secretary
- Perform a full term sheet analysis — route to `legalcode-term-sheet-analysis` for
  complete term sheet deep dive
- Draft definitive documents (SHA, SSA, CCPS instrument, iSAFE note)
- Model fund return economics from the investor's portfolio construction perspective
- Substitute for SEBI AIF registration or RBI FEMA compliance opinion
- Cover non-India foreign investment (route to `legalcode-venture-financing-suite`
  for US/UK/EU/Singapore financing analysis)

**Relationship to other skills:**

| Task                                            | Use This Skill       | Route To                                 |
| ----------------------------------------------- | -------------------- | ---------------------------------------- |
| India-specific instrument + regulatory analysis | ✅ This skill        | —                                        |
| Full term sheet deep dive                       | Initial framing only | `legalcode-term-sheet-analysis`          |
| Equity plan review                              | Summary only         | `legalcode-equity-incentive-plan-review` |
| Multi-jurisdiction venture financing            | India track only     | `legalcode-venture-financing-suite`      |
| M&A due diligence                               | Cross-reference      | `legalcode-ma-due-diligence-checklist`   |
| Founders' agreement                             | Initial structure    | `legalcode-founders-agreement-drafter`   |

---

## Jurisdiction and Governing Law

This skill is **India-specific**. The primary legal frameworks are:

| Framework                                           | Authority                                         | Relevance                                               |
| --------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| Companies Act, 2013                                 | Ministry of Corporate Affairs (MCA)               | Company formation, share classes, ESOP, CCD/CCPS        |
| FEMA (Non-Debt Instruments) Rules, 2019 (NDI Rules) | Reserve Bank of India (RBI)                       | Foreign investment pricing, reporting, repatriation     |
| Income Tax Act, 1961                                | Central Board of Direct Taxes (CBDT)              | Angel tax, Section 80-IAC, ESOP taxation, capital gains |
| SEBI (AIF) Regulations, 2012 (as amended)           | Securities and Exchange Board of India (SEBI)     | Angel funds, venture capital funds                      |
| SEBI (ICDR) Regulations, 2018 (as amended)          | SEBI                                              | IPO eligibility, lock-up, OFS                           |
| RBI Master Directions on Foreign Investment         | Reserve Bank of India                             | FEMA compliance, FC-GPR/FC-TRS, ECB                     |
| DPIIT Startup Recognition Framework                 | Dept for Promotion of Industry and Internal Trade | Recognition eligibility, 80-IAC gateway                 |

India follows a **common law** legal tradition (Companies Act is UK-origin influenced),
but the startup regulatory landscape is driven by FEMA (exchange control), SEBI
(securities regulation), and CBDT (income tax) frameworks that have no direct
equivalents in other common law jurisdictions.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming user intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Regulatory classification depends on facts not yet provided
- India-specific nuances require context before the right answer can be given

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

### Step 1: Accept the Input

Accept input in any of these formats:

- **Term sheet or SHA/SSA draft**: Document pasted or uploaded
- **Description of proposed deal**: Free-text description of instrument, parties,
  amounts, and key terms
- **Specific regulatory question**: FEMA compliance, DPIIT eligibility, AIF analysis
- **Exit scenario**: IPO planning, secondary sale, or reverse flip analysis

If no document or description is provided, prompt the user to supply context.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask:

1. **Task type**: What is the primary objective?
   - Options: Instrument selection (pre-seed/seed), CCPS/iSAFE term review,
     FEMA compliance check, DPIIT recognition strategy, Section 80-IAC analysis,
     SEBI AIF eligibility (angel fund), Exit planning (IPO/secondary/reverse flip),
     Full deal structuring review
   - _Why this matters_: Determines which modules to activate and which research
     depth is appropriate.

2. **Investor profile**: Who is investing?
   - Options: Resident Indian individual (angel), DPIIT-recognized angel fund (AIF),
     Foreign individual (NRI/OCI), Foreign institutional (VC/PE fund), Foreign corporate,
     FVCI-registered fund, Multiple investor types
   - _Why this matters_: FEMA applicability, pricing requirements, and Form FC-GPR
     obligations are triggered by foreign investor participation.

3. **Company stage**: Where is the company in its lifecycle?
   - Options: Pre-incorporation (planning stage), Incorporated < 1 year (pre-revenue),
     Seed (₹0-5 crore raised), Series A (₹5-50 crore raised), Series B+ (₹50+ crore
     raised), Pre-IPO
   - _Why this matters_: Instrument selection, DPIIT recognition eligibility, and
     Section 80-IAC planning are all stage-sensitive.

4. **DPIIT status**: Is the company DPIIT-recognized?
   - Options: Yes (certificate attached), In process, Not yet applied, Not eligible
   - _Why this matters_: DPIIT recognition is a prerequisite for Section 80-IAC and
     affects ECB automatic route access and angel tax (historical) analysis.

5. **Prior foreign investment**: Has the company previously received foreign investment?
   - Options: Yes (FC-GPR filed), Yes (FC-GPR pending), No, Uncertain
   - _Why this matters_: Prior filings affect cap table structure, AD bank relationship,
     and potential FEMA compounding exposure.

If the user provides partial context, proceed with reasonable defaults and state
assumptions explicitly. Example: "I'm assuming no prior FEMA filings — let me know if
that's incorrect and I'll revise the analysis."

### Step 3: Load Reference Framework

Use **legalcode-mcp** to gather India-specific legal authority for this analysis.

**Research targets:**

```
legalcode-mcp search queries:
  - "FEMA Non-Debt Instruments Rules 2019 Rule 21 pricing equity"
  - "Companies Act 2013 Section 55 CCPS definition"
  - "Income Tax Act Section 80-IAC startup tax exemption"
  - "SEBI AIF Regulations 2012 angel fund Category I"
  - "RBI ECB automatic route DPIIT startup"
  - "SEBI ICDR IPO eligibility criteria 2025"
```

Save results to `/tmp/legalcode-india-vf-research.md`:

```markdown
# India Venture Financing — Legal Authority Reference

## Date: [date]

### FEMA / NDI Rules

- [Provision, current text, relevance]

### Companies Act 2013

- [Section, current text, relevance]

### Income Tax Act 1961

- [Section, current text, relevance]

### SEBI Regulations

- [Regulation, current text, relevance]

### RBI Circulars / Master Directions

- [Circular/direction, date, relevance]

### DPIIT Notifications

- [Notification, date, relevance]
```

**If legalcode-mcp is not connected:**

- Proceed using research embedded in this skill
- Mark all statutory references with [VERIFY] for independent verification
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Step 4: Instrument Selection Analysis

Based on the user's context, analyze which financing instrument best suits the deal.

**⟁ CLARIFY** — If the instrument has not been specified, ask:

- "Which instrument are you considering, or would you like a comparison across all
  options (iSAFE, CCPS, CCD, priced equity)?"
- "Is this a foreign investor or domestic investor? [This determines whether FEMA
  compliance and Form FC-GPR apply]"

Run the **Instrument Selection Matrix** from the Core Analysis Framework below.

### Step 5: FEMA Compliance Analysis

For any deal involving a non-resident investor (NRI, OCI, foreign corporate, foreign
institutional), run the FEMA compliance module:

1. **Classify the instrument**: Is it a capital instrument (equity, CCPS, CCD, fully
   convertible warrants) or a non-capital instrument? Capital instruments use FEMA
   equity route (NDI Rules); non-capital instruments require RBI approval or ECB
   treatment.

2. **Apply pricing norms**: Confirm that the issue price ≥ fair market value (FMV)
   per NDI Rules, Rule 21. Check that a valuation certificate dated within 90 days
   of allotment is in place.

3. **Plan FC-GPR filing**: Confirm the 30-day-from-allotment filing deadline. Identify
   the authorized dealer (AD) Category-I bank. Prepare the documentation checklist.

4. **Check sector caps**: Confirm the company's sector is not in a restricted or
   prohibited FDI sector. Most tech startups fall under the automatic route with
   100% FDI permitted, but fintech, media, defense, and insurance have caps or
   conditions.

**⟁ CLARIFY** — For convertible instruments with delayed conversion:

- "When will conversion occur? FEMA pricing compliance must be satisfied both at
  issuance and at conversion if the conversion price is not fixed at issuance."

### Step 6: Tax Benefit Analysis

Run the tax incentive module to assess Section 80-IAC eligibility and angel tax status.

1. **Angel tax** (Section 56(2)(viib)): Confirm abolition effective April 1, 2025.
   For investments made before FY 2025-26, review whether prior exemption certificates
   are needed.

2. **Section 80-IAC**: Check eligibility (incorporated post April 1, 2016; turnover
   <₹100 crore; DPIIT-recognized; not formed by splitting). If eligible, plan which
   3 consecutive years within the 10-year window to claim the exemption.

3. **DPIIT recognition**: If not yet recognized, assess eligibility and map the
   application process. Recognition unlocks both 80-IAC and multiple regulatory
   benefits.

### Step 7: Term Sheet Analysis

Review the key commercial terms of the proposed deal against India market standards.

Use the **Term Sheet Benchmark Table** from the Core Analysis Framework. For each
term, classify as MARKET (aligned with standard India VC practice), AGGRESSIVE
(deviating in investor's favor), or FOUNDER-FAVORABLE (deviating in founder's favor).

**⟁ CLARIFY** — For borderline terms:

- Present both the market standard and the proposed term
- Ask whether to classify as MARKET (acceptable) or AGGRESSIVE (flag for negotiation)
- Example: "Participating liquidation preference is below market (standard is 1x
  non-participating). Should I flag this as AGGRESSIVE?"

### Step 8: Exit Scenario Analysis

For pre-IPO or exit-focused queries, run the exit planning module:

1. **IPO path**: SEBI ICDR eligibility check, promoter contribution requirements,
   lock-up periods, OFS mechanics, reverse flip assessment if company is foreign-held.

2. **Strategic sale**: FEMA pricing compliance on exit, Form FC-TRS requirements,
   drag-along enforcement, deferred consideration (up to 18 months holdback permitted
   per RBI January 2025 Master Direction).

3. **Secondary transaction**: Secondary sale pricing (minimum FMV per FEMA), Form
   FC-TRS filing (60-day deadline), ROFR/ROFO enforcement, buyer FEMA compliance.

### Step 9: Quality Verification

Before delivering the analysis, run the quality checks in the Quality Assurance
Framework section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL-classified item, run 3-pass Self-Interrogation.
3. Score the analysis on the 5-level Confidence Scale per finding.
4. Populate the Glass Box audit trail template.
5. Verify that all India-specific [VERIFY] markers are correctly placed.

### Step 10: Deliver Analysis

Present the output using the **Output Format Template** at the end of this skill.

---

## Core Analysis Framework

### Instrument Selection Matrix

| Feature                           | iSAFE                      | CCPS (Standard Round)             | CCD                           | Priced Equity             |
| --------------------------------- | -------------------------- | --------------------------------- | ----------------------------- | ------------------------- |
| **Legal form**                    | CCPS (preference shares)   | Preference shares                 | Debentures                    | Equity shares             |
| **Valuation at issuance**         | Not required               | Required (FEMA if foreign)        | Required (FEMA if foreign)    | Required                  |
| **FEMA classification**           | Capital instrument         | Capital instrument                | Capital instrument            | Capital instrument        |
| **Form FC-GPR required**          | Yes (if foreign investor)  | Yes (if foreign investor)         | Yes (if foreign investor)     | Yes (if foreign investor) |
| **Pre-conversion tax**            | None (not debt)            | None                              | Interest deductible (company) | N/A                       |
| **Conversion trigger**            | IPO, qualified round, time | IPO, qualified round, time        | Mandatory at maturity         | N/A                       |
| **Conversion tax**                | None (Section 47)          | None (Section 47)                 | None (generally Section 47)   | N/A                       |
| **Typical use case**              | Angel/pre-seed (speed)     | Institutional seed/Series A       | Bridge financing              | Series A/B and beyond     |
| **Documentation complexity**      | Low (5-10 pages)           | Medium-high (SHA + SSA)           | Medium (debenture deed)       | High (full SHA/SSA/SPA)   |
| **Angel fund (AIF) compatible**   | Yes                        | Yes                               | Yes                           | Yes                       |
| **Governance rights at issuance** | Minimal                    | Negotiated                        | Minimal pre-conversion        | Full (upon issuance)      |
| **Regulatory complexity**         | Low                        | Medium (Companies Act procedures) | Medium                        | Medium-high               |

**Decision guidance:**

- **iSAFE**: Optimal for angel rounds requiring speed and minimal documentation.
  Best for pre-revenue startups with DPIIT recognition, where valuation is premature.
  Use when investors want simple terms and founders want to delay dilution.

- **CCPS**: Standard instrument for institutional seed and Series A. Provides
  investors with preference rights, anti-dilution protection, and governance rights.
  Required for investors who need defined equity ownership at issuance.

- **CCD**: Use for bridge financing between rounds or when investor wants
  interest income pre-conversion. Tax advantage: interest deductible for company
  pre-conversion. Less common than CCPS in startup financing.

- **Priced equity**: Appropriate when full governance rights, defined cap table,
  and clean equity structure are required. Standard for Series B and beyond.

---

### iSAFE Deep Dive

#### Legal Structure and Origin

iSAFE (India Simple Agreement for Future Equity) was introduced by 100X.VC in 2019
as India's adaptation of the US SAFE. Unlike the US SAFE (a contractual instrument),
iSAFE is structured as **Compulsorily Convertible Preference Shares (CCPS)** under
**Sections 42, 55, and 62 of the Companies Act, 2013** and the **Companies (Share
Capital and Debentures) Rules, 2014**.

The CCPS structure is legally required because Indian corporate law does not support
a simple contractual claim on future equity — the instrument must be issued as actual
shares to obtain capital instrument treatment under FEMA and proper shareholder
protections under the Companies Act.

#### Standard iSAFE Variants

| Variant                       | Key Mechanism                                                           | Best For                                         |
| ----------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------ |
| **Valuation Cap**             | Investor converts at cap/next-round price (lower of two)                | Angel investors wanting upside protection        |
| **Discount**                  | Investor converts at X% discount to next round price                    | Angel investors wanting price incentive          |
| **Cap + Discount**            | Investor gets better of cap or discount                                 | Standard angel protection in competitive rounds  |
| **MFN (Most Favored Nation)** | iSAFE terms automatically upgrade to best terms of subsequent investors | Very early angels investing before terms are set |
| **Fixed Conversion**          | Predetermined conversion price at issuance                              | Founders wanting certainty on dilution           |

#### Conversion Mechanics

Conversion is **automatic and mandatory** upon the occurrence of a **Liquidity Event**:

- **Qualified Financing**: Next priced round at or above a minimum threshold (typically
  ₹2-5 crore round size), converting at the lower of valuation cap or (if applicable)
  discounted round price
- **Dissolution/Winding Up**: Investors receive invested amount in preference to equity
  holders; iSAFE holder treated as CCPS holder in liquidation waterfall
- **IPO or Acquisition**: Conversion at predetermined ratio before listing or exit

**Anti-dilution on conversion**: iSAFE CCPS typically include broad-based weighted
average (BWAA) anti-dilution protection, adjusting conversion ratio in down rounds.

#### Tax Treatment

**At conversion (Section 47, Income Tax Act 1961)**:
Conversion of preference shares (iSAFE CCPS) into equity shares is **not treated as
a transfer** and **does not trigger capital gains tax** at conversion. [VERIFY current
Section 47 position with tax counsel]

**For company**: No tax event at issuance of iSAFE CCPS (no interest accrues). No
deduction at conversion.

**For investor**: Capital gains arise only upon ultimate **sale of equity shares
received on conversion** — taxed as LTCG (12.5% if listed, 20% with indexation if
unlisted and held > 2 years) or STCG (slab rate if held < 2 years).

#### FEMA Treatment

iSAFE CCPS issued to a foreign investor is a **capital instrument** under FEMA (NDI
Rules 2019, Schedule I). This means:

- **FDI automatic route** applies for most tech startups (100% FDI permitted)
- **Fair market value** certification required at issuance (NDI Rules, Rule 21)
- **Form FC-GPR** must be filed within 30 days of allotment via FIRMS portal
- **No minimum pricing floor below FMV** (but no ceiling either — premium issuance
  to strategic investors is permissible)
- **At conversion**: If conversion ratio is not fixed at issuance, a new FMV
  certificate may be required at conversion to comply with Rule 21 pricing

---

### CCPS Deep Dive

#### Legal Framework

CCPS are issued under **Section 55 of the Companies Act, 2013** (preference shares)
and must mandatorily convert into equity within a maximum period specified in the
terms (commonly 20 years; no minimum period mandated by statute). The conversion terms
must be set out in the Memorandum and Articles of Association or in a special resolution.

#### Standard Terms Reference

**Liquidation Preference:**

- **Market standard**: **1× non-participating** — investor receives invested amount
  first; does not participate in residual proceeds above 1× preference
- **Aggressive (investor-favorable)**: Participating preference — investor receives
  1× preference AND participates in residual proceeds pro-rata with common equity
  holders (also called "double-dip")
- **Founder-favorable**: No liquidation preference (rare; only in founder-friendly
  early seed rounds from domestic angels)
- **Multiple liquidation preferences** (e.g., 2× or 3×): Rare; typically seen only
  in distressed or late-stage structured rounds

**Anti-Dilution (Broad-Based Weighted Average Formula):**

```
New Conversion Price = Old CP × [(A + B) ÷ (A + C)]

Where:
  A = Total shares outstanding before new issue (fully diluted, including all
      outstanding options, warrants, and convertible securities)
  B = Shares that would have been issued at Old CP if new money raised at Old CP
      (= new money raised ÷ Old CP)
  C = Actual new shares issued in down round
```

This formula is **more founder-friendly than full ratchet** (which reprices all
investor shares to the new lower price) and **more investor-friendly than
narrow-based** (which uses a smaller share count in A, resulting in smaller
adjustment).

**Important FEMA constraint**: Anti-dilution adjustments reducing the conversion
price must still result in a price **not below FMV** at the time of conversion.
A conversion price below FMV at exercise would violate NDI Rules, Rule 21. [VERIFY]

**Dividend Rights:**

- Standard: **Cumulative, 0.001%–0.01% per annum** (essentially nominal; accrues
  but is not paid in high-growth startups)
- The dividend accrues as a liability but is almost never paid; it is usually waived
  at IPO conversion or acquirer preference
- Non-cumulative structures exist but are less common

**Voting Rights:**

- CCPS typically carry **limited voting rights** on ordinary business matters
- **Protective provisions** (special consent rights) are standard for material events:
  - New share class creation or CCPS rights modification
  - Asset sale, merger, liquidation above a threshold
  - Increase in total authorized share capital beyond threshold
  - Related-party transactions above threshold
  - Material changes to business plan

**Mandatory Conversion Triggers:**

- **Qualified IPO** (meeting SEBI ICDR minimum thresholds)
- **Qualified financing** (next priced round above minimum threshold)
- **Acqui-hire or M&A** (subject to waterfall analysis)
- **Time-based**: Most CCPs include a **backstop conversion date** (typically 20 years,
  consistent with Companies Act s.55 maximum preference share holding period [VERIFY])
- **Shareholder vote**: Majority consent of CCPS holders can trigger early conversion

---

### FEMA / NDI Rules Compliance Framework

#### Rule 21 Pricing Requirement

**NDI Rules, 2019, Rule 21**: For equity instruments issued to a non-resident investor
in an unlisted Indian company, the **issue price must not be less than fair market value
(FMV)** computed in accordance with **internationally accepted pricing methodologies
on an arm's length basis**.

**Permissible methodologies** (as recognized by SEBI and CA practice):

- Discounted Cash Flow (DCF) — most common for early-stage startups
- Comparable Company Multiples (revenue, EBITDA, GMV)
- Net Asset Value (NAV)
- Option Pricing Model (OPM) — for companies with multiple share classes
- Return on Equity (RoE)

**Certification requirements:**

- SEBI-registered **Category I Merchant Banker**, or
- **Chartered Accountant** (in practice for unlisted company FMV), or
- **IBBI-registered Registered Valuer** (for specific instrument types)

**90-day freshness rule**: Valuation certificate must be dated **within 90 days** of
the date of share allotment. An outdated certificate from a prior funding round is not
sufficient for a new CCPS issuance.

#### Form FC-GPR Filing

**Form FC-GPR** (Foreign Currency – Gross Provisional Return) is the mandatory RBI
reporting for foreign direct investment in Indian equity/capital instruments.

| Parameter           | Requirement                                                     |
| ------------------- | --------------------------------------------------------------- |
| **Filing portal**   | RBI FIRMS (firms.rbi.org.in)                                    |
| **Filing deadline** | Within **30 days** from date of allotment of shares/instruments |
| **Who files**       | Indian company (through AD Category-I bank)                     |
| **AD bank role**    | Validates FEMA compliance, countersigns, submits to RBI         |

**Required documents for FC-GPR:**

1. Board resolution authorizing allotment
2. FEMA-compliant declaration by the company
3. Valuation certificate (FMV, dated within 90 days of allotment)
4. KYC documents of foreign investor (passport, PAN if applicable)
5. Foreign Inward Remittance Certificate (FIRC) — proof of funds received from
   foreign account
6. Shareholding pattern (pre- and post-allotment)
7. Company Secretary certificate of FEMA compliance

**Late filing penalties** (as of 2025 RBI Master Direction):

- First 6 months late: ₹5,000 per day or 1% of investment amount (up to ₹5 lakh)
- Beyond 6 months: Penalties double; compounding proceedings may be initiated

**AD bank requirement**: The company must have an existing banking relationship with
an AD Category-I bank before initiating foreign investment. The AD bank performs KYC
on the foreign investor and validates the FIRC.

#### Form FC-TRS Filing

**Form FC-TRS** (Foreign Currency – Transfer of Shares) is required for **secondary
transfers** between residents and non-residents (and in some cases between two
non-residents).

| Parameter           | Requirement                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Trigger**         | Transfer of equity, CCPS, CCD, or other capital instruments to/from non-resident                                          |
| **Filing deadline** | Within **60 days** of receipt/payment of funds or execution of transfer deed (whichever is earlier)                       |
| **Pricing rule**    | Transfer price must comply with NDI Rules Rule 21 (FMV for buyer if non-resident; minimum FMV for seller if non-resident) |
| **Filing portal**   | RBI FIRMS portal                                                                                                          |

**Deferred consideration** (per RBI January 2025 Master Direction):
Up to 18 months holdback/escrow is now permitted for secondary transactions in Indian
company shares, allowing M&A-style indemnity escrow structures for cross-border deals.

#### Sector FDI Caps

| Sector                               | FDI Cap                               | Route     |
| ------------------------------------ | ------------------------------------- | --------- |
| Technology (B2B SaaS, AI, analytics) | 100%                                  | Automatic |
| E-commerce (marketplace model)       | 100%                                  | Automatic |
| Fintech (payment aggregators)        | 49% (operator); 100% (infrastructure) | Automatic |
| Insurance                            | 74%                                   | Automatic |
| Defense                              | 74% (automatic) / 100% (approval)     | Mixed     |
| Gambling, lottery                    | Prohibited                            | —         |
| Multi-level marketing                | Prohibited                            | —         |

[VERIFY all sector caps against current DPIIT Consolidated FDI Policy and relevant
RBI sector guidelines, as these change regularly]

---

### SEBI AIF Regulations — Angel Fund Analysis

#### Category I AIF — Angel Fund Classification

**SEBI (Alternative Investment Funds) Regulations, 2012**, as amended through
September 2025, classifies **Angel Funds as standalone Category I AIFs** (previously
a sub-category of Venture Capital Funds).

#### Eligibility and Structure Requirements

| Parameter                            | Current Requirement                                                                 | Notes                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Minimum corpus**                   | ₹5 crore                                                                            | Must be maintained throughout fund life                         |
| **Investor type**                    | Accredited investors only                                                           | Individual: net worth > ₹2 crore OR income > ₹50 lakh/year      |
| **Minimum investors at first close** | 5 accredited investors                                                              | First close must occur within 12 months of registration         |
| **Maximum investors**                | 200 per scheme (AIF regulation limit); 49 per investee company (legacy)             | Specific consent required per investment under Sep 2025 reforms |
| **Minimum ticket size**              | ₹10 lakh per investor                                                               | Reduced from prior ₹25 lakh                                     |
| **Maximum per-company investment**   | ₹25 crore per company                                                               | Increased from prior ₹10 crore                                  |
| **Investment eligibility**           | DPIIT-recognized startups; unlisted companies < 10 years old; turnover < ₹100 crore | [VERIFY latest SEBI notification]                               |
| **Registration**                     | SEBI registration mandatory                                                         | Application through SEBI's online portal                        |
| **Quarterly NAV reporting**          | Within 45 days of quarter-end                                                       | Filed with SEBI                                                 |
| **Annual audit**                     | Required                                                                            | By SEBI-registered auditor                                      |

#### September 2025 Restructuring (SEBI AIF Second Amendment Regulations, 2025)

Key changes effective September 8, 2025:

1. **Standalone classification**: Angel funds separated from Venture Capital Fund
   sub-category into independent Category I standing
2. **Scheme elimination**: Angel funds no longer launch separate schemes per investee
   company; instead, investors provide **specific consent per investment opportunity**
3. **Co-investment vehicles (CIV)**: Permitted for parallel deployment alongside
   angel fund investments — investors in the fund can co-invest directly in specific
   opportunities via CIV
4. **Reduced diversification restrictions**: The 25% single-company exposure cap
   removed in favor of consent-based structure
   [VERIFY these specific provisions against latest SEBI AIF Second Amendment Regulations
   notification]

---

### Angel Tax Abolition — Section 56(2)(viib)

#### Current Status: Fully Abolished (Effective FY 2025-26)

**Finance Act 2024** (enacted July 23, 2024) permanently removed **Section 56(2)(viib)**
from the Income Tax Act, 1961, effective **April 1, 2025** (Assessment Year 2025-26
onwards).

**Historical context:**

- Section 56(2)(viib) (introduced 2012): Taxed excess share premium received by
  closely-held companies from **resident investors** when investment exceeded FMV
- **Finance Act 2023 extension**: Scope widened to include **non-resident investors**
  (effective FY 2023-24), causing significant alarm in the startup community
- **2024 abolition**: Both the resident and non-resident provisions removed entirely

#### Practical Implications

| Item                                   | Pre-FY25-26                     | FY 2025-26 Onwards                             |
| -------------------------------------- | ------------------------------- | ---------------------------------------------- |
| Excess premium from resident investors | Taxable as income               | **No tax**                                     |
| Excess premium from foreign investors  | Taxable as income (post-2023)   | **No tax**                                     |
| Exemption certificate (Form 3CG / 3CH) | Previously required             | **No longer needed**                           |
| CBDT-approved FMV computation          | Previously mandatory            | **Not required for angel tax**                 |
| Impact on FEMA FMV requirement         | Separate FEMA FMV still applies | FEMA FMV still required for foreign investment |

**Critical note**: The **FEMA fair market value requirement** (NDI Rules Rule 21) is
a **separate obligation** that continues to apply to foreign investor subscriptions.
Angel tax abolition does not remove FEMA pricing compliance for non-residents.

For **resident investor rounds** (domestic angels, SEBI AIF angel funds), there is
now **no FMV floor requirement** from an income tax perspective. The issuing startup
can issue at any premium to face value without triggering Section 56(2)(viib).

---

### Section 80-IAC Tax Holiday

#### What It Provides

**Section 80-IAC** of the Income Tax Act, 1961 provides a **100% deduction of profits
and gains** from business or profession for **3 consecutive assessment years** chosen
by the startup within the first **10 years** from the year of incorporation.

**Effective tax impact**: Zero income tax on profits for the 3 chosen years
(assuming no other income). This can represent a significant saving for startups
that achieve profitability in their early years.

#### Eligibility Requirements

| Criterion                      | Requirement                                                             | Notes                                                                 |
| ------------------------------ | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Entity type**                | Private Limited Company, LLP, or Registered Partnership Firm            | Not available to sole proprietorships or public companies             |
| **Incorporation date**         | On or after **April 1, 2016**                                           | Window extended to **April 1, 2030** by Union Budget 2025-26 [VERIFY] |
| **Annual turnover**            | Less than **₹100 crore** in any financial year since incorporation      | Measured in each prior year; not a cumulative cap                     |
| **DPIIT recognition**          | Valid DPIIT startup recognition certificate required                    | Recognition is a prerequisite, not just beneficial                    |
| **Not formed by splitting**    | Cannot be formed by splitting or reconstruction of an existing business | Anti-abuse rule; applies to spin-offs and restructured entities       |
| **Not formed by amalgamation** | Cannot be formed by amalgamation/merger                                 | Anti-abuse rule                                                       |

#### Application Process

1. **Obtain DPIIT recognition** (prerequisite — see DPIIT module below)
2. **File income tax return (ITR)** for the relevant assessment year
3. **Claim Section 80-IAC deduction** in the ITR (Form 3CJ for certification by CBDT,
   or as per current procedures — [VERIFY current form requirements])
4. **IMSC review**: An Inter-Ministerial Board of Certification (IMSC) reviews
   applications for startups seeking recognition and 80-IAC eligibility in complex
   cases; standard DPIIT-recognized startups apply directly through the income tax
   return

**Year selection strategy**: Choose the 3 consecutive years that coincide with the
startup's **peak profitability years** within the 10-year window. Early-stage startups
should wait until they have material profits before claiming the benefit.

#### 2025-26 Budget Extension

Union Budget 2025-26 extended the **incorporation date eligibility window** from
April 1, 2025 to **April 1, 2030**, allowing startups incorporated through FY 2029-30
to access the 80-IAC benefit. [VERIFY: Finance Act 2025 final text]

---

### DPIIT Startup Recognition Framework

#### What Is DPIIT Recognition?

The **Department for Promotion of Industry and Internal Trade (DPIIT)** issues
Certificates of Recognition to eligible startups. Recognition is the **gateway
to multiple tax and regulatory benefits** and is a prerequisite for Section 80-IAC.

#### Eligibility Criteria

| Criterion                 | Standard Startup                                                                                       | Deep Tech Startup                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| **Recognition window**    | Up to **10 years** from incorporation                                                                  | Up to **20 years** from incorporation |
| **Annual turnover cap**   | < ₹100 crore (extended to ₹200 crore under new norms [VERIFY])                                         | < ₹300 crore [VERIFY]                 |
| **Entity type**           | Private Ltd, LLP, Partnership Firm, or Cooperative                                                     | Same                                  |
| **Business character**    | Innovation in product/process/service OR scalable model with high wealth/employment creation potential | Demonstrated deep technology focus    |
| **Biotechnology**         | Up to 15 years from incorporation                                                                      | —                                     |
| **Formation restriction** | Not formed by splitting/reconstruction of existing business                                            | Same                                  |

#### Application Process

1. Visit **startupindia.gov.in** (or apply through National Single Window System portal)
2. Create account and verify company email
3. Navigate to "Recognition" → "Apply for DPIIT Recognition"
4. Complete online application form (company details, director/partner list, equity
   structure, business description)
5. Upload required documents:
   - Certificate of Incorporation or Registration
   - Memorandum of Association (MOA) and Articles of Association (AOA)
   - PAN of company and directors/partners
   - Board resolution authorizing DPIIT recognition application
   - Detailed description of innovation OR scalability proposition
   - Audited financial statements (last 2 years if available)
6. Submit application — **no application fee**
7. Typical recognition timeline: **60-120 days** from submission of complete application

#### Benefits Matrix

| Benefit                                    | Details                                                                                                                                      |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Section 80-IAC tax holiday**             | 3-year profit exemption (prerequisite: DPIIT recognition)                                                                                    |
| **Angel tax exemption**                    | Now irrelevant (angel tax fully abolished FY 2025-26)                                                                                        |
| **IPR fast-track**                         | Patents processed in fast-track mode; trademark registration expedited                                                                       |
| **SIDBI Fund of Funds**                    | Access to ₹10,000 crore government venture fund of funds                                                                                     |
| **Government procurement**                 | Exempted from prior turnover/experience requirement in government tenders                                                                    |
| **Self-certification (labor/environment)** | Startups in specified categories can self-certify compliance with 3 labor laws and 3 environmental laws for up to 5 years from incorporation |
| **ECB automatic route**                    | DPIIT-recognized startups eligible for RBI ECB automatic route regardless of business activity [VERIFY]                                      |
| **Collateral-free loans**                  | Access to collateral-free loans up to ₹1 crore from select banks under CGTMSE scheme                                                         |

---

### RBI ECB Framework for Startups

#### What Is ECB?

External Commercial Borrowings (ECBs) are cross-border loans from foreign lenders.
For startups, ECB is **not the primary financing route** (equity/CCPS is preferred
due to FEMA capital instrument treatment), but ECB becomes relevant for:

- Working capital or expansion debt from foreign banks after revenue stage
- Structured debt instruments from offshore venture lenders
- Cross-border intragroup lending from a holding company to an Indian subsidiary

#### DPIIT Startup ECB Automatic Route

Per **RBI Master Direction on External Commercial Borrowings, Trade Credits and
Structured Obligations** (as updated through 2025):

**DPIIT-recognized startups** may access ECB under the **automatic route** (no RBI
approval required) subject to:

| Parameter                    | Requirement                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Borrower eligibility**     | DPIIT-recognized startup as of ECB drawdown date                                                       |
| **Lender eligibility**       | Recognized lender (foreign bank, FI, export credit agency, multilateral institution)                   |
| **Minimum average maturity** | 3 years for FCY-denominated ECB                                                                        |
| **Annual limit**             | USD 3 million per financial year (under startup-specific automatic route) [VERIFY current limit]       |
| **End-use**                  | Capital expenditure, working capital, general corporate purposes (AD bank to approve specific end-use) |
| **Prohibited end-use**       | Real estate (non-infrastructure), personal consumption, equity investment in India                     |

**ECB vs. FEMA equity route comparison:**

| Aspect               | ECB (Cross-border Debt)       | FEMA Equity (FDI)  |
| -------------------- | ----------------------------- | ------------------ |
| Classification       | External debt                 | Capital instrument |
| RBI reporting        | ECB return                    | Form FC-GPR        |
| Repayment obligation | Yes — principal + interest    | No                 |
| Tenor                | Minimum 3 years (FCY)         | No requirement     |
| Tax treatment        | Interest deductible (company) | Dividend flexible  |
| Instrument           | Loan agreement, debentures    | CCPS, equity, CCD  |
| Investor type        | Lender (debt)                 | Equity investor    |
| Exit mechanics       | Loan repayment                | Share sale / IPO   |

---

### India Term Sheet Benchmark Table

Use this table to classify deal terms as MARKET, AGGRESSIVE (investor-favorable),
or FOUNDER-FAVORABLE relative to 2024-2025 India VC market practice.

| Term                         | FOUNDER-FAVORABLE         | MARKET STANDARD                        | AGGRESSIVE (Investor)           | Source                       |
| ---------------------------- | ------------------------- | -------------------------------------- | ------------------------------- | ---------------------------- |
| **Liquidation preference**   | None                      | 1× non-participating                   | 1× participating or 2×+         | India VC practice 2024       |
| **Anti-dilution**            | None                      | Broad-based weighted average (BWAA)    | Narrow-based or full ratchet    | Nishith Desai, AZB Partners  |
| **ESOP pool (pre-Series A)** | <8%                       | 10-15%                                 | >20%                            | India market norms 2024      |
| **Founder vesting**          | None                      | 4-year, 1-year cliff                   | 5-year, 2-year cliff            | India institutional practice |
| **Board composition**        | Founder majority          | 2 founder + 1 investor + 1 independent | Investor majority               | India Series A standard      |
| **Information rights**       | None                      | Q unaudited + annual audited + budget  | Monthly financials + full books | India VC practice            |
| **Valuation cap (iSAFE)**    | No cap                    | Negotiated per deal                    | Below FMV at issuance           | Market dependent             |
| **Pro-rata rights**          | None                      | Lead investor only (1× pro-rata)       | All investors get pro-rata      | India standard               |
| **ROFR**                     | None                      | ROFR on secondary sales                | ROFR + ROFO                     | India institutional          |
| **Co-sale / tag-along**      | None                      | Co-sale on major exits                 | Co-sale on all transfers        | India standard               |
| **Drag-along**               | Triggered at >75% holders | Triggered at >50-75% holders           | Triggered at >25% investors     | India VC practice            |
| **Redemption**               | None                      | None for standard CCPS                 | 3-year put right at 2×          | Rare; flag if present        |

#### Key Term Deep Dives

**ROFR (Right of First Refusal):**
If a founder or existing shareholder proposes to sell shares to a third party, the
ROFR holder can acquire the shares **at the same price and terms as the third-party
offer**. Process: (1) Founder notifies investors with third-party offer terms;
(2) Investors have X days (typically 20-30 business days) to match; (3) If investors
do not match, founder may proceed with third-party sale.

**Co-Sale (Tag-Along):**
Allows minority CCPS holders to sell a pro-rata proportion of their shares alongside
a founder or major shareholder exit. Protects minority investors from being left behind
after a founder exit.

**Drag-Along:**
Compels all shareholders to accept a sale approved by holders of a specified
percentage (commonly 50-75% of shares on an as-converted basis). Enables clean exits
by preventing minority holdout. Typical carve-outs: drag price must meet minimum
return hurdle for investors; drag cannot require investors to accept non-cash
consideration without consent.

**Founder Vesting (Post-Seed Standard):**

```
4-year vesting, 1-year cliff:
  - Month 0-11: 0% vested (cliff period)
  - Month 12: 25% vested (cliff vest)
  - Month 13-48: Remaining 75% vests monthly (2.083% per month)
  - Total at 4 years: 100% vested

Acceleration provisions:
  - Single-trigger (change of control only): Unusual; founder-favorable
  - Double-trigger (change of control + without-cause termination): Market standard
  - 100% acceleration on double-trigger: Common in Series A+ rounds
```

---

### Exit Analysis Framework

#### SEBI ICDR IPO Eligibility

For a startup planning an IPO on NSE/BSE Mainboard:

| Requirement                            | Threshold                                              | Notes                                             |
| -------------------------------------- | ------------------------------------------------------ | ------------------------------------------------- |
| **Positive operating profit (EBITDA)** | At least 3 of last 5 financial years                   | Pre-tax operating profit before exceptional items |
| **Minimum average operating profit**   | ₹15 crore average over 3 of last 5 years               | [VERIFY current SEBI ICDR threshold]              |
| **Minimum paid-up capital post-issue** | ₹10 crore                                              |                                                   |
| **Minimum market cap at listing**      | ₹25 crore                                              |                                                   |
| **Net tangible assets**                | ₹3 crore in each of last 3 years                       | <50% must be non-monetary                         |
| **Promoter contribution**              | Minimum 20% of post-issue equity                       | Locked in for 18 months                           |
| **Minimum public offer**               | 25% of post-issue equity (if market cap <₹1,600 crore) | Varies with market cap band                       |

**SME IPO (NSE Emerge / BSE SME):**

- Reduced EBITDA requirement: ₹1 crore in 2 of last 3 years
- Maximum post-issue paid-up capital: ₹25 crore
- Suitable for earlier-stage profitable startups

#### IPO Lock-Up Periods

| Holder                          | Lock-Up Period                         | Notes                                       |
| ------------------------------- | -------------------------------------- | ------------------------------------------- |
| Promoter (minimum 20%)          | **18 months** from listing date        | Cannot sell until lock-up expiry            |
| Promoter (above 20% threshold)  | **6 months** from listing date         | Standard SEBI ICDR requirement              |
| Pre-IPO institutional investors | **6 months** from listing date         | Applies to pre-IPO CCPS converted to equity |
| ESOP holders                    | Typically **6 months** from listing    | Subject to company policy                   |
| Anchor investors                | 50% locked 30 days; 50% locked 90 days | Per SEBI ICDR Regulations 2018              |

[VERIFY current lock-up provisions against SEBI ICDR as amended to 2025-26. SEBI is
consulting on relaxations for non-promoter pre-IPO investors — monitor finalization]

#### Reverse Flip Analysis

Many India-founded startups incorporate in foreign jurisdictions (Delaware, Cayman,
Singapore) for easier access to US/international VC. A **reverse flip** is the process
of relocating the parent entity back to India for an Indian IPO.

**Fast-track process (effective September 17, 2024):**

- Foreign holding company can **merge into its Indian wholly-owned subsidiary** using
  MCA fast-track merger (Section 233 of Companies Act 2013, as amended)
- **No NCLT approval required** for inbound cross-border mergers under fast-track route
- **RBI approval required** (FEMA implications of restructuring)
- **Timeline**: Approximately **90-120 days** (vs. prior 8-12 months through NCLT)

**Regulatory incentives post-reverse flip:**

- Shares arising from CCPS/CCD conversion count toward promoter minimum contribution
- OFS exemption: 1-year pre-IPO holding period waived for converted security holders
- SEBI ICDR timeline clock can start from Indian entity's earlier history (in certain
  circumstances — [VERIFY])

**Real market examples (2024-2025)**: Dream Sports (Dream11), Razorpay, Zepto, PhonePe,
Pine Labs, Groww, and Meesho have publicly announced or completed reverse flips in
advance of planned Indian IPOs.

---

## Severity Classification System

Use this 4-tier system to classify issues identified in the analysis:

| Tier | Label                  | Description                                                                                                                              | Action Required                                                                 |
| ---- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 🟢   | **COMPLIANT / MARKET** | Term is in line with India market standard or regulatory requirement. No action needed.                                                  | Note for awareness only                                                         |
| 🟡   | **FLAG / NEGOTIATE**   | Term deviates from market standard in one party's favor, or regulatory risk is present but manageable.                                   | Generate specific redline / remediation step                                    |
| 🔴   | **RISK / ESCALATE**    | Material deviation from market standard, significant regulatory exposure, or legal defect. Requires negotiation or counsel review.       | Explain risk, provide market-standard alternative, recommend escalation         |
| ⚫   | **CRITICAL / BLOCK**   | Violation of mandatory Indian law (FEMA, Companies Act, SEBI), deal-blocker, or fundamental structural defect. Cannot be accepted as-is. | Block — must be corrected before proceeding; flag legal and regulatory exposure |

**Auto-trigger CRITICAL classification for:**

- Issue price below FMV for foreign investor without FEMA justification
- Form FC-GPR not filed within 30-day deadline (compounding exposure)
- CCPS terms purporting to have fixed tenor exceeding Companies Act maximum
- Anti-dilution adjustment that would drive conversion price below FEMA FMV floor
- Participating liquidation preference >2× without explicit investor justification
- Drag-along triggerable by < 25% of shares without court-equivalent protection
- ESOP grant not authorized by special resolution under Companies Act Section 62(1)(b)
- Section 80-IAC claimed without valid DPIIT recognition certificate in place

---

## Prioritization Framework

When multiple issues are identified, prioritize as follows:

| Priority               | Tier               | Examples                                                                                                     | Timing                                   |
| ---------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **P1 — Immediate**     | CRITICAL           | FEMA non-compliance, missing FC-GPR filing, mandatory conversion terms violating Companies Act               | Must resolve before deal close           |
| **P2 — Pre-Close**     | RISK / ESCALATE    | Participating liquidation preference, missing DPIIT recognition for 80-IAC benefit, aggressive anti-dilution | Resolve in negotiation before signing    |
| **P3 — Pre-Allotment** | FLAG / NEGOTIATE   | ESOP pool sizing, board composition imbalance, information rights scope                                      | Negotiate; fallback positions acceptable |
| **P4 — Monitor**       | COMPLIANT / MARKET | Standard terms in line with market; FEMA compliance timeline tracking (30-day FC-GPR)                        | Log and monitor compliance deadlines     |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before
delivering.

| Gate           | Rule                                                                                                                | Fail Action                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, SEBI notification, RBI circular, or DPIIT notification                  | Add citation or mark [UNVERIFIED]      |
| **Format**     | Citations follow consistent format: Statute Name, Year, Section/Rule number                                         | Standardize format                     |
| **Currency**   | All cited provisions checked for amendments (Finance Acts amend IT Act annually; SEBI/RBI issue frequent circulars) | Flag [CHECK CURRENCY]                  |
| **Domain**     | Analysis stays within India law scope; no US/UK law principles applied as universal                                 | Remove or flag out-of-scope provisions |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                           | Add confidence qualifier               |

### Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL (⚫), apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the risk classification follow logically from
the cited statutory provision? Would SEBI/RBI/CBDT actually take the position described?
Check for recent amendments or regulatory relaxations that might change the analysis.

**Pass 2 — Completeness**: Have all relevant statutes been considered? FEMA, Companies
Act, Income Tax Act, and SEBI regulations often interact — an issue that appears
CRITICAL under one framework may be resolved under another (e.g., a FEMA pricing
deviation may be cured by compounding with RBI).

**Pass 3 — Challenge**: What is the strongest argument that the CRITICAL classification
is too aggressive? Are there RBI/SEBI notifications or circulars that provide
relaxation? What remediation path exists if the issue cannot be avoided?

### Confidence Scoring

| Level        | Range     | Meaning                                                                   | Action                                                   |
| ------------ | --------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled Indian law; black-letter statute                                  | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong regulatory authority; minor interpretation questions               | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments; recent amendments or RBI/SEBI positions not fully settled | State with reasoning; flag for professional verification |
| **Possible** | 0.40-0.59 | Genuinely uncertain; conflicting guidance                                 | Flag for professional review with both sides             |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative interpretation                                    | Do not assert; flag [UNCERTAIN]                          |

---

## Anti-Patterns

The following are the most common mistakes in India venture financing — what NOT to do:

1. **Missing Form FC-GPR filing deadline**: Filing FC-GPR after 30 days of allotment
   triggers compounding penalties. FEMA violation stays on record. _Fix: File within
   25 days of allotment to have a 5-day buffer._

2. **Using outdated valuation certificate**: Using a DCF or FMV certificate from a
   prior round for a new CCPS issuance. FEMA Rule 21 requires fresh valuation within
   90 days of allotment. _Fix: Obtain fresh valuation certificate for every new
   foreign investor round._

3. **Conflating angel tax abolition with FEMA FMV requirement**: Angel tax (Section
   56(2)(viib)) is abolished — but this does not remove the FEMA FMV floor for foreign
   investors. _Fix: Continue FEMA FMV compliance regardless of angel tax status._

4. **Claiming 80-IAC without DPIIT recognition in place**: Section 80-IAC requires
   valid DPIIT recognition as of the fiscal year of the claim. _Fix: Apply for DPIIT
   recognition before the first profitable year to ensure eligibility._

5. **Over-sized ESOP pool at pre-seed stage**: Creating a >20% ESOP pool pre-Series A
   excessively dilutes founders and makes the cap table unattractive to institutional
   investors. _Fix: Target 10-15% ESOP pool; refresh at Series A._

6. **Participating liquidation preference accepted without modeling**: Founders
   accepting participating CCPS terms without modeling the waterfall impact at exit.
   Participating liquidation preference can result in investors capturing 2-3× their
   invested capital before founders see proceeds. _Fix: Always model the exit waterfall
   for target exit scenarios before signing._

7. **Anti-dilution without FEMA floor analysis**: BWAA anti-dilution adjustments must
   result in a conversion price not below FEMA FMV at the time of conversion. _Fix:
   Always verify that post-adjustment conversion price ≥ FMV at exercise date._

8. **Missing AD bank relationship at deal close**: If the company has no existing
   relationship with an AD Category-I bank, FC-GPR filing is impossible. _Fix:
   Establish AD bank relationship before foreign investor wire; this takes 2-4 weeks._

9. **Failing to obtain FIRC from AD bank**: Foreign Inward Remittance Certificate
   (FIRC) is required for FC-GPR filing. If the AD bank does not issue a FIRC
   spontaneously, it must be requested. _Fix: Request FIRC from AD bank as soon as
   foreign wire is received._

10. **Treating CCPS conversion as a taxable event**: Some founders and investors
    mistakenly treat CCPS-to-equity conversion as a taxable transfer. Under Section
    47 of the Income Tax Act, conversion of preference shares to equity shares is not
    a transfer. _Fix: Confirm tax treatment with a CA before modeling investor returns._

11. **Using iSAFE for a round that requires defined ownership**: iSAFE defers
    valuation and ownership definition. If the investor needs defined CCPS ownership
    immediately (e.g., for SEBI AIF reporting or fund books purposes), iSAFE may not
    be appropriate. _Fix: Use priced CCPS when defined ownership is required._

12. **Not planning 80-IAC year selection strategically**: Founders assume they should
    claim 80-IAC from Year 1. If Year 1 is loss-making, the benefit is wasted. _Fix:
    Model projected profitability across the 10-year window; claim in the highest-
    profit consecutive years._

13. **Drag-along at dangerously low threshold**: A drag-along triggered at 25% of
    shares creates an existential risk that a small minority can force a sale of the
    company. _Fix: Set drag threshold at ≥50-75% of shares on a fully diluted basis._

14. **Reverse flip timing failure**: Starting the reverse flip process 30 days before
    an IPO roadshow. The fast-track MCA process still requires 90-120 days. _Fix:
    Initiate reverse flip 6-9 months before target IPO listing._

15. **SEBI AIF angel fund investing in ineligible startup**: Angel funds under SEBI
    AIF Regulations can only invest in DPIIT-recognized startups or companies meeting
    AIF eligibility criteria (< 10 years, turnover < ₹100 crore). _Fix: Verify
    eligibility of investee company before angel fund deployment._

16. **Ignoring Form FC-TRS on secondary transfers**: When a foreign investor sells
    shares to another entity (resident or non-resident), FC-TRS must be filed within
    60 days. Secondary transactions are commonly delayed. _Fix: Build FC-TRS
    compliance into the secondary share purchase agreement._

17. **Not modeling SEBI ICDR eligibility before late-stage round**: A startup that
    raises at a high valuation with participating liquidation preference may find its
    SEBI ICDR promoter contribution and OFS mechanics are complicated at IPO. _Fix:
    Model IPO eligibility at Series B+ to avoid structural issues._

18. **Assuming ECB is freely available**: ECBs for startups require DPIIT recognition,
    and end-use restrictions apply. Foreign working capital debt is not automatically
    available even to high-growth startups. _Fix: Confirm DPIIT recognition status
    and consult AD bank before initiating ECB discussions._

---

## Writing Standards

Before delivering any output under this skill:

**Plain Language Gates:**

- [ ] Every regulatory provision cited includes its plain-language meaning
- [ ] No unexplained acronyms (FEMA, NDI, FC-GPR, CCPS, CCD, AIF, ICDR, DPIIT,
      BWAA are spelled out on first use)
- [ ] Rupee amounts accompanied by USD equivalents where material (₹ crore conversions)
- [ ] RBI/SEBI citation format: "Regulation Name, Year, Regulation/Rule/Schedule number"
- [ ] All [VERIFY] tags are visible to the reader and not buried

**Precision Gates:**

- [ ] No general statement of India law without statutory citation or [VERIFY] tag
- [ ] Regulatory thresholds (₹5 crore, ₹100 crore, 30-day deadline) stated precisely
- [ ] Confidence level stated for each key analytical conclusion
- [ ] FEMA and Income Tax Act implications stated separately (they are different regimes
      and common sources of conflation)

**Completeness Gates:**

- [ ] Every CRITICAL issue has a specific remediation path
- [ ] Exit waterfall modeled for at least one scenario if a term affects exit economics
- [ ] Compliance calendar items (FC-GPR 30 days, FC-TRS 60 days) flagged explicitly

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for: latest RBI Master Directions, SEBI AIF notifications, Finance Act
  amendments, DPIIT startup recognition circulars, SEBI ICDR amendments
- Verify all statutory thresholds (₹ amounts, day counts, percentage caps) against
  current text
- Search for recent SEBI enforcement orders or RBI compounding orders related to FEMA
  non-compliance in startup rounds
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using research embedded in this skill
- Mark all statutory references with [VERIFY]
- Recommend that user verify: (a) current FEMA sector caps, (b) current SEBI AIF
  corpus and per-company investment limits, (c) current Form FC-GPR penalty schedule,
  (d) Finance Act 2025 80-IAC extension text
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-venture-financing-in"
  mode: "Created from scratch — India jurisdiction"
  topic: "India venture financing (iSAFE/CCPS/CCD/FEMA/DPIIT/Section 80-IAC/SEBI AIF)"
  jurisdiction: "India"
  source_skills_analyzed: 0
  enhancement_type: "Create"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  deal_details:
    investor_type: "[resident / foreign / mixed]"
    instrument: "[iSAFE / CCPS / CCD / equity]"
    stage: "[pre-seed / seed / Series A / Series B+]"
    fema_applicable: "[yes / no]"
    dpiit_recognized: "[yes / no / pending]"
    section_80iac_eligible: "[yes / no / check required]"
  compliance_calendar:
    fc_gpr_deadline: "[Date: within 30 days of allotment]"
    fc_trs_deadline: "[Date: within 60 days of transfer]"
    valuation_certificate_expiry: "[Date: 90 days from certificate date]"
  limitations:
    - "[Scope limitations, assumptions, FEMA provisions requiring independent verification]"
    - "SEBI AIF September 2025 regulations — verify Second Amendment notification"
    - "Finance Act 2025 80-IAC extension — verify final Finance Act text"
    - "RBI ECB startup limits — verify latest Master Direction annual update"
  reviewer: "AI-assisted — requires qualified India legal counsel, CA, and Company Secretary review"
```

---

## Output Format Template

```markdown
# India Venture Financing Analysis

**Company**: [Name]
**Date**: [Date]
**Instrument**: [iSAFE / CCPS / CCD / Priced Equity]
**Stage**: [Pre-seed / Seed / Series A / Series B+]
**Investor Type**: [Resident / Foreign / Mixed]
**FEMA Applicable**: [Yes / No]
**DPIIT Recognition Status**: [Yes / No / Pending]
**Prepared by**: AI-assisted analysis (Legalcode India Venture Financing Skill v1)

> ⚠️ **Not legal advice.** Review with qualified Indian counsel, a SEBI-registered CA,
> and a Company Secretary before taking action.

---

## Executive Summary

[2-4 sentences: instrument chosen, key India-specific issues, FEMA compliance status,
top 1-2 action items]

## Compliance Snapshot

| Item                       | Status                                      | Deadline / Action                 |
| -------------------------- | ------------------------------------------- | --------------------------------- |
| FEMA applicable            | [Yes/No]                                    | —                                 |
| Form FC-GPR filing         | [Required / Not required / Filed / Pending] | [Date: 30 days from allotment]    |
| Valuation certificate      | [In place / Needed / Outdated]              | [Freshness check: within 90 days] |
| DPIIT recognition          | [Active / Applied / Not obtained]           | [Impact on 80-IAC]                |
| Section 80-IAC eligibility | [Eligible / Ineligible / Verify]            | [Recommended year selection]      |
| Angel tax                  | [Not applicable (abolished FY 2025-26)]     | —                                 |

## Instrument Analysis

### [Instrument Name]

**Structure**: [Legal form — CCPS under Companies Act 2013, Section 55 / etc.]
**FEMA treatment**: [Capital instrument / Debt / Mixed]
**Conversion trigger**: [Qualified IPO / Qualified financing / Time-based / etc.]
**Tax at conversion**: [Section 47 — not a transfer / Other]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]

## FEMA Compliance Analysis

[Pricing rule (Rule 21), valuation certificate status, FC-GPR filing plan, sector caps]

## Term Sheet Analysis

| Term                   | Proposed | India Market Standard | Classification                    | Recommended Action           |
| ---------------------- | -------- | --------------------- | --------------------------------- | ---------------------------- |
| Liquidation preference | [X]      | 1× non-participating  | [MARKET / FLAG / RISK / CRITICAL] | [Specific redline or accept] |
| Anti-dilution          | [X]      | BWAA                  | [MARKET / FLAG / RISK / CRITICAL] | [Specific redline or accept] |
| [Additional terms...]  |          |                       |                                   |                              |

## Issues Found

### [Issue 1] — [🟢 / 🟡 / 🔴 / ⚫] [MARKET / FLAG / RISK / CRITICAL]

**Provision**: [Term or regulatory requirement]
**Issue**: [Specific problem — FEMA non-compliance / below market / structural defect]
**Impact**: [Commercial or legal consequence]
**Recommended action**: [Specific redline / filing action / restructuring step]
**Confidence**: [Level]

[Repeat for each issue]

## Tax Benefit Analysis

**Section 80-IAC**: [Eligible / Ineligible / Verify — with reason]
**Recommended year selection**: [Specific recommendation]
**Angel tax status**: Abolished — not applicable FY 2025-26 onwards

## DPIIT Recognition

**Current status**: [Active / Pending / Not obtained]
**Recommendation**: [Apply immediately / Maintain / N/A]
**Benefits unlocked**: [80-IAC / ECB automatic route / IPR fast-track / etc.]

## SEBI AIF Analysis (if applicable)

**Angel fund eligibility**: [Eligible / Ineligible]
**Key parameters**: [Corpus, investor count, per-company limits]
**September 2025 restructuring impact**: [If applicable]

## Exit Scenario Analysis (if applicable)

**IPO path**: [SEBI ICDR eligibility, lock-up analysis]
**Reverse flip**: [Required / Not required — with timeline]
**Secondary transaction**: [FEMA pricing, FC-TRS, deferred consideration]

## Compliance Calendar

| Action                          | Deadline                              | Responsible Party               |
| ------------------------------- | ------------------------------------- | ------------------------------- |
| File Form FC-GPR                | [Date: 30 days from allotment]        | Company + AD bank               |
| Renew valuation certificate     | [Date: 90 days from certificate date] | CA / Merchant Banker            |
| File Form FC-TRS (if secondary) | [Date: 60 days from transfer]         | Transferee/Transferor + AD bank |
| Claim Section 80-IAC            | [Fiscal year of claim]                | Company + Tax counsel           |
| DPIIT recognition renewal       | [Date if applicable]                  | Company                         |

## Glass Box Audit Trail

[Paste populated YAML template from above]

## Recommended Next Steps

1. [Immediate action — FEMA / DPIIT / tax]
2. [Pre-close negotiation items]
3. [Post-close compliance calendar]
4. [Professional review requirements — specify: Indian VC counsel, CA, Company Secretary]
```

---

## Localization Notes

This skill is **India-specific** and does not use jurisdiction-agnostic markers.
All statutory references are to Indian law.

**Key India-specific terminology used in this skill:**

| Term          | Meaning                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------- |
| **CCPS**      | Compulsorily Convertible Preference Shares (Companies Act 2013, Section 55)                        |
| **CCD**       | Compulsorily Convertible Debentures (Companies Act 2013, Section 71)                               |
| **iSAFE**     | India Simple Agreement for Future Equity — CCPS-based instrument introduced by 100X.VC (2019)      |
| **FEMA**      | Foreign Exchange Management Act, 1999                                                              |
| **NDI Rules** | FEMA (Non-Debt Instruments) Rules, 2019                                                            |
| **FC-GPR**    | Form Foreign Currency Gross Provisional Return — RBI form for FDI in Indian equity                 |
| **FC-TRS**    | Form Foreign Currency Transfer of Shares — RBI form for cross-border secondary share transfers     |
| **FIRMS**     | Foreign Investment Reporting and Management System — RBI's online portal for FEMA filings          |
| **AD Bank**   | Authorized Dealer Category-I Bank — commercial bank authorized by RBI to handle foreign exchange   |
| **FIRC**      | Foreign Inward Remittance Certificate — proof of foreign funds receipt issued by AD bank           |
| **DPIIT**     | Department for Promotion of Industry and Internal Trade                                            |
| **BWAA**      | Broad-Based Weighted Average Anti-Dilution — anti-dilution formula using fully-diluted share count |
| **SEBI AIF**  | SEBI (Alternative Investment Funds) Regulations, 2012 — regulates venture capital and angel funds  |
| **SEBI ICDR** | SEBI (Issue of Capital and Disclosure Requirements) Regulations, 2018 — governs IPO eligibility    |
| **80-IAC**    | Section 80-IAC, Income Tax Act 1961 — 3-year startup profit tax exemption                          |
| **ECB**       | External Commercial Borrowings — cross-border debt under RBI framework                             |
| **Crore**     | ₹1 crore = ₹10 million = approximately USD 120,000 (at ₹83/USD; verify current rate)               |
| **Lakh**      | ₹1 lakh = ₹100,000 = approximately USD 1,200 (at ₹83/USD)                                          |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Deep legal research via automated agent team across 10 India venture financing
  topic areas (2024-2025 sources)
- Primary sources: RBI Master Directions, SEBI AIF Regulations and September 2025
  Second Amendment, FEMA NDI Rules 2019, Finance Act 2024 (angel tax abolition),
  Union Budget 2025-26 (80-IAC extension), SEBI ICDR Regulations 2018 (as amended),
  Companies Act 2013 (Sections 42, 55, 62, 71), Income Tax Act 1961 (Sections 47,
  56(2)(viib), 80-IAC), DPIIT startup recognition framework
- Secondary sources: Nishith Desai Associates, AZB & Partners, Cyril Amarchand
  Mangaldas (published guidance), Vinod Kothari Consultants, KPMG India, India
  Briefing, Legal500 India, Mondaq India, 100X.VC, Square Peg VC
- Reference standard: `legalcode-contract-review` (structural and quality framework
  patterns); `legalcode-venture-financing-suite` (India track context)
- Attribution: Legalcode original synthesis; not imported from any external repository
