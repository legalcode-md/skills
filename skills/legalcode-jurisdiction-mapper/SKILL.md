---
name: legalcode-jurisdiction-mapper
description: Produces comparative legal matrices across multiple jurisdictions for privacy and data protection,
  employment law, data localization, consumer protection, contract enforcement, and corporate governance.
  Identifies where legal requirements harmonize, diverge, or directly conflict, and surfaces actionable
  compliance recommendations. Use when planning global operations, structuring cross-border contracts,
  conducting multi-jurisdiction due diligence, designing global compliance programs, preparing regulatory
  filings in multiple markets, or advising on international expansion. Triggers on requests for "compare
  laws across countries," "how does [legal topic] differ in [jurisdictions]," "global compliance matrix,"
  "jurisdiction comparison," "cross-border legal analysis," "which countries require [X]," or "harmonization
  opportunities."
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Jurisdiction Mapper

> ⚠️ **Disclaimer**: This skill provides a framework for AI-assisted multi-jurisdiction
> legal comparison. It does not constitute legal advice. Laws change frequently; all
> outputs must be reviewed by qualified legal professionals licensed in each relevant
> jurisdiction before use. The comparative analysis herein reflects the legal landscape
> as understood from available sources and is marked [VERIFY] wherever specific local
> counsel review is recommended. Jurisdiction-specific legal advice from licensed local
> practitioners is essential before acting on any finding in this matrix.

---

## Purpose and Scope

This skill enables an AI agent to:

- Build comparative legal matrices across user-specified jurisdictions and legal domains
- Identify where requirements are **harmonized**, **divergent**, **conflicting**, or
  **jurisdiction-only** present
- Surface the binding international harmonization frameworks (adequacy decisions, model
  clauses, treaties, OECD guidelines) that reduce compliance burden
- Apply the "highest common denominator" rule to identify a single design that satisfies
  the strictest applicable requirement
- Generate prioritized compliance recommendations ranked by risk exposure and operational impact

**This skill covers these legal domains:**

| Domain                        | What it Maps                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Privacy & Data Protection** | Legal bases, data subject rights, breach notification, cross-border transfer mechanisms, localization               |
| **Employment Law**            | Termination standards, notice periods, mandatory benefits, non-compete enforceability, worker classification        |
| **Data Localization**         | Mandatory in-country storage requirements, sector-specific restrictions, transfer approval regimes                  |
| **Consumer Protection**       | Cooling-off periods, unfair contract terms, product liability, advertising standards                                |
| **Contract Enforcement**      | Civil law vs. common law differences, penalty clauses, limitation of liability, governing law/forum selection, CISG |
| **Corporate Governance**      | Director duties, mandatory disclosures, anti-corruption regimes, ESG reporting requirements                         |

**This skill does not:**

- Provide jurisdiction-specific legal advice (use jurisdiction-specific skills for depth)
- Replace qualified local counsel for implementation
- Produce binding legal opinions
- Map every jurisdiction simultaneously without scoping (focus on 2–15 jurisdictions per run)

**Related skills**: `legalcode-contract-review` (contract clause analysis), `legalcode-ma-due-diligence-checklist` (M&A diligence), `legalcode-employment-agreement-review` (employment-specific depth)

---

## Jurisdiction and Governing Law

This is a **jurisdiction-comparative** skill — it operates simultaneously across multiple
legal systems rather than within one. Key framework conventions:

- **[JURISDICTION-SPECIFIC]** markers appear where rules differ materially by jurisdiction
- All cited legal authority is marked **VERIFIED** (sourced via legalcode-mcp or authoritative
  government/regulatory sources) or **[VERIFY]** (requires local counsel confirmation)
- When requirements conflict, the skill identifies the conflict explicitly and presents
  options — it does not silently pick one jurisdiction's rule as "the answer"
- For EU member states: EU-level directives and regulations are noted separately from
  national implementing legislation, which may add additional requirements

**Legal tradition classification used throughout:**

| Tradition                 | Examples                                              | Key Characteristics                                                                |
| ------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Common Law**            | US, UK, Australia, Canada, India, Singapore, HK       | Precedent-driven; penalty clauses void if punitive; at-will employment possible    |
| **Civil Law**             | EU member states, Brazil, Japan, China, Latin America | Code-driven; penalty clauses generally valid; just-cause termination default       |
| **Mixed**                 | Scotland, South Africa, Quebec, Philippines           | Hybrid elements; research the specific mix                                         |
| **Nordic**                | Iceland, Norway, Sweden, Denmark, Finland             | Civil law base + strong good-faith obligations + collective bargaining integration |
| **Religious Law Overlay** | Saudi Arabia, Malaysia (Islamic finance), Iran        | Additional compliance layers; interest prohibitions; Sharia structuring            |

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** points at key decision forks where your answer determines
the analytical direction. When a CLARIFY point is reached:

1. Present the structured options as written
2. Wait for the user's selection before proceeding
3. Record the selection as a parameter for the rest of the analysis

In batch/automated runs, proceed with the defaults noted at each CLARIFY point.

---

## Workflow

### Step 1: Accept Input

Accept inputs in any of these formats:

- **Topic + jurisdictions**: "Compare GDPR and CCPA privacy requirements" or "Employment
  law: EU, US, Brazil, Japan"
- **Use case driven**: "We are expanding to Germany, Japan, and Brazil — what changes for
  our employment contracts?"
- **Domain sweep**: "Privacy compliance matrix for our 8 operating jurisdictions: [list]"
- **Harmonization focused**: "Where can we use one contract template across the EU?"
- **Conflict detection**: "Our US MSA — which clauses break in France and Germany?"

### Step 2: Gather Context

**⟁ CLARIFY** — Before building the matrix, ask these scoping questions. Skip any
already answered by the input:

1. **Legal domain(s)**: Which area(s) should the matrix cover?
   - Options (select all that apply): Privacy/Data Protection, Employment Law,
     Data Localization, Consumer Protection, Contract Enforcement, Corporate Governance,
     All applicable domains
   - _Why this matters_: Each domain produces a separate matrix layer; scoping prevents
     information overload and keeps the analysis actionable.

2. **Jurisdictions**: Which jurisdictions should be compared?
   - Options: Specify list (e.g., "EU, US, UK, Brazil, Japan"), OR provide use case
     and let the skill select the most relevant 5–12 jurisdictions
   - Recommended maximum per run: **15 jurisdictions** for manageable depth
   - _Why this matters_: Jurisdiction count controls matrix depth vs. breadth tradeoff.

3. **Use case**: What decision will this matrix inform?
   - Options: Global contract template design, M&A/investment due diligence, International
     expansion planning, Compliance program design, Regulatory filing/registration,
     Litigation/dispute forum analysis, Policy/government affairs, Executive briefing only
   - _Why this matters_: A "contract template design" use case focuses on clause-level
     differences; an "executive briefing" use case needs 1-page heat maps.

4. **Home jurisdiction**: What is the organization's primary operating jurisdiction?
   - _Why this matters_: The home jurisdiction becomes the baseline; deviations are
     measured from it. Identifies the additional compliance burden for each market.

5. **Detail level**: How deep should each jurisdiction entry go?
   - Options: **Summary** (1–2 sentence per cell, executive matrix), **Standard** (key
     requirements with citations), **Deep** (clause-level with specific statutory text,
     enforcement data, and recent developments)
   - _Why this matters_: Sets expectations and determines output length.

**Batch default**: Domain = all applicable; jurisdictions = user-specified or top 10 by
relevance; use case = compliance program design; home = jurisdiction-agnostic; detail = Standard.

### Step 3: Load Legal Authority

Use **legalcode-mcp** to search for governing law in each jurisdiction for each selected
domain. Structure the search as:

```
Query pattern: "[domain] law [jurisdiction] requirements 2024 2025"
Secondary query: "[domain] enforcement actions [jurisdiction] recent"
Tertiary query: "harmonization [domain] [jurisdiction list] treaty adequacy"
```

Save results to `/tmp/legalcode-jurisdiction-mapper-research.md` with this structure:

```markdown
# Jurisdiction Mapper Research

## Date: [date]

## Domains: [list]

## Jurisdictions: [list]

### [Domain]

#### [Jurisdiction]

- Governing law: [statute/regulation with citation]
- Key requirements: [bullet list]
- Recent developments: [post-2023 amendments]
- Enforcement authority: [regulator]
- Penalty exposure: [maximum fine or sanction]
- Source: [VERIFIED / [VERIFY]]
```

**Without legalcode-mcp**: Proceed using the legal frameworks documented in this skill
(Steps 5–10). Mark all specific statutory citations with [VERIFY]. Note in the Glass Box:
`legalcode_mcp: "Not connected"`.

### Step 4: Apply Harmonization Framework Overlay

Before building the per-domain matrices, identify which international frameworks reduce
the compliance burden across the selected jurisdictions:

**Privacy/Data Protection:**

- EU GDPR adequacy decisions (check current list — updated periodically)
- UK adequacy regulations (mirrors EU list with differences post-Brexit)
- APEC CBPR / Global CBPR Forum membership
- Binding Corporate Rules (BCRs) — covers intra-group transfers in EU and UK
- Standard Contractual Clauses (EU SCCs 2021; UK IDTAs; Brazil ANPD template)

**Employment:**

- ILO Core Conventions (ratification status per jurisdiction)
- EU Minimum Wage Directive 2022/2041 (applies to all EU member states)
- EU Platform Work Directive 2024 (employment presumption for platform workers)

**Contract Enforcement:**

- New York Convention on Arbitration (172 member states — gold standard enforcement)
- Hague Convention on Choice of Court Agreements 2005 (limited parties — ~40 states)
- CISG (97 states — applies by default to B2B goods sales unless opted out)
- Rome I Regulation (EU) — governing law choice for contractual obligations

**Consumer Protection:**

- EU Consumer Rights Directive 2011/83/EU (applies across all EU member states)
- OECD Consumer Policy Toolkit
- UN Guidelines for Consumer Protection

**Anti-Corruption:**

- OECD Anti-Bribery Convention (44 member states)
- UN Convention Against Corruption (UNCAC) — 190+ parties

Record which frameworks apply and note where they reduce the need for jurisdiction-specific
customization. These appear in the output as **COVERED BY [FRAMEWORK]** tags.

### Step 5: Build the Comparison Matrix — Privacy & Data Protection

**⟁ CLARIFY** — Skip if not selected in Step 2 or if not relevant to the use case.

For each selected jurisdiction, populate this matrix:

#### Privacy Comparison Matrix

| Dimension                              | [JX 1]           | [JX 2] | [JX 3] | Harmonization Status |
| -------------------------------------- | ---------------- | ------ | ------ | -------------------- |
| **Legal basis for processing**         |                  |        |        |                      |
| **Consent model**                      | opt-in / opt-out |        |        |                      |
| **Special category data**              |                  |        |        |                      |
| **Data subject rights**                |                  |        |        |                      |
| **Breach notification — authority**    |                  |        |        |                      |
| **Breach notification — individuals**  |                  |        |        |                      |
| **Cross-border transfer mechanism**    |                  |        |        |                      |
| **Data localization requirement**      |                  |        |        |                      |
| **DPO/privacy officer required**       |                  |        |        |                      |
| **Privacy notice requirements**        |                  |        |        |                      |
| **Children's data age threshold**      |                  |        |        |                      |
| **Penalty exposure (maximum)**         |                  |        |        |                      |
| **Enforcement authority**              |                  |        |        |                      |
| **Effective date / recent amendments** |                  |        |        |                      |

**Reference data for common jurisdictions:**

[JURISDICTION-SPECIFIC]

**EU GDPR (Reg. 2016/679)** [VERIFIED]:

- Legal basis: 6 lawful bases (Art. 6); sensitive data: 10 bases (Art. 9)
- Consent model: Opt-in; freely given, specific, informed, unambiguous
- Breach to authority: 72 hours; to individuals: without undue delay (high risk)
- Transfer mechanisms: Adequacy decisions; SCCs (2021 revised, 4 modules); BCRs; Art. 49 derogations
- Penalty: €20M or 4% global annual turnover (higher)
- Regulator: Lead supervisory authority (one-stop-shop for cross-border)

**UK GDPR (UK GDPR + Data Protection Act 2018)** [VERIFIED]:

- Mirrors EU GDPR structure post-Brexit; enforcement via ICO
- Transfer mechanisms: IDTAs (UK-specific); UK Addendum to EU SCCs; adequacy regulations
- Penalty: £17.5M or 4% global annual turnover
- UK adequacy renewed December 2025 (4-year term)

**US — CCPA/CPRA (Cal. Civ. Code §§ 1798.100–1798.199.100)** [VERIFIED]:

- No omnibus federal privacy law; state-by-state patchwork (CA, CO, CT, VA, TX, FL, WA, etc.)
- CCPA/CPRA model: Opt-out for sale/sharing; opt-in for sensitive PI and minors under 16
- No mandatory breach notification to authority (state AG notification thresholds vary)
- No formal cross-border transfer mechanism; extraterritorial reach through revenue/user thresholds
- Fine: $2,500/unintentional violation; $7,500/intentional; $100–$750/consumer/incident (civil)

**Brazil LGPD (Law No. 13.709/2018)** [VERIFIED]:

- Legal basis: 10 bases (Art. 7) — mirrors GDPR structure; consent = opt-in
- Breach to authority (ANPD): 3 business days
- Transfer mechanisms: Adequacy (EU mutual adequacy January 2026); SCCs (ANPD template,
  mandatory by August 2025); BCRs; ANPD authorization
- Penalty: 2% of Brazil revenue, capped at R$50M per infraction

**China PIPL (Law of 2021)** [VERIFIED]:

- Legal basis: Consent is primary default; 6 additional bases
- Consent model: Opt-in; separate consent for sensitive data; explicit consent for overseas transfer
- Breach: "Immediately" remediate; notify authority without delay; simultaneous individual notification
- Transfer: CAC Security Assessment (mandatory for: CII; >1M individuals; cumulative >100K/500K);
  Standard Contracts (100K–1M records; CAC filing required); CBDT Certification
- Penalty: RMB 50M or 5% global revenue (serious violations)

**Singapore PDPA (Personal Data Protection Act 2012, amended 2021)** [VERIFIED]:

- Consent-based; comparable protection standard for overseas transfers
- Breach to authority (PDPC): 3 calendar days if significant harm or 500+ individuals
- Penalty: S$1M or 10% Singapore annual turnover (higher) — 2021 amendment
- Mandatory DPO for organizations processing significant personal data

**Japan APPI (amended 2022)** [VERIFY]:

- Opt-in for sensitive data; opt-out available for anonymous third-party transfers
- Breach notification: Preliminary 3–5 days; Final report 30 days (60 for malicious)
- Cross-border transfer: Consent; equivalency designation (EU and UK designated); APEC CBPR
- No mandatory data localization; but "retained personal information" concept applies

**India DPDP Act 2023** [VERIFY — implementing rules pending]:

- Consent: "Free, specific, informed, unconditional, unambiguous" affirmative action
- Legal basis: Consent OR 9 "legitimate uses" (employment, state functions, etc.)
- Breach: Without delay + detail within 72 hours
- Cross-border: Unrestricted except to prohibited countries (government list pending)
- Significant Data Fiduciaries: additional restrictions (rules pending)

**Australia Privacy Act 1988 (amended 2024)** [VERIFIED]:

- 13 Australian Privacy Principles; no formal legal basis list — "reasonably necessary" standard
- Breach (NDB scheme): 30-day assessment; notify OAIC + individuals simultaneously if serious harm likely
- Cross-border: APP 8 — reasonable steps; no formal adequacy mechanism
- Penalty post-2024 amendment: AU$50M or 3x benefit or 30% annual turnover (highest)

**Canada PIPEDA (+ provincial laws)** [VERIFIED]:

- 10 fair information principles; consent foundational; commercial activity scope
- Breach: As soon as feasible (to OPCC + affected individuals if real risk of significant harm)
- No formal adequacy mechanism; comparable protection standard
- Quebec Law 25 (in force 2022–2023): adds GDPR-like requirements for Quebec-based organizations

**Saudi Arabia PDPL (2021, effective 2024)** [VERIFY]:

- Consent-based primary framework
- Breach to authority (SDAIA): 72 hours
- Penalty: SAR 5M standard; SAR 3M + 2 years imprisonment for sensitive data violations

**Indonesia PDP Law 2022** [VERIFY]:

- Opt-in consent; 3-day breach notification (authority + individuals)
- 2% annual income penalty; IDR 5B criminal fine; 5 years imprisonment
- No blanket localization; sector-specific rules (health, financial) impose stricter requirements

### Step 6: Build the Comparison Matrix — Employment Law

**⟁ CLARIFY** — Skip if not selected in Step 2.

#### Employment Law Comparison Matrix

| Dimension                               | [JX 1]               | [JX 2] | [JX 3] | Harmonization Status |
| --------------------------------------- | -------------------- | ------ | ------ | -------------------- |
| **Termination standard**                | at-will / just cause |        |        |                      |
| **Notice period (statutory minimum)**   |                      |        |        |                      |
| **Severance / redundancy pay**          |                      |        |        |                      |
| **Non-compete enforceability**          |                      |        |        |                      |
| **Non-compete: compensation required?** |                      |        |        |                      |
| **Non-compete: maximum duration**       |                      |        |        |                      |
| **Worker classification test**          |                      |        |        |                      |
| **Minimum wage (per month/hour)**       |                      |        |        |                      |
| **Mandatory paid leave (days/year)**    |                      |        |        |                      |
| **Maternity/parental leave**            |                      |        |        |                      |
| **Works council / union consultation**  |                      |        |        |                      |
| **Mass layoff notification**            |                      |        |        |                      |
| **IP assignment: employee inventions**  |                      |        |        |                      |
| **Written contract mandatory?**         |                      |        |        |                      |

**Reference data for common jurisdictions:**

[JURISDICTION-SPECIFIC]

**United States (Federal + key state variations)** [VERIFIED]:

- Termination: At-will (federal default); just cause required post-probation in many states
  for public sector; WARN Act: 60-day notice for mass layoffs (100+ employees, plant closing/
  mass layoff affecting 50+ workers)
- Non-compete: FTC rule vacated 2024; state law governs; void in CA, MN, ND, OK;
  enforceable with legitimate business interest in most other states; no mandatory compensation
- Worker classification: Economic realities test (FLSA); ABC test in CA (AB5) and other states
- IP assignment: Work-for-hire doctrine + assignment agreements; CA Labor Code §2870 carve-outs

**United Kingdom (Employment Rights Act 1996 + forthcoming ERA 2025 amendments)** [VERIFIED]:

- Termination: Unfair dismissal protection after 2-year qualifying period (moving to 6-month
  probationary period under Employment Rights Bill 2024); automatically unfair grounds (pregnancy,
  whistleblowing, H&S)
- Notice: 1 week/year of service up to 12 weeks statutory minimum
- Non-compete: Enforceable if reasonable; no mandatory compensation; garden leave preferred
- Works council: No German-style works council; TUPE and collective consultation for 20+
  redundancies (90-day consultation)
- IP assignment: CDPA 1988 s.11(2) employer owns copyright in course of employment;
  Patents Act 1977 s.39 employee inventions

**Germany (KSchG + BGB + BetrVG)** [VERIFIED]:

- Termination: Just cause required after 6-month probation; social selection (seniority, age,
  dependents) applies to operational dismissals; KSchG applies 10+ employees
- Notice: 4 weeks (<2 years) to 7 months (20+ years statutory scale)
- Non-compete: Enforceable with compensation (minimum 50% of average remuneration); maximum
  24 months; written agreement required
- Works council (Betriebsrat): Mandatory consultation before any dismissal; co-determination
  rights on social matters; blocking rights on certain HR decisions
- Minimum wage: €13.90/hour (January 2026) [VERIFY current rate]

**France (Code du travail)** [VERIFIED]:

- Termination: Just cause (motif réel et sérieux) for personal dismissal; economic
  justification + mandatory social plan (PSE) for mass dismissals
- Non-compete: Enforceable with financial compensation (negotiated; typically 30–50% of salary);
  typically max 2 years; geographic and activity limits required
- Works council (CSE): Mandatory consultation; blocking rights; BDES data sharing obligations
- 35-hour working week standard; 25 days paid leave minimum

**Japan** [VERIFY]:

- Termination: "Objective, justifiable and reasonable" cause; courts strictly apply abuse of
  dismissal doctrine; virtually impossible to dismiss regular (seishain) employees without consent
- Non-compete: Generally disfavored; enforceable only with financial consideration; limited
  scope and geography; courts scrutinize closely
- IP assignment: Generally employer owns work-product created in course of employment;
  specific assignment agreement recommended for R&D

**Brazil (CLT — Consolidação das Leis do Trabalho)** [VERIFIED]:

- Termination: Just cause under CLT Art. 482 (limited grounds); without-cause dismissal triggers:
  40% FGTS penalty + notice period + proportional 13th month + vacation
- Non-compete: Requires compensation (50–100% of final salary); typically 6–24 months;
  courts assess reasonableness
- FGTS: 8% monthly employer contribution (severance fund); INSS social security contributions
- 13th month (décimo terceiro): Mandatory annual bonus equivalent to one month's salary

**China (Labor Contract Law 2007, amended 2013)** [VERIFIED]:

- Written contract mandatory within 1 month of commencement
- Termination: Requires statutory grounds; 30-day notice or salary in lieu; no mass layoff
  without advance government approval
- Non-compete: Only for senior management, senior technicians, confidentiality-bound employees;
  monthly compensation during restriction (minimum 30% of average salary); maximum 2 years
- Social insurance: Pension, medical, unemployment, work injury, maternity (employer share varies
  by city)
- Housing Provident Fund: Additional employer contribution (typically 5–12%)

**India (IR Code 2020 + legacy Labour Laws)** [VERIFY — IR Code implementation incomplete]:

- Termination: 1-month notice individual; 3 months + government permission (retrenchment
  compensation) for establishments with 300+ workers (threshold under IR Code 2020)
- Non-compete post-employment: Generally void as restraint of trade under Indian Contract Act;
  non-solicitation and confidentiality clauses enforceable
- Mandatory provident fund + ESIC contributions; 26 weeks paid maternity leave

**Australia (Fair Work Act 2009)** [VERIFIED]:

- Termination: Valid reason required (capacity, conduct, or genuine redundancy); unfair dismissal
  protection after minimum employment period; conciliation + Fair Work Commission
- Non-compete: Enforceable if reasonable; no compensation requirement; typically 6–12 months
- Superannuation: 11.5% employer contribution (from July 2024); NMW reviewed annually
- Paid parental leave: 18 weeks government-funded (expanding to 26 weeks by 2026)

### Step 7: Build the Comparison Matrix — Data Localization

**⟁ CLARIFY** — Skip if not selected in Step 2.

#### Data Localization Requirements Matrix

| Jurisdiction     | General Localization Law                                                        | Sector-Specific Requirements                                   | Overseas Transfer Process                                   | Enforcement                                         |
| ---------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| **China**        | Yes — PIPL + DSL; domestic storage required                                     | Financial, health, transport, energy: additional restrictions  | CAC Assessment / Standard Contract / CBDT Certification     | CAC; significant penalties                          |
| **Russia**       | Yes — 152-FZ Art. 18.1: initial recording/storage must be in Russia             | Financial, state data: absolute restrictions                   | Post-initial-storage transfer permitted                     | Roskomnadzor; website blocking (LinkedIn precedent) |
| **Saudi Arabia** | No blanket law; cross-border requires adequate protection                       | Health, financial: sector-specific localization                | SDAIA-approved mechanisms                                   | SDAIA                                               |
| **Indonesia**    | PDP Law: no blanket; Government Reg. 71/2019: "strategic" data for ESPs         | Health (Ministry of Health), financial (OJK)                   | Equivalent protection + contracts                           | Kominfo; OJK                                        |
| **Vietnam**      | Cybersecurity Law Art. 26: social networks, search engines, e-commerce, payment | Same as general law                                            | Ministry of Public Security notification for important data | Ministry of Public Security                         |
| **India**        | DPDP Act: no localization currently; prohibited countries list pending          | RBI, SEBI, IRDAI: financial/securities data restrictions       | Unrestricted (pending prohibited list)                      | DPBI (Board under MEITY)                            |
| **Nigeria**      | NDPR: significant processors must store locally or certified comparable         | Central Bank: financial data                                   | Consent + contractual safeguards                            | NITDA                                               |
| **EU/EEA**       | No localization; free flow within EEA                                           | NIS2 critical infrastructure: domestic processing preference   | Adequacy decisions / SCCs / BCRs / Art. 49 derogations      | Lead SA + EDPB                                      |
| **US**           | No federal localization; state health/financial data rules                      | HIPAA, GLBA, FedRAMP, ITAR/EAR, CLOUD Act                      | N/A (data sovereignty via CLOUD Act)                        | HHS, FTC, sector regulators                         |
| **Brazil**       | No localization under LGPD                                                      | Central Bank: Circular 3.909 financial data requirements       | Adequacy / ANPD SCCs / BCRs                                 | ANPD                                                |
| **Australia**    | No localization; APP 8 requires reasonable steps for overseas recipients        | APS Cloud Computing Policy: government data onshore preference | Contractual protections                                     | OAIC                                                |
| **Japan**        | No localization                                                                 | Financial services: FSA guidance on cross-border data sharing  | Consent / equivalency / APEC CBPR                           | PPC                                                 |

**Conflict identification**: China (localization) ↔ GDPR (data minimization, right to erasure) creates
inherent tension for organizations with data subjects in both jurisdictions. Architecture
solution: data segregation by subject nationality/residency.

### Step 8: Build the Comparison Matrix — Consumer Protection

**⟁ CLARIFY** — Skip if not selected in Step 2.

#### Consumer Protection Comparison Matrix

| Dimension                                 | [JX 1] | [JX 2] | [JX 3] | Harmonization Status |
| ----------------------------------------- | ------ | ------ | ------ | -------------------- |
| **Distance/online cooling-off period**    |        |        |        |                      |
| **Off-premises cooling-off period**       |        |        |        |                      |
| **Unfair contract terms — standard**      |        |        |        |                      |
| **Unfair contract terms — B2B extension** |        |        |        |                      |
| **Product liability standard**            |        |        |        |                      |
| **Digital products / AI liability**       |        |        |        |                      |
| **Advertising substantiation standard**   |        |        |        |                      |
| **Auto-renewal / subscription rules**     |        |        |        |                      |
| **Regulator**                             |        |        |        |                      |
| **Maximum consumer penalty**              |        |        |        |                      |

**Reference data for common jurisdictions:**

[JURISDICTION-SPECIFIC]

- **EU CRD (Dir. 2011/83/EU)**: 14-day cooling-off for distance/off-premises; significant
  imbalance standard for unfair terms (Dir. 93/13); 2024 Product Liability Directive extends
  to software, AI, digital products; DSA + DMA platform obligations
- **UK (Consumer Rights Act 2015 + Consumer Contracts Regulations 2013)**: 14-day cooling-off;
  CRA s.62 fairness standard; 2024 DMCCA (Digital Markets, Competition and Consumers Act)
  new subscription/auto-renewal rules
- **US (FTC Act § 5 + state UDAP laws)**: 3-day federal cooling-off (door-to-door only);
  no federal unfair terms law; FTC Green Guides, Endorsement Guides, Made in USA; state AGs
  active in enforcement
- **Australia (ACL)**: Cooling-off for unsolicited agreements (10 days); extended UCT to
  small business (from Nov 2023); AUD 50M penalty for serious UCT violations; strict
  product liability for manufacturers
- **Brazil (CDC)**: 7-day cooling-off for distance/off-premises; CDC Art. 51 void terms
  list; PROCON + SENACON enforcement; full supply chain strict liability
- **China (Consumer Protection Law + E-Commerce Law 2019)**: 7-day cooling-off for online
  sales (with exceptions); platform operator joint liability for hosted sellers

### Step 9: Build the Comparison Matrix — Contract Enforcement

**⟁ CLARIFY** — Skip if not selected in Step 2.

#### Contract Enforcement Comparison Matrix

| Dimension                   | Common Law (UK/US/AU)                                            | Civil Law (EU/BR/JP)                                             | China                                                                        | Notes                                                                                                  |
| --------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Penalty clauses**         | Void if punitive; only liquidated damages (genuine pre-estimate) | Generally valid; court may reduce if manifestly excessive        | Valid; court can reduce                                                      | **CONFLICTING** — use "liquidated damages" language universally                                        |
| **Limitation of liability** | Enforceable unless unconscionable; statutory limits (UCTA UK)    | B2C: void if excluding statutory rights; B2B: generally enforced | Enforceable; fraud/intentional acts cannot be excluded                       | DIVERGENT                                                                                              |
| **Good faith obligation**   | Limited; context-specific (no general duty in US/UK)             | General duty (BGB §242; CC Art. 1104; PICC Art. 1.7)             | General principle (Civil Code Art. 7)                                        | **CONFLICTING** — civil law parties may claim good faith breach not recognized in common law governing |
| **Contract formation**      | Offer + acceptance + consideration                               | Offer + acceptance (no consideration)                            | Offer + acceptance (no consideration)                                        | DIVERGENT                                                                                              |
| **Parol evidence rule**     | Applies — written contract controls                              | Generally does not apply — negotiations admissible               | Does not apply                                                               | CONFLICTING                                                                                            |
| **Governing law choice**    | Respected (with public policy limits)                            | Rome I (EU): respected with mandatory override protection        | Parties may choose; restricted for certain domestic transactions             | HARMONIZED (with caveats)                                                                              |
| **Forum selection clause**  | Generally enforced (M/S Bremen standard US; Donohue UK)          | EU Brussels Ibis Reg. (2012): respected within EU                | Chinese courts may decline to enforce exclusive foreign jurisdiction clauses | DIVERGENT                                                                                              |
| **Arbitration clause**      | Enforced per New York Convention (172 states)                    | Enforced per New York Convention                                 | Enforceable; CIETAC/BAC preferred; foreign arbitral awards enforced          | HARMONIZED via NYC                                                                                     |
| **Force majeure**           | No general doctrine; requires express clause                     | Implied in many civil law codes (e.g., CC Art. 1218; BGB §313)   | PRC Civil Code Art. 590 statutory force majeure                              | DIVERGENT                                                                                              |
| **CISG applicability**      | Applies by default; common law parties often opt out             | Applies by default; many EU jurisdictions accept CISG            | China is CISG contracting state; applies to international sales              | [VERIFY opt-out status per contract]                                                                   |

**Practical recommendation**: For international commercial contracts spanning common law and
civil law jurisdictions:

1. Use **"liquidated damages"** language (not "penalty clause") with genuine pre-estimate —
   enforceable in both systems
2. Include an **express force majeure clause** with specific triggering events — do not rely
   on civil law implied doctrine
3. **Opt out of CISG** explicitly unless its no-consideration and specific performance
   defaults are desired
4. Choose **arbitration** over exclusive court jurisdiction for maximum enforcement reach
   across the New York Convention's 172 parties
5. For limitation of liability: include a **reasonableness qualifier** compatible with UCTA
   (UK) and the civil law manifest excess standard

### Step 10: Identify Divergences, Conflicts, and Harmonization Opportunities

For each matrix built in Steps 5–9, apply this classification to every dimension:

#### Classification System

| Status                | Symbol | Definition                                                                                                          | Action Required                                                                       |
| --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **HARMONIZED**        | 🟢     | Requirements are essentially identical across all selected jurisdictions (or covered by a binding treaty/framework) | Single standard suffices; document the covering framework                             |
| **DIVERGENT**         | 🟡     | Requirements differ but can be satisfied by designing to the stricter standard                                      | Apply highest-common-denominator rule; identify which jurisdiction drives the design  |
| **CONFLICTING**       | 🔴     | Requirements are directly incompatible — compliance with one jurisdiction may require non-compliance with another   | Legal risk assessment required; escalate to qualified counsel; document accepted risk |
| **JURISDICTION-ONLY** | 🔵     | Requirement exists only in subset of selected jurisdictions; absent elsewhere                                       | Jurisdiction-specific addendum or local supplement required                           |
| **UNCERTAIN**         | ⚪     | Applicable law is unclear, regulations pending, or enforcement guidance not yet issued                              | [VERIFY] tag; monitor; qualified local counsel required                               |

#### Conflict Register

For each 🔴 CONFLICTING item, document:

```
## Conflict: [Domain] — [Dimension]
**Jurisdictions in conflict**: [JX A] vs. [JX B]
**Conflict description**: [Specific incompatibility]
**Severity**: HIGH / MEDIUM / LOW (based on penalty exposure and operational impact)
**Options**:
  1. [Option with trade-offs]
  2. [Option with trade-offs]
  3. Accept risk in [JX] — document rationale
**Recommendation**: [Preferred approach]
**Local counsel required**: YES / NO
```

#### Highest Common Denominator Analysis

After identifying all DIVERGENT items, run the highest-common-denominator test:

1. List all DIVERGENT dimensions
2. For each, identify the strictest requirement across all jurisdictions
3. Confirm that designing to the strictest requirement satisfies all others (or identify
   residual gaps)
4. Build a single design that satisfies all requirements simultaneously
5. Document which jurisdiction drives each requirement

### Step 11: Generate Compliance Recommendations

Structure recommendations in three priority tiers:

#### Tier 1 — Mandatory Immediate Actions

Jurisdictions with pending regulatory deadlines or currently non-compliant status.
Format per finding:

```
**[Domain] / [Jurisdiction]**: [Specific obligation]
- **Deadline**: [Date or "immediate"]
- **Penalty exposure**: [Maximum fine or sanction]
- **Required action**: [Specific step]
- **Owner**: [Functional area responsible]
```

#### Tier 2 — High-Priority Design Decisions

Cross-cutting design choices that affect multiple jurisdictions simultaneously:

```
**Decision**: [E.g., "Choose cross-border data transfer mechanism"]
**Jurisdictions affected**: [List]
**Options**:
  A. [Approach] — covers [JX list]; does not cover [JX list]
  B. [Approach] — covers [JX list]; additional requirements [list]
**Recommended approach**: [Preferred option with rationale]
**Implementation steps**: [Numbered actions]
```

#### Tier 3 — Jurisdiction-Specific Supplements

Requirements unique to specific jurisdictions that do not require global redesign:

```
**[Jurisdiction]**: [Specific local requirement]
- **Action**: [Local addendum / local counsel engagement / local registration]
- **Risk if deferred**: [Impact description]
```

### Step 12: Quality Verification

Before delivering the matrix, run these checks silently:

#### Citation Quality Gates

| Gate           | Rule                                                                              | Fail Action                                              |
| -------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle  | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | Citations follow a consistent, recognizable format for the jurisdiction           | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal                            | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the legal domain selected; no accidental cross-domain bleed | Remove or segregate                                      |
| **Confidence** | Uncertainty explicitly stated; [VERIFY] applied to unverified claims              | Add confidence qualifier                                 |

#### Self-Interrogation for 🔴 CONFLICTING Items

For each CONFLICTING finding, apply this 3-pass review before delivering:

**Pass 1 — Conflict Integrity**: Is the conflict real, or does a harmonization framework
(treaty, adequacy decision, standard clause) resolve it? Re-check Step 4 frameworks.

**Pass 2 — Completeness**: Have all regulatory dimensions been considered? Are there
sector-specific rules that override the general conflict?

**Pass 3 — Challenge**: What is the strongest argument that the conflict can be resolved
without material risk? Under what conditions might a reasonable practitioner accept the
risk in one jurisdiction?

If a conflict is resolved or downgraded on review, update the classification and document
the rationale.

#### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law; clear statutory text; no ambiguity  | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities       | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

Apply the confidence score to each matrix cell. Aggregate to a domain-level confidence
and overall matrix confidence for the Glass Box.

---

## Domain Reference Data — Corporate Governance

For completeness, capture these governance dimensions when requested:

[JURISDICTION-SPECIFIC]

**Director duties (common law)**: Duty of loyalty; duty of care; duty to act in best
interests of the company (not shareholders directly in UK/AU; shareholders in DE USA)

**Director duties (civil law)**: Good faith; fiduciaries vis-à-vis company and creditors
(France L.225-35; Germany AktG §93; Brazil Law 6.404/76 Arts. 153-159)

**Anti-corruption**:

- **FCPA (US)**: Applies to US issuers and persons globally; books and records requirements;
  $25M/company per violation; DOJ/SEC joint enforcement
- **UK Bribery Act 2010**: Broadest jurisdiction globally; corporate offence of failing to
  prevent bribery (no mens rea required); adequate procedures defense
- **French Sapin II (Loi n° 2016-1691)**: Compliance programs mandatory for companies
  > 500 employees + €100M revenue; AFA oversight
- **Brazil ACPF (Law 12.846/2013)**: Strict corporate liability; leniency agreements;
  CADE/CGU joint enforcement

**ESG Reporting (mandatory)**:

- **EU CSRD (Dir. 2022/2464)**: Double materiality reporting; mandatory from 2025 (large listed);
  cascading to smaller companies through 2028
- **EU Taxonomy Regulation**: Classification of sustainable economic activities; disclosure
  of taxonomy-aligned revenue, capex, opex
- **UK**: TCFD-aligned mandatory climate disclosure for large companies (FCA)
- **US SEC Climate Disclosure Rules (2024)**: Final rule finalized March 2024; Scope 1/2
  mandatory; Scope 3 only for material/targets; implementation phased from 2026
  [VERIFY — subject to legal challenge as of filing date]
- **Australia**: Mandatory climate-related financial disclosures under ASIC from FY2025/2026

---

## Anti-Patterns

What NOT to do when building or using a jurisdiction comparison matrix:

1. **"GDPR-compliant" does not mean globally compliant**: GDPR compliance is a necessary
   condition for EU operations but does not satisfy China PIPL, Russia 152-FZ, India DPDP
   Act, or Saudi Arabia PDPL independently. Never present GDPR compliance as sufficient
   for global privacy operations.

2. **Assuming at-will employment is universal**: At-will employment is a US exception, not
   the global norm. EU, Japan, Brazil, China, and India all require just cause for
   termination. US multinationals routinely underestimate the cost and process of
   international headcount reductions.

3. **Treating common law contract templates as globally portable**: A US or UK contract
   template with limitation-of-liability clauses (possibly void under UCTA), penalty
   clauses (void at common law), and no force majeure (no implied doctrine at common law)
   may have material enforceability gaps in France, Germany, Brazil, or Japan.

4. **Using nominal adequacy without current verification**: Adequacy decisions change.
   Schrems I (Safe Harbor, 2015), Schrems II (Privacy Shield, 2020), and Brexit all
   invalidated existing arrangements. Always verify current adequacy status before relying
   on it; do not treat a 2-year-old analysis as current.

5. **Ignoring data localization in architecture decisions**: Designing a cloud architecture
   without checking data localization requirements for China, Russia, Vietnam, and Indonesia
   can require expensive re-architecture post-launch. Data residency decisions made early
   are far cheaper than compliance retrofits.

6. **Assuming penalty clauses work everywhere**: A liquidated damages clause with a
   punitive element is enforceable in France, Germany, and Brazil but void in England and
   potentially void in the US. Drafting a single clause without this analysis produces
   a contract with unpredictable enforcement across its jurisdiction scope.

7. **Non-compete templates without compensation checks**: Germany (50%+ salary compensation
   during restriction) and China (30%+ monthly salary compensation) require financial
   compensation during non-compete periods. A standard US non-compete template applied
   globally will be unenforceable in both jurisdictions.

8. **Forgetting CISG applies by default**: International B2B sales contracts governed by
   the law of a CISG contracting state are subject to CISG unless explicitly excluded.
   CISG has no parol evidence rule (prior negotiations admissible), no consideration
   requirement, and prefers specific performance over damages. US counsel routinely
   includes CISG opt-out language; many international contracts do not.

9. **Breach notification timelines stack, not queue**: A single data breach affecting EU,
   Brazil, Singapore, and Australia users triggers 72-hour (GDPR), 3-business-day (LGPD),
   3-calendar-day (Singapore PDPA), and 30-day assessment (Australia NDB) timelines
   simultaneously. The process must be designed to meet the shortest applicable window
   (72 hours), not a sequential cascade.

10. **Worker classification is not what the contract says**: Labeling someone an
    "independent contractor" does not make them one under FLSA economic realities test,
    UK employment tribunal analysis, EU Platform Work Directive presumption, or Brazilian
    subordination doctrine. The actual working relationship governs. Misclassification
    penalty exposure is often the most significant unreserved legal risk in international
    operations.

11. **Forum selection without arbitration is not global enforcement**: The Hague Choice of
    Court Convention (2005) covers approximately 40 signatories; the New York Convention
    (1958) covers 172 jurisdictions for arbitral awards. Exclusive court jurisdiction
    clauses in favor of English, New York, or Singapore courts are unenforceable in most
    of the world without the Hague Convention. Arbitration clauses provide far broader
    global enforcement coverage.

12. **Single-country compliance analysis for multi-country operations**: A company
    operating in 10 jurisdictions that conducts compliance analysis for only the highest-
    revenue jurisdiction leaves 9 jurisdictions in uncharted territory. Materiality
    tiering by penalty exposure and operational impact is appropriate, but outright
    omission is not.

13. **Treating regulatory frameworks as static**: Privacy laws, employment regulations,
    and consumer protection frameworks are revised annually. The matrix should be dated,
    include a review cycle, and flag the highest-velocity regulatory areas (privacy law
    is currently changing fastest in terms of new jurisdiction enactments).

14. **Assuming harmonization means identical**: Even within the EU, GDPR sets a minimum
    standard and member states add implementing legislation. Germany has the BDSG,
    France has the Loi Informatique et Libertés, and Ireland has the Data Protection
    Act 2018 — all add local provisions. "EU-compliant" means GDPR-compliant; full
    multi-member-state compliance requires reviewing national implementing legislation
    for each member state of operation.

15. **Conflating legal text with enforcement reality**: Some jurisdictions have strong
    laws with weak enforcement (e.g., certain data protection frameworks in early
    enforcement stages); others have moderate laws with aggressive enforcement (GDPR in
    Ireland and Luxembourg for Big Tech). Penalty exposure in the matrix should reflect
    both maximum fine AND enforcement track record.

---

## Writing Standards

Apply plain-language discipline to all matrix output:

**For matrix cells**:

- Name the requirement specifically: "72-hour breach notification to DPA" not "timely
  notification requirements"
- Include the citation: "GDPR Art. 33(1)" not "under applicable EU law"
- State the status clearly: HARMONIZED / DIVERGENT / CONFLICTING — not vague qualifications
- Flag uncertainty explicitly with [VERIFY]; never present uncertain positions as settled

**For conflict descriptions**:

- Name both jurisdictions and the specific incompatibility
- State the practical consequence for the organization (not just the abstract legal difference)
- Offer at least two resolution options with their trade-offs

**For recommendations**:

- Active voice: "Appoint a DPO before operating in Germany" not "A DPO appointment should
  be considered prior to commencement of operations"
- Name the action, the deadline, and the owner function
- One recommendation per finding; do not bundle unrelated items

**Quality gates before delivery**:

1. Can a non-lawyer business stakeholder understand the executive summary and act on it?
2. Is every cell in the matrix populated (even if the population is "Not applicable" or
   "[VERIFY]")?
3. Is every legal claim supported by a specific citation or flagged [VERIFY]?
4. Are all CONFLICTING findings documented in the Conflict Register with options?
5. Does the highest-common-denominator analysis produce an implementable single design?
6. Is the matrix dated with a next-review date given regulatory velocity?

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- In Step 3, search for current statutory text, recent amendments, and regulatory
  enforcement actions for each jurisdiction × domain combination
- Verify adequacy decisions, treaty membership, and harmonization framework status
- Search for enforcement cases and fine amounts to calibrate penalty exposure
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp**:

- Use the reference data embedded in this skill (Steps 5–9 and Domain Reference sections)
- Mark all statutory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend local counsel review for any jurisdiction where penalty exposure exceeds the
  organization's materiality threshold

**Recommended monitoring tools** (for ongoing matrix maintenance):

- IAPP Global Privacy Law Tracker (privacy law updates)
- ILO NATLEX database (employment law updates)
- OECD FDI Regulatory Restrictiveness Index (market access and governance)
- Norton Rose Fulbright Global Data Hub

---

## Output Format Template

```markdown
# Jurisdiction Comparison Matrix — [Legal Domain(s)]

**Organization**: [Name or "Not provided"]
**Home jurisdiction**: [Baseline jurisdiction]
**Jurisdictions analyzed**: [List — N jurisdictions]
**Legal domains covered**: [Privacy / Employment / Data Localization / Consumer Protection /
Contract Enforcement / Corporate Governance]
**Use case**: [Contract design / DD / Compliance program / etc.]
**Date of analysis**: [Date]
**Next review recommended**: [Date — typically 12 months or on regulatory trigger]
**Matrix confidence**: [HIGH / MEDIUM / LOW — rationale]

---

## Executive Summary

[3–5 bullet summary of the most material findings, conflicts, and highest-priority actions]

---

## Harmonization Overview

| Domain                    | 🟢 Harmonized | 🟡 Divergent | 🔴 Conflicting | 🔵 Jurisdiction-Only | ⚪ Uncertain |
| ------------------------- | ------------- | ------------ | -------------- | -------------------- | ------------ |
| Privacy & Data Protection | [N]           | [N]          | [N]            | [N]                  | [N]          |
| Employment Law            | [N]           | [N]          | [N]            | [N]                  | [N]          |
| Data Localization         | [N]           | [N]          | [N]            | [N]                  | [N]          |
| Consumer Protection       | [N]           | [N]          | [N]            | [N]                  | [N]          |
| Contract Enforcement      | [N]           | [N]          | [N]            | [N]                  | [N]          |
| Corporate Governance      | [N]           | [N]          | [N]            | [N]                  | [N]          |

---

## Active Harmonization Frameworks

[Frameworks from Step 4 that cover this jurisdiction set]

- **[Framework name]**: Covers [domains]; applicable to [jurisdictions]; note [limitation]
- ...

---

## Comparison Matrix — [Domain]

[Full matrix table per domain — see Step 5–9 templates]

---

## Conflict Register

[One entry per 🔴 CONFLICTING finding — see Step 10 format]

---

## Highest Common Denominator Design

[Table: Requirement → Strictest Jurisdiction → Design Standard → Satisfies All?]

| Dimension | Strictest Jurisdiction | Design Standard | Satisfies All Jurisdictions? | Residual Gaps |
| --------- | ---------------------- | --------------- | ---------------------------- | ------------- |
|           |                        |                 |                              |               |

---

## Compliance Recommendations

### Tier 1 — Mandatory Immediate Actions

[Per-finding format from Step 11]

### Tier 2 — High-Priority Design Decisions

[Per-decision format from Step 11]

### Tier 3 — Jurisdiction-Specific Supplements

[Per-jurisdiction format from Step 11]

---

## Regulatory Velocity Monitor

[High-change areas with pending developments:]

| Jurisdiction | Domain     | Development                 | Expected       | Impact                                       |
| ------------ | ---------- | --------------------------- | -------------- | -------------------------------------------- |
| India        | Privacy    | DPDP implementing rules     | Pending (2026) | Localization scope; SDF designation          |
| UK           | Employment | Employment Rights Bill      | 2026           | Day-one unfair dismissal; non-compete reform |
| EU           | AI/Privacy | AI Act + GDPR intersection  | 2025–2026      | HR AI; credit AI; conformity assessments     |
| US           | Privacy    | Federal privacy legislation | Uncertain      | Potential preemption of state laws           |
| EU           | Consumer   | Omnibus/CPC enforcement     | 2025–2026      | Cross-border consumer enforcement            |

---

## Glass Box Audit Trail

\`\`\`yaml
glass_box:
skill_name: "legalcode-jurisdiction-mapper"
domains_analyzed: "[comma-separated list]"
jurisdictions_analyzed: "[N jurisdictions: list]"
home_jurisdiction: "[baseline]"
use_case: "[selected use case]"
detail_level: "[Summary / Standard / Deep]"
legalcode_mcp: "Connected / Not connected"
research_reference_file: "/tmp/legalcode-jurisdiction-mapper-research.md or 'Not created'"
harmonization_frameworks_applied: "[list of applicable frameworks]"
matrix_dimensions_total: "[N dimensions across all domains]"
harmonized_count: "[N]"
divergent_count: "[N]"
conflicting_count: "[N]"
jurisdiction_only_count: "[N]"
uncertain_count: "[N]"
citations_verified: "[N VERIFIED] / [N UNVERIFIED [VERIFY]]"
self_interrogation_conflicts: "[N conflicts reviewed — PASS / REVISED]"
confidence: "HIGH / MEDIUM / LOW — [rationale]"
limitations: - "Matrix reflects law as of [date]; regulatory developments after this date not captured" - "[Any scope limitations]" - "VERIFY-tagged items require qualified local counsel confirmation"
reviewer: "AI-assisted — requires qualified legal review in each jurisdiction"
next_review_date: "[recommended date]"
\`\`\`
```

---

## Localization Notes

This skill is designed to operate across any jurisdiction combination. When adding a
jurisdiction not in the reference data above:

1. Research the governing law using legalcode-mcp or authoritative government sources
2. Populate all matrix dimensions with available data
3. Mark gaps with [VERIFY] and recommend local counsel engagement
4. Note the jurisdiction's legal tradition (common law / civil law / mixed / Nordic /
   religious law overlay) to apply correct default assumptions
5. Add the jurisdiction to the Glass Box `jurisdictions_analyzed` field

**When working with jurisdictions in non-English languages:**

- Use the correct local legal term alongside the English translation
- Note local terminology for key concepts (e.g., "Betriebsrat" = works council (Germany);
  "motif réel et sérieux" = genuine and serious cause (France); "FGTS" = Severance
  Indemnity Fund (Brazil))
- Do not assume English legal concepts map precisely to local equivalents

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis based on deep research
across primary legislative sources (GDPR, UK GDPR, CCPA/CPRA, LGPD, PIPL, PDPA, Japan
APPI, India DPDP Act, Australia Privacy Act, PIPEDA, PDPL, Indonesia PDP Law), employment
law frameworks (ERA 1996, KSchG, Code du travail, CLT, Labor Contract Law, Fair Work Act
2009, IR Code 2020), harmonization instruments (New York Convention, Hague Choice of
Court Convention, CISG, Rome I Regulation, EU SCCs, UK IDTAs, APEC CBPR/Global CBPR
Forum, EU GDPR adequacy decisions, UNIDROIT UPICC 2016, OECD Privacy Guidelines 2013),
and consumer/product liability frameworks (EU CRD, EU PLD 2024, ACL, CDC, CCPA/CPRA).
Recent developments through March 2026 incorporated. Quality bar: 18/18 Legalcode elements.
