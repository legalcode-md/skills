---
name: legalcode-data-mapping-workflow
description: Conduct end-to-end data mapping exercises to build Records of Processing Activities (RoPA)
  compliant with GDPR Article 30, CCPA/CPRA, LGPD, PIPEDA, and APPI. Use when creating or refreshing a
  privacy data inventory, onboarding a new DPO, preparing for a DPIA, responding to a regulator inquiry,
  conducting a vendor privacy audit, or building breach-response readiness.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conduct end-to-end data mapping exercises to build Records of Processing Activities (RoPA) compliant with GDPR Article 30, CCPA/CPRA, LGPD, PIPEDA, and APPI. Use when creating or refreshing a privacy data inventory, onboarding a new DPO, preparing for a DPIA, responding to a regulator inquiry, conducting a vendor privacy audit, or building breach-response readiness. Covers data inventory methodology (interviews, automated scanning, questionnaires), system-by-system data flow documentation, classification of personal data categories and special categories (GDPR Art. 9), legal basis mapping per processing activity, retention schedule alignment, third-party sharing and cross-border transfer identification, and completeness scoring. Produces machine-readable data maps (structured tables + YAML/JSON hooks) suitable for OneTrust, TrustArc, Privaci, and other privacy management platforms. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers; integrates with legalcode-dpia-generator, legalcode-dsar-workflow-builder, legalcode-cross-border-transfer-assessment, and legalcode-breach-severity-assessment.


# Legalcode Data Mapping Workflow

> **Disclaimer**: This skill provides a framework for AI-assisted data mapping and
> Records of Processing Activities (RoPA) creation. It does not constitute legal advice.
> All outputs should be reviewed by a qualified Data Protection Officer or privacy
> professional licensed or operating in the relevant jurisdiction before use as the
> organization's official RoPA. Privacy laws change and regulator guidance evolves;
> verify current applicability of every legal requirement and deadline described here.
> Legal references and regulatory citations from training data carry hallucination risk —
> verify against authoritative primary sources before relying on them. Mark any
> unverified citation with **[VERIFY]** before delivering to regulators or legal counsel.

---

## Purpose and Scope

This skill executes a complete, systematic data mapping workflow — from discovery
through to a production-quality Records of Processing Activities (RoPA) and data flow
documentation package. It is designed for privacy teams, Data Protection Officers,
compliance professionals, and legal operations teams who need a defensible, auditable
data map suitable for regulatory inspection and downstream privacy operations.

Data mapping occupies the **foundational position** in the compliance skill family. A
deficient data map cascades errors into every downstream workflow: DSARs cannot be
fulfilled accurately, DPIAs cannot be scoped correctly, transfer assessments cannot
identify all flows, and breach responses cannot calculate the scope of affected data.
Getting the data map right is the highest-leverage action in a privacy program.

**This skill covers:**

- Intake scoping and organizational boundary definition
- Stakeholder identification and structured interview facilitation
- Automated and questionnaire-based data discovery across system categories
- System-by-system and data-category data flow documentation
- Personal data classification (standard categories, special categories, criminal data)
- Legal basis mapping per processing activity (GDPR Art. 6 + Art. 9; equivalents)
- Necessity and proportionality screening
- Recipient identification (processors, joint controllers, third-party controllers)
- Data Processing Agreement (DPA) audit and gap identification
- Cross-border transfer flagging and transfer mechanism inventory
- Retention schedule alignment and deletion mechanics
- Automated decision-making and profiling detection
- Completeness scoring (GREEN / YELLOW / RED per processing activity)
- Machine-readable RoPA output (structured tables, YAML/JSON hooks for privacy platforms)
- Glass Box audit trail for regulator defensibility
- Integration handoffs to DPIA, DSAR, Transfer Assessment, and Breach Response workflows

**This skill does not:**

- Conduct Data Protection Impact Assessments — see `legalcode-dpia-generator`
- Execute or manage DSAR responses — see `legalcode-dsar-workflow-builder`
- Assess cross-border transfer lawfulness in depth — see `legalcode-cross-border-transfer-assessment`
- Assess breach notification obligations — see `legalcode-breach-severity-assessment`
- Draft or review privacy notices — see `legalcode-privacy-policy-drafter`
- Conduct legitimate interest assessments — see `legalcode-legitimate-interest-assessment`
- Provide legal advice or replace qualified DPO review
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The primary regime is determined in Step 2 based on
the organization's location, data subjects' residences, and applicable sectoral rules.

### Regime Overview

| Regime               | Primary Instrument                          | RoPA Requirement                                              | Key Distinctions                                                   |
| -------------------- | ------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------ |
| **EU GDPR**          | Art. 30 + EDPB guidance                     | Mandatory (250-employee exemption rarely applies in practice) | Most detailed; controller + processor records distinct             |
| **UK GDPR**          | UK GDPR Art. 30 + DPA 2018                  | Mandatory                                                     | Mirrors EU GDPR with post-Brexit divergences                       |
| **CCPA/CPRA**        | Cal. Civ. Code § 1798.100 + CPPA Regs       | De facto mandatory (privacy notice + data inventory required) | Consumer rights basis; "business purpose" vs. "commercial purpose" |
| **LGPD (Brazil)**    | LGPD Art. 37–41                             | Mandatory for controllers; guidance from ANPD [VERIFY]        | Similar to GDPR; ANPD may require specific RoPA format             |
| **PIPEDA (Canada)**  | Principle 1 (Accountability) + OPC guidance | Strongly recommended; audit basis                             | Accountability principle; OPC can require production               |
| **APPI (Japan)**     | APPI Art. 24 + PPC Rules                    | Required for certain processing; third-country transfers      | Updated 2022; specific third-country transfer documentation        |
| **PDPA (Singapore)** | PDPA 2012 + PDPC Advisory Guidelines        | Best practice; required for breach response                   | Advisory but practically mandatory for PDPC investigations         |
| **PDPA (Thailand)**  | PDPA 2019 + PDPC guidance                   | Mandatory [VERIFY]                                            | Article 39 RoPA requirement; enforcement beginning                 |

[JURISDICTION-SPECIFIC] Before finalizing the RoPA, localize:

- EU/EEA Member State-specific derogations for employees, research, public tasks
- UK DPA 2018 Schedule 2 + sector-specific codes (ICO Employment Practices, etc.)
- US sector overlay: HIPAA (health), GLBA (financial), FERPA (education), COPPA (children)
- CCPA/CPRA specifics: data category schema for privacy policy alignment; "sensitive personal information" vs. "personal information" distinctions
- Brazil ANPD guidance on RoPA format and submission requirements (evolving) [VERIFY]
- Canadian provincial laws: PIPEDA vs. substantially-similar (Québec Law 25, Alberta PIPA, BC PIPA) — Law 25 most stringent; RoPA mandatory [VERIFY current Law 25 status]
- APPI third-country transfer documentation requirements (post-2022 amendments)

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** prompts at seven decision points where the answer materially
changes the direction, scope, or output of the workflow. Do not proceed on assumptions at
marked points — pause and ask the user.

If the user has already provided the information, skip the question and proceed. For
batch or non-interactive execution, use the defaults indicated at each point and state
assumptions explicitly.

---

## Workflow

### Step 1: Accept Intake and Define Scope

Accept input in any of these formats:

- **Organization description**: Name, type, size, primary jurisdictions, known systems
- **System list**: Specific systems or processing activities to map (targeted engagement)
- **Existing RoPA draft**: A prior version to verify and refresh
- **Scope brief**: A description of what is (and what is not) in scope

If no input is provided, ask the user to supply one of the above.

**⟁ CLARIFY #1 — Organizational Scope**

Before beginning, confirm the scope of the mapping exercise:

1. **Mapping scope**: What is the organizational boundary?
   - Options: Entire organization (all entities, all jurisdictions), Single legal entity,
     Specific division or product line, Specific processing activity or data type
   - _Why this matters_: Entire-org mapping may take months and require phased rollout.
     Activity-specific mapping is a focused 1-3 week exercise. The scope determines
     which stakeholders to interview and which systems to assess.

2. **Trigger**: What is driving this mapping exercise?
   - Options: Initial RoPA creation, Annual refresh/update, New product/system launch,
     Regulatory inquiry or audit preparation, M&A due diligence, DPIA prerequisite,
     Breach response readiness review
   - _Why this matters_: Triggers with regulator deadlines require triage-first approach
     (identify the most critical gaps immediately). Routine refreshes allow systematic
     coverage.

3. **Existing documentation**: Does any prior data map, RoPA, or data inventory exist?
   - Options: Yes (provide it), Partial (some systems mapped), No
   - _Why this matters_: If prior mapping exists, this workflow validates and refreshes
     it rather than building from scratch.

**Defaults (non-interactive mode)**: Entire organization; initial creation; no prior map.
State assumption: "I will treat this as a full-organization initial data mapping exercise."

---

### Step 2: Identify Applicable Regime(s) and Key Requirements

Identify which privacy regimes apply based on: (1) where the organization is established,
(2) where its data subjects are located, and (3) applicable sectoral rules.

**⟁ CLARIFY #2 — Jurisdiction and Sector**

1. **Primary jurisdiction**: Where is the organization legally established?
   - Options: EU/EEA, UK, USA, Brazil, Canada, Japan, Singapore, Thailand, Australia,
     Other (specify), Multiple (specify)
   - _Why this matters_: Determines primary RoPA format, language, and completeness
     requirements.

2. **Data subject locations**: Where do your data subjects reside?
   - Options: Same jurisdiction as establishment, EU/EEA (triggers GDPR Art. 3(2)),
     UK, USA, Brazil, Canada, Multiple (list)
   - _Why this matters_: Data subjects outside establishment jurisdiction may trigger
     additional regimes (e.g., EU data subjects trigger GDPR regardless of controller location).

3. **Sector overlays**: Does any sector-specific regime apply?
   - Options: None, Healthcare (HIPAA/national equivalents), Financial services (GLBA/FSCA/FCA),
     Education (FERPA/GDPR education derogations), Children's services (COPPA/GDPR Art. 8),
     Public authority, Other (specify)
   - _Why this matters_: Sector rules add requirements beyond privacy law (HIPAA adds
     minimum necessary, BAAs; GLBA adds financial-specific safeguards rule).

**Build a regime matrix** from the answers. Document which regimes apply and what each
requires for the RoPA. Example:

```
Organization: EU-established, processes EU + US data subjects, no sector overlay
Applicable regimes: EU GDPR (primary), CCPA/CPRA (if California residents served)
RoPA format: GDPR Art. 30 (minimum standard); CCPA data category overlay for California
Key requirements: GDPR Art. 30(1) for controller; Art. 30(2) if acting as processor
```

---

### Step 3: Stakeholder Identification and Interview Planning

Identify all organizational stakeholders who own or operate systems that process personal
data. Personal data processing is pervasive — do not limit discovery to obvious systems.

#### 3a. Identify Data Handler Universe

**⟁ CLARIFY #3 — System and Data Handler Landscape**

1. **System types present**: Which categories of systems exist?
   - Options (multiselect): On-premises databases, SaaS applications (Salesforce, HubSpot,
     Google Workspace, etc.), IaaS/cloud storage (AWS S3, Azure, GCP), Mobile apps,
     IoT devices or operational technology, Third-party processors (BPOs, outsourced HR,
     payroll), Paper/physical records
   - _Why this matters_: SaaS-heavy environments require processor coordination protocols;
     on-premises databases require technical scanning; paper records require physical
     inventory and different retention mechanics.

2. **Estimated number of processing activities**: Rough scale?
   - Options: Small (under 20), Medium (20–100), Large (100–500), Enterprise (500+)
   - _Why this matters_: Determines interview bandwidth, phasing strategy, and whether
     to use questionnaire-first vs. interview-first methodology.

#### 3b. Map Business Units to Data Processing

Identify data-processing-relevant business units. For each unit, schedule a structured
data-mapping interview or issue a questionnaire. Typical units include:

| Business Unit                  | Likely Processing Activities                                  | Priority |
| ------------------------------ | ------------------------------------------------------------- | -------- |
| Human Resources                | Employee records, recruitment, payroll, benefits, L&D         | HIGH     |
| Sales / Business Development   | CRM, prospect outreach, customer profiling                    | HIGH     |
| Marketing                      | Email campaigns, web analytics, lead generation, social media | HIGH     |
| Finance / Accounting           | Invoicing, payment processing, tax, banking                   | HIGH     |
| Product / Engineering          | User accounts, product usage data, beta testing               | HIGH     |
| Customer Support               | Ticketing systems, complaint records, interaction logs        | HIGH     |
| IT / Security                  | Access logs, identity management, network monitoring          | MEDIUM   |
| Legal / Compliance             | Contract management, litigation, regulatory filings           | MEDIUM   |
| Operations / Supply Chain      | Vendor management, logistics, B2B contracts                   | MEDIUM   |
| Facilities / Physical Security | CCTV, access control, visitor management                      | MEDIUM   |

#### 3c. Conduct Structured Interviews and/or Distribute Questionnaires

**Interview Protocol** (for high-priority units and complex processing):

Use these structured questions per business unit or system owner:

1. What personal data does your system/process collect? (list each field)
2. Why is that data collected? (specific purpose, not generic)
3. What is the legal or business basis for collection?
4. Where is the data stored? (system name, hosting location, cloud region)
5. Who can access the data? (roles, teams, named vendors)
6. Is the data shared externally? If yes: with whom, why, and under what agreement?
7. Is the data transferred outside the primary jurisdiction? If yes: to which country?
8. How long is the data retained? What triggers deletion?
9. Does any automated decision-making or profiling occur? (scoring, segmentation,
   ranking, filtering)
10. What security controls are in place? (encryption, access control, logging)
11. Have you identified any gaps, risks, or uncertainties in how this data is handled?
12. Are there other systems or data stores I may have missed?

**Questionnaire Protocol** (for medium-priority units or large organizations):

Distribute a structured questionnaire covering the same 12 areas. Set a 10-business-day
completion window. Flag incomplete responses for follow-up interview.

**Automated Discovery** (supplement all human discovery):

Where tools are available, use automated scanning to:

- Identify network-connected data stores (databases, file servers, S3 buckets)
- Detect PII patterns in unstructured data (regex-based or ML-based scanning)
- Map API calls and data flows between systems
- Surface shadow IT that questionnaires may miss

Record all systems discovered (whether by interview, questionnaire, or scanning) in the
**System Inventory Log**:

```
System Inventory Log
| System ID | System Name | Owner/Team | Type | Location | Data Categories (preliminary) | Status |
|-----------|-------------|------------|------|----------|-------------------------------|--------|
| SYS-001   | Salesforce  | Sales       | SaaS | EU-W     | Contact, interaction, company | Mapped |
| SYS-002   | Excel sheets| Finance     | Desktop | Local | Employee salary, IBAN        | Flagged |
| SYS-003   | Unknown CRM | Marketing   | Unknown | Unknown | Unknown                       | Red flag |
```

---

### Step 4: Data Flow Mapping

For each identified system and processing activity, document the complete data flow from
collection to deletion. Use both **Data Flow Mapping** (category-level movement) and
**Data Lineage Mapping** (record-level lifecycle) where required.

**Data Flow Mapping** (category-level — sufficient for GDPR Art. 30):

Document the flow of each data category through the organization:

```
[Source / Collection Point]
        │
        ▼ (Legal basis + purpose documented)
[Storage System]
        │
        ├──▶ [Internal System 2] (purpose: analytics)
        │
        ├──▶ [Processor: Vendor Name] (DPA: [status]) ──▶ [Third country?]
        │
        └──▶ [Deletion / Anonymization] (after: [retention period])
```

**Data Lineage Mapping** (record-level — required for right to erasure and DSAR):

For high-risk or high-volume data categories, trace specific records:

- Where was this individual's data first collected?
- Was it copied to derived systems (analytics, ML training, backups)?
- Has it been pseudonymized, anonymized, or aggregated?
- Can it be located and deleted in response to a DSAR erasure request?

**Cross-Border Transfer Identification**:

For every external recipient or cloud hosting location, document:

- Data destination country
- Legal mechanism in place (adequacy decision, SCC, BCR, derogation)
- Supplementary measures (encryption in transit, access controls at destination)
- Date of last transfer mechanism review

Flag all third-country transfers for downstream assessment by `legalcode-cross-border-transfer-assessment`.

---

### Step 5: Personal Data Classification

Classify every data category discovered in Steps 3 and 4. Classification determines legal
basis requirements, security obligations, DPIA triggers, and data subject rights.

**⟁ CLARIFY #4 — Data Sensitivity Profile**

Before classifying, confirm the data sensitivity landscape:

1. **Highest-sensitivity data present**: Does the organization process any of the following?
   - Options (multiselect): Special-category data (health, biometric, genetic, racial/ethnic
     origin, political opinions, religious beliefs, trade union membership, sexual orientation),
     Criminal conviction or offence data (Art. 10), Data relating to children (under 16),
     Data relating to vulnerable populations (elderly, financially distressed, employees
     under power imbalance), None of the above
   - _Why this matters_: Special-category and criminal data require Art. 9/Art. 10 conditions
     documented in the mapping — not just an Art. 6 basis. Children's data triggers
     heightened DPIA and design obligations. Vulnerability affects the balancing test
     for legitimate interests.

2. **Automated decision-making or profiling**: Does any processing involve automated
   rules, scoring, ranking, segmentation, or recommendation with effects on individuals?
   - Options: None, Segmentation only (non-binding), Scoring/ranking with human review
     (non-binding significant effects), Automated decision with legal/similarly significant
     effects (Art. 22 candidate), Unclear — requires investigation
   - _Why this matters_: Art. 22 automated decisions make DPIA mandatory (GDPR Art. 35(3)(a)),
     require specific transparency notices, and trigger the right not to be subject to
     automated decision-making. Missing this flag is a systematic enforcement risk.

**Defaults (non-interactive mode)**: Assume special categories may be present (flag each
processing activity for confirmation); flag all scoring/ranking for Art. 22 investigation.
State assumption explicitly.

#### 5a. Standard Personal Data Categories

Apply this classification schema to every data field or data category:

| Category               | Description                           | Examples                                   | Risk Tier   |
| ---------------------- | ------------------------------------- | ------------------------------------------ | ----------- |
| **Identifiers**        | Direct identification data            | Name, email, phone, employee ID, NI/SSN    | Medium      |
| **Contact**            | Reachability data                     | Postal address, work address               | Low–Medium  |
| **Financial**          | Payment and banking data              | IBAN, card number, salary, transactions    | High        |
| **Location**           | Geolocation or movement data          | GPS, IP-geolocation, mobile network        | Medium–High |
| **Behavioral**         | Usage, browsing, interaction patterns | Web analytics, app usage, purchase history | Medium      |
| **Communications**     | Message content or metadata           | Email content, call logs, chat transcripts | Medium–High |
| **Professional**       | Employment and business info          | Job title, employer, LinkedIn profile      | Low–Medium  |
| **Education**          | Academic and certification data       | Grades, qualifications, school records     | Medium      |
| **Device**             | Technical device identifiers          | Device ID, MAC address, cookie ID, IMEI    | Medium      |
| **Derived / Inferred** | Conclusions drawn from other data     | Credit score, risk profile, lead score     | Medium–High |

#### 5b. Special Category Data (GDPR Art. 9 — Enhanced Protection)

**Explicitly identify and flag ALL special-category data in the processing register.**
Processing special-category data is prohibited by default; a specific Art. 9(2) condition
must be documented.

| Special Category                  | Art. 9 Sub-Category                       | Typical Context                                      | Art. 9(2) Conditions Most Commonly Used                 |
| --------------------------------- | ----------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| **Health data**                   | Physical or mental health status          | HR wellness programs, insurance, occupational health | (b) Employment law obligations; (h) Healthcare provider |
| **Genetic data**                  | Hereditary or acquired characteristics    | Genomics, research                                   | (j) Scientific research; (a) Explicit consent           |
| **Biometric data**                | Uniquely identifying biometric processing | Fingerprint readers, face recognition, retina scan   | (a) Explicit consent                                    |
| **Racial/ethnic origin**          | Racial or ethnic background               | Diversity monitoring, recruitment                    | (b) Employment law; (g) Public interest                 |
| **Political opinions**            | Political views or affiliations           | Political campaigns, research                        | (a) Explicit consent; (d) Non-profit members            |
| **Religious beliefs**             | Religion or philosophical beliefs         | Accommodations, dietary, faith-based orgs            | (b) Employment law; (a) Explicit consent                |
| **Trade union membership**        | Union affiliation                         | HR, payroll (union dues)                             | (b) Employment law obligations                          |
| **Sexual orientation / sex life** | Sexual orientation or sex life            | LGBTQ+ inclusion programs, HR                        | (a) Explicit consent                                    |

For each special-category item, document:

- Which Art. 9(2) condition applies
- The justification narrative
- Any Data Protection Officer sign-off required by policy

#### 5c. Criminal Conviction and Offence Data (GDPR Art. 10)

Criminal data requires processing under official authority OR national law authorization.
Flag any processing involving: criminal convictions, criminal offences, security measures,
criminal background checks, or spent conviction data.

[JURISDICTION-SPECIFIC] — Criminal data processing varies significantly:

- UK: DBS (Disclosure and Barring Service) checks under regulated exceptions [VERIFY]
- Germany: Employee background screening regulations (BAG case law) [VERIFY]
- US: "Ban-the-box" laws vary by state; FCRA requirements for background checks [VERIFY]
- France: Strict prohibition with limited Art. 10 exceptions (CNIL guidance) [VERIFY]

#### 5d. Data Relating to Children

Flag any processing where data subjects may be under 16 (or under 13 in some regimes).
Children's data triggers heightened obligations: parental consent, age verification,
privacy notices in plain language, prohibition of profiling for commercial purposes.

[JURISDICTION-SPECIFIC] — Age thresholds:

- EU GDPR Art. 8: Default 16; Member States may lower to 13 [VERIFY national implementations]
- UK GDPR: Age 13; ICO's Children's Code (25 standards for age-appropriate design)
- CCPA/COPPA (US): Under-16 require opt-in; under-13 require parental consent (COPPA)
- Brazil LGPD: Under-18 with parental consent required [VERIFY current ANPD guidance]

---

### Step 6: Legal Basis Assignment and Necessity Screening

**⟁ CLARIFY #5 — Consent and Legitimate Interest Landscape**

Before assigning legal bases, confirm the high-impact basis choices:

1. **Consent-based processing**: Does the organization rely on consent for any processing?
   - Options: No (no consent-based processing), Yes — digital consent only (clickwrap,
     checkboxes), Yes — verbal or paper consent (call recordings, forms), Yes — implied
     consent (website analytics with consent banner), Unclear
   - _Why this matters_: Consent requires a demonstrable consent record. If records are
     inaccessible, the basis is unenforceable — not just undocumented. Organizations
     often claim consent without a consent log system.

2. **Legitimate interests scope**: How widely does the organization rely on legitimate
   interests as a legal basis?
   - Options: Rarely (1–2 processing activities), Moderate (3–10 activities), Extensively
     (marketing, analytics, fraud prevention, security monitoring — all LI-based)
   - _Why this matters_: Every legitimate-interest basis requires a documented three-part
     LIA. If the organization relies extensively on LI, this phase will generate multiple
     LIA work orders for `legalcode-legitimate-interest-assessment`. Extensive LI reliance
     without completed LIAs is a high-volume enforcement risk.

**Defaults (non-interactive mode)**: Proceed with basis assignment; flag all LI-basis
activities for LIA completion; flag all consent-basis activities for consent record audit.

For every processing activity, assign a legal basis and document the justification.
This is the most legally rigorous phase of data mapping.

#### 6a. Controller Legal Bases (GDPR Art. 6 equivalents)

**Rule**: Every processing activity must link to exactly ONE primary legal basis.
Document the basis at the time of mapping — never retrospectively.

| Legal Basis              | GDPR Article | When Appropriate                                                               | Documentation Required                                |
| ------------------------ | ------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------- |
| **Consent**              | Art. 6(1)(a) | Data subject freely opted in for this specific purpose                         | Mechanism, moment, withdrawal method, consent log     |
| **Contract**             | Art. 6(1)(b) | Processing is necessary to perform or prepare a contract with the subject      | Contract clause reference, contract copy, end-trigger |
| **Legal obligation**     | Art. 6(1)(c) | Processing required by statute, regulation, or court order                     | Specific law/article citation, scope of obligation    |
| **Vital interests**      | Art. 6(1)(d) | Emergency; subject unable to consent; life at stake                            | Emergency circumstances documentation (rare basis)    |
| **Public task**          | Art. 6(1)(e) | Official authority or public body performing statutory function                | Statutory authority citation                          |
| **Legitimate interests** | Art. 6(1)(f) | Organization's or third party's legitimate interest overrides subject's rights | Documented LIA (three-part test — see below)          |

**Legitimate Interest Assessment (LIA) — Three-Part Test**:

Where legitimate interests is the claimed basis, document all three parts:

1. **Legitimate Interest Test**: What is the specific interest? Is it "real and present"
   (not hypothetical), not unlawful, and socially acceptable?

2. **Necessity Test**: Is processing actually necessary for that interest? Have less
   intrusive alternatives been considered and rejected?

3. **Balancing Test**: Do the data subject's rights, freedoms, and reasonable expectations
   outweigh the legitimate interest? Consider: sensitivity of data, power imbalance,
   reasonable expectations at time of collection, safeguards to mitigate impact.

Flag every Legitimate Interest claim for completion of a full LIA via `legalcode-legitimate-interest-assessment`.

#### 6b. Special Category Legal Bases (GDPR Art. 9(2))

Special-category processing requires BOTH an Art. 6 basis AND an Art. 9(2) condition.
Document both explicitly:

| Art. 9(2) Condition                | When It Applies                                                     | Documentation Required                                              |
| ---------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| (a) Explicit consent               | Freely given, specific, informed, unambiguous explicit consent      | Double-opt-in record; purpose-specific consent text; withdrawal log |
| (b) Employment/social security law | Processing necessary under employment or social protection law      | Specific law citation; HR policy reference                          |
| (c) Vital interests (incapacity)   | Subject cannot consent; vital interests require processing          | Medical/emergency circumstances; DPO oversight                      |
| (f) Legal claims                   | Processing necessary to establish, exercise, or defend legal claims | Litigation reference; legal counsel instruction                     |
| (g) Public interest                | Necessary for reasons of substantial public interest                | Statutory basis; DPIA required                                      |
| (h) Health/social care             | Preventive medicine, occupational health, healthcare delivery       | Professional secrecy obligation; healthcare authority basis         |
| (j) Research/archiving             | Archiving, scientific/historical research, statistics               | Institutional ethics approval; data minimization evidence           |

#### 6c. Necessity and Proportionality Screening

For every processing activity, apply this three-question screen:

1. **Minimum necessary**: Is every data field collected actually needed for the stated purpose?
   Remove or flag any field where the answer is "maybe" or "historic practice."

2. **Purpose limitation**: Is the data used only for the documented purpose?
   Flag any activity where data collected for Purpose A is used for Purpose B without
   a documented compatible purpose analysis.

3. **Storage limitation**: Is the retention period the minimum required for the purpose?
   Flag any "indefinite" or "until no longer needed" retention as YELLOW or RED.

---

### Step 7: Recipient Identification, DPA Audit, and Transfer Mapping

**⟁ CLARIFY #6 — Vendor and Transfer Landscape**

Before auditing recipients, confirm the scope of the external data sharing ecosystem:

1. **Third-party data sharing scope**: How complex is the vendor/recipient landscape?
   - Options: Simple (fewer than 10 processors, no cross-border transfers), Moderate
     (10–50 processors, some cross-border transfers to EEA/UK), Complex (50+ processors,
     transfers to US or other non-adequate third countries), Enterprise (multiple
     corporate-group entities + large processor base + multi-country transfers)
   - _Why this matters_: Complex/enterprise landscapes require phased DPA audits (cannot
     complete in one pass). Transfers to non-adequate third countries (US, India, China)
     require Transfer Impact Assessments as mandatory follow-up.

2. **DPA coverage**: Of your current processors, how many have a signed, current DPA?
   - Options: All processors have current DPAs, Most processors covered (minor gaps),
     Significant gaps (many processors without DPA), Unknown (no prior DPA audit)
   - _Why this matters_: Processors without DPAs represent direct Art. 28 violations.
     The answer determines whether the DPA audit phase is validation (most covered) or
     remediation (significant gaps requiring new DPA executions within 30-60 days).

**Defaults (non-interactive mode)**: Assume moderate complexity; flag all processors for
DPA verification; flag all non-EEA transfers for TIA.

Identify every party that receives personal data from the organization. Classify each
recipient and document the legal framework governing the sharing.

#### 7a. Recipient Classification

| Recipient Type              | Definition                                                 | GDPR Obligation                                                 | Data Map Notation                     |
| --------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------- |
| **Internal teams**          | Same legal entity, different department                    | Data access controls (not a "recipient" in formal sense)        | Document role-based access            |
| **Group companies**         | Same corporate group, different entity                     | May be processors or independent controllers; each requires DPA | Document intra-group DPA or group BCR |
| **Processors**              | Act on controller's instructions; do not determine purpose | Mandatory DPA (Art. 28); subprocessor control                   | DPA date, version, subprocessor list  |
| **Joint controllers**       | Two+ entities jointly determine purpose/means              | Written agreement defining responsibilities (Art. 26)           | JCA date, responsibility allocation   |
| **Third-party controllers** | Receive data for their own independent purposes            | No DPA; separate privacy notice; data subject must be informed  | Basis for sharing; Art. 13/14 notice  |
| **Public authorities**      | Legal obligation to share with regulators, courts, etc.    | No DPA; legal obligation basis                                  | Law/order citation                    |

#### 7b. Data Processing Agreement (DPA) Audit

For every processor relationship, complete a DPA completeness check:

| DPA Element                                              | Required by GDPR Art. 28 | Present? | Quality |
| -------------------------------------------------------- | ------------------------ | -------- | ------- |
| Processing subject matter and duration                   | ✓                        |          |         |
| Nature and purpose of processing                         | ✓                        |          |         |
| Type of personal data and categories of subjects         | ✓                        |          |         |
| Controller's obligations and rights                      | ✓                        |          |         |
| Processor must process only on instruction               | ✓                        |          |         |
| Confidentiality obligations on authorized persons        | ✓                        |          |         |
| Technical and organizational security measures           | ✓                        |          |         |
| Sub-processor restrictions (prior written authorization) | ✓                        |          |         |
| Assistance with data subject rights                      | ✓                        |          |         |
| Assistance with controller compliance obligations        | ✓                        |          |         |
| Deletion or return of data on termination                | ✓                        |          |         |
| Audit and inspection cooperation                         | ✓                        |          |         |
| Sub-processor list (named or category)                   | ✓                        |          |         |

Mark each DPA: `COMPLIANT`, `GAPS_IDENTIFIED` (list gaps), or `MISSING` (RED flag).

#### 7c. Cross-Border Transfer Mapping

For every external recipient or cloud hosting location outside the primary jurisdiction:

1. **Identify the destination country**
2. **Check for adequacy decision** [JURISDICTION-SPECIFIC — check current adequacy decisions for your primary regime; decisions change post-Schrems II and post-Brexit]
3. **Identify current transfer mechanism**: Standard Contractual Clauses (SCCs), BCRs, Art. 49 derogations, or adequacy
4. **Assess SCC validity**: Confirm the version in use is current (EU SCC 2021 Implementing Decision; UK IDTA or Addendum)
5. **Document supplementary measures** (encryption, pseudonymization, contractual limitations on government access)
6. **Flag for Transfer Impact Assessment (TIA)** where transfer is to a country without adequacy and the SCC alone may be insufficient post-Schrems II

Feed all flagged transfers to `legalcode-cross-border-transfer-assessment` for full TIA.

**Transfer Ledger** (for each system with external data flows):

```markdown
| Recipient         | Destination Country | Adequacy?                | Transfer Mechanism | SCCs Version | Last Reviewed | TIA Required?             | Status |
| ----------------- | ------------------- | ------------------------ | ------------------ | ------------ | ------------- | ------------------------- | ------ |
| AWS eu-west-1     | Ireland (EU)        | Yes (EU intra-EEA)       | N/A                | N/A          | —             | No                        | GREEN  |
| Salesforce        | USA                 | No (no US-wide adequacy) | EU SCCs (2021)     | June 2021    | 2024-11-01    | YES (US govt access risk) | YELLOW |
| Support vendor    | India               | No                       | EU SCCs (2021)     | June 2021    | 2024-09-01    | YES                       | YELLOW |
| Unknown analytics | Unknown             | Unknown                  | None on file       | —            | Never         | Blocked                   | RED    |
```

---

### Step 8: Retention Schedule Alignment

For every processing activity and data category, document the retention trigger, period,
deletion method, and any overrides.

#### 8a. Retention Schedule Principles

- **Storage limitation**: GDPR Art. 5(1)(e) requires data is kept no longer than necessary.
  No regime specifies uniform retention periods; organizations set periods based on purpose
  and legal/regulatory requirements.
- **Retention trigger**: The event that starts the retention clock (e.g., contract end,
  last customer interaction, employee departure, consent withdrawal).
- **Deletion method**: How data is destroyed (secure deletion, cryptographic erasure,
  anonymization, certified third-party destruction).
- **Override conditions**: Statutory requirements that extend retention (tax records,
  employment law, litigation hold); document the specific law and duration.

#### 8b. Reference Retention Periods by Category

These are indicative reference ranges. Verify against applicable law for your jurisdiction:

| Data Category                  | Typical Retention Range         | Common Override (Statutory)                                   |
| ------------------------------ | ------------------------------- | ------------------------------------------------------------- |
| **Employee records**           | Employment duration + 2–7 years | Employment law (varies); [JURISDICTION-SPECIFIC]              |
| **Payroll / tax records**      | 7–10 years                      | Tax authority requirements; [JURISDICTION-SPECIFIC]           |
| **Customer / contractual**     | Contract duration + 3–7 years   | Statute of limitations; [JURISDICTION-SPECIFIC]               |
| **Marketing / consent**        | 2–3 years post-last-interaction | Until consent withdrawn (shorter controls)                    |
| **Health data**                | 10–30 years                     | Medical regulation (highly variable); [JURISDICTION-SPECIFIC] |
| **Financial transactions**     | 5–7 years                       | AML, banking regulation; [JURISDICTION-SPECIFIC]              |
| **Server and access logs**     | 30–365 days                     | Security incident investigation needs                         |
| **CCTV footage**               | 30–90 days                      | Security policy; some jurisdictions regulated                 |
| **Recruitment (unsuccessful)** | 6 months post-decision          | Some jurisdictions: up to 2 years [VERIFY]                    |
| **Legal / litigation hold**    | Duration of proceedings + SOL   | Must override normal retention schedule                       |

[JURISDICTION-SPECIFIC] Verify all retention periods against local employment law, tax
authority rules, sector-specific regulation, and applicable statute of limitations.

#### 8c. Retention Schedule Table

Produce a retention schedule table for every processing activity:

```markdown
## Retention Schedule

| Activity ID | Data Category          | Retention Trigger   | Period            | Deletion Method        | Exception             | Statutory Basis          | Documented?        |
| ----------- | ---------------------- | ------------------- | ----------------- | ---------------------- | --------------------- | ------------------------ | ------------------ |
| PA-001      | Employee contract data | Date of termination | 7 years           | Secure deletion        | None                  | [Tax law citation]       | ✓                  |
| PA-002      | Prospect contact (CRM) | Last interaction    | 3 years           | Soft-delete then purge | Legal hold if dispute | Art. 5(1)(e) GDPR        | ✓                  |
| PA-003      | Analytics event data   | Collection date     | 24 months rolling | Automated purge        | None                  | Vendor retention setting | ✓ [VERIFY setting] |
```

---

### Step 9: Completeness Assessment and Gap Identification

**⟁ CLARIFY #7 — Multi-Regime Compliance Scope**

Before generating the completeness scorecard, confirm the full jurisdiction scope:

1. **Additional regimes beyond GDPR**: Besides GDPR/UK GDPR, which regimes apply?
   - Options (multiselect): CCPA/CPRA (California), LGPD (Brazil), PIPEDA + Québec
     Law 25 (Canada), HIPAA (US healthcare), GLBA (US financial), FERPA (US education),
     COPPA (US children online), APPI (Japan), PDPA (Singapore), PDPA (Thailand),
     POPIA (South Africa), Other (specify), None beyond GDPR
   - _Why this matters_: Each additional regime adds columns to the Processing Activity
     Register, different legal basis equivalents, different retention requirements, and
     different rights obligations. CCPA/CPRA adds 11 statutory data categories; LGPD
     adds sensitive data equivalents; Québec Law 25 adds mandatory RoPA equivalent.

2. **Sector-specific completeness checks**: Does the completeness assessment need to
   include sector-specific requirements?
   - Options: No sector overlay, Healthcare sector (HIPAA Business Associate Agreement
     inventory, minimum necessary standard), Financial services (GLBA safeguards rule,
     data categories audit), Education (FERPA records inventory), Other (specify)
   - _Why this matters_: Sector regimes add obligations beyond privacy law. HIPAA
     requires Business Associate Agreements (equivalent to DPAs but distinct); GLBA
     requires a Safeguards Rule compliance inventory.

**Defaults (non-interactive mode)**: Apply GDPR/UK GDPR completeness criteria as
primary standard; flag any CCPA/CPRA, LGPD, and PIPEDA overlays identified in Step 2
as secondary validation tracks. Note assumption explicitly.

Evaluate every processing activity against the completeness criteria and assign a
classification. This drives the remediation backlog.

#### 9a. Classification Criteria

**GREEN — Fully Mapped and Documented** (ALL of the following must be true):

- Processing objective, legal basis, and data categories clearly identified
- Data flows (source → storage → recipients → deletion) documented
- All internal and external recipients identified; DPAs verified where required
- Retention trigger, period, and deletion mechanics documented (no "indefinite" without justified exception)
- Cross-border transfers assessed or confirmed not applicable
- Special-category and criminal-data flags correctly applied (or absence confirmed)
- Automated decision-making classification complete (none, non-significant, or Art. 22 triggers documented)
- Necessity and proportionality test passed (no obviously excessive data collection)

**Action**: Ready to serve as DPIA input, DSAR discovery basis, and transfer assessment foundation.

---

**YELLOW — Partially Mapped / Requires Remediation** (ANY of the following):

- Processing objective stated but legal basis unclear, unverified, or asserted without documentation
- Data sources identified but recipients or destinations incomplete ("possibly shared with subsidiary")
- Retention period ambiguous ("kept as long as needed") without documented justification
- Cross-border transfer flagged but no TIA or adequacy assessment initiated
- Vendor/processor relationship present but DPA absent, expired, or not covering this data
- Special-category data suspected but not confirmed; Art. 9 condition not yet documented
- Automated decision-making presence uncertain or scoring system undocumented
- Necessity screen incomplete (some fields may be excessive but not yet analyzed)
- DPA covers some but not all subprocessors
- Consent records exist but retrieval mechanism not confirmed

**Action**: Issue remediation task with 14-day default deadline. DPIA and DSAR may proceed
with conditional approval for GREEN elements; YELLOW items require parallel remediation.

---

**RED — Unmapped or Blocking Gaps** (ANY of the following):

- Processing activity identified but no purpose, legal basis, or data categories documented
- Data flow destination unknown or undocumented ("needs investigation")
- Retention period missing entirely (indefinite retention with no documented rationale)
- Special-category data processing without any documented Art. 9 condition
- Cross-border transfer to non-adequate third country without any legal mechanism
- Processor relationship with no DPA, no contract, no authorization
- Automated decision-making with legally significant effects and no DPIA, no mitigation, no Art. 22 notice
- Data subject rights cannot be fulfilled due to inaccessible retention/deletion mechanics
- Consent records unrecoverable or consent mechanism confirmed non-compliant
- Data source unknown (e.g., data purchase from broker with unclear provenance)

**Action**: BLOCKING. Do not use this processing activity to respond to DSARs or feed
into DPIAs until RED issue is resolved. Escalate to DPO/Privacy Lead. Consider temporary
suspension of the processing activity pending remediation.

#### 9b. Self-Interrogation for RED-Classified Activities

For every RED item, apply this three-pass review before confirming the classification:

**Pass 1 — Root Cause**: Is this a documentation gap (data exists but wasn't captured),
a process gap (no policy governing this processing), or a design gap (processing
was set up without privacy consideration)?

**Pass 2 — Remediation Path**: What is the fastest route to GREEN? (Document the existing
practice? Implement a missing DPA? Stop the processing? Redesign the data flow?)

**Pass 3 — Challenge**: Is there a reasonable argument this activity is compliant despite
the gap? (e.g., "the processing has always been on Art. 6(1)(b) Contract — we just
haven't documented it yet") — If yes, classify as YELLOW with note, not RED.

#### 9c. Completeness Scorecard

| Metric                                 | Value                                                             |
| -------------------------------------- | ----------------------------------------------------------------- |
| Total processing activities identified | [N]                                                               |
| GREEN (fully mapped)                   | [X] ([X/N]%)                                                      |
| YELLOW (partially mapped)              | [Y] ([Y/N]%)                                                      |
| RED (blocking gaps)                    | [Z] ([Z/N]%)                                                      |
| RoPA Art. 30(1) completeness           | [%] of required fields populated across all activities            |
| Special-category flags reviewed        | [M] of [M_total] activities with Art. 9 conditions documented     |
| Cross-border transfers assessed        | [P] of [P_total] flagged transfers with legal mechanism confirmed |
| Processor DPAs verified                | [Q] of [Q_total] processor relationships with compliant DPAs      |

---

### Step 10: Deliverable Assembly and Quality Gates

Assemble the final RoPA package and run all quality gates before delivery.

#### 10a. Assemble the RoPA Package

The deliverable is a multi-part Records of Processing Activities package:

**Part A: Executive Summary**

```markdown
# Records of Processing Activities — [Organization Name]

## Mapping Details

- Mapping Period: [Start] to [Completion]
- Scope: [Organization / Division / Product / Region]
- Jurisdiction(s): [GDPR / UK GDPR / CCPA-CPRA / LGPD / PIPEDA / Other]
- Version: [1.0 / Refresh date]
- Prepared by: [Role — not individual name for GDPR minimization]
- DPO Review: [Pending / Reviewed on date]

## Completeness Overview

- Total Processing Activities: [N]
- GREEN (ready): [X] ([X/N]%)
- YELLOW (remediation required): [Y] — see Gap Log
- RED (blocking): [Z] — see Escalation Log

## Key Findings

- Special-category processing: [None / Present — [N] activities with Art. 9 conditions]
- Cross-border transfers: [None / Present — [N] transfers, [M] with TIA pending]
- Automated decision-making (Art. 22): [None / Present — [N] activities, DPIA required: [K]]
- Processor DPA gaps: [None / [N] processors without compliant DPA — see Gap Log]

## Downstream Actions Required

- DPIA mandatory for: [list activity IDs]
- Transfer TIA required for: [list destination countries and activity IDs]
- Vendor DPA remediation for: [list processor names]
- Consent mechanism audit for: [list activities using consent basis]
- LIA completion for: [list activities using legitimate interests]
```

**Part B: Processing Activity Register (Master Table)**

Produce a row per processing activity with all GDPR Art. 30(1) fields:

```markdown
| Activity ID | Category | Processing Purpose  | Legal Basis (Art. 6)  | Art. 9 Condition (if applicable) | Data Categories                     | Data Subject Categories | Storage System | Storage Location   | Internal Recipients | External Recipients     | DPA Status            | Retention Period     | Deletion Method | Cross-Border Transfer? | Transfer Mechanism | Automated Decision? | DPIA Required? | Status |
| ----------- | -------- | ------------------- | --------------------- | -------------------------------- | ----------------------------------- | ----------------------- | -------------- | ------------------ | ------------------- | ----------------------- | --------------------- | -------------------- | --------------- | ---------------------- | ------------------ | ------------------- | -------------- | ------ |
| PA-001      | HR       | Employee onboarding | Art. 6(1)(b) Contract | None                             | Name, address, NI/SSN, bank details | Employees               | HRIS           | EU (AWS eu-west-1) | HR, Payroll, IT     | Payroll processor (ADP) | DPA signed 2024-03-01 | Employment + 7 years | Secure deletion | No                     | N/A                | No                  | No             | GREEN  |
```

**Part C: Data Flow Summary (Narrative + Diagram References)**

For each system, provide a brief narrative data flow description and flag diagram locations
(reference external tool such as Miro, Lucidchart, or plain ASCII where applicable):

```markdown
### System: Salesforce CRM

- **Data in**: Contact information, interaction history, company data — collected via
  web forms, manual entry by sales team, API import from marketing automation.
- **Data processed**: Lead scoring via automated rules (non-binding, non-significant
  effects — classified as not Art. 22). Customer segmentation (same).
- **Data out**: Shared with Marketo (marketing automation, EU SCC), Zendesk (support,
  EU SCC), and finance team (internal).
- **Cross-border**: Salesforce hosted on EU instance; Marketo US-hosted (SCC in place,
  TIA pending). [FLAG for cross-border-transfer-assessment]
- **Retention**: 3 years post-last-interaction, then automatic purge via Salesforce
  scheduled deletion.
- **Status**: YELLOW — Marketo TIA pending; SCC audit required.
```

**Part D: Legal Basis Reference Table**

Document legal basis documentation for each processing activity:

```markdown
| Activity ID | GDPR Art. 6 Basis            | Basis Documentation      | CCPA Equivalent                              | LGPD Equivalent | Consent Obtained?   | LIA Completed? |
| ----------- | ---------------------------- | ------------------------ | -------------------------------------------- | --------------- | ------------------- | -------------- |
| PA-001      | 6(1)(b) Contract             | Employment contract, s.3 | B2B exemption (employee data)                | Art. 7(II)      | No (contract basis) | N/A            |
| PA-002      | 6(1)(f) Legitimate interests | LIA pending [YELLOW]     | Business purpose (Cal. Civ. Code § 1798.140) | Art. 7(IX)      | No                  | Pending        |
```

**Part E: Recipient and DPA Verification Matrix**

```markdown
| Recipient        | Role      | Data Processed               | Jurisdiction | DPA Signed                     | DPA Date   | DPA Version       | Subprocessors Listed | Transfer Mechanism           | DPA Status |
| ---------------- | --------- | ---------------------------- | ------------ | ------------------------------ | ---------- | ----------------- | -------------------- | ---------------------------- | ---------- |
| ADP Payroll      | Processor | Salary, NI/SSN, bank details | EU           | Yes ✓                          | 2024-03-01 | GDPR-compliant v3 | Yes (AWS eu-west-1)  | EU intra-EEA                 | GREEN      |
| Marketo          | Processor | Email, behavioral            | USA          | Yes ✓                          | 2024-09-01 | 2021 SCCs         | Yes (AWS, Twilio)    | SCC (audit pending)          | YELLOW     |
| Google Analytics | Processor | Session, device, event       | USA          | [VERIFY: DPA status post-2024] | N/A        | —                 | Yes (GCP)            | [VERIFY: transfer mechanism] | [VERIFY]   |
```

**Part F: Retention and Deletion Schedule**

(See Step 8c table format — compile all activities into single schedule.)

**Part G: Gap Log and Remediation Tracker**

```markdown
## Gap Log

| Gap ID  | Activity ID | Classification | Issue Description                                                            | Remediation Action                                                 | Owner        | Due Date   | Blocking? | Status |
| ------- | ----------- | -------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------ | ---------- | --------- | ------ |
| GAP-001 | PA-003      | RED            | Google Analytics DPA not confirmed; transfer mechanism to USA not documented | (1) Verify DPA with Google; (2) Initiate TIA for US transfer       | Privacy Lead | 2026-04-01 | YES       | Open   |
| GAP-002 | PA-006      | YELLOW         | Legitimate interest basis claimed for profiling but no LIA completed         | Complete LIA via legalcode-legitimate-interest-assessment          | DPO          | 2026-04-15 | No        | Open   |
| GAP-003 | PA-009      | YELLOW         | Retention period set to "until no longer needed" — no specific trigger       | Define specific retention trigger and period; update HRIS settings | HR + Privacy | 2026-04-30 | No        | Open   |
```

---

#### 10b. Citation Quality Gates

Run these five gates silently on every legal citation, regulatory reference, and
compliance claim in the RoPA package before delivery:

| Gate                | Rule                                                                                                                                                   | Fail Action                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| **Source Gate**     | Every legal claim references a specific Article, Regulation, or DPA guidance document                                                                  | Add citation or mark "[UNVERIFIED]"                            |
| **Format Gate**     | All citations follow consistent format for jurisdiction (e.g., "GDPR Art. 30(1)(a)" not "article 30")                                                  | Standardize format                                             |
| **Currency Gate**   | Each cited provision verified as current (not repealed or amended) — especially post-Schrems II SCCs, post-Brexit UK instruments, CCPA/CPRA amendments | Flag "[CHECK CURRENCY]" for any provision post-2021            |
| **Domain Gate**     | Analysis stays within identified applicable regimes; no jurisdiction-specific concepts presented as universal                                          | Mark "[JURISDICTION-SPECIFIC]" for any regime-specific content |
| **Confidence Gate** | Uncertainty is explicitly stated and not hidden; all "[VERIFY]" tags remain visible until resolved                                                     | Add confidence qualifier; do not suppress unverified items     |

#### 10c. Writing Standards and Quality Checks

Before delivering the RoPA package:

- Remove vague descriptions: replace "customer data" with specific enumerated fields
- Remove "until no longer needed": replace with specific retention trigger + period
- Remove "as appropriate": replace with specific action or documented decision
- Verify every Art. 9 condition has a justification narrative (not just the Article number)
- Verify every cross-border transfer entry has either a legal mechanism or a RED flag
- Verify every processor has either a compliant DPA reference or a gap log entry
- Verify every LI-basis activity has either a completed LIA or a YELLOW remediation flag
- Verify the Gap Log captures all YELLOW and RED items from the activity register
- Cross-check counts: Total activities = GREEN + YELLOW + RED. No orphaned items.

---

## Data Classification Quick Reference

### Standard Personal Data Sensitivity Tiers

| Tier                    | Data Types                                                             | Risk Level | Processing Controls                                                               |
| ----------------------- | ---------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------- |
| **Tier 1 — Critical**   | Health, genetic, biometric, financial payment, criminal records        | Very High  | Art. 9 mandatory; DPIA likely; encryption at rest required; strict access control |
| **Tier 2 — Sensitive**  | Location, behavioral profiling, communication content, children's data | High       | Heightened legal basis scrutiny; privacy notice required; consider DPIA           |
| **Tier 3 — Standard**   | Contact info, identifiers, professional data, derived/inferred scores  | Medium     | Standard GDPR Art. 6 basis required; privacy notice required                      |
| **Tier 4 — Lower Risk** | Aggregated/anonymized data, public business information                | Low        | Verify true anonymization; GDPR may not apply if genuinely anonymized             |

---

## Quality Frameworks

### Self-Interrogation for RED-Classified Processing Activities

For any activity classified RED, apply this adversarial review before escalating:

**Pass 1 — Documentation vs. Reality**: Does the gap reflect a documentation failure
(the organization actually has a legal basis and controls, but they're not recorded)
or a substantive gap (the processing was never designed to be compliant)?

**Pass 2 — Harm Assessment**: If this processing activity were challenged by a regulator
today, what is the probability of enforcement? What is the maximum exposure (fine,
enforcement order, reputational damage)?

**Pass 3 — Counter-Argument**: What is the best-case argument that this activity is
compliant despite the apparent gap? Under what circumstances would a regulator
accept the processing? Does that pathway exist here?

### Confidence Scoring

| Level        | Range     | Meaning                                        | Application in Data Mapping                      |
| ------------ | --------- | ---------------------------------------------- | ------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law, clear statutory requirement       | Art. 30 mandatory fields; known legal bases      |
| **High**     | 0.80–0.94 | Strong authority, minor interpretive questions | EDPB guidelines; ICO published guidance          |
| **Probable** | 0.60–0.79 | Good arguments, reasonable interpretation      | Novel data uses; sector-specific applications    |
| **Possible** | 0.40–0.59 | Genuine legal uncertainty                      | Art. 9 edge cases; legitimate interest balancing |
| **Unlikely** | 0.0–0.39  | Speculative or weak basis                      | Do not assert; flag "[UNCERTAIN]"                |

Apply Confidence Scoring to every legal basis assignment. Where confidence is below
0.80, flag the activity as YELLOW and note the interpretive uncertainty.

---

## Anti-Patterns

What NOT to do when conducting a data mapping exercise:

1. **Treating the data map as a one-time artifact.** Organizations create a RoPA once
   and file it. Three years later, the map bears no resemblance to actual operations.
   Schedule an annual review cycle and designate a system-change trigger for immediate
   updates (new SaaS vendor, new data flow, new product feature).

2. **Mapping only the obvious systems.** Enterprise systems (Salesforce, SAP, HRIS) get
   documented; departmental Excel sheets, personal Google Drive exports, contractor-managed
   databases, and Slack channels are missed. Shadow IT holds personal data. Always ask
   stakeholders: "What systems or files do YOU personally use that might hold customer
   or employee data?"

3. **Using generic data category descriptions.** Writing "customer data" instead of
   "name, email address, phone number, purchase history, shipping address." EDPB and
   national DPAs consistently cite vague category descriptions as a primary deficiency.
   Enumerate fields.

4. **Conflating data sensitivity tiers.** Recording health data, name, and email as
   the same category without flagging the health data as special-category requiring
   Art. 9 conditions. Sensitivity drives legal basis requirements, security controls,
   DPIA triggers, and data subject rights — conflation leads to systematic under-protection.

5. **Setting retention as "indefinite" or "as long as needed."** This fails the storage
   limitation principle and makes DSAR erasure requests impossible to fulfill. Every
   processing activity must have a specific retention trigger (e.g., "contract end + 5
   years") and a documented deletion method.

6. **Missing the 250-employee exemption misunderstanding.** Most organizations under
   250 employees still need a full RoPA because the Art. 30(5) exemption only applies
   to processing that is occasional, does not carry risk to rights/freedoms, and does
   not involve special-category or criminal data — conditions that exclude virtually
   all normal business operations.

7. **Completing DPA checkbox without substantive review.** Recording "DPA: Yes" without
   checking whether the DPA: (a) covers the specific data categories in scope, (b) lists
   or authorizes all subprocessors, (c) uses current SCC versions post-2021, (d) includes
   Art. 28(3)(c) audit rights. A defective DPA provides no protection in enforcement.

8. **Failing to identify all cross-border transfers.** Organizations map their primary
   CRM as "EU-hosted" and miss that the CRM's US-based support team accesses EU data,
   the backup region is in Singapore, and the AI feature trains on data in the US.
   Every data path — including subprocessor paths, support access, backups, and ML
   training — is a potential transfer requiring legal mechanism coverage.

9. **Not flagging automated decision-making and profiling.** Lead scoring, segmentation,
   and recommendation engines are automated decision-making. If they produce legally
   significant effects (credit decisions, employment decisions, insurance pricing),
   Art. 22 applies: DPIA is mandatory, transparency notice is required, the right not
   to be subject to the decision must be provided. Missing these triggers cascades into
   undefended DPIA gaps.

10. **Omitting special-category data from the map.** Wellness apps, biometric access
    systems, employee disability accommodations, diversity surveys, and criminal background
    checks all process Art. 9 data. Privacy teams focus on "data" in IT systems and miss
    "data" in physical processes, paper forms, and legacy HR files.

11. **Losing consent records.** Processing on consent requires proving consent was validly
    obtained. If the consent log system is deleted, migrated, or simply not queryable by
    data subject, the basis is unenforceable and DSAR responses cannot be defended. Map
    the consent repository as carefully as the data itself.

12. **Ignoring third-party data entanglement.** Email systems, shared documents, and
    ticketing tools contain data about people who did not submit a DSAR. During DSAR,
    third-party data must be redacted (GDPR Art. 15(4)), but you cannot redact what
    you have not mapped. Pre-map the entanglement problem (not during a DSAR response).

13. **Treating data maps as internal-only documents.** Under GDPR Art. 58(1)(e), supervisory
    authorities can require access to the RoPA. The RoPA must function as a standalone
    document — no requirement to cross-reference policies, DPIAs, or other documents
    to be intelligible to a regulator. Do not assume the regulator will ask before they
    inspect.

14. **Failing to capture processor sub-processors.** Controllers need prior written
    authorization for every sub-processor a processor engages. Processor DPAs often list
    generic categories ("cloud infrastructure providers"). Audit each processor for their
    actual current sub-processor list, verify each is covered by your DPA or consent
    to the sub-processor, and log the date of last sub-processor list review.

15. **Misidentifying joint controllers.** When two organizations co-determine the purpose
    and means of processing (e.g., co-marketing campaign, joint recruitment process,
    shared platform analytics), they are joint controllers under GDPR Art. 26. A processor
    DPA does not cover joint controllership — a separate Joint Controller Agreement (JCA)
    is required defining each party's obligations. Misidentifying a joint controller as
    a processor exposes both organizations.

---

## Integration with the Compliance Skill Family

Data mapping is the foundational upstream input for four downstream compliance workflows.
Explicitly handoff from this skill to the appropriate downstream skill at the marked points:

```
┌────────────────────────────────────────────────────────────────┐
│              LEGALCODE DATA MAPPING WORKFLOW                   │
│  Output: RoPA (Processing Activity Register + Data Flow Docs)  │
│  Classification: GREEN / YELLOW / RED per activity             │
└──────────────┬─────────────────────────────────────────────────┘
               │
   ┌───────────┼──────────────────┬────────────────────┐
   │           │                  │                    │
   ▼           ▼                  ▼                    ▼
┌──────┐  ┌────────┐  ┌────────────────────┐  ┌────────────┐
│DPIA  │  │DSAR    │  │Cross-Border        │  │Breach      │
│Genera│  │Workflow│  │Transfer Assessment │  │Severity    │
│tor   │  │Builder │  │                    │  │Assessment  │
└──────┘  └────────┘  └────────────────────┘  └────────────┘
   ▲           ▲                  ▲                    ▲
   │           │                  │                    │
Activities  System +         Transfer flags      Special-category
flagged for  discovery      + destination       flags + data scope
DPIA trigger protocol       countries + SCCs    + sensitivity tier
```

### Handoff Protocols

**→ legalcode-dpia-generator**: Pass all activities flagged for DPIA (automated
decision-making with significant effects, large-scale special-category processing,
systematic monitoring). Include: processing purpose, data categories, recipients,
legal basis, special-category flag, and risk indicators from the Processing Activity
Register.

**→ legalcode-dsar-workflow-builder**: Make the complete System Inventory and Processing
Activity Register available as the DSAR discovery protocol. The data map defines the
scope of systems to query, the retention schedule to determine what must be preserved,
and the recipient matrix to identify third-party data that must be redacted.

**→ legalcode-cross-border-transfer-assessment**: Pass the Transfer Ledger (Part E) with
all flagged third-country transfers, the current legal mechanism for each, and the
supplementary measures in place. The transfer assessment will conduct full TIA
analysis per Schrems II methodology.

**→ legalcode-breach-severity-assessment**: Make the classification (Tier 1–4 sensitivity)
and special-category flags available for breach scope calculation. The severity assessment
uses the data map to calculate: number of affected data subjects, sensitivity of data
at risk, and applicable notification obligations across regimes.

---

## External Tool Integration

### With legalcode-mcp (preferred for legal research)

Use legalcode-mcp to verify:

- Current adequacy decisions for each destination country under each applicable regime
- EDPB guidance on RoPA format and mandatory fields (current version)
- National DPA guidance on specific RoPA requirements or sector-specific obligations
- Current status of Art. 30 exemptions and their scope
- Sub-processor listing requirements under current DPA templates

Mark all legalcode-mcp-verified citations as `[VERIFIED — legalcode-mcp]` in the audit trail.

### Without legalcode-mcp

Proceed using training-data knowledge and clearly mark:

- All adequacy decision references as `[VERIFY — adequacy decisions change]`
- All SCC version references as `[VERIFY — current SCC implementing decision]`
- All retention period references as `[VERIFY against current national law]`
- Note in Glass Box: `legalcode_mcp: "Not connected — all legal citations require verification"`

---

## Glass Box Audit Trail

Every completed data mapping exercise must include a Glass Box audit trail for regulator
defensibility and internal accountability:

```yaml
glass_box:
  skill_name: "legalcode-data-mapping-workflow"
  topic: "Records of Processing Activities (RoPA) and Data Flow Mapping"
  mapping_scope: "[Entire organization / Division: name / Product: name]"
  jurisdiction_primary: "[GDPR / UK GDPR / CCPA-CPRA / LGPD / Other]"
  jurisdiction_overlays: "[List additional applicable regimes]"
  sector_overlays: "[HIPAA / GLBA / FERPA / None]"
  mapping_dates: "[Start date] to [Completion date]"
  methodology: "[Interview-first / Questionnaire-first / Automated-scan-supplemented]"
  stakeholders_interviewed: "[Number] — [list roles, not names]"
  systems_assessed: "[Number] — [list system categories]"
  processing_activities_identified: "[N]"
  classification_summary:
    green: "[X] ([X/N]%)"
    yellow: "[Y] ([Y/N]%)"
    red: "[Z] ([Z/N]%)"
  cross_border_transfers_flagged: "[N] transfers to [M] destination countries"
  special_category_activities: "[N] activities with Art. 9 conditions documented"
  automated_decision_making_activities: "[N] activities; [K] trigger DPIA"
  processor_dpa_audit:
    compliant: "[N]"
    gaps_identified: "[M]"
    missing: "[K]"
  downstream_handoffs_triggered:
    dpia: "[N] activities — see Gap Log"
    transfer_assessment: "[N] transfers — see Transfer Ledger"
    dsar_discovery: "System Inventory and Retention Schedule provided"
    breach_assessment: "Sensitivity classification and special-category flags provided"
  legalcode_mcp: "[Connected / Not connected — citations marked [VERIFY]]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_primary_source: "GDPR Art. 30 (EUR-Lex); EDPB public guidance; CCPA Cal. Civ. Code; LGPD official statute"
  confidence: "HIGH — based on GDPR/primary regulator guidance; [JURISDICTION-SPECIFIC] markers applied"
  limitations:
    - "Does not constitute legal advice; all findings subject to qualified DPO/counsel review"
    - "[VERIFY] markers present — do not submit to regulators until all [VERIFY] items resolved"
    - "Snapshot mapping; refresh required annually or upon material system/process change"
    - "Automated decision-making classification based on stakeholder interviews; recommend technical validation"
    - "Consent record accessibility requires separate technical audit; not confirmed in this mapping"
    - "Sub-processor lists are as-reported by processors; recommend annual processor audit"
  reviewer: "AI-assisted — requires qualified DPO or privacy professional sign-off before RoPA adoption"
  review_date: "[Date of DPO review]"
  next_scheduled_review: "[Date + 365 days or upon material change]"
```

---

## Machine-Readable Output Format

For organizations importing the data map into privacy management platforms (OneTrust,
TrustArc, Privaci, Securiti, Osano, or custom platforms), produce the following
machine-readable export alongside the markdown deliverables:

### JSON Schema for Processing Activity

```json
{
  "activity_id": "PA-001",
  "category": "HR",
  "processing_purpose": "Employee onboarding and payroll processing",
  "legal_basis_gdpr_art6": "6(1)(b)",
  "legal_basis_detail": "Performance of employment contract",
  "art9_special_category": false,
  "art9_condition": null,
  "data_categories": [
    "name",
    "address",
    "national_id",
    "bank_details",
    "salary"
  ],
  "data_subject_categories": ["employees"],
  "storage_systems": [
    {
      "system_name": "BambooHR",
      "type": "SaaS",
      "location": "EU (AWS eu-west-1)",
      "cross_border": false
    }
  ],
  "external_recipients": [
    {
      "name": "ADP Payroll",
      "role": "processor",
      "dpa_status": "compliant",
      "dpa_date": "2024-03-01",
      "jurisdiction": "EU",
      "transfer_mechanism": "intra_EEA"
    }
  ],
  "retention": {
    "trigger": "employment_end",
    "period": "P7Y",
    "deletion_method": "secure_deletion",
    "statutory_override": "Tax Authority records requirement"
  },
  "automated_decision_making": "none",
  "dpia_required": false,
  "cross_border_transfer": false,
  "classification": "GREEN",
  "last_reviewed": "2026-03-01",
  "next_review": "2027-03-01"
}
```

### YAML Export for RoPA Summary

```yaml
ropa_summary:
  organization: "[Organization Name]"
  version: "1.0"
  created: "2026-03-01"
  jurisdiction_primary: "GDPR"
  jurisdiction_overlays: ["CCPA/CPRA", "UK GDPR"]
  total_activities: 15
  green: 8
  yellow: 5
  red: 2
  processing_activities:
    - id: "PA-001"
      status: "GREEN"
      purpose: "Employee onboarding"
      legal_basis: "6(1)(b)"
      special_category: false
      cross_border: false
      dpia_required: false
    - id: "PA-002"
      status: "YELLOW"
      purpose: "CRM prospect management"
      legal_basis: "6(1)(f)"
      lia_completed: false
      cross_border: true
      transfer_mechanism: "SCC_2021"
      tia_pending: true
      dpia_required: false
```

---

## Localization Notes

This skill is jurisdiction-agnostic. When localizing for specific regimes:

### EU GDPR Localization

- Apply Art. 30(1) for controller records; Art. 30(2) for processor records
- Include EDPB guidelines on transparency (01/2022) [VERIFY current version]
- Apply Member State-specific derogations (Art. 88 employment; Art. 89 research)
- Use EUR-Lex as primary citation source

### UK GDPR Localization (post-Brexit)

- Apply UK GDPR Art. 30 + DPA 2018 Schedule 2 exemptions
- Use ICO documentation guidance as primary operational reference
- Apply UK Addendum to EU SCCs (IDTA) or standalone UK IDTA for transfers
- Note: DUA Act 2025 amendments may affect exemptions — [VERIFY current ICO guidance]

### CCPA/CPRA Localization (California)

- No formal Art. 30-equivalent; but privacy policy + data inventory effectively required
- Apply CPPA regulations for data category schema (11 statutory categories)
- "Sensitive personal information" (SPI) = distinct from "personal information" — requires separate mapping
- 45-day deletion right; 45+45-day response deadline; annual refresh recommended
- [JURISDICTION-SPECIFIC] CPPA enforcement began July 2023; ongoing rulemaking

### LGPD Brazil Localization

- Art. 37: Controller must maintain RoPA of processing activities [VERIFY ANPD format guidance]
- Art. 5(X): Operator (processor) equivalent obligations
- ANPD may adopt specific RoPA format requirements — [VERIFY current ANPD guidance]
- Sensitive data (Art. 11 LGPD): requires explicit consent or qualified legal necessity

### Canada PIPEDA / Provincial Law Localization

- PIPEDA Schedule 1, Principle 1 (Accountability): de facto inventory required
- Québec Law 25 (in force from September 2023): stricter requirements; RoPA-equivalent mandatory
- Alberta PIPA + BC PIPA: substantially similar to PIPEDA
- [VERIFY current OPC/CPVP guidance on inventory requirements]

---

## Provenance

Created by Legalcode as an original synthesis (2026-03-01). Research basis: GDPR Art. 30
and related EDPB guidance, CCPA/CPRA Cal. Civ. Code, LGPD Art. 37, PIPEDA Schedule 1,
APPI Art. 24, and industry methodology from IAPP, ICO, and leading DPA practice guidance.
Agent-team research pipeline (structural analyst + prompt engineering analyst). No prior
version — new skill. Related skills informing this synthesis: `legalcode-dpia-generator`,
`legalcode-dsar-workflow-builder`, `legalcode-cross-border-transfer-assessment`,
`legalcode-legitimate-interest-assessment`.
