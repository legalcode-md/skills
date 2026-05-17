---
name: legalcode-safe-review
description: >
  Review YC post-money SAFEs (Simple Agreements for Future Equity) clause-by-clause for
  founders, investors, and counsel — covering valuation cap mechanics and Company
  Capitalization denominator, discount rate analysis, MFN clause triggering and scope,
  pro rata rights (in-form and side letter), conversion mechanics across all trigger events
  (equity financing, liquidity event, dissolution), amendment and majority-in-interest
  provisions, and non-standard modifications. Benchmarks every material term against the
  current YC post-money templates (v1.1/v1.2, February 2023 update) and market data
  (Carta Q3 2024). Classifies deviations as STANDARD / FLAG / RED FLAG with dual-perspective
  framing (founder view and investor view). Models ownership percentage at conversion.
  Identifies template drift (modifications beyond blank-filling). Reviews accompanying side
  letters (pro rata, information rights, board observer, MFN extension). Flags securities law
  compliance gaps (Reg D Form D, accredited investor verification, Blue Sky notices) and tax
  risks (IRC § 1202 QSBS, Section 409A timing). Produces confidence-scored, jurisdiction-aware
  analysis with prioritized redlines and a Glass Box audit trail. Use when reviewing, negotiating,
  or advising on a YC-form SAFE, any SAFE variant, uncapped MFN SAFE, discount-only SAFE, or
  post-money SAFE side letter at pre-seed, seed, or bridge stage. Also triggers on: post-money
  cap calculation, Company Capitalization definition, valuation cap vs. discount comparison,
  shadow preferred stock at conversion, SAFE conversion mechanics, Liquidity Capitalization,
  MFN notification window, pro rata side letter scope, majority-in-interest amendment, QSBS
  clock for SAFEs, and YC template modification detection.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode SAFE Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of Simple Agreements
> for Future Equity (SAFEs). It does not constitute legal, tax, securities, or financial advice.
> All outputs must be reviewed by a qualified attorney and securities counsel licensed in the
> relevant jurisdiction before any reliance or action. References to YC template versions, IRC
> §§ 1202 and 409A, Regulation D, and market benchmarks reflect the state of law and practice as
> of early 2026 and carry currency risk — verify the latest YC documents page, current Regulation
> D rules, and tax code provisions before relying on them. AI-generated ownership percentage
> calculations and cap table arithmetic require independent verification. SAFE terms are highly
> fact-specific; do not generalize beyond the specific document reviewed. Nothing here constitutes
> investment advice or an offer or solicitation to buy or sell securities. SAFEs are securities
> under federal law; securities counsel review is mandatory before issuance or transfer.

---

## Purpose and Scope

This skill reviews YC post-money SAFE agreements clause-by-clause. It identifies the template
variant in use, detects modifications from the standard form, benchmarks every material economic
term against current market standards, and generates prioritized findings with dual-perspective
framing (founder view and investor view) and actionable redlines.

**Covers:**
- Template identification and modification detection (standard vs. modified form; 2023 non-modification representation)
- Variant classification: cap-only (v1.1), discount-only, uncapped MFN (v1.2), or non-standard cap+discount
- Valuation cap mechanics: Safe Price formula, Company Capitalization denominator composition and negotiation
- Discount rate analysis: discount-derived price, interaction with cap, standard vs. non-standard rates
- MFN clause: trigger events, notification mechanics, election window, scope (economic terms only vs. broader)
- Pro rata rights: in-form (pre-2018 only) vs. side letter; scope, formula, and perpetuity analysis
- Conversion mechanics across all trigger events: equity financing, liquidity event (M&A, IPO), dissolution
- Liquidity Capitalization vs. Company Capitalization distinction
- Shadow preferred stock consequences at conversion
- Amendment and majority-in-interest provisions: Purchase Amount carve-out, solicitation requirements
- Non-standard red flags: interest rates, maturity dates, warrant coverage, board seats, consent/blocking rights
- Side letter review: pro rata scope, information rights, board observer, MFN extension
- Securities compliance flags: Regulation D exemption, Form D filing, accredited investor status, Blue Sky
- Tax flags: IRC § 1202 QSBS holding period clock, Section 409A timing, LLC-structure risks
- Cap table dilution modeling: ownership percentage at conversion, cumulative SAFE stacking effect
- Market benchmarking against YC template current versions and Carta Q3 2024 market data

**Does not:**
- Draft a SAFE from scratch — use a drafting-specific skill or the YC template directly
- Select among financing instruments (SAFE vs. convertible note vs. priced round) — route to `legalcode-venture-financing-suite`
- Review a convertible note — route to `legalcode-convertible-note-review`
- Review a term sheet for a priced equity round — route to `legalcode-term-sheet-analysis`
- Advise on Regulation D securities offering compliance in depth — route to `legalcode-private-placement-memo-review`
- Provide legal, tax, or investment advice, or replace qualified counsel

**Relationship to other skills:**

| Task | Use This Skill | Route To |
|------|---------------|---------|
| SAFE clause-by-clause review + redlines | ✅ This skill | — |
| Instrument selection (SAFE vs. note vs. priced round) | Summary flag only | `legalcode-venture-financing-suite` |
| Convertible note review | ✗ | `legalcode-convertible-note-review` |
| Series A term sheet review at conversion | Flag hand-off | `legalcode-term-sheet-analysis` |
| PPM / Reg D securities compliance | Cross-reference flag | `legalcode-private-placement-memo-review` |
| Equity incentive plan interaction at conversion | Flag only | `legalcode-equity-incentive-plan-review` |

---

## Jurisdiction and Governing Law

This skill covers the YC post-money SAFE governed by the **laws of the State of Delaware** and
federal US law (Regulation D securities exemptions; IRC §§ 1202, 409A, 305, 368). The YC SAFE
is a US-originated instrument; while international variants exist (Cayman, Singapore, Canada),
this skill focuses on the US-form SAFE. International equivalents (UK ASA, Australian KISS) share
structural similarities but differ materially and are flagged separately.

**Governing law check**: Identify the governing law clause in the SAFE. Standard YC form uses
"laws of the State of [Company's state of incorporation], without regard to the conflict of laws
provisions thereof." Flag any SAFE governed by non-US law as requiring jurisdiction-specific
counsel.

[JURISDICTION-SPECIFIC] For non-US companies using YC-form SAFEs or local equivalents:
- **Cayman Islands**: YC provides a Cayman variant. Analyze under Cayman company law; tax and
  securities implications differ materially from US-form. [VERIFY]
- **Singapore**: YC provides a Singapore variant. MAS regulations govern securities offerings;
  accredited investor thresholds differ. [VERIFY]
- **UK / Ireland**: Australian SAFE or UK ASA are analogous but not identical. EIS/SEIS
  incompatibility is a critical flag for UK SAFEs. [VERIFY]
- **Canada**: YC stopped investing in Canadian-domiciled companies as of early 2026; Canadian
  SAFE variant is less relevant but still circulates. [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's context, the workflow pauses and asks when:

- The perspective (founder vs. investor vs. counsel) changes what is flagged
- Whether a SAFE is standard or modified cannot be determined without user input
- The appropriate market benchmark depends on stage, deal size, or investor type
- Side letters exist but have not been provided

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

### Step 1: Accept the SAFE

Accept the SAFE (and any accompanying side letters) in any of these formats:
- **File**: PDF, DOCX, or other document format
- **Pasted text**: Full SAFE text pasted into the conversation
- **URL**: Link to a document in a cloud storage or document system

If a pro rata side letter, information rights letter, or board observer letter is mentioned but
not provided, note this and proceed with the instruments provided. Flag the gap.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask:

1. **Perspective**: Whose interests should the analysis serve?
   - Options: **Founder / Company** (flag investor-favorable deviations), **Investor** (flag
     company-favorable deviations), **Neutral / Counsel** (dual perspective, flag both sides),
     **Investor due diligence** (focus on completeness of investor protections)
   - *Why this matters*: The same term (e.g., broad MFN scope) is favorable for the investor
     and adverse for the founder. The framing of findings flips entirely.

2. **Company stage and deal context**:
   - Options: Pre-seed (first institutional check), Seed (SAFE round with multiple investors),
     Bridge (between priced rounds), Other
   - Deal size: total SAFE round size and this investor's check
   - Cumulative SAFE position: are there prior SAFEs outstanding? How many? At what caps?
   - *Why this matters*: Stacked SAFEs at multiple caps create compounding dilution. Severity
     of findings depends on total SAFE loading.

3. **Investor type**:
   - Options: Individual angel, Seed fund, Accelerator (non-YC), Strategic / corporate, YC batch,
     Crowdfunding, Other
   - *Why this matters*: Market standard terms vary by investor type. Consent rights that are
     unusual from an angel are standard from a lead seed fund.

4. **Has a pro rata side letter been provided?**
   - Yes / No / Pending (will be provided)
   - *Why this matters*: The standard YC post-money SAFE does not include pro rata rights.
     Missing side letter = no pro rata right, which is the default. If the user expects pro rata
     to exist but has not provided the side letter, this must be flagged.

If partial context is provided, state assumptions explicitly and proceed. Do not silently assume.

### Step 3: Template Identification and Modification Detection

Before analyzing terms, determine whether this SAFE uses a standard YC form.

**Identify the template version:**
- Check the document header/footer for: "Postmoney Safe — Valuation Cap Only v1.1",
  "Postmoney Safe — Discount, No Valuation Cap", "Postmoney Safe — MFN Only v1.2", or
  similar YC version designations
- Check the date of the template — pre-2018 templates use "pre-money" mechanics (fundamentally
  different; flag immediately)
- Check for the February 2023 non-modification representation: does the SAFE include a
  representation by both parties that "neither has modified this form, except to fill in blanks
  and bracketed terms"? If present, any deviations from standard form language become a
  potential representation breach.

**Detect modifications beyond blank-filling:**
- Compare operative provisions against the known standard YC form
- Flag any substantive changes to: conversion mechanics, Company Capitalization definition,
  Equity Financing definition, Liquidity Event definition, amendment provisions, MFN mechanics
- Note: Adding interest provisions, maturity dates, warrant coverage, board rights, or consent
  requirements are modifications — not blank-filling. These trigger the RED FLAG classification.

**⟁ CLARIFY** — If the template version cannot be identified from the document:
- Ask the user: "I cannot identify a YC version designation on this document. Do you know
  whether this is a standard YC post-money SAFE, a modified YC SAFE, or a non-YC SAFE?
  This affects whether I benchmark against the YC standard or treat the whole document as custom."

### Step 4: Variant Classification

Classify the SAFE into one of the following variants. This determines which analysis tracks apply.

| Variant | Cap? | Discount? | MFN? | Market Share | Analysis Track |
|---------|------|-----------|------|-------------|----------------|
| **Cap-only (v1.1)** | Yes | No | No | ~62% | Cap mechanics + Conversion |
| **Discount-only** | No | Yes | No | ~9% | Discount mechanics + Conversion |
| **Uncapped MFN (v1.2)** | No | No | Yes | ~1% | MFN mechanics + Conversion |
| **Cap + Discount** | Yes | Yes | No | ~29% | Both mechanics + Conversion; flag as non-standard |
| **Other / Hybrid** | Varies | Varies | Varies | — | Full custom review; RED FLAG |

**Flag**: If Cap + Discount is present, note that YC removed this variant from official templates
in August 2021. While still common in the market (~29% per Carta), the combination provides more
investor protection than YC recommends. Founders should understand the dilution implications.

### Step 5: Economic Terms Analysis

Analyze the core economic terms for the identified variant. Apply the classification system
(STANDARD / FLAG / RED FLAG) as defined below.

#### 5a. Valuation Cap (Cap-Only or Cap+Discount variants)

**Extract and record:**
- Post-Money Valuation Cap (dollar amount)
- Purchase Amount (investor's check size)
- Calculated ownership percentage: Purchase Amount ÷ Post-Money Valuation Cap

**Benchmark against market data (Carta Q3 2024):**

| Stage | Typical Cap Range | Median Check | Expected Ownership |
|-------|------------------|-------------|-------------------|
| Pre-pre-seed | $3M–$8M | $100K–$250K | 2–8% |
| Pre-seed | $5M–$15M | $250K–$750K | 3–10% |
| Seed | $10M–$30M | $500K–$2M | 3–8% |
| Seed (AI / high-traction) | $15M–$50M+ | $1M–$5M | 3–10% |

**Review points:**
- Is the cap reasonable relative to current market benchmarks for the company's stage?
- Does the implied ownership percentage (Purchase Amount ÷ Cap) appear appropriate?
- Are there multiple SAFEs outstanding with different caps? Model cumulative dilution.
  (With post-money mechanics, dilution is additive: each SAFE's guaranteed ownership % comes
  entirely from founders, not from other SAFE holders.)

**Company Capitalization denominator (critical — often overlooked):**

Review the Company Capitalization definition. Standard YC post-money form includes, immediately
prior to the equity financing:
- All issued and outstanding capital stock (on an as-converted basis)
- All issued and outstanding options, warrants, and other convertible securities
- All SAFEs and convertible notes converting at the same time
- The unissued option pool (shares reserved but not yet granted)

Standard YC form **excludes**: any new option pool increase triggered by the equity financing.

Flag any departures from this standard definition. Including or excluding specific securities
changes the Safe Price materially and shifts dilution between parties.

#### 5b. Discount Rate (Discount-Only or Cap+Discount variants)

**Extract and record:**
- Discount rate percentage
- Safe Price formula: Series A Price Per Share × (1 − Discount Rate)

**Benchmark:**
- Market standard: 20% discount
- Aggressive (investor-favorable): >20% (25% is unusual; >25% is non-standard)
- Below standard (founder-favorable): <20% (15% acceptable; <15% requires justification)

**If Cap + Discount:** Model which mechanism produces the lower (more investor-favorable)
Safe Price at various Series A valuation levels. The break-even point: a 20% discount "beats"
the cap only if the Series A valuation is less than 1.25× the cap. Above that, the cap wins.

#### 5c. MFN Provision (Uncapped MFN variant)

**Extract and record:**
- MFN notification trigger definition: what instruments trigger the obligation?
- Notification mechanism: who notifies, in what form, to what address?
- Election window: how many days does the investor have to elect to adopt better terms?
  (YC standard: 10 days from notice)
- Scope of "more favorable terms": limited to cap/discount or broader?

**Review points:**
- Does MFN cover only convertible instruments (SAFEs, convertible notes), or all financing?
- Is YC's own batch investment SAFE carved out? (Founders often negotiate this exclusion.)
- Does MFN automatically extend to side letter terms (pro rata, information rights)?
  If yes, flag as investor-favorable and potentially problematic.
- Is the election window clearly defined with a start date (receipt of notice, not sending)?
- What happens if the company fails to give notice? Is there a remedy mechanism?

### Step 6: Conversion Mechanics Deep-Dive

Review the conversion mechanics for each trigger event. The SAFE should cover all three.

#### 6a. Equity Financing Conversion

**Extract:**
- "Equity Financing" definition: what constitutes a qualifying trigger?
- Minimum aggregate consideration threshold (if any — standard YC form has none)
- Conversion is automatic at Safe Price upon the closing of the equity financing

**Review points:**
- Is there a minimum financing size threshold? (Absence is standard but creates risk —
  any bona fide preferred stock sale could trigger conversion at an inopportune time.)
  Flag absence as STANDARD but note the risk if the company might do small strategic investments.
- Does "Equity Financing" cover only new preferred stock for cash? Could a strategic investment
  or convertible-to-preferred exchange inadvertently trigger conversion?
- Does the definition exclude a financing in which the SAFE itself converts (circular trigger)?

**Safe Price calculation check:**
Verify the Safe Price formula: Post-Money Valuation Cap ÷ Company Capitalization (as defined).
Confirm the denominator is measured immediately prior to conversion (before the new money comes in).

**Shadow preferred stock note:**
At conversion, SAFE holders typically receive a separate sub-series of the same preferred stock
as the new investors, with identical rights except: (i) liquidation preference equals the Purchase
Amount (not the higher Series A price), (ii) conversion price uses the Safe Price, and (iii)
dividends are calculated on Purchase Amount. Flag any SAFE that attempts to give SAFE holders
full Series A preferred liquidation preference — that would be an investor-favorable windfall.

Note for Delaware companies: shadow preferred creates a separate class that may have class
voting rights under DGCL §242(b)(2) in future charter amendments. Advise company counsel.

#### 6b. Liquidity Event

**Extract:**
- "Liquidity Event" definition: what triggers it?
- "Liquidity Capitalization" definition: how does it differ from Company Capitalization?
- Investor's choice: greater of (i) Purchase Amount or (ii) as-converted proceeds at Liquidity Price
- Liquidity Price formula: Post-Money Valuation Cap ÷ Liquidity Capitalization

**Review points:**
- Does "Liquidity Event" include both M&A / change of control and IPO / direct listing?
  If IPO is excluded, SAFE holders may be left in an ambiguous position at public offering.
- Does Liquidity Capitalization correctly exclude the unissued option pool and securities
  that will be cashed out at their Purchase Amount? Including unissued options in the
  liquidation denominator would dilute SAFE holders' as-converted proceeds unfairly.
- Is the 1x floor (Purchase Amount return option) clearly stated?
- In a change-of-control transaction where consideration is non-cash (stock, earnout), how
  is the "as-converted amount" calculated? Flag if ambiguous.

#### 6c. Dissolution Event

**Extract:**
- Dissolution Event definition: corporate dissolution, liquidation, winding up
- Payment: SAFE holder receives Purchase Amount from remaining assets
- Priority: after creditors, pari passu with preferred, senior to common

**Review points:**
- Is priority correctly stated? SAFE holders are unsecured — they receive nothing if there
  are insufficient assets after satisfying creditors.
- Does the SAFE characterize itself as equity (not debt) for dissolution priority? (Standard
  YC form does — this is important for the QSBS tax characterization discussed in Step 9.)
- Any "guaranteed return" or "minimum dissolution payment" language? If yes, flag as
  potentially debt-characterizing and creating unintended complications.

### Step 7: Amendment and Majority-in-Interest Provisions

**Extract:**
- Amendment mechanism: individual consent, majority-in-interest, or other
- Definition of "majority": what percentage and of which group?
- Which SAFE holders are counted in the majority: same cap and discount class only, or all SAFEs?
- Purchase Amount carve-out: can Purchase Amount be amended by majority? (Standard: no —
  requires individual consent)
- Solicitation requirement: must all holders be solicited even if not consented?

**Review points:**
- Does the amendment provision match the YC standard post-money form (majority of same
  cap/discount class, with solicitation but not individual consent required for non-Purchase
  Amount terms)?
- Has the investor negotiated away the majority-in-interest mechanism to require individual
  consent for all amendments? (Investor-favorable; can create holdout problem for company.)
- Is the "same class" definition clear? Ambiguity about which SAFEs are in the same class
  creates uncertainty about whether a particular amendment can proceed.
- Does the provision specify that the company must notify all SAFE holders (including
  non-consenting ones) promptly after any amendment?

### Step 8: Non-Standard Provisions and Red Flags

Identify any provisions not present in the standard YC post-money SAFE template. Each item
below is a RED FLAG unless specifically noted otherwise.

**Checklist — scan the entire SAFE for these provisions:**

| # | Non-Standard Provision | Classification | Rationale |
|---|----------------------|----------------|-----------|
| 1 | **Interest rate / accrual** | 🔴 RED FLAG | Transforms SAFE into debt; OID tax issues; potential re-characterization |
| 2 | **Maturity date** | 🔴 RED FLAG | Creates repayment obligation; removes indefinite-duration feature; debt-like |
| 3 | **Warrant coverage** | 🔴 RED FLAG | Adds separate security; cap table complexity; potential §409A issue |
| 4 | **Board seat / board observer** | 🔴 RED FLAG | Governance entanglement before equity; pre-conversion board rights are unusual |
| 5 | **Consent rights over M&A / fundraising** | 🔴 RED FLAG | Transforms SAFE into control instrument; severe founder constraint |
| 6 | **Anti-dilution provisions** | 🔴 RED FLAG | Duplicates / augments conversion protection already built into SAFE |
| 7 | **Voting rights before conversion** | 🔴 RED FLAG | SAFEs confer no voting rights pre-conversion; any voting right is highly unusual |
| 8 | **Information rights in main SAFE body** | ⚠️ FLAG | Standard form has none; acceptable in side letter for large investors only |
| 9 | **Full-ratchet or ratchet anti-dilution** | 🔴 RED FLAG | Reprices conversion at any subsequent lower-cap issuance; highly dilutive |
| 10 | **Guaranteed minimum ownership** | 🔴 RED FLAG | Super pro rata in disguise; inflates round structure |
| 11 | **Drag-along rights** | 🔴 RED FLAG | Pre-conversion drag-along on a SAFE holder is structurally inappropriate |
| 12 | **Liquidation preference above 1x** | 🔴 RED FLAG | Standard dissolution right is 1x; any premium is non-standard |
| 13 | **Non-compete / exclusivity obligations** | 🔴 RED FLAG | Inappropriate in a convertible instrument; should be in a separate agreement |
| 14 | **Representations and warranties on financials** | ⚠️ FLAG | Standard SAFE has no financial reps; any substantive reps warrant scrutiny |
| 15 | **Most Favored Nation extending to governance** | 🔴 RED FLAG | MFN should cover economic terms only (cap/discount); extending to governance cascades control rights to all MFN holders |

For each red flag found: state the specific provision, explain the risk from the founder's and
investor's perspectives, and provide a recommended resolution.

### Step 9: Side Letter Review

If a pro rata side letter, information rights letter, or board observer letter is provided,
review it against these standards.

#### 9a. Pro Rata Side Letter

**Extract:**
- Formula: ratio-based (standard) or hard percentage / dollar amount (non-standard)
- Scope: which rounds trigger the right? Next round only (standard) or perpetual (non-standard)?
- Threshold: any minimum investment size required to exercise pro rata?
- Termination: when does the right expire (at Equity Financing closing, or earlier)?
- Transfer: can the pro rata right be assigned to affiliates?

**Review points:**

| Term | Standard | Investor-Favorable (Flag) | Highly Non-Standard (Red Flag) |
|------|----------|--------------------------|-------------------------------|
| Formula | Ratio-based (ownership %) | Hard dollar amount | Guaranteed ownership regardless of round |
| Scope | Next qualifying round only | 2 rounds forward | Perpetual / all future rounds |
| Threshold | None (any conversion) | >$500K minimum | Triggered even without conversion |
| Termination | Upon Equity Financing closing | Extended to Series B | Never expires |
| Transfer | Affiliates only | Any person | Freely assignable |

Flag: Confirm that the aggregate pro rata rights across all outstanding investors do not crowd
out new lead investors. If total pro rata allocation demand could consume more than ~30% of the
proposed round, flag as a future fundraising risk.

#### 9b. Information Rights Letter

**Extract:**
- Financial statements required: type (unaudited, audited, reviewed), frequency, and deadline
- Budget / financial projections: annual budget or projections
- Access rights: any right to inspect books, records, or premises?
- Management meetings: any right to attend or receive notes from board/management meetings?
- Cap table access: any right to view the cap table on demand?

**Market standard (acceptable):**
- Quarterly unaudited financials (P&L, balance sheet), within 30-45 days of quarter end
- Annual audited or reviewed financials, within 90-120 days of fiscal year end
- Annual operating budget

**Flag as investor-favorable:**
- Monthly financials (burdensome for small teams)
- Board minutes access (non-standard before conversion)
- Detailed cap table on demand (can expose sensitive investor information to competitors)

**Flag as RED FLAG:**
- Inspection rights (right to visit premises and review books and records)
- Access to individual management or technical staff
- Any information provided to all other investors (creates MFN-like cascade on information rights)
- No confidentiality obligation on the investor for information received

#### 9c. Board Observer Letter

**Extract:**
- Scope: which investor (lead? all?) receives observer rights?
- Duration: until Series A closing? Indefinitely?
- Meetings covered: board meetings only, or committees too?
- Exclusion rights: can company exclude observer from portions of meetings?
- Termination triggers: ownership threshold below which observer rights terminate?

**Market standard (acceptable for lead investor only):**
- One observer right for the lead investor writing the largest check
- Terminates upon Series A board restructuring
- Company retains right to exclude observer from portions involving conflicts of interest
- Applies to full board meetings only (not committee meetings)

Flag as RED FLAG: Observer rights for all investors regardless of check size, perpetual rights
with no termination trigger, committee meeting access, or rights that constrain board deliberation.

### Step 10: Securities Compliance Flags

Flag the following securities law compliance items. These are compliance reminders, not detailed
legal advice; route to `legalcode-private-placement-memo-review` for full analysis.

**Regulation D (primary federal exemption):**

| Requirement | Standard Practice | Flag |
|-------------|------------------|------|
| Exemption used | Rule 506(b) (most common) or 506(c) | Neither stated in SAFE; confirm separate compliance memo |
| General solicitation | None permitted under 506(b) | Any public offering, AngelList, or demo day pitch may implicate 506(c) |
| Investor accreditation | Self-certification under 506(b); verified under 506(c) | No verification language in side letter or subscription docs |
| Form D filing | Within 15 days of first sale | Confirm filing has been or will be made |
| Blue Sky | State notice filings in investor's home state | Multi-state investor base requires multi-state compliance |

**Foreign investor flags:**
- Non-US investors may implicate Regulation S (offshore transaction) or US securities law
  even if resident abroad. Confirm offshore analysis has been completed.
- CFIUS: Investment from investors in covered countries (China, Russia, or other) into US
  technology companies may require CFIUS filing or clearance. [VERIFY current CFIUS rules]
- Certain countries' domestic securities laws may impose disclosure or registration requirements
  on their residents investing in US startups.

**SAFE as security:** Flag any attempt to characterize the SAFE as "not a security" in the
document. SAFEs are investment contracts under SEC v. W.J. Howey Co. and require a valid
securities exemption for issuance.

### Step 11: Tax Flags

Flag the following tax issues. These are reminders only; tax counsel review is mandatory.

**IRC § 1202 QSBS (Qualified Small Business Stock):**

The central issue: does the 5-year QSBS holding period for federal capital gains exclusion
(up to $10M or 10× basis; pending increase under OBBBA 2025) begin on the SAFE purchase date
or the conversion date?

- YC's template includes express language stating the SAFE "is, and at all times has been,
  intended to be characterized as stock" for §§ 304, 305, 306, 354, 368, 1036, and 1202 purposes.
- This characterization is NOT binding on the IRS. The IRS has not issued guidance on SAFE
  treatment under § 1202. [VERIFY current IRS guidance]
- Investors relying on the SAFE purchase date as the § 1202 clock start should obtain a
  tax opinion. Flag if no such language exists in the SAFE.

Check: Does the SAFE include YC's §1202 tax characterization language? If the SAFE does not
include this language, flag as a potential QSBS risk for investors.

**§ 409A Timing:**
- SAFEs issued to employees, consultants, or service providers (rather than investors) can
  create § 409A deferred compensation issues. Flag any SAFE issued to a service provider.
- The conversion of a SAFE at a discount or below-market cap into common stock could create
  § 409A issues depending on when and how the conversion is structured. [VERIFY]

**LLC Issuer Risk:**
- If the issuing entity is an LLC (rather than a C-corporation), SAFE treatment under
  partnership tax law is uncertain. Flag any LLC-structured issuer.
- Most VC-backed companies are Delaware C-corps; flag if otherwise.

**No OID / interest income:**
- Standard SAFEs bear no interest, creating no OID complications. If an interest rate has been
  added (already flagged as a RED FLAG in Step 8), separately flag the OID tax risk.

### Step 12: Cap Table Dilution Modeling

Model the investor's ownership percentage at conversion under reasonable scenarios.

**Basic ownership calculation (cap-only SAFE):**
- Ownership % = Purchase Amount ÷ Post-Money Valuation Cap
- Example: $500K at $10M cap = 5.00% ownership at conversion

**Cumulative stacking (if multiple SAFEs outstanding):**
Sum all SAFE ownership percentages to determine total SAFE dilution to founders:
- Each post-money SAFE's guaranteed ownership % comes entirely from founders
- Total founder dilution from SAFEs = Σ(each SAFE's Purchase Amount ÷ its Post-Money Cap)
- Remaining founder ownership (pre-Series A, post-SAFE conversion) = 100% − total SAFE % − option pool %

Model these scenarios:
1. Series A at 2× the cap (favorable exit for investor — cap beats discount)
2. Series A at 1× the cap (cap provides no benefit; conversion at Series A price)
3. Series A at 0.5× the cap (down round; no cap benefit; discount if present provides some protection)
4. Liquidity event at various multiples (model 1x floor vs. as-converted comparison)

Note any scenario where SAFE investors' combined ownership post-conversion would exceed 30% —
flag as a potential concern for lead Series A investors who typically require minimum free-float.

### Step 13: Quality Verification

Before delivering the analysis, run the quality checks in the **Quality Assurance Framework**.

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED FLAG item, run the 3-pass Self-Interrogation. Revise if any pass reveals
   a weakness in the classification.
3. Assign a Confidence Score to each material finding.
4. Verify completeness: confirm all sections (Steps 3–12) have been addressed or explicitly
   noted as not applicable.
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Finding Classification System

### STANDARD — Matches YC Template

The provision matches or closely follows the current YC post-money SAFE standard form for the
identified variant. No negotiation needed for this item.

**Examples:**
- Conversion mechanics matching the v1.1 or v1.2 standard formula exactly
- Amendment provision using standard majority-in-interest language
- Dissolution payment at 1x Purchase Amount, pari passu with preferred
- Company Capitalization definition matching the YC standard

**Action**: Note for awareness. No redline needed.

### FLAG — Deviates from Standard or Market Practice

The provision departs from the YC standard form or from prevailing market practice in a way
that is investor-favorable or founder-unfavorable (or vice versa). Requires attention and
likely negotiation, but does not fundamentally alter the SAFE structure.

**Examples:**
- Cap at materially above or below market range for the company's stage
- Discount rate above 20% (investor-favorable) or below 15% (founder-favorable)
- MFN scope extending to side letter terms beyond cap/discount
- Pro rata side letter with perpetual scope rather than next-round-only
- Information rights in the main SAFE body (non-standard placement)
- Equity Financing definition with no minimum threshold (creates inadvertent trigger risk)
- Company Capitalization definition departing from YC standard in a material way

**Action**: Generate specific redline language. Provide market-standard alternative. Provide
founder and investor perspective on the deviation. Note impact on dilution if quantifiable.

### RED FLAG — Non-Standard, Structurally Problematic

The provision fundamentally alters the SAFE structure, introduces debt-like features, grants
unusual rights, or creates material legal/tax/compliance risks. Requires negotiation or removal
before signing.

**Examples:**
- Interest rate or maturity date added to a SAFE
- Board seat or governance control provisions
- Consent rights over future M&A, financing, or strategic decisions
- Warrant coverage or supplemental equity rights attached to the SAFE
- MFN extending to governance or information rights
- Anti-dilution provisions beyond standard SAFE conversion mechanics
- Guaranteed minimum ownership / super pro rata provisions

**Action**: Explain the specific structural problem from both founder and investor perspectives.
Provide market-standard alternative. Quantify impact where possible. Recommend removal or
restructuring. Escalate to securities and/or tax counsel as needed.

---

## Actionable Output per Finding

For each finding, deliver:

```
**Finding**: [Brief descriptive title]
**Section**: [SAFE section reference, if applicable]
**Classification**: STANDARD / FLAG / RED FLAG
**Current language**: "[Exact quote or paraphrase of the provision]"
**Founder perspective**: [How this term affects the company / founders]
**Investor perspective**: [How this term affects the investor]
**Market benchmark**: [What the YC standard says or Carta market data shows]
**Proposed redline**: "[Specific alternative language, if FLAG or RED FLAG]"
**Rationale**: [1-2 sentences suitable for sharing with counterparty's counsel]
**Priority**: [Tier 1 — Restructure / Tier 2 — Strongly Negotiate / Tier 3 — Founders' Preference]
```

---

## Negotiation Priority Framework

### Tier 1 — Restructure (Deal-Altering)

Issues that fundamentally change the nature of the instrument or create material legal/tax
exposure. Do not sign without resolving these.

- Interest rate or maturity date provisions (transforms SAFE to debt-like instrument)
- Board seat, voting rights, or consent/blocking provisions pre-conversion
- Anti-dilution provisions beyond standard conversion mechanics
- MFN extending to governance rights
- Guaranteed minimum ownership or super pro rata provisions
- Non-standard dissolution priority (above 1x, above preferred pari passu)
- Warrant coverage attached to the SAFE

### Tier 2 — Strongly Negotiate (Material Economic or Structural Impact)

Issues that meaningfully affect economics or flexibility. Push hard; concede only with
adequate consideration.

- Valuation cap materially outside market range for stage
- Discount rate above 25%
- MFN scope extending to side letter terms beyond cap/discount
- Pro rata side letter with perpetual scope
- Information rights in main SAFE body (acceptable in side letter)
- Equity Financing definition with no minimum threshold (add a reasonable floor)
- Company Capitalization definition departing from YC standard
- Board observer rights for non-lead investors

### Tier 3 — Founders' Preference (Lower Stakes, Negotiable)

Issues that are worth raising but can be conceded strategically if Tier 1 and 2 issues are
resolved.

- Minor departures in boilerplate notices or governing law provisions
- Non-material definitional adjustments
- Information rights timing (45 days vs. 30 days for quarterly financials)
- Pro rata side letter assignment to affiliates vs. freely assignable
- Specific notification mechanics in MFN (form of notice, address for notice)

**Strategy**: Lead with Tier 1 items — these are non-negotiable. Trade Tier 3 concessions to
secure Tier 2 wins. Never sign with unresolved Tier 1 issues.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim (YC template mechanics, securities rule, tax provision) cites a specific source — YC template version, IRC section, Regulation D rule, or market benchmark (Carta/Fenwick) | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow a consistent format: YC form version, IRC §, 17 CFR Part 230, or "Carta Q3 2024 market data" | Fix format |
| **Currency** | Template version references verified as current (check ycombinator.com/documents). Regulatory citations checked for amendments or updates. | Flag "[CHECK CURRENCY — verify against current YC documents page]" |
| **Domain** | Analysis stays within the SAFE's governing law (Delaware / federal). No assumptions from civil law or non-US jurisdiction leaking into the analysis. | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated. Do not state the IRS position on QSBS / SAFE characterization as settled — it is not. | Add "[UNCERTAIN — tax counsel to advise]" for unresolved IRS positions |

### Self-Interrogation for RED FLAG Items

For any item classified as RED FLAG, apply this 3-pass review before delivering:

**Pass 1 — Structural Chain Integrity**:
- Does the red flag assessment follow logically from the standard SAFE structure?
- Would a Delaware court or the SEC actually treat this term as problematic, or is there a
  defensible rationale for including it?
- What is the counterparty's likely defense of this term?

**Pass 2 — Completeness**:
- Have all relevant implications been considered: tax, securities law, future financing,
  corporate governance?
- Are there other provisions in the SAFE that mitigate or amplify this flag?
- Could cumulative effect of multiple non-standard terms compound the risk?

**Pass 3 — Challenge**:
- What is the strongest argument that this provision is commercially reasonable?
- Under what investment thesis or deal structure might a sophisticated investor demand this term?
- Is the RED FLAG classification proportionate, or is this actually a FLAG with conditions?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Clear departure from YC standard form; no ambiguity | State with confidence |
| **High** | 0.80–0.94 | Strong basis in YC template and market data; minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good basis but reasonable practitioners could differ | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., QSBS tax characterization, novel provision) | Flag for counsel review with both sides of the argument |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative, or unverifiable without external information | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every SAFE review output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill: "legalcode-safe-review"
  document: "[SAFE title, company name, investor name, date]"
  template_version: "[YC v1.1 / v1.2 / Modified / Non-YC / Unknown]"
  variant: "[Cap-only / Discount-only / Uncapped MFN / Cap+Discount / Other]"
  perspective: "[Founder / Investor / Neutral / DD]"
  side_letters_reviewed: "[Pro Rata / Information Rights / Board Observer / None / Pending]"
  findings_count:
    standard: "[number]"
    flag: "[number]"
    red_flag: "[number]"
  tier_1_issues: "[number] — [brief titles]"
  modification_detected: "Yes / No / Unable to determine"
  non_modification_representation: "Present / Absent / Not applicable"
  qsbs_language_present: "Yes / No"
  securities_exemption_confirmed: "Yes / No / Not in document"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED FLAG items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, e.g., side letters not provided, template version unclear]"
  reviewer: "AI-assisted — requires qualified legal and securities counsel review"
```

---

## Anti-Patterns

What NOT to do when reviewing or drafting SAFEs:

1. **Treating the SAFE as a simple form** — The YC SAFE looks short (5-7 pages) but contains
   several technically complex provisions (Company Capitalization definition, shadow preferred
   mechanics, majority-in-interest amendment). Line-by-line reading with substantive analysis
   is required, not a quick skim.

2. **Ignoring the denominator** — Founders and investors often focus only on the cap (numerator)
   in the Safe Price formula and neglect the Company Capitalization denominator. Whether the
   denominator includes or excludes the new option pool, outstanding warrants, or all SAFEs
   materially affects the conversion price and resulting dilution.

3. **Failing to model cumulative SAFE stacking** — Analyzing a single SAFE in isolation without
   considering existing SAFEs already outstanding. With post-money mechanics, each SAFE's
   guaranteed ownership is fully additive to founder dilution. A series of seemingly reasonable
   individual SAFEs can produce extreme aggregate dilution.

4. **Confusing pre-money and post-money mechanics** — Applying pre-2018 pre-money conversion
   formulas to a post-money SAFE (or vice versa) produces incorrect dilution calculations.
   Always verify the template version before performing cap table arithmetic.

5. **Accepting a SAFE with a maturity date or interest rate** — These provisions transform a
   SAFE into a debt-like instrument. Do not treat them as minor modifications. They create OID
   tax complications, potential debt accounting treatment, and remove one of the SAFE's core
   advantages (no repayment obligation).

6. **Overlooking the amendment clause** — The majority-in-interest amendment mechanism is
   one of the most founder-important provisions in the post-money SAFE. An investor who
   modifies this to require individual consent for all amendments can hold up conversions.
   An investor who secures amendment rights without a solicitation requirement could have terms
   changed without individual notification.

7. **Ignoring the Equity Financing trigger definition** — No minimum threshold in the standard
   form means any bona fide preferred stock sale could trigger all outstanding SAFEs to convert,
   potentially at an inopportune valuation. Founders issuing small strategic preferred investments
   should be aware of this risk.

8. **Missing the shadow preferred blocking rights risk** — When SAFEs convert to shadow preferred
   at Series A, a separate class of preferred is created. This class may have DGCL §242(b)(2) class
   voting rights that become relevant in future charter amendments or M&A transactions. Advise
   company counsel proactively.

9. **Treating MFN as cap protection** — An uncapped MFN SAFE provides no cap protection if the
   company goes directly from MFN SAFE to a priced round without ever issuing a subsequent lower-
   capped SAFE or convertible note. Investors relying on MFN as a form of valuation protection
   need to understand this limitation.

10. **Accepting perpetual pro rata rights** — Pro rata rights should be limited to the next
    qualifying financing round. Perpetual pro rata rights (applying to Series B, C, and beyond)
    severely constrain future fundraising flexibility and are far beyond market standard.

11. **Granting consent rights over M&A or future financing** — Any provision requiring SAFE
    holder consent for future fundraising or M&A decisions transforms the SAFE from a passive
    economic instrument into an active governance instrument. This is non-standard and potentially
    value-destructive for the company.

12. **Relying on the §1202 QSBS clock starting at SAFE purchase** — The IRS has not issued
    definitive guidance on SAFE characterization for §1202 purposes. The YC template's tax
    characterization language is not binding on the IRS. Do not advise investors to rely on
    this position without a tax opinion.

13. **Failing to check for Form D filing compliance** — Every SAFE issuance under Regulation D
    requires a Form D filing within 15 days of the first sale. Many founders overlook this
    requirement. Failure to file is a state and federal securities law compliance issue.

14. **Missing the cap-plus-discount double benefit** — When reviewing a SAFE with both a cap
    and a discount, always model which mechanism produces the more investor-favorable price at
    various Series A valuations. The interaction is non-linear and has cap table implications
    founders often miss.

15. **Accepting broad MFN triggering governance side letters** — If a subsequent investor
    receives a side letter with favorable governance terms and the prior investor's MFN extends
    beyond economic terms, the prior investor can claim those governance terms. This creates a
    waterfall of governance rights the company did not intend to grant.

16. **Confusing Liquidity Capitalization and Company Capitalization** — These two defined terms
    differ in important ways (Liquidity Capitalization excludes unissued option pool; Company
    Capitalization does not at the equity financing calculation). Applying the wrong capitalization
    denominator in a liquidity event produces incorrect as-converted proceeds calculations.

---

## Writing Standards

### Precision Requirements

- State every finding with a specific section reference from the SAFE, a specific provision
  quote, and a specific market benchmark or YC template reference.
- Do not state general principles (e.g., "valuation caps are investor-friendly") without
  applying them to the specific SAFE being reviewed.
- When calculating ownership percentages, show the full arithmetic. Do not just state
  conclusions.
- Distinguish clearly between what the YC standard form says, what market practice is, and
  what this specific SAFE says. Three distinct things.

### Dual-Perspective Discipline

For every FLAG and RED FLAG finding, provide both perspectives:
- **Founder / Company perspective**: Why this term disadvantages the company or creates risk
- **Investor perspective**: Why the investor may have asked for this, and what protection it
  provides to them

Never deliver a one-sided analysis. Even red flags have a rational investor justification that
founders should understand to negotiate effectively.

### Plain-Language Requirement

After every technical explanation, add a one-sentence plain-language summary. Example:

*Technical*: "The Equity Financing definition does not include a minimum aggregate consideration
threshold, meaning any bona fide sale of preferred stock for cash consideration could trigger
automatic conversion of all outstanding SAFEs under Section 1(a)."

*Plain language*: "There's no minimum deal size required to trigger conversion — even a small
strategic preferred investment could force all your SAFEs to convert."

### Quality Gates Before Delivery

- [ ] Every finding cites a specific SAFE provision (section number and quote)
- [ ] Every market comparison cites the YC template version or market data source
- [ ] All ownership percentage calculations show full arithmetic
- [ ] Both founder and investor perspectives provided for FLAG and RED FLAG items
- [ ] All RED FLAG items have passed the 3-pass Self-Interrogation
- [ ] QSBS and securities compliance flags include explicit "[VERIFY / tax counsel to advise]" markers
- [ ] Cap table modeling shows workings, not just conclusions
- [ ] Glass Box Audit Trail is complete and accurate

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Search for:
- Current Regulation D rules and Form D requirements (17 CFR §§ 230.501–230.508)
- Delaware DGCL § 242 class voting rights — relevance to shadow preferred
- Current SEC no-action letters or guidance relevant to SAFE securities treatment
- IRC § 1202 current text and any IRS guidance on SAFE characterization
- Recent Delaware case law on SAFE conversion disputes or amendment mechanic enforcement

Save results to `/tmp/legalcode-safe-review-authority.md`. Cite all legalcode-mcp results as
VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp

Proceed using the template analysis and market benchmark data in this skill. Mark all statutory
and regulatory citations with [VERIFY]. Note in the Glass Box audit trail:
`legalcode_mcp: "Not connected"`. Advise the user that tax and securities counsel review is
especially important given unverified citations.

---

## Localization Notes

This skill covers US-form YC SAFEs governed by Delaware law. For international SAFE variants:

| Jurisdiction | Local Equivalent | Key Differences | Route |
|-------------|-----------------|-----------------|-------|
| **UK / Ireland** | Advanced Subscription Agreement (ASA) | EIS/SEIS incompatibility; Companies Act 2006 restrictions; no shadow preferred concept | Refer to UK ASA skill [if available] |
| **Australia** | SAFE / KISS | Different conversion mechanics; ASIC compliance requirements | [VERIFY] |
| **Canada** | YC Canada form (less relevant post-2026) | Similar to US form but different securities law | [VERIFY] |
| **Cayman Islands** | YC Cayman form | Used for YC-backed Cayman holdcos; substantially similar to US form | [VERIFY] |
| **Singapore** | YC Singapore form | MAS accredited investor rules; substantially similar mechanics | [VERIFY] |

For any non-US form SAFE, note that mechanics may appear similar to the YC post-money form
but underlying legal consequences differ materially. Do not apply US-form analysis to a
non-US-form SAFE without jurisdiction-specific counsel review.

---

## Output Format Template

Structure the final deliverable as follows:

```markdown
# SAFE Review — [Company Name] / [Investor Name]

> AI-assisted analysis. Requires review by qualified legal and securities counsel.
> Not legal, tax, or investment advice.

---

## Executive Summary

**Template**: [YC Post-Money SAFE — [Variant] / Modified / Non-YC]
**Date of SAFE**: [date]
**Purchase Amount**: $[amount]
**Post-Money Valuation Cap**: $[cap] (implied ownership: [%])
**Discount Rate**: [%] / N/A
**MFN**: Yes / No
**Side Letters Reviewed**: [list or None]

**Overall Assessment**: [1-2 sentence plain-language summary]

| Classification | Count |
|----------------|-------|
| ✅ STANDARD | [n] |
| ⚠️ FLAG | [n] |
| 🔴 RED FLAG | [n] |

**Top Issues**: [Bullet list of Tier 1 and key Tier 2 items]

---

## Section 1: Template and Variant Analysis

[Template identification, modification detection, and variant classification findings]

---

## Section 2: Economic Terms

[Valuation cap, discount, and/or MFN findings with market benchmarks and both perspectives]

---

## Section 3: Conversion Mechanics

[Equity Financing, Liquidity Event, and Dissolution findings]

---

## Section 4: Amendment Provisions

[Amendment mechanism findings]

---

## Section 5: Non-Standard Provisions

[Any RED FLAG non-standard terms with full analysis]

---

## Section 6: Side Letter Review

[Pro rata, information rights, and board observer findings — or "No side letters provided"]

---

## Section 7: Cap Table Modeling

[Ownership percentage at conversion; cumulative stacking if applicable; conversion scenarios]

---

## Section 8: Securities and Tax Flags

[Form D, accredited investor, Blue Sky, QSBS, and other compliance flags]

---

## Section 9: Prioritized Redlines

### Tier 1 — Restructure

[Detailed redline entries for each Tier 1 issue]

### Tier 2 — Strongly Negotiate

[Detailed redline entries for each Tier 2 issue]

### Tier 3 — Founders' Preference

[Detailed redline entries for each Tier 3 issue]

---

## Section 10: Negotiation Strategy

[Recommended approach: sequence, concessions, walk-away positions]

---

## Glass Box Audit Trail

```yaml
glass_box:
  ...
```

```

---

## Provenance

Created by Legalcode (2026-03-22). Original synthesis based on:
- Y Combinator post-money SAFE templates (v1.1/v1.2; February 2023 User Guide update)
- YC Safe User Guide and Primer for Post-Money Safe v1.1 (ycombinator.com/documents)
- Wilson Sonsini analysis of the 2018 post-money SAFE overhaul
- Carta Q3 2024 State of Pre-Seed market data
- Frost Brown Todd "When SAFEs Fail" practitioner analysis
- PKF O'Connor Davies IRC §1202 and SAFE QSBS analysis
- Silicon Hills Lawyer commentary on majority-in-interest amendment mechanics
- Law of VC Substack (Chris Harvey) on Company Capitalization deep dive
- 1984 Ventures Founders Handbook on SAFE side letters
- Orrick / Morse shadow preferred stock and DGCL §242 analysis
- Legalcode repository best practices from `legalcode-contract-review` and
  `legalcode-convertible-note-review` reference standards
- All statutory and regulatory references marked [VERIFY] where not independently confirmed
  via authoritative sources at time of drafting
