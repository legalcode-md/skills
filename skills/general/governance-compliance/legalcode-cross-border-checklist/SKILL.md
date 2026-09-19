---
name: legalcode-cross-border-checklist
description: 'Generate a comprehensive cross-border transaction checklist covering all major compliance
  and legal dimensions of international deals: governing law and choice of law, dispute resolution mechanisms,
  regulatory approvals (merger control, sector-specific consents), tax structuring and withholding obligations,
  cross-border data transfers, sanctions and export controls, anti-bribery and anti-corruption, foreign
  investment review (CFIUS, NSI Act, EU FDI screening, FIRB), and currency controls. Use when advising
  on M&A transactions, joint ventures, commercial agreements, or investment structures with a cross-border
  element. Jurisdiction-agnostic framework with [JURISDICTION-SPECIFIC] markers. Also use when: a deal
  involves parties or assets in two or more countries; a contract crosses regulatory regimes; a transaction
  requires multi-jurisdiction sign-off; or a legal team needs a structured pre-close compliance roadmap
  for an international transaction.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Cross-Border Transaction Checklist

> **Disclaimer**: This skill provides a framework for AI-assisted cross-border compliance
> analysis. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in every relevant jurisdiction before use. Laws,
> regulations, sanctions designations, and tax treaties change frequently; verify current
> applicability before relying on any provision described here. Statutory and regulatory
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill generates structured cross-border transaction checklists that map every major
compliance dimension of an international deal. It is designed for legal teams, in-house
counsel, compliance officers, and deal advisors handling transactions with a cross-border
element.

**Covers:**

- Governing law and choice of law analysis (Rome I, Hague Principles, dépeçage)
- Dispute resolution framework (arbitration institutions, enforcement treaties)
- Regulatory approvals (merger control filings, sector-specific consents)
- Tax structuring (withholding taxes, PE risk, BEPS transfer pricing, Pillar Two)
- Cross-border data transfers (GDPR SCCs, DPF, national data localization laws)
- Sanctions and export controls (OFAC, EU, UK OFSI, EAR/ITAR)
- Anti-bribery and anti-corruption (FCPA, UK Bribery Act, OECD convention)
- Foreign investment review (CFIUS, UK NSI Act, EU FDI screening, FIRB, ICA)
- Currency controls (exchange control regimes, convertibility risk, repatriation)

**Does not:**

- Draft the transaction documents themselves (use drafting-specific skills)
- Provide legal advice or replace qualified multi-jurisdictional counsel
- Substitute for local counsel review in each affected jurisdiction
- Cover every possible regulatory regime — uses a risk-based scope based on deal
  parameters you provide

## Jurisdiction and Governing Law

This is a multi-jurisdiction skill. The checklist is calibrated to the specific
jurisdictions identified in your transaction. The skill uses [JURISDICTION-SPECIFIC]
markers throughout to indicate where local counsel must verify the analysis.

[JURISDICTION-SPECIFIC] For each jurisdiction involved in the transaction, research and apply:

- Choice-of-law rules and mandatory override provisions
- Foreign investment review thresholds and sector triggers
- Applicable sanctions and export control regimes
- Tax treaty network and withholding tax rates
- Data protection regime and cross-border transfer mechanisms
- Anti-bribery and corruption enforcement profile
- Currency control and exchange restrictions
- Any sector-specific regulatory approvals required

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the deal profile, the workflow pauses and asks when:

- The answer would trigger different regulatory filing obligations
- Jurisdiction selection changes the applicable legal framework materially
- Deal type or sector activates or deactivates entire checklist sections
- Risk tolerance or deal timeline affects which items are sequenced as pre-close vs. post-close

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

### Step 1: Accept the Deal Profile

Accept the transaction description in any of these formats:

- **Deal summary**: Plain-language description of the deal structure and parties
- **Term sheet or LOI**: Signed term sheet or letter of intent
- **Draft transaction documents**: Draft share purchase agreement, asset purchase agreement,
  joint venture agreement, or commercial contract
- **Jurisdiction list only**: A list of countries involved — the skill will produce a
  checklist framed around those jurisdictions

If no information is provided, prompt the user to describe the transaction.

### Step 2: Gather Deal Parameters

**⟁ CLARIFY** — Before generating the checklist, ask the user:

1. **Transaction type**: What kind of cross-border transaction is this?
   - Options: M&A (share purchase), M&A (asset purchase), Joint venture, Commercial
     agreement (supply/distribution/license), Investment (minority stake), Financing /
     loan, Real property acquisition, Other
   - _Why this matters_: Merger control, FDI review, and tax obligations depend entirely
     on the transaction type.

2. **Jurisdictions involved**: Which countries are parties, assets, or the target
   established in?
   - List all jurisdictions — country of incorporation, principal operations, and
     governing law of the agreement.
   - _Why this matters_: Every jurisdiction adds a regulatory layer. Missing a jurisdiction
     misses its filing obligations.

3. **Sector or industry**: What sector does the target/subject matter operate in?
   - Options: Technology / Defence / Critical infrastructure / Financial services /
     Telecoms / Healthcare / Energy / Media / General commercial / Other
   - _Why this matters_: Sensitive sectors trigger mandatory FDI reviews and sector-specific
     regulatory approvals that do not apply to general commercial deals.

4. **Parties involved**: Describe the buyer/counterparty profile.
   - Options: Strategic acquirer (same industry), Financial investor (PE/VC), State-owned
     enterprise (SOE) or sovereign wealth fund, Government-affiliated entity, Private
     commercial entity
   - _Why this matters_: SOE or government-linked buyers face more intensive FDI scrutiny
     in most jurisdictions. Mandatory CFIUS filings apply to SOE acquirers in TID
     sectors [VERIFY].

5. **Deal timeline**: What is the target signing and closing timeline?
   - _Why this matters_: Regulatory filing lead times (especially CFIUS: average 3-6
     months; merger control: 4-12 weeks per jurisdiction; NSI Act: up to 30 weeks)
     determine whether the timeline is realistic.

6. **Personal data involved**: Will the transaction or the agreement involve transfers
   of personal data across borders?
   - _Why this matters_: Activates or deactivates the entire data transfer section.

7. **Scope preference**: How detailed a checklist do you need?
   - Options: Full (all 9 sections, all triggers), Priority (cover the 3-5 highest-risk
     areas based on deal profile), Executive summary (top 10 issues for deal team briefing)
   - _Why this matters_: A 30-jurisdiction M&A checklist needs different scoping than a
     bilateral commercial agreement.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly at the top of the checklist output.

### Step 3: Identify the Jurisdiction Matrix

Build a jurisdiction matrix before generating the checklist:

```
Jurisdiction | Role in Deal         | Key Regimes Triggered
-------------|----------------------|------------------------------------------
[Country A]  | Buyer jurisdiction   | FDI review (CFIUS if US), tax, sanctions
[Country B]  | Target jurisdiction  | Merger control, sector licenses, currency
[Country C]  | Governing law        | Choice of law, dispute resolution
[Country D]  | Asset location       | Real property rules, local approvals
```

For each jurisdiction:

- Identify the applicable merger control regime and filing threshold
- Identify the applicable FDI review regime and sector triggers
- Identify the applicable sanctions and export control regime
- Identify the data protection regime and cross-border transfer rules
- Identify the anti-bribery enforcement profile
- Identify currency control status

**⟁ CLARIFY** — If the jurisdiction list is long (5+ countries), ask:

- "Should I prioritize analysis of the [buyer jurisdiction] and [target jurisdiction]
  as the primary regulatory exposure points, and note others with summary flags?"
- "Are there any jurisdictions where you already have local counsel engaged, so I
  can flag items for their review rather than developing them in detail here?"

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference file for the transaction:

1. For each jurisdiction in the matrix, search for:
   - Current merger control thresholds and filing requirements
   - FDI review regime: thresholds, sectors, mandatory vs. voluntary filing
   - Applicable sanctions designations and export control classifications
   - Data protection regime and cross-border transfer mechanisms
   - Anti-bribery enforcement guidance and recent cases
   - Tax treaty network and current withholding tax rates

2. Save the most relevant results to a local reference file:
   `/tmp/legalcode-cross-border-research.md`

**If legalcode-mcp is not connected:**

- Mark every statutory and threshold reference with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — verify all thresholds"`
- Proceed using general market knowledge but flag that thresholds and rates change and
  must be independently verified before acting on them

### Step 5: Generate the Nine-Section Checklist

Generate the full checklist using the Topic Analysis Reference below. For each section:

- Identify which items are **triggered** (required, conditional, or advisory) for this deal
- Classify each triggered item by severity: RED (deal-stopper / pre-sign), YELLOW
  (pre-close condition), GREEN (best-practice / post-close)
- For each RED or YELLOW item, provide the specific action required and the responsible
  party

**⟁ CLARIFY** — For items where the trigger depends on information not yet provided
(e.g., exact transaction value for merger control thresholds), ask specifically:

- "The US HSR Act filing threshold for 2025 is approximately $119.5M (adjusted annually).
  Can you confirm the deal value so I can determine whether an HSR filing is required?"
- "CFIUS mandatory filings apply when a foreign person (including SOE-affiliated buyers)
  acquires a TID US business. Is the buyer government-affiliated or SOE-controlled?"

### Step 6: Sequence the Action Plan

After generating the checklist, sequence the items into a timeline:

| Phase                      | Timing            | Key Actions                                                                                             |
| -------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------- |
| **Pre-signing**            | Before execution  | Sanctions screening; FDI pre-notification if required; identify regulatory approvals                    |
| **At signing**             | Day 0             | Representations and conditions precedent; begin merger control filings; notify data transfer mechanisms |
| **Pre-close (regulatory)** | Signing to close  | Merge control clearances; FDI approvals; sector-specific consents; data transfer documentation          |
| **Pre-close (tax)**        | Signing to close  | Structure withholding tax; arrange gross-up provisions; agree tax indemnities                           |
| **At closing**             | Close date        | Evidence of all regulatory approvals; final sanctions screen; currency registrations                    |
| **Post-close**             | Within 30-90 days | BOI/ownership disclosure filings; transfer tax filings; data transfer records; currency registration    |

**⟁ CLARIFY** — If the closing timeline provided in Step 2 is shorter than the longest
regulatory filing lead time, flag the conflict:

- "The shortest realistic timeline for [CFIUS voluntary notice / UK NSI mandatory
  notification / EU Phase II merger review] is [X weeks/months]. Your target closing
  timeline of [date] may not be achievable. Would you like me to recommend deal provisions
  to manage the timing risk (e.g., reverse break fee; long-stop date extension mechanism)?"

### Step 7: Flag Open Items and Dependencies

Identify items that cannot be resolved without additional information or local counsel:

- **Missing information**: Items where a threshold, rate, or trigger cannot be determined
  from the information provided
- **Local counsel dependencies**: Items that require in-country legal advice beyond the
  skill's scope
- **Sequential dependencies**: Items that cannot be completed until a prior item is resolved
  (e.g., data transfer mechanism cannot be documented until data flows are mapped)
- **Regulatory uncertainty**: Items where the regulatory position is unsettled or recently
  changed [VERIFY]

### Step 8: Quality Verification

Before delivering the checklist, apply the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED item, run the 3-pass Self-Interrogation. Revise if any pass reveals
   a weakness.
3. Assign Confidence Scores to each threshold-dependent item.
4. Verify that all 9 checklist sections have been addressed (or explicitly excluded with
   a reason).
5. Generate the Glass Box Audit Trail and append it to the output.

### Step 9: CLM and Compliance System Routing

If a contract lifecycle management or compliance management system is connected:

- Route the checklist items to the appropriate deal team workstreams
- Flag items requiring specialist counsel (tax, regulatory, data protection)
- Note items that should become closing conditions or representations in the deal documents

If no system is connected, skip this step.

---

## Topic Analysis Reference

### Section 1: Governing Law and Choice of Law

**Trigger**: All cross-border transactions. Always analyze.

**Key checklist items:**

| #   | Item                                                                               | Classification | Notes                                                                                                                 |
| --- | ---------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1.1 | Governing law clause identifies a specific national jurisdiction                   | REQUIRED       | Clauses selecting "international law" or non-state rules are unenforceable in most courts                             |
| 1.2 | Choice of law is valid under Rome I (EU) / applicable conflict of laws rules       | REQUIRED       | Rome I Art. 3(1): party autonomy [VERIFY for post-Brexit UK and non-EU jurisdictions]                                 |
| 1.3 | Mandatory override rules of the jurisdiction of performance have been assessed     | REQUIRED       | Art. 9 Rome I: overriding mandatory rules cannot be displaced by choice of law                                        |
| 1.4 | Dépeçage assessment: are different laws specified for different parts of the deal? | CONDITIONAL    | Permitted under Rome I Art. 3(1) and Hague Principles 2015 Art. 2(2) — ensure no internal conflicts                   |
| 1.5 | Consumer / employment mandatory protections assessed (if applicable)               | CONDITIONAL    | Rome I Arts. 6/8: choice of law cannot deprive consumers or employees of mandatory local protections                  |
| 1.6 | Choice of law for non-contractual obligations (tort, restitution) addressed        | ADVISORY       | Rome II Regulation (EC) No 864/2007 for EU parties — governing law and tort law can diverge                           |
| 1.7 | Non-state rules or UNIDROIT Principles reviewed if referenced as governing law     | CONDITIONAL    | Enforceable in arbitration (Hague Principles Art. 3) but not in most national courts; use only in arbitration clauses |

**Common issues:**

- Asymmetric choice: deal documents specify the buyer's home jurisdiction for all agreements,
  creating an enforcement disadvantage for the seller
- Ignoring mandatory rules: selecting English law for an EU-based employment contract
  does not displace the EU employee's mandatory protections under their national law
- CISG applicability: the UN Convention on Contracts for the International Sale of Goods
  applies automatically to B2B goods sales between parties in contracting states unless
  expressly excluded [VERIFY applicability]

[JURISDICTION-SPECIFIC] UK post-Brexit: Rome I is retained in UK law but EU courts no
longer follow the same rules. Cross-border deals with both UK and EU parties should
confirm governing law enforcement in both systems.

---

### Section 2: Dispute Resolution

**Trigger**: All cross-border transactions. Always analyze.

**Key checklist items:**

| #   | Item                                                                                    | Classification | Notes                                                                                                          |
| --- | --------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------- |
| 2.1 | Dispute resolution mechanism selected: arbitration or litigation                        | REQUIRED       | International arbitration is generally preferred for enforceability                                            |
| 2.2 | If arbitration: institution, rules, seat, language, and number of arbitrators specified | REQUIRED       | Incomplete clauses are "pathological" — see Anti-Patterns                                                      |
| 2.3 | Arbitral seat is a New York Convention signatory (enforcement of award)                 | REQUIRED       | New York Convention 1958: 172 contracting states as of 2025 [VERIFY current count]                             |
| 2.4 | If litigation: jurisdiction assessed for recognition and enforcement of judgments       | REQUIRED       | Hague Judgments Convention 2019 has limited ratifications [VERIFY]; foreign judgment enforcement varies widely |
| 2.5 | Multi-tiered escalation clause: negotiation → mediation → arbitration/litigation        | ADVISORY       | Best practice for commercial relationships; ensures mandatory pre-conditions do not bar enforcement            |
| 2.6 | Emergency arbitrator or interim relief mechanism addressed                              | CONDITIONAL    | Needed when injunctive relief may be required prior to constitution of the tribunal                            |
| 2.7 | Class action / collective action waiver (if governing US law)                           | CONDITIONAL    | Effective under Federal Arbitration Act for commercial contracts; not applicable in most non-US jurisdictions  |
| 2.8 | Investment protection under BIT or multilateral treaty assessed                         | CONDITIONAL    | Relevant if one party is a state or state-owned entity; ICSID Convention may apply [VERIFY]                    |
| 2.9 | Confidentiality of arbitration proceedings addressed                                    | ADVISORY       | Not automatic under all institutional rules; express provision recommended for sensitive deals                 |

**Recommended arbitration institutions by geography:**

| Region                     | Primary Institution                    | Rules Reference                     |
| -------------------------- | -------------------------------------- | ----------------------------------- |
| Global / Europe            | ICC International Court of Arbitration | ICC Rules 2021                      |
| London / UK / Commonwealth | LCIA                                   | LCIA Rules 2020                     |
| Asia-Pacific               | SIAC (Singapore) / HKIAC (Hong Kong)   | SIAC Rules 2016; HKIAC Rules 2024   |
| Americas                   | AAA-ICDR                               | ICDR Rules 2021                     |
| Investor-State             | ICSID (World Bank)                     | ICSID Convention / ICSID Rules 2022 |

[JURISDICTION-SPECIFIC] Some jurisdictions restrict or prohibit arbitration of certain
subject matters (e.g., employment claims in France; competition law damages in some
states). Verify arbitrability in each relevant jurisdiction [VERIFY].

---

### Section 3: Regulatory Approvals and Merger Control

**Trigger**: M&A transactions and joint ventures. Also triggered by commercial agreements
that create de facto control or significant influence.

**Key checklist items:**

| #   | Item                                                                      | Classification | Notes                                                                                                                      |
| --- | ------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 3.1 | Merger control filing obligations assessed for each relevant jurisdiction | REQUIRED       | Filing obligations arise where deal exceeds jurisdictional thresholds                                                      |
| 3.2 | US HSR Act filing assessed (if US nexus)                                  | CONDITIONAL    | 2025 threshold: $119.5M (size-of-person tests also apply) [VERIFY current threshold]                                       |
| 3.3 | EU Merger Regulation 139/2004 filing assessed                             | CONDITIONAL    | EU Regulation: combined worldwide turnover >€5B + EU-wide >€250M (or €100M in 3 Member States) [VERIFY]                    |
| 3.4 | UK CMA merger control filing assessed                                     | CONDITIONAL    | UK: combined share of supply >25% in UK; or UK target turnover >£70M [VERIFY]                                              |
| 3.5 | China SAMR merger filing assessed                                         | CONDITIONAL    | SAMR: combined worldwide turnover >RMB 12B + China turnover of each party >RMB 400M [VERIFY]                               |
| 3.6 | Other jurisdictions' merger control obligations assessed                  | CONDITIONAL    | Check Brazil CADE, Canada Competition Bureau, Australia ACCC, India CCI, Japan JFTC as applicable                          |
| 3.7 | Sector-specific regulatory consents identified                            | REQUIRED       | Financial services (banking licenses), telecoms, media, healthcare, energy, aviation — all may require separate approvals  |
| 3.8 | Pre-closing conditions for all regulatory approvals documented            | REQUIRED       | All clearances must be obtained before closing; long-stop date must accommodate longest lead time                          |
| 3.9 | Gun-jumping / standstill obligations reviewed                             | REQUIRED       | Implementing a notifiable deal before clearance is a serious competition law violation [VERIFY penalties per jurisdiction] |

**Merger control timing guide:**

| Jurisdiction | Initial Review         | Extended Review                   | Notes                      |
| ------------ | ---------------------- | --------------------------------- | -------------------------- |
| US (HSR)     | 30 days                | Up to 12+ months (Second Request) | [VERIFY current timelines] |
| EU           | Phase I: 25 days       | Phase II: 90 days                 | [VERIFY current timelines] |
| UK (CMA)     | Phase 1: up to 40 days | Phase 2: up to 24 weeks           | [VERIFY current timelines] |
| China (SAMR) | 30 days                | Up to 180 days                    | [VERIFY current timelines] |

[JURISDICTION-SPECIFIC] Some jurisdictions have mandatory pre-notification requirements
that must be filed before signing (e.g., Turkey, Austria under certain deal types) [VERIFY].

---

### Section 4: Tax Structuring and Obligations

**Trigger**: All cross-border transactions involving payment flows, IP licensing, or
asset transfers. Tax items are always at least ADVISORY.

**Key checklist items:**

| #    | Item                                                                              | Classification | Notes                                                                                                              |
| ---- | --------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------ |
| 4.1  | Withholding tax on dividends assessed for each jurisdiction pair                  | REQUIRED       | Treaty rates vs. domestic rates; gross-up obligation if withholding not absorbed by treaty                         |
| 4.2  | Withholding tax on interest payments assessed                                     | REQUIRED       | Key risk for intercompany loans and acquisition financing structures                                               |
| 4.3  | Withholding tax on royalties / IP payments assessed                               | REQUIRED       | Particularly material for technology licensing cross-border                                                        |
| 4.4  | Permanent establishment (PE) risk assessed for each jurisdiction                  | REQUIRED       | Service provision, seconded staff, or sales activities in a jurisdiction can create taxable presence [VERIFY]      |
| 4.5  | Transfer pricing policy documented and arm's length basis confirmed               | REQUIRED       | OECD Transfer Pricing Guidelines (2022 ed.); BEPS Action 13 Country-by-Country reporting for groups >€750M revenue |
| 4.6  | BEPS Action Plan measures assessed (Actions 2/4/6/8-10/15)                        | CONDITIONAL    | Relevant for groups with significant intercompany transactions; Pillar One/Two applicable for large MNEs           |
| 4.7  | Pillar Two global minimum tax (15%) assessed                                      | CONDITIONAL    | Applies to MNE groups with revenue >€750M; in force in 35+ jurisdictions [VERIFY current adoption]                 |
| 4.8  | Tax treaty eligibility assessed — limitation on benefits / principal purpose test | REQUIRED       | LOB clause (US model) or PPT (OECD/BEPS MLI) may deny treaty benefits; check each treaty                           |
| 4.9  | VAT/GST on cross-border supplies of services assessed                             | REQUIRED       | Supply-of-services rules differ widely; reverse charge / B2B vs. B2C rules apply differently per jurisdiction      |
| 4.10 | FATCA / CRS reporting obligations assessed                                        | CONDITIONAL    | Applies to financial accounts; relevant for financial institutions and payment flows to US persons                 |
| 4.11 | Stamp duty / transfer tax on asset or share transfer assessed                     | CONDITIONAL    | UK SDLT/SDRT, Indian stamp duty, Australian transfer duty — varies significantly by jurisdiction                   |
| 4.12 | Tax representations, warranties, and indemnities in deal documents reviewed       | REQUIRED       | Tax indemnity should cover pre-closing tax liabilities with appropriate carve-outs                                 |
| 4.13 | Tax gross-up clause assessed for cross-border payment obligations                 | REQUIRED       | Ensure that the party required to make net payments has an obligation to gross up if withholding applies           |

[JURISDICTION-SPECIFIC] Tax positions change rapidly. All rates, treaty interpretations,
and BEPS implementing measures must be verified against current law in each jurisdiction
by qualified tax counsel. The Pillar Two rules in particular are still being implemented
across jurisdictions [VERIFY current adoption status].

---

### Section 5: Cross-Border Data Transfers

**Trigger**: Transactions involving transfer of personal data from one country to another.
If no personal data is transferred, this section is NOT APPLICABLE — document the
finding explicitly.

**⟁ CLARIFY** — Before populating this section, confirm:

- "Does this transaction or the underlying commercial arrangement involve transfer of
  personal data across international borders? And from which countries to which?"
- "Is the transferring entity a data controller, data processor, or both?"

**Key checklist items:**

| #    | Item                                                                            | Classification | Notes                                                                                                                                                                    |
| ---- | ------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 5.1  | Data transfer mechanism identified for each transfer route (EU → third country) | REQUIRED       | GDPR Chapter V: adequacy decision, SCCs, BCRs, or derogations Art. 49 [VERIFY adequacy decisions in force]                                                               |
| 5.2  | EU-US Data Privacy Framework (DPF) assessed for US-bound transfers              | CONDITIONAL    | DPF adopted July 2023; replaces Privacy Shield; US recipient must be certified [VERIFY DPF status]                                                                       |
| 5.3  | UK transfer mechanism identified (UK IDTA or UK Addendum to EU SCCs)            | CONDITIONAL    | UK GDPR maintains its own transfer regime post-Brexit; EU SCCs alone insufficient for UK-originating transfers [VERIFY]                                                  |
| 5.4  | Transfer Impact Assessment (TIA) conducted where required                       | REQUIRED       | Post-Schrems II: TIA required when using SCCs to transfer to third countries; assess destination jurisdiction's surveillance laws                                        |
| 5.5  | China PIPL cross-border transfer mechanism assessed                             | CONDITIONAL    | China Personal Information Protection Law 2021: government security assessment required for operators above thresholds; SCCs available below [VERIFY current thresholds] |
| 5.6  | India DPDP Act 2023 cross-border transfer obligations assessed                  | CONDITIONAL    | India Digital Personal Data Protection Act 2023: prescribed countries approach under development [VERIFY current rules]                                                  |
| 5.7  | Brazil LGPD cross-border transfer mechanism assessed                            | CONDITIONAL    | Brazil LGPD Art. 33: adequacy, contractual clauses, or global corporate policy [VERIFY]                                                                                  |
| 5.8  | Russia data localization requirement assessed                                   | CONDITIONAL    | Russia Federal Law 152-FZ Art. 18(5): personal data of Russian citizens must be processed in Russia [VERIFY]                                                             |
| 5.9  | Data Processing Agreement (DPA) with data processor documented                  | REQUIRED       | Required under GDPR Art. 28, UK GDPR, and most major data protection regimes                                                                                             |
| 5.10 | Sub-processor chain documented and transfer mechanisms verified end-to-end      | REQUIRED       | SCCs must extend to sub-processors; standard contractual clauses alone may be insufficient without TIA                                                                   |
| 5.11 | Data transfer records maintained (Article 30 records of processing)             | REQUIRED       | Required under GDPR; best practice in all jurisdictions                                                                                                                  |

[JURISDICTION-SPECIFIC] Data localization requirements are expanding rapidly. Jurisdictions
including Indonesia (GR 71/2019), Vietnam (Cybersecurity Law 2018 Art. 26), and Saudi
Arabia (PDPL) have or are implementing localization requirements that may affect cloud
service contracts and data hosting arrangements [VERIFY current requirements].

---

### Section 6: Sanctions and Export Controls

**Trigger**: Any transaction with a cross-border element. Sanctions screening is
always required — there is no de minimis exception.

**Key checklist items:**

| #    | Item                                                                                            | Classification | Notes                                                                                                                                           |
| ---- | ----------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 6.1  | Parties screened against OFAC Specially Designated Nationals (SDN) list                         | REQUIRED       | US OFAC: strict liability — no intent required for primary sanctions violations                                                                 |
| 6.2  | Parties screened against EU Consolidated Sanctions List                                         | REQUIRED       | EU Council Regulation 269/2014 et al. — applies to EU persons and EU-territory transactions                                                     |
| 6.3  | Parties screened against UK Consolidated List (OFSI)                                            | REQUIRED       | UK sanctions operate independently of EU post-Brexit; separate screening required                                                               |
| 6.4  | Comprehensive country sanctions assessed (Iran, Cuba, North Korea, Russia/Belarus, Syria)       | REQUIRED       | OFAC comprehensive programs — even non-US entities may have exposure through US dollar clearing or US person involvement                        |
| 6.5  | Sectoral sanctions assessed (Russia/Belarus: finance, energy, defence, transportation sectors)  | REQUIRED       | OFAC: Directive 1-4 under EO 13662; EU: Reg. 833/2014 (Russia) — sectoral restrictions more complex than SDN [VERIFY current scope]             |
| 6.6  | Export control classification assessed (EAR / ITAR if US nexus)                                 | CONDITIONAL    | EAR (Commerce Dept.) covers dual-use items by ECCN; ITAR (State Dept.) covers defense articles on USML — no de minimis exception for ITAR items |
| 6.7  | Re-export and deemed export restrictions assessed                                               | CONDITIONAL    | US EAR re-export rules follow the item internationally; deemed export applies to sharing controlled technology with foreign nationals in the US |
| 6.8  | Non-US export controls assessed (EU Dual-Use Regulation 2021/821, UK Export Control Order 2008) | CONDITIONAL    | EU and UK export controls apply to EU/UK-origin goods and technology [VERIFY]                                                                   |
| 6.9  | Sanctions representations and warranties included in deal documents                             | REQUIRED       | Standard reps: no SDN affiliation; no proceeds from sanctioned activities; no circumvention                                                     |
| 6.10 | Termination right for sanctions compliance breach included                                      | REQUIRED       | Standard market practice: ability to terminate without liability if performance would violate sanctions                                         |
| 6.11 | Ongoing screening / compliance program documented                                               | ADVISORY       | OFAC compliance: frequency of rescreening and escalation path for hits                                                                          |
| 6.12 | Circumvention risk assessed (use of intermediaries to reach sanctioned parties)                 | REQUIRED       | Secondary sanctions (US) can apply even without direct US nexus — assess beneficial ownership chain                                             |

[JURISDICTION-SPECIFIC] US secondary sanctions have extraterritorial reach and can apply
to non-US entities transacting with sanctioned persons or jurisdictions. Non-US entities
should assess OFAC exposure even if no direct US nexus. EU/UK sanctions currently do not
have equivalent secondary sanction reach but are expanding [VERIFY].

---

### Section 7: Anti-Bribery and Anti-Corruption

**Trigger**: Any transaction involving business activities in or with connections to
higher-risk jurisdictions, or involving third-party intermediaries (agents, distributors,
consultants, joint venture partners).

**⟁ CLARIFY** — To calibrate this section:

- "Do any parties or counterparties operate in, or conduct business through, jurisdictions
  with elevated corruption risk scores (e.g., Transparency International CPI below 50)?"
- "Are third-party intermediaries (agents, consultants, introducers) involved in the deal
  or in ongoing commercial operations?"

**Key checklist items:**

| #    | Item                                                                                    | Classification | Notes                                                                                                                                                                              |
| ---- | --------------------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7.1  | UK Bribery Act 2010 applicability assessed                                              | REQUIRED       | Section 7: corporate offense of failure to prevent bribery — applies to any company doing business in the UK or incorporated under UK law; unlimited fine [VERIFY]                 |
| 7.2  | US FCPA applicability assessed                                                          | REQUIRED       | 15 U.S.C. §78dd-1 et seq.: applies to US issuers, US domestic concerns, and any person acting in the US — bribery of foreign officials; extra-territorial reach [VERIFY]           |
| 7.3  | France Sapin II applicability assessed                                                  | CONDITIONAL    | Loi n°2016-1691: companies with >500 employees and >€100M revenue must have compliance programme; AFA enforcement [VERIFY thresholds]                                              |
| 7.4  | Brazil Clean Company Act applicability assessed                                         | CONDITIONAL    | Law 12,846/2013: strict liability for legal entities for acts of bribery of domestic and foreign officials [VERIFY]                                                                |
| 7.5  | Germany LkSG / Strafgesetzbuch §§331-335 applicability assessed                         | CONDITIONAL    | LkSG supply chain due diligence obligations for German companies above thresholds; criminal offences under StGB apply broadly [VERIFY LkSG status — abolition proposed March 2026] |
| 7.6  | OECD Anti-Bribery Convention obligations assessed for relevant OECD member states       | ADVISORY       | 44 signatories; domestic implementing legislation varies [VERIFY]                                                                                                                  |
| 7.7  | Third-party due diligence conducted on agents, distributors, and joint venture partners | REQUIRED       | Key failure-to-prevent adequate procedure; risk-based proportionate diligence required                                                                                             |
| 7.8  | Anti-bribery representations and warranties included in deal documents                  | REQUIRED       | Standard reps: no improper payments made; no government official involvement in deal facilitation                                                                                  |
| 7.9  | Anti-bribery compliance programme assessed for adequacy as a defence                    | REQUIRED       | UK Bribery Act: "adequate procedures" defence; US FCPA: DOJ/SEC consider compliance programme in enforcement                                                                       |
| 7.10 | Government officials involved in transaction assessed                                   | CONDITIONAL    | Any involvement of a government official in facilitating the deal (even indirectly) requires enhanced scrutiny                                                                     |
| 7.11 | Gifts, hospitality, and facilitation payments policy reviewed                           | ADVISORY       | UK Bribery Act prohibits facilitation payments (unlike FCPA where small payments to routine government functionaries may be permitted [VERIFY])                                    |
| 7.12 | Successor liability assessed in M&A context                                             | REQUIRED       | Acquiring a target with FCPA / Bribery Act violations creates acquirer exposure; pre-close anti-corruption due diligence is essential                                              |

[JURISDICTION-SPECIFIC] Anti-bribery laws are enforced with increasing extraterritorial
reach. The UK Bribery Act reaches any company that "carries on a business or part of a
business in the UK" — a test that has been interpreted broadly [VERIFY current guidance].
FCPA enforcement by DOJ/SEC has expanded to non-US companies listed on US exchanges.

---

### Section 8: Foreign Investment Review

**Trigger**: M&A transactions, joint ventures, and significant commercial arrangements
where: (a) a foreign buyer acquires control of or a significant stake in a domestic
entity; OR (b) the target operates in a sensitive sector.

**⟁ CLARIFY** — Before populating this section:

- "What is the nationality of the buyer / investor?"
- "Does the target operate in any of the following: defence, critical infrastructure,
  advanced technology, telecoms, financial services, AI, semiconductor, space, energy,
  media, healthcare?"
- "What percentage of the target does the buyer intend to acquire?"

**Key checklist items:**

| #    | Item                                                                 | Classification | Notes                                                                                                                                                                                                                                                                                                      |
| ---- | -------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8.1  | CFIUS review assessed (US targets)                                   | CONDITIONAL    | FIRRMA 2018: mandatory filing required when TID US business acquired by foreign government-affiliated buyer; voluntary for others in sensitive sectors [VERIFY current thresholds and sector definitions]                                                                                                  |
| 8.2  | CFIUS mandatory filing assessment: TID US business test              | CONDITIONAL    | TID = Technology (critical/emerging tech), Infrastructure (critical), Data (sensitive personal data) — all three trigger mandatory filing for government-affiliated buyers                                                                                                                                 |
| 8.3  | UK NSI Act 2021 mandatory notification assessed                      | CONDITIONAL    | 17 mandatory sectors including advanced materials, AI, civil nuclear, comms, computing hardware, critical suppliers, cryptography, defence, energy, military/dual-use, quantum, satellite, space, transport, advanced robotics, data infrastructure, synthetic biology [VERIFY current sector definitions] |
| 8.4  | EU FDI Screening Regulation 2019/452 assessed                        | CONDITIONAL    | EU Reg. 2019/452: national screening mechanisms coordinated; EU Commission can issue opinions; Member State screening laws are the primary tool [VERIFY per Member State]                                                                                                                                  |
| 8.5  | Australia FIRB approval assessed                                     | CONDITIONAL    | Foreign Acquisitions and Takeovers Act 1975: thresholds and sensitive sector rules [VERIFY current thresholds]; national security test for sensitive acquisitions                                                                                                                                          |
| 8.6  | Canada ICA review assessed                                           | CONDITIONAL    | Investment Canada Act: net benefit test for large investments; national security review for all foreign investments [VERIFY current thresholds]                                                                                                                                                            |
| 8.7  | Germany foreign investment review (BMWi / AWG §55) assessed          | CONDITIONAL    | AWG §55: cross-sectoral review for acquisitions of 10%+ (critical infrastructure) or 25%+ (other sectors) of German companies [VERIFY current thresholds and sector lists]                                                                                                                                 |
| 8.8  | Filing timing assessed: pre-signing vs. pre-closing vs. post-closing | REQUIRED       | CFIUS can review at any time, but filing before closing provides certainty; UK NSI: mandatory notification before completion                                                                                                                                                                               |
| 8.9  | Deal documentation includes FDI review conditionality                | REQUIRED       | Condition precedent to close; reverse break fee if FDI approval not obtained; long-stop date accounts for review period                                                                                                                                                                                    |
| 8.10 | Mitigation conditions from prior deals in same sector assessed       | ADVISORY       | CFIUS and NSI Act routinely impose mitigation agreements (security agreements, divestiture conditions) — assess whether similar conditions are likely                                                                                                                                                      |

**FDI review timing guide:**

| Jurisdiction      | Review Period                                                         | Notes                                                         |
| ----------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| CFIUS (US)        | 30-day review + 45-day investigation + 15-day presidential review     | Average ~3-6 months for sensitive deals [VERIFY]              |
| UK NSI Act        | 30-business-day initial review + up to 30 more if called in           | Mandatory filing for 17 sectors; voluntary otherwise [VERIFY] |
| EU (via national) | Varies by Member State (France: ~30-75 days; Germany: up to 4 months) | [VERIFY current timelines per state]                          |
| Australia (FIRB)  | 30 days from application (extendable)                                 | [VERIFY]                                                      |
| Canada (ICA)      | 45-75 days net benefit; national security: open-ended                 | [VERIFY]                                                      |

[JURISDICTION-SPECIFIC] FDI rules are expanding rapidly. Many jurisdictions have lowered
thresholds or added sectors since 2020. Always verify current requirements with local
regulatory counsel before signing. Filing obligations are often mandatory and penalties
for non-compliance include transaction prohibition, forced divestiture, and significant
fines [VERIFY per jurisdiction].

---

### Section 9: Currency Controls and Exchange Restrictions

**Trigger**: Transactions involving payment flows to or from jurisdictions with active
exchange control regimes, or where target operations generate revenue in restricted
currencies.

**⟁ CLARIFY** — Before populating this section:

- "Are any deal payments flowing to or from jurisdictions known for currency controls?"
  (Key jurisdictions: Argentina, China, India, Brazil, Nigeria, South Africa, Egypt,
  Pakistan, Ukraine, Venezuela, Zimbabwe)
- "Does the target generate revenue in a controlled currency that must be repatriated?"

**Key checklist items:**

| #    | Item                                                                   | Classification | Notes                                                                                                                                                                                |
| ---- | ---------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 9.1  | Exchange control regimes identified for all payment flow jurisdictions | REQUIRED       | Some jurisdictions require government approval for outbound currency transfers above threshold                                                                                       |
| 9.2  | China SAFE registration / filing obligations assessed                  | CONDITIONAL    | State Administration of Foreign Exchange: cross-border capital flows require SAFE registration; equity investments in China require MOFCOM/SAFE filing [VERIFY current requirements] |
| 9.3  | Brazil Central Bank registration assessed                              | CONDITIONAL    | Overseas investments and intercompany loans from Brazil require Central Bank of Brazil registration [VERIFY current requirements]                                                    |
| 9.4  | India RBI / FEMA obligations assessed                                  | CONDITIONAL    | Foreign Exchange Management Act 1999 / RBI regulations: FDI approval and reporting requirements for inbound investment; ODI framework for outbound [VERIFY]                          |
| 9.5  | South Africa SARB exchange control assessed                            | CONDITIONAL    | South African Reserve Bank: exchange control regime for cross-border transactions [VERIFY]                                                                                           |
| 9.6  | Currency convertibility risk assessed for closing payment              | REQUIRED       | Assess whether deal consideration currency is freely convertible in all relevant jurisdictions                                                                                       |
| 9.7  | Currency inconvertibility / force majeure clause assessed              | ADVISORY       | Include provision for currency inconvertibility as a hardship / force majeure event for ongoing payment obligations                                                                  |
| 9.8  | Gross-up / price adjustment for devaluation risk assessed              | ADVISORY       | Multi-year contracts in volatile currency jurisdictions: consider USD or EUR denomination or indexed adjustment                                                                      |
| 9.9  | Repatriation of proceeds assessed                                      | REQUIRED       | After deal closing or after ongoing commercial operations, assess whether proceeds can be repatriated and at what cost                                                               |
| 9.10 | Hedging and FX risk allocation clause reviewed                         | ADVISORY       | Allocate currency risk between parties for long-term commercial agreements; consider FX rate floors/ceilings                                                                         |

[JURISDICTION-SPECIFIC] Currency controls change rapidly in response to economic
conditions. Argentina in particular has experienced multiple rule changes per year.
Always verify current rules immediately before closing any transaction with affected
currency flows. Legal opinions from local counsel are strongly recommended for high-risk
currency jurisdictions [VERIFY].

---

## Severity Classification

### RED — Deal-Stopper / Pre-Signing

A compliance issue that must be resolved before the transaction can be signed or that,
if unresolved, creates material legal risk, regulatory exposure, or deal invalidity.

**Examples:**

- Sanctioned party identified in the transaction chain
- CFIUS mandatory filing applicable but not planned
- Governing law clause selects a jurisdiction incompatible with deal enforcement needs
- Material withholding tax exposure not reflected in deal economics
- Cross-border data transfer mechanism absent for GDPR-regulated data flows

**Action**: Resolve before signing. Escalate to senior counsel and compliance. Document
the resolution and the basis for proceeding. If not resolvable, consider deal redesign
or deal abandonment.

### YELLOW — Pre-Close Condition

A compliance item that must be completed before closing but is not a bar to signing.
These items become closing conditions precedent.

**Examples:**

- Merger control filing pending
- CFIUS voluntary notice filed, awaiting clearance
- FDI notification under NSI Act made, awaiting outcome
- Tax gross-up clause not yet documented in deal terms
- Third-party anti-bribery diligence in progress

**Action**: Document as a closing condition precedent in the transaction documents. Track
progress. Build into the deal timeline. Include fallback (long-stop date; reverse break
fee if regulatory approval fails).

### GREEN — Best Practice / Post-Close

A compliance item that represents best practice or a post-closing obligation that does
not block signing or closing but must be completed within a specified period after close.

**Examples:**

- BOI / beneficial ownership filings within 30 days of closing
- Transfer tax filings within statutory period
- Data processing agreement records updated to reflect new data flows
- Anti-bribery training for newly acquired entity's staff

**Action**: Document in a post-close obligations schedule. Assign responsible party.
Set calendar reminder with compliance deadline.

### NOT APPLICABLE — Excluded from Scope

A section that does not apply to this transaction based on the deal parameters. Document
the exclusion reason explicitly. Future readers should be able to confirm the scope
without re-running the analysis.

---

## Prioritization Framework

### Tier 1 — Must-Have Before Signing

Items that are a precondition to signing or that carry criminal or regulatory enforcement
risk if missed:

- Sanctions screening completed and cleared
- FCPA / Bribery Act no-objection to third parties
- Governing law confirmed enforceable in key jurisdictions
- All RED items resolved or resolution path documented

### Tier 2 — Closing Conditions

Items that must be documented as conditions to close:

- Merger control clearances obtained (all required jurisdictions)
- FDI review clearances obtained (all mandatory filings)
- Sector-specific regulatory consents obtained
- Tax gross-up provisions documented in deal terms
- Cross-border data transfer mechanisms in place
- Key currency control approvals/registrations completed

### Tier 3 — Post-Close / Best Practice

Items that are required by law post-closing or represent best practice but do not block
the deal:

- BOI / ownership disclosure filings
- Transfer tax filings
- Anti-bribery training for acquired entity
- Ongoing compliance program integration
- Foreign exchange registrations

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any checklist output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                              | Fail Action                                                     |
| -------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Source**     | Every threshold, rate, and statutory reference cites a specific law, regulation, or treaty        | Add citation or mark "[UNVERIFIED — verify with local counsel]" |
| **Format**     | All citations follow a consistent format (statute name, jurisdiction, section/article reference)  | Fix format                                                      |
| **Currency**   | Every cited threshold or rate flagged as subject to change ([VERIFY CURRENT THRESHOLD])           | Flag as "[CHECK CURRENCY — may have changed]"                   |
| **Domain**     | Analysis stays within the identified jurisdiction matrix; no unjustified bleed from other systems | Remove or flag jurisdictional bleed                             |
| **Confidence** | Uncertainty explicitly stated; threshold-dependent items explicitly qualified                     | Add confidence qualifier                                        |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the RED classification follow logically from the
statute, regulation, or treaty cited? Is there a plausible argument that this item is
conditional rather than absolute?

**Pass 2 — Completeness**: Have all relevant regulatory dimensions been considered? Is
there a regime — sanctions, tax, FDI, export control — that could also be triggered and
has not been assessed?

**Pass 3 — Challenge**: What is the strongest argument that the transaction can proceed
without resolving this item? Under what circumstances would that argument succeed? If the
argument is strong, reclassify as YELLOW with a noted exception.

### Confidence Scoring

For each threshold-dependent or jurisdiction-specific item, assign a confidence level:

| Level        | Range     | Meaning                                                 | Action                                           |
| ------------ | --------- | ------------------------------------------------------- | ------------------------------------------------ |
| **Definite** | 0.95-1.0  | Settled regime, clear threshold, verified               | State with confidence                            |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions        | State with brief caveat                          |
| **Probable** | 0.60-0.79 | Good basis but recently changed or evolving             | State with explicit caveat and [VERIFY]          |
| **Possible** | 0.40-0.59 | Genuinely uncertain; depends on facts not yet confirmed | Flag for local counsel with both interpretations |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative, rapidly evolving               | Do not assert; mark "[UNCERTAIN]"                |

**Default for all regulatory thresholds**: Probable (0.60-0.79) — thresholds are adjusted
frequently by regulation and must always be verified before acting on them.

---

## Glass Box Audit Trail

Every cross-border checklist output MUST include a Glass Box section:

```yaml
glass_box:
  skill_name: "legalcode-cross-border-checklist"
  mode: "Created from scratch (Mode A)"
  transaction_type: "[M&A / JV / Commercial / Financing / Other]"
  jurisdictions_analyzed: "[list of jurisdictions]"
  sections_activated: "[list of the 9 sections activated]"
  sections_excluded: "[list of sections marked NOT APPLICABLE + reason]"
  red_items: "[count]"
  yellow_items: "[count]"
  green_items: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  thresholds_verified: "[count VERIFIED] / [count UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  key_assumptions:
    - "[Assumption 1 — e.g., 'Deal value assumed below HSR threshold — confirm actual consideration']"
    - "[Assumption 2 — e.g., 'Buyer assumed to be private entity, not SOE — confirm ownership structure']"
  limitations:
    - "[e.g., 'Currency control section based on general market knowledge — local counsel required']"
    - "[e.g., 'CFIUS analysis assumes TID US business test — confirm with CFIUS specialist']"
  reviewer: "AI-assisted — requires qualified legal review in each jurisdiction"
  date: "[YYYY-MM-DD]"
```

---

## Anti-Patterns

Cross-border transaction compliance anti-patterns — what NOT to do:

1. **Treating sanctions screening as a one-time check** — Sanctions lists are updated
   daily. Screen at deal inception, at signing, and immediately before closing. An entity
   clear at signing may be designated before close.

2. **Assuming OFAC only applies to US entities** — US secondary sanctions can reach non-US
   entities transacting with sanctioned persons or jurisdictions. Any transaction with a
   US dollar leg, US person involvement, or US-origin technology may trigger OFAC exposure.

3. **Filing merger control after closing** — Gun-jumping is a serious competition law
   violation. Identify all notifiable jurisdictions before signing and build the filing
   schedule into the deal timeline. Fines can reach 10% of worldwide turnover in the EU.

4. **Ignoring the NSI Act for UK-connected deals** — The UK National Security and
   Investment Act 2021 applies broadly and retroactively. Missing a mandatory filing can
   result in the transaction being void. The 17 mandatory sectors are defined broadly.

5. **Treating the EU-US Data Privacy Framework as permanent** — The DPF has been
   challenged before. Ensure US recipients are certified and maintain SCCs as a fallback.
   Do not delete TIAs or SCCs when relying on DPF.

6. **Relying on one set of SCCs for all transfers** — The EU SCCs are modular and
   different modules apply to different transfer scenarios (controller-to-controller,
   controller-to-processor, processor-to-processor). Using the wrong module is a compliance
   failure.

7. **Assuming treaty benefits apply automatically** — Tax treaties may be restricted by
   LOB clauses (US model treaties) or the OECD/BEPS PPT. Verify treaty entitlement in
   each jurisdiction before structuring payments to rely on reduced withholding rates.

8. **Mapping only direct ownership for CFIUS** — CFIUS assesses the ultimate beneficial
   ownership chain. An otherwise non-triggering deal may be a mandatory filing if a
   government-affiliated investor holds even a minority interest in the buyer's fund.

9. **Treating anti-bribery due diligence as a contract formality** — Under UK Bribery Act
   Section 7, the "adequate procedures" defence requires genuine risk-based due diligence
   on third parties. A questionnaire with no follow-up is not adequate procedures.

10. **Ignoring successor liability for pre-acquisition FCPA violations** — Acquirers
    inherit FCPA and Bribery Act liability for pre-closing violations by the target.
    Pre-close anti-corruption due diligence is essential in higher-risk jurisdictions.
    Disclose discovered violations to DOJ/SEC proactively for more favourable treatment.

11. **Assuming freely convertible currency without checking** — Currency repatriation
    restrictions can trap deal proceeds in-country for years. Assess convertibility risk
    before agreeing deal consideration in a controlled-currency jurisdiction.

12. **Setting a closing timeline without accounting for the longest regulatory approval** —
    CFIUS, UK NSI, and Phase II EU merger review can take 6-12+ months. A 90-day closing
    target is unrealistic if any of these apply. Model the timeline from the longest
    approval, not the average.

13. **Using a single governing law for all deal documents** — Complex cross-border M&A
    involves share purchase agreements, employment arrangements, IP transfers, real
    property, and data processing agreements. Each may need its own governing law selection
    to be valid and enforceable locally.

14. **Ignoring ITAR for technology-related deals** — ITAR controls on defense articles and
    services follow the item internationally regardless of subsequent transfers. There is no
    de minimis exception. An ITAR-controlled component in a product taints the entire
    product for re-export purposes [VERIFY].

15. **Conducting one jurisdiction's analysis and extrapolating to others** — FDI rules,
    merger control thresholds, data transfer mechanisms, and anti-bribery regimes differ
    materially between jurisdictions. Each jurisdiction's analysis must be conducted
    independently by counsel qualified in that jurisdiction.

16. **Treating "best efforts" representations on regulatory approvals as sufficient** —
    Condition precedent clauses for regulatory approvals should specify: (a) which
    approvals are required; (b) the standard of efforts to obtain them; (c) the long-stop
    date; and (d) what happens (reverse break fee, deal termination, or extension) if
    approvals are not obtained by the long-stop date.

17. **Skipping the post-close compliance calendar** — Many regulatory obligations (BOI
    filings, transfer tax, foreign exchange registration) have tight post-close deadlines.
    Failure to calendar these leads to statutory violations and penalties even when the
    deal itself is clean.

18. **Assuming local counsel will catch everything** — Multi-jurisdiction deals require
    active coordination between local counsel in each jurisdiction and a central deal team
    that understands the interactions between regimes. Local counsel know their jurisdiction
    but may not flag how their requirements interact with another jurisdiction's rules.

---

## Writing Standards

Apply plain-language discipline to all checklist output:

**For checklist items:**

- State the obligation in active voice: "File HSR notification within 30 days of signing"
  not "HSR notification should be filed"
- Identify the responsible party: "Buyer's US counsel to file" not "to be filed"
- Specify the deadline: "Pre-closing / within 30 days of signing / by [date]"
- Include the consequence of non-compliance when material: "[fine / transaction void /
  criminal liability] if not completed"

**For issue flags (RED/YELLOW):**

- Lead with the specific risk: "CFIUS mandatory filing required — failure to file before
  closing voids the transaction"
- Cite the authority: "[50 U.S.C. §4565 / FIRRMA 2018] [VERIFY]"
- State the action: "File CFIUS voluntary notice before signing; engage CFIUS-specialist
  counsel immediately"

**Quality gates before delivery:**

1. Can the deal team's non-lawyer members understand which items require action?
2. Is every deadline specific (a date range, not just "pre-closing")?
3. Is every threshold claim marked [VERIFY CURRENT THRESHOLD]?
4. Is the responsible party identified for each action item?
5. Are all RED items followed by a specific remediation action?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes, regulations, thresholds, and
  recent regulatory guidance
- Save the most relevant results to `/tmp/legalcode-cross-border-research.md`
- Use verified thresholds and rates throughout the checklist sections
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Search for recent regulatory developments that may affect items classified as rapidly
  evolving (BEPS Pillar Two, FDI rules, data transfer mechanisms)

**Without legalcode-mcp:**

- Mark all statutory thresholds, rates, and filing requirements with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all thresholds require verification"`
- Focus the checklist on structural identification of applicable regimes; defer threshold
  and rate specifics to local counsel verification
- Do not represent any threshold or rate as current without independent verification

---

## Localization Notes

This skill is jurisdiction-agnostic and generates checklists calibrated to the
jurisdictions identified in each transaction. For jurisdiction-specific deep dives:

- **United States**: CFIUS (FIRRMA 2018), HSR Act, OFAC, FCPA, EAR/ITAR — engage
  specialist US regulatory counsel for each regime
- **European Union**: EU Merger Regulation, EU FDI Screening Regulation, GDPR Chapter V
  transfers, EU sanctions — supplement with Member State-level analysis for each EU
  jurisdiction involved
- **United Kingdom**: UK NSI Act 2021 (17 sectors, mandatory filing), UK CMA merger control,
  UK GDPR + DPA 2018, UK OFSI sanctions, UK Bribery Act — post-Brexit rules operate
  independently of EU frameworks
- **China**: SAMR merger control, MOFCOM/SAFE FDI registration, PIPL cross-border
  transfers, China sanctions/export controls (SMEL, USCL), SAFE exchange controls
- **India**: CCI merger control, FEMA/RBI FDI framework, DPDP Act 2023 cross-border
  transfers, FCPA exposure for US-connected operations
- **Australia**: FIRB foreign investment review, ACCC merger control, Privacy Act 1988
  overseas disclosure principles, AML/CTF Act
- **Canada**: ICA net benefit and national security reviews, Competition Bureau merger
  notifications, PIPEDA/CPPA cross-border transfers

---

## Output Format Template

Structure the final checklist deliverable as:

```markdown
## Cross-Border Transaction Checklist

**Transaction**: [Deal name / description]
**Transaction Type**: [M&A / JV / Commercial / Financing]
**Jurisdictions**: [List all jurisdictions in the matrix]
**Sector**: [Target sector / industry]
**Target Closing Date**: [Date or target range]
**Date of Analysis**: [Date]
**Scope**: [Full / Priority / Executive Summary]

---

### Executive Summary

**Overall Risk Profile**: [HIGH / MEDIUM / LOW] — [1-2 sentence rationale]

**Critical Pre-Signing Items** (RED):

1. [Item] — [Action required] — [Responsible party]
2. [...]

**Closing Conditions** (YELLOW — key items):

1. [Item] — [Action required] — [Target date]
2. [...]

**Estimated Closing Timeline**:

- Fastest realistic close: [date] — assumes [conditions]
- Recommended close: [date] — accounts for [longest regulatory approval]

---

### Jurisdiction Matrix

| Jurisdiction | Role          | Key Regimes          | Filing Required   | Lead Time      |
| ------------ | ------------- | -------------------- | ----------------- | -------------- |
| [Country A]  | Buyer         | CFIUS / HSR          | Mandatory (CFIUS) | 3-6 months     |
| [Country B]  | Target        | Merger control / NSI | Mandatory (NSI)   | Up to 30 weeks |
| [Country C]  | Governing law | Dispute resolution   | N/A               | N/A            |

---

### Section 1: Governing Law and Choice of Law

[Checklist table for triggered items with classification and action]

### Section 2: Dispute Resolution

[Checklist table for triggered items with classification and action]

### Section 3: Regulatory Approvals and Merger Control

[Checklist table for triggered items with classification and action]

### Section 4: Tax Structuring and Obligations

[Checklist table for triggered items with classification and action]

### Section 5: Cross-Border Data Transfers

[Checklist table for triggered items with classification and action — or "NOT APPLICABLE: No personal data transferred across borders (confirmed by [party])"]

### Section 6: Sanctions and Export Controls

[Checklist table for triggered items with classification and action]

### Section 7: Anti-Bribery and Anti-Corruption

[Checklist table for triggered items with classification and action]

### Section 8: Foreign Investment Review

[Checklist table for triggered items with classification and action]

### Section 9: Currency Controls and Exchange Restrictions

[Checklist table for triggered items with classification and action — or "NOT APPLICABLE: All payment currencies freely convertible (confirmed)"]

---

### Sequenced Action Plan

| Phase                | Item             | Action                                      | Responsible           | Deadline                |
| -------------------- | ---------------- | ------------------------------------------- | --------------------- | ----------------------- |
| Pre-signing          | Sanctions screen | Screen all parties against OFAC/EU/UK lists | Compliance team       | Before signing          |
| At signing           | CFIUS filing     | File CFIUS voluntary notice                 | US regulatory counsel | Day 0-14                |
| Pre-close            | Merger control   | Obtain HSR / EU / other clearances          | Antitrust counsel     | 30-180 days             |
| Pre-close            | Data transfers   | Execute and file SCCs / IDTA                | Privacy counsel       | Before data flows begin |
| At closing           | Final screen     | Re-screen all parties                       | Compliance team       | Closing date            |
| Post-close (30 days) | BOI filing       | File beneficial ownership report            | Corporate counsel     | 30 days post-close      |

---

### Open Items and Dependencies

| #    | Item                    | Dependency                        | Action Required | Owner  |
| ---- | ----------------------- | --------------------------------- | --------------- | ------ |
| OI-1 | CFIUS TID analysis      | Confirm buyer ownership structure | CFIUS counsel   | [Date] |
| OI-2 | HSR threshold           | Confirm final deal value          | Deal team       | [Date] |
| OI-3 | PIPL transfer mechanism | Map data flows from China ops     | Privacy counsel | [Date] |

---

### Checklist Summary

| Section                 | Items Triggered | RED | YELLOW | GREEN | N/A |
| ----------------------- | --------------- | --- | ------ | ----- | --- |
| 1. Governing Law        | [n]             | [n] | [n]    | [n]   | [n] |
| 2. Dispute Resolution   | [n]             | [n] | [n]    | [n]   | [n] |
| 3. Regulatory Approvals | [n]             | [n] | [n]    | [n]   | [n] |
| 4. Tax                  | [n]             | [n] | [n]    | [n]   | [n] |
| 5. Data Transfers       | [n]             | [n] | [n]    | [n]   | [n] |
| 6. Sanctions            | [n]             | [n] | [n]    | [n]   | [n] |
| 7. Anti-Bribery         | [n]             | [n] | [n]    | [n]   | [n] |
| 8. Foreign Investment   | [n]             | [n] | [n]    | [n]   | [n] |
| 9. Currency Controls    | [n]             | [n] | [n]    | [n]   | [n] |
| **TOTAL**               |                 |     |        |       |     |

---

### Glass Box Audit Trail

[YAML glass_box block as defined in the Glass Box Audit Trail section above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for the Legalcode skills collection.
Research basis: 2-agent parallel research pipeline covering governing law (Rome I Regulation
593/2008; Hague Principles 2015); dispute resolution (New York Convention 1958; ICC/LCIA/SIAC/
HKIAC/AAA institutional rules; Hague Judgments Convention 2019); merger control (US HSR Act;
EC Merger Regulation 139/2004; UK CMA; China SAMR); foreign investment review (FIRRMA 2018/
50 U.S.C. §4565; UK NSI Act 2021; EU FDI Screening Regulation 2019/452; Australia FIRB;
Canada ICA); sanctions and export controls (OFAC SDN program; EU sanctions framework;
UK OFSI; EAR/ITAR); anti-bribery (UK Bribery Act 2010; FCPA 15 U.S.C. §78dd-1; OECD
Anti-Bribery Convention; France Sapin II Loi n°2016-1691; Brazil Law 12,846/2013); tax
(OECD BEPS Actions 2/4/6/8-10/15; Pillar Two GloBE rules; OECD Transfer Pricing Guidelines
2022; FATCA/CRS); cross-border data transfers (GDPR Chapter V; EU-US DPF 2023; UK IDTA;
China PIPL; India DPDP Act 2023; Brazil LGPD; Russia Federal Law 152-FZ); and currency
controls (China SAFE; Brazil Central Bank; India FEMA/RBI; key exchange control jurisdictions).
Complements: legalcode-cross-border-transfer-assessment (GDPR data transfers), legalcode-
sanctions-export-control-screening (sanctions deep dive), legalcode-anti-bribery-compliance
(anti-bribery deep dive), legalcode-contract-review (contract-level analysis).
