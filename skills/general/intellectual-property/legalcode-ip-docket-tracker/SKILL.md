---
name: legalcode-ip-docket-tracker
description: Calculate, track, and prioritize IP prosecution deadlines across USPTO, EPO/EPC, WIPO/PCT,
  and UKIPO — covering patent Office Action responses, maintenance fees (3.5/7.5/11.5 years at USPTO;
  annual at EPO/UKIPO), issue fee payment, continuation and divisional filing windows, PCT national phase
  entry (30 months), Paris Convention priority claims (12/6 months), trademark use declarations (§§ 8/15/71),
  trademark renewals (§ 9), inter partes review (IPR) time bars (1 year), EPO opposition windows (9 months),
  Unitary Patent requests (1 month), UKIPO compliance periods, and all triggered deadlines. Use when performing
  a docket audit, onboarding a new patent or trademark portfolio, calculating deadlines from a set of
  key dates, identifying overdue or critical IP matters, generating a deadline calendar for a single matter
  or full portfolio, or assessing docketing risk exposure.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Calculate, track, and prioritize IP prosecution deadlines across USPTO, EPO/EPC, WIPO/PCT, and UKIPO — covering patent Office Action responses, maintenance fees (3.5/7.5/11.5 years at USPTO; annual at EPO/UKIPO), issue fee payment, continuation and divisional filing windows, PCT national phase entry (30 months), Paris Convention priority claims (12/6 months), trademark use declarations (§§ 8/15/71), trademark renewals (§ 9), inter partes review (IPR) time bars (1 year), EPO opposition windows (9 months), Unitary Patent requests (1 month), UKIPO compliance periods, and all triggered deadlines. Use when performing a docket audit, onboarding a new patent or trademark portfolio, calculating deadlines from a set of key dates, identifying overdue or critical IP matters, generating a deadline calendar for a single matter or full portfolio, or assessing docketing risk exposure. Covers patent prosecution, post-grant procedures, trademark maintenance, PCT international and national phase, and restoration remedies. Produces a prioritized, tiered deadline report with OVERDUE / CRITICAL / HIGH / MONITOR / CALENDAR classifications and specific recommended actions per deadline.


# Legalcode IP Docket Tracker

> **Disclaimer**: This skill provides a framework for AI-assisted IP deadline calculation and
> docket management. It does not constitute legal advice. All calculated deadlines must be
> independently verified by a qualified patent or trademark attorney or registered IP practitioner
> licensed in the relevant jurisdiction before any reliance or action. Patent and trademark law
> changes; verify current applicability of all statutory and regulatory references before use.
> Statutory and rule references cited from memory carry hallucination risk — verify against
> authoritative sources (USPTO MPEP, EPO Guidelines, WIPO PCT Applicant's Guide, UKIPO Manual
> of Patent Practice) before any filing decision. A single missed IP deadline can result in
> irreversible loss of rights worth significant commercial value. Always maintain redundant
> docketing systems and involve qualified counsel for all hard deadlines.

---

## Purpose and Scope

This skill calculates, organizes, and prioritizes IP prosecution deadlines for portfolios spanning
USPTO, EPO/EPC, WIPO/PCT, and UKIPO. It transforms raw IP asset data (filing dates, priority dates,
grant dates, registration dates, and key event dates) into a prioritized deadline report with
severity classifications and specific recommended actions.

**Covers:**

- USPTO patent prosecution: Office Action response deadlines, issue fee payment, RCE windows,
  continuation/divisional/CIP filing cut-offs, PTAB appeal timing, IPR time bars
- USPTO patent maintenance fees: 3.5, 7.5, and 11.5-year windows with grace periods
- USPTO trademark maintenance: Section 8 Declarations (years 5–6 and every 10 years thereafter),
  Section 15 Declarations of Incontestability, Section 9 Renewals (every 10 years),
  Section 71 Declarations for Madrid Protocol registrations
- EPO/EPC deadlines: examination responses (Rule 132), Rule 71(3) grant approval, opposition
  (Art. 99, 9 months), appeal (Art. 108, 2+4 months), annual renewal fees (Rule 51),
  national validation deadlines, Unitary Patent request (1 month from grant)
- WIPO/PCT international phase: ISR at 16 months, Art. 19 amendments (later of 16 months or
  2 months from ISR), Chapter II demand (later of 22 months or 3 months from ISR), IPER at 28
  months, national phase entry (30 months for most; 31 months for EPO regional phase)
- UKIPO patent: examination response deadlines (2–4 months), compliance period (4.5 years from
  priority or 12 months from first exam report), annual renewal fees (years 4–20), restoration
- UKIPO trademark: renewal (10-year terms), opposition (2 months + TM7a extension to 3 months)
- Restoration and revival remedies: USPTO 37 CFR 1.137 revival, EPO further processing (Rule 135)
  and re-establishment of rights (Art. 122), PCT restoration of priority (Rule 26bis.3),
  UKIPO restoration (PA77 s.28, within 19 months)

**Does not:**

- Provide legal advice or replace qualified patent/trademark counsel
- Guarantee the accuracy of any calculated deadline without independent verification
- Draft patent claims, file patent applications, or conduct patentability/FTO analysis
  (see legalcode-patent-landscape-analysis, legalcode-licensing-agreement-review)
- Cover all national IP offices not listed (e.g., JPO, CNIPA, INPI, EUIPO trademark prosecution
  beyond Madrid Protocol renewals) — flag these for specialist docketing resources
- Account for unpublished USPTO or EPO internal processing variations that may shift notification dates

---

## Jurisdiction and Governing Law

This skill covers four primary IP offices and the PCT international phase:

[JURISDICTION-SPECIFIC: US/USPTO] Patent prosecution governed by 35 U.S.C. and 37 CFR
(Title 37, Code of Federal Regulations). Trademark maintenance governed by 15 U.S.C.
(Lanham Act). Response deadlines, maintenance fee windows, and revival procedures are
mandatory and precisely defined. The America Invents Act (AIA, effective March 16, 2013)
changed to a first-inventor-to-file system; pre-AIA applications still in prosecution are
subject to the prior "first-to-invent" system in limited respects.

[JURISDICTION-SPECIFIC: EU/EPO] European patent prosecution governed by the European Patent
Convention (EPC) and EPO Implementing Regulations. The Unified Patent Court (UPC) has been
operative since June 1, 2023; European patents granted after this date may have UPC exposure
unless opted out. Unitary Patents (UP) require a separate request within 1 month of grant.

[JURISDICTION-SPECIFIC: WIPO/PCT] International patent applications governed by the Patent
Cooperation Treaty (PCT) and PCT Regulations. 157+ contracting states. Deadlines run from
the **earliest priority date**, not the PCT international filing date.

[JURISDICTION-SPECIFIC: UK/UKIPO] UK patent prosecution governed by the Patents Act 1977 (PA77)
and Patents Rules 2007 (as amended). Post-Brexit, the UKIPO operates independently of the EPO
for UK national applications; UK validation of granted European patents remains available.
Trademark maintenance governed by the Trade Marks Act 1994.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points — the docket tracking
context changes significantly depending on portfolio scope, urgency, and IP types. Rather than
assuming, the workflow pauses and asks when:

- The portfolio scope would significantly expand or change the computation load
- Ambiguous date information could produce materially different deadline calculations
- Multiple valid interpretations of a deadline rule exist for specific fact patterns
- The user's role or system context affects how the output should be formatted

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

### Step 1: Accept the IP Portfolio Data

Accept IP portfolio information in any of these formats:

- **Spreadsheet or CSV**: Filing dates, grant dates, registration dates, prosecution event dates
- **Docketing system export**: Anaqua, CPi, Dennemeyer DIAMS, Alt Legal, or other system exports
- **Document or pasted text**: Descriptions of IP matters with key dates
- **Single matter**: A single patent application, granted patent, or trademark registration with
  its relevant date(s)
- **Natural language description**: "We have a US patent granted on January 15, 2022. We also
  have a PCT application filed April 3, 2023, with a priority date of April 10, 2022."

For each IP matter, identify and record:

| Field                     | Description                                                                 | Example               |
| ------------------------- | --------------------------------------------------------------------------- | --------------------- |
| Matter ID / Reference     | Internal or external identifier                                             | US2023/001234         |
| IP Type                   | Patent Application / Granted Patent / Trademark App / TM Registration / PCT | Granted Patent        |
| Office                    | USPTO / EPO / UKIPO / WIPO/PCT / Other                                      | USPTO                 |
| Filing date               | Actual filing date with the office                                          | 2022-03-15            |
| Priority date             | Earliest claimed priority date                                              | 2021-03-16            |
| Grant/registration date   | Date of patent grant or trademark registration                              | 2024-01-10            |
| Key prosecution event     | Most recent Office Action, NOA, publication date, etc.                      | NOA mailed 2025-10-01 |
| Status                    | Active / Pending / Lapsed / Expired / Cancelled                             | Active                |
| Prosecution history flags | Final rejection, abandonment, appeal pending, etc.                          | None                  |

If data is incomplete, flag the gaps and proceed with what is available, explicitly noting
which deadlines cannot be calculated.

### Step 2: Gather Context

**⟁ CLARIFY** — Before calculating deadlines, ask these questions if not already clear:

1. **Who is performing this docket review?**
   - Options: In-house IP counsel, Outside patent/trademark counsel, IP paralegal / docketing
     staff, Business owner (non-lawyer), Other
   - _Why this matters_: Determines level of detail, whether to flag attorney-of-record
     requirements, and professional responsibility reminders.

2. **What is the look-ahead window for this report?**
   - Options: Immediate (next 30 days — critical only), Standard (next 90 days),
     Full calendar year (next 12 months), Full portfolio audit (all deadlines through expiry)
   - _Why this matters_: Determines how many deadlines to surface and level of detail per entry.

3. **Which IP types are in scope?**
   - Options: Patents only, Trademarks only, Both patents and trademarks, PCT applications only,
     Full mixed portfolio
   - _Why this matters_: Different calculation logic applies to each IP type.

4. **Are there any matters with known issues?**
   - Options: Office Action pending response, Application approaching abandonment, Maintenance
     fee overdue, Missed deadline requiring revival petition, No known issues
   - _Why this matters_: Known issues should be flagged OVERDUE immediately regardless of date.

5. **Output format preference?**
   - Options: Deadline calendar by date (chronological), By matter (all deadlines per case),
     By severity tier (OVERDUE → CALENDAR), Combined executive summary + full calendar
   - _Why this matters_: Different users need different views of the same deadline data.

If any answers are provided in the initial context, skip those questions and proceed. State
any assumptions explicitly: "I'm assuming a 90-day look-ahead window — let me know if you
need a longer or shorter period."

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to verify current fee schedules and rule amendments before calculating
deadlines. Save results to `/tmp/legalcode-docket-authority.md`.

**Key areas to verify:**

- USPTO current maintenance fee amounts and any recent USPTO fee schedule changes (37 CFR 1.20)
- EPO official fee schedule changes (Administrative Council decisions; note: ~5% increase effective
  1 April 2026 per AC decision of 11 December 2025)
- UKIPO renewal fee schedule changes (fees increased ~33% effective 1 April 2026)
- Any recent rule amendments affecting time periods (e.g., patent-term adjustments, COVID-related
  waivers, PLTIA changes)
- Current USPTO petitions guidance for unintentional revival standards (37 CFR 1.137)

**If legalcode-mcp is not connected:**

- Mark all fee amounts and rule references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — verify fees and rule amendments"`
- Proceed with the deadline calculations using the reference tables in this skill, which are based
  on the statutory framework as of early 2026 and marked with [VERIFY] where currency is uncertain

### Step 4: Parse and Organize the Portfolio

For each IP matter in the portfolio:

**4a. Identify the IP category and applicable deadline regime:**

| IP Category                               | Deadline Regime                                                      |
| ----------------------------------------- | -------------------------------------------------------------------- |
| US Utility Patent Application (pending)   | USPTO prosecution deadlines                                          |
| US Utility Patent (granted)               | USPTO maintenance fee schedule                                       |
| US Design Patent Application              | USPTO prosecution deadlines (no maintenance fees for design patents) |
| US Trademark Application                  | USPTO trademark prosecution deadlines                                |
| US Trademark Registration                 | USPTO trademark maintenance (§§ 8, 15, 9, 71)                        |
| European Patent Application (pending)     | EPO prosecution deadlines + EPO renewal fees                         |
| European Patent (granted, pre-UPC)        | National validation + national renewal fees; opt-out window          |
| European Patent (granted, post-June 2023) | Unitary Patent option (1 month); national validation                 |
| PCT Application (international phase)     | PCT international phase deadlines                                    |
| PCT Application (national/regional phase) | Per-office national phase deadlines                                  |
| UK Patent Application                     | UKIPO examination + compliance period                                |
| UK Patent (granted)                       | UKIPO renewal fees (years 4–20)                                      |
| UK Trade Mark                             | UKIPO trademark renewal (10-year terms)                              |

**4b. Extract all key dates for each matter:**

- Filing date (actual or PCT international filing date)
- Earliest priority date (critical — most PCT and Paris Convention deadlines run from this)
- Publication date (triggers opposition and some IPR windows)
- Grant/registration date (triggers maintenance fee, opposition, Unitary Patent windows)
- Last Office Action mailing date (triggers response deadline)
- Notice of Allowance date (triggers issue fee payment)
- Last maintenance fee payment date (verify current period)
- Any known prosecution event dates (final rejection, abandonment, appeal filing)

**⟁ CLARIFY** — If key dates are ambiguous or missing:

- "Matter [X] has a PCT filing date but no priority date. Is the PCT filing date also the priority
  date? This affects whether the deadline is 30 months from [date A] or [date B]."
- "Matter [Y] shows a European patent grant date. Was a Unitary Patent request filed within
  1 month of grant? If not, and the grant was post-June 2023, this is an OVERDUE item."
- "Matter [Z] has a US trademark registration date but no information on whether a §8 Declaration
  has been filed. Has this declaration been filed? Registration date is [date]."

**4c. Flag matters requiring immediate attention:**

- Any matter with a deadline already past → mark OVERDUE before calculating anything else
- Any matter with a known missed filing → escalate immediately with restoration remedy analysis
- Any matter with an ambiguous status that could indicate lapse or abandonment

### Step 5: Calculate All Applicable Deadlines

Using the **Deadline Reference Tables** below, calculate every applicable deadline for each
matter. For each deadline, record:

```
Matter: [ID]
Deadline type: [e.g., "Maintenance fee — 7.5-year window (end)"]
Calculated deadline date: [YYYY-MM-DD]
Basis: [e.g., "Grant date 2018-03-15 + 7.5 years = 2025-09-15"]
Grace period available? [Yes/No — dates]
Rule/Statute: [e.g., "37 CFR 1.362(e)"]
Action required: [e.g., "Pay 7.5-year maintenance fee; surcharge applies within grace period"]
Severity tier: [OVERDUE / CRITICAL / HIGH / MONITOR / CALENDAR]
```

Work through the tables in Section **Deadline Reference Tables** for each applicable IP type.

**Calculation notes:**

1. For PCT deadlines: run all calculations from the **earliest priority date**, not the PCT
   international filing date. Where no priority is claimed, the PCT filing date is the priority date.
2. For EPO Rule 71(3) approval: the 4-month period runs from the date of the communication, not
   the grant date.
3. For USPTO §8 Declaration: the "5th to 6th anniversary" means: earliest filing window is the
   day after the 5th anniversary; latest (without grace) is the day before the 6th anniversary;
   with 6-month grace, latest is 6 months after the 6th anniversary.
4. For USPTO maintenance fees: the window period opens 6 months _before_ the due date and the
   grace period runs 6 months _after_ the due date. Both are calculated from the grant date.
5. For EPO renewal fees: fees are due on the last day of the month containing the grant anniversary.
   Prepayment allowed up to 3 months early (6 months for year 3). Late payment allowed within
   6 months with surcharge.
6. For UKIPO compliance period: take the **later** of 4.5 years from priority/filing OR 12 months
   from the first substantive exam report.
7. For IPR time bar: runs from the date on which the petitioner (or real party in interest) was
   **served** with a complaint alleging infringement — not from service of the summons or complaint
   in all jurisdictions; verify the exact service date.
8. For Unitary Patent request: runs from the date the mention of grant was **published** in the
   European Patent Bulletin, not the grant decision date. These can differ.
9. For trademark opposition at UKIPO: the initial 2-month period from publication can be
   extended to 3 months if a Form TM7a is filed within the initial 2 months.
10. When a deadline falls on a Saturday, Sunday, or official holiday at the relevant office,
    the deadline automatically extends to the next business day (verify per-office rules; UKIPO,
    USPTO, and EPO each have specific rules on this).

### Step 6: Classify and Prioritize Deadlines

Apply the **Deadline Severity Classification** system to every calculated deadline. Then
organize by the Prioritization Framework.

**⟁ CLARIFY** — For borderline cases where urgency is context-dependent:

- "Matter [X] has a maintenance fee due in 35 days. Your firm's policy may require payment to be
  initiated 60 days out. Should I classify this CRITICAL (< 30 days) or HIGH (31–90 days)?"
- "This portfolio has [N] MONITOR items beyond 90 days. Do you want those surfaced in full, or
  just a count with a summary entry?"

### Step 7: Generate the Deadline Report

Structure the output using the **Output Format Template** below. Apply the **Writing Standards**
before delivery.

### Step 8: Quality Verification

Before delivering the report:

1. Run the 5 **Citation Quality Gates** silently. Revise any failures before delivery.
2. For every **OVERDUE** deadline, run the 3-pass **Self-Interrogation** to verify the
   classification is correct and the restoration remedy analysis is complete.
3. Verify completeness: confirm every matter in the input has been processed.
4. Confirm all date arithmetic by cross-checking at least the OVERDUE and CRITICAL items.
5. Generate the Glass Box Audit Trail and append it to the report.

---

## Deadline Reference Tables

### Table 1: USPTO Patent Prosecution Deadlines

| Deadline                                  | Period                                                                                               | Statutory Authority                           | Notes                                                                               |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------- |
| Office Action response (non-final)        | SSP: 3 months; extendable to 6 months max                                                            | 35 U.S.C. 133; 37 CFR 1.134, 1.136            | Extensions available under 37 CFR 1.136(a) by paying fee; each extension = 1 month  |
| Office Action response (final)            | SSP: 3 months; extendable to 6 months max                                                            | 35 U.S.C. 133; 37 CFR 1.136                   | After-final: consider RCE or Notice of Appeal                                       |
| Issue fee payment                         | 3 months from Notice of Allowance date                                                               | 37 CFR 1.311(a)                               | **Non-extendable**. Form PTOL-85B                                                   |
| Request for Continued Examination (RCE)   | Before 6-month statutory limit from final rejection, OR before issue fee payment — whichever earlier | 37 CFR 1.114                                  | Requires RCE fee + substantive submission                                           |
| Continuation / Divisional / CIP filing    | Before parent patents, is abandoned, or proceedings terminate                                        | 35 U.S.C. 120, 121; 37 CFR 1.53               | Best practice: file concurrent with issue fee payment                               |
| PTAB Notice of Appeal                     | 2 months from examiner's answer                                                                      | 37 CFR 41.31                                  | Extendable under 37 CFR 1.136(a)                                                    |
| PTAB Appeal Brief                         | 2 months from Notice of Appeal                                                                       | 37 CFR 41.37                                  | Extendable                                                                          |
| PCT national phase entry (USPTO)          | 30 months from earliest priority date                                                                | 35 U.S.C. 371; 37 CFR 1.495; PCT Art. 22(1)   | Basic fee due by 30 months; deficiency correction by later of 2 months or 32 months |
| Paris Convention priority claim (utility) | 12 months from first foreign filing                                                                  | 35 U.S.C. 119(a)–(d); Paris Convention Art. 4 | Clock starts on actual foreign filing date                                          |
| Paris Convention priority claim (design)  | 6 months from first foreign filing                                                                   | 35 U.S.C. 172; Paris Convention Art. 4C(1)    |                                                                                     |
| Provisional → nonprovisional conversion   | 12 months from provisional filing date                                                               | 35 U.S.C. 119(e)                              | +2-month extension for unintentional delay available (PLTIA)                        |
| IPR petition time bar                     | 1 year from date petitioner served with complaint                                                    | 35 U.S.C. 315(b)                              | Joinder exception. Verify exact service date — no extension                         |
| PGR petition window                       | 9 months from patent grant date                                                                      | 35 U.S.C. 321(c)                              | Any invalidity ground; after 9 months, only IPR available                           |
| Revival of abandoned application          | Petition at any time (additional showing if >2 years after abandonment)                              | 37 CFR 1.137(a)                               | "Unintentional" standard. Must file outstanding reply + petition fee                |

### Table 2: USPTO Patent Maintenance Fees

| Fee Window | Window Opens                 | Due Date (no surcharge) | Grace Period (with surcharge) | Surcharge Rule               |
| ---------- | ---------------------------- | ----------------------- | ----------------------------- | ---------------------------- |
| 3.5-year   | 3-year anniversary of grant  | 3.5-year anniversary    | Up to 4-year anniversary      | 37 CFR 1.362(d)–(e), 1.20(h) |
| 7.5-year   | 7-year anniversary of grant  | 7.5-year anniversary    | Up to 8-year anniversary      | 37 CFR 1.362(d)–(e), 1.20(h) |
| 11.5-year  | 11-year anniversary of grant | 11.5-year anniversary   | Up to 12-year anniversary     | 37 CFR 1.362(d)–(e), 1.20(h) |

**Reinstatement after expiry**: Petition under 37 CFR 1.378; additional information required
if >2 years after expiration; subject to intervening rights. Note: design patents are **not**
subject to maintenance fees.

### Table 3: USPTO Trademark Maintenance Deadlines

| Filing                                    | Window                                                                             | Grace Period                                           | Statutory Authority                   | Consequence of Non-Filing                               |
| ----------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------- |
| Section 8 Declaration of Use (1st)        | 5th–6th anniversary of registration                                                | 6 months after 6th anniversary (+$100/class surcharge) | 15 U.S.C. § 1058                      | **Automatic cancellation**                              |
| Section 15 Declaration (Incontestability) | Within 1 year of any consecutive 5-year period of continuous use post-registration | N/A (optional filing)                                  | 15 U.S.C. § 1065                      | No legal consequence; foregoes incontestability benefit |
| Section 9 Renewal (1st)                   | 9th–10th anniversary of registration                                               | 6 months after 10th anniversary                        | 15 U.S.C. § 1059                      | **Cancellation — not reversible**                       |
| Combined §§ 8 & 9 (subsequent)            | 9th–10th anniversary and every 10 years thereafter                                 | 6 months after each 10-year deadline                   | 15 U.S.C. §§ 1058, 1059               | **Cancellation — not reversible for § 9 failure**       |
| Section 8 combined (subsequent)           | 9th–10th anniversary and every 10 years                                            | 6 months                                               | 15 U.S.C. § 1058                      |                                                         |
| Section 71 Declaration (Madrid)           | 5th–6th anniversary and 9th–10th anniversary and every 10 years thereafter         | 6 months (+$100/class surcharge)                       | 15 U.S.C. § 1141k; Trademark Act § 71 | Cancellation of US extension of protection              |

### Table 4: EPO / EPC Prosecution Deadlines

| Deadline                                      | Period                                                                               | Statutory Authority                 | Notes                                                                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Response to Examination Office Action         | 4 months from notification; extendable by 2 months as of right (total 6 months)      | Rule 132 EPC; Art. 94(3) EPC        | Further discretionary extensions available                                                                                |
| Rule 71(3) approval of text for grant         | 4 months from Rule 71(3) communication                                               | Rule 71(3)–(5) EPC                  | **Not routinely extendable**. Pay grant fee, file claims translations, pay claims fees                                    |
| Opposition                                    | 9 months from date of publication of grant mention in European Patent Bulletin       | Art. 99 EPC                         | Written + fee within 9 months; no late filings                                                                            |
| Appeal — Notice of Appeal                     | 2 months from notification of contested decision                                     | Art. 108 EPC                        | Fee must also be paid within 2 months                                                                                     |
| Appeal — Statement of Grounds                 | 4 months from notification of contested decision                                     | Art. 108 EPC                        | Both periods run from same start date                                                                                     |
| PCT regional phase entry (EPO)                | 31 months from earliest priority date                                                | Rule 51(1) EPC; PCT Art. 39         | Translation due at same deadline if not filed in EPO official language                                                    |
| Unitary Patent request                        | 1 month from publication of grant mention in European Patent Bulletin                | Art. 9 Regulation (EU) No 1257/2012 | **Absolute deadline; no extension**. Translation required during transitional period                                      |
| National validation (post-grant)              | Typically 3 months from grant mention publication (varies by country)                | Per national law                    | Germany, France, UK: typically 3 months; translation required for many states                                             |
| Annual renewal fees (EPO, during prosecution) | Due on last day of month containing each annual anniversary of filing date           | Rule 51 EPC                         | Prepayment window: up to 3 months early (6 months for year 3). Late payment: up to 6 months after due date with surcharge |
| Further processing (missed deadline remedy)   | 2 months from notification of loss of rights                                         | Art. 121 EPC; Rule 135 EPC          | Pay further processing fee + complete omitted act. Excluded deadlines: opposition, appeal notice, priority period         |
| Re-establishment of rights (last resort)      | Earlier of: 2 months from removal of cause; OR 1 year from expiry of missed deadline | Art. 122 EPC; Rule 136 EPC          | "All due care" standard. Requires documented proof of docketing system robustness                                         |

### Table 5: WIPO / PCT International Phase Deadlines

All deadlines run from the **earliest priority date** unless otherwise stated.

| Deadline                                            | Period                                                                                   | PCT Authority                       | Notes                                                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------ |
| PCT filing (to claim Paris priority)                | 12 months from first national filing                                                     | Paris Convention Art. 4; PCT Art. 8 | PCT filing date = international filing date; priority date = earlier first national filing |
| International Search Report (ISR) + Written Opinion | Established by 16 months from priority (or 9 months from PCT filing, whichever is later) | PCT Rule 42.1                       | Applicant receives; triggers Art. 19 amendment clock                                       |
| PCT Art. 19 Amendments (claims)                     | Later of: 16 months from priority OR 2 months from ISR transmittal                       | PCT Art. 19; PCT Rule 46.1          | One opportunity; filed with International Bureau, not ISA or receiving office              |
| International Publication                           | 18 months from priority (prompt after)                                                   | PCT Art. 21                         | Early publication possible on applicant request                                            |
| Chapter II Demand (IPEA)                            | Later of: 22 months from priority OR 3 months from ISR transmittal                       | PCT Rule 54bis.1(a)                 | Filing with IPEA; secures 30-month national phase entry                                    |
| PCT Art. 34 Amendments (Ch. II)                     | Before IPER is established (typically before 28 months from priority)                    | PCT Art. 34; PCT Rule 66.1          | Must be filed before IPEA closes examination                                               |
| IPER (Chapter II Report)                            | Established by 28 months from priority                                                   | PCT Rule 69.2                       | Transmitted to applicant and national offices                                              |
| National phase entry (most offices)                 | 30 months from earliest priority date                                                    | PCT Art. 22(1); PCT Rule 39.1       | Includes USPTO (37 CFR 1.495), JPO, CNIPA and most national offices                        |
| PCT regional phase — EPO                            | 31 months from earliest priority date                                                    | Rule 51(1) EPC                      | 1 extra month vs. standard 30-month rule                                                   |
| Restoration of right of priority                    | Up to 2 months after expiry of priority period (i.e., by 14 months from first filing)    | PCT Rule 26bis.3                    | "Unintentional" (US) or "due care" (EPO) standard depending on designated office           |

### Table 6: UKIPO Patent Deadlines

| Deadline                               | Period                                                                                               | Statutory Authority                    | Notes                                                                                      |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------ |
| Response to examination report         | 2 months from report date; extendable to 4 months as of right (with fee)                             | Patents Rules 2007, Rule 30; r.109     | Further extensions discretionary                                                           |
| Compliance period (acceptance)         | Later of: 4 years 6 months from priority/filing date OR 12 months from first substantive exam report | PA77 s.20; Patents Rules 2007, Rule 30 | Can be extended by 2 months as of right; further extensions need compelling circumstances  |
| Annual renewal fees (UKIPO)            | Due annually from 4th anniversary (paid in advance, before each anniversary), through year 20        | PA77 s.25; Patents (Fees) Rules        | Late payment: up to 6 months with surcharge. Fees increase ~33% from 1 April 2026 [VERIFY] |
| Restoration of lapsed patent           | Within 19 months of lapse date                                                                       | PA77 s.28; Patents Rules 2007, Rule 40 | Must show non-payment was "unintentional"                                                  |
| Reinstatement of withdrawn application | Within 12 months of withdrawal                                                                       | PA77 s.20B                             |                                                                                            |
| PCT national phase entry (UKIPO)       | 31 months from earliest priority date                                                                | PA77 s.89A; PCT Art. 22                | UKIPO follows EPO regional phase timeline for PCT entries                                  |

### Table 7: UKIPO Trade Mark Deadlines

| Deadline                                             | Period                                                                                 | Statutory Authority                      | Notes                                                                                                               |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Opposition to UK trade mark application              | 2 months from publication in Trade Marks Journal                                       | TMA 1994 s.38(2); Trade Marks Rules 2008 | Extension to 3 months by filing Form TM7a within initial 2-month period                                             |
| Renewal of UK trade mark registration                | Before 10-year anniversary (and every 10 years thereafter)                             | TMA 1994 ss.42–43                        | Grace period: 6 months after expiry date with surcharge (Form TM11)                                                 |
| Response to examination report (TM application)      | 2 months from examiner's report                                                        | Trade Marks Rules 2008                   | Extensions available on request                                                                                     |
| Madrid Protocol renewal (international registration) | Before 10-year anniversary from international registration date; renewals through WIPO | Madrid Agreement / Protocol; WIPO        | WIPO issues renewal notice; failure to renew through WIPO cancels international registration including UK extension |

---

## Deadline Severity Classification

Every calculated deadline is assigned one of five severity tiers:

### OVERDUE — Immediate Emergency Action

The deadline has already passed. Rights may be at risk or already lost. Emergency remedial
action may still be available under revival, restoration, or re-establishment procedures.

**Mandatory actions:**

- Escalate to qualified patent/trademark attorney immediately
- Identify available restoration remedy (37 CFR 1.137, Art. 122 EPC, PCT Rule 26bis.3,
  PA77 s.28) and calculate the remedy deadline
- Document the cause of the missed deadline for the remedy petition
- Assess intervening rights exposure (especially for reinstated patents)

**OVERDUE examples**: Maintenance fee grace period expired; §9 renewal missed; EPO Rule 71(3)
4-month window passed; continuation filed after parent issued; USPTO §8 grace period expired.

### CRITICAL — Due Within 30 Days

The deadline expires within the next 30 calendar days. Immediate action required to prepare
and file before the deadline.

**Required actions:**

- Begin preparation immediately
- Assign to responsible attorney/agent with specific completion target (>7 days before deadline)
- Confirm foreign associate handling for international deadlines
- Set daily docket alerts

### HIGH — Due in 31–90 Days

The deadline expires in 31–90 days. Active preparation should begin now to ensure on-time
completion with adequate review time.

**Required actions:**

- Schedule preparation with specific target completion date (at least 14 days before deadline)
- Confirm client instructions / maintenance decision
- For foreign matters: instruct local associates with adequate lead time (typically 6–8 weeks)

### MONITOR — Due in 91–180 Days

The deadline expires in 91–180 days. Log for active monitoring; initiate client notification
per office practice.

**Required actions:**

- Docket review date set at transition to HIGH tier
- Notify client/matter owner per standard practice
- For maintenance fee decisions: initiate portfolio review conversation now

### CALENDAR — Due Beyond 180 Days

The deadline is on record and calendared. No immediate action required beyond verification
that the docket entry is accurate.

**Required actions:**

- Confirm docket entry is accurate and complete
- Set reminder for transition to MONITOR tier

---

## Actionable Output Per Deadline

For every OVERDUE and CRITICAL deadline, provide a structured action entry:

```
Matter: [ID / Reference]
IP Type: [Patent/Trademark/PCT]
Office: [USPTO/EPO/UKIPO/WIPO]
Deadline type: [Specific deadline name]
Calculated deadline: [YYYY-MM-DD]
Basis: [Date + calculation logic]
Rule/Statute: [Specific citation]
Severity: [OVERDUE / CRITICAL]
Grace period: [Available / Expired / N/A — with dates]
Restoration remedy: [If OVERDUE — available remedy + remedy deadline]
Recommended action: [Specific steps to take]
Responsible party: [Attorney / Agent / Paralegal / Client — if specified]
Confidence: [Definite / High / Probable / Possible — see Confidence Scoring]
```

For HIGH and MONITOR items, provide a condensed entry:

```
Matter: [ID] | [Deadline type] | Due: [YYYY-MM-DD] | [Severity] | [One-line action]
```

---

## Prioritization Framework

Within each severity tier, prioritize by:

### Tier 1 — Irreversible Deadlines (No Recovery Option)

Deadlines where missing them results in permanent, irreversible loss of rights with **no
restoration mechanism**:

- USPTO §9 Trademark Renewal: cancellation is final and irreversible
- EPO opposition period (Art. 99): cannot be filed after 9 months — missed is missed
- EPO Unitary Patent request: absolute 1-month window; cannot be remedied
- USPTO Continuation/CIP/Divisional filed after parent issues: continuation rights extinct
- PTAB IPR petition time bar (§315(b)): 1-year from complaint service — no exception (except joinder)

**These are absolute deal-breakers. Flag with ⚠️ IRREVERSIBLE.**

### Tier 2 — High-Value / High-Consequence Deadlines

Deadlines where missing them causes major harm but restoration may be possible:

- Patent maintenance fees (USPTO, EPO, UKIPO): expensive restoration petitions with grace periods
  and surcharges; subject to intervening rights
- PCT national phase entry (30/31 months): restoration possible under Rule 26bis.3 for priority
  but national phase entry deadlines generally unforgiving without office-specific restoration
- EPO Rule 71(3) grant approval: further processing available (Rule 135) but adds costs/delays
- USPTO issue fee: application goes abandoned; revival available under 37 CFR 1.137

### Tier 3 — Recoverable Deadlines (Remedy Available)

Deadlines where missing them is costly and disruptive but legal remedies are relatively available:

- USPTO Office Action response: revival under 37 CFR 1.137 (unintentional); reinstatement fee
- EPO examination responses: further processing under Rule 135 EPC (2 months from loss-of-rights notice)
- UKIPO compliance period: discretionary extension available with grounds

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                 | Fail Action                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Source**     | Every deadline period cites a specific statute (35 U.S.C., 37 CFR, EPC Rule/Art., PCT Rule, PA77)                                    | Add citation or mark "[UNVERIFIED — verify before acting]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (§ for US statutes, Art./Rule for EPC/PCT)               | Fix format                                                 |
| **Currency**   | Every cited provision checked for recent amendments (e.g., EPO fee increases Apr 2026, UKIPO fee changes Apr 2026, PLTIA amendments) | Flag "[CHECK CURRENCY — may have been amended]"            |
| **Domain**     | Analysis stays within each IP office's procedural rules; no cross-contamination (e.g., do not apply USPTO deadlines to EPO matters)  | Remove or flag jurisdiction bleed                          |
| **Confidence** | All date arithmetic explicitly stated; uncertainty about input dates explicitly noted                                                | Add calculation basis and uncertainty qualifier            |

---

## Self-Interrogation for OVERDUE Items

For every matter classified OVERDUE, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Deadline Calculation Integrity**:

- Is the start date (priority date / grant date / action mailing date) definitely correct?
- Was the correct calculation rule applied (e.g., 30 months for most offices vs. 31 months for EPO)?
- Does the jurisdiction-specific rule actually apply to this matter (e.g., maintenance fees do
  not apply to US design patents; §71 applies only to Madrid Protocol-based registrations)?

**Pass 2 — Restoration Completeness**:

- Has every available restoration remedy been identified and its own deadline calculated?
- Have intervening rights been flagged for reinstated patents (37 CFR 1.495; MPEP 2590)?
- Has the "all due care" vs. "unintentional" distinction been correctly applied by jurisdiction?

**Pass 3 — Challenge**:

- Could the deadline be tolled by a different date interpretation (e.g., date of mailing vs.
  date of notification vs. date of actual receipt — verify per-office rule)?
- Is there a statutory holiday or weekend rule that shifts the deadline to the next business day?
- Is there any office-specific extension, waiver, or COVID/emergency order that could apply [VERIFY]?

If any pass reveals a different calculation or additional remedy, revise before delivery. Mark
the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

For each calculated deadline, assign a confidence level:

| Level        | Range     | Meaning                                                         | Action                                                               |
| ------------ | --------- | --------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Exact start date known; rule is clear and current               | State with confidence                                                |
| **High**     | 0.80–0.94 | Start date from reliable source; minor interpretation question  | State with brief caveat                                              |
| **Probable** | 0.60–0.79 | Start date uncertain by ≤30 days; or rule has a known ambiguity | State with explicit basis and note the uncertainty                   |
| **Possible** | 0.40–0.59 | Start date uncertain by >30 days; or rule recently amended      | Flag for independent verification before action                      |
| **Unlikely** | 0.0–0.39  | Key date unknown or speculative                                 | Do not assert deadline; flag "[DATE UNKNOWN — docket independently]" |

---

## Glass Box Audit Trail

Every docket report MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-ip-docket-tracker"
  report_date: "[YYYY-MM-DD]"
  portfolio_size: "[N matters processed]"
  ip_types_covered: "[Patents / Trademarks / PCT / Mixed]"
  offices_covered: "[USPTO / EPO / UKIPO / WIPO-PCT]"
  look_ahead_window: "[30 / 90 / 180 / 365 / Full portfolio days]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to /tmp/legalcode-docket-authority.md or 'Not created']"
  fee_schedule_verified: "Yes (legalcode-mcp) / No [VERIFY manually]"
  rule_amendments_checked:
    - "EPO fee increases Apr 2026: [VERIFIED / UNVERIFIED]"
    - "UKIPO fee increases Apr 2026: [VERIFIED / UNVERIFIED]"
    - "USPTO fee schedule: [VERIFIED / UNVERIFIED]"
  overdue_count: "[N]"
  critical_count: "[N]"
  high_count: "[N]"
  monitor_count: "[N]"
  calendar_count: "[N]"
  self_interrogation_applied_to: "[N OVERDUE items]"
  self_interrogation: "PASS / REVISED / N/A (no OVERDUE items)"
  confidence_distribution:
    definite: "[N]"
    high: "[N]"
    probable: "[N]"
    possible: "[N]"
    unlikely: "[N]"
  limitations:
    - "[Any missing dates, ambiguous matters, or IP types not covered]"
    - "[Any fee amounts stated as approximate — verify current schedule]"
  reviewer: "AI-assisted — requires qualified IP counsel verification before action"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in IP docket tracking:

1. **Calculating from the wrong start date** — The most dangerous error in IP docketing. For PCT
   deadlines, always use the **earliest priority date**, not the PCT international filing date.
   These can differ by up to 12 months, shifting a national phase entry deadline by the same amount.

2. **Ignoring the distinction between window and due date for maintenance fees** — USPTO maintenance
   fee windows open 6 months _before_ the due date and grace periods run 6 months _after_. Confusing
   "window opens at 3 years" with "fee is due at 3 years" (it is due at 3.5 years) is a category error.

3. **Treating all EPO/UKIPO renewal fee deadlines the same as USPTO** — EPO renewal fees are due on
   the last day of the month of the filing anniversary; UKIPO fees are due _before_ each anniversary;
   USPTO maintenance fees use different due dates entirely. Cross-applying one system to another
   produces incorrect deadlines.

4. **Missing Unitary Patent deadline by confusing grant decision date with publication in the OJ**
   — The 1-month window for requesting Unitary Patent effect runs from the **date of publication
   of the mention of grant** in the European Patent Bulletin, not from the grant decision date.
   These can differ. This is an absolute, irreversible deadline.

5. **Assuming Section 9 trademark renewal is reversible** — Unlike a lapsed patent or a missed
   Section 8 declaration (where restoration may be possible in narrow circumstances), a US trademark
   registration cancelled for failure to file a Section 9 renewal **cannot be reinstated under any
   circumstances**. Always treat Section 9 deadlines as Tier 1 Irreversible.

6. **Applying IPR time-bar calculation to the wrong trigger event** — The 1-year IPR time bar
   under 35 U.S.C. §315(b) runs from the date the petitioner (or its privy) was **served with
   a complaint**, not from the complaint filing date, case assignment date, or service of summons
   only. Verify the actual service date.

7. **Treating EPO opposition as extendable** — The EPO's 9-month opposition period is absolute.
   Unlike prosecution deadlines where further processing is available, the opposition deadline
   cannot be extended and cannot be remedied by further processing or re-establishment.

8. **Forgetting that US design patents carry no maintenance fees** — Applying maintenance fee
   calculations to a US design patent produces phantom deadlines. Design patents also have a
   different term (15 years from grant for applications filed on or after May 13, 2015; 14 years
   for earlier applications).

9. **Conflating Section 8 and Section 9 trademark deadlines** — Section 8 (Declaration of Use)
   and Section 9 (Renewal) are separate filings with separate deadlines. Both are due in the
   9th–10th anniversary window; a combined §§8&9 filing satisfies both but must be tracked as
   a single composite deadline. Missing either individually has independent consequences.

10. **Omitting Section 71 deadlines for Madrid Protocol registrations** — Madrid Protocol-based US
    registrations require Section 71 declarations (functionally equivalent to Section 8) on the
    same schedule, but the procedural pathway differs. Failure applies to the US extension of
    protection; WIPO handles the international registration separately. Never conflate the two.

11. **Applying "unintentional" revival standards universally** — The USPTO uses an "unintentional"
    delay standard for revival (37 CFR 1.137). The EPO uses "all due care" for re-establishment
    under Art. 122 EPC — a significantly higher standard requiring documented evidence of a robust
    docketing system and an isolated, non-systemic error. Never represent the EPO remedy as readily
    available when it rarely is in practice.

12. **Not accounting for office holiday and weekend shifts** — Patent offices have specific rules
    for deadlines that fall on weekends or official holidays. Each jurisdiction handles this
    differently. Always check whether a calculated deadline falls on a business day for the relevant
    office, and apply the appropriate business-day shift rule.

13. **Ignoring the UKIPO compliance period rule's "later of" logic** — The UKIPO compliance
    period is the **later** of 4.5 years from priority/filing OR 12 months from the first substantive
    exam report. A long-delayed examination can actually extend the compliance period. Calculate
    both and take the later.

14. **Treating docket calculation as a substitute for a professional opinion** — A calculated
    deadline is a tool for organizing workflow, not a legal opinion. Patent term adjustment (PTA),
    patent term extension (PTE), terminal disclaimers, and intervening rights analysis require
    qualified counsel and cannot be reliably automated. Always flag these for human review.

15. **Single-system docketing** — Professional IP docketing standards (AIPLA, ABA Model Rule 1.1)
    require **redundant systems** — a primary docket system and an independent secondary check.
    An AI-generated deadline report is a useful secondary check but should never be the only
    docket record for a hard deadline. Always maintain primary docket records in a qualified
    IP management system.

16. **Skipping the "tickler date" distinction from the actual deadline** — Responsible IP docketing
    distinguishes between the _actual_ deadline and _tickler_ reminder dates (typically at 6 months,
    3 months, 1 month, 1 week, and day-of). This skill reports actual deadlines; the user's docketing
    system should set appropriate tickler dates working backward from each calculated deadline.

17. **Missing triggered deadlines** — Many IP deadlines are not fixed-date but triggered by events:
    opposition by grant publication, IPR time bar by service of complaint, continuation window by
    parent issuance. If the triggering event is not recorded in the portfolio data, the deadline
    cannot be calculated. Always check for completeness of event-date data, not just filing dates.

---

## Writing Standards

Apply plain-language discipline to all docket report output:

**For action items** (shared with attorneys, paralegals, and clients):

- Imperative, verb-first instructions: "Pay 7.5-year maintenance fee by [date]" not "The 7.5-year
  maintenance fee should be paid"
- Specific amounts and deadlines, not approximations: "Due: 2025-09-15" not "Due soon"
- Name the office: "USPTO maintenance fee" not "maintenance fee payment"
- Cite the statute/rule for every hard deadline

**For executive summaries** (shared with business stakeholders):

- Plain English with parenthetical explanations for legal terms on first use
- Severity counts, not just lists: "3 OVERDUE, 7 CRITICAL, 14 HIGH" at the top
- Flag irreversible items explicitly: "⚠️ 2 items are OVERDUE with no recovery option"

**Quality gates before delivery**:

1. Can a senior IP paralegal understand every action item and execute it from the report?
2. Is every calculated deadline traceable to a specific start date + rule + arithmetic?
3. Are OVERDUE and CRITICAL items at the top, not buried in a chronological list?
4. Is every fee amount flagged as [VERIFY] if not verified against the current fee schedule?
5. Are any action items vague ("address this issue") without specifying what "address" means?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal verification tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current USPTO, EPO, UKIPO, and WIPO fee schedules
- Verify any recent rule amendments that could affect time periods
- For OVERDUE matters: search for current revival/restoration petition requirements and fees
- Check for any emergency or COVID-related deadline extensions still in effect [VERIFY]
- Mark all legalcode-mcp-verified references as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all fee amounts and rule references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — verify fees and rule amendments manually"`
- Direct user to authoritative sources: USPTO Fee Schedule (37 CFR 1.16–1.21), EPO Official
  Journal, UKIPO Patents (Fees) Rules, WIPO PCT Applicant's Guide
- Include a prominent notice: "Fee amounts stated in this report are based on information as of
  early 2026 and require independent verification before payment"

**Official verification sources (no legalcode-mcp):**

- USPTO fees: [37 CFR Part 1, Subpart A] and USPTO Patent Fee Schedule at www.uspto.gov/patent/laws-and-regulations/fees-and-payment/current-patent-fee-schedule
- USPTO trademark: USPTO Trademark Fee Schedule
- EPO fees: EPO Official Journal notice; EPO fee calculator at www.epo.org
- UKIPO fees: gov.uk/government/publications/intellectual-property-office-fees
- PCT: WIPO PCT Fee Schedule and PCT Applicant's Guide at www.wipo.int/pct

---

## Output Format Template

Structure the final docket report as:

```markdown
# IP Docket Report

**Generated**: [YYYY-MM-DD]
**Portfolio**: [Name / Reference / "Single Matter"]
**Scope**: [IP types + offices covered]
**Look-ahead window**: [30 / 90 / 180 / 365 days]
**Fee schedule verification**: [VERIFIED via legalcode-mcp / UNVERIFIED — verify before payment]

---

## Executive Summary

| Severity                 | Count   | Includes Irreversible? |
| ------------------------ | ------- | ---------------------- |
| ⛔ OVERDUE               | [N]     | [Yes/No — ⚠️ if yes]   |
| 🔴 CRITICAL (≤30 days)   | [N]     | [Yes/No]               |
| 🟠 HIGH (31–90 days)     | [N]     | —                      |
| 🟡 MONITOR (91–180 days) | [N]     | —                      |
| 🟢 CALENDAR (>180 days)  | [N]     | —                      |
| **Total**                | **[N]** |                        |

[One paragraph: most urgent items, any irreversible items, overall portfolio health]

---

## ⛔ OVERDUE — Immediate Action Required

[For each overdue item:]

### [Matter ID] — [IP Type] — [Office]

**Deadline type**: [e.g., 7.5-year USPTO maintenance fee grace period]
**Was due**: [YYYY-MM-DD]
**Rule**: [37 CFR 1.362(e) / Art. 99 EPC / etc.]
**Status**: [EXPIRED — grace period also expired / In grace period until YYYY-MM-DD]
⚠️ **Irreversible**: [Yes / No]
**Restoration remedy**: [37 CFR 1.378 petition / Art. 122 EPC / None available]
**Remedy deadline**: [YYYY-MM-DD or "None"]
**Action**: [Specific steps — escalate to counsel, document cause, file petition, pay fees]
**Confidence**: [Definite / High / Probable]

---

## 🔴 CRITICAL — Due Within 30 Days

[For each critical item:]

### [Matter ID] — [IP Type] — [Office]

**Deadline type**: [e.g., Section 8 Declaration of Use — 6th anniversary]
**Due**: [YYYY-MM-DD] ([N] days)
**Rule**: [15 U.S.C. § 1058]
⚠️ **Irreversible if missed**: [Yes/No]
**Action**: [Specific preparation steps + responsible party if known]
**Confidence**: [Definite / High / Probable]

---

## 🟠 HIGH — Due in 31–90 Days

| Matter | Deadline Type | Due Date     | Days | Rule   | Action   |
| ------ | ------------- | ------------ | ---- | ------ | -------- |
| [ID]   | [Type]        | [YYYY-MM-DD] | [N]  | [Cite] | [Action] |

...

---

## 🟡 MONITOR — Due in 91–180 Days

[Summary table — same format as HIGH]

---

## 🟢 CALENDAR — Due Beyond 180 Days

[Count only, or brief table at user's option]

---

## Matters Not Calculable (Missing Date Data)

| Matter | Missing Data            | Impact                                             |
| ------ | ----------------------- | -------------------------------------------------- |
| [ID]   | [Priority date unknown] | [PCT national phase deadline cannot be calculated] |

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill covers four major IP regimes. When extending to additional jurisdictions:

1. **Japan (JPO)**: Annual renewal fees; response deadlines of 3 months from Office Action (extendable);
   national phase entry from PCT at 30 months; opposition converted to post-grant invalidation trial system. [VERIFY]
2. **China (CNIPA)**: Annual renewal fees; 3-month response to Office Action (extendable by 2 months);
   national phase entry from PCT at 30 months; 13-month deadline from publication for third-party observations. [VERIFY]
3. **Canada (CIPO)**: 6-month response to Office Action; annual maintenance fees from 2nd anniversary;
   national phase entry from PCT at 30 months. [VERIFY]
4. **Australia (IP Australia)**: 12-month response to examination report; annual renewal fees;
   30-month PCT national phase entry. [VERIFY]
5. **EU Trade Marks (EUIPO)**: 10-year renewable registrations; opposition within 3 months of
   publication in EUTM Bulletin; no examination response deadline (no substantive examination
   on relative grounds). [VERIFY]

For Madrid Protocol (WIPO) international trademark registrations: the international registration
runs for 10 years from the date of international registration, renewable through WIPO. The
"central attack" period runs 5 years from international registration — cancellation of the basic
mark during this period cancels the international registration. Flag Madrid Protocol registrations
with their central attack expiry date.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on USPTO MPEP and 37 CFR, EPC and
EPO Implementing Regulations, PCT Treaty and PCT Regulations (WIPO), Patents Act 1977 and Patents
Rules 2007 (UKIPO), Trade Marks Act 1994 (UK), and Lanham Act (15 U.S.C.). Fee schedule data
based on research as of early 2026 (EPO +5% April 2026; UKIPO +~33% April 2026) — verify
current schedules before use. Structured using the Legalcode quality framework with 17
anti-patterns, 5-tier severity classification, 5 Citation Quality Gates, Self-Interrogation
for OVERDUE items, Confidence Scoring, and Glass Box audit trail.
