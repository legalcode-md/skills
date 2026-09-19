---
name: legalcode-breach-regulatory-notification-drafter
description: 'Draft jurisdiction-specific regulatory notification documents for data protection authorities
  (DPAs), Attorneys General, and sector regulators following a confirmed data breach. Use when you need
  to produce a submission-ready regulatory notification: GDPR Art. 33 supervisory authority notification
  (72-hour timeline), UK ICO breach report, US state Attorney General notification letters (per-state
  format requirements), Australian OAIC Notifiable Data Breach Statement, Canadian OPC / Quebec CAI breach
  report, and Brazilian ANPD incident notification.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft jurisdiction-specific regulatory notification documents for data protection authorities (DPAs), Attorneys General, and sector regulators following a confirmed data breach. Use when you need to produce a submission-ready regulatory notification: GDPR Art. 33 supervisory authority notification (72-hour timeline), UK ICO breach report, US state Attorney General notification letters (per-state format requirements), Australian OAIC Notifiable Data Breach Statement, Canadian OPC / Quebec CAI breach report, and Brazilian ANPD incident notification. Produces formatted, citation-checked notification documents meeting each regulator's mandatory content requirements — nature of breach, categories and approximate number of data subjects, likely consequences, measures taken and proposed, DPO contact details, and timeline of events. Integrates with legalcode-breach-severity-assessment for upstream harm triage and legalcode-us-breach-notification-triage for US state deadline mapping. Covers EU / UK / US / AU / CA / BR multi-regime incidents with parallel-regulator sequencing, phased notification support, and Glass Box audit trail.


# Legalcode Breach Regulatory Notification Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of regulatory
> data breach notifications. It does not constitute legal advice. All draft notifications
> must be reviewed by qualified legal counsel licensed in the relevant jurisdiction(s)
> before submission to any regulator. Laws, regulator guidance, portal formats, and
> submission deadlines change frequently — verify current requirements against official
> regulator guidance before dispatching any notification. Statutory citations and timelines
> in this skill are based on research as of early 2026 and carry hallucination risk; mark
> any unverified claim `[VERIFY]` and cross-check against authoritative sources before
> relying on them. Late or deficient regulatory notifications can result in enforcement
> action, civil penalties, and reputational harm.

---

## Purpose and Scope

This skill drafts submission-ready regulatory notification documents for personal data
breaches across six major jurisdictions. It takes confirmed breach facts (from
`legalcode-breach-severity-assessment` or equivalent analysis) and produces formatted
notification letters, structured forms, and individual notices that satisfy each
regulator's mandatory content requirements.

**Covers:**

- GDPR Article 33 supervisory authority notification (EU, 72-hour timeline)
- UK ICO data breach report (UK GDPR, 72-hour timeline)
- US state Attorney General notification letters (per-state format and threshold)
- Australian OAIC Notifiable Data Breach (NDB) Statement (Privacy Act Part IIIC)
- Canadian OPC breach report (PIPEDA + SOR/2018-64) and Quebec CAI confidentiality
  incident report (Law 25)
- Brazilian ANPD incident notification (LGPD Art. 48 + ANPD Resolution 15/2024)
- Individual data subject notice (multi-regime template)
- Phased/supplementary notification support for all regimes
- Multi-regulator sequencing for parallel notification duties
- Document element classification: REQUIRED / RECOMMENDED / OPTIONAL per regulator
- Glass Box audit trail for defensible decision documentation
- Playbook support for pre-approved organizational language and signature blocks

**Does not:**

- Determine whether a breach is notifiable (use `legalcode-breach-severity-assessment`)
- Triage US state notification obligations and deadlines (use
  `legalcode-us-breach-notification-triage`)
- Perform forensic root-cause analysis or incident containment
- Provide legal advice or replace qualified data protection counsel
- Cover sector-specific overlays in full (HIPAA, GLBA, SEC, FCC, CIRCIA) without
  explicit localization — flag for specialist counsel
- Guarantee regulatory outcome or enforceability of any submission

**Related skills:**

- `legalcode-breach-severity-assessment` — upstream harm triage; feed its output into
  Step 1 of this skill
- `legalcode-us-breach-notification-triage` — US-specific obligation mapping and
  per-state deadline matrix; use in parallel with this skill for US incidents
- `legalcode-data-mapping-workflow` — data inventory; informs categories of data affected
- `legalcode-dsar-workflow-builder` — individual rights management post-breach

---

## Jurisdiction and Governing Law

This skill covers six parallel legal regimes. Each has distinct notification triggers,
timelines, content requirements, and submission formats. For multi-jurisdiction incidents,
the skill coordinates parallel notifications and sequences drafts by deadline urgency.

| Regime        | Legal Basis                                                                 | Regulator                                                | Timeline                                                                                  | Format                                     |
| ------------- | --------------------------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------ |
| EU GDPR       | Art. 33 (Regulation 2016/679); EDPB Guidelines 9/2022                       | Lead DPA (LSA) via one-stop-shop                         | 72 hours from awareness                                                                   | Letter to DPA; phased supplement permitted |
| UK GDPR       | Art. 33 (UK GDPR retained); ICO guidance; DUA Act 2025                      | Information Commissioner's Office (ICO)                  | 72 hours from awareness                                                                   | ICO online reporting portal or letter      |
| United States | Varies by state (all 50 states + DC + territories); HIPAA/GLBA/SEC overlays | State Attorney General; sector regulators                | Varies: 30 days (most); 10 days (Puerto Rico); 72h (federal HIPAA/GLBA)                   | Letter; some states have forms             |
| Australia     | Privacy Act 1988 Part IIIC; OAIC NDB Guidance                               | Office of the Australian Information Commissioner (OAIC) | Assess within 30 days; notify ASAP                                                        | OAIC online NDB form                       |
| Canada        | PIPEDA + SOR/2018-64; Quebec Law 25 Arts. 3.5-3.6; BC PIPA; AB PIPA         | OPC (federal); CAI (Quebec); provincial commissioners    | As soon as feasible (no hard statutory deadline under PIPEDA); Quebec: 72-hour equivalent | Structured report to OPC; CAI online form  |
| Brazil        | LGPD Art. 48; ANPD Resolution CD/ANPD 15/2024                               | Autoridade Nacional de Proteção de Dados (ANPD)          | 3 business days (initial); 20 business days (complementary)                               | ANPD online portal form                    |

[JURISDICTION-SPECIFIC] Always verify current regulator portal formats, submission
deadlines, and guidance before dispatching any notification. Regulatory portals and
guidance documents update without advance notice.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming breach facts or regulatory scope, the workflow pauses and asks when:

- The answer changes which regulators must be notified
- Timeline constraints require priority sequencing of notification drafts
- The user's organizational context affects the notification content
- Uncertainty in breach facts creates drafting forks (estimated vs. confirmed figures)

Use the structured-options pattern (options + "why this matters" explanations) wherever
marked with **⟁ CLARIFY** below. If the user has already provided the information,
skip the question and proceed. For batch/automated runs, apply the defaults stated at
each gate.

---

## Workflow

### Step 1: Accept Breach Facts

Accept incident facts in any of these formats:

- Output from `legalcode-breach-severity-assessment` (preferred — provides structured
  harm assessment and regulator duty matrix)
- Incident ticket or internal breach investigation report
- Forensic investigation summary (partial or complete)
- Free-text narrative of the incident
- Structured breach description pasted directly

Extract and normalize:

- **Discovery date and time** (with timezone)
- **Awareness date** (controller's reasonable-certainty date — may differ from discovery)
- **Nature of the breach** (unauthorized access, unauthorized disclosure, loss/destruction,
  alteration, other)
- **Systems/assets affected**
- **Data categories involved** (identify any Art. 9/10 GDPR special categories or
  equivalent sensitive categories)
- **Approximate number of data subjects** (confirmed or estimated range)
- **Geographic distribution of data subjects** (jurisdictions represented)
- **Harm assessment** (risk of serious harm confirmed? Likely? Unknown?)
- **Containment status** (breach ongoing or contained?)
- **Prior notifications** (any regulator already notified?)

If any of these facts are unknown, mark them as `[TBC — provide when available]` and flag
for phased notification under applicable regimes.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the jurisdiction and regulator analysis, gather
organizational context. Skip questions already answered by the incident report.

**Gate 1 — Controller Role and Establishment**

- Options: (a) Data controller — EU/UK main establishment identified, (b) Data controller
  — non-EU/non-UK, processing EU/UK data, (c) Processor notifying on behalf of controller,
  (d) Joint controllers — formal arrangement exists, (e) Unknown
- _Why this matters_: Controller's main establishment determines which EU Member State DPA
  leads notification. Processors notify controllers, not DPAs. Non-EEA controllers without
  EU/UK establishment must notify each competent national DPA independently.

**Gate 2 — Jurisdictions to Cover**

- Options: (a) EU only, (b) EU + UK, (c) US only, (d) US + EU/UK, (e) All six regimes
  (EU/UK/US/AU/CA/BR), (f) Subset — user specifies
- _Why this matters_: Determines which notification documents to produce and which
  regulatory timelines to sequence.

**Gate 3 — Breach Severity and Harm Confirmation**

- Options: (a) High-risk breach — individual notification required under GDPR Art. 34
  and/or equivalent, (b) Moderate risk — regulator notification required, individual
  notification discretionary, (c) Risk unclear — assessment in progress, (d) Already
  severity-assessed (provide output)
- _Why this matters_: Affects whether individual data subject notices must be drafted
  alongside regulatory notifications. For GDPR, Art. 34 individual notification is
  triggered by "high risk" — a higher threshold than Art. 33.

**Gate 4 — Scope of Documents Required**

- Options: (a) Regulatory authority notifications only (DPA/OAIC/ANPD/OPC),
  (b) Regulatory + AG/public authority letters (US state, Canada provincial),
  (c) Regulatory + AG + individual data subject notice,
  (d) Full package: all of the above + phased supplement templates
- _Why this matters_: Each document type has different drafting requirements, audience,
  and tone. Individual notices are plain-language; regulatory letters are formal.

**Gate 5 — DPO and Organizational Contact Details**

- Options: (a) Provide now (name, title, email, phone), (b) Use placeholders
  `[DPO_NAME]`, `[DPO_EMAIL]`, `[DPO_PHONE]` for completion, (c) No DPO — use General
  Counsel contact
- _Why this matters_: GDPR Art. 33(3)(b) mandates DPO or contact-point details in the
  supervisory authority notification. Omitting this is a common drafting deficiency.

**Gate 6 — Organizational Playbook**

- Options: (a) Load playbook from file path, (b) Load playbook from URL,
  (c) No playbook — use statutory defaults throughout, (d) Use general standards but note
  deviations from typical positions
- _Why this matters_: Playbook contains pre-approved organizational language, signature
  blocks, escalation thresholds, and AG contact lists. Without a playbook, the skill uses
  statutory defaults and flags all content for legal review before dispatch.

**Defaults for non-interactive runs**: EU GDPR main establishment assumed; all six regimes
covered; high-risk breach assumed (individual notification required); full package
produced; DPO placeholder used; general standards applied.

---

### Step 3: Load Regulatory Playbook

If a playbook is provided, extract:

1. **Approved signature block** — authorized signatory (DPO or legal representative),
   title, organization, contact details
2. **Pre-approved language modules** — organization-specific language for each mandatory
   section (nature of breach, measures taken, etc.)
3. **Regulator contact directory** — DPA addresses/portals, US AG submission details,
   OAIC form URL, ANPD portal, OPC address, CAI form
4. **Escalation thresholds** — when C-suite review required before dispatch (e.g.,
   > 10,000 affected data subjects; breach involving financial or health data; media
   > attention likely)
5. **Timeline constraints** — internal review gates (e.g., "Legal sign-off required
   before DPA submission; allow 4 hours")
6. **Prior notification history** — any prior notifications to this regulator for
   previous incidents (affects tone and context of current notification)

If no playbook is available, apply statutory defaults:

- Signature block: `[AUTHORIZED_SIGNATORY_NAME], [TITLE], [ORGANIZATION]`
- Regulator contacts: use statutory addresses noted in each regime section below; flag
  for verification
- Escalation threshold: flag all draft documents as "requires legal review before
  dispatch"
- Timeline constraints: notify as early as possible consistent with factual accuracy

---

### Step 4: Build the Jurisdiction and Regulator Matrix

Construct the Jurisdiction and Regulator Matrix based on the breach facts and CLARIFY
context. This is the master coordination table for the notification package.

```markdown
## Jurisdiction & Regulator Matrix

| Jurisdiction             | Regime                          | Applicable Regulator | Legal Basis        | Clock Start                                     | Deadline                           | Documents Required              | Status |
| ------------------------ | ------------------------------- | -------------------- | ------------------ | ----------------------------------------------- | ---------------------------------- | ------------------------------- | ------ |
| EU (Lead DPA: [COUNTRY]) | GDPR                            | [Lead DPA Name]      | Art. 33(1)         | [Awareness Date/Time + TZ]                      | [72h deadline in local time]       | DPA notification letter         | DRAFT  |
| United Kingdom           | UK GDPR                         | ICO                  | Art. 33(1) UK GDPR | [Awareness Date/Time + TZ]                      | [72h deadline in local time]       | ICO report                      | DRAFT  |
| [STATE], United States   | [STATE] Breach Notification Act | [STATE] AG           | [Statute citation] | [Clock start: discovery/awareness/confirmation] | [Deadline: calendar/business days] | AG notification letter          | DRAFT  |
| Australia                | Privacy Act 1988 Part IIIC      | OAIC                 | s. 26WH            | [Date of becoming aware]                        | [ASAP; assessed within 30 days]    | NDB Statement (form)            | DRAFT  |
| Canada (Federal)         | PIPEDA + SOR/2018-64            | OPC                  | s. 10.1 PIPEDA     | [Awareness date]                                | [As soon as feasible]              | Breach report                   | DRAFT  |
| Canada (Quebec)          | Law 25 Art. 3.5                 | CAI                  | Art. 3.5           | [Awareness date]                                | [72h-equivalent]                   | Confidentiality incident report | DRAFT  |
| Brazil                   | LGPD + ANPD Res. 15/2024        | ANPD                 | Art. 48 LGPD       | [Confirmation date]                             | [3 business days initial]          | ANPD incident notification      | DRAFT  |
```

**Regulator Priority Sequencing** — sequence drafts by deadline urgency:

1. **Priority 1** — 72-hour window: EU GDPR, UK GDPR, Brazil ANPD (3 business days)
2. **Priority 2** — 30 days or fewer: Most US states, Australian OAIC (30-day assess);
   Quebec CAI
3. **Priority 3** — As soon as feasible (no hard deadline): Canada OPC under PIPEDA
4. **Priority 4** — Individual data subject notices (concurrent with or after regulatory;
   check each regime)

If multiple Priority 1 deadlines apply simultaneously, complete them in parallel.

---

### Step 5: Map Content Requirements per Regulator

Before drafting, construct the **Content Requirements Matrix**. This prevents omitting
mandatory elements and ensures each document satisfies the applicable legal standard.

#### Content Element Classification

| Status          | Definition                                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| **REQUIRED**    | Legal framework explicitly mandates this element; omission is a notifiable deficiency                 |
| **RECOMMENDED** | Regulator guidance or best practice strongly advises inclusion; omission may invite follow-up inquiry |
| **OPTIONAL**    | Context-dependent; include if facts warrant or playbook specifies                                     |
| **[VERIFY]**    | Requirement uncertain or recently amended; verify before drafting                                     |

#### Master Content Requirements Table

| Content Element                     | EU GDPR Art. 33                     | UK ICO      | US State AG            | Australia OAIC         | Canada OPC  | Brazil ANPD       |
| ----------------------------------- | ----------------------------------- | ----------- | ---------------------- | ---------------------- | ----------- | ----------------- |
| Nature/type of breach               | REQUIRED (Art. 33(3)(a))            | REQUIRED    | REQUIRED (most states) | REQUIRED               | REQUIRED    | REQUIRED          |
| Categories of data subjects         | REQUIRED (Art. 33(3)(a))            | REQUIRED    | REQUIRED               | REQUIRED               | REQUIRED    | REQUIRED          |
| Approx. number of data subjects     | REQUIRED (Art. 33(3)(a))            | REQUIRED    | REQUIRED               | REQUIRED               | RECOMMENDED | REQUIRED          |
| Categories of personal data records | REQUIRED (Art. 33(3)(a))            | REQUIRED    | REQUIRED               | REQUIRED               | REQUIRED    | REQUIRED          |
| Approx. number of data records      | REQUIRED (Art. 33(3)(a))            | REQUIRED    | OPTIONAL               | OPTIONAL               | OPTIONAL    | RECOMMENDED       |
| DPO / contact point details         | REQUIRED (Art. 33(3)(b))            | REQUIRED    | REQUIRED               | REQUIRED (ABN contact) | REQUIRED    | REQUIRED          |
| Likely consequences of breach       | REQUIRED (Art. 33(3)(c))            | REQUIRED    | RECOMMENDED            | RECOMMENDED            | RECOMMENDED | REQUIRED          |
| Measures taken                      | REQUIRED (Art. 33(3)(d))            | REQUIRED    | REQUIRED               | REQUIRED               | REQUIRED    | REQUIRED          |
| Measures proposed                   | RECOMMENDED (implied Art. 33(3)(d)) | RECOMMENDED | RECOMMENDED            | REQUIRED               | RECOMMENDED | REQUIRED          |
| Timeline of events                  | RECOMMENDED (EDPB Guidelines)       | RECOMMENDED | RECOMMENDED            | OPTIONAL               | OPTIONAL    | RECOMMENDED       |
| Consumer notification date          | N/A                                 | N/A         | REQUIRED (most states) | OPTIONAL               | OPTIONAL    | OPTIONAL          |
| Notification method to individuals  | N/A                                 | N/A         | REQUIRED (most states) | RECOMMENDED            | RECOMMENDED | RECOMMENDED       |
| Sample individual notice attached   | N/A                                 | N/A         | REQUIRED (CA, NY, FL)  | N/A                    | N/A         | N/A               |
| Credit monitoring offer             | N/A                                 | N/A         | REQUIRED (some states) | N/A                    | N/A         | N/A               |
| Cross-border transfer involvement   | OPTIONAL                            | OPTIONAL    | N/A                    | N/A                    | N/A         | OPTIONAL          |
| Data processor identity             | OPTIONAL                            | OPTIONAL    | N/A                    | OPTIONAL               | OPTIONAL    | OPTIONAL          |
| Organization ABN/CNPJ/registration  | N/A                                 | N/A         | N/A                    | REQUIRED               | N/A         | REQUIRED          |
| Police report reference             | N/A                                 | N/A         | OPTIONAL               | OPTIONAL               | N/A         | REQUIRED [VERIFY] |

For US state AG letters, consult `legalcode-us-breach-notification-triage` for
state-specific content requirements, thresholds, and submission instructions.

---

### Step 6: Draft Regulatory Authority Notifications

Draft each notification document in sequence (Priority 1 first). Apply the template
structure below, filling in breach facts and organization-specific language.

For each drafted section:

- Cite the specific legal provision mandating the section
- Assign a Confidence Score to the draft's regulatory compliance
- Mark any uncertain facts as `[TBC]` with a note on when they will be available
- Mark any uncertain legal interpretations as `[VERIFY]`

#### 6a. EU GDPR Article 33 Supervisory Authority Notification

**When to use**: Controller notifying the Lead DPA under GDPR one-stop-shop mechanism
for cross-border processing; or notifying the competent local DPA for single-Member-State
processing.

**Lead DPA determination**:

- Main establishment (central administration in EU) → DPA of that Member State leads
- Multiple EU establishments → DPA of Member State where highest-level management making
  decisions on processing is located
- Non-EEA controller with EU representative → DPA of the Member State where the
  representative is established
- Non-EEA controller without EU/EEA representative → notify each competent national DPA
  independently [VERIFY with legal counsel]

**Format**: Formal letter (1–3 pages). Many DPAs also accept online portal submissions;
check national DPA website for preferred format. [VERIFY] ICO (UK) has its own portal
separate from EU DPAs.

---

**TEMPLATE: GDPR Art. 33 Supervisory Authority Notification**

```
[ORGANIZATION LETTERHEAD]

[DATE]

To: [LEAD DPA NAME]
[LEAD DPA ADDRESS]
[LEAD DPA EMAIL / ONLINE PORTAL URL]

Re: Personal Data Breach Notification pursuant to Article 33 of Regulation (EU)
2016/679 (GDPR)

Reference: [INTERNAL INCIDENT ID] — [DATE OF FIRST NOTIFICATION / SUPPLEMENT NO. X]

Dear [SALUTATION — e.g., "The Data Protection Officer" or specific contact if known],

We write to notify [LEAD DPA NAME] of a personal data breach in accordance with Article
33(1) of the General Data Protection Regulation (Regulation (EU) 2016/679), which
came to our attention on [AWARENESS DATE AND TIME, TIMEZONE].

---

1. NATURE OF THE BREACH [Art. 33(3)(a)]
Confidence: [HIGH] — statutory requirement clearly defined

Type of breach: [Select: unauthorized access / unauthorized disclosure / accidental loss
/ destruction / alteration / combination]

Description: [Plain-language description of what occurred. Example: "On [DATE], we
discovered that an unauthorized third party accessed our [SYSTEM NAME] containing
customer personal data. The unauthorized access occurred between [DATE FROM] and
[DATE TO] and was detected by our security monitoring systems on [DETECTION DATE]."]

Attack vector / cause: [Technical mechanism if known — e.g., phishing credential
compromise, unpatched vulnerability, insider threat, physical loss. Mark [TBC] if
investigation is ongoing.]

Systems affected: [List affected systems, databases, or services]

Data subjects and categories: [e.g., "Registered customers of [PRODUCT LINE]"]

Number of data subjects affected: [Confirmed count: [N]] / [Estimated range: [N]–[M]]
[If exact count unavailable, state: "Our investigation is ongoing; we estimate
approximately [N] data subjects are potentially affected. An updated count will follow
as a phased supplement pursuant to Article 33(4)."]

Categories of personal data records affected:
□ Names and contact information (email, phone, address)
□ National identification numbers (e.g., Social Security Numbers, Tax ID, Passport)
□ Financial data (account numbers, payment card data, credit/debit information)
□ Health or medical data [Art. 9 special category]
□ Biometric data [Art. 9 special category]
□ Location data
□ Online identifiers (IP addresses, user IDs, device identifiers)
□ Other: [specify]

Approximate number of personal data records affected: [N] records / [TBC]

---

2. DATA PROTECTION OFFICER / CONTACT POINT [Art. 33(3)(b)]
Confidence: [HIGH]

Name: [DPO_NAME]
Title: [Data Protection Officer] / [Privacy Counsel] / [Contact Point for Data
Protection Matters]
Organization: [ORGANIZATION_FULL_LEGAL_NAME]
Email: [DPO_EMAIL]
Phone: [DPO_PHONE]
Address: [DPO_MAILING_ADDRESS]

We invite [LEAD DPA NAME] to direct any requests for further information to the above
contact.

---

3. LIKELY CONSEQUENCES OF THE BREACH [Art. 33(3)(c)]
Confidence: [PROBABLE — depends on harm assessment interpretation]

Based on the categories of personal data involved and the nature of the breach, the
likely consequences include:

[Select/adapt as applicable:]
□ Risk of identity theft or fraud: The breach involves [identity/financial data],
  creating risk that affected individuals may be targeted by fraud or identity theft.
□ Financial loss: [If financial account data involved] — risk of unauthorized financial
  transactions.
□ Reputational damage to data subjects: [If sensitive personal or professional data
  involved].
□ Discrimination or social disadvantage: [If special category data per Art. 9 involved].
□ Loss of control over personal data: Data subjects may have reduced control over how
  their information is used.
□ Other: [specify]

[If low-risk breach]: Based on our harm assessment, the breach is unlikely to result in
high risk to the rights and freedoms of data subjects because [REASON: e.g., data was
encrypted; limited sensitivity; no evidence of exfiltration].

---

4. MEASURES TAKEN AND PROPOSED [Art. 33(3)(d)]
Confidence: [HIGH]

Measures already taken:

Technical containment:
□ [Access terminated / systems taken offline / credentials reset on [DATE]]
□ [Malware removed / vulnerability patched on [DATE]]
□ [Forensic investigation initiated — [FIRM NAME] engaged on [DATE]]
□ [Affected records quarantined / encrypted]

Organizational measures:
□ [Internal incident response team convened on [DATE]]
□ [Relevant staff briefed on [DATE]]
□ [Relevant processors/vendors notified on [DATE]]
□ [Law enforcement notified on [DATE] — Reference: [REPORT NUMBER]] [if applicable]

Measures proposed / underway:
□ [Enhanced security controls: [DESCRIPTION]]
□ [Additional security monitoring: [DESCRIPTION]]
□ [Security audit / penetration testing scheduled: [DATE]]
□ [Staff security training: [DATE]]
□ [Notification to affected data subjects: [TIMELINE]] [if required under Art. 34]
□ [Credit monitoring or identity protection services offered: [DESCRIPTION]] [if applicable]
□ [Regulatory review of processing systems for systemic vulnerabilities]

---

5. TIMELINE OF EVENTS [RECOMMENDED — EDPB Guidelines 9/2022]
Confidence: [HIGH]

| Date/Time (TZ) | Event |
|---|---|
| [DATE TIME TZ] | Breach occurrence (known or estimated) |
| [DATE TIME TZ] | First internal detection / discovery |
| [DATE TIME TZ] | Controller's awareness with reasonable certainty |
| [DATE TIME TZ] | Internal incident response team convened |
| [DATE TIME TZ] | Breach scope confirmed (or [TBC]) |
| [DATE TIME TZ] | Forensic investigation commenced |
| [DATE TIME TZ] | This notification dispatched |
| [DATE TIME TZ] | [Any prior regulator notifications] |

[If notifying after 72 hours, add:]
We note that this notification is submitted [X hours/days] after the awareness date
noted above. The delay occurred because: [REASON — e.g., "we required a minimum
threshold of forensic certainty before triggering the notification; investigation to
that threshold was completed on [DATE]."] We provide this explanation in accordance with
Article 33(1), which requires accompanying reasons for late notification.

---

6. PHASED NOTIFICATION NOTICE [OPTIONAL — use if investigation is ongoing]
[Art. 33(4)]

This notification constitutes an initial notification pursuant to Article 33(4). Not all
required information is available at this time because [REASON: e.g., forensic
investigation is ongoing; scope of affected data records is being determined].

We commit to providing the following supplementary information by [TARGET DATE]:
□ Confirmed count of affected data subjects
□ [Other pending items]

We will contact [LEAD DPA NAME] as soon as the above information is available, and no
later than [TARGET DATE].

---

Yours faithfully,

[DPO_NAME]
[TITLE]
[ORGANIZATION_FULL_LEGAL_NAME]
[DATE]

Enclosures: [List any attachments — e.g., forensic summary, sample individual notice]
```

**Self-Interrogation for High-Risk Sections** (run before delivering the draft):

_Pass 1 — Legal Chain Integrity_: Does the "Likely Consequences" section (§3) follow
logically from the data categories and breach type described in §1? Would the DPA agree
that the harm assessment is proportionate and realistic — neither catastrophizing
nor minimizing?

_Pass 2 — Completeness_: Are all four Art. 33(3) paragraphs present? Is the DPO
contact complete? If notifying after 72 hours, is the delay explanation included?

_Pass 3 — Challenge_: What is the strongest argument that this notification is
deficient? Missing categories? Approximate counts not included? Measures inadequate?

---

#### 6b. UK GDPR / ICO Breach Report

**When to use**: Breach affects UK data subjects; controller has UK establishment or
processes UK personal data without establishment.

**Key differences from EU GDPR Art. 33**:

- Recipient: Information Commissioner's Office (ICO)
- ICO preferred submission: online reporting portal at ico.org.uk/for-organisations/
  report-a-breach [VERIFY current URL]
- UK GDPR Art. 33 is substantively identical to GDPR Art. 33 post-Brexit
- Data (Use and Access) Act 2025 (commencement ongoing): monitor for amendments to UK
  GDPR notification obligations — check ICO guidance for updates [VERIFY]
- ICO guidance emphasizes: report even if investigation is incomplete; report and update
- ICO's 72-hour clock interpretation: same "reasonable certainty" standard as EDPB
- For multi-national incidents: EU DPA notification does NOT automatically notify ICO;
  UK notification is legally distinct

**Format**: Use the ICO's online reporting portal where available. If portal is
unavailable or for complex incidents requiring narrative explanation, submit a formal
letter using the GDPR Art. 33 template above with the following modifications:

```
[ORGANIZATION LETTERHEAD]
[DATE]

To: Information Commissioner's Office
Wycliffe House, Water Lane, Wilmslow, Cheshire, SK9 5AF
Email: casework@ico.org.uk [VERIFY current breach reporting email]

Re: Data Breach Notification pursuant to Article 33, UK General Data Protection
Regulation (UK GDPR)

[Use same section structure as EU GDPR Art. 33 template above — §§1–5]

[In §1, cite: Article 33(1) UK GDPR (as retained and amended by the Data Protection
Act 2018 and the UK GDPR)]

[In §2, note whether an EU GDPR simultaneous notification has been or will be filed
with a Member State DPA]
```

**[VERIFY]**: Confirm ICO's current online portal URL and whether ICO prefers portal
submission over letter for the breach size and type involved.

---

#### 6c. US State Attorney General Notification

**When to use**: Breach affects residents of one or more US states that require AG
(or other public authority) notification. Consult `legalcode-us-breach-notification-triage`
for the per-state applicability matrix, thresholds (e.g., >500 CA residents, >500 FL
residents, >1,000 NY residents [VERIFY per-state thresholds]), and deadlines.

**Format**: Most states accept a formal letter by email or portal. A minority have
specific AG form requirements. Verify the current submission method for each state
before dispatching.

**Note**: The AG letter is a separate document from the individual notice to data
subjects. Many states require the AG letter to include or attach a copy of the notice
being sent to individuals.

---

**TEMPLATE: US State AG Notification Letter (General)**

```
[ORGANIZATION LETTERHEAD]

[DATE]

[STATE] Attorney General
[AG MAILING ADDRESS]
[AG EMAIL / PORTAL] — [VERIFY current submission address at ag.[state].gov]

Re: Data Breach Notification — [ORGANIZATION NAME]
    Breach Notification Pursuant to [STATE STATUTE CITATION]

Dear Attorney General [NAME] / Office of the Attorney General:

Pursuant to [STATE] [Breach Notification Act / Security Breach Notification Law /
applicable statute] ([CITATION]), [ORGANIZATION_FULL_LEGAL_NAME] ("the Company")
hereby notifies the [STATE] Attorney General of a data security incident affecting
residents of [STATE].

1. ORGANIZATION CONTACT

Name: [AUTHORIZED_SIGNATORY_NAME]
Title: [TITLE]
Organization: [ORGANIZATION_FULL_LEGAL_NAME]
Address: [ADDRESS]
Phone: [PHONE]
Email: [EMAIL]

2. DESCRIPTION OF THE BREACH

On or about [DATE OF BREACH / DATE OF DISCOVERY], the Company discovered [plain-language
description of breach]. The breach occurred on approximately [DATE RANGE] and involved
[type of access: unauthorized access / disclosure / acquisition].

The breach resulted from: [Brief description of root cause if known — e.g., "a phishing
attack that compromised employee credentials" / "a vulnerability in a third-party vendor
system" / "physical loss of equipment containing encrypted data".]

[If investigation ongoing:] Our investigation is ongoing. The above description
represents our current understanding and may be updated as our investigation concludes.

3. INFORMATION INVOLVED

The categories of personal information affected include:
□ Full name
□ Social Security Number (SSN)
□ Driver's license / state ID number
□ Financial account number (checking, savings, credit card)
□ Medical / health information
□ Username and password / security questions
□ Biometric data
□ Geolocation data
□ Other: [specify]

4. AFFECTED [STATE] RESIDENTS

Estimated number of [STATE] residents affected: [N] / [TBC — full count pending
investigation completion]

5. NOTIFICATION TO AFFECTED RESIDENTS

We [are/will be] notifying affected [STATE] residents by [EMAIL / FIRST-CLASS MAIL /
SUBSTITUTE NOTICE — specify]. Individual notifications [began / will begin] on
[DATE]. [ATTACH: Copy of the individual notice being sent to residents, if required
by [STATE] law.]

6. REMEDIATION MEASURES

[Brief description of steps taken and proposed — consistent with §4 of the GDPR
template above, but simplified for general US AG audience]

7. CREDIT MONITORING / IDENTITY PROTECTION [if required or offered]

[STATE-SPECIFIC] The Company [is/is not] offering affected residents [N months] of
complimentary credit monitoring services through [SERVICE PROVIDER]. [Include only
if required by state law or offered voluntarily: CO, CT, DE, MA, PA, RI, NV require
credit monitoring for certain breach types [VERIFY current requirements].]

Sincerely,

[AUTHORIZED_SIGNATORY_NAME]
[TITLE]
[ORGANIZATION_FULL_LEGAL_NAME]
[DATE]

Enclosures:
□ Copy of individual consumer notice [if required]
□ [Other attachments as required by state law]
```

**State-Specific Adaptations** (verify current requirements):

| State          | AG Threshold       | Submission Method                                          | Special Requirements                                                    |
| -------------- | ------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| California     | >500 CA residents  | CA AG online portal or email to breach@doj.ca.gov [VERIFY] | Must include sample notice; electronic submission preferred             |
| New York       | >500 NY residents  | NY AG online portal [VERIFY]                               | Notice must include specific elements per SHIELD Act                    |
| Texas          | >250 TX residents  | TX AG portal (reports.oag.state.tx.us) [VERIFY]            | Two-track: 30d individual, 60d AG [VERIFY SB 768 status]                |
| Florida        | >500 FL residents  | FL AG online form [VERIFY]                                 | 30-day AG deadline                                                      |
| Illinois       | All residents      | IL AG by email [VERIFY]                                    | 45-day limit [VERIFY]                                                   |
| Massachusetts  | All residents      | MA AG and affected residents concurrently                  | 30-day limit; must include credit monitoring for financial/SSN breaches |
| [Other states] | [Verify threshold] | [Verify method]                                            | See legalcode-us-breach-notification-triage                             |

---

### Step 7: Draft Australian OAIC NDB Statement

**When to use**: Breach is an "eligible data breach" under Privacy Act 1988 Part IIIC
— a breach that is likely to result in serious harm to one or more individuals.

**Eligible Data Breach Assessment**:
Before drafting the NDB Statement, confirm the breach meets the "eligible data breach"
threshold:

1. There is unauthorized access to, or disclosure of, personal information held by
   the organization; OR loss of personal information held by the organization that is
   likely to result in unauthorized access or disclosure
2. The unauthorized access/disclosure/loss is likely to result in serious harm to one or
   more individuals
3. The organization was not able to prevent the likely risk of serious harm with remedial
   action

If the breach does not meet the eligible data breach threshold, notification to OAIC is
not required — but document the assessment.

**Assessment Timeline**: Organizations must complete their eligible data breach assessment
**within 30 days** of becoming aware of a suspected eligible data breach (Privacy Act
s. 26WH(2)).

**Format**: OAIC online NDB Notification Form at oaic.gov.au [VERIFY current URL].
For complex incidents, supplement the form with an attached narrative letter.

---

**TEMPLATE: OAIC NDB Statement (Form Field Guidance)**

```
OAIC NDB Notification Form — Field Completion Guide
[Submit via OAIC online portal at oaic.gov.au/privacy/notifiable-data-breaches]
[VERIFY current form URL and fields — OAIC updates its form periodically]

SECTION 1: ORGANIZATION DETAILS
Entity name: [ORGANIZATION_FULL_LEGAL_NAME]
ABN: [ABN — 11-digit Australian Business Number]
Contact person: [CONTACT_NAME]
Contact title: [TITLE]
Contact email: [EMAIL]
Contact phone: [PHONE]
Address: [REGISTERED_AUSTRALIAN_ADDRESS]

SECTION 2: ELIGIBLE DATA BREACH DETAILS

2.1 Type of breach:
□ Unauthorized access to personal information
□ Unauthorized disclosure of personal information
□ Loss of personal information (likely to result in unauthorized access/disclosure)

2.2 Date/approximate date of breach: [DATE] / [Date range: FROM–TO]
2.3 Date you became aware: [DATE]
2.4 Date eligible data breach assessment completed: [DATE]

2.5 Nature of the breach / circumstances:
[Plain-language narrative — e.g., "On [DATE], we identified unauthorized access to
our customer database. [DESCRIPTION OF HOW BREACH OCCURRED]. We completed our
eligible data breach assessment on [DATE] and determined that this breach is likely
to result in serious harm because [HARM ASSESSMENT]."]

SECTION 3: PERSONAL INFORMATION INVOLVED

3.1 Categories of personal information (check all that apply):
□ Name
□ Address
□ Date of birth
□ Phone / email
□ Financial information (account numbers, credit card, banking details)
□ Government ID (TFN, Medicare number, passport, driver's licence)
□ Health information [sensitive information under Privacy Act s. 6(1)]
□ Biometric information [sensitive]
□ Racial or ethnic origin [sensitive]
□ Religious beliefs [sensitive]
□ Sexual orientation [sensitive]
□ Criminal record [sensitive]
□ Other: [specify]

3.2 Number of individuals affected: [N] / [Estimated range: N–M] / [TBC]

SECTION 4: SERIOUS HARM ASSESSMENT

[Describe the harm that is likely to result, with reference to Privacy Act s. 26WG
factors:]

The likely serious harm assessment considers:
□ The kind(s) of personal information involved (sensitive vs. non-sensitive)
□ The number of individuals affected
□ The persons who may obtain the information
□ The nature of the harm (financial, physical, psychological, reputational)
□ Any other relevant matter

Assessment: [DESCRIBE HARM RISK — e.g., "The breach involves financial account details
of [N] individuals, creating a real risk of financial fraud. The OAIC NDB guidance
indicates that financial data breaches typically meet the serious harm threshold."]

SECTION 5: STEPS TAKEN

5.1 Steps already taken to address the breach:
[List containment, forensic, and remediation actions — consistent with §4 of GDPR
template above, adapted for Australian audience]

5.2 Steps proposed to address the breach:
[List planned remediation measures]

5.3 Steps to assist individuals at risk of serious harm:
□ Direct notification to affected individuals [METHOD / TIMELINE]
□ Guidance provided to affected individuals (e.g., monitor accounts, change passwords)
□ Credit monitoring or identity protection offered [PROVIDER / DURATION]
□ [Other steps]

SECTION 6: RECOMMENDATIONS FOR INDIVIDUALS AT RISK

[Required under Privacy Act s. 26WL(2)(d)] Provide specific, actionable steps:
□ Monitor your [bank accounts / credit card statements] for unauthorized activity
□ Contact your financial institution if you identify suspicious transactions
□ Consider placing a credit freeze with credit reporting agencies
□ Change passwords for any accounts where you used the same credentials
□ Be alert to phishing emails or calls purporting to be from [ORGANIZATION]
□ Contact [ORGANIZATION_CONTACT] with any questions
```

**Post-Notification**: Monitor OAIC website for any inquiry or follow-up. OAIC publishes
quarterly NDB statistics; significant breaches may be cited in OAIC reports.

---

### Step 8: Draft Canadian OPC / CAI Breach Report

**Federal (OPC — PIPEDA):**

**When to use**: Organization subject to PIPEDA suffers a breach of security safeguards
involving personal information under its control, and there is a real risk of significant
harm (RROSH) to individuals.

**RROSH Factors** (SOR/2018-64 s. 6): Sensitivity of the personal information;
probability that the personal information has been/will be misused; number of individuals
affected.

**OPC report content** (SOR/2018-64 s. 7 — mandatory elements):

```
PIPEDA Breach of Security Safeguards Report — OPC

To: Office of the Privacy Commissioner of Canada
30 Victoria Street, Gatineau, Quebec K1A 1H3
Email: info@priv.gc.ca [VERIFY current breach reporting address]

Organization: [NAME]
Contact: [NAME, TITLE, EMAIL, PHONE]

1. Date (or date range) when breach occurred: [DATE]
2. Date you became aware of the breach: [DATE]
3. General description of the circumstances of the breach:
   [Type of breach, systems affected, root cause if known]
4. Personal information involved (categories):
   [List categories]
5. Approximate number of affected individuals: [N] / [TBC]
6. Steps taken to reduce risk of harm: [List measures]
7. Notice to affected individuals: [Given / Planned / Not applicable]
   If given or planned, describe method and timeline: [DETAILS]
8. Why you are of the opinion there is a real risk of significant harm:
   [State RROSH factors: sensitivity, probability of misuse, scale]

Signed: [SIGNATORY_NAME], [TITLE]
Date: [DATE]
```

**Quebec (CAI — Law 25 Art. 3.5):**

**When to use**: Breach affects personal information of Quebec residents; confidentiality
incident involves identity theft risk, credit risk, or damage to reputation.

**Format**: CAI has an online reporting form at cai.gouv.qc.ca [VERIFY].

**Content requirements (Law 25 Art. 3.5)**:

- Description of the incident
- Date or timeframe of the incident
- Number of persons concerned (approximate)
- Nature of the personal information involved
- Brief description of measures taken to prevent repetition

**Timing**: Law 25 uses a practical 72-hour-equivalent approach for serious incidents
(incidents that present a risk of serious injury) — notify CAI as soon as possible
[VERIFY current CAI guidance for exact timing].

**[VERIFY]**: Quebec's Law 25 confidentiality incident requirements are subject to
ongoing CPVP (CAI) guidance updates. Verify current requirements before dispatching.

---

### Step 9: Draft Brazilian ANPD Incident Notification

**When to use**: Breach involves personal data of Brazilian data subjects where the
incident poses a relevant risk or significant damage to data subjects.

**ANPD triggering threshold** (LGPD Art. 48 + ANPD Resolution 15/2024):

- Personal data breach that may pose relevant risk or significant damage to data subjects
- "Relevant risk" factors: type and sensitivity of data; good faith or intention of the
  unauthorized party; economic or social vulnerability of affected data subjects; potential
  for replicating or combining data; data subject is a minor; volume of affected data

**Two-phase notification**:

1. **Initial Communication** (Comunicação Preliminar): within 3 business days of
   becoming aware of the incident [VERIFY — ANPD Res. 15/2024]
2. **Complementary Communication**: within 20 business days of the initial report,
   containing complete information

**Format**: ANPD online portal (gov.br/anpd) [VERIFY current form URL].

```
ANPD Incident Notification — Field Completion Guide
[Submit via ANPD portal — VERIFY current URL]
[VERIFY ANPD Res. 15/2024 is still current; check for 2026 updates]

PHASE 1: COMUNICAÇÃO PRELIMINAR (Initial — within 3 business days)

Organization / Controller:
Full legal name: [RAZÃO SOCIAL]
CNPJ: [CNPJ number]
Registered address: [ENDEREÇO]
DPO contact (Encarregado): [NOME, EMAIL, TELEFONE]

Incident description:
Date of occurrence (or range): [DATE]
Date of discovery: [DATE]
Type of incident: □ Unauthorized access □ Disclosure □ Elimination/loss □ Modification
Affected systems: [LIST]
Description: [Brief narrative in Portuguese if submitting in Brazil — English permitted
for international controllers [VERIFY whether ANPD requires Portuguese]]

Data involved (initial assessment):
Categories: [List personal data categories — e.g., "nome, CPF, dados bancários"]
Special categories: □ Health □ Biometric □ Children's data □ Racial/ethnic origin □ Other
Approximate number affected: [N] / [Estimate pending investigation]

Risk/damage assessment:
Is there relevant risk or significant damage? □ Yes □ Likely □ Under assessment
Risk factors identified: [List applicable factors from ANPD Res. 15/2024 Art. 4]

Preliminary measures taken:
[Brief description of containment actions]

PHASE 2: COMUNICAÇÃO COMPLEMENTAR (Complete — within 20 business days)

[All fields from Phase 1, plus:]
Forensic investigation outcome: [Summary]
Confirmed number of affected data subjects: [N]
Confirmed categories of personal data: [Detailed list]
Harm analysis: [Complete risk/damage assessment]
Measures taken (complete): [Full remediation description]
Measures proposed: [Forward-looking actions]
Individual notification plan: □ Notified □ Will notify by [DATE] □ Not applicable
Reasons if not notifying individuals: [EXPLANATION]
Regulatory authorities notified: [List other authorities notified concurrently]
Enclosures: [Forensic report, security incident timeline, other]

Signed (Encarregado / DPO): [NAME, DATE]
```

**[VERIFY]**: ANPD resolution requirements and portal are subject to change. Check
ANPD website (gov.br/anpd) for current guidance before submitting.

---

### Step 10: Draft Individual Data Subject Notice

**When required**: Draft the individual notice when:

- GDPR Art. 34 triggers (high risk to rights and freedoms)
- UK GDPR Art. 34 triggers (same standard)
- US state breach notification laws trigger (most states require individual notice —
  see `legalcode-us-breach-notification-triage`)
- Australian Privacy Act s. 26WL requires notification to affected individuals
- LGPD Art. 48(2) requires individual notification for serious impact
- Playbook specifies organizational policy of proactive individual notification

**Tone**: Plain language; no legal jargon; empathetic and clear. Avoid hedging language
that obscures what happened. Regulators and plaintiff lawyers scrutinize individual
notices for accurate disclosure.

---

**TEMPLATE: Individual Data Subject Notice (Multi-Regime)**

```
SUBJECT: Important Information About the Security of Your Personal Information

Dear [Customer Name / Valued User],

[ORGANIZATION_NAME] is writing to notify you of a data security incident that may
have affected your personal information.

WHAT HAPPENED

On [DATE], we discovered that [plain-language description of the incident].
[Example: "An unauthorized person accessed our customer database between [DATE FROM]
and [DATE TO]. We became aware of this on [DETECTION DATE] and immediately took steps
to secure our systems."]

WHAT INFORMATION WAS INVOLVED

The information that may have been accessed includes:
□ Your name
□ [Other categories — list only what is confirmed or likely for this individual's data]
□ [SSN / Tax file number / National ID — if involved]
□ [Financial account information — if involved]
□ [Health information — if involved]
□ [Other]

[If unsure of individual-level exposure:] "Based on our investigation, the following
types of information held in the affected system may have been accessed: [LIST].
We are continuing to investigate which specific individuals' information was exposed
and will update you if we learn more about your specific situation."

WHAT WE ARE DOING

We have taken the following steps to address this incident and protect your
information:
□ [Secured the affected systems and prevented further unauthorized access]
□ [Launched a forensic investigation with [FIRM NAME]]
□ [Notified law enforcement] [if applicable]
□ [Enhanced security monitoring across our systems]
□ [Notified the relevant data protection authority] [if applicable — do not commit to
  specific details unless confirmed]

WHAT YOU CAN DO

We recommend that you take the following steps to protect yourself:

□ Monitor your financial accounts and credit card statements for any unauthorized
  activity and report suspicious transactions to your financial institution immediately.
□ [If SSN or national ID involved:] Consider placing a fraud alert or credit freeze
  with the major credit reporting agencies. [US: Equifax, Experian, TransUnion;
  UK: Experian, Equifax, TransUnion; AU: Equifax, Experian, illion]
□ Change your password for your account with [ORGANIZATION] and for any other accounts
  where you use the same password.
□ Be alert to phishing emails, phone calls, or text messages claiming to be from
  [ORGANIZATION] or other organizations seeking personal information.
□ [If credit monitoring offered:] We are offering you [N months] of complimentary
  credit monitoring with [PROVIDER]. To enroll, please visit [URL] and use the
  enrollment code [CODE] by [EXPIRATION DATE].

---

[JURISDICTION-SPECIFIC RIGHTS SECTION — include only sections applicable to the
individual's jurisdiction; remove inapplicable sections]

<!-- EU / UK GDPR RIGHTS (include for EU and UK residents) -->

YOUR DATA PROTECTION RIGHTS (EU and UK residents)

Under the General Data Protection Regulation (GDPR) / UK GDPR, you have the following
rights regarding your personal information:
• Right of access (Art. 15): You may request a copy of the personal information we
  hold about you.
• Right to erasure (Art. 17): You may request deletion of your personal information
  in certain circumstances.
• Right to restriction (Art. 18): You may request that we restrict processing of your
  personal information.
• Right to object (Art. 21): You may object to certain types of processing.
• Right to lodge a complaint: You have the right to lodge a complaint with the
  supervisory authority in your country of residence. A list of EU supervisory
  authorities is available at edpb.europa.eu. The UK supervisory authority is the
  Information Commissioner's Office (ico.org.uk).

<!-- US STATE RIGHTS (include for US residents; adapt per state) -->

YOUR RIGHTS (US residents)

[California:] California law requires us to notify you of this breach. You have the
right to request a copy of any personal information we have about you, to correct
inaccuracies, and to delete your personal information in certain circumstances.
You may also submit a complaint to the California Privacy Protection Agency
(cppa.ca.gov) or the California Attorney General (oag.ca.gov). [Adapt for other states.]

<!-- AUSTRALIA RIGHTS (include for Australian residents) -->

YOUR PRIVACY RIGHTS (Australian residents)

Under the Privacy Act 1988, you have the right to request access to your personal
information and to request corrections if it is inaccurate. You may also lodge a
complaint with the Office of the Australian Information Commissioner (oaic.gov.au).

<!-- BRAZIL RIGHTS (include for Brazilian residents) -->

SEUS DIREITOS (Residentes no Brasil)

Nos termos da Lei Geral de Proteção de Dados (LGPD), você tem o direito de acessar
os seus dados pessoais, corrigir dados incompletos ou desatualizados, e solicitar a
exclusão dos seus dados em determinadas circunstâncias. Você também pode apresentar
uma reclamação à Autoridade Nacional de Proteção de Dados (ANPD) em gov.br/anpd.

<!-- CANADA RIGHTS (include for Canadian residents) -->

YOUR PRIVACY RIGHTS (Canadian residents)

Under Canada's privacy laws, you have the right to access your personal information and
to request corrections. You may also contact the Office of the Privacy Commissioner of
Canada (priv.gc.ca) or, if you are a Quebec resident, the Commission d'accès à
l'information (cai.gouv.qc.ca) to file a complaint.

---

CONTACT US

If you have questions about this notice or about how we protect your personal information,
please contact us:

[DPO_NAME / PRIVACY TEAM NAME]
[ORGANIZATION_NAME]
Email: [PRIVACY_EMAIL]
Phone: [PRIVACY_PHONE] (available [HOURS, TIMEZONE])
Address: [MAILING_ADDRESS]

We sincerely apologize for this incident and for any inconvenience or concern it may
cause you. Protecting your personal information is a responsibility we take seriously.

Sincerely,

[DPO_NAME / CEO / AUTHORIZED_SIGNATORY]
[TITLE]
[ORGANIZATION_NAME]
[DATE]

[OPTIONAL: Reference / Case Number for your records: [INCIDENT_REF]]
```

---

### Step 11: Quality Assurance and Confidence Scoring

Run these quality checks before delivering the notification package. Apply each gate
to every notification document produced.

#### Citation Quality Gates

Run silently before delivering any output. If any gate fails, revise before delivering.

| Gate                | Rule                                                                                                                  | Fail Action                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Source Gate**     | Every legal obligation cited references a specific statutory provision, article, or regulation                        | Add citation or mark `[UNVERIFIED]`       |
| **Format Gate**     | Notification document uses the correct format for the target regulator (letter vs. online form vs. structured report) | Flag format mismatch; note correct format |
| **Currency Gate**   | Every cited provision checked for recent amendments or updated regulator guidance                                     | Flag `[CHECK CURRENCY]`                   |
| **Domain Gate**     | Notification content stays within the legal regime's scope — no bleed from one regime into another                    | Remove or flag jurisdictional bleed       |
| **Confidence Gate** | Uncertainty in legal interpretation is explicitly stated, not hidden in confident language                            | Add confidence qualifier                  |

#### Regulatory Compliance Self-Interrogation

For any notification document section rated PROBABLE or below:

**Pass 1 — Legal Compliance Chain**: Does this section's content directly satisfy the
specific statutory requirement? Would the regulator, reviewing the submission, be able
to identify the required element as present?

**Pass 2 — Completeness**: Are all mandatory sub-elements of this section present?
(E.g., for GDPR Art. 33(3)(a): nature of breach + categories of data subjects +
approximate number of data subjects + approximate number of records — all four?)

**Pass 3 — Challenge**: What is the strongest argument that this section is deficient?
What would a regulator's first follow-up question be? Have we proactively addressed it?

#### Confidence Scoring per Notification Section

| Level        | Range     | Meaning                                                                      | Action                                               |
| ------------ | --------- | ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Definite** | 0.95–1.0  | Section directly satisfies statutory requirement per settled guidance        | Deliver with confidence                              |
| **High**     | 0.80–0.94 | Section meets requirement with minor interpretive question                   | Deliver; note caveat                                 |
| **Probable** | 0.60–0.79 | Section likely meets requirement; some regulatory interpretation uncertainty | Flag for legal review before dispatch                |
| **Possible** | 0.40–0.59 | Uncertain; reasonable regulators could read requirement differently          | Mandatory legal review; present both interpretations |
| **Unlikely** | 0.0–0.39  | Weak basis; section unlikely to satisfy requirement as drafted               | Do not dispatch; revise section                      |

#### Document Element Completeness Check

For each notification document, verify:

```
GDPR Art. 33 Notification Completeness Checklist:
□ Art. 33(3)(a): Nature of breach — present and complete
□ Art. 33(3)(a): Categories of data subjects — present
□ Art. 33(3)(a): Approx. number of data subjects — present (or [TBC] with timeline)
□ Art. 33(3)(a): Categories of personal data records — present
□ Art. 33(3)(a): Approx. number of personal data records — present (or [TBC])
□ Art. 33(3)(b): DPO / contact point — complete (name, email, phone)
□ Art. 33(3)(c): Likely consequences — substantive (not boilerplate)
□ Art. 33(3)(d): Measures taken — specific actions listed with dates
□ Art. 33(3)(d): Measures proposed — included
□ If late: Reasons for delay — present
□ If phased: Supplement timeline committed

ICO / UK GDPR Completeness Checklist:
□ [Same as GDPR Art. 33] plus:
□ ICO online portal used (preferred) or formal letter format
□ [VERIFY] ICO-specific form fields if using portal

US State AG Completeness Checklist (per state):
□ AG contact verified for this state
□ Notification threshold confirmed
□ Required content elements per state statute present
□ Individual notice copy attached (if required by state)
□ Credit monitoring details included (if required by state)

OAIC NDB Statement Completeness:
□ Eligible data breach threshold analysis completed and documented
□ ABN included
□ All OAIC form sections completed
□ Recommendations for affected individuals specific and actionable

OPC / CAI Completeness:
□ RROSH factors addressed (federal OPC)
□ CAI form completed (Quebec, if applicable)
□ [VERIFY] Current OPC/CAI guidance applied

ANPD Completeness:
□ Phase 1 submitted within 3 business days
□ CNPJ included
□ Encarregado (DPO) contact included
□ Phase 2 scheduled within 20 business days
□ [VERIFY] ANPD portal current format used
```

---

### Step 12: Assemble and Deliver the Notification Package

Compile all draft documents into a **Breach Regulatory Notification Package**:

````markdown
# Breach Regulatory Notification Package

## [ORGANIZATION NAME] | Incident ID: [ID] | Generated: [DATE]

---

## EXECUTIVE SUMMARY

**Incident**: [One-sentence description]
**Awareness date**: [DATE TIME TZ]
**Breach confirmed**: [Yes / Under assessment]
**Data categories involved**: [List]
**Estimated affected individuals**: [N]
**Jurisdictions triggered**: [List]

**Priority 1 (72h) deadlines**:

- EU GDPR Art. 33 → [LEAD DPA]: Due [DATE TIME]
- UK GDPR → ICO: Due [DATE TIME]
- Brazil ANPD Phase 1: Due [DATE TIME]

**Priority 2 deadlines**:

- [States]: [Deadlines]
- Australia OAIC: Assessment due [DATE]

**Status**: All documents in DRAFT — legal review required before dispatch.

---

## NOTIFICATION DOCUMENTS

### Document 1: GDPR Art. 33 Notification — [LEAD DPA]

[Full draft from Step 6a]
Completeness: ■■■■□ (4/5 mandatory elements complete; DPO details pending)
Confidence: HIGH (0.85)

### Document 2: UK GDPR Notification — ICO

[Full draft from Step 6b]
Completeness: ■■■■□
Confidence: HIGH (0.85)

### Document 3: [STATE 1] AG Letter

[Full draft from Step 6c]
Completeness: ■■■■■
Confidence: PROBABLE (0.75) — [VERIFY] current AG submission address

### Document 4: OAIC NDB Statement

[Full draft from Step 7]
Completeness: ■■■■□
Confidence: HIGH (0.82)

### Document 5: OPC Breach Report

[Full draft from Step 8]
Completeness: ■■■■□
Confidence: PROBABLE (0.72)

### Document 6: ANPD Incident Notification (Phase 1)

[Full draft from Step 9]
Completeness: ■■■■□
Confidence: PROBABLE (0.70) — [VERIFY] ANPD portal current format

### Document 7: Individual Data Subject Notice

[Full draft from Step 10]
Completeness: ■■■■■
Confidence: HIGH (0.88)

---

## DISPATCH CHECKLIST AND TIMELINE

| Notification      | Recipient            | Deadline    | Method            | Assigned To | Status    |
| ----------------- | -------------------- | ----------- | ----------------- | ----------- | --------- |
| GDPR Art. 33      | [LEAD DPA]           | [DATE TIME] | [Letter / Portal] | [NAME]      | □ Pending |
| UK GDPR           | ICO                  | [DATE TIME] | ICO portal        | [NAME]      | □ Pending |
| [STATE] AG        | [STATE AG]           | [DATE]      | [Email / Portal]  | [NAME]      | □ Pending |
| OAIC NDB          | OAIC                 | [DATE]      | OAIC portal       | [NAME]      | □ Pending |
| OPC Report        | OPC                  | [DATE]      | [Email]           | [NAME]      | □ Pending |
| ANPD Phase 1      | ANPD                 | [DATE TIME] | ANPD portal       | [NAME]      | □ Pending |
| Individual Notice | Affected individuals | [DATE]      | [Email / Mail]    | [NAME]      | □ Pending |
| ANPD Phase 2      | ANPD                 | [DATE]      | ANPD portal       | [NAME]      | □ Pending |

---

## POST-DISPATCH MONITORING

**Supplementary notification triggers**:

- If affected individual count increases by >10% from initial estimate: prepare
  supplementary GDPR Art. 33(4) notification
- If forensic investigation reveals additional categories of data: update all
  notifications with supplementary submission
- If regulator makes inquiry: respond within timeframe indicated by regulator (typically
  5–10 business days)

**Regulator inquiry response**: If any regulator issues a formal inquiry or requests
additional information, engage legal counsel and use the Glass Box audit trail below
to reconstruct the notification decision record.

**Individual notification monitoring**: Track whether affected individuals respond with
complaints, DSARs, or requests for compensation. Route to `legalcode-dsar-workflow-builder`.

---

## OPEN ITEMS AND [VERIFY] REGISTER

| Item                                         | Section  | Action Required                                      | Owner  |
| -------------------------------------------- | -------- | ---------------------------------------------------- | ------ |
| [VERIFY] Lead DPA determination              | Doc 1 §1 | Confirm EU main establishment with legal counsel     | [NAME] |
| [VERIFY] ICO portal URL                      | Doc 2    | Check ico.org.uk for current breach reporting portal | [NAME] |
| [VERIFY] [STATE] AG current submission email | Doc 3    | Check ag.[state].gov                                 | [NAME] |
| [VERIFY] ANPD portal format current          | Doc 6    | Check gov.br/anpd for 2026 updates                   | [NAME] |
| [TBC] Confirmed affected individual count    | All      | Update all documents when forensic count confirmed   | [NAME] |

---

## GLASS BOX AUDIT TRAIL

```yaml
glass_box:
  skill_name: "legalcode-breach-regulatory-notification-drafter"
  mode: "Notification drafting"
  topic: "Regulatory data breach notification — multi-regime"
  incident_id: "[INTERNAL_INCIDENT_ID]"
  jurisdiction: "EU GDPR / UK GDPR / US / Australia / Canada / Brazil"
  awareness_date: "[DATE TIME TZ]"
  draft_generated: "[DATE TIME TZ]"
  drafter: "AI-assisted — requires legal review before dispatch"
  documents_produced:
    - "GDPR Art. 33 notification letter"
    - "UK GDPR / ICO notification"
    - "US State AG letters: [STATES]"
    - "OAIC NDB Statement"
    - "OPC breach report"
    - "ANPD incident notification (Phase 1)"
    - "Individual data subject notice"
  per_regulator_citation_status:
    eu_gdpr_art33: "VERIFIED — GDPR Regulation (EU) 2016/679; EDPB Guidelines 9/2022"
    uk_gdpr_art33: "VERIFIED — UK GDPR (retained); DUA Act 2025 [CHECK CURRENCY for amendments]"
    us_state_ag: "[VERIFY] — State-specific statutory citations; confirm current AG submission method"
    australia_oaic: "VERIFIED — Privacy Act 1988 Part IIIC; OAIC NDB guidance [CHECK CURRENCY]"
    canada_opc: "VERIFIED — PIPEDA + SOR/2018-64; [VERIFY] current OPC guidance"
    canada_cai: "[VERIFY] — Quebec Law 25 Art. 3.5; [VERIFY] current CAI guidance"
    brazil_anpd: "[VERIFY] — LGPD Art. 48; ANPD Res. 15/2024 [CHECK CURRENCY for 2026 updates]"
  phased_notification: "[Yes / No]"
  cross_regulator_conflicts_identified: "[Describe any / None]"
  legalcode_mcp: "Not connected — mark all statutory citations [VERIFY] per above"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[N VERIFIED] / [N VERIFY]"
  confidence: "PROBABLE — requires legal review before dispatch"
  escalation_status: "[C-suite review required / Legal review required / Ready for dispatch]"
  limitations:
    - "AI-generated draft only; not reviewed by qualified legal counsel"
    - "Regulator portal formats and submission methods change — verify before use"
    - "Approximate affected individual count pending forensic confirmation"
    - "ANPD and CAI guidance subject to recent amendments — verify currency"
  reviewer: "Requires qualified legal counsel review before dispatch to any regulator"
```
````

---

## PROVENANCE

**Skill**: legalcode-breach-regulatory-notification-drafter v1.0
**Generated**: [DATE]
**Legal research basis**: GDPR Regulation (EU) 2016/679 Art. 33–34; EDPB Guidelines
9/2022 on personal data breach notification; UK GDPR (as retained by DPA 2018); ICO
breach reporting guidance; Privacy Act 1988 (Cth) Part IIIC (AU); PIPEDA + Breach of
Security Safeguards Regulations SOR/2018-64 (CA); Quebec Law 25 (An Act to modernize
legislative provisions as regards the protection of personal information); LGPD Law
13,709/2018 Art. 48 (BR); ANPD Resolution CD/ANPD No. 15/2024.
**Upstream skills**: legalcode-breach-severity-assessment (harm triage);
legalcode-us-breach-notification-triage (US state deadline matrix).

```

---

## Regulator Reference Directory

Verify all contacts and portals before submitting — these change without notice.

### EU Supervisory Authorities (Lead DPA Candidates)

| Country | DPA | Submission Method | Notes |
|---------|-----|------------------|-------|
| Ireland | Data Protection Commission (DPC) | breach@dataprotection.ie / dpc.ie portal | Leads for Google, Meta, Apple, etc. |
| Germany | Federal (BfDI) or State DPA | Online form — varies by state | Most large data brokers |
| France | CNIL | cnil.fr online portal | French-established controllers |
| Netherlands | AP | autoriteitpersoonsgegevens.nl | Netherlands establishments |
| Spain | AEPD | aepd.es online breach notification tool | Spain establishments |
| Italy | Garante | garante.it | Italy establishments |
| Sweden | IMY | imy.se | Sweden establishments |
| Belgium | APD/GBA | apd-gba.be | Belgium establishments |
| [Other EU states] | [See edpb.europa.eu for full list] | [Verify] | |

[VERIFY] All DPA contact details and portal URLs. Many DPAs update their online systems
annually.

### UK

| Authority | Contact | Method |
|-----------|---------|--------|
| ICO | ico.org.uk/for-organisations/report-a-breach | Online portal (preferred); casework@ico.org.uk for complex incidents [VERIFY] |

### United States (Federal Sector Overlays)

| Regulator | Trigger | Submission | Notes |
|-----------|---------|-----------|-------|
| HHS (HIPAA BNR) | Breach of PHI | hhs.gov/hipaa breach portal | 60 days from discovery (>500 individuals) |
| FTC (GLBA) | Financial institution breach | FTC online form | 30-day post-notification reporting [VERIFY current] |
| SEC | Publicly traded company | Form 8-K Item 1.05 | 4 business days from materiality determination |
| FCC | Telecom carrier breach | FCC reporting portal | 7 business days (agency) + 30 days (customer) [VERIFY] |

### Australia

| Authority | Contact | Method |
|-----------|---------|--------|
| OAIC | oaic.gov.au/privacy/notifiable-data-breaches | Online NDB form [VERIFY current URL] |

### Canada

| Authority | Contact | Method |
|-----------|---------|--------|
| OPC (Federal) | priv.gc.ca | info@priv.gc.ca; written report [VERIFY] |
| CAI (Quebec) | cai.gouv.qc.ca | Online form [VERIFY] |
| OIPC BC | oipc.bc.ca | Written report [VERIFY] |
| OIPC Alberta | oipc.ab.ca | Written report [VERIFY] |

### Brazil

| Authority | Contact | Method |
|-----------|---------|--------|
| ANPD | gov.br/anpd | Online portal; peticionamento@anpd.gov.br [VERIFY] |

---

## Anti-Patterns for Regulatory Notification Drafting

What NOT to do when preparing and submitting regulatory breach notifications:

1. **Waiting for a complete forensic investigation before notifying** — GDPR Art. 33 and
   UK GDPR require notification within 72 hours of awareness, not upon completion of
   forensic analysis. Phased notification under Art. 33(4) exists precisely for this
   reason. Waiting is a common and heavily penalized mistake.

2. **Using GDPR language verbatim in US AG letters** — Regulatory audiences differ.
   A EU DPA expects GDPR citations; a US AG expects plain English and state statute
   citations. Cross-contamination of legal frameworks triggers follow-up questions and
   undermines credibility.

3. **Omitting the DPO contact details from the GDPR Art. 33 notification** — GDPR
   Art. 33(3)(b) mandates the DPO or equivalent contact point. Omitting it is a
   technically deficient notification that regulators flag immediately.

4. **Describing consequences as "none known" without substantive harm assessment** —
   Regulators expect a genuine assessment of likely consequences under Art. 33(3)(c).
   "None known at this time" is not a consequence assessment — it is an evasion. If harm
   risk is genuinely low, explain why (e.g., data was encrypted at rest; no evidence of
   exfiltration; limited sensitivity).

5. **Providing estimated counts as exact counts** — If the forensic investigation is
   ongoing, state an estimated range with an explicit caveat. Overstating certainty in
   initial notifications creates inconsistency with later supplementary notifications.

6. **Failing to submit a phased supplement when facts change** — If the initial
   notification contained estimates or [TBC] items, a supplementary notification under
   Art. 33(4) is legally required when confirmed facts become available. Many organizations
   file the initial notification and never follow up.

7. **Notifying the lead DPA only and assuming cross-border coverage** — GDPR one-stop-shop
   applies for EU cross-border processing, but UK notification is always legally distinct.
   US, Australian, Canadian, and Brazilian notifications are completely independent legal
   obligations.

8. **Copying the DPA notification directly into the individual data subject notice** —
   DPA notifications contain technical and legal language appropriate for regulators.
   Individual notices must be plain-language, empathetic, and actionable. The audiences
   and required tones are completely different.

9. **Including other data subjects' personal information in the individual notice** —
   The individual notice to a data subject must contain only information relevant to that
   individual. Disclosing other affected individuals' details in a notice is itself a
   secondary breach.

10. **Missing US state AG notification thresholds** — Most US state breach notification
    laws apply only when the breach affects a minimum number of state residents (e.g.,
    >500 for California, >500 for Florida [VERIFY thresholds]). Failing to identify
    whether the threshold is met — or submitting notifications to states where the
    threshold is not reached — creates unnecessary regulator attention. Use
    `legalcode-us-breach-notification-triage` for per-state threshold analysis.

11. **Assuming PIPEDA covers all Canadian privacy obligations** — Quebec's Law 25
    creates distinct confidentiality incident reporting obligations to the CAI for
    incidents affecting Quebec residents. PIPEDA and Quebec Law 25 notifications are
    legally independent. Similarly, BC and Alberta PIPA create provincial obligations
    for organizations subject to provincial law.

12. **Failing to track the ANPD's two-phase timeline** — LGPD Art. 48 + ANPD Resolution
    15/2024 requires an initial (Phase 1) communication within 3 business days and a
    complementary (Phase 2) notification within 20 business days. Missing the Phase 2
    deadline after submitting Phase 1 is a common compliance failure.

13. **Submitting notifications to outdated regulator addresses** — Regulatory portals,
    email addresses, and submission methods change. A notification submitted to an
    obsolete portal or email address may not be received or processed in time to meet the
    applicable deadline. Always verify current submission details immediately before
    dispatching.

14. **Offering credit monitoring in states that do not require it without confirming scope**
    — Some US states specifically enumerate which breach types require credit monitoring
    offers (e.g., financial account data, SSN). Offering credit monitoring when not
    required is not harmful, but failing to offer it when required is a violation. Verify
    per-state requirements with `legalcode-us-breach-notification-triage`.

15. **Describing "measures taken" in generalities** — "We have taken steps to secure our
    systems" is not a measure. Regulators expect specific, dated actions: "On [DATE], we
    revoked all compromised credentials; on [DATE], we patched the vulnerability; on
    [DATE], we engaged [FORENSIC FIRM] for investigation." Vague measures invite follow-up.

16. **Using a single notification letter for all jurisdictions** — A combined EU/UK/US/AU
    letter is never appropriate. Each regulator expects a notification addressed to it
    specifically, referencing the applicable legal framework, and formatted for its
    submission process.

17. **Not retaining a copy of every notification dispatched** — Organizations must be
    able to demonstrate compliance. Retain: the exact document submitted, the submission
    timestamp, the method of submission, and any confirmation receipt from the regulator.
    Document retention for breach notifications: minimum 3 years recommended; longer if
    litigation is foreseeable.

18. **Conflating processor notification obligations with controller notification obligations**
    — A processor that suffers a breach must notify the controller without undue delay
    (GDPR Art. 33(2)). The controller then notifies the DPA. Processors do not notify
    DPAs directly (unless they are also acting as a controller for some processing).

19. **Omitting the "measures proposed" element when only "measures taken" are described**
    — GDPR Art. 33(3)(d) covers both: "measures taken or proposed to be taken." Regulators
    expect forward-looking remediation commitments, not just a retrospective account.

20. **Failing to coordinate the timeline between individual notice and regulatory notice**
    — In most jurisdictions, the individual notice and regulatory notice should be
    coordinated: notify the regulator first (or simultaneously) and notify individuals
    promptly thereafter. Dispatching the individual notice before regulatory notification
    — without deliberate coordination — can create a record inconsistency.

---

## Writing Standards

Apply these standards to every notification document before delivery:

1. **Factual precision over hedging** — Write what is known. For unknown items, state
   "TBC" with a timeline. Do not use vague language ("approximately" when you have a
   number; "may have been" when access is confirmed).

2. **Plain language for individual notices** — Individual notices should be readable by
   a general audience. Avoid legal terms (no "tortious conduct," "de minimis risk,"
   "personal data per GDPR Art. 4(1)"). Use "your personal information" not "personal
   data."

3. **Formal language for regulatory letters** — DPA and AG notifications are formal
   legal communications. Use complete sentences, formal salutations, and precise legal
   citations.

4. **Active voice** — "We discovered unauthorized access" not "Unauthorized access was
   discovered." "We have notified affected individuals" not "Individuals have been notified."

5. **Date and time format consistency** — Use ISO 8601 or local convention per jurisdiction:
   - EU/UK: DD/MM/YYYY HH:MM UTC or local timezone with TZ designator
   - US: MM/DD/YYYY or spelled-out month (e.g., March 1, 2026)
   - Australia/Canada/Brazil: DD/MM/YYYY or local convention per audience

6. **No legal conclusions in individual notices** — The individual notice should not
   contain statements like "We are legally required to notify you because your data presents
   a high risk under GDPR Art. 34." Simply state the facts. Legal characterizations are
   for the DPA notification.

7. **Consistency across documents** — Facts, dates, affected counts, and data categories
   must be identical across all notifications dispatched for the same incident. Any
   inconsistency will be identified by regulators and will trigger follow-up inquiries.

8. **Legal review gate** — Every notification document must pass legal review before
   dispatch. The skill produces drafts; final dispatch authority rests with qualified
   legal counsel. Include a clear "DRAFT — NOT FOR DISPATCH WITHOUT LEGAL REVIEW" header
   on all documents until legal review is complete.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- Search for current GDPR Art. 33 text, EDPB Guidelines 9/2022 (latest version), and
  national DPA guidance for the lead DPA country
- Search for current ICO breach reporting guidance (UK)
- Search for current OAIC NDB guidance and form (AU)
- Search for current OPC and CAI breach reporting guidance (CA)
- Search for ANPD Resolution 15/2024 and any subsequent amendments (BR)
- Search for per-state breach notification statutes if not using
  legalcode-us-breach-notification-triage
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp (current configuration):**
- Proceed with drafts using statutory requirements documented in this skill
- Mark all statutory citations and regulatory contact details `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Intensify the [VERIFY] register in the final package — legal review is essential
- The drafts will be structurally and legally complete but require currency verification
  before dispatch

---

## Localization Notes

### EU: One-Stop-Shop and Multi-DPA Scenarios

For EU incidents involving cross-border processing, determine the lead DPA carefully:
- Non-EEA controllers without EU representative must notify each relevant national DPA
  separately — the one-stop-shop mechanism does not apply
- Where the controller has EU representative but no EU main establishment, notify the
  DPA of the Member State where the representative is established
- [JURISDICTION-SPECIFIC] Some national DPAs (e.g., the CNIL) have published country-specific
  breach reporting guidance in addition to the EDPB guidelines — consult local guidance
  before finalizing the notification

### US: Federal vs. State Coordination

Federal sector-specific breach reporting obligations (HIPAA, GLBA, SEC, FCC) may apply
alongside or instead of state breach notification laws. Federal obligations have their own
timelines, content requirements, and submission portals. Coordinate with
`legalcode-us-breach-notification-triage` for the full US notification matrix.

### Australia: Health Records Act

Breaches involving My Health Records are subject to additional notification requirements
under the My Health Records Act 2012 — notify the Australian Digital Health Agency in
addition to the OAIC NDB report. [JURISDICTION-SPECIFIC] [VERIFY current ADHA notification
process]

### Canada: Provincial vs. Federal Coordination

PIPEDA applies to private-sector organizations in provinces without substantially similar
privacy legislation (currently most provinces except BC, Alberta, and Quebec for some
sectors). In those provinces, the relevant provincial privacy commissioner receives the
notification. Law 25 (Quebec) creates a distinct obligation regardless of PIPEDA
applicability for organizations processing Quebec residents' personal information.

### Brazil: Portuguese Language Requirement

ANPD communications are conducted in Portuguese. The ANPD online portal is in Portuguese.
Ensure that the Phase 1 and Phase 2 notifications are submitted in Portuguese unless the
ANPD portal explicitly accepts English submissions for international controllers. [VERIFY]

---

## Provenance

**Skill**: legalcode-breach-regulatory-notification-drafter
**Created**: 2026-03-01
**Category**: general/compliance
**Type**: Legalcode original synthesis

**Legal research basis**:
- GDPR Regulation (EU) 2016/679 Arts. 33–34; EDPB Guidelines 9/2022 (v2.0, April 2023)
  on personal data breach notification; Art. 29 Working Party WP250rev.01 (superseded but
  referenced for historical guidance)
- UK GDPR (as retained by Data Protection Act 2018 and UK-GDPR SI 2019/419); ICO breach
  reporting guidance; Data (Use and Access) Act 2025 [CHECK CURRENCY for commencement]
- US state breach notification laws (50 states + DC + territories); HIPAA Breach
  Notification Rule (45 CFR §§ 164.400–414); GLBA Safeguards Rule (16 CFR Part 314);
  SEC cybersecurity disclosure rules (Form 8-K Item 1.05); FCC telecom breach rules
  (47 CFR Part 64)
- Privacy Act 1988 (Cth) Part IIIC; OAIC NDB guidance and statistics reports
- PIPEDA (Personal Information Protection and Electronic Documents Act) + Breach of
  Security Safeguards Regulations SOR/2018-64; Quebec Law 25 (Act to modernize
  legislative provisions as regards the protection of personal information)
- LGPD (Lei Geral de Proteção de Dados Pessoais) Law 13,709/2018 Art. 48; ANPD
  Resolution CD/ANPD No. 15/2024 (incident communication procedures)

**Structural patterns adapted from**:
- `legalcode-contract-review` — gold standard QA frameworks (Citation Quality Gates,
  Self-Interrogation, Confidence Scoring, Glass Box audit trail, Writing Standards,
  Anti-patterns structure)
- `legalcode-breach-severity-assessment` — multi-jurisdiction baseline matrix, clock
  normalization, notification duty register, finding-level specification
- `legalcode-us-breach-notification-triage` — US multi-state framework, federal overlay
  structure, per-state variation handling
- `legalcode-dsar-workflow-builder` — multi-regime parallel workflow design

**Research methodology**: 2-agent pipeline — Agent 1 (structural analysis of reference
skills: legalcode-contract-review, legalcode-breach-severity-assessment,
legalcode-us-breach-notification-triage, legalcode-dsar-workflow-builder; element map
for new skill; workflow design recommendation; output template recommendation;
classification system) + Agent 2 (deep legal research: GDPR Art. 33/34 with EDPB
Guidelines 9/2022; UK ICO breach reporting; US state AG notification requirements per
key states; Australian OAIC NDB scheme; Canadian OPC/SOR/2018-64 + Quebec Law 25;
Brazilian ANPD Resolution 15/2024; cross-regime common elements; drafting best
practices; anti-patterns).
```
