---
name: legalcode-eu-privacy-notice-drafter
description: Draft and review GDPR-compliant privacy notices for any EU/EEA audience or jurisdiction.
  Use when a user asks to create a privacy policy, privacy notice, Datenschutzerklärung, politique de
  confidentialité, or any Art. 13/14 transparency disclosure.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft and review GDPR-compliant privacy notices for any EU/EEA audience or jurisdiction. Use when a user asks to create a privacy policy, privacy notice, Datenschutzerklärung, politique de confidentialité, or any Art. 13/14 transparency disclosure. Covers five notice types: Website/App, Applicant/Recruiting, Employee, Business Partner (B2B), and B2C Customer. Deep GDPR coverage: controller identity, all six Art. 6 lawful bases, Art. 9 special categories, retention periods, international transfers (SCCs, DPF, BCRs, adequacy), Art. 15–22 data subject rights, Art. 21 right-to-object prominence requirements, Art. 22 automated decision-making, cookie and tracking disclosures, AI Act (Regulation 2024/1689) transparency obligations, DPIA indicators, DPO, joint controllership (Art. 26), and member-state localization for all 27 EU Member States plus EEA. Also triggers when reviewing an existing privacy notice for GDPR compliance gaps, missing mandatory disclosures, or update requirements after regulatory changes. Native EU replacement for imported privacy-notice packs.


# Legalcode EU Privacy Notice Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and compliance
> review of GDPR privacy notices under EU/EEA law. It does not constitute legal advice.
> All outputs should be reviewed by a qualified data protection professional or legal counsel
> licensed in the relevant jurisdiction before publication. Laws and regulatory guidance
> change; verify current applicability — including EDPB guidance, national supervisory
> authority guidance, and any applicable member-state derogations — before relying on any
> provision described here. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources before use.

---

## Purpose and Scope

This skill drafts GDPR-compliant privacy notices for any EU/EEA controller, and reviews
existing notices for compliance gaps. It supports both **creation** (drafting from scratch)
and **review** (auditing an existing notice against Art. 13/14 mandatory disclosures and
member-state requirements).

**Covers:**

- Five notice types: Website/App · Applicant/Recruiting · Employee · Business Partner (B2B) · B2C Customer
- All Art. 13/14 mandatory disclosures with COMPLIANT / PARTIAL / NON-COMPLIANT gap scoring
- All six Art. 6(1) lawful bases with member-state nuances
- Art. 9 special categories with dual-basis protocol
- Art. 22 automated decision-making and EU AI Act (Reg. 2024/1689) interplay
- International transfers: adequacy decisions, SCCs (2021), DPF, BCRs, Art. 49 derogations
- Member-state localization markers for all 27 EU Member States + Norway, Iceland, Liechtenstein
- Retention matrix generation with jurisdiction-specific legal citations
- Cookie and tracking transparency linked to ePrivacy national implementing laws
- DPA/Art. 28 gap identification (processor DPAs required alongside the notice)
- Joint controllership (Art. 26) and Art. 14 indirect-collection disclosure triggers
- DPIA indicator assessment (Art. 35) as a drafting gate

**Does not:**

- Draft Data Processing Agreements (Art. 28) — see `legalcode-dpa-review-and-negotiation`
- Conduct Data Protection Impact Assessments — see `legalcode-dpia-generator`
- Cover UK GDPR as primary regime (but includes UK notes where dual-notice is common)
- Replace the legal review required before publication
- Advise on processing lawfulness beyond what the notice discloses

---

## Jurisdiction and Governing Law

This skill is **EU/EEA-specific** and applies GDPR (Regulation (EU) 2016/679) as its
primary framework, supplemented by the applicable member-state national law at the
controller's registered seat (or principal establishment if multiple states are involved).

**Key legal framework:**

- GDPR Arts. 12–14, 22, 26, 28, 35, 37, 46–49 — transparency, notice, automated decisions,
  joint controllers, processors, DPIAs, DPOs, transfers
- EU AI Act (Regulation (EU) 2024/1689) Arts. 50, 86 — AI transparency obligations (phased
  applicability from August 2025) [VERIFY current applicability date for specific provision]
- ePrivacy Directive 2002/58/EC Art. 5(3) and national implementing laws (TDDDG in DE, PECR
  in UK, CPCE in FR, Telecommunicatiewet in NL, etc.) — cookie/tracking consent
- EDPB Guidelines on transparency (3/2019), special categories (8/2020), consent (05/2020),
  data subject rights (01/2022), DPIAs (from WP29), and legitimate interest (1/2024)

[MEMBER-STATE-SPECIFIC] National derogations and supplementary laws apply per controller
seat — see the **Member-State Localization Reference** section below.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's scenario, the workflow pauses and asks when:

- The answer changes which sections to include or skip
- Multiple valid approaches exist (e.g., combined vs. separate notices)
- A gap or DPIA trigger is found that needs the user's input before proceeding
- Jurisdiction choices affect content materially

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

Accept input in any of these formats:

**For drafting a new notice:**

- Description of the controller's business, processing activities, and target audience
- Answers to a quick-start intake set (present the intake questions in Step 3)
- An existing template to adapt

**For reviewing an existing notice:**

- Pasted text of the existing notice
- File path or URL to the notice
- Instruction to audit for specific issues (e.g., "check if our privacy policy is GDPR-compliant after the DPF decision")

**⟁ CLARIFY** — If the mode is unclear, ask:

> "Are you (A) drafting a new privacy notice from scratch, (B) reviewing an existing notice
> for GDPR compliance, or (C) updating an existing notice after a change (new processors,
> new purposes, regulatory update)?"

---

### Step 2: Gather Context — Notice Type and Jurisdiction

Before collecting detailed processing information, establish the scope. These two decisions
determine everything else.

#### 2a. Notice Type

**⟁ CLARIFY** — Ask as the first question after mode:

> "What type of privacy notice do you need?"

| Type                       | Description                                                        | Primary Legal Hook                                      |
| -------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| **Website / App**          | Visitors, users, subscribers of a website, web app, or mobile app  | Art. 13 GDPR; ePrivacy for cookies                      |
| **Applicant / Recruiting** | Job applicants and candidates                                      | Art. 13/14 GDPR; Art. 88 GDPR + national employment law |
| **Employee**               | Employees, contractors, interns (existing employment relationship) | Art. 13 GDPR; Art. 88 GDPR + national employment law    |
| **Business Partner (B2B)** | Contact persons at vendors, suppliers, clients, partners           | Art. 13 or Art. 14 depending on collection source       |
| **B2C Customer**           | End consumers in a customer/purchase relationship                  | Art. 13 GDPR; ePrivacy for marketing                    |
| **Combined**               | Multiple audiences in one or linked notices                        | All of the above                                        |

The selected type determines: which sections to include/skip, which data categories to probe,
which legal bases are most likely, and which type-specific intake questions to ask.

#### 2b. Jurisdiction

**⟁ CLARIFY** — Ask which countries/markets the service or employment targets:

- **Single-jurisdiction controllers**: Name the Member State where the controller is established.
  Load that state's localization block from the **Member-State Localization Reference**.
- **Multi-jurisdiction controllers**: Identify the principal establishment (for GDPR's
  one-stop-shop mechanism). Load localization blocks for each significant target market.
- **EEA non-EU controllers (NO, IS, LI)**: GDPR applies via EEA Agreement; national
  supplementary laws differ. Flag for country-specific research.

**Multi-language decision:**

| Scenario                             | Approach                                                                                                 |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Single market, single language       | One notice in the market's official language                                                             |
| Single market, international service | Primary market language + English; state governing version                                               |
| Multi-market                         | Separate notices per language/market, or bilingual with clear visual separation; state governing version |
| Pan-EU service                       | English primary + translations for key markets; each version must be standalone and complete             |

---

### Step 3: Information Intake

Collect all information before drafting. Ask in logical groups, not all at once. The notice
cannot be drafted without completing at minimum Groups A–D.

**Summary confirmation**: After intake, produce a structured summary for user confirmation
before drafting (see the template at the end of this step).

#### Group A — Controller Identity (Required)

- Legal entity name and form (GmbH, SA, Ltd., BV, etc.)
- Registered address and country of establishment
- Registration number (Handelsregisternummer, SIREN/SIRET, KvK-nummer, etc.)
- Legal representative name and title
- Contact email and phone
- DPO appointed? → If yes: name/title, contact email (use functional address), whether
  the DPO is internal or external

**Art. 26 — Joint Controllership:**
Ask: "Do you process personal data jointly with another organization for any of the purposes
in this notice, meaning both organizations determine the purposes and means of processing
together?" If yes: the notice must disclose the essence of the Art. 26 arrangement,
including each controller's responsibilities and the designated contact point for data
subjects.

#### Group B — Data Categories and Collection Points (Required)

For each collection point (forms, account creation, cookies, purchase, HR system, etc.):

- What data is collected?
- Is it mandatory or optional for the data subject?
- What is the source: directly from the data subject (Art. 13), or from a third party
  (Art. 14)?

**Standard categories to probe:**

| Category                        | Examples                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------- |
| **Identity**                    | Name, email, phone, address, date of birth, photo, passport/ID                            |
| **Account**                     | Credentials, preferences, settings, activity history                                      |
| **Technical**                   | IP, device ID, browser fingerprint, server/access logs                                    |
| **Browsing**                    | Pages visited, clicks, session duration, referrer URL, scroll depth                       |
| **Transaction**                 | Orders, payment method (via processor), invoices, returns                                 |
| **Communication**               | Messages, support tickets, comments, chat history                                         |
| **Employment**                  | CV/resume, work history, payroll, performance, health/sick leave                          |
| **AI-related**                  | Inputs to AI systems, AI-generated outputs, automated scores/decisions                    |
| **Special categories (Art. 9)** | Health, biometric, political, religious, ethnic, sexual orientation, trade union, genetic |

**If any Art. 9 data is identified** — trigger the Special Category Protocol:

1. Which specific categories are processed?
2. What purpose?
3. Which Art. 9(2) exception? Is there Member State law authorizing it?
4. Is explicit consent documented? How is withdrawal supported?
5. What additional safeguards are in place?
6. Has a DPIA been conducted (mandatory for large-scale Art. 9 processing — Art. 35(3)(b))?
   Every special category processing must cite **both** an Art. 6(1) legal basis **and** an
   Art. 9(2) exception in the notice (dual-basis requirement).

#### Group C — Purposes and Lawful Bases (Required)

For each processing activity, determine the legal basis. Present as a table for user confirmation:

| Purpose                                | Legal Basis (Art. 6)                                   | Art. 9(2) if applicable    | Data Categories |
| -------------------------------------- | ------------------------------------------------------ | -------------------------- | --------------- |
| Service provision / contract execution | Art. 6(1)(b)                                           | —                          | [to fill]       |
| Account management                     | Art. 6(1)(b)                                           | —                          | [to fill]       |
| Legal / tax compliance                 | Art. 6(1)(c) — [specific law to fill]                  | —                          | [to fill]       |
| Analytics (website)                    | Art. 6(1)(a) consent **or** Art. 6(1)(f) LI [assess]   | —                          | [to fill]       |
| Email marketing                        | Art. 6(1)(a) consent [or soft opt-in per national law] | —                          | [to fill]       |
| AI-based processing                    | [determine per use case]                               | [if Art. 9 data involved]  | [to fill]       |
| Employment relationship                | Art. 6(1)(b)/(c) [or national employment law basis]    | Art. 9(2)(b) if applicable | [to fill]       |

**Guidance on basis selection (flag for user review):**

- **Art. 6(1)(a) Consent**: Use for newsletter, marketing cookies, ad tracking, non-essential
  profiling. NOT a good default — consent must be freely given, informed, specific, unambiguous,
  and withdrawable as easily as given (Planet49, C-673/17 [VERIFY]).
- **Art. 6(1)(b) Contract**: Narrowly interpreted. Only processing genuinely necessary for
  contract performance or pre-contractual steps at the data subject's request (EDPB 2/2019).
- **Art. 6(1)(c) Legal Obligation**: Must identify the specific legal provision.
- **Art. 6(1)(f) Legitimate Interest**: Requires documented balancing test (LIA). Data
  subject has absolute right to object for direct marketing (Art. 21(2)).

#### Group D — Recipients and Transfers (Required)

- All processors (Art. 28) with name/category, purpose, and location
- All other recipients (authorities, joint controllers, group companies)
- **DPA gap check**: For each processor identified, ask whether a written Data Processing
  Agreement (Art. 28) exists. If not: flag as a **compliance gap requiring immediate
  remediation** — this is separate from the notice but must be resolved.
- **International transfers** (outside EU/EEA): which countries, which transfer mechanism:
  - Adequacy decision (Art. 45) — current list includes UK, Japan, Canada (PIPEDA),
    South Korea, Switzerland, USA (EU-U.S. DPF — verify recipient's DPF certification)
  - Standard Contractual Clauses 2021 (Art. 46(2)(c)) — specify which module
  - Binding Corporate Rules (Art. 47) — intra-group only
  - Derogations (Art. 49) — explicit consent, necessity for contract, narrow exceptions

**What to disclose in the notice**: processor/recipient name or category, purpose, location,
transfer mechanism. **Do NOT include** DPA terms, sub-processor lists, or technical/
organizational measures (these belong in the Art. 28 agreement).

#### Group E — Cookies and Tracking (Website/App and B2C types only)

- Cookie categories in use: essential, analytics, marketing/advertising, social media, A/B testing
- Specific tools (GA4, Meta Pixel, Matomo, HubSpot, LinkedIn Insight, Hotjar, etc.)
- Consent Management Platform (CMP) in use (Usercentrics, Cookiebot, Axeptio, Didomi, Borlabs, etc.)
- Cookie lifespans
- Server-side tracking or fingerprinting?
- Ask: Is there a separate cookie notice/policy, or should cookies be integrated into the privacy notice?

**ePrivacy mapping** (load relevant national law):

- DE: TDDDG § 25 — consent required for any non-strictly-necessary access/storage on device
- FR: CNIL Guidelines (Délibération 2020-091) — 13-month max, reject as easy as accept
- NL: Telecommunicatiewet Art. 11.7a — AP aggressive enforcement, no cookie walls
- UK: PECR Regulation 6 — broadly similar to ePrivacy Directive
- [other states: apply ePrivacy Directive Art. 5(3) as transposed nationally]

#### Group F — AI and Automated Decision-Making

If the service or employer uses AI/ML:

- What AI systems are used and for what purpose?
- Are decisions solely automated or is there a human in the loop?
- Do decisions produce legal or similarly significant effects on data subjects (Art. 22 trigger)?
- Is user/employee data used to train models?
- EU AI Act classification: prohibited / high-risk / limited-risk / minimal-risk?

**Art. 22 obligations when triggered**: Disclose existence, meaningful information about
the logic involved, significance and envisaged consequences. Safeguards: right to human
intervention, to express point of view, and to contest the decision.

**EU AI Act Art. 50 transparency** (from August 2025): Inform users they interact with
an AI system; disclose AI-generated content; high-risk AI systems require extensive transparency.

#### Group G — DPIA Indicators (Art. 35 Gate)

Before drafting, check whether a DPIA may be mandatory. If **2 or more** of the following
indicators apply, inform the user and recommend a DPIA as a prerequisite to publication:

1. Systematic evaluation/scoring of individuals (profiling, credit scoring, performance scoring)
2. Automated decision-making with legal or similarly significant effects (Art. 22)
3. Systematic monitoring of publicly accessible areas (CCTV, Wi-Fi tracking)
4. Special category data or criminal offence data processed at scale (Art. 9/10)
5. Large-scale processing (high volume, broad geographic scope, many data subjects)
6. Matching or combining datasets in ways data subjects would not reasonably expect
7. Vulnerable data subjects (employees, children, patients, elderly)
8. Innovative use of technology (biometrics, AI/ML, IoT, blockchain for personal data)

Also check national mandatory DPIA lists:

- DE (DSK-Liste der Verarbeitungstätigkeiten, die einer DSFA bedürfen) [VERIFY current list]
- FR (CNIL liste des traitements nécessitant une AIPD) [VERIFY current list]
- [Other MS: EDPB WP248 rev.01 and national supervisory authority lists apply]

If DPIA is required: inform the user, recommend conducting one before processing begins,
and note in the privacy notice that a DPIA has been conducted (without disclosing content).

#### Summary Before Drafting

After intake, confirm with user:

```
NOTICE TYPE:          [Website / Applicant / Employee / B2B / B2C / Combined]
CONTROLLER:           [Name, form, address, registration number]
JURISDICTION(S):      [Countries and principal establishment]
LANGUAGE(S):          [Primary + secondary; governing version]
DPO:                  [Yes/No + contact details]
DATA CATEGORIES:      [List by collection point, flagging Art. 9 if present]
PURPOSES + BASES:     [Table from Group C]
PROCESSORS:           [List with locations + DPA status]
JOINT CONTROLLERS:    [Yes/No + Art. 26 arrangement details]
TRANSFERS:            [Countries + mechanisms]
COOKIES:              [Categories + tools + CMP — if applicable]
AI PROCESSING:        [Yes/No + Art. 22 applicability + AI Act tier]
DPIA REQUIRED:        [Yes/No + indicator count]
SECTIONS TO INCLUDE:  [Per section map for the notice type]
SECTIONS TO SKIP:     [Per section map for the notice type]
OPEN COMPLIANCE GAPS: [DPA gaps, DPIA not conducted, etc.]
```

---

### Step 4: Notice Architecture Selection

Based on the notice type and intake results, determine the document structure.

#### Section Map by Type

| Section                       | Website/App             | Applicant                     | Employee      | B2B                | B2C           |
| ----------------------------- | ----------------------- | ----------------------------- | ------------- | ------------------ | ------------- |
| 1. Controller identity        | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 2. Data collected             | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 3. Purposes and legal bases   | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 4. Recipients                 | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 5. International transfers    | ✅                      | if applicable                 | if applicable | if applicable      | ✅            |
| 6. Retention                  | ✅                      | ✅ critical                   | ✅ critical   | ✅                 | ✅            |
| 7. Data subject rights        | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 8. Cookies and tracking       | ✅ critical             | only if career page           | intranet/MDM  | only if B2B portal | ✅ if online  |
| 9. AI and automated decisions | if applicable           | if applicable                 | if applicable | rarely             | if applicable |
| 10. Data security             | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 11. Children's data           | if accessible to minors | skip (unless intern programs) | skip          | skip               | if applicable |
| 12. Notice updates            | ✅                      | ✅                            | ✅            | ✅                 | ✅            |
| 13. Contact                   | ✅                      | ✅                            | ✅            | ✅                 | ✅            |

**Employee-specific additional sections**: IT monitoring/BYOD, video surveillance (§ 4 BDSG),
GPS/vehicle tracking, whistleblowing channel, works council (Betriebsrat) data access.

#### Combined Notices — Architecture Options

**⟁ CLARIFY** — When covering multiple audiences, ask:

- **Option A: Single comprehensive notice** — merged sections with clear audience sub-headings.
  Best for SMEs with limited processing complexity.
- **Option B: Separate notices per audience** — linked from a central privacy hub. Best for
  large/complex organizations or where audiences have significantly different data flows (e.g.,
  employee + customer + applicant). German best practice strongly favors separate applicant notice.
- **Option C: Layered notice** — short general notice + detailed audience-specific annexes.
  Good for organizations with many data subject categories.

---

### Step 5: Draft the Notice

Using the section map, intake information, and applicable member-state localization blocks,
draft the privacy notice.

#### Standard Document Structure

```
[TITLE: Privacy Notice / Datenschutzerklärung / Politique de confidentialité / etc.]
[Controller Name]
Last updated: [DATE]

TABLE OF CONTENTS (if > 3 pages)

1.  CONTROLLER IDENTITY AND DATA PROTECTION OFFICER
2.  DATA WE COLLECT
3.  PURPOSES AND LEGAL BASES FOR PROCESSING
4.  RECIPIENTS OF YOUR DATA
5.  INTERNATIONAL TRANSFERS
6.  HOW LONG WE KEEP YOUR DATA
7.  YOUR RIGHTS
    [ART. 21 RIGHT TO OBJECT — PRESENTED SEPARATELY AND PROMINENTLY]
8.  COOKIES AND TRACKING TECHNOLOGIES    [Website/App and B2C types]
9.  AI AND AUTOMATED DECISION-MAKING    [if applicable]
10. DATA SECURITY
11. CHILDREN'S DATA                      [if applicable]
12. CHANGES TO THIS NOTICE
13. HOW TO CONTACT US
```

#### Drafting Rules

**Language and tone:**

- Write in the jurisdiction's primary official language. For multi-jurisdiction: primary
  language first, state which version governs.
- Address the reader as "you" / "Sie" / "vous" / "u" — never "the data subject" or
  "the user." The notice is for the data subject, not about them.
- Plain language: understandable by a non-lawyer. Avoid dense legalese.
- Short sentences. Active voice where possible.

**Legal bases — cite precisely:**

- Cite article numbers precisely: "Art. 6(1)(f) GDPR" not "legitimate interest"
- For DE: cite §§ 26 BDSG for employment data alongside DSGVO article
- For FR: cite LIL provision or Code du travail where applicable alongside RGPD article

**Retention periods — be specific:**

- Use specific durations with legal citations: "6 years (§ 257 HGB)" not "as long as necessary"
- Cross-reference the **Retention Matrix** in this skill for jurisdiction-specific defaults

**Art. 21 Right to Object — mandatory prominence:**

- Must be presented **separately and prominently**, NOT buried in a rights list (Art. 21(4) GDPR)
- In German: a dedicated "WIDERSPRUCHSRECHT" section is standard practice (BGH-recommended)
- In French: "DROIT D'OPPOSITION" as a visually distinct section
- In English: "Your Right to Object" highlighted separately from the general rights table

**Transfers:**

- Name the country and mechanism: "Google LLC (USA) — processed under the EU-U.S. Data
  Privacy Framework (EU Commission Adequacy Decision of 10 July 2023)" [VERIFY current DPF status]
- Verify DPF certification at current date before relying on it — certifications can lapse
- For SCCs: state module and effective date

**Cookies:**

- Use tables: cookie name / category / purpose / provider / lifespan
- Reference the CMP for management
- Distinguish consent-based (analytics, marketing) from strictly necessary (session, cart)

**AI / Art. 22:**

- Even where Art. 22 doesn't strictly apply (human in the loop), include an AI section
  if AI processes personal data — EU AI Act Art. 50 may require disclosure independently
- Describe logic, significance, and consequences in plain terms — not source code

**Placeholder management:**

- Use clearly marked placeholders: [COMPANY NAME], [DPO EMAIL], [PROCESSOR NAME], [DATE]
- Do not leave generic placeholder language in the final draft — all positions must be filled
  or explicitly marked for the user to complete

---

### Step 6: Compliance Verification

Before delivery, run the structured verification in this order. Classify each check as
**COMPLIANT**, **PARTIAL**, or **NON-COMPLIANT** using the classification system below.

#### 6a. Art. 13/14 Mandatory Disclosures Checklist

Run each item against the drafted notice. Every item must be present or explicitly not
applicable with documented reason.

**Art. 13 checklist (data collected directly from data subject):**

| #   | Disclosure Required                                                                                                        | Status | Notes |
| --- | -------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| 1   | Controller identity and contact details                                                                                    |        |       |
| 2   | DPO contact details (if appointed)                                                                                         |        |       |
| 3   | Processing purposes for each activity                                                                                      |        |       |
| 4   | Legal basis for each processing activity                                                                                   |        |       |
| 5   | Legitimate interests pursued (if Art. 6(1)(f))                                                                             |        |       |
| 6   | Recipients or categories of recipients                                                                                     |        |       |
| 7   | International transfer + safeguards (if applicable)                                                                        |        |       |
| 8   | Retention period or criteria to determine it                                                                               |        |       |
| 9   | Right of access (Art. 15)                                                                                                  |        |       |
| 10  | Right to rectification (Art. 16)                                                                                           |        |       |
| 11  | Right to erasure (Art. 17)                                                                                                 |        |       |
| 12  | Right to restriction (Art. 18)                                                                                             |        |       |
| 13  | Right to data portability (Art. 20, if consent or contract-based automated processing)                                     |        |       |
| 14  | Right to object (Art. 21) — **presented separately and prominently**                                                       |        |       |
| 15  | Right to withdraw consent (Art. 7(3), if consent-based processing)                                                         |        |       |
| 16  | Right to lodge complaint with supervisory authority + authority's identity and contact                                     |        |       |
| 17  | Whether provision of data is statutory/contractual + consequences of non-provision                                         |        |       |
| 18  | Existence of automated decision-making including profiling (Art. 22) + logic + significance + consequences (if applicable) |        |       |
| 19  | Art. 9(2) exception identified for any special category processing + dual legal basis                                      |        |       |
| 20  | Information about further processing if purpose changes                                                                    |        |       |

**Art. 14 additional items (data NOT collected directly from data subject):**

| #   | Disclosure Required                                                                           | Status | Notes |
| --- | --------------------------------------------------------------------------------------------- | ------ | ----- |
| A   | Categories of personal data concerned                                                         |        |       |
| B   | Source of the data (and whether publicly accessible)                                          |        |       |
| C   | Timing: provided within 1 month / at first communication / at first disclosure to third party |        |       |

#### 6b. Compliance Classification System

For each gap identified:

| Status            | Definition                                                                                                            | Action Required                                      |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **COMPLIANT**     | Disclosure fully present, correctly worded, legally adequate                                                          | None                                                 |
| **PARTIAL**       | Disclosure present but incomplete, vague, missing citation, or using incorrect legal basis                            | Draft corrective language; flag for review           |
| **NON-COMPLIANT** | Mandatory disclosure absent, or a fundamental error (wrong legal basis, prohibited basis, missing Art. 21 prominence) | Must fix before publication; assess enforcement risk |

#### 6c. Prioritization of Gaps

| Priority     | Criteria                                                                                                                                                                               | Examples                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **CRITICAL** | NON-COMPLIANT on a mandatory Art. 13/14 item; wrong or invalid legal basis; Art. 21 not prominently shown; no supervisory authority identified                                         | Missing legal basis for any processing activity; Art. 9 data processed without dual basis; no rights section |
| **HIGH**     | PARTIAL on a mandatory item; incomplete transfer mechanism; vague retention ("as long as necessary" without criteria); no Art. 22 disclosure when automated decision-making is present | Transfer mechanism named but transfer countries missing; retention in general terms only                     |
| **MEDIUM**   | PARTIAL on non-mandatory-but-recommended items; soft opt-in disclosure incomplete; children's section missing where service accessible to minors                                       | Cookie table present but lifespans missing; AI section describing system type but not logic/significance     |
| **LOW**      | Minor formulation improvements; plain-language opportunities; structural preferences; non-material completeness enhancements                                                           | Formal "Sie" vs. "Du" consistency; link anchors; table formatting                                            |

#### 6d. Member-State Verification

Cross-check the drafted notice against the member-state localization blocks:

- Supervisory authority name, address, and URL correct for controller's registered seat?
- Retention periods match jurisdiction-specific legal citations (not just generic defaults)?
- Standard wording blocks (Art. 21 objection, complaint right, controller intro) use validated
  jurisdiction language?
- Jurisdiction-specific requirements addressed (e.g., § 26 BDSG for DE employee/applicant;
  TDDDG § 25 for DE cookie consent; CNIL layered approach for FR)?

#### 6e. Consistency Checks

- [ ] Art. 21 right to object presented separately and prominently
- [ ] Correct supervisory authority named (matches controller's registered seat)
- [ ] DPO contact included if DPO appointed
- [ ] Cookie section matches actual cookie usage
- [ ] Retention periods specific — not "as long as necessary" without criteria
- [ ] Transfer mechanisms match actual processor locations (check current adequacy decisions)
- [ ] AI/automated decision-making addressed if applicable
- [ ] Children's data addressed if service accessible to minors
- [ ] Special category data: dual legal basis disclosed (Art. 6 + Art. 9(2))
- [ ] Language matches target jurisdiction
- [ ] No placeholder text remaining ([...], \_\_\_, TODO, [INSERT])
- [ ] "Last updated" date present
- [ ] Sections match the notice type's section map (no irrelevant, no missing)

---

### Step 7: Quality Verification

Before delivering, run the quality assurance framework:

1. Run **Citation Quality Gates** (5 gates) silently. Revise any failures before delivery.
2. For every **NON-COMPLIANT** gap, run the **3-pass Self-Interrogation**. Revise if any pass
   reveals a weakness.
3. Assign **Confidence Scores** to key legal claims.
4. Verify completeness: confirm all applicable Art. 13/14 items addressed.
5. Generate the **Glass Box Audit Trail** and append it to the output.

---

### Step 8: Deliver

Present the drafted/reviewed notice with:

1. The notice in the required format (Markdown by default; offer .docx via docx skill if needed)
2. A compliance gap summary classified by COMPLIANT / PARTIAL / NON-COMPLIANT
3. A prioritized list of issues (CRITICAL → HIGH → MEDIUM → LOW)
4. Open compliance actions (DPA gaps, DPIA recommendation if triggered)
5. A post-publication checklist (see template below)
6. The Glass Box Audit Trail

**Document formatting standards:**

- A4 page size (EU standard) if formatting as a document
- Numbered sections (1., 2., 3...) with TOC for documents > 3 pages
- Tables for purposes/bases/retention and cookie categories
- Art. 21 right to object visually separated and prominent
- Footer: company name, notice title, "Last updated: [DATE]", page numbers
- No internal references to this skill, regulatory guides, or drafting aids in the final text

**Delivery statement** (always include):

> **Important**: This draft has been prepared by an AI-assisted tool. It does not constitute
> legal advice. Before publishing, have the notice reviewed by a qualified data protection
> professional or legal counsel in the relevant jurisdiction. Verify that all processing
> activities, processors, and transfer mechanisms accurately reflect your current operations.

---

## Member-State Localization Reference

Load the relevant block(s) when drafting for a specific market. For multi-market services,
load all relevant blocks and note where requirements diverge.

### Germany (DE) — DSGVO + BDSG + TDDDG

| Aspect                               | Detail                                                                                                          |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Primary notice title**             | "Datenschutzerklärung" (not "Datenschutzrichtlinie")                                                            |
| **Salutation**                       | "Sie" (formal); "Du" only if brand consistently informal                                                        |
| **Supervisory authority**            | 18 SAs — reference the one for the controller's registered state (see table below)                              |
| **Accessibility**                    | Max 2 clicks from any page (BGH requirement)                                                                    |
| **Cookie/tracking law**              | TDDDG § 25 — consent for non-essential; reject must be as easy as accept (Planet49; BGH Cookie-Einwilligung II) |
| **Employee data**                    | § 26 BDSG as primary basis alongside Art. 6 DSGVO                                                               |
| **Special categories in employment** | § 26(3) BDSG + Art. 9(2)(b) DSGVO — church tax, disability, sick leave, union dues                              |
| **DPO threshold**                    | Art. 37 GDPR + **§ 38 BDSG**: mandatory if ≥ 20 persons constantly engaged in automated processing              |
| **Children's age**                   | 16 years (§ 2 Nr. 17 TDDDG)                                                                                     |
| **Tax retention**                    | 10 years (§ 147 AO); commercial records 6 years (§ 257 HGB)                                                     |
| **Applicant retention**              | 6 months post-rejection (AGG limitation period)                                                                 |
| **CCTV**                             | § 4 BDSG; separate notice at entrance; 48–72 hours retention                                                    |
| **Impressum**                        | Separate legal requirement; link alongside but legally distinct from the privacy notice                         |

**German supervisory authorities (selection by registered state):**

| State                                                  | Authority                                              |
| ------------------------------------------------------ | ------------------------------------------------------ |
| Baden-Württemberg                                      | LfDI Baden-Württemberg                                 |
| Bayern                                                 | BayLDA (private sector) / BayLfD (public sector)       |
| Berlin                                                 | Berliner Beauftragte für Datenschutz (BlnBDI)          |
| Hamburg                                                | Der Hamburgische Beauftragte für Datenschutz (HmbBfDI) |
| Hessen                                                 | HBDI                                                   |
| Nordrhein-Westfalen                                    | LDI NRW                                                |
| [all other states: see BfDI.bund.de for complete list] |                                                        |

**Standard DE wording blocks:**

Art. 21 WIDERSPRUCHSRECHT (mandatory separate section):

```
WIDERSPRUCHSRECHT

Sie haben das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit
gegen die Verarbeitung Sie betreffender personenbezogener Daten, die auf Grundlage von Art. 6
Abs. 1 lit. e oder f DSGVO erfolgt, Widerspruch einzulegen (Art. 21 Abs. 1 DSGVO).

Werden Ihre Daten zur Direktwerbung verarbeitet, haben Sie das Recht, jederzeit Widerspruch
gegen die Verarbeitung einzulegen; dies gilt auch für Profiling, soweit es mit solcher
Direktwerbung in Verbindung steht (Art. 21 Abs. 2 DSGVO).
```

Controller introduction:

```
Verantwortlich im Sinne der Datenschutz-Grundverordnung (DSGVO) ist:

[Firmenname]
[Rechtsform], eingetragen im Handelsregister [HRB-Nummer], [Amtsgericht]
[Straße, PLZ Ort]
Vertreten durch: [Geschäftsführer/Vorstand]
E-Mail: [E-Mail]
Telefon: [Telefon]
```

---

### France (FR) — RGPD + LIL + LCEN

| Aspect                       | Detail                                                                                                                                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary notice title**     | "Politique de confidentialité" or "Protection des données personnelles"                                                                              |
| **Salutation**               | "vous" (formal); CNIL recommends layered approach (summary + full text)                                                                              |
| **Supervisory authority**    | CNIL — 3 Place de Fontenoy, TSA 80715, 75334 Paris Cedex 07 — www.cnil.fr                                                                            |
| **Cookie/tracking law**      | CNIL Guidelines 2020 (Délibérations 2020-091 and 2020-092); 13-month max cookie lifespan; reject as easy as accept; cookie wall generally prohibited |
| **Connection logs**          | 1 year (Art. 6 II LCEN + Décret n°2011-219)                                                                                                          |
| **Prospecting B2C**          | Art. L.34-5 CPCE — soft opt-in for existing customers: similar products, opt-out at collection + every message                                       |
| **Health data hosting**      | HDS certification required for health data hosting providers (Art. L.1111-8 CSP)                                                                     |
| **Children's age**           | 15 years (Art. 45 LIL) — dual consent (child + parental authority) below 15                                                                          |
| **Tax/accounting retention** | 10 years (Art. L.123-22 Code de commerce); commercial contracts 5 years (Art. 2224 Code civil)                                                       |
| **Applicant retention**      | 2 years max (CNIL recommendation)                                                                                                                    |
| **CCTV**                     | 30 days max (Art. L.252-3 Code de la sécurité intérieure)                                                                                            |
| **Special religious data**   | France laïcité principle: collection generally prohibited except where legally required                                                              |
| **DPO threshold**            | Art. 37 GDPR (no additional FR threshold; CNIL recommends voluntary appointment)                                                                     |

Art. 21 DROIT D'OPPOSITION (mandatory separate section):

```
DROIT D'OPPOSITION

Vous pouvez vous opposer à tout moment au traitement de vos données personnelles fondé sur
l'intérêt légitime (article 6.1.f du RGPD), pour des raisons tenant à votre situation
particulière.

Si vos données personnelles sont traitées à des fins de prospection commerciale, vous pouvez
vous y opposer à tout moment et sans justification.
```

---

### Netherlands (NL) — UAVG

| Aspect                    | Detail                                                                                    |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Primary notice title**  | "Privacyverklaring" (Dutch); English acceptable for international services                |
| **Supervisory authority** | Autoriteit Persoonsgegevens (AP) — autoriteitpersoonsgegevens.nl                          |
| **Cookie/tracking law**   | Telecommunicatiewet Art. 11.7a — AP aggressive enforcement; no cookie walls (AP guidance) |
| **BSN (DigiD number)**    | Heavily restricted under Art. 46 UAVG — disclose if processed with strong legal basis     |
| **Children's age**        | 16 years (GDPR default)                                                                   |

---

### Austria (AT) — DSG

| Aspect                    | Detail                                                              |
| ------------------------- | ------------------------------------------------------------------- |
| **Primary notice title**  | "Datenschutzerklärung"                                              |
| **Supervisory authority** | Datenschutzbehörde (DSB) — dsb.gv.at — Barichgasse 40-42, 1030 Wien |
| **Cookie/tracking law**   | § 165 TKG 2021 (Telekommunikationsgesetz)                           |
| **Children's age**        | 14 years (§ 4(4) DSG)                                               |
| **Criminal data**         | Only by official authority or under official supervision            |
| **Tax retention**         | 7 years (§ 132 BAO)                                                 |

---

### Italy (IT) — Codice Privacy

| Aspect                         | Detail                                                                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| **Primary notice title**       | "Informativa sulla privacy" or "Informativa sul trattamento dei dati personali"           |
| **Supervisory authority**      | Garante per la protezione dei dati personali — garanteprivacy.it                          |
| **Cookie/tracking law**        | Garante Cookie Guidelines June 2021 (updated 2022); consent required for non-essential    |
| **Children's age**             | 14 years (Art. 2-quinquies D.lgs. 196/2003)                                               |
| **Marketing**                  | Opt-in for email marketing (Art. 130 D.lgs. 196/2003); soft opt-in for existing customers |
| **Tax retention**              | 10 years (Art. 2220 Codice Civile)                                                        |
| **Public interest processing** | Art. 2-ter: requires specific legal basis in national law                                 |

---

### Spain (ES) — LOPDGDD

| Aspect                      | Detail                                                                                    |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| **Primary notice title**    | "Política de privacidad"                                                                  |
| **Supervisory authority**   | AEPD (national) — aepd.es; regional: APDCAT (Catalonia), AVPD (Basque), CTPDA (Andalusia) |
| **Cookie/tracking law**     | LSSI Art. 22; AEPD cookie guide                                                           |
| **Children's age**          | 14 years (Art. 7 LOPDGDD)                                                                 |
| **Employee digital rights** | Art. 12 LOPDGDD: right to digital disconnection (disconnexion numérica)                   |
| **Whistleblower channels**  | Specific data processing regime under Ley 2/2023                                          |
| **Tax retention**           | 4 years (Ley General Tributaria Art. 66); 6 years accounting (Código de Comercio Art. 30) |
| **Regional languages**      | Consider Catalan, Basque, Galician for regional markets                                   |

---

### Belgium (BE) — Loi du 30 juillet 2018

| Aspect                    | Detail                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| **Primary notice title**  | "Politique de confidentialité" (FR) / "Privacyverklaring" (NL) / "Datenschutzerklärung" (DE) |
| **Supervisory authority** | APD/GBA — autoriteprotectiondonnees.be / gegevensbeschermingsautoriteit.be                   |
| **Languages**             | French AND/OR Dutch AND/OR German depending on regional target audience                      |
| **Children's age**        | 13 years (Art. 7)                                                                            |
| **Direct marketing**      | Code of Economic Law provisions apply alongside GDPR                                         |

---

### Ireland (IE) — Data Protection Act 2018

| Aspect                    | Detail                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Primary notice title**  | "Privacy Notice" or "Privacy Policy"                                                           |
| **Supervisory authority** | Data Protection Commission (DPC) — dataprotection.ie — Lead SA for many US tech multinationals |
| **Cookie/tracking law**   | SI 336/2011 (ePrivacy transposition)                                                           |
| **Children's age**        | 16 years (Sec. 31 DPA 2018)                                                                    |
| **Children's code**       | DPC Fundamentals for a Child-Oriented Approach — if service accessible to children             |

---

### Poland (PL) — UODO Act

| Aspect                    | Detail                                                            |
| ------------------------- | ----------------------------------------------------------------- |
| **Primary notice title**  | "Polityka prywatności" or "Klauzula informacyjna"                 |
| **Supervisory authority** | Urząd Ochrony Danych Osobowych (UODO) — uodo.gov.pl               |
| **Children's age**        | 16 years (GDPR default)                                           |
| **Tax retention**         | 5 years (Ordynacja podatkowa); accounting records 5 years minimum |

---

### Sweden (SE) — Dataskyddslag (2018:218)

| Aspect                      | Detail                                                   |
| --------------------------- | -------------------------------------------------------- |
| **Primary notice title**    | "Integritetspolicy" or "Dataskyddsmeddelande"            |
| **Supervisory authority**   | Integritetsskyddsmyndigheten (IMY) — imy.se              |
| **Children's age**          | 13 years (2 § Kompletteringslagen)                       |
| **Sensitive employer data** | IMY guidance on employee monitoring and trade union data |

---

### Denmark (DK) — Databeskyttelsesloven

| Aspect                    | Detail                                       |
| ------------------------- | -------------------------------------------- |
| **Primary notice title**  | "Privatlivspolitik" or "Persondataoplysning" |
| **Supervisory authority** | Datatilsynet — datatilsynet.dk               |
| **Children's age**        | 13 years (§ 6 Databeskyttelsesloven)         |

---

### Finland (FI) — Tietosuojalaki

| Aspect                    | Detail                                      |
| ------------------------- | ------------------------------------------- |
| **Primary notice title**  | "Tietosuojaseloste" or "Tietosuojakäytäntö" |
| **Supervisory authority** | Tietosuojavaltuutettu (TSV) — tietosuoja.fi |
| **Children's age**        | 13 years (§ 5 Tietosuojalaki)               |

---

### Other EU/EEA Member States

For other member states not detailed above, apply the GDPR defaults and research:

1. National implementing law for Art. 88 (employment) and Art. 8 (children's age)
2. National supervisory authority name and contact (mandatory in the notice)
3. National ePrivacy implementing law for cookies
4. Specific retention obligations under national tax/commercial law

**Key national supervisory authorities (additional):**

| Country             | Authority    | Website               |
| ------------------- | ------------ | --------------------- |
| Czech Republic      | ÚOOÚ         | uoou.cz               |
| Hungary             | NAIH         | naih.hu               |
| Romania             | ANSPDCP      | dataprotection.ro     |
| Portugal            | CNPD         | cnpd.pt               |
| Greece              | HDPA         | dpa.gr                |
| Bulgaria            | CPDP         | cpdp.bg               |
| Croatia             | AZOP         | azop.hr               |
| Slovakia            | ÚOOÚ SR      | dataprotection.gov.sk |
| Slovenia            | IP RS        | ip-rs.si              |
| Estonia             | AKI          | aki.ee                |
| Latvia              | DVI          | dvi.gov.lv            |
| Lithuania           | VDAI         | ada.lt                |
| Luxembourg          | CNPD         | cnpd.lu               |
| Malta               | IDPC         | idpc.org.mt           |
| Cyprus              | CPDC         | dataprotection.gov.cy |
| Norway (EEA)        | Datatilsynet | datatilsynet.no       |
| Iceland (EEA)       | Personuvernd | personuvernd.is       |
| Liechtenstein (EEA) | DSS          | llv.li                |

---

## Retention Matrix

Use these jurisdiction-specific defaults. Always cross-check with the controller's actual
legal obligations and document the legal citation in the notice.

| Data Category                 | DE (default)                           | FR (default)                     | IT (default)             | ES (default)                | General EU fallback                     |
| ----------------------------- | -------------------------------------- | -------------------------------- | ------------------------ | --------------------------- | --------------------------------------- |
| Commercial correspondence     | 6 years (§ 257 HGB)                    | 5 years (Art. 2224 CC)           | 10 years (Art. 2220 CC)  | 6 years (CComercio Art. 30) | Duration of relationship + 3 years      |
| Invoices / tax records        | 10 years (§ 147 AO)                    | 10 years (Art. L.123-22)         | 10 years                 | 4 years (LGT Art. 66)       | Check national tax law                  |
| Active customer / account     | Duration of relationship               | Duration of relationship         | Duration of relationship | Duration of relationship    | Duration of relationship                |
| Inactive customer (marketing) | 3 years without interaction            | 3 years (CNIL rec.)              | —                        | —                           | 3 years without interaction             |
| Applicant (rejected)          | 6 months (AGG)                         | 2 years max (CNIL)               | —                        | —                           | 6 months–2 years [VERIFY]               |
| Employee data                 | Employment + 3 years (§§ 195, 199 BGB) | Employment + 5 years (L.3243-4)  | —                        | —                           | Employment + limitation period          |
| Payroll records               | 6 years (§ 257 HGB)                    | 5 years (L.3243-4)               | 10 years                 | —                           | Check national law                      |
| Server / access logs          | 7–30 days (Art. 6(1)(f))               | 1 year (LCEN)                    | —                        | —                           | 7–30 days (proportionate)               |
| Cookie consent proof          | 3 years (Art. 7(1) DSGVO)              | 6 years (Art. 2224 CC)           | —                        | —                           | Duration of processing + limitation     |
| CCTV footage                  | 48–72 hours (§ 4 BDSG)                 | 30 days max (L.252-3)            | 24–48 hours (Garante)    | —                           | Shortest defensible period              |
| KYC / AML records             | 5 years (GwG § 8)                      | 5 years (Art. L.561-12 CMF)      | 10 years                 | 10 years                    | 5 years minimum                         |
| Medical records               | —                                      | 20 years (R.1112-7 CSP)          | —                        | —                           | Per national healthcare law             |
| Contract data                 | Duration + 3 years (§§ 195, 199 BGB)   | 5 years after end (Art. 2224 CC) | —                        | —                           | Duration + applicable limitation period |

---

## Data Subject Rights Reference

| Right                                  | Article   | Key Conditions                                              | Response Time           | Common Limits                                              |
| -------------------------------------- | --------- | ----------------------------------------------------------- | ----------------------- | ---------------------------------------------------------- |
| **Access**                             | Art. 15   | Free first copy; charge for manifestly excessive            | 1 month (extendable +2) | National security, third-party rights                      |
| **Rectification**                      | Art. 16   | Inaccurate or incomplete data                               | 1 month                 | —                                                          |
| **Erasure ("right to be forgotten")**  | Art. 17   | When consent withdrawn; no longer necessary; unlawful; etc. | 1 month                 | Legal obligation; public interest; legal claims; archiving |
| **Restriction**                        | Art. 18   | Accuracy contested; unlawful processing; claims             | 1 month                 | —                                                          |
| **Data portability**                   | Art. 20   | Only consent or contract-based **automated** processing     | 1 month                 | Not applicable to LI or legal obligation bases             |
| **Object**                             | Art. 21   | LI: compelling grounds; direct marketing: **absolute**      | 1 month                 | Direct marketing objection is absolute                     |
| **Not subject to automated decisions** | Art. 22   | Legal/significant effects from solely automated processing  | 1 month                 | Contract, law, explicit consent (with safeguards)          |
| **Withdraw consent**                   | Art. 7(3) | At any time; as easy as giving consent                      | Without undue delay     | Does not affect prior lawfulness                           |

**Rights exercise procedure to include in notice:**

- Dedicated privacy contact email (e.g., privacy@..., datenschutz@..., dpo@...)
- Postal address
- Identity verification method (must be proportionate — no excessive ID requests)
- Timeline: 1 month; extendable by 2 months for complex/numerous requests
- Free of charge (except manifestly unfounded or excessive)
- How to escalate to the supervisory authority (linked to Art. 77 complaint right)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                               | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific GDPR article, national law provision, EDPB guideline, or established regulatory principle                                                       | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent format (e.g., "Art. 6(1)(b) GDPR", "§ 26 Abs. 1 BDSG", "Délibération CNIL n°2020-091")                                                           | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, repeal, or new EDPB guidance — particularly adequacy decisions (DPF status), national implementing laws, and cookie guidance updates | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the stated jurisdiction. No cross-contamination of DE law into an FR notice or US privacy concepts into EU analysis                                          | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated. If a legal position is contested, uncertain, or jurisdiction-dependent, say so                                                                      | Add confidence qualifier or [VERIFY]                     |

### Self-Interrogation for NON-COMPLIANT Gaps

For any gap classified as NON-COMPLIANT, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the compliance gap follow logically from the cited
GDPR article or national provision? Would the relevant supervisory authority actually cite
this as a violation? Is there a counter-argument that the current wording satisfies the
requirement?

**Pass 2 — Completeness**: Have all relevant GDPR articles, EDPB guidelines, and national
laws been considered? Are there sector-specific rules (health, finance, employment) that
affect this gap? Is the identified fix actually the required fix, or just one possible fix?

**Pass 3 — Challenge**: What is the strongest argument that the current notice language is
adequate? Under what supervisory interpretation might this be accepted? Is the
NON-COMPLIANT classification proportionate, or is this actually PARTIAL?

Record: `self_interrogation: PASS` or `self_interrogation: REVISED` in the Glass Box.

### Confidence Scoring

| Level        | Range     | Meaning                                                          | Action                                               |
| ------------ | --------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled GDPR text, clear EDPB guidance, unambiguous national law | State with confidence                                |
| **High**     | 0.80-0.94 | Strong authority with minor interpretation questions             | State with brief caveat                              |
| **Probable** | 0.60-0.79 | Good arguments, but SA/national court interpretation may differ  | State with reasoning and contra-indicators           |
| **Possible** | 0.40-0.59 | Genuinely uncertain — contested by SAs or no direct authority    | Flag for expert review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                          | Do not assert; flag "[UNCERTAIN — expert to advise]" |

---

## Glass Box Audit Trail

Every privacy notice output MUST include a Glass Box audit section. Append at the end of
the compliance gap report (not in the published notice itself).

```yaml
glass_box:
  skill: "legalcode-eu-privacy-notice-drafter"
  mode: "[Draft / Review / Update]"
  notice_type: "[Website/App / Applicant / Employee / B2B / B2C / Combined]"
  controller: "[Company name — not legal name needed, just identifier]"
  jurisdiction: "[Member State(s) and principal establishment]"
  language: "[Language(s) of notice]"
  art_1314: "[Art. 13 / Art. 14 / Both]"
  gdpr_articles_applied:
    - "Art. 6(1) — lawful bases applied: [(a) consent / (b) contract / (c) legal obligation / (f) LI]"
    - "Art. 9 — special categories: [yes/no — categories if yes]"
    - "Art. 13/14 — transparency disclosure"
    - "Art. 17 — erasure conditions disclosed"
    - "Art. 21 — right to object prominently placed: [yes/no]"
    - "Art. 22 — automated decision-making: [applicable/not applicable/PARTIAL]"
    - "Art. 26 — joint controllership: [applicable/not applicable]"
    - "Art. 28 — processor DPA gaps identified: [yes/no — number if yes]"
    - "Art. 35 — DPIA indicators: [count — mandatory/recommended/not required]"
    - "Art. 37 — DPO: [appointed/not appointed]"
  national_law_applied: "[§ 26 BDSG / LIL / UAVG / etc. as applicable]"
  localization_blocks_loaded: "[DE / FR / NL / AT / IT / ES / etc.]"
  supervisory_authority_correct: "[yes / VERIFY]"
  transfers_disclosed: "[none / [countries] with [mechanisms]]"
  legalcode_mcp: "Connected / Not connected"
  mandatory_disclosures_checked: "[X/20 items COMPLIANT]"
  gaps_identified:
    critical: "[count]"
    high: "[count]"
    medium: "[count]"
    low: "[count]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  citations_verified: "[number VERIFIED via legalcode-mcp or authoritative source] / [number UNVERIFIED — marked [VERIFY]]"
  dpa_gaps: "[none / list of processors without confirmed DPA]"
  dpia_required: "[yes / no / RECOMMEND — based on indicator count]"
  ai_act_applicable: "[yes / no / check — AI Act Art. 50 effective date for this provision]"
  limitations:
    - "[Any scope limitations, assumptions, or processing activities not reviewed]"
    - "Transfer mechanism currency: adequacy decisions and DPF certifications must be verified at time of publication"
    - "AI Act applicability: verify current effective dates for specific AI Act provisions"
  reviewer: "AI-assisted — requires qualified data protection counsel review before publication"
```

---

## Anti-Patterns

What NOT to do when drafting or reviewing GDPR privacy notices:

1. **"As long as necessary" retention without criteria** — Retention language like "we keep
   your data as long as needed for the stated purpose" does not satisfy Art. 13(2)(a). Provide
   specific periods with legal basis for each data category, or articulate the specific
   criteria used to determine the period. Vague language has been cited in enforcement actions.

2. **Using "legitimate interest" as a default basis for everything** — Art. 6(1)(f) requires
   a genuine balancing test (LIA). Controllers that apply LI to marketing, analytics, profiling,
   employee monitoring, and analytics indiscriminately expose themselves to enforcement.
   Document the LIA separately; the notice should state the result, not assume it's fine.

3. **Burying the right to object** — Art. 21(4) GDPR explicitly requires that the right to
   object for LI-based processing and direct marketing be **presented at the latest at the time
   of first communication**, clearly, separately, and in plain language. Putting it in a rights
   table alongside 6 other rights, in small print, does not satisfy this requirement. Multiple
   SA enforcement actions have cited this failure (including Meta €1.2B by DPC, Amazon Ireland
   enforcement, Criteo €40M by CNIL).

4. **Failing to identify the correct supervisory authority** — The notice must name the
   supervisory authority at the controller's principal establishment (for one-stop-shop) or
   registered seat. Naming a generic "data protection authority" or the wrong authority
   (e.g., Irish DPC for a company registered in Germany) is NON-COMPLIANT.

5. **Cookie consent without genuine rejection option** — Presenting "Accept All" prominently
   and making rejection require multiple clicks, a separate page, or individual toggles is a
   dark pattern. CNIL, APD, AP, and Garante have each issued significant fines for this. The
   reject option must be as easy as the accept option.

6. **No legal basis for analytics cookies** — Server-side analytics without cookies may
   operate on legitimate interest (with a proper LIA), but client-side analytics cookies
   require consent under ePrivacy national laws in every EU member state. GA4, Meta Pixel,
   and HubSpot tracking require consent — they are not "strictly necessary."

7. **Disclosing processor names but missing transfer mechanisms** — Naming "Google LLC,
   OpenAI, Stripe" as processors without disclosing that they are based in the USA and the
   applicable transfer mechanism (DPF, SCCs, etc.) leaves a NON-COMPLIANT gap. The notice
   must identify the destination country AND the mechanism (Art. 13(1)(f)).

8. **Using consent as the legal basis for employment data** — In employment contexts,
   consent is rarely a valid basis because it is not freely given (power imbalance). Using
   Art. 6(1)(a) for routine employee data processing (payroll, HR, performance reviews) is
   EDPB-criticized and likely invalid. Use Art. 6(1)(b), (c), or national employment law
   derogations (§ 26 BDSG for DE).

9. **Omitting the Art. 9 dual-basis requirement** — Processing special category data (health,
   biometric, religion, trade union, etc.) requires citing BOTH an Art. 6 legal basis AND an
   Art. 9(2) exception. A notice that says "we process health data for legal compliance" without
   citing both Art. 6(1)(c) AND Art. 9(2)(b) is PARTIAL at best, NON-COMPLIANT for any
   enforcement-focused SA review.

10. **Generic data subject rights with no exercise procedure** — A notice that lists the
    rights (access, rectification, erasure, etc.) without explaining how to exercise them —
    contact details, identity verification method, response timeline — is PARTIAL under
    Art. 12 and Art. 13(2)(b). Provide a dedicated privacy contact and the specific process.

11. **Failing to disclose automated decision-making when Art. 22 is triggered** — A notice
    for a service that uses AI for credit scoring, insurance pricing, employment screening, or
    content moderation without an Art. 22 disclosure (existence, logic, significance, consequences,
    right to human review) is NON-COMPLIANT. The triggering threshold is "legal or similarly
    significant effects" — interpret broadly.

12. **Publishing a notice before conducting a required DPIA** — A DPIA (Art. 35) must be
    conducted before processing begins, not after the notice is published. Publishing a notice
    that references high-risk processing without a DPIA is a process failure, not just a
    documentation gap. The notice should reference that a DPIA was conducted if applicable.

13. **Relying on an expired adequacy decision or uncertified DPF** — The EU-U.S. DPF replaced
    the Privacy Shield. However, DPF certifications can lapse, and the adequacy decision itself
    could be challenged (as Privacy Shield was in Schrems II). Always verify at the time of
    publication that the named processor is currently DPF-certified and that the adequacy
    decision is in effect. Mark transfer mechanism currency checks in the Glass Box.

14. **Placeholder text in published notice** — "[INSERT COMPANY NAME]", "[ADD RETENTION
    PERIOD]", "[DPO CONTACT TO FOLLOW]" in a published notice is a visible compliance failure
    and makes the notice legally inadequate. Every placeholder must be resolved before
    publication.

15. **Layered notices without ensuring each layer is complete** — A short summary notice that
    references a full notice is acceptable, but only if the full notice is equally accessible
    and contains ALL mandatory Art. 13/14 disclosures. A summary-only notice where the full
    text is difficult to find does not satisfy the Art. 12 accessibility requirement.

16. **Failing to cover combined-notice audiences completely** — When drafting a single notice
    for multiple audiences (website visitors + applicants + employees), ensure each audience's
    mandatory disclosures are present. An employment-law disclosure in a website notice but
    missing from the employee-facing section is a gap. Section 6d verification must cover each
    audience separately.

17. **Not updating the notice when processing changes** — A notice published at launch that
    is never updated despite adding new processors, purposes, tools, or transfer mechanisms is
    out-of-date and potentially misleading. The notice must reflect actual current processing.
    Include an "ongoing review triggers" recommendation in the delivery.

18. **Misidentifying joint controllers as processors** — If two organizations jointly determine
    purposes and means of processing, they are joint controllers (Art. 26), not controller and
    processor. The notice must reflect this and disclose the essence of the Art. 26 arrangement.
    Misclassification also affects which contract (Art. 26 agreement vs. Art. 28 DPA) is needed.

19. **Over-disclosing in the notice** — The notice should disclose what data subjects need to
    know, not the controller's entire technical architecture. Do not include: DPA sub-processor
    lists, technical/organizational security measures in detail, SLA terms, pricing information,
    or internal processing documentation. Including these creates maintenance burdens and may
    reveal information that should stay internal.

20. **Assuming the EU AI Act is not yet relevant** — EU AI Act Art. 50 transparency obligations
    for AI systems have phased applicability from August 2025. By the time most notices are
    published in 2025-2026, the general-purpose AI and limited-risk transparency requirements
    may already be in effect. Do not exclude AI disclosures on the assumption that the Act is
    not yet applicable — verify the current effective date for the relevant provision. [VERIFY
    current AI Act implementation status]

---

## Writing Standards

Apply plain-language discipline to all notice drafts.

**Tone and address:**

- Write to the data subject: "We collect your name and email address" — not "The controller
  processes the data subject's name and email address"
- Use "you" / "your" / "Sie" / "Ihre" / "vous" / "vos" consistently throughout
- Match the formality level to the controller's brand voice and audience, but never sacrifice
  clarity for style

**Structural discipline:**

- Numbered sections with descriptive headings
- Tables for purposes/bases/retention — tables are more readable and auditable than paragraph text
- Tables for cookies — name, category, provider, purpose, lifespan
- Bullet points for lists of rights or data categories
- Art. 21 right to object: always a visually separate section, not buried in a table

**Legal precision:**

- Cite article numbers precisely ("Art. 6(1)(f) GDPR" not "legitimate interest")
- Cite national law alongside GDPR where both apply ("Art. 6(1)(c) GDPR + § 26 Abs. 1 BDSG")
- Specific retention periods with legal citation ("6 years — § 257 HGB")
- Specific transfer mechanisms ("EU-U.S. Data Privacy Framework — EU Commission Adequacy
  Decision of 10 July 2023")

**Plain language:**

- Short sentences. One idea per sentence.
- Active voice: "We use your data to..." not "Your data is used for..."
- Explain technical terms: first use → define: "cookies (small text files stored on your device)"
- No legalese without explanation: if "legitimate interest" is cited, briefly explain what it means
  to the reader

**Quality gates before delivery:**

1. Can a non-specialist reader (the intended data subject) understand every section?
2. Is the Art. 21 right to object clearly separated and prominent?
3. Does every processing activity have a stated legal basis and retention period?
4. Is every international transfer disclosed with destination country and mechanism?
5. Are all mandatory Art. 13/14 items present?
6. Is there any placeholder text still in the draft?
7. Is the supervisory authority correctly identified for this controller?

---

## Post-Publication Checklist

Deliver this checklist to the user alongside the notice draft:

**Legal review before publication:**

- [ ] Privacy notice reviewed by a qualified DPO or data protection counsel
- [ ] All legal bases confirmed as appropriate for the specific processing activities
- [ ] Retention periods verified against current legal obligations
- [ ] Transfer mechanisms confirmed as current (DPF certifications, SCC versions, adequacy decisions)
- [ ] Art. 9 special category processing: dual legal basis and safeguards reviewed
- [ ] DPAs in place for all identified processors (Art. 28 obligation — separate from the notice)
- [ ] DPIA conducted if required (Art. 35 — separate from the notice)

**Technical review:**

- [ ] All processors and tools listed are actually in current use (no outdated entries)
- [ ] Cookie table matches actual cookies set — audit with browser developer tools
- [ ] Contact details (privacy email, postal, DPO) are monitored and accurate
- [ ] Transfer mechanisms verified against actual hosting/processor locations

**Publication requirements:**

- [ ] Notice accessible within 2 clicks from any page (DE: BGH requirement)
- [ ] Linked in website footer / app settings / onboarding flow as appropriate
- [ ] Previous version archived with effective date (for audit trail)
- [ ] Cookie banner/CMP updated to reference the current privacy notice
- [ ] Employees/applicants notified of updated notice if applicable (Art. 14 timing requirements)

**Ongoing review triggers — review the notice when:**

- New processors, tools, or integrations are introduced
- New processing purposes are added
- Legal framework changes (adequacy decisions, court rulings, EDPB guidance)
- Company undergoes merger, acquisition, or restructuring
- A data breach reveals undisclosed processing
- Minimum: **annual review**

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for EDPB guidelines, national SA guidance, and current GDPR enforcement decisions
  relevant to the controller's industry and member state
- Verify current adequacy decisions and DPF certification status
- Retrieve current national law provisions for the applicable member states
- Save key findings to `/tmp/legalcode-privacy-notice-research.md` for reference during drafting
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory citations, EDPB guidance references, and SA enforcement examples with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus on GDPR article text (which is reliable from training data) and flag national law
  references, retention defaults, and SA-specific guidance as requiring verification
- Particularly flag: DPF certification status, current adequacy decisions, AI Act effective dates

---

## Output Format Template

Every draft or review output follows this structure:

```markdown
# Privacy Notice — [Controller Name]

**Notice type**: [Website/App / Applicant / Employee / B2B / B2C / Combined]
**Jurisdiction(s)**: [Member State(s)]
**Language**: [Language(s); governing version if bilingual]
**Prepared by**: Legalcode EU Privacy Notice Drafter (AI-assisted)
**Date**: [DATE]
**Status**: DRAFT — requires legal review before publication

---

[NOTICE CONTENT — see Section 5 drafting rules]

---

## Compliance Gap Summary

| Item                                          | Status                              | Priority                       | Notes    |
| --------------------------------------------- | ----------------------------------- | ------------------------------ | -------- |
| Controller identity + DPO (Art. 13(1)(a)+(b)) | COMPLIANT / PARTIAL / NON-COMPLIANT | CRITICAL / HIGH / MEDIUM / LOW | [detail] |
| Purposes + legal bases (Art. 13(1)(c)+(d))    | ...                                 | ...                            | ...      |
| [... all 20 Art. 13/14 items ...]             |                                     |                                |          |

**Summary:**

- COMPLIANT: X/20 mandatory disclosures
- PARTIAL: X items → [list]
- NON-COMPLIANT: X items → [list]

## Priority Action List

### CRITICAL (must fix before publication)

1. [Gap + corrective action]

### HIGH (fix before publication, assess enforcement risk)

1. [Gap + corrective action]

### MEDIUM (address in next revision cycle)

1. [Gap + suggested improvement]

### LOW (nice-to-have improvements)

1. [Suggestion]

## Open Compliance Actions (Separate from Notice)

- [ ] DPA required for: [processor list where not confirmed]
- [ ] DPIA recommended / required for: [processing activities]

## Glass Box Audit Trail

[YAML as per template above]
```

---

## Localization Notes

This skill covers all 27 EU member states and the 3 EEA states. For jurisdictions not
detailed in the localization reference above, apply GDPR defaults and use legalcode-mcp to
research:

- National supplementary law (Art. 88 employment derogation, Art. 85 journalism/research, etc.)
- National supervisory authority name and contact details
- National ePrivacy implementing law for cookie/tracking consent
- National tax and commercial law retention periods
- Any national mandatory DPIA list items

**EEA specifics (Norway, Iceland, Liechtenstein)**: GDPR applies via the EEA Agreement.
National supplementary laws differ from EU member state laws. Norway's Personopplysningsloven,
Iceland's Persónuverndarlög, and Liechtenstein's Datenschutzgesetz each have national specifics —
research via legalcode-mcp or [VERIFY] flag applicable national provisions.

**UK GDPR**: UK diverged from EU GDPR post-Brexit. UK GDPR + DPA 2018 apply for UK
controllers and UK-established services. UK transfer mechanisms differ (UK IDTA, UK Addendum
to EU SCCs). The UK adequacy decision for EU→UK transfers should be verified for current
status (valid as of training data but subject to review). [VERIFY current UK adequacy status]
This skill covers UK as a localization note only — for UK-primary work, use a UK-focused skill.

---

## Provenance

Created by Legalcode — 2026-03-22. Legalcode original synthesis. Mode A creation.

Based on: deep research of GDPR Arts. 12–14, 22, 26, 28, 35, 37, 46–49; EU AI Act Regulation
(EU) 2024/1689 Arts. 50, 86; EDPB Guidelines 3/2019 (transparency), 05/2020 (consent), 2/2019
(Art. 6(1)(b)), 1/2024 (legitimate interest), 07/2020 (processors), 8/2020 (special categories);
Planet49 (C-673/17) [VERIFY]; national laws: BDSG 2018, TDDDG, UWG § 7, HGB, AO (DE); LIL,
LCEN, CPCE (FR); UAVG (NL); DSG (AT); D.lgs. 196/2003 (IT); LOPDGDD (ES); Loi 30 juillet 2018
(BE); DPA 2018 (IE); Databeskyttelsesloven (DK); Tietosuojalaki (FI); Dataskyddslag (SE);
repository reference skills: `imported-lawvable-gdpr-privacy-notice` (superseded by this skill),
`legalcode-contract-review` (quality framework patterns), `legalcode-dpa-review-and-negotiation`
(Art. 28 interface patterns), `legalcode-dpia-generator` (Art. 35 patterns),
`legalcode-legitimate-interest-assessment` (Art. 6(1)(f) patterns),
`legalcode-cross-border-transfer-assessment` (Chapter V patterns).

This skill supersedes `imported-lawvable-gdpr-privacy-notice` as a native Legalcode replacement
with Legalcode quality framework, expanded member-state coverage, COMPLIANT/PARTIAL/NON-COMPLIANT
classification, Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box audit
trail, 20 anti-patterns, and post-publication checklist.
