---
name: legalcode-esg-clause-reviewer
description: Review contracts for ESG (Environmental, Social, Governance) provisions — environmental commitments,
  carbon targets, net-zero clauses, Scope 1/2/3 emissions obligations, science-based targets, social and
  labor standards, human rights and modern slavery obligations, governance and anti-corruption requirements,
  supply chain sustainability due diligence (CSDDD, LkSG, France Devoir de Vigilance, UK Modern Slavery
  Act), ESG reporting obligations, framework compliance (GRI, SASB, TCFD, CSRD/ESRS, ISSB/IFRS S1/S2,
  SBTi), ESG representations and warranties, greenwashing and green claims risk, ESG-linked commercial
  terms and sustainability-linked pricing, ESG material adverse change definitions, biodiversity and circular
  economy provisions. Use when reviewing commercial contracts, supplier agreements, procurement agreements,
  partnership agreements, loan agreements, investment agreements, or any contract that contains, should
  contain, or explicitly lacks ESG provisions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review contracts for ESG (Environmental, Social, Governance) provisions — environmental commitments, carbon targets, net-zero clauses, Scope 1/2/3 emissions obligations, science-based targets, social and labor standards, human rights and modern slavery obligations, governance and anti-corruption requirements, supply chain sustainability due diligence (CSDDD, LkSG, France Devoir de Vigilance, UK Modern Slavery Act), ESG reporting obligations, framework compliance (GRI, SASB, TCFD, CSRD/ESRS, ISSB/IFRS S1/S2, SBTi), ESG representations and warranties, greenwashing and green claims risk, ESG-linked commercial terms and sustainability-linked pricing, ESG material adverse change definitions, biodiversity and circular economy provisions. Use when reviewing commercial contracts, supplier agreements, procurement agreements, partnership agreements, loan agreements, investment agreements, or any contract that contains, should contain, or explicitly lacks ESG provisions. Covers EU (CSRD, CSDDD, EU Taxonomy, SFDR, Green Claims Directive), US (SEC climate rules, California SB 253/261, FTC Green Guides), and UK (TCFD, SDR, Modern Slavery Act, UK Green Claims Code) regulatory frameworks. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers.


# Legalcode ESG Clause Reviewer

> **Disclaimer**: This skill provides a framework for AI-assisted review of ESG (Environmental,
> Social, Governance) provisions in commercial contracts. It does not constitute legal advice.
> All outputs should be reviewed by a qualified legal professional licensed in the relevant
> jurisdiction before use. ESG law is evolving rapidly — CSRD, CSDDD, ISSB standards, SEC
> climate disclosure rules, and national supply chain due diligence laws are being adopted,
> amended, and challenged at pace; verify current applicability before relying on any provision
> described here. Statutory and regulatory references cited from memory carry hallucination risk
> — verify against authoritative sources. Green claims and greenwashing risk assessments require
> expert scientific and regulatory review and are not substitutes for qualified ESG legal counsel.

## Purpose and Scope

This skill reviews contracts for ESG provisions — existing, missing, or deficient clauses
covering environmental commitments, social obligations, governance requirements, supply chain
sustainability, reporting duties, and framework compliance. It classifies issues by severity,
generates actionable redlines, and flags greenwashing risk.

**Covers:**

- Clause-by-clause ESG analysis across 13 ESG-specific clause categories
- Greenwashing and green claims risk assessment (special severity tier)
- Missing ESG clause detection (where law or market practice requires them)
- ESG severity classification (GREEN / YELLOW / RED / GREENWASHING-RISK)
- Redline generation with fallback positions adapted to ESG context
- Regulatory compliance mapping (CSRD, CSDDD, TCFD, SEC, California, LkSG, etc.)
- ESG framework alignment check (GRI, SASB, TCFD, ESRS, ISSB/IFRS S1/S2, SBTi)
- Business impact assessment and ESG negotiation strategy
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new ESG-specific agreements (see legalcode-supply-chain-contract-review for supplier agreements)
- Provide advice on ESG strategy, carbon accounting methodology, or sustainability science
- Replace a qualified ESG lawyer, sustainability consultant, or independent verifier
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Constitute greenwashing legal advice — such risk requires expert legal and scientific review

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. ESG obligations arise from multiple overlapping sources
(contract, statute, regulation, voluntary framework) and vary significantly across jurisdictions.
The skill identifies applicable mandatory ESG regimes based on the parties' locations, contract
type, and deal size, and applies [JURISDICTION-SPECIFIC] markers throughout.

**Key regulatory frameworks covered:**

### European Union

- **CSRD** (Corporate Sustainability Reporting Directive, 2022/2464/EU): Phased mandatory ESG
  reporting (large companies FY2024+, listed SMEs FY2026+); implements ESRS standards; requires
  Scope 1, 2, and 3 disclosure and third-party assurance. [VERIFY current phase-in schedule]
- **CSDDD** (Corporate Sustainability Due Diligence Directive, 2024/1760/EU): Entered into force
  July 2024. **Post-Omnibus I (December 2025)**: single application date July 26, 2029 for all
  in-scope companies; raised threshold to 5,000+ employees AND €1.5B+ worldwide turnover (from
  original 1,000 employees / €450M). Non-EU companies: €1.5B+ EU revenue. Civil liability for
  negligent/intentional breach; penalties up to 5% worldwide annual net turnover. Key contractual
  obligation: in-scope companies must include contractual assurances and audit rights with direct
  business partners as part of their due diligence action plan. [VERIFY Omnibus I final adoption
  status and member state transposition]
- **EU Taxonomy Regulation** (2020/852/EU): Defines environmentally sustainable economic activities
  via Technical Screening Criteria and DNSH (Do No Significant Harm) principle.
- **SFDR** (Sustainable Finance Disclosure Regulation, 2019/2088/EU): Mandatory ESG disclosures
  for financial market participants and advisers; relevant to investment and loan agreements.
- **EU Directive 2024/825** (Empowering Consumers for the Green Transition — in force):
  Amends the Unfair Commercial Practices Directive 2005/29/EC; bans vague generic environmental
  claims (e.g., "eco-friendly," "green," "climate neutral") without verifiable third-party
  substantiation; bans self-made sustainability labels without independent certification; bans
  carbon offset claims implying climate neutrality where actual emissions have not been reduced.
  Member state transposition deadline March 27, 2026; penalty provisions applicable from
  September 27, 2026. Directly impacts contract product descriptions, service representations,
  and marketing commitments.
- **EU Green Claims Directive** (proposed standalone directive COM(2023) 166): European
  Commission signaled withdrawal of the proposal (as of 2026); the existing EU Directive 2024/825
  covers the primary greenwashing prohibition. [VERIFY Commission withdrawal and current
  legislative status — do not rely on this proposal as operative law]
- **EU Deforestation Regulation** (2023/1115/EU): Due diligence obligations for cattle, cocoa,
  coffee, palm oil, soya, wood, rubber, and derived products. Large and medium operators
  compliance deadline: December 30, 2026 (after one-year postponement). First-placement
  operators must submit a Due Diligence Statement (DDS); downstream traders require DDS
  reference numbers from direct suppliers. [VERIFY current postponement status and sector-
  specific timelines]

### United States

- **SEC Climate Disclosure Rules**: Final rule issued March 2024, subsequently stayed pending
  litigation; as of 2026, status uncertain — monitor for reinstatement or replacement.
  [VERIFY current SEC position]
- **California SB 253** (CCRSA, Climate Corporate Data Accountability Act): Companies with
  > $1B US annual revenues doing business in California must report Scope 1 and 2 (FY2026),
  > Scope 3 (FY2027). [VERIFY effective dates and implementing regulations]
- **California SB 261** (CAFA, Climate-Related Financial Risk Act): Enjoined by the Ninth
  Circuit Court of Appeals as of November 2025 — **not currently enforceable as binding law**.
  [VERIFY current litigation status before citing as a binding obligation]
- **FTC Green Guides** (16 C.F.R. Part 260): Guidance on unfair or deceptive environmental
  marketing claims; highly relevant for contract representations and warranties.
- **EO 14030** (Climate-Related Financial Risk): Federal contractor ESG requirements; FAR
  climate provisions for significant federal contractors. [VERIFY current status]
- **UFLPA** (Uyghur Forced Labor Prevention Act, Pub. L. 117-78): Rebuttable presumption that
  goods from Xinjiang involve forced labor; supply chain due diligence required.

### United Kingdom

- **UK TCFD Mandatory Disclosure**: Large UK companies (2,000+ employees or £200M+ turnover)
  and premium listed issuers must include TCFD-aligned disclosures in strategic reports
  (Companies Act 2006, s.414CA as amended); FCA Listing Rule ESG 2.1. [VERIFY]
- **UK SDR** (Sustainability Disclosure Requirements, FCA PS23/16): Sustainability labelling
  and disclosure for investment products; relevant to investment and financial agreements.
- **Modern Slavery Act 2015 (UK)** (s.54): Organisations with £36M+ annual turnover must
  publish an annual modern slavery statement covering supply chain transparency.
- **UK Green Claims Code** (CMA, 2021): Guidance on misleading environmental claims; relevant
  to green contract representations.

### National Supply Chain Due Diligence Laws

- **Germany LkSG** (Lieferkettensorgfaltspflichtengesetz, effective Jan 2023): Companies with
  1,000+ employees in Germany; human rights and environmental due diligence in supply chain.
  **Abolition announced by German coalition government March 2026 — formal repeal status
  uncertain.** [VERIFY current legislative status before treating as binding]
- **France Devoir de Vigilance** (Law No. 2017-399): Companies with 5,000+ employees in France
  or 10,000+ worldwide; vigilance plan covering supply chain human rights and environment.
- **Norway Åpenhetsloven** (Transparency Act, effective July 2022): Larger Norwegian enterprises;
  human rights and decent working conditions due diligence.
- **Switzerland Due Diligence Act** (effective Jan 2022, limited scope): [VERIFY]

[JURISDICTION-SPECIFIC] When reviewing a contract, identify which mandatory regimes apply to
each party based on size, location, and sector, and assess whether the ESG clauses in the
contract are sufficient to enable the party to meet its mandatory compliance obligations.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would materially change the direction or scope of the ESG analysis
- The applicable mandatory ESG regime depends on information not in the contract
- Ambiguity in ESG commitments creates a fork only the user can resolve
- Greenwashing risk depends on facts outside the four corners of the contract

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

### Step 1: Accept the Contract

Accept the contract in any format:

- **File**: PDF, DOCX, or other document
- **URL**: Link to a contract in a CLM, cloud storage, or document system
- **Pasted text**: Contract text pasted directly into the conversation
- **ESG clause excerpt**: Specific clauses for targeted review (note the limitation in the output)

If no contract is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask:

1. **Which side do you represent?**
   - Options: Buyer/Customer, Seller/Supplier, Lender, Borrower, Investor, Investee, Both
     (symmetric assessment), Other
   - _Why this matters_: ESG obligations often run asymmetrically. Suppliers bear compliance
     burdens; buyers bear verification duties. A buyer's ESG clause is a supplier's ESG cost.

2. **What is the ESG review scope?**
   - Options: Full ESG review (all 13 categories), Targeted review (specify categories),
     Regulatory compliance only (mandatory requirements), Missing clause detection only,
     Greenwashing risk only
   - _Why this matters_: A targeted review produces more actionable output for a specific
     concern; a full review takes more time but catches all gaps.

3. **Are there specific regulatory frameworks that apply?**
   - Options: EU-focused (CSRD/CSDDD), US-focused (SEC/California), UK-focused (TCFD/SDR),
     All three jurisdictions, I don't know — please identify from the contract
   - _Why this matters_: The mandatory ESG obligations that apply drive the severity
     classification of missing provisions.

4. **What is the contract type and deal size?**
   - Free text. Prompt: contract type (supply agreement, MSA, loan, investment agreement, etc.),
     approximate deal value, contract duration, and whether this is a template or one-off.
   - _Why this matters_: ESG obligations scale with deal size and risk. A €1B procurement
     contract needs full CSDDD-compliant due diligence; a one-off €10K services contract
     does not.

5. **Are the parties subject to mandatory ESG reporting?**
   - Options: Yes (CSRD/ISSB), Possibly (depends on size/listing status), No, Unknown
   - _Why this matters_: If a party is a mandatory CSRD reporter, their supply chain ESG
     clauses directly affect their ESRS disclosures. Missing Scope 3 data obligations in
     contracts become regulatory compliance gaps.

If the user provides partial context, proceed with what is available and **state assumptions
explicitly**. Do not silently assume regulatory applicability.

### Step 3: Load the ESG Playbook

Check for an organizational ESG contracting playbook in local settings (e.g., `legal.local.md`
or `esg-playbook.md`).

The playbook should define:

- **Minimum ESG clause requirements** by contract type and deal size
- **Preferred ESG frameworks** (GRI, SASB, TCFD, ISSB, etc.)
- **Standard ESG representations**: the organization's standard positions
- **Escalation triggers**: ESG clauses requiring senior ESG officer or external counsel review

**If no ESG playbook is configured:**

**⟁ CLARIFY** — Inform the user and ask:

- **Option A: Define ESG positions now** — Walk through the organization's ESG standards for
  key clause types (carbon target commitments, audit rights, reporting obligations, termination
  triggers). Produces more precise and actionable analysis.
- **Option B: Proceed with market standard** — Use current market practice for ESG clauses as
  the baseline. Label the review: "Based on ESG market standards — not organizational positions."
- **Option C: Regulatory minimum floor** — Benchmark only against mandatory requirements
  applicable to the parties (CSRD, CSDDD, Modern Slavery Act, etc.).

### Step 4: Identify Applicable ESG Regulatory Obligations

Before clause analysis, map which mandatory ESG obligations apply to each party.

Use **legalcode-mcp** to search for:

- Current status of CSDDD transposition in the relevant member states
- CSRD reporting phase-in timeline for the party's size/listing category
- Applicable national supply chain due diligence laws (LkSG, Devoir de Vigilance, etc.)
- Current California SB 253/261 implementation status
- UFLPA applicability for specific commodities/geographies

**Save research to**: `/tmp/legalcode-esg-authority.md`

**If legalcode-mcp is not connected:**

- Mark all mandatory obligation references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — regulatory applicability requires verification"`
- Proceed using general knowledge but flag that mandatory regime mapping requires verification

Build a **Mandatory Obligations Map** at the start of the review:

| Party     | Jurisdiction | Applicable Mandatory Regime        | Scope                                         | Effective/Transposition Date |
| --------- | ------------ | ---------------------------------- | --------------------------------------------- | ---------------------------- |
| [Party A] | [Country]    | [CSRD / CSDDD / LkSG / etc.]       | [In scope / Possibly in scope / Not in scope] | [Date]                       |
| [Party B] | [Country]    | [Modern Slavery Act / TCFD / etc.] | [In scope / Possibly in scope / Not in scope] | [Date]                       |

**⟁ CLARIFY** — If the mandatory regime applicability is uncertain (e.g., company size is
not stated in the contract, or the party is a subsidiary of a group that may be in scope
at group level), ask the user for the relevant facts before proceeding.

### Step 5: ESG Clause-by-Clause Analysis

Analyze the contract systematically across all 13 ESG clause categories. Read the entire
contract before flagging issues — ESG obligations interact (e.g., a Scope 3 reporting
obligation is meaningless without supply chain audit rights to gather the data).

**⟁ CLARIFY** — For long contracts or contracts with multiple schedules incorporating
supplier codes of conduct or ESG annexes:

- Ask whether to review the main body only or also all incorporated ESG documents
- If an external code of conduct or ESG policy is incorporated by reference but not
  provided, flag this as a gap requiring review of the incorporated document

Cover all 13 ESG clause categories. For each, assess presence, substance, and adequacy.

| #   | ESG Clause Category                              | Depth    | Key Review Points                                |
| --- | ------------------------------------------------ | -------- | ------------------------------------------------ |
| 1   | Environmental Commitments & Carbon Targets       | Deep     | Net-zero, SBTi, interim targets, baselines       |
| 2   | Scope 3 Emissions & Supply Chain Decarbonization | Deep     | Data obligations, abatement plans, reporting     |
| 3   | Social & Labor Standards                         | Deep     | ILO, living wage, working conditions, DEI        |
| 4   | Modern Slavery & Human Trafficking               | Deep     | Statutory obligations, supply chain transparency |
| 5   | Governance & Anti-Corruption                     | Standard | Board diversity, anti-bribery, whistleblower     |
| 6   | Supply Chain ESG Due Diligence                   | Deep     | CSDDD/LkSG compliance, audit rights, cascading   |
| 7   | ESG Reporting Obligations                        | Deep     | Frequency, format, verification, CSRD alignment  |
| 8   | ESG Framework Compliance                         | Standard | GRI, SASB, TCFD, ESRS, ISSB, SBTi, CDP           |
| 9   | ESG Representations & Warranties                 | Deep     | Accuracy, materiality, survival, remedies        |
| 10  | Greenwashing & Green Claims Risk                 | Deep     | Substantiation, FTC/CMA compliance, liability    |
| 11  | ESG-Linked Commercial Terms                      | Standard | SLL pricing, sustainability-linked adjustments   |
| 12  | ESG Material Adverse Change & Termination        | Standard | ESG MAC definition, termination triggers         |
| 13  | Biodiversity, Water & Circular Economy           | Standard | Nature-related commitments, circularity targets  |

### Step 6: Missing ESG Clause Detection

After analyzing clauses present, check for important ESG provisions that are entirely absent.
A missing ESG clause can represent a regulatory compliance gap, not merely a commercial risk.

For each of the 13 ESG clause categories:

- Flag complete absence
- Assess severity: GREEN (not needed for this contract type/size), YELLOW (market standard
  would include this), RED (mandatory obligation exists or material risk), GREENWASHING-RISK
  (absence creates greenwashing liability where ESG claims are made elsewhere in the contract)

**Always-absent flags:**

- No modern slavery clause in a goods supply contract with UK-regulated buyer (RED where s.54
  applies) [VERIFY]
- No CSDDD-compliant contractual assurance obligation in supplier contract (RED for in-scope
  EU companies) [VERIFY transposition status]
- No ESG audit right where ESG representations are made (RED — unverifiable representations)
- No Scope 3 data obligation where one party is a mandatory CSRD reporter (RED)
- No greenwashing disclaimer where "sustainable," "green," or "net zero" appears in the
  contract without defined benchmarks (GREENWASHING-RISK)
- No GRI/SASB/ISSB version reference where framework compliance is claimed (YELLOW)

**⟁ CLARIFY** — When severity depends on facts not in the contract:

- "Does [Party A] have annual revenues above £36M? If yes, the absence of a modern slavery
  clause is a statutory compliance gap (RED). If no, it is commercially standard to include
  but not legally required."
- "Is [Party B] subject to CSRD? If yes, the absence of Scope 3 data obligations means
  [Party A] is creating a reporting gap in [Party B]'s ESRS disclosures."

### Step 7: Classify Deviations

Classify each deviation using the four-tier system defined in the **ESG Severity
Classification** section. For each:

- **GREEN**: Note for awareness
- **YELLOW**: Generate redline, provide fallback, estimate risk impact
- **RED**: Explain regulatory or material risk with legal basis, provide market-standard
  alternative language, recommend escalation
- **GREENWASHING-RISK**: Identify the specific claim, the missing substantiation, and the
  regulatory/enforcement risk, with required remediation language

**⟁ CLARIFY** — For borderline classifications:

- "This net-zero target has no interim milestones or SBTi validation. Should I classify as
  YELLOW (market is mixed on requiring milestones) or RED (aspirational-only language with
  no enforcement mechanism creates greenwashing risk under FTC Green Guides)?"
- "This supply chain audit right requires 30-day notice — adequate for routine audits but
  may be insufficient for cause-based audits. Should I flag as YELLOW or treat as acceptable?"

### Step 8: Generate ESG Redlines

**⟁ CLARIFY** — Before generating redlines, ask about ESG negotiation posture:

- **Leverage**: Is the counterparty a key supplier or a commodity vendor? ESG redlines are
  more achievable with commodity suppliers than sole-source strategic partners.
- **Regulatory exposure**: Which party has greater mandatory compliance obligations? The party
  with mandatory CSRD/CSDDD obligations has a stronger negotiating position on ESG terms.
- **Industry norms**: Is this an industry with mature ESG contracting practice (finance, large
  retail, automotive supply chain) or early-stage (SME services)?

For each YELLOW, RED, and GREENWASHING-RISK item, generate a redline using the **ESG Redline
Format** below.

### Step 9: Business Impact Summary

Provide a summary covering:

- **Overall ESG risk profile**: Classification across all 13 categories
- **Regulatory compliance gaps**: Mandatory obligations not covered by the contract's current
  ESG provisions
- **Top 3 ESG issues**: Most material items with severity and priority
- **Greenwashing exposure summary**: Any GREENWASHING-RISK items with liability quantification
  where possible
- **ESG negotiation strategy**: Which terms to lead with, where to concede, how to sequence

### Step 10: Quality Verification

Before delivering:

1. Run the 5 Citation Quality Gates (see Quality Assurance Framework)
2. For every RED and GREENWASHING-RISK item, run the 3-pass Self-Interrogation
3. Assign Confidence Scores to each material ESG clause analysis
4. Verify all 13 categories addressed (present or flagged as missing)
5. Check: do any ESG representations in the contract conflict with the analysis findings?
   If so, flag the internal inconsistency.
6. Generate the Glass Box Audit Trail

---

## ESG Clause Analysis Reference

### 1. Environmental Commitments & Carbon Targets

**Key elements to review:**

- Whether commitments are specific (numerical targets, base year, target year) or aspirational
- Alignment with a validated framework (SBTi 1.5°C pathway, Paris Agreement, net-zero by 2050)
- Whether interim milestones are specified (e.g., 50% reduction by 2030)
- Scope coverage: Scope 1 only, Scope 1+2, or Scope 1+2+3
- Accounting methodology specified (GHG Protocol Corporate Standard, ISO 14064, etc.)
- Baseline year and data source identified
- Whether commitments are "best efforts," "shall," or unconditional obligations
- Verification: third-party assurance required? By whom? To what standard?
- Carbon offset treatment: whether offsets can substitute for reductions, offset quality
  standards specified (Gold Standard, VCS, CORSIA, Article 6 Paris credits), additionality
  and permanence requirements

**Common issues:**

- Aspirational "net zero by 2050" with no interim targets, no accountability mechanism, and
  no definition of "net zero" — unenforceable and GREENWASHING-RISK
- No Scope definition: "carbon reduction" without specifying Scope 1/2/3
- SBTi commitment stated without a timeline for validation or fallback if validation fails
  (SBTi Net Zero Standard v1.3, September 2025, is the current version) [VERIFY current
  SBTi standard edition]
- Offsets allowed to substitute for actual reductions without quality standards — double-
  counting risk and regulatory enforcement risk under FTC Green Guides (updated 2025)
- No verification requirement — self-certification of unverifiable claims
- "Best efforts" standard without a minimum floor — creates no enforceable obligation
- Baseline year manipulation: no historical baseline specified, allowing a party to use a
  favorable year as the base

[JURISDICTION-SPECIFIC]:

- **EU (CSRD/ESRS E1)**: If the party is a mandatory CSRD reporter (1,000+ employees AND
  €450M+ turnover under post-Omnibus scope), contractual carbon targets must be consistent
  with ESRS E1 disclosures submitted to regulators. Misalignment creates regulatory disclosure
  risk [VERIFY Omnibus I final scope]
- **EU (CBAM — Carbon Border Adjustment Mechanism)**: CBAM requires mandatory reporting and
  carbon payment obligations for imports of steel, iron, cement, aluminum, fertilizers,
  electricity, and hydrogen from 2025. Supply contracts for these commodities must address
  CBAM compliance, embedded carbon data obligations, and cost allocation for CBAM payments
  [VERIFY current CBAM commodity scope and reporting requirements]
- **UK (TCFD)**: Large UK companies must disclose climate targets in strategic reports under
  Companies Act s.414CA. Contractual representations should not contradict TCFD disclosures
  [VERIFY]
- **US (California SB 253)**: Companies with >$1B revenue in California must report Scope 1+2
  from FY2026 and Scope 3 from FY2027. Contracts providing data must align with GHG Protocol
  [VERIFY effective dates]

### 2. Scope 3 Emissions & Supply Chain Decarbonization

**Key elements to review:**

- Whether the supplier/counterparty is required to report Scope 3 Category 1 (purchased goods
  and services) or Category 11 (use of sold products) emissions data
- What GHG accounting methodology is specified for Scope 3 (GHG Protocol Corporate Value Chain
  Standard, spend-based vs. activity-based vs. supplier-specific methods)
- Data quality requirements and verification obligations
- Timeline for Scope 3 data collection and format for submission
- Transition plan requirements: is the supplier required to have a science-based Scope 3
  abatement plan?
- Carbon hotspot identification obligations
- Whether Scope 3 obligations cascade to the supplier's own supply chain (Tier 2+)
- Data sharing protocols and confidentiality of emissions data

**Common issues:**

- No Scope 3 data obligation at all — creates CSRD/California SB 253 compliance gap for
  the buyer
- Scope 3 data methodology not specified — spend-based estimates are far less accurate
  than supplier-specific data and may not satisfy CSRD assurance requirements
- Scope 3 data obligations without corresponding audit rights to verify accuracy
- Cascading Scope 3 obligations to Tier 2+ suppliers without the Tier 1 supplier having
  contractual rights to require this from their own suppliers
- No timeline for Scope 3 data — leaves buyer unable to prepare regulatory disclosures
- Confidentiality provisions that prevent a buyer from using Scope 3 data in regulatory
  disclosures — conflicting obligations

[JURISDICTION-SPECIFIC]:

- **EU (CSRD/ESRS E1)**: ESRS E1-6 requires disclosure of Scope 1, 2, and 3 GHG emissions.
  Companies in scope cannot meet this obligation without Scope 3 data from material suppliers
  [VERIFY ESRS standards version]
- **US (California SB 253)**: Scope 3 reporting required from FY2027. Contracts entered into
  now should anticipate this obligation [VERIFY implementing regulations]

### 3. Social & Labor Standards

**Key elements to review:**

- Reference to international labor standards: ILO Core Conventions (Freedom of Association
  C87, Collective Bargaining C98, Forced Labor C29/C105, Child Labor C138/C182,
  Discrimination C100/C111)
- Living wage vs. minimum wage: does the clause require payment of a "living wage" (as defined
  by a recognized benchmark such as the Living Wage Foundation or Anker Living Wage) or
  merely minimum wage compliance?
- Working hours, health, and safety standards
- Freedom of association and right to collective bargaining
- Prohibition on child labor (with age definitions consistent with ILO C138/C182)
- Non-discrimination obligations (ground of race, sex, religion, disability, etc.)
- DEI (Diversity, Equity, Inclusion) commitments: targets, reporting, third-party assessment.
  [JURISDICTION-SPECIFIC — US federal contracting context: DEI-specific contract requirements
  have been curtailed by 2025 executive orders; private sector DEI provisions must be drafted
  with anti-discrimination law compliance in mind. EU context: EU Gender Balance Directive
  2022/2381 requires 40% of non-executive board positions for the under-represented sex by 2026]
- Remediation obligations if social standards are breached
- Audit rights for social compliance verification
- Worker grievance mechanism: ABA Model Contract Clauses (based on UN Guiding Principles on
  Business and Human Rights) provide an established drafting standard for supplier human rights
  due diligence provisions including operational-level grievance mechanisms [VERIFY current
  ABA Model Contract Clauses edition]

**Common issues:**

- "Applicable law compliance" only — offers no additional protection above legal minimum,
  which varies widely by jurisdiction
- No ILO Convention reference — allows parties to claim compliance with local law that
  falls below international standards
- Living wage conflated with minimum wage — materially different standard
- No audit right to verify social compliance — unverifiable representations
- DEI commitments without measurable targets or reporting obligations — aspirational only
- No worker voice mechanism — social standards without anonymous grievance channels
  undermine their effectiveness

[JURISDICTION-SPECIFIC]:

- **EU (CSDDD Art. 8-10)**: CSDDD requires contractual assurances on human rights and
  environmental standards from direct business partners, with cascading obligations further
  down the value chain [VERIFY transposition status]
- **Germany (LkSG §6)**: Requires risk analysis and preventive measures for Tier 1 suppliers;
  contractual implementation through supplier declarations [VERIFY]
- **France (Devoir de Vigilance)**: Vigilance plan must cover supply chain; contractual
  provisions should enable compliance with the plan [VERIFY]

### 4. Modern Slavery & Human Trafficking

**Key elements to review:**

- Whether the contract includes a modern slavery representation and warranty
- Whether the representation covers the party's own operations and supply chain, or
  operations only
- Whether the supplier is required to have a modern slavery policy and conduct supply chain
  due diligence
- Whether annual modern slavery statement publication is required (if statutorily obligated)
- Whether the contract includes a specific prohibition on forced labor, bonded labor, human
  trafficking, and child labor
- Audit rights to verify modern slavery compliance
- Right to audit Tier 2 and below suppliers for modern slavery risks
- Remediation obligations and termination rights on modern slavery discovery
- UFLPA (US) compliance for goods sourced from Xinjiang or using supply chains at risk

**Common issues:**

- Representation covers "party's operations" only — omits supply chain where the risk lies
- No audit right to verify supply chain compliance — self-certification only
- No specific prohibition on forced labor, bonded labor, and debt bondage — reliance on
  "applicable law" in jurisdictions where these are not well-enforced
- No remediation obligation — if modern slavery is discovered, no contractual requirement
  to address it, only to report
- Broad carveout for jurisdictions with inadequate law — undermines the purpose of the clause
- UFLPA risk not addressed in contracts involving goods from at-risk geographies

[JURISDICTION-SPECIFIC]:

- **UK (Modern Slavery Act 2015, s.54)**: Organisations with £36M+ annual turnover must
  publish an annual modern slavery statement. The contract should require the supplier to
  cooperate with the buyer's statement preparation obligations [VERIFY threshold]
- **US (UFLPA, Pub. L. 117-78)**: Rebuttable presumption of forced labor for goods from
  Xinjiang. Supply chain due diligence obligations and import bar risk [VERIFY]
- **EU (CSDDD)**: Forced labor is a core human rights risk requiring contractual assurance
  and due diligence cascade [VERIFY]
- **Germany (LkSG §2)**: Forced labor, child labor, and slavery are core prohibited risks
  requiring contractual preventive measures [VERIFY]

### 5. Governance & Anti-Corruption

**Key elements to review:**

- Anti-bribery and anti-corruption representations (aligned with FCPA, UK Bribery Act,
  OECD Anti-Bribery Convention as applicable)
- Board diversity commitments: gender diversity targets, diversity reporting obligations
- Whistleblower protection: existence of an internal whistleblower channel, non-retaliation
  commitment, alignment with EU Whistleblower Directive 2019/1937 where applicable
- Tax transparency: country-by-country reporting participation, public tax transparency
  commitment
- Executive compensation linked to ESG performance (where relevant to the deal)
- Conflicts of interest disclosure obligations
- Trade ethics and sanctions compliance

**Common issues:**

- Anti-corruption clause limited to "applicable law" without naming key statutes
  (FCPA, UK Bribery Act) — leaves ambiguity about standard applied
- Board diversity commitment aspirational with no reporting obligation
- No whistleblower protection clause in contracts where whistleblowing risk is relevant
  (regulated industries, government contracting, financial services)
- EU Whistleblower Directive obligations not addressed in contracts with EU-regulated entities

[JURISDICTION-SPECIFIC]:

- **EU (Whistleblower Directive 2019/1937)**: EU member states required to implement
  protections for reporting persons in organizations with 50+ workers [VERIFY]
- **UK (Bribery Act 2010)**: Adequate procedures defense requires contractual anti-bribery
  obligations in supply chains [VERIFY]

### 6. Supply Chain ESG Due Diligence

**Key elements to review:**

- Whether the contract requires the counterparty to conduct human rights and environmental
  due diligence in its own supply chain (not just its own operations)
- Mapping and risk assessment obligations for Tier 2+ suppliers — note the CSDDD 2025
  revision limits mandatory due diligence primarily to Tier 1 direct suppliers; cascade to
  indirect suppliers is required only on concrete indications of risk [VERIFY Omnibus status]
- Contractual assurance cascade: is the counterparty required to pass ESG obligations down
  to its own suppliers?
- Audit rights: right to audit the counterparty's ESG compliance, including supply chain
  audits; notice periods; frequency; scope; cost allocation
- Independent audit: right to require third-party audited ESG compliance (as opposed to
  self-certification)
- Corrective action plans: what happens if the audit reveals a deficiency?
- Termination rights for persistent ESG non-compliance
- Supplier code of conduct: is a code of conduct incorporated, and does it set enforceable
  standards or merely aspirational goals?
- Grievance mechanism: is there a mechanism for supply chain workers to raise concerns?

**Common issues:**

- Due diligence limited to Tier 1 — CSDDD and LkSG require looking further into the value
  chain for high-risk categories [VERIFY scope of applicable law]
- Audit right subject to excessive notice period (90+ days) — allows window dressing
- Self-certification only — no right to require independent third-party audit
- Supplier code of conduct incorporated by reference but not provided — unknown standard
- Code of conduct aspirational ("aims to") rather than contractual — no enforcement mechanism
- No corrective action plan procedure — audit without remedy is theater
- Cascading obligation stated but no mechanism for the Tier 1 supplier to actually require
  it from Tier 2 suppliers
- Audit cost entirely on the auditing party — creates disincentive to exercise the right

[JURISDICTION-SPECIFIC]:

- **EU (CSDDD Art. 10, as revised 2025)**: Contractual assurances from direct business
  partners (Tier 1) required. Post-2025 revision: cascade to indirect suppliers (Tier 2+)
  is required only where there are concrete indications of risk; monitoring frequency reduced
  to every five years; mandatory termination replaced by suspension-first model. Application
  dates: 5,000+ employees / €1.5B+ (2027), 3,000+ / €900M+ (2028), 1,000+ / €450M+ (2029)
  [VERIFY Omnibus I final adoption and member state transposition status]
- **Germany (LkSG §6-7)**: Preventive measures must include supplier-facing contractual
  obligations; annual risk analysis required [VERIFY]
- **France (Devoir de Vigilance)**: Vigilance plan must include vigilance measures for
  subsidiaries and established commercial relationships [VERIFY]

### 7. ESG Reporting Obligations

**Key elements to review:**

- Frequency of ESG reporting (annual, quarterly, event-driven)
- Format: aligned with a specified framework (GRI, SASB, TCFD, ESRS, ISSB/IFRS S1/S2)
- Which metrics are required: quantitative targets with baseline, qualitative narrative, or both
- Verification: is third-party assurance required? Limited or reasonable assurance?
  By whom (accredited verifier, Big 4, specialist)? To what standard (ISAE 3000, AA1000)?
- Deadline for submission of ESG reports
- Right to review and challenge ESG report data
- Remediation if ESG metrics are not met: reporting of failure, corrective action, penalty
- CSRD alignment: if the buyer is a mandatory CSRD reporter, does the supplier's reporting
  obligation provide sufficient data for the buyer's ESRS disclosures?
- Public vs. private reporting: is the obligation to provide data to the counterparty or to
  publish publicly?

**Common issues:**

- No framework specified — "ESG report" without specifying GRI, SASB, or ISSB provides no
  assurance of comparability or materiality
- Framework specified without edition/version year — GRI Standards have been significantly
  revised; GRI 2021 Universal Standards vs. earlier versions are not interchangeable
- No assurance requirement — unverified self-reported ESG data has minimal credibility
- Deadline not specified — creates no enforceability
- No materiality definition — parties disagree on what must be reported
- CSRD-driven supplier reporting obligation but no right for the buyer to use the data in
  regulatory disclosures (confidentiality conflict)

[JURISDICTION-SPECIFIC]:

- **EU (CSRD/ESRS)**: If the buyer must comply with CSRD, supplier ESG reporting obligations
  in contracts must provide the specific ESRS-required data points (e.g., ESRS E1 for climate,
  ESRS S2 for workers in the value chain) [VERIFY ESRS delegated regulations]
- **UK (TCFD)**: TCFD-aligned disclosures required for large UK companies. Supplier contracts
  should require climate-related data consistent with TCFD four pillars [VERIFY]

### 8. ESG Framework Compliance

**Key elements to review:**

- Which ESG frameworks are referenced in the contract (GRI, SASB, TCFD, ESRS, ISSB/IFRS
  S1/S2, SBTi, CDP, UN Global Compact, UN SDGs, ISO 14001, ISO 26000, ISO 14064)?
- Whether the framework reference includes the specific edition, version, or year
- Whether the obligation is to "align with," "report in accordance with," or "be certified
  to" the framework — materially different standards
- ISSB/IFRS S1/S2: is adoption mandatory in the relevant jurisdiction? [VERIFY]
- SBTi: if SBTi validation is referenced, is there a deadline for validation submission,
  a fallback if validation is not achieved, and a procedure for maintaining validation?
- CDP: if CDP disclosure is required, which questionnaire (Climate, Water, Forests)?
  What score target, if any?
- UN SDGs: if UN SDG alignment is stated, which goals? How is alignment measured?
- ISO 14001: if referenced, is certification required or only alignment?

**Common issues:**

- Multiple frameworks referenced inconsistently — TCFD for governance but GRI for
  environmental, creating gaps in the coverage
- Framework reference without version year — "GRI Standards" may mean 2016 or 2021
  Universal Standards, which are significantly different
- "Align with" is not the same as "in accordance with" — the former is aspirational
- SBTi commitment without a validation timeline or fallback — creates an unachievable
  obligation with no remedy
- ISO 14001 reference without specifying whether certification is required — "aligned with
  ISO 14001" is virtually unenforceable
- UN SDG goals listed without any measurable contribution methodology

[JURISDICTION-SPECIFIC]:

- **EU**: ESRS standards are mandatory for CSRD reporters and take precedence over voluntary
  frameworks. Contracts should recognize the primacy of ESRS obligations [VERIFY]
- **UK**: ISSB IFRS S1/S2 adoption pathway — UK government endorsing ISSB standards;
  timeline for mandatory adoption uncertain [VERIFY UK ISSB adoption status]
- **US**: SEC has not mandated ISSB adoption. SASB standards widely used voluntarily. [VERIFY]

### 9. ESG Representations & Warranties

**Key elements to review:**

- Whether the contract contains specific ESG representations and warranties (not merely
  general compliance representations that include ESG by implication)
- Accuracy: whether ESG representations are stated as true and correct as of the date of
  signing, or "to the best of the party's knowledge"
- Materiality: whether a materiality qualifier applies and how "materiality" is defined for
  ESG purposes
- Forward-looking representations: whether net-zero commitments, SBTi targets, or ESG
  ratings are warranted — these are promises, not current-state facts
- Survival period: how long do ESG representations survive closing/signing?
- Remedies for breach: indemnification, termination, price adjustment?
- ESG MAC (Material Adverse Change): is an adverse change to ESG status (downgrade, breach
  of mandatory compliance) defined as a MAC?
- Interaction with general representations: do general "no material misrepresentation"
  representations cover ESG disclosures?

**Common issues:**

- "To the best of our knowledge" qualifier on ESG representations — makes the representation
  nearly useless given the complexity of supply chain ESG data
- ESG rating representation without specifying which agency (CDP, MSCI ESG, Sustainalytics,
  ISS ESG) and vintage of rating
- Warranting forward-looking ESG commitments as current facts — creates immediate breach
  if targets are ambitious
- No survival period for ESG representations — expires before verification is possible
- No indemnification for ESG representation breach — representation without remedy
- General "compliance with applicable law" representation does not capture voluntary ESG
  obligations (which, by definition, exceed legal minimum)

[JURISDICTION-SPECIFIC]:

- **EU (CSRD)**: Material misrepresentation in ESG disclosures that feed into mandatory
  CSRD reports creates regulatory liability. Contract ESG reps must be consistent with
  regulatory disclosures [VERIFY]
- **UK (Misrepresentation Act 1967)**: Negligent misrepresentation in ESG reps could
  trigger remedies for rescission or damages [VERIFY]
- **US (FTC Green Guides, updated 2025, 16 C.F.R. Part 260)**: The FTC updated the Green
  Guides in 2025 with stricter requirements for environmental claims. Broad terms like "green,"
  "eco-friendly," or "sustainable" must be backed by clear, specific evidence. "Carbon neutral"
  and "net zero" claims require disclosed scope, methodology, and third-party verification. False
  or misleading ESG representations constitute unfair or deceptive acts under FTC Act §5 [VERIFY
  current Green Guides text — confirm 2025 update in force]

### 10. Greenwashing & Green Claims Risk

**Key elements to review:**

- Any use of "sustainable," "green," "eco-friendly," "net zero," "carbon neutral,"
  "climate positive," "nature positive," "net positive," or similar claims in the contract
  recitals, representations, product descriptions, or marketing provisions
- Whether each claim is: specific and measurable, substantiated by a verified methodology,
  time-bound, and comparable to a defined baseline
- FTC Green Guides compliance (US): specificity, substantiation, comparative claims, seals
  and certifications, "carbon neutral" and "net zero" claims
- CMA Green Claims Code compliance (UK): six principles for lawful green claims
- EU Green Claims Directive compliance (proposed): substantiation and independent
  verification requirements for any public environmental claim
- Whether third-party certification is required for green product/service claims in the
  contract
- Warranty chain: if a buyer relies on a supplier's green claim in its own marketing, is
  the indemnification for greenwashing liability adequately allocated?
- ESG product labelling: is the product labeled as "sustainable," "responsible," or similar?
  Is the labelling basis specified?

**Common issues (GREENWASHING-RISK items):**

- "Net zero by 2050" representation with no SBTi validation, no interim targets, no Scope 3
  coverage, and no offset quality standards — prototypical greenwashing claim
- "Carbon neutral" product claim without specifying: the scope of emissions covered, the
  offset standard used (additionality, permanence, vintage), and the verification body
- "Sustainable sourcing" without a certification scheme or audit right — unsubstantiated
- "Eco-friendly" used as a blanket product descriptor without defined environmental attribute
- Supplier claims EU Taxonomy alignment without specifying the economic activity, the
  Technical Screening Criteria applied, and the DNSH assessment
- Green product certification labelling in contract without the certification body's name
  and scheme standard
- Greenwashing indemnification allocated to the seller where the claim originates with the
  buyer's marketing team — misallocation of liability
- CDP/MSCI ESG score representation based on prior year data without currency disclosure

[JURISDICTION-SPECIFIC]:

- **EU (Directive 2024/825, in force)**: Greenwashing claims in commercial communications
  are prohibited under existing EU law (Unfair Commercial Practices Directive 2005/29/EC as
  amended). Member states must transpose by March 27, 2026; penalties apply from September 27, 2026. Generic green claims — "eco-friendly," "climate neutral," "sustainable" — without
  verifiable third-party substantiation are banned. Do not rely on the proposed standalone EU
  Green Claims Directive (COM(2023)166) — Commission signaled withdrawal; Directive 2024/825
  is the operative instrument. [VERIFY transposition status in relevant member state]
- **UK (CMA Green Claims Code, 2021)**: Six enforceable principles for green claims under
  Consumer Protection from Unfair Trading Regulations 2008. CMA has taken enforcement action.
  [VERIFY current enforcement priorities]
- **US (FTC Green Guides, 16 C.F.R. Part 260)**: Guidance on "carbon neutral," "net zero,"
  and "sustainable" claims. Failure to comply creates FTC §5 enforcement risk [VERIFY
  current Green Guides version — review underway as of 2026]

### 11. ESG-Linked Commercial Terms

**Key elements to review:**

- Sustainability-linked loan (SLL) provisions: KPIs, step-up/step-down interest rates, SPT
  (Sustainability Performance Targets), third-party KPI verification. LMA Sustainability-Linked
  Loan Principles require KPIs to be ambitious, relevant, regularly monitored, and externally
  verified at least annually; two-way pricing (step-down on achievement, step-up on miss) is
  now standard market practice.
- ESG-linked pricing adjustments in supply contracts: which ESG metrics trigger adjustments,
  how are they measured, who determines KPI performance, dispute mechanism. The Chancery Lane
  Project Net Zero Standard for Suppliers provides a market-practice price mechanism: 5%
  discount paid to a climate charity if emissions exceed target; 2% rebate if below target;
  1% tolerance threshold; third-party auditor verification [VERIFY current Chancery Lane
  Project clause version]
- Preferred supplier status contingent on ESG performance
- ESG score gating for procurement eligibility
- Green bond / green loan alignment: use of proceeds, reporting, external review
- ESG-linked earn-out or milestone payment provisions in M&A/investment contexts
- Whether KPI definitions are controlled by one party (creating a conflict of interest)

**Common issues:**

- KPI definitions set by one party without independent verification — creates conflict
  of interest and potential for manipulation
- No dispute resolution mechanism for ESG KPI performance disputes
- Step-up penalty for ESG underperformance but no step-down reward for outperformance
  — creates only downside without incentivizing excellence
- Green bond/loan covenant referring to "green projects" without a defined eligible
  project taxonomy
- SPTs set at current performance level — no ambition, no credibility

[JURISDICTION-SPECIFIC]:

- **EU (Green Bond Standard, Regulation 2023/2631/EU)**: European Green Bond Standard
  requirements for green bond proceeds use and external review [VERIFY]
- **ICMA Principles**: Green Loan Principles and Sustainability Linked Loan Principles are
  market standards — contracts should reference the current edition [VERIFY]

### 12. ESG Material Adverse Change & Termination Rights

**Key elements to review:**

- Whether the MAC/MAE definition includes ESG-specific triggers (significant ESG rating
  downgrade, material ESG regulatory violation, greenwashing finding, modern slavery
  discovery, significant carbon target miss)
- Whether ESG breach is a standalone termination trigger or only triggers MAC
- Cure period for ESG breach: is a corrective action plan period provided before termination
  rights arise?
- Force majeure: does the clause cover regulatory changes that make ESG performance
  commercially impractical (e.g., carbon credit market collapse)?
- Transition assistance on ESG-related termination

**Common issues:**

- MAC clause does not mention ESG regulatory violation — a CSDDD enforcement action or
  modern slavery finding that destroys the counterparty's reputation is not a MAC
- No cure period for ESG breach — immediate termination right may be disproportionate
  for a minor reporting failure
- ESG breach termination right covers only statutory violations, not voluntary commitment
  breaches — leaves ESG representations without adequate remedy
- No distinction between material ESG breach (trigger termination) and minor ESG reporting
  failure (trigger cure period only)

### 13. Biodiversity, Water & Circular Economy

**Key elements to review:**

- Biodiversity commitments: net gain pledges, reference to TNFD (Taskforce on Nature-
  related Financial Disclosures) framework, no-net-loss or net positive nature commitments
- Biodiversity baseline: has a biodiversity impact assessment been conducted? Is the
  baseline defined?
- Water stewardship: water consumption targets, watershed risk disclosure, WASH (Water,
  Sanitation and Hygiene) commitments in operations
- Circular economy: recyclability targets, recycled content obligations, product take-back
  obligations, end-of-life management
- Deforestation and land use: EU Deforestation Regulation compliance for relevant
  commodities (cattle, cocoa, coffee, palm oil, soya, wood, rubber and derived products)
- Chemical and hazardous materials management (REACH, RoHS, conflict minerals)

**Common issues:**

- "Net positive biodiversity" claim without a baseline or methodology — greenwashing risk
- TNFD framework reference without specifying whether voluntary alignment or regulatory
  compliance is the standard
- Circular economy commitment ("100% recyclable packaging by 2030") without lifecycle
  assessment or definition of "recyclable" under applicable waste regulation
- EU Deforestation Regulation compliance obligation absent for relevant commodity contracts
  — creates import risk for EU buyers [VERIFY EU DR applicability]

---

## ESG Severity Classification

### GREEN — Meets or Exceeds Standard

The ESG clause aligns with or exceeds the applicable regulatory requirement or market
standard. Substantive, measurable, independently verifiable, and correctly allocated.

**Examples:**

- Net-zero target validated by SBTi with annual interim milestones and third-party assurance
- CSDDD-compliant contractual assurance with defined cascade and audit right
- ESG reporting obligation aligned with ESRS with independent verification and CSRD-ready
  data points

**Action**: Note for awareness. Preserve in negotiation — do not trade away well-drafted
ESG provisions.

### YELLOW — Negotiate

The ESG clause is present but inadequate — aspirational language, missing verification,
absent milestones, or weak audit rights. Commercially common but below best practice.

**Examples:**

- Net-zero commitment without SBTi validation or interim milestones
- Supplier code of conduct without audit right
- ESG reporting obligation without framework specification or assurance requirement
- Modern slavery representation covering operations only, not supply chain

**Action**: Generate specific redline language. Provide a fallback position. Estimate the
risk impact of accepting vs. negotiating.

### RED — Escalate

The ESG clause is absent where a mandatory legal obligation exists, or the provision
creates a material legal or financial risk that requires senior counsel or ESG officer
sign-off.

**Examples:**

- No CSDDD-compliant contractual assurance in a contract between in-scope EU parties
- No Scope 3 data obligation where the buyer is a mandatory CSRD reporter and the supplier
  is a material Scope 3 source
- No modern slavery clause where the UK buyer has a s.54 Modern Slavery Act obligation
- ESG MAC clause absent in an acquisition where ESG litigation risk is material
- No audit right where ESG representations are made — renders representations unverifiable

**Action**: Explain the specific mandatory obligation or material risk, citing applicable
law. Provide market-standard alternative language. Recommend escalation to ESG legal
officer or specialist external counsel.

### GREENWASHING-RISK — Immediate Action Required

A green claim, environmental representation, or sustainability commitment in the contract
is unsubstantiated, vague, or inconsistent with the party's known ESG performance, creating
exposure under FTC §5 (US), CMA Green Claims Code (UK), the EU Green Claims Directive, or
the Unfair Commercial Practices Directive.

**Examples:**

- "Carbon neutral" claim in product description without specifying offset standard,
  verification body, or scope of emissions covered
- "Net zero by 2050" representation without interim targets, SBTi validation, or Scope 3
  coverage — standard prototypical greenwashing language
- "Sustainably sourced" claim without a certification scheme or audit right to verify
- EU Taxonomy alignment claimed without Technical Screening Criteria and DNSH assessment

**Action**: Identify the specific claim, the missing substantiation elements, and the
applicable regulatory framework creating enforcement risk. Provide remediation language:
either (a) remove the claim, (b) qualify the claim with accurate parameters, or (c) require
substantiation with defined verification requirements.

---

## ESG Redline Format

For each YELLOW, RED, and GREENWASHING-RISK item:

```
**ESG Clause**: [Section reference and clause title]
**Severity**: [YELLOW / RED / GREENWASHING-RISK]
**Current language**: "[Exact quote from the contract, or 'ABSENT — clause not present']"
**Issue**: [Specific problem: vague commitment / missing verification / regulatory gap /
  unsubstantiated claim]
**Applicable framework**: [CSDDD Art. 10 / CSRD ESRS E1 / Modern Slavery Act s.54 /
  FTC Green Guides / GHG Protocol / SBTi criteria / etc.]
**Proposed redline**: "[Specific alternative language, ready to insert]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
**Greenwashing risk** (if applicable): [Applicable regulator, enforcement risk, liability]
```

### ESG Redline Best Practices

1. **Be measurable**: ESG redlines must convert aspirational language into specific, verifiable
   obligations. "Best efforts" → "shall achieve X% reduction by [year], measured in accordance
   with GHG Protocol Corporate Standard."
2. **Specify the framework and version**: Never redline to "GRI Standards" without naming the
   edition year. GRI 2021 and GRI 2016 are materially different.
3. **Include verification**: Every ESG representation redline should require third-party
   verification or independent assurance. Self-certification of ESG data has minimal value.
4. **Allocate liability clearly**: For GREENWASHING-RISK items, the redline should specify
   which party bears liability if the claim is found to be false or misleading.
5. **Cascade explicitly**: Supply chain ESG obligations need explicit language requiring the
   counterparty to impose equivalent obligations on their own suppliers.
6. **Reference applicable law**: Cite the specific statute or framework creating the obligation.
   Where citing from memory, mark [VERIFY].
7. **Provide fallback positions**: For YELLOW items, include a minimum acceptable fallback if
   the primary redline is rejected (e.g., if full SBTi validation is not achievable, minimum
   fallback is a defined emissions reduction target with third-party assurance).

---

## ESG Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:

- Mandatory regulatory compliance gaps (CSDDD contractual assurance absent where required,
  Scope 3 data obligation absent where mandatory CSRD reporting depends on it, modern slavery
  clause absent where s.54 applies)
- GREENWASHING-RISK items in representations or product descriptions — present enforceable
  liability that cannot be accepted
- No audit right where ESG representations are material to the deal
- ESG MAC provisions absent in acquisitions where ESG regulatory risk is a deal risk

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Framework specification (adding GRI edition, ISSB S1/S2 reference, SBTi validation timeline)
- Third-party assurance requirements where self-certification is currently the only obligation
- Scope 3 data obligations where the buyer is potentially in scope for California SB 253
- Corrective action plan procedure where audit rights exist but remediation is not defined
- Cascade obligations to Tier 2 suppliers for high-risk supply chains

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve ESG quality but can be conceded strategically:

- Specific framework edition year (acceptable to reference current version)
- CDP questionnaire score targets
- Preferred assurance provider requirements
- Biodiversity and circular economy provisions in supply chains not involving relevant
  commodities
- Board diversity targets where not legally required

**ESG negotiation strategy**: Lead with mandatory regulatory compliance (Tier 1) and frame
as "protecting both parties from regulatory risk." Trade Tier 3 concessions (preferred
assurance provider, specific CDP score targets) to secure Tier 2 wins (third-party
assurance, Scope 3 data).

---

## Quality Assurance Framework

### ESG Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                         | Fail Action                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| **Source**     | Every ESG regulatory claim cites a specific directive, statute, regulation, or established framework provision                                               | Add citation or mark "[UNVERIFIED — ESG counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the applicable instrument (EU Directive citation, USC citation, UK statute reference)             | Fix format                                                   |
| **Currency**   | Every cited ESG provision checked for amendments, phase-in status, or implementation delays — ESG law is moving faster than any other area of commercial law | Flag "[CHECK CURRENCY — ESG law in active development]"      |
| **Domain**     | Analysis correctly identifies which mandatory regime applies to which party. No bleed of EU obligations onto a purely US-regulated party or vice versa       | Remove or flag jurisdictional bleed                          |
| **Confidence** | Uncertainty about mandatory applicability (company size, listing status, jurisdiction) explicitly stated, not hidden                                         | Add confidence qualifier and flag for verification           |

### Self-Interrogation for RED and GREENWASHING-RISK Items

For any clause classified as RED or GREENWASHING-RISK, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute or framework cited?
- Would a regulator (CSRD supervisor, FTC, CMA, CSDDD competent authority) actually find a
  violation on these facts?
- Is there a counter-argument that the counterparty's ESG counsel will make?

**Pass 2 — Completeness**:

- Have all applicable mandatory ESG regimes been considered (EU, US, UK, national)?
- Have framework obligations been considered alongside statutory obligations?
- Is the Scope 3 / supply chain dimension fully assessed?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS adequate?
- Under what commercial circumstances might a reasonable ESG lawyer accept this language?
- Is the RED classification proportionate, or is this YELLOW with disclosure and fallbacks?
- For GREENWASHING-RISK: is there a plausible substantiation basis the party has not yet
  disclosed in the contract?

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material ESG clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                                                           | Action                                                    |
| ------------ | --------- | --------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled ESG law, clear and current regulation, no ambiguity                       | State with confidence                                     |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions or minor phase-in uncertainty    | State with brief caveat                                   |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ (e.g., CSDDD scope is contested) | State with explicit reasoning and contra-indicators       |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., emerging mandatory standard, contested transposition)  | Flag for ESG counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative, or based on proposed law not yet adopted                 | Do not assert; flag "[UNCERTAIN — ESG counsel to advise]" |

Given the speed of ESG law development, apply Probable or Possible confidence to most
regulatory obligation assessments unless the applicable law is fully in force and unambiguous.

---

## Glass Box Audit Trail

Every ESG clause review MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  contract: "[Contract title and date]"
  contract_type: "[Supply / MSA / Loan / Investment / etc.]"
  user_side: "[Buyer / Supplier / Lender / Borrower / Investor / Investee]"
  esg_review_scope: "[Full (13 categories) / Targeted / Regulatory only / Greenwashing only]"
  mandatory_obligations_identified:
    - "[Party A]: [CSRD / CSDDD / Modern Slavery Act / LkSG / etc.] — [In scope / Possibly in scope / Not in scope]"
    - "[Party B]: [applicable regimes]"
  esg_frameworks_referenced_in_contract:
    - "[Framework + version if stated]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-esg-authority.md / Not created]"
  categories_reviewed: 13
  categories_present: "[number]"
  categories_missing: "[number] — [list]"
  greenwashing_risk_items: "[number]"
  red_items: "[number]"
  yellow_items: "[number]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED or GREENWASHING-RISK items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale, noting ESG law currency uncertainty]"
  esg_law_currency_note: "[Specific note on any ESG provisions whose currency was not verified]"
  limitations:
    - "[Mandatory regime applicability depends on company size — not verified from contract]"
    - "[ESG framework versions not specified in contract — assumed current]"
    - "[CSDDD transposition status in [member state] not verified]"
  reviewer: "AI-assisted — requires qualified ESG legal counsel review"
```

---

## Multi-Stakeholder ESG Mapping

For every ESG review, identify all stakeholders affected by the ESG provisions:

| Stakeholder                  | Role          | Relevant ESG Categories | Impact                                  | Action Required                    |
| ---------------------------- | ------------- | ----------------------- | --------------------------------------- | ---------------------------------- |
| [Buyer/Customer]             | Primary party | All 13                  | Primary regulatory and reputational     | Sign / Negotiate                   |
| [Supplier]                   | Primary party | 1–6, 9–10               | Compliance burden, audit exposure       | Sign / Negotiate                   |
| [Tier 2+ Suppliers]          | Indirect      | 3–6                     | CSDDD/LkSG cascade obligation           | Require contractual pass-through   |
| [Supply chain workers]       | Third party   | 3–4                     | Social standards, modern slavery        | Grievance mechanism required       |
| [ESG regulators]             | Regulator     | All                     | CSRD, CSDDD, Modern Slavery enforcement | Regulatory compliance mandatory    |
| [Investors / Lenders]        | Financial     | 1, 7–8, 11–12           | ESG disclosure, SFDR, SDR               | Reporting obligation alignment     |
| [Consumers / End users]      | Third party   | 10                      | Greenwashing exposure                   | FTC/CMA/EU green claims compliance |
| [Carbon market participants] | Market        | 1, 11                   | Offset quality, double-counting         | Article 6 / registry verification  |

---

## Anti-Patterns

What NOT to do when reviewing ESG clauses:

1. **Treating aspirational language as binding commitment** — "We aspire to net zero" and
   "We shall achieve net zero" are not equivalent. Aspirational ESG language creates no
   enforceable obligation. Never classify aspirational clauses as satisfactory without flagging
   the enforcement gap.

2. **Missing the greenwashing liability chain** — A buyer who incorporates a supplier's
   unsubstantiated green claim into its own marketing inherits the greenwashing liability.
   Always trace where green claims originate and where liability sits.

3. **Reviewing ESG law as static** — CSRD phase-in, CSDDD transposition, the EU Green Claims
   Directive adoption, the FTC Green Guides review, and California SB 253/261 implementing
   regulations are all in active development as of 2026. Never state an ESG regulatory
   obligation as settled without a [VERIFY] check for currency.

4. **Treating Scope 1+2 coverage as full ESG reporting** — For most companies, Scope 3
   emissions are 70-90% of their total carbon footprint. A contract that only addresses
   Scope 1+2 while ignoring Scope 3 covers the minority of the climate impact.

5. **Accepting "best efforts" for mandatory ESG obligations** — Where a mandatory ESG
   obligation exists (CSDDD contractual assurance, CSRD Scope 3 data), "best efforts" is not
   a compliant standard. The obligation is either met or not — effort is not the measure.

6. **Confusing voluntary framework alignment with regulatory compliance** — GRI, SASB, and
   TCFD are voluntary frameworks. ESRS (under CSRD) is mandatory for in-scope companies.
   Never allow the voluntary/mandatory distinction to blur in the analysis.

7. **Ignoring the cascade gap** — A CSDDD-compliant direct supplier obligation is worthless
   if the supplier has no contractual right to impose equivalent obligations on its own
   suppliers. The cascade must be legally achievable all the way down the chain.

8. **Accepting un-versioned framework references** — "In accordance with GRI" or "aligned
   with TCFD" without a version or edition year cannot be audited or enforced. The GRI 2021
   Universal Standards are materially different from earlier editions.

9. **Treating ESG audit rights as equivalent to ESG assurance** — An internal audit by the
   buyer's team and an independent third-party ISAE 3000 assurance engagement are not the
   same. Confusing them understates the verification gap.

10. **Ignoring the confidentiality vs. regulatory disclosure conflict** — An ESG reporting
    obligation in a supply contract may be blocked by confidentiality provisions if the
    receiving party cannot use the ESG data in mandatory CSRD disclosures. Always check for
    this conflict.

11. **Applying a single jurisdiction's ESG framework to a cross-border contract** — A contract
    between a German company (LkSG scope) and a UK company (Modern Slavery Act scope) and a
    US company (UFLPA exposure) has three overlapping mandatory ESG regimes. Each must be
    mapped separately.

12. **Single-pass ESG analysis** — ESG clauses interact. A Scope 3 data obligation is
    unenforceable without audit rights. An ESG termination right is disproportionate without
    a corrective action plan cure period. An SBTi commitment is unachievable without Scope 3
    data from the supply chain. Read the whole contract before classifying any ESG clause.

13. **Accepting "applicable law compliance" as an ESG standard** — Applicable law compliance
    for social and labor standards may mean compliance with local laws that permit child labor
    at 14 or do not protect freedom of association. An ESG clause that merely requires legal
    compliance in jurisdictions with weak ESG law provides no meaningful protection.

14. **Skipping biodiversity and circular economy because "they're emerging"** — The EU
    Deforestation Regulation (DR 2023/1115/EU) is in force for relevant commodity contracts.
    TNFD disclosures are moving toward mandatory. Biodiversity net gain is already law for
    UK developments. These are not hypothetical obligations.

15. **Conflating "carbon neutral" with "net zero"** — "Carbon neutral" typically refers to
    balancing current emissions with offsets. "Net zero" typically means achieving the maximum
    feasible real reductions and then offsetting only residual emissions. They are not
    interchangeable and treating them as such creates GREENWASHING-RISK.

16. **Missing the materiality assessment gap** — ESG representations that survive a materiality
    qualifier ("in all material respects") need a definition of what is "material" for ESG
    purposes. Without this, the representation is unenforceable for all but the most egregious
    misstatements.

17. **Forgetting the ESG insurance gap** — Standard commercial insurance policies typically do
    not cover ESG-related regulatory fines (CSDDD penalties, modern slavery enforcement),
    greenwashing claims, or carbon credit invalidation. An ESG clause without insurance
    alignment may leave the beneficiary party unprotected.

18. **Assuming SBTi validation is self-executing** — Stating "targets are consistent with SBTi"
    does not mean they are SBTi-validated. Validation requires submission, review, and approval
    by the SBTi. If validation is referenced, the contract must specify the submission deadline,
    the standard (Near-term 1.5°C, Net-Zero standard, FLAG for land-use), and the fallback if
    validation is not achieved.

19. **Overlooking double-counting in carbon offsets** — Carbon credits may be claimed by both
    the issuing entity and the purchasing entity. Under Article 6 of the Paris Agreement,
    Corresponding Adjustments are needed for internationally transferred credits to avoid
    double-counting. A contract that allows use of non-Article-6-compliant offsets without
    Corresponding Adjustments may produce non-compliant carbon accounting.

20. **Treating greenwashing risk as low because enforcement is nascent** — ESG enforcement is
    accelerating in all three jurisdictions. EU Directive 2024/825 (in force; penalties from
    September 27, 2026) bans generic green claims without substantiation. The CMA has already
    taken enforcement action under existing UK law. The FTC has issued warning letters on "net
    zero" claims. What feels low-risk in 2024 may attract fines and contract exclusions by 2027.

21. **Citing CSDDD pre-Omnibus I thresholds** — The original CSDDD threshold (1,000 employees /
    €450M turnover, phased application 2026-2029) was revised by Omnibus I (December 2025): the
    single application date is July 26, 2029 and the threshold raised to 5,000 employees AND
    €1.5B worldwide turnover. Contracts or analyses citing the old thresholds or the old phased
    timeline are materially incorrect. Verify which version of the CSDDD applies before advising
    on scope.

22. **Treating California SB 261 as binding** — California SB 261 (Climate-Related Financial
    Risk Act) was enjoined by the Ninth Circuit Court of Appeals in November 2025 and is not
    currently enforceable. Do not cite SB 261 as a current binding obligation. California SB 253
    (Scope 1, 2, 3 reporting for companies with $1B+ revenue in California, first deadline August
    10, 2026 for Scope 1/2) is unaffected and remains in force.

23. **Confusing EU Directive 2024/825 with the proposed standalone Green Claims Directive** —
    The operative EU greenwashing instrument is Directive 2024/825 (Empowering Consumers for the
    Green Transition), which amends the Unfair Commercial Practices Directive and has been in force
    since 2024 with penalty provisions from September 27, 2026. The proposed standalone EU Green
    Claims Directive (COM(2023)166) has been signaled for withdrawal by the Commission as of 2026
    and is not operative law. Citing the proposed standalone GCD as a current obligation — while
    ignoring the in-force Directive 2024/825 — is a double error: it misstates what is currently
    enforceable.

24. **Advising on German LkSG without confirming current legislative status** — The German
    coalition government announced intent to abolish the Lieferkettensorgfaltspflichtengesetz
    (LkSG) in March 2026. Formal repeal legislation status is uncertain as of mid-2026. Do not
    advise that LkSG obligations are currently in force without confirming the repeal has not been
    enacted; do not advise that LkSG has been repealed without confirming the repeal legislation
    is in effect. Either error can lead to misjudged commercial concession or false compliance
    assurance.

25. **No ESG incident reporting obligation** — A contract that creates ESG standards but omits
    any obligation to report ESG incidents (modern slavery discovered in the supply chain,
    environmental spills, UFLPA Entity List designations, regulatory enforcement actions) leaves
    the beneficiary party dependent on external discovery. By the time an ESG incident is
    discovered through press coverage or a regulatory notice, the beneficiary party's own
    disclosure obligations and litigation posture are already compromised. Require the
    counterparty to notify within 5-10 business days of any material ESG incident.

---

## Writing Standards

Apply plain-language discipline to all ESG review output:

**For ESG redline rationales** (shared with counterparty's counsel):

- Active voice: "This clause does not require Scope 3 data" not "Scope 3 data is not required
  by this clause"
- Specific, not vague: "CSDDD Art. 10 requires contractual assurance from direct business
  partners in scope" not "applicable EU sustainability law may require additional provisions"
- Name the standard: cite the specific framework or statute rather than "ESG best practice"
- Avoid advocacy language: state the gap factually; do not editorialize

**For internal ESG analysis**:

- Confidence qualifiers where genuinely uncertain (ESG law is still developing)
- Distinguish between mandatory obligations and market standard (the distinction is material)
- Distinguish between aspirational and binding commitment — use "commits to" vs. "aspires to"
- Distinguish between Scope 1, 2, and 3 emissions explicitly — never say "emissions" alone

**Quality gates before delivery**:

1. Does the executive summary clearly distinguish mandatory compliance gaps (RED) from
   market-standard improvements (YELLOW) from greenwashing risk (GREENWASHING-RISK)?
2. Is every ESG regulatory obligation cited with a specific instrument reference?
3. Are confidence levels applied to all mandatory regime applicability assessments?
4. Can an ESG professional immediately identify the most critical action items?
5. Are any ESG framework references missing version/edition years? If yes, flag for addition.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for the current transposition status of CSDDD in relevant member states
- Search for the current CSRD phase-in schedule and applicable categories
- Verify the current status of the EU Green Claims Directive legislative process
- Verify the current status of SEC climate disclosure rules
- Verify California SB 253/261 implementing regulations and effective dates
- Retrieve TCFD mandatory disclosure requirements for UK companies
- Save results to `/tmp/legalcode-esg-authority.md`
- Mark all legalcode-mcp-sourced references as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all ESG regulatory obligation references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — ESG regulatory currency requires verification"`
- Given the pace of ESG law development, the [VERIFY] flag is especially important: provisions
  that were correct 12 months ago may already be superseded

**ESG-specific caution**: ESG law is the area of commercial law most likely to have changed
since any AI model's training cutoff. Always treat ESG regulatory references as requiring
current-source verification.

---

## Output Format Template

Structure the final deliverable as:

```markdown
## ESG Clause Review Summary

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [buyer/supplier/etc.]
**Contract Type**: [supply agreement / MSA / loan / investment / etc.]
**Governing Law**: [jurisdiction from contract]
**ESG Review Scope**: [Full / Targeted / Regulatory compliance / Greenwashing]
**Date of Review**: [date]
**Review Basis**: [ESG playbook / Market standards / Regulatory minimum]

---

## Mandatory ESG Obligations Map

[Table per Step 4 — identify which mandatory ESG regimes apply to each party]

---

## Key ESG Findings

[Top 3-5 issues with severity flags (RED / GREENWASHING-RISK / YELLOW) and one-line summaries]

---

## Greenwashing Risk Summary

[List all GREENWASHING-RISK items with specific claims, missing substantiation, and
applicable regulatory framework. Quantify liability exposure where possible.]

---

## Missing ESG Clauses

[List ESG clause categories that are absent, with severity assessment and mandatory
obligation basis where applicable]

---

## ESG Clause-by-Clause Analysis

### [ESG Clause Category] — [GREEN / YELLOW / RED / GREENWASHING-RISK] | Confidence: [level]

**Contract says**: [summary of the provision, or "ABSENT"]
**Standard / Requirement**: [applicable mandatory obligation or market standard]
**Gap**: [specific deficiency]
**Regulatory basis**: [CSDDD Art. X / CSRD ESRS E1-6 / Modern Slavery Act s.54 / FTC Green
Guides / etc.]
**Business impact**: [what this means practically]
**Redline** (if YELLOW, RED, or GREENWASHING-RISK):

> [Specific proposed language, ready to insert]
> **Priority**: [Must-have / Should-have / Nice-to-have]

[Repeat for each ESG clause category]

---

## ESG Negotiation Strategy

**Tier 1 (Must-Haves — Regulatory Compliance)**: [list]
**Tier 2 (Should-Haves — Material ESG Risk)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, tone, regulatory risk framing]

---

## ESG Stakeholder Impact Map

[Table per Multi-Stakeholder ESG Mapping section]

---

## Next Steps

[Specific actions, owners, and deadlines — distinguish regulatory deadlines from commercial
negotiation timelines]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic and uses [JURISDICTION-SPECIFIC] markers throughout to
flag where local law must be verified and applied. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local ESG law content
2. Replace [VERIFY] tags with confirmed statutory references and their current status
3. Add jurisdiction-specific ESG clause categories (e.g., German LkSG annual risk analysis
   requirements, French Devoir de Vigilance vigilance plan obligations)
4. Add jurisdiction-specific anti-patterns and enforcement risk examples
5. Update the mandatory obligations map to reflect the specific jurisdiction's regime
6. Add relevant case law (enforcement actions, greenwashing decisions, supply chain liability)

**Related skills:**

- **legalcode-supply-chain-contract-review**: For full review of supply agreements, including
  ESG due diligence, pricing, delivery, warranty, and product liability
- **legalcode-esg-clause-reviewer** (this skill): Focused ESG clause review applicable to
  any commercial contract type
- **legalcode-eu-csrd-sustainability-reporting**: CSRD/ESRS compliance assessment
  (see `skills/jurisdictions/european-union/compliance/`)

**Market practice resources** (external, for reference when drafting ESG redlines):

- **Chancery Lane Project** (chancerylaneproject.org/climate-clauses): 18+ actively maintained
  climate-aligned contract clause types including the Net Zero Standard for Suppliers, Supply
  Chain Cascade Clauses, and Carbon Reduction Target clauses — widely adopted as drafting
  starting points for commercial ESG obligations.
- **ABA Model Contract Clauses** (shiftproject.org/aba-contract-clauses): UN Guiding Principles
  on Business and Human Rights (UNGPs)-based model clauses for supply chain human rights due
  diligence, including grievance mechanism requirements.
- **LMA Green Loan Principles and SLL Principles**: Market standard for sustainability-linked
  loan KPI structure, external verification requirements, and two-way pricing mechanics.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis combining EU CSRD/CSDDD/Taxonomy
regulatory framework analysis, US SEC/California climate disclosure requirements, UK TCFD/SDR/
Modern Slavery Act obligations, global ESG framework analysis (GRI, SASB, TCFD, ISSB/IFRS
S1/S2, SBTi, CDP), greenwashing enforcement risk framework (FTC Green Guides, CMA Green
Claims Code, EU Green Claims Directive), supply chain due diligence law (LkSG, Devoir de
Vigilance, Åpenhetsloven, UFLPA), and Legalcode quality assurance methodology (Glass Box
audit trail, 5-gate Citation Quality system, Self-Interrogation, Confidence Scoring, 4-tier
ESG severity classification). Research conducted via web search. All ESG regulatory references
require current-source verification given the pace of ESG law development.
