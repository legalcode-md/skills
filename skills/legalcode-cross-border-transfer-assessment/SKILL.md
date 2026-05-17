---
name: legalcode-cross-border-transfer-assessment
description: >
  Assess the lawfulness of international personal data transfers under GDPR Chapter V,
  UK GDPR, and Swiss DPA (nDSG). Use when transferring personal data outside the EEA/UK/
  Switzerland to a third country; when selecting or validating a transfer mechanism
  (adequacy decision, SCCs, BCRs, derogations); when building or reviewing a Transfer
  Impact Assessment (TIA) post-Schrems II; when assessing supplementary technical and
  organisational measures; when evaluating destination-country surveillance law (FISA 702,
  EO 12333, CLOUD Act, China PIPL/MPS, India DPDP); when reviewing Binding Corporate Rules
  for intra-group transfers; or when advising on Art. 49 derogations. Produces a mechanism
  selection decision, TIA, supplementary measures catalogue, risk classification
  (LAWFUL/RESTRICTED/UNLAWFUL per transfer), remediation roadmap, and Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Cross-Border Transfer Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted assessment of
> international data transfer lawfulness under GDPR Chapter V, UK GDPR, and Swiss DPA.
> It does not constitute legal advice. All outputs must be reviewed by a qualified privacy
> counsel or Data Protection Officer licensed in the relevant jurisdiction before any
> reliance or action. Laws, regulatory guidance, adequacy decisions, and enforcement posture
> change — verify currency before relying on any legal conclusion. Statutory and case law
> references cited from training data carry hallucination risk — verify against authoritative
> sources before use. Mark any unverified citation **[VERIFY]**.

---

## Purpose and Scope

This skill performs a structured, end-to-end assessment of international personal data
transfers for lawfulness under the three primary European transfer regimes.

**This skill covers:**
- Transfer trigger analysis — whether GDPR Chapter V applies to a given data flow
- Mechanism selection decision tree — adequacy → SCCs → BCRs → derogations, with UK and
  Swiss parallel tracks
- Transfer Impact Assessment (TIA) per the EDPB six-step methodology (Recommendations
  01/2020, v2.0) and CNIL Practical Guide (January 2025)
- Third-country legal framework assessment — surveillance law analysis for the US, China,
  India, and other high-risk destinations
- EU-US Data Privacy Framework (DPF) assessment — current status, certification, and
  litigation risk (as of March 2026: PCLOB disruption and ongoing Schrems III proceedings)
- UK GDPR parallel analysis — IDTA, UK Addendum to EU SCCs, ICO 2026 updated guidance,
  UK adequacy decisions post-Brexit
- Swiss nDSG (revised DPA effective 1 September 2023) — FDPIC adequacy list, transfer tools
- Supplementary measures — technical (encryption, pseudonymization, split processing),
  organisational (audit rights, deletion obligations), and contractual (enhanced SCCs)
- Binding Corporate Rules (BCR) assessment — coverage, required 2024 updates, compliance gaps
- Art. 49 derogations — specific situations, limitations on "occasional" use, consent
  requirements
- Risk classification per transfer: LAWFUL / RESTRICTED / UNLAWFUL
- Remediation roadmap with prioritised corrective actions and deadlines
- Documentation package — TIA record, ROPA update, DPA schedule, Glass Box audit trail

**This skill does not:**
- Provide legal advice or replace qualified privacy counsel
- Guarantee regulatory approval or protect against enforcement
- Cover non-GDPR transfer regimes (CCPA, LGPD, PIPEDA, PDPA Singapore) — see dedicated
  jurisdiction skills for those frameworks
- Draft full Standard Contractual Clauses text — see `legalcode-contract-review` for DPA
  and SCC drafting and review

**Complementary skills:**
- `legalcode-dpia-generator` — DPIA for high-risk processing (often required alongside TIA)
- `legalcode-dsar-workflow-builder` — DSAR operations
- `legalcode-contract-review` — full contract review including DPA/SCC clauses
- `legalcode-breach-severity-assessment` — post-breach classification

---

## Jurisdiction and Governing Law

This skill is multi-jurisdiction by design. It operates across three parallel transfer
regimes that share common origins but diverge in important ways.

### Primary Regimes Covered

| Regime | Legal Basis | Supervisory Authority | Transfer Tools |
|--------|-------------|----------------------|----------------|
| **EU GDPR** | Regulation (EU) 2016/679, Chapter V (Art. 44-49) | Lead SA + EDPB | Adequacy decisions, SCCs (2021), BCRs, Art. 49 derogations, Art. 46 ad hoc clauses, approved codes |
| **UK GDPR** | UK GDPR + DPA 2018, Part 3 Chapter V | ICO | UK adequacy regulations, IDTA (21 March 2022), UK Addendum to EU SCCs, BCRs, UK derogations |
| **Swiss nDSG** | Federal Act on Data Protection (revised), effective 1 Sep 2023 | FDPIC | FDPIC adequacy list, SCCs (EU SCCs with Swiss amendments), BCRs, derogations |

### Key Principle: Essential Equivalence

The overarching standard across all three regimes (and confirmed by Schrems II, C-311/18)
is **essential equivalence**: personal data exported from the EEA/UK/Switzerland must enjoy
a level of protection essentially equivalent to that guaranteed in the exporting jurisdiction.
This is not a requirement for identical protection — but it must be substantively equivalent.

[JURISDICTION-SPECIFIC] Before finalising any transfer assessment, identify and apply:
- Sector-specific transfer restrictions (health data, financial data, children's data,
  national security data — these may impose stricter requirements than GDPR Chapter V alone)
- National derogations to GDPR that affect the transfer analysis in the exporting Member State
- Member State guidance supplementing EDPB recommendations (e.g., CNIL TIA Guide, AEPD
  guidance, GPDP Italian guidance)
- Post-Brexit divergence between EU and UK regimes — transfers from UK to third countries
  require UK-law analysis; transfers from EU to UK are governed by the EU-UK adequacy decisions

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** prompts at key decision forks. Rather than assuming the
user's context, the workflow pauses and asks when:

- The answer materially changes the mechanism selection (e.g., whether data goes to US or
  China changes the entire TIA risk profile)
- Multiple transfer mechanisms could apply and the user's choice is not obvious
- The nature of the data or the role of the parties (controller/processor) is ambiguous
- Risk tolerance decisions need user input to classify as RESTRICTED vs. UNLAWFUL

Present CLARIFY prompts as structured options. If the user has already provided the
information, skip the question and proceed, stating any assumptions explicitly.

---

## Workflow

### Step 1: Accept the Transfer Description

Accept input in any format:
- **Transfer description**: Source entity, destination entity, destination country, data
  categories, data subjects, processing purpose, transfer mechanism (if already chosen)
- **Existing TIA or transfer record**: Document to review for completeness and accuracy
- **Data Processing Agreement (DPA)** or **vendor contract**: Extract cross-border transfer
  provisions and assess their adequacy
- **Transfer mapping output**: Spreadsheet or RoPA entry identifying international flows

If no transfer details are provided, ask the user to describe the transfer: who sends what
data to whom, in which country, for what purpose.

### Step 2: Gather Context

**⟁ CLARIFY** — Before proceeding, ask these questions where the answers have not been
provided. Present as structured options:

1. **Exporting regime(s)**: Which regulatory framework(s) govern the export?
   - Options: EU GDPR only, UK GDPR only, Swiss nDSG only, EU + UK (dual analysis required),
     EU + Swiss, All three, Not sure — I'll identify from the description
   - *Why this matters*: Determines which transfer tools are available and which authorities
     have oversight.

2. **Destination country / countries**: Where is the data going?
   - Free text — enter the destination country or countries.
   - *Why this matters*: Whether the destination has an adequacy decision entirely determines
     whether a TIA is needed. US-bound transfers require DPF analysis; China-bound require
     PIPL/MLPS analysis; India-bound require DPDP analysis.

3. **Parties' roles**: What is the relationship between the exporting and importing entities?
   - Options: Controller → Controller (Art. 46 Module 1 SCCs), Controller → Processor
     (Module 2), Processor → Processor (Module 3), Processor → Controller (Module 4),
     Intra-group (BCRs may apply), Mixed or unclear
   - *Why this matters*: Determines which SCC module applies and whether BCRs are a viable
     option.

4. **Data categories**: What types of personal data are involved?
   - Options: Ordinary personal data only, Special-category data (health, biometric, racial/
     ethnic origin, criminal records, etc.), Children's data, Employee/HR data, Mix of
     ordinary and special category
   - *Why this matters*: Special-category data in transit demands more protective technical
     measures and a higher TIA standard.

5. **Transfer scale and frequency**: What is the volume and regularity?
   - Options: Occasional / one-time (potential Art. 49 derogation territory), Regular ongoing
     transfers (systematic), Large-scale transfers (millions of data subjects or records)
   - *Why this matters*: "Occasional" is the key limiter on Art. 49 derogations. Large-scale
     systematic transfers to high-risk countries attract highest regulatory scrutiny.

6. **Existing transfer mechanism**: Does one already exist?
   - Options: Yes — adequacy decision (specify), Yes — SCCs (which version?), Yes — BCRs,
     Yes — Art. 49 derogation, None in place (needs selection), Unclear / need to verify
   - *Why this matters*: Determines whether to do mechanism selection vs. mechanism review.

If the user provides partial context, proceed with what is available, stating assumptions
explicitly (e.g., "Assuming controller-to-processor relationship — confirm if different").

### Step 3: Transfer Trigger Analysis

Before selecting a mechanism, confirm that GDPR Chapter V is engaged. Not all data flows
involving a non-EU entity are "transfers" in the GDPR sense.

**The two-step test:**

**Step 3a — Is there personal data processing?**
- Confirm that personal data (as defined in Art. 4(1) GDPR) is involved
- If anonymised data only → not personal data → Chapter V does not apply
- If pseudonymised data → still personal data (GDPR Recital 26) → Chapter V applies

**Step 3b — Is it a "transfer" to a third country?**

Apply the EDPB definition (Recommendation 01/2020, §13):
1. A controller or processor is **subject to GDPR** for the processing
2. That controller/processor **"makes available"** personal data
3. **To another controller, joint controller, or processor** in a third country or
   international organisation

**Not transfers:**
- Transmission between entities both established in the EEA (EEA-to-EEA flows)
- An EEA controller accessing data stored in a third-country cloud, where the cloud
  provider is acting as a processor without accessing the data (data physically in EEA)
- Transit through a third country without data access by the transit-country entity
- Employees in the EEA remotely accessing third-country systems (may be a transfer from
  the third country's data into the EEA, not the other way)

**Note: Onward transfers**
If data is first transferred from EEA to Country A under valid mechanism, and Country A
onward-transfers to Country B, the onward transfer is also subject to Chapter V and must
be covered by a chain of appropriate safeguards (see Module 1/2 SCC Clause 8.7 and 8.8).

**Output:**
- TRANSFERS: List each identified transfer with source, destination country, parties, data
  categories
- NOT TRANSFERS: Identify any data flows excluded from Chapter V analysis (with rationale)
- UNCERTAIN: Flag any flows requiring further factual investigation

### Step 4: Mechanism Selection

For each transfer identified in Step 3, apply the mechanism selection hierarchy. The order
is mandated: adequacy first, then appropriate safeguards, then derogations as last resort.

#### Level 1 — Adequacy Decision (Art. 45 GDPR)

**EU adequacy decisions (as of March 2026):**

| Country/Territory | Decision | Key Notes |
|-------------------|----------|-----------|
| Andorra | ✅ Adequate | |
| Argentina | ✅ Adequate | Under Commission review for currency [VERIFY] |
| Canada (PIPEDA) | ✅ Adequate | Commercial sector only; public sector excluded |
| Faroe Islands | ✅ Adequate | |
| Guernsey | ✅ Adequate | |
| Israel | ✅ Adequate | |
| Isle of Man | ✅ Adequate | |
| Japan | ✅ Adequate | Supplementary rules with APPI apply |
| Jersey | ✅ Adequate | |
| New Zealand | ✅ Adequate | |
| Republic of Korea | ✅ Adequate | Sectors covered by PIPA only |
| Switzerland | ✅ Adequate | EU→CH transfers; CH is not EEA |
| United Kingdom | ✅ Adequate | EU→UK; under Commission review — extension proposed in 2025 |
| United States (DPF) | ⚠️ Conditional | DPF certified organisations only; significant legal uncertainty (see TIA Section below) |
| Uruguay | ✅ Adequate | |
| Brazil | 🔄 Pending | EDPB Opinion 28/2025 adopted; awaiting Commission decision [VERIFY] |

[JURISDICTION-SPECIFIC] Check the Commission's current adequacy list at the time of
assessment — decisions are reviewed, amended, and occasionally invalidated (Privacy Shield:
invalidated July 2020; EU-US Safe Harbor: invalidated October 2015).

**UK adequacy regulations (as of March 2026):**
The UK has granted adequacy to EEA countries + EU-adequate countries (by reference) plus
additional countries via its own regulations. UK → US: no blanket UK adequacy for the US;
organisations must use IDTA or UK Addendum. UK → EU: covered by EU adequacy decision for
the UK. [VERIFY current UK adequacy list against ICO website]

**Swiss FDPIC adequacy list:**
Switzerland maintains its own list. Most EU-adequate countries are also Swiss-adequate, but
check the FDPIC list independently. [VERIFY]

**If adequacy applies:**
→ Transfer is LAWFUL without further mechanism requirements.
→ Document: the adequacy decision relied upon, the decision date, and the GDPR Art. 45
  legal basis in the RoPA.
→ Monitor: Set calendar reminder to check adequacy decision status annually — decisions are
  time-limited, reviewed, and can be invalidated.

**If adequacy does not apply:**
→ Proceed to Level 2.

#### Level 2 — Appropriate Safeguards (Art. 46 GDPR)

**2a. Standard Contractual Clauses (SCCs) — EU Commission Decision 2021/914**

The 2021 SCCs (effective 27 June 2021; mandatory for new contracts after 27 September 2021)
have four modules:

| Module | Use case | Parties |
|--------|----------|---------|
| **Module 1** | Controller → Controller (C2C) | EEA controller exports to non-EEA controller |
| **Module 2** | Controller → Processor (C2P) | EEA controller exports to non-EEA processor |
| **Module 3** | Processor → Processor (P2P) | EEA processor exports to non-EEA sub-processor |
| **Module 4** | Processor → Controller (P2C) | EEA processor exports back to non-EEA controller |

**Module selection decision:**

**⟁ CLARIFY** — If the parties' roles are unclear, ask: "Is the entity receiving the data
acting under instructions from the sender (processor) or independently determining the
purpose and means of processing (controller)?" Classify before proceeding.

**SCC implementation checklist:**
- [ ] Correct module selected for the transfer relationship
- [ ] Annex I (A): Description of transfer (parties, data subjects, categories, purposes,
  retention, transfers to third parties)
- [ ] Annex I (B): Competent supervisory authority identified
- [ ] Annex I (C): Local representative identified (if applicable)
- [ ] Annex II: Technical and organisational measures (TOMs) — must be specific and up-to-date
- [ ] Annex III (Module 2/3 only): List of sub-processors
- [ ] Clause 14: Local law assessment completed and documented (TIA — see Step 5)
- [ ] Supplementary measures documented (if TIA reveals risks — see Step 6)
- [ ] Docking clause completed if additional parties join later
- [ ] Execution: signed and dated by both parties

**2025 SCC Update:** The Commission updated the SCCs in 2025 to address transfers between
GDPR-bound entities in non-EEA countries and to add Data Sovereignty Clauses requiring
cloud providers to ensure data remains under EU jurisdiction when resisting third-country
government access demands. [VERIFY applicability to the specific transfer]

**2b. UK Transfer Tools**

For transfers subject to UK GDPR:

- **International Data Transfer Agreement (IDTA)** (ICO, effective 21 March 2022):
  - A standalone agreement replacing the old SCCs for UK-regulated transfers
  - Four tables: (A) Parties, (B) Transfer details, (C) Technical security, (D) Additional
    clauses
  - Must be used for UK-regulated transfers starting from 21 March 2024 (transition period ended)
  - ICO published updated guidance in 2026 [VERIFY current ICO guidance]

- **UK Addendum to EU SCCs** (ICO, effective 21 March 2022):
  - An addendum to the 2021 EU SCCs that converts them into a valid UK transfer tool
  - Easier where EU SCCs are already in place with a counterparty
  - The addendum modifies the EU SCCs to work under UK law

**⟁ CLARIFY** — If the transfer is dual-regulated (both EU and UK GDPR apply), ask: "Do
you want to use the UK Addendum to the EU SCCs (one combined document) or maintain separate
EU SCCs + UK IDTA?" The combined approach is administratively simpler; separate documents
are cleaner legally.

**2c. Binding Corporate Rules (BCRs)**

BCRs are intra-group policies approved by a Lead Supervisory Authority (via the EDPB
consistency mechanism) that authorise transfers within a corporate group.

**When BCRs are appropriate:**
- Large multinational group with frequent intra-group transfers across multiple third countries
- Willing to invest 18-36 months in the approval process
- Resources to maintain and annually update the BCRs

**2024 BCR update obligation:**
All existing BCR holders were required to update their BCRs by end of 2024 to incorporate:
- Schrems II TIA requirements (documented ability to comply despite government access requests)
- Expanded third-party beneficiary rights
- More granular audit programme information
- Exhaustive list of legal bases for processing
[VERIFY current EDPB BCR requirements — EDPB Document March 2025]

**BCR compliance checklist:**
- [ ] BCRs cover all entities and countries to which data is transferred
- [ ] Schrems II / TIA documentation incorporated into BCRs (2024 update)
- [ ] Annual update cycle on track
- [ ] Complaints mechanism operational
- [ ] Third-party beneficiary rights documented and accessible to data subjects
- [ ] EDPB consistency mechanism approval still valid (re-approval may be needed for
  material changes)

**2d. Ad hoc Contractual Clauses (Art. 46(3))**

Subject to supervisory authority authorisation — rarely used in practice due to complexity.
Document the authorisation and do not rely on this mechanism without SA approval. [VERIFY]

**2e. Approved Codes of Conduct / Certification (Art. 46(2)(e)(f))**

Emerging mechanisms — check for approved codes in relevant sectors. [VERIFY]

#### Level 3 — Derogations for Specific Situations (Art. 49 GDPR)

Derogations are **not alternative mechanisms** — they are narrow exceptions for specific,
non-systematic situations. The EDPB has made clear they must be interpreted strictly.

| Derogation | Key Conditions | Limitations |
|------------|---------------|-------------|
| **Consent** (Art. 49(1)(a)) | Explicit, informed consent after being told of risks of transferring to non-adequate country | Cannot be used for systematic / repeated transfers; consent burden is high |
| **Contract performance** (Art. 49(1)(b)) | Transfer necessary for contract between data subject and controller | "Necessary" is narrow — not "useful" or "convenient" |
| **Public interest** (Art. 49(1)(d)) | Transfer necessary for important public interest recognised in EU or Member State law | Must be recognised by law — organisational self-interest does not qualify |
| **Legal claims** (Art. 49(1)(e)) | Transfer necessary for establishment, exercise, or defence of legal claims | Must be actually needed for litigation/regulatory proceedings |
| **Vital interests** (Art. 49(1)(f)) | Data subject or others physically at risk; data subject incapable of giving consent | Last resort — narrow life-or-death situations |
| **Compelling legitimate interests** (Art. 49(1) last para) | Exceptional circumstances; not repetitive; overriding legitimate interest not outweighed by subject's interests; supervisor notified | High bar — must notify the supervisory authority; rarely sustainable |

**⟁ CLARIFY** — If derogations are being considered, confirm: "Is this transfer occasional
and truly exceptional, or does it happen regularly?" Regular reliance on Art. 49 derogations
is non-compliant — EDPB Guidelines 2/2018 confirm they cannot be used for systematic
transfers.

### Step 5: Transfer Impact Assessment (TIA)

A TIA is required for every transfer that does not rely solely on an adequacy decision.
Perform the six-step EDPB methodology from Recommendations 01/2020, incorporating the
CNIL Practical TIA Guide (January 2025).

**Trigger for TIA:**
- Transfers using SCCs, BCRs, ad hoc clauses, or derogations → TIA required
- Transfers using adequacy decisions → TIA not required (adequacy already assessed by
  Commission), but monitor adequacy decision status

#### TIA Step 1 — Know Your Transfer

Map the transfer with precision:
- **Data categories**: Enumerate specific categories and fields transferred
- **Data subjects**: Who — employees, customers, trial participants, minors?
- **Processing purpose**: What is the importer doing with the data?
- **Volume**: Approximate number of records per transfer cycle
- **Transfer frequency**: One-time, daily batch, real-time streaming?
- **Data importer identity**: Full legal name, jurisdiction of incorporation, group structure
- **Storage location**: Where does the data physically reside after transfer?
- **Sub-processors / onward transfers**: Does the importer transfer the data onwards?

#### TIA Step 2 — Verify the Transfer Tool

Confirm the transfer mechanism to be relied upon is valid and correctly implemented:
- For SCCs: Verify module selection, execution, Annex I completion, and currency (using
  2021 SCCs, not the invalidated 2001/2004 versions)
- For BCRs: Verify current approval status, coverage of the importer entity, and 2024 update
- For derogations: Confirm the derogation's narrow conditions are genuinely met

#### TIA Step 3 — Assess the Third-Country Legal Framework

This is the substantive core of the TIA. Evaluate the destination country's legal system
to determine whether it provides essential equivalence.

**Assessment criteria (per EDPB Rec. 01/2020 and CNIL TIA Guide):**

| Criterion | Assessment Questions |
|-----------|---------------------|
| **Data protection law** | Does the country have a comprehensive data protection law? Is it enforced? Does it apply to the importer? |
| **Government access — surveillance law** | What laws allow government authorities to compel access to data? Are they proportionate? Subject to independent oversight? |
| **Judicial redress** | Can data subjects obtain effective redress against government access? Is there an independent court or authority with binding powers? |
| **Rule of law** | Is there an independent judiciary? Does the government respect court orders? |
| **Practical application** | Beyond the text of the law, is there evidence of broad/disproportionate access in practice? Published government reports, court decisions, academic analysis? |

**Country-specific legal surveys:**

##### US Surveillance Law Analysis

The US requires detailed TIA analysis because: (i) the EU-US DPF applies only to certified
organisations; (ii) the Trump administration's Jan 2025 firing of PCLOB members creates
uncertainty about the DPF redress mechanism; and (iii) FISA 702 and EO 12333 provide broad
surveillance authority.

**Key US surveillance laws:**

| Law | Scope | Key Points for TIA |
|-----|-------|-------------------|
| **FISA Section 702** (50 U.S.C. § 1881a) | Compels disclosure of non-US persons' data held by electronic communication service providers for foreign intelligence | Applies to US-based cloud providers, telecoms, and large tech platforms; no probable cause requirement; secret FISC court |
| **Executive Order 12333** | Authorises collection of intelligence outside the US | Does not compel US companies directly, but authorises NSA/CIA bulk collection from foreign infrastructure; no judicial oversight |
| **CLOUD Act** (18 U.S.C. § 2523) | Allows US government to compel US providers to disclose data regardless of storage location | Criminal investigations only; requires court-approved warrant; cannot be used for national security/intelligence purposes |

**EU-US Data Privacy Framework (DPF) — Current Status (March 2026):**
- The Commission adopted the DPF adequacy decision on 10 July 2023
- DPF certified organisations: data transferred to them does not require SCCs or TIA
- **Risk factors as of March 2026**:
  - Trump administration terminated all three Democratic PCLOB members (January 2025),
    leaving PCLOB without a quorum — undermining the independence of the redress mechanism
  - Schrems/NOYB has filed legal challenges (Schrems III proceedings) [VERIFY current status]
  - EO 14086 (October 2022) and the Data Protection Review Court (DPRC) remain in place,
    but independence is questioned without a functional PCLOB
  - EDPB issued first DPF review report (November 2024) noting concerns

**TIA conclusion for US transfers:**
- Transfers to **DPF-certified organisations**: Currently LAWFUL under adequacy decision,
  but flag the PCLOB risk and monitor for changes
- Transfers to **non-DPF-certified organisations**: Full TIA required; FISA 702 exposure is
  material; supplementary technical measures (end-to-end encryption with EU key control) may
  be needed to achieve essential equivalence; document risk openly
- Transfers to **non-DPF-certified organisations processing large-scale or special-category
  data**: HIGH RISK — Meta (€1.2B, 2023) and Uber (€290M, 2024) cases demonstrate that
  SCCs + supplementary measures may not be sufficient without exporter key control

##### China Surveillance Law Analysis

| Law | Scope | Key TIA Risk |
|-----|-------|-------------|
| **Personal Information Protection Law (PIPL)** (effective Nov 2021) | Comprehensive data protection with transfer restrictions | Art. 38-43 require CAC standard contracts, PIIA, or certification for China exports |
| **Multi-Level Protection Scheme (MLPS) / Cybersecurity Law** (2017) | Security review of "important data" and "critical information infrastructure" | Data held in China by operators may be subject to government inspection |
| **National Intelligence Law** (2017, Art. 7) | Requires any Chinese organisation/citizen to "support, assist, and cooperate" with state intelligence work | No judicial oversight; no published limits; broad in text |
| **Data Security Law** (2021) | "Important data" must be stored in China; export requires CAC security assessment | Government can require data localisation for "national security" data |

**TIA conclusion for China transfers:**
- **HIGH RISK** — China transfers typically cannot achieve essential equivalence without
  very strong technical measures (EU-controlled encryption, splitting of re-identifiable
  data) and even then may be RESTRICTED or UNLAWFUL for special-category data
- TikTok €530M fine (May 2025) — DPC fined TikTok for transferring EEA user data to China
  without adequate safeguards; corrective order to remediate within six months [VERIFY]
- Best practice: perform PIIA (Personal Information Protection Impact Assessment) in
  parallel for any data received in China under PIPL

##### India Transfers Analysis

| Law | Status | TIA Relevance |
|-----|--------|--------------|
| **Digital Personal Data Protection Act (DPDP)** (2023) | Enacted Aug 2023; rules pending (as of March 2026) | India→outbound transfers may be restricted by Data Protection Board if India restricts; EU→India transfers still require EU transfer mechanism |
| **Information Technology Act** (2000) + Rules | Legacy framework, still operative | Section 43A: compensation for negligent data protection; Rules 2011: reasonable security practices |

**TIA conclusion for India transfers:**
- India does not have EU adequacy decision
- SCCs + TIA required
- TIA risk: moderate — India IT Act provides some protections; government access powers exist
  but more limited than China; surveillance law less expansive than FISA 702 in practice
- Monitor DPDP rules for transfer restrictions [VERIFY]

##### Other High-Risk Jurisdictions

For destinations not covered above, conduct the following third-country survey:

1. **Does the country have a comprehensive data protection law?** (Y/N — if N: higher risk)
2. **Has the country signed/ratified Convention 108+ or the Budapest Convention?** (indicates
   rule-of-law baseline)
3. **What surveillance/access laws apply?** (identify by country — search for intelligence
   service powers, compelled disclosure laws, national security exceptions)
4. **Is there independent judicial oversight of government access?** (Y/N — if N: higher risk)
5. **Are data subjects able to obtain effective redress?** (Y/N — if N: higher risk)
6. **What does the Bertelsmann / IAPP / Privacy International country risk rating show?** [VERIFY]
7. **Any recent enforcement actions or court findings on this country's data protection?**

Score each criterion and produce a country risk rating: LOW / MEDIUM / HIGH / CRITICAL.

#### TIA Step 4 — Identify and Adopt Supplementary Measures

If Step 3 reveals the destination country does not provide essential equivalence, identify
whether supplementary measures can bridge the gap. See **Supplementary Measures Catalogue**
(Section below) for the full assessment.

Key principle from EDPB: supplementary measures must be **effective** — not merely
documented. If no effective measure can bridge the gap, the transfer must not proceed.

#### TIA Step 5 — Procedural Steps if No Measures Found

If effective supplementary measures cannot be identified:
- **Suspend the transfer** — the transfer must not proceed
- **Notify the supervisory authority** if required (varies by Member State; some require
  proactive notification; others allow post-suspension notification)
- **Suspend the contract** with the importer if the contract requires the transfer
- **Explore data localisation** or an alternative data importer in an adequate jurisdiction
- Document the decision and its rationale in the TIA record

**⟁ CLARIFY** — Before recommending suspension: "Before I recommend suspension, confirm:
Is there an alternative data importer in an adequate country or EEA? Is data localisation
technically feasible? The business impact of suspension may be significant — I want to
ensure all alternatives are explored."

#### TIA Step 6 — Reassess at Appropriate Intervals

- TIAs are not one-time documents — they must be reviewed when:
  - The destination country's legal framework changes materially
  - The transfer volume, data categories, or importer changes
  - The transfer mechanism is challenged (e.g., adequacy decision reviewed/invalidated)
  - Regulatory guidance or enforcement action changes the risk profile
  - On a scheduled basis (recommended: annually for high-risk destinations, every two years
    for low-risk)

Document the reassessment trigger and date in the TIA record.

### Step 6: Supplementary Measures Assessment

Where the TIA reveals risk, assess whether supplementary measures can achieve essential
equivalence. Apply the EDPB Recommendations 01/2020 (v2.0) and EDPB Guidelines 01/2025
on Pseudonymisation.

#### Technical Measures

| Measure | Conditions for Effectiveness | When Effective | Limitations |
|---------|------------------------------|---------------|-------------|
| **End-to-end encryption** | State-of-the-art encryption; key management exclusively in EEA; importer never holds plaintext | Effective where importer only stores/transmits encrypted data without needing to access it | Not effective where importer must access plaintext to perform the processing |
| **Pseudonymisation (EDPB Guidelines 01/2025)** | EEA entity retains additional information (key); pseudonymised data sent without key; re-identification not possible by importer or foreign authorities | Effective where importer processes pseudonymised data without needing re-identification | Not effective if importer needs the actual personal data to perform its function |
| **Split / dual-server processing** | Processing split between EEA and third-country servers; re-identifiable data stays in EEA; third-country server processes only aggregate or non-identifiable data | Effective for analytics and AI training use cases that can be architecturally split | Requires system re-architecture; not applicable to all processing purposes |
| **Anonymisation** | True anonymisation meeting the Breyer test (EU Court, C-582/14) — no reasonable means of re-identification | Effective — anonymised data is not personal data; Chapter V does not apply | High bar — must be truly irreversible; pseudonymisation is not anonymisation |
| **Homomorphic encryption / secure computation** | Processing occurs on encrypted data without decryption | Effective in principle — importer cannot access plaintext | Computationally expensive; limited to specific processing types |

**Key test for technical measure effectiveness**: Would the measure remain effective even
if the data importer were compelled by the third-country government to disclose data?
- If the importer holds the keys → no, measure is not effective against state-compelled disclosure
- If the EEA exporter holds the keys → yes, effective even against a court order to the importer

#### Organisational Measures

| Measure | Effectiveness | Notes |
|---------|--------------|-------|
| **Government access transparency** | Supplementary — not standalone | Importer commits to notify exporter of government requests and challenge them where possible; cannot override a legal compulsion order |
| **Contractual challenge obligation** | Supplementary — not standalone | Importer must challenge government access requests; maximises chances of proportionality review; but cannot guarantee success |
| **Minimisation protocols** | Always apply | Transfer only the minimum data necessary; reduces exposure surface |
| **Retention limits** | Always apply | Shortest retention period feasible; reduces the window of vulnerability |
| **Regular audits** | Supplementary | Exporter audit rights over importer's security and access records |
| **Employee access controls** | Supplementary | Restrict importer employee access to personal data to need-to-know basis; documented access logging |

#### Contractual Measures

| Measure | Content | Effectiveness |
|---------|---------|--------------|
| **Enhanced SCCs** | Adding additional protections in Annex II (TOMs) or via additional clauses | Effective where they impose real obligations; not effective if they are generic boilerplate |
| **Sub-processor restrictions** | Limiting the importer's ability to onward transfer | Essential — without onward transfer restriction, the TIA only covers the first hop |
| **Government request notification clause** | Importer must notify exporter of any government access request to the extent legally permitted | Supplementary — cannot override legal prohibition on notification (e.g., FISA 702 gag orders) |
| **Data deletion on government request** | Importer must delete data rather than comply with an unlawful order | Contractual — effectiveness depends on importer's practical ability to comply |
| **Right to audit** | Exporter has right to audit importer's compliance | Operational value; does not prevent illegal access by third-country authorities |

#### Supplementary Measures Decision Matrix

| TIA Risk Level | Data Sensitivity | Recommended Supplementary Measures | Classification |
|----------------|-----------------|-----------------------------------|----------------|
| LOW (e.g., rule-of-law country, limited surveillance) | Ordinary | Standard SCCs + TOMs | LAWFUL |
| MEDIUM (e.g., broad but judicially supervised surveillance) | Ordinary | SCCs + enhanced TOMs + notification clause | LAWFUL with conditions |
| MEDIUM | Special category | SCCs + strong encryption (EU key control) + minimisation | RESTRICTED — conditional on measure effectiveness |
| HIGH (e.g., FISA 702 exposure, no judicial oversight) | Ordinary | SCCs + EU-controlled encryption + pseudonymisation | RESTRICTED — requires technical architecture verification |
| HIGH | Special category | EU-controlled encryption + split processing OR suspend | RESTRICTED → UNLAWFUL if technical measures not feasible |
| CRITICAL (e.g., China, broad state access laws) | Any | EU-controlled encryption + no importer plaintext access OR suspend | UNLAWFUL if importer needs plaintext access |

### Step 7: UK GDPR Parallel Analysis

If the transfer is also regulated by UK GDPR, perform a parallel analysis:

**UK adequacy assessment:**
- Confirm whether the destination country is on the UK's adequacy list (separate from EU list)
- EU-UK: the UK has adequacy from the EU side; EU → UK transfers are permitted under EU
  adequacy decision (with ongoing review)
- UK → third countries: UK maintains separate adequacy regulations

**UK transfer tool selection:**
- If destination lacks UK adequacy: use IDTA or UK Addendum to EU SCCs
- Both the IDTA and UK Addendum require a Transfer Risk Assessment (TRA) — the UK equivalent
  of a TIA, with a three-part test: (1) destination country assessment, (2) exporter assessment,
  (3) importer assessment
- ICO's 2026 updated guidance introduces a proportionality-based approach to TRA [VERIFY ICO
  2026 guidance details]

**UK BCRs:**
- UK BCRs (approved by ICO) are required for transfers within multinational groups subject to
  UK GDPR; EU BCR approval does not automatically cover UK-regulated transfers

**Key UK divergence points:**
- The UK does not apply the EDPB's six-step TIA methodology (it uses a TRA approach)
- The UK Addendum modifies specific clauses (e.g., liability cap, supervisory authority,
  jurisdiction for disputes)
- The UK GDPR definition of "transfer" may diverge from EDPB interpretation over time
- The Data Use and Access Act (UK, expected 2026) may amend transfer rules [VERIFY]

### Step 8: Swiss nDSG Parallel Analysis

If the transfer is regulated by Swiss DPA (nDSG, effective 1 September 2023):

**FDPIC adequacy list:**
- Transfers to countries on the FDPIC adequacy list are permitted without further safeguards
- The list largely mirrors EU adequacy but with some differences [VERIFY FDPIC list]
- EU Member States are adequate for Swiss purposes

**Swiss transfer tools:**
- For non-adequate countries: use EU SCCs with the Swiss Addendum/Annex, OR bilateral Swiss
  standard data protection clauses
- BCRs approved under EU GDPR may be recognised — FDPIC notification may be required
- FDPIC guidance on TIAs largely follows EDPB recommendations [VERIFY]

**Swiss-specific notes:**
- The FDPIC has stronger enforcement powers under nDSG compared to old FADP
- Swiss data subjects have rights similar to GDPR Art. 15-22
- Cross-border transfer documentation should reference nDSG Art. 16-17 in parallel with GDPR

### Step 9: Classify Each Transfer

Classify each transfer using the three-tier system after completing Steps 4-8:

#### LAWFUL

The transfer is authorised by a valid mechanism that provides essential equivalence.

**Conditions (all must be met):**
- A valid transfer mechanism is in place and properly implemented
- For SCCs: all Annexes complete, module correct, executed
- TIA completed (where required) and no material unmitigated risk identified
- Supplementary measures (if required) are effective and implemented
- Periodic review scheduled

**Action:** Document the mechanism and TIA outcome. Set review calendar reminder.

#### RESTRICTED

The transfer has a valid mechanism, but unresolved risk factors require monitoring,
additional safeguards, or imminent remediation.

**Conditions (any may apply):**
- Valid mechanism in place, but TIA reveals residual risk not fully mitigated
- Adequacy decision in place but subject to legal challenge or Commission review
- SCCs used, but technical supplementary measures not yet fully implemented
- BCR update obligation not yet satisfied
- Transfer continues pending renegotiation or alternative arrangement

**Action:** Document the restriction. Assign a responsible owner. Set a remediation
deadline (typically 30-90 days for material restrictions). Escalate to DPO and business
stakeholder.

#### UNLAWFUL

The transfer lacks a valid mechanism, or the TIA reveals that essential equivalence cannot
be achieved even with supplementary measures.

**Conditions (any may apply):**
- No valid transfer mechanism in place
- Transfer relies on invalidated mechanism (pre-2021 SCCs without conversion)
- Art. 49 derogation relied upon for systematic transfers (non-compliant by definition)
- TIA reveals that the destination country's surveillance laws prevent essential equivalence,
  and no effective supplementary measures can address this (importer must access plaintext;
  government access is unconstrained)
- Supplementary measures are nominal/paper-only and not actually implemented

**Action:** Suspend the transfer immediately (or set a suspension deadline if not
immediately possible). Notify the DPO. Consider supervisory authority notification.
Document the suspension decision with full rationale.

### Step 10: Remediation Plan

For every RESTRICTED or UNLAWFUL transfer, produce a structured remediation plan:

```
Transfer: [ID and description]
Classification: RESTRICTED / UNLAWFUL
Root cause: [Description of the gap or risk]
Remediation owner: [Name / role]
Deadline: [Date — typically 30 days for UNLAWFUL; 60-90 days for RESTRICTED]

Actions required:
1. [Specific action, e.g., "Execute 2021 SCCs Module 2 with Vendor X"]
2. [Specific action, e.g., "Implement EU-controlled encryption for data at rest and in transit"]
3. [Specific action, e.g., "Complete TIA documentation and file in transfer record"]
4. [Specific action, e.g., "Update RoPA entry for this transfer"]
5. [Specific action, e.g., "Notify supervisory authority of suspension — [SA name and form]"]

Verification: How will completion be verified?
[e.g., "DPO to confirm SCC execution and encryption implementation before transfer resumes"]
```

### Step 11: Documentation and Output

**Required documentation package:**

1. **Transfer Record (per transfer)**:
   - Transfer ID, description, parties, data categories, purpose, volume, frequency
   - Transfer mechanism relied upon
   - TIA conclusion (brief summary + reference to full TIA)
   - Supplementary measures (if any)
   - Classification: LAWFUL / RESTRICTED / UNLAWFUL
   - Next review date

2. **Full TIA Document** (per transfer where required):
   - Steps 1-6 completed with evidence
   - Country risk assessment (law text references, regulator reports, enforcement data)
   - Supplementary measures analysis
   - Conclusion on essential equivalence

3. **RoPA Update**:
   - Cross-border transfer column updated with mechanism, destination, and TIA status

4. **DPA/SCC Schedule Update** (if applicable):
   - Annex I and II of the SCCs / IDTA completed and accurate

5. **Glass Box Audit Trail** (see template below)

---

## Transfer Mechanism Reference Checklists

### SCCs (2021 EU) Execution Checklist

- [ ] Correct module identified based on party roles
- [ ] Governing law clause in main contract does not conflict with SCCs
- [ ] SCCs signed or agreed electronically with equal authority to main contract
- [ ] Annex I(A): All required fields completed (data exporter, importer, description of
  transfer, categories of data subjects, categories of personal data, sensitive data,
  frequency, nature of processing, purposes, retention periods, onward transfer)
- [ ] Annex I(B): Competent supervisory authority identified (exporter's lead SA)
- [ ] Annex I(C): Local representative identified if applicable
- [ ] Annex II: TOMs are specific, current, and reflect actual security practices (not generic)
- [ ] Annex III (Module 2/3): Sub-processor list complete with names, countries, and processing
  descriptions
- [ ] Clause 14 (Local Law Assessment): TIA referenced and completed
- [ ] Docking clause: completed if multiple data importers or exporters

### IDTA (UK) Execution Checklist

- [ ] Table 1: Parties (exporter and importer details)
- [ ] Table 2: Transfer details (description, categories, data subjects, purposes, retention)
- [ ] Table 3: Technical/organisational security measures
- [ ] Table 4: Additional clauses (if any)
- [ ] Transfer Risk Assessment (TRA) completed and documented
- [ ] IDTA executed alongside or as part of the main contract

### BCR Compliance Checklist

- [ ] BCRs cover all entities involved in the transfer
- [ ] BCRs are approved by the Lead SA (no material lapses since approval)
- [ ] 2024 update requirements incorporated (Schrems II TIA documentation, expanded audit
  programme, third-party beneficiary rights)
- [ ] Annual update submitted on time
- [ ] Internal training on BCR obligations conducted
- [ ] Complaints mechanism available and operational for data subjects

---

## Risk Classification Framework

### LAWFUL — No Material Gap

All of the following apply:
- Valid transfer mechanism in place and correctly implemented
- TIA completed (where required) and essential equivalence confirmed or adequacy applies
- Supplementary measures implemented where required by TIA
- Documentation complete and current
- Review schedule set

### RESTRICTED — Monitor and Remediate

One or more of the following apply:
- Valid mechanism but TIA reveals residual risk requiring monitoring or enhancement
- Adequacy decision under review/challenge — status uncertain
- Mechanism documentation incomplete but mechanism itself valid
- Supplementary measures partially implemented
- BCR update obligation pending

### UNLAWFUL — Suspend and Remediate

One or more of the following apply:
- No valid transfer mechanism
- Mechanism invalidated or expired
- TIA reveals lack of essential equivalence with no effective supplementary measures
- Art. 49 derogation misapplied (systematic transfers)
- Transfer suspended pending regulatory authority review

---

## Prioritisation Framework

When multiple transfers are assessed simultaneously, prioritise by:

### Priority 1 — Critical (Act within 24-48 hours)

- UNLAWFUL transfer of special-category data, children's data, or large-scale ordinary data
  currently in progress with no mechanism at all
- Transfer to jurisdiction where government access confirmed in practice (not just law)
- Transfer already under supervisory authority investigation

### Priority 2 — High (Act within 30 days)

- UNLAWFUL transfer of ordinary data (limited volume) — needs mechanism urgently
- RESTRICTED transfer of special-category data — supplementary measures gap
- BCRs without 2024 Schrems II update applied
- Pre-2021 SCCs still in use without conversion

### Priority 3 — Medium (Act within 60-90 days)

- RESTRICTED transfers pending mechanism renegotiation
- TIA documentation incomplete for otherwise valid transfer
- Onward transfer restrictions missing from SCC Annex III
- DPF-reliant transfers without DPF certification monitoring

### Priority 4 — Low (Act at next review cycle)

- Minor documentation gaps (e.g., Annex I fields incomplete, non-material)
- TIA review overdue by less than 6 months for low-risk destination
- BCR coverage gaps for new entities added to the group (minor)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivering if any gate fails.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim about GDPR, UK GDPR, Swiss DPA, or surveillance law cites a specific article, decision, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | Citations follow a consistent, recognisable format (GDPR Art. 45(1), C-311/18, Commission Decision 2021/914, ICO IDTA 2022) | Fix format |
| **Currency** | Every cited provision, adequacy decision, and regulatory guidance checked for amendments, repeal, or superseding instrument | Flag "[CHECK CURRENCY — may have changed]" |
| **Domain** | Analysis stays within the applicable regime (EU GDPR, UK GDPR, Swiss nDSG) — no bleed of one regime's rules into another's analysis without explicit cross-reference | Remove or flag as jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden — especially for DPF status, evolving enforcement guidance, and pending legal challenges | Add explicit confidence qualifier |

### Self-Interrogation for UNLAWFUL Classifications

For any transfer classified as UNLAWFUL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**
- Does the UNLAWFUL classification follow from a specific legal gap (no mechanism, invalidated
  mechanism, TIA failure)?
- Would a supervisory authority reviewing this transfer reach the same conclusion?
- Is there a supplementary measure that has been overlooked?

**Pass 2 — Completeness**
- Have all available transfer mechanisms been considered (adequacy — EU, UK, Swiss separately;
  SCCs with all modules; BCRs; derogations)?
- Has the TIA considered the actual practice in the destination country, not just the law on paper?
- Have all supplementary measures been evaluated, including technical architecture options?

**Pass 3 — Challenge**
- What is the strongest argument that this transfer could be made LAWFUL?
- Under what circumstances would an experienced privacy counsel accept the transfer?
- Is the UNLAWFUL classification proportionate, or could this be RESTRICTED with a clear
  remediation path?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled law/enforcement — e.g., pre-2021 SCCs are clearly invalid | State with confidence |
| **High** | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good arguments but developing law or pending review | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain — e.g., DPF legal status, novel transfer scenarios | Flag for counsel review with both sides of argument |
| **Unlikely** | 0.0-0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every assessment output MUST include a Glass Box audit trail:

```yaml
glass_box:
  assessment_id: "[unique ID — e.g., TIA-2026-001]"
  date: "[assessment date]"
  assessor: "AI-assisted — requires qualified DPO/privacy counsel review"

  transfers_assessed:
    - transfer_id: "[ID]"
      description: "[source entity → destination entity, country]"
      data_categories: "[list]"
      mechanism: "[adequacy / SCCs Module X / BCRs / Art. 49 derogation]"
      tia_required: "Yes / No"
      tia_completed: "Yes / No / Partial"
      supplementary_measures: "[list or 'None required']"
      classification: "LAWFUL / RESTRICTED / UNLAWFUL"
      confidence: "HIGH / MEDIUM / LOW"
      self_interrogation: "PASS / REVISED / N/A (no UNLAWFUL)"
      next_review: "[date]"

  regimes_applied:
    - "EU GDPR Chapter V"
    - "UK GDPR + DPA 2018" (if applicable)
    - "Swiss nDSG" (if applicable)

  adequacy_decisions_checked: "[number checked]"
  tias_performed: "[number]"
  transfers_lawful: "[number]"
  transfers_restricted: "[number]"
  transfers_unlawful: "[number]"

  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"

  key_references_used:
    - "GDPR Art. 44-49 [VERIFIED / UNVERIFIED]"
    - "EDPB Recommendations 01/2020 on supplementary measures v2.0 [VERIFIED / UNVERIFIED]"
    - "Commission Decision 2021/914 (2021 SCCs) [VERIFIED / UNVERIFIED]"
    - "Schrems II, C-311/18, CJEU 16 July 2020 [VERIFIED / UNVERIFIED]"
    - "EU-US DPF Adequacy Decision 2023 [VERIFIED / UNVERIFIED]"
    - "[Other references used]"

  limitations:
    - "[Any scope limitations — e.g., assessment based on information provided; actual
       transfer may differ]"
    - "[Any legal developments after March 2026 should be verified against current sources]"
    - "[DPF status as of March 2026: under challenge — legal team to monitor]"

  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when assessing cross-border data transfers:

1. **Treating adequacy decisions as permanent** — Adequacy decisions expire, get reviewed,
   and can be invalidated (Privacy Shield: 2020, Safe Harbor: 2015). Set monitoring alerts;
   never assume adequacy will persist indefinitely.

2. **Using pre-2021 SCCs for new transfers** — The 2001/2004 SCCs are no longer valid for
   new transfers. Ensure all new contracts use the 2021 Commission Decision 2021/914 SCCs.
   Old contracts must have been migrated by 27 December 2022.

3. **Skipping the TIA because SCCs are "standard"** — SCCs are contractual protections
   between the parties; they do not and cannot override the destination country's surveillance
   laws. Schrems II mandates a TIA for every SCC-based transfer to assess whether the legal
   framework undermines the SCC protections.

4. **Nominal supplementary measures** — Listing "encryption" in Annex II without specifying
   who controls the encryption keys. If the importer controls the keys, encryption does not
   protect against state-compelled disclosure and is not an effective supplementary measure.

5. **Conflating DPF adequacy with general US adequacy** — The EU-US DPF only covers
   organisations that are DPF-certified. A transfer to a non-certified US company still
   requires SCCs + full TIA. Do not assume US adequacy in the absence of DPF certification.

6. **Ignoring the PCLOB risk to DPF** — As of March 2026, the Trump administration's firing
   of PCLOB members has undermined the DPF redress mechanism's independence. DPF-reliant
   organisations should monitor Schrems III proceedings and maintain SCC documentation as
   a fallback.

7. **Using Art. 49 derogations for systematic transfers** — EDPB Guidelines 2/2018 are
   explicit: Art. 49 derogations are for exceptional, non-repetitive situations. Systematic
   use of consent or contractual necessity derogations for routine business transfers is
   non-compliant and will attract enforcement.

8. **Module selection errors in SCCs** — Using Module 2 (controller-to-processor) for a
   situation where the importer is actually a controller. The wrong module means the SCCs
   do not reflect the actual legal relationship and may not be enforceable.

9. **Incomplete Annex I** — Leaving Annex I fields vague or incomplete ("various personal
   data categories" without specification). Regulators can void SCCs with inadequate Annex I
   as insufficiently specific to bind the parties.

10. **Not covering onward transfers** — Assessing the first hop (exporter → importer) but
    not the onward transfers (importer → sub-processor in a fourth country). Clause 8.7/8.8
    of the 2021 SCCs require the importer to impose equivalent obligations on sub-processors.

11. **BCRs without the 2024 Schrems II update** — All BCR holders were required to update
    their BCRs in 2024. Organisations that have not completed this update are operating on
    non-compliant BCRs.

12. **Failing to distinguish UK and EU transfer regimes** — Post-Brexit, EU → UK transfers
    rely on the EU's UK adequacy decision; UK → third-country transfers rely on UK law
    (IDTA, UK Addendum, UK adequacy regulations). Applying EU GDPR SCCs to UK-only outbound
    transfers without the UK Addendum creates a validity gap.

13. **Treating pseudonymisation alone as a sufficient technical measure** — Pseudonymisation
    is only effective as a supplementary measure if the EEA exporter retains the
    re-identification key and the importer never has access to the additional information
    (EDPB Guidelines 01/2025). If the importer can re-identify, pseudonymisation fails.

14. **Ignoring sector-specific restrictions** — Some sectors impose stricter rules than
    GDPR Chapter V alone (healthcare data under country-specific health laws; financial data
    under EBA guidance; employee data with works council approval requirements). Always check
    for sector overlays.

15. **Not documenting the TIA** — Performing an informal mental assessment of the destination
    country without a written TIA record. Supervisory authorities (DPC, CNIL, AEPD, ICO) have
    made clear they expect written TIA documentation when SCCs are used — particularly since
    Meta (€1.2B, May 2023) and Uber (€290M, 2024) demonstrated that inadequate TIA
    documentation is a primary enforcement target.

16. **Static transfer registers** — Maintaining a one-time transfer assessment in the RoPA
    that is never updated. Transfers evolve: importers change sub-processors, destination
    countries change their laws, adequacy decisions get reviewed. TIAs must be living
    documents with scheduled reassessment dates.

17. **Assuming CLOUD Act applies to all US transfers** — The CLOUD Act applies only to
    criminal investigations; it does not authorise national security / intelligence access.
    FISA 702 and EO 12333 are the primary TIA concerns for US intelligence exposure; CLOUD
    Act is a more limited, judicially supervised instrument.

---

## Writing Standards

Apply plain-language discipline to all assessment outputs:

**For TIA conclusions and classifications:**
- Plain language — avoid GDPR jargon without explanation
- Active voice: "The transfer lacks a valid mechanism" not "A valid mechanism has not been
  identified for the transfer"
- Specific, not vague: name the article, decision, and specific gap — not "compliance issues exist"
- Actionable: every RESTRICTED and UNLAWFUL classification must have a clear next action

**Quality gates before delivery:**
1. Can the DPO and business stakeholder both understand the summary findings?
2. Does every UNLAWFUL/RESTRICTED classification have a specific root cause and a named owner?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are confidence levels assigned for all material findings?
5. Is the Glass Box audit trail complete?
6. Has the Self-Interrogation been completed for every UNLAWFUL classification?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**
- Search for current adequacy decision status (destination country-specific)
- Retrieve current text of GDPR Art. 44-49, UK GDPR equivalent provisions, Swiss nDSG
- Search for regulatory guidance: EDPB recommendations, ICO guidance, FDPIC guidance
- Find enforcement decisions on cross-border transfer violations (by country and mechanism)
- Verify surveillance law text for the destination country
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all adequacy decision references with [VERIFY]
- Mark all surveillance law analysis with [VERIFY — verify against current country legal sources]
- Mark DPF status analysis with [VERIFY — status may have changed]
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require independent verification"`
- Focus the assessment on structural and mechanism analysis rather than country-specific legal
  certainty; provide more conservative risk ratings where legal analysis cannot be verified

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Cross-Border Transfer Assessment

**Assessment ID**: [e.g., TIA-2026-001]
**Organisation**: [if provided]
**Date of Assessment**: [date]
**Regimes Applied**: EU GDPR Chapter V [/ UK GDPR] [/ Swiss nDSG]
**Assessor**: AI-assisted — requires qualified DPO/privacy counsel review

---

## Executive Summary

[2-3 paragraphs: total transfers assessed, summary of findings, key risks, recommended
immediate actions]

**Overall Risk Profile**: LOW / MEDIUM / HIGH / CRITICAL

---

## Transfer Inventory

| Transfer # | From → To | Country | Data Categories | Mechanism | TIA Required | Classification |
|------------|-----------|---------|----------------|-----------|-------------|----------------|
| 1 | [Entity A → Entity B] | [Country] | [Categories] | [SCCs M2] | Yes | LAWFUL |
| 2 | [Entity A → Entity C] | [Country] | [Categories] | [None] | N/A | UNLAWFUL |

---

## Transfer-by-Transfer Analysis

### Transfer #1 — [From → To, Country] — [LAWFUL / RESTRICTED / UNLAWFUL]

**Mechanism**: [e.g., 2021 EU SCCs Module 2 executed on [date]]
**TIA Status**: [e.g., Completed — see TIA record #TIA-001-2026]
**Supplementary Measures**: [e.g., End-to-end encryption with EU-controlled key management]
**Key findings**: [Specific findings]
**Risk classification**: LAWFUL — Confidence: HIGH
**Actions required**: [None / List]
**Next review date**: [Date]

---

## Remediation Plan

### Priority 1 — Critical (Act within 48 hours)
[Item, owner, deadline, verification method]

### Priority 2 — High (Act within 30 days)
[Item, owner, deadline, verification method]

### Priority 3 — Medium (Act within 60-90 days)
[Item, owner, deadline, verification method]

---

## Documentation Checklist

- [ ] TIA records completed for each SCC/BCR/derogation transfer
- [ ] RoPA updated with transfer mechanism and TIA status
- [ ] SCC/IDTA/BCR documentation executed and filed
- [ ] Supplementary measures implemented and verified
- [ ] Review calendar reminders set
- [ ] DPO sign-off obtained

---

## Glass Box Audit Trail

[Insert completed Glass Box YAML block]
```

---

## Localization Notes

This skill uses EU GDPR as its primary reference with parallel UK GDPR and Swiss nDSG
tracks. When the transfer involves only one regime, the other tracks can be skipped.

**For EU-only transfers:**
- Omit UK GDPR Step 7 and Swiss nDSG Step 8
- Reference only the EU adequacy list and EU SCCs

**For UK-only transfers (no EU GDPR involvement):**
- Use IDTA (not EU SCCs) as the primary transfer tool
- Reference ICO adequacy regulations (not EU Commission decisions)
- Apply TRA methodology (not EDPB six-step TIA) per ICO guidance
- Reference UK DPA 2018 Part 3 Chapter 5, not GDPR Chapter V directly

**For Swiss-only transfers (no EU GDPR involvement):**
- Reference FDPIC adequacy list
- Apply nDSG Art. 16-17
- EU SCCs may be adapted with Swiss annexes per FDPIC guidance

---

## Provenance

Created by Legalcode as a new original skill (2026-03-01). Synthesised from:
- GDPR Chapter V (Art. 44-49)
- EDPB Recommendations 01/2020 on supplementary measures (v2.0, June 2021)
- EDPB Guidelines 01/2025 on Pseudonymisation (January 2025)
- CNIL Practical Guide on Transfer Impact Assessments (January 2025)
- Commission Decision 2021/914 (EU SCCs)
- CJEU, Schrems II (C-311/18, 16 July 2020)
- EU-US Data Privacy Framework Adequacy Decision (10 July 2023)
- EDPB Report on First Review of EU-US DPF (November 2024)
- ICO International Data Transfer Agreement and Guidance
- Swiss Federal Act on Data Protection (nDSG), effective 1 September 2023
- EDPB BCR recommendations (2022/2023 with 2024 update requirements)
- Enforcement landscape: Meta (€1.2B, May 2023), Uber (€290M, 2024), TikTok (€530M, May 2025)
- Best practices from legalcode repository: `legalcode-contract-review` (quality framework
  patterns), `legalcode-dpia-generator` (jurisdiction-agnostic compliance structure),
  `legalcode-dsar-workflow-builder` (multi-regime parallel analysis pattern)

All legal references require independent verification against current authoritative sources.
Laws, regulatory guidance, and enforcement posture change — verify currency before relying
on any conclusion. This skill is not legal advice.
