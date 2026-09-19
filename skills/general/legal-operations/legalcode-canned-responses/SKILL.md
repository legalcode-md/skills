---
name: legalcode-canned-responses
description: Generate, manage, and customize templated responses for routine legal inquiries — data subject
  requests (DSRs/DSARs), litigation holds, privacy inquiries, vendor questions, NDA requests, legal process
  (subpoenas/witness summons), and insurance notifications. Use when responding to routine legal questions,
  managing response template libraries, creating new templates, or identifying when a situation requires
  individualized counsel attention rather than a templated response. Jurisdiction-agnostic with localization
  markers. Includes escalation trigger detection, quality frameworks, and audit trails.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Canned Responses

> **Disclaimer**: This skill provides a framework for AI-assisted legal response
> generation. It does not constitute legal advice. All templated responses should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> sending, especially for regulated communications. Laws change; verify current
> applicability before relying on any provision described here. Statutory and regulatory
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill helps in-house legal teams manage, customize, and generate templated responses
for common legal inquiries. It identifies when a situation should NOT use a templated
response and instead requires individualized attention from qualified counsel.

**Covers:**

- Template generation for 7 core response categories
- Escalation trigger detection (universal and category-specific)
- Template creation, lifecycle management, and retirement workflows
- Customization guidelines for tone, jurisdiction, and audience
- Quality assurance frameworks with audit trails
- Variable placeholder management and validation

**Does not:**

- Provide legal advice or final legal opinions
- Replace counsel review for regulated or high-stakes communications
- Generate responses for novel or unprecedented situations
- Handle matters involving potential litigation without escalation
- Operate as a document management system (integrates with, does not replace)

**Related skills:**

- `legalcode-contract-review` — for contract clause analysis
- `legalcode-nda-triage` — for NDA screening and classification
- Jurisdiction-specific variants (create as needed for localized response requirements)

---

## Jurisdiction and Governing Law

This skill is **jurisdiction-agnostic** by default. It provides a universal framework that
must be localized for each jurisdiction where it is deployed.

**[JURISDICTION-SPECIFIC]** markers throughout indicate where local law, terminology,
timelines, or regulatory requirements must be inserted. When generating responses:

1. Identify the applicable jurisdiction (ask if unclear)
2. Replace generic references with jurisdiction-specific citations
3. Adjust timelines to match local legal requirements
4. Use jurisdiction-appropriate legal terminology
5. Include jurisdiction-specific rights information where required

**Common localization points:**

- Data protection: EU GDPR vs UK GDPR vs CCPA vs LGPD vs POPIA vs PIPEDA
- Litigation: Discovery (US) vs Disclosure (UK) vs local procedural rules
- Privilege: Attorney-client (US) vs Legal Professional Privilege (UK) vs local equivalents
- Legal process: Subpoena (US) vs Witness Summons (UK) vs local mechanisms
- Timelines: "30 days" vs "one calendar month" vs jurisdiction-specific periods

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change which template category applies
- The applicable jurisdiction is unclear
- Escalation trigger detection requires user confirmation
- Multiple valid response approaches exist
- Tone or audience calibration is needed

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

**CLARIFY** — Before selecting or generating a template, gather essential context:

1. **Inquiry type**: What category does this inquiry fall into?
   - Options: Data Subject Request, Litigation Hold, Privacy Inquiry, Vendor Question,
     NDA Request, Legal Process, Insurance Notification, Other (describe)
   - _Why this matters_: Determines which template category and escalation triggers apply.

2. **Jurisdiction**: Which jurisdiction's law governs this response?
   - Options: [List common jurisdictions or ask user to specify]
   - _Why this matters_: Determines timelines, terminology, regulatory citations, and
     mandatory elements (e.g., supervisory authority complaint rights).

3. **Audience**: Who is the recipient?
   - Options: Individual data subject, Business counterparty, Regulator/government,
     Internal (employee/custodian), Opposing counsel, Other
   - _Why this matters_: Determines tone, formality level, and required disclosures.

4. **Urgency**: What is the timeline?
   - Options: Standard (use statutory deadline), Expedited (shorter than standard),
     Already overdue (remediation mode), No deadline (informational)
   - _Why this matters_: Determines whether extension notices are needed and response
     prioritization.

5. **Prior handling**: Has the team handled similar inquiries before?
   - Options: Yes — use existing template, Yes — but template needs update,
     No — novel situation, Unknown
   - _Why this matters_: Novel situations may require escalation rather than templating.

If any answer indicates a potential escalation trigger, proceed to Step 3 before
generating a response.

### Step 3: Check Escalation Triggers

Before generating ANY templated response, systematically check for escalation triggers.
If any trigger is present, do NOT generate a standard templated response — instead,
escalate per the protocol below.

#### Universal Escalation Triggers (Apply to All Categories)

- The matter involves potential litigation or regulatory investigation
- The inquiry is from a regulator, government agency, or law enforcement
- The response could create a binding legal commitment or waiver
- The matter involves potential criminal liability
- Media attention is involved or likely
- The situation is unprecedented (no prior handling by the team)
- Multiple jurisdictions are involved with conflicting requirements
- The matter involves executive leadership, board members, or politically exposed persons
- Privilege considerations are complex or disputed
- The inquiry is from someone in active litigation or dispute with the organization

#### Category-Specific Escalation Triggers

**Data Subject Requests (DSRs/DSARs)**:

- Request from or on behalf of a minor
- Request involves data subject to a litigation hold
- Requester is in active litigation or dispute with the organization
- Request is from an employee with an active HR matter, grievance, or investigation
- Request scope is extraordinarily broad (potential fishing expedition)
- Request involves special category / sensitive personal data (health, biometric, genetic,
  religious beliefs, political opinions, sexual orientation, trade union membership)
- Request involves criminal conviction or offense data
- Privilege analysis is required for responsive documents
- [JURISDICTION-SPECIFIC: Add local escalation triggers, e.g., Age-Appropriate Design
  Code implications for UK, FERPA for US education records, HIPAA for US health data]

**Litigation Holds / Document Preservation**:

- Potential criminal liability
- Unclear or disputed preservation scope
- Preservation conflicts with regulatory deletion requirements (e.g., data subject erasure
  request vs. litigation hold)
- Prior holds exist for related matters
- Custodian objects to the hold scope
- Cross-border preservation obligations with conflicting legal requirements
- Data localization laws restrict where preserved data can be stored or accessed

**Vendor Questions**:

- Vendor is disputing contract terms
- Vendor is threatening litigation or termination
- Response could affect ongoing negotiation
- Question involves regulatory compliance (not just contract interpretation)
- [JURISDICTION-SPECIFIC: Add local compliance requirements, e.g., Modern Slavery Act
  for UK, supply chain due diligence laws for Germany/France]

**Legal Process (Subpoenas / Witness Summons / Court Orders)**:

- **ALWAYS requires counsel review** — templates are starting points only, never final
- Privilege issues identified in responsive documents
- Third-party personal data involved (data protection implications of disclosure)
- Cross-border production issues (requested documents held in another jurisdiction)
- Unreasonable timeline that may require application to court
- [JURISDICTION-SPECIFIC: Add local process types, e.g., Norwich Pharmacal orders for UK,
  grand jury subpoenas for US, European Investigation Orders for EU]

**Insurance Notifications**:

- Late notification (potential coverage dispute)
- Claim may implicate multiple policies or coverage towers
- Reservation of rights letter received from insurer
- Coverage dispute anticipated
- Matter involves D&O, E&O, or cyber policies with complex notification requirements

#### When an Escalation Trigger is Detected

1. **Stop**: Do not generate a final templated response
2. **Alert**: Inform the user that an escalation trigger has been detected
3. **Explain**: Describe which trigger was detected and why it matters
4. **Recommend**: Suggest the appropriate escalation path (senior counsel, outside counsel,
   specific team member, regulatory specialist)
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
- **Generate from framework**: Use the category frameworks below to generate a response
- **Create new template**: Follow the Template Creation Guide to establish a new template

### Step 5: Customize and Generate Response

Apply required customizations:

1. Fill all variable placeholders with correct values
2. Adjust tone for the specific audience and relationship
3. Insert jurisdiction-specific elements (timelines, citations, terminology, rights)
4. Verify deadline calculations are correct
5. Include all legally required elements for the jurisdiction

### Step 6: Quality Verification

Before delivering the response, run the Quality Framework (see below):

1. Citation Quality Gates — all 5 gates must pass
2. Completeness check — all required elements present
3. Writing standards — plain language, active voice, no ambiguity
4. Escalation re-check — confirm no triggers missed during drafting

### Step 7: Generate Glass Box Audit Entry

Create an internal audit record (retained in matter file, NOT sent to recipient).

### Step 8: Deliver Response and Log Follow-Up

Provide the final response and:

1. List required follow-up actions
2. Note any deadlines created by the response
3. Flag the matter for tracking until resolution

---

## Response Categories

### 1. Data Subject Requests (DSRs / DSARs)

**Sub-categories**:

- Acknowledgment of receipt
- Identity verification request
- Fulfillment response (access, deletion, rectification, portability, restriction)
- Partial exemption/redaction with explanation
- Full denial with explanation (manifestly unfounded/excessive, or exemption applies)
- Extension notification (complex request requiring additional time)

**Key template elements**:

- Reference to applicable data protection regulation [JURISDICTION-SPECIFIC]
- Specific timeline for response [JURISDICTION-SPECIFIC: e.g., one calendar month for
  GDPR, 45 days for CCPA, 30 days for LGPD]
- Identity verification requirements (proportionate to data sensitivity)
- Rights of the data subject, including:
  - Right to lodge complaint with supervisory authority [JURISDICTION-SPECIFIC: name and
    contact of authority]
  - Right to judicial remedy [JURISDICTION-SPECIFIC: applicable provision]
- Exemptions applied and legal basis [JURISDICTION-SPECIFIC: cite specific provisions]
- Contact information for DPO or privacy team

**Example template structure — DSR Acknowledgment**:

```
Subject: Your Data [Access/Deletion/Rectification] Request — Reference {{request_id}}

Dear {{requester_name}},

Thank you for your request dated {{request_date}} to {{request_type}} your personal data.
We are processing your request under [APPLICABLE REGULATION].

{{IF identity_verification_needed}}
Before we can process your request, we need to verify your identity. Please provide
{{verification_requirements}}.
{{ENDIF}}

We will respond substantively within [STATUTORY DEADLINE] of
{{receipt_date_or_verification_date}}. If we need additional time due to the complexity
of your request, we will notify you within that period and explain the reasons.

If you have questions, please contact {{privacy_contact}}.

You have the right to lodge a complaint with [SUPERVISORY AUTHORITY NAME AND CONTACT]
if you are not satisfied with how we handle your request.

{{signature_block}}
```

**Example template structure — DSR Partial Exemption**:

```
Subject: Response to Your Data Request — Reference {{request_id}}

Dear {{requester_name}},

Further to your request dated {{request_date}}, please find enclosed the personal data
we hold about you.

We have applied the following exemption(s) to certain data:

{{FOR EACH exemption}}
- **Exemption**: {{exemption_name}} ([REGULATION], {{provision_reference}})
- **Scope**: {{description_of_data_withheld}}
- **Basis**: {{reason_exemption_applies}}
{{ENDFOR}}

The enclosed data represents all personal data we hold about you, subject to the
exemptions noted above.

You have the right to:
- Lodge a complaint with [SUPERVISORY AUTHORITY NAME AND CONTACT]
- [JURISDICTION-SPECIFIC: Other rights, e.g., judicial remedy, appeal mechanism]

{{signature_block}}
```

### 2. Litigation Holds / Document Preservation Notices

**Legal framework**: The duty to preserve documents relevant to litigation arises once
litigation is **reasonably anticipated** [JURISDICTION-SPECIFIC: timing and standard
varies — "reasonably contemplated" in UK, "reasonable anticipation" in US]. Failure to
preserve may constitute spoliation with severe sanctions.

**Sub-categories**:

- Initial preservation notice to custodians
- Preservation reminder / periodic reaffirmation
- Scope modification notice (expansion or narrowing)
- Release of preservation obligations

**Key template elements**:

- Matter name and reference number
- Clear preservation obligations (what must be preserved)
- Scope of preservation (date range, data types, systems, custodians, communication types)
- Prohibition on destruction, alteration, or disposal of potentially relevant materials
- Reference to procedural rules and consequences of non-compliance [JURISDICTION-SPECIFIC]
- Contact for questions
- Acknowledgment requirement with deadline
- Privilege marking [JURISDICTION-SPECIFIC: attorney-client vs LPP vs local equivalent]

**Example template structure — Litigation Hold Notice**:

```
Subject: DOCUMENT PRESERVATION NOTICE — {{matter_name}} — Action Required

[PRIVILEGE MARKING — JURISDICTION-SPECIFIC]

Dear {{custodian_name}},

You are receiving this notice because you may hold documents, communications, or data
relevant to the matter referenced above.

PRESERVATION OBLIGATION:
Effective immediately, you must preserve all documents and electronically stored
information (ESI) relating to:
- Subject matter: {{hold_scope}}
- Date range: {{start_date}} to present
- Document types: {{document_types}}

This includes but is not limited to: emails, letters, memoranda, file notes, reports,
spreadsheets, presentations, instant messages, text messages, voicemails, calendar
entries, and any other records in any format (paper or electronic) including drafts,
notes, and metadata.

YOU MUST NOT delete, destroy, modify, move, or discard any potentially relevant
materials. This includes:
- Do not delete emails (including from deleted items/trash folders)
- Do not overwrite or modify electronic files
- Do not destroy paper documents
- Do not alter any records, including metadata
- Suspend any automated deletion or archiving processes for in-scope data

[JURISDICTION-SPECIFIC: Consequences language — e.g., "Failure to preserve relevant
documents may constitute contempt of court and may result in adverse inferences being
drawn" or local equivalent]

[Specific instructions for systems, email, messaging platforms, local files, shared
drives, cloud storage]

Please acknowledge receipt of this notice by replying to this email by
{{acknowledgment_deadline}}.

Contact {{legal_contact}} immediately if you have questions about what should be
preserved or if you become aware of relevant materials at risk.

{{signature_block}}
```

**Terminology note**: Jurisdictions use different terms:

- US: Discovery, litigation hold, legal hold
- UK: Disclosure, document preservation notice
- [JURISDICTION-SPECIFIC: Add local terminology]

### 3. Privacy Inquiries

**Sub-categories**:

- Cookie/tracking inquiry responses [JURISDICTION-SPECIFIC: ePrivacy, PECR, state laws]
- Privacy notice/policy questions
- Data sharing practice inquiries
- Children's data inquiries [JURISDICTION-SPECIFIC: COPPA, Age-Appropriate Design Code]
- International/cross-border transfer questions
- Regulatory complaint responses [JURISDICTION-SPECIFIC: ICO, CNIL, FTC, state AGs]

**Key template elements**:

- Reference to the organization's privacy notice
- Specific answers based on current processing activities
- Links to relevant privacy documentation
- Lawful basis for processing (if applicable) [JURISDICTION-SPECIFIC]
- Contact information for DPO or privacy team
- Complaint rights information [JURISDICTION-SPECIFIC]

### 4. Vendor Legal Questions

**Sub-categories**:

- Contract status inquiry response
- Amendment request response
- Compliance certification requests (ISO 27001, SOC 2, Cyber Essentials, etc.)
- Audit request responses
- Insurance certificate requests
- Supply chain compliance inquiries [JURISDICTION-SPECIFIC: Modern Slavery Act, LkSG,
  Duty of Vigilance, Uyghur Forced Labor Prevention Act]

**Key template elements**:

- Reference to the applicable agreement (name, date, parties)
- Specific response to the vendor's question
- Any required caveats or limitations
- Next steps and timeline
- [JURISDICTION-SPECIFIC: Compliance statement references if applicable]

### 5. NDA Requests

**Sub-categories**:

- Sending the organization's standard form NDA
- Accepting a counterparty's NDA (with or without markup)
- Declining an NDA request with explanation
- NDA renewal or extension

**Key template elements**:

- Purpose of the NDA (subject matter of the contemplated disclosure)
- Governing law and dispute resolution [JURISDICTION-SPECIFIC]
- Summary of key terms
- Execution instructions [JURISDICTION-SPECIFIC: simple contract vs deed, notarization
  requirements, electronic signature validity]
- Timeline expectations

### 6. Legal Process (Subpoenas / Witness Summons / Court Orders)

**Legal framework**: Compulsory legal process varies significantly by jurisdiction:

- US: Subpoenas (civil and grand jury), court orders, regulatory demands
- UK: Witness summons (CPR Part 34), third-party disclosure orders (CPR Part 31.17),
  Norwich Pharmacal orders
- [JURISDICTION-SPECIFIC: Add local mechanisms]

**Sub-categories**:

- Acknowledgment of receipt
- Objection letter (with specific grounds)
- Request for extension of time
- Compliance cover letter
- Privilege log transmittal

**Key template elements**:

- Court/agency reference, case name, case/claim number
- Specific objections (if any) [JURISDICTION-SPECIFIC: privilege, relevance, burden,
  proportionality, constitutional protections]
- Preservation confirmation
- Timeline for compliance (as specified in the process or order)
- Privilege log description (if withholding documents on privilege grounds)
- Reservation of rights language

**Critical note**: Responses to compulsory legal process ALWAYS require individualized
counsel review. Templates serve as starting frameworks, never as final responses.
Non-compliance may constitute contempt of court or obstruction.

### 7. Insurance Notifications

**Legal framework**: Insurance contracts contain specific notification requirements.
Failure to comply may affect coverage [JURISDICTION-SPECIFIC: strict compliance vs
prejudice requirements vary].

**Sub-categories**:

- Initial claim notification / circumstance notification
- Supplemental information
- Response to reservation of rights letter
- D&O / E&O / Cyber policy notifications (often have unique requirements)

**Key template elements**:

- Policy number, insurer name, broker details, and coverage period
- Description of the matter, incident, or circumstance
- Timeline of events
- Quote of specific policy notification clause being complied with
- Requested coverage confirmation
- Without prejudice / reservation of rights language

---

## Template Management Framework

### Template Organization

Templates should be organized by category and maintained in the team's document management
system or local settings. Each template should include:

| Element                    | Description                              | Required |
| -------------------------- | ---------------------------------------- | -------- |
| **Category**               | Response category (DSR, Hold, etc.)      | Yes      |
| **Template name**          | Descriptive identifier                   | Yes      |
| **Version**                | Version number for change tracking       | Yes      |
| **Last reviewed**          | Date of last legal review                | Yes      |
| **Approved by**            | Name/title of approving counsel          | Yes      |
| **Applicable legislation** | Relevant statutes and regulations        | Yes      |
| **Use case**               | When this template is appropriate        | Yes      |
| **Escalation triggers**    | When NOT to use this template            | Yes      |
| **Required variables**     | Information that must be customized      | Yes      |
| **Template body**          | Response text with variable placeholders | Yes      |
| **Follow-up actions**      | Standard steps after sending             | Yes      |
| **Notes**                  | Special instructions for users           | Optional |

### Template Lifecycle

1. **Creation**: Draft based on current law, regulatory guidance, and team input
2. **Review**: Counsel review and approval of template content
3. **Publication**: Add to template library with full metadata
4. **Use**: Generate responses using the template
5. **Feedback**: Track when templates are modified during use — identify improvement needs
6. **Update**: Revise when laws, regulations, guidance, or best practices change
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

[Special instructions, including regulatory guidance references]
```

---

## Customization Guidelines

### Required Customization

Every templated response MUST be customized with:

- Correct names, dates, and reference numbers
- Specific facts of the situation (not generic placeholders)
- Applicable jurisdiction and regulation
- Correct response deadlines calculated from the date of receipt
- Appropriate signature block and contact information
- [JURISDICTION-SPECIFIC: Required rights information, e.g., supervisory authority
  complaint rights for GDPR responses]

### Tone Adjustment Matrix

| Dimension        | Options                               | Guidance                                  |
| ---------------- | ------------------------------------- | ----------------------------------------- |
| **Audience**     | Internal / External / Regulatory      | Regulatory = most formal, precise         |
| **Relationship** | New / Existing / Adversarial          | Adversarial = more guarded, no admissions |
| **Sensitivity**  | Routine / Contentious / Investigation | Investigation = counsel review required   |
| **Urgency**      | Standard / Expedited / Overdue        | Overdue = acknowledge delay, explain      |

### Jurisdiction-Specific Checks

Before sending any response, verify:

- [ ] Correct regulation cited (e.g., UK GDPR not just "GDPR", CCPA not just "California law")
- [ ] Timelines match applicable law (e.g., "one calendar month" not "30 days" for GDPR)
- [ ] Local legal terminology used (e.g., disclosure vs discovery, solicitor vs attorney)
- [ ] Correct supervisory authority / regulator named
- [ ] Local court / tribunal references accurate
- [ ] Privilege marking uses local convention

---

## Quality Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                     | Fail Action                                  |
| -------------- | ------------------------------------------------------------------------ | -------------------------------------------- |
| **Source**     | Every regulatory reference cites specific article/section/provision      | Add citation or mark "[VERIFY]"              |
| **Format**     | Citations use correct format for the jurisdiction                        | Fix format                                   |
| **Currency**   | Cited provisions and guidance confirmed current                          | Flag "[CHECK CURRENCY]"                      |
| **Domain**     | Terminology matches the jurisdiction (no US terms in UK responses, etc.) | Fix terminology                              |
| **Confidence** | If template is being stretched beyond its designed use case, flag it     | Add "[COUNSEL TO REVIEW — template adapted]" |

### Self-Interrogation for High-Stakes Responses

For any response involving regulators, legal process, or potential litigation, apply
this 3-pass review:

**Pass 1 — Completeness**: Does the response include all legally required elements for
this jurisdiction and response type? Are all statutory rights mentioned? Are all deadlines
correctly calculated?

**Pass 2 — Accuracy**: Are all regulatory citations correct and current? Is the terminology
appropriate for the jurisdiction? Are there any statements that could be construed as
admissions or waivers?

**Pass 3 — Appropriateness**: Is a templated response actually appropriate here, or should
this be escalated? Have all escalation triggers been checked? Would a reasonable counsel
approve sending this without further review?

### Confidence Scoring

| Level        | Range     | Meaning                            | Action                         |
| ------------ | --------- | ---------------------------------- | ------------------------------ |
| **Definite** | 0.95-1.0  | Standard template, routine matter  | Send after standard review     |
| **High**     | 0.80-0.94 | Minor customization, known pattern | Send with quality check        |
| **Probable** | 0.60-0.79 | Significant adaptation required    | Senior review before sending   |
| **Possible** | 0.40-0.59 | Template being stretched           | Counsel review required        |
| **Unlikely** | 0.0-0.39  | Template not appropriate           | Do not use template — escalate |

### Glass Box Audit Trail

Every generated response MUST include an internal Glass Box audit record. This is
retained in the matter file — NOT sent to the recipient.

```yaml
glass_box:
  inquiry_type: "[DSR / Litigation hold / Privacy inquiry / Vendor / NDA / Legal process / Insurance]"
  template_used: "[Template name and version, or 'Generated from framework']"
  template_modified: "Yes / No — if yes, [what was changed and why]"
  jurisdiction: "[Jurisdiction whose law was applied]"
  regulations_applied:
    - "[Regulation], [Article/Section]"
  citations_verified:
    - "[Citation] — VERIFIED / UNVERIFIED"
  deadline_calculation:
    received: "[YYYY-MM-DD]"
    deadline: "[YYYY-MM-DD]"
    basis: "[Statutory basis for deadline]"
  exemptions_applied:
    - "[Exemption] — [Legal basis] — [Applied to: description]"
  escalation_triggers_checked:
    - "[Trigger 1] — Present / Not present"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  quality_gates_passed: "5/5 or [list failures]"
  reviewer: "[Name or 'AI-assisted — requires counsel review before sending']"
  follow_up_actions:
    - "[Action 1]"
```

---

## Writing Standards

Templated legal responses must be clear, professional, and understandable by their
intended audience. Apply these standards to every response.

### Three-Pass Editing

**Pass 1 — Structure**: Does the response answer the inquiry? Is information in logical
order? Is anything missing? Is anything unnecessary?

**Pass 2 — Clarity**: Can the recipient understand this without legal training (where
appropriate)? Replace passive constructions with active voice. Ensure every pronoun has
a clear antecedent. Remove ambiguity.

**Pass 3 — Concision**: Cut padding, hedging, and unnecessary qualifiers. Replace long
words with short where meaning is preserved. Remove jargon unless the audience expects
it. Target 20-30% word count reduction from first draft.

### Specific Rules

- **Active voice**: "We received your request on 15 January" not "Your request was
  received on 15 January"
- **Name the actor**: "The [Regulator] can investigate" not "An investigation may be
  commenced"
- **Plain language for individuals**: DSR responses go to people who may have no legal
  knowledge. Write accordingly.
- **Formal but clear for regulators**: Regulatory authorities appreciate factual,
  well-organized responses. Avoid advocacy language in factual submissions.
- **Precise for preservation notices**: Litigation holds must be unambiguous. "You must
  not delete emails" is better than "Please ensure electronic communications are preserved
  in accordance with the organization's document retention policy."
- **No hidden complexity**: Obscure language that makes it harder for recipients to
  understand their rights is not just bad writing — it risks regulatory enforcement.
- **[JURISDICTION-SPECIFIC: Language/spelling conventions]**: Use local spelling and
  conventions (organisation vs organization, colour vs color, programme vs program).

### Quality Gates Before Sending

1. Would a non-lawyer recipient understand this response (where applicable)?
2. Are all regulatory references correct and current?
3. Is the deadline correctly calculated using the jurisdiction's rules?
4. Are required rights (e.g., complaint to supervisory authority) included?
5. Has every escalation trigger been checked?
6. Is this response appropriate for the specific facts, or is it generic boilerplate?
7. Have all variables been replaced with actual values (no {{placeholders}} remain)?

---

## Anti-Patterns

What NOT to do with templated legal responses:

1. **Sending a template without customization** — A response with "{{requester_name}}"
   or other unfilled variables is worse than no response. Every variable must be filled.
   Every response must be reviewed against the specific facts.

2. **Using incorrect timeline formulations** — "30 days" and "one calendar month" are
   different deadlines in many jurisdictions. One calendar month from 31 January is
   28/29 February, not 2 March. This error has triggered regulatory enforcement.

3. **Ambiguous regulation citations** — Citing "GDPR" without specifying UK or EU is
   ambiguous and may be incorrect. Citing "California law" without specifying CCPA/CPRA
   provisions is imprecise. Always cite specific regulation and provision.

4. **Applying exemptions without documentation** — "We've applied the [exemption] to
   some documents" is insufficient. Each exemption must be applied to specific data with
   a documented reason, retained in the matter file for potential regulatory inquiry.

5. **Vague preservation notices** — A litigation hold that politely asks custodians to
   "please keep relevant documents" doesn't convey the severity. Explain the consequences
   of non-compliance (spoliation, adverse inference, contempt).

6. **Templated responses to regulators** — Never send a template response to a regulator
   without individualized counsel review. Regulators recognize boilerplate, and it signals
   the organization is not taking the matter seriously.

7. **Omitting mandatory disclosures** — Forgetting to include supervisory authority
   complaint rights in DSR responses, or other legally required elements, is a compliance
   failure, not just a drafting error.

8. **Using wrong jurisdiction's terminology** — "Discovery hold" / "subpoena" /
   "attorney-client privilege" are US terms. UK uses disclosure / witness summons /
   legal professional privilege. Using the wrong terms in formal communications is
   unprofessional and may confuse recipients.

9. **Missing deadlines without extension notice** — If you need more time for a DSR, you
   must notify the requester within the original statutory period and explain why.
   Silently missing the deadline is a compliance breach.

10. **Fire-and-forget responses** — Every response needs follow-up actions: log the
    response, schedule follow-up deadlines, update the matter file, close the request
    only when fully resolved.

11. **Ignoring escalation triggers** — Proceeding with a templated response when an
    escalation trigger is present. The escalation check exists because some situations
    cannot be safely handled with templates.

12. **Template scope creep** — Using a template designed for one situation (e.g., simple
    DSR acknowledgment) for a different situation (e.g., complex DSR with exemptions).
    Each template has a designed use case — respect its boundaries.

13. **Copying without understanding** — Using template language without understanding why
    it exists. If you cannot explain why each element of the response is there, you
    should not be sending it.

14. **Inconsistent variable naming** — Using {{name}}, {{requester_name}}, {{data_subject}},
    and {{individual}} interchangeably in the same template library. Standardize variable
    names across all templates.

15. **No version control** — Failing to track template versions, leading to outdated
    templates being used after law changes. Every template needs a version number and
    last-reviewed date.

16. **Privilege marking errors** — Using the wrong privilege assertion for the
    jurisdiction, or failing to mark privileged communications appropriately. This can
    waive privilege.

---

## External Tool Integration

### legalcode-mcp Integration

If **legalcode-mcp** is connected, use it for:

- Verifying current regulatory text and guidance
- Checking recent enforcement actions or guidance updates
- Validating deadline calculations against current law
- Researching jurisdiction-specific requirements

**With legalcode-mcp connected:**

- Mark verified citations as `VERIFIED` in the Glass Box audit trail
- Update templates based on recent regulatory guidance

**Without legalcode-mcp:**

- Proceed with template generation
- Mark regulatory citations as `[VERIFY]` where currency is uncertain
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Document Management Integration

Templates should integrate with the organization's:

- Matter management system (for audit trail retention)
- Document management system (for template storage and versioning)
- Email system (for response delivery)
- Deadline tracking system (for follow-up scheduling)

---

## Output Format Template

When generating a response, structure the output as follows:

````markdown
## Generated Response

**Category**: [Response category]
**Template**: [Template name and version, or "Generated from framework"]
**Jurisdiction**: [Applicable jurisdiction]
**Confidence**: [HIGH / MEDIUM / LOW]

---

### Response Text

[The actual response to be sent, fully customized with all variables filled]

---

### Internal Notes (Do Not Send)

**Deadline**: [Calculated deadline and basis]

**Escalation triggers checked**:

- [x] [Trigger 1] — Not present
- [x] [Trigger 2] — Not present
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

| Gate             | Status      |
| ---------------- | ----------- |
| Source citations | PASS / FAIL |
| Citation format  | PASS / FAIL |
| Currency         | PASS / FAIL |
| Terminology      | PASS / FAIL |
| Confidence       | PASS / FAIL |

**Writing standards**: [Confirmed / Issues noted]

**Ready to send**: [Yes — after counsel review / No — escalation required]

```

---

## Localization Notes

This skill is designed to be jurisdiction-agnostic with clear localization points. When
deploying for a specific jurisdiction:

1. **Create a jurisdiction-specific variant** if the jurisdiction has substantial unique
   requirements (e.g., `legalcode-canned-responses-uk`, `legalcode-canned-responses-ccpa`)

2. **Replace [JURISDICTION-SPECIFIC] markers** with verified local content:
   - Statutory citations with specific article/section numbers
   - Supervisory authority names and contact information
   - Correct timeline formulations (calendar months vs days)
   - Local legal terminology
   - Required disclosures and rights information

3. **Add jurisdiction-specific escalation triggers** based on local regulatory enforcement
   patterns and heightened-risk scenarios

4. **Verify all templates against current local law** — regulatory requirements change
   frequently, especially in data protection

5. **Use local language requirements** where applicable — some jurisdictions mandate
   responses in the local language or both local language and English

---

## Provenance

- **Original synthesis**: Legalcode (2026-02-27)
- **Input skills analyzed**:
  - `skills/general/workflows/canned-responses/SKILL.md` (anthropics/knowledge-work-plugins)
  - `skills/general/workflows/imported-uk-legal-plugins--skills-uk-legal-canned-responses/SKILL.md` (45black/uk-legal-plugins)
  - `skills/general/workflows/imported-claude-legal--skills-canned-responses/SKILL.md` (Kromer-Group/Claude-Legal)
  - `skills/general/compliance/imported-awesome-claude-corporate-skills--06-legal-compliance-canned-responses/SKILL.md` (w95/awesome-claude-corporate-skills)
- **Reference standard**: `legalcode-contract-review` quality framework
- **License**: Apache-2.0 (consistent with source skills)
```
