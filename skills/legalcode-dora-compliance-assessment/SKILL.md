---
name: legalcode-dora-compliance-assessment
description: >
  Assesses EU DORA (Digital Operational Resilience Act, Regulation (EU) 2022/2554) compliance
  for financial entities covering all five DORA pillars: ICT risk management framework
  (Chapter II, Articles 5–16); ICT-related incident classification and reporting
  (Chapter III, Articles 17–23); digital operational resilience testing including
  Threat-Led Penetration Testing — TLPT (Chapter IV, Articles 24–27); third-party ICT
  risk management including critical ICT third-party service providers — CTPPs
  (Chapter V, Articles 28–44); and information sharing arrangements (Chapter VI, Article 45).
  Maps DORA to NIS2 Directive lex specialis, GDPR Article 32, EBA guidelines, and all
  27 finalized regulatory and implementing technical standards (RTS/ITS). Use when a
  financial entity needs to assess DORA compliance posture, prepare for supervisory
  examination, build a DORA gap remediation roadmap, design incident classification and
  reporting procedures, prepare TLPT programs, audit third-party ICT contracts for Article 30
  mandatory provisions, or build information sharing arrangements. Covers entity scope
  determination (21 in-scope categories including credit institutions, investment firms,
  payment institutions, insurers, crypto-asset service providers), simplified regime
  entities (Article 16), board governance requirements (Article 5), TLPT mandatory 3-year
  testing cycle, register of contractual arrangements, CTPP oversight exposure, and
  cross-directive alignment. Produces COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL compliance
  assessments per pillar with IMMEDIATE/NEAR-TERM/BACKGROUND remediation roadmaps,
  prioritised action tables, and Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# DORA Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance
> with Regulation (EU) 2022/2554 (DORA) and its implementing technical standards. It does
> not constitute legal advice, regulatory guidance, or a compliance certification. DORA is
> a complex regulation with evolving supervisory guidance and national enforcement practices —
> verify all statutory references, thresholds, and timelines against current regulatory
> publications at eba.europa.eu, esma.europa.eu, and eiopa.europa.eu before relying on them.
> AI-generated regulatory analysis carries hallucination risk for cited authority: any
> article references, RTS citations, or regulatory interpretations should be independently
> verified by a qualified financial-sector legal professional or DORA compliance officer.
> This skill does not replace a formal compliance audit conducted by a qualified auditor.

## Purpose and Scope

This skill assesses an organisation's compliance posture against the EU Digital Operational
Resilience Act (Regulation (EU) 2022/2554, applied from 17 January 2025). It covers the full
DORA obligation stack across five pillars: ICT risk management, incident classification and
reporting, digital operational resilience testing (TLPT), third-party ICT risk management,
and information sharing.

**Covers:**
- Entity scope determination — all 21 in-scope financial entity categories and exclusions
- Simplified regime applicability (Article 16) for qualifying microenterprises and small entities
- **Pillar 1**: ICT Risk Management Framework — governance (Article 5), strategy (Articles 6–7),
  identification (Article 8), protection (Article 9), detection (Article 10), response and
  recovery (Article 11), backup and restoration (Article 12), learning and evolving (Article 13),
  communication (Article 14), and audit requirements
- **Pillar 2**: ICT Incident Classification and Reporting — major incident classification criteria
  (Article 18 + Commission Delegated Regulation (EU) 2024/1772), reporting timelines (Articles
  19–20 + Commission Delegated Regulation (EU) 2025/301 + Implementing Regulation (EU)
  2025/302), voluntary notification and cyber threat sharing (Article 20)
- **Pillar 3**: Digital Operational Resilience Testing — basic testing programme (Article 25),
  TLPT mandatory testing scope, methodology, frequency, and external tester requirements
  (Article 26 + Commission Delegated Regulation (EU) 2025/1190), TIBER-EU alignment
- **Pillar 4**: Third-Party ICT Risk Management — register of contractual arrangements (Article
  28 + Commission Implementing Regulation (EU) 2024/2956), pre-contractual due diligence,
  mandatory contractual provisions (Article 30), concentration risk (Article 29), sub-outsourcing
  chain visibility (Commission Delegated Regulation (EU) 2025/532), CTPP oversight exposure
  (Articles 31–44 + Commission Delegated Regulation (EU) 2024/1502)
- **Pillar 5**: Information Sharing Arrangements (Article 45) — voluntary sharing frameworks,
  FS-ISAC and equivalent bodies, notification obligations
- Board governance and personal liability (Article 5, Article 50)
- Cross-directive alignment: DORA as lex specialis to NIS2; GDPR Article 32 overlap;
  EBA guidelines supersession; PSD2 dual-reporting resolution
- Remediation roadmap with IMMEDIATE / NEAR-TERM / BACKGROUND tiers and TLPT timeline

**Does not:**
- Certify DORA compliance (compliance certifications require accredited audit)
- Provide jurisdiction-by-jurisdiction legal opinions on national enforcement practices
- Replace supervisory examination processes of any national competent authority
- Assess ISO 27001 / NIST CSF / SOC 2 gap analysis (frameworks that overlap but differ)
- Cover DORA obligations for ICT third-party service providers themselves (this skill covers
  financial entity obligations; CTPP oversight obligations are assessed separately)
- Provide legal advice on sanctions exposure or litigation strategy

**Related skills:**
- `legalcode-nis2-compliance-assessment` — NIS2 Directive compliance; financial entities
  subject to both DORA and NIS2 should run both skills
- `legalcode-dpa-review-and-negotiation` — GDPR Article 28 DPA review for vendors who also
  process personal data under DORA third-party arrangements
- `legalcode-vendor-privacy-assessment` — vendor due diligence; extend for DORA Article 28
  pre-contractual risk assessment
- `legalcode-breach-regulatory-notification-drafter` — incident notification drafts for
  DORA Article 19 initial, intermediate, and final reports
- `legalcode-compliance-risk-assessment` — broader compliance risk baseline that may feed
  into DORA ICT risk management framework documentation

---

## Jurisdiction and Governing Law

**Primary legislation**: Regulation (EU) 2022/2554 of the European Parliament and of the
Council of 14 December 2022 (DORA). Entered into force: 16 January 2023. Applied from:
**17 January 2025**. DORA is a **directly applicable regulation** — unlike NIS2, it requires
no national transposition. All 27 Member States apply the same text simultaneously.

**Key articles for this skill:**
- Article 2 — Scope; 21 categories of in-scope financial entities
- Article 3 — Definitions
- Article 4 — Proportionality principle
- Articles 5–14 — ICT Risk Management Framework (Pillar 1)
- Article 16 — Simplified ICT risk management framework for qualifying entities
- Articles 17–18 — ICT-related incident management and classification
- Articles 19–23 — Reporting obligations; voluntary notification; PSD2 alignment
- Articles 24–27 — Digital operational resilience testing (TLPT)
- Articles 28–30 — General third-party ICT risk management; register; contractual requirements
- Articles 31–44 — CTPP oversight framework; lead overseer powers; Joint Examination Teams
- Article 45 — Information sharing arrangements
- Articles 50–52 — Administrative penalties; personal liability; criminal sanctions

**Key implementing technical standards (all finalized):**

| RTS/ITS | Subject | Published | Applied From |
|---------|---------|-----------|--------------|
| CDR (EU) 2024/1774 | ICT risk management tools, methods, policies; simplified framework | 25 Jun 2024 | 17 Jan 2025 |
| CDR (EU) 2024/1772 | Incident classification criteria and materiality thresholds | 25 Jun 2024 | 17 Jan 2025 |
| CDR (EU) 2025/301 | Incident reporting: timelines, content, intermediate/final reports | OJ published | 12 Mar 2025 |
| CIR (EU) 2025/302 | Incident reporting: standard forms, templates, procedures | OJ published | 12 Mar 2025 |
| CDR (EU) 2024/1773 | Third-party ICT policy (critical/important functions) | 25 Jun 2024 | 17 Jan 2025 |
| CIR (EU) 2024/2956 | Register of information (RoI) templates | Finalized | See NCA deadlines |
| CDR (EU) 2025/532 | Sub-contracting of ICT services for critical/important functions | 2 Jul 2025 | Jul 2025+ |
| CDR (EU) 2025/1190 | TLPT methodology, internal tester requirements, scope criteria | 18 Jun 2025 | 8 Jul 2025 |
| CDR (EU) 2024/1502 | CTPP designation criteria | Finalized | Jan 2025 |
| CDR (EU) 2024/1505 | CTPP oversight fee structure | Finalized | Jan 2025 |
| CDR (EU) 2025/295 | Oversight harmonisation RTS | Finalized | 2025 |
| CDR (EU) 2025/420 | Joint Examination Team (JET) composition | Finalized | 2025 |

**Lex specialis relationship to NIS2 (NIS2 Article 4(1)–(2)):**
DORA operates as lex specialis relative to NIS2. Where DORA mandates equivalent or stricter
cybersecurity risk-management measures or incident notification for in-scope financial entities,
the overlapping NIS2 provisions do not additionally apply. [JURISDICTION-SPECIFIC] Some Member
States may enact NIS2 transpositions stricter than DORA minimums — verify national law for
relevant jurisdictions. NIS2 continues to apply for:
- MFA and encryption requirements (NIS2 Article 21(j)) not specifically addressed in DORA
- Non-financial activities of entities classified as NIS2-essential in addition to DORA scope
- Any stricter national transposition standards

**Supervisory model**: DORA has no single pan-EU supervisor for financial entities. Each
entity reports to its **home Member State national competent authority (NCA)**:
- Credit institutions: prudential supervisor (ECB under SSM for significant institutions;
  national supervisor for less significant institutions)
- Investment firms, asset managers: national securities regulator (e.g., BaFin DE, AMF FR,
  CSSF LU, CBI IE, AFM NL, SEC/CONSOB IT)
- Insurance: national insurance supervisor (e.g., BaFin DE, ACPR FR, DNB NL)
- Payment/e-money: national payment authority or prudential supervisor
- Crypto-assets: MiCA-designated NCA

**CTPP oversight**: The three European Supervisory Authorities (EBA, ESMA, EIOPA) act as Lead
Overseer for designated Critical ICT Third-Party Service Providers, each overseeing providers
most relevant to its sector. First CTPP designations: November 2025. Oversight commenced:
December 2025.

**Penalties [JURISDICTION-SPECIFIC]:**
- Financial entities: Up to 2% of total annual worldwide turnover (national law specifies amounts)
- Individual management body members: Up to €1,000,000 per infringement (some Member States up
  to €5,000,000 — e.g., Germany); [VERIFY current national penalty levels]
- CTPPs: Periodic penalty payments up to 1% of average worldwide daily turnover for up to 6
  months, plus public disclosure of non-compliance

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you encounter a CLARIFY
marker, pause and ask the structured questions shown. Only ask when the answer will materially
change the analysis direction. If context has already been provided, skip that question and
proceed.

**Standard clarification format:**
```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. [Option A]: [Description]
2. [Option B]: [Description]
3. [Option C]: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis]
```

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:
- **System description**: Organisation overview, entity type (credit institution / investment
  firm / payment institution / insurer / crypto-asset service provider / other), Member State(s)
  of main establishment, approximate size, and existing ICT documentation
- **Document set**: Uploaded ICT risk management policies, incident response procedures, third-
  party contracts, board minutes on ICT risk, TLPT reports, register of information drafts
- **Gap analysis request**: Prior DORA readiness assessment for update or re-evaluation
- **Greenfield implementation**: Building DORA compliance from scratch; full roadmap required

**Minimum required context**: Organisation name, primary entity type (Article 2 category),
Member State(s) of main establishment, and approximate annual operating expenses.

### Step 2: Gather Context

**⟁ CLARIFY** — Gather context before beginning the assessment (skip questions already answered):

1. **Assessment mode**: What is the primary objective?
   - *Readiness assessment*: Full gap analysis of current state against all five DORA pillars
   - *Incident reporting preparation*: Focus on Article 17–23 incident classification and reporting
     procedures, timelines, and NCA contact points
   - *TLPT preparation*: Focus on Article 24–27 testing obligations, scope, and methodology
   - *Third-party risk audit*: Focus on Article 28–30 contract review and register of information
   - *Supervisory examination preparation*: Document readiness for imminent NCA inspection
   - *Greenfield implementation roadmap*: Building DORA compliance from scratch
   - **Why this matters**: Determines output depth and section emphasis.

2. **Entity type and simplified regime**: What category of financial entity is this?
   - *Full-scope entity*: Credit institution, investment firm (non-exempt), payment institution,
     e-money institution, CCP, CSD, insurance/reinsurance undertaking, AIF manager, UCITS management
     company, crypto-asset service provider, trading venue, or other Article 2 category
   - *Potentially simplified*: Small non-interconnected investment firm, exempt payment institution
     (PSD2 Article 32), exempt e-money institution (EMD2 Article 9), small IORP, microenterprise
     insurance intermediary
   - *Unknown — need classification*: Perform entity classification gate first
   - **Why this matters**: Simplified-regime entities (Article 16) have reduced Pillar 1 requirements
     and are not subject to mandatory TLPT designation.

3. **Member State(s)**: Which Member State(s) is this assessment for?
   - *Single Member State*: [Specify which — determines competent authority and any supplementary
     national guidance]
   - *Multiple Member States*: [List all — multi-NCA coordination required for incident reporting;
     main-establishment NCA leads]
   - *Unknown/pre-assessment*: Proceed with Directive-level analysis; NCA identification deferred
   - **Why this matters**: Identifies the competent authority for incident reports and supervisory
     examination; national penalty levels and supplementary guidance vary.

4. **Existing security framework**: Does the organisation currently operate under any security
   framework?
   - *ISO 27001 certified*: Use existing controls as baseline; identify DORA-specific gaps
     (TLPT, incident threshold, register, simplified RTS are DORA-only)
   - *NIST CSF implemented*: Map NIST functions to DORA pillars
   - *EBA Guidelines on ICT and Security Risk Management (EBA/GL/2019/04) compliant*: Note
     that DORA supersedes these guidelines for in-scope entities; identify delta changes
   - *TIBER-EU tested (pre-2025)*: Prior TIBER-EU tests may satisfy DORA TLPT; verify with NCA
   - *No formal framework*: Begin from first principles; longer assessment; full implementation roadmap
   - **Why this matters**: Existing frameworks accelerate assessment; DORA gaps are identifiable
     rather than building from zero.

5. **Third-party ICT complexity**: What is the organisation's third-party ICT landscape?
   - *Simple (few critical vendors)*: One or two core systems providers (e.g., core banking system
     plus cloud provider); manageable contract remediation
   - *Complex (multiple critical dependencies)*: Extensive ecosystem of cloud, SaaS, core systems,
     payment processors, market data; significant contract remediation and register-of-information
     work required
   - *Supply chain uncertainty*: Sub-outsourcing chains are not fully mapped; concentration risk
     assessment requires discovery work
   - **Why this matters**: Pillar 4 depth varies significantly based on the third-party estate;
     complex landscapes require register-of-information sprint before broader assessment.

6. **TLPT designation status**: Has the organisation been designated for TLPT by its NCA?
   - *Designated — TLPT required*: Assessment includes full TLPT readiness analysis
   - *Not yet designated — but likely in scope*: G-SII/O-SII banks, major payment firms, large
     insurers are likely targets; assess TLPT readiness proactively
   - *Likely not designated — simplified regime or small entity*: Standard testing (Article 25
     basic programme) is sufficient; no TLPT deep-dive needed
   - *Unknown*: Perform TLPT designation likelihood assessment in Step 10
   - **Why this matters**: TLPT is a mandatory 3-year cycle for designated entities and requires
     distinct planning, budget, and external tester engagement.

### Step 3: Gather Legal Authority

Before assessing, gather current legal authority for the assessment:

**With legalcode-mcp connected:**
- Search: "DORA Regulation 2022/2554 Article [N]" — verify current article text
- Search: "Commission Delegated Regulation 2024/1772 incident classification thresholds" — verify
  finalized thresholds
- Search: "Commission Delegated Regulation 2025/1190 TLPT methodology" — verify TLPT requirements
- Search: "DORA [entity type] competent authority [Member State]" — verify NCA contacts
- Save results to `/tmp/dora-assessment-research.md`
- Mark all verified citations as VERIFIED in Glass Box

**Without legalcode-mcp:**
- Proceed with Regulation text from training data
- Mark all citations [VERIFY] — particularly any RTS/ITS details, thresholds, and penalty amounts
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend human legal review of all quantitative thresholds and regulatory contact points

### Step 4: Entity Scope Classification Gate

**BINARY GATE — Determine DORA applicability before assessing any pillar.**

If the organisation is clearly out of scope, provide the classification determination and stop.
If in scope, identify whether the simplified regime (Article 16) applies and proceed to Step 5.

#### 4a. Scope Test (Article 2)

DORA applies to an entity that is one of the following 21 categories:

| # | Entity Category | Simplified Regime Available? |
|---|----------------|------------------------------|
| 1 | Credit institutions | No |
| 2 | Payment institutions (including PSD2-exempt) | Yes (if PSD2 Article 32 exempt) |
| 3 | Account information service providers | No |
| 4 | Electronic money institutions (including EMD2-exempt) | Yes (if EMD2 Article 9 exempt) |
| 5 | Investment firms | Yes (if small and non-interconnected) |
| 6 | Crypto-asset service providers; issuers of asset-referenced tokens | No |
| 7 | Central securities depositories | No |
| 8 | Central counterparties | No |
| 9 | Trading venues | No |
| 10 | Trade repositories | No |
| 11 | Managers of alternative investment funds | Yes (if below AIFMD Article 3(2) threshold) |
| 12 | UCITS management companies | No |
| 13 | Data reporting service providers | No |
| 14 | Insurance and reinsurance undertakings | No |
| 15 | Insurance/reinsurance/ancillary intermediaries — except microenterprises/SMEs | Yes (microenterprises/SMEs excluded) |
| 16 | Institutions for occupational retirement provision (IORPs) | Yes (if ≤ 15 total members) |
| 17 | Credit rating agencies | No |
| 18 | Administrators of critical benchmarks | No |
| 19 | Crowdfunding service providers | No |
| 20 | Securitisation repositories | No |
| 21 | ICT third-party service providers — subject to oversight framework only | N/A |

**OUT OF SCOPE entities (Article 2(3)):**
- Sub-threshold AIFMs exempt under AIFMD Article 3(2)
- Solvency II Article 4 exempted insurance undertakings
- IORPs operating pension schemes with ≤ 15 total members in aggregate
- MiFID II Articles 2 and 3 exempted persons
- Microenterprise insurance/reinsurance intermediaries and ancillary intermediaries
- Post office giro institutions (CRD IV Article 2(5)(3))

[JURISDICTION-SPECIFIC] Member States may additionally exclude Article 2(5) CRD IV entities
from their territory subject to notification to the Commission (Article 2(4)). [VERIFY current
national exclusion decisions.]

**OUT OF SCOPE determination**: If the organisation does not meet any of the 21 categories,
state: "Organisation appears out of scope for DORA. No further assessment required. Recommend
verification with the national competent authority if scope is uncertain."

#### 4b. Simplified Regime Assessment (Article 16)

The following entities may apply the simplified ICT risk management framework under Article 16:
- Small and non-interconnected investment firms (as defined in Commission Delegated Regulation
  (EU) 2024/1774, Article 2)
- PSD2 Article 32-exempted payment institutions
- EMD2 Article 9-exempted electronic money institutions
- IORPs not excluded under Article 2(3) (> 15 members but still small)
- Microenterprises (where not fully excluded)

The simplified framework covers: (i) governance and management body accountability; (ii) information
security policy; (iii) key ICT risk management elements; (iv) security and access safeguards;
(v) ICT business continuity management; (vi) reporting obligations. Simplified-regime entities
are **not subject to TLPT designation** and have lighter register-of-information requirements.

### Step 5: Pillar 1 — ICT Risk Management Framework (Articles 5–16)

Assess against Commission Delegated Regulation (EU) 2024/1774.

**5a. Management Body Governance (Article 5)**

Verify each element:

| Element | Implementation Evidence Required | Classification |
|---------|----------------------------------|----------------|
| Management body formally approved ICT risk management framework | Board minutes, framework sign-off document | |
| Management body maintains sufficient knowledge and skills in ICT risk | Board training records, CV evidence, external advisory engagements | |
| ICT risk management framework reviewed at least annually | Dated review cycles with outcome documentation | |
| Three lines of defence or equivalent internal control structure defined for ICT risk | RACI matrix, audit independence evidence, control function mandate | |
| CISO or equivalent senior officer appointed with ICT risk responsibility | Appointment letter, job description with reporting line to management body | |
| Management body approves ICT business continuity policy | Dated board approval of BCP/DRP policy | |
| Management body approves TLPT programme (if applicable) | Scope document signed by management body, TLPT authority validation reference | |
| Management body approves ICT third-party risk strategy | Strategy document with board approval date | |

**5b. ICT Risk Management Framework and Strategy (Articles 6–7)**

Verify:

| Element | Assessment Questions | Classification |
|---------|---------------------|----------------|
| Documented ICT risk management framework exists | Is the framework a standalone document or embedded in enterprise risk framework? Is it updated when technology changes? | |
| Digital operational resilience strategy documented | Does the strategy address ICT objectives, risk appetite, and links to business strategy? | |
| ICT risk management integrated into enterprise risk management | Is ICT risk on the risk register? Does it feed into ICAAP/ORSA/SREP reporting? | |
| Internal ICT audit function with relevant expertise | Are ICT auditors independent? Do they have formal ICT security qualifications? | |
| Formal audit follow-up process for critical findings | Are critical audit findings tracked to remediation? Is there a formal escalation path? | |

**5c. Identification (Article 8)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Complete ICT asset inventory (hardware, software, ICT assets, data assets) | Is the inventory automated (CMDB) or manual? Last update date? | |
| Business function to ICT asset mapping | Are critical/important business functions identified with their supporting ICT assets? | |
| ICT risk assessment performed and documented | Is the risk assessment annual or event-triggered? Does it cover all inventory assets? | |
| Dependency mapping — internal and third-party dependencies | Are critical dependencies (cloud, SaaS, core systems) documented in the risk register? | |

**5d. Protection and Prevention (Article 9)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Access control policies (least privilege, need-to-know) | Are privileged access management (PAM) controls in place? Is access reviewed periodically? | |
| Policies for multi-factor authentication (MFA) | Is MFA enforced for all remote access, privileged accounts, and sensitive systems? | |
| Patch management and vulnerability management programme | What is the patching cycle? Is there a critical-patch SLA? Vulnerability scanning frequency? | |
| Encryption of data at rest and in transit | Are encryption standards documented? Are key management procedures defined? | |
| Change management procedures for ICT systems | Are changes tested in non-production before deployment? Is change freeze process defined? | |
| Network segmentation and monitoring | Is there network segmentation between critical and non-critical systems? | |

**5e. Detection (Article 10)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Anomaly detection and event correlation controls | Is a SIEM or equivalent in operation? Are alert thresholds defined? | |
| 24/7 monitoring or equivalent coverage | Who monitors outside business hours? Is there an outsourced SOC? | |
| Threat intelligence feeds integrated into detection | Are commercially available or ISAC-sourced threat intelligence feeds in use? | |

**5f. Response and Recovery (Article 11)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| ICT Business Continuity Plan (BCP) documented and approved | When was BCP last reviewed and approved by management body? | |
| ICT Disaster Recovery Plan (DRP) documented | Does the DRP specify RTOs and RPOs for critical systems? | |
| RTOs and RPOs defined, tested, and documented | When were RTOs/RPOs last validated in a test? Do they meet regulatory expectations? | |
| BCP/DRP tested at least annually | Type of test? (Tabletop / Partial failover / Full failover) — date of last test? | |
| Crisis communication plan with internal and external notification procedures | Does the crisis communication plan include client notification, media handling, and NCA notification? | |

**⟁ CLARIFY** — If testing records are partial or dates are unclear:

"BCP/DRP testing frequency and type are critical for Article 11 assessment. Please clarify:
1. When was the last BCP test conducted (tabletop, partial, or full failover)?
2. Did any test reveal recovery time or recovery point gaps?
3. Are test results formally documented and provided to the management body?
**Why this matters**: Untested BCPs classify as NON-COMPLIANT; missing test documentation as PARTIAL."

**5g. Backup and Restoration (Article 12)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Backup policies for all critical systems | Are backup frequencies aligned with RPO targets? | |
| Isolated/offline backups to prevent ransomware propagation | Are backups air-gapped or logically isolated from production? | |
| Backup restoration tested regularly | When was a restoration test last conducted? Were results within RPO? | |

**5h. Learning and Evolving (Article 13)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Post-incident analysis process for all major incidents | Is there a formal post-incident review process with output fed back into the risk framework? | |
| Processes to incorporate external threat intelligence | Are threat intel reports reviewed by security function? Is there a mechanism to update defences? | |
| Annual or event-triggered ICT risk framework review | Is the framework reviewed after significant technology changes or external incidents? | |

**5i. Communication (Article 14)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Internal communication procedures for ICT incidents | Are escalation chains and decision authorities defined? | |
| External communication procedures (clients, regulators, media) | Is there a pre-approved client notification template? A media holding statement? | |
| Designated spokesperson for ICT incidents | Is there a single point of contact for external communications? | |

### Step 6: Pillar 2 — ICT Incident Classification and Reporting (Articles 17–23)

Assess against Commission Delegated Regulation (EU) 2024/1772, Commission Delegated Regulation
(EU) 2025/301, and Commission Implementing Regulation (EU) 2025/302.

**6a. Incident Management Process (Article 17)**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Formal ICT incident management process documented | Does the process cover detection, logging, classification, escalation, containment, recovery? | |
| Incident register maintained for ALL ICT-related incidents | Is the register comprehensive (not just major incidents)? Is it available to the NCA on request? | |
| Responsible function / incident manager designated | Who has authority to classify an incident as "major"? What is the escalation timeline? | |
| Process for classifying incidents as major (applying Article 18 criteria) | Is the classification process documented with quantitative thresholds? | |

**6b. Incident Classification Criteria (Article 18 + Commission Delegated Regulation (EU) 2024/1772)**

An incident must first meet the **basic condition**: the incident adversely impacts the availability,
authenticity, integrity, or confidentiality of network and information systems supporting critical
or important functions.

Then one of two secondary conditions must be met:

**Secondary Condition A (automatic major):**
A successful, malicious, and unauthorised access to network and information systems that has
occurred and may result in data losses.

**Secondary Condition B (threshold-based — two or more of):**

| Criterion | Major Threshold | Assessment Note |
|-----------|-----------------|-----------------|
| Clients affected | > 100,000 clients affected, or > 10% of service users | Confirm client count tracking capability |
| Service downtime | > 2 hours for critical functions | Confirm downtime tracking mechanism |
| Geographic spread | Impact across ≥ 2 EU Member States | Confirm geographic impact assessment |
| Data compromise | Impacts on data availability, authenticity, integrity, or confidentiality affecting business objectives or regulatory compliance | Confirm data impact classification |
| Economic impact | Direct economic losses > €100,000 | Confirm loss estimation methodology (per JC/GL/2024/34) |
| Reputational impact | Media coverage, repetitive client complaints, or concern raised by senior management | Confirm reputational impact escalation trigger |

**⟁ CLARIFY** — When incident threshold calculations are unclear:

"DORA incident classification requires threshold-based assessment. Please clarify:
1. Does the organisation have a documented methodology for estimating direct economic losses per
   incident (required per Joint Guidelines JC/GL/2024/34)?
2. Is there a defined client-count threshold integrated into incident management tooling?
3. For PSD2 entities: has the organisation mapped the relationship between PSD2 Article 96 and
   DORA Article 23 reporting obligations to avoid dual-reporting gaps?
**Why this matters**: Organisations without pre-calculated thresholds will fail the 4-hour initial
notification window requirement."

**6c. Incident Reporting Timelines (Article 19 + Commission Delegated Regulation (EU) 2025/301)**

| Report Stage | Deadline | Authority | Content Requirements |
|-------------|----------|-----------|---------------------|
| **Initial notification** | Within **4 hours** of classifying incident as major (no later than **24 hours** after first detection) | Home Member State NCA | Initial classification; description of incident; affected critical functions; immediate actions taken |
| **Intermediate report** | Within **72 hours** of classifying incident as major | Home Member State NCA | Detailed incident description; propagation scope; client impact assessment; remediation actions |
| **Final report** | Within **1 month** after intermediate report | Home Member State NCA | Root cause analysis; total impact (economic, client, data); lessons learned; permanent remediation |
| **Voluntary notification** | At any time when significant cyber threat identified | Home Member State NCA | Threat description; potential impact if materialised; mitigation taken |

Verify incident reporting readiness:

| Readiness Element | Assessment Question | Classification |
|------------------|---------------------|----------------|
| NCA contact information on file and validated | Is the NCA incident reporting contact confirmed and tested? | |
| Report templates pre-prepared for each stage | Are Forms from CIR (EU) 2025/302 downloaded and pre-filled with entity-level data? | |
| 4-hour classification capability | Can the organisation classify a major incident within 4 hours of detection? Is the decision-authority available outside business hours? | |
| Economic loss estimation process | Is there a pre-defined methodology (per JC/GL/2024/34) for rapid loss estimation? | |
| Incident register for all incidents (Article 17) | Is the register comprehensive, updated in real time, and supervisor-accessible? | |

**6d. PSD2 Dual-Reporting Resolution (Article 23)**

For payment institutions and e-money institutions with dual obligations under DORA (Article 19)
and PSD2 (Article 96):
- DORA reporting supersedes PSD2 Article 96 major incident reporting
- The entity must use DORA's incident classification criteria (Commission Delegated Regulation
  (EU) 2024/1772) rather than PSD2 criteria for all incidents from 17 January 2025 onwards
- [VERIFY] national NCA guidance on PSD2/DORA reporting transition for entities that historically
  reported under PSD2 to a different authority than the DORA-designated NCA

### Step 7: Pillar 3 — Digital Operational Resilience Testing (Articles 24–27)

Assess against Commission Delegated Regulation (EU) 2025/1190 (applied from 8 July 2025).

**7a. Basic Testing Programme (Article 25)**

All in-scope entities (except simplified-regime entities) must maintain a sound and comprehensive
testing programme covering:

| Test Type | Minimum Frequency | Assessment Question |
|-----------|------------------|---------------------|
| Vulnerability assessments and scans | At least annually | Is automated scanning in place? When was last scan? Were findings remediated? |
| Open-source analyses | As needed | Are open-source components tracked (SBOM)? Are known vulnerabilities monitored? |
| Network security assessments | At least annually | Was an external network assessment conducted in the last 12 months? |
| Gap analyses | At least annually | Is gap analysis formally documented and fed into the risk framework? |
| Physical security reviews | At least annually | Do physical security reviews cover data centre and server rooms? |
| Penetration testing | At least annually | Is this external (preferred) or internal? Scope definition? |
| Scenario-based tests (including BCP/DRP) | At least annually | See Step 5f testing assessment |
| Compatibility testing | As needed (post-change) | Is compatibility testing integrated into the change management process? |

**7b. TLPT Designation Likelihood Assessment**

**⟁ CLARIFY** — If TLPT designation status is not confirmed:

"TLPT designation is determined by the NCA based on entity systemic importance. Confirm:
1. Is the entity a G-SII (Global Systemically Important Institution) or O-SII (Other Systemically
   Important Institution) designated by the ECB or national supervisor?
2. Does the entity exceed significant transaction thresholds for payment/e-money activity
   (approximately €150 billion in payment volumes — verify current NCA threshold)?
3. Is the entity a large trading venue, CCP, or central bank-supervised infrastructure provider?
**Why this matters**: Entities that are likely TLPT candidates should proactively engage their NCA
and begin TLPT provider selection — lead times for qualified testers are 6–12 months."

**7c. TLPT Requirements (Article 26 + Commission Delegated Regulation (EU) 2025/1190)**

For entities designated for TLPT:

| TLPT Element | Requirement | Assessment Question |
|-------------|-------------|---------------------|
| **Frequency** | At least once every 3 years | When was last TLPT conducted? When is next due? |
| **Scope document** | Covers all critical/important functions and supporting ICT systems; approved by management body; validated by TLPT authority | Has scope document been drafted, approved, and validated? |
| **Threat intelligence (TI) phase** | External TI provider to identify attack surfaces and threat scenarios (APT tactics, ransomware variants, payment compromise vectors) | Is a qualified TI provider engaged or shortlisted? |
| **Red team testing phase** | Simulated attacks on live production systems based on TI scenarios | Has a red team provider been engaged? Is budget allocated? |
| **Purple team debrief** | Mandatory collaboration between red team (attackers) and blue team (defenders) | Is a purple team debrief session planned post-test? |
| **External tester** | At least every third TLPT cycle must use an external tester; significant credit institutions (SSM) must always use external testers | Is an external tester identified? Are qualification/independence criteria verified against CDR 2025/1190? |
| **Remediation plan** | Formal remediation plan based on TLPT findings, submitted to TLPT authority | Is there a process for capturing and remediation-tracking TLPT findings? |
| **Senior management participation** | Management body approves scope, receives results, and reviews remediation plan | Is management body involvement documented at each TLPT phase? |
| **Pooled testing** | Permitted for critical third-party ICT providers serving multiple entities | If applicable: have pooled testing arrangements been discussed with affected third-party provider and TLPT authority? |

**TIBER-EU recognition**: Prior TLPT exercises conducted using the TIBER-EU framework before
January 2025 may be recognised by the NCA as satisfying DORA TLPT requirements. [VERIFY with
entity's NCA whether prior TIBER-EU test counts toward the 3-year cycle.]

### Step 8: Pillar 4 — Third-Party ICT Risk Management (Articles 28–44)

Assess against Commission Delegated Regulation (EU) 2024/1773, Commission Implementing Regulation
(EU) 2024/2956, and Commission Delegated Regulation (EU) 2025/532.

**8a. Third-Party ICT Risk Strategy (Article 28(1))**

Verify:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Formal ICT third-party risk strategy documented | Is the strategy approved by the management body? Does it define risk appetite for third-party dependencies? | |
| ICT third-party risk policy (per CDR (EU) 2024/1773) | Does the policy cover service categories, risk tiering, due diligence standards, and monitoring requirements? | |
| Responsibility for third-party ICT risk assigned | Is there a named owner (e.g., Chief Procurement Officer, CISO, Chief Risk Officer)? | |

**8b. Register of Information (Article 28(3) + CIR (EU) 2024/2956)**

The entity must maintain a comprehensive register of all contractual arrangements with ICT
third-party service providers at entity, sub-consolidated, and consolidated group levels.

| Register Element | Requirement | Assessment Question |
|-----------------|-------------|---------------------|
| All ICT contracts documented | Not just critical/important — ALL contractual arrangements | Is the register complete? When was it last validated? |
| Critical/important function designation | Each arrangement must flag whether it supports a critical or important function | Has this designation been formally applied to all arrangements? |
| Provider identification | LEI, EUID, or personal identity documentation | Are all providers identified with required codes? |
| Sub-outsourcing chain visibility | Sub-contractors of ICT services for critical/important functions must be documented | Is tier-2 sub-outsourcing mapped for critical vendors? |
| Annual NCA submission | Register submitted to home NCA annually | Was the first submission completed by the NCA deadline? [VERIFY NCA deadline for specific Member State] |
| Board-level awareness | Management body informed of register contents at least annually | Is register reporting integrated into governance reporting cycle? |

**⟁ CLARIFY** — When register completeness is uncertain:

"DORA Article 28(3) and CIR (EU) 2024/2956 require a comprehensive register of ALL ICT
contractual arrangements, not just critical ones. Please clarify:
1. How many ICT vendor contracts does the organisation estimate it has (to assess register
   completion scope)?
2. Has the organisation completed its annual NCA submission (deadline varies by NCA — check
   national guidance)?
3. Are sub-outsourcing chains for critical vendors documented beyond tier 1?
**Why this matters**: An incomplete register is an observable, immediate NON-COMPLIANT finding
that supervisors will check first."

**8c. Pre-Contractual Risk Assessment (Article 28(2))**

Before entering any ICT service arrangement for a critical or important function, verify:

| Pre-Contractual Step | Requirement | Assessment Question |
|---------------------|-------------|---------------------|
| Critical/important function assessment | Determine whether service supports a critical or important function | Is a documented classification process in place? |
| Due diligence and suitability assessment | Verify provider meets applicable regulatory conditions; assess all relevant risks | Is due diligence documented? Does it cover financial stability, cybersecurity posture, and substitutability? |
| Concentration risk assessment | Assess whether adding this provider increases concentration risk | Is concentration measured (e.g., % of operating expenses per provider; single-source dependency mapping)? |
| Conflicts of interest identification | Identify and manage any conflicts between entity and provider | Is a conflict-of-interest check part of the on-boarding process? |

**8d. Mandatory Contractual Provisions (Article 30)**

ALL ICT service contracts must include these provisions. Enhanced requirements apply to contracts
for critical or important functions.

| Contractual Provision | All Contracts | Critical/Important Functions Additional Requirements | Assessment |
|----------------------|---------------|-----------------------------------------------------|------------|
| Clear description of services and sub-contracting limits | ✓ | Full SLA with performance KPIs | |
| Data location (regions/countries) and change notification | ✓ | Specific data residency warranties | |
| Data availability, authenticity, integrity, confidentiality | ✓ | Specific technical standards | |
| Data portability and recovery upon termination | ✓ | Tested and documented recovery procedures | |
| ICT incident support at pre-agreed cost | ✓ | Response and restoration SLAs | |
| Cooperation with entity's supervisory authorities | ✓ | Full audit, inspection, and access rights | |
| Termination rights for material legal/regulatory breach | ✓ | Exit plan with transition period | |
| Unrestricted access, inspection, and audit rights | — | ✓ (entity, its designated third parties, and competent authorities) | |
| Business contingency and ICT security measures tested by provider | — | ✓ (regular testing; results shared) | |
| TLPT participation rights | — | ✓ (where applicable under Article 26) | |
| Exit strategy and transition planning | — | ✓ (minimum transition period; service continuity; data transfer; secure deletion) | |

**8e. Sub-Outsourcing (Commission Delegated Regulation (EU) 2025/532)**

For contracts supporting critical or important functions, verify:
- Sub-outsourcing chains are identified and mapped (at least to tier 2)
- The primary provider's sub-contractors are assessed for appropriate security standards
- Change notification clauses in primary contracts require provider to notify entity of material
  sub-outsourcing changes before implementation
- The entity has assessed whether sub-outsourcing creates additional concentration risk

**8f. Concentration Risk (Article 29)**

Verify:

| Concentration Risk Element | Assessment Question | Classification |
|---------------------------|---------------------|----------------|
| Single-source dependency identification | Are there any critical or important functions served by a single, non-substitutable provider? | |
| Geographic concentration | Is critical data or processing concentrated in a single data centre region or country? | |
| Financial concentration | What percentage of total operating expenses flows to the top 3 ICT providers? Is there a concentration limit policy? | |
| Exit strategy for concentrated dependencies | Is there a documented exit plan for each critical provider with high switching costs? Has it been tested? | |

**8g. CTPP Oversight Exposure (Articles 31–44)**

If the organisation relies on an ICT provider that has been designated as a Critical ICT
Third-Party Service Provider (CTPP) by the ESAs:

| CTPP Exposure Element | Assessment Question | Classification |
|----------------------|---------------------|----------------|
| Awareness of CTPP designations | Has the organisation identified which of its providers are on the CTPP designation list (published by ESAs in November 2025)? | |
| Contract compliance with CTPP lead overseer requirements | Does the contract with the CTPP enable the lead overseer to inspect, audit, and issue recommendations applicable to the entity? | |
| Contingency planning for CTPP suspension | If the lead overseer instructs suspension of a CTPP, does the entity have a contingency plan to maintain continuity? | |

### Step 9: Pillar 5 — Information Sharing Arrangements (Article 45)

**9a. Participation in Voluntary Sharing Arrangements**

Article 45 does not mandate participation but enables and encourages it:

| Element | Assessment Question | Classification |
|---------|---------------------|----------------|
| Entity participates in an information sharing arrangement | Is the entity a member of FS-ISAC, CERT-FI, national financial sector ISAC, or equivalent? | |
| NCA notified of participation | Has the entity notified its home NCA of joining (required on validation of membership, and again on exit)? | |
| Arrangement governance meets Article 45 requirements | Does the arrangement protect confidential information, comply with GDPR, and comply with competition law? Are conditions of participation documented? | |
| Sharing scope | Does sharing include indicators of compromise (IoCs), TTP (tactics, techniques, procedures), cybersecurity alerts, and configuration intelligence? | |

**⟁ CLARIFY** — If participation status is unknown:

"DORA Article 45 information sharing is voluntary, but participation and NCA notification are
an observable compliance indicator. Please clarify:
1. Is the entity a member of any cybersecurity information sharing arrangement (FS-ISAC, H-ISAC,
   national ISAC, or similar)?
2. Has the NCA been notified of membership (required under Article 45(3))?
**Why this matters**: Non-participation is not a NON-COMPLIANT finding, but absence from any
sharing arrangement and absence of NCA notification where participation exists are both reportable."

### Step 10: Board Governance and Personal Liability Assessment (Article 5, Article 50)

Assess board-level ICT governance independently from the risk management framework assessment
in Step 5. Board accountability is a separate, non-delegable obligation.

| Board Governance Element | Requirement | Assessment Question | Classification |
|--------------------------|-------------|---------------------|----------------|
| Management body formally responsible for ICT risk | Article 5(2) — cannot be delegated | Is there a board resolution or charter formally accepting ICT risk responsibility? | |
| Management body knowledge and skills assessment | Board members individually assessed | Are board competency assessments documented? Is ICT risk training provided to board? | |
| Management body receives regular ICT risk reporting | At minimum annually; more frequently for material developments | Is there a board ICT risk reporting cycle? Are reports substantive (not just green dashboards)? | |
| Board approves digital resilience strategy | Must be formally adopted, not just noted | Is the strategy a board-approved document with a date? | |
| Board approves ICT third-party risk strategy | Formal approval required | Is third-party strategy documented as a board-approved document? | |
| Board receives TLPT scope and results | Before execution and after completion | Is TLPT scope document signed by management body? Is a results presentation to board documented? | |
| CISO/equivalent independence and reporting | Adequate independence from operational IT | Is CISO reporting line independent of the CIO? Is there a direct board reporting channel? | |

### Step 11: Cross-Directive Alignment Assessment

**11a. DORA and NIS2 Alignment**

For financial entities that are also classified as essential or important entities under NIS2:

| Directive | DORA Provision | NIS2 Provision | DORA Alignment Status | Action Required |
|-----------|---------------|----------------|----------------------|-----------------|
| Cybersecurity risk management | Articles 5–16 (DORA) | Article 21 measures 1–10 (NIS2) | DORA displaces NIS2 for in-scope entities | Verify that no additional NIS2 Art. 21 requirements apply in the national transposition |
| Incident reporting | Article 19 (DORA) | Article 23 (NIS2) | DORA displaces NIS2 for in-scope entities | Retain separate NIS2 Art. 23 reporting only for non-financial activities |
| Supply chain security | Articles 28–30 (DORA) | Article 21(d) (NIS2) | DORA displaces NIS2 | DORA Art. 30 mandatory contractual provisions are stricter; DORA is sufficient |
| MFA and encryption | Articles 9 (DORA) | Article 21(j) (NIS2) | Partial overlap — verify DORA Art. 9 addresses all NIS2 Art. 21(j) requirements | [JURISDICTION-SPECIFIC] Review national NIS2 transposition for any stricter MFA/encryption requirements |
| Board accountability | Article 5 (DORA) | Article 20 (NIS2) | DORA Article 5 is broadly equivalent | For entities under both regimes, DORA Article 5 compliance generally satisfies NIS2 Article 20 |

**11b. GDPR Article 32 Alignment**

DORA's ICT security requirements overlap substantially with GDPR Article 32. For systems holding
personal data, verify:
- DORA Pillar 1 (ICT risk management, access controls, encryption) also satisfies GDPR Art. 32
- DORA incident reporting (Article 19) does not replace GDPR Article 33/34 breach notification
  to the supervisory authority (DPA) and data subjects — these are separate obligations
- An ICT incident may simultaneously trigger DORA Art. 19 (to NCA) and GDPR Art. 33 (to DPA);
  both obligations must be met concurrently with their respective timelines

**11c. EBA Guidelines Supersession**

For entities that previously complied with EBA Guidelines on ICT and Security Risk Management
(EBA/GL/2019/04) and EBA Guidelines on Outsourcing Arrangements: DORA supersedes both guidelines.
Confirm that compliance programmes have been updated from EBA guidelines to DORA Regulation text
and implementing RTS/ITS.

### Step 12: Generate Compliance Finding Classifications

After completing Steps 5–11, apply the **Compliance Classification System** (defined below) to
each pillar and sub-element. For each finding:

- **COMPLIANT** ✅: Element fully implemented, documented, tested, and operational. No action required.
- **PARTIAL** ⚠️: Element exists with identifiable gaps — documentation incomplete, testing overdue,
  or partial coverage. Remediation within 90 days. Log owner and target completion date.
- **NON-COMPLIANT** ❌: Element not meaningfully implemented or fundamentally deficient. Remediation
  within 30–90 days. Notify senior management. Assess whether NCA proactive disclosure is appropriate.
- **CRITICAL** 🚨: Element absent, non-functional, or creates immediate operational resilience risk.
  Immediate remediation (0–30 days). Escalate to management body. Consider proactive NCA engagement.

Apply the **Self-Interrogation** (see Quality Assurance Framework) to all CRITICAL and
NON-COMPLIANT findings before finalising classification.

### Step 13: Remediation Roadmap

Prioritise all non-COMPLIANT findings into three tiers:

| Tier | Timeframe | Criteria | Examples |
|------|-----------|----------|---------|
| **IMMEDIATE** | 0–30 days | Absent regulatory obligation; active operational resilience risk; upcoming supervisory inspection; TLPT cycle due | No incident classification process; no NCA reporting contact on file; BCP never tested; TLPT deadline overdue |
| **NEAR-TERM** | 30–90 days | Incomplete but partially addressed; testing or documentation gaps; third-party contract remediation started | Register of information gaps; Article 30 contractual clause gaps in key vendor contracts; TLPT provider engagement started |
| **BACKGROUND** | 90–180 days | Important but not urgent; framework enhancement; information-sharing participation | NCA notification for ISAC membership; sub-outsourcing chain mapping completion; board training programme design |

Add a **TLPT planning timeline** if applicable:

| TLPT Phase | Recommended Timing | Owner |
|-----------|-------------------|-------|
| Scope document preparation | [Month 1–2 of testing year] | CISO + Management Body |
| Management body approval of scope | [Month 2] | Board |
| TLPT authority validation | [Month 2–3] | CISO + NCA |
| Threat intelligence phase (TI provider engagement) | [Month 3–5] | CISO + TI Provider |
| Red team testing execution | [Month 5–9] | CISO + External Red Team |
| Purple team debrief | [Month 9–10] | CISO + Both Teams |
| Final report and remediation plan | [Month 10–11] | CISO |
| Management body results presentation | [Month 11] | CISO + Board |
| Regulatory submission (if required by NCA) | [Month 12] | Legal + CISO |

### Step 14: Quality Verification

Before delivering the assessment, run the quality checks defined in the Quality Assurance
Framework section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL and NON-COMPLIANT finding, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each major finding and the overall assessment.
4. Verify the Glass Box YAML reflects the actual assessment inputs.

### Step 15: Generate Assessment Output

Structure the output using the **Output Format Template** below. Deliver to the user with:
- Executive Summary first (management-facing)
- Pillar findings in detail (technical team-facing)
- Remediation roadmap with clear ownership and deadlines
- Glass Box audit trail at the end (for record-keeping and supervisor requests)

---

## Compliance Classification System

| Tier | Symbol | Definition | Supervisory Risk | Immediate Action |
|------|--------|-----------|-----------------|-----------------|
| **COMPLIANT** | ✅ | Pillar or element fully implemented, documented, tested, and operationalised | Low | Maintain; schedule next review |
| **PARTIAL** | ⚠️ | Element exists with identifiable gaps — documentation incomplete, testing overdue, partial coverage | Medium | Remediation within 90 days; log in risk register |
| **NON-COMPLIANT** | ❌ | Element not meaningfully implemented or fundamentally deficient | High | Remediation within 30–90 days; escalate to senior management |
| **CRITICAL** | 🚨 | Element absent, non-functional, or creates immediate operational resilience risk | Severe | Immediate remediation (0–30 days); escalate to management body; consider proactive NCA engagement |

**Aggregate scoring guidance:**

| Overall Assessment | Meaning |
|-------------------|---------|
| All pillars COMPLIANT | DORA compliant; maintain and update |
| ≥ 1 PARTIAL, 0 NON-COMPLIANT, 0 CRITICAL | Broadly compliant; targeted remediation required |
| ≥ 1 NON-COMPLIANT, 0 CRITICAL | Compliance gap — management escalation and remediation programme required |
| Any CRITICAL | Immediate escalation to management body; prioritised remediation; NCA engagement recommended |

---

## Prioritisation Framework

Prioritise remediation actions by combining severity classification with implementation effort:

| Priority | Classification | Implementation Effort | Action |
|----------|---------------|----------------------|--------|
| P1 — Act now | CRITICAL or NON-COMPLIANT | Any | Allocate resource immediately; escalate to management body |
| P2 — Schedule immediately | CRITICAL or NON-COMPLIANT | High effort | Break into sub-tasks; allocate budget in next sprint; escalate if deadline risk |
| P3 — Remediate | PARTIAL | Low-medium effort | Owner assigned; 90-day target; tracked in risk register |
| P4 — Improve | PARTIAL | High effort | Incorporate into annual planning cycle; 180-day target |
| P5 — Monitor | COMPLIANT | Ongoing | Include in next periodic review; no immediate action |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivery.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every regulatory claim cites a specific DORA Article, Commission Delegated/Implementing Regulation number, or ENISA/EBA/ESMA/EIOPA published guideline | Add citation or mark [UNVERIFIED] |
| **Format** | All citations follow consistent format: "Article 18(1)(a) of Regulation (EU) 2022/2554", "Commission Delegated Regulation (EU) 2024/1772, Article 4" | Fix format |
| **Currency** | Every cited RTS/ITS checked against the 27 finalized documents; mark any implementing measure reference as [CHECK CURRENCY] if post-January 2026 amendments may have occurred | Flag [CHECK CURRENCY] |
| **Domain** | Analysis stays within DORA scope; any GDPR or NIS2 findings explicitly labelled [GDPR] or [NIS2] to prevent confusion | Remove or label regulatory bleed |
| **Confidence** | Any interpretive uncertainty explicitly stated with confidence level; pre-enforcement supervisory interpretations clearly flagged as [SUPERVISORY INTERPRETATION — MAY EVOLVE] | Add confidence qualifier |

### Self-Interrogation for CRITICAL and NON-COMPLIANT Findings

For any finding classified as NON-COMPLIANT or CRITICAL, apply this 3-pass review:

**Pass 1 — Regulatory Necessity**: Does this deficiency actually violate DORA (citing the
specific Article) or a finalized RTS/ITS? Would the national competent authority cite it in a
supervisory examination? Is the requirement in the Regulation text itself, or only in non-binding
ESA guidance?

**Pass 2 — Completeness**: Have all relevant proportionality provisions been considered? Does
Article 4 proportionality apply to this element for this entity type? Are there compensating
controls that partially address the gap? Has the simplified regime (Article 16) been correctly
excluded if applicable?

**Pass 3 — Challenge**: What is the strongest argument that this finding is PARTIAL rather than
NON-COMPLIANT, or PARTIAL rather than CRITICAL? What evidence would upgrade the classification?
Document this challenge as a mitigating note in the finding.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | DORA Regulation text is explicit; requirement unambiguous; no interpretive flexibility | State with confidence |
| **High** | 0.80–0.94 | RTS/ITS provides clear guidance; minor interpretive nuance; most NCAs align | State with brief caveat |
| **Probable** | 0.60–0.79 | RTS/ITS exists but supervisory interpretation is evolving; reasonable reading of text; flag for legal review | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuine uncertainty on applicability to entity type; contradictory signals; supervisory position may differ | Flag for NCA consultation; present both interpretations |
| **Unlikely** | 0.0–0.39 | Speculative interpretation; weak basis; do not assert as requirement | Do not state as requirement; mark [UNCERTAIN] |

---

## Glass Box Audit Trail Template

Include this YAML block at the end of every assessment output:

```yaml
glass_box:
  skill_name: "legalcode-dora-compliance-assessment"
  entity_name: "[Organisation name]"
  entity_type: "[credit institution / investment firm / payment institution / e-money institution / insurance / crypto-asset service provider / UCITS / AIF manager / other]"
  dora_applicability: "[Yes / No / Partial (simplified regime)]"
  simplified_regime: "[Yes — Article 16 / No]"
  member_states:
    - "[Member State 1]"
    - "[Member State 2 if applicable]"
  assessment_mode: "[readiness / incident-prep / TLPT-prep / third-party-audit / supervisory-exam-prep / greenfield-roadmap]"
  existing_framework: "[ISO 27001 / NIST CSF / EBA GL/2019/04 (superseded) / TIBER-EU tested / none]"
  assessment_date: "[YYYY-MM-DD]"
  dora_application_date: "17 January 2025 (directly applicable, no member state transposition)"
  tlpt_designation: "[Designated / Likely designated / Not designated / Unknown]"
  legalcode_mcp: "[Connected / Not connected]"
  pillar_1_classification: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]"
  pillar_2_classification: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]"
  pillar_3_classification: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]"
  pillar_4_classification: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]"
  pillar_5_classification: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]"
  critical_findings: [N]
  non_compliant_findings: [N]
  partial_findings: [N]
  tlpt_readiness: "[Year 1 due / Year 2 due / Year 3 due / Not yet scheduled / Designated test completed on YYYY-MM-DD]"
  register_of_information_submitted: "[Yes, submitted YYYY-MM-DD / Not yet submitted / N/A (simplified regime)]"
  citations_verified: "[N VERIFIED via legalcode-mcp / N marked [VERIFY]]"
  confidence_overall: "[Definite / High / Probable / Possible] — [Rationale]"
  limitations:
    - "Assessment based on organisation-provided information; completeness and accuracy are the organisation's responsibility"
    - "RTS/ITS referenced as of March 2026; verify current status at eba.europa.eu, esma.europa.eu, eiopa.europa.eu before relying on specific thresholds"
    - "DORA enforcement is active as of January 2025; supervisory interpretation of proportionality provisions may evolve through enforcement decisions"
    - "CTPP designation list was first published November 2025; new designations may occur; verify current list"
    - "NCA-specific guidance and national penalty levels vary; verify with the entity's home Member State NCA"
    - "TLPT readiness assessment depends on entity's TLPT designation status confirmed by NCA; designation criteria in CDR (EU) 2025/1190"
  reviewer: "AI-assisted — requires review by a qualified DORA compliance officer, CISO, and qualified financial-sector legal professional before relying on findings"
```

---

## Anti-Patterns

What NOT to do when performing a DORA compliance assessment or building a DORA compliance
programme. These represent the most common errors observed in financial entity DORA readiness
assessments.

1. **Treating ISO 27001 as a DORA proxy** — ISO 27001 certification does not satisfy DORA's
   TLPT mandate, the mandatory register of information (Article 28(3)), the incident threshold
   calculation (Commission Delegated Regulation (EU) 2024/1772), or the specific Article 30
   contractual provisions. ISO 27001 is a useful baseline; it is not a compliance substitute.

2. **Misidentifying the incident reporting authority** — DORA Article 19 reports go to the home
   Member State NCA, not to the EBA or ESAs directly. The ESAs studied a single reporting hub
   (JC 2024/108) but it has not been implemented. Sending DORA reports to an ESA instead of the
   NCA is a reporting failure.

3. **Confusing the 4-hour/24-hour incident window** — The initial notification is due within
   4 hours of **classifying** the incident as major, and no later than 24 hours after first
   **detection**. The 4-hour clock starts at classification, not detection. A 6-hour classification
   process that then triggers a 4-hour notification window can produce a notification 10 hours after
   detection — potentially compliant only if detection-to-notification remains under 24 hours. Pre-define
   classification criteria to enable rapid classification decision.

4. **TLPT as a box-checking exercise** — TLPT is adversarial simulation on live production systems,
   not a penetration test or tabletop exercise. A TLPT that is conducted on a test environment,
   uses a generic attack playbook not informed by threat intelligence, or does not result in actual
   disruption to test response capability, does not satisfy Article 26 or Commission Delegated
   Regulation (EU) 2025/1190.

5. **Assuming year 1 TLPT completion satisfies future cycles** — The 3-year testing cycle requires
   the next test to begin within 3 years of the last. An entity that completes TLPT in year 1 must
   plan, scope, and engage for year-2 testing before the 3-year deadline approaches. TLPT providers
   have 6–12 month lead times; leaving engagement until year 2.5 creates scheduling risk.

6. **Delegating DORA to CISO without board engagement** — Article 5 mandates management body
   (board) responsibility for ICT risk. The management body cannot delegate this responsibility —
   it can delegate execution to the CISO but retains accountability. A DORA programme driven
   entirely by the security function with board members who cannot describe the ICT risk strategy
   is non-compliant with Article 5(4).

7. **Incomplete register of information** — Most NCAs required initial register submissions in
   April 2025. The register must include ALL contractual ICT arrangements, not just critical/important
   ones. Entities that only registered critical vendors have an incomplete register and will fail
   NCA inspection. Conduct a contract discovery exercise before treating the register as complete.

8. **Generic Article 30 contractual clauses** — Article 30 requires specific provisions, not generic
   "information security obligations." Contracts that include a general "comply with applicable law"
   clause without the specific rights — unrestricted audit access, exit strategy, TLPT participation,
   business continuity obligations — are non-compliant. Mass renegotiation of legacy contracts with
   hyperscale cloud and core banking vendors is a known pain point; begin early.

9. **Ignoring sub-outsourcing chains** — Commission Delegated Regulation (EU) 2025/532 requires
   entities to assess and document sub-contracting chains for critical/important function services.
   Entities that only have visibility into tier-1 vendors but not into the hyperscaler's or core
   system vendor's own critical sub-contractors have a concentration and visibility gap.

10. **Treating PSD2 incident reporting as satisfying DORA** — PSD2 Article 96 major incident
    reporting is superseded by DORA Article 19 for in-scope payment and e-money institutions from
    17 January 2025. The incident classification criteria (Commission Delegated Regulation (EU)
    2024/1772) differ from PSD2 criteria. Using PSD2 criteria after January 2025 produces incorrect
    classifications and may generate reporting failures or over-reporting.

11. **No sub-threshold incident register** — DORA Article 17 requires an incident register for ALL
    ICT-related incidents, including those below the major incident threshold. NIS2 treats non-major
    incident reporting as voluntary; DORA does not. The register must be available for NCA inspection
    on request. An organisation tracking only major incidents has a structural compliance gap.

12. **Applying NIS2 proportionality to DORA** — NIS2 has a proportionality framework for important
    entities (Article 21(4)) that allows some flexibility. DORA Article 4 proportionality is
    narrower: it calibrates the intensity of compliance, not the applicability of requirements.
    No DORA pillar can be entirely waived under proportionality; obligations apply to all in-scope
    entities regardless of size (except simplified-regime entities under Article 16).

13. **Missing CTPP designation exposure** — As of December 2025, ESAs have designated the first
    round of CTPPs. Entities relying on a designated CTPP must understand the oversight implications:
    the lead overseer can inspect and issue recommendations affecting how the entity uses the CTPP.
    Entities that have not reviewed their contracts with CTPPs against the oversight framework are
    exposed to contractual compliance gaps.

14. **NCA notification omitted for information sharing membership** — Article 45(3) requires entities
    to notify their home NCA upon validation of membership in an information sharing arrangement,
    and again on exit. Entities that join FS-ISAC or equivalent bodies without notifying their NCA
    have a technical non-compliance even though participation itself is voluntary.

15. **Board competency assessments absent** — Article 5(4) requires management body members to
    maintain sufficient knowledge and skills in ICT risk. Supervisors expect documented evidence of
    board training and individual competency assessment. An absence of any ICT risk training records
    for board members is an audit-ready finding.

16. **TLPT scope document not board-approved** — Commission Delegated Regulation (EU) 2025/1190
    requires the TLPT scope document to be approved by the management body and validated by the TLPT
    authority before execution begins. Entities that proceed with testing without formal board approval
    have a governance gap in the TLPT process.

17. **Economic loss estimation methodology absent** — Joint Guidelines JC/GL/2024/34 provide the
    methodology for estimating direct and indirect economic losses for major incident classification.
    Entities without a pre-defined loss estimation model cannot rapidly apply the €100,000 direct
    loss threshold and risk both under-reporting (missing reportable incidents) and over-reporting
    (reporting immaterial incidents that create unnecessary supervisory burden).

18. **DORA compliance treated as a one-time project** — DORA is a permanent operational framework.
    Annual reviews of the ICT risk management framework (Article 6), annual register-of-information
    submissions (Article 28(3)), and the 3-year TLPT rolling cycle are all recurring obligations.
    A compliance project that concludes after initial implementation without embedding recurring
    governance cycles will drift into non-compliance.

19. **Ignoring information-security clause gaps in legacy contracts** — Many pre-DORA ICT contracts
    with major vendors lack the mandatory Article 30 provisions (audit rights, exit strategy, TLPT
    participation). These cannot be inserted unilaterally; renegotiation requires commercial leverage
    or legal pressure. Entities should triage legacy contracts, prioritise renegotiating contracts
    for the most critical functions, and document best-effort remediation in the risk register pending
    contract renewal.

20. **GDPR breach notification assumed to satisfy DORA incident reporting** — GDPR Article 33 (72-hour
    breach notification to DPA) and DORA Article 19 (initial notification to NCA) are separate
    obligations to different authorities. A personal data breach that is also a major ICT incident
    triggers both: GDPR Art. 33 to the data protection authority AND DORA Art. 19 to the NCA.
    Parallel notifications with different timelines and different content requirements must be managed
    concurrently.

21. **Concentration risk as a static snapshot** — DORA Article 29 concentration risk assessment
    must be updated when entering new contractual arrangements and when the risk landscape changes
    (e.g., a provider is acquired; a sub-contractor is replaced; a new critical service dependency
    emerges). Organisations that conducted a one-time concentration risk assessment at DORA
    application date without a monitoring mechanism are exposed.

---

## Writing Standards

1. **State requirements with confidence levels**: Never assert a Probable finding as Definite.
   Every finding identifies its regulatory basis (Article, RTS/ITS regulation number) and confidence
   score. Distinguish between Regulation text (Definite) and RTS/ITS interpretive guidance (High or
   Probable).

2. **Distinguish directly applicable Regulation text from ESA guidance**: ESA guidelines and opinions
   are best practice unless adopted into a Commission Regulation. Mark ESA-only requirements as
   [ESA GUIDANCE — confirm status with NCA].

3. **Separate finding from recommendation**: Every finding statement describes what is absent or
   deficient with specificity; every recommendation prescribes the specific action, owner, and
   deadline. "Implement appropriate controls" is not a recommendation. "Obtain board-signed TLPT scope
   document by [date] and submit to NCA for validation" is a recommendation.

4. **Avoid generic compliance language**: "Review incident management procedures" is not a finding.
   "No documented methodology for applying the €100,000 direct economic loss threshold from Commission
   Delegated Regulation (EU) 2024/1772 Article 4" is a finding.

5. **Quantitative thresholds require entity-specific calculation**: Do not state "the entity must
   report incidents with direct economic losses exceeding €100,000" without also noting: "Verify the
   entity has documented the direct economic loss calculation methodology per Joint Guidelines
   JC/GL/2024/34, as this threshold must be applied in real time during incident classification."

6. **DORA is directly applicable — no transposition variation**: Unlike NIS2, DORA does not require
   national transposition. Do not use [JURISDICTION-SPECIFIC] markers for the core DORA obligations.
   Use [JURISDICTION-SPECIFIC] only for: NCA identity and contact details, national penalty amounts,
   and any supplementary national guidance issued by the NCA.

7. **Pre-enforcement transparency**: Where a supervisory interpretation has not yet been tested in
   published enforcement decisions, state: "Based on Regulation text + published RTS/ITS; supervisory
   enforcement interpretation may evolve. Verify current NCA guidance."

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- In Step 3, search for the current text of key DORA Articles (particularly Articles 5, 17, 18, 19,
  26, 28, 30) to verify no amendments have occurred since the regulation came into force
- Search for current EBA, ESMA, EIOPA publications on DORA supervisory expectations and enforcement
  trends
- Search for NCA-specific guidance and contact details for the entity's home Member State
- Search for any CTPP designation updates: "EBA ESMA EIOPA CTPP designation [year]"
- Save the most relevant results to `/tmp/dora-assessment-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Proceed with Regulation text from training data
- Mark all Article and RTS citations with [VERIFY]
- Mark all quantitative thresholds (€100,000 direct loss threshold; penalty amounts; RTO/RPO
  expectations) with [VERIFY — confirm current regulatory text]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend human verification of: (i) current CTPP designation list; (ii) NCA-specific
  incident reporting contact details; (iii) current status of any pending RTS/ITS updates

---

## Output Format Template

```markdown
# DORA Compliance Assessment — [Organisation Name]

**Assessment date**: [YYYY-MM-DD]
**Entity type**: [Article 2 category]
**Regulatory regime**: Full scope (Article 5–45) / Simplified regime (Article 16)
**Member State(s)**: [List]
**Competent Authority(ies)**: [NCA name(s)]
**Assessment mode**: [Readiness / Incident-prep / TLPT-prep / Third-party audit / Greenfield]
**Existing frameworks**: [ISO 27001 / NIST CSF / other]
**TLPT designation status**: [Designated / Likely / Not designated]
**Prepared by**: AI-assisted (legalcode-dora-compliance-assessment)

---

## Executive Summary

**Overall compliance status**: [COMPLIANT / BROADLY COMPLIANT / COMPLIANCE GAP / CRITICAL GAPS]

| Pillar | Status | Critical | Non-Compliant | Partial | Compliant |
|--------|--------|----------|---------------|---------|-----------|
| 1. ICT Risk Management | [✅/⚠️/❌/🚨] | [N] | [N] | [N] | [N] |
| 2. Incident Classification & Reporting | [✅/⚠️/❌/🚨] | [N] | [N] | [N] | [N] |
| 3. Digital Operational Resilience Testing | [✅/⚠️/❌/🚨] | [N] | [N] | [N] | [N] |
| 4. Third-Party ICT Risk Management | [✅/⚠️/❌/🚨] | [N] | [N] | [N] | [N] |
| 5. Information Sharing | [✅/⚠️/❌/🚨] | [N] | [N] | [N] | [N] |

**Top 3 priority actions:**
1. [IMMEDIATE] [Finding] — [Recommended action] — Owner: [Role] — Deadline: [Date]
2. [IMMEDIATE/NEAR-TERM] [Finding] — [Recommended action] — Owner: [Role] — Deadline: [Date]
3. [NEAR-TERM] [Finding] — [Recommended action] — Owner: [Role] — Deadline: [Date]

**TLPT status**: [Next TLPT due: [Date] / Currently in scope: [Yes/No] / Test completed: [Date]]

---

## Regulatory Framework Reference

| Instrument | Subject | Applied From |
|-----------|---------|-------------|
| Regulation (EU) 2022/2554 | Core DORA obligations | 17 January 2025 |
| CDR (EU) 2024/1774 | ICT risk management RTS | 17 January 2025 |
| CDR (EU) 2024/1772 | Incident classification criteria | 17 January 2025 |
| CDR (EU) 2025/301 | Incident reporting timelines | 12 March 2025 |
| CIR (EU) 2025/302 | Incident report forms and templates | 12 March 2025 |
| CDR (EU) 2024/1773 | Third-party ICT policy (critical/important) | 17 January 2025 |
| CIR (EU) 2024/2956 | Register of information templates | See NCA deadline |
| CDR (EU) 2025/532 | Sub-contracting RTS | July 2025 |
| CDR (EU) 2025/1190 | TLPT methodology and requirements | 8 July 2025 |

---

## Entity Classification

**DORA applicability**: [Yes / No / Simplified regime (Article 16)]
**Entity category (Article 2)**: [Category name]
**Simplified regime basis** (if applicable): [PSD2 Art.32 exempt / Small non-interconnected
investment firm / EMD2 Art.9 exempt / Small IORP / Other]
**Assessment scope**: [Full five-pillar assessment / Simplified (Articles 5–16 lite only)]

---

## Pillar 1 — ICT Risk Management Framework

**Overall status**: [✅/⚠️/❌/🚨]

| Sub-element | Classification | Finding | Confidence | Recommended Action |
|-------------|---------------|---------|------------|-------------------|
| 5a. Management body governance (Article 5) | [✅/⚠️/❌/🚨] | [Specific finding] | [Level] | [Action + Owner + Deadline] |
| 5b. ICT risk framework and strategy (Articles 6–7) | [✅/⚠️/❌/🚨] | | | |
| 5c. Identification and asset inventory (Article 8) | [✅/⚠️/❌/🚨] | | | |
| 5d. Protection and prevention (Article 9) | [✅/⚠️/❌/🚨] | | | |
| 5e. Detection (Article 10) | [✅/⚠️/❌/🚨] | | | |
| 5f. Response and recovery / BCP / DRP (Article 11) | [✅/⚠️/❌/🚨] | | | |
| 5g. Backup and restoration (Article 12) | [✅/⚠️/❌/🚨] | | | |
| 5h. Learning and evolving (Article 13) | [✅/⚠️/❌/🚨] | | | |
| 5i. Communication (Article 14) | [✅/⚠️/❌/🚨] | | | |

---

## Pillar 2 — ICT Incident Classification and Reporting

**Overall status**: [✅/⚠️/❌/🚨]

| Sub-element | Classification | Finding | Confidence | Recommended Action |
|-------------|---------------|---------|------------|-------------------|
| 6a. Incident management process (Article 17) | [✅/⚠️/❌/🚨] | | | |
| 6b. Major incident classification criteria (CDR 2024/1772) | [✅/⚠️/❌/🚨] | | | |
| 6c. Reporting timelines and templates (CDR 2025/301) | [✅/⚠️/❌/🚨] | | | |
| 6d. PSD2 dual-reporting resolution (Article 23) | [N/A / ✅/⚠️/❌/🚨] | | | |

**Incident threshold calculation:**
- €100,000 direct economic loss threshold: [Defined / Not defined]
- Loss estimation methodology (JC/GL/2024/34): [In place / Absent]
- NCA incident reporting contact on file: [Yes / No — obtain from: [NCA website]]

**Reporting timeline capability:**
- Initial notification (4h after classification, max 24h after detection): [Capable / Gap]
- Intermediate report (72h): [Capable / Gap]
- Final report (1 month): [Capable / Gap]

---

## Pillar 3 — Digital Operational Resilience Testing

**Overall status**: [✅/⚠️/❌/🚨]
**TLPT mandatory**: [Yes (designated) / No (not designated) / Unknown]

| Sub-element | Classification | Finding | Confidence | Recommended Action |
|-------------|---------------|---------|------------|-------------------|
| 7a. Basic testing programme (Article 25) | [✅/⚠️/❌/🚨] | | | |
| 7b. TLPT designation status | [Designated / Not designated / Unknown] | | | |
| 7c. TLPT scope document (CDR 2025/1190) | [N/A / ✅/⚠️/❌/🚨] | | | |
| 7c. TI phase — threat intelligence provider | [N/A / ✅/⚠️/❌/🚨] | | | |
| 7c. Red team testing readiness | [N/A / ✅/⚠️/❌/🚨] | | | |
| 7c. Purple team debrief plan | [N/A / ✅/⚠️/❌/🚨] | | | |
| 7c. External tester engagement | [N/A / ✅/⚠️/❌/🚨] | | | |
| 7c. Board involvement in TLPT | [N/A / ✅/⚠️/❌/🚨] | | | |

**TLPT timeline:**
- Last TLPT completed: [Date / Not yet conducted]
- Next TLPT due: [Date / To be scheduled]
- External tester identified: [Yes / No — commence procurement]

---

## Pillar 4 — Third-Party ICT Risk Management

**Overall status**: [✅/⚠️/❌/🚨]

| Sub-element | Classification | Finding | Confidence | Recommended Action |
|-------------|---------------|---------|------------|-------------------|
| 8a. Third-party ICT risk strategy (Article 28(1)) | [✅/⚠️/❌/🚨] | | | |
| 8b. Register of information (CIR 2024/2956) | [✅/⚠️/❌/🚨] | | | |
| 8c. Pre-contractual due diligence (Article 28(2)) | [✅/⚠️/❌/🚨] | | | |
| 8d. Contractual provisions — critical/important (Article 30) | [✅/⚠️/❌/🚨] | | | |
| 8e. Sub-outsourcing chain visibility (CDR 2025/532) | [✅/⚠️/❌/🚨] | | | |
| 8f. Concentration risk assessment (Article 29) | [✅/⚠️/❌/🚨] | | | |
| 8g. CTPP oversight exposure (Articles 31–44) | [N/A / ✅/⚠️/❌/🚨] | | | |

**Register of information status:**
- Total ICT contracts documented: [N]
- Critical/important function contracts: [N]
- Annual NCA submission completed: [Yes, date: [Date] / Not yet]
- Sub-outsourcing mapped to tier 2: [Yes / Partial / No]

**Top concentration risk exposures:**
1. [Provider] — [Function] — Substitutability: [High / Medium / Low]
2. [Provider] — [Function] — Substitutability: [High / Medium / Low]

---

## Pillar 5 — Information Sharing

**Overall status**: [✅/⚠️/❌/🚨]

| Sub-element | Classification | Finding | Confidence | Recommended Action |
|-------------|---------------|---------|------------|-------------------|
| 9a. Participation in information sharing arrangement | [N/A (not participating) / ✅/⚠️/❌] | | | |
| 9a. NCA notification of participation (Article 45(3)) | [N/A / ✅/⚠️/❌/🚨] | | | |
| 9a. Arrangement compliance with Article 45 requirements | [N/A / ✅/⚠️/❌] | | | |

---

## Board Governance Assessment (Article 5)

**Overall status**: [✅/⚠️/❌/🚨]

| Governance Element | Classification | Evidence Status | Recommended Action |
|-------------------|---------------|-----------------|-------------------|
| Formal board responsibility for ICT risk documented | [✅/⚠️/❌/🚨] | [Present / Absent / Partial] | |
| Board ICT risk knowledge assessment | [✅/⚠️/❌/🚨] | [Present / Absent / Partial] | |
| ICT risk reporting to management body | [✅/⚠️/❌/🚨] | [Present / Absent / Partial] | |
| Board-approved digital resilience strategy | [✅/⚠️/❌/🚨] | [Present / Absent / Partial] | |
| Board-approved third-party risk strategy | [✅/⚠️/❌/🚨] | [Present / Absent / Partial] | |
| CISO appointment with independent reporting | [✅/⚠️/❌/🚨] | [Present / Absent / Partial] | |

---

## Cross-Directive Alignment

| Directive / Regime | Status | Notes |
|-------------------|--------|-------|
| NIS2 Directive 2022/2555 (lex specialis) | [DORA displaces NIS2 for overlapping obligations / Residual NIS2 obligations: [list]] | |
| GDPR Article 32 (security measures) | [DORA Pillar 1 satisfies GDPR Art. 32 for ICT systems / Verify DPA breach notification obligations are maintained separately] | |
| EBA Guidelines on ICT Risk (EBA/GL/2019/04) | [Superseded by DORA / Confirm internal compliance documents updated to DORA text] | |
| PSD2 Article 96 (if applicable) | [DORA supersedes / Confirm incident classification updated from PSD2 to DORA criteria] | |

---

## Remediation Roadmap

### IMMEDIATE (0–30 days)
| Priority | Finding | Action | Owner | Deadline |
|----------|---------|--------|-------|---------|
| [1] | | | | |

### NEAR-TERM (30–90 days)
| Priority | Finding | Action | Owner | Deadline |
|----------|---------|--------|-------|---------|
| | | | | |

### BACKGROUND (90–180 days)
| Priority | Finding | Action | Owner | Deadline |
|----------|---------|--------|-------|---------|
| | | | | |

### TLPT Planning Timeline (if designated)
| Phase | Target Date | Status | Owner |
|-------|------------|--------|-------|
| NCA confirmation of designation | [Date] | [Status] | Compliance |
| Scope document preparation | [Date] | [Status] | CISO |
| Management body approval of scope | [Date] | [Status] | Board |
| TLPT authority validation | [Date] | [Status] | CISO + NCA |
| TI phase (threat intelligence engagement) | [Date] | [Status] | CISO + TI Provider |
| Red team testing | [Date] | [Status] | CISO + External Red Team |
| Purple team debrief | [Date] | [Status] | CISO |
| Final report + remediation plan | [Date] | [Status] | CISO |
| Management body results presentation | [Date] | [Status] | CISO + Board |

---

## Regulatory Readiness Checklist

| Item | Status | Owner |
|------|--------|-------|
| [ ] DORA applicability confirmed and entity type documented | | |
| [ ] Simplified regime status determined (Article 16) | | |
| [ ] Home Member State NCA identified and incident reporting contact on file | | |
| [ ] ICT risk management framework documented and board-approved | | |
| [ ] Digital operational resilience strategy board-approved | | |
| [ ] CISO or equivalent appointed with independent reporting line | | |
| [ ] ICT asset inventory complete and mapped to critical/important functions | | |
| [ ] BCP and DRP documented, board-approved, and tested in the last 12 months | | |
| [ ] Incident management process with major incident classification criteria documented | | |
| [ ] Direct economic loss methodology for incident classification in place (JC/GL/2024/34) | | |
| [ ] Incident report templates (CIR 2025/302) downloaded and pre-populated | | |
| [ ] Annual basic testing programme (Article 25) in operation | | |
| [ ] TLPT designation status confirmed with NCA | | |
| [ ] TLPT external tester shortlisted (if designated) | | |
| [ ] Register of information (CIR 2024/2956) complete and NCA submission filed | | |
| [ ] Third-party ICT risk strategy board-approved | | |
| [ ] All critical/important function contracts reviewed against Article 30 mandatory provisions | | |
| [ ] Sub-outsourcing chains mapped to tier 2 for critical vendors | | |
| [ ] Concentration risk assessment completed and in risk register | | |
| [ ] CTPP designation list reviewed; contract compliance verified for any CTPP dependencies | | |
| [ ] Information sharing arrangement participation and NCA notification status confirmed | | |
| [ ] Board competency training in ICT risk documented | | |

---

## Quality Assurance

**Citation Quality Gates**: Verify all 5 gates passed before delivery (Source, Format, Currency,
Domain, Confidence). Mark any gate-fail items with the appropriate [UNVERIFIED], [CHECK CURRENCY],
or [UNCERTAIN] tag.

**Self-Interrogation applied to**: [List all CRITICAL and NON-COMPLIANT findings that were
subject to the 3-pass review. Note any findings upgraded or downgraded as a result.]

**Confidence scores**: [Overall: [Level]. Lowest-confidence finding: [Finding + basis for uncertainty]]

---

[GLASS BOX YAML — INSERT COMPLETED YAML BLOCK FROM TEMPLATE ABOVE]
```

---

## Localization Notes

DORA is a directly applicable EU Regulation — there is no member state transposition and no
[JURISDICTION-SPECIFIC] variation in the core obligations. However, the following elements
vary by Member State:

**National Competent Authority (NCA) identity and contact:**

| Sector | Germany | France | Netherlands | Ireland | Luxembourg | Italy | Spain |
|--------|---------|--------|-------------|---------|------------|-------|-------|
| Credit institutions (significant) | ECB/BaFin | ECB/ACPR | ECB/DNB | ECB/CBI | ECB/CSSF | ECB/Banca d'Italia | ECB/BdE |
| Credit institutions (less significant) | BaFin | ACPR | DNB | CBI | CSSF | Banca d'Italia | BdE |
| Investment firms | BaFin | AMF | AFM | CBI | CSSF | Consob / BdI | CNMV |
| Insurance | BaFin | ACPR | DNB | CBI | CAA | IVASS | DGSFP |
| Payment institutions | BaFin | ACPR | DNB | CBI | CSSF | Banca d'Italia | BdE |
| Crypto-assets | BaFin | AMF/ACPR | AFM/DNB | CBI | CSSF | Banca d'Italia | CNMV |

[VERIFY] Confirm current NCA contact details and incident reporting procedures directly with the
relevant authority before filing any DORA notification.

**Register of information submission deadlines** (initial submissions, 2025):
- Many NCAs set April 2025 as the initial register submission deadline
- [VERIFY] national NCA deadline guidance and any extensions — submission requirements and
  deadlines are confirmed by individual NCAs, not by the DORA Regulation text directly

**National penalty levels:**
- DORA Article 50 requires "effective, proportionate and dissuasive" penalties
- National implementing legislation varies in specific fine amounts
- Germany: Individual fines up to €5,000,000; [VERIFY current DORA national penalty implementing act]
- Finland: Maximum individual fine €100,000 (lower than most); [VERIFY current status]
- [VERIFY] penalty implementing legislation in the entity's home Member State before relying on
  specific fine amounts

**CTPP oversight — ESA Lead Overseer assignment:**
- EBA is Lead Overseer for providers most relevant to banking, credit, and payment
- ESMA is Lead Overseer for providers most relevant to capital markets and trading
- EIOPA is Lead Overseer for providers most relevant to insurance
- [VERIFY] current CTPP designation list and Lead Overseer assignments at eba.europa.eu

---

## Glossary

| Term | Definition |
|------|-----------|
| **DORA** | Digital Operational Resilience Act — Regulation (EU) 2022/2554, directly applicable from 17 January 2025 |
| **ICT risk** | Risk of loss related to failures of network and information systems; includes cybersecurity risk |
| **Critical or important function** | A function whose disruption would materially impair financial performance, soundness, or continuity of service to clients or the financial system |
| **Major ICT incident** | An ICT-related incident meeting the classification criteria in Article 18 and Commission Delegated Regulation (EU) 2024/1772 |
| **TLPT (Threat-Led Penetration Test)** | An advanced, adversarial simulation exercise using real threat intelligence to test an entity's live production systems under realistic attack conditions (Article 26) |
| **TIBER-EU** | Threat Intelligence Based Ethical Red-teaming framework developed by the ECB; DORA TLPT is closely aligned with and draws on TIBER-EU methodology |
| **CTPP (Critical ICT Third-Party Service Provider)** | A provider designated by the ESAs under DORA Articles 31–32 based on systemic importance to the EU financial system |
| **Lead Overseer** | The ESA (EBA, ESMA, or EIOPA) assigned as primary supervisor for each designated CTPP |
| **JET (Joint Examination Team)** | Cross-authority team formed by the Lead Overseer and relevant NCAs to conduct on-site inspections of CTPPs |
| **Register of Information (RoI)** | Comprehensive register of all contractual ICT arrangements maintained at entity, sub-consolidated, and consolidated group levels under Article 28(3) |
| **RTS** | Regulatory Technical Standard — binding Commission Delegated Regulation specifying technical requirements |
| **ITS** | Implementing Technical Standard — binding Commission Implementing Regulation specifying forms, templates, and procedures |
| **NCA** | National Competent Authority — the home Member State supervisor responsible for DORA oversight of the entity |
| **ESA** | European Supervisory Authority — EBA (banking), ESMA (securities), EIOPA (insurance) |
| **Simplified regime** | The lighter ICT risk management framework available to qualifying smaller entities under Article 16 |
| **Lex specialis** | Principle that DORA, as a more specific regulation, displaces the more general NIS2 Directive for overlapping obligations applicable to financial sector entities |
| **RPO** | Recovery Point Objective — maximum acceptable data loss, measured as time, that a system can sustain in a disaster scenario |
| **RTO** | Recovery Time Objective — maximum acceptable time to restore a system or function after a disruption |
| **BCP** | Business Continuity Plan — documented procedures to maintain critical business functions during and after a disruptive event |
| **DRP** | Disaster Recovery Plan — technical procedures to restore ICT systems after a major outage or disaster |
| **Purple team exercise** | A mandatory TLPT phase involving collaboration between the red team (attackers) and blue team (defenders) to assess detection capabilities and validate findings |

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis produced using the Legalcode 2-agent
research pipeline combining:
- **Structural Agent**: Deep analysis of the `legalcode-nis2-compliance-assessment` reference
  skill; extraction of NIS2 structural patterns, quality frameworks, and anti-pattern catalogue
  for adaptation to DORA
- **Legal Research Agent**: Comprehensive web research covering Regulation (EU) 2022/2554 text,
  all 27 finalized RTS/ITS, EBA/ESMA/EIOPA implementation guidance, BaFin/CSSF/CBI national
  guidance, TIBER-EU framework documentation, and one-year post-application analyses

**Primary sources consulted:**
- Regulation (EU) 2022/2554 (EUR-Lex)
- Commission Delegated Regulation (EU) 2024/1774 — ICT risk management RTS
- Commission Delegated Regulation (EU) 2024/1772 — Incident classification RTS
- Commission Delegated Regulation (EU) 2025/301 — Incident reporting RTS
- Commission Implementing Regulation (EU) 2025/302 — Incident reporting ITS
- Commission Delegated Regulation (EU) 2024/1773 — Third-party ICT policy RTS
- Commission Implementing Regulation (EU) 2024/2956 — Register of information ITS
- Commission Delegated Regulation (EU) 2025/532 — Sub-contracting RTS
- Commission Delegated Regulation (EU) 2025/1190 — TLPT RTS
- Commission Delegated Regulation (EU) 2024/1502 — CTPP designation criteria
- ESAs Joint Report JC 2024/108 — Single EU Hub feasibility
- Joint Guidelines JC/GL/2024/34 — Economic loss estimation methodology
- EBA ESMA EIOPA press release November 2025 — First CTPP designations
- BaFin DORA Implementation Guidance (July 2024)
- EY Luxembourg — DORA One Year Later (2025)
- DLA Piper — Divergence in Administrative Penalties under DORA (October 2025)

**Legal review requirement**: All findings and recommendations should be reviewed by a qualified
DORA compliance officer and qualified financial-sector legal professional licensed in the relevant
jurisdiction before relying on them for regulatory submissions or compliance certifications.
