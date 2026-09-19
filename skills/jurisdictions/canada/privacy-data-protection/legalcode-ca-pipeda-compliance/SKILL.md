---
name: legalcode-ca-pipeda-compliance
description: Comprehensive PIPEDA compliance assessment for Canadian private-sector organizations. Use
  when conducting a PIPEDA compliance audit, preparing for an OPC investigation or complaint, building
  a privacy management program, onboarding a new line of business or product involving personal information,
  or assessing compliance exposure before a merger, acquisition, or regulatory engagement in Canada.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Comprehensive PIPEDA compliance assessment for Canadian private-sector organizations. Evaluates organizational practices against all 10 Fair Information Principles (PIPEDA Schedule 1 Clauses 4.1–4.10), the OPC 2019 Meaningful Consent Guidelines, cross-border transfer accountability obligations, individual access and correction rights, and the breach of security safeguards framework (ss.10.1–10.3, SOR/2018-64). Generates a structured compliance gap report with COMPLIANT/PARTIAL/NON-COMPLIANT findings, CRITICAL/ HIGH/MEDIUM/LOW risk prioritization, and actionable remediation steps. Covers provincial interaction with BC PIPA (SBC 2003, c.63), Alberta PIPA (SA 2003, c.P-6.5), and Quebec Law 25, and includes a CPPA readiness gap analysis against the proposed Consumer Privacy Protection Act (Bill C-27). Use when conducting a PIPEDA compliance audit, preparing for an OPC investigation or complaint, building a privacy management program, onboarding a new line of business or product involving personal information, or assessing compliance exposure before a merger, acquisition, or regulatory engagement in Canada.


# Canada PIPEDA Comprehensive Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted PIPEDA compliance
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in Canada before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and regulatory
> references cited from memory carry hallucination risk — verify against authoritative
> sources (Justice Laws Website consolidations, OPC publications, Canada Gazette) before
> relying on them. PIPEDA compliance determinations carry enforcement and reputational
> consequences; professional legal guidance is essential.

---

## Purpose and Scope

This skill conducts a comprehensive PIPEDA compliance assessment for private-sector
organizations subject to Canada's federal privacy law. It operationalizes the Personal
Information Protection and Electronic Documents Act (SC 2000, c. 5) into a structured
audit workflow with decision points, quality assurance frameworks, and an auditable gap
report.

**Covers:**

- Organizational accountability framework assessment (Principle 1 / Clause 4.1)
- Purpose identification and specification (Principle 2 / Clause 4.2)
- Consent framework — express, implied, and meaningful consent (Principle 3 / Clause 4.3)
- Data minimization and collection limitation (Principle 4 / Clause 4.4)
- Use, disclosure, and retention controls (Principle 5 / Clause 4.5)
- Accuracy practices (Principle 6 / Clause 4.6)
- Security safeguards assessment (Principle 7 / Clause 4.7)
- Openness and transparency obligations (Principle 8 / Clause 4.8)
- Individual access and correction rights (Principle 9 / Clause 4.9)
- Complaint handling and challenging compliance (Principle 10 / Clause 4.10)
- Cross-border transfer accountability obligations
- Breach notification framework (ss.10.1–10.3, SOR/2018-64) summary
- Provincial compliance overlay (BC PIPA, Alberta PIPA, Quebec Law 25)
- CPPA readiness assessment (proposed Bill C-27 gap analysis)
- OPC investigation preparedness

**Does not:**

- Replace the `pipeda-breach-reporting-and-notification-operations` skill — use that skill
  for live breach response, RROSH assessment, OPC report preparation, and individual
  notification drafting
- Replace provincial assessments — use `bc-pipa-privacy-breach-response-and-voluntary-
notification-operations`, `alberta-pipa-privacy-breach-notification-operations`, or
  `quebec-law-25-confidentiality-incident-response-operations` for provincial breach
  response operations
- Assess federal public-sector privacy obligations under the Privacy Act (RSC 1985, c. P-21)
- Address sector-specific federal frameworks (OSFI FRFI data governance, CRTC customer
  data, health sector) beyond flagging their existence
- Constitute legal advice or replace consultation with Canadian privacy counsel

---

## Jurisdiction and Governing Law

This skill is jurisdiction-specific to **Canada (Federal)** with provincial overlay analysis.

**Primary legislation:**

- Personal Information Protection and Electronic Documents Act (PIPEDA), SC 2000, c. 5,
  as amended
- Breach of Security Safeguards Regulations, SOR/2018-64

**Primary regulator:**

- Office of the Privacy Commissioner of Canada (OPC) — powers include investigations,
  audits, public interest audits (s.18 PIPEDA), and Federal Court referrals; no direct
  fine-imposition authority under current PIPEDA

**Territorial scope — PIPEDA applies to:**

- All private-sector organizations collecting, using, or disclosing personal information
  in the course of commercial activities with a real and substantial connection to Canada
- Organizations in all provinces without "substantially similar" legislation: Ontario,
  Manitoba, Saskatchewan, Nova Scotia, New Brunswick, Prince Edward Island, Newfoundland
  and Labrador, all three territories
- Cross-border and inter-provincial transfers, regardless of province of origin
- Federal works, undertakings, and businesses (FWUBs): banks, telecommunications
  companies, airlines, railways, interprovincial trucking, cable broadcasters, Indian
  Bands, federal Crown corporations — including their employees' personal information

**Substantially similar provincial regimes (partial PIPEDA displacement):**

| Province         | Law                                                                                                         | Displaces PIPEDA for                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| British Columbia | Personal Information Protection Act (BC PIPA), SBC 2003, c.63                                               | Intra-provincial commercial activities |
| Alberta          | Personal Information Protection Act (AB PIPA), SA 2003, c.P-6.5                                             | Intra-provincial commercial activities |
| Quebec           | Act respecting the protection of personal information in the private sector (as amended by Law 25 / Law 64) | Intra-provincial commercial activities |

**PIPEDA still applies to BC, AB, and QC organizations for:**

- Cross-border and inter-provincial data transfers
- FWUBs operating in those provinces
- Employee personal information of FWUBs

**Legislative reform awareness (as of 2026-03-21):**

- [VERIFY] Bill C-27 (Digital Charter Implementation Act, 2022) died on the order paper
  when Parliament prorogued in January 2025. The Consumer Privacy Protection Act (CPPA)
  it contained never received Royal Assent. Canada continues to operate under PIPEDA.
- Organizations should nonetheless conduct CPPA readiness assessments given likelihood
  of future reform (see CPPA Readiness section below).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The answer would change the scope or depth of the assessment
- Multiple compliance frameworks may be applicable and the organization's situation is
  unclear
- Risk classification depends on business context the user must supply
- The applicable provincial regime requires determination

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

Accept organizational context in any of these formats:

- **Documentation**: Privacy policy, consent forms, data inventory/RoPA, internal
  privacy procedures, privacy management program documentation
- **Description**: Organization description, business activities, data types processed,
  provinces/countries of operation
- **Questionnaire responses**: Answers to the context-gathering questions in Step 2
- **Prior audit**: Results of a previous privacy audit or OPC investigation

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Before beginning the assessment, gather these critical inputs:

1. **Organization type and FWUB status:**
   - Options: Federally regulated business (FWUB — bank, telecom, airline, broadcaster,
     railway), Provincially regulated private-sector organization, Both (multi-business
     enterprise), Unclear
   - _Why this matters_: Determines which regime(s) apply to employee information and
     which provincial laws can displace PIPEDA.

2. **Operating provinces:**
   - Options: Ontario only, British Columbia, Alberta, Quebec, Multiple provinces (list),
     All of Canada, Canada plus international
   - _Why this matters_: BC, AB, and QC organizations are subject to substantially similar
     provincial laws for intra-provincial activities; PIPEDA still governs inter-provincial
     and cross-border transfers.

3. **Assessment scope:**
   - Options: Full PIPEDA compliance audit (all 10 principles), Targeted assessment
     (specific principles — user to identify), Pre-OPC-investigation readiness review,
     New product/service privacy review, M&A due diligence privacy assessment
   - _Why this matters_: Determines depth and focus of the assessment.

4. **Available documentation:**
   - Options: Privacy policy available, Internal privacy procedures available, Data
     inventory/RoPA available, Consent forms available, No documentation available
   - _Why this matters_: Determines whether the assessment is documentation-based or
     relies on organizational representations.

5. **Industry/sector:**
   - Options: Financial services, Healthcare/life sciences, Technology/SaaS, Retail/
     e-commerce, Human resources/employment, Professional services, Non-profit,
     Government contractor, Other
   - _Why this matters_: Certain industries have additional sector-specific obligations
     (OSFI B-10 for federally regulated financial institutions, health sector provincial
     laws) that the assessment should flag.

6. **Sensitive data categories processed:**
   - Options: Health information, Financial/credit information, Government-issued
     identifiers (SIN, passport), Biometric data, Children's information, Sexual
     orientation or gender identity, Criminal records, Racial/ethnic origin, Religious
     beliefs, Geolocation data, None of the above / unclear
   - _Why this matters_: Sensitive information requires express consent and heightened
     safeguards. The assessment calibrates consent and security requirements accordingly.

### Step 3: Load Organizational Documentation

If documentation is provided, read and extract key information:

1. **Privacy policy** — Check: What purposes are stated? What consent mechanisms are
   described? What individual rights are mentioned? How current is it?
2. **Consent forms/mechanisms** — Check: What information is collected? Is consent
   express or implied? Is it meaningful (plain language, specific)?
3. **Data inventory/RoPA** — Check: What personal information is collected? For what
   purposes? Retention periods? Third-party disclosures? Cross-border transfers?
4. **Internal procedures** — Check: Privacy officer designation? Complaint handling?
   Breach response? Training records?

If no documentation is provided, note this as a gap requiring immediate remediation
(PIPEDA Principle 8 requires policies and practices to be readily available; Principle 1
requires implementation of policies and practices).

### Step 4: Gather Legal Authority via legalcode-mcp

Use **legalcode-mcp** to build a working legal reference for this assessment.

**Search for:**

- PIPEDA Schedule 1 (10 Fair Information Principles) current consolidated text
- OPC published guidance: Meaningful Consent Guidelines (2019), Guidelines for Online
  Consent, Cross-Border Transfer Guidance (2009/updated), Privacy Breach Guidelines
- Recent OPC PIPEDA findings (2022–2025) relevant to the organization's industry
- Applicable provincial law (BC PIPA / AB PIPA / Quebec Law 25) if the assessment scope
  includes provincial overlay
- Sector-specific guidance (OSFI B-10, CRTC customer personal information rules) if
  applicable

Save results to `/tmp/legalcode-pipeda-authority.md`.

**If legalcode-mcp is not connected:**
Mark all statutory and OPC guidance references with [VERIFY]. Note in the Glass Box
audit trail: `legalcode_mcp: "Not connected — all citations require independent verification"`.

### Step 5: Assess Against the 10 Fair Information Principles

Apply the structured assessment framework in **Principle-by-Principle Assessment**
below. For each principle:

1. Identify the specific requirements under PIPEDA Schedule 1
2. Review available documentation for compliance evidence
3. Classify the finding (COMPLIANT / PARTIAL / NON-COMPLIANT / GAP)
4. Assign severity (CRITICAL / HIGH / MEDIUM / LOW)
5. Document specific gaps and remediation steps

**⟁ CLARIFY** — For each principle where documentation is absent and organizational
representations must substitute, ask specifically rather than assuming:

- "I don't have a privacy policy to review. Can you describe how you communicate your
  privacy practices to individuals?"
- "I have no data inventory. Can you describe what categories of personal information
  you collect and for what purposes?"

### Step 6: Cross-Border Transfer Assessment

Apply the cross-border transfer accountability analysis in the **Cross-Border Transfer
Framework** section below. Determine:

- Whether personal information is transferred outside Canada
- Whether appropriate contractual or other protections are in place
- Whether the organization's privacy policy discloses cross-border transfers
- Whether transfers to specific jurisdictions create heightened risk

### Step 7: Provincial Compliance Overlay

**⟁ CLARIFY** — If the organization operates in BC, AB, or QC:

- Ask whether the assessment should include a provincial compliance overlay
- Note that provincial substantially similar laws generally require separate provincial
  compliance programs for intra-provincial activities

Apply the **Provincial Overlay Analysis** in the relevant section below for each
applicable province.

### Step 8: CPPA Readiness Assessment

Apply the **CPPA Readiness Gap Analysis** section below to identify gaps between current
PIPEDA compliance and what would be required under the proposed Consumer Privacy
Protection Act (Bill C-27). This forward-looking analysis helps organizations prepare
for future legislative reform.

### Step 9: Generate Findings and Remediation Plan

Produce a structured report using the **Output Format Template** section below. The
report must include:

- Executive summary with overall compliance posture
- Principle-by-principle findings with COMPLIANT/PARTIAL/NON-COMPLIANT classification
- Severity-prioritized remediation roadmap (CRITICAL first)
- Provincial overlay findings (if applicable)
- CPPA readiness gaps
- Glass Box audit trail

### Step 10: Quality Verification

Before delivering the assessment, run the quality checks in the **Quality Assurance
Framework** section:

1. Citation Quality Gates — revise any failures before delivery
2. Self-Interrogation for NON-COMPLIANT and CRITICAL items
3. Confidence Scoring for each material finding
4. Completeness check — confirm all 10 principles addressed
5. Generate Glass Box Audit Trail

---

## Principle-by-Principle Assessment Framework

### Principle 1 — Accountability (Clause 4.1)

**Statutory requirement**: An organization is responsible for personal information under
its control. This includes information transferred to third parties for processing. The
organization must designate one or more individuals accountable for compliance (the
"privacy officer"), implement policies and practices to give effect to PIPEDA, establish
procedures for receiving and responding to complaints, train staff, and develop policies
for handling third-party processing arrangements.

**Assessment checklist:**

| Requirement                  | Assessment Question                                                                                                                               | Status |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Privacy officer designated   | Is there a named individual responsible for privacy compliance? Is their contact information available to the public?                             |        |
| Policies and practices       | Are there documented privacy policies implementing the 10 principles? Are they implemented in practice, not just on paper?                        |        |
| Third-party accountability   | Does the organization have contracts with processors/service providers ensuring comparable PIPEDA protection? Does it audit or verify compliance? |        |
| Staff training               | Are employees trained on PIPEDA obligations? Is training documented? Is it refreshed periodically?                                                |        |
| Complaint handling procedure | Is there a documented complaint handling process? Is it accessible to individuals? Does it meet the requirements of Principle 10?                 |        |

**Common gaps:**

- Privacy officer designation exists on paper but no one actually performs the role
- Third-party processors engaged without data processing agreements or PIPEDA-comparable
  clauses
- Training is informal or undocumented
- Policies exist but are outdated (e.g., pre-OPC 2019 Meaningful Consent Guidelines)

**Severity calibration:**

- No privacy officer designated: HIGH
- No third-party processing agreements: HIGH
- No documented policies: HIGH
- Outdated policies that are otherwise substantively sound: MEDIUM

---

### Principle 2 — Identifying Purposes (Clause 4.2)

**Statutory requirement**: Identify the purposes for which personal information is
collected at or before the time of collection. Purposes must be stated in such a way
that an individual can reasonably understand how the information will be used.

**Assessment checklist:**

| Requirement           | Assessment Question                                                                                                                                                       | Status |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Purposes identified   | Are all purposes for which personal information is collected documented internally?                                                                                       |        |
| Purposes communicated | Are purposes communicated to individuals at or before collection?                                                                                                         |        |
| Specificity           | Are purposes specific enough that individuals can understand the use (e.g., "for marketing" is too vague; "to send promotional emails about our products" is acceptable)? |        |
| New purposes          | Is a process in place to identify and obtain consent for new purposes before using personal information for them?                                                         |        |
| Purpose documentation | Are purposes documented and linked to the personal information categories they cover?                                                                                     |        |

**Common gaps:**

- Omnibus or vague purpose statements ("to improve our services") that do not meet
  the OPC specificity standard
- Purposes stated in privacy policy but not communicated at point of collection
- No process for identifying and handling new purposes that arise after collection
- Marketing and analytics purposes bundled together without separate disclosure

**Severity calibration:**

- No purpose identification at collection: HIGH
- Vague purposes that fail OPC specificity standard: MEDIUM
- No new-purpose review process: MEDIUM

---

### Principle 3 — Consent (Clause 4.3)

**Statutory requirement**: Knowledge and consent of the individual are required for the
collection, use, or disclosure of personal information, except where inappropriate
(law enforcement, legal proceedings, emergency, etc.). The form of consent must be
appropriate to the sensitivity of the information and reasonable expectations of the
individual. Express consent is required for sensitive information.

**OPC 2019 Meaningful Consent Guidelines — 7 elements:**

| Element                      | Requirement                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1. Emphasize key elements    | Highlight what individuals would find most important, not bury in fine print                                                      |
| 2. Individual control        | Allow individuals to control levels and types of consent                                                                          |
| 3. Plain language            | Clear, understandable language — no legalese                                                                                      |
| 4. Layered approach          | For complex processing, use tiered disclosure                                                                                     |
| 5. Right timing              | Obtain consent when the individual has full context (not retroactively)                                                           |
| 6. Express for sensitive     | Direct, explicit consent for health, financial, government ID, biometric, sexual orientation, religious, and other sensitive data |
| 7. Implied for non-sensitive | Implied consent acceptable only for non-sensitive information within reasonable expectations                                      |

**Assessment checklist:**

| Requirement           | Assessment Question                                                                                            | Status |
| --------------------- | -------------------------------------------------------------------------------------------------------------- | ------ |
| Consent mechanism     | Is there a clear consent mechanism for each purpose?                                                           |        |
| Express vs. implied   | Is express consent obtained for sensitive categories? Is implied consent used appropriately for non-sensitive? |        |
| Meaningful consent    | Does the consent mechanism meet all 7 OPC 2019 elements?                                                       |        |
| Consent withdrawal    | Can individuals withdraw consent? Is the process clearly communicated and easy to use?                         |        |
| Bundled consent       | Is consent bundled (requiring consent to all uses or none) where it should be unbundled?                       |        |
| Pre-checked boxes     | Are pre-checked boxes or opt-out defaults used for purposes requiring opt-in?                                  |        |
| Minors                | Is there a process for identifying and handling personal information of minors?                                |        |
| Conditions of service | Is consent tied as a condition of service for purposes beyond what is necessary?                               |        |

**Common gaps:**

- Pre-ticked checkboxes or opt-out mechanisms for purposes requiring express consent
- Long terms and conditions that bury consent provisions (fails plain language / emphasis
  requirements)
- No consent withdrawal mechanism or unclear process
- Bundled consent requiring individuals to accept all uses or none
- Consent made a condition of service for purposes that are not necessary to the service
- Retroactive consent attempts for new uses of previously collected data
- Children's data collected without parental consent verification

**Severity calibration:**

- Express consent absent for sensitive information: CRITICAL
- Consent withdrawal impossible or unreasonably difficult: HIGH
- Consent buried in unreadable fine print (fails OPC meaningful consent): HIGH
- Pre-checked boxes for opt-in purposes: HIGH
- Bundled consent for distinguishable purposes: MEDIUM

---

### Principle 4 — Limiting Collection (Clause 4.4)

**Statutory requirement**: Collect only the personal information necessary for the
identified purposes. Do not collect information indiscriminately. The means of collection
must be fair and lawful.

**Assessment checklist:**

| Requirement        | Assessment Question                                                                            | Status |
| ------------------ | ---------------------------------------------------------------------------------------------- | ------ |
| Minimum necessary  | Is only the personal information necessary for identified purposes collected?                  |        |
| Proportionality    | Is there documented justification for each category of personal information collected?         |        |
| Collection methods | Are collection methods fair and lawful (no deception, coercion, inappropriate inducement)?     |        |
| Excess collection  | Are there categories of personal information collected for which no identified purpose exists? |        |
| Technical defaults | Are technical systems configured to collect minimum necessary data (privacy by default)?       |        |

**Common gaps:**

- Collecting additional personal information "just in case" it may be useful later
- Forms that collect more information than needed for the specific transaction
- Analytics and tracking tools that collect behavioural data beyond what is necessary
- Legacy systems that continue collecting data for obsolete purposes

**Severity calibration:**

- Systematic excess collection beyond any identified purpose: HIGH
- No periodic review of data collection practices against purposes: MEDIUM
- Isolated legacy excess collection: MEDIUM

---

### Principle 5 — Limiting Use, Disclosure, and Retention (Clause 4.5)

**Statutory requirement**: Do not use or disclose personal information for purposes other
than those for which it was collected, except with consent or as required by law. Retain
personal information only as long as necessary for the fulfillment of identified purposes.

**Assessment checklist:**

| Requirement                | Assessment Question                                                                                                                  | Status |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| Use limitation             | Is personal information used only for identified purposes or with consent/legal authorization?                                       |        |
| Disclosure controls        | Is personal information disclosed to third parties only with consent or legal authority?                                             |        |
| Retention schedule         | Is there a documented retention schedule aligned to purposes?                                                                        |        |
| Disposal/destruction       | Is personal information securely disposed of when retention period ends?                                                             |        |
| Secondary use              | Is there a process for identifying and obtaining fresh consent for secondary uses?                                                   |        |
| Third-party disclosures    | Are all third-party disclosures documented? Are they limited to what is necessary?                                                   |        |
| Legal disclosure authority | When disclosing under law enforcement or legal process, is there a documented process for reviewing and responding to such requests? |        |

**Common gaps:**

- No documented retention schedule; information retained indefinitely "by default"
- Customer data repurposed for analytics or marketing without additional consent
- Third-party disclosures not documented or not limited to necessary parties
- No secure disposal/destruction process for paper and electronic records
- Customer service data retained after account closure without justification

**Severity calibration:**

- Use of personal information for undisclosed purposes without consent: CRITICAL
- No retention schedule: HIGH
- Undocumented third-party disclosures: HIGH
- No secure disposal process: MEDIUM

---

### Principle 6 — Accuracy (Clause 4.6)

**Statutory requirement**: Personal information must be as accurate, complete, and
up-to-date as is necessary for the purposes for which it is to be used. Inaccurate
information must not be routinely used or disclosed to third parties without correction.

**Assessment checklist:**

| Requirement           | Assessment Question                                                                                                                                   | Status |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Accuracy policies     | Are there processes to ensure personal information is accurate, complete, and current for its intended use?                                           |        |
| Correction mechanisms | Can individuals request correction of inaccurate information?                                                                                         |        |
| Pre-decision review   | For decisions that significantly affect individuals (e.g., credit decisions, employment decisions), is accuracy verified before the decision is made? |        |
| Disclosure accuracy   | Before disclosing personal information to third parties, is accuracy assessed?                                                                        |        |

**Common gaps:**

- Customer profiles maintained with outdated information used for important decisions
- No process for individuals to request and obtain correction of their information
- Correction requests received but no formal process to update records across all
  systems containing the inaccurate information

**Severity calibration:**

- No accuracy checks before consequential decisions: HIGH
- No correction request process: MEDIUM
- Information chronically inaccurate due to poor data quality practices: MEDIUM

---

### Principle 7 — Safeguards (Clause 4.7)

**Statutory requirement**: Protect personal information with security safeguards
appropriate to the sensitivity of the information. Safeguards must protect against loss,
theft, unauthorized access, disclosure, copying, use, and modification. The level of
protection must be proportionate to the sensitivity of the information.

**Assessment dimensions:**

| Safeguard Category            | Requirements                                                                                                                                   |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Physical safeguards**       | Locked filing cabinets, restricted server room access, visitor logs, clean-desk policy, secure disposal of physical documents                  |
| **Organizational safeguards** | Security policies, access controls (need-to-know), background checks for high-risk roles, confidentiality agreements, training                 |
| **Technical safeguards**      | Encryption (at rest and in transit), access controls, authentication, audit logs, vulnerability management, patch management, network security |

**Assessment checklist:**

| Requirement                           | Assessment Question                                                                                                                   | Status |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Safeguards appropriate to sensitivity | Are safeguards calibrated to information sensitivity (e.g., health/financial data gets stronger controls than business contact info)? |        |
| Physical controls                     | Are physical records secured? Is access to physical storage restricted?                                                               |        |
| Technical controls                    | Is data encrypted at rest and in transit? Are access controls in place?                                                               |        |
| Organizational controls               | Are need-to-know access controls implemented? Are confidentiality agreements in place for employees and contractors?                  |        |
| Vendor/processor safeguards           | Are third-party processors contractually required to implement comparable safeguards?                                                 |        |
| Breach response                       | Is there a documented breach response plan aligned to SOR/2018-64 obligations?                                                        |        |
| Security testing                      | Is vulnerability assessment/penetration testing conducted periodically?                                                               |        |
| Audit logs                            | Are access and modification logs maintained for sensitive information?                                                                |        |

**Common gaps:**

- No encryption for sensitive data (health records, SIN, financial data) at rest
- Shared credentials or overly broad access permissions
- No third-party security assessment for processors handling sensitive data
- No documented breach response plan or untested plan
- Paper records with sensitive information not secured or destroyed
- Shadow IT systems handling personal information outside official controls

**Severity calibration:**

- Sensitive information unencrypted: CRITICAL
- No breach response plan where mandatory breach reporting applies: CRITICAL
- No access controls for sensitive data systems: HIGH
- No processor security requirements in contracts: HIGH
- No security training: MEDIUM

---

### Principle 8 — Openness (Clause 4.8)

**Statutory requirement**: Make specific information about policies and practices
relating to the management of personal information readily available to individuals.
This includes information about: the privacy officer's name/title and contact information,
how to gain access to personal information held by the organization, what type of
personal information is held and a general account of its use, and what personal
information is made available to related organizations.

**Assessment checklist:**

| Requirement                  | Assessment Question                                                                                    | Status |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ | ------ |
| Privacy policy existence     | Is there a privacy policy that describes the organization's information practices?                     |        |
| Readily available            | Is the privacy policy easy to find (e.g., linked in the footer of every page)?                         |        |
| Privacy officer contact      | Does the privacy policy identify the privacy officer or a privacy contact with contact information?    |        |
| Collection and use described | Does the privacy policy describe what personal information is collected and for what purposes?         |        |
| Individual rights described  | Does the privacy policy explain how individuals can access their information and challenge compliance? |        |
| Third-party disclosures      | Does the privacy policy describe to whom personal information is disclosed?                            |        |
| Cross-border transfers       | Does the privacy policy disclose that information may be transferred outside Canada?                   |        |
| Currency                     | Is the privacy policy current — reflecting current practices and recent legal developments?            |        |

**Common gaps:**

- Privacy policy buried in footer and not accessible from collection points (e.g., account
  registration pages)
- Privacy policy describes what the organization should do but not what it actually does
- No mention of cross-border transfers despite personal information being sent to US or
  other foreign servers
- Privacy officer contact information absent or generic ("privacy@company.com" with no
  name or title)
- Privacy policy last updated several years ago and failing to reflect current practices

**Severity calibration:**

- No privacy policy: HIGH (direct PIPEDA violation)
- Privacy policy exists but is inaccessible: HIGH
- Privacy policy omits cross-border transfer disclosure: MEDIUM
- Privacy policy is outdated: MEDIUM

---

### Principle 9 — Individual Access (Clause 4.9)

**Statutory requirement**: Upon written request, an organization must (a) inform
individuals of the existence, use, and disclosure of their personal information and
(b) give the individual access to that information. The organization must respond within
30 days (extendable by up to 30 days with written notice). The organization may charge
a minimal fee. Grounds for refusal include solicitor-client privilege, information
revealing third-party personal information, and information prohibitively costly to
retrieve.

**Assessment checklist:**

| Requirement                | Assessment Question                                                                                   | Status |
| -------------------------- | ----------------------------------------------------------------------------------------------------- | ------ |
| Access request process     | Is there a documented process for receiving and handling access requests?                             |        |
| 30-day response timeline   | Is the organization capable of responding within 30 days?                                             |        |
| Extension process          | Is there a process for granting extensions (up to 30 days) with written notice?                       |        |
| Refusal grounds            | Is there a process for assessing and documenting refusal grounds (and providing reasons for refusal)? |        |
| Format of response         | Can the organization produce personal information in an understandable format?                        |        |
| Correction request process | Is there a process for handling correction requests and amending records?                             |        |
| Third-party information    | Is there a process for severing third-party personal information from access responses?               |        |
| Documentation              | Are access request receipts, responses, and refusals documented?                                      |        |

**Common gaps:**

- No formal access request process; requests handled ad hoc or not at all
- No systematic way to locate all personal information held about an individual across
  multiple systems
- Access requests treated as customer service inquiries rather than legal obligations
- No documented justification for refusals
- Correction requests acknowledged but records not actually updated in downstream systems

**Severity calibration:**

- No access request process: HIGH
- Inability to locate personal information in response to access requests (data mapping
  gap): HIGH
- No correction request process: MEDIUM
- Access request response capability limited by poor data inventory: MEDIUM

---

### Principle 10 — Challenging Compliance (Clause 4.10)

**Statutory requirement**: An individual must be able to address a challenge about
compliance with PIPEDA to the designated accountable individual or individuals. The
organization must inform the individual of the avenues of recourse available to them,
investigate complaints, take appropriate measures to correct information-handling
practices, and inform the individual of the outcome.

**Assessment checklist:**

| Requirement                | Assessment Question                                                                            | Status |
| -------------------------- | ---------------------------------------------------------------------------------------------- | ------ |
| Complaint process          | Is there a documented, accessible complaint process?                                           |        |
| Complaint receipt          | Is there a defined intake mechanism (email, form, phone) for privacy complaints?               |        |
| Investigation process      | Are complaints investigated in a timely manner? Is there a documented investigation procedure? |        |
| OPC referral information   | Does the process inform complainants of their right to complain to the OPC?                    |        |
| Outcome communication      | Are complainants informed of investigation outcomes and any corrective actions taken?          |        |
| Tracking and documentation | Are complaints tracked, documented, and used to improve practices?                             |        |

**Common gaps:**

- Privacy complaints handled as customer service complaints without legal compliance
  framework
- No OPC referral information provided to complainants
- Complaints not documented, preventing trend analysis or demonstration of responsiveness
- Investigation outcomes never communicated to complainants

**Severity calibration:**

- No complaint mechanism: HIGH
- Complaints not investigated: HIGH
- OPC referral information not provided: MEDIUM
- No outcome communication: MEDIUM

---

## Cross-Border Transfer Assessment Framework

PIPEDA uses an **accountability model** (not an adequacy model like GDPR). The organization
remains accountable for personal information transferred outside Canada to third parties
for processing, and must use contractual or other means to provide a comparable level of
protection.

**Key legal basis:**

- PIPEDA Schedule 1, Clause 4.1.3: "An organization is responsible for personal
  information in its possession or custody, including information that has been transferred
  to a third party for processing."
- OPC Guidance: "Transferring Personal Information Across Borders" (May 2009, updated 2019) [VERIFY for current version]

**Assessment checklist:**

| Requirement                 | Assessment Question                                                                                                                            | Status |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Transfer inventory          | Has the organization identified all jurisdictions to which personal information is transferred?                                                |        |
| Contractual protections     | Are there contracts with foreign processors requiring PIPEDA-comparable protection?                                                            |        |
| Privacy policy disclosure   | Does the privacy policy disclose cross-border transfers and explain that foreign laws may apply?                                               |        |
| Individual notice           | Are individuals notified before cross-border transfers of their information?                                                                   |        |
| Country risk assessment     | Has the organization assessed privacy law adequacy/risk for each country of transfer?                                                          |        |
| Due diligence on processors | Does the organization conduct due diligence on foreign processor security practices?                                                           |        |
| Jurisdiction-specific risk  | Are transfers to jurisdictions with broad government access powers (e.g., US CLOUD Act, national security requests) flagged and risk-assessed? |        |

**OPC position on key cross-border issues:**

- The OPC has found that transfers to the US under the USA PATRIOT Act do not automatically
  violate PIPEDA, but organizations must disclose the possibility of US government access
  to individuals [VERIFY]
- Cloud computing arrangements with US providers are permitted but organizations must
  maintain accountability through contractual terms and due diligence

**Severity calibration:**

- No contracts with foreign processors: HIGH
- Privacy policy does not disclose cross-border transfers: MEDIUM
- No country-level risk assessment for high-risk jurisdictions: MEDIUM
- Transfers to cloud services with no contractual PIPEDA protections: HIGH

---

## Provincial Compliance Overlay

### British Columbia (BC PIPA)

BC PIPA (SBC 2003, c.63) is "substantially similar" to PIPEDA and displaces it for
intra-provincial commercial activities. Key differences from PIPEDA:

| Feature                | BC PIPA                                                                                   | PIPEDA                                             |
| ---------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Breach notification    | Recommended but not mandatory under PIPA itself; see privacy breach response skill        | Mandatory to OPC when RROSH                        |
| Consent model          | Express consent generally required by default; implied consent in specified circumstances | Express or implied depending on sensitivity        |
| Employee information   | Covered for provincially regulated businesses                                             | Not covered for provincially regulated non-FWUBs   |
| Regulator              | Office of the Information and Privacy Commissioner for BC (OIPC BC)                       | Office of the Privacy Commissioner of Canada (OPC) |
| Cross-border transfers | Similar accountability approach to PIPEDA                                                 | Accountability model                               |

**⟁ CLARIFY** for BC-based organizations: Ask whether a full BC PIPA compliance
assessment is needed alongside the PIPEDA assessment. If yes, refer to the
`bc-pipa-privacy-breach-response-and-voluntary-notification-operations` skill for
breach-specific operations, and note that a separate BC PIPA program assessment skill
may be needed.

### Alberta (AB PIPA)

AB PIPA (SA 2003, c.P-6.5) is "substantially similar" to PIPEDA and displaces it for
intra-provincial commercial activities. Key differences from PIPEDA:

| Feature              | AB PIPA                                                                                           | PIPEDA                                           |
| -------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Breach notification  | Mandatory breach notification since 2010 — requires notification to OIPC and affected individuals | Mandatory since 2018 (SOR/2018-64)               |
| Consent model        | Express consent required by default; implied consent for specific circumstances                   | Express or implied depending on sensitivity      |
| Employee information | Covered for provincially regulated businesses                                                     | Not covered for provincially regulated non-FWUBs |
| Regulator            | Office of the Information and Privacy Commissioner of Alberta (OIPC AB)                           | OPC                                              |

### Quebec (Law 25 / Law 64)

Quebec's Act respecting the protection of personal information in the private sector (as
amended by Law 25, also known as Law 64) is the most stringent Canadian private-sector
privacy law, with significant differences from PIPEDA:

| Feature                         | Quebec Law 25                                                                             | PIPEDA                                                        |
| ------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Privacy Impact Assessment (PIA) | **Mandatory** before any project involving personal information that could affect privacy | Not mandatory under PIPEDA                                    |
| Chief Privacy Officer           | **Mandatory designation**, with public name/contact                                       | Privacy officer required but no public listing requirement    |
| Breach notification             | 60-day notification to CAI; individual notification when risk of serious injury           | "As soon as feasible" to OPC; RROSH threshold for individuals |
| Right to erasure                | Yes (in specified circumstances)                                                          | No explicit right                                             |
| Automated decision-making       | Transparency and human review rights                                                      | Not specifically addressed                                    |
| Data portability                | Yes (technology-mediated portability)                                                     | No                                                            |
| Data minimization               | Express minimization requirement                                                          | Implied through limiting collection/use principles            |
| Regulator                       | Commission d'accès à l'information (CAI)                                                  | OPC                                                           |
| Penalties                       | Administrative monetary penalties up to CAD 25M or 4% global revenue                      | Up to CAD 100,000 per offence                                 |

**Key assessment point for Quebec**: Organizations must assess Law 25 requirements
separately; full Law 25 compliance goes substantially beyond PIPEDA. For breach response,
refer to the `quebec-law-25-confidentiality-incident-response-operations` skill.

---

## CPPA Readiness Gap Analysis

Bill C-27 (Consumer Privacy Protection Act) died on the order paper in January 2025 but
may be reintroduced. Key proposed changes that organizations should prepare for:

| CPPA Provision                                          | PIPEDA Gap                                   | Readiness Action                                                            |
| ------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------- |
| **Explicit right to erasure** (s.55)                    | No equivalent in PIPEDA                      | Build data erasure capabilities; document lawful grounds for retention      |
| **Right to portability** (s.62)                         | No equivalent                                | Inventory data, build export functionality for customer data                |
| **Automated decision-making** transparency (s.63)       | No equivalent                                | Document ADM systems; prepare explanation frameworks                        |
| **Algorithmic transparency**                            | No equivalent                                | Inventory algorithmic systems; prepare transparency disclosures             |
| **Higher penalties** (5% global revenue or CAD 25M)     | Max CAD 100,000 under PIPEDA                 | Treat material compliance gaps with higher urgency                          |
| **Privacy Management Program** (s.9, mandatory)         | Best practice under PIPEDA but not mandatory | Formalize and document privacy management program                           |
| **Consent exceptions** (legitimate interest equivalent) | More limited exceptions under PIPEDA         | Map current consent practices; identify where legitimate interest may apply |
| **Sensitive information** enhanced consent              | PIPEDA requires express consent              | Audit sensitive data collection for consent quality                         |
| **Children's data** enhanced protections                | PIPEDA has no age-specific rules             | Identify child users; build enhanced consent and protection processes       |
| **Security research** exception                         | PIPEDA: no explicit research exception       | No action required but monitor for changes                                  |
| **OPC enforcement** (direct order-making power)         | OPC cannot impose fines directly             | Treat OPC compliance as if it has direct enforcement authority              |

**CPPA readiness priority**: Organizations should treat material PIPEDA gaps as CPPA
priority remediation items given the likelihood of future reform and the significantly
higher penalty exposure under the proposed regime.

---

## Compliance Classification System

### COMPLIANT

The organization's practices fully meet the PIPEDA requirement for this principle/element.
Documentation supports compliance; practices align with OPC guidance.

**Action**: Document finding. Schedule periodic review.

### PARTIAL

The organization has some elements in place but material gaps exist. The requirement is
partially met; additional work is needed.

**Action**: Document specific gaps. Assign owner and target date for remediation. Prioritize
based on severity.

### NON-COMPLIANT

The organization fails to meet the PIPEDA requirement. The gap is clear and documentable.
Risk of OPC complaint, investigation, or enforcement.

**Action**: Immediate escalation to privacy officer and legal counsel. Remediation plan
required within defined timeline. Document risk acceptance if remediation cannot be
immediate.

### GAP

No evidence of compliance found. The organization may not have considered this requirement.
Significant exposure.

**Action**: Treat as NON-COMPLIANT with highest urgency. Escalate to senior management.

### N/A

The requirement is not applicable given the organization's specific activities, scale,
or the personal information categories processed.

**Action**: Document the basis for N/A determination with supporting rationale.

---

## Severity and Risk Prioritization Framework

### CRITICAL — Immediate Action Required

Direct statutory violation creating exposure to OPC complaint, investigation, or
Federal Court proceeding. Potential for reputational damage if publicly disclosed.

**Examples:**

- Processing personal information without any form of valid consent where consent is required
- Sensitive information (health, financial, government ID, biometric) held without
  express consent
- Personal information used or disclosed for purposes never disclosed to individuals
- No breach response capability where breach notification obligations exist
- No security safeguards for highly sensitive data categories

**Action**: Escalate to privacy officer and legal counsel immediately. Remediate within
30 days or document formal risk acceptance by senior management.

### HIGH — Remediation Within 90 Days

Material non-compliance that a reasonable privacy officer would treat as a priority.
OPC investigation risk if a complaint is filed. Elevated regulatory exposure.

**Examples:**

- No designated privacy officer
- No formal access request process
- Significant gaps in consent mechanism (buried in fine print, no withdrawal mechanism)
- Third-party processors without data processing agreements
- Retention schedule absent or not enforced
- Privacy policy missing required disclosures
- No staff training on PIPEDA

**Action**: Assign owner. Develop remediation plan within 30 days. Remediate within 90 days.

### MEDIUM — Remediation Within 180 Days

Process gap that creates compliance risk over time. OPC would likely note these in an
audit but may not initiate formal proceedings on these alone.

**Examples:**

- Privacy policy outdated but substantively accurate
- Accuracy mechanisms insufficient for low-stakes data
- Complaint process exists but inadequately documented
- Consent mechanism functional but not fully meeting OPC 2019 Meaningful Consent guidelines

**Action**: Include in next privacy management program review cycle. Remediate within
180 days.

### LOW — Best Practice Improvement

Minor gap or best practice improvement that enhances program quality but does not create
immediate regulatory exposure.

**Examples:**

- Privacy policy could be clearer or more accessible
- Training frequency adequate but could be more regular
- Data inventory exists but could be more granular

**Action**: Include in annual privacy program review. No immediate remediation required.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify organization type, operating provinces, industry, and data categories.
Determine which PIPEDA principles are most material given the organization's profile.
Identify which OPC guidance documents are most relevant.

**DO**: Apply principle-by-principle assessment. Review documentation. Classify findings.
Generate remediation recommendations.

**CHECK**: Run Citation Quality Gates. For CRITICAL and NON-COMPLIANT findings, run
Self-Interrogation. Verify completeness (all 10 principles addressed). Assign confidence
levels.

**ACT**: Note emerging OPC guidance or enforcement trends that may affect the assessment.
Flag CPPA readiness items. Document limitations and scope caveats.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                | Fail Action                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Source**     | Every PIPEDA compliance claim cites a specific PIPEDA clause, OPC guidance, or established principle                                | Add citation or mark "[UNVERIFIED — counsel to confirm]"      |
| **Format**     | All citations follow consistent Canadian legal citation format (statute/section, OPC document with date)                            | Fix format                                                    |
| **Currency**   | Every cited provision checked for amendments or repeal; OPC guidance checked for updates                                            | Flag "[CHECK CURRENCY — may have been amended or superseded]" |
| **Domain**     | Analysis stays within PIPEDA scope; no assumptions from GDPR, CCPA, or other non-Canadian privacy regimes imported without labeling | Remove or flag cross-regime bleed                             |
| **Confidence** | Uncertainty explicitly stated; if OPC position on an issue is unsettled or evolving, say so                                         | Add confidence qualifier                                      |

### Self-Interrogation for NON-COMPLIANT and CRITICAL Findings

For any finding classified as NON-COMPLIANT or CRITICAL, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance determination follow
logically from the cited PIPEDA provision or OPC guidance? Would the OPC actually
characterize this as a violation based on its enforcement history? Is there a
reasonable interpretation that supports compliance?

**Pass 2 — Completeness**: Have all relevant PIPEDA provisions and OPC guidance
documents been considered? Are there exceptions, carve-outs, or safe harbours that
might affect the determination? Have substantially similar provincial law differences
been factored in for organizations operating in BC, AB, or QC?

**Pass 3 — Challenge**: What is the strongest argument that the organization IS
compliant or that the gap is not material? Under what circumstances would a reasonable
privacy counsel accept this risk without immediate remediation? Is the CRITICAL/NON-COMPLIANT
classification proportionate to the actual exposure?

If any pass reveals a weakness, revise the classification before delivery. Mark the
Glass Box audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                        | Action                                                   |
| ------------ | --------- | -------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear PIPEDA provision, settled OPC position                   | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong PIPEDA basis, OPC has addressed similar situations      | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good PIPEDA arguments, OPC position unclear                    | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40-0.59 | Genuinely uncertain — evolving OPC position or novel situation | Flag for privacy counsel review                          |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                        | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every PIPEDA compliance assessment output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-ca-pipeda-compliance"
  organization: "[Organization name or description]"
  assessment_date: "[date]"
  scope: "[Full / Targeted — specify principles] / [Pre-investigation / New product / M&A]"
  operating_provinces: "[list]"
  fwub_status: "[Yes / No / Unclear]"
  sensitive_data_categories: "[list or None]"
  documentation_reviewed:
    - "[Privacy policy — version/date]"
    - "[Data inventory — version/date]"
    - "[Consent forms — version/date]"
    - "[Other documents reviewed]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  opc_guidance_consulted:
    - "[OPC document title — date — VERIFIED or UNVERIFIED]"
  statutes_consulted:
    - "[Statute and section — VERIFIED or UNVERIFIED]"
  principles_assessed: "[number out of 10]"
  findings_by_classification:
    compliant: "[number]"
    partial: "[number]"
    non_compliant: "[number]"
    gap: "[number]"
    na: "[number]"
  findings_by_severity:
    critical: "[number]"
    high: "[number]"
    medium: "[number]"
    low: "[number]"
  provincial_overlay: "[BC PIPA / AB PIPA / Quebec Law 25 / None / N/A]"
  cppa_readiness: "Included / Not included"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL/NON-COMPLIANT items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, documentation gaps, or reliance on unverified representations]"
  reviewer: "AI-assisted — requires review by qualified Canadian privacy counsel"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in PIPEDA compliance assessments:

1. **Treating PIPEDA as equivalent to GDPR** — PIPEDA uses an accountability model for
   cross-border transfers, not adequacy. Consent requirements, rights, and penalty
   structures differ materially. Do not import GDPR concepts (data controllers, data
   processors, legal bases, SCCs, BCRs, adequacy decisions) as if they apply to PIPEDA
   without checking whether a Canadian equivalent exists.

2. **Ignoring the provincial overlay** — Recommending PIPEDA compliance for a BC, AB, or
   QC organization without flagging that substantially similar provincial laws apply for
   intra-provincial activities is an incomplete analysis. Quebec Law 25 in particular is
   significantly stricter than PIPEDA.

3. **Confusing meaningful consent with formal consent** — A checkbox that an individual
   has technically clicked is not necessarily "meaningful" consent under OPC 2019 guidance.
   Assess whether the consent mechanism meets all 7 OPC meaningful consent elements, not
   just whether a mechanism exists.

4. **Applying PIPEDA to employees of non-FWUBs** — PIPEDA generally does not apply to
   employee personal information of privately regulated (non-FWUB) organizations in the
   employment context in provinces without substantially similar legislation. This is a
   frequently misunderstood scope issue. Flag it rather than assuming application.

5. **Treating the accountability principle as purely organizational** — PIPEDA Clause
   4.1.3 makes organizations accountable for personal information transferred to third
   parties for processing. Many organizations believe accountability transfers to the
   processor. It does not. Failure to have contracts with processors and to exercise
   oversight is itself a PIPEDA violation.

6. **Overlooking business contact information** — PIPEDA does not apply to business
   contact information (name, title, business address, business phone, business email used
   in employment capacity). Incorrectly applying PIPEDA requirements to business contact
   information creates unnecessary burden; conversely, improperly treating personal
   emails or personal phones as "business contact information" creates compliance risk.

7. **Assuming "as soon as feasible" means the same as "72 hours"** — The PIPEDA breach
   notification obligation to the OPC is "as soon as feasible" — there is no fixed
   timeline. OPC guidance indicates it expects prompt reporting but has not set a 72-hour
   rule. Do not import the GDPR 72-hour rule into PIPEDA advice.

8. **Conflating RROSH and meaningful harm** — The "real risk of significant harm" threshold
   for PIPEDA breach notification (ss.10.1(7)-(8)) is a specific statutory test involving
   both information sensitivity and probability of misuse. Do not apply generic "harm"
   analysis; apply the two-factor statutory RROSH test.

9. **Treating the OPC as having GDPR-style enforcement powers** — The OPC cannot directly
   impose fines. It investigates, makes findings, attempts to negotiate resolution, and can
   seek Federal Court orders for compliance. While reputational and legal consequences of
   OPC findings are significant, the immediate enforcement mechanism differs from GDPR
   supervisory authority powers.

10. **Assuming CPPA is in force** — Bill C-27 died on the order paper in January 2025.
    Canada operates under PIPEDA as of 2026. Forward-looking CPPA readiness assessment is
    valuable but should be clearly distinguished from current PIPEDA obligations. Never
    state CPPA requirements as if they are current law without a [VERIFY] tag.

11. **Ignoring the sensitive information threshold** — PIPEDA requires express consent
    for sensitive information (health, financial, government ID, sexual orientation,
    religious/political beliefs, biometric data). Many organizations apply implied consent
    across all categories. This is a common and material compliance failure — assess
    consent type carefully against data sensitivity.

12. **Overlooking consent for secondary uses** — When an organization wants to use
    personal information collected for Purpose A for the new Purpose B, this generally
    requires fresh consent. Many organizations treat original consent as perpetually
    covering all future uses. This is incorrect and a common basis for OPC complaints.

13. **Accepting "we have a privacy policy" as sufficient for openness** — Principle 8
    requires that the policy be "readily available." A privacy policy buried in a legal
    archive, written in legalese, or last updated in 2018 does not satisfy the openness
    principle. Assess accessibility, currency, and comprehensibility.

14. **Omitting retention schedule gaps** — No retention schedule, or a schedule that
    says "as long as necessary" without defining specific periods, violates Principle 5.
    This is consistently identified by the OPC as a common gap. Do not accept vague
    retention descriptions as compliant.

15. **Ignoring the cross-border transfer accountability chain** — Many organizations
    transfer personal information to cloud services without contracts, and their cloud
    providers sub-contract to additional processors in multiple jurisdictions. Accountability
    follows the data through the entire processing chain. Failure to map and contractually
    address this chain is a systematic accountability gap.

16. **Treating OPC findings as only applying to the subject organization** — OPC PIPEDA
    findings apply to the organization investigated but signal how the OPC will approach
    similar issues in other organizations. Relevant OPC findings should be applied broadly
    in compliance assessments, not treated as binding only on the original respondent.

17. **Assessing consent mechanisms without testing them** — A written consent mechanism
    may appear compliant on paper but be dysfunctional in practice (withdrawal option
    technically available but effectively hidden, consent is pre-ticked, plain language
    requirement unmet in implementation). Where possible, test consent mechanisms in
    practice, not just review documentation describing them.

---

## Writing Standards

Apply plain-language discipline to all output:

**For compliance findings** (shared with privacy officer, legal counsel, senior management):

- Lead with the finding (COMPLIANT / PARTIAL / NON-COMPLIANT / GAP) before the reasoning
- Active voice: "The organization does not have a retention schedule" not "No retention
  schedule has been implemented"
- Specific, not vague: cite the PIPEDA clause and OPC guidance driving each finding
- One issue per finding; do not bundle multiple non-compliance items together
- Include a concrete remediation step, not just an observation

**For the executive summary**:

- Accessible to non-lawyers: avoid PIPEDA clause numbers without explanation in the summary
- Prioritize CRITICAL and HIGH items upfront
- Quantify: "3 CRITICAL gaps, 5 HIGH gaps, 4 MEDIUM gaps, 2 LOW items" conveys urgency better
  than narrative prose

**Quality gates before delivery:**

1. Can the organization's privacy officer act on each finding without re-reading the source
   material?
2. Is every classification supported by a cited PIPEDA provision or OPC guidance reference?
3. Could any finding be interpreted as more or less severe than intended? If so, clarify.
4. Are PIPEDA obligations clearly distinguished from provincial obligations and CPPA
   readiness items?
5. Is the Glass Box audit trail complete and accurate?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary Canadian legal
research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for: PIPEDA consolidated text, OPC guidance documents, OPC PIPEDA
  findings relevant to the industry, provincial privacy law texts and guidance
- Save results to `/tmp/legalcode-pipeda-authority.md`
- Reference verified authority from the temp file throughout the assessment
- Check for recent OPC guidance or findings that may affect specific principle assessments
- Verify the current status of Bill C-27 / CPPA legislative process
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and OPC guidance references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all citations require
independent verification"`
- Focus the assessment on structural compliance gaps and process issues rather than
  legal certainty on specific statutory interpretations
- Recommend that findings are reviewed against current OPC published guidance before
  action is taken

---

## Output Format Template

Structure the final deliverable as:

```markdown
## PIPEDA Compliance Assessment

**Organization**: [name or description]
**Assessment Date**: [date]
**Assessment Scope**: [Full / Targeted — principles covered]
**Operating Provinces**: [list]
**FWUB Status**: [Yes / No / Unclear]
**Documentation Reviewed**: [list]
**Prepared By**: AI-assisted (legalcode-ca-pipeda-compliance skill) — requires qualified
Canadian privacy counsel review

---

## Executive Summary

**Overall Compliance Posture**: [Brief characterization — e.g., "Foundational gaps in
consent, accountability, and retention require immediate attention"]

**Finding Summary**:

- CRITICAL: [number] gaps
- HIGH: [number] gaps
- MEDIUM: [number] gaps
- LOW: [number] items

**Top 3 Priority Actions**:

1. [Most critical gap — one sentence + remediation action]
2. [Second most critical — one sentence + remediation action]
3. [Third most critical — one sentence + remediation action]

---

## Principle-by-Principle Findings

### Principle 1 — Accountability | [COMPLIANT / PARTIAL / NON-COMPLIANT / GAP] | Severity: [CRITICAL / HIGH / MEDIUM / LOW]

**Finding**: [One-paragraph summary of compliance status]

**Gap(s) identified**:

- [Specific gap 1]
- [Specific gap 2]

**Legal basis**: [PIPEDA Schedule 1, Clause 4.1; OPC guidance reference]
**Remediation**: [Specific, actionable steps with suggested owners and timelines]
**Confidence**: [Definite / High / Probable / Possible]

[Repeat for all 10 principles]

---

## Cross-Border Transfer Assessment

**Transfer jurisdictions identified**: [list]
**Overall classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / GAP]
**Key gaps**: [list]
**Remediation**: [steps]

---

## Provincial Compliance Overlay

[Include only for organizations operating in BC, AB, or QC]

### [Province] — [COMPLIANT / PARTIAL / NON-COMPLIANT / N/A]

**Key differences from PIPEDA**: [table or list]
**Gaps specific to [provincial law]**: [list]
**Remediation**: [steps]

---

## CPPA Readiness Gap Analysis

**Overall CPPA readiness**: [Ready / Partially Ready / Not Ready]
**Key gaps vs. proposed CPPA**: [prioritized list with remediation actions]
**Priority rationale**: [Note higher penalty exposure under CPPA]

---

## Remediation Roadmap

| Priority | Gap   | Owner  | Target Date   | Notes |
| -------- | ----- | ------ | ------------- | ----- |
| CRITICAL | [gap] | [role] | [date]        |       |
| HIGH     | [gap] | [role] | [date]        |       |
| MEDIUM   | [gap] | [role] | [date]        |       |
| LOW      | [gap] | [role] | Annual review |       |

---

## Next Steps

1. [Immediate action — within 30 days]
2. [Short-term action — 30-90 days]
3. [Medium-term action — 90-180 days]
4. [Structural improvement — annual cycle]

---

[Glass Box Audit Trail per template above]
```

---

## Localization Notes

This skill is jurisdiction-specific to Canada (Federal). Key localization points if
adapting this assessment for other jurisdictions:

- **Quebec (Law 25)**: Significantly stricter than PIPEDA. A separate Quebec-specific
  compliance skill is recommended for organizations with substantial Quebec operations.
- **BC PIPA / AB PIPA**: Apply provincial compliance checklist additions for intra-provincial
  activities. BC breach notification is voluntary (not mandatory under PIPA alone). Alberta
  has had mandatory breach notification since 2010.
- **Cross-border**: If the organization is subject to GDPR, CCPA, or other regimes in
  addition to PIPEDA, a multi-regime assessment using `legalcode-multi-jurisdiction-privacy-
comparison` may be more appropriate than this single-jurisdiction skill.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on: PIPEDA (SC 2000, c.5)
consolidated text; OPC published guidance including Meaningful Consent Guidelines (2019),
Cross-Border Transfer Guidance (2009/updated), Privacy Breach Guidelines; existing
Legalcode Canada federal privacy skills (`pipeda-breach-reporting-and-notification-
operations`); the `legalcode-contract-review` gold standard structural framework
(multi-step workflow, 10-principle assessment, COMPLIANT/PARTIAL/NON-COMPLIANT
classification, Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box
audit trail, 17 anti-patterns); deep web research on PIPEDA enforcement, OPC guidance, and
provincial privacy law interactions. Related skills: `pipeda-breach-reporting-and-
notification-operations`, `bc-pipa-privacy-breach-response-and-voluntary-notification-
operations`, `alberta-pipa-privacy-breach-notification-operations`, `quebec-law-25-
confidentiality-incident-response-operations`.
