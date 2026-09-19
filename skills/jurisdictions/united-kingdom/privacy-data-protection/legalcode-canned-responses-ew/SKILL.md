---
name: legalcode-canned-responses-ew
description: Generate, manage, and customise templated responses for routine legal inquiries under the
  laws of England and Wales -- data subject access requests (DSARs) under UK GDPR and DPA 2018, litigation
  holds and document preservation (CPR Part 31 / PD 31B), privacy inquiries (PECR 2003, Age-Appropriate
  Design Code), vendor compliance questions (Modern Slavery Act 2015, Cyber Essentials), NDA requests
  (English law governing law, simple contract execution), legal process (witness summons CPR Part 34,
  Norwich Pharmacal orders, third-party disclosure CPR Part 31.17), and insurance notifications (Insurance
  Act 2015, Enterprise Act 2016). Use when responding to routine legal questions under English law, managing
  response template libraries for UK operations, creating new templates, or identifying when a matter
  requires qualified solicitor review.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generate, manage, and customise templated responses for routine legal inquiries under the laws of England and Wales -- data subject access requests (DSARs) under UK GDPR and DPA 2018, litigation holds and document preservation (CPR Part 31 / PD 31B), privacy inquiries (PECR 2003, Age-Appropriate Design Code), vendor compliance questions (Modern Slavery Act 2015, Cyber Essentials), NDA requests (English law governing law, simple contract execution), legal process (witness summons CPR Part 34, Norwich Pharmacal orders, third-party disclosure CPR Part 31.17), and insurance notifications (Insurance Act 2015, Enterprise Act 2016). Identifies when a situation requires individualised solicitor attention rather than a templated response. Includes escalation trigger detection, quality frameworks, and Glass Box audit trails. Use when responding to routine legal questions under English law, managing response template libraries for UK operations, creating new templates, or identifying when a matter requires qualified solicitor review. Produces structured, audit-ready responses with full regulatory citation.


# Legalcode Canned Responses -- England & Wales

> **Disclaimer**: This skill provides a framework for AI-assisted legal response
> generation under the laws of England and Wales. It does not constitute legal advice.
> All templated responses should be reviewed by a qualified solicitor admitted in England
> and Wales before sending, especially for regulated communications. Laws change; verify
> current applicability before relying on any provision described here. Statutory and
> regulatory references cited from memory carry hallucination risk -- verify against
> authoritative sources (legislation.gov.uk, ICO guidance, CPR online) before relying on
> them.

## Purpose and Scope

This skill helps in-house legal teams operating under the laws of England and Wales
manage, customise, and generate templated responses for common legal inquiries. It
identifies when a situation should NOT use a templated response and instead requires
individualised solicitor attention.

**Covers:**

- Template generation for 7 core response categories under English law
- Escalation trigger detection (universal and category-specific) for England and Wales
- Template creation, lifecycle management, and retirement workflows
- Customisation guidelines for tone, jurisdiction-specific terminology, and audience
- Quality assurance frameworks with Glass Box audit trails
- Variable placeholder management and validation
- Full UK regulatory citation (UK GDPR, DPA 2018, PECR 2003, CPR, Insurance Act 2015)

**Does not:**

- Provide legal advice or final legal opinions
- Replace solicitor review for regulated or high-stakes communications
- Generate responses for novel or unprecedented situations
- Handle matters involving potential litigation without escalation
- Apply to matters governed by Scots law, Northern Ireland law, or any non-English
  jurisdiction (use the jurisdiction-agnostic `legalcode-canned-responses` for those)
- Operate as a document management system (integrates with, does not replace)

**Related skills:**

- `legalcode-canned-responses` -- jurisdiction-agnostic base skill
- `legalcode-contract-review` -- for contract clause analysis
- `legalcode-nda-triage-ew` -- for NDA screening under English law
- `legalcode-nda-triage` -- for jurisdiction-agnostic NDA triage

---

## Governing Law: England and Wales

This skill applies the laws of England and Wales exclusively. All statutory references
are to laws of England and Wales unless otherwise stated. All procedural references are
to the Civil Procedure Rules (CPR) and Practice Directions applicable in the courts of
England and Wales.

**Key regulatory framework:**

- **Data protection**: UK General Data Protection Regulation (UK GDPR), Data Protection
  Act 2018 (DPA 2018), Privacy and Electronic Communications Regulations 2003 (PECR
  2003), Age-Appropriate Design Code (Children's Code)
- **Supervisory authority**: Information Commissioner's Office (ICO), Wycliffe House,
  Water Lane, Wilmslow, Cheshire SK9 5AF; ico.org.uk
- **Litigation and disclosure**: Civil Procedure Rules (CPR), CPR Part 31 (Disclosure
  and Inspection of Documents), CPR Practice Direction 31B (Disclosure of Electronic
  Documents), CPR Part 34 (Witnesses, Depositions and Taking of Evidence Abroad)
- **Privilege**: Legal Professional Privilege (LPP) -- both litigation privilege and
  legal advice privilege. _Three Rivers District Council v Governor and Company of the
  Bank of England (No 5)_ [2004] UKHL 48 limitations for in-house counsel communications
- **Insurance**: Insurance Act 2015, duty of fair presentation (s.3), Enterprise Act
  2016 (s.13A -- damages for late payment of claims)
- **Supply chain**: Modern Slavery Act 2015 (s.54 -- transparency in supply chains,
  applicable to organisations with turnover exceeding GBP 36 million)
- **Criminal**: Bribery Act 2010, Fraud Act 2006, Health and Safety at Work etc Act 1974
- **Electronic signatures**: Electronic Communications Act 2000 (electronic signatures
  valid for most contracts; deeds require additional formalities)
- **Regulators**: ICO, FCA (Financial Conduct Authority), PRA (Prudential Regulation
  Authority), TPR (The Pensions Regulator), CMA (Competition and Markets Authority),
  SFO (Serious Fraud Office), Ofcom, HMRC

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change which template category applies
- The specific English law provision or ICO guidance relevant to the inquiry is unclear
- Escalation trigger detection requires user confirmation
- Multiple valid response approaches exist under English law
- Tone or audience calibration is needed (e.g., ICO response vs individual DSAR response)

Use the **CLARIFY** pattern: present structured options with "Why this matters"
explanations. If the user has already provided the information, skip the question
and proceed.

---

## Workflow

### Step 1: Accept the Inquiry

Accept the legal inquiry requiring a response in any format:

- Forwarded email or message describing the inquiry
- Summary of the request and relevant context
- Reference to a specific template category and variables
- Request to create a new template for a recurring inquiry type

If the inquiry type is unclear, proceed to Step 2 for clarification.

### Step 2: Gather Context

**CLARIFY** -- Before selecting or generating a template, gather essential context:

1. **Inquiry type**: What category does this inquiry fall into?
   - Options: Data Subject Access Request (DSAR), Litigation Hold / Document
     Preservation, Privacy Inquiry, Vendor Question, NDA Request, Legal Process
     (Witness Summons / Court Order), Insurance Notification, Other (describe)
   - _Why this matters_: Determines which template category and escalation triggers
     apply under English law.

2. **Audience**: Who is the recipient?
   - Options: Individual data subject, Business counterparty, Regulator (ICO, FCA, PRA,
     TPR, CMA, SFO, Ofcom, HMRC), Internal (employee/custodian), Opposing solicitor,
     Other
   - _Why this matters_: Determines tone, formality level, and required disclosures
     under English law.

3. **Urgency**: What is the timeline?
   - Options: Standard (use statutory deadline -- e.g., one calendar month for DSARs),
     Expedited (shorter than standard), Already overdue (remediation mode), No deadline
     (informational)
   - _Why this matters_: Determines whether extension notices are needed and response
     prioritisation.

4. **Prior handling**: Has the team handled similar inquiries before?
   - Options: Yes -- use existing template, Yes -- but template needs update,
     No -- novel situation, Unknown
   - _Why this matters_: Novel situations may require escalation rather than templating.

5. **Privilege considerations**: Does Legal Professional Privilege apply?
   - Options: Yes -- litigation privilege, Yes -- legal advice privilege, _Three Rivers_
     considerations for in-house counsel communications, Not applicable, Uncertain
   - _Why this matters_: Affects privilege marking and how the response is prepared
     and stored.

If any answer indicates a potential escalation trigger, proceed to Step 3 before
generating a response.

### Step 3: Check Escalation Triggers

Before generating ANY templated response, systematically check for escalation triggers.
If any trigger is present, do NOT generate a standard templated response -- instead,
escalate per the protocol below.

#### Universal Escalation Triggers (Apply to All Categories)

- The matter involves potential litigation or regulatory investigation
- The inquiry is from the ICO, FCA, PRA, TPR, CMA, SFO, Ofcom, HMRC, or any other
  regulatory body or government agency
- The response could create a binding legal commitment or waiver
- The matter involves potential criminal liability (including Bribery Act 2010, Fraud
  Act 2006, health and safety offences)
- Media attention is involved or likely
- The situation is unprecedented (no prior handling by the team)
- Multiple jurisdictions are involved with conflicting requirements
- The matter involves directors, officers, board members, or politically exposed persons
- Legal Professional Privilege considerations are complex or disputed -- particularly
  _Three Rivers_ limitations for in-house counsel communications
- The inquiry is from a party in active litigation or dispute with the organisation

#### Category-Specific Escalation Triggers

**Data Subject Access Requests (DSARs) -- UK GDPR / DPA 2018:**

- Request from or on behalf of a minor (consider Age-Appropriate Design Code / Children's
  Code implications)
- Request involves data subject to a litigation hold (tension between disclosure and
  preservation obligations)
- Requester is in active litigation or dispute with the organisation
- Request from an employee with an active HR matter, grievance, or disciplinary
  investigation
- Request scope is extraordinarily broad (potential fishing expedition -- but note the
  ICO discourages refusing requests on this basis without careful consideration)
- Request involves special category data (UK GDPR Article 9: health, biometric, genetic,
  religious beliefs, political opinions, sexual orientation, trade union membership)
- Request involves criminal conviction or offence data (UK GDPR Article 10 / DPA 2018
  s.10)
- Legal Professional Privilege analysis required for responsive documents (apply _Three
  Rivers_ test for in-house communications)
- DPA 2018 Schedule 2 exemption analysis required (e.g., legal proceedings exemption,
  management forecasting exemption, negotiations exemption)

**Litigation Holds / Document Preservation:**

- Potential criminal liability (SFO, HMRC, or police involvement)
- Unclear or disputed preservation scope
- Preservation conflicts with UK GDPR erasure obligations (data subject right to erasure
  under UK GDPR Article 17 vs litigation hold preservation duty)
- Prior holds exist for related matters
- Custodian objects to the hold scope
- Cross-border preservation obligations with conflicting legal requirements (e.g., US
  litigation hold overlapping with UK GDPR erasure rights)
- Data localisation requirements restrict where preserved data can be stored or accessed

**Vendor Questions:**

- Vendor is disputing contract terms
- Vendor is threatening litigation or termination
- Response could affect ongoing negotiation
- Question involves regulatory compliance (not just contract interpretation)
- Modern Slavery Act 2015 compliance concerns (s.54 annual statement obligations for
  organisations with turnover exceeding GBP 36 million)
- Cyber Essentials certification disputes or security incident disclosures

**Legal Process (Witness Summons / Court Orders):**

- **ALWAYS requires solicitor review** -- templates are starting points only, never final
  responses
- Legal Professional Privilege issues identified in responsive documents
- Third-party personal data involved (UK GDPR implications of disclosure to court or
  third parties)
- Cross-border production issues (requested documents held outside England and Wales)
- Unreasonable timeline that may require application to court to vary
- Norwich Pharmacal orders -- always instruct solicitors
- Third-party disclosure orders (CPR Part 31.17) -- always instruct solicitors

**Insurance Notifications:**

- Late notification (potential coverage dispute under policy terms or Insurance Act 2015)
- Claim may implicate multiple policies or coverage towers
- Reservation of rights letter received from insurer
- Coverage dispute anticipated
- Matter involves D&O, E&O, or cyber policies with complex notification requirements
- Broker has raised concerns about notification obligations

#### When an Escalation Trigger is Detected

1. **Stop**: Do not generate a final templated response
2. **Alert**: Inform the user that an escalation trigger has been detected
3. **Explain**: Describe which trigger was detected and why it matters under English law
4. **Recommend**: Suggest the appropriate escalation path (senior solicitor, external
   counsel, specific team member, regulatory specialist)
5. **Offer**: Provide a DRAFT for solicitor review, clearly marked:
   ```
   ============================================================
   DRAFT -- FOR SOLICITOR REVIEW ONLY -- NOT TO BE SENT
   Escalation trigger detected: [trigger description]
   Recommended escalation: [path]
   ============================================================
   ```

### Step 4: Select or Create Template

If no escalation triggers are present, proceed to select the appropriate template
category and either:

- **Use existing template**: Select from the team's template library
- **Generate from framework**: Use the category frameworks below to generate a response
- **Create new template**: Follow the Template Creation Guide to establish a new template

### Step 5: Customise and Generate Response

Apply required customisations:

1. Fill all variable placeholders with correct values
2. Adjust tone for the specific audience and relationship
3. Insert England & Wales-specific elements (UK GDPR / DPA 2018 citations, ICO contact
   details, CPR references, English law terminology)
4. Verify deadline calculations are correct (one calendar month, not "30 days")
5. Include all legally required elements (e.g., ICO complaint rights for DSARs)
6. Apply Legal Professional Privilege marking where appropriate

### Step 6: Quality Verification

Before delivering the response, run the Quality Framework (see below):

1. Citation Quality Gates -- all 5 gates must pass
2. Completeness check -- all required elements present
3. Writing standards -- plain language, active voice, British English, no ambiguity
4. Escalation re-check -- confirm no triggers missed during drafting

### Step 7: Generate Glass Box Audit Entry

Create an internal audit record (retained in matter file, NOT sent to recipient).

### Step 8: Deliver Response and Log Follow-Up

Provide the final response and:

1. List required follow-up actions
2. Note any deadlines created by the response (including statutory deadlines under UK
   GDPR, CPR, or policy terms)
3. Flag the matter for tracking until resolution

---

## Response Categories

### 1. Data Subject Access Requests (DSARs) -- UK GDPR / DPA 2018

**Sub-categories:**

- Acknowledgment of receipt
- Identity verification request
- Fulfilment response (access, deletion, rectification, portability, restriction)
- Partial exemption/redaction with explanation (DPA 2018 Schedule 2)
- Full refusal with explanation (manifestly unfounded/excessive under UK GDPR Article
  12(5), or exemption applies)
- Extension notification (complex request requiring additional time -- UK GDPR Article
  12(3))

**Key template elements:**

- Reference to **UK GDPR** (not just "GDPR") and **Data Protection Act 2018** where
  relevant
- Specific timeline: **one calendar month** from receipt (UK GDPR Article 12(3)),
  extendable by **two further months** for complex requests with notification to the data
  subject within the original month
- Identity verification requirements (proportionate to data sensitivity -- ICO guidance)
- Rights of the data subject, including:
  - Right to lodge a complaint with the **Information Commissioner's Office (ICO)**,
    Wycliffe House, Water Lane, Wilmslow, Cheshire SK9 5AF; ico.org.uk
  - Right to a **judicial remedy** (UK GDPR Article 79)
- Exemptions applied and legal basis (DPA 2018 Schedule 2 paragraph references)
- Contact information for the DPO or privacy team

**Example template structure -- DSAR Acknowledgment:**

```
Subject: Your Data Subject Access Request -- Reference {{request_id}}

Dear {{requester_name}},

Thank you for your request dated {{request_date}} to {{request_type}} your personal
data. We are processing your request under the UK General Data Protection Regulation
(UK GDPR) and the Data Protection Act 2018.

{{IF identity_verification_needed}}
Before we can process your request, we need to verify your identity. Please provide
{{verification_requirements}}.
{{ENDIF}}

We will respond substantively within one calendar month of
{{receipt_date_or_verification_date}}. If we need to extend this period due to the
complexity of your request, we will notify you within that month and explain the reasons.

If you have any questions, please contact {{privacy_contact}}.

You have the right to lodge a complaint with the Information Commissioner's Office (ICO)
if you are not satisfied with how we handle your request. The ICO can be contacted at
Wycliffe House, Water Lane, Wilmslow, Cheshire SK9 5AF, or at ico.org.uk.

{{signature_block}}
```

**Example template structure -- DSAR Partial Exemption:**

```
Subject: Response to Your Data Subject Access Request -- Reference {{request_id}}

Dear {{requester_name}},

Further to your request dated {{request_date}}, please find enclosed the personal data
we hold about you.

We have applied the following exemption(s) to certain data:

{{FOR EACH exemption}}
- **Exemption**: {{exemption_name}} (Data Protection Act 2018, Schedule 2,
  {{paragraph_reference}})
- **Scope**: {{description_of_data_withheld}}
- **Basis**: {{reason_exemption_applies}}
{{ENDFOR}}

The enclosed data represents all personal data we hold about you, subject to the
exemptions noted above.

You have the right to:
- Lodge a complaint with the Information Commissioner's Office (ICO) at Wycliffe House,
  Water Lane, Wilmslow, Cheshire SK9 5AF (ico.org.uk)
- Seek a judicial remedy under Article 79 of the UK GDPR

{{signature_block}}
```

### 2. Litigation Holds / Document Preservation Notices

**English law framework:** The duty to preserve documents relevant to litigation arises
once litigation is **reasonably contemplated** (not just when proceedings are issued).
CPR Practice Direction 31B (Disclosure of Electronic Documents) governs the preservation
and disclosure of electronic documents. CPR Part 31 governs disclosure and inspection of
documents generally.

**Sub-categories:**

- Initial preservation notice to custodians
- Preservation notice reminder / periodic reaffirmation
- Scope modification notice (expansion or narrowing)
- Release of preservation obligations

**Key template elements:**

- Matter name and reference number
- Clear preservation obligations (what must be preserved)
- Scope of preservation (date range, data types, systems, custodians, communication
  types)
- Prohibition on destruction, alteration, or disposal of potentially relevant documents
- Reference to CPR duties and potential consequences of non-compliance (contempt of
  court, adverse inferences)
- Contact for questions
- Acknowledgment requirement with deadline
- Legal Professional Privilege marking: "SUBJECT TO LEGAL PROFESSIONAL PRIVILEGE --
  CONFIDENTIAL"

**Example template structure -- Litigation Hold Notice:**

```
Subject: DOCUMENT PRESERVATION NOTICE -- {{matter_name}} -- Action Required

SUBJECT TO LEGAL PROFESSIONAL PRIVILEGE -- CONFIDENTIAL

Dear {{custodian_name}},

You are receiving this notice because you may hold documents, communications, or data
relevant to the matter referenced above.

PRESERVATION OBLIGATION:
With immediate effect, you must preserve all documents and electronic documents (as
defined in CPR Practice Direction 31B) relating to:
- Subject matter: {{hold_scope}}
- Date range: {{start_date}} to present
- Document types: {{document_types}}

This includes but is not limited to: emails, letters, memoranda, file notes, reports,
spreadsheets, presentations, instant messages, text messages, voicemails, calendar
entries, and any other records in any format (paper or electronic) including drafts,
notes, and metadata.

YOU MUST NOT delete, destroy, modify, move, or discard any potentially relevant
documents or data. This includes:
- Do not delete emails (including from deleted items/trash folders)
- Do not overwrite or modify electronic files
- Do not destroy paper documents
- Do not alter any records, including metadata
- Suspend any automated deletion or archiving processes for in-scope data

Failure to preserve relevant documents may constitute contempt of court and may result
in adverse inferences being drawn against the organisation. The court has powers under
CPR Part 31 to impose sanctions for non-compliance with disclosure obligations.

[Specific instructions for systems, email, messaging platforms, local files, shared
drives, cloud storage]

Please acknowledge receipt of this notice by replying to this email by
{{acknowledgment_deadline}}.

Contact {{legal_contact}} immediately if you have any questions about what should be
preserved or if you become aware of any relevant documents that may be at risk.

{{signature_block}}
```

**Terminology note:** England and Wales uses **"disclosure"** (not "discovery") under
CPR Part 31. The process of identifying, reviewing, and producing relevant documents is
governed by the CPR and its Practice Directions. "Litigation hold" and "document
preservation notice" are acceptable terms for internal communications; the CPR itself
refers to the parties' disclosure obligations.

### 3. Privacy Inquiries

**Sub-categories:**

- Cookie/tracking inquiry responses (Privacy and Electronic Communications Regulations
  2003 -- PECR 2003)
- Privacy notice/policy questions (UK GDPR Articles 13-14)
- Data sharing practice inquiries
- Children's data inquiries (Age-Appropriate Design Code / Children's Code)
- International/cross-border transfer questions (UK adequacy decisions, UK International
  Data Transfer Agreement, UK Addendum to EU SCCs)
- ICO complaint or enforcement correspondence

**Key template elements:**

- Reference to the organisation's privacy notice (UK GDPR Articles 13-14)
- Specific answers based on current processing activities
- Links to relevant privacy documentation
- Lawful basis for processing (UK GDPR Article 6, and Article 9 for special category
  data)
- Reference to PECR 2003 for e-marketing and cookie queries
- Age-Appropriate Design Code considerations for services likely to be accessed by
  children
- Contact information for the DPO or privacy team
- ICO complaint rights information (full address: Wycliffe House, Water Lane, Wilmslow,
  Cheshire SK9 5AF; ico.org.uk)

### 4. Vendor Legal Questions

**Sub-categories:**

- Contract status inquiry response
- Amendment request response
- Compliance certification requests (ISO 27001, SOC 2, Cyber Essentials, Cyber
  Essentials Plus)
- Audit request responses
- Insurance certificate requests
- Modern Slavery Act 2015 compliance inquiries

**Key template elements:**

- Reference to the applicable agreement (name, date, parties)
- Specific response to the vendor's question
- Any required caveats or limitations
- Next steps and timeline
- Modern Slavery Act 2015 compliance statement reference (s.54 -- organisations with
  annual turnover exceeding GBP 36 million must publish an annual modern slavery
  statement)
- Cyber Essentials / Cyber Essentials Plus certification status (if applicable)

### 5. NDA Requests

**Sub-categories:**

- Sending the organisation's standard form NDA (governed by English law)
- Accepting a counterparty's NDA (with or without markup)
- Declining an NDA request with explanation
- NDA renewal or extension

**Key template elements:**

- Purpose of the NDA (subject matter of the contemplated disclosure)
- Governing law: English law, exclusive jurisdiction of the courts of England and Wales
- Summary of key terms
- Execution instructions: NDAs do not generally need to be executed as deeds under
  English law; simple contract execution is sufficient. Electronic signatures are valid
  under the Electronic Communications Act 2000 and accepted by the Law Commission
  (September 2019 report on electronic execution of documents). Wet-ink signatures are
  not required unless the NDA is to be executed as a deed.
- Timeline expectations

### 6. Legal Process (Witness Summons / Court Orders)

**English law framework:** England and Wales does not use "subpoenas." The equivalent
mechanisms are:

- **Witness summons** (CPR Part 34) -- compels attendance at court to give evidence or
  produce documents
- **Third-party disclosure orders** (CPR Part 31.17) -- court orders requiring
  non-parties to disclose documents where (a) the documents are likely to support the
  applicant's case or adversely affect another party's case, and (b) disclosure is
  necessary to dispose fairly of the claim or save costs
- **Norwich Pharmacal orders** -- court orders (based on _Norwich Pharmacal Co v
  Customs and Excise Commissioners_ [1974] AC 133) requiring a party mixed up in
  wrongdoing to provide information to identify the wrongdoer
- **Court orders for production** -- various statutory and inherent jurisdiction powers

**Sub-categories:**

- Acknowledgment of receipt of witness summons or court order
- Objection or application to set aside (with specific grounds under CPR)
- Request for extension of time (application to court)
- Compliance cover letter
- Privilege schedule transmittal (listing documents withheld on grounds of Legal
  Professional Privilege, indicating the nature of the privilege claimed)

**Key template elements:**

- Court reference, case name, and claim number
- Specific objections (if any) -- e.g., Legal Professional Privilege (both litigation
  privilege and legal advice privilege), irrelevance, disproportionality, public interest
  immunity
- Preservation confirmation
- Timeline for compliance (as specified in the order or summons)
- Privilege schedule (if applicable -- listing documents withheld on grounds of LPP)
- Without prejudice to any right to apply to set aside or vary the order

**Critical note:** Responses to court orders and witness summons ALWAYS require
individualised solicitor review. Templates serve as starting frameworks, never as final
responses. Non-compliance with a court order may constitute contempt of court.

### 7. Insurance Notifications

**English law framework:** The Insurance Act 2015 governs commercial insurance contracts
entered into after 12 August 2016. Key provisions:

- **Duty of fair presentation** (s.3): Before the contract is entered into, the insured
  must make a fair presentation of the risk to the insurer
- **Notification obligations**: Policy terms specify notification requirements. Late
  notification may entitle insurers to reduce proportionately or rely on specific policy
  terms
- **Damages for late payment** (s.13A, inserted by the Enterprise Act 2016): Insurers
  that unreasonably delay payment of claims may be liable for damages

**Sub-categories:**

- Initial claim notification / circumstance notification
- Supplemental information
- Response to reservation of rights letter
- D&O (Directors' and Officers') / E&O / Cyber policy notifications (often have unique
  notification requirements)

**Key template elements:**

- Policy number, insurer name, broker details, and coverage period
- Broker involvement (most UK commercial insurance is placed through brokers -- notify
  the broker as well as the insurer unless the policy specifies direct notification only)
- Description of the matter, incident, or circumstance
- Timeline of events
- Quote of specific policy notification clause being complied with
- Requested coverage confirmation
- Without prejudice / reservation of rights language
- Compliance with Insurance Act 2015 duty of fair presentation (s.3)

---

## Template Management Framework

### Template Organisation

Templates should be organised by category and maintained in the team's document
management system or local settings. Each template should include:

| Element                     | Description                                                      | Required |
| --------------------------- | ---------------------------------------------------------------- | -------- |
| **Category**                | Response category (DSAR, Hold, etc.)                             | Yes      |
| **Template name**           | Descriptive identifier                                           | Yes      |
| **Version**                 | Version number for change tracking                               | Yes      |
| **Last reviewed**           | Date of last legal review                                        | Yes      |
| **Approved by**             | Name/title of approving solicitor                                | Yes      |
| **Applicable legislation**  | Relevant statutes and regulations (UK GDPR, DPA 2018, CPR, etc.) | Yes      |
| **Use case**                | When this template is appropriate                                | Yes      |
| **Escalation triggers**     | When NOT to use this template                                    | Yes      |
| **Required variables**      | Information that must be customised                              | Yes      |
| **Template body**           | Response text with variable placeholders                         | Yes      |
| **Follow-up actions**       | Standard steps after sending                                     | Yes      |
| **ICO/regulatory guidance** | Relevant ICO or other regulatory guidance referenced             | Optional |
| **Notes**                   | Special instructions for users                                   | Optional |

### Template Lifecycle

1. **Creation**: Draft based on current English law, ICO guidance, CPR provisions, and
   team input
2. **Review**: Solicitor review and approval of template content
3. **Publication**: Add to template library with full metadata
4. **Use**: Generate responses using the template
5. **Feedback**: Track when templates are modified during use -- identify improvement
   needs
6. **Update**: Revise when legislation, ICO guidance, CPR amendments, or best practices
   change
7. **Retirement**: Archive templates that are no longer applicable

### Template Format

```markdown
## Template: {{template_name}}

**Category**: {{category}}
**Version**: {{version}} | **Last Reviewed**: {{date}}
**Approved By**: {{approver}}
**Applicable Legislation**: {{legislation_references}}

### Use When

- [Condition 1]
- [Condition 2]

### Do NOT Use When (Escalation Triggers)

- [Trigger 1]
- [Trigger 2]

### Variables

| Variable | Description  | Example         | Validation           |
| -------- | ------------ | --------------- | -------------------- |
| {{var1}} | [what it is] | [example value] | [format/constraints] |

### Subject Line

[Subject template with {{variables}}]

### Body

[Response body with {{variables}}]

### Follow-Up Actions

1. [Action 1]
2. [Action 2]

### Notes

[Special instructions, including any ICO guidance references]
```

---

## Customisation Guidelines

### Required Customisation

Every templated response MUST be customised with:

- Correct names, dates, and reference numbers
- Specific facts of the situation (not generic placeholders)
- Applicable legislation (UK GDPR, DPA 2018, PECR 2003, CPR, Insurance Act 2015, etc.)
- Correct response deadlines calculated from the date of receipt (one calendar month
  for DSARs, not "30 days")
- Appropriate signature block and contact information
- ICO complaint rights where required by UK GDPR (Article 12/13/14)
- Legal Professional Privilege marking where appropriate

### Tone Adjustment Matrix

| Dimension        | Options                                               | Guidance                                         |
| ---------------- | ----------------------------------------------------- | ------------------------------------------------ |
| **Audience**     | Internal / External / Regulatory (ICO, FCA, PRA, TPR) | Regulatory = most formal, precise                |
| **Relationship** | New / Existing / Adversarial                          | Adversarial = more guarded, no admissions        |
| **Sensitivity**  | Routine / Contentious / Investigation                 | Investigation = solicitor review required        |
| **Urgency**      | Standard / Expedited / Overdue                        | Overdue = acknowledge delay, explain remediation |

### Jurisdiction-Specific Checks

Before sending any response, verify:

- [ ] UK GDPR / DPA 2018 cited (not just "GDPR" which may imply EU GDPR)
- [ ] Timelines match English law (one calendar month for DSARs, not "30 days")
- [ ] English legal terminology used throughout: disclosure (not discovery), witness
      summons (not subpoena), solicitor (not attorney), barrister (not trial lawyer),
      Legal Professional Privilege (not attorney-client privilege), claimant (not
      plaintiff), claim form (not complaint), injunction (not restraining order)
- [ ] ICO named as supervisory authority (not generic "data protection authority")
- [ ] English courts and CPR provisions referenced (not Federal Rules or state rules)
- [ ] Legal Professional Privilege marking uses English convention ("Subject to Legal
      Professional Privilege")
- [ ] British English spelling used throughout (organisation, colour, programme,
      defence, licence/license distinction, practise/practice distinction)
- [ ] Monetary amounts in GBP where relevant

---

## Quality Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                                                                                   | Fail Action                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Source**     | Every regulatory reference cites specific article/section/provision (e.g., "UK GDPR Article 15", "DPA 2018, Schedule 2, paragraph 5")                                                                                  | Add citation or mark "[VERIFY]"                 |
| **Format**     | Citations use correct English law format: statutes by short title and section, SIs by year and number, case law by neutral citation or law report reference                                                            | Fix format                                      |
| **Currency**   | Cited provisions and ICO guidance confirmed current and in force                                                                                                                                                       | Flag "[CHECK CURRENCY]"                         |
| **Domain**     | English law terminology throughout -- no US terms in English law responses (disclosure not discovery, witness summons not subpoena, solicitor not attorney, LPP not attorney-client privilege, claimant not plaintiff) | Fix terminology                                 |
| **Confidence** | If template is being stretched beyond its designed use case, flag it                                                                                                                                                   | Add "[SOLICITOR TO REVIEW -- template adapted]" |

### Self-Interrogation for High-Stakes Responses

For any response involving regulators (ICO, FCA, PRA, TPR, SFO), legal process, or
potential litigation, apply this 3-pass review:

**Pass 1 -- Completeness:** Does the response include all legally required elements
under English law? Are all statutory rights mentioned (e.g., ICO complaint rights for
DSARs)? Are all deadlines correctly calculated using "one calendar month" (not "30
days")?

**Pass 2 -- Accuracy:** Are all UK GDPR / DPA 2018 / CPR citations correct and current?
Is the terminology appropriate for England and Wales (not US or EU)? Are there any
statements that could be construed as admissions or waivers?

**Pass 3 -- Appropriateness:** Is a templated response actually appropriate here, or
should this be escalated to a solicitor? Have all escalation triggers been checked? Would
a reasonable qualified solicitor approve sending this without further review?

### Confidence Scoring

| Level        | Range     | Meaning                            | Action                                 |
| ------------ | --------- | ---------------------------------- | -------------------------------------- |
| **Definite** | 0.95-1.0  | Standard template, routine matter  | Send after standard review             |
| **High**     | 0.80-0.94 | Minor customisation, known pattern | Send with quality check                |
| **Probable** | 0.60-0.79 | Significant adaptation required    | Senior solicitor review before sending |
| **Possible** | 0.40-0.59 | Template being stretched           | Solicitor review required              |
| **Unlikely** | 0.0-0.39  | Template not appropriate           | Do not use template -- escalate        |

### Glass Box Audit Trail

Every generated response MUST include an internal Glass Box audit record. This is
retained in the matter file -- NOT sent to the recipient.

```yaml
glass_box:
  inquiry_type: "[DSAR / Litigation hold / Privacy inquiry / Vendor / NDA / Legal process / Insurance]"
  template_used: "[Template name and version, or 'Generated from framework']"
  template_modified: "Yes / No -- if yes, [what was changed and why]"
  jurisdiction: "England and Wales"
  regulations_applied:
    - "UK GDPR, Article [X]"
    - "DPA 2018, [section/schedule/paragraph]"
    - "CPR Part [X] / PD [X]"
  citations_verified:
    - "[Citation] -- VERIFIED / UNVERIFIED"
  deadline_calculation:
    received: "[YYYY-MM-DD]"
    deadline: "[YYYY-MM-DD]"
    basis: "One calendar month from receipt (UK GDPR Art.12(3))"
  exemptions_applied:
    - "[Exemption] -- [DPA 2018 Schedule 2 paragraph] -- [Applied to: description]"
  escalation_triggers_checked:
    - "[Trigger 1] -- Present / Not present"
  confidence: "HIGH / MEDIUM / LOW -- [rationale]"
  quality_gates_passed: "5/5 or [list failures]"
  reviewer: "[Name or 'AI-assisted -- requires solicitor review before sending']"
  follow_up_actions:
    - "[Action 1]"
```

---

## Writing Standards

Templated legal responses must be clear, professional, and understandable by their
intended audience. Apply these standards to every response.

### British English Requirements

All responses MUST use British English spelling and conventions:

- **-ise** not -ize: organise, customise, recognise, authorise
- **-our** not -or: colour, behaviour, favour, honour
- **-ence** not -ense: defence, licence (noun), offence
- **-mme** not -m: programme (but "program" for software)
- **-re** not -er: centre, metre (measurement)
- **-isation** not -ization: organisation, authorisation, localisation
- **practise** (verb) / **practice** (noun) distinction
- **licence** (noun) / **license** (verb) distinction
- Date format: **15 January 2026** (not January 15, 2026 or 01/15/2026)

### Three-Pass Editing

**Pass 1 -- Structure:** Does the response answer the inquiry? Is information in logical
order? Is anything missing? Is anything unnecessary?

**Pass 2 -- Clarity:** Can the recipient understand this without legal training (where
appropriate)? Replace passive constructions with active voice. Ensure every pronoun has
a clear antecedent. Remove ambiguity.

**Pass 3 -- Concision:** Cut padding, hedging, and unnecessary qualifiers. Replace long
words with short where meaning is preserved. Remove jargon unless the audience expects
it. Target 20-30% word count reduction from first draft.

### Specific Rules

- **Active voice:** "We received your request on 15 January" not "Your request was
  received on 15 January"
- **Name the actor:** "The ICO can investigate" not "An investigation may be commenced"
- **Plain English for individuals:** DSAR responses go to people who may have no legal
  knowledge. Write accordingly.
- **Formal but clear for regulators:** The ICO, FCA, PRA, and TPR appreciate factual,
  well-organised responses. Avoid advocacy language in factual submissions.
- **Precise for preservation notices:** Litigation holds must be unambiguous. "You must
  not delete emails" is better than "Please ensure electronic communications are
  preserved in accordance with the organisation's document retention policy."
- **No hidden complexity:** Obscure language in a DSAR response that makes it harder for
  the data subject to understand their rights is not just bad writing -- it risks ICO
  enforcement.

### Quality Gates Before Sending

1. Would a non-lawyer recipient understand this response (where applicable)?
2. Are all regulatory references correct and current (UK GDPR, DPA 2018, PECR, CPR)?
3. Is the deadline correctly calculated using "one calendar month" (not "30 days")?
4. Are ICO complaint rights included where required by UK GDPR?
5. Has every escalation trigger been checked?
6. Is this response appropriate for the specific facts, or is it generic boilerplate?
7. Have all variables been replaced with actual values (no {{placeholders}} remain)?
8. Is British English spelling used throughout?

---

## Anti-Patterns

What NOT to do with templated legal responses under English law:

1. **Sending a template without customisation** -- A response with "{{requester_name}}"
   or other unfilled variables is worse than no response. Every variable must be filled.
   Every response must be reviewed against the specific facts.

2. **Using "30 days" instead of "one calendar month"** -- These are different deadlines
   under English law. One calendar month from 31 January is 28/29 February, not 2 March.
   This error has been flagged in ICO enforcement action. Always use "one calendar month."

3. **Citing "GDPR" without specifying UK** -- In a DSAR response to a UK individual, you
   must cite the UK GDPR (not "GDPR" unqualified, which may imply EU GDPR). Citing "GDPR"
   without specifying UK or EU is ambiguous and may be incorrect post-Brexit.

4. **Applying DPA 2018 Schedule 2 exemptions without documentation** -- "We have applied
   an exemption to some documents" is insufficient. Each exemption must be applied to
   specific data with a documented reason citing the specific Schedule 2 paragraph,
   retained in the matter file for potential ICO inquiry.

5. **Vague preservation notices** -- A litigation hold that politely asks custodians to
   "please keep relevant documents" does not convey the severity. Explain that
   non-compliance may constitute contempt of court and result in adverse inferences being
   drawn against the organisation under CPR Part 31.

6. **Templated responses to regulators** -- Never send a template response to the ICO,
   FCA, PRA, TPR, SFO, or any regulator without individualised solicitor review.
   Regulators recognise boilerplate, and it signals the organisation is not taking the
   matter seriously.

7. **Omitting ICO complaint rights in DSAR responses** -- This is a legal requirement
   under UK GDPR Articles 12-14, not optional courtesy. Omitting ICO complaint rights is
   a compliance failure.

8. **Using American legal terminology** -- "Discovery hold," "subpoena,"
   "attorney-client privilege," "plaintiff," "complaint," "restraining order" are US
   terms. England and Wales uses: disclosure, litigation hold / document preservation
   notice, witness summons, Legal Professional Privilege (LPP), claimant, claim form,
   injunction. Using the wrong terms in a formal legal communication is unprofessional
   and may confuse recipients.

9. **Missing deadlines without extension notice** -- If you need more time for a DSAR,
   you must notify the data subject within the original one calendar month and explain
   why (UK GDPR Article 12(3)). Silently missing the deadline is a UK GDPR breach.

10. **Fire-and-forget responses** -- Every response needs follow-up actions: log the
    response, schedule follow-up deadlines, update the matter file, close the request
    only when fully resolved.

11. **Ignoring escalation triggers** -- Proceeding with a templated response when an
    escalation trigger is present. The escalation check exists because some situations
    cannot be safely handled with templates.

12. **Template scope creep** -- Using a template designed for one situation (e.g., simple
    DSAR acknowledgment) for a different situation (e.g., complex DSAR with Schedule 2
    exemptions and privilege issues). Each template has a designed use case -- respect its
    boundaries.

13. **Copying without understanding** -- Using template language without understanding
    why it exists under English law. If you cannot explain why each element of the
    response is there and which provision of UK GDPR, DPA 2018, or CPR requires it, you
    should not be sending it.

14. **Inconsistent variable naming** -- Using {{name}}, {{requester_name}},
    {{data_subject}}, and {{individual}} interchangeably in the same template library.
    Standardise variable names across all templates.

15. **No version control** -- Failing to track template versions, leading to outdated
    templates being used after legislation changes (e.g., continued use of templates
    drafted before the UK GDPR replaced direct application of EU GDPR). Every template
    needs a version number and last-reviewed date.

16. **Privilege marking errors** -- Using "Attorney-Client Privilege" or "Attorney Work
    Product" markings on English law communications. The correct marking is "Subject to
    Legal Professional Privilege" (covering both litigation privilege and legal advice
    privilege). Using incorrect privilege assertions may create confusion and, in
    adversarial contexts, may be challenged. Be aware of _Three Rivers_ limitations when
    asserting legal advice privilege over in-house counsel communications.

---

## External Tool Integration

### legalcode-mcp Integration

If **legalcode-mcp** is connected, use it for:

- Verifying current UK statutory text and ICO guidance
- Checking recent ICO enforcement actions or guidance updates
- Validating deadline calculations against current law
- Researching England and Wales-specific requirements (CPR amendments, Practice Direction
  updates)

**With legalcode-mcp connected:**

- Mark verified citations as `VERIFIED` in the Glass Box audit trail
- Update templates based on recent ICO guidance or legislative changes

**Without legalcode-mcp:**

- Proceed with template generation
- Mark regulatory citations as `[VERIFY]` where currency is uncertain
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Document Management Integration

Templates should integrate with the organisation's:

- Matter management system (for audit trail retention)
- Document management system (for template storage and versioning)
- Email system (for response delivery)
- Deadline tracking system (for follow-up scheduling -- particularly statutory deadlines
  under UK GDPR and CPR)

---

## Output Format Template

When generating a response, structure the output as follows:

````markdown
## Generated Response

**Category**: [Response category]
**Template**: [Template name and version, or "Generated from framework"]
**Jurisdiction**: England and Wales
**Confidence**: [HIGH / MEDIUM / LOW]

---

### Response Text

[The actual response to be sent, fully customised with all variables filled, in British
English]

---

### Internal Notes (Do Not Send)

**Deadline**: [Calculated deadline and statutory basis -- e.g., "One calendar month from
receipt (UK GDPR Art.12(3))"]

**Escalation triggers checked**:

- [x] [Trigger 1] -- Not present
- [x] [Trigger 2] -- Not present
- [If any present, explain why proceeding or recommend escalation]

**Required follow-up actions**:

1. [Action 1 with deadline if applicable]
2. [Action 2]

**Glass Box Audit**:

```yaml
[Full glass_box YAML block]
```
````

---

### Quality Verification

| Gate                      | Status      |
| ------------------------- | ----------- |
| Source citations          | PASS / FAIL |
| Citation format           | PASS / FAIL |
| Currency                  | PASS / FAIL |
| Terminology (English law) | PASS / FAIL |
| Confidence                | PASS / FAIL |

**Writing standards**: [Confirmed / Issues noted]

**British English**: [Confirmed / Issues noted]

**Ready to send**: [Yes -- after solicitor review / No -- escalation required]

```

---

## Provenance

- **Original synthesis**: Legalcode (2026-02-27)
- **Base skill**: `skills/general/workflows/legalcode-canned-responses/SKILL.md`
  (jurisdiction-agnostic framework)
- **UK-specific content source**:
  `skills/general/workflows/imported-uk-legal-plugins--skills-uk-legal-canned-responses/SKILL.md`
  (45black/uk-legal-plugins -- Apache-2.0)
- **Jurisdiction variant pattern**: `legalcode-nda-triage-ew` (structural reference)
- **Reference standard**: `legalcode-contract-review` quality framework
- **License**: Apache-2.0 (consistent with source skills)
```
