---
name: legalcode-breach-affected-party-communication
description: 'Drafts and reviews the complete suite of breach communications directed at affected individuals
  and the public following a confirmed personal data breach: individual notification letters with jurisdiction-specific
  mandatory content, timing, and credit monitoring offers; FAQ documents for breach response webpages;
  call center scripts; media statements; and follow-up / supplementary notifications. Use when you need
  to draft, review, or improve any communication sent to data breach victims — not regulatory filings
  (use legalcode-breach-regulatory-notification-drafter for those).'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts and reviews the complete suite of breach communications directed at affected individuals and the public following a confirmed personal data breach: individual notification letters with jurisdiction-specific mandatory content, timing, and credit monitoring offers; FAQ documents for breach response webpages; call center scripts; media statements; and follow-up / supplementary notifications. Use when you need to draft, review, or improve any communication sent to data breach victims — not regulatory filings (use legalcode-breach-regulatory-notification-drafter for those). Covers GDPR Art. 34 "high risk" individual notifications, US state breach notification letters (California SB 446 mandatory format with 30-day deadline, New York SHIELD Act 30-day requirement, Massachusetts 18-month credit monitoring, Texas 30-day deadline, HIPAA individual notification at 45 CFR §164.404), UK GDPR / ICO-compliant notices, and Australian Privacy Act 1988 Part IIIC NDB individual notifications (Privacy and Other Legislation Amendment Act 2024). Triggers on: "draft individual breach notice", "write breach notification letter", "create breach FAQ", "call center script for data breach", "media statement for breach", "draft breach communication", "notify affected users of breach", "data breach communication suite", "credit monitoring offer in breach letter", "follow-up after breach notice", "substituted notice", "HIPAA individual notification", "review breach letter", "breach notification plain language", "what must I tell affected individuals". Jurisdiction-agnostic wrapper with full EU/UK/US/AU localization. Downstream from legalcode-breach-response-checklist and legalcode-breach-regulatory-notification-drafter in the Legalcode breach skill family.


# Legalcode Breach Affected-Party Communication

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of data breach
> communications to affected individuals. It does not constitute legal advice. All draft
> communications must be reviewed by qualified legal counsel licensed in the relevant
> jurisdiction(s) before sending to any individual. Legal requirements for breach
> notifications change frequently — California SB 446 (30-day deadline, effective
> January 2026), New York's 2024 amendment (30-day deadline, expanded private information
> definition effective March 2025), and Australia's Privacy and Other Legislation Amendment
> Act 2024 (December 2024) are recent examples. All statutory citations in this skill
> carry hallucination risk; verify against authoritative sources before relying on them.
> Sending a deficient, late, or misleading notification can trigger regulatory enforcement,
> class action litigation, and significant reputational harm.

---

## Purpose and Scope

This skill drafts and reviews the complete suite of breach communications directed at
**affected individuals and the public** following a confirmed personal data breach. It
covers every document that individuals, the press, or the public actually receive — as
distinct from the regulatory filings sent to data protection authorities and attorneys
general.

**Covers:**

- Individual notification letters with jurisdiction-specific mandatory content (GDPR
  Art. 34, US state laws including California SB 446 mandatory 5-heading format,
  Massachusetts 18-month credit monitoring, UK GDPR, Australia NDB)
- Frequently Asked Questions (FAQ) documents for breach response webpages
- Call center scripts for dedicated breach response support lines
- Media statements and press releases
- Substituted notice language when direct individual contact is not practicable
- Supplementary / follow-up notifications when new information emerges
- Credit monitoring offer language and enrollment instructions (jurisdiction-mapped)
- Communication quality review — assessing draft notices against legal and regulatory
  standards
- Timing and sequencing guidance (sequencing individual notices vs. media; multi-jurisdiction
  orchestration; Australia OAIC-first rule)
- Special population handling (minors, domestic violence victims, HIPAA patients,
  limited-English-proficiency individuals)

**Does not:**

- Draft regulatory / authority notifications (DPA, AG, OAIC, HHS) — use
  `legalcode-breach-regulatory-notification-drafter`
- Determine whether a breach is notifiable — use `legalcode-breach-severity-assessment`
- Map all US state deadlines comprehensively — use `legalcode-us-breach-notification-triage`
- Perform forensic root-cause analysis of the breach
- Provide legal advice or replace qualified counsel
- Guarantee regulatory outcome or litigation immunity

**When to use this skill:**
Use after confirming (by severity assessment and/or legal counsel) that a breach is
notifiable and the affected population and data categories are known. Run
`legalcode-breach-response-checklist` first to establish what notifications are required
and by when.

---

## Position in the Legalcode Breach Skill Family

```
legalcode-breach-severity-assessment
  ↓  (is it notifiable? what is the risk level? what data? how many affected?)
legalcode-breach-response-checklist
  ↓  (what to do, to whom, by when — critical path with earliest-deadline-first sequencing)
legalcode-us-breach-notification-triage         [US incidents — parallel or prior]
  ↓  (maps all applicable US state obligations)
legalcode-breach-regulatory-notification-drafter
  ↓  (drafts submission-ready regulatory notices to DPAs, AGs, HHS, OAIC)
legalcode-breach-affected-party-communication  ← THIS SKILL
  ↓  (drafts letters, FAQs, call center scripts, media statements to individuals and public)
```

This skill is the **final communications layer** in the Legalcode breach skill family —
the documents that affected individuals and the public actually receive. It assumes
upstream skills or legal counsel have confirmed: (a) the breach is notifiable,
(b) which individuals are affected, (c) which jurisdictions are in scope, and
(d) what data categories were compromised.

---

## Jurisdiction and Governing Law

This skill applies multi-jurisdiction breach communication requirements simultaneously.
The notification laws governing the **affected individuals' residence** (not the
controller's or covered entity's headquarters) determine the applicable requirements.
For a single incident, multiple overlapping regimes frequently apply.

**Core legal authority (as of March 2026 — verify currency):**

| Regime                 | Individual Notification Authority                                            | Threshold Trigger                          | Timing                                               |
| ---------------------- | ---------------------------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------- |
| **EU GDPR**            | Art. 34; EDPB Guidelines 9/2022 (v2.0, adopted 28 March 2023)                | "High risk to rights and freedoms"         | Without undue delay                                  |
| **UK GDPR / DPA 2018** | Art. 34 UK GDPR; ICO Guidance (updated May 2025)                             | "High risk to rights and freedoms"         | Without undue delay                                  |
| **California**         | Cal. Civ. Code §§ 1798.29, 1798.82 (SB 446, eff. Jan 1, 2026)                | Breach of defined PII categories           | 30 calendar days from discovery [VERIFY]             |
| **New York SHIELD**    | N.Y. Gen. Bus. Law § 899-aa (amended Dec 24, 2024)                           | Breach of "private information"            | 30 days from discovery [VERIFY]                      |
| **Massachusetts**      | M.G.L. c. 93H; 201 CMR 17.00                                                 | Breach of personal information             | Without unreasonable delay; simultaneous with AG     |
| **Texas**              | Tex. Bus. & Com. Code § 521.053 (HB 4, eff. Sep 1, 2023)                     | Breach of sensitive PII                    | 30 days from discovery [VERIFY]                      |
| **Connecticut**        | Conn. Gen. Stat. § 36a-701b (as amended)                                     | Breach of personal information             | 60 days; 24-month credit monitoring for SSN [VERIFY] |
| **HIPAA**              | 45 CFR §§ 164.400–414 (Breach Notification Rule)                             | Breach of unsecured PHI                    | 60 calendar days from discovery                      |
| **Australia NDB**      | Privacy Act 1988 (Cth), Part IIIC; Privacy and Other Leg. Amendment Act 2024 | Eligible data breach (likely serious harm) | As soon as practicable after OAIC statement          |

[JURISDICTION-SPECIFIC] When drafting for any specific jurisdiction, verify:

- Current statutory text and any implementing regulations or AG guidance in force
- Mandatory content checklist and format requirements for that jurisdiction
- Any applicable sector overlay (HIPAA for health, GLBA/Safeguards for financial,
  FERPA for education, BIPA for biometrics)
- Language requirements (translated notices may be required or appropriate)
- Credit monitoring obligations specific to that jurisdiction and data categories exposed

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming breach facts, jurisdiction scope, or communication preferences, the workflow
pauses and asks when:

- Breach facts are incomplete and would change the scope of required communications
- Multiple valid drafting approaches exist and user preference matters
- Applicable jurisdictions affect mandatory content requirements
- Credit monitoring obligations are uncertain given available information
- Whether to draft from scratch vs. review an existing draft

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

### Step 1: Accept Breach Facts

Accept the breach incident summary in any of these formats:

- **Incident report**: Written summary of what happened, when discovered, what data was
  involved, and who was affected
- **Breach response checklist output**: Output from `legalcode-breach-response-checklist`
  or equivalent analysis
- **Free description**: User describes the breach verbally

**Minimum fact set required before drafting:**

| Fact                                                           | Why Needed                                                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Nature of the breach                                           | Drives "What Happened" section; determines narrative framing                                |
| Date of breach / date discovered                               | Required content in most jurisdictions; anchors all deadlines                               |
| Data categories affected                                       | Drives "What Information Was Involved" and risk-specific advice; triggers credit monitoring |
| Approximate number of affected individuals                     | Determines AG-notification thresholds, media notice (HIPAA), substitute notice              |
| Jurisdictions of affected individuals' residence               | Determines which legal requirements apply                                                   |
| Direct contact information available for affected individuals? | Determines whether substituted notice is needed                                             |
| Organization name, DPO/privacy contact, and contact details    | Required in all notification formats                                                        |

If essential facts are missing, prompt the user to supply them before proceeding.
Do not draft a notification with placeholder facts — incorrect facts are worse than
a brief delay for clarification.

### Step 2: Gather Communication Context

**⟁ CLARIFY** — Before drafting, ask the user:

1. **Document suite needed**: Which documents are required?
   - Options: Individual notification letters only, Full suite (letters + FAQ + call
     center script + media statement), Individual letters + FAQ only, Review an existing
     draft, Custom — specify
   - _Why this matters_: Scopes the work; different incidents require different outputs.

2. **Jurisdiction(s) in scope**: Which jurisdictions have affected individuals?
   - Options: EU/GDPR only, US only (specify key states), UK only, Australia only,
     Multi-jurisdiction (list all), Unknown — help me determine
   - _Why this matters_: Each jurisdiction has different mandatory content requirements.
     Drafting without jurisdiction clarity creates compliance risk.

3. **Data categories compromised**: What types of personal information were exposed?
   - Options: Names + contact information only, Financial account / credit card numbers,
     Social Security / government ID numbers, Health / medical information, Login
     credentials / passwords, Biometric data, GDPR special categories (race, religion,
     health, sexuality, etc.), Multiple categories — specify
   - _Why this matters_: Different data types trigger different credit monitoring
     obligations, different risk-specific guidance, and different threshold tests.

4. **Credit monitoring**: Has a credit monitoring provider been engaged?
   - Options: Yes — provider name and enrollment details available, Not yet — draft
     placeholder language, Not applicable for this breach type
   - _Why this matters_: California requires credit monitoring enrollment details in the
     notice itself; a notice without them is legally deficient.

5. **Existing draft**: Is there an existing draft to review?
   - Options: Yes — paste or upload for review, No — draft from scratch
   - _Why this matters_: Review mode is more targeted and faster than draft-from-scratch.

6. **Organizational context**:
   - Free text: Describe the organization (consumer-facing vs. B2B, size, industry), the
     nature of the relationship with affected individuals, and any litigation or
     reputational sensitivities.
   - _Why this matters_: A consumer health app breach requires different tone and risk
     framing than a B2B payroll processor breach.

### Step 3: Determine Notification Architecture

Based on breach facts and jurisdiction mapping, establish the notification structure.

**3a. Notification trigger confirmation (per jurisdiction):**

| Jurisdiction    | Trigger Met?                      | Basis                                              | Individual Notice Required? |
| --------------- | --------------------------------- | -------------------------------------------------- | --------------------------- |
| EU GDPR Art. 34 | [High risk?]                      | [Data categories + scale + context]                | [Yes / No / Conditional]    |
| UK GDPR Art. 34 | [High risk?]                      | [Same analysis as EU]                              | [Yes / No / Conditional]    |
| California      | [Defined PII categories exposed?] | [SSN / DL / financial / health / etc.]             | [Yes / No]                  |
| New York        | ["Private information" exposed?]  | [Data categories]                                  | [Yes / No]                  |
| Massachusetts   | [Personal information exposed?]   | [Data categories]                                  | [Yes / No]                  |
| HIPAA           | [Unsecured PHI?]                  | [PHI risk assessment — low probability exception?] | [Yes / No]                  |
| Australia NDB   | [Eligible data breach?]           | [Serious harm test]                                | [Yes / No]                  |

**⟁ CLARIFY** — If the user has not confirmed whether the GDPR/UK/Australia high-risk /
serious-harm threshold is met, present the options:

- "A qualified legal or privacy professional has confirmed this breach meets the
  high-risk / eligible data breach threshold" → proceed
- "Not yet confirmed" → recommend running `legalcode-breach-severity-assessment` first;
  draft communications in parallel but label them `DRAFT — PENDING THRESHOLD
CONFIRMATION — DO NOT SEND`

**3b. Sequencing rules — which notices go first:**

| Jurisdiction  | Sequencing Rule                                                                    | Notes                                                                    |
| ------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| EU GDPR       | No statutory sequencing between Art. 33 and Art. 34                                | Both "without undue delay"; EDPB allows simultaneous                     |
| UK GDPR       | ICO guidance: notify ICO and individuals as close to simultaneously as practicable | ICO expects individual notice shortly after the 72-hour SA report        |
| California    | No sequencing rule; AG and individuals simultaneously                              | Individuals and AG (if 500+ residents) at same time                      |
| Massachusetts | Simultaneous                                                                       | AG notification and individual notification must go out at the same time |
| HIPAA         | No prescribed sequencing                                                           | Individual, media (500+ per state), and HHS all within 60 days           |
| Australia NDB | **OAIC first, then individuals**                                                   | Entity must send OAIC Statement before individual notification           |

**⟁ CLARIFY** — If Australia NDB applies and the OAIC statement has not yet been filed:
flag the sequencing requirement. Ask whether to draft the individual notice now for
parallel preparation (labeled DO NOT SEND BEFORE OAIC STATEMENT FILED) or to wait.

**3c. Substituted notice thresholds:**

| Jurisdiction            | Trigger for Substituted Notice                                 | Required Form                                                                     |
| ----------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| GDPR Art. 34(3)(c)      | Disproportionate effort to contact individuals directly        | Public communication of equivalent effect reaching the affected population        |
| HIPAA § 164.404(d)      | Insufficient contact info for 10 or more individuals           | Conspicuous homepage posting for 90 days + toll-free number                       |
| California § 1798.82(g) | Not all individuals have provided postal or email contact info | Email acceptable if individual provided email; otherwise post/newspaper/broadcast |
| Australia s. 26WL(3)    | Impracticable to contact all affected individuals directly     | Prominent website notice + reasonable steps to reach individuals at risk          |

### Step 4: Gather Jurisdiction-Specific Legal Requirements

For each jurisdiction in scope, build the mandatory content checklist. Use **legalcode-mcp**
if connected (see External Tool Integration); otherwise apply the requirements below,
marking all jurisdiction-specific claims [VERIFY] for legal counsel confirmation.

#### 4a. GDPR Art. 34 Mandatory Content

_Authority: Art. 34(2) cross-referencing Art. 33(3)(b)–(d); EDPB Guidelines 9/2022 (v2.0) [VERIFY]_

**Legally required elements:**

- [ ] Name and contact details of the DPO or other designated point of contact (Art. 34(2) → Art. 33(3)(b))
- [ ] Description of the **likely consequences** of the breach (Art. 33(3)(c)) — must be specific, not generic
- [ ] Description of **measures taken or proposed** by the controller to address the breach and mitigate adverse effects (Art. 33(3)(d))
- [ ] Written in **clear and plain language** (Art. 34(2) express requirement)

**EDPB-recommended additions (Guidelines 9/2022 — not strictly required but strongly advised):**

- [ ] Brief description of what happened and the nature of the breach (how it occurred)
- [ ] Categories and approximate number of personal data records and individuals involved
- [ ] Whether any specifically high-risk individuals are affected (children, vulnerable persons)
- [ ] Practical steps individuals can take to protect themselves

**GDPR exemption check (Art. 34(3)) — document basis if any exemption is claimed:**

- (a) Appropriate technical measures (e.g., end-to-end encryption rendering data unintelligible) — document the measure and why high risk cannot materialize despite the breach
- (b) Subsequent remediation removed high risk (e.g., confirmed remote wipe before data accessed) — document the action and evidence basis
- (c) Disproportionate effort — if claimed, a public communication of equivalent effect must be used; document why direct contact is disproportionate

**Supervisory authority override (Art. 34(4))**: The competent DPA may require the controller to notify individuals even if the controller has invoked an exemption. Factor this risk into any exemption claim.

#### 4b. California Mandatory Format (Cal. Civ. Code § 1798.82, as amended by SB 446)

_[VERIFY all requirements against current statute and CA AG guidance; SB 446 eff. January 1, 2026]_

**Mandatory title**: "Notice of Data Breach" [VERIFY statutory requirement]

**Mandatory heading structure (§ 1798.82(d)) — all five headings required:**

- [ ] **"What Happened"**
- [ ] **"What Information Was Involved"**
- [ ] **"What We Are Doing"**
- [ ] **"What You Can Do"**
- [ ] **"For More Information"** (must include a toll-free telephone number) [VERIFY]

**Credit monitoring (§ 1798.82(e) / AB-1710)**: If SSN, driver's license number, or
California ID number was exposed, the notification must include:

- [ ] Offer of **at least 12 months of free** identity theft prevention and mitigation services [VERIFY]
- [ ] **All information necessary to enroll** — provider name, URL, phone number, and activation code must be in the notice itself [VERIFY]
- [ ] Enrollment deadline

**Timing**: 30 calendar days from discovery (SB 446, eff. January 1, 2026) [VERIFY]

**AG submission**: If 500+ California residents affected, submit a sample notification
(excluding personal information) to the California AG electronically [VERIFY current portal]

**Plain language**: Written in plain language; consider Spanish translation for
consumer-facing organizations with significant California Hispanic population

#### 4c. New York Mandatory Content (N.Y. Gen. Bus. Law § 899-aa, as amended December 24, 2024)

_[VERIFY all requirements against current statute and NY AG guidance]_

- [ ] Organization name and contact information
- [ ] Description of categories of information involved in the breach
- [ ] Date / range of dates of the breach (if known)
- [ ] What the organization is doing in response
- [ ] What individuals can do to protect themselves
- [ ] Contact information for the three major CRAs (Equifax, Experian, TransUnion) with
      toll-free numbers [VERIFY current requirement]
- [ ] Information about fraud alerts and security freezes

**Timing**: 30 days from discovery (eff. December 24, 2024) [VERIFY]

**NY DFS notification**: If entity is DFS-licensed, separate DFS notification required —
verify current DFS portal at dfs.ny.gov [VERIFY]

**Expanded "private information" definition**: Effective March 21, 2025, now includes
medical information and health insurance information [VERIFY]

#### 4d. Massachusetts Mandatory Content (M.G.L. c. 93H)

_[VERIFY all requirements against current statute and MA AG guidance]_

- [ ] Name and contact information of the organization
- [ ] Type of personal information involved in the breach
- [ ] Date of breach (to the extent known) and date of discovery
- [ ] What the organization has done or proposes to do regarding the breach
- [ ] Contact information for affected individuals to ask questions

**Credit monitoring (if SSN exposed)**: Offer of **18 months of free credit monitoring**
at no cost to affected individuals; enrollment information must be in the notice [VERIFY]

**Timing**: "Without unreasonable delay"; no calendar-day deadline, but the AG notice
must go out simultaneously with individual notification [VERIFY current AG guidance]

#### 4e. HIPAA Mandatory Content (45 CFR § 164.404(c))

_[VERIFY against current HHS/OCR guidance at hhs.gov/hipaa]_

- [ ] Brief description of **what happened**, including date of breach and date of discovery (if known)
- [ ] **Types of unsecured PHI** involved — must be specific (e.g., full name, SSN, date of birth, address, account number, diagnosis, treatment information, prescription details)
- [ ] **Steps individuals should take** to protect themselves from potential harm
- [ ] Brief description of the covered entity's **investigation and mitigation** steps, including what the entity is doing to investigate, mitigate harm, and protect against future breaches
- [ ] **Contact information**: toll-free telephone number, email address, **and** mailing address — all active for at least 90 days after the notice is sent [VERIFY]

**Preferred form**: First-class mail to last known postal address; email if individual
previously agreed electronically to receive communications; telephone for urgent situations
followed by written notice [VERIFY current OCR guidance]

**Timing**: Without unreasonable delay, **no later than 60 calendar days** after discovery
(for covered entities); Business Associates must notify the covered entity within 60 days
of discovering a breach [VERIFY]

**Substitute notice (§ 164.404(d))**: If contact info is insufficient for 10 or more
individuals, post a **conspicuous notice on the homepage** of the entity's website for
90 days and provide a toll-free number active during that period [VERIFY]

**Media notice (§ 164.406)**: If 500+ residents of a state or jurisdiction are affected,
notify prominent media outlets in that state within 60 days [VERIFY]; same content as
individual notice

**HHS notification (§ 164.408)**: If 500+ individuals, report to HHS Secretary
simultaneously with individual notification; the report is published publicly [VERIFY
current HHS portal at hhs.gov/hipaa/for-professionals/breach-notification]

#### 4f. Australia NDB Individual Notification (Privacy Act 1988 (Cth), s. 26WL)

_[VERIFY against current OAIC guidance; note Privacy and Other Legislation Amendment Act 2024 eff. December 10, 2024]_

- [ ] Identity and contact details of the entity
- [ ] Description of the eligible data breach
- [ ] Kinds of personal information involved
- [ ] Recommendations about **steps individuals should take** in response (specific and actionable)

**Form**: Plain English; directly to each affected individual if practicable; if impracticable
for all, prominent website notice plus reasonable steps to notify individuals at risk

**Timing**: As soon as practicable after the entity becomes aware the eligible data breach
has occurred and after the OAIC Statement has been provided [VERIFY sequence requirement]

**IDCARE**: Include reference to IDCARE (Australia's national identity and cyber support
service) as a recommended resource: 1800 595 160 or idcare.org

### Step 5: Draft Individual Notification Letter(s)

Draft the notification letter using the jurisdiction-appropriate mandatory format. Where
multiple jurisdictions apply, draft to satisfy the **most stringent combined requirements**,
or produce separate jurisdiction-specific letters if content requirements materially conflict.

**Drafting principles:**

- Use the mandatory title "Notice of Data Breach" universally (California requirement;
  best practice everywhere)
- Use mandatory headings exactly as prescribed (California: five specific headings)
- Lead with the most important information: what happened, what data was involved
- Be **specific** — name the exact data elements exposed; never write "personal information"
  without listing the specific fields
- Provide **actionable steps** with specific URLs, phone numbers, and step-by-step
  instructions — not generic direction
- Avoid minimizing language: do not use "incident," "event," or "situation" instead of
  "breach"; do not write "may have been accessed" if access is confirmed
- Avoid premature reassurances: do not write "no evidence of misuse" while investigation
  is incomplete
- Date the notice; include the date on which the breach was discovered

**⟁ CLARIFY** — If the organization has pre-approved language or existing templates:

- Ask whether to use the existing template as a starting point with jurisdictional
  requirements layered in, or to draft fresh
- Ask who signs the notice (named privacy officer, DPO, CEO, or outside counsel sign-off)

**Multi-language considerations:**
[JURISDICTION-SPECIFIC] Consider whether translated notices are required or appropriate:

- Spanish translations are strongly recommended for California, Texas, and Florida
  consumer-facing organizations with significant Spanish-speaking populations
- GDPR: EDPB Guidelines 9/2022 recommend communicating in the language of the individual's
  ordinary interaction with the controller — a French-speaking EU resident using a US
  platform may require a French-language notice
- Australia: OAIC guidance encourages accessible communication for culturally and
  linguistically diverse (CALD) communities
- HIPAA: OCR guidance on language access encourages limited-English-proficiency (LEP)
  accommodation for affected patient populations

See **Output Format Templates** for complete letter templates for each jurisdiction.

### Step 6: Draft FAQ Document

Draft a FAQ for the breach response webpage. Publish simultaneously with (or within 24
hours of) individual notification letters going out.

**Standard FAQ structure (12 questions — adapt as needed):**

1. **What happened?** Timeline: when did the breach occur; when was it discovered; brief factual description of how it occurred
2. **What information was involved?** Specific data categories; what was NOT involved (reassurance about data that was not exposed)
3. **Who is affected?** How individuals can determine whether they personally are affected; note if only a subset of customers/patients/users is affected
4. **What are you doing about it?** Investigation steps taken; security improvements implemented or planned; law enforcement notified; third-party forensic investigation engaged
5. **What can I do to protect myself?** Specific protective steps tailored to the data types exposed; credit monitoring enrollment; fraud alert and credit freeze instructions; password reset guidance
6. **Is there a cost to me for the credit monitoring?** Answer: No — credit monitoring is provided free of charge to affected individuals
7. **How do I enroll in the credit monitoring offer?** Step-by-step enrollment with activation code if applicable; enrollment URL; phone number for enrollment help; enrollment deadline
8. **Is my information safe now?** Honest, measured answer based on current investigation status — avoid false reassurances
9. **Are you legally required to notify me?** Brief explanation of applicable notification law(s) — without being dismissive or legalistic
10. **How can I contact you with questions?** Dedicated phone number; dedicated email address; hours of operation; response time commitment (e.g., "We will respond within 2 business days")
11. **Will I receive updates if there is new information?** Update commitment; webpage update policy; whether subsequent notices will be sent
12. **How do I place a fraud alert or security freeze?** Step-by-step with CRA contact details (Equifax, Experian, TransUnion); note freezes are free since the Economic Growth Act (2018) for US; IDCARE for Australia

**Timestamp and update policy**: Every FAQ version must be dated; material updates must be
prominently flagged with "Updated [date]: [description of change]." Never silently overwrite
FAQ content without a visible timestamp and change note.

**⟁ CLARIFY** — Before drafting the FAQ, ask:

- "Has the investigation determined the full scope of affected data? If not, the FAQ
  should acknowledge the investigation is ongoing and commit to a specific update
  timeline (e.g., 'We will update this page as our investigation progresses, with our
  next update no later than [date]')."
- "Is there a dedicated breach response webpage URL to reference in all communications?"

### Step 7: Draft Call Center Script

Draft a call center script for the breach response support line. Provide the script to
agents **before** the first notification letters go out — allow 24–48 hours for agent
briefing and practice.

**Script structure:**

**Module 1: Opening and Acknowledgment**

- Empathetic, professional greeting ("Thank you for calling [Organization Name]'s data
  security response line")
- Agent identifies themselves by first name and agent ID
- Caller identification and verification process

**Module 2: Verify Affected Status**

- Script for determining whether the caller is an affected individual
- What to say if they are affected; what to say if they are not (but still in the customer database, just not affected by this breach)

**Module 3: High-Frequency Question Scripts**
Prepared answers to each FAQ item above. Key examples:

- "What was taken?" — Specific to the breach; no more and no less than what the notice said
- "Am I at risk of identity theft?" — Balanced, honest; acknowledge the risk without causing panic; direct to protective steps
- "What are you going to do for me?" — Outline the credit monitoring offer; the investigation; the security improvements

**Module 4: Credit Monitoring Enrollment**

- Step-by-step guide for enrollment including troubleshooting common issues (code not working, website issues, enrollment deadline questions)
- Escalation path if enrollment cannot be completed on the call

**Module 5: Identity Theft in Progress**

- Immediate steps: direct to FTC IdentityTheft.gov (US), IDCARE (AU), or equivalent
- Connect with financial institution immediately
- Escalation to senior agent or privacy team for serious cases

**Module 6: Special Population Handling**

- **Domestic violence / stalking victims**: Address exposure may be an acute physical safety risk — escalate immediately to privacy officer; do not provide caller's information to anyone without authorization; provide relevant DV support resources and address confidentiality program information
- **Elderly or cognitively vulnerable individuals**: Slower pace; offer to repeat information; offer to call back with a family member present if requested
- **Limited-English-proficiency callers**: Connect to language support line or interpreter; do not ask the caller to find their own interpreter

**Module 7: Media Inquiries**

- Script: "I'm unable to comment on media inquiries, but I can connect you with our
  communications team. Please call [communications contact] or email [email]."
- Do not discuss specifics of the breach with anyone identifying as media

**Module 8: Hostile Callers / Threatened Legal Action**

- Script: "I hear that you're very frustrated, and I understand. For matters involving
  legal proceedings, I need to escalate this to our legal team. I can take your contact
  information and ensure a qualified representative contacts you within [timeframe]."
- Do not argue; do not make promises; escalate and document

**Module 9: Closing and Follow-Up**

- What the agent commits to (if anything); provide case reference number
- Confirm the caller has the breach response webpage URL and toll-free number

**Module 10: Documentation Requirements**

- Log: caller name, date/time, account number (if applicable), nature of inquiry,
  steps taken, escalation (if any), follow-up commitments
- Do not log personal health information or sensitive personal details beyond what
  is necessary for the call record

**Anti-patterns agents must actively avoid:**

- "We can't comment on an ongoing investigation" as a universal deflection for all questions
- Speculating about the cause of the breach or assigning blame
- Promising that the individual will not be a victim of identity theft ("no one can guarantee this")
- Offering any compensation, settlement, or benefit beyond what the organization has authorized in writing
- Giving legal advice ("you probably don't need to worry about this")
- Contradicting the notice letter — the script must align with every factual statement in the notice

**⟁ CLARIFY** — Before finalizing the script, ask:

- "Has a dedicated toll-free number been established and is it staffed before notices go out?"
- "Is the call center staffed internally or by an external vendor? What languages can agents support?"

### Step 8: Draft Media Statement

Draft a media statement or press release for publication in connection with the breach.

**Timing coordination — critical decision:**

| Jurisdiction                      | Media Statement Timing Rule                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| HIPAA (500+ residents of a state) | Prominent media outlet notification required within 60 days of discovery; coordinate with individual notice timing [VERIFY]                            |
| GDPR/UK GDPR                      | No statutory media release requirement; public communication may substitute for individual notice when direct contact is impracticable (Art. 34(3)(c)) |
| Most US states                    | No statutory media release requirement; media may break the story independently — prepare a statement in advance                                       |
| All                               | Best practice: individual notices go out **before** (or simultaneously with) the media statement                                                       |

**Core rule**: Do NOT publish a media statement before individual notices have been
delivered (unless required under HIPAA or using Art. 34(3)(c) substituted notice). Affected
individuals should not first learn about a breach affecting them from media coverage.
Learning of a breach from media rather than from the organization is a documented
aggravating factor in regulatory enforcement actions.

**Media statement structure:**

1. **Headline**: "[Organization] Notifying [Number of] Individuals Following Data Security Incident"
   — use "breach" or "security breach," not "incident" or "event"
2. **Lead paragraph**: What happened; when discovered; what data was involved
3. **What the organization is doing**: Security improvements; forensic investigation engaged;
   law enforcement notified (if true)
4. **What affected individuals should do**: Reference the dedicated breach response webpage
   URL and toll-free number
5. **Commitment statement**: The organization's accountability and forward-looking commitment
   to those affected
6. **Media contact**: Named communications contact with direct phone and email — not a
   general PR firm mailbox

**⟁ CLARIFY** — Before finalizing the media statement, ask:

- "Has legal counsel reviewed the media statement for litigation exposure? Media statements
  become exhibits in class action litigation. Every factual claim needs to be locked."
- "Is there a coordinated announcement timeline? For example, a regulatory filing that
  will become public on a specific date, potentially triggering media coverage before the
  individual notices go out?"

### Step 9: Draft Follow-Up Communications

Plan and draft the supplementary and follow-up communications framework.

**When follow-up notification is required:**

| Trigger                                                                     | Action                                                                                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Investigation reveals additional affected individuals not in initial notice | Supplementary notification to newly identified individuals using same format                  |
| Investigation reveals additional data categories not in initial notice      | Supplementary notice to ALL previously notified individuals; update FAQ immediately           |
| Initial notice contained incorrect facts (dates, data categories, scale)    | Correction notice with clear "CORRECTION" heading; explain what was wrong and what is correct |
| Credit monitoring enrollment offer expiring and individual has not enrolled | Optional reminder notice (best practice; not legally required in most jurisdictions)          |
| Significant update on investigation findings or security improvements       | Optional FAQ update; press release if material to investors (SEC obligations)                 |
| Regulator requires supplementary notice following an investigation          | Comply with regulator direction; document the requirement in Glass Box                        |

**Format for supplementary / correction notices:**

- Use the same mandatory format as the initial notice (same title, same heading structure)
- Add "Supplemental Notice of Data Breach" or "Correction: Notice of Data Breach" as the title prefix
- In "What Happened," clearly state: "This is an update to our Notice of Data Breach sent
  on [date]" and explain specifically what new information has been determined
- Reference the original notification date
- Provide the same credit monitoring, "What You Can Do," and "For More Information" content

**Follow-up schedule template (adapt to specific incident):**

```
Day 0:         Initial notification letters sent; FAQ published; call center live and staffed
Days 1–7:      Monitor call center volume; update FAQ based on common questions; add new
               Q&A items as they emerge from agent calls
Day 30:        Check credit monitoring enrollment rates; confirm substituted notice is still
               prominently posted (if applicable); California/New York 30-day deadline [VERIFY]
Day 60:        HIPAA: confirm individual notice, HHS notification, and any state media notice
               completed within 60-day window [VERIFY]; confirm HIPAA substitute notice (if
               applicable) is still on homepage
Day 90:        HIPAA substitute notice can be removed from homepage (after 90 days) [VERIFY]
Month 6:       Review investigation status; issue supplementary notice if new information
               requires it
Month 12:      Credit monitoring expiry approaching (if 12-month offer under CA); optional
               reminder to unenrolled individuals; consider whether call center can scale down
Month 18:      Massachusetts credit monitoring expiry (if 18-month offer) [VERIFY]
Month 24:      Connecticut credit monitoring expiry (if 24-month offer) [VERIFY]; assess
               whether active call center is still needed or can be archived
Ongoing:       Maintain breach response webpage until at least the longest credit monitoring
               offer has expired; do not delete FAQ or notice before that date
```

### Step 10: Quality Verification and Delivery Packaging

Before delivering the final communications suite, run all quality checks.

#### 10a. Communication Quality Classification

For each document in the suite, classify each mandatory element as COMPLIANT, NEEDS
REVISION, or NON-COMPLIANT (see Communication Quality Classification section below).
Revise all NEEDS REVISION and NON-COMPLIANT elements before delivery.

#### 10b. Pre-Send Checklist

| Item                                                                                       | Status |
| ------------------------------------------------------------------------------------------ | ------ |
| Mandatory title "Notice of Data Breach" used                                               | ☐      |
| Required heading structure present (California 5-heading format or equivalent)             | ☐      |
| DPO / privacy contact specifically named with direct contact details (not generic mailbox) | ☐      |
| Specific data categories named (not "personal information" without listing fields)         | ☐      |
| Likely consequences described (GDPR Art. 34 requirement)                                   | ☐      |
| Measures taken/proposed described (GDPR/UK requirement)                                    | ☐      |
| Credit monitoring offer included with enrollment instructions where legally required       | ☐      |
| Toll-free number included and staffed before notices go out                                | ☐      |
| Dedicated breach response webpage URL included and live                                    | ☐      |
| Notice written in plain language; no unexplained legal jargon                              | ☐      |
| Notification within applicable deadline (30 / 60 days / "without undue delay")             | ☐      |
| Multi-language versions prepared where appropriate                                         | ☐      |
| Legal counsel review obtained before sending                                               | ☐      |
| AG/OAIC notification sent or scheduled simultaneously where required                       | ☐      |
| For Australia: OAIC Statement filed before individual notices sent                         | ☐      |
| For HIPAA: email channel authorized by individual (if email used)                          | ☐      |
| Substituted notice posted conspicuously on homepage where applicable                       | ☐      |

#### 10c. Citation Quality Gates

Run the 5 Citation Quality Gates (see Quality Assurance Framework section) silently.
Revise any failures before delivery.

#### 10d. Glass Box Audit Trail

Complete the YAML audit trail in the final section before delivery.

#### 10e. Delivery Package Contents

Confirm all applicable elements are included:

- [ ] Individual notification letter(s) (with jurisdiction variants if multiple)
- [ ] Substituted / public notice version (if applicable)
- [ ] Multi-language versions (if applicable)
- [ ] FAQ document with publication date
- [ ] Call center script with briefing notes
- [ ] Media statement
- [ ] Follow-up schedule
- [ ] Pre-send checklist (completed)
- [ ] Glass Box audit trail (completed)

---

## Deep Topic Analysis

### A. Individual Notification — Jurisdiction Content Matrix

The following matrix shows minimum required content elements across the four core
jurisdictions. When multiple jurisdictions apply, satisfy every applicable row.

| Content Element                      | GDPR Art. 34  |    UK GDPR    |     California (SB 446)     |        Massachusetts        |             HIPAA             |
| ------------------------------------ | :-----------: | :-----------: | :-------------------------: | :-------------------------: | :---------------------------: |
| "Notice of Data Breach" title        | Best practice | Best practice |        **REQUIRED**         |        Best practice        |         Not specified         |
| Organization name + contact info     |   Implicit    |   Implicit    |        **REQUIRED**         |        **REQUIRED**         |         **REQUIRED**          |
| DPO / named privacy contact          | **REQUIRED**  | **REQUIRED**  |        Not specified        |        Not specified        |         Not specified         |
| "What Happened" section heading      |  Recommended  |  Recommended  |    **REQUIRED heading**     |        **REQUIRED**         |         **REQUIRED**          |
| Date of breach and date of discovery |  Recommended  |  Recommended  |        Not specified        |        **REQUIRED**         |         **REQUIRED**          |
| Specific data categories             |  Recommended  |  Recommended  |    **REQUIRED heading**     |        **REQUIRED**         |   **REQUIRED** (PHI types)    |
| Likely consequences                  | **REQUIRED**  | **REQUIRED**  |        Not required         |        Not required         |         Not required          |
| Measures taken / proposed            | **REQUIRED**  | **REQUIRED**  |    **REQUIRED heading**     |        **REQUIRED**         |         **REQUIRED**          |
| Specific protective steps            |  Recommended  |  Recommended  |    **REQUIRED heading**     |        **REQUIRED**         |         **REQUIRED**          |
| Toll-free phone number               | Not required  | Not required  |        **REQUIRED**         |        **REQUIRED**         | **REQUIRED** (90 days active) |
| Credit monitoring offer              | Not required  | Not required  | **REQUIRED** (SSN/DL/CA ID) | **REQUIRED** (SSN — 18 mo.) |         Not required          |
| Enrollment instructions in notice    | Not required  | Not required  |        **REQUIRED**         |        **REQUIRED**         |              N/A              |
| CRA contact information              | Not required  | Not required  |        Not specified        |        Not specified        |         Best practice         |
| Plain language                       | **REQUIRED**  | **REQUIRED**  |           Implied           |           Implied           |         Not specified         |

_All cells marked [VERIFY] — verify each requirement against current statutory text and
regulator guidance before sending any notice._

### B. Credit Monitoring Requirements by Jurisdiction

| Jurisdiction                 | Data That Triggers Obligation                                            | Duration                | Who Pays            | Enrollment Instructions in Notice? |
| ---------------------------- | ------------------------------------------------------------------------ | ----------------------- | ------------------- | ---------------------------------- |
| California                   | SSN, driver's license, or CA ID number                                   | 12 months minimum, free | Free to individual  | **REQUIRED in notice** [VERIFY]    |
| Massachusetts                | SSN                                                                      | 18 months minimum, free | Free to individual  | **REQUIRED in notice** [VERIFY]    |
| Connecticut                  | SSN                                                                      | 24 months minimum, free | Free to individual  | Required [VERIFY]                  |
| Delaware                     | SSN                                                                      | 12 months minimum, free | Free to individual  | Required [VERIFY]                  |
| Illinois                     | SSN (AG enforcement practice)                                            | 12 months (practice)    | Free                | Recommended [VERIFY]               |
| New York                     | Not mandated by statute                                                  | —                       | —                   | Best practice if offered           |
| Texas                        | Not mandated by statute                                                  | —                       | —                   | Best practice if offered           |
| HIPAA                        | Not mandated; OCR settlements often require identity protection services | Varies by settlement    | Free per settlement | Required if offered                |
| GDPR / UK GDPR               | Not mandated; proportionate mitigation measure                           | Discretionary           | Discretionary       | Include if offered                 |
| Australia NDB                | Not mandated                                                             | Discretionary           | Discretionary       | Include if offered                 |
| FTC recommendation (general) | Financial data or SSNs exposed                                           | 12–24 months            | Free                | Yes if offered                     |

**Credit monitoring offer standard language:**

```
[ORGANIZATION NAME] is offering [DURATION] months of free credit monitoring and
identity protection services through [PROVIDER NAME] at no cost to you.

To enroll:
  • Online: Visit [URL] and enter activation code [CODE]
  • By phone: Call [PHONE NUMBER], available [HOURS], [DAYS OF WEEK]

You must enroll by [ENROLLMENT DEADLINE DATE].

If you have trouble enrolling, call our dedicated response line at [TOLL-FREE NUMBER].
```

### C. Substituted Notice Requirements

| Jurisdiction         | When Substitute Applies                           | Required Format                                      | Duration                         |
| -------------------- | ------------------------------------------------- | ---------------------------------------------------- | -------------------------------- |
| GDPR Art. 34(3)(c)   | Disproportionate effort to contact individuals    | Public communication of equivalent effect            | Until direct contact practicable |
| HIPAA § 164.404(d)   | Insufficient contact info for 10+ individuals     | Conspicuous homepage posting + toll-free number      | 90 days [VERIFY]                 |
| California § 1798.82 | Contact info unavailable                          | Alternative written, electronic, or broadcast notice | Not specified                    |
| Australia s. 26WL(3) | Impracticable to contact all affected individuals | Prominent website notice + reasonable steps          | Reasonable period                |

**Substituted notice content**: The substitute notice is not abbreviated. It must contain
the same mandatory content as the direct individual notice. The substitution is only in
the delivery channel, not in the content.

### D. Special Population Handling

| Population                               | Heightened Risk                                                         | Required / Recommended Action                                                                              |
| ---------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Minor children**                       | Higher GDPR sensitivity; COPPA implications (US under-13)               | Direct notice to parent or guardian; consider child-specific risk guidance                                 |
| **Domestic violence / stalking victims** | Address exposure = acute physical safety risk                           | Immediate escalation to privacy officer; connect to Address Confidentiality Programs; DV support resources |
| **Elderly or cognitively vulnerable**    | Higher financial fraud risk; may be less able to take protective action | Offer large-print physical letter; ensure call center agents briefed; extra time on calls                  |
| **Limited-English-proficiency**          | Cannot act on notice they cannot understand                             | Translated notices; multi-language call center or interpreter line; multi-language FAQ                     |
| **HIPAA patients**                       | Medical information carries stigma and discrimination risk              | Specific HIPAA mitigation steps; extra sensitivity for mental health, substance abuse, HIV/STI information |
| **Employees**                            | Employment law overlay may apply                                        | Separate protocol; consult employment counsel re: any WARN Act or employment law dimensions                |

---

## Communication Quality Classification

For each element of a breach communication, classify it using this three-tier scale.

### COMPLIANT

The element:

- Is present in the communication
- Contains the legally required content for all applicable jurisdictions
- Is written in plain language accessible to a general (non-legal) audience
- Is accurate based on the breach facts provided
- Does not use minimizing, evasive, or misleading language

### NEEDS REVISION

The element:

- Is present but incomplete (e.g., credit monitoring offer without enrollment instructions)
- Contains legally required content but is written in a way that obscures or confuses
- Uses vague language where specificity is required (e.g., "personal information" without listing the specific fields exposed)
- Uses minimizing language that could be misleading (e.g., "security event," "may have been accessed" when access is confirmed)
- Is legally accurate but not written in plain language
- Is missing a jurisdiction-specific element but has similar content addressing the same concern

### NON-COMPLIANT

The element:

- Is entirely absent from the communication
- Contains factually incorrect information about the breach
- Violates the mandatory format requirements of the applicable jurisdiction
- States a false reassurance (e.g., "there is no risk of misuse" when investigation is incomplete or ongoing)
- Fails the plain language standard in a material way
- Does not include a credit monitoring offer (with enrollment instructions) where legally required
- Sends communication through a non-compliant channel (e.g., email for HIPAA without individual authorization)

---

## Actionable Output per Finding

For each NEEDS REVISION or NON-COMPLIANT element identified, provide:

1. **Element**: Which section / element of the communication is affected
2. **Classification**: NEEDS REVISION or NON-COMPLIANT
3. **Issue**: Specific description of what is wrong and why it matters
4. **Revised text**: Specific replacement language — provide the actual words, not just directions
5. **Legal basis**: Citation to the statute or regulator guidance requiring the fix [VERIFY]
6. **Priority**: CRITICAL / HIGH / MEDIUM / LOW (see Prioritization Framework)

**Example output format:**

```
Element: Credit monitoring offer — enrollment instructions
Classification: NON-COMPLIANT

Issue: California law (Cal. Civ. Code § 1798.82(e)) requires that when SSNs or
driver's license numbers are exposed, the notification must include both (1) an offer
of at least 12 months of free identity theft prevention services AND (2) all information
necessary to enroll — in the notice itself. The current draft mentions credit monitoring
availability but does not include the provider name, enrollment URL, phone number, or
activation code. This is a legally deficient notice under California law.

Revised text: [ORGANIZATION] is offering 12 months of free credit monitoring through
[PROVIDER] at no cost to you. To enroll, visit [URL] and enter code [ACTIVATION CODE],
or call [PHONE NUMBER]. Please enroll by [DATE — 12 months from notice date].

Legal basis: Cal. Civ. Code § 1798.82(e) (as amended by AB-1710) [VERIFY current text]
Priority: CRITICAL
```

---

## Prioritization Framework

| Priority     | Definition                                                                                                                                            | Required Action                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **CRITICAL** | Violation of a statutory deadline or mandatory content requirement that makes the notification legally deficient; creates direct enforcement exposure | Fix before sending any notice; escalate to legal counsel immediately; do not send until resolved |
| **HIGH**     | Creates material regulatory or litigation risk; makes notification substantively inadequate but not necessarily void on its face                      | Fix before sending; legal counsel review required                                                |
| **MEDIUM**   | Reduces clarity or usefulness to affected individuals; increases complaint or reputational risk; best-practice gap                                    | Fix before sending; counsel review recommended                                                   |
| **LOW**      | Minor drafting improvements; tone or style issues; no regulatory risk                                                                                 | Fix if time permits; revisit in next breach notification cycle                                   |

**CRITICAL examples:**

- Credit monitoring offer absent or missing enrollment instructions where legally required (California, Massachusetts)
- Notification sent more than 30 days after discovery (California, New York post-December 2024)
- Individual notification sent before OAIC Statement under Australia NDB
- HIPAA notice does not include toll-free contact active for 90 days
- Notification sent via email under HIPAA without individual's prior electronic authorization
- DPO / specific named contact absent from GDPR / UK GDPR notice

**HIGH examples:**

- Data category described as "personal information" without naming specific fields
- "No evidence of misuse" stated while investigation is ongoing
- FAQ not published simultaneously with notice letters
- Missing the California mandatory 5-heading structure
- Organizational contact is a generic mailbox (info@, privacy@) rather than a named person
- Media statement released before individual notices delivered

**MEDIUM examples:**

- Plain language improvements needed — dense paragraphs, unexplained technical terms
- Call center agents not briefed before notices go out
- No case reference numbers available for call center interactions
- Multi-language versions not prepared for significant non-English population

**LOW examples:**

- Logo or formatting improvements to make the notice more readable
- Minor tone adjustments for empathy or clarity
- Optional elements recommended by regulator guidance but not legally required

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                             | Fail Action                                                            |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Source**     | Every legal requirement cited names a specific statute, regulation, or regulator guidance document                                                                               | Add citation or mark "[UNVERIFIED REQUIREMENT — confirm with counsel]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., "Cal. Civ. Code § 1798.82"; "Art. 34 GDPR"; "45 CFR § 164.404")                                                    | Fix format                                                             |
| **Currency**   | Every cited provision verified for amendments or implementing regulations; recent law changes flagged (SB 446, NY Dec 2024 amendment, AU 2024 amendments, ICO May 2025 guidance) | Flag "[CHECK CURRENCY — THIS LAW MAY HAVE CHANGED]"                    |
| **Domain**     | Analysis stays within the jurisdiction's scope; no jurisdiction X requirements attributed to jurisdiction Y                                                                      | Remove or flag jurisdictional bleed                                    |
| **Confidence** | Uncertainty explicitly stated, not hidden; do not assert requirements with high confidence when the statutory text or regulator guidance is genuinely ambiguous                  | Add confidence qualifier or [VERIFY] tag                               |

### Self-Interrogation for CRITICAL Items

For any element classified CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the requirement follow directly from the cited
legal authority? If the statute requires element X, does the current draft contain element X?
Is there a plausible legal argument that the requirement does not apply to this situation
(e.g., a safe harbor, an exemption, a threshold not met)?

**Pass 2 — Completeness**: Have all sub-elements of the requirement been satisfied? For
example, California's credit monitoring requirement has two distinct parts: (1) the offer
of services AND (2) all enrollment information in the notice. Does the draft satisfy both?

**Pass 3 — Challenge**: What is the strongest argument that the current draft is sufficient
despite the identified CRITICAL gap? Under what circumstances might a regulator accept the
draft as-is? This determines whether to confirm CRITICAL or downgrade to HIGH.

### Confidence Scoring

| Level        | Range     | Meaning                                                       | Action                                                  |
| ------------ | --------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled, unambiguous statutory requirement                    | State with confidence                                   |
| **High**     | 0.80–0.94 | Strong statutory basis; minor interpretive questions          | State with brief caveat                                 |
| **Probable** | 0.60–0.79 | Good arguments; jurisdiction interpretation not fully settled | State with reasoning and contra-indicators              |
| **Possible** | 0.40–0.59 | Genuinely uncertain                                           | Flag for professional review; present both sides        |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                       | Do not assert; flag "[UNCERTAIN — VERIFY WITH COUNSEL]" |

Apply confidence scoring to:

- Claims that a specific jurisdiction requires a specific notice element
- Claims about timing deadlines
- Claims about credit monitoring obligations
- Claims about whether the high-risk / serious-harm threshold is met
- Claims about whether a channel (email, etc.) satisfies delivery requirements

---

## Anti-Patterns

The following patterns appear repeatedly in deficient breach communications. Actively
check for and eliminate each one before delivery.

1. **"Incident," "event," or "situation" instead of "breach"** — Minimizing language that
   fails to communicate seriousness and may mislead individuals about their actual risk.
   EDPB, FTC, and state AG enforcement actions have specifically criticized this pattern.
   Use: "data breach" or "security breach."

2. **"Unauthorized access to some of your personal information"** — Vague data category
   description. Individuals cannot take targeted protective action without knowing
   specifically what was exposed (SSN vs. email address vs. medical record vs. password).
   Name every specific data element.

3. **"No evidence of misuse" stated prematurely** — When investigation is in its early
   stages, asserting "there is no evidence that your information has been misused" creates
   a false reassurance and a later liability if misuse is subsequently discovered. Use
   instead: "Our investigation is ongoing. We have not confirmed that your information has
   been misused, but we encourage you to take the protective steps listed below."

4. **Credit monitoring offer without enrollment instructions** — California law requires
   that the notice contain all information necessary to take advantage of the credit
   monitoring offer. A notice that says "we are offering free credit monitoring — visit our
   website" without a specific URL, phone number, and activation code is legally deficient.

5. **Generic privacy@ or info@ contact instead of a named person** — GDPR Art. 34 requires
   naming the DPO or other specific point of contact. A generic mailbox does not satisfy
   this requirement. ICO enforcement actions have cited inadequate contact information as
   a violation. Provide a named individual with a direct phone number and email.

6. **Email channel without HIPAA authorization** — Under HIPAA, email may only be used
   for breach notice if the individual previously agreed electronically to receive
   communications from the covered entity via email (45 CFR § 164.404(b)(1)(i)). Use
   first-class mail for HIPAA notices unless individual email authorization is confirmed
   and documented.

7. **Notice buried on the website — not linked from homepage** — HIPAA substitute notice
   requires a "conspicuous posting on the home page." ICO guidance criticizes notices
   published only in press release sections or blog posts. The notice must be accessible
   to anyone who visits the organization's main website.

8. **Media statement released before individual notices** — Unless required under HIPAA
   (500+ state residents) or using GDPR Art. 34(3)(c) public substituted notice, individuals
   should receive direct notification before any public statement. Learning about a breach
   from media rather than from the organization directly is a documented aggravating factor
   in regulatory enforcement and a source of reputational harm.

9. **Generic protective steps advice** — Writing "monitor your credit" without providing
   the three CRA URLs, the free credit freeze process, the FTC IdentityTheft.gov URL, and
   IDCARE details (for Australian notices) fails the plain language and usefulness standard.
   Regulators expect specific, actionable guidance tailored to the types of data exposed.

10. **Dense, legalistic prose** — Breach notifications written in legalese to minimize
    organizational liability are routinely criticized by regulators and confuse individuals
    who most need to understand the notice. California's mandatory heading structure exists
    specifically to counter this. Write for a general consumer audience at an 8th-grade
    reading level, not for lawyers.

11. **Single notification wave for a multi-phase investigation** — When investigation
    subsequently reveals additional affected individuals or additional data categories not
    in the initial notice, a supplementary notice must be sent. Failing to update the
    initial notice creates ongoing regulatory exposure. The California AG's $6.75 million
    fine for "misleading the public about the full impact of the breach" establishes that
    materially incomplete initial notices create significant liability. [VERIFY enforcement basis]

12. **Call center agents briefed after notices arrive** — If agents answering the breach
    response line are unaware of the breach when affected individuals call, the resulting
    confusion worsens reputational harm and creates escalation chaos. Brief agents 24–48
    hours before notices go out.

13. **No dedicated toll-free number** — Directing affected individuals to a general company
    phone line rather than a dedicated breach response line dilutes call quality and prevents
    accurate tracking of individual interactions. California and HIPAA both require a toll-free
    number; it is best practice everywhere.

14. **FAQ not updated when investigation findings expand** — Publishing a FAQ and then not
    updating it when new information emerges creates inconsistency between the FAQ and
    supplementary notices, and may constitute misleading communication. Date-stamp all FAQ
    updates prominently.

15. **Failure to address domestic violence and physical safety populations** — When address
    information is exposed and there are populations at physical risk (DV victims, protected
    witnesses, at-risk minors), a general "monitor your credit" response is inadequate.
    These individuals need immediate escalation, connection to DV services, and potentially
    emergency Address Confidentiality Program enrollment.

16. **Australia NDB: individual notice sent before OAIC Statement** — Under the NDB scheme,
    the entity must provide the OAIC Statement before notifying individuals. Sending
    individual notices before the OAIC Statement violates the prescribed sequence and
    creates a procedural compliance failure.

17. **Credit monitoring activation codes not pre-generated** — Most credit monitoring
    vendors require pre-generated activation codes. A notice promising credit monitoring
    with a code that does not work triggers a secondary wave of complaints and call center
    volume. Confirm codes are generated, tested, and ready before notices go out.

18. **"This notice satisfies all applicable legal requirements" language in the consumer
    notice itself** — Including legal compliance statements in the consumer-facing document
    creates false confidence and can backfire if requirements were inadvertently missed.
    Keep compliance analysis in legal memoranda; keep the consumer notice focused on
    informing the individual.

---

## Writing Standards and Plain Language

All breach communications must meet these writing standards before delivery.

### Core Principles

1. **Active voice**: "Our systems were compromised on [date]" not "There was a compromise
   of our systems that occurred on [date]"
2. **Verb-first sentences**: Lead every section with the action — what happened, what you
   are doing, what the individual should do
3. **Sentence length**: Target 25 words or fewer per sentence; break long sentences into
   two shorter ones
4. **Paragraph length**: 3–5 sentences maximum; each paragraph covers one topic
5. **Reading level**: 8th grade reading level target; avoid terminology requiring legal or
   technical knowledge; define any technical term that cannot be replaced with plain English
6. **Concrete specifics**: Exact dates, exact data elements, exact URLs, exact phone
   numbers — never vague approximations
7. **Logical order**: Most important information first; action items before background;
   contact information at the end

### Prohibited Language Patterns

| Instead of                                           | Use                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| "Incident," "event," "situation"                     | "Data breach" or "security breach"                           |
| "May have been accessed" (when confirmed)            | "Was accessed" or "Was exposed"                              |
| "Some personal information"                          | Name the specific data elements                              |
| "No evidence of misuse" (investigation ongoing)      | "Our investigation is ongoing; we have not confirmed misuse" |
| "We take the security of your information seriously" | Cut entirely — this is meaningless filler                    |
| "Pursuant to applicable law"                         | Cut, or specify which law                                    |
| "In order to"                                        | "To"                                                         |
| "At this point in time"                              | "Now"                                                        |
| "Due to the fact that"                               | "Because"                                                    |
| "With respect to"                                    | "About"                                                      |
| "In the event that"                                  | "If"                                                         |
| "We would like to inform you that"                   | Delete — just state the information                          |

### Quality Gate Before Delivery

Run this final check before sending any communication:

- [ ] Read the letter aloud — does it sound like clear communication, or defensive legal writing?
- [ ] Would an affected individual know exactly what happened after reading the opening paragraph?
- [ ] Does the letter tell the individual specifically what data of theirs was exposed?
- [ ] Does the letter provide concrete, actionable steps the individual can take today?
- [ ] Is every piece of contact information (phone, URL, email, address) complete and correct?
- [ ] Would a reasonable regulator consider this communication "clear and plain language"?
- [ ] Is the credit monitoring offer complete with enrollment instructions (where legally required)?
- [ ] Is the notice dated?
- [ ] Has qualified legal counsel reviewed and approved the communication before sending?

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp to:

- Verify current statutory text of cited provisions (SB 446, NY 2024 amendment, AU 2024
  Privacy Act amendments) against authoritative sources
- Check for any regulator guidance published since this skill's creation date (March 2026)
- Retrieve current AG portal and submission format requirements for each applicable state
- Verify HIPAA content requirements against current OCR guidance
- Check for recent enforcement decisions or AG fine announcements that affect best practices

Save results to `/tmp/legalcode-breach-comms-research.md`:

```markdown
# Breach Communications Legal Research

## Date: [date]

## Jurisdictions: [in scope]

### Statutory Text Verified

- [Citation, verification date, key requirement confirmed or changed]

### Recent Regulator Guidance

- [Regulator, guidance title, date, key change]

### Recent Enforcement Actions

- [Regulator, entity, key criticism, penalty amount, date — lessons for this draft]
```

### Without legalcode-mcp (Graceful Degradation)

- Mark all jurisdiction-specific statutory requirements with [VERIFY — confirm against
  current official source]
- Note in Glass Box: `legalcode_mcp: "Not connected — all statutory requirements require
independent verification by qualified counsel before sending any notice"`
- Focus quality assurance on structural completeness, plain language, and mandatory
  heading structure; flag all legal accuracy verification as a counsel responsibility
- Direct the user to official sources: hhs.gov/hipaa, oaic.gov.au, oag.ca.gov,
  ico.org.uk, ftc.gov/data-breach-response for current requirements

### Upstream Skill Integration

| Skill                                              | Input Consumed                                                                   | How to Use                                                                                                        |
| -------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `legalcode-breach-severity-assessment`             | Notifiability determination; affected population; data categories; risk level    | Receive confirmed breach facts and high-risk / serious-harm determination before drafting                         |
| `legalcode-breach-response-checklist`              | Critical path; jurisdiction list; deadline calendar                              | Use as jurisdiction scoping and timing input; do not re-derive what this skill already computed                   |
| `legalcode-us-breach-notification-triage`          | US state-specific requirements; state-by-state content and credit monitoring map | Receive US state content requirements for each state with affected residents                                      |
| `legalcode-breach-regulatory-notification-drafter` | Regulatory notice content; facts stated to regulators                            | Ensure individual notice facts are consistent with regulatory notice facts; discrepancies create enforcement risk |

---

## Glass Box Audit Trail

Complete this YAML block and include it in the final deliverable package (in internal
records, not in consumer-facing communications):

```yaml
glass_box:
  skill_name: "legalcode-breach-affected-party-communication"
  mode: "Draft from scratch / Review existing draft"
  incident_reference: "[Organization internal incident ID or reference]"
  date_of_breach: "[Date breach occurred, or 'Unknown — investigation ongoing']"
  date_of_discovery: "[Date breach discovered by organization]"
  date_of_analysis: "[Today's date]"
  notification_deadlines:
    california_30_day: "[Deadline date if CA residents affected]"
    new_york_30_day: "[Deadline date if NY residents affected]"
    hipaa_60_day: "[Deadline date if PHI breach]"
    australia_asap: "[Target date if AU NDB applies]"
    gdpr_without_undue_delay: "[Target date if GDPR applies]"
  jurisdictions_in_scope:
    - "[Jurisdiction 1 — basis: X residents affected]"
    - "[Jurisdiction 2 — basis: Y residents affected]"
  data_categories_involved:
    - "[Data category 1 — e.g., Social Security numbers]"
    - "[Data category 2 — e.g., Health/medical records]"
  affected_individuals_count: "[Approximate count or range]"
  documents_drafted:
    individual_letter_versions: "[Number of jurisdiction variants; e.g., California-format + GDPR-format]"
    faq: "[Yes / No]"
    call_center_script: "[Yes / No]"
    media_statement: "[Yes / No]"
    supplementary_notice_template: "[Yes / No / Scheduled for: date]"
    multilanguage_versions: "[Yes: languages / No]"
  credit_monitoring:
    required_jurisdictions: "[California / Massachusetts / Connecticut / None / Pending]"
    provider: "[Provider name or 'Not yet selected — placeholder language used']"
    duration: "[Months, by jurisdiction]"
    enrollment_instructions_included: "[Yes / No / Partial — missing: specify]"
  notification_sequencing:
    oaic_statement_filed_before_au_individual_notice: "[Yes / No / N/A]"
    ag_notification_timed_with_individual_notice: "[Yes / No / N/A]"
    individual_notice_before_media_statement: "[Yes / No / Simultaneous per HIPAA]"
  channel_compliance:
    hipaa_email_authorization_confirmed: "[Yes / No / N/A — not email]"
    substitute_notice_needed: "[Yes / No]"
    substitute_notice_posted_on_homepage: "[Yes / No / N/A]"
  quality_classification:
    individual_letter: "[COMPLIANT / NEEDS REVISION / NON-COMPLIANT]"
    faq: "[COMPLIANT / NEEDS REVISION / NON-COMPLIANT]"
    call_center_script: "[COMPLIANT / NEEDS REVISION / NON-COMPLIANT]"
    media_statement: "[COMPLIANT / NEEDS REVISION / NON-COMPLIANT]"
  findings_count:
    critical: "[N]"
    high: "[N]"
    medium: "[N]"
    low: "[N]"
  legalcode_mcp: "[Connected — citations verified / Not connected — manual verification required]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale: e.g., 'HIGH — all major statutory requirements identified; legalcode-mcp confirmed currency of all citations; legal counsel review obtained']"
  limitations:
    - "[Scope limitation — e.g., 'Multi-state credit monitoring map beyond California/Massachusetts/Connecticut not verified in this run — use legalcode-us-breach-notification-triage for complete 50-state mapping']"
    - "[Assumption — e.g., 'Breach facts as provided by client; forensic investigation ongoing']"
  reviewer: "AI-assisted — requires review and approval by qualified legal counsel before any notice is sent"
```

---

## Localization Notes

### EU GDPR Localization

- **Language of communication**: EDPB Guidelines 9/2022 recommend communicating in the
  language of the individual's ordinary interaction with the controller — not the
  organization's preferred language. A French user of a US platform may require a
  French-language notice. A Spanish user of a German platform may require Spanish.
- **DPO requirement**: Organizations required to have a DPO under Art. 37 must name the
  DPO in the notification. Entities not required to have a DPO should name a specific
  privacy contact — not a generic mailbox.
- **Special category data (Art. 9)**: If special categories are involved (health,
  racial/ethnic origin, religion, sexual orientation, biometric/genetic data, criminal
  records), the high-risk threshold is more readily met. The "likely consequences" section
  must address specific risks from the special category (e.g., discrimination, stigma,
  targeting, insurance consequences).
- **Children's data (Art. 8)**: Treat as high-risk by default if children's data was
  involved; consider directing notices to parents or guardians.
- **Supervisory authority override (Art. 34(4))**: The competent DPA can require individual
  notification even when the controller invokes an Art. 34(3) exemption. Factor this risk
  into any exemption analysis.

### UK GDPR Localization

- **ICO "report early, update later" posture**: ICO's May 2025 guidance update emphasizes
  not delaying notification until the investigation is complete. Send an initial notice
  with known facts; update as investigation progresses. [VERIFY current ICO guidance]
- **Data Use and Access Act 2025**: Enacted August 2025; introduced incremental UK
  divergence from EU GDPR. The Art. 34 individual notification framework is not materially
  altered, but verify current ICO guidance for any implementing changes. [VERIFY]
- **PECR (Privacy and Electronic Communications Regulations 2003)**: For telecoms and ISPs,
  separate PECR breach reporting obligations may apply alongside UK GDPR. [VERIFY]

### US State Localization

- **50-state variation**: The framework above covers the highest-impact states. For a
  definitive 50-state map, use `legalcode-us-breach-notification-triage` or the Perkins
  Coie 50-State Security Breach Notification Chart. [VERIFY currency of any external chart]
- **Sector overlay — highest standard prevails**: When state law and a federal sector rule
  both apply (e.g., a California hospital subject to both Cal. Civ. Code § 1798.82 AND
  45 CFR § 164.404), satisfy every applicable requirement from both frameworks. The more
  stringent requirement on each element prevails.
- **AG portal formats**: Each state AG has a specific portal and sometimes a specific form
  format. Verify current portal requirements at the state AG's website before submitting.
- **BIPA (Illinois)**: The Illinois Biometric Information Privacy Act is not primarily a
  breach notification statute, but a BIPA breach creates significant class action liability
  ($1,000 per negligent violation; $5,000 per intentional/reckless violation per person).
  Consult Illinois employment and privacy counsel immediately if biometric data was
  compromised. [VERIFY current BIPA enforcement framework]

### Australia NDB Localization

- **Serious harm threshold**: A genuine harm assessment is required — not every breach
  triggers the NDB scheme. Document the assessment. If harm is not likely, there is no
  notification obligation.
- **OAIC sequencing**: Entity must provide the OAIC Statement **before** notifying
  individuals. Prepare both documents in parallel; do not send individual notices until
  the OAIC Statement is filed.
- **IDCARE**: Australia's national identity and cyber support service (1800 595 160;
  idcare.org). Always reference IDCARE in the "What You Can Do" section for AU NDB notices.
- **Privacy and Other Legislation Amendment Act 2024** (eff. December 10, 2024): Introduced
  a statutory tort for serious privacy invasion and a criminal offence for sharing personal
  information with intent to harm. These increase litigation exposure for inadequate breach
  response significantly. [VERIFY current OAIC guidance incorporating these amendments]
- **State and territory public sector obligations**: Victoria, NSW, and QLD have additional
  public sector breach notification obligations. Check applicable state privacy legislation
  for public sector entities. [VERIFY applicable state legislation]

---

## Output Format Templates

### Template A: Individual Notification Letter — California SB 446 Mandatory Format

```
[ORGANIZATION LETTERHEAD]

[DATE OF NOTICE]

[RECIPIENT NAME]
[ADDRESS]
[CITY, STATE, ZIP]

                    NOTICE OF DATA BREACH

What Happened

On [DATE OF BREACH], [DESCRIPTION OF HOW BREACH OCCURRED — plain language, specific]. We
discovered this incident on [DATE OF DISCOVERY]. We immediately [IMMEDIATE CONTAINMENT
STEP TAKEN — e.g., secured the affected systems and launched an investigation].

What Information Was Involved

Based on our investigation, the following types of your personal information were involved:

  • [DATA ELEMENT 1 — e.g., Social Security number]
  • [DATA ELEMENT 2 — e.g., Name and date of birth]
  • [DATA ELEMENT 3 — e.g., Driver's license number]

[If applicable: Your [DATA ELEMENT] was NOT involved in this incident.]

What We Are Doing

We have taken the following steps in response:

  • [SECURITY STEP 1 — e.g., Secured all affected systems and closed the unauthorized
    access point]
  • [SECURITY STEP 2 — e.g., Engaged a leading cybersecurity firm to conduct a forensic
    investigation]
  • [SECURITY STEP 3 — e.g., Notified law enforcement]
  • [SECURITY IMPROVEMENT — e.g., Implemented additional monitoring and access controls
    to prevent a similar incident]

We are also offering [NUMBER] months of free credit monitoring and identity protection
services. Please see the enrollment instructions in the "What You Can Do" section below.

What You Can Do

We recommend you take these steps now to help protect your information:

1. ENROLL IN FREE CREDIT MONITORING (free for [NUMBER] months)

   [ORGANIZATION] is offering [NUMBER] months of free credit monitoring and identity
   protection services through [PROVIDER NAME] at no cost to you.

   To enroll:
   • Online: Go to [URL] and enter activation code: [CODE]
   • By phone: Call [PHONE NUMBER], [HOURS], [DAYS OF WEEK]

   Please enroll by [ENROLLMENT DEADLINE DATE].

2. PLACE A FRAUD ALERT (free)

   Contact any one of the three major credit bureaus to place a free fraud alert on your
   credit file. A fraud alert asks businesses to verify your identity before opening new
   credit accounts. The bureau you contact will notify the other two.

   • Equifax: 1-800-685-1111 | equifax.com/personal/credit-report-services/free-credit-freeze
   • Experian: 1-888-397-3742 | experian.com/help/fraud-assistance.html
   • TransUnion: 1-888-909-8872 | transunion.com/credit-freeze

3. CONSIDER A SECURITY FREEZE (free)

   A security freeze (credit freeze) prevents new credit accounts from being opened in
   your name. It is free at all three bureaus and can be temporarily lifted when you need
   to apply for credit. Contact each bureau individually to place a freeze.

4. MONITOR YOUR ACCOUNTS

   Review your bank and credit card statements for any unauthorized transactions. Report
   any suspicious activity to your financial institution immediately.

5. VISIT IdentityTheft.gov (U.S. residents)

   If you believe someone has used your personal information fraudulently, go to
   IdentityTheft.gov for a free personalized recovery plan from the Federal Trade Commission.

For More Information

If you have questions about this notice or what steps to take, please contact us:

  Dedicated Response Line: [TOLL-FREE NUMBER]
  Available: [HOURS], [DAYS OF WEEK]

  Email: [DEDICATED BREACH EMAIL — NOT A GENERIC MAILBOX]
  Website: [BREACH RESPONSE WEBPAGE URL]

  Mail: [ORGANIZATION NAME]
        Attention: [PRIVACY OFFICER / NAMED CONTACT]
        [ADDRESS]
        [CITY, STATE, ZIP]

We sincerely regret this incident and the concern it may cause you.

[SIGNATURE]

[NAME]
[TITLE]
[ORGANIZATION NAME]
```

---

### Template B: GDPR / UK GDPR Art. 34 Individual Notification Letter

```
[ORGANIZATION LETTERHEAD]

[DATE OF NOTICE]

Dear [NAME / "Valued Customer" if name not available],

                    Notice of Personal Data Breach

We are writing to inform you that [ORGANIZATION NAME] has experienced a personal data
breach that involves your personal information. We are notifying you because our
assessment indicates this breach is likely to result in a high risk to your rights and
freedoms under [the GDPR / UK GDPR].

What Happened

On [DATE], [PLAIN-LANGUAGE DESCRIPTION OF BREACH — what occurred; how]. We became
aware of this incident on [DISCOVERY DATE]. [Brief description of the type of breach:
unauthorized access / accidental disclosure / ransomware / loss of device / etc.]

Your Personal Data That Was Involved

The following categories of your personal data were involved:

  • [DATA CATEGORY 1]
  • [DATA CATEGORY 2]

[If applicable]: This included [SPECIAL CATEGORY DATA TYPE — e.g., health information],
which we recognize is particularly sensitive.

[Your [DATA CATEGORY] was NOT involved in this incident.]

Likely Consequences

Based on our assessment, this breach may result in: [SPECIFIC LIKELY CONSEQUENCES — e.g.,
risk of identity theft; risk of unauthorized access to financial accounts; risk of targeted
phishing using the exposed data]. We do not [/do] have confirmed evidence of misuse as of
the date of this letter; our investigation is ongoing.

What We Have Done and Are Doing

We have taken the following steps to address this breach and reduce the risk to you:

  • [REMEDIATION ACTION 1]
  • [REMEDIATION ACTION 2]
  • [We have notified [the relevant supervisory authority / the [ICO / DPA name]] as required]

[If credit monitoring offered]: We are offering [details] at no cost to you — see below.

What You Can Do

We recommend the following steps to protect yourself:

  • [SPECIFIC PROTECTIVE ACTION 1 — tailored to data type exposed]
  • [SPECIFIC PROTECTIVE ACTION 2]
  • [SPECIFIC PROTECTIVE ACTION 3 — e.g., change your password for accounts using the
    same credentials as your account with us]

[If credit monitoring offered]: To enroll in free [DURATION] months of credit monitoring
through [PROVIDER], visit [URL] or call [PHONE]. Enrollment code: [CODE].

Contact Us

If you have any questions about this notice, please contact:

  [DPO NAME / PRIVACY CONTACT NAME]
  [Title: Data Protection Officer / Privacy Officer]
  Email: [SPECIFIC EMAIL — not a generic mailbox]
  Phone: [DIRECT PHONE NUMBER]
  Post: [ADDRESS]

We are available [HOURS / DAYS] and commit to responding within [TIMEFRAME — e.g.,
5 business days].

[If ICO/DPA complaint right]: You also have the right to make a complaint to [the ICO
at ico.org.uk / the relevant supervisory authority] if you believe your data protection
rights have been affected.

Yours sincerely,

[NAME]
[TITLE]
[ORGANIZATION NAME]
```

---

### Template C: Australia NDB Individual Notification

```
[ORGANIZATION LETTERHEAD]

[DATE OF NOTICE]

Dear [NAME / "Affected Individual"],

                    Notice of Eligible Data Breach

[ORGANIZATION NAME] is writing to notify you of an eligible data breach under the Privacy
Act 1988 (Cth) that involves your personal information.

What Happened

On [DATE], [PLAIN-LANGUAGE DESCRIPTION]. We became aware of this incident on [DISCOVERY DATE]
and took the following immediate steps: [CONTAINMENT STEPS].

Your Information That Was Involved

The following kinds of your personal information were involved:

  • [KIND 1]
  • [KIND 2]

What We Recommend You Do

To help protect yourself, we recommend:

  1. Contact IDCARE — Australia's national identity and cyber support service — for free
     expert guidance on protecting your identity:
     • Phone: 1800 595 160
     • Website: idcare.org

  2. [SPECIFIC PROTECTIVE STEP — e.g., Change your password and security questions for
     any online accounts where you use similar credentials]

  3. [SPECIFIC PROTECTIVE STEP — e.g., Monitor your bank and credit card statements for
     any unusual transactions]

  4. [If financial data involved]: Contact your financial institution to discuss additional
     account protections.

What We Are Doing

[DESCRIPTION OF INVESTIGATION AND REMEDIATION — specific steps taken]

We have notified the Office of the Australian Information Commissioner (OAIC) as required
under the Privacy Act 1988 (Cth).

Questions or Concerns

For more information or to discuss this notification:

  [CONTACT PERSON NAME]
  [Title: Privacy Officer / DPO]
  Email: [SPECIFIC EMAIL]
  Phone: [PHONE NUMBER]
  Post: [ADDRESS]

Your Rights

You have the right to make a complaint to the Office of the Australian Information
Commissioner (OAIC) if you believe your privacy rights have been affected:
  • Website: oaic.gov.au
  • Phone: 1300 363 992

Yours sincerely,

[NAME]
[TITLE]
[ORGANIZATION NAME]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep legal research
conducted March 2026, covering:

- GDPR Art. 34; EDPB Guidelines 9/2022 on Personal Data Breach Notification (Version 2.0,
  adopted 28 March 2023)
- UK GDPR Art. 34; ICO Personal Data Breaches Guidance (updated May 2025); Data Use and
  Access Act 2025
- California Civil Code §§ 1798.29, 1798.82 as amended by SB 446 (eff. January 1, 2026)
  and AB-1710; California AG breach enforcement practice
- New York General Business Law § 899-aa as amended December 24, 2024 (30-day deadline;
  expanded private information definition eff. March 2025)
- Massachusetts M.G.L. c. 93H; 201 CMR 17.00 (18-month credit monitoring)
- Texas Business & Commerce Code § 521.053 (HB 4, eff. September 1, 2023)
- Connecticut General Statutes § 36a-701b (24-month credit monitoring for SSN)
- HIPAA Breach Notification Rule, 45 CFR §§ 164.400–414; HHS/OCR guidance
- FTC Health Breach Notification Rule, 16 CFR Part 318 (amended 2024)
- FTC GLBA Safeguards Rule, 16 CFR Part 314 (FTC notification eff. May 2024)
- Australia Privacy Act 1988 (Cth), Part IIIC; Privacy and Other Legislation Amendment
  Act 2024 (eff. December 10, 2024); OAIC Data Breach Preparation and Response Guide
- FTC Data Breach Response Guide for Business (ftc.gov)
- IAPP US State Data Breach Notification Law Matrix; Perkins Coie 50-State Security
  Breach Notification Chart [VERIFY current editions]

Positioned as the individual-communications complement to
`legalcode-breach-regulatory-notification-drafter` and downstream from
`legalcode-breach-response-checklist` within the Legalcode breach skill family.

All statutory and regulatory references carry hallucination risk and must be independently
verified against current official sources by qualified legal counsel before any notice is sent.
