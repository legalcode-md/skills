---
name: legalcode-independent-contractor-classification
description: 'Analyse whether a working relationship should be classified as independent contractor or
  employee under multiple overlapping legal tests: ABC test (California AB5/Dynamex, Massachusetts, New
  Jersey, Illinois, 33+ states), economic reality test (FLSA, DOL guidance), common law / right-to-control
  test (IRS three-category framework, Revenue Ruling 87-41), and hybrid tests. Use when onboarding independent
  contractors, auditing an existing contractor workforce, responding to a DOL/state agency investigation,
  evaluating litigation risk, or advising on platform-worker arrangements.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyse whether a working relationship should be classified as independent contractor or employee under multiple overlapping legal tests: ABC test (California AB5/Dynamex, Massachusetts, New Jersey, Illinois, 33+ states), economic reality test (FLSA, DOL guidance), common law / right-to-control test (IRS three-category framework, Revenue Ruling 87-41), and hybrid tests. Evaluates behavioural control, financial control, and relationship-type factors across federal and state regimes simultaneously. Produces a multi-test risk score with per-regime verdicts, identifies misclassification exposure (back taxes, benefits liability, penalties, class action risk), recommends structural modifications to strengthen contractor status, and generates defensibility documentation. Use when onboarding independent contractors, auditing an existing contractor workforce, responding to a DOL/state agency investigation, evaluating litigation risk, or advising on platform-worker arrangements. Covers US federal (FLSA, IRS, NLRB), all US states with notable ABC-test treatment, UK (IR35 / Off-Payroll Working), EU Platform Work Directive (2024/2831), and Australian post-2024 Fair Work Act framework. Includes Section 530 of the Revenue Act safe harbour analysis.


# Legalcode Independent Contractor Classification

> **Disclaimer**: This skill provides a framework for AI-assisted worker classification
> analysis. It does not constitute legal advice. All outputs must be reviewed by a
> qualified employment and tax lawyer licensed in the relevant jurisdiction(s) before use.
> Worker classification law changes rapidly — statutory amendments, new regulations, and
> court decisions can alter the analysis significantly. Statutory, regulatory, and case law
> references cited from AI memory carry hallucination risk: verify every citation against
> authoritative primary sources before relying on them. Where this skill marks content
> [VERIFY], treat that as a hard requirement, not a suggestion.

---

## Purpose and Scope

This skill analyses whether a specific working relationship is correctly classified as
independent contractor or employee under the primary legal tests applicable in the
worker's and engaging entity's jurisdiction(s). It identifies misclassification risk,
quantifies potential exposure, and recommends structural modifications to defend contractor
status across concurrent legal regimes.

**Covers:**

- Multi-test risk analysis run in parallel: ABC test (state), economic reality test
  (FLSA/federal), IRS common law test (tax), and NLRB standard (labour relations)
- US state-specific assessment for ABC-test and strict-liability states
- UK IR35 / Off-Payroll Working Rules (inside/outside determination)
- EU Platform Work Directive 2024/2831 (rebuttable presumption analysis)
- Australian Fair Work Act §15AA post-2024 practical-reality test
- Section 530 Revenue Act safe harbour analysis (federal tax)
- Voluntary Classification Settlement Program (VCSP) evaluation
- Misclassification exposure quantification (back taxes, penalties, benefits, PAGA/class
  action risk)
- Structural modification playbook to strengthen and document contractor status
- Defensibility documentation audit and recommendations

**Does not:**

- Provide legal advice or replace qualified employment and tax counsel
- Constitute a determination binding on any government agency or court
- Analyse immigration classification (separate skill required)
- Address non-US social security treaty issues beyond the framing identified here
- Apply to statutory employment categories (e.g., statutory employees under IRC § 3121)
  unless flagged as relevant

**Related skills:**

- `legalcode-employment-agreement-review` — for reviewing the employment contract once
  worker is determined to be an employee
- `legalcode-employee-handbook-review` — for handbook compliance once employment status
  is confirmed
- `legalcode-contract-review` — for reviewing the independent contractor agreement itself
- `legalcode-dsar-workflow-builder` — if data privacy obligations triggered by new
  employee classification

---

## Jurisdiction and Governing Law

This skill is multi-jurisdiction by design. Worker classification law applies concurrently
across multiple legal regimes and no single classification applies in all contexts. The
same worker may be:

- An **employee** for purposes of California wage law (AB5 Prong B fails)
- An **independent contractor** for purposes of federal tax (IRS common law test passes)
- **Inside IR35** for UK off-payroll purposes

These regimes operate independently. Satisfying one test does not satisfy another.

**Jurisdiction mapping:** The skill automatically applies tests based on:

1. The state(s) where work is physically performed
2. The state(s) where the engaging entity operates
3. The worker's country of residence (for UK/EU/AU overlay)
4. The governing law clause in the contractor agreement (though this does not displace
   mandatory employment law of the work-performance state)

[JURISDICTION-SPECIFIC] Research and apply when localising:

- State ABC test variations: threshold differs (unemployment insurance only vs. all wage
  law) and Prong B interpretation varies significantly by state
- State workers' compensation mandatory coverage thresholds and penalties
- State unemployment insurance classification rules (may differ from wage law ABC test)
- Provincial/state variations in Australia, Canada [not covered here — see
  `legalcode-us-state-privacy-comparison` for pattern]
- EU member-state implementation of Platform Work Directive 2024/2831 (deadline
  December 2026; implementation varies)
- UK IR35 reforms: Umbrella Reforms effective 2026

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked with **⟁ CLARIFY**
throughout the workflow. Rather than assuming context, the analysis pauses when:

- The answer changes which tests apply or which factors carry more weight
- The relationship exhibits mixed signals requiring user context to resolve
- Multiple valid classification strategies exist and the user's risk tolerance matters
- Jurisdiction requires facts the user must confirm

Present clarification questions as structured options with one recommended default.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Engagement Profile

Accept input describing the working relationship in any of these formats:

- **Contractor agreement**: PDF, DOCX, or pasted text of the written agreement
- **Relationship description**: Narrative description of how the worker actually works
- **Questionnaire responses**: Answers to a structured classification questionnaire
- **Workforce audit list**: Multiple workers to analyse in batch

If no information is provided, gather the minimum information needed using the structured
questionnaire in the Appendix (Classification Intake Questionnaire).

### Step 2: Gather Jurisdictional and Context Information

**⟁ CLARIFY** — Before running the tests, confirm the following. Skip questions already
answered by the input:

1. **Where does the worker physically perform services?**
   - Options: US state(s) — specify which; UK; EU member state(s) — specify which;
     Australia; Multiple/remote — specify all
   - _Why this matters_: The ABC test applies in 33+ US states but with different scope;
     UK IR35 applies only to UK engagements; EU Platform Work Directive applies only to
     platform workers in EU member states.

2. **What is the engaging entity's role?**
   - Options: Client/end-user engaging contractor directly; Staffing/recruitment agency
     in the chain; Digital platform (gig economy); Business acquiring services from
     corporate contractor (PSC/LLC)
   - _Why this matters_: UK IR35 liability shifted to end-user from April 2021; EU
     Directive targets "digital labour platforms"; US joint-employer rules may co-apply.

3. **Is there a written independent contractor agreement?**
   - Options: Yes — provide it; Yes — but informal/unsigned; No written agreement
   - _Why this matters_: Australia post-2024 Fair Work Act §15AA emphasises practical
     reality but written terms remain relevant; IRS and UK IR35 both examine contractual
     terms; absence of written agreement is itself a misclassification risk factor.

4. **What is the purpose of this analysis?**
   - Options: New contractor onboarding (prospective risk); Existing workforce audit
     (retrospective risk); DOL/state agency investigation response; Litigation defence;
     Acquisition due diligence; Platform/product policy review
   - _Why this matters_: Retrospective analysis triggers exposure quantification and
     potential penalty calculations; litigation defence requires privilege framing; DD
     requires historical exposure.

5. **Risk appetite for this engagement:**
   - Options: Conservative (flag any elevated risk, even where IC status likely defensible);
     Balanced (flag material and clear risks only); Business-permissive (flag only clear
     misclassification, document defensible positions)
   - _Why this matters_: Determines how borderline factors are characterised in the output.

### Step 3: Extract and Organise Classification Facts

From the contractor agreement and/or relationship description, extract and organise facts
into the Universal Classification Matrix (UCM):

**Behavioural Control Factors:**

- [ ] Instructions given on how to perform work (methods, tools, sequences)
- [ ] Training provided by the engaging entity
- [ ] Required work hours, schedule, or on-site presence
- [ ] Work product review process (how closely supervised)
- [ ] Reporting requirements and frequency
- [ ] Integration into the entity's organisational structure (org chart, direct manager)
- [ ] Mandatory use of entity's systems, software, or communication tools

**Financial Control Factors:**

- [ ] Method of payment (hourly/salary vs. project/deliverable-based)
- [ ] Whether entity reimburses expenses (all business expenses vs. project-direct only)
- [ ] Whether worker provides own tools and equipment
- [ ] Whether worker has opportunity for profit beyond working more hours
- [ ] Whether worker has risk of loss (unreimbursed expenses, defective work)
- [ ] Whether worker can work for competitors or other clients concurrently
- [ ] Whether worker markets services to the public

**Relationship-Type Factors:**

- [ ] Contract label (independent contractor, employee, worker, vendor)
- [ ] Whether entity provides employee-type benefits
- [ ] Permanency and continuity of the relationship (indefinite vs. project-based)
- [ ] Whether services are integral to entity's core business
- [ ] Right of substitution (can worker send a substitute?)
- [ ] Exclusivity clause (is worker prohibited from other engagements?)
- [ ] Termination provisions (at-will vs. cause required)

**Financial Investment Factors (for economic reality test):**

- [ ] Worker's capital investment in own tools, equipment, facilities
- [ ] Whether investment is proportional to services rendered
- [ ] Whether investment reflects independent business operation

Organise extracted facts into a table with:

- **Factor** | **Facts Extracted** | **IC-Favourable / Employee-Favourable** | **Source (contract clause / practice)**

### Step 4: Apply the Multi-Test Framework

Apply each applicable test in sequence. For US engagements, apply all four federal tests
plus relevant state test(s). For UK/EU/AU, apply the overlay tests described below.

---

#### TEST 1: ABC Test (US States — Where Applicable)

**Applicable jurisdictions (non-exhaustive):** California, Massachusetts, New Jersey,
Illinois, Connecticut, Vermont, Maine, Maryland, Nevada, Oregon, Rhode Island, and 23+
additional states for at least unemployment insurance purposes. [VERIFY current state
roster — legislative changes are frequent.]

**Trigger states (most restrictive application):**

- **California (AB5, Lab. Code §2750.3; Dynamex Operations West, Inc. v. Superior Court
  (2018) 4 Cal.5th 903):** ABC test applies to all Labor Code provisions. Failure of
  any single prong = employee. [VERIFY]
- **Massachusetts (M.G.L. c. 149, §148B):** Strictest in nation — applies to all wage
  law provisions, not just unemployment. Burden on employer to prove all three prongs. [VERIFY]
- **New Jersey (N.J.S.A. 43:21-19(i)(6)):** ABC test for unemployment compensation and
  Wage and Hour Law. NJDOL proposed comprehensive new rules (May 2025, N.J.A.C. 12:11)
  — [VERIFY current adoption status]. [VERIFY]

**Three Prongs — evaluate each independently:**

**Prong A — Freedom from Control:**
Worker is free from the control and direction of the engaging entity in performing work,
both under the contract and in fact.

| Sub-factor            | IC Indicators                       | Employee Indicators                         |
| --------------------- | ----------------------------------- | ------------------------------------------- |
| Work method direction | Entity specifies only output/result | Entity prescribes methods, sequences, tools |
| Schedule control      | Worker sets own hours/days          | Entity mandates hours, on-site presence     |
| Direct supervision    | Minimal/output-based review         | Daily supervision or close oversight        |
| Training              | Worker uses own expertise           | Entity provides job-specific training       |
| Integration           | Worker operates autonomously        | Worker embedded in entity's operations      |

Verdict: **Prong A SATISFIED** / **Prong A FAILED** / **Prong A UNCERTAIN — CLARIFY**

**Prong B — Outside Usual Course of Business:**
Work is outside the usual course of the engaging entity's business, OR is performed
outside all places of business of the entity.

| Sub-factor                | IC Indicators                                     | Employee Indicators                               |
| ------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| Core business test        | Worker performs ancillary/specialty function      | Worker performs entity's primary revenue function |
| Location test             | Work performed entirely at worker's own premises  | Work performed at entity's premises               |
| Business unit integration | Worker not on entity's org chart or business unit | Worker assigned to business unit/team             |

> **Critical note (Prong B):** This prong is the most difficult to satisfy for gig
> economy platforms and companies whose product IS the labour (e.g., delivery, cleaning,
> rideshare). A driver performing delivery IS the usual course of a logistics company's
> business. [JURISDICTION-SPECIFIC] — Prong B is interpreted most strictly in California;
> some states apply a more flexible "location" alternative. [VERIFY]

Verdict: **Prong B SATISFIED** / **Prong B FAILED** / **Prong B UNCERTAIN — CLARIFY**

**Prong C — Independent Established Business:**
Worker is customarily engaged in an independently established trade, occupation, or
business of the same nature as the work performed.

| Sub-factor            | IC Indicators                                      | Employee Indicators                       |
| --------------------- | -------------------------------------------------- | ----------------------------------------- |
| Business registration | Worker has DBA, LLC, or similar                    | Worker has no business entity             |
| Multiple clients      | Worker serves multiple clients                     | Worker's income is 100% from this entity  |
| Marketing             | Worker has website, portfolio, or public marketing | Worker is not publicly available for hire |
| Business investment   | Worker owns tools, IP, systems                     | Worker relies on entity's infrastructure  |
| Prior engagement      | Worker engaged in same work before this entity     | Worker trained exclusively by entity      |

Verdict: **Prong C SATISFIED** / **Prong C FAILED** / **Prong C UNCERTAIN — CLARIFY**

**ABC Test Overall Verdict:**

- All three prongs SATISFIED → **IC classification defensible under ABC test**
- Any single prong FAILED → **EMPLOYEE under ABC test** — proceed to exposure calculation
- Any prong UNCERTAIN → **Flag for professional review — do not classify as IC without
  resolution**

**⟁ CLARIFY** — If any prong is borderline, present specific facts and ask: "The following
facts point in both directions on Prong [X]. Which more accurately describes the
relationship in practice: [Option A] or [Option B]?"

---

#### TEST 2: Federal Economic Reality Test (FLSA)

**Applicable jurisdiction:** All US engagements subject to FLSA (virtually all commercial
engagements).

**Current status (as of March 2026):**

- The DOL's January 2024 final rule (29 C.F.R. Part 795, effective March 11, 2024) was
  suspended from enforcement on May 1, 2025 via Field Assistance Bulletin No. 2025-1.
  [VERIFY]
- DOL announced intent to rescind the 2024 rule and issued a proposed replacement rule
  on February 26, 2026 (60-day comment period through April 28, 2026). [VERIFY]
- For DOL enforcement purposes: interim standard reverts to 2008 Fact Sheet #13
  "economic reality" framework. Private litigation under FLSA may continue to invoke
  the 2024 rule pending court resolution. [VERIFY]

Apply the **six-factor "totality of circumstances" analysis** (no single factor is
determinative or given automatic greater weight):

| Factor                                | IC Indicators                                                                                                                                   | Employee Indicators                                                                 | Weight |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------ |
| **1. Opportunity for Profit or Loss** | Worker can earn more through skill/business judgment (not just working more hours); bears unreimbursed losses                                   | Fixed rate regardless of business acumen; no meaningful risk of loss                | High   |
| **2. Investments**                    | Worker makes capital investment in tools, equipment, or marketing comparable in kind (not necessarily dollar amount) to entity's investment     | Entity provides all tools, systems, infrastructure                                  | Medium |
| **3. Permanency of Relationship**     | Definite project term; non-exclusive; works for multiple clients simultaneously                                                                 | Indefinite/open-ended; exclusive; primary income source                             | High   |
| **4. Nature and Degree of Control**   | Entity controls only deliverables/output; worker sets own hours, methods; entity's control is contractual compliance, not operational oversight | Entity controls methods, hours, location, performance standards; direct supervision | High   |
| **5. Work Integral to Business**      | Services are peripheral, supplementary, or specialty input                                                                                      | Services are core to entity's commercial operations                                 | Medium |
| **6. Skill and Initiative**           | Worker exercises specialised skill and independent business initiative; brings expertise entity does not have                                   | Work is routine, unskilled, or performed under entity's direction                   | Medium |

**Economic Reality Analysis:**
For each factor, classify as: **Strongly IC / Somewhat IC / Neutral / Somewhat Employee /
Strongly Employee**

Tally: IC-leaning factors vs. Employee-leaning factors. Apply totality-of-circumstances
weight.

**FLSA Verdict:** **IC Status Defensible** / **HIGH EMPLOYEE RISK** / **BORDERLINE — Seek
Counsel**

---

#### TEST 3: IRS Common Law Test (Federal Tax Classification)

**Applicable jurisdiction:** All US engagements — governs whether entity must withhold
income tax and pay FICA, FUTA.

**Three-category framework (current IRS guidance, IRS Publication 15-A, Topic No. 762):**
[Note: IRS no longer uses the historical 20-factor Revenue Ruling 87-41 test as its
primary framework — though individual factors may arise in audits. [VERIFY]]

**Category 1 — Behavioural Control:**
Does the entity have the right to direct or control how work is accomplished (not just
what the result must be)?

- **Instructions:** Does entity prescribe specific methods, sequences, or tools? → Employee
- **Training:** Does entity require use of particular work methods via training? → Employee
- **Evaluation:** Does entity evaluate work process (not just results)? → Employee
- **Reporting:** Does entity require regular status reports, timesheets, check-ins? → Employee

**Category 2 — Financial Control:**
Does the entity have the right to control the economic aspects of the worker's job?

- **Payment method:** Fixed wage/salary → Employee; Project fee or deliverable rate → IC
- **Expense reimbursement:** All business expenses reimbursed → Employee; Worker bears costs → IC
- **Tools:** Entity provides all tools → Employee; Worker provides own equipment → IC
- **Profit opportunity:** Worker can profit through efficient operation → IC; Worker earns only fixed rate → Employee
- **Services available to market:** Worker actively markets to other clients → IC; Worker's services exclusively used by entity → Employee

**Category 3 — Type of Relationship:**
How do the parties perceive and structure their relationship?

- **Written contracts:** Agreement labels relationship as IC, describes scope-based work → IC; Agreement describes job duties, schedule, reports-to structure → Employee
- **Employee-type benefits:** Health insurance, retirement plan, paid leave, expense accounts → Employee indicator
- **Permanency:** Open-ended, indefinite relationship → Employee; Project-limited, defined-term → IC
- **Services integral:** Work is key/core to entity's operations → Employee; Ancillary or specialist → IC

**IRS Verdict:** **IC Classification Consistent** / **Employee Status Likely — File SS-8** /
**Borderline — Document Reasonable Basis**

> **SS-8 Process note:** Either party may file Form SS-8 (Determination of Worker Status for
> Purposes of Federal Employment Taxes) with the IRS. IRS takes 6+ months to respond and
> the determination is advisory (not binding on courts), but triggers scrutiny. A pending
> SS-8 is a material discovery item in litigation. [VERIFY current IRS processing times]

---

#### TEST 4: Section 530 Safe Harbour Analysis (Revenue Act of 1978)

**Applicable:** US federal employment tax misclassification defence only.

Section 530 provides relief from federal employment tax liability (income tax withholding,
FICA, FUTA) if the taxpayer can prove all three prongs:

**Prong 1 — Reporting Consistency:**

- Did the taxpayer timely file all required information returns treating the worker as
  a non-employee (Form 1099-NEC / 1099-MISC) for all relevant tax years?
- Did any predecessor entity file W-2s for this worker or workers in substantially
  similar positions?
- "Substantially similar position" looks at job duties, not title.

Verdict: **Reporting Consistency MET** / **FAILED** (W-2s filed for similar roles) /
**UNCERTAIN — Verify filing history**

**Prong 2 — Substantive Consistency:**

- Has the taxpayer or any predecessor treated any worker in a "substantially similar
  position" as an employee at any time after December 31, 1977?
- If the entity employs workers doing the same job as the contested contractor → prong
  likely fails.

Verdict: **Substantive Consistency MET** / **FAILED** / **UNCERTAIN**

**Prong 3 — Reasonable Basis:**
The taxpayer must show reliance on at least one of these four safe-harbour bases:

| Basis                                     | What Qualifies                                                                                                    | Notes                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Judicial Precedent / Published Ruling** | Reliance on court decision, published IRS ruling, technical advice memorandum, or IRS private letter ruling       | Most defensible if directly on point                                    |
| **Past IRS Audit**                        | Prior IRS employment tax audit of this taxpayer with no assessment for workers in substantially similar positions | Audit must have actually examined classification, not merely omitted it |
| **Long-Standing Industry Practice**       | Significant segment of the industry treats workers in similar positions as independent contractors                | Must show industry custom, not just employer preference                 |
| **Other Reasonable Basis**                | Subjective good-faith reliance on other grounds                                                                   | Most difficult to defend; requires contemporaneous documentation        |

> **2025 Update:** Revenue Procedure 2025-10 (first major update since RP 85-18, 1985)
> issued updated guidance on Section 530. The 2025 procedure clarifies burden of proof
> standards and tightens the "reasonable basis" safe harbour. [VERIFY current text of RP
>
> > 2025-10 before advising clients.]

Section 530 relief:

- Protects only from **federal employment tax** liability (not state taxes, not wage law
  claims, not workers' compensation obligations, not benefits claims)
- Available from the first 1099 filing onward (not retroactive to pre-1099 periods)
- Must prove all three prongs; failure of any prong defeats the safe harbour

**Section 530 Verdict:** **Safe Harbour Available** / **Safe Harbour NOT Available —
Full Tax Exposure** / **Partial — Available for [period/regime]**

**Voluntary Classification Settlement Program (VCSP):**
If Section 530 is unavailable and misclassification is likely, evaluate VCSP:

- Allows taxpayers to voluntarily reclassify workers prospectively as employees
- Pay 10% of the employment tax liability that would have been owed (2 most recent years)
- Not subject to interest or penalties for prior misclassification
- Not subject to employment tax audit for prior years for reclassified workers
- Requires filing Form 8952 and meeting eligibility criteria [VERIFY current requirements]

---

#### TEST 5: NLRB Standard (Labour Relations)

**Applicable:** US engagements where the worker performs services in a sector covered by
the NLRA (most private-sector workers).

**Current standard (SuperShuttle DFW, Inc. (2019)):**
NLRB applies a common law multi-factor analysis. Entrepreneurial opportunity for profit
or loss is a significant factor, though not the only one, in determining IC status under
the NLRA. [VERIFY current NLRB position — standard has shifted between administrations]

**Key factors:**

- Whether the entity retains control over the manner and means of work
- Whether the worker has genuine entrepreneurial opportunity (can hire helpers, make
  business investments, profit from efficient operation)
- Whether the worker provides a unique skill that the entity could not easily replace
- Whether the relationship is essentially permanent or project-based

**NLRB note:** The NLRB test operates independently of FLSA and IRS tests. A worker
classified as IC for tax purposes may be an "employee" for NLRA purposes (and thus
protected from retaliation for union organising activity). The NLRB cannot compel
reclassification as an employee for tax purposes, but can require recognition of worker's
Section 7 rights.

**NLRB Verdict:** **IC Status Defensible** / **Employee under NLRA — Section 7 Rights Apply**

---

#### TEST 6: UK IR35 / Off-Payroll Working Rules

**Applicable:** UK engagements where worker provides services through an intermediary
(e.g., personal service company / PSC, umbrella company, partnership).

**Statutory authority:** Chapter 8, Income Tax (Earnings and Pensions) Act 2003 (ITEPA
2003). Off-Payroll Working rules (Chapter 10, ITEPA 2003) effective April 2021 — end-user
organisations (medium and large) are responsible for determining IR35 status. [VERIFY]

**Status Determination Notice (SDN) process:**
End-user organisations must issue a Status Determination Statement (SDS) to the worker
and the party they contract with (fee-payer). [VERIFY current HMRC SDN process]

**Inside/Outside IR35 determination — three key tests:**

**Test A — Mutuality of Obligation (MOO):**

- Is there a mutual obligation? Entity must offer work; worker must accept?
- **Absence of MOO = outside IR35** (genuine IC)
- **MOO present = employee hallmark** (but not determinative alone)
- MOO is assumed in many long-term engagements — examine whether the relationship
  has "gaps" between projects

**Test B — Control:**

- Does the client control WHAT, HOW, WHEN, and WHERE the worker performs services?
- High control over all four dimensions → inside IR35
- Contractor controls own methods and schedule, client controls only deliverables → outside

**Test C — Right of Substitution:**

- Does the contractor have a genuine, unfettered right to send a substitute?
- Substitution right exercised in practice → strong IC indicator
- Substitution theoretically permitted but never exercised → weaker indicator
- No substitution right → inside IR35 indicator

**Additional factors (not determinative alone):**

- Integration into client's business (team membership, security pass, email address)
- Financial risk (bears cost of defective work, provides own tools/equipment)
- Length and continuity of engagement

**HMRC tools:** HMRC Check Employment Status for Tax (CEST) tool — [VERIFY currency and
accuracy]. Note: CEST does not always account for MOO; professional review recommended
for complex cases.

**Consequences of inside IR35:**

- Fee-payer must apply PAYE income tax and National Insurance Contributions (NICs)
- Both employee NICs (12%/2%) and employer NICs (13.8%) apply [VERIFY current rates]
- Apprenticeship Levy (0.5% of payroll above threshold) [VERIFY]
- **2024 Offset Rule:** Tax paid by contractor through self-assessment can offset PAYE
  liability — reduces double-taxation risk for historic cases [VERIFY April 2024 effective date]
- **Umbrella Reforms (expected 2026):** Supply chain liability regime being implemented —
  watch for updates [VERIFY legislative status]

**IR35 Verdict:** **Outside IR35 — IC Status Defensible** / **Inside IR35 — PAYE Applies** /
**Borderline — Issue SDS with Legal Review**

---

#### TEST 7: EU Platform Work Directive (Directive (EU) 2024/2831)

**Applicable:** Engagements through digital labour platforms where the platform worker
provides services in an EU member state.

**Effective date:** December 1, 2024. Member-state implementation deadline: December 2, 2026. [VERIFY each member state's implementation status before advising.]

**Scope:** Applies to "platform work" — services provided via digital labour platforms
(apps, websites, marketplaces) that organise and intermediate between clients and
workers, with algorithmic management. Does NOT automatically apply to all contractor
engagements — must meet the "digital platform" definition. [VERIFY]

**Rebuttable presumption of employment:**
Where facts indicate direction and control consistent with an employment relationship
under applicable national law, there is a legal presumption that the worker is an employee.
**The platform bears the burden of rebutting the presumption.**

[JURISDICTION-SPECIFIC] "Direction and control" defined by national law and collective
agreements of each member state — analyse each member state separately. [VERIFY current
member-state implementing legislation]

**Key criteria indicating direction and control (triggering the presumption — at least 2
of these 5 indicators typically required [VERIFY]):**

1. Setting or capping the level of remuneration paid to workers
2. Requiring the worker to observe binding rules on appearance, conduct toward the recipient
   or performance of the work
3. Supervising performance of work or verifying quality of results
4. Effectively restricting freedom to organise work, choose working hours or periods of
   absence
5. Effectively restricting possibility to build up client base or perform work for third parties

**EU Platform Work Directive Verdict:**

- Fewer than 2 indicators present → **IC Status may be defensible** (no automatic
  presumption; national law applies)
- 2 or more indicators present → **Presumption of Employment** — platform must rebut
- Platform cannot rebut → **Employee status required**

[JURISDICTION-SPECIFIC] Member state variations are material: France, Spain, and Italy
have enacted platform worker protections separately. UK left the EU and Directive does
not apply; but UK has analogous "worker" category and platform-worker cases (Uber v.
Aslam [2021] UKSC 5). [VERIFY]

---

#### TEST 8: Australia — Fair Work Act §15AA (Post-August 2024)

**Applicable:** Australian engagements under the Fair Work Act 2009.

**Legislative evolution:**

- **Personnel Contracting Pty Ltd [2022] HCA 1** and **ZG Operations Pty Ltd v. Jamsek
  [2022] HCA 2**: High Court held classification focuses on rights and duties in the
  written contract where a valid contract exists — ignored practical reality. [VERIFY]
- **Fair Work Legislation Amendment (Closing Loopholes) Act 2023:** Inserted §15AA into
  Fair Work Act, effective August 26, 2024, reversing the High Court's strict contractual
  approach. [VERIFY]

**Post-August 2024 test (§15AA):**
Classification examines the "real substance, practical reality and true nature of the
relationship" — restored multi-factorial examination of how the relationship actually
operates. Written contract terms are relevant but not determinative.

**Factors examined:**

| Factor                      | IC Indicators                            | Employee Indicators                              |
| --------------------------- | ---------------------------------------- | ------------------------------------------------ |
| Degree of control           | Worker controls own methods and schedule | Client directs work methods, hours, location     |
| Personal service obligation | Worker can delegate or subcontract       | Worker must perform services personally          |
| Integration into business   | Worker operates own separate business    | Worker integrated into client's structure        |
| Investment/tools            | Worker provides own tools and equipment  | Client provides all equipment and infrastructure |
| Commercial risk             | Worker bears risk of defective work      | Client bears commercial risk                     |
| Business goodwill           | Worker develops own client goodwill      | Worker's goodwill is client's goodwill           |
| Opportunity for profit      | Worker can profit through efficiency     | Worker earns only agreed rate                    |

**Superannuation note:** Even where a worker is classified as an independent contractor,
they may be entitled to superannuation contributions under the Superannuation Guarantee
(Administration) Act 1992 if they work under a contract that is "principally for the
labour" of the person. [VERIFY current rates — 11.5% (2024-25), rising to 12% by 2025-26]

**Australia Verdict:** **IC Status Defensible** / **Employee Status Likely** /
**Borderline — Practical Reality Assessment Required**

---

### Step 5: Run the Risk Scoring Matrix

After completing all applicable tests, score each test:

| Test                       | Verdict                                      | Risk Level                          |
| -------------------------- | -------------------------------------------- | ----------------------------------- |
| ABC Test (state)           | Passed / Borderline / Failed                 | LOW / MEDIUM / HIGH / CRITICAL      |
| FLSA Economic Reality      | IC Defensible / Borderline / Employee Risk   | LOW / MEDIUM / HIGH / CRITICAL      |
| IRS Common Law (tax)       | IC Consistent / Borderline / Employee Likely | LOW / MEDIUM / HIGH / CRITICAL      |
| Section 530 Safe Harbour   | Available / Partial / Unavailable            | N/A / PARTIAL PROTECTION / CRITICAL |
| NLRB Standard              | IC Defensible / Employee under NLRA          | LOW / HIGH                          |
| UK IR35                    | Outside / Borderline / Inside                | LOW / MEDIUM / HIGH                 |
| EU Platform Work Directive | No Presumption / Presumption Triggered       | LOW / CRITICAL                      |
| Australia FWA §15AA        | IC Defensible / Borderline / Employee        | LOW / MEDIUM / HIGH                 |

**Composite Risk Score:**

| Score        | Characterisation                                                              | Recommended Action                                                                    |
| ------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **CRITICAL** | Fails at least one test decisively; clear employee under law                  | Do not engage as IC; reclassify or restructure immediately                            |
| **HIGH**     | Borderline on 2+ tests or fails 1 test; significant litigation risk           | Engage employment counsel immediately; document defensibility; consider restructuring |
| **MEDIUM**   | Passes most tests with some borderline factors; defensible with documentation | Strengthen agreement and documentation; monitor for regulatory changes                |
| **LOW**      | Passes all applicable tests clearly; well-documented relationship             | Maintain documentation; periodic review (annually)                                    |

**⟁ CLARIFY** — If tests produce conflicting verdicts (e.g., IC under IRS test but
Employee under state ABC test), present to user: "The analysis produces split verdicts
across [X] tests. This is common — different tests serve different legal purposes. Should
the output prioritise: (a) the strictest test (most conservative), (b) the test most
likely to be the basis of a claim (state wage law / DOL), or (c) all tests with per-regime
conclusions?"

---

### Step 6: Quantify Misclassification Exposure

If any test produces HIGH or CRITICAL risk, calculate potential exposure:

#### Federal Tax Exposure (IRS)

**Unintentional misclassification per worker per year:**

- 1.5% of wages (income tax withholding)
- 40% of unpaid FICA taxes (employee portion)
- 100% of employer FICA taxes (7.65% of wages for Social Security/Medicare) [VERIFY current rates]
- $50 per unfiled Form W-2 [VERIFY current amount]
- Interest on unpaid taxes (federal short-term rate + 3 percentage points) [VERIFY]

**Willful misclassification — additional:**

- 100% of income tax withholding (not just 1.5%)
- 100% of FICA (both portions)
- Potential criminal prosecution (18 U.S.C. §7201 tax evasion for extreme cases)

**Illustrative calculation template:**

```
Worker Annual Compensation:        $[X]
Employer FICA Exposure (7.65%):    $[X × 0.0765]
Unintentional Tax Penalty:         $[X × 0.015 + 40% × employee FICA]
Per-Worker Annual Exposure:        $[Sum]
Number of Workers:                 [N]
Lookback Period (years):           [Y — max 3 for willful]
Total Federal Tax Exposure:        $[Per-worker × N × Y]
```

#### State Unemployment Insurance Exposure

- Retroactive unemployment insurance tax assessments (typically 2–5% of wages, varies by state)
- Compound interest on back assessments (typically 6–12% annually) [JURISDICTION-SPECIFIC]
- Experience-rating impact: misclassification may increase entity's future UI rate
- Criminal referral risk in states with strict liability UI misclassification laws

#### FLSA / State Wage and Hour Exposure

- Unpaid overtime (1.5× regular rate for hours over 40/week) [JURISDICTION-SPECIFIC for
  daily overtime — California requires daily OT after 8 hours]
- Minimum wage shortfalls (if contractor was paid below applicable minimum)
- Lookback period: 2 years (federal FLSA); 3 years if willful; state law may extend
  further [JURISDICTION-SPECIFIC — California: 3 years; Massachusetts: 3 years; [VERIFY]]
- **Liquidated damages** equal to unpaid wages (FLSA) — doubles the back-wage number
  unless employer shows good faith
- Attorney's fees and costs (prevailing worker entitled under FLSA §216(b))

#### California-Specific Exposure (PAGA / Class Action)

- **PAGA penalties (Cal. Lab. Code §2699):** $100 per employee per pay period for initial
  violations; $200 per pay period for subsequent violations; 75% goes to state, 25% to
  workers [VERIFY current penalty amounts post-Viking River Cruises v. Moriana (2022)]
- **Willful misclassification fines (Cal. Lab. Code §226.8):** $5,000–$25,000 per worker
  per violation [VERIFY]
- **Class action multiplier:** Single PAGA plaintiff can pursue on behalf of all aggrieved
  workers — exposure scales linearly with workforce size

#### Benefits Liability

- Health insurance premiums: retroactive if entity's plan would have covered the worker
- Retirement plan (401k/ERISA): back contributions plus investment growth loss; plan
  correction requirement
- Paid time off: accrued vacation pay (vested in many states)
- Workers' compensation: direct injury costs if worker injured while uninsured
- FMLA / state leave entitlements: claim exposure for leave denied during misclassification period

**Total Exposure Summary Template:**

```
Federal tax (IRS):                 $[Amount] — [Confidence level]
State unemployment insurance:      $[Amount] — [Confidence level]
Federal FLSA back wages + LD:      $[Amount] — [Confidence level]
State wage and hour:               $[Amount] — [Confidence level]
California PAGA risk:              $[Amount] — [Applicable: Yes/No]
Benefits liability:                $[Amount] — [Confidence level]
Litigation costs (est.):           $[Amount]
Total estimated exposure:          $[Low range] – $[High range]
```

---

### Step 7: Structural Modification Recommendations

For each HIGH or CRITICAL risk factor identified, recommend targeted structural
modifications:

#### Structural Modifications to Reduce Employee-Indicator Factors

**Reduce Behavioural Control:**

- [ ] Rewrite agreement to specify deliverables/outcomes rather than work methods
- [ ] Remove any provisions dictating specific hours, schedule, or on-site presence
- [ ] Eliminate mandatory training provisions (replace with deliverable specifications)
- [ ] Remove integration into entity's reporting structure or organisational chart
- [ ] Replace company email/tools mandate with outcome-based access (contractor uses own)
- [ ] Convert daily supervision to milestone-based output review

**Reinforce Financial Independence:**

- [ ] Convert from hourly/salary to project-fee or deliverable-based compensation
- [ ] Require contractor to provide own tools and equipment (specify in contract)
- [ ] Limit entity's expense reimbursement to direct project costs (not business overhead)
- [ ] Allow contractor to profit from efficient delivery (no cap on sub-project hours)
- [ ] Remove exclusive-dealing provisions (or convert to narrowly scoped exclusivity with
      premium compensation for exclusivity)
- [ ] Add provision acknowledging contractor bears risk of defective work

**Establish Relationship-Type Factors:**

- [ ] Add genuine substitution clause (not illusory — contractor must actually have the
      right and ability to substitute a qualified worker)
- [ ] Convert open-ended engagement to project-based or fixed-term structure
- [ ] Remove (or strictly scope) non-compete provisions that limit other client work
- [ ] Exclude contractor from entity's employee benefits (explicit benefit exclusion)
- [ ] Add periodic agreement renewals rather than assumed continuation
- [ ] Document contractor's independent business (require evidence of business licence,
      other clients, or professional portfolio)

**Demonstrate Independent Contractor Status:**

- [ ] Require Form W-9 and record of tax ID
- [ ] Require contractor to maintain business liability insurance (and provide certificate)
- [ ] Allow and document contractor serving other clients concurrently
- [ ] Keep evidence of contractor's independently established business

**Prong B (ABC Test) — Outside Usual Course of Business:**
If Prong B fails, the relationship may not be repairable through structural modification.
Consider:

- [ ] Whether a true arm's-length subcontractor or vendor relationship can be structured
      (e.g., contractor's LLC provides services as B2B vendor, not as personal services IC)
- [ ] Whether the function can be genuinely outsourced (staffing agency, consulting firm)
      so the entity contracts with a business entity, not an individual
- [ ] Whether worker should simply be reclassified as employee — some relationships cannot
      be made IC-compliant without abandoning the function

---

### Step 8: Defensibility Documentation Audit

Generate a documentation gap analysis. For each item, indicate: **Present / Absent /
Needs Revision**

**Core Documentation:**

- [ ] Signed written independent contractor agreement (with proper clauses)
- [ ] Statement of Work (SOW) or scope-limited project description
- [ ] Form W-9 obtained and filed
- [ ] 1099-NEC / 1099-MISC filed for all years with payments ≥$600 (or applicable
      threshold) [VERIFY current threshold]
- [ ] Contractor classification assessment documented in writing (contemporaneous)
- [ ] Evidence of reasonable basis for IC classification (for Section 530)

**Operational Documentation (to show practical reality):**

- [ ] Invoices issued by contractor (not time-sheets like an employee)
- [ ] Records showing contractor worked for other clients during same period
- [ ] Records of contractor's own business registration/licence
- [ ] Evidence contractor maintains own business insurance
- [ ] No W-2s issued to this worker or similar workers
- [ ] Performance communications focused on deliverables, not process

**Periodic Review Documentation:**

- [ ] Annual contractor relationship review record
- [ ] Documentation of any material changes in work arrangement
- [ ] Evidence that classification was reconsidered when relationship evolved

**⟁ CLARIFY** — "Do you want me to generate a Contractor Classification Assessment
memorandum that can be saved to the worker's file as contemporaneous evidence of the
classification decision and its reasonable basis?"

---

### Step 9: Produce Findings and Recommendations

Present findings in the Output Format Template (see below), organising by:

1. Per-test verdict with key supporting and adverse factors
2. Composite risk score with narrative
3. Quantified exposure estimate (range)
4. Prioritised structural modification recommendations
5. Documentation gap list with remediation actions
6. Recommended next steps

---

## Deep Topic Analysis Reference — Test-by-Test Factor Tables

### ABC Test Factor Reference

**States where ABC test applies (to unemployment insurance at minimum) — partial list:**
[VERIFY current state roster before advising — legislative changes are frequent]

| State         | Statute                  | Scope                        | Notable Feature                                                 |
| ------------- | ------------------------ | ---------------------------- | --------------------------------------------------------------- |
| California    | Lab. Code §2750.3 (AB5)  | All labor code provisions    | Strictest Prong B; PAGA enforcement                             |
| Massachusetts | M.G.L. c. 149, §148B     | All wage law provisions      | Prong C: business must be operating at time of work             |
| New Jersey    | N.J.S.A. 43:21-19(i)(6)  | Unemployment + Wage/Hour Law | 2025 proposed comprehensive rules                               |
| Connecticut   | Conn. Gen. Stat. §31-222 | Unemployment                 | Three-prong test                                                |
| Illinois      | 820 ILCS 185/10 (IWPCA)  | Wage Payment Act             | Prong B: outside usual course or outside all places of business |
| Vermont       | 21 V.S.A. §1455          | Unemployment                 | ABC test applies                                                |
| Maine         | 26 M.R.S. §1043(11)(E)   | Unemployment                 | All three prongs required                                       |
| Oregon        | O.R.S. §670.600          | Unemployment + Workers' Comp | Specific statutory exemptions                                   |
| Nevada        | N.R.S. §612.085          | Unemployment                 | All three prongs required                                       |
| New Hampshire | RSA 275:4                | Wage/Hour                    | All three prongs required                                       |
| Rhode Island  | G.L. §28-29-2            | Workers' Compensation        | All three prongs required                                       |

[VERIFY each state's current statute text and scope of application — this table reflects
published information as of early 2026 and may not capture recent legislative amendments.]

---

### Industry-Specific Risk Markers

**Technology / IT consulting:**

- IC-FAVOURABLE: Specialised technical skills not available in-house; project-defined
  engagements; contractor uses own development tools and environment
- RISK FACTORS: Embedded in dev team (daily standups, Jira tickets, company Slack);
  indefinite engagement with same project team; single client for 100%+ of income
- ABC Prong B risk: Core product development IS the software company's primary business

**Healthcare / Clinical (locum tenens, per diem nurses):**

- IC-FAVOURABLE: Licensed professionals; single-shift or per-episode arrangements;
  no long-term relationship; worker maintains independent licence
- RISK FACTORS: Credential verification and scheduling control by entity; mandatory use
  of entity's protocols; ongoing relationship with same facility
- [JURISDICTION-SPECIFIC] Healthcare workers may be subject to state-specific safe harbours

**Creative / Freelance (writers, designers, photographers):**

- **Copyright Act "work made for hire" caution:** If a work is commissioned as a work
  made for hire, the commissioning party (not the creator) owns copyright. But 17 U.S.C.
  §101 provides that independent contractors can create work-for-hire only in 9 specified
  categories — other commissioned works require written assignment. [VERIFY list of 9
  categories; this affects both IP and sometimes classification arguments.]
- IC-FAVOURABLE: Portfolio career; multiple concurrent clients; creatives provide own
  equipment; deadline-based (not schedule-based) relationship
- RISK FACTORS: Exclusive output arrangements; frequent communication and direction over
  creative process; long-term exclusive relationship

**Transportation / Gig / Last-Mile Delivery:**

- HIGHEST RISK for ABC Prong B: Delivery IS the usual course of business for a delivery
  platform
- California AB5 has specific carve-outs for some transportation workers — [VERIFY current
  carve-out status and Prop 22 legal status post-California Supreme Court review]
- EU Platform Work Directive directly targets this sector
- Structural argument: B2B arrangement between platform and owner-operator LLC, not
  individual personal services

**Construction:**

- Many states have specific construction-industry ABC test rules
- [JURISDICTION-SPECIFIC] Joint employer / general contractor liability for
  subcontractor workers varies significantly by state
- Davis-Bacon Act / prevailing wage laws may impose employment-like obligations on
  contractors on federal projects [VERIFY]

---

## Severity Classification

Apply the following classification scheme to each identified risk factor:

| Level        | Symbol | Definition                                                                                                                                                                   | Required Response                                                                                                                            |
| ------------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL** | 🔴     | Clear misclassification — fails one or more applicable tests decisively; any agency or court reviewing the relationship would likely find employee status                    | Immediately engage employment and tax counsel; halt new IC onboarding in this category; evaluate immediate reclassification or restructuring |
| **HIGH**     | 🟠     | Likely misclassification — relationship borderline on 2+ tests or fails 1 test; audit trigger risk elevated; class action plaintiff bar likely to target this classification | Engage counsel within 30 days; document reasonable-basis defence; implement structural modifications; evaluate VCSP                          |
| **MEDIUM**   | 🟡     | Defensible classification — passes most applicable tests but has identifiable weak factors; risk increases if relationship evolves without documentation                     | Strengthen documentation; tighten agreement language; set annual review reminder; monitor regulatory developments                            |
| **LOW**      | 🟢     | Clearly defensible classification — passes all applicable tests with well-documented support                                                                                 | Maintain documentation; review annually; update when regulatory changes occur                                                                |

---

## Actionable Output per Finding

For each finding, produce:

```
Factor: [Factor name]
Test(s) affected: [ABC / FLSA / IRS / IR35 / other]
Current facts: [What the relationship exhibits]
Risk classification: 🔴 CRITICAL / 🟠 HIGH / 🟡 MEDIUM / 🟢 LOW
Why it matters: [Plain-language explanation of legal significance]
Modification recommended:
  - Agreement change: [Specific clause language to add/remove/revise]
  - Operational change: [How day-to-day practice needs to change]
  - Documentation: [What evidence to create and preserve]
Confidence: [Definite / High / Probable / Possible / Unlikely]
```

---

## Prioritisation Framework

After generating all findings, prioritise remediation:

**Tier 1 — Immediate Action (within 5 business days):**

- Any CRITICAL finding (clear misclassification)
- Any finding that triggers imminent state agency audit risk
- Any finding where a worker has already filed a misclassification complaint
- Section 530 safe harbour not available + IRS audit pending

**Tier 2 — Short-Term Action (within 30 days):**

- Any HIGH finding across multiple tests
- ABC test failures in California, Massachusetts, or New Jersey (highest enforcement risk)
- Documentation gaps that undermine Section 530 safe harbour
- UK IR35 Status Determination Statement not issued where required

**Tier 3 — Periodic Action (within 90 days or next agreement renewal):**

- MEDIUM findings addressable at next contract renewal
- Documentation strengthening for currently defensible relationships
- Monitoring plan for regulatory changes (DOL 2026 proposed rule, EU Directive implementation)

---

## Citation Quality Gates

Before delivering any output, silently run these five quality gates. Revise before
delivering if any gate fails.

| Gate           | Rule                                                                                                                                                            | Fail Action                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Source**     | Every legal conclusion cites a specific statute, regulation, case, or established classification principle                                                      | Add citation or mark [UNVERIFIED]         |
| **Format**     | All citations follow consistent, recognisable format for the jurisdiction (statute name + section + year where known)                                           | Fix format                                |
| **Currency**   | Every cited provision verified against known amendments (DOL 2024 rule status; California AB5 exceptions; UK IR35 reforms; EU Directive implementation status)  | Flag [CHECK CURRENCY]                     |
| **Domain**     | Analysis stays within the skill's governing law scope — do not apply California ABC test to a Texas-only engagement without noting California's inapplicability | Remove or flag cross-jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden; borderline verdicts labelled as such                                                                                 | Add confidence qualifier                  |

---

## Self-Interrogation for Critical-Risk Classifications

For any finding classified CRITICAL, apply this three-pass review:

**Pass 1 — Legal Chain Integrity:**
Does the CRITICAL classification follow logically from the stated facts and the
applicable legal test? Would a court, DOL investigator, or state AG viewing these
same facts reach the same conclusion? Is the key controlling factor clearly established
in the relationship (not merely speculative)?

**Pass 2 — Completeness:**
Have all applicable tests been considered for this specific relationship? Are there
regulatory dimensions beyond the primary test that would affect the CRITICAL conclusion
(e.g., does the CRITICAL ABC-test failure also trigger FUTA liability? Does it activate
California PAGA in addition to wage claims)? Have available defences (Section 530,
VCSP, industry-practice argument) been evaluated?

**Pass 3 — Counter-Argument:**
What is the strongest argument that the relationship IS a legitimate IC arrangement?
Under what interpretive framework would a qualified defence counsel argue for IC status?
Does that argument succeed, or does it confirm CRITICAL classification? Document both
sides.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                    | Action                                           |
| ------------ | --------- | ---------------------------------------------------------- | ------------------------------------------------ |
| **Definite** | 0.95–1.0  | Clear settled law on these facts                           | State with confidence                            |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions remain      | State with brief caveat                          |
| **Probable** | 0.60–0.79 | Good arguments for this conclusion; some contra-indicators | State with reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuinely uncertain — expert opinions would differ         | Flag for professional review; present both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                    | Do not assert; flag [UNCERTAIN]                  |

Apply confidence scoring at the factor level (within findings) and at the overall-verdict
level. A CRITICAL overall verdict requires HIGH or Definite confidence; a CRITICAL verdict
at Probable or below should be presented as HIGH pending professional review.

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-independent-contractor-classification"
  mode: "Created from scratch"
  topic: "Independent contractor vs. employee worker classification"
  jurisdiction: "Multi-jurisdiction: US (federal + all states), UK, EU, AU"
  source_skills_analyzed: 0
  enhancement_type: "Create"
  legalcode_mcp: "Not connected — references marked [VERIFY]"
  research_reference_file: "Not created"
  quality_score: "[To be scored on delivery]"
  completeness: "18/18 elements present"
  citations_verified: "[Reported as VERIFY throughout — verify against primary sources]"
  confidence: "MEDIUM — regulatory environment in flux (DOL 2024 rule suspended;
    EU Directive pending member-state implementation; AU post-2024 amendment; UK
    Umbrella Reforms pending)"
  tests_applied:
    - name: "ABC Test"
      jurisdictions: "California, Massachusetts, New Jersey, Illinois, 33+ states"
      prongs:
        [
          "A — Control",
          "B — Usual Course of Business",
          "C — Independent Business",
        ]
    - name: "Federal Economic Reality Test"
      statute: "FLSA; 29 CFR Part 795 (2024 rule — enforcement suspended)"
      factors:
        [
          "Profit/Loss Opportunity",
          "Investments",
          "Permanency",
          "Control",
          "Integral to Business",
          "Skill/Initiative",
        ]
    - name: "IRS Common Law Test"
      guidance: "IRS Topic 762; Rev. Rul. 87-41"
      categories:
        ["Behavioural Control", "Financial Control", "Type of Relationship"]
    - name: "Section 530 Safe Harbour"
      statute: "Revenue Act of 1978, §530; Rev. Proc. 2025-10"
      prongs:
        ["Reporting Consistency", "Substantive Consistency", "Reasonable Basis"]
    - name: "NLRB Standard"
      case: "SuperShuttle DFW, Inc. (2019)"
    - name: "UK IR35"
      statute: "ITEPA 2003, Chapter 8 and 10"
      tests: ["Mutuality of Obligation", "Control", "Right of Substitution"]
    - name: "EU Platform Work Directive"
      directive: "Directive (EU) 2024/2831"
      test: "Rebuttable presumption of employment"
    - name: "Australia Fair Work Act"
      statute: "Fair Work Act 2009, §15AA (post-August 2024)"
      test: "Real substance, practical reality and true nature of relationship"
  limitations:
    - "DOL 2024 rule enforcement suspended — federal FLSA analysis uses interim 2008 framework"
    - "EU Directive implementation varies by member state — member-state law must be verified"
    - "Section 530 Rev. Proc. 2025-10 text not verified — confirm current requirements"
    - "All state statute citations require verification against current text"
    - "Australia superannuation obligation may apply to some IC arrangements"
    - "Skill does not cover Canada, Singapore, India, or LATAM jurisdictions"
  reviewer:
    "AI-assisted — requires review by qualified employment and tax counsel in
    each applicable jurisdiction"
```

---

## Anti-Patterns

Avoid these common misclassification mistakes when advising on or structuring contractor
relationships:

1. **The "Label-Only" Defence:** Putting "independent contractor" in the agreement title
   while the relationship operates exactly like an employment relationship. Courts and
   agencies look through labels to substance. A label is worth nothing if the facts
   contradict it.

2. **Ignoring State ABC Tests When Hiring In High-Risk States:** Relying on the IRS common
   law test (which the company passes) while ignoring California AB5 or Massachusetts
   M.G.L. c. 149 §148B (which it fails). Federal tax compliance does not cure state wage
   law misclassification.

3. **Indefinite Engagements Without Project Structure:** Engaging a contractor under an
   open-ended "master agreement" with no defined term, deliverables, or end date creates a
   permanency indicator across every applicable test.

4. **Exclusive Dedication Requirements:** Requiring a contractor to dedicate 100% of
   working time to the engaging entity (even without labelling it exclusivity) is a strong
   employee indicator under both the economic reality and ABC tests.

5. **Integration into Org Chart and Communication Systems:** Giving the contractor a
   company email address, listing them on the org chart, assigning a direct manager who
   conducts performance reviews, and including them in company-wide communications all
   signal employment regardless of the contract label.

6. **Failure to File 1099s:** Not filing required 1099-NEC forms destroys Section 530
   safe harbour protection on the "reporting consistency" prong — and separately triggers
   its own tax penalties.

7. **Treating Similar Workers Inconsistently:** Classifying some workers performing
   identical roles as employees (W-2) and others as ICs (1099) — this defeats both the
   Section 530 substantive-consistency prong and weakens all other defences.

8. **Reimbursing All Business Expenses:** Covering overhead expenses (phone, internet,
   office supplies, equipment) that an employee would normally receive employer
   reimbursement for — turns financial risk over to the entity, a strong employee
   indicator under the economic reality test.

9. **Illusory Substitution Rights:** Including a substitution clause that the contractor
   has no practical ability to exercise (e.g., requires company approval of any substitute,
   or the work requires personal skill that makes substitution impossible). Courts
   recognise illusory rights.

10. **Confusing Tax Classification with Labor Law Classification:** Treating a worker as
    an IC for tax (1099) and simultaneously providing FMLA, paid leave, or health insurance
    participation — creates liability exposure on both sides simultaneously.

11. **Failing to Document the Reasonable Basis for Classification:** Making the IC
    classification decision verbally or based on industry custom without any contemporaneous
    written record — destroys Section 530 protection and leaves no evidence for litigation
    defence.

12. **Algorithmic Control Blind Spot (Platforms):** Assuming that algorithmic management
    (app-based scheduling, rating systems, route optimisation, price-setting) does not
    constitute "control" for classification purposes. Courts have found that algorithmic
    control can satisfy the control prong of both ABC and economic reality tests.

13. **Sole-Client Trap:** Allowing a contractor relationship to evolve into a sole-client
    arrangement (contractor works 40 hours/week exclusively for one entity for years) —
    this is the strongest single predictor of employee classification across all tests.

14. **Not Reviewing When Relationships Evolve:** Treating classification as a one-time
    decision at contract signing, without reviewing when the worker takes on new duties,
    works more hours, joins a project team, or receives company training.

15. **Inadequate Geographic Analysis for Remote Workers:** Classifying a remote contractor
    without identifying which state(s) the work is being performed in — and thus which
    state ABC tests and wage laws apply. A California-resident contractor performing work
    in California for a non-California company is still subject to AB5.

16. **Prong B Wishful Thinking:** Concluding that Prong B is satisfied because the
    contractor has a specialist skill (e.g., software engineer) without analysing whether
    the engaging entity's core business IS software — in which case Prong B almost always
    fails for core product development work.

17. **Ignoring Workers' Compensation Insurance Requirements:** Many states require
    workers' compensation coverage for any worker meeting the state's employee definition
    for workers' comp purposes — which may differ from the wage law definition. Failing
    to carry coverage when required is a separate statutory violation with independent
    penalties.

18. **UK IR35 Status Determination Not Issued:** For medium and large UK end-user
    organisations engaging contractors through PSCs, failing to issue a Status Determination
    Statement (SDS) is a separate compliance failure — liability falls to the end-user
    by default if no SDS is issued.

19. **EU Platform Work Directive Complacency:** Assuming the December 2026 implementation
    deadline means no action needed now — member states may implement early, workers may
    bring claims under existing national law in the meantime, and platform worker
    litigation is already active in major EU jurisdictions.

20. **Ignoring Superannuation Obligations (Australia):** Classifying a worker as an IC
    and not providing superannuation contributions — if the contract is "principally for
    labour," super obligations may apply regardless of IC classification under the SGA
    Act.

21. **PAGA Threat Underestimation (California):** Treating California misclassification
    as a bilateral wage claim risk without accounting for PAGA — which allows any single
    aggrieved employee to sue on behalf of all current and former aggrieved workers in the
    state, with per-pay-period penalties that scale with workforce size.

22. **Conflating Contract Validity with Classification Validity:** Arguing that the IC
    agreement is "valid" (signed, governed by applicable state law, enforceable on its
    terms) as a defence to misclassification — contract validity and classification
    validity are separate analyses. A binding contract can still describe an employment
    relationship.

---

## Writing Standards

Before delivering any output:

1. **Precision over caution-speak:** Do not substitute vague language for analysis. "This
   may or may not be classified as..." without supporting reasoning is worse than a clear
   conclusion with qualifications.

2. **Verdict-first structure:** Lead with the per-test verdict, then the supporting
   factors, then the remediation. Do not bury the conclusion in analysis.

3. **Plain language:** Explain legal conclusions in terms a non-lawyer can act on.
   Reserve statutory citations for the footnote/source row of each finding.

4. **Flag regulatory flux prominently:** The DOL 2024 rule enforcement suspension, the
   pending 2026 rule, and the EU Directive implementation timeline are material to advice.
   Always note the current regulatory status when invoking federal FLSA analysis.

5. **No false certainty:** Where a factor is genuinely borderline (Probable / Possible
   confidence), say so and present both sides. A 60/40 conclusion presented as definite
   exposes the user to unexpected litigation risk.

6. **Jurisdiction-first labelling:** Begin every jurisdiction-specific finding with the
   jurisdiction label in brackets — `[CALIFORNIA]`, `[UK]`, `[EU]`, `[AUSTRALIA]` — so
   multi-jurisdiction outputs are scannable.

7. **Quality gate before delivery:** Run Citation Quality Gates silently; run
   Self-Interrogation for every CRITICAL finding; verify that all test verdicts are
   internally consistent before presenting the composite score.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current state ABC test legislation and recent amendments
- Search for current DOL enforcement guidance and any FLSA 2026 rule finalization
- Verify Section 530 Revenue Procedure 2025-10 text
- Verify UK IR35 Umbrella Reform legislative status
- Search for member-state implementing legislation for EU Platform Work Directive
- Retrieve recent case law (California AB5 carve-out litigation, Uber v. Aslam progeny,
  Australian Fair Work Commission decisions)

**Without legalcode-mcp:**

- Rely on research conducted at skill invocation time; mark all statutory and case law
  references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Advise user that all statutory citations require primary-source verification before
  reliance

---

## Output Format Template

```markdown
# Independent Contractor Classification Analysis

**Entity:** [Engaging entity name / type]
**Worker/Role:** [Worker name or role description]
**Analysis date:** [Date]
**Jurisdiction(s):** [All jurisdictions where tests applied]
**Purpose:** [Onboarding / Audit / Investigation response / DD / Litigation defence]

---

## Executive Summary

**Composite Risk Score:** 🔴 CRITICAL / 🟠 HIGH / 🟡 MEDIUM / 🟢 LOW

[2–3 sentence summary of the overall classification risk, the tests that drive the
highest risk, and the primary recommended actions.]

---

## Per-Test Verdicts

### ABC Test — [State(s)]

**Verdict:** IC Status Defensible / EMPLOYEE — All Three Prongs Not Satisfied
| Prong | Finding | Key Facts | IC/Employee Indicator |
|-------|---------|-----------|----------------------|
| A — Control | Satisfied / Failed / Borderline | [Facts] | IC / Employee |
| B — Usual Course of Business | Satisfied / Failed / Borderline | [Facts] | IC / Employee |
| C — Independent Business | Satisfied / Failed / Borderline | [Facts] | IC / Employee |

**ABC Test Risk Level:** 🔴 / 🟠 / 🟡 / 🟢

---

### Federal Economic Reality Test (FLSA)

**Applicable standard:** [2008 interim framework / 2024 rule (private litigation) — note regulatory status]
**Verdict:** IC Status Defensible / HIGH Employee Risk / Borderline

| Factor                         | Verdict                 | Key Facts | Confidence |
| ------------------------------ | ----------------------- | --------- | ---------- |
| 1. Opportunity for Profit/Loss | IC / Employee / Neutral | [Facts]   | [Level]    |
| 2. Investments                 | IC / Employee / Neutral | [Facts]   | [Level]    |
| 3. Permanency                  | IC / Employee / Neutral | [Facts]   | [Level]    |
| 4. Control                     | IC / Employee / Neutral | [Facts]   | [Level]    |
| 5. Integral to Business        | IC / Employee / Neutral | [Facts]   | [Level]    |
| 6. Skill and Initiative        | IC / Employee / Neutral | [Facts]   | [Level]    |

**FLSA Risk Level:** 🔴 / 🟠 / 🟡 / 🟢

---

### IRS Common Law Test (Federal Tax)

**Verdict:** IC Classification Consistent / Employee Status Likely / Borderline

| Category             | Key Factors        | IC/Employee Indicator | Confidence |
| -------------------- | ------------------ | --------------------- | ---------- |
| Behavioural Control  | [List key factors] | IC / Employee         | [Level]    |
| Financial Control    | [List key factors] | IC / Employee         | [Level]    |
| Type of Relationship | [List key factors] | IC / Employee         | [Level]    |

**IRS Risk Level:** 🔴 / 🟠 / 🟡 / 🟢

---

### Section 530 Safe Harbour

**Verdict:** Available / Partial / NOT Available

| Prong                   | Status                   | Notes                      |
| ----------------------- | ------------------------ | -------------------------- |
| Reporting Consistency   | Met / Failed / Uncertain | [1099 filing history]      |
| Substantive Consistency | Met / Failed / Uncertain | [Similar worker treatment] |
| Reasonable Basis        | Met / Failed / Uncertain | [Basis relied upon]        |

**VCSP candidate:** Yes / No / Evaluate

---

### [UK IR35 — if applicable]

**Verdict:** Outside IR35 / Inside IR35 / Borderline
| Test | Finding | Key Facts |
|------|---------|-----------|
| Mutuality of Obligation | Present / Absent | [Facts] |
| Control | High / Low | [Facts] |
| Right of Substitution | Genuine / Illusory / Absent | [Facts] |

**IR35 Risk Level:** 🔴 / 🟠 / 🟡 / 🟢

---

### [EU Platform Work Directive — if applicable]

**Verdict:** No Presumption Triggered / Presumption of Employment Triggered
**Indicators present:** [List which of 5 indicators are met]
**Directive implementation status in [Member State]:** [Current status — VERIFY]

---

### [Australia Fair Work Act — if applicable]

**Verdict:** IC Status Defensible / Employee Status Likely / Borderline
[Key practical reality factors supporting each side]

---

## Composite Risk Score and Narrative

**Overall Classification Risk:** 🔴 CRITICAL / 🟠 HIGH / 🟡 MEDIUM / 🟢 LOW

[Narrative of how tests interact; explain any split verdicts across regimes.]

---

## Misclassification Exposure Estimate

| Category                                       | Estimated Exposure   | Confidence  |
| ---------------------------------------------- | -------------------- | ----------- |
| Federal tax (IRS)                              | $[Range]             | [Level]     |
| State unemployment insurance                   | $[Range]             | [Level]     |
| Federal FLSA (back wages + liquidated damages) | $[Range]             | [Level]     |
| State wage and hour                            | $[Range]             | [Level]     |
| California PAGA (if applicable)                | $[Range]             | [Level]     |
| Benefits liability                             | $[Range]             | [Level]     |
| **Total estimated exposure**                   | **$[Low] – $[High]** | **[Level]** |

_All exposure estimates are indicative. Actual liability depends on facts established in
litigation or audit and applicable limitations periods._

---

## Structural Modification Recommendations

### Tier 1 — Immediate Action

- [Specific recommendations with urgency rationale]

### Tier 2 — Short-Term (within 30 days)

- [Specific recommendations]

### Tier 3 — Next Contract Renewal

- [Specific recommendations]

---

## Documentation Gap Analysis

| Document                       | Status                            | Action Required            |
| ------------------------------ | --------------------------------- | -------------------------- |
| Written IC agreement           | Present / Absent / Needs Revision | [Action]                   |
| Form W-9                       | Present / Absent                  | Obtain before next payment |
| 1099-NEC (all years)           | Filed / Missing / Incorrect       | File amended/late returns  |
| Classification assessment memo | Present / Absent                  | Draft and file             |
| Evidence of multiple clients   | Present / Absent                  | Collect and document       |
| [Other items]                  |                                   |                            |

---

## Recommended Next Steps

1. [Most urgent action — tie to CRITICAL/HIGH findings]
2. [Structural or documentation actions]
3. [Monitoring actions — regulatory developments to watch]
4. [Professional referrals — when to engage counsel immediately]

---

## Assumptions and Limitations

- [State all assumptions made due to missing information]
- [Flag any areas where additional facts would change the analysis]
- [Note regulatory flux warnings]
- [Reiterate professional review requirement]

---

_Analysis generated by legalcode-independent-contractor-classification skill. Not legal
advice. Verify all statutory and regulatory citations against current primary sources.
Review by qualified employment and tax counsel required before reliance._
```

---

## Appendix: Classification Intake Questionnaire

Use this questionnaire when no contractor agreement or relationship description is provided.
Present as a structured set of questions.

**Section 1 — The Relationship**

1. What services does the worker perform?
2. In what state(s) does the worker physically perform services?
3. Is the worker a US person? If not, which country?
4. Is the worker an individual, or does the worker provide services through a business
   entity (LLC, corporation, partnership)?
5. Approximately when did the engagement begin? Has it continued since?
6. Is there a written agreement? (If yes, please provide it.)

**Section 2 — Behavioural Control** 7. Does the entity provide specific instructions on HOW the work should be performed
(not just WHAT the result should be)? 8. Does the entity require the worker to use specific tools, software, or methods? 9. Does the entity require the worker to work specific hours or on-site? 10. Who supervises the worker's work and how frequently? 11. Has the entity provided any training to the worker?

**Section 3 — Financial Control** 12. How is the worker compensated? (Hourly rate / fixed project fee / salary / other) 13. Does the entity reimburse the worker's business expenses (phone, equipment, travel)? 14. Who provides tools, equipment, and workspace? 15. Can the worker earn profit beyond what is earned from this engagement? 16. Does the worker perform services for other clients?

**Section 4 — Relationship Type** 17. Does the worker receive any benefits (health insurance, retirement, paid leave)? 18. Is the relationship exclusive (worker not permitted to work for others)? 19. Is the engagement open-ended or project/term-limited? 20. Does the worker have the right to send a substitute to perform the work? 21. Is the work the worker performs the same as or closely related to the entity's core
business activity?

**Section 5 — Tax and Documentation** 22. Has the entity been filing Form 1099-NEC (not W-2) for this worker? 23. Has the entity obtained Form W-9 from the worker? 24. Has the entity ever treated a worker in a substantially similar position as an employee? 25. Has the entity or the worker ever received an IRS determination or been audited on
this worker's classification?

---

## Provenance

Created by Legalcode, 2026-03-01. Original synthesis — no input skills merged.

Research foundation:

- ABC test framework: California Dynamex Operations West v. Superior Court (2018) 4
  Cal.5th 903; California AB5 (Lab. Code §2750.3); Massachusetts M.G.L. c. 149 §148B;
  New Jersey N.J.S.A. 43:21-19(i)(6) [VERIFY current text of each]
- Federal economic reality: DOL Final Rule January 2024 (29 C.F.R. Part 795, enforcement
  suspended May 2025); DOL Field Assistance Bulletin No. 2025-1; DOL Fact Sheet #13
  (2008) [VERIFY]
- IRS common law test: IRS Publication 15-A; IRS Topic No. 762; Revenue Ruling 87-41
  [VERIFY]
- Section 530 safe harbour: Revenue Act of 1978, §530; Revenue Procedure 2025-10
  [VERIFY]
- UK IR35: ITEPA 2003, Chapter 8 and 10; HMRC Off-Payroll Working guidance [VERIFY]
- EU Platform Work Directive: Directive (EU) 2024/2831 (effective December 1, 2024;
  implementation deadline December 2, 2026) [VERIFY member-state status]
- Australia: Personnel Contracting Pty Ltd [2022] HCA 1; ZG Operations v. Jamsek [2022]
  HCA 2; Fair Work Legislation Amendment (Closing Loopholes) Act 2023, §15AA (effective
  August 26, 2024) [VERIFY]
- NLRB: SuperShuttle DFW, Inc. (2019) [VERIFY current NLRB position]
