---
name: legalcode-soc2-readiness-assessment
description: Assess SOC 2 Type I and Type II readiness across all five AICPA Trust Service Criteria (Security,
  Availability, Processing Integrity, Confidentiality, Privacy). Use when a SaaS company, cloud service
  provider, managed service provider, or other service organization needs to determine readiness for a
  SOC 2 audit, identify control gaps, build a remediation roadmap, or understand how SOC 2 maps to ISO
  27001, NIST CSF, HIPAA, or PCI DSS.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess SOC 2 Type I and Type II readiness across all five AICPA Trust Service Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy). Use when a SaaS company, cloud service provider, managed service provider, or other service organization needs to determine readiness for a SOC 2 audit, identify control gaps, build a remediation roadmap, or understand how SOC 2 maps to ISO 27001, NIST CSF, HIPAA, or PCI DSS. Covers all Common Criteria (CC1–CC9), optional TSC criteria (A, PI, C, P series), evidence collection requirements per control, management assertion obligations under AT-C Section 205, subservice organization carve-out vs. inclusive method, and Complementary User Entity Controls (CUECs). Produces a COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL DEFICIENCY classification per control domain, prioritized remediation roadmap, cross-framework gap analysis, and auditor-ready evidence inventory. Also use when reviewing a vendor's SOC 2 report as a user entity, evaluating SOC 2 scope adequacy, or assessing bridge letter sufficiency.


# Legalcode SOC 2 Readiness Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted SOC 2 readiness
> analysis. It does not constitute legal or accounting advice and does not substitute
> for an examination conducted by a licensed CPA firm under AICPA attestation standards.
> All outputs should be reviewed by qualified professionals — including a CPA firm
> and an information security practitioner — before reliance. The AICPA Trust Service
> Criteria and related guidance evolve; verify current applicability of all referenced
> standards. Statutory and regulatory references carry hallucination risk — verify
> against AICPA publications and authoritative sources before acting on them.

---

## Purpose and Scope

This skill assesses a service organization's readiness for a SOC 2 Type I or Type II
examination under the AICPA 2017 Trust Service Criteria (TSC), with 2022 points of
focus updates.

**Covers:**

- Readiness assessment across all five Trust Service Criteria categories
- Gap identification against each Common Criteria (CC1–CC9) and optional TSC criteria
- Evidence sufficiency review (what exists vs. what auditors will require)
- Remediation roadmap with prioritization by risk and audit timeline
- Framework crosswalk: SOC 2 ↔ ISO 27001, NIST CSF, HIPAA, PCI DSS
- Subservice organization scope decisions (carve-out vs. inclusive method)
- System description completeness review (management assertion readiness)
- User entity perspective: reviewing a vendor's SOC 2 report for adequacy
- Bridge letter assessment for expired or gap-period reports

**Does not:**

- Issue a SOC 2 opinion or formal attestation (only licensed CPA firms may do this)
- Provide legal advice or replace qualified counsel
- Substitute for a qualified auditor's judgment on control design or operating effectiveness
- Cover SOC 1 (financial reporting controls) or SOC 3 (public-use summary reports)

---

## Jurisdiction and Governing Law

SOC 2 is a US-origin standard governed by the AICPA (American Institute of Certified
Public Accountants) under AT-C Section 205 (Examination Engagements) and the 2017
Trust Service Criteria for Security, Availability, Processing Integrity, Confidentiality,
and Privacy.

**Global applicability:** SOC 2 is accepted globally as a security and compliance
credential. Enterprise customers in North America, Europe, Asia-Pacific, and the Middle
East routinely require SOC 2 Type II from SaaS vendors. It is not legally mandated in
most jurisdictions but is contractually required in enterprise procurement.

[JURISDICTION-SPECIFIC] **Regulatory intersections vary by jurisdiction:**

- **US healthcare**: HIPAA Security Rule (45 CFR Part 164) overlaps substantially with
  CC6/CC7; a SOC 2 does not substitute for HIPAA compliance but a combined assessment
  reduces effort.
- **EU/UK data protection**: GDPR (Reg. 2016/679) and UK GDPR require technical and
  organisational measures; SOC 2 Security + Confidentiality + Privacy criteria provide
  a strong evidence base for Art. 32 compliance but are not equivalent.
- **US financial services**: SOC 2 overlaps with GLBA Safeguards Rule (16 CFR Part 314)
  and NYDFS Cybersecurity Regulation (23 NYCRR 500).
- **US federal contractors**: FedRAMP (NIST SP 800-53 Rev. 5) has a higher bar than SOC 2;
  a SOC 2 is not a substitute but is a useful precursor.
- **PCI scope**: SOC 2 does not substitute for PCI DSS but organizations pursuing both
  benefit from significant control overlap.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The audit scope (which TSC to include) affects the depth of analysis
- Type I vs. Type II determines the evidence standard being assessed
- Subservice organization decisions change scope materially
- The user's role (service organization vs. user entity) changes the analytical lens

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

### Step 1: Accept Input

Accept input in any of these formats:

- **Current controls documentation**: Policy library, control inventory, evidence samples
- **Existing SOC 2 report**: For gap analysis vs. next audit cycle or user entity review
- **Questionnaire responses**: Completed security questionnaire or internal audit findings
- **Free-text description**: Organization's current control environment as described
- **No input yet**: Prompt the user to describe their control environment or upload documents

### Step 2: Establish Scope and Context

**⟁ CLARIFY** — Before beginning the assessment, gather this context:

1. **Audit type target**:
   - Options: **Type I** (design of controls at a point in time), **Type II** (design +
     operating effectiveness over an observation period), **Not yet decided — advise me**
   - _Why this matters_: Type II requires evidence spanning the full observation period;
     Type I only assesses control design. The evidence standard differs substantially.

2. **Trust Service Criteria in scope**:
   - Options: **Security only** (minimum required), **Security + Availability**,
     **Security + Confidentiality**, **Security + Availability + Confidentiality**,
     **All five (Security, Availability, Processing Integrity, Confidentiality, Privacy)**,
     **Help me determine which apply**
   - _Why this matters_: Including optional criteria adds scope and cost; the right set
     depends on service commitments made to customers.

3. **Organization profile**:
   - Business model: SaaS, cloud infrastructure, managed services, data processing,
     financial services technology, healthcare technology, other
   - Employee count and approximate infrastructure scale
   - Primary cloud platforms in scope (AWS, Azure, GCP, on-premise, hybrid)
   - _Why this matters_: Calibrates the depth of analysis for each control domain and
     identifies which cloud-native controls need examination.

4. **Timeline and audit target**:
   - Options: **Audit in < 3 months** (urgent), **Audit in 3–6 months** (standard),
     **Audit in 6–12 months** (planning phase), **No firm date — strategic assessment**
   - _Why this matters_: Determines whether to surface all gaps or focus on critical
     gaps that could cause a qualified opinion.

5. **Prior SOC 2 history**:
   - Options: **First-time audit**, **Renewing existing SOC 2 (specify last audit date)**,
     **Have Type I, preparing for Type II**, **Reviewing a vendor's SOC 2 report**
   - _Why this matters_: First-time audits need foundational work; renewals focus on
     operating effectiveness evidence continuity; vendor review uses a different analytical lens.

6. **Subservice organizations**:
   - List any third-party infrastructure or service providers that are in scope
     (e.g., AWS, Stripe, Twilio, Salesforce, a payroll processor)
   - _Why this matters_: Determines whether to use carve-out method (most common) or
     inclusive method, and whether CSOCs are needed.

### Step 3: Gather Legal and Regulatory Authority

Use **legalcode-mcp** to search for:

- Current AICPA Trust Service Criteria and any published amendments or points of focus updates
- Applicable regulatory overlays (HIPAA if healthcare data, GLBA if financial data,
  GDPR if EU personal data is processed)
- Relevant guidance from the AICPA on SOC 2 system descriptions and management assertions
- Any jurisdiction-specific regulatory requirements that interact with the SOC 2 scope

Save results to `/tmp/legalcode-soc2-authority.md`:

```markdown
# SOC 2 Legal Authority Reference

## Date: [date]

## Organization: [name]

## TSC in Scope: [list]

### AICPA Standards

- [Standard, publication, relevance]

### Regulatory Overlays

- [Regulation, jurisdiction, interaction with SOC 2]

### Recent Guidance

- [Guidance, date, impact on scope/evidence]
```

**If legalcode-mcp is not connected:**

- Proceed with general SOC 2 knowledge and flag all statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Step 4: Determine Applicable TSC and Criteria

Based on the scope established in Step 2, map the applicable criteria:

**Always applicable (Security):** CC1–CC9 (61 points of focus across the Common Criteria)

**Conditionally applicable:**
| TSC | Include When | Key Indicator |
|-----|-------------|---------------|
| **Availability (A series)** | Service commitments include uptime, SLA, or disaster recovery | Customer contracts promise uptime percentages or recovery time objectives |
| **Processing Integrity (PI series)** | Service involves transaction processing, data accuracy, or completeness commitments | Financial data processing, order management, payroll, clinical data processing |
| **Confidentiality (C series)** | Designated confidential information is processed beyond PII | Legal data, IP, financial models, trade secrets in the service scope |
| **Privacy (P series)** | Personal information is collected, used, retained, disclosed, or disposed of | Any PII processing; note GAPP-based criteria are distinct from GDPR |

**⟁ CLARIFY** — If the applicable TSC are unclear, present the customer contract's service commitments to the user and ask which apply.

### Step 5: Control Environment Assessment — CC1–CC9

Assess each of the nine Common Criteria domains. For each domain, identify:

- **Controls in place**: What exists (documented, implemented, operating)
- **Evidence available**: What evidence can be produced for an auditor
- **Gaps**: Controls that are absent, undocumented, or have evidence deficiencies
- **Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

---

#### CC1: Control Environment

**What auditors assess:** Governance and oversight structures; integrity and ethical values; organizational commitment to security; board-level accountability; authority assignment; human resources practices; background checks.

**Key controls to verify:**

- [ ] Security governance policy with named CISO or security owner
- [ ] Board or executive committee with documented security oversight
- [ ] Code of conduct with security provisions, signed by all employees
- [ ] Background screening policy with documented execution for new hires
- [ ] Security reporting lines documented (org chart)
- [ ] Security training program with completion tracking
- [ ] Annual performance evaluation incorporating security responsibilities

**Common deficiencies:**

- No identifiable security owner or CISO function
- Board/executive oversight of security undocumented
- Code of conduct exists but no acknowledgment records
- Background checks performed inconsistently or undocumented
- Training records missing or not linked to individual employees

**Evidence the auditor will request (Type II):**
Training completion reports, signed code of conduct acknowledgments (per period), board/security committee meeting minutes referencing security, org chart, background check policy + sample records from the observation period.

---

#### CC2: Communication and Information

**What auditors assess:** Quality and availability of information for decision-making; internal communication of policies and objectives; external communication of security commitments to customers and regulators; monitoring of information received from external parties.

**Key controls to verify:**

- [ ] Published security/trust page or customer-facing security documentation
- [ ] Privacy policy and/or terms of service addressing security commitments
- [ ] Internal security policy distribution mechanism
- [ ] Process for communicating material security changes to customers
- [ ] Mechanism for receiving and acting on external security communications (vulnerability disclosures, regulator inquiries)
- [ ] Incident communication procedures (internal escalation + customer notification)

**Common deficiencies:**

- No public trust page or security documentation
- Security policies not distributed to employees on a documented schedule
- No defined process for customer security notifications
- Vulnerability disclosure program absent

---

#### CC3: Risk Assessment

**What auditors assess:** Risk identification and analysis; fraud risk assessment; assessment of changes in the risk environment (new vendors, technology, personnel, regulatory changes); use of risk assessment output to select control activities.

**Key controls to verify:**

- [ ] Formal risk assessment methodology documented
- [ ] Annual (minimum) risk assessment completed and dated
- [ ] Risk register with assets, threats, likelihood, impact, risk rating, owner, and disposition
- [ ] Fraud risk explicitly considered in the assessment
- [ ] Change-triggered reassessment process (new product, new vendor, M&A, major personnel change)
- [ ] Risk assessment output linked to control selection and remediation tracking

**Common deficiencies:**

- Risk assessment completed once and never updated
- No documented methodology (likelihood × impact scoring)
- Risks enumerated but no remediation tracking
- Fraud risk not explicitly addressed
- No process to trigger reassessment when material changes occur

**Evidence the auditor will request:**
Risk assessment document with date, methodology, and signatory; risk register with current ratings; evidence of annual review; remediation tracking records.

---

#### CC4: Monitoring Activities

**What auditors assess:** Ongoing and separate evaluations to assess whether controls are present and functioning; communication of deficiencies to those responsible for corrective action; internal audit or third-party evaluation activities.

**Key controls to verify:**

- [ ] Vulnerability scanning (internal and external) on documented frequency (≥ quarterly)
- [ ] Annual penetration test by qualified third party, results documented
- [ ] Penetration test findings tracked to remediation with owners and target dates
- [ ] Continuous monitoring tooling (SIEM, cloud security posture management)
- [ ] Internal audit or SOC 2 readiness review function
- [ ] Deficiency tracking and escalation to senior management

**Common deficiencies:**

- No annual penetration test (or test was performed but results not documented)
- Penetration test findings untracked or unremediated after 12+ months
- Vulnerability scanning absent or performed ad hoc
- No continuous monitoring (reliance on periodic snapshots only)
- No formal mechanism to escalate deficiencies to management

---

#### CC5: Control Activities

**What auditors assess:** Policies and procedures that ensure management directives are carried out; technology controls (automated enforcement); segregation of duties; transaction authorization; physical controls.

**Key controls to verify:**

- [ ] Policy library complete (see required policies list below)
- [ ] All policies have version numbers, approval dates, and named approvers
- [ ] Policies formally reviewed on defined schedule (annually minimum)
- [ ] Segregation of duties enforced: developers cannot deploy directly to production
- [ ] Change authorization controls (no changes without approval)
- [ ] Exception management process for policy deviations (documented, approved, time-limited)

**Required policy library minimum:**
| Policy | Status | Last Reviewed | Owner |
|--------|--------|---------------|-------|
| Information Security Policy | | | |
| Acceptable Use Policy | | | |
| Access Control Policy | | | |
| Change Management Policy | | | |
| Incident Response Policy | | | |
| Data Classification Policy | | | |
| Vendor Management / Third-Party Risk Policy | | | |
| Business Continuity / Disaster Recovery Policy | | | |
| Risk Assessment Policy | | | |
| Password / Authentication Policy | | | |
| Physical Security Policy | | | |
| Encryption / Key Management Policy | | | |

**Common deficiencies:**

- Policies exist as drafts without formal approval
- No version control or review history
- Developers have direct production database access (SOD failure)
- Policies communicated but no acknowledgment evidence

---

#### CC6: Logical and Physical Access Controls

**What auditors assess:** User registration and authorization; logical access restrictions (least privilege); authentication mechanisms (MFA); logical access to infrastructure; physical access controls; data encryption (at rest and in transit); data disposal.

This is the **most frequently cited deficiency category** in SOC 2 audits.

**Key controls to verify:**

- [ ] User provisioning process with documented approval (tickets, forms)
- [ ] Access review performed on documented frequency (quarterly recommended) with sign-off evidence
- [ ] Termination/deprovisioning: access removed within defined SLA (e.g., same-day for voluntary departures)
- [ ] MFA enforced for all in-scope systems (cloud console, VPN, SSO, admin interfaces)
- [ ] Privileged access inventory documented and reviewed
- [ ] No shared accounts or generic credentials
- [ ] Encryption at rest for all in-scope data stores (database-level or file-system-level)
- [ ] Encryption in transit (TLS 1.2+ minimum; TLS 1.3 preferred)
- [ ] Physical access logs maintained for server rooms/data center facilities
- [ ] Key management policy and documented key rotation schedule
- [ ] Data disposal / media sanitization procedures (NIST 800-88 or equivalent)

**Common deficiencies (CRITICAL DEFICIENCY triggers):**

- MFA not enforced on cloud infrastructure consoles or production environments
- Access reviews not performed per policy frequency
- Terminated employee accounts not removed within the policy SLA
- Unencrypted data stores in production containing sensitive data
- Shared admin credentials across multiple personnel
- No access review evidence for the observation period (Type II)

**For Type II:** Auditors expect to see evidence of access reviews for every cycle within the observation period. A single access review record for a 12-month period with a stated quarterly review frequency is a significant deficiency.

---

#### CC7: System Operations

**What auditors assess:** Detection of vulnerabilities and threats; monitoring for anomalies; evaluation and implementation of security patches; incident detection and response; identification and remediation of malware; management of physical environments.

**Key controls to verify:**

- [ ] SIEM or centralized log aggregation in place
- [ ] Log retention policy (minimum 90 days online; 12 months archived is common)
- [ ] Alerting rules for anomalous activity (failed logins, privilege escalation, data exfiltration patterns)
- [ ] Vulnerability management program: scan → triage → patch → verify
- [ ] Patch management SLAs (e.g., critical patches within 14 days)
- [ ] Endpoint protection (EDR/antivirus) on all in-scope endpoints
- [ ] Incident response plan with defined roles (incident commander, communications lead, legal)
- [ ] IR tabletop exercise completed and documented annually
- [ ] Security incident log maintained
- [ ] DDoS mitigation and web application firewall (WAF) in place

**Common deficiencies:**

- No centralized log management or logging gaps in production systems
- No documented incident response plan or plan is a template not customized to the organization
- No evidence of IR tabletop testing
- Patch management informal (no documented SLAs, no tracking of open vulnerabilities)
- SIEM alerts configured but not reviewed or actioned

---

#### CC8: Change Management

**What auditors assess:** Change authorization and approval; testing prior to deployment; system development lifecycle (SDLC) controls; emergency change procedures; configuration management; infrastructure-as-code controls.

**Key controls to verify:**

- [ ] All code changes reviewed via pull request (PR) process with at least one independent approver
- [ ] No direct commits to main/production branches (branch protection enforced)
- [ ] Change tickets created in issue tracker (Jira, ServiceNow, Linear, etc.) for all changes
- [ ] Deployment pipeline includes automated testing (unit, integration, security scanning)
- [ ] Separate development, staging, and production environments
- [ ] Emergency/hotfix procedure documented, approved by named authority, and post-hoc reviewed
- [ ] Configuration baselines documented and deviations tracked
- [ ] Release management process with rollback capability

**Common deficiencies:**

- No code review requirement enforced (developers can merge their own PRs)
- No separation between development and production environments
- Emergency changes made without documentation or approval
- CI/CD pipeline exists but security scanning (SAST/SCA) not included
- Infrastructure changes made via console without tracking (shadow IT in cloud)

---

#### CC9: Risk Mitigation — Vendors and Business Disruption

**What auditors assess:** Third-party risk management (vendor due diligence and monitoring); business disruption and continuity planning; insurance; risk transfer mechanisms.

**Key controls to verify:**

- [ ] Vendor inventory (all vendors with access to in-scope data or systems)
- [ ] Vendor risk tiering (critical, high, medium, low based on data access and criticality)
- [ ] Annual vendor risk assessment for critical/high-tier vendors
- [ ] Vendor SOC reports collected and reviewed for critical subservice organizations
- [ ] Data processing agreements (DPAs) in place with all vendors processing in-scope data
- [ ] Business continuity plan (BCP) documented and tested
- [ ] Disaster recovery (DR) plan documented, with defined RPO/RTO
- [ ] DR test completed at defined frequency (annually minimum) with documented results
- [ ] Cyber insurance in place with appropriate coverage limits
- [ ] Business interruption insurance assessment

**Common deficiencies:**

- No vendor inventory or risk tiering
- Vendor SOC 2 reports not collected or reviewed
- No DPAs in place with cloud infrastructure vendors
- BCP/DR plan documented but never tested
- DR test results not documented

---

### Step 6: Optional TSC Assessment

Assess additional criteria only if in scope (as determined in Step 4).

#### Availability (A Series)

**Key controls:**

- [ ] Uptime monitoring with alerting (e.g., Pingdom, Datadog, CloudWatch)
- [ ] SLA commitments documented in customer contracts and achievable based on architecture
- [ ] Capacity planning process to anticipate and address growth
- [ ] Redundancy and failover architecture (multi-AZ, load balancing, auto-scaling)
- [ ] DR test results demonstrating achievement of documented RTO/RPO
- [ ] Scheduled maintenance procedures with customer notification

**Common deficiencies:** SLA commitments not backed by monitoring evidence; no capacity planning; DR plan tested but RTO/RPO not achieved in tests.

#### Processing Integrity (PI Series)

**Key controls:**

- [ ] Input validation controls (data type, format, range, completeness checks)
- [ ] Processing controls (error handling, exception logging, reconciliation)
- [ ] Output controls (completeness checks, accuracy verification)
- [ ] Transaction integrity mechanisms (atomic commits, rollback capability)
- [ ] Data quality monitoring and exception reports reviewed regularly

**Common deficiencies:** No input validation causing silent data corruption; no reconciliation process for transaction processors; error logs exist but not reviewed.

#### Confidentiality (C Series)

**Key controls:**

- [ ] Data classification policy with defined categories (confidential, restricted, internal, public)
- [ ] Confidential data inventory and data mapping
- [ ] Access controls specifically governing confidential data (need-to-know enforcement)
- [ ] DLP (data loss prevention) controls or compensating controls
- [ ] Confidential data destruction procedures (retention schedule + disposal SLA)
- [ ] NDA requirements for personnel and vendors with access to confidential data

**Common deficiencies:** No data classification scheme; confidential data not inventoried; DLP absent with no compensating controls documented.

#### Privacy (P Series)

**Key controls (based on AICPA GAPP):**

- [ ] Privacy notice / privacy policy (collection, use, retention, disclosure, disposal of PII)
- [ ] Consent mechanisms for PII collection where required
- [ ] Data subject rights process (access, correction, deletion) with documented SLAs
- [ ] Data retention schedule with automated enforcement where possible
- [ ] Privacy incident response procedures (linked to general IR plan)
- [ ] Cross-border data transfer controls (SCCs, BCRs, adequacy decisions)
- [ ] Privacy training for personnel handling PII
- [ ] Privacy impact assessment process for new products or changes affecting PII

**Common deficiencies:** Privacy policy does not reflect actual data practices; no data retention enforcement (data kept indefinitely); no documented DSR (data subject request) handling process; training records absent.

---

### Step 7: Framework Crosswalk Analysis

Map the organization's current control posture to other frameworks as requested.

#### SOC 2 ↔ ISO 27001:2022 Crosswalk

| SOC 2 Domain                  | ISO 27001:2022 Controls                                               |
| ----------------------------- | --------------------------------------------------------------------- |
| CC1 (Control Environment)     | A.5.1–5.4 (Policies), A.6.1–6.7 (People), A.5.2 (IS Roles)            |
| CC2 (Communication)           | A.5.1 (Policies), A.8.2 (IS awareness), A.5.14 (Information transfer) |
| CC3 (Risk Assessment)         | Clause 6.1 (Risk treatment), A.5.7 (Threat intelligence)              |
| CC4 (Monitoring)              | A.5.35–5.36 (Independent review), A.8.8 (Vuln. management)            |
| CC5 (Control Activities)      | A.5.10–5.15 (Access/asset controls), A.8.3–8.11 (Technical controls)  |
| CC6 (Logical Access)          | A.5.15–5.18 (Access management), A.8.3–8.5 (Auth/MFA/privilege)       |
| CC7 (System Operations)       | A.8.15–8.16 (Logging/monitoring), A.5.24–5.26 (Incident management)   |
| CC8 (Change Management)       | A.8.19–8.32 (Change/dev/config management)                            |
| CC9 (Risk Mitigation/Vendors) | A.5.19–5.22 (Supplier security), A.5.29–5.30 (BCP/DR)                 |
| Availability                  | A.5.29–5.30 (BCP/DR), A.8.6 (Capacity management)                     |
| Confidentiality               | A.5.12–5.13 (Data classification), A.8.12 (DLP)                       |
| Privacy                       | A.5.34 (Privacy/PII)                                                  |

**ISO 27001 certification benefit:** Organizations with ISO 27001 certification have significant overlap with SOC 2 CC1–CC9. Common gaps include: SOC 2 system description requirements not addressed by ISO 27001; AICPA-specific evidence formats; management assertion requirement.

#### SOC 2 ↔ NIST CSF 2.0 Crosswalk

| NIST CSF 2.0 Function | Relevant SOC 2 Domain      |
| --------------------- | -------------------------- |
| GOVERN (GV)           | CC1, CC2, CC3              |
| IDENTIFY (ID)         | CC3, CC9                   |
| PROTECT (PR)          | CC5, CC6, CC8              |
| DETECT (DE)           | CC4, CC7                   |
| RESPOND (RS)          | CC7                        |
| RECOVER (RC)          | CC7, Availability criteria |

#### SOC 2 ↔ HIPAA Security Rule [JURISDICTION-SPECIFIC: US healthcare only]

| HIPAA Safeguard Category                 | SOC 2 Mapping                | Gap                                                                                           |
| ---------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------- |
| Administrative Safeguards (§164.308)     | CC1, CC3, CC4, CC5, CC7, CC9 | HIPAA requires Security Risk Analysis specifically for ePHI; SOC 2 risk assessment is broader |
| Physical Safeguards (§164.310)           | CC6 (physical access)        | HIPAA workstation use controls are more prescriptive                                          |
| Technical Safeguards (§164.312)          | CC6 (access/encryption), CC7 | HIPAA audit log requirements for ePHI access are more specific                                |
| Business Associate Agreements (§164.504) | CC9 (vendor management)      | HIPAA BAA has specific required provisions beyond standard DPA                                |

**Key gap:** SOC 2 Privacy criteria are based on AICPA GAPP, not HIPAA Privacy Rule (45 CFR Part 164 Subpart E). Including Privacy TSC does not satisfy HIPAA Privacy Rule obligations.

#### SOC 2 ↔ PCI DSS v4.0 [JURISDICTION-SPECIFIC: Payment card industry only]

SOC 2 Security + Availability + Confidentiality overlaps with approximately 60–70% of PCI DSS v4.0 requirements. Key PCI-specific gaps not fully addressed by SOC 2:

- PCI Requirement 1 (Network segmentation — firewall/router configuration standards)
- PCI Requirement 3 (Cardholder data protection — specific tokenization/truncation requirements)
- PCI Requirement 6.3 (Web application security — specific WAF configuration requirements)
- PCI Requirement 9 (Physical media controls for cardholder data)
- PCI Requirement 11.3 (Penetration testing methodology — scoping is more prescriptive)
- Quarterly ASV scanning requirement (PCI-specific obligation)

---

### Step 8: Subservice Organization Scope Assessment

**⟁ CLARIFY** — Identify all subservice organizations (vendors providing services that are
part of the in-scope system) and determine the scoping method:

**Carve-out method (most common):**

- The service organization excludes the subservice organization from its system description
- The report notes that Complementary Subservice Organization Controls (CSOCs) must be
  in place at the subservice organization
- The service organization should obtain and review the subservice organization's SOC 2
  report annually
- Common carved-out subservice organizations: AWS, Azure, GCP, Stripe, Twilio, Salesforce

**Inclusive method (less common):**

- The subservice organization is included in the service organization's system description
- The auditor must audit controls at both entities
- Requires cooperation from the subservice organization
- Rarely practical for major cloud infrastructure providers

**System description requirements for carve-out:**

- Identify all subservice organizations by name
- Describe each subservice organization's role in the service
- List all CSOCs — controls the system description assumes are in place at each subservice organization
- Confirm the service organization has reviewed the subservice organization's SOC report within the last 12 months

**Complementary User Entity Controls (CUECs):**
These are controls the system description assumes are implemented by user entities (customers).
Common CUECs include:

- User entities must configure MFA for their users on the platform
- User entities must disable access for terminated personnel within one business day
- User entities must transmit only encrypted data to the service
- User entities must approve changes to configurations prior to implementation
- User entities must maintain up-to-date endpoint protection on devices accessing the service

**⟁ CLARIFY** — Review the organization's current system description (if any) and confirm:

1. Are all subservice organizations identified?
2. Are CSOCs accurately described for each?
3. Are CUECs complete and accurate (not over- or under-specified)?

---

### Step 9: System Description and Management Assertion Readiness

The SOC 2 report includes a system description (Section IV) authored by management. Assess its completeness:

**Required components of the system description:**

- [ ] Services provided and commitments made to customers
- [ ] System components (infrastructure, software, people, procedures, data)
- [ ] System boundaries (what is in and out of scope)
- [ ] Principal service commitments and system requirements (mapped to TSC)
- [ ] Controls designed to provide reasonable assurance of meeting commitments
- [ ] Subservice organizations and their roles (carve-out or inclusive)
- [ ] CUECs and CSOCs
- [ ] Changes to the system during the period (Type II)
- [ ] Significant subsequent events

**Management assertion (AT-C Section 205.16):**
Management must assert in writing that:

1. The system description fairly presents the system as designed and implemented
2. The controls described were suitably designed (Type I + Type II)
3. The controls operated effectively throughout the specified period (Type II only)

The assertion is signed by senior management (CEO, CTO, CISO, or equivalent) and is
Section II of the formal SOC 2 report.

**⟁ CLARIFY** — If no system description exists, ask whether to produce a draft or
identify only the structural gaps for the organization to complete.

---

### Step 10: Generate Remediation Roadmap

Based on findings from Steps 5–9, produce a prioritized remediation roadmap.

**⟁ CLARIFY** — Before generating the roadmap, confirm the target audit date to calibrate
the urgency tiers.

**Prioritization by control area and audit impact:**

| Priority     | Definition                                                                                                                                   | Typical Timeline                                         |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **CRITICAL** | Control entirely absent; likely to cause qualified opinion or adverse finding; addresses high-severity TSC criterion                         | Remediate before audit fieldwork begins (within 30 days) |
| **HIGH**     | Control exists but evidence is insufficient for the observation period; process not documented; significant gap that will generate a finding | Remediate in 30–90 days                                  |
| **MEDIUM**   | Control exists and operates but documentation is incomplete; evidence partially available; process informal                                  | Remediate in 90–180 days                                 |
| **LOW**      | Minor documentation gaps; process informal but evidenced; improvement recommended but unlikely to generate audit finding                     | Address during next policy review cycle                  |

**Remediation roadmap template:**

| #   | Gap Description | TSC Criterion | Priority | Owner | Target Date | Evidence Required | Status |
| --- | --------------- | ------------- | -------- | ----- | ----------- | ----------------- | ------ |
| 1   |                 |               | CRITICAL |       |             |                   | Open   |
| 2   |                 |               | HIGH     |       |             |                   | Open   |
| ... |                 |               |          |       |             |                   |        |

---

## Severity / Status Classification System

Apply these four tiers to every control domain and individual finding:

| Classification          | Definition                                                                                                        | Audit Impact                                       | Required Action                                    |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| **COMPLIANT**           | Control is fully designed and operating; adequate evidence available for the observation period                   | No finding expected                                | Monitor; ensure evidence continuity                |
| **PARTIAL**             | Control exists but has documentation gaps, evidence gaps, or inconsistent operation during the observation period | Likely management comment or informational finding | Remediate documentation/evidence gaps before audit |
| **NON-COMPLIANT**       | Control is designed but not operating effectively; or control design has material weaknesses                      | Likely exception in auditor's opinion              | Immediate remediation; escalate to control owner   |
| **CRITICAL DEFICIENCY** | Control entirely absent or consistently failing; represents a fundamental gap against TSC requirements            | Qualified or adverse opinion risk                  | Escalate to C-suite; remediate before audit begins |

**Automatic CRITICAL DEFICIENCY triggers:**

- MFA not enforced on any cloud infrastructure console or production environment
- No access review performed in the past 12 months (for any observation period)
- Terminated employee accounts not removed within 30 days (or policy SLA)
- No penetration test performed in the past 18 months
- No formal risk assessment completed in the past 24 months
- Production database accessible directly by developers without approval process
- No incident response plan documented
- No encryption at rest on production data stores containing sensitive data
- No vendor inventory or third-party risk management program
- No business continuity / disaster recovery plan

---

## Actionable Output Per Finding

For each finding, provide:

**For CRITICAL DEFICIENCY:**

```
Finding: [Control area and specific gap]
TSC Criterion: [CC6.1, A1.2, etc.]
Risk: [What could go wrong; audit opinion impact]
Remediation Action: [Specific steps to implement the missing control]
Evidence Required: [Exactly what the auditor will need to see]
Responsible Party: [Owner role]
Target Date: [Days before audit fieldwork]
Estimated Effort: [Low / Medium / High]
Automation Tool: [If applicable: Vanta, Drata, Secureframe control that addresses this]
```

**For NON-COMPLIANT:**

```
Finding: [Control area and operating failure]
TSC Criterion: [Criterion reference]
Root Cause: [Why the control is not operating effectively]
Remediation Action: [Steps to restore effective operation]
Evidence Required: [What needs to exist going forward]
Target Date: [Timeline for remediation]
```

**For PARTIAL:**

```
Finding: [Documentation or evidence gap]
TSC Criterion: [Criterion reference]
Gap Description: [What is missing]
Quick Fix: [Specific action to close the gap]
Target Date: [Before audit fieldwork]
```

---

## Prioritization Framework

**Tier 1 — Audit Opinion Risk (must remediate before fieldwork):**

- Any CRITICAL DEFICIENCY finding
- Any finding in CC6 (Logical Access) without Type II evidence for the full observation period
- System description not drafted or materially incomplete
- Management assertion process not understood or no senior executive identified to sign

**Tier 2 — Likely Finding (remediate 30–90 days before fieldwork):**

- NON-COMPLIANT findings in CC7, CC8, CC9
- Vendor SOC reports not collected for critical subservice organizations
- Access review evidence gaps within the observation period
- Policy review cycles missed within the observation period

**Tier 3 — Informational / Management Comment (remediate before next audit cycle):**

- PARTIAL findings in CC1, CC2
- Documentation improvements (policy version history, approval signatures)
- Optional TSC criteria with minor evidence gaps
- Process improvements that do not affect operating effectiveness

---

## Citation Quality Gates

Run these five gates before delivering any output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                                     | Fail Action                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every TSC criterion reference cites the AICPA 2017 TSC (or 2022 updated points of focus) by CC or TSC series code                        | Add criterion reference or mark [UNVERIFIED]                     |
| **Format**     | All criterion references use the standard CC/A/PI/C/P series format                                                                      | Fix format (e.g., "CC6.1" not "criterion 6.1")                   |
| **Currency**   | 2022 AICPA points of focus updates checked for any modified criteria                                                                     | Flag "[CHECK CURRENCY — 2022 POF updates]" for affected criteria |
| **Domain**     | Analysis stays within the SOC 2 TSC scope; HIPAA/GDPR/ISO 27001 references clearly marked as framework crosswalk, not SOC 2 requirements | Remove or clearly flag framework bleed                           |
| **Confidence** | Uncertainty about whether a control satisfies a criterion explicitly stated                                                              | Add confidence qualifier and recommend auditor confirmation      |

---

## Self-Interrogation for Critical Deficiency Findings

For any finding classified CRITICAL DEFICIENCY, apply this three-pass adversarial review:

**Pass 1 — Criterion Chain Integrity**: Does the gap directly fail a specific TSC criterion
or point of focus? Could a reasonable auditor reach a different conclusion about whether
a compensating control satisfies the criterion?

**Pass 2 — Completeness**: Are there compensating controls that partially address the gap?
Has the organization's cloud provider (AWS, Azure, GCP) implemented shared-responsibility
controls that partially satisfy the criterion? Are there regulatory-mandated controls
(HIPAA, PCI) that cross-satisfy the criterion?

**Pass 3 — Challenge**: Under what circumstances might the auditor issue only a management
comment rather than a qualified finding? What is the strongest argument that the control,
as implemented, is sufficient?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                     | Action                                                                  |
| ------------ | --------- | ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear TSC criterion violation; settled audit practice       | State as finding                                                        |
| **High**     | 0.80–0.94 | Strong basis for finding; minor judgment involved           | State with brief caveat; recommend auditor review                       |
| **Probable** | 0.60–0.79 | Control likely insufficient but auditor judgment may differ | Flag for auditor discussion; present both views                         |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on auditor's assessment        | Mark [AUDITOR JUDGMENT REQUIRED]; do not classify as definitive finding |
| **Unlikely** | 0.0–0.39  | Speculative basis; control likely sufficient                | Do not assert as finding; note for awareness only                       |

---

## Glass Box Audit Trail

Include this YAML block in every output:

```yaml
glass_box:
  skill_name: "legalcode-soc2-readiness-assessment"
  mode: "Created from scratch"
  topic: "SOC 2 Type I/II readiness across Trust Service Criteria"
  jurisdiction: "US-origin standard; global application"
  tsc_in_scope: "[Security / Availability / Processing Integrity / Confidentiality / Privacy]"
  audit_type_target: "[Type I / Type II / Not determined]"
  observation_period: "[Start date – End date or 'Type I - not applicable']"
  organization_profile: "[Industry, size, cloud platform]"
  subservice_organizations: "[List or 'None identified']"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-soc2-authority.md or 'Not created']"
  critical_deficiencies_found: "[number]"
  non_compliant_findings: "[number]"
  partial_findings: "[number]"
  compliant_domains: "[number]"
  framework_crosswalks_performed: "[ISO 27001 / NIST CSF / HIPAA / PCI DSS / None]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "This assessment is not an audit opinion and does not constitute an AT-C Section 205 examination"
    - "Control effectiveness can only be finally determined by a licensed CPA firm through audit fieldwork"
    - "[Any scope limitations specific to this assessment]"
  reviewer: "AI-assisted — requires qualified CPA firm and information security practitioner review"
```

---

## Anti-Patterns

The following patterns consistently produce poor SOC 2 outcomes. Flag them whenever identified.

1. **Treating SOC 2 as a documentation exercise**: Producing policies and procedures without
   implementing corresponding technical controls. Auditors test operating effectiveness;
   documents alone do not satisfy controls.

2. **Snapshot-only evidence for Type II**: Providing a single access review screenshot when
   the policy requires quarterly reviews over a 12-month period. Type II auditors sample
   across the entire observation period.

3. **Scoping out critical infrastructure**: Carving out AWS/Azure/GCP and then failing to
   obtain and review those providers' SOC 2 reports annually. The carve-out method requires
   active vendor SOC report review, not passive exclusion.

4. **Over-broad system description**: Describing the entire company rather than the
   in-scope system. A system description that is too broad creates more evidence obligations
   than necessary and increases audit complexity.

5. **Under-broad system description**: Scoping out systems that process in-scope customer
   data in order to reduce evidence burden. Auditors will probe the system boundaries;
   material omissions damage credibility.

6. **CUECs as a liability shield**: Listing CUECs that customers cannot realistically
   implement (e.g., requiring customers to review all access daily) in order to transfer
   control responsibility. Auditors assess whether CUECs are reasonable and clearly communicated.

7. **Selecting all five TSC to appear comprehensive**: Including Processing Integrity or
   Privacy criteria when the service does not make relevant commitments. Optional criteria
   that are in scope but unsupported by controls generate findings.

8. **Treating penetration test as a checkbox**: Commissioning an annual pentest but not
   remediating findings. Auditors review pentest results and remediation tracking; unresolved
   critical/high findings are a significant red flag.

9. **Generic IR plan not customized to the organization**: Using a vendor-provided incident
   response template without tailoring it to the organization's actual systems, personnel,
   contact lists, and escalation paths. Auditors test IR plans against the system description.

10. **Shared admin credentials**: Maintaining shared "admin" or "root" accounts used by
    multiple personnel. This fails CC6 (individual accountability) and makes access reviews
    meaningless.

11. **No separation between development and production environments**: Allowing developers
    to deploy directly to production without a change management process. This fails CC8
    and CC6 simultaneously.

12. **Access review theater**: Completing access reviews by rubber-stamping all access as
    appropriate without actually reviewing whether each account still requires its access
    level. Auditors may interview reviewers or test whether terminated employees were caught.

13. **Vendor management limited to procurement**: Completing vendor due diligence at
    onboarding but not performing ongoing annual assessments. CC9 requires ongoing monitoring
    of vendor risk, not one-time screening.

14. **Observation period evidence gaps**: Failing to maintain continuous evidence collection
    during the Type II observation period and then trying to reconstruct evidence retroactively.
    Auditors can detect post-hoc evidence creation; it severely damages the audit relationship.

15. **Conflating SOC 2 with GDPR/HIPAA compliance**: Telling customers that a SOC 2 report
    means the organization is GDPR-compliant or HIPAA-compliant. SOC 2 is a security
    attestation; it does not certify compliance with data protection laws that have their
    own substantive requirements.

16. **Bridge letter misuse**: Providing customers with a bridge letter for a report that
    is 18+ months old, or treating a bridge letter as equivalent to a current SOC 2 report
    for procurement purposes. Bridge letters cover short gap periods; they are not a
    substitute for timely audit renewal.

17. **Selecting Type I for customer satisfaction without a Type II plan**: Obtaining a
    Type I report to satisfy a customer requirement without planning the path to Type II.
    Enterprise customers increasingly require Type II; a Type I may buy 6–12 months but
    is not a long-term solution.

18. **No control owner assignment**: Having controls documented without named owners.
    Auditors ask who is responsible for each control; "the security team" is not a
    sufficient answer.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Use specific TSC criterion codes**: Reference "CC6.1" not "the access control criterion"
2. **Distinguish Type I from Type II requirements**: Evidence standards differ; never conflate them
3. **Quantify evidence requirements**: "12 access review sign-offs (one per month for a 12-month period)" not "access review evidence"
4. **Name the auditor's action**: Say "auditors will request" or "will generate a finding" not vague risk language
5. **Separate SOC 2 requirements from framework crosswalk references**: Use clear labeling ("ISO 27001 equivalent" vs. "SOC 2 requirement")
6. **Flag unverified references**: Mark all criterion references not verified against current AICPA publications with [VERIFY]
7. **Qualify opinions on auditor judgment**: Auditors have discretion; do not state findings as certain when they involve professional judgment calls

**Quality gate before delivery:**

- [ ] Every CRITICAL DEFICIENCY cites a specific TSC criterion
- [ ] All recommendations specify required evidence
- [ ] Framework crosswalk references are clearly labeled as such (not stated as SOC 2 requirements)
- [ ] Remediation roadmap items have specific owners, dates, and evidence requirements
- [ ] Glass Box audit trail is complete

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current AICPA Trust Service Criteria updates and points of focus (2022 revisions)
- Search for regulatory overlays applicable to the organization's industry and jurisdiction
- Verify management assertion standards under AT-C Section 205
- Search for relevant regulatory guidance from AICPA, OCC, OCR, FTC, or EU authorities
  as applicable to the organization's industry
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with built-in SOC 2 knowledge
- Mark all TSC criterion references with [VERIFY against AICPA 2017 TSC + 2022 POF]
- Recommend the user verify criterion references against the AICPA Trust Services Criteria
  document (available at aicpa-cima.com)

---

## Localization Notes

**United States:**

- SOC 2 reports are prepared by US-licensed CPA firms under AT-C Section 205
- HIPAA overlay: healthcare technology organizations should assess using both SOC 2
  and HIPAA Security Rule simultaneously
- FedRAMP: US federal procurement requires FedRAMP (not SOC 2); a SOC 2 is a useful
  precursor but does not satisfy FedRAMP requirements
- GLBA/NYDFS: financial services technology organizations should identify applicable
  state and federal financial data security requirements that exceed SOC 2 scope

**European Union and United Kingdom:**

- SOC 2 is widely accepted by EU/UK enterprise customers as a security attestation
- SOC 2 Privacy criteria (GAPP-based) do not satisfy GDPR or UK GDPR obligations;
  a separate GDPR compliance program is required
- ISAE 3000 (international attestation standard) is sometimes requested instead of or
  alongside SOC 2; the conceptual framework is similar but the formal standard differs
- [JURISDICTION-SPECIFIC] Some EU regulated industries (banking, insurance) may require
  DORA compliance (Reg. 2022/2554) which has specific ICT risk requirements that overlap
  with but exceed SOC 2 scope

**Asia-Pacific:**

- SOC 2 reports are accepted across Singapore, Australia, Japan, and most APAC markets
- Australia: SOC 2 overlaps with Australian Privacy Act (Privacy Act 1988) requirements;
  the Privacy Act does not have a SOC 2 equivalency pathway
- Singapore: MAS Technology Risk Management Guidelines have additional requirements
  beyond SOC 2 for financial institutions

---

## Output Format Template

Deliver the SOC 2 Readiness Assessment in this structure:

---

# SOC 2 Readiness Assessment Report

**Organization:** [Name]
**Assessment Date:** [Date]
**Target Audit Type:** [Type I / Type II]
**Observation Period (Type II):** [Start – End]
**TSC in Scope:** [List]
**Assessed by:** AI-assisted — requires qualified CPA firm review

---

## Executive Summary

**Overall Readiness:** [READY / SUBSTANTIALLY READY / NOT READY] for [Type I / Type II]
**Estimated Time to Audit-Ready:** [X months from today]
**Critical Deficiencies:** [N] (must remediate before audit)
**High-Priority Findings:** [N] (remediate 30–90 days before audit)
**Medium-Priority Findings:** [N]
**Compliant Domains:** [N of 9 Common Criteria domains]

**Key Strengths:**

- [Top 2–3 areas where controls are well-designed and evidenced]

**Critical Gaps:**

- [Top 2–3 CRITICAL DEFICIENCY findings in plain language]

**Recommended Path:**

- [High-level 3-step action plan]

---

## Control Domain Assessment

### CC1: Control Environment

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Summary:** [2–3 sentence assessment]
**Findings:**
| Finding | Severity | TSC Criterion | Remediation Action | Evidence Required |
|---------|----------|---------------|-------------------|-------------------|

### CC2: Communication and Information

[Same structure]

### CC3: Risk Assessment

[Same structure]

### CC4: Monitoring Activities

[Same structure]

### CC5: Control Activities

[Same structure]

### CC6: Logical and Physical Access Controls

[Same structure]

### CC7: System Operations

[Same structure]

### CC8: Change Management

[Same structure]

### CC9: Risk Mitigation — Vendors and Business Disruption

[Same structure]

---

## Optional TSC Assessment

[Include only if in scope]

### Availability

[Assessment]

### Processing Integrity

[Assessment]

### Confidentiality

[Assessment]

### Privacy

[Assessment]

---

## Framework Crosswalk Summary

[Include only if requested]

| Framework           | Overlap with SOC 2 | Key Gaps (Not Covered by SOC 2)                                           | Notes    |
| ------------------- | ------------------ | ------------------------------------------------------------------------- | -------- |
| ISO 27001:2022      | ~80% overlap       | System description, management assertion, AICPA-specific evidence formats |          |
| NIST CSF 2.0        | ~75% overlap       | GOVERN function documentation formality differs                           |          |
| HIPAA Security Rule | ~70% overlap       | ePHI-specific scope, BAA requirements, specific audit log requirements    | [VERIFY] |
| PCI DSS v4.0        | ~60-70% overlap    | Network segmentation standards, ASV scanning, CHD-specific controls       | [VERIFY] |

---

## Remediation Roadmap

### CRITICAL — Remediate Before Audit Begins

| #   | Finding | CC  | Owner | Due Date | Evidence Required |
| --- | ------- | --- | ----- | -------- | ----------------- |

### HIGH — Remediate 30–90 Days Before Audit

| #   | Finding | CC  | Owner | Due Date | Evidence Required |
| --- | ------- | --- | ----- | -------- | ----------------- |

### MEDIUM — Remediate Before Next Audit Cycle

| #   | Finding | CC  | Owner | Due Date | Evidence Required |
| --- | ------- | --- | ----- | -------- | ----------------- |

---

## System Description and Management Assertion Readiness

**System Description Status:** [Draft / Partial / Not Started]
**Management Assertion Readiness:** [Ready / Needs Work / Not Started]
**CUECs Status:** [Documented / Needs Review / Not Identified]
**Subservice Organizations:** [List with carve-out / inclusive status]

---

## Recommended Next Steps

1. [Immediate action — highest priority]
2. [Auditor engagement recommendation]
3. [Compliance automation tooling recommendation if applicable]
4. [Timeline milestones]

---

## Glass Box Audit Trail

[Insert complete YAML block from template above]

---

_This report is AI-assisted and does not constitute an audit opinion under AT-C Section 205.
Review by a licensed CPA firm and qualified information security practitioner is required._

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- AICPA 2017 Trust Services Criteria for Security, Availability, Processing Integrity,
  Confidentiality, and Privacy (with 2022 points of focus updates)
- AICPA AT-C Section 205 Examination Engagements
- AICPA SOC 2 Guide (Type 2 Report on Management's Description of a Service Organization's
  System and the Suitability of the Design and Operating Effectiveness of Controls)
- AICPA Management Assertion guidance and illustrative templates
- Industry practice patterns across SaaS, cloud infrastructure, and managed service providers
- Framework crosswalk analysis: ISO/IEC 27001:2022, NIST CSF 2.0, HIPAA Security Rule
  (45 CFR Part 164), PCI DSS v4.0
- Common audit deficiency patterns observed in SOC 2 practice (COMPLIANT/PARTIAL/
  NON-COMPLIANT/CRITICAL DEFICIENCY classification framework)
- Legalcode quality frameworks: Citation Quality Gates, Self-Interrogation, Confidence
  Scoring, Glass Box audit trail (adapted from legalcode-contract-review reference standard)
