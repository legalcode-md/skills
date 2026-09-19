---
name: legalcode-invoice-reviewer
description: 'Review outside counsel invoices against billing guidelines — flag block billing, vague narratives,
  excessive hours, rate non-compliance, improper staffing, prohibited charges, and mathematical errors.
  Generates confidence-scored adjustment memoranda with specific deductions, justifications, and recommended
  remediation. Use when a legal operations team, in-house counsel, or billing specialist needs to audit
  law firm invoices for compliance with outside counsel guidelines (OCGs), company billing policies, or
  general legal billing standards. Supports single-invoice review and batch processing. Also triggers
  on: legal invoice audit, legal billing review, billing guideline compliance, law firm invoice dispute,
  LEDES invoice review, UTBMS code audit, outside counsel billing compliance, block-billing analysis,
  excessive legal fees, legal spend audit, invoice adjustment memo, billing reduction letter, legal fee
  reasonableness, ABA Rule 1.5 fee review.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Invoice Reviewer

> **Disclaimer**: This skill provides a framework for AI-assisted outside counsel invoice
> review. It does not constitute legal advice, accounting advice, or bar ethics guidance.
> All outputs should be reviewed by a qualified legal operations professional or in-house
> counsel before communicating adjustments to outside counsel. Billing ethics rules and
> professional responsibility standards vary by jurisdiction and bar association — verify
> current applicability before relying on any provision described here. Benchmarks and
> thresholds cited in this skill represent common market standards and published survey
> data; actual reasonableness depends on matter complexity, jurisdiction, and context.
> Statistical and benchmark references carry standard hallucination risk — verify against
> authoritative sources before applying.

---

## Purpose and Scope

This skill enables AI-assisted review of outside counsel invoices for compliance with
billing guidelines and legal billing standards. It identifies violations, classifies
their severity, generates specific adjustment recommendations, and produces a
confidence-scored adjustment memorandum suitable for sending to outside counsel.

**Covers:**

- Block billing detection and quantification
- Vague and insufficient narrative analysis
- Excessive time identification against task benchmarks
- Rate and timekeeper compliance verification
- Staffing and seniority analysis
- Prohibited charge detection
- Mathematical and administrative error checking
- LEDES/UTBMS format compliance analysis
- Duplicate billing detection
- Travel billing compliance
- Adjustment memorandum generation with specific deductions
- Batch invoice analysis across multiple matters or time periods

**Does not:**

- Provide legal advice or replace qualified counsel
- Constitute a formal fee dispute or legal proceeding
- Apply to any single jurisdiction exclusively — jurisdiction-agnostic with
  [JURISDICTION-SPECIFIC] markers for professional responsibility rules
- Guarantee that adjustment positions will be upheld in fee dispute proceedings
- Replace the judgment of experienced billing specialists for complex matters

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Invoice review is governed by:

1. The controlling Outside Counsel Guidelines (OCGs) or bilateral engagement agreement
2. The applicable bar association's rules on fee reasonableness
3. General professional responsibility standards on fee billing

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **United States**: ABA Model Rules of Professional Conduct Rule 1.5 (fee reasonableness);
  state bar rules that may be more restrictive; UTBMS/LEDES format requirements from the
  client's e-billing platform [VERIFY applicable state rules]
- **United Kingdom**: SRA Code of Conduct and Transparency Rules; solicitor duty to charge
  reasonable and proportionate costs; cost budgeting obligations under CPR PD 3E [VERIFY]
- **Canada**: Law Society rules on fee reasonableness; provincial bar guidelines [VERIFY]
- **Australia**: Legal Services Commissioner guidelines; proportionality requirements
  under the Legal Profession Uniform Law [VERIFY]
- **EU / Continental Europe**: Local bar association fee rules; VAT billing requirements;
  note that hourly billing is less prevalent — AFAs are common [VERIFY]
- **Currency and tax**: Ensure rate analysis accounts for local currency, VAT/GST
  treatment, and cross-border invoice requirements [JURISDICTION-SPECIFIC]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The answer would change the scope or direction of the review
- Multiple valid adjustment approaches exist and organizational policy matters
- Ambiguous entries require context that only the user can provide
- The applicable billing standard is unclear or the OCG is absent

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

### Step 1: Accept Invoice(s) and Guidelines

Accept input in any of these formats:

**Invoice formats:**

- **LEDES file**: Standard LEDES98B or LEDES XML format from an e-billing platform
- **PDF or DOCX**: Scanned or exported invoice document
- **Spreadsheet**: CSV or Excel export from a billing system
- **Pasted text**: Invoice line items copied into the conversation

**Guideline formats:**

- **OCG document**: The organization's Outside Counsel Guidelines (PDF, DOCX, or text)
- **Billing policy summary**: Key billing rules provided by the user
- **No guidelines provided**: Proceed against general market standards (state explicitly)

If no invoice is provided, prompt the user to supply one. If no OCG is provided, note
that the review will use general commercial billing standards and flag this prominently.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions:

1. **Review scope**:
   - Options: Single invoice (full detail), Batch of invoices (summary with top findings),
     Specific violation category only (e.g., block billing only), Full audit with
     memorandum draft
   - _Why this matters_: Determines depth of analysis and output format.

2. **Applicable guidelines**:
   - Options: Use the OCG provided, Apply organization's standard billing rules (describe),
     Use general ABA/market standards — no specific OCG
   - _Why this matters_: The threshold for what constitutes a violation differs
     significantly between OCGs. Some prohibit any block billing; others set a 3-hour
     threshold.

3. **Matter type**:
   - Options: Litigation (trial/arbitration), Litigation (pre-trial / discovery),
     Transactional (M&A, financing), Regulatory / compliance, Employment / labor,
     IP / patent prosecution, General commercial, Real estate, Other
   - _Why this matters_: Time benchmarks vary dramatically by matter type.
     Patent prosecution time norms differ from M&A due diligence.

4. **Adjustment posture**:
   - Options: Strict (apply every guideline provision), Standard (apply material
     violations only), Collaborative (flag issues for discussion, not hard deductions)
   - _Why this matters_: Determines whether to deduct on every technical violation or
     only on material ones. Affects tone and approach of the memorandum.

5. **Timekeeper rate schedule**:
   - Provide the approved rate schedule or rate card if available.
   - If not available, state that rate compliance cannot be verified without it.
   - _Why this matters_: Rate compliance analysis requires the approved schedule.

If partial context is provided, proceed with what is available and **state assumptions
explicitly** at the top of the output.

### Step 3: Load and Parse the OCG

If an OCG or billing guidelines document is provided:

1. **Identify the key billing provisions**:
   - Block billing rules (threshold, if any)
   - Prohibited timekeeper categories or tasks
   - Rate increase notification requirements
   - Expense policies (per-diem amounts, first-class travel prohibition, etc.)
   - Staffing requirements (partner involvement caps, supervision ratios)
   - Required invoice format (LEDES, narrative requirements, minimum entry specificity)
   - Budget and pre-authorization requirements
   - Billing increment rules (0.1-hour vs. 0.25-hour minimum)

2. **Flag any ambiguous or conflicting provisions**:

   **⟁ CLARIFY** — If the OCG contains provisions that are ambiguous or that conflict
   with each other:
   - Present the specific conflict: "Your OCG Section 3.2 prohibits block billing over
     2 hours, but Section 5.1 appears to allow consolidated entries for travel. Do you
     want me to treat multi-task travel entries as exempt from the block billing rule,
     or apply it consistently?"

3. **Build a working rules reference**:
   Extract the OCG provisions into a structured rules table used throughout the review:

   | Rule                             | Source (OCG Section) | Threshold / Limit             | Violation Action  |
   | -------------------------------- | -------------------- | ----------------------------- | ----------------- |
   | Block billing                    | § [X]                | [e.g., >2 tasks in one entry] | Deduct / Reduce   |
   | Hourly increment                 | § [X]                | [e.g., 0.1 hr min]            | Adjust to minimum |
   | Maximum hours/day per timekeeper | § [X]                | [e.g., 14 hrs]                | Flag for review   |
   | Prohibited charges               | § [X]                | [list]                        | Deduct            |
   | Rate compliance                  | § [X]                | [per approved schedule]       | Deduct excess     |
   | Expense per-diems                | § [X]                | [amounts by category]         | Deduct excess     |

**If no OCG is provided:**
Proceed using general market standards as documented in the **Billing Standards
Reference** section. Label the output: "Reviewed against general market standards —
not against a specific outside counsel guidelines document."

### Step 4: Pre-Processing and Invoice Intake

Before running violation analysis, establish a clean baseline:

1. **Invoice summary**: Extract and confirm:
   - Law firm name
   - Invoice number and date
   - Matter number and description
   - Billing period
   - Total fees billed (before expenses)
   - Total expenses billed
   - Total invoice amount
   - Number of timekeepers and names
   - Number of line items

2. **Timekeeper roster**: List each timekeeper with:
   - Name and role/title
   - Billed rate
   - Approved rate (if rate schedule available)
   - Total hours billed
   - Total fees billed

3. **Mathematical pre-check**: Verify arithmetic:
   - Each line item: hours × rate = fees (flag any line-item errors)
   - Column totals: sum of line items = invoice subtotals
   - Grand total: fees + expenses = total due

4. **LEDES/UTBMS format check** (if LEDES file provided):
   - Verify required LEDES fields are present and populated
   - Identify any invalid or non-standard UTBMS task codes, activity codes, or expense codes
   - Flag missing or malformed LEDES fields

   **⟁ CLARIFY** — If the invoice contains entries in a matter or practice area
   unfamiliar from the context provided:
   - "I see entries for [matter type X] billed at [rate Y]. Is this within the expected
     scope of this engagement, or should these be flagged for further investigation?"

### Step 5: Systematic Violation Scan

Conduct a complete line-by-line scan against all violation categories in the **Billing
Violation Reference Catalogue** below. For each entry, assess:

- Does it trigger any violation in the catalogue?
- If yes, which category? (assign violation codes per the catalogue)
- What is the severity? (DEDUCT / FLAG / PASS)
- What is the proposed adjustment? (specific amount or percentage)

Work through all line items before scoring severity — some entries are only identifiable
as violations in the context of other entries (e.g., duplicative work across timekeepers).

**⟁ CLARIFY** — For entries where violation depends on context not visible in the
invoice (e.g., a narrative says "research re: regulatory compliance" but it is unclear
whether this was previously researched):

- Flag for user review rather than making a hard deduction
- Ask: "This entry appears to duplicate earlier research. Can you confirm whether
  [Timekeeper A]'s research on [date] covered the same scope as this entry?"

**⟁ CLARIFY** — For complex matters (50+ line items or multiple matters in one invoice):

- Ask whether to perform a full line-by-line scan or a representative sample audit
  of high-risk entries
- Recommend full scan for invoices under $50K and sample audit for larger invoices
  if the user wants to prioritize efficiency

### Step 6: Rate and Timekeeper Compliance

If an approved rate schedule is available:

1. **Rate verification**: For each timekeeper, compare billed rate to approved rate
2. **Rate increase compliance**: Check whether any rate increased during the period
   without the required advance notice
3. **Unauthorized timekeepers**: Flag any timekeeper not on the approved roster
4. **Billing increment compliance**: Verify minimum billing increment rules are followed
   (e.g., 0.1-hour minimum means a 5-minute call should be billed at 0.1 hours)
5. **Role-rate alignment**: Check whether paralegals, associates, or contract attorneys
   are billed at rates inconsistent with their stated role

**⟁ CLARIFY** — If the rate schedule is not available:

- Note that rate compliance cannot be verified
- Ask whether the user can provide approved rates, even informally
- If not available, state in the memorandum that rates were not independently verified

### Step 7: Staffing and Efficiency Analysis

Assess the overall staffing picture across all line items:

1. **Headcount by task**: Group entries by task category. Were more attorneys deployed
   than necessary for the complexity of each task?

2. **Supervision ratios**: Examine partner-to-associate ratios. Excessive partner
   supervision of routine associate tasks is a common billing issue.

3. **Depositions and hearings**: How many timekeepers attended? Most OCGs cap attendance
   at one or two attorneys per proceeding. Multiple timekeepers billing for the same
   deposition or hearing is a common FLAG item.

4. **Internal conferences**: Multiple timekeepers billing for the same internal meeting
   or status call. Unless justified by matter complexity, only one attorney's time
   should be charged to the client for routine internal coordination.

5. **Excessive associate hours on routine tasks**: Compare associate time on standard
   tasks against the benchmarks in the **Time Benchmarks Reference** section.

6. **Learning curve**: New timekeepers billing significant time to understand the matter
   ("getting up to speed"). OCGs commonly prohibit billing for orientation time.

7. **Seniority creep**: Partner or senior associate time billed for tasks that paralegals
   or junior associates should handle (filing, basic research, document preparation).

### Step 8: Aggregate Analysis and Priority Scoring

After completing the line-by-line scan:

1. **Aggregate by violation category**: Total estimated adjustment by category
2. **Sort by materiality**: Identify the top 5 line items or patterns by dollar value
3. **Classify severity**: Apply the **Violation Severity Classification** to each finding
4. **Calculate total proposed adjustment**: Sum of DEDUCT items
5. **Calculate adjustment as percentage of invoice**: Flag if total exceeds 25% (may
   warrant discussion rather than silent memo)

**⟁ CLARIFY** — If the proposed total adjustment exceeds 20-25% of the invoice:

- Present findings to the user before drafting the memorandum
- Note that large adjustments may benefit from a call with outside counsel rather than
  a written memo alone
- Ask: "The proposed adjustments total [amount] ([X]% of the invoice). Should I draft
  a formal adjustment memo, or draft a talking-points summary for a discussion call first?"

### Step 9: Draft Adjustment Memorandum

Draft the adjustment memorandum following the **Output Format Template** below.

**⟁ CLARIFY** — Before drafting, confirm the tone:

- **Formal**: Standard adjustment memo format, third-person, no explanatory preamble
- **Collaborative**: Begin with acknowledgment of good work, frame adjustments as
  process improvements, offer to discuss
- **Firm**: Lead with dollar amounts, cite OCG provisions explicitly, set a response deadline

For each violation, use the format defined in the **Adjustment Entry Format** section.
Apply the **Writing Standards** discipline throughout.

### Step 10: Quality Verification

Before delivering the memorandum, run the quality checks in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every DEDUCT item, run the 2-pass Self-Interrogation. Revise if any pass reveals
   a weakness.
3. Assign a Confidence Score to each material finding.
4. Verify completeness: confirm all 12 violation categories have been assessed.
5. Cross-check: verify that all arithmetic in the memorandum is correct.
6. Generate the Glass Box Audit Trail and append it to the output.

### Step 11: Deliver Memorandum and Summary Reporting

Deliver:

1. **Executive summary**: Total invoice, proposed adjustments by category, adjusted total
2. **Full adjustment memorandum**: Ready to send (or customized before sending)
3. **Trending notes** (if batch processing): Patterns across multiple invoices or periods
4. **Recommendations**: Systemic issues to address in OCG updates, timekeeper conversations,
   or billing training
5. **Glass Box audit trail**: Traceability record

---

## Billing Violation Reference Catalogue

This catalogue defines every recognized billing violation category. Use it as the
analytical backbone of Step 5. Each category has: a definition, OCG-standard rules,
specific detection tests, and recommended adjustment approach.

### V01 — Block Billing

**Definition**: Combining multiple distinct tasks into a single time entry without
specifying the time spent on each individual task. Block billing prevents the client
from assessing whether the time allocated to each task was reasonable.

**Example of block billing (VIOLATION)**:

> "4.2 hrs — Reviewed discovery requests; researched privilege issues; drafted letter
> to opposing counsel; telephone conference with client"

**Example of proper billing (PASS)**:

> "0.8 hrs — Reviewed plaintiff's third set of interrogatories and request for production;
> identified key issues for privilege log preparation"

**Detection tests**:

- Single entry lists two or more distinct, separable tasks
- Combined time exceeds the OCG threshold (commonly 2.0 hours or 3.0 hours, or any
  multi-task entry if the OCG prohibits block billing entirely)
- Entry contains conjunctions linking different task types (";", "and", "additionally",
  "also reviewed")

**Typical OCG rules**:

- Many OCGs prohibit block billing of any two distinct tasks regardless of time
- Others set a threshold: "time entries combining multiple tasks in a single entry are
  only acceptable if total time does not exceed 2.0 hours"
- If no OCG, market standard: flag blocks over 2.0 hours or entries combining 3+ tasks

**Adjustment approach**:

- Reduce blocked entry by 25-50% depending on the number of tasks combined and ability
  to assess reasonableness
- Document specifically: "Entry combines [N] distinct tasks. Applying a [X]% reduction
  per § [OCG section] / general billing guidelines."
- Alternative: request itemized rebilling (preferred over a percentage reduction where
  possible)

**Severity**: DEDUCT (if OCG explicitly prohibits) or FLAG (if no explicit OCG rule)

---

### V02 — Vague and Insufficient Narratives

**Definition**: Time entries that fail to provide adequate description of the work
performed. Vague entries make it impossible to assess whether the time was reasonable
or whether the task falls within the scope of the matter.

**Example of vague entry (VIOLATION)**:

> "3.0 hrs — Research"

**Example of vague entry (VIOLATION)**:

> "1.5 hrs — Review documents"

**Example of vague entry (VIOLATION)**:

> "2.0 hrs — Attention to matter"

**Example of vague entry (VIOLATION)**:

> "1.0 hr — Email correspondence"

**Example of sufficient entry (PASS)**:

> "1.0 hr — Reviewed [opposing party]'s motion for summary judgment on statute of
> limitations grounds; identified three key factual disputes requiring declaration support;
> drafted notes for response brief"

**Detection tests**:

- Narrative consists of a single noun without subject or object ("research," "review")
- No identification of what was researched, reviewed, or addressed
- No outcome or deliverable indicated
- Boilerplate phrases: "attention to matter," "case management," "miscellaneous"
- Vague email entries: "email correspondence" without specifying subject, recipient,
  or purpose

**Required narrative elements** (minimum standard):

1. **What** was done (the task)
2. **What** it pertained to (the subject)
3. **For what purpose** or with what outcome (the deliverable or decision)

**Adjustment approach**:

- Request rebilling with adequate description
- If pattern is systemic, apply a reduction to all affected entries (typically 15-25%)
- Never approve "attention to matter" or "miscellaneous" entries

**Severity**: FLAG (request clarification) → DEDUCT if unremedied

---

### V03 — Excessive Time

**Definition**: Time entries reflecting more hours than are reasonable for the task
described, considering matter complexity, timekeeper experience, and professional standards.

**Detection approach**:

1. Compare against benchmarks in the **Time Benchmarks Reference** below
2. Review total daily hours per timekeeper (>12 hours in a day raises serious questions;
   > 14 hours is almost never justifiable)
3. Look for task repetition — same task type billed again at a later date by the same
   timekeeper without new developments justifying re-work
4. Partner hours on routine tasks: a senior partner billing 4.0 hours to draft a
   routine motion that a mid-level associate should draft in 2.0 hours

**Red flag patterns**:

- 8+ hours for a "research" entry on a settled legal question
- 6+ hours to draft a short legal memorandum (under 15 pages) by a senior attorney
- 3+ hours for a routine call or conference
- Duplicate research by two attorneys on the same legal issue
- Re-drafting documents previously completed without apparent cause
- Billing 10.0+ hours per day across multiple timekeepers on a non-urgent, routine matter

**Adjustment approach**:

- Reduce to the benchmark amount documented in the **Time Benchmarks Reference**
- Document: "Entry of [X] hours for [task] exceeds the reasonable time for this task
  for a [seniority] attorney. Adjusting to [Y] hours."

**Severity**: FLAG (mild excess) or DEDUCT (significant excess against benchmark)

---

### V04 — Rate Non-Compliance

**Definition**: Billing at rates higher than those approved in the engagement agreement,
rate card, or OCG, including unauthorized mid-period rate increases.

**Detection tests**:

- Billed rate exceeds approved rate for the timekeeper
- Rate increase occurred mid-period without the required advance notice (typically 30-60
  days per most OCGs)
- New timekeeper added to the matter at a rate above the approved tier
- Blended rate used when individual rates were approved (or vice versa)
- Paralegal billed at attorney rates
- Contract attorney or staff attorney billed at associate rates without disclosure

**Adjustment approach**:

- Deduct the difference: (billed rate − approved rate) × hours
- For unauthorized increases: revert to prior-period rates for all affected entries
- Document: "Timekeeper [name] billed at $[rate]; approved rate is $[rate]. Adjusting
  for [X] hours → deduction of $[amount]."

**Severity**: DEDUCT (rate variance) — no discretion once rate schedule is confirmed

---

### V05 — Staffing Issues

**Definition**: Billing for more attorney time than the task or proceeding reasonably
requires, including over-staffing, excessive supervision, and inappropriate seniority
deployment.

**Sub-categories:**

**V05a — Over-Staffing at Depositions/Hearings**: More attorneys attending than the
client authorized or than the matter reasonably requires. Most OCGs cap deposition
attendance at one lead attorney + one associate for complex depositions; routine
depositions may only warrant one attorney.

**V05b — Excessive Supervision**: Partner reviewing and revising associate work product
beyond what is reasonable. Some supervisory billing is appropriate; billing 3.0 hours
to review a 2-page letter drafted by an associate is not.

**V05c — Duplicative Internal Conferences**: Multiple timekeepers billing for the same
internal strategy meeting, status call, or briefing. If four timekeepers attend a 1.0-hour
internal call, the client is billed 4.0 hours for a 1.0-hour internal coordination event.

**V05d — Seniority Creep**: Partner or senior associate time billed for tasks that should
be handled by more junior timekeepers (filing documents, basic research on settled law,
drafting routine correspondence, organizing documents).

**V05e — Learning Curve**: New timekeepers billing orientation time, background reading
on established matter history, or initial research duplicating prior work to get up to
speed. Most OCGs prohibit billing clients for timekeeper education or orientation.

**Adjustment approach**:

- V05a: Deduct time of excess attendees beyond the authorized cap
- V05b: Reduce supervisory time to a reasonable level (typically 10-20% of the
  underlying work product time)
- V05c: Accept only one or two timekeepers' time for routine internal calls; deduct
  remaining attendees
- V05d: Reduce to the rate and expected time for the appropriate seniority level
- V05e: Deduct all orientation/learning-curve time

**Severity**: DEDUCT (V05a, V05e) or FLAG (V05b, V05c, V05d — depends on context)

---

### V06 — Prohibited Charges

**Definition**: Billing for tasks, activities, or expenses that the OCG or standard
practice explicitly excludes from client billing.

**Common prohibited charges (verify against applicable OCG):**

**Administrative and clerical tasks**:

- Filing documents (court filing, document management)
- Photocopying and scanning at cost-per-page rates
- Word processing
- Faxing
- Organizing or labeling files
- Calendaring and docketing
- Internal billing or account management

**Overhead and firm costs**:

- Library or research database charges (LexisNexis, Westlaw, Bloomberg — overhead
  cost in most OCGs)
- Secretarial overtime
- Internal training and legal education (CLEs, firm retreats)
- New attorney orientation or bar exam preparation
- Proofreading services
- Office supplies

**Travel-related (see also V09)**:

- First-class airfare (most OCGs require coach/economy unless pre-approved)
- Premium hotel accommodations above the OCG per-diem
- Personal meals at non-client meetings
- Local transportation above per-diem or standard rates
- Travel time billed at full rates (most OCGs cap travel time at 50% or prohibit it)

**Billing or account administration**:

- Time spent preparing or reviewing the firm's own invoices
- Billing memo time (attorney time to review and approve bills for submission)

**Adjustment approach**:

- Deduct 100% of prohibited charges
- Document each charge category separately in the memorandum

**Severity**: DEDUCT — prohibited charges are non-negotiable deductions

---

### V07 — Mathematical and Administrative Errors

**Definition**: Arithmetic errors, transposition errors, or formatting errors that result
in incorrect amounts on the invoice.

**Detection tests**:

- Hours × rate ≠ line-item fee
- Sum of line items ≠ subtotal
- Subtotals + expenses ≠ grand total
- Same line item appears twice
- Invoice date range does not match actual entry dates
- Time entries outside the stated billing period

**Adjustment approach**:

- Correct all mathematical errors
- Deduct or credit as appropriate
- Note: mathematical errors do not require a percentage reduction — the correction is
  the exact arithmetic result

**Severity**: DEDUCT (automatic — no discretion on arithmetic errors)

---

### V08 — Lumping and Splitting

**Definition**: Lumping is combining distinct matters onto a single invoice (improper
allocation making individual matter analysis impossible). Splitting is artificially
dividing a single task across multiple entries to obscure time totals.

**Lumping detection**:

- Single invoice covering multiple matter numbers without clear delineation
- Time entries that reference different matters or workstreams without matter-level
  sub-totals

**Splitting detection**:

- Multiple consecutive entries by the same timekeeper on the same day for the same task
  (e.g., three separate "legal research" entries of 0.5 hours each on the same day for
  the same issue, which should be one 1.5-hour entry)
- Entries that break a single deliverable across multiple dates to avoid scrutiny of
  total time

**Adjustment approach**:

- Lumping: Request re-invoicing with proper matter-level allocation
- Splitting: Consolidate into a single entry; do not automatically reduce, but flag
  for transparency

**Severity**: FLAG → DEDUCT if pattern is intentional or recurring

---

### V09 — Travel Billing

**Definition**: Billing for travel time or travel expenses in ways that exceed the
client's policy or general market standards.

**Common travel billing issues**:

- **Travel time at full rate**: Most OCGs limit travel time billing to 50% of the standard
  rate, or prohibit billing for travel time unless the attorney is working during travel
  (documented)
- **First-class or business-class airfare**: Prohibited unless pre-approved or flight
  over a threshold duration (varies by OCG — commonly 6 or 8 hours for business class)
- **Overnight travel for proximity matters**: Out-of-town counsel billing travel to attend
  a hearing in their own city
- **Hotel above per-diem**: Most OCGs set a per-diem for hotel accommodations
- **Meal expenses above per-diem**: Personal dining expenses above the OCG meal allowance
- **Out-of-town counsel for local tasks**: Using remote attorneys when local counsel
  would avoid travel costs entirely

**Adjustment approach**:

- Travel time: Reduce to the OCG-allowed percentage or amount
- Airfare: Deduct the premium above economy/coach equivalent
- Hotel/meals: Deduct amounts above the per-diem
- Document with OCG citation

**Severity**: DEDUCT (rate excess, prohibited premium) or FLAG (documentation issue)

---

### V10 — Duplicate Billing

**Definition**: Billing for the same task or work product more than once, either within
a single invoice or across billing periods.

**Detection tests**:

- Identical or near-identical narrative on two entries by the same or different timekeepers
- Research on the same legal issue appearing multiple times across timekeepers
- Documents drafted, revised, and re-drafted without apparent cause (no new developments)
- Same conference or call appearing in multiple timekeepers' entries for more time than
  the conference duration

**Adjustment approach**:

- Full deduction for identical duplicate entries
- Partial deduction for substantially duplicative work
- Flag for explanation before deducting if the duplicate work is unclear

**Severity**: DEDUCT (clear duplicates) or FLAG (apparent duplicates needing explanation)

---

### V11 — LEDES / UTBMS Non-Compliance

**Definition**: Invoice submitted in a format that does not comply with the required
LEDES standard or UTBMS coding requirements.

**Common LEDES/UTBMS issues**:

- Invalid or deprecated task codes (e.g., non-standard codes outside the UTBMS catalog)
- Mismatched activity codes (e.g., activity A108 "Legal Research" used for drafting tasks)
- Missing required LEDES fields (client matter ID, timekeeper bar number, billing date)
- LEDES format version mismatch
- Expenses coded to task codes rather than expense codes
- All time coded to a single task code regardless of actual task performed

**Adjustment approach**:

- Request corrected LEDES submission; do not pay until format compliance is achieved
  if the OCG requires electronic billing
- For material coding errors, request re-coding before processing

**Severity**: FLAG (processing hold) or DEDUCT if the OCG imposes penalties for
non-compliant submissions

---

### V12 — Budget and Authorization Violations

**Definition**: Billing for work that exceeds an approved matter budget without prior
client authorization, or for work requiring pre-approval that was not obtained.

**Detection tests**:

- Invoice total would cause the cumulative billing to exceed the approved matter budget
- Specialized tasks (retaining experts, hiring local counsel, filing certain motions)
  that required pre-approval and for which no authorization is on file
- Staffing changes (adding timekeepers not on the approved roster) made without notice

**Adjustment approach**:

- Flag overages with reference to the approved budget
- Deduct amounts for tasks that required pre-authorization if no authorization is
  confirmed
- Request documentation of any verbal authorizations before deducting

**Severity**: FLAG (budget overrun, requires client decision) or DEDUCT (clearly
unauthorized tasks per OCG)

---

## Violation Severity Classification

### DEDUCT — Mandatory Adjustment

The violation is clear, the amount is quantifiable, and the applicable billing standard
(OCG or market standard) supports a deduction. These items should appear as line-item
deductions in the adjustment memorandum.

**Examples:**

- Rate billed above approved rate schedule
- Mathematical errors (hours × rate ≠ fee)
- Prohibited charges (Westlaw research fees, photocopying at standard per-page rates)
- Travel time billed at 100% when OCG caps at 50%
- Entries below the minimum billing increment threshold

**Action**: Deduct the specific calculated amount. Cite the OCG provision or market
standard. Provide the supporting arithmetic.

### FLAG — Investigate and Resolve

The violation is apparent but either (a) the amount is uncertain, (b) the violation
depends on context the invoice does not supply, or (c) the OCG is ambiguous. These
items should appear in the memorandum as queries requiring a response from outside
counsel within a defined period.

**Examples:**

- Vague narratives (cannot assess reasonableness without more detail)
- Possible duplicate research (requires outside counsel confirmation)
- Over-staffing at a deposition (the business decision to attend was potentially theirs)
- Budget overrun (requires explanation before deduction)
- Apparent block billing where the combined time is borderline

**Action**: Request explanation within [14-30] days. State that the entry will be held
or deducted pending satisfactory response.

### PASS — Acceptable

The entry is within billing guidelines and general standards. No adjustment required.

**Action**: No action. Note that the overall bill was reviewed and these items were
accepted.

---

## Adjustment Entry Format

For each DEDUCT or FLAG item, document using this format:

```
Entry No.:     [Invoice line item number or date/timekeeper reference]
Timekeeper:    [Name, title]
Date:          [Date of entry]
Original:      [X.X hrs × $Y/hr = $Z]
Violation:     [Violation code: V01-V12 and brief label]
OCG Basis:     [OCG § citation or "General market standard"]
Analysis:      [One to three sentences: what the entry says, why it violates the standard,
               how the adjustment was calculated]
Proposed Adj:  [$amount deducted / percentage applied / held pending response]
Adjusted Amt:  [$Z − adjustment = adjusted amount]
```

---

## Time Benchmarks Reference

These benchmarks represent common market ranges for standard legal tasks. They are
starting points — not hard rules. Complexity, jurisdiction, and strategy legitimately
affect timing. Use as flags for investigation, not automatic deductions. [VERIFY against
current benchmarks for your jurisdiction and practice area.]

### Litigation Tasks

| Task                                    | Junior Associate | Mid-Level Associate | Senior Associate / Partner |
| --------------------------------------- | ---------------- | ------------------- | -------------------------- |
| Review and analyze complaint (standard) | 2.0–3.5 hrs      | 1.5–2.5 hrs         | 1.0–2.0 hrs                |
| Draft motion to dismiss (standard)      | 10–18 hrs        | 7–12 hrs            | 5–8 hrs                    |
| Draft opposition to summary judgment    | 15–25 hrs        | 10–18 hrs           | 8–14 hrs                   |
| Deposition preparation (per witness)    | 3.0–6.0 hrs      | 2.0–4.0 hrs         | 1.5–3.0 hrs                |
| Take or defend routine deposition       | —                | 3.0–6.0 hrs         | 2.0–4.0 hrs                |
| Draft 1-page privilege log entry        | 0.1–0.2 hrs      | 0.1 hrs             | —                          |
| Review one document for privilege       | 0.1–0.3 hrs      | 0.1–0.2 hrs         | —                          |
| Attend routine case status hearing      | 1.5–3.0 hrs      | 1.0–2.0 hrs         | 1.0–1.5 hrs                |

### Transactional Tasks

| Task                                     | Junior Associate | Mid-Level Associate | Senior Associate / Partner |
| ---------------------------------------- | ---------------- | ------------------- | -------------------------- |
| Review and mark up standard NDA          | 1.0–2.0 hrs      | 0.5–1.0 hrs         | 0.5 hrs                    |
| Review and mark up APA (standard)        | 15–25 hrs        | 10–18 hrs           | 8–12 hrs                   |
| Draft disclosure schedule (standard)     | 8–14 hrs         | 6–10 hrs            | 4–6 hrs                    |
| Review due diligence document (standard) | 0.2–0.5 hrs      | 0.1–0.3 hrs         | —                          |
| Draft ancillary closing documents        | 2.0–4.0 hrs      | 1.5–3.0 hrs         | 1.0–2.0 hrs                |
| Coordinate closing checklist             | 1.0–2.0 hrs      | 0.8–1.5 hrs         | 0.5–1.0 hrs                |
| Draft board resolutions (standard)       | 1.5–3.0 hrs      | 1.0–2.0 hrs         | 0.5–1.5 hrs                |

### Corporate / General Tasks

| Task                                        | All Seniority Levels                |
| ------------------------------------------- | ----------------------------------- |
| Standard 5-minute email reply               | 0.1 hrs                             |
| Substantive email (analysis of issue)       | 0.2–0.5 hrs                         |
| Internal strategy call (30 min)             | 0.5 hrs maximum per attendee        |
| Client call (30 min)                        | 0.5 hrs                             |
| Review short contract (< 10 pages)          | 1.0–2.5 hrs depending on complexity |
| General legal research (settled question)   | 1.0–3.0 hrs                         |
| General legal research (unsettled question) | 3.0–8.0 hrs                         |
| Attendance at 1-hour internal meeting       | 1.0 hrs maximum per attendee        |

**Daily hour caps**: Many major OCGs set a **hard cap of 8.0 hours per timekeeper per
day**, with documented exceptions only for M&A closings, securities offerings, trial
days, and deposition days (which require a notation in the entry explaining the exception).
Without a specific OCG cap, industry auditors flag entries exceeding **10.0 hours per
day** as requiring explanation and flag consecutive days exceeding 10.0 hours as a
systemic pattern. Entries exceeding 14.0 hours per day are presumptively suspect in
any context — verify against the specific OCG before deducting.

**Internal communications threshold**: When internal firm communications (status calls,
team meetings, internal briefings) exceed **10% of total billed hours** on an invoice,
flag for staffing analysis. This threshold commonly triggers a detailed review of
supervision ratios and duplicative attendance.

**Typical audit savings benchmarks**: First-time invoice audits typically identify
adjustments of **6–11% of invoice value**; portfolios with systemic violations may
yield 20–30%. The California State Bar (Advisory 2016-02) estimates block billing alone
inflates client bills by **10–30%** [VERIFY against current advisory text].

---

## Prioritization Framework

When organizing adjustment memoranda, apply this tiered prioritization:

### Priority 1 — Mandatory Deductions

Items where deduction is clear, calculated, and OCG-supported:

- Mathematical errors
- Rate excess above approved schedule
- Prohibited charges (research databases, copying, clerical tasks)
- Unauthorized timekeeper rates
- Travel time billed above OCG cap

**Action**: Deduct. Include in the memorandum without option for rebuttal beyond
factual correction.

### Priority 2 — Material Findings (Deduct or Hold)

Items that are clearly problematic but where outside counsel response may alter the
outcome:

- Block billing over the OCG threshold
- Excessive time entries more than 50% above benchmark
- Over-staffing at depositions or hearings
- Duplicate entries
- Budget overruns

**Action**: Deduct or hold pending response. Set a response deadline (typically 14-30
days). If no response or unsatisfactory response, convert held items to deductions.

### Priority 3 — Advisory Flags (Request Rebilling or Explanation)

Items that may be acceptable with adequate documentation or rebilling:

- Vague narratives (request resubmission with adequate description)
- Borderline time entries (request explanation of scope and complexity)
- New timekeepers not on the approved roster (request advance approval for future)
- LEDES coding errors (request corrected submission)

**Action**: Flag in the memorandum. Request resolution within 30 days. No deduction
until the response period expires.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                             | Fail Action                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Source**     | Every deduction cites the applicable OCG section, or states "General market standard — [source]" | Add citation or mark "[UNVERIFIED — counsel to confirm]"                                      |
| **Format**     | All arithmetic in the memorandum is verified correct                                             | Re-check all calculations                                                                     |
| **Currency**   | Benchmark figures cited are current (survey year specified, or [VERIFY] flagged)                 | Add currency qualifier                                                                        |
| **Domain**     | Analysis stays within the applicable billing standard scope                                      | Remove or flag conclusions that go beyond billing guidelines into professional responsibility |
| **Confidence** | Uncertainty explicitly stated; DEDUCT vs. FLAG classification is not understated                 | Add confidence qualifier                                                                      |

### Self-Interrogation for DEDUCT Items

For any line item classified as DEDUCT (mandatory deduction), apply this 2-pass review
before including in the memorandum:

**Pass 1 — Legal Chain Integrity**:

- Is the deduction precisely grounded in the OCG provision or market standard cited?
- Is the arithmetic correct? (verify manually)
- Could outside counsel offer a legitimate explanation that would change the classification?
- Is the DEDUCT classification proportionate, or should this be a FLAG with a right of response?

**Pass 2 — Completeness**:

- Have all line items affected by this violation type been identified?
- Is the pattern analysis complete — is this isolated or systematic?
- Have any mitigating factors been considered?

If any pass reveals a weakness, revise or reclassify before delivery.
Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                              | Action                                                       |
| ------------ | --------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| **Definite** | 0.95-1.0  | Mathematical error or explicit OCG rule              | State with confidence; no caveat needed                      |
| **High**     | 0.80-0.94 | Clear violation, well-established market standard    | State with brief caveat if OCG is not explicit               |
| **Probable** | 0.60-0.79 | Likely violation, context could change outcome       | Flag for user review; present as FLAG not DEDUCT             |
| **Possible** | 0.40-0.59 | Apparent issue, insufficient information to conclude | Hold pending outside counsel explanation                     |
| **Unlikely** | 0.0-0.39  | Speculative concern                                  | Do not include in memorandum; note in internal analysis only |

---

## Glass Box Audit Trail

Every invoice review output MUST include a Glass Box audit section. This makes the
review traceable and defensible if disputed:

```yaml
glass_box:
  invoice:
    firm: "[Law firm name]"
    invoice_number: "[number]"
    invoice_date: "[date]"
    billing_period: "[start] to [end]"
    matter: "[matter name / number]"
    total_billed: "$[amount]"
  review_basis: "[OCG document title and version / General market standards]"
  ocg_provided: "Yes / No"
  rate_schedule_provided: "Yes / No"
  line_items_reviewed: "[number]"
  timekeepers_reviewed: "[number]"
  violation_categories_checked: "V01 through V12 — all 12 categories"
  legalcode_mcp: "Connected / Not connected"
  findings:
    total_deductions_proposed: "$[amount]"
    total_flags_pending: "$[amount]"
    deductions_as_pct_of_invoice: "[X]%"
    violations_by_category:
      V01_block_billing: "$[amount] / [N] entries"
      V02_vague_narrative: "$[amount] / [N] entries"
      V03_excessive_time: "$[amount] / [N] entries"
      V04_rate_noncompliance: "$[amount] / [N] entries"
      V05_staffing: "$[amount] / [N] entries"
      V06_prohibited_charges: "$[amount] / [N] entries"
      V07_math_errors: "$[amount] / [N] entries"
      V08_lumping_splitting: "$[amount] / [N] entries"
      V09_travel: "$[amount] / [N] entries"
      V10_duplicate: "$[amount] / [N] entries"
      V11_ledes_utbms: "[N issues identified]"
      V12_budget_authorization: "$[amount] / [N] entries"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no DEDUCT items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "[e.g., Rate schedule not provided — V04 analysis incomplete]"
    - "[e.g., Matter background not available — excessive time determinations are conservative]"
  reviewer: "AI-assisted — requires qualified billing specialist or legal ops review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when reviewing legal invoices:

1. **Applying OCG rules that were not in force at the time of billing** — OCGs are
   amended. Verify that the version you are applying was in effect during the billing
   period. Retroactively applying new OCG provisions is a common billing dispute error.

2. **Flat percentage reductions without justification** — Reducing an invoice by 10%
   "across the board" without identifying specific violations is legally and ethically
   indefensible and inconsistent with ABA guidance on fee reasonableness. Every
   deduction must have a specific factual and policy basis.

3. **Conflating vagueness with excessiveness** — A vague entry may be for a reasonable
   amount of time; an excessively timed entry may have an adequate narrative. These are
   distinct violations requiring distinct analyses. Do not penalize for both from the
   same entry without independent bases for each.

4. **Using benchmarks as absolute limits** — Time benchmarks are reference points, not
   caps. A complex motion in a novel area of law may legitimately require twice the
   benchmark time. Benchmarks trigger investigation, not automatic deduction. Always
   request justification before deducting for excessive time alone.

5. **Deducting for block billing without a threshold basis** — If the OCG does not
   explicitly prohibit block billing (or sets a threshold), do not deduct solely on the
   basis that the entry combines tasks. Note as a recommendation for future OCG update
   instead.

6. **Treating all research database charges identically** — Westlaw/LexisNexis charges
   are overhead under most OCGs. But specialist databases (e.g., a specific patent
   prosecution tool, a real-time regulatory monitoring service engaged specifically
   for the matter) may be billable if pre-authorized. Ask before deducting.

7. **Disregarding the matter complexity context** — A junior associate billing 20 hours
   to draft a brief in a complex securities fraud case is different from 20 hours on a
   routine slip-and-fall matter. Always calibrate against matter type and complexity.

8. **Silent deductions without notice** — Unilaterally deducting from an invoice without
   a written adjustment memorandum explaining the basis damages the client-firm
   relationship and may itself create a fee dispute. Every deduction must be documented
   and communicated.

9. **Holding invoices past payment terms without notice** — If an invoice is under review,
   notify outside counsel that payment is being delayed pending billing audit, and specify
   the resolution timeline. Many OCGs and engagement letters specify payment terms that
   can themselves be violated by unexplained payment delays.

10. **Ignoring the systemic pattern** — An isolated block-billing entry may not be worth
    addressing. Fifty block-billing entries across six invoices from the same firm reveal
    a systemic training problem requiring a different intervention (training call, OCG
    reminder) rather than entry-by-entry deductions.

11. **Over-deducting on flagged items before response** — Deducting amounts that are in
    FLAG status (pending outside counsel explanation) before the response period expires
    is premature. Maintain a clear distinction between DEDUCT (already confirmed) and
    FLAG (pending response).

12. **Applying one matter's context to another** — Staffing, time, and expense norms
    differ across matters. Do not apply litigation staffing norms to a transactional
    matter, or patent prosecution benchmarks to employment litigation.

13. **Missing the compound effect** — Multiple small violations across a single invoice
    may each be individually marginal but collectively significant. Report the aggregate
    picture, not only the per-item analysis.

14. **Failing to document the audit trail** — A billing adjustment that cannot be
    explained entry-by-entry is indefensible if the firm disputes the deduction or the
    matter reaches a fee dispute proceeding. Every review must produce a documented
    audit trail.

15. **Using adjustments punitively** — Invoice review is about ensuring billing accuracy
    and guideline compliance, not punishing outside counsel for outcomes on the matter.
    The tone and content of the memorandum should be professional, specific, and
    forward-looking.

16. **Ignoring the relationship dimension** — How an adjustment memorandum is communicated
    matters. A strategic relationship firm with a single vague entry warrants a phone call.
    A commodity vendor with systemic violations warrants a formal deduction memo. Calibrate
    accordingly.

17. **Skipping the mathematical pre-check** — Mathematical errors are the fastest,
    most defensible deductions available. Always verify arithmetic first. Firms rarely
    dispute arithmetic deductions, and finding them early builds credibility for the
    rest of the review.

18. **Not verifying rate schedules before rate deductions** — Never deduct for rate
    non-compliance without confirming the approved rate. If the rate schedule is
    unavailable, note the issue and request the firm to confirm rates — do not assume
    the billed rate is wrong.

19. **Accepting "we will fix it next invoice" without follow-through** — When outside
    counsel agrees to rebill or correct, track that commitment and verify the corrected
    invoice. The cycle of flagging issues that never get resolved undermines the entire
    review program.

20. **Single-invoice review without trend analysis** — A single invoice review is useful
    but not sufficient for legal spend management. Invoice reviews should feed a trend
    database tracking violation rates by firm, matter type, and timekeeper. This data
    drives OCG updates, training, and panel management decisions.

---

## Writing Standards

Apply plain-language discipline to all adjustment memorandum output:

**For adjustment memorandum text** (sent to outside counsel):

- Plain, professional language. No legal jargon where a plain word works.
- Active voice: "Your September invoice includes entries that violate § 3.4 of our OCG"
  — not "It has come to our attention that entries may be found..."
- Short sentences. One point per sentence.
- Specific, not vague: cite the specific entry date, timekeeper, and OCG provision
- Quantified: state the exact dollar amount of each deduction
- Forward-looking: include what action is needed (respond by [date], resubmit, accept adjustment)

**For internal analysis**:

- May include more technical billing analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can outside counsel identify exactly which entry is being questioned from the memo description?
2. Is every deduction supported by a specific arithmetic calculation?
3. Is every OCG citation accurate to the version in effect during the billing period?
4. Is the tone professional and free from pejoratives or accusations?
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Research the applicable bar association's fee reasonableness rules for the jurisdiction
  where outside counsel practices
- Verify current professional responsibility rules on billing (ABA MRPC Rule 1.5 or
  jurisdiction-specific equivalent) [VERIFY current version]
- Search for any recent bar ethics opinions or court decisions on legal fee reasonableness
  in the relevant jurisdiction
- Save the most relevant results to a local temp file (`/tmp/legalcode-invoice-research.md`)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all professional responsibility rule references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the review on the OCG provisions and mathematical/benchmark analysis rather
  than professional responsibility arguments
- Do not create the local research file

---

## Localization Notes

This skill applies primarily to US/UK legal market billing practices. For other
jurisdictions, note these important variations:

[JURISDICTION-SPECIFIC] **United Kingdom**:

- LEDES format is used but UK-specific practice codes differ from US UTBMS
- Solicitors are subject to the SRA Transparency Rules and indemnity principles
- "Costs budgets" under CPR PD 3E (for litigation matters over £25,000) establish
  court-approved budgets that constrain chargeable time [VERIFY current thresholds]
- The Senior Courts Costs Office provides costs assessment services for disputed
  solicitor-client costs
- "Summary assessment" vs. "detailed assessment" procedures govern court-ordered costs

[JURISDICTION-SPECIFIC] **Australia**:

- Legal profession uniform law governs costs disclosure and billing
- "Costs agreements" must be in place; without them, scale fees apply in some states
- Proportionality requirements under the LPUL limit what can be billed to client
  benefit [VERIFY state-specific rules]

[JURISDICTION-SPECIFIC] **Canada**:

- Each provincial law society has its own fee reasonableness rules
- Some provinces use assessment officers for taxation of bills (Ontario: Assessment
  Officer proceedings; BC: Registrar) [VERIFY current procedure for each province]
- Quebec's civil law tradition affects billing norms

[JURISDICTION-SPECIFIC] **Continental Europe**:

- Hourly billing is far less common; fixed-fee, retainer, and contingency structures
  are prevalent in many jurisdictions
- Many EU jurisdictions have advocate tariff systems that limit or guide fees
- VAT treatment on legal fees differs across jurisdictions; ensure billing rates are
  clearly net or gross as required by local law

---

## Output Format Template

Structure the final deliverable as:

```markdown
---

## Invoice Review Summary

**Law Firm**: [firm name]
**Invoice No.**: [number]
**Invoice Date**: [date]
**Billing Period**: [period]
**Matter**: [matter name/number]
**Total Billed**: $[amount]
**Review Basis**: [OCG name and version / General market standards]
**Date of Review**: [date]
**Reviewed by**: AI-assisted review — [reviewer name if applicable]

---

## Executive Summary

| Category  | Gross Billed | Proposed Deductions | FLAGS Pending |
| --------- | ------------ | ------------------- | ------------- |
| Fees      | $[X]         | $[Y]                | $[Z]          |
| Expenses  | $[X]         | $[Y]                | $[Z]          |
| **Total** | **$[X]**     | **$[Y]**            | **$[Z]**      |

**Adjusted Invoice Total (after deductions, pending FLAGS)**: $[amount]

**Top 3 Issues**:

1. [Violation type] — $[amount] proposed deduction — [one-line summary]
2. [Violation type] — $[amount] proposed deduction — [one-line summary]
3. [Violation type] — $[amount] proposed deduction — [one-line summary]

---

## Adjustment Memorandum

[To be sent to outside counsel — professional tone]

[Firm name]
[Date]
Re: Invoice No. [X], Matter [Y], Billing Period [Z]

Dear [Contact at firm]:

We have reviewed the above invoice. The following adjustments are proposed:

### Section 1 — Mandatory Deductions

[Entry No. / Timekeeper / Date]
**Issue**: [violation description]
**Basis**: [OCG § citation or market standard]
**Deduction**: $[amount]

[Repeat for each DEDUCT item]

**Total Section 1 Deductions**: $[amount]

---

### Section 2 — Items Held Pending Response

The following entries are held pending your explanation within [30] days.
If no response is received, these entries will be deducted.

[Entry No. / Timekeeper / Date]
**Issue**: [description of the concern]
**Information Requested**: [what outside counsel should provide]
**Amount Held**: $[amount]

[Repeat for each FLAG item]

**Total Section 2 Held**: $[amount]

---

### Section 3 — Administrative and Formatting Issues

[LEDES/UTBMS coding errors, narrative deficiencies requiring rebilling]

---

### Adjusted Payment

We will process payment of $[adjusted total] within [X] days, representing the invoice
total less Section 1 deductions. Section 2 amounts will be released or adjusted upon
receipt of your response.

Please confirm receipt and provide your response to Section 2 items by [date].

[Name, title, contact information]

---

## Timekeeper Summary

| Timekeeper | Title   | Approved Rate | Billed Rate | Total Hrs | Total Fees | Adj. Fees |
| ---------- | ------- | ------------- | ----------- | --------- | ---------- | --------- |
| [Name]     | [Title] | $[rate]       | $[rate]     | [X] hrs   | $[X]       | $[X]      |

---

## Findings by Violation Category

### V01 — Block Billing: $[total deduction]

[Table of affected entries]

### V02 — Vague Narratives: $[total held]

[Table of affected entries]

[Continue for each category with findings]

---

## Recommendations

**For this invoice**: [Specific next steps]

**For future invoices**: [Systemic issues to address in training or OCG updates]

**Trending**: [Note any patterns across prior invoices if batch analysis was conducted]

---

[Glass Box audit trail — appended per Quality Assurance Framework]

---
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis covering outside counsel invoice
review methodology, drawing on:

- **ABA Model Rules of Professional Conduct Rule 1.5(a)/(b)** — fee reasonableness and
  written disclosure requirements [VERIFY current version]
- **California State Bar Arbitration Advisory 2016-02** — analysis of bill padding and
  block billing; finding that block billing inflates bills by 10–30% [VERIFY]
- **FDIC Outside Counsel Deskbook (November 2025)** — government-sector model for
  comprehensive OCG requirements [VERIFY currency]
- **LEDES Oversight Committee (LOC) / UTBMS standards** — LEDES 1998B, LEDES 2000,
  complete task/activity/expense code sets
- **ACC Value Challenge framework** and **ACC Outside Counsel Guideline practices**
- **CLOC legal operations billing guidance**
- Benchmark data from Brightflag, LegalBillReview.com, Sterling Analytics, and
  AccurateLegalBilling industry resources
- Zscaler, HP, Yahoo, Microsoft, and other publicly available corporate OCG examples
  for billing standard benchmarks
- Legalcode quality assurance frameworks established in `legalcode-contract-review`

Related skills: `legalcode-outside-counsel-guidelines` (OCG drafting and audit),
`legalcode-legal-spend-analysis` (spend benchmarking and ROI), `legalcode-time-narrative`
(billing narrative compliance for law firms).

All statutory and professional responsibility references carry standard hallucination
risk — verify against authoritative sources before applying.
