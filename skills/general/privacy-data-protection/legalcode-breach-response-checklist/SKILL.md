---
name: legalcode-breach-response-checklist
description: 'Given breach details, generate actionable checklists covering notification deadlines per
  jurisdiction, content requirements, recipient authorities, individual notifications, safe harbors, credit
  monitoring, and filing procedures across GDPR, US state laws, UK GDPR, Canada, Australia, Brazil, Singapore,
  Japan, and sector regulations (HIPAA, GLBA, SEC, FCC, CIRCIA, NY DFS, NIS2). Use when you are IN the
  middle of a breach response and need to know: what to do NOW, who to notify, by when, with what content,
  and how to document it.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Given breach details, generate actionable checklists covering notification deadlines per jurisdiction, content requirements, recipient authorities, individual notifications, safe harbors, credit monitoring, and filing procedures across GDPR, US state laws, UK GDPR, Canada, Australia, Brazil, Singapore, Japan, and sector regulations (HIPAA, GLBA, SEC, FCC, CIRCIA, NY DFS, NIS2). Use when you are IN the middle of a breach response and need to know: what to do NOW, who to notify, by when, with what content, and how to document it. Produces a time-ordered critical path with the earliest-deadline-first sequencing across all applicable jurisdictions. Complements legalcode-breach-severity-assessment (upstream: is the breach notifiable?), legalcode-us-breach-notification-triage (upstream: US state obligations), and legalcode-breach-regulatory-notification-drafter (downstream: draft the actual notices). Jurisdiction-agnostic wrapper that integrates the full Legalcode breach skill family into a single operational response package.


# Legalcode Breach Response Checklist

> **Disclaimer**: This skill provides a framework for AI-assisted breach response planning.
> It does not constitute legal advice. All outputs must be reviewed by qualified legal counsel
> licensed in the relevant jurisdiction(s) before any notification is sent. Laws and regulator
> guidance change frequently — in particular, breach notification deadlines, AG thresholds, and
> sector regulations are amended on a rolling basis. Any legal reference cited from memory
> carries hallucination risk; verify against authoritative sources before relying on it. Missed
> or defective breach notifications carry significant regulatory, litigation, and reputational
> consequences — when in doubt, notify early and notify correctly.

---

## Purpose and Scope

This skill generates jurisdiction-by-jurisdiction breach response checklists for legal,
privacy, and incident response teams operating under time pressure.

**Covers:**

- Integrated deadline timeline — earliest-deadline-first sequencing across all applicable regimes
- Per-jurisdiction regulatory notification checklists: recipient authority, submission portal,
  required content, and proof-of-notification requirements
- Individual (data-subject) notification checklists: sequencing rules (regulator-first vs.
  simultaneous), required content, delivery methods, and language/accessibility requirements
- Safe harbor eligibility tracker: encryption, de-identification, and risk-threshold safe harbors
  with documentation requirements
- Credit monitoring and post-breach service obligations by jurisdiction
- AG filing threshold tracker: when AG/regulator filing is separately required and what to include
- Sector-specific overlay checklists: HIPAA, GLBA, SEC Form 8-K, FCC, CIRCIA, NY DFS 23 NYCRR 500,
  NIS2, and other sector frameworks
- Proof-of-notification documentation checklist for audit trail and regulatory defense
- Hour-by-hour critical path for the first 72 hours of breach response

**Covers (jurisdictions at creation date — 2026-03-21):**
EU (GDPR), UK (UK GDPR/ICO), United States (50 states + DC + major territories + federal sector),
Canada (PIPEDA + Quebec Law 25), Australia (Privacy Act NDB Scheme), Brazil (LGPD + ANPD Res. 15/2024),
Singapore (PDPA NDB), Japan (APPI), India (DPDP Act 2023 — pending implementing rules [VERIFY]),
New Zealand (Privacy Act 2020).

**Does not:**

- Determine whether a breach is notifiable — use `legalcode-breach-severity-assessment` first
- Map all 50 US state deadlines comprehensively — use `legalcode-us-breach-notification-triage`
- Draft the actual regulatory notification documents — use `legalcode-breach-regulatory-notification-drafter`
- Perform forensic root-cause analysis
- Provide legal advice or replace qualified counsel
- Guarantee regulatory outcome

**Position in the Legalcode Breach Skill Family:**

```
legalcode-breach-severity-assessment
  ↓  (is it notifiable? who must be notified? when does the clock start?)
legalcode-breach-response-checklist  ← THIS SKILL
  ↓  (what to do, by when, to whom, with what content, how to document it)
legalcode-breach-regulatory-notification-drafter
  ↓  (draft the submission-ready regulatory notices)
legalcode-us-breach-notification-triage
  ↓  (deep US state mapping — runs in parallel or prior to this skill for US incidents)
```

---

## Jurisdiction and Governing Law

This skill is multi-jurisdiction by design. The incident facts — not an agreement between
parties — determine which notification regimes apply.

**Governing principle**: Apply the **strictest applicable deadline** as the global clock driver.
When multiple regimes overlap (e.g., GDPR 72 hours, US state 30 days, HIPAA 60 days), the
earliest non-waivable deadline drives all parallel workstreams.

**Key legal authority at creation date:**

| Regime                 | Key Authority                       | Deadline Anchor                                                    | Notes                                                                                          |
| ---------------------- | ----------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| EU GDPR                | Art. 33-34; EDPB Guidelines 9/2022  | 72h from awareness                                                 | Art. 33(1) applies "where feasible" for Art. 33; Art. 34 — "without undue delay" for high-risk |
| UK GDPR + DPA 2018     | Art. 33-34 UK GDPR; ICO Guidance    | 72h from awareness                                                 | Post-Brexit UK retained regime; ICO separate from EU DPAs                                      |
| US (HIPAA)             | 45 CFR 164.400-414                  | 60 days from discovery                                             | BA must notify CE within 60 days                                                               |
| US (GLBA Safeguards)   | 16 CFR 314.15; FTC Rule             | 30 days (500+ customers)                                           | FTC notification; effective May 13, 2024                                                       |
| US (SEC Rule)          | 17 CFR 229.106; Item 1.05 Form 8-K  | 4 business days from materiality                                   | Public companies only; materiality determination required                                      |
| US (NY DFS)            | 23 NYCRR 500.17                     | 72h from determination                                             | Financial/insurance entities regulated by NYDFS                                                |
| US (FCC)               | 47 CFR Parts 64 & 54 (2024 update)  | 7 business days (500+) / 30 days (customers)                       | Telecom carriers; NLETS + FBI notification within 7 days                                       |
| US (CIRCIA)            | Forthcoming final rule [VERIFY]     | 72h (incidents) / 24h (ransom)                                     | Critical infrastructure; NPRM April 2024; final rule expected 2026                             |
| US (State laws)        | Varies; see state matrix below      | 30-72 days (most states)                                           | Confirmed via `legalcode-us-breach-notification-triage`                                        |
| Canada (PIPEDA)        | SOR/2018-64; OPC guidance           | "Feasible" (RROSH trigger); 60-day RROSH assessment                | RROSH = Real Risk of Significant Harm                                                          |
| Canada (Quebec Law 25) | Law 25 Art. 3.7-3.8 + Regulation    | "Diligently" (CAI)                                                 | Confidentiality incident reporting to CAI; 72-hour window for CAI in practice [VERIFY]         |
| Australia (NDB)        | Privacy Act s 26WH-26WL             | "Expeditiously" / 30-day assessment period                         | OAIC notification + individual notification simultaneously                                     |
| Brazil (LGPD)          | Art. 48 + ANPD Res. 15/2024 Art. 6  | 3 business days (ANPD) preliminary; 20 business days supplementary | Effective since ANPD Res. 15/2024                                                              |
| Singapore (PDPA NDB)   | PDPA s 26F-26N; Advisory Guidelines | 3 calendar days (PDPC); 30 days (assessment)                       | Significant Harm trigger                                                                       |
| Japan (APPI)           | APPI Art. 26; PPC Rules             | 30 days from becoming aware (3-5 days for large scale [VERIFY])    | Amended APPI effective April 2022                                                              |
| New Zealand            | Privacy Act 2020 ss 113-120         | "Without undue delay"                                              | Privacy Commissioner notification + individual notification                                    |
| India (DPDP)           | DPDP Act 2023 s 8                   | Rules forthcoming [VERIFY]                                         | Act in force 2023; implementing rules pending as of March 2026                                 |

[JURISDICTION-SPECIFIC] Always verify current deadlines against authoritative regulator
guidance. Regulator guidance updates frequently without legislative amendment.

---

## Interactive Clarification

This skill uses **CLARIFY** blocks at key decision points. Rather than assuming facts, the
workflow pauses and asks when the answer materially changes the legal outcome.

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

**For time-pressured breach response:** If the user provides facts in a compressed format
("We had a breach, data exfiltrated, 50,000 EU and US customers, ransomware, discovered 2 hours
ago") — extract all available facts, proceed with reasonable assumptions for any gaps, state
all assumptions explicitly, and flag missing information as items for immediate clarification
in parallel with checklist generation. **Do not block on clarification when the 72-hour clock
is running.**

---

## Workflow

### Step 1: Accept Breach Facts

Accept the incident profile in any format:

- **Structured input**: Output from `legalcode-breach-severity-assessment` (preferred)
- **Free text**: Description of the incident with available facts
- **Incident ticket**: Pasted security/IT incident report
- **Partial facts**: Whatever is known — the skill will flag gaps

Minimum facts needed to generate a useful checklist:

- Approximate number of individuals affected
- Data types compromised (contact data / financial / health / government ID / biometric / passwords)
- Geographic footprint of affected individuals (which countries/states)
- Discovery date and time (to start the clock)
- Organization type (public company, financial institution, healthcare provider, general commercial)
- Whether breach is confirmed or suspected

### Step 2: Gather Context

**⟁ CLARIFY** — Ask these questions before generating the checklist. For time-pressured
responses, accept partial answers and proceed:

1. **What has already been done?**
   - Options: Nothing yet (start from zero), Severity assessment completed (have the breach-severity output), Internal incident declared (IR process active but no external notifications yet), Some notifications already sent (need gap analysis)
   - _Why this matters_: Determines whether to generate a full checklist or a gap-completion checklist.

2. **Entity role and type**
   - Options: Controller/Business (primary obligation holder), Processor/Service Provider (must notify Controller; Controller notifies regulator), Joint Controllers (coordinate notification strategy), Healthcare entity covered by HIPAA, Financial entity covered by GLBA/NY DFS, Public company subject to SEC disclosure, Critical infrastructure operator, Telecom carrier (FCC regulated), Public sector entity
   - _Why this matters_: Role determines who files, with whom, and by when.

3. **Geographic footprint of affected individuals**
   - Options: EU only, US only, US and EU (most complex), Global (specify known jurisdictions), Unknown/to be determined
   - Prompt: "List every country and/or US state where affected individuals reside, to the extent known."
   - _Why this matters_: Drives the entire jurisdiction matrix. An EU-only breach needs GDPR + UK GDPR analysis; a US-only breach triggers state law analysis; both trigger parallel workstreams.

4. **Data type profile**
   - Options (select all that apply): Contact data only (name/email/phone), Government ID (SSN, passport, national ID), Financial account information (card numbers, account numbers), Health/medical information, Biometric data (fingerprints, facial recognition, voice), Username and password/credentials, Location data, Children's data (under 13 / under 16)
   - _Why this matters_: Data type determines which safe harbors apply, which sector overlays are triggered, and which AG notification thresholds are crossed.

5. **Breach type and safe harbor candidates**
   - Options: Ransomware/encryption (data may not have been exfiltrated), Unauthorized access with confirmed exfiltration, Accidental disclosure (wrong recipient), Insider misuse, Lost/stolen device or paper records, Third-party/vendor breach (data in processor's environment)
   - _Why this matters_: Ransomware + encrypted-at-rest data may qualify for safe harbors in many US states. Device loss without confirmed access triggers different thresholds.

6. **Sector-specific overlays**
   - Options (select all that apply): Healthcare (HIPAA applies), Financial services (GLBA applies), Securities issuer / public company (SEC disclosure), NY-regulated financial/insurance entity (NY DFS applies), Telecom carrier (FCC applies), Critical infrastructure (CIRCIA may apply), Federal contractor (DFARS/FAR obligations), Education (FERPA), None of the above
   - _Why this matters_: Sector overlays may impose shorter deadlines than baseline state/GDPR requirements.

7. **Confirmed discovery date and time (with timezone)**
   - Free text: "YYYY-MM-DD HH:MM [timezone]"
   - _Why this matters_: All deadlines are calculated from this anchor. Confirm whether this is the moment of technical detection, the moment legal/privacy was notified, or the moment the determination was made — different regimes use different clock-start events.

**⟁ CLARIFY** — Clock start ambiguity check: If the discovery date is uncertain or multiple
internal dates exist, ask:

- "What date was the security team first aware of the incident?"
- "What date was legal/privacy first notified?"
- "What date was a determination made that personal data was compromised?"
- _Use the earliest credible date for each regime that anchors to 'awareness' or 'determination'. Different regimes may use different anchors._

### Step 3: Build the Jurisdiction Matrix

Map the incident facts to every applicable notification regime. For each jurisdiction where
individuals were affected or where the organization has a legal establishment:

1. **Confirm applicability**: Is the regime triggered by the data types and individual count?
2. **Confirm clock-start event**: When does the deadline begin for this regime?
3. **Calculate the absolute deadline**: Discovery date + clock period = ISO datetime + timezone
4. **Classify deadline status**: MISSED / CRITICAL (< 24h remaining) / URGENT (24-72h remaining) / STANDARD (> 72h remaining) / NOT TRIGGERED

**Jurisdiction applicability screening:**

| Jurisdiction         | Trigger threshold                                               | Ask if unclear                                                                                                                 |
| -------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| GDPR (EU)            | Any EU resident whose personal data was breached                | Was any affected person located in an EU member state at relevant time?                                                        |
| UK GDPR              | Any UK resident affected                                        | Same — UK is now separate from EU post-Brexit                                                                                  |
| US State laws        | Residents of that state affected + PI definition match          | Is the compromised data "personal information" under that state's definition?                                                  |
| HIPAA                | PHI of any individual in any state + covered entity or BA       | Is the organization a covered entity or business associate? Is the data PHI?                                                   |
| GLBA                 | Financial customer information of 500+ customers                | Is the organization a financial institution? Were 500+ financial customers affected?                                           |
| SEC Form 8-K         | Public company; material cybersecurity incident                 | Is the organization SEC-reporting? Is the incident "material"?                                                                 |
| PIPEDA (Canada)      | Canadian residents affected + RROSH determination               | Did the breach create Real Risk of Significant Harm to Canadians?                                                              |
| LGPD (Brazil)        | Brazilian residents affected                                    | Were any Brazilian residents affected?                                                                                         |
| PDPA NDB (Singapore) | Singapore residents affected + significant harm threshold       | Is significant harm to Singapore residents likely?                                                                             |
| APPI (Japan)         | Japanese residents affected + trigger category                  | Does the compromised data fall within APPI's Special Care-Required PI or exceed 1,000 individuals? [VERIFY current thresholds] |
| NDB (Australia)      | Australian residents affected + eligible data breach assessment | Is the organization a regulated entity under the Privacy Act? Did the breach meet the eligible breach threshold?               |
| NZ Privacy Act       | NZ residents affected + serious harm likelihood                 | Is serious harm to New Zealand individuals likely?                                                                             |

### Step 4: Generate the Integrated Deadline Timeline

Produce a unified, **earliest-deadline-first** timeline showing every notification obligation,
sorted by absolute deadline. This is the critical-path view for incident response.

**Timeline format — one row per distinct notification obligation:**

| #   | Jurisdiction | Regime              | Notification Type | Recipient                      | Deadline (ISO)    | Time Remaining    | Status   | Action Owner     |
| --- | ------------ | ------------------- | ----------------- | ------------------------------ | ----------------- | ----------------- | -------- | ---------------- |
| 1   | EU           | GDPR Art. 33        | REGULATORY-DPA    | Lead Supervisory Authority     | [DATE]T[TIME][TZ] | [HH:MM remaining] | CRITICAL | Privacy/Legal    |
| 2   | US           | NY DFS 23 NYCRR 500 | REGULATORY-SECTOR | NY Dept. of Financial Services | [DATE]T[TIME][TZ] | [HH:MM remaining] | CRITICAL | Legal/Compliance |
| 3   | UK           | UK GDPR Art. 33     | REGULATORY-DPA    | ICO                            | [DATE]T[TIME][TZ] | [HH:MM remaining] | URGENT   | Privacy/Legal    |
| 4   | US           | SEC Rule            | REGULATORY-SECTOR | SEC (Form 8-K filing)          | [DATE]T[TIME][TZ] | [HH:MM remaining] | URGENT   | Legal/IR Team    |
| ... |              |                     |                   |                                |                   |                   |          |                  |

**Deadline status definitions:**

- **MISSED**: Deadline has already passed. Document why, assess penalty exposure, notify counsel immediately.
- **CRITICAL**: Less than 24 hours remaining. Drop everything — this notification must be filed NOW.
- **URGENT**: 24-72 hours remaining. Assign immediate owner; begin drafting now.
- **STANDARD**: More than 72 hours remaining. Schedule and assign owner; monitor.
- **NOT TRIGGERED**: Regime applies but threshold for notification not met; document the basis.
- **SAFE HARBOR**: Regime applies but data was encrypted/destroyed and safe harbor is claimed; document the basis.

**Hour-by-hour critical path — first 72 hours:**

Generate this sub-section for any breach where the earliest deadline is within 72 hours:

```
HOUR 0-2: Contain and document
  □ Preserve forensic evidence (before remediation)
  □ Confirm personal data involvement
  □ Identify the earliest notification deadline
  □ Convene breach response team (legal, privacy, IT, comms, executive)
  □ Open legal privilege log (if outside counsel engaged)

HOUR 2-24: Assess and prepare
  □ Confirm affected jurisdiction list
  □ Confirm data types and volume
  □ Assess safe harbor eligibility (encryption, de-identification)
  □ Begin GDPR/UK GDPR preliminary notification if 72h deadline applies
  □ Prepare materials for NY DFS filing if applicable
  □ Begin individual notification triage (who must be notified and when?)
  □ Activate vendor/processor notifications if the org is a controller

HOUR 24-48: Notify regulators (earliest-deadline-first)
  □ File EU GDPR Art. 33 notification with Lead Supervisory Authority
  □ File UK ICO notification
  □ File NY DFS notification if applicable
  □ File Brazil ANPD preliminary notification if applicable
  □ File Singapore PDPC notification if applicable

HOUR 48-72: Prepare individual and supplementary notifications
  □ Confirm timing rule for individual notifications (GDPR Art. 34 vs. state law vs. Australia)
  □ Prepare individual notice letters (in required languages)
  □ Determine AG filing thresholds and begin AG notifications where required
  □ Determine credit monitoring obligations
  □ Preserve all notification artifacts for audit trail
```

### Step 5: Safe Harbor Eligibility Analysis

Before generating notification checklists, assess whether any safe harbors apply. A valid
safe harbor claim can eliminate the notification obligation for some (or all) regimes.

**⟁ CLARIFY** — If breach type involved encrypted data at rest or in transit, ask:

- "Was the compromised data encrypted at rest at the time of the breach?"
- "What encryption standard was used? (AES-256, FIPS 197, other)"
- "Has the encryption key itself been compromised?"
- "Was the data rendered inaccessible/unusable to the attacker (ransomware scenario where attacker cannot decrypt)?"

**Safe harbor framework:**

| Regime           | Safe Harbor               | Standard Required                                                                              | Documentation Needed                                                                                   | Notes                                                                                         |
| ---------------- | ------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| US (most states) | Encryption safe harbor    | Data "encrypted" per statute (most reference NIST FIPS 197, NIST SP 800-111)                   | Written encryption policy + encryption log at breach time + confirmation key not compromised           | ~40 states; wording varies significantly [VERIFY per state]                                   |
| US HIPAA         | HIPAA Safe Harbor         | PHI encrypted per NIST 800-111 + key not compromised, OR PHI destroyed to NIST 800-88 standard | Written determination applying 4-factor low-probability test                                           | Not an automatic safe harbor — must apply 4-factor test even with encryption                  |
| GDPR (EU)        | Risk-threshold exemption  | "Unlikely to result in a risk to the rights and freedoms of natural persons" (Art. 33(1))      | Risk assessment documenting why risk is unlikely; must still maintain internal record under Art. 33(5) | NOT a safe harbor in the US sense; requires documented risk assessment                        |
| UK GDPR          | Same as EU GDPR           | Same risk threshold                                                                            | Same documentation                                                                                     | ICO guidance consistent with EDPB position                                                    |
| Canada (PIPEDA)  | No explicit safe harbor   | RROSH assessment                                                                               | Documented determination that no RROSH exists                                                          | Risk of harm threshold functions as the trigger — if no harm risk, no notification obligation |
| Australia (NDB)  | Eligible breach threshold | Must assess whether "serious harm is likely"                                                   | Documented assessment within 30 days                                                                   | Not a traditional safe harbor; the harm assessment determines notification                    |
| GDPR             | Pseudonymisation          | Not sufficient alone; must combine with other measures                                         | Risk assessment showing re-identification risk is negligible                                           | Pseudonymisation reduces risk but does not eliminate notification obligation                  |

**Safe Harbor Status classification:**

- **CONFIRMED**: Evidence of qualifying encryption/destruction at breach time; key not compromised; document and file non-notification record
- **CONTESTED**: Encryption existed but key may be compromised, or encryption standard unclear; obtain legal opinion before relying on safe harbor
- **INAPPLICABLE**: Data was not encrypted or de-identified at breach time; no safe harbor available
- **EVIDENCE-PENDING**: Status unknown pending forensic analysis; proceed as if notification required while investigation continues

**Documenting safe harbor claims:**

For each safe harbor claimed, prepare:

```
SAFE HARBOR DETERMINATION RECORD
Regime: [e.g., California Civ. Code § 1798.82(g)]
Determination date: [ISO date]
Data status at breach time: [Encrypted at rest using AES-256 / FIPS 140-2 validated module]
Evidence: [Encryption policy (version X); encryption logs; key management confirmation]
Key compromise assessment: [No — HSM logs confirm key not accessed]
Safe harbor claim: CONFIRMED
Authorized by: [Name, title]
Counsel review: [Name, date]
```

### Step 6: Per-Jurisdiction Regulatory Notification Checklists

For each TRIGGERED regime, generate a checklist in this format. Generate one checklist
block per regime.

---

#### GDPR (EU) — Article 33 Supervisory Authority Notification

**Deadline:** 72 hours from awareness (where feasible; document reasons for delay beyond 72h)
**Clock start:** When the organization (controller) became aware of the breach
**Recipient:** Lead Supervisory Authority (LSA) — the DPA in the EU member state of the
organization's main establishment

**⟁ CLARIFY** — Lead Supervisory Authority identification:

- "Where is your organization's EU main establishment (where central administration is, or where
  decisions about data processing purposes are made)?"
- Options: List EU member states + "No EU establishment (local SA of each affected member state)"
- _Why it matters_: Determines which single DPA to notify first under the one-stop-shop mechanism.

**Submission method:** Each DPA has its own portal or form. Key portals:

- Ireland (DPC): forms.dpc.ie
- France (CNIL): notifications.cnil.fr
- Germany (BfDI + state DPAs): varies by Bundesland [VERIFY current portal]
- Netherlands (AP): autoriteitpersoonsgegevens.nl/meldplicht-datalekken
- Sweden (IMY): imy.se/verksamhet/dataskydd/personuppgiftsincidenter
- Spain (AEPD): sedeagpd.gob.es
- [VERIFY portal URLs — these change; use each DPA's official website]

**Required content (GDPR Art. 33(3) + EDPB Guidelines 9/2022):**

```
GDPR ART. 33 NOTIFICATION CHECKLIST
□ Nature of the breach (incident type: unauthorized access / ransomware / accidental disclosure / insider)
□ Categories of personal data involved (what types: contact, financial, health, etc.)
□ Approximate number of personal data records affected
□ Approximate number of data subjects affected
□ Categories of data subjects affected (employees, customers, children, vulnerable groups)
□ Name and contact details of the Data Protection Officer (or other contact point)
□ Likely consequences of the breach (harm types: identity theft, financial loss, discrimination)
□ Measures taken or proposed to address the breach (containment, remediation)
□ Measures taken or proposed to mitigate its possible adverse effects
□ If notification is phased/supplementary: reference to prior notification date/reference number
```

**Phased notification:** If not all information is available within 72 hours, notify with
available information and supplement later. Document reason for delay in the notification.

**Cross-border coordination:** If individuals in multiple EU member states are affected,
the LSA leads the investigation and coordinates with Concerned Supervisory Authorities
(CSAs) in other member states under GDPR Art. 56. Notify LSA; LSA coordinates with CSAs.

**Individual notification trigger (Art. 34):** Assess whether the breach is "likely to result
in a high risk" to individuals. If yes, notify affected individuals "without undue delay" —
this is a separate obligation from Art. 33 regulator notification and may run in parallel.

**Internal record-keeping (Art. 33(5)):** Even when notification is NOT required (risk unlikely),
maintain an internal record documenting the breach and the basis for not notifying.

**Proof of notification required:**

- DPA portal submission receipt / reference number
- Timestamp of submission
- Supplementary notification reference numbers (if phased)
- Internal Art. 33(5) record (regardless of whether external notification was made)

---

#### UK GDPR — ICO Notification

**Deadline:** 72 hours from awareness (same structure as EU GDPR — retained Art. 33)
**Recipient:** Information Commissioner's Office (ICO)
**Submission:** ICO online reporting tool — ico.org.uk/for-organisations/report-a-breach
**Required content:** Same as GDPR Art. 33(3) above; ICO form reflects these requirements

**Post-Brexit note:** UK GDPR is separate from EU GDPR. A cross-border breach affecting both
EU and UK residents requires filing with BOTH the relevant EU LSA AND the ICO — there is no
one-stop-shop between EU and UK post-Brexit.

```
UK GDPR ICO NOTIFICATION CHECKLIST
□ Nature of the personal data breach
□ Contact details of the DPO or other contact
□ Approximate number of individuals concerned
□ Approximate number of records concerned
□ Likely consequences of the breach
□ Measures taken or proposed (including mitigation)
□ Categories and approximate number of personal data records concerned
□ Whether the breach is ongoing
□ ICO report reference number [from portal]
```

**Proof of notification required:**

- ICO portal confirmation / reference number
- Internal record if notification not made (Art. 33(5) UK equivalent)

---

#### United States — Federal Sector Overlays

Apply each overlay that is triggered based on organization type:

**HIPAA Breach Notification (45 CFR 164.400-414)**

| Notification Target                 | Deadline                               | Threshold                                                           |
| ----------------------------------- | -------------------------------------- | ------------------------------------------------------------------- |
| HHS OCR (online portal)             | 60 days from discovery                 | All breaches of unsecured PHI affecting 500+ individuals in a state |
| HHS OCR (annual log)                | Within 60 days after calendar year end | Breaches affecting < 500 individuals per state                      |
| Affected individuals                | 60 days from discovery                 | All breaches of unsecured PHI                                       |
| Media (prominent outlets)           | 60 days from discovery                 | Breaches affecting 500+ individuals in a state                      |
| Business Associate → Covered Entity | 60 days from BA's discovery            | BA must notify CE; CE then has the 60-day clock                     |

```
HIPAA NOTIFICATION CHECKLIST
□ Determine whether breach involves "unsecured PHI" (encrypted per NIST 800-111 = safe harbor)
□ Apply 4-factor low-probability assessment EVEN IF encrypted (document determination)
□ Determine number of affected individuals per state
□ Prepare individual notice (HITECH §13402(f) content requirements):
   □ Brief description of the breach
   □ Description of types of unsecured PHI involved
   □ Steps individuals should take to protect themselves
   □ Brief description of what entity is doing to investigate / mitigate / prevent
   □ Contact procedures for individuals to ask questions
□ File with HHS OCR via hhs.gov/ocr/privacy/hipaa/administrative/breachnotificationrule/brinstruction.html
□ Preserve all notification artifacts
□ If covered entity notified by business associate: track BA notification dates
```

**GLBA Safeguards Rule (16 CFR 314.15 — effective May 13, 2024)**

```
GLBA SAFEGUARDS NOTIFICATION CHECKLIST
□ Confirm applicability: organization is a "financial institution" under GLBA
□ Confirm threshold: 500 or more customers affected
□ Notify FTC via FTC Safeguards Rule Breach Notification portal: ftc.gov/safeguards
□ Deadline: 30 days from discovery
□ Required content:
   □ Name and contact of the notifying institution
   □ Description of the breach (type, date of discovery, dates of occurrence if known)
   □ Number of customers affected
   □ Description of information involved
   □ Whether law enforcement was notified and if so, whether to delay notification
□ Note: GLBA rule requires FTC notification only — does NOT supersede state breach laws;
   check whether state law also requires consumer notification and at what timeline
```

**SEC Cybersecurity Disclosure Rule (17 CFR 229.106; Item 1.05 Form 8-K)**

```
SEC FORM 8-K NOTIFICATION CHECKLIST
□ Confirm applicability: organization is an SEC-reporting company
□ Make materiality determination: Is the incident material to the organization?
   □ Materiality assessed under general securities law standard: would a reasonable investor
     consider this information important in making an investment decision?
   □ Document the materiality analysis (date, participants, conclusion, rationale)
□ Deadline: 4 business days from materiality determination (not from discovery)
□ Required content (Item 1.05):
   □ Material aspects of the nature, scope, and timing of the incident
   □ Material impact or reasonably likely material impact on the registrant
□ Note: SEC may grant delay if DOJ/FBI certify that disclosure would impede national security
   or law enforcement investigation
□ File via EDGAR; coordinate with investor relations and general counsel
□ Coordinate with annual disclosure obligations (Item 106 of Reg S-K)
```

**NY DFS 23 NYCRR 500.17**

```
NY DFS NOTIFICATION CHECKLIST
□ Confirm applicability: organization holds a NY DFS license (banking, insurance, mortgage)
□ Deadline: 72 hours from determination that a "Cybersecurity Event" occurred
□ Notify NY DFS: cybersecurity@dfs.ny.gov + portal.dfs.ny.gov
□ Content: Notice that event occurred; detailed report within 90 days
□ Coordinate with NY Attorney General breach notification (separate obligation)
□ Annual certification of compliance (Part 500.17(b))
```

**FCC Telecom Breach Rules (47 CFR Parts 64 & 54 — 2024 update)**

```
FCC NOTIFICATION CHECKLIST (Telecom carriers only)
□ Confirm applicability: organization is a telecom carrier subject to FCC jurisdiction
□ Notify FBI and Secret Service via NLETS within 7 business days of breach affecting 500+
□ Notify FCC via portal within 7 business days
□ Notify affected customers within 30 days
□ Content: Nature of breach, data affected, customer impact, remediation steps
□ Determine whether state PUC has separate notification requirements [VERIFY per state]
```

**CIRCIA (Critical Infrastructure) — [VERIFY: Final rule pending as of March 2026]**

```
CIRCIA NOTIFICATION CHECKLIST [CHECK CURRENCY — Final Rule Expected 2026]
□ Confirm applicability: organization operates critical infrastructure (16 designated sectors)
□ Report covered cyber incident to CISA within 72 hours of reasonable belief
□ Report ransom payment to CISA within 24 hours of payment
□ Reporting portal: CISA Cyber Incident Reporting Portal [VERIFY current portal]
□ Preserve incident data as required by CIRCIA rules
□ Note: CIRCIA may have sector-specific rules via sector risk management agencies
```

---

#### United States — State Law Notifications

**⟁ CLARIFY** — For US state notifications, ask:

- "Has `legalcode-us-breach-notification-triage` already been run for this incident?"
- If YES: Import the state-by-state output and generate per-state checklists from it.
- If NO: Use the abbreviated state matrix below for the most common states. Run `legalcode-us-breach-notification-triage` for comprehensive 50-state coverage.

**Abbreviated US state deadline reference (most common/restrictive states):**

| State         | Deadline                                     | AG Threshold                                             | Credit Monitoring               | Safe Harbor                    | Notes                                                                        |
| ------------- | -------------------------------------------- | -------------------------------------------------------- | ------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- |
| California    | 30 days (individuals); 15 days (AG if 500+)  | 500+ CA residents                                        | 12 months (SSN/financial)       | Encryption (rendered unusable) | Broadest PI definition; biometric, username+pwd                              |
| New York      | 30 days from discovery (individuals)         | All breaches                                             | No mandate                      | Encryption                     | NY SHIELD Act; expanded PI includes health, biometrics                       |
| Colorado      | 30 days from determination                   | 500+ CO residents                                        | 12 months (SSN-based)           | Encryption (NIST standard)     | Private right of action; NIST Framework safe harbor                          |
| Florida       | 30 days                                      | 500+ FL residents                                        | No mandate                      | Encryption                     | Up to $500,000 in civil penalties for violations                             |
| Texas         | 60 days (individuals); 30 days (AG if 250+)  | 250+ TX residents                                        | No mandate                      | Encryption                     | AG threshold triggers separate filing                                        |
| Massachusetts | "Expeditiously" / without unreasonable delay | All breaches (AG + OCABR)                                | 18 months (SSN/financial)       | Encryption                     | No explicit deadline; AG filed for ALL breaches; strictest credit monitoring |
| Illinois      | "Expeditiously"                              | All breaches                                             | No mandate                      | Encryption                     | BIPA applies separately for biometric data                                   |
| Washington    | "Expeditiously" / in most expedient manner   | 500+ WA residents or all if law enforcement delay lifted | No mandate                      | Encryption                     | My Health MY Data Act (2024) adds health-specific requirements               |
| Connecticut   | 60 days                                      | 500+ CT residents                                        | 24 months (identity theft data) | Encryption                     | Strictest credit monitoring duration                                         |
| Delaware      | 60 days                                      | 500+ DE residents                                        | 12 months (SSN-based)           | Encryption                     |                                                                              |
| DC            | 30 days                                      | 50+ DC residents                                         | 18 months (SSN/financial)       | Encryption                     | Private right of action                                                      |
| Puerto Rico   | 10 days (DACO)                               | All breaches                                             | No mandate                      | [VERIFY]                       | DACO public announcement within 24 hours if 1,000+                           |

**For each affected US state, generate a checklist:**

```
[STATE] STATE NOTIFICATION CHECKLIST
□ Confirm affected [STATE] residents and PI type (match state PI definition)
□ Confirm PI type matches state breach definition (check if breach definition requires
   unauthorized "acquisition" vs. "access" — states differ)
□ Determine clock-start event for this state (discovery vs. determination)
□ Calculate deadline: [DATE]
□ Individual notification:
   □ Method: First-class mail preferred; electronic if prior consent
   □ Substitute notice available if >$[threshold] cost or >$[threshold] persons: website posting + statewide media
   □ Content: [See state-specific requirements below]
□ AG notification: [Required if > X persons] → File with [STATE AG] within [Y] days
□ Credit monitoring: [Required/Not Required — duration: X months]
□ Safe harbor assessment: [Encryption safe harbor applies? Standard: FIPS 197?]
□ Proof of notification: [Affidavit / portal submission / email confirmation]
```

**Standard individual notice content (most US states require these elements):**

```
US INDIVIDUAL NOTIFICATION CONTENT CHECKLIST
□ Description of the incident (in plain language)
□ Types of personal information involved
□ Date(s) of breach (or estimated date range)
□ Date of discovery by the organization
□ What the organization is doing in response (investigation, security improvements)
□ Steps individuals can take to protect themselves (credit freeze, credit monitoring sign-up)
□ Contact information for the organization (toll-free number, address, website)
□ [If SSN involved] Offer of credit monitoring services (duration varies by state)
□ [If financial data] Recommend checking account statements; contact financial institution
□ [If healthcare data] Contact healthcare providers; monitor for fraudulent claims
□ Written in plain language (plain-language requirement varies by state)
□ [CA: Specific format requirements if > 500 CA residents — notify CA AG within 15 days]
```

---

#### Canada — PIPEDA (SOR/2018-64)

```
PIPEDA BREACH NOTIFICATION CHECKLIST
□ Confirm applicability: breach of security safeguards involving personal information; RROSH
   (Real Risk of Significant Harm) determination
□ RROSH factors: sensitivity of information, probability of misuse, number of individuals affected
□ Notify Office of the Privacy Commissioner (OPC): priv.gc.ca/en/report-a-concern/report-a-privacy-breach
□ Deadline: "As soon as feasible" after RROSH determination — OPC interprets as no unreasonable delay
□ OPC report required content (SOR/2018-64 s.3-8):
   □ Organization name and contact details
   □ Description of circumstances of breach
   □ Day or period of breach (if known)
   □ Personal information involved
   □ Number of affected individuals
   □ Whether law enforcement was notified
   □ Measures taken to reduce risk of harm
   □ Measures taken to notify affected individuals
□ Individual notification: required if RROSH; notify "as soon as feasible"
□ Individual notice content: description of breach, circumstances, time/period, PI involved,
   steps to reduce harm, organization's steps to reduce risk, complaint rights, contact details
□ Maintain breach records for minimum 24 months
□ Quebec Law 25 overlay: if Quebec residents affected, also notify CAI (Commission d'accès
   à l'information) — separate obligation from PIPEDA
```

**Quebec Law 25 — CAI Notification:**

```
QUEBEC LAW 25 NOTIFICATION CHECKLIST
□ Confirm applicability: confidentiality incident affecting personal information of Quebec residents
□ Serious injury assessment (analogous to RROSH)
□ Notify CAI: ai.gouv.qc.ca/signalement-dun-incident-de-confidentialite
□ Deadline: "Diligently" — CAI expects prompt notification; coordinate with OPC notification
□ Notify affected individuals if serious injury likely
□ Maintain incident register
```

---

#### Brazil — LGPD + ANPD Resolution 15/2024

```
BRAZIL LGPD NOTIFICATION CHECKLIST
□ Confirm applicability: personal data of Brazilian residents involved; serious risk to data subjects
□ Notify ANPD: gov.br/anpd → reporting portal
□ Preliminary notification deadline: 3 business days from discovery of breach (ANPD Res. 15/2024 Art. 6)
□ Supplementary notification deadline: 20 business days from discovery (full details)
□ Preliminary notification required content (Art. 6):
   □ Data controller identification
   □ Description of breach (date, categories of data, approximate number of individuals)
   □ Data categories involved
   □ Technical and administrative measures implemented
   □ Contact details of DPO
□ Supplementary notification content (Art. 9 + Annex):
   □ Full description of breach circumstances
   □ Identification of affected individuals / categories
   □ Consequences and risks to individuals
   □ Remediation measures adopted and planned
   □ Impact assessment
□ Individual notification: required if serious risk; "within a reasonable time"
□ Content: nature of compromised data, affected individuals, technical measures adopted
□ Language: Portuguese [JURISDICTION-SPECIFIC]
```

---

#### Australia — Privacy Act NDB Scheme

```
AUSTRALIA NDB NOTIFICATION CHECKLIST
□ Confirm applicability: organization is covered by the Privacy Act (annual turnover > AUD $3M,
   or health service provider, or credit reporting body, etc.)
□ Eligible data breach assessment: expeditiously; must conclude within 30 days of suspicion
□ If eligible breach confirmed (serious harm likely): notify OAIC + affected individuals simultaneously
□ Notify OAIC: oaic.gov.au/privacy/notifiable-data-breaches/report-a-data-breach
□ Deadline: "As soon as practicable" after confirming eligible breach
□ OAIC statement required content (Privacy Act s 26WK):
   □ Identity and contact details of entity
   □ Description of eligible data breach
   □ Kinds of information involved
   □ Recommendations: steps individuals should take in response
□ Individual notification: same content as OAIC statement; notify "as soon as practicable"
□ Substitute notice available (if impractical to notify individuals): publish on website prominently
□ Consider parallel state/territory obligations for public sector entities (NSW, VIC, QLD)
□ Health information: may also trigger specific health privacy legislation obligations
```

---

#### Singapore — PDPA Notification Breach (NDB) Rules

```
SINGAPORE PDPA NOTIFICATION CHECKLIST
□ Confirm applicability: organization is a Singapore organization handling personal data;
   significant harm to affected individuals is likely
□ Significant harm categories: financial harm; physical, psychological, reputational harm;
   identity theft; discrimination; bodily harm; adverse employment action
□ Notify PDPC: go.gov.sg/notify-pdpc (if notifiable)
□ Deadline: 3 calendar days from determining breach is notifiable (PDPA s 26F)
□ Assessment period: 30 days from becoming aware of potential notifiable breach
□ PDPC notification content:
   □ Description of the personal data breach
   □ Date(s) and time of breach
   □ Number of individuals affected
   □ Types of personal data involved
   □ Likely consequences of breach
□ Individual notification: required if significant harm is likely; notify "as soon as practicable"
□ Language: English (Singapore's official language of business/regulation) [JURISDICTION-SPECIFIC]
```

---

#### Japan — APPI Article 26 Notification

```
JAPAN APPI NOTIFICATION CHECKLIST
□ Confirm applicability: operator handling personal information of Japan residents;
   breach falls within mandatory report categories (sensitive PI, unauthorized access, 1,000+ individuals,
   or may lead to significant economic damage) [VERIFY current threshold and category list]
□ Notify PPC (Personal Information Protection Commission): ppc.go.jp
□ Deadline: 30 days from becoming aware; for large-scale breaches (>1,000 individuals or
   involving sensitive PI): 30 days but in practice PPC expects earlier notification [VERIFY]
□ Phased notification: preliminary report "without delay" + formal report within 30 days
□ Report content:
   □ Outline of the breach
   □ Type and approximate number of individuals affected
   □ Cause of breach
□ Individual notification: required; notify "without delay"
□ Language: Japanese [JURISDICTION-SPECIFIC]
□ Coordinate with any sector-specific overlays (banking: FSA, health: MHLW) [VERIFY]
```

---

#### New Zealand — Privacy Act 2020

```
NEW ZEALAND NOTIFICATION CHECKLIST
□ Confirm applicability: organization subject to NZ Privacy Act 2020; breach is a "notifiable
   privacy breach" — serious harm to individual is likely
□ Notify Privacy Commissioner: privacy.org.nz → Notify a Privacy Breach
□ Deadline: "Without undue delay" after becoming aware
□ Notification content:
   □ Nature of the privacy breach
   □ Name of individual(s) affected (or description if impractical)
   □ Information that was breached
   □ Actions taken or to be taken to address the breach
   □ Whether serious harm is likely and why
□ Individual notification: required if serious harm is likely (s 115)
□ Harm types: physical safety; significant financial loss; significant psychological harm;
   discrimination; significant reputational damage; significant adverse employment or education consequences
```

### Step 7: Individual Notification Checklist

After mapping regulatory notifications, determine individual (data-subject) notification
obligations. These may run concurrently with or after regulatory notifications depending
on the regime.

**Sequencing rules by regime:**

| Regime         | Individual vs. Regulatory Sequencing                                                                                 | Rule                                                                                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| GDPR           | Parallel — no explicit sequence; Art. 34 says "without undue delay" (not after Art. 33)                              | Notify individuals as soon as the "high risk" determination is made; do not delay because regulator was notified first |
| UK GDPR        | Same as EU GDPR                                                                                                      | Same                                                                                                                   |
| HIPAA          | Individual notification within 60 days (same window as HHS)                                                          | No sequencing requirement between HHS and individual notification                                                      |
| US States      | Varies; most require individual notification within the state deadline; AG notification concurrent                   | Check each state's statute — some require AG notice before or concurrent with individual notice                        |
| Canada PIPEDA  | Notify affected individuals as soon as feasible after RROSH determination; concurrent with or after OPC notification | Do not delay individual notification while OPC assessment is pending                                                   |
| Australia NDB  | Notify individuals "as soon as practicable" after eligible breach confirmed — concurrent with OAIC                   | Simultaneous notification to OAIC and individuals is expected                                                          |
| Singapore PDPA | Notify individuals as soon as practicable after determining breach is notifiable                                     | May follow or concurrent with PDPC notification                                                                        |

**Individual notification delivery requirements:**

| Delivery Method                     | When Available                                             | Notes                                                                                                    |
| ----------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Direct written notice (mail)        | Primary method for most regimes                            | Most US states and GDPR prefer direct written notice                                                     |
| Electronic notice (email)           | If individual has agreed to electronic communications      | Do not send breach notices by email if email account itself was compromised                              |
| Telephone                           | Some regimes permit as supplement                          | Not sufficient alone for most regimes                                                                    |
| Substitute notice (website + media) | When mailing list is unavailable OR cost exceeds threshold | US: Threshold varies by state (typically $250,000 or 500,000 persons); must post prominently for 90 days |
| Media (press release/newswire)      | Specific states require media notice                       | CA, FL, MA require media coverage if 500+ affected in state                                              |

**Language and accessibility:**

| Requirement                 | Jurisdictions                                          | Notes                                                                                         |
| --------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Plain language (generally)  | All jurisdictions                                      | Most statutes require notices to be written in "plain language" understandable to a layperson |
| Specific language (Spanish) | California                                             | CA may require Spanish translation depending on customer base [VERIFY]                        |
| Multiple languages          | EU member states with non-English speaking populations | GDPR does not specify language; member state DPAs may expect local language                   |
| ADA/accessibility           | US                                                     | Digital notices must be accessible under ADA [VERIFY per state]                               |
| Portuguese                  | Brazil (LGPD)                                          | Required for Brazilian individuals                                                            |
| Japanese                    | Japan (APPI)                                           | Required for Japanese individuals                                                             |

```
INDIVIDUAL NOTIFICATION CONTENT CHECKLIST (Universal)
□ Nature of the breach (what happened — plain language description)
□ Date of breach (or estimated date range if not known precisely)
□ Types of personal data involved (be specific — "name and email address" not just "contact data")
□ What individuals can do to protect themselves (actionable steps)
□ Organization's response (what you are doing: investigation, security improvements, credit monitoring)
□ Contact for questions (toll-free telephone; dedicated breach response email; physical address)
□ [If SSN/financial data] Explicit information about credit monitoring or credit freeze options
□ [US states requiring it] Credit monitoring enrollment instructions (website, code, how to enroll)
□ [GDPR/UK GDPR] Rights of individuals under data protection law (right to complain to regulator)
□ DPO or privacy contact details (GDPR/UK GDPR requirement)
□ Whether a formal regulatory notification was made (some regimes require this disclosure)
```

### Step 8: Credit Monitoring and Post-Breach Service Obligations

Assess credit monitoring obligations. These may be:

- **Legally mandated** (some US states require it)
- **Strongly expected** (regulatory guidance without strict mandate)
- **Good practice** (not required but industry standard to offer)

**Credit monitoring mandate matrix (US):**

| State         | Mandate                                                                 | Trigger                                                                 | Duration  | Notes                                                      |
| ------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------- | ---------------------------------------------------------- |
| California    | Mandatory                                                               | SSN, financial account, medical, insurance, biometric, or government ID | 12 months | Must provide at no cost to individual                      |
| Massachusetts | Mandatory                                                               | SSN or financial account                                                | 18 months | Among the strictest; monitor for identity theft and credit |
| Colorado      | Mandatory                                                               | SSN or financial information                                            | 12 months | Must offer credit monitoring at no cost                    |
| Connecticut   | Mandatory                                                               | SSN                                                                     | 24 months | Longest mandatory duration in the US                       |
| Delaware      | Mandatory                                                               | SSN or financial account                                                | 12 months |                                                            |
| Illinois      | Mandatory                                                               | SSN, financial account, or state ID                                     | 12 months |                                                            |
| Maryland      | Mandatory                                                               | SSN                                                                     | 12 months |                                                            |
| New York      | Best practice strongly recommended; not strictly mandated by SHIELD Act | —                                                                       | —         | Consider offering 12-24 months                             |
| DC            | Mandatory                                                               | SSN or financial account                                                | 18 months |                                                            |

[VERIFY] The above list reflects the law as understood at creation date (March 2026). Credit
monitoring mandates are an evolving area of state law; verify against current statutes before
relying on this matrix.

**Non-US post-breach services:**

| Jurisdiction | Obligation                                                                                        | Notes                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| EU (GDPR)    | No mandatory credit monitoring; individual notification must include recommended protective steps | Consider offering credit monitoring as part of "measures to mitigate adverse effects" under Art. 34(2) |
| UK           | Same as EU                                                                                        | ICO guidance recommends informing individuals of steps to protect themselves                           |
| Australia    | No mandatory credit monitoring; notification must include "recommended steps"                     | Consider partnering with credit reporting bodies for affected individuals                              |
| Canada       | No mandatory credit monitoring; notification must include remediation steps                       | OPC expects practical protective guidance                                                              |

**Credit monitoring implementation checklist:**

```
CREDIT MONITORING IMPLEMENTATION CHECKLIST
□ Confirm which states impose mandatory credit monitoring obligations
□ Select credit monitoring provider (Experian, Equifax, TransUnion, or specialized breach
   response services such as Kroll, Epiq, Cyberscout, TransUnion TLO)
□ Negotiate monitoring period and scope (1-bureau vs. 3-bureau; identity theft insurance)
□ Obtain enrollment codes or dedicated enrollment URL
□ Include enrollment instructions in individual notice letter
□ Set up dedicated toll-free hotline for enrollment assistance
□ Track enrollment rates and maintain records
□ Note: Credit monitoring cannot be conditioned on arbitration agreement or release
□ Duration: comply with strictest applicable state law (Connecticut: 24 months)
```

### Step 9: Proof-of-Notification Documentation Tracker

For each notification made, document the following. This audit trail is essential for
regulatory defense, litigation, and insurance claims.

**Master Notification Log:**

```yaml
notification_log:
  incident_id: "[UNIQUE INCIDENT IDENTIFIER]"
  discovery_date: "[ISO datetime + timezone]"

  notifications:
    - id: "NOTIF-001"
      regime: "GDPR Art. 33"
      recipient: "Irish Data Protection Commission (DPC)"
      submission_date: "[ISO datetime + timezone]"
      submission_method: "Online portal (forms.dpc.ie)"
      confirmation_reference: "[Portal reference number]"
      submitted_by: "[Name, title]"
      counsel_reviewed: "[Name, date]"
      supplementary_notification:
        required: true/false
        due_date: "[ISO date]"
        submitted_date: "[ISO datetime]"

    - id: "NOTIF-002"
      regime: "UK GDPR Art. 33"
      recipient: "ICO"
      submission_date: "[ISO datetime + timezone]"
      submission_method: "ICO online breach reporting tool"
      confirmation_reference: "[ICO reference number]"
      submitted_by: "[Name, title]"
      counsel_reviewed: "[Name, date]"

    - id: "NOTIF-003"
      regime: "US State — California"
      recipient: "Individuals (50,234 CA residents)"
      submission_date: "[ISO datetime]"
      submission_method: "First-class mail (mailed [date])"
      confirmation: "Mailing service affidavit [attached]"
      ag_notification:
        filed: true/false
        date: "[ISO date]"
        ag_reference: "[Reference number]"
      credit_monitoring:
        required: true
        duration: "12 months"
        provider: "[Provider name]"
        enrollment_code: "[Code]"
        instructions_in_notice: true

    # Add entry for each notification obligation

  safe_harbor_claims:
    - regime: "[State/Regime]"
      status: "CONFIRMED / CONTESTED / INAPPLICABLE"
      basis: "[Encryption standard, documentation reference]"
      authorized_by: "[Name, title, date]"
      counsel_opinion: "[Yes/No, date if yes]"

  non_notification_records:
    # For GDPR Art. 33(5) — even when no external notification was made
    - regime: "[GDPR]"
      determination: "[Risk unlikely to individual rights — basis for non-notification]"
      date: "[ISO date]"
      authorized_by: "[Name, title]"
      record_location: "[File path / DMS reference]"
```

### Step 10: Quality Verification

Before delivering the checklist, run the following quality checks:

1. **MISSED deadline check**: If any deadline shows status MISSED, escalate immediately.
   Do not deliver a complete checklist — flag MISSED items in a RED alert box at the top
   of the output.

2. **Jurisdiction coverage check**: Confirm every country/US state mentioned in the affected-
   individual geographic footprint has been addressed. Flag any jurisdiction not analyzed.

3. **Sector overlay check**: Confirm all applicable sector overlays (HIPAA, GLBA, SEC, etc.)
   have been included. A missed HIPAA obligation is a per-violation regulatory exposure.

4. **Safe harbor documentation check**: If any safe harbor is claimed (CONFIRMED status),
   verify that the documentation requirements checklist has been generated.

5. **Citation Quality Gates** (run silently):

   | Gate           | Rule                                                                                              | Fail Action                                                   |
   | -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
   | **Source**     | Every deadline and content requirement cites a specific statute, regulation, or guidance document | Add citation or mark [VERIFY]                                 |
   | **Format**     | All citations follow consistent format                                                            | Fix format                                                    |
   | **Currency**   | Deadlines and content requirements verified against law as of March 2026                          | Flag [CHECK CURRENCY] for any provision that may have changed |
   | **Domain**     | No jurisdiction's requirements are applied to another jurisdiction                                | Remove or flag jurisdictional bleed                           |
   | **Confidence** | Uncertainty explicitly stated                                                                     | Add confidence qualifier                                      |

6. **Self-Interrogation for MISSED and CRITICAL items** — For any item with status MISSED
   or CRITICAL:

   **Pass 1 — Legal Chain Integrity**: Is the deadline calculation correct? Is the clock-start
   event identified correctly for this regime? Is the regime actually triggered by these facts?

   **Pass 2 — Completeness**: Have all the notification targets for this regime been identified?
   (E.g., HIPAA requires HHS + individual + possibly media — are all three captured?)

   **Pass 3 — Challenge**: Is there any arguable basis for claiming this obligation is not
   triggered, or that additional time is available? What is the best good-faith counterargument?

7. **Confidence Scoring** — Assign a confidence level to each material deadline:

   | Level        | Range     | Meaning                                                         | Action                                     |
   | ------------ | --------- | --------------------------------------------------------------- | ------------------------------------------ |
   | **Definite** | 0.95-1.0  | Settled law, confirmed deadline                                 | State with confidence                      |
   | **High**     | 0.80-0.94 | Strong authority, minor ambiguity                               | State with brief caveat                    |
   | **Probable** | 0.60-0.79 | Good arguments but some uncertainty                             | State with reasoning and contra-indicators |
   | **Possible** | 0.40-0.59 | Genuinely uncertain (pending legislation, conflicting guidance) | Flag for counsel review                    |
   | **Unlikely** | 0.0-0.39  | Weak basis, speculative                                         | Mark [UNCERTAIN]                           |

---

## Severity and Status Classification

### Notification Obligation Status

| Status                 | Definition                                            | Required Action                                                                                                                      |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **MISSED**             | Deadline has already passed                           | Escalate immediately; assess penalty exposure; notify counsel; document reason for delay; consider voluntary disclosure to regulator |
| **CRITICAL**           | Deadline expires within 24 hours                      | All other work pauses; assign immediate owner; file notification now                                                                 |
| **URGENT**             | Deadline expires within 24-72 hours                   | Assign dedicated owner; begin drafting immediately; target 12-hour preparation buffer                                                |
| **STANDARD**           | Deadline expires after 72 hours                       | Schedule; assign owner; monitor for changes in incident scope                                                                        |
| **NOT TRIGGERED**      | Regime applies but threshold not met                  | Document why (number of individuals, data type mismatch, encryption safe harbor); maintain record                                    |
| **SAFE HARBOR**        | Encryption or de-identification safe harbor confirmed | Document per safe harbor requirements; maintain non-notification record                                                              |
| **PENDING ASSESSMENT** | Regime may apply; awaiting facts to determine         | Proceed as if triggered; reassess when facts confirmed                                                                               |

### Safe Harbor Status

| Status               | Definition                                                                | Required Action                                                       |
| -------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **CONFIRMED**        | Qualifying encryption or safe harbor evidence exists; key not compromised | Document per checklist; file non-notification record; retain evidence |
| **CONTESTED**        | Encryption may not meet standard, or key potentially compromised          | Obtain legal opinion; do not rely on safe harbor until confirmed      |
| **INAPPLICABLE**     | Data was not encrypted at breach time; no qualifying safe harbor          | Proceed with notification obligation                                  |
| **EVIDENCE-PENDING** | Forensic analysis ongoing; safe harbor status unknown                     | Proceed as if notification required; reassess when forensics complete |

---

## Prioritization Framework

### Tier 1 — Act Immediately (Within Hours)

Issues that cannot wait for further analysis:

- Any notification deadline with status MISSED or CRITICAL
- GDPR / UK GDPR 72-hour windows (regulatory notification)
- NY DFS 72-hour notification
- Brazil ANPD 3-business-day preliminary notification
- Singapore PDPC 3-calendar-day notification
- SEC Form 8-K 4-business-day materiality disclosure
- Any HIPAA obligation when the breach affects a very large population

**Escalation path**: Legal, privacy officer, and executive team must be convened immediately.
Outside counsel should be engaged.

### Tier 2 — Act Within 72 Hours (Current Response Window)

Actions that must be completed in the current active response period:

- All regulatory notifications with URGENT status
- Individual notification preparation (letter, substitute notice plan, credit monitoring enrollment)
- Safe harbor documentation (must be complete before deadline to avoid relying on unclaimed safe harbor)
- AG filing threshold determination and preparation
- Vendor/processor notifications (if organization is a controller and processors were breached)

### Tier 3 — Act Within 30 Days (Extended Response)

Actions that are required but within standard response windows:

- US state notifications with 30-60 day deadlines (where not already URGENT/CRITICAL)
- HIPAA HHS filing
- GLBA FTC notification (30-day window)
- Canada PIPEDA + OAIC (Australia) notifications when harm assessment complete
- Credit monitoring implementation and enrollment
- Annual regulatory log submissions (HIPAA <500 affected)
- Post-incident breach register updates (Art. 33(5) GDPR internal record)
- Post-incident review and notification close-out documentation

---

## Anti-Patterns

Explicit catalogue of breach response mistakes — what NOT to do:

1. **Treating detection time as legal awareness without analysis** — Different regimes use
   different clock-start events. GDPR starts from when the controller "becomes aware" (typically
   when DPO/legal is informed, not when the firewall first flagged). US states often use "discovery"
   or "determination." Misidentifying the clock-start by 24 hours can turn a compliant notification
   into a missed deadline.

2. **Applying GDPR's 72-hour deadline to all jurisdictions** — GDPR is the shortest common
   regulatory deadline, but it applies to the supervisory authority, not to individuals. US states
   use 30-60 days for individuals. Australia uses "as soon as practicable" which can be longer.
   Rushing all notifications to 72 hours when not required can cause harm (disclosing before
   affected individuals are identified, sending inaccurate notices).

3. **Claiming encryption safe harbor without documented evidence** — The safe harbor only applies
   if the encryption is documented and verifiable at the breach time. Discovering encryption
   after the breach, or failing to confirm the key was not compromised, invalidates the safe harbor.
   Regulators regularly investigate safe harbor claims; unsupported claims result in late-notification
   penalties.

4. **Confusing the GDPR one-stop-shop with UK GDPR** — Post-Brexit, the UK is not part of the
   GDPR one-stop-shop mechanism. A breach affecting both EU and UK residents requires notifications
   to BOTH the relevant EU lead DPA AND the UK ICO. Filing with only one is a compliance failure
   for the other.

5. **Sending a single notice template to all jurisdictions** — Content requirements differ
   materially between US states, GDPR, HIPAA, and LGPD. A notice that complies with GDPR may
   lack required US state content (credit monitoring enrollment instructions, plain-language
   mandate), and vice versa. Each jurisdiction's notice must be separately reviewed and customized.

6. **Notifying individuals by email if email was compromised** — If the breach involved email
   accounts, email notification is both insecure and counterproductive. Use alternative channels
   (mail, phone, account portal notification, website posting).

7. **Missing AG notification thresholds while complying with individual notifications** — In
   states like California (500+), New York (all breaches), Massachusetts (all breaches), Florida
   (500+), and Texas (250+), the organization must file separately with the AG in addition to
   notifying individuals. AG notifications are frequently overlooked.

8. **Failing to account for credit monitoring mandates in the earliest state** — If Massachusetts
   residents are affected, 18-month credit monitoring must be offered. If Connecticut residents are
   affected, 24 months. The longest mandatory duration in any affected state sets the practical
   standard for the entire notification. Offering only 12 months to a Massachusetts resident when
   18 months is required is a compliance failure.

9. **Treating substitute notice as equivalent to direct notice** — Substitute notice (website
   posting + media) is only available when direct mailing is impractical. Using it when mailing
   would have been practicable, or without meeting the specific cost/number thresholds, does not
   satisfy the notification obligation.

10. **Notifying regulators but not individuals (or vice versa)** — GDPR requires both regulatory
    notification (Art. 33) and, where high risk, individual notification (Art. 34). These are
    separate obligations. Filing only with the supervisory authority while failing to notify high-
    risk-affected individuals is a compliance failure.

11. **Failing to maintain Art. 33(5) internal records even when not notifying** — GDPR requires
    an internal record of ALL breaches, including those where the risk is assessed as "unlikely"
    and no external notification is made. This record is audited by supervisory authorities. A
    missing internal record is itself a GDPR violation.

12. **Missing Brazil ANPD's 3-business-day preliminary notification deadline** — ANPD Resolution
    15/2024 established a 3-business-day window for preliminary notification. Many organizations
    still operate on the older (longer) expectation from pre-Res. 15 practice. This is now one of
    the shortest regulatory deadlines globally alongside GDPR's 72 hours.

13. **Underestimating Singapore's 3-calendar-day deadline** — The PDPA NDB requires PDPC
    notification within 3 calendar days (not business days) from the determination that the breach
    is notifiable. The 30-day assessment period does not delay the 3-day notification clock once
    notifiability is determined.

14. **Ignoring sector-specific obligations as "covered by state law"** — HIPAA, GLBA, SEC, and
    NY DFS are federal or NY-specific frameworks that operate in addition to (not instead of) state
    breach notification laws. A breach affecting a financial institution must comply with BOTH GLBA
    (FTC notification within 30 days of 500+ customer breach) AND applicable state laws. These do
    not preempt each other in most cases.

15. **Failing to notify in the affected individual's language** — GDPR and several EU member state
    DPAs expect notifications to individuals in the language of the affected individuals. Brazil
    requires Portuguese. Japan requires Japanese. A notice sent only in English to EU French-speaking
    individuals may not satisfy Art. 34 requirements in some DPA interpretations [VERIFY].

16. **Mixing up "discovery" and "determination" clock-start events** — Under HIPAA, the clock
    starts on "discovery" (when the covered entity knows or reasonably should have known of a
    breach). Under GDPR, it starts when the controller "becomes aware." Under most US state laws,
    it starts on "discovery" or "determination" (sometimes defined differently). These may be
    different dates; use the correct one for each regime.

17. **Underestimating the scope of CIRCIA for critical infrastructure operators** — CIRCIA, when
    finalized, will impose 72-hour cyber incident reporting and 24-hour ransom payment reporting
    obligations on covered critical infrastructure entities. Organizations in the 16 designated
    sectors should already be tracking the final rule and preparing processes [CHECK CURRENCY —
    rule expected 2026].

18. **Relying on this checklist without verifying currency** — Breach notification law changes
    constantly. Deadlines have been shortened (ANPD Res. 15/2024 shortened Brazil's window),
    AG thresholds have changed, and new sector regulations continue to emerge. Verify each
    deadline against the current statute or regulator guidance before the notification is sent.

---

## Writing Standards

Apply plain-language discipline to all notices and checklist outputs:

**For individual notices (shared directly with affected individuals):**

- Use grade 6-8 reading level where possible (Flesch-Kincaid target)
- Active voice: "Your name and email address were exposed" not "Name and email address information was exposed in the incident"
- Short sentences. One fact per sentence.
- Lead with the most important information (what happened, what data, what to do)
- Avoid legal jargon: "breach" instead of "unauthorized access event"; "your private information" instead of "personal information subject to unauthorized disclosure"
- Include specific steps, not vague guidance ("Call 1-800-XXX-XXXX to enroll in 12 months of free credit monitoring" not "protective steps are available")

**For regulatory notifications (filed with DPAs, AGs, and federal agencies):**

- Precise legal terminology matching the relevant statute and regulator form
- Complete and factual — do not minimize; regulators review for candor
- Use the regulator's preferred format and form where available
- Cite internal investigation findings accurately; avoid conclusory statements not supported by the investigation

**Quality gates before delivery:**

- [ ] All deadlines expressed as absolute ISO datetimes with timezone
- [ ] Every claim cites a specific statute or regulation (or marked [VERIFY])
- [ ] Every safe harbor claim includes documentation requirements
- [ ] No jurisdiction's requirements bleed into another jurisdiction's checklist
- [ ] Individual notice content distinguishes between regulatory requirements and best practice

---

## External Tool Integration

**With `legalcode-breach-severity-assessment` connected (upstream):**

- Import the Notification Duty Register and Unified Action Clock directly
- Use the confirmed severity classification and jurisdiction matrix as inputs to this skill
- The clock-start events and NOTIFIABLE/NOT_NOTIFIABLE determinations replace Steps 2-3 of this workflow

**With `legalcode-us-breach-notification-triage` connected (parallel):**

- For US incidents, import the full state-by-state obligation matrix
- Replace the abbreviated US state table in Step 6 with the comprehensive triage output
- Confirm credit monitoring mandates and AG filing thresholds from triage output

**With `legalcode-breach-regulatory-notification-drafter` (downstream):**

- Pass the per-jurisdiction checklist outputs to the drafter for document generation
- Reference the submission portals and content requirements identified in this skill
- Use the notification log format from Step 9 to track drafts produced by the drafter

**Without upstream/downstream skills connected:**

- Proceed with available facts
- Flag all legal conclusions with confidence scores
- Note in the Glass Box audit trail which skills were not used
- Mark all regime-specific requirements with [VERIFY] where verification against authoritative sources has not been performed

---

## Localization Notes

This skill is jurisdiction-agnostic at the framework level. When localizing for a specific
incident geography:

1. **EU member state DPAs**: Each has its own submission portal, preferred form, and sometimes
   supplementary national guidance. Always use the specific DPA's official website for submission
   instructions rather than relying on this skill's portal references, which may be outdated.

2. **US state law changes**: State breach notification statutes are amended frequently. Before
   every incident, verify current deadlines against the state attorney general's official guidance
   or current statutory text.

3. **Non-English notifications**: For Brazil (Portuguese), Japan (Japanese), and EU member states
   with non-English official languages, engage local counsel and certified translators for both
   regulatory and individual notifications.

4. **Sector-specific implementing regulations**: HIPAA, GLBA, and SEC rules have detailed
   implementing regulations and agency guidance that this skill summarizes. Always verify against
   the specific CFR provisions and agency FAQs before filing.

---

## Glass Box Audit Trail

Every output from this skill MUST include a Glass Box audit section:

```yaml
glass_box:
  skill: "legalcode-breach-response-checklist"
  version: "2026-03-21"
  incident_id: "[UNIQUE INCIDENT IDENTIFIER]"
  mode: "Generated from breach facts"

  inputs_used:
    breach_severity_assessment: "Integrated / Not integrated"
    us_breach_notification_triage: "Integrated / Not integrated"
    raw_incident_facts: "Provided by user"

  jurisdictions_analyzed:
    - "[EU GDPR — VERIFIED]"
    - "[UK GDPR — VERIFIED]"
    - "[US Federal: HIPAA / GLBA / SEC / NY DFS / FCC / CIRCIA — as applicable]"
    - "[US States: list — see triage output or abbreviated matrix]"
    - "[Canada PIPEDA + Quebec Law 25 — VERIFIED]"
    - "[Brazil LGPD + ANPD Res. 15/2024 — VERIFIED]"
    - "[Australia NDB — VERIFIED]"
    - "[Singapore PDPA NDB — VERIFIED]"
    - "[Japan APPI — VERIFIED]"
    - "[New Zealand Privacy Act 2020 — VERIFIED]"
    - "[India DPDP — [VERIFY] pending implementing rules]"

  safe_harbor_claims_evaluated: "[number]"
  safe_harbor_confirmed: "[number]"

  notifications_total: "[number]"
  notifications_missed: "[number — RED ALERT if > 0]"
  notifications_critical: "[number]"
  notifications_urgent: "[number]"
  notifications_standard: "[number]"
  notifications_not_triggered: "[number]"

  legalcode_mcp: "Connected / Not connected"
  statutory_references_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"

  self_interrogation_applied: "PASS / REVISED / [Items flagged]"

  confidence: "HIGH / MEDIUM / LOW — [rationale]"

  key_assumptions:
    - "[List all assumptions made where facts were not provided]"

  limitations:
    - "Sector-specific overlays require verification by specialized counsel (HIPAA, GLBA, SEC)"
    - "US state law summary is abbreviated — run legalcode-us-breach-notification-triage for comprehensive 50-state coverage"
    - "Portal URLs and submission addresses change frequently — verify before submission"
    - "India DPDP implementing rules had not been finalized as of March 2026 — [CHECK CURRENCY]"
    - "CIRCIA final rule had not been published as of March 2026 — [CHECK CURRENCY]"
    - "Deadlines and statutory requirements verified against law as of March 2026; verify currency before filing"

  reviewer: "AI-assisted — requires review by qualified legal counsel in all relevant jurisdictions before any notification is filed"
```

---

## Output Format Template

The final output should follow this structure:

```markdown
# Breach Response Checklist — [Incident Name/ID]

**Generated:** [ISO datetime]
**Incident discovery:** [ISO datetime + timezone]
**Analysis as of:** [ISO datetime]
**Status:** [Active response / Gap analysis / Complete]

---

## ⚠️ IMMEDIATE ALERTS

[If any deadlines are MISSED or CRITICAL — RED box with specific items and recommended actions]

---

## Integrated Deadline Timeline (Earliest-First)

[Full timeline table from Step 4]

---

## Safe Harbor Status

[Summary table of safe harbor assessments + documentation requirements]

---

## Hour-by-Hour Critical Path (First 72 Hours)

[Critical path checklist from Step 4]

---

## Regulatory Notification Checklists

### [Regime 1 — e.g., GDPR Art. 33 — DPC (Ireland)]

[Checklist block from Step 6]

### [Regime 2 — e.g., UK GDPR — ICO]

[Checklist block from Step 6]

### [Regime 3 — US States]

[Per-state checklist blocks from Step 6]

### [Sector Overlays — as applicable]

[HIPAA / GLBA / SEC / NY DFS / FCC / CIRCIA checklists as applicable]

### [Other Jurisdictions — as applicable]

[Canada / Australia / Brazil / Singapore / Japan / NZ checklists as applicable]

---

## Individual Notification Checklist

[Content checklist, delivery methods, language requirements, timing relative to regulatory notifications]

---

## Credit Monitoring and Post-Breach Services

[State-by-state mandate table + implementation checklist]

---

## AG Filing Tracker

[Table of AG filing obligations with deadlines and content requirements]

---

## Proof-of-Notification Log

[Master notification log template (YAML) from Step 9]

---

## Quality Assurance Summary

[Confidence scores for key deadlines; any [VERIFY] flags; jurisdiction coverage confirmation]

---

## Glass Box Audit Trail

[YAML audit trail from Step 10]

---

_Review required: This checklist must be reviewed by qualified legal counsel licensed in all
relevant jurisdictions before any notification is filed. Laws change; verify all deadlines,
thresholds, and content requirements against current authoritative sources._
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for the Legalcode breach skill family.
Research basis: GDPR Art. 33-34, EDPB Guidelines 9/2022 on Personal Data Breach Notification;
ICO Breach Notification Guidance; HIPAA Breach Notification Rule 45 CFR 164.400-414; GLBA
Safeguards Rule 16 CFR 314.15 (amended May 2024); SEC Cybersecurity Disclosure Rule 17 CFR
229.106; NY DFS 23 NYCRR 500; FCC data breach rules (2024 update); CIRCIA NPRM (April 2024);
PIPEDA SOR/2018-64; Quebec Law 25; LGPD Art. 48 + ANPD Res. 15/2024; PDPA NDB Rules
(Singapore); APPI Art. 26 (Japan); Privacy Act NDB Scheme (Australia); Privacy Act 2020 (NZ);
DPDP Act 2023 (India — implementing rules pending). Structural patterns adapted from
`legalcode-breach-severity-assessment`, `legalcode-us-breach-notification-triage`, and
`legalcode-breach-regulatory-notification-drafter`. Quality frameworks adapted from
`legalcode-contract-review` (reference standard).

All statutory references represent understanding as of March 2026. [VERIFY] tags mark provisions
requiring independent confirmation. [CHECK CURRENCY] tags mark provisions subject to pending
legislative or regulatory change.
