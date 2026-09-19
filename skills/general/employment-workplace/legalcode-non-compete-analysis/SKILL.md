---
name: legalcode-non-compete-analysis
description: Cross-jurisdictional router for non-compete enforceability analysis covering US (all 50 states
  + state-by-state variation, California ban, Colorado salary thresholds, FTC landscape post-Ryan LLC
  v. FTC vacatur), UK (common law reasonableness test, garden leave, protectable interests, blue-pencil
  doctrine, 2023/2024 reform landscape), Germany (HGB §§ 74-75a Nachvertragliches Wettbewerbsverbot, mandatory
  Karenzentschädigung 50% minimum, 2-year cap, unverbindlich vs. nichtig distinction), France (clause
  de non-concurrence, five cumulative Cour de cassation criteria including mandatory contrepartie financière,
  employer waiver mechanics, collective bargaining agreement floors), and China (Labor Contract Law Arts.
  23-24, mandatory monthly economic compensation, senior management/senior technical staff scope, Supreme
  Court Interpretation III, 2-year cap).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Cross-jurisdictional router for non-compete enforceability analysis covering US (all 50 states + state-by-state variation, California ban, Colorado salary thresholds, FTC landscape post-Ryan LLC v. FTC vacatur), UK (common law reasonableness test, garden leave, protectable interests, blue-pencil doctrine, 2023/2024 reform landscape), Germany (HGB §§ 74-75a Nachvertragliches Wettbewerbsverbot, mandatory Karenzentschädigung 50% minimum, 2-year cap, unverbindlich vs. nichtig distinction), France (clause de non-concurrence, five cumulative Cour de cassation criteria including mandatory contrepartie financière, employer waiver mechanics, collective bargaining agreement floors), and China (Labor Contract Law Arts. 23-24, mandatory monthly economic compensation, senior management/senior technical staff scope, Supreme Court Interpretation III, 2-year cap). Use when reviewing a non-compete clause, post-employment restriction, covenant not to compete, restrictive covenant, garden leave provision, or competition prohibition in any employment agreement, executive contract, severance agreement, or business-sale agreement across any of these five major jurisdictions. Routes to jurisdiction-specific deep-analysis skills where available. Produces ENFORCEABLE/AT-RISK/NON-COMPLIANT/VOID classification with confidence-scored enforceability assessment, actionable remediation steps, and auditable Glass Box trail. Handles multi-jurisdiction analysis for cross-border employee populations.


# Legalcode Non-Compete Analysis — Cross-Jurisdictional Router

> **Disclaimer**: This skill provides a framework for AI-assisted non-compete enforceability
> analysis across multiple jurisdictions. It does not constitute legal advice. All outputs
> require review by a qualified employment lawyer licensed in the relevant jurisdiction(s)
> before relying on them for any enforcement, litigation, compliance, or negotiation
> decision. Non-compete law changes frequently — salary thresholds, statutory bans, and
> case law evolve year to year; verify current applicability before acting. Statutory and
> case law references cited from memory carry hallucination risk — verify against
> authoritative sources (state statutes, Westlaw, Lexis, official government portals)
> before use. This skill does not substitute for individual legal advice.

---

## Purpose and Scope

This skill analyses whether a non-compete clause is enforceable under the applicable
jurisdiction's law, identifies the specific deficiencies that reduce enforceability,
generates confidence-scored assessments, and routes to jurisdiction-specific deep-analysis
skills where available.

**Covers:**

- Jurisdiction detection and triage: US, UK, Germany, France, China, multi-jurisdiction
- US analysis: 6-state total-ban screening, salary threshold compliance, reasonableness
  testing, blue-pencil/red-pencil doctrine, garden leave, FTC landscape
  → Routes to `legalcode-us-state-non-compete-analysis` for full 50-state analysis
  → Routes to `legalcode-non-compete-enforceability` for US detailed enforceability matrix
- UK analysis: Common law reasonableness test, protectable interests doctrine, garden
  leave mechanics, blue-pencil power, 2023 reform proposal status
- Germany analysis: HGB §§ 74-75a mandatory Karenzentschädigung framework,
  unverbindlich vs. nichtig consequences, employer waiver mechanics, BAG case law
- France analysis: Five cumulative Cour de cassation criteria (incl. mandatory
  contrepartie financière), employer waiver procedure, collective bargaining agreement
  overlay, consequences of non-payment
- China analysis: Labor Contract Law Arts. 23-24, who-can-be-bound scope, mandatory
  monthly compensation, SPC Interpretation III breach consequences
- Multi-jurisdiction analysis: Cross-border populations, governing-law override risks,
  jurisdiction stacking

**Does not:**

- Provide personal legal advice or guarantee court outcomes — courts apply fact-specific tests
- Perform full 50-state US analysis (route to `legalcode-us-state-non-compete-analysis`)
- Analyse non-solicitation of customers, non-solicitation of employees, or NDA covenants
  in isolation (see `legalcode-nda-triage`, `legalcode-employment-agreement-review`)
- Cover jurisdictions outside US/UK/DE/FR/CN as primary analysis
- Apply to non-compete provisions in franchise agreements (different legal framework —
  see `legalcode-franchise-agreement-review`)
- Apply to commercial non-competes in business-sale agreements without noting the
  different (more permissive) standard that applies post-acquisition

**Related skills:**

- `legalcode-us-state-non-compete-analysis` — full 50-state US analysis
- `legalcode-non-compete-enforceability` — US detailed enforceability matrix + garden leave
- `legalcode-non-compete-analysis-is` — Iceland-specific non-compete analysis
- `legalcode-employment-agreement-review` — full employment agreement clause-by-clause review
- `legalcode-nda-triage` — NDA and non-disclosure covenant review
- `legalcode-severance-agreement-review` — severance agreement with non-compete interaction

---

## Jurisdiction and Governing Law

Non-compete law is governed almost entirely by **national or sub-national law**. There is
no international treaty or cross-border harmonisation framework. The jurisdiction applied
depends on:

1. **Contractual choice of law** — the governing law clause in the agreement
2. **Employee's work location** — often overrides the contractual choice in employment
   (especially critical in the US and Germany)
3. **Mandatory employment law** — many jurisdictions impose non-compete requirements as
   mandatory employment law that cannot be waived by contract

**Critical principle**: An employer cannot escape a jurisdiction's non-compete protections
by choosing the law of a less-restrictive jurisdiction. Germany's mandatory HGB rules,
France's mandatory compensation requirement, California's complete ban, and China's Labor
Contract Law all apply regardless of a contrary choice-of-law clause when they constitute
mandatory employment law provisions.

**Routing matrix by jurisdiction:**

| Jurisdiction           | Primary Legal Framework                                | Key Mandatory Element                            | Deep-Skill Available                      |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------- |
| **US** (all states)    | State employment law; FTC Act Section 5                | State-specific; CA/MN/ND/OK/WY/MT ban            | `legalcode-us-state-non-compete-analysis` |
| **UK** (E&W/Scotland)  | Common law restraint of trade doctrine                 | None mandatory; reasonableness test              | This skill (full analysis)                |
| **Germany**            | HGB §§ 74-75a (and statutory analogs)                  | Karenzentschädigung ≥ 50% remuneration           | This skill (full analysis)                |
| **France**             | Cour de cassation social chamber case law              | Contrepartie financière (mandatory compensation) | This skill (full analysis)                |
| **China**              | Labor Contract Law Arts. 23-24; SPC Interpretation III | Monthly economic compensation                    | This skill (full analysis)                |
| **Multi-jurisdiction** | Stacking of all applicable laws                        | Most protective applies                          | This skill                                |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The jurisdiction is ambiguous or the employee works across multiple jurisdictions
- The context is employer or employee perspective (analysis differs materially)
- The document type may affect which legal framework applies
- Governing law and work location diverge

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

### Step 1: Accept the Clause or Agreement

Accept the non-compete provision in any of these formats:

- **Full agreement**: Employment contract, executive offer letter, standalone restrictive
  covenant agreement, or severance agreement — paste full text or provide file path
- **Clause extract**: The non-compete provision extracted from a larger document
- **Summary or description**: A description of the key terms (duration, geography,
  activity scope, compensation) if the full text is not available

If only a summary is provided, note that the analysis is based on described terms and
actual enforceability may differ once the full clause language is reviewed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user (skip questions already answered):

1. **Jurisdiction(s)**: Which jurisdiction(s) should this non-compete be analysed under?
   - Options: United States (specify state(s)), United Kingdom, Germany, France, China,
     Multiple jurisdictions (specify), Unknown — help me determine
   - _Why this matters_: The entire analysis methodology and outcome change dramatically
     by jurisdiction. A clause that is void in Germany for lacking compensation may be
     enforceable in the UK.

2. **Perspective**: Whose interests should the analysis serve?
   - Options: Employer (drafting/enforcement), Employee (challenge/exit planning),
     In-house counsel (both sides, risk assessment), Transactional attorney (M&A context)
   - _Why this matters_: The same clause requires different outputs — enforcement risk
     for employers vs. exit strategy for employees.

3. **Context/Document type**: What document does the non-compete appear in?
   - Options: Employment agreement (new hire), Mid-employment amendment,
     Executive/C-suite agreement, Severance/separation agreement, Acquisition-related
     agreement (business sale), Standalone restrictive covenant agreement, Other
   - _Why this matters_: Courts apply different standards based on context — acquisition
     non-competes receive more latitude; mid-employment amendments require fresh
     consideration in most jurisdictions.

4. **Employee role and seniority** (if known):
   - Free text. Prompt: "Describe the employee's role, seniority, salary (approximate),
     and the nature of their access to confidential information or customer relationships."
   - _Why this matters_: Germany's HGB applies to Handlungsgehilfen; France's Cour de
     cassation criteria require necessity linked to the employee's specific role; China
     limits scope to senior management and technical staff; US salary thresholds
     apply in 12+ states.

5. **Clause terms** (if not already in the document provided):
   - Duration (e.g., "12 months post-termination")
   - Geographic scope (e.g., "within 50 miles of any office location")
   - Activity restriction (e.g., "may not work for any competitor")
   - Compensation provision (e.g., "no additional compensation" or "€500/month")
   - Any garden leave provision

If the user provides partial context, proceed with what is available and **state
assumptions explicitly** before analysis.

### Step 3: Jurisdiction Detection and Routing Decision

Based on the Step 2 responses:

**3a. Confirm Jurisdiction(s)**

Identify:

1. The contractual choice-of-law clause (if any)
2. The employee's primary work location
3. Whether a mandatory-law jurisdiction override applies

**3b. Routing Decision**

| If jurisdiction is...  | Then...                                                                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **US — single state**  | Perform preliminary assessment (Step 5), then route to `legalcode-us-state-non-compete-analysis` for full 50-state analysis                                 |
| **US — multi-state**   | Perform preliminary assessment, identify most restrictive state (especially if CA/MN/ND/OK/WY/MT apply), route to `legalcode-us-state-non-compete-analysis` |
| **UK**                 | Proceed with Step 5 UK analysis in this skill                                                                                                               |
| **Germany**            | Proceed with Step 5 Germany analysis in this skill                                                                                                          |
| **France**             | Proceed with Step 5 France analysis in this skill                                                                                                           |
| **China**              | Proceed with Step 5 China analysis in this skill                                                                                                            |
| **Multi-jurisdiction** | Analyse each jurisdiction in Step 5, identify cross-border risks in Step 6                                                                                  |
| **Unknown**            | Apply Step 4 jurisdiction detection protocol                                                                                                                |

**⟁ CLARIFY** — If the contractual governing law differs from the employee's work
location jurisdiction:

- Inform the user of the conflict and which jurisdiction is likely to govern (mandatory
  employment law typically overrides the contractual choice)
- Ask: "The agreement states [X law] governs, but the employee primarily works in [Y].
  In employment law, the mandatory rules of [Y] will likely apply regardless of the
  choice-of-law clause. Should I analyse under [Y], [X], or both?"

### Step 4: Jurisdiction Detection Protocol

If jurisdiction is unclear, apply these detection steps:

1. **Contract language**: Identify any governing law or jurisdiction clause
2. **Company details**: Note the employer's country of incorporation and principal place
   of business
3. **Employee details**: Note any stated work location, address, or office location
4. **Currency and terminology**: Local-language terms or local currency provide clues
5. **Statutory references**: Any cited law reveals the drafting jurisdiction

If jurisdiction cannot be determined, analyse under all candidate jurisdictions and
flag the ambiguity as a material enforceability risk.

### Step 5: Jurisdiction-Specific Enforceability Analysis

Apply the full analysis for each identified jurisdiction. The analysis for each
jurisdiction is structured as:

- Legal framework overview
- Mandatory validity requirements (each requirement checked against the clause)
- Enforceability factors (scored)
- Classification (ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID)
- Specific deficiencies and remediation

---

### 5-US: United States Analysis

#### Legal Framework

Non-compete law in the US is **entirely state law**. The FTC's April 2024 non-compete
rule was vacated by Ryan LLC v. FTC (N.D. Tex. Aug. 20, 2024) and never took effect;
the FTC formally acceded to vacatur on September 5, 2025. The FTC pursues targeted
Section 5 enforcement against coercive, overbroad agreements.

**Key principle**: Work location governs enforceability and may override the contractual
choice of law (especially California — see SB 699 extraterritorial reach).

#### Preliminary US Screening

**Step US-1: Ban-state check**

| State        | Status                                                   | Key Statute                                                               |
| ------------ | -------------------------------------------------------- | ------------------------------------------------------------------------- |
| California   | **VOID** — complete ban                                  | Bus. & Prof. Code § 16600; SB 699/AB 1076 (2024) — extraterritorial reach |
| Minnesota    | **VOID** — complete ban (July 2023)                      | Minn. Stat. § 181.988                                                     |
| North Dakota | **VOID** — complete ban                                  | N.D. Cent. Code § 9-08-06                                                 |
| Oklahoma     | **VOID** — complete ban                                  | Okla. Stat. tit. 15 § 219A                                                |
| Wyoming      | **VOID** — complete ban (July 2025)                      | Wyo. Stat. § 1-23-106 [VERIFY effective date]                             |
| Montana      | **VOID** — post-probation ban                            | Mont. Code § 28-2-703                                                     |
| DC           | **VOID** — ban for workers ≤ $150,000 [VERIFY threshold] | DC Code § 32-581.02                                                       |

If the employee works in any ban state → classify immediately as **VOID** and note that
the ban overrides the choice-of-law clause (California SB 699 extends to agreements
signed or performed in California regardless of stated governing law).

**Step US-2: Salary threshold check**

If not in a ban state, check whether the employee's salary meets the jurisdiction's
minimum income threshold for non-compete validity. Key thresholds [VERIFY current
figures annually]:

| State         | Threshold (approx., verify) | Exception                                 |
| ------------- | --------------------------- | ----------------------------------------- |
| Colorado      | ~$127,000 (2025)            | ~$76,000 for restricted activity [VERIFY] |
| Illinois      | $75,000                     | Mid-level managers                        |
| Washington    | ~$123,000 (2025)            | [VERIFY]                                  |
| Oregon        | ~$116,000 (2025)            | [VERIFY]                                  |
| DC            | ~$150,000 (2025)            | [VERIFY]                                  |
| Virginia      | ~$76,000 (2025)             | [VERIFY]                                  |
| Nevada        | $25.00/hour                 | [VERIFY]                                  |
| Maine         | —                           | Advance notice requirement                |
| Maryland      | $15/hour                    | [VERIFY]                                  |
| New Hampshire | ~$25/hour                   | [VERIFY]                                  |
| Rhode Island  | $100/hour                   | [VERIFY]                                  |

If salary is below the applicable threshold → classify as **NON-COMPLIANT** with note
that the non-compete is unenforceable regardless of other terms.

**Step US-3: Reasonableness assessment**

For non-ban, above-threshold clauses, apply the three-factor reasonableness test:

| Factor                       | Question                                                                                                                          | Common Outer Limits                                                |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Legitimate business interest | Does the employer have a protectable interest — trade secrets, confidential information, customer goodwill, specialized training? | Generic "competitive advantage" insufficient in most states        |
| Geographic scope             | Is the restriction limited to where the employer actually competes?                                                               | Nationwide bans often struck down unless truly national operations |
| Duration                     | Is the restraint period proportionate to the interest protected?                                                                  | >2 years is suspect in most states; >1 year is contested in some   |
| Activity scope               | Is the restricted activity limited to what the employee actually did or competed in?                                              | Prohibiting employment in entire industry is overbroad             |

**Step US-4: Reformation doctrine**

Assess whether the applicable state applies:

- **Blue-pencil** (strikes only unenforceable terms, enforces remainder): FL, TX, ID,
  and others
- **Reformation** (rewrites to make enforceable): majority approach in most states
- **Red-pencil** (strikes entire agreement if any term is overbroad): CA, MN, ND, OK

**Routing instruction:**

> For complete US analysis including the full 50-state matrix, salary threshold
> verification, consideration analysis, garden leave mechanics, FTC Section 5 landscape,
> and industry-specific exemptions, route to:
> **`legalcode-us-state-non-compete-analysis`**
>
> Alternatively, for the full US enforceability risk matrix with remediation redlines:
> **`legalcode-non-compete-enforceability`**

---

### 5-UK: United Kingdom Analysis (England & Wales)

#### Legal Framework

UK non-compete enforcement is governed by the **common law restraint of trade doctrine**.
There is no statute specifically governing post-employment non-competes. The employer
must establish that the restriction is:

1. Justified by a **legitimate protectable interest**
2. **No wider than reasonably necessary** to protect that interest
3. **Not contrary to the public interest**

The burden lies on the employer to justify enforcement. Courts construe restrictions
strictly against the party who imposed them.

**Scotland**: Applies broadly similar common law principles but is a distinct legal system.
Scottish courts may apply slightly different considerations on public interest and
proportionality — for Scottish-law contracts, note this distinction. [VERIFY with
Scots law counsel for Scotland-governed agreements]

#### Mandatory Validity Requirements

| Requirement                            | Check Against Clause                                                                                                                          | Status if Failed                           |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Legitimate protectable interest exists | Is there trade secrets, confidential information, customer connections, or workforce stability?                                               | No interest → not enforceable              |
| Restriction no wider than necessary    | Duration, geography, activity scope each checked                                                                                              | Overbroad → courts may blue-pencil or void |
| Not against public interest            | Extreme restrictions prevent earning a living                                                                                                 | Void as contrary to public policy          |
| Agreement supported by consideration   | Non-compete must be supported by consideration (employment itself is sufficient at hire; post-employment amendments need fresh consideration) | No consideration → unenforceable           |

**Note — No mandatory compensation**: Unlike Germany and France, UK law does **not**
require the employer to pay compensation during the restraint period. This is a major
distinction. Garden leave arrangements (paying full salary during notice) are the preferred
UK mechanism to manage non-compete risk.

#### Legitimate Protectable Interests

Courts recognise four categories of protectable interests:

| Category                                       | Description                                                                   | Notes                                                                        |
| ---------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Trade secrets and confidential information** | Genuinely confidential business information the employee possesses            | Broad NDA clause does not automatically justify non-compete                  |
| **Customer connections**                       | Employee had direct, meaningful contact with customers and personal influence | Mere acquaintance with customer list insufficient                            |
| **Workforce stability**                        | Preventing mass recruitment of key staff                                      | More permissive — non-solicitation easier to justify than non-compete        |
| **Investment in training**                     | Employer invested significantly in specialist training                        | Only justifies if employee could immediately exploit training for competitor |

**Key case principles:**

- _Beckett Investment Management Group v Hall_ [2007] EWCA Civ 613: employer must identify
  the specific protectable interest; generic restriction cannot stand [VERIFY citation]
- _TFS Derivatives Ltd v Morgan_ [2004] EWHC 3181 (QB): customer connections justified
  non-compete for financial services sales employee [VERIFY citation]
- _Prophet plc v Huggett_ [2014] EWCA Civ 1013: blue-pencil power demonstrated [VERIFY]

#### Reasonableness of Duration

| Duration    | Assessment                                                                     |
| ----------- | ------------------------------------------------------------------------------ |
| ≤ 3 months  | Very likely reasonable; courts rarely challenge                                |
| 3–6 months  | Generally reasonable if legitimate interest exists                             |
| 6–12 months | Scrutinised more closely; requires strong interest and senior role             |
| 12+ months  | Difficult to justify; rare to survive unless trade secret access + senior role |
| > 24 months | Almost certainly unreasonable; would require extraordinary circumstances       |

**2025/2026 UK Reform Landscape** [VERIFY current status]:
The UK Government published a Working Paper in November 2025 seeking views on several
options: a universal statutory cap, a tiered cap by company size (250+ employees vs.
smaller), sector-based differentiation, or outright bans for lower-paid workers. The
consultation closed **February 18, 2026**. As of March 2026, no final policy has been
announced. The current common law reasonableness test remains in force. Monitor for
secondary legislation following the February 2026 consultation response.

**Previous history**: The Conservative government proposed a 3-month cap in May 2023
but took no action before the July 2024 election.

#### Reasonableness of Geographic Scope

- **UK-wide**: Justifiable for senior executives at national businesses; questionable
  for regional employees
- **Region-specific**: More likely to survive for lower-level roles
- **No geographic limit**: Highly suspect; courts may strike entire restriction
- **Industry-wide**: Near-impossible to justify unless operating in very narrow market

#### Activity Scope Analysis

Courts assess whether the prohibited activity is:

- **Directly competitive**: Working for a named list of competitors — more defensible
- **Industry-wide ban**: "Any business in the same sector" — difficult to justify for
  anyone below C-suite level
- **Specific client restriction**: Non-dealing/non-solicitation of named clients — most
  defensible and preferred over blanket non-compete

#### Blue-Pencil Doctrine (England & Wales)

English courts have the power to "blue-pencil" (sever) unenforceable portions of a
restriction, provided:

- The remaining words form a sensible and complete restriction
- The remaining restriction is itself enforceable
- The severance does not effectively rewrite the clause

Courts will **not** rewrite clauses — they can strike words but cannot add them
(_Attwood v Lamont_ [1920] principle, qualified by _Beckett v Hall_). If the restriction
is fundamentally overbroad, the entire clause may be void.

#### Garden Leave and PILON Interaction

UK employers frequently include **garden leave clauses** — allowing the employer to place
the employee on full-pay leave during notice, preventing access to clients or colleagues.

Key garden leave principles:

- Garden leave pay counts against any subsequent non-compete period in practice
  (though no mandatory set-off unless contractually stated)
- Employers who fail to implement garden leave when entitled to do so lose some goodwill
  in court when later seeking to enforce a non-compete
- _Provident Financial Group plc v Hayward_ [1989] ICR 160: garden leave enforceable
  as independent contractual right [VERIFY citation]

**If both garden leave and non-compete are present**: The combined duration should not
exceed what is necessary. Courts view a 6-month garden leave + 12-month non-compete
period sceptically.

**PILON (Payment in Lieu of Notice) — Critical Distinction from Garden Leave:**

| Aspect                | Garden Leave                                    | PILON                                              |
| --------------------- | ----------------------------------------------- | -------------------------------------------------- |
| Employment status     | Remains employed through notice                 | Terminates immediately on PILON payment            |
| Restrictive covenants | Continue for full notice period                 | May end on payment unless drafting preserves them  |
| Non-compete duration  | Starts after notice period ends                 | Typically starts from PILON payment date           |
| Combined effect       | 6-month GL + 12-month NC = 18-month restriction | 6-month PILON + 12-month NC = 12-month restriction |

**Drafting risk**: If a PILON clause is silent on whether restrictive covenants survive,
courts may infer they end with employment. If the employer **wrongfully dismisses** the
employee (repudiatory breach), the employee may be released from all post-employment
restrictions. Always draft PILON clauses to expressly preserve and define the running of
non-compete restrictions.

**Scotland (material difference)**: Scottish courts apply a lower threshold for interim
injunctions (interdict) — an employer need only show a **prima facie case** (possible
case), not a "serious question to be tried." This makes interim enforcement substantially
easier for employers in Scotland than in England and Wales.

---

### 5-DE: Germany Analysis

#### Legal Framework

German non-compete law for employees is governed by the **Handelsgesetzbuch (HGB —
Commercial Code), §§ 74-75a**, extended to all employees by the principle that at
minimum the same protections apply. These provisions are **mandatory** — parties cannot
derogate from them to the employee's detriment.

The German system is fundamentally different from the UK: **the employer must pay
compensation** (Karenzentschädigung) during the entire restraint period. A non-compete
without adequate compensation is either unverbindlich (non-binding at employee's option)
or nichtig (void).

#### Mandatory Validity Requirements

**All requirements must be met for the non-compete to be binding:**

| Requirement                                               | Legal Basis  | Check                                                                                                  | Consequence if Failed                                              |
| --------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **Written form**                                          | HGB § 74(1)  | Agreement must be in writing, signed by both parties                                                   | Void (nichtig)                                                     |
| **Separate document or signed copy to employee**          | HGB § 74(1)  | Employer must provide employee with signed copy                                                        | Void if not provided                                               |
| **Karenzentschädigung ≥ 50% of most recent remuneration** | HGB § 74(2)  | Annual compensation promised ≥ 50% of last full annual contractual compensation (Gesamtvergütung)      | Unverbindlich (see below)                                          |
| **Maximum 2-year duration**                               | HGB § 74a(1) | Post-employment restraint period ≤ 24 months                                                           | Exceeding portion is void (reduces to 2 years by operation of law) |
| **Legitimate business interest**                          | HGB § 74a(1) | Restriction must protect demonstrable employer interests (trade secrets, customer relationships, etc.) | Nichtig (void) if disproportionate                                 |
| **Proportionality of scope**                              | HGB § 74a(1) | Geographic and activity scope must not unreasonably restrict employee's livelihood                     | Nichtig if unbillig (inequitably burdensome)                       |

#### Karenzentschädigung (Mandatory Compensation) — Key Details

**What counts as "most recent remuneration" for the 50% calculation:**

- Base salary (Grundgehalt)
- Regular variable pay, bonuses, commissions (where contractually promised)
- Benefits with regular cash value
- **Excludes**: Exceptional one-time bonuses, expense reimbursements, purely discretionary
  payments
- The calculation period is typically the last 12 months of employment

**Payment mechanics:**

- Compensation is paid **monthly** during the restraint period
- Employee must notify employer if they take new employment (reduces compensation by any
  earnings received from new employer that, combined with Karenzentschädigung, exceed the
  employee's prior total compensation — HGB § 74c)
- Employer must pay even if employee chooses not to work (within limits)

#### Unverbindlich vs. Nichtig — Critical Distinction

| Defect                                             | Legal Status                                           | Employee's Right                                                                                                                           |
| -------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Compensation < 50% of remuneration                 | **Unverbindlich** (non-binding at employee's election) | Employee can choose to comply and claim the promised (insufficient) compensation — OR — ignore the clause entirely (free from restriction) |
| No compensation stated at all                      | **Nichtig** (void) — no legal effect                   | Clause has no legal effect; employee is free from restriction                                                                              |
| Duration > 2 years                                 | Clause valid for 2 years; excess void                  | Only 2-year restriction applies                                                                                                            |
| Scope disproportionate / no legitimate interest    | **Nichtig** (void) — specific to that scope            | Void in its entirety or the disproportionate part                                                                                          |
| Formal deficiency (no writing/no copy to employee) | **Nichtig** (void)                                     | Clause has no legal effect                                                                                                                 |

**Practical consequence**: An employer issuing a non-compete with < 50% compensation
gives the employee a **windfall option** — the employee can either honour it (knowing
they can claim compensation even if underpaid) or disregard it entirely.

#### Employer Waiver Rights

The employer may waive the non-compete within **one year of giving notice** of the
waiver (HGB § 75a). After waiver, the employer is released from the obligation to pay
Karenzentschädigung from the date one year after waiver notice — but must pay for any
period the employee was actually bound before that.

Timing significance: If the employer terminates the employee and wishes to avoid paying
Karenzentschädigung, they must give waiver notice at the same time or shortly after
termination. Failure to waive = obligation to pay.

#### Dismissal and Automatic Voidance

If the **employer terminates without cause** (fristlose Kündigung ohne wichtigen Grund)
or the **employer terminates for a reason within their sphere of responsibility**:

- The employee may declare within one month of receiving the termination notice that they
  elect not to be bound by the non-compete (HGB § 75)
- This removes the non-compete entirely without any compensation obligation

#### BAG Case Law Reference Points

- **BAG 8 AZR 453/21 (August 25, 2022)** — **RSUs/restricted stock units are NOT
  "contractual benefits"** for Karenzentschädigung calculation purposes. They are capital
  investment instruments, not wage components; they do not count toward the 50% minimum
  compensation base. [VERIFY citation format]
- **BAG, March 27, 2025** — Virtual stock option (VSO) payments count toward
  Karenzentschädigung **only if exercised during employment**; post-termination option
  exercises do not inflate the compensation calculation base. [VERIFY citation]
- BAG on Vertragsstrafe: courts typically cap contractual penalty clauses (Vertragsstrafe)
  at **3 months' salary as the maximum enforceable amount**; 1 month's salary is commonly
  enforced in practice. Penalties above 3 months' salary are generally void as unconscionable. [VERIFY]
- BAG on severability clauses: clauses stating parties "would have agreed" to compensation
  do not cure a missing Karenzentschädigung commitment — compensation must be **actually
  agreed in advance**. [VERIFY]
- BAG, 28.06.2006 — Calculation of Gesamtvergütung basis for Karenzentschädigung [VERIFY]
- BAG, 07.07.2015 — Scope proportionality and "unbillig" threshold [VERIFY]

---

### 5-FR: France Analysis

#### Legal Framework

French non-compete law is governed primarily by **Cour de cassation social chamber case
law** rather than statute. The landmark ruling of July 10, 2002 (Société Manoukian —
_Soc._ 10 juill. 2002, no 99-43.334 et no 00-45.135) established the **five cumulative
criteria** for a valid clause de non-concurrence. All five must be satisfied for the
clause to be valid; failure on any one criterion voids the entire clause.

**Applicable collective bargaining agreements (conventions collectives)** may impose
stricter requirements (higher minimum compensation, shorter maximum duration). The
applicable CBA — determined by the employer's sector (code APE/NAF) — must always be
checked. A clause satisfying the statutory minimum may still be invalid if it falls
short of the applicable CBA standard.

#### Five Cumulative Validity Criteria

| #   | Criterion                                                     | Requirement                                                                                              | Common Deficiency                                                             |
| --- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 1   | **Indispensable to protect legitimate business interests**    | Must be necessary to protect a specific, identifiable business interest — not just competition avoidance | Generic "competition prevention" clause without identifying specific interest |
| 2   | **Limited in time**                                           | Duration must be defined and proportionate; typically maximum 2 years                                    | Open-ended restriction; excessive duration                                    |
| 3   | **Limited in geographic scope**                               | Geographic area must be defined and linked to employer's actual market                                   | Worldwide or undefined geographic scope                                       |
| 4   | **Limited in professional activity**                          | The restricted activity must be specifically defined and link to the employee's actual role              | Blanket prohibition on all professional activity                              |
| 5   | **Mandatory financial counterpart (contrepartie financière)** | Employer must pay financial compensation throughout the restraint period                                 | **No compensation stated = void**; below-threshold compensation               |

**Critical rule — contrepartie financière:**

- **Mandatory** — not optional, cannot be waived even by a collective bargaining agreement
- Due for the **entire duration** of the restraint period, paid monthly (or at contractually
  agreed intervals)
- Minimum standard: At least **30% of average gross monthly remuneration** based on
  the last 12 months of salary (_Soc._ 16 mai 2012, no 11-10.760) [VERIFY current
  case law standard]
- Many collective bargaining agreements impose **33% or higher** minimums — always check
  the applicable CBA
- Amount calculated on total remuneration including bonuses, where applicable

**Note on Article L.1237-18 Code du travail (rupture conventionnelle)**: Where employment
ends by agreed termination (rupture conventionnelle), the non-compete clause continues to
apply unless the employer formally waives it at the time of execution of the rupture
conventionnelle.

**Compensation timing — notice period (préavis)**: Contrepartie financière typically
begins only after the **final termination date**, not during any notice period (préavis)
the employee is serving. The restraint period and compensation obligation run concurrently
from the date employment definitively ends.

#### Employer Waiver of the Non-Compete

The employer may waive (renoncer) the clause, thereby freeing both parties from the
restriction and compensation obligation:

- The right and procedure for waiver must generally be specified in the employment
  contract or the applicable collective bargaining agreement
- Waiver must typically be given **at the time of departure** or within the period
  specified in the contract/CBA (often within 8-15 days of notice of termination)
- **If waiver is not timely given**: The employer remains bound to pay compensation for
  the full restraint period, even if they later change their mind

#### Consequences of Non-Payment

If the employer fails to pay the contrepartie financière:

- The employee is **immediately freed from the non-compete obligation** — they may
  immediately take competing employment
- The employee may **claim damages** for the period they were wrongly bound
- The employer cannot enforce the restriction while in breach of the payment obligation
  (_Soc._ 7 mars 2007, no 05-45.031) [VERIFY citation]

#### Practical Classification Considerations

| Deficiency                                | Classification | Consequence                                                         |
| ----------------------------------------- | -------------- | ------------------------------------------------------------------- |
| One or more of criteria 1-4 missing       | VOID           | Clause has no effect; employee free to compete                      |
| No contrepartie financière stated         | VOID           | Clause has no effect                                                |
| Contrepartie financière below CBA minimum | NON-COMPLIANT  | Employee can challenge; employer must pay correct amount to enforce |
| Waiver not provided at departure          | AT-RISK        | Employer bound to pay for full restraint period                     |
| Duration > applicable CBA maximum         | NON-COMPLIANT  | Clause void or reduced to CBA maximum                               |

---

### 5-CN: China Analysis

#### Legal Framework

Chinese non-compete law is governed by the **Labor Contract Law of the People's Republic
of China** (劳动合同法), Articles 23-24 (effective January 1, 2008), supplemented by the
**Supreme People's Court Interpretation (III) on Several Issues Concerning the
Application of Law in the Trial of Labor Dispute Cases** (2010). Key provisions:

- Art. 23: Non-compete (竞业禁止) and confidentiality clauses (保密义务) permitted
- Art. 24: Sets scope of permissible subjects, maximum duration (2 years), and economic
  compensation requirement
- SPC Interpretation III (2010): Consequences of employer's failure to pay compensation

#### Mandatory Validity Requirements

| Requirement                                                                                                           | Legal Basis | Check                                            | Consequence if Failed                                               |
| --------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| **Eligible subject** — senior management, senior technical staff, or other employees with confidentiality obligations | Art. 24     | Employee must fall within permitted categories   | Non-compete may be void as applied to ineligible employees [VERIFY] |
| **Maximum 2-year duration**                                                                                           | Art. 24     | Post-employment restriction ≤ 24 months          | Excess duration unenforceable; reduced to 2 years                   |
| **Economic compensation (经济补偿)** during restraint period                                                          | Art. 23     | Monthly compensation must be stated in agreement | See SPC Interpretation III below                                    |
| **Defined scope** — industry/business activity and/or geographic area                                                 | Art. 24     | Must specify the restricted activities           | Overly vague clauses may be struck                                  |

#### Who Can Be Bound — Eligible Subjects

| Category                                | Chinese Term                        | Description                                                                                                                             |
| --------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Senior management personnel             | 高级管理人员 (gāojí guǎnlǐ rényuán) | Directors, supervisors, general managers, and equivalent C-level roles as defined in the company's articles of association or contracts |
| Senior technical personnel              | 高级技术人员 (gāojí jìshù rényuán)  | Senior engineers, R&D leads, key technical roles — not all technical employees; "senior" threshold is fact-specific                     |
| Others with confidentiality obligations | 其他负有保密义务的劳动者            | Employees with access to genuine trade secrets or confidential customer information                                                     |

**Important**: Art. 24 does not permit employers to impose non-competes on ordinary
employees merely because they are employed. The employee must genuinely fall within
one of the above categories. Courts scrutinise this [VERIFY with current SPC guidance].

#### Economic Compensation — Key Details

- Must be paid **monthly** during the restraint period (not as a lump sum at departure)
- The Labor Contract Law does not specify a **minimum amount** — unlike Germany (50%)
  and France (30-33%). SPC Interpretation III fills some gaps:
  - If no amount is agreed but the clause is otherwise valid: courts may award compensation
    at **30% of the employee's average monthly wage** in the 12 months before contract
    termination [VERIFY current SPC 2022 guidance]
  - If the agreed amount is "unreasonably low," courts may adjust upward
- Compensation continues throughout the full restraint period unless the employee breaches

#### SPC Interpretation III (2010) and Interpretation II (August 2025) — Non-Payment and Damages

**Consequence of employer non-payment:**

| Employer Non-Payment Period           | Employee's Right                                                                                                        |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 3+ consecutive months without payment | Employee may notify employer and terminate non-compete obligation; employer cannot recover previously paid compensation |
| < 3 months without payment            | Employee must continue to honour restriction; can demand payment through arbitration/court                              |

**If employee breaches despite receiving compensation:**

- Employee liable for liquidated damages (违约金) as specified in the agreement
- **SPC Interpretation II (August 2025) — New liquidated damages cap**: Liquidated
  damages for breach **must not exceed 5 times the total non-compete compensation paid**
  to the employee. Courts will reduce any contractually agreed amount above this cap.
  Example: RMB 3,000/month × 12 months = RMB 36,000 total compensation → maximum
  liquidated damages = RMB 180,000.
- Employer may also seek injunction and actual damages beyond liquidated damages, but
  punitive damages against employees are prohibited.

**SPC Interpretation II (August 2025) — Key Updates [VERIFY with current SPC text]:**

- 30% minimum compensation reaffirmed; courts can adjust if compensation is clearly
  inadequate or unreasonably high
- Non-competes void if employee **lacks actual access to trade secrets** — courts examine
  real job duties, not titles
- Liquidated damages cap: 5x total compensation paid
- New guidance on non-competes surviving employee reinstatement after wrongful dismissal

#### Dispute Resolution Process

China labor disputes follow a mandatory sequence:

1. **Labor arbitration** (劳动仲裁) — must file first with the local Labor Dispute
   Arbitration Commission (LDAC); arbitration is mandatory before any court action
2. **Court (人民法院)** — if either party dissatisfied with arbitration result, may
   file with the people's court within 15 days of receiving arbitration award
3. Non-compete disputes are typically treated as labor disputes subject to this process

**Governing rules**: The labor arbitration/court of the place where the labor contract
is performed (employee's work location) has jurisdiction, regardless of contractual
choice-of-law or arbitration clauses attempting to oust labor dispute procedures.

---

### Step 6: Multi-Jurisdiction Analysis

When an employee works across multiple jurisdictions or the employment contract spans
multiple legal systems:

**6a. Stack the analysis**: Apply each relevant jurisdiction's requirements independently.
The non-compete must satisfy the most demanding standard that applies.

**6b. Identify cross-border risks:**

| Scenario                                              | Risk                                                                                  |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------- |
| California employee with non-California governing law | CA SB 699/AB 1076 — void and unenforceable regardless of choice of law                |
| German employee with US/UK governing law              | HGB §§ 74-75a apply as mandatory German employment law — Karenzentschädigung required |
| French employee with foreign governing law            | French mandatory employment law applies — contrepartie financière required            |
| Chinese employee with offshore governing law          | Labor Contract Law mandatory requirements apply to employment performed in China      |
| Multi-country post-M&A population                     | Each target jurisdiction applies own rules — create per-jurisdiction matrix           |

**6c. Choice-of-law override matrix:**

| Jurisdiction    | Override Rule                                                                                                                 | Governing Authority                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| California (US) | Complete extraterritorial ban — SB 699 voids any non-compete as to work performed in CA                                       | Bus. & Prof. Code § 16600.5                               |
| Germany         | Mandatory HGB §§ 74-75a apply to employment relationships performed in Germany                                                | BAG case law; Rome I Regulation Art. 8 (for EU contracts) |
| France          | Cour de cassation criteria are mandatory employment law; foreign-law contracts cannot avoid them for work performed in France | Rome I Regulation Art. 8                                  |
| China           | Labor Contract Law Art. 24 mandatory; arbitration before Chinese LDAC mandatory for China-performed work                      | SPC guidance                                              |
| UK              | No mandatory domestic rules per se; choice of law generally respected, but extreme restrictions may engage UK public policy   | Restraint of trade doctrine                               |

---

### Step 7: Generate Enforceability Assessment

For each jurisdiction analysed, produce:

1. **Classification** (see Severity Classification section below)
2. **Specific deficiencies** — each failing element listed with citation
3. **Remediation steps** — actionable fixes for each deficiency
4. **Confidence score** — per the Confidence Scoring framework below
5. **Priority tier** — per the Prioritization Framework below

---

## Enforceability Classification

### ENFORCEABLE

All mandatory requirements met; clause is proportionate; no per-se invalidity applies.

**Characteristics:**

- No statutory ban applies
- All mandatory elements present (compensation in DE/FR/CN, writing requirements, etc.)
- Duration/geography/activity scope within reasonable limits for the jurisdiction
- Legitimate business interest identified and credible
- Appropriate consideration for the restriction

**Action**: Note for awareness; no remediation required. Flag any terms that are close
to the limit (e.g., UK 12-month restriction in a borderline case) even if currently
enforceable.

### AT-RISK

Clause contains one or more elements that reduce enforceability likelihood, but no
per-se invalidity. The clause may be enforced in favourable circumstances but carries
meaningful litigation risk.

**Characteristics:**

- Duration at or near the upper end of what courts typically accept
- Geographic or activity scope broader than demonstrably necessary
- Legitimate business interest stated but weakly supported
- Minor procedural deficiency (but not one that voids the clause)
- UK: Restriction that a judge might blue-pencil but could also uphold
- France: Compensation slightly below CBA minimum (but above statutory floor)

**Action**: Provide specific redlines to move the clause into ENFORCEABLE territory.
Identify the strongest AT-RISK element for priority negotiation/revision.

### NON-COMPLIANT

Clause fails a mandatory requirement but the failure is remediable.

**Characteristics:**

- Germany: Compensation below 50% of remuneration (unverbindlich — not yet nichtig)
- France: Compensation below CBA minimum or waiver process not followed
- China: No compensation stated (courts may still imply a minimum)
- US: Salary below threshold (remediable by salary increase or removing the clause)
- Duration exceeds statutory maximum (remediable by reducing duration)

**Action**: Provide specific remediation steps. Until remediated, the clause is
unenforceable (or enforceable only at the employee's option in Germany).

### VOID

Clause is per-se invalid under applicable law. No remediation of the existing clause
possible — must be replaced with a valid agreement.

**Characteristics:**

- US ban-state applies (CA, MN, ND, OK, WY, MT)
- Germany: No compensation stated at all; no writing; fundamental formal deficiency
- France: Any one of the five cumulative criteria entirely absent
- China: Employee is not an eligible subject under Art. 24
- UK: Restriction so broad that it is entirely unreasonable with no severable valid core

**Action**: Advise that the clause has no legal effect. If the employer wishes to protect
legitimate interests, provide guidance on what alternative mechanism can be used (e.g.,
UK: carefully scoped non-solicitation or garden leave; US: trade secret protections under
DTSA).

---

## Actionable Output Per Finding

For each deficiency identified, provide:

```
**Finding**: [Short title of the deficiency]
**Jurisdiction**: [Applicable jurisdiction]
**Classification**: [ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]
**Current Clause Language**: "[Quote or describe the relevant provision]"
**Legal Basis**: [Statute, case, or principle — or "General principle [VERIFY]"]
**Deficiency**: [Precise description of what is missing or overbroad]
**Remediation**: [Specific fix — revised language or structural change]
**Priority**: [Tier 1 / Tier 2 / Tier 3 — per the framework below]
**Confidence**: [Definite / High / Probable / Possible / Unlikely — per the framework below]
```

---

## Prioritization Framework

### Tier 1 — Must-Fix (Non-Negotiable for Enforceability)

Issues where the clause is either void or non-compliant without remediation:

- Per-se statutory ban (US ban states, specific country bans)
- Missing mandatory compensation element (Germany, France, China)
- Formal deficiency that voids the clause (Germany: no writing, no copy to employee)
- France: Missing any one of the five cumulative criteria
- China: Non-eligible subject category bound
- Duration beyond statutory maximum (Germany 2-year cap, China 2-year cap)

**For employers**: These must be fixed to have any enforceable restriction.
**For employees**: These are immediate leverage points — clause has no legal effect.

### Tier 2 — Should-Fix (Significant Enforceability Risk)

Issues that do not automatically void the clause but materially increase litigation risk:

- UK: Duration over 12 months without exceptional justification
- UK: No identified legitimate protectable interest
- US: Salary below statutory threshold in applicable state
- Germany: Compensation below 50% (clause becomes unverbindlich — employee's choice)
- France: Compensation below CBA minimum
- China: Compensation not stated (courts imply minimum but parties should specify)
- Any jurisdiction: Overbroad activity scope (entire industry ban)
- Any jurisdiction: Geographic scope without connection to employer's market

**For employers**: These materially weaken enforcement prospects.
**For employees**: These are secondary challenge grounds.

### Tier 3 — Consider-Fixing (Optimisation)

Issues that improve the clause's defensibility without being determinative:

- Duration reduced to the minimum necessary for the identified interest
- Geographic scope tightened to the employer's actual competitive footprint
- Activity scope narrowed to what the employee actually did
- Consider adding garden leave set-off language (UK)
- Specify precise consideration amount (all jurisdictions)
- DTSA/trade secret overlay compliance language (US)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                              | Fail Action                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                  | Add citation or mark "[UNVERIFIED — verify before relying]"                      |
| **Format**     | Citations follow a consistent, recognisable format for the jurisdiction                           | Fix format; use jurisdiction-appropriate citation style                          |
| **Currency**   | All cited thresholds (salary figures, percentages), statutes, and case law checked for amendments | Flag "[CHECK CURRENCY — figure may have been amended]" for all salary thresholds |
| **Domain**     | Analysis stays within the jurisdiction being analysed — no bleed from other systems               | Remove or flag cross-jurisdiction contamination                                  |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                         | Add confidence qualifier; use [VERIFY] for uncertain points                      |

### Self-Interrogation for VOID and NON-COMPLIANT Findings

For any finding classified VOID or NON-COMPLIANT, apply this 3-pass review before
delivering:

**Pass 1 — Legal Chain Integrity**: Does the classification follow logically from the
cited authority? Would a court in this jurisdiction actually reach this conclusion?
Is there a counter-argument the employer's counsel would make?

**Pass 2 — Completeness**: Have all relevant mandatory elements been considered? Is
there a recent statutory amendment or case law development that affects the analysis?
Has the applicable collective bargaining agreement (France) or industry-specific
exception (US healthcare) been checked?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS enforceable?
Under what circumstances might a court reform rather than void? Would blue-pencil save
any portion?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence level to each material finding:

| Level        | Range     | Meaning                                                                    | Action                                                  |
| ------------ | --------- | -------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, no ambiguity                                   | State with confidence                                   |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions                           | State with brief caveat                                 |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ                           | State with explicit reasoning and contra-indicators     |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities or jurisdiction-specific nuance | Flag for professional review with both arguments        |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                                    | Do not assert; flag "[UNCERTAIN — verify with counsel]" |

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section. This makes the reasoning traceable
and auditable for legal review.

```yaml
glass_box:
  skill_name: "legalcode-non-compete-analysis"
  mode: "Cross-jurisdictional router"
  analysis_date: "[date of analysis]"
  jurisdictions_analysed:
    - "[Jurisdiction 1]"
    - "[Jurisdiction 2 — if applicable]"
  employee_perspective: "[Employer / Employee / In-house / Transactional]"
  document_type: "[Employment agreement / Severance / Standalone / Other]"
  clause_duration: "[as stated in clause]"
  clause_geography: "[as stated in clause]"
  clause_activity: "[as stated in clause]"
  clause_compensation: "[as stated in clause or 'Not stated']"
  governing_law_clause: "[as stated in agreement or 'None']"
  work_location: "[Employee's primary work location]"
  jurisdiction_override_applies: "[Yes — specify / No]"
  classifications:
    US: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID / Not analysed]"
    UK: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID / Not analysed]"
    Germany: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID / Not analysed]"
    France: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID / Not analysed]"
    China: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID / Not analysed]"
  deep_skills_routed_to:
    - "[legalcode-us-state-non-compete-analysis — if US]"
    - "[legalcode-non-compete-analysis-is — if Iceland]"
  legalcode_mcp: "Connected / Not connected"
  statutes_cited:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  cases_cited:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number total]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no VOID/NON-COMPLIANT findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  tier_1_findings: "[number]"
  tier_2_findings: "[number]"
  tier_3_findings: "[number]"
  limitations:
    - "Salary thresholds are updated annually — verify current figures before relying"
    - "Collective bargaining agreement (France) not checked — verify applicable CBA"
    - "China SPC 2022 guidance on compensation minimums not independently verified"
    - "[Additional scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by qualified employment lawyer in each jurisdiction"
```

---

## Anti-Patterns

The following are common errors and failures in non-compete practice. Identify and flag
any of these patterns in the clause under review.

1. **Copy-paste from another jurisdiction's template**: Using a US-style non-compete
   (no compensation, one-sided) in Germany or France where mandatory compensation is
   required. The clause will be void or unverbindlich.

2. **Omitting compensation in Germany/France/China**: Treating compensation as optional.
   In Germany, France, and China, compensation during the restraint period is a mandatory
   validity element. A clause without it is void (Germany/France) or risks SPC
   compensation implication (China).

3. **Relying on choice-of-law to escape mandatory employment law**: Inserting a New York
   governing-law clause for a French employee, believing it avoids French mandatory
   non-compete requirements. Rome I Regulation (France) and state statutes (California
   SB 699) override this.

4. **Worldwide or "all of Europe" geographic scope for non-senior roles**: Courts in
   every jurisdiction scrutinise overbroad geographic restrictions. A worldwide ban on
   a mid-level software engineer is almost certainly unenforceable everywhere.

5. **Industry-wide activity bans**: "May not work in the technology / financial services /
   healthcare industry" without limiting to genuinely competitive activities. Too broad in
   all five jurisdictions covered by this skill.

6. **No legitimate business interest identified**: Drafting the restriction without
   specifying what business interest it protects. UK courts require this; German courts
   require "unbillig" assessment; French courts require the "indispensable" criterion;
   US courts apply the legitimate business interest test.

7. **Excessive duration combined with overbroad activity scope**: Multiplying the harm.
   UK courts analyse duration, geography, and activity scope together. A 24-month
   restriction on all competitive activity in all geographies has near-zero chance of
   survival.

8. **Forgetting the French waiver deadline**: The employer's right to waive the French
   clause is often time-limited in the employment contract or CBA (typically 8-15 days
   after notice). Missing this window means paying compensation for the full restraint
   period, even if the employer no longer needs the restriction.

9. **German non-compete without immediate waiver at termination**: Employers who
   terminate an employee without simultaneously waiving the non-compete clause are
   exposed to full Karenzentschädigung liability. Failure to waive = obligation to pay.

10. **Misidentifying the eligible Chinese employee category**: Applying a non-compete to
    a mid-level employee who does not qualify as "senior management" or "senior technical
    staff" under Art. 24. Courts may decline to enforce.

11. **Confusing non-compete with non-solicitation**: Drafting an overly broad activity ban
    when a narrower non-solicitation of clients/employees would be sufficient and more
    defensible. Non-solicitation covenants are generally subject to less scrutiny.

12. **Stacking garden leave and non-compete without coordination**: UK employers sometimes
    add a 6-month garden leave period and a 12-month non-compete without any interaction
    provision. Courts view the combined 18-month restricted period sceptically. Include
    explicit set-off language.

13. **Ignoring sector-specific collective bargaining agreements (France)**: The applicable
    CBA may impose higher compensation floors (often 33%+ vs. the 30% case-law minimum)
    or shorter maximum durations. Failing to check the CBA creates non-compliance risk.

14. **US mid-employment non-compete without fresh consideration**: In states that require
    additional consideration for mid-employment non-competes (e.g., Illinois, Texas
    for independent covenant agreements), offering "continued employment" is insufficient
    in many jurisdictions. Must provide a genuine benefit.

15. **Applying post-employment restrictions to acquisition targets without analysis**:
    Business-sale non-competes are assessed under different (usually more permissive)
    standards than employment non-competes in most jurisdictions (UK, US, Germany, France).
    Using employment-law doctrine to analyse acquisition-related restrictions leads to
    incorrect conclusions.

16. **Missing the China mandatory arbitration-first requirement**: Attempting to resolve
    non-compete disputes through contractual arbitration (e.g., ICC arbitration, CIETAC
    commercial arbitration) when Chinese mandatory labor dispute resolution requires
    labor arbitration before the LDAC first. Commercial arbitration clauses in employment
    contracts are generally invalid for labor dispute purposes in China.

17. **Over-relying on trade secret law as a substitute for a void non-compete**: Trade
    secret law (DTSA/UTSA in the US; German UWG/GeschGehG; French unfair competition)
    is narrower than a non-compete and requires proof of actual misappropriation. It is
    not a substitute for a validly drafted non-compete where a non-compete is enforceable.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Be specific, not general**: "The clause violates HGB § 74(2) because the stated
   Karenzentschädigung of €500/month represents approximately 18% of the employee's
   monthly remuneration, well below the mandatory 50% minimum" — not "the compensation
   may be insufficient."

2. **Active voice, present tense**: "The clause is void under California Business and
   Professions Code § 16600" — not "the clause would appear to potentially be void."

3. **Separate the findings from the recommendations**: Lead with the finding (what is
   wrong and why), then the remediation (what to do). Do not blend them.

4. **Mark uncertainty explicitly**: Use [VERIFY], [CHECK CURRENCY], or [UNCERTAIN] tags.
   Never bury uncertainty in hedged language without flagging it directly.

5. **Calibrate confidence to actual authority**: A clear statutory ban (California,
   Germany) warrants Definite confidence (0.95-1.0). A case-law-only principle
   (UK reasonableness) warrants High or Probable (0.70-0.90). A jurisdiction where
   case law is sparse warrants Possible (0.40-0.60).

6. **Preserve actionability**: Every finding should end with a clear, specific
   recommendation that an employment lawyer or HR professional can act on.

7. **Gate before delivery**: Run the Citation Quality Gates before finalising output.
   Do not deliver findings that have not passed the 5-gate check.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp to verify:

- Current US salary thresholds for the applicable state(s) — these are updated annually
- Recent statutory changes (new state bans, legislative amendments)
- Applicable French collective bargaining agreement for the employer's sector (NAF code)
- Current BAG (German Federal Labour Court) case law on Karenzentschädigung
- SPC guidance on China minimum compensation standard
- UK employment case law on reasonableness of duration/scope

Save verified results to `/tmp/legalcode-noncompete-research.md` and mark citations
as VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp (Graceful Degradation)

Proceed with the analysis using general knowledge from this skill:

- Mark all salary thresholds with [CHECK CURRENCY — verify current figure]
- Mark all case law citations with [VERIFY against authoritative sources]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Particularly flag the France CBA overlay and China SPC 2022 guidance as requiring
  independent verification before relying on the analysis

### Routing to Jurisdiction-Specific Deep Skills

After completing the US preliminary screening, always route to:

```
For comprehensive US analysis (all 50 states, full matrix, garden leave, FTC):
→ Use skill: legalcode-us-state-non-compete-analysis

For US enforceability matrix with full remediation redlines:
→ Use skill: legalcode-non-compete-enforceability

For Iceland-specific analysis:
→ Use skill: legalcode-non-compete-analysis-is
```

---

## Cross-Jurisdiction Comparative Reference

| Aspect                             | US                                                              | UK                                                   | Germany                                                                       | France                                             | China                                                                 |
| ---------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------- |
| **Legal basis**                    | State law; no federal statute                                   | Common law restraint of trade                        | HGB §§ 74-75a (mandatory)                                                     | Cour de cass. case law (Manoukian 2002)            | Labor Contract Law Arts. 23-24                                        |
| **Maximum duration**               | Varies by state; ~2 years typical outer limit                   | No statute; 6-12 months typical; 18+ months rare     | 2 years (§ 74a — hard cap)                                                    | 1-3 years; no statute; CBA often 2 years           | 2 years (Art. 24 — hard cap)                                          |
| **Mandatory compensation**         | Not required (exception: MA garden leave 50% salary)            | **Not required**                                     | **Yes — ≥ 50% of last contractual remuneration** (§ 74(2))                    | **Yes — ≥ ~30% of avg gross monthly remuneration** | **Yes — ≥ 30% of avg monthly salary** (SPC)                           |
| **Consequence of no compensation** | Clause typically still valid (no pay required)                  | Clause may still be valid                            | UNVERBINDLICH (employee's choice to comply or not)                            | VOID (nulle)                                       | Clause voidable; 3 months non-payment → employee may terminate        |
| **Employee scope**                 | All (unless ban-state or below salary threshold)                | Any (if reasonable)                                  | Any employee (if legitimate interest)                                         | Position-dependent; cadres vs. non-cadres          | Senior management, senior technical staff, confidentiality-bound only |
| **Void mechanisms**                | Statutory ban (CA/MN/ND/OK/WY/MT); salary threshold             | Unreasonable in full; or blue-pencil partial         | Nichtig (void) for formal defects; unverbindlich for insufficient pay         | Void on any one of 5 criteria failing              | Void if scope disproportionate or employee ineligible                 |
| **Enforcement remedy**             | Injunction (state court)                                        | Injunction (High Court / interim interdict Scotland) | Injunction (einstweilige Verfügung) + Vertragsstrafe (≤ 3 months' salary cap) | Court action for nullity/damages; injunction       | Labor arbitration (mandatory first) → court                           |
| **Recent development**             | FTC rule vacated Aug 2024; FL CHOICE Act 2025; WY ban July 2025 | Feb 2026 consultation closed; outcome pending        | BAG March 2025 (VSOs); BAG Aug 2022 (RSUs excluded)                           | CBA standards often higher than statutory floor    | SPC Interpretation II Aug 2025 (5× damages cap; scope tightening)     |

---

## Localization Notes

### Jurisdiction-Specific Terminology Quick Reference

| English Term               | US                                                   | UK                                                 | Germany                                                           | France                                                      | China                                                 |
| -------------------------- | ---------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| Non-compete clause         | Non-compete agreement / covenant not to compete      | Post-employment restriction / restrictive covenant | Nachvertragliches Wettbewerbsverbot (§§ 74-75a HGB)               | Clause de non-concurrence                                   | 竞业禁止条款 (jìngyè jìnzhǐ tiáokuǎn)                 |
| Compensation for restraint | Garden leave pay (for GLAs); not mandatory otherwise | Not required by law                                | Karenzentschädigung (mandatory ≥ 50%)                             | Contrepartie financière (mandatory)                         | 经济补偿 (jīngjì bǔcháng, mandatory)                  |
| Void / unenforceable       | Void (ban states), unenforceable (blue/red pencil)   | Void (if unreasonable); blue-pencil to sever       | Nichtig (void) / Unverbindlich (non-binding at employee's option) | Nulle (null and void)                                       | 无效 (wúxiào, invalid)                                |
| Competition authority      | FTC (federal)                                        | Competition and Markets Authority (CMA)            | Bundeskartellamt                                                  | Autorité de la concurrence                                  | SAMR (国家市场监督管理总局)                           |
| Governing court            | State courts (primarily); federal for DTSA           | Employment Tribunal / High Court                   | Arbeitsgericht (Labour Court); BAG (Federal)                      | Conseil de prud'hommes (Labour tribunal); Cour de cassation | Labour Arbitration Commission (LDAC) → People's Court |

### Regional Variants Within Covered Jurisdictions

**US**: State law varies dramatically. The preliminary screening in Step 5-US covers the
key categories. Engage `legalcode-us-state-non-compete-analysis` for full state-by-state
analysis.

**UK**: Scotland has its own legal system. This skill's UK analysis reflects English and
Welsh law. For Scottish-law governed agreements, flag and recommend review by Scots law
counsel, noting that the general reasonableness principles are similar but procedural
aspects differ.

**Germany**: The HGB §§ 74-75a framework applies to Handlungsgehilfen (commercial
employees). By BAG case law extension, substantially equivalent protections apply to all
employees in employment relationships. [VERIFY current BAG doctrine on application to
non-commercial employees]

**France**: Paris-based financial services, technology, and media sectors each have
active collective bargaining agreements with specific non-compete provisions. The
applicable CBA is determined by the employer's sector code (code APE/NAF). Always check
before concluding the contrepartie financière analysis.

**China**: The People's Republic of China Labor Contract Law applies to mainland China.
Distinct rules apply in Hong Kong (common law; no statutory non-compete framework
analogous to mainland China) and Macau. For Taiwan, separate analysis required.

---

## Output Format Template

Structure every non-compete analysis output as follows:

```markdown
# Non-Compete Enforceability Analysis

**Date**: [Date of analysis]
**Document reviewed**: [Contract name/type]
**Jurisdiction(s)**: [List of jurisdictions analysed]
**Perspective**: [Employer / Employee / Neutral]
**Employee role**: [Role description if known]

---

## Summary Classification

| Jurisdiction | Classification                               | Confidence       | Key Issue          |
| ------------ | -------------------------------------------- | ---------------- | ------------------ |
| [US — State] | ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID | [High/Prob/Poss] | [One-line summary] |
| [UK]         | ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID | [High/Prob/Poss] | [One-line summary] |
| [Germany]    | ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID | [High/Prob/Poss] | [One-line summary] |
| [France]     | ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID | [High/Prob/Poss] | [One-line summary] |
| [China]      | ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID | [High/Prob/Poss] | [One-line summary] |

---

## Clause Terms Reviewed

- **Duration**: [as stated]
- **Geographic scope**: [as stated]
- **Restricted activities**: [as stated]
- **Compensation during restraint**: [as stated, or "None stated"]
- **Garden leave**: [present/absent, terms if present]
- **Governing law clause**: [as stated, or "None"]

---

## Detailed Analysis by Jurisdiction

### [Jurisdiction Name]

**Framework**: [Brief statement of applicable law]

**Mandatory requirements check:**
| Requirement | Status | Finding |
|---|---|---|
| [Requirement 1] | ✅ Met / ⚠️ At-Risk / ❌ Failed | [Detail] |
| ... | | |

**Classification**: **[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]** (Confidence: [Level])

**Findings:**

[Finding 1 in the structured format above]
[Finding 2 ...]

**[Route to deep-analysis skill if applicable]**

---

## Prioritised Remediation Plan

### Tier 1 — Must-Fix

1. [Finding title] — [One-line action]

### Tier 2 — Should-Fix

1. [Finding title] — [One-line action]

### Tier 3 — Consider-Fixing

1. [Finding title] — [One-line action]

---

## Cross-Jurisdiction Risks

[Only if multi-jurisdiction analysis was performed]

- [Risk 1]: [Description and impact]
- [Risk 2]: ...

---

## Recommended Next Steps

- [Action 1]: [By whom, by when]
- [Action 2]: ...
- [Route to deep-skill]: For comprehensive US analysis, use `legalcode-us-state-non-compete-analysis`

---

[Glass Box audit trail — YAML format as specified above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- `legalcode-non-compete-enforceability` — US enforcement matrix and anti-pattern catalogue
- `legalcode-us-state-non-compete-analysis` — US state-by-state deep analysis
- `legalcode-non-compete-analysis-is` — Iceland analysis (Nordic comparative context)
- `legalcode-contract-review` — quality assurance frameworks (Citation Quality Gates,
  Self-Interrogation, Confidence Scoring, Glass Box audit trail)
- `legalcode-employment-agreement-review` — employment context and interaction analysis
- Web research: UK restraint of trade doctrine; German HGB §§ 74-75a BAG case law;
  French Cour de cassation social chamber case law including Manoukian 2002; China
  Labor Contract Law Arts. 23-24 and SPC Interpretation III
- Legal sources: HGB (German Commercial Code), French Code du travail, China Labor
  Contract Law 2008, UK restraint of trade common law doctrine

Attribution: Legalcode original synthesis — not imported from any external repository.
