---
name: legalcode-collective-bargaining-review
description: Review collective bargaining agreements (CBAs), labor relations matters, and works council
  procedures. Covers management rights clauses, grievance and arbitration procedures, seniority systems,
  wages and benefits provisions, work rules, union security, and no-strike/no-lockout provisions. Also
  covers works council (Betriebsrat) co-determination rights and Betriebsvereinbarungen under German BetrVG,
  and CSE information-consultation obligations and accords collectifs under French law. Use when reviewing,
  drafting, negotiating, or assessing compliance with a collective bargaining agreement, works agreement,
  or related labor relations document. Covers US NLRA (29 U.S.C. §§ 151-169), German Betriebsverfassungsgesetz
  (BetrVG) and Tarifvertragsgesetz (TVG), and French Code du travail (CSE consultation framework and collective
  agreement hierarchy). Flags legal risk, deviations from market standards, and procedural compliance
  gaps. Jurisdiction-aware with [JURISDICTION-SPECIFIC] markers for all three systems.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Collective Bargaining Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of collective
> bargaining agreements and labor relations documents. It does not constitute legal advice.
> All outputs must be reviewed by a qualified labor and employment law attorney licensed in the
> relevant jurisdiction before use. Labor law is highly jurisdiction-specific and subject to
> rapid change through NLRB decisions, court rulings, and legislative action. Statutory and
> case law references cited here carry hallucination risk — verify against authoritative sources
> before relying on them.

---

## Purpose and Scope

This skill reviews collective bargaining agreements (CBAs), works council agreements, and
related labor relations documents. It identifies legal risks, deviations from market standards,
procedural deficiencies, and compliance gaps, then produces a confidence-scored, auditable
analysis with actionable remediation recommendations.

**Covers:**

- Clause-by-clause review of CBAs (US NLRA), Betriebsvereinbarungen (Germany), and
  accords collectifs (France)
- Mandatory subjects of bargaining and ultra-vires clause detection
- Management rights analysis (scope, reserved-rights doctrine, waiver standards)
- Grievance and arbitration procedure review (Steelworkers standards, timelines, arbitrability)
- Seniority system analysis (competitive status, benefit, unit scope)
- Wages, benefits, and compensation structure review
- Work rules and progressive discipline (just cause/Daugherty seven tests)
- Union security provisions (post-Janus landscape, right-to-work overlay)
- No-strike/no-lockout clause analysis (Boys Markets enforceability)
- German BetrVG co-determination rights (§87 mandatory subjects, §99 hiring, §102 dismissals,
  §§111-112 social plan/Interessenausgleich)
- French CSE consultation obligations (L2312-17 three annual consultations, droit d'alerte)
- Successor employer obligations and §613a BGB / TUPE transfer analysis
- Social plan (Sozialplan) and plan de sauvegarde de l'emploi (PSE) compliance review

**Does not:**

- Draft new CBAs from scratch (see drafting-specific skills)
- Provide legal advice or replace qualified labor counsel
- Guarantee enforceability — all outputs require attorney review
- Cover public sector US labor relations (governed by state law and separate federal statutes,
  not the NLRA)

---

## Jurisdiction and Governing Law

This skill covers three distinct labor law systems:

| System                       | Primary Statute                                                            | Scope                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **US — NLRA**                | 29 U.S.C. §§ 151-169                                                       | Private sector employees only; excludes government workers, Railway Labor Act employees             |
| **Germany — BetrVG/TVG**     | Betriebsverfassungsgesetz (BetrVG); Tarifvertragsgesetz (TVG)              | All private sector establishments with 5+ employees; TVG for union-negotiated collective agreements |
| **France — Code du travail** | Code du travail Arts. L2221-1 to L2262-4 (CBAs); L2312-1 to L2312-71 (CSE) | All companies with 11+ employees (CSE threshold); collective agreements cover relevant industries   |

[JURISDICTION-SPECIFIC] When applying this skill, identify the governing legal system first.
Concepts do not translate directly: a US "no-strike clause" (Boys Markets injunction context)
is fundamentally different from a German Friedenspflicht or a French clause de paix sociale.
Do not import one system's doctrines into another.

[JURISDICTION-SPECIFIC] For US public sector CBAs, state law governs. Note jurisdiction and
apply the relevant state Public Employment Relations Act (PERA) or equivalent rather than
the NLRA framework.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The applicable legal system is unclear
- The user's side (management or union) would change the analysis
- Business context is needed to classify severity correctly
- Ambiguous provisions require user input to resolve

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

### Step 1: Accept the Document

Accept the CBA, Betriebsvereinbarung, accord collectif, or related labor relations document in:

- **File**: PDF, DOCX, or other format (use the `Read` tool)
- **Pasted text**: Document text pasted directly into the conversation
- **URL**: Link to a document system or CLM

If no document is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask:

1. **Jurisdiction and legal system**:
   - Options: US / NLRA, Germany / BetrVG + TVG, France / Code du travail + CSE, Multiple,
     Other (specify)
   - _Why this matters_: The entire analytical framework — mandatory subjects, enforceability
     rules, severity classification — depends on the governing legal system.

2. **Which side are you on?**
   - Options: Employer / Management, Union / Works Council, Neutral analysis (due diligence),
     Government / Regulatory compliance
   - _Why this matters_: A management-side review focuses on preserving operational flexibility;
     a union-side review focuses on protecting employee rights and contractual gains.

3. **Review purpose**:
   - Options: Negotiate new CBA / agreement, Review existing CBA before renewal, Post-execution
     compliance audit, Dispute resolution / grievance preparation, M&A due diligence
     (successor employer analysis), Other
   - _Why this matters_: A renewal negotiation review differs materially from a compliance
     audit or M&A successor analysis.

4. **Focus areas** (allow multiple selections):
   - Management rights and operational flexibility
   - Grievance and arbitration procedure integrity
   - Seniority and job security provisions
   - Wage and benefit cost analysis
   - No-strike/peace obligation enforceability
   - Union security / dues obligations
   - Works council co-determination compliance (DE)
   - CSE consultation obligations (FR)
   - Social plan / PSE compliance (DE/FR)
   - Successor employer obligations
   - No specific focus — full review

5. **Workplace context** (free text): Industry, workforce size, union/works council represented,
   any pending or anticipated organizational changes, recent labor disputes.

### Step 3: Load the Playbook (if available)

Check for the organization's labor relations playbook in local settings (e.g., `labor.local.md`
or similar configuration files). The playbook should define:

- **Standard positions** on key CBA provisions
- **Red lines** that cannot be conceded
- **Business priorities** (cost containment, operational flexibility, stability)

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found and ask:

- **Option A: Set up a playbook now** — Walk through key positions (management rights scope,
  grievance timeline preferences, just cause definition, no-strike enforcement approach, union
  security position). Time-consuming upfront but improves precision for this and future reviews.
- **Option B: Apply market standards** — Use widely accepted CBA standards as the baseline.
  Faster, but may not reflect this organization's specific risk tolerance.
- **Option C: Provide positions as we go** — Start the review and ask for positions when they
  become material for classification decisions.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the applicable legal system from Step 2. Use **legalcode-mcp** to gather
jurisdiction-relevant authority:

**For US / NLRA:**

- NLRB General Counsel memoranda (current GC positions on mandatory subjects, work rules)
- Recent NLRB decisions on management rights waiver standard (Endurance Environmental
  Solutions, 373 NLRB No. 141, Dec. 2024 — clear and unmistakable waiver standard)
- Current arbitration enforcement standards (Steelworkers Trilogy, Misco, W.R. Grace)
- Recent NLRB decisions on Stericycle work rule standard (Aug. 2023)
- Section 10(j) injunction standard (Starbucks Corp. v. McKinney, 2024)

**For Germany / BetrVG:**

- §87 BetrVG mandatory co-determination subject list (current 14 items including §87(1)(14)
  mobile work added by 2021 Modernization Act)
- BAG (Bundesarbeitsgericht) case law on co-determination scope
- Hinweisgeberschutzgesetz (HinSchG) July 2023 — whistleblower channel co-determination

**For France / Code du travail:**

- CSE consultation obligations (L2312-17 three-consultation framework)
- Post-Macron agreement hierarchy (Ordonnance n° 2017-1386)
- Loi n° 2023-1107 (partage de la valeur) requirements for 11-49 employee companies
- Recent Cour de cassation decisions on CSE consultation and agreement validity

Save results to `/tmp/legalcode-cba-authority.md` for use throughout the analysis.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general knowledge but explicitly flag that legal authority is unverified

### Step 5: Document-Level Assessment

Before diving into clause analysis, read the entire document and assess:

1. **Agreement type identification**: CBA (US), Betriebsvereinbarung (DE), Tarifvertrag (DE),
   Accord de branche / d'entreprise (FR), hybrid or multi-jurisdictional
2. **Coverage scope**: Which employees are covered, what bargaining unit is defined
3. **Term and expiration date**: How long is the agreement? When does it expire? Auto-renewal?
4. **Parties**: Employer, union(s), and any affiliates or related entities covered
5. **Successorship clause**: Is there a clause addressing business transfers?
6. **Integration / zipper clause**: Does it purport to be the complete agreement?
7. **Governing law / dispute resolution**: What law governs? Is there an arbitration clause?
8. **Effective date of most recent changes**: Flag outdated provisions that may not reflect
   current law (e.g., union security clauses not updated post-Janus)

**⟁ CLARIFY** — If the agreement appears to be multi-jurisdictional (e.g., a US/Canada frame-
work agreement, or a European Works Council agreement covering both DE and FR operations):

- Confirm which provisions are analyzed under which legal system
- Note that cross-border CBAs require specialist advice on each affected jurisdiction

---

## CBA Clause Analysis Reference

### Topic Coverage Architecture

This skill analyzes **12 core topic areas** for US CBAs and **8 additional areas** for
German/French instruments. Each topic is assessed using the COMPLIANT / PARTIAL / NON-COMPLIANT
classification system defined below.

| #   | Topic Area                     | US (NLRA) | DE (BetrVG) | FR (Code du travail) | Depth     |
| --- | ------------------------------ | --------- | ----------- | -------------------- | --------- |
| 1   | Management Rights              | ✓         | partial     | partial              | Deep      |
| 2   | Grievance & Arbitration        | ✓         | ✓           | ✓                    | Deep      |
| 3   | Seniority                      | ✓         | ✓           | partial              | Deep      |
| 4   | Wages & Benefits               | ✓         | ✓           | ✓                    | Deep      |
| 5   | Work Rules & Discipline        | ✓         | ✓           | ✓                    | Deep      |
| 6   | Union / Works Council Security | ✓         | ✓           | ✓                    | Deep      |
| 7   | No-Strike / Peace Obligation   | ✓         | ✓           | ✓                    | Deep      |
| 8   | Term, Renewal & Termination    | ✓         | ✓           | ✓                    | Standard  |
| 9   | Successorship & Transfer       | ✓         | ✓           | ✓                    | Standard  |
| 10  | Safety & Health                | ✓         | ✓           | ✓                    | Standard  |
| 11  | Non-Discrimination & EEO       | ✓         | partial     | partial              | Standard  |
| 12  | Miscellaneous / Boilerplate    | ✓         | ✓           | ✓                    | Standard  |
| 13  | Co-Determination Compliance    | —         | ✓           | —                    | Deep (DE) |
| 14  | CSE Consultation Compliance    | —         | —           | ✓                    | Deep (FR) |
| 15  | Social Plan / PSE Compliance   | —         | ✓           | ✓                    | Standard  |

---

### 1. Management Rights (US NLRA — Deep Analysis)

**Legal Framework:**

- Reserved-rights doctrine: management retains all rights not explicitly ceded in the CBA
- NLRB requires "very high specificity" before a management-rights clause establishes
  a clear and unmistakable waiver of union bargaining rights [VERIFY — Endurance
  Environmental Solutions, 373 NLRB No. 141 (2024) reinstated this standard]
- Mandatory subjects (§8(d)): wages, hours, terms and conditions of employment — cannot
  be unilaterally changed without bargaining, even where a management-rights clause purports
  to authorize it, unless language is sufficiently specific

**Key elements to review:**

- Scope of enumerated management rights (hire, fire, promote, demote, schedule, subcontract)
- Specificity of any waiver of union bargaining rights
- Language purporting to unilaterally change terms mid-contract
- Zipper clause interaction (does it purport to foreclose all mid-term bargaining?)
- Relationship between management rights and mandatory subjects

**Common issues:**

- Overly broad "all rights not expressly limited" language without specific enumeration;
  may not establish a clear and unmistakable waiver
- Purported management right to subcontract without bargaining over effects (violates
  First National Maintenance, 452 U.S. 666 (1981) as to effects bargaining)
- Management rights clause drafted to override seniority or progressive discipline
  protections already granted elsewhere in the CBA
- Unilateral change rights that ignore the clear and unmistakable waiver standard
  (reinstated in Endurance Environmental Solutions, 2024)

[JURISDICTION-SPECIFIC — DE/FR]: Germany does not have a "management rights" clause concept
in the same sense. Under BetrVG, employer prerogatives exist only where the works council's
§87 mandatory co-determination rights do NOT apply. In France, employer managerial authority
(pouvoir de direction) exists within the collective agreement and statutory framework.

---

### 2. Grievance and Arbitration Procedures (US NLRA — Deep Analysis)

**Legal Framework:**

- Steelworkers Trilogy (363 U.S. 564, 574, 593 (1960)): presumption favoring arbitration;
  courts must order arbitration absent clear exclusion; arbitrators have broad authority;
  courts enforce awards absent explicit public policy violation [VERIFY]
- United Paperworkers v. Misco, 484 U.S. 29 (1987): award overturned only if it violates
  "well defined and dominant" public policy ascertainable from law, not general considerations [VERIFY]
- W.R. Grace & Co. v. Local Union 759, 461 U.S. 757 (1983): public policy exception is narrow;
  seniority protections enforced over countervailing EEO concerns [VERIFY]
- Wright v. Universal Maritime Service Corp., 525 U.S. 70 (1998): waiver of statutory
  rights in arbitration must be "clear and unmistakable" [VERIFY]

**Key elements to review:**

- Number of grievance steps (typically 3-4) and whether they are realistic for the workplace
- Filing timelines: are they reasonable? (5-10 working days from event is standard)
- Definition of "grievance": Is it limited to CBA violations or broader?
- Selection and payment of arbitrator: joint selection, list services (AAA, FMCS), or
  permanent arbitrator panel
- Arbitral authority: Is it limited to CBA interpretation? Does it prohibit adding to,
  subtracting from, or modifying the CBA?
- Expedition provisions for termination cases (many CBAs require priority scheduling)
- Cost allocation (typically each party bears own counsel; arbitrator cost split equally)
- Arbitrability disputes: who decides? Courts under Steelworkers or arbitrator under
  broad clause?
- Whether statutory rights (Title VII, ADA, ADEA) are covered or excluded
- Waiver-by-inaction provisions: do they apply to grievances not timely processed?

**Common issues:**

- Filing windows shorter than 5 working days: excessive forfeiture of meritorious grievances
- "Grievance" defined to exclude unilateral changes: creates un-arbitrable disputes
- Missing provisions on arbitrator selection when parties cannot agree: deadlock risk
- Arbitral authority broader than CBA interpretation: allows arbitrators to effectively
  redraft the agreement
- No clarity on whether statutory discrimination claims are arbitrable: after Wright, a
  clear and unmistakable waiver is required to compel arbitration of statutory rights

**⟁ CLARIFY** — For grievance timelines shorter than 5 working days or broader-than-standard
arbitral authority:

- "The grievance filing window is [X] days, which is shorter than the 5-10 working day
  standard. Is this a known business preference, or should I flag it as a risk?"
- "The arbitral authority clause does not limit the arbitrator to CBA interpretation. Is this
  intentional, or should I flag it as a deviation?"

**German equivalent (Einigungsstelle):**
[JURISDICTION-SPECIFIC — DE] Disputes about co-determination matters under BetrVG §87 go to
the Einigungsstelle (conciliation board), not contractual arbitration. The Einigungsstelle's
decision is binding on both parties (BetrVG §76). Standard labor court (Arbeitsgericht) proceedings
handle individual employment disputes and collective agreement interpretation.

**French equivalent:**
[JURISDICTION-SPECIFIC — FR] Collective agreement disputes in France are adjudicated before
the Conseil de prud'hommes (individual disputes) or Tribunal judiciaire (collective disputes).
There is no mandatory arbitration tradition in French labor law; mediation (médiation
conventionnelle) is increasingly used but not compulsory.

---

### 3. Seniority Systems (US NLRA — Deep Analysis)

**Legal Framework:**

- Seniority is a mandatory subject of bargaining under §8(d) [VERIFY]
- Super-seniority for union officials is permissible if limited to layoff/recall and does
  not extend to all employment decisions (Dairylea Cooperative doctrine) [VERIFY]
- Seniority provisions interact with anti-discrimination obligations: facially neutral
  seniority systems with discriminatory intent may violate Title VII (American Tobacco,
  422 U.S. 405 (1975)); bona fide seniority systems are protected (§703(h)) [VERIFY]

**Key elements to review:**

- Seniority unit definition: plant-wide, department, occupational classification, or company-wide
- Which decisions are governed by seniority: promotions, transfers, layoffs, recall, shift
  preference, vacation scheduling
- Competitive status vs. benefit seniority: are they treated separately?
- Super-seniority: limited to layoff/recall or extended impermissibly to other decisions?
- Probationary period: length, rights during probation, conversion to seniority status
- Break-in-service rules: what events toll or terminate seniority accrual?
- Interplant transfer: does seniority carry over or reset?

**Common issues:**

- Overbroad super-seniority: extends to transfers, promotions, or discipline — creates
  Title VII disparate impact risk
- Undefined seniority unit causing inter-departmental disputes
- No recall rights for laid-off employees after defined period: significant retention risk
- Seniority list not maintained or regularly published: causes disputes

---

### 4. Wages, Benefits, and Compensation

**Legal Framework:**

- Wages and benefits are mandatory subjects of bargaining (§8(d)) [VERIFY]
- Successor employer obligations: a successor must recognize the union and bargain; may
  set initial terms before hiring from predecessor workforce but must bargain once majority
  is drawn from predecessor (Burns International, 406 U.S. 272 (1972)) [VERIFY]
- Past practice: established patterns of compensation not reflected in the CBA may become
  binding through past practice doctrine [VERIFY]

**Key elements to review:**

**Wages:**

- Base wage rates by classification: Are they current relative to market and statutory
  minimum wage [JURISDICTION-SPECIFIC]?
- Wage progression: automatic step increases, merit-based, or mixed?
- COLA (cost of living adjustment) provisions: tied to CPI/PPI index? Cap?
- Overtime pay: rate, eligibility, pyramiding restrictions
- Shift differentials: amount, triggering conditions, interaction with overtime
- Reporting pay (minimum compensation when called in): amount, conditions

**Benefits:**

- Health insurance: employer contribution formula, plan design changes, cost-sharing
- Pension / retirement: defined benefit vs. defined contribution; vesting schedule;
  multiemployer plan participation (ERISA Withdrawal Liability risks for multiemployer plans)
- Paid time off: vacation accrual schedule, sick leave, personal days, carryover rules
- Life and disability insurance: coverage amounts, employer vs. employee funding
- Supplemental unemployment benefits (SUB): trigger events, duration, amounts

**Common issues:**

- Health insurance cost-sharing formula that allows employer to pass all premium increases
  to employees without bargaining: creates unilateral change dispute risk
- Defined benefit pension underfunding disclosure obligations omitted: ERISA risk [VERIFY]
- Multiemployer plan withdrawal liability not addressed in successorship provisions:
  acquirer exposure in M&A context
- COLA caps below projected inflation resulting in real wage erosion over term

[JURISDICTION-SPECIFIC — DE]: Wages and benefits must comply with applicable Tarifvertrag
(collective agreement). If the company is bound by a Tarifvertrag through employer association
membership or Allgemeinverbindlicherklärung (universal declaration), individual employment
contracts or Betriebsvereinbarungen cannot derogate below TVG minimum standards
(Günstigkeitsprinzip — favorability principle) unless the Tarifvertrag itself contains an
opening clause (Öffnungsklausel).

[JURISDICTION-SPECIFIC — FR]: Post-Ordonnances Macron 2017, company-level accords d'entreprise
may derogate from sector accords de branche in most areas, except "ordre public social" minimums.
The Loi n° 2023-1107 (partage de la valeur) requires companies with 11-49 employees that have
been profitable for 3 consecutive years to implement a profit-sharing mechanism by January 2025.

---

### 5. Work Rules and Progressive Discipline

**Legal Framework:**

- Stericycle standard (NLRB, Aug. 2, 2023): workplace rules are presumptively unlawful if
  they have a "reasonable tendency to chill" §7 rights; employer must show legitimate,
  substantial interest not achievable by narrower rule, interpreted from perspective of
  economically dependent employee [VERIFY]
- Just cause standard: Daugherty/Enterprise Wire seven-test framework is the widely accepted
  arbitral standard [VERIFY]
- McLaren Macomb (NLRB, 2023): overly broad confidentiality and non-disparagement clauses
  in separation agreements violate §7 protected concerted activity [VERIFY]

**Key elements to review:**

**Work rules:**

- Attendance and punctuality rules: are they narrowly tailored and objective?
- Social media / electronic communications policy: does it restrict §7 protected
  concerted activity discussions of wages, hours, or working conditions?
- Confidentiality policy: does it impermissibly restrict disclosure of wages or
  protected concerted activity? (McLaren Macomb risk)
- Safety rules: are they clearly defined and consistently enforced?
- Standards of conduct: are prohibited acts specifically enumerated or impermissibly vague?

**Progressive discipline:**

- Does the agreement explicitly require progressive discipline (verbal warning → written
  warning → suspension → discharge) for non-egregious offenses?
- Are egregious offenses warranting immediate discharge specifically defined (violence,
  theft, drug/alcohol, safety violations, sexual harassment)?
- Grievance rights at each discipline step: are employees notified of right to union
  representation (Weingarten rights, 420 U.S. 251 (1975))?
- Discipline records: expungement provisions for prior disciplinary history after defined
  good-behavior period?

**Common issues:**

- Blanket "management discretion" discipline clauses without just cause protection
- Social media policies that restrict employee discussion of wages or working conditions
  (Stericycle risk)
- No Weingarten rights notice in disciplinary procedure sections
- "Last chance agreements" structured to eliminate all contractual grievance rights

[JURISDICTION-SPECIFIC — DE]: Under BetrVG §102, the works council must be notified and
consulted before any dismissal. Failure to properly notify the works council renders the
dismissal null and void. The works council may object to ordinary dismissals (§102(3))
within 3 working days (summary dismissal) or 1 week (ordinary dismissal), and if it objects
and the employer proceeds, the dismissed employee may seek reinstatement pending full
hearing. All disciplinary decisions affecting individual employees require works council
notification under §102.

[JURISDICTION-SPECIFIC — FR]: French labor law does not use the "just cause" concept directly.
Instead, termination must be for "cause réelle et sérieuse" (real and serious cause). The
procedure is strictly codified: entretien préalable (preliminary interview), notification of
dismissal by registered letter, observance of the notice period. Any procedural irregularity
entitles the employee to compensation (Articles L1232-1 to L1237-19 Code du travail).

---

### 6. Union Security and Dues Obligations

**Legal Framework (US):**

- **Private sector**: Union security clauses (agency shop, union shop) are permissible
  under §8(a)(3) NLRA subject to state right-to-work laws
- **Janus v. AFSCME, 138 S.Ct. 2448 (2018)**: Public sector employees cannot be compelled
  to pay agency fees; overruled Abood. DOES NOT APPLY to private sector [VERIFY]
- **Right-to-work states** (28 states): Union security clauses and agency fee arrangements
  are prohibited even for private employers [VERIFY]
- **Beck rights** (CWA v. Beck, 487 U.S. 735 (1988)): Non-union private sector employees
  in non-right-to-work states cannot be compelled to pay the portion of fees used for
  non-collective bargaining purposes [VERIFY]

**Key elements to review:**

- **Union shop vs. agency shop**: Does the clause require union membership or only fee
  payment? (Distinction matters post-Janus for public sector; for private sector, be sure
  to comply with applicable state right-to-work law)
- **Dues check-off**: Is there a dues deduction authorization from payroll? Is it revocable?
- **Grace period**: Is there a grace period for new employees before union security obligations
  attach? (30-day grace period required under §8(a)(3))
- **Beck financial disclosure**: Does the clause address non-member objectors' rights to
  financial disclosure and refund of non-representational expenditures?
- **Right-to-work law compliance**: Is the clause operative in all states where employees
  work? Flag if the CBA uses union security language without a right-to-work carve-out

**Common issues:**

- Union security clause with no right-to-work state carve-out: unenforceable in 28 states
- Agency fee clause in a public sector agreement post-Janus: facial §7 / First Amendment
  violation
- Dues check-off authorization without clear revocation procedure
- Beck financial disclosure rights omitted or buried in an attachment

[JURISDICTION-SPECIFIC — DE]: German law does not require union membership. The DGB union
federation and individual unions operate independently of any mandatory fee or dues structure.
Works council members are elected by all employees regardless of union membership. The
Betriebsrat is not a union and is governed exclusively by BetrVG.

[JURISDICTION-SPECIFIC — FR]: French unions derive representativeness from electoral thresholds
(8% nationally/in sector, 10% at company level), not from membership rates (which are typically
below 10%). The CSE is an elected body representing all employees regardless of union affiliation.
No employee can be required to join or pay dues to any union.

---

### 7. No-Strike / No-Lockout Provisions and Industrial Peace

**Legal Framework (US):**

- **Boys Markets, Inc. v. Retail Clerks Union, 398 U.S. 235 (1970)**: Federal courts may
  enjoin strikes in violation of no-strike clauses provided: (1) valid arbitration clause
  exists for the underlying dispute; (2) employer willing to arbitrate; (3) strike causing
  irreparable harm. This overrides the anti-injunction provisions of the Norris-LaGuardia
  Act [VERIFY]
- **Gateway Coal Co. v. United Mine Workers, 414 U.S. 368 (1974)**: Boys Markets
  injunctive relief extends to wildcat strikes not authorized by the union [VERIFY]
- **Sympathy strikes**: Not covered by a no-strike clause that addresses only "strikes
  against the employer" unless the clause explicitly covers sympathy action [VERIFY]

**Key elements to review:**

- **Scope of no-strike clause**: Does it cover sympathy strikes, work slowdowns, work-to-rule,
  picketing on employer premises, and secondary boycotts?
- **Mutual no-lockout obligation**: Is there a corresponding no-lockout provision protecting
  employees during the agreement term?
- **Safety exception**: Is there a carve-out allowing employees to refuse abnormally dangerous
  work (statutory right under OSHA and Gateway Coal)? [VERIFY]
- **Exceptions to no-strike**: What breaches by the employer, if any, revive strike rights?
  (Typically: failure to arbitrate, or employer conduct constituting a repudiatory breach)
- **Duration**: Does the no-strike clause extend past the agreement term? (Generally
  unenforceable for post-expiration conduct)

**Common issues:**

- No-strike clause without a corresponding no-lockout clause: unilaterally favorable to employer
- Sympathy strike carve-out absent: unclear whether sympathy action is prohibited
- No safety work-refusal carve-out: may interfere with statutory OSHA rights
- No-strike clause drafted to cover non-CBA-related disputes: overbroad; Boys Markets
  injunction unavailable if dispute is not arbitrable under the CBA

**⟁ CLARIFY** — For no-strike clauses without a no-lockout companion:

- "The no-strike clause has no corresponding no-lockout provision. Should this be classified
  as a material gap (PARTIAL) or a negotiation priority (NON-COMPLIANT for union side)?"

[JURISDICTION-SPECIFIC — DE (Friedenspflicht)]: Under the Tarifvertragsgesetz (TVG), a
collective agreement creates a mandatory industrial peace obligation (Friedenspflicht) for
its entire term. Both unions and employers are bound. Strikes to modify or challenge the
agreement are unlawful during the term. Strikes become permissible once the agreement
expires. The BAG has established that: rotating strikes (Wellenstreiks) are lawful; sympathy
strikes (Solidaritätsstreiks) are generally unlawful; occupation of premises is unlawful;
deliberate work slowdowns (Dienst nach Vorschrift) are lawful if arising from legitimate
work safety concerns. [VERIFY — BAG case law]

[JURISDICTION-SPECIFIC — FR]: French accords collectifs do not automatically contain a peace
obligation (clause de paix sociale). Such clauses can be negotiated but are uncommon. The
droit de grève (right to strike) is a constitutional right (Préambule de la Constitution de
1946). Strike rights cannot be contractually waived in French law. Any clause purporting to
prohibit strikes entirely is void as against constitutional right. Accords de méthode
(procedural agreements on negotiation process) are used to structure industrial relations
without restricting strike rights.

---

### 8. Term, Renewal, and Termination of Agreement

**Key elements to review:**

- **Agreement term**: Fixed term with specific expiration date; or rolling with notice
  requirement?
- **Automatic renewal (evergreen) clauses**: Notice windows for renewal opt-out; is the
  notice period reasonable?
- **Mid-term reopeners**: Are there provisions allowing either party to reopen specific
  subjects (wages, benefits) at defined intervals?
- **Continuation on expiration**: Does the CBA address status quo obligations after expiration
  pending negotiation of a successor agreement?

[JURISDICTION-SPECIFIC — US]: After CBA expiration, the duty to bargain continues and the
employer must maintain the status quo of all mandatory subjects until impasse is reached and
implemented [VERIFY — NLRB v. Katz, 369 U.S. 736 (1962)].

[JURISDICTION-SPECIFIC — DE]: Betriebsvereinbarungen continue in effect as "Nachwirkung"
(aftereffect) until superseded by a new agreement, unless the employer terminated the
agreement with proper notice. Tarifverträge also have Nachwirkung under TVG §4(5).

[JURISDICTION-SPECIFIC — FR]: Upon expiry of an accord d'entreprise, the agreement ceases
to have effect (unlike DE Nachwirkung) unless renewed. The employer must initiate
re-negotiation. Acquired advantages (avantages acquis) derived from the CBA do not automatically
persist unless they have become part of individual contracts.

---

### 9. Successorship and Business Transfer

**Legal Framework (US):**

- **Burns International, 406 U.S. 272 (1972)**: A "successor employer" that acquires
  substantially all assets and employs a majority of the predecessor's workforce must recognize
  the union and bargain [VERIFY]
- **Golden State Bottling, 414 U.S. 168 (1973)**: Successor with notice of predecessor's
  unfair labor practices inherits liability [VERIFY]
- **WARN Act** (29 U.S.C. §§ 2101-2109): 60-day notice required for plant closings and
  mass layoffs affecting 50+ employees [VERIFY]

[JURISDICTION-SPECIFIC — DE]: §613a BGB (implementing EU Directive 2001/23) provides automatic
transfer of all employees with preserved terms and conditions upon business transfer
(Betriebsübergang). Both transferor and transferee are jointly and severally liable for
obligations arising before the transfer. Employer must provide written notice to employees
before the transfer; employees have 1 month to object (retaining the right to employment
with the transferor if they object, where available). Dismissals solely caused by the transfer
are void (§613a(4) BGB).

[JURISDICTION-SPECIFIC — FR]: Business transfers (cession de fonds de commerce, fusion, apport
partiel d'actifs) trigger mandatory transfer of employment contracts under Article L1224-1 Code
du travail (implementing EU Directive 2001/23). CBA obligations may also transfer. CSE must be
informed and consulted before the transfer. Employees cannot individually waive transfer rights.

---

### 10. Safety, Health, and Working Conditions

**Key elements to review:**

- Joint labor-management safety committees: composition, meeting frequency, authority
- Incident reporting procedures and timelines
- Hazardous materials training and PPE obligations
- Employee right to refuse dangerous work: scope and procedure
- OSHA compliance obligations (US); BetrVG §87(1)(7) working time/safety (DE);
  CSE/CSSCT obligations (FR companies with 300+ employees)
- Return-to-work procedures after occupational injury

---

### 11. Non-Discrimination, EEO, and Accommodation

**Key elements to review:**

- Non-discrimination clause: does it track current protected classes under applicable law
  [JURISDICTION-SPECIFIC]?
- Reasonable accommodation procedures for disability and religion
- Pregnancy and parental leave interaction with CBA benefits
- Harassment and investigation procedures: do they satisfy Stericycle work-rule standard?
- Seniority system interaction with non-discrimination obligations (check for facially
  neutral but discriminatory impact)

---

### 12. Miscellaneous / Boilerplate

**Key elements to review:**

- Entire agreement / integration clause: interaction with past practice doctrine
- Severability: does it address continuity of remaining provisions if one clause is
  invalidated?
- Amendment procedure: written consent of both parties required?
- Waiver: is there a standard non-waiver clause?
- Successor binding clause: does the CBA bind successors and assigns?
- Notice provision: addresses, delivery method, effective date

---

### 13. German BetrVG Co-Determination Compliance (Deep Analysis — DE Only)

**§87 BetrVG — Mandatory Co-Determination Subjects**

The following 14 subjects require the works council's mandatory co-determination before the
employer may implement changes. Any employer action in these areas without works council
agreement (or Einigungsstelle decision) is null and void:

| §          | Subject                                                   | Key Issues                                                          |
| ---------- | --------------------------------------------------------- | ------------------------------------------------------------------- |
| §87(1)(1)  | Works order / employee conduct                            | Social rules, dress codes, AI-assisted selection guidelines         |
| §87(1)(2)  | Start/end of working time                                 | Daily and weekly hours, shift start/end times                       |
| §87(1)(3)  | Temporary reduction/extension of hours                    | Short-time work, overtime rosters                                   |
| §87(1)(4)  | Timing and form of wage/salary payment                    | Payment method, payroll timing                                      |
| §87(1)(5)  | Holiday/vacation scheduling principles                    | Vacation calendar, vacation precedence rules                        |
| §87(1)(6)  | Technical surveillance equipment                          | CCTV, monitoring software, AI-powered tracking                      |
| §87(1)(7)  | Occupational health and safety                            | OSH measures within statutory framework                             |
| §87(1)(8)  | Form, structure, and administration of welfare facilities | Canteen, showers, recreation                                        |
| §87(1)(9)  | Allocation of housing by employer                         | Employee housing policies                                           |
| §87(1)(10) | Remuneration principles                                   | Pay structure, performance criteria, bonus methodology              |
| §87(1)(11) | Employee performance-linked pay                           | Piecework rates, premium pay                                        |
| §87(1)(12) | Holiday pay                                               | Method of calculation                                               |
| §87(1)(13) | Suggestion schemes / innovation rewards                   | Employee suggestion box procedures                                  |
| §87(1)(14) | Mobile work (remote/hybrid)                               | Conditions of information-technology-based mobile work (added 2021) |

**Common Co-Determination Compliance Issues:**

- Unilateral introduction of remote work policies without §87(1)(14) works council agreement
- AI-powered monitoring or selection tools deployed without §87(1)(6) co-determination
- Bonus scheme modifications implemented without §87(1)(10) consultation
- Shift schedule changes issued as management directive without §87(1)(2) agreement

**§§99-101 BetrVG — Individual Personnel Decisions**

Employer must give works council prior notification for:

- Recruitment of new employees (§99(1))
- Classification into pay grade or group (§99(1))
- Transfer within the establishment (§99(1))
- Promotion (§99(1))

Works council may withhold consent in defined circumstances (§99(2)). If employer proceeds
without consent, the works council may apply to the Labor Court for annulment of the measure (§101).

**§102 BetrVG — Dismissals**

- Employer must notify works council and hear its opinion before any dismissal
- Response period: 3 working days (summary/extraordinary dismissal); 1 week (ordinary dismissal)
- Works council may object to ordinary dismissal on grounds listed in §102(3)
- Failure to notify = dismissal null and void (§102(1) sentence 3)
- Hinweisgeberschutzgesetz (HinSchG, July 2, 2023): works council co-determination rights apply
  to design and implementation of whistleblower reporting offices (technical equipment under
  §87(1)(6))

**§§111-113 BetrVG — Betriebsänderung, Interessenausgleich, Sozialplan**

Applicable when the employer plans a material change to the business (Betriebsänderung):

- Closure or relocation of the whole or substantial part of the establishment
- Merger or split of establishments
- Fundamental changes in work organization
- Introduction of substantially new working methods or production processes affecting
  more than 1/5 of the workforce or more than 50 employees (§111 sentence 2)

**Process:**

1. Employer must attempt to negotiate an **Interessenausgleich** (interest agreement)
   naming affected employees — not legally enforceable, but employer is liable for
   failure to attempt it in good faith (§113 compensation obligation)
2. Employer must attempt to negotiate a **Sozialplan** (social plan) compensating
   for economic hardship — legally enforceable and mandatory
3. If no agreement reached, either party may refer to the **Einigungsstelle** (conciliation
   board), which issues a binding decision

**Namensliste** (named employee list): If Interessenausgleich names specific employees for
dismissal, those employees bear the burden of rebutting the presumption that the dismissal
is operationally necessary (§1(5) KSchG).

---

### 14. French CSE Consultation Compliance (Deep Analysis — FR Only)

**Three Mandatory Annual Consultations (Art. L2312-17 Code du travail):**

| Consultation                                      | Scope                                                                         | Timing                                     | Key Documents                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| **Strategic orientations**                        | Company's long-term strategy, business model, planned investments/divestments | Annually (or up to 3-year cycle if agreed) | Strategic plan, investment forecasts                          |
| **Economic and financial situation**              | Annual accounts, forecasted performance, market conditions                    | When annual accounts presented             | Audited accounts, financial projections                       |
| **Social policy, working conditions, employment** | HR policy, safety measures, training, compensation                            | Annually                                   | Bilan social (companies 300+), training plan, BDES/BDESE data |

**Droit d'Alerte Économique (Arts. L2312-63 to L2312-69):**

- CSE may trigger alert procedure when it becomes aware of facts that could jeopardize
  the company's economic situation
- Phase 1: Request employer explanation within defined period
- Phase 2: If response inadequate, CSE establishes report; may engage expert accountant
- Phase 3: Escalate to statutory auditor and, if necessary, labor authorities
- Employer failure to respond = obstruction of justice (délit d'entrave)

**Ad Hoc / Project-Specific Consultations:**

- All planned economic decisions with potential impact on employment or working conditions
  require prior CSE consultation: restructurings, M&A, outsourcing, significant changes to
  employment policies
- "Prior" means before the decision is implemented — not simultaneous or post-hoc

**Common CSE Compliance Issues:**

- Informing/consulting CSE after, not before, the decision is effectively made (délit
  d'entrave; penalties: criminal fines, transaction voiding risk)
- BDESE/BDES (information database) not maintained or not updated timely
- Failing to engage expert agreed upon by CSE within required timeframe
- Bypassing CSE for restructuring decisions by structuring as "operational changes" below
  the PSE threshold

**CSSCT (Commission Santé, Sécurité et Conditions de Travail):**

- Mandatory in establishments with 300+ employees (or as required by sector agreement)
- Cannot engage external experts independently (unlike main CSE)
- Reviews occupational safety, workplace conditions, accident investigations

**Plan de Sauvegarde de l'Emploi (PSE):**

Triggered when a company with 50+ employees intends to make 10+ economic dismissals over
30 days. Two paths:

| Path                        | Description                                        | CSE Role                                                    |
| --------------------------- | -------------------------------------------------- | ----------------------------------------------------------- |
| **Négocié** (negotiated)    | PSE agreed by majority unions or CSE (if no union) | CSE votes on agreement; majority required                   |
| **Unilatéral** (unilateral) | Employer drafts and submits for DREETS validation  | CSE consulted twice; opinions attached to DREETS submission |

Administrative validation by DREETS is mandatory for both paths. DREETS examines:

- Proportionality of employment measures to company resources
- Adequacy of reclassement (job search/retraining support) measures
- Procedural compliance with CSE consultation obligations

---

## Severity Classification System

### Classification: COMPLIANT / PARTIAL / NON-COMPLIANT

| Level             | Definition                                                                                           | Action Required                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **COMPLIANT**     | Provision meets or exceeds applicable legal requirements and market standards; no action required    | Note for awareness                                        |
| **PARTIAL**       | Provision partially addresses requirements; gap exists but risk is manageable with minor remediation | Specific remediation recommended; flag for negotiation    |
| **NON-COMPLIANT** | Provision violates legal requirements, creates material risk, or is unenforceable as drafted         | Immediate remediation required; escalate to legal counsel |

### Automatic NON-COMPLIANT Triggers

Flag immediately as NON-COMPLIANT regardless of context:

| Trigger                                                                                    | Jurisdiction | Statutory Basis                        |
| ------------------------------------------------------------------------------------------ | ------------ | -------------------------------------- |
| Union security clause requiring fee payment in right-to-work state                         | US           | State right-to-work law                |
| Public sector agency fee clause                                                            | US           | Janus v. AFSCME, 138 S.Ct. 2448 (2018) |
| Work rule that explicitly restricts discussion of wages/working conditions among employees | US           | §7 NLRA; Stericycle (2023)             |
| Dismissal without §102 BetrVG works council notification                                   | DE           | §102(1) sentence 3 BetrVG              |
| §87 co-determination subject implemented without works council agreement                   | DE           | §87(1) BetrVG                          |
| CSE not consulted before decision with employment impact                                   | FR           | Art. L2312-17 + délit d'entrave        |
| PSE implemented without DREETS validation                                                  | FR           | Art. L1233-61 Code du travail          |
| No-strike clause that purports to ban constitutionally protected strike rights             | FR           | Préambule de la Constitution de 1946   |

---

## Step 6: Conduct Full Clause Analysis

Using the Clause Analysis Reference above, analyze each applicable topic area systematically.
For each topic:

1. **Identify the provision** (quote or summarize the relevant clause)
2. **Apply the classification** (COMPLIANT / PARTIAL / NON-COMPLIANT) using the severity
   classification system
3. **State the legal basis** for the classification (cite statute or case law; mark [VERIFY]
   if not confirmed against primary sources)
4. **Identify the issue** specifically and concisely
5. **Propose remediation** (specific alternative language, procedural fix, or negotiation approach)

**⟁ CLARIFY** — For borderline PARTIAL/NON-COMPLIANT classifications where reasonable minds
could differ based on the organization's risk tolerance:

- "This management-rights clause is broad but not unprecedented. Should I classify it as
  PARTIAL (flag for negotiation) or NON-COMPLIANT (escalate for immediate redrafting)?"
- "The grievance filing window is 4 working days, which is below the 5-day standard but
  not obviously unlawful. Should this be PARTIAL or COMPLIANT given your timeline preferences?"

---

## Step 7: Missing Provision Detection

After analyzing all present provisions, check for important clauses that are entirely absent.
A missing mandatory provision can be as significant as a defective one.

| Missing Provision                          | Jurisdictions | Risk Level                                                              |
| ------------------------------------------ | ------------- | ----------------------------------------------------------------------- |
| No no-strike clause                        | US            | Management loses Boys Markets injunction remedy                         |
| No just cause standard for discipline      | US            | Employer may have unconstrained discharge; arbitrability disputes       |
| No grievance arbitration clause            | US            | Disputes default to litigation (§301 suit)                              |
| No §102 BetrVG notification procedure      | DE            | Any dismissal is potentially null and void                              |
| No Sozialplan obligation for restructuring | DE            | Conciliation board may order one in any case; employer exposed          |
| No CSE consultation calendar               | FR            | Risk of délit d'entrave for any major decision                          |
| No BDESE / BDES maintenance obligation     | FR            | CSE cannot fulfil consultation role; creates annual compliance exposure |
| No successorship clause                    | All           | Successor employer status and obligations are uncertain                 |
| No WARN Act notice procedure               | US            | 60-day statutory obligation runs regardless                             |

---

## Step 8: Develop Remediation Recommendations

For each NON-COMPLIANT finding, produce:

1. **Specific redline / alternative language** (exact contractual language that resolves the issue)
2. **Fallback position** (minimum acceptable language if counterparty resists full remediation)
3. **Exposure estimate** (potential legal/financial exposure if issue is not remediated)
4. **Urgency** (immediate / next renewal / long-term)

For each PARTIAL finding, produce:

1. **Specific gap identified**
2. **Recommended addition or modification**
3. **Business impact** of accepting vs. remediating

---

## Step 9: Priority Framework

Prioritize findings using this three-tier system:

| Tier       | Label                       | Criteria                                                                                                              | Action                                                                   |
| ---------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Tier 1** | Critical — Immediate        | NON-COMPLIANT findings involving statutory violations, facial unenforceability, or immediate litigation exposure      | Escalate to counsel immediately; do not execute/implement until resolved |
| **Tier 2** | Material — Next Negotiation | PARTIAL findings that create meaningful risk and should be addressed in the next CBA negotiation or agreement renewal | Include in negotiation priorities; brief business stakeholders           |
| **Tier 3** | Informational — Monitor     | COMPLIANT findings worth monitoring; minor PARTIAL findings that can be addressed opportunistically                   | Add to tracking log; address if opportunity arises                       |

**⟁ CLARIFY** — If there are many Tier 2 findings and not all can be pursued in a single
negotiation:

- "I've identified [N] Tier 2 items. Do you want me to further prioritize these by business
  impact (operational flexibility, financial exposure, workforce relations), or should all
  Tier 2 items be presented to the negotiating team equally?"

---

## Step 10: Quality Verification

Before delivering the analysis, run these quality checks:

1. Run the **5 Citation Quality Gates** silently. Revise any failures before delivery.
2. For every **NON-COMPLIANT** finding, apply the **3-pass Self-Interrogation**.
3. Assign a **Confidence Score** to each material finding.
4. Verify all 15 topic areas have been addressed (or explicitly noted as not applicable).
5. Generate the **Glass Box Audit Trail** and append it to the output.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                    | Fail Action                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Source**     | Every legal classification cites a specific statute, NLRB decision, BAG decision, Code du travail article, or established arbitral principle            | Add citation or mark "[UNVERIFIED]"       |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                                             | Fix format                                |
| **Currency**   | Every cited provision checked for amendments, repeal, or supersession (especially post-2022 NLRB developments; 2021 BetrVG amendments; 2023 French loi) | Flag "[CHECK CURRENCY]"                   |
| **Domain**     | Analysis stays within the applicable jurisdiction's legal framework; no cross-jurisdictional bleed                                                      | Remove or flag cross-system contamination |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                                                               | Add confidence qualifier                  |

### Self-Interrogation for NON-COMPLIANT Findings

For every NON-COMPLIANT classification, apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the NON-COMPLIANT classification follow logically
from the cited authority? Would a labor arbitrator or court actually reach this conclusion?
Is there a strong counterargument (e.g., contextual interpretation, industry custom,
past practice) that could change the outcome?

**Pass 2 — Completeness**: Have all relevant statutes, NLRB decisions, BAG decisions, and
Code du travail provisions been considered? Are there labor relations dimensions (successor
obligations, multi-employer unit issues, multi-jurisdiction application) not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this provision is in fact
COMPLIANT or only PARTIAL? Under what circumstances (industry, deal context, workforce
composition) might a reasonable labor attorney accept this provision without change?

### Confidence Scoring

| Level        | Range     | Meaning                                             | Action                                     |
| ------------ | --------- | --------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95-1.0  | Settled statutory text or NLRB/BAG bright-line rule | State with confidence                      |
| **High**     | 0.80-0.94 | Strong authority; minor interpretive questions      | State with brief caveat                    |
| **Probable** | 0.60-0.79 | Good arguments; reasonable contrary view exists     | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain; fact-specific                  | Flag for qualified labor counsel review    |
| **Unlikely** | 0.0-0.39  | Speculative; no firm authority                      | Do not assert; flag "[UNCERTAIN]"          |

---

## Glass Box Audit Trail

Include this YAML block at the end of every analysis:

```yaml
glass_box:
  skill_name: "legalcode-collective-bargaining-review"
  jurisdiction: "[US-NLRA / DE-BetrVG / FR-Code du travail / multiple]"
  agreement_type: "[CBA / Betriebsvereinbarung / accord collectif / other]"
  document_name: "[agreement name or 'Unnamed']"
  review_purpose: "[negotiation / compliance audit / M&A due diligence / dispute / other]"
  party_side: "[management / union-works council / neutral]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-cba-authority.md / Not created]"
  topics_analyzed: "[number of topics assessed]"
  compliant_findings: "[count]"
  partial_findings: "[count]"
  non_compliant_findings: "[count]"
  missing_provisions_flagged: "[count]"
  tier_1_critical: "[count]"
  tier_2_material: "[count]"
  tier_3_informational: "[count]"
  citations_verified: "[number VERIFIED] / [number marked VERIFY]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Scope limitations: e.g., only US NLRA analysis conducted]"
    - "[If legalcode-mcp not connected: legal authority unverified]"
    - "[Any assumptions made about applicable law]"
  reviewer: "AI-assisted — requires qualified labor and employment law attorney review"
```

---

## Anti-Patterns

What NOT to do when reviewing or drafting collective bargaining agreements:

1. **Overly broad management rights as a waiver substitute**: Drafting a general "all rights
   not expressly limited" clause and relying on it to justify unilateral changes. The NLRB's
   reinstated "clear and unmistakable waiver" standard (Endurance Environmental Solutions, 2024)
   requires high specificity; vague language will not establish a waiver of mandatory subjects.

2. **Ignoring the clear and unmistakable waiver standard post-2024**: Using pre-2024 "contract
   coverage" standard arguments after Endurance Environmental Solutions reinstated the stricter
   standard. Employers who relied on this post-2020 development must re-examine their CBA provisions.

3. **Agency fee clauses in public sector agreements**: Including agency fee or union security
   language in public sector CBAs after Janus v. AFSCME (2018) without updating to reflect that
   public employees cannot be compelled to pay any fees.

4. **Union security clauses without right-to-work carve-outs**: Applying union shop or agency
   shop language uniformly without recognizing that such provisions are void in 28 right-to-work
   states for private sector employers.

5. **Work rule policies that restrict §7 activity**: Social media policies, confidentiality
   rules, or non-disparagement clauses in employment agreements that prevent employees from
   discussing wages, hours, or working conditions with coworkers or unions. After Stericycle
   (2023), even facially neutral rules are presumptively unlawful if they could chill protected
   concerted activity.

6. **Grievance timelines that guarantee forfeiture**: Filing windows of 3 days or fewer for
   grievances, combined with strict waiver-by-inaction clauses, result in forfeiture of
   meritorious grievances on procedural grounds and create workforce morale problems.

7. **Arbitral authority clause without clear limits**: Permitting arbitrators to "modify" or
   "supplement" the CBA beyond interpretation opens the agreement to quasi-legislative rewriting
   by arbitrators. The Steelworkers standard authorizes broad interpretation, not amendment.

8. **Past practice incorporation by accident**: Including integration/zipper clauses that purport
   to supersede all past practices without specifically identifying which practices are terminated
   — and then failing to notify the union and bargain over the termination of those practices.
   Unilateral elimination of established past practices is an unfair labor practice.

9. **§87 BetrVG implementation without works council agreement**: German employers who introduce
   remote work policies, monitoring technology, AI-based tools, or revised working time without
   obtaining works council co-determination under the applicable §87(1) subsection risk having
   the measure declared null and void by the Arbeitsgericht.

10. **Missing §102 BetrVG dismissal procedure**: Failing to notify and consult the works council
    before any dismissal renders the dismissal null and void as a matter of German law, regardless
    of the substantive merits of the dismissal. This is non-negotiable and cannot be cured after the
    fact.

11. **Post-hoc CSE consultation in France**: Informing or consulting the CSE after the employer has
    effectively decided to restructure, close a site, or outsource functions. French courts and
    DREETS consistently invalidate decisions made before the legally required prior consultation
    (information-consultation préalable). This constitutes a délit d'entrave (obstruction offense),
    subject to criminal fines.

12. **Ignoring Friedenspflicht expiry in German CBAs**: Treating a Tarifvertrag as providing
    indefinite strike protection. Once the peace obligation expires at the end of the agreement
    term, strike action becomes lawful immediately. Employers who have not yet concluded a new
    agreement should plan accordingly.

13. **Assuming French accords d'entreprise can always derogate from sector agreements**: Post-2017
    Macron reforms permit company-level deviation in most areas, but "ordre public social" minimums
    remain inviolable. Accords d'entreprise that derogate below statutory minimum protections
    (SMIC, paid leave minimums, occupational health obligations) are partially or wholly void.

14. **Ignoring successor employer obligations in M&A**: Treating a CBA as if it automatically
    terminates on asset sale. Under US successor employer doctrine (Burns International), the
    successor must recognize and bargain with the union once a majority of the workforce is drawn
    from the predecessor. Under DE §613a BGB and FR L1224-1, employment contracts and their
    terms transfer automatically.

15. **Super-seniority for non-layoff/recall decisions**: Granting union officials super-seniority
    extending beyond layoff and recall (e.g., for transfers, job bidding, or shift assignment) is
    potentially unlawful discrimination under Title VII (disparate treatment) and may violate the
    NLRA's prohibition on discriminating against non-union employees in employment decisions.

16. **No Boys Markets analysis for no-strike clause**: Drafting a no-strike clause without confirming
    that all disputes it covers are also subject to the grievance arbitration procedure. Boys Markets
    injunctive relief is only available when the strike violates a no-strike clause AND the underlying
    dispute is arbitrable. A no-strike clause that covers non-arbitrable disputes provides no
    injunctive remedy.

17. **Conflating German Betriebsrat and French CSE roles**: These are fundamentally different
    institutions. The Betriebsrat has judicially enforceable co-determination rights (Mitbestimmung)
    that can block employer action; the CSE has information and consultation rights, but the employer
    may proceed after consultation (albeit with délit d'entrave risk if procedure is violated). Applying
    the co-determination paradigm to French CSE obligations, or the consultation paradigm to German
    works council rights, produces incorrect legal analysis.

---

## Writing Standards

Before delivering any output under this skill:

- [ ] **Jurisdiction clarity**: Every finding identifies the applicable legal system and statute.
      Never use a US NLRA citation in a German BetrVG analysis or vice versa.
- [ ] **Active, imperative language**: Use "Flag this provision" not "This provision might
      potentially be worth flagging." Be direct.
- [ ] **No false certainty**: Mark [VERIFY] for any statutory reference not confirmed against
      primary sources. Do not state contested positions as settled law.
- [ ] **Specific citations**: Reference specific NLRB decision names and years, specific BetrVG
      subsections (e.g., §87(1)(6), not just "§87"), specific Code du travail articles
      (e.g., Art. L2312-63, not just "French labor law").
- [ ] **Actionable remediation**: Every PARTIAL and NON-COMPLIANT finding concludes with
      specific proposed language or a concrete remediation step.
- [ ] **No unnecessary jargon**: Explain terms of art on first use: "Betriebsvereinbarung
      (works agreement — a binding agreement between employer and works council)."
- [ ] **Proportionate depth**: Deep analysis for the 7 deep topics; standard checklist for
      the 8 standard topics. Do not reverse this.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current NLRB decisions, BAG rulings, and Code du travail
  articles relevant to the specific CBA provisions being reviewed
- Save verified results to `/tmp/legalcode-cba-authority.md`
- Mark citations sourced from legalcode-mcp as VERIFIED in the Glass Box audit trail
- Use verified authority to replace [VERIFY] markers throughout the analysis

**Without legalcode-mcp:**

- Proceed using general knowledge and the research embedded in this skill
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require verification"`
- Advise user to verify any material legal citation against the NLRB website,
  Gesetze-im-Internet.de, or Légifrance before relying on it

---

## Localization Notes

This skill covers three legal systems. When working with only one system:

**US only**: Skip sections 13 (BetrVG Co-Determination) and 14 (CSE Consultation). The
15-topic architecture reduces to 12 US-specific topics.

**Germany only**: The NLRA analysis sections do not apply. Focus on BetrVG co-determination,
Tarifvertrag structure, Günstigkeitsprinzip, and §613a BGB successor obligations. Include
§§111-113 Sozialplan analysis for any restructuring context.

**France only**: The NLRA and BetrVG sections do not apply. Focus on CSE consultation
obligations, accord collectif hierarchy (branch vs. company), Macron 2017 derogation
framework, and L1224-1 business transfer analysis. Include PSE analysis for any restructuring
context.

**Multi-jurisdictional**: Clearly label each finding with its governing legal system. Do not
blend analysis — a no-strike finding under French law (constitutionally limited) is
fundamentally different from a US Boys Markets analysis.

---

## Output Format Template

```markdown
# Collective Bargaining Agreement Review

## [Agreement Name] — [Date of Review]

**Jurisdiction:** [US-NLRA / DE-BetrVG / FR-Code du travail / Multiple]
**Agreement type:** [CBA / Betriebsvereinbarung / accord collectif / other]
**Review purpose:** [negotiation / compliance audit / M&A due diligence / dispute]
**Party represented:** [Management / Union-Works Council / Neutral]
**Agreement term:** [from — to / expiration date]
**Bargaining unit:** [description of covered employees]
**Based on:** [playbook / market standards / stated positions]

---

## Executive Summary

**Overall assessment:** [one-paragraph assessment of the agreement's risk profile]

**Risk distribution:**

- NON-COMPLIANT (Tier 1 Critical): [N] findings
- PARTIAL (Tier 2 Material): [N] findings
- PARTIAL (Tier 3 Informational): [N] findings
- COMPLIANT: [N] findings

**Top 3 priorities:**

1. [Most critical finding — NON-COMPLIANT]
2. [Second most critical finding]
3. [Third most critical finding]

**Recommended immediate action:** [one-sentence summary]

---

## Clause-by-Clause Analysis

### [Topic Area Name]

**Status:** [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Priority Tier:** [Tier 1 / Tier 2 / Tier 3]
**Confidence:** [Definite / High / Probable / Possible / Unlikely] ([score])

**Provision reviewed:** "[Quote or summary of the relevant clause]"

**Analysis:** [Specific analysis with legal basis; cite statute/case/decision with [VERIFY] if
unconfirmed]

**Issue:** [Concise description of the problem, if any]

**Remediation:** [Specific proposed language or action]

> _Fallback position (minimum acceptable):_ [Alternative if counterparty resists full remediation]

---

## Missing Provisions

| Provision        | Risk Level                | Recommendation    |
| ---------------- | ------------------------- | ----------------- |
| [Provision name] | [NON-COMPLIANT / PARTIAL] | [Specific action] |

---

## Priority Summary

### Tier 1: Critical — Immediate Action

[List of NON-COMPLIANT findings requiring immediate attention]

### Tier 2: Material — Next Negotiation

[List of PARTIAL findings for the next negotiation cycle]

### Tier 3: Informational — Monitor

[List of minor findings for tracking]

---

## Negotiation / Remediation Strategy

[2-3 paragraphs on recommended approach: what to lead with, what to concede, how to sequence
for management-side or union-side advocacy; or what to flag for buyer/seller in M&A context]

---

## Glass Box Audit Trail

[YAML block as defined in the Glass Box section above]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on:

- US NLRA legal research: 29 U.S.C. §§ 151-169; NLRB official guidance; Steelworkers Trilogy;
  Boys Markets; Janus v. AFSCME; Stericycle (2023); McLaren Macomb (2023); Endurance
  Environmental Solutions (2024); Starbucks Corp. v. McKinney (2024)
- German BetrVG/TVG legal research: Betriebsverfassungsgesetz (BetrVG); Tarifvertragsgesetz
  (TVG); Betriebsrätemodernisierungsgesetz 2021; §613a BGB; Hinweisgeberschutzgesetz (2023);
  BAG case law on Friedenspflicht and co-determination
- French Code du travail legal research: Ordonnances Macron 2017 (n° 2017-1386); Code du
  travail Arts. L2221-1 to L2262-4, L2312-1 to L2312-71; Loi n° 2023-1107 (partage de la
  valeur); PSE/RCC framework; Conseil d'État jurisprudence on CSE consultation
- 2-agent research pipeline (parallel Structural Analyst + Prompt Engineering Analyst) using
  Sonnet 4.6 model
- Calibrated against legalcode-contract-review gold standard skill
