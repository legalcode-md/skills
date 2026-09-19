---
name: legalcode-canned-responses-ccpa
description: Generate, manage, and customize templated responses for routine legal inquiries under California
  and US federal law — consumer rights requests (CCPA/CPRA), litigation holds, privacy inquiries, vendor
  questions, NDA requests, legal process (subpoenas, court orders, regulatory demands), and insurance
  notifications. Use when responding to routine legal questions governed by California or US law, managing
  response template libraries, creating new templates, or identifying when a situation requires individualized
  attorney attention rather than a templated response. Hardcoded for California/US jurisdiction. Includes
  escalation trigger detection, quality frameworks, and audit trails.
metadata:
  jurisdiction: united-states/california
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Canned Responses -- California (CCPA/CPRA)

> **Disclaimer**: This skill provides a framework for AI-assisted legal response
> generation under California and US federal law. It does not constitute legal
> advice. All templated responses should be reviewed by a qualified attorney
> licensed in California before sending, especially for regulated communications.
> Laws change; verify current applicability before relying on any provision
> described here. Statutory and regulatory references cited from memory carry
> hallucination risk -- verify against authoritative sources (California
> Legislative Information, Code of Federal Regulations, CPPA rulemaking docket)
> before relying on them.

## Purpose and Scope

This skill helps in-house legal teams manage, customize, and generate templated
responses for common legal inquiries governed by California and US federal law. It
identifies when a situation should NOT use a templated response and instead requires
individualized attention from qualified counsel.

This is a **jurisdiction-specific variant** of `legalcode-canned-responses`, with all
`[JURISDICTION-SPECIFIC]` markers replaced with hardcoded California and US federal
law references. It uses American English throughout.

**Covers:**

- Template generation for 7 core response categories under California/US law
- Escalation trigger detection (universal and category-specific)
- Template creation, lifecycle management, and retirement workflows
- Customization guidelines for tone, jurisdiction, and audience
- Quality assurance frameworks with audit trails
- Variable placeholder management and validation
- California-specific regulatory requirements (CCPA/CPRA, COPPA, CMIA, HIPAA)

**Does not:**

- Provide legal advice or final legal opinions
- Replace attorney review for regulated or high-stakes communications
- Generate responses for novel or unprecedented situations
- Handle matters involving potential litigation without escalation
- Operate as a document management system (integrates with, does not replace)
- Cover non-California state privacy laws (use jurisdiction-specific variants or
  the base `legalcode-canned-responses` skill for other states)

**Related skills:**

- `legalcode-canned-responses` -- jurisdiction-agnostic base skill
- `legalcode-contract-review` -- for contract clause analysis
- `legalcode-nda-triage` -- for NDA screening and classification
- `ccpa-cpra-consumer-rights-operations` -- for California consumer rights
  compliance artifact drafting

---

## Jurisdiction and Governing Law

This skill is specific to **California and US federal law**. All statutory
references, timelines, terminology, and regulatory citations are hardcoded for
this jurisdiction.

**Primary data protection framework:**

- California Consumer Privacy Act of 2018, as amended by the California Privacy
  Rights Act (Cal. Civ. Code SS 1798.100-1798.199.100)
- CPPA regulations (11 CCR SS 7000 et seq.)
- Children's Online Privacy Protection Act (COPPA), 15 U.S.C. SS 6501-6506
  (children under 13)
- California Age-Appropriate Design Code Act (AB 2273) (children under 18)
- California Confidentiality of Medical Information Act (CMIA), Cal. Civ. Code
  SS 56-56.37
- HIPAA (42 U.S.C. SS 1320d et seq.; 45 CFR Parts 160, 164) where applicable

**Enforcement authorities:**

- California Privacy Protection Agency (CPPA) -- primary CCPA/CPRA enforcement
- California Attorney General -- concurrent enforcement authority
- Federal Trade Commission (FTC) -- COPPA and federal unfair/deceptive practices
- Securities and Exchange Commission (SEC) -- for securities-related matters
- State attorneys general -- for multi-state matters
- California Department of Financial Protection and Innovation (DFPI) -- for
  financial services matters

**Litigation framework:**

- Federal Rules of Civil Procedure (FRCP)
- California Code of Civil Procedure (Cal. CCP)
- Federal Rules of Evidence (FRE)
- California Evidence Code

**Privilege framework:**

- Attorney-client privilege (Cal. Evidence Code SS 950-962)
- Work product doctrine (Cal. CCP SS 2018.030; FRCP Rule 26(b)(3))

**Penalties and enforcement:**

- CCPA: $2,500 per violation (unintentional); $7,500 per violation (intentional)
  (Cal. Civ. Code SS 1798.155)
- Private right of action for data breaches: $100-$750 per consumer per incident
  or actual damages, whichever is greater (Cal. Civ. Code SS 1798.150)
- COPPA: up to $50,120 per violation (FTC-adjusted)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change which template category applies
- Escalation trigger detection requires user confirmation
- Multiple valid response approaches exist
- Tone or audience calibration is needed
- Federal vs. state law priority is unclear

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
   - Options: Consumer Rights Request (CCPA/CPRA), Litigation Hold, Privacy
     Inquiry, Vendor Question, NDA Request, Legal Process (Subpoena/Court Order/
     Regulatory Demand), Insurance Notification, Other (describe)
   - _Why this matters_: Determines which template category and escalation
     triggers apply.

2. **Audience**: Who is the recipient?
   - Options: Individual consumer, Business counterparty, Regulator/government
     (CPPA, AG, FTC, SEC), Internal (employee/custodian), Opposing counsel, Other
   - _Why this matters_: Determines tone, formality level, and required
     disclosures.

3. **Urgency**: What is the timeline?
   - Options: Standard (use statutory deadline), Expedited (shorter than
     standard), Already overdue (remediation mode), No deadline (informational)
   - _Why this matters_: Determines whether extension notices are needed and
     response prioritization.

4. **Prior handling**: Has the team handled similar inquiries before?
   - Options: Yes -- use existing template, Yes -- but template needs update,
     No -- novel situation, Unknown
   - _Why this matters_: Novel situations may require escalation rather than
     templating.

5. **Overlapping regulatory regimes**: Do any sector-specific laws apply?
   - Options: HIPAA (health data), GLBA/FCRA (financial data), FERPA (education
     records), COPPA (children under 13), AB 2273 (children under 18), CMIA
     (medical information), None identified
   - _Why this matters_: Sector-specific laws may impose additional requirements
     or preempt CCPA provisions.

If any answer indicates a potential escalation trigger, proceed to Step 3 before
generating a response.

### Step 3: Check Escalation Triggers

Before generating ANY templated response, systematically check for escalation
triggers. If any trigger is present, do NOT generate a standard templated
response -- instead, escalate per the protocol below.

#### Universal Escalation Triggers (Apply to All Categories)

- The matter involves potential litigation or regulatory investigation
- The inquiry is from a regulator, government agency, or law enforcement (CPPA,
  California AG, FTC, SEC, DOJ, state AGs, DFPI)
- The response could create a binding legal commitment or waiver
- The matter involves potential criminal liability (CFAA, California Penal Code,
  wire fraud under 18 U.S.C. SS 1343)
- Media attention is involved or likely
- The situation is unprecedented (no prior handling by the team)
- Multiple jurisdictions are involved with conflicting requirements
- The matter involves executive leadership, board members, or politically exposed
  persons
- Privilege considerations are complex or disputed (attorney-client privilege,
  work product doctrine)
- The inquiry is from someone in active litigation or dispute with the
  organization

#### Category-Specific Escalation Triggers

**Consumer Rights Requests (CCPA/CPRA)**:

- Request from or on behalf of a minor (COPPA for under-13; AB 2273 for under-18)
- Request involves data subject to a litigation hold
- Requester is in active litigation or dispute with the organization
- Request is from an employee with an active HR matter, grievance, or
  investigation (note: CCPA employee data provisions)
- Request scope is extraordinarily broad (potential fishing expedition)
- Request involves sensitive personal information (SPI) as defined in Cal. Civ.
  Code SS 1798.140(ae) -- social security number, precise geolocation, racial/ethnic
  origin, religious beliefs, health data, biometric data, sexual orientation,
  genetic data, communications content
- Request involves health data implicating HIPAA or CMIA
- Request involves financial data implicating GLBA or FCRA
- Privilege analysis is required for responsive documents
- Request involves FERPA-protected education records
- Authorized agent request where power of attorney or signed authorization is
  disputed or absent (11 CCR SS 7063)

**Litigation Holds / Document Preservation**:

- Potential criminal liability (CFAA, wire fraud, obstruction of justice)
- Unclear or disputed preservation scope
- Preservation conflicts with CCPA deletion obligations (consumer deletion request
  vs. litigation hold)
- Prior holds exist for related matters
- Custodian objects to the hold scope
- Cross-border preservation obligations with conflicting legal requirements
- Data localization laws restrict where preserved data can be stored or accessed
- Electronic discovery issues involving proportionality under FRCP Rule 26(b)(1)

**Vendor Questions**:

- Vendor is disputing contract terms
- Vendor is threatening litigation or termination
- Response could affect ongoing negotiation
- Question involves regulatory compliance (not just contract interpretation)
- California Transparency in Supply Chains Act compliance concerns (for large
  retailers/manufacturers with worldwide gross receipts exceeding $100 million)
- CCPA service provider/contractor classification issues (Cal. Civ. Code
  SS 1798.140(ag), SS 1798.140(j))
- HIPAA business associate agreement requirements

**Legal Process (Subpoenas / Court Orders / Regulatory Demands)**:

- **ALWAYS requires attorney review** -- templates are starting points only,
  never final responses
- Attorney-client privilege or work product issues identified in responsive
  documents
- Third-party personal data involved (CCPA implications of disclosure)
- Cross-border production issues (requested documents held in another
  jurisdiction)
- Unreasonable timeline that may require a motion to quash or motion for
  protective order
- Grand jury subpoenas (secrecy obligations under FRCP Rule 6(e))
- Civil Investigative Demands (CIDs) from CPPA, AG, or FTC
- SEC subpoenas or formal orders of investigation

**Insurance Notifications**:

- Late notification (potential coverage dispute -- evaluate late notice prejudice
  under applicable state law)
- Claim may implicate multiple policies or coverage towers
- Reservation of rights letter received from insurer
- Coverage dispute anticipated
- Matter involves D&O, E&O, or cyber policies with complex notification
  requirements
- Claims-made policy with strict reporting deadline approaching

#### When an Escalation Trigger is Detected

1. **Stop**: Do not generate a final templated response
2. **Alert**: Inform the user that an escalation trigger has been detected
3. **Explain**: Describe which trigger was detected and why it matters
4. **Recommend**: Suggest the appropriate escalation path (senior attorney,
   outside counsel, specific team member, regulatory specialist)
5. **Offer**: Provide a DRAFT for attorney review, clearly marked:
   ```
   ============================================================
   DRAFT -- FOR ATTORNEY REVIEW ONLY -- NOT TO BE SENT
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

Apply required customizations:

1. Fill all variable placeholders with correct values
2. Adjust tone for the specific audience and relationship
3. Insert California/US-specific elements (timelines, citations, terminology,
   rights information)
4. Verify deadline calculations are correct under applicable California/US law
5. Include all legally required elements (consumer rights disclosures, CPPA/AG
   complaint information, applicable opt-out mechanisms)

### Step 6: Quality Verification

Before delivering the response, run the Quality Framework (see below):

1. Citation Quality Gates -- all 5 gates must pass
2. Completeness check -- all required elements present
3. Writing standards -- plain language, active voice, no ambiguity
4. Escalation re-check -- confirm no triggers missed during drafting

### Step 7: Generate Glass Box Audit Entry

Create an internal audit record (retained in matter file, NOT sent to recipient).

### Step 8: Deliver Response and Log Follow-Up

Provide the final response and:

1. List required follow-up actions
2. Note any deadlines created by the response
3. Flag the matter for tracking until resolution

---

## Response Categories

### 1. Consumer Rights Requests (CCPA/CPRA)

**Legal framework**: Cal. Civ. Code SS 1798.100 et seq. Consumers have the right
to access, delete, correct, opt out of sale/sharing, and limit use of sensitive
personal information. Businesses must respond within **45 calendar days** of
receiving a verifiable request, extendable by an additional **45 calendar days**
upon notice to the consumer (Cal. Civ. Code SS 1798.130(a)(2)). Verification
requirements are specified in 11 CCR SS 7060-7063.

**Sub-categories**:

- Acknowledgment of receipt
- Identity verification request (per 11 CCR SS 7060-7063)
- Fulfillment response (access, deletion, correction, portability)
- Opt-out of sale/sharing confirmation
- Limit use of sensitive personal information confirmation
- Partial exemption/redaction with explanation
- Full denial with explanation
- Extension notification (complex request requiring additional time)

**Key template elements**:

- Reference to CCPA/CPRA (Cal. Civ. Code SS 1798.100 et seq.) and CPPA
  regulations (11 CCR SS 7000 et seq.)
- Specific timeline: **45 calendar days** from receipt of verifiable request,
  extendable by **45 additional calendar days** with notice
- Identity verification requirements proportionate to data sensitivity and
  request type (11 CCR SS 7060-7063)
- Consumer rights disclosures, including:
  - Right to submit complaints to the California Privacy Protection Agency
    (CPPA) at cppa.ca.gov
  - Right to submit complaints to the California Attorney General at
    oag.ca.gov
  - Right to non-discrimination for exercising privacy rights (Cal. Civ. Code
    SS 1798.125)
- Exemptions applied and legal basis (cite specific Cal. Civ. Code provisions)
- Contact information for privacy team
- Global Privacy Control (GPC) processing confirmation where applicable

**Example template structure -- Consumer Rights Request Acknowledgment**:

```
Subject: Your Privacy Request -- Reference {{request_id}}

Dear {{requester_name}},

Thank you for your request dated {{request_date}} to {{request_type}} your
personal information. We are processing your request under the California
Consumer Privacy Act, as amended by the California Privacy Rights Act
(Cal. Civ. Code Section 1798.100 et seq.).

{{IF identity_verification_needed}}
Before we can process your request, we need to verify your identity in
accordance with applicable regulations (11 CCR Section 7060 et seq.). Please
provide {{verification_requirements}}.
{{ENDIF}}

We will respond to your request within 45 calendar days of
{{receipt_date_or_verification_date}}. If we need additional time due to the
complexity of your request, we will notify you within that period, explain the
reasons, and provide an expected completion date (not to exceed an additional
45 calendar days).

You will not be discriminated against for exercising your privacy rights under
the CCPA/CPRA.

If you have questions, please contact {{privacy_contact}}.

You may submit a complaint to the California Privacy Protection Agency (CPPA)
at cppa.ca.gov or to the California Attorney General at oag.ca.gov if you are
not satisfied with how we handle your request.

{{signature_block}}
```

**Example template structure -- Consumer Rights Partial Exemption**:

```
Subject: Response to Your Privacy Request -- Reference {{request_id}}

Dear {{requester_name}},

In response to your request dated {{request_date}}, please find enclosed the
personal information we hold about you.

We have applied the following exemption(s) to certain information:

{{FOR EACH exemption}}
- **Exemption**: {{exemption_name}} (Cal. Civ. Code Section {{provision}})
- **Scope**: {{description_of_data_withheld}}
- **Basis**: {{reason_exemption_applies}}
{{ENDFOR}}

The enclosed information represents all personal information we hold about
you, subject to the exemptions noted above.

You have the right to:
- Submit a complaint to the California Privacy Protection Agency (CPPA) at
  cppa.ca.gov
- Submit a complaint to the California Attorney General at oag.ca.gov
- Exercise your other rights under the CCPA/CPRA, including the right to
  non-discrimination (Cal. Civ. Code Section 1798.125)

{{signature_block}}
```

### 2. Litigation Holds / Document Preservation Notices

**Legal framework**: The duty to preserve documents relevant to litigation arises
once litigation is **reasonably anticipated** under federal and California law.
Failure to preserve may constitute spoliation, resulting in sanctions including
adverse inference instructions, monetary sanctions, or case-dispositive sanctions
under FRCP Rule 37(e) (for ESI) and inherent court authority. California courts
apply similar principles under Cal. CCP SS 2023.010 et seq.

**Sub-categories**:

- Initial preservation notice to custodians
- Preservation reminder / periodic reaffirmation
- Scope modification notice (expansion or narrowing)
- Release of preservation obligations

**Key template elements**:

- Matter name and reference number
- Clear preservation obligations (what must be preserved)
- Scope of preservation (date range, data types, systems, custodians,
  communication types)
- Prohibition on destruction, alteration, or disposal of potentially relevant
  materials
- Reference to FRCP Rule 37(e) and potential sanctions including adverse
  inference, monetary penalties, and case-dispositive sanctions
- Contact for questions
- Acknowledgment requirement with deadline
- Privilege marking: **ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL / WORK
  PRODUCT**

**Example template structure -- Litigation Hold Notice**:

```
Subject: DOCUMENT PRESERVATION NOTICE -- {{matter_name}} -- Action Required

ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL
ATTORNEY WORK PRODUCT

Dear {{custodian_name}},

You are receiving this notice because you may hold documents, communications,
or data relevant to the matter referenced above.

PRESERVATION OBLIGATION:
Effective immediately, you must preserve all documents and electronically
stored information (ESI) relating to:
- Subject matter: {{hold_scope}}
- Date range: {{start_date}} to present
- Document types: {{document_types}}

This includes but is not limited to: emails, letters, memoranda, file notes,
reports, spreadsheets, presentations, instant messages (including Slack,
Teams, and similar platforms), text messages, voicemails, calendar entries,
social media content, and any other records in any format (paper or
electronic) including drafts, notes, and metadata.

YOU MUST NOT delete, destroy, modify, move, or discard any potentially
relevant materials. This includes:
- Do not delete emails (including from deleted items/trash folders)
- Do not overwrite or modify electronic files
- Do not destroy paper documents
- Do not alter any records, including metadata
- Suspend any automated deletion or archiving processes for in-scope data

Failure to preserve relevant documents may result in serious legal
consequences, including adverse inference instructions to the jury, monetary
sanctions, and potential case-dispositive sanctions under Federal Rule of
Civil Procedure 37(e) and applicable California law.

[Specific instructions for systems, email, messaging platforms, local files,
shared drives, cloud storage]

Please acknowledge receipt of this notice by replying to this email by
{{acknowledgment_deadline}}.

Contact {{legal_contact}} immediately if you have questions about what should
be preserved or if you become aware of relevant materials at risk.

{{signature_block}}
```

### 3. Privacy Inquiries

**Sub-categories**:

- Cookie/tracking inquiry responses (note: California does not have a
  comprehensive cookie law comparable to EU ePrivacy, but CCPA opt-out and GPC
  requirements apply to tracking for sale/sharing purposes)
- Privacy notice/policy questions (Cal. Civ. Code SS 1798.130, SS 1798.100(a))
- Data sharing practice inquiries
- Children's data inquiries (COPPA for under-13; AB 2273 for under-18)
- Cross-border transfer questions
- CPPA or AG complaint/inquiry responses
- Health data inquiries (HIPAA/CMIA intersection)
- Employee data inquiries (CCPA employee data provisions; Cal. Labor Code
  privacy protections)

**Key template elements**:

- Reference to the organization's privacy notice/policy
- Specific answers based on current processing activities
- Links to relevant privacy documentation, including "Do Not Sell or Share My
  Personal Information" link (Cal. Civ. Code SS 1798.135)
- Lawful processing purposes disclosed in privacy notice
- Contact information for privacy team
- CPPA and AG complaint rights information
- Global Privacy Control (GPC) processing statement where relevant

### 4. Vendor Legal Questions

**Sub-categories**:

- Contract status inquiry response
- Amendment request response
- Compliance certification requests (ISO 27001, SOC 2, SOC 2 Type II, FedRAMP)
- Audit request responses
- Insurance certificate requests
- Supply chain compliance inquiries -- California Transparency in Supply Chains
  Act (for retail sellers or manufacturers with worldwide gross receipts
  exceeding $100 million doing business in California)
- CCPA service provider/contractor compliance questions (Cal. Civ. Code
  SS 1798.140(ag), SS 1798.140(j); contract requirements per SS 1798.100(d))
- HIPAA business associate agreement questions (where applicable)

**Key template elements**:

- Reference to the applicable agreement (name, date, parties)
- Specific response to the vendor's question
- Any required caveats or limitations
- Next steps and timeline
- CCPA vendor classification confirmation (service provider, contractor, or
  third party) and corresponding contractual obligations
- California Transparency in Supply Chains Act disclosure reference (if
  applicable)

### 5. NDA Requests

**Sub-categories**:

- Sending the organization's standard form NDA
- Accepting a counterparty's NDA (with or without markup)
- Declining an NDA request with explanation
- NDA renewal or extension

**Key template elements**:

- Purpose of the NDA (subject matter of the contemplated disclosure)
- Governing law: California law, exclusive jurisdiction of courts of the State
  of California (or agreed federal forum, e.g., Northern District of California)
- Summary of key terms
- Execution instructions: Standard US contract execution. Electronic signatures
  are valid under the federal Electronic Signatures in Global and National
  Commerce Act (ESIGN Act, 15 U.S.C. SS 7001 et seq.) and the Uniform Electronic
  Transactions Act (UETA), Cal. Civ. Code SS 1633.1 et seq. Notarization is not
  required for NDAs.
- Timeline expectations
- Non-compete limitations: Note that California Business and Professions Code
  SS 16600 renders most non-compete provisions void. NDA terms should not be
  drafted so broadly as to function as de facto non-competes.

### 6. Legal Process (Subpoenas / Court Orders / Regulatory Demands)

**Legal framework**: Compulsory legal process under California and US federal law
includes:

- **Federal civil subpoenas** (FRCP Rule 45) -- compel testimony and/or
  document production
- **California civil subpoenas** (Cal. CCP SS 1985-1997) -- duces tecum and
  deposition subpoenas
- **Grand jury subpoenas** (FRCP Rule 17(c); 18 U.S.C. SS 3321 et seq.) --
  secrecy obligations under FRCP Rule 6(e)
- **Civil Investigative Demands (CIDs)** -- from CPPA, California AG, FTC, or
  other agencies
- **SEC subpoenas and formal orders of investigation**
- **Administrative subpoenas** from federal and state agencies
- **Court orders** -- various federal and state court powers

**Sub-categories**:

- Acknowledgment of receipt
- Objection letter (with specific grounds: attorney-client privilege, work
  product, relevance, undue burden, overbreadth, proportionality, First Amendment,
  Fourth Amendment, Fifth Amendment)
- Motion to quash or motion for protective order (FRCP Rule 45(d); Cal. CCP
  SS 1987.1)
- Request for extension of time
- Compliance cover letter
- Privilege log transmittal

**Key template elements**:

- Court/agency reference, case name, case number
- Specific objections (if any) with legal bases -- attorney-client privilege
  (Cal. Evidence Code SS 950-962), work product doctrine (FRCP Rule 26(b)(3);
  Cal. CCP SS 2018.030), relevance (FRCP Rule 26(b)(1)), undue burden
  (FRCP Rule 45(d)(3)), proportionality, constitutional protections
- Preservation confirmation
- Timeline for compliance (as specified in the subpoena or order)
- Privilege log description (if withholding documents on privilege grounds) --
  must identify nature of the document, date, author, recipients, and basis
  for privilege assertion
- Reservation of rights language

**Critical note**: Responses to compulsory legal process ALWAYS require
individualized attorney review. Templates serve as starting frameworks, never as
final responses. Non-compliance with a subpoena may result in contempt of court.
Non-compliance with a court order may result in sanctions, contempt, or criminal
penalties.

### 7. Insurance Notifications

**Legal framework**: US insurance contracts contain specific notification
requirements. Key considerations under California and general US insurance law:

- **Claims-made vs. occurrence policies**: Claims-made policies require
  notification during the policy period or extended reporting period.
  Occurrence policies are triggered by the date of the occurrence, regardless
  of when the claim is made.
- **Duty to defend vs. duty to indemnify**: In California, the duty to defend
  is broader than the duty to indemnify. An insurer must defend if the complaint
  alleges facts that could potentially bring the claim within coverage.
- **Late notice prejudice**: California law (Cal. Insurance Code SS 554)
  generally requires the insurer to demonstrate prejudice before denying coverage
  for late notice on occurrence policies. Rules vary by state for multi-state
  matters.
- **Excess/umbrella coverage**: Notification may be required to excess and
  umbrella carriers in addition to primary carriers.

**Sub-categories**:

- Initial claim notification / circumstance notification
- Supplemental information
- Response to reservation of rights letter
- D&O / E&O / Cyber policy notifications (often have unique requirements)

**Key template elements**:

- Policy number, insurer name, broker details, and coverage period
- Claims-made vs. occurrence classification
- Description of the matter, incident, or circumstance
- Timeline of events
- Quote of specific policy notification clause being complied with
- Requested coverage confirmation (including duty to defend, if applicable)
- Without prejudice / reservation of rights language
- Notice to excess/umbrella carriers if potentially implicated

---

## Template Management Framework

### Template Organization

Templates should be organized by category and maintained in the team's document
management system or local settings. Each template should include:

| Element                    | Description                                     | Required |
| -------------------------- | ----------------------------------------------- | -------- |
| **Category**               | Response category (Consumer Rights, Hold, etc.) | Yes      |
| **Template name**          | Descriptive identifier                          | Yes      |
| **Version**                | Version number for change tracking              | Yes      |
| **Last reviewed**          | Date of last legal review                       | Yes      |
| **Approved by**            | Name/title of approving attorney                | Yes      |
| **Applicable legislation** | Relevant statutes and regulations               | Yes      |
| **Use case**               | When this template is appropriate               | Yes      |
| **Escalation triggers**    | When NOT to use this template                   | Yes      |
| **Required variables**     | Information that must be customized             | Yes      |
| **Template body**          | Response text with variable placeholders        | Yes      |
| **Follow-up actions**      | Standard steps after sending                    | Yes      |
| **Notes**                  | Special instructions for users                  | Optional |

### Template Lifecycle

1. **Creation**: Draft based on current California/US law, CPPA regulations, AG
   guidance, and team input
2. **Review**: Attorney review and approval of template content
3. **Publication**: Add to template library with full metadata
4. **Use**: Generate responses using the template
5. **Feedback**: Track when templates are modified during use -- identify
   improvement needs
6. **Update**: Revise when statutes, regulations, CPPA rulemaking, AG guidance,
   or best practices change
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

[Special instructions, including CPPA/AG guidance references]
```

---

## Customization Guidelines

### Required Customization

Every templated response MUST be customized with:

- Correct names, dates, and reference numbers
- Specific facts of the situation (not generic placeholders)
- Correct California/US regulation and provision citations
- Correct response deadlines calculated from the date of receipt (45 calendar
  days for CCPA consumer rights requests)
- Appropriate signature block and contact information
- CPPA and AG complaint rights where required for consumer rights responses
- Non-discrimination notice for CCPA consumer rights responses
- "Do Not Sell or Share My Personal Information" link reference where applicable

### Tone Adjustment Matrix

| Dimension        | Options                               | Guidance                                  |
| ---------------- | ------------------------------------- | ----------------------------------------- |
| **Audience**     | Internal / External / Regulatory      | Regulatory = most formal, precise         |
| **Relationship** | New / Existing / Adversarial          | Adversarial = more guarded, no admissions |
| **Sensitivity**  | Routine / Contentious / Investigation | Investigation = attorney review required  |
| **Urgency**      | Standard / Expedited / Overdue        | Overdue = acknowledge delay, explain      |

### Jurisdiction-Specific Checks

Before sending any response, verify:

- [ ] CCPA/CPRA cited with specific Cal. Civ. Code section numbers (not just
      "California privacy law")
- [ ] Timelines match applicable law (45 calendar days for CCPA consumer rights
      requests, not "30 days" or "one month")
- [ ] US legal terminology used: attorney (not solicitor), plaintiff (not
      claimant), complaint (not claim form), discovery (not disclosure),
      subpoena (not witness summons), deposition, interrogatories, motion to
      quash, attorney-client privilege (not legal professional privilege)
- [ ] Correct regulators named (CPPA, California AG, FTC -- not "supervisory
      authority" or "ICO")
- [ ] California court references accurate (Superior Court, Court of Appeal,
      Supreme Court of California; or applicable federal court)
- [ ] Privilege marking uses US convention: "ATTORNEY-CLIENT PRIVILEGED AND
      CONFIDENTIAL" and/or "ATTORNEY WORK PRODUCT"

---

## Quality Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                                                                                       | Fail Action                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **Source**     | Every regulatory reference cites specific Cal. Civ. Code section, CFR section, or USC section                                                              | Add citation or mark "[VERIFY]"                |
| **Format**     | Citations use standard US legal citation format (Cal. Civ. Code SS X, 15 U.S.C. SS X, 11 CCR SS X)                                                         | Fix format                                     |
| **Currency**   | Cited provisions, CPPA regulations, and AG guidance confirmed current                                                                                      | Flag "[CHECK CURRENCY]"                        |
| **Domain**     | US legal terminology throughout: attorney (not solicitor), discovery (not disclosure), subpoena (not witness summons), attorney-client privilege (not LPP) | Fix terminology                                |
| **Confidence** | If template is being stretched beyond its designed use case, flag it                                                                                       | Add "[ATTORNEY TO REVIEW -- template adapted]" |

### Self-Interrogation for High-Stakes Responses

For any response involving regulators, legal process, or potential litigation,
apply this 3-pass review:

**Pass 1 -- Completeness**: Does the response include all legally required
elements under California and US federal law? Are all statutory rights mentioned?
Are all deadlines correctly calculated (45 days, not 30 days or "one month")?
Are CPPA/AG complaint rights included where required?

**Pass 2 -- Accuracy**: Are all statutory citations correct and current? Is the
terminology appropriate (US English, US legal terms)? Are there any statements
that could be construed as admissions or waivers? Are CPPA regulation citations
accurate (11 CCR SS 7000 et seq.)?

**Pass 3 -- Appropriateness**: Is a templated response actually appropriate here,
or should this be escalated? Have all escalation triggers been checked? Would a
reasonable California-licensed attorney approve sending this without further
review?

### Confidence Scoring

| Level        | Range     | Meaning                            | Action                          |
| ------------ | --------- | ---------------------------------- | ------------------------------- |
| **Definite** | 0.95-1.0  | Standard template, routine matter  | Send after standard review      |
| **High**     | 0.80-0.94 | Minor customization, known pattern | Send with quality check         |
| **Probable** | 0.60-0.79 | Significant adaptation required    | Senior review before sending    |
| **Possible** | 0.40-0.59 | Template being stretched           | Attorney review required        |
| **Unlikely** | 0.0-0.39  | Template not appropriate           | Do not use template -- escalate |

### Glass Box Audit Trail

Every generated response MUST include an internal Glass Box audit record. This is
retained in the matter file -- NOT sent to the recipient.

```yaml
glass_box:
  inquiry_type: "[Consumer rights request / Litigation hold / Privacy inquiry / Vendor / NDA / Legal process / Insurance]"
  template_used: "[Template name and version, or 'Generated from framework']"
  template_modified: "Yes / No -- if yes, [what was changed and why]"
  jurisdiction: "United States -- California"
  regulations_applied:
    - "Cal. Civ. Code Section [X]"
    - "11 CCR Section [X]"
    - "[Other applicable statutes/regulations]"
  citations_verified:
    - "[Citation] -- VERIFIED / UNVERIFIED"
  deadline_calculation:
    received: "[YYYY-MM-DD]"
    deadline: "[YYYY-MM-DD]"
    basis: "45 calendar days from receipt of verifiable request (Cal. Civ. Code Section 1798.130(a)(2))"
  exemptions_applied:
    - "[Exemption] -- [Legal basis] -- [Applied to: description]"
  escalation_triggers_checked:
    - "[Trigger 1] -- Present / Not present"
  confidence: "HIGH / MEDIUM / LOW -- [rationale]"
  quality_gates_passed: "5/5 or [list failures]"
  reviewer: "[Name or 'AI-assisted -- requires attorney review before sending']"
  follow_up_actions:
    - "[Action 1]"
```

---

## Writing Standards

Templated legal responses must be clear, professional, and understandable by
their intended audience. Apply these standards to every response.

### Language and Spelling

Use **American English** spelling and conventions throughout:

- organization (not organisation)
- color (not colour)
- program (not programme)
- defense (not defence)
- analyze (not analyse)
- fulfill (not fulfil)
- practice (noun and verb, not practise)
- judgment (not judgement, except in UK court titles)
- canceled (not cancelled)
- labeled (not labelled)

### Three-Pass Editing

**Pass 1 -- Structure**: Does the response answer the inquiry? Is information in
logical order? Is anything missing? Is anything unnecessary?

**Pass 2 -- Clarity**: Can the recipient understand this without legal training
(where appropriate)? Replace passive constructions with active voice. Ensure
every pronoun has a clear antecedent. Remove ambiguity.

**Pass 3 -- Concision**: Cut padding, hedging, and unnecessary qualifiers.
Replace long words with short where meaning is preserved. Remove jargon unless
the audience expects it. Target 20-30% word count reduction from first draft.

### Specific Rules

- **Active voice**: "We received your request on January 15" not "Your request
  was received on January 15"
- **Name the actor**: "The CPPA can investigate" not "An investigation may be
  commenced"
- **Plain language for consumers**: Consumer rights responses go to people who
  may have no legal knowledge. Write accordingly.
- **Formal but clear for regulators**: The CPPA, California AG, and FTC
  appreciate factual, well-organized responses. Avoid advocacy language in
  factual submissions.
- **Precise for preservation notices**: Litigation holds must be unambiguous.
  "You must not delete emails" is better than "Please ensure electronic
  communications are preserved in accordance with the organization's document
  retention policy."
- **No hidden complexity**: Obscure language that makes it harder for consumers
  to understand their rights is not just bad writing -- it risks enforcement
  action, including dark-pattern scrutiny under CPPA regulations.
- **US date format**: January 15, 2026 (not 15 January 2026)

### Quality Gates Before Sending

1. Would a non-lawyer recipient understand this response (where applicable)?
2. Are all regulatory references correct and current?
3. Is the deadline correctly calculated (45 calendar days for CCPA requests)?
4. Are CPPA/AG complaint rights included where required?
5. Has every escalation trigger been checked?
6. Is this response appropriate for the specific facts, or is it generic
   boilerplate?
7. Have all variables been replaced with actual values (no {{placeholders}}
   remain)?
8. Is non-discrimination language included where required?
9. Are "Do Not Sell or Share" link references included where applicable?

---

## Anti-Patterns

What NOT to do with templated legal responses under California/US law:

1. **Sending a template without customization** -- A response with
   "{{requester_name}}" or other unfilled variables is worse than no response.
   Every variable must be filled. Every response must be reviewed against the
   specific facts.

2. **Using incorrect timeline formulations** -- CCPA consumer rights requests
   require a response within **45 calendar days**, extendable by 45 additional
   calendar days. This is different from GDPR's "one calendar month." Applying
   the wrong deadline is a compliance failure.

3. **Ambiguous regulation citations** -- Citing "California privacy law" without
   specifying CCPA/CPRA section numbers is imprecise. Citing "federal law"
   without specifying the statute is useless. Always cite the specific statute
   and provision (e.g., Cal. Civ. Code SS 1798.105 for deletion rights).

4. **Applying exemptions without documentation** -- "We've applied an exemption
   to some information" is insufficient. Each exemption must be applied to
   specific data with a documented reason and specific statutory basis, retained
   in the matter file for potential CPPA or AG inquiry.

5. **Vague preservation notices** -- A litigation hold that politely asks
   custodians to "please keep relevant documents" does not convey the severity.
   Explain the consequences: adverse inference instructions, monetary sanctions,
   and potential case-dispositive sanctions under FRCP Rule 37(e).

6. **Templated responses to regulators** -- Never send a template response to
   the CPPA, California AG, FTC, or any other regulator without individualized
   attorney review. Regulators recognize boilerplate, and it signals the
   organization is not taking the matter seriously.

7. **Omitting mandatory disclosures** -- Forgetting to include CPPA/AG
   complaint rights in consumer rights responses, or omitting the
   non-discrimination notice, is a compliance failure, not just a drafting
   error.

8. **Using wrong jurisdiction's terminology** -- "Disclosure" / "witness
   summons" / "legal professional privilege" / "solicitor" are UK terms. In
   California/US practice, use: discovery, subpoena, attorney-client privilege,
   attorney. Using the wrong terms in formal communications is unprofessional
   and may confuse recipients.

9. **Missing deadlines without extension notice** -- If you need more time for
   a CCPA consumer rights request, you must notify the consumer within the
   original 45-day period and explain why. Silently missing the deadline is a
   compliance breach that may result in CPPA or AG enforcement.

10. **Fire-and-forget responses** -- Every response needs follow-up actions:
    log the response, schedule follow-up deadlines, update the matter file,
    close the request only when fully resolved. CCPA requires retention of
    request records for at least 24 months (11 CCR SS 7101).

11. **Ignoring escalation triggers** -- Proceeding with a templated response
    when an escalation trigger is present. The escalation check exists because
    some situations cannot be safely handled with templates.

12. **Template scope creep** -- Using a template designed for one situation
    (e.g., simple consumer rights acknowledgment) for a different situation
    (e.g., complex request with exemptions and authorized agent issues). Each
    template has a designed use case -- respect its boundaries.

13. **Copying without understanding** -- Using template language without
    understanding why it exists. If you cannot explain why each element of the
    response is there, you should not be sending it.

14. **Inconsistent variable naming** -- Using {{name}}, {{requester_name}},
    {{consumer}}, and {{data_subject}} interchangeably in the same template
    library. Standardize variable names across all templates.

15. **No version control** -- Failing to track template versions, leading to
    outdated templates being used after law changes. CPPA rulemaking is ongoing;
    templates must be updated when new regulations take effect. Every template
    needs a version number and last-reviewed date.

16. **Privilege marking errors** -- Using the wrong privilege assertion. Under
    California/US law, use "ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL" and/or
    "ATTORNEY WORK PRODUCT." Do not use "SUBJECT TO LEGAL PROFESSIONAL
    PRIVILEGE" (UK convention). Incorrect privilege marking may create confusion
    about the privilege assertion and, in adversarial contexts, may be used to
    argue waiver or ambiguity.

17. **Ignoring GPC signals** -- Failing to process Global Privacy Control (GPC)
    opt-out preference signals as valid opt-out requests under CCPA/CPRA and
    CPPA regulations. GPC signals must be treated as valid consumer opt-out
    requests (Cal. Civ. Code SS 1798.135(b); 11 CCR SS 7025).

18. **Conflating CCPA roles** -- Referring to a "service provider" when the
    entity is actually a "contractor" or "third party" under CCPA definitions.
    Each classification carries different contractual and operational
    requirements (Cal. Civ. Code SS 1798.140).

---

## External Tool Integration

### legalcode-mcp Integration

If **legalcode-mcp** is connected, use it for:

- Verifying current California statutory text and CPPA regulations
- Checking recent CPPA enforcement actions and AG guidance updates
- Validating deadline calculations against current law
- Monitoring CPPA rulemaking docket for upcoming regulation changes
- Researching California-specific requirements (CMIA, AB 2273, Cal. Labor Code)

**With legalcode-mcp connected:**

- Mark verified citations as `VERIFIED` in the Glass Box audit trail
- Update templates based on recent CPPA regulatory guidance

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
- CCPA request log (11 CCR SS 7101 requires 24-month retention)

---

## Output Format Template

When generating a response, structure the output as follows:

````markdown
## Generated Response

**Category**: [Response category]
**Template**: [Template name and version, or "Generated from framework"]
**Jurisdiction**: United States -- California
**Confidence**: [HIGH / MEDIUM / LOW]

---

### Response Text

[The actual response to be sent, fully customized with all variables filled]

---

### Internal Notes (Do Not Send)

**Deadline**: [Calculated deadline and basis]

**Escalation triggers checked**:

- [x] [Trigger 1] -- Not present
- [x] [Trigger 2] -- Not present
- [If any present, explain why proceeding or recommend escalation]

**Required follow-up actions**:

1. [Action 1 with deadline if applicable]
2. [Action 2]
3. Log in CCPA request tracking system (24-month retention per 11 CCR
   Section 7101)

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

**Ready to send**: [Yes -- after attorney review / No -- escalation required]

```

---

## Provenance

- **Original synthesis**: Legalcode (2026-02-27)
- **Base skill**: `skills/general/workflows/legalcode-canned-responses/SKILL.md`
  (jurisdiction-agnostic version)
- **California law reference skill**:
  `skills/jurisdictions/united-states/california/compliance/ccpa-cpra-consumer-rights-operations/SKILL.md`
- **Quality framework reference**:
  `skills/general/workflows/imported-uk-legal-plugins--skills-uk-legal-canned-responses/SKILL.md`
  (45black/uk-legal-plugins)
- **Jurisdiction**: United States -- California
- **Primary statutory sources**:
  - California Consumer Privacy Act / California Privacy Rights Act (Cal. Civ.
    Code SS 1798.100-1798.199.100)
  - CPPA regulations (11 CCR SS 7000 et seq.)
  - Federal Rules of Civil Procedure (FRCP)
  - California Code of Civil Procedure (Cal. CCP)
  - California Evidence Code SS 950-962
  - COPPA (15 U.S.C. SS 6501-6506)
  - California Age-Appropriate Design Code Act (AB 2273)
  - CMIA (Cal. Civ. Code SS 56-56.37)
  - CFAA (18 U.S.C. SS 1030)
  - ESIGN Act (15 U.S.C. SS 7001 et seq.)
  - California UETA (Cal. Civ. Code SS 1633.1 et seq.)
  - Cal. Business and Professions Code SS 16600
  - California Transparency in Supply Chains Act (Cal. Civ. Code SS 1714.43)
- **License**: Apache-2.0 (consistent with source skills)
```
