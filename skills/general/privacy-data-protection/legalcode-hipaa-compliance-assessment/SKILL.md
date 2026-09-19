---
name: legalcode-hipaa-compliance-assessment
description: HIPAA compliance assessment for covered entities and business associates covering the Security
  Rule (45 CFR Part 164 Subpart C), Privacy Rule (45 CFR Part 164 Subpart E), and Breach Notification
  Rule (45 CFR Part 164 Subpart D). Use when a covered entity or business associate needs to determine
  compliance posture, prepare for OCR audit, conduct an annual security evaluation under 45 CFR 164.308(a)(8),
  respond to a security incident, assess a new technology deployment involving ePHI, or build a HIPAA
  compliance program from scratch.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

HIPAA compliance assessment for covered entities and business associates covering the Security Rule (45 CFR Part 164 Subpart C), Privacy Rule (45 CFR Part 164 Subpart E), and Breach Notification Rule (45 CFR Part 164 Subpart D). Assesses all administrative safeguards (security management process, workforce security, information access management, security awareness and training, contingency planning, evaluation, and business associate oversight), physical safeguards (facility access, workstation security, device and media controls), and technical safeguards (access controls, audit controls, integrity, authentication, and transmission security). Evaluates Privacy Rule obligations including minimum necessary standard, individual rights (access, amendment, accounting, restriction, confidential communications), Notice of Privacy Practices, and authorization requirements. Incorporates 2024-2025 Security Rule NPRM awareness (mandatory MFA, encryption mandates, 72-hour restoration, network segmentation) as emerging requirements to prepare for. Assesses business associate agreement completeness under 45 CFR 164.504(e) and 164.314. Produces Security Risk Analysis documentation structured to meet OCR audit expectations and NIST SP 800-66r2 guidance, with COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL DEFICIENCY classification, prioritized remediation roadmaps, and Glass Box audit trail. Use when a covered entity or business associate needs to determine compliance posture, prepare for OCR audit, conduct an annual security evaluation under 45 CFR 164.308(a)(8), respond to a security incident, assess a new technology deployment involving ePHI, or build a HIPAA compliance program from scratch.


# HIPAA Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance
> with HIPAA (Health Insurance Portability and Accountability Act of 1996, Pub. L. 104-191)
> and HITECH (Health Information Technology for Economic and Clinical Health Act, Pub. L.
> 111-5). It does not constitute legal advice, regulatory guidance, or a compliance
> certification. HIPAA requirements and HHS/OCR enforcement guidance evolve — verify all
> statutory references, regulatory thresholds, and penalty tiers against current CFR text
> and HHS guidance before relying on them. AI-generated legal analysis carries hallucination
> risk for cited authority: any CFR citations, OCR guidance references, or enforcement
> interpretations should be independently verified by a qualified healthcare attorney or
> HIPAA compliance professional. This skill does not replace a formal compliance audit
> conducted by a qualified auditor, and does not constitute a Security Risk Analysis for
> purposes of 45 CFR 164.308(a)(1)(ii)(A) — it produces a structured framework to
> support a human-led risk analysis, not a substitute for one.

## Purpose and Scope

This skill assesses an organization's compliance posture across all three HIPAA rules:
the Security Rule, Privacy Rule, and Breach Notification Rule. It is designed for use
by covered entities (health plans, healthcare clearinghouses, healthcare providers) and
business associates, and supports both initial assessments and annual evaluations.

**Covers:**

- Covered entity and business associate determination (45 CFR 160.103)
- All 18 Security Rule standards and implementation specifications (45 CFR 164.308/310/312/314/316)
- Required vs. Addressable implementation specification analysis
- Security Risk Analysis (SRA) documentation framework (45 CFR 164.308(a)(1))
- Annual Security Rule evaluation (45 CFR 164.308(a)(8))
- Privacy Rule obligations: minimum necessary, individual rights, NPP, authorization
- Breach Notification Rule: four-factor risk assessment, notification timelines, HHS reporting
- Business Associate Agreement (BAA) completeness review (45 CFR 164.504(e), 164.314)
- HITECH overlay: expanded BA liability, enhanced penalties, notification obligations
- 2024-2025 Security Rule NPRM awareness — emerging requirements [VERIFY finalization status]
- NIST SP 800-66r2 (February 2024) implementation guidance alignment
- OCR enforcement patterns and Security Risk Analysis Initiative findings
- State law preemption analysis (CMIA, Texas MRPA, 42 CFR Part 2 overlay)
- Remediation roadmap with IMMEDIATE / NEAR-TERM / BACKGROUND prioritization

**Does not:**

- Certify HIPAA compliance — compliance certifications require accredited auditor
- Constitute a Security Risk Analysis under 45 CFR 164.308(a)(1) — supports, not replaces, human-led SRA
- Provide legal opinions on specific enforcement exposure or litigation strategy
- Assess HIPAA-adjacent frameworks as primary scope (HITRUST CSF, SOC 2, ISO 27001) — those overlap but differ
- Cover 42 CFR Part 2 (Substance Use Disorder records) in full depth — use supplementary analysis
- Apply outside the United States — HIPAA is a US federal statute

**Related skills:**

- `hipaa-breach-notification-operations` — operational breach notification workflow under
  45 CFR 164.400-414 and 42 U.S.C. 17932; use when triaging a specific breach event
- `legalcode-us-breach-notification-triage` — all 50 states + federal overlays including HIPAA;
  use when determining multi-state breach notification obligations
- `legalcode-incident-response-plan-builder` — NIST SP 800-61r3 + multi-regime incident
  response; integrates HIPAA breach notification into the broader IR plan
- `legalcode-vendor-privacy-assessment` — TPRM framework including HIPAA BAA completeness;
  use for ongoing vendor due diligence beyond initial BAA review
- `legalcode-data-processing-agreement-drafter` — GDPR Art. 28 DPA + HIPAA BAA dual-regime
  drafting; use when a vendor processes both EU personal data and US PHI
- `legalcode-nist-csf-mapping` — NIST CSF 2.0 gap analysis with HIPAA SP 800-66r2 overlay;
  use when mapping HIPAA to the CSF for board-level cybersecurity reporting

---

## Jurisdiction and Governing Law

**Primary legislation**: Health Insurance Portability and Accountability Act of 1996
(Pub. L. 104-191), as amended by the Health Information Technology for Economic and
Clinical Health Act (HITECH), Pub. L. 111-5 (2009).

**Primary regulations (45 CFR Part 164)**:

- **Part 160, Subpart A**: General provisions, definitions (covered entity, business associate, PHI)
- **Part 160, Subparts D-E**: Compliance and enforcement; Civil Money Penalties
- **Part 164, Subpart A**: General provisions
- **Part 164, Subpart C** (§§ 164.302-318): Security Standards — Security Rule
- **Part 164, Subpart D** (§§ 164.400-414): Breach Notification Rule
- **Part 164, Subpart E** (§§ 164.500-534): Privacy Standards — Privacy Rule

**Key enforcement authority**: HHS Office for Civil Rights (OCR) — primary HIPAA enforcer.
HHS Office of Inspector General (OIG) and DOJ for criminal referrals (42 U.S.C. § 1320d-6).

**HITECH overlay (42 U.S.C. §§ 17921-17954)**:

- Extends direct HIPAA obligations to business associates (§ 13401)
- Establishes tiered civil penalty structure (§ 13410)
- Requires notification of breaches (§ 13402)
- Strengthens enforcement with state AG authority (§ 13410(e))
- Mandates enhanced audit program (§ 13411)

**NIST guidance** [not legally binding, but OCR-endorsed]:

- **NIST SP 800-66r2** (February 2024): Implementing the HIPAA Security Rule —
  A Cybersecurity Resource Guide; maps Security Rule to NIST CSF 2.0 and SP 800-53r5

**2025 Security Rule NPRM** [PROPOSED — NOT YET FINAL]:

- Published Federal Register January 6, 2025 (89 Fed. Reg. 9954) — NPRM only
- Comment period closed March 7, 2025
- Subject to regulatory freeze (Trump EO January 31, 2025 moratorium on pending rules)
- [VERIFY current finalization status before advising compliance with NPRM requirements]
- Key proposals: eliminate Required/Addressable distinction, mandatory MFA, mandatory
  encryption at rest/in transit, 72-hour restoration for critical systems, annual pen
  testing, quarterly vulnerability scanning, network segmentation requirements

**State law preemption** (45 CFR 160.202-203):

- HIPAA preempts contrary state law — unless state law is MORE stringent (protective)
- HIPAA is a floor, not a ceiling — many states impose stricter requirements
- [JURISDICTION-SPECIFIC] Key state overlays to assess:
  - California CMIA (Cal. Civ. Code §§ 56-56.37): stricter requirements for medical info
  - Texas Medical Records Privacy Act (Tex. Health & Safety Code Ch. 181)
  - 42 CFR Part 2: Substance use disorder records — more restrictive than HIPAA
  - State breach notification laws: 50 states all have separate breach notification laws

**Civil Monetary Penalties** (45 CFR 160.404; 45 CFR Part 102 for annual inflation adjustment):
| Tier | Culpability | Per-Violation Range (2024) | Annual Cap (OCR Discretion) | Annual Statutory Cap |
|------|-------------|---------------------------|----------------------------|---------------------|
| 1 | No knowledge | $141–$71,162 [VERIFY] | $35,581 [VERIFY] | $2,134,831 [VERIFY] |
| 2 | Reasonable cause | $1,424–$71,162 [VERIFY] | $142,355 [VERIFY] | $2,134,831 [VERIFY] |
| 3 | Willful neglect (corrected) | $14,232–$71,162 [VERIFY] | $355,808 [VERIFY] | $2,134,831 [VERIFY] |
| 4 | Willful neglect (not corrected) | $71,162–$2,134,831 [VERIFY] | No reduction | $2,134,831 [VERIFY] |

Note: Base statutory amounts are $100/$1,000/$10,000/$50,000 per violation. OCR applies
annual inflation adjustments under the IAAA. OCR announced in April 2019 it would apply
lower enforcement discretion caps for Tiers 1–3 pending rulemaking; Tier 4 remains at
statutory maximum. [VERIFY current adjusted figures at
hhs.gov/hipaa/for-professionals/compliance-enforcement — these amounts adjust annually].

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you reach a CLARIFY
marker, ask the user before proceeding — do not silently assume defaults. Only ask when
the answer will materially change the analysis; if the context has already been provided,
skip that question and proceed.

Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4 questions per
  call, 2–4 options each, header ≤ 12 characters. Pass the CLARIFY options as the `options`
  array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a `canUseTool`
  callback):** emit the CLARIFY questions as numbered plain text and **stop until the user
  replies**. Do not proceed with assumed answers.

When you proceed with partial context, state every assumption explicitly so the user can
correct it.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. [Option A]: [Description]
2. [Option B]: [Description]
3. [Option C]: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction]
```

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Organization description**: Name, type (hospital, health plan, BA, clearinghouse),
  size, specialties, states of operation, existing security documentation
- **Document set**: Uploaded policies, procedures, risk assessments, training records,
  BAA inventory, incident logs, penetration test reports, audit logs
- **Assessment request**: Prior assessment findings for re-evaluation or annual update
- **Incident trigger**: Post-breach HIPAA posture review (coordinate with incident response
  workflow; use `hipaa-breach-notification-operations` for the breach notification itself)
- **New deployment**: Greenfield compliance build or new technology deployment involving ePHI

**Minimum required context**: Organization type (CE or BA), primary activities involving
PHI/ePHI, states of operation, approximate number of patients/members, and current
compliance posture (no controls / some controls / mature program).

### Step 2: Gather Context

**⟁ CLARIFY** — Gather context before beginning. Ask (skip questions already answered):

1. **Assessment mode**: What is the primary objective?
   - _Full compliance assessment_: Comprehensive evaluation of all three HIPAA rules
   - _Security Rule assessment only_: Focus on 45 CFR Part 164 Subpart C (administrative,
     physical, technical safeguards + organizational/documentation requirements)
   - _Annual Security Rule evaluation (§ 164.308(a)(8))_: Periodic technical and
     nontechnical evaluation to verify safeguards are still adequate
   - _Security Risk Analysis (SRA) support_: Document risk analysis framework per
     § 164.308(a)(1) for OCR audit readiness
   - _BAA audit_: Business associate agreement inventory and completeness review
   - _Breach aftermath review_: Post-incident posture assessment
   - **Why this matters**: Full assessment vs. focused assessment changes depth, output
     format, and time investment.

2. **Entity type**: What kind of entity is this?
   - _Covered Entity — Healthcare Provider_: Hospital, physician practice, pharmacy,
     laboratory, nursing facility, home health agency, behavioral health provider
   - _Covered Entity — Health Plan_: Health insurer, HMO, employer-sponsored group
     health plan (>50 participants), Medicare/Medicaid plan, long-term care insurer
   - _Covered Entity — Healthcare Clearinghouse_: Billing services, claims processors
   - _Business Associate_: Third-party vendor performing functions involving CE's PHI
     (EHR vendors, billing companies, cloud providers, lawyers, accountants, IT support)
   - _Subcontractor Business Associate_: BA's downstream vendor handling ePHI
   - _Hybrid Entity_: Organization with both covered and non-covered components
   - **Why this matters**: Covered entities and business associates have different direct
     obligations; entity type determines which safeguard categories apply and which BAA
     provisions are required.

3. **PHI environment scope**: Where does PHI/ePHI exist?
   - _On-premises only_: Server rooms, workstations, local storage
   - _Cloud-hosted_: AWS, Azure, GCP, or other cloud environments (BA relationships required)
   - _Hybrid_: Both on-premises and cloud
   - _Third-party EHR/practice management_: Vendor-hosted — BA relationship required
   - _Mobile/BYOD_: ePHI on mobile devices or personal devices
   - **Why this matters**: Cloud, mobile, and third-party environments require specific
     technical safeguards and BA agreements; scoping the ePHI environment is the first
     step of any Security Risk Analysis.

4. **Existing framework**: Does the organization operate under any security framework?
   - _HITRUST CSF certified or implementing_: Map HITRUST controls to HIPAA gaps
   - _ISO 27001 certified_: Use as security baseline; identify HIPAA-specific gaps
   - _NIST CSF implementing_: Use SP 800-66r2 crosswalk
   - _SOC 2 Type II report_: Assess Trust Services Criteria overlap with Security Rule
   - _No formal framework_: Begin from first principles
   - **Why this matters**: Existing frameworks accelerate assessment; HIPAA gaps are
     identifiable rather than building from zero.

5. **Prior assessment history**: Has a Security Risk Analysis been conducted previously?
   - _Yes — within 12 months_: Update/verify existing SRA
   - _Yes — more than 12 months ago_: Full refresh required
   - _No documented SRA_: Critical gap — first priority (most common OCR finding)
   - _Unknown_: Treat as no documented SRA
   - **Why this matters**: Absence of a documented SRA is the most frequently cited HIPAA
     Security Rule violation in OCR enforcement; it is also a breach notification factor.

6. **Workforce and access scope**:
   - How many workforce members access ePHI?
   - Do contractors, vendors, or remote workers access ePHI?
   - Is ePHI accessible on mobile devices?
   - **Why this matters**: Workforce size and remote access patterns drive administrative
     and technical safeguard requirements and risk profile.

### Step 3: Gather Legal Authority

Before assessing, gather current authority for the assessment:

**With legalcode-mcp connected:**

- Search: "HIPAA Security Rule 45 CFR 164.308 administrative safeguards" — verify current CFR text
- Search: "HIPAA OCR enforcement 2024 2025 resolution agreements" — verify recent enforcement trends
- Search: "HIPAA Security Rule NPRM 2025 finalization status" — check whether NPRM was finalized
- Search: "NIST SP 800-66r2 HIPAA cybersecurity resource guide" — verify February 2024 guidance
- Search: "[State] healthcare privacy law HIPAA preemption" — verify state law overlay
- Save results to `/tmp/hipaa-assessment-research.md`
- Mark all verified citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Proceed with CFR text from training data; mark all citations [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Particularly flag [VERIFY] on:
  - Current inflation-adjusted CMP amounts
  - NPRM finalization status
  - State law preemption analysis
  - Recent OCR enforcement settlements
- Recommend human verification of all enforcement-specific findings

### Step 4: Entity Determination and PHI Scoping Gate

**BINARY GATE — Apply before assessing any safeguard requirements.**

This step determines whether HIPAA applies and what PHI/ePHI is in scope. If the
organization is out of scope, issue the determination and stop. If in scope, identify
entity type and ePHI scope before proceeding.

#### 4a. Covered Entity Determination (45 CFR 160.102, 160.103)

Test whether the organization is a **covered entity** by applying this three-part gate:

**Gate 1 — Healthcare Provider**:

- Does the organization furnish, bill, or receive payment for healthcare in the normal
  course of business? (45 CFR 160.103 definition)
- AND: Does it transmit any health information in electronic form in connection with a
  HIPAA-covered transaction? (Eligibility inquiries, claims, remittances, etc. — 45 CFR Part 162)
- → COVERED ENTITY if both prongs satisfied
- Note: Small providers who never transmit electronically are exempt; however, they
  typically use clearinghouses or billing services that transmit on their behalf — making
  those clearinghouses/billing services CEs or BAs

**Gate 2 — Health Plan**:

- Does the organization provide or pay for the cost of medical care? (45 CFR 160.103)
- Includes: health insurance issuers, HMOs, employer group health plans >50 participants,
  Medicare/Medicaid/CHIP programs, long-term care insurers
- Excludes: workers' compensation, property/casualty, auto insurance (for healthcare)
- → COVERED ENTITY if satisfied

**Gate 3 — Healthcare Clearinghouse**:

- Does the organization process health information by translating between standard and
  non-standard formats? (45 CFR 160.103)
- → COVERED ENTITY if satisfied

**Result**: If none of the three CE gates pass, assess whether the organization is a
**Business Associate** (Gate 4) before concluding HIPAA does not apply.

#### 4b. Business Associate Determination (45 CFR 160.103, 164.502(e))

A Business Associate (BA) is a person/entity that performs functions or activities on
behalf of a CE involving the use or disclosure of PHI, or that provides services to a CE
where the provision of services involves PHI disclosure.

**BA test**: Does the organization:

- Process, store, or transmit PHI on behalf of a CE?
- Provide data analysis, claims processing, utilization review, QA, billing, benefit
  management, practice management, or financial services to a CE involving PHI?
- Provide legal, actuarial, accounting, consulting, data aggregation, management,
  administrative, accreditation, or financial services to a CE where performance requires
  disclosure of PHI?

**Important distinctions**:

- **Conduit exception**: Mere conduits (USPS, UPS, certain ISPs, couriers) that transmit
  PHI but do not access its content are NOT business associates
- **Workforce members**: CE's workforce is not a BA (covered under CE's direct obligations)
- **Subcontractors**: A BA's subcontractor that receives ePHI is itself a BA (45 CFR 160.103)

**Result**: If the organization is neither a CE nor a BA, document the determination and
close the assessment. If it is a CE, BA, or subcontractor BA, proceed to Step 5.

#### 4c. PHI/ePHI Scoping

Identify and document all locations where PHI and ePHI exists. This is required for
the Security Risk Analysis under 45 CFR 164.308(a)(1)(ii)(A).

**ePHI inventory checklist**:

- [ ] Electronic Health Record (EHR) systems
- [ ] Practice management / revenue cycle management systems
- [ ] Medical imaging systems (PACS, DICOM)
- [ ] Laboratory information systems
- [ ] Pharmacy systems
- [ ] Email systems (if ePHI is transmitted via email)
- [ ] File shares / NAS / SAN
- [ ] Cloud storage (SharePoint, OneDrive, Google Drive, Dropbox, etc.)
- [ ] Mobile devices and tablets
- [ ] Laptops and workstations
- [ ] Backup systems and tapes
- [ ] Third-party vendor systems (EHR-as-a-service, billing platforms, etc.)
- [ ] Telehealth platforms
- [ ] Patient portals
- [ ] APIs and data exchange endpoints
- [ ] Fax servers (if eFax involving ePHI)
- [ ] Legacy / retired systems still holding ePHI

**⟁ CLARIFY** — If the ePHI scope is unclear or involves novel environments:

1. _Cloud-native organization_: All ePHI in cloud — is the cloud provider under a BAA?
2. _IoT/Connected medical devices_: ePHI generated by devices — are these in scope?
3. _Research or de-identified data_: Is PHI fully de-identified per 45 CFR 164.514?

### Step 5: Security Rule Assessment — Administrative Safeguards (45 CFR 164.308)

Assess all nine administrative safeguard standards. For each, determine whether the
organization has implemented the standard (or, for Addressable specs, has implemented
an equivalent alternative and documented the rationale).

**Classification per standard**:

- **COMPLIANT**: Standard fully implemented with documented evidence
- **PARTIAL**: Standard partially implemented; gaps exist but some controls present
- **NON-COMPLIANT**: Standard not implemented or materially inadequate
- **CRITICAL DEFICIENCY**: Standard not implemented AND creates significant, imminent risk
  (e.g., no Security Risk Analysis, no sanction policy, no incident response procedure)

#### 5.1 — Security Management Process (§ 164.308(a)(1)) [ALL REQUIRED]

**5.1.1 — Risk Analysis [Required]** (45 CFR 164.308(a)(1)(ii)(A))

Conduct an accurate and thorough assessment of potential risks and vulnerabilities to
the confidentiality, integrity, and availability of ALL ePHI held by the organization.

**OCR-required risk analysis elements** (per OCR Guidance on Risk Analysis, July 2010):

- [ ] Scope: All ePHI regardless of form or location (use ePHI inventory from Step 4c)
- [ ] Data collection: Document current systems, applications, users, and data flows
- [ ] Identify and document reasonably anticipated threats to ePHI
- [ ] Identify and document vulnerabilities to ePHI (technical and non-technical)
- [ ] Assess current security measures and their effectiveness
- [ ] Determine likelihood of threat occurrence (Low/Medium/High)
- [ ] Determine potential impact if a threat occurs (Low/Medium/High)
- [ ] Determine level of risk for each threat-vulnerability pair
- [ ] Document all findings in a written Risk Analysis report
- [ ] Review and update as conditions change (workforce, technology, regulations)

**Evidence expected by OCR**:

- Written Risk Analysis document (not a vendor checklist — must reflect this organization)
- ePHI system inventory supporting the scope
- Threat-vulnerability-risk matrix with likelihood/impact ratings
- Documentation of current controls and their effectiveness
- Sign-off by security official and senior leadership

**Common OCR finding**: Inadequate risk analysis is the #1 HIPAA Security Rule violation.
OCR's Security Risk Analysis Initiative (2024-2025) found risk analysis failures in
13 of its enforcement matters, all related to ransomware incidents.

**⟁ CLARIFY** — If the organization has a prior risk analysis:

1. _Within 12 months, comprehensive_: Verify it covers all ePHI locations and document review date
2. _More than 12 months old_: Treat as requiring full update — significant changes likely occurred
3. _Vendor-completed checklist only_: Flag as PARTIAL — checklists do not constitute a risk analysis
4. _None documented_: CRITICAL DEFICIENCY — highest priority remediation item

**5.1.2 — Risk Management [Required]** (45 CFR 164.308(a)(1)(ii)(B))

Implement security measures sufficient to reduce risks identified in the Risk Analysis
to a reasonable and appropriate level.

Assessment criteria:

- [ ] Written Risk Management Plan exists and addresses Risk Analysis findings
- [ ] Risk Management Plan prioritizes risks and identifies remediation actions
- [ ] Risk Management Plan is updated as risks change
- [ ] Progress against Risk Management Plan is tracked and documented
- [ ] Plan is tied to the organization's overall HIPAA compliance program

**5.1.3 — Sanction Policy [Required]** (45 CFR 164.308(a)(1)(ii)(C))

Apply appropriate sanctions against workforce members who fail to comply with security
policies and procedures.

Assessment criteria:

- [ ] Written sanction policy exists and is communicated to all workforce
- [ ] Policy addresses a range of violations (from careless to intentional)
- [ ] Policy specifies graduated sanctions (verbal warning / written warning / termination)
- [ ] Policy applies equally to all workforce including supervisors and leadership
- [ ] Sanctions are documented and applied consistently (including against leadership)
- [ ] Policy is enforced — check personnel records for documentation

**5.1.4 — Information System Activity Review [Required]** (45 CFR 164.308(a)(1)(ii)(D))

Implement procedures to regularly review records of information system activity
(audit logs, access reports, security incident tracking reports).

Assessment criteria:

- [ ] Audit logs are generated for systems processing ePHI
- [ ] Procedures exist for reviewing audit logs at defined intervals
- [ ] Logs are reviewed regularly (frequency documented and appropriate to risk)
- [ ] Anomalies and suspicious activity trigger escalation procedures
- [ ] Log review results are documented

#### 5.2 — Assigned Security Responsibility (§ 164.308(a)(2)) [Required]

Identify the security official responsible for developing and implementing security
policies and procedures.

Assessment criteria:

- [ ] A specific individual is designated as HIPAA Security Official (not a committee)
- [ ] Role is documented in writing (job description or formal designation letter)
- [ ] Security Official has appropriate authority and resources
- [ ] Role is actively performing security oversight functions (not title-only)
- [ ] Designation is current — updated if personnel changes occurred

#### 5.3 — Workforce Security (§ 164.308(a)(3)) [All Addressable]

**5.3.1 — Authorization and/or Supervision [Addressable]**

- [ ] Procedures exist to ensure workforce access to ePHI is authorized and supervised
- [ ] Supervisory oversight is documented for workforce handling ePHI
- OR: Document equivalent compensating control and rationale for not implementing

**5.3.2 — Workforce Clearance Procedure [Addressable]**

- [ ] Procedures exist to determine appropriateness of access for each workforce member
- [ ] Background check process exists (appropriate to role and access level)
- [ ] Access authorization decisions are documented
- OR: Equivalent compensating control documented

**5.3.3 — Termination Procedures [Addressable]**

- [ ] Written procedures for revoking ePHI access upon termination or role change
- [ ] Procedures cover: system access revocation, badge/key return, device collection
- [ ] Procedures apply to voluntary terminations, involuntary terminations, and role changes
- [ ] Access is revoked promptly (same day or prior to termination for high-risk departures)
- OR: Equivalent compensating control documented

#### 5.4 — Information Access Management (§ 164.308(a)(4))

**5.4.1 — Isolating Healthcare Clearinghouse Functions [Required — only for hybrid entities]**

- [ ] If CE is a hybrid entity or clearinghouse: firewall/isolation controls exist
      separating clearinghouse functions from other organizational functions

**5.4.2 — Access Authorization [Addressable]**

- [ ] Policies/procedures exist for authorizing access to ePHI
- [ ] Access is granted based on documented role and minimum necessary principle
- [ ] Access authorization is approved by appropriate authority (manager/security official)
- [ ] Authorization decisions are documented
- OR: Equivalent compensating control documented

**5.4.3 — Access Establishment and Modification [Addressable]**

- [ ] Procedures exist for establishing, modifying, and terminating access to ePHI
- [ ] Role-based access control (RBAC) is implemented or equivalent
- [ ] Access reviews are conducted periodically (quarterly or annually at minimum)
- [ ] Privileged access is documented and regularly reviewed
- OR: Equivalent compensating control documented

#### 5.5 — Security Awareness and Training (§ 164.308(a)(5)) [All Addressable]

**⟁ CLARIFY** — Training scope:

1. _New hire + annual training program_: Existing — assess quality and documentation
2. _Ad hoc / informal training_: Flag as PARTIAL — document gap
3. _No training program_: NON-COMPLIANT or CRITICAL DEFICIENCY depending on workforce size

**5.5.1 — Security Reminders [Addressable]**

- [ ] Periodic security reminders sent to workforce (emails, newsletters, posters, meetings)
- [ ] Reminders cover current threats (phishing, ransomware, social engineering)
- [ ] Reminder distribution is documented (who received, when, topic)
- OR: Equivalent compensating control documented

**5.5.2 — Protection from Malicious Software [Addressable]**

- [ ] Antivirus/endpoint detection and response (EDR) deployed on all ePHI systems
- [ ] Malware protection is updated regularly (real-time update or daily at minimum)
- [ ] Procedures exist for reporting suspected malware infections
- [ ] Email filtering deployed to block malicious attachments and phishing
- OR: Equivalent compensating control documented

**5.5.3 — Log-in Monitoring [Addressable]**

- [ ] Procedures exist to monitor log-in attempts to ePHI systems
- [ ] Failed log-in attempts are logged and reviewed
- [ ] Account lockout policies are in place
- [ ] Unusual access patterns trigger alerts
- OR: Equivalent compensating control documented

**5.5.4 — Password Management [Addressable]**

- [ ] Procedures for creating, changing, and safeguarding passwords exist
- [ ] Password complexity requirements are enforced (length, complexity, reuse prohibition)
- [ ] Passwords are changed at defined intervals or upon suspected compromise
- [ ] Shared/generic accounts are prohibited or controlled for ePHI systems
- [ ] Password managers or SSO with strong authentication are in use
- OR: Equivalent compensating control documented

#### 5.6 — Security Incident Procedures (§ 164.308(a)(6)) [Required]

**5.6.1 — Response and Reporting [Required]**

- [ ] Written security incident response policy and procedures exist
- [ ] "Security incident" is defined broadly (any attempted or successful unauthorized access)
- [ ] Incident reporting chain is documented (who reports to whom, how)
- [ ] Procedures cover: detection, response, containment, eradication, recovery
- [ ] Procedures identify when to escalate to potential breach assessment
- [ ] Incidents are documented (incident log) even if not ultimately a reportable breach
- [ ] Policy has been tested (tabletop exercise or simulated incident)
- [ ] Procedures reference coordination with `hipaa-breach-notification-operations` workflow

#### 5.7 — Contingency Plan (§ 164.308(a)(7))

**5.7.1 — Data Backup Plan [Required]**

- [ ] Written policy for creating and maintaining retrievable exact copies of ePHI
- [ ] Backups occur at defined intervals (daily recommended for patient-facing systems)
- [ ] Backups are encrypted (especially if stored offsite or in cloud)
- [ ] Backup integrity is tested (restore tests conducted periodically)
- [ ] Backups are stored at a geographically separate location from primary systems

**5.7.2 — Disaster Recovery Plan [Required]**

- [ ] Written plan exists for restoring lost data after a disaster
- [ ] Plan identifies recovery time objectives (RTO) and recovery point objectives (RPO)
- [ ] Plan covers natural disasters, ransomware, hardware failure, power loss
- [ ] Recovery procedures are documented and assigned to specific individuals
- [ ] Plan is tested at defined intervals (annual at minimum)

**5.7.3 — Emergency Mode Operation Plan [Required]**

- [ ] Written plan exists for maintaining critical business processes while ePHI is unavailable
- [ ] Plan identifies which processes are critical to patient care or operations
- [ ] Downtime procedures are documented (paper-based fallback where applicable)
- [ ] Workforce knows the downtime procedures (trained)

**5.7.4 — Testing and Revision Procedures [Addressable]**

- [ ] Procedures for testing and revising contingency plans exist
- [ ] Tests are conducted at defined intervals and results documented
- [ ] Lessons from tests or actual incidents are incorporated into plan updates
- OR: Equivalent compensating control documented

**5.7.5 — Applications and Data Criticality Analysis [Addressable]**

- [ ] Organization has assessed and documented the criticality of applications and data
- [ ] Criticality rankings inform backup frequency, recovery priority, and RTO/RPO
- OR: Equivalent compensating control documented

**Note on 2025 NPRM [VERIFY finalization]**: The proposed Security Rule update would require
72-hour restoration of critical systems — significantly stricter than the current standard.

#### 5.8 — Evaluation (§ 164.308(a)(8)) [Required]

Perform periodic technical and non-technical evaluation in response to environmental or
operational changes that affect ePHI security.

Assessment criteria:

- [ ] Formal Security Rule evaluation has been conducted within the last 12 months
- [ ] Evaluation covers both technical controls (penetration testing, vulnerability scans)
      and non-technical controls (policy review, training adequacy)
- [ ] Evaluation is conducted in response to significant changes (new systems, workforce
      changes, new threats, regulatory updates)
- [ ] Evaluation findings are documented and feed into the Risk Management process

#### 5.9 — Business Associate Contracts and Other Arrangements (§ 164.308(b)) [Required]

**5.9.1 — Written Contract or Other Arrangement [Required]**

- [ ] Written BAA in place for every business associate
- [ ] BAA covers all required provisions (assessed in Step 8)
- [ ] BAA inventory exists and is maintained (updated when BA relationships begin/end)
- [ ] BAA review process exists (reviewed when BA activities change or contract renews)

### Step 6: Security Rule Assessment — Physical Safeguards (45 CFR 164.310)

Assess all four physical safeguard standards. Physical safeguards protect ePHI systems
and equipment from unauthorized physical access, natural hazards, and environmental threats.

#### 6.1 — Facility Access Controls (§ 164.310(a)) [All Addressable]

**6.1.1 — Contingency Operations [Addressable]**

- [ ] Procedures exist for physical access to facilities during a contingency
- [ ] Emergency access is documented (who can access systems in an emergency)
- [ ] Access controls do not impede emergency response (but also don't default to open)
- OR: Equivalent compensating control documented

**6.1.2 — Facility Security Plan [Addressable]**

- [ ] Written plan to safeguard ePHI systems and facilities from unauthorized access
- [ ] Physical security controls documented (locks, badges, cameras, visitor log)
- [ ] Plan covers server rooms, data centers, and areas with workstations handling ePHI
- OR: Equivalent compensating control documented

**6.1.3 — Access Control and Validation Procedures [Addressable]**

- [ ] Procedures for controlling/validating workforce access to ePHI facilities
- [ ] Access is role-based (not all workforce can access all areas)
- [ ] Visitor access is controlled, logged, and supervised
- [ ] Access logs are reviewed periodically
- OR: Equivalent compensating control documented

**6.1.4 — Maintenance Records [Addressable]**

- [ ] Records of repairs and modifications to physical security components maintained
- [ ] Maintenance records include who performed work, date, and what was done
- OR: Equivalent compensating control documented

#### 6.2 — Workstation Use (§ 164.310(b)) [Required]

- [ ] Policies/procedures specifying proper use of workstations that access ePHI
- [ ] Policies specify where workstations may be located and how ePHI may be accessed
- [ ] Remote work policies address workstation security for at-home access
- [ ] Auto-locking screen policy is enforced (5-15 minutes of inactivity)
- [ ] Clean desk policy enforced for workstations in areas accessible to patients/visitors

#### 6.3 — Workstation Security (§ 164.310(c)) [Required]

- [ ] Physical safeguards in place for workstations (locked rooms, cable locks, privacy screens)
- [ ] Workstations in patient/public areas have physical privacy controls
- [ ] Laptop security controls in place (cable locks, asset tracking, encryption — see also
      Technical Safeguard 7.1.4)
- [ ] Unattended workstations auto-lock and require authentication to resume

#### 6.4 — Device and Media Controls (§ 164.310(d))

**6.4.1 — Disposal [Required]**

- [ ] Written procedures for disposal of ePHI-containing hardware and media
- [ ] Disposal includes: degaussing, physical destruction, or DoD-level wipe
- [ ] Certificates of destruction obtained and retained for disposed equipment
- [ ] Disposal vendor is a Business Associate (BAA required)

**6.4.2 — Media Re-Use [Required]**

- [ ] Procedures for removing ePHI from media before re-use (within or outside organization)
- [ ] Media sanitization standard is documented (NIST SP 800-88 or equivalent)
- [ ] Re-use process is documented and tracked

**6.4.3 — Accountability [Addressable]**

- [ ] Device/media inventory tracks hardware and electronic media containing ePHI
- [ ] Inventory records: type, location, user, serial number/ID
- [ ] Inventory updated when devices move, are assigned, or retired
- OR: Equivalent compensating control documented

**6.4.4 — Data Backup and Storage [Addressable]**

- [ ] Backup copy of ePHI made before moving equipment
- [ ] Backup copies are stored securely and separately from primary systems
- OR: Equivalent compensating control documented

### Step 7: Security Rule Assessment — Technical Safeguards (45 CFR 164.312)

Assess all five technical safeguard standards. Technical safeguards are technology
and policies/procedures that protect ePHI and control access to it.

#### 7.1 — Access Control (§ 164.312(a)) [Standard: Required]

**7.1.1 — Unique User Identification [Required]**

- [ ] Every user has a unique identifier (username/user ID) — no shared accounts for ePHI access
- [ ] User IDs are linked to individual workforce members (audit trail to person)
- [ ] Generic, shared, or group accounts for ePHI systems are prohibited or tightly controlled
- [ ] Service/system accounts are documented, monitored, and not used for interactive access

**7.1.2 — Emergency Access Procedure [Required]**

- [ ] Written procedure for obtaining access to ePHI during an emergency
- [ ] Emergency access is documented (break-glass credentials, emergency accounts)
- [ ] Emergency access is logged and reviewed post-event
- [ ] Emergency access does not become routine (audited for misuse)

**7.1.3 — Automatic Logoff [Addressable]**

- [ ] Systems automatically log off or lock after a defined period of inactivity
- [ ] Logoff timeout is appropriate to risk (5-15 minutes recommended for ePHI access)
- [ ] Remote access sessions have shorter timeouts (or require re-authentication)
- OR: Equivalent compensating control documented (e.g., mandatory screen lock policy enforced)

**7.1.4 — Encryption and Decryption [Addressable]**

- [ ] ePHI is encrypted at rest on all storage media and systems
- [ ] Encryption algorithm is industry-standard (AES-256 recommended)
- [ ] Encryption keys are managed separately from encrypted data
- [ ] Encryption status of laptops/mobile devices is verified (BitLocker, FileVault, MDM)
- [ ] Cloud storage is encrypted at rest (verify cloud provider BAA confirms this)
- OR: Equivalent compensating control documented with rationale
- [VERIFY 2025 NPRM: Proposed rule would make encryption mandatory — not addressable]

#### 7.2 — Audit Controls (§ 164.312(b)) [Required]

- [ ] Hardware, software, or procedural mechanisms record and examine ePHI system activity
- [ ] Audit logs capture: user ID, date/time, action taken, ePHI accessed
- [ ] Audit logs are protected from modification or deletion (immutable logging)
- [ ] Audit logs are retained for sufficient period (6 years minimum per § 164.316(b)(2))
- [ ] Logs are reviewed at defined intervals (link to Information System Activity Review, § 164.308(a)(1)(ii)(D))
- [ ] SIEM (Security Information and Event Management) or equivalent log aggregation in place

#### 7.3 — Integrity (§ 164.312(c)) [Standard: Required]

**7.3.1 — Mechanism to Authenticate ePHI [Addressable]**

- [ ] Mechanisms exist to corroborate that ePHI has not been altered or destroyed
      in an unauthorized manner
- [ ] File integrity monitoring (FIM) deployed for ePHI data stores
- [ ] Checksums or cryptographic hashes used to verify data integrity
- [ ] Database integrity controls implemented (access controls, versioning, audit logging)
- OR: Equivalent compensating control documented

#### 7.4 — Person or Entity Authentication (§ 164.312(d)) [Required]

- [ ] Procedures verify the identity of persons seeking access to ePHI
- [ ] Multi-factor authentication (MFA) is implemented for remote access to ePHI systems
- [ ] MFA is implemented for privileged/administrative access to ePHI systems
- [ ] MFA for internal ePHI system access assessed (recommended; proposed as mandatory in NPRM)
- [ ] Authentication mechanisms are documented (passwords, tokens, biometrics, certificates)
- [VERIFY 2025 NPRM: Proposed rule would require MFA for all ePHI access without exception]

#### 7.5 — Transmission Security (§ 164.312(e)) [Standard: Addressable]

**7.5.1 — Integrity Controls [Addressable]**

- [ ] Technical controls ensure ePHI transmitted electronically is not improperly modified
- [ ] TLS 1.2+ is required for all ePHI in transit (TLS 1.3 recommended)
- [ ] API transmission of ePHI uses encrypted channels
- OR: Equivalent compensating control documented

**7.5.2 — Encryption [Addressable]**

- [ ] ePHI encrypted when transmitted electronically over open networks
- [ ] Encryption applied to email transmission of ePHI (encrypted email or secure portal)
- [ ] VPN or equivalent encryption for remote access to ePHI systems
- [ ] eFax transmission of ePHI uses encrypted channels
- OR: Equivalent compensating control documented
- [VERIFY 2025 NPRM: Proposed rule would make transmission encryption mandatory]

### Step 8: Business Associate Agreement (BAA) Assessment (45 CFR 164.504(e), 164.314(a))

#### 8a. BAA Inventory

Compile or verify the organization's BAA inventory. A BAA is required with every
Business Associate before any PHI/ePHI is shared. Assess:

- [ ] Complete, current inventory of all Business Associates maintained
- [ ] Every BA with access to PHI/ePHI has a signed BAA
- [ ] BAA dates are tracked — no expired BAAs
- [ ] Process exists for identifying new BA relationships before they begin
- [ ] Annual BAA review process established

**Common gap**: Organizations often have legacy BAs (legacy IT systems, old billing
services) without BAAs, or BAAs that predate HITECH and were never updated to include
expanded BA obligations.

#### 8b. BAA Completeness Checklist

Each BAA must include the following provisions per 45 CFR 164.504(e)(2) and 164.314(a)(2):

**Privacy Rule provisions (45 CFR 164.504(e)(2))**:

- [ ] Establish permitted and required uses and disclosures of PHI by the BA
- [ ] Prohibit BA from using or disclosing PHI in ways not permitted by contract or required by law
- [ ] Require BA to use appropriate safeguards to prevent unauthorized use or disclosure
- [ ] Require BA to report security incidents (including breaches) to CE
- [ ] Require BA to report uses/disclosures not provided for by the contract
- [ ] Require BA to ensure any subcontractors agree to the same restrictions (flow-down)
- [ ] Provide individuals access to PHI where requested per § 164.524
- [ ] Make PHI available for amendment per § 164.526
- [ ] Make PHI available for accounting of disclosures per § 164.528
- [ ] Make internal practices/books/records available to HHS for compliance purposes
- [ ] Return or destroy all PHI at contract termination (or justify why not possible)
- [ ] Authorize CE to terminate contract if BA has materially breached provisions

**Security Rule provisions (45 CFR 164.314(a)(2))**:

- [ ] BA must implement administrative, physical, and technical safeguards for ePHI
- [ ] BA must ensure subcontractors agree to the same safeguard requirements
- [ ] BA must report to CE any security incidents including breaches under § 164.410
- [ ] BA must identify and report all security incidents, including attempted attacks

**Recommended (not required but best practice)**:

- [ ] Specific incident notification timeline (most organizations require 1-3 business days)
- [ ] BA liability for data breach costs (indemnification provision)
- [ ] BA must maintain documented compliance program
- [ ] Audit rights for CE to verify BA compliance
- [ ] Cyber insurance requirements for BA

**⟁ CLARIFY** — If BAA gaps are found:

1. _No BAA — active relationship_: CRITICAL DEFICIENCY — BAA must be executed immediately
2. _Pre-HITECH BAA (pre-2013)_: HIGH priority update — BA now directly liable; BAA should reflect
3. _Missing subcontractor flow-down_: PARTIAL — risk depends on subcontractor access to ePHI

### Step 9: Privacy Rule Assessment (45 CFR Part 164 Subpart E)

Assess key Privacy Rule obligations. Focus on: Notice of Privacy Practices, individual
rights, minimum necessary, and authorization requirements.

#### 9a. Notice of Privacy Practices (NPP) (§ 164.520)

**Requirement**: Covered healthcare providers and health plans must develop and distribute
a Notice of Privacy Practices to individuals.

- [ ] NPP is written in plain language
- [ ] NPP describes all uses and disclosures the CE may make of PHI
- [ ] NPP describes individual rights and CE duties
- [ ] NPP includes effective date
- [ ] NPP lists contact information for complaints and Privacy Official
- [ ] NPP includes required statement about uses for TPO, law enforcement, etc.
- [ ] Healthcare providers: NPP provided on first visit/interaction; posted prominently
- [ ] Health plans: NPP provided at enrollment and every 3 years; distributed upon revision
- [ ] Website NPP is current and matches paper version

#### 9b. Individual Rights Compliance

Assess whether procedures exist and function for each individual right:

| Right                                | CFR Citation | Requirement                                                                | Evidence Checklist                          |
| ------------------------------------ | ------------ | -------------------------------------------------------------------------- | ------------------------------------------- |
| Right of Access                      | § 164.524    | 30 days to respond (60 if extension); provide ePHI in requested format     | Written policy; response tracking log       |
| Right to Amendment                   | § 164.526    | 60 days to respond; may deny with valid reason                             | Written policy; denial documentation        |
| Right to Accounting                  | § 164.528    | 60 days; 6-year lookback; certain disclosures only                         | Accounting log; disclosure tracking system  |
| Right to Restrict                    | § 164.522(a) | Must honor restriction on disclosure to health plan if individual pays OOP | Written policy; intake process for requests |
| Right to Confidential Communications | § 164.522(b) | Must accommodate reasonable requests                                       | Written policy; patient intake form         |
| Right to Notice                      | § 164.520    | See NPP section above                                                      | NPP distribution records                    |

**2021 Access Right Updates [VERIFY]**:

- HHS increased scrutiny of right of access compliance — multiple enforcement actions
- OCR's Right of Access Initiative: dozens of enforcement actions since 2019
- Fees for copies must be "reasonable" — cost-based fee schedule
- Electronic access must be provided in the requested format if readily producible

#### 9c. Minimum Necessary Standard (§ 164.502(b), § 164.514(d))

- [ ] Policies limit PHI use, disclosure, and requests to the minimum necessary
- [ ] Role-based access controls reflect minimum necessary principle (link to § 164.308(a)(4))
- [ ] Standard protocols exist for routine disclosures (what PHI is routinely needed)
- [ ] Individual review for non-routine disclosures
- [ ] "Need to know" culture is reinforced through training
- Exception: Minimum necessary does not apply to disclosures for TPO

#### 9d. Authorization Requirements (§ 164.508)

- [ ] Written authorization policy exists and covers when authorization is required
- [ ] Authorization forms meet § 164.508(c) content requirements
- [ ] Authorizations for psychotherapy notes and marketing have specific requirements
- [ ] Tracking system exists for outstanding authorizations
- [ ] Authorization revocation process exists and is communicated to individuals

#### 9e. Workforce Training and Privacy Official

- [ ] Privacy Official designated (may be same as Security Official for small CEs)
- [ ] All workforce trained on Privacy Rule upon hire and periodically
- [ ] Training records document: who trained, when, content
- [ ] Contact for privacy questions/complaints publicized internally

### Step 10: Breach Notification Rule Assessment (45 CFR Part 164 Subpart D)

Assess whether the organization is prepared to identify, assess, and report HIPAA breaches.

**Note**: For operational breach response, use `hipaa-breach-notification-operations`.
This step assesses whether the organization has the infrastructure to respond correctly.

#### 10a. Breach Detection and Assessment Infrastructure

- [ ] Incident log maintained — all potential breaches documented even if ultimately not reportable
- [ ] Four-factor risk assessment procedure documented for assessing whether breach occurred:
  - Factor 1: Nature/extent of PHI involved and likelihood of re-identification
  - Factor 2: Who accessed/received PHI — authorized or unauthorized person?
  - Factor 3: Whether PHI was actually acquired or viewed (or merely at risk)
  - Factor 4: Extent to which risk has been mitigated
- [ ] 60-day clock tracking mechanism exists (discovery date is clearly documented)
- [ ] Breach assessment team identified (Privacy Official, Security Official, Legal)
- [ ] Breach response procedure tested (tabletop exercise conducted)

#### 10b. Notification Preparation

- [ ] Template individual breach notification letter exists and meets § 164.404(c) content requirements:
  - Brief description of the breach
  - Types of PHI involved
  - What affected individuals should do to protect themselves
  - What CE is doing to investigate and mitigate
  - Contact information for CE
- [ ] Template media notification exists (for >500 individuals in a state)
- [ ] HHS OCR online breach reporting portal access confirmed (Breach Portal)
- [ ] Law enforcement delay procedure understood (§ 164.412)

#### 10c. Business Associate Breach Reporting

- [ ] BAAs require BA to report security incidents to CE promptly
- [ ] BAA incident notification SLA is defined (HHS recommends reporting without unreasonable delay)
- [ ] Process exists for CE to receive and assess BA breach reports
- [ ] BA breach triggers CE's 60-day notification clock from date of CE's knowledge (not BA discovery)

#### 10d. Documentation and Retention

- [ ] Breach assessments documented and retained 6 years (whether or not reportable)
- [ ] Burden-of-proof documentation retained for low-probability determinations
- [ ] HHS annual breach log maintained for breaches affecting <500 individuals
- [ ] Large breach reports (>500) documented with submission confirmation

### Step 11: Emerging Requirements — 2025 Security Rule NPRM

**IMPORTANT**: The following requirements are PROPOSED in the NPRM published
January 6, 2025 (89 Fed. Reg. 9954). They are NOT yet final rules. A regulatory
freeze was imposed January 31, 2025. Verify current finalization status before
treating these as binding obligations. [VERIFY]

Nevertheless, assess readiness for these proposed requirements, as they reflect
current OCR expectations and security best practices regardless of final rule status:

| Proposed Requirement                                                         | Current Status | Gap Assessment                                               |
| ---------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------ |
| Eliminate Required/Addressable distinction — all safeguards become mandatory | PROPOSED       | Assess which Addressable specs are not currently implemented |
| Mandatory MFA for all ePHI access (no exceptions)                            | PROPOSED       | Identify systems/users lacking MFA                           |
| Mandatory encryption at rest for all ePHI                                    | PROPOSED       | Inventory unencrypted ePHI storage                           |
| Mandatory encryption in transit for all ePHI                                 | PROPOSED       | Identify unencrypted transmission paths                      |
| 72-hour restoration of critical systems after breach                         | PROPOSED       | Compare to current DR RTO/RPO targets                        |
| Annual penetration testing of systems with ePHI                              | PROPOSED       | Assess current pen test frequency and scope                  |
| Quarterly vulnerability scans                                                | PROPOSED       | Assess current scanning frequency                            |
| Network segmentation of ePHI systems                                         | PROPOSED       | Assess network architecture for segmentation                 |
| Written inventory of all technology assets handling ePHI                     | PROPOSED       | Assess asset inventory completeness                          |
| Enhanced BA security oversight obligations                                   | PROPOSED       | Assess BA risk management and monitoring process             |
| Multi-factor authentication for workforce re-training                        | PROPOSED       | Assess current MFA training adequacy                         |

**Risk posture**: Even where the NPRM is not finalized, implementing these measures
reduces HIPAA violation risk (risk management defense) and aligns with the NIST SP
800-66r2 guidance, which IS current and OCR-endorsed.

### Step 12: Synthesize Findings and Produce Assessment

#### 12a. Classification Framework

Apply the four-tier classification to each finding across all assessed areas:

| Classification          | Definition                                                                                                                                                     | Response Requirement                                                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPLIANT**           | Standard fully implemented; documented evidence available                                                                                                      | Document and maintain                                                                                                                                     |
| **PARTIAL**             | Standard partially implemented; addressable gap exists                                                                                                         | Remediation plan within 90 days                                                                                                                           |
| **NON-COMPLIANT**       | Standard not implemented or materially inadequate                                                                                                              | Remediation plan within 30 days                                                                                                                           |
| **CRITICAL DEFICIENCY** | Standard not implemented AND creates significant, imminent risk to PHI confidentiality, integrity, or availability; or creates direct OCR enforcement exposure | Immediate remediation — stop ePHI processing through affected pathway until control is in place, or interim compensating control deployed within 72 hours |

**CRITICAL DEFICIENCY automatic triggers** (any one of these = CRITICAL):

1. No documented Security Risk Analysis (§ 164.308(a)(1)) — most common OCR finding
2. No designated Security Official (§ 164.308(a)(2))
3. No sanction policy (§ 164.308(a)(1)(ii)(C))
4. No BAA for a known active Business Associate
5. No incident response procedure (§ 164.308(a)(6))
6. No data backup plan (§ 164.308(a)(7)(ii)(A))
7. Unencrypted portable devices containing ePHI (highest breach risk)
8. Shared/generic accounts used for ePHI access (no unique user ID)
9. No individual right of access procedure despite patient requests received
10. Breach notification missed — no notification sent for an event that triggered the rule

#### 12b. Prioritization Framework

For all NON-COMPLIANT and PARTIAL findings, assign a remediation tier:

**IMMEDIATE** (within 2 weeks):

- All CRITICAL DEFICIENCY items
- Any missing BAA for active BA relationship
- Unencrypted portable devices or transmission paths for ePHI
- No documented Security Risk Analysis (if OCR audit is imminent or breach occurred)
- Missing or expired individual right of access response

**NEAR-TERM** (within 90 days):

- Risk Management Plan gaps (if Risk Analysis exists but no remediation tracking)
- Missing or inadequate training program
- Incomplete BAA inventory
- Audit log gaps or log review deficiencies
- Workstation security gaps
- Emergency access procedures not documented

**BACKGROUND** (within 6 months):

- Policy documentation gaps (policies exist but not formally written/approved)
- Media sanitization procedure formalization
- Privacy Rule procedural enhancements beyond minimum
- NPRM emerging requirements — readiness planning
- Annual evaluation planning

#### 12c. Citation Quality Gates

Before delivering any finding, run these 5 gates silently:

| Gate           | Rule                                                                                          | Fail Action                         |
| -------------- | --------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every compliance finding cites specific CFR section                                           | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All CFR citations follow standard format (45 CFR 164.xxx)                                     | Fix format                          |
| **Currency**   | Any cited OCR guidance or enforcement action verified as current                              | Flag "[CHECK CURRENCY]"             |
| **Domain**     | All findings are within HIPAA/HITECH scope; state-law findings marked [JURISDICTION-SPECIFIC] | Remove or flag scope bleed          |
| **Confidence** | Uncertainty explicitly stated; proposed NPRM requirements distinguished from final rules      | Add confidence qualifier            |

#### 12d. Self-Interrogation for CRITICAL DEFICIENCY Items

For each CRITICAL DEFICIENCY finding, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain**: Does this classification follow logically from the CFR text?
Would OCR actually cite this as a violation based on current enforcement precedent?

**Pass 2 — Completeness**: Have all relevant CFR sections been considered? Is there
a compensating control or alternative compliance pathway that was missed?

**Pass 3 — Challenge**: What is the strongest counterargument? Under what circumstances
might OCR accept the current state as compliant? (e.g., small CE with documented
rationale for Addressable specification alternative)

#### 12e. Confidence Scoring

| Level        | Range     | Meaning                                                | Action                            |
| ------------ | --------- | ------------------------------------------------------ | --------------------------------- |
| **Definite** | 0.95-1.0  | Clear CFR requirement, verified                        | State with confidence             |
| **High**     | 0.80-0.94 | Strong CFR basis, minor interpretation question        | State with brief caveat           |
| **Probable** | 0.60-0.79 | Good basis; OCR interpretation may vary                | State with reasoning and caveats  |
| **Possible** | 0.40-0.59 | Genuinely uncertain; depends on fact-specific analysis | Flag for attorney review          |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                | Do not assert; flag "[UNCERTAIN]" |

---

## Anti-Patterns

What NOT to do in a HIPAA compliance assessment or compliance program:

1. **Treating Addressable as optional** — The Required/Addressable distinction does NOT
   mean optional. Addressable means: implement the spec as reasonable and appropriate, OR
   document why it is not reasonable/appropriate AND implement an equivalent alternative.
   Failing to implement and failing to document the alternative is a violation.

2. **Vendor-provided checklist as the Security Risk Analysis** — A vendor-generated
   checklist (e.g., from an EHR company or compliance software) is NOT a Security Risk
   Analysis under 45 CFR 164.308(a)(1). The SRA must be specific to this organization's
   ePHI environment. OCR has rejected vendor checklists as inadequate in enforcement actions.

3. **Scope-limiting the SRA** — Conducting the SRA only for one system (e.g., just the EHR)
   and ignoring email, shared drives, cloud storage, laptops, or third-party systems.
   The SRA must cover ALL ePHI regardless of location or system.

4. **Stale risk analysis without updates** — Conducting a thorough SRA and then never
   updating it as technology, workforce, and threats change. OCR expects the SRA to be
   a living document, updated when material changes occur.

5. **Missing BAA for a known business associate** — Organizations routinely overlook
   IT support vendors, cloud providers, lawyers, and accountants. If they access PHI,
   they are a BA and need a BAA — regardless of whether their function feels non-medical.

6. **Outdated pre-HITECH BAAs** — BAAs executed before the 2013 Omnibus Rule do not
   reflect direct BA liability, subcontractor flow-down requirements, or breach notification
   obligations. These must be updated.

7. **No subcontractor flow-down** — A BA's subcontractors who receive ePHI are themselves
   BAs and need BAAs. The original CE's BAA must require the BA to execute BAAs with its
   own subcontractors (45 CFR 164.308(b)(4)).

8. **Shared accounts for ePHI access** — Creating shared accounts for ePHI systems (e.g.,
   "admin" or departmental accounts) violates the Unique User Identification requirement
   (§ 164.312(a)(2)(i)) and prevents audit trail tracing to individuals.

9. **Undocumented Addressable spec alternatives** — Choosing not to implement an
   Addressable specification without documenting the rationale and alternative control.
   If OCR asks, "Why didn't you implement automatic logoff?" the answer cannot be "It wasn't
   required" — the documentation of the alternative and rationale must exist.

10. **Training records not retained** — Training workforce on HIPAA without keeping records
    of who was trained, when, and on what. Documentation is itself a HIPAA requirement
    (§ 164.316(b)) and required to demonstrate compliance in an audit.

11. **Security incident log not maintained** — Failing to document and track security
    incidents (including minor ones that do not result in a reportable breach). 45 CFR
    164.308(a)(6) requires response AND reporting — and documentation of disposition.

12. **Breach assessment skipped on the assumption it "wasn't a breach"** — Treating every
    impermissible disclosure as non-reportable without conducting the four-factor risk
    assessment. The regulatory default is presumption of breach — the organization bears
    the burden of proving otherwise with documentation.

13. **Starting the 60-day clock from breach discovery, not from knowledge** — For CE-BA
    relationships, the CE's 60-day clock starts from the date the CE knows of the breach,
    NOT the date the BA discovered it. Delayed BA reporting does not extend the CE's clock.

14. **Privacy Notice not updated** — Using an outdated NPP that does not reflect current
    uses and disclosures (e.g., pre-2016 NPP that predates marketing exception updates,
    or post-COVID NPP that doesn't address telehealth).

15. **Right of access denied or delayed without valid basis** — OCR's Right of Access
    Initiative has resulted in dozens of enforcement actions and settlements for delayed,
    fee-excessive, or unjustified denials of patient record access requests.

16. **Minimum necessary not operationalized** — Having a policy that says "minimum
    necessary" without operationalizing it through role-based access controls, standard
    information release protocols, and individual review procedures.

17. **Encryption "too expensive" justification** — Arguing that encryption is not
    "reasonable and appropriate" due to cost without a genuine analysis. OCR has shown
    low tolerance for cost-based excuses after unencrypted device breaches, especially
    for laptops and portable media.

18. **No employee termination access revocation** — Failing to implement a timely
    process for revoking ePHI access for terminated employees. Former employees retaining
    access has resulted in multiple OCR enforcement actions for insider threat breaches.

19. **Treating remote workers differently** — Failing to extend physical and technical
    safeguards to remote workers who access ePHI from home. Remote workstations are in
    scope for § 164.310(b) Workstation Use and all Technical Safeguards.

20. **No annual evaluation** — Not conducting an annual Security Rule evaluation
    (§ 164.308(a)(8)). The evaluation requirement is separate from the SRA — it asks
    whether safeguards are still adequate given changes since the last SRA.

21. **Ignoring state law preemption analysis** — Assuming HIPAA compliance equals
    full compliance without checking state law. California CMIA, Texas MRPA, and 42 CFR
    Part 2 all impose stricter requirements in specific contexts.

22. **Applying HIPAA to de-identified data** — HIPAA applies to PHI. If data is properly
    de-identified under § 164.514 (Safe Harbor or Expert Determination), HIPAA does not
    apply — but the de-identification must be genuine and documented. Partial de-identification
    is not de-identification.

23. **Confusing Evaluation with Risk Analysis** — Treating the periodic evaluation required
    by § 164.308(a)(8) as identical to the risk analysis required by § 164.308(a)(1)(ii)(A).
    These are distinct requirements. The evaluation asks: are our security measures working
    and still appropriate? The risk analysis asks: what are our threats, vulnerabilities, and
    risk levels? Both are independently required. An organization can have a current evaluation
    and an outdated risk analysis — it is still non-compliant.

24. **Treating HIPAA as IT's Problem** — Assigning all HIPAA Security Rule responsibility
    to the IT department with no engagement from legal, compliance, HR, operations, or senior
    leadership. HIPAA is an organizational obligation requiring cross-functional governance.
    Administrative safeguards (training, sanctions, access management, contingency planning,
    evaluation) are not IT controls. An IT team cannot implement a sanction policy, a
    termination procedure, or a workforce training program without organizational buy-in and
    cross-functional ownership.

25. **Risk Identified but Never Mitigated** — Completing a thorough risk analysis that
    identifies serious vulnerabilities, documenting them, and then taking no remediation action.
    This is potentially worse than never conducting a risk analysis — it demonstrates awareness
    and willful neglect simultaneously. The Enzo Biochem case ($4.5M state AG settlement, 2024)
    is the definitive example: risks identified in 2017 and 2021 risk analyses were never
    remediated; ransomware exploited those exact vulnerabilities in 2023.

---

## Compliance Maturity Framework

Apply this 5-level maturity model to each HIPAA safeguard domain to calibrate assessment
depth and remediation investment. Adapted from HITRUST CSF maturity methodology.

| Level               | Name          | Description                                                                                                                                                                                                                       |
| ------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1 — Ad Hoc**      | Non-existent  | No documented policy or procedure. No consistent implementation. No ownership. Evidence cannot be produced. OCR would find this area non-compliant.                                                                               |
| **2 — Defined**     | Policy exists | Written policy exists but implementation is inconsistent. Controls may be in place for some systems but not universally applied. Organization would struggle to demonstrate compliance under audit.                               |
| **3 — Implemented** | Managed       | Policy implemented consistently across the organization. Controls technically deployed or procedurally enforced. Workforce trained. Evidence documentable. This is baseline HIPAA compliance.                                     |
| **4 — Monitored**   | Measured      | Compliance actively monitored. Metrics collected (training completion %, log review rate, access review findings). Exception management in place. Periodic evaluation drives documented improvement. This is OCR audit readiness. |
| **5 — Optimized**   | Continuous    | Compliance integrated into operational processes and continuously improved. Controls validated through testing (pen tests, tabletop exercises, restoration tests). Lessons learned drive program evolution.                       |

**Target maturity by domain**:

| HIPAA Domain                           | Minimum Viable | OCR Audit Ready | Leading Practice |
| -------------------------------------- | -------------- | --------------- | ---------------- |
| Risk Analysis (§ 164.308(a)(1))        | Level 3        | Level 4         | Level 5          |
| Risk Management                        | Level 3        | Level 4         | Level 5          |
| Sanction Policy                        | Level 3        | Level 4         | Level 4          |
| Audit Log Review                       | Level 3        | Level 4         | Level 5          |
| Workforce Training                     | Level 3        | Level 4         | Level 4          |
| BAA Program                            | Level 3        | Level 4         | Level 4          |
| Contingency Planning / Backup Testing  | Level 3        | Level 4         | Level 5          |
| Technical Safeguards (MFA, encryption) | Level 3        | Level 4         | Level 5          |
| Incident Response                      | Level 3        | Level 4         | Level 5          |
| Physical Safeguards                    | Level 3        | Level 3         | Level 4          |

Use this table to set realistic improvement targets — an organization at Level 2 across all
domains should prioritize reaching Level 3 before pursuing Level 4+ optimizations.

---

## Writing Standards

Before delivering the assessment output, apply these quality gates:

1. **Precision**: Every finding must cite the specific CFR section it relates to
2. **Distinction**: Proposed NPRM requirements are always distinguished from current law
3. **Actionability**: Every NON-COMPLIANT and PARTIAL finding includes a specific remediation action
4. **Evidence-grounding**: Every COMPLIANT finding identifies the evidence type that supports it
5. **Proportionality**: CRITICAL DEFICIENCY is reserved for genuine high-risk gaps — do not
   use it to underscore minor documentation gaps
6. **Plain language**: Avoid legal jargon where plain language communicates the same content;
   use jargon only where technical precision requires it
7. **Verified claims**: NPRM status, CMP amounts, and enforcement figures must be marked
   [VERIFY] unless verified via legalcode-mcp or confirmed primary source

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for: current OCR enforcement actions and resolution agreements
- Search for: NPRM finalization status (verify whether the 2025 Security Rule NPRM became final)
- Search for: current inflation-adjusted CMP amounts
- Search for: state-specific healthcare privacy law preemption analysis
- Save verified citations to `/tmp/hipaa-assessment-research.md`
- Mark citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark all CFR citations, CMP amounts, and enforcement references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag NPRM status as requiring special verification before advising on NPRM-based requirements

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-hipaa-compliance-assessment"
  assessment_date: "[date]"
  entity_name: "[Organization name or 'Not specified']"
  entity_type: "[Covered Entity — Healthcare Provider / Health Plan / Clearinghouse / Business Associate / Subcontractor BA]"
  jurisdiction: "United States (federal HIPAA; state law analysis: [specify states])"
  assessment_scope:
    security_rule: "[Full / Administrative only / Physical only / Technical only]"
    privacy_rule: "[Full / NPP only / Individual rights only / Not assessed]"
    breach_notification: "[Full / Infrastructure only / Not assessed]"
    baa_review: "[Full inventory / Sample / Not assessed]"
    nprm_readiness: "[Assessed / Not assessed]"
  phi_ephi_scope:
    systems_inventoried: "[number or 'Not inventoried']"
    cloud_environments: "[Yes/No — provider(s)]"
    mobile_devices: "[Yes/No]"
    remote_access: "[Yes/No]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/hipaa-assessment-research.md or 'Not created'"
  nprm_status: "PROPOSED only — regulatory freeze as of March 2026 [VERIFY current status]"
  nist_guidance: "NIST SP 800-66r2 (February 2024) — OCR-endorsed, not legally binding"
  prior_sra_exists: "[Yes — date / No / Unknown]"
  critical_deficiencies_found: "[number]"
  non_compliant_findings: "[number]"
  partial_findings: "[number]"
  compliant_findings: "[number]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "Assessment based on information provided — undisclosed ePHI systems or processes may create additional gaps"
    - "NPRM requirements distinguished from current law — verify finalization status before treating as binding"
    - "State law preemption analysis requires jurisdiction-specific legal review"
    - "SRA framework produced here requires human-led execution — not a substitute for a qualified risk analyst"
  reviewer: "AI-assisted — requires review by qualified HIPAA compliance professional or healthcare attorney"
```

---

## Output Format Template

Deliver the assessment in this format:

```markdown
# HIPAA Compliance Assessment — [Organization Name]

**Assessment Date**: [date]
**Entity Type**: [CE type / BA]
**Scope**: [Security Rule / Privacy Rule / Breach Notification / Full]
**Assessed by**: AI-assisted framework (legalcode-hipaa-compliance-assessment) — for professional review

---

## Executive Summary

| Category                       | Finding Count | Critical | Non-Compliant | Partial | Compliant |
| ------------------------------ | ------------- | -------- | ------------- | ------- | --------- |
| Security Rule — Administrative |               |          |               |         |           |
| Security Rule — Physical       |               |          |               |         |           |
| Security Rule — Technical      |               |          |               |         |           |
| Business Associate Agreements  |               |          |               |         |           |
| Privacy Rule                   |               |          |               |         |           |
| Breach Notification            |               |          |               |         |           |
| **TOTAL**                      |               |          |               |         |           |

**Overall Posture**: [COMPLIANT / REQUIRES IMPROVEMENT / NON-COMPLIANT / AT-RISK]

**Immediate Actions Required**: [List any CRITICAL DEFICIENCYs — 1-3 sentences each]

---

## Finding Detail

### [1] [Finding Title]

- **Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
- **CFR Basis**: [45 CFR 164.xxx]
- **Current State**: [What was found]
- **Gap**: [What is missing or inadequate]
- **Remediation**: [Specific action required]
- **Priority**: [IMMEDIATE / NEAR-TERM / BACKGROUND]
- **Evidence Required**: [What documentation would demonstrate compliance]
- **Confidence**: [Definite / High / Probable] — [brief rationale]

[Repeat for each finding]

---

## Business Associate Agreement Assessment

| Business Associate | BAA on File | Date   | All Required Provisions  | Issues   |
| ------------------ | ----------- | ------ | ------------------------ | -------- |
| [BA name]          | Yes/No      | [date] | Complete/Partial/Missing | [issues] |

---

## Security Risk Analysis Status

**SRA Status**: [Completed/date / Not completed / Unknown]
**SRA Scope**: [ePHI systems covered]
**Last Updated**: [date or N/A]
**SRA Gaps Identified**: [list]
**OCR Audit Readiness**: [Ready / Partial / Not ready]

---

## NPRM Readiness Snapshot [VERIFY finalization status]

| Proposed Requirement          | Gap   | Readiness Timeline |
| ----------------------------- | ----- | ------------------ |
| Mandatory MFA all ePHI        | [gap] | [timeline]         |
| Mandatory encryption at rest  | [gap] | [timeline]         |
| 72-hour restoration           | [gap] | [timeline]         |
| Annual penetration testing    | [gap] | [timeline]         |
| Quarterly vulnerability scans | [gap] | [timeline]         |

---

## Remediation Roadmap

### Immediate (0–2 weeks)

- [ ] [Action 1] — Responsible: [role] — CFR: [cite]
- [ ] [Action 2]

### Near-Term (2 weeks–90 days)

- [ ] [Action 3]
- [ ] [Action 4]

### Background (3–6 months)

- [ ] [Action 5]
- [ ] [Action 6]

---

## Glass Box Audit Trail

[Paste completed Glass Box YAML template]

---

## Recommended Next Steps

1. Engage qualified HIPAA compliance professional or healthcare attorney to review findings
2. Execute Security Risk Analysis using this framework as a guide, with human expert oversight
3. Address CRITICAL DEFICIENCY items before processing additional ePHI through affected systems
4. Update BAA inventory and execute missing BAAs within 30 days
5. Establish annual HIPAA Security Rule evaluation cycle (§ 164.308(a)(8))
6. Monitor 2025 NPRM status — [VERIFY] and adjust compliance roadmap when finalized

**Disclaimer**: This assessment does not constitute legal advice and is not a substitute
for a formal compliance audit by a qualified auditor. All findings should be reviewed by
a healthcare attorney or certified HIPAA compliance professional before action.
```

---

## Localization Notes

This skill is US-specific (HIPAA is a federal US statute). When working alongside
international privacy obligations:

- **GDPR + HIPAA overlap**: Healthcare organizations processing EU patients' data may
  need both GDPR compliance (use `legalcode-dpa-review-and-negotiation`) and HIPAA.
  The DPA (GDPR) and BAA (HIPAA) serve related but legally distinct purposes.
- **42 CFR Part 2**: Substance use disorder records are subject to stricter requirements
  than HIPAA — cannot be re-disclosed without patient authorization even for TPO.
  Flag any SUD treatment context for specialized analysis.
- **State law**: HIPAA preempts contrary state law but not more-protective state law.
  California (CMIA), Texas (MRPA), and many other states have healthcare-specific privacy
  laws that impose additional obligations — always conduct state law preemption analysis.

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis incorporating:

- Complete 45 CFR Part 164 Security Rule standards and implementation specifications (Subpart C)
- 45 CFR Part 164 Privacy Rule (Subpart E) individual rights and key obligations
- 45 CFR Part 164 Breach Notification Rule (Subpart D) four-factor risk assessment
- HITECH Act (Pub. L. 111-5) BA liability and enforcement enhancements
- HHS OCR Security Risk Analysis Initiative enforcement findings (2024-2025)
- NIST SP 800-66r2 (February 2024) — Implementing the HIPAA Security Rule
- HHS NPRM January 6, 2025 (89 Fed. Reg. 9954) — proposed Security Rule amendments
- OCR enforcement resolution agreements and CMP determinations (2020-2025)
- NIS2 compliance assessment structural pattern adapted for US healthcare regulatory context
- legalcode-contract-review quality framework (Citation Quality Gates, Self-Interrogation,
  Confidence Scoring, Glass Box audit trail, Anti-patterns)
- Related Legalcode skills: hipaa-breach-notification-operations, legalcode-vendor-privacy-assessment,
  legalcode-incident-response-plan-builder, legalcode-us-breach-notification-triage
