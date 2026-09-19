---
name: legalcode-deadline-calculator
description: Calculate litigation deadlines based on triggering events, applicable court rules, and jurisdictional
  requirements. Use when computing FRCP response deadlines (answer to complaint, discovery responses,
  MSJ oppositions, post-trial motions), appeals windows (FRAP Rule 4 notice of appeal), statute of limitations
  expiry dates with tolling analysis, EEOC charge filing deadlines (180/300 days), FTCA administrative
  claim windows (2 years + 6 months), government tort claims notice requirements, and regulatory filing
  deadlines.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Calculate litigation deadlines based on triggering events, applicable court rules, and jurisdictional requirements. Use when computing FRCP response deadlines (answer to complaint, discovery responses, MSJ oppositions, post-trial motions), appeals windows (FRAP Rule 4 notice of appeal), statute of limitations expiry dates with tolling analysis, EEOC charge filing deadlines (180/300 days), FTCA administrative claim windows (2 years + 6 months), government tort claims notice requirements, and regulatory filing deadlines. Applies FRCP Rule 6 day-count mechanics including weekend/holiday extensions, service-method additions under Rule 6(d) (2016 amendment), and calendar vs. business day distinctions. Handles multi-jurisdiction deadline tracking for matters pending in multiple courts. Produces deadline calendars with parallel dependency trees, urgency-tiered risk alerts, buffer recommendations, and court-ready outputs including iCal, JSON, and scheduling order language. Jurisdiction-agnostic framework with deep US federal/state coverage and [JURISDICTION-SPECIFIC] markers for England & Wales (CPR), Australia (Federal Court Rules 2011), and EU proceedings.


# Legalcode Deadline Calculator

> **Disclaimer**: This skill provides a framework for AI-assisted litigation deadline
> calculation. It does not constitute legal advice. All computed deadlines must be
> verified by a qualified legal professional licensed in the relevant jurisdiction before
> being acted upon. Deadline calculation errors are a leading cause of legal malpractice.
> Court rules change, local rules vary by district and judge, and this skill may not
> reflect the most recent amendments. Statutory and case law references cited from memory
> carry hallucination risk — verify every citation against authoritative sources before
> relying on them. Never treat an AI-generated deadline as final without independent
> verification.

---

## Purpose and Scope

This skill calculates litigation deadlines from a triggering event, applying the
applicable day-count rules, holiday calendars, service-method modifiers, and tolling
doctrines. It produces auditable deadline outputs with rule citations, confidence
scores, parallel dependency trees, and urgency-tiered risk alerts.

**Covers:**

- FRCP procedural deadlines: answer, 12(b) motions, initial disclosures, discovery
  responses, expert witness disclosures, summary judgment, post-trial motions
- FRAP appellate deadlines: civil and government-party notice of appeal windows,
  post-judgment motion tolling
- Statute of limitations calculation: accrual rules, state-specific periods, tolling
  doctrines (equitable tolling, fraudulent concealment, discovery rule, American Pipe,
  COVID-19 orders, minority/incapacity)
- Administrative claim deadlines: EEOC 180/300-day charge filing, FTCA two-step window,
  Social Security disability appeals, IRS Tax Court petitions, NLRB unfair labor practice
  charges, state government claims acts
- FRCP Rule 6 computation mechanics: calendar days, weekend/holiday extensions, legal
  holiday definition, clerk inaccessibility, service-method additions (including 2016
  amendment eliminating CM/ECF three-day addition)
- Parallel deadline dependency modeling: answer → scheduling order → discovery cutoff →
  expert reports → summary judgment → trial
- Multi-jurisdiction deadline comparison for matters pending in multiple courts
- Buffer recommendations and urgency-tiered risk alerts

**Does not:**

- Replace counsel judgment on discretionary deadline extensions, equitable tolling
  arguments, or emergency relief applications
- Determine the validity of service or authenticate triggering event dates
- Model all local rules across 94 federal districts (checks key patterns; always verify
  local rules for the specific district)
- Provide binding legal advice or guarantee accuracy in any jurisdiction
- See `legalcode-litigation-risk-assessment` for overall litigation risk scoring
- See `legalcode-case-timeline-builder` for event chronology reconstruction
- See `legalcode-damages-calculation` for damages quantum analysis

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic as a framework, with deep coverage of US federal
court rules (FRCP, FRAP) and US state courts as the primary jurisdiction, and
[JURISDICTION-SPECIFIC] markers for non-US jurisdictions.

**US Federal Courts (Primary Coverage):**
The Federal Rules of Civil Procedure (FRCP) govern procedural deadlines in US federal
courts. FRCP Rule 6 governs time computation. Local Civil Rules and individual judge
standing orders frequently modify FRCP defaults. Always check: (1) FRCP, (2) Local
Civil Rules for the specific district, (3) Individual judge standing orders.

**US State Courts:**
State courts have their own procedural rules that may differ substantially from the FRCP.
Many states use business days instead of calendar days for motion practice. State statutes
of limitations and tolling doctrines vary significantly by state and claim type.

[JURISDICTION-SPECIFIC] **England & Wales (CPR):**
The Civil Procedure Rules govern time computation in England & Wales. CPR Rule 2.8
sets out time computation: exclude the day of the triggering event; if the period
expires on a non-business day (weekend or bank holiday), the period expires on the
next business day. CPR Rule 6 governs service and deemed service dates. Claim forms
under CPR Rule 7 must be served within 4 months of issue (2 months if served outside
the jurisdiction). Research current CPR provisions via authoritative sources — CPR
amendments are frequent.

[JURISDICTION-SPECIFIC] **Australia (Federal Court):**
The Federal Court Rules 2011 (Cth) govern federal proceedings. Rule 2.26 sets out
time computation. State supreme courts have their own rules. The Limitation Act
applicable varies by state (New South Wales: Limitation Act 1969; Victoria: Limitation
of Actions Act 1958; Queensland: Limitation of Actions Act 1974). Verify current rules.

[JURISDICTION-SPECIFIC] **European Union:**
EU procedural regulations vary by forum and instrument (e.g., Regulation 1215/2012
Brussels I Recast for jurisdiction; Regulation 44/2001 for time computation in EU
proceedings). The Court of Justice of the EU has its own Rules of Procedure. Verify
applicable EU and member state rules for any specific proceeding.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
computing deadlines on ambiguous inputs, the workflow pauses and asks when:

- The triggering event date is ambiguous or unconfirmed
- Multiple day-count rules could apply (calendar vs. business days)
- Service method is unknown and affects the deadline
- Jurisdiction is unclear or multiple courts are involved
- The deadline type spans multiple competing rules

Use the **⟁ CLARIFY** pattern (structured options with "Why this matters" explanations)
at each marked decision point. If the user has already provided the information, skip
the question and proceed.

---

## Workflow

### Phase 1: Accept Deadline Input

Accept the deadline calculation request in any of these formats:

- **Specific event**: "Complaint was personally served on defendant on March 15, 2026 —
  when is the answer due in SDNY?"
- **Document**: Court order, scheduling order, or docket entry provided as text or file
- **Deadline type + jurisdiction**: "Calculate EEOC charge deadline for Texas employee
  terminated March 1, 2026"
- **Multi-deadline request**: "Build the full litigation calendar from complaint filing
  in N.D. Cal. through trial-ready date"
- **Statute of limitations check**: "Client's breach of contract claim in New York —
  last act of breach was June 15, 2022 — has the SOL run?"
- **Administrative deadline**: "FTCA medical malpractice claim, injury date October 5,
  2024 — map both deadline steps"

If the request is too vague to compute without assumptions, proceed to Phase 2 to
gather context before calculating.

### Phase 2: Gather Context

**⟁ CLARIFY** — Before computing deadlines, ask the user these questions. Skip any
already answered by the input.

1. **Procedural Forum**
   - Options: US Federal Court (specify district), US State Court (specify state and
     county/court), England & Wales (CPR), Australia (Federal Court / specify state
     Supreme Court), EU / other
   - _Why this matters_: FRCP Rule 6 calendar-day rules differ from CPR Rule 2.8
     business-day rules and from state court rules that use court days. The wrong
     day-count method produces wrong deadlines.

2. **Triggering Event**
   - Options: Personal service of complaint, E-filing through CM/ECF, Mail service,
     Entry of judgment, End of discovery, Other (specify)
   - _Why this matters_: Under FRCP Rule 6(a)(1), the day of the triggering event is
     excluded from the count — but "triggering event" must be precisely identified.
     Service date and filing date can differ by days or weeks.

3. **Triggering Event Date — Confirm or Clarify**
   - Ask: "What is the exact date of the triggering event, and how was it confirmed?
     (e.g., date on court docket, certificate of service, certified mail receipt)"
   - _Why this matters_: A one-day error in the triggering event date propagates
     through all downstream deadlines. Ambiguity in "served" vs. "filed" date is a
     common malpractice source.

4. **Service Method (if applicable)**
   - Options: Personal service, Electronic service via CM/ECF, Electronic service
     outside CM/ECF, US Mail, Leave at dwelling, Other
   - _Why this matters_: Under FRCP Rule 6(d) (as amended December 1, 2016): mail
     service and non-CM/ECF electronic service add 3 days; CM/ECF electronic service
     adds 0 days. Applying pre-2016 rules to CM/ECF service is a common error.

5. **Holiday Calendar**
   - Options: Federal holidays only (US federal court), Federal + [State] holidays
     (specify state), Custom org calendar, Multiple jurisdictions (specify all)
   - _Why this matters_: Federal courts use the 11 federal legal holidays. State courts
     may observe additional state holidays (e.g., state founders' days, Good Friday in
     some states). Juneteenth was added as a federal holiday in 2021 and is still missed
     by older deadline calculators.

6. **Related Deadlines to Model**
   - Options: Just this one deadline, Full case calendar (all deadlines from this
     triggering event), Dependency chain only (what this deadline triggers)
   - _Why this matters_: Many deadlines are interdependent. The answer deadline triggers
     the scheduling order window, which triggers discovery cutoff, which triggers expert
     report deadlines. Modeling the chain prevents downstream surprises.

7. **Buffer Policy**
   - Options: No buffer (bare deadline only), Standard buffer (subtract 5 business
     days for internal review), Aggressive buffer (subtract 10 business days), Custom
     (specify)
   - _Why this matters_: Bare calculated deadlines leave no room for drafting,
     revision, approval, or last-minute complications. A recommended-file date is more
     useful than a hard deadline alone.

8. **Playbook or Configuration**
   - Ask: "Does your organization have a deadline playbook or deadline policy document?
     If so, share the path or paste the relevant policies."
   - _Why this matters_: Some organizations have standing policies on extensions,
     pre-clearance for filings near deadlines, and jurisdiction-specific holiday
     calendars that should override defaults.

For batch/non-interactive runs, use these defaults:

- Forum: US Federal Court (FRCP)
- Triggering event: As stated by user
- Service method: Personal service (no addition)
- Holiday calendar: Federal holidays only
- Related deadlines: Single deadline requested
- Buffer: Standard (5 business days)
- Playbook: None; apply FRCP defaults

### Phase 3: Load Deadline Playbook

**Check for organizational configuration:**

1. Look for a playbook file at: `./deadline-playbook.md`, `./legal-config.yaml`, or
   a path specified by the user
2. If found, extract:
   - `buffer_policy`: How many days before the hard deadline to target for filing
   - `holiday_calendars`: List of holidays the organization observes
   - `extension_defaults`: Whether stipulated extensions or court-ordered extensions
     apply to specific deadline types
   - `court_specific_rules`: Local rule modifications for frequently-used courts
   - `escalation_thresholds`: When to escalate (e.g., < 7 days to deadline)
3. If no playbook found, apply FRCP defaults and note assumption in Glass Box

**Fallback to defaults if playbook missing:**

- Buffer policy: 5 business days before hard deadline
- Holiday calendar: 11 US federal holidays (5 U.S.C. § 6103)
- Extension defaults: No automatic extensions unless specified
- Escalation threshold: CRITICAL if < 7 days; ELEVATED if 7–21 days

### Phase 4: Identify Applicable Rule and Authority

**Step 4a — Identify the procedural rule governing this deadline:**

1. Identify the court and type of proceeding
2. Identify the specific FRCP/FRAP rule, statute, or contract clause
3. If legalcode-mcp is connected: search for current rule text, recent amendments,
   and local rules for the specific court
4. If legalcode-mcp is not connected: apply general rule knowledge and mark every
   cited rule with [VERIFY] — verify against current court rules before relying

**Step 4b — Check for local rule modifications:**
The FRCP provides default deadlines that are frequently modified by:

- Local Civil Rules for the specific district (check district court website)
- Individual judge standing orders (check court-specific resources)
- Scheduling orders entered in the case
- Stipulations between the parties

The hierarchy is: FRCP → Local Rules → Scheduling Order → Judge's Standing Orders.
Later and more specific sources control.

**⟁ CLARIFY** — If a scheduling order is in effect in this case, ask:
"Has the court entered a scheduling order? If yes, what deadlines does it set? The
scheduling order supersedes FRCP defaults for most procedural deadlines."

**Step 4c — Verify for recent amendments:**
FRCP amendments take effect December 1 of the applicable year. Key recent amendments
to note:

- December 1, 2016: FRCP Rule 6(d) amended to remove 3-day addition for CM/ECF
  electronic service — this is still frequently misapplied
- December 1, 2020: FRCP Rule 30(b)(6) amended on deposition notice requirements
- Mark any rule not recently verified with [CHECK CURRENCY]

### Phase 5: Compute Primary Deadline(s)

**Step 5a — Apply FRCP Rule 6(a) day-count mechanics:**

_Exclude the triggering day:_
Under Rule 6(a)(1)(A), exclude the day of the event that triggers the period. Day 1
of the period is the calendar day immediately following the triggering event.

_Count every day:_
Under Rule 6(a)(1)(B), count every day including intermediate Saturdays, Sundays,
and legal holidays. Federal courts use calendar days — never "court days" unless a
specific local rule provides otherwise.

_Extend for weekend/holiday end date:_
Under Rule 6(a)(1)(C), if the last day of the period falls on a Saturday, Sunday,
or legal holiday, extend to the next day that is not a Saturday, Sunday, or legal
holiday.

_State the calculation trace explicitly:_
For every computed deadline, document:

```
Triggering event: [Event name] — [Date]
Rule citation: [FRCP Rule X.X or statute]
Day count: [N] calendar days
Day 1 of period: [Date after triggering event]
Counted through: [N days]
Raw deadline date: [Date]
Weekend/holiday adjustment: [Yes/No — if yes, describe]
Service method adjustment (Rule 6(d)): [+N days or none]
Final computed deadline: [Date]
Confidence: [Definite / High / Probable / Possible / Unlikely]
```

**Step 5b — Apply service-method additions (FRCP Rule 6(d)):**

Under FRCP Rule 6(d) as amended December 1, 2016:

| Service Method          | Rule Citation               | Days Added | Note                       |
| ----------------------- | --------------------------- | ---------- | -------------------------- |
| US Mail                 | Rule 5(b)(2)(C)             | +3 days    | Classic mail service       |
| Leaving at dwelling     | Rule 5(b)(2)(B)             | +3 days    | Left at usual abode        |
| Electronic (not CM/ECF) | Rule 5(b)(2)(E)             | +3 days    | Email service, for example |
| Electronic via CM/ECF   | (Removed from 6(d) in 2016) | **0 days** | Instantaneous transmission |
| Personal service        | Rule 5(b)(2)(A)             | 0 days     | Hand delivery              |

⚠️ **Critical note**: The 2016 amendment eliminated the 3-day addition for CM/ECF service.
Practitioners trained before December 1, 2016 frequently apply the pre-amendment rule in
error, adding 3 days to CM/ECF deadlines. This error can result in an untimely filing.

After applying service additions, re-apply the weekend/holiday extension rule to the
adjusted date. The addition of 3 days may push the deadline to a weekend or holiday
that must itself be extended.

**Step 5c — Legal holidays for federal courts:**

The 11 US federal legal holidays under 5 U.S.C. § 6103, as incorporated in FRCP
Rule 6(a)(6)(A):

| Holiday                              | Date                     |
| ------------------------------------ | ------------------------ |
| New Year's Day                       | January 1                |
| Birthday of Martin Luther King, Jr.  | 3rd Monday in January    |
| Washington's Birthday                | 3rd Monday in February   |
| Memorial Day                         | Last Monday in May       |
| Juneteenth National Independence Day | June 19 ⚠️ Added 2021    |
| Independence Day                     | July 4                   |
| Labor Day                            | 1st Monday in September  |
| Columbus Day                         | 2nd Monday in October    |
| Veterans Day                         | November 11              |
| Thanksgiving Day                     | 4th Thursday in November |
| Christmas Day                        | December 25              |

When a fixed-date holiday falls on Saturday, it is observed on the preceding Friday.
When it falls on Sunday, it is observed on the following Monday. Use the **observed**
date (not the calendar date) when computing deadlines.

⚠️ **Juneteenth alert**: Any deadline calculator or office practice established before
June 2021 may not account for Juneteenth (June 19). If a deadline falls on June 19 or
is calculated across June 19 after 2021, verify that Juneteenth is included in the
holiday set.

**Step 5d — Apply backward-counting rule for deadlines measured before an event:**

For deadlines that must be met a set number of days **before** an event (e.g., pretrial
disclosures due 30 days before trial):

- Count backward from the deadline event date
- If the last day falls on a Saturday, Sunday, or legal holiday, move the deadline
  **earlier** (to the preceding business day)
- Note: backward-counted deadlines move to **earlier** dates on weekend/holiday collision,
  not later dates

**Step 5e — Minimum period thresholds:**

Under Rule 6(a)(1), when a period of fewer than 11 days is stated, only count day for
day (no weekend/holiday exclusion from the count itself — only the end-date extension
applies). For periods of 11+ days, all intermediate days are counted and only the
end-date is extended.

[JURISDICTION-SPECIFIC] For periods of fewer than 11 days in some earlier versions of
FRCP (pre-2009), intermediate weekends and holidays were excluded. The 2009 amendments
eliminated this distinction — verify whether the operative version of the rule applies
calendar days throughout. The current FRCP (post-December 1, 2009) uses calendar days
for all periods.

### Phase 6: Model Parallel Deadline Dependencies

For multi-deadline requests or full case calendars, model the dependency chain:

**Step 6a — Identify the deadline cascade:**

| Triggering Deadline                                      | Triggers                                               | Rule                |
| -------------------------------------------------------- | ------------------------------------------------------ | ------------------- |
| Complaint filed                                          | Summons issued (court)                                 | FRCP 4              |
| Complaint personally served on defendant                 | Answer/12(b) motion: 21 days                           | FRCP 12(a)(1)(A)(i) |
| Defendant served (last defendant)                        | Scheduling conference: within 90 days of first service | FRCP 16(b)          |
| Rule 26(f) conference held                               | Initial disclosures: 14 days after                     | FRCP 26(a)(1)(C)    |
| Scheduling order entered                                 | All downstream deadlines per order                     | FRCP 16(b)          |
| Discovery cutoff                                         | Expert reports: 90 days before trial                   | FRCP 26(a)(2)(D)    |
| Expert reports disclosed                                 | Rebuttal experts: 30 days after                        | FRCP 26(a)(2)(D)    |
| Close of all discovery                                   | Summary judgment: 30 days after (FRCP default)         | FRCP 56(b)          |
| Trial-ready date                                         | Pretrial disclosures: 30 days before                   | FRCP 26(a)(3)(B)    |
| Judgment entered                                         | Rule 59/50(b) motions: 28 days                         | FRCP 59(b), 50(b)   |
| Judgment entered (or last post-judgment motion disposed) | Notice of appeal: 30 or 60 days                        | FRAP 4(a)(1)        |

**Step 6b — Critical path analysis:**

Identify the deadline that controls the schedule (i.e., the bottleneck). Common
critical-path constraints:

- Expert report deadline often controls trial date in complex cases
- Discovery cutoff controls summary judgment deadline (default FRCP 56(b))
- FTCA administrative exhaustion controls when suit can be filed
- EEOC charge deadline is often the most time-sensitive pre-litigation deadline

**Step 6c — Conflict detection:**

Flag any cases where:

- Two concurrent deadlines fall within 5 days of each other (resource strain)
- A discovery deadline overlaps with a brief-filing deadline
- A response deadline would require filing on a holiday or immediately after a holiday
  period (Thanksgiving week, December holiday period)
- Extension of one deadline would push a dependent deadline into a problem zone

**Step 6d — Floating deadlines:**

Some deadlines "float" because they depend on events that have not yet occurred:

- "30 days after expert reports are served" — calculate assuming typical service date,
  then show sensitivity analysis: "If expert reports served [date +/- 14 days], motion
  deadline would be [date +/- 14 days]"
- "Within a reasonable time" — flag as [JUDGMENT REQUIRED]; do not compute a specific
  date; recommend counsel set a specific deadline

### Phase 7: Validate — Citation Quality Gates and Self-Interrogation

#### Citation Quality Gates

Run these 5 gates silently before delivering output. If any gate fails, revise before
delivering.

| Gate                         | Rule                                                                                                          | Fail Action                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Source Identified**        | Every deadline cites a specific rule, statute, court order, or contract clause                                | Add citation or mark [UNVERIFIED] |
| **Current Applicability**    | Every cited rule verified for amendments (especially FRCP Rule 6(d) 2016 amendment, local rule modifications) | Flag [CHECK CURRENCY]             |
| **Jurisdiction Correctness** | Rule applied in the correct jurisdiction; no FRCP rule applied in state court without verification            | Remove or qualify                 |
| **Competing Authority**      | Alternative interpretations or extensions (local rules, standing orders, tolling) acknowledged                | Add caveat                        |
| **Confidence Alignment**     | Confidence score reflects actual uncertainty; no false precision                                              | Revise score                      |

#### Self-Interrogation for CRITICAL Deadlines

For any deadline classified CRITICAL (< 7 days remaining), apply this 3-pass review:

**Pass 1 — Fact Integrity**: Is the triggering event date confirmed in the record (court
docket, certificate of service, certified mail receipt)? Is there any ambiguity about
when service was effected? Would a court agree that the clock started when I calculated?

**Pass 2 — Rule Interpretation**: Does the cited rule support the day count stated?
Is there a local rule, scheduling order, or standing order that modifies this deadline?
Has the rule been recently amended? Is the 2016 CM/ECF amendment correctly applied?

**Pass 3 — Completeness**: Are all related deadlines identified? Has the 3-day Rule 6(d)
addition been applied or correctly omitted? Is the weekend/holiday extension correctly
applied? Have I accounted for all state holidays (in state court matters)?

### Phase 8: Generate Deliverables

Produce all deliverables appropriate to the request scope.

#### 8a — Deadline Summary (Markdown)

For single-deadline requests, produce the deadline summary template from the Output
Format section. Include: deadline date, rule citation, day-count trace, urgency tier,
recommended file date, and related deadlines.

#### 8b — Case Calendar (Markdown Table)

For multi-deadline requests, produce a full case calendar in tabular form. See the
Output Format section for the table template.

#### 8c — JSON Output

For downstream system integration, produce the JSON output template. See Output Format.

#### 8d — iCal Entries

For calendar import, produce iCal VEVENT entries with:

- DTSTART: Recommended file date (buffer applied)
- DTEND: Hard deadline date
- SUMMARY: Deadline type + matter identifier
- DESCRIPTION: Rule citation, triggering event, confidence

#### 8e — Glass Box Audit Trail

Always include the Glass Box YAML. See the Glass Box section below.

---

## Day-Count Computation Reference

### FRCP Key Deadlines Quick Reference

#### Pleadings and Pre-Answer Motions

| Event                                               | Deadline                                                                                         | Rule                      | Notes                           |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------- | ------------------------------- |
| Answer (personal service)                           | 21 days                                                                                          | FRCP 12(a)(1)(A)(i)       | From service date               |
| Answer (waiver of service, US defendant)            | 60 days from waiver request                                                                      | FRCP 12(a)(1)(B), 4(d)(3) | From date request was sent      |
| Answer (waiver of service, international defendant) | 90 days from waiver request                                                                      | FRCP 12(a)(1)(B), 4(d)(3) | From date request was sent      |
| Answer (United States as defendant)                 | 60 days                                                                                          | FRCP 12(a)(2)             | From service                    |
| Answer to counterclaim or crossclaim                | 21 days                                                                                          | FRCP 12(a)(1)(B)          | From service                    |
| 12(b) pre-answer motion                             | Before or simultaneous with responsive pleading                                                  | FRCP 12(b)                | Must not be delayed post-answer |
| Amended pleading (as of right)                      | 21 days after service of responsive pleading, or 21 days after service of a 12(b)/(e)/(f) motion | FRCP 15(a)(1)(B)          | Right to amend expires          |

#### Discovery

| Event                            | Deadline                                                                   | Rule             | Notes                             |
| -------------------------------- | -------------------------------------------------------------------------- | ---------------- | --------------------------------- |
| Rule 26(f) conference            | At least 21 days before scheduling conference or scheduling order deadline | FRCP 26(f)(1)    | Parties must confer               |
| Initial disclosures              | 14 days after Rule 26(f) conference                                        | FRCP 26(a)(1)(C) | Unless otherwise ordered          |
| Expert witness disclosures       | 90 days before trial or trial-ready date                                   | FRCP 26(a)(2)(D) | Absent other order                |
| Rebuttal expert disclosures      | 30 days after opposing expert disclosure                                   | FRCP 26(a)(2)(D) | Absent other order                |
| Pretrial disclosures             | 30 days before trial                                                       | FRCP 26(a)(3)(B) | Witnesses, depositions, exhibits  |
| Interrogatory responses          | 30 days after service                                                      | FRCP 33(b)(2)    | Failure = waiver of objections    |
| Document production responses    | 30 days after service                                                      | FRCP 34(b)(2)(A) |                                   |
| Requests for admission responses | 30 days after service                                                      | FRCP 36(a)(3)    | **Failure = automatic admission** |

#### Motions and Post-Trial

| Event                                              | Deadline                                         | Rule          | Extendable?                |
| -------------------------------------------------- | ------------------------------------------------ | ------------- | -------------------------- |
| Summary judgment (default)                         | 30 days after close of all discovery             | FRCP 56(b)    | Yes, by scheduling order   |
| Rule 59 new trial / alter judgment                 | 28 days after judgment entry                     | FRCP 59(b)    | **NO — absolute**          |
| Rule 50(b) renewed JMOL                            | 28 days after judgment entry (or jury discharge) | FRCP 50(b)    | **NO — absolute**          |
| Rule 52(b) amended findings                        | 28 days after judgment entry                     | FRCP 52(b)    | **NO — absolute**          |
| Rule 60(b)(1)–(3) (mistake, new evidence, fraud)   | Within 1 year of judgment                        | FRCP 60(c)(1) | NO extension beyond 1 year |
| Rule 60(b)(4)–(6) (void, satisfied, other reasons) | Reasonable time                                  | FRCP 60(c)(1) | Court discretion           |

#### Appellate

| Event                                           | Deadline                                            | Rule            | Extendable?                          |
| ----------------------------------------------- | --------------------------------------------------- | --------------- | ------------------------------------ |
| Notice of appeal (civil, standard)              | 30 days after entry of judgment                     | FRAP 4(a)(1)(A) | See FRAP 4(a)(5) — excusable neglect |
| Notice of appeal (US government party)          | 60 days after entry of judgment                     | FRAP 4(a)(1)(B) | See FRAP 4(a)(5)                     |
| Notice of appeal (post-judgment motion pending) | 30/60 days after last post-judgment motion disposed | FRAP 4(a)(4)(A) | **Tolled while motion pending**      |
| Extension (excusable neglect motion)            | Must move within 30 days after original deadline    | FRAP 4(a)(5)    | Limited: max 30 additional days      |

⚠️ **Jurisdictional bar (Bowles v. Russell, 551 U.S. 205 (2007))**: The notice of
appeal deadline in civil cases is jurisdictional. Equitable tolling does not apply.
A court-issued order purporting to extend the deadline beyond the statutory limit is
void. There is no excuse for a late notice of appeal; the appellate court will dismiss
for lack of jurisdiction.

---

## Statute of Limitations Reference

### Federal Claims — Key Limitations Periods

| Claim                                     | Period                                                                                                       | Citation                                                          | Accrual Rule                                                                                                   | Notes                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Section 1983 (civil rights)               | Borrowed from state personal injury (typically 2–3 years by state)                                           | Wilson v. Garcia, 471 U.S. 261 (1985) [VERIFY]                    | Federal discovery rule — when plaintiff knew or should have known                                              | Federal tolling rules apply; state tolling rules supplement                                       |
| Title VII / ADA employment discrimination | 90 days to file suit after EEOC right-to-sue letter                                                          | 42 U.S.C. § 2000e-5(f)(1)                                         | After right-to-sue letter issued                                                                               | EEOC charge must be filed first (see Admin Deadlines)                                             |
| ADEA (age discrimination)                 | 90 days after right-to-sue letter; or sue 60 days after filing charge                                        | 29 U.S.C. § 626(d) [VERIFY]                                       | After right-to-sue letter, or 60 days after EEOC charge                                                        | Can sue without waiting in some circumstances                                                     |
| FLSA (wage & hour)                        | 2 years (3 years if willful)                                                                                 | 29 U.S.C. § 255(a)                                                | Each workweek of underpayment: separate violation                                                              | Burden on plaintiff to prove willfulness for 3-year period                                        |
| False Claims Act                          | 6 years from violation; OR 3 years from government knowledge — whichever is later, but no more than 10 years | 31 U.S.C. § 3731(b)                                               | Government official's knowledge governs alternative period (Cochise Consultancy, 587 U.S. 408 (2019) [VERIFY]) | Complex dual-provision; compute both and use later date                                           |
| Patent infringement                       | 6 years                                                                                                      | 35 U.S.C. § 286                                                   | Each infringing act                                                                                            | Laches not available for damages within 6 years (SCA Hygiene, 580 U.S. 328 (2017) [VERIFY])       |
| Copyright infringement                    | 3 years                                                                                                      | 17 U.S.C. § 507(b)                                                | Discovery rule: when plaintiff discovered or should have discovered (most circuits)                            | Damages not limited to 3-year lookback if timely filed (Warner Chappell v. Nealy (2024) [VERIFY]) |
| RICO                                      | 4 years                                                                                                      | Agency Holding Corp. v. Malley-Duff, 483 U.S. 143 (1987) [VERIFY] | Injury discovery rule                                                                                          | Separate accrual for each new, independent injury                                                 |
| FTCA (federal tort claims)                | 2 years to file admin claim; 6 months after denial to file suit                                              | 28 U.S.C. § 2401(b)                                               | When plaintiff knows injury and its cause                                                                      | Two mandatory steps — see Admin Deadlines                                                         |

### State Claims — Key Jurisdictions

#### California (Cal. Code Civ. Proc.)

| Claim                               | Period                                                              | Citation                        |
| ----------------------------------- | ------------------------------------------------------------------- | ------------------------------- |
| Personal injury                     | 2 years                                                             | CCP § 335.1                     |
| Breach of written contract          | 4 years                                                             | CCP § 337                       |
| Breach of oral contract             | 2 years                                                             | CCP § 339                       |
| Medical malpractice                 | 3 years from injury; or 1 year from discovery — whichever first     | CCP § 340.5 [VERIFY]            |
| Fraud                               | 3 years from discovery                                              | CCP § 338(d)                    |
| Tort claims against public entities | 6-month admin claim required; 6 months after rejection to file suit | Gov. Code §§ 910–912.8 [VERIFY] |

#### New York (CPLR)

| Claim                         | Period                                                                  | Citation             |
| ----------------------------- | ----------------------------------------------------------------------- | -------------------- |
| Personal injury               | 3 years                                                                 | CPLR § 214(5)        |
| Breach of contract (any form) | 6 years                                                                 | CPLR § 213(2)        |
| Medical malpractice           | 2 years 6 months (2.5 years)                                            | CPLR § 214-a         |
| Fraud                         | 6 years from commission or 2 years from discovery — whichever is longer | CPLR § 213(8)        |
| UCC goods contracts           | 4 years                                                                 | UCC § 2-725 [VERIFY] |

⚠️ **New York COVID tolling**: New York Executive Orders tolled limitations periods
for approximately 228 days (March 20 – November 3, 2020). Claims that appear time-
barred under a straight calculation may be viable if this tolling applies. Verify
current status of any COVID tolling arguments for matters first evaluated before 2025.

#### Texas (Tex. Civ. Prac. & Rem. Code)

| Claim                                | Period                             | Citation          |
| ------------------------------------ | ---------------------------------- | ----------------- |
| Personal injury                      | 2 years                            | § 16.003          |
| Breach of contract (written or oral) | 4 years                            | § 16.004          |
| Fraud                                | 4 years                            | § 16.004(a)(4)    |
| Medical malpractice                  | 2 years; 10-year statute of repose | § 74.251 [VERIFY] |

#### Florida (Fla. Stat.)

| Claim                        | Period                                | Citation               | Note                                                   |
| ---------------------------- | ------------------------------------- | ---------------------- | ------------------------------------------------------ |
| Personal injury (negligence) | **2 years**                           | § 95.11(3)(a)          | ⚠️ Reduced from 4 years by HB 837, eff. March 24, 2023 |
| Breach of written contract   | 5 years                               | § 95.11(2)(b)          |                                                        |
| Breach of oral contract      | 4 years                               | § 95.11(3)(k)          |                                                        |
| Medical malpractice          | 2 years from discovery; 4-year repose | § 95.11(4)(b) [VERIFY] |                                                        |

⚠️ **Florida HB 837 (effective March 24, 2023)**: Personal injury / negligence claims
accruing on or after March 24, 2023 have a 2-year limitations period. Claims accruing
before that date retain the prior 4-year period. Applying the old period to new claims
is a serious malpractice risk.

#### Illinois (735 ILCS)

| Claim                           | Period                                | Citation                                        |
| ------------------------------- | ------------------------------------- | ----------------------------------------------- |
| Personal injury                 | 2 years                               | 735 ILCS 5/13-202                               |
| Breach of written contract      | 10 years                              | 735 ILCS 5/13-206 [VERIFY: note unusually long] |
| Oral contract / general actions | 5 years                               | 735 ILCS 5/13-205                               |
| Medical malpractice             | 2 years from discovery; 4-year repose | 735 ILCS 5/13-212 [VERIFY]                      |

### Tolling Doctrines

| Doctrine                        | Requirements                                                                                   | Leading Authority                                                    | Key Limit                                                                                                                                           |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Equitable tolling**           | (1) Diligent pursuit of rights AND (2) extraordinary circumstance preventing timely filing     | Pace v. DiGuglielmo, 544 U.S. 408 (2005) [VERIFY]                    | Attorney error generally not "extraordinary"; not available for appellate deadlines (Bowles v. Russell)                                             |
| **Fraudulent concealment**      | (1) Affirmative concealment act, (2) plaintiff's ignorance of claim, (3) due diligence         | Circuit-specific [VERIFY]                                            | Some circuits require separate act; some recognize self-concealing conspiracies                                                                     |
| **Discovery rule**              | Limitations begins when plaintiff knew or reasonably should have known of injury and its cause | Federal: claim-specific [VERIFY]                                     | Default rule for many federal claims; state application varies                                                                                      |
| **American Pipe class tolling** | Class action filed and pending; plaintiff is putative class member                             | American Pipe & Constr. Co. v. Utah, 414 U.S. 538 (1974) [VERIFY]    | Does NOT extend to successive class actions — only individual opt-out/denied plaintiffs (China Agri-Business v. Resh, 584 U.S. 732 (2018) [VERIFY]) |
| **Minority tolling**            | Plaintiff is a minor                                                                           | State law governs for state-borrowed limitations                     | Begins running on plaintiff's 18th birthday (most states)                                                                                           |
| **COVID-19 emergency tolling**  | Depends on state executive orders or court orders                                              | New York: ~228 days (March 20 – November 3, 2020); other states vary | Federal claims: no blanket federal tolling; only state claims in deferring states                                                                   |
| **Absence from jurisdiction**   | Defendant absent from state and unable to be served                                            | State law; limited by long-arm statutes                              | Often rendered moot by modern long-arm service                                                                                                      |

---

## Administrative Claim Deadlines

### EEOC Charges — Title VII / ADA / ADEA

**Determining the applicable deadline:**

1. Identify the state where the discriminatory act occurred
2. Determine whether that state has a qualifying Fair Employment Practices Agency (FEPA)
3. If FEPA exists (deferral state): deadline is **300 calendar days** from the discriminatory act
4. If no FEPA (non-deferral state): deadline is **180 calendar days**

⚠️ **Most states are deferral states**. The 300-day period is operative for the majority
of practitioners. Failing to verify the state's status — or advising only 180 days when
300 are available — is a reversible malpractice error.

**After EEOC right-to-sue letter:**

- 90 days to file suit in federal court
- Strictly enforced; equitable tolling applies only in limited circumstances
- Calendar from the date the letter is issued (or received, per circuit — [VERIFY])

**ADEA exception:**
Unlike Title VII, ADEA plaintiffs may file suit 60 days after filing the EEOC charge
without waiting for a right-to-sue letter, provided the EEOC has not filed suit first.

### FTCA — Two-Step Deadline

**Step 1 — Administrative Claim:**

- Present written claim to the appropriate federal agency
- Deadline: **2 years** from accrual of the cause of action
- Accrual: when plaintiff knows both the existence of the injury and its cause
  (discovery rule applies to FTCA medical malpractice claims)
- "Presented" = when the agency actually receives the claim (not the mailing date)
- Missing this deadline is a jurisdictional bar — no equitable exception

**Step 2 — File Suit:**

- After agency issues a final written denial (by certified or registered mail): **6 months**
- OR: if agency fails to act within 6 months, claimant may treat as constructive denial
  and file suit
- Missing this deadline is also a jurisdictional bar

⚠️ **FTCA malpractice trap**: Practitioners often correctly calendar Step 1 but fail to
calendar Step 2. Set both deadlines from the start of representation.

### Social Security Disability Appeals

| Step                           | Deadline                  | Standard                     | Note                                   |
| ------------------------------ | ------------------------- | ---------------------------- | -------------------------------------- |
| Request reconsideration        | 60 days + 5 days for mail | 20 C.F.R. § 404.909 [VERIFY] | From receipt of initial determination  |
| Request ALJ hearing            | 60 days + 5 days for mail | 20 C.F.R. § 404.929 [VERIFY] | From receipt of reconsideration denial |
| Request Appeals Council review | 60 days + 5 days for mail | 20 C.F.R. § 404.968 [VERIFY] | From receipt of ALJ decision           |
| File in federal district court | 60 days + 5 days for mail | 42 U.S.C. § 405(g) [VERIFY]  | From receipt of Appeals Council action |

The 5-day mail buffer is a regulatory presumption: absent other evidence, the SSA assumes
the notice was received 5 days after the date on the notice.

### IRS Tax Court Petition

- **90 days** from the date the IRS mails a Notice of Deficiency (150 days if addressed
  outside the United States)
- Jurisdiction is absolute — the Tax Court cannot extend this deadline under any
  circumstances
- Missing this deadline forfeits the right to prepayment review and requires payment first

### NLRB Unfair Labor Practice Charges

- **6 months** from the date of the alleged unfair labor practice — 29 U.S.C. § 160(b)
- Charges filed after 6 months will not be processed
- May be extended for fraudulent concealment

### California Government Claims Act

- Tort claims against California public entities:
  - **Administrative claim**: 6 months from accrual — Gov. Code § 911.2 [VERIFY]
  - **After rejection notice**: 6 months to file suit
  - **If no action taken**: 2 years from accrual to file suit
- Failure to comply is a complete bar to suit

---

## Severity Classification (Urgency Tiers)

Classify each computed deadline by urgency:

| Tier         | Remaining Time      | Color     | Prescribed Action                                                                                                                                                                         |
| ------------ | ------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL** | < 7 calendar days   | 🔴 RED    | Immediate escalation to responsible partner/supervising attorney. File protective motions if any ambiguity. Same-day calendar and docketing verification required.                        |
| **ELEVATED** | 7–21 calendar days  | 🟡 YELLOW | Assign primary drafter immediately. Begin drafting. Seek extensions now if needed — do not wait. Internal review buffer at risk.                                                          |
| **STANDARD** | 22–60 calendar days | 🟢 GREEN  | Normal workflow. Set recommended-file date with buffer. Schedule drafting session.                                                                                                        |
| **ADVANCE**  | > 60 calendar days  | ⚪ GREY   | Acknowledge and calendar. No urgency action required. Revisit in 30 days or when case activity warrants.                                                                                  |
| **OVERDUE**  | Past deadline       | ⛔ BLACK  | Immediate escalation. Assess sanctions, default, dismissal, malpractice risk. Determine whether emergency relief is available (Rule 6(b), FRAP 4(a)(5), equitable tolling). Do not delay. |

---

## Prioritization Framework

When multiple concurrent deadlines compete for the same resources, prioritize as follows:

**Tier 1 — Absolute (cannot be extended):**

- Notice of appeal deadline (FRAP 4(a) / Bowles v. Russell — jurisdictional)
- Rule 59/50(b)/52(b) post-trial motion deadline (FRCP 6(b) — cannot be extended by court)
- EEOC charge filing deadline (once missed, administrative exhaustion fails)
- FTCA administrative claim filing deadline (jurisdictional)
- IRS Tax Court petition deadline (jurisdictional)
- Statute of limitations (where no tolling applies)

**Tier 2 — High Consequence (extensions possible but difficult):**

- Answer to complaint (default judgment risk)
- Response to requests for admission (automatic admission upon failure — Rule 36)
- Initial disclosures (sanctions risk, preclusion of evidence)
- SOL deadlines where tolling is arguable but uncertain

**Tier 3 — Standard Consequence (extendable by consent or court order):**

- Discovery responses (interrogatories, document requests)
- Expert witness disclosure
- Summary judgment responses
- Most scheduling order deadlines

**Tier 4 — Operational (important but low immediate consequence):**

- Pretrial disclosures
- Scheduling order modifications
- Administrative filing deadlines without jurisdictional consequences

---

## Citation Quality Gates

Run these 5 gates silently before delivering any deadline output. If any gate fails, revise.

| Gate                      | Rule                                                                                                                                                             | Fail Action                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Source Identified**     | Every computed deadline cites the specific FRCP rule, statute, court order, or contract clause                                                                   | Add citation or mark [UNVERIFIED]                      |
| **Current Applicability** | Rule verified for recent amendments — especially FRCP Rule 6(d) 2016 amendment (CM/ECF 3-day addition removed), Juneteenth added 2021, local rule current status | Flag [CHECK CURRENCY]                                  |
| **Jurisdiction Correct**  | Rule applied to the correct court and jurisdiction; FRCP not applied in state court without local confirmation                                                   | Remove or qualify with [VERIFY state court equivalent] |
| **Competing Authority**   | Local rules, scheduling orders, standing orders that could modify the deadline acknowledged                                                                      | Add caveat                                             |
| **Confidence Alignment**  | Confidence score reflects actual certainty about triggering event date, rule interpretation, and application                                                     | Revise score                                           |

---

## Self-Interrogation for Critical Deadlines

For any deadline classified CRITICAL (< 7 calendar days) or any Tier 1 absolute deadline,
apply this 3-pass review before delivery:

**Pass 1 — Fact Integrity**: Is the triggering event date confirmed in the official record
(court docket, CM/ECF entry, certified mail receipt, certificate of service)? Is there any
ambiguity about when service was effective? Could a court hold that the triggering event
occurred on a different date?

**Pass 2 — Rule Interpretation**: Does the cited rule language support the day count I
computed? Is there a local rule, scheduling order, or individual judge standing order that
modifies this deadline in this district or before this judge? Has the rule been amended
since the date I am relying on? Is the 2016 CM/ECF amendment correctly applied?

**Pass 3 — Completeness**: Are all related deadlines identified? Have all applicable
service-method additions been applied (or correctly omitted for CM/ECF)? Have I applied
the weekend/holiday extension correctly — and to the right end date? Are there tolling
events that affect this deadline?

---

## Confidence Scoring

Apply this 5-tier scale to every computed deadline:

| Level        | Range     | Meaning                                                                                                                                 | Action                                                                            |
| ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Definite** | 0.95–1.00 | Triggering event date confirmed in official record; rule language is unambiguous; no competing local rules; calculation straightforward | State deadline with confidence                                                    |
| **High**     | 0.80–0.94 | Triggering event date confirmed; rule clear; minor local rule check outstanding                                                         | State deadline with brief caveat: "verify local rules"                            |
| **Probable** | 0.60–0.79 | Triggering event date established but from secondary source; or rule application requires interpretation                                | State deadline with reasoning; flag for attorney verification                     |
| **Possible** | 0.40–0.59 | Triggering event date disputed or ambiguous; or competing rules apply                                                                   | Present as range with alternative scenarios; escalate to attorney                 |
| **Unlikely** | 0.00–0.39 | Triggering event date not confirmed; rule application highly uncertain                                                                  | Do not state a deadline; flag as [UNCERTAIN]; recommend immediate attorney review |

---

## Glass Box Audit Trail

Include this YAML block in every deadline output:

```yaml
glass_box:
  skill_name: "legalcode-deadline-calculator"
  version: "2026-03-02"
  matter_id: "[case name / file number — redact if needed]"
  court_or_forum: "[specific court, district, and division]"
  governing_rules: "[FRCP / state rules / CPR / other]"
  deadline_type: "[answer / discovery response / notice of appeal / SOL / EEOC charge / etc.]"
  triggering_event:
    description: "[description of event]"
    date: "[YYYY-MM-DD]"
    confirmed_by: "[docket entry / certificate of service / court order / stated by counsel]"
  applicable_rule: "[e.g., FRCP Rule 12(a)(1)(A)(i) — [VERIFY] if memory-sourced]"
  day_count: "[N calendar days]"
  day_count_type: "[calendar days / business days / clear days]"
  service_method: "[personal / CM/ECF / mail / other]"
  service_addition_applied: "[+3 days for mail / 0 days for CM/ECF / etc.]"
  holiday_calendar_used: "[federal holidays only / federal + state / custom org]"
  holidays_encountered_in_period: "[list dates if any]"
  raw_deadline_date: "[YYYY-MM-DD — before weekend/holiday extension]"
  final_deadline_date: "[YYYY-MM-DD — after all adjustments]"
  recommended_file_date: "[YYYY-MM-DD — with buffer applied]"
  buffer_applied: "[N business days]"
  urgency_tier: "[CRITICAL / ELEVATED / STANDARD / ADVANCE / OVERDUE]"
  priority_tier: "[Tier 1 / 2 / 3 / 4]"
  parallel_deadlines_identified: "[list key related deadlines]"
  local_rules_checked: "[yes — [court name]; no — [VERIFY required]]"
  scheduling_order_in_effect: "[yes / no / unknown]"
  tolling_applicable: "[yes / no / possibly — describe]"
  confidence: "[Definite / High / Probable / Possible / Unlikely — rationale]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[N verified / N unverified with [VERIFY] tags]"
  limitations:
    - "[Any scope limitations, assumptions, or outstanding verification items]"
  reviewer: "AI-assisted — requires verification by qualified legal professional before reliance"
```

---

## Anti-Patterns

What NOT to do in litigation deadline calculation:

1. **Including the trigger date in the count.** Under FRCP Rule 6(a)(1)(A), the day of
   the triggering event is excluded. Day 1 is the calendar day immediately after service.
   This is the single most common computational error.

2. **Adding 3 days to CM/ECF electronic service.** As of December 1, 2016, FRCP Rule 6(d)
   was amended to remove the 3-day addition for service made through CM/ECF. Practitioners
   trained before 2016 frequently commit this error, producing deadlines that appear to be
   3 days later than they actually are.

3. **Confusing calendar days with court days.** Federal courts use calendar days exclusively.
   Some state courts (notably California for opposition and reply periods) use court days.
   Never apply state-court day-count rules to federal proceedings without verification.

4. **Failing to check local rules.** FRCP deadlines are the floor, not the ceiling. Most
   active federal districts have local rules that modify briefing schedules, impose pre-motion
   conference requirements, and set different MSJ page limits and timing. A deadline
   calculated from FRCP alone is frequently wrong in practice.

5. **Treating post-trial motion deadlines as extendable.** Rules 50(b), 52(b), 59(b), 59(d),
   and 59(e) deadlines (28 days from judgment) cannot be extended by the court under FRCP
   Rule 6(b). Many attorneys assume the general extension power covers all deadlines; it
   does not. Missing these deadlines is irreversible.

6. **Assuming the notice of appeal can be equitably tolled.** After Bowles v. Russell (2007),
   the civil appeal deadline is jurisdictional. A court-issued order purporting to extend
   the deadline beyond the statutory limit is void. Equitable exceptions do not apply.

7. **EEOC deadline confusion: 180 vs. 300 days.** Failing to determine whether the relevant
   state is a "deferral state" before advising a client on the EEOC charge deadline. This is
   state-specific; most states are deferral states (300-day period), but some are not. The
   error can leave a client who has 300 days believing only 180 remain — causing premature
   filing of a weak EEOC charge — or advising 300 days when only 180 apply.

8. **Florida SOL: applying the pre-2023 four-year period to post-March 2023 claims.** HB 837
   reduced personal injury limitations from 4 years to 2 years effective March 24, 2023.
   Advising Florida personal injury clients based on the old period for new claims is a
   malpractice exposure.

9. **Missing Juneteenth from the holiday calendar.** Juneteenth (June 19) became a federal
   legal holiday in 2021. Any deadline calculator or practice established before 2021 may
   not account for it. Deadlines that fall on or are calculated across June 19 can be off
   by one day.

10. **FTCA: calendaring only Step 1 and forgetting Step 2.** The FTCA requires two steps:
    a 2-year window to file the administrative claim, then a 6-month window after agency
    denial to file suit. Both are jurisdictional. Missing Step 2 after successfully
    completing Step 1 is as fatal as missing Step 1.

11. **American Pipe tolling for successive class actions.** Post-China Agri-Business (2018),
    American Pipe tolling does not extend to successive class actions — it benefits only
    individual plaintiffs who opt out or whose class certification is denied and then file
    individual suits. Advising a client that a successive class action is protected by
    American Pipe tolling is reversible error.

12. **Failing to calendar tolling end dates.** When tolling applies (COVID emergency orders,
    class action tolling, minority reaching majority, incapacity ending), the end of the
    tolling period restarts the clock — it does not suspend it permanently. Failure to
    calendar the resumption date and the resulting new expiration is as dangerous as missing
    the original deadline.

13. **Backward-counting errors.** For deadlines measured before an event (e.g., pretrial
    disclosures due 30 days before trial), if the last day falls on a weekend or holiday,
    the deadline moves **earlier**, not later. Applying the forward-count rule to backward-
    counted deadlines produces a deadline that is too late.

14. **Failure to model the dependency chain.** Computing the answer deadline correctly but
    failing to note that it triggers the scheduling order window, which triggers discovery
    cutoff, which triggers expert report deadlines. Clients and supervising attorneys need
    the full cascade, not isolated dates.

15. **Relying on standard practice without verifying individual judge standing orders.** Many
    district judges impose their own briefing schedules, pre-motion conference requirements,
    page limits, and timing rules through standing orders published on the court's website.
    These control over Local Civil Rules, which control over FRCP defaults. A deadline
    calculated from FRCP alone that ignores a judge's standing order is wrong.

16. **Applying state holiday calendars to federal proceedings.** State courts observe
    additional holidays beyond the 11 federal holidays. Only the federal holidays apply
    to federal court deadlines under FRCP Rule 6(a)(6)(A), unless a scheduling order or
    local rule provides otherwise. Importing state holiday calendars into federal deadline
    calculations can produce incorrect extended deadlines.

17. **Not issuing urgency alerts for cluster periods.** When multiple Tier 1 or Tier 2
    deadlines cluster within a 7-day window (common around trial, holiday periods, or
    post-judgment motion periods), the risk is greater than any individual deadline would
    suggest. Failure to flag the cluster leads to resource allocation failures.

18. **Treating equitable tolling as a safety net.** Equitable tolling is sparingly applied
    in federal court. Attorney error, miscalculation, and missed deadlines typically do not
    qualify as "extraordinary circumstances." Never advise a client to rely on equitable
    tolling as a fallback for a deadline that could have been timely met.

---

## Writing Standards

Apply these standards before delivering any deadline output:

- **State dates unambiguously**: Use YYYY-MM-DD format or full written date (e.g.,
  "April 15, 2026") — never shorthand that could be misread (e.g., "4/5" is May 4 in
  some formats, April 5 in others)
- **Always cite the triggering event date alongside the deadline**: "Answer due April 5,
  2026 (21 days after personal service on March 15, 2026 — FRCP 12(a)(1)(A)(i))"
- **Separate calculated deadline from recommended-file date**: Never present only one date
- **Flag every [VERIFY] and [CHECK CURRENCY] item explicitly** in the output summary
- **Never state a Possible (0.40–0.59) or Unlikely deadline without a qualification**:
  "Based on assumption X; verify with [Y] before relying"
- **Do not bury urgency information**: Urgency tier should appear at the top of the
  summary, not at the end
- **Avoid vague hedging that obscures the deadline**: "It appears the deadline might
  be around..." is not acceptable; either state the deadline with a confidence score or
  flag that calculation is not possible pending clarification
- **Proofread the calendar math**: Recount the days independently before delivery,
  especially across month boundaries and near holidays

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Phase 4, search for the current text of applicable FRCP rules, local rules for
  the specific district, and relevant precedent on deadline computation
- Verify that no amendments have taken effect since the rules were last updated in
  the skill's knowledge base
- Search for standing orders of the specific judge (if matter is assigned)
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Apply general knowledge of FRCP and state procedural rules
- Mark every cited rule, statute, and case with [VERIFY]
- Recommend counsel verify all rules against official court websites before relying
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural quality: correct day-count framework and holiday list; flag all
  specifics for independent verification

**Practice management system integration:**

- Produce JSON and iCal outputs as described in the Output Format section
- These are designed for import into Relativity, LexisNexis Firm Manager, MyCase,
  Clio, and standard calendar applications — verify compatibility with the specific
  system used before import

---

## Localization Notes

When applying this skill outside US federal courts:

**US State Courts:**

- Most use calendar days like FRCP, but some use court days (e.g., California motion
  practice uses court days for opposition and reply periods)
- State holiday calendars vary — verify the specific state's observed holidays
- Statute of limitations periods vary substantially (see State Claims table above)
- Some states have notice-of-claim requirements before suing government entities
  (e.g., California Government Claims Act, New York CPLR § 50-e for notice of claim)

[JURISDICTION-SPECIFIC] **England & Wales:**

- CPR Rule 2.8: exclude the day of the triggering event; extend to next business day
  if last day is not a business day (Saturday, Sunday, or bank holiday)
- Bank holidays in England & Wales differ from US federal holidays — verify the current
  list on the official UK government website
- CPR Part 6 governs service; CPR 6.14 (deemed service rules) are complex and differ
  by service method
- Limitation Act 1980: most claims 6 years (simple contract) or 3 years (personal
  injury from knowledge) — [VERIFY]

[JURISDICTION-SPECIFIC] **Australia:**

- Federal Court Rules 2011 r. 2.26: exclude first day, include last day; extend to
  next business day if last day is not a business day
- State and territory holiday calendars differ — verify for the specific court
- Limitation periods vary by state and claim type — verify applicable Act

[JURISDICTION-SPECIFIC] **EU Proceedings (CJEU):**

- Rules of Procedure of the Court of Justice govern timing
- Time limits for preliminary reference proceedings and direct actions differ
- Verify current provisions on the CJEU website

---

## Output Format Template

### Single Deadline Summary

```markdown
## Deadline Calculation: [Deadline Type]

**Matter**: [Case Name / File Number]
**Prepared**: [YYYY-MM-DD]

---

### 🔴 CRITICAL / 🟡 ELEVATED / 🟢 STANDARD / ⚪ ADVANCE / ⛔ OVERDUE

| Field                     | Value                                                                          |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Hard Deadline**         | [YYYY-MM-DD]                                                                   |
| **Recommended File Date** | [YYYY-MM-DD] (hard deadline minus [N] business days)                           |
| **Days Remaining**        | [N] calendar days to hard deadline                                             |
| **Urgency Tier**          | [CRITICAL / ELEVATED / STANDARD / ADVANCE / OVERDUE]                           |
| **Priority Tier**         | [Tier 1 — Absolute / Tier 2 — High / Tier 3 — Standard / Tier 4 — Operational] |

---

### Calculation Trace

- **Triggering event**: [Event name] — [Date], confirmed by [source]
- **Applicable rule**: [Rule citation — FRCP Rule X.X or statute] [VERIFY if unconfirmed]
- **Day count**: [N] calendar days
- **Day 1 of period**: [Day after triggering event]
- **Raw deadline (Day [N])**: [Date]
- **Weekend/holiday adjustment**: [None / Extended from [day] to [date] because [reason]]
- **Service method adjustment (Rule 6(d))**: [+3 days for mail / 0 for CM/ECF / none]
- **Final computed deadline**: **[YYYY-MM-DD]**
- **Confidence**: [Definite / High / Probable / Possible / Unlikely] — [brief rationale]

---

### Related Deadlines Triggered by This Event

| Deadline             | Date   | Rule   | Tier   |
| -------------------- | ------ | ------ | ------ |
| [Related deadline 1] | [Date] | [Rule] | [Tier] |
| [Related deadline 2] | [Date] | [Rule] | [Tier] |

---

### Verification Required

- [ ] Confirm triggering event date against [source]
- [ ] Verify local rules for [district] do not modify this deadline [VERIFY]
- [ ] Check individual judge standing orders for [judge name] [VERIFY]
- [ ] Confirm no scheduling order modifies this deadline

---

### Counsel Escalation

**If CRITICAL**: Notify [responsible partner/supervising attorney] immediately.
**If OVERDUE**: Assess sanctions/default risk. Evaluate Rule 6(b)/FRAP 4(a)(5)/
equitable tolling arguments. Engage senior counsel.
```

---

### Full Case Calendar (Multi-Deadline)

```markdown
## Case Calendar: [Matter Name]

**Generated**: [YYYY-MM-DD]
**Forum**: [Court — District — Judge]
**Governing Rules**: [FRCP / Local Rules / Scheduling Order dated YYYY-MM-DD]

---

### Urgency Summary

| Tier                     | Count | Deadlines |
| ------------------------ | ----- | --------- |
| 🔴 CRITICAL (< 7 days)   | [N]   | [list]    |
| 🟡 ELEVATED (7–21 days)  | [N]   | [list]    |
| 🟢 STANDARD (22–60 days) | [N]   | [list]    |
| ⚪ ADVANCE (> 60 days)   | [N]   | [list]    |

---

### Full Deadline Table

| Deadline                     | Hard Date | Rec. File Date | Rule                     | Tier     | Priority   | Confidence |
| ---------------------------- | --------- | -------------- | ------------------------ | -------- | ---------- | ---------- |
| Answer to complaint          | [Date]    | [Date]         | FRCP 12(a)(1)(A)(i)      | STANDARD | Tier 2     | High       |
| Rule 26(f) conference        | [Date]    | [Date]         | FRCP 26(f)(1)            | STANDARD | Tier 3     | High       |
| Initial disclosures          | [Date]    | [Date]         | FRCP 26(a)(1)(C)         | STANDARD | Tier 2     | High       |
| Discovery cutoff             | [Date]    | [Date]         | Scheduling Order         | STANDARD | Tier 3     | High       |
| Expert disclosures           | [Date]    | [Date]         | FRCP 26(a)(2)(D)         | [Tier]   | Tier 2     | [Conf]     |
| MSJ deadline                 | [Date]    | [Date]         | FRCP 56(b) / Sched Order | [Tier]   | Tier 2     | [Conf]     |
| Pretrial disclosures         | [Date]    | [Date]         | FRCP 26(a)(3)(B)         | [Tier]   | Tier 3     | [Conf]     |
| Rule 59/50(b) (if judgment)  | [Date]    | [Date]         | FRCP 59(b) / 50(b)       | [Tier]   | **Tier 1** | [Conf]     |
| Notice of appeal (if appeal) | [Date]    | [Date]         | FRAP 4(a)(1)(A)          | [Tier]   | **Tier 1** | [Conf]     |

---

### Dependency Diagram (Text)
```

Complaint filed
└─ Complaint served on Defendant A ─→ Answer due: [Date] ──────┐
└─ Complaint served on Defendant B ─→ Answer due: [Date] │
↓
Scheduling Conf: [Date]
└─ Discovery Cutoff: [Date]
├─ Expert Reports: [Date]
│ └─ Rebuttal Experts: [Date]
└─ MSJ Filing Deadline: [Date]
└─ Trial Ready: [Date]
└─ Pretrial Disclosures: [Date]

```

---

### Outstanding Verification Items

- [ ] [Verification item 1 — rule, local rule, scheduling order]
- [ ] [Verification item 2]
```

---

### JSON Deadline Object

```json
{
  "matter_id": "[case name / file number]",
  "generated": "[YYYY-MM-DD]",
  "forum": "[court / district / judge]",
  "governing_rules": "[FRCP / Local Rules / Scheduling Order]",
  "deadlines": [
    {
      "deadline_type": "[e.g., answer_to_complaint]",
      "hard_deadline": "[YYYY-MM-DD]",
      "recommended_file_date": "[YYYY-MM-DD]",
      "rule_citation": "[FRCP 12(a)(1)(A)(i)]",
      "triggering_event": {
        "description": "[e.g., personal service of complaint]",
        "date": "[YYYY-MM-DD]",
        "confirmed_by": "[docket entry / certificate of service]"
      },
      "day_count": 21,
      "day_count_type": "calendar",
      "service_adjustment_days": 0,
      "holiday_adjustments_applied": false,
      "urgency_tier": "[CRITICAL / ELEVATED / STANDARD / ADVANCE / OVERDUE]",
      "priority_tier": "[1 / 2 / 3 / 4]",
      "confidence": "[Definite / High / Probable / Possible / Unlikely]",
      "verify_flags": []
    }
  ],
  "glass_box_reference": "[see audit trail section]"
}
```

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis using 2-agent research pipeline.
Agent 1 (Legal Research): deep research on FRCP Rule 6 time computation mechanics (Rule
6(a)(1)–(3), 6(a)(6), 6(b), 6(d) including 2016 amendment eliminating CM/ECF 3-day
addition), key FRCP procedural deadlines (Rules 12, 16, 26, 30, 33, 34, 36, 50, 52,
56, 59, 60), FRAP Rule 4 appellate deadlines (Bowles v. Russell jurisdictional bar),
federal statutes of limitations (§ 1983 Wilson v. Garcia; Title VII 42 U.S.C. § 2000e-
5; FLSA 29 U.S.C. § 255; FCA 31 U.S.C. § 3731(b) Cochise Consultancy; patent 35 U.S.C.
§ 286 SCA Hygiene; copyright 17 U.S.C. § 507(b) Petrella/Warner Chappell; RICO Agency
Holding Corp. v. Malley-Duff; FTCA 28 U.S.C. § 2401(b)), state limitations periods for
California/New York/Texas/Florida/Illinois (including Florida HB 837 2023 SOL reduction),
tolling doctrines (equitable tolling Pace v. DiGuglielmo; American Pipe; China Agri-
Business successive class action bar; COVID-19 emergency tolling by state), EEOC 180/300-
day deferral-state framework (42 U.S.C. § 2000e-5(e)), federal holiday calendar (5 U.S.C.
§ 6103 including Juneteenth 2021), and 12 anti-patterns drawn from legal malpractice
analysis. Agent 2 (Structural Analyst): analyzed legalcode-litigation-risk-assessment,
legalcode-damages-calculation, legalcode-case-timeline-builder, and legalcode-contract-
review (reference standard), extracting multi-phase workflow architecture, CLARIFY block
pattern (8–11 questions), Glass Box YAML template, 5-tier Confidence Scoring framework,
5-gate Citation Quality Gates, 3–4-pass Self-Interrogation, playbook integration pattern,
multi-format output architecture, and identified 10 structural gaps specific to deadline
calculation. Synthesized into an 18-element Legalcode gold-standard skill with US federal/
state jurisdiction as primary coverage and [JURISDICTION-SPECIFIC] markers for England &
Wales, Australia, and EU proceedings.
