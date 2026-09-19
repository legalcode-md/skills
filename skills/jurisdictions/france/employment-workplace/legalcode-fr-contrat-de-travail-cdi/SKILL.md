---
name: legalcode-fr-contrat-de-travail-cdi
description: Draft or review a French CDI (contrat de travail à durée indéterminée — permanent employment
  contract) for an employer or employee in France. Use when drafting a new CDI, reviewing an existing
  French employment contract, advising on enforceability of restrictive covenants, assessing compliance
  with Code du travail mandatory provisions, or preparing for termination.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft or review a French CDI (contrat de travail à durée indéterminée — permanent employment contract) for an employer or employee in France. Covers all mandatory clauses under the Code du travail, convention collective alignment (Syntec IDCC 1486, Métallurgie IDCC 3248, and major sector CCNs), non-compete clause (clause de non-concurrence) validity and mandatory financial compensation, mobility clauses (clause de mobilité), intellectual property assignment and employee inventions (Art. L113-9 / L611-7 Code de la propriété intellectuelle), forfait jours for autonomous executives, telework (télétravail) provisions, RGPD/CNIL employee data clause, probationary period (période d'essai) rules, termination (licenciement) procedure and Barème Macron, and rupture conventionnelle. Use when drafting a new CDI, reviewing an existing French employment contract, advising on enforceability of restrictive covenants, assessing compliance with Code du travail mandatory provisions, or preparing for termination. France-specific skill; not for CDD, interim, or non-French employment.


# Legalcode — Contrat de Travail CDI (France)

> **Avertissement / Disclaimer**: Ce skill fournit un cadre pour l'assistance juridique par IA
> en matière de droit du travail français. Il ne constitue pas un conseil juridique. Toutes les
> sorties doivent être examinées par un avocat qualifié en droit du travail français ou un
> conseil en ressources humaines habilité avant toute utilisation. Le droit du travail français
> évolue rapidement — vérifiez l'applicabilité actuelle des dispositions citées. Les références
> aux articles de loi et à la jurisprudence provenant de la mémoire entraînent un risque
> d'hallucination — vérifiez sur légifrance.gouv.fr avant de vous y fier.
>
> **Disclaimer**: This skill provides a framework for AI-assisted French employment law work.
> It does not constitute legal advice. All outputs must be reviewed by a qualified French
> employment lawyer (avocat en droit du travail) or authorized HR counsel before use. French
> labour law changes frequently — verify current applicability of all provisions cited. Statutory
> and case law references cited from memory carry hallucination risk — verify against
> légifrance.gouv.fr before relying on them.

---

## Purpose and Scope

This skill enables an AI agent to **draft and review** French CDI employment contracts
(contrats de travail à durée indéterminée — permanent employment contracts) on behalf of
employers or employees.

**Covers:**

- Drafting a complete CDI from scratch, including all mandatory clauses (clauses obligatoires)
- Reviewing an existing CDI for compliance with Code du travail, applicable CCN, and CNIL/RGPD
- Clause-by-clause analysis with GREEN / YELLOW / RED severity classification
- Convention collective alignment — identifying the applicable CCN and checking consistency
- Restrictive covenant validity — non-compete (clause de non-concurrence), mobility clause
- IP assignment analysis — employee works under CPI Art. L113-9 (software) and L611-7 (inventions)
- Working time regime — 35h, RTT, forfait jours (autonomous executives)
- Télétravail / remote work provisions under Art. L1222-9 and ANI 2020
- RGPD / CNIL data protection clause for employees
- Probationary period (période d'essai) — validity, renewal, and termination notice
- Termination analysis — licenciement procedure, indemnités, Barème Macron (Art. L1235-3)
- Rupture conventionnelle — homologation, indemnité spécifique, new 40% employer contribution
- Redline generation with alternative model language
- Glass Box audit trail for traceability

**Does not:**

- Cover CDD (contrat à durée déterminée), interim, or CDI de chantier/d'opération in full depth
- Apply to non-French employment relationships
- Constitute a legal opinion on any specific situation
- Replace qualified French employment counsel

---

## Jurisdiction and Governing Law

**Jurisdiction: France (métropole and DOM-TOM).**

The CDI is governed by the **Code du travail** (Labour Code), supplemented by the applicable
**convention collective nationale (CCN)** for the employer's sector. The Code du travail sets
the statutory floor — CCN provisions can improve (améliorer) statutory minimums but cannot
fall below them (principe de faveur — Art. L2251-1).

**Key governing texts:**

- **Code du travail** — Art. L1211-1 et seq. (employment contract framework)
- **Code de la propriété intellectuelle (CPI)** — Art. L113-9 (employee software), L611-7
  (employee inventions)
- **RGPD** (Règlement (UE) 2016/679) + **Loi Informatique et Libertés** (as amended by
  Loi n°2018-493)
- **Accord National Interprofessionnel (ANI) du 26 novembre 2020** (télétravail)
- **Loi n°2022-1598 du 21 décembre 2022** (marché du travail — abandon de poste, CDI refusal)
- **Loi n°2023-1107 du 29 novembre 2023** (partage de la valeur)
- **LFSS 2026** — increased contribution patronale on rupture conventionnelle (30% → 40%)

The contract must be drafted in **French** (Art. L1221-3 Code du travail). If a function
title has no French equivalent, it must be explained in French.

**Primary court:** Conseil de prud'hommes (CPH) — labour tribunal for individual disputes.
Appeal: Cour d'appel, then Cour de cassation (Chambre sociale).

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at key decision points where the
user's context materially changes the analysis or drafting direction. The skill pauses and
asks when:

- The answer would change which CCN applies or which clauses are mandatory
- The working time regime (35h / forfait heures / forfait jours) must be chosen
- The employee's classification (ETAM vs. IC, cadre status) is unclear
- A restrictive covenant requires employer-side or employee-side analysis
- A termination scenario requires specific procedure selection

If the user has already supplied the information, skip the question and proceed. For
batch/non-interactive runs, state the assumption explicitly and flag it for human review.

---

## Workflow

### Step 1: Accept Input

Accept the task in any of these formats:

- **Draft mode**: User describes the employment relationship and wants a CDI drafted
- **Review mode**: User provides an existing CDI (PDF, DOCX, or pasted text) for analysis
- **Clause mode**: User wants analysis or drafting of one specific clause (e.g., non-compete,
  forfait jours, termination procedure)
- **Termination mode**: User describes a dismissal or rupture conventionnelle scenario

Determine the operating mode and confirm with the user before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, gather context. Present these as structured options where
possible:

**For any mode:**

1. **Employer perspective or employee perspective?**
   - Options: Employer (drafting or reviewing as the company), Employee (reviewing as the
     employee or their representative), Neutral (balanced analysis for both sides)
   - _Why this matters_: Determines which deviations are flagged as risks and the tone of
     redline recommendations.

2. **Employee category (catégorie professionnelle):**
   - Options: Ouvrier/Employé, Agent de maîtrise/Technicien (AMT), Cadre (IC/Ingénieur et
     Cadre), Cadre dirigeant (Art. L3111-2), Unsure — determine from job title
   - _Why this matters_: Sets the applicable probationary period maximums, notice periods,
     overtime regime, and forfait jours eligibility.

3. **Applicable convention collective (CCN):**
   - Options: Syntec-Cinov (IDCC 1486 — IT, engineering, consulting), Nouvelle Métallurgie
     (IDCC 3248 — manufacturing, automotive, aerospace), Other known CCN (specify IDCC code),
     Unknown — help me identify it from the NAF/APE code
   - _Why this matters_: The CCN governs minimum salary, classification, trial period renewal
     permission, forfait jours eligibility, and notice periods.

4. **Working time regime:**
   - Options: 35h/week (standard), Forfait heures (executive fixed weekly hours), Forfait
     jours (autonomous executive flat-rate days — 218 max), Cadre dirigeant (exempt from all
     working time rules), Unknown — determine from the contract
   - _Why this matters_: Forfait jours requires specific CCN authorization and individual
     written agreement, both of which can be null if improperly structured.

5. **Focus areas** (allow multiple selections):
   - Mandatory clauses compliance | Non-compete validity | IP assignment | Forfait jours
     validity | Termination procedure | Rupture conventionnelle | Télétravail provisions |
     RGPD/CNIL compliance | Full review
   - _Why this matters_: Lets the analysis lead with what the user cares about most.

### Step 3: Identify the Applicable Convention Collective

Identify or confirm the applicable CCN before proceeding. The CCN is the single most
important jurisdictional variable for a French CDI — it governs up to a dozen critical
parameters.

**Identification method:**

1. Look for the CCN reference on the existing contract (mandatory on pay slips, Art. L3243-2;
   typically also on the contract itself)
2. Identify the employer's NAF/APE code (look it up on the SIRET certificate or legal notices)
3. Cross-reference using the Code du travail numérique (codetravail.fr) or CNDT tool
4. Confirm by reading the CCN's champ d'application (scope clause)

**⟁ CLARIFY** — If the CCN cannot be identified:

- Ask the user for the employer's NAF/APE code or primary activity
- Present the top 3-4 candidate CCNs most likely to apply to that activity
- Flag that CCN misidentification is a common and material error

**Key CCNs with special drafting requirements:**

| CCN                          | IDCC | Key CDI Provisions                                                                                                                                                          |
| ---------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Syntec-Cinov**             | 1486 | ETAM/IC classification grid; forfait jours from position IC 2.3 (effective 1 July 2024); generous notice periods (up to 3 months cadres); mandatory coefficient in contract |
| **Nouvelle Métallurgie**     | 3248 | New unified CCN (effective 1 Jan 2024, replaced ~70 legacy CCNs); new job evaluation classification (cotation des emplois); min €300 mission invention bonus                |
| **Commerce de gros**         | 573  | Standard provisions                                                                                                                                                         |
| **BTP Ouvriers**             | 1596 | CDI de chantier usage; specific working time rules                                                                                                                          |
| **BTP ETAM**                 | 1597 | Distinct from ouvriers; specific classification                                                                                                                             |
| **Commerce et distribution** | 2216 | Sunday work; specific notice periods                                                                                                                                        |
| **Banque**                   | 2120 | Specific classification grid; strong notice periods                                                                                                                         |

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to retrieve current legal authority on the specific issues raised:

**Recommended searches:**

- `CDI contrat travail clauses obligatoires France`
- `clause non-concurrence conditions validité contrepartie financière`
- `forfait jours cadres autonomes conditions validité 2024`
- `rupture conventionnelle contribution patronale 2026`
- `période d'essai renouvellement conditions CDI`
- `Barème Macron licenciement sans cause réelle sérieuse`

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the legal authority embedded in this skill, but flag that it requires
  verification against légifrance.gouv.fr

### Step 5: Clause-by-Clause Analysis

Analyze the CDI systematically across all 14 clause categories. Read the entire contract
before flagging issues — clauses interact (e.g., a broad IP clause combined with a missing
inventions clause creates compound risk).

**⟁ CLARIFY** — For a comprehensive review of a long CDI (20+ articles), ask whether to
perform a **full review** of all 14 categories or a **priority review** focused on the user's
stated focus areas plus any RED items discovered.

| #   | Clause Category                | Depth    | Key Review Points                                                                |
| --- | ------------------------------ | -------- | -------------------------------------------------------------------------------- |
| 1   | Parties and Contract Formation | Deep     | French-language requirement, legal entity identification, employee full identity |
| 2   | Classification and CCN         | Deep     | Coefficient/position accuracy, CCN reference, minimum salary compliance          |
| 3   | Remuneration                   | Deep     | SMIC floor, CCN minimum, variable pay structure, primes legality                 |
| 4   | Probationary Period            | Deep     | Duration vs. legal/CCN maximum, renewal conditions, termination notice           |
| 5   | Working Time                   | Deep     | 35h / forfait heures / forfait jours validity, RTT, contingent heures supp.      |
| 6   | Non-Compete Clause             | Deep     | Five cumulative validity conditions, financial compensation adequacy, waiver     |
| 7   | Mobility Clause                | Deep     | Geographic precision, private/family life proportionality, notice                |
| 8   | IP Assignment                  | Deep     | Software L113-9, inventions L611-7 (mission/attribuable/libre), moral rights     |
| 9   | Télétravail / Remote Work      | Standard | Voluntary nature, equipment/cost reimbursement, right to disconnect              |
| 10  | RGPD / Data Protection         | Standard | Art. 13 transparency, retention periods, data processed, employee rights         |
| 11  | Termination and Notice         | Standard | Statutory notice (Art. L1234-1), CCN notice, indemnité légale calculation        |
| 12  | Confidentiality                | Standard | Scope, duration, relationship to non-compete                                     |
| 13  | Specific Obligations           | Standard | Exclusivity, secondary activity, training repayment (clause de dédit-formation)  |
| 14  | Boilerplate                    | Standard | Severability, amendment, entire agreement, governing law, dispute resolution     |

---

## Deep Clause Analysis

### Category 1: Parties and Contract Formation

**Mandatory requirements:**

| Requirement                             | Legal Basis       | Risk if Missing/Wrong                                                                  |
| --------------------------------------- | ----------------- | -------------------------------------------------------------------------------------- |
| Contract drafted in French              | Art. L1221-3      | Risk of contract being challenged; employee can demand French version at any time      |
| Employer legal entity name + SIRET      | Practice standard | Identity of contracting employer critical for enforcement                              |
| Employee full name, date/place of birth | Practice standard | Required for social security and payroll                                               |
| Start date (date d'entrée en poste)     | Art. L1221-1      | Seniority calculation anchored to start date                                           |
| Part-time CDI: written form mandatory   | Art. L3123-6      | Absence of writing → rebuttable presumption of full-time status; employer bears burden |

**For part-time CDI additionally:**

- Exact weekly or monthly working hours
- Distribution of hours across days of the week or weeks of the month
- Circumstances permitting modification of distribution
- Limits for heures complémentaires (additional hours)

**Severity:** Missing written contract for part-time → **RED** (legal presumption of full-time
status). Missing writing for full-time CDI → **YELLOW** (oral contracts are technically valid
but create evidentiary risk; all major CCNs require writing in practice).

---

### Category 2: Classification and Convention Collective

**Mandatory CCN reference:** The applicable CCN must be identified in the contract (and on
pay slips per Art. L3243-2). An incorrect CCN reference is a material defect.

**Classification accuracy:** The employee's classification (coefficient, position, emploi group)
must match their actual functions. An inflated classification creates wage obligations; an
understated classification creates backdated salary claims.

**For Syntec (IDCC 1486):**

| Status                    | Positions  | Coefficients (approx.) |
| ------------------------- | ---------- | ---------------------- |
| ETAM                      | 1.1 to 3.3 | 200–400                |
| IC (Ingénieurs et Cadres) | 1.1 to 3.3 | 85–270                 |

The coefficient must appear on the employment contract (Syntec CCN requirement). A Syntec
contract missing the coefficient is defective.

**For Nouvelle Métallurgie (IDCC 3248, effective 1 January 2024):**

- No longer uses the old coefficient system
- Uses a job evaluation methodology (cotation des emplois) resulting in an emploi group (A–N)
  and class within that group
- Transposition table from old coefficients does NOT exist; new evaluation must be performed
- Contracts referencing old CCN structure (e.g., IDCC 1938 or legacy territorial metal CCNs)
  for employees in scope of the new CCN require updating

**Severity:** Wrong CCN → **RED** (risk of mandatory provision non-compliance, salary
shortfalls). Wrong classification → **YELLOW** to **RED** depending on direction of error.

---

### Category 3: Remuneration

**SMIC floor (2026):**

- Monthly gross (35h/week): **€1,823.03**
- Hourly rate: **€12.02 gross**
- Any salary below the SMIC is null and void — the SMIC applies automatically

**CCN minimum salaries:** The SMIC always takes precedence over CCN minimums where the CCN
minimum is lower. Verify both:

1. CCN minimum for the stated classification (varies by CCN, position, and year)
2. SMIC floor

**Variable pay (part variable, primes, bonus):**

- Variable pay terms must be clear on the basis of calculation, triggering conditions, and
  payment frequency
- An employer cannot unilaterally reduce or eliminate a variable component that is part of
  the agreed remuneration structure
- Performance bonuses agreed contractually = part of remuneration = cannot be removed without
  employee consent
- Discretionary bonuses (not contractually defined) can be modified or removed; they must
  be genuinely discretionary

**Clause de dédit-formation (training repayment):**

- An employer may require repayment of significant training costs if the employee leaves
  within a defined period
- Requirements for validity (Cour de cassation):
  - Cost must be real and significant (not routine or legally mandatory training)
  - Time period and amount must be proportionate
  - Employee must have signed a specific written agreement at the time of the training
- Maximum repayment amount must decrease proportionally over time
- **Cannot be used for** training that is legally mandatory for the role (e.g., habilitation
  électrique, CACES) — those costs cannot be charged back

**Severity:** Salary below SMIC → **RED** (automatic statutory top-up; potential criminal
sanctions for employer). Ambiguous variable pay → **YELLOW**. Invalid dédit-formation →
**YELLOW** (clause unenforceable but contract remains valid).

---

### Category 4: Probationary Period (Période d'Essai)

**Statutory maximums (Art. L1221-19):**

| Employee Category                | Initial Maximum | Maximum with Renewal |
| -------------------------------- | --------------- | -------------------- |
| Ouvriers / Employés              | 2 months        | 4 months             |
| Agents de maîtrise / Techniciens | 3 months        | 6 months             |
| Cadres                           | 4 months        | 8 months             |

**Renewal conditions (both must be met):**

1. A **branch-level extended collective agreement** (accord de branche étendu) expressly
   authorizes renewal for the relevant employee category
2. The employment contract or offer letter expressly provides for the possibility of renewal
   AND the employee gives **explicit written consent to the renewal during the initial period**
   (before it expires)

**Prior employment deduction:** If the employee worked for the employer previously under a
CDD or interim mission for the same role, that prior period must be deducted from the trial
period (Art. L1221-21 and L1251-36).

**Termination during trial — notice periods (Art. L1221-25):**

| Duration of Trial Completed | Notice by Employer |
| --------------------------- | ------------------ |
| < 8 days                    | 24 hours           |
| 8 days to 1 month           | 48 hours           |
| 1 month to 3 months         | 2 weeks            |
| > 3 months                  | 1 month            |

| Duration of Trial Completed | Notice by Employee |
| --------------------------- | ------------------ |
| < 8 days                    | 24 hours           |
| ≥ 8 days                    | 48 hours           |

**Critical drafting requirements:**

- Trial period and possibility of renewal are not presumed — must be **expressly stipulated**
  in the letter of engagement or contract (Art. L1221-23)
- A trial period agreed only verbally → null and void → employee is deemed permanent from day 1
- Renewal without written employee consent during the initial period → renewal is null and void

**Severity:** Trial period exceeding statutory maximum → **RED** (excess period null, but
employment continues). Renewal without written consent → **RED** (renewal null; termination
during "renewal" treated as dismissal without cause). Missing express stipulation → **RED**
(no enforceable trial period).

---

### Category 5: Working Time Regime

#### Standard 35-hour regime

**Legal working time:** 35 hours/week (Art. L3121-27).

**Overtime (heures supplémentaires — Art. L3121-28 et seq.):**

- Hours 36–43 (first 8 overtime hours): +25% supplement
- Hours 44+ (from 9th overtime hour): +50% supplement
- By company or branch agreement: rates can be reduced to a minimum of 10%
- Annual statutory contingent: **220 hours** (absent CCN/company agreement)
- Hours beyond contingent trigger mandatory compensatory rest (repos compensateur de
  remplacement): 50% for ≤20 employees; 100% for >20 employees

**RTT (Réduction du Temps de Travail):** Applicable when actual working time exceeds 35h but
falls below the overtime threshold; excess is compensated as RTT days off.

#### Forfait Jours (Art. L3121-58 to L3121-66)

**Who is eligible:**

- Cadres with genuine autonomy in organizing their working time whose functions do not require
  following collective working hours (Art. L3121-58 1°)
- Non-executive employees whose working time cannot be predetermined (Art. L3121-58 2°)
  [rare in practice]

**Three cumulative conditions for validity:**

1. **CCN/company agreement authorization:** A branch-level or company-level collective
   agreement must authorize the forfait jours regime AND define: eligible employee categories,
   maximum number of days, rest periods, workload monitoring procedures, annual review
   mechanism, right to disconnect modalities
2. **Individual written convention de forfait:** The individual agreement cannot be implied;
   it must be an explicit written clause in the employment contract or a signed amendment
3. **Maximum 218 days/year** (Art. L3121-64): CCN/company agreement may set a lower cap

**Mandatory employer obligations (Art. L3121-65) — failure renders the forfait null:**

- Control document showing the number and dates of days worked (and half-days)
- Ensure workload compatibility with daily rest (minimum 11h) and weekly rest (minimum 35h)
- Annual entretien (review meeting) on workload, work/life balance, remuneration, and right
  to disconnect

**Syntec-specific (avenant 13 December 2022, effective 1 July 2024):**

- Eligible from position IC 2.3 (previously only IC position 3 and above)
- Minimum remuneration for IC 2.3 on forfait jours: **122% of the IC 2.3 CCN minimum**
- Annual entretien: one per year (previously two)
- Companies >250 employees: must designate a "référent à la déconnexion"

**Cadre dirigeant (Art. L3111-2):**
Three cumulative criteria (courts scrutinize strictly; mere title insufficient):

1. Major independent responsibility
2. Autonomous decision-making authority
3. Highest-level remuneration in the company/establishment

Cadres dirigeants are exempt from ALL working time rules (35h, overtime, rest periods,
forfait jours requirements). Misclassification as cadre dirigeant → all working time rules
apply retroactively.

**Severity:** Forfait jours without valid CCN authorization → **RED** (forfait null; retroactive
overtime claims from 35th hour for full contract duration — massive exposure). Forfait jours
without individual written convention → **RED** (same consequence). Missing annual entretien
or monitoring → **RED** (Cour de cassation 10 janvier 2024: forfait nullity). Cadre dirigeant
misclassification → **RED**.

---

### Category 6: Non-Compete Clause (Clause de Non-Concurrence)

**Five cumulative conditions for validity** (Cour de cassation, Chambre sociale, 10 juillet
2002, n°99-43.334 and n°99-43.135):

| Condition                                                         | Required Standard                                                                                                                    | Common Defect                                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| 1. Protection of legitimate business interests                    | Must be necessary and proportionate to a real risk (access to strategic information, client relationships, trade secrets)            | Generic clause not linked to employee's actual access                               |
| 2. Limited in time                                                | Typically 6–24 months; no statutory maximum but disproportionate durations voided                                                    | Duration not specified or excessive                                                 |
| 3. Limited in geographic scope                                    | Must reflect the actual geographic reach of the company's business; must be precisely defined                                        | "All of France" without justification; "worldwide" without genuine global operation |
| 4. Limited in scope of activity                                   | Defined by reference to the employee's actual functions; not the entire industry                                                     | Clause prohibiting all commercial activity in a broad sector                        |
| 5. **Mandatory financial compensation (contrepartie financière)** | Must be real, serious, and not derisory; in practice 20–50% of last monthly gross salary; paid monthly throughout restriction period | Zero compensation = automatic nullity; < ~20% = risk of "dérisoire" finding         |

**Critical rules on contrepartie financière:**

- **Derisory threshold:** Cour de cassation has voided clauses with compensation below
  approximately 20% of the last monthly salary — treat anything below 25% as at-risk
- **Payment mechanism:** Paid monthly throughout the restriction period AFTER departure
  (not as a lump sum upon signing)
- **Cannot be offset** against severance pay or other indemnities

**Waiver (renonciation) by employer:**

- The contract or CCN must expressly grant the employer the right to waive
- Waiver must be **express, unequivocal, and individually notified** to the employee
- **Timing is critical:** Waiver must occur by the date of effective departure; a clause
  permitting waiver "at any time during the restriction period" is void (leaves the employee
  in permanent uncertainty)
- If the employee is relieved of notice (dispensé de préavis), waiver must occur at the
  moment of the dispense

**2024 case law developments:**

- **Cour de cassation, 24 janvier 2024:** Employee's breach of a non-compete clause, even
  temporary, releases the employer from the obligation to pay the contrepartie financière —
  even after the breach has ended
- **Invalidity rate:** 61% of contested non-compete clauses declared null/void in 2024 court
  proceedings (up from 48% in 2023); judicial scrutiny is intensifying

**Drafting guidance (employer side):**

- Tailor the clause precisely to the employee's actual functions and genuine competitive risks
- Set compensation at 30–50% of gross monthly salary to provide clear headroom above the
  "dérisoire" threshold
- Define the geographic scope by reference to specific countries/regions
- Grant the employer a waiver right with a defined notice period (e.g., 15 days after
  notification of termination)
- Match the duration to the actual competitive risk (12 months standard for most commercial
  roles; 24 months for senior executives with strategic knowledge)

**Severity:** No contrepartie financière → **RED** (clause null and void; employee can compete
immediately). Derisory contrepartie (< ~20%) → **RED** (risk of nullity). Missing waiver
right → **YELLOW** (employer locked into paying even when departing employee poses no real
risk). Imprecise geographic scope → **RED** (clause null; unenforceability).

---

### Category 7: Mobility Clause (Clause de Mobilité)

**Validity requirements (Cour de cassation):**

| Requirement                            | Standard                                                                                                                                            | Consequence of Failure                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Sufficient geographic precision        | Zone must be defined clearly; "all subsidiaries" without geographic boundary → void                                                                 | Clause null; refusal to move = unfair dismissal if employer relies on it                               |
| Proportionality to private/family life | Activation must not disproportionately affect employee's private and family life (Art. 8 ECHR; Cour de cassation Soc. 14 février 2018, n°16-23.042) | Dismissal for refusal = without cause réelle et sérieuse                                               |
| No unilateral expansion                | Cannot grant the employer the right to expand the zone beyond what was stipulated                                                                   | Expansion null; new location outside zone must be treated as a modification requiring employee consent |

**Implementation notice:**

- No fixed statutory notice period; assessed case-by-case
- Factors: distance, seniority, family situation (children, spouse employment), duration of
  relocation, whether accommodation assistance is provided

**Employee's right to refuse:**

- Refusal to implement a valid mobility clause generally justifies dismissal for personal
  reasons (motif personnel)
- BUT dismissal of an employee whose refusal is based on legitimate private/family life
  reasons can be found without cause réelle et sérieuse — even if the clause is technically
  valid
- Example upheld by Cour de cassation: Lyon-based employee with two young children forced
  to work in Lille 5 days/week for 4 months → refusal justified → dismissal unfair

**Severity:** Geographically imprecise clause → **RED** (null; employer cannot enforce).
Activation without adequate notice for family situation → **YELLOW/RED** depending on
circumstances. Missing proportionality analysis in drafting → **YELLOW** (enforcement risk).

---

### Category 8: Intellectual Property Assignment

#### 8A — Copyright (Droit d'Auteur)

**Software — Art. L113-9 CPI (automatic employer ownership):**

- Software created by an employee **in the exercise of their functions** or **according to
  employer instructions** automatically vests in the employer — no assignment clause required
  for software
- Exception to the general copyright rule (which vests rights in the human creator)
- **Droit moral (moral rights)** — inalienable; remains with the employee; cannot be waived
  or transferred by contract under any circumstances

**Other works (articles, designs, artistic works — general rule):**

- Rights do NOT automatically transfer to the employer
- Assignment must be express and specific (Art. L131-3 CPI): must identify each category of
  rights assigned (reproduction, representation, adaptation), the territory, and the duration
- A blanket "all works created during employment" clause → too general → void for non-software
  works

**Drafting guidance for non-software creative works:**

```
"L'employé cède à l'employeur, de manière exclusive et à titre gratuit (inclus dans
la rémunération), les droits patrimoniaux suivants sur les œuvres créées dans le cadre
de ses fonctions ou selon les instructions de l'employeur:
(i) le droit de reproduction sur tout support connu ou à connaître;
(ii) le droit de représentation par tout procédé de communication au public;
(iii) le droit d'adaptation, de traduction, d'arrangement;
pour la durée légale de protection et pour le monde entier."
```

#### 8B — Employee Inventions (Art. L611-7 CPI)

**Three categories — employer/employee ownership depends on category:**

| Category                                                                                   | French Term                                  | Ownership                                                                                       | Compensation                                                                                                                     |
| ------------------------------------------------------------------------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Inventions made in execution of an inventive mission or R&D tasks explicitly assigned      | **Inventions de mission**                    | Employer (automatic)                                                                            | Mandatory supplementary remuneration (rémunération supplémentaire) — now minimum €300 under Nouvelle Métallurgie CCN (IDCC 3248) |
| Made outside the mission but using company resources, knowledge, or in the company's field | **Inventions hors mission attribuables**     | Employee initially, but employer may claim by request within 4 months of employee's declaration | "Prix équitable" — negotiated or determined by INPI's Commission Nationale des Inventions de Salariés (CNIS)                     |
| Made outside the mission, without company resources, outside the company's field           | **Inventions hors mission non attribuables** | Employee entirely                                                                               | None                                                                                                                             |

**Declaration obligation:** Employees must declare inventions to the employer; employer has
**4 months** from receipt of declaration to claim ownership of attribuable non-mission
inventions.

**Drafting guidance:** The contract should:

- Confirm the mission invention rule (employer ownership + supplementary remuneration)
- Include an obligation to declare all inventions (mission and non-mission) promptly
- Specify the supplementary remuneration formula (or reference the CCN provision)
- Carve out pre-existing employee IP (background IP) from the assignment

**Severity:** Missing supplementary remuneration commitment for mission inventions → **YELLOW/
RED** (statutory right cannot be waived; liability for retroactive payment). Clause attempting
to assign "all inventions" including hors mission non attribuables → **RED** (void; employee
owns those inventions despite the clause).

---

### Category 9: Télétravail / Remote Work

**Legal framework:** Art. L1222-9 to L1222-11 Code du travail; ANI du 26 novembre 2020.

**Voluntary nature:** Télétravail is voluntary for both parties. An employer cannot impose
télétravail (except in exceptional circumstances recognized by public authorities) and an
employee cannot claim an absolute right to télétravail absent an applicable company agreement.

**Implementation options (hierarchical):**

1. Collective agreement (accord collectif) — preferred
2. Employer charter (charte) after CSE consultation
3. Individual agreement "by any means" (par tout moyen) — minimum but riskier

**Mandatory employer obligations:**

| Obligation                                                | Source                                                                                                      |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Inform employee of any restrictions on IT equipment       | Art. L1222-9                                                                                                |
| Priority access for teleworkers wishing to return on-site | Art. L1222-9                                                                                                |
| Annual review meeting on working conditions and workload  | Art. L1222-10                                                                                               |
| Cover costs directly related to télétravail               | ANI 2005 / ANI 2020 (URSSAF flat rate: €10.70/month for 1 day/week telework in 2025; scales proportionally) |
| Provide or reimburse necessary equipment                  | ANI 2020                                                                                                    |
| Respect employee's private life                           | General obligation                                                                                          |

**Droit à la déconnexion (right to disconnect — Art. L2242-17):**

- Companies with union representatives: mandatory annual negotiation on right to disconnect
- Absence of agreement: unilateral employer charter after CSE consultation required
- Syntec 2024 (>250 employees): mandatory "référent à la déconnexion"
- Violation: criminal penalty (1 year imprisonment + €3,750 fine for the responsible manager)

**Severity:** Télétravail imposed unilaterally by employer → **RED** (modification of contract
terms requiring employee consent). Missing cost reimbursement → **YELLOW** (URSSAF compliance
risk + employee claim). No right-to-disconnect protocol → **YELLOW/RED** depending on company
size and CSE situation.

---

### Category 10: RGPD / Data Protection (CNIL)

**Legal basis:** RGPD Art. 13 (information obligation to data subjects) + Loi Informatique et
Libertés (amended 2018).

**Employment contract RGPD clause — what must be disclosed:**

| Element                      | Content                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Identity of data controller  | Employer legal entity + DPO contact if applicable                                                                    |
| Purposes of processing       | Payroll, benefits administration, time management, access control, performance management                            |
| Legal basis for each purpose | Contract performance, legal obligation, legitimate interest (Art. 6 RGPD)                                            |
| Retention periods            | Payroll records: 5 years (Urssaf audits); disciplinary records: 5 years max; monitoring data: 3 months max typically |
| Recipients                   | HR, payroll providers, health insurance, pension funds, regulatory authorities                                       |
| Employee rights              | Access, rectification, portability, erasure (limited in employment context), restriction, objection                  |
| Right to lodge a complaint   | CNIL (cnil.fr)                                                                                                       |

**Sensitive data rules:**

- Trade union membership, political opinions, religious beliefs, health data, ethnic/racial origin
  = special category data requiring specific legal basis (Art. 9 RGPD)
- An employer **cannot** collect or process these categories in the recruitment or employment
  context without specific legal authorization
- **Biometric data** (fingerprint, iris scanning) for time attendance: requires CNIL-recognized
  legal basis; subject to DPIA; must be disclosed to CSE

**Employee monitoring:**

- Any monitoring tool (computer surveillance, GPS, keyloggers) must be: disclosed to employees
  BEFORE implementation, subject to CSE information-consultation, proportionate, and time-limited
- Secret surveillance of employees = violation of Art. 9 of French Civil Code (right to privacy)
  - RGPD — evidence obtained by secret monitoring is inadmissible in proceedings

**Severity:** Missing RGPD clause entirely → **RED** (CNIL sanction risk; employee information
right violation). Collection of prohibited sensitive data in recruitment/contract → **RED**
(CNIL fine up to €20M or 4% global turnover + discrimination claim risk). Secret monitoring →
**RED** (inadmissible evidence + criminal exposure).

---

### Category 11: Termination and Notice

#### Pre-termination Procedure (Licenciement)

**Entretien préalable (Art. L1232-2 to L1232-4):**

| Step                         | Requirement                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1. Convocation               | By registered letter (LR/AR) or hand-delivered receipt; must state the purpose                                              |
| 2. Notice period             | Minimum 5 ouvrables working days between receipt and interview                                                              |
| 3. Employee assistance       | Employee may bring a colleague or (absent employee representatives) a salarié conseiller from the official prefectural list |
| 4. Notification of dismissal | Minimum 2 working days after interview; maximum 1 month after interview for disciplinary dismissal                          |
| 5. Letter of dismissal       | Must state specific reasons (Art. L1232-6); vague letters can be challenged for form defect                                 |

**Notice periods (préavis — Art. L1234-1 statutory minimums):**

| Seniority           | Minimum Notice             |
| ------------------- | -------------------------- |
| < 6 months          | Determined by CCN or usage |
| 6 months to 2 years | 1 month                    |
| ≥ 2 years           | 2 months                   |

CCN provisions are frequently more generous (e.g., Syntec: up to 3 months for cadres). The
more favorable provision (CCN or statutory) applies.

**Indemnité légale de licenciement (Art. R1234-1, R1234-2, R1234-4):**

- Triggered from **8 months** continuous seniority
- Rate: **¼ month/year** for years 1–10; **⅓ month/year** from year 11 onwards
- Reference salary: higher of (1) 1/12 of last 12 months' remuneration; or (2) 1/3 of last
  3 months' remuneration

_Example:_ Employee with 12 years' seniority → (10 × ¼) + (2 × ⅓) = 2.5 + 0.667 = **3.17
months** of reference salary minimum.

CCN indemnités may be higher and apply if more favorable.

#### Barème Macron (Art. L1235-3 — Dismissal Without Cause Réelle et Sérieuse)

| Ancienneté | Floor (≥11 employees) | Ceiling (≥11 employees) | Floor (<11 employees) |
| ---------- | --------------------- | ----------------------- | --------------------- |
| 1 year     | 1 month               | 1 month                 | 0.5 month             |
| 2 years    | 3 months              | 3.5 months              | 0.5 month             |
| 5 years    | 3 months              | 6 months                | 1.5 months            |
| 10 years   | 3 months              | 10 months               | 2.5 months            |
| 20 years   | 3 months              | 15.5 months             | 2.5 months            |
| 30 years   | 3 months              | 20 months               | 2.5 months            |

**Constitutional status:** Fully validated by Cour de cassation, Assemblée plénière,
11 mai 2022 — binding on all prud'hommes courts. Cour de cassation 29 avril 2025: for
employees with ≥11 years seniority, the standard floor applies regardless of company size.

**Exception — discriminatory dismissal (licenciement nul):** The Barème Macron does NOT
apply to dismissals declared null on discrimination grounds or in violation of a fundamental
right. For null dismissals: employee may demand reinstatement + full back-pay, or opt for
minimum **6 months' salary** (uncapped, not subject to barème). Far greater exposure for
employer.

**Tax / social exemption:** Indemnités for unfair dismissal exempt from income tax and
social charges up to the barème ceiling AND up to 2 PASS = **€94,200 in 2025** (€97,000
est. for 2026 — [VERIFY]).

---

### Category 12: Rupture Conventionnelle (Art. L1237-11 to L1237-16)

**Key features:**

- Mutual termination of CDI by agreement — exclusive of both dismissal and resignation
- Cannot be imposed by either party (freedom of consent is a condition of homologation)
- Requires at least one meeting (entretien) between parties
- **Cooling-off period:** 15 calendar days from the signature of the convention, during
  which either party may withdraw (rétractation)
- After cooling-off: submission to DREETS via the TéléRC platform by the most diligent party
- **DREETS instruction period:** 15 working days from receipt; silence = homologation acquired
- DREETS refuses if: freedom of consent compromised, minimum indemnity not met, procedural
  irregularity

**Minimum indemnité spécifique:**

- Cannot be less than the indemnité légale de licenciement (¼ month/year up to 10 years;
  ⅓ month/year from year 11)
- If the applicable CCN provides a higher indemnité, the CCN minimum applies

**Tax / social charges:**

- Employee: exempt from income tax up to 2 PASS (€94,200 in 2025); subject to CSG/CRDS
  on the exempt portion; no social charges on exempt portion
- Employee retains right to unemployment benefits (unlike resignation)

**Contribution patronale spécifique (employer forfait social):**

- **CRITICAL 2026 CHANGE:** Raised from 30% to 40% of the tax-exempt portion of the
  indemnité effective **1 January 2026** (LFSS 2026)
- Example impact: indemnité of €50,000 → employer pays an additional €20,000 (vs €15,000
  pre-2026) = net employer cost significantly increased
- Employers signing rupture conventionnelles from 1 January 2026 must budget for the 40%
  rate in HR cost models

**Distinction from accord amiable:** A mutual termination agreement outside Art. L1237-11
lacks homologation protection, minimum indemnity floor, and unemployment benefit entitlement
— courts may requalify it as a dismissal without cause.

**Severity in review:** Missing homologation step → **RED** (rupture null; courts treat as
dismissal without cause). Indemnité below legal minimum → **RED** (DREETS will refuse
homologation). Rupture following a disciplinary procedure without adequate time gap →
**YELLOW/RED** (risk of coerced consent; courts scrutinize the context).

---

## Severity Classification System

**GREEN — Compliant / No Action Required:**

- The clause meets Code du travail requirements, the applicable CCN, and general market
  practice for French CDI contracts
- Note for awareness only; no redline needed

**YELLOW — Should Improve / Negotiate:**

- The clause is technically legal but creates elevated risk or falls below best practice
- Generate alternative language and explain the risk
- Recommend negotiation before signature or correction at next contract update

**RED — Non-Compliant / Must Fix:**

- The clause violates a mandatory Code du travail provision, applicable CCN requirement, RGPD
  obligation, or established Cour de cassation rule
- Automatic triggers (any one of these → RED):
  - Salary below SMIC
  - Non-compete clause without financial compensation
  - Forfait jours without valid CCN authorization or without individual written agreement
  - Trial period exceeding statutory maximum
  - Dismissal letter without stated reasons
  - Biometric data collection without proper legal basis
  - Secret employee monitoring
  - IP clause attempting to waive moral rights
  - Rupture conventionnelle without homologation
  - Non-compete waiver clause that can be exercised during the restriction period

**CRITICAL — Immediate Legal Action Required:**

- The defect creates immediate or imminent legal liability that cannot be remedied by
  contract amendment alone
- Triggers: Discrimination claim elements (dismissal referencing protected characteristic);
  ongoing unlawful monitoring; salary below SMIC being actively paid

---

## Prioritization Framework

### Tier 1 — Address Immediately (Before Signature / Before First Pay Period)

Must-fix items that render the contract or specific clauses void, create mandatory statutory
obligations, or create immediate criminal/administrative liability:

- SMIC compliance
- Mandatory CCN provisions
- Non-compete financial compensation
- Forfait jours CCN authorization
- Part-time CDI written form

### Tier 2 — Address Before Dispute Arises (Within 30 Days)

Should-fix items that create meaningful litigation risk but do not render the contract null:

- Mobility clause geographic precision
- IP assignment clause for non-software works
- RGPD / CNIL transparency clause
- Variable pay formula clarity
- Trial period renewal conditions

### Tier 3 — Address at Next Contract Review (Within 90 Days)

Nice-to-fix items that represent best practice improvements or emerging risks:

- Télétravail cost reimbursement protocol
- Right-to-disconnect policy reference
- Training repayment (dédit-formation) proportionality check
- Update CCN reference for Nouvelle Métallurgie contracts

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivery.

| Gate           | Rule                                                                                                                                                   | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Source**     | Every legal claim cites a specific Code du travail article, CPI article, CCN reference, or Cour de cassation decision                                  | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow a consistent French legal citation format (Art. L1234-1 Cdt, Cass. Soc., 10 juill. 2002, n°99-43.334)                             | Fix format                          |
| **Currency**   | Every cited provision checked against légifrance.gouv.fr for amendments since the research date; 2026 LFSS changes (rupture conventionnelle 40%) noted | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within French law; do not apply UK/US/EU concepts without identifying they are foreign                                                  | Remove or flag domain bleed         |
| **Confidence** | Uncertainty explicitly stated (e.g., CCN salary minimums updated annually; verify current year figures); not hidden                                    | Add confidence qualifier            |

### Self-Interrogation for RED Items

For any RED-classified finding, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity:** Does the finding follow logically from the cited legal
authority? Would a Cour de cassation ruling or conseil de prud'hommes actually reach this
conclusion? Is the Code du travail article cited still in force and applicable to this
specific employment category?

**Pass 2 — Completeness:** Have all relevant sources been considered — Code du travail,
applicable CCN, RGPD, CNIL guidance, recent Cour de cassation decisions, and any sector-
specific regulations? Are there regulatory angles (URSSAF, DREETS, INPI for inventions)
not yet addressed?

**Pass 3 — Challenge:** What is the strongest argument that this clause is actually valid?
Under what circumstances (CCN derogation, company agreement, employee negotiated exception)
might a reasonable employment lawyer accept this clause? State this contra-indicator
explicitly.

### Confidence Scoring

| Level         | Range     | Meaning                                                  | Action                                       |
| ------------- | --------- | -------------------------------------------------------- | -------------------------------------------- |
| **Définitif** | 0.95–1.0  | Settled Cour de cassation doctrine; clear statutory text | State with confidence                        |
| **Élevé**     | 0.80–0.94 | Strong authority; minor interpretive questions           | State with brief caveat                      |
| **Probable**  | 0.60–0.79 | Good arguments; lower courts have split                  | State with reasoning and contra-indicators   |
| **Possible**  | 0.40–0.59 | Genuinely uncertain; CCN interpretation contested        | Flag for avocat review with both sides       |
| **Incertain** | 0.0–0.39  | Weak basis; speculative                                  | Do not assert; flag "[INCERTAIN — VÉRIFIER]" |

---

## Glass Box Audit Trail

Include this YAML block at the end of every output:

```yaml
glass_box:
  skill_name: "legalcode-fr-contrat-de-travail-cdi"
  mode: "[Draft / Review / Clause Analysis / Termination]"
  employee_category: "[Ouvrier-Employé / AMT / Cadre / Cadre dirigeant]"
  convention_collective: "[CCN name and IDCC code, or 'Not identified']"
  working_time_regime: "[35h standard / Forfait heures / Forfait jours / Cadre dirigeant]"
  legalcode_mcp: "[Connected / Not connected — manual verification required]"
  perspective: "[Employer / Employee / Neutral]"
  clauses_analyzed: "[number]"
  red_findings: "[number]"
  yellow_findings: "[number]"
  green_findings: "[number]"
  citations_verified: "[number VERIFIED] / [number [VERIFY] flagged]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  confidence: "[ÉLEVÉ / PROBABLE / POSSIBLE] — [brief rationale]"
  smic_compliance_checked: "[Yes / No]"
  ccn_minimum_compliance_checked: "[Yes / No]"
  non_compete_validity_assessed: "[Yes / No / Not applicable]"
  forfait_jours_validity_assessed: "[Yes / No / Not applicable]"
  rupture_conventionnelle_contribution_rate: "[30% (pre-2026) / 40% (2026+) / Not applicable]"
  limitations:
    - "CCN salary minimums are updated annually — verify current year figures on the CCN text or légisocial.fr"
    - "Cour de cassation jurisprudence evolves rapidly in French labour law"
    - "Barème Macron ceilings are subject to ongoing constitutional/international law challenges — verify current status"
    - "Rupture conventionnelle contribution rate changed to 40% effective 1 January 2026"
  reviewer: "AI-assisted — requires review by avocat en droit du travail or RH conseil habilité"
```

---

## Anti-Patterns

What NOT to do when drafting or reviewing French CDI contracts:

1. **Using a CDD form for a structurally permanent role.** If the business need is ongoing,
   using repeated CDDs or a CDD for a role that is intrinsically permanent in the company
   → requalification to CDI from inception (indemnité de requalification: 1 month minimum
   salary). Particularly common with "accroissement temporaire d'activité" abused for seasonal
   or structural demand.

2. **Non-compete clause without financial compensation.** No compensation = automatic nullity.
   The employer cannot retroactively cure the defect by offering compensation post-dispute.
   The employee is immediately free to compete and may also claim damages for the period they
   were incorrectly restrained.

3. **Derisory contrepartie financière.** Setting compensation at 10–15% of gross salary
   risks the "dérisoire" finding by courts. The 61% invalidity rate for contested non-compete
   clauses in 2024 reflects this. Budget for 30–50% to ensure safety.

4. **Non-compete waiver right exercisable at any time during the restriction period.** This
   leaves the employee in permanent uncertainty — they cannot plan their professional future.
   Cour de cassation has voided such clauses. The waiver right must have a defined time
   window (e.g., "within 15 days of notification of termination").

5. **Forfait jours without verifying CCN authorization.** Many CCN provisions authorizing
   forfait jours have been declared invalid by the Cour de cassation for lacking sufficient
   protections on rest time and workload monitoring. Post-2014 Cour de cassation decisions
   invalidated dozens of CCN forfait provisions. Always verify the specific CCN's forfait
   provision is still valid before including a forfait jours clause.

6. **Forfait jours convention without annual entretien or monitoring.** Cour de cassation
   (10 janvier 2024): failure to comply with Art. L3121-65 monitoring obligations (control
   document + annual entretien) renders the individual forfait convention null and void.
   Consequence: retroactive overtime claims from the 35th hour for the entire duration of
   employment — potentially several years × 10–15 hours/week of overtime pay.

7. **Mobility clause covering "all group subsidiaries" without geographic boundary.** A
   clause covering "any company in the group, anywhere" without geographic delimitation is
   void. The employer cannot enforce it. If the employer dismisses the employee for refusing
   to apply it, the dismissal is without cause réelle et sérieuse.

8. **IP assignment clause purporting to waive moral rights.** Droit moral is inalienable
   under French law (Art. L121-1 CPI). Any contractual waiver of moral rights is null and
   void. The author/employee retains the right of divulgation, attribution, integrity, and
   withdrawal regardless of what the contract states.

9. **Broad IP assignment clause for all creations.** For non-software works, a clause
   assigning "all intellectual property created during employment" without specifying the
   type of rights (reproduction, representation, adaptation), territory, and duration fails
   the Art. L131-3 CPI formality requirements → void. Exception: software under Art. L113-9
   CPI auto-vests without an assignment clause.

10. **Not identifying the applicable CCN or using the wrong CCN.** Misidentification of the
    CCN is a compound error: wrong trial period maximums, wrong salary minimums, wrong notice
    periods, wrong forfait jours eligibility, wrong invention bonus. Always determine the
    employer's NAF/APE code and cross-reference on codetravail.fr before drafting.

11. **Trial period renewal without CCN authorization or without employee written consent.**
    If the CCN does not permit renewal, the renewal is null. If the employee has not given
    written consent during the initial period (not after expiry), the renewal is null.
    Terminating the employee "during the renewed trial" when the renewal is null = dismissal
    without cause réelle et sérieuse — full dismissal procedure and indemnities apply.

12. **Dismissal letter without specific stated reasons.** Art. L1232-6 requires specific
    reasons. A letter stating only "professional insufficiency" without concrete facts can
    be challenged as insufficiently grounded. The employer is bound by the reasons stated
    in the letter — new reasons cannot be added in court proceedings.

13. **Confusing rupture conventionnelle with accord amiable.** A mutual termination agreement
    that bypasses the Art. L1237-11 homologation process lacks legal protection for both
    parties — it may be requalified as a dismissal without cause or as a resignation without
    unemployment benefit entitlement. Always use the official TéléRC homologation process.

14. **Failing to update the rupture conventionnelle cost model for 2026.** The employer
    contribution (contribution patronale) on the exempt portion of the indemnité spécifique
    increased from 30% to 40% effective 1 January 2026 (LFSS 2026). HR models using pre-2026
    rates will underestimate the cost by approximately 33% of the exempt amount.

15. **Discrimination risk in termination notices.** A dismissal letter referencing a protected
    characteristic (illness, pregnancy, trade union activity, age, disability, whistleblowing)
    — even obliquely — creates a null dismissal (nullité), not merely a dismissal without cause.
    The Barème Macron does not apply; the employee can claim reinstatement or minimum 6 months'
    salary uncapped by the barème.

16. **Secret employee monitoring.** Any evidence obtained by secret surveillance (keyloggers,
    undisclosed GPS tracking, hidden cameras) is inadmissible in prud'hommes proceedings and
    constitutes a violation of Art. 9 Civil Code (right to privacy) and RGPD. The employer
    may face CNIL sanctions and criminal liability. Always disclose monitoring tools to the
    CSE and employees before implementation.

17. **Clause de dédit-formation for mandatory training.** A training repayment clause covering
    training that is legally mandatory for the role (habilitation électrique, CACES, safety
    training required by labor regulation) is null — employers cannot charge employees for
    training they are legally required to provide.

18. **Cadre dirigeant misclassification.** Courts apply three strict cumulative criteria
    (Art. L3111-2). Classifying an employee as cadre dirigeant to avoid all working time
    protections, without meeting all three criteria, exposes the employer to retroactive
    overtime claims for the full employment period.

---

## Writing Standards

### Plain-Language Discipline

Before delivering any output:

1. **Audience check:** Who will read this? A legal team → technical precision acceptable.
   An HR manager → explain French legal terms with English parenthetical. An employee →
   avoid jargon; use clear, direct language.

2. **Bilingual clarity:** For French-specific legal terms with no direct English equivalent,
   always provide the French term with an explanatory gloss:
   - "rupture conventionnelle (consensual termination — distinct from both dismissal and
     resignation)"
   - "contrepartie financière (mandatory financial compensation for the restriction period)"
   - "forfait jours (flat-rate days regime for autonomous executives — replaces hourly tracking)"
   - "barème Macron (statutory scale capping damages for unfair dismissal)"

3. **No false certainty:** Acknowledge where French labour law is contested or evolving.
   The non-compete invalidity rate (61% in 2024) and the ongoing scrutiny of forfait jours
   provisions are not settled areas — say so.

4. **Self-edit for verbosity:** Cut preamble. Lead with the finding. State the article.
   State the risk. Provide the fix.

5. **Consistency gate:** All defined French legal terms (CDI, CCN, IDCC, SMIC, etc.)
   must be used consistently throughout the output — no synonym drift (e.g., do not switch
   between "salaire minimum" and "SMIC" without explanation).

---

## External Tool Integration

### legalcode-mcp (Preferred)

When legalcode-mcp is connected, use it to:

- Retrieve the current text of the applicable Code du travail articles
- Verify current CCN salary minimums for the relevant year (CCN minimums are updated
  annually by avenant — never rely on values older than 12 months)
- Retrieve recent Cour de cassation decisions on non-compete, forfait jours, and termination
- Verify the current SMIC rate
- Check the current DREETS/TéléRC procedure for rupture conventionnelle

### légifrance.gouv.fr (Fallback)

If legalcode-mcp is not available, direct the user to verify key provisions at:

- légifrance.gouv.fr — authoritative source for Code du travail and CCN texts
- codetravail.fr — Ministry of Labour tool for CCN identification by NAF/APE code
- service-public.fr — procedural guides for rupture conventionnelle, period d'essai, etc.
- cnil.fr — CNIL guidance on employee data processing
- inpi.fr — INPI guidance on employee inventions (inventions de salariés)
- urssaf.fr — current SMIC rates and social charge exemption thresholds

Mark all statutory references with [VERIFY] when legalcode-mcp is not connected. Note in
the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`.

---

## Output Format Template

Deliver the analysis or draft in this structure:

---

# Analyse CDI — [Nom de l'employé / Description du poste]

**Date:** [date]
**Mode:** [Révision / Rédaction / Analyse de clause / Rupture]
**Perspective:** [Employeur / Salarié / Neutre]
**Convention collective:** [Nom CCN — IDCC XXXX, ou "Non identifiée"]
**Catégorie professionnelle:** [Ouvrier-Employé / AMT / Cadre / Cadre dirigeant]
**Régime de temps de travail:** [35h standard / Forfait jours (218j) / Cadre dirigeant]

---

## Synthèse (Executive Summary)

**Profil de risque global:** [FAIBLE / MOYEN / ÉLEVÉ / CRITIQUE]

**Points critiques à adresser immédiatement:**

- [Tier 1 RED item 1 — one sentence]
- [Tier 1 RED item 2 — one sentence]

**Points à améliorer (Tier 2):**

- [YELLOW item summary]

**Bonne pratique confirmée:**

- [GREEN finding summary — brief]

---

## Analyse Clause par Clause

### [Clause Category] — [GREEN / YELLOW / RED]

**Texte analysé:** "[Relevant clause text]"

**Analyse:**
[Finding — specific, citing the legal authority]

**Risque:** [If YELLOW or RED — precise risk description]

**Modèle de redline:** [If YELLOW or RED — replacement or additional language]

**Priorité:** [Tier 1 / Tier 2 / Tier 3]

---

_(Repeat for each clause category)_

---

## Tableau Récapitulatif

| #   | Clause                | Statut           | Priorité   | Action requise |
| --- | --------------------- | ---------------- | ---------- | -------------- |
| 1   | Parties et formation  | GREEN/YELLOW/RED | Tier 1/2/3 | [Action]       |
| 2   | Classification et CCN | …                | …          | …              |
| ... | ...                   | ...              | ...        | ...            |

---

## Calcul des Indemnités (si applicable)

**Indemnité légale de licenciement:**

- Ancienneté: [X] ans [Y] mois
- Salaire de référence: [€X] (1/12 des 12 derniers mois ou 1/3 des 3 derniers mois — le plus favorable)
- Calcul: ([années ≤10] × ¼) + ([années >10] × ⅓) × salaire de référence = €[total]

**Barème Macron (si licenciement sans cause réelle et sérieuse):**

- Ancienneté: [X] ans → Plancher: [X] mois | Plafond: [X] mois
- Effectif: [≥11 / <11 salariés]

**Rupture conventionnelle (si applicable):**

- Indemnité spécifique minimum: €[X] (même calcul que légale, ou CCN si plus favorable)
- Contribution patronale 40% (2026): €[X × 0.40]
- Coût total employeur: €[X + X]

---

## [YAML Glass Box Audit Trail — as per template above]

---

## Recommandations Prioritaires

### ⚡ Tier 1 — Avant signature / avant première paie

1. [Action item + legal basis]

### ⚠️ Tier 2 — Dans les 30 jours

1. [Action item + legal basis]

### 💡 Tier 3 — Lors de la prochaine révision contractuelle

1. [Action item + legal basis]

---

_Avertissement final: Cette analyse est générée par IA et ne constitue pas un conseil
juridique. Faites vérifier par un avocat en droit du travail ou un juriste RH qualifié
avant toute décision._

---

## Localization Notes

### Language Requirements

- The CDI must be drafted in French (Art. L1221-3). If a position title can only be designated
  by a foreign-language term (e.g., "Product Manager," "CTO"), include a French explanation
  of the actual functions
- All official notices (convocation to entretien préalable, notification of dismissal) must
  be in French
- For foreign employees, a translated version may be provided alongside the French original
  — but the French version governs

### DOM-TOM Variations

- The Code du travail applies in all DOM (Guadeloupe, Martinique, Guyane, La Réunion, Mayotte)
  but some CCNs have specific DOM provisions
- For TOM, verify applicability of specific provisions [VERIFY]

### Cross-Border Employment

- For employees split between France and another country, verify:
  - Applicable social security regime (EU Regulation 883/2004 A1 certificate, or bilateral
    convention)
  - Détachement vs. CDI local — significant tax and social charge consequences
  - Rome I Regulation Art. 8: mandatory French employment law provisions apply regardless of
    governing law choice if the employee habitually works in France

### Expatriate Employees (Cadres Internationaux)

- Impatriation tax regime available for certain newly recruited foreign executives (Art. 155 B
  CGI) — flag but note it is a tax matter outside the scope of the CDI skill
- "Impatriés" regime: 30% income tax exemption on French-source salary for up to 8 years

---

## Provenance

Created by Legalcode (2026-03-21). Mode A — original synthesis. Research sources:

- Légifrance — Code du travail (Books I–III, employment contract and working time)
- Légifrance — Code de la propriété intellectuelle (Art. L113-9, L611-7)
- Légifrance — RGPD + Loi Informatique et Libertés
- Légifrance — Loi n°2022-1598 du 21 décembre 2022 (marché du travail)
- Légifrance — Loi n°2023-1107 du 29 novembre 2023 (partage de la valeur)
- Légifrance — LFSS 2026 (contribution patronale rupture conventionnelle 40%)
- Cour de cassation, Chambre sociale — non-compete case law (10 juillet 2002; 24 janvier 2024)
- Cour de cassation, Assemblée plénière — Barème Macron (11 mai 2022)
- Cour de cassation, Chambre sociale — forfait jours (10 janvier 2024)
- URSSAF — SMIC 2026 (€12.02/h, €1,823.03/month)
- Syntec-Cinov CCN (IDCC 1486) — avenant 13 December 2022, effective 1 July 2024
- Nouvelle Métallurgie CCN (IDCC 3248) — effective 1 January 2024
- CNIL — guidance on employee data processing and monitoring
- INPI — guidance on inventions de salariés (Art. L611-7 CPI)
- ANI du 26 novembre 2020 — télétravail
- Service-public.fr — rupture conventionnelle TéléRC procedure
- Mayer Brown, Villie Avocat, Légisocial, Éditions Tissot — practice guidance
- Legalcode reference standard: legalcode-contract-review (quality framework baseline)
