---
name: legalcode-nist-csf-mapping
description: NIST Cybersecurity Framework 2.0 (CSWP 29, February 2024) mapping and maturity assessment
  for organizations implementing, assessing, or reporting against NIST CSF 2.0 across all six functions
  (Govern, Identify, Protect, Detect, Respond, Recover) and 22 categories. Use when assessing current-state
  CSF maturity, designing a Target Profile, performing gap analysis between Current and Target Profiles,
  preparing for a third-party CSF assessment, mapping CSF to other compliance frameworks for harmonized
  control implementation, benchmarking maturity against industry peers, or producing board-ready cybersecurity
  governance reporting.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

NIST Cybersecurity Framework 2.0 (CSWP 29, February 2024) mapping and maturity assessment for organizations implementing, assessing, or reporting against NIST CSF 2.0 across all six functions (Govern, Identify, Protect, Detect, Respond, Recover) and 22 categories. Cross-framework mapping to ISO 27001:2022, SOC 2 Trust Services Criteria (CC1–CC9, Availability, Confidentiality, Privacy), CIS Controls v8 (18 controls / 153 safeguards / IG1–IG3), CMMC 2.0 (Levels 1–3 / NIST SP 800-171/172), and COBIT 2019 (40 governance and management objectives). Regulatory overlay assessment for HIPAA Security Rule (NIST SP 800-66r2), GLBA/FTC Safeguards Rule, SEC cybersecurity disclosure rules, FISMA, NYDFS 23 NYCRR Part 500, and NIS2 Directive (2022/2555) CSF alignment. Use when assessing current-state CSF maturity, designing a Target Profile, performing gap analysis between Current and Target Profiles, preparing for a third-party CSF assessment, mapping CSF to other compliance frameworks for harmonized control implementation, benchmarking maturity against industry peers, or producing board-ready cybersecurity governance reporting. Covers all 106 CSF 2.0 subcategories with implementation evidence requirements, Tier 1–4 maturity characterization per function and overall, control-gap-to-regulatory-obligation mapping, and POAM (Plan of Action and Milestones) generation. Produces current-state maturity assessments with Partial/Risk-Informed/Repeatable/Adaptive tier classifications, cross-framework alignment matrices, prioritized implementation roadmaps (IMMEDIATE/ NEAR-TERM/BACKGROUND), GRC-platform-ready control-to-requirement mapping tables, and Glass Box audit trails. Jurisdiction-agnostic core (NIST CSF 2.0, US-originated but internationally adopted) with [JURISDICTION-SPECIFIC] markers for sector-specific regulatory overlays (HIPAA, GLBA, SEC, FISMA, NYDFS, NIS2, CRA) and international alignment (Italy National Cybersecurity Framework, ISO 27001 parallel certification paths).


# NIST CSF 2.0 Mapping and Maturity Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing and mapping
> organizational cybersecurity controls against the NIST Cybersecurity Framework 2.0
> (NIST CSWP 29, February 2024) and related frameworks. It does not constitute legal
> advice, regulatory certification, or a formal compliance audit. NIST does not issue
> certifications, endorse third-party assessors, or validate organizational assessments.
> Cross-framework mapping relationships cited here are derived from official NIST OLIR
> catalog entries, AICPA crosswalk tables, CIS Controls v8 mappings, and ISACA publications —
> verify all mappings against current authoritative sources before relying on them for
> compliance purposes. Regulatory references (HIPAA, GLBA, SEC, FISMA, NYDFS, NIS2) carry
> legal and technical obligations beyond CSF alignment; seek qualified cybersecurity legal
> counsel for regulatory compliance determinations. AI-generated analysis carries hallucination
> risk for cited authority: any statutory references, NIST document numbers, or regulatory
> interpretations should be independently verified by a qualified professional.

## Purpose and Scope

This skill assesses an organization's cybersecurity control posture against the NIST
Cybersecurity Framework 2.0 (CSWP 29) and produces cross-framework mappings, maturity
tier assessments, gap analyses, and prioritized implementation roadmaps. It is designed
for GRC professionals, CISOs, security compliance teams, and external assessors working
with CSF as a risk management or regulatory alignment tool.

**Covers:**

- All six CSF 2.0 functions: **Govern (GV)**, Identify (ID), Protect (PR), Detect (DE),
  Respond (RS), Recover (RC) — with all 22 categories and 106 subcategories
- Implementation Tier characterization (Tier 1: Partial through Tier 4: Adaptive) per
  function and overall organizational posture
- Current Profile assessment and Target Profile development with gap analysis
- Cross-framework mapping: CSF 2.0 ↔ ISO 27001:2022, SOC 2 TSC, CIS Controls v8,
  CMMC 2.0 (NIST SP 800-171/172), and COBIT 2019
- Regulatory overlay assessment for sector-specific obligations (HIPAA, GLBA/FTC
  Safeguards Rule, SEC cybersecurity disclosure, FISMA, NYDFS Part 500, NIS2)
- POAM generation: prioritized remediation tasks with owners, timelines, and success metrics
- GRC platform export guidance (ServiceNow, OneTrust, Archer, LogicGate, Cybersaint)
- Control redundancy and harmonization analysis across multiple frameworks

**Does not:**

- Issue NIST CSF certifications or endorse organizational assessments (NIST does not do this)
- Provide formal compliance opinions on HIPAA, GLBA, CMMC, or other regulations — CSF
  alignment is one input to compliance, not a substitute for regulatory analysis
- Replace a formal third-party CSF assessment by a qualified cybersecurity firm
- Cover technical penetration testing, vulnerability scanning, or red team assessments
- Assess frameworks not listed above (PCI DSS, FedRAMP, DORA — though DORA/NIS2 alignment
  markers are included)
- Provide legal advice on regulatory exposure, enforcement risk, or litigation strategy

**Related skills:**

- `legalcode-nis2-compliance-assessment` — NIS2 Directive (EU 2022/2555) compliance;
  NIS2 and NIST CSF share a risk-based approach; for EU-regulated entities use both
- `legalcode-incident-response-plan-builder` — NIST SP 800-61r3 IRP aligned to
  CSF RS/RC functions; use for detailed incident response plan development
- `legalcode-compliance-program-builder` — ISO 37301 / DOJ ECCP program design;
  integrates with CSF GOVERN function governance outputs
- `legalcode-vendor-privacy-assessment` — Third-party vendor risk assessment aligning
  with CSF GV.SC (Supply Chain Risk Management)
- `legalcode-ai-governance-framework-builder` — ISO 42001 / NIST AI RMF governance
  builder; bridges AI-specific controls with CSF GOVERN function

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill anchored to the NIST Cybersecurity Framework 2.0
(February 2024, NIST CSWP 29). NIST CSF originated in US federal policy (Executive Order
13636, 2013) but has been widely adopted internationally and is referenced or endorsed in
regulatory frameworks across multiple jurisdictions.

**US regulatory context**: FISMA requires federal agencies to implement NIST risk management
frameworks. CSF is explicitly referenced in Executive Order 14028 (2021). CISA Binding
Operational Directives (BODs) align to specific CSF functions (BOD 23-01 → ID.AM, BOD
22-01 → DE.CM/PR.PS). NYDFS 23 NYCRR Part 500 (2023 amendments) expects use of "a
nationally recognized cybersecurity framework" including NIST CSF. FTC Safeguards Rule
(effective June 2023) expects a risk-based program consistent with CSF principles.

**International context**: Italy's National Cybersecurity Framework (Piano Nazionale di
Ripresa e Resilienza, updated 2025) explicitly aligns with NIST CSF 2.0. Ireland references
CSF 2.0 in NIS2 national implementation guidance. ISO 27001:2022 shares approximately 83%
control domain overlap with CSF 2.0.

[JURISDICTION-SPECIFIC] For US federal agencies: FISMA mandates use of NIST Risk Management
Framework (RMF) and SP 800-53 as the technical control catalog; CSF serves as the
organizational risk management layer. Federal entities may need additional RMF/ATO process.

[JURISDICTION-SPECIFIC] For EU-regulated entities (NIS2 essential/important): CSF alignment
supports NIS2 Article 21 risk management measures but does not substitute for NIS2 national
implementation compliance. Run `legalcode-nis2-compliance-assessment` in parallel.

[JURISDICTION-SPECIFIC] For defense contractors (CMMC 2.0): Level 2 (C3PAO assessment)
requires demonstrating 110 practices from NIST SP 800-171 Rev 2; CSF is used as a planning
tool but CMMC certification requires a separate formal assessment.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. Rather than assuming the
user's context, the workflow pauses and asks when:

- The answer would change the scope or direction of the assessment
- Multiple valid assessment approaches exist and the user's preference matters
- Regulatory overlay selection depends on the organization's sector and jurisdiction
- Current maturity tier is ambiguous and evidence is needed before classification

Use the structured options pattern (bullet options + "Why this matters" explanations)
wherever ⟁ CLARIFY appears below. If the user has already provided the information (e.g.,
in the initial prompt or prior conversation), skip the question and proceed.

For batch/non-interactive runs, apply these defaults:

- Operating mode: Full assessment
- Scope: All six functions
- Regulatory overlay: None (general CSF only)
- Target tier: Determined from risk context provided

---

## Workflow

### Step 1: Accept Input

Accept the organization's cybersecurity posture information in any of these formats:

- **Existing assessment data**: Prior CSF assessment results, ISO 27001 statement of
  applicability, SOC 2 report, audit findings, CMMC SPRS score
- **Control inventory**: Spreadsheet or document listing existing security controls mapped
  to functions, categories, or subcategories
- **Narrative description**: Text description of the organization's current security
  posture, policies, and implemented technologies
- **GRC platform export**: JSON, CSV, or structured export from OneTrust, Archer, ServiceNow,
  LogicGate, Cybersaint, or AuditBoard
- **Policy documents**: Security policies, procedures, risk management documents, and
  incident response plans
- **No existing data**: Organization is starting from scratch; proceed to Step 2 for
  guided intake

If no structured input is provided, proceed to Step 2 to conduct a discovery questionnaire.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask these questions. Present structured
options; allow free-text for context details.

1. **Organization profile**:
   - Sector (Healthcare / Finance and Banking / Defense / Technology / Energy / Government /
     Retail / Other critical infrastructure / Other)
   - Approximate size (Small: <100 employees; Medium: 100–1,000; Large: >1,000)
   - Geographic operations (US-only / US + EU / Global)
   - _Why this matters_: Sector determines applicable regulatory overlays; size affects
     proportionality guidance and CIS Implementation Group (IG1/IG2/IG3) targeting.

2. **Assessment driver**:
   - Options: Internal governance improvement / Third-party customer requirement / Board
     reporting / Regulatory compliance (specify) / CMMC certification preparation / Pre-audit
     gap analysis / ISO 27001 certification acceleration / M&A due diligence / Other
   - _Why this matters_: The driver determines which framework mappings to emphasize and
     what output format to prioritize.

3. **Existing frameworks in use**:
   - Options: ISO 27001:2022 (certified) / ISO 27001 (implementing) / SOC 2 (report exists) /
     CIS Controls v8 / CMMC 2.0 Level 1/2/3 / None / Other
   - _Why this matters_: Existing frameworks provide a head-start on CSF mapping and allow
     the assessment to focus on gaps rather than fully recertified areas.

4. **Assessment scope**:
   - Options: Full assessment (all six functions) / Prioritized functions only (specify) /
     Single function deep-dive / Cross-framework mapping only (no new assessment) /
     Target Profile development only (current state known)
   - _Why this matters_: Scoping determines depth, duration, and resource requirements
     for the assessment.

5. **Target tier aspiration**:
   - Options: Determine target from risk context / Minimum viable (Tier 2: Risk-Informed) /
     Formal program (Tier 3: Repeatable) / Continuous improvement (Tier 4: Adaptive) /
     Accept current tier; no uplift planned
   - _Why this matters_: Target tier shapes the gap analysis — not every organization
     needs or benefits from Tier 4; appropriate target depends on risk context and budget.

### Step 3: Determine Regulatory Overlays

**⟁ CLARIFY** — Based on the sector and driver from Step 2, confirm applicable regulatory
overlays. Present only relevant options for the identified sector.

**Healthcare sector**:

- HIPAA Security Rule (45 C.F.R. Parts 160, 162, 164) — NIST SP 800-66r2 provides the
  official crosswalk; applicable to covered entities and business associates

**Financial services sector**:

- GLBA / FTC Safeguards Rule (16 C.F.R. Part 314, effective June 9, 2023) — non-banking
  financial institutions
- NYDFS 23 NYCRR Part 500 (2023 amendments) — licensed financial institutions in New York
- SEC Cybersecurity Disclosure Rules (effective December 2023) — public companies
- Federal Reserve / OCC / FDIC — banking organizations

**Defense / federal government**:

- FISMA / NIST RMF (SP 800-37 Rev 2) — federal agencies and federal contractors
- CMMC 2.0 — DoD contractors (Level 1: basic cyber hygiene; Level 2: 110 SP 800-171
  practices; Level 3: 110+ SP 800-172 practices)
- CISA Binding Operational Directives — federal civilian executive branch agencies

**EU-regulated operations**:

- NIS2 Directive (2022/2555) — essential and important entities in the EU; for full NIS2
  assessment run `legalcode-nis2-compliance-assessment`
- EU Cyber Resilience Act (CRA) — manufacturers of products with digital elements [VERIFY
  current implementation timeline]

**Multiple / general**:

- No sector-specific overlay — assess against CSF core only
- Multiple overlays — assess against CSF then generate per-overlay gap tables

### Step 4: Load Reference Authority

Before beginning the function-by-function assessment, gather current reference material.

1. **Primary reference**: NIST CSWP 29 (NIST CSF 2.0, February 2024) — the authoritative
   framework document. Access current subcategory and implementation example data via
   the NIST CPRT (Cybersecurity and Privacy Reference Tool) at:
   `csrc.nist.gov/projects/cprt/catalog`

2. **Cross-framework references** (load only those needed for the confirmed overlays):
   - ISO 27001:2022 ↔ CSF 2.0 OLIR: `csrc.nist.gov/projects/olir/informative-reference-catalog/details?referenceId=154`
   - CIS Controls v8 ↔ CSF 2.0: `cisecurity.org/insights/white-papers/cis-controls-v8-mapping-to-nist-csf-2-0`
   - AICPA TSC ↔ CSF: `aicpa-cima.com/resources/download/mapping-2017-trust-services-criteria-to-nist-csf`
   - HIPAA Security Rule ↔ CSF 2.0: NIST SP 800-66r2, Appendix D [VERIFY: now in CPRT]

3. **Regulatory overlay documents** (for confirmed overlays):
   - HIPAA: 45 C.F.R. §§ 164.302–164.318 Security Rule standards
   - FTC Safeguards: 16 C.F.R. Part 314 Final Rule (2021, effective 2023)
   - SEC Cyber: Form 8-K Item 1.05; Form 10-K Item 1C; Release S7-09-22
   - FISMA: OMB Circular A-130; NIST SP 800-37 Rev 2 RMF
   - NYDFS 500: 23 NYCRR Part 500 (2023 amendment text)

Save key reference data to a temporary file if legalcode-mcp is connected:

```
/tmp/nist-csf-mapping-research-[date].md
```

**If legalcode-mcp is not connected**: Proceed with built-in cross-framework mapping
tables in the Cross-Framework Alignment Matrix section below. Mark all cited subcategory
numbers and regulatory provisions with [VERIFY] in the output.

### Step 5: Conduct Discovery Questionnaire (if no existing data)

If the organization has not provided structured control documentation, conduct a guided
discovery across six function areas. For each function, ask:

- **What exists**: Documented policies, procedures, and implemented technologies
- **What is practiced**: Evidence of consistent execution (not just documentation)
- **What is measured**: Metrics, KPIs, and monitoring in place
- **What is governed**: Board/leadership visibility and accountability

Use the CSF 2.0 reference structure in the **NIST CSF 2.0 Reference Structure** section
below to frame questions. Do NOT ask about all 106 subcategories individually — group by
category and focus on evidence of outcomes, not control names.

### Step 6: Assess GOVERN Function (GV)

**The GOVERN function is new in CSF 2.0 and central to the framework.** It addresses
organizational cybersecurity risk management strategy, expectations, and policy. GOVERN
informs all other five functions. Assess against six categories:

**GV.OC — Organizational Context** (GV.OC-01 through GV.OC-05): Assess whether the
organization understands its mission, stakeholder expectations, legal and regulatory
obligations, and critical asset dependencies that shape cybersecurity decisions.

| Subcategory                                                         | Evidence Required                                                     | Tier 1 Indicator   | Tier 3–4 Indicator                                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------- |
| GV.OC-01: Organizational mission aligned to cybersecurity           | Mission statement; cyber risk tolerance linked to business objectives | No documented link | Cyber risk formally scoped to business mission in board-level document |
| GV.OC-02: Legal, regulatory, contractual obligations catalogued     | Regulatory register; legal obligation tracker                         | Ad hoc list        | Formal register, owner assigned, reviewed annually                     |
| GV.OC-03: Business environment understood; dependencies mapped      | Asset/system dependency map; vendor catalog                           | No documentation   | Formal dependency map updated on change                                |
| GV.OC-04: Risk tolerance statement approved                         | Written risk appetite / tolerance statement                           | None               | Board-approved, quantified, reviewed annually                          |
| GV.OC-05: Supplier dependencies understood in cybersecurity context | Vendor tier classification; critical vendor list                      | No classification  | Formal C-SCRM policy with tier-based DD                                |

**GV.RM — Risk Management Strategy**: Risk tolerance, constraints, and assumptions
informing operational cyber risk decisions. Assess: risk appetite formalization, risk
management policy, integration with enterprise risk management (ERM).

**GV.RR — Roles, Responsibilities, and Authorities**: Cybersecurity accountability
structure. Assess: CISO/ISSO role definition, board-level accountability (GV.RR-01
requires board engagement), RACI documentation, accountability for GV.SC.

**⟁ CLARIFY** — Board and leadership accountability often requires sensitive validation.
Before classifying GV.RR-01 (leadership accountable for cybersecurity risk), confirm:

- Does the board receive regular cybersecurity reporting? How frequently?
- Is there a named executive accountable for cybersecurity risk (CISO, CRO, or equivalent)?
- Has the board approved the cybersecurity risk management strategy?

**GV.PO — Policy**: Organizational cybersecurity policy established, communicated, and
enforced. Assess: policy hierarchy (enterprise → domain-specific), communication channels,
enforcement mechanisms, review cycle.

**GV.OV — Oversight**: Assess whether results of cybersecurity risk management activities
are used to improve the risk management strategy. Key evidence: board reporting cadence,
CISO reporting line, continuous improvement loop between GV functions and operations.

**GV.SC — Cybersecurity Supply Chain Risk Management** (GV.SC-01 through GV.SC-10): The
largest single category in CSF 2.0 with 10 subcategories. Assess: C-SCRM plan existence
and scope, supplier risk classification (tier-based due diligence), contractual security
requirements, vendor monitoring program, incident communication with suppliers.

### Step 7: Assess IDENTIFY Function (ID)

**IDENTIFY** — The organization understands its current cybersecurity risks. Three categories:

**ID.AM — Asset Management** (ID.AM-01 through ID.AM-08): Assess hardware asset
inventory, software asset inventory, network resource inventory, data inventory (with
classification), service/facility inventory, and personnel catalog against cybersecurity
roles. Evidence: CMDB or asset inventory system; software bill of materials (SBOM) for
regulated entities; data classification policy.

**ID.RA — Risk Assessment** (ID.RA-01 through ID.RA-10): Assess: documented risk
assessment methodology; threat identification process; vulnerability identification (internal
scanning + external threat intelligence); impact and likelihood analysis; risk response
decisions documented; asset criticality ratings. Evidence: current risk assessment report;
threat model; CVE tracking / vulnerability scan reports; risk register.

**ID.IM — Improvement** (ID.IM-01 through ID.IM-04) [NEW in CSF 2.0]: Assess whether
the organization learns from cybersecurity activities and improves continuously. Evidence:
lessons-learned process after incidents or tests; metrics reviewed and acted upon;
improvements tracked and closed.

### Step 8: Assess PROTECT Function (PR)

**PROTECT** — Safeguards to manage cybersecurity risks. Five categories:

**PR.AA — Identity Management, Authentication, and Access Control** (PR.AA-01 through
PR.AA-06): Assess: identity lifecycle management (provisioning, de-provisioning); MFA
deployment scope; least-privilege implementation; privileged access management (PAM); remote
access controls; physical access controls aligned to digital access. Evidence: identity
governance tool; MFA enrollment rates; PAM tool; access review documentation.

**PR.AT — Awareness and Training** (PR.AT-01 through PR.AT-02): Assess: security awareness
training program (coverage, frequency, role-based curriculum); privileged user and
administrator specialized training. Evidence: LMS records; completion rates; phishing
simulation results; role-specific training curriculum.

**PR.DS — Data Security** (PR.DS-01 through PR.DS-11): Assess: data classification
implementation; encryption at rest and in transit (standards: AES-256, TLS 1.3+); DLP
controls; data retention and disposal; backup policy and testing; integrity verification.
Evidence: encryption configuration standards; DLP alert reports; backup test results;
data destruction records.

**PR.PS — Platform Security** (PR.PS-01 through PR.PS-06): Assess: secure configuration
baselines (CIS Benchmarks or equivalent); software supply chain security; vulnerability
management cycle (scan → patch → verify); patch management metrics (mean time to patch by
severity); software lifecycle management; log configuration. Evidence: configuration
management database; patch SLAs by CVE severity; vulnerability management dashboard.

**PR.IR — Technology Infrastructure Resilience** (PR.IR-01 through PR.IR-04): Assess:
network segmentation architecture; resilience design (redundancy, failover); backup and
recovery infrastructure; recovery testing results. Evidence: network architecture diagrams;
BCP/DR documentation; recovery test reports.

### Step 9: Assess DETECT Function (DE)

**DETECT** — Possible cybersecurity attacks and compromises are identified. Two categories:

**DE.CM — Continuous Monitoring** (DE.CM-01 through DE.CM-09): Assess: network monitoring
infrastructure (SIEM, NDR); endpoint detection and response (EDR/XDR) deployment; personnel
activity monitoring for insider threat; external attack surface monitoring; vulnerability
scanning cadence; service provider monitoring; threat intelligence integration; event log
collection and retention. Evidence: SIEM architecture; EDR deployment coverage; log
retention policy; threat intelligence feed contracts.

**⟁ CLARIFY** — Continuous monitoring is the key differentiator for Tier 4 (Adaptive). Before
classifying DE.CM at Tier 3+, confirm:

- Is the SIEM receiving logs from all critical systems (not just selective feeds)?
- Is threat intelligence operationalized (automated blocking rules / playbooks) or just
  informational (read-only reports)?
- What is the MTTD (mean time to detect) and MTTR (mean time to respond) for the last
  12 months?

**DE.AE — Adverse Event Analysis** (DE.AE-01 through DE.AE-08): Assess: baseline of
normal network behavior established and maintained; event correlation across sources;
estimated impact and scope of adverse events; incident information shared with designated
contacts; detection effectiveness metrics. Evidence: SIEM correlation rules; SOC runbook;
incident metrics dashboard; threat hunting records.

### Step 10: Assess RESPOND Function (RS)

**RESPOND** — Actions regarding a detected cybersecurity incident. Four categories:

**RS.MA — Incident Management** (RS.MA-01 through RS.MA-05): Assess: incident response
plan (IRP) existence and currency; incident categorization and triage criteria; incident
escalation paths; legal counsel engagement protocol; executive notification thresholds.
Evidence: IRP document; incident classification matrix; recent tabletop exercise report.

**RS.AN — Incident Analysis** (RS.AN-01 through RS.AN-08): Assess: investigation procedures
(forensic capability or DFIR retainer); root cause analysis process; artifact collection
procedures (chain of custody); malware analysis capability; threat actor attribution approach.
Evidence: DFIR retainer agreement; forensic investigation records; post-incident analysis reports.

**RS.CO — Incident Response Reporting and Communication** (RS.CO-01 through RS.CO-05):
Assess: internal notification procedures; regulatory reporting workflows (aligned to HIPAA
72h, GDPR 72h, SEC 4-day, CIRCIA 72h/24h — as applicable); external communication
(customers, press, law enforcement); information sharing participation (ISAC membership,
CISA reporting). Evidence: notification procedures; regulatory reporting templates; ISAC
membership records.

[JURISDICTION-SPECIFIC] Regulatory notification timelines vary significantly:

- HIPAA: 60 days from discovery to affected individuals; Covered Entity to HHS simultaneous
  or within 60 days; Business Associate to Covered Entity within 60 days
- SEC: 4 business days from materiality determination (Form 8-K Item 1.05)
- NYDFS Part 500: 72 hours to NYDFS
- CIRCIA (critical infrastructure): 72 hours for substantial incidents; 24 hours for
  ransomware payments [VERIFY: CISA rulemaking timeline and final rule effective date]
- NIS2 (EU): 24-hour early warning / 72-hour notification / 1-month final report

**RS.MI — Incident Mitigation** (RS.MI-01 through RS.MI-03): Assess: containment capability
and playbooks; evidence preservation vs. recovery trade-off procedures; vulnerability
remediation process post-incident. Evidence: containment playbooks; post-incident
remediation tracking records.

### Step 11: Assess RECOVER Function (RC)

**RECOVER** — Assets and operations affected by a cybersecurity incident are restored.
Two categories:

**RC.RP — Incident Recovery Plan Execution** (RC.RP-01 through RC.RP-06): Assess: recovery
plan existence, scope, and testing frequency; recovery objectives (RTO/RPO) defined per
system criticality tier; restoration procedures tested against current infrastructure;
lessons learned integration from past recoveries. Evidence: BCP/DR plan; RTO/RPO matrix
by system tier; tabletop and live failover test records.

**RC.CO — Incident Recovery Communication** (RC.CO-01 through RC.CO-04): Assess: public
relations and communications plan for post-incident restoration; stakeholder update
procedures; timeline commitments to affected parties; regulatory post-incident reporting
compliance. Evidence: post-incident communication templates; regulatory reporting checklists.

### Step 12: Cross-Framework Mapping

After completing the function-by-function assessment, generate the cross-framework alignment
matrix using the reference tables in the **Cross-Framework Alignment Matrix** section.

For each cross-framework pair confirmed in Step 3:

1. Identify which CSF subcategories are already met through the existing framework
2. Identify CSF subcategories NOT covered by the existing framework
3. Identify existing-framework requirements NOT addressed by CSF alone (reverse gap)
4. Assign control-ownership tags (who is responsible in the organization for each
   cross-framework control)
5. Export as a GRC platform-compatible table with columns: Framework | Control ID |
   Control Name | CSF Subcategory | Implementation Status | Evidence Reference

### Step 13: Maturity Tier Scoring and Current Profile

Assign a Tier (1–4) to each of the six functions, then determine an overall organizational
tier. Apply the Tier definitions from the **Tier Classification System** section below.

**Aggregation rule**: The organizational overall tier is NOT an average — it is the
lowest-scoring tier across any function, unless the organization explicitly accepts a
lower tier for that function as a risk decision. Document any accepted tier gaps.

**Current Profile output**: A structured record of:

- Per-function tier: GV [Tier], ID [Tier], PR [Tier], DE [Tier], RS [Tier], RC [Tier]
- Evidence basis for each tier assignment
- Key evidence gaps that prevent higher tier assignment
- Confidence score per function tier (use 5-level scale below)

### Step 14: Target Profile and Gap Analysis

**Target Profile development**: Based on the driver from Step 2, the regulatory overlays
from Step 3, and the risk appetite from GV.OC-04, establish a Target Tier per function.

**Important NIST guidance**: Target Tier should reflect the organization's risk context,
not automatically default to Tier 4. A Tier 2 Target may be appropriate for a small
organization with limited regulatory exposure. Tier 4 requires continuous monitoring
infrastructure that is resource-intensive to maintain.

**Gap analysis**: For each subcategory where Current < Target:

1. Classify the gap severity (CRITICAL / HIGH / MEDIUM / LOW — see Gap Severity Framework)
2. Identify the root cause (policy gap / technology gap / people gap / process gap)
3. Estimate remediation effort (person-days and cost range if known)
4. Map to any regulatory obligation triggered by the gap
5. Assign a recommended owner (CISO, IT Operations, HR, Legal, etc.)

**⟁ CLARIFY** — Before finalizing the Target Profile, confirm any tradeoffs:

- Are there functions where accepting a lower target tier is a deliberate risk decision?
- Are there budget or resource constraints that should shape the roadmap timeline?
- Is there an existing project roadmap the security improvements should integrate with?

### Step 15: Generate Implementation Roadmap

Build a POAM (Plan of Action and Milestones) with three prioritization tiers:

**IMMEDIATE (0–30 days)**: CRITICAL gap findings where current tier is Partial (Tier 1)
for controls directly governing regulatory obligations, incident response, or access control.
Includes IG1 CIS Controls not yet implemented. Board must be notified of CRITICAL items.

**NEAR-TERM (30–90 days)**: HIGH gap findings where current tier is Partial or Risk-Informed
for key protective and detection controls. Address before next audit or customer assessment.

**BACKGROUND (90–180 days)**: MEDIUM and LOW gap findings. Formalization and documentation
of existing informal practices. Optimization of implemented controls toward Tier 3.

For each POAM item:

- Specific task (not just "improve access controls" — specific deliverable)
- Named owner (role, not just team)
- Due date
- Resource requirement (estimated)
- Success metric (verifiable evidence of remediation)
- Cross-framework requirement triggered (if any)
- Dependency on prior POAM items

### Step 16: Quality Verification

Before delivering the assessment report, run all quality checks silently.

**Citation Quality Gates** (5 gates — see full section below): Run for every CSF
subcategory reference, regulatory citation, and cross-framework mapping.

**Self-Interrogation** (3-pass — see full section below): Apply to every CRITICAL gap
finding and any Tier 1 (Partial) function assessment.

**Confidence Scoring** (5-level — see full section below): Apply to every tier assignment.

**Internal consistency check**:

- Does every CRITICAL POAM item have an IMMEDIATE timeline?
- Does every regulatory gap have a regulatory reference in the finding?
- Does the Overall Tier match the lowest per-function tier?
- Are all cross-framework gaps documented in both the CSF and the target framework columns?

### Step 17: Generate Assessment Report

Produce the full assessment output following the **Output Format Template** below.

---

## NIST CSF 2.0 Reference Structure

Complete function and category structure. All subcategory codes and counts are from
NIST CSWP 29 (February 2024) — verify against current CPRT for authoritative subcategory
details.

| Function          | Category Code | Category Name                                           | Subcategory Count      |
| ----------------- | ------------- | ------------------------------------------------------- | ---------------------- |
| **GOVERN (GV)**   | GV.OC         | Organizational Context                                  | 5                      |
|                   | GV.RM         | Risk Management Strategy                                | 7                      |
|                   | GV.RR         | Roles, Responsibilities, and Authorities                | 4                      |
|                   | GV.PO         | Policy                                                  | 2                      |
|                   | GV.OV         | Oversight                                               | 3                      |
|                   | GV.SC         | Cybersecurity Supply Chain Risk Management              | 10                     |
| **IDENTIFY (ID)** | ID.AM         | Asset Management                                        | 8                      |
|                   | ID.RA         | Risk Assessment                                         | 10                     |
|                   | ID.IM         | Improvement (NEW in 2.0)                                | 4                      |
| **PROTECT (PR)**  | PR.AA         | Identity Management, Authentication, and Access Control | 6                      |
|                   | PR.AT         | Awareness and Training                                  | 2                      |
|                   | PR.DS         | Data Security                                           | 11                     |
|                   | PR.PS         | Platform Security                                       | 6                      |
|                   | PR.IR         | Technology Infrastructure Resilience                    | 4                      |
| **DETECT (DE)**   | DE.CM         | Continuous Monitoring                                   | 9                      |
|                   | DE.AE         | Adverse Event Analysis                                  | 8                      |
| **RESPOND (RS)**  | RS.MA         | Incident Management                                     | 5                      |
|                   | RS.AN         | Incident Analysis                                       | 8                      |
|                   | RS.CO         | Incident Response Reporting and Communication           | 5                      |
|                   | RS.MI         | Incident Mitigation                                     | 3                      |
| **RECOVER (RC)**  | RC.RP         | Incident Recovery Plan Execution                        | 6                      |
|                   | RC.CO         | Incident Recovery Communication                         | 4                      |
| **TOTALS**        |               | **22 categories**                                       | **~106 subcategories** |

**Key CSF 2.0 changes from CSF 1.1**:

- GOVERN function added (new sixth function; governance formerly in ID.GV)
- GV.SC (Supply Chain) is entirely new — 10 subcategories, the largest single category
- ID.IM (Improvement) consolidates improvement activities from RC.IM and other functions
- IDENTIFY reduced from 6 to 3 categories (ID.BE, ID.GV merged into GV)
- DETECT reduced from 5 to 2 categories (DE.DP merged into DE.CM)
- RESPOND and RECOVER each reduced by one improvement category → ID.IM
- Implementation Examples added as a new non-normative layer beneath subcategories
- Informative references moved from the PDF to the online CPRT (csrc.nist.gov/projects/cprt)

---

## Cross-Framework Alignment Matrix

The tables below reflect key mapping relationships. These are derived from official NIST
OLIR catalog entries, AICPA TSC crosswalk, CIS mapping publications, and ISACA COBIT
publications. **[VERIFY all mappings against current authoritative sources before use in
compliance reporting.]**

### CSF 2.0 ↔ ISO 27001:2022 Key Mappings

Overall overlap: ISO 27001:2022 covers ~83% of CSF 2.0 requirements; CSF 2.0 covers
~61% of ISO 27001:2022 requirements. Primary gap areas: GOVERN function governance
dimensions (GV.RM risk appetite, GV.OV oversight) not fully addressed by ISO 27001
clause requirements.

| CSF 2.0 Function | CSF Category | ISO 27001:2022 Annex A Controls                                                                                              |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| GOVERN           | GV.OC        | A.5.4 (Management responsibilities), A.5.19 (Supplier info security)                                                         |
| GOVERN           | GV.RM        | A.5.3 (Segregation of duties), A.8.2 (Privileged access rights)                                                              |
| GOVERN           | GV.RR        | A.5.2 (Info security roles and responsibilities), A.5.4 (Mgmt resp.)                                                         |
| GOVERN           | GV.PO        | A.5.1 (Policies for information security)                                                                                    |
| GOVERN           | GV.SC        | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 (Supplier relationship controls)                                                      |
| IDENTIFY         | ID.AM        | A.5.9 (Asset inventory), A.5.10 (Acceptable use), A.5.11 (Return of assets), A.5.12 (Classification)                         |
| IDENTIFY         | ID.RA        | A.5.24 (Incident management planning), A.8.8 (Technical vulnerability mgmt.)                                                 |
| PROTECT          | PR.AA        | A.5.15 (Access control), A.5.16 (Identity mgmt.), A.5.17 (Authentication), A.5.18 (Access rights), A.8.2 (Privileged access) |
| PROTECT          | PR.AT        | A.6.3 (Information security awareness, education, training)                                                                  |
| PROTECT          | PR.DS        | A.5.33 (Protection of records), A.8.10–A.8.12 (Deletion, masking, DLP)                                                       |
| PROTECT          | PR.PS        | A.8.8 (Vulnerability mgmt.), A.8.9 (Configuration mgmt.)                                                                     |
| DETECT           | DE.CM        | A.8.15 (Logging), A.8.16 (Monitoring activities)                                                                             |
| DETECT           | DE.AE        | A.5.25 (Assessment of IS events), A.5.26 (Response to IS incidents)                                                          |
| RESPOND          | RS.MA        | A.5.24 (IS incident management planning), A.5.26 (Response)                                                                  |
| RESPOND          | RS.CO        | A.5.29 (Info security during disruption), A.5.5 (Contacts with authorities)                                                  |
| RECOVER          | RC.RP        | A.5.29 (Info security during disruption), A.5.30 (ICT readiness for BCP)                                                     |

### CSF 2.0 ↔ SOC 2 Trust Services Criteria Key Mappings

[VERIFY: AICPA mapping published for CSF v1.1 / 2017 TSC; a CSF 2.0–specific update
may exist. The GOVERN function mapping below reflects structural alignment, not an
official AICPA publication.]

| CSF 2.0 Function | CSF Category        | SOC 2 Trust Services Criteria                                                                        |
| ---------------- | ------------------- | ---------------------------------------------------------------------------------------------------- |
| GOVERN           | GV.OC, GV.RM, GV.PO | CC1 (Control Environment: CC1.1–CC1.5), CC3 (Risk Assessment: CC3.1–CC3.4)                           |
| GOVERN           | GV.RR               | CC1.2 (Board oversight), CC1.3 (Org. structure, reporting lines)                                     |
| IDENTIFY         | ID.AM               | CC6.1 (Logical access security), A1.1 (Capacity planning)                                            |
| IDENTIFY         | ID.RA               | CC3.1 (Risk assessment), CC3.2 (Fraud risk), CC3.3 (Regulatory requirements)                         |
| PROTECT          | PR.AA               | CC6.1 (Logical access), CC6.2 (Authentication), CC6.3 (Access provisioning), CC6.6 (External access) |
| PROTECT          | PR.AT               | CC1.4 (Commitment to competence), CC2.2 (Internal communication)                                     |
| PROTECT          | PR.DS               | C1.1–C1.2 (Confidentiality criteria), CC6.7 (Data in transit)                                        |
| PROTECT          | PR.PS               | CC7.1 (Vulnerability detection), CC8.1 (Change management)                                           |
| DETECT           | DE.CM               | CC7.1 (Detect configuration deviations), CC7.2 (Monitor anomalous activity)                          |
| DETECT           | DE.AE               | CC7.3 (Evaluate security events), CC7.4 (Respond to incidents)                                       |
| RESPOND          | RS.MA, RS.AN        | CC7.4 (Respond to incidents), CC7.5 (Communicate breaches)                                           |
| RESPOND          | RS.CO               | CC2.3 (External communication), CC7.5 (Communicate breaches)                                         |
| RECOVER          | RC.RP               | A1.2 (Availability backup), A1.3 (Recovery testing)                                                  |
| RECOVER          | RC.CO               | CC2.3 (Communication with external parties)                                                          |

### CSF 2.0 ↔ CIS Controls v8 Key Mappings

CIS Controls are more prescriptive (the "how"); CSF 2.0 is outcome-focused (the "what").
IG1 (56 safeguards) corresponds approximately to Tier 2 outcomes for foundational controls.
Full IG3 (all 153 safeguards) corresponds approximately to Tier 3–4 overall posture.

| CSF 2.0 Function | CSF Category        | CIS Controls v8                                                                                                                                                                |
| ---------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GOVERN           | GV.SC               | CIS 15 (Service Provider Management) — entire control                                                                                                                          |
| IDENTIFY         | ID.AM               | CIS 1 (Enterprise Asset Inventory), CIS 2 (Software Asset Inventory)                                                                                                           |
| IDENTIFY         | ID.RA               | CIS 7 (Vulnerability Management — identification dimension), CIS 18 (Penetration Testing)                                                                                      |
| PROTECT          | PR.AA               | CIS 5 (Account Management), CIS 6 (Access Control Management)                                                                                                                  |
| PROTECT          | PR.AT               | CIS 14 (Security Awareness and Skills Training)                                                                                                                                |
| PROTECT          | PR.DS               | CIS 3 (Data Protection)                                                                                                                                                        |
| PROTECT          | PR.PS               | CIS 4 (Secure Configuration), CIS 9 (Email and Web Protections), CIS 10 (Malware Defenses), CIS 12 (Network Infrastructure Management), CIS 16 (Application Software Security) |
| PROTECT          | PR.IR               | CIS 11 (Data Recovery)                                                                                                                                                         |
| DETECT           | DE.CM               | CIS 7 (Vulnerability Management), CIS 8 (Audit Log Management), CIS 13 (Network Monitoring and Defense)                                                                        |
| DETECT           | DE.AE               | CIS 8 (Audit Log Management), CIS 13 (Network Monitoring)                                                                                                                      |
| RESPOND          | RS.MA, RS.AN, RS.MI | CIS 17 (Incident Response Management)                                                                                                                                          |
| RECOVER          | RC.RP               | CIS 11 (Data Recovery)                                                                                                                                                         |

### CSF 2.0 ↔ CMMC 2.0 Key Mappings

CMMC 2.0 Level 2 = all 110 practices from NIST SP 800-171 Rev 2. Level 3 adds 24+
practices from NIST SP 800-172. CSF is used as a planning and risk management overlay;
formal CMMC certification requires a C3PAO third-party assessment (Level 2) or
government-led assessment (Level 3).

| CSF 2.0 Function | CSF Category | CMMC 2.0 / NIST SP 800-171 Domain                                                              |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------- |
| GOVERN           | GV.SC        | SR (Supply Chain Risk Management) domain — SP 800-171 Rev 3                                    |
| IDENTIFY         | ID.AM        | CM (Configuration Management): CM.L1-3.4.1–CM.L2-3.4.2                                         |
| IDENTIFY         | ID.RA        | RA (Risk Assessment): RA.L2-3.11.1–RA.L2-3.11.3                                                |
| PROTECT          | PR.AA        | AC (Access Control): AC.L1-3.1.1–AC.L1-3.1.2 (Level 1 foundational), AC.L2-3.1.3+ (Level 2)    |
| PROTECT          | PR.AT        | AT (Awareness and Training): AT.L2-3.2.1–AT.L2-3.2.2                                           |
| PROTECT          | PR.DS        | MP (Media Protection): MP.L1-3.8.3–MP.L2-3.8.9                                                 |
| PROTECT          | PR.PS        | CM (Configuration Mgmt.) + SI (System and Info Integrity): SI.L1-3.14.1–SI.L2-3.14.7           |
| DETECT           | DE.CM        | AU (Audit and Accountability): AU.L2-3.3.1–AU.L2-3.3.9; CA (Security Assessment): CA.L2-3.12.4 |
| RESPOND          | RS.MA        | IR (Incident Response): IR.L2-3.6.1–IR.L2-3.6.3                                                |
| RECOVER          | RC.RP        | IR domain recovery elements + CA security assessment recovery elements                         |

### CSF 2.0 ↔ COBIT 2019 Key Mappings

COBIT 2019 provides governance and management objectives (the "how"); CSF defines
outcomes (the "what"). COBIT's capability levels (0–5) provide additional measurement
beyond CSF Tiers 1–4.

| CSF 2.0 Function | CSF Category | COBIT 2019 Domain/Objective                                                           |
| ---------------- | ------------ | ------------------------------------------------------------------------------------- |
| GOVERN           | GV (overall) | EDM03 (Ensure Risk Optimization), EDM01 (Ensure Governance Framework)                 |
| GOVERN           | GV.OC        | EDM01.01, APO02 (Manage Strategy)                                                     |
| GOVERN           | GV.RM        | EDM03.01, APO12.01–APO12.04 (Risk management)                                         |
| GOVERN           | GV.RR        | APO01 (Manage IT Management Framework), EDM01.02                                      |
| GOVERN           | GV.SC        | APO10 (Manage Suppliers), DSS06 (Manage Business Process Controls)                    |
| IDENTIFY         | ID.AM        | APO03 (Manage Enterprise Architecture), BAI09 (Manage Assets)                         |
| IDENTIFY         | ID.RA        | APO12.02 (Analyze risk), APO12.03 (Maintain risk profile)                             |
| PROTECT          | PR.AA        | DSS05.04 (Manage user identity and logical access), DSS05.05 (Manage physical access) |
| PROTECT          | PR.DS        | APO14 (Manage Data), DSS05.02 (Manage network security)                               |
| PROTECT          | PR.PS        | DSS05.03 (Manage endpoint security), BAI10 (Manage Configuration)                     |
| DETECT           | DE.CM        | DSS05.07 (Monitor infrastructure for security events), MEA01 (Monitor Performance)    |
| DETECT           | DE.AE        | DSS02 (Manage Service Requests and Incidents), MEA02 (Manage Internal Control)        |
| RESPOND          | RS.MA        | DSS02 (Manage Incidents), DSS03 (Manage Problems)                                     |
| RECOVER          | RC.RP        | DSS04 (Manage Continuity)                                                             |

---

## Tier Classification System

NIST CSF 2.0 Tiers describe the rigor of an organization's cybersecurity risk governance
and management practices. **Tiers are NOT compliance grades, certification levels, or
performance scores.** The appropriate target tier depends on the organization's risk
context, sector, regulatory obligations, and budget — not every organization should
target Tier 4.

Tiers assess three dimensions:

1. **Risk Management Process**: From informal and reactive (Tier 1) to adaptive and
   dynamic (Tier 4)
2. **Integrated Risk Management Program**: From no organization-wide awareness (Tier 1)
   to fully integrated with enterprise risk management (Tier 4)
3. **External Participation**: From no external sharing (Tier 1) to active threat
   intelligence sharing and community contribution (Tier 4)

| Tier  | Name              | Risk Mgmt. Process                                                                                                                             | Integrated Risk Mgmt.                                                                                            | External Participation                                                                            | Typical Evidence                                                                                                                                                                                                        |
| ----- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Partial**       | Ad hoc, reactive. No organization-wide policy. Risk responses not coordinated.                                                                 | No awareness. No enterprise risk category.                                                                       | No external sharing.                                                                              | No written security policy; incident response is improvised; no formal asset inventory.                                                                                                                                 |
| **2** | **Risk-Informed** | Risk management practices approved by leadership but not established as organization-wide policy. Awareness exists but inconsistently applied. | Leadership aware of cyber risk. Not integrated with ERM.                                                         | Informal sharing. No formalized process.                                                          | Security policy exists but inconsistently enforced; basic vulnerability scanning; informal incident handling.                                                                                                           |
| **3** | **Repeatable**    | Formally approved organizational policy. Practices consistently applied across the organization. Communicated via established processes.       | Integrated into overall enterprise risk management. Senior executives communicate risk through the organization. | Formalized sharing. Receives and shares threat intelligence. Participates in coordination bodies. | Mature policies enforced; formal ISMS; vulnerability management with SLAs; formal IRP with regular tabletop exercises; ISAC participation.                                                                              |
| **4** | **Adaptive**      | Continuously improving based on previous and current cybersecurity activities. Incorporates lessons learned and predictive indicators.         | Risk management practices integrated into organizational culture.                                                | Active sharing of threat intelligence. Receives and contributes to community threat data.         | Continuous monitoring (SIEM + threat intel feeds + automated response); board-level cybersecurity metrics; red team exercises; contribution to threat intel sharing (ISACs, CISA); formal maturity improvement program. |

**Per-function tier classification rule**: Assign each function the tier that best describes
the current maturity of governance, management process, and external engagement for that
function's domain. Apply the weakest-evidence rule: if any key control within the function
is clearly Tier 1, the function cannot exceed Tier 2 overall without documented compensating
controls.

---

## Gap Severity Framework

Use this framework to classify individual control gaps (subcategory-level) found during
the assessment. This is distinct from the overall Tier — a function can be Tier 2 overall
but contain individual CRITICAL gaps.

| Severity     | Description                                                                                                                                                                                                    | Regulatory Trigger                                        | POAM Priority                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------- |
| **CRITICAL** | Absence of control creates immediate regulatory exposure, is likely to be detected in an external audit, or creates direct operational risk (e.g., no MFA on privileged accounts, no IRP, no asset inventory). | Likely triggers regulatory finding or customer breach.    | IMMEDIATE (0–30 days)             |
| **HIGH**     | Control exists informally or partially; significant documentation or enforcement gap; required for Tier 2+ in the function.                                                                                    | Regulatory examiner likely to note.                       | NEAR-TERM (30–90 days)            |
| **MEDIUM**   | Control exists and is partially effective; improvement needed to achieve target tier.                                                                                                                          | May be noted by examiner as best-practice recommendation. | BACKGROUND (90–180 days)          |
| **LOW**      | Control largely meets requirements; minor gaps in documentation, coverage, or optimization.                                                                                                                    | Unlikely to be noted; continuous improvement.             | Accept or schedule in next cycle. |

---

## Prioritization Framework

For remediation planning, map gap severity to implementation priority:

| Finding Severity | Implementation Tier  | Timeline    | Board Notification                |
| ---------------- | -------------------- | ----------- | --------------------------------- |
| CRITICAL         | IMMEDIATE            | 0–30 days   | Required                          |
| HIGH             | NEAR-TERM            | 30–90 days  | Recommended                       |
| MEDIUM           | BACKGROUND           | 90–180 days | Optional (at next board briefing) |
| LOW              | Accept or next cycle | 180+ days   | Not required                      |

**Top-3 priority rule**: Always identify the three highest-severity gaps across all functions
and present them as the "Top 3 Priority Actions" in the executive summary. These must have
named owners and specific due dates.

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
the affected finding before delivering.

| Gate           | Rule                                                                                                                                                                                                                    | Fail Action                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Source**     | Every CSF claim cites a specific function, category, subcategory code (e.g., GV.SC-01), or NIST document number. Every regulatory claim cites the specific provision (e.g., 45 C.F.R. § 164.312(a)(1)).                 | Add citation or mark [UNVERIFIED — verify against NIST CPRT or regulatory text]. |
| **Format**     | All CSF citations use the standard format: Function-Category-Subcategory (e.g., PR.AA-02). All regulatory citations use jurisdiction-standard format.                                                                   | Fix format inconsistencies.                                                      |
| **Currency**   | NIST CSF 2.0 (February 2024, CSWP 29) is the current version. Flag any CSF 1.1 subcategory codes that no longer exist in 2.0. Flag regulatory provisions that may have been amended after the current date.             | Mark [CSF 1.1 REFERENCE — verify against CSF 2.0] or [CHECK CURRENCY].           |
| **Domain**     | Cross-framework claims are labeled with the target framework (e.g., "[ISO 27001]" or "[SOC 2]"). Regulatory overlay claims are labeled with the regulation ("[HIPAA]", "[GLBA]"). No unmarked bleed between frameworks. | Add framework label or remove claim.                                             |
| **Confidence** | Any interpretive uncertainty (especially for GOVERN function interpretations, pre-enforcement regulatory readings, or cross-framework equivalence claims) is explicitly stated with a confidence qualifier.             | Add confidence qualifier or [VERIFY].                                            |

---

## Self-Interrogation

For every finding classified as CRITICAL severity or any function assessed at Tier 1
(Partial), apply this three-pass adversarial review before finalizing the classification.

**Pass 1 — Evidence Integrity**: Is the CRITICAL / Tier 1 classification supported by
concrete evidence of absence, or by assumed absence? Did the assessment actually verify
that the control does not exist, or merely that no documentation was provided? What evidence
would be needed to upgrade the classification to HIGH or Tier 2?

**Pass 2 — Completeness**: Have all compensating controls been considered? Could a control
in an adjacent subcategory provide partial coverage? Are there regulatory safe harbors or
flexibility provisions that reduce the severity? Have sector-specific implementation
examples from the CPRT been reviewed for the subcategory?

**Pass 3 — Challenge**: What is the strongest argument that this gap is already addressed,
or that the current tier is higher than assessed? What would a qualified assessor finding
this same evidence conclude? Document the strongest counter-argument in the finding, and
confirm that the classification withstands it.

**Output of self-interrogation**: A brief note in the finding record: "Self-interrogation
PASS" (classification confirmed) or "Self-interrogation REVISED — [basis for revision]."

---

## Confidence Scoring

Assign a confidence score to every tier classification and every cross-framework mapping
equivalence claim.

| Level        | Range     | Meaning                                                                                                                                          | Action                                             |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| **Definite** | 0.95–1.0  | Evidence conclusively supports classification. Official NIST or regulatory source directly confirms the mapping.                                 | State with confidence.                             |
| **High**     | 0.80–0.94 | Strong evidence supports classification; minor interpretation questions. Official crosswalk table exists but may be for prior framework version. | State with brief caveat.                           |
| **Probable** | 0.60–0.79 | Good evidence but reasonable practitioners could reach different conclusions. Crosswalk is derived from secondary sources.                       | State with explicit reasoning and [VERIFY] marker. |
| **Possible** | 0.40–0.59 | Genuinely uncertain; evidence is incomplete or conflicting.                                                                                      | Flag for professional review; present both sides.  |
| **Unlikely** | 0.0–0.39  | Weak or speculative basis; insufficient evidence for classification.                                                                             | Do not assert; flag [UNCERTAIN].                   |

---

## Anti-Patterns for NIST CSF Mapping

What NOT to do when assessing or implementing NIST CSF 2.0 compliance:

**Governance and Executive Errors:**

1. **CISO-only GOVERN function**: Treating GV as the CISO's responsibility alone rather
   than a board and executive leadership obligation. GV.RR-01 requires organizational
   leadership accountability; CISO-only implementation is a CRITICAL gap in GV.

2. **No risk appetite statement**: Developing a Target Profile without a documented,
   leadership-approved risk appetite and risk tolerance statement (GV.OC-04, GV.RM).
   Target Tier selection becomes arbitrary without this anchor.

3. **Governance gap between GOVERN and execution**: Completing GV policy documentation
   without translating policy into operational controls in PR, DE, and RS. Policy documents
   are not evidence of controls implemented.

4. **CSF treated as IT compliance only**: Implementing CSF within the IT/security team
   in isolation from legal, HR, finance, operations, and supply chain. GOVERN function
   explicitly requires organizational context across all business functions.

5. **Ignoring GV.SC entirely**: Treating supply chain risk management as optional or
   deferring it to a future phase. GV.SC is the largest single category in CSF 2.0 (10
   subcategories); GOVERN without supply chain is fundamentally incomplete.

**Tier Assessment Methodology Errors:**

6. **Confusing Tiers with scores or certifications**: Treating Tier 4 as the mandatory
   target for all organizations. Tiers characterize governance maturity relative to risk
   context — a Tier 2 Target may be appropriate and defensible for a small, low-risk entity.

7. **Self-assessment inflation**: Over-rating maturity during self-assessments to present
   favorable results to leadership or customers. Without independent validation, inflated
   tier claims create false assurance.

8. **Assessing policies rather than practice**: Evaluating whether a policy document exists
   rather than whether it is consistently enforced. The distinction between documented and
   implemented controls is fundamental to meaningful tier assessment.

9. **No baseline before remediation**: Starting remediation without first establishing
   a documented Current Profile baseline, making it impossible to measure improvement
   or demonstrate compliance progress over time.

10. **Treating all 106 subcategories as equally required**: Failing to tailor the
    assessment scope to organizational risk context. Not all subcategories are equally
    critical for every organization; proportionality is built into the framework.

11. **Scoring subcategories without principled aggregation**: Summing subcategory scores
    into an overall "CSF percentage score" without a documented aggregation methodology,
    producing misleading results that obscure critical gaps in specific functions.

**Cross-Framework Mapping Errors:**

12. **Assuming ISO 27001 certification fully satisfies CSF**: ISO 27001 covers approximately
    83% of CSF 2.0 requirements. The remaining 17% — concentrated in GV.RM risk appetite,
    GV.OV oversight, and GV.SC supply chain governance — may be uncovered and material.

13. **Stale mapping tables**: Using CSF 1.1 crosswalk mappings (e.g., AICPA TSC v1.1
    mapping) without verifying applicability to CSF 2.0. The GOVERN function was added in
    2.0; any v1.1 mapping has a structural gap for the entire GV function.

14. **One-directional mapping only**: Mapping FROM CSF TO another framework without also
    performing the reverse mapping. Approximately 39% of ISO 27001:2022 requirements are
    not fully covered by CSF alignment; the reverse gap is as important as the forward gap.

15. **Framework proliferation without control harmonization**: Maintaining separate compliance
    programs for NIST CSF, ISO 27001, SOC 2, and CMMC with no unified control library.
    This creates duplicated evidence, inconsistent positions, and audit fatigue.

**Implementation Execution Errors:**

16. **Tool proliferation as tier advancement**: Purchasing additional security tools without
    improving governance maturity. Tier advancement requires governance rigor and consistency —
    not more technology. Organizations can be at Tier 1 with extensive tooling if those tools
    are not governed.

17. **No POAM ownership**: Assigning remediation tasks to teams rather than named individuals.
    Without individual accountability, remediation tasks stall and timelines slip.

18. **Scope creep on first iteration**: Attempting to address all 106 subcategories simultaneously
    rather than using a phased, risk-prioritized approach. Start with CRITICAL gaps and IG1
    foundational controls.

19. **No integration with IT project pipeline**: Creating a security remediation roadmap
    that is not integrated with the IT capital planning and project portfolio. Security
    improvements compete with and lose to business capability projects when they are not
    formally in the portfolio.

20. **Ignoring the POAM as a living document**: Treating the Plan of Action and Milestones
    as a static artifact rather than a continuously updated tracking tool. POAMs must be
    reviewed at minimum quarterly and updated as items are completed or circumstances change.

**Regulatory Alignment Errors:**

21. **Assuming CSF satisfies regulatory compliance**: NIST CSF is a risk management
    framework, not a compliance standard. CSF alignment does not substitute for HIPAA
    Security Rule compliance, CMMC certification, SEC disclosure obligations, or state-law
    requirements. Use CSF as a planning tool, then verify regulatory requirements separately.

22. **No legal review of regulatory overlay gaps**: Treating CSF regulatory overlay mapping
    as purely technical without legal analysis of enforcement risk, regulatory examiner
    expectations, or penalty exposure. HIPAA OCR, FTC, SEC, and state regulators have
    independently developed examination frameworks that go beyond CSF.

---

## Writing Standards

Before delivering any assessment output, verify these writing quality gates:

1. **Specificity over vagueness**: Every gap finding must specify which subcategory is
   deficient, what evidence was reviewed, and what specific improvement is needed. Not
   "improve access controls" — "PR.AA-01: No evidence of formal identity provisioning
   and de-provisioning process. Required: documented joiner/mover/leaver workflow with
   approval records. Owner: IT Operations. Due: 60 days."

2. **Evidence basis always stated**: Every tier classification must reference the evidence
   reviewed (or the evidence gap). Not "Tier 2 overall" — "Tier 2: Security policy
   exists (reviewed) and is approved by CISO (confirmed), but is not consistently enforced
   across all business units (3 of 5 business units audited had no policy acknowledgment
   records)."

3. **Regulatory citations complete**: Every regulatory reference must include the specific
   provision number, not just the regulation name. Not "HIPAA requires access controls" —
   "45 C.F.R. § 164.312(a)(1) (Technical Safeguards: Access Control standard) requires
   unique user identification (§ 164.312(a)(2)(i)), emergency access procedure
   (§ 164.312(a)(2)(ii)), and automatic logoff (§ 164.312(a)(2)(iii)) as implementation
   specifications."

4. **Owner always named**: Every POAM item must have a named owner (role, not team). Not
   "IT team" — "CISO" or "Director of IT Operations" or "VP of Legal" as appropriate.

5. **Success metric always defined**: Every POAM item must have a verifiable success metric.
   Not "implement MFA" — "MFA enrollment rate ≥ 95% for all user accounts; 100% for
   privileged accounts; verified via quarterly access review report."

6. **Confidence markers used consistently**: Every uncertain claim carries [VERIFY], and
   every cross-framework equivalence claim below Definite confidence carries a confidence
   qualifier.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** for legal authority verification.

**With legalcode-mcp connected:**

- Search for current NIST CSWP 29 subcategory definitions and informative references
- Verify current FISMA, HIPAA, GLBA, and SEC rule text for regulatory overlay claims
- Search for current CISA BOD requirements aligned to CSF functions
- Save reference data to `/tmp/nist-csf-mapping-research-[date].md`

**Without legalcode-mcp:**

- Proceed using built-in cross-framework tables above
- Mark all regulatory provisions with [VERIFY]
- Direct users to NIST CPRT (`csrc.nist.gov/projects/cprt`) for authoritative subcategory
  data and informative references
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

**GRC Platform Export**: For GRC tool import, generate the POAM as a structured table
with columns compatible with the target platform:

- **ServiceNow GRC**: Control → Policy → Risk → Remediation Task hierarchy
- **OneTrust**: Framework → Control → Evidence → Task format
- **Archer**: Application → Record → Field structure
- **Generic CSV**: Framework | Control ID | Control Name | CSF Subcategory | Current Status |
  Target Status | Gap | Severity | Owner | Due Date | Success Metric | Evidence Reference

---

## Output Format Template

````markdown
# NIST CSF 2.0 Maturity Assessment — [Organization Name]

**Assessment Date**: [YYYY-MM-DD]
**Assessor**: [Name/Role]
**Organization**: [Full legal name]
**Sector**: [Healthcare / Finance / Defense / Technology / Energy / Government / Other]
**Organization Size**: [Small / Medium / Large]
**Geographic Scope**: [US-only / US + EU / Global]
**Assessment Driver**: [Internal governance / Third-party requirement / Regulatory / Other]
**Existing Frameworks**: [ISO 27001:2022 (certified) / SOC 2 / CIS Controls / None / Other]
**Regulatory Overlays Assessed**: [HIPAA / GLBA / SEC / FISMA / NYDFS / NIS2 / None]
**Assessment Scope**: [Full (all 6 functions) / Prioritized functions / Cross-framework mapping only]

---

## Executive Summary

**Current Organizational Tier**: [Partial (1) / Risk-Informed (2) / Repeatable (3) / Adaptive (4)]
**Summary**: [2–3 sentences: overall posture, most material gaps, recommended priority actions]

### Per-Function Tier Dashboard

| Function          | Current Tier | Target Tier | Delta | Critical Gaps | Priority   |
| ----------------- | ------------ | ----------- | ----- | ------------- | ---------- |
| **Govern (GV)**   | [Tier 1–4]   | [Tier 1–4]  | [+N]  | [Count]       | [P1/P2/P3] |
| **Identify (ID)** | [Tier 1–4]   | [Tier 1–4]  | [+N]  | [Count]       | [P1/P2/P3] |
| **Protect (PR)**  | [Tier 1–4]   | [Tier 1–4]  | [+N]  | [Count]       | [P1/P2/P3] |
| **Detect (DE)**   | [Tier 1–4]   | [Tier 1–4]  | [+N]  | [Count]       | [P1/P2/P3] |
| **Respond (RS)**  | [Tier 1–4]   | [Tier 1–4]  | [+N]  | [Count]       | [P1/P2/P3] |
| **Recover (RC)**  | [Tier 1–4]   | [Tier 1–4]  | [+N]  | [Count]       | [P1/P2/P3] |

### Gap Summary

| Severity    | Count | Priority                 |
| ----------- | ----- | ------------------------ |
| 🚨 CRITICAL | [N]   | IMMEDIATE (0–30 days)    |
| 🔴 HIGH     | [N]   | NEAR-TERM (30–90 days)   |
| 🟡 MEDIUM   | [N]   | BACKGROUND (90–180 days) |
| 🟢 LOW      | [N]   | Accept or next cycle     |

### Top 3 Priority Actions

1. **[Function]-[Category]: [Specific gap]** — Action: [Specific deliverable]
   Owner: [Named role] | Due: [Date] | Regulatory trigger: [If applicable]
2. **[Function]-[Category]: [Specific gap]** — Action: [Specific deliverable]
   Owner: [Named role] | Due: [Date] | Regulatory trigger: [If applicable]
3. **[Function]-[Category]: [Specific gap]** — Action: [Specific deliverable]
   Owner: [Named role] | Due: [Date] | Regulatory trigger: [If applicable]

---

## Applicable Framework and Regulatory Context

| Element                       | Reference                                                  | Applicability                         |
| ----------------------------- | ---------------------------------------------------------- | ------------------------------------- |
| Primary Framework             | NIST Cybersecurity Framework 2.0 (NIST CSWP 29, Feb. 2024) | Full                                  |
| Technical Control Reference   | NIST SP 800-53 Rev 5 / NIST CPRT Informative References    | Informative                           |
| Regulatory Overlay 1          | [HIPAA / GLBA / SEC / FISMA / NYDFS / NIS2 / None]         | [Mandatory / Voluntary]               |
| Cross-Framework: ISO 27001    | [Version / Certification status]                           | [Certified / Implementing / Gap only] |
| Cross-Framework: SOC 2        | [Report status / Period]                                   | [Current / Expired / Not assessed]    |
| Cross-Framework: CIS Controls | [IG level targeted]                                        | [IG1 / IG2 / IG3]                     |
| Cross-Framework: CMMC         | [Level / Phase]                                            | [Level 1–3 / Self-assess / C3PAO]     |

---

## Function Assessments

### Govern (GV) — [Current Tier N / Target Tier N]

**Confidence**: [Definite / High / Probable / Possible]
**Overall classification**: [Partial / Risk-Informed / Repeatable / Adaptive]
**Self-interrogation**: [PASS / REVISED — reason]

| Category | Subcategory                       | Current State   | Gap Severity            | Recommended Action | Owner  | Deadline |
| -------- | --------------------------------- | --------------- | ----------------------- | ------------------ | ------ | -------- |
| GV.OC    | GV.OC-01 (Mission/objectives)     | [Current state] | [CRITICAL/HIGH/MED/LOW] | [Specific action]  | [Role] | [Date]   |
| GV.OC    | GV.OC-02 (Regulatory obligations) | [Current state] | [Severity]              | [Action]           | [Role] | [Date]   |
| GV.OC    | GV.OC-03 (Business environment)   | [Current state] | [Severity]              | [Action]           | [Role] | [Date]   |
| GV.OC    | GV.OC-04 (Risk tolerance)         | [Current state] | [Severity]              | [Action]           | [Role] | [Date]   |
| GV.OC    | GV.OC-05 (Supplier dependencies)  | [Current state] | [Severity]              | [Action]           | [Role] | [Date]   |
| GV.RM    | GV.RM-01 through GV.RM-07         | [Summary]       | [Worst-case severity]   | [Key action]       | [Role] | [Date]   |
| GV.RR    | GV.RR-01 through GV.RR-04         | [Summary]       | [Worst-case severity]   | [Key action]       | [Role] | [Date]   |
| GV.PO    | GV.PO-01 through GV.PO-02         | [Summary]       | [Severity]              | [Key action]       | [Role] | [Date]   |
| GV.OV    | GV.OV-01 through GV.OV-03         | [Summary]       | [Severity]              | [Key action]       | [Role] | [Date]   |
| GV.SC    | GV.SC-01 through GV.SC-10         | [Summary]       | [Worst-case severity]   | [Key action]       | [Role] | [Date]   |

[Repeat structure for ID, PR, DE, RS, RC functions]

---

## Cross-Framework Alignment Matrix

### [CSF 2.0 ↔ ISO 27001:2022] (if applicable)

| CSF 2.0 Subcategory | CSF Status        | ISO 27001:2022 Control     | ISO Status        | Gap Direction                     | Notes    |
| ------------------- | ----------------- | -------------------------- | ----------------- | --------------------------------- | -------- |
| GV.PO-01            | [Compliant / Gap] | A.5.1 (Policies)           | [Certified / Gap] | [CSF→ISO / ISO→CSF / Both / None] | [VERIFY] |
| GV.SC-01            | [Compliant / Gap] | A.5.19 (Supplier security) | [Status]          | [Direction]                       |          |
| PR.AA-02            | [Compliant / Gap] | A.5.16 (Identity mgmt.)    | [Status]          | [Direction]                       |          |

[Repeat for each confirmed cross-framework pair]

---

## POAM (Plan of Action and Milestones)

### IMMEDIATE Tier (0–30 days) — CRITICAL Gaps

| ID  | Gap               | CSF Subcategory | Regulatory Trigger | Specific Task          | Owner        | Due Date | Success Metric      | Evidence        | Status |
| --- | ----------------- | --------------- | ------------------ | ---------------------- | ------------ | -------- | ------------------- | --------------- | ------ |
| P1  | [Gap description] | [Code]          | [Regulation/None]  | [Specific deliverable] | [Named role] | [Date]   | [Verifiable metric] | [Evidence type] | Open   |

### NEAR-TERM Tier (30–90 days) — HIGH Gaps

[Same table structure as IMMEDIATE]

### BACKGROUND Tier (90–180 days) — MEDIUM Gaps

[Same table structure as IMMEDIATE]

---

## Regulatory Overlay Assessment (if applicable)

### [HIPAA Security Rule] (if applicable)

[JURISDICTION-SPECIFIC] For HIPAA covered entities and business associates:
Reference: NIST SP 800-66r2, Appendix D — HIPAA Security Rule ↔ CSF 2.0 crosswalk
(verify against current CPRT entry for HIPAA ↔ CSF 2.0 mapping).

| HIPAA Standard                  | 45 C.F.R. Citation | CSF Subcategory    | Status   | Gap   | Notes                                 |
| ------------------------------- | ------------------ | ------------------ | -------- | ----- | ------------------------------------- |
| Access Control — Unique User ID | § 164.312(a)(2)(i) | PR.AA-01, PR.AA-02 | [Status] | [Gap] | Required implementation specification |
| Audit Controls                  | § 164.312(b)       | DE.CM-03, DE.AE-02 | [Status] | [Gap] | Required implementation specification |
| Integrity                       | § 164.312(c)(1)    | PR.DS-06, PR.DS-10 | [Status] | [Gap] | Standard                              |
| Person Authentication           | § 164.312(d)       | PR.AA-01, PR.AA-03 | [Status] | [Gap] | Required implementation specification |
| Transmission Security           | § 164.312(e)(1)    | PR.DS-02           | [Status] | [Gap] | Standard                              |

[Repeat overlay assessment tables for GLBA, SEC, FISMA, NYDFS as applicable]

---

## Glass Box Audit Trail

```yaml
glass_box:
  assessment: "[Organization name] — NIST CSF 2.0 Maturity Assessment"
  assessment_date: "[YYYY-MM-DD]"
  assessment_type: "[Full / Prioritized / Cross-framework mapping / Target Profile]"
  entity_sector: "[Healthcare / Finance / Defense / Technology / Energy / Other]"
  entity_size: "[Small / Medium / Large]"
  applicable_framework: "NIST Cybersecurity Framework 2.0 (NIST CSWP 29, February 2024)"
  nist_csf_version: "2.0"
  functions_assessed: "[Number: 1–6]"
  current_profile:
    govern: "Tier [1–4]"
    identify: "Tier [1–4]"
    protect: "Tier [1–4]"
    detect: "Tier [1–4]"
    respond: "Tier [1–4]"
    recover: "Tier [1–4]"
    overall: "Tier [1–4] — [lowest across all assessed functions]"
  target_profile:
    govern: "Tier [1–4]"
    identify: "Tier [1–4]"
    protect: "Tier [1–4]"
    detect: "Tier [1–4]"
    respond: "Tier [1–4]"
    recover: "Tier [1–4]"
  regulatory_overlays: "[HIPAA / GLBA / SEC / FISMA / NYDFS / NIS2 / None]"
  cross_framework_mapping: "[ISO 27001:2022 / SOC 2 / CIS Controls v8 / CMMC 2.0 / COBIT 2019 / None]"
  subcategories_assessed: "[Count out of 106]"
  critical_gaps: "[Count]"
  high_gaps: "[Count]"
  medium_gaps: "[Count]"
  low_gaps: "[Count]"
  poam_items_total: "[Count]"
  legalcode_mcp: "Connected / Not connected"
  reference_file: "[/tmp/nist-csf-mapping-research-[date].md or 'Not created']"
  citations_verified: "[Count VERIFIED] / [Count UNVERIFIED]"
  self_interrogation: "PASS / REVISED — [basis if revised]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Cross-framework mapping tables derived from secondary sources; verify against current
      NIST CPRT OLIR catalog and framework-specific official mappings before regulatory use."
    - "Tier assessments based on evidence provided; additional documentation review may
      change classifications."
    - "[Any sector-specific limitation, e.g., 'CMMC assessment pending C3PAO selection']"
    - "[Any regulatory overlay limitation, e.g., 'HIPAA mapping not verified against SP 800-66r2 Appendix D']"
  reviewer: "AI-assisted — requires qualified cybersecurity professional and legal review"
```
````

---

## Localization Notes

**United States (all sectors)**: CSF 2.0 is primarily a US framework and is most directly
applicable to US-domiciled organizations. FISMA-regulated entities (federal agencies and
federal contractors) must also implement NIST RMF (SP 800-37 Rev 2) and select controls
from SP 800-53 Rev 5 — CSF is the risk management layer, not the full compliance stack.

[JURISDICTION-SPECIFIC] **European Union**: CSF 2.0 is not a regulatory requirement under
EU law, but it is recognized as an equivalent risk management approach in several NIS2
national implementations (Ireland, Italy, Cyprus). Align CSF GOVERN and PROTECT functions
with NIS2 Article 21 minimum measures and run `legalcode-nis2-compliance-assessment` for
the formal NIS2 compliance determination.

[JURISDICTION-SPECIFIC] **Healthcare (HIPAA)**: NIST SP 800-66r2 (2024) provides the
official HIPAA Security Rule ↔ CSF 2.0 crosswalk. HHS OCR guidance on reasonable and
appropriate safeguards explicitly references NIST publications. CSF alignment is strong
evidence of HIPAA Security Rule compliance but does not eliminate OCR audit risk —
demonstrate implementation, not just policy.

[JURISDICTION-SPECIFIC] **Defense (CMMC)**: CSF alignment does NOT satisfy CMMC 2.0
certification requirements. Level 2 requires 110 practices from NIST SP 800-171 Rev 2
assessed by a C3PAO. CSF serves as a useful planning tool but is not a substitute for
the CMMC formal assessment process.

[JURISDICTION-SPECIFIC] **Financial Services (GLBA / NYDFS)**: FTC Safeguards Rule
(16 C.F.R. Part 314) expects a risk-based information security program; CSF is widely
cited as appropriate methodology. NYDFS 23 NYCRR Part 500 (2023 amendments) explicitly
allows use of a "nationally recognized cybersecurity framework" including NIST CSF.
Both regulators evaluate implementation, not just framework adoption.

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis based on:

- NIST CSWP 29 (NIST CSF 2.0, February 2024) — primary framework document
- NIST SP 1299–1308 Quick Start Guide series
- NIST SP 800-66r2 (HIPAA Security Rule ↔ CSF 2.0, 2024)
- NIST CPRT / OLIR catalog — authoritative cross-framework informative references
- CIS Controls v8 and v8.1 to NIST CSF 2.0 Mapping (CIS Security, 2024)
- AICPA Trust Services Criteria to NIST CSF crosswalk
- ISACA "Connecting COBIT 2019 to the NIST Cybersecurity Framework"
- CISA EDM/NIST CSF Crosswalk (April 2020)
- SEC Cybersecurity Disclosure Rules (Release S7-09-22, effective December 2023)
- 16 C.F.R. Part 314 (FTC Safeguards Rule Final Rule, effective June 9, 2023)
- 23 NYCRR Part 500 (NYDFS, 2023 amendments)
- Two-agent research pipeline: Structural Analyst (reference skill pattern extraction) +
  Legal Research (NIST CSF 2.0 structure, cross-framework mappings, regulatory applicability,
  anti-patterns). Structured synthesis producing 18-element Legalcode gold standard skill.

All cross-framework mapping tables should be verified against current authoritative sources
before use in regulatory reporting or audit contexts.
