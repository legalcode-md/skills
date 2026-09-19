---
name: legalcode-uk-whistleblower-program-builder
description: Build, audit, and design UK whistleblowing frameworks under the Public Interest Disclosure
  Act 1998 (PIDA) and Employment Rights Act 1996 Part IVA (ss.43A-43L, s.47B, s.103A) for England and
  Wales. Use when building a whistleblowing programme from scratch, auditing an existing programme for
  PIDA/FCA compliance gaps, reviewing employment agreements for void confidentiality language, assessing
  detriment or dismissal risk in a specific case, designing investigation procedures, responding to an
  FCA SYSC 18 supervisory review, or advising a board on governance obligations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Build, audit, and design UK whistleblowing frameworks under the Public Interest Disclosure Act 1998 (PIDA) and Employment Rights Act 1996 Part IVA (ss.43A-43L, s.47B, s.103A) for England and Wales. Covers worker status (extended s.43K definition), all six categories of qualifying disclosure (s.43B), public interest requirement (post-ERRA 2013), protected disclosure routes (ss.43C-43H), detriment and automatic unfair dismissal risk, unlimited compensation exposure (s.123A), interim relief (s.128), vicarious liability (s.47B(1A)), the Jhuti tainted-decision doctrine, Kong separability principle, settlement agreement restrictions, FCA/PRA SYSC 18 sector-specific requirements (whistleblowers' champion, annual board report, SYSC 18.3 settlement agreement term), SM&CR interaction, prescribed persons reporting (ERA s.43F; Prescribed Persons Order 2014 as amended to SI 2025/604), internal and external reporting channel architecture, investigation sequencing and independence, board and audit committee escalation, employer-facing policy design, UK GDPR / DPA 2018 data-handling obligations, and NHS Freedom to Speak Up framework. Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY gap analysis with remediation roadmap and Glass Box audit trail. Use when building a whistleblowing programme from scratch, auditing an existing programme for PIDA/FCA compliance gaps, reviewing employment agreements for void confidentiality language, assessing detriment or dismissal risk in a specific case, designing investigation procedures, responding to an FCA SYSC 18 supervisory review, or advising a board on governance obligations. Jurisdiction: England and Wales (primary); Scotland and Northern Ireland share PIDA but have different prosecution authorities and some distinct overlay provisions — note where relevant.


# UK Whistleblower Programme Builder (PIDA / ERA 1996 / FCA SYSC 18)

> **Disclaimer**: This skill provides an AI-assisted framework for building and assessing
> UK whistleblowing programmes under the Public Interest Disclosure Act 1998 and associated
> legislation. It does not constitute legal advice, employment law advice, or regulatory
> guidance from the FCA or PRA. All outputs must be reviewed by a qualified solicitor or
> barrister experienced in employment law and, for regulated firms, by compliance counsel
> with FCA/PRA expertise, before implementation. Statutory citations, case law holdings, and
> regulatory references cited here carry hallucination risk — verify against current
> legislation at legislation.gov.uk, FCA Handbook at handbook.fca.org.uk, and authoritative
> case databases (BAILII, WestLaw, LexisNexis) before relying on them. Employment tribunal
> awards, PIDA interpretation, and FCA enforcement priorities evolve; confirm current state
> before use.

---

## Purpose and Scope

This skill designs, audits, and remediates whistleblowing programmes for organisations
operating in England and Wales. It anchors every recommendation to the specific statutory
framework of ERA 1996 Part IVA (as amended by PIDA 1998 and ERRA 2013) and, for regulated
financial services firms, FCA SYSC 18 and PRA SS39/15.

**Covers:**

- Qualifying disclosure analysis — all six categories under ERA 1996 s.43B(1)
- Worker status mapping — extended definition under ERA 1996 s.43K (employees, contractors,
  agency workers, LLP members, trainees, NHS practitioners, police officers)
- Public interest requirement — Enterprise and Regulatory Reform Act 2013 s.17 amendment
- Protected disclosure routes — employer (s.43C), legal adviser (s.43D), Minister (s.43E),
  prescribed persons (s.43F), wider/public disclosure (ss.43G-43H)
- Detriment framework — ERA 1996 s.47B including vicarious liability (s.47B(1A)) for
  co-worker detriment
- Automatic unfair dismissal — ERA 1996 s.103A (no qualifying period; principal reason test;
  unlimited compensation per s.123A)
- Jhuti tainted-decision doctrine — Royal Mail Group Ltd v Jhuti [2019] UKSC 55
- Kong separability principle — Kong v Gulf International Bank [2022] EWCA Civ 941
- Interim relief — ERA 1996 s.128 (7-day deadline; "pretty good" prospect test)
- Settlement agreement restrictions — void confidentiality clauses; s.111A(3) exception;
  SYSC 18 mandatory settlement agreement term for FCA/PRA-regulated firms
- FCA SYSC 18 requirements — whistleblowers' champion, annual board report, settlement
  agreement language, training, external reporting obligation
- SM&CR interaction — conduct rules, personal accountability, culture obligations
- Prescribed persons external reporting — ERA s.43F; SI 2014/2932 as amended to SI 2025/604
  (HM Treasury added for financial sanctions, June 2025)
- Internal reporting channel architecture — design, third-party providers, anonymity,
  confidentiality, routing logic, acknowledgment timelines
- Investigation sequencing — independence screening, privilege election, evidence
  preservation, feedback obligations
- Board escalation and governance framework
- Policy design — minimum required elements and operational procedures
- UK GDPR / Data Protection Act 2018 interface — data handling during investigations
- NHS Freedom to Speak Up — National Guardian's Office, FTSU Guardian requirements,
  quarterly and annual reporting
- COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY classification
- IMMEDIATE / NEAR-TERM / BACKGROUND remediation prioritisation
- Glass Box audit trail for board, counsel, and regulatory examination

**Does not:**

- Conduct live employment tribunal advocacy or draft claim forms (see
  `legalcode-uk-employment-tribunal-claim` for the litigation workflow)
- Assess multi-jurisdiction programmes beyond UK primary scope (see
  `legalcode-whistleblower-program-builder` for EU Directive 2019/1937, US SOX/Dodd-Frank,
  France Sapin II/Loi Waserman coverage)
- Constitute a legal opinion on specific prosecution risk or tribunal outcome
- Apply the full FCA/PRA regulatory framework — for broader SM&CR and Threshold Conditions
  assessment see `legalcode-uk-fca-regulatory-compliance`
- Certify programme adequacy — that is a determination for qualified counsel

**Related skills:**

- `legalcode-whistleblower-program-builder` — multi-jurisdiction (EU/US/FR/UK) scaffold;
  use when assessing a programme across jurisdictions simultaneously
- `legalcode-uk-employment-tribunal-claim` — employment tribunal procedural framework;
  use when a detriment or s.103A dismissal claim is being filed or defended
- `legalcode-uk-fca-regulatory-compliance` — full FCA regulatory compliance assessment
- `legalcode-workplace-investigation` — investigation planning and conduct procedures;
  cross-reference when designing or running a specific investigation
- `legalcode-de-betriebsrat-consultation` / `legalcode-fr-cnil-privacy-compliance` — if
  the employer has works council or CNIL obligations touching whistleblowing

---

## Jurisdiction and Governing Law

**Primary legislation**: Employment Rights Act 1996 (ERA 1996) Part IVA, as amended by
the Public Interest Disclosure Act 1998 (PIDA 1998) and the Enterprise and Regulatory
Reform Act 2013 (ERRA 2013) s.17 (public interest requirement, effective 25 June 2013).

**Key statutory provisions:**

| Provision          | Content                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------ |
| ERA 1996 s.43A     | Definition of "protected disclosure"                                                       |
| ERA 1996 s.43B     | "Qualifying disclosure" — six categories of relevant failure + public interest requirement |
| ERA 1996 s.43C     | Disclosure to employer or responsible person (internal route)                              |
| ERA 1996 s.43D     | Disclosure to legal adviser                                                                |
| ERA 1996 s.43E     | Disclosure to Minister of the Crown                                                        |
| ERA 1996 s.43F     | Disclosure to prescribed person (regulator)                                                |
| ERA 1996 s.43G     | Wider disclosure (public disclosure in limited circumstances)                              |
| ERA 1996 s.43H     | Disclosure of exceptionally serious failure                                                |
| ERA 1996 s.43J     | Contractual duty of confidentiality — void to the extent it prevents qualifying disclosure |
| ERA 1996 s.43K     | Extended definition of "worker" for PIDA purposes                                          |
| ERA 1996 s.47B     | Right not to suffer detriment; vicarious liability (s.47B(1A))                             |
| ERA 1996 s.103A    | Automatic unfair dismissal where principal reason is protected disclosure                  |
| ERA 1996 s.123A    | Removal of compensation cap for s.103A dismissals                                          |
| ERA 1996 s.128     | Interim relief application (7-day deadline; "pretty good" prospect test)                   |
| ERA 1996 s.111A(3) | Protected conversations exception — whistleblowing claims excluded                         |
| ERRA 2013 s.17     | Inserted public interest requirement into s.43B                                            |
| ERRA 2013 s.18     | Removed good faith requirement; tribunal discretion to reduce award by up to 25%           |

**Secondary and regulatory materials:**

- The Public Interest Disclosure (Prescribed Persons) (Amendment) Order 2025, SI 2025/604
  (HM Treasury added as prescribed person for UK financial sanctions breaches; in force
  26 June 2025) [VERIFY currency at legislation.gov.uk]
- FCA SYSC 18 (Whistleblowing module) — mandatory for UK deposit-takers with ≥ £250m
  assets, PRA-designated investment firms, Solvency II insurers, Lloyd's; non-binding
  guidance for all other FCA-regulated firms
- FCA Policy Statement PS15/24 (October 2015); PRA Supervisory Statement SS39/15
- FCA/PRA joint consultation CP15/31; implementation deadline September 7, 2016
- NHS Freedom to Speak Up: National Guardian's Office requirements; NHSE National Freedom
  to Speak Up Policy (NHS-specific overlay)

**Leading case law:** [VERIFY citations against BAILII/WestLaw before relying on them]

- _Darnton v University of Surrey_ [2002] UKEAT 882_01_1112 — reasonable belief test;
  assessed on facts as understood by worker, not actual facts
- _Royal Mail Group Ltd v Jhuti_ [2019] UKSC 55 — tainted-decision doctrine; innocent
  decision-maker manipulated by colleague who knew of disclosure; dismissal still
  automatically unfair
- _Kong v Gulf International Bank (UK) Ltd_ [2022] EWCA Civ 941 — separability principle;
  conduct distinct from the disclosure itself may be the principal reason for dismissal
- _Osipov v International Petroleum Ltd_ (EAT 2023) — individual directors personally
  liable for whistleblowing detriment under s.47B(1A); awards in excess of £2 million
- _Sullivan v Isle of Wight Council_ [2024] EAT 3 — external job applicants do NOT have
  worker status for PIDA purposes; protection requires a pre-existing worker relationship
- _Clyde & Co v Bates van Winkelhof_ [2014] UKSC 32 — LLP members are "workers" within
  s.43K; protected by PIDA
- _Parkins v Sodexho Ltd_ [2002] — prior to ERRA 2013; breach of own employment contract
  could qualify; now excluded by public interest requirement [VERIFY]
- _Chesterton Global v Nurmohamed_ [2017] EWCA Civ 979 — public interest test; disclosure
  affecting only a group of employees may still satisfy the test

**Territorial scope:**

- England and Wales: Employment Tribunal (England and Wales) jurisdiction
- Scotland: Same PIDA statute but Crown Office and Procurator Fiscal Service (COPFS);
  Scottish Employment Tribunal system; note Scottish law differences on some employment
  matters
- Northern Ireland: Employment Rights (Northern Ireland) Order 1996 (similar but distinct);
  Public Prosecution Service NI
- This skill focuses on England and Wales; flag where Scotland and NI diverge materially

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's organisational context, the workflow pauses and asks when:

- The answer materially changes the regulatory framework or statutory analysis
- Multiple valid programme design approaches exist and organisational factors determine
  the right choice
- Worker status, sector, or organisational structure is ambiguous
- An enforcement or investigation context changes priorities

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

Accept the engagement in any of these forms:

- **New programme build**: Organisation description + sector + employee count + regulatory
  drivers (FCA/PRA? NHS? General employer?)
- **Programme audit**: Existing policy documents, procedure manuals, training records,
  channel descriptions, investigation logs (anonymised)
- **Specific case risk assessment**: Facts of a specific situation — worker identity,
  disclosure made, detriment alleged — for detriment/dismissal risk analysis
- **Employment agreement review**: Agreement text for void confidentiality or NDA language
  that impedes PIDA rights
- **Board readiness**: Request for executive-facing assessment and governance recommendations
- **FCA/SYSC 18 supervisory review prep**: Preparation for FCA supervisory review of
  SYSC 18 obligations
- **Investigation design**: Request for investigation protocol and independence mapping

If insufficient context is provided, proceed immediately to Step 2 (context gathering).

---

### Step 2: Gather Organisational Context

**⟁ CLARIFY** — Ask the following before proceeding. Skip questions already answered:

**1. Engagement mode** — What should this engagement produce?

- **Build new programme** — Full programme design: policy, channels, procedures, governance,
  training, rollout roadmap
- **Audit existing programme** — Gap assessment against PIDA and applicable regulatory
  requirements
- **Detriment / dismissal risk assessment** — Case-specific analysis of a situation already
  in progress or recently completed
- **Employment agreement / NDA review** — Audit for void confidentiality language and
  Dodd-Frank / SYSC 18 settlement agreement compliance
- **Board readiness** — Executive summary, maturity score, governance recommendations
- **FCA SYSC 18 compliance review** — Targeted assessment of SYSC 18 requirements
- _Why this matters_: Each mode produces different outputs and engages different sections
  of the workflow.

**2. Organisation type and sector** — What is the employer?

- Options: FCA/PRA-regulated financial services firm (specify: bank, insurer, investment
  firm, other); NHS trust or foundation trust; Central government / public body; Private
  sector general employer; Charity or third sector; Other
- If FCA/PRA-regulated: Is the firm subject to **mandatory** SYSC 18 requirements (UK
  deposit-taker ≥ £250m assets; PRA-designated investment firm; Solvency II insurer;
  Lloyd's)?
- _Why this matters_: FCA SYSC 18 imposes mandatory procedures, whistleblowers' champion,
  and settlement agreement requirements for in-scope firms. NHS has Freedom to Speak Up
  overlay. General employers face PIDA only.

**3. Organisation size and structure**:

- Employee count (UK total; global if multinational)
- Are workers classified as employees, contractors, agency workers, or LLP members?
  (PIDA's extended s.43K definition covers all, but remedies differ slightly)
- Is the organisation part of a group? (Third-party managers / associated employer
  questions may arise under s.47B)
- _Why this matters_: Proportionality of programme design; agency worker and LLP member
  analysis under s.43K

**4. Current programme status**:

- Options: No policy in place; Written policy but no operational procedures; Partial
  programme (policy + channel but gaps elsewhere); Full programme claimed; Programme under
  review post-incident or regulatory inquiry
- Has there been a relevant tribunal claim, regulatory inquiry, or significant internal
  incident?
- _Why this matters_: Determines whether to design from scratch or remediate specific gaps.

**5. Specific focus areas** (allow multiple):

- Worker status and qualifying disclosure analysis
- Protected disclosure routes and prescribed persons mapping
- Detriment and dismissal risk for a specific case
- Internal reporting channel design and third-party provider evaluation
- Investigation independence and sequencing
- FCA SYSC 18 compliance (champion, board report, settlement language)
- SM&CR interaction and culture assessment
- Policy drafting — mandatory elements
- Employment agreement / NDA audit
- Board escalation and governance
- NHS Freedom to Speak Up framework
- Scotland / Northern Ireland overlay

---

### Step 3: Map the Statutory Framework

Before analysing the programme or situation, establish the precise legal framework:

#### 3a. Worker Status Analysis

Identify whether the relevant individuals are "workers" under ERA 1996 s.43K. The
extended definition covers:

| Category                     | Coverage                                                                     | Notes                                                                               |
| ---------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Employees (s.43K(2)(a))      | All employees under a contract of employment                                 | Core category; full ERA rights                                                      |
| Agency workers (s.43K(2)(b)) | Where terms substantially determined by end-user                             | Claims possible against end-user; _Southern Cross Healthcare v Perkins_ [2010] EWCA |
| Contractors (s.43K(1)(a))    | Contract personally to perform work or services (other than client/customer) | Must be personal service; check _Pimlico Plumbers v Smith_ [2018] UKSC 29           |
| LLP members                  | Partners in a limited liability partnership                                  | _Bates van Winkelhof_ [2014] UKSC 32: LLP members are workers                       |
| NHS practitioners            | GPs, dentists, pharmacists, optometrists under NHS contracts                 | ERA s.43K(3): deemed workers for PIDA purposes                                      |
| Crown employees              | Civil servants, government employees                                         | s.191 ERA 1996; protection applies                                                  |
| Police officers              | Constables                                                                   | Specific extension; check rank-specific regulations                                 |
| Trainees                     | Training contracts where not employees                                       | s.43K(1)(b): vocational training contracts                                          |
| Post-termination detriment   | Former workers                                                               | Protection applies to post-employment detriment (references, ongoing harassment)    |
| External applicants          | Job applicants without pre-existing worker relationship                      | NOT protected per _Sullivan v Isle of Wight Council_ [2024] EAT 3                   |

**⟁ CLARIFY** — For any case involving contractors, agency workers, or LLP members:

- Is the individual's personal service to the organisation (distinguishing from a true
  business-to-business relationship)?
- Does the individual have control over their own substitution — can they send a substitute?
  If yes, the personal service requirement may not be met.
- For agency workers: did the end-user substantially determine the terms of engagement?

#### 3b. Qualifying Disclosure Analysis

A "qualifying disclosure" requires (ERA 1996 s.43B):

1. **Disclosure of information** — not mere expression of concern; must provide facts [VERIFY
   _Cavendish Munro Professional Risks Management v Geduld_ [2010] IRLR 38]
2. **Reasonable belief** — the worker must reasonably believe the information tends to show
   a relevant failure; assessed on facts as worker understood them (_Darnton_ [2002])
3. **In the public interest** — added by ERRA 2013; worker must reasonably believe disclosure
   is in the public interest; blocks purely personal employment contract disputes
   (_Chesterton Global_ [2017])

**The six categories of relevant failure (s.43B(1)):**

| Category                   | ERA 1996 s.43B(1) | Examples                                                              |
| -------------------------- | ----------------- | --------------------------------------------------------------------- |
| Criminal offences          | (a)               | Fraud, theft, bribery, market abuse, Health & Safety Act breaches     |
| Breach of legal obligation | (b)               | Regulatory breach, contract breach by employer, statutory duty breach |
| Miscarriage of justice     | (c)               | Wrongful conviction, perversion of justice within the organisation    |
| Health and safety danger   | (d)               | Unsafe working conditions, risk to public safety, near-misses         |
| Environmental damage       | (e)               | Pollution, illegal dumping, breach of environmental permit            |
| Deliberate concealment     | (f)               | Cover-up of any of the above five categories                          |

**Public interest test guidance** (post-ERRA 2013):

- A disclosure affecting only the worker personally (e.g., own contract breach) requires
  additional factors to satisfy the public interest test [VERIFY]
- A disclosure affecting a group of workers (even a small group) may satisfy the test
  (_Chesterton Global_ [2017] — 100 workers)
- Worker's honest and reasonable belief that the disclosure is in the public interest is
  sufficient; no need for the disclosure to actually be in the public interest

#### 3c. Protected Disclosure Route Analysis

A qualifying disclosure becomes a "protected disclosure" under ERA 1996 s.43A only if made
through an appropriate route (ss.43C-43H):

| Route                         | Statutory basis | Conditions                                                                                                                       |
| ----------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Employer / responsible person | s.43C           | No additional conditions; internal disclosure route                                                                              |
| Legal adviser                 | s.43D           | Made in course of obtaining legal advice; covers solicitor-client privileged communication                                       |
| Minister of the Crown         | s.43E           | Employer is appointed by the Crown; limited route                                                                                |
| Prescribed person             | s.43F           | Must be within the prescribed person's area of responsibility; Prescribed Persons Order 2014 as amended                          |
| Wider / public disclosure     | s.43G           | Reasonable belief substantially true; not for personal gain; one of four gateway conditions met; reasonable in all circumstances |
| Exceptionally serious failure | s.43H           | Failure is exceptionally serious; reasonable belief substantially true; not for personal gain; reasonable to disclose            |

**Key prescribed persons for financial services** (ERA 1996 s.43F; SI 2014/2932 as amended):

- Financial Conduct Authority (FCA) — all FCA-regulated activities
- Prudential Regulation Authority (PRA) — PRA-regulated firms
- Bank of England — financial stability matters
- Financial Reporting Council (FRC) — accounting, auditing, actuarial standards
- HM Treasury — UK financial sanctions breaches (added SI 2025/604; in force 26 June 2025)
  [VERIFY currency]
- Health and Safety Executive (HSE) — workplace health and safety
- Environment Agency — environmental matters (England)
- Information Commissioner's Office (ICO) — data protection
- Competition and Markets Authority (CMA) — competition law
- Serious Fraud Office (SFO) — serious fraud and corruption
  [Full list: gov.uk/government/publications/blowing-the-whistle-list-of-prescribed-people-and-bodies--2]

**Wider disclosure (s.43G) — four gateway conditions** (at least one required):

1. Worker reasonably believed the employer would subject them to detriment if disclosed
   internally
2. No prescribed person responsible for the subject matter and worker disclosed internally
   and reasonably believed employer would suppress/destroy evidence
3. Worker previously disclosed substantially the same information to employer or prescribed
   person
4. Failure is exceptionally serious and circumstances make wider disclosure reasonable

---

### Step 4: Gather Legal Authority via legalcode-mcp

Use **legalcode-mcp** to build a working legal reference for this engagement.

**Search for:**

- Current text of ERA 1996 Part IVA (ss.43A-43L, s.47B, s.103A, s.123A, s.128)
- ERRA 2013 amendments currently in force
- Current Prescribed Persons Order (SI 2014/2932 as amended through SI 2025/604)
- FCA SYSC 18 current handbook text
- PRA SS39/15 current version
- Any Employment Appeal Tribunal or Court of Appeal decisions post-Kong [2022]

**Save results** to `/tmp/uk-whistleblower-authority.md` structured as:

```
# Legal Authority — UK Whistleblower Programme
## Date Gathered: [date]
### Primary Legislation (verified)
### Secondary Legislation (verified)
### FCA/PRA Handbook (verified)
### Case Law (verified)
```

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using research-backed knowledge; flag for mandatory verification before use

---

### Step 5: Assess Programme Against Core Domains

For audit or build engagements, assess the programme against the **seven core domains**
below. For new-build engagements, design each domain from scratch.

Rate each domain using the four-tier classification:

- **COMPLIANT** — Meets or exceeds all applicable statutory and regulatory requirements
- **PARTIAL** — Partially meets requirements; specific gaps identified with exposure level
- **NON-COMPLIANT** — Fails to meet requirements; tribunal / regulatory exposure exists
- **CRITICAL DEFICIENCY** — Material statutory breach or regulatory non-compliance that
  requires immediate remediation; risk of Employment Tribunal claim or FCA enforcement

---

#### Domain 1: Policy and Governance Framework

**Minimum required policy elements:**

| Element                            | Requirement                                                                                     | Notes                                                        |
| ---------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Definition of protected disclosure | Six categories of relevant failure; public interest requirement                                 | Use statutory language from ERA s.43B                        |
| Worker coverage statement          | All workers including contractors, agency workers, LLP members, trainees                        | Reference s.43K extended definition explicitly               |
| Reporting channels                 | Internal reporting routes clearly described; external prescribed persons listed                 | Must not deter external reporting                            |
| Confidentiality commitment         | Identity protection; access-limited case files; breach consequences                             | Cannot be used to prevent protected disclosure               |
| Anti-retaliation statement         | Zero-tolerance policy; specific prohibited conduct list                                         | Reference s.47B and personal liability exposure              |
| Investigation process              | Overview of steps; independence requirement; timeline commitments                               | Detailed procedure in separate operational document          |
| Board oversight                    | Audit committee / board oversight of programme; reporting line                                  | FCA: whistleblowers' champion must be non-executive director |
| External reporting rights          | Workers may report directly to FCA, PRA, and prescribed persons                                 | Cannot restrict or penalise external reporting               |
| Settlement agreement language      | No confidentiality clause prevents qualifying disclosure; settlement does not waive PIDA rights | SYSC 18.3.7 mandatory for FCA/PRA in-scope firms             |
| Review and training commitment     | Annual review; training for all workers, managers, and senior leaders                           | FCA SYSC 18 training obligation                              |

**FCA SYSC 18 mandatory elements** (for in-scope firms only):

| Requirement                                                              | SYSC 18 Reference | Deadline                       |
| ------------------------------------------------------------------------ | ----------------- | ------------------------------ |
| Appoint whistleblowers' champion (non-executive director)                | SYSC 18.4.1R      | Implemented (since March 2016) |
| Whistleblowers' champion annual report to governing body                 | SYSC 18.4.4R      | Annual                         |
| Settlement agreement term (right to make protected disclosure preserved) | SYSC 18.3.7R      | Implemented                    |
| Inform employees they may report directly to FCA/PRA                     | SYSC 18.3.4R      | Implemented                    |
| Training on recognising and handling disclosures                         | SYSC 18.3.5R      | Annual minimum                 |
| Maintain arrangements for handling requests for confidentiality          | SYSC 18.3.1R      | Ongoing                        |
| Maintain arrangements preventing victimisation                           | SYSC 18.3.1R      | Ongoing                        |

**SM&CR interaction** (FCA/PRA regulated firms):

- Responsibility for maintaining an effective whistleblowing culture is a Senior Management
  responsibility under the Senior Managers Regime
- Failure to maintain effective whistleblowing procedures may constitute a breach of
  Individual Conduct Rule 2 (acting with due skill, care, and diligence) and Senior Manager
  Conduct Rule 4 (disclosing appropriately to FCA/PRA) [VERIFY current COCON text]
- Whistleblowers' champion is not itself an SMF, but the appointed individual's conduct
  in the role may be assessed under general conduct obligations

**⟁ CLARIFY** — For FCA/PRA-regulated firms:

- Has a whistleblowers' champion been appointed? Is it a non-executive director?
- Has the champion produced the required annual report to the governing body?
- Do settlement agreements and severance documents include the SYSC 18.3.7 mandatory
  term? If not, this is NON-COMPLIANT with an IMMEDIATE remediation classification.

---

#### Domain 2: Worker Coverage and Qualifying Disclosure Assessment

**Assess whether the programme's scope of protection is correct:**

- Does the policy extend protection to all workers under s.43K (not just employees)?
- Are contractors and agency workers explicitly included or excluded from the policy scope?
  If excluded, is there a legal basis or is this a gap?
- Does the policy define "qualifying disclosure" in terms consistent with ERA s.43B?
- Does the policy explain the public interest requirement added by ERRA 2013?
- Does the policy address the "disclosure of information" requirement (mere allegations
  without information may not qualify — _Geduld_ [2010])?

**Analyse any specific situation** for qualifying disclosure status:

```
Qualifying Disclosure Checklist (per situation):
☐ The worker discloses information (not just allegation or opinion)
☐ Worker reasonably believes information tends to show a relevant failure
   (s.43B(1)(a)-(f) — which category or categories?)
☐ Worker reasonably believes the disclosure is in the public interest
   (post-ERRA 2013; distinguish personal contract complaints)
☐ Disclosure made through appropriate route (s.43C-43H — which?)
   If s.43F: Is the subject matter within the prescribed person's remit?
   If s.43G-43H: Are the gateway conditions met?
```

---

#### Domain 3: Reporting Channel Architecture

Design or assess the internal reporting infrastructure:

**Channel design principles:**

| Principle            | Application                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Independence         | Channel must not be controlled by operational management in the area being reported; best practice — third-party intake provider |
| Anonymity capability | Must support anonymous submissions; note UK GDPR impact on investigating anonymous reports                                       |
| Accessibility        | Available 24/7; multi-language where workforce requires it; accessible to remote/hybrid workers                                  |
| Non-intimidating     | Secure, confidential, not routed through line management                                                                         |
| Audit trail          | Every submission must be date-stamped and assigned a case reference; acknowledgment generated automatically                      |
| Confidentiality      | Reporter identity accessible only to designated personnel; segregated from HR / personnel files                                  |

**Routing logic — who receives and handles reports:**

| Allegation Type                      | Primary Handler                                  | Escalation Trigger                       |
| ------------------------------------ | ------------------------------------------------ | ---------------------------------------- |
| Financial crime / accounting / audit | Audit Committee (Board); outside counsel         | Immediately if executive involved        |
| Anti-bribery / corruption            | General Counsel / CCO                            | Board if senior executive                |
| Health and safety                    | HR + Compliance; HSE reporting if s.43F relevant | Regulator notification if mandatory      |
| Data protection / privacy            | Data Protection Officer + GC                     | ICO if personal data breach              |
| Regulatory breach (FCA/PRA)          | Compliance + GC                                  | Whistleblowers' champion (FCA/PRA firms) |
| Retaliation against reporter         | Audit Committee or Board                         | Outside counsel immediately              |
| Misconduct by investigator           | Board; independent outside counsel               |                                          |
| NHS clinical safety                  | FTSU Guardian + Medical Director                 | NHS Resolution if serious incident       |

**Acknowledgment timeline (best practice / statutory):**

| Regime                                         | Acknowledgment                                  | Substantive Update                                |
| ---------------------------------------------- | ----------------------------------------------- | ------------------------------------------------- |
| PIDA (England & Wales)                         | No statutory requirement; best practice: 7 days | No statutory requirement; best practice: 3 months |
| FCA SYSC 18 firms                              | SYSC 18.3.2G: promptly                          | Reasonable timescale                              |
| EU Directive 2019/1937 (if also EU operations) | 7 days mandatory                                | 3 months mandatory                                |

**⟁ CLARIFY** — Channel architecture decisions:

- Does the organisation currently operate its own internal channel or engage a third-party
  intake provider? Third-party providers improve independence and perceived safety.
- Is anonymous reporting currently supported? What investigation procedures apply to
  anonymous reports (note that UK GDPR may limit use of data from anonymous investigations
  in disciplinary proceedings)?
- Are multi-language materials required for the workforce?

---

#### Domain 4: Investigation Sequencing and Independence

**Investigation protocol requirements:**

**Step 1 — Intake and triage** (on receipt of report):

1. Date-stamp and assign case reference number
2. Acknowledge receipt to reporter (if identity known)
3. Classify allegation type using routing matrix (Domain 3)
4. Conduct **independence screen**: identify all potential conflicts
   - Is the respondent the investigator's manager or line report?
   - Does the investigator have personal or professional relationship with respondent?
   - Was the investigator involved in the decision or conduct being reported?
   - Is the investigator in the respondent's reporting line?
5. If conflict exists: escalate to alternative investigator or outside counsel

**Step 2 — Privilege election** (before investigation begins):

- Decide at outset: Is this an attorney-directed investigation (legal professional privilege
  may apply to investigation materials) or an HR/Compliance-directed investigation
  (materials potentially disclosable)?
- Document the decision and rationale in the investigation file
- If attorney-directed: Ensure all significant communications and documents are directed
  to and from legal counsel [VERIFY current English law privilege analysis]
- **Note**: Three Rivers [2004] UKHL 48 established narrow scope of litigation privilege
  in English law for investigation materials; obtain current advice from qualified privilege
  counsel before relying on attorney-client privilege protection [VERIFY]

**Step 3 — Investigator assignment by complexity tier:**

| Tier        | Characteristics                                                                           | Investigator                                                | Counsel                       |
| ----------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------- |
| PRELIMINARY | Single allegation; limited impact; no senior management involvement                       | HR officer / Compliance officer                             | Optional                      |
| STANDARD    | Multiple allegations; financial impact possible; middle management involved               | Senior Compliance / CCO designee                            | Recommended                   |
| COMPLEX     | Regulatory implications; board-level; executive involvement; significant financial impact | CCO + senior outside employment counsel                     | Required                      |
| CRISIS      | Criminal exposure; regulatory investigation triggered; board governance failure           | Independent outside counsel lead; board committee oversight | Required; GC and CEO informed |

**Step 4 — Evidence preservation:**

- Litigation hold should be applied immediately upon reasonable anticipation of dispute
  or regulatory inquiry arising from the disclosure
- Identify all custodians (reporter, respondent, witnesses); preserve documents in all
  formats (email, messaging apps, physical)
- UK GDPR / DPA 2018: data preservation must be proportionate; cannot retain indefinitely

**Step 5 — Reporter feedback:**

- Keep reporter informed of investigation status without revealing information that would
  breach respondent confidentiality
- Advise reporter whether the matter has been referred to an external regulator
  (if required to do so under applicable regulatory regime)
- Do NOT commit to disclosing investigation outcome in full

**Step 6 — Post-investigation actions:**

- Document findings and conclusions
- Implement remediation where required
- Record and retain case file with appropriate retention period (UK GDPR: no prescribed
  period; best practice — retain through any applicable limitation period for tribunal
  claims, then delete or anonymise)
- Where the allegation is not substantiated, consider whether the reporter faces detriment
  risk from colleagues or management, and actively monitor

**⟁ CLARIFY** — Investigation design:

- For a specific situation in progress: Has an independence screen been completed? Are
  there any conflicts that would require an alternative investigator or outside counsel?
- Has privilege election been made and documented? (If not, materials may be disclosable
  in subsequent tribunal or regulatory proceedings.)

---

#### Domain 5: Detriment and Dismissal Risk

**This domain applies to any specific situation involving an identified worker and
potential detriment or dismissal.**

**5a. Detriment risk analysis (ERA 1996 s.47B):**

Detriment includes any act or deliberate failure to act by the employer **or co-worker**
(vicarious liability under s.47B(1A)) that adversely affects the worker:

**Common detriment acts:**

- Pay reduction, bonus denial, refusal of pay increase [CRITICAL EXPOSURE]
- Demotion or denial of promotion [CRITICAL EXPOSURE]
- Transfer to less favourable role or location [HIGH RISK]
- Exclusion from meetings, projects, or information flows [HIGH RISK]
- Unfavourable performance review immediately after disclosure [HIGH RISK — timing creates
  inference of causation]
- Disciplinary action or suspension post-disclosure [CRITICAL EXPOSURE]
- Hostile or bullying behaviour from line manager or colleagues [HIGH RISK]
- Issuing a poor reference after employment ends [HIGH RISK — post-termination detriment
  is actionable]
- Making settlement discussions inadmissible in whistleblowing claims (s.111A(3) exception
  applies; pre-termination negotiations are NOT protected) [CRITICAL EXPOSURE if used to
  suppress claim]

**Causation test (s.47B):** The protected disclosure must be a **material factor** (more
than trivial) in the detriment. This is a lower threshold than the s.103A dismissal test.

**Individual liability (s.47B(1A)):** Directors, managers, and colleagues can be personally
liable for detriment they cause; _Osipov_ [2023] EAT established awards exceeding £2 million
against individual directors. Personal liability arises independently of employer liability.

**⟁ CLARIFY** — For detriment risk assessment:

- What employment actions have been taken in relation to the worker since the protected
  disclosure was made?
- Is the decision-maker aware (or should be aware) of the protected disclosure?
- What is the time interval between the protected disclosure and the adverse action?
  (Short intervals create strong causation inferences)
- Is the same or similar treatment being applied to non-whistleblower colleagues?
  (Differential treatment strengthens causation)

**5b. Automatic unfair dismissal risk (ERA 1996 s.103A):**

Dismissal is **automatically unfair** if the protected disclosure is the **principal reason**
(or sole reason if only one) for the dismissal. No qualifying period required (applies
from day one).

**Jhuti tainted-decision doctrine** (_Jhuti_ [2019] UKSC 55):

- If an innocent decision-maker dismisses based on reasons manufactured by a colleague who
  knew of the protected disclosure, the dismissal is still automatically unfair
- The tribunal must penetrate through the invented reason to find the real reason
- _Implication_: Organisations cannot "clean" a whistleblowing dismissal by routing it
  through an uninformed decision-maker

**Kong separability principle** (_Kong_ [2022] EWCA Civ 941):

- If the employer dismisses for the **manner or conduct** of raising a concern (rather than
  the fact of the disclosure itself), the dismissal may not be automatically unfair under
  s.103A
- However: Tribunals scrutinise separability claims carefully; conduct must be genuinely
  distinct from the protected disclosure and must be the true reason, not a pretext

**Compensation for s.103A dismissals:**

- No statutory cap on compensation (ERA 1996 s.123A removes the normal compensatory award
  cap of approximately £120,000)
- Compensation includes: past loss of earnings to hearing; future loss (often substantial
  for senior workers); loss of benefits; injury to feelings (aggravated damages where
  conduct is particularly reprehensible)
- Basic award can be reduced by up to 25% if disclosure was not made in good faith
  (ERRA 2013 s.18)
- Reinstatement and re-engagement orders available but rarely granted

**Interim relief (ERA 1996 s.128):**

- Employee (not all workers) may apply for interim relief at employment tribunal
- 7-day deadline from EDT (effective date of termination) — cannot be extended
- Test: "Pretty good" prospect of establishing protected disclosure and causation at final
  hearing (higher than normal "reasonable prospect" test)
- If granted: employer must continue employment (or pay) until final hearing
- _Implication_: Interim relief risk is a critical factor in any s.103A dismissal decision

**5c. Settlement agreement restrictions:**

Any confidentiality clause in a compromise agreement or settlement agreement that purports
to prevent a qualifying disclosure is **void and unenforceable** under ERA 1996 s.43J.

The s.111A(3) exception to protected conversations (settlement discussions):

- Discussions about termination of employment are ordinarily inadmissible in ordinary
  unfair dismissal claims (ERA 1996 s.111A protected conversations)
- s.111A(3) **expressly excludes** automatic unfair dismissal claims (s.103A),
  whistleblowing detriment claims (s.47B), and discrimination claims from this protection
- Effect: The content of settlement discussions with a whistleblower **IS admissible** in
  any s.103A or s.47B claim brought by that worker

**FCA SYSC 18 settlement agreement mandatory term:** For in-scope firms, every settlement
or severance agreement must include express language making clear that the agreement does
not prevent the worker from making a protected disclosure to the FCA or PRA (SYSC 18.3.7R).
Any settlement without this term is **NON-COMPLIANT** with SYSC 18 requirements.

---

#### Domain 6: Board Escalation and Governance

**Board governance requirements:**

| Element                        | Requirement                                                                                                            | Applies to                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Audit committee responsibility | Audit committee (or equivalent) should be the ultimate recipient of serious disclosures where management is implicated | All organisations                                 |
| Whistleblowers' champion       | Non-executive director appointed; annual report to governing body                                                      | FCA/PRA SYSC 18 in-scope firms (mandatory)        |
| Annual whistleblowing report   | Summary of reports received; themes; programme effectiveness; champion's assessment                                    | FCA/PRA firms (mandatory); others (best practice) |
| Escalation protocol            | Clear documented path from Compliance/HR to board for high-risk disclosures                                            | All organisations                                 |
| Board culture                  | Board should actively signal that speaking up is valued and safe                                                       | All organisations                                 |
| Subsidiary oversight           | Parent company board should receive aggregate reporting from UK subsidiaries on whistleblowing activity                | Groups with SYSC 18 obligations                   |

**Escalation triggers requiring immediate board / audit committee notification:**

- Any allegation implicating a member of senior management or the board itself
- Any allegation that the FCA or PRA has already been notified directly by a worker
- Any allegation involving a potential criminal offence
- Any case where the investigator has identified a possible conflict of interest within
  Compliance or GC
- Any case where detriment has been suffered by a worker after a protected disclosure
  (immediate risk of s.47B claim)
- Any dismissal of a known or suspected whistleblower
- Any settlement agreement with a known or suspected whistleblower (especially if the
  SYSC 18 mandatory term has not been included for FCA/PRA firms)

---

#### Domain 7: Data Protection Interface (UK GDPR / DPA 2018)

**Key data protection obligations during whistleblowing investigations:**

| Obligation                     | Application                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lawful basis for processing    | Typically: legal obligation (ERs must investigate certain matters) or legitimate interests; document in ROPA                                                                                                                                         |
| Data minimisation              | Collect only what is necessary for the investigation; do not retain excessive personal data on respondents or witnesses                                                                                                                              |
| Access restriction             | Reporter's identity and investigation file accessible only to designated personnel; separated from HR / personnel files                                                                                                                              |
| Retention                      | No prescribed UK GDPR period for whistleblowing records; best practice — retain for the duration of any applicable limitation period (3 years from detriment / dismissal for tribunal claims [VERIFY current time limits]); then delete or anonymise |
| Subject Access Requests (SARs) | Respondent may submit a SAR for information held during an investigation; carefully balance against third-party rights (reporter confidentiality) — exemptions under DPA 2018 Sch.2 may apply [VERIFY]                                               |
| Anonymous reports              | Processing data from anonymous investigations is lawful but may reduce ability to use disciplinary findings if the reporter's identity cannot be established; document proportionality decision                                                      |
| International transfers        | If investigation materials are shared with overseas parent company, consider adequacy / IDTA requirements [VERIFY]                                                                                                                                   |

**⟁ CLARIFY** — Data protection:

- Has a Record of Processing Activities (ROPA) entry been created for the whistleblowing
  programme?
- Has a Data Protection Impact Assessment (DPIA) been conducted for the whistleblowing
  investigation process? (Required if processing is likely to result in high risk)
- What is the current retention schedule for closed investigation files?

---

#### Domain 7A: NHS Freedom to Speak Up (Overlay — NHS Trusts Only)

For NHS trusts and foundation trusts, the Freedom to Speak Up framework overlays PIDA:

**Freedom to Speak Up Guardian requirements:**

- Trusts and foundation trusts must appoint a FTSU Guardian
- Guardian must complete Foundation Level training (National Guardian's Office programme)
- Guardian must be registered with the National Guardian's Office (NGO)
- Reflective conversation with a mentor required within 6 months of appointment
- Quarterly reporting to the National Guardian's Office
- Annual refresh training requirement

**Scope:** The FTSU framework goes beyond formal PIDA whistleblowing to encompass any
concerns raised by staff, including clinical safety concerns, grievances, and suggestions
for improvement. Staff should feel able to raise issues without fear of detriment.

**Integration with PIDA:** FTSU Guardians often receive matters that constitute PIDA
protected disclosures. The trust must have a written policy that integrates FTSU and
PIDA frameworks without creating confusion about which route applies and what protections
flow from each.

---

### Step 6: Classify Gaps and Draft Remediation Roadmap

For each domain assessed in Step 5, assign a classification and remediation priority:

**Classification tiers:**

| Classification          | Definition                                                                                          | Default Priority       |
| ----------------------- | --------------------------------------------------------------------------------------------------- | ---------------------- |
| **COMPLIANT**           | Meets all applicable PIDA / SYSC 18 / NHS requirements                                              | No action required     |
| **PARTIAL**             | Gap exists but does not currently create material tribunal / regulatory exposure                    | NEAR-TERM              |
| **NON-COMPLIANT**       | Clear statutory or regulatory breach; tribunal claim or regulatory enforcement risk                 | NEAR-TERM to IMMEDIATE |
| **CRITICAL DEFICIENCY** | Material breach creating active tribunal exposure, FCA enforcement risk, or criminal liability risk | IMMEDIATE              |

**Remediation priority tiers:**

| Priority       | Timeframe   | Criteria                                                                                                        |
| -------------- | ----------- | --------------------------------------------------------------------------------------------------------------- |
| **IMMEDIATE**  | ≤ 30 days   | Active tribunal risk (known detriment post-disclosure); SYSC 18 breach; failure that may be reported to FCA/PRA |
| **NEAR-TERM**  | 30–90 days  | Policy gaps; investigation procedure deficiencies; training gaps; settlement agreement language absent          |
| **BACKGROUND** | 90–180 days | Best practice improvements; governance enhancements; third-party channel evaluation                             |

---

### Step 7: Policy Drafting — Minimum Required Elements

For new policy builds, draft the whistleblowing policy incorporating all of the following:

**Section 1 — Purpose and Commitment**

- Organisation's commitment to maintaining a speak-up culture
- Reference to PIDA 1998 and ERA 1996 Part IVA statutory protections
- Statement that protection applies from day one of engagement (no qualifying period)

**Section 2 — Who Is Covered**

- Extended worker definition explicitly stated (employees, contractors, agency workers,
  LLP members, trainees) — reference s.43K
- Post-termination detriment expressly included
- External applicants excluded (per _Sullivan_ [2024]) [VERIFY]

**Section 3 — What Is Covered (Qualifying Disclosures)**

- Six categories of relevant failure — use statutory language from s.43B(1)(a)-(f)
- Public interest requirement explained in accessible language
- Reasonable belief test explained — worker need not prove the concern is true

**Section 4 — How to Report (Reporting Channels)**

- Internal channel(s) described with contact details and availability
- Management of anonymous reports (if anonymous reporting is supported)
- External reporting rights — named prescribed persons including FCA/PRA where applicable
- Workers may report externally to FCA/PRA without first exhausting internal channels
  (for FCA/PRA firms, expressly stated per SYSC 18.3.4R)

**Section 5 — Confidentiality and Anonymity**

- Identity protection: who has access to the reporter's identity and on what basis
- Process for authorised identity disclosure
- What happens to anonymous reports

**Section 6 — Anti-Retaliation**

- List of specifically prohibited retaliatory acts
- Statement that retaliation by line managers, colleagues, or any worker is prohibited
- Personal liability of individual employees explicitly mentioned (deters retaliation)
- Process for reporting retaliation
- Reference to interim relief (s.128) if dismissed

**Section 7 — Investigation Process**

- Overview of investigation steps (without providing a tactical roadmap to respondents)
- Independence requirement
- Timeline commitments: acknowledgment within 7 days; update within 3 months (if consistent
  with SYSC 18 or EU Directive obligations applying to the organisation)
- Right to be accompanied at interview (statutory right; also good practice in investigations)

**Section 8 — Limitations of This Policy**

- This policy cannot be used to raise personal grievances (use the grievance procedure)
- Individuals making disclosures they know to be false are not protected
- Confidentiality obligations may not be used to prevent qualifying disclosures

**Section 9 — Settlement Agreements (FCA/PRA in-scope firms)**

- Any settlement or compromise agreement entered into by the organisation will include
  language preserving the worker's right to make a protected disclosure to the FCA, PRA,
  or other prescribed person — SYSC 18.3.7R
- For all employers: Any confidentiality clause in a settlement agreement that purports
  to prevent a qualifying disclosure is void and unenforceable — ERA 1996 s.43J

**Section 10 — Governance and Oversight**

- Who is responsible for the programme (CCO, GC, Audit Committee)
- For FCA/PRA firms: name/title of whistleblowers' champion
- Annual review commitment
- Training frequency and format

---

### Step 8: Employment Agreement and NDA Audit

Where employment agreements, compromise agreements, settlement agreements, or NDAs are
provided for review:

**Per-document audit checklist:**

```
Employment Agreement / NDA Whistleblowing Audit:

Void confidentiality language (s.43J ERA 1996):
☐ Does any confidentiality clause purport to prevent disclosure to an external regulator?
☐ Does any NDA include language requiring the worker to keep regulatory concerns
  confidential "in all circumstances"?
☐ Is there language purporting to prevent disclosure to police or law enforcement?
If any box checked: Mark clause as VOID — NON-COMPLIANT

Settlement agreement (compromise agreement) review:
☐ For FCA/PRA in-scope firms: Does the agreement contain the SYSC 18.3.7R mandatory
  term preserving the right to report to FCA/PRA?
If not: CRITICAL DEFICIENCY for FCA/PRA firms; NON-COMPLIANT for others
☐ Does the agreement contain an express acknowledgment that nothing in it prevents
  the worker from making a protected disclosure?
If not: PARTIAL — add standard savings clause

Protected conversations (s.111A(3) exception):
☐ Were pre-termination settlement discussions conducted in good faith?
☐ Is the worker a known or suspected whistleblower?
If yes: Settlement discussions are admissible in any s.103A or s.47B claim;
  advise that no "protected conversation" protection applies to this worker

Garden leave provisions:
☐ Does garden leave require maintaining confidentiality about disclosures made
  after the start of the garden leave period?
If yes: Clause likely void under s.43J if it covers qualifying disclosures
```

---

### Step 9: Quality Verification

Before delivering any analysis, run the Quality Assurance Framework checks.

1. Run the **5 Citation Quality Gates** silently. Revise any failure before delivery.
2. For every **CRITICAL DEFICIENCY** item, run the **3-pass Self-Interrogation**. If
   any pass reveals a weakness, revise the classification and rationale.
3. Assign a **Confidence Score** to each material analysis conclusion.
4. Verify completeness: all seven domains addressed (assessed or designed).
5. Generate the **Glass Box Audit Trail** and append to the output.

---

## Core Legal Frameworks

### Qualifying Disclosure — Checklist Application

Use this checklist for any specific situation requiring qualifying disclosure analysis:

```
Step 1 — Is there a "disclosure of information"?
☐ The communication provided factual content (not merely an allegation, opinion, or
  general complaint)
☐ The information was communicated to a specific person or entity

Step 2 — Does it fall within one or more of the six categories (s.43B(1))?
☐ (a) Criminal offence — suspected or likely
☐ (b) Breach of any legal obligation
☐ (c) Miscarriage of justice
☐ (d) Health/safety danger to any individual
☐ (e) Environmental damage
☐ (f) Deliberate concealment of any of the above

Step 3 — Reasonable belief test
☐ Worker reasonably believed (assessed on facts as understood by the worker) that
  the information tended to show the relevant failure
☐ Note: Worker need not be correct; honest, reasonable mistake is sufficient

Step 4 — Public interest test (post-ERRA 2013 s.17)
☐ Worker reasonably believed the disclosure was in the public interest
☐ Disclosure goes beyond the worker's purely personal contractual dispute?
  (Multiple workers affected; matter of regulatory concern; criminal conduct?)

Step 5 — Proper disclosure route (s.43C-43H)?
☐ Disclosed to employer (s.43C) — no conditions
☐ Disclosed to legal adviser in course of seeking advice (s.43D) — no conditions
☐ Disclosed to prescribed person (s.43F) — within that person's prescribed matters?
☐ Wider disclosure (s.43G) — four conditions met?
☐ Exceptionally serious failure (s.43H) — failure "exceptionally serious"?

Result:
→ All boxes checked: Protected disclosure — protections under s.47B and s.103A apply
→ Step 4 fails: Qualifying disclosure only if other indicia of public interest present;
  advise caution and verify with employment counsel
→ Step 5 fails: Qualifying disclosure may exist but not protected; consider whether
  the route can be corrected (new report through proper channel)
```

---

### Detriment and Dismissal Classification

| Risk Classification      | Definition                                                                                                       | Indicators                                                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL EXPOSURE**    | Active tribunal risk; potential award in excess of £100,000; regulatory enforcement risk                         | Dismissal of known whistleblower within 12 months of protected disclosure; detriment by senior manager aware of disclosure; SYSC 18 settlement breach |
| **HIGH RISK**            | Material tribunal risk; potential significant award                                                              | Adverse employment action within 3–12 months of protected disclosure; performance management of known whistleblower; exclusion from projects/meetings |
| **MODERATE RISK**        | Some tribunal risk; gap in documentation or process                                                              | Employment action that may be justifiable but poorly documented; proximate timing to disclosure; informal treatment changes                           |
| **LOW RISK / COMPLIANT** | Good documentation; independent business justification clear; disclosure not demonstrably connected to treatment | Employment action with clear prior justification; adequate performance process; disclosure remote in time                                             |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivery.

| Gate           | Rule                                                                                                                 | Fail Action                         |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every statutory claim cites a specific ERA 1996 section, case, or regulatory provision                               | Add citation or mark [UNVERIFIED]   |
| **Format**     | All citations use recognised format (ERA 1996 s.43B; _Jhuti_ [2019] UKSC 55; SYSC 18.4.1R)                           | Fix format                          |
| **Currency**   | Every cited provision checked for amendments; ERRA 2013 changes noted; SI 2025/604 Prescribed Persons update flagged | Flag [CHECK CURRENCY]               |
| **Domain**     | Analysis stays within England and Wales; Scotland/NI flagged separately where different                              | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; evolving case law areas flagged                                                       | Add confidence qualifier            |

### Self-Interrogation (CRITICAL DEFICIENCY items)

For every CRITICAL DEFICIENCY item, apply this 3-pass review before finalising:

**Pass 1 — Legal chain integrity**: Does the risk assessment follow logically from the
cited ERA 1996 provision or case law? Would an employment tribunal and/or FCA/PRA
actually reach this conclusion on these facts?

**Pass 2 — Completeness**: Have all relevant provisions been considered? Is there a
competing interpretation that reduces the severity? Have any recent EAT or Court of Appeal
decisions been missed?

**Pass 3 — Challenge**: What is the strongest argument for the employer? Under what
circumstances would a tribunal not make the most adverse finding?

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                       |
| ------------ | --------- | ------------------------------------------------ | -------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled statutory text; clear case law           | State with confidence                        |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions | State with brief caveat                      |
| **Probable** | 0.60–0.79 | Good arguments; may differ on facts              | State with reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends heavily on tribunal | Flag for professional review with both sides |
| **Unlikely** | 0.0–0.39  | Weak statutory basis; speculative                | Do not assert; flag [UNCERTAIN]              |

---

## Anti-Patterns Catalogue

What NOT to do when building, auditing, or advising on a UK whistleblowing programme:

1. **Treating PIDA as only applying to employees** — The s.43K extended definition covers
   contractors, agency workers, LLP members, trainees, and NHS practitioners. Policies
   drafted as "employee" policies miss these categories and create liability gaps.

2. **Applying the pre-2013 framework** — The Enterprise and Regulatory Reform Act 2013
   added the public interest requirement and removed good faith as a protection threshold.
   Policies or advice based on the pre-2013 PIDA framework (e.g., relying on _Parkins v
   Sodexho_ [2002] for pure employment contract grievances) are out of date.

3. **Confusing qualifying disclosure with protected disclosure** — A qualifying disclosure
   (correct content; reasonable belief; public interest) becomes a protected disclosure
   only if made through a proper route under ss.43C-43H. A disclosure to the wrong person
   or through an unauthorised channel may be a qualifying disclosure but not protected.

4. **Routing all reports through line management** — Having reports routed through the
   direct line manager of the reporter is a structural anti-pattern. Where the concern
   involves the line manager, this route is both useless and detriment-creating.

5. **Using settlement agreements to silence whistleblowers** — Any confidentiality clause
   preventing a qualifying disclosure is void under s.43J. Attempting to enforce such a
   clause, or including language designed to deter external reporting, creates additional
   liability exposure and, for FCA/PRA firms, regulatory enforcement risk.

6. **Failing to include the SYSC 18.3.7R mandatory term** — FCA/PRA in-scope firms that
   do not include the mandatory settlement agreement language preserving FCA/PRA reporting
   rights are in breach of SYSC 18. This is a NON-COMPLIANT to CRITICAL DEFICIENCY issue.

7. **Not applying the Jhuti principle** — Routing a dismissal decision through an
   "innocent" decision-maker unaware of the protected disclosure does not immunise the
   employer from s.103A liability if another person with knowledge of the disclosure
   manipulated events. Tribunals will look for the real reason.

8. **Treating the Kong separability principle as a broad escape route** — Kong permits
   dismissal for conduct genuinely distinct from the protected disclosure, but tribunals
   scrutinise separability claims. "Manner of raising concerns" is not a blanket defence.
   Over-relying on Kong in the face of clear retaliatory intent invites adverse findings.

9. **Failing to assess individual director liability** — Under s.47B(1A), individuals
   (directors, managers, co-workers) can be personally liable for detriment. _Osipov_
   [2023] resulted in £2 million personal awards against directors. Individual liability
   risk must be explicitly assessed and communicated to senior management.

10. **Omitting post-termination detriment from the scope** — PIDA protections do not end
    on termination. Giving a poor reference to a whistleblower, continuing harassment after
    departure, or making public statements about a former worker's protected disclosure
    can all constitute actionable detriment.

11. **Setting a 7-day interim relief clock running without awareness** — The s.128 interim
    relief application deadline is 7 days from the EDT. If an employer dismisses a
    whistleblower, the 7-day window is already running. Failure to monitor this risk and
    prepare for an interim relief hearing creates significant operational disruption.

12. **Ignoring the data protection interface** — Whistleblowing investigations involve
    personal data of reporters, respondents, and witnesses. The failure to have a lawful
    basis, retention policy, access restriction, and SAR exemption analysis for the
    investigation process is both a UK GDPR breach and a reputational risk.

13. **Using generic "legal privilege" labels without proper privilege analysis** — English
    law privilege for internal investigation materials (_Three Rivers_ [2004]) is narrower
    than US attorney-client privilege. Labelling investigation documents "privileged"
    without qualified legal advice on privilege architecture is false security.

14. **Failing to train line managers** — Most detriment is caused by line managers, not
    senior management. FCA SYSC 18 requires training at all levels. Absent training, the
    employer faces both the substantive detriment claim and reduced ability to argue lack
    of knowledge.

15. **Designing the programme around deterring reports** — Policies that use complex
    procedures, require multiple levels of approval before a report is accepted, or make
    the process feel risky for the reporter are counterproductive. They increase rather than
    decrease regulatory and tribunal exposure.

16. **Treating Scotland and Northern Ireland identically to England and Wales** — PIDA
    applies across the UK but through different tribunal systems and prosecution authorities.
    Scotland has COPFS; Northern Ireland has PONI and a distinct Order (Employment Rights
    (NI) Order 1996). Multinational UK employers need jurisdiction-specific legal advice
    for Scottish and NI employees.

17. **Neglecting NHS Freedom to Speak Up alongside PIDA** — NHS trusts that run a PIDA
    compliance programme without addressing Freedom to Speak Up Guardian requirements,
    NGO registration, and quarterly reporting are partially non-compliant with NHS
    England governance frameworks even if PIDA-compliant.

18. **Failing to monitor for post-disclosure detriment patterns** — A single adverse action
    may not establish detriment, but a pattern of small actions (reduced workload, social
    exclusion, minor performance criticisms) across a period following a protected disclosure
    can cumulatively establish detriment. Compliance monitoring should track employment
    actions involving known whistleblowers.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for: current ERA 1996 Part IVA text; ERRA 2013 amendments; current
  Prescribed Persons Order; FCA SYSC 18 handbook text; recent EAT/CA case law
- Save results to `/tmp/uk-whistleblower-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Confirm SI 2025/604 (HM Treasury as prescribed person) is in force and covers the
  relevant subject matter for the engagement

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural quality, workflow design, and gap classification; flag that all
  statutory text and case law requires independent verification before use

---

## Localization Notes

**Scotland:**

- Same PIDA statute (ERA 1996 Part IVA) applies but enforced through Scottish Employment
  Tribunal and, for criminal matters, Crown Office and Procurator Fiscal Service (COPFS)
- FCA/PRA SYSC 18 requirements apply equally to Scotland
- Prescription and limitation periods may differ from England and Wales [VERIFY under
  Prescription and Limitation (Scotland) Act 1984 as amended]
- Substantive employment law is UK-wide; procedural aspects of Scottish Employment Tribunal
  may differ in minor respects

**Northern Ireland:**

- The equivalent legislation is the Employment Rights (Northern Ireland) Order 1996
  (ERINO 1996) as amended by the Public Interest Disclosure (Northern Ireland) Order 1998
- Substantively equivalent to PIDA; parallel provisions apply
- Prosecution authority is the Public Prosecution Service NI (PPS NI)
- Separate tribunal system: Industrial Tribunal and Fair Employment Tribunal
- FCA/PRA SYSC 18 applies equally (UK-wide regulatory regime)

**Isle of Man / Channel Islands:**

- Separate jurisdictions; PIDA does not extend to the Crown Dependencies
- Each has its own employment rights legislation; flag for specialist local advice

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-uk-whistleblower-program-builder"
  mode: "Created from scratch — Mode A"
  topic: "UK Whistleblowing Programmes (PIDA 1998 / ERA 1996 Part IVA / FCA SYSC 18)"
  jurisdiction: "England and Wales (primary); Scotland and NI noted where relevant"
  engagement_mode: "[Build / Audit / Case risk assessment / NDA review / Board readiness / SYSC 18 review]"
  organisation_type: "[FCA/PRA regulated / NHS trust / General employer]"
  source_skills_analysed: "1 (legalcode-whistleblower-program-builder — general multi-jurisdiction)"
  enhancement_type: "UK jurisdiction-specific creation from research + general skill"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/uk-whistleblower-authority.md / Not created]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  domains_assessed:
    domain_1_policy_governance: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_2_worker_coverage: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_3_reporting_channels: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_4_investigation: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_5_detriment_dismissal: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_6_board_governance: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_7_data_protection: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
  critical_deficiencies:
    - "[Item / risk / ERA provision / case / remediation]"
  immediate_actions:
    - "[Action / responsibility / deadline]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "PIDA case law is rapidly developing; EAT and CA decisions post-Kong [2022] not all
      captured here — verify against current BAILII/WestLaw before relying"
    - "FCA SYSC 18 enforcement priorities evolve; confirm current FCA supervisory focus
      areas with FCA-experienced compliance counsel before use"
    - "NHS Freedom to Speak Up framework evolves through NGO guidance; confirm current
      Guardian training and registration requirements with National Guardian's Office"
    - "Scotland and Northern Ireland have distinct tribunal systems and, in NI, a distinct
      statutory instrument; jurisdiction-specific advice required"
    - "This skill does not assess the full multi-jurisdiction programme; for EU Directive
      2019/1937, US SOX/Dodd-Frank, or France Sapin II/Loi Waserman use
      legalcode-whistleblower-program-builder"
  reviewer:
    "AI-assisted — requires review by qualified solicitor/barrister experienced
    in UK employment law and, for FCA/PRA firms, FCA-experienced compliance counsel"
```

---

## Output Format Template

Use this template to structure the final deliverable for the user:

```markdown
# UK Whistleblowing Programme Assessment / Design

## [Organisation Name — redact if required]

## Date: [date]

## Engagement Mode: [Build / Audit / Case Risk / NDA Review / Board Readiness / SYSC 18]

---

## Executive Summary

**Overall Programme Status**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Critical Deficiencies**: [N items requiring immediate action]
**Near-Term Gaps**: [N items]
**For FCA/PRA Firms**: SYSC 18 Status: [COMPLIANT / NON-COMPLIANT]

**Top 3 Priorities:**

1. [Priority 1 — description, risk, and action]
2. [Priority 2 — description, risk, and action]
3. [Priority 3 — description, risk, and action]

---

## Domain-by-Domain Assessment

### Domain 1: Policy and Governance

**Status**: [Classification]
**Key findings**: [bullets]
**Remediation**: [specific actions; deadline]

### Domain 2: Worker Coverage and Qualifying Disclosure

**Status**: [Classification]
[...]

### Domain 3: Reporting Channel Architecture

**Status**: [Classification]
[...]

### Domain 4: Investigation Sequencing and Independence

**Status**: [Classification]
[...]

### Domain 5: Detriment and Dismissal Risk

**Status**: [Classification]
**Detriment risk level**: [CRITICAL EXPOSURE / HIGH RISK / MODERATE / LOW]
**Key case law applicable**: [Jhuti / Kong / Osipov — as relevant]
[...]

### Domain 6: Board Escalation and Governance

**Status**: [Classification]
[...]

### Domain 7: Data Protection Interface

**Status**: [Classification]
[...]

[Domain 7A: NHS Freedom to Speak Up — if applicable]

---

## Remediation Roadmap

### IMMEDIATE Actions (≤ 30 days)

| Action   | Owner  | Deadline | Risk if Not Done |
| -------- | ------ | -------- | ---------------- |
| [action] | [role] | [date]   | [risk]           |

### NEAR-TERM Actions (30–90 days)

| Action | Owner | Deadline | Risk if Not Done |
| ------ | ----- | -------- | ---------------- |

### BACKGROUND Actions (90–180 days)

| Action | Owner | Deadline | Risk if Not Done |
| ------ | ----- | -------- | ---------------- |

---

## [For NDA/Agreement Review] Agreement Audit Results

| Agreement / Provision | Issue | Classification | Recommended Action |
| --------------------- | ----- | -------------- | ------------------ |

---

## [For Case Risk Assessment] Detriment / Dismissal Risk Analysis

**Qualifying disclosure status**: [Yes / Possibly / No — with reasoning]
**Protected disclosure route**: [s.43C / s.43D / s.43F / s.43G / s.43H / Not protected]
**Detriment risk (s.47B)**: [CRITICAL EXPOSURE / HIGH / MODERATE / LOW]
**Auto-unfair dismissal risk (s.103A)**: [CRITICAL EXPOSURE / HIGH / MODERATE / LOW]
**Jhuti risk**: [Applicable / Not applicable — reasoning]
**Kong separability**: [Applicable as defence / Unlikely to apply — reasoning]
**Individual director/manager liability (s.47B(1A))**: [Named individuals at risk]
**Interim relief risk (s.128)**: [7-day window status; "pretty good" prospect assessment]
**Compensation exposure estimate**: [Range; note unlimited cap removal for s.103A]

---

## Confidence Notes

[Any areas of legal uncertainty; provisions marked [VERIFY]; recent case law developments
that may affect the analysis]

---

## Glass Box Audit Trail

[Insert YAML from template above, populated for this engagement]
```

---

## Provenance

Created by Legalcode (2026-03-22). Legalcode original synthesis. Built from deep research
on ERA 1996 Part IVA (PIDA 1998 as amended by ERRA 2013), FCA SYSC 18, PRA SS39/15, the
Prescribed Persons Order 2014 as amended to SI 2025/604, leading Employment Appeal Tribunal
and Supreme Court case law (_Jhuti_ [2019], _Kong_ [2022], _Sullivan_ [2024], _Osipov_
[2023]), and NHS Freedom to Speak Up framework. Informed by the general multi-jurisdiction
`legalcode-whistleblower-program-builder` scaffold and the England and Wales UK-specific
Legalcode skills library (`legalcode-uk-bribery-act-compliance`,
`legalcode-uk-fca-regulatory-compliance`, `legalcode-uk-employment-tribunal-claim`).
Jurisdiction-specific for England and Wales; Scotland and Northern Ireland noted where
they differ. Covers PIDA's full scope including s.43K worker definition, s.103A automatic
unfair dismissal, s.123A unlimited compensation, s.128 interim relief, and FCA SYSC 18
mandatory programme elements.
