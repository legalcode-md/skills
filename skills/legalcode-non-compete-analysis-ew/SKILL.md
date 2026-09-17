---
name: legalcode-non-compete-analysis-ew
description: Analyse English law restrictive covenant enforceability (England & Wales) covering the common
  law reasonableness test (legitimate proprietary interest + proportionality of duration, geography, and
  activity scope), Tillman v Egon Zehnder [2019] UKSC 32 blue-pencil severance, garden leave and PILON
  interaction (Credit Suisse v Armstrong credit principle; Tullett Prebon combined-period assessment),
  springboard injunctions (Roger Bullivant doctrine; QBE v Dymoke [2012] team-move analysis; Aquinas Education
  v Miller [2023] continuing-benefit requirement), employee versus shareholder/business-sale covenant
  distinction (Nordenfelt permissive standard; Law by Design v Ali [2022] equity- stake spectrum), tiered/cascading
  covenants, consideration and mid-employment amendment requirements, and pending UK Government reform
  (November 2025 Working Paper; consultation closed 18 February 2026; four reform options including 3-month
  cap).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyse English law restrictive covenant enforceability (England & Wales) covering the common law reasonableness test (legitimate proprietary interest + proportionality of duration, geography, and activity scope), Tillman v Egon Zehnder [2019] UKSC 32 blue-pencil severance, garden leave and PILON interaction (Credit Suisse v Armstrong credit principle; Tullett Prebon combined-period assessment), springboard injunctions (Roger Bullivant doctrine; QBE v Dymoke [2012] team-move analysis; Aquinas Education v Miller [2023] continuing-benefit requirement), employee versus shareholder/business-sale covenant distinction (Nordenfelt permissive standard; Law by Design v Ali [2022] equity- stake spectrum), tiered/cascading covenants, consideration and mid-employment amendment requirements, and pending UK Government reform (November 2025 Working Paper; consultation closed 18 February 2026; four reform options including 3-month cap). Produces ENFORCEABLE / AT-RISK / PROBLEMATIC / UNENFORCEABLE / VOID classification with confidence-scored per-element analysis, Tier 1/2/3 prioritisation, actionable redlines, Glass Box audit trail. Use when reviewing employment agreements, severance packages, business-sale non-competes, or standalone restrictive covenant agreements governed by English law. Routes to legalcode-non-compete-analysis for cross-jurisdictional triage. Key authorities: Herbert Morris v Saxelby [1916] HL; Faccenda Chicken v Fowler [1987] CA; TFS Derivatives v Morgan [2004]; Tillman v Egon Zehnder [2019] UKSC 32; Planon v Gilligan [2022] EWCA Civ 642; Boydell v NZP [2023] EWCA Civ 373; Tom James v Potter [2025] EWHC 2873. Jurisdiction: England & Wales (primary); Scotland and Northern Ireland noted where divergent.


# Legalcode Non-Compete Analysis — England & Wales

> **Disclaimer**: This skill provides a framework for AI-assisted restrictive covenant
> enforceability analysis under English law. It does not constitute legal advice. All
> outputs require review by a qualified solicitor or barrister experienced in employment
> and commercial litigation in England and Wales before any enforcement, compliance,
> drafting, or litigation decision is made. Restrictive covenant law evolves through
> case-by-case judicial assessment — no algorithmic analysis predicts with certainty how
> a court will rule on a specific clause against a specific employee in specific
> circumstances. Statutory and case law references cited here carry hallucination risk;
> verify all citations against authoritative sources (legislation.gov.uk, BAILII, Westlaw,
> Lexis+) before use. UK Government non-compete reform is active: the November 2025
> Working Paper options (including a 3-month cap) have not been enacted as of the date
> of this analysis; verify current reform status before advising on future-proof drafting.

---

## Purpose and Scope

This skill analyses whether a restrictive covenant is enforceable under English law,
identifies specific deficiencies reducing enforceability, generates confidence-scored
assessments, and produces Tier-ranked remediation recommendations.

**Covers:**

- Common law reasonableness test: legitimate proprietary interest + proportionality
- Four categories of protectable interest: trade secrets, customer connections,
  workforce stability, and specialist training investment
- _Tillman v Egon Zehnder_ [2019] UKSC 32 blue-pencil severance mechanics
- Garden leave and PILON interaction — combined market exclusion period analysis
- Springboard injunctions — separate equitable remedy independent of PTRNC validity
- Employee vs. shareholder/business-sale covenant distinction
- Tiered and cascading covenants
- Consideration requirements — new-hire vs. mid-employment amendments
- UK Government reform landscape (November 2025 Working Paper; outcome pending)
- 5-tier enforceability classification with confidence scoring
- Tier 1/2/3 prioritised remediation framework
- Glass Box audit trail for counsel and board use

**Does not:**

- Draft new restrictive covenant clauses (this skill reviews existing clauses only)
- Provide legal advice or predict court outcomes — judges apply fact-specific tests
- Perform full cross-jurisdictional analysis (route to `legalcode-non-compete-analysis`)
- Analyse non-solicitation of employees, confidentiality, or IP assignment provisions
  in isolation (see `legalcode-employment-agreement-review`, `legalcode-nda-triage`)
- Apply to franchise agreement non-compete clauses (different framework — see
  `legalcode-franchise-agreement-review-uk`)
- Cover Scotland or Northern Ireland in depth — the skill flags material differences
  but is primarily calibrated to English law

**Related skills:**

- `legalcode-non-compete-analysis` — cross-jurisdictional router (US/UK/DE/FR/CN)
- `legalcode-us-state-non-compete-analysis` — US 50-state matrix
- `legalcode-employment-agreement-review` — full employment contract clause-by-clause
- `legalcode-franchise-agreement-review-uk` — franchise non-compete under UK/BFA law
- `legalcode-nda-triage` — non-disclosure and confidentiality covenant review
- `legalcode-uk-employment-tribunal-claim` — ET claim preparation workflow

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: England and Wales.

**Legal framework**: Entirely judge-made common law. There is no UK statute specifically
governing the enforceability of post-employment restrictive covenants. The doctrine of
restraint of trade is the governing principle. The default rule is that all restraints
of trade are void as contrary to public policy; the burden falls on the employer to
justify the restriction.

**Key legal principles:**

- _Herbert Morris Ltd v Saxelby_ [1916] 1 AC 688 (HL) — foundational authority defining
  legitimate proprietary interest categories; employer cannot protect against mere
  competition
- _Faccenda Chicken Ltd v Fowler_ [1987] Ch 117 (CA) — three-tier information hierarchy
  for confidentiality claims; post-employment protection only for genuine trade secrets
- _TFS Derivatives Ltd v Morgan_ [2004] EWHC 3181 (QB) — three-stage reasonableness test
- _Tillman v Egon Zehnder Ltd_ [2019] UKSC 32 — blue-pencil severance within single
  standalone covenant; overruled _Attwood v Lamont_ [1920]
- _Planon Ltd v Gilligan_ [2022] EWCA Civ 642 — delay in enforcement is potentially fatal
- _Boydell v NZP Ltd_ [2023] EWCA Civ 373 — Tillman severance applied; fantastical
  consequences principle
- _Tom James UK Ltd v Potter_ [2025] EWHC 2873 (KB) — 12-month covenant void: no
  individual tailoring, no evidence justifying duration, alternatives available

**Critical principle — timing of assessment**: Reasonableness is assessed **at the
time the covenant was entered into**, not at enforcement. A covenant reasonable when
signed by a junior employee does not become enforceable when that employee is later
promoted. A covenant unreasonable at signing cannot be saved by subsequent role changes
(_Patsystems Holding Ltd v Neilly_ [2012] EWHC 2609 (QB)).

**Scotland differences (note):**

- Scotland applies the same restraint-of-trade doctrine (common to the whole of the
  UK), but has a separate court system (Court of Session; Sheriff Courts).
- For **interim relief**, Scotland's threshold is easier for employers: the test is
  _prima facie_ case (lower than England's "serious question to be tried" threshold
  under _American Cyanamid_ [1975] UKHL 1).
- If the agreement is governed by Scots law or the employee is based in Scotland,
  obtain specific Scots law advice.

**Northern Ireland**: Applies English common law restraint-of-trade doctrine; separate
court system (Belfast High Court). Differences are minor; English authorities are
directly persuasive.

**UK Government reform (current status — March 2026)**:

- November 2025: Labour government publishes _Working Paper on Options for Reform of
  Non-Compete Clauses in Employment Contracts_.
- Consultation closed: 18 February 2026.
- Reform options under consideration include: (1) statutory cap of 3 months;
  (2) variable cap by employer size; (3) complete ban; (4) salary threshold ban;
  (5) hybrid salary/cap approach.
- **No legislation enacted.** Reform requires primary legislation; not imminent.
- Approximately 5 million UK workers currently subject to non-compete clauses (est.
  26% of the workforce).
- Reform would **not** affect: non-solicitation, non-dealing, non-poaching, garden
  leave, or confidentiality provisions; nor covenants in shareholder/commercial
  agreements.
- **Practical implication for current analysis**: advise clients to future-proof
  clauses against a potential 3-month statutory cap by ensuring existing restrictions
  would survive even if reduced to 3 months.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the covenant creates a fork that only context can resolve
- Severity classification depends on business or role context not yet supplied

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

### Step 1: Accept Input

Accept the restrictive covenant in any of these formats:

- **Full document**: Employment agreement, severance agreement, shareholders' agreement,
  business-sale agreement, or standalone restrictive covenant deed
- **Clause extract**: The specific post-termination restrictions section only (note that
  interaction with PILON, garden leave, and notice provisions may be lost without the
  full document)
- **Description**: Summary of the clause terms (duration, geography, activity scope,
  whether compensation is paid during the restriction, employee role and seniority)

If only a description is provided, state that the analysis is based on described terms
and that a review of the actual drafted language is required before relying on the
assessment.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user for the following (skip any already
provided):

1. **Document type and context**: What type of agreement is this from?
   - Options: Employment agreement (new hire), Employment agreement (mid-employment
     amendment), Severance/settlement agreement, Business-sale/M&A agreement,
     Shareholders' agreement, Partnership agreement, Standalone covenant, Other
   - _Why this matters_: Employment contracts receive strict scrutiny; business-sale
     agreements receive permissive treatment (_Nordenfelt_ standard). Mid-employment
     amendments require fresh consideration. Different standards, different analysis.

2. **Perspective**: Who is seeking this analysis?
   - Options: Employer — assessing enforceability before attempting enforcement;
     Employee — assessing risk of challenge before joining a competitor;
     In-house counsel — risk-assessing a proposed or existing clause;
     Transactional counsel — drafting or reviewing in a deal context
   - _Why this matters_: Determines whether the output focuses on enforcement strategy,
     challenge strategy, remediation, or drafting improvements.

3. **Employee seniority and role**: What is the employee's position?
   - Options: C-suite / Board director; Senior executive / VP / Director-level; Mid-level
     manager; Junior / entry-level; Technical specialist (e.g., software engineer,
     scientist, researcher); Sales or client-facing professional
   - _Why this matters_: Courts assess reasonableness against the employee's actual role
     and access to protectable information at the time of contracting. A 12-month
     non-compete for a junior employee will receive extremely hostile scrutiny.

4. **Access to protectable information**: What did the employee have access to?
   - Options: Genuine trade secrets (secret formulae, proprietary algorithms, classified
     pricing data); Senior customer relationships (primary point of contact for key
     accounts); Workforce knowledge (knows which employees are key, likely to be poached);
     Employer-funded specialist training; Limited / general commercial knowledge only
   - Allow multiple selections.
   - _Why this matters_: Without a specific identifiable protectable interest, the
     covenant is void regardless of how it is drafted.

5. **Covenant terms**: Specify (or confirm from the document):
   - Duration of restriction (months/years)
   - Geographic scope (UK-wide, regional, specific area, no restriction)
   - Activity scope (specific named competitors, named clients, broad sector, all work)
   - Whether any compensation is paid during the restriction period
   - Garden leave status (currently on garden leave, garden leave served, not applicable)
   - PILON clause: present / absent / unclear

6. **Enforcement urgency** (if employer perspective):
   - Options: Pre-emptive (employee not yet left or breached); Imminent (employee has
     left and appears to be in breach); Active breach confirmed; Reviewing for future
     drafting only
   - _Why this matters_: Delay in enforcement is potentially fatal (_Planon v Gilligan_
     [2022]). If breach is active, the workflow must trigger urgent interim injunction
     guidance.

State assumptions explicitly if partial context is provided (e.g., "I am assuming this
is an employment contract with no paid restriction period — correct me if wrong").

### Step 3: Establish the Legal Baseline

Before analysing the specific covenant, apply the three-stage reasonableness test from
_TFS Derivatives v Morgan_ [2004]:

**Stage 1 — Construe the covenant**: Determine the actual scope of the restriction on
a proper construction, before assessing enforceability. Avoid both under-reading (where
the employer loses protection unnecessarily) and over-reading (where the clause appears
broader than intended). Apply the _Home Counties Dairies v Skilton_ [1970] principle:
a clause valid in all "ordinary circumstances contemplated by the parties" is not
invalidated because it might theoretically catch highly improbable scenarios.

**Stage 2 — Identify the legitimate proprietary interest**: The employer must establish
a specific protectable proprietary interest (see Part A of the analysis in Step 5).
General competitive advantage, the employee's general skill and knowledge, or the mere
risk of competition are not protectable interests (_Herbert Morris v Saxelby_ [1916]).

**Stage 3 — Assess reasonableness**: The restriction must go no further than reasonably
necessary to protect the identified interest. This is assessed at the time the covenant
was entered into, not at enforcement.

**⟁ CLARIFY** — If the context raises any of the following, ask the user before
proceeding with the main analysis:

- **Employee is both an employee and a shareholder**: Ask what equity stake they hold.
  The analysis differs significantly (see Part G — Employee vs. Shareholder Covenant).
- **The covenant appears in a shareholders' agreement, not an employment contract**: Confirm
  the nature of the arrangement and whether it is linked to a genuine business sale or
  transfer of goodwill, or to employment only.
- **The covenant has been amended post-commencement of employment**: Ask for details of
  the amendment — fresh consideration is essential and its absence may void the amended
  version.

### Step 4: Assess the Governing Law and Territorial Position

Confirm that English law governs the covenant. If a different governing law is stated
or the employee is primarily based outside England and Wales, flag:

- If governed by **Scots law**: note lower interim relief threshold; advise Scots law
  counsel.
- If governed by a **non-UK law**: note that English restraint-of-trade principles may
  still apply as mandatory law if the employee works in England and Wales.
- If **no governing law clause**: flag as a missing element; English law likely applies
  by default if the employee works here.

### Step 5: Conduct Enforceability Analysis

Analyse the covenant across nine analytical parts. Deliver findings in the Output Format
Template (see below) for each Part.

#### Part A — Legitimate Proprietary Interest

The starting point is always the interest to be protected. Without a specific protectable
interest, no amount of reasonable drafting will save the clause.

**Assess each of the four recognised categories:**

| Category                                       | Core Authority                                                                                      | What Must Be Established                                                                                                                                                                                     |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Trade secrets / confidential information**   | _Faccenda Chicken v Fowler_ [1987] CA; _Herbert Morris v Saxelby_ [1916] HL                         | The employee had access to genuine Category 3 information (true trade secrets) — not merely confidential information that forms part of general skill and knowledge; specific information must be identified |
| **Trade connections / customer relationships** | _Herbert Morris v Saxelby_ [1916]; _Beckett Investment Management Group v Hall_ [2007] EWCA Civ 613 | Personal influence over customers sufficient to divert business; must be more than merely knowing the client list; frequency and depth of contact is assessed                                                |
| **Workforce stability**                        | General principle                                                                                   | Applies only where the employee was genuinely placed to poach key colleagues; applies to senior management; insufficient for most employees                                                                  |
| **Investment in specialist training**          | General principle; _Hanover Insurance Brokers v Shapiro_ [1994]                                     | Employer-funded training that gives the employee specialist competitive advantage; more limited category; must be genuinely distinct from ordinary on-the-job learning                                       |

**Findings for Part A:**

For each category: state whether the interest is (a) clearly established on the facts
described, (b) arguable but not clearly established, or (c) absent. Classify the overall
interest finding as:

- **ESTABLISHED** — Specific identifiable protectable interest clearly present.
- **ARGUABLE** — Some basis for a protectable interest but it could be challenged.
- **ABSENT** — No identifiable proprietary interest beyond general competitive protection.
  If ABSENT: the covenant is unenforceable regardless of duration, geography, or scope.
  Stop the proportionality analysis and classify as VOID unless a partial interest can
  be established.

#### Part B — Duration Assessment

Assess the duration of the covenant against these benchmarks, all derived from case law:

| Duration    | Typical Court Treatment                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ≤ 3 months  | Almost always reasonable for employees with genuine access to protectable interests                                                                                                                                                  |
| 3–6 months  | Generally reasonable for mid-level and senior employees                                                                                                                                                                              |
| 6–12 months | Scrutinised carefully; requires specific justification linked to seniority and the nature of the protectable interest; currently the de facto practical maximum for most senior employees                                            |
| 12 months   | Achievable for senior executives with very strong customer relationships or highly sensitive trade secrets; must be specifically justified (_Tom James v Potter_ [2025]: refusal where no justification for 12 months was evidenced) |
| > 12 months | Very difficult; courts rarely uphold beyond 12 months for individual employees; exceptional cases only (e.g., senior partner with critical client relationships, key holder of genuinely proprietary technology)                     |
| > 24 months | Effectively unenforceable in an employment context under current case law                                                                                                                                                            |

Critically: the duration must be calibrated to the identified protectable interest. The
time frame should reflect how long it takes for the trade secret to lose its value, or
for customer relationships to naturally attenuate without the employee's influence.

**Finding for Part B:** Classify as COMPLIANT / BORDERLINE / EXCESSIVE, with confidence
score.

#### Part C — Geographic Scope Assessment

The geographic scope must reflect the territory in which the employer actually operates
and in which the employee actually carried out work. Assess:

- **Employer's actual geographic market**: Identify from context — is this a local, regional,
  national, European, or global business?
- **Employee's actual operational territory**: A regional manager covering the South East
  of England cannot be subject to a worldwide restriction.
- **Nature of the business**: Online businesses may legitimately claim broader geographic
  scope than purely physical businesses.
- **Relationship to the identified interest**: For customer relationship protection, the
  scope should be limited to the territories where the employee had those relationships.

Common scope patterns and their typical treatment:

| Geographic Scope                       | Treatment                                                                                                                               |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Named counties / defined regional area | Generally reasonable if linked to employee's actual territory                                                                           |
| England and Wales                      | Reasonable for employees with UK-wide client responsibilities                                                                           |
| United Kingdom                         | May require justification if the business is primarily England-based                                                                    |
| Europe / EU                            | Requires very strong justification; European scope upheld where the business genuinely operates pan-European and the employee is senior |
| Worldwide                              | Only upheld for genuinely global businesses and very senior employees (_Nordenfelt_ standard in commercial context, not employment)     |
| No geographic restriction              | Will be assessed: is the restriction effectively unlimited by the activity scope?                                                       |

**Finding for Part C:** Classify as COMPLIANT / BORDERLINE / EXCESSIVE, with confidence score.

#### Part D — Activity Scope Assessment

The activity scope must be limited to activities that would genuinely harm the
identified protectable interest. Assess:

- **Narrowly tailored restrictions** (most defensible):
  - Prohibition on working for named direct competitors
  - Prohibition on soliciting specific named clients
  - Prohibition on working in the employee's specific specialism at a competitor
- **Mid-range restrictions** (scrutinised closely):
  - Prohibition on working for companies in a broadly described competitive sector
  - Prohibition on working in any capacity for named competitors (including as a cleaner)
- **Overbroad restrictions** (typically unenforceable):
  - Prohibition on being "engaged or concerned or interested" in any competing business
    (pre-_Tillman_ standard; may be severable post-_Tillman_ if "interested" is deleted)
  - Prohibition on working "in any capacity" for any competitor (_Tom James v Potter_ [2025])
  - Industry-wide ban for a non-senior employee ("cannot work in financial services")

**⟁ CLARIFY** — If the activity scope has an apparent minor overreach that might be
severable under _Tillman_, present the options:

- "The activity scope includes 'interested in', which was the specific language considered
  in _Tillman_. I can assess whether severance of 'interested' leaves an enforceable core,
  or treat the clause as written. How would you like to proceed?"

**Finding for Part D:** Classify as COMPLIANT / BORDERLINE / EXCESSIVE / OVERBROAD, with
confidence score.

#### Part E — Garden Leave and PILON Interaction

Garden leave and post-termination restrictive covenants serve overlapping protective
purposes. Assess their interaction:

**Garden leave analysis:**

If a garden leave clause is present:

1. What is its duration (in months)?
2. Is full salary payable throughout? (If not, a reduced-salary garden leave is more
   likely to face challenge itself.)
3. Does the PTRNC contain a **set-off clause** (reducing the PTRNC period by any garden
   leave actually served)?

**Legal position on the credit principle:**

- There is **no automatic legal requirement** to reduce the PTRNC by the garden leave
  period (_Credit Suisse Asset Management Ltd v Armstrong_ [1996] IRLR 450 CA).
- However, courts assess the **total period of market exclusion** (garden leave + PTRNC
  combined) when evaluating proportionality (_Tullett Prebon Plc v BGC Brokers LP_ [2011]
  EWCA Civ 131).
- A combined period that is disproportionately long will attract scrutiny even if each
  element individually would be reasonable.
- **Best practice**: include a garden leave set-off clause reducing the PTRNC by any
  garden leave served. While not legally mandated, it demonstrates proportionality and
  materially strengthens enforceability (_Square Global Ltd v Leonard_ [2020] EWHC).

**PILON analysis:**

If a PILON clause is present:

1. Does it expressly state that post-termination restrictive covenants survive payment
   in lieu of notice?
2. If silent on this point: flag as a potential gap — some courts may be willing to
   imply survival, but the express statement eliminates ambiguity.

**Combined period assessment:**

| Combined Period (Garden Leave + PTRNC) | Assessment                                                                |
| -------------------------------------- | ------------------------------------------------------------------------- |
| ≤ 6 months                             | Generally proportionate for mid-level employees                           |
| 6–12 months                            | Needs justification; generally proportionate for senior employees         |
| 12–18 months                           | Subject to scrutiny; needs strong justification for very senior employees |
| > 18 months                            | Near-impossible to enforce in employment context                          |

**Finding for Part E:** State combined period, whether a set-off clause is present/absent,
whether PILON clause expressly preserves PTRNCs, and overall assessment.

#### Part F — Blue-Pencil Severance Assessment (Tillman Analysis)

Following _Tillman v Egon Zehnder_ [2019] UKSC 32, courts can sever an unenforceable
portion of a standalone covenant if three conditions are met:

| Tillman Test                             | Condition                                                                                                                                |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Blue Pencil**                       | The offending words can be removed by deletion only — no additions or modifications to the remaining text                                |
| **2. Adequate Consideration**            | The remaining terms continue to be supported by consideration (rarely in dispute in employment)                                          |
| **3. No Major Change in Overall Effect** | Severance must not generate a major change in the overall character or effect of all post-employment restraints. Burden on the employer. |

**Assess which elements are potentially severable:**

- If the activity scope is overbroad only in one dimension (e.g., "interested in any
  competitor" — delete "interested in"): likely severable per _Tillman_ itself.
- If the duration is overbroad in one limb of a tiered covenant (e.g., 24 months /
  18 months / 12 months — delete the first two limbs): likely severable per _Beckett
  Investment Management Group v Hall_ [2007] EWCA Civ 613.
- If the entire covenant is fundamentally unreasonable (no narrower core survives):
  not severable. The court will not rewrite to give the clause commercial effect
  (_Prophet PLC v Huggett_ [2014] EWCA Civ 1013 — courts cannot add words).
- If the geographic scope is the only problem (entire UK clause for a regional employee):
  courts may be able to sever to the relevant region if the covenant is structured to
  allow it.

**Finding for Part F:** State which elements (if any) appear severable under _Tillman_,
the predicted outcome of severance, and overall confidence in whether a court would
sever.

#### Part G — Employee vs. Shareholder/Commercial Covenant

**The spectrum of scrutiny:**

| Context                                                                       | Standard                                                                                                                  | Key Authority                                                                     |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Employment contract only                                                      | Strict scrutiny — _Herbert Morris v Saxelby_ applies; must protect specific proprietary interest; no wider than necessary | _Herbert Morris v Saxelby_ [1916] HL                                              |
| Shareholders' agreement with substantial equity stake / genuine business sale | Permissive — broader restrictions can be upheld; parties of equal commercial sophistication                               | _Nordenfelt v Maxim_ [1894] AC 535; _Quantum Actuarial_ [2021] EWCA Civ 227       |
| Shareholders' agreement with minimal equity grant to employee                 | Near-employment scrutiny — small equity stake does not shift to commercial standard                                       | _Law by Design Ltd v Ali_ [2022] IRLR 610; _Gardiner Graphics Group v Pay_ (2022) |
| Post-acquisition non-compete by seller/departing shareholder                  | More permissive — buyer entitled to protection of goodwill purchased                                                      | _Nordenfelt_ and commercial cases generally                                       |

**Assessment of which standard applies:**

If the employee holds equity:

- What is the size of the equity stake? (A 3% stake in a small firm attracted near-
  employment scrutiny in _Law by Design v Ali_ [2022])
- Was the equity granted as a genuine transfer of business value, or as a retention
  mechanism?
- Were the parties of broadly equal commercial sophistication when the agreement was
  entered into?
- Did the covenant arise in connection with a genuine business sale transferring goodwill?

**⟁ CLARIFY** — If the employee holds any equity:
"I can see the employee holds a [X]% equity stake. Courts apply a spectrum of scrutiny
that moves from employment-law strictness for minimal equity grants toward Nordenfelt
permissiveness for genuine business sales. To assess which standard applies, I need:
(a) the size of the stake; (b) whether the covenants were entered into as part of a
business sale or a shareholder/employment package; and (c) whether the parties were of
similar commercial sophistication."

**Finding for Part G:** State which standard applies, with confidence score.

#### Part H — Consideration and Mid-Employment Amendments

**New-hire covenants**: Supported by the offer of employment itself. No additional payment
required, though adequacy of overall remuneration is a factor in the broader
reasonableness assessment.

**Mid-employment amendments**: Require **fresh consideration**. Continued employment
alone is not sufficient consideration under English law. Required: a pay rise, bonus,
promotion, or another tangible new benefit expressly linked to the amended covenant.

**Practical risks:**

- Employer issues new employment contract on promotion, including new/strengthened
  covenants, but does not expressly link the promotion to the covenants: courts may
  find the promotion is consideration for the contract as a whole, but specific items
  may be challenged.
- New covenants added to an existing contract by way of letter, without any
  accompanying benefit: very likely unenforceable.
- Covenants in a deed: deeds require no consideration as a matter of general law, but
  restraints of trade are a special category — courts have held that even deed-based
  restraints require consideration (_Lorimer v Mackin_ noted, but the position is
  unsettled [VERIFY]).

**Timing of assessment**: Even if fresh consideration was provided, the covenant's
reasonableness is assessed at the time it was entered into, based on the role at that
point. A covenant added at a junior level is assessed against a junior employee's
circumstances — subsequent promotion does not strengthen it.

**Finding for Part H:** State whether consideration is present, whether the covenant is
a new-hire or mid-employment amendment, and confidence in the consideration analysis.

#### Part I — Springboard Injunction Context

A springboard injunction is a distinct equitable remedy separate from PTRNC
enforceability. It can be granted even if the PTRNC is unenforceable, and it does not
require a non-compete clause at all.

**Requirements** (from _Roger Bullivant Ltd v Ellis_ [1987] IRLR 491; _QBE Management
Services v Dymoke_ [2012] EWHC 80):

1. **Unlawful conduct** — prior misuse of confidential information, breach of fiduciary
   duty, or breach of contract (e.g., covert recruitment, removal of customer data).
2. **Ongoing unfair advantage** — the defendant must currently be benefiting from the
   competitive head start gained through that wrongdoing (_Aquinas Education Ltd v Miller_
   [2023] — refused where continuing benefit was speculative).
3. **Risk of future economic harm** — the ongoing advantage must threaten measurable
   loss.
4. **Inadequacy of damages** — monetary compensation alone must be insufficient.

**Duration**: Calibrated to the actual competitive advantage gained — the time it would
take for the defendant to legitimately reach the same position without the benefit of
the wrongdoing. In practice: days to months. Rarely exceeds 12 months.

**Assess springboard exposure:**

| Indicator                                                                              | Higher Springboard Risk                  |
| -------------------------------------------------------------------------------------- | ---------------------------------------- |
| Employee copied customer lists or trade secrets on departure                           | Yes                                      |
| Employee covertly recruited colleagues before resigning                                | Yes (team move context — _QBE v Dymoke_) |
| Employee shared confidential pricing, strategy, or technical data with future employer | Yes                                      |
| Departure was sudden and employee had unusually detailed knowledge of upcoming deals   | Yes                                      |
| No evidence of wrongdoing; ordinary competitive departure                              | No — springboard inappropriate           |

**Finding for Part I:** State whether springboard exposure is present, assess risk level
(HIGH / MODERATE / LOW / NOT APPLICABLE), and explain the basis.

### Step 6: Run Quality Verification

Before generating the final output, run the Quality Assurance Framework (see below):

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every UNENFORCEABLE or VOID classification, run the 3-pass Self-Interrogation.
   Revise if any pass causes doubt.
3. Apply Confidence Scoring to every finding and the overall classification.
4. Complete the Glass Box Audit Trail YAML template.

### Step 7: Generate the Enforceability Assessment

Deliver the full output using the Output Format Template (see below), incorporating all
findings from Parts A through I, quality-verified before delivery.

**⟁ CLARIFY** — If the analysis reveals a borderline classification where reasonable
employment counsel could disagree:

- "This covenant sits at the boundary between AT-RISK and PROBLEMATIC on the duration
  dimension. Courts have gone both ways on 12-month restrictions for senior executives
  in this sector. Do you want me to: (a) take a conservative view and classify it as
  PROBLEMATIC (more risk, stronger case for remediation), or (b) take an optimistic view
  and classify it as AT-RISK (manageable risk, emphasis on enforcement strategy)?"

---

## Enforceability Classification

Apply the 5-tier enforceability classification to the overall covenant and to each
analytical dimension:

| Classification    | Meaning                                                                                                                                                                                                                                                                                                                                                        | Typical Outcome                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ENFORCEABLE**   | All elements satisfy the reasonableness test; legitimate interest clearly established; duration, geography, and activity scope are proportionate; consideration supported; garden leave coordination appropriate                                                                                                                                               | Covenant likely enforceable as drafted; enforcement strategy appropriate; no material remediation required                                                                                                                                      |
| **AT-RISK**       | One element is borderline — close to but not clearly exceeding reasonable limits (e.g., 12-month duration for a senior executive where the business interest is strong); overall risk of challenge but reasonable prospect of enforcement                                                                                                                      | Enforcement may succeed but faces litigation risk; consider whether the borderline element can be strengthened prospectively; active enforcement requires interim injunction strategy prepared in advance                                       |
| **PROBLEMATIC**   | One or more identified deficiencies — e.g., no fresh consideration for mid-employment amendment; garden leave + PTRNC combined period is disproportionately long; activity scope ambiguous; PILON clause silent on PTRNCs — these deficiencies are identifiable but may be remediable in future agreements                                                     | Existing clause has significant vulnerabilities; court may enforce in whole or part, or may decline; immediate remediation recommended for future agreements; litigation strategy must account for the specific deficiency                      |
| **UNENFORCEABLE** | Overbroad in multiple dimensions (e.g., 18-month duration + worldwide scope + any-capacity restriction for a mid-level employee); or a single element is so grossly disproportionate (e.g., 5-year duration) that no court would enforce it; or the identified legitimate interest is absent                                                                   | Clause unlikely to be enforced as drafted; consider whether partial enforcement (via Tillman severance) is possible; if not, alternative protective mechanisms should be considered (garden leave, non-solicitation, confidentiality, clawback) |
| **VOID**          | Per-se invalidity — e.g., employer has repudiated the employment contract (employee released from all post-employment obligations); covenant is in a deed with no consideration and fails the restraint-of-trade exception; or the covenant was entered into under duress or as a condition of not being dismissed in circumstances amounting to a repudiation | Covenant has no legal effect; a fresh covenant (with fresh consideration and a properly terminated and re-engaged employment relationship) would be required if protection is desired                                                           |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                                             | Fail Action                           |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Source**     | Every enforceability claim cites a specific case, statute, or established common law principle                                                                                   | Add citation or mark [UNVERIFIED]     |
| **Format**     | All citations use consistent neutral format: _Case Name_ [YYYY] Court Ref                                                                                                        | Fix format                            |
| **Currency**   | Every cited case checked: still good law? Check whether _Tillman_ has been applied, distinguished, or affected by later cases; check whether UK Government reform has progressed | Flag [CHECK CURRENCY]                 |
| **Domain**     | Analysis stays within English law; flag any inadvertent reference to US, Australian, or other law as if it were binding English authority                                        | Remove or flag [FOREIGN JURISDICTION] |
| **Confidence** | Uncertainty about borderline cases or fact-specific outcomes explicitly stated; no false certainty on findings that are genuinely judge-dependent                                | Add confidence qualifier              |

### Self-Interrogation for UNENFORCEABLE and VOID Findings

For any finding at UNENFORCEABLE or VOID, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the enforceability classification follow
logically from the cited authority? Would a High Court judge actually reach this
conclusion, or is there a tenable alternative construction of the clause?

**Pass 2 — Completeness**: Has the _Tillman_ severance possibility been fully assessed?
Has the employee-vs.-shareholder distinction been considered? Are there any facts not
yet established that could change the analysis?

**Pass 3 — Strongest Counter-Argument**: What would the employer's leading employment
counsel argue? Under what circumstances might a reasonable court enforce a version of
this covenant (even a severed version)? Mark the output with the counter-argument if
it is material.

If any pass causes doubt: revise the classification or note the uncertainty explicitly.
Mark in the Glass Box: `self_interrogation: REVISED — [reason]`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                                                         | Action                                                 |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law with clear, consistent authority (e.g., no mandatory financial compensation in English law, unlike French law)      | State with confidence                                  |
| **High**     | 0.80–0.94 | Strong binding precedent; minor variations in fact patterns                                                                     | State with brief caveat                                |
| **Probable** | 0.60–0.79 | Good authority but outcomes are fact-specific; judges have gone both ways (e.g., 12-month duration for senior executive)        | State with reasoning and key uncertainty               |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities; highly fact-dependent outcome (e.g., _Tillman_ severance success in a novel clause) | Flag for qualified legal review with both sides argued |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative (e.g., springboard injunction duration beyond 6 months without extremely strong facts)                | Do not assert; flag [UNCERTAIN]                        |

---

## Anti-Patterns

What NOT to do when drafting, amending, or enforcing English law restrictive covenants.
These are the most common failures identified by employment courts in England and Wales.

1. **No identifiable legitimate proprietary interest specified** — Generic recitals that
   the employer "wishes to protect its business interests" without identifying specific
   trade secrets, customer relationships, or other qualifying interests are worthless.
   Courts will not supply the missing justification. The covenant is void from the outset.

2. **One-size-fits-all covenants applied across all seniority levels** — A single
   standard-form covenant applied identically to the CEO and the junior sales
   administrator will be unenforceable for the junior. _Tom James v Potter_ [2025]:
   "one size fits all" globally applied restrictions were specifically criticised. Draft
   by role tier, not by employment band.

3. **Twelve-month restriction without specific justification** — Twelve months is not
   a "safe" default. It requires specific evidential justification: why does this
   particular role with this particular set of client relationships or trade secrets
   justify 12 months? If the employer cannot articulate the justification, a court cannot
   accept it. _Tom James v Potter_ [2025]: 12-month restriction void where employer could
   not justify the doubling from a previous 6-month term.

4. **Worldwide or entire-sector activity scope for a non-global employee** — "The
   Employee shall not be engaged in any capacity in the financial services industry
   anywhere in the world" is almost certainly void for anyone below senior partner
   at a global institution. The scope must reflect where the employee actually worked
   and what they actually competed in.

5. **'Any capacity' formulation without carve-outs** — Prohibiting the employee from
   working "in any capacity" for a competitor (including as a driver or receptionist)
   goes beyond protecting the identified interest. Post-_Tillman_, courts may sever the
   overbroad capacity language, but drafters should use targeted language from the outset
   (e.g., "in a role similar to or competitive with the role held during the last 12
   months of employment").

6. **Failure to include a shareholding carve-out** — Post-_Tillman_, the lack of an
   express carve-out for passive shareholdings (e.g., holding shares in a competitor as
   an investment) creates the same vulnerability as existed in _Tillman_. Include a
   standard carve-out: "This clause shall not prevent the Employee from holding up to
   3% of the issued share capital of any company listed on a recognised investment
   exchange for investment purposes only."

7. **No fresh consideration for mid-employment amendments** — Continued employment is
   not adequate consideration for new or strengthened post-termination restrictions
   added during an existing employment relationship. A simultaneous pay rise, bonus,
   or promotion must be expressly identified as the consideration for the amended
   restrictions.

8. **Garden leave clause without set-off against the PTRNC** — A 6-month garden leave
   clause followed by a 12-month non-compete produces an 18-month market exclusion.
   Without a set-off clause, an employer cannot easily demonstrate proportionality.
   Courts will scrutinise the combined period as a whole. Include: "The post-termination
   restriction period shall be reduced by any period of garden leave served."

9. **PILON clause silent on survival of post-termination covenants** — If the PILON
   clause does not expressly state that restrictive covenants survive payment in lieu
   of notice, there is uncertainty about whether the covenants run from the date of PILON
   payment or the date notice would otherwise have expired. Express survival language
   eliminates this gap.

10. **Covenant assessed at the wrong time** — Employers often attempt to justify a
    covenant by reference to the employee's seniority or access to information at the
    time of enforcement, not at the time of contracting. _Patsystems v Neilly_ [2012]:
    a covenant entered into when an employee was a junior account manager was void when
    enforcement was sought after their promotion to Director — the covenant was
    unreasonable at inception. Always re-execute covenants when an employee's role changes
    materially.

11. **Conflating PTRNC enforceability with springboard injunction availability** — An
    employer can obtain a springboard injunction even if the PTRNC is unenforceable, if
    there is evidence of misuse of confidential information or other unlawful conduct.
    Conversely, a valid PTRNC does not automatically give rise to springboard relief.
    Assess each separately. Do not advise on springboard relief based solely on
    PTRNC enforceability.

12. **Failing to act immediately on a known breach** — _Planon Ltd v Gilligan_ [2022]
    EWCA Civ 642: the Court of Appeal refused an interim injunction in part because of
    the employer's delay in taking action. By the time of the Court of Appeal hearing,
    only 4 months of a 12-month restriction remained. Delay signals that the employer
    did not view the breach as causing irreparable harm — fatal to the balance of
    convenience. Employers must act within days of discovering a breach: send a letter
    before action, obtain an undertaking, or apply to court immediately.

13. **Business-sale/shareholder covenants drafted using employment-law precedents** —
    Covenants in shareholders' agreements or business-sale agreements can be substantially
    broader than employment covenants. Using employment-contract precedents when drafting
    commercial covenants leaves the buyer under-protected. Conversely, using commercial
    precedents in an employment contract invites challenge — the employee will argue the
    commercial standard has been inappropriately imported.

14. **Tiered/cascading covenants without clear sequencing** — Tiered covenants work only
    if the drafting makes clear whether the tiers are (a) sequential alternatives (courts
    enforce the narrowest applicable) or (b) simultaneous obligations. Ambiguous tiering
    makes it harder for courts to apply _Tillman_ severance and increases the risk of the
    entire structure being struck down.

15. **Ignoring the upcoming reform risk in long-term drafting** — The UK Government's
    2025 Working Paper proposed a statutory cap of 3 months for employee non-competes.
    Although no legislation has been enacted, employers signing long-term employment
    contracts (e.g., 5-year executive contracts) should consider whether their 12-month
    covenants will still be effective for the duration of the contract. Best-practice
    drafting builds in a reduced restriction period that would remain protective even
    at a 3-month cap: ensure non-solicitation, confidentiality, and garden leave
    provisions carry the primary burden.

16. **Relying on non-compete when non-solicitation would suffice** — If the employer's
    genuine concern is poaching of key clients or recruitment of key staff, a targeted
    non-solicitation covenant is materially easier to enforce than a full non-compete,
    and courts are more receptive. Overreaching with a non-compete when the interest is
    actually narrower generates unnecessary enforceability risk.

17. **Scottish employee, English law choice-of-clause** — Choosing English law does not
    eliminate Scottish procedural advantages for the employee. If the employee is based
    in Scotland, seeking an interim interdict in the Court of Session may be harder for
    the employer under English law than under Scots law. Consider carefully which system
    provides better enforcement mechanics for the specific employee population.

---

## Writing Standards

- State every finding in active voice: "The covenant is void for want of a protectable
  interest" not "The covenant may possibly be considered void."
- Cite every material claim to a specific case, statute, or principle.
- Mark uncertain citations [VERIFY] and reformed/pending areas [CHECK CURRENCY].
- Separate findings from recommendations — never embed a recommendation inside a finding.
- Avoid softening language that obscures risk: do not say "there are some concerns" when
  the finding is UNENFORCEABLE.
- Maintain impartiality: note the strongest counter-argument for every high-severity
  finding.
- Use the 5-tier classification consistently throughout — do not mix severity language
  (e.g., "a concern" vs. "problematic") in the body when the classification table
  defines the terms precisely.

---

## External Tool Integration

### With legalcode-mcp connected (preferred)

Use legalcode-mcp to:

- Search for recent High Court and Court of Appeal decisions on restrictive covenants
  post-_Tillman_ (2019–current)
- Verify the current status of the UK Government non-compete reform Working Paper
- Check whether the targeted statutory provisions (if any) are in force
- Retrieve the current text of relevant legislation (Senior Courts Act 1981 s.37;
  any reform statute if enacted)

Save results to `/tmp/legalcode-nc-ew-research.md` before beginning analysis. Mark
legalcode-mcp sourced citations as VERIFIED in the Glass Box.

### Without legalcode-mcp

Mark all case citations and reform status references with [VERIFY] in the output.
Note in the Glass Box: `legalcode_mcp: "Not connected — all citations require
independent verification"`.

Proceed with the analysis using the legal framework set out in this skill, but advise
the user that an independent verification check is required before relying on the output.

---

## Glass Box Audit Trail

Include this YAML block at the end of every analysis output, completed for the specific
analysis:

```yaml
glass_box:
  skill_name: "legalcode-non-compete-analysis-ew"
  jurisdiction: "England & Wales"
  analysis_date: "[YYYY-MM-DD]"

  # Input summary
  document_type: "[Employment (new hire) / Employment (amendment) / Severance / Business-sale / Shareholders' agreement / Standalone deed / Other]"
  analysis_perspective: "[Employer / Employee / In-house counsel / Transactional counsel]"
  input_format: "[Full document / Clause extract / Description only]"

  # Covenant terms
  clause_duration: "[e.g., 12 months post-termination]"
  clause_geography: "[e.g., England and Wales]"
  clause_activity: "[Describe the restriction]"
  clause_compensation: "[Garden leave at full salary / Payment during restriction / None]"

  # Employee context
  employee_seniority: "[C-suite / Senior executive / Mid-level / Junior / Technical specialist / Sales/client-facing]"
  employee_access: "[Trade secrets / Customer relationships / Workforce knowledge / Specialist training / General commercial knowledge]"
  contract_date: "[YYYY-MM-DD or 'Not stated']"
  assessment_at_date_of_contract: "[Yes — context provided / Assumed — insufficient detail]"

  # Garden leave and PILON
  garden_leave_present: "[Yes — [X] months / No / Not stated]"
  garden_leave_set_off_clause: "[Yes / No / Not applicable]"
  pilon_clause: "[Present — expressly preserves PTRNCs / Present — silent on PTRNCs / Absent]"
  combined_market_exclusion: "[X months total]"

  # Analysis findings
  protectable_interest_classification: "[ESTABLISHED / ARGUABLE / ABSENT]"
  duration_classification: "[COMPLIANT / BORDERLINE / EXCESSIVE]"
  geography_classification: "[COMPLIANT / BORDERLINE / EXCESSIVE]"
  activity_classification: "[COMPLIANT / BORDERLINE / EXCESSIVE / OVERBROAD]"
  garden_leave_interaction: "[Complements / Conflicts / No set-off clause — proportionality risk / Not applicable]"
  tillman_severance_applicable: "[Yes — [specify what can be severed] / No — entire clause overbroad / Not required]"
  blue_pencil_prediction: "[Clause likely saveable after severance / Uncertain / Clause not saveable — core too broad]"
  employee_vs_shareholder_standard: "[Employment standard — strict scrutiny / Commercial standard — permissive / Spectrum — [position on spectrum]]"
  consideration_status: "[New-hire — employment constitutes consideration / Mid-employment — fresh consideration present / Mid-employment — fresh consideration absent / Not applicable]"
  springboard_exposure: "[HIGH / MODERATE / LOW / NOT APPLICABLE]"

  # Reform landscape
  uk_reform_status: "[November 2025 Working Paper — consultation closed 18 Feb 2026 — no legislation enacted]"
  future_proof_assessment: "[Would survive 3-month cap: Yes / No / Partially]"

  # Overall classification
  overall_classification: "[ENFORCEABLE / AT-RISK / PROBLEMATIC / UNENFORCEABLE / VOID]"
  confidence: "[Definite / High / Probable / Possible / Unlikely — 0.XX — rationale]"

  # Findings count
  tier_1_findings: "[count]"
  tier_2_findings: "[count]"
  tier_3_findings: "[count]"

  # Quality assurance
  citation_quality_gates: "[All passed / Gate [X] failed — revised before delivery]"
  self_interrogation: "[PASS / REVISED — [reason]]"
  legalcode_mcp: "[Connected — citations VERIFIED / Not connected — citations require independent verification]"
  citations_verified: "[X VERIFIED] / [Y UNVERIFIED — [VERIFY]]"

  # Limitations
  limitations:
    - "[UK Government reform outcome not yet enacted; analysis assumes current common law]"
    - "[Reasonableness assessed on described facts; full document review may reveal additional dimensions]"
    - "[Blue-pencil prediction is probabilistic; individual judicial assessment varies]"
    - "[Springboard injunction risk is factual; requires specific evidence of wrongdoing to pursue]"
    - "[Scotland/NI differences noted but not comprehensively analysed]"

  reviewer: "AI-assisted analysis — requires review by a qualified solicitor or barrister in England and Wales before enforcement, litigation, or advice to clients"
```

---

## Output Format Template

Deliver the analysis in this structure:

```markdown
# Restrictive Covenant Enforceability Analysis — England & Wales

**Date:** [YYYY-MM-DD]
**Perspective:** [Employer / Employee / Counsel]
**Document Type:** [Type]
**Overall Classification:** [ENFORCEABLE / AT-RISK / PROBLEMATIC / UNENFORCEABLE / VOID]
**Confidence:** [Level — 0.XX]

---

## Executive Summary

[2–4 sentences: overall classification, the one or two most important findings, and the
critical recommended action. No hedging — be direct.]

### Key Findings

- [Finding 1 — highest severity first]
- [Finding 2]
- [Finding 3]
- [...]

### Priority Actions

1. **Tier 1 (Immediate):** [Action]
2. **Tier 2 (Near-term):** [Action]
3. **Tier 3 (Consider):** [Action]

---

## Covenant Summary

| Element                             | Stated Terms                          |
| ----------------------------------- | ------------------------------------- |
| **Duration**                        | [X months post-termination]           |
| **Geographic scope**                | [Stated scope]                        |
| **Activity scope**                  | [Stated restriction]                  |
| **Compensation during restriction** | [Full salary / Garden leave / None]   |
| **Garden leave**                    | [Present — X months / Absent]         |
| **PILON clause**                    | [Present / Absent / Silent on PTRNCs] |
| **Employee seniority**              | [Role]                                |
| **Governing law**                   | [England and Wales / Other]           |
| **Contract date**                   | [Date or estimate]                    |

---

## Detailed Analysis

### Part A — Legitimate Proprietary Interest

**Interest identified:** [Yes / No / Partial]

[For each applicable category:]

**Trade Secrets / Confidential Information**

- **Assessment:** [Does the employee have access to genuine Category 3 trade secrets?]
- **Authority:** _Faccenda Chicken v Fowler_ [1987]; _Herbert Morris v Saxelby_ [1916]
- **Finding:** [ESTABLISHED / ARGUABLE / ABSENT]
- **Confidence:** [Level]

**Customer Connections**

- **Assessment:** [Degree of personal influence over customers?]
- **Finding:** [ESTABLISHED / ARGUABLE / ABSENT]
- **Confidence:** [Level]

**Workforce Stability** (if applicable)

- **Assessment:** [Senior role with poaching risk?]
- **Finding:** [ESTABLISHED / ARGUABLE / ABSENT]
- **Confidence:** [Level]

**Specialist Training** (if applicable)

- **Assessment:** [Employer-funded training with competitive value?]
- **Finding:** [ESTABLISHED / ARGUABLE / ABSENT]
- **Confidence:** [Level]

**Overall Part A Classification:** [ESTABLISHED / ARGUABLE / ABSENT]

---

### Part B — Duration Assessment

**Covenant duration:** [X months]
**Benchmark analysis:**

| Benchmark                                | Assessment                         | Status                               |
| ---------------------------------------- | ---------------------------------- | ------------------------------------ |
| ≤ 6 months (generally reasonable)        | [Compliant / Exceeds]              | [COMPLIANT / BORDERLINE]             |
| ≤ 12 months (requires justification)     | [Within / Exceeds]                 | [COMPLIANT / BORDERLINE / EXCESSIVE] |
| Proportionate to the identified interest | [Proportionate / Disproportionate] | [COMPLIANT / EXCESSIVE]              |
| Proportionate to employee seniority      | [Proportionate / Disproportionate] | [COMPLIANT / EXCESSIVE]              |

**Finding:** [COMPLIANT / BORDERLINE / EXCESSIVE]
**Authority:** [Tom James v Potter [2025]; Patsystems v Neilly [2012]; other]
**Confidence:** [Level]
**Remediation (if BORDERLINE / EXCESSIVE):** [Specific proposed duration and rationale]

---

### Part C — Geographic Scope Assessment

**Covenant scope:** [Stated scope]
**Employer's operational territory:** [Described]
**Employee's actual territory:** [Described]

[Analysis of proportionality]

**Finding:** [COMPLIANT / BORDERLINE / EXCESSIVE]
**Confidence:** [Level]
**Remediation (if BORDERLINE / EXCESSIVE):** [Proposed scope]

---

### Part D — Activity Scope Assessment

**Covenant restriction:** [Quoted language]
**Analysis:** [Specific and targeted / Moderately broad / Overbroad industry ban]

[Sub-analysis if applicable: 'any capacity' formulation; 'interested in' formulation]

**Finding:** [COMPLIANT / BORDERLINE / EXCESSIVE / OVERBROAD]
**Authority:** [Tillman v Egon Zehnder [2019]; Tom James v Potter [2025]]
**Confidence:** [Level]
**Tillman severance applicable?** [Yes — delete '[X words]' leaves enforceable core /
No — core too broad / Not required]
**Remediation (if BORDERLINE / EXCESSIVE / OVERBROAD):** [Specific revised language]

---

### Part E — Garden Leave and PILON Interaction

**Garden leave:** [Present — X months at full salary / Absent]
**Set-off clause:** [Present / Absent]
**PILON clause:** [Present — expressly preserves PTRNCs / Present — silent / Absent]
**Combined market exclusion period:** [X months]

[Analysis of combined period proportionality; Credit Suisse v Armstrong / Tullett Prebon principles]

**Finding:** [COMPLEMENTS the PTRNC / CONFLICTS with PTRNC / SET-OFF MISSING — risk /
PILON SILENT — gap identified / NO INTERACTION]
**Confidence:** [Level]
**Remediation:** [Add set-off clause / Add PILON survival language / Reduce combined period]

---

### Part F — Blue-Pencil Severance Assessment

**Elements potentially severable:** [List with basis]
**Tillman three-part test:**

- Blue pencil (deletion only): [Possible / Not possible — would require additions]
- Adequate consideration: [Satisfied / Disputed]
- No major change in overall effect: [Satisfied / Disputed — rationale]

**Prediction:** [Clause likely saveable / Uncertain / Clause not saveable]
**Confidence:** [Level]
**Authority:** _Tillman v Egon Zehnder_ [2019] UKSC 32; _Prophet PLC v Huggett_ [2014]

---

### Part G — Employee vs. Shareholder/Commercial Covenant

**Standard applicable:** [Employment — strict scrutiny / Commercial — permissive /
Spectrum — position and basis]
**Equity stake (if any):** [X% / None]
**Basis for standard applied:** [Authority]

---

### Part H — Consideration

**Type:** [New-hire / Mid-employment amendment]
**Consideration analysis:** [Analysis of adequacy]
**Finding:** [Consideration PRESENT / ABSENT / UNCERTAIN]
**Confidence:** [Level]

---

### Part I — Springboard Injunction Context

**Springboard exposure:** [HIGH / MODERATE / LOW / NOT APPLICABLE]
**Basis:** [Indicators of wrongdoing present / No evidence of wrongdoing]
**Note:** [Springboard remedy is independent of PTRNC enforceability; requires separate
assessment with specific evidence]

---

## FINDINGS SUMMARY

### Tier 1 — Non-Negotiable for Enforceability

| #     | Finding   | Classification         | Part   |
| ----- | --------- | ---------------------- | ------ |
| 1     | [Finding] | [VOID / UNENFORCEABLE] | [Part] |
| [...] |           |                        |        |

### Tier 2 — Significant Risk

| #     | Finding   | Classification          | Part   |
| ----- | --------- | ----------------------- | ------ |
| 1     | [Finding] | [PROBLEMATIC / AT-RISK] | [Part] |
| [...] |           |                         |        |

### Tier 3 — Optimisation

| #     | Finding   | Classification    | Part   |
| ----- | --------- | ----------------- | ------ |
| 1     | [Finding] | [AT-RISK — minor] | [Part] |
| [...] |           |                   |        |

---

## OVERALL CLASSIFICATION

| Dimension                           | Classification                                                   | Confidence         |
| ----------------------------------- | ---------------------------------------------------------------- | ------------------ |
| **Legitimate proprietary interest** | [ESTABLISHED / ARGUABLE / ABSENT]                                | [Level]            |
| **Duration**                        | [COMPLIANT / BORDERLINE / EXCESSIVE]                             | [Level]            |
| **Geographic scope**                | [COMPLIANT / BORDERLINE / EXCESSIVE]                             | [Level]            |
| **Activity scope**                  | [COMPLIANT / BORDERLINE / EXCESSIVE / OVERBROAD]                 | [Level]            |
| **Garden leave coordination**       | [Appropriate / SET-OFF MISSING / PILON GAP]                      | [Level]            |
| **Tillman severance available**     | [Yes / No / Partial]                                             | [Level]            |
| **Consideration**                   | [PRESENT / ABSENT / UNCERTAIN]                                   | [Level]            |
| **OVERALL**                         | **[ENFORCEABLE / AT-RISK / PROBLEMATIC / UNENFORCEABLE / VOID]** | **[Level — 0.XX]** |

---

## REMEDIATION RECOMMENDATIONS

### Tier 1 — Immediate (Non-Negotiable for Enforceability)

**[Finding title]**

- **Current position:** [Quote or describe the deficiency]
- **Legal basis:** [Case/principle]
- **Risk:** [Specific consequence of non-remediation]
- **Proposed remedy:** [Specific revised language or structural change]
- **Priority:** Tier 1

### Tier 2 — Near-Term (Significant Risk)

**[Finding title]**

- **Current position:** [Quote or describe]
- **Legal basis:** [Case/principle]
- **Risk:** [Consequence]
- **Proposed remedy:** [Specific revision]
- **Priority:** Tier 2

### Tier 3 — Consider (Optimisation)

**[Finding title]**

- **Current position:** [Quote or describe]
- **Risk:** [Consequence if not addressed]
- **Proposed revision:** [Suggested change]
- **Priority:** Tier 3

---

## ANTI-PATTERN CHECKLIST

Rate each: ✅ Present and adequate | ⚠️ Present but incomplete | ❌ Absent

|     | Element                                                                 | Status | Notes |
| --- | ----------------------------------------------------------------------- | ------ | ----- |
| 1   | Legitimate proprietary interest specifically identified in the covenant |        |       |
| 2   | Activity scope limited to genuinely competitive roles/clients           |        |       |
| 3   | Geographic scope linked to employer's actual market footprint           |        |       |
| 4   | Duration within reasonable range for seniority and business interest    |        |       |
| 5   | Role-specific drafting (not one-size-fits-all)                          |        |       |
| 6   | Fresh consideration provided (if mid-employment amendment)              |        |       |
| 7   | Shareholding carve-out included                                         |        |       |
| 8   | Garden leave set-off clause present                                     |        |       |
| 9   | PILON clause expressly preserves post-termination covenants             |        |       |
| 10  | Tillman-safe drafting (cascading tiers / severable structure)           |        |       |
| 11  | Tiered covenants clearly sequenced (not ambiguous)                      |        |       |
| 12  | Covenant reassessed after any material role change                      |        |       |
| 13  | Springboard injunction risk independently assessed                      |        |       |
| 14  | Enforcement plan prepared (letter before action ready)                  |        |       |
| 15  | Reform risk considered (clause viable at 3 months if reform enacted)    |        |       |

---

## CASE LAW REFERENCE TABLE

| Case                                     | Citation              | Key Principle                                                                                    | Relevance to This Analysis                |
| ---------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| _Herbert Morris v Saxelby_               | [1916] 1 AC 688 (HL)  | Defines legitimate interest categories; cannot protect mere competition                          | [Applies / Not directly applicable]       |
| _Faccenda Chicken v Fowler_              | [1987] Ch 117 (CA)    | Three-tier information hierarchy; post-employment only trade secrets protected without covenant  | [Applies / Not directly applicable]       |
| _TFS Derivatives v Morgan_               | [2004] EWHC 3181 (QB) | Three-stage reasonableness test; garden leave and PTRNC not mutually exclusive                   | [Applies]                                 |
| _Credit Suisse Asset Mgmt v Armstrong_   | [1996] IRLR 450 (CA)  | No automatic garden leave credit against PTRNC; exceptional cases only                           | [Applies / Not applicable]                |
| _Tullett Prebon v BGC Brokers_           | [2011] EWCA Civ 131   | Combined market exclusion (garden leave + PTRNC) assessed as a whole                             | [Applies / Not applicable]                |
| _Beckett Investment Mgmt v Hall_         | [2007] EWCA Civ 613   | Legitimate interest test; cascading/tiered covenants; blue-pencil foundation                     | [Applies]                                 |
| _Prophet PLC v Huggett_                  | [2014] EWCA Civ 1013  | Blue pencil deletes only; court cannot add words to repair defective clause                      | [Applies / Not applicable]                |
| _Patsystems Holding v Neilly_            | [2012] EWHC 2609 (QB) | Reasonableness assessed at date of contracting; subsequent promotion cannot save void covenant   | [Applies / Not applicable]                |
| _Bartholomews Agri Food v Thornton_      | [2016] EWHC 648 (QB)  | Non-solicitation void where employee had no real customer relationships at time of contracting   | [Applies / Not applicable]                |
| _Tillman v Egon Zehnder_                 | [2019] UKSC 32        | Overruled _Attwood_; Tillman three-part test for severance within standalone covenant            | [Applies]                                 |
| _Guest Services Worldwide v Shelmerdine_ | [2020] EWCA Civ 85    | SHA covenants bind after employment ends; commercial standard applied to shareholder-employee    | [Applies / Not applicable]                |
| _Square Global v Leonard_                | [2020] EWHC (QB)      | No set-off required; garden leave and PTRNC can run consecutively without breach                 | [Applies / Not applicable]                |
| _QBE Management Services v Dymoke_       | [2012] EWHC 80 (QB)   | Springboard injunction — team move; duration calibrated to actual competitive advantage          | [Applies to springboard / Not applicable] |
| _Harcus Sinclair v Your Lawyers_         | [2021] UKSC 32        | Commercial 6-year non-compete enforceable; unstated party intentions relevant                    | [Applies / Not applicable]                |
| _Quantum Actuarial v Quantum Advisory_   | [2021] EWCA Civ 227   | 99-year commercial covenant upheld; freedom to contract in commercial context                    | [Applies / Not applicable]                |
| _Law by Design v Ali_                    | [2022] IRLR 610 (HC)  | Small equity (3%) does not shift to commercial standard; employment contract NC enforced         | [Applies / Not applicable]                |
| _Planon Ltd v Gilligan_                  | [2022] EWCA Civ 642   | No presumption of injunctive relief; delay potentially fatal; balance of convenience             | [Applies to enforcement]                  |
| _Boydell v NZP Ltd_                      | [2023] EWCA Civ 373   | Tillman severance applied; "fantastical consequences" principle limits over-literal construction | [Applies / Not applicable]                |
| _Aquinas Education v Miller_             | [2023] (HC)           | Springboard refused; continuing benefit must be evidenced, not speculative                       | [Applies to springboard / Not applicable] |
| _Tom James UK Ltd v Potter_              | [2025] EWHC 2873 (KB) | 12-month NC void: overbroad, non-tailored, unjustified, non-solicitation available               | [Applies]                                 |

---

## UK GOVERNMENT REFORM NOTE

The November 2025 Working Paper (_Options for Reform of Non-Compete Clauses in
Employment Contracts_) proposes four reform options:

| Option                    | Description                                            | Impact if Enacted                                                             |
| ------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Statutory duration limits | 3-month cap (flat) or variable by employer size        | Existing covenants beyond 3 months would be void for new contracts            |
| Complete ban              | All employment non-competes void                       | Shifts burden entirely to non-solicitation, garden leave, and confidentiality |
| Salary threshold ban      | Non-competes void for workers below a specified salary | Creates two-tier market                                                       |
| Hybrid                    | Salary threshold + 3-month cap for higher earners      | Most likely legislative form if reform proceeds                               |

**Current status**: Consultation closed 18 February 2026. No legislation enacted.
Requires primary legislation. Reform is not imminent but planning for a 3-month cap
scenario is prudent for long-term employment drafting.

**Recommended action for current drafting**: Structure covenants so that:

- Non-solicitation, non-dealing, and garden leave provisions carry the primary protective
  burden independently of the non-compete.
- Any non-compete beyond 3 months is specifically justified and targeted so that, in
  the event of reform, the core protection is not lost.

---

## LOCALIZATION NOTES

**Scotland**: Applies the same restraint-of-trade doctrine but:

- Interim interdict (the Scottish equivalent of an interim injunction) is easier to
  obtain — the employer need only show a _prima facie_ case (lower threshold than
  England's "serious question to be tried" under _American Cyanamid_).
- If the agreement is governed by Scots law or the employee is primarily Scotland-based,
  engage Scottish employment counsel.

**Northern Ireland**: Applies English common law restraint of trade principles; English
authorities are directly persuasive. The court system is separate (Belfast High Court).
Differences are minor for substantive enforceability analysis.

**Channel Islands and Crown Dependencies**: Not subject to English restraint-of-trade
doctrine. Guernsey, Jersey, and Isle of Man apply their own legal frameworks; English
analysis is of limited (if any) value.

---

## PROVENANCE

Created by Legalcode (2026-03-21). Mode A original synthesis. Research sourced from:
web-backed research pipeline (2-agent: Structural Analyst + Legal Research Agent);
case law research covering Herbert Morris v Saxelby [1916] through Tom James v Potter
[2025]; UK Government Working Paper on Non-Compete Reform (November 2025); practitioner
guidance from Mayer Brown (2024), Lewis Silkin, Freshfields, Addleshaw Goddard, Taylor
Wessing, Farore Law, and Littleton Chambers. All citations carry [VERIFY] requirement;
verify against legislation.gov.uk, BAILII, Westlaw UK, and Lexis+ before relying on
them. This skill is a jurisdiction-specific England & Wales variant complementing
`legalcode-non-compete-analysis` (cross-jurisdictional router). Routes to:
`legalcode-non-compete-analysis` for US/DE/FR/CN coverage;
`legalcode-employment-agreement-review` for full contract review;
`legalcode-uk-employment-tribunal-claim` for ET claim preparation.
```
