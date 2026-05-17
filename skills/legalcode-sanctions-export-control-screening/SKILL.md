---
name: legalcode-sanctions-export-control-screening
description: >
  Screen transactions, counterparties, and exports against major international sanctions
  and export control regimes: OFAC SDN and Consolidated Sanctions Lists (all programs),
  EU Consolidated Sanctions List, UK OFSI Consolidated List, UN Security Council
  consolidated lists, BIS Entity/Denied Persons/Unverified/MEU Lists, and DDTC Debarred
  Parties. Applies the OFAC 50% Rule (SDN-owned beneficial owners), secondary sanctions
  analysis under CAATSA Sections 228/231/232/233 and CISADA, and Sectoral Sanctions
  Identifications (SSI) Directive 1-4 analysis for Russia. Covers EAR export
  classification (ECCN and EAR99), Commerce Control List (CCL) mapping, license exception
  analysis (STA, ENC, LVS, TMP, TSU, RPL, GOV, and others), Foreign Direct Product Rule
  (FDPR), Military End-Use Rule (15 C.F.R. § 744.21), and deemed export analysis. Covers
  ITAR US Munitions List (USML) classification, deemed export, TAA/MLA requirements,
  and fundamental research exemption analysis. Addresses correspondent banking
  de-risking, SWIFT compliance, and shell-company/beneficial ownership risk. Produces
  a five-tier risk determination (BLOCKED / HIGH RISK / ELEVATED / MONITORED / CLEAR),
  program-by-program analysis, confidence-scored findings, and a complete Glass Box
  audit trail. Use when screening a transaction before it proceeds, onboarding a
  counterparty, classifying an export, evaluating secondary sanctions exposure, preparing
  a due diligence report, or responding to a potential violation. Triggers on: "sanctions
  screening," "OFAC check," "SDN list," "50% rule," "entity list," "ECCN classification,"
  "ITAR compliance," "EAR license exception," "export control classification," "secondary
  sanctions," "CAATSA," "EU sanctions," "UK OFSI," "correspondent banking sanctions,"
  "trade compliance screening," "restricted party list," "denied party," "sectoral
  sanctions," "deemed export," "Foreign Direct Product Rule," "FDPR," "voluntary
  self-disclosure sanctions."
allowed-tools: Read, Bash(grep:*)
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Sanctions & Export Control Screening

> **Disclaimer**: This skill provides a framework for AI-assisted sanctions and export
> control screening. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs must be reviewed by qualified trade sanctions
> counsel or a licensed export compliance professional before reliance. Sanctions
> designations and regulations change continuously — verify all findings against current
> official sources (OFAC, BIS, DDTC, EEAS, OFSI, UN) before acting. List data cited
> from training knowledge carries hallucination risk — always re-screen against live
> list versions before any transaction proceeds. This skill does not substitute for
> independent screening against current official lists.

---

## Purpose and Scope

This skill screens transactions, counterparties, goods, and technology against the major
US, EU, UK, and UN sanctions and export control frameworks. It applies the OFAC 50%
Rule, sectoral sanctions Directive analysis, EAR export classification, ITAR USML
classification, secondary sanctions risk assessment, and red flag analysis, producing
a five-tier risk determination with a complete Glass Box audit trail.

**Covers:**
- OFAC SDN List, Consolidated Sanctions List (all 26+ programs), and SSI Directives 1-4
- OFAC 50% Rule: UBO screening and beneficial ownership look-through
- EU Consolidated Sanctions List (EEAS); Russia 14-package sanctions regime; all EU thematic programs
- UK OFSI Consolidated List; Russia (Sanctions) (EU Exit) Regulations 2019 (SI 2019/855)
- UN Security Council consolidated lists (1267/ISIL/Al-Qaeda, 1988/Taliban, 1718/DPRK, 1970/Libya, and all applicable subsidiary committees)
- BIS Entity List, Denied Persons List, Unverified List, Military End-User List
- DDTC Debarred Parties List
- EAR export classification: ECCN/EAR99, CCL, Country Chart, license exception analysis
- ITAR USML classification: 21 categories, license/exemption determination, deemed export analysis
- Foreign Direct Product Rule (FDPR) for items manufactured outside the US using US technology
- Military End-Use Rule (15 C.F.R. § 744.21) for China, Russia, and Venezuela
- Secondary sanctions: CAATSA Sections 228/231/232/233; CISADA; PEESA; IEEPA-based programs
- Correspondent banking compliance: SWIFT screening, shell company risk, beneficial ownership
- Red flag analysis: transshipment, end-user mismatch, payment routing anomalies, documentation gaps
- Voluntary self-disclosure (VSD) guidance for OFAC, BIS, and DDTC programs

**Does not:**
- Constitute legal advice or replace qualified trade compliance counsel
- Screen in real time against live list versions — all findings must be verified against current official list versions before a transaction proceeds
- Provide a complete AML/KYC program assessment (see `legalcode-aml-kyc-compliance`)
- Cover anti-bribery or anti-corruption compliance (see `legalcode-anti-bribery-compliance`)
- Provide CFIUS/foreign investment national security screening
- Cover all export control regimes globally — focuses on US (EAR/ITAR), EU, and UK programs

---

## Jurisdiction and Governing Law

This skill is multi-jurisdictional by design. Unlike contract review, no single "governing
law" clause determines which regime applies — nexus to each jurisdiction's territory,
persons, currency, and subject matter determines applicability simultaneously.

### Nexus Matrix

| Regime | Nexus Trigger (any one suffices) | Primary Citation |
|--------|----------------------------------|-----------------|
| **OFAC (US)** | US person (citizen/PR/US-incorporated entity) is party or intermediary; USD or US correspondent bank in payment chain; US-origin goods/technology | 50 U.S.C. §§ 1701-1707 (IEEPA); 31 C.F.R. Chapter V [VERIFY applicable program part] |
| **EAR (US)** | Item "subject to the EAR": US-origin; manufactured using US technology (FDPR); on CCL anywhere in world with US-controlled content | 50 U.S.C. §§ 4801-4852 (ECRA); 15 C.F.R. Parts 730-774 |
| **ITAR (US)** | Item is a defense article/service/technical data on USML; exported, re-exported, or released to a foreign national (including inside the US) | 22 U.S.C. § 2778 (AECA); 22 C.F.R. Parts 120-130 |
| **EU Sanctions** | EU-incorporated entity or EU national is party; EUR or EU banking in payment chain; goods originate in or transit through the EU | TFEU Art. 215; Council Reg. 269/2014; Council Reg. 833/2014 [VERIFY current applicable regulation] |
| **UK OFSI** | UK-incorporated entity; UK national or UK-resident involved; GBP or UK banking; goods transit UK | SAMLA 2018; SI 2019/855 (Russia); penalties: 14 years/£1M or 50% of value [VERIFY current provisions] |
| **UN Sanctions** | All UN member states; universal mandatory baseline | UN Charter Chapter VII; Art. 25; UNSCR 1267, 1988, 1718, 1970 [VERIFY applicable resolution] |

[JURISDICTION-SPECIFIC] Secondary sanctions (CAATSA, CISADA, PEESA) extend US
jurisdiction to non-US persons conducting transactions outside the US in designated
sectors. For non-US organizations with no direct US nexus, secondary sanctions create
risk of exclusion from the US financial system and potential SDN designation — not a
direct legal prohibition on the foreign person per se, but a material business risk
requiring separate analysis.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming transaction context, the workflow pauses and asks when:

- The answer determines which regulatory regimes apply
- Transaction type determines whether export controls (EAR/ITAR) are triggered
- Beneficial ownership information is needed to apply the OFAC 50% Rule
- Risk tolerance calibration affects screening thresholds and output format

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked
below. If the user has already provided the information, skip that question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept transaction information in any of these formats:
- **Transaction description**: Counterparty names, transaction type, goods/services, jurisdictions, payment routing
- **Contract or order document**: PDF/DOCX containing party names, product descriptions, Incoterms, delivery terms
- **Counterparty data file**: CSV or list of names for batch pre-screening
- **ECCN classification request**: Product technical specifications for export classification only
- **Organizational ownership chart**: For complex OFAC 50% Rule analysis

If no information is provided, proceed directly to Step 2 and construct the screen from user answers.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning analysis, gather the following. Skip questions the user has already answered.

---

**Q1 — Transaction Type**

What type of transaction is being screened?
- **Financial transfer / payment**: Wire, ACH, SWIFT, trade finance (LC/documentary collection) — no goods component
- **Goods export or import**: Physical goods crossing a border — determines EAR/ITAR applicability
- **Technology transfer or deemed export**: Sharing technical data, software, or know-how with a foreign person (including foreign nationals inside the US)
- **Services or professional engagement**: Consulting, engineering, legal, financial advisory — no physical goods
- **Re-export or transshipment**: Previously exported goods being re-exported from a third country
- **Investment or acquisition**: Equity investment, joint venture — ownership-level 50% Rule analysis required
- **Mixed transaction**: Combination of the above

*Why this matters*: Transaction type determines which regimes apply. A pure financial transfer does not trigger EAR; a technology transfer may trigger both EAR and ITAR; investment transactions require ownership analysis distinct from transactional screening.

---

**Q2 — Primary Counterparty**

Who is the primary counterparty? Provide:
- **Full legal name** (Latin script AND local script: Arabic, Cyrillic, Chinese, Farsi as applicable)
- **Country of incorporation / registration**
- **Country where counterparty physically operates** (may differ from incorporation jurisdiction)
- **Known aliases, trading names, or former legal names**
- **Entity type**: Natural person / Private company / State-owned enterprise (SOE) / Financial institution / Government agency / NGO

*Follow-up if entity*: Are the beneficial owners (UBOs) known? Provide name(s), nationality, and ownership percentage if available.

*Follow-up if individual*: Date of birth, nationality, country of residence?

*Why this matters*: OFAC's 50% Rule means an entity may be blocked even if not itself listed, if ≥50% is owned (in aggregate) by SDN-designated persons. SOEs present heightened risk under SSI sectoral sanctions. Common names require additional identifiers for accurate screening.

---

**Q3 — Additional Parties**

Who else is involved in this transaction?
- **Intermediaries**: Agents, brokers, distributors, trading companies, freight forwarders, customs brokers
- **Financial institutions**: Banks in the payment chain, correspondent banks (if known)
- **Shipping and logistics**: Carrier, shipping agent, vessel name (for maritime transport)
- **End user** (if different from buyer): Who will ultimately receive or use the goods/services?
- **Guarantors or sureties**: Financial backing parties

*Why this matters*: Violations frequently occur at intermediary nodes. BIS enforcement actions consistently involve cases where the direct counterparty is clean but an intermediary routes goods to a prohibited end user. Every party in the chain should be screened.

---

**Q4 — Jurisdictions**

List all countries involved:
- **Origin**: Where goods, services, or technology originate
- **Destination**: Where they will ultimately be delivered or used
- **Transit / transshipment**: Countries through which goods will pass
- **Payment routing**: Countries through which funds will be routed (correspondent banking)
- **Counterparty incorporation**: Where each entity in the chain is incorporated

*Flag*: If UAE, Turkey, Georgia, Kazakhstan, Armenia, or Serbia appear as transit or destination points for goods related to Russia or Belarus — flag as known transshipment risk pathways requiring enhanced analysis. [VERIFY current BIS/OFAC guidance on transshipment jurisdictions]

---

**Q5 — Product / Technology / Services**

If the transaction involves goods, technology, software, or services:
- **What is the product or technology?** (Technical description, model number, commercial name)
- **Primary commercial or industrial application**
- **Any military, dual-use, or specialized applications?**
- **HTS or Schedule B code** (10-digit tariff classification, if known)
- **ECCN** (if previously classified)
- **Country of origin or manufacture**

Classification status options:
- I believe it is **EAR99** (no ECCN — not on the CCL)
- I believe it has an **ECCN but I don't know the number** (flag for Step 6B classification)
- I believe it may be **ITAR-controlled** (flag for Step 6D)
- **No goods or technology involved** — pure financial or services transaction (skip Step 6)

---

**Q6 — End Use and End User**

If goods, technology, or services are involved:
- **Stated end use**: What will the goods/technology be used for specifically?
- **Ultimate end user** (if different from buyer): Who receives and operates the item?
- **Military, government, or WMD connection?**: Is the end user or use related to military programs, weapons development, or government defense programs?
- **End-use certificate**: Has the counterparty provided one? If so, what does it state?

*Red flag triggers*: Vague end-use description ("commercial", "industrial", "general use") for dual-use technology; end user is a military entity, ministry of defense, or defense contractor in a country of concern; counterparty declines to specify end use or end user.

---

**Q7 — Applicable Jurisdiction Nexus**

Which of the following applies to your organization? (Select all that apply)
- **US nexus**: US-incorporated entity, US citizen/permanent resident, USD or US correspondent bank, US-origin goods
- **EU nexus**: EU member state incorporation, EUR or EU banking, goods originate in or transit EU
- **UK nexus**: UK incorporation, UK national or UK-resident involved, GBP or UK banking
- **Multiple nexuses apply**: Specify
- **Unsure**: Flag for nexus analysis in Step 3

---

**Q8 — Prior Screening History**

- Has this counterparty been screened before? When and with what result?
- Is there an existing commercial relationship? How long?
- Is this triggered by a specific concern (whistleblower report, regulatory inquiry, internal audit finding)?

**Escalation trigger**: If this screening relates to a regulatory inquiry, government subpoena, or pending enforcement action, advise:

> "This screening is occurring in the context of a potential enforcement matter.
> AI-assisted outputs may not be attorney-client privileged. Before generating written
> findings in this context, consult with trade sanctions counsel about how to structure
> this analysis to preserve applicable protections."

---

**Q9 — Transaction Value and Frequency**

- **Approximate USD equivalent value**
- **Frequency**: One-time / Recurring (specify interval) / Ongoing relationship
- **Payment structure**: Advance payment / Letter of credit / Open account / Installment / Milestone / Other

*Why this matters*: Value affects which reporting thresholds may apply. Frequency determines whether one-time or periodic re-screening is appropriate. Unusual payment structures (installments to third countries, advance payments to unfamiliar parties) are independent red flags.

---

**Q10 — Risk Tolerance and Output Mode**

Purpose of this screening:
- **Transaction approval decision**: Specific transaction needs a CLEAR / HOLD / ESCALATE / DECLINE determination
- **Due diligence report**: Written report needed for onboarding file or counterparty compliance record
- **Batch pre-screening**: Multiple counterparties to screen (high-volume, lower detail per counterparty)
- **Program design**: Designing or auditing a sanctions screening program
- **Incident response**: A potential violation has been identified; need facts analysis and next steps

Risk tolerance calibration:
- **Conservative**: Flag all potential matches and borderline country risks; prefer false positives over false negatives
- **Pragmatic**: Flag credible matches and material risks; apply reasonable industry-standard thresholds
- **Streamlined**: Flag only clear matches or prohibited transactions; minimize false positives for high-volume screening

---

### Step 3: Determine Applicable Programs

Based on Step 2 answers, construct the **Applicable Programs Matrix** — the set of regimes requiring active screening. Apply the nexus decision trees from the Nexus Matrix above.

For every transaction, assess:
1. **US nexus?** → Apply OFAC programs + EAR/ITAR (if goods/tech involved)
2. **EU nexus?** → Apply EU Consolidated Sanctions List
3. **UK nexus?** → Apply UK OFSI Consolidated List
4. **UN baseline?** → Apply UN consolidated lists (universal mandatory floor)
5. **Secondary sanctions risk?** → Assess CAATSA/CISADA even absent direct US nexus (non-US parties dealing with sanctioned sectors face correspondent banking and designation risk)

Document the applicable programs before proceeding. If nexus is unclear for any regime, flag it as requiring legal determination and proceed with conservative assumption that the regime applies.

### Step 4: Restricted Party Screening

For each party identified in Step 2 (including all intermediaries, end users, financial institutions, and vessels), screen against each applicable list.

#### Lists to Screen Against

**US Lists (OFAC)**
- SDN List (Specially Designated Nationals and Blocked Persons)
- SSI List (Sectoral Sanctions Identifications — Russia Directives 1-4)
- Non-SDN Consolidated Sanctions List (NS-MBS, NS-CMIC, NS-PLC, and others)
- Foreign Sanctions Evaders (FSE) List

**US Lists (BIS)**
- Entity List (Supplement 1 to 15 C.F.R. Part 744) — license required; often policy of denial
- Denied Persons List (15 C.F.R. Part 764) — absolute prohibition; US persons cannot participate in any export transaction involving listed persons
- Unverified List (Supplement 6 to Part 744) — triggers enhanced due diligence; BIS unable to verify bona fides; not a hard prohibition but significant compliance flag
- Military End-User (MEU) List (Supplement 7 to Part 744) — military/intelligence end users in China, Russia, Venezuela

**US Lists (DDTC)**
- Debarred Parties List — cannot receive defense articles/services; US persons cannot participate

**EU Lists**
- EU Consolidated Financial Sanctions List (European External Action Service — eeas.europa.eu) [VERIFY current source URL]

**UK Lists**
- UK Consolidated List (OFSI / HM Treasury) [VERIFY current source]

**UN Lists**
- UN Security Council Consolidated Sanctions List: 1267/ISIL/Al-Qaeda; 1988/Taliban; 1718/DPRK; 1970/Libya; and all applicable subsidiary committees [VERIFY current resolution scope at un.org/securitycouncil]

#### OFAC 50% Rule Application (Mandatory for All Entity Counterparties)

For every entity (non-individual) counterparty, apply the 50% Rule:

1. Identify all known beneficial owners (UBOs) with any ownership interest
2. Screen each UBO against the OFAC SDN List individually
3. **Aggregate** ownership interests of multiple SDN-listed persons toward the 50% threshold
4. Apply look-through analysis for indirect ownership chains (SDN → Company A → Company B)
5. If SDN person(s) hold ≥50% aggregate ownership (direct or indirect): **the entity is blocked as a matter of US sanctions law even if not itself listed**
6. If ownership structure is opaque, undisclosed, or runs through secrecy jurisdictions: flag as **OWNERSHIP RISK — ENHANCED DUE DILIGENCE REQUIRED** (TIER 3 minimum)

*Important*: OFAC does not publish a list of 50%-rule-blocked entities. The obligation to trace ownership rests entirely with the screener. [VERIFY current OFAC FAQ guidance on 50% Rule application, particularly for complex ownership structures]

#### Name Matching Protocol

- Screen full legal name, all trading names, former names, and all known aliases
- Apply transliteration variants for Arabic, Cyrillic (Russian/Ukrainian/Belarusian), Chinese, and Farsi scripts
- Screen individual owners and directors by name against individual SDN list entries
- Apply fuzzy matching at approximately 80% similarity threshold (Wolfsberg Group industry guidance)
- Flag all matches at ≥75% similarity for manual human review — do not auto-clear below 95%
- For every match reviewed and cleared as a false positive, document the reasoning using objective identifiers (DOB, country, registration number, address) — not relationship familiarity
- Record list version dates and screening methodology in the audit trail

### Step 5: Country/Jurisdiction Sanctions Analysis

Assess country-level sanctions risk independent of named-party screening.

#### Comprehensive Sanctions Jurisdictions (US OFAC)

Most transactions are prohibited absent a specific OFAC license or applicable general license. [VERIFY current program scope against OFAC publications before each screening]

| Jurisdiction | OFAC Program | Key Citation | Key Note |
|-------------|-------------|-------------|---------|
| Cuba | Cuban Assets Control Regulations | 31 C.F.R. Part 515; TWEA | Near-total embargo; broad GL exceptions for humanitarian, remittances, journalism |
| Iran | Iranian Transactions and Sanctions Regulations | 31 C.F.R. Part 560; IEEPA; ISA | Most comprehensive; secondary sanctions on foreign persons in key sectors (finance, energy, shipping) |
| North Korea (DPRK) | North Korea Sanctions Regulations | 31 C.F.R. Part 510; IEEPA; UNSCR 1718 | Near-total embargo; secondary sanctions; maritime evasion and SWIFT circumvention are highest-risk patterns |
| Syria | Syrian Sanctions Regulations | 31 C.F.R. Part 542 | Comprehensive; reconstruction-sector GL available [VERIFY]; IRGC/Hezbollah presence |
| Russia (occupied territories) | Ukraine-/Russia-Related Sanctions | 31 C.F.R. Part 589; E.O. 14065 | Specific geographic prohibitions in Donetsk, Luhansk, Zaporizhzhia, Kherson regions |

#### Targeted Sanctions Programs (Transaction-Specific Analysis Required)

[VERIFY current scope — these programs expand continuously]

- **Russia (broader)**: E.O. 14024 (Russian Harmful Foreign Activities) + CAATSA — SDN designations; SSI Directive restrictions on Russia financial/energy/defense sector debt and equity; not comprehensive embargo but expanding through 2022-2026 packages
- **Belarus**: Coordinated EU/US/UK targeted sanctions; specific goods restrictions; aviation-related restrictions
- **Venezuela**: E.O.s 13850/13884 — government entity and PDVSA restrictions; petroleum sector; secondary sanctions risk for non-US persons
- **Myanmar**: Targeted OFAC sanctions; military entity restrictions; EU/UK coordinated; jade/gems sector controls
- **China**: NS-CMIC list; Entity List restrictions; no comprehensive OFAC embargo but expanding targeted programs; EAR export controls (D:5 country group)

#### Country-Level Red Flags

- Counterparty in high-risk jurisdiction with no plausible legitimate business rationale for the transaction
- Multiple jurisdictional hops suggesting transshipment or re-export risk
- Free trade zone routing in UAE, Turkey, Georgia, Kazakhstan, Armenia, Serbia for goods with Russia or Belarus nexus — known transshipment hubs for controlled goods [VERIFY current BIS/OFAC transshipment guidance]
- Payment routing through third-country banks with no nexus to the transaction
- Destination country is an embargo jurisdiction but counterparty claims to be a third-country reseller

### Step 6: Export Control Classification (if goods / technology / services involved)

**Skip this step** for pure financial transactions with no goods, technology, software, or technical services component. Proceed directly to Step 7.

#### Step 6A — Is the Item Subject to the EAR?

Under 15 C.F.R. Part 734, an item is "subject to the EAR" if it is:
- In the United States (all items physically in the US are subject to EAR)
- US-origin (manufactured in the US, even if currently located abroad)
- Foreign-made and incorporates more than the *de minimis* threshold of US-controlled content [VERIFY current de minimis thresholds: generally 25% for most destinations; 10% for E:1 countries and certain Entity List/SSI parties]
- Foreign-made as the direct product of US-origin technology or US-origin equipment (FDPR) [VERIFY current FDPR scope — significantly expanded in April 2022 for Russia/Belarus military end users]

If the item is not subject to the EAR, flag as potentially outside US export control jurisdiction and assess under other applicable national control regimes.

#### Step 6B — ECCN Classification

1. Is the item listed on the Commerce Control List (CCL)? (15 C.F.R. Part 774)
2. Identify the CCL Category (0-9) and Product Group (A-E):
   - Category 0: Nuclear / Miscellaneous
   - Category 1: Materials, chemicals, microorganisms, toxins
   - Category 2: Materials processing
   - Category 3: Electronics
   - Category 4: Computers
   - Category 5: Telecommunications and information security
   - Category 6: Sensors and lasers
   - Category 7: Navigation, avionics, inertial systems
   - Category 8: Marine
   - Category 9: Aerospace and propulsion
3. Identify control reason(s): AT (Anti-terrorism), CB (Chemical/Biological), CC (Crime Control), CW (Chemical Weapons), EI (Encryption items), FC (Firearms Convention), MT (Missile Technology), NP (Nuclear Nonproliferation), NS (National Security), RS (Regional Stability), SL (Surreptitious listening), SS (Short Supply), UN (United Nations)
4. If not on CCL: classify as **EAR99** — note that EAR99 items still cannot be exported to comprehensive embargo destinations or for prohibited end uses, and cannot go to denied parties

**⟁ CLARIFY** — If ECCN is unknown or uncertain, determine classification basis:
- **Self-classification confirmed**: Proceed; note as [SELF-CLASSIFIED] in audit trail
- **Manufacturer's binding classification available**: Most reliable; document in audit trail
- **BIS Commodity Classification Request required**: Advise; required before export when uncertainty is material [VERIFY current BIS classification request procedure and timeline]
- **Uncertain — possible ITAR**: Flag for DDTC determination; treat as ITAR until confirmed EAR

#### Step 6C — License Requirement and Exception Analysis

1. Identify the destination country's Country Group (Supplement 1 to 15 C.F.R. Part 740): Group A (allies, 42 countries), Group B (general), Group D:1 (national security — Russia, China), Group D:5 (end-user review — China, Russia, Venezuela), Group E:1 (Cuba, Iran, DPRK, Syria)
2. Cross-reference ECCN control reasons against the Country Chart (Supplement 1 to 15 C.F.R. Part 738) for the destination
3. If the ECCN/Country Chart intersection requires a license, check license exceptions in order:
   - **STA (§ 740.20)**: Strategic Trade Authorization — most broadly applicable; covers most dual-use items to 42 Group A allied nations
   - **ENC (§ 740.17)**: Encryption items — widely applicable to commercial encryption products for non-E:1 destinations
   - **TSU (§ 740.13)**: Technology/software unrestricted — publicly available; educational; mass-market software
   - **LVS (§ 740.3)**: Limited value shipments — per-transaction dollar limits by ECCN
   - **TMP (§ 740.9)**: Temporary exports for return; tools of trade; exhibition
   - **RPL (§ 740.10)**: One-for-one replacement of previously exported US-origin items
   - **GOV (§ 740.11)**: US government agencies; international organizations; inspection regimes
4. Apply enhanced export controls for Russia and Belarus (expanded from April 2022): additional CCL categories controlled; expanded Entity List; extended FDPR reach [VERIFY current Russia/Belarus control scope under BIS rulemakings]
5. If no license exception applies and a license is required: advise on BIS license application via SNAP-R; typical review timeline 60-90+ days; policy of denial likely for many Russia/DPRK/Iran/Syria end users

#### Step 6D — ITAR Determination

1. Is the item on the US Munitions List (USML)? (22 C.F.R. Part 121 — 21 categories)
   - Key categories: IV (launch vehicles/missiles), VI (surface vessels), VII (tanks/military vehicles), VIII (aircraft), XI (military electronics), XII (fire control/targeting/C2), XV (spacecraft), XIX (gas turbine engines)
   - An item "designed for" or "modified for" military use may be USML even if it has a commercial appearance
2. If yes → ITAR-controlled; any export requires DDTC license (typically DSP-5 for permanent export); any defense service requires a Technical Assistance Agreement (TAA); manufacturing abroad requires a Manufacturing License Agreement (MLA)
3. **Deemed export analysis**: Any release of ITAR-controlled technical data to a foreign national inside the US is treated as an export to that person's country — requires the same DDTC authorization as a physical export (unless an exemption applies)
4. Key exemptions:
   - Fundamental research (22 C.F.R. § 120.41): university/laboratory basic or applied research with no sponsor-imposed publication restrictions and no access restrictions on foreign nationals; does not qualify if proprietary obligations or access restrictions are present
   - Public domain information: data already in general publication without restriction
   - Personal baggage exception: limited personal-use items
5. ITAR registration: manufacturers, exporters, and brokers of defense articles must register with DDTC regardless of whether an export occurs [VERIFY current DDTC registration requirements and fees]

### Step 7: Transaction-Specific Red Flag Analysis

Beyond named-party screening and country analysis, assess the following red flags for sanctions evasion or export control circumvention. Apply the "reason to know" standard — the presence of red flags creates an affirmative obligation to investigate; they cannot simply be noted and ignored.

#### Red Flag Matrix

| Category | Indicator | Escalation Level |
|----------|-----------|-----------------|
| **Payment routing anomalies** | Payment from a third country with no nexus to the transaction; correspondent bank in a sanctioned jurisdiction; cryptocurrency for high-value commercial transactions with no clear rationale | TIER 2-3 |
| **Beneficial ownership opacity** | Refusal to disclose UBOs; ownership chain through multiple shell companies in secrecy jurisdictions; jurisdiction with no public ownership registry | TIER 2-3 |
| **End-user mismatch** | Stated end user is in Country A but delivery is Country B; small trading company buying military-grade technology; end user has no plausible use for the product quantity or type | TIER 2-3 |
| **Transshipment risk** | Routing through UAE, Turkey, Georgia, Kazakhstan, Armenia, Serbia for goods with Russia/Belarus nexus; multiple re-routing requests after initial order; shipping agent with no track record | TIER 2-3 |
| **Product-buyer mismatch** | Buyer lacks technical expertise, storage/handling capacity, or business rationale for the quantity or type of goods | TIER 3 |
| **Documentation gaps** | Refusal to provide an end-use certificate; unusual vagueness about intended use; inconsistent documentation (different names, addresses) across transaction documents | TIER 2-3 |
| **Pricing anomaly** | Transaction price significantly above or below market value for the goods; pricing inconsistent with the stated commercial relationship | TIER 3 |
| **Urgency or secrecy** | Pressure to complete without normal due diligence; request to omit certain parties from documentation; request for unusual payment methods or currency | TIER 2 |
| **Prior compliance concerns** | Counterparty previously screened with red flags unresolved; prior violations in same jurisdiction or sector | TIER 2-3 |

### Step 8: Classify All Findings Using the Five-Tier Severity System

Apply the **Five-Tier Severity System** (defined below) to each finding from Steps 4-7.

For every TIER 1 (BLOCKED) or TIER 2 (HIGH RISK) finding, apply the **Self-Interrogation** framework before finalizing (see Quality Frameworks section).

### Step 9: Quality Verification

Before delivering the screening report:
1. Run all five **Citation Quality Gates** (Sanctions-Adapted) — see Quality Frameworks section
2. Run all four **Additional Quality Gates** unique to sanctions screening (Temporal Validity, List Version Integrity, Program Scope Verification, Escalation Confirmation)
3. Apply **Confidence Scoring** (Dual Scale A/B) to all findings
4. Verify the **Glass Box Audit Trail** is complete before delivery

### Step 10: Deliver Screening Report

Produce output using the **Output Format Template** at the end of this skill. The Glass Box Audit Trail is mandatory and must accompany every screening deliverable.

For TIER 1 or TIER 2 determinations, include a prominent standalone notice:

> "**COUNSEL REVIEW REQUIRED**: This determination has been classified [TIER 1 BLOCKED /
> TIER 2 HIGH RISK]. This AI-assisted finding must be reviewed by qualified trade
> sanctions counsel before the organization acts on it. Do not process, block, reject,
> or report this transaction based solely on this AI output."

---

## Five-Tier Severity Classification System

The standard GREEN/YELLOW/RED scale from contract review is inadequate for sanctions
screening. Some prohibitions are absolute — a confirmed SDN match is not a "yellow." The
following five-tier system is designed specifically for sanctions and export control.

---

### TIER 1 — BLOCKED / PROHIBITED ⛔

**Definition**: The transaction is prohibited by law without a specific license or
governmental authorization. No further analysis changes this outcome until authorization
is obtained.

**Triggers:**
- Confirmed SDN match: match score ≥95%, or exact name match with ≥1 corroborating identifier (DOB, country of incorporation, registration number, or address)
- Confirmed match on EU Consolidated List, UK OFSI Consolidated List, or UN Consolidated List
- Transaction falls within a comprehensive sanctions program (Cuba, Iran, DPRK, Syria) without an applicable OFAC general license or specific license
- Entity is ≥50% owned (directly or indirectly, in aggregate) by one or more SDN-listed persons — 50% Rule confirmed
- Export requires EAR license; no license exception applies; no BIS authorization obtained
- Item is ITAR-controlled; DDTC license or TAA required and not yet obtained
- Transaction is for a confirmed WMD, terrorist, or other absolute end-use prohibition under 15 C.F.R. Part 744 or 22 C.F.R. § 126.1

**Required action**: **DO NOT PROCESS.** Escalate immediately to Chief Compliance Officer and General Counsel. Engage external trade sanctions counsel. Consider blocking/reporting requirements. Assess whether a voluntary self-disclosure obligation exists to OFAC, BIS, or DDTC. If funds or property are already received, block and report per applicable program requirements [VERIFY current blocking/reporting obligations].

---

### TIER 2 — HIGH RISK / ESCALATE TO COUNSEL 🔴

**Definition**: A credible legal basis exists to prohibit or seriously restrict the
transaction, but the analysis is not yet conclusive — the match requires expert
adjudication, the program application is novel, or aggregate risk factors exceed
routine compliance officer authority.

**Triggers:**
- Match score 75-94% against SDN, EU, or UK list — credible potential match but insufficient identifiers to confirm
- 50% Rule: ownership structure is opaque and partial evidence suggests SDN ownership may be present
- Transaction involves Russia SSI sectoral sanctions — counterparty is SSI-listed and the proposed transaction type may fall within a Directive prohibition
- Multiple Tier 3 findings present simultaneously, creating aggregate risk exceeding routine compliance authority
- ECCN classification is uncertain and item may be ITAR-controlled (requires DDTC determination)
- Counterparty appears on BIS Unverified List (not a hard prohibition, but triggers enhanced due diligence)
- Transaction involves a jurisdiction with targeted sanctions and counterparty operates in a targeted sector
- Serious transshipment or evasion indicators present

**Required action**: HOLD. Do not process until escalation is resolved. Escalate to compliance counsel or General Counsel. Document hold in the compliance record.

---

### TIER 3 — ELEVATED / ENHANCED DUE DILIGENCE REQUIRED 🟠

**Definition**: Meaningful risk indicators are present that exceed normal compliance
thresholds, but no confirmed match or clear legal prohibition has been identified.
Enhanced due diligence can resolve the question.

**Triggers:**
- Match score 50-74% — possible match requiring additional identifying information
- Counterparty in a jurisdiction with targeted sanctions; in a sector targeted by that program; not itself listed
- Transaction routes through a known transshipment hub with no clear explanation
- Beneficial ownership partially known with indications (not confirmed) of SDN connection below 50%
- End use or end user is vague for a dual-use item with known military application
- Item is borderline between EAR99 and CCL-controlled — ECCN determination required before export
- BIS Entity List or Unverified List match on an intermediary or freight agent (not the direct counterparty)
- Counterparty has prior history of operating in a sanctioned jurisdiction or known SDN connections

**Required action**: HOLD pending enhanced due diligence. Obtain additional identifying information (DOB, registration number, UBO disclosure, end-use certificate). Require senior compliance officer sign-off before proceeding. Document all due diligence steps taken.

---

### TIER 4 — MONITORED / STANDARD CONTROLS PLUS HEIGHTENED AWARENESS 🟡

**Definition**: No identified match or clear prohibition, but risk indicators warrant
documenting, monitoring, and ensuring standard controls are fully applied.
Transaction can proceed subject to conditions.

**Triggers:**
- Match score below 50% — unlikely match; name similarity noted and documented
- Counterparty in a country with elevated sanctions risk but not itself in a sanctioned sector or on any list (e.g., private Russian company not otherwise designated)
- One or two isolated red flags present without corroboration
- Transaction uses payment routing through a jurisdiction with some sanctions exposure but not itself prohibited
- Item is EAR99; destination country has AT column X controls (generally no license required, but end-use restrictions apply)
- Counterparty operates in a sector adjacent to sanctioned activity but is not itself restricted

**Required action**: Proceed with standard compliance controls. Document all risk indicators in the compliance record. Set calendar reminder for re-screening per organizational policy. Compliance officer sign-off sufficient; no senior escalation required.

---

### TIER 5 — CLEAR ✅

**Definition**: Screening is complete; no matches found on any applicable restricted
party list; no prohibited country nexus; no applicable export control bar; no material
red flags present.

**Triggers:**
- All screened parties return NO MATCH on all applicable lists
- Destination is not subject to any comprehensive or targeted sanctions program applicable to this transaction type
- Item is EAR99 and destination is not sanctioned; or a specific license exception has been confirmed
- No red flags present, or red flags have been assessed and documented as resolved

**Required action**: Document screening outcome, list versions consulted, and screening date in the compliance record. Transaction may proceed. Set re-screening interval per organizational policy (standard guidance: re-screen at each transaction, or at minimum on each SDN list update for ongoing relationships).

---

## Regulatory Frameworks Reference

### OFAC: Key Programs

| Program | CFR Part | Primary Statute | Key Prohibition |
|---------|----------|----------------|----------------|
| Russian Harmful Foreign Activities | 31 C.F.R. Part 578 | IEEPA; E.O. 14024 | Asset freeze; all transactions with designated persons |
| Ukraine-/Russia-Related | 31 C.F.R. Part 589 | IEEPA; E.O.s 13660/13661/13662/13685/14065 | Geographic prohibition (occupied territories); SDN designations |
| Iran | 31 C.F.R. Part 560 | IEEPA; ISA; CISADA | Near-comprehensive embargo; secondary sanctions on foreign persons in key sectors |
| North Korea | 31 C.F.R. Part 510 | IEEPA; UNPA; CAATSA | Near-total embargo; secondary sanctions; maritime evasion highest-risk pattern |
| Cuba | 31 C.F.R. Part 515 | TWEA | Comprehensive embargo (TWEA-based); broad general license exceptions |
| Syria | 31 C.F.R. Part 542 | IEEPA | Comprehensive; reconstruction-sector GL available [VERIFY] |
| Venezuela | 31 C.F.R. Part 591 | IEEPA; E.O.s 13808/13850/13884 | Government entity/PDVSA restrictions; secondary sanctions risk |
| Narcotics Trafficking | 31 C.F.R. Part 598 | IEEPA; Narcotics Kingpin Act | SDN designations |
| Terrorism (SDGT) | 31 C.F.R. Part 594 | IEEPA; E.O. 13224 | SDN designations; UN 1267 implementation |

[VERIFY all program citations against current OFAC publications — programs change]

### SSI Directives 1-4 (Russia Sectoral Sanctions)

| Directive | Targeted Sector | Core Prohibition |
|-----------|----------------|-----------------|
| Directive 1 (amended) | Russian financial sector entities | New debt >14 days maturity; new equity; US person dealings with listed entities |
| Directive 2 | Russian energy sector entities | New debt >60 days maturity |
| Directive 3 | Russian defense/related materiel | New debt (any maturity); new equity transactions |
| Directive 4 | Deep-water, Arctic offshore, shale projects | Goods, services, and technology for specific project types |

[VERIFY current Directive lists and scope at ofac.treas.gov]

### CAATSA Secondary Sanctions Key Sections

| Section | Target | Trigger |
|---------|--------|---------|
| Section 228 | Persons providing significant support to OFAC-designated persons under Iran/DPRK/Russia programs | "Significant" — facts-and-circumstances; no minimum publicly disclosed |
| Section 231 | Persons conducting significant transactions with Russian defense/intelligence sector | Tier 1 (mandatory) / Tier 2 (discretionary); no bright-line threshold |
| Section 232 | Persons investing in/providing goods-services for Russian energy export pipelines | >$1M single transaction or $5M aggregate in 12 months |
| Section 233 | Foreign persons facilitating significant financial transaction for Russia energy sector SDN | Facts-and-circumstances; no bright-line threshold |

### OFAC Penalties (Reference)

| Category | Benchmark |
|----------|-----------|
| Civil maximum (most IEEPA programs) | Up to $368,136 per count [VERIFY current inflation-adjusted figure] or 2× transaction value, whichever is greater |
| Civil (certain IEEPA programs) | Statutory maximum up to $20M+ per violation under specific program provisions |
| Criminal | Up to 20 years imprisonment + $1M per violation |
| Egregious non-voluntary-disclosure reference | Binance (Nov. 2023): $968,618,825; 1,667,153 violations; 5-year external compliance monitor |

### BIS Penalties (Reference)

| Category | Benchmark |
|----------|-----------|
| Administrative maximum | $374,474 per violation [VERIFY current inflation-adjusted figure as of Jan. 2025] or 2× transaction value |
| Criminal (ECRA) | Up to 20 years imprisonment + $1M per violation |
| Landmark settlements | Applied Materials (Feb. 2026): $252M — largest BIS administrative settlement; Seagate Technology (2023): ~$300M |

### UK OFSI: Key Penalty Provisions (SI 2019/855; SAMLA 2018)

- Criminal: up to 14 years imprisonment + unlimited fine (Regulation 80, SI 2019/855) [VERIFY]
- Civil monetary penalty: maximum of £1 million or 50% of the estimated value of funds/economic resources involved — whichever is greater
- Civil standard of proof: balance of probabilities
- Voluntary disclosure is a significant mitigating factor; OFSI enforcement priorities emphasize Russia sanctions compliance (OFSI enforcement policy, March 2026) [VERIFY current guidance]

---

## Quality Frameworks

### Citation Quality Gates (Sanctions-Adapted)

Run these five gates silently before delivering any output. If any gate fails, revise before delivery.

| Gate | Rule (Sanctions/Export Control Adapted) | Fail Action |
|------|----------------------------------------|-------------|
| **Source** | Every sanctions program citation must reference a specific OFAC program regulation (31 C.F.R. Part XXX), EU Council Regulation number, UK Statutory Instrument number, or UNSC Resolution number. Every EAR citation: 15 C.F.R. Part. Every ITAR citation: 22 C.F.R. Part 120-130. Do not cite "OFAC sanctions" without naming the specific program. | Add specific citation or mark "[UNVERIFIED — confirm program regulation with sanctions counsel]" |
| **Format** | OFAC: "31 C.F.R. Part [XXX]". EAR: "15 C.F.R. Part [XXX]". ITAR: "22 C.F.R. Part [XXX]". EU: "Council Regulation (EU) No [XXX/YYYY]". UK: "SI [YYYY/NNNN]". License exceptions: cite full exception name and CFR section. | Fix format |
| **Currency** | Sanctions programs change without predictable schedule. OFAC SDN list updates multiple times per week. Every program citation and list version must be flagged as potentially outdated if not verified against current official sources. Never state a party is "designated" without noting that live-list re-verification is required before transaction proceeds. | Flag "[VERIFY CURRENT STATUS — lists updated continuously]" |
| **Domain** | Sanctions rules must not bleed across jurisdictions. OFAC clearance ≠ EU/UK clearance. OFAC general licenses do not apply to EU or UK transactions. ITAR and EAR are distinct regimes. Comprehensive program analysis (Iran, Cuba) must not be applied to targeted program analysis (Russia SSI) without qualification. | Flag and correct all jurisdiction bleed |
| **Confidence** | Consequences of both false-positive BLOCKED (blocking a legitimate transaction) and false-negative BLOCKED (missing a genuine violation) are serious. Confidence must be explicit — a 75% match score is not CLEAR; a 50% match score is not BLOCKED. Uncertainty about ECCN classification must be stated and scored, not papered over with a default. | Assign explicit confidence score; recommend action proportionate to confidence level |

### Self-Interrogation for TIER 1 and TIER 2 Findings

For any finding classified at TIER 1 (BLOCKED) or TIER 2 (HIGH RISK), apply this mandatory 3-pass review before finalizing.

**Pass 1 — Match Quality Chain**
- Is the classification based on a confirmed list match or a potential match requiring adjudication?
- Has the full set of identifying information been compared? (Name, DOB, nationality, country, registration number, address — not just name alone)
- Have transliteration variants, aliases, and alternative spellings been searched?
- Is there a documented SDN Program Code, and does it indicate an absolute prohibition or a conditional one?
- If based on the 50% Rule: has the ownership chain been traced to a confirmed SDN, or is SDN ownership only suspected?
- Could this be a common-name false positive? What corroborating identifiers are available?

**Pass 2 — Regulatory Authorization Path**
- Is there an applicable OFAC general license that would permit this transaction despite the match? [VERIFY current GLs for the applicable program — review ofac.treas.gov before finalizing BLOCKED status]
- Is there an available EAR license exception under 15 C.F.R. Part 740?
- Does a humanitarian exception, NGO exception, or personal remittance exception apply?
- Has the complete 31 C.F.R. Part for the applicable program been considered — including all authorizations and exceptions — not just the designation entry?
- Is there a specific OFAC license, BIS license application, or DDTC authorization that could authorize the transaction?

**Pass 3 — Consequence Proportionality**
- Is a TIER 1/TIER 2 determination proportionate to the quality of the match and the available evidence?
- What is the cost of a false positive (blocking a legitimate transaction) versus a false negative (missing a genuine violation)?
- Under what circumstances would a qualified sanctions attorney reviewing the same screen reach a different conclusion?
- Has the user been clearly advised that this determination is AI-assisted and requires review by qualified sanctions counsel before being acted upon?

If any pass reveals a weakness in the TIER 1/TIER 2 classification, revise to TIER 2/TIER 3 as appropriate, explain the revision, and recommend specific additional steps to resolve. Mark the audit trail: `self_interrogation: "PASS"` or `self_interrogation: "REVISED — [reason]"`.

### Confidence Scoring — Dual Scale

**Scale A: Match Confidence** (Is this party actually the listed person/entity?)

| Level | Score | Meaning | Required Action |
|-------|-------|---------|----------------|
| **Definite Match** | 0.95-1.0 | Exact name + ≥2 corroborating identifiers (DOB, country, registration number, address) | TIER 1 — BLOCKED |
| **High Confidence** | 0.80-0.94 | Strong name match + ≥1 corroborating identifier, or exact match with no identifiers available on either side | TIER 2 — Escalate before processing |
| **Possible Match** | 0.60-0.79 | Plausible name similarity; identifiers missing or ambiguous | TIER 3 — Hold; obtain additional identifiers |
| **Low Probability** | 0.40-0.59 | Name similarity but significant distinguishing identifiers that do not match | TIER 4 — Document; compliance officer review; may proceed |
| **False Positive** | 0.0-0.39 | Incidental name similarity; sufficient distinguishing identifiers confirm this is NOT the listed party | TIER 5 — Document false positive reasoning; proceed |

**Scale B: Export Classification Confidence** (Is this item controlled as classified?)

| Level | Score | Meaning | Action |
|-------|-------|---------|--------|
| **Confirmed** | 0.90-1.0 | BIS Commodity Jurisdiction ruling or manufacturer's binding classification with supporting technical documentation | Use confirmed ECCN for license determination |
| **Probable** | 0.70-0.89 | Self-classified by compliance/legal team based on CCL review with documented technical analysis | Use; flag [SELF-CLASSIFIED]; periodic review |
| **Uncertain** | 0.50-0.69 | Classification disputed or ambiguous; item could fall under multiple ECCNs or under ITAR | Do not export until confirmed; consider BIS CJ ruling request |
| **EAR99 by Elimination** | 0.40-0.69 | Appears EAR99 based on CCL review but no positive determination obtained | Acceptable for low-risk destinations; for sensitive destinations or end users, obtain positive confirmation |
| **Unclassified** | 0.0-0.39 | No classification analysis has been conducted | Do not export without classification determination |

### Four Additional Quality Gates Unique to Sanctions Screening

**Temporal Validity Gate**

Every screening result has a defined validity period. A screen conducted more than [30/90 days — per organizational policy] before transaction execution must be refreshed. Record both the screening date and the transaction execution date in the audit trail so the gap can be assessed. Flag: "[SCREEN REFRESH REQUIRED — re-screen against current live list versions before execution]"

**List Version Integrity Gate**

Every list consulted must be logged with its publication date. If the screening is based on training-data list knowledge rather than live list access, flag prominently:

> "[LIST VERSION ALERT — OFAC SDN list updates multiple times per week; EU and UK lists
> update frequently. Re-screen against current live list versions at ofac.treas.gov,
> eur-lex.europa.eu, and hmtreasury.gov.uk/ofsi before finalizing any determination.]"

**Program Scope Verification Gate**

For each applicable sanctions program, verify that the specific transaction type (financial transfer, goods export, services, investment) is covered by that program's prohibitions. Some programs prohibit financial transactions but not goods exports; some prohibit new investments but not performance of pre-existing contracts. Do not state a blanket prohibition without verifying the specific transaction type is covered by the cited regulatory provisions.

**Escalation Confirmation Gate**

For every TIER 1 or TIER 2 determination, the output must explicitly state — in a visible, standalone notice — that the determination requires review by qualified trade sanctions counsel before being acted upon. This gate is non-negotiable. AI-assisted screening cannot substitute for the legal judgment required to interpret a sanctions match in the context of the specific transaction, available licenses, and current regulatory guidance.

---

## Anti-Patterns Catalogue

What NOT to do in sanctions and export control screening — drawn from OFAC, BIS, and DDTC enforcement actions and industry guidance.

1. **Treating "not on the SDN list" as cleared.** A complete screen requires: OFAC SDN + Consolidated Sanctions Lists, EU Consolidated List, UK OFSI Consolidated List, UN consolidated lists, BIS Entity/Denied Persons/Unverified/MEU Lists, and DDTC Debarred Parties. Many enforcement actions involve parties on EU or BIS lists but not the OFAC SDN list.

2. **The 50% Rule blind spot.** Screening the counterparty entity but not tracing ownership to determine whether SDN-listed persons own ≥50% in aggregate. OFAC does not publish a list of 50%-rule-blocked entities — the obligation to trace ownership rests entirely with the screener. This is one of the most common causes of inadvertent violations.

3. **Fuzzy matching without human review.** Either exact-match-only screening (misses transliterations, aliases, and alternative spellings) or automated fuzzy matching that auto-clears all flagged items (misses genuine matches through "false positive fatigue"). Both failure modes have generated enforcement actions. Calibrated fuzzy matching with human review above a defined threshold is the required standard.

4. **Screening only the direct counterparty.** Not screening the freight forwarder, correspondent bank, shipping agent, end user, or intermediary broker. Export control violations frequently occur at intermediary nodes, not at the primary buyer level. BIS enforcement actions consistently involve clean direct counterparties with prohibited end users downstream.

5. **Clearing a match based on relationship familiarity.** "I've worked with this company for ten years — it can't be them" is not a compliance determination. Every potential match must be adjudicated using objective identifying information (DOB, country, registration number) and documented. Relationship familiarity is an aggravating factor in enforcement, not a mitigating one.

6. **Not obtaining or verifying end-use certificates.** Accepting an EUC without verification, or not requiring one at all for dual-use exports. A false EUC does not relieve exporter liability where red flags should have prompted deeper inquiry.

7. **Treating EAR99 as a blanket clearance.** EAR99 items cannot be exported to Cuba, Iran, DPRK, or Syria without a license; cannot be for WMD or terrorist end uses; and cannot go to denied parties. EAR99 means no specific ECCN on the CCL — it does not mean unrestricted.

8. **Deemed export blind spot.** Sharing EAR or ITAR-controlled technical data with a foreign national inside the United States without recognizing the deemed export obligation. Technology companies, universities, and research institutions consistently underestimate this exposure for employees and collaborators on research projects.

9. **Failing to apply the FDPR.** Assuming a foreign-manufactured item has no US nexus because it was not made in the US. The Foreign Direct Product Rule extends EAR jurisdiction to foreign-made items that are the direct product of US-origin technology or equipment — significantly expanded for Russia and Belarus military end users since April 2022. [VERIFY current FDPR scope]

10. **One-time screening at onboarding with no re-screening.** OFAC may designate an entity that a company has transacted with for years. A compliance program that only screens at onboarding misses post-onboarding designations. Re-screen on every new transaction or at minimum on each SDN list update for ongoing relationships.

11. **Ignoring transshipment and re-export red flags.** Approving an export to a "clean" destination without assessing whether goods will be re-exported to a sanctioned country. UAE, Turkey, Georgia, Kazakhstan, Armenia, and Serbia are known transshipment routes for Russia-bound controlled goods. A pattern of exports to intermediaries in these countries with no plausible local end use requires enhanced due diligence. [VERIFY current BIS/OFAC transshipment guidance]

12. **Initiating voluntary self-disclosure without counsel.** Starting an OFAC, BIS, or DDTC VSD process without first scoping the potential violation, securing privilege, and engaging external trade counsel. An incomplete or inaccurate VSD can result in a worse outcome than a properly prepared one. OFAC, BIS, and DDTC each have separate VSD procedures and mitigation credit frameworks — these are not interchangeable. [VERIFY current VSD procedures for each agency]

13. **Applying OFAC analysis to EU/UK programs without recognizing material differences.** Clearance under OFAC does not mean clearance under EU or UK sanctions. Post-Brexit, UK OFSI maintains its own independent regime. EU Russia sanctions (14 packages) are broader than OFAC's in certain areas (goods export controls); OFAC is broader in others (financial institution restrictions). Each program must be analyzed independently.

14. **Using outdated list versions.** Running a screen against an SDN list that is not the current version. OFAC updates the SDN list multiple times per week; EU and UK lists update frequently. The audit trail must document the list version date for every list consulted. Using outdated lists has been cited in enforcement actions as a program deficiency.

15. **Ignoring the "reason to know" standard.** Proceeding with a transaction despite multiple red flags on the theory that no list match was found. Under EAR Part 744 and OFAC's willful blindness standard, proceeding despite facts that should have prompted inquiry can constitute a violation even without actual knowledge. Red flags create affirmative investigation obligations — they cannot be noted and ignored.

16. **Conflating sanctions compliance with AML/KYC compliance.** A passed AML/KYC check is not a sanctions screen. An entity can pass AML risk assessment and still be SDN-listed or 50%-Rule-blocked. These are distinct legal obligations with separate required controls and distinct regulatory frameworks.

17. **Over-relying on counterparty representations.** Accepting a written representation of non-SDN status and no re-export intentions as sufficient due diligence where red flags are present. Representations shift contractual risk and may be evidence of good faith; they do not satisfy the screener's independent compliance obligations where red flags exist.

18. **Not documenting "no match" findings.** Conducting a thorough screen that finds no matches but creating no compliance record. Documentation of cleared screenings is as important as flagged screenings — a program that cannot demonstrate what was screened, when, against what list versions, and by whom cannot defend against later allegations of failure to screen.

---

## Writing Standards

Before delivering any screening report:

1. **Lead with the determination**: Start with CLEAR / HOLD / ESCALATE / DECLINE — do not bury the outcome in a narrative
2. **State all assumptions explicitly**: Any CLARIFY question skipped due to insufficient information must be listed as an explicit assumption with its consequence ("Assuming no ITAR-controlled items — if items are USML-controlled, Step 6D applies and determination may change")
3. **Mark all unverified legal references**: Use [VERIFY] on all statutory and regulatory citations not independently confirmed against current official sources
4. **Quantify confidence scores**: Do not use "likely" or "probably" without a numeric score; do not use "confirmed" without Scale A ≥0.95
5. **Avoid false precision**: A screen based on partial counterparty information should be labeled "PRELIMINARY — ADDITIONAL INFORMATION REQUIRED"; do not present a TIER 5 CLEAR when information is incomplete
6. **One finding, one record**: Each party screened and each finding (match, red flag, export control issue) should be individually recorded — not merged into a narrative that obscures individual findings
7. **Plain language for escalation notices**: ESCALATE and DECLINE notices must be written so that any recipient can act on them — not in regulatory citation form that only a trade lawyer can parse
8. **Mandatory disclaimer on every output**: Include at minimum: "AI-assisted screening — verify against current official lists before reliance"

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- In Step 4, verify current OFAC program regulations, EU Council Regulation texts, and applicable UNSC Resolutions
- In Step 6, verify current EAR Country Chart status, applicable ECCN controls, and recent BIS rulemakings (especially Russia/Belarus enhanced controls)
- Search for recent enforcement actions involving similar transaction types, industries, or counterparty jurisdictions to calibrate risk
- Verify current OFAC general license availability for the applicable program before finalizing any BLOCKED determination
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all regulatory citations [VERIFY] — particularly CFR part numbers, EU Regulation numbers, and UK SI numbers
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Emphasize live list verification against official sources: ofac.treas.gov, bis.doc.gov, ddtc.state.gov, eur-lex.europa.eu, hmtreasury.gov.uk/ofsi, un.org/securitycouncil/sanctions/un-sc-consolidated-list

---

## Output Format Template

```
SANCTIONS AND EXPORT CONTROL SCREENING REPORT
────────────────────────────────────────────────────────
Organization:        [Screening party / compliance function]
Report Date:         [YYYY-MM-DD]
Report ID:           [Unique identifier for compliance recordkeeping]
Prepared by:         AI-assisted (legalcode-sanctions-export-control-screening)
                     ⚠️ Requires review by qualified sanctions counsel before reliance
Screening Mode:      [Transaction Approval / Due Diligence / Batch / Incident Response]
Applicable Programs: [List: OFAC / EU / UK OFSI / UN / EAR / ITAR — applicable only]

⚠️  AI-ASSISTED SCREENING — VERIFY AGAINST CURRENT LIVE LIST VERSIONS BEFORE RELIANCE
────────────────────────────────────────────────────────
PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION
[Only include this header if specifically directed by counsel — confirm before adding]
```

---

### Section 1: Overall Screening Determination

```
OVERALL STATUS: [CLEAR ✅ / HOLD ⏸ / ESCALATE 🔴 / DECLINE ⛔]

Determination Summary: [1-2 sentences explaining the basis for the overall determination]

Determination Confidence: [0.X] — [one-line rationale]

List Versions Consulted:
  OFAC SDN List:         As of [DATE — VERIFY against current live version]
  EU Consolidated List:  As of [DATE — VERIFY]
  UK OFSI List:          As of [DATE — VERIFY]
  UN Consolidated List:  As of [DATE — VERIFY]
  BIS Entity List:       As of [DATE — VERIFY]
  [Others as applicable]

⚠️  These list versions reflect training data only. Re-screen against current
    official list versions before any transaction proceeds.

Screening Completed: [Timestamp UTC]
```

---

### Section 2: Party-by-Party Screening Results

```
## Party Screening Matrix

| Party | Role | Names Searched | Lists Screened | Result | Match Score | Tier | Action |
|-------|------|---------------|----------------|--------|-------------|------|--------|
| [Name] | [Counterparty / Intermediary / End User / Bank / Vessel] | [All variants searched] | [SDN / EU / UK / UN / BIS EL / BIS DPL / BIS UVL / DDTC] | [NO MATCH / POTENTIAL MATCH / CONFIRMED MATCH / 50% RULE CONCERN] | [Score or N/A] | [1-5] | [None / Hold / Decline] |

---

### Match Detail (for any result other than NO MATCH)

Party:              [Name as submitted]
Match Found:        [Name on list]
List:               [Specific list; SDN program code if applicable]
Match Score:        [X%] — [methodology: exact / alias / transliteration / fuzzy]
SDN Program Code:   [e.g., RUSSIA, IRAN, SDNT — indicates treatment and relevant GL search]
Confidence (Scale A): [0.X]
Distinguishing Information:
  DOB on list:         [From list entry]
  DOB of party:        [Known / Unknown]
  Country on list:     [From list entry]
  Country of party:    [As submitted]
  Aliases on list:     [From list entry]
  Registration no.:    [If available on either side]
Recommendation:     [CONFIRM MATCH — DECLINE / LIKELY FALSE POSITIVE — DOCUMENT AND CLEAR /
                    REQUIRES ADDITIONAL INFORMATION TO RESOLVE]

50% Rule Analysis:
  UBOs identified:   [Yes — [detail] / No — ownership investigation required]
  SDN ownership:     [NONE IDENTIFIED / POTENTIAL — [detail] / CONFIRMED ≥50% — BLOCKED]
  Aggregate SDN %:   [X% or UNKNOWN]
```

---

### Section 3: Program-by-Program Analysis

```
## OFAC Analysis
SDN List:            [CLEAR / POTENTIAL MATCH / CONFIRMED MATCH] — [Detail]
Consolidated List:   [CLEAR / POTENTIAL MATCH / CONFIRMED MATCH] — [Detail]
SSI Directives:      [APPLICABLE / NOT APPLICABLE] — [Directive and sector if applicable]
Country Program:     [Program name and 31 C.F.R. Part] [VERIFY] — [CLEAR / PROHIBITED]
50% Rule:            [COMPLETED — CLEAR / REQUIRES OWNERSHIP VERIFICATION / BLOCKED]
General License:     [Not required / GL [X] applies (cite and verify) / Specific license required / None available]

## EU Sanctions Analysis
EU Consolidated:     [CLEAR / POTENTIAL / CONFIRMED] — [Detail]
Applicable Reg:      [Council Regulation (EU) No XXX/YYYY] [VERIFY]
Asset Freeze:        [APPLICABLE / NOT APPLICABLE]
Authorization:       [Not required / Competent authority authorization required / None available]

## UK OFSI Analysis
UK Consolidated:     [CLEAR / POTENTIAL / CONFIRMED] — [Detail]
Applicable SI:       [SI YYYY/NNNN] [VERIFY]
Asset Freeze:        [APPLICABLE / NOT APPLICABLE]
OFSI License:        [Not required / General license available / Specific license required]

## UN Sanctions Analysis
UN Consolidated:     [CLEAR / POTENTIAL / CONFIRMED] — [Detail]
Resolution(s):       [UNSCR XXXX (program)] [VERIFY]

## EAR Export Control (if applicable)
ECCN:                [ECCN number / EAR99 / Unclassified — requires determination] [SELF-CLASSIFIED / VERIFY]
Classification Basis: [Self / Manufacturer confirmation / BIS CJ ruling]
Classification Conf:  [Scale B score]
License Required:    [Yes — [Country] under [Control Reason] / No / Exception applies]
License Exception:   [Full exception name and § XXX] [VERIFY] / [No exception available]
Entity List:         [CLEAR / FLAGGED — detail]
MEU Rule (§ 744.21): [Applicable / Not applicable] — [detail if applicable]
FDPR:                [Applicable / Not applicable] [VERIFY current FDPR scope]
Russia/Belarus:      [Enhanced controls applicable / Not applicable] [VERIFY]

## ITAR Analysis (if applicable)
USML Classification: [Category if applicable / Not USML / Requires DDTC determination] [VERIFY]
License Required:    [Not required / DSP-5 required / TAA required / Other] [VERIFY]
Deemed Export:       [Not applicable / Assessed — [detail]]
TAA/MLA Required:    [Yes — [detail] / No]
```

---

### Section 4: Red Flag Assessment

```
## Red Flag Summary

| Category | Indicator Present? | Tier | Finding |
|----------|--------------------|------|---------|
| Payment routing anomalies | Y / N / Unclear | [1-5] | [Detail] |
| Beneficial ownership opacity | Y / N / Unclear | [1-5] | [Detail] |
| End-user mismatch | Y / N / Unclear | [1-5] | [Detail] |
| Transshipment risk | Y / N / Unclear | [1-5] | [Detail] |
| Product-buyer mismatch | Y / N / Unclear | [1-5] | [Detail] |
| Documentation gaps | Y / N / Unclear | [1-5] | [Detail] |
| Pricing anomaly | Y / N / Unclear | [1-5] | [Detail] |
| Urgency or secrecy | Y / N / Unclear | [1-5] | [Detail] |
| Prior compliance concerns | Y / N / Unclear | [1-5] | [Detail] |

Aggregate Red Flag Level: [NONE / LOW / ELEVATED / HIGH / CRITICAL]
```

---

### Section 5: Recommended Next Steps

```
## Next Steps

### IMMEDIATE (before transaction proceeds)
1. [Specific action — e.g., "Resolve potential SDN match for [Name] before authorizing payment"]

### REQUIRED FOR COMPLETION (if HOLD status)
1. [Information needed — e.g., "Obtain UBO disclosure from counterparty to complete 50% Rule analysis"]

### COMPLIANCE RECORD ACTIONS
☐ File this screening report in the compliance record for this transaction
☐ Re-screen at [interval] or upon next SDN/EU/UK list update before transaction executes
☐ Obtain and retain end-use certificate / end-user statement
☐ Obtain and retain beneficial ownership disclosure
☐ Confirm license exception or general license authority in writing before export

### VOLUNTARY SELF-DISCLOSURE CONSIDERATION
If a potential violation has been identified during this screen:
- OFAC VSD: ofac.feedback@treasury.gov (∼50% base penalty reduction under OFAC guidelines) [VERIFY current process]
- BIS VSD: BIS Office of Export Enforcement [VERIFY current VSD procedure and contact]
- DDTC VSD: State Department DDTC [VERIFY current VSD procedure and contact]
Engage external trade counsel before initiating any VSD process.

### ESCALATION PATH (if ESCALATE or DECLINE)
First:     Compliance Officer / Legal
Second:    General Counsel / Chief Compliance Officer
External:  Trade sanctions counsel (required for all DECLINE determinations and VSD)
```

---

### Section 6: Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-sanctions-export-control-screening"
  screening_date: "[YYYY-MM-DD HH:MM UTC]"
  report_id: "[Unique identifier]"
  legalcode_mcp: "[Connected — citations verified / Not connected — [VERIFY] tags applied throughout]"

  applicable_programs: ["OFAC", "EU", "UK OFSI", "UN", "EAR", "ITAR"]  # list applicable only

  parties_screened:
    - name: "[Name as submitted]"
      role: "[Counterparty / Intermediary / End User / Vessel / etc.]"
      variants_searched: ["[variant 1]", "[variant 2 — transliteration]", "[alias]"]
      lists_consulted: ["OFAC SDN", "OFAC Consolidated", "EU", "UK OFSI", "UN", "BIS EL", "BIS DPL", "BIS UVL", "DDTC"]
      list_versions: {ofac_sdn: "[date — VERIFY]", eu: "[date — VERIFY]", uk_ofsi: "[date — VERIFY]", un: "[date — VERIFY]", bis_el: "[date — VERIFY]"}
      match_result: "[NO MATCH / POTENTIAL / CONFIRMED / 50% RULE CONCERN]"
      match_confidence_scale_a: "[0.XX or null]"
      fifty_percent_rule:
        checked: "[true / false]"
        ubo_information: "[Available / Requested — pending / Not available]"
        result: "[CLEAR / OWNERSHIP RISK — investigation required / BLOCKED — confirmed ≥50% SDN]"
        reasoning: "[Brief]"

  export_control:
    applicable: "[true / false]"
    item_description: "[Brief]"
    eccn: "[Number / EAR99 / UNCLASSIFIED — requires determination]"
    classification_basis: "[Self / Manufacturer confirmation / BIS CJ ruling]"
    classification_confidence_scale_b: "[0.XX]"
    license_required: "[true / false / null]"
    license_exception: "[Exception name and CFR section / None / N/A]"
    itar_assessed: "[true / false]"
    usml_classification: "[Category / Not USML / DDTC determination required]"
    fdpr_assessed: "[true / false]"
    deemed_export_assessed: "[true / false]"

  red_flags:
    total_assessed: "[N]"
    flags_present: "[N]"
    aggregate_level: "[NONE / LOW / ELEVATED / HIGH / CRITICAL]"

  citation_quality_gates:
    source: "[PASS / FAIL — detail]"
    format: "[PASS / FAIL — detail]"
    currency: "[PASS — noted as training data requiring live verification / FAIL — detail]"
    domain: "[PASS / FAIL — detail]"
    confidence: "[PASS / FAIL — detail]"

  additional_quality_gates:
    temporal_validity: "[PASS / FLAG — re-screen required before execution]"
    list_version_integrity: "[PASS / FLAG — live list verification required]"
    program_scope_verification: "[PASS / FAIL — detail]"
    escalation_confirmation: "[PASS — included in output / FAIL]"

  self_interrogation:
    tier1_tier2_count: "[N]"
    applied: "[true / false]"
    result: "[CONFIRMED / REVISED — reason for revision]"

  overall_determination: "[CLEAR / HOLD / ESCALATE / DECLINE]"
  determination_confidence: "[0.X]"
  counsel_review_required: "[true / false]"
  determination_rationale: "[One-line justification]"

  limitations:
    - "List versions reflect training data only — verify against current live lists before reliance"
    - "[Any scope limitations, missing information, or assumptions made during screening]"

  reviewer: "AI-assisted — requires review by qualified trade sanctions counsel before reliance"
```

---

## Localization Notes

**United States (OFAC / EAR / ITAR)**: The most comprehensive sanctions and export control framework with the broadest jurisdictional reach. US nexus is broad — USD clearing and US-origin goods create nexus even for transactions between non-US parties. IEEPA provides broad executive authority; program-specific 31 C.F.R. parts govern each program's prohibitions and authorizations. EAR and ITAR are separate regimes; the boundary between them is a frequent source of compliance risk (600-series ECCNs reflect items moved from USML to CCL under Export Control Reform).

**European Union**: EU sanctions are directly applicable in all 27 member states via Council Regulations. Each member state has a competent authority for licensing derogations. The EU Consolidated List is maintained by EEAS. Post-Brexit, UK and EU lists diverge — a party on the EU list may not appear on the UK list and vice versa. EU Russia sanctions (14 packages through July 2024) include goods export controls that in certain areas exceed OFAC's scope. [VERIFY current EU package status]

**United Kingdom**: SAMLA 2018 provides the independent post-Brexit sanctions architecture. UK OFSI operates separately from HMRC and ECJU (export controls). The Russia (Sanctions) (EU Exit) Regulations 2019 (SI 2019/855) have been amended multiple times since Brexit — verify the current amended version. OFSI enforcement has become increasingly active: monetary civil penalties, enforcement policy updates, and prosecution referrals have all increased since 2022. [VERIFY current OFSI enforcement posture]

**United Nations**: UN SCSC lists are mandatory floors for all 193 UN member states. UN lists are generally incorporated by reference into EU, UK, and US programs, but the UN list should be screened independently to capture the universal baseline that applies regardless of national autonomous sanctions programs.

**ITAR/EAR Distinction**: Many items were moved from USML to CCL (600-series ECCNs) under Export Control Reform (ECR). Items bearing 600-series ECCNs are often subject to stricter EAR controls than other CCL items. When jurisdiction is genuinely unclear, err toward ITAR and seek a DDTC Commodity Jurisdiction (CJ) determination.

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis. Produced via 2-agent research pipeline (Structural Analyst + Prompt Engineering Analyst) with web-backed legal research.

**Legal framework coverage**: IEEPA (50 U.S.C. §§ 1701-1707); ECRA (50 U.S.C. §§ 4801-4852); AECA (22 U.S.C. § 2778); TWEA (50 U.S.C. § 4301 et seq.); UNPA (22 U.S.C. § 287c); CAATSA (Pub. L. 115-44) Sections 228/231/232/233; CISADA Section 104; PEESA; SAMLA 2018; 31 C.F.R. Chapter V (all OFAC program regulations); 15 C.F.R. Parts 730-774 (EAR); 22 C.F.R. Parts 120-130 (ITAR); TFEU Art. 215; Council Reg. 269/2014 (Russia asset freezes); Council Reg. 833/2014 (Russia sectoral, 14 packages); SI 2019/855 (UK Russia Sanctions); UN Charter Chapter VII; UNSCR 1267 (ISIL/Al-Qaeda), 1988 (Taliban), 1718 (DPRK), 1970 (Libya).

**Enforcement data**: OFAC enforcement actions 2023-2026 (Binance $968M; IMG Academy $1.72M; TradeStation $1.1M); BIS enforcement (Applied Materials $252M, Seagate ~$300M); DDTC consent agreements; UK OFSI enforcement policy paper (March 2026).

**Industry guidance**: Wolfsberg Group sanctions screening guidance; ACAMS best practices; OFAC compliance framework (2019); OFAC FAQ 174 (50% Rule); BIS Export Compliance Guidelines.

All statutory and regulatory references should be verified against current official sources before reliance. Laws, regulations, and designations change continuously in this area.
