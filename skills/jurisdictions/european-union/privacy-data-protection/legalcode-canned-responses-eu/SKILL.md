---
name: legalcode-canned-responses-eu
description: Generate, manage, and customize templated responses for routine legal inquiries under EU
  law — data subject requests (DSRs under EU GDPR), litigation holds, privacy inquiries, vendor questions,
  NDA requests, legal process (European Investigation Orders, court orders, Member State mechanisms),
  and insurance notifications. Use when responding to routine legal questions governed by EU law, managing
  response template libraries for EU operations, creating new templates, or identifying when a situation
  requires individualized counsel attention rather than a templated response. Covers the EU GDPR framework
  (Regulation 2016/679) with Member State variation markers where national law diverges. Includes escalation
  trigger detection, quality frameworks, and audit trails.
metadata:
  jurisdiction: european-union
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Canned Responses (European Union)

> **Disclaimer**: This skill provides a framework for AI-assisted legal response
> generation under EU law. It does not constitute legal advice. All templated
> responses should be reviewed by a qualified legal professional licensed in the
> relevant Member State before sending, especially for regulated communications.
> Laws change; verify current applicability before relying on any provision
> described here. Statutory and regulatory references cited from memory carry
> hallucination risk — verify against authoritative sources (EUR-Lex, national
> gazette publications) before relying on them. Where this skill references EU
> law, Member State implementation may vary — always confirm the national
> transposition or supplementary legislation that applies to the specific
> situation.

## Purpose and Scope

This skill helps in-house legal teams operating in the European Union manage,
customize, and generate templated responses for common legal inquiries governed
by EU law. It identifies when a situation should NOT use a templated response
and instead requires individualized attention from qualified counsel.

This is the EU-specific variant of `legalcode-canned-responses`. It replaces
jurisdiction-agnostic markers with hardcoded EU law references. Where Member
State law varies (procedural rules, employment law, criminal law, insurance
law, privilege), it uses `[MEMBER STATE]` markers with guidance on what to
verify locally.

**Covers:**

- Template generation for 7 core response categories under EU law
- Escalation trigger detection (universal and category-specific, EU-adapted)
- Template creation, lifecycle management, and retirement workflows
- Customization guidelines for tone, jurisdiction, and audience
- Quality assurance frameworks with audit trails and variable validation
- Member State variation guidance where EU-level harmonization is incomplete

**Does not:**

- Provide legal advice or final legal opinions
- Replace counsel review for regulated or high-stakes communications
- Generate responses for novel or unprecedented situations
- Handle matters involving potential litigation without escalation
- Operate as a document management system (integrates with, does not replace)
- Cover UK GDPR — use `legalcode-canned-responses-uk` for the United Kingdom
- Substitute for Member State-specific legal analysis where national law applies

**Related skills:**

- `legalcode-canned-responses` — jurisdiction-agnostic base skill
- `legalcode-contract-review` — for contract clause analysis
- `legalcode-nda-triage` — for NDA screening and classification
- `gdpr-data-processing-addendum` — for GDPR Article 28 DPA drafting and review
- `ai-act-prohibited-practices-and-literacy-readiness` — for EU AI Act compliance

---

## Jurisdiction and Governing Law

This skill is specific to the **European Union** under the following primary
legal framework:

**Data protection:**

- Regulation (EU) 2016/679 (EU GDPR)
- ePrivacy Directive 2002/58/EC (as implemented by each Member State)
- Commission Implementing Decision (EU) 2021/914 (Standard Contractual Clauses)

**Civil procedure and cross-border jurisdiction:**

- Regulation (EU) 1215/2012 (Brussels I Recast) — jurisdiction and enforcement
  of judgments in civil and commercial matters
- Regulation (EC) 593/2008 (Rome I) — applicable law for contractual obligations
- Regulation (EC) 864/2007 (Rome II) — applicable law for non-contractual
  obligations
- Regulation (EU) 2020/1784 — cross-border service of documents

**Legal process and enforcement:**

- Directive 2014/41/EU (European Investigation Order)
- Regulation (EU) 655/2014 (European Account Preservation Order)
- [MEMBER STATE PROCEDURAL RULES] for domestic court procedures

**Electronic signatures:**

- Regulation (EU) 910/2014 (eIDAS) — qualified, advanced, and simple electronic
  signatures

**Corporate and supply chain compliance:**

- Corporate Sustainability Due Diligence Directive (CSDDD)
- Regulation (EU) 2024/... (Forced Labour Regulation)
- Regulation (EU) 2024/1689 (EU AI Act)
- Directive (EU) 2022/2555 (NIS2 Directive — cybersecurity)

**Insurance:**

- Directive 2009/138/EC (Solvency II)
- Directive (EU) 2016/97 (Insurance Distribution Directive)
- [MEMBER STATE INSURANCE LAW] for policy interpretation and claims procedure

**Criminal and anti-money laundering:**

- Directive (EU) 2018/1673 (6th Anti-Money Laundering Directive)
- Directive (EU) 2019/1937 (Whistleblower Protection Directive)
- [MEMBER STATE CRIMINAL LAW] for substantive criminal offenses and procedure

**Terminology conventions (EU English):**

- "Data controller" / "data processor" (Art. 4(7)-(8))
- "Supervisory authority" — not "regulator" generically (Art. 4(21))
- "Processing" (Art. 4(2)), "Data subject" (Art. 4(1)), "Personal data
  breach" (Art. 4(12))
- "Lead supervisory authority" — one-stop-shop mechanism (Art. 56)

**Key supervisory authorities** (the correct authority depends on the data
subject's Member State or the controller's main establishment):

- **CNIL** (France), **BfDI** (Germany, plus Landesdatenschutzbeauftragte),
  **DPC** (Ireland), **AEPD** (Spain), **Garante** (Italy), **AP**
  (Netherlands), **UODO** (Poland)

**Cross-border coordination:** EDPB for cross-border guidance; lead
supervisory authority under one-stop-shop (Art. 56); European Commission for
adequacy decisions (Art. 45) and SCCs.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The
workflow pauses when: the answer would change which template applies, the
applicable Member State is unclear, the lead supervisory authority must be
identified, escalation triggers require confirmation, multiple valid approaches
exist, or Member State law variation could affect content.

Use the **CLARIFY** pattern: present structured options with "Why this matters"
explanations. If the user has already provided the information, skip and
proceed.

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

**CLARIFY** — Before selecting or generating a template, gather essential context:

1. **Inquiry type**: What category does this inquiry fall into?
   - Options: Data Subject Request, Litigation Hold, Privacy Inquiry, Vendor
     Question, NDA Request, Legal Process, Insurance Notification, Other (describe)
   - _Why this matters_: Determines which template category and escalation
     triggers apply.

2. **Member State**: Which Member State's law governs this response (if any
   Member State-specific elements apply)?
   - Options: [List relevant Member States or ask user to specify]
   - _Why this matters_: Determines supervisory authority, procedural rules,
     employment law, privilege rules, and Member State-specific transpositions
     of EU directives.

3. **Supervisory authority**: If data protection-related, which supervisory
   authority has jurisdiction?
   - Options: Lead supervisory authority under Art. 56 GDPR, or the authority
     of the data subject's Member State
   - _Why this matters_: DSR responses must name the correct supervisory
     authority for the data subject to lodge a complaint.

4. **Audience**: Who is the recipient?
   - Options: Individual data subject, Business counterparty, Supervisory
     authority / regulator, Internal (employee/custodian), Opposing counsel,
     Other
   - _Why this matters_: Determines tone, formality level, and required
     disclosures.

5. **Urgency**: What is the timeline?
   - Options: Standard (use statutory deadline), Expedited (shorter than
     standard), Already overdue (remediation mode), No deadline (informational)
   - _Why this matters_: Determines whether extension notices are needed and
     response prioritization.

6. **Prior handling**: Has the team handled similar inquiries before?
   - Options: Yes — use existing template, Yes — but template needs update,
     No — novel situation, Unknown
   - _Why this matters_: Novel situations may require escalation rather than
     templating.

If any answer indicates a potential escalation trigger, proceed to Step 3 before
generating a response.

### Step 3: Check Escalation Triggers

Before generating ANY templated response, systematically check for escalation
triggers. If any trigger is present, do NOT generate a standard templated
response — instead, escalate per the protocol below.

#### Universal Escalation Triggers (Apply to All Categories)

- The matter involves potential litigation or regulatory investigation
- The inquiry is from a supervisory authority (CNIL, BfDI, DPC, AEPD, Garante,
  AP, UODO, or any other national DPA), the European Commission, the EDPB, or
  any other EU or national regulatory body
- The response could create a binding legal commitment or waiver
- The matter involves potential criminal liability
- Media attention is involved or likely
- The situation is unprecedented (no prior handling by the team)
- Multiple Member States are involved with conflicting national requirements
- The matter involves executive leadership, board members, or politically
  exposed persons
- Privilege considerations are complex or disputed — note that in-house counsel
  privilege is NOT recognized in EU competition law proceedings (Case C-550/07 P,
  _Akzo Nobel Chemicals and Akcros Chemicals v Commission_)
- The inquiry is from someone in active litigation or dispute with the
  organization
- Cross-border processing triggers one-stop-shop mechanism complexity

#### Category-Specific Escalation Triggers

**Data Subject Requests (DSRs — EU GDPR):**

- Request from or on behalf of a minor (Art. 8 GDPR — parental consent
  thresholds vary by Member State: 13-16 years)
- Request involves data subject to a litigation hold
- Requester is in active litigation or dispute with the organization
- Request is from an employee with an active HR matter, grievance, or
  investigation — note: [MEMBER STATE EMPLOYMENT LAW] governs works council
  consultation and employee monitoring rules
- Request scope is extraordinarily broad (potential fishing expedition — but
  note: supervisory authorities discourage blanket refusals on this basis)
- Request involves special category data (Art. 9 GDPR: health, biometric,
  genetic, racial or ethnic origin, political opinions, religious or
  philosophical beliefs, trade union membership, sexual orientation)
- Request involves criminal conviction or offense data (Art. 10 GDPR —
  processing only under official authority or [MEMBER STATE] authorization)
- Privilege analysis required — [MEMBER STATE PRIVILEGE RULES] apply
- Request involves cross-border transfer of personal data (adequacy decisions
  under Art. 45, or SCCs under Commission Decision 2021/914)
- Digital Services Act (DSA) obligations may interact with the response

**Litigation Holds / Document Preservation:**

- Potential criminal liability
- Unclear or disputed preservation scope
- Preservation conflicts with GDPR erasure obligations (Art. 17 right to
  erasure vs. litigation hold — Art. 17(3)(e) exemption for legal claims)
- Prior holds exist for related matters
- Custodian objects to the hold scope
- Cross-border preservation with conflicting Member State requirements
- Data localization laws restrict where preserved data can be stored or accessed
- [MEMBER STATE PROCEDURAL RULES] govern specific preservation obligations

**Vendor Questions:**

- Vendor is disputing contract terms
- Vendor is threatening litigation or termination
- Response could affect ongoing negotiation
- Question involves regulatory compliance
- CSDDD (Corporate Sustainability Due Diligence Directive) supply chain
  compliance concerns
- EU Forced Labour Regulation implications
- EU AI Act obligations for AI system providers or deployers (Regulation
  2024/1689)
- NIS2 Directive (Directive 2022/2555) cybersecurity compliance questions

**Legal Process (Court Orders / Member State Mechanisms):**

- **ALWAYS requires counsel review** — templates are starting points only,
  never final responses
- Privilege issues identified in responsive documents — [MEMBER STATE PRIVILEGE
  RULES] apply
- Third-party personal data involved (GDPR implications of disclosure)
- Cross-border production issues — Brussels I Recast (Regulation 1215/2012) for
  jurisdiction; Regulation 2020/1784 for service of documents
- European Investigation Order (Directive 2014/41/EU) received
- European Account Preservation Order (Regulation 655/2014) served
- Unreasonable timeline that may require application to court under [MEMBER
  STATE PROCEDURAL RULES]

**Insurance Notifications:**

- Late notification (potential coverage dispute)
- Claim may implicate multiple policies or coverage towers
- Reservation of rights letter received from insurer
- Coverage dispute anticipated
- Matter involves D&O, E&O, or cyber policies with complex notification
  requirements
- [MEMBER STATE INSURANCE LAW] governs policy interpretation — Solvency II
  (Directive 2009/138/EC) and Insurance Distribution Directive (2016/97/EU)
  provide EU-level framework only

#### When an Escalation Trigger is Detected

1. **Stop**: Do not generate a final templated response
2. **Alert**: Inform the user that an escalation trigger has been detected
3. **Explain**: Describe which trigger was detected and why it matters
4. **Recommend**: Suggest the appropriate escalation path (senior counsel,
   external counsel in the relevant Member State, specific team member,
   supervisory authority liaison)
5. **Offer**: Provide a DRAFT for counsel review, clearly marked:
   ```
   ============================================================
   DRAFT — FOR COUNSEL REVIEW ONLY — NOT TO BE SENT
   Escalation trigger detected: [trigger description]
   Recommended escalation: [path]
   ============================================================
   ```

### Step 4: Select or Create Template

If no escalation triggers are present, proceed to select the appropriate template
category and either:

- **Use existing template**: Select from the team's template library
- **Generate from framework**: Use the category frameworks below to generate a
  response
- **Create new template**: Follow the Template Creation Guide to establish a new
  template

### Step 5: Customize and Generate Response

Apply required customizations: fill all variable placeholders; adjust tone for
audience; insert EU-specific elements (GDPR articles, correct supervisory
authority for the data subject's Member State, one calendar month timeline,
SCCs for transfers, eIDAS signature type); verify deadline calculations (one
calendar month per Art. 12(3), not "30 days"); add [MEMBER STATE] markers
where national law must be verified.

### Step 6: Quality Verification

Run the Quality Framework before delivering: Citation Quality Gates (all 5
must pass), completeness check, writing standards, and escalation re-check.

### Step 7: Generate Glass Box Audit Entry

Create an internal audit record (retained in matter file, NOT sent to
recipient).

### Step 8: Deliver Response and Log Follow-Up

Provide the final response with: required follow-up actions, deadlines created
by the response, and matter tracking flags.

---

## Response Categories

### 1. Data Subject Requests (DSRs — EU GDPR)

**Legal framework**: Regulation (EU) 2016/679, Articles 12-22. Data subjects
have the right of access (Art. 15), rectification (Art. 16), erasure (Art. 17),
restriction of processing (Art. 18), data portability (Art. 20), and objection
(Art. 21). Automated decision-making rights under Art. 22. Controllers must
respond within **one calendar month** of receipt (Art. 12(3)), extendable by
**two further months** for complex or numerous requests.

**Sub-categories:**

- Acknowledgment of receipt
- Identity verification request (proportionate to data sensitivity)
- Fulfillment response (access, deletion, rectification, portability,
  restriction, objection)
- Partial exemption/redaction with explanation
- Full denial with explanation (manifestly unfounded or excessive under
  Art. 12(5), or exemption applies)
- Extension notification (complex request requiring additional time —
  Art. 12(3))

**Key template elements:**

- Reference to EU GDPR (Regulation 2016/679) — not just "GDPR" unqualified
- Specific timeline: **one calendar month** from receipt (Art. 12(3)),
  extendable by two further months for complex requests
- Identity verification requirements (proportionate to data sensitivity)
- Lawful basis for processing (Art. 6) if relevant to the response
- Special categories under Art. 9 flagged if applicable
- Rights of the data subject, including:
  - Right to lodge complaint with the **supervisory authority of the data
    subject's Member State** (name the specific authority — e.g., CNIL for
    France, BfDI for Germany, DPC for Ireland, AEPD for Spain, Garante for
    Italy, AP for Netherlands, UODO for Poland)
  - Right to an effective judicial remedy (Art. 79 GDPR)
- Exemptions applied and legal basis (cite specific GDPR provisions and
  [MEMBER STATE] implementing legislation where applicable)
- Contact information for DPO (if designated under Art. 37-39) or privacy team
- DPIA reference (Art. 35) if processing is relevant to DPIA scope

**Example template structure — DSR Acknowledgment:**

```
Subject: Your Data [Access/Deletion/Rectification/Portability] Request —
  Reference {{request_id}}

Dear {{requester_name}},

Thank you for your request dated {{request_date}} to {{request_type}} your
personal data. We are processing your request under the General Data Protection
Regulation (EU) 2016/679.

{{IF identity_verification_needed}}
Before we can process your request, we need to verify your identity. Please
provide {{verification_requirements}}.
{{ENDIF}}

We will respond substantively within one calendar month of
{{receipt_date_or_verification_date}} (Article 12(3) GDPR). If we need
additional time due to the complexity or number of requests, we will notify
you within that period and explain the reasons for the delay.

If you have questions, please contact our Data Protection Officer at
{{dpo_contact}}.

You have the right to lodge a complaint with {{supervisory_authority_name}}
({{supervisory_authority_contact}}) if you are not satisfied with how we
handle your request. You also have the right to an effective judicial remedy
under Article 79 of the GDPR.

{{signature_block}}
```

**Example template structure — DSR Partial Exemption:**

```
Subject: Response to Your Data Request — Reference {{request_id}}

Dear {{requester_name}},

Further to your request dated {{request_date}}, please find enclosed the
personal data we hold about you.

We have applied the following exemption(s) to certain data:

{{FOR EACH exemption}}
- **Exemption**: {{exemption_name}} (Regulation (EU) 2016/679,
  {{provision_reference}})
- **Scope**: {{description_of_data_withheld}}
- **Basis**: {{reason_exemption_applies}}
{{ENDFOR}}

The enclosed data represents all personal data we hold about you, subject to
the exemptions noted above.

You have the right to:
- Lodge a complaint with {{supervisory_authority_name}}
  ({{supervisory_authority_contact}})
- Seek an effective judicial remedy under Article 79 of the GDPR

{{signature_block}}
```

### 2. Litigation Holds / Document Preservation Notices

**Legal framework**: Document preservation is governed by [MEMBER STATE
PROCEDURAL RULES] — there is no single EU-wide obligation. For cross-border
disputes, Brussels I Recast (Regulation 1215/2012) determines jurisdiction,
and preservation obligations may arise under multiple Member States' laws.
GDPR Art. 17(3)(e) exempts erasure where processing is necessary for legal
claims.

**Sub-categories:**

- Initial preservation notice to custodians
- Preservation reminder / periodic reaffirmation
- Scope modification notice (expansion or narrowing)
- Release of preservation obligations

**Key template elements:**

- Matter name and reference number
- Clear preservation obligations (what must be preserved)
- Scope of preservation (date range, data types, systems, custodians,
  communication types)
- Prohibition on destruction, alteration, or disposal of potentially relevant
  materials
- Reference to [MEMBER STATE PROCEDURAL RULES] and consequences of
  non-compliance
- Privilege marking — [MEMBER STATE PRIVILEGE RULES] (note: in-house counsel
  privilege is NOT recognized in EU competition law proceedings per _Akzo Nobel_)
- Contact for questions
- Acknowledgment requirement with deadline
- GDPR Art. 17(3)(e) exemption noted where preservation overrides erasure
  requests

**Example template structure — Litigation Hold Notice:**

```
Subject: DOCUMENT PRESERVATION NOTICE — {{matter_name}} — Action Required

[MEMBER STATE PRIVILEGE MARKING]

Dear {{custodian_name}},

You are receiving this notice because you may hold documents, communications,
or data relevant to the matter referenced above.

PRESERVATION OBLIGATION:
Effective immediately, you must preserve all documents and electronically
stored information relating to:
- Subject matter: {{hold_scope}}
- Date range: {{start_date}} to present
- Document types: {{document_types}}

This includes but is not limited to: emails, letters, memoranda, file notes,
reports, spreadsheets, presentations, instant messages, text messages,
voicemails, calendar entries, and any other records in any format (paper or
electronic) including drafts, notes, and metadata.

YOU MUST NOT delete, destroy, modify, move, or discard any potentially
relevant materials. This includes:
- Do not delete emails (including from deleted items/trash folders)
- Do not overwrite or modify electronic files
- Do not destroy paper documents
- Do not alter any records, including metadata
- Suspend any automated deletion or archiving processes for in-scope data

[MEMBER STATE PROCEDURAL RULES: Insert consequences of non-compliance under
applicable national law — e.g., adverse inferences, procedural sanctions,
contempt of court equivalent]

Please acknowledge receipt of this notice by replying to this email by
{{acknowledgment_deadline}}.

Contact {{legal_contact}} immediately if you have questions about what should
be preserved or if you become aware of relevant materials at risk.

{{signature_block}}
```

**Terminology note**: Litigation terminology varies by Member State (e.g.,
French procedure civile, German Zivilprozessordnung). For cross-border matters,
reference Brussels I Recast (Regulation 1215/2012) and Regulation 2020/1784.

### 3. Privacy Inquiries

**Legal framework**: EU GDPR (Regulation 2016/679) and ePrivacy Directive
2002/58/EC (as implemented by each Member State).

**Sub-categories:** Cookie/tracking inquiries (ePrivacy Directive 2002/58/EC,
as transposed by [MEMBER STATE]), privacy notice questions (Arts. 13-14),
data sharing inquiries, children's data (Art. 8 — age threshold 13-16 by
Member State; DSA requirements), cross-border transfers (Arts. 44-49,
adequacy decisions Art. 45, SCCs Decision 2021/914), supervisory authority
complaint responses.

**Key template elements:**

- Privacy notice references (Arts. 13-14), lawful basis (Art. 6)
- ePrivacy Directive 2002/58/EC for e-marketing, cookies, communications
  confidentiality
- DPO contact (Arts. 37-39), complaint rights with correct supervisory
  authority named

### 4. Vendor Legal Questions

**Legal framework**: Contract law varies by [MEMBER STATE CONTRACT LAW]. Rome I
Regulation (593/2008) for applicable law in cross-border contracts.

**Sub-categories:** Contract status inquiry, amendment request, compliance
certification (ISO 27001, SOC 2), audit request, insurance certificate, supply
chain compliance (CSDDD, EU Forced Labour Regulation, EU AI Act provider/deployer
obligations, NIS2 cybersecurity requirements).

**Key template elements:**

- Reference to applicable agreement (name, date, parties)
- Specific response, caveats, next steps, and timeline
- Compliance statement references (CSDDD, EU AI Act, NIS2) where applicable
- GDPR Art. 28 data processing requirements if vendor processes personal data

### 5. NDA Requests

**Legal framework**: Contract law varies by Member State — use [MEMBER STATE
CONTRACT LAW]. Rome I Regulation (593/2008) for applicable law. eIDAS
Regulation (910/2014) for electronic signatures.

**Sub-categories:** Sending standard form NDA, accepting counterparty NDA
(with/without markup), declining NDA request, NDA renewal/extension.

**Key template elements:**

- Purpose of the NDA (subject matter of contemplated disclosure)
- Governing law and dispute resolution — specify Member State law; Rome I
  determines applicable law absent a choice-of-law clause
- Execution instructions: eIDAS QES has handwritten-signature equivalence
  across all Member States; AES widely accepted; simple electronic signatures
  may suffice but vary by [MEMBER STATE CONTRACT LAW]. Notarization/witnessing
  per [MEMBER STATE CONTRACT LAW]
- Timeline expectations and confidentiality period

### 6. Legal Process (Court Orders / European Instruments / Member State Mechanisms)

**Legal framework**: EU-level instruments: European Investigation Order
(Directive 2014/41/EU, criminal); European Account Preservation Order
(Regulation 655/2014, civil debt); cross-border service of documents
(Regulation 2020/1784); Brussels I Recast (Regulation 1215/2012, jurisdiction).
Member State-specific mechanisms (domestic court orders, witness requirements,
document production) are governed by [MEMBER STATE PROCEDURAL RULES].

**Sub-categories:** Acknowledgment of receipt, objection letter, extension
request, compliance cover letter, privilege log transmittal.

**Key template elements:**

- Court/agency reference, case name, case/claim number
- Objections per [MEMBER STATE PROCEDURAL RULES]; privilege per [MEMBER STATE
  PRIVILEGE RULES]
- Preservation confirmation, compliance timeline, reservation of rights
- GDPR implications of disclosing third-party personal data

**Critical note**: Responses to compulsory legal process ALWAYS require
individualized counsel review. Templates are starting frameworks only.
Non-compliance may constitute contempt or equivalent under [MEMBER STATE
PROCEDURAL RULES].

### 7. Insurance Notifications

**Legal framework**: Insurance law is primarily [MEMBER STATE INSURANCE LAW].
EU-level framework: Solvency II (2009/138/EC) for prudential rules; Insurance
Distribution Directive (2016/97/EU) for distribution. Notification requirements
and policy interpretation are governed by [MEMBER STATE INSURANCE LAW].

**Sub-categories:** Initial claim/circumstance notification, supplemental
information, response to reservation of rights, D&O/E&O/Cyber notifications.

**Key template elements:**

- Policy number, insurer, broker, coverage period
- Matter description and timeline of events
- Specific policy notification clause quoted
- Coverage confirmation request, without-prejudice reservation
- [MEMBER STATE INSURANCE LAW] for notification interpretation rules

---

## Template Management Framework

### Template Organization

Templates should be organized by category and maintained in the team's document
management system. Each template must include: Category, Template name, Version,
Last reviewed date, Approved by (counsel name), Applicable legislation (EU
regulation and Member State law), Member State coverage, Supervisory authority
(if data protection template), Use case, Escalation triggers, Required
variables, Template body, and Follow-up actions.

### Template Lifecycle

1. **Creation**: Draft based on current EU law, EDPB guidance, supervisory
   authority guidance, and team input
2. **Review**: Counsel review and approval
3. **Publication**: Add to template library with full metadata
4. **Use**: Generate responses using the template
5. **Feedback**: Track modifications during use to identify improvement needs
6. **Update**: Revise when EU regulations, EDPB guidance, supervisory authority
   decisions, or CJEU case law changes
7. **Retirement**: Archive templates no longer applicable

---

## Customization Guidelines

### Required Customization

Every templated response MUST be customized with:

- Correct names, dates, and reference numbers
- Specific facts of the situation (not generic placeholders)
- EU GDPR (Regulation 2016/679) cited with specific article references
- Correct supervisory authority for the data subject's Member State (named
  with contact details)
- Correct response deadlines — one calendar month (Art. 12(3)), not "30 days"
- DPO contact information (Arts. 37-39) where applicable
- [MEMBER STATE] markers where national law must be verified

### Tone Adjustment Matrix

| Dimension        | Options                                     | Guidance                                     |
| ---------------- | ------------------------------------------- | -------------------------------------------- |
| **Audience**     | Internal / External / Supervisory authority | Supervisory authority = most formal, precise |
| **Relationship** | New / Existing / Adversarial                | Adversarial = more guarded, no admissions    |
| **Sensitivity**  | Routine / Contentious / Investigation       | Investigation = counsel review required      |
| **Urgency**      | Standard / Expedited / Overdue              | Overdue = acknowledge delay, explain         |

### EU-Specific Checks

Before sending any response, verify:

- [ ] EU GDPR (Regulation 2016/679) cited — not just "GDPR" unqualified
      (which may be confused with UK GDPR)
- [ ] Timelines use "one calendar month" (Art. 12(3)), not "30 days"
- [ ] Correct supervisory authority named for the data subject's Member State
- [ ] EU English terminology used: data controller, data processor, supervisory
      authority, processing, data subject, personal data breach
- [ ] Correct Member State court / tribunal references where applicable
- [ ] Privilege marking uses [MEMBER STATE PRIVILEGE RULES] convention
- [ ] eIDAS Regulation cited for electronic signature requirements
- [ ] SCCs (Commission Decision 2021/914) referenced for international
      transfers outside the EEA
- [ ] Member State-specific law marked with [MEMBER STATE] where
      harmonization is incomplete

---

## Quality Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                                                                                                                                                                                        | Fail Action                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Source**     | Every regulatory reference cites both the EU-level instrument AND the specific article/section/provision. Where Member State implementation law is relevant, cite the national transposition or supplementary legislation (or mark [MEMBER STATE — VERIFY]) | Add citation or mark "[VERIFY]"                                               |
| **Format**     | Citations use correct EU format: "Regulation (EU) 2016/679, Article 15" or "Directive 2002/58/EC, Article 5(3)" — not informal shorthand                                                                                                                    | Fix format                                                                    |
| **Currency**   | Cited provisions, EDPB guidance, and supervisory authority decisions confirmed current. CJEU case law checked for recent developments                                                                                                                       | Flag "[CHECK CURRENCY]"                                                       |
| **Domain**     | EU English terminology throughout. No UK-specific terms (ICO, DPA 2018, PECR) in EU responses. No US terms (subpoena, discovery, attorney-client privilege)                                                                                                 | Fix terminology                                                               |
| **Confidence** | If template is being stretched beyond its designed use case, or if Member State variation creates uncertainty, flag it                                                                                                                                      | Add "[COUNSEL TO REVIEW — template adapted]" or "[MEMBER STATE LAW — VERIFY]" |

### Self-Interrogation for High-Stakes Responses

For responses involving supervisory authorities, legal process, or potential
litigation, apply this 3-pass review:

**Pass 1 — Completeness**: All required elements present? Data subject rights
(Arts. 15-22) mentioned? Correct supervisory authority named? Deadlines
correctly calculated?

**Pass 2 — Accuracy**: EU regulation citations correct and current? EU
terminology used (not UK/US)? No inadvertent admissions or waivers? Member
State elements correctly identified?

**Pass 3 — Appropriateness**: Is a template appropriate, or should this be
escalated? All triggers checked? Would qualified counsel approve sending this?

### Confidence Scoring

| Level        | Range     | Meaning                                                | Action                         |
| ------------ | --------- | ------------------------------------------------------ | ------------------------------ |
| **Definite** | 0.95-1.0  | Standard template, routine matter, single Member State | Send after standard review     |
| **High**     | 0.80-0.94 | Minor customization, known pattern                     | Send with quality check        |
| **Probable** | 0.60-0.79 | Significant adaptation or multiple Member States       | Senior review before sending   |
| **Possible** | 0.40-0.59 | Template being stretched or Member State law unclear   | Counsel review required        |
| **Unlikely** | 0.0-0.39  | Template not appropriate                               | Do not use template — escalate |

### Glass Box Audit Trail

Every generated response MUST include an internal Glass Box audit record. This
is retained in the matter file — NOT sent to the recipient.

```yaml
glass_box:
  inquiry_type: "[DSR / Litigation hold / Privacy inquiry / Vendor / NDA / Legal process / Insurance]"
  template_used: "[Template name and version, or 'Generated from framework']"
  template_modified: "Yes / No — if yes, [what was changed and why]"
  jurisdiction: "European Union — [Member State if applicable]"
  member_state: "[Applicable Member State or 'EU-wide']"
  supervisory_authority: "[Name of applicable supervisory authority]"
  regulations_applied:
    - "Regulation (EU) 2016/679 (GDPR), Article [X]"
    - "[Member State] implementing legislation, [section/article] — or [MEMBER STATE — VERIFY]"
  citations_verified:
    - "GDPR Art. 15 — VERIFIED / UNVERIFIED"
    - "[Member State law] — VERIFIED / UNVERIFIED / [MEMBER STATE — VERIFY]"
  deadline_calculation:
    received: "[YYYY-MM-DD]"
    deadline: "[YYYY-MM-DD]"
    basis: "One calendar month from receipt (GDPR Art. 12(3))"
  exemptions_applied:
    - "[Exemption] — [Legal basis, e.g., GDPR Art. 17(3)(e)] — [Applied to: description]"
  escalation_triggers_checked:
    - "[Trigger 1] — Present / Not present"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  quality_gates_passed: "5/5 or [list failures]"
  member_state_verification_needed:
    - "[Area requiring Member State law check] — [MEMBER STATE — VERIFY]"
  reviewer: "[Name or 'AI-assisted — requires counsel review before sending']"
  follow_up_actions:
    - "[Action 1]"
```

---

## Writing Standards

Templated legal responses must be clear, professional, and understandable by
their intended audience. Apply these standards to every response.

### Three-Pass Editing

**Pass 1 — Structure**: Does the response answer the inquiry? Is information
in logical order? Is anything missing or unnecessary?

**Pass 2 — Clarity**: Can the recipient understand this without legal training?
Replace passive constructions with active voice. Remove ambiguity.

**Pass 3 — Concision**: Cut padding and qualifiers. Replace jargon. Target
20-30% word count reduction from first draft.

### Specific Rules

- **EU English conventions**: Use EU institutional English ("supervisory
  authority" not "regulator," "data subject" not "consumer"). Spelling follows
  EU English (typically British: organisation, colour, programme, defence).
- **Active voice**: "We received your request on 15 January" not "Your request
  was received on 15 January."
- **Name the actor**: "The supervisory authority can investigate" not "An
  investigation may be commenced."
- **Plain language for data subjects**: Data subjects may have no legal
  knowledge and may not have the response language as their first language —
  use simple, clear sentence structures.
- **Formal but clear for supervisory authorities**: Factual, well-organized
  responses. No advocacy language in factual submissions.
- **Precise for preservation notices**: "You must not delete emails" is better
  than "Please ensure electronic communications are preserved."
- **No hidden complexity**: Obscure language risks supervisory authority
  enforcement. The EDPB emphasizes transparency (Arts. 12-14 GDPR).
- **Multilingual awareness**: Some Member States require responses in the
  national language. Consider bilingual responses where appropriate. [MEMBER
  STATE] language requirements may apply.

### Quality Gates Before Sending

1. Would a non-lawyer recipient understand this response?
2. Are all EU regulation references correct and current?
3. Is the deadline one calendar month (Art. 12(3)), not "30 days"?
4. Is the correct supervisory authority named with contact details?
5. Has every escalation trigger been checked?
6. Is this response appropriate for the specific facts?
7. Have all {{placeholders}} been replaced with actual values?
8. Are [MEMBER STATE] markers included where national law must be verified?

---

## Anti-Patterns

What NOT to do with templated legal responses under EU law:

1. **Sending a template without customization** — A response with
   "{{requester_name}}" or other unfilled variables is worse than no response.
   Every variable must be filled. Every response must be reviewed against the
   specific facts.

2. **Using incorrect timeline formulations** — "30 days" and "one calendar
   month" are different deadlines. One calendar month from 31 January is
   28/29 February, not 2 March. Art. 12(3) GDPR requires "one calendar month."
   This error has triggered supervisory authority enforcement.

3. **Citing "GDPR" without specifying EU or UK** — Citing "GDPR" unqualified
   is ambiguous. In an EU context, cite "Regulation (EU) 2016/679" or "EU
   GDPR." Failing to distinguish from UK GDPR creates legal uncertainty and
   may be incorrect if the data subject is in a different jurisdiction.

4. **Applying exemptions without documentation** — "We have applied an
   exemption to some data" is insufficient. Each exemption must be applied to
   specific data with a documented reason citing the specific GDPR provision
   (e.g., Art. 17(3)(e)), retained in the matter file for potential
   supervisory authority inquiry.

5. **Vague preservation notices** — A litigation hold that politely asks
   custodians to "please keep relevant documents" does not convey the severity.
   Explain the consequences of non-compliance under [MEMBER STATE PROCEDURAL
   RULES] (sanctions, adverse inferences, contempt equivalents).

6. **Templated responses to supervisory authorities** — Never send a template
   response to a supervisory authority (CNIL, BfDI, DPC, AEPD, Garante, AP,
   UODO, or any other DPA) without individualized counsel review. Supervisory
   authorities recognize boilerplate, and it signals the organization is not
   taking the matter seriously.

7. **Omitting mandatory disclosures** — Forgetting to include supervisory
   authority complaint rights in DSR responses is a compliance failure under
   Art. 12 GDPR, not just a drafting error. The specific authority for the
   data subject's Member State must be named with contact details.

8. **Using wrong jurisdiction's terminology** — "Subpoena," "discovery,"
   "attorney-client privilege" are US terms. "Witness summons," "disclosure,"
   "legal professional privilege" are UK terms. EU responses should use EU
   terminology: "supervisory authority" (not "regulator"), "data controller"
   (not "data holder"), "processing" (not "handling"). Each Member State also
   has its own procedural terminology — use the correct terms for the
   applicable national jurisdiction.

9. **Missing deadlines without extension notice** — If you need more time
   for a DSR, you must notify the data subject within the original one
   calendar month period and explain the reasons (Art. 12(3) GDPR). Silently
   missing the deadline is a GDPR compliance breach.

10. **Fire-and-forget responses** — Every response needs follow-up actions:
    log the response, schedule follow-up deadlines, update the matter file,
    close the request only when fully resolved.

11. **Ignoring escalation triggers** — Proceeding with a templated response
    when an escalation trigger is present. The escalation check exists because
    some situations cannot be safely handled with templates.

12. **Template scope creep** — Using a template designed for one situation
    (e.g., simple DSR acknowledgment) for a different situation (e.g., complex
    cross-border DSR with special category data and multiple exemptions). Each
    template has a designed use case — respect its boundaries.

13. **Copying without understanding** — Using template language without
    understanding why it exists. If you cannot explain why each element of
    the response is there, you should not be sending it.

14. **Inconsistent variable naming** — Using {{name}}, {{requester_name}},
    {{data_subject}}, and {{individual}} interchangeably in the same template
    library. Standardize variable names across all templates.

15. **No version control** — Failing to track template versions, leading to
    outdated templates being used after GDPR guidance updates, CJEU rulings,
    or supervisory authority enforcement decisions. Every template needs a
    version number and last-reviewed date.

16. **Privilege marking errors** — Using the wrong privilege assertion for the
    Member State, or failing to mark privileged communications appropriately.
    Note that in-house counsel privilege is NOT recognized in EU competition
    law proceedings (_Akzo Nobel_). [MEMBER STATE PRIVILEGE RULES] govern
    privilege in other contexts. Errors can waive privilege.

17. **Assuming supervisory authority** — Every DSR response must name the
    supervisory authority for the data subject's Member State, not a generic
    "supervisory authority" reference or the authority of the controller's
    establishment. Verify which authority is correct based on the data
    subject's location and the one-stop-shop mechanism (Art. 56 GDPR).

18. **Ignoring Member State implementation differences** — EU directives
    (ePrivacy, Whistleblower Protection, 6AMLD) are transposed differently
    by each Member State. Treating directive-based obligations as uniform
    across the EU without checking national implementation is an error.

19. **Conflating EU GDPR with UK GDPR** — After Brexit, the UK operates
    under UK GDPR and DPA 2018, which may diverge from EU GDPR over time.
    Templates for EU data subjects must cite EU GDPR (Regulation 2016/679),
    not UK legislation.

---

## External Tool Integration

### legalcode-mcp Integration

If **legalcode-mcp** is connected, use it for:

- Verifying current EU regulatory text and EDPB guidance
- Checking recent CJEU rulings and supervisory authority enforcement decisions
- Validating deadline calculations against current law
- Researching Member State-specific requirements and implementations

**With legalcode-mcp connected:**

- Mark verified citations as `VERIFIED` in the Glass Box audit trail
- Update templates based on recent EDPB guidance or supervisory authority
  decisions

**Without legalcode-mcp:**

- Proceed with template generation
- Mark regulatory citations as `[VERIFY]` where currency is uncertain
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Document Management Integration

Templates should integrate with the organization's matter management system
(audit trail), document management system (versioning), email system
(delivery), and deadline tracking system (follow-up scheduling).

---

## Output Format Template

When generating a response, structure the output as follows:

```markdown
## Generated Response

**Category**: [Response category]
**Template**: [Template name and version, or "Generated from framework"]
**Jurisdiction**: European Union — [Member State if applicable]
**Supervisory Authority**: [Applicable DPA]
**Confidence**: [HIGH / MEDIUM / LOW]

---

### Response Text

[The actual response to be sent, fully customized with all variables filled]

---

### Internal Notes (Do Not Send)

**Deadline**: [Calculated deadline — one calendar month per Art. 12(3) GDPR]
**Escalation triggers checked**: [List with Present / Not present]
**Member State verification needed**: [Any [MEMBER STATE] items]
**Required follow-up actions**: [List with deadlines]
**Glass Box Audit**: [Full glass_box YAML block]

---

### Quality Verification

| Gate                                 | Status      |
| ------------------------------------ | ----------- |
| Source citations (EU + Member State) | PASS / FAIL |
| Citation format (EU standard)        | PASS / FAIL |
| Currency (EDPB, CJEU, DPA decisions) | PASS / FAIL |
| Terminology (EU English)             | PASS / FAIL |
| Confidence                           | PASS / FAIL |

**Ready to send**: [Yes — after counsel review / No — escalation required /
No — [MEMBER STATE] verification needed first]
```

---

## Localization Notes

This skill covers the **EU GDPR framework**. Key localization points:

1. **Regulation vs. directive**: EU regulations (GDPR) apply uniformly.
   Directives (ePrivacy, Whistleblower Protection, 6AMLD) are transposed
   differently by each Member State. [MEMBER STATE] markers cover all areas
   where national law may diverge.
2. **Supervisory authority**: Each DSR response must name the authority for the
   data subject's Member State. The one-stop-shop mechanism (Art. 56) governs
   lead authority for cross-border processing, but data subjects retain the
   right to complain to their own Member State's authority.
3. **Language**: Some Member States require correspondence in the national
   language. Consider whether responses should be bilingual.
4. **Procedural rules**: Litigation procedure, preservation obligations, and
   court terminology vary by Member State — always verify [MEMBER STATE
   PROCEDURAL RULES].
5. **Privilege**: In-house counsel privilege is not recognized in EU competition
   law proceedings (_Akzo Nobel_). For other proceedings, [MEMBER STATE
   PRIVILEGE RULES] apply and vary significantly.
6. **Companion skills**: Use `legalcode-canned-responses-uk` for the UK;
   `legalcode-canned-responses` for the jurisdiction-agnostic framework.

---

## Provenance

- **Original synthesis**: Legalcode (2026-02-27)
- **Base skill**: `skills/general/workflows/legalcode-canned-responses/SKILL.md`
- **Reference skills analyzed**:
  - `imported-uk-legal-plugins--skills-uk-legal-canned-responses` (quality framework)
  - `gdpr-data-processing-addendum` (GDPR framework reference)
  - `ai-act-prohibited-practices-and-literacy-readiness` (EU law format reference)
- **EU legal sources** (all via EUR-Lex): Regulation 2016/679 (GDPR), Directive
  2002/58/EC (ePrivacy), Decision 2021/914 (SCCs), Regulation 1215/2012
  (Brussels I Recast), Regulation 593/2008 (Rome I), Regulation 864/2007
  (Rome II), Regulation 910/2014 (eIDAS), Directive 2014/41/EU (EIO),
  Regulation 655/2014 (EAPO), Regulation 2020/1784 (Service of Documents),
  Directive 2009/138/EC (Solvency II), Directive 2016/97/EU (IDD), Directive
  2022/2555 (NIS2), Regulation 2024/1689 (AI Act), Directive 2019/1937
  (Whistleblower), Case C-550/07 P _Akzo Nobel v Commission_
- **License**: Apache-2.0 (consistent with source skills)
