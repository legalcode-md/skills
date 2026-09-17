---
name: legalcode-de-kuendigungsschutz
description: 'Analyze German dismissal protection (Kündigungsschutz) for any employment termination scenario
  in Germany. Use when advising on KSchG social justification (betriebsbedingt, personenbedingt, verhaltensbedingt),
  Sozialauswahl criteria and scoring, BGB § 622 statutory notice periods, BGB § 626 extraordinary dismissal
  (außerordentliche Kündigung), special protection categories (pregnancy/MuSchG, parental leave/BEEG,
  severely disabled/ SGB IX, works council members/BetrVG § 103, DPOs/BDSG), Abfindung negotiation and
  § 1a KSchG statutory severance, works council consultation under BetrVG § 102, and the § 4 KSchG three-week
  claim period. Also use when drafting Aufhebungsverträge, assessing Massenentlassung (collective redundancy)
  obligations, or reviewing a proposed dismissal strategy for legal risk. Jurisdiction: Germany.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — German Dismissal Protection (Kündigungsschutz)

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of German
> dismissal protection law. It does not constitute legal advice (Rechtsberatung). All
> outputs require review by a Rechtsanwalt or Fachanwalt für Arbeitsrecht licensed in
> Germany before any action is taken. German employment law is highly fact-specific and
> the Bundesarbeitsgericht (BAG) issues continuous case-law refinements. Statutory
> citations and case references herein carry hallucination risk — verify against
> gesetze-im-internet.de and bundesarbeitsgericht.de before relying on them.

---

## Purpose and Scope

This skill enables systematic, auditable analysis of German dismissal protection across
the full life-cycle of an employment termination — from pre-dismissal risk assessment
through labor court proceedings and Abfindung negotiation.

**Covers:**

- KSchG applicability assessment (six-month waiting period, § 23 headcount threshold)
- Social justification analysis under all three dismissal grounds (§ 1 KSchG)
- Sozialauswahl (social selection) criteria and Punkteschema review (§ 1 Abs. 3–4 KSchG)
- Statutory notice period calculation (§ 622 BGB) including probationary period
- Extraordinary dismissal (außerordentliche Kündigung) under § 626 BGB
- Special protection categories — each requiring separate administrative process
- Works council consultation under § 102 BetrVG (ordinary) and § 103 BetrVG (WC members)
- Abfindung routes: § 1a KSchG statutory offer, §§ 9–10 KSchG court dissolution, Sozialplan
- Mass dismissal notification obligations (§§ 17–18 KSchG)
- Procedural compliance: § 623 BGB written form, § 4 KSchG three-week claim period
- Aufhebungsvertrag (termination agreement) structure

**Does not:**

- Draft the dismissal notice itself — use the arbeitsvertrag-employment-agreement skill
- Cover non-German employment law
- Provide individual legal advice or replace qualified German labour counsel
- Substitute for works council consultation, which is a mandatory legal step

---

## Jurisdiction and Governing Law

**Germany only.** This skill applies German federal employment law. Key statutes:

| Statute                                      | Abbreviation | Topic                                                          |
| -------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Kündigungsschutzgesetz                       | KSchG        | Core dismissal protection; social justification; Sozialauswahl |
| Bürgerliches Gesetzbuch §§ 620–628, 622, 626 | BGB          | Notice periods; extraordinary dismissal; written form (§ 623)  |
| Betriebsverfassungsgesetz                    | BetrVG       | Works council rights: §§ 102, 103, 111–113                     |
| Sozialgesetzbuch IX §§ 168–175               | SGB IX       | Severely disabled protection; Integrationsamt consent          |
| Mutterschutzgesetz § 17                      | MuSchG       | Pregnancy and maternity dismissal prohibition                  |
| Bundeselterngeld- und Elternzeitgesetz § 18  | BEEG         | Parental leave dismissal prohibition                           |
| Bundesdatenschutzgesetz §§ 6, 38             | BDSG         | Data protection officer dismissal protection                   |
| Berufsbildungsgesetz § 22                    | BBiG         | Trainee dismissal rules                                        |
| Einkommensteuergesetz §§ 24, 34              | EStG         | Severance tax treatment (Fünftelregelung)                      |
| Hinweisgeberschutzgesetz                     | HinSchG      | Whistleblower retaliation protection (since July 2023)         |

**Key court**: Bundesarbeitsgericht (BAG) — decisions accessible at bundesarbeitsgericht.de.

All statutory references should be verified at gesetze-im-internet.de. Mark uncertain
interpretations with **[VERIFY]**.

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at decision points where:

- The answer changes the legal analysis materially
- Multiple valid approaches exist
- Business context is needed to assess proportionality
- Threshold conditions must be confirmed before proceeding

Present CLARIFY questions as structured option sets with "Why this matters" explanations.
Skip questions already answered by prior context. For batch/automated runs, proceed with
conservative defaults and state all assumptions explicitly.

---

## Workflow

### Step 1: Accept the Dismissal Scenario

Accept input in any of these formats:

- **Employer perspective**: Facts about the employee, dismissal ground, establishment,
  works council status, employee's protection category
- **Employee perspective**: Dismissal notice received; facts about employment and grounds
- **Document**: Kündigungsschreiben (dismissal notice), Aufhebungsvertrag draft, or
  Interessenausgleich/Sozialplan for review
- **Strategic planning**: Pre-dismissal scenario analysis or HR restructuring assessment

If no scenario is provided, prompt the user to supply the key facts.

---

### Step 2: Gather Core Facts

**⟁ CLARIFY** — Before beginning, gather these facts. Present as a structured intake:

**A. Parties and Establishment:**

1. **Perspective**: Are you advising the employer or the employee?
   - Options: Employer (Arbeitgeber), Employee (Arbeitnehmer), Both (neutral audit)
   - _Why this matters_: The entire risk assessment flips depending on the side.

2. **Establishment size** (Betriebsgröße): How many employees does the establishment
   (Betrieb, not necessarily the whole company) employ as a rule?
   - Options: ≤ 5, 6–10, > 10 (full headcount) — part-timers ≤ 20 hrs/week = 0.5,
     ≤ 30 hrs/week = 0.75, > 30 hrs/week = 1.0; trainees excluded
   - _Why this matters_: KSchG applies only if the establishment "in der Regel" has
     more than 10 employees (§ 23 Abs. 1 KSchG). Below this threshold, only minimum
     protections apply (AGG, special categories, BGB § 138).

3. **Length of employment** (Betriebszugehörigkeit): When did the employment begin?
   - Provide the start date; the skill calculates the waiting period and notice periods.
   - _Why this matters_: KSchG requires > 6 months (§ 1 Abs. 1 KSchG); § 622 BGB
     graduated notice periods kick in at 2, 5, 8, 10, 12, 15, and 20 years.

**B. Employee Characteristics:** 4. **Special protection status** (Sonderkündigungsschutz): Does the employee belong to
any protected category?

- Options (multiple): Pregnant/post-natal (MuSchG § 17), Parental leave (BEEG § 18),
  Severely disabled — GdB ≥ 50 or equated status (SGB IX §§ 168 ff.), Works council
  member/candidate (BetrVG §§ 15, 103), Trainee (BBiG § 22), DPO (BDSG § 6/38),
  Youth/apprentice representative, Whistleblower (HinSchG), None known
- _Why this matters_: Special protection categories require prior administrative
  approval or works council consent — and dismissal without these is void.

5. **Works council exists?** (Betriebsrat vorhanden?): Is there an active works council
   in this establishment?
   - Options: Yes, No, Unknown
   - _Why this matters_: § 102 BetrVG consultation is mandatory; violation voids dismissal.

**C. Dismissal Type:** 6. **Intended dismissal type**:

- Options: Ordinary — operational (betriebsbedingt), Ordinary — personal capacity
  (personenbedingt), Ordinary — conduct (verhaltensbedingt), Extraordinary without notice
  (außerordentlich fristlos, § 626 BGB), Extraordinary with notice in lieu, Termination
  agreement (Aufhebungsvertrag), Not yet determined
- _Why this matters_: Each type triggers different legal requirements and risks.

7. **Dismissal ground facts**: Describe the specific facts the employer relies on for
   dismissal (free text). Include: for operational dismissals — the business decision and
   its effect on the position; for personal/illness dismissals — the medical facts and
   history; for conduct dismissals — the specific acts, dates, and whether an Abmahnung
   was issued.

State all assumptions explicitly if the user provides partial context.

---

### Step 3: KSchG Applicability Assessment

Before analysing social justification, determine whether the KSchG applies at all.

**Threshold 1 — Six-Month Waiting Period (§ 1 Abs. 1 KSchG):**
Calculate from the contractual employment start date.

- If < 6 months: KSchG does not apply. Remaining protections: AGG discrimination ban,
  § 138 BGB (unconscionable dismissal), special protection categories (SGB IX, MuSchG,
  BEEG), BetrVG § 102 consultation if works council exists, BBiG § 22 for trainees.
- If ≥ 6 months: proceed to Threshold 2.

**Threshold 2 — Establishment Size (§ 23 Abs. 1 KSchG):**

- If ≤ 10 employees (weighted): KSchG does not apply. Apply the same minimum protections.
  Note: Employees employed before 31 December 2003 are protected under the old > 5 employee
  threshold (§ 23 Abs. 1 S. 2–3 KSchG) — verify status for long-tenured employees.
- If > 10 employees: KSchG applies in full.

**Output:** Classify as:

- **KSchG APPLICABLE** — social justification required under § 1 KSchG
- **KSchG NOT APPLICABLE** — only minimum protections; document which apply
- **THRESHOLD UNCERTAIN** — headcount near the boundary; recommend verification

**⟁ CLARIFY** — If the establishment is near the 10-employee threshold, ask the user
to confirm the exact weighted headcount (including part-time factors and trainee exclusion)
before proceeding, as this is outcome-determinative.

---

### Step 4: Special Protection Analysis

**Always run this step regardless of KSchG applicability.**

For each confirmed special protection category, apply the relevant analysis:

#### 4a. Pregnancy and Post-Natal (MuSchG § 17)

- Ordinary AND extraordinary dismissal are **prohibited** from the start of pregnancy
  until four months after delivery.
- Prohibition applies even if the employer was unaware of the pregnancy at the time of
  dismissal — BUT the employee must notify the employer within **two weeks** of receiving
  the notice to invoke retrospective protection.
- Exception: State authority (Gewerbeaufsichtsamt or equivalent Landesamt) may grant
  approval — in practice, only for reasons entirely unconnected with the pregnancy.
- **Risk**: **RED — Void dismissal** unless state approval obtained in advance.

#### 4b. Parental Leave (BEEG § 18)

- Ordinary AND extraordinary dismissal are **prohibited** during Elternzeit and for
  **four weeks before** the parental leave begins (from notification of the request).
- Duration: up to three years per child.
- Exception: State authority approval required (same authority as MuSchG). Rarely granted.
- **Risk**: **RED — Void dismissal** unless state approval obtained in advance.

#### 4c. Severely Disabled Persons (SGB IX §§ 168–175)

Three-step administrative process:

1. **Consult Schwerbehindertenvertretung (SBV)** before submitting consent application
   (§ 178 Abs. 2 S. 3 SGB IX) — failure renders dismissal void regardless of Integrationsamt consent.
2. **Obtain Integrationsamt consent** before issuing notice:
   - Ordinary dismissal: Integrationsamt has **one month** to decide (silence = consent
     after one month, § 170 Abs. 1 SGB IX).
   - Extraordinary dismissal: employer must apply within **two weeks** of learning dismissal
     facts; Integrationsamt has **two weeks** to decide (silence = consent, § 174 Abs. 3 SGB IX).
3. **Issue notice only after consent** — retroactive validation is not possible.

- Employee's duty to disclose: if employer unaware of disability, employee has **three
  weeks** from receipt of notice to invoke protection retroactively.
- Protection applies after six-month waiting period in employment.
- **Risk**: **RED — Void dismissal** if SBV consultation or Integrationsamt consent omitted.

#### 4d. Works Council Members and Co-Determination Office Holders (BetrVG §§ 15, 103)

- **Ordinary dismissal**: Entirely prohibited during the term of office (§ 15 KSchG),
  with two exceptions: complete establishment closure (Betriebsstilllegung) or closure
  of the organisational unit where the member works (and transfer is impossible).
- **Extraordinary dismissal**: Requires **prior affirmative consent of the works council**
  under § 103 BetrVG. Unlike ordinary § 102 consultation, silence is not consent — the
  employer must obtain a positive vote. If works council refuses, employer must apply to
  the Arbeitsgericht to replace the consent by court order.
- **Post-term protection**: One year after expiry of office, ordinary dismissal remains
  prohibited; extraordinary dismissal requires only works council notification.
- Applies equally to: works council candidates during election, youth and apprentice
  representatives, Schwerbehindertenvertretung members.
- **Risk**: **RED — Void dismissal** if affirmative consent not obtained (extraordinary)
  or prohibition disregarded (ordinary).

#### 4e. Data Protection Officers (BDSG §§ 6 Abs. 4, 38 Abs. 2)

- Mandatory internal DPOs (those obliged under GDPR Art. 37 / BDSG § 38) may only be
  dismissed for **wichtiger Grund** (§ 626 BGB standard) during their term and for
  one year after appointment ends.
- Voluntary DPOs (appointed beyond legal obligation) do not receive this elevated
  protection.
- **⟁ CLARIFY** — Confirm whether the DPO appointment was legally mandatory or voluntary.
- **Risk**: **RED** for mandatory DPOs if dismissal lacks wichtiger Grund basis.

#### 4f. Trainees (BBiG § 22)

- During Probezeit (min. 1 month, max. 4 months): dismissal by either party without
  notice or reasons is permitted.
- After Probezeit: only extraordinary dismissal for wichtiger Grund (§ 626 BGB) is
  available to the employer. Ordinary notice termination by the employer is **not
  available** after the Probezeit ends.
- Written form and two-week deadline apply by analogy.
- **Risk**: **RED** if employer attempts ordinary notice dismissal post-Probezeit.

#### 4g. Whistleblowers (HinSchG, in force July 2023)

- Applies to employers with 50+ employees. Dismissal following a protected report creates
  a **statutory presumption of retaliation** — employer must rebut that the dismissal had
  a lawful independent basis (reversal of burden of proof).
- **Risk**: **YELLOW-to-RED** depending on proximity of report to dismissal and employer's
  ability to evidence an independent lawful ground.

---

### Step 5: KSchG Social Justification Analysis (if KSchG Applicable)

The burden of proof rests on the **employer** (§ 1 Abs. 2 S. 4 KSchG).

Run the relevant sub-analysis based on the stated dismissal ground:

#### 5a. Betriebsbedingte Kündigung (Operational/Redundancy Dismissal)

**Legal test (three elements, all required):**

| Element                                 | Test                                                                                        | Key Questions                                                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1. Unternehmerische Entscheidung        | A genuine entrepreneurial decision that eliminates the need for the employee's work         | What specific decision was made? Is it documented? When was it made and communicated?                                 |
| 2. Dringende betriebliche Erfordernisse | The business requirement is urgent — the position is genuinely eliminated, not just reduced | Can the employee be moved to a comparable position within the establishment or undertaking? (Freikündigungsgrundsatz) |
| 3. Sozialauswahl (§ 1 Abs. 3 KSchG)     | Social selection criteria applied correctly among comparable employees                      | See Step 5d — Sozialauswahl analysis                                                                                  |

**Court review standard**: Courts apply only a Missbrauchskontrolle — they will not
second-guess the commercial wisdom of the business decision, only verify it is not
"offenbar unsachlich, unvernünftig oder willkürlich" (manifestly unreasonable/arbitrary).

**Presumption via Interessenausgleich (§ 1 Abs. 5 KSchG):** Where the employer and works
council have concluded an Interessenausgleich naming the affected employees, dringende
betriebliche Erfordernisse are **presumed** — the employee bears the burden of rebuttal
with concrete contradictory facts. This significantly strengthens the employer's position.

**Risk flags for betriebsbedingte Kündigung:**

- A comparable position exists elsewhere in the undertaking — **RED**: dismissal void
  under ultima-ratio principle if transfer was possible
- Dismissal followed by re-hiring for the same or equivalent role — **RED**: motive
  scrutiny (Missbrauchsschutz); new hire within a short period contradicts urgency
- Sozialauswahl group too narrow or criteria not applied — **RED**: see Step 5d
- No documentation of the entrepreneurial decision — **YELLOW**: evidentiary risk
- Interessenausgleich with named list absent despite works council presence — **YELLOW**:
  missed opportunity to create § 1 Abs. 5 presumption

#### 5b. Personenbedingte Kündigung (Personal Capacity Dismissal — Illness)

**BAG three-stage test** (krankheitsbedingte Kündigung — the most common personenbedingter ground):

| Stage                                                   | Test                                                 | Evidence Required                                                                                                                             |
| ------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Negative Gesundheitsprognose                         | Long-term or recurring incapacity likely to continue | Medical evidence; past absence pattern (≥ 6 weeks per year over ≥ 24-month period creates prima facie prognosis); specialist opinion          |
| 2. Erhebliche Beeinträchtigung betrieblicher Interessen | Substantial operational impairment                   | Continued Entgeltfortzahlungskosten (continued pay during illness) exceeding six-week threshold; operational disruption; cover costs          |
| 3. Interessenabwägung                                   | Overall balance of interests                         | Employee's age, length of service, prospects, likelihood of recovery; employer's operational burden; availability of reasonable accommodation |

**⟁ CLARIFY** — Has the employer conducted a Betriebliches Eingliederungsmanagement (BEM)
under § 167 Abs. 2 SGB IX? If the employer has 20+ employees and the employee was absent

> 6 weeks in the previous 12 months, BEM must be offered. Failure creates significant
> evidential risk in the subsequent dismissal proceeding.

**Risk flags for personenbedingte Kündigung:**

- BEM not offered where required — **RED**: courts may treat this as disproportionate
  without proof that BEM would have been futile
- No medical prognosis — only current illness — **RED**: absence of prognosis is fatal
- Solely short-term isolated illnesses — **YELLOW**: may not satisfy prognosis threshold
- Employee's long blameless service not weighed in Interessenabwägung — **YELLOW**

#### 5c. Verhaltensbedingte Kündigung (Conduct Dismissal)

**Legal requirements (sequential):**

1. **Contractual breach** that is culpable (vorwerfbar) and within the employee's control
2. **Prior Abmahnung (formal warning)** — required as a rule; must:
   - Name the specific conduct complained of
   - Warn that dismissal will follow if repeated
   - Be in writing (though not strictly required by statute — but evidentially critical)
   - The same or sufficiently similar conduct must recur after the warning
3. **Ultima ratio**: No milder response (Abmahnung, transfer, reduction of duties) is
   available. The court will examine whether a further warning would suffice.
4. **Interessenabwägung**: The conduct's severity and recurrence risk must outweigh the
   employee's personal circumstances (length of service, age, maintenance obligations).

**Abmahnung exception** — a warning may be dispensed with only where:

- The breach is so severe the employee must have known dismissal would follow (e.g.,
  sustained working-time fraud, workplace violence, serious criminal acts against employer)
- The trust basis is so fundamentally destroyed that a warning would be pointless

**Key BAG case — "Emmely" (BAG 2 AZR 541/09, 10 June 2010):** A cashier of 31 years was
dismissed for misappropriating bottle deposit vouchers worth €1.30. The BAG held the
extraordinary dismissal void because the Interessenabwägung overwhelmingly favoured the
employee given her long blameless service and the trivial financial harm. **[VERIFY]**

**Risk flags for verhaltensbedingte Kündigung:**

- No prior Abmahnung for a conduct that required one — **RED**: dismissal void
- Abmahnung does not name the specific conduct — **YELLOW**: may be insufficient
- Same conduct, different Abmahnung recipient (selective enforcement) — **YELLOW**
- Long blameless employment history not weighed — **YELLOW**: Interessenabwägung flaw
- Extraordinary dismissal for minor-value dishonesty without Abmahnung — **RED**: Emmely risk

---

### Step 6: Sozialauswahl Analysis (§ 1 Abs. 3–4 KSchG)

Required for every betriebsbedingte Kündigung where multiple employees are potentially
affected. Run even where only one employee is dismissed — the employer must have considered
the selection pool.

#### 6a. Define the Comparison Group (Vergleichbare Arbeitnehmer)

Employees are comparable where they are **mutually interchangeable** based on:

- Work tasks and qualifications (functional interchangeability)
- Organisational unit
- The employer could, after reasonable notice, transfer one to the other's role

**Exclusions from the selection pool (§ 1 Abs. 3 S. 2 KSchG):** Employees whose retention
is in the "berechtigtem betrieblichen Interesse" — typically key-knowledge holders or
employees with specialised skills not held by others.

**⟁ CLARIFY** — Confirm who the employer placed in the comparison group and why any
employees were excluded. Courts scrutinise the group composition carefully.

#### 6b. Apply the Four Social Criteria (§ 1 Abs. 3 S. 1 KSchG)

All four criteria must be "ausreichend berücksichtigt" (sufficiently considered):

| Criterion               | German Term           | Weighting Notes                                                                                                                                                        |
| ----------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Length of service       | Betriebszugehörigkeit | Longer service = higher protection                                                                                                                                     |
| Age                     | Lebensalter           | Protects workers with poor re-employment prospects; age-group partitioning (Altersgruppen) requires concrete operational justification — BAG 2 AZR 468/08 **[VERIFY]** |
| Maintenance obligations | Unterhaltspflichten   | Number of legal dependants                                                                                                                                             |
| Severe disability       | Schwerbehinderung     | GdB ≥ 50 or equated status                                                                                                                                             |

#### 6c. Punkteschema (Point Scoring Scheme)

Where a Punkteschema has been agreed in a Betriebsvereinbarung or Tarifvertrag (§ 1 Abs. 4 KSchG):

- Courts apply **highly deferential review** — only "grobe Fehlerhaftigkeit" (gross error)
  triggers invalidity
- All four statutory criteria must be represented in the scheme
- Absence of any criterion from the scheme = gross error, selection void

**Risk flags for Sozialauswahl:**

- One statutory criterion entirely omitted — **RED**: selection void
- Comparison group obviously drawn too narrowly to avoid a protected employee — **RED**
- Age criterion used without group-partitioning justification — **YELLOW**: BAG risk
- No documentation of the Sozialauswahl process — **YELLOW**: evidentiary exposure
- Employee with higher social need (more dependants, longer service) retained over employee
  with lower social need — **RED** unless documented retention justification under § 1 Abs. 3 S. 2

---

### Step 7: Notice Period Calculation (§ 622 BGB)

Apply only to ordinary dismissals. For extraordinary dismissal, proceed to Step 8.

**Probationary Period (§ 622 Abs. 3 BGB):**

- During contractually agreed Probezeit (maximum 6 months): **2 weeks' notice** by either
  party, without reference to mid-month or end-of-month.

**Standard Notice Period (§ 622 Abs. 1 BGB):**

- Basic period for either party: **4 weeks to the 15th or end of a calendar month**

**Graduated Employer Notice Periods (§ 622 Abs. 2 BGB)** — applicable only to
**employer-initiated** terminations:

| Length of Service in Establishment | Minimum Notice Period             |
| ---------------------------------- | --------------------------------- |
| 2+ years                           | 1 month to end of calendar month  |
| 5+ years                           | 2 months to end of calendar month |
| 8+ years                           | 3 months to end of calendar month |
| 10+ years                          | 4 months to end of calendar month |
| 12+ years                          | 5 months to end of calendar month |
| 15+ years                          | 6 months to end of calendar month |
| 20+ years                          | 7 months to end of calendar month |

**Note on age-exclusion rule (§ 622 Abs. 2 S. 2 BGB):** Service before age 25 is
excluded from the calculation. This rule may conflict with EU anti-discrimination law
(Mangold/Kücükdeveci ECJ line) — apply with caution and flag for legal verification.
**[VERIFY]**

**Collective Agreement Derogations (§ 622 Abs. 4–5 BGB):** Tarifverträge may shorten or
extend notice periods. Verify the applicable Tarifvertrag for the sector.

**Employee notice periods**: Remain fixed at 4 weeks (§ 622 Abs. 1 BGB); graduated
extended periods do not apply in reverse.

**Risk flags for notice periods:**

- Notice period shorter than statutory minimum — **RED**: employee entitled to additional
  wages for the gap period (Annahmeverzug, § 615 BGB)
- Notice expires on a date other than 15th or end of month (except probation) — **YELLOW**:
  technical defect; notice may be construed as effective from the next permissible date
- Pre-age-25 service included in calculation — **YELLOW**: [VERIFY] EU compatibility

---

### Step 8: Extraordinary Dismissal Analysis (§ 626 BGB)

Apply when the employer seeks to terminate without serving the notice period.

#### 8a. Two-Stage BAG Test

**Stage 1 — Abstract Suitability (abstrakte Eignung):**
Does a fact situation exist that, in principle, could justify extraordinary dismissal?
This acts as a negative filter — if the facts cannot abstractly constitute an important
reason (e.g., minor, isolated, non-culpable conduct), the analysis ends here.

**Stage 2 — Proportionality and Interest Balancing:**
Given the individual circumstances, is immediate termination without notice proportionate,
or could a milder response (ordinary dismissal, warning, transfer) have been used?

Factors favouring the employee: long blameless service; trivial financial harm; provocation;
personal circumstances (age, dependants, health); genuine remorse.
Factors favouring the employer: severity of breach; loss of trust; position of responsibility;
pattern of conduct; financial harm to employer.

#### 8b. Two-Week Notification Deadline (§ 626 Abs. 2 BGB)

- Employer must declare extraordinary dismissal within **two weeks** from gaining
  sufficient reliable knowledge of the facts — not from suspicion, but from a clear
  factual picture.
- The clock may be paused during necessary investigations (aufklärende Maßnahmen) — but
  only while the employer actively investigates, not simply waits.
- **Hard exclusion deadline (Ausschlussfrist)**: Cannot be extended or waived.
- To preserve the deadline while awaiting § 103 BetrVG works council consent, the employer
  may pre-sign the dismissal notice (Blankokündigung) for conditional delivery.

**Risk flags for extraordinary dismissal:**

- Two-week deadline missed — **RED**: extraordinary dismissal void regardless of merits;
  ordinary dismissal route remains if KSchG applicable and social justification exists
- Facts relied on are disputed without investigation — **YELLOW**: insufficient knowledge
  basis for starting the deadline
- Milder response (Abmahnung, transfer) not considered — **YELLOW-to-RED** depending on
  the gravity of the conduct
- Works council § 103 consent not obtained for protected WC member — **RED**: void

---

### Step 9: Works Council Consultation (§ 102 BetrVG)

**Mandatory for every dismissal where a works council exists.** A dismissal declared
without prior works council consultation is void (§ 102 Abs. 1 S. 3 BetrVG).

#### 9a. Scope of Notification

The employer must provide the works council:

- Identity of the employee
- Type of dismissal (ordinary / extraordinary)
- Intended date of dismissal
- Reasons for dismissal (the full factual basis the employer relies on — courts apply
  "subjektive Determinierung": only what the employer itself relies upon need be disclosed)
- For operational dismissals: the Sozialauswahl basis and outcome

An incomplete or misleading notification creates an "Anhörungsdefizit" that voids the dismissal.

**⟁ CLARIFY** — Ask the user to confirm that the works council notification was or will be
complete, and whether the works council has responded, objected, or raised concerns.

#### 9b. Deadlines and Responses

| Dismissal Type                       | Works Council Response Deadline                           |
| ------------------------------------ | --------------------------------------------------------- |
| Ordinary dismissal                   | **1 week** (§ 102 Abs. 2 S. 1 BetrVG)                     |
| Extraordinary dismissal              | **3 days** (§ 102 Abs. 2 S. 3 BetrVG)                     |
| Extraordinary dismissal of WC member | No deadline — affirmative consent required (§ 103 BetrVG) |

Employer may issue dismissal notice after the deadline if the works council has not
responded (silence = non-objection for ordinary dismissals).

#### 9c. Works Council Objection Effects

If the works council objects in writing on one of the statutory grounds (§ 102 Abs. 3
BetrVG — e.g., failure to consider social criteria, dismissal contrary to Sozialplan):

- The employee is entitled to **continue working during the Kündigungsschutzklage
  proceedings** (§ 102 Abs. 5 BetrVG) — this can be costly for the employer.
- The works council objection does not invalidate the dismissal but strengthens the
  employee's procedural position.

**Risk flags for § 102 BetrVG:**

- No consultation at all — **RED**: dismissal void
- Consultation conducted but notification factually incomplete — **RED**: Anhörungsdefizit
- Works council consulted after dismissal notice issued — **RED**: void
- Works council objects on § 102 Abs. 3 grounds — **YELLOW**: employee continuation right; assess settlement

---

### Step 10: Abfindung (Severance) Assessment

#### 10a. § 1a KSchG — Statutory Severance Offer Route

Available for betriebsbedingte Kündigung only.

**Mechanics:**

1. Employer includes in the dismissal notice a clear offer of severance payment conditional
   on the employee not filing a Kündigungsschutzklage within the three-week period.
2. Statutory amount: **0.5 gross monthly salaries per year of service** (§ 1a Abs. 1 KSchG).
   - Years calculated to nearest complete year; ≥ 6 months counts as a full year (§ 1a Abs. 2).
3. Employee accepts by allowing the three-week deadline to expire without filing.
4. Advantage: creates legal certainty for both parties with no litigation.

**⟁ CLARIFY** — Is the employer intending to use the § 1a route? If yes, confirm the
notice text explicitly includes the offer and the statutory amount has been calculated.

#### 10b. §§ 9, 10 KSchG — Court-Awarded Dissolution

Where an unfair dismissal claim succeeds but reinstatement is unreasonable (unzumutbar):

- **Employee application** (§ 9 Abs. 1 S. 1 KSchG): always available; must show
  continued cooperation is unreasonable.
- **Employer application** (§ 9 Abs. 1 S. 2 KSchG): requires additional grounds showing
  employee conduct incompatible with the establishment's interests.

**Maximum court-awarded severance caps (§ 10 KSchG):**

| Employee Category           | Maximum Severance |
| --------------------------- | ----------------- |
| General                     | 12 months' salary |
| Age 50+, 15+ years' service | 15 months' salary |
| Age 55+, 20+ years' service | 18 months' salary |

#### 10c. Social Plan Severance (BetrVG §§ 111–113)

Required for establishments with 20+ employees when a Betriebsänderung occurs (mass
redundancy, partial closure, merger, fundamental work reorganisation).

**Process:**

1. Employer informs works council (§ 111 BetrVG) — early and comprehensively.
2. Negotiate Interessenausgleich (non-binding reconciliation of interests).
3. Negotiate Sozialplan (binding; enforceable by labour court): specifies compensation
   formulas for economic disadvantages.

**Nachteilsausgleich (§ 113 BetrVG):** If employer fails to attempt Interessenausgleich
negotiations or departs from an agreed Interessenausgleich without sufficient cause,
affected employees are entitled to compensation equivalent to what they would have received
under a Sozialplan — even without one.

**Typical Sozialplan formula:** Gross monthly salary × Years of service × Factor (0.5–1.0,
higher for older employees). Actual formulas are negotiated; no statutory minimum applies.

#### 10d. Negotiated Severance — Market Practice

Market norm for settlement of Kündigungsschutzklage proceedings:

- **Approximately 0.5 gross monthly salaries per year of service** (Daumenregel)
- Range: 0.25–1.5 months per year depending on:
  - Legal risk of the dismissal (stronger claim = higher settlement)
  - Employee age (older employees command higher settlements)
  - Length of service
  - Industry and size of employer
  - Strategic interests of both parties

Settlements are typically reached at the **Gütetermin** (mandatory conciliation hearing
at first-instance Arbeitsgericht) — often on the same day as filing.

#### 10e. Tax Treatment (§§ 24, 34 EStG)

Severance payments are taxable as income (Einkünfte aus nichtselbständiger Arbeit).

**Fünftelregelung (§ 34 Abs. 1 EStG):** Where the severance qualifies as Entschädigung
under § 24 Nr. 1a EStG, the Fünftelregelung provides tax relief — the payment is taxed
as if received in equal fifths over five years, reducing the marginal rate.

**Important change since 1 January 2025:** Employers no longer apply the Fünftelregelung
at payroll tax (Lohnsteuer) level. The employee must claim the relief through their annual
income tax return (Einkommensteuererklärung). This affects gross/net calculations in
settlement negotiations — ensure the employee understands the cash-flow impact.

---

### Step 11: Massenentlassung Assessment (§§ 17–18 KSchG)

**Apply when the employer plans to dismiss a significant number of employees within
30 calendar days from a single establishment.** Thresholds (§ 17 Abs. 1 KSchG):

| Establishment Size | Minimum Dismissals to Trigger |
| ------------------ | ----------------------------- |
| 21–59 employees    | 6+                            |
| 60–499 employees   | 10%+ or 26+                   |
| 500+ employees     | 30+                           |

**Two-step compliance process:**

**Step 1 — Works Council Consultation (§ 17 Abs. 2 KSchG):**
Employer must consult the works council before notifying the Agentur für Arbeit. The
consultation must be genuine (ausreichende Konsultation); a mere information exercise is
insufficient. The employer must provide written information on: reasons, categories of
affected employees, selection criteria, calculation of any severance.

**Step 2 — Notification to Agentur für Arbeit (§ 17 Abs. 1 KSchG):**
Employer must notify the Agentur für Arbeit before dismissals take effect. The notice must
comply with § 17 Abs. 3 KSchG formal requirements (including a copy of the works council
consultation).

**Ongoing CJEU referral (BAG 2 AS 22/23 (A), February 2024):** The BAG has referred to
the Court of Justice of the European Union the question of whether EU law (Directive 98/59)
requires that a defective mass-dismissal notification makes the dismissals void. Until the
CJEU rules, treat notification requirements as **strict compliance obligations with voidness
consequences**. **[VERIFY — pending CJEU ruling]**

**Risk flags:**

- Notification to Agentur für Arbeit omitted or defective — **RED**: voidness risk (pending CJEU)
- Works council consultation inadequate — **RED**: voidness under domestic law
- Dismissals issued before the Agentur für Arbeit's one-month waiting period expires (§ 18
  Abs. 1 KSchG) — **RED**: premature effective date

---

### Step 12: Procedural Compliance Checklist

Run this checklist for every dismissal before confirming the analysis:

| Requirement                                                 | Statutory Basis          | Status                |
| ----------------------------------------------------------- | ------------------------ | --------------------- |
| Written form — hand-signed original                         | § 623 BGB                | ✓ / ✗ / Not confirmed |
| Works council consulted (§ 102 / § 103)                     | BetrVG                   | ✓ / ✗ / No WC         |
| Integrationsamt consent (if SGB IX applies)                 | § 168 SGB IX             | ✓ / ✗ / N/A           |
| SBV consulted before Integrationsamt (if SGB IX)            | § 178 Abs. 2 SGB IX      | ✓ / ✗ / N/A           |
| State authority approval (if MuSchG/BEEG)                   | MuSchG § 17 / BEEG § 18  | ✓ / ✗ / N/A           |
| § 103 BetrVG works council affirmative consent (WC members) | BetrVG § 103             | ✓ / ✗ / N/A           |
| Two-week deadline for extraordinary dismissal observed      | § 626 Abs. 2 BGB         | ✓ / ✗ / N/A           |
| Notice period correct                                       | § 622 BGB / Tarifvertrag | ✓ / ✗                 |
| Massenentlassung notification filed (if threshold met)      | §§ 17–18 KSchG           | ✓ / ✗ / N/A           |
| § 1a offer included in notice (if intended)                 | § 1a KSchG               | ✓ / ✗ / N/A           |

**Critical rule — § 623 BGB written form:** Dismissal by email, text message, fax, oral
communication, or DocuSign is **void** — the statute expressly excludes electronic form.
This defect cannot be cured retroactively.

**Three-week claim period — § 4 KSchG:** The employee has **three weeks from receipt** of
the written notice to file a Kündigungsschutzklage. Failure voids the right to challenge
regardless of the dismissal's actual legality (§ 7 KSchG). For employees, this deadline
is critical and should be flagged prominently.

---

## Severity Classification Framework

Classify every identified issue using this three-tier system:

### RED — Legal Invalidity Risk

The defect renders the dismissal void or creates a high-probability labor court loss.
Immediate corrective action required before proceeding.

**Triggers:**

- Special protection category: no required prior approval/consent
- § 102/103 BetrVG consultation entirely omitted
- § 623 BGB written form violated
- Two-week deadline (§ 626 Abs. 2 BGB) missed for extraordinary dismissal
- No valid Abmahnung where required for conduct dismissal
- No social justification (§ 1 KSchG) and KSchG applicable
- Massenentlassung notification omitted (pending CJEU outcome)

**Action:** Do not proceed without remediation. Identify the only available corrective path
(e.g., re-run consultation, obtain required approval, revert to ordinary dismissal route).

### YELLOW — Material Procedural/Substantive Risk

The issue creates meaningful exposure in labor court proceedings but does not make the
dismissal automatically void. Remediation is strongly advisable.

**Triggers:**

- Sozialauswahl documentation incomplete or group composition arguable
- Abmahnung technically deficient (does not name specific conduct precisely)
- Notice period calculation error (incorrect date; age-exclusion rule applied)
- Works council objection under § 102 Abs. 3 BetrVG — continuation right triggered
- BEM not offered prior to illness dismissal
- § 1a KSchG offer mechanics defective
- HinSchG retaliation presumption triggered

**Action:** Document remediation steps. If proceeding, quantify settlement risk at Step 10.

### GREEN — Compliant or Accepted Risk

The aspect is procedurally and substantively sound, or any deviation is within an
acceptable risk range given the specific facts.

**Triggers:**

- All statutory procedural steps completed and documented
- Social justification well-founded on the stated facts
- Sozialauswahl criteria applied and documented with a defensible Punkteschema
- Notice period correctly calculated and stated

**Action:** Record for audit trail. Flag any residual uncertainty with [VERIFY].

---

## Actionable Output per Finding

For every RED or YELLOW finding, provide:

1. **Issue**: Name the specific legal defect
2. **Statutory basis**: The provision violated (e.g., § 102 Abs. 1 S. 3 BetrVG)
3. **Consequence**: What happens if unaddressed (void dismissal / court loss risk)
4. **Remediation**: The specific corrective step available; if none exists, state so
5. **Settlement estimate**: Where the issue would likely affect Abfindung quantum

---

## Prioritization Framework

Where multiple issues exist, prioritize remediation in this order:

**Tier 1 — Absolute Blockers (address before any dismissal notice is issued)**

- Any special protection category without required prior approval
- § 102/103 BetrVG consultation not yet completed
- § 623 BGB written form not prepared
- § 626 Abs. 2 BGB two-week deadline about to expire

**Tier 2 — Pre-Issuance Improvements (address before notice if possible)**

- Strengthen Sozialauswahl documentation
- Prepare/verify Abmahnung file for conduct dismissal
- Conduct BEM for illness dismissal
- Draft § 1a KSchG offer text if intended
- Prepare Massenentlassung notification if threshold met

**Tier 3 — Litigation Mitigation (address if proceedings are filed)**

- Assess settlement value based on § 10 KSchG caps and market norms
- Evaluate works council objection strategy
- Prepare evidence file for Arbeitsgericht proceedings

---

## Citation Quality Gates

Run these 5 gates silently before delivering output. Revise if any gate fails.

| Gate           | Rule                                                                                                                                      | Fail Action                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute (§ number + law name) or established BAG principle                                             | Add citation or mark "[UNVERIFIED — counsel to confirm]"         |
| **Format**     | German statutory citations use standard German citation format (§ X Abs. Y S. Z [Statute])                                                | Fix format                                                       |
| **Currency**   | Every cited provision verified for amendments against gesetze-im-internet.de                                                              | Flag "[CHECK CURRENCY — may have been amended]"                  |
| **Domain**     | Analysis stays within German law; no assumptions from other jurisdictions                                                                 | Remove or flag jurisdictional bleed with [JURISDICTION-SPECIFIC] |
| **Confidence** | Uncertainty explicitly stated — especially for pending CJEU referral, disputed BAG positions, or regional Landesarbeitsgericht divergence | Add confidence qualifier                                         |

---

## Self-Interrogation for RED Items

For every RED finding, apply this 3-pass review before delivering the analysis:

**Pass 1 — Legal Chain Integrity:**

- Does the void-risk conclusion follow logically from the statutory provision cited?
- Would a BAG chamber or Landesarbeitsgericht actually reach this conclusion on these facts?
- Has the employer's strongest counter-argument been considered?

**Pass 2 — Completeness:**

- Have all relevant statutes, regulations, and BAG principles been considered?
- Are there special protection category dimensions not yet assessed?
- Has the Massenentlassung threshold been checked?
- Has the BetrVG § 102/103 consultation been fully assessed?

**Pass 3 — Challenge:**

- What is the strongest argument that the dismissal is valid despite this issue?
- Under what factual circumstances might a Landesarbeitsgericht uphold the dismissal?
- Is the RED classification proportionate, or does this risk reduce to YELLOW with mitigations?

If any pass reveals a weakness, revise the analysis. Mark: `self_interrogation: PASS` or
`self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                              | Action                                                |
| ------------ | --------- | -------------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled BAG authority, clear statute                                 | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong BAG authority, minor interpretation questions                 | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; BAG divergence or LAG conflict                       | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; pending CJEU referral or unsettled BAG position | Flag for Fachanwalt review with both sides            |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                              | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Specific application for pending issues:**

- Massenentlassung notification voidness: **Possible** — pending CJEU referral (BAG 2 AS 22/23 (A))
- Age-exclusion rule (§ 622 Abs. 2 S. 2 BGB): **Probable** — EU compatibility contested
- Disability waiting-period BEM obligation: **Possible** — Arbeitsgericht Köln (Dec. 2023) contested

---

## Glass Box Audit Trail

Append this YAML block to every analysis:

```yaml
glass_box:
  skill_name: "legalcode-de-kuendigungsschutz"
  analysis_date: "[date]"
  perspective: "[Employer / Employee / Neutral audit]"
  employee_name_or_role: "[anonymised if required]"
  establishment_headcount: "[weighted count or 'Not confirmed']"
  kschg_applicable: "[YES / NO / THRESHOLD UNCERTAIN]"
  kschg_basis:
    waiting_period_met: "[YES / NO — [months]]"
    headcount_threshold_met: "[YES / NO — [weighted count]]"
  special_protection_categories: "[list or None]"
  dismissal_type: "[betriebsbedingt / personenbedingt / verhaltensbedingt / außerordentlich / Aufhebungsvertrag / Not determined]"
  works_council_exists: "[YES / NO / Unknown]"
  betrvg_102_103_status: "[Completed / Not yet completed / Not applicable / VOID RISK]"
  sozialauswahl_required: "[YES / NO]"
  sozialauswahl_assessed: "[YES / NO / N/A]"
  notice_period_calculated: "[X months / Not applicable]"
  abfindung_route: "[§ 1a KSchG / §§ 9-10 KSchG / Sozialplan / Negotiated / None identified]"
  massenentlassung_threshold_triggered: "[YES / NO / Not confirmed]"
  red_findings: "[number]"
  yellow_findings: "[number]"
  legalcode_mcp: "Connected / Not connected"
  statutes_cited:
    - "KSchG §§ 1, 1a, 4, 7, 9, 10, 15, 17, 18, 23 — [VERIFIED / UNVERIFIED]"
    - "BGB §§ 138, 622, 623, 626 — [VERIFIED / UNVERIFIED]"
    - "BetrVG §§ 15, 76, 77, 99, 102, 103, 111–113 — [VERIFIED / UNVERIFIED]"
    - "SGB IX §§ 168–175, 178 — [VERIFIED / UNVERIFIED]"
    - "MuSchG § 17 — [VERIFIED / UNVERIFIED]"
    - "BEEG § 18 — [VERIFIED / UNVERIFIED]"
    - "BDSG §§ 6, 38 — [VERIFIED / UNVERIFIED]"
    - "BBiG § 22 — [VERIFIED / UNVERIFIED]"
    - "EStG §§ 24, 34 — [VERIFIED / UNVERIFIED]"
  bag_cases_cited:
    - "[Case reference] — [VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  pending_legal_developments:
    - "CJEU referral BAG 2 AS 22/23 (A) — Massenentlassung notification voidness — outcome pending"
    - "EU Pay Transparency Directive — implementation deadline June 2026"
    - "Fünftelregelung moved to employee self-assessment effective 1 January 2025"
  reviewer: "AI-assisted — requires review by Fachanwalt für Arbeitsrecht"
```

---

## Anti-Patterns

What NOT to do when analysing German dismissal protection:

1. **Skipping the KSchG threshold check** — Proceeding to social justification analysis
   without confirming the six-month waiting period and headcount threshold are both met.
   The entire KSchG analysis is irrelevant if either threshold fails.

2. **Ignoring special protection categories** — Analysing social justification without
   first running the special protection check. A socially justified dismissal is still
   void without the required prior approval or consent.

3. **Treating BetrVG § 102 as a formality** — Underestimating the Anhörungsdefizit risk.
   An incomplete works council notification is as fatal as no consultation at all. The
   employer's notification must match the employer's actual reliance basis.

4. **Missing the two-week deadline for § 626 BGB** — Proceeding with extraordinary
   dismissal analysis without flagging the hard two-week exclusion deadline. A missed
   deadline voids the extraordinary dismissal regardless of the merits; the employer is
   then relegated to ordinary dismissal if KSchG applicable.

5. **Applying electronic form to dismissal notices** — Advising that a PDF, email, DocuSign,
   or fax dismissal is valid. § 623 BGB expressly and unambiguously excludes electronic
   form. This is one of the most common and costly errors in practice.

6. **Omitting the Abmahnung analysis for conduct dismissals** — Assuming an extraordinary
   dismissal is available for any conduct breach without checking whether a prior formal
   warning was required. The Emmely line of cases establishes that even trivial dishonesty
   may require a prior warning where the employee's service record is long and unblemished.

7. **Narrowing the Sozialauswahl group without justification** — Accepting the employer's
   defined comparison group without examining whether it is correctly drawn. Courts
   scrutinise group composition — a too-narrow group that conveniently excludes a better-
   protected employee will void the selection.

8. **Confusing the establishment (Betrieb) with the company (Unternehmen)** — The § 23
   KSchG headcount threshold is measured at the establishment level, not the company or
   group level. A company with 500 employees may have individual establishments below the
   10-employee threshold.

9. **Ignoring the Freikündigungsgrundsatz for operational dismissals** — Failing to check
   whether any comparable position exists within the establishment or undertaking before
   classifying an operational dismissal as unavoidable. The employer must fill the position
   with the dismissed employee if one is available, even if that requires reasonable
   retraining.

10. **Confusing § 9/10 KSchG severance caps with market settlement values** — The §§ 9–10
    KSchG caps apply to court-awarded severance where the court dissolves the employment
    relationship. Negotiated Aufhebungsverträge and settlement agreements are not bound by
    these caps — they can exceed the statutory maximum. Mis-advising a client that the cap
    limits their negotiating position is a significant error.

11. **Overlooking the Nachteilsausgleich route (§ 113 BetrVG)** — In restructurings where
    a Betriebsänderung occurs, failing to advise on the § 113 compensation claim where the
    employer has bypassed Interessenausgleich negotiations. This is an independent severance
    entitlement that exists regardless of whether a Sozialplan was agreed.

12. **Applying the Fünftelregelung calculation at employer payroll level post-2025** — Since
    1 January 2025, the employer no longer applies the Fünftelregelung at payroll tax level.
    Gross/net severance calculations must reflect this change — the employee receives a
    larger gross amount withheld at the standard marginal rate, then reclaims the benefit
    through self-assessment.

13. **Treating all DPO dismissal restrictions as equivalent** — The enhanced § 626 BGB
    dismissal protection for DSBs under BDSG § 6 Abs. 4 applies only to legally mandated
    DPO appointments. Voluntary DPO appointments do not attract this protection. Conflating
    the two can either over-advise (protecting a non-protected DPO) or under-advise (failing
    to protect a mandatory DPO).

14. **Ignoring the HinSchG retaliation presumption** — Where dismissal follows a protected
    report under the Hinweisgeberschutzgesetz, the burden of proof shifts to the employer
    to prove an independent lawful basis. Failing to identify this reversal can materially
    mis-state the employer's litigation position.

15. **Citing pending CJEU outcomes as settled law** — Stating that defective Massenentlassung
    notifications render dismissals void, without noting that the BAG's 2024 CJEU referral
    (2 AS 22/23 (A)) has cast this doctrine into genuine uncertainty. The current law should
    be presented as a **Probable** rather than **Definite** position until the CJEU rules.

16. **Single-pass analysis without cross-checking procedural requirements** — Reading through
    the dismissal facts once without then returning to the procedural compliance checklist.
    Social justification analysis and procedural compliance must both be completed — a
    procedurally perfect dismissal may lack social justification, and a substantively sound
    ground may be voided by procedural error.

---

## Writing Standards

Apply plain-language discipline to all output:

**For employer-facing risk assessments:**

- Use German legal terms with English glosses on first use: "Sozialauswahl (social selection)"
- Active voice: "The employer must obtain Integrationsamt consent" — not "Consent of the
  Integrationsamt must be obtained"
- Name specific statutory provisions: "§ 102 Abs. 1 S. 3 BetrVG" — not "the consultation requirement"
- Avoid euphemism for void risks: state "this dismissal is void" not "this may create issues"

**For employee-facing analysis:**

- Highlight the § 4 KSchG three-week deadline prominently and in plain language
- Explain the Gütetermin process and likelihood of settlement
- Provide a realistic severance range, not just the § 10 KSchG maximum cap

**Quality gates before delivery:**

1. Does every RED finding state the specific statute violated and the consequence (void/loss)?
2. Is every Abfindung range grounded in § 1a KSchG, § 10 KSchG, or market norms — not guesswork?
3. Are all pending legal developments (CJEU referral, 2025 tax change) flagged?
4. Has the procedural compliance checklist been completed for every dismissal?
5. Is the Glass Box audit trail appended?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current BAG decisions on the specific dismissal ground
- Verify current statutory text on gesetze-im-internet.de via the MCP
- Search for Landesarbeitsgericht decisions in the relevant federal state for jurisdiction-
  specific nuances (LAG decisions are not binding but may predict first-instance outcomes)
- Confirm current Massenentlassung CJEU referral status
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and BAG case citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus enhancement on structural completeness and procedural checklist
- Recommend verification of all statutory citations against gesetze-im-internet.de before
  any action is taken

**Authoritative free sources for manual verification:**

- gesetze-im-internet.de — current statutory text (maintained by BMJ/BfJ)
- bundesarbeitsgericht.de — full-text BAG decisions
- dejure.org — annotated statutes with BAG citations

---

## Output Format Template

```markdown
## Kündigungsschutz Analysis

**Employee / Role**: [anonymised identifier]
**Establishment**: [employer name or anonymised]
**Perspective**: [Employer / Employee / Neutral]
**Analysis Date**: [date]
**Scenario**: [brief description of dismissal scenario]

---

## 1. KSchG Applicability

**Waiting period**: [months] — [Met / Not met]
**Headcount**: [weighted count] — [Above / Below / Uncertain re § 23 threshold]
**KSchG Status**: [APPLICABLE / NOT APPLICABLE / THRESHOLD UNCERTAIN]

If not applicable: [list minimum protections that still apply]

---

## 2. Special Protection Assessment

| Category                              | Applicable? | Status                                        | Risk             |
| ------------------------------------- | ----------- | --------------------------------------------- | ---------------- |
| MuSchG § 17 (pregnancy)               | [YES/NO]    | [approval obtained / not obtained / N/A]      | [RED/GREEN/N/A]  |
| BEEG § 18 (parental leave)            | [YES/NO]    | [approval obtained / not obtained / N/A]      | [RED/GREEN/N/A]  |
| SGB IX §§ 168–175 (severely disabled) | [YES/NO]    | [consent obtained / not obtained / N/A]       | [RED/GREEN/N/A]  |
| BetrVG §§ 15, 103 (WC member)         | [YES/NO]    | [§ 103 consent obtained / not obtained / N/A] | [RED/GREEN/N/A]  |
| BDSG §§ 6/38 (DPO)                    | [YES/NO]    | [mandatory appointment? / N/A]                | [RED/YELLOW/N/A] |
| BBiG § 22 (trainee)                   | [YES/NO]    | [post-Probezeit? / N/A]                       | [RED/GREEN/N/A]  |
| HinSchG (whistleblower)               | [YES/NO]    | [report preceded dismissal? / N/A]            | [YELLOW/N/A]     |

---

## 3. Social Justification Analysis (if KSchG Applicable)

**Dismissal Ground**: [betriebsbedingt / personenbedingt / verhaltensbedingt]

### [Ground-specific analysis]

| Issue       | Classification       | Remediation |
| ----------- | -------------------- | ----------- |
| [Finding 1] | RED / YELLOW / GREEN | [Action]    |
| [Finding 2] | RED / YELLOW / GREEN | [Action]    |

---

## 4. Sozialauswahl Analysis (betriebsbedingte Kündigung only)

**Comparison Group**: [description]
**Criteria Applied**:

- Betriebszugehörigkeit: [assessment]
- Lebensalter: [assessment]
- Unterhaltspflichten: [assessment]
- Schwerbehinderung: [assessment]

**Punkteschema**: [agreed / not agreed / [VERIFY] ]
**Selection Result**: [GREEN / YELLOW / RED]

---

## 5. Notice Period

**Probezeit**: [Yes / No]
**Length of service**: [X years Y months]
**Applicable notice period**: [X months] to [15th / end of month]
**Stated notice period**: [X months]
**Assessment**: [Correct / SHORT — RED / Long — acceptable]

---

## 6. Works Council Consultation (§ 102 / § 103 BetrVG)

**Works council exists**: [YES / NO]
**Consultation completed**: [YES / NO / In progress]
**Notification complete**: [YES / NO / [VERIFY] ]
**Deadline**: [Ordinary: 1 week / Extraordinary: 3 days / § 103 consent]
**Works council response**: [No objection / Objection — continuation right triggered / Consent obtained / Pending]
**Assessment**: [GREEN / YELLOW / RED]

---

## 7. Massenentlassung (§§ 17–18 KSchG)

**Threshold triggered**: [YES / NO / Not confirmed]
**Agentur notification**: [Filed / Not filed / N/A]
**Assessment**: [GREEN / RED — VOID RISK (pending CJEU) / N/A]

---

## 8. Abfindung Assessment

**Applicable routes**:

- § 1a KSchG: [Available / Not available (non-operational dismissal)] — [Calculated amount if applicable]
- §§ 9–10 KSchG: [Maximum cap — [X months' salary]]
- Sozialplan: [Applicable / Not applicable]

**Market settlement estimate**: [Low: X — High: Y months' salary]
**Fünftelregelung note**: Since 1 January 2025, employee must claim through self-assessment.

---

## 9. Procedural Compliance Checklist

| Requirement                                       | Status                |
| ------------------------------------------------- | --------------------- |
| § 623 BGB written form — hand-signed              | ✓ / ✗ / Not confirmed |
| § 102/103 BetrVG consultation                     | ✓ / ✗ / N/A           |
| Special protection prior approval                 | ✓ / ✗ / N/A           |
| § 626 Abs. 2 BGB two-week deadline                | ✓ / ✗ / N/A           |
| § 4 KSchG — three-week challenge deadline flagged | ✓ / ✗                 |

---

## 10. Summary and Prioritized Action List

**Overall Risk**: [HIGH — RED findings / MEDIUM — YELLOW findings only / LOW — GREEN]

**Tier 1 — Act Before Issuing Notice**:

1. [Action]

**Tier 2 — Improve Before Issuance**:

1. [Action]

**Tier 3 — Litigation Preparation**:

1. [Action]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

- Use German legal terminology in operative sections with English glosses on first use.
- Be precise about the **Betrieb** (establishment) vs. **Unternehmen** (undertaking) vs.
  **Konzern** (group) distinction — many rights and thresholds operate at the Betrieb level.
- Regional differences: some Bundesländer use different names for the state authority
  responsible for MuSchG/BEEG approvals (e.g., Gewerbeaufsichtsamt, Landesamt für
  Verbraucherschutz und Veterinärwesen, RP Darmstadt). The generic term is "zuständige
  Behörde" — recommend the user verify the competent authority in the relevant state.
- Collective agreements (Tarifverträge) frequently modify statutory defaults on notice
  periods, Sozialplan formulas, and probationary periods. Always flag whether the employer
  is tarifgebunden (bound by a collective agreement) and what sector tariff applies.
- For bilingual international teams, provide German-language summaries of the key risk
  points for use in works council communications and board resolutions.
- German-controlled language requirements: dismissal notices should be drafted in German
  (or at minimum in the employee's contractual language) to ensure receipt (Zugang) is
  unambiguous.

---

## Provenance

Legalcode original synthesis created 2026-03-21.

Primary legal sources consulted:

- German federal statutes (KSchG, BGB, BetrVG, SGB IX, MuSchG, BEEG, BDSG, BBiG, EStG,
  HinSchG) via gesetze-im-internet.de
- Bundesarbeitsgericht decisions: BAG 2 AZR 541/09 (Emmely), BAG 2 AZR 519/11
  (Interessenausgleich presumption), BAG 2 AZR 468/08 (Sozialauswahl age criteria),
  BAG 2 AZR 42/10 (entrepreneurial decision review), BAG 2 AZR 404/11 (gross error
  standard), BAG 2 AZR 955/11 (Emmely refinement), BAG 2 AZR 582/13 (illness prognosis)
- BAG 2 AS 22/23 (A) — CJEU referral on Massenentlassung notification voidness (February 2024)
- ICLG Germany Employment and Labour Laws and Regulations 2025–2026
- L&E Global Germany Employment Law Overview (Termination section)
- Bird & Bird Germany Employment Law Horizon Scanning 2025
- Gleiss Lutz commentary on BAG Massenentlassung referral
- Kliemt.blog: illness dismissal three-stage test; DPO Sonderkündigungsschutz;
  Wartezeit dismissal pitfalls; mass dismissal developments
- Bundesfinanzministerium guidance on Fünftelregelung changes effective January 2025

No external SKILL.md content was imported.
