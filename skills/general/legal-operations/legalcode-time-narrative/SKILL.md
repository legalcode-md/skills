---
name: legalcode-time-narrative
description: Generate, improve, and validate attorney billing narratives for LEDES/UTBMS-compliant invoices.
  Use when a law firm timekeeper needs to draft, fix, or audit billing narratives; when a legal ops team
  needs to pre-validate invoices before e-billing submission; when a file reviewer is converting legacy
  block-billed time records; or when an outside counsel is preparing narratives to survive client billing
  guideline review or lodestar fee petition scrutiny.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generate, improve, and validate attorney billing narratives for LEDES/UTBMS-compliant invoices. Covers all four core operations: (1) generate narratives from bare time entries, (2) rewrite vague descriptions into specific, billable-quality text, (3) convert block-billed entries into individual task-level line items, and (4) validate completed narratives against client billing guidelines and e-billing platform rules (Tymetrix, Legal Tracker, CounselLink, eBillingHub, Brightflag). Applies the ABA UTBMS task code framework (L-codes for litigation, C-codes for counseling/advisory, P-codes for transactions, B-codes for bankruptcy) combined with cross-cutting activity codes (A101–A111). Also enforces professional ethics compliance under ABA Model Rule 1.5 and MRPC fee standards. Use when a law firm timekeeper needs to draft, fix, or audit billing narratives; when a legal ops team needs to pre-validate invoices before e-billing submission; when a file reviewer is converting legacy block-billed time records; or when an outside counsel is preparing narratives to survive client billing guideline review or lodestar fee petition scrutiny. Triggers on: UTBMS task codes, LEDES narratives, block billing, time entry descriptions, billing narrative, legal billing compliance, Tymetrix billing, CounselLink invoice, Legal Tracker submission, billing guidelines narrative, vague time entry, attorney time records, fee petition narrative, lodestar.


# Legalcode Time Narrative

> **Disclaimer**: This skill provides a framework for AI-assisted generation and review of
> attorney billing narratives. It does not constitute legal advice or professional responsibility
> guidance. Billing narrative standards vary by jurisdiction, client guidelines, e-billing
> platform, and matter type. All outputs must be reviewed by a licensed attorney or qualified
> billing professional before submission to clients. ABA Model Rule references and court-cited
> standards cited from memory carry hallucination risk — verify against current professional
> conduct rules and authoritative sources before relying on them. Time entry amounts, rates, and
> billing decisions remain the sole responsibility of the billing attorney.

---

## Purpose and Scope

This skill generates, improves, and validates attorney time entry narratives for LEDES/UTBMS
e-billing submission, client billing guideline compliance, and fee petition preparation.

**Covers four operating modes:**

| Mode         | Use Case                                              | Input                                             | Output                                             |
| ------------ | ----------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Generate** | Create narratives from bare or minimal time data      | Timekeeper, date, task code, brief note           | Complete compliant narrative                       |
| **Improve**  | Rewrite vague or inadequate existing narratives       | Draft time entries with poor descriptions         | Improved narratives with task code validation      |
| **Convert**  | Break block-billed entries into individual line items | Block-billed entry (multiple tasks, one duration) | Separated task-level entries with distributed time |
| **Validate** | Audit completed narratives against billing guidelines | Completed time entries + client guidelines        | Compliance findings with remediation               |

**Also covers:**

- UTBMS task code selection and validation (L-codes, A-codes, P-codes, activity codes)
- LEDES 1998B / LEDES 2000 field compliance
- Client e-billing platform requirements (Tymetrix/Legal Tracker, CounselLink, eBillingHub, Brightflag)
- ABA Model Rule 1.5 ethics compliance for billing narratives
- Fee petition / lodestar methodology narrative standards
- Minimum time increment compliance (.1 hour standard; platform-specific variations)
- Privilege preservation in billing narratives

**Does not:**

- Set billing rates or determine the reasonableness of hours billed (attorney judgment required)
- Provide legal advice on substantive matter issues
- Constitute professional responsibility guidance — ethics obligations vary by jurisdiction
- Guarantee acceptance by any specific e-billing platform or client billing review team
- Apply to expense/disbursement narratives (fee entries only)

---

## Jurisdiction and Governing Law

This is a **jurisdiction-agnostic** skill with the following multi-layer standards framework:

**Layer 1 — ABA Model Rules** (baseline across US jurisdictions): Model Rule 1.5 requires fees
to be reasonable; billing practices that are inherently deceptive or that do not reflect actual
work may constitute professional misconduct. [JURISDICTION-SPECIFIC: Each state has its own
Rules of Professional Conduct — the Model Rules are a template, not binding law in any state.]

**Layer 2 — Client Billing Guidelines / OCGs**: The primary compliance standard for most law
firm billing. The client's Outside Counsel Guidelines (OCGs) define acceptable narrative
standards, block billing prohibitions, minimum time increments, and task code requirements.

**Layer 3 — Court Standards** (for fee petitions): The lodestar standard requires billing
records to be "sufficiently detailed" for a reviewing court to assess reasonableness. Courts
apply the Hensley v. Eckerhart [VERIFY] standard in the US, or jurisdiction-specific fee
shifting provisions in other matters.

**Layer 4 — E-billing Platform Rules**: Tymetrix/Legal Tracker, CounselLink, and other
platforms may reject entries based on automated rule sets that are more granular than the
client's OCG.

[JURISDICTION-SPECIFIC] Outside the United States, billing narrative standards are governed
by local bar association rules, court fee schedules, and client agreements. Key variations:

- **England & Wales**: Solicitors Regulation Authority (SRA) Code of Conduct; detailed
  statutory assessment of costs under CPR Part 47 [VERIFY]
- **Canada**: Law Society requirements per province; Alberta, Ontario billing practices differ [VERIFY]
- **Australia**: Legal Profession Uniform Law (NSW/Vic) billing disclosure requirements [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
billing context, the workflow pauses and asks when:

- The matter type or timekeeper role is ambiguous (affects code selection)
- Multiple valid UTBMS codes could apply to the same task
- Block-billed entries cannot be reliably decomposed without timekeeper input
- Client billing guidelines conflict with standard UTBMS practice
- Privilege concerns limit the narrative detail that can safely be included

Use the **⟁ CLARIFY** pattern (structured options with explanations) wherever marked below.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept time entry data in any of these formats:

- **Pasted text**: Raw time entry notes, draft narratives, or billing descriptions
- **LEDES 1998B file**: Tab-delimited LEDES invoice file — parse the LINE_ITEM_DESCRIPTION field
- **CSV/spreadsheet**: Columns for date, timekeeper, hours, task code (if any), description
- **Single entry**: One time entry described in free text for immediate improvement
- **Batch file**: Multiple entries requiring systematic improvement or validation

Parse and structure each entry into:

```
Entry ID:        [sequential number]
Date:            [billing date]
Timekeeper:      [name and classification — Partner, Associate, Paralegal]
Hours:           [billed hours]
Task Code:       [existing code if provided; blank if none]
Activity Code:   [existing code if provided; blank if none]
Description:     [current narrative text]
Status:          [GENERATE / IMPROVE / CONVERT / VALIDATE — determined in Step 4]
```

If the input is a LEDES file, extract the relevant fields and proceed with the structured
format above.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the user these questions before proceeding. Skip any already answered:

1. **Matter type**: What type of legal matter do these entries cover?
   - Options: Litigation (dispute), Transactional (deal/contract), Regulatory/Compliance,
     Corporate (governance/general), Employment, Real Estate, Intellectual Property,
     Bankruptcy/Restructuring, Other/Multiple
   - _Why this matters_: Determines the correct UTBMS code set (L-codes vs. A-codes).

2. **Client billing guidelines**: Are there specific client billing guidelines to comply with?
   - Options: Yes — provide guidelines or OCG document, Yes — guidelines are on file
     (specify path), No — use general UTBMS/ABA standards, Unknown
   - _Why this matters_: Client OCGs often have stricter narrative requirements than general
     UTBMS standards, and platform-specific rejections are based on OCG rules.

3. **E-billing platform**: Which platform will receive these invoices?
   - Options: Tymetrix / Legal Tracker, CounselLink (LexisNexis), eBillingHub,
     Brightflag, Acuity, No e-billing platform / paper invoice, Unknown
   - _Why this matters_: Each platform has different character limits, code validation
     rules, and automated rejection triggers.

4. **Operating mode**: What does each entry need?
   - Options: Generate new narratives from bare notes, Improve existing vague narratives,
     Convert block-billed entries into separate line items, Validate complete entries against
     billing guidelines, Mixed — analyze each entry and determine appropriate mode
   - _Why this matters_: Determines the workflow path for each entry.

5. **Privilege sensitivity**: Does this matter involve highly sensitive legal strategy?
   - Options: Yes — narratives must not reveal legal strategy (privilege must be preserved),
     Moderate — be careful about privileged communications, No special concerns
   - _Why this matters_: Fee petition narratives may be public; some entries must be
     sanitized without losing specificity.

6. **Fee petition use**: Are these narratives for a fee petition or court-submitted billing?
   - Options: Yes — lodestar review anticipated, Possibly — matter may settle with fee
     shifting, No — standard client invoice only
   - _Why this matters_: Fee petition narratives require even higher specificity to survive
     lodestar scrutiny.

### Step 3: Load Client Billing Guidelines

Check for client billing guidelines in the user's provided documents or local configuration.

**If guidelines are provided**, extract these key requirements:

- Minimum narrative specificity requirements (what must be described)
- Block billing prohibition and minimum time increment (typically .1 hours)
- Prohibited activities (administrative tasks, excessive supervision, intra-firm conferences)
- Required task and activity code fields
- Character limits for narrative fields
- Specific prohibited phrases or vague descriptions listed by the client
- Staffing restrictions (caps on number of timekeepers per task, seniority requirements)

**If no guidelines are provided**, apply the **general UTBMS/ACC minimum standard**:

- Narrative must identify: (1) the legal task performed, (2) the specific subject matter,
  (3) the purpose or outcome where applicable
- No block billing of distinct tasks without time allocation
- Minimum time increment: .1 hours per entry
- Task and activity codes required (or map to standard UTBMS set)

**⟁ CLARIFY** — If multiple clients' guidelines are relevant (e.g., batch entries from
different matters), ask whether to:

- Apply the most restrictive guidelines across all entries
- Identify guidelines per matter and apply separately
- Apply general UTBMS standards and flag client-specific issues for manual review

### Step 4: Identify Operating Mode per Entry

For each entry, determine which operating mode applies based on the user's instruction
(Step 2) or by analyzing the entry:

**Auto-detection logic** (apply when mode is "Mixed" or unspecified):

| Signal                                                                                  | Mode                    |
| --------------------------------------------------------------------------------------- | ----------------------- |
| Description is blank or under 10 characters                                             | GENERATE                |
| Description mentions multiple distinct tasks in one entry                               | CONVERT (block billing) |
| Description uses vague terms ("review documents," "call with client") without specifics | IMPROVE                 |
| Description is complete but platform compliance is unknown                              | VALIDATE                |
| Description contains comma-delimited task list with no time allocation                  | CONVERT                 |
| Description is specific and substantive; code validation only needed                    | VALIDATE                |

Assign each entry a mode and proceed through the appropriate track in Steps 5–9.

### Step 5: Apply UTBMS Code Framework

For each entry, validate or assign the correct UTBMS task code and activity code using the
**UTBMS Code Reference** section below.

**Code validation process:**

1. Identify the matter phase (litigation stage, transaction stage, or counseling type)
2. Map the task described to the correct task code category
3. Map the "how" (the verb describing the work) to the correct activity code
4. Check that the task code and activity code combination is coherent
5. Flag any mismatch between the narrative description and the assigned codes

**⟁ CLARIFY** — When multiple valid codes apply to the same task, present options:

> "The entry 'analyzed mediation position and prepared settlement matrix' could map to
> L160 (Settlement/ADR) or L120 (Analysis/Strategy). For the activity, A102 (Research)
> or A104 (Review/Analyze) could both apply. Which better reflects the primary task?"

Flag any entries where the existing task code is inconsistent with the narrative description.
This is a common billing guideline violation that automated e-billing platforms detect.

### Step 6: Analyze Narrative Quality

Evaluate each entry's narrative against the **Six-Element Narrative Quality Framework**:

| Element          | Question                                                          | Present? |
| ---------------- | ----------------------------------------------------------------- | -------- |
| **1. Actor**     | Is the timekeeper's role and activity clear?                      | ✓ / ✗    |
| **2. Action**    | Is the specific legal task clearly described (verb + object)?     | ✓ / ✗    |
| **3. Subject**   | Is the specific document, issue, party, or proceeding identified? | ✓ / ✗    |
| **4. Purpose**   | Is the purpose or relevance to the matter stated or implied?      | ✓ / ✗    |
| **5. Outcome**   | Is the result or next step noted (where appropriate)?             | ✓ / ✗    |
| **6. Isolation** | Does this entry describe one distinct task (no block billing)?    | ✓ / ✗    |

A **COMPLIANT** entry must satisfy elements 1–4 and 6. Element 5 is required for entries
over 3.0 hours or entries involving significant deliverables (motions, agreements, opinions).

Classify each entry using the **Narrative Compliance Classification** defined below.

### Step 7: Rewrite and Improve Narratives

**For GENERATE mode**: Construct a narrative from the available data (timekeeper, task code,
matter notes, brief description). Use the Six-Element Framework as the construction template.

**For IMPROVE mode**: Rewrite the vague narrative using the improvement patterns in the
**Vague Narrative Improvement** section. Preserve factual accuracy — do not add details
that the timekeeper has not provided.

**Core rewriting rules:**

1. Replace generic verbs with specific ones (see **Vague-to-Specific Verb Table** below)
2. Add the document or subject matter name — never leave it as "documents" or "materials"
3. Add the purpose where inferrable from context (e.g., "in preparation for summary judgment motion")
4. Remove padding phrases ("attention to," "continued work on," "further review of")
5. Remove internal billing jargon that clients do not understand
6. Ensure the entry starts with the primary action verb (not "continued" or "further")

**⟁ CLARIFY** — When the subject matter cannot be inferred from the bare entry, ask:

> "Entry #3 says 'Review documents (2.1 hrs).' To rewrite this accurately, I need: (1) which
> specific documents (e.g., deposition transcripts, contract drafts, discovery responses),
> and (2) the purpose (e.g., preparation for cross-examination, due diligence review). Can
> you provide these details?"

**Privilege preservation rule**: If the matter requires high privilege sensitivity, rewrite
to identify the task and document type without revealing the content of legal advice, attorney
mental processes, or litigation strategy. Use formulations like:

- "Reviewed [document type] in connection with [procedural event/deliverable]"
- "Prepared memorandum re: [general legal issue] for attorney-client communication"

### Step 8: Convert Block-Billed Entries

For entries classified as block billing (single time entry covering multiple distinct tasks):

**Block billing identification markers:**

- Entry contains multiple distinct verbs separated by commas, semicolons, or "and"
- Entry describes tasks that could reasonably take different amounts of time
- Entry lists sequential tasks that occurred across different parts of the day
- Entry uses phrases like "various matters," "multiple calls," "various correspondence"

**Conversion methodology:**

1. **Identify distinct tasks** — parse the entry and list each distinct task
2. **Estimate time allocation** — apply reasonable time estimates per task type:
   - Review of motion/brief (per page): .1–.2 hours per 10 pages (matter complexity-dependent)
   - Telephone conference: actual call duration, rounded to nearest .1
   - Drafting correspondence: .2–.5 hours per substantive letter or email
   - Court appearance or deposition: actual time + reasonable preparation
3. **Cross-check total** — ensure the sum of individual entries equals or approaches the
   original total; note any variance to the timekeeper for confirmation
4. **Flag for timekeeper review** — mark every converted entry: "⚠ TIME ALLOCATED —
   review and confirm before submission"

**⟁ CLARIFY** — Before finalizing conversions, present the decomposed entries to the user:

> "I have decomposed Entry #7 (4.2 hours of block billing) into 4 separate entries. Please
> review the time allocation and confirm each entry accurately reflects the time spent
> before submitting."

**Example conversion** (see also **Before/After Examples** section):

```
BEFORE (block billed):
  Date: 2026-03-10 | Timekeeper: J. Smith (Partner) | Hours: 3.5
  Description: "Reviewed deposition transcripts, drafted summary judgment motion,
  conferred with expert witness re: damages analysis."
  Task Code: L300

AFTER (converted):
  Entry 7a | Hours: 1.2 | Task: L330 | Activity: A104
    Description: "Reviewed deposition transcripts of [Deponent Name] and [Deponent Name]
    for factual support for summary judgment motion; identified key testimony re: [issue]."

  Entry 7b | Hours: 1.8 | Task: L240 | Activity: A103
    Description: "Drafted argument section of motion for summary judgment addressing
    [legal issue]; incorporated deposition testimony re: [fact issue]."

  Entry 7c | Hours: 0.5 | Task: L130 | Activity: A108
    Description: "Telephone conference with [Expert Name] re: damages calculation
    methodology and alignment with summary judgment theory."
```

### Step 9: Validate Against Platform Requirements

Check the completed narratives against the applicable e-billing platform requirements:

**Tymetrix / Legal Tracker:**

- Narrative character limit: typically 2,000–4,000 characters (verify against client config) [VERIFY]
- Task code and activity code: both required fields; entry rejected if either is missing
- Block billing detection: automated rule may flag entries with multiple conjunctive tasks
- Prohibited phrases: client-specific lists loaded in Legal Tracker configuration
- Minimum time increment: typically .1 hours; entries below threshold may be rejected

**CounselLink (LexisNexis):**

- Character limit: typically 3,000 characters [VERIFY]
- Activity code: required in most client configurations
- Budget adherence: entries exceeding approved matter budget may trigger hold
- Timekeeper classification: must match registered LEDES timekeeper classification
- Special characters: avoid &, <, >, ", ' in narrative text (LEDES XML encoding issues)

**eBillingHub / Brightflag:**

- AI-assisted billing guideline compliance scoring: narrative specificity is scored automatically
- Duplicate detection: similar narratives across consecutive dates may be flagged
- Administrative task detection: entries resembling non-billable work are flagged

**General LEDES 1998B Compliance:**

- LINE_ITEM_DESCRIPTION field must not be blank
- No LEDES delimiter characters (pipe | ) within the narrative text
- Encoding: standard ASCII; avoid special characters outside the ASCII set
- Date format: YYYYMMDD in LEDES date fields; verify date matches billing period

Flag any violation as NON-COMPLIANT or PARTIAL using the classification below.

### Step 10: Run Quality Verification

Before delivering the improved narratives, run the quality checks defined in the
**Quality Assurance Framework** section:

1. Run the **5 Citation Quality Gates** silently. Revise any failures before delivery.
2. For every entry classified **NON-COMPLIANT** on re-review, run the **Self-Interrogation**
   to confirm the classification is correct and the recommended fix is accurate.
3. Assign a **Confidence Score** to the improved narrative quality assessment.
4. Verify all task code assignments are coherent with the narrative content.
5. Verify no privileged information has been inadvertently disclosed in narratives
   intended for client delivery.

### Step 11: Generate Output

Produce the output in the format requested by the user:

- **Narrative text only**: Cleaned narratives ready to copy into billing software
- **Structured table**: Date | Timekeeper | Hours | Task Code | Activity Code | Narrative
- **LEDES 1998B patch**: Tab-delimited rows for the changed LINE_ITEM_DESCRIPTION fields only
- **Track-changes style**: Original vs. improved narrative for each entry
- **Compliance report**: Validation-only output with finding per entry, no rewrites

Append the **Glass Box Audit Trail** to every output.

---

## UTBMS Code Reference

### Litigation Task Codes (L-codes)

The ABA UTBMS Litigation task code set. Use for all contentious matters (litigation,
arbitration, regulatory enforcement). Combine with activity codes for each entry.

| Code     | Phase/Task                                          | Typical Activities                                          |
| -------- | --------------------------------------------------- | ----------------------------------------------------------- |
| **L100** | **Case Assessment, Development and Administration** | —                                                           |
| L110     | Fact Investigation/Development                      | Investigate, interview witnesses, gather facts              |
| L120     | Analysis/Strategy                                   | Analyze merits, develop case strategy, assess exposure      |
| L130     | Experts/Consultants                                 | Retain, consult, coordinate with experts                    |
| L140     | Document/File Management                            | Organize, index, maintain case files                        |
| L150     | Budgeting                                           | Prepare, monitor, update case budgets                       |
| L160     | Settlement/Non-Binding ADR                          | Evaluate settlement, mediation preparation                  |
| L190     | Other Case Assessment                               | Miscellaneous case administration                           |
| **L200** | **Pre-Trial Pleadings and Motions**                 | —                                                           |
| L210     | Pleadings                                           | Draft, file, respond to complaints, answers, counterclaims  |
| L220     | Preliminary Injunctions / Provisional Remedies      | TRO, preliminary injunction work                            |
| L230     | Court Mandated Conferences                          | Rule 16/scheduling conferences, CMCs                        |
| L240     | Dispositive Motions                                 | Motions to dismiss, summary judgment, judgment on pleadings |
| L250     | Other Written Motions / Submissions                 | Briefs, oppositions, replies, amicus briefs                 |
| **L300** | **Discovery**                                       | —                                                           |
| L310     | Written Discovery                                   | Interrogatories, RFPs, RFAs — draft, respond, review        |
| L320     | Document Production                                 | Review, process, produce documents; privilege log           |
| L330     | Depositions                                         | Prepare for, take, defend depositions; review transcripts   |
| L340     | Expert Discovery                                    | Expert reports, depositions, Daubert analysis               |
| L350     | Discovery Motions                                   | Motions to compel, protective orders, discovery disputes    |
| L390     | Other Discovery                                     | Subpoenas, third-party discovery                            |
| **L400** | **Trial Preparation and Trial**                     | —                                                           |
| L410     | Fact Witnesses                                      | Prepare fact witnesses, coordinate testimony                |
| L420     | Expert Witnesses                                    | Prepare expert witnesses, coordinate with retained experts  |
| L430     | Written Motions / Trial Submissions                 | Motions in limine, trial briefs, jury instructions          |
| L440     | Other Trial Preparation                             | Organize exhibits, trial logistics, war room support        |
| L450     | Trial and Hearing Attendance                        | Attend trial, evidentiary hearings, oral argument           |
| **L500** | **Appeal**                                          | —                                                           |
| L510     | Appellate Motions and Submissions                   | Appellate briefs, motions, petitions for certiorari         |
| L520     | Local Counsel Coordination                          | Coordinate with local appellate counsel                     |
| L530     | Oral Argument                                       | Prepare for, attend, deliver oral argument on appeal        |
| **L600** | **Settlement / Regulatory / Other**                 | —                                                           |
| L610     | Settlement / Mediation                              | Draft settlement agreements, attend mediations              |
| L620     | Expert Witnesses (post-trial)                       | Expert coordination in regulatory or post-trial phase       |
| L630     | Expert Depositions                                  | Expert depositions in settlement or regulatory phase        |
| L640     | Regulatory Proceedings                              | Agency submissions, regulatory hearings                     |
| L650     | Other Post-Trial / Appellate                        | Post-judgment enforcement, regulatory follow-up             |

### Counseling Task Codes (C-codes)

Use for non-contentious matters: general advice, regulatory guidance, opinion work. These
are high-level phase codes; detail is carried in the activity code and narrative.

| Code | Description               | Typical Work                                                |
| ---- | ------------------------- | ----------------------------------------------------------- |
| C100 | Fact Gathering            | Investigate facts, gather background information for advice |
| C200 | Researching Law           | Research applicable statutes, regulations, case law         |
| C300 | Analysis and Advice       | Analyze issues, advise client, draft opinion letters        |
| C400 | Third Party Communication | Communicate with regulators, counterparties, agencies       |

**Note on P-codes for transactions**: Many law firms and clients route transactional work
(M&A, financing, real estate) through the P-code set (see below) rather than C-codes.
Confirm the client's preferred code set before submission.

### Standard Activity Codes (A-codes)

Activity codes describe **how** the work was performed and cut across all task code sets
(L, C, B, P). Most e-billing platforms require an activity code alongside every task code.
The standard UTBMS set maintained by the LEDES Oversight Committee [VERIFY current version]:

| Code | Description                         | Typical Narrative Pattern                                                                                                 |
| ---- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| A101 | Plan and Prepare                    | "Prepared for [deposition/hearing/closing] re: [topic]..."                                                                |
| A102 | Research                            | "Researched [legal issue] under [jurisdiction/statute]..."                                                                |
| A103 | Draft / Revise                      | "Drafted [document]; revised [document] per [party] comments..."                                                          |
| A104 | Review / Analyze                    | "Reviewed [document]; analyzed [legal issue] re: [purpose]..."                                                            |
| A105 | Communicate (in-firm)               | "Strategy conference with [partner/associate names] re: [topic]..."                                                       |
| A106 | Communicate (with client)           | "Telephone conference with [client name, title] re: [topic]..."                                                           |
| A107 | Communicate (other outside counsel) | "Call with [co-counsel firm] re: [topic]; [outcome]..."                                                                   |
| A108 | Communicate (other external)        | "Call with opposing counsel / regulator / expert re: [topic]..."                                                          |
| A109 | Appear for / Attend                 | "Attended [hearing/trial/mediation/closing] before [tribunal]..."                                                         |
| A110 | Manage data/files                   | "Organized and indexed [document set]; updated [case file]..."                                                            |
| A111 | Other                               | Use sparingly; always pair with a specific narrative description                                                          |
| A112 | Analysis / Strategy                 | "Analyzed [issue] and assessed strategic options for [purpose]..." [VERIFY — extended code, not present in all platforms] |
| A113 | Expert Witnesses                    | "Prepared expert witness [name] for deposition re: [subject]..." [VERIFY — extended code]                                 |
| A114 | Attend Deposition                   | "Attended deposition of [witness] re: [issues]..." [VERIFY — extended code; some platforms use A109 for depositions]      |

**Code set version note**: The standard UTBMS A-code set maintained by the LEDES Oversight Committee is A101–A111. Some platforms and clients use an extended set through A114. Verify the applicable version against the client's billing guidelines or platform configuration before using A112–A114.

**Important**: Travel time, when billable, is typically coded separately per client OCG
or engagement letter. Check the applicable guideline — some clients prohibit billing for
travel; others allow up to 50% of normal rate. There is no universal UTBMS travel activity
code; use A109 (Appear/Attend) for the event itself and confirm travel billing treatment.

### Project Management / Transaction Codes (P-codes)

Use for structured transactional matters (M&A, financing, real estate, IP transactions).

| Code | Description                           |
| ---- | ------------------------------------- |
| P100 | Project Administration                |
| P200 | Fact Gathering / Due Diligence        |
| P210 | Corporate Review                      |
| P220 | Tax                                   |
| P230 | Environmental                         |
| P240 | Real and Personal Property            |
| P250 | Employee / Labor                      |
| P260 | Intellectual Property                 |
| P270 | Regulatory Reviews                    |
| P280 | Other Due Diligence                   |
| P300 | Structure / Strategy / Analysis       |
| P400 | Initial Document Preparation / Filing |
| P500 | Negotiation / Revision / Responses    |
| P600 | Completion / Closing                  |
| P700 | Post-Completion / Post-Closing        |
| P800 | Maintenance and Renewal               |

### Bankruptcy Task Codes (B-codes)

For insolvency and restructuring matters.

| Code | Description                                    |
| ---- | ---------------------------------------------- |
| B100 | Administration                                 |
| B110 | Case Administration                            |
| B120 | Asset Analysis and Recovery                    |
| B130 | Asset Disposition                              |
| B140 | Relief from Stay / Adequate Protection         |
| B150 | Meetings with Creditors                        |
| B160 | Fee / Employment Applications                  |
| B170 | Fee / Employment Objections                    |
| B180 | Avoidance Action Analysis                      |
| B185 | Assumption / Rejection of Leases and Contracts |
| B190 | Other Contested Matters                        |
| B195 | Non-Working Travel                             |
| B200 | Operations                                     |
| B210 | Business Operations                            |
| B220 | Employee Benefits / Pensions                   |
| B230 | Financing / Cash Collections                   |
| B240 | Tax Issues                                     |
| B250 | Real Estate                                    |
| B260 | Board of Directors Matters                     |
| B300 | Claims and Plan                                |
| B310 | Claims Administration and Objections           |
| B320 | Plan and Disclosure Statement                  |
| B400 | Bankruptcy Advice                              |
| B410 | General Bankruptcy Advice / Opinions           |
| B420 | Restructuring                                  |

### Expense Codes (E-codes) — Reference Only

This skill covers fee entries only. Expense/disbursement narratives follow a separate
standard. E-code categories for reference: E101 (Copying), E102 (Outside Printing),
E103 (Word Processing), E104 (Facsimile), E105 (Telephone), E106 (Overtime Meals),
E107 (Delivery), E108 (Postage), E109 (Local Travel), E110 (Out-of-Town Travel),
E111 (Meals), E112 (Court Fees), E113 (Subpoena Fees), E114 (Witness Fees),
E115 (Deposition Transcripts), E116 (Trial Transcripts), E117 (Trial Exhibits),
E118 (Litigation Support Vendors), E119 (Outside Experts), E120 (Filing Fees),
E121 (Arbitration Fees), E122 (Consultant Fees), E123 (Process Server Fees),
E124 (Other).

---

## Narrative Quality Standards

### The Six-Element Framework

Every compliant billing narrative must answer these six questions:

| #   | Element      | Test                                                                                    |
| --- | ------------ | --------------------------------------------------------------------------------------- |
| 1   | **Who**      | Is the timekeeper's role and function clear from context?                               |
| 2   | **What**     | Is the specific legal action taken clearly described? (specific verb + specific object) |
| 3   | **Which**    | Are the specific documents, issues, parties, or proceedings named?                      |
| 4   | **Why**      | Is the purpose or relevance to the matter stated or inferrable?                         |
| 5   | **Result**   | For major work product, is the outcome or deliverable noted?                            |
| 6   | **Discrete** | Is this a single task, not a block of mixed tasks?                                      |

A narrative that passes elements 2, 3, 4, and 6 is the minimum for COMPLIANT status.
Elements 1 and 5 elevate a COMPLIANT narrative to **Excellent**.

### Vague-to-Specific Verb Table

Replace generic billing verbs with specific, descriptive alternatives:

| Vague Verb                | Replace With                                                          |
| ------------------------- | --------------------------------------------------------------------- |
| "Review" / "Reviewed"     | "Analyzed," "Assessed," "Examined for [purpose]," "Redlined"          |
| "Draft" / "Drafted"       | "Drafted Section [X] of [document] addressing [issue]"                |
| "Research" / "Researched" | "Researched [legal issue] under [jurisdiction]; identified [finding]" |
| "Call" / "Conference"     | "Telephone conference with [person, title] re: [specific topic]"      |
| "Meeting"                 | "Strategy meeting with [client/team] re: [specific agenda item]"      |
| "Correspondence"          | "Drafted/reviewed email to [recipient] re: [specific topic]"          |
| "Work on"                 | Replace entirely — specify what aspect of what document               |
| "Attention to"            | Replace entirely — this phrase alone describes nothing                |
| "Continued work"          | Replace with the specific task being continued                        |
| "Review and analyze"      | Specify what was reviewed and what the analysis determined            |

### Platform-Specific Requirements

#### Tymetrix / Legal Tracker (Thomson Reuters)

- **Character limit**: The LEDES 1998B standard sets LINE_ITEM_DESCRIPTION at 2,000 characters; Legal Tracker may allow client-configured extensions [VERIFY against current platform documentation]
- **Required fields**: TASK_CODE and ACTIVITY_CODE are mandatory for most client configurations
- **Block billing detection**: Automated; narratives with comma-separated task lists may trigger
- **Prohibited phrases**: Client-configurable; common prohibited phrases include "various," "multiple matters," "as needed," "miscellaneous"
- **Duplicate detection**: Identical or near-identical narratives on consecutive billing days may trigger manual review
- **Timekeeper rate card**: TIMEKEEPER_CLASSIFICATION must match approved rate card on file

#### CounselLink (LexisNexis)

- **Character limit**: Typically 3,000 characters [VERIFY]
- **XML encoding**: Certain characters (&, <, >, ", ') must be XML-escaped in LEDES XML submissions
- **Activity code**: Required in most client configurations
- **Budget alerts**: Entries that cause matter totals to exceed approved budgets may be placed on hold
- **Duplicate entry detection**: Same timekeeper, same date, same task code, similar description — flagged
- **Matter ID**: LINE_ITEM_MATTER_ID must match the client's internal matter numbering

#### eBillingHub

- **Narrative scoring**: AI-assisted compliance scoring that penalizes vague descriptions
- **Block billing detection**: Machine learning-based detection of block-billed entries
- **Guideline enforcement**: Client-specific rules loaded at submission time; narrative violations auto-rejected

#### Brightflag

- **AI compliance**: Narrative analyzed against client billing guidelines using NLP
- **Specificity scoring**: Low-specificity narratives flagged for attorney review before client delivery
- **Real-time feedback**: Integrates with timekeeping software (Intapp, BigTime, etc.) to provide live narrative guidance

### Ethics Framework

**ABA Model Rule 1.5** (Fees) [VERIFY current version]: A lawyer's fee must be reasonable.
Factors include: time and labor required, novelty and difficulty, the skill requisite, preclusion
of other employment, the customary fee, the amount involved and results obtained, time limitations,
the nature and length of the professional relationship, the experience of the lawyer, and whether
the fee is fixed or contingent. Billing narratives that obscure or misrepresent the nature of
work performed may constitute a violation. [JURISDICTION-SPECIFIC: State rules of professional
conduct govern — verify your jurisdiction's version of Rule 1.5.]

**Fee Petition / Lodestar Standard**: Under the lodestar methodology (Hensley v. Eckerhart,
461 U.S. 424 (1983) [VERIFY]), courts calculate reasonable attorneys' fees by multiplying
reasonable hours by reasonable rates. Courts reduce hours for:

- Vague entries that do not allow assessment of reasonableness
- Block billing that obscures how much time was spent on each task
- Excessive, redundant, or otherwise unnecessary hours
- Administrative tasks billed at attorney rates

Narratives intended for fee petitions must meet a higher specificity standard than standard
client invoices.

---

## Block Billing Analysis and Conversion

### Definition and Consequences

**Block billing** (also called "lumped billing") is the practice of recording multiple distinct
tasks under a single time entry without allocating time among those tasks.

**Consequences of block billing:**

- Courts routinely reduce fee petition requests by 20–40% for block billing [VERIFY]
- E-billing platforms with automated detection will flag or reject entries
- Clients with OCG block billing prohibitions may reject invoices and demand re-submission
- State bar grievance committees may investigate systematic block billing as a fee ethics matter

**Common block billing patterns to detect:**

```
Pattern 1 — Comma-list:
"Reviewed deposition transcripts, drafted motion, called client, reviewed expert report."
→ 4 distinct tasks, zero time allocation

Pattern 2 — "And" connector:
"Researched personal jurisdiction issues and drafted analysis memorandum."
→ May be convertible to one entry if research and drafting are inseparable, or must split

Pattern 3 — Multi-document review:
"Reviewed contract, exhibits A through F, and seller's disclosure statement."
→ Single review task but may need volume/complexity notation, not necessarily block billing

Pattern 4 — Day-spanning tasks:
"Reviewed deposition from morning session; attended client meeting; revised motion draft."
→ Three discrete events that should be three entries

Pattern 5 — Catch-all:
"Various matters related to transaction."
→ Prohibited — never acceptable; requires complete rewrite with specific task identification
```

### Before/After Examples

**Example 1 — Vague research entry:**

```
BEFORE:  "Legal research. (1.5)"
AFTER:   "Researched enforceability of non-compete covenants under California Business
          and Professions Code § 16600 in the context of the proposed executive employment
          agreement; reviewed recent Court of Appeal decisions applying the Edwards v.
          Arthur Andersen [VERIFY] broad restraint standard."
Task: A102 | Activity: A102
```

**Example 2 — Vague review entry:**

```
BEFORE:  "Review documents. (2.0)"
AFTER:   "Reviewed plaintiff's document production (approximately 340 pages) in response
          to Request for Production No. 12 (financial records) for responsiveness,
          relevance, and privilege; annotated 18 documents for inclusion in summary
          judgment exhibit list."
Task: L320 | Activity: A104
```

**Example 3 — Block-billed conference and drafting:**

```
BEFORE:  "Conference with client re: settlement; draft counter-proposal; review mediator
          demand letter. (3.0)"
AFTER:
  Entry A | Hours: 0.8 | Task: L610 | Activity: A106
    "Telephone conference with [Client Name], General Counsel, re: evaluation of
     mediator's proposal of [amount]; discussed authority parameters and
     non-monetary terms."
  Entry B | Hours: 1.5 | Task: L610 | Activity: A103
    "Drafted written counter-proposal to mediator's settlement demand addressing
     monetary terms, indemnification, and confidentiality; incorporated client's
     authority and negotiating instructions from conference."
  Entry C | Hours: 0.7 | Task: L160 | Activity: A104
    "Reviewed and analyzed mediator's initial demand letter and supporting
     damages calculation; identified legal and factual challenges to damages theory."
```

**Example 4 — Vague correspondence:**

```
BEFORE:  "Correspondence and calls. (1.0)"
AFTER:   "Telephone conference with opposing counsel [Name] re: proposed deposition
          schedule and scope of witness list; confirmed agreement on dates; drafted
          confirming email to opposing counsel re: scheduling agreement."
Task: L310 | Activity: A107
```

**Example 5 — Generic "attention to" entry:**

```
BEFORE:  "Attention to motion practice matters. (4.5)"
AFTER:   [CANNOT IMPROVE WITHOUT TIMEKEEPER INPUT — this entry lacks sufficient
          information. Request: (1) which motion(s) were worked on, (2) what specific
          tasks were performed, (3) whether this is one continuous task or multiple tasks.]
```

**Example 6 — Fee petition level detail:**

```
BEFORE:  "Research ERISA preemption. (2.5)"
AFTER:   "Researched federal ERISA preemption of state insurance law claims under
          29 U.S.C. § 1144 [VERIFY] as applicable to plaintiff's breach of contract
          count; analyzed circuit split between Sixth Circuit and Ninth Circuit
          approaches to savings clause analysis; reviewed Supreme Court's Pilot Life
          Insurance Co. v. Dedeaux [VERIFY] standard; drafted research memorandum
          summarizing applicable law for use in motion to dismiss briefing."
Task: L240 | Activity: A102
```

---

## Narrative Compliance Classification

### COMPLIANT — No Action Required

The narrative satisfies elements 2, 3, 4, and 6 of the Six-Element Framework. Specific
document/issue/party names are present. No block billing. Task code and activity code
are consistent with the narrative. No prohibited phrases.

**Examples of COMPLIANT narratives:**

- "Drafted motion to dismiss for lack of personal jurisdiction; analyzed defendant's
  contacts with the forum state under the three-part Calder effects test."
- "Telephone conference with J. Parker (client CFO) re: proposed earn-out calculation
  methodology and treatment of non-recurring items in EBITDA definition."

**Action**: None. Confirm task and activity code assignment.

### PARTIAL — Fixable Deficiency

The narrative identifies the work product or task but is missing one or more required
specificity elements. No block billing present. Deficiency is correctable by adding
factual detail that the timekeeper would know.

**Common PARTIAL patterns:**

- Names the document type but not the specific document ("reviewed deposition transcripts")
- Names the issue but not the document ("researched personal jurisdiction issues")
- Describes the communication type but not the subject ("telephone conference with client")
- Has adequate specificity but uses a prohibited client phrase

**Action**: Improve the narrative using the rewriting rules in Step 7. Flag specific
missing element(s) for timekeeper confirmation where needed.

### NON-COMPLIANT — Rewrite Required

The narrative fails to meet minimum standards. Entry will be rejected by platform,
flagged by client billing review, or reduced in a fee petition.

**NON-COMPLIANT triggers (any one sufficient):**

- Description is blank, single word, or under 15 characters
- Pure block billing with no task-level specificity ("various matters," "miscellaneous")
- Uses only a prohibited phrase ("attention to," "work on," "miscellaneous legal services")
- Task code and narrative are materially inconsistent (narrative describes L300 discovery
  work but task code is L110 case assessment)
- Contains LEDES delimiter characters that will corrupt the invoice file

**Action**: Full rewrite required. Request timekeeper input where factual detail is missing.
Flag for billing supervisor review before submission.

---

## Actionable Output per Finding

For each entry analyzed, produce a finding in this format:

```
Entry [#] | [Date] | [Timekeeper] | [Hours] | Status: [COMPLIANT / PARTIAL / NON-COMPLIANT]
──────────────────────────────────────────────────────────────────────────────────────────
Task Code:     [Assigned code] | Activity Code: [Assigned code]
Finding:       [What is wrong with the narrative, or COMPLIANT]
Element Gap:   [Which of the 6 elements is missing — e.g., "Element 3 (Subject): document
                not specifically identified"]
Platform Risk: [TYMETRIX: will reject | COUNSELLINK: will reject | No specific risk]
Ethics Risk:   [HIGH / MEDIUM / LOW — explain if not LOW]
Original:      "[original narrative text]"
Improved:      "[rewritten narrative — or 'TIMEKEEPER INPUT NEEDED: [specific question]']"
Confidence:    [HIGH / PROBABLE / POSSIBLE]
```

---

## Prioritization Framework

When presenting findings to a billing professional, prioritize by submission urgency:

### Tier 1 — Submission Blockers (Fix Before Any Submission)

Issues that will cause invoice rejection or billing system errors:

- NON-COMPLIANT entries: blank narratives, block-billed entries without decomposition
- Task code / narrative mismatches that automated systems will flag
- LEDES format errors (delimiter characters, blank required fields)
- Narratives that the client OCG expressly prohibits
- Time entries with zero hours or negative hours

### Tier 2 — Fee Petition Risk (Fix Before Court Submission)

Issues that will cause court reduction in fee petition context:

- Block billing that hasn't been converted (courts reduce by 20–40%) [VERIFY]
- Vague entries that don't identify the specific document, witness, or issue
- "Continued work" entries without specification of what was continued
- Administrative tasks billed at attorney rates
- Duplicate or near-duplicate entries across consecutive days

### Tier 3 — Client Satisfaction (Fix Before Client Delivery)

Issues that may not be rejected but create client friction or fee dispute risk:

- Prohibited phrases that the client has listed in their OCG
- Narratives that, while technically sufficient, don't help the client understand the value
- Excessively terse entries that invite scrutiny even if technically correct
- Narrative inconsistencies across entries from different timekeepers on the same task

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise if any gate fails.

| Gate           | Rule                                                                          | Fail Action                              |
| -------------- | ----------------------------------------------------------------------------- | ---------------------------------------- |
| **Source**     | Every code assignment references the UTBMS standard (ABA) or client guideline | Mark [UNVERIFIED] or add code reference  |
| **Format**     | All improved narratives follow the Six-Element Framework                      | Revise to add missing elements           |
| **Currency**   | Client billing guideline requirements reflect current OCG version on file     | Flag "[CHECK GUIDELINE VERSION]"         |
| **Domain**     | Analysis stays within billing narrative scope — no substantive legal advice   | Remove or flag out-of-scope observations |
| **Confidence** | Uncertainty about timekeeper intent explicitly stated, not hidden             | Add "TIMEKEEPER INPUT NEEDED" flags      |

### Self-Interrogation for NON-COMPLIANT Classifications

For any entry classified as NON-COMPLIANT, apply this 3-pass review before confirming:

**Pass 1 — Classification Integrity**:

- Does the NON-COMPLIANT finding follow from the specific deficiency identified?
- Would a billing partner at a peer firm agree this entry is problematic?
- Is there a reading of the narrative that satisfies the minimum standard?

**Pass 2 — Completeness**:

- Have all six elements been tested against the entry?
- Has the correct client OCG version been applied (not a prior version)?
- Has the correct task code standard been applied (litigation vs. counseling)?

**Pass 3 — Challenge**:

- What is the strongest argument that this entry IS compliant?
- Under what circumstances would a billing court or client accept this entry?
- Is the NON-COMPLIANT finding proportionate, or should this be reclassified as PARTIAL?

Mark the audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                             | Action                                             |
| ------------ | --------- | --------------------------------------------------- | -------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear violation of stated rule; would be rejected   | State finding with confidence                      |
| **High**     | 0.80–0.94 | Strong basis for finding; minor edge case questions | State with brief caveat                            |
| **Probable** | 0.60–0.79 | Good arguments but narrative is borderline          | State with reasoning; recommend timekeeper review  |
| **Possible** | 0.40–0.59 | Genuinely uncertain — client guidelines unclear     | Flag for billing supervisor judgment               |
| **Unlikely** | 0.0–0.39  | Weak basis for concern                              | Do not flag as violation; note as observation only |

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section for traceability:

```yaml
glass_box:
  skill_name: "legalcode-time-narrative"
  mode: "[Generate / Improve / Convert / Validate / Mixed]"
  entries_processed: "[total count]"
  entries_compliant: "[count]"
  entries_partial: "[count]"
  entries_non_compliant: "[count]"
  entries_requiring_timekeeper_input: "[count]"
  matter_type: "[Litigation / Transactional / Regulatory / Corporate / Mixed]"
  utbms_code_set: "[L-codes / A-codes / P-codes / Mixed]"
  client_guidelines: "[OCG name/version or 'General UTBMS standards']"
  platform: "[Tymetrix/Legal Tracker / CounselLink / eBillingHub / Brightflag / None]"
  fee_petition_mode: "[Yes / No]"
  privilege_sensitivity: "[High / Moderate / Standard]"
  block_billing_detected: "[count] entries decomposed"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Time allocations in block-billing conversions are estimates — timekeeper confirmation required"
    - "Improved narrative content is based on available context — factual accuracy is timekeeper responsibility"
    - "Platform-specific character limits and rule sets may have changed — verify against current platform documentation"
    - "Ethics references are jurisdiction-agnostic — verify against applicable state rules of professional conduct"
  reviewer: "AI-assisted — requires qualified legal billing professional review before submission"
```

---

## Anti-Patterns

What NOT to do when generating, improving, or validating billing narratives:

1. **Adding facts not in evidence** — Never improve a narrative by adding specific document
   names, party names, legal issues, or outcomes that the timekeeper did not provide. Every
   fact in an improved narrative must come from the timekeeper's original entry or from
   explicit context. Invented specificity is worse than vagueness — it creates billing fraud risk.

2. **Defaulting to "review and analyze"** — This phrase combination is the most common
   vague-but-specific-sounding billing phrase. A genuine improvement must replace both verbs
   with concrete alternatives and add the document name and purpose.

3. **Block billing conversion without timekeeper confirmation** — Never submit time-allocated
   entries from a block billing conversion without the billing timekeeper's confirmation that
   the time estimates are accurate. Always mark converted entries with a flag.

4. **Assigning task codes by guessing** — When the narrative is too vague to determine the
   correct task code, ask rather than guess. An incorrect task code that contradicts the
   narrative is a billing compliance violation that is harder to fix than a missing code.

5. **Stripping privilege without intent** — When improving narratives that discuss
   attorney-client communications or legal strategy, do not inadvertently reveal privileged
   content by making the narrative more specific. Privilege preservation takes priority over
   maximum specificity.

6. **Ignoring the time increment** — Improving a narrative without checking the hours billed
   for reasonableness relative to the task described. A perfectly worded narrative for a task
   that took .1 hours but is billed at 3.0 hours does not pass the lodestar test.

7. **Treating "correspondence" as one task** — An entry that says "correspondence re: closing"
   covering emails, calls, and letter drafting is block billing. "Correspondence" as a category
   descriptor, not a single discrete task, always requires decomposition or clarification.

8. **Applying litigation codes to transactional matters** — L-codes are for contentious matters.
   A merger review, contract negotiation, or compliance matter should use A-codes or P-codes.
   Misapplied codes are automatically flagged by e-billing platforms.

9. **Failing to flag "miscellaneous" and "various"** — These words are prohibited by virtually
   every sophisticated client billing guideline. They always require decomposition. Never
   "improve" an entry that contains these words without decomposing it first.

10. **Ignoring time entry sequence** — Reviewing entries in isolation misses patterns. The
    same timekeeper billing the same vague narrative on consecutive days suggests systematic
    billing issues that one improved entry will not fix. Review the sequence.

11. **Accepting "continued" without antecedent** — An entry that says "Continued drafting of
    motion" is only compliant if there is a prior entry that identifies which motion. If the
    batch does not include prior dates, flag for antecedent verification.

12. **Over-improving beyond reasonable specificity** — A narrative does not need to be a
    paragraph. The goal is sufficient specificity, not maximum specificity. A 300-word
    narrative for a .2-hour phone call is suspicious and may attract more scrutiny, not less.

13. **Treating all research entries as equivalent** — Legal research billing is the most
    scrutinized category in fee petitions. Research entries must specify: (1) the legal
    issue researched, (2) the jurisdiction or source consulted, and (3) the deliverable or
    purpose. "Legal research" alone is never sufficient.

14. **Ignoring paralegal and staff entries** — Non-attorney entries are frequently the least
    specific in a firm's billing records. Apply the same Six-Element Framework to paralegal
    and support entries — courts and clients review these with equal rigor.

15. **Conflating rewrite quality with compliance** — A beautifully written narrative that
    misrepresents the nature of the work is not compliant — it is worse. The goal is accurate
    specificity, not compelling prose.

16. **Missing the privilege log interaction** — If a time entry describes review of a document
    that is being withheld on privilege, the narrative must align with (and not contradict) the
    privilege log description. Check for this interaction in litigation matters.

17. **Assuming the narrative will not be seen** — In litigation, billing records are frequently
    produced in discovery. In regulatory matters, fee applications are public filings. Write
    every narrative as if a federal judge will review it — because one day, one might.

---

## Writing Standards

Apply plain-language discipline to all billing narratives:

**For time entry narratives:**

- **Lead with the action verb** — not "Further review of..." but "Reviewed..."
- **Name specific documents** — not "the contract" but "[Party] Master Services Agreement, Section 4"
- **Name specific people by role** — "opposing counsel [Smith]" or "client's CFO"; avoid generic "client"
- **State the purpose in a prepositional phrase** — "in preparation for," "in connection with," "regarding"
- **Use past tense** — billing entries are retrospective; use "drafted," not "draft"
- **One task per entry** — if you're writing "and" between two distinct legal tasks, split the entry
- **Avoid Latin and unnecessary legalese** — "court filing" not "submission to the tribunal"; clients
  should be able to understand what they paid for

**Length guidelines:**

- Short tasks (.1–.3 hours): one complete sentence is sufficient
- Medium tasks (.4–1.5 hours): one to two sentences identifying task, subject, and purpose
- Long tasks (1.6+ hours): two to three sentences noting task, subject, purpose, and key output

**Quality gates before delivery:**

1. Could a non-lawyer client understand what the timekeeper did?
2. Could a billing reviewer confirm the task against the task code without asking questions?
3. Does the narrative contain any vague words flagged in the client's OCG prohibited list?
4. If this entry appeared in a fee petition exhibit, would a judge be able to assess its reasonableness?
5. Does this narrative accurately describe what happened, or has specificity been added that the timekeeper did not provide?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research and
guideline look-up tool.

**With legalcode-mcp connected (preferred):**

- Look up the specific client's billing guideline document if available in the legalcode database
- Verify current ABA UTBMS code set against authoritative source
- Look up relevant fee petition case law for the governing jurisdiction
- Look up applicable state bar ethics opinions on billing narrative standards
- Mark all legalcode-mcp-sourced standards as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Apply general UTBMS standards and mark any specific guideline reference [VERIFY]
- Flag all ethics rule references with [VERIFY — check current state RPC]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus analysis on structural quality (Six-Element Framework, block billing detection,
  task code assignment) rather than specific platform or guideline verification

**Billing software integration** (where connected):

- If integrated with a time and billing system (Intapp Time, BigTime, TimeSolv, Aderant,
  Elite 3E, Clio), pull entry data from the connected system rather than requiring manual paste
- Write improved narratives back to the connected system where supported
- Flag entries for timekeeper review in the billing system workflow

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Billing Narrative Review — [Matter Name / Invoice Number]

**Law Firm**: [firm name]
**Timekeeper(s)**: [names and classifications]
**Billing Period**: [start date]–[end date]
**Matter Type**: [Litigation / Transactional / etc.]
**UTBMS Code Set**: [L-codes / A-codes / Mixed]
**Client Guidelines**: [OCG name or "General UTBMS standards"]
**E-Billing Platform**: [platform name or "Not specified"]
**Operating Mode**: [Generate / Improve / Convert / Validate / Mixed]
**Date of Review**: [today's date]

---

## Summary

| Metric                             | Count |
| ---------------------------------- | ----- |
| Total entries reviewed             | [N]   |
| COMPLIANT (no action)              | [N]   |
| PARTIAL (minor improvement)        | [N]   |
| NON-COMPLIANT (rewrite required)   | [N]   |
| Block-billed entries identified    | [N]   |
| Entries requiring timekeeper input | [N]   |
| Task code corrections              | [N]   |

**Overall compliance rate**: [X]%
**Top issue**: [most common finding in one sentence]

---

## Tier 1 — Submission Blockers

[List of NON-COMPLIANT entries with original text, finding, and improved narrative]

### Entry [#] — NON-COMPLIANT

**Original**: "[original narrative]"
**Finding**: [specific deficiency]
**Improved**: "[improved narrative]"
**Task Code**: [corrected code] | **Activity Code**: [corrected code]
**Confidence**: [level]

---

## Tier 2 — PARTIAL Entries (Minor Improvement Required)

[List of PARTIAL entries with original, finding, and improved narrative]

### Entry [#] — PARTIAL

**Original**: "[original narrative]"
**Finding**: [missing element]
**Improved**: "[improved narrative]"
**Task Code**: [code] | **Activity Code**: [code]
**Confidence**: [level]

---

## Tier 3 — COMPLIANT Entries (Code Adjustments Only)

[List of entries that are substantively compliant but may need task code corrections]

| Entry | Date   | Timekeeper | Hours | Finding                           |
| ----- | ------ | ---------- | ----- | --------------------------------- |
| [#]   | [date] | [name]     | [hrs] | [task code corrected / no action] |

---

## Block Billing Decompositions

[Full before/after for each converted entry, marked ⚠ for timekeeper confirmation]

---

## Entries Requiring Timekeeper Input

[List of entries that cannot be improved without additional factual information]

| Entry | Date   | Timekeeper | Hours | Information Needed    |
| ----- | ------ | ---------- | ----- | --------------------- |
| [#]   | [date] | [name]     | [hrs] | "[specific question]" |

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic for billing narrative structure, but jurisdiction-specific
considerations apply in these areas:

**Fee petition standards** [JURISDICTION-SPECIFIC]:

- **US Federal Courts**: Hensley v. Eckerhart lodestar standard; specific circuit variations
  in how block billing reductions are applied [VERIFY per circuit]
- **US State Courts**: State-specific fee shifting statutes vary significantly [VERIFY]
- **England & Wales**: Detailed assessment under CPR Part 47; Queen's Bench Guidelines on
  assessment [VERIFY]; different narrative requirements for costs budgets vs. detailed assessment
- **Canada**: Tariff-based or solicitor-client cost assessment depending on province [VERIFY]

**Professional conduct** [JURISDICTION-SPECIFIC]:

- Ethics rules are state/jurisdiction-specific. ABA Model Rule 1.5 is the template; states
  may have stricter or different requirements. Always verify under the applicable jurisdiction.

**Language requirements** [JURISDICTION-SPECIFIC]:

- Some jurisdictions require billing narratives in the local language for court submissions
  (e.g., French in Quebec for provincial court matters, German for certain German court filings)
- Client contracts may specify the language for invoice descriptions

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on ABA UTBMS task code
standards, LEDES 1998B format specifications, ACC/ACCA model outside counsel guideline
billing requirements, published judicial opinions on lodestar billing narrative standards,
and Legalcode's billing workflow research pipeline. Complements the
`legalcode-outside-counsel-guidelines` and `legalcode-legal-spend-analysis` skills in the
Legalcode legal operations workflow family.
