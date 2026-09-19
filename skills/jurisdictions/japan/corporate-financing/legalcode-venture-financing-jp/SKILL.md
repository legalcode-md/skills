---
name: legalcode-venture-financing-jp
description: Japanese venture financing adviser covering the full lifecycle of startup capital formation
  under Japanese law. Use when structuring or reviewing J-KISS (新株予約権 convertible warrant), KK preferred
  share rounds, shareholder agreement terms, FIEA Article 63 fund-formation exemption, METI/JVCA standard
  documentation, the Enterprise Value Charge (企業価値担保権, spring 2026 enforcement), shinkabu yoyakuken employee
  stock options, angel tax incentive qualification, and FEFTA foreign investment screening. Covers instrument
  selection (J-KISS vs. priced preferred round), KK corporate mechanics (Articles 108, 199, 236 of the
  Companies Act), fund structuring (ILP vs. TK/GK), securities exemption compliance, and cross-border
  considerations for foreign VC investing in Japanese startups. Japan-specific. Requires qualified Japanese
  legal counsel review.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Venture Financing — Japan (legalcode-venture-financing-jp)

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of Japanese
> venture financing law. It does not constitute legal advice. All outputs must be reviewed
> by a qualified lawyer (_bengoshi_ 弁護士) admitted in Japan and, where applicable, a
> registered tax accountant (_zeirishi_ 税理士) before reliance. Japanese corporate,
> securities, and tax law change frequently; verify current applicability against
> authoritative sources. Statutory and case law references carry hallucination risk —
> verify against the Japan Law Translation Database (japaneselawtranslation.go.jp) and
> official regulatory sources before relying on them.

---

## Purpose and Scope

This skill analyses and advises on the formation, structuring, and documentation of
venture capital investments in Japanese startups and VC funds.

**Covers:**

- **J-KISS** (J-KISS型新株予約権): seed-stage convertible warrant instrument — structure,
  conversion mechanics, v2.0 key terms, JVCA/Coral Capital template, angel tax eligibility
- **KK corporate mechanics**: preferred share class design (種類株式), shinkabu yoyakuken
  (新株予約権), Companies Act special resolutions, board composition, shareholder agreement
  (株主間契約) key terms — liquidation preference, anti-dilution, drag-along, tag-along,
  investor call options
- **FIEA compliance**: Article 63 SPBQII exemption (Form 20 notification), Type II
  Financial Instruments Business registration, fund structure selection (ILP vs. TK)
- **METI/JVCA documentation**: 2025 Model Limited Partnership Agreement (LPA), JETRO
  investment guidelines, standard term sheet practices
- **Enterprise Value Charge (EVC / 企業価値担保権)**: new floating security interest
  enacted June 2024, enforcement targeted spring 2026 — impact on deal structuring
- **Angel tax incentives (エンジェル税制)**: income deduction and capital gains rollover,
  METI prefecture confirmation, J-KISS warrant eligibility (from April 2024)
- **FEFTA foreign investment screening**: FX Act prior notification for foreign VC
  investors in sensitive sectors, 2025 Specified Foreign Investor classification

**Does not:**

- Cover listed company securities regulation (takeover bids, large shareholding reports)
- Provide legal advice or replace qualified Japanese counsel (_bengoshi_)
- Cover M&A/post-IPO equity capital markets in depth
- Provide tax advice — tax analysis is directional only; engage a _zeirishi_ for binding positions

## Jurisdiction and Governing Law

**Japan only.** This skill applies Japanese law exclusively:

| Statute                                                          | Japanese Name                        | Relevance                                                  |
| ---------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------- |
| Companies Act (Act No. 86 of 2005)                               | 会社法                               | KK corporate structure, share issuance, shinkabu yoyakuken |
| Financial Instruments and Exchange Act                           | 金融商品取引法 (FIEA)                | Securities regulation, fund formation, SPBQII exemption    |
| Investment LPS Act (Act No. 90 of 1998, as amended 2024)         | 投資事業有限責任組合契約に関する法律 | ILP fund structure                                         |
| Act on Special Measures Concerning Taxation                      | 租税特別措置法                       | Stock option tax qualification, angel tax                  |
| Foreign Exchange and Foreign Trade Act                           | 外国為替及び外国貿易法 (FEFTA)       | Foreign VC investment screening                            |
| Act on Promotion of Cash Flow-Based Lending (Act No. 52 of 2024) | キャッシュフロー融資促進法           | Enterprise Value Charge                                    |

All monetary amounts are in Japanese Yen (¥) unless stated otherwise.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the recommended instrument or structure
- A regulatory compliance determination turns on undisclosed facts
- Multiple valid approaches exist and the client's priorities matter
- Risk tolerance or investor base composition determines the compliance path

Use the **⟁ CLARIFY** convention below. If the user has already supplied the information,
skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Company profile**: Stage, sector, incorporation status, target raise amount, investor base
- **Document for review**: J-KISS terms, term sheet, draft shareholder agreement, LPA
- **Specific question**: "Can a US VC take a board seat without FEFTA prior notification?"
- **Structured task**: Instrument selection, FIEA compliance check, angel tax eligibility

If insufficient context is provided, proceed to Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the following before proceeding. Present as structured options. Skip
any question already answered by the input.

1. **Task type** — What is the primary need?
   - Options: J-KISS review/structuring | Priced preferred round / term sheet | Shareholder
     agreement review | FIEA fund compliance | Angel tax eligibility | FEFTA screening |
     EVC impact analysis | Employee stock options | Full structuring analysis
   - _Why this matters_: Determines which modules to activate.

2. **Stage and amount** — Where is the company in its lifecycle?
   - Options: Pre-seed (pre-revenue, seeking first institutional capital) | Seed (J-KISS or
     first preferred round, ¥50M–¥300M) | Series A/B (institutional round, ¥300M+) |
     Mature (later stage, complex cap table)
   - _Why this matters_: Determines instrument suitability and FIEA exemption analysis.

3. **Investor base** — Who is investing?
   - Options: Japanese institutional VC only | Japanese angels only | Foreign VC (US/EU/APAC)
     only | Mixed Japanese institutional + foreign | Mixed with Japanese angels
   - _Why this matters_: FEFTA prior notification and FIEA exemption conditions turn on
     investor composition.

4. **Company sector** — What does the company do?
   - Options: Software/SaaS (no regulated sector) | Life sciences/pharma | Fintech/financial
     services | Defence/aerospace | Telecoms/data processing | Other regulated sector | Multiple
   - _Why this matters_: FEFTA screening and FIEA registration requirements depend on sector.

5. **Perspective** — Who is the user?
   - Options: Founder/company | Japanese VC fund manager (GP) | Foreign VC fund manager |
     Legal counsel | Investor (LP or direct)
   - _Why this matters_: Determines which risks and obligations to prioritise.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to search for:

- Relevant Companies Act provisions (Articles 108, 199, 236, 247, 309, 324)
- FIEA Article 63 SPBQII exemption conditions and 2016 amendment requirements
- FSA guidance on Form 20 notification and ongoing compliance
- FEFTA designated business sectors (current official list)
- Act on Special Measures Concerning Taxation Article 29-2 (stock option qualification)
- Angel tax: METI angel guideline _r7_ (July 2025, investments from April 2025)
- EVC Act (Act No. 52 of 2024) enforcement status and Cabinet Orders issued

Save findings to `/tmp/legalcode-vf-jp-authority.md`:

```markdown
# Legal Authority — Japan Venture Financing

## Date: [date]

### Companies Act Provisions

- [Article, text/summary, source]

### FIEA Provisions

- [Article, text/summary, source]

### FSA Guidance

- [Title, date, relevance]

### FEFTA Provisions

- [Article, current designated sector list, source]

### Tax Provisions

- [Article, text/summary, source]

### EVC Act

- [Enforcement status, relevant Cabinet Orders, source]
```

**Without legalcode-mcp**: Proceed using training knowledge. Mark all statutory references
`[VERIFY]` and note in Glass Box: `legalcode_mcp: "Not connected"`.

### Step 4: Route to Modules

Based on task type, activate the relevant modules:

| Task                         | Primary Module | Supporting                           |
| ---------------------------- | -------------- | ------------------------------------ |
| J-KISS review/structuring    | A              | E (angel tax), F (FEFTA if foreign)  |
| Priced preferred round       | B              | C (shareholder agreement), F (FEFTA) |
| Shareholder agreement review | C              | B                                    |
| FIEA fund compliance         | D              | F                                    |
| Angel tax eligibility        | E              | A (J-KISS warrants)                  |
| FEFTA screening              | F              | D                                    |
| EVC impact analysis          | G              | C                                    |
| Employee stock options       | H              | E                                    |
| Full structuring analysis    | All            | —                                    |

### Step 5: Execute Module Analysis

Run each activated module in sequence. Apply classification:

- **Instrument selection**: OPTIMAL / SUBOPTIMAL / INCOMPATIBLE
- **Document review**: COMPLIANT / FLAG / NON-COMPLIANT
- **Regulatory compliance**: AVAILABLE / PARTIAL / NOT AVAILABLE

**⟁ CLARIFY** on any material undisclosed facts before delivering a compliance conclusion.

### Step 6: Classify Findings

Apply the Severity Classification system (see below). For each finding:

- State the finding
- Classify its severity
- Provide the actionable recommendation

### Step 7: Apply Prioritization Framework

Sort all findings into Tier 1 / Tier 2 / Tier 3 (see Prioritization Framework below).

### Step 8: Quality Verification

Before delivery:

1. Run Citation Quality Gates (5 gates — see below)
2. For every NON-COMPLIANT / RED finding: apply 3-pass Self-Interrogation
3. Assign Confidence Score to each material conclusion
4. Verify all [JURISDICTION-SPECIFIC] markers are resolved for Japan context
5. Generate Glass Box Audit Trail

### Step 9: Deliver Output

Structure using the Output Format Template below.

---

## Module A — J-KISS Analysis

### What is J-KISS?

J-KISS (J-KISS型新株予約権, "J-KISS Warrant") is Japan's standard seed-stage convertible
instrument. Legally structured as a _shinkabu yoyakuken_ (新株予約権 — stock acquisition
right/warrant) under **Companies Act Article 236**, it functions analogously to a US SAFE
but with important structural differences.

**Key distinctions from US SAFE:**

| Feature                      | US SAFE (YC post-money) | J-KISS v2.0                                                      |
| ---------------------------- | ----------------------- | ---------------------------------------------------------------- |
| Legal vehicle                | Simple contract         | Shinkabu yoyakuken (Companies Act warrant)                       |
| Discount                     | Optional                | 20% (market standard)                                            |
| Valuation cap                | Yes (post-money)        | Yes (post-money in v2.0)                                         |
| MFN clause                   | Optional                | Yes (standard)                                                   |
| Maturity                     | None                    | 18 months                                                        |
| Exit multiple pre-conversion | 1×                      | **2×** (cash or convert, investor's choice)                      |
| Angel tax eligible           | N/A                     | Yes (from 1 April 2024)                                          |
| Board approval required      | No                      | **Yes** (special resolution required)                            |
| FEFTA classification         | N/A                     | Not "foreign direct investment" — no prior notification required |

### J-KISS Standard Terms (v2.0 — Coral Capital / Mori Hamada template)

| Term                        | Standard / Default                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------- |
| Valuation cap               | Post-money; negotiated per deal                                                       |
| Discount rate               | 20%                                                                                   |
| MFN clause                  | Yes — investor receives benefit of more favourable terms in subsequent J-KISS rounds  |
| Qualified financing trigger | ¥100M equity round (adjustable)                                                       |
| Maturity                    | 18 months                                                                             |
| Maturity conversion         | Majority of J-KISS holders may elect conversion at valuation cap price                |
| Conversion price            | Lower of: (a) cap ÷ fully-diluted pre-money cap; (b) financing price × (1 − discount) |
| Pre-conversion exit         | Investor chooses: 2× cash or convert at cap and receive M&A proceeds                  |
| MFN scope                   | All new J-KISS issuances post-signing                                                 |
| Governing law               | Japan; Companies Act                                                                  |

### Review Checklist — J-KISS Document

**Structural completeness (COMPLIANT / FLAG):**

- [ ] Instrument structured as shinkabu yoyakuken — not as a loan or simple contract
- [ ] Terms of issuance (_hakkō yōkō_) prepared and board resolution obtained
- [ ] Shareholders' meeting special resolution obtained if "particularly favorable terms" allotment
- [ ] Post-money cap (v2.0) — confirm whether pre-money (v1.x) or post-money cap applies
- [ ] Qualified financing threshold defined — confirm ¥100M or adjusted amount is appropriate
- [ ] 18-month maturity — majority conversion right mechanism documented
- [ ] 2× exit multiple confirmed; investor election mechanism specified
- [ ] MFN clause present; scope defined
- [ ] Pari passu with general creditors on liquidation (not subordinated)

**Angel tax compliance (COMPLIANT / FLAG / NON-COMPLIANT):**

- [ ] Company has obtained or applied for prefecture confirmation (_kakuninsho_)
- [ ] Company meets METI eligibility criteria (≤5 years old, ≥1/6 external ownership, not
      large group, unlisted KK)
- [ ] Investment documentation references exercise date (not issuance date) as controlling
      date for angel tax deduction (post-April 2024 rule)
- [ ] Investor is an individual (corporate VCs do not qualify for angel tax)

**FEFTA (if foreign investor):**

- [ ] Confirm J-KISS is structured as shinkabu yoyakuken — acquisition of J-KISS warrants
      is **not** classified as "foreign direct investment" under FEFTA; no prior notification
      required at seed stage via J-KISS (even for foreign investors in sensitive sectors)
- [ ] Note: conversion into equity shares at Series A **will** trigger FEFTA FDI analysis

**Common deviations and flags:**

| Deviation                                          | Classification | Issue                                                                     | Recommended Action                                              |
| -------------------------------------------------- | -------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Pre-money cap (v1.x) used                          | FLAG           | Higher investor dilution at conversion vs. market standard                | Negotiate post-money cap or obtain detailed cap table modelling |
| Qualified financing threshold >¥300M               | FLAG           | J-KISS may never convert; overhang risk                                   | Lower threshold to ¥100M–¥150M                                  |
| No MFN clause                                      | FLAG           | Investor unprotected against better terms in later J-KISS                 | Add standard MFN clause                                         |
| Exit multiple below 2×                             | FLAG           | Below J-KISS v2.0 market standard                                         | Reinstate 2× floor or document rationale                        |
| No majority conversion right at maturity           | NON-COMPLIANT  | No enforcement mechanism at 18 months; J-KISS becomes zombie instrument   | Add majority holder conversion election                         |
| Structured as loan not warrant                     | NON-COMPLIANT  | Not a valid J-KISS; angel tax ineligible; different liquidation treatment | Restructure as shinkabu yoyakuken                               |
| No board resolution / no hakkō yōkō                | NON-COMPLIANT  | Issuance invalid under Companies Act                                      | Obtain board resolution; prepare terms of issuance              |
| Angel tax — no prefecture confirmation             | FLAG           | Investor cannot claim deduction                                           | Obtain pre-confirmation from relevant prefecture before closing |
| Angel tax — issuance date used (not exercise date) | NON-COMPLIANT  | Investor tax deduction will fail post-April 2024 rules                    | Update documentation to reference exercise date                 |

---

## Module B — Priced Preferred Round / Term Sheet Analysis

### KK Preferred Share Mechanics

A _Kabushiki Kaisha_ (KK, 株式会社) issues **preferred shares (種類株式)** under **Companies
Act Article 108**. Each round is a new class: A-type preferred (A種優先株式), B-type, C-type,
etc. Preferred share terms must be set out in the **articles of incorporation (定款)** before
issuance — requiring an **articles amendment (special resolution: 2/3 majority)** at each new
round.

### Key Share Terms to Review

**Liquidation preference (残余財産優先分配権):**

| Term                         | Market Standard (Japan)                                            | Watch for                                                                     |
| ---------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Preference multiple          | 1× invested amount                                                 | >2× preference — aggressive; flag                                             |
| Participation                | **Participating** (uncapped "double-dip" is still common in Japan) | Non-participating is increasingly negotiated; cap on participation >3× rounds |
| Priority vs. other preferred | Pari passu on liquidation (most common)                            | Strictly senior waterfall — complex; flag                                     |
| Deemed liquidation           | M&A triggers preference                                            | Absent deemed liquidation clause — NON-COMPLIANT                              |

**Anti-dilution protection:**

| Feature            | Market Standard                                    | Watch for                                        |
| ------------------ | -------------------------------------------------- | ------------------------------------------------ |
| Anti-dilution type | Broad-based weighted average (fully diluted)       | Full ratchet — NON-COMPLIANT                     |
| Trigger            | Any issuance at lower price                        | Pay-to-play not common in Japan; note if present |
| Carve-outs         | Employee options, J-KISS conversions, stock splits | Absent carve-outs — FLAG                         |

**Conversion rights:**

- Automatic conversion on IPO (at ratio ≥ 1:1 preferred:common)
- Optional conversion at investor election
- Conversion price adjustment mechanism for anti-dilution

**Veto rights (拒否権):**

Standard veto right items in Japanese VC shareholder agreements:

| Category   | Veto Item                                  | Notes                        |
| ---------- | ------------------------------------------ | ---------------------------- |
| Corporate  | New share issuance of any class            | Must include                 |
| Corporate  | Articles amendment                         | Must include                 |
| M&A        | Merger, company split, share exchange      | Must include                 |
| M&A        | Material asset disposal                    | Must include                 |
| Finance    | New debt above threshold                   | Include threshold amount     |
| Operations | Related-party transactions above threshold | Include threshold            |
| Governance | IPO timing and underwriter selection       | Standard in Japan            |
| Governance | New director appointments                  | Optional; common             |
| Finance    | EVC grant (from spring 2026)               | **Add post-EVC enforcement** |

**Transfer rights in shareholder agreement (株主間契約):**

| Right                     | Description                                                          | Classification if Absent     |
| ------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| ROFR (先買権)             | Right of first refusal on founder/other investor transfers           | FLAG                         |
| Tag-along (共売権)        | Investor co-sells proportionate shares on same terms as founder sale | FLAG                         |
| Drag-along (従随権)       | Majority investors compel minority to sell in approved M&A           | FLAG if investor perspective |
| Founder vesting / lock-up | Share vesting or lock-up period post-investment                      | FLAG                         |

**Investor call options (_kōbai opushon_) on founder shares:**

Call options giving investors the right to purchase founder shares at par on:

- Material breach of reps/warranties
- Material covenant breach
- Non-compete breach

> **Warning**: Blanket investor call options on all founder shares have been flagged by
> METI/JETRO (2022 guidelines) and the JFTC as potentially restrictive of competition
> under the Antimonopoly Act. Market is trending toward founder-friendly: limit call
> options to material breach scenarios with defined cure periods. Flag any call option
> that is not tied to specific triggering events.

### Term Sheet Review Checklist

**Minimum required terms (NON-COMPLIANT if absent):**

- [ ] Share class defined and articles-compatible
- [ ] Liquidation preference amount and participation stated
- [ ] Anti-dilution mechanism specified (BBWA or other)
- [ ] Conversion rights and ratio
- [ ] Deemed liquidation event defined
- [ ] Veto rights list
- [ ] Transfer restrictions (ROFR, tag-along minimum)
- [ ] Representations and warranties scope
- [ ] Conditions precedent to closing

**Market standard terms (FLAG if absent):**

- [ ] Board composition and investor appointment rights
- [ ] Information rights (quarterly management accounts, annual audited, annual plan)
- [ ] Pro-rata rights in future rounds
- [ ] Drag-along mechanism
- [ ] Founder vesting / lock-up
- [ ] IPO cooperation obligation
- [ ] Observer rights for smaller investors

---

## Module C — Shareholder Agreement (株主間契約) Review

### Structural Requirements

A Japanese shareholder agreement is a private contract among shareholders — not filed with
any public registry and not binding on the company unless the company is a party. Best
practice: make the company a party to the agreement to bind it.

**Key legal considerations:**

- Articles of incorporation govern share rights vis-à-vis the company (public filing)
- Shareholder agreement governs private rights among shareholders
- Inconsistencies between articles and shareholder agreement: articles prevail as between
  shareholders and the company; shareholder agreement enforceable as contract between parties
- Governing law: Japanese law (Civil Code, Companies Act)
- Dispute resolution: arbitration (JCAA rules in Tokyo) or Japanese courts

### Review Framework

**Governance — COMPLIANT / FLAG / NON-COMPLIANT:**

| Item                          | Check                                         | Flag Condition                                |
| ----------------------------- | --------------------------------------------- | --------------------------------------------- |
| Board appointment rights      | Clear per class, with ownership threshold     | Threshold not specified                       |
| Quorum and voting thresholds  | Set out for board and shareholder resolutions | Silent — defaults only                        |
| Deadlock mechanism            | Defined resolution process for board deadlock | Absent in founder-investor deadlock scenarios |
| Corporate auditor appointment | Investor auditor appointment right            | Absent if KK with audit obligation            |

**Economic rights — compliance check:**

| Item                   | Check                                         | Flag Condition                      |
| ---------------------- | --------------------------------------------- | ----------------------------------- |
| Liquidation preference | Matches articles; deemed liquidation included | Inconsistency with articles         |
| Anti-dilution          | BBWA mechanism; adjustment formula specified  | Full ratchet; absent formula        |
| Dividend rights        | Defined order of preference                   | Silent (defaults to pro-rata)       |
| Redemption rights      | Absent or very limited (market norm)          | Cash redemption demand right — FLAG |

**EVC provision (post-spring 2026):**

- [ ] Shareholder agreement includes grant of Enterprise Value Charge (EVC) as a **veto-right
      item** — company may not create an EVC without prior investor approval
- [ ] If EVC already granted: confirm it is disclosed; rank implications documented
- _Rationale_: An EVC creates a floating security interest over all company assets, ranking
  senior to equity on enforcement. Investors must control when portfolio companies can grant EVCs.

---

## Module D — FIEA Fund Compliance

### Fund Structure Selection

| Structure               | Legal Form                   | Best For                           | FIEA Treatment                        |
| ----------------------- | ---------------------------- | ---------------------------------- | ------------------------------------- |
| ILP                     | 投資事業有限責任組合         | Japanese domestic VC fund; GP + LP | LP interests = Paragraph 2 Securities |
| TK (silent partnership) | 匿名組合                     | Smaller funds; angel syndicates    | TK interests = Paragraph 2 Securities |
| GK-TK                   | GK as manager + TK structure | Foreign PE with Japan operations   | TK interests = Paragraph 2 Securities |
| Foreign fund            | Cayman LP / Delaware LP      | Foreign VC with Japanese LPs       | LP interests = Paragraph 2 Securities |

### FIEA Article 63 SPBQII Exemption — Form 20 Notification

The Article 63 exemption (_Tokutei Toshi-ka Tou Tokutei Jigyo_ — "Specially Permitted
Business for Qualified Institutional Investors, etc.") is the primary compliance pathway
for Japanese VC fund GPs.

**Conditions (all must be satisfied):**

| Condition           | Requirement                                                                                            | NON-COMPLIANT if                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| QII requirement     | At least **1 Qualified Institutional Investor (QII)** solicited in Japan                               | Zero QIIs in Japanese LP base                       |
| Non-QII cap         | Maximum **49 non-QII Japanese investors**                                                              | 50+ non-QII Japanese investors                      |
| Non-QII eligibility | Each non-QII must be an "eligible investor" (sophisticated individual / certain entities)              | Retail/unsophisticated Japanese investors solicited |
| Prior notification  | **Form 20** filed with relevant Local Finance Bureau (typically Kanto Finance Bureau) before marketing | Marketing commences before filing                   |
| Annual reporting    | Annual business report filed                                                                           | Failure to file                                     |
| Change notification | Material changes notified promptly                                                                     | Undisclosed material changes                        |

**QIIs include (statutory list — not exhaustive):**

- Japanese banks (_ginko_), insurance companies (_hokensha_)
- Type I Financial Instruments Business Operators
- Investment corporations (_toshi hojin_)
- Government Pension Investment Fund (GPIF)
- Registered foreign securities firms

**⟁ CLARIFY**: If investor count includes both Japanese and non-Japanese investors, confirm
the number of **Japanese** non-QII investors specifically. Non-Japanese investors do not
count toward the 49-person non-QII cap.

### Type II Registration — When Required

Type II Financial Instruments Business Operator registration is required when:

- The Article 63 exemption is unavailable (no Japanese QII; >49 Japanese non-QIIs)
- Soliciting Japanese retail investors directly
- Acting as placement agent for another fund's Paragraph 2 Securities in Japan

**Registration requirements (summary):**

- Minimum stated capital: ¥10M
- Compliance officer appointment
- Internal control procedures
- Financial statements filed with FSA
- Registration timeline: approximately 3–6 months

### FIEA Compliance Checklist

**Article 63 path (COMPLIANT / FLAG / NON-COMPLIANT):**

- [ ] At least 1 Japanese QII confirmed in LP base
- [ ] Japanese non-QII count: ≤49 (track carefully; aggregate count over fund lifecycle)
- [ ] Each non-QII investor confirmed as "eligible investor" (documentation in LP file)
- [ ] Form 20 filed before first Japanese investor solicitation
- [ ] Annual business report filing system in place
- [ ] Marketing materials do not constitute "public solicitation" (no general advertising)

**2016 reform compliance:**

- [ ] Enhanced non-QII eligibility confirmed (2016 tightening applies)
- [ ] Record-keeping obligations satisfied
- [ ] No misleading materials used in fund marketing

**J-KISS and Paragraph 1 Securities:**

- J-KISS (_shinkabu yoyakuken_) is a **Paragraph 1 Security** (warrant)
- Private issuance to ≤49 investors over 6 months = small-number private placement (少人数私募)
  — no registration required
- Any general solicitation for J-KISS investments = triggers securities registration — NON-COMPLIANT

---

## Module E — Angel Tax Incentives (エンジェル税制)

### Overview

Japan's angel tax system provides two benefits to **individual investors** (not corporate VCs):

| Benefit                            | Description                                                            | Limit                                                       |
| ---------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| Measure A — Income deduction       | Deduct investment amount from taxable income in year of investment     | Lesser of ¥8M or 40% of total taxable income                |
| Measure B — Capital gains rollover | Defer tax on exit gains by rolling over into new qualifying investment | No cap; reinvestment window now 2 years (from January 2026) |

### Eligibility Requirements

**Company eligibility (METI certification required):**

| Requirement             | Standard                                                       | Check                                       |
| ----------------------- | -------------------------------------------------------------- | ------------------------------------------- |
| Age                     | Established ≤5 years (≤10 for certain sub-measures)            | Confirm incorporation date                  |
| External ownership      | ≥1/6 of total shares from non-founder third parties            | Cap table review                            |
| Group structure         | Not part of large corporate group                              | Parent entity analysis                      |
| Listing status          | Unlisted KK only                                               | Confirm not listed or planning imminent IPO |
| Sector                  | No adult entertainment; no large-company-controlled operations | Confirm                                     |
| Innovation criteria     | R&D expenditure threshold or other METI innovation criteria    | Request METI confirmation                   |
| Prefecture confirmation | _Kakuninsho_ (確認書) obtained from relevant prefecture        | **Condition precedent to angel tax**        |

**J-KISS / warrant-specific rules (from 1 April 2024):**

- Acquisition of _shinkabu yoyakuken_ (including J-KISS) now qualifies
- Controlling date = **exercise date** (conversion date), not issuance date
- Investor must exercise (convert) J-KISS before year-end to claim deduction in that tax year
- Common mistake: investor assumes deduction year = J-KISS investment date — **incorrect** post-2024

**Capital gains rollover extension (from 1 January 2026):**

- Reinvestment window extended from same year to **end of following calendar year** (max 2-year window)
- Minimum holding period introduced: shares must be held until end of year following acquisition
  (IPO/M&A exit exceptions apply)
- Applicable to acquisitions from 1 January 2026

### Angel Tax Checklist

**Company obligations (NON-COMPLIANT if absent):**

- [ ] Prefecture confirmation (_kakuninsho_) obtained — or pre-confirmation application submitted
- [ ] Company listed on METI prefecture confirmation public register
- [ ] Company meets METI guideline _r7_ (July 2025) eligibility requirements for investments from April 2025
- [ ] Subscription documentation confirms exercise date as the controlling date for J-KISS investments

**Investor obligations (FLAG if unaddressed):**

- [ ] Investor is an individual (not a corporation — angel tax is individual-only)
- [ ] Investor will file confirmation certificate with individual tax return
- [ ] Investor understands exercise date rule for J-KISS (not investment date)
- [ ] For rollover: prior qualifying investment gain being rolled over is documented

**Red flag scenarios:**

- Company fails post-investment METI eligibility criteria → retroactive investor tax liability risk
- Investor files deduction based on J-KISS issuance date (not exercise date) → deduction disallowed
- Company obtains confirmation but investor fails to file certificate → no deduction
- Corporate VC fund investing → angel tax inapplicable (individual investors only)

---

## Module F — FEFTA Foreign Investment Screening

### When Prior Notification is Required

Under the Foreign Exchange and Foreign Trade Act (FEFTA), a **foreign investor** acquiring
**any shares in an unlisted KK** (even a single share) must analyse FX Act obligations.
Prior notification (_jizen todoke_) is required if **all three** conditions are met:

1. The acquirer is a "foreign investor" under FEFTA
2. The target company is in a **designated or core business sector**
3. No valid exemption applies

**Foreign investor definition (includes):**

- Non-resident individuals
- Foreign corporations
- Japanese entities with ≥50% foreign voting rights (direct or indirect)
- Investment partnerships where non-residents are ≥50% of capital or hold majority of managing partners
- **2025 new category**: "Specified Foreign Investors" — entities/individuals obligated to
  disclose sensitive information to foreign governments; **no exemptions available**

### Designated and Core Business Sectors

Effectively all tech startups are in designated sectors. Key sectors:

| Sector                                    | In-scope?   | Notes                                      |
| ----------------------------------------- | ----------- | ------------------------------------------ |
| Software development                      | **Yes**     | Internet support services; data processing |
| SaaS / cloud services                     | **Yes**     | Telecoms; data processing                  |
| Cybersecurity                             | **Yes**     | Core Business Sector                       |
| Life sciences / pharma                    | **Yes**     | Core Business Sector                       |
| Defence / aerospace                       | **Yes**     | Core Business Sector                       |
| Semiconductors / electronics              | **Yes**     | Core Business Sector                       |
| Pure services (e.g., retail, hospitality) | Possibly no | Sector-by-sector analysis required         |

**⟁ CLARIFY**: Before completing FEFTA analysis, confirm the exact business of the target
company and check against the current METI/MOF designated sector list (updated periodically).

### Exemption Conditions

A foreign investor **may invoke the standard exemption** (avoiding prior notification) if
they undertake all of the following:

1. Will **not** cause closely related persons to become director or statutory auditor of target
2. Will **not** propose disposal or transfer of business in designated sector at shareholders' meeting
3. Will **not** access non-public technology information related to designated sectors

> **Critical**: Conditions 1–3 are **incompatible with standard VC governance**.
> A foreign VC investor who wants a board seat, veto rights over business changes,
> or access to technology diligence **cannot** use the standard exemption.
> **The correct path for foreign VCs taking governance rights is to file for prior notification**,
> not to invoke the exemption.

**Specified Foreign Investors (2025):** Cannot claim any exemption for Core Business Sector
targets. Prior notification is mandatory.

### J-KISS structural advantage for foreign investors

**Acquisition of J-KISS warrants (_shinkabu yoyakuken_) by a foreign investor does NOT
constitute "foreign direct investment" under FEFTA** — prior notification is not required
at the J-KISS stage, even for targets in sensitive sectors.

This is a significant structural tool: foreign VCs can invest at seed stage via J-KISS
without triggering FEFTA, deferring the compliance burden to the Series A equity round.

**Note**: When J-KISS converts into equity shares at Series A, FEFTA prior notification
analysis applies to the conversion. Plan for this in deal timeline.

### FEFTA Prior Notification Process

- **File with**: Bank of Japan (accepting on behalf of relevant Ministry/MOF)
- **Standard review period**: 30 days from Bank of Japan acceptance
- **Fast-track**: 4 business days to 2 weeks for straightforward low-risk cases
- **Extended**: Up to 5 months for national security concerns
- **Post-investment reporting**: Required within 45 days of completion even if no prior
  notification filed

### FEFTA Checklist (Foreign VC Investor)

**Analysis steps (NON-COMPLIANT if prior notification required but not filed):**

- [ ] Confirm investor is "foreign investor" under FEFTA (including 2025 Specified classification check)
- [ ] Screen target sector against current METI/MOF designated sector list
- [ ] If in designated sector: assess exemption availability
- [ ] If governance rights sought (board seat, veto rights, tech access): prior notification required
- [ ] If J-KISS instrument: no prior notification required at warrant stage; plan for Series A
- [ ] File prior notification before signing, with sufficient runway for 30-day review period
- [ ] File post-investment report within 45 days of completion

---

## Module G — Enterprise Value Charge (EVC / 企業価値担保権)

### Status and Timeline

| Event                            | Date                                           |
| -------------------------------- | ---------------------------------------------- |
| Act enacted (Act No. 52 of 2024) | 7 June 2024                                    |
| Act promulgated                  | 14 June 2024                                   |
| Target enforcement               | **Spring 2026** (Cabinet Orders pending)       |
| Latest enforcement deadline      | 14 December 2026 (2.5 years from promulgation) |

As of March 2026, the Act is enacted but Cabinet Orders/Ordinances required for full
implementation are pending. Monitor FSA announcements.

### What is an EVC?

The EVC is a new security interest enabling a company's **entire enterprise value** —
all present and future assets, intangibles, goodwill, know-how, customer relationships,
and future cash flows — to serve as collateral. It is Japan's first floating-charge
equivalent, created through a **security trust structure**.

**Structure:**

- **Settlor/Debtor**: The borrowing KK (not individuals or foreign entities)
- **Trustee**: Licensed "Enterprise Value Charge Trust Company"
- **Specified Secured Creditors**: Banks/lenders with specified claims; receive priority distributions
- **Unspecified Secured Creditors**: General creditors receiving a reserved share

**Priority**: Determined by **commercial registry registration date** — earlier registration
ranks higher.

**Enforcement**: Court-ordered proceeding → court-appointed enforcement trustee → going
concern business transfer (not piecemeal liquidation). This deliberately preserves enterprise value.

### EVC Impact on VC Deal Structure

**Why VC investors must act now (even pre-enforcement):**

| Risk                                   | Impact                                                                                       | Mitigation                                                  |
| -------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Portfolio company grants EVC to lender | Creates floating charge over all company assets, ranking **senior to equity** on enforcement | Add EVC as veto-right item in shareholder agreement         |
| EVC enforcement = business transfer    | Preferred liquidation preferences paid only from residual after EVC holders satisfied        | Negotiate EVC restriction covenant in shareholder agreement |
| Multiple EVCs possible                 | First-registered EVC ranks first — no maximum cap required                                   | Monitor commercial registry for any EVC registrations       |
| Existing FEFTA governance restrictions | Foreign VC with exemption may not have access to tech information needed for EVC diligence   | Use prior notification path instead of exemption            |

**Shareholder agreement EVC provision (add immediately):**

The company shall not, without the prior written consent of investors holding [X]% of
preferred shares, grant or permit to exist any Enterprise Value Charge (企業価値担保権,
as created under Act No. 52 of 2024 and any implementing Cabinet Orders) over any of
its assets.

**Due diligence requirement (post-enforcement):**

- Check commercial registry for EVC registrations on target company before any VC investment
- EVC is registered in commercial registry — publicly searchable

---

## Module H — Employee Stock Options (新株予約権 / ストックオプション)

### Tax-Qualified Stock Options (税制適格ストックオプション)

Under **Article 29-2 of the Act on Special Measures Concerning Taxation**, employees,
directors, and contractors who receive qualifying stock options benefit from:

- No income tax at **exercise** (contrast: non-qualifying = income tax at exercise)
- Tax deferred to **sale of shares** and treated as capital gains (20.315% effective rate)

**2024 reform key changes (effective from April 2024):**

| Feature                   | Pre-2024            | Post-2024                                                                                                          |
| ------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Exercise period           | Up to 10 years      | **Up to 15 years** for companies ≤5 years old                                                                      |
| Annual exercise price cap | ¥12M                | **¥36M** (3× increase)                                                                                             |
| Share custody requirement | Mandatory custodian | **Self-custody now permitted**                                                                                     |
| Board delegation of terms | Limited             | Board can now delegate exercise price/period determination (with shareholders' meeting approval for 15-year terms) |

**Qualifying conditions (all must be satisfied):**

- Recipient is an employee, director, or approved contractor of the company or subsidiary
- Exercise price ≥ share fair market value at grant date
- Exercise period: 2–15 years from grant (within statutory maximum)
- Annual exercise price within ¥36M cap
- No transfer of options (must be non-transferable and non-pledgeable)
- Shares deposited with custodian at exercise (or self-custody under new rules)

**Non-qualifying stock options (非適格ストックオプション):**

- Income tax at exercise on difference between exercise price and FMV
- Still useful for contractors not eligible for tax-qualified options
- Or where exercise price < FMV at grant (which disqualifies tax treatment)

### Stock Option Review Checklist

**Tax qualification (NON-COMPLIANT if conditions not met):**

- [ ] Exercise price ≥ FMV at grant (valuations for unlisted companies: use company assessment or recent transaction price)
- [ ] Exercise period within statutory range (2–15 years for eligible companies)
- [ ] Annual exercise price within ¥36M cap
- [ ] Non-transferable and non-pledgeable confirmed in option agreement
- [ ] Shareholders' meeting approval for 15-year exercise period delegation (if using new authority)
- [ ] Recipient eligibility confirmed (employees, directors, qualifying contractors)

**Employee experience quality (FLAG if missing):**

- [ ] Option pool size adequate for competitive employee equity
- [ ] Vesting schedule defined (standard: 1-year cliff + 4-year monthly vesting)
- [ ] Acceleration provisions (single trigger / double trigger) defined
- [ ] Exercise period post-termination specified
- [ ] Anti-dilution adjustment on stock splits / share combinations

---

## Severity Classification System

### Instrument Selection: OPTIMAL / SUBOPTIMAL / INCOMPATIBLE

| Classification   | Meaning                                                                    | Action                                         |
| ---------------- | -------------------------------------------------------------------------- | ---------------------------------------------- |
| **OPTIMAL**      | Best fit for stage, investor base, tax goals, and legal constraints        | Recommend and proceed                          |
| **SUBOPTIMAL**   | Functional but leaves material value or compliance efficiency on the table | Flag with specific improvement                 |
| **INCOMPATIBLE** | Not appropriate due to legal, regulatory, or structural constraints        | Do not use; explain why; recommend alternative |

### Document Review: COMPLIANT / FLAG / NON-COMPLIANT

| Classification    | Meaning                                                                               | Action                                                            |
| ----------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **COMPLIANT**     | Term meets Japanese legal requirement and market standard                             | Note for awareness                                                |
| **FLAG**          | Diverges from market standard or creates addressable risk not rising to NON-COMPLIANT | Specific redline or recommendation with fallback                  |
| **NON-COMPLIANT** | Violates statutory requirement, regulatory obligation, or fundamental market norm     | Immediate remediation required; do not proceed without resolution |

### Regulatory Compliance: AVAILABLE / PARTIAL / NOT AVAILABLE

| Classification    | Meaning                                                                 | Action                                             |
| ----------------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| **AVAILABLE**     | Company/transaction qualifies; conditions satisfied                     | Confirm conditions and proceed                     |
| **PARTIAL**       | Qualification possible but specific conditions must be met or confirmed | List conditions; recommend counsel confirmation    |
| **NOT AVAILABLE** | Does not qualify; cannot be restructured to qualify                     | Do not rely on this pathway; recommend alternative |

---

## Prioritization Framework

### Tier 1 — Critical (Must Resolve Before Closing)

- FIEA Article 63 exemption conditions violated (50+ non-QII, no QII, general solicitation)
- FEFTA prior notification required but not filed (foreign VC + designated sector + governance rights)
- J-KISS structured as loan or simple contract — not as shinkabu yoyakuken
- Missing mandatory board resolution or special shareholders' resolution for share issuance
- EVC already granted over all assets by portfolio company (ranking senior to equity)
- Angel tax — company lacks prefecture confirmation (no deduction available to investors)
- Stock options — exercise price below FMV at grant (tax disqualification)

### Tier 2 — Important (Address Before Finalizing)

- J-KISS qualified financing threshold miscalibrated (too high — creates zombie J-KISS risk)
- Participating liquidation preference: uncapped double-dip on moderate-value exits
- Anti-dilution: full ratchet used instead of BBWA
- Absent deemed liquidation clause (M&A not triggering preference)
- Investor call option on founder shares: blanket (not limited to material breach)
- Absent EVC veto right in shareholder agreement (post-spring 2026 risk)
- FEFTA: foreign VC claiming standard exemption while holding board seat — incompatible
- Angel tax: investment documentation uses issuance date not exercise date (post-April 2024)
- Form 20 notification not yet filed but fund marketing commencing

### Tier 3 — Advisory (Consider / Best Practice)

- Negotiate non-participating or capped preferred (market trend in Japan)
- Add post-investment EVC registry check procedure to due diligence checklist
- Align shareholder agreement veto right list with METI/JETRO 2022 guidelines
- Use English-language METI 2025 Model LPA for foreign LP capital attraction
- Obtain advance FEFTA informal consultation for complex cross-border structures
- Extend angel tax rollover window benefit (2-year reinvestment window from January 2026)

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivery.

| Gate           | Rule                                                                                                                                                                                                      | Fail Action                                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific statute (article number), regulation, or official guideline                                                                                                            | Add citation or mark `[UNVERIFIED — bengoshi to confirm]`                |
| **Format**     | All citations follow Japanese legal citation format: Act name, Act number, article number                                                                                                                 | Fix format                                                               |
| **Currency**   | Every cited provision checked for recent amendments — key reform dates: April 2024 (stock options, angel tax J-KISS eligibility); 2024 ILP amendment; 2025 FEFTA amendment; spring 2026 (EVC enforcement) | Flag `[CHECK CURRENCY — may have been amended]`                          |
| **Domain**     | Analysis stays within Japanese law. No US/UK/EU concepts imported without explicit flag                                                                                                                   | Remove or flag with `[JURISDICTION-SPECIFIC — does not apply in Japan]`  |
| **Confidence** | Uncertainty explicitly stated. EVC provisions marked `[VERIFY — enforcement pending]` until Cabinet Orders confirmed                                                                                      | Add confidence qualifier; never state EVC enforcement details as settled |

---

## Self-Interrogation for NON-COMPLIANT Findings

For every **NON-COMPLIANT** or **Tier 1 Critical** finding, apply this 3-pass review
before delivery:

**Pass 1 — Statutory Chain Integrity**
Does the NON-COMPLIANT conclusion follow directly from the cited statutory provision?

- Confirm article number and current text
- Would FSA / MOF / a court actually reach this conclusion on these facts?
- Is there a counter-argument that the structure is acceptable?

**Pass 2 — Completeness**

- Are there exceptions, safe harbours, or exemptions not yet considered?
- Have recent amendments been checked? (Key reform dates above)
- Are there regulatory guidance documents or FSA no-action letters that qualify the rule?
- Has the specific factual scenario been mapped to the statute correctly?

**Pass 3 — Proportionality Challenge**

- What is the strongest argument that this structure IS compliant?
- Under what circumstances might qualified Japanese counsel accept this risk?
- Is the NON-COMPLIANT classification proportionate to the legal risk?

If any pass reveals weakness, revise classification before delivery.
Mark audit trail: `self_interrogation: "PASS"` or `self_interrogation: "REVISED — [reason]"`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                     | Action                                                 |
| ------------ | --------- | --------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law; clear statutory text; unambiguous FSA/METI guidance            | State with confidence                                  |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions                            | State with brief caveat                                |
| **Probable** | 0.60–0.79 | Good arguments; reasonable minds could differ; guidance directionally clear | State with explicit reasoning and contra-indicators    |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities; EVC provisions pre-enforcement  | Flag for _bengoshi_ review; present both sides         |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; extrapolating from non-Japanese precedent          | Do not assert; flag `[UNCERTAIN — bengoshi to advise]` |

**EVC confidence note**: All EVC analysis is **Possible (0.40–0.59)** until Cabinet Orders
are issued and enforcement begins. The Act is enacted but implementing regulations are
pending. Mark all EVC provisions `[VERIFY — EVC implementing regulations pending, spring 2026]`.

---

## Anti-Patterns

What NOT to do when advising on Japanese venture financing:

1. **Treating J-KISS as a simple contract** — J-KISS is a _shinkabu yoyakuken_ under
   Companies Act Article 236. It requires board resolution, terms of issuance, and
   shareholder approval if "particularly favorable terms" allotment. Treating it as a
   simple contractual IOU renders it invalid.

2. **Using the J-KISS issuance date for angel tax** — Post-April 2024, the **exercise
   (conversion) date** is the controlling date for angel tax deduction. Investors who plan
   the year of their deduction around the J-KISS signing date will file incorrectly.

3. **Assuming FEFTA exemption is compatible with VC governance** — The standard FEFTA
   exemption prohibits the foreign investor from: taking a board seat, proposing business
   changes at shareholders' meetings, and accessing sensitive technology information.
   These conditions are incompatible with normal VC governance. **Prior notification is
   the correct path for foreign VCs who want governance rights.**

4. **Claiming FEFTA prior notification is not required because the foreign VC is "passive"**
   — The FEFTA triggering event for unlisted KKs is any single share acquisition regardless
   of stake size. "Passive" is not a FEFTA category; the exemption conditions (not passivity)
   determine whether notification is required.

5. **Stacking J-KISS rounds without cap table modelling** — Multiple J-KISS rounds with
   different valuation caps and discount rates create complex, opaque conversion tables.
   Always model the cap table at various Series A prices before committing to additional
   J-KISS rounds.

6. **Setting the qualified financing threshold too high** — A ¥100M+ threshold was standard
   when J-KISS was designed for a different fundraising environment. For early-stage seed
   rounds, if the Series A is expected to be smaller, a threshold of ¥50M–¥150M may be
   more appropriate. Too-high thresholds create "zombie J-KISS" instruments that never
   convert automatically.

7. **Using participating liquidation preference without exit scenario modelling** — Uncapped
   "double-dip" participating preferred is still common in Japan but creates severe founder
   misalignment at moderate exit values. Model exits at 1×, 2×, 3×, and 5× the invested
   capital before accepting uncapped participation.

8. **Accepting blanket investor call options on founder shares** — METI/JETRO 2022 guidelines
   and JFTC guidance flag blanket call options as potentially restrictive under the
   Antimonopoly Act. Limit call options to specific material breach triggers with defined
   cure periods. Blanket "at any time" or "at any departure" call options are NON-COMPLIANT
   with emerging regulatory expectations.

9. **Structuring a GK (_Godo Kaisha_) for multi-round VC financing** — A GK lacks a
   share-based capital structure compatible with Japanese VC standard documentation.
   Use a KK for any startup planning institutional VC investment.

10. **Forgetting to add EVC as a veto-right item in shareholder agreements** — Post-spring
    2026 EVC enforcement, any portfolio company that can freely grant an EVC has effectively
    granted a floating charge over all its assets to a lender, ranking senior to preferred
    shareholders on enforcement. Add EVC consent as a standard investor veto right immediately.

11. **Advising a corporate VC fund manager that their angel investor clients qualify for
    angel tax** — Angel tax (エンジェル税制) applies to **individual investors only**. A
    VC fund entity does not qualify regardless of its portfolio company's METI confirmation
    status. The deduction flows to the individual LPs who invest directly, not through a fund.

12. **Ignoring the interaction between FIEA Article 63 non-QII count and co-investors**
    — The 49 non-QII cap is tracked per fund, not per closing. Co-investors added in
    subsequent closings count toward the running total. GPs must maintain meticulous
    investor-eligibility records across all closings. Exceeding the cap invalidates the
    exemption for the **entire fund**, not just the excess investors.

13. **Treating the METI 2025 English Model LPA as a translation of the Japanese version**
    — The English and Japanese versions of the METI 2025 Model LPA are **not translations
    of each other**. The English version contains materially different provisions (fair
    allocation, AIVs, feeder fund provisions, expanded unilateral GP amendment rights) that
    are absent from the Japanese version. Use them as separate templates, not interchangeably.

14. **Failing to plan for FEFTA prior notification timing at J-KISS to Series A conversion**
    — When J-KISS converts at Series A, the foreign investor's acquisition of equity shares
    triggers FEFTA FDI analysis. This requires a 30-day notification window. If no one plans
    for this, Series A closing timelines will be materially disrupted.

15. **Assuming the 2025 FEFTA Specified Foreign Investor category does not apply** —
    Entities with obligations to disclose information to foreign governments are "Specified
    Foreign Investors" and cannot claim any exemption for Core Business Sector targets.
    Due diligence on foreign investors must now include screening against this classification.

16. **Using a pre-April 2024 J-KISS template without reviewing the angel tax provisions**
    — The April 2024 angel tax reform changed the controlling date for J-KISS investments.
    Pre-2024 templates may contain documentation language inconsistent with the exercise
    date rule. Always review and update angel tax provisions when using older J-KISS templates.

---

## Writing Standards

**For all findings and recommendations:**

- Lead with the finding, then the explanation. Example: "No deemed liquidation clause
  present — preferred liquidation preference will not trigger on an M&A exit. Add a deemed
  liquidation definition covering share sales, mergers, and asset sales where control changes."
- **Active voice**: "The company must obtain prefecture confirmation" not "Prefecture
  confirmation must be obtained by the company."
- **Short sentences**: One point per sentence.
- **Precise citations**: "Companies Act Article 199(2)" not "applicable company law."
- **Name the actor**: "The investor must file Form 20 before any Japanese investor solicitation"
  not "Form 20 must be filed."
- **Uncertainty flagged explicitly**: Use `[VERIFY]`, `[UNCERTAIN]`, or `[BENGOSHI TO ADVISE]`
  — never bury uncertainty in hedged language.
- **Japanese terms**: Include Japanese term with English translation on first use. Example:
  "Shinkabu yoyakuken (新株予約権 — stock acquisition right/warrant)."

**Quality gates before delivery:**

1. Can a founder without legal training understand the executive summary?
2. Can Japanese counsel understand and act on each FLAG/NON-COMPLIANT finding?
3. Is every statutory claim backed by specific article number (or flagged `[VERIFY]`)?
4. Are Japanese legal terms used with their English translations?
5. Is every EVC provision flagged `[VERIFY — implementing regulations pending]`?
6. Could any sentence be shorter? If yes, shorten it.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current Companies Act article text (Articles 108, 199, 236, 309, 324)
- Confirm current METI angel tax guideline version (_r7_ July 2025 or subsequent)
- Search for current FEFTA designated business sector list (updated periodically)
- Verify EVC implementing Cabinet Orders and ordinances (target spring 2026)
- Search for FSA guidance on Form 20 notification and Article 63 exemption conditions
- Save all verified citations to `/tmp/legalcode-vf-jp-authority.md`
- Mark all legalcode-mcp-sourced citations: `VERIFIED (legalcode-mcp, [date])`

**Without legalcode-mcp:**

- Proceed using training knowledge through August 2025 cutoff
- Mark all statutory references `[VERIFY]`
- Specifically note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag EVC analysis as higher-uncertainty given enforcement status: `[VERIFY — EVC not yet in force as of training cutoff]`
- Recommend client engage Japanese _bengoshi_ for statutory verification

---

## Output Format Template

````markdown
## Japan Venture Financing Analysis

**Company**: [Name / stage / sector]
**Task type**: [J-KISS review / Priced round / FIEA / FEFTA / Angel tax / EVC / Full]
**Perspective**: [Founder / VC GP / Foreign investor / Counsel]
**Investor base**: [Domestic / Foreign / Mixed]
**Modules activated**: [A, B, C, D, E, F, G, H as applicable]
**Date of analysis**: [date]

---

### Executive Summary

[3–5 bullet points. Non-technical. Lead with action items.]

---

### Instrument Recommendation

_(If instrument selection task)_

| Option                      | Classification                      | Rationale |
| --------------------------- | ----------------------------------- | --------- |
| J-KISS (shinkabu yoyakuken) | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |
| KK priced preferred round   | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |
| Other                       | OPTIMAL / SUBOPTIMAL / INCOMPATIBLE | [Reason]  |

**Recommended**: [Instrument] — [1-sentence rationale]

---

### Critical Findings (Tier 1)

| #   | Issue   | Module | Classification | Action Required   |
| --- | ------- | ------ | -------------- | ----------------- |
| 1   | [Issue] | [A–H]  | NON-COMPLIANT  | [Specific action] |

---

### Important Findings (Tier 2)

| #   | Issue   | Module | Classification | Action Required   |
| --- | ------- | ------ | -------------- | ----------------- |
| 1   | [Issue] | [A–H]  | FLAG           | [Specific action] |

---

### Advisory Items (Tier 3)

_(Summarise briefly)_

---

### FIEA Compliance Summary

_(If FIEA module activated)_

| Compliance pathway          | Available                           | Key conditions |
| --------------------------- | ----------------------------------- | -------------- |
| Article 63 SPBQII (Form 20) | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]   |
| Type II registration        | AVAILABLE / PARTIAL / NOT AVAILABLE | [Conditions]   |

---

### FEFTA Summary

_(If foreign investor or FEFTA module activated)_

| Obligation                   | Required?                       | Notes                                        |
| ---------------------------- | ------------------------------- | -------------------------------------------- |
| Prior notification           | Yes / No / Confirm              | [Rationale]                                  |
| Standard exemption available | Yes / No                        | [Reason if no — governance incompatibility?] |
| J-KISS seed investment       | No notification required        | Warrants are not FDI                         |
| Series A conversion          | Requires analysis at conversion | [Plan timeline]                              |

---

### Angel Tax Summary

_(If angel tax module activated)_

| Benefit                              | Available                           | Conditions to Confirm        |
| ------------------------------------ | ----------------------------------- | ---------------------------- |
| Measure A (income deduction)         | AVAILABLE / PARTIAL / NOT AVAILABLE | [List]                       |
| Measure B (capital gains rollover)   | AVAILABLE / PARTIAL / NOT AVAILABLE | [List]                       |
| J-KISS eligibility (post-April 2024) | AVAILABLE / NOT AVAILABLE           | [Confirm exercise date rule] |

---

### EVC Impact Assessment

_(If EVC module activated)_

| Risk                                      | Current Status                                     | Recommended Shareholder Agreement Provision |
| ----------------------------------------- | -------------------------------------------------- | ------------------------------------------- |
| Portfolio company may grant EVC           | Spring 2026 enforcement [VERIFY implementing regs] | Add EVC as investor veto right              |
| EVC ranks senior to equity on enforcement | Yes (once in force)                                | EVC restriction covenant                    |
| Due diligence — registry check            | Required post-enforcement                          | Add to DD checklist                         |

---

### Recommended Next Steps

1. [Highest-priority action]
2. [Next action]
3. [Engage Japanese bengoshi for: ...]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-venture-financing-jp"
  task_type: "[J-KISS / Priced round / FIEA / FEFTA / Angel tax / EVC / Full]"
  stage: "[Pre-seed / Seed / Series A / Later]"
  company_sector: "[Sector]"
  investor_base: "[Domestic / Foreign / Mixed]"
  modules_activated: "[A, B, C, D, E, F, G, H]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-vf-jp-authority.md or 'Not created']"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  evc_status: "[VERIFY — implementing regulations pending, spring 2026]"
  self_interrogation: "PASS / REVISED — [reason] / NOT APPLICABLE (no NON-COMPLIANT findings)"
  findings_summary:
    critical_tier1: "[number]"
    important_tier2: "[number]"
    advisory_tier3: "[number]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "EVC analysis is directional — Cabinet Orders pending as of analysis date"
    - "Angel tax analysis is directional — engage zeirishi for binding tax position"
    - "FEFTA sector analysis based on published sector list — verify currency against MOF/METI"
    - "J-KISS template review assumes Coral Capital v2.0 — confirm version used"
  reviewer: "AI-assisted — requires bengoshi review before reliance; zeirishi for tax positions"
```
````

```

---

## Localization Notes

This skill is **Japan-specific**. For cross-border or multi-jurisdiction venture financing
involving Japan, consider the following adjacent skills:

| Adjacent need | Recommended resource |
|--------------|---------------------|
| US venture financing (SAFE, QSBS, Reg D) | `legalcode-venture-financing-suite` (US track) |
| UK venture financing (ASA, SEIS/EIS) | `legalcode-venture-financing-suite` (UK track) |
| General cross-border VC structuring | `legalcode-venture-financing-suite` |
| Employment agreement under Japanese law | `legalcode-jp-labor-standards-compliance` |
| APPI / personal data compliance in Japan | `japan-appi-personal-data-breach-reporting-and-notification-operations` |

**Japanese legal terminology reference** (used throughout this skill):

| Japanese term | Romaji | English |
|--------------|--------|---------|
| 株式会社 | Kabushiki Kaisha (KK) | Joint-stock company (closest equivalent: corporation) |
| 新株予約権 | Shinkabu yoyakuken | Stock acquisition right / warrant |
| 種類株式 | Shurui kabu | Class of shares (preferred shares) |
| 株主間契約 | Kabunushi-kan keiyaku | Shareholder agreement |
| 定款 | Teikan | Articles of incorporation |
| 残余財産優先分配権 | Zanjyo zaisan yūsen bunpai-ken | Liquidation preference |
| 拒否権 | Kyohi-ken | Veto right |
| 共売権 | Kyōbai-ken | Tag-along right |
| 従随権 | Jūzui-ken | Drag-along right |
| 先買権 | Sakigai-ken | Right of first refusal |
| 買収オプション | Kōbai opushon | Call option (on shares) |
| 確認書 | Kakuninsho | Confirmation certificate (angel tax) |
| 弁護士 | Bengoshi | Attorney / lawyer |
| 税理士 | Zeirishi | Tax accountant |
| 企業価値担保権 | Kigyō kachi tanpo-ken | Enterprise Value Charge |
| エンジェル税制 | Enjeru zeisei | Angel tax incentive system |
| 匿名組合 | Tokumei kumiai | Silent partnership (TK) |
| 投資事業有限責任組合 | ILP / Toshi jigyo yugen sekinin kumiai | Investment limited partnership |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

**Primary legal sources:**
- Companies Act (会社法, Act No. 86 of 2005) — Articles 108, 199, 236, 247, 309, 324
- Financial Instruments and Exchange Act (FIEA, Act No. 25 of 1948, as amended)
  — Article 2 (securities definitions), Article 63 (SPBQII exemption)
- Investment Limited Partnership Act (Act No. 90 of 1998, as amended 2024)
- Act on Special Measures Concerning Taxation — Article 29-2 (tax-qualified stock options)
- Act on the Promotion of Cash Flow-Based Lending (Act No. 52 of 2024) — EVC
- Foreign Exchange and Foreign Trade Act (FEFTA, as amended through May 2025)
- METI Angel Tax Guidelines *r7* (July 2025)

**Industry documentation:**
- Coral Capital J-KISS v2.0 template (coralcap.co/j-kiss/, 2022)
- METI Model Limited Partnership Agreement 2025 (English and Japanese versions, June 2025)
- METI/JETRO "Key Points to Consider in Contracts for Sound Venture Investments in Japan"
  (2022 revision)
- JVCA primer on investment documentation

**Secondary research sources:**
- Chambers & Partners: Venture Capital 2025 — Japan (Trends and Developments)
- Baker McKenzie: Enterprise Value Charge analysis (2024)
- White & Case: Japan New LPA (2025 analysis)
- Ushijima & Partners: Model LPA 2025 client alert (June 2025)
- ICLG: Japan Alternative Investment Funds 2025–2026
- ICLG: Japan FDI Regimes 2026
- Norton Rose Fulbright: FEFTA analysis
- UPenn ALR: Convertible Equity in the Japanese Startup Ecosystem

**Attribution**: Legalcode original synthesis. No input skill provided.
```
