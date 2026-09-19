---
name: legalcode-employee-handbook-review
description: Review employee handbooks and policy manuals for legal compliance, policy gaps, and liability-creating
  language. Use when onboarding as HR counsel, conducting an annual compliance audit, after a merger or
  acquisition, when entering a new state, or after a significant statutory change. Covers US federal baseline
  (Title VII, ADA, ADEA, FMLA, NLRA, FLSA, OSHA, GINA, USERRA, PUMP Act, PWFA), multi-state analysis for
  distributed workforces, UK requirements (ERA 1996, Equality Act 2010, Employment Rights Act 2025), and
  Australian requirements (Fair Work Act 2009 NES, positive duty, right to disconnect). Classifies each
  policy area as COMPLIANT, UPDATE REQUIRED, NON-COMPLIANT, or CRITICAL RISK. Produces a prioritized remediation
  checklist with model policy language, a multi-state compliance matrix, and a Glass Box audit trail.
  Supports multi-state operations with jurisdiction-specific supplement analysis.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Employee Handbook Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of employee
> handbooks and HR policy manuals. It does not constitute legal advice. All outputs
> should be reviewed by a qualified employment attorney licensed in all relevant
> jurisdictions before the handbook is distributed to employees. Employment laws change
> frequently and vary dramatically by jurisdiction — provisions that were compliant in
> 2021 may be non-compliant in 2026. Statutory and regulatory references carry
> hallucination risk; verify against authoritative sources (DOL, EEOC, NLRB, applicable
> state agency) before relying on any citation in this analysis.

---

## Purpose and Scope

This skill reviews employee handbooks and HR policy manuals against federal, state, and
international employment law requirements. It identifies policy gaps, outdated provisions,
and legally risky language, and produces prioritized update recommendations with model
policy language.

**Covers:**

- At-will employment disclaimers and implied contract risk analysis
- EEO, anti-discrimination, and anti-harassment policies (all post-_Bostock_ protected classes)
- NLRA Section 7 compliance analysis under the 2023 _Stericycle_ standard
- FMLA, state leave law, and leave stacking exposure
- ADA, PWFA, and PUMP Act accommodation procedures
- FLSA wage and hour policies (overtime, off-the-clock work, timekeeping)
- OSHA workplace safety, injury reporting, and whistleblower protections
- Drug testing policies and state cannabis law conflicts
- Pay transparency requirements (multi-state matrix)
- Separation procedures, final pay, and COBRA references
- Social media, electronic communications, and employee monitoring policies
- Remote work and multi-state wage and hour compliance
- Background check policies and FCRA / ban-the-box compliance
- UK requirements: ERA 1996 written statement, Equality Act 2010, WTR 1998, PIDA 1998,
  Employment Rights Act 2025
- AU requirements: Fair Work Act 2009 NES, right to disconnect, positive duty, WHS
- AI acceptable use policies (emerging 2025–2026 requirement)
- Multi-state employer supplement analysis and jurisdiction prioritization

**Does not:**

- Draft entire employee handbooks from scratch (see drafting-specific skills)
- Provide legal advice or replace qualified employment counsel
- Apply to collective bargaining agreements (handbooks and CBAs interact but are distinct)
- Review benefits plans, ERISA documents, or payroll tax compliance
- Apply outside the US, UK, and AU without explicit jurisdictional configuration

**Related skills:** `legalcode-dsar-workflow-builder` (employee data subject rights),
`legalcode-us-breach-notification-triage` (breach involving employee data),
`legalcode-us-state-privacy-comparison` (state privacy law for employee monitoring),
`legalcode-incident-response-plan-builder` (workplace incident response).

---

## Jurisdiction and Governing Law

Employment law follows the employee's **physical work location**, not the employer's
headquarters state. A handbook choice-of-law clause does not override mandatory state
employment law protections.

**Jurisdiction-agnostic baseline:** Federal US law (Title VII, ADA, ADEA, FMLA, FLSA,
NLRA, OSHA, GINA, USERRA, PUMP Act, PWFA) sets the floor. Every state adds layers.

**[JURISDICTION-SPECIFIC]** — When locating this review, research and apply:

- State anti-discrimination law coverage thresholds (California FEHA: 5+ employees;
  New York SHRL: all employers; federal Title VII: 15+ employees)
- State leave laws and their interaction with FMLA (stacking risks)
- State wage and hour requirements for meal/rest breaks, overtime, and pay frequency
- Pay transparency requirements in job postings (13+ states as of 2025)
- Non-compete enforceability (banned in CA, MN, ND, OK; restricted in most others)
- Salary history ban provisions (13+ states and numerous localities)
- Cannabis/marijuana employment policies (off-duty use protections in 24+ states)
- Mandatory training requirements (CA: 2-hour supervisor training; NY: annual;
  IL: annual; AU: positive duty training)
- Employee monitoring and surveillance consent requirements (CA CIPA; MD; CT; DE)

**For UK handbooks:** Employment law derives from ERA 1996, Equality Act 2010,
Working Time Regulations 1998, PIDA 1998, and Employment Rights Act 2025.
ACAS Codes of Practice have quasi-statutory force (up to 25% ET award adjustment).

**For Australian handbooks:** The Fair Work Act 2009, National Employment Standards,
applicable modern awards, and harmonized WHS legislation govern. State systems apply
to non-national system employers (primarily some WA employers).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change the direction or scope of the analysis
- Jurisdiction determines whether a policy area is even legally required
- Workforce size determines which federal statutes apply
- Union status determines which NLRA analysis framework applies

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

### Step 1: Accept the Handbook

Accept the handbook in any of these formats:

- **File**: PDF, DOCX, or other document
- **URL**: Link to an HR system, document repository, or shared drive
- **Pasted text**: Handbook text pasted directly into the conversation
- **Section-by-section**: For large handbooks (50+ pages), accept and analyze in
  logical sections (e.g., Section 1: Employment relationship; Section 2: Compensation)

If no handbook is provided, prompt the user to supply one. If the handbook is very
long (>50 pages), ask whether to conduct a full review or a priority-first triage.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Skip any already answered:

1. **Jurisdiction(s) of operation**: In which states/countries does the organization
   have employees?
   - Options: Single US state (specify which), Multi-state (list states), National —
     all 50 US states, United Kingdom, Australia, Multiple countries
   - _Why this matters_: Every state applies its own employment law. A California
     handbook is materially different from a Texas handbook. A national handbook must
     satisfy the strictest applicable state requirement for each policy area.

2. **Workforce size**: Approximately how many employees does the organization have?
   - Options: 1–14 employees, 15–49 employees, 50–99 employees, 100–499 employees,
     500+ employees
   - _Why this matters_: Federal applicability thresholds — Title VII / ADA / GINA /
     PWFA / PUMP Act: 15+; ADEA: 20+; FMLA: 50+; WARN Act: 100+. State equivalents
     often have lower thresholds (CA FEHA: 5+; CA CFRA: 5+; NY SHRL: all employers).

3. **Industry**: What sector does the organization operate in?
   - Options: Healthcare (HIPAA-covered), Financial services (FINRA/SEC-regulated),
     Education (FERPA), Federal contractor/subcontractor (OFCCP/DFWA), Transportation
     (DOT), General commercial, Multiple regulated sectors
   - _Why this matters_: Healthcare employers have HIPAA workforce training obligations,
     OIG exclusion check requirements, and stricter background check duties. Federal
     contractors must have affirmative action plans and specific OFCCP EEO language.
     FINRA-regulated firms must address outside business activities and Form U4.

4. **Union or non-union workforce**: Is any portion of the workforce represented by
   a union?
   - Options: Fully non-union, Partially unionized (specify covered unit), Fully
     unionized, Organizing campaign underway, Unknown
   - _Why this matters_: For non-union workforces, NLRA Section 7 analysis under the
     2023 _Stericycle_ standard is the primary constraint. Policies permissible under
     the pre-2023 _Boeing_ standard may now be unlawful. For unionized workforces, the
     CBA governs many terms and the handbook must not conflict with negotiated terms.

5. **Last review date**: When was the handbook last formally reviewed or updated?
   - Options: Within the last 12 months, 1–2 years ago, 2–5 years ago, More than 5
     years ago, Never formally reviewed, Unknown
   - _Why this matters_: A handbook last reviewed before 2022 pre-dates: _Bostock_
     sexual orientation/gender identity extension (2020), Ending Forced Arbitration of
     Sexual Assault and Sexual Harassment Act (2022), PUMP Act (2022/effective 2023),
     PWFA (2023/effective 2023), NLRB _Stericycle_ standard (August 2023), numerous
     state leave law expansions (CA AB 1949 bereavement 2023), and DOL salary threshold
     increase (July 2024).

**Default assumptions** (state explicitly if user cannot answer): Single state (ask
which); 50–499 employees (FMLA applicable, WARN Act not); general commercial industry;
non-union; last reviewed more than 2 years ago. Apply these defaults and flag each
explicitly in the Glass Box audit trail.

### Step 3: Load Organization's HR Playbook

If the organization has a standard HR policy playbook, prior employment counsel's
guidance, or a precedent handbook, ask the user to provide it. Extract:

- Standard policy positions (at-will language, leave entitlements, accommodation
  processes, discipline procedures)
- Prior employment counsel's standing guidance or known red flags
- Industry association model policies (if applicable)

If no playbook exists, proceed with federal minimum standards plus the jurisdiction-specific
requirements identified in Step 2. Label the review: _"Based on federal minimum standards
and applicable state law — not organizational precedent."_

**⟁ CLARIFY** — If no playbook is found:

- **Option A**: Proceed with general federal and state compliance standards as baseline
- **Option B**: Supply key organizational positions now (I'll ask about each major policy
  area as we proceed)
- **Option C**: Focus the review solely on legal compliance (not organizational preferences)

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify all applicable jurisdictions from Step 2 and compile a working reference:

1. **Federal floor**: Title VII, ADA, ADEA, FMLA (29 C.F.R. Part 825), FLSA (29 C.F.R.
   Part 541), NLRA (29 U.S.C. § 151 et seq.), OSHA (29 U.S.C. § 651 et seq.),
   GINA, USERRA, PUMP Act (FLSA § 7(r)), PWFA (42 U.S.C. § 2000gg et seq.), FCRA
2. **State-specific requirements**: Leave laws, anti-discrimination thresholds, wage
   and hour rules, pay transparency, non-compete restrictions, cannabis policies
3. **Local ordinances** (where known): NYC Human Rights Law, Chicago Fair Workweek
   Ordinance, LA Wage Theft Prevention Act
4. **Industry-specific overlays**: HIPAA, GLBA, DOT, OFCCP, FINRA

**With legalcode-mcp connected**: Search for current statutory text and recent
regulatory guidance for each implicated jurisdiction. Save results to
`/tmp/legalcode-handbook-authority.md`. Mark all citations VERIFIED.

**Without legalcode-mcp**: Proceed with web-sourced research. Mark all statutory and
regulatory citations [VERIFY] and note in the Glass Box audit trail:
`legalcode_mcp: "Not connected"`. Flag the most rapidly-changing areas (NLRB standards,
DOL salary threshold, state cannabis laws) for priority attorney verification.

### Step 5: Policy-by-Policy Analysis

**⟁ CLARIFY** — For handbooks longer than 30 pages or covering more than 20 policy areas:

- **Full review**: Analyze all 16 policy categories below; produce complete
  remediation report (recommended for annual compliance audits and post-merger reviews)
- **Priority triage**: Focus on CRITICAL RISK categories first, then NON-COMPLIANT,
  then UPDATE REQUIRED; defer COMPLIANT documentation (recommended for initial scoping
  or rapid turnaround engagements)

Analyze each of the 16 policy categories in Section 7 (Deep Policy Analysis) below.
For each:

1. Is the policy present? If absent → classify immediately (most absences = NON-COMPLIANT
   or CRITICAL RISK)
2. Does present language comply with current applicable law at the applicable threshold?
3. Does it contain CRITICAL RISK indicators (implied contract, _Stericycle_ violation,
   discriminatory classification, waiver of non-waivable rights)?
4. Does it need updating for post-2020 statutory changes (see anti-patterns below)?
5. Is it adequate for all identified jurisdictions in Step 2?

### Step 6: Missing Policy Detection

After analyzing present policies, identify policy areas entirely absent from the handbook.
A missing required policy can be as significant as a deficient one — absence of a required
FMLA policy for a 50+ employee employer is a per se NON-COMPLIANT finding.

Apply the Self-Interrogation framework (Section 12) to all CRITICAL RISK classifications
before finalizing: could the policy be read as compliant under a reasonable alternative
interpretation? If yes, reconsider the classification.

### Step 7: Generate Remediation Language

For each UPDATE REQUIRED and NON-COMPLIANT finding, generate specific replacement or
supplemental policy language. For CRITICAL RISK items, generate corrected language plus a
plain-language explanation of the liability mechanism suitable for escalation to
employment counsel.

**Remediation item format:**

```
Policy Area: [name]
Classification: [CRITICAL RISK / NON-COMPLIANT / UPDATE REQUIRED]
Finding: [what the handbook currently says, or "Policy absent"]
Legal basis: [specific statute, regulation, or NLRB decision + citation]
Jurisdiction(s): [federal / state / local]
Recommended language: [specific draft policy text]
State-specific note: [if multi-state employer needs a different provision by state]
Priority: [Immediate — do not distribute / Before next distribution / Next revision cycle]
```

### Step 8: Quality Verification

Before delivering any output, run the Citation Quality Gates (Section 11), apply
Self-Interrogation to all CRITICAL RISK items (Section 12), and assign Confidence Scores
to all significant findings (Section 13). Verify the output format template (Section 18)
is complete before delivery.

---

## Severity Classification System

The four-tier classification system for handbook review.

| Tier           | Name                | Definition                                                                                                                                                                                                                                     | Required Action                                                                                                                                                                                      |
| -------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | **COMPLIANT**       | Policy is present, legally sufficient under all applicable law, and current. No changes recommended at this time.                                                                                                                              | Note for awareness. Re-review on next annual cycle or after relevant statutory change.                                                                                                               |
| **YELLOW**     | **UPDATE REQUIRED** | Policy is present but outdated, incomplete, or uses language that creates ambiguity. Not currently unlawful but creates risk or fails a best-practice standard.                                                                                | Generate specific recommended language. Note which jurisdiction or statute triggers the update. Schedule for next revision cycle.                                                                    |
| **RED**        | **NON-COMPLIANT**   | Policy is missing entirely, or present language directly conflicts with a current federal, state, or local statute or regulation.                                                                                                              | Identify the specific statutory violation. Provide compliant alternative language. Flag for remediation before next handbook distribution.                                                           |
| **⚠ CRITICAL** | **CRITICAL RISK**   | Policy creates independent legal liability regardless of whether any employee complains. Includes implied employment contract language, NLRA § 7 violations, discriminatory classification, or language waiving non-waivable statutory rights. | Explain the specific liability mechanism. Cite the statute, regulation, or NLRB precedent. Provide corrected language. Escalate to employment counsel immediately. Do not distribute until resolved. |

**Critical distinction from contract review**: In contract review, RED means "escalate
and negotiate." In handbook review, CRITICAL RISK means "do not distribute." The handbook
is a unilateral employer document; there is no counterparty to negotiate with. The
liability attaches the moment the policy is published to employees.

**Important note on NLRB standards**: The NLRB _Stericycle_ standard (August 2, 2023,
372 NLRB No. 113) replaced the prior _Boeing Co._ (2017) balancing test. Under
_Stericycle_, a facially neutral work rule is **presumptively unlawful** if an employee
"could reasonably interpret" the rule to restrict NLRA § 7 protected concerted activity,
evaluated from the perspective of an employee who is economically dependent on the
employer. Even if a non-coercive interpretation is also plausible, the rule is
presumptively unlawful unless the employer proves the rule advances a legitimate and
substantial business interest that cannot be achieved through a more narrowly tailored
rule. [VERIFY current NLRB enforcement posture — NLRB standards shift between
administrations.]

---

## Deep Policy Analysis: 16 Policy Categories

### Tier A — CRITICAL RISK Categories (Review First)

These policy areas most frequently contain language creating independent legal liability.

---

#### Category 1: At-Will Employment Disclaimer

**Federal and state basis**: Common law at-will doctrine; all US states except Montana
(Montana Wrongful Discharge from Employment Act, Mont. Code Ann. § 39-2-901 et seq.,
creates cause-of-action requirement after probation).

**Required handbook elements:**

- [ ] Clear statement that employment is at-will — either party may terminate at any
      time, with or without cause, with or without notice
- [ ] Explicit statement that nothing in the handbook creates or is intended to create
      a contract of employment for a specific period
- [ ] Statement that only a written employment agreement signed by a designated
      executive (name the title) can modify at-will status
- [ ] Disclaimer appears prominently at the beginning of the handbook AND in the
      acknowledgment signature form
- [ ] No language elsewhere in the handbook that undermines at-will status

**Implied contract risk indicators (flag as CRITICAL RISK):**

- [ ] Language stating employment is for a "specific period" (e.g., "annual employment")
- [ ] Language that termination is "only for cause" without an explicit at-will carve-out
- [ ] Progressive discipline described with mandatory, non-reservable steps ("will
      receive a verbal warning, then a written warning, then termination") — must include
      reservation clause: _"The Company reserves the right to skip, combine, or forego any
      step at its sole discretion"_
- [ ] "Job security" or "long-term career development" promises that contradict the
      disclaimer
- [ ] Any statement that employees are "guaranteed" employment, benefits, or processes

**Model at-will disclaimer language** (effective in most US states):

> _"Your employment with [Company Name] is at-will. This means that either you or the
> Company may end the employment relationship at any time, with or without cause and
> with or without notice, for any lawful reason. Nothing in this handbook, any other
> Company document, or any statement by any Company representative creates or is
> intended to create an express or implied contract of employment for any specific
> period of time. Only a written employment agreement signed by the [CEO/President]
> of the Company can modify the at-will nature of your employment."_

**[JURISDICTION-SPECIFIC]**: California, Massachusetts, New Jersey, Michigan, and
Illinois courts closely scrutinize handbook disclaimers; courts may find a disclaimer
ineffective if it is undermined by specific promises elsewhere in the handbook. Run
court-specific analysis for these states.

---

#### Category 2: Confidentiality and Non-Disparagement Policies

**Federal basis**: NLRA § 7 (29 U.S.C. § 157); _Stericycle, Inc._ (372 NLRB No. 113,
Aug. 2, 2023); _McLaren Macomb_ (372 NLRB No. 58, Feb. 21, 2023)

**NLRA § 7 protected concerted activity** includes: discussing wages, hours, and working
conditions with coworkers; discussing unsafe working conditions; cooperating with NLRB
investigations; engaging in union organizing activity. These rights apply to all private
employers, union and non-union alike.

**Required handbook elements:**

- [ ] Confidentiality policy expressly carves out: _"Nothing in this policy prohibits
      employees from discussing their wages, hours, or other terms and conditions of
      employment with coworkers or with any labor organization or government agency"_
- [ ] Non-disparagement clause (if present) is narrowly limited to genuinely
      unprotected speech (e.g., disclosing actual trade secrets or confidential client
      information); does not sweep in statements about working conditions
- [ ] Social media policy does not prohibit "negative," "derogatory," or "disparaging"
      posts generally; includes explicit § 7 carve-out
- [ ] Workplace investigation confidentiality is addressed case-by-case with documented
      business justification (blanket "all investigations must remain confidential"
      instruction is presumptively unlawful under NLRB precedent)

**CRITICAL RISK indicators:**

- [ ] Policy prohibiting employees from discussing "company business" with each other
- [ ] Policy prohibiting discussion of wages, salaries, or compensation
- [ ] Non-disparagement clause covering statements about co-workers or working
      conditions without a § 7 carve-out
- [ ] Social media policy prohibiting "negative posts" about the employer without
      limitation to genuinely unprotected speech
- [ ] "No gossip" policy that extends to working conditions
- [ ] Recording prohibition without a carve-out for protected concerted activity

**[JURISDICTION-SPECIFIC]**: California Labor Code § 232 independently prohibits
employer policies preventing employees from disclosing their wages to others. California
Labor Code § 1197.5 prohibits salary secrecy policies. Illinois Equal Pay Act (820 ILCS 112) and New York Equal Pay Act provide similar protections.

---

#### Category 3: EEO, Anti-Discrimination, and Anti-Harassment Policy

**Federal basis**: Title VII, Civil Rights Act 1964 (42 U.S.C. § 2000e et seq.);
ADA (42 U.S.C. § 12101 et seq.); ADEA (29 U.S.C. § 621 et seq.); GINA (42 U.S.C.
§ 2000ff et seq.); _Bostock v. Clayton County_ (590 U.S. 644, 2020)

**Post-_Bostock_ protected classes under Title VII (42+ employees):**
Race, color, religion, sex (including pregnancy, sexual orientation, and gender identity),
national origin.

**Required handbook elements:**

- [ ] Protected class list explicitly includes sexual orientation, gender identity,
      and gender expression post-_Bostock_ (2020)
- [ ] Pregnancy, childbirth, and related medical conditions listed as protected
      (Pregnancy Discrimination Act; PWFA 2023 — separate from disability accommodation)
- [ ] Multiple internal reporting channels described (supervisor, HR, hotline, legal,
      and/or an external ombudsperson)
- [ ] Explicit non-retaliation provision (retaliation is independently unlawful under
      Title VII § 704; ADA § 12203; ADEA § 623(d))
- [ ] Investigation commitment with timeline (not necessarily a specific number of days,
      but a clear commitment to investigate)
- [ ] Appropriate confidentiality provision (balanced against § 7 rights — see Category 2)
- [ ] EEOC charge filing rights preserved (policy must not suggest internal complaint
      procedure is the exclusive remedy)

**CRITICAL RISK indicators:**

- [ ] Protected class list omits sexual orientation and gender identity (pre-_Bostock_)
- [ ] Policy suggests internal complaint procedure must be exhausted before filing with
      EEOC (EEOC filing right is non-waivable)
- [ ] Retaliation provision absent or limited to "formal complaints" only (anti-retaliation
      extends to informal complaints, participation in investigations, and requests for
      accommodation)

**[JURISDICTION-SPECIFIC]**: California FEHA (5+ employees) adds: marital status,
sexual orientation, gender expression, military/veteran status, and reproductive health
decision-making. New York SHRL (all employers): domestic violence victim status,
familial status. Illinois IHRA: family responsibilities, source of income, status as
victim of domestic violence. NYCHRL (4+ employees in NYC): caregiver status.

**[JURISDICTION-SPECIFIC - UK]**: Equality Act 2010, 9 protected characteristics.
Employer vicariously liable unless it can show it took "all reasonable steps" to prevent.

**[JURISDICTION-SPECIFIC - AU]**: Sex Discrimination Act 1984 (Cth), as amended by
Respect at Work Act 2022: positive duty to take reasonable and proportionate measures
to eliminate sexual harassment. AHRC 7 compliance standards apply.

---

#### Category 4: Arbitration and Dispute Resolution

**Federal basis**: Federal Arbitration Act (9 U.S.C. § 1 et seq.); _Epic Systems Corp.
v. Lewis_ (584 U.S. 497, 2018); Ending Forced Arbitration of Sexual Assault and Sexual
Harassment Act of 2022 (Pub. L. 117-90)

**Required handbook elements:**

- [ ] Arbitration clause (if used) covers only claims where mandatory pre-dispute
      arbitration is lawful — does NOT cover sexual harassment or sexual assault claims
      (Ending Forced Arbitration Act, effective March 3, 2022: mandatory arbitration of
      these claims is void and unenforceable regardless of state)
- [ ] EEOC and NLRB charge filing rights expressly preserved
- [ ] Arbitration agreement is in a separately signed instrument (not embedded only
      in a handbook acknowledgment, which creates enforceability risks)
- [ ] Mutual arbitration obligation (applies to both employer and employee)

**CRITICAL RISK indicators:**

- [ ] Mandatory arbitration clause sweeps in sexual harassment or sexual assault
      claims (void under 2022 federal law)
- [ ] Clause waives right to file charges with EEOC or NLRB (impermissible — these
      are non-waivable statutory rights)
- [ ] Handbook-embedded arbitration clause is the only signed agreement (may be
      unenforceable for illusoriness where employer can amend handbook at will)

**[JURISDICTION-SPECIFIC]**: California — PAGA representative actions have survived
waiver challenges (Viking River Cruises v. Moriana, 596 U.S. 639, 2022, partially;
Adolph v. Uber Technologies, 14 Cal.5th 1104, 2023). California AB 51 (Cal. Gov.
Code § 12953) restrictions on mandatory arbitration of FEHA claims enjoined as of 2025
[VERIFY current status of AB 51 litigation]. New York Labor Law § 203-q prohibits
mandatory arbitration of sexual harassment claims (pre-empted by FAA for certain
agreements — verify current status).

---

### Tier B — NON-COMPLIANT Risk Categories

---

#### Category 5: FMLA Policy

**Federal basis**: Family and Medical Leave Act of 1993 (29 U.S.C. § 2601 et seq.);
29 C.F.R. Part 825; DOL updated FMLA poster (April 2023)

**Applicability**: Employers with 50+ employees within 75 miles; employees with 12+
months service and 1,250+ hours in prior 12 months.

**Required handbook elements (50+ employee employers):**

- [ ] 12-week annual entitlement for covered family/medical reasons
- [ ] 26-week military caregiver leave entitlement
- [ ] All covered reasons: serious health condition (employee or qualifying family
      member); birth, adoption, or foster placement; qualifying military exigency
- [ ] Employer designation rights and obligations (employer designates leave as FMLA
      when it has sufficient information, even if employee does not invoke FMLA by name)
- [ ] Intermittent leave and reduced schedule leave described
- [ ] Substitution of accrued paid leave during FMLA
- [ ] Key Employee exception (if applicable)
- [ ] Reference to FMLA required notices (general notice, eligibility notice,
      rights and responsibilities notice, designation notice — 29 C.F.R. § 825.300)

**[JURISDICTION-SPECIFIC]**: California CFRA (5+ employees) covers broader family members;
runs concurrently with FMLA but expands qualifying reasons. CA PDL (5+ employees): up to
4 months for pregnancy disability — separable from CFRA baby-bonding, potentially 7 months
combined protected leave. Colorado FAMLI (10+ employees). Washington PFML. New York NYPFL.
Massachusetts PFML. New Jersey FLA/TDI. Oregon OFLA + Paid Leave Oregon (note: stacking
rules changed July 1, 2024 — OFLA and Paid Leave Oregon no longer run concurrently in
all circumstances).

---

#### Category 6: ADA Reasonable Accommodation Procedure

**Federal basis**: Americans with Disabilities Act, 42 U.S.C. § 12101 et seq.;
EEOC Enforcement Guidance on Reasonable Accommodation (2002); 29 C.F.R. Part 1630

**Applicability**: 15+ employees.

**Required handbook elements:**

- [ ] Description of how to initiate an accommodation request (designated contact,
      written or verbal — do not require only written requests)
- [ ] Description of the interactive process: employer will engage in an interactive,
      good-faith dialogue to identify effective accommodations
- [ ] Confidentiality of medical information (ADA requires medical records in separate,
      locked files from personnel records — 29 C.F.R. § 1630.14(c))
- [ ] Statement that accommodation will be provided absent undue hardship
- [ ] Non-retaliation for requesting accommodation

**CRITICAL RISK indicators:**

- [ ] Policy suggests accommodation is at employer's discretion (ADA creates a legal
      obligation, not a discretionary benefit)
- [ ] Policy fails to describe the interactive process (employer liability for failure
      to engage in the interactive process is independent of whether a reasonable
      accommodation exists)
- [ ] Policy requires accommodation requests in writing only (may exclude employees
      whose disability affects written communication)

---

#### Category 7: PWFA Pregnancy Accommodation Procedure

**Federal basis**: Pregnant Workers Fairness Act (42 U.S.C. § 2000gg et seq.);
EEOC Final Rule (89 Fed. Reg. 29096, effective June 18, 2024)

**Applicability**: 15+ employees; effective June 27, 2023.

**Required handbook elements:**

- [ ] PWFA described separately from ADA (covers "known limitations" from pregnancy,
      childbirth, and related medical conditions — broader than ADA's "disability" standard)
- [ ] Interactive process for pregnancy accommodations described
- [ ] Temporary suspension of essential functions described as potential accommodation
- [ ] Non-retaliation for PWFA accommodation requests

**Note**: The PWFA covers conditions that do not qualify as ADA disabilities. Treating
the ADA as the sole vehicle for pregnancy accommodation is legally insufficient
post-June 2023. A handbook that references only ADA accommodations for pregnancy-related
conditions is NON-COMPLIANT.

---

#### Category 8: Lactation / Nursing Accommodation Policy

**Federal basis**: PUMP for Nursing Mothers Act of 2022 (Pub. L. 117-328, Div. KK;
amending FLSA § 7(r)); effective April 28, 2023

**Applicability**: All employers (small employers <50 employees may claim undue hardship
exemption, but must still provide if not causing undue hardship).

**Required handbook elements:**

- [ ] Reasonable break time to express breast milk for up to one year post-birth
- [ ] Private, non-bathroom space that is shielded from view and free from intrusion
- [ ] Coverage extends to ALL employees (PUMP Act expanded prior § 7(r) to cover
      exempt/salaried employees, not just non-exempt)
- [ ] Break time is unpaid if employee is fully relieved of duty; compensable if
      not completely relieved

**CRITICAL RISK indicators:**

- [ ] Handbook references old FLSA § 7(r) language without PUMP Act updates
- [ ] Policy limits accommodation to non-exempt employees only (pre-PUMP Act
      limitation — no longer lawful)
- [ ] Policy does not specify a private, non-bathroom space

---

#### Category 9: State-Specific Leave Policies

**[JURISDICTION-SPECIFIC]** — Review each applicable state. Key requirements:

**California (5+ employees):**

- [ ] CFRA (12 weeks family/medical; covered family members broader than FMLA)
- [ ] PDL (4 months pregnancy disability leave — separate from CFRA)
- [ ] California Paid Family Leave (PFL) reference (up to 8 weeks paid via EDD)
- [ ] AB 1949 Bereavement Leave (5 days; effective January 1, 2023; 5+ employees)
- [ ] California Kin Care (up to half accrued sick leave for family care)
- [ ] Mandatory sick leave (HWHFA; 1 hour per 30 hours worked, minimum 5 days usable)

**New York:**

- [ ] NYPFL (up to 12 weeks paid; applies to most NY employers)
- [ ] NY Earned Safe and Sick Time Act

**Colorado:**

- [ ] FAMLI (up to 12 weeks; 10+ employees contribute; 10+ employees provide leave)
- [ ] HFWA (Healthy Families and Workplaces Act paid sick leave)

**Washington:**

- [ ] PFML (up to 12 weeks medical + 12 weeks family; 18 weeks maximum combined)
- [ ] Washington Cares Fund (long-term care insurance; employee payroll deduction)
- [ ] Paid Sick Leave (1 hour per 40 hours worked)

**Oregon:**

- [ ] Paid Leave Oregon + OFLA (note stacking changes effective July 1, 2024)
- [ ] Oregon Paid Sick Leave (1 hour per 30 hours worked)

**Illinois:**

- [ ] ESST (Illinois Paid Leave for All Workers Act; 1 hour per 40 hours worked;
      effective January 1, 2024; up to 40 hours per year)

**Massachusetts / New Jersey**: Equivalent PFML programs with mandatory employee notice.

**Bereavement leave mandates (as of 2026)**: Six states mandate bereavement leave —
California (AB 1949: 5 days, 5+ employees), Illinois (12 weeks for large employers;
6 weeks for 50–249; effective January 1, 2023 [VERIFY]), Maryland, Oregon (OFLA:
2 weeks per qualifying family member), Vermont, Washington. [VERIFY current status.]

---

#### Category 10: Wage and Hour Policy

**Federal basis**: FLSA (29 U.S.C. § 201 et seq.); 29 C.F.R. Part 541 (exemption
regulations); DOL Final Rule (effective July 1, 2024, raising salary threshold to
$684/week for standard exemption and $107,432 for HCE — [CHECK CURRENCY — threshold
subject to litigation and potential revision])

**Required handbook elements:**

- [ ] Exempt vs. non-exempt classification explanation and designation basis
- [ ] Overtime rate and calculation method for non-exempt employees (1.5x regular
      rate of pay for all hours over 40 per workweek under FLSA)
- [ ] Timekeeping obligations: all non-exempt employees must record all time worked;
      unauthorized overtime is prohibited AND must be compensated if employer knows
      or should know work is being performed (off-the-clock work policy must state both)
- [ ] Meal and rest break policy by applicable state (no federal requirement; state law
      governs):
  - California: 30-minute unpaid meal period after 5 hours (IWC Wage Orders);
    10-minute paid rest break per 4 hours (or major fraction); premium pay of 1 hour
    for each missed break (Cal. Labor Code § 226.7)
  - Colorado, Oregon, Washington, New York: state-specific break requirements apply
  - Federal: short breaks (<20 min) are compensable; meal periods (30+ min,
    completely duty-free) are not

**[JURISDICTION-SPECIFIC]**: California has daily overtime (1.5x after 8 hours/day;
2x after 12 hours; 1.5x on 7th consecutive workday). Multi-state employers must
address applicable state rules in supplements.

---

### Tier C — UPDATE REQUIRED Categories

---

#### Category 11: Anti-Harassment Policy

**Federal basis**: Title VII (42 U.S.C. § 2000e-2); EEOC Enforcement Guidance on
Harassment in the Workplace (2024 — supersedes 1999 guidance)

**Required handbook elements:**

- [ ] Harassment definition updated for all post-_Bostock_ protected classes
- [ ] Specific investigation process described (not merely "we will investigate") —
      EEOC 2024 Guidance requires reasonable investigation
- [ ] Named or described reporting channels (supervisor, HR, hotline, ethics line,
      external option — minimum two channels, at least one that bypasses direct supervisor)
- [ ] Non-retaliation protection for reporters and witnesses
- [ ] Bystander intervention encouraged
- [ ] Third-party harassment covered (customers, clients, vendors)

---

#### Category 12: Social Media and Electronic Communications Policy

**Federal basis**: NLRA § 7 (_Stericycle_ standard); Stored Communications Act (18
U.S.C. § 2701 et seq.); state monitoring consent laws

**Required handbook elements:**

- [ ] Explicit NLRA § 7 carve-out: _"Nothing in this policy prohibits employees from
      discussing wages, hours, or working conditions with each other or with a union
      representative or labor organization"_
- [ ] Policy does not ban all "negative," "disparaging," or "offensive" online posts;
      limitations must be tied to specific, articulable business interests (trade secret
      protection, anti-harassment)
- [ ] Monitoring of company-owned devices and networks: disclosed, with clear scope
- [ ] Personal device monitoring disclosure (where applicable)
- [ ] AI acceptable use policy: what AI tools employees may use; prohibitions on
      inputting confidential information, client data, or trade secrets into AI systems;
      disclosure obligations for AI-generated work product [Emerging 2025–2026 requirement]

**[JURISDICTION-SPECIFIC]**: California (CIPA), Maryland (Md. Cts. & Jud. Proc. §
10-402), Connecticut (CGS § 52-570d), and Delaware require all-party consent for
interception of communications. Monitoring disclosure must be explicit and acknowledged.

---

#### Category 13: Remote Work / Hybrid Work Policy

**Federal basis**: FLSA (compensable time; off-the-clock risk); OSH Act § 5(a)(1)
(general duty clause); state wage and hour laws follow employee's work location

**Required handbook elements:**

- [ ] Applicable state law (wage and hour) follows employee's physical work location;
      policy addresses how this applies to remote workers
- [ ] Expense reimbursement for remote work: required in California (Labor Code §
      2802), Illinois (820 ILCS 115/9.5), Montana, North Dakota, Iowa, Washington;
      policy must address home office, internet, and phone reimbursement obligations
- [ ] Timekeeping requirements for remote workers
- [ ] Data security and use of personal devices for work
- [ ] Home office safety expectations (ergonomics; injury reporting procedure applies
      to home offices)
- [ ] Right to disconnect provisions (required in AU; recommended in UK post-ERA 2025)

**[JURISDICTION-SPECIFIC]**: For multi-state employers, remote work policies must
identify which jurisdiction's pay, leave, and expense rules apply. This is not
overridable by contract — the employee's work state controls.

---

#### Category 14: Drug and Alcohol Policy

**Federal basis**: Drug-Free Workplace Act of 1988 (41 U.S.C. §§ 8101–8106, federal
contractors only); DOT drug testing regulations (49 C.F.R. Part 40, transportation
employees only); OSHA § 11(c) (post-injury drug testing)

**Required handbook elements:**

- [ ] Cannabis/marijuana policy updated for applicable state laws:
  - States restricting adverse action based on off-duty use or non-psychoactive
    metabolite tests (as of 2026 — [VERIFY current state list]): California (AB 2188,
    eff. January 1, 2024), New Jersey, New York (SB S6578-A), Minnesota, Montana,
    Rhode Island, Connecticut, Delaware, Illinois, Colorado
  - States where recreational cannabis is legal but employment protection is more
    limited: check state-specific provisions
- [ ] Federal contractor language (if applicable): federal contract obligations
      require drug-free workplace policy even in cannabis-legalization states
- [ ] Post-injury drug testing policy complies with OSHA § 11(c): blanket post-injury
      testing that deters injury reporting is unlawful (29 C.F.R. § 1904.35)
- [ ] DOT drug testing policy (transportation employees)

---

#### Category 15: Background Check Policy

**Federal basis**: Fair Credit Reporting Act (15 U.S.C. § 1681 et seq.); EEOC
Enforcement Guidance on Criminal Background Checks (April 25, 2012)

**Required handbook elements:**

- [ ] FCRA-compliant disclosure (separate document) and authorization referenced
- [ ] Individualized assessment process for criminal history (per EEOC guidance;
      blanket criminal history bans can constitute disparate impact race discrimination)
- [ ] "Ban the box" compliance (jurisdictions prohibiting criminal history inquiry
      on applications include California [FEHA], Illinois [Human Rights Act], New York
      City [Fair Chance Act], New Jersey, Philadelphia, Chicago, Los Angeles — [VERIFY])
- [ ] Adverse action procedures referenced (pre-adverse action notice + copy of report)

---

#### Category 16: Workplace Safety and OSHA

**Federal basis**: OSH Act 1970 (29 U.S.C. § 651 et seq.); 29 C.F.R. Part 1904
(recordkeeping); § 11(c) (whistleblower anti-retaliation)

**Required handbook elements:**

- [ ] OSHA general duty clause obligation acknowledged
- [ ] Injury and illness reporting procedure (must be accessible; cannot be structured
      in a way that deters reporting — 29 C.F.R. § 1904.35(b)(1)(i))
- [ ] Non-retaliation for reporting safety concerns (§ 11(c))
- [ ] Emergency procedures and evacuation plan reference
- [ ] Hazard communication reference (where applicable — chemicals/labs/manufacturing)
- [ ] Return-to-work procedure

**[JURISDICTION-SPECIFIC]**: 25 states and territories have OSHA-approved state plans
with independent (sometimes more stringent) requirements: California (Cal/OSHA),
Washington (WISHA), Michigan (MIOSHA), Oregon (OR-OSHA), and others. State plan
requirements must be separately analyzed.

**[JURISDICTION-SPECIFIC - UK]**: Health and Safety at Work etc. Act 1974 (HSWA);
Management of Health and Safety at Work Regulations 1999; policy statement required for
5+ employees.

**[JURISDICTION-SPECIFIC - AU]**: Work Health and Safety Act 2011 (Cth) (harmonized
in most states); primary duty of care on PCBU; workers' compensation state schemes.

---

## Prioritization Framework

Organize all findings into three remediation tiers:

| Priority                              | Trigger                                                                                                              | Action                                                                                                                       |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — Immediate**                | CRITICAL RISK items; NON-COMPLIANT items with imminent enforcement risk; policies that have already created exposure | Escalate to employment counsel; do not distribute handbook until resolved                                                    |
| **Tier 2 — Before Next Distribution** | NON-COMPLIANT items discovered; missing required policies; UPDATE REQUIRED items where the change is material        | Include in next handbook revision; notify employees of interim policy via separate communication if distribution is imminent |
| **Tier 3 — Annual Review Cycle**      | UPDATE REQUIRED items that are not immediately material; best-practice improvements; minor language updates          | Include in next annual handbook revision; note review trigger for future cycles                                              |

**Annual review cadence**: Best practice (Seyfarth, Littler, Fisher Phillips) is an
October-December annual review to capture January 1 state law changes. **Trigger-based
supplemental reviews** should occur upon: new state expansion, significant NLRB/EEOC/DOL
guidance change, major new legislation, or merger/acquisition.

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivering if
any gate fails.

| Gate           | Rule                                                                                                                                                                                   | Fail Action                                                         |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Source**     | Every compliance finding cites a specific statute, regulation, EEOC guidance document, NLRB decision, or established common law principle                                              | Add citation or mark "[UNVERIFIED — employment counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., "29 U.S.C. § 2601" for FMLA; "Cal. Gov. Code § 12950.1" for CA FEHA training)                       | Fix format                                                          |
| **Currency**   | Every cited provision checked for post-2020 amendments; NLRB standards flagged for administration-specific variability                                                                 | Flag "[CHECK CURRENCY — may have been amended]"                     |
| **Domain**     | No California law applied to Texas analysis; no federal law stated as requiring what is only required in certain states; state-specific requirements clearly labeled                   | Remove or flag jurisdictional bleed                                 |
| **Confidence** | Uncertainty explicitly stated; no false precision on NLRB standards (which shift between administrations), DOL salary thresholds (subject to litigation), or pending state legislation | Add confidence qualifier                                            |

---

## Self-Interrogation for CRITICAL RISK Items

For any item classified CRITICAL RISK, apply this 3-pass review before finalizing:

**Pass 1 — Legal Chain Integrity**: Does the liability follow from the cited statute,
regulation, or NLRB decision? Would an NLRB ALJ, a federal court, or a state agency
actually reach this conclusion on these facts? Is the policy language actually present
in the handbook, or am I inferring it?

**Pass 2 — Completeness**: Have all relevant federal, state, and local requirements
been checked? Have EEOC enforcement guidance, NLRB General Counsel memoranda, relevant
circuit-specific case law, and state agency guidance been considered? Could there be a
carve-out or exception in the handbook I may have missed?

**Pass 3 — Challenge**: What is the strongest argument that this policy IS compliant?
Does the policy have an explicit NLRA § 7 carve-out that saves it? Does an at-will
disclaimer elsewhere in the handbook cure the implied contract risk? Under what
circumstances would a reasonable employment lawyer accept this language? If the
challenge reveals the classification was overstated, revise to YELLOW (UPDATE REQUIRED).

Mark Self-Interrogation outcome in the Glass Box: "PASS" (classification confirmed) or
"REVISED" (classification changed with explanation).

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                                                       | Action                                                                     |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled federal or state statutory requirement; no circuit split or litigation ambiguity                                      | State with confidence                                                      |
| **High**     | 0.80–0.94 | Strong authority; minor ambiguity in application to these specific facts                                                      | State with brief caveat                                                    |
| **Probable** | 0.60–0.79 | EEOC guidance, NLRB decisions (subject to administrative revision), or state agency interpretation; circuit split possible    | State with reasoning and contra-indicators; flag for attorney verification |
| **Possible** | 0.40–0.59 | Genuinely uncertain; emerging law; pending litigation affecting the rule (e.g., DOL salary threshold post-Texas court ruling) | Flag for professional review with both sides of the analysis               |
| **Unlikely** | 0.0–0.39  | Weak legal basis; speculative; extrapolated from analogous but not directly applicable law                                    | Do not assert as a compliance finding; flag "[UNCERTAIN]"                  |

**Note on NLRB standards**: All _Stericycle_ (2023) applications occupy the "Probable"
tier at best — NLRB enforcement posture and interpretive standards shift between
administrations. Confirm current NLRB enforcement stance before finalizing any
_Stericycle_-based CRITICAL RISK classification.

---

## Anti-Patterns

What NOT to do when reviewing employee handbooks:

1. **Treating a California-compliant handbook as nationally compliant.** California has
   the most expansive employment law protections. A handbook written for California
   may over-comply in most states but can still be non-compliant in New York (NYCHRL
   additional protected classes), Colorado (FAMLI), Washington (PFML and salary
   transparency), or Illinois (BIPA, CROWN Act, ESST) on specific issues.

2. **Applying the pre-_Stericycle_ NLRB standard.** Prior to August 2, 2023, overbroad
   confidentiality policies were evaluated under the _Boeing Co._ balancing test.
   Post-_Stericycle_, facially neutral policies are presumptively unlawful if
   employees could reasonably construe them as restricting § 7 activity. Always apply
   the current standard — but flag that NLRB enforcement posture can change between
   administrations [VERIFY current stance].

3. **Treating Title VII as not covering sexual orientation or gender identity.**
   _Bostock v. Clayton County_ (2020) definitively extended Title VII to cover
   discrimination based on sexual orientation and gender identity. Any handbook with a
   pre-_Bostock_ EEO policy is out of date.

4. **Confusing ADA with PWFA for pregnancy accommodations.** The PWFA (eff. June 27, 2023) creates a separate accommodation obligation for known limitations related to
   pregnancy, childbirth, and related medical conditions. It covers conditions that
   do not qualify as ADA disabilities. Treating the ADA as the sole vehicle for
   pregnancy accommodation is legally insufficient after June 2023.

5. **Flagging FMLA absence as non-compliant for sub-50-employee employers.** FMLA
   applies at 50+ employees. However, many states have equivalents with lower thresholds
   (CA CFRA at 5+; NY NYPFL for most employers; CO FAMLI at 10+). Apply the correct
   threshold for each jurisdiction identified in Step 2.

6. **Ignoring the Ending Forced Arbitration of Sexual Assault and Sexual Harassment
   Act (2022).** Federal law as of March 3, 2022 voids mandatory pre-dispute arbitration
   agreements covering sexual harassment or sexual assault claims. A handbook arbitration
   clause sweeping in those claims is unenforceable and a CRITICAL RISK.

7. **Accepting progressive discipline language without checking for implied contract
   risk.** "Employees will receive a verbal warning, then a written warning, then a
   final written warning before termination" without a reservation of rights clause
   limits at-will employment in many states. Flag any such language unless accompanied
   by an explicit reservation clause.

8. **Treating absence of a social media policy as harmless.** In the post-_Stericycle_
   environment, absence of a social media policy with a § 7 carve-out is preferable
   to a deficient one. However, absence leaves the employer without a lawful basis for
   disciplining genuinely harmful online conduct. Recommend adding a compliant policy
   rather than treating absence as COMPLIANT.

9. **Applying the current FLSA overtime salary threshold without noting its litigation
   vulnerability.** The DOL raised the FLSA salary threshold in July 2024. This rule
   has faced and continues to face legal challenges. Always mark threshold figures
   [CHECK CURRENCY] and recommend verification by counsel before updating handbook
   language.

10. **Assuming a boilerplate disclaimer is sufficient in all states.** Montana eliminated
    at-will employment for most employees after the probationary period (Montana WDEA).
    New Jersey, California, and Illinois courts apply strict scrutiny to disclaimers that
    are undermined by other handbook language. A disclaimer buried in a 60-page handbook
    that elsewhere promises job security may not be effective.

11. **Reviewing only present policies and ignoring handbook structure.** The order and
    prominence of policies matters. An at-will disclaimer in Appendix C after a
    25-page section promising "career development opportunities" may not be effective.
    The handbook's structure, headings, and tone are part of the implied contract analysis.

12. **Applying uniform drug testing rules to all states.** California (AB 2188, eff.
    January 1, 2024), New Jersey, New York, Minnesota, Montana, Rhode Island, Connecticut,
    Delaware, Illinois, and other states restrict adverse employment action based on
    off-duty cannabis use or non-psychoactive metabolite tests. Do not apply a blanket
    national drug testing policy without per-state analysis.

13. **Treating the handbook's EEO policy as a complete anti-harassment compliance
    program.** The EEOC's 2024 Enforcement Guidance on Harassment requires employers
    to take reasonable steps to prevent and correct harassment. A policy statement alone
    is not sufficient. Note whether the handbook describes an adequate reporting
    mechanism, investigation process, and non-retaliation commitment.

14. **Applying a blanket rule on non-compete enforceability.** Non-compete enforceability
    varies significantly: California, Minnesota, North Dakota, and Oklahoma generally void
    non-competes. Other states enforce them with reasonableness limitations. [CHECK
    CURRENCY — state non-compete laws are actively changing; FTC non-compete rule was
    vacated by federal courts in 2024.] Do not apply a blanket rule without per-state
    analysis.

15. **Overlooking pay transparency requirements when reviewing compensation policies.**
    As of 2025–2026, 13+ states require disclosure of pay ranges in job postings or
    upon employee request (CA, CO, CT, HI, IL, MD, MA, NV, NY, RI, WA, and others —
    [VERIFY current list]). If the handbook contains a compensation policy, check it
    against applicable requirements.

16. **Treating the PUMP Act as merely extending FLSA § 7(r).** The PUMP Act (eff. April 2023) materially expanded prior lactation protections by covering all employees (not
    just non-exempt), clarifying the private space requirement, and creating an explicit
    cause of action. A handbook referencing old FLSA § 7(r) language without PUMP Act
    updates is NON-COMPLIANT.

17. **Ignoring the interaction between remote work policies and multi-state wage and hour
    compliance.** An employee working remotely in California is entitled to California
    wage and hour protections regardless of where the employer is headquartered. Handbooks
    applying a single state's wage and hour rules to a distributed remote workforce are
    frequently non-compliant.

18. **Citing EEOC guidance or NLRB General Counsel memoranda as binding law.** EEOC
    guidance and NLRB GC memoranda are persuasive but not binding. Distinguish between
    statutory requirements (binding), regulatory requirements (binding), and agency
    guidance (persuasive). Mark the distinction clearly. NLRB GC memoranda in particular
    shift between administrations.

19. **Assuming a handbook compliant in 2021 remains compliant in 2026.** Since 2020:
    _Bostock_ (2020), ARPA leave changes (2021), Ending Forced Arbitration Act (2022),
    PUMP Act (2022/2023), PWFA (2023), _Stericycle_ (2023), CA AB 1949 bereavement (2023),
    DOL salary threshold (2024), CA AB 2188 cannabis (2024), IL ESST (2024), multiple
    state pay transparency laws (2024–2025), and AU right to disconnect (2024) all
    represent material developments. Any handbook not reviewed since 2022 very likely
    contains multiple NON-COMPLIANT items.

20. **Generating remediation language without jurisdiction-specific tailoring.** A
    one-size-fits-all policy fix may resolve the federal compliance gap while creating
    a new state compliance problem. When generating recommended replacement language,
    always note which jurisdiction(s) the language is drafted for and flag where
    state-specific variants are required.

21. **Omitting an AI acceptable use policy.** As AI tools proliferate in the workplace,
    handbooks without AI acceptable use policies create exposure: trade secret disclosure
    through AI prompts; discriminatory AI-assisted hiring/promotion decisions (EEOC
    Technical Assistance Document on AI, 2023); NLRA issues if AI monitors protected
    concerted activity. A 2025–2026 handbook update without an AI policy is a
    material omission.

22. **Failing to flag the _McLaren Macomb_ impact on separation agreements.** NLRB
    _McLaren Macomb_ (372 NLRB No. 58, 2023) held that broad non-disparagement clauses
    in severance/separation agreements are unlawful if they could restrict former employees'
    rights to discuss wages or working conditions during employment. Separation agreement
    templates referenced in the handbook should be reviewed against _McLaren Macomb_.
    [VERIFY current NLRB enforcement posture.]

---

## Writing Standards

Apply these standards to all output before delivery:

1. **Remediation language is written for the HR professional, not the lawyer.** Plain
   language; active voice; short sentences. The goal is text the HR team can adopt and
   employees can understand — not legalese.

2. **Analysis is written for the employment attorney who will review it.** Precise
   citations; confidence qualifiers; explicit assumptions.

3. **Distinguish "required by law" from "best practice."** Not every recommendation is
   a legal mandate. Label the basis clearly: _"Required: [statute]"_ vs. _"Recommended
   (best practice): [professional standard or risk management rationale]"_.

4. **Quantify risk where possible.** PAGA penalties in California are per violation
   per pay period. NLRA violations can result in reinstatement and back pay. ADA
   violations carry compensatory and punitive damages up to applicable caps. Explain
   the liability mechanism in concrete terms.

5. **No false precision on evolving standards.** NLRB standards, DOL salary thresholds,
   and cannabis employment law are all rapidly changing. Use confidence qualifiers
   explicitly; do not present probable standards as definite.

6. **Recommend counsel review for all CRITICAL RISK items.** The remediation language
   provided is a starting point; the CRITICAL RISK classification means the employer
   should not adopt new language without attorney review.

7. **Preserve the employer's tone and voice in remediation language.** Match the
   formality level of the existing handbook when drafting recommended replacement language.

8. **Run the Quality Gates before delivery.** If any gate fails, revise. No unverified
   legal claims in the final output.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current statutory text and agency guidance for each applicable
  jurisdiction and policy area
- Save results to `/tmp/legalcode-handbook-authority.md`
- Mark all legalcode-mcp-sourced citations VERIFIED in the Glass Box
- Pay particular attention to: NLRB current GC memoranda on _Stericycle_ application;
  DOL current salary threshold post-litigation; state-specific leave law amendments;
  state cannabis employment protection statutes; state pay transparency law status

**Without legalcode-mcp:**

- Conduct web research for the most material and jurisdiction-specific issues
- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Concentrate quality assurance efforts on ensuring no outdated law is stated as current

**Graceful degradation**: If legalcode-mcp search returns no results for a specific
jurisdiction, state explicitly: "No search results returned for [jurisdiction] — analysis
based on general principles; [VERIFY] against current state statute."

---

## Output Format Template

````markdown
## Employee Handbook Review Report

**Document**: [handbook name, version, and date if identifiable]
**Organization**: [if provided]
**States / Countries Covered**: [jurisdictions from Step 2]
**Workforce Size**: [bracket from Step 2]
**Industry**: [from Step 2]
**Union Status**: [from Step 2]
**Last Reviewed**: [from Step 2]
**Review Basis**: [Organizational playbook / Federal minimum standards + state law]
**Date of This Review**: [today's date]

---

## Executive Summary

**Overall compliance status**: [COMPLIANT / NEEDS ATTENTION / SIGNIFICANT GAPS /
CRITICAL ISSUES PRESENT]

| Category                                       | Count |
| ---------------------------------------------- | ----- |
| CRITICAL RISK items (immediate action)         | [N]   |
| NON-COMPLIANT items (before next distribution) | [N]   |
| UPDATE REQUIRED items (next revision cycle)    | [N]   |
| COMPLIANT items                                | [N]   |
| Policy areas absent                            | [N]   |

**Top 3 urgent findings**: [one-line descriptions of the most material items]

---

## Critical Risk Items

### [Policy Name] — ⚠ CRITICAL RISK | Confidence: [level]

**What the handbook says**: [summary or verbatim excerpt of problematic language]
**Liability mechanism**: [specific explanation of how this language creates exposure]
**Legal basis**: [statute, regulation, or NLRB decision — full citation]
**Jurisdiction(s)**: [federal / specific state(s)]
**Recommended language**: [specific compliant draft text]
**State-specific note**: [if state-specific variation needed]
**Action**: Escalate to employment counsel immediately. Do not distribute until resolved.

[Repeat for each CRITICAL RISK item]

---

## Non-Compliant Items

### [Policy Name] — NON-COMPLIANT | Confidence: [level]

**Finding**: [what is missing or what current language says]
**Legal basis**: [statute, regulation — full citation]
**Jurisdiction(s)**: [federal / specific state(s)]
**Recommended language**: [specific compliant draft text]
**Priority**: Remediate before next handbook distribution.

[Repeat for each NON-COMPLIANT item]

---

## Update Required Items

### [Policy Name] — UPDATE REQUIRED | Confidence: [level]

**Finding**: [what needs updating and why]
**Trigger**: [statutory change, new EEOC guidance, or best-practice standard]
**Recommended language or guidance**: [specific draft text or directional guidance]
**Priority**: Include in next annual revision cycle.

[Repeat for each UPDATE REQUIRED item]

---

## Compliant Items

The following policy areas were reviewed and found COMPLIANT with applicable law as
of the date of this review:

- [Policy Area 1] — [brief basis]
- [Policy Area 2] — [brief basis]
  [...]

---

## Missing Policies

Policies entirely absent from the handbook:

| Policy Area | Classification                  | Legal Basis | Action             |
| ----------- | ------------------------------- | ----------- | ------------------ |
| [Name]      | [CRITICAL RISK / NON-COMPLIANT] | [statute]   | [immediate action] |

[...]

---

## Multi-State Compliance Matrix

[For multi-state employers — one row per policy area, one column per jurisdiction]

| Policy Area         | Federal         | [State 1]                  | [State 2]          | [State 3]           | Status            |
| ------------------- | --------------- | -------------------------- | ------------------ | ------------------- | ----------------- |
| FMLA/Family Leave   | 12 wks (50+ EE) | CFRA: 12 wks (5+ EE)       | NYPFL: 12 wks      | FAMLI: 12 wks (10+) | [COMPLIANT / GAP] |
| Harassment Training | EEOC recommends | 2h sup / 1h EE (mandatory) | Annual (mandatory) | Annual (mandatory)  | [COMPLIANT / GAP] |

[...]

---

## Remediation Checklist

**Tier 1 — Immediate (before next distribution):**

- [ ] [CRITICAL RISK item] — [specific action required] — [owner]
- [ ] [NON-COMPLIANT item] — [specific action required] — [owner]

**Tier 2 — Before Next Workforce Distribution:**

- [ ] [NON-COMPLIANT item] — [specific action]

**Tier 3 — Annual Review Cycle:**

- [ ] [UPDATE REQUIRED item] — [specific action]

**Recommended next review date**: [date + trigger conditions]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-employee-handbook-review"
  handbook: "[name and version if identifiable]"
  review_date: "[date]"
  jurisdictions_covered: "[list from Step 2]"
  workforce_size: "[bracket]"
  industry: "[from Step 2]"
  union_status: "[from Step 2]"
  explicit_assumptions: "[list any defaults applied]"
  policy_areas_reviewed: "[count]"
  policy_areas_present: "[count]"
  policy_areas_missing: "[list]"
  critical_risk_items: "[count]"
  non_compliant_items: "[count]"
  update_required_items: "[count]"
  compliant_items: "[count]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "Title VII, Civil Rights Act 1964, 42 U.S.C. § 2000e et seq. — [VERIFIED/UNVERIFIED]"
    - "Stericycle, Inc., 372 NLRB No. 113, August 2, 2023 — [VERIFIED/UNVERIFIED]"
    - "[additional citations]"
  self_interrogation: "[PASS / REVISED — explanation / NOT APPLICABLE — no CRITICAL items]"
  citation_quality_gates: "[ALL PASS / GATE [N] FAILED — explanation]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  explicit_assumptions:
    - "[e.g., 50+ employee threshold applied — user reported 150 employees]"
    - "[e.g., NLRB Stericycle standard applied — verify current enforcement posture]"
  limitations:
    - "Law verified as of early 2026; [CHECK CURRENCY] for recent amendments"
    - "NLRB standards subject to change with administration; verify Stericycle current status"
    - "State law analysis limited to jurisdictions identified in Step 2 — expand for new state entries"
    - "DOL salary threshold figures [CHECK CURRENCY — subject to ongoing litigation]"
    - "Cannabis employment protection state list rapidly changing — verify current state list"
  reviewer: "AI-assisted — requires review by qualified employment attorney before handbook distribution"
```
````

---

## Localization Notes

### US Multi-State Handbook Architecture

**Universal core + state supplements** (recommended by Seyfarth, Littler, Fisher Phillips):

- Core handbook: federal baseline; at-will disclaimer; EEO policy (all federal classes
  - gender identity post-_Bostock_); NLRA § 7-compliant policies; ADA + PWFA + PUMP Act
    accommodation procedures; FMLA policy (where applicable); FLSA wage and hour baseline;
    OSHA safety policy
- State supplement: mandatory additions for each state where employees work; supplement
  must include a supremacy clause: _"This supplement applies to all employees working in
  [State] and supersedes the core handbook to the extent of any conflict"_
- Supplement format: short (2–5 pages per state); addresses only material state
  deviations from the core

**Version control**: Each supplement carries its own version date. Track independently
of core handbook version.

### UK Specific Localization

**Contract vs. handbook distinction**: UK employment law creates a distinction between
the written statement of particulars (legally required, contractually binding) and the
employee handbook (may or may not be contractually incorporated). Clearly state in the
handbook whether it is contractually incorporated or guidance only.

**ACAS Code compliance**: Disciplinary and grievance procedures must follow the ACAS
Code of Practice on Disciplinary and Grievance Procedures (2015, updated guidance
anticipated post-ERA 2025). Non-compliance can result in up to 25% uplift in any
Employment Tribunal compensatory award.

**Employment Rights Act 2025 (ERA 2025)**: Royal Assent December 18, 2025. Most
provisions take effect 2026–2027 via statutory instruments. Key changes requiring handbook
revision: flexible working from Day 1; unfair dismissal protection from Day 1 (removing
2-year qualifying period); zero-hours guaranteed hours entitlement after 12 weeks.
[VERIFY commencement dates for specific provisions.]

### Australian Specific Localization

**Fair Work Information Statement**: Must be provided to every new employee before or
as soon as practicable after commencement. Handbook should reference (but not substitute
for) the FWIS.

**Right to disconnect (NES, effective August 26, 2024)**: Handbook must include a
right to disconnect policy. FAIR WORK COMMISSION model term or equivalent required in
all modern awards. Small businesses: effective August 26, 2025. [VERIFY FWC model
language and any Commission decisions on "unreasonable refusal" criteria.]

**Positive duty compliance (Respect at Work)**: Handbook policy alone does not satisfy
the positive duty under Sex Discrimination Act 1984 (Cth). Organizations must demonstrate
active measures across AHRC's 7 compliance standards (leadership, culture, knowledge,
risk management, support, reporting, monitoring/evaluation). Note this limitation
explicitly in the output.

---

## Provenance

Created by Legalcode (2026-03-01). Mode A (Create from scratch). Research methodology:
2-agent pipeline — Agent 1 (legal research: US federal requirements matrix, Title VII/ADA/
ADEA/FMLA/NLRA/_Stericycle_/FLSA/OSHA/GINA/USERRA/PUMP Act/PWFA analysis; state hot spots
CA/NY/IL/WA/OR; UK ERA 1996/Equality Act 2010/Employment Rights Act 2025; AU Fair Work
Act 2009/NES/Closing Loopholes/positive duty; 20 high-risk drafting errors; multi-state
handbook architecture best practices from Seyfarth/Littler/Fisher Phillips) + Agent 2
(prompt engineering/quality: legalcode-contract-review pattern extraction; legalcode-
us-breach-notification-triage compliance adaptation; 4-tier severity system design;
8-step workflow with CLARIFY points; 16-category policy checklist; 20 anti-patterns;
Glass Box YAML design). Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers.
