---
name: legalcode-term-sheet-analysis
description: >
  Deep analysis of venture capital term sheets across three dimensions: economics
  (pre/post-money valuation, option pool dilution, liquidation preference multiples
  and participation mechanics, pay-to-play provisions, anti-dilution weighted-average
  vs. full-ratchet), control (board composition, protective provisions and veto rights,
  drag-along/tag-along, information rights, registration rights), and other terms
  (founder vesting and acceleration, ESOP allocation, exclusivity, no-shop, conditions
  precedent). Evaluates each term against market benchmarks by stage (seed, Series A–D)
  and identifies investor-favorable vs. founder-favorable deviations. Models cap table
  dilution and founder economics across multiple exit scenarios. Produces dual-perspective
  annotated analysis (founder view and investor view for every material term) with
  confidence-scored negotiation recommendations and a Glass Box audit trail.
  Use when reviewing VC term sheets for founders, legal counsel, or investors in
  US, UK, or Indian jurisdictions. Jurisdiction-agnostic base with [JURISDICTION-SPECIFIC]
  markers for US (Delaware), UK (BVCA model), and India (SEBI AIF/Companies Act).
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Term Sheet Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted venture capital term
> sheet analysis. It does not constitute legal advice or investment advice. All outputs
> should be reviewed by a qualified legal professional licensed in the relevant jurisdiction
> and experienced in venture financings before use. Market benchmarks cited reflect general
> trends and should be verified against current data sources before relying on them.
> References to NVCA, BVCA, SEBI, or other model documents carry data-currency risk —
> verify the latest edition before relying on them. AI-generated analysis may contain
> errors in financial modeling, cap table arithmetic, or benchmark comparisons — verify
> all quantitative outputs independently.

---

## Purpose and Scope

This skill analyses venture capital term sheets holistically. It identifies whether each
material term is founder-favorable, market-standard, or founder-dilutive; models founder
economics under multiple exit scenarios; and generates a dual-perspective negotiation
strategy (founder view and investor view for every material term).

**Covers:**
- Full economics analysis: valuation, option pool dilution, liquidation preference structure
  and waterfall, pay-to-play provisions, anti-dilution mechanics, and scenario modeling
  across three exit outcomes
- Control and governance analysis: board composition, protective provisions (veto rights),
  drag-along/tag-along, information rights, registration rights, and founder removal risk
- Founder and employee economics: vesting schedule, cliff, acceleration triggers,
  ESOP allocation and refresh mechanics
- Other material terms: ROFR/co-sale, exclusivity and no-shop, conditions precedent,
  representations and warranties
- Multi-round interaction analysis: how current terms cascade into Series B/C and affect
  future fundraising, employee retention, and exit optionality
- Missing provisions detection: flagging absent terms that market-standard term sheets
  include at this stage
- Market benchmarking against NVCA standard (US), BVCA model (UK), and AIF market
  norms (India) by round stage (seed, Series A–D)
- Dual-perspective framing for every material term (founder view and investor view)
- Confidence-scored redline recommendations with tiered negotiation strategy

**Does not:**
- Provide legal advice or replace qualified VC counsel
- Draft a term sheet from scratch — see `legalcode-saas-agreement-drafter` or
  `legalcode-master-services-agreement` for drafting skills
- Review definitives (stock purchase agreement, charter, voting agreement, ROFR
  co-sale agreement) — this skill analyses the indicative term sheet only
- Assess deal economics from the investor's fund return perspective (LTV/CAC, IRR,
  portfolio construction) — this skill focuses on founder and company economics

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at the base layer, with three jurisdiction-specific
tracks for US, UK, and India. The governing law clause in the term sheet (or the
incorporation jurisdiction) determines which track to engage.

**US (Delaware primacy)**
[JURISDICTION-SPECIFIC] The overwhelming majority of US VC-backed companies are Delaware
corporations governed by the Delaware General Corporation Law (DGCL). Most US term sheet
analysis applies NVCA Model Legal Documents (latest edition, October 2025 update) as the
benchmark. Key US-specific considerations:
- Liquidation preference enforceability under DGCL § 151
- Anti-dilution adjustments treated as recapitalizations for tax (IRC § 305)
- IRC § 280G golden parachute screening for founder acceleration on change of control
- Section 409A valuation requirements for founder option pricing
- Investment Company Act exemption (Section 3(c)(1) or 3(c)(7) for the fund)
- Delaware court fiduciary duty analysis for board composition and drag-along rights
  (Trados, SolarCity, Corwin doctrine)

**UK**
[JURISDICTION-SPECIFIC] UK VC deals typically use BVCA Model Documents for Early Stage
Investments (February 2025 edition). Key UK-specific considerations:
- UK companies incorporated under Companies Act 2006 (not DGCL)
- BVCA model defaults to 1× non-participating liquidation preference (same as NVCA)
- Anti-dilution formula in February 2025 BVCA update defaults to broad-based weighted
  average ratchet — consistent with NVCA
- UK Enterprise Investment Scheme (EIS) / Seed Enterprise Investment Scheme (SEIS)
  tax relief compatibility: EIS/SEIS eligibility can constrain term structure (no
  cumulative preference dividends, no guaranteed return provisions)
- Articles of Association govern preference rights (not a separate charter amendment
  as in Delaware)
- Material adverse change clauses governed by UK contract law and Companies Act 2006
- Employment rights: UK Employment Rights Act 1996 / Employment Rights Act 2025
  affect founder removal and vesting forfeit mechanics

**India**
[JURISDICTION-SPECIFIC] Indian VC deals are governed by a complex regulatory framework:
- Companies Act 2013 governs preference share rights, board composition, and shareholder
  agreements
- SEBI (Alternative Investment Funds) Regulations 2012 (as amended through 2024/2025)
  govern eligible fund structures; most institutional VCs operate as Category I or
  Category II AIFs
- SEBI AIF Regulations restrict certain preferred share structures (particularly those
  that look like debt instruments)
- Foreign Exchange Management Act (FEMA) / FEMA (Non-Debt Instruments) Rules 2019:
  restrict certain preference dividend and liquidation preference structures for
  foreign investors (automatic vs. approval-route thresholds)
- Reserve Bank of India (RBI) pricing guidelines: foreign investment into Indian
  startups must comply with pricing norms (DCF or net asset value)
- National Company Law Tribunal (NCLT) has jurisdiction over shareholder disputes
- Key India-specific norms: liquidation preference often structured as compulsorily
  convertible preference shares (CCPS) rather than participating preferred due to FEMA
  restrictions; anti-dilution typically weighted average

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid benchmark approaches exist (e.g., NVCA vs. BVCA vs. AIF norms)
- Ambiguity in the term sheet creates a fork only the user can resolve
- Existing cap table complexity creates interaction effects that need user confirmation
- Risk tolerance or business context is needed to classify severity correctly

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

### Step 1: Accept the Term Sheet

Accept the term sheet in any of these formats:
- **File**: PDF, DOCX, or other document format
- **URL**: Link to a term sheet in a document management system
- **Pasted text**: Term sheet text pasted directly into the conversation
- **Stage reference**: User states "this is a Series A term sheet" — ask for the document

If no term sheet is provided, prompt the user to supply one.

### Step 2: Gather Initial Context

**⟁ CLARIFY** — Before beginning, ask the user these questions (skip any already answered):

1. **Whose perspective?**
   - Options: **Founder / Company** (analyzing an investor's term sheet), **Lead Investor**
     (reviewing before sending), **Syndicate / Follow-on Investor** (reviewing a round
     you're joining), **Advisor / Counsel** (neutral analysis), **Other**
   - *Why this matters*: The entire analysis inverts depending on which side you represent.
     A liquidation preference that is GREEN for an investor is RED for a founder. Dual-
     perspective framing is mandatory but knowing the primary reader sharpens priorities.

2. **Round stage?**
   - Options: Pre-seed, **Seed**, **Series A**, **Series B**, **Series C+**
   - *Why this matters*: Market benchmarks differ fundamentally by stage. A 2× participating
     preference may be unusual at seed (where SAFE notes dominate) but standard at
     Series C distressed. Option pool expectations, board seat norms, and protective
     provision scope all scale with stage.

3. **Existing cap table complexity?**
   - Options: Simple (founding team only, no prior investors), Medium (seed investors with
     SAFE or priced notes, limited prior rights), Complex (multiple priced rounds with
     accumulated preferred rights, drag-along, anti-dilution, and existing board seats)
   - *Why this matters*: New terms interact with existing rights. A new Series A anti-
     dilution provision stacks on top of any existing seed anti-dilution. A new board seat
     shifts existing board dynamics. Failing to model this is the single most common
     term sheet analysis error.

4. **Jurisdiction / governing law?**
   - Options: US (Delaware corporation), UK (Companies Act 2006), India (Companies Act
     2013 / AIF), Other (specify), Unknown (I'll identify from the term sheet)
   - *Why this matters*: Delaware, UK, and India have different rules for preference share
     enforceability, anti-dilution mechanics, board removal, and regulatory constraints.

If the user provides partial context, proceed with what you have and **state your
assumptions explicitly** (e.g., "Assuming you are a founder reviewing an investor's
Series A term sheet under Delaware law — let me know if that's wrong").

### Step 3: Load Benchmarks or Playbook

Check for an organization-specific venture financing playbook (e.g., `venture-standards.md`
or similar configuration).

If no playbook is found:

**⟁ CLARIFY** — Inform the user and ask which benchmark to use:

- **Option A: NVCA Standard (US, Series A default)** — Use the NVCA Model Term Sheet
  (October 2025 edition) as the benchmark. Appropriate for most US early-stage deals.
- **Option B: BVCA Model Documents (UK)** — Use the BVCA Model Documents for Early Stage
  Investments (February 2025 edition). Appropriate for UK deals.
- **Option C: AIF market norms (India)** — Use Indian AIF regulatory framework and market
  practice as the benchmark.
- **Option D: Market-stage-adjusted** — I'll calibrate benchmarks to the specific round
  stage and geography based on available market data (PitchBook, Carta, Orrick benchmarks).
- **Option E: I'll tell you our standard positions as we go** — Start the analysis and
  I'll ask about your preferred position when it matters for each term.

If proceeding without a specific playbook, label the analysis clearly:
"Benchmarked against [NVCA Standard / BVCA Model / AIF market norms] for [stage] rounds
in [geography]. Not organizational positions."

### Step 4: Read the Term Sheet Holistically

Before analysing individual terms, read the entire term sheet for:
1. **Structure**: Is this a standard template (NVCA, BVCA, Y Combinator SAFE-extension)?
   Or a custom investor-drafted document?
2. **Round summary**: Investment amount, pre-money valuation, post-money valuation, and
   implied price per share
3. **Key interaction flags**: How does the liquidation preference interact with anti-
   dilution? How does the option pool affect fully-diluted ownership? Do protective
   provisions create operational vetoes?
4. **Missing provisions**: What does a market-standard term sheet include that this
   document does not?

Identify the governing law clause and activate the appropriate jurisdiction track.

### Step 5: Gather Jurisdiction-Relevant Authority

Read the governing law clause and identify the applicable jurisdiction. Then use
**legalcode-mcp** (if connected) to search for:
- Relevant statutes governing preference share rights in the identified jurisdiction
- Recent court decisions on drag-along, fiduciary duties, or anti-dilution enforceability
- Regulatory guidance (SEBI AIF, FCA, SEC) relevant to the fund structure

Save relevant findings to a local reference file at
`/tmp/legalcode-term-sheet-research.md`.

If legalcode-mcp is not connected, proceed with market research only and mark any
statutory references with [VERIFY].

### Step 6: Economics Analysis

Analyse the economics dimension in five sub-categories. For each finding, produce a
dual-perspective classification (see Classification System below).

#### 6.1 Valuation and Share Price

- Identify pre-money valuation, investment amount, and post-money valuation
- Verify share price calculation: investment ÷ pre-money valuation × total shares
- Identify whether the option pool is included in or added to pre-money valuation
  (pre-money pool inclusion dilutes founder; post-money addition dilutes all)
- Calculate founder ownership percentage post-close, fully diluted
- Compare implied valuation to recent comparable rounds at this stage and sector

**⟁ CLARIFY** (if valuation is ambiguous): "The term sheet states a pre-money valuation
of [X] but does not specify whether the option pool is included pre-money or post-money.
This difference can reduce founder ownership by 5–15%. Do you want me to: (A) Assume
pre-money pool inclusion (most common, more dilutive), (B) Assume post-money addition,
or (C) Flag it as a key item for legal clarification before signing?"

#### 6.2 Liquidation Preference Structure

Identify and classify the liquidation preference on five dimensions:

| Dimension | Description | Market Standard (Series A, US 2025) |
|-----------|-------------|--------------------------------------|
| Multiple | 1×, 2×, 3× or other | 1× (98% of Q2 2025 rounds per NVCA) |
| Participation | Non-participating, participating, or capped participating | Non-participating (55–60% Series A; market shifting toward parity) |
| Scope | Liquidation proceeds only, or includes dividends and redemptions | Liquidation proceeds (standard) |
| Priority | Senior to all other preferred, pari-passu, or junior | Senior to common; pari-passu with other preferred of same series |
| Trigger | Merger, acquisition, asset sale, IPO carve-out | M&A and asset sales standard; IPO typically does not trigger |

Model the liquidation preference in three exit scenarios:
- **Down exit** (50% of current valuation)
- **Flat exit** (at or near current valuation)
- **Up exit** (3× current valuation)

For each scenario, calculate: preference payout, remaining proceeds, founder share,
investor total return.

#### 6.3 Anti-Dilution Mechanics

Identify the anti-dilution provision type and scope:

| Type | Mechanism | Founder Impact | Market Standard |
|------|-----------|----------------|-----------------|
| None | No protection | Best for founder | Rare at Series A+ |
| Broad-based weighted average | Adjusts conversion price using all outstanding shares | Moderate dilution in down rounds | NVCA default; BVCA 2025 default |
| Narrow-based weighted average | Adjusts using only preferred shares outstanding | More dilutive than broad-based | Less common; sometimes in older deals |
| Full ratchet | Resets conversion price to new lower price entirely | Devastating in down rounds | ~22% of Series A (up from 12% in 2021; more common in down markets) |

Identify carve-outs from anti-dilution (standard carve-outs per NVCA):
- Shares issued under the stock option plan (up to a stated pool size)
- Shares issued as stock splits, dividends, or recapitalizations
- Shares issued to strategic partners, advisors, or vendors at board discretion
- Shares issued in connection with equipment leasing or bank financing

Model the anti-dilution impact in a down-round scenario (Series B at 50% of Series A
valuation) for all three anti-dilution types. Show founder ownership change for each.

#### 6.4 Option Pool

Identify the option pool on four dimensions:
1. **Pool size** as percentage of fully diluted shares, before or after this round
2. **Pool inclusion**: Is the pool included in the pre-money share count (dilutes founder)
   or added post-close (dilutes all)?
3. **Refresh mechanism**: Is the pool fixed at closing or refreshable at board discretion?
4. **Founder treatment**: Are founder shares subject to vesting or already vested?

Calculate fully-diluted ownership table with and without option pool.

#### 6.5 Pay-to-Play Provisions

Identify whether pay-to-play provisions are present:

Pay-to-play requires existing investors to participate in future down rounds or lose
some or all of their preferred stock privileges. Approximately 10% of Q2 2025 VC deals
include pay-to-play provisions (up from near-zero in 2021). The presence of pay-to-play
can signal that existing investors may be reluctant to participate in future rounds.

Assess: which investor rights are forfeited on non-participation (anti-dilution only?
all preferred rights? conversion to common?), and whether the threshold triggers are
fair to smaller investors.

### Step 7: Control and Governance Analysis

Analyse the control dimension in four sub-categories.

#### 7.1 Board Composition

Identify the board structure post-close:
- Total board size
- Investor-designated seats (lead investor, follow-on investors separately)
- Founder-designated seats
- Independent / neutral seats and appointment process
- Any board observer rights (non-voting; still provides information access)

Classify board control:

| Board Outcome | Classification | Notes |
|---------------|----------------|-------|
| Founder majority (e.g., 2F / 1I / 0N) | FOUNDER-FAVORABLE | Rare at Series A |
| Parity with neutral or founder-appointed neutral (e.g., 1F / 1I / 1N-founder-approved) | MARKET-STANDARD | Common at seed/Series A |
| Investor majority or investor-approved neutral (e.g., 1F / 2I / 1I-controlled) | FOUNDER-DILUTIVE | Escalate; requires negotiation or compensating founder veto |
| Full investor control (e.g., 0F / 3I) | FOUNDER-DILUTIVE / RED | Highly unusual at seed/Series A; major red flag |

Market standard at Series A: 2 founders / 1 investor / 1 independent (source: NVCA
2025; Orrick VC Report 2025 Q1).

#### 7.2 Protective Provisions (Investor Veto Rights)

List every action that requires investor consent under the protective provisions. Standard
NVCA protective provisions include:
- Amend or change rights of preferred stock
- Authorize or issue new equity or equity-equivalent securities
- Liquidate, dissolve, or wind up the company
- Acquire another company or material business
- Effect a change of control, merger, or asset sale
- Increase/decrease board size
- Incur debt above stated threshold
- Pay dividends on common stock
- Repurchase common stock (other than option buybacks at cost)
- Engage in a related-party transaction above stated threshold
- Change in business purpose or plan

**⟁ CLARIFY** if protective provisions include unusual operational controls (e.g., investor
consent on CEO hire, consent on annual budget, consent on key customer contracts): "The
protective provisions include [unusual term]. This gives investors veto over day-to-day
operations. Should I classify this as FOUNDER-DILUTIVE / RED, or do you want to negotiate
a carve-out?"

Flag as FOUNDER-DILUTIVE / RED any protective provision that:
- Requires investor consent for normal operations (hiring, budgeting, customer contracts)
- Allows a single investor to block a decision (super-majority or unanimous preferred
  required vs. majority preferred is more balanced)
- Does not sunset or diminish as the investor's ownership percentage decreases

#### 7.3 Drag-Along and Tag-Along Rights

**Drag-Along**: Allows the majority to force minority shareholders to join a sale.
- Who triggers: majority of preferred, majority of all shares, or board plus majority?
- Threshold: 50%, 60%, 66%, or 75% approval required?
- Protections for dragged shareholders: appraisal rights, right to separate counsel,
  guaranteed minimum price?
- Carve-outs: does drag-along apply to founders who are employees (employment termination
  risk if they refuse)?

Market standard: Drag-along triggered by board approval + majority of preferred +
majority of common (three-party consent). Single-class drag-along (preferred alone) is
FOUNDER-DILUTIVE.

**Tag-Along (Co-Sale)**: Allows minority to join a sale at the same price if majority sells.
- Scope: founder shares only? All common? Including transfer to third parties?
- Right of first refusal before tag-along triggers?
- Threshold for activation?

#### 7.4 Information Rights and Transparency Asymmetry

List every information right granted to investors:
- Quarterly financial statements (unaudited): threshold (e.g., investors holding >1%)
- Annual financial statements (audited or unaudited)
- Annual budget and operating plan
- Cap table (all shareholders, fully diluted)
- Board meeting materials (advance notice days)
- Material event notices (definition: customer loss, key hire/departure, regulatory inquiry)
- Right to inspect books and records

Flag information rights as FOUNDER-DILUTIVE if:
- No threshold on who receives (all investors, including micro-angels)
- No confidentiality obligation on information received
- No time limit on information retention or use
- "Any information reasonably requested" language (blank check)

Model information asymmetry: investor receives detailed financial and operational data;
founder receives none from the investor fund. Flag this as a structural asymmetry, not
a negotiating point.

### Step 8: Founder and Employee Economics

#### 8.1 Founder Vesting

Identify founder vesting schedule and acceleration:
- Standard: 4-year vesting with 1-year cliff (25% vests at month 12, then 1/48 per month)
- Does the term sheet impose or modify founder vesting? (common for founders with prior
  co-founder splits or founders who have been working < 1 year)
- Acceleration type:
  - No acceleration: Founder forfeits unvested shares on termination
  - Single-trigger: Full or partial acceleration on change of control (sale of company)
  - Double-trigger: Acceleration only if change of control AND termination without cause
    or resignation for good reason
- Market standard: 100% double-trigger acceleration (Fenwick & West data: 100% double-
  trigger is market, but many VCs accept 50% or 12-month acceleration as fallback)

#### 8.2 ESOP Allocation and Refresh

- ESOP size: % of fully diluted post-close
- Is the ESOP included in pre-money share count or created post-close?
- Refresh: fixed pool or refreshed at board discretion? (refresh without cap creates
  unlimited dilution risk for all other shareholders)
- Standard market ESOP at Series A: 10–15% fully diluted

#### 8.3 Employee Lockup and Transfer Restrictions

- Any restrictions on founder or key employee transfers before or after IPO?
- Post-IPO lockup period (standard: 180 days; longer is FOUNDER-DILUTIVE)
- ROFR on employee shares: does investor get first right if employee sells?

### Step 9: Other Material Terms

#### 9.1 Right of First Refusal and Co-Sale

- ROFR: if founder wants to sell shares, does investor get first right at same price?
- Co-sale: can investor join founder's sale on same terms?
- Market standard: Company ROFR first, then investor ROFR on waiver, then co-sale
- Flag if ROFR allows investor to block founder liquidity entirely

#### 9.2 Exclusivity and No-Shop

- Exclusivity period: how long? Standard: 30–45 days; longer is FOUNDER-DILUTIVE
- No-shop: prohibits founder from talking to other investors during exclusivity
- Expenses: if deal does not close, who pays diligence costs?
- Market standard: exclusivity for due diligence period only; founder can engage other
  investors for different rounds; expenses each party bears their own

#### 9.3 Conditions Precedent

- List every condition the investor must satisfy before closing
- List every condition the company must satisfy before closing
- Flag unusual conditions: governance changes, employment agreements for founders, IP
  assignments, key employee retention agreements, regulatory approvals
- Assess materiality and time-to-satisfy for each condition

#### 9.4 Representations and Warranties

- Company representations: cap table accuracy, IP ownership, regulatory compliance,
  no material litigation, financial statements
- Founder personal representations: authority to enter, no conflicts, IP contribution
- Flag unusually broad representations (e.g., "no material adverse change in any
  respect" without carve-outs for market conditions)

### Step 10: Detect Missing Provisions

Check for absent terms that market-standard term sheets include at this stage. For each:

| Missing Provision | Stage Expectation | Classification |
|-------------------|-------------------|----------------|
| Liquidation preference clause | All priced rounds | FOUNDER-DILUTIVE RED if absent (no investor protection) |
| Anti-dilution protection | Series A+ | MARKET-STANDARD to include; absence is unusual |
| Pro-rata rights (investor) | Series A+ | MARKET-STANDARD (87% of Series A per NVCA 2025) |
| Board observer rights | Seed+ | MARKET-STANDARD for larger investors |
| Information rights | Series A+ | MARKET-STANDARD |
| Drag-along / tag-along | Series A+ | MARKET-STANDARD |
| Founder vesting schedule | All rounds | MARKET-STANDARD to specify |
| ESOP pool size | All priced rounds | MARKET-STANDARD to state |
| No-shop / exclusivity | All rounds | MARKET-STANDARD |
| Registration rights | Series B+ | Optional at Seed/Series A; MARKET-STANDARD at Series B+ |
| Pay-to-play | Situational | Unusual at Seed; ~10% of Series A 2025; worth flagging |

### Step 11: Classify All Findings and Generate Redlines

#### Classification System

Every material term is classified from two perspectives:

**FOUNDER PERSPECTIVE**:
- **FOUNDER-FAVORABLE** (GREEN): Term is more favorable than market standard for this
  stage. Founder should preserve in negotiation; do not trade away without significant
  compensation.
- **MARKET-STANDARD** (YELLOW): Term aligns with market norms for this stage. Acceptable.
  No negotiation needed unless founder's risk tolerance or specific objectives conflict.
- **FOUNDER-DILUTIVE** (RED): Term is materially less favorable than market standard,
  or creates governance/economic risk materially worse than norm. Flag for negotiation
  or escalation.

**INVESTOR PERSPECTIVE**:
- **INVESTOR-FAVORABLE** (GREEN): Term provides stronger-than-standard investor
  protection. Investor should preserve.
- **MARKET-STANDARD** (YELLOW): Term is within normal investor expectations.
- **INVESTOR-RESTRICTIVE** (RED): Term is weaker than market investor protections.
  Investor counsel may flag.

For every FOUNDER-DILUTIVE finding, generate:
1. Current language (quoted from term sheet)
2. Why it is problematic (plain language, 1–2 sentences)
3. Proposed redline (specific alternative language)
4. Fallback position (what founder can accept if full redline is rejected)
5. Business impact (quantified where possible)
6. Market context (benchmark data with source and date)
7. Confidence level (see Confidence Scoring)

#### Prioritisation Framework (Tiers)

**Tier 1 — Must Address (Dealbreakers)**
Terms whose acceptance materially impairs founder governance, dilutes founder below
acceptable thresholds, or creates irreversible risk. Founder should not sign without
resolution. Examples: full-ratchet anti-dilution, investor board majority, participating
preference with high multiple, investor veto on operational decisions.

**Tier 2 — Should Address (High-Value Negotiation)**
Terms that are FOUNDER-DILUTIVE but not uncommon. Worth negotiating; fallback positions
exist. Examples: option pool percentage, exclusivity period length, information rights
scope without thresholds, drag-along triggering mechanics.

**Tier 3 — Concession Candidates (Nice to Have)**
Terms where founder has market leverage but is likely to trade away to gain on Tier 1.
Examples: board observer rights for micro-investors, ROFR thresholds, specific information
delivery timing.

**⟁ CLARIFY** (before generating redlines for borderline items): "The [Term] is on the
MARKET-STANDARD / FOUNDER-DILUTIVE border. At [this stage], [X]% of comparable rounds
include it. Do you want me to: (A) Accept as market-standard and move on, (B) Generate
a redline as Tier 2, or (C) Flag as Tier 3 concession candidate?"

### Step 12: Deliver Founder Impact Summary and Negotiation Strategy

After completing the analysis:

1. **Quantify founder impact**: post-close ownership %, projected Series B ownership,
   governance control score
2. **Model three exit scenarios** with final founder economics
3. **Sequence negotiation strategy**: "Lead with [Tier 1 terms], trade [Tier 3 terms]
   to win [Tier 1 terms], accept [Tier 2 terms] with fallback language"
4. **Flag multi-round interactions**: how current terms cascade into Series B/C
5. **List critical items for legal review** before signing
6. Append the **Glass Box audit trail**

---

## Deep Topic Analysis

### Economics Deep Dive

#### Liquidation Preference Waterfall

Model the liquidation preference as a waterfall with three tiers:
1. **Priority payments**: Debt, payroll, vendor payables
2. **Preferred stock preferences**: Series A (and any senior series), then earlier preferred
   series, then pari-passu series
3. **Common stock participation**: Remaining proceeds distributed to common shareholders
   (which may include converted preferred in non-participating structures)

For participating preferred, add a fourth calculation: preferred participation payout
from remaining proceeds after preference, on as-converted basis.

Work through the waterfall for each exit scenario. Show who receives what dollar amount
at each tier.

#### Anti-Dilution Worked Example

For a weighted-average anti-dilution clause, apply the formula:

```
NCP = OCP × (OS + SI) ÷ (OS + NS)

Where:
NCP = New Conversion Price
OCP = Old Conversion Price (Series A issue price)
OS  = Fully-diluted shares outstanding before new issuance
SI  = Shares issuable for full consideration at old conversion price
NS  = New shares actually issued (at lower price)
```

Work through the formula for a down-round scenario with the actual numbers from the
term sheet. Then compare to full-ratchet (NCP = new lower price, no weighting).

Show the difference in founder ownership percentage under both anti-dilution types.

#### Option Pool Dilution Modeling

Pre-money pool inclusion example:
- Pre-money valuation: $10M
- Investment: $2M
- New 10% option pool required (pre-money)
- Result: Pool is created from existing shares before investor buys in; founder absorbs
  all pool dilution; investor buys new shares at full $12M post-money valuation

Post-money pool addition example:
- Same valuation and investment
- 10% pool added post-close
- Result: Pool dilutes all shareholders proportionally (founder and investor share dilution)

Difference: Pre-money inclusion can reduce founder ownership by 5–15% more than post-
money addition, depending on pool size and round structure.

---

## Severity Classification Reference

| Finding Severity | Founder View | Investor View | Action Required |
|-----------------|--------------|---------------|-----------------|
| FOUNDER-FAVORABLE / INVESTOR-RESTRICTIVE | GREEN | RED | Preserve if founder; negotiate if investor |
| Founder-favorable / Investor-standard | GREEN | YELLOW | No action if founder; may negotiate if investor |
| MARKET-STANDARD (both sides) | YELLOW | YELLOW | Accept; no negotiation needed |
| Founder-standard / Investor-favorable | YELLOW | GREEN | May negotiate if founder; preserve if investor |
| FOUNDER-DILUTIVE / INVESTOR-FAVORABLE | RED | GREEN | Negotiate if founder; preserve if investor |
| FOUNDER-DILUTIVE / Investor-standard | RED | YELLOW | Must negotiate if founder |

---

## Citation and Benchmark Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every market claim cites a specific benchmark source (NVCA, BVCA, SEBI, PitchBook, Carta, Orrick VC Report) or a documented comparable round (company, stage, date, key terms) | Add source or mark "[UNVERIFIED — cite recent comparable round]" |
| **Format** | All market benchmark citations follow: "[Source] reports [X]% of [stage] rounds in [geography/period] include [term]" | Fix to standardised format |
| **Currency** | Every cited benchmark checked for data currency; market moved materially between 2021 (peak) and 2023 (trough) and 2025 (normalising); flag data older than 12 months | Flag as "[CHECK CURRENCY — collected [year]; current market sentiment is [up/neutral/down]]" |
| **Domain** | Analysis stays within VC term sheet context; US DGCL statutes, UK Companies Act, and SEBI AIF regulations are flagged as "regulatory backdrop" not "market benchmarks"; NVCA models not conflated with contract law precedent | Separate market norms from regulatory requirements; flag when regulatory risk enters |
| **Confidence** | Uncertainty explicitly stated; if benchmark is based on <50 rounds, flag low sample size; if market has shifted since data collection, note it | Add confidence level with reasoning; never state "market standard" without data |

---

## Self-Interrogation for Tier 1 Findings

For every FOUNDER-DILUTIVE finding classified as Tier 1 (Must Address), apply this
three-pass adversarial review:

**Pass 1 — Market Chain Integrity**: Does the RED classification follow logically from
the benchmark data? Would a VC counsel with 20 years of Series A experience agree this
is out-of-market? Could this term be contextually acceptable for this specific deal
(investor type, sector, founder background)?

**Pass 2 — Completeness**: Have all relevant market data sources been considered? Are
there compensating terms elsewhere in the term sheet that mitigate this finding
(e.g., higher than normal liquidation threshold mitigated by stronger anti-dilution)?

**Pass 3 — Challenge**: What is the investor's strongest argument for this term? Under
what circumstances might a reasonable founder accept it? What trade-off would make this
term acceptable?

---

## Confidence Scoring

Confidence scoring for market-benchmark assertions (not legal certainty):

| Level | Range | Market Characteristic | Prescribed Action |
|-------|-------|----------------------|-------------------|
| **Definite** | 0.95–1.0 | Universal consensus; >95% of comparable rounds include it; documented in multiple independent benchmarks with convergent data; included in NVCA/BVCA model as default | State with confidence: "This is market standard." |
| **High** | 0.80–0.94 | Strong consensus; 80–95% prevalence; documented in multiple benchmarks; occasional investor deviations; in NVCA/BVCA model or near-equivalent | State with brief caveat: "Standard in most comparable rounds, though some investors negotiate." |
| **Probable** | 0.60–0.79 | Consensus with material variance; 60–79% prevalence; documented but with notable variance by investor type, stage, or market conditions; noted as alternative in NVCA/BVCA | State with reasoning and contra-indicators: "Common in [X]% of rounds, less common in [Y situation]." Offer fallback. |
| **Possible** | 0.40–0.59 | Market split; 40–59% prevalence; strong variance; mentioned as an alternative; ~half of comparable rounds include it | Flag for discussion: "About half of comparable rounds include this. Depends on investor type and deal momentum." Present both sides. |
| **Unlikely** | 0.0–0.39 | Outlier or red flag; found in <40% of comparable rounds; noted as non-standard in benchmarks; often signals down-market or distressed negotiation | Flag explicitly: "This term is below market. It appears in <[X]% of comparable rounds. Signals [market stress / investor conservatism / deal risk]." |

---

## Anti-Patterns

What NOT to do when analysing VC term sheets:

1. **Analysing economic terms in isolation from control terms** — A founder-favorable
   liquidation preference is only meaningful if the founder retains governance control.
   If the investor holds board majority and veto rights, favorable economics provide
   limited protection when the company underperforms. Always cross-check economics
   and governance findings before concluding.

2. **Failing to model the liquidation preference stack** — A Series A term sheet does
   not exist in isolation. If a Series Seed with 1× participating preference is already
   on the cap table, adding a Series A with 2× non-participating creates a compound
   preference stack that may consume most exit proceeds in a modest exit. Always request
   the full cap table and model interactions.

3. **Treating all anti-dilution clauses as equivalent** — "Weighted average" can be
   broad-based (uses all outstanding shares in the formula — NVCA default, more founder-
   friendly) or narrow-based (uses only preferred shares — more dilutive). These are
   not the same. Always identify which formula is specified and model the difference.

4. **Accepting "full-ratchet anti-dilution" without modeling impact** — Full ratchet on
   a Series A term can, in a down round, effectively reset the entire Series A ownership
   position to match the new lower price. A Series A at $1/share with full ratchet, and
   a Series B at $0.50/share, doubles the Series A share count and can wipe out founder
   ownership below 20%. Always model this before classifying full ratchet as YELLOW.

5. **Ignoring the option pool trap** — Pre-money option pool inclusion is a well-known
   founder dilution mechanic. A $10M pre-money valuation with a 10% pre-money pool
   effectively reduces founder ownership by the pool percentage before the investor
   even invests. Always calculate fully-diluted ownership with and without pool expansion.

6. **Assuming "board observer rights" are harmless** — Board observers receive the same
   materials as voting directors, attend all meetings, and have full visibility into
   strategy and operations. Multiple observer rights can create de facto investor
   control of information, even without a formal board seat. Flag if more than 2
   investors hold observation rights without confidentiality obligations.

7. **Reading protective provisions as boilerplate** — Protective provisions vary widely.
   An investor consent requirement for "any annual budget in excess of 110% of prior
   year" creates day-to-day operational friction. "Any related-party transaction above
   $25,000" requires investor sign-off on routine advisor agreements. Read every item
   in the protective provisions list; flag unusual operational controls.

8. **Accepting "market standard" without data** — Investors routinely describe their
   terms as "market standard" regardless of whether they are. Always cite benchmark
   data (NVCA, Carta, Orrick) with source and date when classifying terms. A term that
   was standard in 2021 (peak capital abundance) may not be standard in 2025.

9. **Applying US benchmarks to UK or Indian deals** — NVCA model terms do not apply
   to UK or Indian deals. UK BVCA model documents have different defaults for board
   composition, anti-dilution, and liquidation preferences. Indian AIF regulations
   constrain certain preference structures (CCPS requirement, FEMA restrictions on
   guaranteed returns). Always identify jurisdiction before applying any benchmark.

10. **Ignoring the multi-round cascade** — A term that is MARKET-STANDARD at Series A
    can become FOUNDER-DILUTIVE at Series C when it interacts with three more rounds of
    anti-dilution adjustments and compounding preference stacks. Always flag terms that
    create "preference stack" risk or compound anti-dilution effects across rounds.

11. **Missing the founder removal trap** — If the investor controls board composition
    AND holds veto rights on CEO appointment AND founder is subject to involuntary
    termination without cause (common in investor board-controlled structures), then
    the investor can effectively remove the founder from the company while preserving
    the preferred preference — leaving the founder with common stock but no seat at
    the table. Flag this cascade explicitly.

12. **Treating drag-along as symmetric** — Drag-along rights that allow the preferred
    majority to drag all shareholders into a sale are founder-unfavorable. A drag-along
    without appraisal rights, without minimum price protection, and without the founder's
    ability to veto (if the founder controls a blocking stake) can force founder into
    accepting an exit at a price that returns the preference to the investor but nothing
    to the founder. Always check drag-along trigger thresholds and founder's ability
    to block.

13. **Not quantifying governance control** — "Investor gets one board seat" sounds
    manageable. "Investor gets one board seat, one observer, veto rights on hiring,
    veto rights on budget, veto rights on M&A" is near-total operational control.
    Quantify governance control by counting how many decisions require investor consent
    vs. founder discretion. Score: 0–5 decisions = limited control; 6–10 = moderate;
    11+ = high; 20+ = operational veto.

14. **Confusing the cap table before and after close** — Always calculate ownership
    percentages at two points: (A) immediately post-close (investment complete, option
    pool created, all existing convertible notes converted), and (B) fully diluted
    post-close (including all options, warrants, and convertible instruments). These
    are often materially different.

15. **Presenting investor perspective as neutral** — Many investors frame their term
    sheets as standard or balanced when they are not. Dual-perspective framing requires
    explicitly labeling which party each term favors. Never present a term as neutral
    if it systematically advantages one party.

16. **Missing the information asymmetry** — Investors receive detailed financials, cap
    table, and operational data from the company. Founders receive none from the
    investor. This is structural and expected, but when investors impose unusually broad
    information rights without confidentiality obligations, the asymmetry becomes a
    competitive risk (investor may share data across portfolio companies).

17. **Accepting pro-rata rights as passive** — Pro-rata rights allow investors to
    participate in future rounds at the same price. But exercising pro-rata rights adds
    capital from a potentially skeptical existing investor, may signal weakness to new
    investors, and in some structures forces the company to hold capacity for the
    pro-rata exercise before closing a new round. Frame pro-rata as an investor option,
    not a company benefit.

18. **Ignoring EIS/SEIS compatibility (UK)** — UK deals where founders or investors
    need EIS (Enterprise Investment Scheme) or SEIS (Seed EIS) tax relief require the
    investment structure to be EIS/SEIS compatible. Certain liquidation preference
    structures (cumulative dividends, guaranteed returns, debt-like mechanics) disqualify
    EIS/SEIS status. Always flag for UK deals if EIS/SEIS relief is material.

19. **Ignoring FEMA/RBI constraints (India)** — Foreign investment into Indian startups
    is subject to FEMA pricing guidelines. A liquidation preference that guarantees
    returns to a foreign investor (e.g., "investor receives 1.5× investment regardless
    of company value") may be characterised as an assured return instrument, which
    violates FEMA pricing rules. Always flag for Indian deals with foreign investors.

20. **Analysing pay-to-play in isolation** — Pay-to-play provisions require investors
    to participate in future rounds or forfeit preferred status. But the impact depends
    on which rights are forfeited (anti-dilution only? all preferred? conversion to
    common?) and which investors are exempt (larger lead investors often carve themselves
    out). Model the pay-to-play impact on each existing investor class separately.

21. **Single-pass analysis without interaction modeling** — Term sheet provisions
    interact: liquidation preference + anti-dilution + pay-to-play + board composition
    = a complete risk allocation picture. Any single provision analysed alone may appear
    MARKET-STANDARD while the combination is FOUNDER-DILUTIVE. Always run an
    interaction analysis after completing individual term reviews.

22. **Citing outdated benchmark data** — VC term sheet markets shift rapidly. 2022 data
    (post-peak, down-market pressure) is not valid for 2025 (normalising market). Q2
    2025 NVCA data shows 98% non-participating 1× preference — a reversion from the
    participating preference increase seen in 2022–2023. Always cite the most recent
    available benchmark. Never use data older than 18 months without flagging it.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Active voice**: "The liquidation preference entitles investors to receive [X]"
   not "The liquidation preference allows for [X] to be received by investors"
2. **Plain language**: Define every VC term on first use. Founders may not be experts;
   counsel may skip explanations.
3. **Quantify**: State founder ownership percentages, not just "dilution occurs." Show
   the math.
4. **Dual perspective**: Every material finding must state the founder classification
   AND the investor classification, even if one is MARKET-STANDARD.
5. **Source every benchmark claim**: "[X]% of [stage] rounds per [source, date]"
6. **Confidence qualifiers**: State uncertainty explicitly; never assert "market standard"
   without data
7. **One finding per paragraph**: Do not bundle multiple issues into one paragraph;
   separate findings are easier to negotiate against
8. **Redlines are proposals**: Mark redlines as "Suggested language (Proposed)" not as
   "Required change"
9. **Flag non-binding status**: Term sheets are mostly non-binding. Note which specific
   provisions are binding (confidentiality, exclusivity, expense reimbursement, break-
   up fees) vs. indicative
10. **Proofread arithmetic**: Verify all cap table calculations; dilution math errors are
    common and can be damaging if not caught

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:
- Search for jurisdiction-relevant statutes governing preference share enforceability,
  anti-dilution mechanics, and board fiduciary duties
- Verify SEBI AIF regulatory constraints for Indian deals
- Verify UK Companies Act and BVCA model updates
- Save results to `/tmp/legalcode-term-sheet-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp**:
- Proceed with market benchmark research and repository analysis only
- Mark all statutory references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus analysis on structural quality, market benchmarking, and dual-perspective
  framing rather than statutory depth

---

## Output Format Template

```markdown
# VC Term Sheet Analysis — [Company Name] [Series X] [YYYY-MM-DD]

## Executive Summary (60-Second Read)

**Investment**: $[X]M at $[Y]M pre-money / $[Z]M post-money
**Stage**: [Seed / Series A / B / C]
**Investor**: [Name]
**Jurisdiction**: [US-DE / UK / India / Other]
**Overall Classification**: [FOUNDER-FAVORABLE / BALANCED / INVESTOR-FAVORED / OUTLIER]
**Benchmark**: [NVCA 2025 Standard / BVCA Feb 2025 / AIF Market Norms / Stage-adjusted]

**Tier 1 Issues (Must Address)**: [N] issues require negotiation before signing
**Tier 2 Issues (Should Address)**: [N] issues worth negotiating
**Tier 3 Concessions**: [N] terms where founder has leverage to trade

**Immediate Action**: [Negotiate [X] before signing / Acceptable with minor redlines /
RED-FLAG issues — retain VC counsel immediately / Competitive — proceed to diligence]

---

## Founder Cap Table Impact

| Party | Pre-Close % | Shares | Post-Close % | Fully Diluted % |
|-------|------------|--------|--------------|-----------------|
| Founder(s) | — | X | Y% | Z% |
| Seed investors (prior) | — | X | Y% | Z% |
| Series A investor | $[X]M | X | Y% | Z% |
| ESOP (unissued) | — | X | Y% | Z% |
| **Total** | | | 100% | 100% |

**Founder dilution from this round**: [X.X%]
**Founder fully-diluted ownership post-close**: [X.X%]
**Projected founder ownership at Series B (if standard 20% dilution)**: [X.X%]

---

## Exit Scenario Modeling

| Scenario | Exit Value | Preference Stack Paid | Remaining Proceeds | Founder Return | Investor Return |
|----------|------------|----------------------|-------------------|----------------|-----------------|
| Down exit (0.5× valuation) | $[X]M | $[X]M | $[X]M | $[X]M ([X]%) | $[X]M ([X]%) |
| Flat exit (current valuation) | $[X]M | $[X]M | $[X]M | $[X]M ([X]%) | $[X]M ([X]%) |
| Up exit (3× valuation) | $[X]M | $[X]M | $[X]M | $[X]M ([X]%) | $[X]M ([X]%) |

*Calculations assume [non-participating / participating] preference of [X]× on
$[investment]M. Preference stack includes [any existing preferred + new preferred].*

---

## Governance Control Assessment

**Board composition (post-close)**: [Founder seats] / [Investor seats] / [Independent seats]
**Founder board control**: [MAJORITY / PARITY / MINORITY]
**Investor veto rights**: [N] protective provisions requiring investor consent
**Governance friction risk**: [LOW / MEDIUM / HIGH / CRITICAL]

Investor consent required for:
- [ ] [List all decisions]

Founder discretion (no consent required):
- [ ] [List remaining operational decisions]

---

## Tier 1 Findings — Must Address

### [1.1] [Term Name] | Founder: [RED] | Investor: [GREEN] | Confidence: [HIGH / PROBABLE / etc.]

**Plain-language summary**: [1–2 sentences describing the term and why it matters]

**Founder risk**: [Specific impact; quantify where possible]
**Investor rationale**: [Why investor wants this term]

**Market context**: [X]% of [stage] rounds include this term per [Source, YYYY-QQ].
[Any stage or geography variance]. Benchmark: [DEFINITE / HIGH / PROBABLE / POSSIBLE].

**Proposed redline**:
- Current: "[Exact quoted language from term sheet]"
- Proposed: "[Exact alternative language]"
- Fallback: "[What founder can accept if full redline is rejected]"

**Impact if accepted as-is**: [Specific quantified consequence]
**Trade-off opportunity**: [What founder can offer to win this point]

---

[Repeat for each Tier 1 finding]

---

## Tier 2 Findings — Should Address

### [2.1] [Term Name] | Founder: [YELLOW-RED] | Investor: [YELLOW-GREEN] | Confidence: [...]

[Abbreviated format — plain-language summary, market context, proposed redline, fallback]

---

[Repeat for each Tier 2 finding]

---

## Tier 3 — Concession Candidates

### [3.1] [Term Name] | Founder: [YELLOW] | Investor: [YELLOW-GREEN] | Confidence: [...]

[Brief summary — describe the term, state that it is a negotiation trade-off, and
suggest how to use it strategically]

---

## Missing Provisions

| Provision | Stage Expectation | Classification | Recommended Action |
|-----------|-------------------|----------------|--------------------|
| [Provision] | [Standard at this stage] | [FOUNDER-DILUTIVE / MARKET-STANDARD / Not applicable] | [Add / Not necessary / Clarify] |

---

## Multi-Round Interaction Analysis

**How current terms cascade to Series B/C**:
- Anti-dilution: [If Series B is a down round, current weighted-average provision adjusts
  conversion price as follows: ...]
- Preference stack: [Current $[X]M Series A preference will be senior to new Series B.
  Combined preference stack at Series B may exceed exit value in [down exit scenario].]
- Board composition: [New Series B investor will likely request [1 / 2] seats.
  Projected Series B board: [composition]. Founder [retains / loses] control.]
- Option pool: [Series B will likely require option pool refresh of [X]%.
  Post-refresh founder dilution: [Y]%.]

---

## Comparable Precedent Rounds

| Company | Stage | Date | Key Terms | Comparison |
|---------|-------|------|-----------|------------|
| [Comparable A] | Series A | YYYY-QQ | [Key terms] | [Better/Worse/Same] |
| [Comparable B] | Series A | YYYY-QQ | [Key terms] | [Better/Worse/Same] |

*Source: [PitchBook / Carta / AngelList / Publicly disclosed rounds]*

---

## Critical Items for Legal Review

1. [Specific term or clause]: [Why VC counsel must review before signing]
2. [Specific term or clause]: [Why VC counsel must review]
3. [Non-binding status]: Confirm which provisions are binding (typically: confidentiality,
   exclusivity, expense reimbursement, break-up fees) vs. indicative.

---

## Recommended Next Steps

1. **[Immediate]** — [Action with owner and deadline]
2. **[Before signing]** — Retain experienced VC counsel; share this analysis
3. **[Parallel track]** — [Any diligence or negotiation preparation founder can do now]
4. **[After signing]** — [Diligence timeline, definitive docs drafting, expected changes]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-term-sheet-analysis"
  topic: "VC Term Sheet Analysis — Economic and Governance Assessment"

  # Term sheet context
  company_name: "[Company name]"
  investor_name: "[Lead investor]"
  investment_amount: "$[X]M"
  pre_money_valuation: "$[Y]M"
  stage: "[Seed / Series A / B / C / D]"
  governing_law: "[Delaware / England & Wales / India / Other]"
  jurisdiction_track: "[US-NVCA / UK-BVCA / India-AIF / Other]"
  term_sheet_type: "[NVCA standard / BVCA standard / Custom / SAFE extension / Other]"
  binding_status: "NON-BINDING except: [confidentiality, exclusivity period, expense reimbursement]"

  # Analysis context
  analysis_date: "[YYYY-MM-DD]"
  primary_perspective: "[Founder / Investor / Neutral]"
  dual_perspective_applied: "[Yes — all material terms / Partial / No]"
  benchmark_selected: "[NVCA Oct 2025 / BVCA Feb 2025 / AIF market norms / Stage-adjusted]"

  # Cap table
  founder_ownership_pre: "[X.X% pre-round]"
  founder_ownership_post: "[X.X% post-round, basic] / [X.X% post-round, fully diluted]"
  esop_pool_size: "[X.X% pre-money included / X.X% post-money added]"

  # Market benchmarks used
  market_benchmarks:
    - "[Source] — [metric] — [YYYY-QQ]"
    - "NVCA Model Term Sheet (October 2025 update)"
    - "BVCA Model Documents for Early Stage Investments (February 2025)"
    - "Carta VC Benchmark Report [relevant quarter]"
    - "PitchBook Q2 2025 VC Term Sheet Data"
    - "Orrick VC Report [relevant quarter]"
  benchmark_data_currency: "[Last 12 months / Current quarter / YYYY-QQ]"
  market_conditions: "[Up market / Neutral / Down market] as of [YYYY-QQ]"

  # Findings summary
  tier_1_count: "[N] must-address findings"
  tier_2_count: "[N] should-address findings"
  tier_3_count: "[N] concession-candidate findings"
  founder_red_findings: "[List of FOUNDER-DILUTIVE RED terms]"
  missing_provisions_count: "[N] provisions absent that are market-standard"

  # Key classifications
  liquidation_preference: "[Type and multiple — Founder: X / Investor: Y]"
  anti_dilution_type: "[Weighted-average / Full-ratchet / None]"
  board_control: "[FOUNDER-MAJORITY / PARITY / INVESTOR-MAJORITY]"
  protective_provisions_count: "[N] items requiring investor consent"
  founder_governance_score: "[LOW / MODERATE / HIGH] — [N] decisions require investor consent"

  # Exit scenario modeling
  scenario_modeling_performed: "[Yes / No]"
  down_exit_founder_return: "$[X]M ([X]%)"
  flat_exit_founder_return: "$[X]M ([X]%)"
  up_exit_founder_return: "$[X]M ([X]%)"

  # Quality frameworks
  citation_quality_gates: "[All 5 gates PASSED / Gate [X] flagged and corrected]"
  self_interrogation_applied: "[Applied to [N] Tier 1 findings / Not required]"
  dual_perspective_framing: "[Applied comprehensively / Applied to key terms]"
  confidence_scoring: "[All material terms scored]"

  # Research
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-term-sheet-research.md / Not created]"
  interaction_analysis_performed: "[Yes — N cross-term interactions flagged / No]"
  multi_round_cascade_modeled: "[Yes — Series B/C projections included / No]"

  # Limitations
  scope_limitations:
    - "Term sheet is non-binding except [listed provisions]"
    - "Definitive docs will re-negotiate [most] / [some] terms; re-negotiation expected on [X]"
    - "Analysis assumes [key assumptions: sole founder, no prior preferred, Delaware corp, etc.]"
  jurisdictional_notes: "[Analysis applies to [US/UK/India] context per stated governing law]"
  data_date_cut: "[YYYY-MM-DD — most recent benchmark data used]"

  # Reviewer
  reviewer: "AI-assisted — requires review by qualified VC counsel and founder/investor judgment"
  review_recommendation: "[Full VC counsel review before signing] / [Selective review: [terms]]"
```
```

---

## Localization Notes

When analysing term sheets under non-US governing law, activate the relevant track:

### US Track (Delaware)
- Apply NVCA Model Term Sheet (October 2025 edition) as the primary benchmark
- Cite DGCL provisions when relevant (§ 151 for preference rights, § 141 for board)
- Note IRC § 409A for option pricing and IRC § 280G for acceleration on change of control
- Reference Delaware Court of Chancery precedent on drag-along fiduciary duties
  (*Trados Inc.* appraisal, *In re SolarCity Corp.*) where relevant — mark [VERIFY]

### UK Track (England & Wales)
- Apply BVCA Model Documents for Early Stage Investments (February 2025 edition)
- Note EIS/SEIS compatibility requirements for eligible startups
- Apply Companies Act 2006 rules for preference share amendments and board removal
- Note UK Employment Rights Act 1996/2025 for founder employment and vesting mechanics
- Preference structures that guarantee returns may trigger financial promotion rules
  (FCA) — flag for regulated-activity assessment if applicable

### India Track
- Apply SEBI (AIF) Regulations 2012 (as amended 2024/2025) for fund eligibility
- Apply Companies Act 2013 for preference share rights and shareholder agreements
- Apply FEMA (Non-Debt Instruments) Rules 2019 for foreign investor structures —
  liquidation preferences with guaranteed returns may be characterised as assured-
  return instruments and violate FEMA pricing norms
- Flag compulsorily convertible preference shares (CCPS) as the typical Indian
  structure (mandatory conversion timeline required under Companies Act)
- Note SEBI AIF valuation framework circular (September 2024) for AIF portfolio
  valuation methodology — relevant for secondary transactions and mark-to-market

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis. Research pipeline:
2-agent structural and prompt engineering analysis (reference skills: legalcode-contract-
review, legalcode-indemnification-analysis, legalcode-eu-ai-act-high-risk-compliance) +
deep legal research (NVCA October 2025 update, BVCA February 2025 edition, SEBI AIF
Regulations 2024/2025, Chambers VC Guide India 2025, Nishith Desai AIF publications,
PitchBook Q2 2025 data, market benchmark research). Covers US/UK/India VC term sheet
markets with dual-perspective founder/investor framing, 12-step workflow, 6-category
deep analysis, three-scenario exit modeling, and 22 term-sheet-specific anti-patterns.
