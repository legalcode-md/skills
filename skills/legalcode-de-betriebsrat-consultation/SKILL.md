---
name: legalcode-de-betriebsrat-consultation
description: 'Guide employers through works council (Betriebsrat) consultation obligations under German
  Betriebsverfassungsgesetz (BetrVG). Use when planning hiring, reclassification, transfers, or dismissals
  in Germany (§§ 99–102), rolling out technical monitoring or AI systems, mobile work policies, or working-time
  changes that trigger § 87 mandatory codetermination, or when conducting operational changes (Betriebsänderung)
  requiring Interessenausgleich and Sozialplan under §§ 111–113. Also covers § 80 information rights,
  Einigungsstelle deadlock procedure, European Works Council (EBRG) requirements, and Betriebsvereinbarung
  drafting and validity. Triggers on: Betriebsrat consultation, BetrVG compliance, works council hearing,
  § 99 consent, § 102 Anhörung, § 87 Mitbestimmung, Interessenausgleich, Sozialplan, Nachteilsausgleich,
  Einigungsstelle, Betriebsvereinbarung, EWC, EBRG, SE-BetrVG, German labor law.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — German Works Council (Betriebsrat) Consultation

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of works council
> consultation obligations under German law. It does not constitute legal advice (Rechtsberatung).
> All outputs must be reviewed by a Rechtsanwalt or Fachanwalt für Arbeitsrecht licensed in
> Germany before reliance. Laws and collective agreements change; verify current applicability
> before acting on any provision described here. Statutory references and case law cited from
> memory carry hallucination risk — verify against gesetze-im-internet.de and the
> Bundesarbeitsgericht database before relying on them.

---

## Purpose and Scope

This skill guides employers, HR teams, and legal advisors through the full works council
(Betriebsrat) consultation lifecycle under the Betriebsverfassungsgesetz (BetrVG).

**Covers:**

- § 99 consent procedure for hiring, grading, reclassification, and transfers
- § 100 urgent provisional measures
- § 102 Anhörung (dismissal hearing) — ordinary and extraordinary dismissals
- § 87 mandatory codetermination across all 14 categories, including AI/monitoring (Nr. 6) and mobile work (Nr. 14)
- § 80 general information rights and timing obligations
- § 106 economic committee (Wirtschaftsausschuss) information
- §§ 111–113 Betriebsänderung: Interessenausgleich, Sozialplan, and Nachteilsausgleich
- § 76 Einigungsstelle (conciliation board) — formation, procedure, and binding decisions
- § 77 Betriebsvereinbarung drafting, form requirements, and after-effect (Nachwirkung)
- European Works Council (EBRG / Directive 2009/38/EC) and SE-BetrVG

**Does not:**

- Advise individual employees on works council election procedures
- Draft collective bargaining agreements (Tarifverträge) — separate from BetrVG framework
- Replace jurisdiction-specific legal counsel for contested Beschlussverfahren proceedings
- Apply to public sector employees under Personalvertretungsgesetz (PVG/BPersVG) — separate statute

---

## Jurisdiction and Governing Law

**Germany only.** This skill applies exclusively to private-sector establishments subject to the
Betriebsverfassungsgesetz (BetrVG) as amended (current version at gesetze-im-internet.de).

**Key statutory framework:**

| Statute                                     | Relevance                                              |
| ------------------------------------------- | ------------------------------------------------------ |
| BetrVG (Betriebsverfassungsgesetz)          | Primary works constitution law                         |
| KSchG (Kündigungsschutzgesetz)              | Dismissal protection — interacts with § 102            |
| ArbGG (Arbeitsgerichtsgesetz)               | Labor court procedure for Beschlussverfahren           |
| EBRG (Gesetz über Europäische Betriebsräte) | European Works Council — 1,000+ employees EU-wide      |
| SE-BetrVG                                   | Societas Europaea — enhanced board-level participation |
| BDSG / DSGVO (GDPR)                         | Data protection dimension of § 87 Nr. 6 monitoring     |
| EU AI Act (in force 01.08.2024)             | High-risk AI classification for HR applications        |

**Threshold reminder**: Most §§ 99 and 111 obligations apply only in establishments with
**more than 20 eligible employees** (wahlberechtigte Arbeitnehmer). Always verify actual
headcount at the relevant establishment (Betrieb), not the entire enterprise (Unternehmen).

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **⟁ CLARIFY**) at key decision points.
Rather than assuming employer context, the workflow pauses when:

- The measure type determines which BetrVG section applies
- Establishment headcount affects whether obligations are triggered at all
- The presence or absence of a works council, collective agreement, or existing
  Betriebsvereinbarung changes the analysis materially
- Ambiguity in the measure's classification creates a procedural fork

When the user has already provided the relevant context, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Planned measure description**: Summary of the HR or operational action the employer intends to take
- **Document**: Draft dismissal notice, works agreement text, restructuring plan, job posting, or similar
- **Free-form query**: A question about works council obligations for a specific scenario

If no context is provided, ask the user to describe the measure before proceeding.

---

### Step 2: Establish Jurisdiction and Establishment Profile

**⟁ CLARIFY** — Ask the following before any analysis. Present as structured options:

1. **Establishment headcount** (for § 99 and § 111 threshold checks):
   - Options: ≤ 20 eligible employees | 21–100 | 101–300 | > 300 | Unknown — help me assess
   - _Why this matters_: § 99 applies only at > 20; §§ 111–112 economic committee at > 100;
     advisor rights at > 300.

2. **Works council status**:
   - Options: Works council exists and is active | No works council | Election in progress |
     Multiple Betriebsräte (Gesamtbetriebsrat or Konzernbetriebsrat also relevant) | Unknown
   - _Why this matters_: Many consultation obligations only arise when a Betriebsrat exists.
     Absence of a Betriebsrat does not eliminate all protections (§ 113 can still apply).

3. **Governing collective agreement (Tarifvertrag)**:
   - Options: Sector-wide agreement applies (Flächentarifvertrag) | Company agreement (Haustarifvertrag) |
     No collective agreement | Unknown
   - _Why this matters_: § 87 Abs. 1 S. 1 — codetermination right does NOT arise where
     a statutory or collective agreement already regulates the matter.

4. **Measure type** — what are you planning to do?
   - Options (multiple selections allowed):
     - A: Hire, grade/reclassify, or transfer an employee (→ § 99)
     - B: Dismiss an employee (→ § 102)
     - C: Roll out technical system, monitoring tool, or AI application (→ § 87 Nr. 6)
     - D: Change working hours, mobile work, or pay method (→ § 87 Nr. 2/14)
     - E: Restructure, close a department, or relocate the business (→ §§ 111–113)
     - F: Draft or amend a Betriebsvereinbarung (→ § 77)
     - G: Assess European Works Council obligations (→ EBRG)
     - H: Other/unclear — describe below

If the user provides partial context, proceed with stated assumptions and flag them explicitly.

---

### Step 3: Load Playbook or Works Agreement Library

Check for existing documentation:

- **Betriebsvereinbarungen** already in effect that may pre-empt or modify consultation requirements
- **Tarifvertrag** opening clauses that authorise or restrict Betriebsvereinbarung regulation
- **Internal HR policy manuals** that may impose stricter internal consultation requirements
- **Prior § 99 consent or § 102 hearing records** relevant to the current measure

**If no documentation is available**, proceed with default BetrVG rules and note this explicitly
in the output. Recommend that the user confirm whether any works agreements exist for the topic
area before finalising the assessment.

---

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve:

- Current text of the relevant BetrVG sections
- Recent BAG decisions on the specific procedure (search by section number + decision year)
- Any pending legislative amendments

**If legalcode-mcp is not connected**: Proceed using the statutory and case-law references in
this skill. Flag all citations with [VERIFY] and note in the Glass Box audit trail:
`legalcode_mcp: "Not connected"`.

Authoritative public sources (no authentication required):

- BetrVG full text: https://www.gesetze-im-internet.de/betrvg/
- BAG decisions: https://www.bundesarbeitsgericht.de/
- dejure.org for section-level jurisprudence index

---

### Step 5: Run Section-by-Section Analysis

Apply the analysis modules below based on the measure types identified in Step 2.
Run all relevant modules; skip inapplicable ones with a brief note.

---

## Analysis Modules

### Module A — § 99 BetrVG: Hiring, Grading, and Transfers

**Trigger**: Employer plans an Einstellung (hiring), Eingruppierung (initial grading),
Umgruppierung (reclassification), or Versetzung (transfer).
**Threshold**: Establishment with **> 20 eligible employees** AND a works council exists.

#### A.1 Scope Check — Is This Measure Within § 99?

| Measure                                            | § 99 Applies?   | Notes                                |
| -------------------------------------------------- | --------------- | ------------------------------------ |
| New hire into any role                             | ✅ Yes          | Regardless of contract type          |
| Agency worker placed for > 1 month                 | ✅ Yes [VERIFY] | BAG treats as Einstellung            |
| Grading of new hire                                | ✅ Yes          | Combined with Einstellung            |
| Reclassification/upgrade                           | ✅ Yes          | Umgruppierung                        |
| Transfer to different work area > 1 month          | ✅ Yes          | § 95 Abs. 3 definition               |
| Transfer with substantial working condition change | ✅ Yes          | Even if < 1 month                    |
| Cross-border transfer within EU                    | ✅ Yes [VERIFY] | Establishment-level analysis applies |
| Freelancer/contractor engagement                   | ❌ No           | Not an Arbeitnehmer (verify)         |
| Internal rotation < 1 month / no condition change  | ❌ No           | Below § 95 Abs. 3 threshold          |
| Pay increase for freed works council member        | ❌ No           | BAG 26.11.2024, Az. 1 ABR 12/23      |

#### A.2 Disclosure Obligations (§ 99 Abs. 1)

The employer must provide the works council with:

- **Application documents and personal data** of the candidate (Bewerbungsunterlagen)
- **Intended work area** and planned **grading/classification**
- **Information about affected employees** and impacts on their terms
- **Any relevant internal job-posting history** (if internal posting policy applies)
- _Digital disclosure is sufficient_: BAG 13.12.2023 (Az. 1 ABR 28/22) — employer need not
  provide paper copies; digital access to documents meets the requirement.

**Completeness check**: Works council must receive enough information to form an independent
assessment. Vague job descriptions or incomplete grading data enable later consent refusal on
grounds of insufficient disclosure.

#### A.3 Works Council Response Window

| Stage                                          | Deadline        | Consequence of Silence                    |
| ---------------------------------------------- | --------------- | ----------------------------------------- |
| Works council receipt of complete notification | Day 0           | Clock starts                              |
| Written refusal with grounds                   | 1 week (7 days) | Consent deemed given (fiktive Zustimmung) |
| Extraordinary circumstances                    | 3 days [VERIFY] | Accelerated procedure                     |

**Critical rule**: The 1-week deadline is absolute. If the works council fails to respond
in writing with specific statutory grounds, consent is deemed given. The employer may then
implement the measure.

#### A.4 Grounds for Withholding Consent (§ 99 Abs. 2 — All 8 Grounds)

Works council may refuse consent only if the measure:

| #   | Statutory Ground                                                                                                           | Examples                                                            |
| --- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 1   | Violates law, regulation, safety standard, collective agreement, works agreement, court order, or administrative order     | Hiring below minimum wage; violating applicable Tarifvertrag        |
| 2   | Creates justified concern of unjustified disadvantage to existing employees                                                | Transfer triggers redundancies without justification                |
| 3   | Violates internal job-posting obligations                                                                                  | Works agreement requires internal postings; none issued             |
| 4   | Creates justified concern the applicant/employee will engage in unlawful conduct or discrimination harming workplace peace | Criminal record relevant to role; documented discrimination history |
| 5   | Concerns about the employee's qualifications or suitability                                                                | [VERIFY] — narrow grounds; objective deficits only                  |
| 6   | Applicant/employee will have substantially worse terms than comparable employees                                           | Pay below market for same role without justification                |
| 7   | Employee rights under collective agreement violated                                                                        | Grading below applicable Tarifgruppe                                |
| 8   | Administrative reasons affecting company interest                                                                          | [VERIFY] — rarely successful standalone ground                      |

**Refusal must be in writing, within 1 week, citing specific statutory grounds.**
Vague or ungrounded refusal = deemed consent.

#### A.5 Consent Replacement Procedure (§ 99 Abs. 4)

If works council refuses:

1. Employer may petition the labor court (Arbeitsgericht) for **Zustimmungsersetzung**
2. No fixed statutory filing deadline — but prompt filing advisable to maintain operational momentum
3. Procedure: **Beschlussverfahren** (§ 2a ArbGG) — summary/non-contentious proceedings
4. Court asks: are the cited § 99 Abs. 2 grounds objectively justified?
5. BAG 25.02.2025 (Az. 1 ABR 18/24): Employer may file **multiple replacement procedures
   sequentially or in parallel** for the same employee/position — re-litigation permitted if
   initial decision adverse.
6. Court-replaced consent: Employer may implement measure immediately upon court order.

#### A.6 Urgent Provisional Measures (§ 100 BetrVG)

Where the measure cannot wait for works council consultation (urgent operational necessity):

1. Employer may implement provisionally
2. Must **immediately inform** works council of the measure and the urgency grounds
3. Works council may declare within **3 days** that it considers the urgency absent — dispute
   then goes to Einigungsstelle or court
4. If no urgency agreement: employer must obtain consent or court replacement for continued measure

#### A.7 Defect Consequences

| Defect                                        | Consequence                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| Measure implemented without § 99 consultation | Measure **void** (unwirksam) — invalid ab initio                               |
| Employee hired without consultation           | Employment relationship may be challenged; employee entitled to original terms |
| Transfer implemented before deadline expires  | Transfer has no legal effect; employee remains in original position            |
| Court replacement obtained                    | Defect cured; measure valid from replacement order date                        |

**Severity: RED** — Implementation without § 99 consultation is a pre-implementation blocker.

---

### Module B — § 102 BetrVG: Dismissal Hearing (Anhörung)

**Trigger**: Employer intends to dismiss any employee (ordinary or extraordinary dismissal).
**Threshold**: **ALL establishments regardless of size** — no employee-count threshold.
A works council must exist; if none exists, § 102 does not apply (but KSchG still does).

#### B.1 Scope — Every Dismissal Requires Anhörung

| Dismissal Type                                      | § 102 Applies? | Notes                                     |
| --------------------------------------------------- | -------------- | ----------------------------------------- |
| Ordinary (fristgemäße) dismissal                    | ✅ Yes         | Standard notice period                    |
| Extraordinary (außerordentliche) dismissal          | ✅ Yes         | Shortened 3-day deadline                  |
| Dismissal during probationary period (Wartezeit)    | ✅ Yes         | BAG settled since 1978                    |
| Mass dismissal (Massenentlassung)                   | ✅ Yes         | Plus separate KSchG §§ 17-18 notification |
| Change notice (Änderungskündigung)                  | ✅ Yes         | Treated as dismissal for § 102 purposes   |
| Termination by mutual agreement (Aufhebungsvertrag) | ❌ No          | Not a Kündigung                           |
| Fixed-term contract expiry                          | ❌ No          | No dismissal act required                 |

#### B.2 Minimum Content of the Anhörung Communication

The employer's written communication to the works council must include:

1. **Identity** of the employee to be dismissed
2. **Type of dismissal** — ordinary or extraordinary
3. **Intended dismissal date** (or notice end date)
4. **All material facts** that form the employer's subjective basis for dismissal, including:
   - For behavioural (verhaltensbedingte) dismissal: documented incidents, prior warnings
   - For personal (personenbedingte) dismissal: health facts, capacity issues, prognosis
   - For operational (betriebsbedingte) dismissal: business rationale, social selection criteria, alternatives considered
5. **Social data** (Sozialdaten): length of service, age, family obligations — relevant to social selection

**Substantive equivalence doctrine**: Disclosure is sufficient if the works council possesses
actual knowledge of the facts even if not formally communicated. However, employer should not
rely on this — document complete disclosure to protect against later voidance claims.

#### B.3 Response Deadlines — The Fatal Window

| Dismissal Type          | Works Council Response Deadline | Employer Wait Rule                                 |
| ----------------------- | ------------------------------- | -------------------------------------------------- |
| Ordinary dismissal      | **1 week (7 calendar days)**    | MUST NOT deliver Kündigung before deadline expires |
| Extraordinary dismissal | **3 calendar days**             | MUST NOT deliver Kündigung before deadline expires |

⚠️ **FATAL FLAW RULE**: A dismissal delivered to the employee **before the response deadline
expires** is **void ab initio** (unwirksam) — regardless of the substantive merits of the
dismissal. This is one of the most common and costly employer errors in German labor law.

- **Silence within deadline = implicit approval** (Billigung durch Schweigen)
- Works council may also expressly consent before the deadline expires, allowing earlier delivery.

#### B.4 Works Council Response Options

| Response                | Works Council Action                           | Employer Implication                        |
| ----------------------- | ---------------------------------------------- | ------------------------------------------- |
| Silence                 | Deadline expires without response              | Deemed consent; employer may proceed        |
| Express consent         | Written agreement before deadline              | Employer may deliver dismissal immediately  |
| Concerns (Bedenken)     | Non-binding statement                          | Employer may still proceed; note in records |
| Objection (Widerspruch) | Formal written objection on §102 Abs.3 grounds | Triggers continued employment obligation    |

#### B.5 Grounds for Works Council Objection (§ 102 Abs. 3 — 5 Grounds)

Works council may formally object if:

1. Employer failed to follow social selection principles (Sozialauswahl)
2. Dismissal violates a workplace guideline or works agreement
3. Employee could be retained in another position within the establishment or enterprise
4. Employee could be retained after retraining or further training (Umschulung/Fortbildung)
5. Employee could continue employment under changed conditions (subject to employee consent)

#### B.6 Continued Employment Obligation (§ 102 Abs. 5)

If the works council files a **timely and formally valid objection**:

- Employee entitled to **continued employment** under unchanged conditions until final court judgment
- Obligation persists even if employer disagrees with objection
- Court may exempt employer only if:
  - The claim is manifestly unfounded (offensichtlich unbegründet)
  - Continued employment would cause **disproportionate economic burden** on the employer
  - Prospects of claim are very weak

**Employer checklist for § 102 compliance:**

- [ ] Notification in writing with all material facts
- [ ] Delivered to works council chairman or deputy
- [ ] Date of delivery documented
- [ ] Response deadline calculated correctly
- [ ] Dismissal NOT delivered until deadline expired (or express consent received)
- [ ] Works council response (or silence) documented

**Severity: RED** — Dismissal without § 102 Anhörung is expressly void by statute:
_"Eine ohne Anhörung des Betriebsrats ausgesprochene Kündigung ist unwirksam"_ (§ 102 Abs. 1 S. 3 BetrVG).

---

### Module C — § 87 BetrVG: Mandatory Codetermination

**Trigger**: Employer plans any measure falling within § 87 Abs. 1 Nr. 1–14.
**Threshold**: Works council exists; no statutory or collective agreement already regulates the matter
(§ 87 Abs. 1 S. 1 tariff priority clause).

#### C.1 Pre-Screening: Tariff Priority Clause

Before assessing any § 87 obligation, verify:

> Does an applicable **Tarifvertrag** (collective agreement) or **Gesetz** (statute) already
> regulate this specific matter in a way that displaces works council codetermination?

- If yes: § 87 codetermination does **not** arise for that matter — but document the basis.
- If the collective agreement contains an **opening clause** permitting Betriebsvereinbarung:
  § 87 codetermination applies within the permitted scope.

#### C.2 The 14 § 87 Abs. 1 Codetermination Categories

| Nr. | Category                                                            | Key Triggers                                                              | AI/Digital Notes                                                                                     |
| --- | ------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1   | Workplace order and conduct (Ordnung des Betriebs)                  | Workplace conduct rules, dress codes, use-of-equipment policies           | AI acceptable-use policies                                                                           |
| 2   | Work hours (Arbeitszeit)                                            | Start/end times, breaks, weekly distribution                              | Algorithmic scheduling systems                                                                       |
| 3   | Temporary hour changes                                              | Short-time work (Kurzarbeit), overtime                                    | —                                                                                                    |
| 4   | Payment modalities                                                  | Salary payment timing, location, method                                   | Digital payroll systems                                                                              |
| 5   | Vacation principles                                                 | General vacation policy and scheduling rules                              | —                                                                                                    |
| 6   | Technical monitoring systems (technische Überwachungseinrichtungen) | **Any system technically capable of monitoring behaviour or performance** | AI performance analytics, keyloggers, GPS tracking, video surveillance, algorithmic decision systems |
| 7   | Workplace safety and health                                         | OSH measures, occupational health screenings                              | —                                                                                                    |
| 8   | Social facilities                                                   | Canteen, sports, childcare administration                                 | —                                                                                                    |
| 9   | Company housing                                                     | Assignment terms                                                          | —                                                                                                    |
| 10  | Wage/bonus principles                                               | Pay structures, grading principles                                        | Algorithmic pay determination                                                                        |
| 11  | Piecework/incentive rates                                           | Piece rates, target bonuses                                               | Productivity-based AI systems                                                                        |
| 12  | Suggestion schemes                                                  | Innovation scheme rules                                                   | —                                                                                                    |
| 13  | Group work                                                          | Group work organisation principles                                        | —                                                                                                    |
| 14  | Mobile work (Mobiles Arbeiten)                                      | Remote work design via IT systems                                         | Added by amendment 19.07.2024, BGBl. I Nr. 248                                                       |

#### C.3 AI and Digital Monitoring — § 87 Nr. 6 in Detail

**Key rule** (Hamburg ArbG 16.01.2024, Az. 24 BVGa 1/24):

- § 87 Nr. 6 is triggered by technical **suitability for monitoring** — not by actual monitoring use
- Employer needs works council consent even if the system is deployed for other purposes but is
  technically capable of tracking employee behaviour or performance
- **Exception**: Employees voluntarily using third-party tools (e.g., ChatGPT with private
  accounts, no employer access to data) — no § 87 Nr. 6 trigger

**EU AI Act overlay** (in force 01.08.2024):

- HR applications classified as **high-risk AI systems** include: hiring screening, task assignment,
  performance evaluation, promotion decisions, and dismissal-related scoring
- Deploying a high-risk AI system requires works council consultation under § 87 Nr. 6 [VERIFY:
  final BMAS guidance on AI Act/BetrVG interaction pending]
- Recommend Betriebsvereinbarung on AI usage as best practice even where not strictly mandated

#### C.4 Procedure When Codetermination Right Arises

1. Employer presents the planned measure to works council with full technical/operational detail
2. Works council has **right to negotiate** — can propose modifications or alternatives
3. If agreement reached: execute as **Betriebsvereinbarung** (see Module F) or joint protocol
4. If no agreement: either party may invoke **Einigungsstelle** (see Module E)
5. Einigungsstelle decision **replaces agreement and is binding** (§ 76 Abs. 5 BetrVG)

**Enforcement**: Works council has **Unterlassungsanspruch** (cessation claim) — employer
cannot implement measure until codetermination is satisfied. Works council may obtain
interim injunction in Beschlussverfahren.

**Severity: RED** — Implementation of § 87 measure without consent or Einigungsstelle
resolution is a pre-implementation blocker.

---

### Module D — § 80 BetrVG: General Information Rights

**Trigger**: Any employer action that affects the workforce, even if no specific consultation
right is engaged.

#### D.1 Core Obligation — "Rechtzeitig und Umfassend"

§ 80 Abs. 2 S. 1 BetrVG requires the employer to inform the works council:

- **Rechtzeitig** (timely): so early that the works council can still fulfil its statutory tasks
  in relation to the matter — not after decisions are finalised
- **Umfassend** (comprehensively): all information materially relevant to the works council's
  task — not selectively filtered by the employer

**Practical standard**: Information obligation attaches the moment the employer **begins planning**
— not merely when a decision is confirmed. Disclosure only after "exploring options" is too late
if real planning activity has begun.

#### D.2 Specific Information Rights Under § 80

| Information Type                                     | Employer Obligation                                        |
| ---------------------------------------------------- | ---------------------------------------------------------- |
| Personnel planning                                   | Information on planned staffing changes, headcount targets |
| Non-employee workforce (agency workers, contractors) | Duration, location, tasks, qualifications                  |
| Gross wage/salary lists                              | Provide on request at any time                             |
| Employment of severely disabled persons              | Regular statistics                                         |
| Occupational safety measures                         | All planned or implemented measures                        |

#### D.3 Economic Committee (Wirtschaftsausschuss) — § 106 BetrVG

- Applies in companies with **> 100 regularly employed workers**
- Separate body from works council; liaisons between them
- Employer must provide:
  - Financial statements, annual reports, economic situation
  - Personnel planning and economic impact of planned measures
  - Production and investment plans
- Trade secrets: narrow carve-out; employer must document genuine secrecy rationale — blanket refusal invalid

**Sanctions**: Failure to provide timely/complete information = administrative offense under
§ 121 BetrVG — fine up to **€10,000** per violation.

---

### Module E — Einigungsstelle (§ 76 BetrVG): Conciliation Board

**Trigger**: Employer and works council reach impasse on any matter subject to mandatory
codetermination (§§ 87, 91, 94 BetrVG) or dispute resolution (§ 76 Abs. 6).

#### E.1 Formation and Composition

| Element         | Rule                                                                 |
| --------------- | -------------------------------------------------------------------- |
| Formation       | By mutual agreement (permanent or ad-hoc) OR labor court appointment |
| Composition     | Equal representatives + **neutral independent chair**                |
| Chair selection | Agreed by parties; if no agreement, appointed by labor court         |
| Meeting venue   | Neutral; chair has procedural discretion                             |

#### E.2 Procedure

1. **Initiation**: Either party may demand Einigungsstelle — no prerequisite to exhaust direct negotiations
2. **Chair appointment**: If parties cannot agree on chair within reasonable time, either party
   applies to labor court (§ 76 Abs. 2 S. 2 ArbGG) — expedited appointment
3. **Proceedings**: Oral hearings; chair may take evidence, hear experts; board deliberates
4. **Voting rule**: Chair abstains in first round; if no majority, chair casts decisive vote in second round
5. **Decision**: Written, with reasons — replaces agreement; **binding on both parties**
6. **Timeline**: Statutory "unverzüglich" (without delay); simple matters hours–days; complex technology deployments may require multiple sessions and expert input

#### E.3 Binding Authority: Sozialplan vs. Interessenausgleich

| Matter                             | Einigungsstelle Can Bind?                                                                                |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------- |
| § 87 codetermination matters       | ✅ Yes — binding decision                                                                                |
| Sozialplan (§ 112 Abs. 4)          | ✅ Yes — binding decision                                                                                |
| Interessenausgleich (§ 112 Abs. 2) | ❌ No — board may mediate but cannot bind either party to proceed or not proceed with operational change |

#### E.4 Challenging Board Decisions

- Must be challenged in **Beschlussverfahren** within **2 weeks** of decision being served
- Ground: Einigungsstelle exceeded its competence (Überschreitung des Ermessens/Zuständigkeit)
- Procedural errors that do not affect substance rarely succeed

---

### Module F — § 77 BetrVG: Betriebsvereinbarung Drafting and Validity

**Trigger**: Employer and works council are concluding, amending, or terminating a works agreement.

#### F.1 Form Requirements (§ 77 Abs. 2 BetrVG)

The Betriebsvereinbarung is only valid if:

| Requirement                  | Details                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Written form**             | Agreement must be in writing (Schriftform)                                                           |
| **Signatures**               | Both the employer **and** the works council chairman (or deputy) must sign **the same document**     |
| **Electronic form**          | Since 18.06.2021 (BetrVG reform): qualified electronic signature (§ 126a BGB) acceptable             |
| **Works council resolution** | Internal works council vote must precede signature — absence of resolution renders agreement invalid |
| **Publication duty**         | Must be displayed in the establishment or made accessible to employees                               |
| **Annexes**                  | Must be signed or clearly incorporated by reference in the main agreement                            |

**Common defect**: Dynamic references to external documents ("as amended from time to time")
are generally invalid — agreement must be self-contained.

#### F.2 Tariff Priority (§ 77 Abs. 3 BetrVG)

Betriebsvereinbarungen **may not** regulate:

- Wages and other working conditions **already regulated by a Tarifvertrag** — unless the
  Tarifvertrag contains an opening clause permitting supplementation
- This is the § 77 Abs. 3 "Tarifsperre" (tariff bar)

**Practical check**: Before drafting any Betriebsvereinbarung touching pay, hours, or working
conditions — verify that no applicable Tarifvertrag covers the matter.

#### F.3 Direct and Mandatory Effect (§ 77 Abs. 4 BetrVG)

- Betriebsvereinbarung provisions apply **directly and mandatorily** to employment relationships
- Employer cannot contract below Betriebsvereinbarung standards with individual employees
- More favourable individual terms are preserved (Günstigkeitsprinzip)

#### F.4 Termination and After-Effect (Nachwirkung) (§ 77 Abs. 5–6 BetrVG)

| Rule                           | Details                                                                                                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ordinary termination notice    | 3 months (default) unless agreement specifies otherwise                                                                                                              |
| Termination without notice     | By mutual consent only                                                                                                                                               |
| **Nachwirkung (after-effect)** | Normative provisions of Betriebsvereinbarungen that were subject to mandatory codetermination (§ 87) continue to apply after expiry until replaced by new regulation |
| Exceptions to Nachwirkung      | Non-codetermination subject matter — no Nachwirkung                                                                                                                  |

---

### Module G — §§ 111–113 BetrVG: Betriebsänderung, Interessenausgleich, and Sozialplan

**Trigger**: Employer plans an operational change (Betriebsänderung) in an enterprise
with **> 20 eligible employees** and an existing works council.

#### G.1 Definition of Betriebsänderung (§ 111 Abs. 1 and 3 BetrVG)

Five statutory categories:

| Category                                                          | Examples                                                                     |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Restriction or closure** (Einschränkung/Stilllegung)            | Plant closure, significant workforce reduction                               |
| **Relocation** (Verlegung)                                        | Moving the entire establishment or substantial parts to a different location |
| **Merger or split** (Zusammenschluss/Aufspaltung)                 | Consolidating two establishments; dividing one                               |
| **Fundamental organisational change** (Betriebliche Umgestaltung) | Major restructuring of business organisation, purpose, or equipment          |
| **New work methods or processes** (Neue Arbeitsmethoden)          | Introduction of fundamentally different production or work processes         |

**Triggering condition**: The change must involve or result in **wesentliche Nachteile**
(substantial/material disadvantages) for a significant portion of the workforce.

**Workforce reduction thresholds** [VERIFY — proportional triggers]:

- Small establishments (21–59): reduction of 20% or minimum 6 employees
- Medium establishments (60–250): reduction of 20% or minimum 37 employees
- Large establishments (> 250): minimum 30 employees or 10%

#### G.2 Employer Obligations — Timely and Comprehensive Disclosure

Must inform works council:

- **Early** — before any planning decisions crystallise (not after internal sign-off)
- **Comprehensively** — including strategic rationale, financial context, planned timeline,
  and projected employee impacts
- **In writing** (best practice — statute does not specify form, but writing is essential for
  evidence purposes)
- For establishments **> 300 employees**: works council may appoint an **external advisor** at
  employer expense (§ 111 Abs. 2 S. 2)

#### G.3 Interessenausgleich — Interest Balance Agreement

An Interessenausgleich is a negotiated agreement addressing:

- **Whether** the operational change will proceed
- **When** it will be implemented
- **How** (the specific manner of execution)

**Key characteristics:**

| Feature                         | Rule                                                                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Binding force**               | **NOT binding** — works council cannot compel an Interessenausgleich in Einigungsstelle                                         |
| **Genuine negotiation**         | Employer must negotiate with Einigungswille (genuine intent to agree) — pro forma consultation is insufficient                  |
| **Consequence of no agreement** | Employer may proceed with change — but exposes itself to § 113 Nachteilsausgleich                                               |
| **Name list (Namensliste)**     | If Interessenausgleich includes list of employees to be dismissed, creates § 1 Abs. 5 KSchG presumption of social justification |

#### G.4 Sozialplan — Social Plan

A Sozialplan is an agreement or board decision addressing:

- Compensation for **economic disadvantages** suffered by employees due to the Betriebsänderung

**Key characteristics:**

| Feature                        | Rule                                                                                                                                                  |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Binding force**              | ✅ **Binding** — Einigungsstelle can impose Sozialplan if parties cannot agree (§ 112 Abs. 4)                                                         |
| **Minimum content**            | Must address the specific economic consequences of the planned change                                                                                 |
| **Severance formulas**         | No statutory formula — board has equitable discretion; typical approaches: monthly-salary multiples × years of service × age factor                   |
| **Relationship to KSchG § 1a** | Sozialplan severance and § 1a statutory severance are independent; § 1a only applies when employer offers it individually at time of dismissal notice |

#### G.5 § 112a BetrVG — Sozialplan Exemption for New Businesses

- Enterprises founded **within the last 4 years** are exempt from mandatory Sozialplan obligations
- **Exception**: Exemption does NOT apply to companies created through legal restructuring
  (Betriebsumwandlung, merger, Abspaltung, Ausgliederung, spin-off, creation of subsidiary)

#### G.6 Nachteilsausgleich — Compensation for Missing Interessenausgleich (§ 113 BetrVG)

If employer:

1. Fails to attempt Interessenausgleich with the works council, **or**
2. Deviates from a concluded Interessenausgleich without compelling operational reasons

→ Employer owes **Nachteilsausgleich** (equalization payments) to each affected employee.

Nachteilsausgleich is calculated by reference to § 10 KSchG severance formula:

- 0.5 × monthly gross salary × year of service (capped at 12 monthly salaries)
- Individual employees may claim independently in Urteilsverfahren (labor court, adversarial)

**Critical timing trap**: Dismissals implemented **before** Interessenausgleich has been
attempted may expose the employer to both invalid dismissals (if § 99 or § 102 also violated)
and § 113 Nachteilsausgleich liability.

---

### Module H — European Works Council (EBRG / Directive 2009/38/EC)

**Trigger**: Employer operates a group or undertaking with:

- **≥ 1,000 employees** across EU/EEA Member States, AND
- **≥ 150 employees** in each of at least **2 different Member States**

#### H.1 German Implementation — EBRG

German law: Gesetz über Europäische Betriebsräte (EBRG), amended 07.04.2011.
The EBRG implements EU Directive 2009/38/EC (recast).

#### H.2 EWC Information and Consultation Rights

| Right                             | Scope                                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Information**                   | Employee representatives receive information on decisions that may significantly affect employees across the group — before decision is finalised |
| **Consultation**                  | Meaningful input on transnational decisions — opinion must be able to influence the decision                                                      |
| **Annual/extraordinary meetings** | At least one annual meeting; extraordinary meeting for transnational changes affecting ≥ 2 Member States                                          |

**Definitional note**: "Transnational" matters are those affecting establishments or undertakings
in at least 2 Member States, regardless of whether they originate in Germany.

#### H.3 Interaction with Local BetrVG Betriebsrat

- **Complementary, not exclusive**: EWC operates at group/multinational level; local Betriebsrat
  retains full rights under §§ 99, 102, 87, 111–113 for establishment-level matters
- EWC consultation does **not** substitute for or abbreviate local BetrVG consultation
- Group-level restructuring announcement → EWC first (transnational impact) → local Betriebsrat
  subsequently (establishment-level impacts and local §§ 111–113 procedure)

#### H.4 SE-BetrVG (Societas Europaea)

For groups that have adopted the SE corporate form:

- SE-BetrVG provides enhanced **board-level employee participation** rights
- Integrates European Company law requirements with German codetermination principles
- Separate negotiation procedure for SE participation agreement prior to SE registration

---

## Severity Classification

All findings from the analysis modules are classified as:

| Classification                          | Meaning                                                                                                                                          | Action Required                                                                                   |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 🔴 **RED — Pre-Implementation Blocker** | Consultation step is legally required and has not been completed; proceeding without it renders the measure **void or creates direct liability** | Stop. Complete the required consultation step before any further action.                          |
| 🟡 **YELLOW — Procedural Risk**         | Step is likely required or there is material uncertainty; proceeding carries significant litigation risk                                         | Resolve the uncertainty before proceeding. Seek confirmation from works council or legal counsel. |
| 🟢 **GREEN — Compliant**                | Consultation obligation satisfied or does not apply to this measure                                                                              | Proceed. Document the basis for compliance.                                                       |
| ⚪ **N/A — Not Applicable**             | The measure or threshold does not trigger this module                                                                                            | Note in output and move on.                                                                       |

---

## Prioritisation Framework

Rank findings in three tiers:

### Tier 1 — Must Resolve Before Any Implementation (Pre-Implementation Blockers)

- All RED findings from §§ 99, 102, 87 analysis
- Unresolved Einigungsstelle disputes on § 87 matters
- Missing § 111 disclosure on Betriebsänderung

### Tier 2 — Resolve Before or Concurrent With Implementation

- § 80 information rights gaps
- Betriebsvereinbarung form defects (unsigned annexes, missing resolution)
- § 102 Anhörung content gaps that may attract objection
- Sozialplan negotiation initiation

### Tier 3 — Documentation and Risk Mitigation

- Records of works council responses and silence periods
- Completeness of disclosure documentation
- EWC consultation records for transnational measures

---

## Citation Quality Gates

Run silently before delivering any output. Fail action required before delivery:

| Gate           | Rule                                                                                                                                         | Fail Action                       |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every legal claim cites a specific BetrVG section, BAG decision, or named principle                                                          | Add citation or mark [UNVERIFIED] |
| **Format**     | BetrVG citations in format "§ [section] Abs. [subsection] S. [sentence] BetrVG"; BAG citations include Az. (file reference)                  | Fix format                        |
| **Currency**   | BetrVG provisions checked against current version at gesetze-im-internet.de — confirm §87 Nr.14 mobile work amendment (19.07.2024) reflected | Flag [CHECK CURRENCY]             |
| **Domain**     | Analysis stays within German private-sector BetrVG scope — does not bleed into Personalvertretungsgesetz (public sector)                     | Remove or flag                    |
| **Confidence** | Uncertainty explicitly stated with [VERIFY]; not hidden                                                                                      | Add confidence qualifier          |

---

## Self-Interrogation for RED Findings

For any finding classified RED, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the RED classification follow logically from the
cited statutory provision? Would a German Arbeitsgericht reach the same conclusion on these
facts?

**Pass 2 — Completeness**: Have all relevant BetrVG sections, applicable Tarifvertrag
provisions, and existing Betriebsvereinbarungen been considered? Is there a collective
agreement carve-out that displaces the obligation?

**Pass 3 — Challenge**: What is the strongest argument that this obligation does NOT apply?
For example: does the tariff priority clause under § 87 Abs. 1 S. 1 eliminate the
codetermination right? Is the establishment below the threshold? Is there no works council?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                   | Action                                     |
| ------------ | --------- | --------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Clear statutory text, settled BAG jurisprudence           | State with confidence                      |
| **High**     | 0.80–0.94 | Strong authority, minor factual questions remain          | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good arguments, factual uncertainty or pending case law   | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely contested — e.g., novel AI/monitoring scenarios | Flag for specialist legal review           |
| **Unlikely** | 0.0–0.39  | Speculative basis                                         | Do not assert; flag [UNCERTAIN]            |

---

## Anti-Patterns Catalogue

What NOT to do when managing Betriebsrat consultation in Germany:

1. **Delivering dismissal before the 1-week Anhörung deadline** — the single most common and
   most costly error; renders the Kündigung void regardless of substantive merit. Always
   calculate the deadline and calendar-block it.

2. **Treating works council silence as active consent in § 99 situations before the deadline** —
   fiktive Zustimmung (deemed consent) only arises _after_ the 1-week period expires. Acting on
   day 5 because the works council has not called back is a procedural violation.

3. **Providing incomplete dismissal reasons in § 102 Anhörung** — employer must disclose all
   material facts; selectively omitting inconvenient history or the employee's social data
   creates grounds for a voidance challenge even if the dismissal itself is substantively justified.

4. **Assuming no codetermination obligation because the system "just collects data"** — § 87
   Nr. 6 is triggered by technical _suitability_ for monitoring behaviour or performance, not by
   actual monitoring activity. AI analytics tools, productivity trackers, and access-log systems
   all require works council consent even if management never intends to use them for surveillance.

5. **Forgetting the § 87 Abs. 1 S. 1 tariff priority check** — before engaging § 87 negotiation
   at all, confirm that no applicable Tarifvertrag already regulates the matter. Failing this check
   leads to unnecessary negotiation or, worse, to a Betriebsvereinbarung that is invalid under
   § 77 Abs. 3 Tarifsperre.

6. **Rolling out an operational change without attempting Interessenausgleich** — even though the
   Einigungsstelle cannot compel an Interessenausgleich, the failure to attempt genuine negotiation
   triggers § 113 Nachteilsausgleich liability for every affected employee. The employer's savings
   on the agreement typically are dwarfed by the individual compensation claims.

7. **Using oral or unsigned Betriebsvereinbarungen** — § 77 Abs. 2 mandates written form with
   both parties' signatures on the same document. Oral agreements or exchanged emails do not
   constitute a Betriebsvereinbarung and have no normative force.

8. **Dynamic references in Betriebsvereinbarungen** — blanket clauses incorporating external
   documents "in their current version" are void. The agreement must be self-contained at the
   time of signature.

9. **Implementing measures during Einigungsstelle proceedings as "accomplished facts"** —
   employers who proceed with § 87 measures before the Einigungsstelle has resolved the dispute
   face injunctions and, in egregious cases, § 23 Abs. 3 BetrVG gross-breach applications. The
   only safe path is to await the board's binding decision.

10. **Forgetting Nachwirkung when terminating a Betriebsvereinbarung** — normative provisions of
    a § 87-based Betriebsvereinbarung continue as after-effect upon termination until replaced.
    Believing that termination of the agreement restores full unilateral employer discretion is wrong.

11. **Not extending § 102 consultation to dismissals during probationary period** — some employers
    incorrectly assume that the Wartezeit (probationary period before KSchG applies) also suspends
    BetrVG obligations. The BAG settled this against employers decades ago: § 102 Anhörung is
    required for every dismissal, including those during the Wartezeit.

12. **Conflating EWC consultation with local BetrVG consultation** — completing the EWC information
    process does not discharge the employer's obligations to local Betriebsräte. Both procedures
    must run; the EWC process typically runs first (group-level), local BetrVG subsequently
    (establishment-level).

13. **Missing the § 113 Nachteilsausgleich exposure when naming employees pre-Interessenausgleich**
    — dismissing employees identified in a restructuring plan before the Interessenausgleich attempt
    is complete signals bad-faith negotiation and substantially strengthens § 113 claims.

14. **Ignoring the § 112a four-year new-business exemption trap** — the Sozialplan exemption
    applies only to genuinely newly founded businesses, not to entities formed through restructuring
    (Umwandlung, Abspaltung, Ausgliederung). Miscategorisation leads to unexpected Sozialplan
    obligations materialising when the Einigungsstelle is invoked.

15. **Treating information rights under § 80 as a formality** — works council can challenge
    employer measures on the grounds that information was untimely or incomplete. Build a clear
    documentary record of when disclosure was made and what was provided.

16. **Overlooking the works council resolution requirement for Betriebsvereinbarung** — the
    works council chairman's signature is not sufficient; a valid internal works council resolution
    (Beschluss) must precede the signature. Agreements signed without such a resolution can be
    voided.

17. **Failing to model the Sozialplan budget before entering Einigungsstelle proceedings** —
    the Einigungsstelle has broad equitable discretion on severance formulas and may impose a plan
    that exceeds the employer's expectations. Enter proceedings with a fully-costed model of
    expected outcomes, including age and tenure distributions.

---

## Writing Standards

Before delivering any analysis output:

- [ ] Use correct German legal terminology alongside English explanations
- [ ] All BetrVG section references in format "§ [N] Abs. [N] S. [N] BetrVG"
- [ ] BAG citations include "Az." (Aktenzeichen) and decision date
- [ ] No assertion of legal positions without cited authority or [VERIFY] tag
- [ ] RED findings lead the output — do not bury pre-implementation blockers
- [ ] Recommendations are actionable (state who must do what by when)
- [ ] Plain-language summary before technical analysis for non-lawyer users
- [ ] Confidence scores stated for any novel or contested legal position
- [ ] No jurisdiction bleed — do not apply BetrVG rules to public sector or non-German entities

---

## External Tool Integration

**With legalcode-mcp connected** (preferred):

- Use `workspace_search` to retrieve current BetrVG section text and recent BAG decisions
- Query: `"§ 99 BetrVG Zustimmungsverweigerung"` or `"BAG § 102 Anhörung 2024"`
- Save most relevant results to `/tmp/legalcode-betrv g-research.md` for session reference
- Flag all legalcode-mcp-sourced citations as VERIFIED in Glass Box audit trail

**Without legalcode-mcp**:

- Proceed using statutory references in this skill
- Mark all statutory citations with [VERIFY]
- Direct user to gesetze-im-internet.de and bundesarbeitsgericht.de for verification
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

---

## Glass Box Audit Trail

Include this block at the end of every analysis output, completed:

```yaml
glass_box:
  skill_name: "legalcode-de-betriebsrat-consultation"
  jurisdiction: "Germany (BetrVG — private sector)"
  establishment_profile:
    headcount_band: "[≤20 | 21–100 | 101–300 | >300 | Unknown]"
    works_council_exists: "[Yes | No | Unknown]"
    collective_agreement: "[None | Flächentarifvertrag | Haustarifvertrag | Unknown]"
  modules_applied:
    - "[A: §99 | B: §102 | C: §87 | D: §80 | E: Einigungsstelle | F: BV | G: §§111-113 | H: EBRG]"
  findings_summary:
    red_pre_implementation_blockers: "[count]"
    yellow_procedural_risks: "[count]"
    green_compliant: "[count]"
    na_not_applicable: "[count]"
  legalcode_mcp: "[Connected | Not connected]"
  citations_verified: "[N VERIFIED / N UNVERIFIED]"
  confidence_overall: "[HIGH | MEDIUM | LOW] — [one-line rationale]"
  limitations:
    - "[Any factual uncertainties, missing documents, or scope limitations]"
  reviewer: "AI-assisted — requires Rechtsanwalt / Fachanwalt für Arbeitsrecht review"
  date: "[ISO 8601 date of analysis]"
```

---

## Output Format Template

Structure every analysis output as follows:

```markdown
# Betriebsrat Consultation Analysis

**Establishment**: [name or description]
**Measure(s) assessed**: [brief description]
**Date**: [ISO 8601]

---

## Plain-Language Summary

[2–3 sentence non-technical summary of the key findings and required actions, for HR/business audience]

---

## Pre-Implementation Blockers (RED)

> Complete these steps BEFORE implementing any part of the planned measure.

| Finding               | Module        | Required Action        | Deadline         |
| --------------------- | ------------- | ---------------------- | ---------------- |
| [Finding description] | [§ reference] | [Specific action step] | [Before/by date] |

_(If none: "No pre-implementation blockers identified.")_

---

## Procedural Risks (YELLOW)

| Finding               | Module        | Risk                       | Recommended Action |
| --------------------- | ------------- | -------------------------- | ------------------ |
| [Finding description] | [§ reference] | [Litigation/voidance risk] | [Action]           |

_(If none: "No procedural risks identified.")_

---

## Compliant Items (GREEN)

| Item               | Module        | Basis           |
| ------------------ | ------------- | --------------- |
| [Item description] | [§ reference] | [Why compliant] |

---

## Module-by-Module Analysis

### Module [X] — [§ reference and title]

[Detailed analysis applying the module's checklist to the specific facts]

**Classification**: 🔴 RED / 🟡 YELLOW / 🟢 GREEN / ⚪ N/A
**Confidence**: [Level] ([score range])

---

## Recommended Consultation Timetable

| Step | Action             | Responsible                   | Target Date |
| ---- | ------------------ | ----------------------------- | ----------- |
| 1    | [Step description] | [Employer/BR/Einigungsstelle] | [Date]      |
| 2    | ...                | ...                           | ...         |

---

## Betriebsvereinbarung Recommendations

_(Include if Module F is applicable)_

[Draft BV scope, key clauses recommended, tariff priority check result]

---

## Glass Box Audit Trail

[Insert completed YAML block from Glass Box section]
```

---

## Localization Notes

This skill is Germany-specific. For cross-border application:

- **Austria**: Similar Arbeitsverfassungsgesetz (ArbVG) framework but different procedural rules
  and consent grounds — do not apply this skill to Austrian Betriebsräte without Austrian law review
- **Netherlands**: Ondernemingsraad under the WOR (Wet op de ondernemingsraden) — structurally
  similar but materially different thresholds and consent powers
- **EU-level measures**: Always assess EWC obligations under Module H alongside local BetrVG

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from:

- Betriebsverfassungsgesetz (BetrVG) current text (gesetze-im-internet.de)
- BAG case law 2020–2025 including BAG 13.12.2023 (Az. 1 ABR 28/22), BAG 25.02.2025 (Az. 1 ABR 18/24), BAG 26.11.2024 (Az. 1 ABR 12/23)
- Hamburg ArbG 16.01.2024 (Az. 24 BVGa 1/24) on § 87 Nr. 6 AI monitoring
- EU AI Act (in force 01.08.2024) — HR high-risk classification overlay
- EBRG (Gesetz über Europäische Betriebsräte), amended 07.04.2011
- Existing legalcode repository skill: `germany-works-council-codetermination-checklist` (informing structural approach)
- Legalcode 2-agent research pipeline with web-backed research
