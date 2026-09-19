---
name: legalcode-multi-jurisdiction-privacy-comparison
description: Perform a side-by-side comparison of global privacy law requirements for specific processing
  activities or business operations across 12+ international regimes. Use when assessing multi-country
  compliance obligations, determining the highest common denominator compliance baseline, identifying
  cross-regime conflicts, building a global harmonized compliance strategy, conducting pre-market entry
  privacy due diligence, or advising on international data transfers affecting multiple jurisdictions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Perform a side-by-side comparison of global privacy law requirements for specific processing activities or business operations across 12+ international regimes. Use when assessing multi-country compliance obligations, determining the highest common denominator compliance baseline, identifying cross-regime conflicts, building a global harmonized compliance strategy, conducting pre-market entry privacy due diligence, or advising on international data transfers affecting multiple jurisdictions. Covers GDPR (EU), UK GDPR, CCPA/CPRA (California), LGPD (Brazil), PIPEDA/Bill C-27 (Canada), PIPL (China), PDPA (Singapore), POPIA (South Africa), APPI (Japan), Privacy Act (Australia), DPDP Act (India), and emerging frameworks (Thailand, Indonesia, Vietnam, New Zealand). Analyzes legal basis requirements, data subject rights, cross-border transfer mechanisms, breach notification timelines, DPO/privacy officer obligations, consent architecture, sensitive data treatment, territorial scope, enforcement penalties, and data localisation mandates. Produces compliance gap matrices, regime conflict maps, and harmonized compliance strategies that satisfy the highest common denominator across target jurisdictions. Outputs COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL gap classifications with prioritized remediation roadmaps and a Glass Box audit trail.


# Legalcode Multi-Jurisdiction Privacy Comparison

> **Disclaimer**: This skill provides a framework for AI-assisted global privacy law
> comparison. It does not constitute legal advice. All outputs must be reviewed by
> qualified privacy counsel licensed or operating in the relevant jurisdictions before
> reliance, action, or regulatory submission. Privacy laws across jurisdictions are
> amended frequently — verify current statutory text, regulations, and supervisory
> authority guidance before acting on any requirement described here. Statutory, case
> law, and regulatory references cited from training data carry hallucination risk —
> verify against authoritative primary sources before use. Mark any unverified citation
> **[VERIFY]** before delivery. This skill covers 12+ jurisdictions; no single output
> can substitute for local counsel review in each applicable regime.

---

## Purpose and Scope

This skill performs a comprehensive multi-jurisdiction global privacy law comparison.
Given a set of processing activities or business operations, it determines which
international privacy regimes apply, maps all obligations across comparison dimensions,
identifies genuine cross-regime conflicts, and produces a harmonized compliance strategy
that satisfies the highest common denominator across all target jurisdictions.

By 2026, 144 countries — covering over 79% of the global population — have enacted
comprehensive data privacy legislation. A multinational organisation may simultaneously
be subject to the GDPR in Europe, PIPL in China, CCPA/CPRA in California, LGPD in
Brazil, and a dozen more regimes. These laws share common concepts (lawful bases,
data subject rights, breach notification, accountability) but diverge critically on
scope, consent models, transfer restrictions, enforcement, and data localisation —
and some provisions actively conflict with each other.

**This skill covers:**

- Applicability threshold analysis: which of 12+ regimes apply to the organisation's
  specific processing activities
- Legal basis / lawful grounds comparison across all applicable regimes
- Data subject rights matrix: right of access, correction/rectification, erasure,
  portability, objection, restriction, opt-out of sale/profiling — with deadlines and
  exceptions per regime
- Cross-border transfer mechanism mapping: adequacy decisions, SCCs/standard contracts,
  BCRs/binding rules, consent, and derogations — per regime
- Breach notification timelines: regulator notification deadline + threshold; data
  subject notification deadline + threshold — per regime
- DPO / Privacy Officer / Information Officer requirements: mandatory triggers, role,
  registration requirements — per regime
- Consent architecture: opt-in vs. opt-out; separate consent requirements; withdrawal
  mechanisms — per regime
- Sensitive / special category data: definitions, treatment, and additional conditions
  — per regime
- Enforcement authority and maximum penalties — per regime, with recent enforcement
  benchmarks (2023–2026)
- Data localisation mandates: mandatory local storage, storage limitation rules, and
  state security review obligations — per regime
- Cross-regime conflict identification: where compliance with one law creates risk of
  non-compliance with another
- Harmonized compliance strategy: the "highest common denominator" baseline that
  satisfies all target regimes simultaneously
- Compliance gap matrix: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL classification
  per dimension per regime
- Prioritized remediation roadmap: Tier 1 (immediate) / Tier 2 (near-term) / Tier 3
  (long-term) action items with specific implementation steps
- Glass Box audit trail for full decision traceability

**This skill does not:**

- Provide legal advice or replace qualified privacy counsel review in each jurisdiction
- Conduct a full DPIA / FRIA — see `legalcode-dpia-generator` and
  `legalcode-ai-fundamental-rights-impact-assessment`
- Perform US state-level privacy law comparison — see `legalcode-us-state-privacy-comparison`
- Draft privacy policies — see `legalcode-privacy-policy-drafter`
- Draft data processing agreements — see `legalcode-data-processing-agreement-drafter`
- Assess cross-border transfer mechanisms in depth — see `legalcode-cross-border-transfer-assessment`
- Conduct data breach notification drafting — see `legalcode-breach-regulatory-notification-drafter`
- Assess individual GDPR lawful bases — see `legalcode-gdpr-legal-basis-assessment`
- Cover sector-specific laws (HIPAA, GLBA, FERPA, PCI-DSS, BIPA) alongside the
  general privacy frameworks — flag for separate specialist review

---

## Jurisdiction and Governing Law

This skill covers the following 12 core regimes plus 4 emerging frameworks. The "core"
designation reflects that the law is in force and actively enforced with meaningful
penalty exposure as of early 2026.

### Core Regimes Roster (12)

| #   | Jurisdiction               | Law / Regime                                                                                                        | Abbreviation       | Enforcement Authority                                    | Effective / Enforcement Date                                                     |
| --- | -------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 1   | European Union             | General Data Protection Regulation, Regulation (EU) 2016/679                                                        | GDPR               | DPAs per Member State (EDPB coordinates)                 | May 25, 2018                                                                     |
| 2   | United Kingdom             | UK GDPR + Data Protection Act 2018 + Data (Use and Access) Act 2025                                                 | UK GDPR            | Information Commissioner's Office (ICO)                  | Jan. 1, 2021 (post-Brexit)                                                       |
| 3   | United States (California) | California Consumer Privacy Act as amended by CPRA                                                                  | CCPA/CPRA          | California Privacy Protection Agency (CPPA); AG          | Jan. 1, 2020 (CCPA); Jan. 1, 2023 (CPRA); Jan. 1, 2026 (ADMT/cybersecurity regs) |
| 4   | Brazil                     | Lei Geral de Proteção de Dados, Law No. 13,709/2018                                                                 | LGPD               | Autoridade Nacional de Proteção de Dados (ANPD)          | Aug. 18, 2020 (general); Aug. 2021 (sanctions active)                            |
| 5   | Canada                     | Personal Information Protection and Electronic Documents Act + proposed Consumer Privacy Protection Act (Bill C-27) | PIPEDA / CPPA      | Office of the Privacy Commissioner (OPC)                 | Jan. 1, 2001 (PIPEDA); Bill C-27 not yet in force [VERIFY]                       |
| 6   | China                      | Personal Information Protection Law                                                                                 | PIPL               | Cyberspace Administration of China (CAC); MPS; SAMR      | Nov. 1, 2021                                                                     |
| 7   | Singapore                  | Personal Data Protection Act 2012 (amended 2020/2021)                                                               | PDPA               | Personal Data Protection Commission (PDPC)               | July 2, 2014; 2020 amendments effective Oct. 2021 – Feb. 2022                    |
| 8   | South Africa               | Protection of Personal Information Act 4 of 2013                                                                    | POPIA              | Information Regulator                                    | July 1, 2021 (enforcement)                                                       |
| 9   | Japan                      | Act on the Protection of Personal Information (amended April 2022)                                                  | APPI               | Personal Information Protection Commission (PPC)         | Apr. 1, 2022 (major amendment)                                                   |
| 10  | Australia                  | Privacy Act 1988 + Australian Privacy Principles + Privacy and Other Legislation Amendment Act 2024                 | Privacy Act / APPs | Office of the Australian Information Commissioner (OAIC) | Mar. 12, 1989; 2024 reforms in force Dec. 2024                                   |
| 11  | India                      | Digital Personal Data Protection Act 2023 + DPDP Rules 2025                                                         | DPDP Act           | Data Protection Board of India (DPB)                     | Nov. 13, 2025 (Phase 1); May 13, 2027 (full compliance)                          |
| 12  | New Zealand                | Privacy Act 2020                                                                                                    | NZ Privacy Act     | Office of the Privacy Commissioner (OPC-NZ)              | Dec. 1, 2020                                                                     |

### Emerging Frameworks (4 — Monitor)

| #   | Jurisdiction    | Law                                                               | Abbreviation         | Status                                                     |
| --- | --------------- | ----------------------------------------------------------------- | -------------------- | ---------------------------------------------------------- |
| E1  | Thailand        | Personal Data Protection Act B.E. 2562                            | PDPA-TH              | In force May 2022; PDPC actively enforcing                 |
| E2  | Indonesia       | Personal Data Protection Law                                      | PDP Law              | In force Oct. 2024; 2-year transition to Oct. 2026         |
| E3  | Vietnam         | Decree 13/2023/ND-CP on Personal Data Protection                  | PDPL-VN              | In force Jul. 2023; implementing circular pending [VERIFY] |
| E4  | UAE (DIFC/ADGM) | DIFC Data Protection Law 2020 (Law No. 5 of 2020); ADGM DPLR 2021 | DIFC DPL / ADGM DPLR | Free zone scope only; in force 2020/2021                   |

> **Note on scope**: This skill focuses on the 12 core regimes. Emerging frameworks
> are flagged where they affect organisations already subject to a core regime (e.g.,
> a company subject to PIPL operating in Thailand must also comply with PDPA-TH).

---

## Interactive Clarification

This skill uses **CLARIFY** prompts at key decision points. When a CLARIFY point is
reached, pause and ask the user the structured question before proceeding. If the user
has already provided the information, skip the question.

Do not assume answers that would materially change the scope (e.g., which regimes apply,
what processing activities are in scope, whether data localisation exists in a country
where the organization operates).

---

## Workflow

### Step 1: Accept Input

Accept input in any of these forms:

- **Processing activity description**: "We operate a B2B SaaS platform with customers
  in the EU, UK, Brazil, and Singapore. We process employee data from all four regions,
  customer usage data, and we use a US-based sub-processor for analytics."
- **Organisation profile**: Industry, headquarters, employee locations, customer locations,
  data flows, sub-processors used
- **Specific comparison request**: "Compare GDPR, UK GDPR, and CCPA/CPRA on data subject
  rights deadlines and breach notification timelines."
- **Target jurisdiction list**: An explicit list of regimes to compare (skip applicability
  screening and proceed to comparison matrix)
- **Business scenario**: "We are entering the Chinese and Indian markets — what additional
  obligations do PIPL and DPDP impose compared to our existing GDPR baseline?"

**If the input is insufficient**, proceed to Step 2 to gather context.

---

### Step 2: Gather Context

**CLARIFY 1 — Jurisdiction scope:**

> Which jurisdictions or regimes should this comparison cover?
>
> - **All applicable based on my operations** _(Recommended — I'll determine applicability
>   based on your organisation profile)_
> - **Specific list** — I'll tell you which ones
> - **Global overview** — Compare all 12 core regimes regardless of applicability
> - **New-jurisdiction entry** — I'm assessing a specific market I'm entering

_Why this matters_: Scoping to applicable regimes produces an actionable gap matrix;
a global overview is better for policy design or benchmarking.

---

**CLARIFY 2 — Primary use case:**

> What is the primary objective of this comparison?
>
> - **Gap analysis** — Identify where my organisation's current GDPR/CCPA compliance
>   fails to satisfy other applicable regimes
> - **Market entry due diligence** — I'm launching in a new jurisdiction and need to
>   understand incremental obligations
> - **Harmonized compliance strategy** — Build a single privacy framework that satisfies
>   all applicable regimes
> - **Conflict identification** — Identify where two regimes conflict and I need a
>   resolution approach
> - **Policy drafting support** — Compare regimes to determine the highest common
>   denominator for policy/notice/consent language

_Why this matters_: Gap analysis produces a remediation roadmap; harmonization produces
a design-phase framework; conflict identification produces resolution strategies.

---

**CLARIFY 3 — Processing activities in scope:**

> Describe the processing activities this comparison should cover:
>
> - **All processing** — Map all personal data processing across the organisation
> - **Specific categories** — Employee data only / Customer data only / Marketing data /
>   Analytics / Cross-border transfers / Specific product/service
> - **Sensitive data focus** — I process health, financial, biometric, or children's data
>   and need the sensitive-data comparison specifically
> - **Sub-processor chain** — I need to map obligations through my processor/sub-processor
>   hierarchy

_Why this matters_: Sensitive data triggers additional conditions in every regime;
employee vs. customer data has different legal basis and rights landscapes.

---

**CLARIFY 4 — GDPR baseline status:**

> Does the organisation already have GDPR compliance in place?
>
> - **Yes — full GDPR compliance** _(Recommended starting point — I'll highlight
>   incremental obligations)_
> - **Partial GDPR compliance** — Note specific gaps
> - **No GDPR baseline** — Start fresh across all regimes
> - **CCPA/CPRA baseline** — Map additional regimes against California as the baseline

_Why this matters_: Most global privacy laws are GDPR-inspired. If GDPR compliance
exists, the incremental gap is often smaller — but critical exceptions (PIPL consent
model, DPDP Consent Manager, LGPD legitimate interest scope) may still create risk.

---

### Step 3: Applicability Screening

For each of the 12 core regimes, assess whether the regime applies to the organisation
based on the processing activities and organisation profile provided.

Apply the following applicability tests per regime:

| Regime                 | Applicability Trigger                                                                                                                                                                                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GDPR**               | (a) Establishment in EEA; OR (b) Offering goods/services to EEA data subjects; OR (c) Monitoring behaviour of EEA data subjects (Art. 3). No revenue threshold.                                                                                                           |
| **UK GDPR**            | (a) Establishment in UK; OR (b) Offering goods/services to UK data subjects; OR (c) Monitoring UK data subjects. Post-Brexit replaces GDPR for UK.                                                                                                                        |
| **CCPA/CPRA**          | For-profit entity doing business in California that meets one of: (i) $25M+ annual gross revenue; (ii) buys/sells/shares/receives personal info of 100,000+ consumers/households; (iii) derives 50%+ revenue from selling/sharing consumer personal info. Effective 2023. |
| **LGPD**               | Processing personal data of individuals located in Brazil; OR data collected in Brazil; OR processing aimed at offering goods/services to individuals in Brazil. Applies regardless of processor's location.                                                              |
| **PIPEDA**             | Private-sector organisations engaged in commercial activity involving personal information about Canadian individuals. Applies interprovincially and internationally.                                                                                                     |
| **PIPL**               | (a) Personal information handling activities within the PRC; OR (b) Handling outside PRC of personal information of natural persons in China for purposes of: providing products/services, analysing/assessing behavior, or other circumstances under law (Art. 3).       |
| **PDPA (Singapore)**   | Organisations that collect, use, or disclose personal data in Singapore. Does not apply to: individuals acting in personal/domestic capacity; employees acting in employment capacity; public agencies.                                                                   |
| **POPIA**              | Public and private bodies that process personal information in South Africa; OR bodies that use automated or non-automated means where domiciled in South Africa; OR not domiciled but using means in South Africa other than purely for transit.                         |
| **APPI**               | Business operators handling personal information in Japan. 5,000-individual threshold abolished April 2017 — all businesses handling any personal information are covered.                                                                                                |
| **Privacy Act (APPs)** | APP entities: Australian Government agencies; organisations with $3M+ annual turnover; health service providers; other prescribed organisations (regardless of size).                                                                                                     |
| **DPDP Act (India)**   | (a) Processing of digital personal data within India; OR (b) Processing outside India where personal data relates to Data Principals (individuals) in India. Phase 1 live Nov. 2025; full compliance May 2027.                                                            |
| **NZ Privacy Act**     | Agencies (persons and organisations) that hold personal information in New Zealand. Extraterritorial reach for agencies with NZ link.                                                                                                                                     |

**Applicability Output**: Produce an applicability table:

```
| Regime   | Applicable? | Trigger Basis            | Confidence |
|----------|-------------|--------------------------|------------|
| GDPR     | YES         | EEA customer base         | HIGH       |
| UK GDPR  | YES         | UK customers              | HIGH       |
| PIPL     | MAYBE       | Assess if PRC users exist | MEDIUM     |
| ...      | ...         | ...                       | ...        |
```

For MAYBE determinations, ask the user before proceeding.

---

### Step 4: Generate Comparison Matrix

For all applicable regimes, populate the following 10-dimension comparison matrix.
Use the per-regime reference tables in Section 6 to populate each cell.

#### Dimension 1: Legal Basis / Lawful Grounds

| Regime           | Available Bases                                                                                                                                                         | Key Notes                                                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| GDPR             | Consent; Contract; Legal obligation; Vital interests; Public task; Legitimate interests (Art. 6(1)(a-f))                                                                | No hierarchy — most appropriate basis per activity; basis-switching prohibited                     |
| UK GDPR          | Same 6 bases as EU GDPR + Recognised Legitimate Interests (Schedule 1, DUA 2025)                                                                                        | DUA 2025 expands Recognised LI list — reduces LIA burden                                           |
| CCPA/CPRA        | No "legal basis" concept — opt-out model; businesses may collect/use unless consumer opts out of sale/sharing                                                           | CPRA adds opt-out of ADMT (sensitive data treatment applies)                                       |
| LGPD             | 10 legal bases including consent, contract, legal obligation, legitimate interest, protection of life, health, research, credit, process execution (Art. 7)             | Legitimate interest permitted but ANPD interpretation narrower than GDPR                           |
| PIPEDA           | Consent; Explicit consent for sensitive data; Limited non-consent cases (journalism, investigation, emergency)                                                          | Consent is the default; limited legitimate interest analog                                         |
| PIPL             | Consent; Contract performance; Legal obligations; Public interest; Vital interests; Disclosed data; Other per law (Art. 13) — **no legitimate interests**               | Separate consent required for sensitive data (Art. 29); separate consent for cross-border transfer |
| PDPA (Singapore) | Consent; Legitimate interests (2020 amendment, limited scope); Contractual necessity; Legal proceedings; Research; Other specified purposes                             | LI introduced in 2020 amendment but scope narrower than GDPR                                       |
| POPIA            | Consent; Contract; Obligation; Vital interests; Public interest; Legitimate interest of responsible party/third party (Condition 5, s.11)                               | Similar 6-ground framework to GDPR                                                                 |
| APPI             | Broadly purpose-based; consent for sensitive data and third-party transfer; opt-out for third-party provision of non-sensitive data                                     | No enumerated legal basis system — purpose specification + use limitation is the core mechanism    |
| Privacy Act (AU) | No explicit legal basis system — APPs permit collection that is reasonably necessary; consent applies for sensitive data                                                | APP 3 requires lawful/fair collection; sensitive data needs consent or health exception            |
| DPDP (India)     | Consent (primary); Legitimate uses (8 specified: state/public interest functions, medical emergency, epidemic, employment-related, legal proceedings, default handling) | Only consent + 8 enumerated legitimate uses — no general legitimate interest                       |
| NZ Privacy Act   | No legal basis system — purpose-based collection; reasonable necessity standard                                                                                         | IPP 1 (collection limitation); IPP 2 (source); IPP 3 (collection from subject)                     |

**[JURISDICTION-SPECIFIC]**: Research the current ANPD position on legitimate interest scope for Brazil (LGPD) before advising; ANPD guidance has evolved since 2022. Mark Brazil legitimate interest conclusions **[VERIFY]** against current ANPD guidance.

---

#### Dimension 2: Data Subject Rights Matrix

| Right                                        | GDPR                                                      | UK GDPR       | CCPA/CPRA                                 | LGPD             | PIPEDA            | PIPL                           | PDPA (SG)                   | POPIA                    | APPI                             | AU APPs                                  | DPDP                  | NZ               |
| -------------------------------------------- | --------------------------------------------------------- | ------------- | ----------------------------------------- | ---------------- | ----------------- | ------------------------------ | --------------------------- | ------------------------ | -------------------------------- | ---------------------------------------- | --------------------- | ---------------- |
| **Access**                                   | 30 days (Art. 15)                                         | 30 days       | 45 days (CPRA)                            | 15 days          | 30 days           | 15 working days (PIPL Art. 50) | 30 days (s.21)              | 30 days (s.23)           | Promptly                         | 30 days (APP 12)                         | TBD in Rules [VERIFY] | 20 days (IPP 6)  |
| **Correction/Rectification**                 | Without undue delay (Art. 16)                             | Same          | Yes (CPRA)                                | 15 days          | Yes               | Within 7 days of verification  | Yes (s.22)                  | Yes (s.24)               | Without delay                    | Yes (APP 13)                             | Yes                   | Yes              |
| **Erasure**                                  | Art. 17 — grounds-based                                   | Same          | Yes — broad                               | Yes              | No explicit right | Yes (Art. 47) — within 7 days  | Yes (s.16B, 2020 amendment) | Yes (s.24)               | Yes (limited)                    | No explicit right (2024 reform deferred) | Yes                   | Yes              |
| **Portability**                              | Art. 20                                                   | Same          | Yes (CPRA)                                | Yes (Art. 18)    | No                | Yes (Art. 45)                  | No                          | No                       | No                               | No                                       | No                    | No               |
| **Opt-out of Sale/Sharing**                  | N/A                                                       | N/A           | Yes — core CCPA right; UOOM/GPC mandatory | No direct analog | No                | No                             | No                          | No                       | No                               | No                                       | No                    | No               |
| **Objection/Opt-out**                        | Art. 21 (legitimate interests/direct marketing/profiling) | Same          | Opt-out of ADMT (CPRA regs Jan. 2026)     | Yes (Art. 18)    | Limited           | Yes (withdraw consent only)    | No                          | Yes (s.11(3))            | Opt-out of third-party provision | No                                       | Withdraw consent      | No               |
| **Restriction**                              | Art. 18                                                   | Same          | No                                        | No               | No                | No                             | No                          | No                       | No                               | No                                       | No                    | No               |
| **Not subject to automated decision-making** | Art. 22                                                   | Same          | CPRA ADMT regs                            | Limited          | No                | No (human review requested)    | No                          | No                       | No                               | No                                       | No                    | No               |
| **Complaint / Appeal**                       | SA complaint (Art. 77)                                    | ICO complaint | CPPA appeal process                       | ANPD complaint   | OPC complaint     | CAC; courts                    | PDPC complaint              | Info Regulator complaint | PPC complaint                    | OAIC complaint                           | DPB complaint         | OPC-NZ complaint |

**Deadline comparison note**: PIPL's 15-working-day deadline for access requests is more
demanding than GDPR's 30-calendar-day standard in practice during high-volume periods.
CCPA/CPRA's 45-day response window (extendable by additional 45 days with notice) is the
most permissive of the major regimes.

---

#### Dimension 3: Cross-Border Transfer Mechanisms

| Regime           | Mechanism 1                                                                                                                          | Mechanism 2                                                                    | Mechanism 3                                   | Mechanism 4                                                                              | Special Notes                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| GDPR             | Adequacy decision (Art. 45)                                                                                                          | SCCs (Art. 46(2)(c))                                                           | BCRs (Art. 46(2)(b))                          | Art. 49 derogations (consent, contract, vital interest, public interest, legal claims)   | DPF (EU-US, July 2023); UK adequacy (ongoing)                                                                            |
| UK GDPR          | UK adequacy regulations                                                                                                              | IDTA (March 2022) or Addendum to EU SCCs                                       | UK BCRs                                       | Derogations (similar to Art. 49)                                                         | DPA 2018; DUA 2025 updates transfer regime; ICO international transfer guidance                                          |
| CCPA/CPRA        | No cross-border transfer restrictions — "sale/sharing" is the key concept                                                            | Service provider restrictions apply                                            |                                               |                                                                                          | Focus is on contractual limits on service provider use, not geographic transfer                                          |
| LGPD             | Adequacy recognition by ANPD                                                                                                         | Standard clauses (SCCs-BR, ANPD Resolution 19/2024 — mandatory from Aug. 2025) | BCRs/global corporate policies                | Consent; contractual necessity; legal obligation                                         | ANPD adequacy list in development [VERIFY]; EU SCCs not directly equivalent                                              |
| PIPEDA           | No adequacy framework — accountability-based transfers                                                                               | Contractual protections required (PIPEDA Principle 4.1.3)                      | No BCR concept                                | No formal derogations list                                                               | Proposed CPPA would add transfer impact assessment requirement                                                           |
| PIPL             | CAC Security Assessment (≥1M individuals' PI, or sensitive PI of ≥10K individuals)                                                   | Standard Contract (PI <1M, sensitive <10K) + CAC filing within 10 working days | Personal Information Protection Certification | Free-trade zone (FTZ) exemptions per Regulations on Cross-Border Data Flows (March 2024) | No adequacy decisions issued yet; GDPR compliance ≠ PIPL compliance; "separate consent" required regardless of mechanism |
| PDPA (Singapore) | PDPC approved whitelist countries                                                                                                    | Contractual arrangements (Schedule 10, PDPC Standard)                          | BCR equivalent (Data Protection Policy)       | Consent for transfers outside whitelist                                                  | 2024 whitelist includes EU, UK, AU, JP, NZ, CA, US (sector-specific) [VERIFY]                                            |
| POPIA            | Recipient country provides adequate protection per Information Regulator; OR consent; OR contractual necessity; OR legal proceedings | No formal SCCs framework yet (Information Regulator developing)                |                                               |                                                                                          | [JURISDICTION-SPECIFIC] — verify Information Regulator transfer guidance                                                 |
| APPI             | Equivalent protection standard (overseas recipient)                                                                                  | Opt-in consent for transfers to non-equivalent countries                       | PPC-approved framework (similar to BCRs)      | Exceptions: public interest, legal proceedings, vital interests                          | Japan granted GDPR adequacy 2019 (mutual); US not adequate                                                               |
| Privacy Act (AU) | Contractual protections (APP 8.1)                                                                                                    | OAIC-approved binding scheme                                                   | Consent (APP 8.2(a))                          | Australian law applies to acts/practices of recipient                                    | No adequacy decision model — accountability-based                                                                        |
| DPDP (India)     | Government-approved blacklist model: permitted to all countries except those on negative list                                        | No positive adequacy list system                                               | Consent                                       | Government may restrict by notification                                                  | Blacklist not yet published as of early 2026 [VERIFY]                                                                    |
| NZ Privacy Act   | Comparable protection standard                                                                                                       | Model contract clauses                                                         | Consent                                       | Public interest exception                                                                | Similar to Australian accountability model                                                                               |

**[JURISDICTION-SPECIFIC]**: The PIPL–GDPR conflict is structurally significant. PIPL requires
"separate consent" for cross-border transfers (Art. 39) regardless of which PIPL mechanism
is used. This conflicts with GDPR Article 7 requirements for freely given consent — where
a GDPR controller uses SCCs as the transfer mechanism (not consent), obtaining PIPL separate
consent in addition may be required, which may not satisfy GDPR's freely-given standard for
the consent element. Obtain specialist advice before operating in both regimes simultaneously.

---

#### Dimension 4: Breach Notification Timelines

| Regime           | Regulator Notification — Deadline                                                                | Regulator Notification — Threshold               | Data Subject Notification — Deadline                        | Data Subject Notification — Threshold                      | Notable Features                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| GDPR             | 72 hours (Art. 33)                                                                               | Likely to result in risk to rights/freedoms      | Without undue delay (Art. 34)                               | High risk to rights/freedoms                               | EDPB Guidelines 9/2022 on notification; no-risk exemption available                                       |
| UK GDPR          | 72 hours (UK GDPR Art. 33)                                                                       | Same risk threshold                              | Without undue delay (Art. 34)                               | High risk                                                  | ICO self-assessment tool; no-risk exemption                                                               |
| CCPA/CPRA        | Expedient notification to AG (not formal SA)                                                     | "Expedient" — no fixed timeline                  | Most expedient time possible and without unreasonable delay | Any breach of unencrypted/unredacted PI categories defined | 500+ consumer breaches → notify AG; regulates content                                                     |
| LGPD             | 72 hours to ANPD (Resolution 15/2024)                                                            | Risk or relevant damage                          | "Reasonable period" to data subjects (ANPD determines)      | Relevant damage likely                                     | ANPD Res. 15/2024 effective Apr. 2024; report form mandated                                               |
| PIPEDA           | Promptly — "as soon as feasible"                                                                 | Real risk of significant harm                    | Promptly — "as soon as feasible"                            | Real risk of significant harm                              | RROSH assessment required; report to OPC; recordkeeping obligation                                        |
| PIPL             | Immediately (PIPL Art. 57 — no fixed hour window)                                                | Any breach / leakage / falsification / loss      | Immediately                                                 | Same                                                       | CAC/MPS may require additional reporting; no specific hour count                                          |
| PDPA (Singapore) | 3 calendar days (s.26D, 2021 amendment)                                                          | Significant harm or large scale                  | 3 calendar days                                             | Same significant harm threshold                            | Mandatory notification for >500 affected individuals OR sensitive data OR financial data                  |
| POPIA            | As soon as reasonably possible (s.22)                                                            | Reasonable belief of unauthorized access         | As soon as reasonably possible                              | Same                                                       | Information Regulator expects 72-hour-equivalent urgency per published guidance; criminal penalties apply |
| APPI             | "Promptly" — PPC guidance: within approximately 30 days; 60 days for third-party provision cases | Likely to violate rights/interests               | Promptly                                                    | Same                                                       | PPC's 2021 Rules specify notification form and content; pseudonymous data exempt                          |
| Privacy Act (AU) | 30 days to OAIC (NDB scheme, s.26WK)                                                             | Likely to result in serious harm                 | Promptly when practicable                                   | Same serious harm                                          | 2024 reform proposed 72-hour timeline — check reform status [VERIFY]; new civil penalties AUD 50M         |
| DPDP (India)     | 72 hours — initial report to DPB (DPDP Rules 2025, Rule 8)                                       | Any breach                                       | Promptly to affected Data Principals                        | Same                                                       | Detailed follow-up report to DPB within 72 hours; no threshold exemption                                  |
| NZ Privacy Act   | As soon as practicable (s.113)                                                                   | Notifiable privacy breach = risk of serious harm | As soon as practicable                                      | Same                                                       | OPC-NZ guidance published 2021                                                                            |

**Harmonized minimum approach**: A 72-hour-or-better breach notification process to
supervisory authorities + immediate notification to affected individuals upon high/significant
risk satisfies the most demanding overlap of GDPR + LGPD + DPDP. PIPL's "immediately"
requirement is the most demanding; apply as the default for all regimes unless a longer
window expressly applies.

---

#### Dimension 5: DPO / Privacy Officer Requirements

| Regime           | Mandatory?                     | Trigger                                                                                                                  | Role Title                                            | Registration Required?                                              | Notes                                                                               |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| GDPR             | Yes — where applicable         | (i) Public authority; (ii) Large-scale systematic monitoring; (iii) Large-scale special category/criminal data (Art. 37) | Data Protection Officer (DPO)                         | Notify lead DPA; contact details public                             | EDPB Guidelines 243 on DPOs                                                         |
| UK GDPR          | Yes — same triggers as EU GDPR | Same                                                                                                                     | Data Protection Officer (DPO)                         | Notify ICO                                                          | Same criteria; separate UK DPO required if separate UK establishment                |
| CCPA/CPRA        | No mandatory DPO               | —                                                                                                                        | —                                                     | —                                                                   | CPPA recommends privacy officer-equivalent role; no formal requirement              |
| LGPD             | Yes — all controllers          | All personal data controllers (SME exemption pending ANPD regulation)                                                    | Encarregado (Data Protection Officer)                 | No registration — but identity/contact must be published on website | ANPD Resolution 2/2022 provides SME guidance [VERIFY current exemption status]      |
| PIPEDA           | No mandatory DPO               | —                                                                                                                        | Accountable individual designated                     | No                                                                  | PIPEDA Principle 1 requires designated individual for accountability                |
| PIPL             | Yes — above threshold          | >1M individuals' personal information processed (Art. 52)                                                                | Personal Information Protection Officer               | No registration per se, but security review may require disclosure  | Also required for critical information infrastructure operators (CIIOs)             |
| PDPA (Singapore) | No mandatory DPO               | —                                                                                                                        | —                                                     | —                                                                   | PDPC guidance recommends DPO designation; can register voluntary DPO with PDPC      |
| POPIA            | Yes — all organisations        | All public and private bodies                                                                                            | Information Officer (and Deputy Information Officers) | Must register with Information Regulator                            | Information Officer = most senior executive by default; can delegate                |
| APPI             | No mandatory DPO               | —                                                                                                                        | —                                                     | —                                                                   | Security management measures required; no mandatory privacy officer title           |
| Privacy Act (AU) | No mandatory DPO               | —                                                                                                                        | —                                                     | —                                                                   | Privacy Officer role recommended in OPC guidance; mandatory for government agencies |
| DPDP (India)     | No mandatory DPO               | —                                                                                                                        | Grievance Officer (mandatory)                         | Grievance Officer contact on website                                | Consent Manager (separate role/entity) required for certain services from Nov. 2026 |
| NZ Privacy Act   | No mandatory DPO               | —                                                                                                                        | Privacy Officer (recommended)                         | No                                                                  | s.23 allows delegation; Privacy Commissioner guidance                               |

**[JURISDICTION-SPECIFIC]**: Brazil's LGPD Encarregado obligation currently applies to all
controllers. The ANPD has published guidance on SME proportionality but has not formally
exempted small businesses. Verify current ANPD regulatory position before advising Brazilian
clients on DPO exemptions. Mark **[VERIFY]**.

---

#### Dimension 6: Consent Architecture

| Regime           | Consent Model                                                                                                                           | Standard for Consent                                                         | Sensitive Data Consent                                         | Withdrawal                                                            | Children                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| GDPR             | Opt-in required                                                                                                                         | Freely given, specific, informed, unambiguous (FSIU) affirmative action      | Explicit consent (Art. 9(2)(a))                                | Any time, no detriment, withdrawal as easy as giving                  | 13-16 per Member State (Art. 8); consent by holder of parental responsibility below age    |
| UK GDPR          | Opt-in required                                                                                                                         | Same FSIU standard                                                           | Explicit consent (UK GDPR Art. 9)                              | Same                                                                  | Age 13 (DPA 2018 s.9)                                                                      |
| CCPA/CPRA        | Opt-out for sale/sharing                                                                                                                | Opt-in for sensitive data (CPRA)                                             | Opt-in for sensitive data sharing                              | Right to opt back in                                                  | <16: opt-in; <13: parental opt-in                                                          |
| LGPD             | Opt-in required                                                                                                                         | "Free, informed, and unequivocal expression of will"                         | Explicit consent for sensitive data (Art. 11(a))               | "At any time upon express request"                                    | Parental/guardian consent for children (ANPD Res. 5/2024)                                  |
| PIPEDA           | Opt-in default; implied consent for less sensitive                                                                                      | "Meaningful consent" — informed, voluntary, given for purpose                | Express consent for sensitive data                             | Withdrawal with reasonable notice                                     | PIPEDA's sensitivity spectrum                                                              |
| PIPL             | Opt-in required; **separate consent** for: cross-border transfer, sensitive data, providing to third parties, automated decision-making | Voluntary, informed, specific, unambiguous                                   | Separate consent for sensitive PI (Art. 29)                    | Withdrawal — controller must stop processing within reasonable time   | 14 years for parent consent (Art. 31); minor <14 is separate consent class                 |
| PDPA (Singapore) | Opt-in; deemed consent with notification (2020 amendment)                                                                               | Voluntary, informed, for specific purpose                                    | Opt-in for disclosure of sensitive data categories             | Withdrawal reasonable notice — must stop processing unless legitimate | 18 for personal consent                                                                    |
| POPIA            | Opt-in (s.11(1)(a))                                                                                                                     | Voluntary, specific, informed, unambiguous                                   | Specific consent for special personal information (s.26(1)(a)) | Objection right — processing must stop unless compelling grounds      | <18 children's personal information — parental consent                                     |
| APPI             | Opt-out for standard third-party provision; opt-in for cross-border transfer; opt-in for sensitive data                                 | No FSIU standard — purpose specification + notification                      | Opt-in for special care-required information                   | Withdrawal of third-party opt-out — stop at next provision            | Third parties handling information of minors — [JURISDICTION-SPECIFIC]                     |
| Privacy Act (AU) | Opt-in for sensitive info collection                                                                                                    | APP 3 — reasonably necessary; sensitive = consent                            | Consent for sensitive information (APP 3.3)                    | No explicit withdrawal standard — complaints-based                    | No specific children's law under APPs; general care standard                               |
| DPDP (India)     | Opt-in (consent is the primary basis)                                                                                                   | Specific, informed, unconditional, unambiguous with clear affirmative action | Consent applies (no separate sensitive-data category concept)  | Any time — withdrawal mechanism must be as easy as giving consent     | <18 (or <Digital Nativity age per Rules): parental consent required; no tracking/profiling |
| NZ Privacy Act   | Opt-in for sensitive data; purpose-based otherwise                                                                                      | Reasonably obtained for the purpose                                          | Sensitive personal information — heightened care               | No formal withdrawal mechanism                                        | No specific children's threshold                                                           |

**[JURISDICTION-SPECIFIC]**: PIPL's "separate consent" requirement (Art. 30 for sensitive PI;
Art. 39 for cross-border transfer) is architecturally distinct — it cannot be bundled with
general consent. A single consent form cannot cover both general processing and cross-border
transfer under PIPL. This structural requirement must be reflected in consent management
platforms (CMPs) used across EU + China simultaneously.

---

#### Dimension 7: Sensitive / Special Category Data

| Regime           | Sensitive Data Categories                                                                                                                                                                                                                              | Additional Conditions                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| GDPR             | Race/ethnicity, political opinions, religious/philosophical beliefs, trade union membership, genetic data, biometric data for ID purposes, health, sex life/orientation, criminal convictions (Art. 9, Art. 10)                                        | Art. 9(2) conditions (10 bases); explicit consent or specific exception                                        |
| UK GDPR          | Same + DPA 2018 Schedule 1 conditions                                                                                                                                                                                                                  | DPA 2018 Sch. 1 adds employment, research, and other specific UK conditions                                    |
| CCPA/CPRA        | Social Security/government IDs, financial account data, precise geolocation, racial/ethnic origin, religious/philosophical beliefs, union membership, mail/email/text content, genetic/biometric data for ID, health/sex life data, citizenship status | Opt-in required for sharing sensitive data (CPRA); CPPA regulations govern ADMT                                |
| LGPD             | Race/ethnicity, religious beliefs, political opinions, trade union membership, health/sexual life data, genetic/biometric data, children/adolescents' data                                                                                             | Explicit consent or Art. 11 conditions; ANPD has enforcement focus                                             |
| PIPEDA           | No explicit list — sensitivity-spectrum approach                                                                                                                                                                                                       | More sensitive = higher standard; express consent required for most sensitive                                  |
| PIPL             | Race/ethnicity, religious beliefs, biometric information, medical/health data, financial accounts, location tracking, personal information of minors under 14 (Art. 28)                                                                                | Separate consent; specific purpose; minimum necessity principle; security impact assessment                    |
| PDPA (Singapore) | No explicit separate "sensitive" category — PDPA 2020 amendment broadens notion                                                                                                                                                                        | Higher care expected for NRIC data, health, financial data per PDPC advisories                                 |
| POPIA            | Race/ethnicity, trade union membership, political persuasion, health/sex life, criminal behaviour, biometric data, children's data (s.26)                                                                                                              | Prohibition on processing special PI without specific condition (s.26 conditions)                              |
| APPI             | Special care-required information: race, belief/creed, social status, medical history, criminal records, victimization history, disability (Art. 2(3))                                                                                                 | Opt-in consent; prohibition on obtaining without consent except listed exceptions                              |
| Privacy Act (AU) | Health, genetics, biometric, sexual orientation/practices, criminal record, political/religious/philosophical opinions, trade union membership, racial/ethnic origin (APP 6)                                                                           | Express consent required (APP 3.3(a)); sensitive info — limited use/disclosure                                 |
| DPDP (India)     | No separate "sensitive" category in DPDP Act 2023 (a significant departure from GDPR)                                                                                                                                                                  | Government may prescribe sensitive data categories by notification (s.16) [VERIFY for any notification issued] |
| NZ Privacy Act   | No formal "sensitive" category — IPP 2 principle of collection limitation                                                                                                                                                                              | Health information subject to stricter regime under Health Information Privacy Code                            |

---

#### Dimension 8: Enforcement — Authority, Penalties, Notable Actions

| Regime           | Enforcement Authority                           | Maximum Penalty                                                                                                               | Notable Enforcement (2023–2026)                                                                                                                              |
| ---------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GDPR             | 27 National DPAs + EDPB                         | Art. 83(5): €20M or 4% global annual turnover (higher of); Art. 83(4): €10M or 2%                                             | Meta €1.2B (Irish DPC, May 2023 — record GDPR fine); LinkedIn €310M (Irish DPC, Oct. 2024 — legal basis); Meta €479M (AEPD Spain, 2025)                      |
| UK GDPR          | ICO                                             | £17.5M or 4% global annual turnover                                                                                           | TikTok £12.7M (children's data, Apr. 2023); Equifax £11.1M; NHS Trusts enforcement 2024                                                                      |
| CCPA/CPRA        | California Privacy Protection Agency (CPPA); AG | $7,500 per intentional violation; $2,500 unintentional; civil penalties + private right of action $100–$750/consumer/incident | Sephora $1.2M (AG, Aug. 2022 — sale opt-out); DoorDash $375K (AG, Feb. 2024); Disney $45.6M (class action, 2024); CPPA issued investigative sweeps 2024–2025 |
| LGPD             | ANPD                                            | 2% of Brazil annual revenue, capped R$50M (~€9M) per infraction                                                               | Telekommunikationssystem GmbH (telecom) — first substantive enforcement 2023; Serasa Experian [VERIFY status]                                                |
| PIPEDA           | OPC                                             | No fines under PIPEDA (recommendations only); proposed CPPA would add CAD 25M or 5% global revenue fines                      | Facebook Canada CAD 9M (proposed settlement 2023); Tim Hortons (location tracking) OPC finding 2023                                                          |
| PIPL             | CAC; MPS; SAMR                                  | RMB 50M (~€6.5M) or 5% of annual revenue; serious violations: business suspension, permit revocation                          | Didi Global (RMB 8.026B, ~USD 1.2B, July 2022 — data security + PIPL); Zhihu (2023 CAC action)                                                               |
| PDPA (Singapore) | PDPC                                            | SGD 1M or 10% of annual Singapore turnover (2020 amendment)                                                                   | SingHealth SGD 1M (2019, pre-amendment benchmark); Marina Bay Sands SGD 1M (2024 — 665K customers) [VERIFY]                                                  |
| POPIA            | Information Regulator                           | ZAR 10M (~€490K) or criminal imprisonment up to 10 years (s.107)                                                              | Enforcement notices issued 2023–2024; administrative fines not yet reached maximum cap; Transunion and Experian enforcement investigations ongoing [VERIFY]  |
| APPI             | PPC                                             | JPY 100M per corporation (2022 amendment); JPY 1M for individuals                                                             | NTT Marketing Act (PPC 2023); LINE Yahoo (2024 cross-border transfer case) — largest APPI enforcement                                                        |
| Privacy Act (AU) | OAIC                                            | AUD 50M or 30% of adjusted Australian turnover per serious/repeated interference (2022 Privacy Act reform)                    | HealthEngine AUD 2.9M (2022); Medibank — ongoing OAIC investigation; optus/Latitude breaches 2023                                                            |
| DPDP (India)     | Data Protection Board (DPB)                     | Up to ₹250 crore (~USD 30M) per incident; ₹500 crore for breach notification violations                                       | DPB not yet constituted as of early 2026 — enforcement beginning Phase 1 Nov. 2025                                                                           |
| NZ Privacy Act   | OPC-NZ                                          | NZD 10,000 for individuals; organisations — no cap but court-ordered compensation; civil penalties                            | Latitude Financial NZ 2023; Waka Kotahi investigation 2024                                                                                                   |

---

#### Dimension 9: Territorial Scope and Applicability Thresholds

| Regime           | Controller Scope                                                                        | Processor Scope                                                                   | Threshold                                   | Extraterritorial Reach                    |
| ---------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------- | ----------------------------------------- |
| GDPR             | Controllers established in EEA; non-EEA controllers targeting EEA data subjects         | Processors contractually bound (Art. 28); no separate extraterritorial trigger    | No revenue threshold                        | Yes — Art. 3(2)                           |
| UK GDPR          | Same + UK establishment criterion                                                       | Same                                                                              | No threshold                                | Yes                                       |
| CCPA/CPRA        | For-profit doing business in CA                                                         | Service providers bound contractually                                             | Revenue/volume/revenue-from-sale thresholds | Yes — CA nexus                            |
| LGPD             | Any data handling of individuals in Brazil                                              | No explicit processor extraterritorial trigger                                    | No threshold                                | Yes                                       |
| PIPEDA           | Commercial activity in Canada                                                           | No direct processor obligations (accountability-based)                            | No threshold                                | Yes — Canadian connection                 |
| PIPL             | Handling PI within PRC; handling outside PRC where targeting PRC persons                | PI handlers — both controllers and processors covered                             | No threshold                                | Yes — Art. 3(2)                           |
| PDPA (Singapore) | Organisations collecting/using/disclosing data in Singapore                             | No separate processor chapter                                                     | No threshold                                | Limited — organization must have SG nexus |
| POPIA            | Responsible parties (controllers) in SA or using means in SA                            | Operators (processors) bound by contract                                          | No threshold                                | Limited to SA means                       |
| APPI             | Business operators in Japan                                                             | Trustees (processors) bound by contract                                           | No threshold                                | Limited — establishment-based primarily   |
| Privacy Act (AU) | APP entities with AU connection                                                         | No separate processor chapter                                                     | $3M turnover; health providers exempt       | Limited — AUS operation link              |
| DPDP (India)     | Data Fiduciaries (controllers) in India or processing data of India-located individuals | Data Processors contractually bound; no direct extraterritorial processor trigger | No threshold                                | Yes — Art. 3                              |
| NZ Privacy Act   | Agencies in NZ                                                                          | No separate processor chapter                                                     | No threshold                                | NZ link required                          |

---

#### Dimension 10: Data Localisation Requirements

| Regime           | Data Localisation?                                                                                           | Scope                                                                           | Mechanism                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------- |
| GDPR             | No mandatory localisation                                                                                    | —                                                                               | Transfer restrictions, not storage mandates             |
| UK GDPR          | No mandatory localisation                                                                                    | —                                                                               | Same as GDPR                                            |
| CCPA/CPRA        | No mandatory localisation                                                                                    | —                                                                               | No geographic storage restriction                       |
| LGPD             | No mandatory localisation                                                                                    | —                                                                               | Transfer restrictions via adequacy or SCCs-BR           |
| PIPEDA           | No mandatory localisation                                                                                    | —                                                                               | Accountability-based                                    |
| PIPL             | Yes — for Critical Information Infrastructure Operators (CIIOs) and important data (DSL Art. 31/CSL Art. 37) | PI of large scale/sensitive nature must be stored in China before export review | CAC security assessment for export; tiered thresholds   |
| PDPA (Singapore) | No mandatory localisation                                                                                    | —                                                                               | Transfer restrictions via whitelist/contract            |
| POPIA            | No mandatory localisation                                                                                    | —                                                                               | Transfer restrictions via adequate protection           |
| APPI             | No mandatory localisation                                                                                    | —                                                                               | Transfer restrictions via consent/equivalent protection |
| Privacy Act (AU) | No mandatory localisation                                                                                    | —                                                                               | Accountability-based APP 8                              |
| DPDP (India)     | Government blacklist model — transfers permitted except to designated restricted countries                   | Blacklist not yet published (early 2026) [VERIFY]                               | Government notification                                 |
| NZ Privacy Act   | No mandatory localisation                                                                                    | —                                                                               | Comparable protection standard                          |

**[JURISDICTION-SPECIFIC]**: PIPL data localisation for CIIOs is the most restrictive global
requirement among the 12 core regimes. If the organisation operates CIIO-classified systems
in China, technical infrastructure must be redesigned — not merely contractually addressed.
Obtain PRC specialist counsel to determine CIIO classification status.

---

### Step 5: Conflict Identification

After populating the comparison matrix, identify genuine cross-regime conflicts — situations
where complying fully with one regime creates risk of non-compliance with another.

#### Known Structural Conflicts

**Conflict 1: PIPL Separate Consent vs. GDPR Transfer Mechanisms**

- **The tension**: PIPL Art. 39 requires separate individual consent for cross-border
  transfer regardless of which mechanism is used. GDPR permits SCCs, BCRs, and adequacy
  decisions without individual consent. A GDPR-compliant transfer via SCCs may still lack
  PIPL-required individual consent.
- **Resolution strategy**: Implement PIPL-compliant separate consent in addition to SCCs
  for transfers from EEA to China. Note that this consent must meet PIPL's specific
  standard (separate, not bundled). Assess whether this changes the GDPR legal basis
  analysis if consent is now being relied upon for the transfer element.
- **Classification**: HIGH — operational redesign required

**Conflict 2: CCPA Opt-Out vs. GDPR Opt-In**

- **The tension**: CCPA/CPRA uses opt-out for sale/sharing of personal information;
  GDPR requires opt-in consent or another legal basis. A combined EU/US privacy notice
  that offers opt-out of "sale" under CCPA is not equivalent to GDPR's affirmative
  consent requirement.
- **Resolution strategy**: Apply GDPR's opt-in standard globally (highest common
  denominator) and add CCPA-required opt-out mechanisms. This satisfies both — GDPR
  is more protective so complying with GDPR on consent will also satisfy CCPA.
- **Classification**: MEDIUM — architectural choice (applying GDPR consent globally
  resolves the conflict)

**Conflict 3: PIPL No Legitimate Interests vs. GDPR Art. 6(1)(f)**

- **The tension**: Many GDPR controllers rely on legitimate interests as the legal basis
  for analytics, fraud prevention, and direct marketing. PIPL has no equivalent. Processing
  of Chinese nationals' data requires consent or one of 6 specified alternatives —
  legitimate interests is not available.
- **Resolution strategy**: Identify all processing activities relying on GDPR Art. 6(1)(f)
  for data involving PRC persons. Re-basis each activity using PIPL alternatives or obtain
  consent. This may require product/service design changes for PRC users.
- **Classification**: HIGH — legal basis restructuring required for PRC operations

**Conflict 4: DPDP India — Processor Obligations vs. GDPR Processor Accountability**

- **The tension**: GDPR directly imposes obligations on processors (Art. 28). DPDP India's
  processor (Data Processor) accountability flows through contract with the Data Fiduciary
  — there is no direct processor regulatory obligation. A Data Processor that is DPDP-only
  compliant may lack GDPR Art. 28 documentation.
- **Resolution strategy**: Ensure contractual frameworks between Data Fiduciary and
  Data Processor meet GDPR Art. 28 standards even if DPDP does not require it. Apply
  GDPR standard as the baseline.
- **Classification**: MEDIUM — contract documentation gap

**Conflict 5: Australia NDB 30-Day Window vs. GDPR 72-Hour Requirement**

- **The tension**: The Australian Privacy Act NDB scheme provides 30 days to assess and
  notify the OAIC. GDPR requires notification within 72 hours. For an organisation holding
  Australian and EU citizen data in the same breach, the 72-hour GDPR deadline will be
  reached while the Australian assessment is still ongoing.
- **Resolution strategy**: Apply 72-hour notification as the global default for the SA/DPA
  notification; submit a separate OAIC notification complying with Australian content
  requirements. The 2024 Australian reform proposes a 72-hour requirement — if enacted,
  this conflict will dissolve. [VERIFY reform status.]
- **Classification**: LOW — dual-track notification resolves; timelines do not conflict
  if GDPR timeline is adopted globally

**Conflict 6: LGPD Legitimate Interest Scope vs. GDPR Scope**

- **The tension**: LGPD Art. 7(IX) permits processing based on legitimate interest but
  the ANPD's interpretation is narrower than EDPB WP217 — it requires a genuine social
  interest or commercial activity justification. GDPR controllers accustomed to broad
  Art. 6(1)(f) reliance may find LGPD LI requires independent justification.
- **Resolution strategy**: Conduct LGPD-specific Legitimate Interest Assessment (LIA)
  separately from GDPR LIA. Do not assume GDPR LIA satisfies LGPD.
- **Classification**: MEDIUM — documentation gap; analytical work required

---

### Step 6: Generate Harmonized Compliance Strategy

The harmonized compliance strategy is the "highest common denominator" approach — a
single compliance posture that satisfies all applicable regimes simultaneously without
requiring different behaviour for different user groups (where feasible).

#### Principle 1: Opt-In Consent Architecture Globally

**Rationale**: GDPR, LGPD, PIPL, and DPDP all require opt-in consent. CCPA/CPRA uses
opt-out but does not prohibit opt-in. Applying global opt-in consent architecture
satisfies all regimes simultaneously.

**Implementation**:

- Use a consent management platform (CMP) that supports:
  - Purpose-specific consent (GDPR Art. 7; PIPL Art. 13; LGPD Art. 8)
  - Separate consent for sensitive data (all regimes — use strictest definition overlap)
  - Separate consent for cross-border transfer (PIPL Art. 39; LGPD Art. 33; PDPA-SG)
  - Consent withdrawal mechanism as easy to use as consent provision
  - Age verification gates: <13 (GDPR minimum); <14 (PIPL); <16 (per Member State
    default); <18 (POPIA) — apply strictest per user jurisdiction
  - CCPA-required opt-out of Sale/Sharing signal (in addition to opt-in framework)
  - Global Privacy Control (GPC) signal recognition (mandatory CCPA/CPRA and several
    US states; recommended for EU)

#### Principle 2: 72-Hour Breach Notification Capability

**Rationale**: GDPR, UK GDPR, LGPD, DPDP Act all require 72-hour or similar notification.
PIPL requires "immediately." Building 72-hour capability satisfies the most demanding
common threshold.

**Implementation**:

- Incident response playbook with 72-hour SA/DPA notification as the global default
- Parallel notification tracks per regime (content requirements vary — see
  `legalcode-breach-regulatory-notification-drafter`)
- PIPL: escalate to "immediate" internal notification → external within 24 hours
- OAIC (Australia): 30-day window currently; track 2024 reform for 72-hour change
- Separate data subject notification assessment for each breach per regime
- Breach log maintained for all incidents regardless of notification threshold

#### Principle 3: Global Data Subject Rights Infrastructure

**Implementation**:

- Access request → 15 working days SLA (PIPL most demanding) with ability to document
  extensions permitted under GDPR (30 days + 2-month extension) and CCPA (45 days
  - 45 days)
- Correction → 7-day processing for PIPL; 30-day for others
- Erasure → trigger across all jurisdictions simultaneously; apply GDPR exemptions
  (ongoing legal obligation) and PIPL exemptions as applicable
- Portability → machine-readable format (GDPR Art. 20; CCPA/CPRA; LGPD Art. 18)
- Opt-out of sale/sharing → US state compliance (CCPA/CPRA + 19 state laws)
- Rights request intake that captures jurisdiction of data subject to route correctly

#### Principle 4: Controller / Data Fiduciary Agreement Framework

**Implementation**:

- Inbound DPA (as data processor/service provider) meeting GDPR Art. 28 + CCPA
  service provider restrictions + LGPD processor contract + PIPL entrustment agreement
- Outbound DPA (as controller) with all sub-processors meeting GDPR Art. 28; include
  PIPL filing obligations (10-day SCC filing for cross-border); LGPD Resolution 19/2024
  SCCs-BR provisions
- Sub-processor management: GDPR general authorisation + 30-day notice; PIPL requires
  consent/security assessment for transfers to sub-processors outside PRC

#### Principle 5: Privacy Officer / DPO Designation

**Implementation**:

- Appoint GDPR DPO where Art. 37 trigger met
- Appoint LGPD Encarregado (mandatory)
- Register Information Officer with South Africa Information Regulator (mandatory)
- Designate PIPL Personal Information Protection Officer if >1M PI processed
- Establish Grievance Officer with published contact for India (DPDP Rules)
- Cross-train as needed; role may be filled by same individual in non-conflicting capacity

#### Principle 6: Transfer Mechanism Architecture

**Implementation**:

- EU → EEA: GDPR internal transfer (no mechanism needed)
- EU → US: EU SCCs Module 2 + EU-US Data Privacy Framework (DPF) if US entity certified
- EU → UK: UK IDTA or Addendum to EU SCCs
- EU → Brazil: SCCs-BR (ANPD Resolution 19/2024) from Aug. 2025
- EU → China: EU SCCs (not direct equivalent) + PIPL Standard Contract + CAC filing +
  PIPL separate consent; security assessment if ≥1M PI
- EU → Australia, NZ, Japan: GDPR adequacy decisions exist — confirm current status
- EU → India: No adequacy; contractual protections (DPDP blacklist model not yet published)
- EU → Singapore: SCCs or PDPA Schedule 10 contractual arrangement
- Implement Transfer Impact Assessments (TIAs) for all transfers to non-adequate countries

---

### Step 7: Compliance Gap Matrix

For each applicable regime, classify the organisation's current compliance status per
dimension:

**Classification system:**

- **COMPLIANT** (green): Meets all requirements; no remediation needed
- **PARTIAL** (amber): Meets some requirements; specific gaps identified; remediation
  within standard timelines
- **NON-COMPLIANT** (red): Material gap; does not meet core requirements; remediation
  required before further processing
- **CRITICAL** (red+): Active enforcement risk; processing should be suspended pending
  remediation; immediate escalation required

**Output format:**

```
COMPLIANCE GAP MATRIX — [Organisation Name] — [Date]
Processing scope: [description]
Applicable regimes: [list]

Dimension                | GDPR | UK GDPR | CCPA | LGPD | PIPL | PDPA-SG | DPDP |
-------------------------|------|---------|------|------|------|---------|------|
Legal basis              |      |         |      |      |      |         |      |
Data subject rights      |      |         |      |      |      |         |      |
Cross-border transfers   |      |         |      |      |      |         |      |
Breach notification      |      |         |      |      |      |         |      |
DPO/Privacy Officer      |      |         |      |      |      |         |      |
Consent architecture     |      |         |      |      |      |         |      |
Sensitive data           |      |         |      |      |      |         |      |
Enforcement exposure     |      |         |      |      |      |         |      |
Documentation            |      |         |      |      |      |         |      |
Data localisation        |      |         |      |      |      |         |      |
```

---

### Step 8: Prioritization Framework

Classify all identified gaps into three remediation tiers.

**Tier 1 — Immediate (< 30 days)**: Active enforcement risk; breach notification gaps;
processing without legal basis; PIPL data export without mechanism.

**Tier 2 — Near-Term (30–90 days)**: DPO/officer appointments; consent architecture
redesign; transfer mechanism documentation; breach response plan updates.

**Tier 3 — Long-Term (90–180 days)**: Data mapping updates; privacy notice localisation;
sub-processor agreement updates; training programs; governance documentation.

---

### Step 9: Quality Verification

Before delivering output, verify:

1. **Applicability accuracy**: Have you confirmed each applicable regime with the user?
   Have MAYBE determinations been resolved?

2. **Conflict completeness**: Have you checked all 6 known structural conflicts plus any
   organisation-specific conflicts (e.g., China + EU operations, India + GDPR overlap)?

3. **Highest common denominator validation**: Does the harmonized strategy genuinely
   satisfy each applicable regime, or have you compromised on a regime's requirement?
   Flag any compromises explicitly.

4. **Classification confidence**: For any NON-COMPLIANT or CRITICAL classification, apply
   the Self-Interrogation framework (Section 9 below).

5. **Currency check**: Verify that DPDP India blacklist status, Australian 72-hour reform
   status, LGPD Encarregado exemption, and PIPL whitelist country status are current.
   Mark time-sensitive items **[VERIFY]**.

---

### Step 10: Deliver Output

Present the output using the template in Section 11.

---

## Per-Regime Reference — Quick Reference Cards

### GDPR (EU) — Key Facts

- **Lawful bases**: 6 (Art. 6) + 10 special category conditions (Art. 9(2))
- **Rights**: Access (30 days); Rectification; Erasure; Restriction; Portability; Objection; No ADM
- **Transfers**: Adequacy + SCCs + BCRs + derogations; TIA mandatory post-Schrems II
- **Breach**: 72h to SA; without undue delay to individuals (high risk)
- **DPO**: Mandatory for public bodies, large-scale monitoring, large-scale special category
- **Enforcement**: €20M / 4% global turnover; EDPB coordination
- **Max fine case**: Meta €1.2B (May 2023, Irish DPC)

### UK GDPR — Key Facts

- **Lawful bases**: Same 6 as EU GDPR + DUA 2025 Recognised Legitimate Interests
- **Rights**: Same as EU GDPR
- **Transfers**: UK adequacy regulations; IDTA (March 2022); UK SCCs Addendum
- **Breach**: 72h to ICO
- **DPO**: Mandatory — same triggers as EU GDPR
- **Enforcement**: £17.5M / 4% global turnover
- **Key divergence**: DUA Act 2025 introduces "recognised legitimate interests" (Schedule 1 list)
  expanding Art. 6(1)(f) equivalent without full LIA — significant difference from EU GDPR

### CCPA/CPRA (California) — Key Facts

- **Legal basis model**: Opt-out (no legal basis concept); opt-in for sensitive data sharing
- **Rights**: Access (45 days); Deletion; Correction; Portability; Opt-out of Sale/Sharing;
  Opt-out of ADMT (Jan. 2026); No discrimination; Appeal
- **Transfers**: No transfer mechanism restrictions — service provider contracts key
- **Breach**: Most expedient time; notify AG for 500+ CA consumers
- **DPO**: None required; CPPA privacy officer functionally recommended
- **Enforcement**: $7,500 intentional; $2,500 unintentional; $100–750 per consumer per incident (PRA)
- **Key divergence**: Opt-out model; focus on "sale/sharing" not "processing"

### LGPD (Brazil) — Key Facts

- **Lawful bases**: 10 (Art. 7) — broadest base catalogue globally; legitimate interest permitted
- **Rights**: Access (15 days); Correction; Deletion; Portability; Opt-out of consent; Opposition;
  Information on transfer; Review of automated decisions
- **Transfers**: ANPD adequacy list; SCCs-BR (Res. 19/2024 — mandatory Aug. 2025); consent
- **Breach**: 72h to ANPD (Res. 19/2024)
- **DPO (Encarregado)**: Mandatory for all controllers — SME proportionality guidance exists
- **Enforcement**: 2% Brazil annual revenue; capped R$50M per infraction; ANPD actively enforcing
- **Key divergence**: Legitimate interest permitted but ANPD interpretation narrower than EDPB

### PIPL (China) — Key Facts

- **Lawful bases**: 7 (Art. 13) — consent primary; **no legitimate interests**
- **Rights**: Access (15 working days); Correction (7 days); Deletion (7 days); Explanation of
  automated decisions; Portability (government will define)
- **Transfers**: Security assessment (≥1M PI) → Standard Contract + CAC filing (100K–999K PI) →
  Certification; March 2024 provisions ease requirements for small volume
- **Breach**: Immediately to authorities and individuals
- **DPO**: Mandatory if >1M individuals processed
- **Enforcement**: RMB 50M / 5% annual revenue; plus: business suspension, permit revocation
- **Key divergences**: No legitimate interests; separate consent for CBT; data localisation for CIIOs;
  "important data" concept (no equivalent elsewhere)

### PDPA (Singapore) — Key Facts

- **Lawful bases**: Consent + Legitimate Interests (2020 amendment, limited) + deemed consent
  - specific purpose (business contact exemption, etc.)
- **Rights**: Access (30 days); Correction (30 days); Withdraw consent; Data portability
  (PDPC portability advisory)
- **Transfers**: PDPC whitelist + Schedule 10 contractual arrangement + consent + binding rules
- **Breach**: 3 calendar days to PDPC if notifiable (significant harm or >500 individuals)
- **DPO**: Not mandatory; voluntary registration recommended; MNC DPO designation common
- **Enforcement**: SGD 1M or 10% Singapore annual turnover
- **Key divergence**: Deemed consent with notification (2020) allows processing with adequate
  notice if individual does not object — lower burden than EU consent in some scenarios

### POPIA (South Africa) — Key Facts

- **Lawful bases**: 6 conditions (s.11) — consent, contract, public interest, legal obligation,
  legitimate interest, vital interests — closely mirrors GDPR
- **Rights**: Access (30 days); Correction/deletion (30 days); Objection; No ADM; Complaint to
  Information Regulator
- **Transfers**: Adequate protection standard (Condition 8, s.72) — Information Regulator developing
  adequacy list and transfer guidance
- **Breach**: As soon as reasonably possible; Information Regulator expects 72-hour urgency
- **DPO (Information Officer)**: Mandatory for ALL public and private bodies; must register with
  Information Regulator; serious obligation
- **Enforcement**: ZAR 10M; criminal penalties up to 10 years; civil liability
- **Key divergence**: Mandatory Information Officer registration with regulator (no EU equivalent
  of registration); criminal liability provisions broader than GDPR

### APPI (Japan) — Key Facts

- **Legal basis model**: Purpose specification + use limitation — no enumerated bases (unlike GDPR)
- **Rights**: Access; Correction; Cessation of use (grounds-based); Opt-out of third-party provision
- **Transfers**: Equivalent protection standard; opt-in consent for non-equivalent countries; PPC
  framework approval (Japan has GDPR adequacy); Pseudonymous data exempt from CBT restrictions
- **Breach**: 30 days to PPC (60 days for third-party incidents); individual notification promptly
- **DPO**: Not mandatory
- **Enforcement**: JPY 100M per corporation
- **Key divergence**: Purpose specification model (not legal basis); pseudonymous information
  concept (allows more flexible use within organisation); opt-out mechanism for third-party
  provision of standard (non-sensitive) personal data

### Privacy Act (Australia) — Key Facts

- **Legal basis model**: APPs — reasonable necessity + consent for sensitive data; no enumerated bases
- **Rights**: Access (30 days); Correction (30 days); Complaint to OAIC
- **Transfers**: Contractual protections (APP 8); OAIC binding schemes; consent; no adequacy model
- **Breach**: 30 days to OAIC (NDB scheme); 2024 reform proposes 72 hours [VERIFY status]
- **DPO**: Not mandatory (recommended)
- **Enforcement**: AUD 50M or 30% Australian turnover (2022 reform); 2024 reform adds new tiers
- **Key divergence**: No right to erasure (not in 2024 first-tranche reform; deferred to second tranche);
  APP 8 accountability transfers (not adequacy/transfer-mechanism model)

### DPDP Act (India) — Key Facts

- **Lawful bases**: Consent (primary) + 8 "Legitimate Uses" (Art. 7) — no general legitimate interests
- **Rights**: Access (TBD in Rules); Correction; Erasure; Grievance mechanism; Data Fiduciary summary;
  Nominee rights; Right to withdraw consent
- **Transfers**: Government blacklist model — transfers permitted except to restricted countries;
  blacklist not yet published (early 2026) [VERIFY]
- **Breach**: 72-hour initial report to DPB + individual notification; full follow-up report within 72h
- **DPO**: Not mandatory; Grievance Officer required; Consent Manager (from Nov. 2026) is a separate
  registered intermediary
- **Enforcement**: ₹250 crore (~USD 30M) per incident; ₹500 crore for breach notification violations
- **Key divergences**: No sensitive data category; DPB (not a traditional DPA — adjudicatory model);
  Consent Manager regulatory innovation; Significant Data Fiduciary (SDF) designation by government
  triggers additional obligations; no processor direct obligations

### NZ Privacy Act 2020 — Key Facts

- **Legal basis model**: IPPs — collection limitation + purpose; no enumerated bases
- **Rights**: Access (20 days); Correction; Complaint to OPC-NZ
- **Transfers**: Comparable protection standard; model contract clauses
- **Breach**: As soon as practicable; NZ serious harm standard
- **DPO**: Not mandatory; Privacy Officer role functional requirement for agencies
- **Enforcement**: NZD 10,000 per individual; court compensation for organisations; remedies-based
- **Key divergence**: Most closely aligned with Australian approach; Pacific regional cooperation

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. Fail → revise before delivery.

| Gate           | Rule                                                                                                        | Fail Action                           |
| -------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Source**     | Every legal claim cites specific article, section, or regulation                                            | Add citation or mark **[UNVERIFIED]** |
| **Format**     | Citations follow consistent format per jurisdiction (Art. XX for EU; § XX for US; s. XX for AU/UK)          | Fix format                            |
| **Currency**   | Every cited provision checked for amendments, new regulations, blacklists, adequacy lists                   | Flag **[CHECK CURRENCY]**             |
| **Domain**     | Analysis stays within regime scope — do not cross-apply GDPR concepts to PIPL without noting the difference | Remove or flag jurisdictional bleed   |
| **Confidence** | Uncertainty explicitly stated; no false certainty about jurisdiction-specific rules                         | Add confidence qualifier              |

---

## Self-Interrogation for CRITICAL / NON-COMPLIANT Items

For any classification at CRITICAL or NON-COMPLIANT, apply this 3-pass review:

**Pass 1 — Legal Chain**: Does the non-compliance conclusion follow from the cited rule?
Is there an exception or derogation that applies? Would the relevant supervisory authority
(EDPB, PDPC, CAC, Information Regulator) reach this conclusion?

**Pass 2 — Completeness**: Have all parallel regimes been checked for the same dimension?
Does the same gap exist across all applicable regimes or only in one?

**Pass 3 — Challenge**: What is the strongest argument that the organisation IS compliant
on this dimension? What would opposing counsel argue? Under what circumstances might a
regulator accept the current approach?

---

## Confidence Scoring

| Level        | Range     | Action                                                                    |
| ------------ | --------- | ------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | State with confidence — settled law or clear statutory text               |
| **High**     | 0.80–0.94 | State with brief caveat — strong authority, minor interpretive questions  |
| **Probable** | 0.60–0.79 | State with reasoning and contra-indicators — regulatory guidance evolving |
| **Possible** | 0.40–0.59 | Flag for specialist review — genuinely uncertain area                     |
| **Unlikely** | 0.0–0.39  | Do not assert; flag **[UNCERTAIN]** — weak basis, speculative             |

Apply to: blacklist publication status (DPDP India); ANPD legitimate interest scope
(Brazil); adequacy status of any jurisdiction; emerging framework enforcement triggers.

---

## Glass Box Audit Trail

Include the following YAML block in every output:

```yaml
glass_box:
  skill_name: "legalcode-multi-jurisdiction-privacy-comparison"
  run_date: "[date]"
  organisation: "[organisation name or 'Not disclosed']"
  processing_scope: "[description of processing activities assessed]"
  regimes_assessed: "[list of applicable regimes]"
  regimes_excluded: "[list of core regimes determined not applicable + reason]"
  emerging_frameworks_flagged: "[list of emerging frameworks relevant to this organisation]"
  legalcode_mcp: "[Connected / Not connected]"
  conflicts_identified: "[N conflicts, [list by name]]"
  critical_gaps: "[N critical gaps]"
  non_compliant_dimensions: "[list]"
  harmonized_strategy_confidence: "[HIGH / MEDIUM / LOW — rationale]"
  known_limitations:
    - "DPDP India blacklist not yet published — transfer restriction analysis provisional"
    - "Australian 72-hour breach reform status unconfirmed — verify before breach planning"
    - "ANPD legitimate interest scope evolving — verify current regulatory position"
    - "[Any additional organisation-specific limitations]"
  time_sensitive_items:
    - "[Item requiring verification before next review date]"
  next_review_recommended: "[date or trigger event]"
  reviewer: "AI-assisted — requires qualified privacy counsel review in each applicable jurisdiction"
```

---

## Anti-Patterns

What NOT to do when performing multi-jurisdiction privacy comparisons:

1. **GDPR-washing**: Assuming GDPR compliance satisfies all other regimes. PIPL, DPDP, and
   LGPD each have material differences from GDPR that require independent analysis.

2. **Treating PIPL as a GDPR variant**: PIPL has no legitimate interests, requires separate
   consent for cross-border transfers, and imposes data localisation for CIIOs. It is not
   a GDPR-aligned law — it reflects a different governance philosophy.

3. **Forgetting the processor chain**: Multi-jurisdiction compliance failures often occur
   in sub-processor relationships. A GDPR-compliant controller using a PIPL-noncompliant
   US sub-processor for Chinese user data creates dual exposure.

4. **Using a single transfer mechanism globally**: EU SCCs do not satisfy PIPL's Standard
   Contract obligation. LGPD SCCs-BR (August 2025) are not the same as EU SCCs. Each
   regime requires its own mechanism or a PIPL-compatible consent overlay.

5. **Ignoring the PIPL separate consent requirement**: Companies implementing SCCs for
   China-EU transfers frequently miss PIPL Art. 39's additional "separate consent"
   requirement. SCCs + separate consent is required; SCCs alone is insufficient.

6. **Assuming CCPA opt-out = sufficient for global marketing**: EU/UK/Brazil/India users
   require opt-in consent. A US-centric opt-out architecture fails GDPR, UK GDPR, LGPD,
   and DPDP simultaneously.

7. **Treating breach notification timelines as jurisdiction-specific silos**: A breach
   affecting EU and Indian users simultaneously triggers both GDPR's 72-hour and DPDP's
   72-hour windows — running in parallel with different content requirements for each SA.

8. **Registering only one DPO for multi-jurisdiction operations**: UK GDPR may require a
   separate UK DPO from the EU DPO if the UK entity operates independently. POPIA's
   Information Officer must be registered separately with the South Africa Information
   Regulator. One global DPO does not automatically satisfy all regimes.

9. **Waiting for DPDP India enforcement before acting**: DPDP Phase 1 began November 2025.
   The Data Protection Board is being constituted. Waiting for enforcement creates
   retroactive exposure — build compliance before the DPB becomes fully operational.

10. **Conflating "no data localisation" with "free transfers"**: Most regimes allow transfers
    but impose conditions (mechanisms, TIAs, contracts). The absence of localisation
    requirements does not mean transfers are unrestricted.

11. **Applying APPI's opt-out third-party provision to non-Japanese contexts**: APPI's
    opt-out mechanism for third-party provision is specific to Japan's framework. It does
    not satisfy GDPR, LGPD, or PIPL where opt-in is required.

12. **Missing the POPIA Information Officer registration**: Unlike GDPR DPO (notify lead DPA
    contact only), POPIA requires formal registration of Information Officers with the
    South Africa Information Regulator. This is often overlooked by international companies.

13. **Assuming Canada CPPA is in force**: Bill C-27 / CPPA was not in force as of early 2026. Continue applying PIPEDA + provincial PIPEDA-equivalents (BC, AB, QC). Track
    C-27 legislative progress — it will significantly increase PIPEDA enforcement capacity.

14. **Overlooking Thailand, Indonesia, and Vietnam in ASEAN operations**: Companies
    operating across ASEAN with PDPA Singapore compliance often miss Thailand's PDPA-TH
    (in force May 2022), Indonesia's new PDP Law (in force Oct. 2024), and Vietnam's Decree 13.

15. **Underestimating PIPL enforcement velocity**: The Didi Global RMB 8.026B fine (USD 1.2B)
    established that PIPL enforcement can be existential. Unlike early GDPR enforcement,
    PIPL enforcement has been high-profile and high-value from the outset.

16. **Producing a comparison without a conflict map**: A regime comparison that identifies
    differences but does not identify genuine conflicts where complying with one law risks
    non-compliance with another is insufficient for operational guidance.

17. **Not tracking the DPDP blacklist**: India's DPDP transfer restriction model depends on
    a government-issued blacklist of restricted countries. Until published, all transfers are
    technically permitted — but the list could appear with short notice. Monitor MeitY
    notifications.

18. **Advising on PIPL without PRC-qualified counsel**: PIPL involves national security
    review, CIIO classification, and CAC approval processes that require PRC-licensed counsel.
    Do not provide final PIPL transfer mechanism advice without PRC specialist review.

19. **Treating NZ Privacy Act as equivalent to Australia APPs**: New Zealand and Australia
    have separately evolved privacy frameworks. APP entities with AU and NZ operations
    require separate analysis under each law.

20. **Not reassessing when new adequacy decisions or blacklists are published**: The cross-
    border transfer analysis is highly time-sensitive. EU adequacy decisions can be
    invalidated (Schrems I, Schrems II); DPDP blacklist will be published; ANPD adequacy
    list is under development. Build a monitoring trigger into the output.

---

## Writing Standards

Before delivering any output:

1. **Jurisdiction labels are precise**: Always label conclusions with the regime name (not
   "the law" or "EU regulations") — multiple "laws" apply simultaneously.

2. **Distinguish controller from processor obligations**: Many regimes impose different
   duties on controllers vs. processors. Specify which role the analysis applies to.

3. **Mark all pending items**: All items awaiting regulatory action (DPDP blacklist, ANPD
   adequacy list, Australian 72-hour reform, Canada CPPA) must be marked **[VERIFY/MONITOR]**.

4. **Quantify penalty exposure**: For each applicable regime, state the maximum penalty in
   local currency and USD equivalent as a reference. Where enforcement benchmarks exist,
   cite the highest relevant case.

5. **No false precision on "immediately"**: PIPL's breach notification requirement is
   "immediately" — do not translate this to a specific hour count without citing regulatory
   guidance that provides one. State the uncertainty explicitly.

6. **Conflict classifications are conservative**: When in doubt, classify a cross-regime
   tension as HIGH (requiring operational redesign) rather than MEDIUM (documentation gap).
   The cost of under-estimating a conflict is greater than the cost of over-engineering a
   resolution.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for: current adequacy decisions per regime; latest DPDP blacklist/whitelist status;
  ANPD SCCs-BR requirements; PIPL Standard Contract CAC filing guidance; PDPA Singapore
  whitelist countries; Information Regulator South Africa transfer adequacy guidance
- Save results to `/tmp/legalcode-mjpc-research.md`
- Mark all legalcode-mcp verified citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed with training-data research
- Mark all statutory and adequacy references **[VERIFY]**
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag time-sensitive items for client verification before reliance

---

## Output Format Template

```markdown
# Multi-Jurisdiction Privacy Compliance Report

**Organisation**: [Name]
**Date**: [Date]
**Prepared by**: Legalcode AI — requires qualified legal review
**Scope**: [Processing activities assessed]

---

## Executive Summary

**Applicable regimes**: [N of 12+ core regimes]
**Critical gaps identified**: [N]
**Non-compliant dimensions**: [N]
**Cross-regime conflicts**: [N]
**Harmonized strategy available**: [Yes / Yes with caveats / No — conflicts require resolution]

**Top 3 priority actions**:

1. [Highest urgency item]
2. [Second priority]
3. [Third priority]

---

## Applicability Analysis

[Applicability table per regime]

---

## Compliance Gap Matrix

[Full 10-dimension × N-regime gap matrix]

---

## Cross-Regime Conflicts

[For each conflict: description, classification (HIGH/MEDIUM/LOW), resolution strategy]

---

## Harmonized Compliance Strategy

[6 principles with implementation guidance tailored to organisation]

---

## Prioritized Remediation Roadmap

### Tier 1 — Immediate (< 30 days)

[Action items with responsible party, target date, regime(s) addressed]

### Tier 2 — Near-Term (30–90 days)

[Action items]

### Tier 3 — Long-Term (90–180 days)

[Action items]

---

## Jurisdiction Deep-Dive Notes

[For each applicable regime: key findings specific to this organisation's operations]

---

## Glass Box Audit Trail

[YAML block per template above]

---

## Disclaimer and Next Steps

This report was prepared with AI assistance. All conclusions must be reviewed by qualified
privacy counsel licensed in each applicable jurisdiction before reliance or action.

**Recommended specialist review**: [List regimes where local counsel review is essential,
particularly PIPL (PRC counsel), POPIA (ZA counsel), DPDP (India counsel)]
```

---

## Localization Notes

This skill is itself jurisdiction-agnostic — it covers all 12 core regimes simultaneously.
When a specific jurisdiction-specific skill is needed alongside this comparison:

- **GDPR deep-dive**: `legalcode-gdpr-legal-basis-assessment`, `legalcode-dpia-generator`,
  `legalcode-legitimate-interest-assessment`
- **US state law details**: `legalcode-us-state-privacy-comparison`
- **Data subject access requests**: `legalcode-dsar-workflow-builder`
- **Cross-border transfer deep-dive**: `legalcode-cross-border-transfer-assessment`
- **Vendor assessment**: `legalcode-vendor-privacy-assessment`
- **Breach notification drafting**: `legalcode-breach-regulatory-notification-drafter`

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis. Primary research via web-backed
sources and in-repository pattern analysis. Key frameworks analysed:

**EU / International**:

- GDPR Reg. 2016/679; UK GDPR + DPA 2018 + DUA 2025
- EDPB Guidelines 9/2022 (breach notification); EDPB Guidelines 05/2020 (consent)

**Americas**:

- Cal. Civ. Code §§ 1798.100 et seq. (CCPA/CPRA)
- LGPD Law No. 13,709/2018; ANPD Resolution 19/2024 (SCCs-BR; breach)
- PIPEDA, S.C. 2000, c. 5

**Asia-Pacific**:

- PIPL (2021); CAC Regulations on Cross-Border Data Flows (March 2024)
- PDPA Singapore (2012 + 2020/2021 amendments)
- APPI (2003 + April 2022 amendment)
- Privacy Act 1988 (Australia) + Privacy and Other Legislation Amendment Act 2024
- DPDP Act 2023 (India) + DPDP Rules 2025
- New Zealand Privacy Act 2020

**Africa**:

- POPIA (2013), in force July 2021

**Reference quality standard**: `legalcode-contract-review` (glass box, quality frameworks,
anti-patterns, workflow design); `legalcode-us-state-privacy-comparison` (cross-regime
matrix architecture); `legalcode-gdpr-legal-basis-assessment` (disclaimer depth, legal
basis table design).
