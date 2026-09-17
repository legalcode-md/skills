---
name: legalcode-non-compete-analysis-fr
description: Deep enforceability analysis of a French non-compete clause (clause de non-concurrence) against
  the five cumulative Cour de cassation criteria established by the landmark decisions of 10 juillet 2002
  (Cass. Use when reviewing a clause de non-concurrence in a French CDI, CDD, severance agreement, or
  rupture conventionnelle; advising an employer on waiver strategy; or assessing an employee's ability
  to join a competitor.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Deep enforceability analysis of a French non-compete clause (clause de non-concurrence) against the five cumulative Cour de cassation criteria established by the landmark decisions of 10 juillet 2002 (Cass. Soc. n° 00-45.135 and 00-45.387). Covers mandatory financial compensation (contrepartie financière) and its calculation basis, collective bargaining agreement (CCN/CBA) overlay including Syntec IDCC 1486, Métallurgie IDCC 3248, and other major sector agreements, geographic and activity scope proportionality, maximum duration, employer renunciation (waiver) mechanics and deadlines, consequences of non-payment and employee breach (Cass. Soc. 24 janvier 2024), and special situations (rupture conventionnelle, licenciement économique, période d'essai, Art. L1224-1 business transfers). Produces ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID classification with confidence-scored enforceability assessment, CCN-specific remediation steps, employer waiver checklist, and Glass Box audit trail. Use when reviewing a clause de non-concurrence in a French CDI, CDD, severance agreement, or rupture conventionnelle; advising an employer on waiver strategy; or assessing an employee's ability to join a competitor. Routes from legalcode-non-compete-analysis (cross-jurisdictional router) for France-specific deep analysis. France only — not for non-competes in French franchise agreements (see legalcode-franchise-agreement-review-eu-fr) or in commercial business-sale agreements.


# Legalcode — Clause de Non-Concurrence (France)

> **Avertissement / Disclaimer**: Ce skill fournit un cadre pour l'analyse par IA de la
> clause de non-concurrence en droit du travail français. Il ne constitue pas un conseil
> juridique. Toutes les sorties doivent être examinées par un avocat qualifié en droit du
> travail français avant toute décision d'application, de renonciation ou de contentieux.
> Le droit de la non-concurrence évolue par voie jurisprudentielle — les décisions récentes
> de la Cour de cassation peuvent modifier l'analyse. Les références aux arrêts et aux
> conventions collectives issues de la mémoire comportent un risque d'hallucination —
> vérifiez sur légifrance.gouv.fr et service-public.fr avant de vous y fier.
>
> **Disclaimer**: This skill provides a framework for AI-assisted analysis of French
> non-compete clauses (clauses de non-concurrence). It does not constitute legal advice.
> All outputs must be reviewed by a qualified French employment lawyer (avocat en droit
> du travail) before any enforcement, waiver, or litigation decision. French non-compete
> law evolves through case law — recent Cour de cassation decisions may change the
> analysis. Statutory and case law references cited from memory carry hallucination risk
> — verify against légifrance.gouv.fr and service-public.fr before relying on them.

---

## Purpose and Scope

This skill analyses whether a French non-compete clause (clause de non-concurrence) is
enforceable, identifies specific deficiencies, assesses the applicable CCN overlay, and
generates confidence-scored enforceability classifications with actionable remediation.

**Covers:**

- Complete five-criteria enforceability test (Cour de cassation Soc. 10 juillet 2002)
- Mandatory financial compensation (contrepartie financière): calculation, adequacy, nullity risk
- CCN/CBA overlay for 6 major sector agreements (Syntec, Métallurgie, Commerce de gros,
  Banque/Assurances, and others)
- Geographic scope (limitation spatiale) proportionality analysis
- Activity scope (limitation matérielle) proportionality analysis
- Duration (limitation temporelle) assessment against CCN caps and case law
- Employer waiver (renonciation) strategy: timing, form, CCN deadlines, consequences
- Consequences analysis: non-payment (employee freed + damages), employee breach (forfeiture
  of all compensation — Cass. Soc. 24 janvier 2024, n° 22-20.926)
- Special situations: CDD, période d'essai, rupture conventionnelle, licenciement
  économique, Art. L1224-1 business transfer, démission
- Prescription periods (Art. L1471-1: 2 years; Art. L3245-1: 3 years for wage claims)
- Employer drafting or waiver strategy from contrepartie financière adverse ruling (Cass.
  Soc. 27 novembre 2020 — excessive compensation also voids)
- Glass Box audit trail for full traceability

**Does not:**

- Analyse non-solicitation of customers (clause de non-débauchage) or non-disclosure
  agreements in isolation — see `legalcode-nda-triage`
- Apply to non-competes in commercial franchise agreements — see
  `legalcode-franchise-agreement-review-eu-fr`
- Apply to non-competes in business-sale (cession de fonds de commerce) agreements,
  which follow a different (more permissive) standard under commercial law
- Cover non-French employment relationships
- Provide a legal opinion on any specific situation
- Replace qualified French employment counsel (avocat en droit du travail)

**Related skills:**

- `legalcode-non-compete-analysis` — cross-jurisdictional router (US/UK/DE/FR/CN)
- `legalcode-fr-contrat-de-travail-cdi` — full French CDI drafting and review
- `legalcode-franchise-agreement-review-eu-fr` — franchise non-compete (Art. L341-2)
- `legalcode-de-kuendigungsschutz` — German Kündigungsschutz and non-compete (HGB §§74-75a)

---

## Jurisdiction and Governing Law

**Jurisdiction: France (droit du travail français).**

French non-compete law is governed **entirely by case law** — the Code du travail contains
no dedicated statutory regime for clauses de non-concurrence in employment contracts. The
applicable framework derives from:

1. **Jurisprudence**: Cour de cassation, Chambre sociale (landmark: 10 juillet 2002)
2. **Conventions collectives nationales (CCN)**: Sector agreements supplement case law
   with specific duration caps, compensation floors, and waiver deadlines
3. **General contract law**: Code civil Arts. 1104 (good faith) and 1170 (unfair terms)
4. **Prescription**: Art. L1471-1 Code du travail (2-year general prescription for
   employment disputes) and Art. L3245-1 (3-year prescription for unpaid wage claims)

The **principe de faveur** (Art. L2251-1 Code du travail) means CCN provisions can
improve on (améliorer) statutory minimums but never fall below them. Where a CCN sets a
higher compensation floor than the contractual agreement, the CCN floor prevails.

**Legifrance verification link**: https://www.legifrance.gouv.fr (statutes, case law,
CCN texts) | https://code.travail.gouv.fr (CCN contributions and non-compete Q&A)

---

## Key Legal Framework

### Foundational Case Law

| Decision                   | Citation                                        | Key Holding                                                                             |
| -------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Landmark**               | Cass. Soc. 10 juil. 2002, n° 00-45.135 [VERIFY] | Establishes the five cumulative validity criteria; zero compensation = nullity          |
| **Companion**              | Cass. Soc. 10 juil. 2002, n° 00-45.387 [VERIFY] | Confirms that inadequate (derisory) compensation also = nullity                         |
| **Employee breach**        | Cass. Soc. 24 janv. 2024, n° 22-20.926 [VERIFY] | Employee who breaches forfeits ALL compensation, including for periods before violation |
| **Excessive compensation** | Cass. Soc. 27 nov. 2020 [VERIFY]                | Compensation disproportionately high relative to scope = clause void                    |
| **Waiver deadline**        | Cass. Soc. 13 sept. 2023 [VERIFY]               | Departure date (not notice end) triggers waiver deadline when notice is exempted        |
| **Pre-departure waiver**   | Cass. Soc. 19 oct. 2019, n° 18-19.741 [VERIFY]  | Employer cannot waive unilaterally during execution without contractual authority       |
| **Prescription**           | Cass. Soc. 2 oct. 2024, n° 23-12.844 [VERIFY]   | Damages for unlawful clause: 2 years from implementation; unpaid compensation: 3 years  |
| **Geographic scope**       | Cass. Soc. 8 janv. 2020, n° 18-16.667 [VERIFY]  | Clause limited to employee's activity perimeter is valid                                |

### CCN Non-Compete Matrix

| CCN                                    | IDCC | Duration Cap                                            | Compensation Floor                                     | Waiver Deadline                                       |
| -------------------------------------- | ---- | ------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
| **Syntec** (IT/consulting/engineering) | 1486 | Not fixed in CCN; 1-2 years standard                    | 30–50% of gross monthly salary [VERIFY]                | ~15 days after termination (registered mail) [VERIFY] |
| **Métallurgie** (post-Jan 2024)        | 3248 | Max 1 yr initial + 1 yr renewal = 2 yrs max (Art. 79.2) | ≤1 yr: ⅓ gross salary; 1-2 yrs: ½ gross salary         | At or before effective departure date                 |
| **Commerce de gros**                   | 573  | Typically 1-2 years                                     | Minimum financial compensation required [VERIFY]       | Per contract / general rules                          |
| **Banque**                             | 2120 | Per individual/senior agreement                         | Sector-specific; generally ≥30% [VERIFY]               | Per contract / general rules                          |
| **Assurances**                         | 105  | Per individual agreement                                | Sector-specific [VERIFY]                               | Per contract / general rules                          |
| **No CCN / CCN silent**                | —    | No statutory cap; 2 years reasonable maximum            | Minimum ~25% of gross salary; <25% = high nullity risk | At or before departure (apply general rule)           |

> **Note**: CCN provisions change via branch-level negotiation. Always verify current
> text on legifrance.gouv.fr or code.travail.gouv.fr before advising.

### Code du Travail Articles (Non-Compete Related)

| Article       | Subject                                                         |
| ------------- | --------------------------------------------------------------- |
| Art. L1221-1  | Freedom of contract (employment contract basis)                 |
| Art. L2251-1  | Principe de faveur — CCN can only improve statutory minimums    |
| Art. L1224-1  | Automatic transfer of employment contracts on business transfer |
| Art. L1471-1  | 2-year prescription for employment disputes                     |
| Art. L3245-1  | 3-year prescription for unpaid wage/compensation claims         |
| Art. L1232-1  | Dismissal for personal cause — relates to waiver timing         |
| Art. L1237-11 | Rupture conventionnelle — non-compete may survive unless waived |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the enforceability analysis
- The applicable CCN determines different compensation floors or waiver deadlines
- The termination type affects when the waiver window opens and closes
- The user's role (employer or employee) determines the remediation strategy

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

### Step 1: Accept the Non-Compete Clause

Accept input in any of these formats:

- **Clause text**: The clause de non-concurrence as written in the employment contract
- **Described terms**: A verbal or structured description of the clause's key parameters
  (duration, geographic scope, activity scope, compensation amount, CCN applicable)
- **Full contract**: A CDI or CDD from which the non-compete clause will be extracted

If no clause is provided, ask the user to supply the relevant clause text or its key terms.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask:

1. **Which party are you advising?**
   - Options: Employer (drafting or waiving clause), Employee (assessing ability to leave),
     Buyer/Acquirer (M&A due diligence), Neutral (academic / policy analysis)
   - _Why this matters_: The enforceability conclusion and remediation strategy depend
     entirely on which side needs to act.

2. **What is the stage of the matter?**
   - Options: Drafting (new contract — optimize clause), Pre-departure (employment still
     active — waiver strategy), Post-departure (restriction period active — enforcement
     or challenge), Litigation (dispute already filed)
   - _Why this matters_: The available remedies and priority actions differ materially
     by stage.

3. **What type of termination occurred or is expected?**
   - Options: Licenciement (employer-initiated dismissal), Démission (employee resignation),
     Rupture conventionnelle (mutual termination), Licenciement économique (redundancy),
     Fin de période d'essai (end of probationary period), Still employed / not yet terminated
   - _Why this matters_: Affects waiver deadline calculation and some CCN-specific rules.

4. **What is the applicable CCN (convention collective nationale)?**
   - Options: Syntec IDCC 1486, Nouvelle Métallurgie IDCC 3248, Commerce de gros IDCC
     573, Banque IDCC 2120, Assurances IDCC 105, Other (specify), Not known / None
   - _Why this matters_: Each CCN sets its own compensation floor, duration cap, and
     waiver deadline, any of which can override contract terms.

5. **What is the employee's position category?**
   - Options: Cadre (executive/manager), Technicien/Agent de maîtrise (intermediate),
     Employé (non-management), Apprenti (apprentice), Not known
   - _Why this matters_: Compensation floors and duration norms differ for cadres vs.
     non-cadres in several CCNs.

6. **What is the employee's approximate gross monthly remuneration?** (to calculate
   compensation adequacy)
   - _Why this matters_: Determines whether the contractual compensation meets CCN and
     case law minimums. If not known, note that adequacy cannot be verified.

### Step 3: Identify the Applicable CCN Rules

Using the CCN identified in Step 2:

1. Retrieve the CCN's specific non-compete provisions (duration cap, compensation floor,
   waiver deadline, form requirements) from the CCN matrix in the Key Legal Framework
   section above.
2. Note any CCN provisions that are more favourable to the employee than the contractual
   terms — these prevail under the principe de faveur.
3. If the CCN is not known or the CCN is silent on non-compete, apply general case law
   standards (5 criteria, minimum ~25% compensation, general waiver rules).
4. If multiple CCNs could apply (e.g., company recently changed sector), flag the
   uncertainty and apply the most protective standard.

### Step 4: Apply the Five Validity Criteria

Assess each criterion sequentially. **All five are cumulative** — failure on any one
criterion renders the clause null and void (nulle et de nul effet).

#### Criterion 1: Written Form (Forme écrite)

- [ ] Is the clause de non-concurrence included in a written document signed by both parties?
- [ ] Is the clause sufficiently specific to put the employee on notice of its terms?
- [ ] Is it in French (or with a French translation for non-French-speaking employees)?

**Classification**:

- ENFORCEABLE: Written, signed, legible, in French
- AT-RISK: Clause exists but appears in a document not specifically signed by employee,
  or in a document reference only
- VOID: No written clause, or purely oral agreement

#### Criterion 2: Legitimate Employer Interest (Intérêt légitime de l'entreprise)

Assess whether protecting the employer from this employee's competition serves a genuine
business interest:

- [ ] Does the employee have significant access to clients, trade secrets, proprietary
      know-how, or strategic information that would give a competitor an unfair advantage?
- [ ] Is the employee's role one where departure to a competitor would cause concrete harm?
- [ ] Is the interest proportionate to the restriction (secretary with no client contact
      vs. senior commercial director)?

**Red flags** (high nullity risk):

- Administrative, clerical, or support employees with no client/data access
- Junior employees who have not yet developed relationships or technical know-how
- Roles where the knowledge is publicly available or taught at university

**Classification**:

- ENFORCEABLE: Clear legitimate interest documented
- AT-RISK: Marginal interest; court could go either way depending on role evidence
- VOID: No plausible legitimate interest (e.g., office assistant restricted from
  working in any insurance company)

#### Criterion 3: Geographic Scope Limitation (Limitation spatiale)

- [ ] Is the geographic scope expressly defined (specific regions, departments, cities)?
- [ ] Is the geographic scope proportionate to the employee's actual work territory?
- [ ] Could the employee reasonably find equivalent work outside the restricted area?

**Proportionality tests**:

- Employee worked only in Île-de-France → restriction on all of France = disproportionate
- National sales director covering all of France → national restriction = proportionate
- International business development role → European or global restriction may be justified
  if the employer's competitive interest genuinely spans those geographies

**Red flags**:

- Worldwide restriction without specific justification for international scope
- "France and Benelux" for a salesperson covering only Paris region
- No geographic limitation at all (void on its face)

**Classification**:

- ENFORCEABLE: Scope matches employee's actual territory; proportionate
- AT-RISK: Somewhat broader than actual territory; court could sever or void
- VOID: No geographic limit, or scope clearly disproportionate to role

#### Criterion 4: Activity Scope Limitation (Limitation matérielle)

- [ ] Are the restricted activities specifically identified?
- [ ] Are the restricted activities limited to what the employee actually performed?
- [ ] Does the restriction prevent the employee from using their general professional
      skills (not just employer-specific knowledge)?

**Proportionality tests**:

- Software engineer restricted from working for any technology company = too broad
- Software engineer restricted from working for companies that develop competing
  payroll software in direct competition with employer's product = proportionate
- Any restriction that prevents the employee from using skills acquired through
  education or prior careers = likely void

**Red flags**:

- Restriction on "any activity in the [sector]" rather than specific competing activities
- Restriction covering employer's entire field even though employee touched only a subset
- Catch-all language like "any business similar to" without specificity

**Classification**:

- ENFORCEABLE: Activities clearly defined and match actual role
- AT-RISK: Scope somewhat broader than role; partial reduction risk
- VOID: Entire sector prohibited, or no activity limitation

#### Criterion 5: Mandatory Financial Compensation (Contrepartie financière)

This criterion is the most frequently litigated. Apply the following sub-analysis:

**5a. Existence check**:

- [ ] Does the contract provide for financial compensation (contrepartie financière)?
- [ ] If no compensation is stated: clause is automatically VOID (Cass. Soc. 10 juil. 2002)

**5b. Adequacy check**:

- [ ] Is the compensation amount at or above the applicable CCN floor?
- [ ] If no CCN floor: is the compensation at least ~25% of gross monthly remuneration?
      (Below 25% = high nullity risk as "dérisoire" under Cour de cassation standards)
- [ ] Is the compensation amount proportionate (not excessively high) relative to the
      scope of the restriction? Excessive compensation can also void the clause
      (Cass. Soc. 27 nov. 2020) [VERIFY]

**5c. Calculation basis check**:

- [ ] Is the compensation calculated on gross remuneration (salaire brut)?
- [ ] Does the calculation base include variable pay, bonuses, and commissions?
      (Courts broadly interpret "remuneration" — artificially narrow bases = risk)
- [ ] Is the reference period "average of the last 12 months" or equivalent?
- [ ] Is payment made monthly during the restriction period?

**5d. Payment start date**:

- [ ] Does payment begin from the employee's actual departure date (date effective de
      départ), not from the expiry of a notice period if the employee was exempted?

**Compensation adequacy thresholds by CCN**:

| CCN                   | Duration  | Minimum Compensation                                     |
| --------------------- | --------- | -------------------------------------------------------- |
| Syntec IDCC 1486      | Any       | 30% of gross monthly salary [VERIFY]                     |
| Métallurgie IDCC 3248 | ≤ 1 year  | ⅓ of average gross monthly remuneration (last 12 months) |
| Métallurgie IDCC 3248 | 1–2 years | ½ of average gross monthly remuneration (last 12 months) |
| No CCN / CCN silent   | Any       | ≥25% of gross monthly remuneration (case law minimum)    |

**Classification**:

- ENFORCEABLE: Compensation exists, meets CCN/case law floor, calculation is sound
- AT-RISK: Compensation exists but is marginally adequate; calculation base is narrow
  or ambiguous
- NON-COMPLIANT: Compensation exists but falls below applicable minimum
- VOID: No compensation stated at all

### Step 5: Assess Duration

Even if compensation is adequate, duration must be proportionate:

- [ ] What is the stated duration?
- [ ] Does the duration comply with the applicable CCN cap?
  - Métallurgie IDCC 3248: maximum 2 years total (1 year + 1 year renewal)
  - Syntec IDCC 1486: no hard statutory cap in CCN; 1-2 years standard
  - Most CBAs: 1-2 year range is standard; beyond 2 years rarely upheld
- [ ] Is the duration proportionate to the level of legitimate interest?
      (A senior executive with deep client relationships = 2 years reasonable;
      a junior developer = 6-12 months more appropriate)
- [ ] Is the clause of indefinite duration? → VOID

**⟁ CLARIFY** — If the contract provides for employer renewal of the non-compete (as in
Métallurgie IDCC 3248), ask: "Has the employer formally exercised the renewal right, and
if so, by what means and on what date? Under Cass. Soc. 13 sept. 2023, renewal requires
a positive act (acte positif) by the employer."

### Step 6: Assess Employer Waiver (Renonciation)

Analyse the employer's waiver position, applicable deadlines, and consequences:

**6a. Identify the CCN waiver deadline**:

- Syntec IDCC 1486: ~15 days after termination/notification (by registered mail) [VERIFY]
- Métallurgie IDCC 3248: at or before actual departure date
- No CCN: apply general case law — employer must waive by the employee's actual
  departure date (date effective de départ)

**6b. Identify the triggering event**:

- Normal notice completed: waiver deadline runs from the last day of notice
- Notice exempted (dispensé de préavis): waiver deadline runs from the date the
  employee physically leaves (Cass. Soc. 13 sept. 2023) — NOT from the end of the
  contractual notice period
- Rupture conventionnelle: deadline runs from the homologation date or actual departure

**6c. Assess waiver form compliance**:

- [ ] Was the waiver in writing? (Oral waiver = not recognized)
- [ ] Was it sent by registered letter with acknowledgement of receipt (LR-AR), or
      included in the dismissal/termination letter itself (acceptable per Cour de cassation)?
- [ ] Was the waiver received by the employee within the applicable CCN deadline?

**6d. Assess waiver consequences**:

- Valid waiver → employer owes NO compensation; employee is free immediately
- Late or defective waiver → employer must pay FULL compensation for the entire
  restriction period, even if employee joins a competitor immediately
- Silence = failure to waive → compensation remains due; clause is in effect

**6e. Can the employer waive prospectively (during contract execution)?**

- General rule: NO — waiver during employment execution requires specific contractual
  or CCN authority (Cass. Soc. 19 oct. 2019)
- The contract may include a clause granting the employer discretion to waive at
  termination; this is enforceable

**Classification** (for waiver analysis):

- WAIVER VALID: Written, timely, correct form, within CCN deadline
- WAIVER DEFECTIVE: Late, wrong form, or ambiguous
- WAIVER IMPOSSIBLE: Past the applicable deadline; employer must pay compensation

### Step 7: Assess Post-Departure Enforcement and Breach

If the restriction period is active (employee has left or will leave), analyse:

**7a. Employer enforcement options**:

- Injunction (référé) before Conseil de prud'hommes: fast (weeks to months); requires
  showing breach (constat d'huissier or equivalent evidence) and urgent threat
- Claim for damages: filed in Conseil de prud'hommes (full merits); typically 6-12
  months to first-instance judgment
- Claim for restitution of paid compensation from breaching employee

**7b. Employee breach consequences** (Cass. Soc. 24 janv. 2024, n° 22-20.926):

- Employee who violates the clause forfeits ALL compensation — including compensation
  already received before the breach
- This rule applies even if the violation lasted only a brief period
- Employee cannot "cure" the breach retroactively by later complying
- Advise any employee client: do NOT join a competitor until legal advice is obtained
  on enforceability; the financial exposure is the entire compensation stream

**7c. Employer non-payment consequences**:

- Employee is freed from the non-compete obligation
- Employee may claim all unpaid compensation as a wage claim (prescription: 3 years
  under Art. L3245-1 Code du travail)
- Employee may claim additional damages
- CRITICAL: Employee must continue to honour the clause until a court releases them —
  the employee cannot unilaterally decide the clause is void due to non-payment without
  judicial confirmation

### Step 8: Special Situations Analysis

Apply additional analysis for specific termination types:

**Période d'essai (probationary period)**:

- Non-compete clauses CAN apply to terminations during probation
- Métallurgie IDCC 3248 (Art. 79.2): if terminated during trial period, duration of
  non-compete cannot exceed the duration of the trial period itself [VERIFY]
- Compensation is still due from actual departure date

**Rupture conventionnelle**:

- Non-compete survives rupture conventionnelle unless explicitly waived in the agreement
- The parties can negotiate waiver as part of the rupture conventionnelle package —
  advisable to address explicitly in the homologation form annexe
- Waiver deadline: employer must waive by the date of actual departure (date de fin
  de contrat agreed in the rupture conventionnelle form)

**Licenciement économique (redundancy)**:

- Same five-criteria rules apply; no special exemption
- Employers often negotiate non-compete waiver as part of the economic dismissal
  settlement package (Plan de Sauvegarde de l'Emploi / accord collectif)
- Higher severance may provide leverage to obtain employee agreement to a reduced or
  waived non-compete

**Démission (employee resignation)**:

- Same rules apply; compensation is due unless employer waives within the CCN deadline
- From the employer's perspective, timely waiver is advisable to avoid paying
  compensation when the employee voluntarily chose to leave

**Art. L1224-1 business transfer**:

- Employment contracts (and all obligations therein) transfer automatically to the
  acquiring employer
- The non-compete clause transfers with the contract
- New employer inherits both the right to enforce the clause AND the obligation to pay
  compensation (or waive)
- If the competitive landscape changes post-transfer (acquired employer is no longer
  in the same business), courts may scrutinize enforceability more closely [VERIFY]

**CDD (contrat à durée déterminée)**:

- Non-compete clauses CAN be validly included in CDD contracts
- Same five-criteria test applies
- Duration of restriction must be reasonable relative to the CDD's own duration

---

## Enforceability Classification

### Four-Tier Classification System

| Classification    | Meaning                                                                               | Immediate Action                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **ENFORCEABLE**   | All five criteria met; CCN floors satisfied; no material defect                       | Employer may enforce; employee must honour                                                        |
| **AT-RISK**       | One or more criteria met weakly; court could void or sever                            | Both sides: seek counsel before acting; employer consider waiver if cost-beneficial               |
| **NON-COMPLIANT** | Specific defect identified (e.g., compensation below CCN floor) but not facially void | Remediable if parties agree to modify; otherwise court likely to void                             |
| **VOID**          | Facially invalid — missing compensation, no geographic limit, or no written form      | Employee is freed from obligation; employer owes compensation for any restriction already imposed |

### Overall Enforceability Determination

After completing Steps 4–6, assign the worst (most adverse) classification from any
individual criterion as the overall enforceability level. If any criterion is VOID,
the overall clause is VOID regardless of other criteria.

---

## Actionable Output per Finding

For each deficiency identified, generate:

1. **Finding**: Precise description of the deficiency (quote the clause text where possible)
2. **Legal basis**: Cour de cassation authority or CCN provision
3. **Classification**: ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID
4. **Confidence**: Definite / High / Probable / Possible / Unlikely
5. **Remediation** (employer-side): Specific action to cure the deficiency or manage risk
6. **Counter-position** (employee-side): Grounds to challenge enforceability in court
7. **Model language** (if applicable): Alternative drafting to cure the deficiency

**Example finding**:

> **Finding**: The clause restricts the employee from working "in the [sector] industry in
> France" without limiting the restriction to activities actually performed by the employee
> (payroll software development).
>
> **Legal basis**: Cour de cassation requirement that activity restriction be limited to
> "specifically targeted activities" actually performed.
>
> **Classification**: AT-RISK → NON-COMPLIANT (courts have voided similarly broad clauses)
>
> **Confidence**: High (0.85)
>
> **Employer remediation**: Propose amendment narrowing restriction to "development,
> marketing, or sale of payroll or HRIS software products in direct competition with
> [Employer]'s [ProductName] product." Require employee consent to the amendment (signed
> addendum).
>
> **Employee counter-position**: Apply to Conseil de prud'hommes for declaration of nullity
> and recovery of all financial compensation paid (Art. L3245-1, 3-year prescription).
>
> **Model language**: _"Le Salarié s'interdit, pendant [durée], de rejoindre toute
> entreprise concurrente dont l'activité principale comprend [activité spécifique], dans
> les territoires de [géographie], étant entendu que cette restriction est limitée aux
> fonctions effectivement exercées par le Salarié au sein de la Société."_

---

## Prioritization Framework

### Tier 1 — Critical (0–14 days action required)

Deficiencies that render the clause immediately void or expose the employer to
irreversible financial liability:

- Missing or zero compensation (clause is void; any restriction already imposed creates
  employer liability)
- Employer has missed the waiver deadline while still intending to waive
- Employee has violated clause — employer needs to assess enforcement or accept breach
- Employer has stopped paying compensation mid-period — employee may seek release

### Tier 2 — Material (15–60 days)

Deficiencies that significantly reduce enforceability but are potentially curable or
manageable:

- Compensation below CCN floor but above zero
- Geographic scope wider than employee's actual territory
- Activity scope covering more than employee's actual functions
- Duration exceeds CCN cap by < 6 months
- Waiver notice served by incorrect method (email vs. registered mail where CCN requires LR-AR)

### Tier 3 — Advisory (60–180 days)

Deficiencies worth addressing in the next contracting cycle or HR policy review:

- Ambiguous calculation base for compensation (no explicit reference to variable pay)
- No specified waiver deadline in contract (employer relying solely on general case law)
- Duration at upper end of CCN range but still within maximum
- No express provision for Art. L1224-1 business transfer scenarios
- Clause last reviewed more than 3 years ago (CCN may have changed)

---

## Citation Quality Gates

Run these five gates **silently** before delivering any output. If any gate fails,
revise before delivering.

| Gate                       | Rule                                                                                                                       | Fail Action                                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source** (Source)        | Every enforceability conclusion cites a Cour de cassation decision, CCN provision, or Code du travail article              | Add citation or mark "[UNVERIFIED]"                              |
| **Format** (Format)        | All French citations follow standard format: "Cass. Soc. [date], n° [pourvoi]" or "Art. [L/R/D][number] Code du travail"   | Fix format                                                       |
| **Currency** (Actualité)   | Every CCN compensation floor and waiver deadline checked — CCNs change via avenant; Cour de cassation evolves law annually | Flag "[VÉRIFIER ACTUALITÉ — CCN / jurisprudence récente]"        |
| **Domain** (Domaine)       | Analysis stays within French employment law scope; no confusion with commercial non-compete standards or foreign law       | Remove or flag any cross-contamination                           |
| **Confidence** (Confiance) | Uncertainty is explicitly stated for any conclusion below High confidence; no false precision                              | Add confidence qualifier and recommend professional verification |

---

## Self-Interrogation for VOID and NON-COMPLIANT Findings

For any finding classified VOID or NON-COMPLIANT, apply this 3-pass adversarial review
before delivering the conclusion:

**Pass 1 — Legal Chain Integrity**: Does the void/non-compliant conclusion follow
directly from the cited Cour de cassation authority? Is the authority factually analogous
to the clause being analysed, or is there a meaningful distinction?

**Pass 2 — Completeness**: Have all five criteria been checked? Has the applicable CCN
been identified and its provisions checked against the contractual terms? Has the
compensation calculation base been verified, not just the stated percentage?

**Pass 3 — Challenge**: What is the strongest argument that the clause IS enforceable
or that the deficiency is curable? Under what circumstances might a Cour d'appel uphold
the clause despite this deficiency (e.g., by severing an overly broad geographic scope
rather than voiding entirely)?

---

## Confidence Scoring

| Level         | Range     | Meaning                                                       | Action                                                             |
| ------------- | --------- | ------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Définitif** | 0.95–1.0  | Settled Cour de cassation principle; direct application       | State with confidence                                              |
| **Élevé**     | 0.80–0.94 | Strong case law authority; minor factual distinction possible | State with brief caveat                                            |
| **Probable**  | 0.60–0.79 | Good authority; court could distinguish on facts              | State with reasoning and contra-indicators                         |
| **Possible**  | 0.40–0.59 | Genuinely uncertain — new issue or conflicting decisions      | Flag for qualified counsel with both sides presented               |
| **Incertain** | 0.0–0.39  | Weak basis or genuinely speculative                           | Do not assert; flag "[INCERTAIN — vérification juridique requise]" |

---

## Glass Box Audit Trail

Include the following YAML block at the end of every analysis output:

```yaml
glass_box:
  skill_name: "legalcode-non-compete-analysis-fr"
  jurisdiction: "France — droit du travail"
  analysis_date: "[YYYY-MM-DD]"
  clause_source: "[Contract title / Description / 'Described by user']"
  applicable_ccn: "[CCN name and IDCC, or 'Not identified']"
  employee_category: "[Cadre / Non-cadre / Apprenti / Unknown]"
  termination_type: "[Licenciement / Démission / Rupture conventionnelle / Licenciement économique / Période d'essai / Not yet terminated]"
  advising_party: "[Employer / Employee / Acquirer / Neutral]"
  criteria_assessed:
    - criterion_1_written_form: "[ENFORCEABLE / AT-RISK / VOID]"
    - criterion_2_legitimate_interest: "[ENFORCEABLE / AT-RISK / VOID]"
    - criterion_3_geographic_scope: "[ENFORCEABLE / AT-RISK / VOID]"
    - criterion_4_activity_scope: "[ENFORCEABLE / AT-RISK / VOID]"
    - criterion_5_compensation: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]"
  duration_assessment: "[WITHIN CCN CAP / MARGINAL / EXCEEDS CCN CAP / INDEFINITE]"
  waiver_assessment: "[VALID / DEFECTIVE / IMPOSSIBLE / NOT APPLICABLE]"
  overall_classification: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]"
  legalcode_mcp: "[Connected — [N] results retrieved / Not connected]"
  citations_verified: "[N VERIFIED via légifrance.gouv.fr / N UNVERIFIED — marked [VERIFY]]"
  confidence_overall: "[Définitif / Élevé / Probable / Possible / Incertain] — [rationale]"
  key_limitations:
    - "[Any assumptions made, e.g., 'CCN not confirmed — Syntec assumed based on sector']"
    - "[Any factual gaps that affect analysis, e.g., 'Compensation calculation base not stated in clause']"
  reviewer: "AI-assisted — requires review by avocat en droit du travail before action"
```

---

## Anti-Patterns

What NOT to do when analysing or drafting a French non-compete clause:

1. **Omitting compensation entirely**: The single most common and fatal error. A clause
   de non-concurrence without contrepartie financière is automatically void — no
   judicial severance possible. Never draft or advise a clause with zero compensation.

2. **Setting derisory compensation**: Compensation of 5-10% of salary has been struck
   down as "dérisoire" by courts. The practical minimum is ~25%; below 30% is high risk
   for most roles.

3. **Making compensation disproportionately high**: As established in Cass. Soc.
   27 novembre 2020, compensation excessively high relative to the restriction's scope
   (e.g., 100% salary for a narrow geographic/activity scope) can also void the clause.
   Compensation must be proportionate in both directions.

4. **Using a narrow compensation base**: Calculating the contrepartie financière on
   base salary only and excluding bonuses, commissions, and variable pay. Courts broadly
   interpret "remuneration" — deliberate exclusions are challenged and frequently fail.

5. **Starting compensation payment from notice expiry when notice is exempted**: If
   the employer exempts the employee from notice (dispense de préavis), the restriction
   period and payment obligation begin from the actual departure date — not from when
   the contractual notice would have ended. Late payment start = employer breach.

6. **Missing the CCN waiver deadline**: Failing to renounce the non-compete within the
   CCN-specified window (e.g., ~15 days for Syntec) means the employer must pay full
   compensation even if the employee immediately joins a competitor. Calendar the
   deadline at the outset of any termination process.

7. **Waiving by email or telephone**: Where the CCN (or the contract) requires waiver
   by lettre recommandée avec accusé de réception (LR-AR), an email or phone call is
   insufficient. Always use the specified form; if in doubt, use LR-AR.

8. **Applying a nationwide restriction to a locally-based employee**: A salesperson
   covering the Île-de-France region cannot be validly restricted from working across
   all of France. Courts void clauses whose geographic scope exceeds the employee's
   actual territory.

9. **Restricting entire industry sectors rather than specific competing activities**:
   Prohibiting an IT employee from "working in any technology company" is void. The
   restriction must be limited to activities that directly compete with the employer's
   specific products or services and that the employee actually performed.

10. **Advising an employee to stop honouring the clause because the employer stopped
    paying**: This is dangerous advice. The employee must continue to comply and file a
    claim for unpaid compensation — self-help (working for a competitor) forfeits ALL
    compensation under Cass. Soc. 24 janvier 2024, including compensation already paid
    before the breach.

11. **Failing to update the clause when the employee's role changes materially**: A
    clause that was proportionate for a junior developer becomes disproportionate after
    promotion to Global Head of Sales. Stale clauses are challenged on proportionality
    grounds and frequently voided.

12. **Confusing the Métallurgie IDCC 3248 renewal rules**: The new Métallurgie CCN
    (effective 1 January 2024) allows renewal once — but only by a positive act (acte
    positif) of the employer. Automatic renewal clauses do not work under Cass. Soc.
    13 septembre 2023. The renewal must be actively exercised by the employer.

13. **Assuming the clause does not apply to CDD or probationary period terminations**:
    Non-compete clauses apply to all contract types and termination circumstances unless
    the clause specifically carves out those scenarios. Assume it applies unless it is
    explicitly excluded.

14. **Ignoring Art. L1224-1 in M&A contexts**: When a business is transferred, the
    non-compete obligation (and liability to pay compensation) automatically transfers
    to the acquiring entity. Failure to account for this in the SPA creates unexpected
    ongoing compensation liabilities for the acquirer.

15. **Confusing the two prescription regimes**: Damages for an unlawful clause (e.g.,
    void clause applied anyway) prescribe in 2 years from implementation (Art. L1471-1).
    Claims for unpaid compensation prescribe in 3 years from when the debt became due
    (Art. L3245-1). Mixing these up causes missed claims or spurious defenses.

16. **Treating the non-compete as severable when it is void**: French courts do not
    generally sever void non-compete clauses and rewrite them to be proportionate (unlike
    some US courts applying blue-pencil doctrine). When a French court finds a clause
    void, it is void in full — the employer loses all protection.

17. **Failing to consider the non-compete in the rupture conventionnelle negotiation**:
    The rupture conventionnelle creates a natural opportunity to negotiate a mutual waiver
    of the non-compete as part of the overall separation package. Failing to address the
    clause at this stage leaves it active and potentially costly for the employer.

---

## Writing Standards

Before delivering any output:

1. **Lead with the overall classification** — ENFORCEABLE / AT-RISK / NON-COMPLIANT /
   VOID — before presenting detailed findings.
2. **Use bilingual terminology** for key French legal concepts on first use:
   "non-compete clause (clause de non-concurrence)", "financial compensation
   (contrepartie financière)", "collective bargaining agreement (convention collective
   nationale / CCN)".
3. **State confidence explicitly** — never present a contested point as settled without
   flagging the uncertainty level.
4. **Use precise clause references** — quote the problematic language verbatim where
   possible rather than paraphrasing.
5. **Distinguish employer-side from employee-side advice** clearly when the user has
   specified which party is being advised.
6. **Flag all [VERIFY] markers** in the output with a note: "This reference was cited
   from AI memory — verify on légifrance.gouv.fr before relying on it."
7. **Avoid false certainty on CCN-specific rules** — CCN provisions change via avenants;
   always recommend confirming current text on code.travail.gouv.fr.
8. **Plain language where possible** — if using French legal terms without an English
   translation, add "(i.e., [plain English explanation])" on first use.
9. **Do not state as fact any Cour de cassation decision without a [VERIFY] marker**
   unless the decision was confirmed via legalcode-mcp or légifrance.gouv.fr search.

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- In Step 3, search for current CCN provisions by IDCC number: query "clause de
  non-concurrence [CCN name] IDCC [number] contrepartie financière durée"
- In Steps 4–5, search for recent Cour de cassation decisions on non-compete
  proportionality and compensation adequacy: query "Cass. Soc. clause non-concurrence
  [criterion] [year range 2020-2026]"
- Save key verified citations and CCN provisions to `/tmp/legalcode-fr-non-compete-research.md`
- Mark verified citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Proceed with analysis using the CCN matrix and case law table in this skill
- Mark all Cour de cassation citations and CCN-specific rules with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all citations require
verification on légifrance.gouv.fr"`
- Direct the user to verify current CCN text on code.travail.gouv.fr before acting

---

## Output Format Template

```markdown
# Analyse — Clause de Non-Concurrence (France)

**Date d'analyse / Analysis Date**: [YYYY-MM-DD]
**Clause source**: [Contract title or description]
**Partie conseillée / Party advised**: [Employer / Employee / Acquirer / Neutral]

---

## Classification générale / Overall Classification

**[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]**
**Confidence**: [Level] ([score range]) — [One-sentence rationale]

---

## CCN applicable / Applicable CBA

**[CCN name] IDCC [number]** — or "Not identified; general case law standards applied"

**CCN-specific rules applicable**:

- Duration cap: [X years]
- Compensation floor: [%] of gross monthly remuneration
- Waiver deadline: [X days / at departure date]
- Form requirement: [LR-AR / dismissal letter / other]

---

## Résultats par critère / Findings by Criterion

### Critère 1 — Forme écrite (Written Form)

**Classification**: [ENFORCEABLE / AT-RISK / VOID]
**Finding**: [Description]
[If AT-RISK or VOID: **Remediation** | **Counter-position** | **Model language**]

### Critère 2 — Intérêt légitime (Legitimate Interest)

**Classification**: [ENFORCEABLE / AT-RISK / VOID]
**Finding**: [Description]
[If AT-RISK or VOID: **Remediation** | **Counter-position**]

### Critère 3 — Limitation spatiale (Geographic Scope)

**Classification**: [ENFORCEABLE / AT-RISK / VOID]
**Finding**: [Description]
[If AT-RISK or VOID: **Remediation** | **Counter-position** | **Model language**]

### Critère 4 — Limitation matérielle (Activity Scope)

**Classification**: [ENFORCEABLE / AT-RISK / VOID]
**Finding**: [Description]
[If AT-RISK or VOID: **Remediation** | **Counter-position** | **Model language**]

### Critère 5 — Contrepartie financière (Financial Compensation)

**Classification**: [ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]
**Finding**: [Description — amount, calculation base, CCN compliance]
**Compensation adequacy**: [€X/month = Y% of gross salary; CCN floor = Z%]
[If deficient: **Remediation** | **Counter-position** | **Model language**]

---

## Durée / Duration

**Classification**: [WITHIN CCN CAP / MARGINAL / EXCEEDS CCN CAP / INDEFINITE]
**Finding**: [Stated duration vs. CCN cap]

---

## Renonciation / Employer Waiver Analysis

**Classification**: [VALID / DEFECTIVE / IMPOSSIBLE / NOT APPLICABLE]
**Deadline**: [Date or event that triggers the waiver window]
**Recommended action**: [If employer has not yet waived: specific action with deadline]

---

## Situations particulières / Special Situation Notes

[If applicable: CDD, période d'essai, rupture conventionnelle, licenciement économique,
Art. L1224-1 transfer — analysis of specific implications]

---

## Plan d'action / Action Plan by Priority

### Tier 1 — Critical (0–14 days)

- [ ] [Action with responsible party and deadline]

### Tier 2 — Material (15–60 days)

- [ ] [Action with responsible party and deadline]

### Tier 3 — Advisory (60–180 days)

- [ ] [Action with responsible party and deadline]

---

## Prescription / Limitation Periods

- **Damages for unlawful clause**: [Date prescription expires — 2 years from [event]]
- **Unpaid compensation claims**: [Date prescription expires — 3 years from [event]]

---

[Glass Box YAML block — see Glass Box Audit Trail section above]
```

---

## Localization Notes

### DOM-TOM (Overseas Territories)

Code du travail applies in the DOM (Guadeloupe, Martinique, Guyane, La Réunion,
Mayotte) with some adaptations. The CCN applicable depends on the employer's sector
registration — verify that the same metropolitan CCN covers the overseas territory,
as some territories have their own accords.

### Cross-Border Employees

For employees who work partly in France and partly in other EU jurisdictions, the
Rome I Regulation (EU) 593/2008 determines the applicable law. An employer cannot
contract out of French mandatory employment law provisions (including the five-criteria
non-compete test) by choosing a foreign governing law if France is the country of
habitual work. French courts will apply French law regardless of a foreign law clause
in such cases [VERIFY].

### Comparison with German HGB §§74-75a

| Aspect               | France                                                   | Germany                                                                         |
| -------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Statutory basis      | Case law only                                            | HGB §§74-75a (explicit statute)                                                 |
| Minimum compensation | ~25% (case law); CCN floors vary                         | 50% of gross salary (statutory minimum)                                         |
| Maximum duration     | No statutory cap (2 years standard by case law and CCNs) | 2 years (statutory maximum — HGB §74a)                                          |
| Waiver timing        | At or before departure; CCN-specific windows             | Written release ≥1 year before contract end                                     |
| Unenforceable clause | Void (no severance rewriting by courts)                  | Unverbindlich (employee can choose to comply and claim compensation, or ignore) |
| CCN overlay          | Extensive — CCNs govern much of the detail               | Less prominent; law is largely self-executing                                   |

Multinational employers with employees in both France and Germany must treat each
jurisdiction separately — a clause compliant in Germany may be void in France and
vice versa.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Cour de cassation jurisprudence (Légifrance) — landmark decisions from 2002 through 2024
- CCN provisions for Syntec IDCC 1486 and Métallurgie IDCC 3248 (code.travail.gouv.fr)
- L&E Global France employment law overview (2024)
- Mayer Brown, "Restrictive Covenants — France" (July 2024)
- DLA Piper, New remuneration thresholds (2025)
- Cass. Soc. 24 janvier 2024 n° 22-20.926 (employee breach forfeiture)
- Cass. Soc. 2 octobre 2024 n° 23-12.844 (prescription)
- Service-public.fr non-compete clause overview
- DWF, Key Considerations for Employers in France (2022)
- Dechert, Restrictive Covenant Clauses Q&A France (2021)

All citations carry hallucination risk and require verification on légifrance.gouv.fr.
This skill routes to and from `legalcode-non-compete-analysis` (cross-jurisdictional
router) for France-specific deep analysis. For cross-jurisdictional non-compete
comparison, use the router skill.
