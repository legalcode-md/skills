---
name: legalcode-warn-act-analysis
description: Analyzes federal WARN Act (29 U.S.C. §§ 2101–2109) and state mini-WARN compliance for plant
  closings and mass layoffs. Use when assessing a proposed or completed reduction-in-force, plant closing,
  or business sale for WARN Act exposure; when calculating potential damages; when evaluating whether
  exceptions apply; or when determining which state mini-WARN statutes impose additional obligations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyzes federal WARN Act (29 U.S.C. §§ 2101–2109) and state mini-WARN compliance for plant closings and mass layoffs. Covers covered-employer determination, plant closing and mass layoff triggering thresholds, employment loss definitions, the 90-day rolling aggregation lookback, the three notice-reduction exceptions (faltering company, unforeseeable business circumstances, natural disaster), notice content and delivery requirements, damages calculation (back pay + ERISA benefits + $500/day civil penalty), the single-employer/affiliated-companies doctrine, sale-of-business allocation, WARN in bankruptcy, and remote-worker site-of-employment questions. Maps state mini-WARN variations for California, New York, New Jersey, Maine, Maryland, Minnesota, and Illinois. Use when assessing a proposed or completed reduction-in-force, plant closing, or business sale for WARN Act exposure; when calculating potential damages; when evaluating whether exceptions apply; or when determining which state mini-WARN statutes impose additional obligations.


# Legalcode WARN Act Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of federal and
> state WARN Act compliance. It does not constitute legal advice. All outputs must be
> reviewed by a qualified employment attorney licensed in the relevant jurisdiction(s)
> before use. WARN Act law is highly fact-intensive, subject to circuit-level splits, and
> evolves through DOL guidance and litigation — including unresolved questions on remote
> workers and post-2023 state amendments. Statutory and case law references cited here
> carry hallucination risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill analyzes federal WARN Act (29 U.S.C. §§ 2101–2109) and state mini-WARN
compliance for employers contemplating or executing plant closings, mass layoffs, and
business restructurings. It identifies compliance gaps, classifies their severity,
calculates potential damages exposure, and produces an actionable, auditable analysis
with remediation recommendations.

**Covers:**

- Covered-employer threshold analysis (100-employee rule, 4,000-hour-week alternative)
- Plant closing and mass layoff triggering event identification
- Employment loss definition (termination, 6-month layoff, 50%-hour reduction)
- 90-day rolling lookback aggregation calculation
- Three federal notice-reduction exceptions (faltering company, unforeseeable business
  circumstances, natural disaster)
- Statutory exemptions (temporary facilities, project-based work, strikes/lockouts)
- Notice timing, recipient, content, and delivery requirements under 20 CFR Part 639
- Damages calculation: back pay, ERISA benefits, $500/day civil penalty, attorney's fees
- Single employer / affiliated-companies five-factor doctrine
- Asset-sale vs. stock-sale WARN allocation between buyer and seller
- WARN Act in bankruptcy (§ 507(a)(4) priority wage claim analysis)
- Remote-worker single-site-of-employment analysis (unsettled law flagged)
- State mini-WARN comparison for CA, NY, NJ, ME, MD, MN, and IL

**Does not:**

- Provide legal advice or replace qualified employment counsel
- Cover non-US mass layoff notice requirements (EU Collective Redundancies Directive,
  UK collective consultation, etc.) — see jurisdiction-specific skills
- Analyze individual employee wrongful termination, discrimination, or severance claims
  outside the WARN Act framework

---

## Jurisdiction and Governing Law

This skill covers the US federal WARN Act and key state mini-WARN statutes:

| Law              | Statute / Regulation                                | Scope                                             |
| ---------------- | --------------------------------------------------- | ------------------------------------------------- |
| **Federal WARN** | 29 U.S.C. §§ 2101–2109; 20 CFR Part 639             | Baseline; applies nationwide                      |
| **California**   | Cal. Lab. Code §§ 1400–1408                         | 75-employee threshold; no UBC exception           |
| **New York**     | NY Lab. Law Art. 25-A, §§ 860–860-i                 | 50-employee threshold; 90-day notice              |
| **New Jersey**   | N.J.S.A. 34:21-1 et seq. (as amended Apr. 10, 2023) | 90-day notice; mandatory severance                |
| **Maine**        | ME Rev. Stat. Title 26, § 625-B                     | 90-day notice (closings); mandatory severance     |
| **Maryland**     | Md. Lab. & Emp. Code §§ 11-301 et seq.              | 50-employee threshold; 3-month window             |
| **Minnesota**    | Minn. Stat. §§ 116L.976–116L.979                    | Supplemental rapid-response reporting             |
| **Illinois**     | 820 ILCS 65                                         | Close federal mirror; state court right of action |

[JURISDICTION-SPECIFIC] Always confirm which state(s)' laws apply based on where the
affected employees work — not where the employer is headquartered or incorporated.
Multiple state mini-WARN statutes can apply simultaneously for multi-state RIFs.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context that changes the analysis, the workflow pauses and asks when:

- The answer would alter employer-threshold or trigger-threshold calculations
- Multiple valid exception arguments exist and their relative strength is unclear
- Sale-of-business facts determine whether buyer or seller bears notice obligation
- State mini-WARN layering is complex and the scope of the analysis should be defined

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

### Step 1: Accept the Input

Accept input in any of these formats:

- **RIF plan or term sheet**: Document describing the planned reduction, affected
  positions, site(s), and timing
- **WARN notice already issued**: Draft or executed notice for review
- **Free-text description**: User description of the planned action
- **Transaction documents**: Asset purchase agreement, merger agreement, or board
  resolution relevant to a business sale or restructuring

If input is insufficient to begin the analysis, prompt the user for the minimum facts:
employer size, affected-employee count per site, action type, and planned timing.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask:

1. **Action type**: What is the employer planning?
   - Options: Plant closing (permanent shutdown), Plant closing (temporary shutdown),
     Mass layoff (no shutdown), Business sale (asset deal), Business sale (stock deal /
     merger), Combination of the above, Not yet determined
   - _Why this matters_: The faltering company exception applies only to plant closings.
     Asset vs. stock sale determines which party bears the notice obligation.

2. **Workforce size**: How many employees does the employer have nationwide?
   - Options: Under 100, 100–499, 500–999, 1,000+, Unknown
   - _Why this matters_: Determines whether the employer is covered by federal WARN at
     all. If under 100, federal WARN does not apply (though state mini-WARN may still).

3. **Affected sites and states**: In which states and at which sites will employment
   losses occur?
   - Free text. Include city/state, number of employees affected per site.
   - _Why this matters_: Determines which state mini-WARN statutes layer on top of
     federal obligations. CA, NY, NJ, ME, and MD have materially stricter rules.

4. **Proposed timing**: When does the employer plan to order the first employment loss?
   - Options: Within 30 days, 30–60 days, 60–90 days, More than 90 days, Already
     occurred (retroactive analysis), Unknown
   - _Why this matters_: Determines whether 60-day federal notice is still achievable,
     whether an exception is being invoked, and whether liability has already accrued.

5. **Exception being considered**: Is the employer considering a notice-reduction exception?
   - Options: Faltering company (plant closings only), Unforeseeable business
     circumstances, Natural disaster, No exception — full 60-day notice will be given,
     Unsure — advise
   - _Why this matters_: Each exception has distinct legal elements and the burden of
     proof is on the employer. Analysis depth differs based on which exception applies.

6. **Union representation**: Are any affected employees represented by a union?
   - Options: Yes (all), Yes (some — specify which bargaining units), No, Unknown
   - _Why this matters_: Notice to the chief elected officer of the union is required
     instead of individual notice for represented employees.

If the user provides partial context, proceed with what is available and **state all
assumptions explicitly**. Do not silently assume facts that change the analysis.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to build a working legal reference for this analysis.

Search for:

- Federal WARN Act statute text: 29 U.S.C. §§ 2101–2109
- DOL implementing regulations: 20 CFR Part 639 (especially §§ 639.3, 639.5, 639.7,
  639.9)
- State mini-WARN statutes for each affected state identified in Step 2
- Recent case law on: single-site-of-employment for remote workers; single-employer
  doctrine in PE-backed companies; post-COVID unforeseeable business circumstances cases
- WARN Act in bankruptcy: 11 U.S.C. § 507(a)(4) priority cap (current dollar amount)

Save verified citations to `/tmp/legalcode-warn-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all citations [VERIFY] throughout the analysis
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using the legal framework below, but flag that citations are unverified

### Step 4: Establish Employer Coverage

**Threshold Analysis — 29 U.S.C. § 2101(a)(1); 20 CFR § 639.3(a)**

Determine whether the employer is a "covered employer" under federal WARN. The employer
must meet either test on the date notice is required (or would have been required):

| Test                    | Threshold                                          | How to Count                                                        |
| ----------------------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| **Full-time headcount** | ≥ 100 full-time employees                          | Exclude part-time (< 20 hrs/week or < 6 of last 12 months employed) |
| **Aggregate hours**     | ≥ 4,000 hours/week (all employees, excl. overtime) | Include part-time employees' actual hours; exclude overtime         |

**Who counts as an employee:**

- All full-time employees at any site nationwide (not just the affected site)
- Workers on temporary layoff or approved leave with a reasonable expectation of recall
- Non-profit organization employees (if threshold met)

**Who does NOT count:**

- Part-time employees (for threshold test only)
- Independent contractors with their own employment relationships
- Federal, state, and local government employees (as to governmental functions)
- Workers supplied by staffing agencies (counted against the agency, not the client)

**Single Employer / Affiliated Companies — 20 CFR § 639.3(a)(2)**

Related entities may be aggregated as a single employer under a five-factor test. Apply
when the employer is a subsidiary, division, or portfolio company:

| Factor                           | What to Assess                                         |
| -------------------------------- | ------------------------------------------------------ |
| **Common ownership**             | Shared equity ownership, parent-subsidiary structures  |
| **Common directors/officers**    | Overlapping boards, dual roles of senior management    |
| **De facto exercise of control** | Actual operational authority over day-to-day decisions |
| **Unity of personnel policies**  | Centralized HR, shared hiring/firing authority         |
| **Dependency of operations**     | Shared facilities, services, financial integration     |

> No single factor is determinative. Courts weigh all five together. PE fund sponsors
> face increasing litigation risk on the "de facto control" factor when they exercise
> operational influence beyond normal investment oversight.

**⟁ CLARIFY** — If the employer is a subsidiary or PE-backed portfolio company:

- "Is the parent / PE sponsor involved in the affected entity's day-to-day personnel
  decisions, or does the portfolio company operate independently? This determines whether
  the parent's employee count is aggregated for WARN threshold purposes."

**State mini-WARN thresholds** (check all affected states):

| State      | Employer Threshold                 | Employee Counting Notes                      |
| ---------- | ---------------------------------- | -------------------------------------------- |
| Federal    | 100 FT employees                   | Excludes part-time (< 20 hrs/wk or < 6 mo.)  |
| California | 75 employees (12-mo. lookback)     | Includes all employees at the establishment  |
| New York   | 50 FT employees                    | Follows federal part-time exclusion          |
| New Jersey | 100 employees (12-mo. lookback)    | Broad employee definition                    |
| Maine      | 100 employees (12-mo. lookback)    | Follows federal generally                    |
| Maryland   | 50 employees                       | Excludes < 20 hrs/wk and < 6 months employed |
| Minnesota  | Follows federal                    | Supplemental reporting only                  |
| Illinois   | ~75–100 (generally tracks federal) | State court private right of action          |

### Step 5: Identify Triggering Events and Apply 90-Day Aggregation

**5a. Employment Loss Definition — 29 U.S.C. § 2101(a)(6); 20 CFR § 639.3(f)**

An "employment loss" occurs when an employee experiences any of:

| Type                    | Definition                                                                         | Notes                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Termination**         | Any termination other than discharge for cause, voluntary departure, or retirement | Most common trigger                                                        |
| **Layoff > 6 months**   | A layoff lasting or expected to last more than 6 months                            | A temporary layoff that extends beyond 6 months becomes an employment loss |
| **50%+ hour reduction** | Reduction in hours of more than 50% in each month of any 6-month period            | Rare but can trigger WARN without formal termination                       |

**What is NOT an employment loss:**

- Discharge for cause (documented and genuine)
- Voluntary resignation or retirement
- Transfer accepted within 30 days: offer of a position at any other site (regardless
  of distance) or at a site within reasonable commuting distance (with ≤ 6-month break)

**5b. Plant Closing — 29 U.S.C. § 2101(a)(2); 20 CFR § 639.3(b)**

A permanent or temporary shutdown of a **single site of employment**, or one or more
facilities/operating units within a single site, resulting in employment loss for:

- **≥ 50 employees** (excluding part-time) **within any 30-day period**

> A shutdown that retains only a skeleton crew still qualifies as a plant closing if the
> effective cessation of the unit's production or work occurs.

**5c. Mass Layoff — 29 U.S.C. § 2101(a)(3); 20 CFR § 639.3(c)**

A reduction-in-force (not a plant closing) resulting in employment loss at a single site
during any 30-day period for:

| Test                     | Threshold                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **Large-count**          | ≥ 500 employees (excluding part-time)                                              |
| **Percentage + minimum** | ≥ 50 employees AND ≥ 33% of the active workforce at the site (excluding part-time) |

**5d. Single Site of Employment — 20 CFR § 639.3(i)**

The "single site of employment" is the operative geographic unit for threshold counting.
For most employers this is a building or campus. Key issues:

- **Geographically dispersed workers** (e.g., construction, trucking): A single site
  requires (1) reasonable geographic proximity, (2) same purpose, and (3) shared staff
  and equipment — per _Meadows v. Latshaw Drilling_ (N.D. Tex.). Sites hundreds of miles
  apart are separate sites.
- **Remote workers** [UNCERTAIN]: Whether a remote employee's home is a separate
  "single site" from the employer's office is unresolved. DOL regulations predate
  widespread remote work. Courts have not uniformly addressed this. [VERIFY current
  circuit split before advising on remote-heavy RIFs.]
- **Headquarters employees assigned to other sites**: May be aggregated into the site
  where they primarily work.

**5e. 90-Day Aggregation Rule — 29 U.S.C. § 2102(d); 20 CFR § 639.5**

Employment losses at a single site within any **90-day period** are aggregated and
counted together for threshold purposes — even if individual waves would not independently
trigger WARN — **unless** the employer demonstrates the losses resulted from **separate
and distinct actions and causes** (not an attempt to evade WARN).

**Aggregation calculation methodology:**

1. Identify the proposed layoff date (Day 0)
2. Look back 90 calendar days: count all employment losses from Day −90 to Day −1
3. Look forward 90 calendar days: count all anticipated losses from Day +1 to Day +90
4. Add the lookback count + proposed losses + forward count
5. If aggregate ≥ 50 employees AND ≥ 33% of active workforce, OR ≥ 500 employees →
   WARN threshold met
6. Re-run if the employer changes the planned dates (each new date creates a new window)

> **Example:** An employer lays off 20 employees in Month 1, 20 in Month 2, and 20 in
> Month 3 at the same site (300-employee workforce). Individually, no wave triggers WARN.
> Aggregated: 60 employees over 90 days = 20% of 300 — not a mass layoff. But if the
> workforce is 150: 60 ÷ 150 = 40% AND 60 ≥ 50 → **mass layoff triggered.**

**⟁ CLARIFY** — If the employer is planning phased layoffs:

- "Are the planned layoff waves driven by the same business cause (e.g., one decision to
  restructure), or are they truly independent decisions triggered by separate causes? If
  they share a common cause, aggregation is likely regardless of how they are phased."

**5f. State Mini-WARN Triggering Thresholds**

| State      | Plant Closing Trigger                    | Mass Layoff Trigger                     | Relocation Trigger                   |
| ---------- | ---------------------------------------- | --------------------------------------- | ------------------------------------ |
| Federal    | 50 FT in 30 days                         | 500 FT, OR 50 FT + 33% in 30 days       | Not covered                          |
| California | 50 employees, or cessation of operations | 50 employees in 30 days (no % required) | Removal 100+ miles                   |
| New York   | 25 FT in 30 days                         | 33% + 25 FT, OR 250 FT in 30 days       | Removal 50+ miles                    |
| New Jersey | 50 employees in 30 days                  | 500, OR 50 + 33% in 30 days             | Transfer of operations (no mileage)  |
| Maine      | 100 employees                            | 33% or 500+ lasting 6+ months           | Not separately defined               |
| Maryland   | 25% or 15 employees over 3 months        | Same                                    | Relocation reducing workforce 25%/15 |
| Minnesota  | Follows federal                          | Follows federal                         | Not separately defined               |

### Step 6: Evaluate Notice-Reduction Exceptions

When the employer cannot provide 60 days' advance notice, evaluate each applicable
exception. The **employer bears the burden of proof** on all exceptions. When an
exception applies, the employer must give "as much notice as is practicable" and must
include in the notice **a brief statement of the basis for reducing the notice period**.

**6a. Faltering Company Exception — 29 U.S.C. § 2102(b)(1); 20 CFR § 639.9(a)**

> **Applies ONLY to plant closings. Does NOT apply to mass layoffs.**
>
> **Does NOT apply under California mini-WARN.**

All four elements must be satisfied:

| Element                               | What to Show                                                                                                                            | Evidentiary Need                                                          |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Actively seeking capital/business** | Specific documented actions: loan applications, investor meetings, contract negotiations — not general business development             | Board minutes, lender correspondence, term sheets, investor presentations |
| **Realistic opportunity**             | Actual prospect of obtaining financing or business — not speculative hope                                                               | Lender letters of interest, credible investor commitments                 |
| **Sufficiency**                       | The capital or business, if obtained, would have avoided or postponed the shutdown for a reasonable time                                | Financial projections showing how funding would sustain operations        |
| **Good-faith belief**                 | Employer reasonably believed notice would preclude obtaining the capital or business (e.g., lender would withdraw if closure announced) | Documented lender condition or investor concern about public disclosure   |

**6b. Unforeseeable Business Circumstances — 29 U.S.C. § 2102(b)(2)(A); 20 CFR § 639.9(b)**

> **Applies to both plant closings and mass layoffs.**
>
> **Does NOT apply under California or New Jersey (post-April 2023) mini-WARN.**
>
> **Does NOT apply under New York mini-WARN for plant closings (faltering co. also absent).**

Closing or layoff must be caused by business circumstances **not reasonably foreseeable**
at the time 60-day notice would have been required:

- Standard: What a **similarly situated employer exercising commercially reasonable
  business judgment** would have foreseen at the notice deadline
- Employers are NOT required to predict general economic conditions
- Qualifying examples: sudden, unexpected cancellation of a major client contract with
  no warning; unanticipated strike by a supplier; dramatic and sudden government shutdown
  order issued without 60 days' advance notice

> **COVID-19 lesson**: Courts generally accepted that government-mandated closure
> orders (issued without 60 days' notice) could support this exception — but only if the
> employer lacked specific knowledge of the impending closure at the relevant triggering
> date. Generalized economic downturn from COVID-19 was NOT sufficient on its own.
>
> **Tech layoffs (2022–2023)**: Employers who argued that post-acquisition economic
> disruption was "unforeseeable" faced close scrutiny. The Twitter/X class action
> (_Cornet v. Twitter_, N.D. Cal. 2022–2024) settled for ~$2M after Twitter asserted
> this exception — a cautionary data point on litigation risk even with the exception.

**6c. Natural Disaster — 29 U.S.C. § 2102(b)(2)(B); 20 CFR § 639.9(c)**

> **Applies to both plant closings and mass layoffs.**
>
> **Does NOT apply under California mini-WARN (only exception is physical calamity or act of war — similar but verify).**

The closing or layoff must be a **direct result** of a natural disaster (flood,
earthquake, storm, drought, tsunami, or similar natural effect). Notice is still required
"whether in advance or after the fact."

**6d. Statutory Exemptions — 29 U.S.C. § 2103**

These actions are wholly exempt (no notice required):

| Exemption                                      | Requirements                                                                                                                                                                                                            |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Temporary facility / project-based work**    | Employer closes a temporary facility or lays off workers at project completion — AND affected employees were hired with the understanding that their employment was limited to the duration of that facility or project |
| **Strike / lockout**                           | Closing or layoff constitutes or results from a strike or an employer lockout **not intended to evade WARN**                                                                                                            |
| **Permanent replacement of economic strikers** | Narrowly construed; applies only when employer permanently replaces employees deemed economic strikers under the NLRA                                                                                                   |

> The **construction industry** frequently invokes the project-based work exemption.
> The key is that workers must have had advance understanding that employment was
> project-limited — not simply that they were employed on a project that ended.

### Step 7: Analyze Notice Requirements

**7a. Timing — 29 U.S.C. § 2102(a)**

The employer may not "order" a plant closing or mass layoff until the end of a **60-day
period** after serving written notice. "Order" means the decision that triggers employment
losses — not merely an internal discussion.

- 60 days is measured in **calendar days** (not business days)
- The 60-day clock begins when the **first affected employee** receives notice
- Notice must be served before employment losses begin, not before announcement to press

**State notice periods:**

| State      | Notice Period                                          | Notes                                       |
| ---------- | ------------------------------------------------------ | ------------------------------------------- |
| Federal    | 60 calendar days                                       | Baseline                                    |
| California | 60 calendar days                                       | Same period; fewer exceptions               |
| New York   | **90 calendar days**                                   | Most significant NY difference from federal |
| New Jersey | **90 calendar days**                                   | As amended April 10, 2023                   |
| Maine      | **90 calendar days** (closings); 7 days (mass layoffs) | Separate severance obligation               |
| Maryland   | 60 calendar days                                       |                                             |
| Minnesota  | Follows federal                                        | Supplemental reporting                      |
| Illinois   | 60 calendar days                                       |                                             |

> A multi-state RIF must satisfy the **longest applicable notice period** in each state
> where employment losses occur. NY and NJ require 90 days regardless of what federal
> law requires.

**7b. Recipients — 29 U.S.C. § 2102(a); 20 CFR § 639.6**

Four recipients must receive written notice:

| Recipient                          | Who                                                                                                | Notes                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Union**                          | Chief elected officer of each exclusive representative / bargaining agent                          | Individual employee notice not required for represented workers                        |
| **Affected employees (non-union)** | Each affected employee individually                                                                | Part-time employees also receive notice even though they don't count toward thresholds |
| **State dislocated worker unit**   | State rapid response unit (or Governor until designated)                                           | State-specific agency; varies by state                                                 |
| **Chief elected official**         | Top elected official of the municipality/political subdivision where the closing/layoff will occur | Chairperson for elected boards                                                         |

**7c. Required Content — 20 CFR § 639.7**

Content requirements differ by recipient. Notices may specify a 14-day window
(rather than a single date) for expected separations, as long as 60-day advance service
is still met.

**Notice to Union:**

- Site name/address and company contact person
- Whether action is permanent or temporary, and whether the entire plant will close
- Expected date of first separation and anticipated schedule for separations
- Job titles affected and names of workers in those positions

**Notice to Individual Affected Employees:**

- Whether action is permanent or temporary; whether the entire plant will close
- Expected date employment loss commences for that individual
- Whether bumping rights exist
- Company contact for further information

**Notice to State and Local Government:**

- Site name/address and company contact
- Whether action is permanent or temporary
- Expected date of first separation and schedule
- Job titles, number of affected employees per classification
- Whether bumping rights exist
- Names/addresses of union representatives (or statement no union exists)

**Note — SB 617 (California, eff. Jan. 1, 2026):** Cal/WARN notice must now also
include information about workforce board services, rapid response activities, CalFresh
food assistance details, and employer contact email/phone. [VERIFY SB 617 effective date
and content requirements against current Cal. Lab. Code § 1401 text.]

**7d. Delivery Methods — 20 CFR § 639.8**

Any reasonable method designed to ensure receipt at least 60 days before the first
separation:

- First-class mail
- Personal delivery with acknowledgment of receipt
- Insertion in pay envelope

> **Pre-printed boilerplate notices** routinely included in pay envelopes do NOT satisfy
> WARN — the notice must be specific to the particular closing or layoff event.

**⟁ CLARIFY** — If notice has already been served:

- "Please share the notice language. I will compare it against the 20 CFR § 639.7
  content requirements for each recipient category and identify any deficiencies."

### Step 8: Apply Sale-of-Business Rules

**8a. Asset Sale — 29 U.S.C. § 2101(b)(1); 20 CFR § 639.4(b)**

In an asset purchase transaction:

- The **seller** is responsible for WARN notice for any plant closing or mass layoff
  that occurs **on or before the date of the sale**
- The **buyer** is responsible for any plant closing or mass layoff that occurs **after
  the date of the sale**
- Both parties should confirm allocation in the purchase agreement

**8b. Stock Sale / Merger**

In a stock deal or statutory merger, the surviving entity assumes all WARN Act
obligations as a successor employer. No allocation is needed because the entity
(and its employment relationships) continues — the WARN obligation travels with the
workforce.

**⟁ CLARIFY** — For transactions:

- "Is this an asset deal (buyer acquires specific assets and selected employees transfer
  to a new entity) or a stock/merger deal (entire entity is acquired)? The answer
  determines which party is responsible for WARN notice for layoffs occurring around the
  closing date."

### Step 9: Calculate Damages Exposure

**9a. Federal Damages Formula — 29 U.S.C. § 2104**

For each affected employee for each day of violation (maximum 60 days):

```
Daily Rate = Higher of:
  (A) Average regular rate over last 3 years of employment, OR
  (B) Employee's final regular rate

ERISA Benefits = Value of health insurance, life insurance, pension
                 contributions, and other ERISA-covered benefits
                 that would have been provided during the violation period

Gross Liability per Employee = (Daily Rate × Days of Violation)
                              + ERISA Benefits Value

Net Liability per Employee = Gross Liability
  − Wages paid by employer during violation period (excl. accrued vacation)
  − Voluntary, unconditional payments by employer not legally required
  − Third-party payments made for benefits (e.g., COBRA premiums paid)
```

**9b. Civil Penalty — 29 U.S.C. § 2104(a)(3)**

Up to **$500 per day of violation** for failure to notify the chief elected official
of local government. **Maximum: $30,000** (60 days × $500). The penalty is avoided if
the employer pays all § 2104(a)(1) employee damages within **three weeks** of the plant
closing or layoff date.

**9c. Good Faith Defense — 29 U.S.C. § 2104(a)(4)**

Courts **may** reduce (not eliminate) employer liability if the employer demonstrates:

1. The act or omission was in good faith, AND
2. The employer had reasonable grounds for believing the act or omission was not a
   violation

This is a discretionary equitable reduction — courts are not required to reduce even on
a showing of good faith.

**9d. State Damages**

State mini-WARN violations generally track the federal back-pay + benefits formula,
measured against the state's notice period (up to 90 days for NY and NJ):

| State      | Key Difference                                                                                                                                  |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| California | Same formula; max 60 days; § 1402                                                                                                               |
| New York   | Same formula; max **90 days** (reflecting longer notice period)                                                                                 |
| New Jersey | **Mandatory severance**: 1 week/year of service (regardless of notice). Plus **4 weeks additional** if employer fails to provide 90-day notice. |
| Maine      | **Mandatory severance**: 1 week/year for employees with 3+ years of continuous service                                                          |
| Maryland   | Back pay + benefits; private right of action                                                                                                    |
| Minnesota  | Penalties not separately specified; federal as baseline                                                                                         |
| Illinois   | Tracks federal damages; state court right of action                                                                                             |

**9e. WARN Act in Bankruptcy — 11 U.S.C. § 507(a)(4)**

WARN Act backpay claims are priority wage claims entitled to fourth-priority treatment
(wages earned within 180 days before the bankruptcy petition filing date), capped at
approximately **$17,150 per employee** (as of 2025; adjusted every three years). [VERIFY
current cap.] Claims exceeding the cap or outside the 180-day window are general
unsecured claims. Bankruptcy does not excuse WARN compliance — trustees and
debtors-in-possession must provide notice when ordering qualifying closings or layoffs.

### Step 10: Classify Each Compliance Element

For each element analyzed, assign a classification and document findings using the
format in the Output Format Template below.

**Compliance Classification System:**

| Classification    | Definition                                                                                               | Required Action                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **COMPLIANT**     | Employer meets or exceeds the applicable WARN Act requirement; no remediation needed                     | Note for awareness; no action                       |
| **PARTIAL**       | Employer partially meets the requirement; a gap exists that increases litigation risk but may be curable | Flag for remediation; provide specific cure         |
| **NON-COMPLIANT** | Employer violates or would violate the applicable requirement; material exposure present                 | Immediate remediation required; escalate to counsel |

**Automatic NON-COMPLIANT Triggers**

Flag immediately as NON-COMPLIANT without further analysis:

| Trigger                                                                                     | Applicable Law       | Statutory Basis                       |
| ------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------- |
| No notice served where 50+ FT employees face plant-closing employment loss in 30 days       | Federal              | 29 U.S.C. § 2102(a)                   |
| No notice served where 500+ or (50+ + 33%) FT employees face mass-layoff employment losses  | Federal              | 29 U.S.C. § 2102(a)                   |
| Notice provided but timing is less than 60 calendar days with no documented exception basis | Federal              | 29 U.S.C. § 2102(a)                   |
| Notice served but omits required content items for any recipient category                   | Federal              | 20 CFR § 639.7                        |
| Pre-printed boilerplate notice used as the WARN notice                                      | Federal              | 20 CFR § 639.8                        |
| Faltering company exception claimed for a mass layoff (not a plant closing)                 | Federal              | 29 U.S.C. § 2102(b)(1)                |
| Unforeseeable business circumstances exception claimed under California mini-WARN           | California           | Cal. Lab. Code § 1401                 |
| Unforeseeable business circumstances exception claimed under post-April 2023 NJ WARN        | New Jersey           | N.J.S.A. 34:21-1 et seq.              |
| NY or NJ employer provides only 60-day (not 90-day) notice                                  | NY / NJ              | NY Lab. Law § 860-b; N.J.S.A. 34:21-2 |
| NJ employer fails to pay mandatory severance (1 wk/year) on a WARN-triggering event         | New Jersey           | N.J.S.A. 34:21-2 (as amended 2023)    |
| No notice to state dislocated worker unit                                                   | Federal / all states | 29 U.S.C. § 2102(a)(2)                |
| No notice to chief elected official of the affected municipality                            | Federal / all states | 29 U.S.C. § 2102(a)(2)                |
| Sale-of-business: seller fails to provide notice for pre-closing layoffs in asset deal      | Federal              | 29 U.S.C. § 2101(b)(1)                |

### Step 11: Apply Quality Frameworks

#### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivery if any
gate fails.

| Gate           | Rule                                                                                                                                            | Fail Action                       |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every legal claim cites a specific statute section, regulation provision, or established case holding                                           | Add citation or mark [UNVERIFIED] |
| **Format**     | All citations follow consistent format: statute name § number (short cite) or Case name, reporter cite (year)                                   | Fix format                        |
| **Currency**   | Every cited provision checked for amendments — especially NJ WARN (Apr. 2023), CA SB 617 (Jan. 2026), NY WARN amendments                        | Flag [CHECK CURRENCY]             |
| **Domain**     | Analysis stays within US federal and applicable state WARN Act scope; no inadvertent bleed into EU collective redundancy or UK consultation law | Remove or flag contamination      |
| **Confidence** | Uncertainty explicitly stated, especially on: remote-worker single site, post-2023 NJ severance formula, circuit splits                         | Add confidence qualifier          |

#### Self-Interrogation for NON-COMPLIANT Classifications

For every NON-COMPLIANT finding, apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the NON-COMPLIANT classification follow
logically from the cited statutory text and regulations? Would a federal district court
or state court actually reach this conclusion on these facts? Is the statutory text clear
or subject to reasonable interpretive ambiguity?

**Pass 2 — Completeness**: Have all applicable exceptions been evaluated? Is there a
natural disaster, unforeseeable business circumstances, or temporary-facility argument
the employer could raise? Has the 90-day aggregation been calculated correctly (both
lookback and forward)? Are all affected employees correctly identified?

**Pass 3 — Challenge**: What is the strongest argument that the employer IS compliant
or that the exposure is lower than assessed? Would the good faith defense apply? Is the
damages calculation conservative or aggressive? Could the notice be cured retroactively?

#### Confidence Scoring

Apply to each major finding:

| Level        | Range     | Meaning                                                       | Action                                              |
| ------------ | --------- | ------------------------------------------------------------- | --------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory text, settled DOL regulatory interpretation   | State without qualification                         |
| **High**     | 0.80–0.94 | Strong statutory basis, minor interpretive questions          | State with brief caveat                             |
| **Probable** | 0.60–0.79 | Good arguments; reasonable minds could differ; fact-intensive | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; circuit split or DOL silence             | Flag for qualified counsel review with both sides   |
| **Unlikely** | 0.0–0.39  | Weak statutory basis or speculative                           | Do not assert; flag [UNCERTAIN]                     |

> Apply "Possible" or "Unlikely" to:
>
> - Remote worker single-site analysis (unsettled)
> - Single-employer doctrine applied to PE fund (fact-intensive, circuit split)
> - Unforeseeable business circumstances in economic downturns (highly fact-specific)
> - Post-2023 NJ WARN severance formula application to multi-year employees

---

## Prioritization Framework

Tier findings to guide employer remediation sequencing:

**Tier 1 — Act Within 24 Hours**

- Employer has not served any notice and employment losses are imminent (≤ 30 days)
- Aggregation analysis reveals threshold already met from prior layoff waves
- NJ mandatory severance not paid on an already-completed WARN-triggering event
- Sale closing imminent with no buyer/seller WARN allocation in the APA

**Tier 2 — Cure Within Notice Period**

- Notice served but content is deficient for one or more recipient categories
- Exception basis documented but evidence is weak — strengthen now
- State mini-WARN notice not yet served (NY 90-day or NJ 90-day gap)
- Remote-worker site analysis not conducted — RIF may cross a threshold not yet identified

**Tier 3 — Document Before Proceeding**

- Exception reliance requires documentary support (board minutes, lender correspondence)
- Single-employer doctrine risk: document independent operation of subsidiary
- 90-day aggregation window: maintain a running log of employment losses at each site
- Part-time employee count: confirm exclusion methodology against § 2101(a)(8) definition

---

## State Mini-WARN Interaction Analysis

When employment losses occur in multiple states, layer each applicable state mini-WARN:

**Step A**: Identify all states where affected employees work.

**Step B**: For each state with a mini-WARN, determine:

- Does the employer meet the state's threshold?
- Does the layoff/closing meet the state's triggering thresholds?
- What notice period applies (60 vs. 90 days)?
- What exceptions are available (and which are unavailable)?
- Is there a mandatory severance obligation (NJ, ME)?
- Who are the required state notice recipients?

**Step C**: Use the **most restrictive applicable requirement** as the governing standard
for each jurisdiction. A 90-day notice state cannot be satisfied by federal 60-day notice.

**Step D**: For each affected state, draft separate notices if state-specific content
requirements differ from federal requirements.

[JURISDICTION-SPECIFIC] States without mini-WARN (TX, GA, TN, FL, AZ, MA) rely entirely
on federal WARN — confirm current state law before advising, as state legislatures
continue to enact new worker-protection statutes.

---

## Anti-Patterns

What NOT to do in WARN Act analysis and compliance planning:

1. **Counting only full-time employees at the affected site** — The covered-employer
   threshold counts all full-time employees at all sites nationwide. Employers with
   regional operations often fail this threshold only when they wrongly exclude employees
   at other locations. 29 U.S.C. § 2101(a)(1).

2. **Confusing the employer-threshold test with the triggering-event test** — The
   100-employee threshold determines coverage. The 50/500-employee (and 33%) thresholds
   determine whether a triggering event has occurred. These are separate tests with
   different counting rules and different timeframes.

3. **Treating a 6-month temporary layoff as exempt** — A temporary layoff expected to
   last more than 6 months (or that extends beyond 6 months after the fact) is an
   "employment loss" triggering WARN. Employers who extend temporary layoffs past the
   6-month mark retroactively create WARN exposure. 29 U.S.C. § 2101(a)(6)(B).

4. **Structuring phased layoffs to evade 90-day aggregation** — Deliberate sequencing
   of layoffs across multiple "waves" to avoid the 90-day window is specifically
   prohibited. DOL regulations and courts require employers to demonstrate separate and
   distinct causes for each wave — not just different dates. 29 U.S.C. § 2102(d).

5. **Claiming the faltering company exception for a mass layoff** — The faltering company
   exception applies **only** to plant closings. It is unavailable for mass layoffs. This
   is one of the most common WARN Act misapplications in restructuring contexts.
   29 U.S.C. § 2102(b)(1).

6. **Relying on unforeseeable business circumstances without documentation** — UBC is a
   defense, not an escape hatch. Employers must document, at the time notice would have
   been required, that a similarly situated employer exercising reasonable business
   judgment would not have foreseen the closing. Retrospective documentation is
   insufficient. 20 CFR § 639.9(b).

7. **Applying California's mini-WARN exceptions using federal law** — California's WARN
   Act does not recognize the faltering company exception or the unforeseeable business
   circumstances exception. Employers operating in California routinely discover this only
   after advising management they have a valid federal exception defense. Cal. Lab. Code
   § 1401.

8. **Using 60-day notice for New York or New Jersey operations** — NY requires 90 days'
   advance notice. NJ (since April 10, 2023) requires 90 days' advance notice. Providing
   the federal 60-day notice in these states is non-compliant and exposes the employer to
   30 additional days of damages. NY Lab. Law § 860-b; N.J.S.A. 34:21-2.

9. **Ignoring NJ mandatory severance** — New Jersey's post-2023 WARN Act requires
   mandatory severance of one week's pay per full year of employment on any WARN-
   triggering event — regardless of whether proper notice was given. Failure to pay this
   severance is a separate violation from the notice failure. N.J.S.A. 34:21-2.

10. **Treating all remote workers as employees of the HQ site** — Whether remote
    employees' homes constitute separate "single sites of employment" is an unresolved
    question. Employers who aggregate all remote workers into a single HQ site count may
    be overstating the threshold (which could be beneficial) or understating the count at
    a site (which could cause a missed trigger if the HQ itself crosses a threshold with
    the remote-worker addition). Both directions carry risk. [VERIFY current guidance.]

11. **Assuming buyer bears all WARN Act obligations in a business sale** — In asset
    sales, the seller is responsible for WARN notice for any employment losses occurring
    on or before the sale date. The parties can allocate this in the APA, but allocation
    between buyer and seller does not bind employees — both parties may be jointly
    exposed until notice is served. 29 U.S.C. § 2101(b)(1).

12. **Sending a single generic notice to all recipients** — WARN requires different
    content for union representatives, individual employees, and state/local government
    officials. A single generic notice almost certainly omits required elements for at
    least one recipient category. 20 CFR § 639.7.

13. **Treating bankruptcy as a WARN Act shield** — Bankruptcy does not excuse WARN
    compliance. WARN backpay claims are priority wage claims under § 507(a)(4) and
    liquidating trustees remain subject to WARN obligations. In re Jevic and subsequent
    bankruptcy-WARN cases establish that trustees can be personally liable. 11 U.S.C.
    § 507(a)(4).

14. **Assuming the construction exemption applies automatically** — The project-based
    work exemption requires that workers were **hired with the understanding** that
    employment was limited to the duration of the project — not just that the project
    ended. Employers who convert long-term construction employees to project-limited
    status at project completion do not qualify. 29 U.S.C. § 2103(1).

15. **Assuming the single-employer doctrine only applies to subsidiaries** — PE fund
    sponsors and controlling parent entities can be held liable as single employers when
    they exercise de facto control over the portfolio company's personnel decisions beyond
    normal investment oversight. Courts in multiple circuits have imposed liability on PE
    funds. 20 CFR § 639.3(a)(2).

16. **Using business days instead of calendar days for the 60-day clock** — WARN's
    60-day notice period is measured in calendar days. An employer who starts the clock
    on a Monday and plans the first layoff for "60 business days later" will be
    non-compliant by approximately two calendar months. 20 CFR § 639.5.

17. **Serving notice after the "order" to close rather than before** — The WARN Act
    requires notice before the employer "orders" the plant closing or mass layoff. The
    "order" is the decision that sets the employment loss in motion — not the public
    announcement. An employer who decides to close in a board meeting and then serves
    notice has already violated the Act. 29 U.S.C. § 2102(a).

---

## External Tool Integration

**With legalcode-mcp connected:**

- In Step 3, search for current text of 29 U.S.C. §§ 2101–2109 and 20 CFR Part 639
- Search for applicable state mini-WARN statutes for each affected state
- Search for recent cases: remote-worker single-site, PE single-employer doctrine,
  post-COVID unforeseeable business circumstances
- Confirm current § 507(a)(4) priority cap and adjustment date
- Save verified citations to `/tmp/legalcode-warn-authority.md`
- Mark all legalcode-mcp-verified citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with the legal framework in this skill, noting that all legal citations require
  independent verification against current authoritative sources

---

## Localization Notes

Federal WARN applies nationwide to covered employers, but every multi-state RIF requires
a state-by-state mini-WARN overlay:

1. **Determine each state where employment losses will occur** — not headquarters state
2. **Run the mini-WARN analysis for each state**: threshold, trigger, notice period,
   exceptions, mandatory severance
3. **Use the most restrictive applicable standard for each affected site/state**
4. **Monitor for new mini-WARN legislation** — state legislatures have actively expanded
   mini-WARN statutes (NJ 2023, CA SB 617 2026). Check for amendments since 2024.

[JURISDICTION-SPECIFIC] For countries outside the US, separate legal frameworks apply:

- EU: Collective Redundancies Directive (Directive 98/59/EC), implemented by each
  member state with significant national variations
- UK: Trade Union and Labour Relations (Consolidation) Act 1992, s. 188 (45-day or
  30-day notice for 100+ or 20–99 redundancies respectively)
- Canada: Provincial employment standards acts with varying thresholds and notice periods

Use jurisdiction-specific skills for non-US mass layoff notifications.

---

## Writing Standards

Before delivering any output under this skill:

- [ ] **Jurisdiction clarity**: Every finding identifies which statute (federal vs. state)
      applies. Never mix jurisdictions in a single analysis point without labeling.
- [ ] **Active voice**: "The employer must serve notice to the state dislocated worker
      unit" — not "Notice is required to be served."
- [ ] **Specific citations**: Include section numbers (§ 2102(b)(1)), CFR part/section
      (20 CFR § 639.9(b)), and case reporter citations with year.
- [ ] **No false certainty**: Mark [VERIFY] for unverified citations. Mark [UNCERTAIN]
      for genuinely unsettled legal questions (especially remote-worker single-site).
- [ ] **Actionable remediation**: Every NON-COMPLIANT or PARTIAL finding includes a
      specific action: draft the missing notice, obtain the documentation, confirm the
      employee count.
- [ ] **Proportionate depth**: Employer coverage and triggering event analysis are deep.
      Content-of-notice details are standard. Do not invert this.
- [ ] **Avoid overconfidence on exceptions**: The UBC and faltering company exceptions
      are defenses — not rights. Use language like "the employer may have a defense" rather
      than "the employer is exempt."

---

## Output Format Template

```markdown
# WARN Act Analysis — [Employer Name / RIF Name]

**Date of Analysis:** [Date]
**Analyst:** AI-assisted (requires qualified employment attorney review)
**Governing Law:** Federal WARN Act (29 U.S.C. §§ 2101–2109; 20 CFR Part 639)
[+ applicable state mini-WARN statutes]
**Sites Analyzed:** [Site name(s), city/state, employee count per site]
**Proposed Action:** [Plant closing / Mass layoff / Transaction]
**Proposed Timing:** [First employment loss date]

---

## Executive Summary

[2–3 paragraph overview: (1) employer coverage determination, (2) whether a triggering
event occurs and under which law, (3) top 3 compliance risks, and (4) overall exposure
estimate if the RIF proceeds as planned without remediation.]

**Overall Compliance Risk:** [HIGH / MEDIUM / LOW]

---

## Key Findings

| #   | Finding            | Classification | Priority | Statute |
| --- | ------------------ | -------------- | -------- | ------- |
| 1   | [One-line summary] | NON-COMPLIANT  | Tier 1   | [Cite]  |
| 2   | [One-line summary] | PARTIAL        | Tier 2   | [Cite]  |
| 3   | [One-line summary] | COMPLIANT      | —        | [Cite]  |

---

## Analysis

### 1. Employer Coverage

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Confidence:** [Level] ([score])

**Employees identified:** [Count at each site; nationwide total]
**Part-time exclusions applied:** [Count excluded; methodology]
**Single-employer analysis:** [Result of five-factor test if applicable]

**Finding:** [Does the employer meet the covered-employer threshold under federal WARN?
Under each applicable state mini-WARN?]

**Remediation (if PARTIAL or NON-COMPLIANT):** [Specific action]

---

### 2. Triggering Event Analysis

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Confidence:** [Level] ([score])

**Plant closing threshold:** [X employees / threshold: 50 FT in 30 days]
**Mass layoff threshold:** [X employees / Y% of Z-person workforce]
**90-day aggregation:** [Prior 90 days: X losses; Proposed: Y losses; Forward 90 days:
Z anticipated; Aggregate: W total — [above / below] threshold]

**Finding:** [Does a triggering event occur? Which type?]

**Remediation (if PARTIAL or NON-COMPLIANT):** [Specific action]

---

### 3. Notice Timing

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Confidence:** [Level] ([score])

**Required notice date:** [60 or 90 days before first employment loss]
**Actual notice date:** [Date notice was or will be served]
**Days of shortfall (if any):** [Number]
**Exception claimed:** [None / Faltering company / UBC / Natural disaster]
**Exception elements satisfied:** [Analysis of each element with evidence assessment]

**Finding:** [Is notice timing compliant?]

**Remediation (if PARTIAL or NON-COMPLIANT):** [Specific action]

---

### 4. Notice Content and Recipients

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Confidence:** [Level] ([score])

| Recipient                    | Notice Served? | Content Complete? | Deficiencies |
| ---------------------------- | -------------- | ----------------- | ------------ |
| Union (if applicable)        | [Yes/No]       | [Yes/Partial/No]  | [List]       |
| Individual employees         | [Yes/No]       | [Yes/Partial/No]  | [List]       |
| State dislocated worker unit | [Yes/No]       | [Yes/Partial/No]  | [List]       |
| Chief elected official       | [Yes/No]       | [Yes/Partial/No]  | [List]       |

**Finding:** [Summary of notice content compliance]

**Remediation (if PARTIAL or NON-COMPLIANT):** [Specific content additions needed]

---

### 5. State Mini-WARN Obligations

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT per state]
**Confidence:** [Level] ([score])

| State          | Mini-WARN Applies? | Notice Period      | Mandatory Severance?      | Compliance Status |
| -------------- | ------------------ | ------------------ | ------------------------- | ----------------- |
| California     | [Yes/No]           | 60 days            | No                        | [Status]          |
| New York       | [Yes/No]           | 90 days            | No                        | [Status]          |
| New Jersey     | [Yes/No]           | 90 days            | 1 wk/yr + 4-wk penalty    | [Status]          |
| Maine          | [Yes/No]           | 90 days (closings) | 1 wk/yr (3+ yr employees) | [Status]          |
| [Other states] |                    |                    |                           |                   |

**Finding:** [Summary of state mini-WARN compliance]

**Remediation (if PARTIAL or NON-COMPLIANT):** [Specific action per state]

---

### 6. Damages Exposure Estimate

**If employer proceeds without full compliance:**

| Component                              | Estimated Exposure                            |
| -------------------------------------- | --------------------------------------------- |
| Back pay (federal, max 60 days)        | $[X] ([Y employees × daily rate × Z days])    |
| ERISA benefits (federal)               | $[X]                                          |
| Civil penalty (federal, max $30,000)   | $[X]                                          |
| NY additional exposure (90-day period) | $[X]                                          |
| NJ mandatory severance                 | $[X] (1 wk × [Y employees] × avg. weekly pay) |
| NJ penalty for notice failure (4 wks)  | $[X]                                          |
| Attorney's fees (estimate)             | $[X]                                          |
| **Total exposure estimate**            | **$[X]**                                      |

_Note: This is a directional estimate. Actual damages depend on individual employee
wages, benefits values, and the number of days of violation. Consult employment counsel
for a precise damages calculation._

---

## Prioritization

### Tier 1 — Act Within 24 Hours

[List findings and specific actions]

### Tier 2 — Cure Within Notice Period

[List findings and specific actions]

### Tier 3 — Document Before Proceeding

[List findings and specific actions]

---

## Glass Box Audit Trail

\`\`\`yaml
glass_box:
skill_name: "legalcode-warn-act-analysis"
mode: "WARN Act compliance analysis"
jurisdiction: "[Federal + state(s) analyzed]"
employer_name: "[Name or 'Not disclosed']"
sites_analyzed: "[Number and locations]"
action_type: "[Plant closing / Mass layoff / Transaction / Combination]"
employees_affected: "[Number]"
legalcode_mcp: "[Connected / Not connected]"
research_reference_file: "[/tmp/legalcode-warn-authority.md or 'Not created']"
topics_analyzed: "[Number of analysis sections completed]"
compliant_findings: "[Count]"
partial_findings: "[Count]"
non_compliant_findings: "[Count]"
automatic_triggers_hit: "[Count]"
exceptions_evaluated: "[List: faltering company / UBC / natural disaster / none]"
state_mini_warn_states: "[List of states analyzed]"
citations_verified: "[Number VERIFIED] / [Number UNVERIFIED / VERIFY-flagged]"
damages_estimate: "[$X total directional estimate]"
confidence: "[HIGH / MEDIUM / LOW — rationale]"
limitations: - "Remote-worker single-site analysis is an unresolved area of law — flagged as UNCERTAIN" - "NJ WARN 2023 amendments (mandatory severance formula) should be verified against current N.J.S.A. 34:21-1 text" - "CA SB 617 (effective Jan. 1, 2026) notice content requirements should be verified" - "Bankruptcy § 507(a)(4) cap should be verified against current dollar amount" - "[Any other scope limitations specific to this analysis]"
reviewer: "AI-assisted — requires qualified employment attorney review before reliance"
\`\`\`
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A (create from scratch)
skill creation workflow. Legal research basis: comprehensive analysis of 29 U.S.C.
§§ 2101–2109; 20 CFR Part 639 (DOL regulations); Cal. Lab. Code §§ 1400–1408 (including
SB 617 effective Jan. 1, 2026); NY Lab. Law Art. 25-A §§ 860–860-i; N.J.S.A. 34:21-1
et seq. (as amended P.L. 2020, c.3, effective April 10, 2023 mandatory severance and
90-day notice); ME Rev. Stat. Title 26, § 625-B; Md. Lab. & Emp. Code §§ 11-301 et seq.;
Minn. Stat. §§ 116L.976–116L.979; 820 ILCS 65; 11 U.S.C. § 507(a)(4) (bankruptcy
priority). Case law reference: Meadows v. Latshaw Drilling (single-site dispersed
worksites); Cornet v. Twitter (N.D. Cal. 2022–2024) (UBC exception in mass tech layoffs);
In re Jevic Holding Corp. (bankruptcy-WARN intersection); COVID-19 era UBC cases (2020–
2022). Structural framework: 2-agent research pipeline calibrated against legalcode-
contract-review and legalcode-collective-bargaining-review reference standards.
All citations carry [VERIFY] risk and should be confirmed against authoritative sources
before legal reliance.
