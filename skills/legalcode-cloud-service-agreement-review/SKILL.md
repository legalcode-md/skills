---
name: legalcode-cloud-service-agreement-review
description: >
  Review cloud and hosted-service agreements (CSA, cloud MSA, SaaS agreement, cloud
  subscription agreement, cloud order form) — flag deviations, generate confidence-scored
  redlines, and produce an auditable analysis. Covers service description and scope, SLAs
  and uptime credits, security commitments, data processing (GDPR Art. 28 / DPA overlay),
  sub-processors, audit rights, customer data ownership, provider AI training rights,
  limitation of liability (including data breach super-caps), indemnification, business
  continuity and DR, exit assistance and data portability (EU Data Act 2023), regulatory
  compliance allocation (DORA, HIPAA BAA, PCI DSS, FedRAMP), unilateral modification
  rights, and term and termination. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers. Native Legalcode replacement for imported cloud-service agreement packs.
  Use when reviewing cloud provider terms, AWS/Azure/GCP order forms, SaaS enterprise
  agreements, managed-hosting contracts, IaaS/PaaS/SaaS agreements, or any contract
  where a customer is consuming computing, storage, or software as a service.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Cloud Service Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of cloud and
> hosted-service agreements. It does not constitute legal advice. All outputs should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use. Laws change; verify current applicability before relying on any provision described
> here. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them.

## Purpose and Scope

This skill reviews cloud service agreements (CSAs), SaaS enterprise agreements, cloud
MSAs, and related hosted-service contracts against an organization's negotiation playbook
or general market standards. It identifies deviations, classifies their severity, generates
actionable redline suggestions, and produces a confidence-scored, auditable analysis
calibrated to the specific risks of cloud and hosted-service procurement.

**Covers:**
- Clause-by-clause analysis across 16 CSA-specific categories plus 6 standard categories
- Deviation classification (GREEN / YELLOW / RED) adapted to cloud procurement risk
- SLA uptime credit mechanics and carveout analysis
- GDPR Art. 28 / DPA overlay and sub-processor flow-down assessment
- Data breach liability structure and super-cap negotiation
- EU Data Act Chapter VI (Arts. 23–26) exit and switching compliance (applicable from 12 September 2025)
- DORA (Reg. 2022/2554) mandatory contract term compliance for financial sector customers
- Provider AI training use of customer data — rights, restrictions, and safeguards
- Business continuity, DR, and resilience commitment analysis
- Redline generation with fallback positions
- Multi-stakeholder mapping including data subjects, regulators, and sub-processors
- Glass Box audit trail

**Does not:**
- Draft new cloud agreements (see legalcode-technology-license-agreement for drafting)
- Replace qualified legal counsel or provide legal advice
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Cover on-premise software license agreements (see legalcode-technology-license-review)

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The contract's own governing law clause determines
which legal framework applies. The review identifies the governing law early and applies
the relevant mandatory overlay.

[JURISDICTION-SPECIFIC] Key jurisdiction-specific overlays to apply:

- **EU / EEA**: GDPR Art. 28 DPA requirements; EU Data Act Chapter VI switching/portability
  (from 12 September 2025); NIS2 Directive (2022/2555) incident reporting; DORA
  (2022/2554) for financial sector; 2021 SCCs (Modules 2 and 3) for cross-border transfers
- **United Kingdom**: UK GDPR + DPA 2018; ICO guidance; UK IDTA or UK Addendum to EU
  SCCs for international transfers
- **United States**: CCPA/CPRA for California residents; HIPAA / BAA requirement for
  PHI; PCI DSS 4.0 for payment data; FedRAMP for federal agencies; state breach
  notification laws (all 50 states; California SB 446 effective 1 January 2026)
- **Financial sector (global)**: DORA (EU); FCA PS21/3 / SS2/21 (UK); OCC guidance (US)
- **Healthcare (US)**: HIPAA Security Rule; proposed 2025 updates (annual pen testing,
  enhanced audit logs) [VERIFY currency at review date]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- The contract's scope or governing law creates ambiguity requiring resolution
- Risk tolerance or regulatory status is needed to classify severity correctly

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

### Step 1: Accept the Agreement

Accept the cloud service agreement in any of these formats:
- **File**: PDF, DOCX, or other document format
- **URL**: Link to cloud provider terms page, CLM, or document system
- **Pasted text**: Agreement text pasted directly into the conversation

If no agreement is provided, prompt the user to supply one. For multi-document agreements
(MSA + Order Form + SLA Schedule + DPA), accept all components before beginning analysis.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions. Present as
structured options where possible:

1. **Which side are you on?**
   - Options: Customer / Cloud Consumer, Provider / Cloud Vendor, Both (reviewing own standard terms)
   - *Why this matters*: What protects a customer harms a provider and vice versa. The
     analysis of SLA exclusions, liability caps, and data use rights flips completely.

2. **Industry / regulatory status**: Is the customer subject to regulated-industry rules?
   - Options: Financial services (DORA / OCC / FCA applies), Healthcare (HIPAA applies),
     Government / Public sector (FedRAMP / sovereignty concerns), General commercial, Other
   - *Why this matters*: DORA requires mandatory contract terms; HIPAA requires a BAA;
     government procurement triggers specific security and data sovereignty requirements.

3. **Data sensitivity**: What types of data will be processed under this agreement?
   - Options: Personal data of EU/UK residents (GDPR applies), Personal data of US
     residents (CCPA/state laws apply), Protected Health Information (HIPAA), Payment card
     data (PCI DSS), Classified / government data (sovereignty rules), Non-personal / no
     regulated data
   - Allow multiple selections.
   - *Why this matters*: Determines whether DPA, BAA, PCI Responsibility Matrix, and
     data transfer mechanism review are mandatory vs. advisory.

4. **Deal context**: Relevant commercial context?
   - Free text. Prompt with examples: annual contract value, strategic importance of the
     service, whether this is the provider's standard click-through or a negotiated
     enterprise agreement, existing relationship, whether there is a competitive process.
   - *Why this matters*: A $15K/year SaaS tool gets different treatment than a $5M/year
     infrastructure migration. Negotiation leverage differs significantly.

5. **Focus areas**: Any specific concerns?
   - Options: SLA / uptime reliability, Data security and breach liability, Exit and
     portability (EU Data Act), AI training use of our data, Regulatory compliance (DORA
     / HIPAA / FedRAMP), IP and customer data ownership, Liability cap exposure, No
     specific focus — full review
   - Allow multiple selections.

If the user provides partial context, proceed with what you have but **state assumptions
explicitly** (e.g., "Assuming you are the customer — let me know if that's wrong").

### Step 3: Load the Playbook

Check for the organization's cloud procurement playbook in local settings
(e.g., `legal.local.md`, `cloud-playbook.md`, or similar configuration files).

A cloud playbook should define standard positions for: SLA minimums, credit percentages,
maximum liability caps, data breach carveout requirements, DPA standards, AI training
prohibitions, exit assistance minimums, and DORA/HIPAA compliance requirements.

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining the organization's standard
  positions for the key CSA clauses listed in Step 5. Takes time upfront but makes this
  and all future cloud reviews more precise.
- **Option B: Proceed with general market standards** — Use widely-accepted market
  standards and regulatory minimums as the baseline. Faster, but the review will not
  reflect the organization's specific risk appetite.
- **Option C: Provide positions as we go** — Start the review and ask about preferred
  positions when they matter for each clause.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the contract's governing law clause. Use **legalcode-mcp** to build a working
legal reference file before analyzing clauses.

**Research process:**

1. **Identify the governing law** from the agreement (typically in the MSA or Order of
   Precedence). Also note any data protection governing law (DPA may specify a different
   governing law, typically the customer's EU member state for GDPR compliance).

   **⟁ CLARIFY** — If any of the following are true, ask the user before proceeding:
   - **No governing law clause**: Ask which jurisdiction the user expects to apply.
     Flag absence as RED.
   - **Mismatch between MSA governing law and DPA governing law**: Note and flag.
   - **Provider's home-jurisdiction governing law in a foreign deal**: Confirm the user
     is aware and ask whether to analyze under stated law or flag as a negotiation point.

2. **Search legalcode-mcp** for:
   - Data protection regime (GDPR Art. 28, UK GDPR, CCPA/CPRA, LGPD, PIPA)
   - Cloud switching and exit obligations (EU Data Act Arts. 23–26 if EU-connected)
   - DORA mandatory contract requirements (if financial sector customer)
   - NIS2 incident reporting requirements (if EU-connected)
   - Cross-border data transfer mechanisms (2021 EU SCCs, UK IDTA, adequacy decisions)
   - Exclusion clause enforceability (UCTA 1977 for UK, statutory rules per jurisdiction)
   - Penalty / liquidated damages rules (for SLA credit and early termination fee analysis)
   - Industry-specific mandatory requirements (HIPAA BAA, PCI DSS, FedRAMP)

3. **Save results** to `/tmp/legalcode-csa-authority.md` structured as:
   ```
   # CSA Legal Authority — [Contract Name]
   ## Governing Law: [Jurisdiction]
   ## Date: [date]
   ### Data Protection
   ### Cloud Switching / Data Act
   ### DORA (if applicable)
   ### Exclusion Clause Enforceability
   ### Cross-Border Transfers
   ```

4. **Use this reference throughout** the clause analysis. Mark citations sourced from
   legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general market knowledge but flag that legal authority is unverified

### Step 5: Map the Agreement Structure

Before clause analysis, map the full agreement architecture:

- Identify all documents forming the agreement: MSA / Base Agreement, Order Form(s),
  Service Descriptions, SLA Schedule, DPA / Privacy Addendum, Security Policy,
  Sub-processor List, Acceptable Use Policy, Support Terms
- Identify the **Order of Precedence** clause. Note which documents govern in conflict.

**⟁ CLARIFY** — For multi-document agreements:
- Ask whether to perform a **full review** of all documents or a **priority review**
  focused on the MSA, DPA, and SLA Schedule only
- If external documents are incorporated by reference (e.g., "Provider's current Security
  Policy at [URL]"), ask whether the user wants those documents reviewed or only flagged
  as an incorporation-by-reference risk

### Step 6: Clause-by-Clause Analysis

Analyze the agreement systematically. Read the entire agreement before flagging issues —
clauses interact (e.g., an SLA credits-as-exclusive-remedy clause may limit breach of
contract claims, not just SLA remedies).

**⟁ CLARIFY** — For long or complex agreements (50+ pages, or with multiple schedules):
- Ask whether to perform a full review of all 16 CSA-specific categories and 6 standard
  categories, or a priority review focused on the user's stated focus areas.

Cover all categories below. For each, assess against the playbook (or market standards)
and note whether the clause is present, absent, or unusual.

| # | Clause Category | Depth | Key Review Points |
|---|----------------|-------|-------------------|
| 1 | Service Description and Scope | Deep | Service definition precision, exclusions, change of scope, benchmarking restrictions |
| 2 | SLA and Uptime Credits | Deep | Uptime %, credit %, measurement method, carveouts, exclusive remedy, downtime definition |
| 3 | Security Commitments | Deep | Security standards, pen testing, incident notification, access controls, vulnerability management |
| 4 | Data Processing Agreement | Deep | GDPR Art. 28 compliance, DPA structure, processing purpose limitation, data subject rights |
| 5 | Sub-Processors | Deep | Approval model, notification windows, objection rights, flow-down obligations, liability |
| 6 | Audit Rights and Certifications | Deep | Direct audit, SOC 2 substitution, DORA oversight rights, frequency, scope, cost |
| 7 | Customer Data Ownership and IP | Deep | Data ownership, provider license scope, pre-existing IP, customer-developed configurations |
| 8 | Provider Use of Customer Data (AI) | Deep | Service improvement rights, AI/ML training rights, anonymization, aggregation, restrictions |
| 9 | Limitation of Liability | Deep | Cap level, data breach super-cap, mutual exclusion of consequential damages, uncapped items |
| 10 | Indemnification | Deep | IP infringement, data breach indemnity, scope, mutual vs. unilateral, procedure, cap |
| 11 | Business Continuity and DR | Deep | RTO/RPO commitments, geographic redundancy, backup, DR testing, DORA resilience |
| 12 | Exit Assistance and Data Portability | Deep | Transition period, data export format, deletion certification, EU Data Act compliance, fees |
| 13 | Regulatory Compliance Allocation | Deep | Industry-specific obligations (HIPAA BAA, PCI DSS, DORA Art. 30, FedRAMP), government access |
| 14 | Unilateral Modification Rights | Deep | Price changes, feature changes, policy changes, notice periods, termination rights on change |
| 15 | Term, Termination, and Auto-Renewal | Standard | Duration, renewal notice windows, convenience termination, cause cure periods, wind-down |
| 16 | Governing Law and Disputes | Standard | Jurisdiction, arbitration vs. litigation, venue, escalation |
| 17 | Payment and Fees | Standard | Payment terms, price escalation, disputed invoices, taxes, egress fees, overage charges |
| 18 | Confidentiality | Standard | Scope, term, carveouts, provider use of customer information |
| 19 | Assignment and Change of Control | Standard | Consent requirements, change-of-control triggers, service continuity |
| 20 | Force Majeure | Standard | Scope, notification, duration thresholds, cloud-provider-caused outages distinction |
| 21 | Compliance and Regulatory (General) | Standard | Anti-bribery, sanctions, modern slavery, regulatory approvals |
| 22 | Definitions and Boilerplate | Standard | Order of precedence, entire agreement, notices, amendments |

### Step 7: Missing Clause Detection

After analyzing clauses that are present, check for important absent clauses. In a
cloud service agreement, absence can be as significant as a problematic clause.

Critical missing clause flags:

| Missing Clause | Severity | Rationale |
|---------------|----------|-----------|
| No DPA when personal data processed | RED | GDPR Art. 28 mandatory; regulatory fine risk |
| No limitation of liability | RED | Provider or customer exposed to unlimited claims |
| No SLA / all "commercially reasonable efforts" | RED | No enforceable uptime floor; credits meaningless |
| No exit assistance obligations | RED | Vendor lock-in risk; EU Data Act compliance failure if EU-connected |
| No data deletion certification on termination | RED | GDPR / CCPA retention obligations; data sovereignty risk |
| No security incident notification timeline | RED | GDPR 72-hour obligation; CA SB 446 (30 days from 1 Jan 2026) |
| No DPA sub-processor provisions | RED | GDPR Art. 28(4) mandatory sub-processor flow-down |
| No DORA mandatory provisions (financial sector) | RED | Regulatory violation; DORA Art. 30 minimum terms |
| No data ownership clause | YELLOW | Ambiguity about who owns customer data; training use risk |
| No DR / business continuity provisions | YELLOW | Material gap for business-critical services |
| No audit rights or SOC 2 substitution | YELLOW | No assurance mechanism for security commitments |
| No AI training prohibition / restriction | YELLOW | Risk of customer data used to train provider's AI models |
| No benchmark restriction carveout | YELLOW | Customer unable to test own environment |
| No change-of-control provision | YELLOW | Provider may be acquired by competitor with no customer right |
| Missing HIPAA BAA (if PHI involved) | RED | HIPAA violation without BAA; civil and criminal penalties |
| Missing PCI DSS Responsibility Matrix | YELLOW | Shared-responsibility gaps for cardholder data environments |

**⟁ CLARIFY** — Where absence depends on business context not yet provided:
- "This agreement has no DPA. Will personal data of EU or UK residents be processed?
  If yes, this is a regulatory violation (RED). If no personal data is involved, this is fine."
- "There are no DR commitments. How critical is this service? An outage of how many
  hours would materially impact your operations?"
- "No HIPAA Business Associate Agreement is attached. Will Protected Health Information
  be processed or stored through this service?"

### Step 8: Flag Deviations

Classify each deviation using the three-tier system in the **Deviation Severity
Classification** section. For each deviation:

- **GREEN**: Note for awareness
- **YELLOW**: Generate redline language, provide fallback position, estimate business impact
- **RED**: Explain the specific risk with legal basis, provide market-standard alternative,
  estimate exposure, recommend escalation

**⟁ CLARIFY** — For borderline classifications:
- **YELLOW vs. RED on SLA credits**: "The SLA credits clause states credits are the
  exclusive remedy for all SLA failures including extended outages. Should I treat this
  as YELLOW (negotiate broader remedy right) or RED (requires escalation) for a
  business-critical service?" Depends on service criticality and customer's risk tolerance.
- **YELLOW vs. RED on AI training rights**: "The agreement grants the provider a broad
  right to use customer data to 'improve and develop' its services. Does this meet your
  organization's threshold for escalation, or is it a negotiate-only item?"
- **Overall risk posture**: If many items trend toward the provider's benefit, ask whether
  the user wants a conservative (flag more) or pragmatic (flag material items only) classification.

### Step 9: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, ask about negotiation posture if not clear:
- **Volume of redlines**: "I've found [N] items worth negotiating. Do you want redlines
  for all of them, or focus on the top [X] most material ones? Too many redlines can
  signal inexperience or slow a closing."
- **Negotiation realism**: Is this a hyperscaler (AWS, Azure, GCP) with standard terms
  that rarely move, or a mid-market SaaS provider with more flexibility?

For hyperscalers, distinguish between:
- **Non-negotiable** standard terms (usually pricing, liability structure, platform policies)
- **Negotiable** with enterprise addenda or DPA amendments (usually DPA terms, sub-processor
  notification windows, audit rights)
- **Customer-responsibility** configurations (security settings, BAA setup, encryption keys)

### Step 10: Business Impact Summary

Provide a summary covering:
- **Overall risk assessment**: High-level view of the agreement's risk profile
- **Top 3 issues**: Most important items to address, with severity and regulatory dimension
- **Regulatory exposure**: Specific regulatory violations or near-misses (GDPR, DORA, HIPAA)
- **Negotiation strategy**: Which issues to lead with, what to concede, sequencing
- **Cloud-specific considerations**: Vendor lock-in risk, switching cost, exit realism

**⟁ CLARIFY** — If deal context would materially affect strategy:
- **Walk-away option**: Is there a competing provider, or is this vendor the only viable
  option? This determines whether the strategy is assertive or accommodating.
- **Regulatory deadline**: Is there a regulatory compliance deadline (e.g., DORA applies
  from 17 January 2025 for financial sector — gap between contract date and compliance
  deadline is a risk factor)?
- **Existing service already running**: If migrating from another provider or already
  in production, exit and transition terms become more critical.

### Step 11: Quality Verification

Before delivering the analysis, run the quality checks in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material clause analysis.
4. Verify all 22 clause categories have been addressed.
5. Confirm DPA/data protection overlay is complete and accurate.
6. Generate the Glass Box Audit Trail and append it to the output.

---

## Clause Analysis Reference

### 1. Service Description and Scope

**Key elements to review:**
- Whether the service is defined precisely or broadly at the provider's discretion
- Whether the provider may change the service features, functionality, or components
  without consent (covered in Category 14 — Unilateral Modification)
- Exclusions from service scope (e.g., customer-caused issues, third-party components)
- Benchmark and performance testing restrictions
- Prohibited use provisions (acceptable use policy)

**Common issues:**
- Service defined by reference to "current documentation" which the provider may change
- Benchmark testing prohibited without provider consent (even for the customer's own
  environment and data)
- Exclusions so broad they eliminate the provider's accountability for most outages
- "Beta" or "preview" features explicitly carved out from SLA, support, and indemnity

[JURISDICTION-SPECIFIC] Benchmark restriction clauses are common across major providers
(AWS, Azure, Google Cloud) and are typically non-negotiable in standard terms. Seek
carveout for internal security testing and performance testing of customer's own environment.

---

### 2. SLA and Uptime Credits

**Key elements to review:**
- **Uptime commitment**: Numeric percentage (99.9%, 99.95%, 99.99%) vs. "commercially
  reasonable efforts" (no enforceable floor)
- **Measurement period**: Per calendar month vs. rolling 30 days (provider typically uses
  calendar month; customers prefer trailing period)
- **Downtime definition**: Provider-side availability vs. end-to-end connectivity;
  "degraded performance" vs. complete unavailability
- **Credit percentage**: Typically 10–30% of monthly fees for the affected service
- **Credit cap**: Credits capped at the monthly fee for the affected service (market standard)
- **Exclusive remedy**: Whether SLA credits are the **only** remedy for service unavailability
  — even for extended outages, severe degradation, or loss of customer data during downtime
- **SLA carveouts**: Scheduled maintenance, customer-caused, force majeure, third-party
  failures — assess whether carveouts are reasonable or so broad they swallow the SLA

**Uptime "Nines" Reference:**

| Commitment | Annual Downtime | Monthly Downtime | Typical Use Case |
|-----------|----------------|-------------------|-----------------|
| 99.9% | ~8.76 hours/year | ~43.8 minutes | Baseline business SaaS |
| 99.95% | ~4.38 hours/year | ~21.9 minutes | Mid-tier enterprise |
| 99.99% | ~52.6 minutes/year | ~4.4 minutes | Payment, auth, core infra |
| 99.999% | ~5.26 minutes/year | ~26.3 seconds | Life-critical / regulated |

**Common issues:**
- SLA commitment is "commercially reasonable efforts" — no enforceable uptime floor
- Credits are the exclusive remedy for **all** service failures, including data loss during
  outages (Red flag: a 10% monthly fee credit may be $5 against a $50K data breach loss)
- Downtime defined as "complete unavailability" only — excludes degraded performance
- Scheduled maintenance windows excluded but with no maximum frequency or duration limits
- Customer-caused exclusion broad enough to cover legitimate outages the customer did not cause
- Credits require affirmative claim within 30 days with no automatic payment mechanism
- SLA measured only for "core service" with features outside the SLA scope undefined

**Market standards (negotiation reference):**
- Enterprise agreements often achieve 99.95% or 99.99% for core infrastructure
- Credits of 25–30% for breaches below 99.9% are achievable for large accounts
- Exclusive remedy language should carve out breach of the general agreement (not just
  SLA failure), data loss during outages, and security incidents
- Scheduled maintenance should be limited to defined windows with advance notice (7–14 days)

[JURISDICTION-SPECIFIC] SLA credit clauses may be subject to penalty clause / liquidated
damages analysis. In England & Wales (post-Cavendish Square Holding BV v El Makdessi
[2015] UKSC 67 [VERIFY]), the test is whether the provision is extravagant and unconscionable
relative to the legitimate interest in performance. In civil law jurisdictions (e.g.,
France Art. 1231-5 Cc, Germany BGB §343 [VERIFY]), courts may reduce disproportionate
penalty clauses. Conversely, under-compensation through credits-only remedies may be
challengeable if the clause is a penalty clause in disguise.

---

### 3. Security Commitments

**Key elements to review:**
- Security standard the provider commits to maintain (ISO 27001 / 27017, SOC 2 Type II,
  NIST SP 800-53, CSA STAR, FedRAMP)
- Whether commitments are a contractual obligation or just a representation of current practice
- Access controls and least-privilege principles
- Encryption requirements (at-rest and in-transit; provider-managed vs. customer-managed keys)
- Vulnerability management program (patching SLAs, responsible disclosure)
- Penetration testing commitments (annual, scope, results sharing)
- Security incident notification obligations (timeline, content requirements, root cause)

**Common issues:**
- Security standards referenced but with no obligation to maintain them ("we currently
  maintain ISO 27001" vs. "we shall maintain ISO 27001")
- Encryption at rest not addressed, or only using provider-managed keys with no option
  for customer-managed key (BYOK/HYOK)
- Pen testing restricted — customer may not test even its own deployed environment
- Incident notification timeline exceeds GDPR 72-hour DPA-to-controller window
- Root cause analysis not committed or committed on a timeline (e.g., 30 days) that
  may be inadequate for regulatory reporting
- Security commitments apply "to the extent reasonably practicable" — not actionable

**Market standard security commitments:**
- ISO 27001 certification maintained and renewed annually
- SOC 2 Type II report issued at least annually, provided to customer on request
- Encryption at rest (AES-256 minimum) and in transit (TLS 1.2+)
- Customer-managed encryption key option (BYOK) for enterprise/regulated customers
- Security incident notification to customer within 24–48 hours of provider becoming
  aware (to allow customer to meet GDPR 72-hour reporting window)
- Annual penetration testing; results summary shared with customer on NDA basis
- DORA-specific: financial sector contracts must include ICT incident reporting within
  timelines specified in DORA Art. 19 (initial notification, intermediate reports, final report)

[JURISDICTION-SPECIFIC] NIS2 Directive (2022/2555, transposition deadline 17 October 2024):
Cloud computing services are in scope as digital infrastructure. Penalties for essential
entities up to €10M or 2% global annual turnover. EU customers should verify their own
NIS2 obligations and ensure the cloud agreement supports compliance [VERIFY].

---

### 4. Data Processing Agreement (GDPR Art. 28 / DPA Overlay)

**Key elements to review (GDPR Art. 28 mandatory elements [VERIFY]):**
- Processing only on documented customer instructions
- Provider confidentiality obligation for personnel processing personal data
- Technical and organisational security measures (Art. 32 standard)
- Sub-processor approval and flow-down requirement (Art. 28(4))
- Assistance with data subject rights requests (Arts. 12–22)
- Assistance with DPIAs and prior consultation (Arts. 35–36)
- Deletion or return of data on termination
- Audit and inspection assistance right

**Common issues:**
- No standalone DPA — data protection terms buried in general MSA without GDPR-required
  structure (violates Art. 28(3))
- Instructions limited to the agreement itself with no ability to issue further documented
  instructions
- DPIA assistance obligation absent or limited to "reasonable assistance"
- No cross-border transfer mechanism specified (SCCs, adequacy, BCRs)
- Sub-processor list not incorporated by reference or not regularly updated
- Deletion timeline on termination unreasonably long or unspecified

**2021 EU SCCs (Modules 2 and 3):**
- **Module 2 (Controller-to-Processor)**: For customer (controller) to provider (processor)
  transfers to third countries. Required where personal data leaves the EEA.
- **Module 3 (Processor-to-Processor)**: For provider (processor) to sub-processor transfers.
  Required under Art. 28(4) read with Art. 46.
- SCCs must be incorporated by reference or in full; optional clauses must be selected.

[JURISDICTION-SPECIFIC] UK: UK IDTA or UK Addendum to EU SCCs required for transfers
from the UK. ICO must be identified as the supervisory authority. [VERIFY]

[JURISDICTION-SPECIFIC] California (CCPA/CPRA): Cloud providers processing California
residents' personal information as "service providers" must have a written contract
prohibiting: (a) selling personal information; (b) retaining/using/disclosing data outside
the service relationship; (c) combining personal information from incompatible sources. [VERIFY]

---

### 5. Sub-Processors

**Key elements to review:**
- Authorization model: **specific** (customer approves each) vs. **general** (customer
  approves list at signing with notification rights for changes)
- Advance notice period before sub-processor addition or replacement (14–30 days market
  standard; negotiate for 30 days minimum)
- Customer objection mechanism: right to object and, if unresolved, right to terminate
  affected services without penalty
- Flow-down obligations: GDPR Art. 28(4) requires same obligations as in the DPA to
  flow down to each sub-processor by contract
- Provider liability for sub-processor failures: provider should remain fully liable
- Sub-processor list publication: stable URL, regularly updated, incorporated into DPA

**Common issues:**
- Blanket authorization for all current and future sub-processors with no notification
  requirement (violates Art. 28(2) spirit; leaves customer with no oversight)
- Objection right exists but only triggers termination after a lengthy notice period
  that leaves customer exposed in the interim
- Sub-processor obligations less stringent than obligations in the main DPA
- No customer right to audit sub-processors even on specific, documented concern
- Provider sub-processor list only available on request, not at a published URL

---

### 6. Audit Rights and Certifications

**Key elements to review:**
- **Direct audit right**: Customer's right to audit (or appoint an auditor to audit)
  provider's systems, with frequency, notice, NDA, scope, and cost allocation
- **Certification substitution**: Whether provider may satisfy audit obligations by
  providing current SOC 2 Type II, ISO 27001, CSA STAR, or equivalent reports
- **Trigger-based audit**: Right to demand direct audit on reasonable cause (security
  incident, compliance concern) regardless of the standard cycle
- **DORA oversight rights**: For financial sector customers — regulatory authority's
  right to audit under DORA Arts. 40–44 (CTPPs) must be preserved in the contract

**Common issues:**
- Audit right theoretically present but conditioned on requirements that make it
  practically unusable (e.g., 90-day notice, customer bears all costs, limited to
  business hours, provider may designate a proxy for all inspections)
- SOC 2 report substitution with no trigger-based direct audit fallback
- DORA regulatory audit rights not preserved — regulatory supervisor cannot access
  provider on behalf of the financial entity customer
- "Reasonable cause" for direct audit defined so narrowly it effectively only triggers
  after a data breach (too late)

**Market standard audit structure:**
- Annual: customer receives current SOC 2 Type II or equivalent upon request (NDA basis)
- Cause-based: customer may conduct (or appoint auditor for) direct audit with 30-day
  advance notice and reasonable NDA, limited to customer's data and relevant controls;
  customer bears costs unless audit reveals material breach
- DORA (financial sector): contract must expressly preserve the right of competent
  authorities and the lead overseer to conduct full inspections including on-site audits
  of CTPP infrastructure (DORA Art. 30(2)(f) [VERIFY])

---

### 7. Customer Data Ownership and Intellectual Property

**Key elements to review:**
- Explicit statement that customer retains all right, title, and interest in customer data
- Provider's license to process customer data: scope, purpose, duration
- Whether the license terminates on expiration or termination of the agreement
- Pre-existing IP ownership: each party retains its own background IP
- Customer-developed configurations, code, or customizations: who owns them?
- Feedback clauses: do suggestions or feedback grant provider perpetual rights to use?
- Open source components in the service: disclosed? license obligations passed through?

**Common issues:**
- No express customer data ownership statement — rights left to implication
- Provider license scope broader than needed for service delivery (e.g., "any purpose")
- Provider retains broad rights to customer data post-termination
- Customer configurations developed using provider's APIs assigned to or co-owned by provider
- Broad feedback clause: "any feedback, suggestions, or improvements you provide may be
  used by Provider for any purpose without restriction or compensation"
- Perpetual, irrevocable license granted to customer feedback even after termination

---

### 8. Provider Use of Customer Data (AI / Machine Learning)

This is a rapidly evolving and heavily negotiated area (2024–2026). Review carefully.

**Key elements to review:**
- Whether the agreement permits provider to use customer data to **improve, develop, or
  train** its services, products, or AI/ML models
- Whether any use of customer data for such purposes requires anonymization/aggregation
- Whether customer data may be used to benefit **other customers** or third parties
- Benchmark and performance data: may provider use performance metrics of customer's
  usage in aggregate statistics?
- Prohibition on training AI models on customer-identifiable data

**Common issues:**
- Broad service improvement right: "Provider may use aggregated, de-identified Customer
  Data to improve Provider's products and services" — if "de-identified" is not defined
  to a clear standard (e.g., GDPR pseudonymization ≠ true anonymization), this may
  still constitute personal data processing
- No prohibition on using identifiable customer data in AI training pipelines
- Customer data used to train models that benefit other customers (competitive intelligence
  risk, especially for proprietary business data)
- No opt-out mechanism for AI training use of aggregated data
- Agreement predates generative AI; old service improvement clause may not have been
  intended to cover LLM training but now does [see: Fastcase v. Alexi Technologies
  (November 2025) — retroactive AI training use of licensed data litigation risk [VERIFY]]

**Market standard (2025):**
- Express prohibition on using identifiable customer data for AI/ML model training
- Any use of aggregated/anonymized data for service improvement must require genuine
  anonymization meeting the applicable data protection standard (GDPR recital 26 standard
  for EU [VERIFY]; de-identification standards under CCPA for US [VERIFY])
- Prohibition on using customer data to benefit other customers without express opt-in
- Customer right to opt out of any aggregate benchmarking data collection

**EU AI Act overlay (applicable from 2 August 2026 for GPAI [VERIFY]):**
Providers of general-purpose AI models must publish detailed summaries of training data.
Where a customer's data contributed to training a GPAI model, implications for IP
ownership and licensing should be assessed.

---

### 9. Limitation of Liability

**Key elements to review:**
- **General liability cap**: Amount (typically 12 months' fees — negotiate for higher
  for business-critical or regulated services), mutual vs. unilateral
- **Data breach super-cap**: Whether a higher separate cap applies specifically to data
  protection failures, data breach, or GDPR violations
- **Uncapped obligations**: Items carved out from any cap
- **Consequential / indirect damages exclusion**: Mutual vs. one-sided; carveouts from
  the exclusion
- **Credit-as-sole-remedy trap**: Confirm the limitation clause does not transform SLA
  credits into the only remedy for **all** types of service failure (not just SLA failure)

**Standard uncapped carveouts (market reference):**
- Death or personal injury caused by negligence
- Fraud or fraudulent misrepresentation
- Any obligation that cannot be limited by law (jurisdiction-specific)
- IP infringement indemnification (many enterprise providers offer uncapped IP indemnity)
- Confidentiality breaches
- Customer's payment obligations

**Data breach super-cap trend (2024–2025):**
Regulated industry customers increasingly demand either (a) uncapped liability for data
protection failures, or (b) a dedicated super-cap (e.g., 2× or 3× annual fees) for
GDPR/DPA breaches separate from the general cap. This is now a standard negotiating
position for financial services and healthcare customers. [VERIFY current market practice]

**Common issues:**
- General cap set at 3 months' fees or fees paid in the prior month — far below market
- No data breach super-cap; regulatory fines and customer loss from breach capped at
  nominal amount
- Consequential damages exclusion is one-sided (protects only provider)
- Consequential damages exclusion explicitly includes "loss of data" or "loss of revenue"
  — these are the most likely losses in a cloud service failure
- SLA credits stated as exclusive remedy for "any failure to meet the service levels"
  where SLAs are defined so broadly they encompass most contractual obligations

[JURISDICTION-SPECIFIC] UK (Unfair Contract Terms Act 1977): Provider cannot exclude
liability for negligence causing death or personal injury; limitation of liability for
negligence causing other loss must satisfy a reasonableness test. [VERIFY]

[JURISDICTION-SPECIFIC] EU civil law: Many civil codes prohibit exclusion of liability
for intentional misconduct (dolus) or gross negligence. [VERIFY per member state]

[JURISDICTION-SPECIFIC] GDPR Art. 82 and DORA: Regulatory liability (supervisory
authority fines) cannot be contractually allocated to the provider; however, the provider
can indemnify the customer for fines caused by provider's breach of the DPA. [VERIFY]

---

### 10. Indemnification

**Key elements to review:**
- **IP infringement indemnification**: Provider indemnifies customer for third-party
  claims that the service, as provided, infringes IP rights — scope, procedure, carveouts
- **Data breach indemnification**: Whether provider indemnifies customer for losses
  caused by a security failure on the provider's side (including regulatory fines
  attributable to the provider's failure)
- Mutual vs. unilateral: customer should also indemnify provider for misuse of the service
- Indemnification cap: subject to general liability cap or separately negotiated
- Procedure: notice, right to control defense, right to approve settlements, mitigation

**Common issues:**
- IP indemnity excludes the most likely infringement scenarios (open source components,
  APIs, third-party software embedded in the service)
- "Combination carveout" so broad it excludes all infringement arising from use of the
  service combined with customer's systems — effectively gutting the indemnity
- Data breach indemnity absent; customer bears all downstream losses from provider failure
- Unilateral indemnity: customer indemnifies provider for customer's acts, but provider
  does not indemnify customer for provider's acts
- No control-of-defense right for customer when provider assumes defense

---

### 11. Business Continuity and Disaster Recovery

**Key elements to review:**
- **RTO (Recovery Time Objective)**: Maximum tolerable time from disruption to restoration
- **RPO (Recovery Point Objective)**: Maximum tolerable data loss (age of last recoverable backup)
- Geographic redundancy: multi-AZ, multi-region, active-active vs. active-passive
- Backup frequency, retention period, immutable storage, and restoration testing
- DR plan documentation and customer access to summary
- Relationship between DR commitments and SLA uptime commitments (are they the same or
  separately defined?)

**Market standard DR reference:**

| Tier | RTO | RPO | Typical Service |
|------|-----|-----|----------------|
| Standard | 4–8 hours | 1–4 hours | Non-critical SaaS |
| Enhanced | 1–4 hours | 15–60 minutes | Business-critical SaaS |
| Premium/HA | < 15 minutes | < 15 minutes | Financial / healthcare |

**Common issues:**
- No DR commitments — entirely subsumed into the SLA uptime commitment, which
  addresses availability but not data recovery
- RPO undefined or set at "best efforts" — no guaranteed data recovery point
- Geographic redundancy asserted but not committed — provider "may" use multi-region
  infrastructure at its discretion
- Backup retention insufficient for regulated industries (7-year retention for financial
  records, etc.)
- DR testing conducted but results not shared with customer; customer cannot verify
  commitments are operational

**DORA overlay (financial sector, applied 17 January 2025):**
DORA Art. 25 requires financial entities to test ICT business continuity plans annually.
Cloud contracts must (a) commit to specific RTO/RPO, (b) include exit strategy and
documented exit plan, (c) allow testing of exit plan, and (d) commit to regular resilience
testing with result sharing. [VERIFY]

---

### 12. Exit Assistance and Data Portability

This clause category is critical for cloud procurement. Review with EU Data Act
compliance if EU-connected services are involved.

**EU Data Act Chapter VI obligations (applicable from 12 September 2025 [VERIFY]):**

- **Switching right**: Customer may request switching to another cloud provider (or on-premise)
  at any time, subject to a maximum 2-month advance notice period
- **Transitional period**: Maximum 30 days during which the outgoing provider must:
  (a) continue providing the service; (b) provide reasonable assistance to the customer
  and incoming provider; (c) maintain business continuity; (d) disclose known risks;
  (e) maintain security
- **Data retrieval window**: Minimum 30 days after the transitional period ends for
  customer to retrieve data
- **Data deletion**: All digital assets and exportable data must be erased after the
  retrieval window, unless agreed otherwise
- **Switching fees**: From 12 September 2025 to 12 January 2027: fees permitted but
  capped to actual direct costs (including data egress charges); from 12 January 2027:
  switching fees prohibited. [VERIFY current fee cap implementation]

**Key elements to review (beyond Data Act minimum):**
- Export data formats: open, machine-readable, documented formats vs. proprietary formats
- API access for export: whether customer can use APIs to export data programmatically
- Written deletion certification: provider certifies in writing that all customer data
  and copies have been securely deleted
- Exit assistance scope: technical assistance beyond data export (e.g., configuration
  migration, documentation handover)
- Transition period duration: contractual commitment for 90–180 days for complex migrations

**Common issues:**
- No exit assistance obligation — service simply terminates, leaving customer data
  inaccessible or deleted immediately
- Proprietary data export format requiring provider's own tools to read — functional
  lock-in even after export
- Data deletion on termination occurs immediately, before customer can complete export
- High egress fees that function as exit penalties (illegal under EU Data Act from
  12 January 2027; capped to actual cost until then)
- Transition period too short for complex migrations (30 days for enterprise data
  migrations is often inadequate)

---

### 13. Regulatory Compliance Allocation

**Key elements to review:**
- **HIPAA Business Associate Agreement (BAA)**: Required if PHI is processed. Must address:
  permitted uses and disclosures, safeguards, breach notification, sub-agent obligations,
  return or destruction of PHI on termination, access rights. Without a BAA, both parties
  are in HIPAA violation. [VERIFY]
- **PCI DSS 4.0 Responsibility Matrix**: Cloud provider must publish and contractually
  commit to its share of PCI DSS controls; customer's share must be documented. Required
  if payment card data is processed within the cloud environment. [VERIFY]
- **DORA Art. 30 mandatory minimum provisions** (financial sector, applied 17 January 2025):
  Written agreement must include at minimum [VERIFY]: (a) full service description; (b)
  location(s) where data is processed; (c) data security provisions; (d) access, recovery,
  and return of data; (e) service continuity arrangements; (f) DR testing provisions;
  (g) exit strategy provisions; (h) notice requirements for changes materially affecting
  the arrangement; (i) cooperation obligation with competent authorities; (j) audit rights
  (including regulatory authority access for CTPPs)
- **FedRAMP**: If the customer is a US federal agency or federal contractor, cloud provider
  must have current FedRAMP authorization at the applicable impact level (Low, Moderate,
  High). Contracts should reference the FedRAMP authorization and authorization to operate.
- **Government access requests (CLOUD Act)**: US authorities may compel US-based providers
  to produce data stored anywhere globally (18 U.S.C. § 2713 [VERIFY]). EU customers
  contracting with US-headquartered providers face CLOUD Act exposure. Contract should
  require provider to: (a) notify customer of government access requests where legally
  permitted; (b) commit to challenging overreaching requests; (c) publish transparency
  reports covering aggregate government access requests

**Common issues:**
- HIPAA BAA absent or attached but materially deficient
- PCI DSS responsibility matrix not provided or outdated (PCI DSS 4.0 effective 1 April
  2024; PCI DSS 4.0.1 effective 1 April 2025 — verify current version [VERIFY])
- DORA Art. 30 mandatory provisions absent for financial sector customers — regulatory
  violation from 17 January 2025
- Government access request notification limited by "applicable law" without provider
  committing to challenge overreaching requests
- No data sovereignty commitment for EU customers contracting with US providers

---

### 14. Unilateral Modification Rights

This is one of the most asymmetric provisions in cloud agreements and frequently the
source of post-signing commercial disputes.

**Key elements to review:**
- Provider's right to modify: (a) service features/functionality; (b) pricing; (c)
  policies (AUP, security policy, sub-processor list); (d) SLA commitments; (e) these
  terms themselves
- Notice period for modifications: advance notice before taking effect (30, 60, 90 days?)
- Customer's right to terminate for convenience if a material adverse modification is
  made (without early termination fee or penalty)
- Distinction between: minor updates (may be unilateral with short notice), material
  changes (longer notice + termination right), and pricing changes (price lock vs. CPI
  cap vs. no protection)

**Common issues:**
- Provider may modify service features or SLA commitments unilaterally with 30-day notice
  and no customer right to terminate (customer is locked into a degraded service)
- Price escalation clause unlimited (not capped at CPI or fixed percentage)
- AUP and security policy changes take effect immediately upon provider posting to website
  without advance notice
- Provider may "discontinue" features at will, including features customer relies on
- No distinction between material and non-material changes

**Market standard:**
- 90-day advance notice for material changes (pricing, material feature removals, SLA reductions)
- 30-day advance notice for non-material changes
- Customer right to terminate for convenience (no penalty) if a notified material change
  is adverse to the customer and the parties cannot agree on a resolution
- Multi-year pricing lock (or cap at CPI) for the committed subscription period

---

### 15–22. Standard Clause Checklist

For the following clause categories, review presence, reasonableness, and alignment with
playbook. Flag deviations using the GREEN/YELLOW/RED system.

**15. Term, Termination, and Auto-Renewal**
- [ ] Initial term reasonable for the service type
- [ ] Auto-renewal: notice window to prevent renewal is sufficient (60–120 days minimum)
- [ ] FTC Auto-Renewal Rule compliance (US) [VERIFY; FTC enforcement active 2024–2025]
- [ ] Termination for convenience: available? notice period? early termination fee?
- [ ] Termination for cause: cure period (typically 30 days), material breach definition
- [ ] Wind-down period: data export window, service continuity during notice period
- [ ] Survival: what obligations survive termination (confidentiality, IP, payment)?

**16. Governing Law and Dispute Resolution**
- [ ] Governing jurisdiction is acceptable and commercial (not unusually remote)
- [ ] Dispute escalation: negotiation, mediation before formal proceedings?
- [ ] Arbitration vs. litigation: institution (ICC, AAA, LCIA), seat, rules?
- [ ] EU: Jurisdiction clause compatible with Brussels I Recast (for EU customers)?
- [ ] Class action waiver / jury waiver (US): present and enforceable under applicable law?

**17. Payment and Fees**
- [ ] Net payment terms specified (Net 30 is standard; Net 60+ is customer-favorable)
- [ ] Late payment interest rate defined (not penalty-rate)
- [ ] Data egress fees: disclosed, capped, or unlimited? (EU Data Act capping from 2025)
- [ ] Overage charges: defined and capped or uncapped?
- [ ] Price escalation: CPI cap, fixed percentage, or unlimited?
- [ ] Disputed invoice process: customer may withhold disputed amounts without late fee

**18. Confidentiality**
- [ ] Customer data classified as confidential
- [ ] Provider's permitted disclosures (employees with need to know, sub-processors under NDA)
- [ ] Provider's right to disclose: government requests, legal obligation, with notice
- [ ] Confidentiality term (2–5 years; indefinite for trade secrets)
- [ ] Return or deletion of confidential information on termination (aligns with data portability)

**19. Assignment and Change of Control**
- [ ] Customer consent required for assignment (or not to be unreasonably withheld)
- [ ] **Change of control (provider acquired)**: Customer right to terminate if provider is
  acquired by a direct competitor — critical for cloud services where competitive intelligence
  risk is high
- [ ] Customer's affiliate assignment right (no consent required for intra-group transfers)

**20. Force Majeure**
- [ ] Scope: specific events listed, not just "acts of God"
- [ ] Provider infrastructure failures NOT included as force majeure (provider controls its own infrastructure)
- [ ] Notification and mitigation obligations on claiming party
- [ ] Duration threshold before customer termination right arises (typically 30–60 days)
- [ ] Credit obligations continue during force majeure period (if SLA credits are the remedy)

**21. Compliance and Regulatory (General)**
- [ ] Anti-bribery and anti-corruption (UK Bribery Act 2010, US FCPA, local equivalents)
- [ ] Sanctions and export control compliance representations
- [ ] Modern slavery statement (if required by applicable law)

**22. Definitions and Boilerplate**
- [ ] Order of Precedence: clearly defined for multi-document agreements
- [ ] Entire Agreement: covers all documents forming the agreement
- [ ] Amendment: written amendments only; click-through acceptance of revised terms limited
- [ ] Notices: method, deemed receipt, addresses for legal notices
- [ ] No third-party beneficiaries (or appropriate carveout for data subjects / regulators)

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than the organization's standard position. Minor
variations that are commercially reasonable and do not materially increase risk.

**CSA examples:**
- SLA uptime at 99.99% when standard is 99.95%
- Sub-processor notification at 14 days when standard is 14 days
- Data deletion within 30 days when standard is 30 days
- Credit at 25% of monthly fees when standard is 25%

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the standard position but within a negotiable range. Requires
attention and likely negotiation, but not escalation.

**CSA examples:**
- SLA uptime at 99.9% when standard is 99.95% (missed by 0.05 nines)
- Sub-processor notification at 10 days (below 14-day standard but not egregious)
- AI training right on aggregated data without anonymization standard definition
- Liability cap at 6 months fees when standard is 12 months
- Exit assistance limited to 30 days for a complex enterprise migration
- Auto-renewal notice window at 30 days when standard is 60 days
- Provider change-of-control: customer right to terminate but with 60-day delay

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Escalate

The clause poses material risk, triggers a defined escalation criterion, or conflicts
with mandatory regulatory requirements.

**CSA examples:**
- No DPA when personal data of EU/UK residents is processed (GDPR Art. 28 violation)
- SLA credits as exclusive remedy for **all** contractual failures including data breach
- No security incident notification timeline (GDPR 72-hour reporting risk)
- Provider retains right to use identifiable customer data for AI training with no opt-out
- No exit assistance: data deleted at termination with no retrieval window
- DORA mandatory Art. 30 provisions missing for financial sector customer
- Liability cap at 1 month's fees for a business-critical infrastructure service
- Blanket sub-processor authorization with no notification obligation
- No deletion certification post-termination (data sovereignty / GDPR risk)
- Government access requests: provider notifies government before customer (reversed order)

**Action**: Explain the specific risk (with legal basis and regulatory citation where
possible). Provide market-standard alternative language. Estimate exposure. Recommend
escalation path (senior counsel, CISO, DPO, regulatory counsel as appropriate).

---

## Redline Format

For each redline:
```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote or accurate paraphrase]"
**Issue**: [One sentence on why this is a problem]
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences, suitable for sharing with provider's counsel]
**Legal/regulatory basis**: [Statute, regulation, or market standard — or "General
commercial practice" — mark unverified with [VERIFY]]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language, not vague guidance. The redline should be ready to insert.
2. **Distinguish hyperscaler vs. mid-market**: Hyperscaler standard terms rarely move on
   liability, fee structure, or platform governance. Focus negotiation efforts on the DPA
   addendum, security addendum, and enterprise order form where flexibility is greater.
3. **Regulatory minimum vs. negotiation ask**: Clearly label redlines that are regulatory
   minimums (non-negotiable legally) vs. commercial asks (negotiable).
4. **Provide fallback positions**: For YELLOW items, include a fallback if the primary
   ask is rejected.
5. **Reference applicable law**: Where the redline addresses a regulatory minimum, cite
   the specific provision. If citing from memory, mark with [VERIFY].
6. **Consider the relationship**: A long-term strategic cloud relationship warrants
   collaborative tone; a commodity SaaS vendor gets firmer language.

---

## Negotiation Priority Framework

Organize redlines by negotiation priority:

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:
- GDPR Art. 28 DPA absent or materially deficient — cannot process EU/UK personal data
- HIPAA BAA absent — cannot store or process PHI
- DORA Art. 30 mandatory provisions missing — regulatory violation from day one
- No security incident notification timeline — unable to meet GDPR 72-hour obligation
- Provider right to use identifiable customer data for AI training with no opt-out
- No exit assistance / data retrieval rights — vendor lock-in with no legal exit
- SLA credits as exclusive remedy for data breach or extended outage in excess of [X] hours
- Liability cap under [minimum acceptable level] for the service criticality

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:
- Data breach super-cap (higher cap or uncapped for data protection failures)
- Sub-processor advance notice window extension (14 → 30 days)
- Direct audit right alongside SOC 2 substitution (trigger-based)
- Prohibition on aggregated/anonymized data use for AI training
- Exit assistance duration extension (30 → 90+ days for complex migrations)
- Change-of-control termination right (immediate, no-penalty)
- Unilateral modification notice extension (30 → 90 days for material changes)
- Uptime commitment upgrade (99.9% → 99.95% or 99.99%)

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:
- Preferred governing law (if alternative is acceptable)
- Customer-managed encryption keys (BYOK) for non-regulated data
- Benchmark restriction carveout (if no security testing planned)
- Price lock for multi-year term (if pricing is acceptable)
- Minor SLA credit percentage increases above market standard

**Negotiation strategy**: Lead with Tier 1 (regulatory minimums — present as compliance
requirements, not preferences). Trade Tier 3 concessions to secure Tier 2 wins.
Never concede on Tier 1 without CISO/DPO/regulatory counsel sign-off.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow a consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments or repeal (especially: DORA applied Jan 2025; EU Data Act applicable Sep 2025; PCI DSS 4.0.1 from Apr 2025; ISO 27017 revision underway) | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within the contract's governing law. No jurisdictional bleed | Remove or flag |
| **Confidence** | Uncertainty explicitly stated, not hidden | Add confidence qualifier |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:
- Does the risk assessment follow logically from the statute/principle cited?
- Would a regulator or court actually reach this conclusion on these facts?
- Is there a counter-argument the provider's counsel will make?

**Pass 2 — Completeness**:
- Have all relevant statutes and regulations been considered?
- Are there any DORA, GDPR, NIS2, or Data Act dimensions not yet addressed?
- Have any relevant regulatory guidance documents been missed?

**Pass 3 — Challenge**:
- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable legal professional accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations
  (e.g., the clause is aggressive but the deal is strategic and leverage is limited)?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law or clear regulatory mandate (e.g., GDPR Art. 28 DPA requirement) | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions (e.g., DORA Art. 30 mandatory terms) | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ (e.g., whether aggregated data is "anonymous" under GDPR recital 26) | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., enforceability of SLA credits as exclusive remedy for all claims) | Flag for counsel with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every cloud service agreement review output MUST include this audit section:

```yaml
glass_box:
  contract: "[Agreement title and date]"
  contract_type: "[CSA / SaaS Agreement / Cloud MSA / Order Form / IaaS / PaaS]"
  user_side: "[Customer / Provider]"
  governing_law: "[Jurisdiction identified from the agreement]"
  data_protection_regime: "[GDPR / UK GDPR / CCPA / HIPAA / Multiple / None identified]"
  regulated_industry: "[Financial services (DORA) / Healthcare (HIPAA) / Government (FedRAMP) / General / Unknown]"
  playbook_used: "[Playbook name or 'General market standards']"
  review_basis: "[Organizational playbook / General market standards]"
  clauses_reviewed: 22
  clauses_present: "[number]"
  clauses_missing: "[number] — [list key absences]"
  dpa_compliance_checked: "[Yes / No — reason]"
  dora_compliance_checked: "[Yes — financial sector / No — general commercial]"
  data_act_compliance_checked: "[Yes — EU-connected services / No]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) / UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review (and DPO / regulatory counsel review where data protection or regulated-industry obligations are in scope)"
```

---

## Multi-Stakeholder Mapping

Cloud service agreements affect multiple stakeholders beyond the contracting parties:

| Stakeholder | Role | Affected Clauses | Key Concern | Action Required |
|-------------|------|-----------------|-------------|----------------|
| Customer | Primary | All | Service reliability, data control, cost | Sign / Negotiate |
| Provider | Primary | All | Liability, operational flexibility, revenue | Sign / Negotiate |
| Data subjects | Third party | DPA, sub-processors, data breach | Privacy rights, breach notification | DPA required |
| Sub-processors | Third party | Sub-processor, DPA, security | Flow-down obligations | Notification rights |
| DPA supervisory authority | Regulator | DPA, security, breach notification | GDPR compliance | Breach reporting obligation |
| Financial regulator | Regulator (if DORA) | DORA Art. 30 terms, audit rights | Operational resilience | DORA compliance verification |
| CISO / Security team | Internal | Security, SLA, DR, audit | Technical controls, incident response | Security review required |
| DPO | Internal | DPA, sub-processors, transfers | GDPR compliance | DPO sign-off required |
| Procurement / Finance | Internal | Payment, auto-renewal, egress fees | Cost exposure | Budget alignment |

---

## Anti-Patterns

Explicit catalogue of what NOT to do when reviewing cloud service agreements:

1. **Accepting "commercially reasonable efforts" SLAs without numeric commitments** —
   "Commercially reasonable efforts" creates no enforceable uptime floor. Credits against
   a non-committal SLA are meaningless. Always push for numeric uptime percentages.

2. **Missing the exclusive-remedy trap** — A credits-as-sole-remedy clause that applies
   to "any failure to meet service levels" may, depending on how SLAs are defined,
   eliminate the customer's right to claim breach of contract, indemnification, or tort
   claims for extended outages, data loss, or degraded performance. Read the SLA, the
   limitation clause, and the indemnity clause together before classifying.

3. **Ignoring the carveout structure of the liability cap** — A cap with no data breach
   or confidentiality carveout means a catastrophic data breach is subject to the same
   nominal cap as a routine service dispute. Review carveouts as carefully as the cap itself.

4. **Failing to check whether the DPA includes 2021 EU SCCs** — A GDPR DPA without
   incorporated 2021 SCCs for cross-border transfers leaves EU personal data transfers
   to third countries without a legal mechanism. This is a regulatory violation, not a
   commercial preference.

5. **Treating "de-identified" as "anonymous" under GDPR** — Pseudonymized data is still
   personal data under GDPR (Recital 26 [VERIFY]). Provider rights to use "de-identified"
   or "pseudonymized" customer data may still constitute personal data processing.
   True anonymization requires irreversibility; always check the definition used.

6. **Ignoring EU Data Act Chapter VI for EU-connected services** — From 12 September 2025,
   new cloud contracts with EU-connected services must include compliant switching and
   exit provisions. Absence is a legal violation, not just a commercial weakness.

7. **Skipping the DORA Art. 30 checklist for financial sector customers** — For financial
   entities under DORA, the mandatory minimum contract provisions are non-negotiable.
   Missing any Art. 30 item from the cloud contract is a regulatory violation from
   17 January 2025. Treat absent DORA provisions as RED regardless of commercial context.

8. **Accepting sub-processor "blanket authorization" without a notification mechanism** —
   GDPR Art. 28(2) requires the controller to be given the opportunity to object before
   any sub-processor change. Blanket authorization with no advance notice mechanism
   removes this right in practice.

9. **Conflating SLA uptime with DR/RPO commitments** — A 99.99% monthly uptime SLA
   tells you about availability but nothing about data recovery after a failure. A service
   can be restored within the SLA window with hours of data loss. RTO and RPO must be
   separately specified.

10. **Not reading the Order of Precedence clause** — In multi-document agreements (MSA +
    Order Form + SLA + DPA), the Order of Precedence determines which document governs
    conflicts. A DPA that is subordinate to the MSA may be overridden by conflicting MSA
    terms — undermining GDPR Art. 28 compliance.

11. **Ignoring the provider's AI training use clause** — Many agreements contain a
    service improvement right that predates generative AI awareness. "Improve our services
    using aggregated data" in a 2019 agreement may now extend to training LLMs. Do not
    assume this is benign; flag for specific analysis.

12. **Treating government access request provisions as boilerplate** — For EU customers
    contracting with US-headquartered providers, CLOUD Act exposure is a material data
    sovereignty risk. Review the government access request notification provisions and
    the provider's transparency report commitment.

13. **Missing the egress fee trap** — High data egress fees can function as exit penalties,
    making switching prohibitively expensive. Under the EU Data Act, switching fees will
    be prohibited from 12 January 2027 and capped until then. Review egress pricing as
    part of the exit assistance analysis.

14. **Reviewing the CSA without the provider's current security policy** — Security
    commitments in the CSA often cross-reference the provider's Security Policy as a
    schedule or incorporated document. If the security policy is changeable unilaterally
    by the provider (as it often is), the security commitment in the CSA is effectively
    only as strong as the provider's current goodwill.

15. **Assuming the BAA covers everything** — A HIPAA Business Associate Agreement
    is necessary for HIPAA compliance, but it is not sufficient. The overall CSA must
    also be reviewed for provisions that create HIPAA compliance gaps (e.g., broad data
    use rights that conflict with the BAA's use restrictions).

16. **Failing to review all documents in the agreement** — Cloud agreements are frequently
    multi-document: MSA, Order Form, DPA, SLA Schedule, Security Policy, AUP,
    Sub-processor List. Key protections may be in schedules; key risks may be hidden in
    policies incorporated by reference. Review all documents.

17. **Classifying hyperscaler standard terms as negotiable without checking their
    enterprise addendum** — AWS, Azure, and Google Cloud have different negotiability
    levels for their standard agreement vs. their enterprise addendum / DPA. Many customer
    protections (DORA addenda, HIPAA BAAs, customer-managed keys) are available through
    the addendum process, not the standard terms.

18. **Missing benchmark restrictions when security testing is planned** — Providers
    routinely prohibit publishing benchmark results; many also restrict pen testing of
    the customer's own deployed environment. If the customer's CISO plans security
    testing, these restrictions must be negotiated upfront.

19. **Ignoring the auto-renewal notice window against a busy contract calendar** — A
    90-day auto-renewal notice window means the customer must decide on renewal 90 days
    before the anniversary. Missing this window locks the customer into another year.
    Flag the critical date explicitly and recommend calendar entry.

20. **Not recommending DPO and CISO review for data-intensive agreements** — Legal review
    alone is insufficient for cloud agreements where the technical security commitments
    and data processing details require CISO and DPO input. Always flag when technical
    or data protection specialist review is required alongside legal review.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (may be shared with provider's counsel):
- Plain language; no jargon or filler
- Active voice: "The provider must notify within 24 hours" not "Notification within 24 hours is required"
- Short sentences; one point per sentence
- Name the actor and the obligation
- Cite the regulatory basis where applicable

**For internal analysis**:
- Same plain-language standards; technical legal analysis as needed
- Confidence qualifiers applied throughout
- Glass Box audit trail appended

**Quality gates before delivery**:
1. Can a non-lawyer senior stakeholder (CFO, CISO, CPO) understand the executive summary?
2. Can the provider's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation or flagged [VERIFY]?
4. Are DORA / GDPR / Data Act mandatory requirements clearly distinguished from commercial preferences?
5. Does the output include the Glass Box audit trail?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- In Step 4, search for jurisdiction-relevant statutes, regulations, and case law
- Prioritize: GDPR Art. 28 structure; EU Data Act Arts. 23–26 switching requirements;
  DORA Art. 30 mandatory provisions; applicable SCCs; NIS2 Directive; jurisdiction-specific
  exclusion clause enforceability rules
- Save results to `/tmp/legalcode-csa-authority.md`
- Reference verified authority throughout clause analysis
- For RED items, search for additional regulatory guidance to support or challenge classification
- Check currency of statutes (DORA applied Jan 2025; Data Act applicable Sep 2025;
  PCI DSS 4.0.1 from Apr 2025; ISO 27017 revision underway 2025–2026)
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all statutory and regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice that regulatory citations require independent verification
- Focus analysis on structural and commercial risk assessment rather than regulatory certainty
- Do not create the local authority reference file

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Cloud Service Agreement Review

**Agreement**: [title and identifier]
**Parties**: [Customer name] (Customer) and [Provider name] (Cloud Service Provider)
**Your Side**: [Customer / Provider]
**Governing Law**: [jurisdiction]
**Data Protection Regime**: [GDPR / UK GDPR / CCPA / HIPAA / Multiple / None]
**Regulatory Status**: [DORA / HIPAA / FedRAMP / General commercial]
**Review Basis**: [Playbook name / General market standards]
**Date of Review**: [date]

---

## Executive Summary

[3–5 bullet points: overall risk rating, critical issues, regulatory exposure, top
negotiation asks. Written for a senior non-lawyer (CFO, CPO, COO).]

---

## Key Findings

| Issue | Severity | Regulatory Dimension | Priority |
|-------|----------|---------------------|----------|
| [issue] | RED/YELLOW | [GDPR / DORA / None] | Must-have / Should-have |

---

## Missing Clauses

[List clause categories absent from the agreement, with severity and regulatory impact]

---

## Clause-by-Clause Analysis

### [#]. [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Agreement says**: [summary of the provision]
**Market standard / playbook**: [benchmark position]
**Deviation**: [description of gap]
**Regulatory dimension**: [GDPR Art. X / DORA Art. Y / Data Act Art. Z / None]
**Business impact**: [practical risk — financial exposure, regulatory risk, operational impact]
**Redline** (if YELLOW or RED):
> [Specific proposed language]
**Fallback**: [alternative position]

[Repeat for each clause category]

---

## Negotiation Strategy

**Tier 1 — Must-Haves (Regulatory / Deal-Breakers)**: [list]
**Tier 2 — Should-Haves (Material Commercial Asks)**: [list]
**Tier 3 — Concession Candidates**: [list]

**Recommended sequencing**: [Lead with regulatory must-haves (GDPR DPA, DORA) as
compliance requirements. Use Tier 3 concessions to secure Tier 2 commercial asks.]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Critical Dates

| Date / Trigger | Action Required | Owner |
|----------------|----------------|-------|
| [Auto-renewal notice deadline] | Send notice to avoid renewal | [Legal / Procurement] |
| [DORA review deadline if applicable] | Verify Art. 30 compliance | [DPO / Legal] |
| [Data Act compliance date 12 Sep 2025] | Update exit assistance provisions | [Legal] |

---

## Next Steps

[Specific actions: who sends redlines, who reviews DPA, who engages DPO/CISO,
what is the deadline, when is the next negotiation session]

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To apply jurisdiction-specific analysis:

1. **EU / EEA services**: Replace [JURISDICTION-SPECIFIC] markers with GDPR, Data Act,
   and NIS2 content verified against current legislation. Confirm whether the customer
   is subject to DORA (financial sector).
2. **UK services**: Apply UK GDPR + DPA 2018 overlay; UK IDTA or UK Addendum to EU SCCs;
   UCTA 1977 for exclusion clause enforceability.
3. **US services**: Apply state-specific data protection laws (CCPA/CPRA for California),
   breach notification laws (all 50 states), HIPAA for PHI, FedRAMP for federal agencies.
4. **Financial sector (any jurisdiction)**: Apply DORA (EU/EEA), FCA SS2/21 (UK), OCC
   guidance (US), and relevant local financial services regulation.

The `legalcode-contract-review` skill provides the base commercial framework that this
skill supplements for cloud-specific obligations.

---

## Provenance

Created by Legalcode (2026-03-22). Native Legalcode synthesis for cloud and hosted-service
agreement review, replacing the imported `cloud-service-agreement` skill
(`general/contracts/imported-open-agreements--skills-cloud-service-agreement/SKILL.md`),
which covers drafting only. Research basis: EU Data Act (Reg. 2023/2854, Chapter VI);
DORA (Reg. 2022/2554, Arts. 28–30); GDPR Art. 28; NIS2 Directive (2022/2555); 2021 EU
SCCs (Commission Decision C(2021)3972); CCPA/CPRA; ISO/IEC 27001/27017/27018; SOC 2
Type II (AICPA TSC); CSA STAR; PCI DSS 4.0.1; FedRAMP; CLOUD Act (18 U.S.C. § 2713);
SLA uptime mechanics (uptime.is); Fastcase v. Alexi Technologies (2025) AI training
data risk; California SB 446 (effective 1 Jan 2026); DORA CTPP first designation list
(November 2025); AWS / Azure / Google Cloud standard SLA structures (market reference).
Structured following the legalcode-contract-review gold standard (2026-02-27).
