---
name: legalcode-venture-financing-de
description: German venture financing skill covering the full lifecycle from pre-seed instrument selection
  through Series A and beyond. Use when advising on Wandeldarlehen (convertible loans under BGB §488),
  GESSI standard bilingual documents, GmbH/UG startup structure, mandatory § 15 GmbHG notarization for
  share transfers, the INVEST federal angel grant (15% acquisition + 25% exit via BAFA), founder liability
  under § 43 GmbHG, VSOP/ESOP under German law including § 19a EStG deferral, the EuVECA passport (Regulation
  EU 345/2013), and German VC market term sheet standards (Gesellschaftervereinbarung, Liquidationspräferenz,
  Verwässerungsschutz, Mitverkaufspflicht).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

German venture financing skill covering the full lifecycle from pre-seed instrument selection through Series A and beyond. Use when advising on Wandeldarlehen (convertible loans under BGB §488), GESSI standard bilingual documents, GmbH/UG startup structure, mandatory § 15 GmbHG notarization for share transfers, the INVEST federal angel grant (15% acquisition + 25% exit via BAFA), founder liability under § 43 GmbHG, VSOP/ESOP under German law including § 19a EStG deferral, the EuVECA passport (Regulation EU 345/2013), and German VC market term sheet standards (Gesellschaftervereinbarung, Liquidationspräferenz, Verwässerungsschutz, Mitverkaufspflicht). Also triggers on: Wandeldarlehen valuation cap, Qualifizierter Rangrücktritt, GmbH capital increase, Gesellschafterliste, Handelsregister, DiRUG online GmbH formation, BAFA INVEST Zuschuss, Jahressteuergesetz 2024 equity reform, VSOP good/bad leaver BAG 2025 ruling, virtual options Lohnsteuer, phantom shares Germany, BaFin KAGB vs EuVECA, German down round anti-dilution, drag-along GmbH, UG haftungsbeschränkt Series A conversion, pre-money valuation cap Germany, GESSI bilingual convertible, INVEST Zuschuss angel tax-free. Germany-specific jurisdiction skill. Routes to deeper analysis modules for specific topics. Complements legalcode-de-gmbh-formation (formation) and legalcode-venture-financing-suite (cross-border router).


# Legalcode: German Venture Financing

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of German
> venture financing structures. It does not constitute legal advice (Rechtsberatung),
> tax advice (Steuerberatung), or investment advice. All outputs must be reviewed by a
> qualified _Rechtsanwalt_ (attorney) and _Steuerberater_ (tax advisor) licensed to
> practise German law before any reliance or action. Statutory references (GmbHG, BGB,
> EStG, KStG, GewO, KAGB), case law citations (BGH, BAG), regulatory guidance (BAFA,
> BaFin, BMF), and market practice benchmarks carry hallucination and currency risk —
> verify against authoritative sources (gesetze-im-internet.de, dejure.org, bafa.de,
> bafin.de) before relying on them. Nothing here constitutes an offer or solicitation to
> buy or sell securities or participation rights.

---

## Purpose and Scope

This skill analyses German venture financing decisions from pre-seed instrument selection
through to exit, covering the distinctive features of the German startup ecosystem that
differ from US, UK, or other common-law frameworks.

**Covers:**

- Instrument selection: Wandeldarlehen vs. direct equity round vs. GESSI standard forms
- Wandeldarlehen deep dive: valuation cap, discount, Rangrücktritt, conversion events
- GESSI (German Standards Setting Institute) bilingual standard document ecosystem
- GmbH vs. UG (haftungsbeschränkt) entity selection and startup structure
- Mandatory notarization: § 15 GmbHG share transfer requirements and DiRUG reform
- INVEST-Zuschuss: 15% acquisition grant and 25% exit grant via BAFA
- Founder liability: § 43 GmbHG business judgment rule, Vorgesellschaft, D&O
- VSOP vs. ESOP under German law: notarization cost drivers, § 19a EStG deferral,
  BAG March 2025 ruling on bad leaver clauses for vested options
- EuVECA passport: Regulation EU 345/2013, BaFin registration, KAGB comparison
- German term sheet standards: Liquidationspräferenz, Verwässerungsschutz,
  Mitverkaufspflicht, Erdienungsklausel, Gesellschaftervereinbarung

**Does not:**

- Provide legal advice or substitute qualified German counsel
- Cover AG (Aktiengesellschaft) structures or German-listed company rules
- Analyse cross-border flip-ups or Delaware C-Corp holding structures
  (see legalcode-venture-financing-suite for cross-border routing)
- Cover German M&A / Unternehmenskauf post-investment
- Constitute securities law advice under WpHG or Prospektpflicht analysis

**Complements:**

- `legalcode-de-gmbh-formation` — GmbH/UG formation workflow
- `legalcode-venture-financing-suite` — cross-border instrument router (US/UK/SG/IN)

---

## Jurisdiction and Governing Law

**Jurisdiction**: Federal Republic of Germany (Bundesrepublik Deutschland).

**Primary legal framework**:

- _GmbHG_ (Gesetz betreffend die Gesellschaften mit beschränkter Haftung) — GmbH
  company law; share structure, transfer formalities, managing director duties
- _BGB_ (Bürgerliches Gesetzbuch) §§ 488 et seq. — loan and Wandeldarlehen provisions
- _EStG_ (Einkommensteuergesetz) §§ 17, 19a, 20 — investor and employee tax treatment
- _KStG_ (Körperschaftsteuergesetz) § 8b — corporate participation exemption
- _KAGB_ (Kapitalanlagegesetzbuch) — German fund regulation; AIFMD implementation
- _EU Regulation 345/2013_ (EuVECA) — European venture capital fund passport
- _InsO_ (Insolvenzordnung) § 19 — over-indebtedness filing obligations
- _GNotKG_ (Gerichts- und Notarkostengesetz) — notary fee schedule

**Germany-specific practice notes**:

- Germany is a **civil law jurisdiction**. Contracts fill gaps in statutory provisions
  but cannot override mandatory _zwingendes Recht_ (mandatory law).
- GmbH shares (_Geschäftsanteile_) cannot be traded like corporate stock. Every transfer
  requires a notarial act under § 15 GmbHG — this shapes everything from bridge finance
  to employee equity design.
- German tax law distinguishes sharply between _Arbeitnehmereinkünfte_ (employment income,
  up to ~45% + solidarity surcharge) and _Veräußerungsgewinne_ (capital gains; § 17 EStG
  40% partial exemption for ≥1% holders). This gap drives VSOP vs. real equity choices.
- The **INVEST-Zuschuss** makes Germany one of the few jurisdictions with a federal
  tax-free grant specifically for angel investors — a material factor in deal structuring.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The answer would change the instrument recommendation or legal analysis
- Multiple valid structures exist and the user's risk appetite or stage matters
- Germany-specific compliance requirements depend on facts not yet provided
- A CLARIFY point requires a decision before the analysis can proceed

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

Accept the engagement in any of these formats:

- **Document**: Wandeldarlehen draft, term sheet, Gesellschaftervereinbarung, VSOP
  agreement, or other financing document (PDF/DOCX/pasted text)
- **Scenario description**: Factual scenario for instrument selection, INVEST eligibility,
  or VSOP structuring analysis
- **Question**: Specific German VC law question on any topic this skill covers

If no document or scenario is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user (skip items already answered by the input):

1. **Role and perspective**: Which party are you advising or representing?
   - Options: Founder/startup (company-side), Angel/seed investor, VC fund (institutional),
     Employee (equity plan analysis), Outside counsel reviewing on behalf of any party,
     Other
   - _Why this matters_: Analysis of term sheet provisions, INVEST eligibility, and VSOP
     design differs fundamentally depending on perspective.

2. **Stage and instrument**: What stage and financing instrument is involved?
   - Options: Pre-seed Wandeldarlehen / bridge, GESSI convertible, Seed equity round,
     Series A, Series B+, Employee equity plan (VSOP/ESOP), INVEST grant application,
     EuVECA fund structuring, Other
   - _Why this matters_: Drives which analytical modules to activate.

3. **Company structure**: Current or proposed entity type?
   - Options: UG (haftungsbeschränkt), GmbH, Planning to form GmbH, Planning to convert
     UG → GmbH, Other
   - _Why this matters_: UG constraints (§ 5a GmbHG profit retention) often require
     conversion before institutional investment.

4. **INVEST eligibility**: Is the INVEST-Zuschuss a relevant consideration?
   - Options: Yes — investor wants to apply / already applied, Yes — checking company
     eligibility, No, Not sure
   - _Why this matters_: INVEST compliance requirements affect deal structure (e.g.,
     minimum share acquisition, BAFA recognition procedure).

### Step 3: Load Jurisdiction-Relevant Legal Authority

Identify the correct German legal framework for the specific matter. Use **legalcode-mcp**
if connected to search for:

- Current text of GmbHG § 15 (share transfer formality) and § 43 (managing director duty)
- EStG § 17 and § 19a (current thresholds after Jahressteuergesetz 2024)
- Current BAFA INVEST-Zuschuss guidelines (effective March 6, 2024 through end-2026)
- BAG case law on bad leaver / vested option forfeiture (2025 ruling)
- BaFin guidance on EuVECA registration requirements

Save relevant results to `/tmp/legalcode-de-vc-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note: `legalcode_mcp: "Not connected"` in the Glass Box audit trail
- Proceed using the legal framework in this skill, flagging currency risk

### Step 4: Instrument Analysis Module

Perform analysis for the relevant instrument(s). Activate all applicable modules.

**⟁ CLARIFY** — For complex multi-instrument scenarios (e.g., Wandeldarlehen _plus_
an equity round _plus_ VSOP), confirm the priority order: "Which instrument or question
should I analyse first? I can address all of them but would like to sequence correctly."

---

## Module A: Instrument Selection — Wandeldarlehen vs. Direct Equity

### A1. Why Germany Uses Wandeldarlehen (Not SAFE)

The YC SAFE is not directly usable in German GmbH law. The structural impediments:

| Impediment           | German Law Reality                                                                                                                                                        | Practical Consequence                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Automatic conversion | Capital increase requires notarized shareholder resolution (§ 55 GmbHG) — cannot happen automatically                                                                     | Wandeldarlehen use a _Wandlungspflicht_ (conversion obligation) triggered by a qualifying event, executed via notarial act        |
| Interest-free loan   | German tax authority may treat interest-free loans as gifts, triggering _Schenkungssteuer_ (gift tax) at 5.5% p.a. deemed advantage                                       | Wandeldarlehen include contractual interest (typically 4–8% p.a.), often capitalized and added to conversion amount               |
| Preferred shares     | GmbH law does not recognize preferred share _classes_ in the US sense; investor economics are structured through _Sonderrechte_ in the shareholder agreement and articles | Conversion typically results in ordinary _Geschäftsanteile_ with investor protections layered in the _Gesellschaftervereinbarung_ |
| Registration         | GmbH share register (_Gesellschafterliste_) is public (§ 40 GmbHG)                                                                                                        | Each round requires updated _Gesellschafterliste_ filed with _Handelsregister_                                                    |

**Recommended instrument by stage:**

| Stage                       | Recommended Instrument                                      | Rationale                                                              |
| --------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------- |
| Pre-seed / friends & family | GESSI Wandeldarlehen                                        | Low cost, defers valuation, INVEST-compatible                          |
| Seed (€100k–€1M)            | GESSI Wandeldarlehen or direct equity if valuation is clear | GESSI standard widely accepted; direct equity if lead investor insists |
| Seed-to-A bridge            | Wandeldarlehen with qualified financing trigger             | Preserves flexibility; Rangrücktritt protects solvency filings         |
| Series A (€1M+)             | Direct equity round with full _Gesellschaftervereinbarung_  | Institutional VCs require GmbH structure and full governance package   |

### A2. GESSI Standard Documents

**GESSI** (German Standards Setting Institute / _Gesellschaft für Startup-Standardverträge_)
is a nonprofit founded in 2018 by BAND (Business Angels Deutschland) and Bundesverband
Deutsche Startups e.V. All documents are bilingual German/English and freely available at
**standardsinstitute.de** after registration.

**Published standard documents:**

| Document                              | Purpose                        | Key Features                                                                                                             |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **Wandeldarlehen** (convertible loan) | Pre-seed/seed bridge financing | 5-component package: usage instructions, shareholder resolution, loan agreement, conversion obligation, Excel calculator |
| **Term Sheet**                        | Equity round pre-documentation | Includes annexes and standard cap table (Excel)                                                                          |
| **Gesellschafterbeschluss**           | Shareholder resolutions        | Used alongside Wandeldarlehen and capital increases                                                                      |
| **VSOP Agreement**                    | Virtual stock option plan      | Standard employee equity structure                                                                                       |
| **Exit / SPA**                        | Share purchase on exit         | Standard exit with escrow provisions                                                                                     |
| **NDA**                               | Pre-deal confidentiality       | Bilingual standard form                                                                                                  |

> GESSI documents explicitly account for INVEST-Zuschuss eligibility conditions and have
> 180,000+ downloads with ~1,000 Wandeldarlehen used annually in the German market.
> Documents developed with participation from Orrick, YPOG, Taylor Wessing, and others.

---

## Module B: Wandeldarlehen Deep Dive

### B1. Key Economic Terms

**Bewertungsdach (Valuation Cap):**

- Sets the maximum _pre-money_ valuation at which the investor's loan converts to equity
- If the next round's pre-money valuation exceeds the cap, the investor converts as if the
  company were valued at the cap — yielding a lower conversion price and higher ownership
- Typical ranges: €2–10M for pre-seed; €5–20M for seed bridges
- **Drafting note**: Confirm whether the cap is _pre-money_ or _post-money_ — this
  ambiguity is a major source of dispute and cap table errors

**Abschlag (Discount Rate):**

- Investor converts at a percentage discount to the next-round share price
- Typical: 15–25% discount (e.g., discount of 20% → conversion price = 80% of new price)
- When both a cap _and_ a discount apply, the investor usually takes whichever is more
  favourable: `conversion_price = min(cap_price, (1 - discount) × round_price)`
- **⟁ CLARIFY** — Confirm which mechanism applies when both cap and discount trigger:
  "Lower of" (investor-favourable) vs. "only the cap applies" (more founder-favourable)?

**Zinsen (Interest Rate):**

- Statutory rate is 4% p.a. under BGB § 246 if no rate is specified
- Market rate: 0–8% p.a.; 5–6% p.a. is typical in GESSI standard
- Interest is usually accrued and added to the principal at conversion (capitalized), not
  paid in cash — preserving the company's cash position
- German tax: interest is deductible for the company (KStG § 4h subject to interest
  barrier rules); taxable as capital income for the investor (EStG § 20)

**Laufzeit / Long Stop Date (Maturity):**

- Typically 24–60 months; 36 months most common in GESSI standard
- At maturity without a conversion event: loan is repayable with accrued interest
- **Risk flag**: A short long-stop date (< 24 months) creates pressure on founders to
  raise a qualifying financing or repay — negotiate adequate runway

**Qualifiziertes Finanzierungsereignis (Qualified Financing):**

- The primary conversion trigger: a new equity round meeting a minimum investment
  threshold (typically €500k–€2M)
- Often also requires a minimum post-money valuation threshold
- Converts automatically upon closing of the qualifying round (via _Wandlungsobligation_)
- **⟁ CLARIFY** — Does the qualified financing definition exclude the existing Wandeldarlehen
  holder(s) from counting toward the minimum? This is a critical drafting point.

**Sonstige Wandlungsereignisse (Other Conversion Events):**

| Event                      | Mechanics                                                                                              | Investor Outcome               |
| -------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------ |
| IPO / Börsengang           | Converts to shares at IPO price less discount or cap (whichever favourable)                            | Liquid shares post-IPO lock-up |
| Exit / Unternehmensverkauf | Typically: investor chooses conversion (pro-rata share of proceeds) _or_ repayment of 1.5–2× principal | Cash premium for early risk    |
| Long-stop / Maturity       | Loan repayable; if company cannot repay, Rangrücktritt ranking controls                                | Creditor claim (subordinated)  |

### B2. Qualifizierter Rangrücktritt (Qualified Subordination)

This clause is **essential** in every Wandeldarlehen and distinguishes it from an
ordinary senior loan:

- **Effect**: The convertible lender agrees its claim ranks _after_ all unsubordinated
  creditors; the company does not need to repay the loan if doing so would cause or
  worsen over-indebtedness (_Überschuldung_) under InsO § 19
- **Insolvency benefit**: A Wandeldarlehen with a proper _Rangrücktritt_ does not count
  as a liability for the company's balance sheet solvency test — preventing a premature
  insolvency filing obligation (_Insolvenzantragspflicht_)
- **Drafting standard**: Must use the BGH-approved language from established case law
  (BGH II ZR 100/18 and predecessors [VERIFY]). GESSI standard form uses correct language.
- **RED flag**: Wandeldarlehen without a _Rangrücktritt_ may trigger _Überschuldung_
  even for a well-functioning startup if its nominal liabilities exceed assets on a
  balance-sheet basis

### B3. Wandeldarlehen Review Checklist

| Term                                                  | COMPLIANT | FLAG                    | RISK                                       | CRITICAL                                               |
| ----------------------------------------------------- | --------- | ----------------------- | ------------------------------------------ | ------------------------------------------------------ |
| Interest rate ≥ 0% and specified                      | ✓         | —                       | —                                          | Missing rate: BGB § 246 default applies; gift tax risk |
| Valuation cap defined (pre vs. post-money specified)  | ✓         | Ambiguous pre/post      | Cap unreasonably low for stage             | No cap: full dilution risk                             |
| Rangrücktritt clause present and BGH-compliant        | ✓         | Exists but non-standard | Partial subordination only                 | Missing: Überschuldung risk                            |
| Conversion obligation (_Wandlungsobligation_) present | ✓         | —                       | Conversion right only (company can refuse) | Missing: lender has no equity path                     |
| Qualified financing threshold defined                 | ✓         | Threshold ≤ €100k       | —                                          | No threshold: any financing converts                   |
| Maturity ≥ 24 months                                  | ✓         | 12–24 months            | < 12 months                                | At-will repayment                                      |
| Exit conversion or repayment mechanics defined        | ✓         | Ambiguous               | Missing exit mechanics                     | No exit provision                                      |
| Notarization of conversion obligation                 | ✓         | —                       | —                                          | Missing: conversion void under § 15 GmbHG              |

---

## Module C: GmbH/UG Structure for Startups

### C1. Entity Selection

| Criterion              | UG (haftungsbeschränkt)                                                                          | GmbH                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------- |
| **Statutory basis**    | GmbHG § 5a                                                                                       | GmbHG §§ 1–88                           |
| **Min. share capital** | €1 (practical minimum €500–€5,000)                                                               | €25,000                                 |
| **Capital payment**    | 100% cash before registration                                                                    | ≥ 50% (min €12,500) before registration |
| **Profit retention**   | 25% of annual net profit until share capital reaches €25,000 (§ 5a(3))                           | None                                    |
| **Designation**        | Must use "UG (haftungsbeschränkt)" — abbreviation "UG" or "GmbH" not permitted                   | Can use "GmbH"                          |
| **VC acceptability**   | Usually not accepted for Series A; most VCs require GmbH conversion                              | Standard institutional vehicle          |
| **Conversion**         | Can convert to GmbH once accumulated share capital (including retained earnings) reaches €25,000 | N/A                                     |
| **Online formation**   | Yes — DiRUG video notarization available since Aug 2022 (cash contributions only)                | Yes — same conditions                   |

**Recommendation matrix:**

| Scenario                           | Recommendation                                    |
| ---------------------------------- | ------------------------------------------------- |
| Bootstrapped / pre-idea            | UG — lowest entry cost                            |
| Pre-seed with INVEST-seeking angel | GmbH or UG (INVEST eligible for both)             |
| Seed round with institutional lead | GmbH required — convert UG if needed              |
| International co-founders (non-EU) | GmbH preferred — UG creates additional complexity |

### C2. GmbH Share Structure

- Shares are _Geschäftsanteile_ (business interests) denominated in whole euros (e.g., a
  GmbH with €25,000 share capital might have 25,000 shares of €1 each)
- Each _Geschäftsanteil_ carries equal rights unless the _Gesellschaftsvertrag_ provides
  for differentiated rights (_Sonderrechte_)
- **Multiple Geschäftsanteile per shareholder**: Legally possible; each tranche can have
  different rights (e.g., vesting schedule, leaver mechanics) if structured in articles
  or shareholder agreement
- **Investor preference**: Cannot create US-style preferred share _classes_ by default;
  investor protections (liquidation preference, anti-dilution) are implemented via the
  _Gesellschaftervereinbarung_ (contractual rights) and/or amended _Gesellschaftsvertrag_

### C3. Gesellschafterliste (Shareholder Register)

- Mandatory public filing with _Handelsregister_ under GmbHG § 40
- Lists every shareholder, their _Geschäftsanteil_ number, and percentage
- Must be updated within one month of each share transfer or capital change
- **Good faith purchaser protection**: A bona-fide purchaser who relies on the register
  and takes for value can acquire valid title even from a non-owner (§ 16(3) GmbHG)
- **Practice**: Every Wandeldarlehen conversion or round must include a notarized share
  transfer and updated _Gesellschafterliste_ filing

---

## Module D: Notarization (§ 15 GmbHG)

### D1. Mandatory Notarization Requirements

**Scope of notarization obligation (§ 15(3)-(4) GmbHG):**

| Transaction                                                | Notarization Required?                                    |
| ---------------------------------------------------------- | --------------------------------------------------------- |
| Transfer of Geschäftsanteil (share sale)                   | **Yes** — notarial deed required                          |
| Obligation to transfer (Verpflichtung zur Abtretung)       | **Yes** — notarial form required                          |
| Capital increase with new shares                           | **Yes** — shareholder resolution + subscription notarized |
| Option agreement granting right to acquire Geschäftsanteil | **Contested** [VERIFY] — best practice: notarize          |
| VSOP (purely contractual phantom shares)                   | **No** — contractual only; no real share transfer         |
| Formation (Gründung)                                       | **Yes** — Gesellschaftsvertrag notarized                  |
| Amendments to Gesellschaftsvertrag                         | **Yes** — majority shareholder resolution notarized       |

**Effect of missing notarization:**

- Agreement is **void** (_nichtig_) under § 15(4) GmbHG
- The void agreement is _cured_ only when the actual notarized transfer under § 15(3)
  is executed — meaning the obligation becomes enforceable only at the point of transfer
- **Practical trap**: Options or pre-emptive right agreements that are not notarized may
  be unenforceable — investors have lost rights in contested cases [VERIFY BGH case law]

### D2. Cost and Timeline

**Cost (GNotKG-based, indicative):**

| Transaction Value                      | Estimated Notary Fee |
| -------------------------------------- | -------------------- |
| €25,000 (GmbH formation)               | ~€300–500            |
| €500,000 (seed round capital increase) | ~€1,200–1,800        |
| €2M (Series A capital increase)        | ~€2,500–4,000        |
| €10M (later stage)                     | ~€6,000–9,000        |

_Note: +30% surcharge for foreign-language documents; +30% for choice-of-law clauses
that are not purely declaratory. Fees are for the notarization itself; KYC and ancillary
legal fees are separate._

**Timeline (typical):**

- Standard formation or transfer: 2–4 weeks (includes AML/KYC per German Anti-Money
  Laundering Act requirements in force since January 1, 2020)
- Complex cross-border transactions: 4–8 weeks (apostille, foreign notary recognition)

### D3. DiRUG Reform (Online Notarization)

**Current status (as of 2025):**

- **GmbH/UG formation**: Online via video notarization permitted since August 1, 2022
  (cash contributions only; no in-kind contributions)
- **Shareholder resolutions (unanimous)**: Online notarization permitted since August 1,
  2023 (DiREG expansion)
- **Capital increases**: Partially online; subject to limitations
- **Share transfers (§ 15 GmbHG)**: Online notarization **not yet** available — still
  requires physical or proxy attendance [VERIFY 2025 status — planned expansion under
  evaluation since August 1, 2024]

**International founders:**

- Can use video notarization for formation if using German notary system
- Requires valid EU eID or qualified video identification
- For non-EU founders: physical attendance or power of attorney (apostilled) still the
  safest path for complex transactions

---

## Module E: INVEST-Zuschuss (Federal Angel Grant)

### E1. Program Overview

The **INVEST-Zuschuss** is a federal grant administered by BAFA (_Bundesamt für
Wirtschaft und Ausfuhrkontrolle_). It provides **tax-free subsidies** to angel investors
in innovative German startups. Current program guideline: effective **March 6, 2024**
through **December 31, 2026**.

### E2. Grant Structure

| Grant Type                              | Rate                     | Mechanics                                                                 |
| --------------------------------------- | ------------------------ | ------------------------------------------------------------------------- |
| **Erwerbszuschuss** (Acquisition grant) | **15%** of investment    | Paid to investor tax-free at purchase; triggers 3-year holding obligation |
| **Exitzuschuss** (Exit grant)           | **25%** of net exit gain | Lump-sum compensation for disposal gains; no minimum gain below €2,000    |

**Investment limits (per investor per year):**

- Acquisition grant: max **€100,000** total per investor per year
- Maximum subsidized investment per transaction: ~€333,333 (to yield the €50,000 per-
  transaction maximum [VERIFY current per-transaction cap with BAFA])
- **3-year minimum holding period** (_Haltefrist_) post-acquisition before exit grant
  becomes available

### E3. Investor Eligibility

**Individual investors (most common path):**

- Natural person (_natürliche Person_)
- Principal residence within the **EEA** (EU + Iceland, Liechtenstein, Norway)
- **Independent from the company**: No prior managerial control, no connected-party status
- Must acquire _new_ shares (_Neuanteile_) — grant does not apply to secondary purchases

**Corporate investor vehicle:**

- GmbH or UG with maximum **6 natural person shareholders**, all EEA-resident
- None of the natural persons may hold >50% in the company being invested in
- All natural person shareholders must jointly apply

### E4. Portfolio Company Eligibility

| Criterion                  | Requirement                                                                                                                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Age**                    | Not older than **7 years** from founding                                                                                                                                                            |
| **Size**                   | < 50 full-time employees; annual turnover or balance sheet ≤ €10M                                                                                                                                   |
| **Location**               | Head office in EEA; **at least one branch registered in Germany**                                                                                                                                   |
| **Listing**                | Not listed on regulated market                                                                                                                                                                      |
| **Innovation**             | Must satisfy at least one of: operates in innovative sector, holds patent, received public R&D funding in prior 2 years, received innovation award, or independent expert opinion on innovativeness |
| **Active operations**      | Economically active at application or commences within 1 year of investment                                                                                                                         |
| **Minimum equity capital** | ≥ €12,500 (practical: properly capitalised GmbH)                                                                                                                                                    |

**BAFA recognition process:**

1. Company applies to BAFA for recognition as eligible (_förderfähiges Unternehmen_)
2. BAFA reviews innovation criteria (typically 2–4 weeks)
3. Upon recognition, company issues BAFA certificate to investor
4. Investor submits acquisition grant application to BAFA within 3 months of share purchase
5. BAFA processes application; grant paid directly to investor

**GESSI Wandeldarlehen note:** GESSI standard documents are designed to be INVEST-compatible.
Verify that any custom Wandeldarlehen also meets INVEST conditions (particularly: shares
must be acquired for cash consideration, not debt-for-equity conversion without fresh
capital [VERIFY current BAFA interpretation]).

### E5. INVEST Deal Structure Checklist

- [ ] Company has applied for and received BAFA recognition certificate
- [ ] Investor is an EEA-resident natural person (or qualifying GmbH vehicle)
- [ ] Investment is for _new_ shares (primary issuance, not secondary)
- [ ] Minimum investment amount: €10,000
- [ ] Holding period commitment: investor will not transfer shares for ≥ 3 years
- [ ] No connected-party relationship between investor and company founders
- [ ] Acquisition grant application submitted to BAFA within 3 months of share purchase
- [ ] Exit grant planned: ensure disposal is structured as taxable event to claim 25%
      compensation [VERIFY interaction with § 17 EStG partial exemption — only one
      benefit applies; professional tax advice required]

---

## Module F: Founder Liability

### F1. Managing Director Duty of Care (§ 43 GmbHG)

The _Geschäftsführer_ (managing director) owes the GmbH the care of an "orderly
businessman" (_Sorgfalt eines ordentlichen Geschäftsmannes_) under § 43(1) GmbHG:

**Key duties:**

- File insolvency within maximum **6 weeks** of becoming aware of _Zahlungsunfähigkeit_
  (illiquidity) or within **3 weeks** for _Überschuldung_ (over-indebtedness) — post-2021
  reform [VERIFY current deadlines after COVID temporary suspension expiry]
- Remit withheld wage taxes (_Lohnsteuer_) and social security contributions (_SV-Beiträge_)
  promptly — personal liability persists in insolvency
- Maintain proper books and prepare annual financial statements
- Refrain from competing with the company or taking corporate opportunities
- Observe capital maintenance rules: no payments to shareholders that deplete the
  registered share capital below €25,000 (§ 30 GmbHG)

**Liability mechanism:**

- § 43(2): Breach of duty → personal liability to the **company** for resulting damage
- Limitation period: **5 years** from breach (§ 43(4) GmbHG)
- In insolvency: insolvency administrator (_Insolvenzverwalter_) may pursue these claims
- Shareholder waiver of § 43 claims: possible but must be explicit; cannot waive in
  advance for unknown claims [VERIFY]

**Business judgment rule (German analogy):**

- German courts apply a functional equivalent: Geschäftsführer who makes informed
  business decisions in good faith, without personal interest, on adequate information
  basis are protected from liability for mere business failures
- BGH case law has developed this protection analogous to the US business judgment rule
  [VERIFY specific BGH cases]

### F2. Pre-Incorporation Liability (Vorgesellschaft)

**Phase 1 — Before notarization (_Vorgründungsgesellschaft_):**

- Partnership (_GbR_) under BGB §§ 705 et seq.
- All founding partners: **unlimited joint and several liability** for obligations incurred

**Phase 2 — After notarization, before _Handelsregister_ entry (_GmbH in Gründung / GmbH i.G._):**

- Company has partial legal capacity (_Teilrechtsfähigkeit_)
- _Handelndenhaftung_: Persons acting on behalf of the GmbH i.G. remain personally liable
  for all obligations until registration
- Upon registration: personal liability extinguished (founders released); company assumes
  liabilities and assets automatically (_Identitätsprinzip_)
- **Practical advice**: Avoid significant obligations before registration; use separate
  payment arrangement or shareholder advance account for pre-registration expenses

### F3. D&O Insurance (Vermögensschadenhaftpflichtversicherung)

- Covers personal liability of Geschäftsführer for breach of § 43 GmbHG duties
- Increasingly required by institutional VCs as a closing condition in Series A
- Typical policy limits: €1M–€5M for seed/Series A; €5M–€25M for later stages
- Key exclusions to review: fraud/intentional misconduct (_Vorsatz_), criminal conduct,
  known violations pre-policy
- **⟁ CLARIFY**: Has the company obtained D&O coverage? What is the limit? Are investor
  board observers covered?

---

## Module G: VSOP, ESOP, and § 19a EStG

### G1. Why VSOPs Dominate German Startup Equity Plans

| Factor                     | Real Shares (ESOP / Geschäftsanteile)                                        | VSOPs (Phantom Shares)                                                                   |
| -------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Notarization**           | Every grant requires notarial act (§ 15 GmbHG)                               | None — purely contractual                                                                |
| **Cost per grant**         | €500–€2,000+ per employee                                                    | €100–€500 per employee                                                                   |
| **Shareholder resolution** | Capital increase resolution required                                         | Not required                                                                             |
| **Handelsregister update** | Required after each grant                                                    | Not required                                                                             |
| **Voting rights**          | Full voting rights (unless restricted in articles)                           | None                                                                                     |
| **Tax treatment**          | § 19a EStG deferral possible; § 17 EStG capital gains on exit (if ≥1% stake) | Wage income (Lohnsteuer) at exit; no capital gains treatment unless structured carefully |
| **Timeline**               | 2–4 weeks per grant cycle                                                    | 1–2 business days                                                                        |

**Conclusion**: VSOPs are standard for pre-IPO German startups. Real share options are
reserved for co-founders, key executives receiving material stakes, or cases where
§ 19a EStG deferral is specifically optimized.

### G2. VSOP Mechanics

**Core structure:**

- Employee receives a contractual right (_schuldrechtlicher Anspruch_) to a cash payment
  upon a _liquidity event_ (exit, IPO, secondary sale, or sometimes a deemed liquidity event)
- Payment = (Exit Valuation × Virtual Share Percentage) − Baseline Price (strike price)
- Baseline price typically set at the FMV of the company at time of grant (to limit
  speculative elements and gift tax risk)
- **No actual Geschäftsanteil changes hands**: VSOP payout is a contractual debt of the
  company at exit

**Standard vesting schedule (market standard):**

- **Total vesting period**: 4 years
- **Cliff**: 12 months (0% vested before cliff)
- **Post-cliff**: 25% vests at cliff anniversary, then 2.0833% per month (monthly
  vesting) or 6.25% per quarter
- **Full vesting**: After 48 months from grant date

**Leaver provisions:**

| Leaver Type     | Typical Trigger                                                                      | VSOP Treatment                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Good leaver** | Company-initiated termination without cause, disability, death, permanent incapacity | Vested options retained; payout at liquidity event                                                                                  |
| **Bad leaver**  | Voluntary resignation, termination for cause, non-compete breach, serious misconduct | Post-2025: only _unvested_ options can be forfeited or bought back at nominal value; _vested_ options may not be forfeited [see G3] |
| **Grey leaver** | Early voluntary exit with company consent (some plans)                               | Vested portion retained; unvested forfeited                                                                                         |

### G3. BAG March 2025 Ruling — Critical Development

**Bundesarbeitsgericht (BAG) ruling, March 19, 2025 [VERIFY exact citation]:**

The BAG held that bad leaver clauses which cause **forfeiture of vested VSOP options**
are potentially invalid as _unangemessene Benachteiligung_ (unreasonable disadvantage)
under BGB § 307, when the vested options constitute a _Vergütungsbestandteil_
(remuneration component) earned by performance of work.

**Practical implications:**

- Plans should no longer provide that _all_ options (vested and unvested) are forfeited
  at nominal value upon bad leaver event
- **Restructuring required**: Bad leaver provisions should distinguish between:
  - _Unvested_ options: may still be forfeited / bought back at nominal value upon bad leaver
  - _Vested_ options: buyback at fair market value or on exit terms — nominal-value
    forfeiture is now HIGH RISK of being invalid
- **Transition plans in place before 2025**: Review and amend to avoid exposure to
  employee claims for vested option value
- **GESSI and YPOG** have issued updated guidance on restructuring leaver mechanics
  [VERIFY current GESSI/YPOG position]

> **ACTION REQUIRED**: Any VSOP plan with a nominal-value forfeiture clause for vested
> options should be reviewed by German employment and corporate counsel immediately.

### G4. § 19a EStG — Employee Equity Tax Deferral

**Statute**: § 19a EStG (Einkommensteuergesetz), as amended by _Jahressteuergesetz 2024_
(effective December 2, 2024).

**Effect**: Defers the wage-tax event on equity participation from the time of grant/vest
to the _earlier of_: (a) sale of the equity, (b) 15 years after transfer of the
participation, or (c) employment termination _if employer assumes the tax liability_.

**Company eligibility thresholds (post-JStG 2024):**

| Criterion                       | Threshold                                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Company age                     | ≤ **20 years** from founding (previously 12 years)                                                                      |
| Employee count                  | ≤ **1,000** (previously 250)                                                                                            |
| Annual turnover                 | ≤ **€100M** (previously €50M)                                                                                           |
| Annual balance sheet            | ≤ **€86M** (previously €43M)                                                                                            |
| Group company clause (NEW 2024) | Can grant interests in affiliated group companies if no group company exceeds 20 years and group SME thresholds are met |

**Annual tax-free allowance (post-JStG 2024):** **€2,000** per employee per year
(previously €1,440; proposed €5,000 was not adopted).

**Deferral period extension**: Extended from 12 to **15 years** under 2024 reforms.
Applies retroactively to participations already transferred before 2024.

**Key conditions:**

- Plan must be offered to all employees employed ≥ 1 year (all-employee requirement
  for the tax-free allowance portion)
- Participation must be in the **employing company** or a group affiliate (post-2024)
- Employee's tax at deferred exit is on the value at time of liquidity event — meaning
  no benefit from capital gains rate; still taxed as income (_Lohnsteuer_)

**VSOP interaction:**

- § 19a applies to _direct equity_ (real share transfers) more cleanly
- For VSOPs: deferral can apply but plan must be carefully structured as a qualifying
  _Mitarbeiterbeteiligung_ — standard VSOP with cash settlement may not qualify
  automatically [VERIFY current BMF guidance]
- **Dry income problem**: § 19a deferral specifically addresses the "dry income" problem
  where a vesting event creates taxable income without liquid funds; 2024 reforms
  expanded the deferral to reduce this risk materially

**⟁ CLARIFY** — For VSOP/equity plan analysis: "What is the founding date of the company?
This determines § 19a eligibility (≤ 20 years). Has the company obtained a tax ruling
(_verbindliche Auskunft_) from the _Finanzamt_ on § 19a treatment of its plan?"

### G5. EIP (Equity Incentive Plan) — Evolution Beyond VSOP

Some German startups and their advisors (particularly Gaia Law, YPOG) are moving toward
_Equity Incentive Plans (EIPs)_ that qualify under § 19a EStG while providing closer-to-
equity economics than traditional VSOPs:

- Structures using _Genussrechte_ (profit participation certificates) or _stille
  Beteiligung_ (silent partnership interests) that qualify as capital instruments
- Provides potential capital gains treatment (_§ 17 EStG_) at exit if structured correctly
- Significant complexity and legal cost vs. VSOPs — typically only for material grants
- **⟁ CLARIFY** — For significant equity grants (>1% diluted): "Should I analyse an EIP
  structure that may qualify for § 17 EStG capital gains treatment alongside the standard
  VSOP approach?"

---

## Module H: EuVECA Passport

### H1. What EuVECA Provides

**EuVECA** (European Venture Capital Funds, Regulation EU 345/2013) creates a voluntary
EU-wide passport for smaller VC fund managers:

| Feature                | EuVECA                                                | Full KAGB (AIFM) Authorization                            |
| ---------------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| **Authorization body** | BaFin registration (simplified)                       | BaFin full KVG authorization                              |
| **Threshold**          | For managers with AUM < €500M (AIFMD threshold)       | AIFMD: AUM ≥ €500M (or leveraged ≥ €100M)                 |
| **EU passport**        | Yes — market in all EU member states                  | Yes (full AIFMD passport)                                 |
| **Depositary**         | Not required (custodian may be used)                  | AIFMD-compliant depositary required                       |
| **Prospectus**         | Not required — confidential investor document         | KAGB prospectus requirements apply                        |
| **Leverage**           | Prohibited                                            | Permitted (subject to limits)                             |
| **Investor type**      | Professional investors only (MiFID II classification) | Professional investors; retail if specific conditions met |

### H2. Qualifying Portfolio Companies

A EuVECA fund must invest ≥ 70% of its capital in _qualifying portfolio companies_:

| Criterion                 | Requirement                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Listing status**        | Not admitted to trading on a regulated market                                                                          |
| **Size**                  | Qualifies as an SME (< 250 employees; turnover ≤ €50M or balance sheet ≤ €43M)                                         |
| **Type**                  | Legal person (i.e., includes GmbH/UG)                                                                                  |
| **Financing**             | Equity or quasi-equity; convertibles and participating loans permitted                                                 |
| **No financial services** | Cannot be a credit institution, investment firm, insurance undertaking, or holding company of financial services group |

### H3. EuVECA vs. KAGB for German VC Funds

**When EuVECA is preferred:**

- Fund manager AUM < €500M
- Focus on early-stage German and European startups
- Want simplified compliance infrastructure
- Do not require leverage
- Target sophisticated (professional) investors only

**When full KAGB is preferred:**

- AUM > €500M (mandatory)
- Fund requires leverage or complex derivative strategies
- Retail investor access required
- Fund structures requiring AIFMD-compliant depositary relationship (e.g., pension fund LPs)

**German VC fund structure:**

- Typical German VC fund: **GmbH & Co. KG** (limited partnership with GmbH GP)
- Tax transparent for German and international investors
- GP (_Komplementär_): GmbH; LPs (_Kommanditisten_): investors
- Management company (_KVG_) may be separate entity

### H4. AIFMD 2024 Changes Affecting German VCs [VERIFY current status]

- Enhanced sustainability (_SFDR_) reporting requirements for EuVECA funds
- Due diligence on ESG factors for qualifying portfolio companies
- Potential restrictions on SPACs and tokenized fund interests under evaluation
- Compressed annual reporting timelines to BaFin

---

## Module I: German Term Sheet Standards

### I1. Liquidationspräferenz (Liquidation Preference)

| Type                     | Mechanics                                                                                                        | German Market Status                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **1x non-participating** | Investor receives 1× investment back before any distribution to founders; then participates pro-rata with common | Market standard (96%+ of deals, per 2024 data)                       |
| **1x participating**     | Investor receives 1× investment _plus_ pro-rata participation with common shareholders                           | Less common; used in distress/down rounds or high-leverage positions |
| **Multiple (1.5x, 2x)**  | Investor receives 1.5–2× before any distribution to common                                                       | Rare; red flag in normal market conditions                           |

**Trigger events:**

- _Unternehmensverkauf_ (acquisition of >50% of shares or assets)
- _Liquidation_ (dissolution and winding up)
- _IPO_: liquidation preference typically lapses upon IPO as shares convert

**German structuring note**: Since GmbH law does not have preferred share classes, the
liquidation preference is implemented via the _Gesellschaftervereinbarung_ and/or
_Gesellschaftsvertrag_ _Sonderrechte_ — a contractual waterfall obligation on all
shareholders to distribute exit proceeds in the agreed priority order.

### I2. Verwässerungsschutz (Anti-Dilution)

| Mechanism                               | Calculation                                                                                                                                                                        | German Market                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Broad-based weighted average (BBWA)** | New conversion price = (old price × all outstanding shares + new price × new shares) ÷ (all outstanding + new shares). Broadest base → smallest adjustment → most founder-friendly | **Market standard** in German VC     |
| **Narrow-based weighted average**       | Same formula but base includes only ordinary/common shares                                                                                                                         | Less common                          |
| **Full ratchet**                        | Investor's price resets to the down-round price → maximum dilution to founders                                                                                                     | Rare; used only in distressed recaps |

**Carve-outs (standard exclusions from anti-dilution triggers):**

- Employee option pool grants (VSOP/ESOP)
- Stock splits / share reclassifications
- Pro-rata rights exercise by existing investors
- Certain strategic issuances approved by investor consent threshold

### I3. Mitverkaufspflicht / Drag-Along (Forced Sale Rights)

- Allows a qualifying majority (investor alone, or investor + majority founders) to
  force all other shareholders to sell their _Geschäftsanteile_ on the same economic terms
- Implemented via _Gesellschaftervereinbarung_ — not a statutory right in GmbH law
- **Typical threshold**: 50–75% of all shares (by value), including investor consent
- **Key safeguards** for minority protection:
  - Drag cannot be used to sell to a _connected party_ of the majority at below-FMV
  - All shareholders receive the same per-share consideration (_pari passu_ economics)
  - Tag-along rights of minority shareholders are preserved (they can participate in the
    same sale terms rather than being dragged)
- **⟁ CLARIFY** — Does the drag-along allow the investor to force a sale at any price,
  or only at or above a minimum return threshold (e.g., 1× invested capital)? This is
  a key founder protection point.

### I4. Mitverkaufsrecht / Tag-Along (Co-Sale Rights)

- Minority shareholders (founders, angels) can elect to sell their _Geschäftsanteile_
  alongside a major shareholder's sale on the same terms
- **Typical trigger**: Any sale of >10–20% of all shares by a single shareholder
- **Pro-rata mechanics**: Each tag-along holder can sell their pro-rata proportion of
  the buyer's total acquisition
- Prevents founders from being excluded from a lucrative exit
- **German market practice**: Tag-along rights are broadly applied — often extended to
  all shareholders, not just investors

### I5. Erdienungsklausel / Vesting for Founders

**Standard market vesting in German VC deals:**

| Parameter                     | Standard                                                             |
| ----------------------------- | -------------------------------------------------------------------- |
| Total period                  | **4 years**                                                          |
| Cliff                         | **12 months** (0% before cliff)                                      |
| Post-cliff                    | 25% at cliff, then monthly (~2.08%/month)                            |
| Acceleration — single trigger | 25–50% on change of control                                          |
| Acceleration — double trigger | 100% on change of control + involuntary termination within 12 months |

**Good/Bad Leaver treatment for founders (shares, not VSOPs):**

| Scenario                                | Typical Treatment                                                     |
| --------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Good leaver                             | Vested shares retained; unvested shares bought back at FMV or nominal |
| Bad leaver                              | Unvested shares: nominal value buyback                                | Vested shares (post-BAG 2025): FMV buyback required for proportionate portion |
| Involuntary good leaver (illness, etc.) | All shares (vested + unvested) retained at FMV                        |

**Post-BAG 2025 rule**: Apply the BAG vested-option ruling also to founder share vesting
where founders are simultaneously employees/service providers — nominal-value forfeiture
of **vested** shares may be unenforceable as a _unangemessene Benachteiligung_ [VERIFY
specific application to founder shares vs. employee VSOPs].

### I6. Gesellschaftervereinbarung (Shareholder Agreement) Structure

**Mandatory topics in a German VC shareholder agreement:**

| Topic                           | Key Provisions                                                                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Governance**                  | Geschäftsführer appointment/removal rights; investor board/advisory board seats; managing director service contract terms                          |
| **Investor consent thresholds** | Reserved matters requiring investor approval (capital increases, major asset disposals, related-party transactions, new debt, salary changes, M&A) |
| **Anti-dilution**               | BBWA calculation; trigger events; carve-outs                                                                                                       |
| **Liquidation preference**      | Waterfall; trigger events; participating vs. non-participating                                                                                     |
| **Drag-along**                  | Trigger threshold; protections; mechanics                                                                                                          |
| **Tag-along**                   | Threshold; pro-rata calculation; deadline                                                                                                          |
| **Vesting / leaver**            | Schedule; good/bad leaver definitions; buyback mechanics and price                                                                                 |
| **Pre-emptive rights**          | Right of first refusal (Vorkaufsrecht) on secondary transfers                                                                                      |
| **Information rights**          | Quarterly unaudited financials; annual audited financials; budget; cap table updates                                                               |
| **Non-compete / non-solicit**   | Founder post-departure restrictions [VERIFY German enforceability limits]                                                                          |
| **Exit**                        | Forced sale mechanics; IPO cooperation obligations; drag-along                                                                                     |
| **Amendments**                  | Threshold (100% consent or 75%+ supermajority)                                                                                                     |

**Notarization of Gesellschaftervereinbarung**: **Not required** — it is purely
contractual (_schuldrechtlich_), not an amendment to the _Gesellschaftsvertrag_. However,
if any provision effectively creates new share rights or alters the _Gesellschaftsvertrag_,
notarization may be required.

---

## Severity Classification

Apply this four-tier classification to all findings:

| Tier | Label         | Definition                                                                                             | Required Action                          |
| ---- | ------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| ✅   | **COMPLIANT** | Term or structure meets German legal requirements and market standard                                  | No action required; note for record      |
| 🟡   | **FLAG**      | Term deviates from market standard or contains ambiguity but is not immediately harmful                | Recommend negotiation or clarification   |
| 🔴   | **RISK**      | Term creates material legal risk, tax exposure, or enforceability concern                              | Recommend amendment; escalate to counsel |
| ⛔   | **CRITICAL**  | Term is void or unenforceable under German law, creates insolvency risk, or violates mandatory statute | Mandatory remediation before proceeding  |

**CRITICAL auto-triggers** (escalate immediately regardless of context):

- Wandeldarlehen missing _Qualifizierter Rangrücktritt_ → **over-indebtedness risk**
- VSOP or option agreement not notarized where notarization is required under § 15 GmbHG
- Share transfer agreement not notarized → **void** under § 15(4) GmbHG
- Bad leaver clause with nominal-value forfeiture of _vested_ options (post-BAG 2025)
- INVEST grant application filed after 3-month deadline (right lost)
- Missing insolvency filing when _Insolvenzantragspflicht_ triggers (personal liability)

---

## Actionable Output Per Finding

For every **FLAG**, **RISK**, or **CRITICAL** finding, provide:

1. **What was found**: Exact provision or missing element
2. **Why it matters**: Legal basis (statute, case law, regulatory guidance)
3. **Severity**: FLAG / RISK / CRITICAL with rationale
4. **Recommended action**: Specific redline language, structural change, or process step
5. **Fallback position**: If the preferred fix cannot be agreed, the next-best acceptable
   position
6. **Deadline**: Any time-sensitive elements (e.g., INVEST grant 3-month window)

---

## Prioritization Framework

| Priority            | Tier                | When to Act                                              |
| ------------------- | ------------------- | -------------------------------------------------------- |
| **P1 — Immediate**  | CRITICAL            | Before execution; do not proceed without fix             |
| **P2 — Pre-Close**  | RISK                | Resolve before signing; obtainable in normal negotiation |
| **P3 — Post-Close** | FLAG                | Address within 30–90 days; manageable risk in interim    |
| **P4 — Awareness**  | COMPLIANT with note | Monitor; no action currently needed                      |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering output. Revise any failures before delivery.

| Gate           | Rule                                                                                                                | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every statutory claim cites a specific GmbHG section, BGB provision, EStG paragraph, or named case                  | Add citation or mark [UNVERIFIED]   |
| **Format**     | Citations follow German legal citation format (e.g., "§ 15 Abs. 3 GmbHG", "BGH II ZR 100/18")                       | Fix format                          |
| **Currency**   | Verify provisions against JStG 2024 changes (§ 19a EStG, § 3 Nr. 39 EStG) and post-2025 BAG ruling                  | Flag [CHECK CURRENCY]               |
| **Domain**     | Analysis applies German law only; no US/UK law stated as universal without [VERIFY]                                 | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; no false precision on unsettled questions (EIP tax treatment, BAG application scope) | Add confidence qualifier            |

### Self-Interrogation for CRITICAL Items

For every **CRITICAL** finding, apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the CRITICAL classification follow logically
from the cited statutory provision? Would a German court or BaFin/BAFA actually reach
this conclusion on these facts?

**Pass 2 — Completeness**: Have all potentially relevant German statutes, regulations
(GmbHG, BGB, EStG, InsO, KAGB), and case law (BGH, BAG, BFH) been considered?
Are there regulatory dimensions (BAFA, BaFin, Finanzamt _verbindliche Auskunft_) not
yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this term or structure is
_not_ CRITICAL? Under what circumstances might a reasonable German lawyer accept the
risk? If a qualified _Rechtsanwalt_ could credibly argue the other side, downgrade to
RISK and explain the disagreement.

### Confidence Scoring

| Level        | Range     | Meaning                                                        | Action                                     |
| ------------ | --------- | -------------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled German law; clear statute; unambiguous BGH case        | State with confidence                      |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions remain          | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good arguments; some doctrinal uncertainty                     | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., BAG ruling application to founders) | Flag for specialist review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                        | Do not assert; flag [UNCERTAIN]            |

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-venture-financing-de"
  version: "1.0.0"
  date: "[YYYY-MM-DD]"
  jurisdiction: "Germany (federal); GmbHG, BGB, EStG, KStG, KAGB, EU Reg 345/2013"
  matter_type: "[Wandeldarlehen / INVEST / VSOP / Term Sheet / EuVECA / General]"
  stage: "[Pre-seed / Seed / Series A / Series B+ / Employee equity / Fund]"
  party_perspective: "[Founder / Investor / Fund / Employee / Counsel]"
  legalcode_mcp: "[Connected — N citations verified / Not connected — manual verification required]"
  key_statutes_applied:
    - "[GmbHG § 15 — share transfer formality]"
    - "[GmbHG § 43 — managing director duty of care]"
    - "[BGB § 488 et seq. — loan provisions]"
    - "[EStG § 17 — capital gains on substantial shareholding]"
    - "[EStG § 19a — employee equity tax deferral (post-JStG 2024)]"
    - "[InsO § 19 — over-indebtedness]"
    - "[EU Reg 345/2013 — EuVECA]"
  key_case_law_applied:
    - "[BGH II ZR 100/18 — Rangrücktritt language [VERIFY]]"
    - "[BAG March 19, 2025 — bad leaver vested options [VERIFY citation]]"
  findings_summary:
    critical: "[N]"
    risk: "[N]"
    flag: "[N]"
    compliant: "[N]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, BAFA program currency caveats, BAG ruling application uncertainty]"
    - "All statutory references carry hallucination risk — verify at gesetze-im-internet.de"
    - "INVEST program expires Dec 31, 2026 unless renewed — verify current status with BAFA"
  reviewer: "AI-assisted analysis — requires review by German Rechtsanwalt and Steuerberater"
```

---

## Anti-Patterns

What NOT to do in German venture financing:

1. **Using a SAFE without adaptation**: A YC-standard SAFE is not directly enforceable
   in German GmbH law. The automatic conversion mechanics and preferred share structure
   require German law adaptation. Use GESSI Wandeldarlehen instead.

2. **Omitting the Rangrücktritt from a Wandeldarlehen**: A convertible loan without a
   _Qualifizierter Rangrücktritt_ may count as a liability for _Überschuldung_ purposes
   under InsO § 19, forcing a premature insolvency filing obligation. This is the single
   most dangerous drafting error in German convertible finance.

3. **Forgetting to notarize share transfer obligations**: Option agreements, pre-emptive
   rights, and drag-along commitments that trigger an obligation to transfer
   _Geschäftsanteile_ should be notarized under § 15 GmbHG. Unnotarized agreements may
   be void — investors have lost rights because of this error.

4. **Conflating pre-money and post-money valuation caps**: GESSI and German market
   practice use pre-money caps as the default, but custom agreements vary. A "post-money
   cap" is materially more investor-favorable. Ambiguous drafting leads to cap table
   disputes at conversion. Always specify explicitly.

5. **Not filing the INVEST-Zuschuss application within 3 months**: The acquisition grant
   application must be submitted to BAFA within 3 months of share acquisition. Missing
   this deadline means the acquisition grant is permanently lost — no extension.

6. **Applying for INVEST on a secondary share purchase**: INVEST requires acquisition of
   _new_ primary shares (_Neuanteile_). Secondary purchases from existing shareholders do
   not qualify. Structuring the transaction incorrectly forfeits the grant.

7. **Nominal-value bad leaver forfeiture of vested VSOP options (post-BAG 2025)**: After
   the March 2025 BAG ruling, clauses forfeiting _vested_ VSOP options at nominal value
   upon bad leaver events face serious enforceability risk. Plans not yet updated carry
   material litigation exposure.

8. **Assuming § 19a EStG covers VSOPs automatically**: § 19a EStG applies most cleanly
   to direct equity transfers. VSOP plans with cash settlement may need specific
   structural adaptation to qualify for deferral. Do not advise employees that VSOP
   payouts are § 19a-deferred without verifying the plan's specific qualification.

9. **Failing to convert UG to GmbH before Series A**: Institutional VCs will typically
   not invest in a UG. Failing to budget time and cost for the conversion (including
   accumulated profit retention requirement) delays financings and creates last-minute
   pressure in negotiations.

10. **Treating the Gesellschaftervereinbarung as sufficient without notarized articles**:
    Investor protections (liquidation preference, anti-dilution mechanics) in a
    _Gesellschaftervereinbarung_ are enforceable contractually but may not bind a
    good-faith purchaser of _Geschäftsanteile_ who is not a party to the agreement.
    For structural protections that must bind all future shareholders, incorporate them
    into the _Gesellschaftsvertrag_ (requires notarization).

11. **Using foreign-law cap table templates without German law review**: US-style cap
    tables assume stock structures (common, preferred Series A/B). GmbH _Geschäftsanteile_
    have different mechanics. Liquidation waterfalls, anti-dilution calculations, and
    option pool percentages require German-law-specific calculation tools.

12. **EuVECA qualification without investing ≥70% in qualifying portfolio companies**:
    A EuVECA fund that falls below the 70% qualifying portfolio company threshold loses
    the EuVECA designation and EU passport. Monitor investments carefully; a single
    non-qualifying portfolio company can tip a concentrated fund below the threshold.

13. **Assuming drag-along rights automatically override minority shareholder rights**:
    German courts have increasingly scrutinized drag-along clauses in GmbH shareholder
    agreements. Clauses that allow drag-along at any price (including below invested
    capital) may be challenged as _sittenwidrig_ (contrary to public policy) under
    BGB § 138 [VERIFY current BGH position].

14. **Founder personal liability during Vorgesellschaft phase**: Founders who incur
    significant obligations (office leases, employment contracts, software licenses)
    before GmbH registration remain personally liable for those obligations. Pre-registration
    costs should be carefully managed or structured as shareholder advances.

15. **Ignoring KYC/AML timeline in notarization planning**: Since 2020, German notaries
    must complete AML checks on all parties before executing share transfers. Failing to
    initiate KYC early (especially for foreign investors) can delay closings by 3–6 weeks.

16. **Treating BAFA INVEST company eligibility as permanent**: BAFA recognition is not
    a permanent status. Changes in company headcount, turnover, age, or business activity
    can cause a company to fall outside INVEST eligibility. Inform investors of any changes
    that could affect eligibility before they apply for grants.

17. **Relying on oral agreements for founder vesting or leaver mechanics**: German contract
    law generally does not require written form for shareholder agreements. However, oral
    agreements are nearly impossible to enforce in disputes. All vesting, leaver, and
    buy-back mechanics must be in writing (signed _Gesellschaftervereinbarung_).

---

## Writing Standards

Apply these standards to all output:

**Plain language discipline:**

- Write in clear English with German legal terms _in italics_ followed by the English
  translation in parentheses on first use: _Geschäftsanteil_ (GmbH share/business interest)
- Avoid unnecessary legal Latin or German jargon without explanation
- Explain the _why_ behind each German law requirement — most users are not German lawyers
- Annotate any provision where German law differs materially from US/UK practice

**Bilingual terminology reference** (use consistently):

| German Term                                       | English Gloss                                   |
| ------------------------------------------------- | ----------------------------------------------- |
| _Wandeldarlehen_                                  | Convertible loan                                |
| _Gesellschaft mit beschränkter Haftung (GmbH)_    | Limited liability company                       |
| _Unternehmergesellschaft (UG) haftungsbeschränkt_ | Entrepreneurial company (limited liability)     |
| _Geschäftsanteil(e)_                              | Share(s) / business interest(s)                 |
| _Gesellschaftsvertrag_                            | Articles of association / company agreement     |
| _Gesellschaftervereinbarung_                      | Shareholders' agreement                         |
| _Gesellschafterliste_                             | Shareholder register                            |
| _Handelsregister_                                 | Commercial register                             |
| _Geschäftsführer_                                 | Managing director                               |
| _Qualifizierter Rangrücktritt_                    | Qualified subordination clause                  |
| _Bewertungsdach_                                  | Valuation cap                                   |
| _Abschlag_                                        | Discount rate                                   |
| _Liquidationspräferenz_                           | Liquidation preference                          |
| _Verwässerungsschutz_                             | Anti-dilution protection                        |
| _Mitverkaufspflicht_                              | Drag-along obligation                           |
| _Mitverkaufsrecht_                                | Tag-along right (co-sale right)                 |
| _Erdienungsklausel_                               | Vesting provision                               |
| _Überschuldung_                                   | Over-indebtedness                               |
| _Insolvenzantragspflicht_                         | Mandatory insolvency filing obligation          |
| _Vorgesellschaft / GmbH i.G._                     | Pre-registration company                        |
| _Notar_                                           | Notary (German civil law notary)                |
| _verbindliche Auskunft_                           | Tax ruling (binding information from Finanzamt) |

**Quality gates before delivery:**

- [ ] All CRITICAL findings identified before COMPLIANT items listed
- [ ] Every statutory citation includes paragraph number (e.g., § 15 Abs. 3 GmbHG,
      not just "§ 15 GmbHG")
- [ ] All [VERIFY] tags placed on uncertain legal references
- [ ] BAG 2025 ruling impact addressed if any VSOP leaver clause is present
- [ ] INVEST eligibility analysis completed if angel investment is in scope
- [ ] § 19a EStG analysis completed if employee equity plan is in scope
- [ ] Glass Box audit trail included in output
- [ ] Confidence scores assigned to all CRITICAL and RISK findings

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for current GmbHG provisions, BGB loan sections, and EStG § 19a text
- Verify BAG March 2025 ruling citation and full holding
- Search for current BAFA INVEST-Zuschuss program guidelines
- Search for BaFin guidance on EuVECA registration requirements for Germany
- Retrieve recent BMF (Bundesministerium der Finanzen) letters on § 19a EStG and VSOP
  tax treatment
- Save verified results to `/tmp/legalcode-de-vc-authority.md`; cite as VERIFIED in
  Glass Box trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Recommend user verify at: `gesetze-im-internet.de` (statutes), `dejure.org` (case law),
  `bafa.de` (INVEST program), `bafin.de` (EuVECA/KAGB guidance), `bundesfinanzministerium.de`
  (tax guidance)
- Note: `legalcode_mcp: "Not connected"` in Glass Box audit trail

---

## Localization Notes

**Germany vs. other jurisdictions — key divergences for international practitioners:**

| Topic              | Germany                                                                         | US (Delaware)                               | UK                                           |
| ------------------ | ------------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------- |
| Bridge instrument  | Wandeldarlehen (interest-bearing, notarized conversion)                         | SAFE (interest-free, no notarization)       | ASA / convertible note                       |
| Share classes      | Contractual differentiation via _Sonderrechte_; no true preferred share classes | True preferred stock (_Series A Preferred_) | Ordinary + preference shares (Companies Act) |
| Transfer formality | Notarization mandatory (§ 15 GmbHG)                                             | No formality; stock transfer agreement      | Stock transfer form (but no notarization)    |
| Employee equity    | VSOP (contractual); § 19a EStG deferral                                         | ISOs / NSOs; 83(b) election                 | EMI / growth shares / CSOP                   |
| Angel grant        | INVEST-Zuschuss (15% + 25%); tax-free                                           | QSBS § 1202 (gain exclusion)                | SEIS/EIS tax relief                          |
| VC fund            | EuVECA or KAGB                                                                  | SEC exemption (§ 3(c)(1)/§ 3(c)(7))         | AIFMD (UK) / FCA registration                |

---

## Output Format Template

Structure your final output in this format:

```markdown
# German Venture Financing Analysis — [Matter Title]

**Date**: [YYYY-MM-DD]
**Jurisdiction**: Germany
**Matter type**: [Wandeldarlehen / Term Sheet / VSOP / INVEST / EuVECA / General]
**Perspective**: [Founder / Investor / Fund / Employee / Counsel]
**Confidence**: [HIGH / MEDIUM / LOW]

---

## Executive Summary

[2–4 sentence summary of the key findings, primary issues, and recommended actions.
Lead with CRITICAL items if present.]

---

## ⛔ CRITICAL Issues — Act Immediately

[If none: "No critical issues identified."]

### [Issue Title]

- **Finding**: [What was found or is missing]
- **Legal basis**: [§ X GmbHG / BGH case / BAFA guideline]
- **Risk**: [Specific consequence if not remediated]
- **Action**: [Specific remediation step]
- **Fallback**: [If preferred fix unavailable]
- **Deadline**: [If time-sensitive]
- **Confidence**: [Definite / High / Probable]

---

## 🔴 RISK Items — Resolve Before Closing

[If none: "No material risk items identified."]

### [Issue Title]

[Same structure as CRITICAL]

---

## 🟡 FLAG Items — Address Post-Close or in Negotiation

[If none: "No flag items identified."]

### [Issue Title]

[Same structure as CRITICAL, with FLAG priority note]

---

## ✅ COMPLIANT Items — No Action Required

[List clause/topic and brief note confirming compliance]
| Clause/Topic | Status | Note |
|---|---|---|
| [Rangrücktritt] | ✅ COMPLIANT | BGH-approved language present |
| [Valuation cap] | ✅ COMPLIANT | Pre-money; clearly specified |
| ... | | |

---

## Module-Specific Analysis

[Include any of the following modules that were activated for this matter:]

### [A. Instrument Selection / B. Wandeldarlehen / C. GmbH Structure / D. Notarization

/ E. INVEST Grant / F. Founder Liability / G. VSOP/Equity Plan / H. EuVECA / I. Terms]

[Module content structured per the relevant module above]

---

## Recommended Next Steps

1. [Priority 1 action — who, what, by when]
2. [Priority 2 action — who, what, by when]
3. [P3 monitoring items]

---

## Specialist Referrals

| Topic                                | Specialist Required                                      |
| ------------------------------------ | -------------------------------------------------------- |
| § 19a EStG VSOP plan qualification   | _Steuerberater_ with startup/equity expertise            |
| BAG 2025 leaver clause restructuring | German employment law counsel (_Arbeitsrechtler_)        |
| BAFA INVEST application              | BAFA certified advisor or experienced angel fund manager |
| EuVECA BaFin registration            | German capital markets / investment fund counsel         |
| Notarization of share transfer       | German _Notar_ (civil law notary)                        |

---

[Glass Box Audit Trail — YAML as specified above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis — Mode A (created from
scratch). Research methodology: 2-agent parallel research pipeline covering (1) German
venture financing legal framework: BGB §§ 488 et seq., GmbHG §§ 1–88 (particularly §§
5a, 15, 40, 43), EStG §§ 17/19a/20/3 Nr.39–40, KStG § 8b, InsO § 19, KAGB, GNotKG,
EU Regulation 345/2013 (EuVECA), AIFMD 2011/61/EU; (2) GESSI standard documents
(standardsinstitute.de); INVEST-Zuschuss program (BAFA guidelines effective March 6,
2024 through December 31, 2026); BAG March 2025 ruling on bad leaver vested option
forfeiture; Jahressteuergesetz 2024 § 19a EStG reforms; DiRUG/DiREG online GmbH
formation; German VC market practice. Secondary sources: Orrick (Germany VC Guide,
Legal Ninja series), YPOG (ESOPs in Start-ups), Taylor Wessing, Heuking (liquidation
preferences), Noerr (BAG leaver ruling), Gaia Law (EIP vs VSOP), Bird & Bird (§ 15
GmbHG form requirements), Rose & Partner, Chambers (Germany VC 2025 trends). Complements
`legalcode-de-gmbh-formation` (formation workflow) and `legalcode-venture-financing-suite`
(cross-border instrument router). All statutory citations carry hallucination risk;
verify at gesetze-im-internet.de before reliance. Recommended review by German
_Rechtsanwalt_ and _Steuerberater_ before operational use.
