---
name: legalcode-pl-employment-agreement
description: Draft or review Polish employment agreements (umowa o pracę) under the Kodeks pracy (Labour
  Code).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft or review Polish employment agreements (umowa o pracę) under the Kodeks pracy (Labour Code). Covers all mandatory content requirements (Art. 29 KP), probation period rules (Art. 25 KP), fixed-term limits (33 months / 3 contracts under Art. 25¹ KP), notice and termination procedures (Art. 36, 52, 53 KP), severance pay, non-compete clauses (zakaz konkurencji — Art. 101¹–101² KP), remote work provisions (Art. 67¹⁹–67³⁶ KP, effective April 7 2023), IP ownership (UPAPP Art. 12, 74; PrWłPrzem Art. 11), personal data and monitoring rules (Art. 22¹–22² KP + GDPR), ZUS contribution structure, and whistleblower protection (Ustawa o ochronie sygnalistów 2024). Also assesses misclassification risk: whether a civil law contract (umowa zlecenia / umowa o dzieło) or B2B arrangement would be reclassified as employment under Art. 22 KP and the 2026 PIP reclassification powers. Triggers on: Polish employment contract, umowa o pracę, kodeks pracy, Polish labour law, zakaz konkurencji Poland, praca zdalna regulations, PIP reclassification risk, Polish fixed-term limit, umowa zlecenia versus employment.


# Legalcode — Polish Employment Agreement (Umowa o Pracę)

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and review of
> Polish employment agreements. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs must be reviewed by a qualified Polish
> employment lawyer (radca prawny or adwokat) before use. Polish labour law changes
> frequently; verify current provisions before relying on any citation. Statutory and
> case law references carry hallucination risk — cross-check against the official
> consolidated text at isap.sejm.gov.pl before acting.

---

## Purpose and Scope

This skill enables AI-assisted drafting and review of Polish employment agreements and
assessment of civil-law contract misclassification risk.

**Operates in three modes:**

| Mode             | Use When                                                                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **A — Draft**    | Creating a new umowa o pracę from scratch                                                                                                 |
| **B — Review**   | Reviewing an existing employment contract (employer-drafted or employee-received)                                                         |
| **C — Classify** | Assessing whether a civil-law contract (zlecenia/dzieło) or B2B arrangement is at risk of reclassification as employment under Art. 22 KP |

**Covers:**

- Mandatory content requirements under Art. 29 KP and the 7-day supplementary information duty
- All three contract types: próbny (trial), czas określony (fixed-term), czas nieokreślony (indefinite)
- 2023 trial period amendments and fixed-term 33-month / 3-contract limits (Art. 25¹ KP)
- Termination: notice periods (Art. 36 KP), fault-based dismissal (Art. 52 KP), medical (Art. 53 KP), severance (redundancy statute)
- Non-compete during and after employment (Art. 101¹–101² KP), including the 25% compensation floor
- Remote work regime (Art. 67¹⁹–67³⁶ KP) — OSH obligations, cost-coverage rules
- Intellectual property: copyright (UPAPP Art. 12, 74), service inventions (PrWłPrzem Art. 11), 50% tax-deductible creative-work cost structures
- Data protection: permissible recruitment data (Art. 22¹ KP), biometrics (Art. 22¹b KP), monitoring (Art. 22² KP), GDPR/UODO
- ZUS social insurance contribution structure and employer costs
- Parental and maternity leave (2023 EU Work-Life Balance Directive implementation)
- Whistleblower protection obligations (Ustawa o ochronie sygnalistów, June 14 2024)
- Anti-discrimination (Art. 18³a–18³e KP), minimum wage compliance

**Does not:**

- Provide legal advice or replace qualified Polish employment counsel
- Cover civil servants (ustawa o służbie cywilnej) or managerial employment (kontrakt menedżerski) which follow different regimes
- Generate ZUS forms (ZUS ZUA / ZUA / ZWUA) or draft PIT tax filings
- Cover collective bargaining agreement (układ zbiorowy pracy) drafting

---

## Jurisdiction and Governing Law

**Governing law:** Republic of Poland. Primary statute: **Ustawa z dnia 26 czerwca 1974 r. —
Kodeks pracy** (KP), consolidated text at Dz.U. 2023 poz. 1465 as amended.

Polish labour law is mandatory — the parties may not contract out of statutory minimum
protections. Art. 18 KP: contractual terms less favourable to the employee than the
statutory minimum are replaced by law with the statutory provision.

For employees working in Poland under a foreign-law employment contract, Polish mandatory
rules still apply by operation of Rome I Regulation (Art. 8) when the employee habitually
carries out work in Poland.

Key legislation:

- **Kodeks pracy (KP)** — employment contracts, working time, leave, termination, non-compete, monitoring
- **Ustawa o szczególnych zasadach rozwiązywania stosunków pracy** — severance and collective redundancy procedures
- **Ustawa z dnia 10 października 2002 r. o minimalnym wynagrodzeniu za pracę** — minimum wage
- **Ustawa z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych (UPAPP)** — copyright
- **Ustawa z dnia 30 czerwca 2000 r. — Prawo własności przemysłowej (PrWłPrzem)** — patents and service inventions
- **Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych (UODO)** + GDPR — personal data
- **Ustawa z dnia 14 czerwca 2024 r. o ochronie sygnalistów** — whistleblower protection
- **Kodeks cywilny (KC)** — civil law contracts (umowa zlecenia Art. 734, umowa o dzieło Art. 627)

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at key decision points. The
workflow pauses and asks when:

- The mode (draft/review/classify) changes the entire analysis direction
- Contract type determines mandatory content and protections
- Employer or employee perspective affects which risks to prioritise
- Ambiguous clauses require business context to classify correctly

Present options as structured choices where possible. If context is already clear from
the conversation, skip the question and state your assumption explicitly.

---

## Key Legal Framework

| Article / Statute                    | Subject                            | Key Rule                                                                                                                             |
| ------------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Art. 22 § 1 KP                       | Employment relationship definition | Work performed personally, under employer direction, at designated time/place, for remuneration = employment by operation of law     |
| Art. 22 § 1¹–1² KP                   | Anti-misclassification             | The contract's name is irrelevant; replacing employment with civil law contract is unlawful if conditions satisfy Art. 22 § 1        |
| Art. 25 KP                           | Contract types                     | Three types: próbny (trial), czas określony (fixed-term), czas nieokreślony (indefinite)                                             |
| Art. 25¹ KP                          | Fixed-term limits                  | Max 3 consecutive fixed-term contracts OR 33 months aggregate; on breach → indefinite by operation of law                            |
| Art. 29 KP                           | Mandatory content                  | Written contract specifying 7 core items; 7-day supplementary information duty                                                       |
| Art. 36 KP                           | Notice periods                     | Length of service → 2 weeks / 1 month / 3 months                                                                                     |
| Art. 52 KP                           | Dismissal without notice (fault)   | Serious breach, crime, own-fault licence loss; 1-month employer deadline                                                             |
| Art. 53 KP                           | Dismissal without notice (medical) | Prolonged illness exceeding protection period; reinstatement right on recovery                                                       |
| Art. 92 KP                           | Employer-funded sick pay           | First 33 days/year (14 days if employee >50); employer-paid at 80% (100% in pregnancy)                                               |
| Art. 101¹ KP                         | Non-compete during employment      | Written form; no compensation required; breach = Art. 52 grounds                                                                     |
| Art. 101² KP                         | Post-employment non-compete        | Minimum 25% of pre-termination remuneration per month of restriction; written form; employee's non-payment right on employer default |
| Art. 154–155¹ KP                     | Annual leave                       | 20 days (<10 years total experience) / 26 days (≥10 years)                                                                           |
| Art. 18³a–18³e KP                    | Anti-discrimination                | Equal treatment obligation; employer bears proof burden; minimum-wage compensation floor                                             |
| Art. 22¹ KP                          | Permissible recruitment data       | Closed list; no marital status, family situation, criminal record (unless legally required)                                          |
| Art. 22¹b KP                         | Biometric data                     | Permissible only with free consent OR access to sensitive areas; timekeeping by fingerprint = unlawful (UODO position)               |
| Art. 22² KP                          | Workplace monitoring               | Purpose required; proportionality; 2-week pre-notification; max 3-month retention                                                    |
| Art. 67¹⁹–67³⁶ KP                    | Remote work                        | Effective April 7, 2023; agreement/regulations basis; employer cost-coverage; OSH obligations; 24-day occasional remote work cap     |
| UPAPP Art. 12                        | Employee copyright works           | Employer acquires economic rights on acceptance; 2-year use-or-lose rule; moral rights inalienable                                   |
| UPAPP Art. 74(3)                     | Software                           | Employer primary acquisition at creation (no intermediate employee holding)                                                          |
| PrWłPrzem Art. 11                    | Service inventions                 | Employer owns inventions arising from employment duties; employee entitled to remuneration from exploitation                         |
| Ustawa o ochronie sygnalistów (2024) | Whistleblower protection           | Mandatory for 50+ employees; anti-retaliation; internal channel required by September 24, 2024                                       |

---

## Workflow

### Step 1: Accept Input and Determine Mode

Accept input in any of these formats:

- **For Mode A (Draft)**: Key facts about the role, employer, employment type, remuneration, location, and any special provisions needed
- **For Mode B (Review)**: An existing employment contract as text, file, or URL
- **For Mode C (Classify)**: A civil law contract (umowa zlecenia / umowa o dzieło), B2B arrangement, or description of actual working conditions

**⟁ CLARIFY** — If the mode is ambiguous, ask:

> "Which mode applies here?
>
> - **A — Draft**: Create a new umowa o pracę from scratch
> - **B — Review**: Analyse an existing Polish employment (or civil-law) contract
> - **C — Classify**: Assess whether a civil-law / B2B arrangement is at risk of being
>   reclassified as employment by PIP or a labour court"

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before proceeding, ask (skip questions already answered):

1. **Perspective**:
   - Options: Employer (drafting or reviewing before issuance), Employee (reviewing before signing), HR/Legal advisor (neutral review)
   - _Why_: Priorities differ — employer wants flexibility, employee wants protections.

2. **Contract type intended**:
   - Options: Umowa na czas nieokreślony (indefinite), Umowa na czas określony (fixed-term), Umowa na okres próbny (trial period)
   - _Why_: Mandatory content and legal constraints differ per type.

3. **Sector / Industry**:
   - Options: Technology/IT, Manufacturing, Finance, Healthcare, Retail, Professional services, Other
   - _Why_: Sector determines applicable sectoral minimum wages, collective agreement (układ zbiorowy pracy) requirements, and typical non-compete scope. The 50% copyright cost deduction requires identifying roles where creative output is a primary duty.

4. **Special provisions needed** (select all that apply):
   - Remote work (praca zdalna)
   - Post-employment non-compete (zakaz konkurencji po ustaniu)
   - IP-intensive role (software, creative content, R&D)
   - 50% tax-deductible creative cost structure (koszty uzyskania przychodu 50%)
   - Confidentiality obligations
   - Relocation / mobility clause

5. **Deadline**: When must the agreement be finalised?
   - Options: Immediate (same day), 48 hours, 1 week, Flexible

---

### Step 3: Research Legal Authority

Search **legalcode-mcp** for current Polish employment law authority on the specific
issues raised by the contract. If not connected, proceed with the research below and
mark all statutory citations [VERIFY].

Save findings to `/tmp/legalcode-pl-employment-research.md`:

```markdown
# Legal Authority — Polish Employment Agreement

## Date: [date]

### Current statutory provisions verified:

- Art. 29 KP — mandatory content (isap.sejm.gov.pl)
- Art. 25¹ KP — fixed-term limits (current consolidated text)
- 2026 minimum wage: PLN 4,806 gross/month (PLN 31.40/hour) [Dz.U. 2025]
- ZUS contribution rates current as of [date]

### Collective agreement applicable:

- [Industry/sector CCN or "None identified"]

### Recent developments:

- 2023 trial period amendments (effective April 26, 2023)
- 2023 remote work regime (effective April 7, 2023)
- 2024 whistleblower protection (effective September 25, 2024)
- 2026 PIP reclassification powers (Sejm resolution March 11, 2026)
```

---

### Step 4: Core Analysis

Proceed with the mode-specific analysis below.

---

## Mode A: Draft Employment Agreement

### A1. Mandatory Elements — Art. 29 KP

Every umowa o pracę **must** specify all of the following in writing:

| #   | Required Element                       | Drafting Note                                                                                              |
| --- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1   | **Parties**                            | Full legal name, registered address, and NIP (tax ID) for employer; full name, PESEL, address for employee |
| 2   | **Type of contract**                   | State explicitly: "umowa na czas nieokreślony / określony / na okres próbny"                               |
| 3   | **Date of conclusion**                 | The date the contract is signed                                                                            |
| 4   | **Type of work (rodzaj pracy)**        | Job title + brief description of duties; must be specific enough to define the role                        |
| 5   | **Workplace location (miejsce pracy)** | Physical address; for remote/hybrid work, specify accordingly (see Clause 9 below)                         |
| 6   | **Remuneration**                       | Gross monthly salary + itemised breakdown of all components (base salary, bonuses, allowances)             |
| 7   | **Working time dimension**             | Full-time (pełny etat) or fraction thereof (e.g., ½ etatu)                                                 |
| 8   | **Work commencement date**             | Must appear; if future, include the specific date                                                          |

**Consequence of omission**: If not in writing before start of work, employer must confirm in writing **on the first day** (Art. 29 § 2 KP). Failure to issue a written contract is a misdemeanour under Art. 281 § 1 KP (fine up to PLN 30,000).

### A2. Seven-Day Supplementary Information Duty — Art. 29 § 3 KP

Within **7 days** of employment commencement, the employer must deliver (in paper or
electronic form) supplementary information covering:

- Daily and weekly working time norms applicable to the employee
- Reference period for working time calculation
- Overtime supplement rates
- Rest break and daily/weekly rest period entitlements
- Night-shift rules (if applicable)
- Leave entitlement (including type and dimension)
- Notice period rules applicable to the contract
- Any collective agreements applicable

**⟁ CLARIFY** — The supplementary information may be included in the employment contract
itself (saves administrative effort) or delivered in a separate document. Ask whether to
integrate it into the draft or prepare as a separate Annex.

### A3. Contract Type and Duration Rules

**Trial period (umowa na okres próbny — Art. 25 § 2–3 KP):**

- Intended future contract ≥ 12 months (or indefinite) → max **3 months** trial
- Intended future contract ≥ 6 months but < 12 months → max **2 months** trial
- Intended future contract < 6 months → max **1 month** trial
- The trial period clause must state its duration and, if shorter than 3 months, must
  reference the intended future contract duration
- Extension by up to 1 additional month permitted for 1- or 2-month trials if justified
  by type of work
- Re-hiring on trial: permitted only if (a) different type of work, or (b) same type
  of work but at least **3 years** elapsed since prior employment ended

**Fixed-term (umowa na czas określony — Art. 25¹ KP):**

- Maximum **3 consecutive fixed-term contracts** with the same employer
- Maximum aggregate duration of **33 months** across all fixed-term contracts
- On reaching either limit (whichever comes first), the next or continuing contract
  is **deemed indefinite by operation of law** — no action needed by either party
- Trial period contracts do NOT count toward either limit
- Draft a clear expiry date; do not use "until project completion" formulations as these
  create duration uncertainty [VERIFY — some courts accept project-tied durations]

**Indefinite-term (umowa na czas nieokreślony — Art. 25 § 1 KP):**

- The default form affording maximum employee protection
- No expiry date; termination requires substantive justification and procedural compliance

---

## Mode B: Review Employment Agreement

Analyse the contract clause by clause against the mandatory requirements and market
standards below. For each clause assess: ZGODNY (compliant), RYZYKO (issue/risk), or
NIEWAŻNY (void / unenforceable by operation of law).

### B1. Clause Analysis Reference

#### Clause 1: Parties and Contract Identification

**Review points:**

- All 8 mandatory Art. 29 KP elements present?
- Contract type stated explicitly?
- Work commencement date present?
- Are there inconsistencies between the stated contract type and the actual intended
  duration or renewal terms?

**RED flags:**

- Missing mandatory elements → automatic NIEWAŻNY risk for specific provisions
- Contract labelled "umowa zlecenia" but with characteristics of employment → reclassification exposure (see Mode C)

#### Clause 2: Trial Period

**Review points:**

- Is the trial duration proportionate to the intended follow-on contract under 2023 rules?
- Does a 3-month trial indicate an intended indefinite or 12-month+ fixed-term continuation?
- Is the possibility of re-hiring on trial correctly limited?

**RED flags (NIEWAŻNY):**

- Trial period exceeding 3 months → the excess is void; contractual duration is limited to statutory maximum
- Re-hiring on trial for same work type within 3-year window → void

#### Clause 3: Remuneration

**Review points:**

- Is gross salary at or above the minimum wage (PLN 4,806/month from January 2026 for full-time)?
- Are all remuneration components itemised (base + bonuses + allowances)?
- Is there a variable pay clause? If so, is the calculation method specified?
- Is the pay period stated (monthly is standard; at least once a month on a fixed date — Art. 85 KP)?

**RED flags:**

- Remuneration below minimum wage → Art. 18 KP replacement by statutory minimum; employer misdemeanour liability
- "Remuneration per agreement" or cross-reference to unattached schedule → ambiguity; recommend full specification

#### Clause 4: Working Time

**Review points:**

- Does the contract specify the working time dimension (full / fractional)?
- If less than full-time, is the overtime threshold for the employee set (Art. 151 § 5 KP — parties must set the hours above which part-time employee receives overtime supplement)?
- Are overtime rules aligned with Art. 151–151⁴ KP (150-hour annual limit; supplement rates)?

**RED flags:**

- Part-time contract with no overtime threshold clause → employer owes supplement from first hour above contractual hours
- Unlimited overtime obligation without supplement → NIEWAŻNY; void against statutory overtime rules

#### Clause 5: Fixed-Term Duration (if applicable)

**Review points:**

- Is this the 2nd or 3rd fixed-term contract? If so, has the 33-month aggregate been checked?
- Is this the 3rd consecutive fixed-term contract? The next renewal is indefinite by law.
- Does the contract incorrectly attempt a 4th fixed-term contract?

**RED flags:**

- 4th fixed-term contract purported → void as to fixed-term character; indefinite by operation of Art. 25¹ KP
- 33-month aggregate exceeded → indefinite by operation of law from that date

#### Clause 6: Annual Leave

**Review points:**

- Leave entitlement stated (20 or 26 days)?
- If stated, is it consistent with the employee's total seniority across all employers (including study periods counted per Art. 155 KP)?
- Is the accrual rule for the first year of employment correctly set (1/12 per completed month)?
- Are the 4 "on demand" days (urlop na żądanie — Art. 167² KP) referenced?

**RED flags:**

- Stating 20 days for an employee who qualifies for 26 → NIEWAŻNY; statutory entitlement prevails
- Purporting to reduce annual leave below statutory minimum → NIEWAŻNY

#### Clause 7: Notice Periods

**Review points:**

- Notice periods compliant with Art. 36 KP thresholds?
- Are shorter-than-statutory notice periods purported by contract?

**Table — Statutory notice periods (Art. 36 § 1 KP):**

| Employment length with current employer | Notice period |
| --------------------------------------- | ------------- |
| < 6 months                              | 2 weeks       |
| ≥ 6 months, < 3 years                   | 1 month       |
| ≥ 3 years                               | 3 months      |

**For trial period contracts (Art. 34 KP):**

| Trial period duration | Notice period  |
| --------------------- | -------------- |
| ≤ 2 weeks             | 3 working days |
| > 2 weeks, ≤ 3 months | 1 week         |
| 3 months              | 2 weeks        |

**RED flags:**

- Shorter notice periods than statutory minimums → NIEWAŻNY; statutory periods apply
- Asymmetric notice periods (shorter for employer than employee) → assess enforceability; courts may equate them
- Note: art. 36 § 6 KP — employer may unilaterally release employee from work duty during notice period while paying full remuneration (garden leave); clause is optional but useful to include

#### Clause 8: Termination for Cause

**Review points:**

- Are grounds for dismissal without notice consistent with Art. 52 KP?
- Contract must not purport to expand or restrict Art. 52 grounds beyond the statute
- Is the 1-month employer deadline for exercising Art. 52 rights referenced?
- Is trade union consultation (Art. 52 § 3 KP — required if employee is a union member or is represented by a union) addressed?

**RED flags:**

- Broad contractual "termination for cause" that exceeds Art. 52 — employer may still be liable for wrongful termination
- Missing reference to the 21-day employee remedy period (Art. 264 § 1 KP — claim to labour court)

#### Clause 9: Non-Compete (Zakaz Konkurencji)

**During employment — Art. 101¹ KP:**

- Written form required (ad solemnitatem; verbal clause is NIEWAŻNY)
- Scope of prohibited activity must be defined (subject matter + geographic scope)
- No compensation required; obligation is a condition of employment
- Breach = serious duty violation → Art. 52 § 1(1) dismissal grounds

**Post-employment — Art. 101² KP:**

- Written form required (ad solemnitatem)
- Employee must have access to "particularly important information" — courts scrutinise; overly broad application is challenged
- Compensation: minimum **25% of the pre-termination monthly remuneration** for each month of restriction
- Duration must be stated (courts accept 6–24 months; longer periods require strong justification)
- Geographic scope must be proportionate
- If the employer fails to pay compensation → employee is released from the restriction immediately
- Consider whether the agreement should include an employer termination right (e.g., if commercial situation changes)
- **Calculation example**: 12-month non-compete on PLN 10,000 gross salary → minimum PLN 30,000 total compensation (25% × PLN 10,000 × 12 months)

**RED flags:**

- Post-employment non-compete without compensation clause → NIEWAŻNY (Art. 101² § 1 KP requires compensation as essential element)
- Compensation rate below 25% → NIEWAŻNY as to the deficit; courts will supplement to 25%
- Non-compete binding all employees regardless of access to sensitive information → potential NIEWAŻNY challenge; should be limited to qualifying employees

#### Clause 10: Remote Work (Praca Zdalna)

**Applicable where remote or hybrid work is intended — Art. 67¹⁹–67³⁶ KP:**

Remote work must be established in one of:

1. An agreement with the trade union / works council (porozumienie ze związkiem zawodowym)
2. Employer remote work regulations (regulamin pracy zdalnej) — if no collective agreement reached within 30 days
3. Individual agreement between employer and employee (where no collective arrangement)

The employment contract or remote work agreement must address:

- Frequency of remote work (wholly remote / hybrid / ad hoc)
- Location(s) where remote work may be performed
- Employee confirmation that the remote workstation meets OSH (BHP) requirements
- Equipment provision (employer's or employer-equivalent payment for employee's equipment)
- Cost reimbursement mechanism (electricity, telecommunications) — or agreed lump sum
- Rules for employer inspection of the remote workstation (prior notice required; occupant consent required if workstation is not at employee's exclusive address)
- Communication and availability expectations

**Occasional remote work (praca zdalna okazjonalna):**

- Up to 24 days/year at employee request
- Simplified procedure — no formal remote work rules needed
- Employer may refuse on operational grounds
- Full employer OSH obligation does NOT apply in this mode

**Tax treatment of equipment/cost coverage:** Provision of equipment and cost reimbursement lump sums are income-tax exempt for the employee (not subject to PIT).

**RED flags:**

- Employment contract states remote work without covering required cost reimbursement → employer liability exposure
- No OSH (BHP) risk assessment performed for remote workstation → employer violates Art. 67²⁷ KP; PIP inspection risk
- Attempting to mandate remote work by employer order without emergency conditions → NIEWAŻNY; remote work is by agreement

#### Clause 11: Intellectual Property

**Copyright works (UPAPP Art. 12):**

- Default rule: employer acquires economic rights in works created in performance of employment duties, upon acceptance of the work
- Employer acquires rights only within the scope of the employment purpose
- **2-year use-or-lose rule**: If employer does not exploit the work within 2 years of acceptance, the employee may set a deadline; upon expiry the author may exercise or assign the rights (unless collective agreement or contract provides otherwise)
- **Moral rights** (right of authorship, right of integrity) are inalienable — employer cannot contractually acquire them
- Works created outside employment duties, on personal time, with personal resources, unrelated to employment purpose → employee's own rights

**Software (UPAPP Art. 74(3)):**

- Employer acquires primary economic rights in software created in the course of employment **at the moment of creation** — no intermediate employee holding
- This differs from Art. 12: there is no acceptance requirement and no 2-year deadline
- This rule is the default for all code, algorithms, and related software materials

**50% tax-deductible creative cost (koszty uzyskania przychodu 50% — Art. 22 ust. 9 pkt 3 ustawy o PIT):**

- Available where the employee creates copyrightable works and transfers economic rights to the employer
- Requires explicit clause: (a) identifying the creative portion of work, (b) stating that the employee creates works and transfers economic rights, (c) stating the fee attributable to the creative work separately from other remuneration
- Cap: 50% tax deduction is capped at PLN 120,000/year (subject to annual adjustment — [VERIFY current cap])
- For software roles using this structure, Art. 74(3) UPAPP must be disapplied by contract (so rights vest first in employee, then are transferred) — requires careful drafting reviewed by a Polish tax/employment lawyer

**Service inventions (PrWłPrzem Art. 11):**

- Inventions, utility models, and industrial designs created as a result of employment duties belong to the employer
- If created using employer experience/resources but not strictly within employment duties → employer has right of pre-emption
- Employee-inventor is entitled to **remuneration from the employer's exploitation** of the invention, unless the contract provides otherwise
- Amount: if not agreed, courts determine by reference to the economic significance of the invention and the employee's contribution

**RED flags:**

- Contract purports to assign employee's moral rights → NIEWAŻNY under UPAPP Art. 16
- No mention of 50% PIT deduction for a software developer role → missed tax optimisation opportunity
- Broad "all IP assigned" clause without distinguishing employment-scope vs. outside-employment works → may overreach; creates enforcement risk

#### Clause 12: Personal Data and Monitoring

**Recruitment data (Art. 22¹ KP):**

- The employment agreement may not condition continued employment on provision of data outside the closed statutory list (name, date of birth, contact details, education, qualifications, prior employment history)
- Employer may not collect: marital status, information about dependants, criminal record (unless specific legal authority), financial status

**Workplace monitoring (Art. 22² KP):**

- Purpose must be legitimate (safety, property protection, production secrets, other legitimate business information)
- Cannot cover areas of personal intimacy (rest rooms, changing rooms, canteen — except specific safety necessity)
- Employees must be informed at least **2 weeks before** monitoring begins
- Monitoring rules must appear in work regulations (regulamin pracy) or be disclosed in the employment contract
- Monitoring data must be deleted within **3 months** unless used in proceedings

**Biometric data (Art. 22¹b KP):**

- Permissible only with freely given consent OR to control access to areas requiring special protection
- Using fingerprints for timekeeping purposes → UNLAWFUL per UODO's published guidance

**GDPR / UODO:**

- GDPR applies in full; supervisory authority is UODO
- Consent is generally NOT a valid lawful basis for mandatory employment data processing given power imbalance — use Art. 6(1)(c) (legal obligation) or Art. 6(1)(b) (contractual necessity)
- Employees must receive an Art. 13 GDPR information notice at or before commencement

**RED flags:**

- Contract includes blanket consent to data processing for employment-related purposes → UODO would likely invalidate; replace with information notice
- No mention of monitoring in contract or work regulations but monitoring occurs → Art. 22² KP violation; employee privacy claim and UODO complaint risk

---

## Mode C: Civil Law Contract Classification Risk Assessment

### C1. The Art. 22 KP Test

Apply all five indicators to the arrangement under review:

| Indicator                       | Employment Characteristic                               | Civil Law Characteristic                                 |
| ------------------------------- | ------------------------------------------------------- | -------------------------------------------------------- |
| **Personal performance**        | Work must be performed by the specific named individual | Performance may be delegated to a sub-contractor         |
| **Direction and subordination** | Employer directs how, when, and where work is performed | Party sets their own methods and schedule                |
| **Time and place**              | Specific hours and location designated by the employer  | Independent scheduling and location freedom              |
| **Employer's tools**            | Employer provides equipment, materials, workspace       | Worker uses own tools and resources                      |
| **Economic risk**               | Worker bears no financial risk for results              | Worker bears risk of cost overruns and defective results |

**If 4 or 5 indicators favour employment**: HIGH reclassification risk. Art. 22 § 1¹ KP makes this an unlawful replacement of employment. Recommend converting to employment contract without delay.

**If 3 indicators favour employment**: MEDIUM risk. Legal challenge is possible; PIP or a court may reclassify. Review the arrangement; consider structural changes or conversion.

**If 0–2 indicators favour employment**: LOW risk. Civil-law contract is defensible, but document the factual basis for each indicator clearly.

### C2. The 2026 PIP Reclassification Powers

**CRITICAL 2026 development**: The Sejm (March 11, 2026) has resolved to grant PIP authority to issue **administrative decisions** establishing the existence of an employment relationship. Key enforcement features:

- Decisions are **immediately enforceable** (rygor natychmiastowej wykonalności)
- **Burden of proof shifts** to employer/principal once PIP issues a preliminary order
- Triggered after PIP identifies violations and the party fails to comply with a remediation order
- Employer must treat the worker as a full employee from the decision date, with all retrospective consequences

**Consequences of reclassification:**

- Back ZUS contributions (employer's + employee's share) plus statutory interest
- PIT arrears (income tax)
- All KP protections applied retroactively (notice pay, severance, leave entitlements, sick pay)
- Administrative fines up to PLN 30,000 per violation (Art. 281 KP) for obstructing PIP
- Criminal liability for intentional misclassification (Art. 281 KP — fines up to PLN 30,000)

### C3. B2B Arrangements

B2B arrangements (individual running a one-person business contracted to provide services) face the same Art. 22 KP reclassification test. The B2B form provides no protection if the factual working conditions satisfy the employment relationship test.

Additional B2B risk factors:

- Exclusivity clause (sole client) + personal performance → strong employment indicator
- Fixed daily/weekly hours set by the principal → employment indicator
- Business premises provided by principal → employment indicator
- Client controls daily methods, not just results → employment indicator

### C4. ZUS Classification for Zlecenia vs. Dzieło

**Umowa zlecenia:** Subject to ZUS contributions (pension + disability + sickness — if single employer; all if sole source of income). Minimum wage applies per hour (PLN 31.40/hour from January 2026). ZUS may reclassify umowa o dzieło as umowa zlecenia and impose back contributions.

**Umowa o dzieło:** No ZUS contributions from contractor's perspective (only accident insurance if performed on principal's premises). Most vulnerable to reclassification because ZUS has direct power to reclassify as umowa zlecenia (distinct from PIP power to reclassify as employment).

**Risk table for ZUS audit:**

| Factor                                              | Increases dzieło → zlecenia reclassification risk |
| --------------------------------------------------- | ------------------------------------------------- |
| Ongoing services (not a defined, assessable result) | High                                              |
| No identifiable "result" (dzieło) at contract end   | High                                              |
| Monthly payments regardless of specific deliverable | Medium                                            |
| No defect liability for the result                  | Medium                                            |
| Same content as prior zlecenia contracts            | High                                              |

---

## Deviation Severity Classification

| Classification | Polish / Symbol | Meaning                                                                                                        | Response                                                              |
| -------------- | --------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **ZGODNY**     | ✅              | Clause is compliant with mandatory law and standard practice                                                   | Note and proceed                                                      |
| **RYZYKO**     | ⚠️              | Clause creates legal or commercial risk; not necessarily void                                                  | Flag, redline, and recommend correction                               |
| **NIEWAŻNY**   | ❌              | Clause is void by operation of mandatory law (Art. 18 KP or specific statute); statutory provision replaces it | Mandatory correction; void clause cannot be relied on by either party |

---

## Actionable Output per Finding

For each **RYZYKO** finding, provide:

1. The specific article violated or at risk
2. Recommended contract language (Polish and English)
3. Business impact of accepting vs. correcting
4. Negotiation or correction priority

For each **NIEWAŻNY** finding, provide:

1. The specific article that overrides the contractual provision
2. The statutory provision that replaces it by operation of law
3. Steps to correct (redraft, not merely note)
4. Employer liability exposure if uncorrected

---

## Prioritization Framework

| Tier                                  | Contents                                                                                                                                                                      | Action Required                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Tier 1 — Correct Immediately**      | NIEWAŻNY clauses; below-minimum-wage remuneration; missing mandatory Art. 29 KP elements; post-employment non-compete without compensation                                    | Must correct before contract is signed or issued              |
| **Tier 2 — Correct Before Signature** | Ambiguous non-compete scope; missing supplementary information; no IP clause for IP-generating role; GDPR notice absent; monitoring in practice without Art. 22² KP procedure | Should correct before execution; material legal risk if not   |
| **Tier 3 — Optimise**                 | Below-optimal notice period formulation; garden leave clause absent; 50% PIT deduction structure absent for qualifying roles; occasional remote work procedure not documented | Good practice; low immediate legal risk but improves position |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise if any fails.

| Gate           | Rule                                                                                                                                        | Fail Action                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every legal claim cites a specific article of KP, UPAPP, PrWłPrzem, or other statute                                                        | Add citation or mark [UNVERIFIED] |
| **Format**     | Citations in format "Art. [X] KP" or "Art. [X] [statute abbreviation]"                                                                      | Fix format                        |
| **Currency**   | All cited provisions checked against current consolidated text (isap.sejm.gov.pl); 2023 and 2024 amendments incorporated                    | Flag [CHECK CURRENCY]             |
| **Domain**     | Analysis stays within Polish law; do not apply German, French, or EU-general employment law concepts without [JURISDICTION-SPECIFIC] marker | Remove or flag                    |
| **Confidence** | Uncertainty explicitly stated; never hide doubt behind confident language                                                                   | Add confidence qualifier          |

### Self-Interrogation for NIEWAŻNY Findings

For any clause classified NIEWAŻNY, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the nullity assessment follow directly from the cited statute? Is Art. 18 KP (or specific nullity provision) correctly applied? Would a Polish labour court reach this conclusion?

**Pass 2 — Completeness**: Are all relevant KP provisions considered? Is there a saving interpretation (partial nullity vs. full nullity)? Would a sectoral collective agreement modify the analysis?

**Pass 3 — Challenge**: What is the strongest argument for enforceability? Under what circumstances might the clause be valid despite the statutory concern? (Example: a shorter notice period in a contract with a senior executive may be challenged but upheld if the executive's overall package clearly compensates.)

### Confidence Scoring

| Level             | Range     | Meaning                                                        | Action                                              |
| ----------------- | --------- | -------------------------------------------------------------- | --------------------------------------------------- |
| **Definitywny**   | 0.95–1.0  | Express statutory provision; settled case law                  | State without caveat                                |
| **Wysoki**        | 0.80–0.94 | Strong statutory support; minor interpretive questions         | State with brief caveat                             |
| **Prawdopodobny** | 0.60–0.79 | Good arguments for and against; depends on court/UODO approach | State with reasoning and contra-indicators          |
| **Możliwy**       | 0.40–0.59 | Genuinely uncertain; doctrinal debate                          | Flag for Polish employment lawyer review            |
| **Wątpliwy**      | 0.0–0.39  | Weak or speculative basis                                      | Do not assert; flag [NIEPEWNY — wymaga weryfikacji] |

---

## Glass Box Audit Trail

Append the following YAML block at the end of every output:

```yaml
glass_box:
  skill: legalcode-pl-employment-agreement
  mode: "[A — Draft / B — Review / C — Classify]"
  date: "[ISO date]"
  jurisdiction: "Poland — Kodeks pracy (Dz.U. 2023 poz. 1465 as amended)"
  contract_type: "[próbny / czas określony / czas nieokreślony / civil-law / B2B]"
  perspective: "[Employer / Employee / Neutral]"
  sector: "[identified sector]"
  legalcode_mcp: "[Connected — citations verified / Not connected — citations require manual verification]"
  minimum_wage_used: "PLN [amount]/month (from [date])"
  key_statutes_applied:
    - "[Art. X KP — subject]"
    - "[UPAPP Art. Y — subject (if applicable)]"
  tier1_findings: "[count] NIEWAŻNY items"
  tier2_findings: "[count] RYZYKO items"
  tier3_findings: "[count] optimisation items"
  confidence_overall: "[Definitywny / Wysoki / Prawdopodobny / Możliwy / Wątpliwy] — [rationale]"
  citations_verified: "[count] articles checked"
  limitations:
    - "[Collective agreement not reviewed — obtain and cross-check against any industry CCN]"
    - "[Remuneration structure tax treatment not verified — consult Polish tax adviser for 50% cost deduction structure]"
    - "[PIP reclassification powers pending full legislative enactment — verify current status]"
  reviewer: "AI-assisted — requires review by Polish radca prawny or adwokat before use"
```

---

## Anti-Patterns

The following errors occur frequently in Polish employment agreements. Do not reproduce
them in drafts or accept them without flagging in reviews.

1. **Using "umowa zlecenia" for employee-directed work**: Labelling a contract as a civil-law mandate when the actual working conditions satisfy Art. 22 KP. The contract name is irrelevant; the factual relationship controls. This is the single most common source of ZUS arrears and PIP enforcement.

2. **Omitting mandatory Art. 29 KP elements**: Failing to specify all 8 required elements (particularly the complete remuneration breakdown or the working time dimension). Incomplete contracts are a misdemeanour under Art. 281 KP.

3. **Exceeding the fixed-term 33-month / 3-contract limits without realising conversion has occurred**: Issuing a 4th consecutive fixed-term contract that is legally an indefinite contract. The employer cannot terminate it on fixed-term expiry grounds.

4. **Post-employment non-compete without the 25% compensation floor**: A non-compete clause that omits compensation, or sets it below 25% of pre-termination monthly remuneration, is void under Art. 101² KP as to the deficient amount. The employee is released from the restriction.

5. **Blanket IP assignment including moral rights**: Polish copyright law makes moral rights inalienable (UPAPP Art. 16). Any contractual assignment of moral rights is void. Draft to acquire economic rights only; address moral rights through an authorisation (upoważnienie) clause limited to what the employer's business requires.

6. **Implementing monitoring without the Art. 22² KP procedure**: Installing CCTV or email monitoring without a stated legitimate purpose, without including monitoring rules in work regulations, or without the 2-week prior employee notice. Creates UODO complaint exposure and potential invalidation of monitoring evidence in labour proceedings.

7. **Ignoring the 2-year employer use-or-lose rule (UPAPP Art. 12)**: For non-software creative works, if the employer does not use the work within 2 years of acceptance, the author may set a further deadline. Many contracts do not address this. Include a clause extending or varying the 2-year period if commercially required.

8. **Applying 3-month trial period without linking to intended follow-on contract type**: The 2023 amendment requires shorter trial periods if the intended follow-on contract is short (< 12 months). A 3-month trial for an intended 6-month fixed-term contract violates Art. 25 § 2 KP.

9. **Stating leave entitlement without cross-checking total seniority**: Polish annual leave is based on total professional experience across all employers (and certain study periods), not just service with the current employer. Granting 20 days to an employee who qualifies for 26 days creates an underpayment liability.

10. **Remote work without employer cost-coverage provisions**: Failing to include a cost reimbursement mechanism (cash equivalent, lump sum, or equipment provision) in a remote work arrangement. The employer's obligation under Art. 67²⁴ KP is mandatory; omitting it does not eliminate it.

11. **Treating PIT 50% creative cost deduction as automatic**: The 50% tax deduction for creative work requires explicit contractual structure. Without the required clause distinguishing creative remuneration and providing for rights transfer, the employee cannot claim the deduction and both parties face a tax dispute.

12. **Missing the 7-day supplementary information obligation**: Many employers issue the Art. 29 KP contract but fail to deliver the supplementary information required within 7 days of commencement (working time norms, overtime rates, notice periods, leave entitlement). This is a separate PIP inspection trigger.

13. **Non-compete with no employer termination right**: Post-employment non-competes bind the employer to pay compensation for their full duration even if circumstances change. Include a contractual right for the employer to terminate the non-compete obligation (with reasonable notice) to stop the compensation meter.

14. **Ignoring the whistleblower protection Act for employers with 50+ employees**: Employment agreements for employers with 50+ employees should cross-reference the internal whistleblower reporting channel. Dismissing a reporting employee is a strict-liability tort under the 2024 Act (minimum 1 average national salary compensation).

15. **Asymmetric termination notice periods**: Some contracts set longer notice obligations for the employee than for the employer. Polish courts have held that Art. 36 KP sets symmetrical minimum floors. Asymmetric periods shorter than statutory minimums are replaced by statute.

16. **Failing to specify the overtime threshold for part-time employees**: Art. 151 § 5 KP requires fixed-term and indefinite contracts for part-time employees to specify the hours above which the employee is entitled to overtime supplements. Omitting this clause means the employer owes supplements from the first hour above the contractual hours.

17. **Biometric timekeeping without valid legal basis**: Using fingerprint scanners or facial recognition for attendance tracking. UODO has stated this violates Art. 22¹b KP and GDPR Art. 9 (special category data) because less intrusive alternatives exist (PIN, proximity cards). Exposure to UODO investigation and employee claims.

18. **Drafting broad post-employment non-competes for all staff regardless of information access**: Art. 101² KP limits the non-compete to employees who have access to "particularly important information." Courts will void non-competes applied to employees with no meaningful access to competitively sensitive information.

---

## Writing Standards

Before delivering any output, apply these quality gates:

1. **Polish legal terminology accuracy**: Use the correct Polish legal terms with English translations in brackets on first use. Do not substitute approximate English equivalents (e.g., "mandate contract" for umowa zlecenia is acceptable; "freelance contract" is not a legal term).

2. **Article references**: Always cite the specific KP article (e.g., "Art. 36 § 1 KP") rather than paraphrasing. Polish employment law is article-number driven in practice.

3. **Bilingual clause drafting** (for Mode A output): Provide key clauses in Polish (required for enforceability) with English translation. Note: Polish is the mandatory language for employment contracts performed in Poland under the Act on the Polish Language (Ustawa o języku polskim) — contracts with foreign employees may be bilingual but the Polish version prevails for domestic legal purposes [VERIFY per Art. 8 Ustawa o języku polskim].

4. **Minimum wage currency**: Always confirm and state the current applicable minimum wage at the time of drafting. Minimum wage changes annually (and previously twice per year). The 2026 rate is PLN 4,806/month / PLN 31.40/hour as of January 1, 2026. Mark as [CHECK CURRENCY] for forward-dated contracts.

5. **Active voice and imperative form**: Draft contractual obligations in active voice ("The Employer shall provide…") not passive ("Equipment is to be provided…").

6. **No jurisdictional bleed**: Do not import German, French, or general EU employment law concepts. Polish law does not have a "Verhältnismäßigkeit" test for non-competes by that name — use the Polish courts' proportionality standard as interpreted under Art. 101² KP.

7. **Avoid hallucinated court citations**: Polish Sąd Najwyższy (Supreme Court) and Trybunał Konstytucyjny (Constitutional Tribunal) case law should be cited with full reference (court, date, docket number). If not retrievable via legalcode-mcp, mark as [VERIFY citation]. Do not invent case references.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

1. Search for the current consolidated text of the Kodeks pracy on isap.sejm.gov.pl
2. Verify current minimum wage (Rozporządzenie Rady Ministrów on minimum wage for the current year)
3. Search for Sąd Najwyższy case law on the specific non-compete, fixed-term, or IP question at issue
4. Verify current ZUS contribution rates and the annual pension/disability contribution ceiling
5. Search for UODO enforcement decisions relevant to monitoring or biometrics in employment
6. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

### Without legalcode-mcp

Proceed with the research embedded in this skill and mark all statutory citations [VERIFY].
Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`.
Focus enhancement on structural quality, workflow design, and prompt engineering rather
than legal substance depth for any novel points.

### Cross-reference Skills

- **legalcode-pl-contract-review**: For reviewing non-employment commercial contracts governed by Polish civil law (Kodeks cywilny) — covers Art. 353¹ KC, kara umowna, limitation of liability, etc.
- **legalcode-nda-triage-pl**: For Polish non-disclosure agreements in commercial contexts
- **legalcode-gdpr-data-processing-addendum**: For GDPR-compliant data processing addenda to employment agreements involving third-party data processors

---

## Output Format Template

Deliver output in this structure:

---

### Polish Employment Agreement Analysis

**Date**: [date]
**Mode**: [A — Draft / B — Review / C — Classify]
**Contract**: [name or description]
**Perspective**: [Employer / Employee / Neutral]
**Governing Law**: Republic of Poland — Kodeks pracy

---

### Executive Summary

**Overall Classification**: [ZGODNY / MIXED — see findings / SIGNIFICANT ISSUES]
**Tier 1 (Correct Immediately)**: [N] item(s)
**Tier 2 (Correct Before Signature)**: [N] item(s)
**Tier 3 (Optimise)**: [N] item(s)

**Top 3 Issues:**

1. [Issue] — [Classification] — [One-line impact]
2. [Issue] — [Classification] — [One-line impact]
3. [Issue] — [Classification] — [One-line impact]

---

### Mandatory Content Checklist — Art. 29 KP

| Element                              | Present | Status            | Note |
| ------------------------------------ | ------- | ----------------- | ---- |
| Parties                              | ✅/❌   | [ZGODNY/NIEWAŻNY] |      |
| Contract type                        | ✅/❌   |                   |      |
| Date of conclusion                   | ✅/❌   |                   |      |
| Type of work (rodzaj pracy)          | ✅/❌   |                   |      |
| Workplace location                   | ✅/❌   |                   |      |
| Remuneration (itemised)              | ✅/❌   |                   |      |
| Working time dimension               | ✅/❌   |                   |      |
| Work commencement date               | ✅/❌   |                   |      |
| 7-day supplementary information duty | ✅/❌   |                   |      |

---

### Clause-by-Clause Findings

#### [Clause Name]

**Status**: [✅ ZGODNY / ⚠️ RYZYKO / ❌ NIEWAŻNY]
**Tier**: [1 / 2 / 3]
**Issue**: [Description of the problem]
**Statutory basis**: [Art. X KP / UPAPP Art. Y / etc.]
**Recommended action**: [Specific redline or corrective language]
**Confidence**: [Definitywny / Wysoki / Prawdopodobny]

---

### [Mode C only] Civil Law Contract Risk Assessment

**Art. 22 KP indicator score**: [X/5 employment indicators satisfied]
**Overall reclassification risk**: [HIGH / MEDIUM / LOW]
**2026 PIP enforcement exposure**: [Description]

| Indicator                   | Finding          | Risk       |
| --------------------------- | ---------------- | ---------- |
| Personal performance        | [Yes/No/Partial] | [🔴/🟡/🟢] |
| Direction and subordination | [Yes/No/Partial] | [🔴/🟡/🟢] |
| Time and place              | [Yes/No/Partial] | [🔴/🟡/🟢] |
| Employer's tools            | [Yes/No/Partial] | [🔴/🟡/🟢] |
| Economic risk               | [Yes/No/Partial] | [🔴/🟡/🟢] |

**Recommended action**: [Convert to employment / Restructure civil-law arrangement / Document factual basis for current form]

---

### [Mode A only] Draft Contract Outline

**Clause structure proposed:**

1. Parties (Strony umowy)
2. Type and duration of contract (Rodzaj i czas trwania umowy)
3. Workplace (Miejsce wykonywania pracy)
4. Type of work and duties (Rodzaj pracy i zakres obowiązków)
5. Working time (Wymiar czasu pracy)
6. Remuneration (Wynagrodzenie)
7. Annual leave (Urlop wypoczynkowy)
8. Notice period (Okres wypowiedzenia)
9. Non-compete — during employment (Zakaz konkurencji w czasie zatrudnienia) [if applicable]
10. Non-compete — post-employment (Zakaz konkurencji po ustaniu zatrudnienia) [if applicable]
11. Remote work arrangement (Praca zdalna) [if applicable]
12. Intellectual property (Prawa własności intelektualnej) [if applicable]
13. Personal data information clause (Informacja o przetwarzaniu danych osobowych)
14. Whistleblower channel reference (Kanał zgłaszania naruszeń) [if employer ≥ 50 employees]
15. Applicable collective agreement or work regulations (Układ zbiorowy / Regulamin pracy)
16. Final provisions (Postanowienia końcowe)
17. Supplementary information annex (Informacja uzupełniająca — Art. 29 § 3 KP)

---

### ZUS Cost Summary [Mode A / B if applicable]

| Component                                | Employer rate              | Employee rate |
| ---------------------------------------- | -------------------------- | ------------- |
| Pension (emerytalne)                     | 9.76%                      | 9.76%         |
| Disability (rentowe)                     | 6.50%                      | 1.50%         |
| Sickness (chorobowe)                     | 0%                         | 2.45%         |
| Accident (wypadkowe)                     | [sector rate: ~1.67–3.33%] | 0%            |
| Labour Fund (FP)                         | 2.45%                      | 0%            |
| FGŚP                                     | 0.10%                      | 0%            |
| Health (zdrowotne)                       | 0%                         | 9.00%         |
| **Approx. employer on-cost above gross** | **~19–22%**                |               |

Annual pension/disability ceiling (2026): PLN 282,600 — [CHECK CURRENCY]

---

### Glass Box Audit Trail

```yaml
[Insert completed Glass Box YAML here]
```

---

## Localization Notes

This skill covers **national Polish law only**. The following local variations should
be investigated case-by-case:

- **Collective agreements (układy zbiorowe pracy)**: Industry or company-level collective agreements may grant better conditions than the statutory floor (more annual leave, higher severance, shorter working time). Identify the applicable NAF/PKD code to determine whether a sectoral collective agreement (porozumienie branżowe) applies. These are registered with the National Labour Inspectorate (PIP) and available on pip.gov.pl. [VERIFY applicability]

- **Free zones and special economic zones (Specjalne Strefy Ekonomiczne)**: Special employment incentives may apply for employers within these zones, including some ZUS exemption structures. [VERIFY for specific zone]

- **Posted workers (pracownicy delegowani)**: If the employee will temporarily work in another EU/EEA member state under a posting, the Directive on Posting of Workers (Dyrektywa 96/71/WE as amended) and Ustawa o delegowaniu pracowników w ramach świadczenia usług require specific documentary compliance. This skill does not cover posting compliance.

- **Civil servants and public sector workers**: Employed under Ustawa o służbie cywilnej or specific sectoral laws (e.g., teachers under Karta Nauczyciela, academics under Prawo o szkolnictwie wyższym). Different mandatory content, notice periods, and termination rules apply.

---

## Provenance

Created by Legalcode (2026-03-21). Mode A (creation from scratch). Research conducted via
web search across Polish government portals (isap.sejm.gov.pl, pip.gov.pl, gov.pl, zus.pl),
leading Polish employment law firm publications (CMS, Baker McKenzie, Getsix, Accace,
Milewska Legal, ATL Law, HLB Poland, CGO Legal, Dudkowiak & Putyra), and WIPO Lex.
Covers Kodeks pracy consolidated text as at Dz.U. 2023 poz. 1465 with all 2023 and 2024
amendments (trial period reform, remote work regime, parental leave EU directive,
whistleblower protection). Minimum wage based on PLN 4,806/month from January 2026.
PIP reclassification powers based on Sejm resolution of March 11, 2026.
All citations should be verified against current isap.sejm.gov.pl before reliance.
