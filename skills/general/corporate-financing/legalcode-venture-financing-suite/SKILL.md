---
name: legalcode-venture-financing-suite
description: 'Comprehensive venture financing suite covering instrument selection (SAFE vs. ASA vs. convertible
  note vs. priced equity round), cross-border structuring, securities exemption analysis, tax incentive
  routing (QSBS/Section 1202, SEIS/EIS/EMI, Singapore Sections 13H/13O/13U/13X), employee equity comparison
  (ISO/NSO, EMI, ESOP, 83(b)), and jurisdiction-specific frameworks for US, UK, EU, Singapore, and India.
  Use when a founder, investor, or counsel needs to: select the right early-stage financing instrument;
  understand tax relief eligibility; structure a cross-border investment or flip-up; review SAFE or convertible
  note terms; analyze QSBS or EIS/SEIS qualification; compare ISO vs. NSO vs. EMI equity for employees;
  or assess securities exemption availability under Reg D 506(b)/506(c), UK s.86, EU Prospectus Regulation,
  or MAS rules.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Comprehensive venture financing suite covering instrument selection (SAFE vs. ASA vs. convertible note vs. priced equity round), cross-border structuring, securities exemption analysis, tax incentive routing (QSBS/Section 1202, SEIS/EIS/EMI, Singapore Sections 13H/13O/13U/13X), employee equity comparison (ISO/NSO, EMI, ESOP, 83(b)), and jurisdiction-specific frameworks for US, UK, EU, Singapore, and India. Use when a founder, investor, or counsel needs to: select the right early-stage financing instrument; understand tax relief eligibility; structure a cross-border investment or flip-up; review SAFE or convertible note terms; analyze QSBS or EIS/SEIS qualification; compare ISO vs. NSO vs. EMI equity for employees; or assess securities exemption availability under Reg D 506(b)/506(c), UK s.86, EU Prospectus Regulation, or MAS rules. Router skill — routes to deep-dive modules based on task type and jurisdiction. Also triggers on: post-money SAFE mechanics, ASA HMRC compliance, convertible note maturity risk, option pool shuffle, anti-dilution weighted average vs. full ratchet, liquidation preference participation, pro-rata rights, Delaware C-Corp structuring, Cayman holding co, FEMA/RBI foreign investment, advance assurance, advance subscription agreement.


# Legalcode Venture Financing Suite

> **Disclaimer**: This skill provides a framework for AI-assisted venture financing analysis. It
> does not constitute legal, tax, securities, or financial advice. All outputs must be reviewed
> by a qualified attorney, tax advisor, and securities counsel licensed in the relevant jurisdiction
> before any reliance or action. Laws, regulations, tax codes, and market practice change; verify
> current applicability before relying on any provision described here. References to statutes
> (IRC § 1202, ITEPA 2003, FEMA, MAS rules), model documents (NVCA, BVCA, YC SAFE), and market
> benchmarks carry currency risk — verify the latest edition. AI-generated financial modeling and
> cap table arithmetic require independent verification. Nothing here constitutes investment advice
> or an offer or solicitation to buy or sell securities.

---

## Purpose and Scope

This skill analyses venture financing decisions end-to-end — from selecting the right instrument
at the earliest stage through to understanding the tax, regulatory, and cross-border consequences
of the structure chosen.

**Covers:**

- Instrument selection: SAFE vs. ASA vs. Convertible Note vs. Priced Equity round (seed through
  Series A/B), with jurisdiction-adjusted recommendations
- SAFE deep dive: post-money mechanics, valuation cap, discount rate, MFN, pro-rata rights,
  conversion events, YC standard vs. custom variants
- ASA deep dive: HMRC qualifying conditions for SEIS/EIS compatibility, advance assurance process,
  longstop date, non-refundability requirements, failure modes
- Convertible note analysis: interest accrual, maturity risk, conversion mechanics, redemption
  rights, qualified financing thresholds
- Priced round elements: option pool shuffle, anti-dilution (BBWA vs. full ratchet), liquidation
  preference structure, protective provisions (router to `legalcode-term-sheet-analysis` for
  full term-sheet deep dive)
- Securities exemptions: US Reg D 506(b)/506(c), Reg A+, Reg CF; UK s.86 exemptions; EU
  Prospectus Regulation exemptions; Singapore MAS qualified investor/institutional rules; India
  FEMA automatic route and FVCI route
- Tax incentive routing: US QSBS (IRC § 1202); UK SEIS/EIS/EMI (ITEPA 2003 / ITA 2007);
  Singapore Sections 13H, 13O, 13U, 13X; India FEMA pricing rules and CCPS structuring
- Employee equity comparison: US ISOs vs. NSOs (IRC §§ 422/83), 83(b) elections, 409A safe
  harbor; UK EMI/CSOP options (ITEPA 2003); ESOP pool sizing and vesting norms; multi-
  jurisdiction equity sub-plan flags
- Cross-border structuring: Delaware C-Corp formation, flip-up transactions, Cayman/Singapore
  holding structures, QSBS optimization, SEIS/EIS structural constraints, FEMA-compliant
  investment routing

**Does not:**

- Provide legal, tax, or investment advice or replace qualified counsel
- Perform a full term sheet analysis — route to `legalcode-term-sheet-analysis` for that
- Draft definitive documents (stock purchase agreement, SAFE instrument, note) — those are
  drafting skills
- Model fund return economics from the investor's portfolio construction perspective
- Substitute for HMRC advance assurance or IRS QSBS eligibility opinion

**Relationship to other skills:**

| Task                               | Use This Skill       | Route To                                 |
| ---------------------------------- | -------------------- | ---------------------------------------- |
| Instrument selection + tax routing | ✅ This skill        | —                                        |
| Full term sheet analysis           | Initial framing only | `legalcode-term-sheet-analysis`          |
| Equity plan deep review            | Summary only         | `legalcode-equity-incentive-plan-review` |
| Founders' agreement                | Initial structure    | `legalcode-founders-agreement-drafter`   |
| M&A due diligence                  | Cross-reference      | `legalcode-ma-due-diligence-checklist`   |

---

## Jurisdiction and Governing Law

This skill is multi-jurisdictional with five deep-coverage tracks:

| Track             | Legal Framework                                            | Instruments                                           | Tax Incentives                          | Securities                       |
| ----------------- | ---------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------- | -------------------------------- |
| **US (Delaware)** | DGCL; IRC; Securities Act 1933                             | SAFE (post-money), convertible note, priced preferred | QSBS (IRC § 1202), 83(b), ISO/NSO       | Reg D 506(b/c), Reg A+, Reg CF   |
| **UK**            | Companies Act 2006; ITEPA 2003; ITA 2007                   | ASA, priced preferred                                 | SEIS/EIS (ITA 2007), EMI (ITEPA 2003)   | s.86 FSMA exemptions, FCA rules  |
| **EU**            | Prospectus Regulation (EU) 2017/1129; national company law | Priced preferred; local variants                      | National schemes (vary by member state) | Prospectus Regulation exemptions |
| **Singapore**     | Companies Act; MAS regulations; Income Tax Act             | Priced preferred; Singapore Pte Ltd                   | Sections 13H/13O/13U/13X                | MAS qualified investor; Reg S    |
| **India**         | Companies Act 2013; FEMA/NDI Rules 2019; SEBI AIF          | CCPS, equity, convertible notes                       | India-specific incentives; FEMA routing | FEMA automatic route; FVCI       |

[JURISDICTION-SPECIFIC] When localizing beyond these five tracks, research and apply:

- Local company law governing preference share issuance and conversion
- Securities law exemptions for private placements
- Tax incentive schemes for early-stage investment
- Foreign investment restrictions and reporting requirements
- Currency control and repatriation rules

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming intent,
the workflow pauses and asks when:

- The answer would materially change the instrument recommendation
- Tax incentive eligibility depends on facts not yet provided
- Jurisdiction-specific constraints create forks only the user can resolve
- Cross-border complexity requires knowing the primary investor base

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

### Step 1: Accept Input

Accept input in any of these formats:

- **Company profile**: Stage, jurisdiction, amount raising, investor base, founder composition
- **Document review**: SAFE, ASA, convertible note, or term sheet provided as file/URL/pasted text
- **Specific question**: "Am I QSBS-eligible?", "Should we use SAFE or ASA?", "How does the
  option pool shuffle affect us?"
- **Structured task**: Instrument comparison, tax routing, securities analysis, equity design

If insufficient context is provided, proceed to Step 2 to gather what is needed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before routing the analysis, ask the user these questions (skip any already
answered):

1. **Task type** — What is the primary objective?
   - Options: **Instrument selection** (what should we use?), **Document review** (review a
     specific SAFE/ASA/note), **Tax routing** (QSBS/SEIS/EIS eligibility), **Securities
     compliance** (what exemption applies?), **Equity design** (ISO vs. NSO vs. EMI for
     employees), **Cross-border structuring** (flip-up, Cayman, FEMA routing), **All of the
     above** (full financing suite analysis)
   - _Why this matters_: Determines which modules to activate. Document review starts at
     Module B/C/D; tax routing starts at Module H; equity design starts at Module I.

2. **Stage and amount** — What round is this, and how much are you raising?
   - Options: Pre-seed (<$500k), Seed ($500k–$2M), Post-seed/Bridge ($2M–$5M), Series A ($5M+)
   - _Why this matters_: Instrument norms vary dramatically by stage. SAFEs dominate pre-priced;
     priced rounds dominate from Series A. Option pool sizing norms also differ.

3. **Primary jurisdiction** — Where is the company incorporated?
   - Options: US (Delaware C-Corp), UK (Companies Act Ltd), EU (specify member state), Singapore
     (Pte Ltd), India (Private Ltd), Other (specify), Not yet incorporated
   - _Why this matters_: Determines which tax incentives are available (QSBS requires C-Corp;
     SEIS/EIS requires UK company; ASA requires UK company for HMRC purposes), which securities
     exemptions apply, and which instrument variants are appropriate.

4. **Investor base** — Who are the investors?
   - Options: US VC funds only, UK/EU angel investors, Mixed US + UK/EU, Singapore/APAC
     institutional, India-based or FVCI-registered, Angel investors (retail/individual), Mixed
   - _Why this matters_: US investors expect SAFEs; UK angels expect ASAs for SEIS/EIS; Indian
     foreign investors require FEMA compliance; Singapore funds may prefer MAS-compliant structures.

5. **Tax incentive priority** — Is tax relief a primary driver?
   - Options: Yes — QSBS optimization (US), Yes — SEIS/EIS eligibility (UK), Yes — Singapore
     tax efficiency, No — tax is secondary to speed/simplicity, Unknown
   - _Why this matters_: Tax incentive requirements constrain instrument structure. SEIS/EIS
     prohibits certain ASA features; QSBS requires C-Corp and $50M gross assets threshold.

6. **Perspective** — Whose interests does this analysis serve?
   - Options: Founder/Company (structuring our raise), Investor (reviewing before committing),
     Legal counsel (neutral), Board/Advisor (governance perspective)
   - _Why this matters_: Instrument trade-offs favor different parties. Pro-rata rights benefit
     investors; simplified conversion terms benefit founders.

If the user provides partial context, proceed with what is available and **state assumptions
explicitly** (e.g., "Assuming US Delaware corporation at seed stage — correct me if wrong").

### Step 3: Route to Modules

Based on Step 2, activate the relevant modules:

| Task Type                 | Primary Module                                            | Supporting Modules                 |
| ------------------------- | --------------------------------------------------------- | ---------------------------------- |
| Instrument selection      | A (Comparison), + B/C/D as needed                         | H (Tax), G (Securities)            |
| SAFE review               | B (SAFE)                                                  | A (Comparison), G (Securities)     |
| ASA review                | C (ASA)                                                   | H (Tax — SEIS/EIS), G (Securities) |
| Convertible note review   | D (Note)                                                  | A (Comparison), G (Securities)     |
| Term sheet (priced round) | Brief Module E + route to `legalcode-term-sheet-analysis` | H (Tax), I (Equity)                |
| Tax routing               | H (Tax Incentives)                                        | A (Comparison), F (Cross-border)   |
| Securities compliance     | G (Securities)                                            | F (Cross-border)                   |
| Employee equity           | I (Employee Equity)                                       | H (Tax — ISOs/EMI)                 |
| Cross-border structure    | F (Cross-border)                                          | G, H                               |
| Full suite                | All modules                                               | —                                  |

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to build a jurisdiction-relevant legal reference for this analysis.

Search for authority across these categories based on the jurisdiction activated:

**US Track:**

- IRC § 1202 (QSBS) — current text and IRS guidance
- Securities Act § 4(a)(2) and Reg D Rule 506(b)/(c)
- IRC §§ 422, 83(b), 409A — option and equity incentive rules
- Delaware General Corporation Law §§ 151–154 (preferred stock)

**UK Track:**

- Income Tax Act 2007 Part 5A (EIS) and Part 5B (SEIS) — qualifying conditions
- Income Tax (Earnings and Pensions) Act 2003 Schedule 5 (EMI options)
- Companies Act 2006 — preference share rights, advance subscription mechanics
- HMRC VCM Manual — VCM12025 (EIS ASA); VCM33025 (SEIS ASA)

**EU Track:**

- Regulation (EU) 2017/1129 (Prospectus Regulation) Art. 1(4) exemptions
- Local member state company laws (research specific jurisdiction)

**Singapore Track:**

- Income Tax Act ss. 13H, 13O, 13U, 13X
- Securities and Futures Act — accredited investor definition
- MAS Notice SFA 02-N02 — VCFM regime

**India Track:**

- FEMA (Non-Debt Instruments) Rules 2019
- RBI pricing guidelines for FDI (historical cost / DCF / NAV)
- Companies Act 2013 — CCPS structuring
- SEBI AIF Regulations 2012

Save results to `/tmp/legalcode-vf-authority.md`. Mark citations as VERIFIED.

**If legalcode-mcp is not connected:** Mark all statutory references with [VERIFY] and note
`legalcode_mcp: "Not connected"` in the Glass Box audit trail.

### Step 5: Execute Module Analysis

Activate the modules selected in Step 3. Run each module in sequence, applying the Instrument
Classification system (OPTIMAL / SUBOPTIMAL / INCOMPATIBLE) and Document Classification
(COMPLIANT / FLAG / NON-COMPLIANT) as appropriate.

**⟁ CLARIFY** — For any module where a critical fact is missing and would change the analysis,
pause and ask before proceeding:

- "QSBS eligibility requires that the company had gross assets ≤ $50M at the time of issuance.
  Can you confirm the company's gross assets at closing?"
- "SEIS eligibility requires the company to be ≤ 3 years old from its first commercial trade.
  When did the company start trading?"
- "ASA HMRC compliance requires a maximum 6-month longstop date. The longstop in this document
  is [X]. Should I flag this as a non-compliant term?"

### Step 6: Classify Findings

For **document review tasks** (SAFE, ASA, note review), classify every material finding:

- **COMPLIANT**: Term meets the standard or is within acceptable range. Note for awareness.
- **FLAG**: Term diverges from market standard or creates a risk worth addressing. Generate
  specific commentary and recommended revision.
- **NON-COMPLIANT**: Term violates a statutory or regulatory requirement (e.g., ASA charges
  interest — fails HMRC SEIS/EIS test; SAFE lacks market standard conversion mechanics). Explain
  the specific violation, provide market-standard replacement language, and recommend resolution.

For **instrument selection tasks**, classify each option:

- **OPTIMAL**: Best fit given jurisdiction, stage, investor base, and tax goals.
- **SUBOPTIMAL**: Works but leaves tax efficiency, deal speed, or investor protection on the table.
- **INCOMPATIBLE**: Not appropriate for this situation (e.g., SAFE for UK SEIS/EIS investors;
  interest-bearing ASA for HMRC compliance).

For **tax incentive / securities tasks**, classify each scheme or exemption:

- **AVAILABLE**: Company/transaction qualifies. Describe conditions to maintain.
- **PARTIAL**: Company qualifies, but specific structural choices may disqualify. Flag risks.
- **NOT AVAILABLE**: Company/transaction does not qualify. Explain why and suggest alternatives.

### Step 7: Apply Prioritization Framework

For each classified finding or recommendation, assign a negotiation / action priority:

**Tier 1 — Critical (Must Address)**

- Tax incentive disqualification risks (e.g., ASA charges interest → loses SEIS/EIS)
- Securities law violations (e.g., no applicable exemption for the investor type)
- FEMA non-compliance for India-bound FDI
- Instrument incompatibility with primary investor jurisdiction or tax goals
- Missing conversion mechanics or maturity provisions with material economic impact

**Tier 2 — Important (Should Address)**

- Suboptimal instrument choice given tax efficiency goals
- MFN clause absent on uncapped SAFEs (loss of investor protection)
- Pro-rata rights absent for significant investors
- Option pool pre-money vs. post-money structuring
- Anti-dilution mechanics diverging from BBWA market standard

**Tier 3 — Advisory (Consider)**

- Minor drafting improvements to standard templates
- Board observer right structuring preferences
- Information rights scope and reporting cadence
- BBWA carve-out completeness
- Drag/tag mechanics for early-stage documents

### Step 8: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For every NON-COMPLIANT finding, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to all key recommendations.
4. Verify all [JURISDICTION-SPECIFIC] markers are placed correctly.
5. Confirm no jurisdiction-specific concept is stated as universal.
6. Generate the Glass Box Audit Trail and append to output.

### Step 9: Route to Deep Skills

Where the analysis reveals a need for deeper work than this suite covers:

| Trigger                                           | Route To                                  |
| ------------------------------------------------- | ----------------------------------------- |
| Full term sheet with all priced-round terms       | `legalcode-term-sheet-analysis`           |
| Equity incentive plan (ISO/NSO/RSU plan document) | `legalcode-equity-incentive-plan-review`  |
| Founders' agreement structuring                   | `legalcode-founders-agreement-drafter`    |
| Cap table M&A analysis                            | `legalcode-ma-due-diligence-checklist`    |
| Shareholder agreement review                      | `legalcode-shareholders-agreement-review` |

### Step 10: Deliver Output

Structure the final output using the Output Format Template at the end of this skill.

---

## Module A: Instrument Comparison Reference

### Decision Matrix

Use this matrix to identify the starting recommendation before deep analysis:

| Factor                     | SAFE                                    | ASA                                     | Convertible Note          | Priced Equity                                                |
| -------------------------- | --------------------------------------- | --------------------------------------- | ------------------------- | ------------------------------------------------------------ |
| **Debt?**                  | No                                      | No                                      | Yes (debt)                | No                                                           |
| **Interest**               | None                                    | None                                    | 5–8% typical              | N/A                                                          |
| **Maturity risk**          | None                                    | 6 mo longstop (HMRC)                    | 18–36 months              | N/A                                                          |
| **Conversion trigger**     | Qualified financing / IPO / dissolution | SEIS/EIS-qualifying event + financing   | Qualified financing       | Immediate                                                    |
| **Investor protection**    | Cap ± discount                          | Implicit cap                            | Cap + discount + interest | Liquidation preference, anti-dilution, protective provisions |
| **Documentation**          | 2–5 pages                               | 3–6 pages                               | 10–20 pages               | 50–100+ pages                                                |
| **Closing speed**          | Days                                    | Days                                    | 1–2 weeks                 | 3–8 weeks                                                    |
| **US market share (2024)** | 91% of pre-priced                       | N/A                                     | 9% of pre-priced          | All priced rounds                                            |
| **Tax incentive fit**      | Limited (QSBS via C-Corp)               | SEIS/EIS (UK)                           | Limited                   | QSBS (US); SEIS/EIS (UK); CCPS (India)                       |
| **Jurisdiction fit**       | US-primary                              | UK/EU-primary                           | Flexible                  | All                                                          |
| **Best for**               | US early-stage, speed, simplicity       | UK/EU early-stage, SEIS/EIS eligibility | Bridge/gap financing      | Post-traction, institutional investors                       |

### Primary Selection Rules

Apply these rules in priority order:

1. **UK company + SEIS/EIS investors** → ASA (not SAFE — SAFE is not a recognized SEIS/EIS vehicle)
2. **US company + US VCs / angels at seed** → Post-money SAFE (YC standard)
3. **Existing debt on cap table or maturity concern** → Avoid convertible note; prefer SAFE or direct equity
4. **Series A+ with institutional VCs** → Priced equity round (SAFEs/notes convert)
5. **Bridge financing between priced rounds** → Convertible note or SAFE, depending on jurisdiction
6. **Indian company + foreign investors** → CCPS or convertible notes under FEMA automatic route
7. **Singapore company + institutional APAC investors** → Priced preferred shares (Singapore Pte Ltd)
8. **EU company (non-UK) + EU investors** → Local variant; check Prospectus Regulation exemptions
9. **Cross-border US + UK investors** → Structure under US law (Delaware C-Corp); UK investors use
   SAFE, note SEIS/EIS loss for those investors unless flip-up to US C-Corp is completed

---

## Module B: SAFE Deep Dive

### Overview

A **Simple Agreement for Future Equity (SAFE)** is a non-debt instrument that grants the right to
receive equity upon a future priced financing or exit event. Introduced by Y Combinator in 2013;
post-money SAFE variant introduced in 2018 and now dominant.

### Post-Money vs. Pre-Money SAFEs

| Feature                      | Post-Money SAFE (current standard)                      | Pre-Money SAFE (legacy)                 |
| ---------------------------- | ------------------------------------------------------- | --------------------------------------- |
| **Ownership calculation**    | Fixed at signing: Investment ÷ Post-Money Valuation Cap | Variable — depends on all SAFEs issued  |
| **Investor knows ownership** | Yes — immediately                                       | Only at conversion                      |
| **Subsequent SAFE dilution** | Borne by founders, not prior SAFE investors             | All SAFE holders diluted by new SAFEs   |
| **Market adoption**          | Dominant (YC standard since 2018)                       | Legacy; being replaced                  |
| **Founder impact**           | More dilution if many SAFEs stack                       | Less dilution per SAFE, but uncertainty |

**Recommendation**: Default to post-money SAFE (YC standard form) unless there is a specific
reason to deviate. Custom SAFEs require careful analysis of conversion mechanics.

### Key Terms to Review

**Valuation Cap**

- Definition: Maximum company valuation at which the SAFE converts to equity
- Formula: SAFE Shares = Investment Amount ÷ (Lower of: Cap Price or Discount Price)
- Cap Price = Post-Money Valuation Cap ÷ Fully-Diluted Post-Money Cap Table Shares
- **COMPLIANT**: Cap set at a premium to current company value, reflecting startup risk
- **FLAG**: Cap at or below current fair market value (no investor reward for early risk)
- **FLAG**: No cap on an uncapped SAFE without MFN protection (investor bears unlimited upside risk without floor)

**Discount Rate**

- Definition: Percentage discount applied to Series A price if lower than the cap calculation
- Typical range: 15–25% (most common: 20%)
- **COMPLIANT**: 20% discount is market standard
- **FLAG**: Discount > 30% is aggressive; may signal over-generous terms to early investors
- **FLAG**: Discount absent and no cap (uncapped, no-discount SAFE) — no investor protection

**MFN (Most Favored Nation) Clause**

- Definition: If the company issues a subsequent convertible on better terms, the SAFE holder
  may elect to amend their SAFE to match those terms
- **COMPLIANT**: Present on uncapped or minimal-protection SAFEs
- **FLAG**: Absent on an uncapped SAFE — early investor lacks protection against better terms
  granted to later investors
- **Mechanics**: Investor receives written notice; has [X] days to elect MFN amendment

**Pro-Rata Rights**

- Definition: Right (not obligation) to invest in future priced rounds to maintain ownership %
- Formula: Pro-Rata Amount = Current SAFE Ownership % × Total New Round Size
- **COMPLIANT**: Present for significant investors ($100k+ SAFEs is common threshold)
- **FLAG**: Absent for lead investors who expect to participate in Series A
- **FLAG**: Pro-rata extends to ALL future rounds (may create problems at Series B/C)

**Conversion Events**

| Event                     | Mechanics                                                                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Equity Financing**      | Converts to shadow preferred stock (same rights as Series A preferred, minus amount) OR into the next round at cap/discount — whichever benefits investor most |
| **Liquidity Event (IPO)** | Cash out at cap value OR convert to common at IPO price — investor's choice                                                                                    |
| **Dissolution**           | Receives cash from dissolution proceeds, pari passu with other SAFE holders, before common                                                                     |
| **Change of Control**     | Cash out at cap value (typically 1× investment at minimum)                                                                                                     |

**Review Flag**: Many custom SAFEs have non-standard conversion mechanics. Verify:

- Does "Equity Financing" definition include a minimum raise threshold (e.g., >$1M)?
- Is "Liquidity Event" defined to include standard exit scenarios?
- Is dissolution priority explicitly stated?

### QSBS Compatibility (US)

For QSBS eligibility, the underlying company must be a C-Corporation. SAFEs issued by an
S-Corp, LLC, or partnership do not generate QSBS stock upon conversion. [VERIFY: IRC § 1202(c)]

---

## Module C: ASA Deep Dive

### Overview

An **Advance Subscription Agreement (ASA)** is a UK/EU instrument under which an investor pays
cash now for shares to be issued in the future. Not debt; no interest. The primary use case is
early-stage UK companies seeking SEIS/EIS-compatible investment.

### HMRC Qualifying Conditions for SEIS/EIS

**Non-negotiable requirements** (failure on any one = loss of SEIS/EIS relief):

| Condition               | Requirement                                       | Common Failure Mode                                               |
| ----------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| **No interest**         | Zero interest charges under any circumstances     | ASA with "late subscription fee" interpreted as interest          |
| **Non-refundable**      | Funds non-refundable under ANY circumstances      | "Refund if shares not issued by longstop" clause                  |
| **Non-assignable**      | ASA cannot be varied, cancelled, or assigned      | Transfer or assignment provisions                                 |
| **Longstop date**       | Maximum 6 months from ASA date for HMRC comfort   | Longstop > 6 months; HMRC unlikely to grant advance assurance     |
| **Simple subscription** | Must be a simple agreement to subscribe new funds | Investor protections that resemble investment instrument features |
| **Not debt conversion** | Cannot convert existing debt to shares            | Using ASA to convert existing loan                                |

[VERIFY: HMRC VCM12025 (EIS ASA); HMRC VCM33025 (SEIS ASA) — verify current HMRC guidance before relying on these thresholds]

### Advance Assurance Process

- **What it is**: HMRC confirmation that the arrangement is likely to qualify for SEIS/EIS relief
- **Mandatory?**: No — but strongly recommended for investor confidence and fundraising
- **When to apply**: Before the ASA is entered into (not after)
- **Processing time**: Typically 4–8 weeks (may be longer during peak periods) [VERIFY: current HMRC processing times]
- **Application form**: HMRC SEIS1/EIS1 application
- **Benefit**: De-risks the investment for angels; enables tax relief marketing

**⟁ CLARIFY** — If the user is evaluating an ASA and advance assurance has not been obtained,
ask: "Has HMRC advance assurance been obtained for this ASA? If not, the investor bears the risk
that the arrangement is later found not to qualify for SEIS/EIS relief. Do you want guidance on
how to apply?"

### ASA vs. SAFE Comparison

| Feature                 | UK ASA                       | US SAFE                  |
| ----------------------- | ---------------------------- | ------------------------ |
| **SEIS/EIS compatible** | Yes (if HMRC conditions met) | No                       |
| **Interest**            | Prohibited                   | None by default          |
| **Maturity / longstop** | 6 months (HMRC comfort)      | No maturity              |
| **Refundability**       | Never (HMRC requirement)     | N/A (equity-like)        |
| **Conversion trigger**  | SEIS/EIS qualifying event    | Qualified financing      |
| **Discount / cap**      | Typically included           | Typically cap ± discount |
| **Jurisdiction**        | UK/EU (primarily)            | US (primarily)           |

### Key Review Flags for ASAs

**FLAG — Interest provision**: Any clause that could be interpreted as charging interest or
providing a guaranteed minimum return is a disqualifying risk for SEIS/EIS.

**FLAG — Refund trigger**: Any circumstance under which funds could be returned to the investor
before share issuance disqualifies the arrangement.

**FLAG — Longstop > 6 months**: HMRC has indicated that longstops exceeding 6 months make
advance assurance unlikely. Renegotiate to ≤ 6 months.

**FLAG — Assignment or novation**: Any provision permitting transfer of the ASA to another
party risks disqualification.

**NON-COMPLIANT — Debt conversion**: Using an ASA to convert existing debt into shares is
explicitly excluded from HMRC's qualifying treatment. Use a separate debt-for-equity swap
structure with appropriate legal advice.

---

## Module D: Convertible Note Deep Dive

### Overview

A **convertible note** is a debt instrument that converts to equity upon a qualifying financing
event. Unlike a SAFE, it accrues interest and has a maturity date.

### Key Terms to Review

**Interest Rate**

- Market range: 5–8%; most common 5–6% (US); varies by jurisdiction
- Accrual: Simple interest (not compound) accumulates to principal
- Economic effect: Investor receives more shares at conversion than principal alone would generate
- **FLAG**: Interest rate > 8% on a seed-stage note is above market
- **FLAG**: Compound interest compounds in investor's favor; founders should prefer simple interest

**Maturity Date**

- Market range: 18–36 months
- **Maturity scenarios:**
  1. **Conversion**: Company raises a qualified financing before maturity → converts
  2. **Repayment**: Company repays principal + accrued interest in cash (requires reserves)
  3. **Extension/Renegotiation**: No financing, no cash → forced renegotiation (often costly)
- **FLAG**: Maturity < 18 months on a pre-seed company is high risk; limited time to raise
- **FLAG**: No extension mechanism — company has no negotiating room if round is delayed
- **NON-COMPLIANT for SEIS/EIS**: Convertible notes are debt instruments and do not qualify
  for UK SEIS/EIS relief without specific structuring [VERIFY: ITA 2007 Part 5A, 5B]

**Qualified Financing Threshold**

- Definition: The minimum round size that triggers automatic conversion
- Typical range: $500k–$2M (varies by round size and note terms)
- **FLAG**: Threshold set too high (company may raise a meaningful round without triggering
  conversion — leaves notes outstanding as overhang)
- **FLAG**: Threshold set too low (micro-rounds trigger conversion prematurely at low valuation)

**Conversion Mechanics**

- Conversion price: Lower of (a) valuation cap price or (b) discount to round price
- Formula: Shares = (Principal + Accrued Interest) ÷ Conversion Price
- **Review**: Confirm whether accrued interest also converts (market standard is yes)

**Redemption Rights**

- Most convertible notes include a right for the noteholder to demand cash repayment at maturity
  if the qualified financing has not occurred
- **FLAG**: No redemption right can create a "zombie note" outstanding indefinitely
- **FLAG**: Automatic acceleration on change of control without conversion option can be punitive

### Maturity Risk Assessment

Assess maturity risk by scoring these factors:

| Factor                         | Low Risk                           | High Risk                                |
| ------------------------------ | ---------------------------------- | ---------------------------------------- |
| Time to maturity               | >24 months remaining               | <6 months remaining                      |
| Company's fundraising pipeline | Strong/ongoing                     | None / uncertain                         |
| Note overhang                  | Single note                        | Multiple notes with staggered maturities |
| Extension mechanism            | Negotiated extension right in note | No extension mechanism                   |
| Redemption on maturity         | Cash reserves available            | No cash reserves                         |

**⟁ CLARIFY** — If the maturity date is within 6 months, flag proactively:
"This note matures on [date], which is [X] months away. If a qualified financing does not occur
before then, the company will face a choice between cash repayment, renegotiation, or technical
default. Is the company actively fundraising? Do you want to discuss extension or amendment
options?"

---

## Module E: Priced Round Overview

### When to Use This Module

Use Module E for a high-level priced round orientation. For deep term-sheet analysis, route to
`legalcode-term-sheet-analysis`.

### Option Pool Shuffle (Critical Red Flag)

**Definition**: Expansion of the employee option pool as part of pre-money capitalization,
before the investment is calculated.

**Impact**: Dilutes founders and all existing shareholders, not the incoming investors. The entire
cost of the new option pool is borne by pre-investment holders.

**Example**:

- Pre-money valuation: $10M
- New option pool: 10% of post-money (added pre-money)
- Effective pre-money per founder share: reduced by ~10%

**Review flag**: Term sheet requires option pool expansion pre-money → FLAG. Argue for:
(a) post-money pool (dilutes everyone including new investors), or
(b) smaller pool justified by 12-month bottoms-up hiring plan.

### Anti-Dilution Summary

| Mechanism                               | Founder Impact                                          | Market Status                        |
| --------------------------------------- | ------------------------------------------------------- | ------------------------------------ |
| **Broad-Based Weighted Average (BBWA)** | Proportional adjustment; moderate downside protection   | Market standard                      |
| **Narrow-Based Weighted Average**       | More aggressive than BBWA; greater preferred protection | Disfavored                           |
| **Full Ratchet**                        | Severe dilution to founders in any down round           | Rare in 2024; reject if possible     |
| **No anti-dilution**                    | No protection for investors                             | Rare; negotiable upside for founders |

**Review flag**: Full ratchet → NON-COMPLIANT with market standard. Demand BBWA.

### Liquidation Preference Summary

| Structure                        | Founder Impact                                          | Prevalence               |
| -------------------------------- | ------------------------------------------------------- | ------------------------ |
| **1× non-participating**         | Preferred get 1× first; all share remainder             | Market standard          |
| **1× participating (capped 2×)** | Preferred get 1×, then participate up to 2× cap         | Common; acceptable       |
| **1× participating (uncapped)**  | Preferred get 1× then full pro-rata — "double-dip"      | Aggressive; negotiate    |
| **2× non-participating**         | Preferred get 2× before founders see anything           | Aggressive; push back    |
| **>2× participating uncapped**   | Founders rarely see meaningful proceeds until high exit | Reject unless distressed |

Route to `legalcode-term-sheet-analysis` for full liquidation waterfall modeling.

---

## Module F: Cross-Border Structuring

### US Delaware C-Corp Formation

**Why Delaware?**

- Most VC funds require Delaware C-Corp (legal infrastructure, court predictability)
- Required for QSBS (IRC § 1202(c)(1): must be domestic C-Corporation)
- Required for standard NVCA term sheet documents
- DGCL provides broad preference share flexibility (§§ 151–154)

**Key steps:**

1. Incorporate as Delaware C-Corp (not LLC, not S-Corp — both disqualify from QSBS)
2. Issue Common Stock to founders (low FMV at founding; 83(b) election within 30 days)
3. File Section 1202 "qualified small business" records at time of each issuance
4. Confirm gross assets ≤ $50M at issuance (including proceeds of new round)
5. Issue to US persons for QSBS — non-US investors do not benefit from QSBS on US stock

### Flip-Up to Delaware C-Corp

When a UK/EU/other company needs to restructure as a US holding company for US VC:

**Common scenario**: UK Ltd has SEIS/EIS shareholders → wants to flip to Delaware C-Corp.

**Key issues:**

- SEIS/EIS shares cannot be transferred without risking relief clawback [VERIFY: ITA 2007 s.209]
- Flip-up may require HMRC clearance for existing SEIS/EIS investors
- US investors receive Delaware C-Corp shares (QSBS-eligible); UK investors remain in UK entity
  (EIS-eligible) — "parallel structure" or sequential raise
- Tax year alignment and US corporate governance requirements

**⟁ CLARIFY** — If the user has existing SEIS/EIS investors and is considering a flip-up, ask:
"Existing SEIS/EIS shareholders cannot transfer their shares without potentially triggering
clawback of their tax relief. Before proceeding with a flip-up analysis, can you confirm: How
many SEIS/EIS shareholders are there, and have they all held for the minimum 3-year period?"

### Singapore Holding Structure

**When to use:** APAC-focused company; Singapore as regional hub; fund structure accessing
MAS-regulated capital.

**Key features:**

- Singapore Pte Ltd: private company limited by shares
- Can issue preference shares, option pools under standard documents
- MAS VCFM regime: simplified licensing for VC fund managers
- Tax incentives: Sections 13H, 13O, 13U, 13X for qualifying fund income [VERIFY: Singapore Income Tax Act]
- Section 13H: Approved venture capital fund — investment income exemption
- GIP (Global Investor Programme) and EntrePass for founder immigration

### Cayman Islands Holding Company

**When to use:** Multi-jurisdictional investor base; fund-of-funds structure; pre-IPO holding.

**Key features:**

- No corporate income tax in Cayman
- Standard for offshore fund structures investing in Asian markets
- "VIE structure" in China: Cayman holding → Wholly Foreign-Owned Enterprise (WFOE) → VIE
- Not QSBS-eligible (non-US entity)
- Not SEIS/EIS-eligible (non-UK entity)

### India (FEMA) Investment Routing

**Foreign Direct Investment (FDI) via Automatic Route:**

- No Government/RBI approval required for most startup-sector investments
- Must comply with sectoral caps and pricing guidelines
- Investment must flow through an RBI-recognized Authorized Dealer (Category I) bank
- FC-GPR reporting within 30 days of share allotment [VERIFY: RBI FEMA NDI Rules 2019]

**CCPS (Compulsorily Convertible Preference Shares):**

- Preferred instrument for foreign investors in Indian startups
- Avoids FEMA restrictions on non-convertible preference shares
- Liquidation preference-like economics achievable within FEMA compliance
- Must convert within a defined period (typically 10–20 years)

**Pricing constraints:**

- FDI pricing cannot be below fair value (DCF or NAV basis)
- SAFEs with no defined valuation at time of issuance may create RBI compliance uncertainty
- Uncapped convertible instruments require documentation of valuation basis

**⟁ CLARIFY** — For India-bound foreign investment, ask: "Is the investment from a SEBI-registered
Foreign Venture Capital Investor (FVCI), or from an individual/fund investing via the FDI automatic
route? The compliance path differs significantly."

---

## Module G: Securities Exemptions

### United States

**Rule 506(b) — No General Solicitation**

| Feature               | Detail                                                                             |
| --------------------- | ---------------------------------------------------------------------------------- |
| Capital limit         | Unlimited                                                                          |
| Investor types        | Accredited investors (unlimited) + up to 35 sophisticated non-accredited investors |
| General solicitation  | Prohibited                                                                         |
| Verification standard | "Reasonable belief" of accredited status                                           |
| Most common for       | Traditional VC (relationships-based; no advertising)                               |

[VERIFY: Securities Act § 4(a)(2); Reg D Rule 506(b)]

**Rule 506(c) — General Solicitation Permitted**

| Feature               | Detail                                                                        |
| --------------------- | ----------------------------------------------------------------------------- |
| Capital limit         | Unlimited                                                                     |
| Investor types        | Accredited investors ONLY (no non-accredited investors)                       |
| General solicitation  | Permitted (advertising, social media, public events allowed)                  |
| Verification standard | Strict verification required (income tax returns, W-2, bank statements, etc.) |
| Most common for       | Token sales, AngelList syndicates, broadly-marketed equity crowdfunding       |

**Accredited Investor Definition (2024)** [VERIFY: Reg D Rule 501(a)]:

- Individual net worth ≥ $1M (excluding primary residence), or
- Individual annual income ≥ $200k (≥ $300k joint with spouse), for 2 years + expectation of same, or
- Institutional investors (banks, funds, endowments, registered investment companies), or
- "Knowledgeable employees" of a fund, or
- Entities with >$5M assets; family offices with >$5M assets

**Regulation A+ (Mini-IPO)**

| Tier   | Annual Cap | Requirements                                      |
| ------ | ---------- | ------------------------------------------------- |
| Tier 1 | $20M       | State filing; less ongoing reporting              |
| Tier 2 | $75M       | Audited financials; ongoing reporting obligations |

**Regulation CF (Equity Crowdfunding)**

- Maximum: $5M per 12-month period [VERIFY: Reg CF Rule 100]
- Must use SEC-registered broker/dealer or funding portal
- Available to general public (non-accredited investors welcome)
- Resale lock-up: 12 months post-purchase
- Disclosure: Form C filing required

### United Kingdom

**Financial Services and Markets Act 2000 (FSMA) s.86 exemptions** [VERIFY: FSMA 2000 s.86]:

| Exemption                                   | Condition                                                                 |
| ------------------------------------------- | ------------------------------------------------------------------------- |
| Qualified investors only                    | Offering restricted to "qualified investors" as defined in FSMA           |
| < 150 non-qualified investors per EEA state | Limited retail participation                                              |
| Minimum denomination ≥ £100,000             | Institutional-size denomination                                           |
| Total consideration < £8M (12 months)       | Small company exemption; varies with Prospectus Regulation implementation |

**FCA Authorised Persons**: Companies offering shares must either have FCA authorization or use
an FCA-authorized person as intermediary (e.g., a regulated crowdfunding platform).

### European Union

**Prospectus Regulation (EU) 2017/1129 Art. 1(4) exemptions** [VERIFY]:

| Exemption                                      | Condition                                |
| ---------------------------------------------- | ---------------------------------------- |
| Qualified investors only                       | No retail investor participation         |
| < 150 non-qualified investors per member state | Limited retail                           |
| Denomination ≥ €100,000 per unit               | Institutional-size                       |
| Total consideration < €8M (12 months)          | SME threshold (varies by member state)   |
| Employee share schemes                         | Shares offered to employees or directors |

**Note**: Member states may layer national rules above the Regulation minimum. Local counsel
essential for member-state-specific exemption compliance.

### Singapore

**Securities and Futures Act (SFA) Exemptions** [VERIFY: SFA Part XIII]:

| Exemption                                      | Condition                                           |
| ---------------------------------------------- | --------------------------------------------------- |
| Accredited investor                            | High-net-worth individual or institutional investor |
| Institutional investor                         | Banks, insurers, regulated fund managers            |
| Small offering (< 50 investors; $5M threshold) | Restriction on public circulation                   |
| Private placement                              | Not made to the public; standard for VC rounds      |

### India (FEMA)

Investment from foreign investors into Indian startups is governed by FEMA, not securities law
exemptions per se. The key compliance is FDI route compliance (automatic vs. approval route)
rather than a prospectus exemption framework.

---

## Module H: Tax Incentive Routing

### US: QSBS (Qualified Small Business Stock) — IRC § 1202

**Eligibility conditions** [VERIFY: IRC § 1202(c)–(d)]:

| Condition         | Requirement                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Entity type       | C-Corporation (not LLC, S-Corp, or partnership)                                                                               |
| Gross assets      | ≤ $50M at the time of issuance AND after giving effect to the issuance                                                        |
| US domestic       | Must be a domestic (US) corporation                                                                                           |
| Active business   | Must be in a qualifying trade or business (not financial services, hospitality, law, health, etc.) [VERIFY: IRC § 1202(e)(3)] |
| Original issuance | Stock must be acquired at original issuance (not secondary market)                                                            |
| Holding period    | Must hold for > 5 years from acquisition date                                                                                 |
| Taxpayer type     | Individual US taxpayers (not C-Corps, partnerships structured as C-Corp blockers)                                             |

**Tax benefit**: Gain from qualified stock sale excluded from federal income tax (100% exclusion for shares acquired after September 27, 2010) up to the greater of $10M or 10× basis [VERIFY: IRC § 1202(b)].

**Key planning points:**

- Issue C-Corp stock, not SAFE or convertible note — clock starts at _conversion_ to stock for
  note/SAFE holders, not at note/SAFE issuance
- File § 1202 documentation at each issuance; confirm gross asset compliance
- Non-US investors do not benefit from QSBS (they are not US taxpayers)
- AMT preference item risk: 7% of excluded gain may be an AMT preference [VERIFY: IRC § 57(a)(7)]
- State tax: California and some states do not conform to § 1202 exclusion [VERIFY]

**⟁ CLARIFY** — To assess QSBS eligibility, ask:
"Can you confirm: (1) the company is a Delaware C-Corp? (2) The company had gross assets ≤ $50M
immediately before and after this investment? (3) The company is engaged in a qualifying business
(technology, manufacturing, biotech — not law, finance, or health services)? (4) The investors
are individual US taxpayers?"

### UK: SEIS (Seed Enterprise Investment Scheme) — ITA 2007 Part 5B

**Company qualifying conditions** [VERIFY: ITA 2007 ss.257A–257HJ]:

| Condition                  | Requirement                                                |
| -------------------------- | ---------------------------------------------------------- |
| Age                        | ≤ 3 years old from first commercial trade                  |
| Employees                  | < 25 full-time equivalent employees                        |
| Gross assets               | ≤ £350,000 (before the investment)                         |
| Total SEIS raises          | Maximum £250,000 cumulative                                |
| UK permanent establishment | Company must carry on trade wholly or mainly in UK         |
| Qualifying trade           | Must not be a disqualified activity                        |
| Share type                 | Ordinary (not preference) shares [VERIFY: ITA 2007 s.257D] |

**Investor tax relief:**

- **50% income tax relief** on investment (up to £200,000 per year) [VERIFY: ITA 2007 s.257AB]
- **Capital gains exemption**: Gains on SEIS shares exempt if held ≥ 3 years
- **Loss relief**: If company fails, loss after relief is deductible against income tax

**SEIS structuring constraints:**

- No cumulative preference dividends (disqualifies)
- No guaranteed return provisions
- ASA must comply with HMRC conditions (see Module C)

### UK: EIS (Enterprise Investment Scheme) — ITA 2007 Part 5A

**Company qualifying conditions** [VERIFY: ITA 2007 ss.156–257]:

| Condition                  | Requirement                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------- |
| Age                        | < 7 years from first commercial sale (< 10 years for knowledge-intensive companies) |
| Employees                  | < 250 FTE (< 500 for knowledge-intensive)                                           |
| Gross assets               | ≤ £15M (before) / ≤ £16M (after)                                                    |
| Total EIS raises           | Maximum £12M lifetime (£20M for knowledge-intensive, from April 2026) [VERIFY]      |
| UK permanent establishment | Required                                                                            |
| Qualifying trade           | No disqualified activities                                                          |

**Investor tax relief:**

- **30% income tax relief** on investment (up to £1M per year; £2M if knowledge-intensive)
- **Capital gains deferral**: Invest in EIS within 1 year before or 3 years after a capital gain
  to defer CGT
- **IHT relief**: EIS shares may qualify for Business Property Relief after 2-year hold [VERIFY]
- **Loss relief**: Losses net of relief deductible against income

**Advance assurance**: Apply to HMRC before fundraising for confirmation of likely qualification.

### UK: EMI (Enterprise Management Incentives) — ITEPA 2003 Schedule 5

**Company qualifying conditions** [VERIFY: ITEPA 2003 Sch. 5]:

| Condition                  | Requirement                |
| -------------------------- | -------------------------- |
| Employees                  | < 250 FTE                  |
| Gross assets               | ≤ £30M                     |
| Qualifying trade           | No disqualified activities |
| UK permanent establishment | Required                   |

**Employee benefits:**

- Options granted at market value → no income tax or NIC on exercise [VERIFY]
- Capital gain on sale taxed at CGT rates (10% with BADR if held ≥ 24 months) [VERIFY]
- Annual individual limit: £250,000 EMI options outstanding per employee [VERIFY]
- Company limit: £3M total EMI options outstanding [VERIFY]

**vs. Unapproved (NSO equivalent) options:**

- Unapproved options: income tax + NIC on exercise spread (AME equivalent)
- EMI: no income tax on exercise (only CGT on ultimate gain)
- EMI advantage: significant tax saving (up to 47% PAYE vs. 10/20% CGT)

### Singapore: Tax Incentives

**Section 13H — Approved Venture Capital Fund** [VERIFY: Singapore Income Tax Act s.13H]:

- Investment income exemption for qualifying Singapore-incorporated VC funds
- Must obtain MAS approval as approved venture capital fund
- Income derived from disposal of qualifying investments exempt

**Sections 13O/13U — Fund Tax Exemption Frameworks** [VERIFY]:

- 13O (Onshore Fund Tax Incentive): Singapore-based funds with minimum AUM requirements
- 13U (Enhanced-Tier Fund Tax Incentive): Large funds (S$50M+) with enhanced exemptions
- Both: Exemption on qualifying income; concessionary rates on fund management fees

**FMI Scheme (Fund Management Incentive)**: 5% concessionary corporate tax rate for
qualifying fund managers [VERIFY: EDB/MAS scheme terms]

### India: Tax and FEMA Routing

**No direct equivalent to QSBS or EIS/SEIS** for foreign investors in Indian companies.

**Key considerations:**

- India does not offer income tax relief on early-stage investment for foreign investors
- CCPS structuring provides preferred economics within FEMA constraints
- Angel Tax (Section 56(2)(viib)) [VERIFY: Income Tax Act]: Startups recognized by DPIIT may
  be exempt from Angel Tax on premium valuations — confirm DPIIT recognition
- Startup India recognition: DPIIT-recognized startups may access regulatory benefits

---

## Module I: Employee Equity Comparison

### US: ISO vs. NSO

| Feature                 | ISO (Incentive Stock Option)                               | NSO (Non-Qualified Stock Option)                                  |
| ----------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- |
| **Eligible recipients** | Employees only                                             | Employees, directors, contractors, advisors                       |
| **Tax at grant**        | None                                                       | None                                                              |
| **Tax at exercise**     | None (regular); AMT preference                             | Ordinary income = spread (FMV - exercise price)                   |
| **Tax at sale**         | Long-term CGT if hold ≥ 2yr from grant + 1yr from exercise | LT or ST capital gain on spread from exercise price to sale price |
| **Max annual vesting**  | $100K/year rule [VERIFY: IRC § 422(d)]                     | No limit                                                          |
| **QSBS interaction**    | Exercised ISO shares may qualify for QSBS [VERIFY]         | Exercised NSO shares may qualify for QSBS [VERIFY]                |
| **409A requirement**    | Exercise price ≥ 409A FMV required                         | Same                                                              |
| **Employer deduction**  | No deduction (ISO)                                         | Deduction equal to ordinary income recognized by employee         |

**83(b) Election:**

- Available for restricted stock (RSAs) and early-exercise options
- File within 30 days of grant/exercise — NO exceptions, NO extensions
- Elects to recognize ordinary income NOW on the unvested spread (typically near zero at grant)
- Benefit: Converts subsequent appreciation to capital gain; starts holding periods immediately
- Risk: If shares are forfeited, no refund of tax paid
- **Critical action**: Always advise founders and early employees to evaluate 83(b) at grant

**409A Valuation:**

- Options must be granted at not less than FMV per share (as of grant date)
- FMV determined by independent 409A appraisal (annual, or after material events)
- "Safe harbor" requires independent appraisal from qualified appraiser
- Failure: Immediate income inclusion + 20% penalty tax on all unvested options [VERIFY: IRC § 409A]

### UK: EMI vs. Unapproved Options

See Module H (ITEPA 2003 Schedule 5 summary above).

**Key comparison:**

| Feature           | EMI                                  | Unapproved (NSO equivalent)     |
| ----------------- | ------------------------------------ | ------------------------------- |
| Tax at exercise   | None (if at market value)            | Income tax + NIC on spread      |
| Tax at sale       | CGT (10% BADR / 20% standard)        | CGT on gain from exercise price |
| Company size      | < 250 FTE; gross assets < £30M       | No restriction                  |
| Eligibility       | Employees only (committed time rule) | Anyone                          |
| Advance assurance | Recommended                          | N/A                             |

### Vesting Schedule Norms

**Market standard**: 4 years total / 1 year cliff (25% vests at 12-month anniversary; remaining
75% vests monthly or quarterly over 36 months)

**Acceleration provisions:**

| Type                | Mechanics                                                               | Market Status                                         |
| ------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------- |
| **Single-trigger**  | Accelerates on change of control alone                                  | Disfavored by investors (removes retention incentive) |
| **Double-trigger**  | Accelerates only if (1) change of control AND (2) employment terminated | Market standard                                       |
| **No acceleration** | Unvested shares treated per plan on CoC (assumption/cash-out)           | Depends on plan terms                                 |

**Option pool sizing norms by stage:**

| Stage     | Typical Pool Size                         |
| --------- | ----------------------------------------- |
| Pre-seed  | 10–15% post-money                         |
| Seed      | 10–15% post-money                         |
| Series A  | 10–15% (often refreshed to 10% at series) |
| Series B+ | 5–10% refresh                             |

**⟁ CLARIFY** — If the option pool has been created pre-money at a size > 15%, ask:
"The option pool is [X]% and is being included pre-money. This creates hidden founder dilution
beyond what the stated pre-money valuation suggests. Do you want a dilution analysis showing the
effective per-share price after the option pool shuffle?"

---

## Instrument Classification System

### For Document Review (SAFE, ASA, Note)

**COMPLIANT**: Term meets the applicable standard or statutory requirement. No action needed.

**FLAG**: Term diverges from market standard, tax-incentive requirement, or regulatory norm.
Generate specific commentary and recommended revision. Assess business impact.

**NON-COMPLIANT**: Term violates a statutory requirement, regulatory rule, or market standard
so fundamental that it creates material legal or tax risk. Explain the specific violation,
state the applicable rule, provide market-standard replacement language, and recommend
immediate resolution.

### For Instrument Selection

**OPTIMAL**: Best fit for the company's jurisdiction, stage, investor base, and tax goals.
Recommend with confidence.

**SUBOPTIMAL**: Functional but leaves efficiency on the table (speed, tax, investor protection,
or legal simplicity). Recommend the superior alternative and explain the trade-off.

**INCOMPATIBLE**: Not appropriate for this situation due to legal, tax, or practical constraints.
Explain why and identify the compatible alternative.

### For Tax Incentives / Securities Exemptions

**AVAILABLE**: Company and transaction qualify. State the conditions to maintain eligibility.

**PARTIAL**: Qualification is possible but specific structural or documentary conditions must
be met. Flag the gaps and provide the remediation path.

**NOT AVAILABLE**: Company or transaction does not qualify and cannot be restructured to qualify.
Explain why and identify alternative incentives or structuring options.

---

## Negotiation and Action Priority Framework

### Tier 1 — Critical (Must Resolve Before Closing)

- Tax incentive disqualification: ASA fails HMRC SEIS/EIS conditions (FLAG → NON-COMPLIANT)
- Securities law violation: no applicable exemption for the investor type or offering method
- FEMA non-compliance: India-bound FDI without automatic route eligibility or proper pricing
- Instrument structural incompatibility: interest provision in an ASA; maturity risk within
  6 months without extension mechanism; SAFE conversion mechanics fail for QSBS clock
- 83(b) election deadline: within 30 days of grant — cannot miss this window

### Tier 2 — Important (Address Before Finalizing)

- Suboptimal instrument for tax goals (e.g., using convertible note instead of ASA for
  UK SEIS/EIS investors)
- Missing MFN on uncapped SAFE
- Pro-rata rights absent for significant investors
- Option pool pre-money vs. post-money structuring (founder dilution)
- BBWA carve-outs for employee plan issuances absent
- Anti-dilution deviating from BBWA market standard
- 409A appraisal not current (>12 months old or post-material event)

### Tier 3 — Advisory (Best Practice)

- Board observer right structuring preferences
- Information rights scope and frequency of reporting
- Minor ASA drafting improvements (non-HMRC-critical terms)
- SAFE discount rate calibration (within market range)
- Pro-rata scope limitation to preserve flexibility in future rounds

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                  | Fail Action                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every statutory claim cites a specific code section, HMRC manual reference, or regulatory rule                        | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | Citations follow a recognized format (IRC § 1202; ITA 2007 s.257AB; FEMA NDI Rules 2019)                              | Fix format                                               |
| **Currency**   | All cited thresholds and conditions checked for amendments                                                            | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the identified jurisdiction(s). No cross-contamination of US QSBS concepts into UK EIS analysis | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated. If a tax outcome or securities analysis is uncertain, flag it rather than hiding it    | Add confidence qualifier                                 |

### Self-Interrogation for NON-COMPLIANT Findings

For any finding classified as NON-COMPLIANT, apply this 3-pass review before delivering:

**Pass 1 — Statutory Chain**: Does the non-compliance follow directly from the cited statute or
HMRC guidance? Would HMRC/the SEC/SEBI actually reach this conclusion on these facts? Is there
a counter-argument that the arrangement is compliant?

**Pass 2 — Completeness**: Are there other statutory provisions or exemptions that could cure
the non-compliance? Have all relevant statutes been considered? Are there transitional or
grandfathering provisions?

**Pass 3 — Proportionality**: Is the NON-COMPLIANT classification proportionate? Could this be
a FLAG (risk but curable) rather than NON-COMPLIANT (violation requiring immediate resolution)?

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                          | Action                                                   |
| ------------ | --------- | -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statute, unambiguous condition, established HMRC/IRS guidance              | State with confidence                                    |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions                                 | State with brief caveat                                  |
| **Probable** | 0.60–0.79 | Good arguments; HMRC/IRS guidance directionally clear but specific facts unclear | State with reasoning and contra-indicators               |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations                                   | Flag for specialist tax counsel review                   |
| **Unlikely** | 0.0–0.39  | Speculative; no clear authority                                                  | Do not assert; flag "[UNCERTAIN — specialist to advise]" |

---

## Glass Box Audit Trail

Every output from this skill MUST include a Glass Box audit section:

```yaml
glass_box:
  skill: "legalcode-venture-financing-suite"
  task_type: "[Instrument selection / Document review / Tax routing / Securities / Equity / Cross-border / Full suite]"
  stage: "[Pre-seed / Seed / Series A / etc.]"
  amount: "[Amount raising, if provided]"
  jurisdiction_primary: "[US-Delaware / UK / EU / Singapore / India / Other]"
  jurisdiction_tracks_activated: "[list of tracks engaged]"
  instrument_reviewed: "[SAFE / ASA / Convertible Note / Priced Round / None]"
  modules_activated: "[A, B, C, etc.]"
  tax_incentives_analyzed: "[QSBS / SEIS / EIS / EMI / Singapore / India / None]"
  securities_exemptions_analyzed: "[Reg D 506b / 506c / UK s.86 / Prospectus Reg / MAS / FEMA / None]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-vf-authority.md or 'Not created']"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT findings)"
  findings_summary:
    critical_tier1: "[number]"
    important_tier2: "[number]"
    advisory_tier3: "[number]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  deep_skill_routes:
    - "[legalcode-term-sheet-analysis: recommended for full term sheet analysis]"
    - "[legalcode-equity-incentive-plan-review: recommended for full equity plan review]"
  limitations:
    - "[e.g., No QSBS eligibility opinion — recommend IRS PLR or tax counsel letter]"
    - "[e.g., SEIS/EIS analysis based on HMRC published guidance; advance assurance not obtained]"
  reviewer: "AI-assisted — requires qualified legal and tax review before reliance"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in venture financing analysis and structuring:

1. **Recommending SAFEs for UK SEIS/EIS investors** — SAFEs are US instruments not recognized
   by HMRC as a qualifying subscription method under SEIS/EIS. UK angels investing for SEIS/EIS
   relief must use an ASA or direct share subscription. Recommending a SAFE in this context
   loses the investor's tax relief.

2. **Treating convertible notes as SEIS/EIS-compatible** — Convertible notes are debt instruments.
   SEIS/EIS requires ordinary share subscriptions (or qualifying ASAs). Do not advise UK investors
   that a convertible note qualifies for relief without verifying the specific structure.

3. **Starting the QSBS clock at SAFE issuance** — QSBS holding period begins when the underlying
   stock is issued (i.e., when the SAFE or note converts). Founders and investors who want the
   5-year QSBS clock running as early as possible should convert instruments promptly or consider
   investing directly as equity.

4. **Missing the 83(b) election window** — The 30-day window for filing a Section 83(b) election
   after receipt of restricted stock is absolute. No extensions exist. Failing to advise founders
   and early employees of this deadline is a material omission with permanent tax consequences.

5. **Ignoring the option pool shuffle** — Accepting a term sheet with a pre-money option pool
   expansion without modeling the effective dilution to founders. A "20% pre-money pool" can
   reduce the effective per-share pre-money valuation by more than a naive reading suggests.

6. **Accepting full ratchet anti-dilution** — In a down round, full ratchet dramatically dilutes
   founders and common holders. BBWA is the market standard. Full ratchet should be flagged as
   NON-COMPLIANT with current market practice and negotiated out.

7. **Overlooking ASA longstop creep** — Accepting an ASA with a longstop date exceeding 6 months
   because "we'll close before then." HMRC requires the longstop to be ≤ 6 months to give advance
   assurance. A longstop of 9–12 months creates SEIS/EIS eligibility risk for the investor even
   if the round closes in month 3.

8. **FEMA misstep on uncapped convertibles** — SAFEs issued to Indian company foreign investors
   without a defined valuation basis may violate RBI pricing guidelines (which require FDI to be
   at or above fair value). Uncapped structures need documented valuation basis.

9. **Advising non-US persons that QSBS applies to them** — IRC § 1202 applies to US federal
   income tax. Non-US investors (and many US funds structured as C-Corps) do not benefit. Do not
   advise cross-border investors that they will receive QSBS exclusion without verifying their
   US taxpayer status and entity type.

10. **Confusing SEIS and EIS conditions** — SEIS requires company ≤ 3 years old; EIS ≤ 7 years.
    SEIS cap is £250k cumulative; EIS is £12M (£20M for knowledge-intensive). SEIS relief is
    50% income tax; EIS is 30%. Conflating the schemes produces wrong investor advice.

11. **Participating liquidation preference without cap analysis** — Uncapped participating
    liquidation preference ("double-dip") means preferred investors take both their 1× first and
    a pro-rata share of all remaining proceeds. This can leave founders with near-zero proceeds
    in all but the highest exit scenarios. Always model the waterfall before accepting.

12. **Vague qualified financing threshold on convertible notes** — A qualified financing threshold
    set too high means a meaningful funding round may not automatically convert the notes, leaving
    them as overhang. A threshold set too low means small bridge rounds prematurely convert at an
    unfavorable cap price. Get the threshold right.

13. **Ignoring prior convertible notes when structuring new instruments** — Existing unconverted
    SAFEs or notes interact with new instruments. New investors receive shares; old SAFE holders
    are still unconverted. The new round may or may not trigger conversion. Failing to model this
    interaction leads to cap table surprises.

14. **California QSBS non-conformity** — California does not conform to the federal § 1202 exclusion
    as of the most recent guidance. Founders in California may owe California state income tax
    on gains that are federally excluded. Do not advise that QSBS "eliminates" all tax without
    flagging state-level non-conformity.

15. **Assuming ASA advance assurance guarantees relief** — Advance assurance is HMRC's indication
    of likely qualification, not a binding guarantee. HMRC can withdraw assurance if facts change
    or if the documents differ from the assurance application. Investors should be informed of
    this distinction.

16. **Option pool timing mismatch** — Creating the option pool post-closing (to avoid pre-money
    dilution) is a legitimate negotiating win, but it must be reflected correctly in closing
    documents and capitalization table calculations. Failing to track this creates cap table errors
    at next financing.

17. **EMI options without working time requirements** — EMI requires employees to work at least
    25 hours per week (or 75% of their working time) for the company. Part-time advisors who do
    not meet this test cannot receive EMI options. Using EMI for advisors who fall below this
    threshold disqualifies those specific options.

18. **Cross-border equity plans without local sub-plans** — A US stock option plan does not
    automatically function in the UK, Germany, France, or Singapore. Each jurisdiction requires
    a local sub-plan (or equivalent approval) to handle local income tax, social security, and
    securities law issues. Skipping this creates compliance exposure in each jurisdiction.

---

## Writing Standards

Apply plain-language discipline to all output:

**For recommendations and flags:**

- Lead with the finding, then the explanation. "This ASA charges interest — this disqualifies
  it from SEIS/EIS relief under ITA 2007 s.257D. Remove the interest provision or restructure
  as a direct share subscription."
- Active voice: "The company must confirm gross assets ≤ $50M" not "Gross assets must be
  confirmed to be ≤ $50M by the company"
- Short sentences. One point per sentence.
- Name the actor: "The investor must exercise pro-rata rights within 15 days" not "Pro-rata
  rights must be exercised within 15 days"

**For tax and securities analysis:**

- State the rule, then the application. "IRC § 1202(c)(1) requires a domestic C-Corporation.
  This company is a Delaware C-Corp — condition satisfied."
- Mark uncertainty explicitly: [VERIFY] for unconfirmed citations, [UNCERTAIN] for speculative
  conclusions
- Confidence qualifiers where appropriate

**Quality gates before delivery:**

1. Can a founder understand the executive summary without a law degree?
2. Can the investor's counsel understand and act on each FLAG/NON-COMPLIANT finding?
3. Is every statutory claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix them.
5. Could any sentence be shorter without losing meaning? If yes, shorten it.
6. Is every [JURISDICTION-SPECIFIC] marker correct and complete?

---

## External Tool Integration

**With legalcode-mcp connected:**

- In Step 4, search for jurisdiction-specific statutes, HMRC manual references, SEC releases,
  and regulatory guidance relevant to the instruments and jurisdictions activated
- Save results to `/tmp/legalcode-vf-authority.md` structured by jurisdiction track
- Verify statutory thresholds (QSBS gross asset limit, SEIS/EIS company age, EMI option limits)
  against current legalcode-mcp results — these change
- For any NON-COMPLIANT finding, search for additional authority confirming the violation
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory references with [VERIFY]
- Note `legalcode_mcp: "Not connected"` in Glass Box audit trail
- Add a prominent notice: "All statutory thresholds and conditions should be verified against
  current HMRC, IRS, SEC, MAS, and RBI guidance before reliance — limits change"
- Focus on structural and commercial analysis rather than precise statutory compliance

---

## Output Format Template

````markdown
## Venture Financing Analysis

**Company profile**: [Name / Stage / Incorporation jurisdiction]
**Task type**: [Instrument selection / Document review / Tax routing / Securities / Equity / Full suite]
**Modules activated**: [A–I as relevant]
**Jurisdiction tracks**: [US / UK / EU / SG / IN]
**Perspective**: [Founder / Investor / Counsel]
**Date of analysis**: [date]

---

### Executive Summary

[3–5 bullet points covering the highest-priority findings. Non-technical language suitable for
a founder or CFO. Lead with action items.]

---

### Instrument Recommendation

_(If instrument selection task)_

| Option           | Classification                      | Rationale |
| ---------------- | ----------------------------------- | --------- |
| SAFE             | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |
| ASA              | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |
| Convertible Note | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |
| Priced Round     | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |

**Recommended instrument**: [Name] — [1-sentence rationale]

---

### Document Review Findings

_(If document review task)_

#### Tier 1 — Critical Findings

| #   | Term        | Classification | Issue         | Recommended Action |
| --- | ----------- | -------------- | ------------- | ------------------ |
| 1   | [Term name] | NON-COMPLIANT  | [Description] | [Action]           |

#### Tier 2 — Important Findings

| #   | Term        | Classification | Issue         | Recommended Action |
| --- | ----------- | -------------- | ------------- | ------------------ |
| 1   | [Term name] | FLAG           | [Description] | [Action]           |

#### Tier 3 — Advisory Items

_(Summarize briefly; do not over-engineer)_

---

### Tax Incentive Analysis

_(If tax routing task)_

| Incentive         | Jurisdiction | Availability                        | Key Conditions to Maintain |
| ----------------- | ------------ | ----------------------------------- | -------------------------- |
| QSBS (IRC § 1202) | US           | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]               |
| SEIS              | UK           | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]               |
| EIS               | UK           | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]               |
| EMI               | UK           | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]               |
| s.13H/13O/13U     | SG           | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]               |

---

### Securities Exemption Analysis

_(If securities compliance task)_

| Exemption                     | Jurisdiction | Available?         | Conditions / Caveats |
| ----------------------------- | ------------ | ------------------ | -------------------- |
| Reg D 506(b)                  | US           | Yes / No / Partial | [Detail]             |
| Reg D 506(c)                  | US           | Yes / No / Partial | [Detail]             |
| s.86 FSMA                     | UK           | Yes / No / Partial | [Detail]             |
| Prospectus Reg (EU) Art. 1(4) | EU           | Yes / No / Partial | [Detail]             |

---

### Employee Equity Analysis

_(If equity design task)_

| Option Type | Tax Treatment | Recommended For       | Caveats     |
| ----------- | ------------- | --------------------- | ----------- |
| ISO         | [Summary]     | [Eligible recipients] | [Key risks] |
| NSO         | [Summary]     | [Eligible recipients] | [Key risks] |
| EMI         | [Summary]     | [Eligible recipients] | [Key risks] |

**83(b) election**: [Applicable / Not applicable] — [Action and deadline if applicable]
**409A valuation**: [Current / Stale / Not applicable] — [Action if needed]

---

### Cross-Border Structuring Notes

_(If cross-border task)_

[Key structuring considerations based on the jurisdiction combination identified]

---

### Recommended Next Steps

1. [Highest-priority action — Tier 1 Critical if any]
2. [Next action]
3. [Route to deeper skill if needed]

---

### Route to Deep Skills

- `legalcode-term-sheet-analysis`: [Recommended if priced round term sheet requires full analysis]
- `legalcode-equity-incentive-plan-review`: [Recommended if full option plan review needed]
- [Other routes as relevant]

---

```yaml
glass_box: [Glass Box fields as defined above]
```
````

```

---

## Localization Notes

When this skill routes to a jurisdiction outside the five primary tracks (US/UK/EU/SG/IN),
apply these principles:

1. Research the local company law for preferred share issuance and conversion mechanics
2. Identify whether local tax schemes analogous to SEIS/EIS/QSBS exist
3. Identify the applicable securities law exemption framework for private placements
4. Check for currency control or foreign investment restrictions
5. Replace [JURISDICTION-SPECIFIC] markers with verified local content
6. Add local legal terminology with English translations
7. Recommend local counsel for any jurisdiction where the skill lacks coverage

**Known gaps requiring local counsel:**
- Middle East (Sharia-compliant structures, DIFC/ADGM free zones)
- Brazil (CVM regulation, FIPE valuation rules)
- China (VIE structures, SAFE regulations — not SAFE the instrument, but China's foreign
  exchange safe rules)
- Canada (provincial securities regulation, SR&ED tax credits)
- Australia (Early Stage Innovation Company tax offsets)
- France (BSPCE — employee warrants with preferential CGT treatment)

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis from deep venture financing legal
research spanning US (YC SAFE documentation, NVCA model documents, IRC § 1202 QSBS,
Reg D exemptions), UK (HMRC VCM Manual, ITA 2007 SEIS/EIS, ITEPA 2003 EMI, BVCA model
documents), EU (Prospectus Regulation 2017/1129), Singapore (MAS regulations, Singapore
Income Tax Act), and India (FEMA NDI Rules 2019, SEBI AIF Regulations). Consolidated
from prior Legalcode skills including `legalcode-term-sheet-analysis` (jurisdiction
frameworks, instrument mechanics) and `legalcode-equity-incentive-plan-review` (ISO/NSO/EMI
analysis patterns, 409A, 83(b)). Router design enables routing to deeper specialist skills
while providing comprehensive instrument selection and tax routing as a standalone suite.
```
