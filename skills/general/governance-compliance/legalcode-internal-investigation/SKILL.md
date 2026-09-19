---
name: legalcode-internal-investigation
description: Guide corporate internal investigations from initial allegation through remediation. Use
  when receiving an internal allegation or whistleblower complaint, responding to a regulatory inquiry,
  conducting pre-acquisition due diligence on compliance matters, or building investigation capacity.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Guide corporate internal investigations from initial allegation through remediation. Covers: investigation scoping and mandate design; legal hold implementation and litigation-hold notice drafting; investigator selection and independence analysis (in-house vs. outside counsel, conflict screening); attorney-client privilege protection (Upjohn Co. v. United States, 449 U.S. 383 (1981)); work product doctrine preservation and selective waiver risk under FRE 502; interview planning and execution (Upjohn warning scripts, witness sequencing, 5th Amendment considerations, Garrity warnings for public employees); electronically stored information (ESI) collection and chain-of-custody protocols; forensic imaging standards; document review and privilege logging; evidence preservation and spoliation avoidance under FRCP Rule 37(e); witness credibility assessment frameworks; findings documentation and evidence-to-allegation mapping; voluntary self-disclosure decisions (DOJ CEP presumption of declination, SFO DPA pathway); cooperation credit strategy (DOJ Monaco Memo, Filip Factors, Nov 2024 CEP update); parallel government investigation management (grand jury, SEC CID, CWA/CFPB subpoenas, DOJ/SEC coordination); DOJ Clawbacks Pilot Program (2023) and SEC Rule 10D-1; whistleblower protection obligations (SOX 18 U.S.C. §1514A, Dodd-Frank 15 U.S.C. §78u-6, anti-retaliation); GDPR and data-protection constraints on employee monitoring and data collection (EU, UK, Germany Betriebsverfassungsgesetz); and comprehensive remediation frameworks including disciplinary actions, compliance program enhancements, and monitorship evaluation. Produces: SUBSTANTIATED / PARTIALLY SUBSTANTIATED / UNSUBSTANTIATED / INCONCLUSIVE findings classifications; evidence matrices; interview memoranda templates; remediation action plans; board-ready investigation reports; and Glass Box audit trails. Aligned with DOJ Criminal Division Corporate Enforcement Policy (as amended November 2024), DOJ Evaluation of Corporate Compliance Programs (updated September 2024), UK SFO Corporate Guidance (2025 update), FCA Investigation Guide, and EU regulatory enforcement expectations. Use when receiving an internal allegation or whistleblower complaint, responding to a regulatory inquiry, conducting pre-acquisition due diligence on compliance matters, or building investigation capacity. Jurisdiction-agnostic core with US/UK/EU [JURISDICTION-SPECIFIC] markers.


# Legalcode Corporate Internal Investigation Manager

> **Disclaimer**: This skill provides a framework for AI-assisted corporate internal
> investigation planning and management. It does not constitute legal advice and does
> not create an attorney-client relationship. All outputs must be reviewed by qualified
> legal counsel — and, for regulated entities, by appropriately licensed professionals —
> before being relied upon in an actual investigation or regulatory engagement. Laws,
> regulations, and enforcement policies change; verify current applicability before
> relying on any provision described here. Statutory, regulatory, and case law references
> cited from training-data knowledge carry hallucination risk — verify against
> authoritative sources (DOJ Justice Manual, SFO Corporate Guidance, EUR-Lex, FCA
> Handbook, court records) before relying on them in live matters. Privilege analysis
> in particular is highly jurisdiction- and fact-specific; consult qualified privilege
> counsel before sharing investigation materials with any third party.

---

## Purpose and Scope

This skill guides the complete lifecycle of a corporate internal investigation, from
initial allegation intake through remediation recommendations. It operates across three
modes:

- **Plan**: Design an investigation structure, mandate, and work plan in response to
  a new allegation or regulatory trigger
- **Execute**: Manage an ongoing investigation — legal hold, document collection,
  interview scheduling, evidence analysis, and findings development
- **Report**: Draft investigation findings, remediation recommendations, and board
  or audit committee reports

**Covers:**

- Allegation intake triage and investigation scoping
- Investigator independence analysis and team structure
- Legal hold design and distribution
- Privilege framework (attorney-client privilege, work product doctrine, Upjohn warnings)
- ESI collection protocols and chain-of-custody standards
- Witness sequencing, interview planning, and execution
- Evidence analysis and allegation-to-finding mapping
- Voluntary self-disclosure (VSD) decisions and cooperation credit strategy
- Parallel government investigation management
- Whistleblower protection obligations during investigations
- Remediation frameworks (disciplinary, compliance, clawback, monitorship)
- Board and audit committee reporting

**Does not:**

- Provide legal advice or replace qualified counsel in an actual investigation
- Conduct the investigation autonomously — it guides the human investigator
- Access case management systems, email servers, or document repositories directly
- Provide real-time legal research (verify all cited authority independently)
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-compliance-program-builder` — for building the underlying compliance program
- `legalcode-breach-regulatory-notification-drafter` — if investigation uncovers a data breach
- `legalcode-dsar-workflow-builder` — if investigation involves employee data subject access requests
- `legalcode-aml-kyc-compliance` — if investigation involves AML/financial crime

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The governing law of the investigation depends on:

- The jurisdiction(s) where alleged misconduct occurred
- The jurisdiction(s) where the entity is incorporated or operates
- The regulatory authorities with jurisdiction over the subject matter

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**

- DOJ Criminal Division Corporate Enforcement Policy (CEP, as amended Nov 2024)
- FCPA Corporate Enforcement Policy (DOJ Criminal Division)
- DOJ Justice Manual (JM) §§ 9-28.000 (corporate charging), 9-47.120 (FCPA CEP)
- Filip Factors (JM 9-28.300) — factors governing corporate charging decisions
- DOJ Evaluation of Corporate Compliance Programs (Sep 2024 update)
- SEC Division of Enforcement — Cooperation Initiative (2010)
- FRCP Rule 37(e) — ESI preservation and sanctions
- FRE Rule 502 — privilege waiver limitations
- SOX Section 806 (18 U.S.C. §1514A) — whistleblower protections
- Dodd-Frank Section 922 (15 U.S.C. §78u-6) — SEC whistleblower protections
- 5th Amendment — individual privilege in interviews

**United Kingdom:**

- SFO Corporate Guidance on self-reporting, cooperation and DPAs (April 2025 update)
- Crime and Courts Act 2013, Schedule 17 — DPA regime
- Serious Organised Crime and Police Act 2005 (SOCPA) ss. 71-73 — immunity and reduction
- FCA Decision Procedure and Penalties Manual (DEPP)
- FCA Enforcement Guide (EG)
- UK GDPR / Data Protection Act 2018 — employee data collection constraints
- Employment Rights Act 1996 — employee rights during investigation
- Proceeds of Crime Act 2002 — tipping-off obligations

**European Union:**

- European Commission Competition Investigations (Arts. 101, 102 TFEU; Regulation 1/2003)
- GDPR Arts. 5-6 — legal basis for employee data processing during investigation
- GDPR Art. 88 — employment-context derogations
- National works council consultation requirements (Germany: Betriebsverfassungsgesetz
  §§ 87, 94-95; France: Code du travail Art. L.2312-8; Netherlands: Wet op de
  ondernemingsraden Art. 27)
- National whistleblower protection laws implementing EU Whistleblowing Directive
  2019/1937 (transposed by Member States by December 2021; enforcement ongoing)
- EU Whistleblowing Directive 2019/1937 — mandatory internal reporting channels for
  organizations with 50+ employees
- NIS2 incident reporting obligations (Directive 2022/2555) if investigation involves
  a cybersecurity incident

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The allegation type or scope determines which legal framework applies
- The decision to engage outside counsel vs. use in-house counsel has not been made
- Privilege protection strategy requires a decision on investigation structure
- The voluntary self-disclosure decision has not been made and timing is material
- Parallel government proceedings create conflicts that affect witness interview strategy

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

Accept input in any of the following formats:

- **Allegation description**: Text describing the alleged misconduct, how it was
  reported, who is implicated, and what evidence (if any) has been identified
- **Complaint document**: A whistleblower complaint, HR report, board referral, or
  regulatory inquiry (subpoena, CID, regulator letter)
- **Investigation request**: A board or audit committee resolution to investigate
- **Ongoing investigation status**: A description of investigation phase and what
  guidance is needed (legal hold, interview prep, privilege review, report drafting)
- **Post-investigation remediation request**: Findings already complete; need
  remediation plan and/or board report

Identify the **investigation trigger category**:

| Trigger                                | Characteristics                                                                | Typical Urgency |
| -------------------------------------- | ------------------------------------------------------------------------------ | --------------- |
| **Internal whistleblower complaint**   | SOX/Dodd-Frank implications; anti-retaliation obligations activate immediately | High            |
| **Anonymous tip or hotline report**    | Credibility assessment needed; may not trigger formal investigation yet        | Medium          |
| **Government subpoena or CID**         | Investigation may already be parallel; counsel engagement critical             | Critical        |
| **Regulatory inquiry or exam finding** | Specific regulatory framework applies; timelines may be externally imposed     | High            |
| **Board / audit committee referral**   | Governance tone at top involved; board privilege considerations                | High            |
| **M&A due diligence finding**          | Pre-closing timeline; remediation affects valuation and reps                   | Varies          |
| **Employee complaint / HR report**     | Employment law dimensions; dual-hat counsel conflict risk                      | Medium-High     |
| **Media inquiry / public disclosure**  | Reputational dimension; communications strategy needed alongside investigation | Critical        |

---

### Step 2: Gather Investigation Context

**⟁ CLARIFY — Before proceeding, ask the user (skip questions already answered):**

**1. Investigation Mode**

- Plan a new investigation from scratch
- Guide an investigation already underway (specify phase)
- Draft remediation and report for a completed investigation

_Why this matters_: Determines whether to start with scoping and mandate, or jump to
interview protocol, evidence analysis, or report drafting.

**2. Allegation Type**

- Financial fraud / accounting irregularity (earnings manipulation, revenue recognition, unauthorized transactions)
- Corruption / bribery (FCPA, UK Bribery Act, domestic bribery)
- Workplace misconduct (harassment, discrimination, hostile work environment, retaliation)
- Data security breach or unauthorized access (may trigger mandatory reporting)
- Trade secret theft or IP misappropriation
- Regulatory violation (securities, AML/BSA, environmental, healthcare, export controls)
- Employment and labor law violation
- Antitrust or competition law concern
- Conflict of interest or code of conduct violation
- Other (describe)

_Why this matters_: Allegation type determines the regulatory framework, potential
criminal exposure, whistleblower protections at stake, and mandatory reporting obligations.

**3. Entity Profile**

- Public company (SEC-reporting) — SOX Section 301 audit committee obligations apply
- Regulated entity (bank, broker-dealer, healthcare, government contractor) — regulatory
  supervisor likely has direct interest
- Private company / portfolio company of PE fund
- Non-profit / NGO
- Government agency or government-owned entity

_Why this matters_: Public company obligations (audit committee independence, Sarbanes-Oxley
reporting, SEC cooperation initiatives), regulated entity obligations (supervisor notification),
and individual employee rights all depend on entity type.

**4. Investigator Status**

- Outside counsel leading the investigation (privilege protection maximized)
- In-house counsel leading the investigation (privilege risk in some jurisdictions)
- HR or compliance function leading the investigation (limited privilege protection)
- Hybrid: outside counsel supervising in-house or HR
- Not yet determined

_Why this matters_: Determines privilege architecture. In most US circuits, investigations
led by in-house counsel directed to provide legal advice can be privileged, but the
determination is fact-specific and contested in some contexts. SFO and UK courts have
scrutinized the privilege claims of internal investigations more aggressively than US courts.

**5. Jurisdiction(s)**

- United States only
- United Kingdom only
- European Union / specific Member States (specify)
- Multi-jurisdictional (specify all)

_Why this matters_: Determines applicable legal framework for privilege, data protection
constraints, employee rights, regulatory cooperation obligations, and self-disclosure strategy.

**6. Government Involvement**

- No known government investigation
- Received subpoena / CID / government inquiry (specify agency)
- Parallel government investigation confirmed
- Company received Wells Notice or target letter

_Why this matters_: Government involvement activates parallel-proceedings management,
privilege-waiver risk when cooperating, obstruction-of-justice constraints on witness
interviews, and immediate strategic decisions on self-disclosure timing.

---

### Step 3: Determine Applicable Regulatory Framework

Based on allegation type and jurisdiction, identify the primary regulatory framework:

#### 3a. US Regulatory Framework Matrix

| Allegation Type            | Primary Regulator            | Key Statute/Framework                                  | Cooperation Path                       | VSD Available? |
| -------------------------- | ---------------------------- | ------------------------------------------------------ | -------------------------------------- | -------------- |
| **Securities fraud**       | SEC, DOJ (Criminal Division) | Securities Act 1933; Securities Exchange Act 1934; SOX | SEC Cooperation Initiative; DOJ CEP    | Yes (DOJ CEP)  |
| **FCPA/bribery**           | DOJ Criminal Division, SEC   | 15 U.S.C. §78dd-1 et seq.; UK Bribery Act 2010         | DOJ FCPA CEP (declination presumption) | Yes            |
| **AML/BSA**                | FinCEN, OCC, FDIC, Fed, DOJ  | 31 U.S.C. §§5311-5336; Bank Secrecy Act                | Consent order; DPA                     | Case-by-case   |
| **Healthcare fraud**       | DOJ, HHS-OIG, CMS            | False Claims Act (31 U.S.C. §§3729-3733); AKS          | Self-disclosure to HHS-OIG; CIA        | Yes            |
| **Government contracting** | DOJ, agency IG, DCAA         | FAR 52.209-5 mandatory disclosure; False Claims Act    | FAR mandatory disclosure               | Mandatory      |
| **Export controls**        | OFAC, BIS, DDTC              | EAR, ITAR, IEEPA                                       | OFAC VSD; BIS VSD                      | Yes            |
| **Antitrust/competition**  | DOJ Antitrust, FTC           | Sherman Act; Clayton Act                               | DOJ Leniency Program                   | Yes (leniency) |
| **Tax fraud**              | IRS, DOJ Tax                 | IRC §7201-7207                                         | DOJ Tax Division VSD                   | Case-by-case   |
| **Environmental**          | EPA, DOJ Environment         | CERCLA, CAA, CWA                                       | EPA Audit Policy VSD                   | Yes            |
| **Employment**             | EEOC, DOL, NLRB              | Title VII, FLSA, NLRA, OSHA                            | Agency mediation                       | N/A            |

#### 3b. UK Regulatory Framework Matrix

| Allegation Type     | Primary Regulator          | Key Statute                                                            | SFO Involvement?                | DPA Available?            |
| ------------------- | -------------------------- | ---------------------------------------------------------------------- | ------------------------------- | ------------------------- |
| **Fraud / bribery** | SFO, CPS                   | Fraud Act 2006; Bribery Act 2010                                       | Yes (for serious/complex fraud) | Yes                       |
| **Financial crime** | FCA                        | POCA 2002; Terrorism Act 2000; Financial Services and Markets Act 2000 | FCA leads                       | FCA Voluntary Attestation |
| **Competition**     | CMA                        | Competition Act 1998; Enterprise Act 2002                              | CMA leads                       | CMA Leniency              |
| **Data breach**     | ICO                        | UK GDPR; DPA 2018                                                      | ICO leads                       | N/A                       |
| **Employment**      | Employment Tribunals, ACAS | Employment Rights Act 1996; Equality Act 2010                          | N/A                             | N/A                       |

#### 3c. EU Regulatory Framework Matrix

| Allegation Type     | Primary Regulator                         | Key Framework                         | Cooperation Mechanism         |
| ------------------- | ----------------------------------------- | ------------------------------------- | ----------------------------- |
| **Antitrust**       | DG COMP (European Commission)             | Regulation 1/2003; Arts. 101-102 TFEU | EU Leniency Programme         |
| **Market abuse**    | ESMA, national NCAs                       | Market Abuse Regulation 596/2014      | Reporting to NCA              |
| **Data protection** | Lead supervisory authority (GDPR Art. 56) | GDPR Regulation 2016/679              | Mandatory breach notification |
| **AML**             | National FIUs, AMLA (from 2025)           | EU AML Package 2024                   | STR filing                    |
| **Cybersecurity**   | National CSIRT, ENISA                     | NIS2 Directive 2022/2555              | 24h/72h reporting             |

---

### Step 4: Establish Investigation Structure

#### 4a. Team Composition

Define the investigation team and reporting lines:

**Investigation Lead:**

- **Outside counsel** (preferred for maximum privilege protection and independence):
  Appropriate when: criminal exposure is possible; government investigation is parallel
  or anticipated; the allegations involve senior management; the board needs independent
  assurance
- **In-house counsel** (appropriate for lower-risk, contained investigations):
  Appropriate when: allegations are relatively minor; no criminal exposure apparent;
  no government investigation; cost efficiency is paramount; matter is managed for legal
  advice purposes
- **HR/compliance lead** (appropriate for employment matters without legal complexity):
  Risk: limited or no privilege protection; not appropriate when criminal exposure possible

**Conflicts Screen**: Before finalizing lead, screen for conflicts:

- [ ] Does the investigation lead represent any implicated individuals?
- [ ] Does the law firm doing the investigation have other significant client relationships
      with implicated individuals?
- [ ] Is in-house counsel implicated or potentially a witness?
- [ ] Does the investigation lead have a prior relationship that creates appearance of bias?

**⟁ CLARIFY** — Conflict identified: If any conflict is present, describe the conflict
and ask: "Should I recommend outside counsel to handle this matter independently, or is
a conflict waiver and screen sufficient?"

#### 4b. Investigation Charter

Draft an investigation charter covering:

```
INVESTIGATION CHARTER — [MATTER NAME]
Date: [Date]
Authorized by: [Board / Audit Committee / CEO / General Counsel]
Authorization basis: [Resolution / Instruction / Regulatory mandate]

MATTER SCOPE:
The investigation covers [allegation description] allegedly occurring during
[time period] involving [individuals/departments]. The scope includes:
- [Specific transaction types, time periods, geographies, individuals]
- [Systems and records to be reviewed]
- [Witnesses to be interviewed]

OUT OF SCOPE:
- [Specify explicitly what is excluded to prevent scope creep]

INVESTIGATION TEAM:
Lead Counsel: [Name, Firm, Engagement Letter Reference]
Supporting Counsel: [Name]
Forensic Accountants / Investigators: [Name, Firm]
Reporting to: [Audit Committee / Board / GC]

CONFIDENTIALITY:
This investigation is protected by attorney-client privilege and work product
doctrine. All materials are confidential. No oral or written communications about
this investigation should occur outside the investigation team without counsel's
approval.

TIMELINE:
Estimated completion: [Date or phase milestones]
Interim reports: [As needed / specific dates]

SCOPE CHANGE PROTOCOL:
Any expansion or reduction in scope requires written authorization from [Audit
Committee / GC / Board].
```

---

### Step 5: Issue Legal Hold and Preserve Evidence

#### 5a. Duty to Preserve

The duty to preserve arises when litigation, investigation, or regulatory action is
reasonably anticipated — not merely when commenced. In the US, failure to preserve can
result in sanctions under FRCP Rule 37(e), including:

| Sanction Level                                  | Conduct Required                                    | FRCP 37(e) Basis |
| ----------------------------------------------- | --------------------------------------------------- | ---------------- |
| **Curative measures** (no finding of bad faith) | Failure to take reasonable steps; prejudice caused  | Rule 37(e)(1)    |
| **Adverse inference instruction**               | Intent to deprive opposing party of use of evidence | Rule 37(e)(2)(A) |
| **Dismissal or default judgment**               | Intent to deprive; most severe                      | Rule 37(e)(2)(B) |

[JURISDICTION-SPECIFIC: UK] UK courts have broad discretionary authority to draw adverse
inferences from destruction of evidence; the leading case is _Douglas v Hello!_ [2003]
EWCA Civ 139. The Civil Procedure Rules Practice Direction 31B governs ESI preservation.

#### 5b. Legal Hold Notice Design

Issue a legal hold notice immediately upon decision to investigate. The notice must:

- [ ] Identify the matter by name (without prejudging outcome)
- [ ] Instruct custodians to preserve ALL potentially relevant documents and data
      (email, text messages, Slack/Teams, voicemail, hardcopy, personal devices used for work)
- [ ] Suspend normal document destruction policies for covered records
- [ ] Define the time period covered
- [ ] List the document categories to be preserved
- [ ] Provide a point of contact for questions
- [ ] Request acknowledgment of receipt and compliance

**Legal Hold Notice Template:**

```
LEGAL HOLD NOTICE — CONFIDENTIAL — PRIVILEGED COMMUNICATION

TO: [Custodian Name(s)]
FROM: [Legal Department / Outside Counsel]
DATE: [Date]
RE: Preservation of Potentially Relevant Documents — [Matter Name]

This notice is protected by attorney-client privilege and work product doctrine.
Do not forward or discuss its contents.

The Company is conducting a legal matter that may require the preservation and
production of documents. Effective immediately, you are required to preserve ALL
documents and electronically stored information (ESI) that may be relevant to:

[Description of the matter — general enough to protect confidentiality while
broad enough to capture relevant materials]

TIME PERIOD: [Start Date] through the present

PRESERVE ALL of the following, regardless of format:
□ Emails and attachments (including deleted items if recoverable)
□ Text messages and instant messages (Slack, Teams, WhatsApp, Signal, iMessage)
□ Documents, spreadsheets, presentations (on shared drives, local drives, USB)
□ Calendar entries, notes, voicemails
□ Records on personal devices if used for work-related communications on this subject
□ Records in third-party systems (cloud storage, SaaS platforms) you have access to

REQUIRED ACTIONS:
1. Immediately suspend any scheduled deletion of documents covered by this hold
2. Do not delete, destroy, modify, or transfer any covered documents
3. Do not discuss this notice or the underlying matter except with legal counsel

ACKNOWLEDGMENT REQUIRED: Please sign and return the attached acknowledgment
within [48 hours / 5 business days] to [contact information].

Questions? Contact [Name] at [email / phone].
```

#### 5c. Custodian Identification

Identify custodians systematically:

- [ ] Primary custodians (directly implicated individuals)
- [ ] Secondary custodians (supervisors, approvers, counterparties)
- [ ] Silent custodians (individuals whose data is preserved but not notified — e.g.,
      IT administrators, departing employees)
- [ ] Third-party data (cloud providers, SaaS platforms, outside counsel files)
- [ ] System-level data sources (ERP, CRM, financial systems, access logs)

#### 5d. ESI Preservation Protocol

For each data source:

| Data Source                         | Preservation Method                             | Priority  | Chain of Custody                |
| ----------------------------------- | ----------------------------------------------- | --------- | ------------------------------- |
| Corporate email                     | Exchange / O365 litigation hold; journaling     | Immediate | IT administrator log            |
| Mobile devices                      | Forensic imaging (Cellebrite or equivalent)     | Immediate | Forensic firm engagement letter |
| Slack / Teams                       | eDiscovery API export; channel-level legal hold | High      | Platform export log             |
| - Shared drives                     | Snapshot / versioning enabled; access log       | High      | IT log                          |
| Personal devices (if used for work) | Voluntary collection or court-ordered imaging   | High      | Consent form / court order      |
| SaaS / cloud                        | API-level preservation (Salesforce, Box, etc.)  | Medium    | Platform confirmation           |
| Physical documents                  | Copy to secure location; log originals          | Varies    | Chain of custody form           |
| Financial systems                   | Read-only export; system access log             | High      | Finance department confirmation |

---

### Step 6: Develop Investigation Plan

#### 6a. Document Review Plan

Define the document review protocol:

**Review Approach Options:**

| Approach                             | Use Case                            | Pros                     | Cons                             |
| ------------------------------------ | ----------------------------------- | ------------------------ | -------------------------------- |
| **Linear review**                    | Small data set (<50GB)              | Simple; defensible       | Time-intensive for large sets    |
| **Technology-Assisted Review (TAR)** | Large data set (>50GB)              | Efficient; courts accept | Requires validation; vendor cost |
| **Targeted keyword search**          | Known issues; specific transactions | Focused; fast            | May miss unknown issues          |
| **Investigative review**             | Complex fraud; requires judgment    | Identifies unknowns      | Resource-intensive               |

**⟁ CLARIFY** — Document volume: Estimate the total data volume and ask: "Should I design
a review protocol optimized for targeted/investigative review (typical for internal
investigations) or full linear review (typical when government production is anticipated)?"

**Privilege Review:**

- Establish a privilege review log (date, author, recipient, subject, privilege basis)
- Tag documents as: Privileged / Responsive-Non-Privileged / Non-Responsive
- Create a clawback agreement under FRE 502(d) before any government production

#### 6b. Witness Interview Schedule

Design the interview sequence:

**Sequencing Principles:**

1. **Peripheral witnesses first** (those not suspected of involvement, who can provide
   context and facts without contamination risk)
2. **Process witnesses second** (those who can explain how systems, controls, approvals
   worked — finance, operations, compliance)
3. **Corroborating witnesses** (those who can confirm or deny key facts)
4. **Core witnesses** (those at the center of the allegations — implicated employees,
   counterparties)
5. **Senior management and executives last** (after documentary foundation is established)

This sequencing prevents early disclosure of the investigation's direction to implicated
witnesses and ensures the investigator has maximum factual context before key interviews.

---

### Step 7: Collect and Review Documents and ESI

#### 7a. Forensic Collection Standards

For defensible ESI collection:

- [ ] Use qualified digital forensics personnel or a reputable forensic firm
- [ ] Preserve the forensic image in read-only format; work from copies
- [ ] Generate and preserve cryptographic hash values (MD5, SHA-256) for all collected items
- [ ] Document chain of custody at every step: who collected, when, from what device/system,
      how transported and stored
- [ ] Record collection metadata: collection date, collector, device serial number, capacity,
      operating system, collection tool and version
- [ ] Where applicable, collect deleted items and unallocated space
- [ ] Issue chain-of-custody forms signed by each custodian from whom physical evidence is received

**Chain-of-Custody Log Fields:**
| Field | Description |
|-------|-------------|
| Item ID | Unique identifier for each collected item |
| Description | Device type, model, serial number |
| Custodian | Name of original custodian |
| Collection date/time | Timestamp of collection |
| Collector | Name and credentials of forensic collector |
| Hash value | MD5 + SHA-256 of original and working copy |
| Transfer date | When transferred to review team |
| Transfer recipient | Review team member who received it |
| Current location | Where stored (with access log) |

#### 7b. Document Review Execution

Apply a multi-pass review approach:

**Pass 1 — Responsiveness**: Identify all documents relevant to the investigation scope
**Pass 2 — Privilege**: Tag privileged documents; prepare privilege log entries
**Pass 3 — Significance**: Identify "hot documents" — documents that materially advance
or refute the allegation
**Pass 4 — Gaps**: Identify missing documents or periods of unusual document scarcity
that may indicate deletion

**⟁ CLARIFY** — Document gaps identified: "The review revealed a gap in [custodian's]
email during [period], which coincides with the alleged misconduct. Should I recommend:
(a) forensic recovery of deleted items; (b) legal hold expansion to backup tapes;
(c) interview custodian about document gap; or (d) all of the above?"

#### 7c. Privilege Logging

Prepare a privilege log for any withheld documents:

| Date   | Author       | Recipients   | Subject/Description                                | Privilege Basis | Redacted/Withheld |
| ------ | ------------ | ------------ | -------------------------------------------------- | --------------- | ----------------- |
| [Date] | [Name, role] | [Name, role] | [Description without revealing privileged content] | AC / WP / Both  | W                 |

**Privilege basis codes:**

- **AC** — Attorney-client privilege (communication seeking or providing legal advice)
- **WP** — Work product doctrine (prepared in anticipation of litigation)
- **JDA** — Joint defense agreement (shared privilege among co-defendants)

---

### Step 8: Plan and Execute Witness Interviews

#### 8a. Pre-Interview Preparation

For each interview, prepare:

- [ ] **Witness profile**: Role, tenure, relationship to allegations, prior statements
- [ ] **Document set**: Key documents to review or show in the interview
- [ ] **Outline**: Open-ended narrative questions → specific fact questions → challenge
      questions (for witnesses with potential adverse interests)
- [ ] **Upjohn warning script** (see §8b)
- [ ] **Logistical considerations**: Location (in-person preferred; video if necessary),
      attendees (lead + note-taker only), recording policy

#### 8b. Upjohn Warning

Administer an Upjohn warning at the outset of every interview of a current employee.
The warning derives from _Upjohn Co. v. United States_, 449 U.S. 383 (1981) and is
required to establish privilege and inform employees of its limits.

**Standard Upjohn Warning Script:**

```
Before we begin, I need to explain a few important things.

1. I am [Name], an attorney at [Firm / Legal Department]. I represent
   [Company Name], not you personally.

2. The purpose of this interview is to gather information to assist the
   Company's legal counsel in providing legal advice to the Company.

3. Our conversation today is protected by the attorney-client privilege.
   However, that privilege belongs to the Company, not to you.

4. This means the Company has the right to decide whether to disclose
   the contents of this interview to third parties, including government
   regulators, without your consent.

5. I am not your personal attorney. If you want your own legal counsel,
   you have the right to consult an attorney before or during this interview.

6. You are expected to answer my questions truthfully and completely.

7. Please do not discuss the contents of this interview with others,
   including your colleagues, to preserve confidentiality.

Do you understand these points? Do you have any questions before we begin?
[Wait for affirmative acknowledgment — note in interview memorandum]
```

**Upjohn Warning — Critical Variations:**

| Situation                               | Modification Required                                                                                                                                                                                                   |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Former employee**                     | Cannot be ordered to participate; may retain own counsel; privilege belongs to Company but individual can seek independent advice                                                                                       |
| **Senior executive implicated**         | Consider whether executive's own interests diverge; executive may need independent counsel; dual representation conflict analysis required                                                                              |
| **Employee likely to be terminated**    | Heightened conflict; individual counsel strongly advisable                                                                                                                                                              |
| **Public sector / government employee** | Garrity warning required (cannot compel self-incriminating statements under threat of termination in US; verify jurisdiction)                                                                                           |
| **UK interview**                        | Note: English courts (ENRC v. Director of the SFO [2018] EWCA Civ 2006) have questioned privilege for dominant-purpose internal investigation documents; obtain UK privilege counsel advice before relying on privilege |

#### 8c. Interview Execution

**Opening Phase:**

1. Administer Upjohn warning and document acknowledgment
2. Explain note-taking (no recording unless explicitly agreed and documented)
3. Ask for a brief professional background to establish witness profile

**Narrative Phase:** 4. Use open-ended questions to elicit the witness's own account: "Can you walk me
through your role in [process/project] during [period]?" 5. Avoid leading questions; allow silences; do not fill pauses 6. Follow the witness's narrative before imposing your document chronology

**Specific Inquiry Phase:** 7. Ask specific questions about key facts, documents, and transactions 8. Show documents in logical sequence; ask witness to identify and explain each 9. Pin down dates, locations, communications, and approval chains 10. Address any inconsistencies with prior statements or documents

**Challenge Phase (for potentially adverse witnesses):** 11. Present contradictory documents calmly and without accusation 12. Ask for the witness's explanation 13. Note evasive, non-responsive, or internally inconsistent answers

**Closing:** 14. Ask: "Is there anything else you think is relevant that I have not asked about?" 15. Advise on confidentiality and next steps 16. Note witness demeanor and any observable indicia of credibility or concern

#### 8d. 5th Amendment and Individual Rights Considerations

[JURISDICTION-SPECIFIC: US] In US investigations:

- Employees have a 5th Amendment right to refuse to answer self-incriminating questions
- However, employees who invoke the 5th Amendment in a corporate interview may face
  employment consequences (termination for failure to cooperate with a legitimate employer
  investigation) — consult employment counsel on jurisdiction-specific limitations
- Companies cannot compel employees to waive 5th Amendment rights as a condition of
  employment in the first instance; the right to terminate for non-cooperation post-hire
  is jurisdiction-specific [VERIFY — state law varies significantly]
- If a grand jury is parallel: advise witnesses to consult their own counsel before
  the interview; do not conduct the company interview in a way that is designed to
  obtain information the government needs for criminal prosecution
- Do NOT conduct interviews of individuals who are subjects or targets of a parallel
  criminal investigation without coordinating with outside counsel to avoid obstruction
  and prejudicing the individual's rights

[JURISDICTION-SPECIFIC: UK] UK employee rights during investigation:

- Employees have the right to be accompanied by a trade union representative or
  colleague in disciplinary/investigatory interviews (Employment Relations Act 1999, s.10)
  — this right applies to investigatory interviews if disciplinary action may follow
- No equivalent 5th Amendment right, but individuals may consult solicitors; note:
  self-incrimination protection under Police and Criminal Evidence Act 1984 (PACE)
  applies if caution is administered

#### 8e. Witness Credibility Assessment

After each interview, complete a credibility assessment:

| Factor                    | Assessment                                                           | Notes                                         |
| ------------------------- | -------------------------------------------------------------------- | --------------------------------------------- |
| **Consistency**           | Internally consistent? Consistent with prior statements?             |                                               |
| **Corroboration**         | Account corroborated by documents or other witnesses?                |                                               |
| **Plausibility**          | Account logically plausible given known facts?                       |                                               |
| **Demeanor**              | Forthcoming, evasive, defensive, agitated?                           | Descriptive only; avoid character conclusions |
| **Detail quality**        | Spontaneous detail consistent with genuine recall? Scripted-seeming? |                                               |
| **Motive to falsify**     | Does witness have a stake in the outcome?                            | Note but do not over-weight                   |
| **Prior inconsistencies** | Any prior conflicting statements on record?                          |                                               |
| **Document alignment**    | Account consistent with or contradicted by key documents?            | Cite specific documents                       |

**Credibility Classification:**

- **HIGH** — Account consistent, corroborated, detailed, plausible, no apparent motive to falsify
- **MEDIUM** — Account generally consistent with some gaps, limited corroboration, or minor inconsistencies
- **LOW** — Material inconsistencies, contradicted by documents, implausible account, or apparent strong motive to falsify
- **INCONCLUSIVE** — Insufficient basis to assess credibility (limited interaction, witness declined to answer)

---

### Step 9: Assess Evidence and Substantiate Allegations

#### 9a. Evidence Matrix

Construct an evidence matrix for each allegation:

| Allegation Element                                          | Evidence For       | Evidence Against    | Source                     | Confidence |
| ----------------------------------------------------------- | ------------------ | ------------------- | -------------------------- | ---------- |
| [Element 1 — e.g., "Payments made to government officials"] | [Document/witness] | [Contrary evidence] | [Bates no./interview date] | [0.X]      |
| [Element 2 — e.g., "Approval by senior management"]         |                    |                     |                            |            |
| [Element 3 — e.g., "Knowledge of improper purpose"]         |                    |                     |                            |            |

#### 9b. Allegation Classification

Apply the following classification to each substantive allegation:

| Classification              | Standard                                                                                                  | Action Required                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **SUBSTANTIATED**           | Preponderance of credible evidence supports the allegation; evidence chain is strong and corroborated     | Report findings; determine regulatory and remedial action; assess VSD obligation                            |
| **PARTIALLY SUBSTANTIATED** | Evidence supports some but not all elements of the allegation; key elements are missing corroboration     | Report qualified findings; identify evidence gaps; consider whether further investigation can resolve       |
| **UNSUBSTANTIATED**         | Credible evidence refutes the allegation, or the evidence in support is insufficient and not corroborated | Document findings; close allegation; preserve investigation record; address any systemic issues identified  |
| **INCONCLUSIVE**            | Evidence is ambiguous, irreconcilable, or insufficient; cannot determine more likely than not             | Document limitations; identify further investigative steps that could resolve; consider whether to continue |

**Note on Standard of Proof:**
Internal investigations use a "preponderance of the evidence" standard (more likely than
not) unless a higher standard is required by applicable law, collective bargaining
agreement, or company policy. [JURISDICTION-SPECIFIC: UK employment] UK employment law
uses the "reasonable belief" standard for disciplinary action — the company need not
prove the employee committed the act, but must have a reasonable belief based on a
reasonable investigation (_British Home Stores Ltd v. Burchell_ [1978] IRLR 379).

#### 9c. Root Cause Analysis

For substantiated findings, identify root causes in four categories:

| Category                       | Examples                                                                                             |
| ------------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Individual conduct**         | Deliberate misconduct; negligent conduct; lack of training; dishonest intent                         |
| **Supervisory failure**        | Failure to supervise; supervisory complicity; tone at the top; inadequate oversight                  |
| **Systemic / process failure** | Inadequate controls; approval bypass; segregation-of-duties gaps; system vulnerabilities             |
| **Cultural / environmental**   | Pressure to meet targets; "ends justify means" culture; fear of raising concerns; compliance fatigue |

Identifying root causes is essential for meaningful remediation. Remediation that addresses
only individual conduct without fixing systemic failures will not satisfy regulators.

---

### Step 10: Evaluate Regulatory Dimensions

#### 10a. Mandatory Reporting Obligations

Assess whether findings trigger mandatory reporting:

**⟁ CLARIFY** — Ask: "Have the investigation findings revealed any of the following?"

| Trigger                                                      | Reporting Obligation                                                                      | Deadline (US)                                           |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Federal government contractor overpayment or false claim     | FAR 52.209-5 mandatory disclosure to contracting officer                                  | "Timely" (interpreted as ~30 days of credible evidence) |
| SEC-reportable item (material weakness, restatement trigger) | SEC Form 8-K, Form 10-K disclosure                                                        | 4 business days (8-K)                                   |
| Data breach involving personal data                          | US state breach notification laws (50 states); GDPR 72h (EU)                              | Varies by state/regime                                  |
| FCPA violation involving US-listed company                   | No standalone mandatory disclosure; but SOX §302/906 certification integrity implications | SOX-driven                                              |
| NIS2 cybersecurity incident                                  | EU: 24h early warning → 72h notification → 1-month final report                           | 24h/72h                                                 |
| AML/BSA suspicious activity                                  | SAR filing with FinCEN                                                                    | 30 days (60 with extension)                             |
| Child exploitation or terrorism-related materials            | Mandatory reporting (NCMEC, law enforcement)                                              | Immediate                                               |

#### 10b. Voluntary Self-Disclosure Decision Framework

**⟁ CLARIFY** — Ask: "Has the company decided whether to make a voluntary self-disclosure
to relevant government authorities? This decision is material and time-sensitive. Should
I model the VSD decision?"

**US VSD Framework (DOJ Criminal Division CEP, as amended November 2024):**

A company that voluntarily self-discloses, fully cooperates, and timely remediates
receives a **presumption of declination** (no prosecution).

**VSD Qualification Criteria:**

1. Disclosure is voluntary (not in response to imminent threat of disclosure or investigation
   already underway with respect to the specific misconduct)
2. Disclosure is timely (before DOJ reaches out; within 120 days of internal whistleblower
   report per Aug 2024 amendment)
3. Disclosure is complete (all known relevant facts at the time)
4. Full cooperation follows (timely production, individual accountability, non-interference
   with witnesses)
5. Appropriate remediation (disciplinary actions, compliance improvements, compensation
   clawback where applicable)

**If VSD criteria not strictly met (Nov 2024 amendment):**
Good-faith disclosure efforts — even if not qualifying for full VSD status — can still
yield: non-prosecution agreement (NPA), increased cooperation credit, shorter DPA terms.
Scope, quantity, quality, impact, and timing of cooperation are all weighed.

**Benefits of VSD + full cooperation + remediation:**

- Presumption of declination (no prosecution)
- No independent compliance monitor (if effective compliance program demonstrated)
- Criminal fine reduction: 50-75% off the low end of Sentencing Guidelines range
- Cooperation credit on individual accountability

**Costs of VSD:**

- Disgorgement of profits from misconduct
- Forfeiture
- Restitution
- Potential public disclosure (DPA/NPA terms are often public)
- Civil litigation exposure (VSD can be used by private plaintiffs)

**VSD Decision Matrix:**

| Scenario                                                                             | VSD Recommended?   | Rationale                                                                                                     |
| ------------------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------- |
| Serious FCPA or other criminal violation; no prior record; strong compliance program | Yes — strong       | VSD qualifies for declination presumption; risk of criminal prosecution without VSD outweighs disclosure cost |
| Isolated incident; no government awareness; effective remediation possible           | Evaluate carefully | If incident can be fully remediated without ongoing risk, cost-benefit requires analysis by outside counsel   |
| Misconduct discovered during M&A due diligence                                       | Yes — often        | CEP provides VSD credit even for acquirees; pre-closing VSD is strategically important                        |
| Government subpoena already received                                                 | No VSD available   | Subpoena triggers the "not voluntary" analysis; focus on cooperation credit instead                           |
| Recidivist — prior related enforcement action                                        | VSD less impactful | VSD credit reduced; likelihood of prosecution higher regardless                                               |

[JURISDICTION-SPECIFIC: UK] UK SFO Self-Reporting (April 2025 Guidance):

If a company self-reports promptly and cooperates fully, the SFO will **invite DPA
negotiation** rather than prosecute, unless exceptional circumstances apply. Key expectations:

- Self-report as soon as reasonably practicable after internal investigation confirms
  credible evidence of serious fraud, bribery, or corruption
- Engage with SFO early during internal investigation to align parameters
- Provide facts gathered during internal investigation to SFO
- Full cooperation: no tipping-off witnesses; proactive identification of individuals
- SFO commitments: respond within 48 business hours; decision on investigation within
  six months; DPA negotiation completed within six months of invitation

#### 10c. Parallel Government Investigation Management

When a government investigation is parallel or anticipated:

**Immediate steps:**

- [ ] Engage outside counsel immediately if not already retained
- [ ] Issue or reinforce legal hold (government likely has its own preservation order)
- [ ] Halt any ongoing employee interviews that could prejudice government investigation
      or create obstruction risk — consult outside counsel before proceeding
- [ ] Document all government contacts (subpoenas, informal requests, agent visits)
- [ ] Establish a single point of contact for all government communications

**Key principles:**

- **Do not obstruct**: Any action that interferes with a government investigation,
  destroys evidence, or suborns witnesses can create additional criminal exposure
  for the company and individuals (18 U.S.C. §1512 witness tampering; §1519 obstruction)
- **Do not tip off**: Companies receiving grand jury subpoenas are generally prohibited
  from notifying targets (although they may notify employees of the subpoena to allow
  them to seek counsel)
- **Grand jury vs. CID**: Materials provided to a grand jury cannot be shared with
  civil regulators without judicial order; CID materials can be shared. Coordinate
  production format strategically with outside counsel
- **Common interest agreements**: If multiple entities or individuals have aligned
  interests, consider a common interest agreement to preserve privilege across parties;
  review DOJ's common interest doctrine position

**DOJ-SEC coordination**: The DOJ and SEC routinely coordinate in parallel investigations.
Document all contacts with each agency; avoid inadvertent inconsistencies in statements
to different agencies; consider whether Reg. FD applies if company is public.

#### 10d. Whistleblower Protections

**Anti-Retaliation Obligations — Activate Immediately Upon Allegation Receipt:**

| Framework                                                           | Protected Activity                                           | Protected Persons                                                | Remedies                                                               |
| ------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **SOX §806** (18 U.S.C. §1514A)                                     | Reporting to employer or SEC; participating in investigation | Public company employees, subsidiaries                           | Reinstatement, back pay, attorneys' fees; contributing-factor standard |
| **Dodd-Frank §922** (15 U.S.C. §78u-6)                              | Reporting directly to SEC                                    | Employees (incl. non-US workers of US-registered companies)      | Double back pay + interest; reinstatement; but-for causation standard  |
| **EU Whistleblowing Directive 2019/1937**                           | Reporting via internal or external channels                  | Employees, contractors, volunteers of 50+ employee organizations | Reversal of burden of proof for employer; reinstatement; compensation  |
| [JURISDICTION-SPECIFIC: UK] **Public Interest Disclosure Act 1998** | Protected disclosures to employer or prescribed persons      | Workers (broad definition includes contractors)                  | Reinstatement; uncapped compensation                                   |

**Anti-Retaliation Protocol:**

- [ ] Flag the complainant's identity to HR for "at-risk" status tracking
- [ ] Ensure no adverse employment actions (termination, demotion, transfer, change in
      duties, harassment) are taken against the complainant during or after the investigation
- [ ] Do not question the complainant in a coercive manner; they retain rights during
      the investigation they triggered
- [ ] DOJ September 2024 ECCP update: DOJ will penalize companies that retaliate against
      whistleblowers, including revoking cooperation credit already earned

---

### Step 11: Draft Findings and Remediation Recommendations

#### 11a. Findings Documentation Standards

For each allegation, produce:

**Findings Summary:**

- Allegation as stated / received
- Classification (SUBSTANTIATED / PARTIALLY / UNSUBSTANTIATED / INCONCLUSIVE)
- Confidence level (see Confidence Scoring, §Quality Frameworks)
- Evidence relied upon (cite specific documents and interview dates)
- Evidence considered but found insufficient or unreliable (cite and explain)
- Applicable legal framework and potential violations identified

**Individual Conduct Findings:**

- For each individual, document: role, alleged conduct, evidence supporting and
  refuting involvement, classification of their conduct, recommended consequence
- Note any adverse inference considerations (deletion of messages, inconsistent testimony,
  invocation of 5th Amendment)

#### 11b. Remediation Recommendations Framework

DOJ ECCP (September 2024 update) focuses on "consequence management" — the company must
demonstrate that it identifies, investigates, disciplines, and remediates violations.

**Remediation Tier Structure:**

| Tier           | Finding Type                                                    | Remediation Actions                                                                                                                       |
| -------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **IMMEDIATE**  | Criminal conduct; ongoing harm; regulatory obligation triggered | Termination of implicated individuals; immediate escalation to board; VSD decision; SAR/breach notification if required; interim controls |
| **NEAR-TERM**  | Substantiated policy violations; control failures               | Disciplinary actions per policy; compliance program redesign; training remediation; clawback initiation; root cause fixes                 |
| **BACKGROUND** | Process improvements; cultural reinforcement                    | Enhanced training; policy updates; monitoring enhancements; tone-at-top communication                                                     |

**Individual Consequence Recommendations:**

| Finding                                   | Recommended Consequence                                         |
| ----------------------------------------- | --------------------------------------------------------------- |
| Knowing participation in criminal conduct | Termination; referral to DOJ (with counsel's review)            |
| Reckless or willful disregard of controls | Termination or significant discipline; clawback of bonuses      |
| Failure of supervision (senior managers)  | Discipline / demotion; reduced compensation; enhanced oversight |
| Negligent compliance failure              | Written warning; retraining; enhanced monitoring                |
| Good-faith error; prompt self-correction  | Counseling; retraining; no formal discipline                    |

**Compliance Program Remediation:**

Identify systemic gaps using the root-cause analysis from Step 9c and recommend:

- Control redesigns to close specific gaps identified in the investigation
- Policy and procedure updates (cite specific policies needing revision)
- Training enhancements (audience-specific; role-based; tested for comprehension)
- Monitoring and audit enhancements (detective controls)
- Reporting channel improvements (ensure anonymity; expand access)

**Compensation Clawback (where applicable):**

DOJ Clawbacks Pilot Program (launched March 2023, ongoing):

- Pursue clawback from individuals who engaged in wrongdoing or had supervisory
  authority and knew of or were willfully blind to misconduct
- Begin clawback efforts before the resolution is finalized
- DOJ provides 100% fine reduction for successfully clawed-back compensation
- Up to 25% fine reduction for good-faith efforts that do not succeed
- [JURISDICTION-SPECIFIC: US public companies] SEC Rule 10D-1 requires written clawback
  policies for erroneously awarded incentive compensation from all executive officers

**Independent Monitor Considerations:**

DOJ will not impose an independent compliance monitor if:

- The company has implemented an effective compliance program at the time of resolution
- The company has demonstrated full remediation
- If a monitor is imposed: typical term is 1-3 years; monitor reports to DOJ; monitor
  costs are company's responsibility (can be substantial)

---

### Step 12: Quality Verification and Report Generation

Before generating the final report, run the quality verification checklist:

- [ ] All allegations addressed with explicit classification
- [ ] Every factual finding cites specific evidence (document Bates number or interview date)
- [ ] All legal conclusions marked with confidence score and [VERIFY] where unverified
- [ ] All [JURISDICTION-SPECIFIC] flags reviewed for accuracy
- [ ] Upjohn warnings documented for all employee interviews
- [ ] Chain-of-custody log complete for all collected evidence
- [ ] Legal hold notices and acknowledgments on file
- [ ] Privilege log complete for all withheld documents
- [ ] VSD decision documented (decision made / decision deferred / not applicable)
- [ ] Whistleblower anti-retaliation measures in place
- [ ] Remediation actions are specific (who, what, by when), not generic

---

## Severity Classification System

| Classification               | Standard                                                                              | Regulatory Risk                                    | Board Reporting                                      |
| ---------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- |
| **SUBSTANTIATED — Critical** | Preponderance of evidence; potential criminal violation or material regulatory breach | Immediate — potential criminal/regulatory exposure | Immediate board/audit committee notification         |
| **SUBSTANTIATED — Material** | Preponderance of evidence; significant compliance or policy violation                 | High — regulatory examination finding likely       | Board report at next meeting; immediate if ongoing   |
| **PARTIALLY SUBSTANTIATED**  | Some elements proven; key elements insufficiently corroborated                        | Moderate — may warrant further investigation       | Report with explicit gaps noted                      |
| **UNSUBSTANTIATED**          | Insufficient credible evidence to support allegation                                  | Low — unless systemic issues discovered            | Report findings; note any systemic concerns          |
| **INCONCLUSIVE**             | Evidence irreconcilable; further investigation required or not feasible               | Varies                                             | Report evidence limitations; recommend further steps |

---

## Prioritization Framework

| Priority     | Criteria                                                                                               | Response Timeline           | Escalation                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------ | --------------------------- | -------------------------------------------------------------- |
| **CRITICAL** | Active criminal violation; ongoing harm; mandatory reporting deadline; parallel criminal investigation | Immediate (within 24 hours) | Board/Audit Committee; Outside Counsel                         |
| **HIGH**     | Substantiated material violation; regulatory filing deadline approaching; VSD timing decision required | Within 5 business days      | GC/CCO; Outside Counsel; Board if senior management implicated |
| **MEDIUM**   | Substantiated policy violation; systemic control gap; significant workplace misconduct                 | Within 30 days              | GC/CCO; HR; Senior Management                                  |
| **LOW**      | Administrative gap; minor policy violation; process improvement opportunity                            | Within 90 days              | CCO; HR; Line Management                                       |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any investigation output. If any gate
fails, revise before delivering.

| Gate           | Rule                                                                                                                          | Fail Action                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific statute, regulation, case, or established principle                                        | Add citation or mark "[UNVERIFIED]"                          |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                   | Fix format (e.g., 18 U.S.C. §1519, not "US obstruction law") |
| **Currency**   | Every cited provision verified as current (statutes not repealed; regulations not superseded; DOJ/SFO policies not updated)   | Flag "[CHECK CURRENCY — DOJ policy updated frequently]"      |
| **Domain**     | Analysis stays within the stated jurisdictional scope; no jurisdictional bleed without explicit [JURISDICTION-SPECIFIC] label | Remove or clearly label                                      |
| **Confidence** | Uncertainty explicitly stated; contested legal doctrines labeled; circuit splits noted                                        | Add confidence qualifier; note circuit split if applicable   |

---

## Self-Interrogation for Critical Findings

For any allegation classified as SUBSTANTIATED — Critical, apply this 3-pass review
before delivering the finding:

**Pass 1 — Evidence Chain Integrity**: Does the finding follow logically from the evidence
cited? Would an experienced prosecutor or regulator reach the same conclusion? Is the
evidence chain complete (document → conduct → intent, where intent is an element)?

**Pass 2 — Completeness**: Have all available evidence sources been considered? Are there
witnesses not yet interviewed who could corroborate or refute? Are there document sets
not yet collected that are relevant? Is there an alternative interpretation of the
evidence that has not been fully considered?

**Pass 3 — Challenge**: What is the strongest defense argument against this classification?
Under what circumstances might a court or regulator decline to act? Is there exculpatory
evidence that should be explicitly addressed in the findings?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                       | Reporting Action                                                               |
| ------------ | --------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Definite** | 0.95-1.0  | Clear documentary evidence; corroborated by multiple witnesses; no credible contrary evidence | State finding with full confidence                                             |
| **High**     | 0.80-0.94 | Strong evidence; minor credibility questions or isolated contrary indicator                   | State finding with brief acknowledgment of uncertainty                         |
| **Probable** | 0.60-0.79 | Good evidence but with unresolved gaps or limited corroboration                               | State finding with explicit notation of evidence gaps                          |
| **Possible** | 0.40-0.59 | Genuine evidentiary ambiguity; credible competing interpretations                             | Flag for further investigation; present both interpretations to decision-maker |
| **Unlikely** | 0.0-0.39  | Weak evidentiary basis; primarily circumstantial; credible exculpatory evidence               | Do not assert; classify as INCONCLUSIVE; note basis                            |

---

## Glass Box Audit Trail

Include this block in all final reports and investigation outputs:

```yaml
glass_box:
  skill_name: "legalcode-internal-investigation"
  mode: "Plan / Execute / Report"
  matter_name: "[Matter name — use code name if not yet disclosed]"
  allegation_type: "[Financial fraud / FCPA / Workplace / Regulatory / etc.]"
  jurisdiction: "[US / UK / EU / Multi-jurisdictional]"
  investigation_lead: "[Outside counsel / In-house counsel / HR / Hybrid]"
  government_involvement: "[None / Subpoena received / Parallel investigation / Target]"
  vsd_decision: "[Made (Yes/No) / Pending / Not applicable]"
  legal_hold_issued: "[Yes — date / No — reason]"
  interviews_completed: "[N interviews; list custodians]"
  documents_collected: "[Volume / Sources]"
  privilege_log_prepared: "[Yes / No / In progress]"
  allegations_addressed: "[N total: X SUBSTANTIATED / Y PARTIALLY / Z UNSUBSTANTIATED / W INCONCLUSIVE]"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[N VERIFIED] / [N marked [VERIFY]]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Assessment based on information provided; actual investigation requires qualified counsel"
    - "Privilege analysis is jurisdiction- and fact-specific; consult privilege counsel before sharing"
    - "VSD timing is critical; decision must be made with current knowledge of government activity"
    - "[Any other matter-specific limitations]"
  reviewer: "AI-assisted — requires review by qualified legal counsel before any action"
```

---

## Anti-Patterns

What NOT to do in a corporate internal investigation:

1. **Failing to issue a legal hold immediately** — Delaying the legal hold by days or
   weeks while "assessing whether an investigation is necessary" creates spoliation risk.
   The duty to preserve arises when litigation or government investigation is _reasonably
   anticipated_, not when it is certain. Issue the hold first; refine scope later.

2. **Upjohn warning failure** — Omitting the Upjohn warning entirely, or giving a
   defective warning that fails to clarify the company — not the employee — holds the
   privilege. A defective warning can result in the interview being attributed to the
   employee (no privilege) or to both (contested waiver).

3. **Investigator conflict blindspot** — Using inside counsel who simultaneously
   represents implicated senior executives, or outside counsel with an existing
   relationship with a key witness. Undisclosed conflicts can destroy privilege, expose
   the company to malpractice claims, and undermine the investigation's credibility with
   regulators.

4. **Interviewing core witnesses first** — Conducting the executive interview before the
   documentary foundation is established. This gives senior witnesses an opportunity to
   shape their account before the investigator has the documents to challenge it.
   Always build the evidentiary record before interviewing core witnesses.

5. **Leading questions in interviews** — Asking "Did [person] tell you to approve the
   payments?" instead of "Walk me through how the approval for these payments happened."
   Leading questions contaminate witness testimony, create challenge material for later
   proceedings, and reduce the value of the interview record.

6. **Selective privilege claims** — Asserting privilege over investigation materials
   with no principled basis for the assertion, or applying privilege inconsistently
   (e.g., claiming privilege for bad-news memos but not routine ones). Selective privilege
   claims are often challenged successfully in litigation.

7. **Sharing investigation materials without 502(d) order** — Producing investigation
   materials to the government without a court order under FRE 502(d) (or equivalent
   in the relevant jurisdiction) risks subject-matter waiver that extends to all
   privileged communications on the topic.

8. **Scope creep without authorization** — Expanding the investigation scope as new
   issues emerge without obtaining board or audit committee authorization. Unauthorized
   scope expansion can result in investigation findings that are not protected by the
   board resolution and creates governance accountability questions.

9. **Tipping off implicated witnesses** — Notifying individuals under investigation
   of the investigation's existence or scope, directly or indirectly, before their
   interview or before their data is collected. Tipping off creates obstruction risk and
   allows witnesses to coordinate accounts or destroy evidence.

10. **Document destruction after trigger** — Any destruction of potentially relevant
    documents after the duty to preserve arises — even pursuant to a routine document
    retention schedule — can constitute spoliation and create severe sanctions exposure.
    Do NOT resume routine destruction until the legal hold is formally lifted.

11. **Conducting interviews without counsel** — HR-led investigations without legal
    oversight create three risks: (a) no privilege protection; (b) no legal framework
    for interview technique; (c) no qualified judgment on the legal implications of
    what is discovered.

12. **Interview recording without consent** — Recording witness interviews without
    consent in jurisdictions requiring all-party consent (California, Illinois, New York
    in some contexts) creates criminal and civil liability. Recording also produces a
    transcript that becomes discoverable; note-taking and memoranda are generally
    preferable [VERIFY — local wiretapping laws].

13. **Parallel interview programs** — Allowing HR to conduct employment-related
    interviews (for disciplinary purposes) simultaneously with legal counsel conducting
    privilege-protected interviews on the same subject matter. Parallel programs create
    dual-hat counsel conflict and may contaminate privilege protection for both programs.

14. **Ignoring EU data protection constraints** — Collecting employee communications,
    monitoring employee devices, or transferring employee data to the US for review without
    establishing a GDPR-compliant legal basis. In most EU jurisdictions, a legitimate
    interest (GDPR Art. 6(1)(f)) combined with a balancing test is the appropriate basis
    for internal investigation data collection, but works council consultation may be
    required first [JURISDICTION-SPECIFIC: see §Works council consultation].

15. **Works council failure (EU/Germany)** — In Germany, France, the Netherlands, and
    many other EU jurisdictions, certain employee monitoring measures require prior works
    council consultation or co-determination (German BetrVG §87(1) No. 6 — monitoring
    of employee conduct via technical means). Proceeding without required consultation
    can render the investigation evidence inadmissible in labor proceedings.

16. **VSD timing failure** — Waiting for the full investigation to be complete before
    deciding on voluntary self-disclosure. The 120-day window (DOJ CEP Aug 2024 amendment)
    from receipt of an internal whistleblower report means delay can forfeit the VSD
    presumption of declination. Make the VSD decision early; complete the investigation
    either pre- or post-disclosure.

17. **Failing to identify root causes** — Producing a findings report that identifies
    what happened and who did it, but not why the controls failed. DOJ ECCP (2024)
    specifically asks: "Why did the compliance program fail to prevent this?" Without
    root cause analysis, the remediation plan cannot be effective, and regulators will
    not give full credit.

18. **Individual accountability gap** — Cooperating with DOJ but failing to identify
    culpable individuals with specificity. The Yates Memo / Monaco Memo / current DOJ
    policy all require that companies seeking cooperation credit must identify individuals
    responsible for the misconduct. Vague findings that describe systemic failures without
    naming responsible individuals receive reduced cooperation credit.

19. **Deficient privilege log** — Logging privileged documents with inadequate
    descriptions (e.g., "Legal advice re: compliance") that do not adequately describe
    the communication without revealing the privileged content. Deficient privilege logs
    result in privilege challenges, in camera review, and potential compelled production.

20. **Overlooking third-party data** — Investigating only company-owned systems while
    ignoring personal email, personal devices, messaging apps, and cloud storage used by
    employees for business communications. Some of the most incriminating evidence in
    major investigations was found on personal devices or encrypted messaging apps
    (WhatsApp deletion example: IFF €15.9M EC obstruction fine, 2024).

21. **Retaliation against the whistleblower** — Taking any adverse employment action
    against the employee who made the allegation, including subtle actions like transfer,
    exclusion from meetings, or increased scrutiny of their work. DOJ's September 2024
    ECCP update specifies that retaliation against whistleblowers will result in loss of
    cooperation credit and possible additional enforcement action.

22. **Failing to engage PR/communications counsel early** — Conducting an investigation
    without a parallel communications strategy for the scenario in which the investigation
    becomes public. Media inquiries received during an investigation require immediate,
    coordinated responses that are consistent with the investigation's privilege and
    cooperation strategy.

---

## Writing Standards

Apply these standards before delivering any investigation output:

1. **Precision**: Name the specific statute, regulation, or guidance document — not
   "applicable law." Write "DOJ CEP (as amended November 2024)" not "DOJ guidelines."

2. **Factual foundation**: Every factual assertion in a findings report must cite its
   source. "The evidence shows that [person] approved [payment] on [date]" must be
   followed by "(Ex. [Bates number]; Interview of [Witness], [Date])."

3. **Neutral framing**: Investigation findings are factual; they do not prejudge criminal
   guilt or civil liability. Write "The evidence is sufficient to conclude that [person]
   approved the payments knowing they were intended for [recipient]" — not "committed
   fraud." Reserve legal conclusions for counsel's analysis section.

4. **Severity alignment**: CRITICAL findings require urgent, specific language;
   LOW findings must not be overstated to appear more significant. Calibrate language
   to severity.

5. **Confidence qualification**: Where evidence is ambiguous, say so explicitly.
   "The evidence is insufficient to determine [person]'s knowledge" is a complete and
   defensible finding. Never assert certainty beyond the evidentiary basis.

6. **[VERIFY] discipline**: Every legal citation from training-data knowledge must be
   marked [VERIFY] unless confirmed through legalcode-mcp or direct source review.
   Never present unverified legal authority as settled fact.

7. **Privilege consciousness**: The investigation report is a privileged document.
   Do not include admissions, candid assessments of criminal exposure, or frank
   regulatory risk analysis in any document that may lose privilege. Separate
   "findings" documents (potentially producible) from "legal analysis" documents
   (privilege-protected).

8. **Tone**: Professional, objective, and non-accusatory in factual sections. Findings
   reports will be read by regulators, courts, and potentially juries; every sentence
   must be defensible.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current DOJ policy documents (CEP, ECCP, Filip Memo) — these are updated
  frequently; always verify the current version
- Search for SFO Corporate Guidance and DPA guidance — updated April 2025
- Research jurisdiction-specific works council requirements (Germany, France, Netherlands)
  before commencing EU investigations
- Verify current whistleblower protection statutes and regulations in applicable jurisdictions
- Research recent enforcement actions for comparable misconduct to calibrate VSD strategy
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and policy citations with [VERIFY]
- Direct users to authoritative sources: DOJ Justice Manual (justice.gov), SFO
  corporate guidance (sfo.gov.uk), EUR-Lex (eur-lex.europa.eu), FCA Handbook (fca.org.uk)
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the investigation plan on structural and procedural quality rather than
  specific legal authority depth

---

## Output Format Template

```markdown
# Corporate Internal Investigation Report — [MATTER NAME]

**Classification: CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGE / WORK PRODUCT**

---

## Header

| Field                | Value                                |
| -------------------- | ------------------------------------ |
| Matter Name          | [Code name]                          |
| Investigation Lead   | [Outside Counsel / In-house Counsel] |
| Reporting to         | [Audit Committee / Board / GC]       |
| Allegation Type      | [Category]                           |
| Jurisdiction(s)      | [US / UK / EU / Multi]               |
| Investigation Period | [Start Date – End Date]              |
| Report Date          | [Date]                               |
| Report Status        | [Preliminary / Interim / Final]      |

---

## Executive Summary

**Overall Assessment**: [SUBSTANTIATED / PARTIALLY SUBSTANTIATED / UNSUBSTANTIATED / INCONCLUSIVE]

**Critical Findings** (if any):

- [Finding 1 — one sentence with severity]
- [Finding 2]

**Top Priority Actions**:

1. [Immediate action with deadline]
2. [Near-term action]
3. [Background action]

**VSD Recommendation**: [Disclose / Do not disclose / Pending — with brief rationale]

---

## Investigation Scope and Methodology

**Allegation as received**: [Verbatim or paraphrased allegation]

**Investigation mandate**: [Authorized by — date — scope]

**Materials reviewed**:

- Documentary: [Volume; sources; date range]
- ESI: [Volume; custodians; platforms]
- Witnesses interviewed: [N witnesses; dates]

**Scope limitations**: [Anything not reviewed and why]

---

## Findings by Allegation

### Allegation [1]: [Description]

**Classification**: [SUBSTANTIATED / PARTIALLY SUBSTANTIATED / UNSUBSTANTIATED / INCONCLUSIVE]
**Confidence**: [Level — 0.X] — [rationale]

**Evidence supporting**:

- [Document description (Bates no. / interview date)]
- [Witness statement summary (Interview of [Name], [Date])]

**Evidence against / gaps**:

- [Counter-evidence or absence of evidence]

**Individual accountability**:
| Individual | Role | Finding | Recommended Consequence |
|-----------|------|---------|------------------------|
| [Name] | [Role] | [Finding] | [Recommendation] |

**Root cause**: [Individual / Supervisory / Systemic / Cultural — describe]

---

## Evidence Matrix

| Allegation Element | Evidence For | Evidence Against | Confidence |
| ------------------ | ------------ | ---------------- | ---------- |
| [Element]          | [Source]     | [Source]         | [0.X]      |

---

## Regulatory Assessment

**Mandatory reporting triggered?**: [Yes / No / Pending]
If yes: [Obligation; deadline; recommended action]

**VSD Analysis**:

- Eligibility: [Qualifies / Does not qualify / Evaluate]
- Benefits: [Expected benefit if disclosed]
- Risks: [Cost of disclosure]
- Recommendation: [Recommend / Do not recommend / Decision for client]

**Parallel government investigation**: [Status; coordination steps taken]

**Whistleblower protections**: [Status; anti-retaliation measures in place]

---

## Remediation Action Plan

### Immediate (0-30 days)

| Action   | Owner  | Deadline | Status    |
| -------- | ------ | -------- | --------- |
| [Action] | [Role] | [Date]   | [Pending] |

### Near-Term (30-90 days)

| Action | Owner | Deadline | Status |
| ------ | ----- | -------- | ------ |

### Background (90+ days)

| Action | Owner | Deadline | Status |
| ------ | ----- | -------- | ------ |

---

## Glass Box Audit Trail

[Insert YAML block from §Glass Box Audit Trail]

---

## Appendices

- Appendix A: Legal Hold Notices and Acknowledgments
- Appendix B: Witness Interview List (dates; topics; Upjohn warning confirmation)
- Appendix C: Document Collection Log (custodians; volumes; platforms)
- Appendix D: Privilege Log
- Appendix E: Evidence Index (key documents referenced in Findings)
- Appendix F: Regulatory Framework Summary (jurisdiction-specific analysis)

---

_This report is protected by attorney-client privilege and work product doctrine.
It was prepared by [law firm] at the direction of [Company] legal counsel in
anticipation of litigation and regulatory proceedings. Do not distribute without
legal counsel approval._
```

---

## Localization Notes

**United States**: Full framework applies. FCPA, SOX, Dodd-Frank, DOJ CEP, SEC
Cooperation Initiative, FRCP, FRE 502 all apply. State law variations in employment
rights and wiretapping statutes require jurisdiction-specific review.

**United Kingdom**: Key differences:

- Privilege for internal investigations: _ENRC v. Director of the SFO_ [2018]
  questioned dominant purpose test for internal investigation documents; English
  courts apply stricter scrutiny than US courts. Obtain UK privilege counsel advice.
- Employee interview rights: Right to be accompanied (Employment Relations Act 1999
  s.10) if investigation may lead to disciplinary action.
- SFO DPA pathway available: requires early engagement per April 2025 guidance.
- Data protection: UK GDPR / DPA 2018; employee data processing requires legal basis
  and privacy notice.
- Tipping-off offence under POCA 2002 may apply if money laundering is suspected.

**European Union / Member States**: Key differences:

- GDPR requires legal basis (typically legitimate interest under Art. 6(1)(f)) for
  employee data collection; conduct balancing test; issue data protection notice.
- Works council consultation required in Germany (BetrVG §87(1) No. 6), France
  (Code du travail Art. L.2312-8), Netherlands (WOR Art. 27) before using technical
  monitoring measures. Failure renders evidence potentially inadmissible.
- EU Whistleblowing Directive 2019/1937: organizations with 50+ employees must have
  internal reporting channels; member-state implementation varies; [VERIFY current
  national law in each member state].
- Competition law investigations (DG COMP): EU leniency programme applies to cartel
  conduct; early disclosure is strategically critical; NCA leniency may also apply.

**Multi-jurisdictional**: Apply a "highest common denominator" analysis for employee
rights and data protection. Design the investigation protocol to comply with the most
restrictive jurisdiction across: interview rights, data collection, privilege, and
reporting obligations.

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis drawing on:

**Legal Framework Sources** [VERIFY all before reliance]:

- DOJ Criminal Division Corporate Enforcement Policy (as amended November 22, 2024)
- DOJ Evaluation of Corporate Compliance Programs (updated September 2024)
- DOJ Justice Manual §§ 9-28.000, 9-47.120
- DOJ Compensation Incentives and Clawbacks Pilot Program (March 2023)
- DOJ November 2024 CEP amendment (120-day whistleblower window)
- _Upjohn Co. v. United States_, 449 U.S. 383 (1981)
- FRE Rule 502 (attorney-client privilege waiver limitations)
- FRCP Rule 37(e) (ESI preservation and spoliation sanctions)
- SOX Section 806 (18 U.S.C. §1514A) — whistleblower protections
- Dodd-Frank Section 922 (15 U.S.C. §78u-6) — SEC whistleblower
- SEC Rule 10D-1 (executive compensation clawback)
- UK SFO Corporate Guidance on self-reporting, cooperation and DPAs (April 2025)
- Crime and Courts Act 2013, Schedule 17 (UK DPA regime)
- Employment Relations Act 1999, s.10 (right to be accompanied)
- _ENRC v. Director of the SFO_ [2018] EWCA Civ 2006 (UK privilege for investigations)
- EU Whistleblowing Directive 2019/1937
- GDPR Regulation 2016/679 Arts. 5-6, 88
- German Betriebsverfassungsgesetz §87(1) No. 6 (works council co-determination)
- _British Home Stores Ltd v. Burchell_ [1978] IRLR 379 (UK reasonable belief standard)
- European Commission v. International Flavors & Fragrances — €15.9M obstruction fine (2024)
- ABA White Collar Crime Committee — Upjohn Warning Best Practices

**Methodology**: 2-agent research pipeline (structural analyst + legal researcher) with
parallel web-backed research across DOJ guidance, SFO cooperation framework, EU
enforcement, privilege doctrine, ESI standards, whistleblower protections, interview
techniques, and remediation frameworks. Cross-referenced against legalcode-contract-review
quality bar for structural completeness.

**No prior skill on this topic** was present in the skills repository at time of creation.
