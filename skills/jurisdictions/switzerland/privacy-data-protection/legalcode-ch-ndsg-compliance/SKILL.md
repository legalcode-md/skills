---
name: legalcode-ch-ndsg-compliance
description: Switzerland revised Federal Act on Data Protection (nDSG / revDSG / FADP, SR 235.1, in force
  1 September 2023) compliance assessment. Use when an organisation needs to determine nDSG applicability,
  assess compliance posture against processing principles, information obligations, DPIA requirements,
  breach notification to the FDPIC, cross-border transfer safeguards, data processing agreement requirements,
  and criminal sanction exposure.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Switzerland revised Federal Act on Data Protection (nDSG / revDSG / FADP, SR 235.1, in force 1 September 2023) compliance assessment. Use when an organisation needs to determine nDSG applicability, assess compliance posture against processing principles, information obligations, DPIA requirements, breach notification to the FDPIC, cross-border transfer safeguards, data processing agreement requirements, and criminal sanction exposure. Covers: processing principles (Art. 6 nDSG), privacy by design/default (Art. 7), data security (Art. 8), processor contracts (Art. 9), ROPA (Art. 12), foreign representative (Art. 14), information obligations (Arts. 19–21), DPIA and prior FDPIC consultation (Arts. 22–23), breach notification threshold and timeline (Art. 24), data subject rights including access and portability (Arts. 25–28), cross-border transfers and Federal Council adequacy list (Arts. 16–17, Annex 1 DPO), criminal sanctions on natural persons (Arts. 60–62), cantonal law variations, and GDPR comparison for EU-facing operations. Produces compliance assessments with COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL classifications, prioritised remediation roadmaps, FDPIC notification readiness checklists, and criminal liability exposure analysis. Jurisdiction: Switzerland (federal nDSG) with cantonal variation notes.


# Swiss nDSG Compliance Assessment

_(Bundesgesetz über den Datenschutz / Loi fédérale sur la protection des données / SR 235.1)_

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance with the
> Swiss revised Federal Act on Data Protection (nDSG / revDSG / FADP, SR 235.1) and its implementing
> ordinance (Data Protection Ordinance / DPO / VDSG, SR 235.11). It does not constitute legal advice,
> regulatory guidance, or a compliance certification. The nDSG entered into force on 1 September 2023
> and implementing guidance from the FDPIC continues to evolve — verify all statutory references,
> thresholds, and current FDPIC factsheets before relying on them. AI-generated legal analysis carries
> hallucination risk for cited authority: any statutory references, FDPIC guidelines, or regulatory
> interpretations should be independently verified by a qualified Swiss data protection legal
> professional. Criminal sanctions under Arts. 60–62 nDSG can expose individual employees and
> executives to fines up to CHF 250,000 — engage qualified Swiss counsel before making decisions
> based on this output. Cantonal data protection laws are not covered by this skill for cantonal
> public-sector processing — consult the relevant cantonal data protection authority.

---

## Purpose and Scope

This skill assesses an organisation's compliance posture against the Swiss revised Federal Act on
Data Protection (nDSG, in force 1 September 2023). It covers the full nDSG obligation stack for
**private controllers and processors** operating in or toward Switzerland.

**Covers:**

- Applicability determination (private vs. federal body; extraterritorial scope; foreign representative
  obligation under Art. 14 nDSG)
- Processing principles compliance: lawfulness, good faith, proportionality, purpose limitation,
  accuracy, storage limitation (Art. 6 nDSG)
- Privacy by design and privacy by default (Art. 7 nDSG)
- Technical and organisational security measures (Art. 8 nDSG; Arts. 1–7 DPO)
- Processor contract (Auftragsbearbeitung) requirements (Art. 9 nDSG)
- Record of Processing Activities (ROPA) obligation and SME exemption (Art. 12 nDSG)
- Information obligations for direct and indirect data collection (Arts. 19–21 nDSG)
- Automated individual decisions and profiling obligations (Art. 21 nDSG)
- Data Protection Impact Assessment (DPIA) requirement and FDPIC consultation (Arts. 22–23 nDSG)
- Security incident and breach notification to FDPIC — threshold, timeline, content (Art. 24 nDSG;
  Art. 15 DPO)
- Data subject rights: access, rectification, portability — timelines and exceptions (Arts. 25–28 nDSG)
- Cross-border data transfer safeguards: Federal Council adequacy list, SCCs, BCRs, derogations
  (Arts. 16–17 nDSG; Annex 1 DPO)
- Sensitive personal data enhanced requirements (Art. 5(c) nDSG)
- High-risk profiling requirements (Art. 5(g) nDSG)
- Criminal sanction exposure under Arts. 60–62 nDSG (natural persons; max CHF 250,000)
- Data Protection Advisor (DPO) voluntary appointment incentives (Art. 23(4) nDSG)
- Cantonal data protection law applicability and cantonal variation notes
- GDPR alignment assessment for organisations with dual Swiss/EU obligations

**Does not:**

- Cover processing by federal public bodies (governed by nDSG but with different legal basis rules)
- Provide canton-by-canton detailed legal opinions on cantonal data protection laws
- Replace a formal compliance audit by a qualified Swiss data protection professional
- Constitute legal advice on criminal prosecution risk or individual criminal liability
- Assess compliance with sector-specific Swiss laws (banking secrecy, Finanzmarktaufsicht,
  health data regulations) beyond the nDSG framework
- Cover GDPR compliance in detail (see `legalcode-gdpr-legal-basis-assessment` and related skills)

**Related skills:**

- `legalcode-cross-border-transfer-assessment` — multi-regime (GDPR/UK GDPR/nDSG) transfer impact
  assessment and SCC selection
- `legalcode-dpia-generator` — GDPR Art. 35 DPIA; adaptable for nDSG Art. 22 requirements
- `legalcode-breach-regulatory-notification-drafter` — multi-regime breach notification templates
- `legalcode-data-processing-agreement-drafter` — GDPR Art. 28 DPAs; adaptable with nDSG Art. 9 overlay
- `legalcode-ropa-generator` — Record of Processing Activities; adaptable for nDSG Art. 12

---

## Jurisdiction and Governing Law

**Primary law**: Federal Act on Data Protection (FADP / nDSG / revDSG), SR 235.1, 25 September 2020
(AS 2022 491); in force **1 September 2023**. No transitional period — immediate full compliance required.

**Implementing ordinance**: Data Protection Ordinance (DPO / VDSG / Ordonnance sur la protection des
données), SR 235.11; also in force 1 September 2023.

**Adequacy**: Switzerland holds unconditional EU adequacy status (confirmed January 2024 under GDPR
standard). Swiss–U.S. Data Privacy Framework (Swiss-U.S. DPF) effective 15 September 2024 for
US-bound transfers.

**Cantonal laws**: Each of Switzerland's 26 cantons has its own data protection law governing cantonal
and communal public bodies. This skill covers the federal nDSG (private controllers). Cantonal
variations are noted in the Cantonal Considerations section.

**Official text**: https://www.fedlex.admin.ch/eli/cc/2022/491/en

**Supervisory authority**: Federal Data Protection and Information Commissioner (FDPIC / EDÖB /
Préposé fédéral à la protection des données et à la transparence / PFPDT). Website: edoeb.admin.ch

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
organisation's profile, the workflow pauses and asks when:

- The answer determines which nDSG obligations apply (e.g., SME ROPA exemption, DPIA threshold)
- Multiple valid compliance approaches exist (e.g., SCC vs. BCR for cross-border transfers)
- Risk classification depends on business context the user must supply
- A finding requires legal judgment beyond AI capability

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

### Step 1: Accept Organisational Profile

Accept the compliance assessment input in any of these formats:

- **Completed questionnaire**: Responses to the context-gathering questions in Step 2
- **Existing privacy documentation**: Privacy notices, DPAs, ROPA extracts, DPIA records
- **Free-form description**: Organisation type, data processing activities, and known concerns
- **Specific topic**: A single nDSG area to assess (e.g., "assess our breach notification readiness")

If no profile is provided, proceed directly to Step 2 to gather context.

### Step 2: Gather Organisational Context

**⟁ CLARIFY** — Before beginning the assessment, gather this information. Present as structured
options where possible. Skip questions already answered by the input.

1. **Organisation type and size**:
   - Options: Private company (large, >250 FTE), Private company (SME, ≤250 FTE), Non-profit,
     Partnership/sole trader, Foreign entity with Swiss operations, Public sector (cantonal/federal)
   - _Why this matters_: Determines SME ROPA exemption eligibility; cantonal law applicability for
     public bodies; extraterritorial scope thresholds.

2. **Processing profile** — does the organisation process any of the following?
   - Sensitive personal data (health, biometric, genetic, racial/ethnic origin, religious/political
     views, trade union membership, social assistance, administrative/criminal proceedings)
   - Large-scale processing (thousands or more data subjects or records)
   - Systematic public surveillance (CCTV, location tracking, behavioural monitoring)
   - High-risk profiling (automated analysis assessing essential personality aspects)
   - Data from Swiss residents targeted from abroad (extraterritorial scope trigger)
   - _Why this matters_: Determines DPIA obligation, FDPIC consultation requirement, enhanced
     security requirements, and CLARIFY points throughout the assessment.

3. **Cross-border transfers** — does the organisation transfer personal data outside Switzerland?
   - Options: No transfers outside Switzerland, Transfers only to EU/EEA (adequacy), Transfers to US
     (DPF status relevant), Transfers to other countries (list if known), Unknown — needs mapping
   - _Why this matters_: Determines adequacy analysis, SCC requirement, and transfer impact
     assessment obligations.

4. **Existing compliance infrastructure**:
   - Options: Existing GDPR-compliant programme (adapt for nDSG), Partial privacy programme
     (some documentation), Starting from scratch, Existing nDSG programme (gap assessment needed)
   - _Why this matters_: Calibrates the assessment depth; GDPR-compliant organisations often need
     targeted nDSG-specific additions rather than a full programme build.

5. **Assessment scope**:
   - Options: Full nDSG compliance assessment (all domains), Priority gaps only (known weaknesses),
     Specific domain (breach notification / DPIAs / cross-border transfers / data subject rights /
     criminal liability exposure)
   - _Why this matters_: Determines whether to run the full 10-domain assessment or focus on
     specific risk areas.

6. **Data Protection Advisor (DPO)**:
   - Options: Appointed and registered with FDPIC, Appointed but not registered, Under consideration,
     Not appointed — no plans, Federal body (mandatory DPO)
   - _Why this matters_: Registered DPO provides exemption from mandatory FDPIC consultation under
     Art. 23(4) nDSG — a critical compliance incentive.

If the user provides partial context, proceed with stated assumptions. State all assumptions
explicitly at the start of the assessment output.

### Step 3: Load Legal Authority Reference

Use **legalcode-mcp** to retrieve current nDSG statutory text, FDPIC guidelines, and DPO ordinance
provisions relevant to the assessment scope.

**If legalcode-mcp is connected:**

Search for:

- `nDSG Art. 5-28 definitions and obligations Switzerland FADP`
- `FDPIC breach notification guidelines Art. 24 nDSG`
- `Switzerland cross-border transfer adequacy DPO Annex 1 2024`
- `nDSG DPIA Art. 22 23 high risk processing Switzerland`
- `nDSG criminal sanctions Art. 60 61 62 CHF 250000`
- `Switzerland data protection cantonal law variations`

Save results to `/tmp/legalcode-ch-ndsg-research.md` for reference throughout the assessment.

**If legalcode-mcp is not connected:**

Proceed using the legal framework embedded in this skill. Mark all statutory references as [VERIFY]
to indicate they should be confirmed against current FDPIC guidance and official text at
fedlex.admin.ch. Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`.

### Step 4: Applicability Determination

Before assessing compliance domains, confirm that the nDSG applies and identify the full scope
of obligations.

#### 4a. Territorial Scope

**Primary scope (Art. 3 nDSG)**: The nDSG applies to processing of personal data by:

- Private persons or federal bodies with activities in Switzerland
- Any controller with effects in Switzerland (extraterritorial reach, mirroring GDPR)

**Foreign representative obligation (Art. 14 nDSG)**: A foreign controller must appoint a
Swiss-based representative if it:

1. Processes data of persons in Switzerland on a regular basis
2. Processes data involving large-scale processing or high risk
3. Offers goods/services to Swiss persons or monitors their behaviour

Failure to appoint: reportable violation under Art. 61(c) nDSG (criminal sanction risk).

Assess: | Applicable | Not Applicable | Uncertain [VERIFY]

#### 4b. Private vs. Federal Body

Private controllers operate under a **permissive default** — processing is permitted unless it
violates the processing principles or the specific prohibitions (sensitive data, high-risk profiling
without justification). A legal basis/justification is required only when:

- Processing violates a key principle (proportionality, purpose limitation, etc.)
- Processing is contrary to the express wishes of the data subject
- Sensitive personal data is disclosed to third parties
- High-risk profiling is performed

Federal bodies always require a statutory basis for every processing activity.

#### 4c. SME ROPA Exemption (Art. 12(5) nDSG)

Private organisations with **fewer than 250 employees** AND **low-risk processing** (no sensitive
personal data, no high-risk profiling, no large-scale processing) are **exempt from the ROPA
obligation** under Art. 12(5) nDSG.

**⟁ CLARIFY** — If the organisation has ≤250 employees: confirm whether any of the following
exist (if yes, the exemption does not apply): sensitive personal data; high-risk profiling;
large-scale regular data processing.

### Step 5: Run the 10-Domain Compliance Assessment

Assess compliance across all applicable domains. For each domain, produce findings classified
using the four-tier system (see Severity Classification below). Where insufficient information
is available, flag as [INSUFFICIENT INFORMATION — REQUEST FROM CLIENT].

---

#### Domain 1: Processing Principles (Art. 6 nDSG)

Assess compliance with each of the seven processing principles:

| Principle              | Art. 6 Ref  | Assessment Questions                                                             | Common Failures                                                                  |
| ---------------------- | ----------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Lawfulness**         | Art. 6(1)   | Is data obtained through lawful means? No deception or coercion?                 | Scraping without notice; purchasing data without provenance verification         |
| **Good faith**         | Art. 6(1)   | Is processing transparent and honest? No hidden secondary use?                   | Undisclosed analytics; dark patterns in consent flows                            |
| **Proportionality**    | Art. 6(2)   | Is only necessary data collected for the stated purpose? Minimum data collected? | Over-collection "just in case"; excessive retention; unnecessary fields          |
| **Purpose limitation** | Art. 6(3)   | Is data used only for the specified purpose? Secondary use compatible?           | Using HR data for marketing; sharing customer data with unrelated group entities |
| **Accuracy**           | Art. 6(4)   | Are correction procedures in place? Inaccurate data corrected or deleted?        | No rectification workflow; outdated data retained without review                 |
| **Storage limitation** | Art. 6(5)   | Are retention periods defined per data category? Destruction process in place?   | Indefinite retention defaults; no deletion triggers; backup data excluded        |
| **Security**           | Art. 8 nDSG | See Domain 3                                                                     | —                                                                                |

**Privacy by Design and Default (Art. 7 nDSG)**:

- Design: Are data minimisation, pseudonymisation, and access controls built in from project inception?
- Default: Are the most privacy-protective settings the default configuration (not opt-in)?
- Documentation: Is the privacy-by-design process documented for new processing activities?

---

#### Domain 2: Information Obligations (Arts. 19–21 nDSG)

**Scope**: The nDSG requires controllers to inform data subjects whenever personal data is
collected — regardless of sensitivity. This is broader than the old 1992 FADP.

**Mandatory minimum information (Art. 19 nDSG)**:
Assess whether privacy notices include all four required elements:

| Required Element                        | Art. 19 Ref   | Present? | Quality? |
| --------------------------------------- | ------------- | -------- | -------- |
| Controller identity and contact details | Art. 19(2)(a) |          |          |
| Purpose(s) of processing                | Art. 19(2)(b) |          |          |
| Recipients or categories of recipients  | Art. 19(2)(c) |          |          |
| Countries of transfer and safeguards    | Art. 19(2)(d) |          |          |

**Timing requirements**:

- Direct collection: at time of collection
- Indirect collection (data from third parties): within 30 days or before first disclosure

**Automated decisions notice (Art. 21 nDSG)**:
Assess whether: any automated-only decisions with legal or significant effects exist; data subjects
are informed; right to express viewpoint is provided; human review mechanism is available.

**Exceptions (Art. 20 nDSG)** — Assess whether any exemptions claimed are valid:

- Data subject already possesses the information
- Legal basis for restricting disclosure (professional secrecy, trade secrets)
- Providing information is impossible or disproportionate (indirect collection only)
- Conflicting overriding private or public interest

**nDSG vs. GDPR comparison note**: nDSG information obligations are less prescriptive than GDPR
Arts. 13–14. The mandatory list is shorter. However, the scope (all personal data) is now
equivalent. Organisations with GDPR-compliant notices typically satisfy nDSG minimum requirements —
but must verify that transfer destination countries are disclosed.

---

#### Domain 3: Data Security (Art. 8 nDSG; Arts. 1–7 DPO)

The DPO requires a **risk-based approach** to security, with measures commensurate to the risk.

**Required assessment areas**:

| Security Domain                | DPO Reference | Assessment Questions                                                                                   |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------ |
| Risk assessment                | Art. 1 DPO    | Is a formal risk assessment performed per processing activity? Documented?                             |
| Access controls                | Art. 2 DPO    | Are access rights restricted to authorised personnel? Role-based access? Privileged access management? |
| Pseudonymisation/anonymisation | Art. 3 DPO    | Is pseudonymisation used where appropriate? Anonymisation tested for re-identification risk?           |
| Encryption                     | Art. 4 DPO    | Is personal data (especially sensitive) encrypted in transit and at rest?                              |
| Availability/integrity         | Art. 5 DPO    | Are backup procedures in place? Business continuity plans? Disaster recovery tested?                   |
| Processor security oversight   | Art. 6 DPO    | Are processors assessed for security measures? Contractual security obligations imposed?               |
| Incident detection             | Art. 7 DPO    | Are monitoring and intrusion detection systems in place?                                               |

**Sensitive data enhanced requirements**:

- Access controls ensuring only authorised personnel can access sensitive data
- Encryption mandatory for electronically processed sensitive data
- Physical security for paper-based sensitive records
- Documented employee confidentiality obligations

**⟁ CLARIFY** — If sensitive personal data is processed: identify specific data categories
(health/genetic/biometric/political/religious/trade union/social assistance/criminal proceedings)
and confirm enhanced security measures are in place for each.

---

#### Domain 4: Record of Processing Activities — ROPA (Art. 12 nDSG)

**Obligation**: Maintain a written inventory of all processing activities.

**SME exemption**: Organisations with ≤250 employees and low-risk processing are exempt
(Art. 12(5) nDSG) — confirm exemption eligibility first.

**Mandatory ROPA content (Art. 12 nDSG)**:

| Field                                    | Required for Controller | Required for Processor |
| ---------------------------------------- | ----------------------- | ---------------------- |
| Name and contact details                 | ✓                       | ✓                      |
| Type of personal data processed          | ✓                       | ✓                      |
| Categories of data subjects              | ✓                       | —                      |
| Categories of recipients                 | ✓                       | —                      |
| Destination countries and safeguards     | ✓                       | ✓                      |
| Retention periods or criteria            | ✓                       | ✓                      |
| General description of security measures | ✓                       | ✓                      |
| Processing purposes                      | ✓                       | —                      |

**Best practice additions** (recommended but not mandatory): data classification; legal
justification per processing activity; DPIA flags; incident history; sub-processor list.

**Assessment questions**:

- Does a current, written ROPA exist?
- Is it maintained and reviewed at defined intervals (at minimum annually; best practice: upon any
  new processing activity)?
- Does it cover all processing activities including those by processors?
- Are transfer safeguards documented per destination country?

---

#### Domain 5: Processor Contracts / Data Processing Agreements (Art. 9 nDSG)

**Requirement**: Written agreement with every processor mandating:

1. Processing only on controller instructions
2. Implementation of appropriate security measures (Art. 8/DPO standards)
3. Sub-processor engagement only with prior controller consent

**Assessment framework**:

| Requirement               | Art. 9 nDSG  | Assessment Questions                                                           |
| ------------------------- | ------------ | ------------------------------------------------------------------------------ |
| Written DPA in place      | Art. 9(1)    | Does a signed written agreement exist for every processor?                     |
| Instruction restriction   | Art. 9(1)(a) | Does the DPA restrict the processor to controller instructions only?           |
| Security obligations      | Art. 9(1)(b) | Are security measures required by contract? Do they meet Art. 8/DPO standards? |
| Sub-processor consent     | Art. 9(3)    | Is prior controller consent required before any sub-processor engagement?      |
| Sub-processor obligations | Art. 9(3)    | Are sub-processors bound to the same obligations as the primary processor?     |

**Note on GDPR DPA compatibility**: GDPR Art. 28-compliant DPAs typically satisfy nDSG Art. 9
requirements, as nDSG requirements are less prescriptive. However, confirm that nDSG references
are included in the governing law and that the DPA covers all Swiss data subjects.

**Processor inventory**: Is there a complete inventory of all processors? Are DPAs in place for
each? When were they last reviewed?

---

#### Domain 6: Data Protection Impact Assessment — DPIA (Arts. 22–23 nDSG)

**Mandatory DPIA triggers (Art. 22 nDSG)** — A DPIA is required when processing is likely to
result in a high risk to the personality or fundamental rights of data subjects.

**Absolute mandatory triggers** (Art. 22(2) nDSG):

| Trigger                                             | Threshold                                   |
| --------------------------------------------------- | ------------------------------------------- |
| Large-scale sensitive personal data processing      | Large scale + sensitive data (any category) |
| Systematic large-scale surveillance of public areas | Any systematic public area monitoring       |

**Risk-elevating factors** (not absolute triggers but elevating risk):

- New technologies not previously assessed
- Combination of datasets creating new risk
- Geographic scope across multiple jurisdictions
- Large number of data subjects affected
- Irreversible harm potential

**DPIA methodology checklist (Art. 22 nDSG)**:

- [ ] Processing activities described in detail
- [ ] Risks to personality and fundamental rights evaluated
- [ ] Risk mitigation measures identified and documented
- [ ] Residual risks assessed after mitigation
- [ ] DPIA completed **before** processing commences

**Prior FDPIC consultation (Art. 23 nDSG)**:

If DPIA reveals a **high residual risk** despite mitigation, the controller must consult the FDPIC
before commencing.

**Key exemption (Art. 23(4) nDSG)**: Private controllers who have appointed a **registered Data
Protection Advisor (DPO)** and consult them regarding the high-risk processing are **exempt from
mandatory FDPIC consultation**. This is the primary regulatory incentive for voluntary DPO
appointment. Confirm: (1) DPO is appointed; (2) DPO is registered with FDPIC; (3) DPO consultation
is documented.

**Assessment questions**:

- Has a DPIA process been established?
- Are all absolute-trigger processing activities identified?
- Are DPIAs completed before new high-risk processing launches?
- Where high residual risk exists: is FDPIC consulted, or is registered DPO exemption available?
- Are DPIA records maintained and reviewed when processing changes?

---

#### Domain 7: Breach Notification (Art. 24 nDSG; Art. 15 DPO)

**Breach definition (Art. 5(h) nDSG)**: Personal data is "breached" when accidentally or
unlawfully lost, deleted, destroyed, modified, or made accessible to unauthorised persons.

**Notification threshold**: Controllers must notify the FDPIC only when a breach poses a
**likely high risk to the personality or fundamental rights** of data subjects (Art. 24(1) nDSG).

> This is a **higher threshold than GDPR** (which requires notification for any "risk"). Not every
> breach triggers FDPIC notification — a high-risk threshold applies.

**FDPIC notification timeline**: "**As soon as possible**" after becoming aware. No explicit
72-hour numeric deadline exists in nDSG (unlike GDPR). In practice, 72 hours is the market
benchmark, but it is not legally mandated.

**FDPIC notification content requirements (Art. 15 DPO)**:

| Required Element                                                    | Art. 15 DPO |
| ------------------------------------------------------------------- | ----------- |
| Nature of the breach                                                | ✓           |
| Date of occurrence and date of discovery                            | ✓           |
| Categories and approximate number of affected data subjects         | ✓           |
| Categories and approximate number of affected personal data records | ✓           |
| Contact details of DPO or other contact person                      | ✓           |
| Likely consequences of the breach                                   | ✓           |
| Measures taken or proposed to address the breach                    | ✓           |

**Notification to data subjects (Art. 24(4) nDSG)**: Notify affected data subjects only when
**necessary for their protection** or when the **FDPIC requests** notification. There is no
automatic obligation to notify all affected data subjects.

**Processor reporting obligation**: Processors must notify the controller of any breach regardless
of the risk level. Ensure processor DPAs include this obligation.

**FDPIC reporting portal**: Notifications must be submitted via the FDPIC's DataBreach portal
at edoeb.admin.ch.

**Assessment questions**:

- Is there a documented breach detection and classification procedure?
- Is there a documented FDPIC notification workflow targeting "as soon as possible"?
- Are all breaches documented regardless of notification threshold (accountability principle)?
- Do DPAs require processors to notify the controller promptly?
- Is the FDPIC DataBreach portal registered and accessible to the incident response team?
- Is a data subject notification procedure established for high-risk breach scenarios?

---

#### Domain 8: Data Subject Rights (Arts. 25–28 nDSG)

**⟁ CLARIFY** — Confirm the volume of data subject requests historically received to calibrate
the depth of assessment for rights response workflows.

**Right of access (Art. 25 nDSG)**:

| Requirement                | Details                                                                                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Confirmation of processing | Must confirm if personal data is being processed                                                                                                                        |
| Information provided       | Controller identity; data categories; purposes; retention periods; data origin; recipient categories; automated decision information; transfer countries and safeguards |
| Timeline                   | 30 days (in principle); extendable for complex requests                                                                                                                 |
| Cost                       | Free; max CHF 300 only in exceptional circumstances per DPO rules                                                                                                       |
| Restrictions               | May refuse for professional secrecy, legal obligations, manifestly unfounded/vexatious requests (Arts. 26–27 nDSG)                                                      |

**Right to rectification (Art. 32(1) nDSG)**:

- Data subjects may demand correction of inaccurate data
- Exceptions apply for archival purposes or legal prohibition

**No standalone right to erasure** — critical nDSG divergence from GDPR:

> The nDSG does not provide a standalone Art. 17 GDPR-equivalent right to erasure. Erasure as
> a remedy is available through Swiss civil law personality rights claims (Art. 28 ZGB / Swiss
> Civil Code) for unlawful processing — but it requires court proceedings, not a direct
> administrative request. Do not implement GDPR-style erasure workflows as an nDSG right.

**Right to data portability (Art. 28 nDSG)**:

| Condition                                                                   | Requirement                                                                                |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Processing is automated                                                     | Required                                                                                   |
| Based on consent **or** directly related to contract conclusion/performance | Required (either/or)                                                                       |
| Format                                                                      | Commonly used electronic format (JSON, CSV, ODT preferred; proprietary formats prohibited) |
| Timeline                                                                    | 30 days; free of charge                                                                    |
| Transfer to other controller                                                | Available on request; receiving controller not obligated to accept                         |

**Right to object to automated decisions (Art. 21 nDSG)**:

- Express viewpoint regarding automated-only decisions
- Request human review

**Assessment questions**:

- Is a documented access request workflow in place with 30-day response SLA?
- Is a rectification procedure in place?
- Is there a documented position on erasure (civil law remedy only — not an administrative right)?
- Is a data portability workflow in place for consent-based and contract-based automated processing?
- Is a human review procedure in place for automated decisions?
- Are request logs maintained for accountability?

---

#### Domain 9: Cross-Border Data Transfers (Arts. 16–17 nDSG; Annex 1 DPO)

**Adequacy mechanism**: The **Federal Council** (not FDPIC) makes binding adequacy determinations
published in Annex 1 of the DPO. Last updated: September 2024.

**Adequate countries (Annex 1 DPO — as of September 2024)**:

- **Full adequacy**: All EU/EEA member states (including Iceland, Norway, Liechtenstein); Andorra,
  Argentina, Gibraltar, Guernsey, Isle of Man, Israel, Jersey, Monaco, New Zealand, Faroe Islands,
  Uruguay, and other full-adequacy third countries.
- **Conditional adequacy**:
  - **Canada**: Under PIPEDA (federal) and equivalent provincial laws (QC, BC, AB only)
  - **United Kingdom**: Adequate including for Directive 2016/680 transfers
  - **United States**: Adequate **only for Swiss-U.S. DPF certified organisations** (effective
    15 September 2024); non-DPF US entities require SCCs or other safeguards

[VERIFY: Check current Annex 1 DPO at fedlex.admin.ch for the most current adequacy list before
advising on any specific transfer. The list is updated by Federal Council regulation.]

**Safeguards for non-adequate countries (Art. 16(2); Art. 17 nDSG)**:

| Mechanism                           | Notes                                                                                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Standard Contractual Clauses (SCCs) | FDPIC recognises EU Commission SCCs (2021 version) with Swiss-specific adaptations; no FDPIC pre-notification required |
| Binding Corporate Rules (BCRs)      | Requires FDPIC approval (or pre-approval by adequate country DPA)                                                      |
| FDPIC-approved other guarantees     | 90-day FDPIC review window                                                                                             |
| Derogations (Art. 17 nDSG)          | Explicit consent; contract performance; vital interests; public register; public interest with FDPIC notification      |

**Swiss SCC adaptations** (when using EU SCCs for Switzerland-origin transfers):

- Replace all GDPR references with FADP/nDSG references
- Designate FDPIC as competent supervisory authority
- Adapt "member state" references to permit Swiss data subjects to enforce rights at habitual
  residence
- Adjust governing law and jurisdiction clauses to Swiss law
- Conduct Schrems II-analogous transfer impact assessment for jurisdictions with disproportionate
  government surveillance risks

**Assessment framework**:

- Are all cross-border data flows mapped (controller, processor, sub-processor)?
- For each destination country: adequacy status confirmed per current Annex 1 DPO?
- For non-adequate countries: appropriate safeguards in place (SCCs, BCRs)?
- For US transfers: DPF certification status of each US recipient verified?
- Swiss SCC adaptations implemented where EU SCCs are used?
- Transfer records maintained in ROPA?

---

#### Domain 10: Criminal Sanction Exposure (Arts. 60–62 nDSG)

> This domain assesses criminal liability risk to **natural persons** (employees, executives,
> board members, compliance officers, CISOs). The nDSG's criminal sanction model is
> structurally different from GDPR — fines attach to **individuals**, not organisations.
> This assessment identifies violation-prone areas; do not rely on it for legal defence.
> Engage qualified Swiss counsel for criminal liability advice.

**Criminal sanctions structure (Arts. 60–62 nDSG)**:

| Provision   | Violations Covered                                                                                                                             | Max Fine                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **Art. 60** | Violation of information/access obligations; providing false privacy notices; falsifying data subject request responses                        | CHF 250,000 per violation |
| **Art. 61** | Failure to maintain data security; unlawful cross-border transfers; engaging processors without written DPA; failure to perform required DPIAs | CHF 250,000 per violation |
| **Art. 62** | Breach of professional confidentiality; disclosing confidential personal data to unauthorised parties                                          | CHF 250,000 per violation |

**Key structural features**:

- Sanctions apply to **natural persons** who committed the wilful violation — employees,
  executives, board members, CISOs, compliance officers
- **Intent requirement**: Contingent intent (_dolus eventualis_) is sufficient; negligence is not
  criminal under these provisions
- **Subsidiary entity liability**: If the fine would not exceed CHF 50,000 and identifying the
  individual would require disproportionate investigation, the fine may be imposed on the legal entity
- **Prosecution**: The FDPIC cannot file criminal complaints directly but may report to cantonal
  prosecution authorities. Cantonal prosecuting authorities initiate proceedings.
- **Note**: General principle violations and breach notification failures (late or missed FDPIC
  notification) are **not** covered by the criminal sanction provisions directly

**High-risk individual exposure areas** (automatic criminal sanction risk review triggers):

| Violation Risk Area                                                | Provision | Individual Role Most at Risk               |
| ------------------------------------------------------------------ | --------- | ------------------------------------------ |
| False or incomplete privacy notices (Art. 19 nDSG)                 | Art. 60   | Head of Marketing, Privacy Officer         |
| Falsified data subject access responses                            | Art. 60   | Privacy Officer, Customer Service Director |
| Unlawful cross-border transfers (no safeguards)                    | Art. 61   | CISO, CTO, Privacy Officer                 |
| Missing written processor DPAs                                     | Art. 61   | Head of Procurement, Privacy Officer       |
| Failure to implement data security measures                        | Art. 61   | CISO, CTO, Board                           |
| Failure to conduct required DPIA                                   | Art. 61   | Privacy Officer, Product Team Lead         |
| Confidentiality breach (sensitive data leak to unauthorised party) | Art. 62   | CISO, employee with access                 |

**⟁ CLARIFY** — For each identified violation risk area: confirm whether the responsible natural
person(s) are aware of their individual criminal exposure and whether governance controls exist
to prevent wilful violations.

---

### Step 6: Assess Data Protection Advisor (DPO) Incentive

The nDSG does not mandate DPO appointment for private controllers. However, a registered DPO
unlocks the **FDPIC consultation exemption** — the primary structural incentive.

| Factor                     | DPO Not Appointed                    | DPO Appointed and Registered                 |
| -------------------------- | ------------------------------------ | -------------------------------------------- |
| DPIA high residual risk    | Must consult FDPIC before processing | Exempt from FDPIC consultation (Art. 23(4))  |
| Compliance signal          | Standard                             | Enhanced — signals organisational commitment |
| FDPIC investigation stance | No formal effect                     | May reduce escalation risk in practice       |
| Required for?              | No                                   | No (private sector)                          |

**Appointment requirements** (for FDPIC consultation exemption):

1. DPO possesses required expert knowledge in data protection
2. DPO exercises functions in a professionally independent manner (no conflict of interest)
3. DPO contact details published (ideally in privacy notice)
4. DPO registered with FDPIC via the FDPIC online portal

**Recommendation**: Private organisations conducting high-risk processing should seriously
consider DPO appointment for the FDPIC consultation exemption benefit alone.

### Step 7: Cantonal Considerations

The nDSG applies to **private controllers**. Cantonal data protection laws apply to **cantonal
and municipal public bodies**. However, organisations should assess cantonal law where they:

- Process personal data as a processor on behalf of cantonal authorities
- Operate as contractors to cantonal hospitals, universities, or government agencies
- Are subject to cantonal employment law (cantonal labour law may interact with data protection)

**Key cantonal authorities to be aware of**:

- Zurich: _Beauftragter für Datenschutz und Information_ (BDI)
- Geneva: _Préposé cantonal à la protection des données_ (PPDT)
- Bern: Cantonal Data Protection Commissioner
- All 26 cantons have designated cantonal data protection supervisory authorities

**⟁ CLARIFY** — If the organisation processes data for or on behalf of cantonal or communal
bodies: identify which cantons are involved and confirm whether the relevant cantonal data
protection law has been separately assessed.

### Step 8: GDPR Comparison for Dual-Obligation Organisations

Many Swiss-based organisations are also subject to GDPR (EU data subjects). Produce a divergence
summary where applicable:

| Area                          | nDSG Position                                                                         | GDPR Position                                | Action Required                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Legal basis                   | Not required for all private processing; justification for restricted categories only | Six mandatory legal bases for all processing | Maintain GDPR legal basis register; nDSG does not require the same structure but document justifications |
| Right to erasure              | Not a standalone right; civil law remedy only                                         | Art. 17 standalone right                     | Maintain GDPR erasure workflow; document nDSG civil law position separately                              |
| DPO mandatory threshold       | Not mandatory for private sector                                                      | Mandatory for many organisations             | Assess GDPR DPO obligation independently; one DPO can cover both                                         |
| Breach notification timeline  | "As soon as possible" — no numeric deadline                                           | 72 hours to supervisory authority            | Design workflow to meet 72-hour GDPR threshold; satisfies nDSG "as soon as possible"                     |
| Breach notification threshold | Likely HIGH risk                                                                      | Any risk                                     | GDPR triggers more notifications; nDSG threshold is higher                                               |
| Processor DPA content         | Minimal mandatory content                                                             | Detailed Art. 28 mandatory clauses           | Use GDPR Art. 28-compliant DPAs; add FADP references                                                     |
| Information obligations       | Four mandatory elements                                                               | Exhaustive Arts. 13–14 lists                 | Use GDPR-compliant notices; add cross-border transfer disclosure for all transfers                       |
| Criminal sanctions            | Natural persons; CHF 250,000                                                          | Organisations; EUR 20M/4% turnover           | Govern individual conduct; both regimes apply simultaneously                                             |

---

## Severity Classification

Every finding is classified using the four-tier system:

| Tier       | Label             | Definition                                                                                                                                                                                                                                                       | Default Priority               |
| ---------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **Tier 1** | **CRITICAL**      | Automatic criminal sanction exposure risk (Arts. 60–62 nDSG); active unlawful processing of sensitive data without justification; systematic FDPIC notification failure for high-risk breaches; ongoing transfer to non-adequate countries without any safeguard | Immediate — within 72 hours    |
| **Tier 2** | **NON-COMPLIANT** | Breach of a specific nDSG obligation with material regulatory or legal risk; missing mandatory DPAs; no DPIA for absolute-trigger processing; missing required information elements in privacy notices; no written ROPA where required                           | Near-term — within 30 days     |
| **Tier 3** | **PARTIAL**       | Obligation exists but implementation is incomplete or of insufficient quality; ROPA exists but missing mandatory fields; DPIA conducted but undocumented; privacy notice present but missing transfer destination countries                                      | Medium-term — within 90 days   |
| **Tier 4** | **COMPLIANT**     | Obligation met; documentation adequate; no material gaps identified                                                                                                                                                                                              | Maintain; review at next cycle |

**Automatic CRITICAL triggers** — regardless of context, the following findings are always
classified CRITICAL:

1. **Unlawful transfer to non-adequate country without any safeguard** (Art. 16 nDSG + Art. 61)
2. **Missing written DPA with a processor handling sensitive personal data** (Art. 9 + Art. 61)
3. **DPIA not performed for large-scale sensitive data or systematic public surveillance** (Art. 22 + Art. 61)
4. **False or materially misleading privacy notice** (Art. 19 + Art. 60)
5. **No breach detection or FDPIC notification process for high-risk breaches** (Art. 24 + Art. 61)
6. **No foreign representative appointed for qualifying foreign controller** (Art. 14 + Art. 61)
7. **Confidential sensitive data disclosed to unauthorised party without legal basis** (Art. 62)

---

## Prioritization Framework

Organise all findings into three remediation tiers:

### Tier 1 — IMMEDIATE (0–30 days)

Address all CRITICAL findings. These carry criminal sanction exposure or active unlawful processing
risk. Assign named individual owners with board-level visibility.

_Typical Tier 1 findings_: Missing processor DPAs for sensitive data processing; unlawful
cross-border transfers with no safeguard; false privacy notices; failure to conduct DPIA for
absolute-trigger processing.

### Tier 2 — NEAR-TERM (30–90 days)

Address all NON-COMPLIANT findings. These are breaches of specific nDSG obligations without
immediate criminal exposure but with material regulatory and reputational risk.

_Typical Tier 2 findings_: Incomplete ROPA; missing DPIA for non-absolute-trigger high-risk
processing; privacy notices missing transfer destination countries; data subject request workflow
exceeding 30-day response SLA; no breach documentation system.

### Tier 3 — BACKGROUND (90–180 days)

Address all PARTIAL findings. These are quality and documentation improvements to existing
compliant foundations.

_Typical Tier 3 findings_: ROPA missing optional best-practice fields; DPAs lacking enhanced
sub-processor provisions; security measures adequate but not formally documented; no DPO
appointed (voluntary but beneficial).

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                  | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every nDSG obligation cites the specific article (e.g., "Art. 24(1) nDSG") or DPO article             | Add citation or mark "[UNVERIFIED]"                      |
| **Format**     | Citations follow Swiss legislative citation format (Art. [number] nDSG; SR [number])                  | Fix format                                               |
| **Currency**   | Every cited provision confirmed as in force post-1 September 2023; FDPIC guidance checked for updates | Flag "[CHECK CURRENCY — nDSG entered force 1 Sept 2023]" |
| **Domain**     | Analysis stays within Swiss federal nDSG scope; cantonal law clearly distinguished                    | Remove or clearly flag as cantonal scope                 |
| **Confidence** | Uncertainty explicitly stated; no confident assertion of unsettled nDSG interpretation                | Add confidence qualifier                                 |

---

## Self-Interrogation for CRITICAL Findings

For every finding classified CRITICAL, apply this three-pass review before delivering it:

**Pass 1 — Legal Chain Integrity**: Does the CRITICAL classification follow directly from the
cited nDSG article? Would the FDPIC or a Swiss criminal prosecutor reach the same conclusion?
Is the criminal provision correctly identified (Art. 60, 61, or 62)?

**Pass 2 — Completeness**: Have all relevant nDSG articles and DPO provisions been considered?
Are there FDPIC guidelines that qualify or expand the obligation? Is the cantonal/federal scope
boundary correct?

**Pass 3 — Challenge**: What is the strongest argument that this is not CRITICAL? Is there an
exception or justification that applies? Under what circumstances would a qualified Swiss
data protection lawyer reach a different conclusion? State the strongest counterargument before
confirming CRITICAL.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                            | Action                                                                    |
| ------------ | --------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Black-letter nDSG requirement; FDPIC confirmed; no interpretive ambiguity                          | State with confidence                                                     |
| **High**     | 0.80–0.94 | Strong statutory basis; minor interpretive questions remain                                        | State with brief caveat                                                   |
| **Probable** | 0.60–0.79 | Good arguments; FDPIC guidance not yet confirmed this specific scenario                            | State with reasoning and contra-indicators                                |
| **Possible** | 0.40–0.59 | Genuine interpretive uncertainty; nDSG is recent (2023) and some areas lack authoritative guidance | Flag for Swiss counsel review with both sides                             |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative interpretation of novel nDSG issue                                         | Do not assert; flag "[UNCERTAIN — consult Swiss data protection counsel]" |

**Note on nDSG maturity**: The nDSG entered into force on 1 September 2023. Several interpretive
questions remain unsettled, particularly regarding: exact scope of "large-scale" processing;
"high risk" threshold for DPIA; assessment of "proportionate effort" exceptions; FDPIC enforcement
priorities. Apply Probable or Possible confidence scores to any analysis depending on FDPIC
enforcement guidance not yet published.

---

## Glass Box Audit Trail

Include this section in every compliance assessment output:

```yaml
glass_box:
  skill_name: "legalcode-ch-ndsg-compliance"
  assessment_date: "[YYYY-MM-DD]"
  organisation_type: "[Private company / SME / Non-profit / Foreign entity / other]"
  jurisdiction: "Switzerland — federal nDSG (SR 235.1, in force 1 Sept 2023)"
  nDSG_version: "SR 235.1 (AS 2022 491) as in force [assessment date]"
  DPO_ordinance_version: "SR 235.11 as in force [assessment date]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[/tmp/legalcode-ch-ndsg-research.md or 'Not created']"
  domains_assessed:
    - "Processing principles (Art. 6 nDSG)"
    - "Information obligations (Arts. 19–21 nDSG)"
    - "Data security (Art. 8 nDSG; DPO)"
    - "ROPA (Art. 12 nDSG)"
    - "Processor contracts (Art. 9 nDSG)"
    - "DPIA (Arts. 22–23 nDSG)"
    - "Breach notification (Art. 24 nDSG; Art. 15 DPO)"
    - "Data subject rights (Arts. 25–28 nDSG)"
    - "Cross-border transfers (Arts. 16–17 nDSG; Annex 1 DPO)"
    - "Criminal sanctions (Arts. 60–62 nDSG)"
  sme_ropa_exemption_assessed: "[Yes / No / Not applicable]"
  dpo_registered: "[Yes / No / Not applicable]"
  fdpic_consultation_exemption_available: "[Yes / No / Not assessed]"
  cantonal_law_flag: "[Cantonal processing identified — assess separately / No cantonal processing]"
  gdpr_alignment_check: "[Performed / Not performed — single-jurisdiction only]"
  critical_findings_count: "[number]"
  non_compliant_findings_count: "[number]"
  partial_findings_count: "[number]"
  automatic_critical_triggers_identified: "[list or 'None']"
  criminal_sanction_exposure: "[Identified — see Domain 10 / Not identified]"
  breach_notification_readiness: "[READY / PARTIAL / NOT READY]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  confidence: "HIGH / MEDIUM / LOW — [rationale based on information quality]"
  limitations:
    - "[List of scope limitations, information gaps, or assumptions made]"
    - "nDSG interpretive guidance continues to evolve — FDPIC factsheets should be checked at edoeb.admin.ch"
    - "Criminal liability assessment requires qualified Swiss counsel"
  reviewer: "AI-assisted — requires review by a qualified Swiss data protection professional"
```

---

## Anti-Patterns

The following errors are common in nDSG compliance assessments and implementations. Check
for each in any assessment.

1. **GDPR = nDSG fallacy**: Assuming GDPR compliance automatically means nDSG compliance.
   Critical divergences exist: no standalone erasure right; criminal sanctions on natural persons;
   different legal basis framework; different breach threshold; different information obligation scope.

2. **Six-basis GDPR model applied to nDSG**: Applying GDPR's mandatory six-legal-basis framework
   to Swiss private controllers. Under nDSG, private controllers do not need a formal legal basis
   for all processing — a justification is required only for restricted categories.

3. **GDPR erasure right implemented as nDSG right**: Creating an "nDSG Art. 17 right to erasure"
   that does not exist. Erasure under nDSG is a civil law remedy, not an administrative right.
   Responding to erasure requests as if nDSG mandates them is legally misleading.

4. **72-hour FDPIC notification deadline**: Stating that nDSG imposes a 72-hour breach
   notification deadline. The nDSG uses "as soon as possible" — no numeric deadline exists. The
   72-hour standard comes from GDPR; it is market practice for nDSG, not a legal requirement.

5. **All breaches reported to FDPIC**: Reporting every security incident to the FDPIC. nDSG
   notification only triggers for "likely high risk" breaches (higher threshold than GDPR). Over-
   notification can strain FDPIC resources and create unnecessary documentation.

6. **Criminal fines assessed against the organisation**: Modeling nDSG sanctions as corporate
   fines (like GDPR). nDSG criminal fines up to CHF 250,000 target natural persons (employees,
   executives, board members) — not the legal entity. Risk should be assessed at the individual level.

7. **Negligence criminalised**: Treating negligent nDSG violations as criminal. Arts. 60–62 nDSG
   require at minimum contingent intent (_dolus eventualis_). Purely negligent violations are not
   criminal under nDSG, though they may trigger FDPIC corrective orders.

8. **SME ROPA exemption applied without checking triggers**: Assuming all ≤250 employee companies
   are ROPA-exempt. The exemption only applies if there is no sensitive personal data, no high-risk
   profiling, and no large-scale processing. One sensitive data category voids the exemption.

9. **EU SCCs used for Swiss transfers without Swiss adaptations**: Using unmodified EU Commission
   SCCs for Switzerland-outbound transfers. Swiss adaptations are required: replace GDPR references
   with FADP references; designate FDPIC as supervisory authority; adapt member state references.

10. **US transfer adequacy assumed without DPF verification**: Assuming all US transfers are
    adequate post-September 2024. Only US organisations certified under the **Swiss-U.S. Data
    Privacy Framework (Swiss-U.S. DPF)** qualify for adequacy. Non-DPF US entities require SCCs
    or other safeguards.

11. **DPO appointment overlooked**: Dismissing the DPO as a GDPR concept irrelevant to nDSG.
    A registered Data Protection Advisor unlocks the FDPIC consultation exemption for DPIA
    high-risk residual risk scenarios (Art. 23(4) nDSG) — a material compliance benefit for
    organisations conducting high-risk processing.

12. **Cantonal law conflated with nDSG**: Applying nDSG compliance conclusions to cantonal public-
    sector processing. Cantonal authorities and their processing activities are governed by cantonal
    data protection laws, not the federal nDSG. Separate assessments are required.

13. **Information obligation scope under old FADP**: Maintaining the old 1992 FADP approach of
    providing notices only for sensitive data. The nDSG requires notices for **all** personal data
    collection — the scope is now equivalent to GDPR.

14. **DPIA threshold underestimated**: Treating nDSG DPIAs as optional. The absolute mandatory
    triggers (large-scale sensitive data; systematic public area surveillance) are not negotiable
    under Art. 22(2) nDSG. Missing a mandatory DPIA is a criminal violation risk under Art. 61.

15. **Biometric data classification missed**: Failing to classify biometric data as sensitive
    personal data under Art. 5(c)(4) nDSG. Biometric data is a new addition to the nDSG sensitive
    categories (not in the 1992 FADP). Facial recognition, fingerprints, and voice prints are
    sensitive data requiring enhanced protection.

16. **Administrative proceedings in sensitive data category**: Not recognising that nDSG extends
    its sensitive data definition to cover **administrative proceedings and sanctions** — a category
    not in GDPR's Art. 9. This includes disciplinary proceedings, regulatory investigations, and
    civil enforcement actions.

17. **Social assistance data not treated as sensitive**: Overlooking social assistance measures
    as a sensitive personal data category (Art. 5(c)(6) nDSG). This is unique to Swiss law with
    no GDPR equivalent. Social assistance, welfare, and related data requires enhanced protection.

18. **Foreign representative obligation ignored**: Foreign controllers operating from abroad who
    process Swiss resident data at scale fail to appoint a Swiss representative under Art. 14 nDSG.
    The failure is a criminal violation risk under Art. 61.

19. **No separation between high-risk profiling and general profiling**: Failing to apply the
    nDSG's distinct "high-risk profiling" concept (Art. 5(g) nDSG). High-risk profiling — where
    a combination of data allows assessment of essential personality aspects — requires explicit
    consent from private actors, triggers mandatory DPIA, and carries enhanced protection obligations.
    It is not merely "sensitive automated processing" as in GDPR.

20. **Processor breach notification gap**: DPAs that do not require processors to notify the
    controller of any breach (regardless of risk level). Under nDSG, the processor has an
    unconditional notification obligation to the controller — DPAs must capture this.

---

## Writing Standards

Before delivering any compliance assessment output, apply these quality gates:

- **Accuracy first**: Every nDSG obligation stated must cite the specific article. Every gap
  identified must state the violated provision.
- **Swiss legal terminology**: Use correct bilingual terminology — _Verantwortlicher_ (controller),
  _Auftragsbearbeiter_ (processor), _Datenschutzberater_ (DPA/DPO), _EDÖB_ (FDPIC), _nDSG_
  (or FADP in English) — alongside English translations on first use.
- **No false equivalence**: Do not conflate nDSG obligations with GDPR obligations. Where they
  diverge, state the divergence clearly.
- **Escalation language for criminal risk**: Use explicit escalation language for criminal
  sanction findings: "This finding exposes natural person(s) responsible for [domain] to criminal
  liability under Art. [60/61/62] nDSG — maximum fine CHF 250,000 per individual. Engage
  qualified Swiss counsel immediately."
- **Plain language**: Compliance findings must be actionable by a non-lawyer. Avoid unexplained
  legal jargon. Explain what needs to be done, not just what is wrong.
- **Confidence qualifiers on nDSG novelty**: The nDSG is recent (2023) with limited enforcement
  precedent. Apply appropriate confidence qualifiers and direct to FDPIC guidance at edoeb.admin.ch
  for interpretive questions.
- **No guarantee of currency**: Always include a note that the nDSG is actively evolving —
  FDPIC guidance should be checked before relying on any specific interpretation.

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for current nDSG statutory text, FDPIC guidelines, and DPO ordinance provisions
- Retrieve FDPIC factsheets on DPIA methodology, breach notification, and cross-border transfers
- Verify current Federal Council adequacy list (Annex 1 DPO) for specific transfer destinations
- Retrieve cantonal data protection law text for cantons identified in Step 7
- Mark all retrieved citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using the legal framework embedded in this skill
- Mark all statutory and regulatory references as [VERIFY]
- Direct user to: fedlex.admin.ch (official texts), edoeb.admin.ch (FDPIC guidance)
- Note in Glass Box: `legalcode_mcp: "Not connected"`

---

## Localization Notes

### Cantonal Data Protection Laws

All 26 Swiss cantons have enacted their own data protection legislation. Key characteristics:

- Based on the same general principles as nDSG but vary in: terminology, sectoral scope, DPIA
  thresholds, enforcement powers, and registration requirements
- Major cantons with active data protection enforcement: Zurich (IDG), Geneva (LIPAD), Bern,
  Basel-Stadt, Vaud, Aargau
- Cantonal laws govern: cantonal government bodies, cantonal courts, cantonal hospitals and
  universities, municipal authorities within the canton

### Linguistically Diverse Jurisdiction

Switzerland has four official languages. Privacy notices and DPAs for Swiss-resident data subjects
must be in a language they understand. For organisations operating nationally:

- German: _Datenschutzhinweis_, _Datenschutzbeauftragte_
- French: _avis de protection des données_, _délégué à la protection des données_
- Italian: _informativa sulla protezione dei dati_
- Romansh: relevant for specific cantonal applications

### Cross-Border from Switzerland to EU

Switzerland does not need GDPR compliance for outbound transfers to the EU — the EU-Switzerland
adequacy decision means EU recipients can receive Swiss personal data freely. However, Swiss
organisations transferring personal data from EU data subjects to Switzerland must comply with
GDPR for those transfers (the adequacy finding runs inbound to Switzerland). Distinguish clearly
between the direction of data flows when assessing obligations.

---

## Output Format Template

Produce compliance assessment reports in the following format:

```markdown
# nDSG Compliance Assessment Report

**Organisation**: [Name]
**Assessment date**: [YYYY-MM-DD]
**Scope**: [Full assessment / Targeted domain(s)]
**Assessed by**: AI-assisted (legalcode-ch-ndsg-compliance skill)
**Status**: DRAFT — Requires review by qualified Swiss data protection professional

---

## Stated Assumptions

[List all assumptions made about the organisation's processing activities, based on Step 2 responses]

---

## Executive Summary

| Category                               | Count          |
| -------------------------------------- | -------------- |
| CRITICAL findings                      | [N]            |
| NON-COMPLIANT findings                 | [N]            |
| PARTIAL findings                       | [N]            |
| COMPLIANT domains                      | [N]            |
| Automatic CRITICAL triggers identified | [list or None] |
| Criminal sanction exposure identified  | [Yes/No]       |

**Overall compliance posture**: [CRITICAL RISK / MATERIAL GAPS / LARGELY COMPLIANT / COMPLIANT]

**Immediate actions required**: [Summary of Tier 1 actions]

---

## Applicability Determination

- **nDSG applies**: [Yes / No / Partial]
- **Foreign representative required**: [Yes / No / Not applicable]
- **SME ROPA exemption**: [Applies / Does not apply / Cannot confirm]
- **DPO registered**: [Yes / No / Recommended]
- **FDPIC consultation exemption available**: [Yes / No]
- **Cantonal law considerations**: [None identified / Cantons: list]

---

## Domain Findings

### Domain 1: Processing Principles (Art. 6 nDSG) — [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]

**Summary**: [One paragraph]

| Principle          | Status | Finding | Action Required |
| ------------------ | ------ | ------- | --------------- |
| Lawfulness         |        |         |                 |
| Good faith         |        |         |                 |
| Proportionality    |        |         |                 |
| Purpose limitation |        |         |                 |
| Accuracy           |        |         |                 |
| Storage limitation |        |         |                 |

**Privacy by Design/Default (Art. 7)**: [Status and findings]

---

### Domain 2: Information Obligations (Arts. 19–21 nDSG) — [Status]

**Summary**: [One paragraph]

| Required Element                | Present | Quality | Action Required |
| ------------------------------- | ------- | ------- | --------------- |
| Controller identity             |         |         |                 |
| Processing purpose(s)           |         |         |                 |
| Recipients/categories           |         |         |                 |
| Transfer countries + safeguards |         |         |                 |

**Timing compliance**: [Direct collection / Indirect collection / Automated decisions]

---

### Domain 3: Data Security (Art. 8 nDSG; DPO) — [Status]

**Summary**: [One paragraph]
[Security domain table with findings]

---

### Domain 4: ROPA (Art. 12 nDSG) — [Status / Exempt]

**SME exemption**: [Applies / Does not apply]
[ROPA completeness assessment if applicable]

---

### Domain 5: Processor Contracts (Art. 9 nDSG) — [Status]

**Processor inventory**: [Complete / Incomplete / Unknown]
[DPA compliance table]

---

### Domain 6: DPIA (Arts. 22–23 nDSG) — [Status]

**Absolute triggers present**: [Yes — list / No]
**DPIAs completed**: [Yes / No / Partial]
**FDPIC consultation required**: [Yes / No / Exempt — registered DPO]

---

### Domain 7: Breach Notification (Art. 24 nDSG; Art. 15 DPO) — [Status]

**Breach detection process**: [READY / PARTIAL / NOT READY]
**FDPIC notification workflow**: [READY / PARTIAL / NOT READY]
**Processor notification DPA clause**: [Present / Missing]

---

### Domain 8: Data Subject Rights (Arts. 25–28 nDSG) — [Status]

| Right                               | Workflow Present | 30-day SLA | Notes |
| ----------------------------------- | ---------------- | ---------- | ----- |
| Access (Art. 25)                    |                  |            |       |
| Rectification (Art. 32)             |                  |            |       |
| Portability (Art. 28)               |                  |            |       |
| Automated decision review (Art. 21) |                  |            |       |

**Erasure position**: [Correct civil law position documented / Incorrect GDPR right implemented]

---

### Domain 9: Cross-Border Transfers (Arts. 16–17 nDSG) — [Status]

**Transfer destinations identified**: [Yes / No / Partial]

| Destination Country | Adequacy Status                     | Safeguard in Place                          | Compliant? |
| ------------------- | ----------------------------------- | ------------------------------------------- | ---------- |
| [Country]           | [Full / Conditional / Not adequate] | [Adequacy / SCCs / BCR / Derogation / None] |            |

---

### Domain 10: Criminal Sanction Exposure (Arts. 60–62 nDSG) — [Status]

**Criminal sanction risk identified**: [Yes / No]

| Provision     | Risk Area        | Exposed Individual(s) | Severity |
| ------------- | ---------------- | --------------------- | -------- |
| Art. 60/61/62 | [Violation type] | [Role]                | CRITICAL |

**Recommendation**: [Immediate Swiss counsel engagement / Monitoring / No current exposure]

---

## Prioritised Remediation Roadmap

### Tier 1 — IMMEDIATE (0–30 days)

| Finding   | Domain   | Owner        | Action            |
| --------- | -------- | ------------ | ----------------- |
| [Finding] | [Domain] | [Named role] | [Specific action] |

### Tier 2 — NEAR-TERM (30–90 days)

| Finding   | Domain   | Owner        | Action            |
| --------- | -------- | ------------ | ----------------- |
| [Finding] | [Domain] | [Named role] | [Specific action] |

### Tier 3 — BACKGROUND (90–180 days)

| Finding   | Domain   | Owner        | Action            |
| --------- | -------- | ------------ | ----------------- |
| [Finding] | [Domain] | [Named role] | [Specific action] |

---

## GDPR Alignment Note (if applicable)

[Summary of key divergences between nDSG and GDPR obligations for this organisation]

---

## Cantonal Law Considerations

[Identified cantonal processing activities and applicable laws; or "No cantonal public-sector
processing identified — nDSG federal scope applies"]

---

## Limitations

- This assessment is AI-assisted and does not constitute legal advice
- Criminal liability findings require review by qualified Swiss criminal law / data protection counsel
- The nDSG is recent (in force September 2023); FDPIC enforcement guidance continues to evolve
- Cantonal data protection laws are not comprehensively assessed
- Verify all adequacy list references against current Annex 1 DPO at fedlex.admin.ch
- [Any organisation-specific limitations identified during assessment]

---

## Glass Box Audit Trail

[Insert completed YAML from template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for the Switzerland jurisdiction. Legal
research conducted via multi-agent parallel research pipeline covering: Swiss Federal Act on Data
Protection (nDSG / FADP, SR 235.1); Data Protection Ordinance (DPO / VDSG, SR 235.11); FDPIC
guidelines and factsheets (edoeb.admin.ch); Swiss-U.S. Data Privacy Framework (effective September
2024); Federal Council adequacy list (Annex 1 DPO, updated September 2024); criminal sanction
architecture under Arts. 60–62 nDSG; GDPR comparison research; cantonal data protection law
overview; DLA Piper Data Protection Laws of the World (Switzerland); ICLG Switzerland Data
Protection 2025–2026; Pestalozzi Law nDSG criminal sanctions analysis; Hogan Lovells EU SCCs
Swiss recognition guidance; MME personal liability analysis; HÄRTING data subject rights under
nDSG; LALIVE ROPA documentation guidance; PwC Switzerland EU adequacy confirmation; Morgan
Lewis Swiss adequacy list analysis; Goodwin Privacy Blog nDSG overview. The skill incorporates
the Legalcode standard quality framework (Citation Quality Gates, Self-Interrogation, Confidence
Scoring, Glass Box audit trail, anti-patterns catalogue) adapted for the Swiss nDSG context,
with particular attention to the unique criminal sanction model targeting natural persons and
the structural divergences from GDPR. Quality: 18/18 Legalcode quality elements present.
