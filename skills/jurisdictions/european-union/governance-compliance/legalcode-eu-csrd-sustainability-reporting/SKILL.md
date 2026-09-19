---
name: legalcode-eu-csrd-sustainability-reporting
description: EU CSRD (Directive 2022/2464/EU) sustainability reporting compliance assessment.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

EU CSRD (Directive 2022/2464/EU) sustainability reporting compliance assessment. Determine CSRD applicability and wave classification under Omnibus I thresholds (≥1,000 employees + €50M turnover or €25M balance sheet), assess double materiality assessment (DMA) completeness against ESRS 1 Chapter 3, evaluate ESRS disclosures across all cross-cutting (ESRS 1, ESRS 2) and topical standards (E1–E5, S1–S4, G1), review Scope 1/2/3 GHG methodology against ESRS E1, assess value chain data collection and CSDDD alignment, check XBRL/iXBRL digital tagging readiness, and evaluate limited assurance readiness under ISSA 5000. Classifies findings as COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL. Outputs executive summary, ESRS gap matrix, DMA assessment, assurance readiness report, and remediation roadmap with phased timelines. Covers phased Wave 1–4 implementation, Omnibus I postponements, and sector-specific ESRS in development. Related: legalcode-esg-sustainability-reporting, legalcode-supply-chain-contract-review, legalcode-environmental-compliance-review.


# EU CSRD Sustainability Reporting Compliance Assessment

> ⚠️ **Disclaimer**: This skill provides a framework for AI-assisted CSRD compliance
> assessment. It does not constitute legal advice, a regulatory opinion, or an assurance
> engagement. All outputs must be reviewed by a qualified legal professional and/or
> a sustainability assurance provider licensed in the relevant jurisdiction before use.
> CSRD and ESRS requirements are evolving rapidly — the Omnibus I simplification package
> (COM/2025/81) has substantially modified phasing, thresholds, and scope. Verify current
> applicability of all provisions, thresholds, and implementation dates against authoritative
> EU sources before relying on them. AI-generated regulatory analysis carries hallucination
> risk: all article references, ESRS data point citations, and assurance standard references
> should be independently verified. Greenwashing liability attaches to both overstated
> disclosures and misleading omissions — the stakes of inaccuracy are material.

---

## Purpose and Scope

This skill guides organisations through a structured CSRD compliance assessment, covering
applicability determination, double materiality assessment (DMA) quality review, ESRS
gap analysis, value chain data readiness, digital reporting compliance, and limited
assurance preparation.

**Covers:**

- Applicability and wave classification under Directive 2022/2464/EU and Omnibus I (Directive (EU) 2025/794)
- Double materiality assessment (impact materiality + financial materiality) per ESRS 1 Chapter 3
- Cross-cutting ESRS compliance: ESRS 1 (General requirements) and ESRS 2 (General disclosures)
- Topical ESRS gap analysis: E1 (Climate), E2 (Pollution), E3 (Water/Marine), E4 (Biodiversity), E5 (Circular Economy)
- Social ESRS gap analysis: S1 (Own workforce), S2 (Value chain workers), S3 (Affected communities), S4 (Consumers/End-users)
- Governance ESRS gap analysis: G1 (Business conduct)
- Scope 1, 2, and 3 GHG methodology completeness and Paris alignment
- Value chain reporting obligations and CSDDD (Directive 2024/1760) due diligence alignment
- XBRL/iXBRL digital tagging readiness (ESEF extension, EFRAG taxonomy)
- Limited assurance readiness under ISSA 5000 and transitional reasonable assurance pathway
- Remediation roadmap with IMMEDIATE / NEAR-TERM / BACKGROUND prioritisation

**Does not:**

- Draft the sustainability report or individual ESRS disclosures
- Certify CSRD compliance or issue assurance opinions (this requires an accredited statutory auditor)
- Provide jurisdiction-by-jurisdiction tax or legal opinions on CSRD transposition
- Replace a qualified double materiality consultant or ESG assurance provider
- Apply to voluntary or non-mandatory sustainability reporting under GRI, SASB, or TCFD
  where no CSRD obligation exists

**Related skills:**

- `legalcode-esg-sustainability-reporting` — broader ESG programme design and multi-framework comparison
- `legalcode-supply-chain-contract-review` — value chain contract obligations, CSDDD due diligence integration
- `legalcode-environmental-compliance-review` — site-level environmental compliance for E1–E5 ESRS inputs
- `legalcode-dora-compliance-assessment` — digital operational resilience for financial entities in scope of both DORA and CSRD
- `legalcode-compliance-risk-assessment` — enterprise-wide compliance baseline to feed the CSRD governance pillar

---

## Jurisdiction and Governing Law

### Primary Legislative Framework

| Instrument                                     | Reference                                      | Status (as at March 2026)                             |
| ---------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| Corporate Sustainability Reporting Directive   | Directive 2022/2464/EU                         | In force; national transposition varied               |
| Non-Financial Reporting Directive (superseded) | Directive 2014/95/EU                           | Repealed for CSRD entities                            |
| ESRS Delegated Regulation                      | Commission Delegated Regulation (EU) 2023/2772 | In force; subject to Omnibus I ESRS simplification    |
| Omnibus I — "Stop-the-Clock"                   | Directive (EU) 2025/794                        | Adopted; in force [VERIFY: precise OJ date]           |
| Omnibus I — Substantive CSRD changes           | COM(2025) 81 final proposal                    | Legislative procedure ongoing [VERIFY current status] |
| Accounting Directive (parent directive)        | Directive 2013/34/EU as amended                | Governs CSRD Articles 19a, 29a, 34, 40a               |
| CSDDD (value chain due diligence)              | Directive 2024/1760/EU                         | Phased from 2027; Omnibus I changes proposed          |
| EU Taxonomy Regulation                         | Regulation (EU) 2020/852                       | ESRS E1 Taxonomy-alignment disclosures required       |

### Supervisory Architecture

- **EU level**: European Commission (ESRS adoption), EFRAG (technical standards development), ESMA (enforcement coordination for listed issuers)
- **Member State level**: Designated competent authorities oversee enforcement (typically financial market supervisors for listed companies; separate authorities for large non-listed entities)
- **Statutory auditors**: Required to provide limited assurance under Article 34 CSRD; regulated by national audit oversight bodies (e.g., APAB in Germany, H3C in France, FRC in UK for cross-listed entities)
- **EFRAG sustainability reporting board**: Issues additional guidance, Q&A, and implementation support

### Penalties for Non-Compliance

[JURISDICTION-SPECIFIC] CSRD is a directive — penalties are set by each Member State upon transposition. The framework sets minimum expectations:

- **Failure to publish sustainability statement**: Potential criminal or administrative penalties; public naming in supervisory action
- **Materially false or misleading disclosures**: Greenwashing liability under national consumer and securities law; potential EU Regulation on Eco-design or Green Claims Directive enforcement (when enacted)
- **Germany (DE) [VERIFY]**: HGB penalties for false Nachhaltigkeitsbericht; DIN/ISO alignment obligations [CHECK CURRENCY]
- **France (FR) [VERIFY]**: Building on existing Devoir de Vigilance (Loi 2017-399) enforcement; CSRD transposition integrating AML/AMF oversight for listed entities
- **Netherlands (NL) [VERIFY]**: AFM oversight for listed entities; potential civil penalties and director liability
- **Assurance failures**: Auditors may face professional body sanctions and regulatory fines; entities face invalidation of the sustainability statement

[JURISDICTION-SPECIFIC] For each Member State where the organisation operates, verify: (1) date of CSRD transposition into national law, (2) designated competent authority, (3) specific penalty regime, and (4) whether national law imposes more stringent requirements than the Directive minimum.

### Omnibus I Alert — Critical Phasing Changes

> ⚠️ **OMNIBUS I ALERT (as at March 2026):** The Omnibus I package has fundamentally
> changed CSRD's applicability and timing. The "Stop-the-Clock" Directive (EU) 2025/794
> postponed Wave 2 and Wave 3 by two years. The substantive Omnibus I proposal
> (COM/2025/81) proposes raising the large company threshold to ≥1,000 employees and
> reducing mandatory ESRS data points. Until the substantive Omnibus I proposal is
> finally adopted and published in the Official Journal, the original ESRS Delegated
> Regulation 2023/2772 remains formally in force. Organisations should plan to the
> stricter standard while tracking Omnibus I legislative progress. \*\*[VERIFY: final
>
> > status of COM(2025) 81 legislative procedure and any adopted ESRS amendments.]\*\*

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you reach a ⟁ CLARIFY
point, pause and ask the structured questions shown. Skip the question if the user has
already provided the answer in their input. Every clarification point includes a "Why
this matters" note explaining how the answer changes the assessment direction.

---

## Workflow

### Step 1: Accept Input

Accept the assessment input in any of these formats:

- **Organisation description**: Size, sector, group structure, listing status, EU revenues, reporting year
- **Existing draft sustainability statement**: Full or partial draft for gap analysis
- **Prior-year NFRD/CSR report**: For continuity review and transition gap analysis
- **Double materiality assessment documentation**: For DMA quality review
- **Data inventory or gap register**: For targeted ESRS data completeness review
- **Board governance documentation**: For ESRS 2 governance pillar assessment

If no specific document is provided, conduct a structured compliance assessment based on
the contextual information gathered in Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask these questions. Present options in structured form:

1. **Assessment mode** — What is the primary objective?
   - **Gap analysis**: Identify ESRS disclosures currently missing or incomplete — most common
   - **Applicability check**: Determine whether and when CSRD applies to this organisation
   - **DMA review**: Assess the quality and completeness of the double materiality assessment
   - **Assurance readiness**: Evaluate readiness for limited assurance engagement under ISSA 5000
   - **Full assessment**: All four modes combined
   - _Why this matters_: Each mode produces a different output structure and depth of analysis.

2. **Organisational profile** — Provide the following details:
   - Legal form and incorporation jurisdiction(s)
   - Number of employees (full-time equivalent, group level)
   - Net turnover (last financial year, group level in EUR)
   - Balance sheet total (group level in EUR)
   - Listed or unlisted (and on which market/exchange if listed)
   - Non-EU parent with EU operations? (specify EU turnover and subsidiary structure)
   - _Why this matters_: These determine CSRD wave applicability and phased deadlines.

3. **Sector and value chain complexity**
   - Primary sector (NACE code or description)
   - Value chain length and geographic spread (EU-only, global)
   - Exposure to high-impact sectors (fossil fuels, aviation, cement, steel, chemicals, agriculture, finance)
   - _Why this matters_: Sector affects presumptive ESRS E1 materiality (certain sectors presumed material); sector-specific ESRS in development (oil/gas, mining, road transport, etc.).

4. **Reporting year and maturity level**
   - Intended first CSRD reporting year (FY2024, FY2025, FY2026, FY2027, or later)
   - Existing sustainability reporting framework (GRI, SASB, TCFD, ESRS partial, none)
   - Assurance history (prior assurance of any sustainability data? by whom?)
   - _Why this matters_: Wave 1 entities (FY2024) already have first-year obligations; later waves have more preparation time but must start DMA now.

5. **Focus areas** — Any specific concerns?
   - Climate/Scope 3 value chain emissions
   - Double materiality methodology
   - Governance and anti-corruption (G1)
   - Supply chain social standards (S2)
   - Digital taxonomy/XBRL tagging
   - Limited assurance preparation
   - All areas — full ESRS assessment
   - _Why this matters_: Allows the analysis to lead with the user's highest-priority concerns.

### Step 3: Gather Legal and Technical Authority

Use **legalcode-mcp** (if connected) to retrieve current CSRD regulatory text, EFRAG
implementation guidance, and member-state transposition status.

**Research targets:**

1. ESRS Delegated Regulation (EU) 2023/2772 — full text of applicable ESRS standards for this sector
2. EFRAG CSRD Q&A publications and implementation guidance (most recent)
3. Omnibus I — current legislative status; any adopted ESRS simplification
4. Member State transposition status for the organisation's relevant jurisdictions
5. ESMA enforcement priorities for sustainability reporting (most recent supervisory statement)
6. ISSA 5000 (IAASB) text — assurance standard for sustainability information
7. GHG Protocol Corporate Standard — for Scope 3 methodology cross-check
8. EU Taxonomy Regulation Delegated Acts — for Taxonomy-alignment disclosure requirements

Save the most relevant results to `/tmp/csrd-assessment-authority.md` structured as:

```markdown
# CSRD Legal Authority Reference — [Organisation Name]

## Date Gathered: [date]

## legalcode-mcp: Connected / Not connected

### Primary ESRS Standards Applicable (list relevant standards)

### EFRAG Guidance Documents Retrieved

### Omnibus I Status

### Member State Transposition Notes

### ESMA Enforcement Priorities
```

**If legalcode-mcp is not connected:**

- Mark all ESRS article and data point references with [VERIFY]
- Proceed based on the Delegated Regulation 2023/2772 framework as of March 2026
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require independent verification"`

### Step 4: CSRD Applicability Determination (Hard Gate)

Determine whether the organisation is in scope. If out of scope, stop the assessment and
provide a clear applicability ruling with the reasoning.

#### 4a. Wave 1 — PIE Entities Previously Subject to NFRD

**Criteria (unchanged by Omnibus I):**

- Public-interest entity (PIE): listed on EU regulated market, credit institution, or insurance undertaking
- AND >500 employees at group level
- First CSRD reporting year: FY2024 (report published by June 2025 for calendar-year entities)
- Estimated ~900 companies in Europe

If Wave 1 applies: note that these entities are already in their first or second reporting year.
Flag any FY2024 non-publication as CRITICAL.

#### 4b. Wave 2 — Large Companies (Post-Omnibus I Thresholds)

**Pre-Omnibus I criteria (original Directive):**

- Large company: ≥250 employees AND (≥€50M turnover OR ≥€25M balance sheet)
- First reporting year: FY2025

**Post-Omnibus I proposed criteria (pending final adoption) [VERIFY]:**

- Threshold raised to ≥1,000 employees (not yet finally adopted — track COM/2025/81)
- Combined with ≥€50M turnover OR ≥€25M balance sheet
- Revised first reporting year: FY2027 (2-year Stop-the-Clock postponement, Directive (EU) 2025/794)

**⟁ CLARIFY** — For companies with 250–1,000 employees: given Omnibus I legislative
uncertainty, should the assessment use:

- **Conservative approach**: Assume original 250-employee threshold (plan for FY2025 readiness)
- **Pragmatic approach**: Apply proposed Omnibus I threshold (plan for FY2027)
- **Dual-track**: Assess current gaps under FY2025 standards; identify minimum viable compliance for FY2027

_Why this matters_: Companies near the threshold risk significant wasted effort or non-compliance depending on the legislative outcome.

#### 4c. Wave 3 — Listed SMEs

- Listed on EU regulated market; SME as defined under Accounting Directive
- Original first reporting year: FY2026
- Post-Omnibus I (Stop-the-Clock): FY2028 [VERIFY final text]
- Listed SMEs may opt out until FY2028 by publishing a brief statement explaining non-compliance
- Voluntary VSME standard (EFRAG) available as alternative framework

#### 4d. Wave 4 — Non-EU Companies with EU Nexus

- Non-EU ultimate parent generating >€150M net turnover in the EU (two consecutive years)
- Having at least one large EU subsidiary (exceeding 2 of 3 thresholds: >€25M balance sheet, >€50M turnover, >250 employees) OR an EU-listed entity
- First CSRD reporting year: FY2028 (consolidated group sustainability report at parent level)
- Reported under Article 40a Accounting Directive as amended
- [VERIFY: Omnibus I proposed changes to non-EU parent thresholds — confirmation pending]

#### 4e. Group-Level and Subsidiary Scoping

- CSRD applies at the group (consolidated) level as the default
- Subsidiaries included in the consolidated group report are individually exempt from separate reporting
- Subsidiaries NOT included (e.g., certain regulated entities, different FY) must assess separately
- Small and micro enterprises are explicitly excluded unless listed (and subject to Wave 3 opt-out)

**Out-of-Scope Ruling:** If the organisation does not meet any Wave 1–4 criteria, state:
"This organisation does not meet CSRD applicability thresholds as of [assessment date].
Monitor Omnibus I legislative progress and re-assess if the organisation's size, listing
status, or EU revenues change. Voluntary reporting under EFRAG VSME or GRI remains available."

### Step 5: Double Materiality Assessment (DMA) Quality Review

The DMA is the foundation of the CSRD framework. Every ESRS disclosure is conditional on
materiality determination. A weak or undocumented DMA creates cascading gaps across all
topical standards.

**⟁ CLARIFY** — Has the organisation completed a DMA? If yes, is documentation available for review?

- **Yes, DMA complete and documented**: Review against ESRS 1 Chapter 3 quality criteria
- **DMA in progress**: Identify completion gaps and provide priority guidance
- **DMA not started**: Scope the DMA work required before ESRS analysis can proceed

#### 5a. DMA Framework Completeness (ESRS 1 Chapter 3)

Assess against these mandatory DMA requirements:

| DMA Element                                                                               | ESRS 1 Reference | Assessment |
| ----------------------------------------------------------------------------------------- | ---------------- | ---------- |
| Understanding the organisation's business model, activities, and value chain              | §§32-33          |            |
| Identification of relevant sustainability topics (longlist)                               | §§34-36          |            |
| Identification of actual and potential impacts (impact materiality)                       | §§37-44          |            |
| Identification of material sustainability risks and opportunities (financial materiality) | §§45-53          |            |
| Stakeholder engagement in the materiality process                                         | §§22-30          |            |
| Rebuttable presumption — ESRS E1 (Climate) presumptively material                         | §§16-17          |            |
| Threshold-setting methodology documented and justified                                    | §§34-35          |            |
| Review and approval process (board involvement per ESRS 2 GOV-5)                          | §§18-20          |            |
| DMA documented and available for assurance scrutiny                                       | §§21-31          |            |
| Periodic review process defined                                                           | §32              |            |

**Impact Materiality (inside-out)**: The organisation's actual or potential impacts on
people and environment — positive and negative, intended and unintended, across own
operations and value chain. Apply the severity criteria: scale, scope, irremediability.

**Financial Materiality (outside-in)**: Sustainability-related risks and opportunities
that could reasonably affect the organisation's cash flows, access to finance, or cost
of capital over short, medium, and long-term horizons.

**⟁ CLARIFY** — For sector-specific materiality: has the organisation considered ESRS E1
Climate as presumptively material (only rebuttable with extraordinary justification)? If
the organisation has concluded E1 is not material, escalate for legal review — this is
a high-enforcement-risk position.

#### 5b. DMA Stakeholder Engagement Quality

Assess whether stakeholder engagement meets ESRS 1 requirements:

- Identification of affected stakeholders (employees, workers in value chain, communities, users, investors)
- Process for direct engagement OR reasonable estimation where direct engagement is impractical
- Documentation of how stakeholder perspectives informed the materiality threshold-setting
- Disclosure of the engagement process in ESRS 2 SBM-2 (Interests and views of stakeholders)

#### 5c. DMA Output — Materiality Matrix

Confirm the DMA produces a documented output including:

- List of material sustainability topics per ESRS category (E, S, G)
- List of topics assessed and concluded not material (with reasoning documented)
- Threshold methodology (quantitative where possible; qualitative otherwise)
- Time horizons for risks and opportunities (short: ≤1yr; medium: 1–5yr; long: >5yr)

### Step 6: Cross-Cutting ESRS Compliance (ESRS 1 and ESRS 2)

ESRS 1 (General requirements) and ESRS 2 (General disclosures) are **mandatory** — they
cannot be assessed as not material and apply to all entities in scope of CSRD.

#### 6a. ESRS 2 — General Disclosures (Mandatory)

Assess each mandatory ESRS 2 disclosure requirement:

| ESRS 2 Disclosure                                               | Reference | Key Requirements                                                 |
| --------------------------------------------------------------- | --------- | ---------------------------------------------------------------- |
| **GOV-1**: Governance body role in sustainability               | §§28-30   | Board composition; sustainability expertise; oversight processes |
| **GOV-2**: Management reporting to governance body              | §31       | How sustainability information reaches the board                 |
| **GOV-3**: Integration into remuneration                        | §32       | Whether sustainability KPIs link to remuneration                 |
| **GOV-4**: Due diligence statement                              | §33       | Description of due diligence process per Art. 19a(1)(d)          |
| **GOV-5**: DMA review and approval                              | §34       | Board approval and periodic review of materiality process        |
| **SBM-1**: Strategy, business model, value chain                | §§40-52   | Sustainability context of business model                         |
| **SBM-2**: Stakeholder interests and views                      | §§53-57   | How stakeholders are identified and engaged                      |
| **SBM-3**: Material impacts, risks, opportunities               | §§58-63   | Integration with financial planning                              |
| **IRO-1**: Description of processes to identify and assess IROs | §§64-68   | Methodology; thresholds; due diligence integration               |
| **IRO-2**: Disclosure requirements covered, not covered         | §§69-71   | Phased-in omissions and data point exceptions                    |

#### 6b. ESRS 1 Reporting Quality Requirements

Assess compliance with ESRS 1 cross-cutting reporting requirements:

- **Connectivity**: Sustainability statement integrated with financial statements (not standalone document)
- **Comparability**: Consistent methodology year-on-year; prior-year figures restated if methodology changes
- **Comparative information**: Prior-year comparatives required from second reporting year
- **Accuracy and verifiability**: Data traceable to source systems; audit trail available for assurance
- **Forward-looking information**: Targets and milestones include time-bound commitments
- **Value chain**: Upstream and downstream value chain covered proportionately [VERIFY: Omnibus I value chain proportionality modifications]
- **Phase-in provisions**: ESRS 1 Appendix C — certain data points phased in for Year 1 and Year 2; document which phase-in provisions are used

### Step 7: Topical ESRS Gap Analysis — Environment (E1–E5)

For each topical ESRS, assess: (a) whether the topic was concluded material in the DMA,
(b) if material, whether all mandatory and applicable disclosure requirements are addressed,
and (c) data quality and verifiability.

**Classification logic**: If the topic was assessed as NOT MATERIAL in the DMA, the entity
discloses the conclusion and reasoning (per ESRS 1 §48). If the topic IS MATERIAL, all
applicable disclosure requirements must be met.

#### E1 — Climate Change (ESRS E1)

**Presumptive materiality**: Climate change (E1) is presumptively material for all entities.
Rebuttal requires extraordinary justification and creates significant greenwashing liability risk.

Key E1 disclosure areas to assess:

| E1 Disclosure                                                       | Reference | Assessment Notes                                                                      |
| ------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------- |
| E1-1: Transition plan for climate change mitigation                 | §§14-24   | Science-based pathway; Paris 1.5°C alignment; no-transition-plan disclosure if absent |
| E1-2: Policies relating to climate change mitigation and adaptation | §§25-29   | Scope of policies; governance approval                                                |
| E1-3: Actions and resources for climate change                      | §§30-36   | Capex/opex aligned to transition; CapEx plan                                          |
| E1-4: Climate-related targets                                       | §§37-44   | Absolute and intensity targets; interim milestones; SBTi alignment [VERIFY]           |
| E1-5: Energy consumption and mix                                    | §§45-55   | Total energy consumption; fossil/renewable split; EU Taxonomy-eligible activities     |
| E1-6: GHG emissions — Scope 1, 2, 3                                 | §§56-68   | See detailed Scope 3 requirements below                                               |
| E1-7: GHG removals and carbon credits                               | §§69-72   | Separate reporting of removals vs. offsets                                            |
| E1-8: Internal carbon pricing                                       | §§73-77   | If used; shadow price methodology                                                     |
| E1-9: Physical and transition risk exposure                         | §§78-84   | Financial effects of climate risks on balance sheet                                   |

**Scope 1, 2, 3 GHG Methodology — Detailed Assessment:**

| GHG Element                                              | Requirement                                                                           | Assessment |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------- |
| Scope 1 (direct emissions)                               | GHG Protocol Corporate Standard; tonnes CO₂-equivalent                                |            |
| Scope 2 — location-based                                 | Grid average emission factors; electricity consumption                                |            |
| Scope 2 — market-based                                   | Energy Attribute Certificates (EACs); supplier emission factors                       |            |
| Scope 3 — all 15 categories assessed                     | GHG Protocol Scope 3 Standard; categorise as upstream/downstream                      |            |
| Scope 3 category 15 (investments) for financial entities | PCAF methodology or equivalent [VERIFY]                                               |            |
| Total GHG footprint (Scope 1+2+3)                        | Consolidated; biogenic emissions disclosed separately                                 |            |
| Methodology and assumptions documented                   | For assurance; base year defined and justified                                        |            |
| Paris Agreement alignment pathway                        | 1.5°C aligned preferred; 2°C ceiling                                                  |            |
| Scope 3 phase-in (Year 1)                                | ESRS 1 Appendix C: Scope 3 may be phased in for first year [VERIFY Omnibus I changes] |            |

#### E2 — Pollution (ESRS E2)

If material: assess air pollutant disclosures (NOx, SOx, particulate matter), water
pollutants, soil contamination, substances of very high concern (SVHC under REACH
Regulation EC 1907/2006), microplastics, and pollution prevention policies.
Flag: industries with material pollution exposure where E2 is not assessed as material (pharmaceutical, chemical, mining, agriculture) — this is a high-scrutiny position.

#### E3 — Water and Marine Resources (ESRS E3)

If material: water consumption, water intensity, water recycling, impacts on marine
ecosystems. Industries in water-stressed areas (food/beverage, semiconductor, textiles)
face particular scrutiny. Cross-reference with EU Water Framework Directive (2000/60/EC).

#### E4 — Biodiversity and Ecosystems (ESRS E4)

If material: assess impacts on biodiversity-sensitive areas (Natura 2000, Key Biodiversity
Areas), ecosystem degradation, species affected, and restoration targets. Cross-reference
with EU Biodiversity Strategy 2030, Kunming-Montreal Global Biodiversity Framework (GBF),
and TNFD framework (voluntary but increasingly referenced). Flag: agriculture, mining,
real estate, infrastructure sectors — E4 frequently under-assessed.

#### E5 — Resource Use and Circular Economy (ESRS E5)

If material: assess resource inflows (materials, components, water), outflows (products,
by-products, waste), circular economy transition plan, and alignment with EU Circular
Economy Action Plan. Manufacturing, retail, and packaging-intensive sectors face high
scrutiny.

### Step 8: Topical ESRS Gap Analysis — Social (S1–S4)

#### S1 — Own Workforce (ESRS S1)

If material: assess disclosures on:

- S1-1 to S1-17: Policies, actions, targets, and metrics for own workforce
- Working conditions: working hours, adequate wages (link to EU Adequate Minimum Wages Directive 2022/2041/EU), work-life balance
- Equal treatment: gender pay gap disclosure (linked to EU Pay Transparency Directive 2023/970/EU)
- Social protection, health and safety metrics
- Training and skills development
- Collective bargaining coverage rates [JURISDICTION-SPECIFIC: varies significantly by Member State]

**Key S1 data requirements:**

- Total workforce headcount by employment type, country, gender
- Employee turnover rate
- Accident rate (LTIFR/TRIR)
- Hours of training per employee
- Gender pay gap percentage

#### S2 — Workers in the Value Chain (ESRS S2)

If material: assess whether the organisation has identified material negative impacts on
value chain workers (contractors, suppliers, subcontractors). Cross-reference CSDDD
due diligence requirements. Common gaps:

- Assuming value chain workers are always not material (rarely defensible in global supply chains)
- No supplier code of conduct or audit programme referenced
- No grievance mechanism accessible to value chain workers

#### S3 — Affected Communities (ESRS S3)

If material: assess community engagement, impact assessments for local communities,
particularly for operations near vulnerable or indigenous populations, or in areas with
weak governance. Mining, oil/gas, construction, and large infrastructure sectors face
heightened scrutiny.

#### S4 — Consumers and End-Users (ESRS S4)

If material: assess product safety, data privacy of consumers (cross-reference GDPR
Art. 13–14 for ESRS S4 nexus), responsible marketing, and access to products and services.
Retail, digital platforms, financial services, and healthcare sectors face highest scrutiny.

### Step 9: Topical ESRS Gap Analysis — Governance (G1)

#### G1 — Business Conduct (ESRS G1)

G1 covers corporate culture, ethics, and anti-corruption policies. Assess:

| G1 Disclosure                                      | Reference | Assessment                                                                |
| -------------------------------------------------- | --------- | ------------------------------------------------------------------------- |
| G1-1: Business conduct policies                    | §§6-14    | Anti-bribery, whistleblowing, conflicts of interest                       |
| G1-2: Whistleblower management                     | §§15-17   | EU Whistleblowing Directive (2019/1937/EU) compliance; reporting channels |
| G1-3: Prevention of corruption and bribery         | §§18-21   | Training, risk assessments, conviction/case history                       |
| G1-4: Incidents of corruption or bribery           | §22       | Number and nature of confirmed incidents                                  |
| G1-5: Political influence and lobbying             | §§23-26   | Financial contributions; lobbying register                                |
| G1-6: Supplier relationships and payment practices | §§27-30   | Average payment terms; LPA compliance [JURISDICTION-SPECIFIC]             |
| G1-7: Remuneration (sustainable governance)        | §§31-35   | Link between executive pay and sustainability outcomes                    |

**Cross-reference**: ESRS G1 and GOV-3 (remuneration) together constitute the full
governance pillar. Both must be assessed together.

### Step 10: Value Chain Reporting and CSDDD Alignment

Value chain data collection is typically the most operationally challenging CSRD requirement.

#### 10a. Value Chain Data Assessment

- **Scope of value chain**: Upstream (suppliers, raw materials, logistics) and downstream (distributors, end-of-life handling, consumers)
- **Data collection methodology**: Direct data from suppliers (Tier 1), estimated data for Tier 2+, published sector averages as proxy
- **Phase-in provisions**: ESRS 1 Appendix C allows entities to use reasonable estimates for value chain data in early reporting years [VERIFY Omnibus I simplifications to value chain obligations]
- **Proportion of spend covered**: Document what percentage of procurement spend is covered by direct supplier data
- **Supplier engagement programme**: Questionnaires, audit rights, capacity building

#### 10b. CSDDD Due Diligence Integration

[VERIFY: Omnibus I proposed changes to CSDDD timeline and scope — confirm current applicability dates]

Original CSDDD (Directive 2024/1760/EU) framework:

- Companies >5,000 employees and >€1.5B turnover: from 2027
- Companies >3,000 employees and >€900M turnover: from 2028
- Companies >1,000 employees and >€450M turnover: from 2029

**CSRD–CSDDD alignment check**: Assess whether the organisation's CSRD S2/E-category value chain analysis is consistent with any CSDDD due diligence already underway. Conflicting scope definitions create regulatory risk.

#### 10c. ESRS Data Points — Upstream/Downstream Coverage Table

Produce a summary coverage table:

| ESRS Standard | Topic                              | Own Operations | Upstream Value Chain | Downstream Value Chain | Data Source                |
| ------------- | ---------------------------------- | -------------- | -------------------- | ---------------------- | -------------------------- |
| E1            | Scope 3 Category 1–8 (upstream)    | N/A            | [%]                  | N/A                    | [GHG Protocol / estimates] |
| E1            | Scope 3 Category 9–14 (downstream) | N/A            | N/A                  | [%]                    | [estimates]                |
| S2            | Worker conditions                  | N/A            | [%]                  | [%]                    | [Supplier survey / audit]  |
| E2            | Pollution in supply chain          | N/A            | [%]                  | N/A                    | [Sector averages]          |

### Step 11: Digital Reporting — XBRL/iXBRL Tagging Readiness

CSRD Article 19d requires the sustainability statement to be published in a machine-readable
format (iXBRL inline XBRL) as part of the mandatory European Single Electronic Format (ESEF).

#### 11a. ESEF Extension Assessment

- **EFRAG ESRS XBRL Taxonomy**: Official digital taxonomy for CSRD disclosures
- **Tagging requirement**: All mandatory disclosure requirements tagged; voluntary disclosures tagged where possible
- **iXBRL format**: Human-readable HTML + machine-readable XBRL embedded; submission to OAM (Officially Appointed Mechanism) in home Member State
- **First-year exception**: [VERIFY whether any phase-in for digital tagging applies — EFRAG guidance]

#### 11b. System Readiness Gaps

Assess:

- Whether the organisation's ESG reporting tool/software supports ESRS XBRL taxonomy export
- Whether the statutory auditor's process includes review of digital tagging
- Whether the OAM filing process has been tested with the relevant national authority
- Key software providers for ESRS iXBRL: Workiva, Certent, Donnelley Financial Solutions, local filing agents [VERIFY current ESRS taxonomy support status of these platforms]

### Step 12: Limited Assurance Readiness (ISSA 5000)

Article 34 CSRD requires mandatory limited assurance of the sustainability statement from
the first reporting year. The European Commission is expected to adopt EU assurance
standards for sustainability reporting, potentially converging with ISSA 5000 (IAASB).

**⟁ CLARIFY** — Has the organisation engaged a statutory auditor or assurance provider for
the sustainability statement? If yes, provide assurance engagement details for review.

#### 12a. Assurance Scope and Provider Assessment

- **Mandatory scope**: The entire sustainability statement (all material ESRS disclosures)
- **Provider**: Statutory auditor (or accredited third-party where Member State permits)
- **Standard**: ISSA 5000 (IAASB) or EU assurance standard when adopted [VERIFY current status]
- **Independence**: Assurance provider must be independent of the entity; same audit firm as financial audit raises independence questions in some Member States [JURISDICTION-SPECIFIC]
- **Reasonable assurance pathway**: Article 34(3) CSRD contemplates future move to reasonable assurance; Commission to adopt delegated act by October 2028 [VERIFY timeline]

#### 12b. Internal Control and Data Quality Readiness

Assess:

| Assurance Readiness Element                                                            | Assessment |
| -------------------------------------------------------------------------------------- | ---------- |
| KPIs calculated from documented methodology                                            |            |
| Source data traceable to primary records (HR systems, energy bills, supplier invoices) |            |
| Internal review and sign-off process for sustainability data                           |            |
| Version control on sustainability statement drafts                                     |            |
| Audit trail for estimates and assumptions (including GHG proxies)                      |            |
| Prior-year restatement methodology documented                                          |            |
| Board approval process for sustainability statement                                    |            |
| Internal audit involvement in sustainability data quality                              |            |
| Legal letter equivalent (management representation) process                            |            |

#### 12c. Assurance Gap Findings

For each element assessed as PARTIAL or NON-COMPLIANT for assurance readiness:

- Identify the specific control gap
- Assess the likelihood of a qualified assurance conclusion
- Recommend pre-assurance remediation actions

### Step 13: Classify All Findings

Apply the four-tier compliance classification to all findings across Steps 5–12:

| Classification    | Symbol | Definition                                                                                                                                               | Remediation Urgency                                                                           |
| ----------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **COMPLIANT**     | ✅     | ESRS requirement fully met, documented, and verifiable                                                                                                   | Maintain; include in next periodic review                                                     |
| **PARTIAL**       | ⚠️     | Requirement exists but has identifiable gaps in coverage, data quality, documentation, or process                                                        | Remediate within 90 days; track in compliance register                                        |
| **NON-COMPLIANT** | ❌     | Requirement not meaningfully addressed; material omission or deficiency                                                                                  | Remediate within 30–90 days; management escalation required                                   |
| **CRITICAL**      | 🚨     | Requirement entirely absent, or a deficiency that creates immediate greenwashing liability, assurance qualification risk, or regulatory enforcement risk | Immediate remediation (0–30 days); escalate to board; consider proactive regulator engagement |

**Aggregate Posture Guidance:**

- All COMPLIANT → Compliant; maintain and build for reasonable assurance transition
- ≥1 PARTIAL, 0 NON-COMPLIANT, 0 CRITICAL → Broadly compliant; targeted remediation plan
- ≥1 NON-COMPLIANT → Management escalation; remediation project required before publication
- Any CRITICAL → Board escalation; immediate remediation; consider delay of publication vs. cost of non-publication; review with external counsel

### Step 14: Remediation Roadmap

Prioritise all NON-COMPLIANT and CRITICAL findings into a structured remediation roadmap:

#### Tier 1 — IMMEDIATE (0–30 days)

Items that must begin remediation today:

- Missing double materiality assessment (cannot publish without)
- ESRS E1 Climate not assessed despite no rebuttable justification (greenwashing liability)
- No sustainability statement planned when publication deadline has passed (Wave 1)
- No assurance engagement initiated when first CSRD report is imminent
- Greenwashing claim in existing disclosures inconsistent with ESRS data (legal liability)

#### Tier 2 — NEAR-TERM (30–90 days)

Items requiring structured remediation project:

- DMA completed but undocumented or missing stakeholder engagement evidence
- Scope 3 Category 11 (Use of sold products) not estimated despite material operations
- XBRL tagging not started when digital submission required
- S2 (value chain workers) not assessed despite global supply chain exposure
- G1-4 incidents disclosure blank without documented absence of incidents
- Assurance provider not engaged; assurance scope undefined

#### Tier 3 — BACKGROUND (90–180 days)

Items for annual planning cycle:

- Sector-specific ESRS monitoring (oil/gas, mining, road transport, agriculture in development)
- Scope 3 data collection from Tier-2+ suppliers (proportionate improvement year-on-year)
- Transition from limited to reasonable assurance (track Commission delegated act)
- Integration of CSRD data with financial reporting systems (connectivity improvement)
- Sector-specific trade association guidance integration

### Step 15: Quality Verification

Before delivering the assessment, run all quality checks silently and revise failures.

#### 15a. Citation Quality Gates

| Gate           | Rule                                                                                                      | Fail Action                       |
| -------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every ESRS requirement cited by specific standard, section, and data point number                         | Add citation or mark [UNVERIFIED] |
| **Format**     | ESRS citations follow consistent format: "ESRS E1 §56" or "ESRS 2 GOV-1 §28"                              | Fix format                        |
| **Currency**   | All references checked for Omnibus I amendments; flag [CHECK CURRENCY — Omnibus I may have modified this] | Flag or verify                    |
| **Domain**     | Analysis stays within CSRD/ESRS scope; voluntary framework references (GRI, SASB) clearly labelled        | Remove or label                   |
| **Confidence** | Uncertainty about Omnibus I status or evolving EFRAG guidance explicitly stated                           | Add qualifier                     |

#### 15b. Self-Interrogation for CRITICAL and NON-COMPLIANT Findings

For every CRITICAL or NON-COMPLIANT classification:

**Pass 1 — Regulatory Necessity**: Is this deficiency actually required by ESRS text? Is the data point mandatory (identified with a phase-in) or only "shall disclose if material"? Would an auditor cite this as a qualified finding?

**Pass 2 — Completeness**: Have all ESRS proportionality provisions been considered? Have phase-in provisions for Year 1 been checked? Has Omnibus I simplification been applied if it reduces the obligation?

**Pass 3 — Challenge**: What is the strongest argument that this finding is PARTIAL rather than NON-COMPLIANT? What evidence would upgrade the classification? Document this as a mitigating note.

Record: `self_interrogation: PASS` or `self_interrogation: REVISED` in the audit trail.

#### 15c. Confidence Scoring

For each major finding, assign a confidence level:

| Level        | Range     | Meaning                                                                     | Action                                     |
| ------------ | --------- | --------------------------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | ESRS text explicit; no Omnibus I ambiguity; settled interpretation          | State with confidence                      |
| **High**     | 0.80–0.94 | Clear ESRS requirement; minor Omnibus I uncertainty                         | State with brief caveat                    |
| **Probable** | 0.60–0.79 | ESRS text present; Omnibus I modification possible; evolving EFRAG guidance | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuine uncertainty — pending Omnibus I, unpublished EFRAG Q&A              | Flag for external legal/assurance review   |
| **Unlikely** | 0.0–0.39  | Speculative; weak basis                                                     | Mark [UNCERTAIN]                           |

---

## Compliance Assessment Reference — ESRS Disclosure Matrix

The following matrix provides a structured reference for assessing ESRS compliance.
Use alongside the detailed Step 7–9 analysis above.

### Environmental Standards Overview

| ESRS | Topic            | Presumptive Materiality                                | Key Data Points                                                   |
| ---- | ---------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| E1   | Climate change   | Presumptively material (rebuttable with justification) | Scope 1/2/3 GHG; transition plan; climate risks on balance sheet  |
| E2   | Pollution        | Sector-dependent                                       | Air/water/soil emissions; SVHC; microplastics                     |
| E3   | Water & marine   | Sector-dependent                                       | Water consumption; water stress area exposure                     |
| E4   | Biodiversity     | Sector-dependent                                       | Sites in/near Natura 2000; species impacts; ecosystem degradation |
| E5   | Circular economy | Sector-dependent                                       | Resource inflows/outflows; waste; circular design                 |

### Social Standards Overview

| ESRS | Topic                | Presumptive Materiality              | Key Data Points                                                    |
| ---- | -------------------- | ------------------------------------ | ------------------------------------------------------------------ |
| S1   | Own workforce        | Typically material for all employers | Headcount; turnover; gender pay gap; accident rate; training hours |
| S2   | Value chain workers  | Sector-dependent                     | Supplier assessments; % spend covered; grievance mechanism         |
| S3   | Affected communities | Sector/location-dependent            | Community engagement; FPIC for indigenous peoples                  |
| S4   | Consumers/end-users  | Sector-dependent                     | Product safety; privacy; responsible marketing                     |

### Governance Standards Overview

| ESRS               | Topic               | Status             | Key Data Points                                            |
| ------------------ | ------------------- | ------------------ | ---------------------------------------------------------- |
| ESRS 2 (mandatory) | General disclosures | Always applies     | All GOV/SBM/IRO disclosure requirements                    |
| G1                 | Business conduct    | Typically material | Anti-bribery; whistleblowing; supplier payments; incidents |

---

## Prioritisation Framework

When presenting findings, organise by remediation priority:

### Priority 1 — Foundational (Must resolve before any publication)

Issues that prevent publication of a legally valid sustainability statement:

- No double materiality assessment completed
- ESRS E1 Climate not assessed with no documented rebuttal justification
- No statutory auditor/assurance provider engaged (Wave 1 entities)
- Material misstatements in existing disclosures creating greenwashing liability
- Digital (XBRL) filing capability absent for entities with imminent publication deadline

### Priority 2 — Material Gaps (Must resolve before or at publication)

Issues that would likely result in a qualified assurance opinion or regulator challenge:

- DMA completed but undocumented or not board-approved
- Scope 3 GHG assessment absent or materially incomplete for high-Scope-3 sectors
- Value chain coverage insufficient (e.g., <20% of procurement spend covered)
- Key S1 metrics missing (gender pay gap, accident rate) without phase-in justification
- G1 incidents disclosure absent without documented clean history

### Priority 3 — Enhancement (Target for Year 2 and beyond)

Items to improve quality and future assurance readiness:

- Transition from estimates to primary data for Scope 3 categories
- Supplier engagement programme formalised with contractual data rights
- Sector-specific ESRS monitoring and early adoption assessment
- Reasonable assurance pathway planning

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Establish assessment scope, wave applicability, sector materiality presumptions.
Identify which ESRS standards are likely material before conducting detailed analysis.

**DO**: Conduct DMA quality review, ESRS gap analysis, assurance readiness assessment,
and digital reporting review. Apply four-tier classification to every finding.

**CHECK**: Run the 5 Citation Quality Gates. Apply self-interrogation to all CRITICAL and
NON-COMPLIANT findings. Verify all Omnibus I references against latest legislative status.
Confirm confidence scores are assigned.

**ACT**: Note any Omnibus I developments that change findings. Flag heuristics for future
reviews (e.g., new EFRAG Q&A that resolves previously uncertain points). Update
remediation roadmap priorities based on any time-sensitive deadlines discovered.

---

## Anti-Patterns

What NOT to do in CSRD compliance assessment:

1. **Treating Climate (E1) as not material without extraordinary justification.** E1 is presumptively material for all CSRD entities. Concluding otherwise exposes the organisation to greenwashing liability and assurance qualification. Only rebut with explicit, documented, board-approved reasoning — and consider the reputational risk of that position.

2. **Confusing ESRS mandatory data points with "material if assessed as material."** Some ESRS data points are mandatory regardless of materiality (those in ESRS 2). Others only apply if the topic is material. Misclassifying mandatory-as-conditional creates material disclosure gaps that auditors will find.

3. **Assuming Omnibus I resolves compliance obligations.** The "Stop-the-Clock" Directive postpones Wave 2/3 timelines but does NOT change Wave 1 obligations. The substantive Omnibus I proposal (COM/2025/81) reducing ESRS data points has NOT been finally adopted as at March 2026. Plan to the existing Delegated Regulation standard until Omnibus I is published in the Official Journal.

4. **Treating GRI/SASB/TCFD reporting as CSRD-equivalent.** ESRS have specific data points, methodologies, and assurance requirements that differ materially from voluntary frameworks. Cross-walking prior GRI reports to ESRS is not sufficient without a systematic gap analysis.

5. **Completing the DMA without stakeholder engagement.** ESRS 1 explicitly requires identification and engagement of affected stakeholders. A "desk-based" DMA using only internal management views fails this requirement and will likely receive a qualified assurance conclusion.

6. **Using Scope 3 "not required in Year 1" as a permanent exemption.** ESRS 1 Appendix C provides a limited phase-in for certain Scope 3 categories in the first reporting year only. It is not a permanent opt-out. By Year 2, Scope 3 must be substantially complete for all material categories.

7. **Ignoring the XBRL/iXBRL tagging requirement.** Many organisations focus on content quality and discover digital filing requirements too late. XBRL taxonomy selection, software integration, and test submission require 3–6 months of preparation. Starting this after the sustainability statement is drafted creates significant delays.

8. **Publishing a sustainability statement without assurance.** Article 34 CSRD makes limited assurance mandatory from Year 1. Publishing without assurance is itself non-compliance — not a permitted workaround for delayed readiness.

9. **Separating the sustainability statement from the financial statements.** CSRD requires the sustainability statement to be a designated section of the annual management report (not a standalone document). Publishing as a separate "ESG report" does not satisfy the CSRD format requirement.

10. **Assuming small subsidiaries of large groups are exempt.** Subsidiaries included in a consolidated CSRD-compliant group report may be individually exempt — but only if the group report covers them. Subsidiaries with different financial years or that are excluded from the consolidated report must assess their own obligations separately.

11. **Conflating Scope 2 location-based and market-based without disclosure of both.** ESRS E1 requires disclosure of both location-based and market-based Scope 2 emissions. Reporting only the market-based figure (which may be lower due to EAC purchases) without the location-based figure is a non-compliance gap.

12. **Disclosing GHG reductions via carbon credits as equivalent to emission reductions.** Carbon removals and credits must be reported separately from actual GHG emission reductions under ESRS E1-7. Netting offsets against gross emissions is a greenwashing risk and inconsistent with ESRS requirements.

13. **Treating the value chain phase-in as eliminating Scope 3.** The value chain proportionality provisions allow entities to use estimates where primary data is unavailable — they do not eliminate the Scope 3 disclosure obligation. An entity with material downstream use-of-products emissions cannot simply omit Category 11.

14. **Delegating the DMA entirely to sustainability consultants without board engagement.** ESRS 2 GOV-5 requires the governance body to oversee and review the DMA. Board approval is not merely procedural — a DMA signed off only at management level fails the governance pillar.

15. **Assuming G1 (Business Conduct) is not material because no incidents have occurred.** G1 requires disclosure of the absence of known incidents (G1-4), not only the presence of them. Omitting G1 because "there is nothing to report" misunderstands the disclosure requirement. Zero incidents must be affirmatively disclosed.

16. **Not assessing S2 (Value Chain Workers) for global supply chains.** Organisations with global supply chains in high-risk sectors (textiles, electronics, agriculture, construction) almost never have a credible justification for concluding S2 is not material. A non-material conclusion here will face investor and regulator scrutiny.

17. **Failing to document the DMA threshold methodology.** The DMA must be documented with sufficient detail for assurance purposes — including how thresholds were set, which stakeholders were engaged, and how their views were integrated. A DMA described only as "management assessment" fails the ESRS 1 documentation standard.

18. **Assuming EU Taxonomy disclosure is separate from ESRS.** For entities already subject to Taxonomy reporting (large companies with >500 employees previously under NFRD), Taxonomy-alignment KPIs (eligible and aligned CapEx, OpEx, Revenue) are required disclosures under ESRS E1. These must be integrated into the sustainability statement, not produced as a separate document.

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for current ESRS Delegated Regulation text and any Omnibus I amendments adopted
- Retrieve EFRAG Q&A publications and implementation guidance
- Verify Member State transposition status and penalty frameworks
- Cross-reference ISSA 5000 assurance standard text for assurance readiness steps
- Save all retrieved authority to `/tmp/csrd-assessment-authority.md`
- Mark all legalcode-mcp citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using ESRS Delegated Regulation (EU) 2023/2772 as the baseline framework
- Mark all article references and data point citations with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all ESRS citations require independent verification"`
- Flag Omnibus I-sensitive items explicitly for external legal verification

---

## Output Format Template

Structure every CSRD compliance assessment output as follows:

---

````markdown
# CSRD Compliance Assessment — [Organisation Name]

**Assessment date**: [Date]
**Reporting period**: [FY20XX]
**Assessment mode**: [Applicability / Gap Analysis / DMA Review / Assurance Readiness / Full]
**Wave classification**: [Wave 1 / Wave 2 / Wave 3 / Wave 4 / Not in scope — confirmed]

---

## Executive Summary

**Overall CSRD compliance posture**: [COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT / CRITICAL GAPS]

**Applicability**: [In scope — Wave X, first reporting year FY20XX] / [Not in scope — reason]

**Top findings**:

1. 🚨 CRITICAL: [Most urgent finding — typically DMA, E1 climate, or assurance]
2. ❌ NON-COMPLIANT: [Second most urgent]
3. ⚠️ PARTIAL: [Key partial compliance item]
4. ⚠️ PARTIAL: [Second key partial compliance item]
5. ✅ COMPLIANT: [Strong area — e.g., governance structure]

**Immediate actions required (0–30 days)**:

- [Action 1]
- [Action 2]

---

## ESRS Compliance Gap Matrix

### Cross-Cutting Standards (Always Applicable)

| Standard                               | Requirement                                | Classification   | Key Gap                                           | Priority |
| -------------------------------------- | ------------------------------------------ | ---------------- | ------------------------------------------------- | -------- |
| ESRS 2 GOV-1                           | Board sustainability governance            | ⚠️ PARTIAL       | No board-level sustainability expertise disclosed | P2       |
| ESRS 2 GOV-5                           | DMA review and approval                    | ❌ NON-COMPLIANT | DMA not formally board-approved                   | P1       |
| ESRS 2 SBM-3                           | Material IROs linked to financial planning | ⚠️ PARTIAL       | No connection to financial statements             | P2       |
| [Continue for all ESRS 2 requirements] |                                            |                  |                                                   |          |

### Environmental Standards

| Standard              | Material?         | Classification   | Key Gap                            | Priority   |
| --------------------- | ----------------- | ---------------- | ---------------------------------- | ---------- |
| E1 — Climate          | Presumptively yes | 🚨 CRITICAL      | No transition plan; Scope 3 absent | P1         |
| E2 — Pollution        | [DMA result]      | [Classification] | [Gap]                              | [Priority] |
| E3 — Water            | [DMA result]      | [Classification] | [Gap]                              | [Priority] |
| E4 — Biodiversity     | [DMA result]      | [Classification] | [Gap]                              | [Priority] |
| E5 — Circular Economy | [DMA result]      | [Classification] | [Gap]                              | [Priority] |

### Social Standards

| Standard                 | Material?    | Classification   | Key Gap | Priority   |
| ------------------------ | ------------ | ---------------- | ------- | ---------- |
| S1 — Own workforce       | [DMA result] | [Classification] | [Gap]   | [Priority] |
| S2 — Value chain workers | [DMA result] | [Classification] | [Gap]   | [Priority] |
| S3 — Communities         | [DMA result] | [Classification] | [Gap]   | [Priority] |
| S4 — Consumers           | [DMA result] | [Classification] | [Gap]   | [Priority] |

### Governance Standards

| Standard              | Material?    | Classification   | Key Gap | Priority   |
| --------------------- | ------------ | ---------------- | ------- | ---------- |
| G1 — Business conduct | [DMA result] | [Classification] | [Gap]   | [Priority] |

---

## Double Materiality Assessment Review

**DMA completion status**: [Complete / Partial / Not started]
**Stakeholder engagement**: [Adequate / Inadequate — gaps: X]
**Threshold methodology**: [Documented / Undocumented]
**Board approval**: [Yes / No / Pending]
**DMA classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]

Key DMA gaps:

- [Gap 1 with ESRS 1 reference]
- [Gap 2]

---

## GHG Emissions Assessment (ESRS E1)

| Scope                                   | Status             | Methodology            | Coverage             | Classification   |
| --------------------------------------- | ------------------ | ---------------------- | -------------------- | ---------------- |
| Scope 1 (direct)                        | [Present / Absent] | [GHG Protocol / other] | [%]                  | [Classification] |
| Scope 2 location-based                  | [Present / Absent] | [Grid factor source]   | [%]                  | [Classification] |
| Scope 2 market-based                    | [Present / Absent] | [EAC source]           | [%]                  | [Classification] |
| Scope 3 — total                         | [Present / Absent] | [GHG Protocol Scope 3] | [Categories covered] | [Classification] |
| Scope 3 — Category 11 (use of products) | [Present / Absent] | [Methodology]          | [%]                  | [Classification] |
| Paris alignment pathway                 | [Present / Absent] | [SBTi / IEA / own]     | [°C scenario]        | [Classification] |

---

## Assurance Readiness Assessment

**Assurance provider engaged**: [Yes — [Provider name] / No]
**Assurance standard**: [ISSA 5000 / national equivalent / TBD]
**Internal controls readiness**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]

Assurance readiness gaps:

- [Gap 1 — specific control weakness]
- [Gap 2]

Estimated likelihood of clean assurance conclusion: [High / Medium / Low] — [Rationale]

---

## Digital Reporting Readiness (XBRL/iXBRL)

**ESRS XBRL taxonomy identified**: [Yes / No]
**Filing software ESRS-capable**: [Yes / No / Unknown]
**Test submission to OAM conducted**: [Yes / No]
**Digital reporting classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]

---

## Remediation Roadmap

### Tier 1 — IMMEDIATE (0–30 days)

| Finding                       | ESRS Reference | Action            | Owner (suggested)   | Target  |
| ----------------------------- | -------------- | ----------------- | ------------------- | ------- |
| [CRITICAL/NON-COMPLIANT item] | [ESRS X §Y]    | [Specific action] | [CFO / CSO / Legal] | [Day X] |

### Tier 2 — NEAR-TERM (30–90 days)

| Finding | ESRS Reference | Action   | Owner (suggested) | Target  |
| ------- | -------------- | -------- | ----------------- | ------- |
| [Item]  | [ESRS X §Y]    | [Action] | [Owner]           | [Day X] |

### Tier 3 — BACKGROUND (90–180 days)

| Finding | ESRS Reference | Action   | Owner (suggested) | Target  |
| ------- | -------------- | -------- | ----------------- | ------- |
| [Item]  | [ESRS X §Y]    | [Action] | [Owner]           | [Day X] |

---

## Quality Assurance Summary

- Citation Quality Gates: [X/5 passed] — [List any failures and how addressed]
- Self-Interrogation applied to: [List of CRITICAL/NON-COMPLIANT items reviewed]
- [VERIFY] items requiring independent verification: [List]
- [CHECK CURRENCY — Omnibus I] items: [List of Omnibus I-sensitive references]
- Overall confidence: [Definite / High / Probable / Possible] — [Rationale]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-eu-csrd-sustainability-reporting"
  organisation_name: "[Organisation name]"
  assessment_date: "[YYYY-MM-DD]"
  reporting_year: "[FY20XX]"
  assessment_mode: "[Applicability / Gap Analysis / DMA Review / Assurance Readiness / Full]"
  wave_classification: "[Wave 1 / Wave 2 / Wave 3 / Wave 4 / Not in scope]"
  csrd_applicability: "[Yes — Wave X, first reporting year FY20XX] / [No — threshold not met]"
  omnibus_i_status: "[Stop-the-Clock Directive (EU) 2025/794 applied; COM(2025) 81 — [current status]]"
  sector: "[Primary NACE sector]"
  existing_framework: "[GRI / SASB / TCFD / ESRS partial / None]"
  dma_completion: "[Complete / Partial / Not started]"
  assurance_provider: "[Provider name / Not engaged]"
  legalcode_mcp: "[Connected / Not connected]"
  esrs_standards_assessed: "[E1, E2, S1, S2, G1 — list all assessed]"
  critical_findings: [N]
  non_compliant_findings: [N]
  partial_findings: [N]
  compliant_measures: [N]
  citations_verified: "[N VERIFIED via legalcode-mcp / N marked [VERIFY]]"
  omnibus_i_sensitive_items: "[N items marked [CHECK CURRENCY — Omnibus I]]"
  self_interrogation: "[PASS / REVISED — list findings reviewed]"
  confidence_overall: "[Definite / High / Probable / Possible] — [Rationale, including Omnibus I uncertainty]"
  limitations:
    - "Omnibus I (COM/2025/81) substantive ESRS changes not yet finally adopted — assessed against Delegated Regulation (EU) 2023/2772 as in force"
    - "Sector-specific ESRS (oil/gas, mining, agriculture, road transport) not yet adopted — monitor EFRAG work programme"
    - "Limited assurance standard (EU equivalent to ISSA 5000) not yet adopted — assessed against ISSA 5000 framework"
    - "Member State penalty regimes vary — [JURISDICTION-SPECIFIC] items require local legal verification"
    - "[Any additional scope limitations]"
  reviewer: "AI-assisted — requires review by qualified sustainability reporting legal professional and/or accredited assurance provider before relying on findings"
```
````

---

```

---

## Localization Notes

CSRD is an EU Directive — national transposition creates variation in procedural requirements,
penalties, and competent authority designations. Adapt each [JURISDICTION-SPECIFIC] marker
using the guidance below:

**Germany (DE)** [JURISDICTION-SPECIFIC]:
- CSRD transposed via Bilanzrichtlinie-Umsetzungsgesetz (CSR-RUG 2017 updated by CSRD-UG)
- Competent authority: [VERIFY — likely Bundesamt für Justiz for enforcement; BaFin for listed entities]
- HGB §§289b–289e (Nachhaltigkeitsbericht) as amended by CSRD transposition legislation
- Penalties: [VERIFY current penalty framework under CSRD transposition]

**France (FR)** [JURISDICTION-SPECIFIC]:
- Strong pre-existing Devoir de Vigilance framework (Loi 2017-399) informs CSRD integration
- Competent authority: AMF for listed entities; HCGE and CNCC for assurance oversight
- CSRD transposition via Ordonnance — [VERIFY current status and date]
- Penalties: [VERIFY — potential criminal and civil penalties under Code de commerce]

**Netherlands (NL)** [JURISDICTION-SPECIFIC]:
- Competent authority: AFM for listed entities
- CSRD transposition: [VERIFY current legislative status]
- Strong history of mandatory non-financial reporting enforcement

**Italy (IT)** [JURISDICTION-SPECIFIC]:
- Competent authority: Consob for listed entities
- Pre-existing D.Lgs. 254/2016 (NFRD transposition) framework
- CSRD transposition: [VERIFY current status]

**Ireland (IE)** [JURISDICTION-SPECIFIC]:
- Competent authority: IAASA (Irish Auditing and Accounting Supervisory Authority)
- CSRD transposition via Companies Act amendment: [VERIFY current status]

**For all Member States**: EFRAG maintains a CSRD transposition tracker. Consult the relevant
national authority website and the EFRAG transposition monitoring tool for current status of
each Member State's implementation, designated competent authority, and any national additions
beyond the Directive minimum.

**Non-EU entities (Wave 4 — Art. 40a)**:
- Report at the ultimate parent level under the laws of the Member State where the parent is domiciled (or, if not EU-domiciled, designate a Member State of filing)
- Third-country equivalence determinations: Commission may declare certain non-EU sustainability frameworks equivalent [VERIFY: no equivalence decisions adopted as at March 2026]
- UK companies cross-listed in EU: separate obligations under UK Sustainability Disclosure Standards (UK SDS — [VERIFY current UK SDS adoption status]) and CSRD

---

## Glossary

**Balance sheet total**: Total assets as at the reporting date under Directive 2013/34/EU.

**CSDDD (Corporate Sustainability Due Diligence Directive)**: Directive 2024/1760/EU — requires large companies to identify and address adverse human rights and environmental impacts in their operations and value chains. Phased from 2027. Omnibus I changes proposed.

**Double materiality**: CSRD's materiality concept combining impact materiality (inside-out: the company's impacts on society/environment) and financial materiality (outside-in: sustainability risks/opportunities affecting the company's financial position).

**EFRAG**: European Financial Reporting Advisory Group — develops ESRS technical standards and implementation guidance under a mandate from the European Commission.

**ESRS (European Sustainability Reporting Standards)**: The mandatory sustainability reporting standards adopted via Commission Delegated Regulation (EU) 2023/2772. Comprise 2 cross-cutting standards (ESRS 1, ESRS 2) and 10 topical standards (E1–E5, S1–S4, G1).

**EU Taxonomy**: Regulation (EU) 2020/852 establishing a classification system for environmentally sustainable economic activities. ESRS E1 requires disclosure of Taxonomy-alignment KPIs.

**Financial materiality**: The outside-in dimension of double materiality — sustainability-related risks and opportunities that could reasonably affect the company's financial performance, position, or cash flows.

**GHG Protocol**: World Resources Institute (WRI) / World Business Council for Sustainable Development (WBCSD) GHG Protocol Corporate Standard — the primary reference methodology for Scope 1, 2, and 3 GHG accounting under ESRS E1.

**Impact materiality**: The inside-out dimension of double materiality — the company's actual or potential impacts on people and the environment, positive or negative, direct or through the value chain.

**ISSA 5000**: International Standard on Sustainability Assurance 5000 (IAASB) — the global standard for sustainability assurance engagements; CSRD's mandatory limited assurance is expected to align with or adopt equivalent requirements.

**iXBRL (inline XBRL)**: The machine-readable digital format required for CSRD sustainability statements under ESEF. Combines human-readable HTML with embedded XBRL data tagged to the EFRAG ESRS taxonomy.

**Limited assurance**: Lower level of assurance than "reasonable assurance" (audit); provides a negative conclusion ("nothing has come to our attention") rather than a positive opinion; mandatory under Article 34 CSRD from Year 1.

**NFRD (Non-Financial Reporting Directive)**: Directive 2014/95/EU — the predecessor to CSRD; applies to public-interest entities with >500 employees; superseded by CSRD for in-scope entities.

**Omnibus I**: Package of EU legislative proposals (COM/2025/81) to simplify CSRD and CSDDD. Includes the "Stop-the-Clock" Directive (EU) 2025/794 postponing Waves 2/3 by two years, and substantive proposals to raise thresholds and reduce ESRS data points.

**Paris Agreement alignment**: Commitment to limit global warming to 1.5°C above pre-industrial levels; ESRS E1 requires disclosure of how the entity's GHG targets align with the Paris Agreement scenarios.

**PIE (Public-Interest Entity)**: Under Directive 2013/34/EU: EU-regulated-market-listed entities, credit institutions, and insurance undertakings; Wave 1 CSRD applies to PIEs with >500 employees.

**Reasonable assurance**: Higher level of assurance providing a positive opinion ("true and fair" / "presents fairly"); CSRD Article 34(3) contemplates future transition from limited to reasonable assurance.

**Scope 1 emissions**: Direct GHG emissions from sources owned or controlled by the reporting entity (combustion of fuel in owned/controlled facilities and vehicles).

**Scope 2 emissions**: Indirect GHG emissions from purchased electricity, steam, heat, or cooling consumed by the reporting entity.

**Scope 3 emissions**: All indirect GHG emissions (not covered in Scope 2) that occur in the entity's upstream and downstream value chain across 15 categories as defined by the GHG Protocol Scope 3 Standard.

**SBTi (Science Based Targets initiative)**: An independent initiative that validates corporate GHG reduction targets aligned with Paris Agreement scenarios; widely referenced in ESRS E1 target disclosures.

**VSME (Voluntary SME Standard)**: EFRAG's voluntary sustainability reporting standard for SMEs not in scope of CSRD; provides a simplified alternative to ESRS.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on: Directive 2022/2464/EU (CSRD),
Commission Delegated Regulation (EU) 2023/2772 (ESRS), Directive (EU) 2025/794 ("Stop-the-Clock"),
COM(2025) 81 final (Omnibus I proposal), ESRS 1 and ESRS 2 technical requirements,
EFRAG implementation guidance, ISSA 5000 (IAASB), GHG Protocol Corporate Standard and Scope 3 Standard,
Structural patterns derived from legalcode-dora-compliance-assessment, legalcode-esg-sustainability-reporting,
legalcode-environmental-compliance-review, and the legalcode-contract-review reference standard.
Deep web research conducted via the legalcode skill enhancement research pipeline (March 2026).
All ESRS article references should be verified against the current official ESRS text and any
Omnibus I amendments adopted subsequent to this skill's creation date.
```
