---
name: legalcode-eu-gdpr-breach-notification-operations
description: Runs the complete EU GDPR personal data breach response workflow from initial incident triage
  through post-incident remediation.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Runs the complete EU GDPR personal data breach response workflow from initial incident triage through post-incident remediation. Use when: (1) a data breach or security incident involving personal data has occurred or is suspected, (2) an organisation needs to determine whether GDPR Articles 33 or 34 notification obligations are triggered, (3) a controller or processor needs to manage the 72-hour notification clock and lead supervisory authority determination, (4) a phased or supplementary notification must be prepared under Art. 33(4), (5) an operator needs to draft the Art. 33 SA notification, Art. 34 data subject communication, or processor-to-controller notification, (6) a forensic coordination plan or post-breach mitigation playbook is required, (7) Art. 33(5) internal documentation must be produced for regulatory audit. Covers controller-only, processor-only, and hybrid scenarios. Embeds the ENISA SE severity formula (DPC × EI + CB), EDPB 01/2021 case taxonomy, cross-border one-stop-shop rules, and the Art. 34 exemptions. EU jurisdiction only (separate skill for UK GDPR/ICO). Designed as the native Legalcode replacement for imported breach-notification packs.


# Legalcode — EU GDPR Breach Notification Operations

> **Disclaimer**: This skill provides a framework for AI-assisted GDPR breach response
> analysis. It does not constitute legal advice. All notification decisions should be
> reviewed by a qualified Data Protection Officer and, where appropriate, qualified legal
> counsel licensed in the relevant jurisdiction before acting. GDPR requirements and
> supervisory authority guidance evolve; verify current applicability before relying on
> any provision described here. Statutory, case law, and enforcement references cited
> from memory carry hallucination risk — verify against authoritative sources before
> relying on them.

---

## Purpose and Scope

This skill manages the **end-to-end operational response** to a personal data breach
under EU GDPR. It runs from initial incident triage through supervisory authority
notification, data subject communication, and post-incident remediation.

**Covers:**

- Incident triage — does the event qualify as a personal data breach under Art. 4(12)?
- Controller vs. processor role determination and obligation split
- T0 clock establishment and 72-hour deadline management
- ENISA severity scoring (SE = DPC × EI + CB) with full DPC/EI/CB tables
- EDPB Guidelines 01/2021 case matching (18 reference scenarios)
- Art. 33 supervisory authority notification decision and draft
- Art. 33(2) processor-to-controller notification
- Art. 33(4) phased/supplementary notification management
- Art. 33(5) internal documentation obligation
- Art. 34 data subject communication decision and draft (including exemptions)
- Cross-border processing — lead supervisory authority determination
- Forensic coordination and evidence preservation guidance
- Tailored breach mitigation playbook
- Post-incident remediation, DPIA update, and Art. 30 records revision
- AI Act Art. 62 serious incident check (where AI systems are involved)
- Assessment override documentation with regulatory risk warnings

**Does not:**

- Cover UK GDPR / ICO breach notification (separate skill required)
- Replace legal advice or DPO professional judgment
- Cover multi-regime breach notification outside the EU (see `legalcode-breach-regulatory-notification-drafter` for US, AU, CA, BR)
- Assess GDPR compliance generally (see `gdpr-data-processing-addendum`, `legalcode-dsar-workflow-builder`, `legalcode-cross-border-transfer-assessment`)

**Related skills to chain:**

- `legalcode-breach-severity-assessment` — general multi-jurisdiction severity triage
- `legalcode-breach-regulatory-notification-drafter` — multi-regime regulator notification drafting
- `legalcode-dpa-review-and-negotiation` — reviewing Art. 28 processor agreements
- `legalcode-cross-border-transfer-assessment` — Chapter V transfer mechanism review
- `legalcode-dsar-workflow-builder` — where the breach triggers subject access requests

---

## Jurisdiction and Governing Law

**Primary**: EU GDPR — Regulation (EU) 2016/679 of the European Parliament and of the
Council of 27 April 2016, in force from 25 May 2018.

**Authoritative guidance applied:**

- EDPB Guidelines 9/2022 on personal data breach notification under the GDPR (version 2.0, adopted 28 March 2023) [VERIFY currency]
- EDPB Guidelines 01/2021 on examples regarding personal data breach notification (version 2.0, adopted 14 December 2021)
- ENISA Technical Guidelines — Recommendations for a methodology of the assessment of severity of personal data breaches (v1.0)

**Territorial scope:** GDPR applies to controllers and processors established in the EU,
and to those outside the EU that offer goods or services to data subjects in the EU or
monitor their behaviour (Art. 3). Where the controller has no EU establishment, the
one-stop-shop mechanism does not apply.

**Post-Brexit UK note:** UK-resident data subjects trigger a separate obligation to the
Information Commissioner's Office (ICO) under UK GDPR + Data Protection Act 2018. This
skill does not cover UK obligations. Where UK subjects are affected, flag the parallel
ICO obligation and advise consulting a UK-qualified practitioner.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent or filling gaps silently, the workflow pauses and asks when:

- The answer would change the legal obligation (e.g., processor vs. controller changes
  which notification track applies)
- A time-critical decision must be made immediately rather than deferred
- Ambiguous facts require the user's authoritative input
- Regulatory risk depends on context not inferable from the incident description

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked
below. If the information is already available from the incident description, skip the
question and proceed.

---

## Workflow

### Step 1: Session Initialization

**1a. Display the disclaimer and obtain acknowledgment.**

> IMPORTANT NOTICE: This system provides guidance based on GDPR Arts. 33–34, EDPB
> Guidelines 9/2022 and 01/2021, and the ENISA severity methodology. It does not
> constitute legal advice. Final notification decisions should involve your DPO and,
> where appropriate, qualified legal counsel. Do you acknowledge this and wish to proceed?

Wait for acknowledgment before proceeding.

**1b. Check emergency status.**

> Are you in a time-critical situation with fewer than 12 hours remaining on your
> notification clock?

- **Yes** → Activate EMERGENCY MODE:
  - Skip the standard question sequence
  - Accept a free-form incident description and extract all critical data points
  - Produce an immediate preliminary assessment within the first response
  - Flag: "This is a preliminary emergency assessment. A full ENISA/EDPB analysis must
    be completed within the next 48 hours. An emergency follow-up checklist is appended."
  - Proceed directly to Step 6 (ENISA Assessment) with worst-case assumptions
- **No** → Continue to Step 1c

**1c. Offer intake mode.**

> How would you like to proceed?
>
> - **Guided Mode** — I will ask questions one at a time (recommended if unsure)
> - **Fast Path** — Provide a structured or free-form incident description and I will
>   extract the facts and assess immediately

If **Fast Path**: extract the 12 data points from Step 2 and confirm before proceeding.

**Quick Decision Tree — Preliminary Triage (Experienced DPOs)**

For rapid orientation before the full workflow:

```
ENCRYPTED DEVICE LOST
├── Current encryption (AES-256 or equivalent) + key secure + stored separately + backup?
│   └── ALL YES → Likely LOW, Art. 34 exemption likely (Art. 34(3)(a)). Confirm with full assessment.
└── ANY NO → Full assessment required.

MISDIRECTED EMAIL (single recipient)
├── Recalled/deleted before read, confirmed? → YES → Likely LOW. Document under Art. 33(5).
├── Contains Art. 9 data (health/biometric/etc.)? → YES → Full assessment. Likely HIGH.
├── Contains financial data? → YES → Full assessment. Likely HIGH.
└── Simple contact data only → Likely LOW–MEDIUM. Document and assess.

RANSOMWARE
├── Exfiltration evidence? → YES → Full assessment. Likely HIGH or VERY HIGH.
├── Backup restored <24h, no exfiltration? → YES → Assess availability impact. Likely MEDIUM.
└── No backup / extended downtime → Full assessment. Likely HIGH.

PHISHING (credentials compromised)
├── Admin/privileged account? → YES → Full assessment immediately.
├── MFA in place and working? → YES → Reduced risk. Still assess.
└── Single standard account → Assess what data that account could access.
```

**Note:** The tree provides orientation only. Always complete the full ENISA assessment for the definitive classification and Art. 33(5) documentation.

---

### Step 2: Gather Incident Facts

Ask in **Guided Mode** one at a time. In **Fast Path**, extract from the user's description.

| #   | Category            | Question                                                                                                                                                                                                                              |
| --- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Role**            | Does the affected personal data belong to your organisation's own operations, to your clients (you process on their behalf), or both?                                                                                                 |
| 2   | **T0**              | When did your organisation achieve **reasonable certainty** that a breach occurred? (This is T0 — the starting point of the 72h clock.)                                                                                               |
| 3   | **Breach type**     | Which types apply? Select all: Confidentiality (data disclosed/accessed by unauthorised parties), Integrity (data altered), Availability (data lost or inaccessible), or **Still under investigation**. Many incidents combine types. |
| 4   | **Data categories** | What categories of personal data were affected? (Names, emails, addresses, phone numbers, financial data, health data, biometrics, location, criminal records, passwords, etc.)                                                       |
| 5   | **Subject count**   | Approximately how many individuals are affected? (Estimate with basis if exact count unavailable.)                                                                                                                                    |
| 6   | **Identifiers**     | What direct and indirect identifiers are present in the affected data?                                                                                                                                                                |
| 7   | **Encryption**      | Was the data encrypted? If yes: Is the algorithm current (e.g., AES-256)? Is the key secure and stored separately from the data? Does a backup exist?                                                                                 |
| 8   | **Intent**          | Was the event accidental (human error, technical failure, misconfiguration) or intentional (theft, hacking, insider attack, data sale)?                                                                                               |
| 9   | **Cross-border**    | Are affected data subjects in multiple EU Member States? Where is your main establishment?                                                                                                                                            |
| 10  | **DPA deadlines**   | If you are a processor: does your Data Processing Agreement specify a notification window shorter than 72 hours? (Common: 24h or 48h.)                                                                                                |
| 11  | **AI system**       | Did this breach involve an AI system (e.g., model weight exfiltration, adversarial attack, AI-generated output exposure, training data leak)?                                                                                         |
| 12  | **Sector**          | What sector is the controller in? (Healthcare, finance, public authority, telecom, retail, etc.)                                                                                                                                      |

For each unanswered question, note the gap and proceed with worst-case assumption; flag the gap in the output.

---

### Step 3: Role Determination and Track Selection

**⟁ CLARIFY** — Confirm the organisational role based on the answer to Question 1:

| Scenario            | Track        | Obligations                                                                                                                                                                                   |
| ------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Controller only** | Track A      | Full ENISA assessment; Art. 33 SA notification decision; Art. 34 subject communication decision; Art. 33(5) internal log                                                                      |
| **Processor only**  | Track B      | Notify affected controller(s) "without undue delay" (Art. 33(2)); contractual DPA deadline governs; no independent SA notification; no independent ENISA assessment for the controller's risk |
| **Hybrid (both)**   | Tracks A + B | Run Track A for own-controller data; run Track B for client data simultaneously; never conflate the two                                                                                       |

**Processor T0 Rules (Track B):**

Track B has a two-stage T0 with separate legal consequences:

| Stage             | T0 Event                                                                                     | Obligation                                    | Deadline                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Processor T0**  | Processor achieves awareness of the breach                                                   | Notify affected controller(s)                 | "Without undue delay" (Art. 33(2)) — contractual DPA deadline applies (commonly 24h or 48h) |
| **Controller T0** | Controller achieves reasonable certainty (typically upon receiving processor's notification) | Controller's 72h SA notification clock starts | 72h from controller T0                                                                      |

Always determine and display both T0 timestamps in hybrid and processor scenarios. The processor's T0 does **not** start the controller's 72-hour clock.

**Supply Chain / Sub-Processor Scenarios:**

When the breach originates at a sub-processor, the notification chain follows the contractual hierarchy:

```
Sub-processor → Processor → Controller → Supervisory Authority
```

Key rules:

1. Each entity notifies the next link "without undue delay" with available information, supplemented later.
2. DPA deadlines in each link compound: if sub-processor has 24h to notify processor, and processor has 24h to notify controller, the controller may have very little of the 72h remaining.
3. Document every notification timestamp and information state at each stage.

---

### Step 4: Incident Triage — Does GDPR Apply?

Before the full ENISA assessment, confirm the event qualifies:

**4a. Is it a "personal data breach"?**

Art. 4(12) GDPR: "a breach of security leading to the accidental or unlawful **destruction, loss, alteration, unauthorised disclosure of, or access to**, personal data transmitted, stored or otherwise processed."

Check:

- [ ] Was personal data involved? (Any information relating to an identified or identifiable natural person — Art. 4(1))
- [ ] Did any of the six qualifying events occur? (Destruction / loss / alteration / unauthorised disclosure / unauthorised access)
- [ ] Was this linked to a security failure (however caused — human error, technical fault, or malicious act)?

If **all three yes** → GDPR Art. 33 breach notification framework applies. Proceed to Step 5.

If **no personal data involved** → GDPR breach obligation does not apply. Advise on any other applicable notification obligations (NIS2, sector-specific) and close.

If **uncertain** → proceed with the assessment applying the most conservative interpretation, and flag for DPO/legal counsel review.

**4b. Aggregation analysis:**

Where the breach involves multiple data categories that appear low-risk individually, assess their combined effect. A name + employer + medical condition combination elevates risk significantly above each element considered alone.

**4c. Special category check (Art. 9):**

Does the breach involve Art. 9 data?

- Health data
- Genetic or biometric data (where used for identification)
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Sexual orientation or sex life
- Criminal convictions or offences (Art. 10)

If yes, note as a **mandatory aggravating factor** in the ENISA assessment (raises DPC base score to 4) and increases likelihood of Art. 34 subject notification requirement.

---

### Step 5: T0 Validation and Clock Management

**5a. Establish T0.**

T0 = the moment the controller (or, for Track B, the processor) achieved **reasonable certainty** that a breach occurred. This is not the moment of first suspicion, nor the completion of the full investigation.

**⟁ CLARIFY** — If T0 is ambiguous or the user reports a long gap between first indication and T0:

Challenge T0 claims when:

- Gap between first suspicion and declared T0 > 24 hours → Require detailed explanation of investigation steps; note "may be scrutinised by SA"
- Gap > 48 hours → Flag explicitly: "Supervisory authorities consistently scrutinise delayed T0 declarations; document investigation chronology in detail"
- T0 is set at a suspiciously convenient boundary (midnight, start of business) → Ask for the specific triggering event

**5b. Calculate the deadline.**

| Obligation                                      | Deadline                                                                        | Starting Point              |
| ----------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------- |
| Art. 33 SA notification                         | 72 hours from T0 (or "without undue delay" with documented explanation if >72h) | Controller T0               |
| Art. 33(2) processor-to-controller notification | "Without undue delay" — DPA contractual deadline governs                        | Processor T0                |
| Art. 34 data subject communication              | "Without undue delay" — no absolute deadline, but delay prolongs harm           | After notification decision |

Display the remaining time prominently in the output:

```
T0:              [timestamp]
Current time:    [timestamp]
Elapsed:         [X hours Y minutes]
72h deadline:    [timestamp]
Time remaining:  [Y hours Z minutes] ⚠️ or [DEADLINE PASSED — late notification with explanation required]
```

**5c. Phased notification (Art. 33(4)).**

Where not all required information is available within 72 hours, Art. 33(4) explicitly permits phased notification:

1. Submit an **initial notification** with the facts known at T0 + available information under Art. 33(3)(a)–(e)
2. Note in the submission: "Further information will follow; phased notification under Art. 33(4)"
3. Submit **supplementary notification(s)** as investigation findings are confirmed
4. Document the reasons for phased submission in the Art. 33(5) internal record

Advise the user to use Art. 33(4) proactively rather than delaying the initial submission while gathering complete information.

---

### Step 6: ENISA Severity Assessment

Apply the ENISA severity formula: **SE = (DPC × EI) + CB**

**⟁ CLARIFY** — For any variable where the facts are ambiguous, apply the conservative (higher) value and note the assumption.

#### 6a. DPC — Data Processing Context: 1–4 (integer after adjustments; hard bounds 1–4)

**Base score by data category:**

| Category                | Base | Examples                                                                                                                                                                         |
| ----------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simple Data             | 1    | Name, email, postal address, phone number, biographical data, education, employment history                                                                                      |
| Behavioural Data        | 2    | Location / traffic data, browsing history, preferences and habits, purchase behaviour                                                                                            |
| Financial Data          | 3    | Income, bank account numbers, payment card data, salary, transaction history, credit score                                                                                       |
| Sensitive Data (Art. 9) | 4    | Health, genetic, biometric (for identification), political opinions, religious/philosophical beliefs, trade union membership, sexual orientation, criminal convictions (Art. 10) |

**Contextual adjustments (±1 to ±3, applied to base; final DPC capped at 4, floored at 1):**

| Factor                                                                                                           | Direction | Amount   |
| ---------------------------------------------------------------------------------------------------------------- | --------- | -------- |
| High volume of data per individual                                                                               | ↑         | +1 to +2 |
| Controller type implies sensitive inference (online pharmacy → health status; luxury dealership → wealth)        | ↑         | +1 to +2 |
| Vulnerable data subjects (minors, patients, abuse survivors, witnesses)                                          | ↑         | +1 to +3 |
| Data already publicly available or previously disclosed                                                          | ↓         | −1 to −2 |
| Data is invalid, expired, or outdated (e.g., expired cards 10+ years old)                                        | ↓         | −1 to −2 |
| Nature of data reveals less than its category implies (e.g., generic medical certificate vs. specific diagnosis) | ↓         | −1       |

Where adjustments would push DPC above 4.0, note the excess as **qualitative aggravating circumstances** in the Strategic Advisory section. They reinforce severity but do not alter the numeric DPC.

**Adjustment examples:**

| Scenario                                        | Base | Adjustment            | Final DPC |
| ----------------------------------------------- | ---- | --------------------- | --------- |
| Supermarket customer list (name, phone)         | 1    | None                  | 1         |
| Online pharmacy customer list (name, order)     | 1    | +2 (health inference) | 3         |
| Undercover police officer personnel file        | 1    | +3 (safety risk)      | 4         |
| 10-year-old expired credit card numbers         | 3    | −2 (invalidity)       | 1         |
| Dating app breach (sexual preference disclosed) | 4    | None                  | 4         |

#### 6b. EI — Ease of Identification: 0.25 / 0.50 / 0.75 / 1.00

| Score | Level       | Description                                                                                              |
| ----- | ----------- | -------------------------------------------------------------------------------------------------------- |
| 0.25  | Negligible  | Re-identification extremely difficult; requires specific expertise and access unavailable to most actors |
| 0.50  | Limited     | Re-identification requires significant effort or access to additional data sources                       |
| 0.75  | Significant | Re-identification achievable with moderate effort or commonly available information                      |
| 1.00  | Maximum     | Direct identification possible from the breached data alone without additional research                  |

**EI by identifier type:**

| Identifier        | 0.25                          | 0.50                          | 0.75                           | 1.00                            |
| ----------------- | ----------------------------- | ----------------------------- | ------------------------------ | ------------------------------- |
| Full name only    | Common name, large population | Uncommon name, national scope | Uncommon name, small locale    | + DOB + email + address         |
| National ID / SSN | No reference database access  | + DOB visible                 | + email or employer            | + name from public registry     |
| Phone / address   | Not in public register        | Non-public, small area        | —                              | In public register              |
| Email             | No name, not searchable       | —                             | Searchable via social networks | Contains full name, searchable  |
| Clear photo       | Distant, unclear              | + location clues              | Clear, no other data           | Clear + linked profile/location |

**Encryption adjustment on EI:**
Where data is encrypted with current-standard algorithms (AES-256 or equivalent) and the key is secure and stored separately: apply EI = 0.25 (encryption renders identification negligible). Verify: Is the algorithm current? Is the key uncompromised? Is the key stored separately? If any answer is "No" or "Unknown," treat as unencrypted.

#### 6c. CB — Circumstances of Breach: 0–2 (additive; multiple circumstances may apply simultaneously)

**Loss of Confidentiality:**

| Score | Circumstance                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------------- |
| 0     | Data exposed to risk without evidence of actual access by unauthorised parties                             |
| +0.25 | Data disclosed to limited, known recipients (e.g., single misdirected email, identifiable wrong recipient) |
| +0.50 | Data disclosed to unknown number of recipients or made publicly accessible                                 |

**Loss of Integrity:**

| Score | Circumstance                                                      |
| ----- | ----------------------------------------------------------------- |
| 0     | Data altered but original recovered before use                    |
| +0.25 | Data altered; possibly used incorrectly; original recoverable     |
| +0.50 | Data altered; possibly used incorrectly; original NOT recoverable |

**Loss of Availability:**

| Score | Circumstance                                                            |
| ----- | ----------------------------------------------------------------------- |
| 0     | Data recoverable without difficulty (backup available and restored)     |
| +0.25 | Temporary unavailability (recovery requires significant effort or time) |
| +0.50 | Permanent unavailability (no recovery possible)                         |

**Malicious Intent:**

| Score | Circumstance                                                                |
| ----- | --------------------------------------------------------------------------- |
| 0     | Accidental — human error, technical failure, misconfiguration               |
| +0.50 | Intentional — theft, hacking, insider attack, data sale, social engineering |

#### 6d. Severity Calculation and Verdict

**Calculate: SE = (DPC × EI) + CB**

| SE Score   | Level         | Description                                                                                              | Notification Obligation                                                                     |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| SE < 2     | **LOW**       | Minor inconveniences; limited risk to rights and freedoms                                                | Art. 33(5) internal log only — SA notification not required                                 |
| 2 ≤ SE < 3 | **MEDIUM**    | Significant inconveniences; overcome with difficulty (extra costs, denial of services)                   | Art. 33 SA notification required (72h)                                                      |
| 3 ≤ SE < 4 | **HIGH**      | Serious consequences with difficulty (misappropriation, blacklisting, job loss, property damage)         | Art. 33 SA notification + Art. 34 data subject notification                                 |
| SE ≥ 4     | **VERY HIGH** | Significant or irreversible consequences (financial distress, long-term psychological harm, safety risk) | Art. 33 SA notification + Art. 34 data subject notification + consider public communication |

**Borderline score guidance:**

| Score Range | Guidance                                                                                                 |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| 1.75 – 2.00 | Document thoroughly why LOW is justified; SA may disagree; review with DPO before deciding not to notify |
| 2.75 – 3.00 | Assess whether any uncaptured aggravating factor pushes into HIGH; lean conservative                     |
| 3.75 – 4.00 | Assess whether public communication beyond direct subject notification is warranted                      |

For any score within 0.25 of a threshold, flag the borderline explicitly and recommend the user discuss the classification with DPO or legal counsel before finalising.

**Borderline worked examples:**

_Near LOW/MEDIUM (SE ≈ 1.75):_ Newsletter sent with all 150 subscriber emails in CC instead of BCC. DPC = 1 (email, simple data). EI = 1.00 (emails are direct identifiers). CB = 0.25 (disclosed to limited known recipients) + 0 (accidental) = 0.25. SE = 1.25 → LOW. BUT: if the newsletter topic implies sensitive status (e.g., HIV support group), DPC adjustment +2 → SE = 3.25 → HIGH.

_Near MEDIUM/HIGH (SE ≈ 2.75–3.00):_ HR SaaS processor breach, employee records of 3 client companies exposed via misconfigured API (500 employees, salary + performance ratings, discovered within 12 hours). DPC = 3, EI = 1.00, CB = 0.25 (API exposure, unclear access). SE = 3.25 → HIGH. At boundary: if logs confirm zero external access, CB = 0, SE = 3.0, exactly at threshold. Lean toward HIGH given performance data's potential for workplace harm.

---

### Step 7: EDPB Case Matching

After the ENISA calculation, identify the closest EDPB Guidelines 01/2021 reference case. This validates the severity verdict and, where ENISA and EDPB cases conflict, the more conservative (higher notification) result governs.

**Case taxonomy:**

| Category            | Cases | Key Variables                                                                   |
| ------------------- | ----- | ------------------------------------------------------------------------------- |
| Ransomware          | 01–04 | Backup availability; exfiltration evidence; sector (hospital vs. manufacturing) |
| Data exfiltration   | 05–07 | Hashing strength; credential type; data category (financial vs. health)         |
| Internal human risk | 08–09 | Intent (departing employee vs. accidental); data recovery confirmation          |
| Lost/stolen devices | 10–12 | Encryption state; key security; backup existence; paper vs. digital             |
| Mispostal           | 13–16 | Whether opened; data category; scale (single vs. batch)                         |
| Social engineering  | 17–18 | Impersonation vs. phishing; access duration; scope                              |

**Output format:**

> "This scenario most closely resembles **EDPB Case [XX]: [Brief Description]**.
> EDPB recommendation: SA notification [YES/NO]; Subject notification [YES/NO].
> Your situation differs in: [key differences].
> These differences [support / suggest reconsidering] the calculated severity verdict of [LEVEL]."

If EDPB case recommendation and ENISA calculation conflict: document both, apply the more conservative (higher notification) result, and note the discrepancy in the Art. 33(5) internal record.

**⟁ CLARIFY** — Where the closest EDPB case supports a different verdict than ENISA, ask:
"The ENISA formula yields [LEVEL], but the most analogous EDPB case (Case [XX]) suggests [different verdict]. I recommend applying the more conservative classification. Do you agree, or do you wish to document your reasons for selecting [alternative]?"

---

### Step 8: Article 33 Notification Decision

**8a. Is Art. 33 notification required?**

Art. 33(1): "In the case of a personal data breach, the controller shall without undue delay and, where feasible, not later than 72 hours after having become aware of it, notify the personal data breach to the supervisory authority competent in accordance with Article 55, **unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons**."

| ENISA Level | Art. 33 Required?                     |
| ----------- | ------------------------------------- |
| LOW         | No — Art. 33(5) internal log required |
| MEDIUM      | Yes                                   |
| HIGH        | Yes                                   |
| VERY HIGH   | Yes                                   |

**8b. When is notification late?**

If the 72-hour deadline has passed:

- Art. 33(1) requires: "where notification is not made within 72 hours, it shall be accompanied by reasons for the delay"
- Document the delay reasons explicitly in the notification
- Note that late notification is a separate violation from non-notification, but its severity depends on circumstances; proactive late notification is substantially better than non-notification

**8c. Identify the competent supervisory authority.**

Standard rule (Art. 55): The competent SA is the SA of the Member State where the controller is established.

For cross-border processing (Art. 56 / EDPB one-stop-shop): see Step 10.

**8d. Minimum content of Art. 33 notification (Art. 33(3)):**

Every notification must include, to the extent available:

1. Nature of the personal data breach, including categories and approximate number of affected data subjects and records
2. Name and contact details of the Data Protection Officer or other contact point
3. Likely consequences of the breach
4. Measures taken or proposed to address the breach, including mitigation measures

Where information under (a) or (d) is not available within 72 hours, use Art. 33(4) phased notification and supplement when information becomes available.

---

### Step 9: Article 34 Data Subject Communication Decision

**9a. Is Art. 34 communication required?**

Art. 34(1): "When the personal data breach is likely to result in a **high risk** to the rights and freedoms of natural persons, the controller shall communicate the personal data breach to the data subject without undue delay."

| ENISA Level | Art. 34 Indicated?                                                    |
| ----------- | --------------------------------------------------------------------- |
| LOW         | No                                                                    |
| MEDIUM      | No (risk, but not "high risk") — monitor; document the assessment     |
| HIGH        | Yes                                                                   |
| VERY HIGH   | Yes — consider public communication if direct contact is not feasible |

**9b. Art. 34 exemptions (Art. 34(3)) — when subject notification is NOT required even at HIGH/VERY HIGH:**

| Exemption                             | Condition                                                                                                                                                                                                  | Document how                                                                                                                                 |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Art. 34(3)(a) Encryption              | Controller implemented appropriate technical measures (e.g., AES-256 encryption) rendering data unintelligible to any person not authorised to access it, and those measures were applied to affected data | Confirm: algorithm, key security, key separation, backup. Encryption does NOT exempt from Art. 33 SA notification or Art. 33(5) internal log |
| Art. 34(3)(b) Subsequent measures     | Controller has taken measures to ensure high risk is no longer likely to materialise                                                                                                                       | Specify the measures and explain why risk is eliminated — this bar is high; SAs apply this narrowly                                          |
| Art. 34(3)(c) Disproportionate effort | Direct communication to each data subject would involve disproportionate effort                                                                                                                            | Where applicable, use public communication instead (e.g., news release, website notice visible to affected subjects)                         |

**⟁ CLARIFY** — Before applying an Art. 34(3) exemption:
"I'm considering applying the [Art. 34(3)(a) / (b) / (c)] exemption to avoid notifying data subjects. Before doing so, can you confirm [specific facts required for that exemption]? Applying this exemption incorrectly is a GDPR violation independent of the underlying breach."

**9c. Content of Art. 34 communication:**

Each communication must describe:

1. The nature of the breach in clear, plain language (not technical jargon)
2. The name and contact details of the DPO or other point of contact
3. The likely consequences of the breach
4. The measures taken or proposed to address the breach
5. Recommended protective steps the data subject should take

Do **not** include information that increases risk (e.g., specific vulnerability details that could assist further attacks).

---

### Step 10: Cross-Border Processing and Lead SA Determination

**10a. Does the one-stop-shop (Art. 56) apply?**

One-stop-shop applies where:

- The controller has establishments in more than one Member State, **or**
- The controller has a single establishment but processing substantially affects data subjects in multiple Member States

**If yes — identify the Lead SA:**

The Lead SA is the SA of the Member State where the controller's **main establishment** is located. Main establishment = the place of central administration in the EU, **or** the establishment in the EU that has the power to take decisions about the data processing and implement those decisions (Art. 4(16)).

**⟁ CLARIFY** — Ask:

1. "Where are decisions about this specific data processing operation taken?"
2. "Where is your organisation's central administration in the EU?"
3. "Which EU establishment has authority to implement processing decisions?"

If the answers point to different Member States, document the analysis and apply Art. 4(16) strictly. Where genuinely ambiguous, advise the user to seek a Lead SA determination from the candidate authorities.

**10b. If no EU establishment:**

The one-stop-shop does not apply. Notify **each SA** of every Member State where affected data subjects are resident. Track submissions separately.

**10c. Notification to concerned SAs:**

Even when notifying the Lead SA, other concerned SAs (where data subjects reside) must be informed. The Lead SA coordinates with them. Document which SAs are "concerned" and provide this information in the notification.

**10d. UK subjects — separate obligation:**

Flag explicitly: If any affected data subjects are UK residents, a separate breach notification to the ICO under UK GDPR + DPA 2018 is required, with its own 72-hour clock. This skill does not cover UK obligations. Consult UK GDPR provisions and the ICO's self-assessment tool.

**10e. SA Contact Directory — legalcode-mcp and web research:**

For the identified Lead SA, use legalcode-mcp or targeted web search to retrieve:

- Official notification portal URL
- SA contact email/phone for breach notifications
- SA-specific mandatory forms (CNIL, BfDI, and some others require their own forms)
- Operating hours and emergency contact

Key SAs for reference:

- **IE — DPC** (lead for many US tech companies): dataprotection.ie — online notification portal
- **FR — CNIL**: cnil.fr/fr/notifier-une-violation-de-donnees — French-language portal
- **DE — BfDI** (federal bodies/telecoms) or relevant Länder LDA/LfDI (private sector)
- **NL — AP** (Autoriteit Persoonsgegevens): autoriteitpersoonsgegevens.nl
- **SE — IMY** (Integritetsskyddsmyndigheten): imy.se
- **PL — UODO**: uodo.gov.pl
- **ES — AEPD**: aepd.es
- **IT — Garante**: garanteprivacy.it

Note: Always verify portal URLs via official SA websites — phishing risk is real. Do not click links provided by third parties without verification.

---

### Step 11: Mitigation Playbook

Generate a **tailored mitigation playbook** specific to the incident. Avoid generic checklists. Analyse the breach type, attack vector, data categories, organisational context, and urgency to produce actions that matter for **this specific case**.

**Design principles:**

1. **Case-driven, not category-driven.** Structure the playbook around what stops the harm for this case — not a generic "isolate systems" list.
2. **Prioritise by actual impact.** If the attacker has already left and data is exfiltrated, forensics is less urgent than harm scoping and subject communication.
3. **Specificity over generality.** "Audit all database accounts with read access to [specific system], revoke service accounts idle >90 days, enforce MFA on remaining accounts" beats "review access controls."
4. **Include dependencies.** If forensic imaging must occur before system changes, state this.
5. **Frame for SA scrutiny.** SAs will ask: "What did you do immediately? Why didn't you do X? What changed to prevent recurrence?"

**Action plan format per item:**

| #   | Action                      | Rationale                          | Priority                 | Owner           | Deadline (relative to T0) | Dependencies       | Status |
| --- | --------------------------- | ---------------------------------- | ------------------------ | --------------- | ------------------------- | ------------------ | ------ |
| 1   | [Specific, concrete action] | [Why this matters for this breach] | Critical / High / Medium | [Specific role] | T0+[Xh]                   | [None / Action #X] | ☐      |

**Reference action categories (use only what applies; customise each):**

- **Containment & forensics:** System isolation, credential revocation, evidence preservation, IOC sweep, access log audit, attack vector analysis, lateral movement assessment, forensic imaging before remediation
- **Data & impact scoping:** Exact data compromised, individual mapping, downstream risk assessment (identity theft, discrimination, financial fraud, blackmail, safety risk)
- **Legal & regulatory:** SA notification preparation, subject communication drafting, law enforcement engagement, legal privilege considerations, DPA contractual obligation review, insurance notification
- **Communication:** Internal stakeholder briefing, employee and works council communication, customer communication, media response preparation, support channel setup for affected individuals
- **Hardening & prevention:** Vulnerability remediation, encryption deployment, access control tightening, monitoring enhancement, detection rule creation, security architecture review
- **Governance & documentation:** Root cause analysis, DPIA review and update, Art. 30 records update, incident response procedure revision, training needs assessment, lessons learned

---

### Step 12: Post-Incident Documentation and Closure

**12a. Art. 33(5) internal documentation (mandatory regardless of severity).**

Every personal data breach — including LOW-severity ones — must be documented in the controller's internal breach register. The register must contain:

- Facts of the breach
- Effects of the breach
- Remedial action taken

Documentation must be sufficient for the SA to verify GDPR compliance on audit. Produce the full Art. 33(5) internal compliance log using the template in the Output Format section.

**12b. Post-notification case tracking.**

Where Art. 33 SA notification was submitted:

- Monitor for SA acknowledgment and reference number
- Track supplementary notification deadlines (Art. 33(4))
- Respond to SA follow-up inquiries promptly (SAs commonly request: ENISA calculation methodology, investigation timeline, measures implemented, DPIA status)
- Document SA communication in the breach register

**12c. DPIA review.**

Where a Data Protection Impact Assessment (DPIA) existed for the affected processing:

- Update the DPIA to reflect the breach findings
- Reassess residual risk level
- Update mitigation measures
- If the DPIA now shows high residual risk: Art. 36 prior consultation with the SA may be required for any resumed or modified processing

**12d. Art. 30 Records of Processing update.**

Update the Art. 30 register entry for the affected processing activity to reflect:

- Security incident reference
- Changes to technical and organisational measures implemented post-breach
- Updated risk assessment

**12e. Lessons learned and close-out.**

Document:

- Root cause (definitive, after investigation)
- Whether notification decisions were correct (retrospective assessment)
- Systemic control failures and remediation
- Policy and procedure updates
- Training delivered or planned
- Sign-off by DPO and appropriate responsible person

---

## ENISA Severity Classification Reference

This skill uses a four-level classification adapted directly from ENISA severity levels, aligned to Art. 33 and Art. 34 obligations:

| Level         | SE Range   | Compliance Status     | Art. 33             | Art. 34                                  |
| ------------- | ---------- | --------------------- | ------------------- | ---------------------------------------- |
| **LOW**       | SE < 2     | NO-NOTIFICATION       | Internal log only   | Not required                             |
| **MEDIUM**    | 2 ≤ SE < 3 | SA-NOTIFICATION       | Required within 72h | Not required                             |
| **HIGH**      | 3 ≤ SE < 4 | FULL-NOTIFICATION     | Required within 72h | Required without undue delay             |
| **VERY HIGH** | SE ≥ 4     | CRITICAL-NOTIFICATION | Required within 72h | Required + consider public communication |

---

## Actionable Output per Classification

### LOW — Internal Log Only

- Complete Art. 33(5) internal compliance log
- Document the ENISA calculation and reasoning for LOW classification
- Retain for minimum 3 years (SA audit right)
- Monitor: if new facts emerge that change the severity, re-run the assessment

**Do not** present a LOW classification as definitive without qualifying: "This classification is based on the facts currently available. If further investigation reveals [specific aggravating factor], the severity may increase and notification may become required."

### MEDIUM — SA Notification (Art. 33)

- Prepare and submit Art. 33 notification within 72h (or as soon as possible if clock has run)
- Use Art. 33(4) phased notification if all required content is not yet available
- Complete Art. 33(5) internal compliance log
- Document why Art. 34 subject notification is not required
- Monitor for SA follow-up

### HIGH — SA + Subject Notification (Art. 33 + Art. 34)

- Prepare and submit Art. 33 notification (as above)
- Check Art. 34(3) exemptions — if none applies, prepare Art. 34 subject communication
- Art. 34 communication must be in plain language; personalised where feasible
- Complete Art. 33(5) internal compliance log
- Generate tailored mitigation playbook (Step 11)
- DPIA review if applicable (Step 12c)

### VERY HIGH — SA + Subject + Possible Public Communication

- All HIGH actions, plus:
- Assess whether direct communication to all affected subjects is feasible; if not, public communication required (Art. 34(3)(c))
- Escalate immediately within the organisation (C-suite, board where applicable)
- Engage external legal counsel and consider law enforcement notification
- Prepare crisis communications for media enquiries
- Apply 3-pass Self-Interrogation to all severity classifications and notification decisions

---

## Prioritisation Framework

Prioritise response actions across three tiers:

| Tier       | Label                    | Description                                                                                                              | Typical Timeframe |
| ---------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **Tier 1** | Immediate / Mandatory    | Actions without which regulatory non-compliance is certain or subject harm continues to accumulate                       | T0 to T0+12h      |
| **Tier 2** | Material / High-Risk     | Actions that materially affect the severity assessment or reduce harm, but where a brief delay is defensible             | T0+12h to T0+72h  |
| **Tier 3** | Recommended / Preventive | Actions that reduce recurrence risk and improve regulatory standing but do not affect immediate notification obligations | T0+72h to 30 days |

**Tier 1 mandatory actions (always):**

- Establish T0 and start the 72h clock
- Determine controller vs. processor track
- Preserve evidence (logs, system state) before any remediation
- Complete initial ENISA assessment (even if preliminary)
- Notify processor's controller(s) if on Track B

**Tier 1 conditional actions (where SA notification required):**

- Identify competent SA / Lead SA
- Prepare Art. 33 notification with available information
- Submit notification or phased initial notification within 72h

**Tier 1 conditional actions (where Art. 34 required):**

- Draft data subject communication in plain language
- Identify all affected data subjects and communication method
- Transmit without undue delay after notification decision

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivery if any gate fails.

| Gate           | Rule                                                                                                                                                                            | Fail Action                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Source**     | Every GDPR obligation cited references a specific Article, paragraph, and subparagraph; every EDPB guidance reference identifies the specific guideline and version             | Add citation or mark [UNVERIFIED]    |
| **Format**     | All citations use consistent format (e.g., "GDPR Art. 33(1)"; "EDPB GL 9/2022 para. 23")                                                                                        | Fix format                           |
| **Currency**   | EDPB guidelines and national SA guidance are checked for more recent versions (EDPB issues updated versions; note the version and date in output)                               | Flag [CHECK CURRENCY]                |
| **Domain**     | Analysis stays within GDPR EU scope; any UK GDPR, US, or other jurisdiction reference is explicitly labelled as outside scope                                                   | Remove or label jurisdictional bleed |
| **Confidence** | Uncertainty — especially around borderline severity classifications, exemption application, and novel breach types (AI, supply chain) — is explicitly stated rather than hidden | Add confidence qualifier             |

---

## Self-Interrogation for HIGH and VERY HIGH Items

For any item classified as HIGH or VERY HIGH severity, and for any proposed Art. 34(3) exemption application, run this 3-pass adversarial review before delivering:

**Pass 1 — Legal Chain Integrity**
Does the risk assessment follow logically from the cited GDPR authority and ENISA methodology? Would a supervisory authority actually reach this conclusion given these facts? Have I applied the correct DPC base and adjustments?

**Pass 2 — Completeness**
Have all relevant data categories, subject vulnerabilities, and breach circumstances been captured? Have I checked for Art. 9 special category data, minor subjects, and cross-border dimensions? Does the EDPB case comparison align with the ENISA score?

**Pass 3 — Challenge**
What is the strongest argument against this classification? Under what circumstances might a well-advised controller reasonably reach a different severity verdict? If I am applying a HIGH verdict, what facts would reduce it to MEDIUM, and are any of those facts unconfirmed?

Document this review in the Glass Box Audit Trail.

---

## Confidence Scoring

Assign a confidence level to each severity classification and each notification decision:

| Level        | Range     | Meaning                                                                    | Action                                                                              |
| ------------ | --------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Definite** | 0.95–1.00 | Clear-cut case matching settled EDPB guidance                              | State classification with confidence                                                |
| **High**     | 0.80–0.94 | Strong alignment with EDPB cases and ENISA methodology; minor factual gaps | State with brief caveat noting the gap                                              |
| **Probable** | 0.60–0.79 | Good arguments for this classification; reasonable expert could disagree   | State with reasoning and contra-indicators; recommend DPO review                    |
| **Possible** | 0.40–0.59 | Genuinely uncertain — borderline score and ambiguous facts                 | Flag for professional review; present both possible classifications                 |
| **Unlikely** | 0.00–0.39 | Weak basis; facts do not clearly support this classification               | Do not assert; flag [UNCERTAIN]; recommend legal counsel consultation before acting |

Where confidence is below **Probable**, escalate the classification to DPO and legal counsel before finalising any decision not to notify.

---

## User Override Protocol

Where the user disagrees with the calculated severity verdict:

1. Document the system-calculated verdict: "This assessment indicates **[LEVEL]** (SE = [score]). You wish to classify as **[USER LEVEL]**."
2. Require documented justification from the user
3. If the user wishes to **downgrade** (lower notification), display:

> ⚠️ **REGULATORY RISK WARNING**: You are selecting a lower severity classification than the ENISA methodology indicates. If a supervisory authority later determines that higher severity was warranted, this independent decision may attract separate sanctions (Art. 83(4): up to €10M or 2% global annual turnover) and will be scrutinised alongside the underlying breach. Regulatory authorities are not bound by the controller's internal assessment. This override must be documented in the Art. 33(5) internal record and should be reviewed by qualified legal counsel before finalising.

4. Document the override in full in the Art. 33(5) internal compliance log: original verdict, selected verdict, justification, authorised by, timestamp.

---

## AI Act Intersection (Art. 62 Check)

Where the breach involves an AI system (Question 11), perform an additional assessment:

**Check 1: Is this a high-risk AI system?**

- Is it listed in Annex III of Regulation (EU) 2024/1689 (AI Act)? (Biometric identification, employment AI, credit scoring, critical infrastructure management, education AI, law enforcement, migration, justice, democratic processes)
- Is it deployed in a critical infrastructure sector?

**Check 2: Does the incident constitute a "serious incident" under Art. 62 AI Act?**
Art. 62 defines serious incidents as those that directly or indirectly lead to:

- Death or serious damage to health, property, or the environment
- Serious and irreversible disruption of critical infrastructure management

**If Art. 62 applies:**

- Providers must report to the market surveillance authority of the Member State(s) where the incident occurred
- Timeline: immediately after establishing causal link, no later than 15 days after awareness [VERIFY currency — Art. 62 implementation timelines under review]
- AI Act Art. 62 reporting runs in **parallel** to GDPR Art. 33 notification — they are separate, independent obligations

Add to the Assessment Dashboard:

```
AI ACT STATUS:       [Applicable / Not Applicable / Requires Further Assessment]
Art. 62 Reporting:   [Required / Not Required / Under Assessment]
AI Classification:   [High-Risk / Limited Risk / Minimal Risk / Not Classified]
```

---

## Glass Box Audit Trail

Every output must include a completed Glass Box section for traceability:

```yaml
glass_box:
  skill_name: "legalcode-eu-gdpr-breach-notification-operations"
  run_date: "[YYYY-MM-DD]"
  incident_reference: "[User-provided ID or 'Not assigned']"
  jurisdiction: "EU GDPR — Regulation (EU) 2016/679"
  track: "[A — Controller / B — Processor / A+B — Hybrid]"
  mode: "[Guided / Fast Path / Emergency]"
  t0_timestamp: "[datetime or 'Under determination']"
  deadline_72h: "[datetime or 'N/A — processor track']"
  hours_elapsed: "[N hours]"
  hours_remaining: "[N hours or 'DEADLINE PASSED']"
  enisa_calculation:
    dpc_base: "[1–4]"
    dpc_adjustments: "[list applied adjustments]"
    dpc_final: "[1–4]"
    ei_score: "[0.25 / 0.50 / 0.75 / 1.00]"
    ei_level: "[Negligible / Limited / Significant / Maximum]"
    cb_breakdown:
      confidentiality: "[0 / 0.25 / 0.50]"
      integrity: "[0 / 0.25 / 0.50]"
      availability: "[0 / 0.25 / 0.50]"
      malicious_intent: "[0 / 0.50]"
    cb_total: "[0–2]"
    se_formula: "([DPC] × [EI]) + [CB]"
    se_final: "[score]"
  severity_verdict: "[LOW / MEDIUM / HIGH / VERY HIGH]"
  override_applied: "[Yes — see justification / No]"
  edpb_case_match: "[Case XX — description / No close match]"
  art33_required: "[Yes / No — Art. 33(1) threshold not met]"
  art34_required: "[Yes / No — below high risk / No — Art. 34(3) exemption applied]"
  art34_exemption: "[None / Art. 34(3)(a) encryption / Art. 34(3)(b) subsequent measures / Art. 34(3)(c) disproportionate effort / Not applicable]"
  lead_sa: "[SA name and Member State / Not determined / N/A — no EU establishment]"
  ai_act_applicable: "[Yes — Art. 62 / No / Under assessment]"
  legalcode_mcp: "[Connected — citations verified / Not connected — verify independently]"
  self_interrogation_applied: "[Yes — HIGH/VERY HIGH items / No — below threshold]"
  confidence_level: "[Definite / High / Probable / Possible / Unlikely]"
  confidence_rationale: "[Brief rationale]"
  data_gaps: "[List any facts assumed worst-case due to unavailability]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires DPO and qualified legal review before acting"
```

---

## Anti-Patterns

What NOT to do when managing a GDPR breach response:

1. **Waiting for the complete investigation before declaring T0.** T0 is "reasonable certainty a breach occurred" — not completion of the root cause investigation. Investigating first and notifying later consistently attracts SA criticism and separate Art. 83 exposure.

2. **Setting T0 to a convenient moment rather than the actual triggering event.** SAs review email and log timestamps. A T0 set at midnight or start of business when the triggering event clearly occurred at 3 AM attracts scrutiny and undermines accountability.

3. **Conflating the processor's notification clock with the controller's.** The 72-hour Art. 33(1) clock runs from the controller's awareness. The processor's separate "without undue delay" obligation (Art. 33(2)) runs from the processor's awareness. These are different obligations with different starting points.

4. **Applying the Art. 34(3)(a) encryption exemption without verifying all four conditions.** The exemption requires: (a) appropriate encryption algorithm, (b) key not compromised, (c) key stored separately from data, and (d) no availability breach for which the encryption is irrelevant. Missing any condition eliminates the exemption.

5. **Treating a LOW severity verdict as a final decision.** LOW means internal log only based on currently available facts. New facts — especially exfiltration evidence or subsequent misuse — can retroactively change the assessment. Monitor, and rerun the ENISA formula if circumstances change.

6. **Notifying only the Lead SA and ignoring concerned SAs.** The one-stop-shop means the Lead SA is the primary contact; it does not mean other concerned SAs are uninvolved. The Lead SA informs them under the consistency mechanism.

7. **Not notifying at all where no EU establishment exists.** The one-stop-shop does not apply to non-EU-established controllers. Each SA of every Member State where affected subjects reside must receive a notification.

8. **Sending the Art. 34 subject communication in technical language.** Art. 34(2) and EDPB GL 9/2022 require "clear and plain language." A notification littered with technical jargon or legal citations is non-compliant and may attract separate enforcement.

9. **Failing to document a decision not to notify.** Art. 33(5) applies regardless of severity — even LOW-severity events where no SA notification is made must be logged. Absence of documentation is independently sanctionable.

10. **Applying the "disproportionate effort" exemption under Art. 34(3)(c) without implementing public communication.** This exemption does not permit silence — it requires public communication instead of direct subject communication. The controller must still ensure subjects are effectively informed.

11. **Using a processor notification to satisfy Art. 33(1) controller obligations.** A processor that also holds its own controller data cannot rely on its Track B notification to satisfy its Track A Art. 33(1) duty. The obligations are parallel and independent.

12. **Running remediation before forensic preservation.** Patching systems, resetting credentials, and restoring backups before imaging the incident environment destroys evidence needed for the investigation, the EDPB case matching, and SA follow-up. Preserve first; remediate second.

13. **Underestimating the impact of Art. 9 data.** Special category data (health, biometric, political, religious, sexual orientation) automatically elevates DPC to 4 and almost always pushes the severity verdict to HIGH or VERY HIGH. Treating it as ordinary personal data is a systematic under-assessment.

14. **Assuming phased notification means unlimited time.** Art. 33(4) allows phased notification — it does not extend the 72-hour deadline for the initial submission. The initial notification must be filed within 72 hours with available information; supplementary notifications follow as facts become clear.

15. **Not adjusting EI for the encryption state.** Where full-disk encryption with a secure, separately stored key is confirmed, EI adjusts to 0.25 — this is the primary mechanism by which the Art. 34(3)(a) exemption numerically flows through the ENISA formula. Failing to apply this adjustment leads to over-notification.

16. **Conflating Art. 33 SA notification with Art. 34 data subject communication.** These are independent obligations with different thresholds (risk vs. high risk), different content requirements, and different exemptions. Notifying the SA does not satisfy the subject communication obligation, and vice versa.

17. **Ignoring the AI Act Art. 62 parallel obligation.** Where a breach involves a high-risk AI system and constitutes a serious incident, Art. 62 AI Act requires separate reporting to the market surveillance authority. Running only the GDPR workflow without the AI Act check creates an independent compliance gap.

18. **Downgrading severity without documented DPO/legal review.** User override of ENISA verdicts is permitted under this skill, but downgrading without documented justification and DPO/legal review creates primary evidence of knowing non-compliance in any subsequent SA investigation.

19. **Treating EDPB case matching as the definitive answer.** EDPB 01/2021 cases are reference illustrations, not bright-line rules. Circumstances vary; where your case materially differs from the closest EDPB case, the differences must be explicitly assessed — not glossed over with "most closely resembles Case X."

20. **Closing the breach case before receiving SA case closure.** Many organisations complete their internal actions and close the breach file while the SA case is still open. Maintain an active post-notification tracker until the SA formally closes the matter.

---

## Writing Standards

Apply these standards when generating breach notifications, internal documentation, and the assessment dashboard:

1. **Plain language for subject communications.** Art. 34 communications must be intelligible to a lay person. Write at approximately a 10th-grade reading level. Test: "Would a non-technical individual understand what happened, what data was affected, what risk they face, and what they should do?"

2. **Active voice.** "We discovered a breach" not "A breach was discovered." "We will contact you" not "You will be contacted."

3. **Specific over vague.** "Your name, email address, and purchase history were exposed" not "Some of your personal data may have been involved." Specificity aids trust and regulator confidence.

4. **Timestamped chronology.** SA notifications must include precise timestamps — date and time, not just dates. Use ISO 8601 format (YYYY-MM-DD HH:MM UTC) for clarity across jurisdictions.

5. **No speculation in formal notifications.** Art. 33 notifications must be factual. Where facts are unknown, use "under investigation" — do not speculate about the attacker's intent, how data may be used, or third-party impacts not yet confirmed.

6. **Separate containment actions from investigation status.** In the SA notification, clearly distinguish: (a) what has been done to contain the breach, (b) what is the current investigation status, and (c) what preventive measures are planned. SAs read these in separate sections.

7. **Avoid minimising language.** Words like "minor," "limited," "unlikely to cause harm" in the Art. 33 submission are read by SAs as attempts to pre-empt their assessment. State facts; let the ENISA calculation speak to severity.

8. **Proofread for legal precision.** Check: Are all Article references correct? Are the named data categories accurate and complete? Is the DPO contact information current? Is the estimated number of data subjects defensible?

9. **Consistency between documents.** The Art. 33 notification, Art. 34 communication, processor notification, and internal log must describe the same breach consistently. Contradictions between these documents — even innocent ones — attract SA attention.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 10, search for Lead SA current notification portal, recent enforcement actions involving similar breach types, and SA-specific guidance documents
- Search for recent EDPB plenary decisions or opinions affecting the applicable breach category
- Save the most relevant results to `/tmp/legalcode-gdpr-breach-research.md` for reference during the analysis
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Example search: `"GDPR Article 33 notification [SA name] [breach type] enforcement [year]"`

**Without legalcode-mcp:**

- Proceed with embedded ENISA formula and EDPB case taxonomy
- Mark all enforcement precedents and SA-specific guidance with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — verify citations independently"`
- Focus the output on the structural methodology (ENISA/EDPB) rather than case-law depth

**Dynamic web research (where available):**
After completing the ENISA calculation and EDPB case matching, perform targeted research using specific breach details:

1. `"[Lead SA name]" breach notification [data category] enforcement [year]` — recent decisions
2. `"[Lead SA name]" breach guidance requirements [year]` — current SA-specific requirements
3. `GDPR [sector] data breach enforcement [year]` — sector-specific precedent
4. `EDPB guidelines data breach notification [year]` — check for updated guidance versions

Caveat all web-sourced information: "Supplementary context from web research — verify against official SA and EDPB sources before relying on in formal notifications."

---

## Output Format Template

Produce the following sections in order. Adapt content based on the track and severity verdict.

---

### Assessment Dashboard

```
╔══════════════════════════════════════════════════════════════════════╗
║               EU GDPR BREACH RESPONSE — ASSESSMENT DASHBOARD         ║
╠══════════════════════════════════════════════════════════════════════╣
║ Incident Ref:   [ID or "Not assigned"]                               ║
║ Role:           [Controller / Processor / Hybrid]                    ║
║ Breach Types:   [Confidentiality / Integrity / Availability]         ║
║ T0 (Awareness): [YYYY-MM-DD HH:MM UTC]                               ║
║ Elapsed:        [X hours Y minutes]                                  ║
║ 72h Deadline:   [YYYY-MM-DD HH:MM UTC]  ⚡ [Y hours remaining]        ║
║ DPA Deadline:   [If Track B: X hours / N/A]                          ║
╠══════════════════════════════════════════════════════════════════════╣
║                        SEVERITY CALCULATION                          ║
╠══════════════════════════════════════════════════════════════════════╣
║ DPC:  [Score] — [Category] [Adjustments applied]                     ║
║ EI:   [Score] — [Level]                                              ║
║ CB:   [Score] — C:[x] I:[x] A:[x] Malicious:[x]                     ║
║ SE:   ([DPC] × [EI]) + [CB] = [Final Score]                          ║
║ Verdict: [LOW / MEDIUM / HIGH / VERY HIGH]                           ║
║ Override: [None / Original: X, Selected: Y — see justification]      ║
║ EDPB Match: Case [XX] — [Description]                                ║
╠══════════════════════════════════════════════════════════════════════╣
║                       NOTIFICATION DECISIONS                         ║
╠══════════════════════════════════════════════════════════════════════╣
║ Art. 33 SA Notification:   [Required / Not required — LOW verdict]   ║
║ Lead SA:                   [SA name, Member State]                   ║
║ Art. 34 Subject Comms:     [Required / Not required — [reason]]      ║
║ Art. 34(3) Exemption:      [None / (a) Encryption / (b) Measures     ║
║                             / (c) Disproportionate effort]           ║
║ Art. 33(4) Phased:         [Yes — initial now, supplement by [date]  ║
║                             / No — full notification within 72h]     ║
╠══════════════════════════════════════════════════════════════════════╣
║                         SPECIAL FLAGS                                ║
╠══════════════════════════════════════════════════════════════════════╣
║ 🔒 ENCRYPTED   [Yes / No]   🚩 SCALE       [>100 subjects: Yes/No]  ║
║ 👶 VULNERABLE  [Yes / No]   ⚠️ CROSS-BORDER [Multiple MS: Yes/No]    ║
║ 🤖 AI SYSTEM   [Yes / No]   🇬🇧 UK SUBJECTS [Yes — ICO also / No]   ║
╠══════════════════════════════════════════════════════════════════════╣
║                       CONFIDENCE SCORE                               ║
╠══════════════════════════════════════════════════════════════════════╣
║ Classification Confidence: [Definite / High / Probable / Possible]   ║
║ Rationale: [Brief statement]                                         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### Document Templates

**Template 1 — Art. 33 Notification to Supervisory Authority**

```
PERSONAL DATA BREACH NOTIFICATION
Pursuant to Article 33 GDPR

1. CONTROLLER INFORMATION
   Organisation: [Legal name]
   Address: [Registered address]
   DPO / Contact: [Name, Email, Phone]
   Main Establishment: [Member State]

2. INCIDENT IDENTIFICATION
   Incident Reference: [Internal ID]
   Date/Time of Breach: [YYYY-MM-DD HH:MM UTC — if known, or "Under investigation"]
   Date/Time of Awareness (T0): [YYYY-MM-DD HH:MM UTC]
   Notification Timestamp: [YYYY-MM-DD HH:MM UTC]
   [If >72h: REASONS FOR DELAY: [Detailed explanation]]

3. NATURE OF BREACH
   Breach Type(s): [Confidentiality / Integrity / Availability — explain each]
   Description: [Factual description — no speculation]

4. DATA AFFECTED
   Categories of Personal Data: [Specific list]
   Approximate Records: [Number or estimate with basis]
   Approximate Individuals: [Number or estimate with basis]
   Special Categories (Art. 9): [Yes — specify / No]
   Vulnerable Subjects: [Yes — specify / No]

5. LIKELY CONSEQUENCES
   [Description of actual and potential impacts on data subjects — specific, not generic]
   ENISA Severity Level: [LOW / MEDIUM / HIGH / VERY HIGH] (SE = [score])

6. MEASURES TAKEN AND PROPOSED
   Containment (implemented): [Actions with timestamps]
   Mitigation (implemented): [Steps taken to reduce impact]
   Prevention (planned): [Future safeguards with target dates]

7. DATA SUBJECT NOTIFICATION
   [ ] Will communicate — planned for [date], method: [direct / public]
   [ ] Have communicated — sent [date], method: [direct / public]
   [ ] Not required — [detailed justification citing Art. 34(3) exemption]

8. CROSS-BORDER ELEMENTS (if applicable)
   Member States affected: [List]
   Other establishments involved: [List]
   Concerned SAs informed: [Yes / No / In progress]

9. SUPPLEMENTARY INFORMATION (if phased notification)
   Information still to be provided: [List]
   Expected by: [Date]

---
This notification was prepared using GDPR Art. 33 and EDPB Guidelines 9/2022.
This output does not constitute legal advice.
```

---

**Template 2 — Art. 34 Communication to Data Subjects**

```
IMPORTANT: A Security Incident Has Affected Your Personal Data

Dear [Name / "Valued Customer"],

WHAT HAPPENED
On [date], we discovered [one or two plain-language sentences — what occurred and how].

WHAT DATA WAS INVOLVED
The following information was affected:
• [Specific item 1]
• [Specific item 2]
[If applicable: The following was NOT affected: [specify]]

WHAT WE ARE DOING
We immediately [specific containment action taken].

We have also:
• [Mitigation step 1]
• [Mitigation step 2]

We have notified [the relevant supervisory authority] as required by law.

WHAT YOU SHOULD DO
We recommend the following steps to protect yourself:
1. [Specific protective action — e.g., change your password immediately]
2. [Specific action — e.g., monitor your bank statements]
3. [Specific action — e.g., be alert for suspicious communications claiming to be from us]

QUESTIONS?
Contact our Data Protection Officer:
Name: [DPO Name]
Email: [DPO Email]
Phone: [DPO Phone]

We sincerely apologise for this incident.
[Signature] | [Date]
```

---

**Template 3 — Processor-to-Controller Notification (Track B)**

```
NOTICE OF SECURITY INCIDENT
[Processor Name] → [Controller Name]
Issued pursuant to GDPR Article 33(2) and [DPA Reference, Clause X]

Date: [YYYY-MM-DD HH:MM UTC]
Incident Reference: [Internal ID]
Processor T0: [YYYY-MM-DD HH:MM UTC]

SUMMARY
We notify you of a security incident that may have affected personal data we process
on your behalf under our Data Processing Agreement dated [date].

TIMELINE
• [Date/Time]: [First indication of incident]
• [Date/Time]: [Confirmation of breach]
• [Date/Time]: [Containment action]
• [Date/Time]: This notification

INCIDENT DESCRIPTION
[Factual description of what occurred — no speculation about cause or scope beyond
what is confirmed at this time]

DATA POTENTIALLY AFFECTED
Based on current investigation, the following may have been affected:
• [Category 1]
• [Category 2]
Estimated volume: [Number] records relating to [Number] individuals

ACTIONS TAKEN
• [Containment action 1]
• [Containment action 2]

ASSISTANCE AVAILABLE
We are prepared to provide:
• Technical logs and forensic data
• Detailed incident timeline
• Support for your regulatory notification

IMPORTANT
As Processor, we provide this information to assist your assessment under GDPR
Article 33. Final risk determination and notification decisions are yours as Controller.
We have not performed the severity assessment on your behalf.

Contact: [Processor DPO / Security Lead] | [Email] | [Phone]
Available: [Hours/Timezone]
```

---

**Template 4 — Art. 33(5) Internal Compliance Log**

```
═══════════════════════════════════════════════════════
INTERNAL BREACH RECORD — GDPR ARTICLE 33(5)
═══════════════════════════════════════════════════════

INCIDENT IDENTIFICATION
Incident ID:        [Unique identifier]
Date of Record:     [Today's date]
Prepared by:        [Name, Role]
DPO Reviewed:       [Name, Date]

SECTION 1: FACTS OF THE BREACH
Discovery Date/Time:    [When first suspected]
T0 (Awareness):         [YYYY-MM-DD HH:MM UTC]
T0 Triggering Event:    [Specific event establishing reasonable certainty]
Investigation Gap:      [Time between discovery and T0 — justify if >24h]

Breach Type(s): [Confidentiality / Integrity / Availability]
Description:    [Detailed factual account]

SECTION 2: DATA AFFECTED
Categories: [Specific list]  |  Records: [Number]  |  Individuals: [Number]
Estimation Methodology: [How determined]
Art. 9 Special Categories: [Yes — specify / No]
Vulnerable Subjects: [Yes — specify / No]

SECTION 3: ENISA RISK ASSESSMENT
DPC: [Score] ([Base category] + adjustments: [list])
EI:  [Score] ([Level])
CB:  C:[score] I:[score] A:[score] Malicious:[score] = [Total CB]
SE = ([DPC] × [EI]) + [CB] = [Final]
Severity Level: [LOW / MEDIUM / HIGH / VERY HIGH]

EDPB Case Comparison:
Most Similar: Case [XX] — [Description]
EDPB Recommendation: SA [Y/N], Subjects [Y/N]
Differences: [Key differences from our situation]
Impact on Assessment: [Supports / Suggests reconsidering]

SECTION 4: OVERRIDE (if applicable)
System Verdict: [LEVEL] (SE = [score])
Final Classification: [LEVEL]
Override: [YES / NO]
[If YES: Reason / Authorised by / Legal counsel consulted / Timestamp]

SECTION 5: ACTUAL AND POTENTIAL IMPACT
Actual (confirmed): [What has demonstrably occurred]
Potential (assessed): [What could reasonably occur]

SECTION 6: REMEDIAL ACTIONS
Containment: [Action | Date/Time]
Mitigation:  [Action | Date/Time]
Prevention:  [Planned action | Target date]

SECTION 7: NOTIFICATION DECISIONS
Art. 33 SA: [Required and submitted / Required — pending / Not required — LOW]
  SA: [Name]  |  Submitted: [Date/Time]  |  Reference: [SA ref if received]
  [If phased: Supplementary info due by: [date]]

Art. 34 Subjects: [Required / Not required]
  [If not required: Exemption applied: Art. 34(3)([a/b/c]) — [justification]]
  [If required: Method: [Direct / Public]  |  Timing: [Date]]

SECTION 8: JUSTIFICATION FOR NON-NOTIFICATION (where applicable)
[If Art. 33 not required: Detailed reasoning applying GDPR Art. 33(1)]
[If Art. 34 not required: Detailed reasoning applying GDPR Art. 34(1) and (3)]

SECTION 9: AUTHENTICATION
Prepared: [Name] | [Title] | [Date]
Reviewed: [Name] | [Title] | [Date]
Approved: [Name] | [Title] | [Date]

Assessment tool: legalcode-eu-gdpr-breach-notification-operations
Authority: GDPR Art. 33–34, EDPB GL 9/2022 v2.0, EDPB GL 01/2021, ENISA v1.0
DISCLAIMER: AI-assisted. Does not constitute legal advice. Decisions certified by signatories above.
═══════════════════════════════════════════════════════
```

---

**Template 5 — Emergency Follow-Up Checklist** _(for Emergency Mode assessments)_

```
⚡ EMERGENCY ASSESSMENT — FOLLOW-UP REQUIRED

Preliminary assessment issued: [YYYY-MM-DD HH:MM UTC]
Full assessment required by:   [YYYY-MM-DD HH:MM UTC — 48h from preliminary]

□ Complete full ENISA calculation with all DPC adjustments validated
□ Confirm T0 against investigation logs — document triggering event
□ Review Art. 34 subject notification requirement if verdict is HIGH or VERY HIGH
□ Complete Art. 33(5) Internal Compliance Log
□ Submit or supplement Art. 33 SA notification if new information is material
□ Obtain DPO and legal counsel review of all notification decisions
□ Document any changes from preliminary to final assessment
□ Update post-notification case tracker

Preliminary assessment confidence: [Level]
Known gaps in preliminary assessment: [List]
```

---

**Template 6 — Post-Notification Case Tracker**

```
POST-NOTIFICATION CASE TRACKER
Incident Reference: [ID]  |  Initial Assessment: [Date]  |  Last Updated: [Date]

SA NOTIFICATION STATUS
SA: [Name]  |  Portal: [URL]  |  Reference: [If received]

| Milestone | Due | Done | Notes |
|-----------|-----|------|-------|
| Initial notification submitted | [Date] | ☐ | |
| SA acknowledgment received | — | ☐ | |
| Supplementary info (Art. 33(4)) | [Date] | ☐ | |
| SA follow-up inquiry response | [Date] | ☐ | |
| Case closed by SA | — | ☐ | |

SUBJECT NOTIFICATION STATUS
| Milestone | Due | Done | Notes |
|-----------|-----|------|-------|
| Communication drafted and DPO reviewed | [Date] | ☐ | |
| Communication sent | [Date] | ☐ | |
| Method: [Direct / Public / Both] | — | — | |
| Total subjects notified | — | — | Count: [X] |
| All subject inquiries resolved | — | ☐ | |

DOCUMENTATION COMPLETENESS
| Document | Required | Done | Location |
|----------|----------|------|----------|
| Art. 33(5) internal log | YES | ☐ | |
| Art. 33 SA notification | [Y/N] | ☐ | |
| Art. 34 subject comms | [Y/N] | ☐ | |
| Non-notification justification | [Y/N] | ☐ | |
| Root cause analysis | YES | ☐ | |
| DPIA updated | [Y/N] | ☐ | |
| Art. 30 records updated | YES | ☐ | |
| Lessons learned | YES | ☐ | |

CASE STATUS
Overall: [ACTIVE / PENDING SA RESPONSE / CLOSED]
Next action: [Description]  |  Next deadline: [Date]
Last updated by: [Name] | [Date]
```

---

## Localization Notes

**Germany:** For private-sector controllers, the competent SA is the Landesbeauftragte für Datenschutz und Informationsfreiheit (LfDI) or Landesbeauftragter für den Datenschutz (LDA) of the Bundesland where the main establishment is registered — not the federal BfDI (which covers federal public bodies and certain telecoms/post operators). Each Bundesland has its own form preferences. [VERIFY current BfDI/LDA scope — marginal cases exist]

**France — CNIL:** CNIL requires notification via its dedicated online portal (notifier.cnil.fr). Paper or email notifications are generally not accepted. CNIL also publishes supplementary guidance on specific breach scenarios. [VERIFY portal URL currency]

**Ireland — DPC:** The DPC is the Lead SA for many US-headquartered global tech companies operating in Ireland. DPC has a breach notification form and specific guidance documents for common scenarios. [VERIFY current DPC form requirements]

**Netherlands — AP:** The AP has historically been one of the more active SAs in enforcing Art. 33 timelines. The AP distinguishes between routine notifications and serious notifications requiring priority review. [VERIFY current AP tiering]

**Nordic SAs (SE-IMY, DK-Datatilsynet, NO-Datatilsynet, FI-Tietosuojavaltuutetun toimisto):** Nordic supervisory authorities are highly digitalised and expect online notification. Norway is not an EU Member State but applies the GDPR via the EEA Agreement — notify the Norwegian Datatilsynet for breaches affecting Norwegian subjects. [VERIFY EEA status and current portal details]

**Poland — UODO:** UODO has been active in enforcement and publishes its own breach handling guidance in Polish. Where the breach involves Polish data subjects and a Polish-established controller, UODO is the competent SA. [VERIFY]

**EEA non-EU Members (NO, IS, LI):** The GDPR applies in Norway, Iceland, and Liechtenstein via the EEA Agreement. Notify the national SA (Datatilsynet for Norway and Iceland; DSB for Liechtenstein) as appropriate. [VERIFY current EEA SA details]

---

## Provenance

**Created:** 2026-03-22
**Mode:** Mode A — Created from scratch (Legalcode native synthesis)
**Based on:**

- Deep analysis of `imported-lawvable-gdpr-breach-sentinel/SKILL.md` (Oliver Schmidt-Prietz, AGPL-3.0) — the imported skill's ENISA formula implementation, T0 validation logic, EDPB case taxonomy, emergency mode design, mitigation playbook principles, and document template structures informed this native skill. No text was directly copied; all content has been restructured, extended, and adapted to the Legalcode quality standard.
- `imported-lawvable-gdpr-breach-sentinel/references/enisa-methodology.md` — ENISA formula and scoring tables
- `imported-lawvable-gdpr-breach-sentinel/references/edpb-cases.md` — EDPB 01/2021 case taxonomy
- `imported-lawvable-gdpr-breach-sentinel/references/templates.md` — document template structure reference
- `skills/general/contracts/legalcode-contract-review/SKILL.md` — Legalcode gold standard quality framework (Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box Audit Trail, Anti-Patterns, Writing Standards)
- GDPR Regulation (EU) 2016/679 — Arts. 4(12), 33, 34, 56, 83
- EDPB Guidelines 9/2022 on personal data breach notification (v2.0, 28 March 2023)
- EDPB Guidelines 01/2021 on examples regarding personal data breach notification (v2.0, 14 December 2021)
- ENISA Technical Guidelines on severity methodology for personal data breaches (v1.0)
- AI Act Regulation (EU) 2024/1689, Art. 62 (serious incident reporting)

**Quality score:** 38/40 prompt engineering dimensions
**Completeness:** 18/18 required Legalcode elements
**Anti-patterns:** 20 items
**Workflow steps:** 12 steps with 8 CLARIFY points
