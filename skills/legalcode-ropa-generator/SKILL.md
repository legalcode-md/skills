---
name: legalcode-ropa-generator
description: >
  Generate Article 30 Records of Processing Activities (RoPA) for controllers and
  processors under GDPR, UK GDPR, Swiss FADP, and Brazil LGPD. Use when creating or
  auditing a processing register, onboarding a new business unit into a data inventory,
  assessing ROPA completeness before a supervisory authority audit, building a
  department-by-department data inventory, or integrating data mapping outputs into a
  supervisory-authority-ready ROPA format. Supports controller RoPA (Art. 30(1)) and
  processor RoPA (Art. 30(2)) with distinct mandatory-field coverage, Art. 30(5) SME
  exemption screening, multi-regime jurisdictional overlays, and machine-readable
  export hooks. Produces both summary and detailed ROPA formats with completeness
  scoring and prioritized remediation.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode ROPA Generator

> **Disclaimer**: This skill provides a framework for AI-assisted generation and review of
> Records of Processing Activities (RoPAs). It does not constitute legal advice. All ROPA
> outputs must be reviewed by a qualified data protection professional or legal counsel
> licensed in the relevant jurisdiction before being submitted to a supervisory authority,
> shared externally, or relied upon for compliance purposes. Privacy laws and regulatory
> guidance evolve — verify currency before treating any provision here as current. Legal
> references and regulatory citations from training data carry hallucination risk; verify
> against authoritative primary sources before relying on them. Mark any unverified claim
> with **[VERIFY]** before delivery.

## Purpose and Scope

This skill generates, audits, and completes Records of Processing Activities (RoPAs) as
required under GDPR Article 30, UK GDPR Article 30, Swiss FADP Article 12, and Brazil
LGPD Article 37. It supports the full ROPA lifecycle — from initial exemption screening
through department-by-department discovery, mandatory-field population, completeness
assessment, and supervisory-authority-ready output.

**Covers:**
- Art. 30(5) exemption screening before building the ROPA
- Controller RoPA (Art. 30(1)) with all 13 mandatory field categories
- Processor RoPA (Art. 30(2)) with all 11 mandatory field categories
- Department-by-department discovery questionnaire for data inventory
- Legal basis assignment and special category / criminal data documentation
- Recipient, sub-processor, and third-country transfer mapping
- Retention schedule assignment with trigger-and-period specificity
- Technical and Organisational Measures (TOM) description at ROPA depth
- GREEN / YELLOW / RED completeness classification per processing activity
- LIA and DPIA cross-reference tracking
- Multi-regime compliance overlays (EU GDPR / UK GDPR / Swiss FADP / Brazil LGPD)
- Machine-readable export hooks for ROPA management tools
- Maintenance calendar and real-time update trigger system
- Supervisory authority submission readiness checklist

**Does not:**
- Replace a Data Protection Impact Assessment (see `legalcode-dpia-generator`)
- Conduct a full data mapping discovery exercise (see `legalcode-data-mapping-workflow`)
- Draft Data Processing Agreements (see `legalcode-data-processing-agreement-drafter`)
- Provide legal advice or replace qualified data protection counsel
- Guarantee compliance with any jurisdiction — outputs require professional verification

**Related skills:**
- `legalcode-data-mapping-workflow` — discovery upstream of ROPA population
- `legalcode-dpia-generator` — DPIA for activities flagged by ROPA
- `legalcode-legitimate-interest-assessment` — LIA for Art. 6(1)(f) activities
- `legalcode-cross-border-transfer-assessment` — deep transfer mechanism analysis
- `legalcode-dsar-workflow-builder` — DSAR workflow fed by ROPA system inventory

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware across four regimes. The applicable regime is determined
during Step 3 and conditions the mandatory field matrix, classification criteria, and
output format.

| Regime | Instrument | ROPA Equivalent | Key Difference |
|--------|-----------|----------------|---------------|
| **EU GDPR** | Art. 30 GDPR (Reg. 2016/679) | Records of Processing Activities | Reference standard; mandatory legal basis in practice |
| **UK GDPR** | Art. 30 UK GDPR (onshored via EU Withdrawal Act 2018 + DPA 2018) | Records of Processing Activities | Must document DPA 2018 Sch. 1 conditions; UK IDTA for transfers |
| **Swiss FADP** | Art. 12 FADP (effective 1 Sept 2023) | Bearbeitungsverzeichnis | No "where possible" qualifier for TOMs; federal bodies must report via DataReg |
| **Brazil LGPD** | Art. 37 LGPD (Lei 13.709/2018) | Registro das atividades de tratamento | Sparse statutory text; ANPD non-binding template; "especially when legitimate interest" |

[JURISDICTION-SPECIFIC] When the governing jurisdiction differs from EU GDPR, apply the
regime-specific field matrix in Step 6 and the localization notes in Section 15 of this skill.

[JURISDICTION-SPECIFIC] For organizations with processing in multiple jurisdictions,
apply the most demanding regime as the baseline and note supplementary requirements per
regime in the output.

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at key decision points. Rather
than assuming intent, the workflow pauses and asks when the answer materially changes the
analysis direction, the mandatory field set, or the output format.

In non-interactive (batch) mode, apply these defaults and state assumptions explicitly:
- Side: Controller (Art. 30(1))
- Exemption: Exemption does not apply — full ROPA required
- Regime: EU GDPR primary with overlays as described
- Scope: Full organization ROPA across all departments

---

## Workflow

### Step 1: Accept Input

Accept input in any of the following formats:

- **Existing ROPA** (spreadsheet, document, JSON, XML): Audit existing entries for
  completeness, classify each activity, and generate a gap remediation plan
- **Data mapping output**: Accept the output of `legalcode-data-mapping-workflow` and
  convert it to a ROPA-format register with mandatory-field coverage
- **Organizational description**: Accept a narrative or bullet list of the organization's
  functions, systems, and data types — build the ROPA from scratch using the
  department-by-department discovery questionnaire (Step 5)
- **Single processing activity**: Accept a description of one processing activity and
  generate or audit that single ROPA entry
- **Template request**: Generate a blank ROPA template for a controller or processor,
  pre-populated with the mandatory fields and guidance text

If no input is provided, prompt the user to supply one of the above.

### Step 2: Art. 30(5) Exemption Screening

Before building or auditing the ROPA, determine whether the organization is required to
maintain one at all.

**⟁ CLARIFY** — Ask the following three questions to assess the Art. 30(5) exemption:

1. **Organization size**: How many employees does the organization have?
   - Options: Fewer than 250, 250 or more, Unsure

2. **Processing regularity**: Does the organization process personal data on a regular,
   ongoing basis (e.g., HR records, customer database, website analytics, marketing emails)?
   - Options: Yes — regularly, No — only occasionally and one-off, Unsure

3. **Data sensitivity**: Does the organization process any of the following? (multi-select)
   - Special category data (Art. 9): health, biometric, genetic, racial/ethnic origin,
     political opinions, religious beliefs, trade union membership, sexual orientation
   - Criminal conviction or offence data (Art. 10)
   - None of the above

**Exemption determination logic:**

| Condition | Result |
|-----------|--------|
| 250 or more employees | **ROPA REQUIRED** — exemption not available |
| Fewer than 250 AND processing is regular/ongoing | **ROPA REQUIRED** — "not occasional" trigger |
| Fewer than 250 AND processes special category or criminal data | **ROPA REQUIRED** — data sensitivity trigger |
| Fewer than 250 AND processing is likely to risk data subject rights | **ROPA REQUIRED** — risk trigger |
| Fewer than 250 AND genuinely occasional AND no sensitive data AND low risk | **EXEMPTION MAY APPLY** — document the decision |

> **Warning — Exemption is nearly illusory in practice**: Any organization that maintains
> employee records, operates a CRM, runs a website with analytics, or sends marketing
> emails processes data on a "not occasional" basis. The exemption is designed for
> genuinely one-off processing (e.g., a community event organizer collecting one
> attendance list). Supervisory authorities interpret "occasional" very narrowly.
> [VERIFY — EDPB WP29 Position Paper 19 April 2018; 2025 Omnibus IV proposes 750-employee
> threshold but is not yet law as of this skill's creation]

If the exemption may apply, produce a written **Exemption Decision Record** with:
- Organization size and basis for that figure
- Rationale why processing is genuinely occasional
- Confirmation that no special category or criminal data is processed
- Risk assessment showing no likely risk to data subject rights
- Recommendation to seek legal advice before relying on the exemption

If ROPA is required, proceed to Step 3.

### Step 3: Determine Organization Role

**⟁ CLARIFY** — Ask the user which ROPA variant is needed:

1. **Organization role**:
   - **Controller** — the organization determines the purposes and means of processing
     → Apply Art. 30(1) mandatory field matrix (13 fields; includes purposes and legal basis)
   - **Processor** — the organization processes data only on behalf of controllers
     → Apply Art. 30(2) mandatory field matrix (11 fields; no legal basis required)
   - **Both controller and processor** — the organization acts as controller for some
     activities and processor for others → Generate two separate ROPA documents

   *Why this matters*: The mandatory field set differs fundamentally. Controllers must
   document purposes, legal basis, data subject categories, and personal data categories.
   Processors document what they *do* for each controller — not why it is done. Confusing
   the two is the most common ROPA structural error.

2. **Scope**:
   - Full organization (all departments, all processing activities)
   - Single department or business unit
   - Single processing activity
   - Audit of existing ROPA entries only

### Step 4: Identify Applicable Regimes

**⟁ CLARIFY** — Ask which regimes apply:

1. **Primary regime**:
   - EU GDPR (organization is established in EU, or targets/monitors EU data subjects)
   - UK GDPR (organization is established in UK, or targets/monitors UK data subjects)
   - Swiss FADP (organization is established in Switzerland, or targets Swiss data subjects)
   - Brazil LGPD (organization is established in Brazil, or processes Brazilian data)

2. **Additional regime overlays**: Select all that apply
   - US state privacy laws (CCPA/CPRA, VCDPA, CPA, etc.) — note: no ROPA equivalent,
     but data inventory obligations apply; document in Part G of the output
   - PIPEDA + Québec Law 25 — Law 25 adds mandatory "information register" obligations
   - APPI (Japan) — Art. 24 requires documentation; record cross-border transfer grounds
   - PDPA (Thailand/Singapore) — processing records obligations apply [VERIFY]

3. **Sector-specific overlays** (select all that apply):
   - Healthcare / HIPAA: Additional retention requirements; minimum necessary standard
   - Financial services / PCI DSS: Cardholder data processing scope
   - Telecoms / ePrivacy Directive: Traffic and location data processing rules
   - Children's data / COPPA / AADC: Age-appropriate design and parental consent overlay
   - Employment: Employment law retention minimums by jurisdiction

For each applicable regime, apply the regime-specific mandatory field additions documented
in the Mandatory Field Reference in Section 7 below.

### Step 5: Department-by-Department Discovery Questionnaire

If building the ROPA from scratch (not auditing existing entries), conduct structured
discovery using this questionnaire. Issue to each department head or process owner.

> **Instruction**: Send this questionnaire to each business unit. The skill will aggregate
> responses into ROPA entries. One questionnaire response may produce one or more entries.
> A single "activity" is defined as a distinct combination of purpose + legal basis +
> data category. If a department processes customer data for invoicing (one legal basis)
> and for marketing (a different legal basis), these are two separate ROPA entries.

---

**Department ROPA Discovery Questionnaire**

*Department/Business Unit*: ______________________
*Completed by*: ______________________
*Date*: ______________________
*Reviewed by DPO*: ______________________

**Section A — Processing Activities**

For each distinct processing activity in your department:

1. **What is the specific purpose of this processing?**
   (Be precise — "marketing purposes" is insufficient. Write: "sending monthly newsletter
   to consenting subscribers to promote product updates." One purpose per entry.)

2. **What personal data do you collect or use?**
   (List specific data fields — e.g., name, email, date of birth, IP address, health data.
   Do not generalize as "personal data.")

3. **Who are the individuals whose data you process?**
   (e.g., customers, employees, job applicants, website visitors, business contacts,
   children under 16, vulnerable individuals)

4. **What is the legal basis for this processing?**
   - Art. 6(1)(a) — Consent (do you have documented consent records?)
   - Art. 6(1)(b) — Necessary for a contract with the individual
   - Art. 6(1)(c) — Necessary to comply with a legal obligation (cite the law)
   - Art. 6(1)(d) — Necessary to protect vital interests
   - Art. 6(1)(e) — Necessary for public task
   - Art. 6(1)(f) — Legitimate interests (has a Legitimate Interest Assessment been done?)

5. **Do you process any special category data?** (Art. 9 — health, biometric, genetic,
   racial/ethnic, political, religious, trade union, sexual orientation data)
   - If yes: Which Art. 9(2) condition applies? (e.g., explicit consent, employment law,
     substantial public interest, health care, legal claims)
   - UK only: Which DPA 2018 Schedule 1 condition applies?

6. **Do you process criminal conviction or offence data?** (Art. 10)
   - If yes: What authorizes this processing?

7. **Who receives this data?** (List all recipients)
   - Internal departments or teams
   - Third-party organizations (name each, and whether they are processors or controllers)
   - Government agencies or regulators (name each)
   - Is data shared with organizations in countries outside the EU/UK/Switzerland/Brazil?
     (name the countries and the transfer mechanism used)

8. **Which external processors (vendors) do you use for this activity?**
   (e.g., cloud providers, CRM vendors, analytics tools, payroll providers — name each)

9. **How long is the data retained?**
   (State a specific period — e.g., "7 years after end of tax year" not "as required by law."
   What triggers deletion? What is the deletion method?)

10. **What security measures apply to this processing?**
    (e.g., encryption at rest and in transit, access controls, MFA, backups, ISO 27001,
    SOC 2, penetration testing frequency)

11. **Is this processing used for automated decision-making or profiling?** (Art. 22)
    - If yes: Does the decision produce legal or similarly significant effects on individuals?
    - Have you conducted a DPIA for this automated decision-making?

12. **Has a Data Protection Impact Assessment (DPIA) been conducted for this activity?**
    - Yes — DPIA ID: ____________ Status: ____________
    - No — should one be conducted? (Will be assessed in Step 11)
    - Not required — basis: ____________

---

### Step 6: Process Activity Population

Using the discovery questionnaire responses (Step 5) or the input ROPA / data mapping
output, populate each processing activity entry.

Apply the mandatory field matrix appropriate to the organization's role:

#### Controller ROPA Entry — Art. 30(1) Mandatory Fields

| # | Field | Mandatory? | Notes |
|---|-------|-----------|-------|
| C1 | **Controller name** | Yes | Legal entity name of the controller |
| C2 | **Controller contact details** | Yes | Address, email, phone |
| C3 | **Joint controller name and contact** | If applicable | Any entity jointly determining purposes and means |
| C4 | **Controller's EU representative** | If applicable | Required for non-EU controllers targeting EU data subjects |
| C5 | **Data Protection Officer contact** | If applicable | Required if DPO appointed; name and contact |
| C6 | **Processing activity name** | Best practice | Short descriptive label per activity |
| C7 | **Processing purposes** | Yes | Specific, substantiated purpose — not generic |
| C8 | **Legal basis (Art. 6)** | Best practice (EDPB-recommended; required by Art. 5(2)) | Specify sub-paragraph; document LIA reference for Art. 6(1)(f) |
| C9 | **Art. 9 condition** | If special category data | Specify Art. 9(2) sub-paragraph |
| C10 | **DPA 2018 Schedule 1 condition** | UK only, if Art. 9 applies | Cross-reference Schedule 1 condition |
| C11 | **Art. 10 authorisation** | If criminal data | Specify domestic law authorisation |
| C12 | **Categories of data subjects** | Yes | Employees, customers, job applicants, children, etc. |
| C13 | **Categories of personal data** | Yes | Specific data types (name, email, IP address, etc.) |
| C14 | **Categories of recipients** | Yes | Internal and external recipients; named processors |
| C15 | **Third-country recipients** | If applicable | Named countries receiving data |
| C16 | **Transfer mechanism** | If third-country transfer | SCCs (module), IDTA, adequacy decision, BCR, Art. 49 derogation |
| C17 | **Envisaged time limits for erasure** | Yes ("where possible") | Specific period + trigger + deletion method |
| C18 | **General description of TOMs** | Yes ("where possible") | Encryption, access controls, certifications |
| C19 | **Profiling / ADM flag** | Best practice | Art. 22 screening result |
| C20 | **DPIA status** | Best practice | Completed, pending, or basis for no DPIA required |
| C21 | **LIA reference** | Best practice if Art. 6(1)(f) | LIA document ID and completion status |
| C22 | **Business unit / data owner** | Best practice | Department responsible for this activity |
| C23 | **Source of personal data** | Best practice | Directly from subject, third party, or public source |
| C24 | **Review date** | Best practice | When entry was last reviewed and by whom |

#### Processor ROPA Entry — Art. 30(2) Mandatory Fields

| # | Field | Mandatory? | Notes |
|---|-------|-----------|-------|
| P1 | **Processor name** | Yes | Legal entity name of the processor |
| P2 | **Processor contact details** | Yes | Address, email, phone |
| P3 | **Processor's EU representative** | If applicable | For non-EU processors |
| P4 | **DPO contact** | If applicable | Processor's DPO, if appointed |
| P5 | **Controller name(s)** | Yes | Each controller on whose behalf the processor acts |
| P6 | **Controller contact details** | Yes | For each controller — name and contact |
| P7 | **Controller's EU representative** | If applicable | For each controller without EU establishment |
| P8 | **Categories of processing** | Yes | Per each controller — describe what types of processing are carried out |
| P9 | **Sub-processors used** | Best practice (required in DPA; should mirror here) | Name, function, and location of each sub-processor |
| P10 | **Third-country transfers** | If applicable | Countries to which data is transferred |
| P11 | **Transfer mechanism** | If third-country transfer | Per each transfer — SCCs module, adequacy, BCR |
| P12 | **General description of TOMs** | Yes | Security measures per Art. 32(1) |
| P13 | **Processing categories per controller** | If multiple controllers | Separate section per controller where different |
| P14 | **Sub-processor notification protocol** | Best practice | When and how controllers are notified of sub-processor changes |

> **Key distinction**: Processors do NOT document processing purposes, data subject
> categories, personal data categories, or retention periods. These are the controller's
> responsibility. The processor records what it *does* — not why. Documenting purposes
> in a processor ROPA is a structural error that creates confusion about role boundaries.

### Step 7: Recipient, Sub-Processor, and Transfer Mapping

For each processing activity, conduct a systematic recipient audit:

**7a — Internal Recipients**
- List internal teams, departments, or roles that have access to the data
- Document access basis (role-based access control, need-to-know)

**7b — External Processors**
- For each vendor, cloud provider, or SaaS tool that processes personal data on the
  organization's behalf:
  - Confirm a Data Processing Agreement (DPA/DPA) is in place
  - Record the processor name, processing function, data categories processed, and location
  - For sub-processors: record each sub-processor the processor is authorized to use
  - Note whether authorization is specific (named sub-processors) or general (categories)

**7c — Third-Party Controllers**
- For data disclosed to recipients who determine their own purposes (not processors),
  record the recipient, the disclosure basis, and the categories of data disclosed

**7d — International Transfer Mapping**
For each transfer of personal data to a country outside the EEA / UK / Switzerland / Brazil:

| Transfer Field | Content |
|---------------|---------|
| Destination country | Named country |
| Recipient name and role | Controller or processor |
| Transfer mechanism | Adequacy decision / EU SCCs (Module 1-4) / UK IDTA / UK SCCs + Addendum / Swiss FADP SCCs / BCRs / Art. 49 derogation |
| SCC Module | Controller-to-controller (M1), Controller-to-processor (M2), Processor-to-controller (M3), Processor-to-processor (M4) |
| Transfer Risk Assessment | Completed / Pending / Not required (adequacy) |
| Transfer mechanism document reference | DPA clause, SCC execution date, BCR approval date |
| Transfer mechanism status | Current / Requires renewal |

> **Common gap**: Many organizations fail to recognize that using US-headquartered SaaS
> providers (AWS, Google Workspace, Microsoft 365, Salesforce) constitutes a restricted
> transfer if data is processed on US servers. The EU-US Data Privacy Framework (adequacy
> decision, July 2023) covers DPF-certified organizations — verify each vendor's
> certification status. [VERIFY — adequacy decision status and DPF certification list]

**⟁ CLARIFY** — If any transfer destination lacks a documented mechanism:
- Flag as RED (blocking gap)
- Ask the user to identify the mechanism or confirm suspension of that transfer

### Step 8: Retention Schedule Assignment

For each processing activity, document the full retention lifecycle:

| Retention Field | Content |
|----------------|---------|
| Retention trigger | What event starts the retention clock (e.g., end of contract, date of last transaction, departure of employee) |
| Retention period | Specific duration from trigger (e.g., "7 years," "2 years," "1 month") |
| Statutory basis | Legal or regulatory requirement driving the period, if any |
| Deletion method | How data is deleted (e.g., secure deletion, anonymization, physical destruction) |
| Deletion responsibility | Which team or system performs the deletion |
| Exception | Any category of data retained longer, and the basis |

> **Supervisory authority red flag**: Retention entries that say "as required by law,"
> "see retention policy," or contain hyperlinks to external documents are consistently
> flagged in DPC and ICO audits as inadequate. The ROPA entry itself must state the
> specific period and trigger. Reference numbers to external policies are acceptable as
> supplementary, not as a substitute.

**Common retention periods by data category** (verify against applicable jurisdiction):

| Data Category | Common Minimum Period | Common Maximum Period | Notes |
|--------------|----------------------|----------------------|-------|
| Employee payroll records | 3 years | 7 years | Tax law drives minimum; varies by jurisdiction |
| Employee personnel files | End of employment + 6 years | End of employment + 10 years | Statute of limitations for claims |
| Customer invoices | 5 years | 10 years | VAT / tax law; insolvency law |
| Customer contracts | Term + 6 years | Term + 10 years | Limitation periods |
| Marketing consent records | Duration of consent + 3 years | Duration of consent + 5 years | Evidence for consent-based processing |
| Job application records (unsuccessful) | 6 months | 1 year | Discrimination claim risk |
| Website analytics / cookies | 1 month (session) | 25 months (analytics) | EDPB Guideline recommendation |
| CCTV footage | 30 days | 90 days | Unless part of incident investigation |
| Health/medical records | Varies — see sector rules | Varies | Heavily jurisdiction-specific [VERIFY] |

[JURISDICTION-SPECIFIC] Verify retention periods against applicable sector-specific
regulations (employment law, financial services, healthcare, consumer protection) in
each applicable jurisdiction before finalizing the ROPA.

### Step 9: Technical and Organisational Measures Documentation

For each processing activity, document the general description of TOMs required by
Art. 30(1)(g) / Art. 30(2)(d):

**ROPA-appropriate TOM description** (general description — not full Art. 32 documentation):

| TOM Category | Document in ROPA |
|-------------|-----------------|
| Encryption | "Encryption at rest (AES-256) and in transit (TLS 1.3)" |
| Access control | "Role-based access control; MFA required for admin access" |
| Pseudonymization | "Customer IDs pseudonymized in analytics pipeline" |
| Backups | "Daily automated backups with 30-day retention" |
| Incident response | "Documented incident response plan; breach notification procedure in place" |
| Staff training | "Annual data protection training; DPA awareness e-learning on onboarding" |
| Physical security | "Servers in ISO 27001-certified data center" |
| Vendor certifications | "Primary cloud provider: AWS (ISO 27001, SOC 2 Type II, C5)" |
| Penetration testing | "Annual penetration test; most recent [date]" |

> **Level of detail calibration**: The ROPA requires a "general description" — not the
> full security architecture. Write enough to allow a supervisory authority to understand
> the security posture for this activity. Detailed technical specifications, penetration
> test reports, and security policies belong in Art. 32 documentation, not the ROPA.

> **Swiss FADP note**: Art. 12 FADP removes the "where possible" qualifier — TOMs are
> mandatory without qualification. Include at minimum encryption, access control, and
> incident response measures.

### Step 10: Activity Completeness Assessment

Assess each processing activity entry against the GREEN / YELLOW / RED classification
system below. Run the assessment silently before presenting results.

---

## Classification System

### Completeness Classification — Per Processing Activity

#### GREEN — Fully Compliant and Audit-Ready
**All of the following must be true:**

- [ ] Processing purpose is specific, substantiated, and not generic
- [ ] All mandatory fields for the applicable role (controller/processor) are populated
- [ ] Legal basis (Art. 6) documented for every controller-side activity
- [ ] Art. 9(2) condition documented for every special category activity
- [ ] All recipients identified by name or category (with named processors)
- [ ] DPA in place with every third-party processor; reference documented
- [ ] Third-country transfers identified with mechanism documented and current
- [ ] Retention trigger, period, deletion method, and responsibility all specified
- [ ] TOMs described at sufficient detail for ROPA (not just "see security policy")
- [ ] Profiling / ADM flag set; DPIA status documented
- [ ] LIA completion documented for every Art. 6(1)(f) activity
- [ ] Entry is version-controlled with review date

#### YELLOW — Partial Compliance — Remediation Required
**Any of the following present:**

- [ ] Legal basis stated but without adequate documentation (e.g., "consent" with no
  confirmation of consent records being maintained)
- [ ] Purpose described generically ("service improvement") without specific operational
  articulation
- [ ] Recipient identified by category but specific processor names missing or incomplete
- [ ] DPA flagged as "pending" or "under review" with a processor actively processing data
- [ ] Third-country transfer identified but transfer mechanism documentation incomplete
  (mechanism type known but SCC execution not confirmed)
- [ ] Retention period stated but deletion trigger or method missing
- [ ] TOMs described as "appropriate security measures" without substance
- [ ] Art. 6(1)(f) claimed without LIA completion status documented
- [ ] DPIA trigger identified but DPIA status unknown or not yet initiated
- [ ] Entry has not been reviewed in more than 12 months
- [ ] Special category data suspected but not confirmed; Art. 9 condition undocumented

**YELLOW Routing**: Assign remediation tasks with 30-day deadline. Escalate to DPO.
Do not block processing — proceed with 30-day remediation SLA.

#### RED — Blocking Gap — Immediate Action Required
**Any single one of the following:**

- [ ] Processing purpose missing entirely
- [ ] Legal basis missing for controller-side activity
- [ ] No legal basis possible for the processing as described (unlawful)
- [ ] Special category data processed with no Art. 9(2) condition identified
- [ ] Criminal data processed without Art. 10 authorisation
- [ ] Third-country transfer occurring with no documented legal mechanism
- [ ] Processor relationship with no DPA / processing contract in place
- [ ] Data retention period entirely missing (not just vague — completely absent)
- [ ] Automated decision-making with significant effects identified; no DPIA, no Art. 22
  safeguards
- [ ] Data source unknown (e.g., purchased from data broker without provenance)
- [ ] Consent-based processing with no retrievable consent records
- [ ] Processing activity identified but legal basis claimed is clearly inapplicable

**RED Routing**: Escalate immediately to DPO and legal counsel. Suspend the processing
activity if it cannot be remediated without redesign. Document in Glass Box. [VERIFY all
RED-level determinations with qualified legal counsel before suspending production systems.]

---

## Actionable Output per Finding

For each YELLOW or RED finding, produce a structured finding record:

```
Finding ID: ROPA-[YYYYMMDD]-[nnn]
Processing Activity: [Activity name]
Field at issue: [Field name or number from mandatory field matrix]
Classification: YELLOW / RED
Finding: [Precise description of the gap — what is missing or inadequate]
Legal basis: [Article and paragraph; Confidence: [level]]
Business impact: [Risk of supervisory authority scrutiny, fines, individual complaints]
Remediation action: [Specific action to take]
Responsible party: [Business unit / DPO / Legal counsel]
Deadline: [Date — 30 days for YELLOW; immediate for RED]
Evidence artifact: [What document or record must be produced to close this finding]
Verification: [How to confirm the finding is closed]
```

---

## Prioritization Framework

Prioritize remediation across the ROPA gap log using this three-tier framework:

**Tier 1 — Immediate (RED items, must resolve before relying on ROPA)**
- Missing legal basis for any processing activity
- Third-country transfers without documented mechanisms
- Special category or criminal data processing without Art. 9(2) / Art. 10 basis
- Processor relationships without DPAs
- Automated decision-making with significant effects and no DPIA

**Tier 2 — Near-Term (HIGH-impact YELLOW items, within 30 days)**
- Vague purposes requiring specification
- Retention periods missing triggers or deletion methods
- Pending DPAs with active processors
- LIA not completed for Art. 6(1)(f) activities
- DPIAs triggered but not initiated

**Tier 3 — Background (LOW-impact YELLOW items, within 90 days)**
- Missing best-practice fields (data owner, system reference, source)
- Entries not reviewed in 12+ months
- Sub-processor lists incomplete in detail
- Machine-readable export hooks not set up

---

## Quality Frameworks

### Citation Quality Gates

Run these five gates silently before delivering any ROPA output. If any gate fails, revise
before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal basis claim cites a specific article and paragraph | Add citation or mark "[UNVERIFIED]" |
| **Format** | Citations follow consistent, jurisdiction-aware format | Standardize format |
| **Currency** | Cited provisions checked for amendments (e.g., EDPB guidance updates, adequacy decisions) | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within the skill's applicable regime scope | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; no hidden assumptions | Add confidence qualifier |

### Self-Interrogation for RED Items

For any RED-classified activity, apply this three-pass adversarial review before
finalizing the classification:

**Pass 1 — Legal Chain Integrity**: Does the RED classification follow logically from the
cited authority? Is the gap genuinely material to compliance, or is it a documentation
gap that could be resolved without suspending the activity?

**Pass 2 — Completeness**: Have all available legal mechanisms and defences been
considered? For a transfer without a documented mechanism, is there an adequacy decision
that was simply overlooked? For a missing legal basis, is there a reasonable Art. 6
ground not yet identified?

**Pass 3 — Challenge**: What is the strongest argument against this classification? Under
what circumstances would a reasonable DPO classify this as YELLOW rather than RED? If the
counter-argument is persuasive, reconsider the classification.

### Confidence Scoring

Apply confidence scoring to every legal basis assignment and transfer mechanism determination:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law; clear statutory text | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretive questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments; reasonable interpretation | State with reasoning |
| **Possible** | 0.40–0.59 | Genuine legal uncertainty | Flag for professional review |
| **Unlikely** | 0.0–0.39 | Weak basis; speculative | Do not assert; mark "[UNCERTAIN]" |

Confidence below 0.80 on a legal basis assignment → automatically classify the activity
as YELLOW regardless of other field completeness.

---

## Glass Box Audit Trail

Include this audit trail template at the end of every ROPA output:

```yaml
glass_box:
  skill_name: "legalcode-ropa-generator"
  mode: "Created from scratch / Auditing existing ROPA / Converting data mapping output"
  topic: "Records of Processing Activities — Art. 30 GDPR"
  organization_role: "Controller / Processor / Both"
  primary_regime: "EU GDPR / UK GDPR / Swiss FADP / Brazil LGPD"
  regime_overlays: []
  sector_overlays: []
  scope: "Full organization / Single department / Single activity"
  processing_activities_documented: 0
  classification_summary:
    GREEN: 0
    YELLOW: 0
    RED: 0
  exemption_determination: "ROPA required / Exemption may apply — decision recorded"
  art_30_5_exemption_screened: true
  controller_mandatory_fields_covered: "0/24"
  processor_mandatory_fields_covered: "0/14"
  transfers_documented: 0
  transfers_with_mechanism_confirmed: 0
  special_category_activities: 0
  automated_decision_making_activities: 0
  dpia_cross_references_complete: false
  lia_cross_references_complete: false
  sub_processor_audit_complete: false
  legalcode_mcp: "Connected / Not connected — citations marked [VERIFY]"
  research_reference_file: "Not created / /tmp/legalcode-ropa-research.md"
  quality_score: "0/40"
  completeness: "0/18 elements"
  citations_verified: "0 VERIFIED / 0 [VERIFY] pending"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Outputs require verification by a qualified data protection professional"
    - "Legal basis assignments are provisional — professional review recommended"
    - "Transfer mechanism determinations require verification of current adequacy status"
  reviewer: "AI-assisted — requires qualified DPO or legal counsel review"
  review_date: "[date]"
  next_scheduled_review: "[date — typically 12 months or on material change]"
```

---

## Anti-Patterns

What NOT to do when generating or auditing a ROPA:

1. **Treating the ROPA as a one-time project** — A ROPA is a living document. It must be
   updated whenever a processing activity is added, changed, or discontinued. Organizations
   that complete a ROPA once and file it without a maintenance protocol will have a stale,
   non-compliant record within months.

2. **Generic purpose statements** — "Marketing," "service improvement," "analytics," and
   "HR management" are not purposes — they are categories. Each purpose must describe what
   specific action is taken, for which goal, using which legal basis. "Sending monthly
   product newsletters to consenting subscribers to promote new product features" is a
   purpose.

3. **Omitting processors** — Failing to document SaaS vendors, cloud providers (AWS,
   Azure, GCP), CRM tools, payroll processors, and analytics platforms is the most common
   ROPA gap identified in DPA audits. Every vendor that touches personal data on behalf of
   the controller is a processor that must appear in the ROPA.

4. **Missing international transfers** — Organizations routinely fail to recognize that
   using US-headquartered SaaS vendors constitutes a restricted transfer if data is
   processed on US servers. Verify whether each processor is DPF-certified; document the
   mechanism if not.

5. **Retention as a hyperlink** — Writing "see Retention Policy v3.2" or linking to an
   external document is insufficient. The ROPA entry must state the specific period, the
   trigger event, and the deletion method. Supervisory authorities consistently flag this.

6. **SME exemption over-reliance** — Organizations with fewer than 250 employees that
   process employee records, customer data, or website analytics cannot rely on the Art.
   30(5) exemption. The exemption is nearly illusory for operational organizations.

7. **System-based rather than activity-based structure** — Organizing by IT systems ("the
   CRM," "the HR platform") instead of by processing activities ("customer relationship
   management," "employee performance management") produces a ROPA that is readable from
   an IT perspective but unintelligible from a privacy perspective. Supervisory authorities
   audit by activity.

8. **Controller-processor role confusion** — Processing purposes and legal basis belong
   in the controller ROPA. They do not belong in the processor ROPA. Processors document
   what they do — not why. Adding purpose and legal basis to a processor ROPA blurs role
   boundaries and creates compliance confusion.

9. **Group company consolidation** — Each separate legal entity that acts as a controller
   must maintain its own ROPA. A parent company cannot maintain a consolidated ROPA that
   covers all subsidiaries as a single legal entity. Joint controller arrangements require
   explicit documentation of which controller takes responsibility for which obligation.

10. **DPO as sole ROPA owner** — The DPO has an advisory, not an operational, role in
    ROPA maintenance. Responsibility for each ROPA entry rests with the business unit that
    owns the processing activity. A DPO-maintained ROPA that no business unit has reviewed
    will have gaps and inaccuracies. Supervisory authorities look for evidence of
    organizational accountability — not just DPO outputs.

11. **Missing Art. 9 conditions** — Processing special category data without documenting
    the Art. 9(2) condition is a RED finding. The ROPA must identify the specific ground —
    explicit consent, employment and social security law, vital interests, nonprofit
    processing, manifestly public data, legal claims, substantial public interest, medical
    purposes, public health, or archiving/research/statistical — and cross-reference any
    required policy document.

12. **No version control** — Being unable to demonstrate what the ROPA said at a specific
    point in time (e.g., at the time of a data breach) is an audit problem. ROPA entries
    should carry version numbers and review dates. Maintain a version history or use a
    change-tracked format.

13. **Ignoring processor's Art. 30(2) obligation** — Organizations that act as processors
    for their clients frequently fail to maintain a processor-side ROPA entirely. Every
    SaaS provider, payroll processor, and managed service provider has an independent Art.
    30(2) obligation regardless of whether their clients maintain a ROPA.

14. **Missing LIA for Art. 6(1)(f) activities** — Claiming legitimate interests as a legal
    basis without a completed Legitimate Interest Assessment introduces a YELLOW finding.
    The ROPA entry should reference the LIA document ID and completion status. An
    outstanding LIA is not a valid basis for continued processing at Probable confidence.

15. **DPIA triggers not identified** — Failing to screen ROPA entries against Art. 35
    DPIA triggers. Every ROPA entry should carry a DPIA status field. High-risk processing
    without a completed DPIA is a RED finding where DPIA is legally required.

16. **Transfer mechanism not current** — Adequacy decisions and SCC versions change.
    The EU-US Privacy Shield was invalidated in Schrems II (2020). The UK adequacy
    decision for EEA transfers was valid until June 2025 — confirm renewal. Legacy EU SCCs
    (pre-June 2021) should have been replaced by EU SCCs 2021. UK legacy contracts should
    have migrated to IDTA or SCCs + UK Addendum by March 21, 2024. Always verify
    mechanism currency. [VERIFY — current adequacy decisions and SCC transition deadlines]

17. **Sub-processor lists incomplete** — Processor-side RoPAs must document sub-processors
    (the vendor's vendors). Controllers' RoPAs should reference the DPA's sub-processor
    authorization mechanism. Failing to identify sub-processors creates compliance gaps in
    both controller and processor obligations.

18. **Security described as "appropriate"** — Writing "appropriate technical and
    organisational measures" in the TOM field is the equivalent of writing nothing. Name
    the measures. State whether encryption is in place and at what strength. Identify the
    access control model. Reference relevant certifications. One sentence of substance is
    better than a platitude.

19. **Missing automated decision-making flags** — Art. 22 automated decision-making with
    legal or similarly significant effects requires safeguards (human review, explanation
    on request, right to contest). Not flagging ADM in the ROPA prevents DPIA assessment
    and safeguard implementation. Every ROPA entry must include a profiling/ADM field.

20. **Data source undocumented** — For data received from third parties (purchased lists,
    broker data, referral partners), the source must be documented to meet Art. 14
    transparency obligations. A ROPA that cannot answer "where did this data come from?"
    creates downstream DSAR and transparency failures.

---

## Writing Standards

Apply these standards to all ROPA output and finding descriptions:

1. **Activity names**: Use noun phrases that would be intelligible to a supervisory
   auditor who has no knowledge of the organization's internal terminology (e.g.,
   "Customer invoice processing" not "BillingOps ERP flow").

2. **Purposes**: Complete sentences using the format "Processing [data type] to [specific
   operational goal] for [category of data subjects]."

3. **Legal basis**: State the Art. 6 paragraph and sub-paragraph in full, then explain
   in plain language why it applies to this specific activity.

4. **Retention periods**: State as "X [days/months/years] from [specific trigger event]."
   Never state "as required" or "indefinitely."

5. **TOMs**: Minimum one sentence per measure category present. Do not use bullet lists
   of single words ("encryption, access controls, training") without substance.

6. **Finding descriptions**: Describe what is missing, why it matters, and what the
   remediation looks like — not just that a field is empty.

7. **Confidence qualifiers**: Use in-line qualifiers — "Confidence: High" — for every
   legal basis and transfer mechanism assignment. Do not state legal positions as settled
   fact when Confidence is below 0.80.

8. **Plain language discipline**: Avoid unexplained acronyms. Spell out DPO, DPA, SCC,
   TOM, LIA, DPIA, ADM on first use.

---

## External Tool Integration

### legalcode-mcp (Preferred for Legal Authority Verification)

Use **legalcode-mcp** to verify:
- Current adequacy decisions per destination country (adequacy decisions change)
- Current version of EU SCCs and any implementing guidance
- Specific EDPB opinions and guidelines on RoPA format and completeness
- National DPA guidance on ROPA expectations (DPC Ireland, ICO, CNIL, AEPD, BfDI)
- Art. 30(5) current interpretation and any pending legislative changes
- Swiss FDPIC guidance on Art. 12 FADP processing register
- ANPD guidance on LGPD Art. 37 records

Save results to `/tmp/legalcode-ropa-research.md` and mark citations as VERIFIED.

**Without legalcode-mcp:**
- Mark all adequacy decisions, SCC references, and DPA guidance citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural completeness, mandatory field coverage, and classification accuracy

---

## Downstream Integration

The ROPA generator is positioned between data mapping (upstream discovery) and the
specialized compliance workflows (downstream action):

```
legalcode-data-mapping-workflow
    → legalcode-ropa-generator    (this skill)
        → legalcode-dpia-generator          (for Art. 35 DPIA triggers)
        → legalcode-legitimate-interest-assessment  (for Art. 6(1)(f) activities)
        → legalcode-cross-border-transfer-assessment  (for RED transfer gaps)
        → legalcode-dsar-workflow-builder    (system inventory feeds DSAR process)
        → legalcode-dpa-review-and-negotiation  (for missing or inadequate DPAs)
```

**DPIA handoff trigger**: Any ROPA entry flagged with any of these characteristics should
be passed to `legalcode-dpia-generator`:
- Large-scale processing of special category data
- Systematic monitoring of publicly accessible areas
- Automated decision-making with legal / significant effects
- New technology processing with high risk to data subject rights
- Two or more EDPB WP248 nine-criteria triggers met

**LIA handoff trigger**: Any ROPA entry claiming Art. 6(1)(f) without a completed LIA
should be passed to `legalcode-legitimate-interest-assessment`.

**Transfer assessment handoff**: Any RED transfer gap should be passed to
`legalcode-cross-border-transfer-assessment` for a full TIA and mechanism selection.

---

### Step 11: LIA and DPIA Cross-Reference

For each processing activity, assess and document:

**LIA Cross-Reference** (controller-side only):

| Activity | Legal Basis Claimed | LIA Required? | LIA Status | LIA Doc ID | Owner | Deadline |
|----------|--------------------|--------------| -----------|------------|-------|---------|
| [Activity] | Art. 6(1)(f) LI | Yes | Completed / Pending / Not initiated | [ID or N/A] | [Name] | [Date] |

**DPIA Cross-Reference**:

Assess each activity against the EDPB WP248 nine-criteria list. If two or more criteria
are met, a DPIA is likely required. If any Art. 35(3) automatic trigger applies, a DPIA
is required without qualification:

Art. 35(3) automatic triggers:
- Systematic and extensive profiling with legal or similarly significant effects
- Large-scale processing of Art. 9 special category or Art. 10 criminal data
- Systematic monitoring of publicly accessible areas on a large scale

EDPB WP248 nine criteria (≥2 = DPIA likely required):
1. Evaluation or scoring
2. Automated decision-making with legal/significant effects
3. Systematic monitoring
4. Sensitive data or highly personal data
5. Large-scale processing
6. Matching or combining datasets
7. Vulnerable data subjects
8. Innovative use or application of technology
9. Data transfers across borders with risk

| Activity | Art. 35(3) Trigger? | WP248 Criteria Count | DPIA Required? | DPIA Status | DPIA Doc ID |
|----------|--------------------|--------------------|----------------|------------|------------|
| [Activity] | Yes / No | [n]/9 | Yes / No / Recommended | Completed / Pending / Not initiated | [ID or N/A] |

### Step 12: Output Assembly and Maintenance Framework

Assemble the final ROPA package and establish the maintenance protocol.

**⟁ CLARIFY** — Confirm which output format(s) the user needs:
- **Full ROPA package** (all parts A–J below)
- **Controller ROPA register only** (Part B)
- **Gap log and remediation plan only** (Parts F and G)
- **Machine-readable export** (Part J — JSON/YAML for ROPA management tools)
- **Supervisory authority submission format** (Parts A + B + C — regulator-ready)

**Maintenance Protocol**: Present the user with a maintenance trigger checklist:

**Events requiring immediate ROPA update** (update within 5 business days):
- [ ] New third-party vendor / processor onboarded
- [ ] Existing processor relationship terminated
- [ ] New processing purpose implemented (new product feature, new marketing channel)
- [ ] New category of personal data collected
- [ ] New third-country transfer route established
- [ ] Data Processing Agreement signed or amended
- [ ] Sub-processor added or removed by a processor
- [ ] Consent mechanism changed
- [ ] Retention policy changed
- [ ] Data breach that reveals an undocumented processing activity
- [ ] Automated decision-making first introduced
- [ ] Corporate restructure, acquisition, or divestiture affecting data flows

**Annual ROPA review** (scheduled, regardless of events):
- Full review of all entries for accuracy and completeness
- Update review dates on each entry
- Re-assess transfer mechanism currency (adequacy decisions, SCC version)
- Update processor/sub-processor lists from current vendor inventory
- Re-run Art. 30(5) exemption screen if organization size changed
- Update Glass Box audit trail and Glass Box confidence assessment

---

## Output Format Template

### Part A — Executive Summary

```markdown
# Records of Processing Activities — [Organization Name]
**Generated by**: legalcode-ropa-generator
**Date**: [YYYY-MM-DD]
**Version**: [n.n]
**Regime(s)**: [EU GDPR / UK GDPR / Swiss FADP / Brazil LGPD]
**Role**: [Controller / Processor / Both]
**Scope**: [Full organization / Department: X]
**DPO**: [Name, contact]

## Overview
- **Total processing activities documented**: [n]
- **GREEN (audit-ready)**: [n] ([%])
- **YELLOW (remediation required)**: [n] ([%])
- **RED (blocking gaps)**: [n] ([%])

## Immediate Actions Required
[List of RED items requiring immediate attention]

## Key Metrics
- Mandatory fields complete (all activities): [%]
- Activities with documented legal basis: [n/n]
- Activities with documented retention: [n/n]
- Activities with completed LIA (Art. 6(1)(f)): [n/n]
- Activities with DPIA status documented: [n/n]
- Third-country transfers with documented mechanism: [n/n]
- Processors with confirmed DPA: [n/n]
```

### Part B — Processing Activity Register

**Controller ROPA Format:**

| Activity ID | Activity Name | Purpose | Legal Basis | Data Subjects | Personal Data | Recipients | Transfers | Retention | TOMs | ADM | DPIA | LIA | Classification |
|------------|--------------|---------|------------|---------------|---------------|-----------|----------|-----------|------|-----|------|-----|---------------|
| ACT-001 | [Name] | [Purpose] | Art. 6(1)([x]) | [Types] | [Categories] | [Named] | [Countries + mechanism] | [Period + trigger] | [Summary] | [Yes/No] | [Status] | [Status] | 🟢/🟡/🔴 |

**Processor ROPA Format:**

| Activity ID | Controller Name | Controller Contact | Categories of Processing | Sub-Processors | Transfers | TOMs | Classification |
|------------|-----------------|-------------------|--------------------------|---------------|----------|------|---------------|
| PRO-001 | [Controller] | [Contact] | [Processing types] | [Named] | [Countries + mechanism] | [Summary] | 🟢/🟡/🔴 |

### Part C — Mandatory Field Coverage Matrix

| Activity | C1 | C2 | C6 | C7 | C8 | C9 | C12 | C13 | C14 | C15 | C16 | C17 | C18 | Status |
|---------|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|--------|
| ACT-001 | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟢 |

*(C-codes correspond to field numbers in the Controller ROPA Entry table in Step 6)*

### Part D — Transfer Ledger

| Activity | Destination Country | Recipient | Role | Mechanism | Module | TRA Status | Mechanism Reference | Status |
|---------|--------------------|---------|----|---------|------|-----------|-------------------|--------|
| ACT-001 | United States | [Vendor] | Processor | EU SCCs 2021 | M2 | Completed | DPA Annex B, dated [date] | ✅ |

### Part E — Retention Schedule

| Activity | Data Category | Retention Trigger | Period | Deletion Method | Statutory Basis | Exception |
|---------|--------------|------------------|--------|-----------------|-----------------|-----------|
| ACT-001 | Customer invoices | End of tax year | 7 years | Secure deletion | VAT Act § [x] | None |

### Part F — Sub-Processor Inventory (Processor ROPA)

| Controller | Sub-Processor | Function | Location | Authorization Type | Notification Date | Status |
|-----------|-------------|--------|--------|------------------|-----------------|--------|
| [Controller] | [Sub-processor] | [Function] | [Country] | Specific / General | [Date] | Active |

### Part G — Gap Log (YELLOW Items)

| Finding ID | Activity | Field | Gap Description | Remediation Action | Owner | Deadline | Status |
|-----------|---------|-------|-----------------|-------------------|-------|---------|--------|
| ROPA-[date]-001 | ACT-001 | C8 — Legal Basis | LIA not completed for Art. 6(1)(f) claim | Complete LIA using legalcode-legitimate-interest-assessment | DPO | [30 days] | Open |

### Part H — Escalation Log (RED Items)

| Finding ID | Activity | Field | Blocking Gap | Immediate Action | DPO Notified | Legal Counsel Needed |
|-----------|---------|-------|-------------|----------------|-------------|---------------------|
| ROPA-[date]-001 | ACT-003 | C16 — Transfer | US vendor transfer: no documented mechanism | Suspend transfer or execute DPF verification / SCCs | Yes | Yes |

### Part I — Completeness Scorecard

```markdown
## ROPA Completeness Scorecard
**Assessment date**: [date]

| Metric | Count | % Complete |
|--------|-------|-----------|
| Total activities | [n] | — |
| GREEN (fully compliant) | [n] | [%] |
| YELLOW (remediation needed) | [n] | [%] |
| RED (blocking gaps) | [n] | [%] |
| Activities with legal basis documented | [n/n] | [%] |
| Activities with retention documented | [n/n] | [%] |
| Activities with transfer mechanism documented | [n/n] | [%] |
| Processors with DPA confirmed | [n/n] | [%] |
| DPIA status documented | [n/n] | [%] |
| LIA documented for Art. 6(1)(f) activities | [n/n] | [%] |
| Mandatory fields complete | [n/24 per activity avg] | [%] |

**Overall ROPA readiness**: 🔴 NOT READY / 🟡 REQUIRES REMEDIATION / 🟢 AUDIT-READY
```

### Part J — Machine-Readable Export Hooks

Provide YAML/JSON export compatible with common ROPA management tools:

```yaml
# legalcode-ropa-generator export
# Compatible with: OneTrust, TrustArc, Privaci, ROPA Manager, DataGrail
export_version: "1.0"
export_date: "[YYYY-MM-DD]"
organization: "[Name]"
role: "controller|processor|both"
regime: ["eu_gdpr", "uk_gdpr", "swiss_fadp", "brazil_lgpd"]
activities:
  - id: "ACT-001"
    name: "[Activity name]"
    purpose: "[Purpose]"
    legal_basis:
      article: "6(1)(f)"
      description: "Legitimate interests"
      lia_status: "completed|pending|not_initiated"
      lia_reference: "[doc_id]"
      confidence: 0.85
    data_subjects: ["customers", "prospects"]
    personal_data: ["name", "email", "purchase_history"]
    recipients:
      - name: "[Recipient]"
        role: "processor|controller"
        location: "DE"
        dpa_reference: "[doc_id]"
    transfers:
      - destination: "US"
        recipient: "[Vendor]"
        mechanism: "eu_sccs_2021_m2"
        tra_completed: true
        reference: "[doc_id]"
    retention:
      trigger: "end_of_contract"
      period: "6 years"
      deletion_method: "secure_deletion"
      statutory_basis: "[cite law]"
    toms:
      encryption: "AES-256 at rest, TLS 1.3 in transit"
      access_control: "RBAC, MFA"
      certifications: ["ISO 27001", "SOC 2 Type II"]
    adm_flag: false
    dpia_status: "not_required"
    classification: "GREEN"
```

---

## Localization Notes

### EU GDPR (Reference standard)
- Legal basis field: Art. 6(1)(a)–(f); Art. 9(2)(a)–(j) for special categories
- Transfer mechanisms: EU SCCs 2021 (Modules 1–4), BCRs, adequacy decisions, Art. 49 derogations
- EDPB guidelines are binding interpretive authority
- Fines for Art. 30 violations: Art. 83(4)(a) — up to EUR 10M or 2% of global turnover

### UK GDPR
- Additional field: DPA 2018 Schedule 1 condition for Art. 9 processing
- Additional field: Appropriate Policy Document (APD) reference for several Schedule 1 conditions
- Transfer mechanisms: UK IDTA, EU SCCs + UK Addendum (transition deadline: 21 March 2024 for legacy contracts)
- Adequacy: UK-EU transfers — UK adequacy decision (confirm renewal status post-June 2025) [VERIFY]
- ICO guidance supersedes EDPB for UK GDPR interpretation
- ICO audit framework includes ROPA completeness as a scored element

### Swiss FADP (Art. 12)
- Effective: 1 September 2023
- No "where possible" qualifier — TOMs are mandatory without qualification
- Exemption: 250 employees + negligible risk (narrower framing than GDPR three conditions)
- Federal bodies: Must report register to FDPIC via DataReg system
- Transfer mechanisms: FDPIC-recognized standard data protection clauses; separate from EU SCCs
- Adequacy list: Switzerland's own list — separate from EU; US does not appear [VERIFY current]
- Language: German (Bearbeitungsverzeichnis), French (registre des activités de traitement), Italian (registro delle attività di trattamento)

### Brazil LGPD (Art. 37)
- Statutory text: One sentence; no mandatory fields in statute
- ANPD template: 13 fields — non-binding but represents regulatory expectation
- Both controllers (controladores) and operators (operadores) must maintain records
- Special emphasis: Art. 37 explicitly calls out legitimate interest processing
- DPIA equivalent: RIPD (Relatório de Impacto à Proteção de Dados) required for legitimate interest processing
- SME threshold: Based on revenue and risk level (small processing agents), not headcount
- Fines: ANPD can impose fines up to 2% of revenue in Brazil (capped at BRL 50M per infraction)
- ANPD has 13-element template [VERIFY — current ANPD guidance on mandatory vs. recommended fields]

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis based on deep research into GDPR
Article 30 primary text and Recital 82, EDPB WP29 Position Paper on Art. 30(5) derogations
(19 April 2018), ICO ROPA guidance and accountability framework, DPC Ireland Records of
Processing Activities guidance (2023), Swiss FADP Article 12 and FDPIC implementing
guidance, Brazil LGPD Article 37 and ANPD Resolution CD/ANPD No. 2/2022 template,
structural patterns from `legalcode-data-mapping-workflow`, `legalcode-dpia-generator`,
and `legalcode-data-processing-agreement-drafter`, and the `legalcode-contract-review`
quality framework standard. References to the 2025 EU Omnibus IV proposal (750-employee
threshold) are included as informational — the proposal is not yet law.
