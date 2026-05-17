---
name: legalcode-vendor-privacy-assessment
description: >
  Conduct comprehensive privacy risk assessments of third-party vendors and service
  providers. Use when onboarding new vendors, renewing vendor contracts, responding
  to procurement due diligence requests, conducting periodic vendor audits, evaluating
  vendors following a breach incident, reviewing sub-processor chains, assessing
  vendor acquisitions, or responding to regulatory inquiries about supplier oversight.
  Covers security controls evaluation (encryption, access controls, vulnerability
  management, penetration testing), sub-processor identification and oversight
  mechanisms, data breach detection and notification capabilities (GDPR 72-hour rule,
  HIPAA 60-day, all-US-state breach notification), cross-border transfer mechanisms
  and adequacy (EU SCCs 2021 Modules 1-4, UK IDTA, BCRs, EU-US DPF), data retention
  and deletion verification practices, employee privacy training and background screening,
  business continuity and disaster recovery, regulatory compliance certifications
  (SOC 2 Type II, ISO 27001:2022, ISO 27701:2019, PCI DSS, FedRAMP), contractual
  safeguards adequacy (GDPR Art. 28 DPA, SCCs, CCPA/CPRA service provider agreements,
  HIPAA BAAs), data subject rights fulfillment capability, and ongoing monitoring and
  reassessment trigger management. Produces vendor risk tier rating (Tier 1-4),
  GREEN/YELLOW/RED/CRITICAL classification across 11 assessment domains, conditional
  approval recommendations with remediation timelines, and a Glass Box audit trail.
  Supports integration with VRM platforms (OneTrust, Prevalent, Venminder, ProcessUnity)
  and standard questionnaire frameworks (SIG Core/Lite, CAIQ, HECVAT, VSA).
  Jurisdiction-agnostic baseline with [JURISDICTION-SPECIFIC] markers covering GDPR,
  UK GDPR, CCPA/CPRA, HIPAA, LGPD, PIPEDA, APPI, PDPA, and NIS2 supply chain
  security obligations.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Vendor Privacy Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted vendor privacy risk
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional — preferably a privacy attorney or certified privacy
> professional (CIPP/E, CIPP/US, CIPM) — licensed in the relevant jurisdiction before
> use. Privacy regulations change rapidly; verify current applicability before relying
> on any requirement described here. Statutory references cited from training data carry
> hallucination risk — verify against authoritative primary sources before relying on
> them. Vendor risk ratings produced by this skill are AI-assisted assessments, not
> professional audits; high-stakes decisions require independent qualified review.

---

## Purpose and Scope

This skill conducts structured privacy risk assessments of third-party vendors and service
providers across the full vendor lifecycle: initial onboarding, periodic review, renewal,
post-incident reassessment, and offboarding verification.

**Covers:**
- Vendor risk tiering based on data sensitivity, access level, business criticality, and
  geographic risk (four-factor scoring model)
- Security controls evaluation across 8 technical control domains
- Sub-processor chain identification, mapping, and oversight adequacy
- Breach detection, investigation, and notification capability assessment
- Cross-border transfer mechanism review (SCCs, IDTA, BCRs, DPF, adequacy)
- Data retention schedules and verified deletion / return capability
- Employee controls (background screening, training, privileged access)
- Business continuity and disaster recovery (BCP/DR) adequacy
- Regulatory certification review (SOC 2 Type II, ISO 27001, ISO 27701, PCI DSS)
- Contractual safeguards adequacy (DPA, SCCs, HIPAA BAA, CPRA service provider terms)
- Data subject rights fulfillment — response SLAs, technical capability, escalation paths
- Ongoing monitoring framework and event-driven reassessment trigger management

**Does not:**
- Draft vendor contracts or DPAs (see `legalcode-dpa-review-and-negotiation`)
- Conduct cross-border transfer impact assessments (see `legalcode-cross-border-transfer-assessment`)
- Generate breach notification drafts (see `legalcode-breach-regulatory-notification-drafter`)
- Constitute a formal third-party audit or replace penetration-testing professional services
- Provide legal advice or substitute for qualified privacy counsel

**Related skills:**
- `legalcode-dpa-review-and-negotiation` — Review and negotiate the DPA with the vendor
- `legalcode-cross-border-transfer-assessment` — Deep TIA / LIA for specific transfer routes
- `legalcode-breach-severity-assessment` — Assess a specific incident involving a vendor
- `legalcode-dpia-generator` — DPIA for high-risk vendor processing relationships
- `legalcode-data-mapping-workflow` — Map vendor data flows into the RoPA

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at its core. The assessment framework applies across
all major data protection regimes. Where a specific regime imposes materially different
or additional requirements, the content is flagged:

```
[JURISDICTION-SPECIFIC: GDPR] — EU and EEA controller/processor relationships
[JURISDICTION-SPECIFIC: UK GDPR] — Post-Brexit UK controller/processor obligations
[JURISDICTION-SPECIFIC: CCPA/CPRA] — California service provider and contractor categories
[JURISDICTION-SPECIFIC: HIPAA] — US healthcare sector Business Associate obligations
[JURISDICTION-SPECIFIC: LGPD] — Brazil operator obligations
[JURISDICTION-SPECIFIC: PIPEDA/Law 25] — Canada/Quebec third-party accountability
[JURISDICTION-SPECIFIC: APPI] — Japan third-party provision rules
[JURISDICTION-SPECIFIC: PDPA] — Singapore transfer limitation obligations
[JURISDICTION-SPECIFIC: NIS2] — EU critical infrastructure supply chain security
```

When multiple regimes apply simultaneously (e.g., a US-based SaaS vendor processing
EU personal data of Canadian employees for a UK-headquartered controller), assess each
regime's requirements in parallel and flag where they diverge.

[JURISDICTION-SPECIFIC: GDPR] Under GDPR Article 28, controllers must select only
processors providing "sufficient guarantees" to implement appropriate technical and
organisational measures. This is a pre-contract obligation — due diligence must be
completed before signing, not after.

[JURISDICTION-SPECIFIC: NIS2] NIS2 Directive (Directive EU 2022/2555), transposed into
EU member state law by October 18, 2024, imposes mandatory supply chain risk management
for organisations in critical and important sectors. Assess direct suppliers and, where
material, their sub-suppliers.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the direction, scope, or depth of the assessment
- Multiple valid risk-tiering approaches exist (e.g., ambiguous data sensitivity level)
- The applicable regulatory regime is unclear from the vendor information provided
- A finding's severity depends on organizational risk tolerance

Use the **⟁ CLARIFY** pattern (structured options with "Why this matters" blurb) wherever
marked below. If the user has already provided the information (e.g., in the initial
prompt or from a prior conversation turn), skip the question and proceed.

---

## Workflow

### Step 1: Accept Vendor Information

Accept vendor information in any of these formats:
- **Completed questionnaire**: SIG Core, SIG Lite, CAIQ, HECVAT, or similar structured
  questionnaire responses
- **Vendor-provided documentation**: Privacy policy, DPA, security certifications, SOC 2
  report, ISO 27001 certificate, penetration testing summary, BCP documentation
- **Freeform description**: User description of the vendor, services, and data processed
- **Vendor profile export**: JSON or CSV from a VRM platform (OneTrust, Prevalent, etc.)

If no information is provided beyond the vendor name, prompt the user to supply at least:
the type of services provided, the categories of personal data the vendor will process,
and the data subjects involved.

### Step 2: Gather Assessment Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Skip any question already
answered by the information provided:

1. **Assessment trigger**: Why is this assessment being conducted?
   - Options: New vendor onboarding, Annual/periodic review, Contract renewal,
     Post-incident reassessment, Regulatory audit response, Acquisition due diligence,
     Sub-processor chain review
   - *Why this matters*: The trigger determines assessment depth — post-incident
     assessments require deeper scrutiny than routine renewals. Acquisition due diligence
     requires full historical record review.

2. **Data categories processed**: What types of personal data will this vendor process?
   - Options: Ordinary PII (names, contact details), Financial data (payment cards, bank
     accounts), Health/medical data (PHI), Biometric or genetic data, Children's data
     (under 16 or COPPA under 13), Employee/HR data, Criminal conviction data,
     Political/religious/sensitive special-category data, Behaviorally inferred data
   - *Why this matters*: Special category data (GDPR Art. 9) and children's data trigger
     heightened assessment requirements, stricter contractual terms, and may require a DPIA.

3. **Applicable regulatory regimes**: Which data protection laws govern this relationship?
   - Options: EU GDPR, UK GDPR, CCPA/CPRA, HIPAA/HITECH, LGPD, PIPEDA/Law 25,
     APPI, PDPA (Singapore), Other / I'm not sure
   - *Why this matters*: Different regimes impose materially different contractual,
     technical, and organizational requirements on vendors.

4. **Assessment depth**: What level of assessment is needed?
   - Options: Full assessment (SIG Core equivalent — all 11 domains), Standard assessment
     (10 key domains, skipping low-risk domains), Expedited assessment (priority domains
     only, 48-hour turnaround), Focused assessment (specific concern area only)
   - *Why this matters*: Full assessments are appropriate for Tier 1/2 vendors;
     expedited assessments may be appropriate for urgent procurement decisions with a
     commitment to full assessment before go-live.

5. **Organizational playbook**: Does your organization have a vendor privacy assessment
   playbook, baseline standards, or minimum security requirements?
   - Options: Yes, I'll provide it, Yes, load from context, No — use regulatory baselines
     and industry standards, I'll provide specific requirements as we go
   - *Why this matters*: Playbook-based assessments measure the vendor against your
     organization's specific requirements; baseline assessments measure against regulatory
     minimums. Both are valid; the resulting output differs.

### Step 3: Establish Regulatory Regime Map

Based on the context gathered in Step 2, build a **Regulatory Regime Map** for this
vendor relationship:

| Regime | Applies? | Basis | Key Obligations |
|--------|----------|-------|-----------------|
| EU GDPR | Yes / No | [data subjects in EEA / establishment] | Art. 28 DPA, Art. 32 security, Art. 44-49 transfers |
| UK GDPR | Yes / No | [UK data subjects / UK establishment] | UK Art. 28, IDTA for transfers |
| CCPA/CPRA | Yes / No | [California consumers / revenue thresholds] | Service provider/contractor agreement, audit rights |
| HIPAA | Yes / No | [US healthcare data, covered entity relationship] | BAA required, Security Rule compliance |
| LGPD | Yes / No | [Brazilian data subjects] | Operator DPA, transfer mechanism |
| PIPEDA/Law 25 | Yes / No | [Canadian/Quebec data subjects] | Accountability, contractual protection |
| NIS2 | Yes / No | [Critical/important sector entity in EU] | Supply chain risk assessment |
| Other | Yes / No | [Specify] | [Specify] |

If multiple regimes apply, assess the vendor against all applicable regimes. Where regimes
impose conflicting requirements, flag the conflict explicitly and recommend the most
protective approach (often GDPR if EU data subjects are involved).

### Step 4: Load Assessment Playbook or Baseline Standards

**⟁ CLARIFY** — If no organizational playbook was provided:

- **Option A — Use industry baseline standards**: Proceed with GDPR Article 28 mandatory
  elements, ISO 27001:2022 Annex A.5.19-5.23 supplier controls, and NIST SP 800-53
  security baselines as the assessment standard.
- **Option B — Use questionnaire framework**: Map the assessment against a specific
  questionnaire format (SIG Core, SIG Lite, CAIQ, HECVAT). Specify which framework.
- **Option C — Provide specific requirements now**: User supplies their organization's
  minimum vendor privacy requirements for the relevant data tier.

If an organizational playbook is provided, load it as the primary assessment baseline.
Where the playbook is silent, fall back to regulatory baselines and industry standards.

### Step 5: Vendor Risk Tiering

Before conducting the full assessment, assign the vendor to a risk tier using the
**Four-Factor Scoring Model**. This determines assessment depth and ongoing monitoring
frequency.

#### Factor 1: Data Sensitivity Score (0–40 points)

| Data Category | Points |
|---------------|--------|
| PHI / health / genetic / biometric data | 35–40 |
| Financial / payment card / bank account data | 30–35 |
| Government ID / criminal conviction / sensitive special-category data | 30–35 |
| Children's data (under 16 GDPR / under 13 COPPA) | 28–35 |
| Employee / HR data | 22–28 |
| Standard PII (names, contact details, behavioral data) | 12–22 |
| Pseudonymised or encrypted data (keys not held by vendor) | 5–12 |
| Aggregate / anonymised data (no re-identification risk) | 0–5 |

#### Factor 2: Access Level Score (0–30 points)

| Access Type | Points |
|-------------|--------|
| Network / system access + administrative credentials | 25–30 |
| Data hosting / storage (vendor holds data at rest) | 20–25 |
| Data processing (vendor processes in-memory, no persistent storage) | 12–18 |
| Viewing access only (read-only, no download rights) | 8–12 |
| Incidental / background access (support access, logs) | 3–8 |
| No direct access to personal data | 0–3 |

#### Factor 3: Business Criticality Score (0–20 points)

| Criticality Level | Points |
|-------------------|--------|
| Mission-critical / single-source dependency | 16–20 |
| Important but replaceable within 90 days | 10–15 |
| Significant operational dependency | 6–10 |
| Convenience / non-essential service | 0–5 |

#### Factor 4: Geographic Risk Score (0–10 points)

| Transfer Destination | Points |
|----------------------|--------|
| No cross-border transfer (data stays in originating jurisdiction) | 0 |
| Transfer to jurisdiction with adequacy decision (EEA ↔ adequate country) | 1–3 |
| Transfer to jurisdiction covered by EU-US DPF (certified US entity) | 2–4 |
| Transfer via SCCs / IDTA to non-adequate jurisdiction | 5–7 |
| Transfer to jurisdiction with known surveillance concerns (requiring TIA) | 8–10 |

**Risk Tier Assignment:**

| Total Score | Risk Tier | Label | Assessment Protocol | Reassessment Frequency |
|-------------|-----------|-------|--------------------|-----------------------|
| 70–100 | Tier 1 | Critical | Full SIG Core + SOC 2 Type II review + virtual/on-site audit | Annual |
| 45–69 | Tier 2 | High | SIG Core or tailored assessment + SOC 2 Type II or ISO 27001 cert | 18 months |
| 20–44 | Tier 3 | Moderate | SIG Lite + certification attestation | 24 months |
| 0–19 | Tier 4 | Low | Lightweight self-attestation + privacy policy review | 36 months or event-triggered |

**⟁ CLARIFY** — If the tier assignment is borderline (within 5 points of a tier boundary),
ask the user: "This vendor scores at the boundary between Tier [X] and Tier [X+1]. Given
[specific ambiguous factor], which tier should apply? Tier [X] requires [deeper assessment];
Tier [X+1] allows [lighter assessment]."

### Step 6: Security Controls Evaluation

Evaluate the vendor's security controls across 8 technical domains. For each domain,
classify as GREEN / YELLOW / RED based on whether the vendor meets the assessment baseline.

#### Domain 1: Encryption

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| Data at rest | AES-256 or equivalent | [Vendor response] | G / Y / R |
| Data in transit | TLS 1.3 (TLS 1.2 minimum) | [Vendor response] | G / Y / R |
| Key management | HSM or equivalent; keys not co-located with encrypted data | [Vendor response] | G / Y / R |
| Database encryption | Transparent data encryption (TDE) for databases storing PII | [Vendor response] | G / Y / R |
| Backup encryption | Encrypted backups with separate key management | [Vendor response] | G / Y / R |
| End-to-end encryption | Required if data is highly sensitive (PHI/special category) | [Vendor response] | G / Y / R |

**RED triggers**: Absence of encryption at rest for sensitive data; TLS below 1.2; keys
co-located with encrypted data; unencrypted backups containing personal data.

#### Domain 2: Access Controls

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| MFA | MFA enforced for all administrative and privileged access | [Vendor response] | G / Y / R |
| RBAC | Role-based access with least-privilege principle documented | [Vendor response] | G / Y / R |
| PAM | Privileged access management with session recording for admin access | [Vendor response] | G / Y / R |
| Access reviews | Quarterly access reviews with automated de-provisioning | [Vendor response] | G / Y / R |
| Contractor access | Time-limited, role-specific credentials; no shared accounts | [Vendor response] | G / Y / R |
| Separation of duties | Development/production environment isolation | [Vendor response] | G / Y / R |

**RED triggers**: No MFA on administrative accounts; shared credentials; no documented
access review process; no de-provisioning workflow.

#### Domain 3: Vulnerability Management

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| Patch management | Critical patches within 48 hours; high within 14 days; medium within 30 days | [Vendor response] | G / Y / R |
| Vulnerability scanning | Automated scanning at least weekly; authenticated scans for internal systems | [Vendor response] | G / Y / R |
| Penetration testing | Annual minimum for Tier 1; results shared with customers on request (executive summary) | [Vendor response] | G / Y / R |
| SAST/DAST | Application security testing integrated into SDLC | [Vendor response] | G / Y / R |
| Dependency scanning | SCA (software composition analysis) for open-source components | [Vendor response] | G / Y / R |
| Bug bounty or CVD | Coordinated vulnerability disclosure program | [Vendor response] | G / Y / R |

**RED triggers**: No documented patch management SLAs; no penetration testing in past 18
months; no vulnerability scanning program; critical vulnerabilities unpatched beyond SLA.

#### Domain 4: Network Security

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| Network segmentation | Production personal data environment isolated from development and corporate networks | [Vendor response] | G / Y / R |
| Firewall / WAF | Web application firewall protecting customer-facing services | [Vendor response] | G / Y / R |
| DDoS protection | DDoS mitigation service active on production endpoints | [Vendor response] | G / Y / R |
| Zero-trust | Network access based on verified identity, not network location | [Vendor response] | G / Y / R |
| VPN / secure remote access | Encrypted remote access with MFA for staff accessing personal data | [Vendor response] | G / Y / R |

#### Domain 5: Audit Logging and Monitoring

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| Comprehensive logging | All access to personal data logged with user, timestamp, action | [Vendor response] | G / Y / R |
| Log retention | Security logs retained for minimum 12 months; 6 months immediately available | [Vendor response] | G / Y / R |
| Tamper resistance | Logs stored in append-only, tamper-evident system | [Vendor response] | G / Y / R |
| SIEM / alerting | Security information and event management with real-time alerting | [Vendor response] | G / Y / R |
| Anomaly detection | Behavioral analytics or UBA for detecting unusual access patterns | [Vendor response] | G / Y / R |

**RED triggers**: No logging of access to personal data; logs deletable by ordinary
administrative users; log retention below 3 months.

#### Domain 6: Incident Detection and Response

Evaluated in detail in Step 8 (Breach Detection and Notification).

#### Domain 7: Physical Security

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| Data center security | ISO 27001 or SOC 2-certified data center (or equivalent third-party facility) | [Vendor response] | G / Y / R |
| Access control | Biometric or card-based access; visitor logs maintained | [Vendor response] | G / Y / R |
| Media handling | Encrypted and certified destruction of decommissioned media | [Vendor response] | G / Y / R |
| Clean desk / screen lock | Policy and enforcement for offices handling personal data | [Vendor response] | G / Y / R |

#### Domain 8: Secure Development Lifecycle

| Control | Baseline Requirement | Vendor Status | Classification |
|---------|---------------------|---------------|----------------|
| Security training | Developer secure coding training annual minimum | [Vendor response] | G / Y / R |
| Code review | Security-focused code review for features handling personal data | [Vendor response] | G / Y / R |
| Privacy by design | Privacy impact review integrated into feature specification | [Vendor response] | G / Y / R |
| Third-party components | SBOM (Software Bill of Materials) available; open-source dependencies tracked | [Vendor response] | G / Y / R |

[JURISDICTION-SPECIFIC: EU CRA] The EU Cyber Resilience Act (Regulation 2024/2847), entered
into force December 2024 with phased obligations starting December 2027, imposes security
requirements on manufacturers of products with digital elements. Verify whether the vendor's
software products fall within CRA scope, and if so, confirm conformity declaration timeline.

### Step 7: Sub-Processor Identification and Oversight

**⟁ CLARIFY** — Has the vendor provided a sub-processor list? If not, request one before
proceeding with this step.

#### 7a. Sub-Processor Registry Review

Obtain and review the vendor's sub-processor list. For each sub-processor, document:

| Sub-Processor | Registered Name | Location | Service Provided | Data Categories | Transfer Mechanism | Last Review |
|---------------|-----------------|----------|-----------------|-----------------|---------------------|-------------|
| [Name] | [Legal entity] | [Country] | [Function] | [PII types] | [SCC / adequacy / DPF] | [Date] |

**Completeness checks:**
- [ ] Sub-processor list identifies legal entity name (not just trade name)
- [ ] Location / data processing jurisdiction for each sub-processor
- [ ] Specific function / service each sub-processor performs
- [ ] Data categories each sub-processor receives
- [ ] Transfer mechanism for cross-border sub-processors
- [ ] Date of last sub-processor review or list update

#### 7b. Sub-Processor Contractual Flow-Down

Verify that the vendor's contracts with sub-processors flow down all controller-mandated
obligations:

[JURISDICTION-SPECIFIC: GDPR] Under GDPR Article 28(4), a processor shall not engage a
sub-processor without the controller's prior specific or general written authorization. Where
general authorization is given, the processor must inform the controller of any intended
changes (additions or substitutions) in advance, giving the controller the opportunity to
object. The sub-processor contract must impose the same data protection obligations as the
main DPA. The initial processor remains fully liable for the sub-processor's performance.

| Requirement | Standard | Present in Sub-Processor DPA? | Classification |
|-------------|----------|-------------------------------|----------------|
| Data protection obligations identical to main DPA | GDPR Art. 28(4) | Yes / No | G / R |
| Advance notification of sub-processor changes (30-day minimum recommended) | GDPR Art. 28(2) | Yes / No | G / Y / R |
| Customer's right to object to new sub-processors | GDPR Art. 28(2) | Yes / No | G / Y / R |
| Audit rights flowing to sub-processors | GDPR Art. 28(3)(h) | Yes / No | G / R |
| Deletion or return of data upon termination | GDPR Art. 28(3)(g) | Yes / No | G / R |
| Breach notification obligation from sub-processor to primary processor | GDPR Art. 33 | Yes / No | G / R |

#### 7c. Sub-Processor Retention Chain Analysis

Map the longest data retention timeline in the sub-processor chain:
- Primary vendor retention period: [X days/months]
- Sub-processor with longest retention: [Name] — [X days/months] for [purpose]
- Effective retention timeline applicable to the organization: [maximum of chain]

**RED trigger**: Sub-processor retention exceeds what was disclosed to data subjects or
what is permitted under the controller's retention schedule — effective retention is
governed by the longest link in the chain.

### Step 8: Breach Detection and Notification Capabilities

Assess the vendor's ability to detect, investigate, and notify data breaches in compliance
with applicable regulatory timelines.

#### 8a. Detection Capability

| Capability | Baseline | Vendor Status | Classification |
|------------|----------|---------------|----------------|
| SIEM / log correlation | Real-time alerting on anomalous access or exfiltration indicators | [Vendor response] | G / Y / R |
| DLP (Data Loss Prevention) | DLP tools monitoring egress of personal data | [Vendor response] | G / Y / R |
| EDR / threat detection | Endpoint detection and response on systems processing personal data | [Vendor response] | G / Y / R |
| Incident playbook | Documented breach detection and response procedures | [Vendor response] | G / Y / R |
| 24/7 monitoring | SOC (Security Operations Center) coverage, internal or managed | [Vendor response] | G / Y / R |

#### 8b. Investigation and Notification SLAs

Regulatory notification obligations require the vendor to notify the controller within
sufficient time to meet the controller's own statutory deadlines:

| Regulatory Obligation | Controller's Deadline | Required Vendor Notification Window |
|-----------------------|----------------------|--------------------------------------|
| GDPR Art. 33 (supervisory authority) | 72 hours of awareness | Vendor must notify controller within 24–36 hours |
| GDPR Art. 34 (data subjects — high risk) | Without undue delay | Vendor must enable classification within 24 hours |
| HIPAA § 164.410 (covered entity notification) | 60 days of discovery | Vendor (BA) must notify CE: 30 days (contractual best practice) |
| CCPA breach notification | Without unreasonable delay; CA AG 15 days for 500+ | Vendor must notify controller within 48 hours |
| US state breach laws (all 50 states + DC) | 30–90 days depending on state | Vendor must notify controller within 24–72 hours |

**⟁ CLARIFY** — Review the vendor's DPA for the contractual breach notification period:
- Is the breach notification SLA specified in the contract?
- Does it allow the controller sufficient time to meet its own obligations?

| Contractual Requirement | Present? | SLA Stated | Classification |
|------------------------|----------|------------|----------------|
| Breach notification obligation | Yes / No | [Hours] from discovery | G / Y / R |
| Initial notification window (24–48 hours) | Yes / No | [Hours] | G / Y / R |
| Detailed follow-up report (5–10 business days) | Yes / No | [Days] | G / Y / R |
| Forensic assistance / cooperation obligation | Yes / No | [Description] | G / Y / R |
| Root cause analysis provided | Yes / No | [Timeline] | G / Y / R |
| Notification covers sub-processor incidents | Yes / No | N/A / [Hours] | G / Y / R |

**RED triggers**: No breach notification obligation in contract; vendor notification window
exceeds 48 hours (leaving controller insufficient time for GDPR 72-hour compliance); breach
notification obligation excludes sub-processor incidents.

### Step 9: Cross-Border Transfer Mechanisms

For any personal data transfer to a vendor processing in a non-adequate jurisdiction, verify
that an appropriate transfer mechanism is in place. For a full Transfer Impact Assessment,
use `legalcode-cross-border-transfer-assessment`.

#### 9a. Transfer Mechanism Classification

| Transfer Route | Primary Mechanism | Status | Classification |
|----------------|------------------|--------|----------------|
| EEA → adequate country (UK, Japan, Canada, Israel, etc.) | Adequacy decision | Valid / Expired / N/A | G / Y / R |
| EEA → US (DPF-certified entity) | EU-US DPF adequacy decision (July 2023) | DPF certified / Not certified / N/A | G / Y / R |
| EEA → US (non-DPF) | EU SCCs 2021 Module 2 (controller-to-processor) | In place / Missing / N/A | G / Y / R |
| UK → non-adequate | UK IDTA (effective March 2022) or EU SCC + UK Addendum | In place / Missing / N/A | G / Y / R |
| EEA → intra-group transfer (multinational) | BCRs (controller or processor) | Approved / Pending / N/A | G / Y / R |
| Other route | [Mechanism] | [Status] | G / Y / R |

[JURISDICTION-SPECIFIC: UK GDPR] The International Data Transfer Agreement (IDTA) is the
UK's mechanism replacing EU SCCs for new transfer arrangements since March 21, 2022. Confirm
that any UK-governed transfer arrangement uses the IDTA (or EU SCCs + ICO UK Addendum).

[JURISDICTION-SPECIFIC: GDPR] EU SCCs 2021 Modules 1–4 selection:
- Module 1: Controller-to-Controller (use when vendor is a controller in its own right)
- Module 2: Controller-to-Processor (most vendor relationships; also functions as Art. 28 DPA)
- Module 3: Processor-to-Processor (EEA processor engaging a non-EEA sub-processor)
- Module 4: Processor-to-Controller (vendor returning processed data to EEA controller)

#### 9b. Transfer Risk Assessment Status

For transfers to jurisdictions with surveillance law concerns (US pre-DPF, China, Russia,
India, etc.), verify whether a Transfer Impact Assessment (TIA) has been completed:

| Transfer Destination | TIA Required? | TIA Completed? | TIA Currency | Classification |
|----------------------|--------------|----------------|--------------|----------------|
| [Jurisdiction] | Yes / No | Yes / No | [Date] | G / Y / R |

**RED triggers**: Transfer to non-adequate jurisdiction without SCCs, IDTA, or BCRs in
place; SCCs using the 2010 EU model clauses (invalid since December 27, 2022); IDTA not
in place for UK-governed transfers entered into after March 21, 2022.

### Step 10: Data Retention and Deletion

#### 10a. Retention Schedule Review

| Data Category | Vendor Stated Retention | Business Purpose | Proportionality | Classification |
|---------------|------------------------|-----------------|-----------------|----------------|
| [Category] | [Period] | [Purpose] | Proportionate / Excessive | G / Y / R |

Verify:
- [ ] Retention periods stated specifically (not "as required by law" without specification)
- [ ] Retention is tied to a documented legal basis and business purpose
- [ ] Backup data subject to same retention limits (not indefinitely retained in cold storage)
- [ ] Sub-processor retention chain does not exceed disclosed periods (cross-reference Step 7c)
- [ ] Logs and audit trails retention separate from personal data retention

#### 10b. Deletion Verification Capability

| Deletion Requirement | Vendor Capability | Evidence Available | Classification |
|----------------------|-------------------|-------------------|----------------|
| Deletion within [X] days of contract termination | [Capability description] | Certificate / Statement / None | G / Y / R |
| Deletion on individual data subject erasure request | [SLA stated] | Demonstrated / Stated only | G / Y / R |
| Deletion confirmation / certificate provided | Yes / No | [Format] | G / Y / R |
| Secure media disposal (NIST 800-88 or equivalent) | [Standard cited] | Certificate / Statement / None | G / Y / R |
| Backup purge included in deletion process | Yes / No | [Confirmation] | G / Y / R |
| Sub-processor deletion verified | Yes / No | [How verified] | G / Y / R |

**RED triggers**: No contractual deletion obligation upon termination; deletion limited
to primary storage (backups excluded); no deletion verification mechanism; sub-processor
deletion not addressed.

### Step 11: Employee Controls

#### 11a. Privacy and Security Training

| Control | Requirement | Vendor Status | Classification |
|---------|-------------|---------------|----------------|
| Annual privacy training | All staff handling personal data — annual minimum | [Description] | G / Y / R |
| Role-based security training | Developers: secure coding; admins: PAM; support: data handling | [Description] | G / Y / R |
| Phishing simulation | Regular phishing simulations with targeted training for failures | [Description] | G / Y / R |
| New hire training | Privacy and security training before access granted | [Description] | G / Y / R |
| Training completion tracking | Documented completion records available on request | Yes / No | G / Y / R |

#### 11b. Background Screening

| Control | Requirement | Vendor Status | Classification |
|---------|-------------|---------------|----------------|
| Criminal background check | For staff with access to sensitive personal data | Yes / No / [Scope] | G / Y / R |
| Employment verification | Prior employment history verified | Yes / No | G / Y / R |
| Ongoing screening | Periodic or triggered re-screening (e.g., upon role change) | Yes / No | G / Y / R |
| Contractor screening | Same standards applied to contractors as employees | Yes / No | G / Y / R |
| Confidentiality agreements | All staff with data access sign NDAs / confidentiality undertakings | Yes / No | G / Y / R |

[JURISDICTION-SPECIFIC] Background screening practices are subject to local employment and
anti-discrimination law. Verify that the vendor's screening practices comply with applicable
law in each jurisdiction where employees process personal data. [VERIFY for US: FCRA
compliance; UK: Rehabilitation of Offenders Act 1974; EU: GDPR Art. 9 constraints on
processing criminal conviction data about employees.]

### Step 12: Business Continuity and Disaster Recovery

| Control | Requirement | Vendor Status | Classification |
|---------|-------------|---------------|----------------|
| BCP documented | Written Business Continuity Plan covering personal data systems | Yes / No | G / Y / R |
| RTO defined | Recovery Time Objective stated and tested | [RTO] / Not stated | G / Y / R |
| RPO defined | Recovery Point Objective stated and tested | [RPO] / Not stated | G / Y / R |
| DR testing | Annual minimum DR test with documented results | Yes / No / [Frequency] | G / Y / R |
| Backup verification | Backup integrity verified through restoration testing | Yes / No | G / Y / R |
| Multi-region / availability zone | Data replicated across geographically separated facilities | Yes / No | G / Y / R |
| Uptime SLA | SLA stated with service credits for downtime | [%] / Not stated | G / Y / R |
| Notification of outages | Contractual obligation to notify customer of material outages | Yes / No / [SLA] | G / Y / R |
| Personal data in BCP scope | BCP explicitly includes personal data systems, not just operational systems | Yes / No | G / Y / R |

**RED triggers**: No documented BCP; DR never tested; RTO/RPO not defined for systems
processing personal data; backups not tested for restoration; personal data explicitly
excluded from BCP scope.

### Step 13: Regulatory Certifications

Verify the currency, scope, and applicability of claimed certifications:

| Certification | Claimed | Certificate / Report Available | Issuing Body | Validity Period | Scope Includes Relevant Systems | Classification |
|---------------|---------|-------------------------------|--------------|-----------------|--------------------------------|----------------|
| SOC 2 Type II | Yes / No | Report available / Summary only / None | [Auditor] | [Date range] | Yes / No / Partial | G / Y / R |
| SOC 2 Type I | Yes / No | [Same columns] | | | | G / Y / R |
| ISO 27001:2022 | Yes / No | Certificate available | [Certification body] | [Expiry date] | Yes / No / Partial | G / Y / R |
| ISO 27701:2019 | Yes / No | Certificate available | [Certification body] | [Expiry date] | Yes / No / Partial | G / Y / R |
| PCI DSS | Yes / No | AoC available | [QSA] | [Expiry date] | Yes / No | G / Y / R |
| FedRAMP | Yes / No | Authorization level | [JAB / Agency] | [Date] | Yes / No | G / Y / R |
| CSA STAR | Yes / No | Level (1/2/3) | [Certification body] | [Date] | Yes / No | G / Y / R |

**SOC 2 evaluation guidance:**
- SOC 2 Type II is preferred over Type I (Type II tests operating effectiveness over a
  period, typically 6–12 months; Type I tests only design adequacy at a point in time)
- Review the Management Description section for services and infrastructure in scope —
  verify that services being procured are explicitly in scope
- Review the applicable Trust Services Criteria — Security (CC) is mandatory; review
  whether Availability, Confidentiality, Privacy are included where relevant
- Review the Complementary User Entity Controls (CUECs) — these are obligations that
  fall on the customer (your organization) to make the vendor's controls effective
- Review exceptions noted in the auditor's opinion — "qualified" opinions or a high
  number of exceptions in a relevant area are RED flags

**ISO 27001 evaluation guidance:**
- Verify certificate against the IAF accreditation database [VERIFY: current IAF
  directory URL] — certificates may be forged or expired
- Confirm the scope (Statement of Applicability) includes the services being procured
- ISO 27001:2022 transition deadline was October 31, 2025 — certificates issued to the
  2013 standard after this date should be verified [VERIFY current UKAS/IAF guidance]

**YELLOW triggers**: SOC 2 Type I only (insufficient for Tier 1 vendors); audit period
ending more than 12 months ago; scope excludes relevant services; multiple exceptions in
relevant trust services criteria.

**RED triggers**: No certifications claimed by a Tier 1 or Tier 2 vendor; expired
certificate with no renewal in progress; certificate scope explicitly excludes the
services being procured; qualified SOC 2 opinion with material exceptions in security
criteria.

### Step 14: Contractual Safeguards Review

Review the DPA and main agreement to verify contractual safeguards adequacy.
For detailed DPA review and negotiation, use `legalcode-dpa-review-and-negotiation`.

#### 14a. GDPR Article 28 Mandatory DPA Elements

[JURISDICTION-SPECIFIC: GDPR] The following 12 elements are mandatory in every DPA
where GDPR applies. Absence of any mandatory element renders the DPA non-compliant:

| # | Mandatory Element | GDPR Provision | Present | Classification |
|---|------------------|----------------|---------|----------------|
| 1 | Subject-matter, duration, nature, and purpose of processing | Art. 28(3) preamble | Yes / No | G / R |
| 2 | Type of personal data and categories of data subjects | Art. 28(3) preamble | Yes / No | G / R |
| 3 | Processing only on documented controller instructions | Art. 28(3)(a) | Yes / No | G / R |
| 4 | Confidentiality obligations on authorized persons | Art. 28(3)(b) | Yes / No | G / R |
| 5 | Security measures per Article 32 (risk-appropriate) | Art. 28(3)(c) | Yes / No | G / R |
| 6 | Sub-processor authorization mechanism (specific or general) | Art. 28(3)(d) | Yes / No | G / R |
| 7 | Data subject rights assistance (access, erasure, portability) | Art. 28(3)(e) | Yes / No | G / R |
| 8 | DPIA and prior consultation assistance | Art. 28(3)(f) | Yes / No | G / R |
| 9 | Deletion or return of data upon termination | Art. 28(3)(g) | Yes / No | G / R |
| 10 | Audit rights — right to conduct or commission audits | Art. 28(3)(h) | Yes / No | G / R |
| 11 | Processor notifies controller if instruction violates GDPR | Art. 28(3) | Yes / No | G / R |
| 12 | Sub-processor flow-down contract requirements | Art. 28(4) | Yes / No | G / R |

#### 14b. CCPA/CPRA Service Provider Agreement Elements

[JURISDICTION-SPECIFIC: CCPA/CPRA] For California personal information, the service
provider or contractor agreement must include:

| Element | CPRA Requirement | Present | Classification |
|---------|-----------------|---------|----------------|
| Specific, limited processing purpose | Cal. Civ. Code § 1798.140(ag) | Yes / No | G / R |
| Prohibition on selling or sharing personal information | § 1798.140(ag)(1) | Yes / No | G / R |
| Prohibition on retaining, using, or disclosing for other purposes | § 1798.140(ag)(2) | Yes / No | G / R |
| Audit rights (annual; automated scans acceptable) | § 1798.140(ag)(6) | Yes / No | G / Y |
| Service provider's obligation to notify if it can no longer comply | § 1798.140(ag)(5) | Yes / No | G / Y |
| Flow-down to sub-service providers | § 1798.140(ag)(3) | Yes / No | G / R |
| Consumer rights fulfillment cooperation | § 1798.100 et seq. | Yes / No | G / Y |

#### 14c. HIPAA Business Associate Agreement Elements

[JURISDICTION-SPECIFIC: HIPAA] For relationships involving Protected Health Information
(PHI), a HIPAA-compliant Business Associate Agreement (BAA) must include:

| Element | 45 C.F.R. § 164.504(e) | Present | Classification |
|---------|----------------------|---------|----------------|
| Permitted uses and disclosures of PHI | § 164.504(e)(2)(i) | Yes / No | G / R |
| Prohibition on unauthorized use or disclosure | § 164.504(e)(2)(ii)(A) | Yes / No | G / R |
| Appropriate safeguards (Security Rule-aligned) | § 164.504(e)(2)(ii)(B) | Yes / No | G / R |
| Reporting of breaches / unauthorized disclosures within 30 days | § 164.504(e)(2)(ii)(C) | Yes / No | G / R |
| Sub-BA flow-down requirements | § 164.504(e)(2)(ii)(D) | Yes / No | G / R |
| Individual rights support (access, amendment, accounting) | § 164.504(e)(2)(ii)(E-G) | Yes / No | G / R |
| HHS audit / compliance access | § 164.504(e)(2)(ii)(H) | Yes / No | G / R |
| Return or destruction of PHI upon termination | § 164.504(e)(2)(ii)(J) | Yes / No | G / R |
| Termination for material breach | § 164.504(e)(2)(iii) | Yes / No | G / Y |

#### 14d. Audit Rights Adequacy

Regardless of the applicable regime, contractual audit rights should be assessed:

| Audit Rights Element | Present | Adequacy | Classification |
|----------------------|---------|----------|----------------|
| Right to audit specified (not just "inspect") | Yes / No | Adequate / Weak | G / Y / R |
| Frequency stated (minimum annual for Tier 1) | Yes / No | [Frequency] | G / Y / R |
| Adequate notice period (30 days is common) | Yes / No | [Period] | G / Y / R |
| Third-party audit report accepted in lieu of on-site (SOC 2 / ISO 27001) | Yes / No | — | G / Y |
| On-site audit rights reserved for material concerns | Yes / No | — | G / Y |
| Scope covers sub-processors | Yes / No | — | G / Y / R |
| Cost allocation specified | Yes / No | — | G / Y |
| Confidentiality protection for audit findings | Yes / No | — | G / Y |

**RED triggers**: No audit rights; audit rights are purely theoretical (no mechanism
to exercise); audit scope excludes sub-processors; third-party audit reports not accepted
in lieu of on-site audit (unreasonable burden for routine review).

### Step 15: Data Subject Rights Fulfillment

Assess whether the vendor can technically and operationally support the controller's
data subject rights obligations:

| Rights Obligation | Technical Capability | SLA / Process | Documented? | Classification |
|------------------|---------------------|---------------|-------------|----------------|
| Access / portability (GDPR Art. 15/20; CCPA § 1798.100) | Full / Partial / None | [Days] | Yes / No | G / Y / R |
| Erasure / deletion (GDPR Art. 17; CCPA § 1798.105) | Full / Partial / None | [Days] | Yes / No | G / Y / R |
| Rectification (GDPR Art. 16) | Full / Partial / None | [Days] | Yes / No | G / Y / R |
| Restriction of processing (GDPR Art. 18) | Full / Partial / None | [SLA] | Yes / No | G / Y / R |
| Objection to processing (GDPR Art. 21) | Full / Partial / None | [SLA] | Yes / No | G / Y / R |
| Opt-out of sale/sharing (CCPA § 1798.120) | Full / Partial / None | [SLA] | Yes / No | G / Y / R |
| Automated decision-making opt-out (GDPR Art. 22) | Full / Partial / None | [Process] | Yes / No | G / Y / R |

**⟁ CLARIFY** — If the vendor's rights-fulfillment capability is unclear from documentation,
ask: "Can you provide documentation of the technical process for responding to [specific
right] requests propagated from your customers to your platform? What is your SLA, and
does this SLA allow your customers to meet their own statutory deadlines?"

**RED triggers**: Vendor has no documented mechanism to propagate or respond to erasure
or access requests; SLA for erasure exceeds the controller's statutory obligation;
automated decision-making with significant effects on data subjects occurs but vendor
has no opt-out mechanism.

### Step 16: Overall Vendor Risk Rating

Synthesize all domain findings into an overall vendor risk rating:

#### 16a. Domain-Level Summary

| Assessment Domain | Classification | Key Findings |
|------------------|----------------|--------------|
| Security Controls | G / Y / R | [Summary] |
| Sub-Processor Management | G / Y / R | [Summary] |
| Breach Detection & Notification | G / Y / R | [Summary] |
| Cross-Border Transfers | G / Y / R | [Summary] |
| Data Retention & Deletion | G / Y / R | [Summary] |
| Employee Controls | G / Y / R | [Summary] |
| Business Continuity & DR | G / Y / R | [Summary] |
| Regulatory Certifications | G / Y / R | [Summary] |
| Contractual Safeguards | G / Y / R | [Summary] |
| Data Subject Rights | G / Y / R | [Summary] |
| Ongoing Monitoring Capability | G / Y / R | [Summary] |

#### 16b. Overall Vendor Rating

| Rating | Criteria | Recommended Action |
|--------|----------|--------------------|
| **APPROVED** | No RED domains; maximum 3 YELLOW domains (none in contractual safeguards) | Proceed to contract execution; schedule periodic reassessment |
| **CONDITIONALLY APPROVED** | 1–2 RED domains in non-critical areas; or 4+ YELLOW domains; no CRITICAL findings | Conditional approval with 60-day remediation plan; re-assessment of RED domains at 60 days |
| **HIGH RISK** | RED in contractual safeguards OR security controls OR breach notification; 3+ RED domains | Do not proceed until RED items remediated; escalate to DPO and business sponsor |
| **PROHIBITED** | Missing GDPR Art. 28 DPA; missing HIPAA BAA where PHI involved; unlawful transfer mechanism; CRITICAL finding in any domain | Processing prohibited; vendor cannot be engaged for this data category until deficiencies resolved |

#### 16c. Conditional Approval Framework

When the vendor receives CONDITIONALLY APPROVED or HIGH RISK, issue a remediation plan:

| Finding | Domain | Severity | Remediation Required | Deadline | Owner |
|---------|--------|----------|---------------------|----------|-------|
| [Finding] | [Domain] | RED | [Specific remediation] | 30 / 60 / 90 days | [Vendor team] |
| [Finding] | [Domain] | YELLOW | [Specific remediation or accept with compensating control] | [Timeline] | [Vendor team] |

Compensating controls accepted for YELLOW findings pending remediation:
- Contractual indemnification and insurance requirements
- Enhanced monitoring during remediation period
- Escrow arrangements for data in case of vendor failure
- Reduced data scope until remediation complete

### Step 17: Quality Verification

Before delivering the assessment, run these quality gates.

#### Citation Quality Gates (Run Silently)

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every regulatory claim cites a specific statute, regulation, or published guidance | Add citation or mark "[UNVERIFIED — verify before relying]" |
| **Format** | All citations follow a consistent, recognizable format | Fix format |
| **Currency** | All cited provisions checked for amendment or repeal | Flag "[CHECK CURRENCY — may have been amended]" |
| **Domain** | Analysis stays within applicable regime; no cross-regime contamination without explicit flag | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden | Add confidence qualifier |

#### Self-Interrogation for RED and PROHIBITED Findings

For each RED or PROHIBITED finding, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
statute or principle cited? Would a regulator or DPA in the applicable jurisdiction
actually classify this as a compliance failure? Is there an alternative legal basis
the vendor could rely on that was not considered?

**Pass 2 — Completeness**: Have all applicable regulatory regimes been assessed for this
finding? Could the vendor's practice be compliant in a regime that was not yet analyzed?
Are there regulatory guidance documents, DPA decisions, or enforcement actions that
would inform the classification?

**Pass 3 — Challenge**: What is the strongest argument that this finding is acceptable?
Under what commercial circumstances would a reasonable privacy professional accept this
risk with appropriate mitigations? Is the RED classification proportionate, or could
a well-constructed compensating control convert it to a YELLOW?

If any pass reveals weakness in the classification, revise the finding before delivery.
Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

#### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Clear statutory requirement, unambiguous; settled regulatory guidance | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good regulatory arguments but reasonable professionals might differ | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing guidance | Flag for DPO / privacy counsel review with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — qualified privacy professional to advise]" |

Apply confidence scores to all RED and PROHIBITED findings, and to any YELLOW finding
where the classification is based on a novel regulatory argument.

---

## Severity Classification Framework

### GREEN — Approved / Compliant

The vendor meets or exceeds the assessment baseline for this domain.

**Action**: Document and schedule next reassessment per risk tier. No remediation required.

**Examples**:
- SOC 2 Type II report available, issued within 12 months, in-scope services confirmed,
  no material exceptions in Security criteria
- DPA contains all 12 GDPR Article 28 mandatory elements; verified against checklist
- Breach notification SLA of 24 hours contractually specified; vendor demonstrated
  detection capability via tabletop exercise results

### YELLOW — Conditional / Gap Requiring Attention

The vendor has a gap that should be remediated or negotiated but falls within acceptable
range for lower-risk data categories or with mitigating compensating controls.

**Action**: Issue remediation request with timeline. Accept with compensating controls
pending remediation for non-critical data. Escalate to business sponsor if vendor refuses.

**Examples**:
- SOC 2 Type I only (design adequacy tested, but operating effectiveness not validated
  over time) — acceptable for Tier 3; insufficient for Tier 1
- Breach notification SLA is 72 hours (exactly meeting GDPR supervisory authority
  requirement but leaving controller no time to assess before regulatory notification)
- ISO 27001 certificate scope excludes one supporting service not used in the processing
  relationship — confirm in writing that excluded service does not touch personal data

### RED — High Risk / Non-Compliant

The vendor has a critical gap that prevents processing certain data categories or requires
escalation before proceeding.

**Action**: Do not proceed with processing until gap resolved. Issue formal remediation
notice with 30-day response deadline. Escalate to DPO, CISO, and business sponsor.
Document risk acceptance in writing if business proceeds over DPO objection.

**Examples**:
- No GDPR Article 28 DPA in place (or vendor refuses to sign)
- Breach notification SLA exceeds 7 days (controller cannot meet GDPR 72-hour requirement)
- Data transferred to non-adequate jurisdiction without SCC, IDTA, or DPF coverage
- SOC 2 Type II report contains material exceptions in Security criteria (CC6 or CC7)
- Sub-processor list not provided and vendor refuses to disclose

### CRITICAL — Prohibited

The vendor cannot process this category of data under any circumstances until the
deficiency is fully resolved. Continued engagement would constitute a regulatory violation.

**Action**: Processing immediately prohibited. Notify DPO and Legal. If vendor is already
processing, initiate data recovery and migration planning. Engage external privacy counsel.

**Examples**:
- Vendor processing special category data without a GDPR Art. 9(2) legal basis
- Vendor found to have transferred data to a jurisdiction where a supervisory authority
  has suspended or prohibited transfers
- Missing HIPAA BAA where vendor is processing PHI (violation of 45 C.F.R. § 164.308)
- Vendor subject to OFAC sanctions (data processing may constitute a prohibited transaction)

---

## Prioritization Framework

Prioritize remediation across all findings using this three-tier structure:

**Tier 1 — Must-Have (Critical — remediate within 30 days)**

These findings must be resolved before processing proceeds or as an immediate priority
for existing vendor relationships:
- Any PROHIBITED / CRITICAL classification
- Missing mandatory DPA elements (GDPR Art. 28 / HIPAA BAA)
- Unlawful cross-border transfer mechanism
- No breach notification obligation in contract
- No encryption of personal data at rest
- Missing MFA on administrative accounts

**Tier 2 — Should-Have (High — remediate within 60 days)**

These findings materially weaken the vendor's privacy posture and should be remediated
promptly, with compensating controls accepted in the interim:
- Sub-processor list not current or incomplete
- Breach notification SLA allows fewer than 24 hours for controller response
- Audit rights absent or purely theoretical
- SOC 2 Type II scope excludes material services
- No documented data retention schedule
- No employee privacy training program

**Tier 3 — Nice-to-Have (Medium — include in next contract cycle)**

These findings represent improvements beyond baseline compliance that should be raised
at contract renewal or during good-faith negotiation:
- Upgrade from SOC 2 Type I to Type II
- ISO 27701 certification for vendors processing significant volumes of personal data
- Enhanced sub-processor notification window (advance notice from 30 to 60 days)
- Bug bounty or coordinated vulnerability disclosure program
- Enhanced deletion certification with cryptographic proof

---

## Ongoing Monitoring and Reassessment

### Scheduled Reassessment

| Risk Tier | Reassessment Frequency | Assessment Protocol at Renewal |
|-----------|----------------------|-------------------------------|
| Tier 1 (Critical) | Annual | Full reassessment + updated SOC 2 Type II review |
| Tier 2 (High) | 18 months | Standard reassessment + updated certification |
| Tier 3 (Moderate) | 24 months | Lite questionnaire + certification confirmation |
| Tier 4 (Low) | 36 months | Self-attestation + privacy policy review |

### Event-Driven Reassessment Triggers

Initiate immediate reassessment upon any of the following events:
- [ ] **Breach or security incident** involving the vendor, whether or not it involves
  your organization's data
- [ ] **Regulatory enforcement action** against the vendor (GDPR fine, FTC consent order,
  OCR resolution agreement, etc.)
- [ ] **Material ownership change**: acquisition, merger, private equity buyout,
  significant investor change
- [ ] **Certification lapse**: SOC 2 or ISO 27001 expired or not renewed within 30 days
  of expiry
- [ ] **Infrastructure migration**: data center relocation, migration to new cloud
  provider, significant architecture change
- [ ] **Change in processing scope**: vendor begins processing new data categories or
  sub-processing to new sub-processors
- [ ] **Contract renewal or significant amendment**
- [ ] **Adverse continuous monitoring signal**: significant drop in security rating score
  (Bitsight, SecurityScorecard), credential exposure detected on dark web, CVE with
  CVSS 9.0+ in vendor's disclosed technology stack

### Continuous Monitoring Integration

For Tier 1 and Tier 2 vendors, supplement point-in-time assessments with continuous
monitoring:

| Tool Type | Examples | What It Monitors | Action Threshold |
|-----------|----------|-----------------|-----------------|
| Security rating service | Bitsight, SecurityScorecard | Exposed ports, SSL, credential exposure, darkweb signals | 20+ point rating drop |
| Certificate monitoring | [Automated tool] | SSL/TLS certificate expiry, revocation | 14 days before expiry |
| Compliance certificate tracker | [VRM platform] | SOC 2 / ISO 27001 expiry | 60 days before expiry |
| DPF status checker | dataprivacyframework.gov | DPF certification currency for US vendors | Certification lapse |
| News / enforcement monitoring | [Legal monitoring service] | Regulatory enforcement, breaches, litigation | Material action against vendor |

---

## Anti-Patterns

What NOT to do when conducting vendor privacy assessments:

1. **Treating assessment as a one-time onboarding checkbox** — The most common failure.
   Vendor security posture degrades over time. Most vendor-related breaches occur months
   or years after initial approval. Implement continuous monitoring and scheduled
   reassessment per risk tier.

2. **Accepting "we're SOC 2 certified" without reviewing the report** — SOC 2
   Type I tests design only; Type II tests operating effectiveness. Even a Type II report
   may have a scope excluding the relevant services, a qualified opinion, or material
   exceptions. Always read the management description and auditor's opinion.

3. **Sub-processor chain opacity** — Mapping only the primary vendor and ignoring
   sub-processors. The longest retention period in the sub-processor chain governs
   effective data retention. Controllers are liable for sub-processor failures under
   GDPR Art. 28(4).

4. **Audit rights that are contractual but never exercised** — Organizations include
   audit rights in DPAs but never invoke them, treating SOC 2 report sharing as
   equivalent to comprehensive audit compliance. Regulators hold controllers accountable
   for processor failures regardless of whether a SOC 2 report was reviewed.

5. **Equating vendor size or brand with compliance** — Large, reputable vendors
   frequently fail assessments on specific regulatory requirements (missing HIPAA BAA
   provisions, DPA signed by an entity without authority, sub-processor clause
   inconsistent with GDPR Art. 28(2)). Assess every vendor against the baseline
   regardless of market position.

6. **Reviewing the privacy policy instead of the DPA** — Vendor privacy policies govern
   the vendor's own data subject relationships, not the controller-processor relationship.
   A vendor may have an exemplary privacy policy and a deficient DPA. Both must be assessed,
   but the DPA governs the B2B relationship.

7. **Accepting SaaS defaults without negotiation** — Many SaaS vendors present non-
   negotiable standard DPAs. However, the GDPR Art. 28 mandatory elements are legally
   required — they are not optional even if the vendor calls the DPA "standard." Escalate
   missing mandatory elements rather than accepting a non-compliant DPA.

8. **Ignoring transfer mechanisms for cloud-hosted data** — Failing to assess cross-border
   transfer mechanisms because "the vendor is US-based and so are we." If any data subject
   is in the EEA or UK, GDPR / UK GDPR transfer restrictions apply regardless of where
   the controller is located.

9. **Using 2010 EU Model Clauses** — The 2010 standard contractual clauses were invalidated
   by Schrems II (C-311/18) and formally replaced by the 2021 SCCs. All new arrangements
   after September 27, 2021 must use the 2021 SCCs. Existing 2010 SCC arrangements should
   have been migrated; verify migration has occurred for legacy vendor relationships.

10. **Breach notification SLA that leaves the controller no time to respond** — A
    contractual breach notification SLA of 72 hours (matching GDPR's own deadline)
    leaves the controller zero time to assess the breach before the supervisory authority
    notification deadline. Require 24–36 hours from the vendor to give the controller
    investigation time.

11. **Deletion obligation that excludes backups** — Contracts requiring deletion "from
    production systems" may leave personal data in cold storage or disaster recovery
    backups indefinitely. Deletion obligations must explicitly cover backup data with
    documented timelines for secure purge.

12. **Treating the Data Privacy Framework (DPF) as an automatic solution** — DPF
    certification covers data transfers to the certified entity but does not replace
    the need for a GDPR Art. 28 DPA. DPF certification also does not cover all data
    categories (verify scope). Check currency: DPF certification is annual.

13. **Skipping background screening review for high-risk vendors** — For vendors with
    administrative or privileged access to personal data systems, employee background
    screening is a material control. Failure to verify screening practices has led to
    insider-threat data breaches.

14. **Not verifying certificate scope** — ISO 27001 and SOC 2 certificates have defined
    scopes. A certificate for a subsidiary may not cover the parent; a certificate for
    one data center may not cover the facility processing your data. Always verify that
    the certificate scope covers the services being procured.

15. **Risk-tiering by contract value instead of data sensitivity** — High-value vendor
    contracts are not necessarily high-risk vendors. A large facilities management
    contract with no personal data access is low risk. A small SaaS vendor processing
    employee health data is high risk. Risk-tier by data sensitivity and access level,
    not by commercial value.

16. **Accepting "comply with applicable law" as a security obligation** — Generic
    "comply with applicable law" clauses in vendor contracts do not constitute adequate
    GDPR Art. 32 security measures. Specific technical and organizational measures must
    be described or referenced.

17. **Ignoring sub-processor notification gaps** — Failing to require advance notice
    of sub-processor additions or substitutions. GDPR Art. 28(2) requires the processor
    to give the controller the opportunity to object before engaging a new sub-processor.
    Without contractual advance notice, the controller loses this right in practice.

18. **Continuous monitoring as a substitute for assessment** — Security rating services
    (Bitsight, SecurityScorecard) provide valuable signals but do not assess regulatory
    compliance, contractual safeguards, or internal controls. They supplement point-in-time
    assessment, not replace it.

19. **Failing to document risk acceptance decisions** — When a business owner proceeds
    with a vendor over DPO objection or accepts a YELLOW/RED finding, that decision must
    be documented in writing with the rationale, the accepting authority, and any
    compensating controls. Undocumented risk acceptance leaves the organization without
    a defensible audit trail.

20. **Post-incident DPA review** — Executing vendor agreements with attached DPAs that
    are never reviewed by privacy counsel, discovering deficiencies only during breach
    response. DPA review must be a documented gate in the vendor onboarding workflow,
    not an afterthought triggered by an incident.

---

## Writing Standards

Apply these standards before delivering any vendor assessment output:

1. **Name every gap specifically**: Do not write "the DPA is deficient." Write "The DPA
   does not contain a data subject rights assistance obligation (GDPR Art. 28(3)(e)).
   Insert: [specific language]."

2. **State the regulatory basis for every RED finding**: Every RED classification must
   cite the specific provision that is violated or missing. Findings without regulatory
   basis are opinions, not assessments.

3. **Confidence without evidence is dangerous**: Do not state that a practice is
   "non-compliant" without citing the specific statutory requirement it violates.
   Unverified assertions carry higher risk than expressed uncertainty.

4. **Active voice for all findings**: "The DPA lacks an audit rights clause" not
   "An audit rights clause is lacking in the DPA."

5. **Specific before general**: State the specific gap before the general risk. Not
   "There are security concerns" but "The vendor's penetration testing was last conducted
   in [year], exceeding the 18-month threshold for Tier 2 vendors."

6. **Proportionate language**: YELLOW findings should be worded to prompt negotiation,
   not alarm. RED findings should convey urgency without catastrophizing.

7. **Self-check before delivery**: Re-read every RED finding and ask: "If the vendor's
   privacy counsel read this, is the basis clear enough to generate a productive
   remediation discussion?" If not, add specificity.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When legalcode-mcp is available, use it in Step 3 and throughout the assessment to:
- Retrieve current text of applicable statutory provisions (GDPR Art. 28, Art. 44-49;
  HIPAA § 164.504; CCPA § 1798.140)
- Search for DPA enforcement actions in the relevant jurisdiction (fines for missing
  Art. 28 elements, audit right failures, breach notification non-compliance)
- Verify current adequacy decision status for the relevant destination country
- Check current DPF certification status for US-based vendors

Save findings to `/tmp/legalcode-vendor-privacy-research.md`:

```markdown
# Vendor Privacy Assessment Research — [Vendor Name]
## Date: [date]

### Statutory Verification
- [Provision] — [VERIFIED: current text] or [UNVERIFIED: check authoritative source]

### DPA Enforcement Precedents
- [Case/enforcement action, jurisdiction, relevance]

### Adequacy Status
- [Destination country] — [Current adequacy status, date verified]

### DPF Certification
- [Vendor / entity name] — [Certified: Yes/No, expiry date]
```

### Without legalcode-mcp

Proceed using training knowledge and the statutory references in this skill. Mark all
statutory and enforcement references with [VERIFY] and note in the Glass Box audit trail:
`legalcode_mcp: "Not connected"`. Recommend that the reviewing privacy counsel verify
all regulatory citations against authoritative primary sources before relying on them.

### VRM Platform Integration

When the assessment will be exported to a VRM platform:

| Platform | Export Format | Integration Notes |
|----------|--------------|------------------|
| OneTrust Vendorpedia | JSON / API | Map domains to OneTrust risk categories; export overall rating and finding details |
| Prevalent | CSV / API | Questionnaire responses map to Prevalent risk library; export remediation plan |
| Venminder | PDF + structured data | Export full assessment as PDF; flag Tier 1 findings for Venminder oversight services |
| ProcessUnity | XML / API | Map remediation items to ProcessUnity workflow tasks with owners and deadlines |

---

## Output Format Template

```markdown
# Vendor Privacy Assessment Report

**Vendor**: [Legal entity name and DBA if different]
**Services**: [Description of services being procured]
**Assessment Date**: [Date]
**Assessment Trigger**: [Onboarding / Annual review / Post-incident / Other]
**Assessed By**: [Organization name — AI-assisted; review by [DPO/Privacy Counsel] required]
**Assessment Basis**: [Organizational playbook / Regulatory baselines (GDPR, ISO 27001, etc.)]
**Risk Tier**: [Tier 1 / 2 / 3 / 4] — [Score: X/100]

---

## Overall Vendor Rating: [APPROVED / CONDITIONALLY APPROVED / HIGH RISK / PROHIBITED]

**Confidence**: [Definite / High / Probable]

### Summary Rationale
[2–3 sentences summarizing the overall rating and the primary basis for it]

---

## Key Findings

| # | Finding | Domain | Severity | Remediation Required |
|---|---------|--------|----------|---------------------|
| 1 | [Finding] | [Domain] | RED / YELLOW | [Yes/No — Timeline] |
| 2 | [Finding] | [Domain] | RED / YELLOW | [Yes/No — Timeline] |
| ... | | | | |

---

## Domain-Level Assessment

### Security Controls — [GREEN / YELLOW / RED]

**Overall assessment**: [1–2 sentence summary]

| Sub-domain | Status | Finding |
|------------|--------|---------|
| Encryption | G / Y / R | [Specific finding] |
| Access Controls | G / Y / R | [Specific finding] |
| Vulnerability Management | G / Y / R | [Specific finding] |
| Network Security | G / Y / R | [Specific finding] |
| Audit Logging | G / Y / R | [Specific finding] |
| Physical Security | G / Y / R | [Specific finding] |
| Secure Development | G / Y / R | [Specific finding] |

### Sub-Processor Management — [GREEN / YELLOW / RED]

**Sub-processor list**: [Provided / Not provided / Partial]
**Sub-processor count**: [Number]
**Longest retention in chain**: [Vendor name] — [Period] for [purpose]

[Summary of sub-processor flow-down compliance]

### Breach Detection and Notification — [GREEN / YELLOW / RED]

**Contractual notification SLA**: [Hours] from discovery
**Applicable regime deadline**: GDPR: 72 hours / HIPAA: 60 days / [Other]
**Buffer for controller**: [Hours remaining after vendor notification]

[Summary of detection capability and notification adequacy]

### Cross-Border Transfers — [GREEN / YELLOW / RED]

| Transfer Route | Mechanism | Status |
|----------------|-----------|--------|
| [Origin → Destination] | [SCC / DPF / Adequacy / IDTA] | Valid / Invalid / Missing |

### Data Retention and Deletion — [GREEN / YELLOW / RED]

[Summary of retention schedule and deletion verification capability]

### Employee Controls — [GREEN / YELLOW / RED]

[Summary of training program and background screening]

### Business Continuity and DR — [GREEN / YELLOW / RED]

**RTO**: [Hours] | **RPO**: [Hours] | **Last DR test**: [Date]

[Summary of BCP/DR adequacy]

### Regulatory Certifications — [GREEN / YELLOW / RED]

| Certification | Status | Expiry | Scope Coverage |
|---------------|--------|--------|----------------|
| SOC 2 Type II | [Current / Expired / Not held] | [Date] | [Yes / No / Partial] |
| ISO 27001:2022 | [Current / Expired / Not held] | [Date] | [Yes / No / Partial] |
| [Other] | [Status] | [Date] | [Yes / No] |

### Contractual Safeguards — [GREEN / YELLOW / RED]

**GDPR Art. 28 DPA**: [Present / Absent / Deficient — X/12 mandatory elements]
**HIPAA BAA**: [Present / Absent / Not required — N/A]
**CCPA service provider agreement**: [Present / Absent / Not required — N/A]
**Audit rights**: [Adequate / Inadequate / Absent]

[Summary of specific gaps with proposed redline language for RED items]

### Data Subject Rights Fulfillment — [GREEN / YELLOW / RED]

[Summary of technical and operational capability for rights fulfillment]

---

## Remediation Plan

### Tier 1 — Must-Have (Complete within 30 days)

| # | Finding | Required Action | Responsible Party | Verification Method |
|---|---------|----------------|-------------------|---------------------|
| 1 | [Finding] | [Specific action] | Vendor | [Evidence required] |

### Tier 2 — Should-Have (Complete within 60 days)

| # | Finding | Required Action | Responsible Party | Verification Method |
|---|---------|----------------|-------------------|---------------------|

### Tier 3 — Nice-to-Have (Next contract cycle)

| # | Finding | Recommended Improvement | Proposed Timeline |
|---|---------|------------------------|-------------------|

---

## Stakeholder Impact Map

| Stakeholder | Role | Affected Domains | Risk if Not Remediated | Action Required |
|-------------|------|-----------------|----------------------|-----------------|
| Data subjects | Third party | Data protection rights | Rights unable to be fulfilled | Ensure technical capability |
| Supervisory authority | Regulator | All | Enforcement / fines | Ensure DPA and transfer mechanism in place |
| DPO | Internal oversight | Contractual safeguards | Accountability gap | Sign off on risk acceptance if proceeding over concerns |
| CISO | Security governance | Security controls | Breach risk | Validate technical controls evidence |
| Procurement | Business owner | All | Contract execution risk | Do not countersign without DPO clearance |
| Legal | Contract review | Contractual safeguards | Non-compliant DPA | Negotiate and execute compliant DPA |

---

## Ongoing Monitoring Plan

**Risk Tier**: [Tier] → **Reassessment due**: [Date]
**Continuous monitoring**: [Active / Not implemented]

**Event-based reassessment triggers set**: [Yes / No — list active triggers]

---

## Glass Box Audit Trail

```yaml
glass_box:
  vendor_name: "[Legal entity name]"
  assessment_date: "[Date]"
  assessment_trigger: "[Onboarding / Annual / Post-incident / Other]"
  risk_tier: "[Tier 1 / 2 / 3 / 4] — [Score: X/100]"
  overall_rating: "[APPROVED / CONDITIONALLY APPROVED / HIGH RISK / PROHIBITED]"
  regulatory_regimes_assessed:
    - "[GDPR — VERIFIED / UNVERIFIED]"
    - "[HIPAA — VERIFIED / UNVERIFIED]"
    - "[CCPA/CPRA — VERIFIED / UNVERIFIED]"
    - "[Other]"
  domains_assessed: "11/11 (full) / [N]/11 (partial — specify)"
  red_findings: "[Number] — [brief list]"
  yellow_findings: "[Number]"
  green_findings: "[Number]"
  sub_processors_mapped: "[Number] / [Total disclosed by vendor]"
  dpa_present: "Yes — [X]/12 mandatory elements / No"
  certifications_reviewed: "[SOC 2 Type II / ISO 27001 / Other]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-vendor-privacy-research.md / Not created"
  statutes_consulted:
    - "GDPR Art. 28 — VERIFIED (legalcode-mcp) / UNVERIFIED"
    - "GDPR Arts. 44-49 — VERIFIED / UNVERIFIED"
    - "HIPAA 45 C.F.R. § 164.504(e) — VERIFIED / UNVERIFIED"
    - "CCPA Cal. Civ. Code § 1798.140 — VERIFIED / UNVERIFIED"
  self_interrogation: "PASS / REVISED (see finding #[N]) / NOT APPLICABLE (no RED findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Assessment based on vendor-provided documentation — independent audit not performed]"
    - "[Sub-processor chain verified to depth [N] only — further chain not assessed]"
    - "[Any other scope limitation]"
  reviewer: "AI-assisted — requires qualified privacy professional review before reliance"
```
```

---

## Localization Notes

When adapting this assessment for a specific jurisdiction:

**EU/EEA** (GDPR): Use the full GDPR Art. 28 checklist (Step 14a). Require SCCs 2021
Module 2 for any cross-border transfer to a non-adequate country. Verify DPF certification
for US vendors as an alternative to SCCs where applicable.

**UK** (UK GDPR / IDTA): Replace SCC Module 2 with UK IDTA for transfers. Note that the
UK has its own adequacy decisions (not always identical to EU list). UK ICO has published
IDTA-specific guidance — verify currency. [VERIFY: current UK adequacy country list]

**United States — Federal Sector** (FedRAMP): Add FedRAMP authorization level to the
certifications assessment (Moderate, High, or Agency ATO). FISMA-covered systems require
FedRAMP-authorized SaaS vendors. [VERIFY: current FedRAMP Marketplace status]

**United States — California** (CCPA/CPRA): Step 14b governs. Service provider vs.
contractor categorization matters — verify which category applies based on the nature
of data flows. Third-party designation (neither service provider nor contractor) triggers
the most restrictive data handling obligations.

**United States — Healthcare** (HIPAA/HITECH): Step 14c governs. Confirm covered entity
status and whether vendor qualifies as a Business Associate (BA) under 45 C.F.R. § 160.103.
Sub-BA flow-down is required. HITECH expanded HIPAA to apply directly to BAs — verify
the vendor's own HIPAA compliance program, not just BAA execution.

**Brazil** (LGPD): Operator (operador) obligations parallel GDPR processor obligations.
Transfer mechanisms under LGPD remain subject to ANPD regulatory development — verify
current ANPD guidance on international transfers. [VERIFY: current ANPD Resolution on
international transfers]

**Canada** (PIPEDA / Quebec Law 25): PIPEDA Accountability Principle (Schedule 1, Principle
4.1.3) requires organizations to protect personal information transferred to third parties
by contract or equivalent means. Quebec Law 25 (effective September 2023) introduced
additional requirements including privacy impact assessments for cross-border transfers
(Art. 70.1). [VERIFY: current CPVP / CAI guidance on Law 25 transfers]

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis. Research conducted via
web-backed research covering: GDPR Article 28 and DPA enforcement, EU SCCs 2021
Module structure, UK IDTA (March 2022), EU-US DPF (July 2023), HIPAA BAA requirements,
CCPA/CPRA service provider obligations, ISO 27001:2022 Annex A.5.19-5.23 supplier
controls, SOC 2 Trust Services Criteria, NIS2 supply chain security (Directive 2022/2555),
NIST SP 800-171 Rev. 3, Shared Assessment SIG Core/Lite framework, OneTrust VRM
methodology, and regulatory enforcement precedents (CNIL €40M Criteo, OCR HIPAA BAA
enforcement actions). Informed by structural patterns from `legalcode-contract-review`,
`legalcode-dpa-review-and-negotiation`, and `legalcode-cross-border-transfer-assessment`
reference skills.
