---
name: legalcode-termination-risk-assessment
description: Conducts pre-termination risk assessment scoring to identify potential legal exposure before
  adverse employment actions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conducts pre-termination risk assessment scoring to identify potential legal exposure before adverse employment actions. Use before terminating an employee — especially after FMLA leave, workers' compensation claim, whistleblower report, EEO complaint, disability accommodation request, union activity, or wage complaint. Evaluates documentation adequacy (progressive discipline, PIPs, performance reviews), protected class status and adverse impact analysis (four-fifths/80% rule for group actions), temporal proximity to protected activity (FMLA, workers comp, whistleblower, EEO complaint, NLRA concerted activity), retaliation indicators (departure from policy, pretextual framing, supervisor animus, selective enforcement), consistency with prior similar situations (comparator analysis), at-will employment exceptions and implied contract risks (public policy, implied contract, good faith and fair dealing), WARN Act applicability for group terminations (100-employee federal threshold, state mini-WARN acts — CA 75, NY 50, NJ 100, IL 75), and final pay timing requirements by state (immediate, next scheduled payday, within X days). Produces a 0-100 composite risk score across six weighted categories with GO / GO-WITH-CAUTION / NO-GO / RESTRUCTURE recommendation, confidence intervals, Tier 1–3 mitigation pathways, and Glass Box audit trail. US-primary with [JURISDICTION-SPECIFIC] markers for UK Employment Rights Act 1996 / ERA 2025 and Australia Fair Work Act 2009 general protections (reverse onus).


# Legalcode Termination Risk Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted pre-termination risk
> assessment. It does not constitute legal advice. All outputs require review by a
> qualified employment lawyer licensed in the relevant jurisdiction(s) before executing
> any termination decision. Retaliation and wrongful discharge claims are fact-intensive
> and discovery-sensitive — actual litigation exposure may exceed or differ from any
> pre-action assessment once hidden facts (supervisor emails, text messages, comparator
> records, internal complaint logs) emerge during discovery. Employment law changes
> frequently; verify all statutory citations, salary thresholds, WARN Act thresholds,
> and final pay requirements against current state and federal sources before relying on
> them. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources (EEOC, DOL, Fair Work Commission, ACAS, state
> labor agencies) before relying on them. This skill does not substitute for
> individual legal advice about a specific employee's situation.

---

## Purpose and Scope

This skill conducts a structured, multi-dimensional risk assessment before an adverse
employment action (termination, constructive dismissal, or forced resignation). It
quantifies legal exposure across six risk categories, produces a composite risk score
from 0–100, and issues a GO / GO-WITH-CAUTION / NO-GO / RESTRUCTURE recommendation
with tiered mitigation pathways.

**Covers:**

- Documentation adequacy analysis — progressive discipline, PIPs, performance reviews,
  contemporaneous notes
- Protected class and adverse impact screening — individual terminations and group
  actions (RIF/layoff), four-fifths/80% rule analysis
- Temporal proximity to protected activity — FMLA leave, workers' compensation claims,
  EEO/agency complaints, whistleblower reports, NLRA Section 7 concerted activity,
  ADA accommodation requests, USERRA military service
- Retaliation indicator analysis — departure from policy, pretextual stated reason,
  supervisor animus, sudden PIP post-protected activity, selective enforcement
- Comparator and consistency analysis — similarly situated employees treated differently
- At-will employment exceptions — public policy, implied contract, implied covenant of
  good faith and fair dealing (state-by-state)
- WARN Act applicability — federal 60-day notice threshold and state mini-WARN acts
  (CA, NY, NJ, IL, MA)
- Final pay and PTO payout timing — state-by-state requirements
- UK unfair dismissal framework — ERA 1996, five potentially fair reasons, ACAS Code,
  ERA 2025 qualifying period reform [JURISDICTION-SPECIFIC]
- Australia general protections and unfair dismissal — Fair Work Act 2009, reverse
  onus under Part 3-1, small business fair dismissal code [JURISDICTION-SPECIFIC]
- Mitigation pathways — Tier 1 (must-do before termination), Tier 2 (strongly
  recommended), Tier 3 (alternative actions to consider)
- Glass Box audit trail with confidence-scored, jurisdiction-aware output

**Does not:**

- Provide legal advice or substitute for qualified employment counsel
- Draft severance or separation agreements (see `legalcode-severance-agreement-review`)
- Conduct wage and hour compliance analysis (see `legalcode-wage-hour-compliance-audit`)
- Perform internal investigation quality assessment (see `legalcode-internal-investigation`)
- Assess non-compete enforceability post-termination (see `legalcode-non-compete-enforceability`)
- Apply to independent contractor relationships (see `legalcode-independent-contractor-classification`)
- Handle constructive dismissal claims arising from employer conduct (out of scope)

**Related skills:**

- `legalcode-severance-agreement-review` — OWBPA/ADEA waiver compliance, release scope,
  consideration adequacy for high-risk individual terminations where severance is offered
- `legalcode-employee-handbook-review` — handbook policies that create implied contract
  obligations or affect documentation adequacy scoring
- `legalcode-internal-investigation` — investigation quality informs pretext analysis
- `legalcode-non-compete-enforceability` — restrictive covenant exposure post-termination
- `legalcode-wage-hour-compliance-audit` — FLSA retaliation where wage complaints filed

---

## Jurisdiction and Governing Law

This skill is US-primary with structured UK and Australia modules.

**United States**: The primary analytical framework covers federal statutes (Title VII,
ADEA, ADA, GINA, FMLA, FLSA, NLRA, OSHA, SOX, Dodd-Frank, USERRA, ERISA § 510),
the Uniform Guidelines on Employee Selection Procedures (UGESP, 29 C.F.R. Part 1607),
federal WARN Act (29 U.S.C. §§ 2101–2109; 20 C.F.R. Part 639), and state law — at-will
exceptions, final pay timing, PTO payout obligations, and state mini-WARN acts.

Montana is the only US state that is not at-will: after the probationary period (typically
6 months), the Montana Wrongful Discharge from Employment Act (WDEA, Mont. Code § 39-2-904)
requires good cause for termination. [VERIFY current WDEA interpretation]

**[JURISDICTION-SPECIFIC — United Kingdom]**: Employment Rights Act 1996 (ERA 1996),
Part X — unfair dismissal. Five potentially fair reasons: capability (s. 98(2)(a)),
conduct (s. 98(2)(b)), redundancy (s. 98(2)(c)), statutory bar (s. 98(2)(d)), some other
substantial reason / SOSR (s. 98(1)(b)). Procedural fairness: ACAS Code of Practice on
Disciplinary and Grievance Procedures (25% compensation uplift for unreasonable
non-compliance). Qualifying period: 2 years standard; reducing to 6 months under
Employment Rights Act 2025 (ERA 2025) — [VERIFY exact implementation date].
Automatically unfair dismissals require no qualifying period: whistleblowing (PIDA 1998),
pregnancy/maternity, protected disclosures, trade union activities, assertion of statutory
rights, health and safety activities, and others. Equality Act 2010: nine protected
characteristics; discrimination claims are uncapped.

**[JURISDICTION-SPECIFIC — Australia]**: Fair Work Act 2009 (Cth). Unfair dismissal
(Part 3-2): qualifying period 6 months (12 months small business — fewer than 15
employees); high income threshold (approximately $175,000–$183,000 per annum, adjusted
annually 1 July — [VERIFY current figure]); compensation cap: lower of 6 months' pay or
half the high income threshold. s. 387 fairness criteria: valid reason, notification,
opportunity to respond, support person, performance warnings, small business size, HR
expertise. General protections (Part 3-1, ss. 340–365): reverse onus — once employee
establishes adverse action and exercise of a workplace right, employer must disprove the
prohibited reason. Application deadline: 21 days for dismissal claims. Small Business
Fair Dismissal Code applies to businesses fewer than 15 employees.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the risk score in a material category
- Protected activity exists and the timeline is ambiguous
- Comparator information is incomplete or borderline
- Jurisdiction selection affects the legal framework to apply

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

### Step 1: Accept the Termination Profile

Accept the situation in any of these formats:

- **Structured input**: Employee name/ID, title, tenure, jurisdiction, reason for
  termination, supporting documentation, recent employee history
- **Free text description**: Narrative of the employment relationship, reason for
  termination, and any known risk factors
- **Document review**: Personnel file, performance reviews, discipline records, HR notes

If no input is provided, prompt the user to describe the situation.

### Step 2: Gather Jurisdiction and Situation Context

**⟁ CLARIFY** — Before beginning, ask the following. Skip questions already answered:

1. **Jurisdiction**: Where is the employee primarily based / performing work?
   - Options: US — specify state(s); United Kingdom; Australia; Multiple jurisdictions;
     Unknown
   - _Why this matters_: Final pay requirements, at-will exceptions, WARN Act (state
     variants), and the applicable legal framework all depend on jurisdiction.

2. **Termination type**: What type of adverse action is this?
   - Options: Individual involuntary termination (performance / conduct), Individual
     involuntary termination (restructuring / position elimination), Group
     layoff / RIF / mass layoff (two or more employees), Forced resignation /
     constructive dismissal, Other
   - _Why this matters_: Group actions trigger WARN Act analysis and adverse impact
     screening; individual actions focus on documentation and retaliation.

3. **Stated reason for termination**: What is the documented, intended reason?
   - Options: Performance failure, Misconduct / policy violation, Position elimination /
     restructuring, Business necessity, Attendance / reliability, Other
   - _Why this matters_: The stated reason must be consistent with the file and comparator
     treatment; a pretextual reason is a primary retaliation indicator.

4. **Protected activity in the past 12 months**: Has the employee engaged in any of
   the following in the 12 months preceding the proposed termination date?
   - Options (multiselect): FMLA leave (requested, taken, or returned from), Workers'
     compensation claim, EEOC / state agency complaint (filed or threatened), ADA
     accommodation request, Whistleblower report (internal or external), NLRA concerted
     activity / union organizing, OSHA safety complaint, FLSA wage complaint, USERRA
     military service or FMLA military qualifying exigency, None identified
   - _Why this matters_: Any YES answer triggers temporal proximity analysis and
     materially elevates the risk score.

5. **Documentation level**: Describe the documentation in the personnel file:
   - Options: Comprehensive (multiple written warnings + signed PIP + consistent
     performance reviews reflecting the issue), Moderate (some written documentation,
     but gaps or inconsistencies), Limited (mostly verbal warnings; little written
     record), None (no written documentation supporting the termination reason)
   - _Why this matters_: Documentation quality is the single largest risk modifier.

6. **Group action size (if RIF/layoff)**: If this is a group action, how many employees
   are being terminated at or around the same time?
   - Options: 1 employee (individual termination), 2–24 employees, 25–49 employees,
     50–99 employees, 100+ employees
   - _Why this matters_: WARN Act thresholds (federal: 50+ at a site; state mini-WARNs
     vary); adverse impact analysis required for any group action.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference file before analyzing the facts.

**legalcode-mcp** is the Legalcode law, regulatory, and case law database. Use it to
gather jurisdiction-specific authority before scoring:

1. **Identify the applicable state(s)** from Step 2 and search for:
   - State-specific retaliation statutes and case law (FMLA retaliation, workers' comp
     retaliation, state whistleblower protection)
   - At-will employment exceptions recognized in this state
   - State final pay and PTO payout requirements
   - State mini-WARN Act (if group termination)

2. **Save the most relevant results** to a temporary reference file:

   ```
   /tmp/legalcode-termination-research-[employee-id].md
   ```

   Structure: Key Statutes → Case Law → Regulatory Guidance → State-Specific Notes

3. **Use this reference file** when scoring the six risk categories in Step 4. Mark
   legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Proceed using general knowledge and the legal framework in this skill
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Step 4: Extract the Risk Factor Matrix

Extract facts from the provided documentation or description and map them against the
six risk categories below. Score each category independently before aggregating.

This step is non-interactive. Extract from whatever information is available and flag
information gaps explicitly.

**For each risk category, record:**

- The relevant facts extracted from the personnel file / situation description
- The sub-factor scores and total category score
- The category classification (GREEN / YELLOW / RED)
- Any information gaps that, if filled, could materially change the score

---

### Risk Category 1: Documentation Adequacy (max 15 points)

Documentation is the single most important defense in wrongful termination litigation.
A legally defensible termination requires a **clear, consistent, and contemporaneous**
paper trail demonstrating: the existence of the performance or conduct issue, notice to
the employee, opportunity to improve, progressive discipline consistently applied, and a
legitimate business reason that predates any protected activity.

| Sub-Factor                                                                                      | Points |
| ----------------------------------------------------------------------------------------------- | ------ |
| Contemporaneous performance reviews reflecting the issue (annual or more frequent)              | 0–4    |
| Written warnings / counseling notes (signed by employee and supervisor)                         | 0–4    |
| Written Performance Improvement Plan (specific, measurable, time-bound goals; check-in records) | 0–4    |
| Progressive discipline applied consistently (verbal → written → final → termination)            | 0–3    |

**Scoring:**

- **0–4 points** (RED): No written documentation, or single informal note only. Termination
  is legally exposed. No documentation for the stated reason is the highest-risk scenario
  in retaliation litigation.
- **5–9 points** (YELLOW): Partial documentation — some written notes but gaps exist,
  or PIP was introduced only after protected activity. Mitigation needed.
- **10–15 points** (GREEN): Comprehensive, consistent, contemporaneous file. Strong
  defense against retaliation and wrongful termination claims.

**Documentation red flags** (each increases score risk by 2–3 points):

- PIP introduced within 90 days of protected activity with no prior written warnings
- Performance evaluations immediately preceding termination contradict the stated reason
- File contains no employee-signed acknowledgment of warnings
- Supervisor who issued documentation was replaced post-protected activity by a new
  decision-maker who lacks personal knowledge of the stated issue
- Documentation uses generic language ("attitude problem," "not a cultural fit") rather
  than specific, observable behaviors with dates and consequences

**[JURISDICTION-SPECIFIC — UK]**: For conduct dismissals, ACAS Code of Practice requires
investigation, written notification of allegations, a disciplinary hearing before decision,
and right of appeal. Absence of any of these steps is a procedural unfairness finding
carrying up to 25% compensation uplift.

**[JURISDICTION-SPECIFIC — Australia]**: Under s. 387(e) FW Act, for performance
dismissals, the employer must have **warned** the employee about the unsatisfactory
performance before dismissal (unless a single incident justifies immediate dismissal).
Absence of a prior performance warning is an independent ground for unfair dismissal.

---

### Risk Category 2: Protected Class and Adverse Impact (max 10 points)

Protected class membership alone does not create liability — it is a risk multiplier when
combined with other factors. For group actions, disparate impact analysis is mandatory.

| Sub-Factor                                                                                                                                                                       | Points |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Employee is a member of one or more protected classes (race, sex, age 40+, disability, pregnancy, national origin, religion, LGBTQ+ status, veteran status, genetic information) | 0–3    |
| Employee is the only member of a protected class in the affected group, or the protected class is disproportionately represented in the termination group                        | 0–3    |
| Adverse impact analysis (group actions): four-fifths / 80% rule fails for a protected group in the selection pool                                                                | 0–4    |

**Adverse Impact Analysis — Four-Fifths (80%) Rule (UGESP, 29 C.F.R. Part 1607):**

For group terminations, apply the four-fifths rule:

1. For each protected group, calculate: [termination rate for group] ÷ [termination rate for highest-rate group]
2. If the result is less than 0.80 (80%), adverse impact is indicated
3. For small samples (fewer than 30 employees), also consider statistical significance tests (chi-square, Fisher's exact test, z-test for proportions)
4. Adverse impact must be assessed for: race and ethnicity (all EEOC categories), sex / gender, age (employees 40+), national origin, disability status, veterans' status, and state-protected categories

**Scoring:**

- **0–2 points** (GREEN): No protected class present; no adverse impact in group action
- **3–5 points** (YELLOW): Protected class present; no group adverse impact or single comparator class
- **6–10 points** (RED): Protected class present with adverse impact in group action (4/5 rule fails), or employee is sole or disproportionate member of protected class in action

**[JURISDICTION-SPECIFIC — UK]**: Under Equality Act 2010, nine protected characteristics.
Dismissal connected to a protected characteristic may be direct discrimination (no
justification defence) or indirect discrimination (can be justified by proportionate means).
No qualifying period for discrimination claims; uncapped compensation including injury
to feelings.

**[JURISDICTION-SPECIFIC — Australia]**: General protections (Part 3-1 FW Act, s. 340):
adverse action for reasons including protected attributes (race, colour, sex, sexual
orientation, age, physical or mental disability, marital status, family/carer
responsibilities, pregnancy, religion, political opinion, national extraction, social
origin) is unlawful. Reverse onus: once employee establishes adverse action + protected
attribute, employer must prove the action was not for a prohibited reason.

---

### Risk Category 3: Temporal Proximity to Protected Activity (max 15 points)

Courts apply the **temporal proximity doctrine**: a close temporal connection between
protected activity and adverse employment action can, standing alone, establish the
causal connection element of a retaliation prima facie case under _McDonnell Douglas
Corp. v. Green_, 411 U.S. 792 (1973) burden-shifting.

Courts have generally held that proximity must be "very close" to be sufficient alone.
Combine with other factors (documentation gaps, retaliation indicators) to assess the
full causal nexus. [VERIFY specific circuit holdings for the applicable jurisdiction]

| Days Between Protected Activity and Proposed Termination | Risk Points | Courts' Characterization                                              |
| -------------------------------------------------------- | ----------- | --------------------------------------------------------------------- |
| 0–30 days                                                | 15          | Near-certain retaliation inference; highest risk                      |
| 31–60 days                                               | 13          | Strong presumption sufficient alone in most circuits                  |
| 61–90 days                                               | 10          | Sufficient alone in many circuits; generally triggers scrutiny        |
| 91–180 days                                              | 6           | Presumption weakens; still material with corroborating indicators     |
| 181–365 days                                             | 3           | Presumption attenuates significantly; requires corroborating evidence |
| More than 365 days / no protected activity               | 0           | Not probative of retaliation without other evidence                   |

**Use the MOST RECENT protected activity** when calculating proximity. If multiple
protected activities occurred in the past 12 months, score for the most recent.

**Protected activity reference table (score applies for each type detected):**

| Protected Activity Type                                  | Primary Statute(s)                                    | Notes                                                                                      |
| -------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| FMLA leave (requested, taken, or returned from)          | 29 U.S.C. § 2615; 29 C.F.R. § 825.220                 | Requesting leave is protected even if leave not ultimately taken                           |
| Workers' compensation claim                              | State law (varies significantly)                      | Filing, reporting injury, or threatening to file is protected                              |
| EEOC / state agency complaint (filed or threatened)      | Title VII § 704; ADEA § 623(d); ADA § 503             | Even informal oral opposition can be protected activity                                    |
| ADA accommodation request                                | 42 U.S.C. § 12203                                     | Requesting is protected; engaging in interactive process is protected                      |
| Whistleblower report (internal or to external regulator) | SOX § 806; Dodd-Frank § 922; state whistleblower acts | Internal reports may qualify; external reports to SEC/CFTC carry strongest protection      |
| NLRA Section 7 concerted activity / union organizing     | 29 U.S.C. § 158(a)(1)–(a)(3)                          | Discussing wages with coworkers is protected even without union                            |
| OSHA safety complaint                                    | 29 U.S.C. § 660(c)                                    | Reporting unsafe conditions is protected                                                   |
| FLSA wage complaint                                      | 29 U.S.C. § 215(a)(3)                                 | Oral complaints to supervisor may qualify; circuit split on whether informal is sufficient |
| USERRA military service                                  | 38 U.S.C. § 4311                                      | Service-related absence or reporting for duty is protected                                 |
| ERISA § 510 benefits claim / activity                    | 29 U.S.C. § 1140                                      | Particularly high risk pre-vesting or near plan eligibility dates                          |

**Continuing violation doctrine**: If a pattern of adverse actions began during or
immediately after protected activity, the proximity analysis looks at when the adverse
treatment **started**, not just the termination date.

**[JURISDICTION-SPECIFIC — UK]**: Under PIDA 1998 (incorporated in ERA 1996, ss. 43A-43L,
47B), detriment or dismissal for a protected disclosure is automatically unfair dismissal
with no qualifying period and uncapped compensation. "Qualifying disclosure" requires
reasonable belief in the public interest. Temporal proximity analysis is used by
Employment Tribunals similarly to US courts.

**[JURISDICTION-SPECIFIC — Australia]**: General protections (FW Act, s. 361): once
the employee shows they exercised a workplace right AND suffered adverse action, the
onus reverses — employer must disprove that the action was for the prohibited reason.
Application deadline: 21 calendar days from dismissal.

---

### Risk Category 4: Retaliation Indicators (max 15 points)

Temporal proximity establishes timing. Retaliation indicators establish intent. Together,
they constitute a composite causal nexus that is far stronger than either alone.

Score for each retaliation indicator present. Each indicator adds to the category score:

| Retaliation Indicator                                                                                                                                                           | Points |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Termination departs from documented progressive discipline policy without prior waiver or exception                                                                             | 3      |
| PIP or formal discipline was imposed immediately after (within 60 days of) protected activity, with no prior written documentation                                              | 3      |
| Stated termination reason does not match prior performance evaluations (e.g., no prior performance concerns in file; last review rated employee "meets expectations" or better) | 3      |
| Supervisor or HR made contemporaneous negative comments about the protected activity (emails, texts, meeting notes referencing leave, complaint, or union activity)             | 3      |
| Decision-maker was aware of the protected activity before the termination decision                                                                                              | 2      |
| Termination timeline was accelerated or decision pre-dated investigation completion                                                                                             | 2      |
| Policy was applied differently here than in prior similar situations (selective enforcement)                                                                                    | 2      |
| No opportunity was given to respond to the stated reason before the termination decision                                                                                        | 1      |

**Cap**: Max 15 points regardless of cumulative total.

**Scoring:**

- **0–3 points** (GREEN): No material retaliation indicators; termination appears non-retaliatory
- **4–9 points** (YELLOW): One or two moderate indicators; mitigation required to reduce pretext risk
- **10–15 points** (RED): Multiple strong indicators; pretext inference is plausible; high litigation risk

**Pretext analysis guidance** (_McDonnell Douglas_ burden-shifting):

- Once the employee establishes a prima facie case (protected class/activity → adverse
  action → causal nexus), the burden shifts to the employer to articulate a legitimate,
  non-discriminatory / non-retaliatory reason
- Then the employee must demonstrate the stated reason is **pretextual** (i.e., unworthy
  of credence or a cover for discrimination / retaliation)
- Contradictory documentation, departures from policy, and comparator inconsistency are
  the primary pretext evidence sources

---

### Risk Category 5: Comparator and Consistency Analysis (max 15 points)

"Comparator analysis" asks: were similarly situated employees outside the protected class
(or who had not engaged in protected activity) treated the same way for the same or
similar conduct? Inconsistent treatment is among the strongest forms of pretext evidence.

| Sub-Factor                                                                                                                                                                                | Points |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Other employees in the same or substantially similar role were not terminated for the same or similar conduct (strong inconsistency — same supervisor, same department, same time period) | 0–8    |
| Prior employees with documented worse performance / conduct records were retained or given additional progressive discipline opportunities                                                | 0–4    |
| Inconsistency is systemic (multiple comparators or pattern across department) rather than isolated                                                                                        | 0–3    |

**Comparator closeness standard** (courts apply the "similarly situated in all material
respects" test, not identical): Key comparator factors are:

- Same or substantially similar job function and level
- Same supervisor or decision-maker
- Same or similar conduct or performance issue
- Same time period (usually within 1–2 years)
- Comparator did not engage in protected activity (or, for adverse impact, comparator is
  not a member of the protected class)

**Scoring:**

- **0–3 points** (GREEN): No adverse comparators identified; treatment is consistent
- **4–9 points** (YELLOW): One or two comparators showing some inconsistency; document
  differentiating factors
- **10–15 points** (RED): Multiple strong comparators showing systemic inconsistency;
  creates strong inference of disparate treatment or retaliation

**⟁ CLARIFY** — If comparator information is not provided, ask:

- "Are you aware of other employees in similar roles who were treated more leniently for
  the same or similar conduct? For example: retained despite the same performance issues,
  given additional PIP cycles, or demoted rather than terminated?"
- Provide options: Yes (with specifics), No, Unknown / not yet reviewed
- _Why this matters_: If comparator information exists, it is likely the most powerful
  evidence the opposing party will marshal. Identifying it now protects against surprise.

---

### Risk Category 6: State-Specific Statutory Exposure (max 15 points)

These are statutory violations independent of the termination decision — they create
liability regardless of whether the underlying termination is defensible.

| Sub-Factor                                                                                                                                                                                                                       | Points |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Final pay timing: proposed action does not comply with state requirement (e.g., California — immediate; Colorado — immediate; Massachusetts — immediate; New York — next payday; other states vary)                              | 0–5    |
| PTO / accrued vacation payout: employer has not addressed accrued leave payout per applicable state rule (California — mandatory; Colorado — mandatory; Montana — mandatory; employer-policy states — depends on written policy) | 0–4    |
| Severance obligation: employment agreement, offer letter, or plan document creates contractual or ERISA-governed severance obligation not accounted for                                                                          | 0–3    |
| WARN Act non-compliance: group termination meets federal or state trigger threshold without 60/90-day notice plan                                                                                                                | 0–3    |

**Final Pay Quick Reference (key states — [VERIFY current requirements before acting]):**

| State         | Involuntary Termination — Final Pay Timing        |
| ------------- | ------------------------------------------------- |
| California    | Immediately upon termination (Labor Code § 201)   |
| Colorado      | Immediately upon termination                      |
| Massachusetts | Immediately upon termination                      |
| Montana       | Immediately upon termination                      |
| Nevada        | Immediately (or within 3 days if no prior notice) |
| Illinois      | Next scheduled payday                             |
| New York      | Next scheduled payday                             |
| Texas         | Within 6 calendar days                            |
| Washington    | End of established pay period                     |
| Florida       | Next regular payday                               |
| All others    | Verify against current state DOL guidance         |

**PTO Payout — Key Rules ([VERIFY before acting]):**

- **California**: Accrued vacation is earned wages; must be paid on termination; use-it-or-lose-it prohibited (Labor Code § 227.3)
- **Colorado**: Accrued vacation must be paid on termination (Colorado Wage Claim Act)
- **Montana**: Accrued vacation must be paid on termination
- **Most other states**: Payout required if employer policy provides for it; employers may disclaim payout in a written policy, but inconsistent application undermines enforceability
- **Sick leave**: California explicitly does NOT require payout of accrued sick leave (separate from vacation)

**WARN Act Quick Reference:**

| Requirement             | Federal WARN                | CA WARN                              | NY WARN                             | NJ WARN                                   |
| ----------------------- | --------------------------- | ------------------------------------ | ----------------------------------- | ----------------------------------------- |
| Employer size threshold | 100+ employees              | 75+ employees                        | 50+ employees                       | 100+ employees                            |
| Trigger (site)          | 50+ employees (33% or 500+) | 50+ employees (any %)                | 25+ employees (25%/min 25, or 250+) | 50+ employees                             |
| Notice period           | 60 days                     | 60 days                              | **90 days**                         | 90 days (closing) / 60 days (mass layoff) |
| Mandatory severance     | No                          | No                                   | No                                  | **Yes — 1 week/year of service**          |
| Federal exceptions      | Yes (3 statutory)           | No faltering/unforeseeable exception | Limited                             | Limited                                   |

**Scoring:**

- **0–2 points** (GREEN): Full compliance with all statutory obligations
- **3–9 points** (YELLOW): One or two timing or payout gaps; correctable before termination
- **10–15 points** (RED): WARN Act non-compliance, or mandatory severance obligation unaddressed; creates independent statutory liability

---

### Step 5: Calculate the Composite Risk Score

#### 5a. Sum the Category Scores

| Category                            | Max Points | Actual Score | Classification     |
| ----------------------------------- | ---------- | ------------ | ------------------ |
| 1. Documentation Adequacy           | 15         | [X]          | [GREEN/YELLOW/RED] |
| 2. Protected Class & Adverse Impact | 10         | [X]          | [GREEN/YELLOW/RED] |
| 3. Temporal Proximity               | 15         | [X]          | [GREEN/YELLOW/RED] |
| 4. Retaliation Indicators           | 15         | [X]          | [GREEN/YELLOW/RED] |
| 5. Comparator & Consistency         | 15         | [X]          | [GREEN/YELLOW/RED] |
| 6. State-Specific Statutory         | 15         | [X]          | [GREEN/YELLOW/RED] |
| **TOTAL**                           | **85**     | **[X]**      |                    |

#### 5b. Scale to 0–100

Composite Risk Score = (Sum ÷ 85) × 100, rounded to nearest integer

#### 5c. Apply the Risk Classification and GO/NO-GO Table

| Scaled Score | Classification   | GO/NO-GO                | Confidence Baseline | Recommended Action                                                                                                                                                                 |
| ------------ | ---------------- | ----------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0–20**     | **GREEN**        | **GO**                  | High                | Proceed. Standard precautions (document decision, confirm final pay compliance). Annual review of file completeness recommended.                                                   |
| **21–35**    | **YELLOW-LIGHT** | **GO with Caution**     | Medium–High         | Implement Tier 1 mitigation steps before proceeding. Legal review optional but recommended for employees with recent protected activity.                                           |
| **36–50**    | **YELLOW**       | **GO with Conditions**  | Medium              | Tier 1 + Tier 2 mitigation required before proceeding. Employment counsel review strongly recommended. Consider whether timing adjustment or additional documentation is feasible. |
| **51–65**    | **RED-LIGHT**    | **NO-GO / Restructure** | Medium              | Recommend AGAINST proceeding without major restructuring. Tier 3 alternatives (demotion, PIP extension, mutual separation) should be explored. Counsel review mandatory.           |
| **66–80**    | **RED**          | **STRONG NO-GO**        | High                | Extreme exposure. Alternative actions strongly recommended. If proceeding, offer severance with general release (OWBPA compliance for employees 40+).                              |
| **81–100**   | **CRITICAL**     | **ABSOLUTE NO-GO**      | High                | Do not terminate without explicit employment counsel authorization and full mitigation execution. Litigation risk is severe and may exceed insurance reserves.                     |

#### 5d. Confidence Interval

Apply a confidence interval to the composite score:

- **Narrow CI (±5 points)**: Strong documentation, clear comparator record, unambiguous protected activity timeline
- **Medium CI (±10 points)**: Some documentation gaps or ambiguous comparator facts
- **Wide CI (±15 points)**: Significant information gaps, disputed facts, evolving regulatory landscape

Report as: **Score: [X]/100 (likely range: [X-CI]–[X+CI])**

### Step 6: Quality Verification

Before producing any output, run these quality gates silently. Revise failures before delivery.

#### Citation Quality Gates (run silently)

| Gate           | Rule                                                                                                    | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, case, or established principle                  | Add citation or mark [VERIFY]       |
| **Format**     | All citations follow consistent, recognizable format (29 U.S.C. § XXXX; Cal. Lab. Code § XXX)           | Fix format                          |
| **Currency**   | Every cited provision checked for amendments, repeal, or administrative action                          | Flag [CHECK CURRENCY]               |
| **Domain**     | Analysis stays within the applicable jurisdiction's law; no bleed of CA-specific rules into TX analysis | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                               | Add confidence qualifier            |

#### Self-Interrogation for RED and CRITICAL Risk Scores

For any item classified RED or CRITICAL, and for the composite score if 51+, apply this
3-pass adversarial review before finalizing:

**Pass 1 — Legal Chain Integrity**: Does the risk finding follow logically from the
cited authority? Would a court / arbitrator / tribunal actually reach this conclusion
based on the facts presented? Are there circuit splits or jurisdiction-specific rules
that undermine the finding?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and principles been
considered? Are there mitigating facts not yet surfaced? Is the comparator analysis
complete, or might favorable comparators exist that haven't been identified?

**Pass 3 — Challenge**: What is the strongest argument AGAINST this risk classification?
Under what circumstances might a reasonable employment lawyer advise that the risk is
manageable? What documentation, if added now, would materially reduce the score?

Conclude: confirm the classification or adjust with explicit rationale.

#### Confidence Scoring

| Level        | Range     | Meaning                                       | Action                                       |
| ------------ | --------- | --------------------------------------------- | -------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, unambiguous facts | State with confidence                        |
| **High**     | 0.80–0.94 | Strong authority, minor factual questions     | State with brief caveat                      |
| **Probable** | 0.60–0.79 | Good arguments, some uncertainty              | State with reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; fact-intensive           | Flag for professional review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                       | Do not assert; flag [UNCERTAIN]              |

### Step 7: Produce the Risk Assessment Output

Deliver the full output following the **Output Format Template** in the final section.

**⟁ CLARIFY** — Before generating mitigation recommendations, ask if not already known:

- **Proceeding despite risk**: "Given the risk score, do you want mitigation steps for
  proceeding (Tier 1 and Tier 2), or a full restructuring / alternatives analysis (Tier 3)?"
- **Group action WARN planning**: "Is outside counsel already involved in WARN analysis
  for this group action?" If yes, defer WARN specifics to counsel; summarize exposure only.
- **Severance intent**: "Is a severance offer planned? If yes, high-risk terminations
  should be reviewed against `legalcode-severance-agreement-review` for OWBPA compliance
  (employees 40+) and release scope before execution."

---

## Mitigation Framework

### Tier 1 — Non-Negotiable (must complete before any YELLOW or above termination)

1. **Documentation gap remediation**: Create or obtain contemporaneous documentation
   of the legitimate business reason. If documentation is being created now, ensure it
   accurately reflects the history and is not forward-dated or post-hoc framing.
2. **HR and legal chain sign-off**: Confirm HR review and, for scores of 36+, outside
   employment counsel review of the proposed action before it is executed.
3. **Final pay compliance verification**: Confirm the state-specific final pay timing
   requirement and accrued leave payout obligation are addressed in the termination plan.
4. **WARN Act threshold check**: For group actions of 50+ employees, confirm a WARN
   analysis has been completed by employment counsel before the termination date is set.
5. **COBRA notification**: Arrange timely COBRA election notice — 14 days from plan
   administrator's knowledge of qualifying event (29 C.F.R. § 2590.606-4). Failure to
   provide timely notice creates statutory penalties.

### Tier 2 — Strongly Recommended (for YELLOW and RED scores)

1. **Comparator audit**: Identify all similarly situated employees outside the protected
   class or who have not engaged in protected activity and document their treatment for
   the same conduct. If favorable comparators exist for the employer, document the
   differentiating factors.
2. **Decision-maker substitution review**: If the primary decision-maker has personal
   knowledge of the employee's protected activity or has made comments reflecting
   hostility, consider involving a second decision-maker with independent knowledge.
3. **Timing assessment**: For scores driven primarily by temporal proximity (Category 3),
   assess whether the termination decision is truly ripe. A delay to allow additional
   documentation of independent grounds reduces the proximity argument. Do not delay
   indefinitely — protracted delay after documented cause can create its own problems.
4. **Stated reason alignment audit**: Confirm that the stated termination reason in
   all documents (termination letter, HRIS, severance paperwork, EEOC response form)
   is consistent and matches the file.
5. **Supervisor communication audit**: Review recent supervisor communications (email,
   Teams/Slack, text) for comments referencing the employee's protected activity,
   protected class, or any statements that could evidence animus.

### Tier 3 — Alternative Actions (for RED and CRITICAL scores where termination risk exceeds business benefit)

| Alternative                                                     | When to Use                                                                             | Risk Reduction                                                                                          |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Extended PIP with additional documentation period**           | Documentation gaps; premature termination timeline                                      | Rebuilds documentation record; delays clock on temporal proximity                                       |
| **Demotion or role change**                                     | Business need met by reduced responsibility; position elimination but employee retained | Avoids termination claim entirely; separate analysis needed for demotion-as-retaliation risk            |
| **Mutual separation agreement**                                 | Employee likely to sue; severance can be conditioned on release of claims               | Converts adverse action to negotiated departure; severance review required                              |
| **Internal transfer**                                           | Performance issue is supervisor-specific; cross-department performance is adequate      | Separates employee from problematic supervisor; tests legitimate performance diagnosis                  |
| **Last-chance agreement (LCA)**                                 | Misconduct requiring one final clear-line notice                                        | Documents notice and opportunity; provides unambiguous basis for future termination                     |
| **Severance offer with full release (OWBPA-compliant for 40+)** | Score 51+; termination must proceed for business reasons                                | Buys out claim; requires 21-day consideration + 7-day revocation (individual) or 45-day + 7-day (group) |

---

## Anti-Patterns

What NOT to do in pre-termination risk assessment:

1. **Assuming at-will status eliminates all risk** — At-will employment means you can
   terminate for any reason, not for a discriminatory or retaliatory reason. At-will is
   not a defense to Title VII, ADEA, ADA, FMLA retaliation, or state law claims.

2. **Creating documentation after protected activity and calling it "contemporaneous"**
   — Courts and opposing counsel know how to use metadata, email timestamps, and
   document version histories. Backdated or post-hoc documentation is worse than no
   documentation: it is evidence of consciousness of guilt.

3. **Conflating a different reason with a legitimate reason** — "We fired Person A for
   attendance and Person B for performance" are different stated reasons but that alone
   does not refute a retaliation claim. The question is whether _this_ termination, for
   _this_ employee, at _this_ time, would have occurred absent the protected activity.

4. **Skipping temporal proximity analysis because the employee has been a "problem" for
   years"** — Courts look at the timing of the _decision to terminate_, not just the
   start of performance issues. A long-troubled employee terminated within 30 days of
   filing an EEOC charge still presents high temporal proximity risk.

5. **Performing comparator analysis only for the protected class** — Comparator analysis
   must also include employees who have not engaged in protected activity. Retaliation
   comparators are employees without the protected activity, not just employees outside
   the protected class.

6. **Forgetting WARN Act analysis for "small" group actions** — Two or three individual
   terminations announced in the same week, aggregated with earlier terminations in the
   same 90-day rolling window, can trigger WARN if the cumulative count meets the
   threshold. Use the 90-day aggregation window.

7. **Applying California final pay rules to non-California employees** — Final pay law
   varies dramatically by state. Immediate payment in California is not the rule in
   Texas, New York, or Florida. Confirm state-specific requirements before setting the
   termination date and logistics.

8. **Relying on the "business restructuring" label to avoid documentation requirements**
   — A "position elimination" is a valid non-discriminatory reason, but only if the
   position is actually eliminated and not refilled within a reasonable period. If the
   role is refilled within 6–12 months, it begins to look like a pretextual elimination.

9. **Assuming investigation completeness reduces risk automatically** — An unfair or
   partial investigation (single investigator who is the accused manager's supervisor;
   no interview of the complaining employee; foregone conclusion reaching) can increase
   pretext risk rather than reducing it.

10. **Missing ERISA § 510 exposure near plan eligibility or vesting dates** — Terminating
    an employee shortly before they would vest in a retirement plan, qualify for a bonus,
    or become eligible for health benefits creates independent ERISA § 510 retaliation
    exposure. Calculate benefit cliff dates before setting termination timing.

11. **Treating "HR approved" as equivalent to "legally reviewed"** — HR sign-off is
    necessary but not sufficient. For terminations scoring 36+ or involving recent
    protected activity, independent employment counsel review is the standard of care.

12. **Ignoring UK procedural fairness for remote or expatriate employees** — UK employees
    working for US-headquartered organizations are protected by ERA 1996 regardless of
    where the organization is based. The ACAS Code applies; failure to investigate, give
    notice, hold a hearing, and offer appeal is procedural unfairness.

13. **Assuming Australia's general protections reverse onus is manageable without
    counsel** — Under s. 361 FW Act, once the employee establishes adverse action and
    exercise of a workplace right, the burden shifts entirely to the employer. This is
    categorically different from US burden-shifting and is operationally more difficult
    to overcome.

14. **Applying the four-fifths rule only to race and sex** — Adverse impact analysis
    in a RIF must cover all protected classes: age (40+), disability, national origin,
    religion, sex, race, ethnicity, veterans' status, and state-protected categories.
    Overlooking age disparate impact in a reduction that disproportionately affects
    employees over 50 is a common and costly error.

15. **Offering severance without OWBPA compliance for employees 40+** — If a general
    release is included in a separation agreement with an employee 40 or older, the
    OWBPA seven-factor knowing-and-voluntary test applies, including 21-day consideration
    period (45 days for group actions) and non-waivable 7-day revocation window. A
    defective waiver is void and does not release ADEA claims even if the employee
    accepted the severance. See `legalcode-severance-agreement-review`.

16. **Forgetting to account for protected activity by associates** — Title VII and ADA
    anti-retaliation provisions protect employees from adverse action because of a family
    member's or close associate's protected activity or protected class membership.

17. **Conflating "involuntary termination" with "position elimination" in WARN
    analysis** — WARN applies based on employment loss status regardless of the label
    used. A "voluntary" separation induced by a constructive dismissal may still count
    toward WARN thresholds if a court later determines the separation was involuntary.

18. **Producing a risk score without a confidence interval** — A score of 52 stated
    alone suggests precision that does not exist. Reporting "52 ± 12 (likely range 40–64)"
    honestly reflects the evidentiary gaps and prevents overconfidence in a borderline
    number.

19. **Failing to coordinate across state lines in multi-state RIFs** — Where employees
    across multiple states are terminated in the same action, each state's mini-WARN
    thresholds must be analyzed independently. California and New York have their own
    separate final pay, WARN, and adverse impact obligations.

20. **Treating this assessment as final without legal review** — This skill quantifies
    risk; it does not eliminate it. All RED and CRITICAL scores, and any YELLOW score
    involving recent protected activity, require review by a qualified employment lawyer
    before the termination decision is executed.

---

## Writing Standards

Before delivering any output, verify:

- [ ] All risk scores are explained by reference to specific facts provided (not generic)
- [ ] Every legal claim includes a statutory citation or is marked [VERIFY]
- [ ] Jurisdiction-specific content is clearly marked [JURISDICTION-SPECIFIC] or
      limited to the applicable jurisdiction
- [ ] Confidence intervals are reported alongside scores (not bare numbers)
- [ ] The GO/NO-GO recommendation includes an explicit rationale tied to the score bands
- [ ] Mitigation steps are concrete and actionable (not "improve documentation" — instead
      "obtain signed acknowledgment from employee of the [DATE] written warning")
- [ ] Comparator gaps are identified explicitly rather than dismissed
- [ ] Anti-hallucination: no court citations have been invented; uncertain authority
      is marked [VERIFY]

**Plain-language discipline**: Write for an HR director and general counsel reading
simultaneously. Use legal terms where they matter (temporal proximity, prima facie case,
reverse onus) but define them briefly in context. Do not use jargon to fill space.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for state-specific final pay law, at-will exceptions, workers'
  compensation retaliation statutes, and state mini-WARN provisions for the applicable
  jurisdiction(s)
- Save results to `/tmp/legalcode-termination-research-[id].md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed using the general framework in this skill
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that the reviewer verify state-specific final pay requirements against
  current state DOL guidance and mini-WARN requirements with employment counsel

---

## Localization Notes

**For US terminations**: This skill covers all 50 states. State-specific elements
(final pay, at-will exceptions, workers' comp retaliation, mini-WARN) require state-level
verification. Montana is the only non-at-will state and is explicitly noted in the
framework. California, New York, New Jersey, Illinois, and Massachusetts present the
highest statutory exposure due to their mini-WARN, final pay, and retaliation regimes.

**For UK terminations**: Apply the UK unfair dismissal and Equality Act frameworks. Note
that ERA 2025 changes (qualifying period, industrial action protections, fire-and-rehire
restrictions) are phasing in 2025–2027 — verify current implementation status. ACAS
Code procedural analysis is mandatory for conduct and capability dismissals.

**For Australia terminations**: Apply both the unfair dismissal framework (Part 3-2)
and general protections (Part 3-1). Note that for any dismissal involving exercise of
a workplace right, the general protections reverse onus makes Part 3-1 the higher-risk
pathway. Application window is 21 days — extremely short.

---

## Output Format Template

Deliver output in this format:

````markdown
# TERMINATION RISK ASSESSMENT

[Employee Identifier] | [Primary Jurisdiction] | [Assessment Date]

---

## EXECUTIVE SUMMARY

**Composite Risk Score: [X]/100 (likely range: [X-CI]–[X+CI])**
**Classification: [GREEN / YELLOW-LIGHT / YELLOW / RED-LIGHT / RED / CRITICAL]**
**Recommendation: [GO / GO-WITH-CAUTION / GO-WITH-CONDITIONS / NO-GO / RESTRUCTURE]**
**Overall Confidence: [HIGH / MEDIUM / LOW]**

[2–4 sentence summary of the primary risk drivers and the basis for the recommendation.
Reference the highest-scoring categories and the key facts driving them.]

---

## PART 1: TERMINATION PROFILE

**Employee:** [Role, tenure, protected class(es) if applicable, age (if 40+ for OWBPA)]
**Proposed Reason:** [Stated termination reason]
**Termination Type:** [Individual / Group RIF — N employees]
**Primary Jurisdiction:** [State / UK / Australia]
**Proposed Effective Date:** [Date or "TBD"]
**Severance Offered:** [Yes — amount / No / TBD]

---

## PART 2: PROTECTED ACTIVITY TIMELINE

**Most Recent Protected Activity:** [Type] on [Date] — [X] days from proposed termination
**Temporal Proximity Assessment:** [STRONG PRESUMPTION / MODERATE / WEAK / NONE]

| Date   | Protected Activity | Type      | Days to Termination |
| ------ | ------------------ | --------- | ------------------- |
| [Date] | [Description]      | [Statute] | [X] days            |

**Retaliation Presumption Status:** [Explanation of strength based on proximity and corroborating indicators]

---

## PART 3: RISK CATEGORY SCORECARDS

### Category 1: Documentation Adequacy [X]/15 — [GREEN/YELLOW/RED]

**Sub-factor scores:** [List]
**Key finding:** [What documents exist; what is missing; specific gap(s)]
**Information gaps:** [What additional documentation would lower this score]

### Category 2: Protected Class & Adverse Impact [X]/10 — [GREEN/YELLOW/RED]

**Protected classes present:** [List]
**Adverse impact analysis (group actions):** [4/5 rule result or N/A]
**Key finding:** [Assessment of class exposure]

### Category 3: Temporal Proximity [X]/15 — [GREEN/YELLOW/RED]

**Days since most recent protected activity:** [X]
**Applicable statute:** [FMLA / Title VII / State Workers Comp / etc.]
**Key finding:** [Strength of proximity presumption; corroborating factors]

### Category 4: Retaliation Indicators [X]/15 — [GREEN/YELLOW/RED]

**Indicators present:** [List each; number of points each contributes]
**Key finding:** [Strongest indicator(s) and their combined effect]

### Category 5: Comparator Analysis [X]/15 — [GREEN/YELLOW/RED]

**Comparators identified:** [List with role, demographics, conduct, outcome]
**Key finding:** [Strength of inconsistency; whether differentiating factors exist]

### Category 6: State-Specific Statutory [X]/15 — [GREEN/YELLOW/RED]

**Final pay timing required:** [State rule] — **Status:** [Compliant / Gap]
**PTO payout obligation:** [State rule / policy] — **Status:** [Compliant / Gap]
**WARN Act:** [Applicable / Not applicable] — **Status:** [Plan / No plan / N/A]
**Severance obligation:** [Contract / Plan / None]
**Estimated statutory exposure (if non-compliant):** [$X or N/A]

### Score Summary

| Category                  | Score   | Max     | Classification       |
| ------------------------- | ------- | ------- | -------------------- |
| 1. Documentation          | [X]     | 15      | [COLOR]              |
| 2. Protected Class        | [X]     | 10      | [COLOR]              |
| 3. Temporal Proximity     | [X]     | 15      | [COLOR]              |
| 4. Retaliation Indicators | [X]     | 15      | [COLOR]              |
| 5. Comparator             | [X]     | 15      | [COLOR]              |
| 6. Statutory              | [X]     | 15      | [COLOR]              |
| **TOTAL**                 | **[X]** | **85**  |                      |
| **Scaled (0–100)**        | **[X]** | **100** | **[CLASSIFICATION]** |

---

## PART 4: JURISDICTION-SPECIFIC ANALYSIS

### [US — Primary]

**Federal Retaliation Exposure:**

- Applicable statutes: [List relevant statutes given protected activity type]
- Prima facie case assessment: [STRONG / MODERATE / WEAK] — rationale
- Burden-shifting position: [Where does burden currently rest given facts?]

**State-Specific Exposure — [State]:**

- At-will exceptions applicable: [Public policy / Implied contract / Good faith / None]
- Final pay compliance status: [Compliant / Gap — amount]
- PTO payout compliance: [Compliant / Gap]
- State mini-WARN: [Applicable / Not applicable]
- Workers' comp retaliation: [Applicable statute if recent claim]

### [UK — if applicable]

**Qualifying period status:** [Met 2-year / Not met / ERA 2025 6-month post-implementation]
**Potentially fair reason:** [Capability / Conduct / Redundancy / SOSR / None identified]
**ACAS Code compliance:** [Investigation completed / Hearing held / Appeal offered]
**Automatically unfair risk:** [Protected disclosure / Pregnancy / Trade union / None]
**Compensation exposure:** [Uncapped (discrimination) / Capped (unfair dismissal) — estimated range]

### [Australia — if applicable]

**Unfair dismissal eligibility:** [Qualifying period met: Yes / No / Small business]
**High income threshold:** [Above / Below — note: general protections not income-limited]
**General protections risk (Part 3-1 reverse onus):** [Workplace right exercised: Yes / No]
**s. 387 analysis:** [Valid reason / Procedural fairness status]
**Application deadline:** 21 calendar days from termination date

---

## PART 5: CONFIDENCE ASSESSMENT

| Risk Area                      | Level       | Confidence  | Rationale       |
| ------------------------------ | ----------- | ----------- | --------------- |
| Temporal proximity presumption | [Level]     | [Score]     | [Basis]         |
| Retaliation indicator strength | [Level]     | [Score]     | [Basis]         |
| Comparator adequacy            | [Level]     | [Score]     | [Basis]         |
| Statutory compliance           | [Level]     | [Score]     | [Basis]         |
| **Overall**                    | **[Level]** | **[Score]** | **[Rationale]** |

---

## PART 6: MITIGATION PLAN

**Applicable Tier(s):** [1 / 1+2 / 1+2+3 based on score]

### Tier 1 — Non-Negotiable (required before proceeding)

1. [Specific, concrete step — not generic]
2. [...]

### Tier 2 — Strongly Recommended (for YELLOW and above)

1. [Specific step]
2. [...]

### Tier 3 — Alternative Actions (for RED and CRITICAL scores)

| Option        | Description   | Risk Reduction             |
| ------------- | ------------- | -------------------------- |
| [Alternative] | [Description] | [Score reduction estimate] |

---

## PART 7: GLASS BOX AUDIT TRAIL

```yaml
glass_box:
  skill_name: "legalcode-termination-risk-assessment"
  assessment_date: "[DATE]"
  employee_identifier: "[ID or descriptor]"
  jurisdiction_primary: "[State / UK / Australia]"
  jurisdictions_assessed: ["[J1]", "[J2]"]
  termination_reason: "[Stated reason]"
  termination_type: "[Individual / Group RIF — N employees]"
  composite_risk_score: "[X]/100"
  score_confidence_interval: "[X-CI]–[X+CI]"
  risk_classification: "[GREEN / YELLOW-LIGHT / YELLOW / RED-LIGHT / RED / CRITICAL]"
  recommendation: "[GO / GO-WITH-CAUTION / GO-WITH-CONDITIONS / NO-GO / RESTRUCTURE]"
  confidence_overall: "[HIGH / MEDIUM / LOW]"
  protected_activity_detected: "[Yes / No]"
  protected_activity_types:
    ["[FMLA / Workers Comp / Whistleblower / EEOC / NLRA / ADA / Other]"]
  most_recent_protected_activity_date: "[DATE or None]"
  temporal_proximity_days: "[X or None]"
  temporal_proximity_classification: "[STRONG / MODERATE / WEAK / NONE]"
  retaliation_indicators_count: "[N]"
  retaliation_indicator_score: "[X]/15"
  comparator_analysis_completed: "[Yes / No / Partial — gaps noted]"
  comparator_consistency: "[Consistent / Inconsistent — [N] adverse comparators]"
  documentation_quality: "[Comprehensive / Strong / Partial / Limited / None]"
  warn_act_applicable: "[Yes — [N] employees / No / Analysis pending]"
  final_pay_compliant: "[Yes / No — [State] gap identified / N/A]"
  pto_payout_compliant: "[Yes / No — [State] gap identified / N/A]"
  severance_offered: "[Yes — $[X] / No / TBD]"
  owbpa_required: "[Yes — employee 40+ / No]"
  legalcode_mcp: "[Connected — [N] citations VERIFIED / Not connected]"
  research_reference_file: "[Path or 'Not created']"
  self_interrogation_applied: "[Yes — [N] RED/CRITICAL categories reviewed / No]"
  citations_verified: "[N VERIFIED] / [N [VERIFY] marked]"
  mitigation_tier_recommended: "[Tier 1 / Tier 1+2 / Tier 1+2+3]"
  limitations:
    - "State employment law varies significantly; all statutory references require independent verification"
    - "Retaliation analysis is fact-intensive; additional facts from discovery may materially change this assessment"
    - "Comparator analysis is limited to information provided; undisclosed comparators may exist"
    - "[Any additional scope limitations or assumption statements]"
  reviewer: "AI-assisted — requires review by qualified employment counsel before action"
```
````

---

## PART 8: RECOMMENDED NEXT STEPS

1. [Specific next step — concrete and actionable]
2. [e.g., "Confirm final pay compliance with payroll team for [State] — immediate payment required"]
3. [e.g., "Engage employment counsel for independent review given [specific reason]"]
4. [e.g., "If termination proceeds, prepare OWBPA-compliant separation agreement — see legalcode-severance-agreement-review"]
5. [e.g., "Document decision rationale in writing before execution, including: decision-maker, date, reason, evidence reviewed, alternatives considered"]

```

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis via 2-agent research
pipeline. Agent 1 (Structural Analyst): analyzed legalcode-severance-agreement-review,
legalcode-independent-contractor-classification, and legalcode-employee-handbook-review;
extracted scoring framework architecture, tiered mitigation design, CLARIFY placement,
Glass Box YAML template, and output format template. Agent 2 (Legal Research Analyst):
conducted 8 targeted web research queries covering temporal proximity doctrine, at-will
employment exceptions, WARN Act requirements (federal + CA/NY/NJ/IL), final pay timing
by state, UK ERA 1996/ERA 2025/ACAS Code framework, and Australia Fair Work Act 2009
general protections and unfair dismissal. Primary legal authority [VERIFY all before
reliance]: Title VII § 704 (42 U.S.C. § 2000e-3(a)); ADEA § 623(d) (29 U.S.C. § 623(d));
ADA § 503 (42 U.S.C. § 12203); FMLA § 2615 (29 U.S.C. § 2615; 29 C.F.R. § 825.220);
NLRA § 8(a)(1)–(3) (29 U.S.C. § 158(a)); FLSA § 215(a)(3) (29 U.S.C. § 215(a)(3));
SOX § 806 (18 U.S.C. § 1514A); Dodd-Frank § 922 (15 U.S.C. § 78u-6); USERRA § 4311
(38 U.S.C. § 4311); ERISA § 510 (29 U.S.C. § 1140); *McDonnell Douglas Corp. v. Green*,
411 U.S. 792 (1973) (burden-shifting framework); UGESP 29 C.F.R. Part 1607 (four-fifths
rule); WARN Act 29 U.S.C. §§ 2101–2109 (20 C.F.R. Part 639); Mont. Code § 39-2-904
(WDEA good cause requirement); Cal. Lab. Code § 201 (immediate final pay); Cal. Lab.
Code § 227.3 (vacation as earned wages); CA WARN Health & Safety Code §§ 1400–1408;
NY Lab. Law § 860 (90-day notice); NJ WARN N.J. Stat. § 34:21-1 et seq. (mandatory
severance); ERA 1996 Part X ss. 94–134 (unfair dismissal); ACAS Code of Practice on
Disciplinary and Grievance Procedures; Equality Act 2010; PIDA 1998 (incorporated in
ERA 1996 ss. 43A-43L, 47B); Fair Work Act 2009 (Cth) ss. 340–365 (general protections),
385–405 (unfair dismissal), s. 361 (reverse onus). Novel contributions: 6-category
pre-termination risk scoring matrix with 0-100 composite scale and GO/NO-GO decision
bands; temporal proximity scoring table with circuit-agnostic day-range thresholds;
retaliation indicator registry with individual point weights; WARN Act four-jurisdiction
comparison table; final pay state quick reference integrated into scoring; reverse onus
explanation for Australian general protections; UK ERA 2025 qualifying period reform
noted; OWBPA/severance handoff to legalcode-severance-agreement-review; Tier 1/2/3
mitigation framework with alternative action table; 20 termination-specific anti-patterns;
full Glass Box YAML with termination-specific fields; output format template with 8-part
structure. All legal citations require independent verification before reliance.
```
