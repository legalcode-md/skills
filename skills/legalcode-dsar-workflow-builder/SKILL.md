---
name: legalcode-dsar-workflow-builder
description: >
  Build and execute end-to-end Data Subject Access Request (DSAR) operational workflows
  covering intake normalization, identity and authority verification, jurisdiction mapping,
  scope determination, data discovery across all systems, legal basis review, exemption
  analysis (trade secrets, third-party data, legal privilege, manifestly unfounded/excessive,
  national security, ongoing investigations), redaction protocols with proportionality
  review, response assembly, notice drafting, timeline management, and post-dispatch
  monitoring. Supports GDPR Article 15, CCPA/CPRA, UK GDPR/DPA 2018, LGPD (Brazil), and
  PIPEDA (Canada). Includes escalation paths, template responses, compliance documentation,
  and a full Glass Box audit trail. Use when receiving a DSAR or right-to-know request
  from any individual, managing backlog of open requests, building a DSAR process program,
  or auditing an existing DSAR response for defensibility.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode DSAR Workflow Builder

> **Disclaimer**: This skill provides a framework for AI-assisted Data Subject Access
> Request operations. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional or Data Protection Officer licensed or operating in the
> relevant jurisdiction before any data is disclosed or withheld. Privacy laws change and
> regulator guidance evolves; verify current applicability before relying on any deadline,
> exemption, or procedure described here. Legal references cited from training data carry
> hallucination risk — verify against authoritative sources before relying on them. Mark
> any unverified citation with **[VERIFY]**.

---

## Purpose and Scope

This skill builds and executes a complete, operationally actionable DSAR workflow from
intake through dispatch and post-response monitoring. It is designed for privacy teams,
legal operations teams, and compliance professionals who need a defensible, auditable
process that works across the five major data subject access regimes.

**This skill covers:**
- Intake normalization from any channel (email, web form, phone, certified mail, in-person)
- Identity and authority verification (individual, agent, guardian, attorney, executor)
- Jurisdiction mapping and deadline calculation across GDPR, UK GDPR, CCPA/CPRA, LGPD, PIPEDA
- Scope clarification and data category determination
- Data discovery orchestration across structured and unstructured systems
- Exemption analysis with three-pass self-interrogation for each exemption claimed
- Redaction operations with proportionality review
- Response assembly (data package + cover notice)
- Template notice drafting with jurisdiction-specific variables
- Timeline tracking and extension trigger analysis
- Vendor/processor coordination for data held by third parties
- QA framework with Citation Quality Gates and Confidence Scoring
- Glass Box audit trail for regulator defensibility
- Escalation paths for borderline exemption decisions
- Post-dispatch monitoring for appeals and supplemental requests

**This skill does not:**
- Provide legal advice or replace qualified Data Protection Officer review
- Guarantee regulatory approval or exemption from enforcement
- Draft or review privacy policies (see `legalcode-privacy-policy-drafter`)
- Conduct Data Protection Impact Assessments (see `legalcode-dpia-generator`)
- Assess breach notification obligations (see `legalcode-breach-severity-assessment`)
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers throughout

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic with coverage built for the five major DSAR regimes.
The applicable regime is determined in Step 3 based on the data subject's residence,
the organization's location, and the applicable sectoral rules.

### Regime Overview

| Regime | Primary Instrument | Response Deadline | Extension | Fee |
|--------|--------------------|-------------------|-----------|-----|
| **EU GDPR** | GDPR Article 15 + EDPB Guidelines 01/2022 | 1 calendar month | +2 months (complex/multiple) | Free; reasonable fee for manifestly excessive |
| **UK GDPR** | UK GDPR Article 15 + DPA 2018 | 1 calendar month | +2 months | Free (with narrow exceptions) |
| **CCPA/CPRA** | Cal. Civ. Code § 1798.100 + CPPA Regs | 45 calendar days | +45 days | Free; limit 2 per 12 months |
| **LGPD (Brazil)** | LGPD Articles 18–19 | 15 calendar days | +15 days | [JURISDICTION-SPECIFIC] |
| **PIPEDA (Canada)** | PIPEDA Principle 9 + OPC Guidance | 30 days (OPC recommendation) | Reasonable extension | Minimal / nil |

[JURISDICTION-SPECIFIC] Before finalizing deadline calculations, localize:
- Member State-specific implementation derogations (EU GDPR)
- DPA 2018 Schedule 2 exemption list (UK GDPR)
- California Privacy Protection Agency regulations updated post-2023 (CCPA/CPRA)
- ANPD enforcement posture and sector-specific LGPD guidance (Brazil)
- Provincial privacy law overlaps (PIPEDA vs. PIPEDA-substantially-similar provinces)
- Sector-specific rules: HIPAA, FERPA, GLBA (US healthcare/education/financial sectors)
- Applicable national security or law enforcement carve-outs

---

## Interactive Clarification

This skill uses **CLARIFY** prompts at five decision points where the answer materially
changes the direction or output of the workflow. Do not proceed on assumptions when the
decision fork is marked **CLARIFY** — pause and ask the user.

CLARIFY format used throughout:
```
**CLARIFY** — [Decision Point Name]
1. [Question]
   - Options: A / B / C
   - *Why it matters*: [consequence of each choice]
```

If context has already been provided, skip the CLARIFY and proceed, but state your
assumption explicitly.

---

## Workflow

### Step 1: Intake and Request Normalization

Accept the DSAR in any channel format and normalize into a canonical request record.

**Supported intake channels:**
- **Email**: forward to designated privacy inbox
- **Web form**: structured intake via privacy portal or cookie consent platform
- **Certified mail / postal**: scan and log
- **Phone**: documented verbally, reduced to writing (request caller to confirm in writing)
- **In-person**: identity verification on-site; reduce to writing

**Canonical Request Record fields:**

| Field | Value |
|-------|-------|
| Request ID | `DSAR-[YYYY]-[MM]-[NNN]` (assign on intake) |
| Request Date | Date received (channel-dependent — email receipt, postmark, form timestamp) |
| Legal Clock Start | Date organization became "aware" of request — this is the statutory trigger |
| Delivery Channel | Email / Web Form / Postal / Phone / In-Person |
| Requester Name (Claimed) | As stated |
| Requester Contact | Email, address, or phone |
| Claimed Relationship | Self / Agent / Attorney / Guardian / Executor / Other |
| Stated Scope | What the requester is asking for |
| Urgency Flags | Time-sensitive circumstances stated by requester |
| Assigned Owner | Privacy team member responsible |

**CLARIFY** — Step 1: Request validity screening

1. **Does the request on its face constitute a valid DSAR?**
   - Options: Clear DSAR (proceed), Ambiguous (treat as DSAR provisionally and clarify with requester), Not a DSAR (route to other process)
   - *Why it matters*: Treating a non-DSAR inquiry as a DSAR wastes resources; failing to recognize a DSAR triggers the statutory clock and risks deadline miss.

2. **Is the request clearly manifestly unfounded or manifestly excessive?**
   - Options: No (proceed), Borderline (document and proceed while assessing), Yes — abuse pattern evident
   - *Why it matters*: Manifestly unfounded/excessive requests may be refused or subject to fee (GDPR Art. 12(5), UK GDPR equivalent) — but the bar is high. Mis-classifying a legitimate request risks enforcement action.

**Action items for Step 1:**
- Assign Request ID
- Log Legal Clock Start date
- Acknowledge receipt to requester (in writing, within 24-48 hours)
- Assign owner
- Note any urgency flags

---

### Step 2: Identity and Authority Verification

Verify that the person submitting the request is (a) who they claim to be, and
(b) authorized to receive the requested data.

**CLARIFY** — Step 2: Verification level

1. **What is the risk level of this request?**
   - Options: Low (individual known to us, data not sensitive), Medium (individual partially known, some sensitive data likely), High (individual unknown, sensitive data likely, or large-scale)
   - *Why it matters*: Verification burden scales with risk. Requesting more information than necessary itself violates data minimization principles.

2. **Is a third party claiming to act on behalf of the data subject?**
   - Options: No — request directly from data subject, Yes — attorney/agent, Yes — parent/guardian, Yes — executor/administrator of estate
   - *Why it matters*: Third-party authority requires additional verification (power of attorney, guardianship order, letters of administration, signed authorization letter).

#### Identity Verification Matrix

| Risk Level | Minimum Verification |
|------------|---------------------|
| **Low** | Email confirmation (reply from known account) or account-authenticated portal request |
| **Medium** | Email confirmation + one additional factor: (a) answer to security question, (b) confirm last-4 of account number, or (c) date of last transaction/interaction |
| **High** | Two independent factors including at least one government-document-based check: (a) government ID excerpt (last-4 of ID number + name), (b) live video or in-person check, or (c) notarized declaration |
| **Special Category Data** | Treat as High + require written consent and destruction of verification materials post-check |

**Third-party authority verification requirements:**
- **Attorney**: signed engagement letter or bar-verified representation letter
- **Agent**: signed written authorization from data subject (wet ink or qualified electronic signature)
- **Parent/Guardian**: documentation of legal guardianship (birth certificate for minors; court order for incapacitated adults)
- **Executor**: grant of probate, letters of administration, or equivalent

**Verification evidence handling:**
- Store verification materials in a designated secure folder, access-restricted to DSAR team
- Delete verification artifacts within [30/90] days of response dispatch [JURISDICTION-SPECIFIC]
- Never use verification data for any purpose other than identity check
- Log: `verification_method`, `verification_date`, `verifier_name`, `verification_confidence`

[JURISDICTION-SPECIFIC] Note:
- GDPR/UK GDPR: Controllers "may" request additional information to verify identity but only when there are "reasonable doubts" (EDPB Guidelines 01/2022 §4)
- CCPA/CPRA: "Verifiable consumer request" standard — verification method must be reasonably designed to confirm identity while minimizing collection
- LGPD: Verification requirements not explicitly specified; proportionality principle applies
- PIPEDA: Verification may be required; must not collect more than necessary for verification

---

### Step 3: Jurisdiction Mapping and Deadline Calculation

Identify all applicable data protection regimes and calculate the binding response deadline.

**Regime identification factors:**
- Data subject's place of residence (primary trigger for EU GDPR, UK GDPR, LGPD, CCPA/CPRA)
- Organization's establishment or targeting of individuals in-jurisdiction
- Sector-specific overlays (HIPAA, FERPA, GLBA, DPA 2018 sector schedules)
- Contractual obligations (processor agreements may impose shorter deadlines)

**Deadline calculation procedure:**

1. Identify the Legal Clock Start date (Step 1)
2. For each applicable regime, calculate:
   - **Base deadline**: Legal Clock Start + statutory period
   - **Extension eligibility**: Is the request complex? Multiple requests from same individual?
   - **Extension deadline**: Base deadline + statutory extension period
3. Apply the **strictest-safe rule**: use the shortest applicable deadline unless extension is justified and documented

**Deadline Reference Table:**

| Regime | Base Deadline Formula | Extension Trigger | Extension Period |
|--------|----------------------|-------------------|-----------------|
| EU GDPR | Clock Start + 1 calendar month | Complex request or multiple requests | +2 calendar months |
| UK GDPR | Clock Start + 1 calendar month | Complex request or multiple requests | +2 calendar months |
| CCPA/CPRA | Clock Start + 45 calendar days | Good cause (notify requester within 45 days) | +45 calendar days |
| LGPD | Clock Start + 15 calendar days | Justified (notify requester) | +15 calendar days |
| PIPEDA | Clock Start + 30 days (OPC recommendation) | Reasonable justification (notify requester) | Reasonable |

**Extension notification requirement:** If extending, notify the requester in writing within the
original deadline period. State the reason for the extension and the new deadline. Failure
to notify is itself a compliance violation.

**Output of Step 3:**
```
Jurisdiction Applicability Matrix:
- [Regime 1]: APPLICABLE / NOT APPLICABLE — Reason
- [Regime 2]: APPLICABLE / NOT APPLICABLE — Reason
Governing Deadline: [Date] ([Regime] [Base/Extension])
Extension Triggered: YES/NO — Reason
Extension Notice Sent: [Date] / NOT REQUIRED
Buffer Target: [Date] ([3-5 days before deadline])
```

---

### Step 4: Scope Clarification and Data Inventory

Determine exactly what data the request covers and which organizational systems are in scope.

**CLARIFY** — Step 4: Scope ambiguity check

1. **Is the request scope clear?**
   - Options: Clear ("all personal data you hold about me"), Ambiguous (subject used vague language), Scoped (subject specified categories or time periods)
   - *Why it matters*: A clear all-data request triggers comprehensive discovery; an ambiguous request may require a scoping clarification letter (which may toll the deadline [JURISDICTION-SPECIFIC]).

2. **Is the request potentially manifestly excessive?**
   - Options: No, Borderline (flag for assessment but proceed), Yes — genuinely excessive given volume or prior requests
   - *Why it matters*: Excessive requests may justify extension or (in narrow circumstances) refusal.

**Scope interpretation principles:**
- Default to broad interpretation when scope is ambiguous (error on side of transparency)
- "Personal data" includes all information that can identify the subject, directly or indirectly
- Includes derived and inferred data, behavioral profiles, and automated decision-making outputs
- Includes data in archived, backed-up, or legacy systems accessible with reasonable effort
- Does NOT include data that cannot reasonably be retrieved (disproportionate effort)

[JURISDICTION-SPECIFIC] CCPA/CPRA distinguishes between:
- Right to Know — Categories: broader, covers past 12 months by default
- Right to Know — Specific Pieces: targeted, must be responded to with actual data
- Confirm the request type before proceeding with discovery

**System inventory checklist — identify all systems potentially holding personal data:**

| System Category | Examples | In Scope? |
|----------------|---------|-----------|
| CRM | Salesforce, HubSpot, Dynamics | Assess |
| Email | Outlook/Exchange, Gmail | Assess |
| HR Systems | Workday, BambooHR, Personio | Assess if subject is/was employee |
| ERP/Finance | SAP, NetSuite | Assess |
| Marketing | Marketo, Mailchimp, Klaviyo | Assess |
| Support Ticketing | Zendesk, ServiceNow, Intercom | Assess |
| Analytics/BI | Google Analytics, Mixpanel, Amplitude | Assess |
| Data Warehouse | Snowflake, BigQuery, Redshift | Assess |
| File Storage | SharePoint, Dropbox, Google Drive | Assess |
| Communication | Slack, Teams, Zoom records | Assess |
| Product/App DB | Custom databases, event streams | Assess |
| Third-Party Processors | SaaS vendors, cloud services, outsourced functions | Coordinate per Step 5b |
| Archives & Backups | Legacy systems, tape/offline backups | Assess effort vs. obligation |

---

### Step 5: Data Discovery Execution

Execute discovery across all in-scope systems identified in Step 4.

#### Step 5a: Primary System Discovery

For each in-scope system, execute search using the subject's known identifiers:
- Primary email address
- Username or customer ID
- Name (with common spelling variants)
- Phone number
- National ID or account number (if known and verifiable)
- IP addresses or device identifiers (if applicable)

**Discovery protocol per system type:**

| System Type | Discovery Method | Completeness Check |
|-------------|-----------------|-------------------|
| Relational DB | SQL query on all tables with FK to user ID | Run row count before and after extraction |
| CRM | Export contact record + all related objects (activities, notes, opportunities) | Check "last modified" date to catch recent entries |
| Email | Full-text search on all From/To/CC/BCC fields + body search on name/ID | Include sent, received, drafts, deleted (if accessible) |
| File Storage | Metadata search on creator/editor + full-text search on name/ID | Check all folders including shared and archived |
| Analytics | Query on user ID / cookie ID / device ID | Note: often only aggregate data available |
| Backups | Only if data is not reasonably accessible elsewhere; document effort | Assess proportionality before executing |

**De-duplication:** After extracting from all systems, de-duplicate records appearing in
multiple systems. Maintain cross-reference: which record appears in which system(s).

**Discovery register format:**

| Record ID | Source System | Category | Description | Responsive? | Exemption Flag |
|-----------|--------------|----------|-------------|-------------|----------------|
| REC-001 | CRM | Identity | Name, email, phone | YES | None |
| REC-002 | Email | Communications | Support thread (subject + agents) | PARTIAL | Third-party names in agent replies |
| REC-003 | Analytics | Behavioral | Click-stream profile | YES | De-identification possible |

#### Step 5b: Vendor and Processor Coordination

Personal data held by processors (SaaS vendors, outsourced functions, cloud providers)
must also be gathered. [JURISDICTION-SPECIFIC]

**Processor coordination procedure:**
1. Identify all data processors contractually engaged (check DPA register or data processing agreements)
2. For each processor holding the subject's data:
   a. Submit a DSAR to the processor under the controller-processor agreement
   b. Set internal deadline: processor response by [buffer date before Step 12]
   c. Log: Processor name, date DSAR sent, response deadline, response received date
3. Aggregate processor responses into the master discovery register
4. Note gaps: if a processor fails to respond in time, document and consider whether to extend the overall deadline

---

### Step 6: Exemption and Redaction Analysis

For each item in the discovery register, assess whether any exemption applies and
determine the appropriate redaction approach.

**This is the most legally consequential step. Apply three-pass self-interrogation
to every claimed exemption (see Quality Frameworks section).**

#### Major DSAR Exemptions

##### 6a. Manifestly Unfounded or Excessive

**[JURISDICTION-SPECIFIC]** — EU GDPR Art. 12(5); UK GDPR equivalent

- **Manifestly unfounded**: Requester has no genuine intent to exercise rights (bad faith,
  harassment, or purely disruptive purpose). The bar is very high — "manifestly" requires
  clear and obvious unfoundedness. Disagreement with a prior response is not unfoundedness.
- **Manifestly excessive**: Clearly unreasonable in scope or frequency, especially repetitive
  requests without new basis. CCPA/CPRA allows refusal of more than 2 right-to-know requests
  per 12-month period.
- **Effect**: Controller may (a) charge a reasonable fee or (b) refuse to act. Must notify
  requester of grounds within the original deadline.
- **Documentation**: Document specific reasons with evidence. Retain for 3 years minimum.
- **Confidence threshold**: Only refuse at Definite (0.95+) confidence. If uncertain → process.

##### 6b. Third-Party Personal Data

**[JURISDICTION-SPECIFIC]** — GDPR Art. 15(4), Recital 63; DPA 2018 Sch. 2 Paras. 16-17

- Data that would identify or relate to a person other than the data subject must be
  considered separately.
- **Three options** (in order of preference):
  1. **Redact third-party identifiers** while preserving the substance of the data subject's record
  2. **Anonymize or aggregate** to provide information without identifying the third party
  3. **Withhold entirely** only if the above options are not feasible without distorting the record
- **Balancing test**: Third-party privacy vs. data subject's right of access — neither automatically
  overrides the other. Consider: sensitivity of third-party data, consent obtained, reasonable
  expectation of the third party.
- **Proportionality check**: Is full withholding necessary, or can the data subject receive
  meaningful information with partial redaction?

##### 6c. Legal Professional Privilege / Attorney-Client Privilege

**[JURISDICTION-SPECIFIC]** — DPA 2018 Sch. 2 Para. 19 (UK); varies by jurisdiction

- Communications with qualified legal counsel for the purpose of obtaining legal advice
  are typically exempt.
- **Scope**: Covers advice letters, strategy memos, and work-product in anticipation of
  litigation. Does NOT cover business advice incidentally sent to or received from a lawyer.
- **Internal legal memos**: Privilege applicability varies by jurisdiction — [VERIFY] before
  applying this exemption to internal communications.
- **Waiver risk**: Disclosing privileged material in error constitutes a waiver in many
  jurisdictions. Escalate all privilege decisions to qualified counsel.
- **Confidence threshold**: Privilege is highly jurisdiction-specific — mark < 0.85 as requiring
  counsel escalation.

##### 6d. Trade Secrets and Confidential Commercial Information

**[JURISDICTION-SPECIFIC]** — GDPR Recital 63; CCPA § 1798.185(a)(7); UK GDPR equivalent

- Information constituting trade secrets or confidential commercial information that the
  organization has taken steps to protect may be withheld.
- **Applies when**: Disclosure would reveal algorithms, pricing formulas, source code, or
  proprietary business methods alongside or inseparable from personal data.
- **Does not apply when**: The "secret" is merely commercially sensitive but not protected
  under applicable trade-secret law.
- **Proportionality**: Redact the trade-secret portion while disclosing the personal data
  portion where separable.
- **[VERIFY]**: Apply applicable trade-secret law for the jurisdiction (EU Trade Secrets
  Directive 2016/943, Defend Trade Secrets Act (US), etc.).

##### 6e. Ongoing Investigations and Legal Proceedings

**[JURISDICTION-SPECIFIC]** — GDPR Art. 23(1)(f); DPA 2018 Sch. 2 Para. 7; CCPA exceptions

- Disclosure may be restricted when it would prejudice ongoing criminal, civil, or regulatory
  proceedings, or an internal investigation.
- **Scope**: Must be a genuine, ongoing investigation (not a speculative future investigation).
- **Duration**: Exemption applies only for the duration of the investigation. Reassess at
  each request.
- **Notify**: Inform requester that data is being withheld under this exemption without
  disclosing the existence or details of the investigation (if notification itself prejudices it).

##### 6f. National Security, Defence, and Law Enforcement

**[JURISDICTION-SPECIFIC]** — GDPR Art. 23(1)(a-b); DPA 2018 Parts 3-4; PIPEDA s. 8(2)

- Data processed for national security, law enforcement, or intelligence purposes may be
  exempt from subject access in many regimes.
- **Highly jurisdiction-specific**: Apply the specific national security carve-out in the
  applicable regime only.
- **[VERIFY]**: This exemption is highly contested and frequently litigated. Escalate to
  qualified counsel and follow organizational security review procedures.

##### 6g. Research, Archiving, and Statistical Purposes

**[JURISDICTION-SPECIFIC]** — GDPR Art. 89(2); DPA 2018 Sch. 2 Para. 27-28

- Data processed solely for scientific/historical research or statistical purposes may be
  exempt where disclosure would seriously impair the purpose.
- Applies only when appropriate safeguards are in place (pseudonymization, etc.).

#### Exemption Analysis Register

For each exemption claimed, complete this register entry:

```
| Record ID(s) | Exemption Claimed | Statute/Provision | Applicability Assessment | Confidence | Self-Interrogation | Redaction Approach | Owner Escalation? |
|--------------|------------------|-------------------|--------------------------|---------|--------------------|-------------------|------------------|
| REC-xxx | Third-Party Privacy | GDPR Art. 15(4) | Third-party names in CC lines | 0.92 | PASS | Redact names; preserve context | NO |
| REC-xxx | Legal Privilege | DPA 2018 Sch.2 P.19 | Internal memo w/ external counsel | 0.72 | REVISED | Withhold pending counsel review | YES |
```

---

### Step 7: Response Format and Delivery Method

Determine the format and delivery channel for the response data package.

**Format requirements by regime:**

[JURISDICTION-SPECIFIC]
- **EU GDPR Art. 15(3)**: Provide a copy of the personal data in a "commonly used electronic
  format" where the request is made electronically. For portal/email requests, electronic
  format is default.
- **UK GDPR**: Same as EU GDPR.
- **CCPA/CPRA**: "In a portable and, to the extent technically feasible, readily usable format."
- **LGPD Art. 19**: Must provide in a "portable, interoperable format."
- **PIPEDA**: In a form understandable to the individual; machine-readable preferred.

**Format selection:**

| Data Type | Recommended Format | Notes |
|-----------|-------------------|-------|
| Structured records (contact, transaction) | CSV or JSON | Machine-readable, portable |
| Unstructured (emails, documents) | PDF | Human-readable; apply redactions before converting |
| Mixed | Zip package with CSV + PDF | Include manifest/index file |
| Special category | Encrypted download with one-time link | Extra security layer |

**Delivery channel selection:**

| Preference | Channel | Security Requirement |
|------------|---------|---------------------|
| Electronic (default) | Secure download link (time-limited) or encrypted email | Do not send plaintext personal data via unencrypted email |
| Postal | Certified/tracked mail to verified address | Confirm address matches verified identity |
| In-person | In-person collection with ID check | Maintain attendance log |

---

### Step 8: Redaction Execution and Package Assembly

Apply the redaction decisions from Step 6 and assemble the final data package.

**Redaction standards:**
- Use **permanent redaction** (not visual masking) — cover-text redactions that can be
  lifted have caused regulator enforcement actions
- Apply redactions before format conversion (redact source, then export to PDF/CSV)
- Redact minimum necessary — do not over-redact beyond what the exemption requires
- Generate **redaction index**: for each redaction, note Record ID, what was redacted, and
  exemption invoked

**Post-redaction validation checklist:**
- [ ] All redacted areas are permanently removed (not masked with a coloured bar over selectable text)
- [ ] Redacted records are still coherent and useful to the data subject
- [ ] No third-party identifiers remain visible (check PDF metadata as well as visible content)
- [ ] Machine-readable formats (CSV/JSON) have fields deleted, not set to null/empty
- [ ] Images, scanned documents, or video frames with embedded text have been reviewed
- [ ] Zip archive index correctly lists all included and withheld items

**Package assembly checklist:**
- [ ] Cover notice attached (see Step 9)
- [ ] Data files correctly named and organized
- [ ] Index/manifest included listing all data categories and file counts
- [ ] Secure delivery method prepared (encrypted link, secure email)
- [ ] Confirmation of receipt mechanism ready

---

### Step 9: Notice Drafting

Draft the cover notice that accompanies the data package.

**Required notice elements [JURISDICTION-SPECIFIC]:**

| Element | GDPR/UK GDPR | CCPA/CPRA | LGPD | PIPEDA |
|---------|-------------|-----------|------|--------|
| Identity confirmation | ✓ | ✓ | ✓ | ✓ |
| Scope description | ✓ | ✓ | ✓ | ✓ |
| Categories disclosed | ✓ | ✓ | ✓ | ✓ |
| Exemptions/withholdings with basis | ✓ | ✓ | ✓ | ✓ |
| Processing purposes | ✓ | ✓ | ✓ | Principle 4 |
| Data sources | ✓ (Art. 15(1)(g)) | ✓ | ✓ | Principle 4 |
| Retention period or criteria | ✓ (Art. 15(1)(d)) | — | ✓ | Principle 5 |
| Recipient categories | ✓ (Art. 15(1)(c)) | ✓ | ✓ | — |
| Automated decision-making info | ✓ (Art. 15(1)(h)) | — | Art. 20 | — |
| Third-country transfer info | ✓ (Art. 15(2)) | — | Art. 33 | Principle 1 |
| Right to lodge complaint | ✓ | ✓ (CPPA) | ✓ (ANPD) | ✓ (OPC) |
| Appeal/correction rights | ✓ | ✓ | ✓ | ✓ |
| Contact details | ✓ | ✓ | ✓ | ✓ |

**Notice template — fill all [PLACEHOLDER] values:**

```
[Organization Name]
[Organization Address]
Data Protection Officer / Privacy Team: [DPO email]

[Date]

Re: Response to Your Data Subject Access Request (Request ID: [DSAR-YYYY-MM-NNN])

Dear [Requester Name],

We are writing in response to your data subject access request received on [Date]. We have
verified your identity and your authority to make this request. [If third party: We have
verified your authority to act on behalf of [Data Subject Name] pursuant to [authority basis].]

Applicable Legal Regime: [Regime Name and Statute]
Response Deadline: [Date]
This Response Date: [Date]

---

SECTION 1: DATA PROVIDED

We have located the following categories of personal data about [you / Data Subject Name] and
are providing them with this letter:

- [Category 1]: [Description, e.g., "Contact information (name, email, phone, mailing address)
  — [N] records"]
- [Category 2]: [Description]
- [Continue per category]

A copy of these records is enclosed in the attached [format description].

---

SECTION 2: DATA WITHHELD

We have withheld the following data on the grounds specified:

- [Description of withheld data]: Withheld under [exemption name and statute section].
  [Brief explanation of why exemption applies.]
- [Continue per exemption]

---

SECTION 3: PROCESSING INFORMATION

Purpose(s) of processing: [List purposes]
Legal basis/bases: [Consent / Contract / Legal obligation / Legitimate interests / etc.]
Data sources: [Where we obtained your personal data]
Retention: [Retention period or criteria for determining it]
Recipients / recipient categories: [Who we share your data with]
[If international transfers:] International transfers: [Safeguards used — SCCs, adequacy decision, BCRs, etc.]
[If automated decisions:] Automated decision-making: [Description, logic, significance, and your right to challenge]

---

SECTION 4: YOUR RIGHTS

You have the following rights regarding your personal data:
- Right to rectification (correct inaccurate data)
- Right to erasure (in certain circumstances)
- Right to restriction of processing
- Right to object to processing
- Right to data portability [where applicable]
- Right to withdraw consent (where processing is based on consent)

[JURISDICTION-SPECIFIC: Add regime-specific rights and describe how to exercise them]

---

SECTION 5: HOW TO COMPLAIN

If you are dissatisfied with our response, you have the right to:
[JURISDICTION-SPECIFIC — fill in applicable regulator and procedure:]
- Lodge a complaint with [Supervisory Authority / CPPA / ANPD / OPC / other] at [URL/address]
- Seek judicial remedy in [applicable court]

For further questions or to exercise additional rights, please contact:
[DPO Name], [DPO email], [DPO phone / address]

Yours sincerely,
[Name]
[Title]
[Organization]
```

---

### Step 10: Quality Assurance and Audit Trail

Before dispatching the response, run all quality checks and complete the Glass Box audit trail.

#### Citation Quality Gates

Run these five gates silently before delivering the final response. If any gate fails, revise.

| Gate | Rule for DSAR | Fail Action |
|------|---------------|-------------|
| **Source** | Every deadline, exemption, or right-description cites a specific statute, regulation, or regulator guidance | Add statutory citation or mark "[UNVERIFIED — legal team to confirm]" |
| **Format** | All citations use consistent format: [Regime Statute §Section] or [Regulator Guidance — URL] | Standardize format across notice and exemption register |
| **Currency** | Every deadline, exemption, and regulator guidance reference checked for recent amendments or updated guidance (within past 24 months) | Flag "[CHECK CURRENCY — deadline or exemption may have changed — verify at [regulator URL]]" |
| **Domain** | Analysis uses only the regime(s) applicable to this request. No concepts from GDPR bleeding into a CCPA-only request. | Remove or flag cross-regime contamination |
| **Confidence** | Uncertainty about exemption applicability, deadline, or scope is explicitly stated, not hidden. Present both positions when uncertain. | Add confidence qualifier; surface for legal sign-off |

#### Self-Interrogation for HIGH-STAKES Decisions

For any exemption claimed, or any decision not to disclose data, apply this three-pass
review before the response is dispatched:

**Pass 1 — Legal Basis Integrity:**
- Is the exemption actually named in the applicable statute or binding regulator guidance?
- Does the factual basis for claiming the exemption match the statutory language?
- Would the applicable data protection regulator's recent enforcement guidance support this application?
- What is the strongest counter-argument the data subject or their counsel would make?

**Pass 2 — Completeness:**
- Have all potentially applicable exemptions been considered, not just the most convenient?
- Are there partial alternatives (redact rather than withhold; anonymize rather than redact)?
- Have recent enforcement actions against similar exemption claims been reviewed?
- Is there a duty to disclose under another legal regime that overrides this exemption?

**Pass 3 — Proportionality:**
- Is the exemption claim narrowly tailored, or are we over-withholding?
- Would a proportionality-minded regulator agree that full withholding (vs. partial redaction)
  is justified?
- Under what circumstances might a reasonable DPO accept this risk without escalating?
- If challenged by the regulator, could we defend this decision with documented evidence?

Mark audit trail: `self_interrogation: [EXEMPTION_NAME]: PASS` or `REVISED — [reason]`.

#### Confidence Scoring for DSAR Decisions

| Level | Range | Meaning | DSAR Action |
|-------|-------|---------|-------------|
| **Definite** | 0.95–1.0 | Settled law, clear regulator guidance, no ambiguity | Record decision; apply without caveat |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | Apply with brief caveat; note in Glass Box |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ; guidance mixed | Surface for DPO review before dispatch |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing regulator interpretations | Escalate to legal counsel; present both positions |
| **Unlikely** | 0.0–0.39 | Weak basis; speculative | Do not claim exemption; disclose data; flag "[UNCERTAIN — do not withhold without legal sign-off]" |

#### Glass Box Audit Trail

Append this YAML block to every completed DSAR response:

```yaml
dsar_glass_box:
  # Request Metadata
  request_id: "[DSAR-YYYY-MM-NNN]"
  request_date: "[ISO 8601 date received]"
  legal_clock_start: "[ISO 8601 date of awareness]"
  response_date: "[ISO 8601 date dispatched]"
  deadline: "[ISO 8601 response deadline]"
  deadline_met: true  # or false — document reason if false
  extension_triggered: false  # if true, document reason and notice date
  request_channel: "[Email / Web Form / Postal / Phone / In-Person]"

  # Subject Verification
  subject:
    name: "[Data subject name]"
    relationship: "[Self / Agent / Attorney / Guardian / Executor]"
    identity_verification_method: "[Methods used]"
    identity_confidence: 0.93
    authority_verified: "[YES / NO / NOT APPLICABLE]"
    authority_basis: "[Power of attorney / Guardianship order / etc.]"

  # Jurisdiction
  regime_primary: "[GDPR / UK GDPR / CCPA-CPRA / LGPD / PIPEDA]"
  regimes_assessed: "[All regimes checked and applicability determination for each]"
  deadline_source: "[Statute §Section — VERIFIED / UNVERIFIED]"
  legalcode_mcp: "Connected / Not connected"

  # Scope
  request_scope_as_interpreted: "[All personal data / Specific categories]"
  scope_confidence: 0.90

  # Systems Searched
  systems_in_scope:
    - system: "[System 1]"
      searched: true
      records_found: 0
      responsive: 0
      notes: "[Any search limitations]"
    - system: "[System 2]"
      searched: true
      records_found: 0
      responsive: 0
      notes: ""
  systems_not_searched:
    - system: "[System X]"
      reason: "[Not in scope / Technical barrier / Disproportionate effort]"
  vendor_coordination:
    - vendor: "[Vendor name]"
      dsar_sent_date: "[date]"
      response_received: true
      notes: ""

  # Responsive Data
  total_responsive_records: 0
  data_categories_disclosed:
    - category: "[Category]"
      records: 0

  # Exemptions
  exemptions_applied:
    - exemption_name: "[Name]"
      statute_section: "[Citation]"
      records_withheld: 0
      self_interrogation: "PASS"  # or "REVISED — [reason]"
      confidence: 0.90
      regulator_guidance_consulted: "[URL or legalcode-mcp ref]"
      escalated_to_counsel: false

  # Redactions
  redactions_summary: "[Brief description of what was redacted and why]"
  redaction_permanent: true  # false = risk of recoverable masking

  # Delivery
  delivery_format: "[CSV / PDF / ZIP / Other]"
  delivery_channel: "[Secure download / Encrypted email / Postal]"
  dispatch_confirmed: false  # to be set true at Step 12

  # QA
  citation_gates_passed: true  # all 5 gates: source, format, currency, domain, confidence
  self_interrogation_summary: "[PASS / REVISED — details]"
  confidence_distribution:
    definite: 0   # count of decisions at 0.95–1.0
    high: 0       # 0.80–0.94
    probable: 0   # 0.60–0.79
    possible: 0   # 0.40–0.59
    unlikely: 0   # 0.0–0.39

  # Sign-off
  escalated_to_counsel: false
  escalation_reason: ""
  sign_off_required_by: "[DPO / General Counsel / Both]"
  sign_off_obtained: false
  sign_off_date: ""

  # Meta
  limitations:
    - "[Any scope limitations, data discovery gaps, or unresolved uncertainties]"
  reviewer: "AI-assisted DSAR analyst — requires DPO/legal review before dispatch"
```

---

### Step 11: Legal Review and Sign-off Gate

Escalate to the Data Protection Officer (DPO) or qualified counsel before dispatch.

**Mandatory escalation triggers:**
- Any exemption with confidence < 0.80
- Any exemption self-interrogation marked `REVISED`
- Any decision to refuse to act (manifestly unfounded/excessive)
- Any request from a regulator, journalist, or law enforcement officer
- Any request where the subject appears to be in active litigation with the organization
- Any request involving special category data (health, biometric, criminal, etc.)
- Any request where the deadline extension has been triggered

**Sign-off record:**
```
Reviewed by: [DPO / Counsel name]
Date reviewed: [Date]
Decision: APPROVED FOR DISPATCH / REVISED — [revision instructions]
Exemption decisions confirmed: [List]
Exemptions revised: [List changes]
Sign-off signature: [Electronic or wet ink per organizational policy]
```

---

### Step 12: Final Dispatch and Documentation

Execute the final delivery and lock the compliance record.

**Dispatch checklist:**
- [ ] Cover notice finalized and approved
- [ ] Data package assembled with correct contents
- [ ] Redactions verified as permanent (not recoverable masking)
- [ ] Delivery method confirmed as secure
- [ ] Delivery address or email matches verified identity
- [ ] Dispatch timestamp logged (critical for statutory deadline proof)
- [ ] Delivery confirmation mechanism active (read receipt, tracking number, portal confirmation)

**Post-dispatch documentation:**
- Lock the DSAR file (no modifications without documented change log)
- Save: canonical request, verification record, discovery register, exemption register,
  redaction index, notice, Glass Box audit trail, sign-off record, dispatch log
- Set reminder for: [30 / 60 / 90]-day follow-up window for appeals or supplemental requests
- Update DSAR register / data processing records with: request ID, date, regime, outcome, exemptions applied

**Retention of DSAR records:** [JURISDICTION-SPECIFIC]
- EU GDPR: ICO recommends 3 years minimum
- UK GDPR: Organizational policy, minimum 1 year (ICO enforcement standard)
- CCPA/CPRA: CPPA regulations require 24 months minimum
- LGPD: Not explicitly specified; 5 years recommended for documentation
- PIPEDA: OPC recommends reasonable retention to defend against complaints

---

### Step 13 (Optional): Post-Dispatch Monitoring and Appeal Handling

**Appeal and challenge triggers:**
- Data subject disputes the completeness of the response
- Data subject challenges a withheld record or exemption claim
- Regulator opens investigation based on complaint
- Data subject submits a supplemental request (additional data not covered by original scope)

**Supplemental vs. Re-request distinction:**
- **Supplemental**: Builds on original request; requests data discovered post-dispatch or
  corrects a recognized gap. Treat as continuation; clock restarts on the supplemental scope.
- **Re-request**: Identical scope to a prior request within the statutory frequency limit.
  May be refused under manifestly excessive rules (CCPA/CPRA: 2 per 12 months; GDPR: repeat
  request without change in circumstances).

**Appeal response procedure:**
1. Review the specific challenge raised
2. Re-apply exemption analysis to the challenged item (re-run three-pass self-interrogation)
3. If exemption is upheld: provide a more detailed written explanation of the basis
4. If exemption is revised: supplement the response with the additional data
5. Document all appeal proceedings in the DSAR file

**Regulator investigation procedure:**
1. Appoint internal investigation lead
2. Preserve all DSAR records (litigation hold)
3. Engage qualified counsel immediately
4. Respond to regulator requests within statutory timeframes
5. Document all regulator communications

---

## Exemption Decision Framework Summary

Apply this quick-reference matrix to each potentially exempt item before claiming exemption:

| Exemption | Confidence Threshold to Apply | Proportionality Requirement | Escalation Required |
|-----------|------------------------------|----------------------------|---------------------|
| Manifestly Unfounded/Excessive | 0.95+ | N/A (full refusal permitted) | DPO sign-off always |
| Third-Party Privacy | 0.80+ | Redact minimum; prefer partial disclosure | If borderline |
| Legal Privilege | 0.85+ | Privilege must attach to specific document | Counsel always |
| Trade Secrets | 0.80+ | Redact trade secret portion; disclose personal data | If borderline |
| Ongoing Investigation | 0.85+ | Must be genuine ongoing proceeding | DPO always |
| National Security | 0.95+ | Strict statutory compliance required | DPO + Counsel always |
| Research / Archiving | 0.80+ | Safeguards must be in place | DPO sign-off |

---

## Prioritization and Triage Framework

When managing multiple open DSARs, prioritize using this four-tier framework:

| Tier | Trigger | Action |
|------|---------|--------|
| **Critical** | Less than 5 business days to statutory deadline; or regulator investigation active; or special category data + vulnerable individual | Immediate — all available resources; escalate to DPO and counsel same day |
| **High** | 6–15 business days to deadline; or complex exemption decisions pending; or third-party processor delays | Priority assignment; daily status check; DPO check-in within 48 hours |
| **Standard** | 16–30 business days to deadline; normal scope and exemption profile | Normal workflow; weekly status check |
| **Low** | More than 30 business days to deadline; or clear de minimis data held; or clear single-system scope | Background processing; no rush, but do not allow deadlines to creep |

---

## Multi-Stakeholder Map

DSAR responses require coordination across multiple internal stakeholders:

| Stakeholder | Role | Involvement |
|-------------|------|-------------|
| Privacy Team | Process owner; coordinates discovery, exemptions, notice | All steps |
| IT / Engineering | Executes data discovery in technical systems | Steps 5, 8 |
| Legal / DPO | Reviews exemption decisions; signs off on response | Steps 6, 10, 11 |
| HR | Searches HR systems for employee data | Step 5 (if employee DSAR) |
| Finance / Revenue | Searches billing and transaction records | Step 5 |
| Customer Support | Searches CRM and ticketing | Step 5 |
| Vendor Management | Coordinates with third-party processors | Step 5b |
| Security | Verifies secure delivery channel; approves redaction tools | Steps 7–8, 12 |
| Communications | Reviews any externally visible statements (appeals, regulator) | Step 13 |

---

## Anti-Patterns

What NOT to do when handling DSARs:

1. **Starting discovery without verified identity** — Disclosing to the wrong person is
   itself a personal data breach. Always complete identity verification (Step 2) before
   executing any data discovery. Identity confirmation is not optional.

2. **Treating the statutory deadline as the target** — The deadline is the backstop, not
   the target. Missed deadlines are the most common enforcement trigger globally. Build a
   3-5 day buffer. Set internal deadlines earlier.

3. **Searching only primary systems** — DSARs require a comprehensive search. Failing to
   check email archives, collaboration tools, marketing platforms, and legacy systems
   produces incomplete responses that regulators will flag as non-compliant.

4. **Applying exemptions without three-pass self-interrogation** — Exemption claims that
   fail under legal challenge are worse than no exemption (they suggest bad faith).
   Every exemption must survive: legal basis, completeness, and proportionality review.

5. **Using visual masking instead of permanent redaction** — Cover-text and highlighting-bar
   redactions are regularly reversed in post-disclosure PDF processing. The ICO has issued
   enforcement notices specifically for this failure mode. Use tools that permanently remove
   or overwrite the underlying text.

6. **Over-withholding under third-party exemption** — The third-party exemption does not
   license wholesale withholding of all records containing any third-party reference.
   Redact the third-party identifier (name, email) while preserving the subject's data.
   Courts and regulators consistently reject over-broad third-party claims.

7. **Conflating business sensitivity with trade-secret protection** — Commercially sensitive
   information is not automatically a trade secret. Trade-secret protection requires: the
   information has commercial value, is not publicly known, and reasonable steps have been
   taken to protect it. Internal sales targets or pricing strategies without these elements
   are not protected.

8. **Calculating deadlines without checking for extension eligibility** — Automatically
   triggering extensions is improper. Extensions are only justified where the request is
   genuinely complex or multiple requests are received simultaneously. Assess extension
   eligibility explicitly and document the justification.

9. **Failing to notify the requester of an extension** — Triggering an extension without
   notifying the requester within the original deadline is a compliance failure in all
   five regimes covered by this skill. Set a calendar trigger for extension notification.

10. **Disclosing data before sign-off on exemption decisions** — Under pressure of deadline,
    teams sometimes dispatch before legal review of borderline exemptions. This is
    particularly risky for legal privilege: once privilege is waived by disclosure, it
    cannot be reclaimed. Always obtain sign-off before dispatch.

11. **Assuming the response is complete without a system-completeness check** — Data is
    held in unexpected places (collaboration threads, archived emails, legacy databases,
    vendor systems). Always complete the system inventory before declaring discovery
    complete, and document systems checked and not checked.

12. **Treating email requests as lower priority than portal requests** — The statutory
    clock starts when the request is received, regardless of channel. An email DSAR
    received on a Friday at 5pm starts the clock on that Friday. Route all intake channels
    through a monitored privacy inbox or triage system.

13. **Using the same response template across jurisdictions without localization** — GDPR
    response notices have different required elements from CCPA notices, which differ from
    LGPD notices. A single template applied globally produces notices that are legally
    non-compliant in most of the regimes it purports to address.

14. **Failing to retain the DSAR file for the minimum statutory or recommended period** —
    Regulators routinely ask to see DSAR records during investigations. Files deleted before
    the retention period expires (or without a retention policy at all) create indefensibility
    gaps that compound enforcement risk.

15. **Disclosing auto-generated or derived data as if it were factual** — Algorithmic
    scoring, behavioral predictions, or inferred attributes must be disclosed under GDPR
    Art. 15(1)(h) (automated decision-making). Failing to disclose inferred data while
    disclosing input data produces an incomplete response.

16. **Processing supplemental requests as fresh DSARs instead of continuations** —
    Supplemental requests for data missed in an original response should be processed as
    continuations (with a new deadline from the supplemental request date), not as new
    DSARs that reset the frequency count. Treating them as new DSARs misapplies the
    "manifestly excessive" rule and may prejudice the data subject.

---

## Writing Standards

**For cover notices (externally visible):**
- Plain language: a non-lawyer should understand every sentence
- Active voice: "We hold the following data about you" not "Data about you is held by us"
- Specific, not vague: cite the statute section when invoking an exemption
- Short sentences: one point per sentence
- No jargon without explanation: if "legitimate interests" appears, define it briefly
- Name your contact person, not just a generic inbox

**For internal documentation (DSAR file, exemption register):**
- Same plain-language standard, with more technical detail permitted
- Confidence qualifiers where appropriate: "We believe this data is responsive because…"
- Every legal claim followed by citation or [VERIFY]
- Glass Box audit trail appended to every response file

**Quality gates before dispatch:**
1. Can the data subject understand the cover notice without legal assistance?
2. Is every exemption basis cited with a specific statute section?
3. Is every data category described in plain language?
4. Is every [VERIFY] item resolved or escalated?
5. Could any sentence in the notice be shorter or clearer?
6. Has the notice been checked against the jurisdiction-specific required elements table (Step 9)?

---

## External Tool Integration

### With legalcode-mcp (preferred):

Use legalcode-mcp to verify:
- Current statutory deadline for each applicable regime (verify statute has not been amended)
- Regulator guidance on exemption interpretation (check for recent guidance publications)
- Enforcement actions involving similar fact patterns (validate exemption claims against
  enforcement precedent)
- Recent legislative changes affecting DSAR obligations (new state privacy laws, LGPD
  amendments, PIPEDA reform bills)
- International transfer adequacy decisions affecting disclosure obligations

Save research to `/tmp/dsar-[request_id]-research.md` structured as:
```markdown
# DSAR Legal Research — [Regime]
## Date: [date]
### Deadlines Verified: [Cite statute and regulator guidance]
### Exemptions Verified: [Cite for each exemption being applied]
### Enforcement References: [Relevant enforcement actions]
### Recent Developments: [Any changes in last 24 months]
```

### Without legalcode-mcp:

- Proceed with web research and organizational documentation only
- Mark all statutory and deadline references with **[VERIFY]** before dispatching
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus quality effort on proportionality review and three-pass self-interrogation
  (these do not depend on external legal databases)
- Escalate all borderline exemption decisions to qualified counsel regardless of confidence score

---

## Localization Notes

When applying this skill to a specific jurisdiction, localize:

**EU GDPR:**
- Identify the competent Supervisory Authority (varies by Member State, lead authority for
  cross-border processing)
- Check for Member State derogations under Art. 23 (national security, criminal law, etc.)
- Apply EDPB Guidelines 01/2022 on the right of access

**UK GDPR / DPA 2018:**
- Apply DPA 2018 Schedule 2 exemption list in full
- Check ICO guidance publications for current enforcement standards
- Note: UK GDPR diverged from EU GDPR post-Brexit — do not assume full parity

**CCPA/CPRA (California):**
- Confirm the business meets the applicability threshold (>$25M revenue, OR >100K consumers'
  data per year, OR derives >50% revenue from selling personal information)
- Distinguish Right to Know — Categories vs. Right to Know — Specific Pieces requests
- Apply CPPA regulations effective 2023 and any subsequent rulemaking
- Note: multiple US state privacy laws now exist (Virginia VCDPA, Colorado CPA, Texas TDPSA,
  etc.) — check which states apply

**LGPD (Brazil):**
- Note that ANPD enforcement has been increasing since 2022
- Check ANPD's current guidance on data subject rights procedures
- LGPD's 15-day deadline is very short by global standards — plan discovery to complete
  within 10 calendar days to maintain buffer

**PIPEDA (Canada):**
- Check whether provincial law applies (PIPA Alberta, PIPA British Columbia, LPRPSP Quebec)
  — these may have stricter requirements than PIPEDA
- Note: Bill C-27 (Consumer Privacy Protection Act / CPPA) was tabled and, if enacted,
  will replace PIPEDA — [CHECK CURRENCY] for current legislative status

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis drawing on:
- GDPR Article 15 and EDPB Guidelines 01/2022 on the right of access
- UK GDPR Article 15 and ICO Subject Access guidance
- CCPA California Civil Code § 1798.100–1798.199.100 and CPPA regulations
- LGPD Articles 18–19 (Brazilian LGPD)
- PIPEDA Principle 9 and OPC guidance on access requests
- Industry best practices from DPO consulting, privacy management platforms, and enforcement
  precedent analysis
- Legalcode reference standards: `legalcode-contract-review` (quality frameworks and audit
  trail patterns), `legalcode-dpia-generator` (compliance workflow structure), and
  `legalcode-breach-severity-assessment` (jurisdiction matrix and multi-regime handling)
- Agent team analysis (structural and prompt engineering) conducted 2026-03-01

---

*This skill is part of the Legalcode compliance skill suite. Related skills:*
- *`legalcode-dpia-generator` — Data Protection Impact Assessments*
- *`legalcode-privacy-policy-drafter` — Privacy policy drafting*
- *`legalcode-breach-severity-assessment` — Data breach notification obligations*
