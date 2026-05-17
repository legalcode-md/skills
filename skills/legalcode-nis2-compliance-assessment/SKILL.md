---
name: legalcode-nis2-compliance-assessment
description: >
  NIS2 Directive (EU 2022/2555) compliance assessment for essential and important entities
  covering entity classification (essential vs. important), all ten Article 21 risk management
  measures, Article 23 incident reporting obligations (24-hour early warning, 72-hour
  notification, one-month final report), Article 32 board accountability and training mandates,
  supply chain security requirements, cross-border cooperation, and intersection with GDPR,
  DORA, and sector-specific regulations. Use when an organization needs to determine NIS2
  applicability, assess compliance posture against the ten risk management measures, design
  incident reporting procedures, prepare for supervisory examination, or understand member
  state transposition variations. Covers entity classification gates, all ten Article 21
  measures with implementation checklists and evidence requirements, incident significance
  thresholds and reporting timelines, supply chain risk methodology, board-level governance,
  and cross-directive alignment. Produces compliance assessments with COMPLIANT/PARTIAL/
  NON-COMPLIANT/CRITICAL classifications, prioritized remediation roadmaps with timelines,
  incident reporting readiness checklists, and board-level governance recommendations.
  Jurisdiction-agnostic core (NIS2 Directive 2022/2555) with [JURISDICTION-SPECIFIC] markers
  for national implementations across EU member states and sector-specific variations.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# NIS2 Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance with
> the NIS2 Directive (EU 2022/2555) and its national transpositions. It does not constitute
> legal advice, regulatory guidance, or a compliance certification. The NIS2 Directive is
> recent legislation with ongoing national transpositions and evolving supervisory guidance —
> verify all statutory references, thresholds, and deadlines against current national
> implementation law before relying on them. AI-generated legal analysis carries hallucination
> risk for cited authority: any statutory references, ENISA guideline citations, or regulatory
> interpretations should be independently verified by a qualified information security legal
> professional licensed in the relevant jurisdiction. This skill does not replace a formal
> compliance audit conducted by a qualified auditor.

## Purpose and Scope

This skill assesses an organization's compliance posture against the EU NIS2 Directive
(Directive 2022/2555 on measures for a high common level of cybersecurity across the Union).
It covers the full NIS2 obligation stack: entity classification, risk management measures,
incident reporting, board accountability, supply chain security, cross-border cooperation,
and cross-directive alignment.

**Covers:**
- Entity classification assessment (essential vs. important entity determination; size thresholds;
  sectoral criteria; self-identification obligations under Article 3)
- Article 21 ten minimum security measures — all ten, with implementation checklists, evidence
  requirements, and proportionality guidance for important entities
- Article 23 incident reporting: significant incident definition, financial loss thresholds,
  three-stage reporting timeline (24h early warning / 72h notification / one-month final report),
  and national CSIRT coordination
- Article 32 board accountability: management liability, mandatory awareness training,
  personal liability under national transpositions, and audit obligations
- Supply chain security: third-party and vendor risk management, contractual security clauses,
  and circular dependency analysis for critical service providers
- Cross-border cooperation: information sharing, EU-CyCLONe, CSIRT network participation,
  and multi-member-state reporting obligations
- Cross-directive alignment: GDPR Article 32 security measures overlap, DORA operational
  resilience intersection (financial sector), and sector-specific regulatory overlays
  (EECC for telecom, NIS2 + ACER for energy, EBA guidelines for finance, sector-specific CAs)
- Member state transposition variations: national competent authority identification,
  enforcement timelines by member state, sector-specific national rules
- Remediation roadmap: IMMEDIATE / NEAR-TERM / BACKGROUND prioritization tiers

**Does not:**
- Certify NIS2 compliance (compliance certifications require accredited audit)
- Provide jurisdiction-by-jurisdiction legal opinions on national transpositions
- Replace the supervisory examination process of any national competent authority
- Assess ISO 27001 / NIST CSF / SOC 2 gap analysis (those frameworks overlap but differ)
- Cover NIS1 (Directive 2016/1148) obligations where not already superseded by NIS2
- Provide legal advice on sanctions exposure or litigation strategy

**Related skills:**
- `legalcode-dpia-generator` — GDPR Article 35 DPIA; required for high-risk processing; integrates with NIS2 Art. 21 security measures
- `legalcode-breach-regulatory-notification-drafter` — multi-regime breach notification including NIS2 Art. 23 draft templates
- `legalcode-eu-ai-act-high-risk-compliance` — EU AI Act compliance for AI systems deployed within NIS2-covered networks
- `legalcode-data-processing-agreement-drafter` — GDPR Art. 28 DPAs for supply chain vendors who also process personal data
- `legalcode-vendor-privacy-assessment` — vendor due diligence framework; extend for NIS2 supply chain security obligations

---

## Jurisdiction and Governing Law

**Primary legislation**: EU Directive 2022/2555 (NIS2), entered into force 16 January 2023;
transposition deadline for member states: 17 October 2024.

**Key articles for this skill:**
- Article 2 — Scope and entity coverage
- Article 3 — Essential and important entity classification
- Article 4 — Annex I and II sector lists
- Article 20 — Governance obligations (management accountability)
- Article 21 — Cybersecurity risk management measures (ten minimum measures)
- Article 23 — Reporting obligations for significant incidents
- Article 24 — Use of European cybersecurity certification schemes
- Article 32 — Supervisory and enforcement measures for essential entities
- Article 33 — Supervisory and enforcement measures for important entities
- Annexes I and II — Sector lists determining entity classification

**Important national transpositions** [JURISDICTION-SPECIFIC]:
- **Germany (DE)**: NIS2UmsuCG enacted December 5, 2025; in force December 6, 2025. Amends
  BSI Act (BSIG). BSI (Federal Office for Information Security) is competent authority.
  KRITIS threshold retained for third entity category. Registration deadline: April 2026.
  In-scope entities may increase from ~4,500 to ~29,000 organizations.
- **France (FR)**: ANSSI (national cybersecurity agency) is competent authority. [VERIFY
  current status of transposition legislation — deadline was October 2024; verify enactment.]
- **Netherlands (NL)**: [VERIFY current transposition act and NCSC/RDI authority scope.]
- **Poland (PL)**: [VERIFY current amendment to the Act on the National Cybersecurity System.]
- **Ireland (IE)**: [VERIFY NIS2 Regulations SI (Statutory Instrument) status post-October 2024.]
- **Sweden (SE)**: [VERIFY transposition status and NCSC authority scope.]

**Sector scope (Annex I — Highly Critical)**: Energy (electricity, oil, gas, district heating),
transport (air, rail, road, water), banking, financial market infrastructure, health, drinking
water, wastewater, digital infrastructure (IXPs, DNS, TLD, cloud computing, data centre,
CDN, TSP, electronic communications networks), ICT service management (B2B MSPs and MSSPs),
public administration, space.

**Sector scope (Annex II — Other Critical)**: Postal and courier services, waste management,
manufacture/production/distribution of chemicals, food production/processing/distribution,
manufacturing (medical devices, computers, electronics, electrical equipment, machinery,
motor vehicles), digital providers (online marketplaces, online search engines, social
networking platforms).

**Supervisory model**: NIS2 uses **distributed non-hierarchical supervision** — 27 national
competent authorities (one or more per member state) plus ENISA (advisory capacity) plus
sectoral regulators (ACER for energy, EBA/ECB for finance, BEREC for telecom). No single
pan-EU NIS2 supervisor. For cross-border incidents, the member state where the entity has
its main establishment leads.

**Penalties** [JURISDICTION-SPECIFIC]:
- **Essential entities**: Up to €10,000,000 or 2% of total worldwide annual turnover,
  whichever is higher.
- **Important entities**: Up to €7,000,000 or 1.4% of total worldwide annual turnover,
  whichever is higher.
- **Board-level personal liability**: Many member states (including Germany's NIS2UmsuCG)
  create direct personal liability for management board members for NIS2 violations. [VERIFY
  personal liability provisions in specific member state transpositions.]

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
- **System description**: Organization overview, sector, size, geographic presence, and
  existing security documentation (risk assessments, incident response plans, policies)
- **Document set**: Uploaded security policies, risk registers, supplier agreements,
  incident response procedures, training records
- **Gap analysis request**: Prior assessment findings for re-evaluation
- **New implementation**: Greenfield organization building NIS2 compliance from scratch

**Minimum required context**: Organization name, primary sector (Annex I or II), member
state(s) of main establishment, and approximate organization size (revenue + employee count).

### Step 2: Gather Context

**⟁ CLARIFY** — Gather context before beginning the assessment. Ask (skip questions already answered):

1. **Assessment mode**: What is the primary objective?
   - *Readiness assessment*: Full gap analysis of current state against all NIS2 requirements
   - *Incident reporting preparation*: Focus on Art. 23 timelines, thresholds, and CSIRT contacts
   - *Supervisory examination preparation*: Document readiness for imminent inspection
   - *Implementation roadmap*: Building NIS2 compliance from greenfield
   - **Why this matters**: Determines output focus and depth of assessment.

2. **Entity classification confidence**: Has the organization performed entity self-identification?
   - *Yes — classified as essential entity*: Proceed to full assessment
   - *Yes — classified as important entity*: Note proportionality provisions in Step 4
   - *Not yet performed*: Classification gate is Step 4; perform classification first
   - **Why this matters**: Essential and important entities have different obligation intensities and supervisory regimes.

3. **Member state(s)**: Which member state(s) is this assessment for?
   - *Single member state*: [Specify which — applies national transposition]
   - *Multiple member states*: [List — multi-jurisdiction assessment required]
   - *Unknown/pre-assessment*: Jurisdiction-agnostic assessment; national transposition TBD
   - **Why this matters**: National transpositions differ significantly; competent authority, timeline, and specific national requirements vary.

4. **Sector and overlap**: What sector(s) does the organization operate in?
   - *Annex I sector (highly critical)*: Energy, transport, banking, financial market infrastructure, health, water, digital infrastructure, ICT B2B, public administration, space
   - *Annex II sector (other critical)*: Postal, waste, chemicals, food, manufacturing, digital providers
   - *Multiple sectors or vertical integration*: Identify primary sector; note sector-specific overlays
   - **Why this matters**: Sector determines applicable sectoral regulations (DORA for finance, EECC for telecom, etc.) and sector-specific ENISA technical guidelines.

5. **Existing security framework**: Does the organization currently operate under any security framework?
   - *ISO 27001 certified*: Use existing controls as baseline; identify NIS2-specific gaps
   - *NIST CSF implemented*: Map NIST functions to Art. 21 measures
   - *No formal framework*: Begin from first principles; longer assessment
   - *NIS1 compliant*: Identify delta changes under NIS2 (expanded scope, stricter measures)
   - **Why this matters**: Existing frameworks accelerate assessment; NIS2 gaps are identifiable rather than building from zero.

6. **Compliance maturity**: What is the current compliance posture?
   - *Greenfield (no controls)*: Full implementation roadmap required
   - *Partial (some controls in place)*: Gap analysis and remediation roadmap
   - *Mature (most controls in place)*: Verification and documentation assessment
   - **Why this matters**: Calibrates assessment depth and output focus (build vs. verify vs. remediate).

### Step 3: Gather Legal Authority

Before assessing, gather current legal authority for the assessment:

**With legalcode-mcp connected:**
- Search: "NIS2 Directive 2022/2555 [Article N]" — verify current text and ENISA guidance
- Search: "[Member State] NIS2 transposition [national act name]" — verify national implementation
- Search: "ENISA NIS2 [sector] guidelines [year]" — verify sector-specific guidance currency
- Search: "NIS2 competent authority [member state]" — verify current supervisory authority
- Save results to `/tmp/nis2-assessment-research.md`
- Mark all verified citations as VERIFIED in Glass Box

**Without legalcode-mcp:**
- Proceed with Directive text from training data
- Mark all citations [VERIFY] — particularly national transpositions (evolving as of March 2026)
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus assessment on Directive text and published ENISA guidelines
- Recommend human legal review of all national transposition findings

### Step 4: Entity Classification Gate

**BINARY GATE — Apply this test before assessing any risk management measures.**

If the organization is clearly out of scope, provide the classification determination and stop.
If in scope, identify entity tier (essential or important) and proceed to Step 5.

#### 4a. Scope Determination (Article 2)

NIS2 applies when the entity:
1. **Sector test**: Operates in a sector listed in Annex I or Annex II (see Jurisdiction section)
2. **Size test**: Qualifies as medium-sized or large enterprise:
   - Medium: 50+ employees AND/OR €10M+ annual turnover/balance sheet
   - Large: 250+ employees AND/OR €50M+ annual turnover OR €43M+ balance sheet
   - Note: Size thresholds do NOT apply to certain entities (public administration, critical
     service providers, essential entities designated regardless of size by national authority)
3. **Establishment test**: Provides services in the EU or is established in the EU

**Entities excluded regardless of size** (certain categories are essential by law):
- Qualified trust service providers
- TLD name registries and DNS service providers
- Internet exchange points
- Providers of public electronic communications networks/services

**OUT OF SCOPE determination**: If the organization fails the sector test or size test
and is not excluded-by-law, state: "Organization appears out of scope for NIS2. No
further assessment required. Recommend verification with national competent authority
if scope is uncertain."

#### 4b. Essential vs. Important Entity Determination (Article 3)

| Criterion | Essential Entity | Important Entity |
|-----------|-----------------|-----------------|
| Sector | Annex I | Annex II |
| Size | Large enterprise (250+ employees / €50M+ turnover) | Medium or large enterprise |
| Designation | Designated essential by national authority | Annex II by default (if size met) |
| Supervisory model | **Proactive supervision** — ex ante inspections, regular audits | **Reactive supervision** — ex post inspections triggered by incidents or complaints |
| Fines | Up to €10M or 2% global turnover | Up to €7M or 1.4% global turnover |
| Special rules | Annex I entities regardless of size: trust service providers, TLD, DNS, IXPs, telecom providers | Annex II medium-large entities; some sectors designated at national discretion |

**Note on proportionality**: Essential entities cannot claim blanket proportionality
exemptions on Art. 21 measures. Important entities have limited proportionality under
Art. 21(4) — "simplified" measures may be permitted for some low-risk implementations.
Consult national competent authority guidance.

### Step 5: Legal Authority Research

Gather sector-specific and member state-specific guidance:
- Identify the competent authority for the entity's sector and member state [JURISDICTION-SPECIFIC]
- Locate ENISA sector-specific guidelines (ENISA publishes implementation guidance for
  each sector category; check enisa.europa.eu for current versions)
- Identify any sectoral implementing regulations (Commission Implementing Regulations for
  DNS providers, cloud providers, digital infrastructure — published 2024)
- Note enforcement timeline for the member state [JURISDICTION-SPECIFIC] [VERIFY]

### Step 6: Assess Article 21 Measure 1 — Risk Assessment and Risk Management

**Article 21(2)(a)**: Policies on risk analysis and information system security.

**Implementation requirements:**
- [ ] Formal cybersecurity risk assessment conducted and documented
- [ ] Risk assessment methodology defined (asset identification → threat assessment → vulnerability assessment → likelihood/impact scoring → risk ranking)
- [ ] Risk assessment updated at least annually and after significant changes
- [ ] Management approval of risk assessment documented
- [ ] Risk treatment plan derived from risk assessment with remediation owners and deadlines
- [ ] Residual risk acceptance criteria defined and documented

**Evidence required**: Written risk assessment policy; completed risk register; management sign-off record; treatment plan with status tracking.

**Proportionality note**: Risk assessment scope should match organization size and sector
criticality. A small Annex II entity with limited digital services needs a proportionate
risk assessment — not a full enterprise-grade assessment. However, **all essential entities
must conduct comprehensive risk assessments with no proportionality exceptions.**

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 7: Assess Article 21 Measure 2 — Incident Handling

**Article 21(2)(b)**: Incident handling.

**Implementation requirements:**
- [ ] Incident response plan (IRP) documented and approved by management
- [ ] Incident classification criteria defined (including NIS2 "significant incident" threshold — see Step 14)
- [ ] Incident detection capabilities operational (SIEM, alerting, or equivalent)
- [ ] Incident response roles and responsibilities documented (RACI)
- [ ] Incident communication procedures documented (internal escalation + external reporting)
- [ ] Post-incident review (lessons-learned) process defined
- [ ] IRP tested (tabletop exercise or equivalent) at least annually

**Evidence required**: Approved IRP document; incident log/register; exercise record; post-incident review reports.

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 8: Assess Article 21 Measure 3 — Business Continuity and Crisis Management

**Article 21(2)(c)**: Business continuity, backup management, disaster recovery, and crisis management.

**Implementation requirements:**
- [ ] Business continuity plan (BCP) documented covering service disruption scenarios
- [ ] Disaster recovery plan (DRP) with defined RTO and RPO targets
- [ ] Backup strategy documented: backup frequency, retention, offsite/immutable storage
- [ ] Backup restoration tested at least annually
- [ ] Crisis management escalation procedure defined (who decides what, at what threshold)
- [ ] BCP/DRP aligned with incident response plan (measure 2 integration)

**Evidence required**: Approved BCP and DRP; backup policy; restoration test records; crisis management procedure.

**Glossary**: RTO = Recovery Time Objective (target time to restore service); RPO = Recovery Point Objective (maximum acceptable data loss window).

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 9: Assess Article 21 Measure 4 — Supply Chain Security

**Article 21(2)(d)**: Supply chain security, including security-related aspects concerning
the relationships between each entity and its direct suppliers or service providers.

**Implementation requirements:**
- [ ] Supplier/vendor inventory maintained (all third parties with system access or data access)
- [ ] Supplier risk classification criteria defined (criticality tiers: critical, high, standard)
- [ ] Security due diligence process for new suppliers documented
- [ ] Contractual security requirements in supplier agreements (incident notification, audit rights, security standards)
- [ ] Ongoing supplier monitoring process (periodic re-assessment of critical suppliers)
- [ ] Process for revoking supplier access upon contract termination
- [ ] Assessment of ICT product/service security: ENISA European Cybersecurity Certification Schemes considered

**Evidence required**: Vendor register; supplier risk tiers; standard contractual security clauses; due diligence questionnaire; monitoring records.

**⟁ CLARIFY** — Supply chain complexity:
1. *Simple (few suppliers, limited system access)*: Basic due diligence and contractual clauses sufficient
2. *Complex (many critical suppliers, shared infrastructure)*: Full supplier risk management program required
3. *Critical service provider status*: Organization may itself be a supplier to other essential entities — assess circular dependency

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 10: Assess Article 21 Measure 5 — Secure Acquisition, Development, and Maintenance

**Article 21(2)(e)**: Security in network and information systems acquisition, development,
and maintenance, including vulnerability handling and disclosure.

**Implementation requirements:**
- [ ] Secure development lifecycle (SDLC) policy documented (if software is developed internally)
- [ ] Security requirements defined at acquisition phase for all new systems/services
- [ ] Patch and vulnerability management policy: assessment, prioritization, remediation timelines
- [ ] Penetration testing or vulnerability scanning conducted at defined frequency
- [ ] Vendor security patch commitments included in procurement contracts
- [ ] Vulnerability disclosure process defined for own systems (if applicable)
- [ ] Change management process includes security impact assessment

**Evidence required**: SDLC policy; patch management policy; vulnerability scan reports; pen test reports; change management records.

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 11: Assess Article 21 Measure 6 — Effectiveness Assessment

**Article 21(2)(f)**: Policies and procedures to assess the effectiveness of cybersecurity
risk management measures.

**Implementation requirements:**
- [ ] Internal audit or review program for cybersecurity controls defined
- [ ] Key performance indicators (KPIs) or metrics for cybersecurity effectiveness documented
- [ ] Management review of cybersecurity posture at defined intervals
- [ ] Third-party assessment or certification considered (ISO 27001, SOC 2, sector-specific)
- [ ] Audit findings tracked to remediation with ownership and deadlines
- [ ] Continuous monitoring program operational (logs, alerts, dashboards)

**Evidence required**: Audit plan; KPI/metrics reports; management review records; third-party assessment reports (if applicable).

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 12: Assess Article 21 Measure 7 — Cybersecurity Hygiene and Training

**Article 21(2)(g)**: Basic cyber hygiene practices and cybersecurity training.

**Implementation requirements:**
- [ ] Cybersecurity awareness training program documented and operationalized
- [ ] Training covers: phishing, social engineering, password security, data handling, device security
- [ ] All employees receive training at least annually; new starters at onboarding
- [ ] Privileged users (admins, IT staff) receive enhanced technical training
- [ ] Management/board receives NIS2-specific governance training (Art. 20 requirement)
- [ ] Training completion records maintained
- [ ] Phishing simulation or equivalent testing conducted

**Evidence required**: Training program documentation; completion records; training content; management training records.

**Important**: Article 20 requires that management body members receive training in
cybersecurity. This is a mandatory separate requirement from general employee awareness.

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 13: Assess Article 21 Measure 8 — Cryptography

**Article 21(2)(h)**: Policies and procedures regarding the use of cryptography and,
where appropriate, encryption.

**Implementation requirements:**
- [ ] Cryptography policy documented: approved algorithms, key lengths, key management
- [ ] Data classification scheme drives encryption requirements (at rest + in transit)
- [ ] Encryption of sensitive data at rest (AES-256 or equivalent)
- [ ] Encryption in transit: TLS 1.2 minimum; TLS 1.3 preferred for new deployments
- [ ] Encryption key management: generation, storage, rotation, revocation, destruction
- [ ] Certificate management program: inventory, expiry monitoring, renewal procedures
- [ ] End-to-end encryption for particularly sensitive communications [where applicable]

**Evidence required**: Cryptography policy; data classification policy; key management procedure; certificate inventory.

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 14: Assess Article 21 Measure 9 — Human Resources Security and Access Control

**Article 21(2)(i)**: Human resources security, access control policies, and asset management.

**Implementation requirements:**
- [ ] Access control policy documented (need-to-know, least-privilege principles)
- [ ] Identity and access management (IAM): user provisioning, access reviews, offboarding
- [ ] Multi-factor authentication (MFA) required for remote access and admin accounts
- [ ] Privileged access management (PAM): separate accounts, Just-in-Time (JIT) access
- [ ] Asset management: hardware and software inventory maintained (network-connected assets)
- [ ] Personnel security measures: background checks where applicable and legally permissible [JURISDICTION-SPECIFIC]
- [ ] Secure remote access: VPN, zero-trust architecture, or equivalent
- [ ] Secure emergency communication systems [for essential entities in critical sectors]

**Evidence required**: Access control policy; IAM records; MFA implementation evidence; asset inventory; access review records.

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 15: Assess Article 21 Measure 10 — Multi-Factor Authentication and Secure Communications

**Article 21(2)(j)**: Use of multi-factor authentication or continuous authentication
solutions, secure voice, video, and text communications, and secure emergency communications.

**Implementation requirements:**
- [ ] MFA implemented for: all remote access, all administrative access, all cloud service access, email access for privileged roles
- [ ] Continuous authentication mechanisms considered for high-risk systems (behavioral analytics, zero-trust)
- [ ] Secure communications policy: approved channels for sensitive communications
- [ ] Voice, video, and text communications: encrypted channels mandated for sensitive topics
- [ ] Emergency communication systems: secure, resilient, and tested independently of primary channels
- [ ] No reliance on SMS-only MFA for high-privilege accounts (phishing-resistant MFA preferred)

**Evidence required**: MFA deployment records; secure communications policy; emergency communication system documentation; MFA coverage scope.

**Note**: Measures 9 and 10 overlap in access control and MFA. Assess together but score
separately — many organizations have MFA deployed but lack the access control policy (measure
9) or lack secure emergency communications (measure 10).

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 16: Incident Reporting Assessment (Article 23)

Article 23 creates **time-critical obligations** that must be operationalized in advance.
Do not assess this section as a future plan — verify that procedures are ready to execute
within the required timelines.

#### 16a. Significant Incident Threshold

A "significant incident" triggers the three-stage reporting obligation. An incident is
significant if it meets any of these criteria:

**Financial threshold** (Implementing Regulation): Direct financial loss exceeding €500,000
or 5% of total annual turnover in the previous financial year, whichever is lower.

**Service disruption criteria** (from Article 23 and Recitals):
- Has caused or is capable of causing severe operational disruption of services
- Affects a large number of users
- Causes geographical spread (cross-border impact)
- Causes significant damage to physical or digital infrastructure
- Causes considerable reputational damage (e.g., media reporting; likely customer loss with material business impact)
- Involves exfiltration of trade secrets
- Causes death or considerable damage to health of a natural person
- Involves successful unauthorized access to network and information systems

**Assessment question**: Has the organization defined internal incident significance thresholds
that map to NIS2 criteria? If thresholds are undefined, the 24-hour early warning clock may
expire before a reporting decision is made.

- [ ] Significant incident definition documented (with NIS2-specific criteria)
- [ ] Internal classification criteria for significance operationalized (decision criteria, not just policy)
- [ ] Decision-maker(s) identified for significance classification

#### 16b. Three-Stage Reporting Timeline

| Stage | Deadline | Recipient | Content |
|-------|----------|-----------|---------|
| **Early Warning** (Art. 23.1) | **24 hours** from detecting a significant incident | CSIRT or national competent authority | Brief alert: occurrence, nature of incident (if known), any cross-border impact indicator |
| **Incident Notification** (Art. 23.4) | **72 hours** from detecting a significant incident | CSIRT or national competent authority | Initial assessment: severity, impact assessment, indicators of compromise (if known), status of incident |
| **Final Report** (Art. 23.4(c)) | **One month** from submitting notification | CSIRT or national competent authority | Detailed description, threat type, root cause analysis, impact summary, mitigation measures applied, cross-border impact assessment |

**Additional timing notes**:
- If incident still ongoing at one-month mark: submit progress report; final report upon resolution
- For incidents affecting multiple member states: report to each national CSIRT/CA; lead authority is member state of main establishment
- Early warning (24h) does NOT require root cause analysis — it is an alert, not an investigation report

**Assessment checklist**:
- [ ] 24-hour early warning procedure documented and assigned to identified role
- [ ] 72-hour notification template prepared with required content fields
- [ ] One-month final report template prepared
- [ ] CSIRT/competent authority contact information current and accessible
- [ ] Decision tree for significance classification operable in real-time (not requiring post-incident investigation to trigger)
- [ ] Multi-member-state reporting procedure if cross-border operations exist
- [ ] "Voluntary reporting" channel identified for near-miss or non-significant incidents (Art. 30)

**Classification for incident reporting readiness**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 17: Board Accountability Assessment (Article 20 and 32)

Article 20 requires management bodies to approve cybersecurity risk management measures
and oversee their implementation. Board members face personal liability in many member states.

**Assessment requirements:**
- [ ] Management body has formally approved the organization's NIS2 risk management framework (documented approval, board minutes, or equivalent)
- [ ] Management body receives regular cybersecurity briefings (at defined intervals — recommended quarterly)
- [ ] Management body members have completed NIS2-specific cybersecurity training (Art. 20(2) requirement — mandatory, not optional)
- [ ] Responsibility for NIS2 compliance assigned to named senior officer (CISO, CTO, DPO, or equivalent)
- [ ] Management body has been informed of the sanctions regime (personal liability under national transpositions) [JURISDICTION-SPECIFIC]
- [ ] Internal audit or equivalent mechanism reports to management body on NIS2 compliance status
- [ ] Management body reviewed and approved the incident response policy (Measure 2)

**Assessment of board cybersecurity competence:**
- Does the board understand the distinction between essential and important entity obligations?
- Can the board articulate the 24-hour early warning obligation and who is responsible?
- Has the board discussed supply chain risk at the governance level?
- Is there a named board member (or subcommittee) accountable for cybersecurity oversight?

**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT / 🚨 CRITICAL

### Step 18: Cross-Directive Alignment Assessment

**⟁ CLARIFY** — Cross-directive scope:
1. *General organization*: Assess GDPR Art. 32 overlap only
2. *Financial sector*: Assess GDPR + DORA (Regulation 2022/2554) intersection
3. *Telecom provider*: Assess GDPR + EECC (Directive 2018/1972) intersection
4. *Health sector*: Assess GDPR + NIS2 + national health data regulations
5. **Why this matters**: Different sectors have layered obligations that create both overlapping requirements (where NIS2 compliance satisfies GDPR Art. 32) and divergent requirements (where DORA creates stricter standards not fully captured by NIS2).

#### 18a. GDPR Article 32 Alignment

GDPR Article 32 requires "appropriate technical and organisational measures" to ensure
security. NIS2 Article 21 overlaps significantly with GDPR Art. 32.

**Alignment mapping**:
| NIS2 Art. 21 Measure | GDPR Art. 32 Equivalent |
|---------------------|------------------------|
| Measure 1: Risk assessment | Art. 32(1): Assessment of risks |
| Measure 2: Incident handling | Art. 33/34: Breach notification + remediation |
| Measure 3: Business continuity | Art. 32(1)(c): Resilience of processing systems |
| Measure 5: Secure development | Art. 32(1): Appropriate technical measures |
| Measure 8: Cryptography | Art. 32(1)(a): Pseudonymisation and encryption |
| Measure 9: Access control | Art. 32(1)(b): Ongoing confidentiality assurance |
| Measure 10: MFA | Art. 32(1)(b): Ongoing integrity and availability |

**Assessment**: Where GDPR Art. 32 measures are documented for personal data processing,
verify that NIS2 measures cover the full scope of network and information systems (not
just personal data systems).

#### 18b. DORA Alignment (Financial Sector Only)

For entities subject to DORA (Regulation 2022/2554) — credit institutions, investment
firms, payment institutions, insurance companies, crypto-asset service providers:
- DORA's ICT risk framework (Chapter II) partially overlaps NIS2 Art. 21
- DORA incident reporting (Chapter III) has different thresholds and timelines than NIS2 Art. 23
- DORA's digital operational resilience testing (Chapter IV) goes beyond NIS2 effectiveness assessment (Measure 6)
- **Key conflict**: DORA reporting timelines may differ from NIS2 Art. 23; identify which obligation is stricter and apply highest common denominator

**Assessment**: Document DORA / NIS2 obligations in parallel; identify any conflicts; apply strictest standard and document rationale.

#### 18c. Sector-Specific Overlays [JURISDICTION-SPECIFIC]

| Sector | Applicable Overlay | Interaction with NIS2 |
|--------|-------------------|-----------------------|
| Telecom | EECC Directive 2018/1972 | Security measures + incident reporting pre-dated NIS2; review for stricter requirements |
| Energy | ACER/TSO sector rules | Energy sector NIS2 Annex I entities; additional sector-specific ENISA guidelines |
| Finance | DORA + EBA guidelines | See 18b above; DORA generally stricter; apply DORA standard |
| Health | National health data law | Personal health data adds GDPR sensitivity + sector-specific confidentiality rules |
| Water | National water authority | Infrastructure protection laws may add physical security requirements |

### Step 19: Generate Assessment Output

Apply the classification system and generate the output using the Output Format Template below.

---

## Classification System

### Four-Tier Compliance Classification

| Tier | Symbol | Definition | Required Action |
|------|--------|-----------|----------------|
| **COMPLIANT** | ✅ | Measure fully implemented, documented, tested, and demonstrably operationalized. Evidence available. No material gaps. | No immediate action required. Maintain and monitor. |
| **PARTIAL** | ⚠️ | Measure exists but with identifiable gaps. Implementation incomplete. Documentation missing or outdated. Policy exists but not operationalized. | Action within 90 days. Address gaps, update documentation, test operationalization. |
| **NON-COMPLIANT** | ❌ | Measure not meaningfully implemented or fundamentally deficient. Significant deviation from NIS2 requirements. | Near-term remediation (30-90 days). Priority action with ownership and deadline. |
| **CRITICAL** | 🚨 | Measure entirely absent, non-functional, or creates immediate cybersecurity risk to the organization's core services. Supervisory enforcement risk if incident occurs. | Immediate remediation (0-30 days). Escalate to management. No delay acceptable. |

### Prioritization Framework

| Priority | Timeframe | Triggers |
|----------|-----------|---------|
| **IMMEDIATE** | 0–30 days | Any CRITICAL finding; any incident reporting gap (Art. 23 cannot be remediated after an incident occurs); any active cybersecurity incident |
| **NEAR-TERM** | 30–90 days | NON-COMPLIANT findings; measures with no implementation; absent documentation for operable controls |
| **BACKGROUND** | 90–180 days | PARTIAL findings; enhancement actions; documentation improvements; optimization |

### Confidence Scoring

Apply to each finding before delivering output:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | NIS2 Directive text is explicit; requirement unambiguous; no national variation expected | State with confidence |
| **High** | 0.80–0.94 | ENISA guidelines provide clear guidance; minor interpretive uncertainty; most member states align | State with brief caveat |
| **Probable** | 0.60–0.79 | ENISA guidance exists but national implementations vary; reasonable interpretation; flag for legal review | State with reasoning and caveats |
| **Possible** | 0.40–0.59 | Genuine uncertainty on measure interpretation or national scope; supervisory interpretation may differ | Flag for regulator consultation; present both interpretations |
| **Unlikely** | 0.0–0.39 | Speculative interpretation; weak basis; do not assert | Do not state as requirement; flag as [UNCERTAIN] |

---

## Citation Quality Gates

Run these five gates silently before delivering any finding. If any gate fails, revise before delivery.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every regulatory claim cites specific NIS2 article, recital, ENISA guideline section, or national transposition provision | Add citation or mark [UNVERIFIED] |
| **Format** | All citations use consistent format: Art. 21(2)(a), Recital 74, Annex I, NIS2UmsuCG §X | Fix format |
| **Currency** | Every cited provision checked for amendments; national transposition acts marked [VERIFY] for evolving implementations | Flag [CHECK CURRENCY] |
| **Domain** | Analysis stays within NIS2 scope; any GDPR or DORA claims explicitly labeled [GDPR] or [DORA] | Remove or label jurisdictional bleed |
| **Confidence** | Any interpretive uncertainty explicitly stated with confidence level; pre-enforcement interpretations clearly flagged | Add confidence qualifier |

---

## Self-Interrogation

For all CRITICAL and NON-COMPLIANT findings, apply this three-pass review before finalizing:

**Pass 1 — Regulatory Necessity**: Does this deficiency actually violate NIS2 Article 21 (or other cited article)? Would the national competent authority cite it in a supervisory examination? Is the requirement explicitly in the Directive text, or is it ENISA guidance interpretation?

**Pass 2 — Completeness**: Have all relevant proportionality provisions been considered? Are there sector-specific carve-outs or ENISA safe harbor approaches? Has the compensating control question been asked (e.g., could an alternative control satisfy the same security objective)?

**Pass 3 — Challenge**: What is the strongest argument that this finding is actually PARTIAL rather than NON-COMPLIANT, or PARTIAL rather than CRITICAL? What evidence would upgrade the classification? Document this challenge in the finding.

---

## Anti-Patterns for NIS2 Compliance

What NOT to do when assessing or implementing NIS2 compliance:

**Entity Classification Errors:**

1. **Self-classifying as important when essential** — Claiming proportionality exemptions as a size-threshold shortcut without formal classification assessment. Essential entities face proactive supervision; misclassification creates enforcement risk.

2. **Ignoring the size-threshold exceptions** — Assuming size thresholds always apply. Qualified trust service providers, DNS service providers, and TLD registries are essential regardless of size. Similarly, national competent authorities may designate additional entities essential by law.

3. **Treating NIS2 and ISO 27001 as equivalent** — ISO 27001 certification does not automatically satisfy NIS2. NIS2 includes specific obligations (Art. 23 reporting timelines, Art. 20 board training, Art. 21 supply chain) that ISO 27001 does not fully address.

**Risk Management Measure Errors:**

4. **Conducting risk assessment once** — Risk assessment under Measure 1 must be updated at least annually and after significant changes. A 2023 risk assessment does not satisfy 2026 assessment obligations.

5. **Treating all ten measures with equal priority** — Incident handling (Measure 2) and incident reporting (Art. 23) are time-critical: gaps cannot be remediated after an incident occurs. Prioritize these before focusing on less time-sensitive measures.

6. **Delegating supply chain risk entirely to third parties** — Measure 4 does not permit third-party reliance. The assessed entity retains NIS2 responsibility even when using managed service providers. Third-party MSPs and MSSPs who are themselves NIS2 essential entities create circular dependency risk that must be assessed.

7. **Incident response plan as compliance checkbox** — An IRP not operationalized through exercise, tested reporting chains, and role-specific training fails NIS2. Evidence means demonstrably implemented, not merely documented.

8. **Access control without identity management baseline** — Measure 9 requires both access control policy (need-to-know) and identity management (IAM). Many organizations have access lists but no formal provisioning or deprovisioning controls. Offboarding is a common gap.

9. **Treating encryption policy as sufficient for Measure 8** — Cryptography measure requires key management (generation, rotation, revocation) not just a policy stating "we encrypt data at rest." Certificate expiry causing outages is a common enforcement signal.

10. **Separating MFA deployment from Measure 10** — MFA for remote access is well-understood, but Measure 10 also requires secure emergency communication systems. Most organizations have not addressed secure out-of-band communications for use during an active cybersecurity incident.

**Incident Reporting Errors:**

11. **Undefined significance thresholds** — If the organization has not pre-defined what constitutes a "significant incident," the 24-hour early warning clock expires while the incident response team debates whether to report. Decision criteria must be established before incidents occur.

12. **Treating early warning (24h) as the incident notification (72h)** — These are two distinct reports with different content requirements and different recipients in some member states. The 24h early warning is an alert; the 72h notification requires an initial assessment. Preparing only one template creates the risk of delivering the wrong content at the wrong time.

13. **Assuming GDPR breach notification satisfies NIS2** — GDPR Article 33 (72-hour breach notification to DPA) and NIS2 Article 23 are separate obligations to different authorities. GDPR applies to personal data breaches; NIS2 applies to significant incidents regardless of personal data involvement.

14. **Delaying 24-hour early warning pending investigation** — Art. 23(1) early warning must be submitted even without root cause analysis. "We are still investigating" is not a reason to delay the alert. Send the early warning; update the notification and report as investigation progresses.

**Board and Governance Errors:**

15. **Delegating NIS2 to the CISO without board engagement** — Article 20 creates direct management body accountability. NIS2 compliance is not a CISO responsibility that can be fully delegated. Board approval of risk management framework is mandatory.

16. **General security training as substitute for Art. 20(2) management training** — Article 20(2) requires management body members to be offered training in cybersecurity. General IT security awareness training does not satisfy this requirement. Board-level governance training is distinct.

17. **Board-level reporting as quarterly KPI dashboards** — Board oversight requires board members to understand and engage with cybersecurity risk, not just receive reports. Assessment should verify board members can articulate key risks, not just confirm report delivery.

**Cross-Directive and Jurisdictional Errors:**

18. **Assuming EU-wide consistency in NIS2** — ENISA guidelines are not legally binding; national supervisors may interpret Art. 21 measures differently. [JURISDICTION-SPECIFIC] guidance must be sought from each national competent authority.

19. **GDPR/NIS2 single program** — While GDPR Art. 32 and NIS2 Art. 21 overlap, they are not identical. NIS2 applies to network and information system security (broader than personal data). Running a single program may create gaps where NIS2 requires broader coverage than GDPR.

20. **Ignoring DORA for financial sector entities** — Financial sector entities subject to DORA must comply with both DORA and NIS2. Where requirements conflict, apply the stricter standard. DORA's incident reporting timelines (different thresholds and recipients than NIS2) require a dual-track reporting procedure.

---

## Writing Standards

1. **State requirements with confidence levels**: Never assert a Probable finding as Definite. Every finding identifies its regulatory basis (article, recital, ENISA guideline) and confidence score.

2. **Distinguish Directive text from ENISA guidance**: ENISA guidelines are best practice, not law. Mark ENISA-only requirements as [ENISA GUIDANCE — not legally binding unless adopted by national CA].

3. **Mark national transpositions as [VERIFY]**: As of March 2026, national transpositions are still evolving. Never state national implementation requirements as settled without [VERIFY] marker.

4. **Separate finding from recommendation**: Every finding statement describes what is absent or deficient; every recommendation prescribes the specific action, owner, and deadline.

5. **Avoid generic compliance language**: "Implement appropriate security measures" is not a finding. "Backup restoration testing records do not exist; most recent test was in 2022" is a finding.

6. **Proportionality claims require specificity**: If claiming proportionality for an important entity on a particular measure, cite the specific Art. 21(4) basis and ENISA guidance for the simplified measure. Generic proportionality claims are not sufficient.

7. **Pre-enforcement transparency**: NIS2 enforcement is early-stage as of March 2026. Where no enforcement precedent exists, state interpretations as "based on Directive text + ENISA guidelines; supervisory interpretation may evolve."

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:
- Search for current ENISA NIS2 implementation guidelines by sector
- Verify national transposition legislation status for each member state
- Search for competent authority guidance and supervisory expectations
- Verify incident reporting thresholds from implementing regulations (Commission Implementing Regulation for digital infrastructure providers)
- Mark all legalcode-mcp-verified citations as VERIFIED in Glass Box

**Without legalcode-mcp**:
- Proceed with Directive text and published ENISA guidelines from training knowledge
- Mark all national transposition references as [VERIFY]
- Mark ENISA guideline version references as [VERIFY — check current version at enisa.europa.eu]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Strongly recommend human legal review of all national implementation findings

---

## Output Format Template

```markdown
# NIS2 Compliance Assessment — [Organization Name]

**Assessment Date**: [YYYY-MM-DD]
**Assessor**: [Name/Role]
**Organization**: [Full legal name]
**Primary Sector**: [Annex I/II sector]
**Member State(s)**: [List]
**National Competent Authority**: [Authority name + contact] [VERIFY]
**Entity Classification**: [Essential / Important / Not in Scope]
**Assessment Mode**: [Readiness / Gap-analysis / Incident-prep / Supervisory exam prep]
**Existing Security Framework**: [ISO 27001 / NIST CSF / None / NIS1]
**NIS2 Enforcement Status (Member State)**: [National enforcement date] [VERIFY]

---

## Executive Summary

**Overall Compliance Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]
**Summary**: [2–3 sentences on overall posture, most material gaps, and key risks]

| Classification | Count | Priority |
|---------------|-------|----------|
| 🚨 CRITICAL | [N] | IMMEDIATE (0–30 days) |
| ❌ NON-COMPLIANT | [N] | NEAR-TERM (30–90 days) |
| ⚠️ PARTIAL | [N] | BACKGROUND (90–180 days) |
| ✅ COMPLIANT | [N] | Maintain and monitor |

### Top 3 Priority Actions
1. **[Measure/Article]**: [Specific required action] — Owner: [Role] — Deadline: [Date]
2. **[Measure/Article]**: [Specific required action] — Owner: [Role] — Deadline: [Date]
3. **[Measure/Article]**: [Specific required action] — Owner: [Role] — Deadline: [Date]

---

## Applicable Regulatory Framework

| Element | Applicable Standard |
|---------|-------------------|
| Primary legislation | NIS2 Directive (EU) 2022/2555 |
| National implementation | [Act name + citation] [VERIFY] |
| National competent authority | [Authority + enforcement model (proactive/reactive)] |
| Sector-specific overlay | [DORA / EECC / ACER / None] |
| GDPR interaction | GDPR Art. 32 (security measures overlap with NIS2 Art. 21) |

---

## Entity Classification Assessment

**Classification**: [Essential / Important / Out of Scope]
**Confidence**: [Definite / High / Probable / Possible]
**Regulatory basis**: [Article 3 + specific Annex I/II sector point]
**Supervisory model**: [Proactive (essential) / Reactive (important)]

| Classification Criterion | Status | Finding |
|--------------------------|--------|---------|
| Sector (Annex I or II) | [CONFIRMED / UNCLEAR / NOT APPLICABLE] | [Finding] |
| Size threshold (employees/turnover) | [CONFIRMED / UNCLEAR / EXEMPT] | [Finding] |
| Member state designation | [CONFIRMED / PENDING] [VERIFY] | [Finding] |

---

## Article 21 Risk Management Measures Assessment

### Measure 1: Risk Assessment and Risk Management
**Status**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]
**Confidence**: [Definite / High / Probable / Possible]
**Regulatory basis**: Art. 21(2)(a)

| Control Element | Status | Finding | Recommended Action | Owner | Deadline |
|----------------|--------|---------|-------------------|-------|----------|
| Risk assessment documented | [✅/⚠️/❌/🚨] | [Finding] | [Action] | [Role] | [Date] |
| Annual update | [✅/⚠️/❌/🚨] | [Finding] | [Action] | [Role] | [Date] |
| Management approval | [✅/⚠️/❌/🚨] | [Finding] | [Action] | [Role] | [Date] |
| Risk treatment plan | [✅/⚠️/❌/🚨] | [Finding] | [Action] | [Role] | [Date] |

[Repeat table format for Measures 2–10]

---

## Incident Reporting Assessment (Article 23)

### Timeline Capability

| Stage | Requirement | Current Capability | Status |
|-------|-------------|-------------------|--------|
| Early Warning | 24h to CSIRT/CA | [Assessment] | [✅/⚠️/❌/🚨] |
| Notification | 72h to CSIRT/CA | [Assessment] | [✅/⚠️/❌/🚨] |
| Final Report | 1 month from notification | [Assessment] | [✅/⚠️/❌/🚨] |

### Incident Significance Thresholds
**Defined thresholds**: [Yes / No / Partially]
**Financial threshold documented**: [€500K / 5% turnover criterion acknowledged: Yes / No]
**Decision-maker identified for significance classification**: [Yes / No / Partially]

### Competent Authority Contact
**CSIRT/CA name**: [Name] [VERIFY]
**Contact method**: [Email / Portal / Phone]
**Contact information current**: [Yes / No / Unknown]

---

## Board Accountability Assessment (Article 20 and 32)

**Status**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]

| Governance Element | Status | Finding |
|-------------------|--------|---------|
| Board approval of NIS2 risk management framework | [✅/⚠️/❌/🚨] | [Finding] |
| Art. 20(2) board-level cybersecurity training | [✅/⚠️/❌/🚨] | [Finding] |
| Named senior officer accountable for NIS2 | [✅/⚠️/❌/🚨] | [Finding] |
| Regular board cybersecurity reporting | [✅/⚠️/❌/🚨] | [Finding] |
| Board awareness of personal liability provisions | [✅/⚠️/❌/🚨] | [Finding] |

---

## Cross-Directive Compliance

### GDPR Article 32 Alignment
**Status**: [ALIGNED / PARTIAL OVERLAP / DIVERGENT]
[Brief analysis: where NIS2 Art. 21 satisfies GDPR Art. 32, and where NIS2 requires additional scope]

### DORA (Financial Sector Only)
**Status**: [NOT APPLICABLE / COMPLIANT / PARTIAL / NON-COMPLIANT]
[Brief analysis of DORA/NIS2 interaction; identify any reporting timeline conflicts]

### Sector-Specific Overlay
[Analysis of applicable sector regulation]

---

## Remediation Roadmap

### IMMEDIATE (0–30 days)
| Finding ID | Measure/Article | Finding | Required Action | Owner | Deadline |
|-----------|----------------|---------|----------------|-------|----------|
| [ID] | [Art. 21(X) / Art. 23] | [Finding] | [Action] | [Role] | [Date] |

### NEAR-TERM (30–90 days)
| Finding ID | Measure/Article | Finding | Required Action | Owner | Deadline |
|-----------|----------------|---------|----------------|-------|----------|
| [ID] | [Art. 21(X)] | [Finding] | [Action] | [Role] | [Date] |

### BACKGROUND (90–180 days)
| Finding ID | Measure/Article | Finding | Required Action | Owner | Deadline |
|-----------|----------------|---------|----------------|-------|----------|
| [ID] | [Art. 21(X)] | [Finding] | [Action] | [Role] | [Date] |

---

## Regulatory Readiness Checklist

**Pre-Examination Documentation:**
- [ ] Risk assessment (current, signed, dated within 12 months)
- [ ] Incident response plan (tested within 12 months)
- [ ] Business continuity plan (tested within 12 months)
- [ ] Supplier/vendor risk register (current)
- [ ] Cryptography policy (current)
- [ ] Access control policy (current)
- [ ] Personnel training records (all staff, within 12 months)
- [ ] Board training record (Art. 20(2) requirement)
- [ ] Incident reporting procedure (operationalized, contacts current)
- [ ] Asset inventory (current)
- [ ] Patch management records (last 12 months)
- [ ] Security effectiveness metrics (last review date)
- [ ] CSIRT/CA contact information (current) [VERIFY]
- [ ] Previous supervisory correspondence (if applicable)

---

## Quality Assurance

**Citation Quality Gates**: [X/5 passed — list any failures]
**Self-Interrogation Applied**: [List NON-COMPLIANT and CRITICAL findings reviewed]
**[VERIFY] Items**: [List all items requiring independent verification]
**[JURISDICTION-SPECIFIC] Items**: [List all items requiring national competent authority guidance]
**Confidence Assessment**: [Definite / High / Probable / Possible] — [Rationale]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-nis2-compliance-assessment"
  entity_type: "[essential / important / out-of-scope]"
  sector: "[telecom / finance / energy / healthcare / water / transport / digital-infra / other]"
  member_states:
    - "[Member State 1]"
  assessment_mode: "[readiness / gap-analysis / incident-prep / supervisory-exam-prep]"
  existing_framework: "[ISO 27001 / NIST CSF / NIS1 / none]"
  assessment_date: "[YYYY-MM-DD]"
  nis2_enforcement_status: "[member state enforcement date — VERIFY]"
  legalcode_mcp: "[Connected / Not connected]"
  critical_findings: [N]
  non_compliant_findings: [N]
  partial_findings: [N]
  compliant_measures: [N]
  citations_verified: "[N VERIFIED / N marked [VERIFY]]"
  jurisdiction_specific_items: [N]
  confidence_overall: "[Definite / High / Probable / Possible] — [Rationale]"
  limitations:
    - "Assessment based on information provided by organization; completeness depends on accuracy of inputs"
    - "National transpositions evolving as of March 2026; [VERIFY] markers applied to all national implementation references"
    - "NIS2 enforcement is early-stage; supervisory interpretation of Art. 21 measures may evolve"
    - "No enforcement precedent (no published enforcement decisions as of assessment date)"
    - "ENISA guidelines are not legally binding unless adopted by national CA; [VERIFY] guidance status"
  reviewer: "AI-assisted — requires review by qualified information security legal professional and senior security officer"
```

---

## Localization Notes

This skill produces a jurisdiction-agnostic assessment based on NIS2 Directive text and
ENISA guidelines. For production assessments, adapt each [JURISDICTION-SPECIFIC] marker
using national authority guidance:

**Germany (DE)** [JURISDICTION-SPECIFIC]:
- NIS2UmsuCG (in force December 6, 2025) amends the BSI Act (BSIG)
- BSI is competent authority; registration deadline April 2026 via BSI portal
- KRITIS framework retained for critical facilities; KRITIS operators designated essential by law
- Board personal liability: NIS2UmsuCG creates direct management responsibility for NIS2 compliance
- Registration: two-step process (Mein Unternehmenskonto → BSI portal from January 6, 2026)

**France (FR)** [JURISDICTION-SPECIFIC]:
- ANSSI (Agence nationale de la sécurité des systèmes d'information) is lead authority
- [VERIFY: current status of NIS2 transposition legislation and specific French national requirements]

**Netherlands (NL)** [JURISDICTION-SPECIFIC]:
- [VERIFY: Cybersecuritywet or equivalent NIS2 transposition act; NCSC/RDI authority scope]

**Poland (PL)** [JURISDICTION-SPECIFIC]:
- [VERIFY: amendment to the Act on the National Cybersecurity System; CSIRT Poland + CERT.PL authorities]

**Ireland (IE)** [JURISDICTION-SPECIFIC]:
- [VERIFY: NIS2 Regulations SI (Statutory Instrument) status; National Cyber Security Centre (NCSC) authority]

**Sweden (SE)** [JURISDICTION-SPECIFIC]:
- [VERIFY: NIS2 transposition legislation; NCSC-SE authority scope]

**For all member states**: Consult ENISA's NIS2 transposition tracker (enisa.europa.eu)
for current status of each member state's implementation.

---

## Glossary

**Essential entity**: An entity in an Annex I sector that is large (250+ employees / €50M+ turnover),
or designated essential by a national authority, or exempt from size thresholds.

**Important entity**: An entity in Annex I (that is medium-sized) or Annex II (medium or large),
subject to reactive (not proactive) supervision.

**Significant incident**: An incident causing or capable of causing severe service disruption,
financial loss exceeding €500K or 5% of annual turnover, reputational damage, data exfiltration
of trade secrets, or physical harm. Triggers Art. 23 reporting.

**CSIRT**: Computer Security Incident Response Team — national authority receiving NIS2 incident
notifications.

**RTO**: Recovery Time Objective — maximum time to restore a system after disruption.

**RPO**: Recovery Point Objective — maximum acceptable data loss window (measured in time).

**SIEM**: Security Information and Event Management — centralized log collection and alerting system.

**SOC**: Security Operations Centre — team responsible for monitoring and responding to security events.

**PAM**: Privileged Access Management — controls governing high-privilege accounts and administrator access.

**IAM**: Identity and Access Management — systems and processes for user authentication, authorization,
and lifecycle management.

**ENISA**: European Union Agency for Cybersecurity — provides guidelines and guidance on NIS2
implementation (not legally binding unless adopted by national CA).

**KRITIS**: German framework for identifying critical infrastructure; retained under NIS2UmsuCG.

**DORA**: Digital Operational Resilience Act (Regulation 2022/2554) — applies to EU financial
sector entities; overlaps with NIS2 for financial sector essential entities.

**EECC**: European Electronic Communications Code (Directive 2018/1972) — applies to telecom
sector; predates NIS2; some security measures overlap.

---

## Provenance

Created: 2026-03-02. Legalcode original synthesis.

Primary sources:
- EU Directive 2022/2555 (NIS2) — full Directive text and Annexes I and II
- ENISA NIS2 Technical Implementation Guidance (Version 1.0, 2025)
- European Commission Implementing Regulations on NIS2 significant incident thresholds
  (€500,000 / 5% turnover criterion from 2024 implementing regulation) [VERIFY currency]
- Germany NIS2UmsuCG (enacted December 5, 2025; in force December 6, 2025)
- Article 21(2)(a)–(j) ten minimum measures — interpreted per ENISA implementation guidance
- Article 23 significant incident definition and three-stage timeline — per Directive text
- Article 20 / Article 32 board accountability — per Directive text and emerging member state implementations

Research methodology: 2-agent research pipeline (Agent 1: structural analysis of legalcode-eu-ai-act-high-risk-compliance and legalcode-aml-kyc-compliance reference skills; Agent 2: NIS2 legal research via WebSearch across 10+ targeted queries covering entity classification, Art. 21 measures, Art. 23 incident reporting, member state transpositions, GDPR/DORA interaction, and enforcement framework). Web research supplemented with Directive text analysis.

All national transposition references marked [VERIFY] — as of March 2026, national implementations are evolving. Verify against current national authority guidance.

Legal review required: This skill requires review by a qualified information security legal professional in the relevant member state before use in production compliance assessments.
```
