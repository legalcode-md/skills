---
name: legalcode-venture-financing-uk
description: 'UK venture financing analysis and drafting skill covering the full stack of England & Wales
  early-stage and growth equity law: Advanced Subscription Agreements (ASAs/SeedFASTs), BVCA/UK Private
  Capital model documents (Feb 2025 suite), SEIS/EIS tax relief (expanded April 2026 — new limits), EMI
  options (individual limit doubled April 2026), Companies Act 2006 ss 549-561 pre-emption rights and
  Pre-emption Group Statement of Principles, new UK prospectus regime (FCA rules effective January 2026
  under FSMA 2000 as amended by FSMA 2023), convertible loan notes, term sheets, shareholder agreements,
  cap table mechanics, anti-dilution, liquidation preferences, drag/tag-along, board governance, FSMA
  2000 s.21 financial promotion restrictions, and ECCTA 2023 Companies House reforms.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

UK venture financing analysis and drafting skill covering the full stack of England & Wales early-stage and growth equity law: Advanced Subscription Agreements (ASAs/SeedFASTs), BVCA/UK Private Capital model documents (Feb 2025 suite), SEIS/EIS tax relief (expanded April 2026 — new limits), EMI options (individual limit doubled April 2026), Companies Act 2006 ss 549-561 pre-emption rights and Pre-emption Group Statement of Principles, new UK prospectus regime (FCA rules effective January 2026 under FSMA 2000 as amended by FSMA 2023), convertible loan notes, term sheets, shareholder agreements, cap table mechanics, anti-dilution, liquidation preferences, drag/tag-along, board governance, FSMA 2000 s.21 financial promotion restrictions, and ECCTA 2023 Companies House reforms. Use for: reviewing or drafting investment documents, assessing SEIS/EIS eligibility, structuring EMI option schemes, advising founders or investors on UK VC round mechanics, analysing term sheets against BVCA market standards, or building a compliance checklist for a UK fundraise.


# Legalcode UK Venture Financing

> **Disclaimer**: This skill provides a framework for AI-assisted legal and tax analysis
> of UK venture financing transactions. It does not constitute legal, tax, financial, or
> investment advice. All outputs must be reviewed by a qualified solicitor and, where
> relevant, a tax adviser (for SEIS/EIS/EMI matters) licensed in England & Wales before
> any reliance or action. Laws, HMRC guidance, FCA rules, and market practice change;
> verify current applicability. Statutory and case law references carry hallucination
> risk — verify against authoritative sources (HMRC.gov.uk, legislation.gov.uk, FCA
> Handbook, BVCA model documents) before relying on them. Nothing here constitutes
> investment advice within the meaning of FSMA 2000.

---

## Purpose and Scope

This skill analyses, drafts, and reviews UK venture financing documents and structures for
transactions governed by the laws of England and Wales.

**Covers:**

- Advanced Subscription Agreements (ASAs) including SEIS/EIS compatibility analysis
- Convertible Loan Notes (CLNs) with SEIS/EIS routing analysis
- BVCA Model Documents (Term Sheet, Investment Agreement, Shareholder Agreement — Feb 2025)
- SEIS and EIS tax relief: eligibility, compliance, advance assurance, post-investment
  filing (post-April 2026 expanded limits)
- EMI option schemes: structuring, HMRC valuation/approval, disqualifying events
  (post-April 2026 doubled individual limit)
- Companies Act 2006 pre-emption rights (ss 549–561) and disapplication mechanics
- New UK prospectus regime (FCA rules, January 2026)
- Cap table mechanics: option pools, anti-dilution, liquidation preferences
- FSMA 2000 s.21 financial promotion restrictions and VC exemptions
- ECCTA 2023 Companies House reforms affecting share issuances
- Drag-along, tag-along, reserved matters, and board governance
- Term sheet analysis against BVCA market standards

**Does not:**

- Provide investment or financial advice within the meaning of FSMA 2000
- Cover Scottish law (separate legal system), Northern Ireland, or Cayman/Delaware flip-up
  structuring (see separate skills)
- Replace qualified legal counsel for a live transaction
- Constitute HMRC advance assurance or formal tax advice

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: England and Wales
**Key legal sources**:

- Companies Act 2006 (CA 2006)
- Income Tax Act 2007 (ITA 2007), Part 5 (EIS), Part 5A (SEIS)
- Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003), Part 7 Chapter 9 (EMI)
- Financial Services and Markets Act 2000 (FSMA 2000) as amended by FSMA 2023
- Economic Crime and Corporate Transparency Act 2023 (ECCTA 2023)
- FCA Handbook: COBS, Prospectus Regulation Rules (PRR), financial promotions regime
- Pre-emption Group Statement of Principles (2022 edition, updated November 2023)
- BVCA Model Documents (Investment Agreement, SHA, Term Sheet — February 2025)

[VERIFY] All statutory provisions, HMRC guidance references, and FCA rules against
current legislation.gov.uk, HMRC.gov.uk, and FCA Handbook as of the review date.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses when:

- The answer would change the direction of the analysis
- Multiple valid instrument structures exist with different tax and legal consequences
- SEIS/EIS/EMI eligibility depends on facts only the user can provide
- The user's role (founder, lead investor, co-investor, counsel) affects perspective

Use the **⟁ CLARIFY** pattern below. If the user has already provided the information,
skip the question and proceed.

---

## Workflow

### Step 1: Accept Input and Identify the Task

Accept input in any of these formats:

- **Document(s)**: Term sheet, investment agreement, SHA, ASA, CLN, EMI option deed
- **Scenario description**: "I am a founder raising a £500K SEIS round — review my ASA"
- **Question**: "Does our EMI scheme still qualify after the April 2026 changes?"

**⟁ CLARIFY** — Identify the task type and user role before proceeding:

1. **Task type** — What do you need?
   - Review an existing document against market standards
   - Draft a new document (or specific clause)
   - Assess SEIS/EIS/EMI eligibility for a company or transaction
   - Analyse a term sheet against BVCA standards
   - Build a compliance checklist for a fundraise
   - Explain a concept or clause

2. **User's role** — Who are you?
   - Options: Founder/company, Lead investor (VC/angel), Co-investor, Counsel (for
     company), Counsel (for investor), Other
   - _Why this matters_: The entire analysis perspective flips depending on your side.
     What protects an investor harms a founder and vice versa.

3. **Round type and amount** — What stage and how much?
   - Options: Pre-seed (< £250K), Seed (£250K–£2M), Series A (£2M–£10M), Series B+
     (> £10M), Secondary / follow-on, Other
   - _Why this matters_: Determines which BVCA module applies, SEIS vs. EIS thresholds,
     and whether the new prospectus regime is relevant.

4. **Instrument** — What is the investment vehicle?
   - Options: ASA (Advanced Subscription Agreement), CLN (Convertible Loan Note),
     Straight equity (priced round), SAFE (note: US instrument — caution for UK SEIS/EIS),
     Other
   - _Why this matters_: SEIS/EIS compatibility depends critically on instrument choice.

### Step 2: Gather Legal and Tax Context

**⟁ CLARIFY** — Collect factual context needed for SEIS/EIS and EMI analysis (skip
questions already answered):

1. **Company status**: When was the company incorporated? Is it UK-resident for tax?
2. **Trade test**: Is the company carrying on a qualifying trade (for SEIS/EIS)? Any
   excluded activities (land, financial services, property development, legal/
   accountancy, energy generation subsidies)?
3. **Gross assets**: What are the company's gross assets? (SEIS: < £350K; EIS: < £15M
   pre-money [VERIFY April 2026 limits]; KIC EIS: higher limit applies [VERIFY])
4. **Employees**: How many full-time equivalent employees? (SEIS: < 25; EIS: < 250;
   KIC EIS: < 500 [VERIFY])
5. **Previous rounds**: Has the company received prior SEIS investment? (£250K lifetime
   limit per company [VERIFY April 2026]). Prior EIS? (£5M/yr, £12M lifetime limit
   [VERIFY April 2026])
6. **Investor status**: Are any investors connected persons (associates, employees,
   related parties)? Have they previously invested via SEIS?
7. **EMI context** (if applicable): Total FMV of unexercised EMI options already granted?
   (Post-April 2026: individual limit and company-wide pool [VERIFY])

If the user cannot provide some of this, proceed with assumptions stated explicitly and
note which answers would change the analysis.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to retrieve current legal authority for this analysis. If not
connected, proceed with the statutes listed below marked [VERIFY].

**Search targets for legalcode-mcp:**

- ITA 2007 Part 5A (SEIS) — current limits post-April 2026
- ITA 2007 Part 5 (EIS) — current limits, KIC provisions post-April 2026
- ITEPA 2003 Part 7 Chapter 9 (EMI) — post-April 2026 individual limit
- CA 2006 ss 549–561 (pre-emption rights)
- FSMA 2000 s.21 and Schedule 1 (financial promotions, VC exemptions)
- FCA Prospectus Regulation Rules (PRR) — January 2026 rules
- ECCTA 2023 ss 1–63 (Companies House identity verification requirements)
- HMRC SEIS/EIS Compliance Statement guidance (current)
- HMRC EMI technical guidance (current)

Save results to `/tmp/legalcode-uk-vc-authority.md` for reference throughout the analysis.

**Without legalcode-mcp**: Mark all statutory references [VERIFY]. Note:
`legalcode_mcp: "Not connected"` in the Glass Box audit trail.

### Step 4: Instrument Analysis

Analyse the investment instrument(s) based on the task type. Use the appropriate module
below. Multiple modules can be activated simultaneously.

---

## Module 1: Advanced Subscription Agreement (ASA)

### What an ASA Is

An Advanced Subscription Agreement (ASA) is a UK-native equity pre-payment instrument:
the investor pays cash upfront in exchange for the right to receive shares at a future
trigger event. It is **not a loan** — the investment is irrevocably committed to equity
with no repayment rights. This distinguishes it from a Convertible Loan Note.

The ASA was developed (by SeedLegals/SeedFAST and the Seedsummit template) specifically
to address the inadequacy of US Y Combinator SAFEs under UK law and HMRC SEIS/EIS
requirements. SAFEs may not qualify for SEIS/EIS as they do not constitute a subscription
for shares within the required timeframe [VERIFY HMRC guidance].

### Key Terms to Analyse

| Term                           | Market Standard                                                                              | RED Flags                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Discount**                   | 10–20% on next-round price                                                                   | > 30% unusual; 0% removes benefit                                                      |
| **Valuation cap**              | Optional; if used, investor converts at lower of cap-implied price or discounted round price | Cap too low can cause founder dilution surprise                                        |
| **Longstop date**              | **Must be ≤ 6 months from signing** for SEIS/EIS compliance [VERIFY current HMRC guidance]   | > 6 months = SEIS/EIS disqualification risk                                            |
| **Longstop valuation**         | Pre-agreed fallback for automatic conversion if no round by longstop                         | Missing longstop valuation leaves conversion mechanics uncertain                       |
| **Conversion triggers**        | (1) Next priced round; (2) Exit / share sale; (3) Insolvency; (4) Longstop date              | Missing exit trigger = investor stuck in perpetuity                                    |
| **Share type on conversion**   | **Must convert into Ordinary Shares** (not preference shares) for SEIS/EIS                   | Preference shares = SEIS/EIS disqualification [VERIFY]                                 |
| **Interest / repayment**       | **None** — any interest right or cash repayment option disqualifies SEIS/EIS                 | Any interest provision = RED if SEIS/EIS required                                      |
| **Pro rata rights**            | Common in investor-friendly drafts                                                           | May interact with CA 2006 s.561 pre-emption (usually disapplied by special resolution) |
| **Most Favoured Nation (MFN)** | Investor gets benefit of better terms offered to later investors                             | Check it does not create continuing financial obligation post-conversion               |

### SEIS/EIS Compatibility Checklist — ASA

| Requirement                                     | Check                                | Statutory Basis                               |
| ----------------------------------------------- | ------------------------------------ | --------------------------------------------- |
| Shares must be fully paid Ordinary Shares       | ✓ Check conversion mechanics         | ITA 2007 s.173 (EIS), s.257CA (SEIS) [VERIFY] |
| No preferential rights to assets on winding up  | ✓ Verify share class on conversion   | ITA 2007 s.173(2)(b) (EIS) [VERIFY]           |
| No right to be redeemed                         | ✓ No redemption provision            | ITA 2007 s.173(2)(c) [VERIFY]                 |
| Shares must be new shares issued by the company | ✓ Not a transfer of existing shares  | ITA 2007 s.173(1)(a) [VERIFY]                 |
| Longstop ≤ 6 months                             | ✓ **Critical** — check longstop date | HMRC SEIS/EIS guidance [VERIFY]               |
| No repayment rights                             | ✓ No cash repayment option           | ITA 2007 s.157(1)(b) (EIS) [VERIFY]           |
| Qualifying company at time of subscription      | ✓ Run eligibility check (Step 2)     | ITA 2007 ss 181–187 [VERIFY]                  |

### Severity Classification — ASA

| Item                     | GREEN                  | YELLOW                         | RED                                                      |
| ------------------------ | ---------------------- | ------------------------------ | -------------------------------------------------------- |
| Longstop ≤ 6 months      | ≤ 6 months             | 6 months exactly (borderline)  | > 6 months                                               |
| Share type on conversion | Ordinary shares        | Preference with limited rights | Preference with financial rights (SEIS/EIS disqualifier) |
| Interest / repayment     | None                   | —                              | Any interest or repayment right (SEIS/EIS killer)        |
| Discount                 | 10–20%                 | > 25%                          | —                                                        |
| Longstop valuation       | Defined                | Missing but longstop triggers  | Missing and no fallback                                  |
| MFN clause               | Absent or time-limited | Perpetual MFN                  | Creates continuing financial obligation                  |

---

## Module 2: Convertible Loan Notes (CLNs)

### CLN vs. ASA: Key Distinction

A Convertible Loan Note **is a loan** with a right to convert into equity. Interest
typically accrues. This creates SEIS/EIS structuring complications.

### SEIS/EIS Compatibility — CLNs

CLNs are **more complex** to structure for SEIS/EIS than ASAs:

- HMRC may treat the note as a loan (not a share subscription) until conversion
- Some CLN structures are compatible with EIS if structured as a qualifying convertible
  loan under ITA 2007 s.175A [VERIFY current HMRC guidance and Finance Act changes]
- SEIS is generally **not compatible** with CLNs that bear interest or have repayment
  rights [VERIFY]
- Advance assurance from HMRC is **strongly recommended** before using a CLN for
  SEIS/EIS investment

### Key CLN Terms to Analyse

| Term                               | Market Standard                                               | RED Flags                                                                |
| ---------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Principal amount**               | Face value of the note                                        | —                                                                        |
| **Interest rate**                  | 6–8% p.a. (often PIK); 0% for SEIS/EIS compatible structures  | Interest accrual = SEIS disqualifier; EIS: analyse under s.175A [VERIFY] |
| **Discount on conversion**         | 15–25% on next qualifying round                               | > 30% unusual                                                            |
| **Valuation cap**                  | Optional; investor-protective                                 | Interplay with discount — check which is more favourable                 |
| **Maturity date**                  | 12–24 months; often 18 months                                 | Short maturity (< 12 months) = pressure on company                       |
| **Qualifying financing threshold** | Usually £250K–£500K minimum round size                        | Below-market threshold may force premature conversion                    |
| **Long stop / forced conversion**  | At maturity: forced conversion at agreed price, or redemption | Redemption at maturity = distress exit for company                       |
| **Redemption option**              | Investor usually has option but rarely exercises              | Redemption in place of conversion = adverse tax treatment [VERIFY]       |
| **Security**                       | Generally unsecured; secured CLNs are unusual for VC          | Security over assets reduces SEIS/EIS qualifying status [VERIFY]         |

---

## Module 3: BVCA Model Documents (February 2025)

### Overview

The British Venture Capital Association (BVCA) maintains a suite of model investment
documents, last updated February 2025, available at [bvca.co.uk — VERIFY URL and
current edition]. The suite includes:

| Document                          | Purpose                                                        |
| --------------------------------- | -------------------------------------------------------------- |
| **Term Sheet**                    | Non-binding heads of terms                                     |
| **Investment Agreement**          | Binding subscription agreement for new shares                  |
| **Shareholders' Agreement (SHA)** | Governance and rights agreement between investors and founders |
| **Articles of Association**       | Constitutional document (Companies House filing required)      |
| **Disclosure Letter**             | Warranties qualification                                       |
| **Board Written Resolutions**     | Authorise the allotment, disapply pre-emption                  |
| **Deed of Adherence**             | New investors joining existing SHA                             |

### Term Sheet Analysis

Analyse each term against BVCA market standard (February 2025):

#### Valuation and Economics

| Term                       | BVCA Market Standard                            | Deviation Classification                            |
| -------------------------- | ----------------------------------------------- | --------------------------------------------------- |
| **Pre-money valuation**    | Negotiated; no standard                         | Note for awareness                                  |
| **Option pool**            | Created/topped up pre-money (dilutes founders)  | RED if post-money (dilutes all)                     |
| **Liquidation preference** | 1× non-participating (Series A market standard) | YELLOW: 1× participating; RED: > 1× or full-ratchet |
| **Anti-dilution**          | Broad-based weighted average                    | YELLOW: Narrow-based WA; RED: Full-ratchet          |
| **Dividend rights**        | Non-cumulative (or absent)                      | YELLOW: Cumulative; RED: Cumulative + priority      |

**⟁ CLARIFY** — If the liquidation preference is participating or > 1×:

- "This term carries a [X]× participating liquidation preference. At what exit valuation
  would investors' preference rights convert to ordinary participation? I can model this
  waterfall if you provide the capitalisation table."

#### Investor Protections

| Term                                | BVCA Market Standard                                                              | Deviation Classification                                      |
| ----------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Drag-along threshold**            | 75% of all shareholders (or investor class)                                       | RED: < 50% (abusive drag)                                     |
| **Tag-along**                       | Pro rata tag-along for all shares                                                 | YELLOW: Investor-only tag                                     |
| **Reserved matters**                | Defined list requiring investor consent                                           | Check each item — too broad = operational constraint          |
| **Board composition**               | One investor director per major investor; independent director common at Series A | GREEN: Standard; YELLOW: > 2 investor directors vs. 1 founder |
| **Information rights**              | Monthly management accounts; annual audited accounts; 12-month budget             | YELLOW: Missing budget/forecast; RED: No accounts at all      |
| **Investor consent for new rounds** | Pro rata participation rights; anti-dilution                                      | RED: No pre-emption rights in new rounds                      |
| **Share transfer restrictions**     | ROFO/ROFR standard; lock-up for founders                                          | YELLOW: Founder lock-up > 36 months                           |
| **Vesting**                         | 4-year founder vesting with 1-year cliff is market standard                       | YELLOW: No cliff; RED: No vesting or > 5 years                |

#### Anti-Dilution Analysis

Three anti-dilution mechanisms exist in UK market practice:

1. **Full-ratchet** (most investor-friendly): Option/warrant conversion price resets to
   lowest price in any down round. Highly dilutive to founders. **RED** at any stage.
2. **Narrow-based weighted average**: Adjusts conversion price based on price and number
   of new shares only (ignores option pool). More investor-friendly than broad-based.
   **YELLOW** — negotiate to broad-based.
3. **Broad-based weighted average** (market standard): Adjusts for all shares on a
   fully diluted basis (including options and warrants). Least dilutive to founders.
   **GREEN** for investors; market standard at Series A.

**Formula (broad-based WA)**:

```
New Conversion Price = CP × (A + B) / (A + C)
Where:
  CP = Current conversion price
  A  = Number of shares outstanding (fully diluted) before new issuance
  B  = Aggregate consideration received / original conversion price
  C  = Number of new shares issued
```

### Shareholder Agreement (SHA) Reserved Matters

Flag if any of the following are classified more expansively than BVCA standard:

| Reserved Matter                     | BVCA Standard                                    | RED Flag                                   |
| ----------------------------------- | ------------------------------------------------ | ------------------------------------------ |
| Amend Articles                      | Investor consent required                        | —                                          |
| Issue new shares                    | Investor consent required                        | Missing                                    |
| Borrow beyond threshold             | Investor consent required                        | Threshold too low (operational constraint) |
| Sell major assets                   | Investor consent required                        | —                                          |
| Capital expenditure                 | Threshold typically £[X]; Investor consent above | Threshold too low                          |
| Acquire another business            | Investor consent required                        | —                                          |
| Related-party transactions          | Investor consent required                        | Missing                                    |
| Change of business                  | Investor consent required                        | —                                          |
| Winding up / insolvency proceedings | Investor consent required                        | Missing                                    |

**⟁ CLARIFY** — If reserved matters list is unusually long or includes routine operational
decisions: "Some reserved matters appear to require investor consent for day-to-day
operations. Should I flag these as operational constraints (YELLOW) or accept them as
negotiated terms?"

---

## Module 4: SEIS and EIS — Expanded April 2026

### SEIS Limits (Post-April 2026) [VERIFY ALL LIMITS]

| Limit                                | Pre-April 2026         | Post-April 2026 [VERIFY]       |
| ------------------------------------ | ---------------------- | ------------------------------ |
| Maximum raise per company (lifetime) | £250,000               | [VERIFY — expansion announced] |
| Investor income tax relief           | 50%                    | 50%                            |
| CGT exemption (shares held 3+ years) | Full                   | Full                           |
| CGT reinvestment relief              | 50% of gain reinvested | 50%                            |
| Loss relief                          | Income or CGT          | Income or CGT                  |
| Maximum company age at first SEIS    | 3 years (trading)      | [VERIFY]                       |
| Maximum gross assets                 | £350,000               | [VERIFY expansion]             |
| Maximum full-time employees          | 25                     | [VERIFY]                       |

### EIS Limits (Post-April 2026) [VERIFY ALL LIMITS]

| Limit                                   | Current (pre-April 2026)   | Post-April 2026 [VERIFY]   |
| --------------------------------------- | -------------------------- | -------------------------- |
| Annual raise per company                | £5,000,000                 | [VERIFY expansion]         |
| Lifetime raise per company              | £12,000,000                | [VERIFY expansion]         |
| KIC annual raise                        | £10,000,000                | [VERIFY]                   |
| KIC lifetime raise                      | £20,000,000                | [VERIFY]                   |
| Investor annual investment (30% relief) | £1,000,000                 | £1,000,000 (or £2M if KIC) |
| Maximum company age                     | 7 years (10 years for KIC) | [VERIFY]                   |
| Maximum gross assets (pre-investment)   | £15,000,000                | [VERIFY expansion]         |
| Maximum full-time employees             | 250 (500 KIC)              | [VERIFY]                   |

### SEIS/EIS Eligibility Checklist

Run through each limb. A single failure = disqualification (usually).

**Company qualifying conditions:**

- [ ] UK-resident company (or permanent establishment in UK) — CA 2006 / ITA 2007 s.180
- [ ] Not quoted on recognised stock exchange at time of issue [VERIFY]
- [ ] Within gross asset limit [VERIFY current limit]
- [ ] Within employee limit [VERIFY current limit]
- [ ] Carrying on a qualifying trade (or will do so within 2 years) [VERIFY ITA 2007 ss 189–200]
- [ ] No excluded activities [VERIFY ITA 2007 s.192 list including: dealing in land, financial
      instruments, leasing, legal/accountancy services, property development, energy generation
      with subsidy (with exceptions)]
- [ ] Within age limit at time of first SEIS/EIS investment [VERIFY]
- [ ] Not in difficulty (State Aid rules) [VERIFY for EIS — SEIS does not require this]

**Shares qualifying conditions:**

- [ ] New ordinary shares [VERIFY ITA 2007 s.173]
- [ ] Fully paid at time of issue
- [ ] No preferential rights (assets on winding up, dividends, redemption)
- [ ] No arrangements for shares to be redeemed
- [ ] Held by investor for minimum 3-year period (to retain relief)

**Investor qualifying conditions (EIS):**

- [ ] Individual investor (not a company or trust)
- [ ] Not "connected" with the company [VERIFY ITA 2007 s.163 — employee, director (unless
      newly appointed), 30%+ interest]
- [ ] Not previously a director of the company unless newly appointed business angel [VERIFY]

**Post-investment compliance (EIS):**

- [ ] Company must carry on qualifying activity for 3 years post-issue
- [ ] Compliance Statement (EIS3) filed with HMRC after 4 months of trading on raised funds
- [ ] Investor receives EIS3 to claim relief on tax return
- [ ] HMRC Advance Assurance (AA) obtained before issue (strongly recommended; not mandatory)

### HMRC Advance Assurance — Process

1. Apply via HMRC SEIS/EIS unit (HMRC Venture Capital Schemes team, Cardiff) using
   online service at HMRC.gov.uk [VERIFY current process]
2. Provide: business plan, financial projections, draft investment documents, description
   of qualifying trade
3. Typical timeline: 4–8 weeks (may be longer)
4. AA is not binding but gives high confidence; HMRC may revoke if facts change
5. **Recommended**: Obtain AA before shares are issued; investors rely on it for relief

---

## Module 5: EMI Options — Post-April 2026

### What EMI Is

The Enterprise Management Incentives (EMI) scheme (ITEPA 2003 Part 7 Chapter 9
[VERIFY]) is the UK's tax-advantaged share option scheme for growth companies. It
provides:

- **No income tax or NICs** on grant (if FMV used as exercise price)
- **Business Asset Disposal Relief** (BADR, formerly Entrepreneurs' Relief) on sale:
  10% CGT rate (subject to qualifying conditions [VERIFY current BADR rules post-April
  2026 Autumn Budget])
- 90-day window to exercise after leaving employment (without losing tax advantages)

### Post-April 2026 Changes [VERIFY]

| Item                              | Pre-April 2026                        | Post-April 2026 [VERIFY]                         |
| --------------------------------- | ------------------------------------- | ------------------------------------------------ |
| **Individual option limit (FMV)** | £250,000 per employee                 | Doubled [VERIFY new limit — announced in Budget] |
| **Company-wide aggregate limit**  | £3,000,000 FMV of unexercised options | [VERIFY if also increased]                       |

### EMI Qualifying Conditions

**Company qualifying conditions:**

- [ ] UK-resident (or permanent establishment)
- [ ] Gross assets ≤ £30,000,000 [VERIFY]
- [ ] Fewer than 250 full-time equivalent employees [VERIFY]
- [ ] Not a subsidiary of a quoted parent
- [ ] Independent company (not controlled by another) [VERIFY]
- [ ] No excluded trades (broadly similar to EIS, plus financial activities) [VERIFY
      ITEPA 2003 s.527 Schedule 5 para 16]

**Option qualifying conditions:**

- [ ] Granted over ordinary shares in the EMI company (or parent of a group)
- [ ] Exercise price ≥ FMV at date of grant (for full income tax / NIC advantage)
- [ ] Maximum value: £[VERIFY post-April 2026 limit] per employee
- [ ] 10-year maximum exercise period from grant date [VERIFY]
- [ ] Written option agreement with prescribed contents (ITEPA 2003 Schedule 5 para 37
      [VERIFY])
- [ ] Notification to HMRC within 92 days of grant [VERIFY current deadline — may have
      changed; late notification results in loss of EMI status]

**Valuation process:**

1. Agree Unrestricted Market Value (UMV) and Actual Market Value (AMV) with HMRC
   Shares and Assets Valuation (SAV)
2. Apply via HMRC SAV's online service [VERIFY]
3. Typical timeline: 4–6 weeks (may be longer at busy periods)
4. Agreed valuation is valid for 90 days [VERIFY current validity period]
5. Valuation applies only to the grant date; new valuation needed for subsequent grants

### Disqualifying Events

Certain events cause an option to lose EMI status. The employee then has 90 days to
exercise before:

- Income tax / NICs become chargeable on any gain above the exercise price
- BADR may no longer apply [VERIFY]

Key disqualifying events [VERIFY ITEPA 2003 Schedule 5 para 41]:

- Employee ceases to be a qualifying employee (leaves, reduces to < 25 hours/week or
  75% of working time, if applicable)
- Company ceases to meet qualifying conditions (e.g., gross assets exceed limit)
- Company comes under control of another company (pre-exit disqualification risk)
- Material amendment to the option terms

**⟁ CLARIFY** — For acquisition scenarios: "An acquisition (share sale) will cause a
disqualifying event unless options are exercised before completion or rolled over into
acquirer options. Have you planned for EMI exercise or rollover at exit?"

### EMI Option Agreement — Key Clauses

| Clause                | Market Standard                                                             | RED Flags                                                           |
| --------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Vesting schedule**  | 4-year, 1-year cliff (market standard)                                      | No cliff; > 5-year schedule; no good leaver protection              |
| **Good / Bad Leaver** | Good leavers: pro-rata vested + accelerate; Bad leavers: unvested forfeited | No distinction = unfair to employees                                |
| **Exit provisions**   | Automatic exercise or acceleration on change of control                     | Missing exit provision = options worthless at acquisition           |
| **Exercise price**    | FMV at date of grant (HMRC-agreed)                                          | Below FMV = income tax charge on exercise; above FMV = unattractive |
| **Exercise period**   | Up to 10 years from grant [VERIFY]                                          |                                                                     |
| **Payment mechanism** | Cashless exercise / sell-to-cover common at exit                            | Cash exercise only = barrier to exercise                            |

---

## Module 6: Companies Act 2006 — Pre-Emption Rights (ss 549–561)

### Overview

Sections 549–551 of CA 2006 require that new shares (equity securities) must first be
offered to existing shareholders in proportion to their holdings, before being offered
to new investors. This is the **statutory pre-emption right**.

### Key Provisions

| Section   | Content                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| **s.549** | Directors cannot allot shares without authority                                                            |
| **s.550** | Private companies with one class of shares: directors may allot without s.551 authority if articles permit |
| **s.551** | Shareholder authorisation for allotment (by ordinary resolution or articles)                               |
| **s.561** | Statutory pre-emption right: existing shareholders must be offered shares pro rata                         |
| **s.563** | Civil consequences of contravening s.561                                                                   |
| **s.569** | Private company: disapplication of pre-emption by special resolution                                       |
| **s.570** | Disapplication by special resolution generally (public companies mainly)                                   |

### Disapplication in a VC Round

For a VC round, pre-emption rights are typically disapplied by:

1. **Board resolution**: Allotting directors must have authority under s.549/550/551
2. **Special resolution (75% majority)**: Disapplying s.561 pre-emption rights under
   s.569 for the specific allotment
3. **Written resolutions** are common for private companies (CA 2006 s.288)

**⟁ CLARIFY** — Check whether:

- The company's articles already disapply pre-emption (common in investor-friendly
  articles prepared by VC-experienced solicitors)
- Existing investors have any pre-emption rights in the SHA that are **separate** from
  and additional to the statutory right (contractual pre-emption survives disapplication
  of statutory pre-emption)
- The SHA's anti-dilution rights (if any) interact with the allotment

### Pre-emption Group Statement of Principles (2022, updated November 2023)

The Pre-emption Group (representing listed companies and institutional investors)
publishes a Statement of Principles for UK-listed companies on non-pre-emptive issues
(placings, accelerated bookbuilds). **Relevant for VC-backed companies approaching IPO:**

- 2022 Principles expanded the soft limit for non-pre-emptive issuances to **20% of
  issued share capital** (from 10%), if at least 10% is used for specific acquisition/
  capital investment [VERIFY current edition — November 2023 update]
- Investor consultation is expected for issuances approaching these limits
- Not legally binding for private companies; relevant once listed

### Severity Classification — Pre-emption

| Issue                                                                                         | Classification |
| --------------------------------------------------------------------------------------------- | -------------- |
| No board authority to allot shares (s.549/551) — allotment void                               | RED            |
| No disapplication of s.561 pre-emption for VC round — offer required to existing shareholders | RED            |
| Contractual pre-emption in SHA not waived before third-party allotment                        | RED            |
| Pre-emption rights offered but non-participating investors not notified                       | YELLOW         |
| Articles contain pre-emption with short acceptance period                                     | YELLOW         |

---

## Module 7: New UK Prospectus Regime (January 2026)

### Background

The UK's post-Brexit prospectus regime reformed significantly under FSMA 2023, with FCA
new Prospectus Rules (replacing the EU-derived UK Prospectus Regulation) effective
**January 2026** [VERIFY effective date and FCA rules].

### Key Changes Relevant to VC-Backed Companies

| Feature                    | Old UK Prospectus Regulation                              | New FCA Prospectus Rules (Jan 2026) [VERIFY]                                                                                   |
| -------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Public offer threshold** | Prospectus required for offers to ≥ 150 persons or > €8M  | [VERIFY new threshold — FCA consulted on raising limit]                                                                        |
| **Admission threshold**    | Full prospectus for admission to regulated market         | [VERIFY changes for Growth Market / AIM]                                                                                       |
| **Exemptions**             | Art. 3(2) exemptions (HNW, sophisticated investors, etc.) | [VERIFY new exemption structure]                                                                                               |
| **Public offer platforms** | Not available                                             | New "public offer platform" regime under FSMA 2023 s.85A et seq. [VERIFY] — allows wider retail offers without full prospectus |
| **Format**                 | Prescriptive EU-derived format                            | More flexible UK format [VERIFY]                                                                                               |

### VC Relevance

- **Secondary sales** (selling VC-held shares on secondary platforms): New public offer
  platform regime may facilitate wider secondary markets without full prospectus [VERIFY]
- **IPO readiness**: Companies considering AIM or main market listing need to understand
  new admission document vs. prospectus requirements [VERIFY current AIM Rules for
  Companies]
- **SEIS/EIS**: SEIS/EIS investments are typically made under private placement exemptions
  and are unaffected by the new prospectus regime for initial investment rounds [VERIFY]

### Financial Promotions (FSMA 2000 s.21)

Separate from the prospectus regime, section 21 FSMA 2000 restricts **communications
that invite or induce investment**:

- **Rule**: Only FCA-authorised persons can issue/approve financial promotions [VERIFY]
- **VC exception — High Net Worth Investors**: CA 2000 Art. 48 [VERIFY current Article
  number] exempts communications to HNW individuals (typically: income ≥ £100K or net
  assets ≥ £250K, excluding main residence) [VERIFY current thresholds — FCA reformed
  these in January 2024: income ≥ £170K or net assets ≥ £430K (Statement 2 HNW test)
  or alternative consumer test] [VERIFY]
- **Sophisticated Investor exemption**: Self-certified or certified sophisticated investors
  (previously involved in unlisted company investment, industry professional, etc.)
  [VERIFY FCA January 2024 reforms to exemptions]

**⟁ CLARIFY** — For any investor communication or pitch deck:

- "Is this being sent to investors who have signed a current-year HNW or sophisticated
  investor self-certification? If not, it may constitute an unlawful financial promotion
  under FSMA 2000 s.21 unless approved by an FCA-authorised firm."

---

## Module 8: Cap Table and Governance Analysis

### Cap Table Red Flags

| Issue                                                                          | Classification      |
| ------------------------------------------------------------------------------ | ------------------- |
| Option pool created post-money (dilutes investors as well as founders)         | YELLOW              |
| No ESOP (Employee Share Option Pool) reserved                                  | YELLOW for Series A |
| Founder shares fully vested from day one (no reverse vesting)                  | YELLOW              |
| Single founder with > 80% pre-investment (concentration risk)                  | YELLOW              |
| Previous SEIS/EIS raises with wrong share class (may create compliance issues) | RED                 |
| Shares not fully paid up                                                       | RED — CA 2006 s.578 |

### Liquidation Preference Waterfall Analysis

When a participating or stacked preference exists, model the exit waterfall:

```
Exit proceeds: £X

Step 1: Repay any debt (CLNs if not converted)
Step 2: Pay preference to senior preference holders (1× non-part is market standard)
Step 3: If participating: preference holders also participate pro-rata
Step 4: Remainder to ordinary holders (founders + option pool)

Key question: At what exit valuation does preference convert to ordinary participation?
(The "crossover point" — below which preference holders are better off taking preference
than converting to ordinary)
```

**⟁ CLARIFY** — "To model the waterfall accurately, I need the capitalisation table
(pre and post-investment) including: (1) all share classes and holdings, (2) option pool
size and vesting status, (3) any CLNs or other instruments outstanding. Can you provide
this?"

### ECCTA 2023 — Companies House Impacts on Share Issuances

The Economic Crime and Corporate Transparency Act 2023 introduced significant Companies
House reforms, phased in from 2024–2026 [VERIFY current implementation status]:

- **Identity verification** (ss 65–84 ECCTA 2023): All directors, PSCs (persons with
  significant control), and those filing at Companies House must verify their identity
  before or when accepting appointment. Required for new appointments and for existing
  officers from the date mandated by Companies House [VERIFY current go-live date]
- **Material false statements**: Enhanced criminal liability for inaccurate filings
  [VERIFY]
- **Registered office**: Must be an "appropriate address" (not just a PO box or nominee
  address) [VERIFY s.1-5 ECCTA 2023 effective date]
- **Registered email address**: Required from [VERIFY date]
- **Annual confirmation statement**: Enhanced accuracy requirements

**Impact on VC rounds**: All new directors appointed as investor directors must complete
identity verification before or when accepting appointment. Failure may cause the
appointment filing to be rejected [VERIFY current Companies House practice].

---

## Step 5: Quality Verification

Before delivering the output, run the following checks silently.

### Citation Quality Gates

| Gate           | Rule                                                                                            | Fail Action                                               |
| -------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Source**     | Every legal claim cites specific statute, HMRC guidance, or FCA rule                            | Add citation or mark "[VERIFY — cite authority]"          |
| **Format**     | All UK citations follow standard format: "CA 2006 s.561", "ITA 2007 s.173(2)(b)"                | Fix format                                                |
| **Currency**   | Each provision checked against legislation.gov.uk for amendments                                | Flag "[CHECK CURRENCY — provision may have been amended]" |
| **Domain**     | Analysis stays within England & Wales law; no bleed from US/EU concepts unless explicitly noted | Remove or flag jurisdictional bleed                       |
| **Confidence** | Uncertainty explicitly stated, especially for post-April 2026 limits not yet verified           | Add "[VERIFY current limits]" qualifier                   |

### Self-Interrogation for RED Items

For any item classified RED, run a 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the RED classification follow from the cited
statute or principle? Would HMRC or a court reach this conclusion on these facts?

**Pass 2 — Completeness**: Have all relevant statutory provisions been checked? Are there
transitional provisions or exceptions that might change the analysis?

**Pass 3 — Challenge**: What is the strongest argument that the issue is not as serious
as classified? Under what circumstances might a VC-experienced solicitor accept this risk?

If any pass reveals a weakness, revise the classification before delivery.

### Confidence Scoring

| Level        | Range     | Meaning                           | Action                                       |
| ------------ | --------- | --------------------------------- | -------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law / clear statute       | State with confidence                        |
| **High**     | 0.80–0.94 | Strong authority, minor questions | Brief caveat                                 |
| **Probable** | 0.60–0.79 | Good arguments, could differ      | State reasoning and contra-indicators        |
| **Possible** | 0.40–0.59 | Genuinely uncertain               | Flag for professional review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative           | "[UNCERTAIN — tax/legal adviser to advise]"  |

---

## Step 6: Deliver Output

### Output Format Template

```markdown
## UK Venture Financing Analysis

**Company**: [name]
**Round**: [type, amount]
**Instrument(s)**: [ASA / CLN / Priced equity / Mixed]
**Your side**: [Founder / Lead investor / Co-investor / Counsel]
**Date of review**: [YYYY-MM-DD]
**Review basis**: [BVCA Feb 2025 / SEIS/EIS rules post-April 2026 / General market standard]

---

## Executive Summary

[2-3 sentences: overall assessment, top issues, and strategic recommendation]

---

## Critical Issues (RED)

| #   | Issue   | Module   | Impact   | Action            |
| --- | ------- | -------- | -------- | ----------------- |
| 1   | [Issue] | [Module] | [Impact] | [Action required] |

---

## Items for Review (YELLOW)

| #   | Issue   | Module   | Current Position | Market Standard | Recommended Action |
| --- | ------- | -------- | ---------------- | --------------- | ------------------ |
| 1   | [Issue] | [Module] | [current]        | [standard]      | [action]           |

---

## Accepted / Market Standard (GREEN)

| #   | Item   | Module   | Note          |
| --- | ------ | -------- | ------------- |
| 1   | [item] | [module] | [note if any] |

---

## SEIS/EIS/EMI Summary

**Eligibility assessment**: [ELIGIBLE / AT RISK / INELIGIBLE — with reasoning]
**Key risks**: [List any disqualifying factors or risks]
**HMRC Advance Assurance**: [Obtained / Not obtained / Recommended]
**Action items**: [List steps needed to preserve or achieve eligibility]

---

## Cap Table Analysis

**Pre-money**: £[X]
**Post-money**: £[X]
**Key concerns**: [Any cap table RED flags]
**Waterfall summary**: [If liquidation preferences are complex]

---

## Pre-emption Rights Summary

**Status**: [Pre-emption disapplied / Waived / Outstanding issue]
**Action items**: [Any board or shareholder resolutions needed]

---

## Negotiation Priorities

### Must-Have (Tier 1)

- [Item]: [Why non-negotiable]

### Should-Have (Tier 2)

- [Item]: [Why important]

### Nice-to-Have (Tier 3)

- [Item]: [Lower priority; potential concession]

---

## Next Steps

1. [Action]: [Owner] — [Target]
2. [Action]: [Owner] — [Target]
3. [Action]: [Owner] — [Target]

---

## Glass Box Audit Trail

[See YAML below]
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in UK venture financing analysis:

1. **Treating a SAFE as SEIS/EIS compatible** — US Y Combinator SAFE notes are not
   designed for UK tax law and typically fail SEIS/EIS qualifying conditions (wrong share
   type, potential repayment rights). Always recommend an ASA for SEIS/EIS investment.
   [VERIFY current HMRC guidance on SAFEs]

2. **Using an ASA with a longstop > 6 months for SEIS/EIS** — HMRC requires conversion
   within 6 months for SEIS/EIS qualifying purposes. A longstop of 12 months (common in
   non-SEIS/EIS ASAs) is a disqualifier. Check the longstop date before anything else.

3. **Issuing preference shares for SEIS/EIS** — SEIS/EIS require ordinary shares with
   no preferential rights. Even "A Ordinary" shares with enhanced voting but no economic
   preference may be scrutinised. Get HMRC advance assurance if unusual share class.

4. **Forgetting to notify HMRC of EMI grants within 92 days** — Late notification
   causes the option to lose EMI status. The employee loses the income tax/NIC advantage
   and BADR. Calendar this immediately on grant. [VERIFY current deadline]

5. **Option pool created post-money** — An option pool created post-money dilutes both
   founders and investors. The market convention (BVCA and market standard) is to create
   or top up the option pool pre-money, so it only dilutes founders (and is reflected in
   pre-money valuation). If a term sheet says "option pool post-money," this is a YELLOW
   deserving negotiation.

6. **Not disapplying pre-emption for the VC round** — Failing to disapply CA 2006 s.561
   before allotting shares to new investors technically requires offering shares to all
   existing shareholders first. An allotment without valid disapplication is subject to
   civil consequences under s.563. Ensure special resolution and board resolution are in
   order before completion.

7. **Conflating statutory pre-emption with contractual pre-emption** — A special
   resolution disapplying s.561 does not disapply contractual pre-emption rights in a
   SHA. Both must be addressed: the s.569 disapplication for statutory rights AND a
   waiver / exercise of rights by existing SHA-party investors.

8. **Ignoring the 30% "connected" investor rule for EIS** — An investor who holds ≥ 30%
   of the company's ordinary share capital (or is an employee/paid director) is
   "connected" and cannot claim EIS relief [VERIFY ITA 2007 s.163]. New investors
   approaching this threshold on a follow-on investment must check connectivity.

9. **Full-ratchet anti-dilution** — A full-ratchet anti-dilution provision resets the
   investor's conversion price to the lowest price in any down round, regardless of
   the size of the down round. This can be catastrophically dilutive for founders and
   subsequent investors. It is not market standard in UK VC (BVCA uses broad-based
   weighted average). Always flag as RED.

10. **Missing good/bad leaver provisions in EMI agreements** — Without good/bad leaver
    distinction, all leavers (voluntary resignation, dismissal for cause, death, ill
    health) are treated equally. This creates perverse incentives. BVCA and market
    standard requires: good leavers keep pro-rata vested options; bad leavers forfeit
    unvested options (and sometimes vested too).

11. **Issuing CLNs without checking EIS compatibility** — Convertible Loan Notes with
    interest and/or repayment rights may not qualify for EIS under ITA 2007. Many CLN
    structures fail the qualifying share requirement. Advise investors to obtain HMRC
    advance assurance before committing funds under a CLN if EIS relief is important.

12. **Stacked liquidation preferences from multiple rounds** — Successive rounds with
    1× non-participating preferences create a "stack" that, in a downside exit, absorbs
    the entire proceeds before founders or common shareholders receive anything. Model
    the full waterfall after each round to ensure founders understand the economics.

13. **Missing FSMA s.21 approval for pitch materials** — Pitch decks, investment teasers,
    and "opportunity documents" that invite investment may constitute financial promotions
    under FSMA 2000 s.21. If not issued/approved by an FCA-authorised person, this is a
    criminal offence and the contract is unenforceable [VERIFY s.30 FSMA]. Obtain FCA
    approval or rely on a verified investor exemption (HNW/sophisticated investor cert).

14. **Drag-along threshold below 75%** — A drag-along below 75% means a minority can
    force a sale that the majority and/or founders oppose. BVCA market standard is 75%
    of all shareholders (or 75% of a defined investor class). A drag threshold of 50%
    or any single investor veto is RED.

15. **No founder vesting (reverse vesting)** — Institutional investors almost universally
    require founder shares to be subject to reverse vesting (i.e., the company has an
    option to buy back unvested shares if a founder leaves early). No reverse vesting
    means a founder can leave on day 1 after funding and retain 100% of their shares.
    Flag as YELLOW if absent and RED if prior rounds have already required it.

16. **Ignoring EMI disqualifying events at acquisition** — An acquisition (share purchase
    or change of control) triggers a disqualifying event under ITEPA 2003. If EMI options
    are not exercised within 90 days, the income tax advantage is lost. This must be
    planned for in exit mechanics — either exercise before completion, or agree an option
    rollover with the acquirer.

17. **Failing to update the Articles before issuing new share classes** — Each new share
    class (A Ordinary, B Ordinary, Preference) must be authorised in the Articles of
    Association, which must be filed at Companies House. An allotment of shares under a
    class not in the Articles is invalid. Ensure Articles are updated by special resolution
    before completing a round that introduces a new share class.

18. **ECCTA 2023 identity verification gaps** — Investor directors appointed on closing
    must complete HMRC identity verification at Companies House before or when filing
    the appointment. If verification is delayed, Companies House may reject the filing.
    Plan for this in the round closing timeline.

---

## Writing Standards

Apply plain-language discipline to all output:

- **Active voice**: "The investor holds a 1× liquidation preference" not "A 1× liquidation
  preference is held by the investor"
- **Name the actor**: "The company must file Form SH01 within 1 month of allotment"
- **Specific citations**: "CA 2006 s.551" not "the relevant Companies Act provision"
- **Uncertainty flagged**: "[VERIFY current HMRC limit]" not stated as fact
- **Short sentences**: One point per sentence in executive summaries
- **Qualify post-April 2026 changes**: Always note "[VERIFY]" for limits that changed
  in April 2026 until confirmed against current HMRC/FCA guidance

**Quality gates before delivery**:

1. Is every SEIS/EIS limit flagged [VERIFY] if not confirmed against current HMRC guidance?
2. Is every statutory reference in the format "CA 2006 s.561" (not "section 561 of the Companies Act 2006")?
3. Can a non-lawyer founder understand the executive summary?
4. Is every RED issue backed by a specific statutory or regulatory citation?
5. Are the post-April 2026 changes to SEIS, EIS, and EMI limits explicitly marked [VERIFY]?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected** (preferred):

- In Step 3, search for current ITA 2007, ITEPA 2003, CA 2006, and FCA PRR provisions
- Verify current post-April 2026 SEIS/EIS/EMI limits against HMRC guidance
- Confirm current FCA financial promotions exemption thresholds (post-January 2024 reform)
- Save the most relevant results to `/tmp/legalcode-uk-vc-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all statutory and HMRC guidance references [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural and commercial analysis; do not assert specific statutory limits
  for SEIS/EIS/EMI without verification

---

## Localization Notes

**Scotland**: Scottish company law for incorporated companies is the same (CA 2006
applies UK-wide), but Scottish contract law differs. A Scottish law SHA requires a
qualified Scots law solicitor to review.

**Northern Ireland**: CA 2006 applies. Separate from England & Wales court system.

**US/Cayman flip-up**: Many UK startups "flip" to Delaware C-Corp or Cayman holding
structure before a US-led Series A. This skill does not cover the flip-up process.
Separate tax analysis (UK exit charge on share exchange, US 83(b) election, treatment
of existing SEIS/EIS shares) is required.

**EU investors**: Post-Brexit, UK EIS/SEIS relief is UK-only. EU-based investors may
have separate local tax incentives (e.g., French PEA, German INVEST-Zuschuss) that
apply in addition to UK EIS.

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-venture-financing-uk"
  task: "[Review / Draft / SEIS-EIS eligibility / Term sheet analysis / Other]"
  company: "[Company name]"
  round: "[Round type and amount]"
  instrument: "[ASA / CLN / Priced equity / Mixed]"
  user_side: "[Founder / Lead investor / Co-investor / Counsel]"
  jurisdiction: "England and Wales"
  modules_activated:
    - "[Module 1: ASA / Module 2: CLN / Module 3: BVCA / Module 4: SEIS-EIS / Module 5: EMI / Module 6: Pre-emption / Module 7: Prospectus / Module 8: Cap table]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "/tmp/legalcode-uk-vc-authority.md / Not created"
  statutes_consulted:
    - "CA 2006 ss 549-561 — VERIFIED / UNVERIFIED"
    - "ITA 2007 Part 5 (EIS) — VERIFIED / UNVERIFIED"
    - "ITA 2007 Part 5A (SEIS) — VERIFIED / UNVERIFIED"
    - "ITEPA 2003 Part 7 Ch 9 (EMI) — VERIFIED / UNVERIFIED"
    - "FSMA 2000 s.21 — VERIFIED / UNVERIFIED"
    - "ECCTA 2023 — VERIFIED / UNVERIFIED"
  hmrc_guidance_consulted:
    - "SEIS/EIS Guidance (HMRC) — VERIFIED / UNVERIFIED"
    - "EMI Technical Guidance (HMRC) — VERIFIED / UNVERIFIED"
  post_april_2026_limits_verified: "Yes / No — [if No, all limits marked VERIFY in output]"
  citations_verified: "[count] VERIFIED / [count] UNVERIFIED"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Post-April 2026 SEIS/EIS/EMI limits are subject to [VERIFY] throughout — confirm against current HMRC guidance"
    - "New UK prospectus regime (January 2026 FCA rules) requires verification against current FCA Handbook"
    - "Financial promotions exemption thresholds subject to FCA reform — verify against current COBS rules"
    - "[Any other scope limitations or assumptions made]"
  reviewer: "AI-assisted — requires qualified solicitor and tax adviser review before reliance"
  review_date: "[YYYY-MM-DD]"
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- BVCA Model Documents (February 2025 suite)
- HMRC SEIS, EIS, and EMI technical guidance (current as of March 2026)
- ITA 2007 Parts 5 and 5A, ITEPA 2003 Part 7 Chapter 9
- CA 2006 ss 549–561, Pre-emption Group Statement of Principles (2022, November 2023 update)
- FSMA 2000 as amended by FSMA 2023; FCA Prospectus Regulation Rules (January 2026)
- ECCTA 2023
- SeedLegals/SeedFAST ASA template mechanics and HMRC guidance on ASA/SEIS compatibility
- Market practice synthesis from UK VC law literature
- Legalcode research pipeline (web research, 2026-03-21)

**Review recommended**: Given the April 2026 SEIS/EIS/EMI limit expansions and the
January 2026 prospectus regime, all limits and regulatory thresholds marked [VERIFY]
should be confirmed against current HMRC.gov.uk, legislation.gov.uk, and the FCA
Handbook before reliance.
