---
name: legalcode-us-state-non-compete-analysis
description: Analyze non-compete agreement enforceability across all 50 US states. Use when reviewing
  a non-compete clause, covenant not to compete, restrictive covenant, post-employment restriction, or
  garden leave agreement — whether for an employer, employee, in-house counsel, or transactional attorney.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze non-compete agreement enforceability across all 50 US states. Use when reviewing a non-compete clause, covenant not to compete, restrictive covenant, post-employment restriction, or garden leave agreement — whether for an employer, employee, in-house counsel, or transactional attorney. Covers: 6-state total ban screening (California, Minnesota, North Dakota, Oklahoma, Montana, Wyoming), salary threshold screening for 12+ states, reasonableness factor analysis (geographic scope, duration, scope of activity, legitimate business interest), consideration requirements (at-hire vs. mid-employment), blue-pencil vs. red-pencil reformation doctrine, garden leave mechanics and salary requirements, choice-of-law enforceability (California SB 699 extraterritorial reach, DraftKings v. Hermalyn analysis), FTC rulemaking status post-Ryan LLC v. FTC vacatur (September 2025 accession), Florida CHOICE Act 2025, healthcare and physician-specific restrictions, and state legislative trends 2023–2026. Jurisdiction-specific for United States (all 50 states + DC). Supports both employer (drafting/enforcement) and employee (challenge/negotiation) perspectives.


# Legalcode US State Non-Compete Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of non-compete
> agreement enforceability under US state law. It does not constitute legal advice. All
> outputs should be reviewed by a qualified employment attorney licensed in the relevant
> state(s) before reliance. Non-compete law changes rapidly — statutes cited here reflect
> research through early 2026 but may have been amended. Salary thresholds adjust annually;
> verify current figures before relying on them. Statutory and case law references carry
> hallucination risk — verify against authoritative sources (state statutes, Westlaw,
> Lexis) before use.

---

## Purpose and Scope

This skill analyzes whether a non-compete agreement or clause is enforceable under US
state law — and if not, what can be done about it. It applies to post-employment
non-competition restrictions in employment contracts, standalone non-compete agreements,
restrictive covenant agreements, and garden leave provisions.

**Covers:**

- Total-ban and near-ban state screening (6 states with statutory bans + DC)
- Salary threshold compliance (12+ states with income-floor requirements)
- Reasonableness analysis: legitimate business interest, geographic scope, duration,
  scope of restricted activities
- Consideration requirements: at-hire vs. mid-employment execution
- Blue-pencil vs. red-pencil reformation doctrine by state
- Garden leave provisions: requirements, mechanics, and enforceability impact
- Choice-of-law analysis: California's extraterritorial reach (SB 699/AB 1076),
  Restatement (Second) of Conflicts § 187 analysis
- FTC regulatory landscape: Ryan LLC v. FTC (N.D. Tex. Aug. 20, 2024) vacatur,
  FTC's September 2025 accession, current Section 5 case-by-case enforcement posture
- Florida CHOICE Act (eff. July 1, 2025) enhanced enforcement regime
- Healthcare and physician-specific restrictions (16+ states)
- State legislative trends 2023–2026
- Practical drafting fixes and negotiation recommendations

**Does not:**

- Analyze non-solicitation-of-customers or non-solicitation-of-employees clauses in
  isolation (though it flags interactions with non-compete analysis)
- Provide advice under any jurisdiction outside the United States
- Constitute legal advice or replace qualified employment counsel
- Guarantee enforceability — a ENFORCEABLE classification reflects analysis, not
  a legal opinion

---

## Jurisdiction and Governing Law

This skill covers **United States — all 50 states, the District of Columbia, and US
territories** for employment non-compete enforceability. It is US-specific; do not use
for non-compete analysis under UK, EU, or other national law.

Non-compete law in the US is almost entirely **state law**. As of early 2026, there is
no federal statute governing post-employment non-competes (the FTC's April 2024 final
rule was vacated in August 2024 and the FTC formally acceded to vacatur in September 2025).
The FTC continues targeted Section 5 enforcement against coercive, overbroad agreements.

**Choice of law matters enormously**: The state law that governs a non-compete is not
always the state the agreement designates. California, in particular, applies its ban
extraterritorially via Cal. Bus. & Prof. Code § 16600.5 (eff. Jan. 1, 2024) regardless
of where the agreement was signed or which state's law is designated.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist (e.g., employer vs. employee perspective)
- Threshold questions require specific facts to resolve
- The applicable state(s) are ambiguous

Use the **⟁ CLARIFY** pattern wherever marked below. If the user has already provided
the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Non-Compete Provision

Accept the non-compete agreement or clause in any of these formats:

- **Full document**: Employment agreement, standalone restrictive covenant agreement,
  separation agreement, or offer letter — PDF, DOCX, or pasted text
- **Excerpt**: The non-compete clause(s) alone, pasted directly
- **Description**: A plain-language description of the restriction for a hypothetical
  or drafting review scenario

If no agreement text is provided, prompt the user to supply it before proceeding.

Extract and record the following information from the document (ask the user if missing):

- Restricted duration (in months/years)
- Geographic scope (counties, states, national, global, or customer-based)
- Scope of restricted activities (industry-wide, role-specific, named competitors)
- Governing law clause (which state's law the agreement designates)
- Consideration recital (what consideration is stated for the non-compete)
- Date of execution (when the agreement was signed)
- Employee's job title, role, and compensation level
- Whether the agreement was presented at hire or mid-employment

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before analyzing, gather this context. Present as structured questions:

1. **Which perspective are you analyzing from?**
   - Options: Employer (drafting, enforcement, or pre-hire review), Employee (challenge,
     negotiation, or pre-signing review), In-house counsel (compliance audit), Transactional
     (M&A — asset sale exception analysis), Other
   - _Why this matters_: The entire risk framing inverts. An employer needs to know what
     is likely enforceable; an employee needs to know what can be challenged.

2. **Which state(s) are involved?**
   - State where employee works / will work
   - State where employee resides
   - State designated in the governing law clause
   - State where employer is based (if different)
   - _Why this matters_: Multiple states may have a claim to govern; California's rule
     applies regardless of choice of law for employees working in California.

3. **What is the employee's annual compensation?**
   - Provide base salary figure (bonus structure if relevant)
   - _Why this matters_: 12+ states have salary thresholds that render non-competes
     void for sub-threshold earners. This can resolve the analysis immediately.

4. **Is the employee in a healthcare profession?**
   - Options: Physician/MD, Nurse/NP/PA, Dentist, Psychologist, Other healthcare,
     Not healthcare
   - _Why this matters_: 16+ states have healthcare-specific restrictions (geographic
     radius limits, duration caps, buyout rights). Florida, Texas, Maryland, Pennsylvania,
     and Indiana have enacted major healthcare non-compete restrictions since 2024.

5. **When was the agreement signed relative to employment start?**
   - Options: Before employment began (offer letter stage), On day one of employment,
     After employment began (mid-employment), Unknown
   - _Why this matters_: Pennsylvania, Illinois, Washington, and other states require
     independent consideration for mid-employment non-competes; timing determines
     whether the agreement may be void for lack of consideration.

If the user provides partial context, state your assumptions explicitly and proceed.

---

### Step 3: Threshold Screening — Ban and Near-Ban State Check

**This step may resolve the analysis immediately.** Before assessing reasonableness,
screen for total bans and salary threshold violations. These are threshold issues —
if a state's statutory ban applies, reasonableness analysis is irrelevant.

#### 3a. Total-Ban States (6 States — Non-Competes VOID by Statute)

| State            | Statute                                                                                   | Key Rule                                                                                                                                              | Exception                                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **California**   | Cal. Bus. & Prof. Code §§ 16600–16600.5 (as amended by SB 699/AB 1076, eff. Jan. 1, 2024) | Non-competes void AND **unlawful** regardless of where/when signed; employer SHALL NOT attempt to enforce; private right of action with attorney fees | Sale of a business (§ 16601); dissolution of a partnership (§ 16602); dissolution/sale of an LLC (§ 16602.5) |
| **Minnesota**    | Minn. Stat. § 181.988 (eff. July 1, 2023)                                                 | All post-employment non-competes void for both employees and independent contractors                                                                  | Sale/dissolution of a business; agreements signed BEFORE July 1, 2023 remain valid if otherwise reasonable   |
| **North Dakota** | N.D. Cent. Code § 9-08-06                                                                 | Non-competes void and against public policy                                                                                                           | Sale of a business or dissolution of a partnership                                                           |
| **Oklahoma**     | Okla. Stat. tit. 15, § 219A                                                               | Non-competes void; courts apply red pencil (entire agreement void, no reform)                                                                         | Sale of a business goodwill                                                                                  |
| **Montana**      | Mont. Code Ann. § 28-2-703                                                                | Non-competes void                                                                                                                                     | Sale of a business                                                                                           |
| **Wyoming**      | (eff. July 1, 2025)                                                                       | Non-competes void upon termination of employment                                                                                                      | Sale of a business                                                                                           |

**If the employee works in, is a resident of, or will move to any of these states:**

- **California (SB 699)**: The ban applies regardless of the governing law clause.
  Cal. Bus. & Prof. Code § 16600.5 voids agreements "regardless of where and when the
  contract was signed." An employer SHALL NOT attempt to enforce a void agreement.
  Classify: **VOID — STATUTORY BAN (CA)**
- **Minnesota (post-July 1, 2023 agreements)**: Void. Classify: **VOID — STATUTORY BAN (MN)**
- **North Dakota, Oklahoma, Montana, Wyoming**: Apply void classification without
  reasonableness analysis. Classify: **VOID — STATUTORY BAN ([state])**

**⟁ CLARIFY** — If the employee currently resides in a non-ban state but the non-compete
restricts activity in California or would require the employee to relocate to California:

> California courts have applied § 16600 to prevent enforcement of non-competes that would
> affect California employees even when the employee hasn't yet moved. Do you want me to
> analyze both the current-state position AND the California position?

#### 3b. Salary Threshold States

If none of the 6 total-ban states apply, screen for salary thresholds. A non-compete is
**void by operation of law** for employees earning below the applicable threshold:

| State             | 2025 Non-Compete Threshold                         | 2025 Non-Solicitation Threshold   | Authority                                                                                 |
| ----------------- | -------------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Colorado**      | $127,091/year                                      | $76,255/year                      | Colo. Rev. Stat. § 8-2-113(2)(b) (2022 amendment; adjusts annually)                       |
| **D.C.**          | ~$162,164/year (highest nationally)                | Same                              | D.C. Non-Compete Clarification Amendment Act 2022                                         |
| **Illinois**      | $75,000/year                                       | $45,000/year                      | 820 ILCS §§ 90/1 et seq. (IFWA, eff. Jan. 1, 2022; $80K/$47K in 2027)                     |
| **Maine**         | ~$62,600/year                                      | N/A                               | Me. Rev. Stat. tit. 26 § 599-A                                                            |
| **Maryland**      | ~$46,800/year                                      | N/A                               | Md. Labor & Emp't § 3-716 (150% of state min. wage; healthcare: $350K separate threshold) |
| **Nevada**        | ~$3,869/month (FLSA overtime-eligible)             | N/A                               | Nev. Rev. Stat. § 613.195                                                                 |
| **New Hampshire** | FLSA overtime-eligible threshold                   | N/A                               | N.H. RSA § 275:70-a                                                                       |
| **Oregon**        | $116,427/year                                      | N/A                               | ORS § 653.295 (adjusts annually; 2026: ~$119,541)                                         |
| **Rhode Island**  | 250% of federal poverty level (~$38,000/year)      | N/A                               | R.I. Gen. Laws § 28-59-3                                                                  |
| **Virginia**      | $76,081/year                                       | N/A                               | Va. Code § 40.1-28.7:8 (adjusts annually; "low-wage employee" standard)                   |
| **Washington**    | $123,394/year (employees) / $308,485 (contractors) | $123,394 (current customers only) | RCW §§ 49.62.005–.900 (as amended by SB 5935, eff. June 6, 2024)                          |

> **Note**: Thresholds adjust annually. Verify current figures for the applicable year.
> Colorado's 2026 threshold is approximately $130,014.

**If the employee's compensation falls below the applicable state threshold:**

- Classify the provision: **VOID — BELOW SALARY THRESHOLD ([State])**
- Note: In states with tiered thresholds (Illinois, Washington), the non-solicit may
  still be valid even if the non-compete is void. Flag this separately.

**⟁ CLARIFY** — If the employee's compensation is within 10% of the applicable threshold:

> [State]'s threshold adjusts annually. Do you want me to analyze both a below-threshold
> (void) scenario and an above-threshold (enforceability analysis) scenario?

---

### Step 4: FTC and Federal Exposure Assessment

Even without a categorical rule, **assess FTC Section 5 exposure** for employer-side
analysis:

**Current federal landscape (as of early 2026):**

- The FTC's April 2024 Non-Compete Rule was vacated by the U.S. District Court for the
  Northern District of Texas on August 20, 2024 (_Ryan LLC v. FTC_, No. 3:24-cv-00986-E),
  and the FTC formally acceded to the vacatur on September 5, 2025. The rule is not in
  effect and is not enforceable.
- The FTC under Chair Andrew Ferguson (Trump appointee) has shifted to targeted Section 5
  enforcement against coercive, overbroad non-competes on a case-by-case basis.
- The FTC's **Joint Labor Task Force** (established February 26, 2025) actively
  investigates anticompetitive labor-market conduct.
- FTC warning letters (September 2025) targeted healthcare employers and staffing companies
  with overbroad nurse and physician non-competes.
- **Workforce Mobility Act** (S. 2031, reintroduced June 2025): Would create a federal
  statutory ban; has not advanced beyond committee as of early 2026.

**Section 5 Red Flags (elevated FTC scrutiny risk):**

- Non-competes applied to low-wage workers who clearly lack access to trade secrets
- Industry-wide restrictions in healthcare, nursing, or clinical staffing
- Non-competes combined with arbitration clauses and class-action waivers
- Agreements where the employer is a dominant market player in a local labor market
- Evidence of employer coordination with competitors on non-compete terms

**Classify FTC exposure as:**

- **LOW**: Agreement is narrowly tailored, high-earner, legitimate trade secret protection
- **MODERATE**: Agreement has some overbreadth; may attract scrutiny if challenged
- **HIGH**: Agreement is broad, low-wage worker, or healthcare sector; elevated enforcement risk

---

### Step 5: Reasonableness Factor Analysis

For states where the agreement is not void by statute (i.e., all states except those
classified in Step 3), apply the **Reasonableness Framework**. Courts across all
non-ban states use some version of this multi-factor test.

#### 5a. Legitimate Business Interest

Assess whether the employer has a recognized legitimate business interest:

| Interest                                      | Strength       | What Courts Look For                                                                                                                        |
| --------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Trade secrets / proprietary information**   | Very Strong    | Specific, identified categories of confidential information; employee had meaningful access; information is not publicly available          |
| **Substantial customer/client relationships** | Strong         | Employee had direct customer contact; employee could divert identifiable customers; customer list not publicly available                    |
| **Customer goodwill**                         | Moderate       | Employee is the "face" of the business to customers; geographic or industry goodwill tied to a specific trade name or location              |
| **Extraordinary/specialized training**        | Moderate       | Substantial investment in genuinely proprietary training (not general skills); months of training, not days; documented training investment |
| **General industry knowledge**                | NOT legitimate | Skills the employee brought to the job, general industry expertise, publicly available information                                          |
| **Replacement cost protection**               | NOT legitimate | In most states, the mere cost of replacing an employee is not a recognized legitimate interest                                              |

**Classify:**

- **Clearly established**: Specific trade secrets or identifiable customer relationships documented → supports enforcement
- **Arguable**: Some customer contact or confidential information access but unclear scope → AT-RISK
- **Absent or implausible**: No trade secrets, no meaningful customer contact, generic role → NON-COMPLIANT

**State-specific notes:**

- **Florida (§ 542.335)**: Employer must plead AND prove a legitimate business interest. Courts will not supply one.
- **Georgia (GRCA)**: Recognized interests codified at O.C.G.A. § 13-8-51 — any arguable interest from the statutory list shifts burden to employee.
- **Texas (§ 15.50)**: The non-compete must be "ancillary to or part of an otherwise enforceable agreement" under which the employer promises to provide trade secrets or special training. Circular non-competes with no consideration are void.
- **New York (common law)**: Courts additionally require that the employee possess "unique or extraordinary skills" OR has access to genuine trade secrets. Mere employment does not justify restriction.

#### 5b. Geographic Scope

| Scope                                                               | Generally Accepted       | Likely Overbroad                       |
| ------------------------------------------------------------------- | ------------------------ | -------------------------------------- |
| Specific counties or MSAs where employee worked                     | ✅                       | —                                      |
| States where employee had customer relationships                    | ✅                       | —                                      |
| Nationwide restriction for nationally-facing role                   | ✅ with documentation    | —                                      |
| Worldwide restriction for international employee                    | Possible if justified    | Likely overbroad for most employees    |
| "Anywhere the employer does business"                               | Risky                    | Overbroad if employer is multinational |
| Customer-defined territory ("anywhere I did business for employer") | ✅ Increasingly accepted | —                                      |

> **Georgia 2024 update**: The Georgia Supreme Court held (September 4, 2024) that a
> geographic restriction need not be expressed as a defined territory — it may be implied
> from the employee's customer contact scope — but must still be reasonable in totality.
> (_[VERIFY] — Georgia Supreme Court, Sept. 4, 2024_)

**⟁ CLARIFY** — If the agreement uses vague geographic language such as "anywhere the
Company has done business" or "any market in which the Company competes":

> The geographic scope is defined in terms that could be interpreted very broadly or
> very narrowly depending on the employer's business. What is the employer's approximate
> geographic footprint, and in which areas did the employee actually work with customers?

#### 5c. Duration

| Duration     | Classification                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------ |
| ≤ 6 months   | Presumptively reasonable in all non-ban states                                                               |
| 7–12 months  | Reasonable in most states; Massachusetts statutory maximum (MNAA)                                            |
| 13–18 months | Reasonable in most states; Washington presumptive maximum                                                    |
| 19–24 months | Outer limit in many states; Florida presumptive upper limit (base statute); Georgia presumptively reasonable |
| 25–36 months | Courts split; usually requires strong justification; AT-RISK in most states                                  |
| 37–48 months | Florida CHOICE Act (high earners only, eff. July 1, 2025); OTHERWISE generally unreasonable                  |
| > 48 months  | AT-RISK to NON-COMPLIANT in virtually all employment contexts; common in sale-of-business context only       |

#### 5d. Scope of Restricted Activities

The restriction must match the employee's actual role and the employer's actual competitive
interest. Classify:

- **ENFORCEABLE scope**: Restriction tied to the employee's actual duties and the employer's
  specific competitive arena (e.g., "software development for [specific product category]
  for direct competitors")
- **AT-RISK scope**: Some nexus to the role but broader than necessary (e.g., "any position
  at a company in the technology industry")
- **NON-COMPLIANT scope**: Restriction prevents the employee from practicing their profession
  entirely or working in any capacity for a competitor (e.g., "any position at any company
  competing with Employer in any market")

---

### Step 6: Consideration Analysis

Adequate consideration is a required element in every state. Analyze based on timing:

#### At-Hire Agreements

An offer of employment, if presented before the employee starts, constitutes adequate
consideration in virtually all states. The agreement must be presented:

- **Before the employee's first day** (most states)
- **At least 10 business days before start** — Massachusetts (MNAA requirement)
- **At least 14 days before start** — Colorado, Illinois (IFWA requirement)
- **At least 2 weeks before start** — Oregon (ORS § 653.295 requirement)
- **At time of hire or at least 14 days before signing** — Washington (RCW § 49.62.020)

**⟁ CLARIFY** — If the agreement was presented "at hire" but the exact timing is unclear:

> Do you know approximately when (relative to the employee's first day) the non-compete
> was presented for signature? In some states (Massachusetts, Colorado, Illinois, Oregon,
> Washington), a specific advance notice period is required for enforceability.

#### Mid-Employment Agreements

**Continued employment alone is NOT sufficient consideration in these states:**

- **Pennsylvania**: Agreement must be signed at or before employment commencement; mid-term
  agreements require independent consideration. [VERIFY against current PA case law]
- **Washington**: Explicit statutory requirement — employer must provide a promotion, pay
  raise, bonus, fixed term of employment, or access to confidential information.
- **Illinois**: Employee must work at least 2 years after signing, OR receive additional
  professional or financial benefits beyond continued employment.
- **Oregon**: New or different consideration required (promotion, raise, bonus, or access
  to protected information).
- **North Carolina**: Many courts hold continued employment insufficient for mid-term
  non-competes. [VERIFY]
- **Montana, South Carolina**: Continued employment generally insufficient. [VERIFY]

**Continued employment IS generally sufficient consideration in:**

- **Florida**: Employer's promise of continued employment is expressly recognized as
  sufficient under § 542.335 and in Florida case law.
- **Georgia**: Continued employment recognized as consideration under O.C.G.A. § 13-8-53.
- Most at-will employment states (unless specific statute provides otherwise).

**Classify:**

- **VALID CONSIDERATION**: Agreement signed at or before hire; OR independent consideration
  provided for mid-employment agreement in states that require it
- **CONSIDERATION AT-RISK**: Mid-employment agreement; state rules on continued employment
  are ambiguous or require investigation
- **INVALID CONSIDERATION**: Mid-employment agreement in a state where continued employment
  is clearly insufficient; no additional consideration documented

---

### Step 7: Blue Pencil / Red Pencil Doctrine Analysis

The reformation doctrine determines whether a court will **modify** or **void entirely**
an overbroad non-compete. This is critical for drafting strategy.

#### Red Pencil (Void) States — Overbroad = Entire Agreement Void

Courts in these states will NOT reform an overbroad agreement. If any material restriction
is unreasonable, the entire covenant is void:

- **California, Minnesota, North Dakota, Oklahoma, Montana, Wyoming** (entire agreement
  void — these are already the ban states)
- **Nebraska**: Courts apply red pencil approach to void overbroad agreements
- **Wisconsin**: Strong tendency toward voiding rather than reforming
- **Virginia**: Traditionally applies red pencil; some recent courts exercise limited reform
- **Delaware** (emerging): Delaware Supreme Court in _Sunder Energy, LLC v. Tyler Jackson_
  (Dec. 10, 2024) refused to reform a patently overbroad non-compete; signals move away
  from automatic blue-pencil reform in Delaware

**Drafting implication**: In red-pencil states, the employer MUST draft narrowly and
precisely. An overbroad provision kills the entire agreement.

#### Mandatory Reformation (Blue Pencil Plus) States — Courts MUST Reform

Courts in these states MUST reform overbroad covenants to reasonable scope; they cannot
void the entire agreement:

- **Florida** (§ 542.335): "A court shall modify and grant only the relief reasonably
  necessary to protect such interests."
- **Texas** (Tex. Bus. & Com. Code § 15.52): "A court shall reform the covenant to the
  extent necessary to cause the limitations contained in the covenant as to time,
  geographical area, and scope of activity to be restrained to be reasonable."
- **Idaho** (§ 44-2704): Mandatory reform.

**Drafting implication**: In FL and TX, employers can draft somewhat broadly and courts
will trim to a reasonable scope. However, this is not a license for gross overbreadth —
courts will reform down but cannot add obligations the employer failed to include.

#### Discretionary Reformation States (Majority)

Courts in most other states MAY reform overbroad covenants but are not required to. Most
do so rather than voiding entirely, but outcomes are unpredictable:

New York, Massachusetts, Georgia, Colorado, Connecticut, Delaware (pre-2024 approach),
Illinois, Iowa, Kansas, Kentucky, Maine, Michigan, New Jersey, Ohio (some courts), Oregon,
Pennsylvania, Tennessee, Vermont, Washington, West Virginia, and most others.

**Classify the agreement's reformation posture:**

- **Reform-favorable (FL, TX, ID)**: Courts will fix overbreadth; employer may still enforce
  a narrowed version
- **Reform-possible (most states)**: Court may reform but outcome uncertain; risk of void
- **Reform-hostile (CA, MN, ND, OK, MT, WY, NE, WI)**: Overbreadth voids the agreement
- **Reform-uncertain (DE post-2024, VA)**: Recent signals moving toward void-not-reform;
  confirm current state of law with counsel

---

### Step 8: Garden Leave and Compensation Analysis

Garden leave provisions — where the employer continues paying the employee's salary during
the restricted period — significantly affect enforceability in multiple states.

#### States with Mandatory or Near-Mandatory Garden Leave

**Massachusetts (MNAA, Mass. Gen. Laws ch. 149 § 24L)**:

- Employer must pay at least **50% of the employee's highest base salary** in the two years
  preceding the agreement, for the entire restricted period, unless "other mutually agreed
  upon consideration" is provided.
- For employees laid off or terminated without cause: the agreement is **void** unless the
  employer pays full garden leave for the restricted period.
- This is a statutory condition of enforceability, not a best practice.

**Illinois (IFWA, 820 ILCS § 90)**:

- For employees terminated, furloughed, or laid off due to COVID-19 (or similar causes):
  agreement is unenforceable unless employer pays full base salary during restricted period.
- Garden leave is excluded from the definition of "covenant not to compete," meaning a
  pure garden leave arrangement (employer pays; employee cannot work) is not treated as
  a non-compete and faces fewer restrictions.

**Florida CHOICE Act (eff. July 1, 2025, for "covered employees")**:

- The non-compete period is **reduced day-for-day** by any garden leave period under a
  compliant garden leave agreement.
- Employer must advise employee in writing of the right to seek counsel, with at least
  7 days to review, before the CHOICE Act's enhanced enforcement regime applies.
- "Covered employees" must receive written acknowledgment of receipt of confidential
  information or customer relationships.

#### Garden Leave Best Practices (All States)

Even where not legally required, a garden leave clause strengthens enforceability by:

1. Removing the employee's "undue hardship" argument
2. Demonstrating good faith and reasonable business purpose
3. Providing the employer more control over the transition period
4. Reducing the risk of a court finding the restriction unconscionable

**Minimum recommended garden leave structure:**

```
During the [N]-month Restricted Period, Employer shall continue to pay Employee
[100% / 50%] of Employee's base salary then in effect, provided Employee complies
with all restrictions herein. Employer may elect to waive the Restricted Period
at any time upon [30] days' written notice to Employee, in which case the
payment obligation shall cease as of the effective date of such waiver.
```

---

### Step 9: Choice-of-Law Analysis

**This step is critical for employees who live or work in California, Minnesota,
North Dakota, Oklahoma, Montana, or Wyoming — or who may relocate there.**

#### California's Extraterritorial Reach (SB 699 / § 16600.5)

California Business and Professions Code § 16600.5 (eff. January 1, 2024) provides:

> A contract that is void under this chapter is unenforceable regardless of where and
> when the contract was signed.

An employer "shall not attempt to enforce" a void non-compete. This creates a private
right of action in California, meaning an employee can sue the employer in California
to have the non-compete declared void — **even if the agreement has a non-California
choice-of-law clause**.

_Application Group, Inc. v. Hunter Group, Inc._ (Cal. Ct. App. 1998): Landmark case
establishing that California law governs employment non-competes for California employees
even when the contract designates another state's law.

**Key question**: Is the employee currently working in California, a California resident,
or seeking employment in California? If yes, the California ban applies regardless of
the agreement's governing law clause.

#### The DraftKings v. Hermalyn Counter-Example

_DraftKings, Inc. v. Hermalyn_, No. 24-1443 (1st Cir. Sept. 26, 2024): The First Circuit
upheld a Massachusetts non-compete against a California-resident employee. Key factors:

- The employee signed the agreement in Massachusetts with a Massachusetts company
- His pre-existing work relationships were with a Massachusetts-based business
- California became relevant only when he chose to take a job there
- The court held California's interest was not **materially greater** than Massachusetts's
  interest in enforcing the agreement under the Restatement (Second) § 187(2) analysis

**Restatement (Second) of Conflicts § 187(2) analytical framework:**

1. Does the chosen state have a **substantial relationship** to the parties/transaction?
   (Employer's home state, place of signing, place of performance)
2. Would applying the chosen state's law violate a **fundamental public policy** of the
   state with the materially greater interest?
3. Does the state whose law would apply absent the choice clause have a
   **materially greater interest** than the chosen state?

**Classify choice-of-law risk:**

| Scenario                                                                                | Classification                                                     |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Employee in CA / MN / ND / OK / MT / WY and employer designates a pro-enforcement state | VOID — choice-of-law clause ineffective; ban state law applies     |
| Employee in CA; agreement signed in MA with MA employer, MA governing law               | AT-RISK — DraftKings suggests MA law may govern; outcome uncertain |
| Employee in WA; agreement waives WA rights                                              | VOID — RCW § 49.62.060 renders waivers of WA rights void           |
| Employee in ban state with a purely in-state employer; no interstate facts              | VOID — no choice-of-law argument available to employer             |
| Employee in moderate state; governing law of moderate state; no ban-state nexus         | Analyze under designated state's law; choice clause likely honored |

---

### Step 10: Healthcare and Licensed Professional Special Analysis

If the employee is a healthcare professional, apply additional restrictions before
concluding the analysis:

| State                                  | Healthcare Restriction                                                                                                                          | Authority                                                          |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **California**                         | Ban applies to all professionals including physicians                                                                                           | Cal. Bus. & Prof. Code § 16600                                     |
| **Indiana**                            | Non-competes between physicians and hospitals BANNED (eff. July 1, 2025)                                                                        | Indiana P.L. 77-2025                                               |
| **Massachusetts**                      | Physicians, nurses, psychologists: exempt from non-competes entirely                                                                            | Mass. Gen. Laws ch. 149 § 24L(b)(ii)                               |
| **Maryland**                           | Healthcare providers earning under $350,000: protected; above threshold: 1-year max, 10-mile radius (eff. 2024)                                 | Md. Code Health Occ. § 14-301.1                                    |
| **Pennsylvania**                       | Healthcare practitioners: maximum 1-year duration; void if employer terminates without cause (eff. 2025)                                        | 2025 PA healthcare non-compete legislation [VERIFY exact citation] |
| **Texas**                              | All healthcare practitioners: 5-mile radius from primary practice, 1-year max, buyout option capped at total annual salary (eff. Sept. 1, 2025) | Tex. Bus. & Com. Code § 15.50(b) as amended by SB 1318             |
| **Connecticut**                        | Physicians: non-compete must be limited to geographic area of practice; 2-year max; must survive employer-initiated termination [VERIFY]        | Conn. Gen. Stat. § 20-14p                                          |
| **Arkansas, Louisiana, West Virginia** | Various physician-specific restrictions added or strengthened 2024–2025 [VERIFY current statutes]                                               | [VERIFY]                                                           |
| **FTC (all states)**                   | FTC warning letters (Sept. 2025) targeting healthcare employers with overbroad nurse/physician agreements; elevated Section 5 risk              | FTC Section 5, 15 U.S.C. § 45                                      |

**⟁ CLARIFY** — If the employee is a physician in Texas:

> Texas SB 1318 (eff. Sept. 1, 2025) significantly restricts physician non-competes.
> Do you need me to analyze enforceability under the pre-SB 1318 rules (for historical
> agreements) or the post-SB 1318 rules (for new agreements)?

---

### Step 11: Quality Verification

Before delivering output, apply all three quality frameworks silently.

#### Citation Quality Gates

Run these 5 gates before delivery. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                              | Fail Action                                                                      |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Source**     | Every enforceability classification cites the specific state statute, regulation, or established common law principle relied upon | Add citation or mark "[UNVERIFIED — employment counsel to confirm]"              |
| **Format**     | All statutory citations follow consistent format (state code section number, year in effect where material)                       | Fix format                                                                       |
| **Currency**   | Every threshold figure and statute checked for annual adjustments and recent amendments; salary thresholds noted as of 2025       | Flag "[CHECK CURRENCY — threshold adjusts annually; verify current year figure]" |
| **Domain**     | Analysis stays within the identified state(s)' governing law; no assumptions from other states bleeding in                        | Remove or flag cross-state bleed                                                 |
| **Confidence** | Uncertainty explicitly stated; no concealed uncertainty                                                                           | Add confidence qualifier                                                         |

#### Self-Interrogation for VOID and NON-COMPLIANT Classifications

For any item classified **VOID — STATUTORY BAN** or **NON-COMPLIANT**, apply this
3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the void/non-compliant classification follow directly from the cited statute or
  case law? Is the statute in force and current?
- Would the applicable state court actually reach this conclusion on these facts?
- Is there a counter-argument the employer's counsel would make (e.g., sale-of-business
  exception, senior executive carve-out)?

**Pass 2 — Completeness**:

- Have all applicable statutes and exceptions been considered?
- Has the choice-of-law question been fully resolved — is it clear which state's law
  governs?
- Have any healthcare-specific or role-specific carve-outs been checked?

**Pass 3 — Challenge**:

- What is the strongest argument that this non-compete IS enforceable?
- Under what facts might a court reform rather than void the agreement?
- Is there a narrowing construction of the restriction that would save it?

If any pass reveals a weakness, revise the classification before delivery. Mark the
Glass Box audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

#### Confidence Scoring

Assign a confidence level to each key classification:

| Level        | Range     | Meaning                                                                  | Action                                                              |
| ------------ | --------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled statute, unambiguous ban or clear threshold violation            | State with confidence; cite statute                                 |
| **High**     | 0.80–0.94 | Strong authority; minor questions on application to these specific facts | State with brief caveat                                             |
| **Probable** | 0.60–0.79 | Good arguments but reasonable courts could differ                        | State with explicit reasoning and contra-indicators                 |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities                               | Flag for employment counsel review with both sides of argument      |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                  | Do not assert; flag as "[UNCERTAIN — employment counsel to advise]" |

---

### Step 12: Deliver Analysis Output

Structure the final output using the Output Format Template (see below). Include the
Glass Box Audit Trail at the end of every output.

---

## Enforceability Classification System

Every analyzed non-compete provision receives one of four classifications:

### ENFORCEABLE

The provision is likely valid in the applicable state under current law. It satisfies
the ban/threshold screen, has a plausible legitimate business interest, is reasonable
in scope/geography/duration, and consideration is adequate.

**Action**: Note for awareness. Confirm annually as state law evolves. Flag for re-review
if employee's role or compensation changes materially.

### AT-RISK

The provision contains one or more elements that make it vulnerable to challenge,
though a court might still enforce it (likely in a discretionary-reform state). Issues
include: duration or geographic scope at the outer edge of reasonableness; legitimate
business interest arguable but not clearly established; consideration that could be
challenged; or a choice-of-law clause that faces challenge from an employee's current
state of residence.

**Action**: Specific redraft recommendations provided. Employer: redraft to reduce AT-RISK
elements before enforcement. Employee: document AT-RISK factors as potential challenge
grounds.

### NON-COMPLIANT

The provision fails one or more material enforceability requirements and is likely
unenforceable. A court in the applicable state would likely decline to enforce it as
written, even if the state allows discretionary reformation. Examples: salary threshold
violation; consideration defect; scope so broad that no legitimate business interest
could support it; duration exceeding any defensible standard.

**Action**: Provide specific revised language addressing each failure. In mandatory-reform
states (FL, TX), note that a court might reform rather than void — but advise redrafting
to control the outcome rather than leaving it to judicial discretion.

### VOID — [Basis]

The provision is void by operation of law:

- **VOID — STATUTORY BAN**: The applicable state has banned non-competes by statute (CA,
  MN, ND, OK, MT, WY).
- **VOID — BELOW SALARY THRESHOLD**: The employee earns below the applicable state's
  income floor for non-competes.
- **VOID — CHOICE-OF-LAW INAPPLICABLE**: The agreement designates a non-ban state's law
  but the employee is in a ban state and the choice clause is ineffective.

**Action**: Employer: do not attempt to enforce; risk of Section 5 FTC exposure (CA) or
litigation. Employee: document the void classification; notify employer that enforcement
will be contested.

---

## Prioritization Framework

When the analysis surfaces multiple issues, prioritize remediation or challenge in
this order:

### Tier 1 — Determinative (Act Immediately)

Issues that resolve enforceability categorically:

- Employee is in a total-ban state (CA, MN, ND, OK, MT, WY) → entire provision void
- Employee's compensation falls below applicable state threshold → provision void
- Agreement was signed after employment commencement in a state that requires at-hire
  execution → invalid consideration; provision likely void
- Choice-of-law clause designating pro-enforcement state is ineffective for employee
  in a ban state → provision void regardless of governing law designation

### Tier 2 — Material (Address Before Enforcement or Signing)

Issues that significantly increase the risk of unenforceability:

- Duration exceeds presumptive reasonableness for the applicable state
- Geographic scope broader than the employee's actual customer territory
- Legitimate business interest not clearly established (no trade secrets, no meaningful
  customer contact)
- Garden leave not provided in a state where it is required (MA) or heavily incentivized
- No notice period honored in states requiring advance notice (CO, IL, WA, OR, MA)
- Healthcare employee in a state with profession-specific restrictions

### Tier 3 — Risk Reduction (Address When Resources Permit)

Issues that reduce risk without being determinative:

- Single omnibus restriction without internal severability language (increases void risk
  in red-pencil states)
- Scope language uses undefined terms ("in any capacity," "anywhere the Company operates")
- No explicit identification of the legitimate business interest in the agreement text
- No garden leave provision even where not required (removes "undue hardship" defense)
- Agreement is more than 3 years old and has not been reviewed against updated state law

---

## 50-State Enforceability Reference Matrix

Use this matrix for quick screening. Always perform full analysis for Tiers 2 and 3.

| State              | Category                          | Key Rule                                                                                                                                               | Reform Doctrine                             |
| ------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| **Alabama**        | Moderate                          | Common law reasonableness; statutory support: Ala. Code § 8-1-190                                                                                      | Discretionary reform                        |
| **Alaska**         | Moderate                          | Common law reasonableness                                                                                                                              | Discretionary reform                        |
| **Arizona**        | Moderate                          | Common law; courts apply reasonableness; statutory: A.R.S. § 23-491.01 for low-wage workers                                                            | Blue pencil (literal)                       |
| **Arkansas**       | Moderate                          | Ark. Code Ann. § 4-75-101; physicians: specific restrictions (2024–2025)                                                                               | Discretionary reform                        |
| **California**     | **TOTAL BAN**                     | Cal. Bus. & Prof. Code §§ 16600–16600.5; extraterritorial reach; private right of action                                                               | Void; no reform                             |
| **Colorado**       | Near-ban                          | Colo. Rev. Stat. § 8-2-113; $127,091 threshold (2025); 14-day notice; physician ban (eff. Aug. 6, 2025)                                                | Discretionary reform                        |
| **Connecticut**    | Moderate                          | Common law; physician-specific restrictions; 2-year max for physicians                                                                                 | Discretionary reform                        |
| **Delaware**       | Moderate (shifting)               | Common law; _Sunder Energy_ (2024) signals move away from reform of patently overbroad agreements                                                      | Discretionary (shifting toward void)        |
| **D.C.**           | Near-ban                          | D.C. Non-Compete Clarification Amendment Act; ~$162,164 threshold (2026)                                                                               | Reform possible                             |
| **Florida**        | Strong enforcement                | Fla. Stat. § 542.335; CHOICE Act (eff. July 1, 2025) for high earners: 4-year max, mandatory injunction                                                | Mandatory reform                            |
| **Georgia**        | Strong enforcement                | O.C.G.A. §§ 13-8-50 to 13-8-59; 2-year presumptively reasonable; no express geographic restriction required (2024)                                     | Discretionary (court may modify under GRCA) |
| **Hawaii**         | Near-ban                          | HRS § 480-4; non-competes for technology employees void since 2015; broader restrictions proposed                                                      | Limited reform                              |
| **Idaho**          | Moderate                          | Idaho Code § 44-2701 et seq.; notable for mandatory reform provision                                                                                   | Mandatory reform                            |
| **Illinois**       | Near-ban                          | 820 ILCS §§ 90/1 et seq.; $75,000 threshold; 14-day notice; 2-year service or additional consideration                                                 | Discretionary reform                        |
| **Indiana**        | Moderate (healthcare: ban)        | Common law; physician-hospital non-competes BANNED (eff. July 1, 2025)                                                                                 | Discretionary reform                        |
| **Iowa**           | Moderate                          | Common law; reasonableness standard                                                                                                                    | Discretionary reform                        |
| **Kansas**         | Moderate                          | Common law; reasonableness standard                                                                                                                    | Discretionary reform                        |
| **Kentucky**       | Moderate                          | Common law; reasonableness standard                                                                                                                    | Discretionary reform                        |
| **Louisiana**      | Moderate                          | La. Rev. Stat. § 23:921; specific geographic/duration requirements (parishes, 2-year max); physician-specific rules                                    | Limited blue pencil                         |
| **Maine**          | Near-ban                          | 26 M.R.S. § 599-A; salary threshold ~$62,600; 3-year max; advance notice; notification of existing employees required                                  | Discretionary reform                        |
| **Maryland**       | Near-ban                          | Md. Labor & Emp't § 3-716; salary threshold ~$46,800; healthcare: $350,000 separate threshold                                                          | Discretionary reform                        |
| **Massachusetts**  | Near-ban                          | Mass. Gen. Laws ch. 149 § 24L (MNAA, eff. Oct. 1, 2018); 12-month max; 50% garden leave; 10-day advance notice                                         | Discretionary reform                        |
| **Michigan**       | Moderate                          | Mich. Comp. Laws § 445.774a; reasonableness standard                                                                                                   | Discretionary reform                        |
| **Minnesota**      | **TOTAL BAN**                     | Minn. Stat. § 181.988 (eff. July 1, 2023); sale/dissolution exception                                                                                  | Void; no reform                             |
| **Mississippi**    | Moderate                          | Common law; reasonableness standard                                                                                                                    | Discretionary reform                        |
| **Missouri**       | Moderate                          | Common law; reasonableness; no statute governing generally                                                                                             | Discretionary reform                        |
| **Montana**        | **TOTAL BAN**                     | Mont. Code Ann. § 28-2-703; sale of business exception                                                                                                 | Void; no reform                             |
| **Nebraska**       | Near-void                         | Common law but courts apply red pencil; voids entire agreement if any part unreasonable                                                                | Red pencil (void)                           |
| **Nevada**         | Near-ban                          | Nev. Rev. Stat. § 613.195; FLSA overtime-eligible threshold; reasonable geographic/duration required                                                   | Discretionary reform                        |
| **New Hampshire**  | Near-ban                          | RSA § 275:70-a; FLSA overtime-eligible threshold; advance notice requirement                                                                           | Discretionary reform                        |
| **New Jersey**     | Moderate                          | Common law; reasonableness; proposed legislation not enacted                                                                                           | Discretionary reform                        |
| **New Mexico**     | Moderate                          | Common law; reasonableness standard                                                                                                                    | Discretionary reform                        |
| **New York**       | Moderate (skeptical)              | Common law; "unique/extraordinary skills" or genuine trade secrets required; NY Senate bill pending but not enacted                                    | Discretionary reform                        |
| **North Carolina** | Moderate                          | Common law; must be ancillary to employment or sale-of-business                                                                                        | Blue pencil (literal)                       |
| **North Dakota**   | **TOTAL BAN**                     | N.D. Cent. Code § 9-08-06                                                                                                                              | Void; no reform                             |
| **Ohio**           | Moderate                          | Common law; reasonableness; Ohio SB 11 (proposed ban) not enacted                                                                                      | Discretionary (some courts: red pencil)     |
| **Oklahoma**       | **TOTAL BAN**                     | Okla. Stat. tit. 15, § 219A; red pencil — void in full                                                                                                 | Void; no reform                             |
| **Oregon**         | Near-ban                          | ORS § 653.295; $116,427 threshold (2025); 12-month max; 2-week advance notice; medical licensee ban (2025)                                             | Discretionary reform                        |
| **Pennsylvania**   | Moderate                          | Common law; must be signed at or before hire; mid-employment requires independent consideration; healthcare: 1-year max (2025)                         | Discretionary reform                        |
| **Rhode Island**   | Near-ban                          | R.I. Gen. Laws §§ 28-59-1 et seq.; 250% federal poverty threshold                                                                                      | Discretionary reform                        |
| **South Carolina** | Moderate                          | Common law; mid-employment: continued employment may be insufficient [VERIFY]                                                                          | Discretionary reform                        |
| **South Dakota**   | Moderate                          | S.D. Codified Laws § 53-9-11; reasonableness required                                                                                                  | Discretionary reform                        |
| **Tennessee**      | Moderate                          | Tenn. Code Ann. §§ 47-25-101 to 47-25-111 (employer-friendly)                                                                                          | Discretionary reform                        |
| **Texas**          | Strong enforcement                | Tex. Bus. & Com. Code §§ 15.50–15.52; "ancillary to or part of" an otherwise enforceable agreement; mandatory reform; healthcare: SB 1318 (Sept. 2025) | Mandatory reform                            |
| **Utah**           | Moderate                          | Utah Code § 34-51-101 et seq.; post-employment covenants: 1-year maximum                                                                               | Limited discretionary reform                |
| **Vermont**        | Moderate                          | Common law; reasonableness standard                                                                                                                    | Discretionary reform                        |
| **Virginia**       | Near-ban                          | Va. Code § 40.1-28.7:8; "low-wage employee" threshold $76,081 (2025)                                                                                   | Red pencil tendency; limited reform         |
| **Washington**     | Near-ban                          | RCW §§ 49.62.005–.900; $123,394 threshold; 18-month presumptive max; 14-day notice; independent consideration for mid-employment                       | Discretionary reform                        |
| **West Virginia**  | Moderate                          | Common law; reasonableness standard; some courts: red pencil                                                                                           | Discretionary (some: red pencil)            |
| **Wisconsin**      | Near-void                         | Common law; courts historically skeptical; tend toward void over reform                                                                                | Red pencil tendency                         |
| **Wyoming**        | **TOTAL BAN** (eff. July 1, 2025) | Non-competes void upon termination of employment                                                                                                       | Void; no reform                             |

---

## Anti-Patterns

What NOT to do when analyzing or drafting US non-compete provisions:

1. **Applying a single-state analysis nationally** — Non-compete law is 50 different legal
   regimes. A provision enforceable in Florida may be void in California, and an analysis
   that ignores the employee's actual state of work is worthless.

2. **Ignoring California's extraterritorial reach** — Post-SB 699 (eff. Jan. 1, 2024),
   California's ban applies "regardless of where and when the contract was signed." A
   Texas governing-law clause does not protect an employer from California's ban if the
   employee works or moves to California. This is the single most commonly missed analysis
   step.

3. **Treating "continued employment" as universally sufficient consideration** — In
   Pennsylvania, Washington, Illinois, Oregon, and North Carolina (among others), continued
   employment alone is not adequate consideration for mid-employment non-competes. Failing
   to check this often results in entirely void agreements.

4. **Ignoring salary thresholds** — 12+ states now void non-competes for employees below
   an income floor. These thresholds adjust annually. A threshold analysis done in 2023
   is not reliable in 2026.

5. **Using a national template without state customization** — A single non-compete
   agreement applied uniformly to a 50-state workforce will be void in some states,
   unenforceable in others, and enforceable in the remainder — creating inconsistent
   protection and potential employer liability (especially in California, which creates
   a cause of action against employers who attempt to enforce void agreements).

6. **Conflating non-solicitation with non-compete analysis** — Non-solicitation clauses
   (of customers or employees) are analyzed under different standards and are generally
   more enforceable than non-competes. Illinois, Washington, and Colorado have separate
   thresholds for non-solicitation that are lower than non-compete thresholds. Treating
   them identically produces incorrect analysis.

7. **Ignoring the advance-notice requirement** — Colorado, Illinois, Oregon, Massachusetts,
   and Washington require advance written notice before the agreement is signed. An
   agreement presented on day one, without the required notice period, may be
   unenforceable despite adequate consideration.

8. **Overrelying on choice-of-law clauses in ban states** — Choice-of-law clauses
   designating a pro-enforcement state do not work in California, Minnesota, North Dakota,
   Oklahoma, Montana, Wyoming, or Washington (which voids waivers of Washington law
   outright). Employers who rely on these clauses to enforce non-competes in ban states
   expose themselves to FTC scrutiny and private litigation.

9. **Drafting a nationwide geographic restriction for a regional employee** — Courts
   consistently reject nationwide restrictions for employees whose customer relationships
   are regional. Geographic scope must match the employee's actual territory; nationwide
   restrictions are overbroad for any employee who did not have nationwide customer
   relationships.

10. **Assuming the FTC Rule's failure means no federal exposure** — The FTC's April 2024
    rule was vacated, but the FTC's Section 5 enforcement authority under the FTC Act
    remains and is being used through case-by-case enforcement. Healthcare employers,
    staffing companies, and employers of low-wage workers face elevated FTC enforcement
    risk as of early 2026.

11. **Omitting internal severability clauses** — A non-compete, non-solicitation of
    customers, and non-solicitation of employees provision bundled in a single run-on
    paragraph without explicit standalone severability language will be voided entirely in
    red-pencil states if any element is overbroad. Separate each restriction into an
    independently enforceable paragraph.

12. **Skipping garden leave analysis in Massachusetts** — The Massachusetts MNAA requires
    payment of at least 50% of the employee's highest base salary during the restricted
    period as a statutory condition of enforceability. Missing this turns an otherwise
    valid 12-month non-compete into an unenforceable agreement.

13. **Failing to identify the specific legitimate business interest in the agreement text**
    — "Employee will have access to confidential information" is insufficient. Florida and
    Georgia courts require the employer to specifically plead and prove a legitimate
    business interest. An agreement that does not identify what specific trade secrets or
    customer relationships are at stake is more vulnerable to challenge.

14. **Treating healthcare professionals like other employees** — At least 16 states have
    enacted healthcare-specific non-compete restrictions since 2022. Analyzing a physician
    non-compete under the general reasonableness standard without checking the applicable
    state's healthcare-specific rules produces incorrect results.

15. **Using duration as a proxy for quality** — A 6-month restriction drafted with no
    geographic scope, no legitimate business interest, and no consideration is more
    vulnerable than a 2-year restriction drafted with all required elements. Duration is
    one factor; a short duration does not cure other deficiencies.

16. **Ignoring the red-pencil vs. blue-pencil doctrine** — In red-pencil states (CA, MN,
    ND, OK, WI, NE, and trending: DE, VA), a single overbroad element voids the entire
    agreement. Drafting strategy must account for the applicable state's reformation
    doctrine — an aggressive Florida-style draft is disastrous in Oklahoma.

---

## Localization Notes

This skill covers US state law only. Key localization notes for multi-jurisdictional
employer workforces:

- **Puerto Rico and US territories**: Non-compete enforceability analysis is not covered
  by this skill. Puerto Rico has its own labor law regime. [VERIFY]
- **Canada**: Canadian non-compete law is provincial and distinct from US law. Do not
  apply this skill to Canadian employees.
- **UK**: UK non-compete law (common law restraint of trade doctrine; no statutory ban
  equivalent to CA or MN) is not covered by this skill.
- **EU employees**: EU employees subject to their national laws; this skill does not apply.

---

## Writing Standards

Apply plain-language discipline to all output:

**For employer analysis**:

- Lead with the classification (ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID) for
  each state and each element assessed
- Explain the legal basis in plain terms: cite the specific statute or doctrine, not
  just a conclusion
- For AT-RISK and NON-COMPLIANT items: provide specific revised language, not just
  a description of the problem
- Flag salary thresholds with the applicable year: "[2025 threshold — verify annually]"

**For employee analysis**:

- Lead with actionable findings: if the restriction is void or likely unenforceable,
  say so clearly and explain the consequence (employer cannot enforce; employee should
  not let fear of void agreement prevent career decisions)
- Distinguish between "void" (legally null; employer cannot enforce) and "AT-RISK"
  (employer may try to enforce; outcome depends on litigation)
- Note that an employee receiving a void non-compete should consult employment counsel
  before making career decisions based on this analysis alone

**Quality gates before delivery**:

1. Is every classification backed by a specific state statute or case citation, or marked [VERIFY]?
2. Are salary thresholds labeled with the applicable year and flagged for annual verification?
3. Has the choice-of-law question been answered explicitly — not assumed from the governing law clause?
4. Are blue-pencil and red-pencil implications reflected in AT-RISK vs. NON-COMPLIANT classifications?
5. Is the output formatted using the Output Format Template below?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Steps 3 and 5, search for current state statutes governing non-competes in each
  relevant state (salary thresholds, ban statutes, notice requirements)
- Search for recent case law: _Sunder Energy v. Jackson_ (Del. 2024), _DraftKings v.
  Hermalyn_ (1st Cir. 2024), Georgia Supreme Court geographic restriction ruling (2024),
  _Ryan LLC v. FTC_ (N.D. Tex. 2024)
- Verify current salary thresholds for Colorado, D.C., Illinois, Maine, Maryland, Nevada,
  New Hampshire, Oregon, Rhode Island, Virginia, and Washington for the applicable year
- Check for any state statutes enacted or amended after the skill's research date
  (March 2026) that may affect the analysis
- Save verified citations to `/tmp/legalcode-noncompete-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with the analysis using the state matrix and salary threshold table in this skill
- Mark all salary threshold figures with "[CHECK CURRENCY — adjusts annually; verify
  current year figure]"
- Mark all statutory citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all citations require
independent verification before reliance"`
- Add a prominent notice to the output: "This analysis is based on training data through
  early 2026. State non-compete law changes frequently. Verify all statutory citations and
  salary thresholds against current state statutes before relying on this analysis."

---

## Output Format Template

Structure the final analysis as follows:

```markdown
## Non-Compete Enforceability Analysis

**Agreement / Clause**: [name or identifier]
**Employee Role**: [title and compensation level]
**States Analyzed**: [list all relevant states]
**Perspective**: [Employer / Employee / In-house counsel / Transactional]
**Date of Analysis**: [date]
**FTC Rule Status**: Vacated (N.D. Tex. Aug. 20, 2024); FTC acceded Sept. 5, 2025;
rule not in effect. Case-by-case Section 5 enforcement continues.

---

## Summary Findings

| State   | Classification                                 | Basis        | Confidence |
| ------- | ---------------------------------------------- | ------------ | ---------- |
| [State] | [VOID / NON-COMPLIANT / AT-RISK / ENFORCEABLE] | [Key reason] | [Level]    |

---

## Determinative Issues (Tier 1)

[Any total bans, salary threshold violations, consideration defects, or ineffective
choice-of-law clauses that resolve enforceability categorically]

---

## Detailed Analysis

### [State] — [CLASSIFICATION] | Confidence: [Level]

**Governing authority**: [Statute/case/doctrine]
**Issue**: [What the analysis found]
**Basis**: [Legal reasoning]
**Impact**: [Practical consequence for employer or employee]
**Recommended action**: [Specific redraft language or challenge strategy]

[Repeat for each state and each material issue]

---

## Reasonableness Assessment

**Legitimate business interest**: [Classification + basis]
**Geographic scope**: [Classification + basis]
**Duration**: [Classification + basis]
**Scope of activities**: [Classification + basis]
**Overall reasonableness**: [ENFORCEABLE / AT-RISK / NON-COMPLIANT]

---

## Consideration Analysis

**Timing of execution**: [At hire / Mid-employment / Unknown]
**Consideration identified in agreement**: [What the agreement states]
**Applicable state rule**: [Which states require what]
**Classification**: [VALID / AT-RISK / INVALID]

---

## Garden Leave Analysis

**Garden leave provision present?**: [Yes / No]
**If yes**: [Duration, percentage of salary, and compliance with applicable state rules]
**Massachusetts compliance (if applicable)**: [COMPLIANT / NON-COMPLIANT — 50% base salary requirement]
**Recommendation**: [Specific garden leave language if absent or deficient]

---

## Choice-of-Law Analysis

**Governing law designated**: [State]
**Employee's state of work/residence**: [State]
**Choice-of-law effectiveness**: [EFFECTIVE / INEFFECTIVE / AT-RISK]
**California extraterritorial analysis (if applicable)**: [Does SB 699 apply?]
**DraftKings analysis (if applicable)**: [§ 187 Restatement factors]

---

## Prioritization

**Tier 1 (Determinative — Act Immediately)**:

- [List]

**Tier 2 (Material — Address Before Enforcement or Signing)**:

- [List]

**Tier 3 (Risk Reduction — Address When Resources Permit)**:

- [List]

---

## Recommended Redrafts

[For each AT-RISK or NON-COMPLIANT element, provide specific revised language]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Glass Box Audit Trail

Append the following YAML block to every output:

```yaml
glass_box:
  skill: "legalcode-us-state-non-compete-analysis"
  agreement_reviewed: "[Agreement name/identifier]"
  employee_role: "[Title and compensation]"
  states_analyzed:
    - "[State 1] — [VOID / NON-COMPLIANT / AT-RISK / ENFORCEABLE]"
    - "[State 2] — [classification]"
  governing_law_designated: "[State]"
  ftc_rule_status: "Vacated Aug. 20, 2024 (Ryan LLC v. FTC, N.D. Tex.); FTC acceded Sept. 5, 2025; rule not in effect"
  salary_threshold_check: "[TRIGGERED / NOT TRIGGERED / NOT APPLICABLE]"
  threshold_year: "2025 — verify for subsequent years"
  consideration_issue: "[None / AT-RISK / DEFECTIVE]"
  garden_leave_issue: "[None / Massachusetts compliance / Other]"
  choice_of_law_issue: "[None / California extraterritorial / AT-RISK]"
  healthcare_employee: "[Yes — [state]-specific rules applied] / [No]"
  blue_pencil_doctrine: "[Reform-favorable / Reform-possible / Reform-hostile]"
  legalcode_mcp: "[Connected — citations VERIFIED] / [Not connected — citations require verification]"
  authority_reference_file: "[/tmp/legalcode-noncompete-authority.md or 'Not created']"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no VOID or NON-COMPLIANT items)]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "Salary thresholds are 2025 figures; verify annually"
    - "State statutes change frequently; verify all citations before reliance"
    - "This analysis does not constitute legal advice"
    - "[Any additional scope limitations]"
  reviewer: "AI-assisted — requires qualified employment attorney review before reliance"
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A (create from scratch)
workflow. Research pipeline: deep web-backed legal research via specialized agent covering
the FTC non-compete rulemaking timeline (_Ryan LLC v. FTC_, N.D. Tex., Aug. 20, 2024;
FTC Sept. 5, 2025 accession); all 50 states + DC; Cal. Bus. & Prof. Code §§ 16600–16600.5
(SB 699/AB 1076, eff. Jan. 1, 2024); Minn. Stat. § 181.988 (eff. July 1, 2023); Fla. Stat.
§ 542.335 + Florida CHOICE Act (eff. July 1, 2025); Tex. Bus. & Com. Code §§ 15.50–15.52

- SB 1318 healthcare (eff. Sept. 1, 2025); O.C.G.A. §§ 13-8-50–13-8-59; Mass. Gen. Laws
  ch. 149 § 24L (MNAA); RCW § 49.62 (SB 5935, eff. June 6, 2024); 820 ILCS §§ 90/1 et seq.
  (IFWA); Colo. Rev. Stat. § 8-2-113; ORS § 653.295; Va. Code § 40.1-28.7:8; Wyoming
  (eff. July 1, 2025); Montana Mont. Code Ann. § 28-2-703; _DraftKings, Inc. v. Hermalyn_,
  No. 24-1443 (1st Cir. Sept. 26, 2024); _Application Group v. Hunter Group_ (Cal. Ct. App.
  1998); _Sunder Energy, LLC v. Tyler Jackson_ (Del. S. Ct., Dec. 10, 2024); Georgia Supreme
  Court geographic restriction ruling (Sept. 4, 2024); Restatement (Second) of Conflicts
  § 187; garden leave requirements (MA MNAA; IL IFWA; FL CHOICE Act); salary threshold
  matrix (12+ states, 2025 figures); blue-pencil vs. red-pencil doctrine by state; healthcare
  and physician-specific restrictions (16+ states, 2024–2025). Calibrated against the
  `legalcode-contract-review` reference standard (18/18 quality elements). Sources: Katz
  Banks Kumin March 2026 noncompete law survey; Foley & Lardner 2025 income threshold update;
  Littler, Seyfarth Shaw, Jackson Lewis, Epstein Becker Green, and Greenberg Traurig client
  alerts (2024–2025); FTC press releases and consent orders; state statutes via Justia and
  state legislature websites. All citations marked [VERIFY] where not independently confirmed
  via legalcode-mcp.
