---
name: legalcode-uk-prospectus-and-fca-offering-compliance
description: 'Reviews UK capital raising and securities offering compliance across the full regulatory
  stack: the Public Offers and Admissions to Trading Regulations 2024 (POATR 2024, in force 19 January
  2026), FSMA 2000 s.21 financial promotion restriction, FCA Financial Promotion Gateway (from 7 February
  2024), COBS 4 financial promotion rules, public-offer exemptions (£5 million de minimis, 150-person,
  qualified investor, Public Offer Platform), sophisticated-investor and high-net-worth pathways under
  the FPO 2005 (Articles 19, 48, 50, 50A), AIM/Main Market sensitivities under UKLR 2024 and AIM Rules,
  MTF admission prospectus obligations, offering document risk factor standards, Protected Forward-Looking
  Statements (PFLS), PISCES disclosure requirements, and cross-border UK/EU marketing boundaries including
  National Private Placement Regimes (NPPRs).'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews UK capital raising and securities offering compliance across the full regulatory stack: the Public Offers and Admissions to Trading Regulations 2024 (POATR 2024, in force 19 January 2026), FSMA 2000 s.21 financial promotion restriction, FCA Financial Promotion Gateway (from 7 February 2024), COBS 4 financial promotion rules, public-offer exemptions (£5 million de minimis, 150-person, qualified investor, Public Offer Platform), sophisticated-investor and high-net-worth pathways under the FPO 2005 (Articles 19, 48, 50, 50A), AIM/Main Market sensitivities under UKLR 2024 and AIM Rules, MTF admission prospectus obligations, offering document risk factor standards, Protected Forward-Looking Statements (PFLS), PISCES disclosure requirements, and cross-border UK/EU marketing boundaries including National Private Placement Regimes (NPPRs). Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE gap analysis with IMMEDIATE / NEAR-TERM / BACKGROUND remediation tiers, investor qualification pathway map, FP approval checklist, Glass Box audit trail, and anti-pattern catalogue. Use when assessing a proposed capital raise (equity or debt), reviewing marketing materials, designing an offering structure, preparing for AIM admission or Main Market IPO, stress- testing investor qualification procedures, auditing financial promotion approvals, or evaluating cross-border UK/EU marketing programmes. Applies to UK issuers, overseas issuers seeking UK capital markets access, FCA-authorised firms approving third-party promotions, Nominated Advisers (Nomads), sponsors, and legal and compliance teams advising on UK securities law. Jurisdiction: England and Wales under FSMA 2000 (as amended by FSMA 2023), POATR 2024, and FCA Handbook. Scotland and Northern Ireland share the same statutory framework; separate Scots law and Northern Ireland procedural considerations apply in litigation contexts.


# UK Prospectus and FCA Offering Compliance

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance with
> UK securities offering and financial promotion regulation. It does not constitute legal
> advice, regulatory guidance, or a compliance certification. The UK prospectus and financial
> promotion regime is in a period of substantial reform (POATR 2024 came into force 19 January
> 2026; UKLR 2024 took effect 29 July 2024; the Financial Promotion Gateway from 7 February
> 2024); rules are evolving rapidly and require verification against current primary and
> secondary legislation, FCA Handbook, and FCA policy statements. All statutory references,
> thresholds, case law citations, and regulatory guidance cited here carry hallucination risk
> — verify against legislation.gov.uk, fca.org.uk/handbook, and primary legislation before
> relying on them. This skill does not replace advice from a qualified solicitor, barrister,
> or FCA-authorised compliance professional. FCA enforcement priorities and interpretive
> positions evolve; verify current FCA expectations before use. No analysis herein constitutes
> a legal opinion on whether a particular offering is lawful.

---

## Purpose and Scope

This skill assesses the compliance of a UK capital raising, securities offering, or financial
promotion programme against the current UK regulatory framework. It identifies gaps, classifies
their severity, and produces a prioritised remediation roadmap with practical structuring
recommendations.

**Covers:**

- **POATR 2024 framework** (in force 19 January 2026): General prohibition analysis,
  exemption mapping, Public Offer Platform (POP) route, PISCES, secondary issuance thresholds
- **FCA financial promotion controls**: FSMA 2000 s.21 restriction, Financial Promotion
  Gateway (FPR, s.55NA FSMA), COBS 4, high-risk investment promotion rules (RMMI/NMMI),
  cryptoasset financial promotions, social media guidance (FG24/1)
- **Investor qualification frameworks**: FPO 2005 Articles 19, 48, 50, 50A — investment
  professionals, HNW individuals, certified sophisticated, self-certified sophisticated
- **AIM sensitivities**: AIM Rules for Companies, Nomad obligations, MTF admission
  prospectus (post-POATR 2024), AIM Rule 26 corporate governance, AIM disciplinary risk
- **Main Market (UKLR 2024)**: ESCC eligibility, sponsor obligations, dual-class share
  structures, significant transactions, related party transactions
- **Offering document risk factors**: Specificity, materiality, categorisation, PFLS
  interaction, climate/ESG risk factor requirements
- **Protected Forward-Looking Statements (PFLS)**: Scope, liability standard, labelling
  requirements
- **Cross-border UK/EU marketing**: No prospectus passporting, NPPR framework for AIFs,
  reverse solicitation limits, EEA country-by-country private placement, EU marketing of
  UK securities, UK marketing of EU securities
- **Severity classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL EXPOSURE
- **Remediation tiers**: IMMEDIATE / NEAR-TERM / BACKGROUND
- **Glass Box audit trail**

**Does not:**

- Provide a legal opinion on whether a specific offering is lawful — that requires qualified
  legal counsel
- Fully assess PRA prudential requirements for dual-regulated firms (banks, insurers)
- Replace the firm-specific FCA Handbook analysis required for s.19 FSMA authorisation
  (see `legalcode-uk-fca-regulatory-compliance`)
- Cover US securities law (Reg D, Reg S) — use jurisdiction-specific US skill
- Apply to CREST depositary interests, warrants, or specialist securities without adaptation
- Assess personal liability of individual directors for prospectus inaccuracies under POATR
  2024 s.8 (requires separate legal opinion)

**Related skills:**

- `legalcode-uk-fca-regulatory-compliance` — full FCA Handbook compliance assessment
- `legalcode-uk-bribery-act-compliance` — Bribery Act 2010 adequate procedures; use
  alongside this skill for cross-border offering due diligence
- `legalcode-eu-prospectus-regulation` — EU 2017/1129 regime for EEA offerings
- `legalcode-venture-financing-uk` — VC financing structuring and term sheet review

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: England and Wales under:

- **Financial Services and Markets Act 2000 (FSMA 2000)** as substantially amended by
  the Financial Services and Markets Act 2023 (FSMA 2023)
- **The Public Offers and Admissions to Trading Regulations 2024 (POATR 2024,
  SI 2024/105)** — in force 19 January 2026
- **The Financial Services and Markets Act 2000 (Financial Promotion) Order 2005
  (FPO 2005, SI 2005/1529)** as amended
- **FCA Handbook** — in particular COBS 4, the Prospectus Rules: Admissions to Trading
  on a Regulated Market (PRM) Sourcebook, UKLR, and MAR
- **AIM Rules for Companies and AIM Rules for Nominated Advisers** (London Stock Exchange)

**Geographic scope**: UK-wide for FCA and FSMA purposes. Scotland and Northern Ireland:
same statutory framework; separate procedural routes for regulatory referral and court
proceedings.

**Cross-border scope**: Where a UK offering has EU distribution elements, assess EU member
state national law requirements separately — no equivalence or passporting exists
between UK and EU prospectus regimes post-Brexit.

**Temporal note**: The UK prospectus regime is in active transition. Key effective dates:

- 29 July 2024: UKLR 2024 replaced old premium/standard listing regime
- 7 February 2024: Financial Promotion Gateway (s.55NA FSMA) operational
- 8 October 2023: Cryptoasset financial promotions brought within FPO/COBS regime
- 19 January 2026: POATR 2024 fully in force, replacing UK Prospectus Regulation

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The offering structure is ambiguous and the choice changes the applicable regulatory
  pathway
- Threshold calculations could be made in multiple ways
- The user's investor base mix is unclear (affects both FPO and prospectus exemption analysis)
- AIM vs. Main Market vs. private placement pathway choices require user input

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

### Step 1: Accept the Offering

Accept the offering description in any of these formats:

- **Term sheet or offering memorandum**: Document describing the securities, the issuer,
  and the proposed offer
- **Draft prospectus or admission document**: Full or draft offering document for review
- **Deal description**: Free-text description of the proposed offering structure
- **Financial promotion**: Marketing material (slide deck, website, social media content,
  investor communication) for financial promotion assessment
- **Compliance questionnaire**: Pre-filled Q&A about the offering for gap analysis

If insufficient information is provided to assess the offering structure, proceed to
Step 2 clarification questions before analysis.

### Step 2: Gather Offering Context

**⟁ CLARIFY** — Before beginning the assessment, ask the user:

1. **Offering type**: What kind of capital raise is this?
   - Options: IPO (Main Market / UKLR), IPO (AIM), Secondary issuance (listed company),
     Private placement (unlisted), Public offer via POP route, Debt offering (investment
     grade), Debt offering (high-yield), PISCES secondary liquidity event, Financial
     promotion approval only (no new issuance)
   - _Why this matters_: Determines which regulatory pathway (POATR, UKLR, AIM Rules,
     or financial promotion rules only) is primary.

2. **Issuer status**: What is the current status of the issuer?
   - Options: UK-incorporated private company, UK-incorporated public company (unlisted),
     AIM-admitted company, Main Market (UKLR)-admitted company, Overseas company
     (specify domicile), Fund / collective investment scheme, AIFM / fund manager
   - _Why this matters_: Different rules apply based on whether the issuer is already
     admitted to a market.

3. **Target investor base**: Who are the intended investors?
   - Options: Qualified investors only (institutional), Sophisticated investors (Articles
     50 / 50A FPO), High-net-worth individuals (Article 48 FPO), Investment professionals
     only (Article 19 FPO), Retail investors (general public), Mixed (specify proportions)
   - _Why this matters_: Determines which FPO exemptions apply and whether RMMI/NMMI
     rules are engaged.

4. **Offer size**: What is the total consideration being raised?
   - Amount in GBP. Specify whether this is the current tranche or the aggregate over
     12 months.
   - _Why this matters_: The £5 million threshold determines whether the POATR de minimis
     exemption applies; above £5 million requires a POP or another qualifying exemption.

5. **Distribution geography**: Where will the offer be marketed?
   - Options: UK only, UK + EU (specify EEA member states), UK + US, UK + other (specify),
     Global (specify key jurisdictions)
   - _Why this matters_: EU distribution requires country-by-country EEA assessment; no
     prospectus passporting exists between UK and EU.

6. **Review scope**: What is the primary objective?
   - Options: Full compliance assessment (all regulatory pathways), Financial promotion
     review only (marketing materials), Prospectus / offering document review, Investor
     qualification pathway design, AIM/Main Market admission readiness, Cross-border
     marketing boundary assessment
   - _Why this matters_: Scopes the analysis to the user's priority need.

If the user provides partial context, state assumptions explicitly and flag them in the
Glass Box audit trail.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to build a working legal reference for this review.
Search for:

- Current POATR 2024 text and FCA PRM Sourcebook rules
- Relevant FSMA 2000 provisions (ss.19, 21, 25, 30, 55NA, 86, 87)
- FPO 2005 Articles 19, 48, 50, 50A — current thresholds and statement requirements
- COBS 4 financial promotion rules (latest version)
- AIM Rules for Companies (current version, including 2025 reform derogations)
- UKLR 2024 relevant provisions
- FCA Final Notices and Dear CEO letters on prospectus and financial promotion failures
- Recent FCA enforcement data on financial promotion breaches

Save results to `/tmp/legalcode-uk-prospectus-research.md`.

**If legalcode-mcp is not connected**: Mark all statutory references with [VERIFY] and
note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`.

### Step 4: Map the Regulatory Pathways

Before conducting detailed analysis, map the applicable regulatory pathways for this
offering. This determines which assessment modules to prioritise.

**Decision tree — prospectus / admission requirement:**

```
Is the offering of "relevant securities" to the public in the UK? (POATR 2024)
│
├── NO (e.g., private fundraising from a single investor, purely internal restructuring)
│   └── No POATR prospectus requirement — assess s.21 FSMA financial promotions only
│
└── YES — Is an exemption available?
    │
    ├── Qualified investors only (all investors are QIs)?
    │   └── EXEMPT — No prospectus needed — assess s.21 FSMA separately
    │
    ├── Fewer than 150 persons (excluding QIs)?
    │   └── EXEMPT — No prospectus needed — assess s.21 FSMA separately
    │
    ├── Total consideration < £5 million over 12 months?
    │   └── EXEMPT — No prospectus needed — assess s.21 FSMA separately
    │
    ├── Via a registered Public Offer Platform (POP)?
    │   └── EXEMPT from prospectus — POP operator obligations apply
    │
    ├── Offer to existing shareholders of private company?
    │   └── EXEMPT — assess s.21 FSMA separately
    │
    ├── Employee / director exemption applies?
    │   └── EXEMPT — assess s.21 FSMA separately
    │
    ├── Securities admitted / conditional on admission to regulated market or primary MTF?
    │   ├── Main Market (regulated market): FCA-approved prospectus required (PRM Sourcebook)
    │   └── AIM (primary MTF): MTF admission prospectus required (LSE-validated, not FCA)
    │
    └── No exemption applies?
        └── CRITICAL EXPOSURE — Offer is PROHIBITED; no prospectus can cure non-compliance
```

**Decision tree — financial promotion (s.21 FSMA):**

```
Is the communication an "invitation or inducement to engage in investment activity"?
│
├── NO → No s.21 restriction applies
│
└── YES — Who is communicating it?
    │
    ├── Authorised person (own promotion) → Subject to COBS 4 only
    │
    ├── Authorised person (approving third-party promotion)
    │   └── Does the firm have FP Gateway permission (s.55NA)? [From 7 Feb 2024]
    │       ├── YES → May approve; ongoing COBS 4 obligations apply
    │       └── NO → CRITICAL EXPOSURE — Cannot approve; criminal offence risk
    │
    └── Unauthorised person → Does an FPO 2005 exemption apply?
        │
        ├── Article 19 (Investment professionals): all recipients investment professionals?
        ├── Article 48 (HNW): individuals certified with £100k income / £250k net assets?
        ├── Article 50 (Sophisticated): individuals hold authorised-person certificate?
        ├── Article 50A (Self-certified sophisticated): individuals meet Article 50A criteria?
        └── No FPO exemption? → CRITICAL EXPOSURE — s.25 criminal offence; s.30 civil
                                  consequence (unenforceable agreement + right to recover)
```

**⟁ CLARIFY** — If the decision tree reveals an ambiguity (e.g., offer is borderline on
the 150-person count, or investor qualification is mixed), ask the user to confirm:

- "Your investor list appears to include [X] persons who may not qualify as QIs, HNW, or
  sophisticated. Does this change the intended investor qualification approach?"
- "The aggregate consideration for this tranche and prior tranches over the last 12 months
  appears to approach the £5 million threshold. Please confirm the total."

### Step 5: POATR 2024 Prospectus / Admission Assessment

Assess the offering against the POATR 2024 framework and FCA PRM Sourcebook.

#### 5a. General Prohibition Analysis

| Issue                                      | Status | Finding | Severity |
| ------------------------------------------ | ------ | ------- | -------- |
| Does a general prohibition apply?          |        |         |          |
| Is an exemption clearly established?       |        |         |          |
| Aggregation risk (12-month rolling total)  |        |         |          |
| Is the offering structure POATR-compliant? |        |         |          |

**Critical POATR 2024 departure from old regime**: A prospectus **cannot cure** a non-
compliant public offer. If no exemption applies, the offer is prohibited regardless of
any prospectus published. Confirm the exemption basis BEFORE approving any offer marketing.

#### 5b. Prospectus Content Assessment (if a prospectus is required)

Assess each required section against PRM Sourcebook requirements:

| Section                                                      | Required?              | Present? | Quality | Gaps |
| ------------------------------------------------------------ | ---------------------- | -------- | ------- | ---- |
| Summary (max 10 pages)                                       | Equity: yes / Debt: no |          |         |      |
| Risk factors (specific, material, categorised)               | Yes                    |          |         |      |
| Information about the issuer                                 | Yes                    |          |         |      |
| Financial information (historical)                           | Yes                    |          |         |      |
| Business description                                         | Yes                    |          |         |      |
| Capital structure and major shareholders                     | Yes                    |          |         |      |
| Related party transactions                                   | Yes                    |          |         |      |
| Persons responsible / liability statement                    | Yes                    |          |         |      |
| PFLS labelling (if applicable)                               | If PFLS present        |          |         |      |
| Climate/ESG disclosure (equity issuers with transition plan) | Conditional            |          |         |      |
| Working capital statement                                    | Equity: yes            |          |         |      |
| Dilution section (secondary offers)                          | Conditional            |          |         |      |

**Secondary issuance threshold check** (for already-admitted companies):

- Threshold under POATR 2024: New securities > **75%** of existing fungible securities
  (over 12 months) → prospectus required
- Closed-ended investment funds: **100%** threshold (no prospectus required for further
  issuances)
- Compare with old regime (20%) — the significantly higher threshold means many fundraises
  that previously required a prospectus no longer do

#### 5c. MTF Admission Prospectus — AIM-Specific

For AIM offerings:

- Confirm MTF admission prospectus is required (IPO or reverse takeover)
- Note: FCA does not approve MTF admission prospectuses — LSE (as AIM operator) validates
- Secondary fundraises by existing AIM companies: LSE has confirmed these do not require
  an MTF prospectus
- New share class admission: AIM companies no longer required to publish an admission
  document for a new class of securities [VERIFY current AIM Rules text]

#### 5d. Public Offer Platform (POP) Assessment

If the POP route is proposed for an offer above £5 million:

| Checkpoint                                                                        | Status |
| --------------------------------------------------------------------------------- | ------ |
| Is the POP operator FCA-registered?                                               |        |
| Has due diligence been conducted on the issuer by the POP operator?               |        |
| Has the POP operator assessed issuer financial resources for 6 months post-offer? |        |
| Investor disclosure summary prepared by POP operator?                             |        |
| Equality of information rule applied (for exempted offers > £1m)?                 |        |

#### 5e. PISCES Assessment (if applicable)

If the transaction involves secondary trading on PISCES:

| Checkpoint                                                                       | Status |
| -------------------------------------------------------------------------------- | ------ |
| PISCES operator approved by FCA?                                                 |        |
| Core information pack prepared (3-yr financials, management, capital structure)? |        |
| Risk factors included in information pack?                                       |        |
| Material contracts and 25%+ shareholders disclosed?                              |        |
| Trading limited to professional/institutional investors and employees?           |        |
| Stamp duty exemption confirmed?                                                  |        |
| EMI/CSOP tax treatment assessed?                                                 |        |

### Step 6: Financial Promotion Assessment

Assess all offering-related communications against FSMA 2000 s.21 and COBS 4.

#### 6a. Gateway Compliance (FP Approval — Post 7 February 2024)

| Issue                                                                                                | Status | Severity if Failing |
| ---------------------------------------------------------------------------------------------------- | ------ | ------------------- |
| Promotion communicator: authorised person, or unauthorised?                                          |        |                     |
| If authorised person approving third-party promotion: does firm have FP Gateway permission (s.55NA)? |        | CRITICAL            |
| If approving: adequate systems and controls in place?                                                |        | NON-COMPLIANT       |
| If approving: ongoing monitoring for lifetime of communication?                                      |        | NON-COMPLIANT       |
| If approving: competence/expertise in the product approved?                                          |        | NON-COMPLIANT       |
| Is the FPO 2005 exemption pathway properly documented?                                               |        | PARTIAL             |

#### 6b. COBS 4 Fair, Clear and Not Misleading Test

Assess each marketing communication:

| Standard                                                                         | Assessment | Issues Found |
| -------------------------------------------------------------------------------- | ---------- | ------------ |
| **Fair**: Balanced presentation of risks and benefits?                           |            |              |
| **Clear**: Appropriate level of complexity for audience?                         |            |              |
| **Not misleading**: No false impressions of performance, returns, or protection? |            |              |
| Prominent, prominent, prominent risk warnings (COBS 4.5A for retail)?            |            |              |
| Risk warnings not undermined by design, colour, or placement?                    |            |              |
| Past performance disclaimers where past performance cited?                       |            |              |
| Forecasts clearly labelled and not presented as guaranteed returns?              |            |              |

#### 6c. RMMI / NMMI Compliance (High-Risk Investments)

Determine the investment category:

| Category     | Securities Type                                                         | Key Rule                                                                                                                        |
| ------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **RMMI**     | Unlisted shares/bonds, P2P, cryptoassets                                | May be promoted to retail; mandatory risk warning; ban on inducements; positive frictions; appropriateness; 24-hour cooling-off |
| **NMMI**     | Unauthorised funds, speculative mini-bonds, certain structured products | Cannot be mass marketed; restricted to Art. 50/50A/HNW only                                                                     |
| **Standard** | Listed securities, regulated funds                                      | COBS 4 fair/clear/not misleading; no special RMMI/NMMI rules                                                                    |

**For RMMI promotions — checklist:**

| Requirement                                                                | Status | Finding |
| -------------------------------------------------------------------------- | ------ | ------- |
| Prescribed risk warning included verbatim? ("Don't invest unless...")      |        |         |
| Monetary/non-monetary inducements to invest prohibited?                    |        |         |
| Positive friction implemented (investor must confirm risk warning read)?   |        |         |
| Client categorisation documented before promotion shown?                   |        |         |
| Appropriateness assessment required for direct offer financial promotions? |        |         |
| 24-hour cooling-off period implemented for new investors?                  |        |         |

#### 6d. Social Media and Digital Promotions

| Requirement                                                         | Status | Finding |
| ------------------------------------------------------------------- | ------ | ------- |
| Promotions clearly identifiable as such ("ad" / "promotion" label)? |        |         |
| Risk warning on every slide of story/carousel formats?              |        |         |
| Emoji-only risk communication avoided?                              |        |         |
| Platform character limits do not excuse omission of risk warnings?  |        |         |
| Finfluencer/affiliate responsibility chain documented?              |        |         |
| Firm has systems to monitor affiliate and influencer promotions?    |        |         |

#### 6e. Cryptoasset Promotions (if applicable)

| Requirement                                                                                                                                          | Status | Finding |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------- |
| Qualifying cryptoassets classified as RMMI?                                                                                                          |        |         |
| All RMMI rules applied to crypto promotions?                                                                                                         |        |         |
| FCA registration/authorisation of issuer confirmed, or promotions approved by FCA-registered approver with gateway permission covering cryptoassets? |        |         |
| FG23/3 guidance reviewed for real-time communications and social media?                                                                              |        |         |

### Step 7: Investor Qualification Assessment

Map the investor base against FPO 2005 exemptions and POATR 2024 prospectus exemptions.

#### 7a. FPO 2005 Exemption Pathway Map

| Article      | Exemption                    | Qualifying Criteria                                                                                                                                                                                                                                            | Procedure                                                                                                        | Pitfalls                                                                                                                                               |
| ------------ | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Art. 19**  | Investment professionals     | Authorised persons, exempt persons, overseas regulated persons, governments/central banks, listed companies (own securities only), those with professional investment capacity                                                                                 | Communication must be incapable of reaching non-professionals                                                    | Catch-all "investment professional" designation without verification; mixing retail with institutional lists                                           |
| **Art. 48**  | HNW individuals              | Income ≥ **£100,000** in last FY; OR net assets ≥ **£250,000** (excl. primary residence, pension, life insurance); statement signed within last 12 months                                                                                                      | Business must collect and retain signed statement; enhanced disclosures: business address, contact, registration | Failing to re-collect annually; using expired statements; net assets calculation including excluded assets                                             |
| **Art. 50**  | Certified sophisticated      | Current certificate signed by an **authorised person** assessing knowledge and experience; investor statement signed within last 12 months                                                                                                                     | Authorised person must genuinely assess — no rubber-stamping; no prescribed certificate duration                 | Certificates issued without genuine assessment; authorised firm taking on responsibility without adequate process; no ongoing review of sophistication |
| **Art. 50A** | Self-certified sophisticated | Self-declaration meeting ≥1 of: (1) member of business angel network ≥6 months; (2) ≥2 unlisted investments in past 2 years; (3) professional capacity in PE/SME finance (past 2 years); (4) director of company with turnover ≥**£1 million** in last 2 years | Self-certification statement signed within last 12 months; firm must collect and retain                          | No authorised person involvement required — but firm must have collection process; director turnover test: company's turnover, not personal income     |

**Annual re-certification requirement**: Articles 48, 50, and 50A statements must be
re-signed within the 12 months preceding each communication. Stale statements invalidate
the exemption. Build automated expiry tracking into investor management systems.

**Threshold note — 2024 changes and reversal:**

- From 31 January 2024: Thresholds raised to £170k income / £430k net assets
- From 27 March 2024: **Reversed** to £100k / £250k (previous thresholds reinstated)
- Investor statements signed under the January 2024 higher thresholds remained valid
  until 30 January 2025 only
- **Current thresholds**: £100,000 income / £250,000 net assets (as of March 2026)

#### 7b. Qualified Investor (QI) Status

For POATR prospectus exemptions, the "qualified investor" concept covers:

- FCA-authorised firms (acting for their own account)
- Large undertakings (two of: balance sheet ≥ €20m / net turnover ≥ €40m / own funds
  ≥ €2m) [VERIFY precise POATR 2024 thresholds — transitional period may apply]
- National and regional governments, central banks, international institutions
- Other institutional investors

Note: QI status under POATR is distinct from "professional client" status under MiFID
II / UK MiFIR and from FPO 2005 exemption status. A person can be a QI for prospectus
exemption purposes but not an "investment professional" under FPO Art. 19.

#### 7c. Dual Framework — FPO and Prospectus Exemptions

Both frameworks must be satisfied simultaneously:

| Scenario                                        | Prospectus Required?                      | FP Approval Required?                  |
| ----------------------------------------------- | ----------------------------------------- | -------------------------------------- |
| Offer exclusively to QIs                        | No                                        | No (Art. 19 FPO likely applies to QIs) |
| Offer to <150 certified sophisticated investors | No                                        | Depends — Art. 50 or 50A FPO           |
| Offer to 200 Art. 48 HNW individuals            | YES (200 > 150 non-QIs; and Art. 48 ≠ QI) | No (Art. 48 FPO exempts promotion)     |
| Offer to public via POP                         | No (POP exemption)                        | YES — COBS 4 applies; may be RMMI      |
| AIM IPO                                         | Prospectus = MTF admission prospectus     | COBS 4 applies to all marketing        |

**The 200 HNW individual example above is a critical trap**: HNW individuals (Article 48)
do not qualify as "qualified investors" for POATR prospectus exemption purposes unless
they also meet the QI definition. An offer to 200 HNW individuals therefore exceeds the
150-person limit and requires either a prospectus or POP route.

### Step 8: AIM / Main Market Admission Assessment

#### 8a. AIM Admission Checklist

| Requirement                                                                                          | Status | Finding |
| ---------------------------------------------------------------------------------------------------- | ------ | ------- |
| Nomad appointed and LSE-approved?                                                                    |        |         |
| Nomad eligibility assessment completed for applicant company?                                        |        |         |
| MTF admission prospectus required (IPO or reverse takeover)?                                         |        |         |
| MTF prospectus validated by LSE (not FCA)?                                                           |        |         |
| AIM Rule 1 compliance (Nomad maintained at all times)?                                               |        |         |
| AIM Rule 26 corporate governance website disclosure current?                                         |        |         |
| Chosen governance code identified (QCA or UKCGC)?                                                    |        |         |
| AIM Rule 11 inside information disclosure obligations briefed to directors?                          |        |         |
| Substantial transaction threshold (25% post-reform derogation) assessed?                             |        |         |
| Related party transaction procedures documented?                                                     |        |         |
| AIM Rule 31 cancellation provisions understood (75% independent shareholder vote if within 5 years)? |        |         |
| Directors briefed on AIM Disciplinary Handbook sanctions?                                            |        |         |

**2025 AIM Reform** (immediate derogations in place):

- Substantial transaction threshold: Raised from 10% to **25%** class test (aligned with UKLR)
- Nomad role: Refocusing from compliance-only to strategic corporate finance advisory

#### 8b. Main Market (UKLR 2024) Admission Checklist

| Requirement                                                                         | Status | Finding |
| ----------------------------------------------------------------------------------- | ------ | ------- |
| ESCC eligibility: Market cap ≥ £30m?                                                |        |         |
| Free float ≥ 10% confirmed?                                                         |        |         |
| Sponsor appointed for IPO?                                                          |        |         |
| Sponsor is FCA-authorised (unlike Nomad which is LSE-regulated)?                    |        |         |
| FCA-approved prospectus required (not LSE as for AIM)?                              |        |         |
| Dual-class share structure (DCSS): High-vote shares by natural persons (no sunset)? |        |         |
| DCSS: High-vote shares by institutional investors — 10-year sunset confirmed?       |        |         |
| Controlling shareholder agreement (voluntary — no longer mandated)?                 |        |         |
| UK Corporate Governance Code compliance (comply-or-explain)?                        |        |         |
| Ongoing regulatory obligations briefed (UK MAR, DTRs, transparency)?                |        |         |

**Key UKLR 2024 departures from old premium listing:**

- Three-year revenue track record: **Removed** (pre-revenue companies eligible)
- Shareholder approval for significant transactions: **Eliminated** (board decision only)
- Sponsor required for significant transactions: **No** (only for IPOs, prospectuses, RPTs)
- Clean working capital: **No longer required** as mandatory element

### Step 9: Offering Document Risk Factor Assessment

Assess risk factors in any prospectus, MTF admission prospectus, or offering memorandum
against PRM Sourcebook / ESMA risk factor guidelines (as retained in UK law).

| Quality Criterion                        | Standard                                                                          | Assessment |
| ---------------------------------------- | --------------------------------------------------------------------------------- | ---------- |
| **Specificity**                          | Each risk must explain HOW it affects this issuer / these securities              |            |
| **No generic risks**                     | "General economic conditions" alone is insufficient; must be tailored             |            |
| **Materiality evident**                  | Risk is material — would affect an informed investor's decision                   |            |
| **Categorisation**                       | Grouped: issuer risks, securities risks, market risks, regulatory risks           |            |
| **Ordering**                             | Most material within each category appears first                                  |            |
| **Prominence**                           | Not buried; key risk factors in prospectus summary (equity)                       |            |
| **No disclaimers masquerading as risks** | Risks must be substantive, not legal boilerplate                                  |            |
| **Quantification**                       | Risk quantified where possible and material                                       |            |
| **PFLS interaction**                     | Forward-looking content within risk factors assessed for PFLS labelling           |            |
| **Climate/ESG risk**                     | Climate transition risk factors included for equity issuers with transition plans |            |

#### 9a. Protected Forward-Looking Statements (PFLS)

New concept under POATR 2024 / PRM Sourcebook:

| Issue                           | Guidance                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **What qualifies as PFLS**      | Forward-looking statements in prospectuses clearly labelled as PFLS and meeting PRM Sourcebook criteria |
| **Liability standard for PFLS** | Claimant must prove **recklessness or dishonesty** — higher bar than negligence standard                |
| **Labelling requirement**       | Must be clearly identified as PFLS in the document                                                      |
| **Risk factor interaction**     | Risk factors are not PFLS; forward-looking content within risk factors should be separately assessed    |
| **Strategic benefit**           | Encourages more meaningful forward-looking disclosure; reduces litigation chill effect                  |

**⟁ CLARIFY** — If the prospectus contains forward-looking financial projections or
profit forecasts:

- "Have the forward-looking statements been reviewed by counsel for potential PFLS
  labelling? PFLS labelling reduces claimant liability risk but requires careful identification."

### Step 10: Cross-Border UK/EU Marketing Assessment

For offerings with any EU distribution component:

#### 10a. Prospectus Passporting — Complete Loss

| Issue                                    | Position                                            |
| ---------------------------------------- | --------------------------------------------------- |
| UK prospectus valid in EU member states? | **No** — no passporting; no equivalence             |
| EU prospectus valid in UK?               | **No** — no passporting; no equivalence             |
| FCA/ESMA MoU                             | Regulatory cooperation only — not cross-recognition |

#### 10b. Options for UK Issuer Marketing to EU Investors

| Route                        | Description                                                                                                                   | Key Requirements                                                |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **EU Prospectus Regulation** | Prepare EU-compliant prospectus; obtain EEA competent authority approval (e.g., AMF, BaFin, CBI Ireland); passport across EEA | EEA local counsel; EEA CA relationship; significant cost        |
| **EEA Private Placement**    | Use QI / 150-person / minimum consideration exemptions under each EEA state's implementation of EU PR                         | Country-by-country legal review; EEA counsel per jurisdiction   |
| **Reverse solicitation**     | EEA investor approaches without prior UK solicitation                                                                         | Narrow; strictly construed by ESMA; document evidence carefully |

#### 10c. AIFM / AIF Cross-Border Marketing (NPPR Framework)

| Scenario                                              | Route                                                                                                                       | Requirements                                                                                        |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| UK AIFM marketing UK AIF to EU professional investors | NPPR per EEA member state                                                                                                   | FCA regulation of AIFM; local regulator notification; local compliance; country-specific conditions |
| EU AIFM marketing EU AIF to UK professional investors | UK NPPR (FCA)                                                                                                               | Notify FCA; comply with UK AIFMD provisions applicable to overseas AIFMs                            |
| Pre-marketing trap (AIFMD II, April 2026 EU)          | If pre-marketing to EU investors: subscriptions within 18 months deemed to result from marketing (not reverse solicitation) | Document pre-marketing timeline; consider whether EU NPPR required from outset                      |

**⟁ CLARIFY** — If EU distribution is planned:

- "The EU component of this offering requires country-by-country legal analysis. Should
  this assessment flag the EU distribution as a gap requiring separate EEA legal counsel,
  or should I provide the general NPPR/EU PR framework for in-house use?"

### Step 11: Severity Classification and Findings Summary

Classify each finding using the four-tier system:

| Tier                  | Label                                           | Criteria                                                                                    | Escalation                                                                  |
| --------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **CRITICAL EXPOSURE** | Offering is prohibited or criminal offence risk | No valid exemption; s.21 FSMA breach; POATR general prohibition violated; FP Gateway breach | STOP — do not proceed; obtain urgent legal opinion from qualified solicitor |
| **NON-COMPLIANT**     | Clear regulatory breach or material gap         | Required disclosure absent; investor qualification procedure fails; RMMI rule not applied   | Remediate before launch; senior legal sign-off required                     |
| **PARTIAL**           | Incomplete or improvable compliance             | Required element present but deficient; procedure exists but not robustly documented        | Remediate before launch or early in post-launch programme                   |
| **COMPLIANT**         | No material gap identified                      | Requirement met with adequate documentation                                                 | Note for completeness; no action required                                   |

For each finding, generate an **Actionable Remediation** using the format in the Output
Format Template.

### Step 12: Prioritisation Framework

Tier remediation actions:

| Tier           | Label                                                    | Timeline                                                | Criteria                                                                  |
| -------------- | -------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| **IMMEDIATE**  | Deal-blocking; must resolve before marketing / admission | Before any investor approach or marketing communication | CRITICAL EXPOSURE items; NON-COMPLIANT items where promotion already live |
| **NEAR-TERM**  | Important; address in launch preparation                 | Within 4 weeks of instruction                           | NON-COMPLIANT structural gaps; PARTIAL items on prospectus content        |
| **BACKGROUND** | Governance improvement; does not block launch            | Within 3 months                                         | PARTIAL items on documentation quality; process improvements              |

### Step 13: Quality Verification

Before delivering the assessment, run these checks:

1. **Citation Quality Gates** — silently (see Quality Assurance Framework)
2. **Self-Interrogation** — for every CRITICAL EXPOSURE finding (see Quality Assurance Framework)
3. **Confidence Scoring** — assign a confidence level to each material finding
4. **Completeness check** — confirm all six assessment modules have been addressed:
   - POATR 2024 prospectus / admission assessment (Step 5)
   - Financial promotion assessment (Step 6)
   - Investor qualification assessment (Step 7)
   - AIM / Main Market assessment (if applicable) (Step 8)
   - Risk factor assessment (if applicable) (Step 9)
   - Cross-border assessment (if applicable) (Step 10)
5. **Generate Glass Box Audit Trail** and append to output

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivery.

| Gate           | Rule                                                                                                                                           | Fail Action                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, statutory instrument, FCA rule, or established principle                                           | Add citation or mark [UNVERIFIED]         |
| **Format**     | All citations follow recognisable format: FSMA 2000 s.X; POATR 2024 reg. X; COBS 4.X.X; SI YYYY/NNNN Art. X                                    | Fix format                                |
| **Currency**   | Key thresholds and dates verified against current law (2024 threshold reversals; POATR 2024 in force 19 Jan 2026; UKLR 2024 from 29 July 2024) | Flag [CHECK CURRENCY]                     |
| **Domain**     | Analysis stays within UK law scope; EU law not applied as if UK law; no bleed of pre-POATR rules into post-January 2026 analysis               | Remove or flag cross-jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; rapidly evolving areas (PISCES, AIFMD II UK implementation) flagged with [VERIFY]                               | Add confidence qualifier                  |

### Self-Interrogation — CRITICAL EXPOSURE Items

For any CRITICAL EXPOSURE finding, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the finding follow logically from the cited
statutory provision? Would the FCA or a court actually reach this conclusion on these
facts? Are there alternative interpretations that could support compliance?

**Pass 2 — Completeness**: Have all potentially applicable exemptions been considered?
Is the POATR 2024 analysis fully applied (as opposed to the old UK Prospectus Regulation
framework)? Have both the FPO exemption and the prospectus exemption been separately
assessed?

**Pass 3 — Challenge**: What is the strongest argument that the offering IS compliant?
Under what structuring adjustment could the CRITICAL EXPOSURE be resolved without
abandoning the offering? Flag as CRITICAL only if the strongest counter-argument fails.

### Confidence Scoring

| Level        | Range     | Meaning                                                  | Action                                     |
| ------------ | --------- | -------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95-1.0  | Clear statutory provision; well-established FCA position | State with confidence                      |
| **High**     | 0.80-0.94 | Strong statutory basis; limited interpretive uncertainty | State with brief caveat                    |
| **Probable** | 0.60-0.79 | Good arguments; some regulatory uncertainty              | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain; new regime not yet tested           | Flag for legal opinion with both sides     |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                  | Do not assert; flag [UNCERTAIN]            |

**Note**: The POATR 2024 regime came into force 19 January 2026 and has limited
interpretive precedent. Many assessments under this regime will be scored Probable
(0.60-0.79) or Possible (0.40-0.59) until FCA guidance and case law develop.

---

## Deep Reference — Regulatory Provisions

### Key Statutory Framework Reference

| Provision                          | Effect                                                                                                                         | Status                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| FSMA 2000 s.19                     | General prohibition on carrying on regulated activities without authorisation                                                  | In force               |
| FSMA 2000 s.21                     | Financial promotion restriction — no promotion except by authorised person or approved by authorised person or FPO-exempt      | In force               |
| FSMA 2000 s.25                     | Criminal offence for breach of s.21 — up to 2 years' imprisonment / unlimited fine on indictment                               | In force               |
| FSMA 2000 s.30                     | Civil consequences — agreement in consequence of unlawful promotion is unenforceable; investor right to recover + compensation | In force               |
| FSMA 2000 s.55NA                   | Financial Promotion Gateway requirement — authorised firms need specific FCA permission to approve third-party promotions      | In force (7 Feb 2024)  |
| POATR 2024 reg. [core prohibition] | General prohibition on public offers without an exemption — a prospectus cannot cure a non-compliant offer                     | In force (19 Jan 2026) |
| POATR 2024                         | Secondary issuance threshold: 75% (equity), 100% (closed-ended funds)                                                          | In force (19 Jan 2026) |
| POATR 2024                         | £5 million de minimis threshold for public offer exemption                                                                     | In force (19 Jan 2026) |
| POATR 2024                         | Public Offer Platforms — new regulated activity for private company capital raising >£5m                                       | In force (19 Jan 2026) |
| FPO 2005 Art. 48                   | HNW: £100k income / £250k net assets (post 27 March 2024 reversal)                                                             | In force               |
| FPO 2005 Art. 50A                  | Self-certified sophisticated: Art. 50A criteria                                                                                | In force               |
| UKLR 2024                          | ESCC: 10% free float, £30m market cap, no 3-yr revenue track record, no shareholder approval for significant transactions      | In force (29 Jul 2024) |
| COBS 4.13                          | Cryptoasset financial promotions                                                                                               | In force (8 Oct 2023)  |
| PS23/13                            | FP Gateway application requirements and ongoing obligations                                                                    | In force               |

### POATR 2024 Public Offer Exemptions — Quick Reference

| Exemption                                  | Key Condition                                              | Aggregation Risk                   |
| ------------------------------------------ | ---------------------------------------------------------- | ---------------------------------- |
| Qualified investors only                   | All offerees are QIs                                       | No                                 |
| 150 persons                                | <150 non-QI recipients                                     | Yes — multiple tranches count      |
| £5m de minimis                             | Total consideration <£5m over 12 months                    | Yes — rolling 12-month aggregation |
| Existing shareholders (private companies)  | UK company offering to own shareholders                    | No size limit                      |
| Employees / directors                      | Current or former employees / directors of issuer or group | No size limit                      |
| Via POP                                    | FCA-registered POP operator conducts the offer             | No upper limit via POP             |
| Admitted to regulated market / primary MTF | Admission-conditional offer                                | Prospectus still required          |

### AIM vs. Main Market Comparison

| Feature                                  | AIM (Primary MTF)                                       | Main Market — ESCC (Regulated Market)              |
| ---------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- |
| Regulator                                | LSE (as exchange operator)                              | FCA (UKLR 2024)                                    |
| Admission document                       | MTF admission prospectus (LSE-validated)                | FCA-approved prospectus (PRM Sourcebook)           |
| Ongoing adviser                          | Nomad (required at all times)                           | Sponsor (IPOs, specific transactions only)         |
| Free float requirement                   | No fixed minimum                                        | 10%                                                |
| Market cap minimum                       | No formal minimum                                       | £30 million                                        |
| Revenue track record                     | No formal requirement                                   | Removed under UKLR 2024                            |
| Significant transaction shareholder vote | Not required                                            | Not required (UKLR 2024)                           |
| Related party transactions               | Nomad opinion; no shareholder vote                      | Sponsor opinion (larger RPTs); no shareholder vote |
| Corporate governance                     | Self-selected code (QCA or UKCGC)                       | UKCGC recommended; comply-or-explain               |
| Settlement (T+1 transition)              | October 2027                                            | October 2027                                       |
| Secondary issuances                      | MTF prospectus not required (LSE confirmed)             | Required if >75% of existing shares (POATR)        |
| DCSS                                     | Possible under Companies Act; AIM Rules not restrictive | Permitted; institutional investor 10-year sunset   |

---

## Anti-Patterns Catalogue

What NOT to do when advising on UK capital raising and financial promotion compliance:

1. **Applying the old UK Prospectus Regulation to post-January 2026 offers**: The UK
   Prospectus Regulation was replaced by POATR 2024 on 19 January 2026. Using the old
   €8m threshold, the old 20% secondary issuance threshold, or the old rule that a
   prospectus cures a non-compliant offer is a critical analytical error.

2. **Confusing FPO exemptions with POATR prospectus exemptions**: These are distinct
   frameworks. Satisfying Article 48 (HNW) FPO exemption does not mean the offering
   is prospectus-exempt. Both frameworks must be independently satisfied.

3. **Treating HNW individuals as "qualified investors" for prospectus purposes**: Article
   48 HNW status does not confer QI status under POATR 2024. An offer to 200 HNW
   individuals exceeds the 150-person limit and requires a prospectus or POP route.

4. **Assuming a prospectus can cure a non-compliant public offer post-POATR**: Under
   the old regime, publishing a compliant prospectus could save a non-exempt offer.
   Under POATR 2024, if no exemption applies, the offer is prohibited regardless of
   any prospectus published. Establish the exemption basis FIRST.

5. **Using stale investor statements**: Articles 48, 50, and 50A all require the investor
   statement to have been signed within the 12 months preceding the communication. Using
   statements more than 12 months old is a common CRM/investor database failure.

6. **Approving financial promotions without FP Gateway permission post-7 February 2024**:
   Any FCA-authorised firm that approves financial promotions for third parties without
   FCA permission granted under s.55NA is committing a criminal offence. The Gateway is
   not optional — it requires a separate FCA application.

7. **Ignoring the 12-month rolling aggregation for the £5m threshold**: Raises structured
   in tranches across a 12-month period must be aggregated. A series of £2m tranches may
   collectively exceed £5m and trigger the general prohibition.

8. **Treating AIM and Main Market as equivalent for prospectus approval purposes**: The
   FCA approves Main Market prospectuses; the LSE validates AIM MTF admission prospectuses.
   This distinction affects the timeline, content requirements, and approval process.

9. **Omitting the Financial Promotion Gateway from compliance diligence**: Since February
   2024, any due diligence on FCA-authorised firms must include verification of whether the
   firm has (or has applied for) FP Gateway permission before relying on their promotion
   approvals.

10. **Generic risk factors**: Risk factors that merely describe industry or market conditions
    without explaining how they specifically affect this issuer or these securities are
    non-compliant under PRM Sourcebook / ESMA guidelines. The FCA frequently raises
    comments on generic risk factors in prospectus review.

11. **Applying RMMI prescribed risk warning with variation**: The RMMI prescribed risk
    warning (_"Don't invest unless you're prepared to lose all the money you invest..."_)
    must appear in the **exact prescribed wording**. Paraphrasing or shortening is
    non-compliant.

12. **Assuming PFLS labelling is always beneficial**: Protected Forward-Looking Statements
    attract a recklessness/dishonesty liability standard — beneficial for issuers — but
    only if properly labelled under PRM Sourcebook criteria. Improper PFLS labelling can
    create liability confusion. Verify the statement qualifies before labelling.

13. **Assuming prospectus passporting still operates between UK and EU**: Post-Brexit,
    there is no passporting and no equivalence arrangement in either direction. A UK
    prospectus approved by the FCA has no legal effect in any EU member state. Every
    EU distribution element requires separate legal analysis.

14. **Neglecting the AIFMD II 18-month pre-marketing trap for EU distribution**: If an
    AIFM or placement agent conducts "pre-marketing" to EU professional investors before
    the full NPPR notification, any subscription within 18 months is deemed to result
    from that marketing, not reverse solicitation. This is an AIFMD II rule (effective
    April 2026 in EU) that can trap UK AIFMs using reverse solicitation as a fallback.

15. **Omitting the equality of information rule for exempted offers above £1m**: Where
    an exempted offer exceeds £1m and targets multiple investors, any material information
    provided to some investors must be made available to all targeted investors. Failing
    to apply this rule (new under POATR 2024) can create selective disclosure liability.

16. **Assuming Article 50 certificates from non-authorised persons are valid**: Only
    certificates issued by FCA-authorised persons satisfy Article 50 FPO. Certificates
    issued by overseas regulated firms, unregulated entities, or individuals are ineffective.

17. **Promoting NMMI securities to retail or restricted-category investors**: Non-Mass
    Market Investments cannot be mass marketed and can only be promoted to persons who
    qualify under Articles 50 or 50A or are HNW individuals under Article 48. Promoting
    NMMI to anyone outside this group is a COBS / FPO breach.

18. **Ignoring social media risk for affiliate networks**: Firms are responsible for all
    promotions they "cause to be made" — including those made by affiliates and influencers
    they have engaged. FCA enforcement (19,766 promotions amended/withdrawn in 2024) is
    actively targeting the affiliate responsibility chain.

---

## Writing Standards

Apply these standards before delivering any output:

- **Precision over length**: Every finding states the specific rule breached and the
  specific gap — no vague references to "regulatory requirements"
- **Actionable first**: Lead each finding with the required action, then the legal basis
- **Severity explicit**: Label every finding CRITICAL EXPOSURE / NON-COMPLIANT / PARTIAL /
  COMPLIANT at the start
- **Thresholds specific**: Quote exact thresholds (£100,000 / £250,000; £5 million; 75%;
  150 persons) not approximations
- **Dates precise**: Specify effective dates for rules cited (19 January 2026 for POATR;
  29 July 2024 for UKLR; 7 February 2024 for FP Gateway)
- **Mark uncertainty**: All provisions with interpretive uncertainty under the new regime
  are marked [VERIFY] or assigned a Confidence Score below 0.80
- **No false certainty on new regime**: POATR 2024 has limited interpretive precedent;
  do not assert positions as settled when they are merely logical readings of new rules
- **Active voice**: "The offering breaches..." not "It appears that there may be a breach..."
- **Audience calibration**: If the user is a legal team, use statutory shorthand; if in-
  house or non-legal, explain provisions in plain English with the statutory reference
  in brackets

---

## External Tool Integration

### legalcode-mcp

This skill uses **legalcode-mcp** as its primary source of verified legal authority.

**With legalcode-mcp connected:**

- Search for current POATR 2024 provisions, FPO 2005 article text, COBS 4 current rules,
  and UKLR 2024 ESCC provisions
- Retrieve current FCA enforcement data and Dear CEO letters relating to financial
  promotions and prospectus failures
- Verify FCA Final Notices for relevant enforcement precedent
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using knowledge base
- Mark all statutory threshold citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Especially flag: POATR 2024 precise regulation numbers; current FPO 2005 threshold
  text post-reversal; UKLR 2024 specific rule numbers — these require verification

**Graceful degradation**: The skill remains useful without legalcode-mcp for structural
assessment (pathway mapping, exemption decision trees, investor qualification framework)
but legal substance depth requires verification of cited provisions.

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-uk-prospectus-and-fca-offering-compliance"
  assessment_date: "[date]"
  offering_type: "[IPO-AIM / IPO-MainMarket / Private placement / FP approval / Other]"
  issuer_name: "[if provided]"
  offer_size_gbp: "[amount or 'Not confirmed']"
  target_investors: "[QI / HNW / Sophisticated / Retail / Mixed]"
  distribution_geography: "[UK only / UK+EU / Other]"
  regulatory_pathways_assessed:
    - poatr_2024: "[Yes / No / Partial]"
    - financial_promotion_s21: "[Yes / No / Partial]"
    - fpo_2005_exemptions: "[Yes / No / Partial]"
    - aim_rules: "[Yes / No / N/A]"
    - uklr_2024: "[Yes / No / N/A]"
    - cross_border_eu: "[Yes / No / N/A]"
  regime_temporal_note: "POATR 2024 in force 19 Jan 2026; analysis applies new regime"
  legalcode_mcp: "[Connected — citations VERIFIED] / [Not connected — citations require verification]"
  research_reference_file: "[/tmp/legalcode-uk-prospectus-research.md or 'Not created']"
  critical_exposure_items: "[number]"
  non_compliant_items: "[number]"
  partial_items: "[number]"
  compliant_items: "[number]"
  citations_verified: "[number VERIFIED] / [number requiring verification]"
  confidence_overall: "[HIGH 0.80+ / MEDIUM 0.60-0.79 / LOW <0.60] — [rationale]"
  pfls_consideration: "[Yes — assessed] / [No — not applicable]"
  pisces_consideration: "[Yes — assessed] / [No — not applicable]"
  limitations:
    - "POATR 2024 has limited interpretive precedent; positions on new provisions are
      reasoned readings, not settled law"
    - "EU distribution analysis requires country-by-country EEA legal counsel"
    - "FCA Gateway permission status for any approving firm requires direct verification
      with the firm or FCA register"
    - "[Any other scope limitations]"
  reviewer:
    "AI-assisted — requires review by qualified UK securities solicitor or barrister
    before use in any offering"
```

---

## Output Format Template

```markdown
# UK Prospectus and FCA Offering Compliance Assessment

**Issuer / Offering**: [Name / Description]
**Assessment Date**: [Date]
**Offer Size**: [GBP amount]
**Offering Type**: [IPO-AIM / IPO-MainMarket / Private Placement / FP Review]
**Target Investors**: [QI / HNW / Sophisticated / Retail / Mixed]
**Regulatory Regime Applied**: POATR 2024 (in force 19 Jan 2026); UKLR 2024; FCA COBS 4

---

## Executive Summary

**Overall Compliance Status**: [CRITICAL EXPOSURE / NON-COMPLIANT / PARTIAL / COMPLIANT]

| Priority | Finding               | Severity          | Action Required |
| -------- | --------------------- | ----------------- | --------------- |
| 1        | [Most critical issue] | CRITICAL EXPOSURE | [Action]        |
| 2        | [Next issue]          | NON-COMPLIANT     | [Action]        |
| 3        | [Next issue]          | PARTIAL           | [Action]        |

---

## Regulatory Pathway Map

**Prospectus / Admission Route**:

- Applicable framework: [POATR 2024 / AIM Rules / UKLR 2024]
- Exemption relied upon: [State exemption or "None — prospectus required"]
- Prospectus type required: [FCA-approved (Main Market) / MTF (AIM, LSE-validated) / None]

**Financial Promotion Route**:

- Communicating party: [Authorised / Unauthorised]
- FP Gateway status: [Confirmed / Not confirmed / N/A — own-firm promotion]
- FPO 2005 exemption: [Art. 19 / Art. 48 / Art. 50 / Art. 50A / None]
- RMMI/NMMI classification: [RMMI / NMMI / Standard / N/A]

---

## Module 1: POATR 2024 — Prospectus / Admission Assessment

### Finding 1.1: [Issue Title]

**Severity**: [CRITICAL EXPOSURE / NON-COMPLIANT / PARTIAL / COMPLIANT]
**Confidence**: [Level — 0.XX]
**Rule**: [POATR 2024 reg. X / FSMA 2000 s.XX]

**Issue**: [Description of the compliance gap]

**Risk**: [Consequence of non-compliance — regulatory sanction, criminal offence, civil
unenforceability, etc.]

**Remediation** [IMMEDIATE / NEAR-TERM / BACKGROUND]:
[Specific corrective action with reference to the rule or procedure to be followed]

**Redline / Alternative Approach**:
[Where applicable: specific alternative structure, exemption, or document language that
resolves the issue]

---

## Module 2: Financial Promotion Assessment

### Finding 2.1: [Issue Title]

[Same format as Module 1]

---

## Module 3: Investor Qualification Assessment

### Investor Qualification Pathway Map

| Investor Type                | Number | FPO Exemption  | Prospectus Exemption   | Documentation Required           |
| ---------------------------- | ------ | -------------- | ---------------------- | -------------------------------- |
| Qualified investors          | [n]    | Art. 19        | QI exemption           | QI status records                |
| HNW individuals              | [n]    | Art. 48        | 150-person limit check | Signed statement <12 months      |
| Self-certified sophisticated | [n]    | Art. 50A       | 150-person limit check | Signed statement <12 months      |
| Other / unclassified         | [n]    | None confirmed | No exemption           | STOP — resolve before proceeding |

### Finding 3.1: [Issue Title]

[Same format]

---

## Module 4: AIM / Main Market Assessment (if applicable)

[Same format]

---

## Module 5: Risk Factor Assessment (if applicable)

[Same format]

---

## Module 6: Cross-Border UK/EU Assessment (if applicable)

[Same format]

---

## Prioritised Remediation Roadmap

### IMMEDIATE — Before any investor approach or marketing communication

1. [Finding reference]: [Action] — [Responsible party]
2. [Finding reference]: [Action] — [Responsible party]

### NEAR-TERM — Within 4 weeks of instruction

1. [Finding reference]: [Action] — [Responsible party]
2. [Finding reference]: [Action] — [Responsible party]

### BACKGROUND — Within 3 months (governance improvement)

1. [Finding reference]: [Action] — [Responsible party]

---

## Quality Scores

| Metric                               | Value                                     |
| ------------------------------------ | ----------------------------------------- |
| CRITICAL EXPOSURE items              | [n]                                       |
| NON-COMPLIANT items                  | [n]                                       |
| PARTIAL items                        | [n]                                       |
| COMPLIANT items                      | [n]                                       |
| Overall confidence                   | [Level]                                   |
| Citations verified via legalcode-mcp | [n VERIFIED] / [n requiring verification] |

---

[Glass Box Audit Trail — YAML — see template above]
```

---

## Localization Notes

This skill is UK-specific (England and Wales primary; Scotland and Northern Ireland share
the same FSMA/FCA framework). For offerings with cross-border elements:

- **EU distribution**: EU Prospectus Regulation (EU 2017/1129) applies in EEA member
  states; UK and EU regimes are entirely separate post-Brexit; engage EEA local counsel
- **US distribution**: Reg D (private placement) and Reg S (offshore offering) exemptions
  apply if US persons are offered; use a separate US securities law skill
- **Other jurisdictions**: Each jurisdiction where the offering is marketed requires
  separate legal analysis — financial promotion rules, prospectus requirements, and
  private placement exemptions vary significantly

For Scotland: FSMA 2000 and FCA Handbook apply uniformly; Scottish law governs contract
formation, property, and court procedure; s.21 and prospectus requirements are UK-wide.

---

## Provenance

**Created by**: Legalcode original synthesis — 2026-03-22

**Legal research basis**: Comprehensive web research conducted March 2026 covering:

- POATR 2024 (SI 2024/105) and FCA PS25/9 / PS25/10 final rules
- FSMA 2023 amendments (Financial Promotion Gateway, Designated Activities Regime)
- FCA PS23/13 (FP Gateway), FCA PS22/10 (RMMI/NMMI), FCA PS23/6 (cryptoassets)
- FCA FG24/1 (social media financial promotions)
- UKLR 2024 (FCA PS24/6), AIM Rules 2025 reform derogations
- FPO 2005 as amended 2024 (threshold reversal from 27 March 2024)
- FCA enforcement data 2024-25 (£186m penalties; 19,766 promotions intervened)
- A&O Shearman, Latham & Watkins, Slaughter and May, Davis Polk, Norton Rose Fulbright
  practitioner analysis of POATR 2024 and UKLR 2024 reforms

**Research file**: `research/UK_PROSPECTUS_FCA_OFFERING_COMPLIANCE_REFERENCE.md`

**Verification status**: Key thresholds and effective dates verified against multiple
practitioner and primary source references; provisions marked [VERIFY] require independent
verification against current legislation.gov.uk and fca.org.uk/handbook text.

**Related Legalcode skills**: `legalcode-uk-fca-regulatory-compliance`,
`legalcode-uk-bribery-act-compliance`, `legalcode-venture-financing-uk`
