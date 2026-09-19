---
name: legalcode-eu-whistleblower-directive
description: Implement and audit compliance with EU Whistleblower Directive 2019/1937. Use when building
  a whistleblower program from scratch, auditing an existing program, conducting a gap analysis against
  the Directive, advising on national implementation differences (Hinweisgeberschutzgesetz, Loi Sapin
  II, Wet Bescherming Klokkenluiders, Protected Disclosures Act, etc.), drafting internal reporting policies,
  handling retaliation allegations, designing intake/triage workflows, or assessing interaction with sector-specific
  rules (MAR, MiFID II, CRD V).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Implement and audit compliance with EU Whistleblower Directive 2019/1937. Covers internal reporting channel design, protected persons scope, reportable breach categories, 7-day acknowledgment and 3-month feedback obligations, investigator independence, confidentiality requirements, anti-retaliation framework (Article 19 burden-of-proof reversal), external reporting authorities, public disclosure conditions (Article 15), GDPR interaction, and national transposition variations across all EU Member States. Use when building a whistleblower program from scratch, auditing an existing program, conducting a gap analysis against the Directive, advising on national implementation differences (Hinweisgeberschutzgesetz, Loi Sapin II, Wet Bescherming Klokkenluiders, Protected Disclosures Act, etc.), drafting internal reporting policies, handling retaliation allegations, designing intake/triage workflows, or assessing interaction with sector-specific rules (MAR, MiFID II, CRD V). Jurisdiction: European Union (Directive 2019/1937/EU), with member-state-specific notes.


# Legalcode EU Whistleblower Directive — Compliance & Implementation

> **Disclaimer**: This skill provides a framework for AI-assisted compliance analysis under
> EU Directive 2019/1937 and its national transpositions. It does not constitute legal advice.
> All outputs must be reviewed by a qualified legal professional licensed in the relevant
> Member State before reliance. Laws and transpositions change; verify current applicability
> before acting on any provision described here. Statutory and case law references carry
> hallucination risk — verify against authoritative sources (EUR-Lex, national official gazettes)
> before relying on them.

---

## Purpose and Scope

This skill supports comprehensive compliance work under Directive (EU) 2019/1937 on the
protection of persons who report breaches of Union law (the "Whistleblower Directive" or
"Directive"). It functions in three modes:

**Mode A — Build**: Design and implement a compliant whistleblower program from scratch.

**Mode B — Audit**: Assess an existing program against Directive requirements and produce
a gap analysis with prioritized remediation recommendations.

**Mode C — Advise**: Answer targeted compliance questions about specific provisions,
national transpositions, or particular implementation challenges (e.g., multinational
shared channels, GDPR interaction, retaliation allegations).

**Covers:**

- Entity threshold assessment (50-employee rule, group structures)
- Internal reporting channel design (written + oral, acknowledgment timelines, security)
- Protected persons scope (employees, contractors, facilitators, third persons)
- Reportable breach categories (Article 6 + national extensions)
- Investigation procedures (independence, confidentiality, GDPR)
- Anti-retaliation framework (Article 19 prohibited measures, burden of proof reversal)
- External reporting authorities (by Member State and topic area)
- Public disclosure conditions (Article 15)
- GDPR integration (legal basis, DPIA, Article 23 restrictions, data minimization)
- National transposition variations across key Member States
- Support measures (legal, psychological, financial assistance — Article 20)
- Sector-specific overlaps (MAR, MiFID II, CRD V, food safety, environmental)
- Sanctions and enforcement (CJEU infringement proceedings, national fines)

**Does not:**

- Provide legal advice or replace qualified EU / Member State counsel
- Cover non-EU whistleblower regimes (UK PIDA, US Dodd-Frank, SOX) except by analogy
- Draft full policy documents (it produces structured frameworks and templates to adapt)
- Replace a qualified Data Protection Officer for GDPR purposes

---

## Jurisdiction and Governing Law

**Primary instrument:** Directive (EU) 2019/1937 of the European Parliament and of the
Council of 23 October 2019 — entered into force 16 December 2019.

**Nature:** Minimum harmonisation Directive. Member States may enact stronger protections
but may not go below the Directive's floor.

**Transposition status:** All 27 Member States enacted implementing legislation by May 2024.
The European Commission's July 2024 compliance assessment found material gaps in 15+ Member
States, particularly on material scope, protected persons definitions, and support measures.

**Sectoral lex specialis (Article 3):** In financial services, sectoral whistleblowing rules
take precedence over the Directive where they provide at least equivalent protection:

- Market Abuse Regulation (MAR), Article 32(3)
- Capital Requirements Directive (CRD V), Article 71(3)
- MiFID II, Article 73(2)
- UCITS Directive, Article 99d(5)
- SFTR, Article 24(3); Prospectus Regulation, Article 41(4)

**[MEMBER-STATE-SPECIFIC]** Throughout this skill, provisions marked with
[MEMBER-STATE-SPECIFIC] or flagged with a country code (e.g., [DE], [FR], [NL]) require
verification against the applicable national transposing law. The skill notes where
national implementations vary materially from the Directive floor.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked with
**⟁ CLARIFY**. Rather than assuming context, the workflow pauses to ask when:

- The answer changes the direction of analysis (e.g., which Member States are relevant)
- Multiple valid compliance approaches exist and the organization's preference matters
- Threshold questions determine whether obligations apply at all
- Sector-specific overlaps need to be resolved before applying the Directive framework

If the user has already provided the information, skip the question and proceed with the
analysis stated explicitly.

---

## Workflow

### Step 1: Accept Input and Determine Mode

Accept input in any of these formats:

- **Build mode**: Organisation description, headcount per entity, Member States of operation,
  sector, existing compliance infrastructure, target go-live date
- **Audit mode**: Existing policy documents, current channel descriptions, investigation
  procedures, GDPR/data protection documentation, retaliation incident history
- **Advise mode**: A specific compliance question, scenario, or provision for analysis

**⟁ CLARIFY** — If mode is unclear, ask:

1. **Goal**: Are you (A) building a new whistleblower program, (B) auditing an existing one,
   or (C) answering a specific compliance question?

2. **Organisation type**: Private sector, public sector, or both? (Public sector always
   covered; private sector requires headcount threshold assessment)

3. **Headcount**: How many employees does each legal entity have across EU Member States?
   (Determines whether 50-employee threshold is met per entity)

4. **Sectors**: Does the organisation operate in financial services, food/feed, transport,
   environment, public procurement, competition, or corporate taxation? (Determines whether
   sector-specific lex specialis applies and extends reportable breach categories)

5. **Member States**: In which EU Member States does the organisation have legal entities or
   operations? (Determines which national transposing laws apply)

### Step 2: Entity Mapping and Threshold Assessment

Determine which legal entities are subject to mandatory internal channel obligations.

**The 50-Employee Rule (Article 8):**

| Entity Size            | Obligation                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| **250+ employees**     | Mandatory internal channel — compliance required since 17 December 2021                   |
| **50–249 employees**   | Mandatory internal channel — compliance required since 17 December 2023                   |
| **Below 50 employees** | No mandatory internal channel; anti-retaliation obligations still apply                   |
| **Public sector**      | All public bodies covered regardless of size; municipalities 10,000+ inhabitants included |
| **Financial services** | Sector-specific rules may apply regardless of headcount                                   |

**Shared Channels (Article 8(6)):**

- Entities with 50–249 employees may share a single internal reporting channel across
  multiple group entities
- Entities with 250+ employees must have dedicated channels per legal entity
- [MEMBER-STATE-SPECIFIC] Some Member States permit or restrict shared channel arrangements
  beyond the Directive's floor — verify locally [DE][FR][NL]

**⟁ CLARIFY** — For group structures, ask:

- Which legal entities in the group have 50+ employees in which Member States?
- Is a centralised group-level channel currently in use? If so, does it meet the independence,
  confidentiality, and language requirements for each covered entity?
- Are any entities in the financial services sector that may have separate obligations
  under MAR/MiFID/CRD regardless of headcount?

**Produce an Entity Map:**

```
Entity Name | Jurisdiction | Headcount | Threshold Met? | Channel Required? | Shared Channel OK?
------------|-------------|-----------|----------------|-------------------|-------------------
[Entity 1]  | [DE]        | [350]     | Yes (250+)     | Dedicated          | No
[Entity 2]  | [FR]        | [75]      | Yes (50–249)   | Yes               | Yes (with Entity 3)
[Entity 3]  | [ES]        | [60]      | Yes (50–249)   | Yes               | Yes (with Entity 2)
[Entity 4]  | [AT]        | [25]      | No             | No (anti-ret. applies) | N/A
```

### Step 3: Assess Reportable Breach Scope

Determine which categories of breach the internal channel must cover (Article 6).

**Mandatory Coverage — EU Law Breaches (Article 6(1)):**

| Category                                        | Key Instruments                                               |
| ----------------------------------------------- | ------------------------------------------------------------- |
| Public procurement                              | Directives 2014/24/EU, 2014/25/EU, 2014/23/EU                 |
| Financial services, products, and markets       | MiFID II, MAR, AIFMD, UCITS, CRR/CRD, Solvency II, EMIR, SFTR |
| Anti-money laundering and terrorist financing   | AMLD4, AMLD5, AMLD6                                           |
| Product safety and compliance                   | General Product Safety Directive, sectoral product regs       |
| Transport safety                                | Aviation, maritime, rail, road, inland waterways safety       |
| Environmental protection and nuclear safety     | EIA Directive, Water Framework, Air Quality, Habitats         |
| Food and feed safety, animal health and welfare | Regulation 178/2002 and related                               |
| Data protection and cybersecurity               | GDPR, NIS2 Directive, ePrivacy                                |
| Competition law and State aid                   | Articles 101–109 TFEU, Merger Regulation                      |
| Corporate taxation                              | Arrangements defeating the purpose of tax law                 |
| Financial interests of the EU                   | Budget fraud, corruption affecting EU funds                   |

**[MEMBER-STATE-SPECIFIC] National Extensions:**
Many Member States expanded the material scope beyond EU law breaches. Verify locally:

- **Germany (HinSchG §2)**: Extends to violations of German criminal law and significant
  administrative offences [DE]
- **France (Loi 2022-401)**: Extends to French law violations and threats to general
  interest [FR]
- **Netherlands (Wet BK)**: Follows Directive scope with some extensions [NL]
- **Poland**: Commission July 2024 assessment identified scope limitations; verify current
  status [PL]
- **Hungary, Greece, Romania, Bulgaria**: Commission identified significant material scope
  gaps — do not assume full Directive coverage without local legal verification [VERIFY]

**⟁ CLARIFY** — If the organisation has compliance-relevant activities in multiple sectors:

- Should the skill map reportable breaches sector by sector for each entity?
- Does the organisation want to expand coverage beyond the Directive minimum (best practice
  approach: cover all significant internal misconduct regardless of EU law nexus)?

### Step 4: Protected Persons Analysis

Identify who is protected by the Directive (Article 4). Protection extends far beyond employees.

**Article 4 Protected Persons:**

| Category                      | Description                                                            | Notes                                            |
| ----------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------ |
| Employees                     | Current and former, including civil servants                           | Core category                                    |
| Job applicants                | Persons in pre-employment process                                      | Protection extends before hiring                 |
| Fixed-term/casual workers     | All forms of engagement                                                | Not limited to permanent contracts               |
| Volunteers                    | Unpaid service providers                                               | Included if performing work for the entity       |
| Trainees and apprentices      | Paid or unpaid                                                         | Explicitly included                              |
| Self-employed / freelancers   | Independent contractors                                                | Covered                                          |
| Shareholders                  | Members of ownership                                                   | Included                                         |
| Management / board members    | Administrative, supervisory, management bodies                         | Included                                         |
| Subcontractors / supply chain | Working for or reporting to the entity                                 | Covered                                          |
| **Facilitators**              | Persons assisting the reporter in the reporting process                | Protected from retaliation equally               |
| **Third persons connected**   | Family members, colleagues, persons economically dependent on reporter | Protected if facing retaliation linked to report |

**Condition for Protection (Article 6(1)):**
A reporting person is protected if, at the time of reporting, they had **reasonable grounds
to believe** that:

1. The reported information was true; AND
2. The breach fell within the scope of the Directive

**Critical principles:**

- **Honest mistakes protected**: Inaccuracies discovered after reporting do not forfeit protection (Recital 51)
- **Motives irrelevant**: Protection applies regardless of the reporter's underlying motivation
- **Subjective standard**: Based on what the person knew or reasonably believed at the time of reporting

**[MEMBER-STATE-SPECIFIC] Protection gaps identified by Commission (July 2024):**
Several Member States narrowed the protected persons definition below Article 4's floor.
Verify national implementing law in: Poland [PL], Italy [IT], Hungary [HU], Bulgaria [BG].

### Step 5: Internal Reporting Channel Assessment

Evaluate or design the internal reporting channel against Article 8 and 9 requirements.

#### 5.1 Channel Design Requirements (Article 8)

**Written Channels (at least one required):**

- Secure online form / web portal (preferred — enables anonymity features)
- Physical secure mailbox (designated, locked, access-controlled)
- Postal mail to designated recipient

**Oral Channels (at least one required):**

- Telephone hotline (may be recorded with consent, or transcribed)
- Voice messaging system for after-hours reporting
- In-person meeting upon reporter request

**⟁ CLARIFY** — For existing organisations:

- Which channels currently exist? (Document each type and assess technical adequacy)
- Are anonymous reports accepted and technically protected? (Not mandatory under Directive;
  best practice and required by some Member States [NL])
- Is the channel available 24/7 in all relevant languages?
- Does the channel provider have a GDPR-compliant data processing agreement in place?

#### 5.2 Procedural Obligations (Article 9)

| Obligation                                             | Timeline                                        | Classification |
| ------------------------------------------------------ | ----------------------------------------------- | -------------- |
| Acknowledge receipt of report                          | **Within 7 calendar days**                      | NON-NEGOTIABLE |
| Provide feedback (status, actions taken, or envisaged) | **Within 3 months**                             | NON-NEGOTIABLE |
| Follow-up if investigation exceeds 3 months            | Notify reporter of extended timeline and reason | Required       |
| Communicate final outcome                              | Within reasonable time                          | Required       |

**Common failures — verify each:**

- [ ] Automated 7-day acknowledgment configured and tested
- [ ] 3-month feedback reminder system active
- [ ] Feedback content adequate (not just "we received your report" — must address actions taken or envisaged)
- [ ] Extended timeline notification procedure documented if investigation runs long

#### 5.3 Investigator Independence (Articles 8-9, Recital 56)

Requirements for the designated person or department:

- **Impartial**: Free from conflicts of interest with any matter likely to be reported
- **Independent**: Not in the reporting line of persons likely to be accused
- **Adequately resourced**: Sufficient time, staff, and training to handle reports
- **Trained**: In confidentiality obligations, GDPR requirements, investigation procedures

**Acceptable designations:** Chief Compliance Officer, General Counsel, Internal Audit Head,
dedicated Ethics Officer, external service provider (outsourced hotline). NOT: line managers,
HR business partners reporting to accused, direct reports of likely accused parties.

**Conflict of interest protocol:**

- Screen for conflicts at time of report receipt
- Maintain secondary designated person for conflict situations
- Document screening outcomes

#### 5.4 Confidentiality Requirements (Article 16)

Classify: **COMPLIANT** / **PARTIAL** / **NON-COMPLIANT**

| Requirement                            | Test                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------ |
| Access limited to designated staff     | Only authorised persons can view reports — not general HR, not line management |
| Identity of reporter protected         | Reporter name / identifying info not disclosed without explicit consent        |
| Disclosure only when legally required  | E.g., required by court order, criminal investigation                          |
| Confidentiality obligations documented | Written commitment by all persons with access                                  |
| Technical access controls implemented  | Role-based access, audit logging, no shared credentials                        |

**GDPR Interaction on Confidentiality:**

- Processing is lawful under Article 6(1)(c) GDPR (legal obligation) where national law mandates the channel
- GDPR Article 23 permits restrictions on data subject access rights to protect reporter identity — verify Member State law implements this restriction [MEMBER-STATE-SPECIFIC]
- Do not disclose reporter identity in response to a GDPR Subject Access Request from the accused without legal advice

### Step 6: Anti-Retaliation Framework Assessment

Assess compliance with Article 19's prohibition on retaliation and the burden-of-proof reversal.

#### 6.1 Prohibited Retaliatory Measures (Article 19)

The following are expressly prohibited. Verify each is covered in internal policy:

| #   | Prohibited Measure                                                 |
| --- | ------------------------------------------------------------------ |
| 1   | Dismissal, termination, or threat thereof                          |
| 2   | Suspension from duties                                             |
| 3   | Demotion or denial of promotion                                    |
| 4   | Change of duties or place of work (adverse)                        |
| 5   | Reduction in remuneration, hours, or benefits                      |
| 6   | Negative performance appraisals or references                      |
| 7   | Non-renewal of fixed-term contracts                                |
| 8   | Harassment, intimidation, or ostracism                             |
| 9   | Discrimination in working conditions                               |
| 10  | Blacklisting (internal or industry-wide)                           |
| 11  | Harm to professional or personal reputation                        |
| 12  | Failure to renew or premature termination of a fixed-term contract |
| 13  | Pressure to resign or move to another role                         |
| 14  | Withdrawal of training opportunities                               |
| 15  | Disciplinary measures or sanctions                                 |
| 16  | Coercion, intimidation, threats                                    |
| 17  | Damage to physical or mental health                                |

**Protection also extends to:** facilitators, third persons connected to the reporter (family,
colleagues, persons economically dependent on reporter) — Article 4(4).

#### 6.2 Burden of Proof Reversal (Article 19, Recital 69)

**How the reversal operates:**

**Step 1 — Reporter establishes prima facie case:**
Reporter must demonstrate:

1. They made a report (internal, external, or public disclosure); AND
2. They suffered a detriment (one of the prohibited measures above); AND
3. Temporal proximity (detriment occurred after or in connection with the report)

**Step 2 — Legal presumption of retaliation arises:**
Once Step 1 is established, it is **legally presumed** that the detriment was retaliatory.
The causal link is presumed — the reporter does not need to prove it.

**Step 3 — Employer must rebut:**
The burden shifts entirely to the employer to prove the detriment was based on **"duly
justified grounds"** that are demonstrably unrelated to the protected reporting.

**Practical implications for employers:**

- Document performance issues, disciplinary history, and business justifications **contemporaneously** — not retrospectively after a whistleblower complaint is filed
- Apply consistent standards: if the adverse action would have been taken for the same reason against a non-reporting employee, document the comparator
- Implement advance approval requirements for adverse actions against recent reporters

**[MEMBER-STATE-SPECIFIC] National burden reversal standards:**

- **Germany (HinSchG §36 + §612a BGB)**: Clear reversal; employer must prove non-retaliatory grounds [DE]
- **France (Loi 2022-401 Art. 10)**: Presumption established; employer must rebut with concrete evidence [FR]
- **Netherlands (Wet BK Art. 11)**: Presumption applies [NL]
- **Ireland (PDA 2022 s.11)**: Burden shifts to employer once prima facie case established [IE]
- **Poland**: Burden reversal implemented; exact application developing in courts [PL]

#### 6.3 Interim Relief (Article 21)

Courts must be empowered to grant interim measures to prevent retaliation pending proceedings.
Assess whether the organisation's policy acknowledges and facilitates:

- Suspension of termination decisions pending investigation
- Reinstatement during proceedings
- Injunctive relief against ongoing harassment

### Step 7: External Reporting and Public Disclosure

#### 7.1 External Reporting Authorities (Article 10)

Reporters may choose to report externally rather than (or in addition to) using internal channels.
There is **no requirement to exhaust internal channels first** under the Directive — reporters
may go directly to competent authorities.

**[MEMBER-STATE-SPECIFIC] Key national competent authorities (Article 10, non-exhaustive):**

| Member State            | General Authority                                                                                | Sector-Specific Authorities                       |
| ----------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| **Germany [DE]**        | Federal Office of Justice (Bundesamt für Justiz)                                                 | BaFin (financial), Bundeskartellamt (competition) |
| **France [FR]**         | Agence Française Anticorruption (AFA)                                                            | AMF (financial markets), ACPR (banking)           |
| **Netherlands [NL]**    | House for Whistleblowers (Huis voor Klokkenluiders)                                              | AFM (financial), De Nederlandsche Bank            |
| **Ireland [IE]**        | Office of Protected Disclosures Commissioner                                                     | CBI (financial), CPPA (competition)               |
| **Spain [ES]**          | Independent Authority for Whistleblower Protection (pending)                                     | CNMV (financial), CNMC (competition)              |
| **Italy [IT]**          | ANAC (Anti-Corruption Authority)                                                                 | Consob (financial), Banca d'Italia                |
| **Belgium [BE]**        | Federal coordinator (sector-specific)                                                            | FSMA (financial), NBB (banking)                   |
| **Denmark [DK]**        | Data Protection Agency (for DPA matters); sector-specific bodies                                 | Finanstilsynet (financial)                        |
| **Sweden [SE]**         | Swedish Work Environment Authority; sector-specific                                              | Finansinspektionen (financial)                    |
| **Poland [PL]**         | Rzecznik Praw Obywatelskich (Ombudsman) + sector bodies                                          | KNF (financial), UOKiK (competition)              |
| **Austria [AT]**        | BAB (Federal Anti-Corruption Bureau); sector bodies                                              | FMA (financial)                                   |
| **Czech Republic [CZ]** | Ministry of Justice; sector bodies                                                               | CNB (financial)                                   |
| **EU Level**            | OLAF (EU fraud), ECA (audit), ECB (banking), ESMA (securities), EIOPA (insurance), EBA (banking) | Various                                           |

**[VERIFY] — This list reflects implementation as of early 2026. Verify current authority designations via national official gazettes or EUR-Lex national transposition tracking before advising.**

#### 7.2 Public Disclosure (Article 15)

Protected public disclosure (e.g., to journalists, media, civil society) is permitted without
prior internal or external reporting when **any one** of the following conditions is met:

| Condition                               | Test                                                                                                                 |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **A — Prior reporting failed**          | Internal + external channel used but no adequate action taken within 3 months                                        |
| **B — External channel not acted upon** | Reported externally but no feedback within 3 months from competent authority                                         |
| **C — Imminent or manifest danger**     | Reasonable grounds to believe irreversible damage, physical harm, or public emergency                                |
| **D — Risk of cover-up/retaliation**    | Reasonable grounds to believe reporting internally or externally poses retaliation risk or evidence destruction risk |

**Journalistic source protection (Recitals 74–76):**
Journalists and media outlets reporting on whistleblower disclosures receive source protection.
Public disclosure through journalism is within scope of protected disclosure.

---

## Compliance Classification Framework

Classify each assessed element using the three-tier system below.

### COMPLIANT — No Action Required

The organisation's implementation meets or exceeds the Directive's requirements for this
element. Minor procedural refinements may be noted but do not require remediation.

**Examples:**

- Dedicated, encrypted online reporting portal with documented access controls
- Written 7-day acknowledgment policy with automated confirmation tested and operational
- Anti-retaliation policy explicitly listing all 17 Article 19 prohibited measures

**Action:** Document as compliant in audit output. Flag for re-verification at next annual review.

### PARTIAL — Remediation Required

The organisation has begun implementing this element but material gaps exist. Compliance
risk is present. Remediation is required within a defined timeframe.

**Examples:**

- Internal channel exists but only written (no oral channel — violates Article 8 requirement)
- Anti-retaliation policy exists but does not cover facilitators or third persons
- 7-day acknowledgment implemented but 3-month feedback mechanism absent
- Investigator designated but no conflict-of-interest screening documented

**Action:** Generate specific remediation steps with a recommended timeline (see Output
Format below). Classify urgency as Critical, High, or Standard per the Prioritization
Framework.

### NON-COMPLIANT — Immediate Action Required

This element is entirely absent or materially contrary to a mandatory Directive requirement.
The organisation faces direct legal exposure — fines, infringement action, or private
liability for retaliation.

**Examples:**

- No internal reporting channel in place for an entity with 250+ employees (two years past
  the compliance deadline)
- Whistleblower identity disclosed to the accused during investigation
- Termination of a reporter without documented business justification (triggers reversal
  presumption)
- No acknowledgment or feedback procedures of any kind

**Action:** Escalate immediately. Generate remediation with specific urgency timeline.
Apply Self-Interrogation (below) to any NON-COMPLIANT classification before delivery.

---

## Prioritization Framework

Tier findings by implementation priority for the organisation's remediation plan.

### Critical (Legal Obligation — Non-Deferrable)

Must be remediated before the compliance deadline or immediately if already past deadline.
Direct penalties, fines, or private liability exposure exist.

- No internal channel for covered entities (Art. 8)
- No 7-day acknowledgment mechanism (Art. 9(1)(b))
- No 3-month feedback mechanism (Art. 9(1)(c))
- No designated impartial person/department (Art. 8(1))
- Whistleblower identity disclosed without lawful basis (Art. 16)
- Retaliatory action taken without documented justified grounds (Art. 19)
- No data processing lawful basis documented (GDPR Art. 6)

### High (Best Practice — Short-Term Remediation)

Required for robust compliance and risk mitigation. Should be remediated within 30–90 days.

- Anonymous reporting not supported (not mandatory under Directive but required by [NL];
  best practice universally)
- No DPIA conducted for whistleblower data processing
- Investigator conflict-of-interest screening not documented
- No interim relief mechanism documented for retaliation allegations
- Anti-retaliation policy not distributed or acknowledged by management
- External authority contacts not communicated to employees
- Shared channel used for entities with 250+ employees (violates Art. 8(6))

### Standard (Enhancement — Medium-Term Implementation)

Good governance measures that reduce risk and improve program quality. Implement within
90–180 days as resources permit.

- Multi-language support for reporting channels in all jurisdictions of operation
- Independent audit of the whistleblowing program by external advisor
- Reporter satisfaction feedback mechanism
- Annual transparency reporting on program metrics (anonymised)
- Training for managers on subtle forms of retaliation and burden-of-proof implications
- GDPR Article 23 restriction formally implemented in local policies [MEMBER-STATE-SPECIFIC]

---

## GDPR and Data Protection Integration

Processing whistleblower personal data requires GDPR compliance. Assess all five elements.

### 1. Lawful Basis (Article 6 GDPR)

**Primary basis:** Article 6(1)(c) — legal obligation (where national law mandates the channel)
**Secondary basis:** Article 6(1)(f) — legitimate interest (investigating internal misconduct)

Classify: Is the lawful basis documented in the organisation's Record of Processing Activities
(RoPA)? If not: **NON-COMPLIANT** (GDPR violation, separate from Directive obligations).

### 2. Data Protection Impact Assessment (DPIA — Article 35 GDPR)

A DPIA is required because whistleblower processing involves:

- Systematic monitoring of employees (criteria under GDPR Art. 35(3)(c))
- Processing of potentially criminal allegations (special category risk)
- Confidentiality / identity protection mechanisms (high risk to reporters)

Classify: DPIA conducted and documented? If not: **PARTIAL** at minimum — must be remediated.

### 3. Data Minimisation and Retention (Articles 5(1)(c) and (e) GDPR)

- Collect only data strictly necessary for the investigation
- Do not retain unverified allegations beyond the investigation's conclusion unless legally required
- Retention periods vary by Member State: typically 2–5 years [MEMBER-STATE-SPECIFIC]
- Implement scheduled deletion with documented evidence of deletion

### 4. Article 23 GDPR — Restricting Data Subject Rights to Protect Reporter

Member States may restrict data subject rights (access, rectification, erasure) where
necessary to protect whistleblower identity. Key points:

- A Subject Access Request (SAR) from the accused must not result in disclosure of the
  reporter's identity — apply the Art. 23 restriction (where enacted nationally) or
  exercise the third-party rights balance (where restriction not yet enacted)
- Document the basis for withholding in the SAR response log
- [MEMBER-STATE-SPECIFIC] Verify whether the applicable Member State enacted Article 23
  restrictions in its transposing law [DE][FR][NL][IE] — absent explicit restriction,
  seek legal advice before responding to SARs about whistleblower reports

### 5. Third-Party Processor Agreements (Article 28 GDPR)

Where using a third-party reporting channel platform:

- A GDPR Article 28 data processing agreement must be in place
- Processor must implement security measures per Article 32 (encryption, access controls,
  breach notification)
- Data localisation: processor must store data within EU or use approved transfer mechanisms
- Audit rights: organisation must retain the right to audit the processor's compliance

---

## Citation Quality Gates

Run these five gates silently before delivering any output. Revise if any gate fails.

| Gate           | Rule                                                                                                                         | Fail Action                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Source**     | Every legal claim cites a specific Directive article, national statute section, or established principle                     | Add citation or mark "[UNVERIFIED]"      |
| **Format**     | Citations reference Directive 2019/1937 with article numbers, and national laws with their official citation                 | Fix format                               |
| **Currency**   | National transposition laws verified as current — post May 2024 (all MS enacted); Commission July 2024 assessment considered | Flag "[CHECK CURRENCY]"                  |
| **Domain**     | Analysis stays within EU law scope; does not bleed non-EU regimes without explicit labeling                                  | Remove or re-label                       |
| **Confidence** | Uncertainty — especially on national transposition variations — explicitly stated                                            | Add confidence qualifier or [VERIFY] tag |

---

## Self-Interrogation for NON-COMPLIANT Classifications

For any NON-COMPLIANT finding, apply this three-pass review before delivery.

**Pass 1 — Legal Chain Integrity:**
Does the non-compliance finding follow directly from the Directive text? Cite the specific
article. Would a national competent authority or court actually find a violation on these
facts? Consider whether a defence or exception applies (e.g., de minimis, transitional
period, lex specialis).

**Pass 2 — Completeness:**
Have all relevant articles, recitals, and national implementing provisions been considered?
Is there sector-specific guidance (EBA, ESMA, OLAF) that bears on this finding? Are there
interim relief or cure opportunities the organisation could exercise?

**Pass 3 — Challenge:**
What is the strongest argument against this classification? Could the organisation plausibly
argue compliance through an alternative reading? Under what circumstances might a regulator
or court reach a different conclusion? State the contra-argument and why the NON-COMPLIANT
classification still stands despite it.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                             | Action                                              |
| ------------ | --------- | ------------------------------------------------------------------- | --------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear Directive text or settled national law                        | State finding with full confidence                  |
| **High**     | 0.80–0.94 | Strong authority; minor open questions of national implementation   | State with brief caveat                             |
| **Probable** | 0.60–0.79 | Good arguments; national transposition unclear or in flux           | State with reasoning and note contra-indicators     |
| **Possible** | 0.40–0.59 | Genuinely uncertain; national law gap or conflicting implementation | Flag for qualified legal review; present both sides |
| **Unlikely** | 0.0–0.39  | Speculative; weak legal basis                                       | Do not assert; flag "[UNCERTAIN]"                   |

---

## Deep Topic Analysis: Key Compliance Elements

### Topic 1: Multinational Group Channel Architecture

**Common compliance failure:** Treating a centralised group channel as compliant for all
subsidiaries, when each legal entity with 50+ employees requires its own compliant channel.

**Analysis framework:**

1. Map each legal entity with 50+ employees in EU Member States
2. For entities with 250+ employees: each requires a **dedicated** channel (no sharing)
3. For entities with 50–249 employees: sharing is permitted between entities in this tier
4. The shared channel must be **operationally separate** — impartial handler for each entity,
   no cross-contamination of reports, confidentiality maintained per entity
5. Cross-border data flows within group: assess transfer mechanism (intra-group transfer is not
   automatically GDPR-compliant; an intra-group data transfer agreement or BCRs may be required)

**Language requirement [MEMBER-STATE-SPECIFIC]:**
Employees must be able to report in a language they understand. For multinational groups,
the channel should support all languages of jurisdictions where the entity operates.
[VERIFY local requirements — some Member States specify language obligations in transposing law]

### Topic 2: Retaliation Detection and Monitoring

**Framework for ongoing retaliation monitoring:**
After a report is filed, implement monitoring for 12–24 months:

- Flag any adverse employment action affecting the reporter (termination, suspension,
  demotion, transfer, performance review) for review before execution
- Require sign-off from compliance/legal before adverse action proceeds against a recent reporter
- Document that the decision would have been made regardless of the reporting (compare
  to similarly situated non-reporting employees)
- If retaliation is suspected: apply interim relief immediately (suspend the adverse action
  pending investigation)

### Topic 3: GDPR Subject Access Requests During Investigations

**Scenario:** Accused person submits a GDPR Subject Access Request seeking all data about them.

**Analysis:**

1. Right of access under GDPR Article 15 is not absolute — must be balanced against third-party
   rights (reporter's identity)
2. Provide access to information about the accused's own data that does not reveal the reporter
3. Withhold or redact information that would directly or indirectly identify the reporter
4. [MEMBER-STATE-SPECIFIC] If national law implements GDPR Article 23 restriction, invoke it
   explicitly and document the decision
5. Maintain an access request log showing what was provided and what was withheld (and why)
6. Do not delay the SAR response beyond the 1-month statutory deadline — respond with
   the partial disclosure and an explanation for any withheld information

### Topic 4: Interaction with Sector-Specific Rules (Financial Services)

**For organisations subject to MAR, MiFID II, or CRD V:**

1. Determine whether the sectoral rule provides "at least equivalent" protection — if yes,
   the sectoral framework takes precedence (Directive Art. 3(1))
2. Map the sectoral channel's coverage against the Directive's scope — the Directive's
   anti-retaliation protections still apply to the extent not covered by the sectoral rule
3. Practically: maintain sector-specific channels (e.g., FCA SYSC 18.6 channel for UK/EEA
   investment firms) **and** a Directive-compliant general channel, unless the sectoral channel
   meets all Directive requirements
4. ESMA Q&As and EBA guidelines provide additional sector-specific guidance [VERIFY current version]

### Topic 5: False/Malicious Reports and Abuse of the System (Article 24)

**Member States must provide effective, proportionate, dissuasive penalties for knowingly
false reports.** Key points:

- **Knowledge of falsity required** — honest mistakes are protected (Recital 51)
- **High bar for employer:** Must prove the reporter knew the report was false (recklessness
  insufficient in most implementations — [VERIFY nationally])
- **No chilling effect:** Sanctions for abuse must not deter legitimate reporting — the
  threshold for invoking Article 24 should be genuinely high
- **Employer cannot simply allege abuse** to escape Article 19 retaliation prohibition —
  the retaliation prohibition applies unless and until the report is proven knowingly false

---

## Anti-Patterns

Catalogue of what **not** to do when implementing EU Whistleblower Directive compliance:

1. **Implementing channels without independence protocols** — Designating the HR director
   or the CFO's direct report as the sole handler without conflict-of-interest screening.
   Violates the impartiality requirement (Art. 9, Recital 56).

2. **Treating a group intranet "contact us" form as a compliant reporting channel** —
   These typically lack encryption, access controls, and anonymity features required for
   GDPR compliance and Directive confidentiality obligations.

3. **Delaying acknowledgment beyond 7 days** — The 7-day timeline is non-negotiable.
   Automated acknowledgment systems should be tested before go-live.

4. **3-month feedback that says nothing substantive** — Sending a form letter that says
   only "your report is under review" does not meet the Article 9(1)(c) obligation to
   inform the reporter of "actions taken or envisaged."

5. **Applying Article 24's false report sanction too readily** — Using the malicious
   reporting sanction as a de facto retaliation tool against reporters who raised concerns
   that were ultimately unsubstantiated. Honest mistakes are not malicious reports.

6. **Centralising channels for 250+ employee entities** — Entities with 250+ employees
   must have dedicated channels. Sharing with the group-level channel violates Art. 8(6).

7. **Ignoring national transpositions that exceed the Directive** — Implementing only the
   Directive minimum without checking the national implementing law. Germany, France, and
   Netherlands each extend scope or protections beyond the Directive floor.

8. **Failing to update the Entity Map when the organisation restructures** — M&A, TUPE
   transfers, and group reorganisations change which entities cross the 50-employee threshold.
   Compliance mapping must be event-triggered, not just annual.

9. **Processing reporter data without a GDPR lawful basis** — Particularly where the
   channel accepts reports anonymously; the processing of any identifiable data of the
   accused or witnesses must have its own documented lawful basis.

10. **Disclosing reporter identity in response to a GDPR SAR from the accused** — This
    violates Art. 16 of the Directive and may constitute retaliation. Seek legal advice
    before responding to any SAR touching on a live whistleblower investigation.

11. **Terminating a reporter without a documented business justification prepared before
    the decision** — Under Art. 19's burden reversal, retrospective justifications are
    insufficient. The employer must prove the decision was made on grounds unrelated to
    the report; contemporaneous documentation is critical.

12. **Not telling employees the external reporting authority exists** — Employees have a
    right to go directly to the competent authority. Omitting this information from the
    internal policy (to funnel all reports through internal channels) violates the
    Directive's principle of free choice of reporting channel.

13. **Ignoring the protection of facilitators and third persons** — Not extending
    anti-retaliation protection to persons who assist reporters, or to their family members
    and colleagues. Article 4(4) protection for these persons is mandatory.

14. **Using the same person to handle all reports regardless of subject matter** — If the
    designated handler is the subject of a report, or is in the reporting line of the accused,
    the handler must recuse. Failure to maintain a secondary handler leaves the organisation
    with no compliant channel for that report.

15. **Storing whistleblower reports in shared drives or unencrypted email folders** —
    Violates both the Directive's confidentiality obligations (Art. 16) and GDPR security
    requirements (Art. 32). Reports must be stored in access-controlled, encrypted systems
    with audit logging.

16. **Conflating internal investigation outcomes with reporter protection** — Even if an
    investigation concludes no breach occurred, the reporter retains full anti-retaliation
    protection provided the report was made with reasonable grounds. "We investigated and
    found nothing" is not a basis for adverse action.

17. **Assuming the Directive does not apply because the entity is below 50 employees** —
    The mandatory channel obligation does not apply; the anti-retaliation obligations apply
    to all employers regardless of size. If a reporter at a sub-threshold entity is
    retaliated against for reporting to an external authority, the Art. 19 prohibition applies.

18. **Neglecting DPIA obligations** — Whistleblower processing carries high GDPR risk
    (sensitive allegations, identity protection requirements, special access restrictions).
    DPIA is required under Art. 35 GDPR and should be updated when the channel design changes.

19. **Operating a channel in only one language for a multilingual workforce** — Where the
    organisation operates across multiple Member States, reporters must be able to report
    in a language they understand. Single-language channels effectively exclude workers.

20. **No post-investigation retaliation monitoring** — Retaliation often occurs months after
    a report, not immediately. Without ongoing monitoring of employment decisions affecting
    reporters, subtle retaliation (denied promotion, delayed salary review, unfavourable
    reassignment) goes undetected until litigation is filed.

---

## Writing Standards

Apply these standards before delivering any output under this skill.

1. **Cite specifically**: Every compliance finding must cite the applicable article number
   (e.g., "Art. 9(1)(b) of Directive 2019/1937") or national provision (e.g., "§ 17(3)
   HinSchG [DE]"). Vague citations like "under the Directive" are insufficient.

2. **Classify every finding**: Every identified gap must carry a classification
   (COMPLIANT / PARTIAL / NON-COMPLIANT) and a priority tier (Critical / High / Standard).
   Unclassified findings reduce the output's utility.

3. **[MEMBER-STATE-SPECIFIC] markers are non-negotiable**: Any statement that varies by
   Member State must be flagged. Do not state national law positions as universal.

4. **Plain-language compliance summaries**: Produce a plain-language executive summary
   alongside the technical legal analysis. Legal teams need the detail; business sponsors
   need the summary.

5. **Actionable remediation steps**: Every PARTIAL or NON-COMPLIANT finding must end with
   specific, numbered remediation steps — not "consider addressing this gap."

6. **Confidence scoring on uncertain items**: Where national transposition is unclear, in
   flux, or varies across Member States, apply the confidence scoring scale and state the
   basis for uncertainty.

7. **Do not fabricate authority names or statutory citations**: If a competent authority
   designation or statutory reference cannot be verified, mark [VERIFY] and direct the
   user to the national transposition tracker on EUR-Lex.

---

## External Tool Integration — legalcode-mcp

**With legalcode-mcp connected (preferred):**

Use legalcode-mcp to search for:

- Current text of Directive 2019/1937 and Consolidated versions
- National implementing legislation for each relevant Member State
- CJEU infringement decisions and penalty orders
- Commission compliance reports (especially July 2024 assessment)
- EBA/ESMA/FCA guidance notes on sector-specific whistleblowing
- Recent national case law on burden-of-proof reversal and retaliation findings

Save results to `/tmp/legalcode-whistleblower-research.md` structured as:

```markdown
# Legal Authority — EU Whistleblower Directive

## Date: [date]

## Member States in scope: [list]

### Directive Text (Verified)

- [Article, text or summary, EUR-Lex reference]

### National Transpositions

- [Country, statute name, official citation, effective date, key variations]

### CJEU Decisions

- [Case, citation, key finding]

### Commission Reports

- [Title, date, key finding]

### Sector-Specific Guidance

- [Regulator, title, date, relevance]
```

Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**

- Proceed with analysis using general legal knowledge
- Mark all statutory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Direct users to EUR-Lex (eur-lex.europa.eu) and national official gazettes for verification

---

## Glass Box Audit Trail

Include this YAML block at the end of every output produced by this skill:

```yaml
glass_box:
  skill_name: "legalcode-eu-whistleblower-directive"
  mode: "[Build / Audit / Advise]"
  organisation_type: "[Private / Public / Mixed]"
  member_states_in_scope: "[list]"
  sectors_assessed: "[list]"
  entities_assessed: "[number]"
  threshold_entities: "[number above 50 employees]"
  legalcode_mcp: "[Connected / Not connected — manual verification required]"
  research_reference_file: "[path or 'Not created']"
  compliance_findings:
    compliant: "[number]"
    partial: "[number]"
    non_compliant: "[number]"
  priority_findings:
    critical: "[number]"
    high: "[number]"
    standard: "[number]"
  quality_score: "[X]/40"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations — Member States not assessed, sectors excluded, etc.]"
    - "[Reliance on national transposition as understood at date of assessment]"
    - "[Any areas of genuine legal uncertainty flagged]"
  reviewer: "AI-assisted — requires qualified legal review in each applicable Member State"
  assessment_date: "[date]"
```

---

## Output Format Template

Produce all formal outputs using this template. Adapt sections for the applicable mode.

---

```markdown
# EU Whistleblower Directive Compliance [Audit / Assessment / Advisory]

**Organisation:** [name]
**Date:** [date]
**Scope:** [Member States, entities, sectors]
**Mode:** [Build / Audit / Advise]

---

## Executive Summary

[2–4 sentence plain-language summary of overall compliance posture, critical findings,
and recommended immediate actions. Designed for C-suite or board-level readers.]

**Overall Compliance Status:** [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Critical Findings:** [N]
**High Priority Findings:** [N]
**Standard Findings:** [N]

---

## Entity Threshold Map

| Entity | Jurisdiction | Headcount | Channel Required | Channel Type          | Status   |
| ------ | ------------ | --------- | ---------------- | --------------------- | -------- |
| [Name] | [MS]         | [N]       | Yes/No           | Dedicated/Shared/None | [C/P/NC] |

---

## Compliance Findings

### [CRITICAL] [Finding Title]

**Provision:** [Directive Art. X / National Law Section Y]
**Classification:** NON-COMPLIANT
**Priority:** Critical
**Current State:** [What exists today]
**Gap:** [What is missing or inadequate]
**Remediation:**

1. [Specific step 1]
2. [Specific step 2]
3. [Specific step 3]
   **Deadline:** [Immediate / 30 days / 60 days / 90 days]
   **Confidence:** [Level — rationale]

### [HIGH] [Finding Title]

[Same structure]

### [STANDARD] [Finding Title]

[Same structure]

---

## Reportable Breach Scope Assessment

| Category   | Directive Coverage | National Extension | Gap Identified         |
| ---------- | ------------------ | ------------------ | ---------------------- |
| [Category] | Yes/No             | [MS: Yes/No]       | [Yes/No — description] |

---

## Protected Persons Assessment

| Category   | Directive Coverage | National Coverage | Gap      |
| ---------- | ------------------ | ----------------- | -------- |
| [Category] | Yes/No             | [MS: Yes/No]      | [Yes/No] |

---

## Internal Reporting Channel Assessment

| Element                   | Requirement          | Current State | Classification | Priority        |
| ------------------------- | -------------------- | ------------- | -------------- | --------------- |
| Written channel           | Yes (Art. 8)         | [State]       | [C/P/NC]       | [Crit/High/Std] |
| Oral channel              | Yes (Art. 8)         | [State]       | [C/P/NC]       | [Crit/High/Std] |
| 7-day acknowledgment      | Yes (Art. 9(1)(b))   | [State]       | [C/P/NC]       | [Crit/High/Std] |
| 3-month feedback          | Yes (Art. 9(1)(c))   | [State]       | [C/P/NC]       | [Crit/High/Std] |
| Investigator independence | Yes (Art. 9/Rec 56)  | [State]       | [C/P/NC]       | [Crit/High/Std] |
| Confidentiality controls  | Yes (Art. 16)        | [State]       | [C/P/NC]       | [Crit/High/Std] |
| GDPR compliance           | Yes (GDPR + Art. 16) | [State]       | [C/P/NC]       | [Crit/High/Std] |

---

## Anti-Retaliation Framework Assessment

| Element                                         | Requirement     | Current State | Classification | Priority   |
| ----------------------------------------------- | --------------- | ------------- | -------------- | ---------- |
| Article 19 prohibited measures documented       | Yes             | [State]       | [C/P/NC]       | [Priority] |
| Burden-of-proof reversal acknowledged in policy | Yes             | [State]       | [C/P/NC]       | [Priority] |
| Interim relief mechanism                        | Yes (Art. 21)   | [State]       | [C/P/NC]       | [Priority] |
| Facilitator/third person protection             | Yes (Art. 4(4)) | [State]       | [C/P/NC]       | [Priority] |
| Post-report retaliation monitoring              | Best practice   | [State]       | [C/P/NC]       | [Priority] |

---

## GDPR Integration Assessment

| Element                              | Requirement       | Status   | Gap   |
| ------------------------------------ | ----------------- | -------- | ----- |
| Lawful basis documented in RoPA      | GDPR Art. 6       | [Status] | [Gap] |
| DPIA conducted                       | GDPR Art. 35      | [Status] | [Gap] |
| Data minimisation policy             | GDPR Art. 5(1)(c) | [Status] | [Gap] |
| Retention schedule defined           | GDPR Art. 5(1)(e) | [Status] | [Gap] |
| Art. 23 GDPR restriction implemented | [MS-specific]     | [Status] | [Gap] |
| Art. 28 processor agreement          | GDPR Art. 28      | [Status] | [Gap] |

---

## Prioritised Remediation Roadmap

### Immediate (Do Now)

1. [Action] — [Owner] — [Deadline]

### 30 Days

1. [Action] — [Owner] — [Deadline]

### 60–90 Days

1. [Action] — [Owner] — [Deadline]

### Ongoing

1. [Action] — [Frequency / Trigger]

---

## Localization Notes by Member State

### [Member State] — [National Transposition Law]

- **Scope:** [Extensions or gaps vs. Directive floor]
- **Protected persons:** [Extensions or gaps]
- **Key variations:** [Notable differences]
- **Competent authority:** [Name]
- **Sanctions:** [Fine levels]
- **[VERIFY]:** [Items requiring local legal verification]

---

## Recommended Next Steps

1. [Immediate priority — who does what by when]
2. [External legal review recommended for: [specific topics or MS]]
3. [Annual compliance review cadence]

---

[Glass Box YAML block here]
```

---

## Localization Notes

### National Transposition Quick-Reference

| Member State            | Law                                        | In Force                                 | Scope vs. Directive                                        | Notable Features                                                        |
| ----------------------- | ------------------------------------------ | ---------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Germany [DE]**        | Hinweisgeberschutzgesetz (HinSchG)         | 2 July 2023                              | Wider (criminal + admin law violations)                    | Bundesamt für Justiz as external authority; fines up to €50,000         |
| **France [FR]**         | Loi n° 2022-401                            | 1 Sept 2022                              | Wider (French law violations; general interest threats)    | Built on Sapin II; AFA as external authority; no escalation requirement |
| **Netherlands [NL]**    | Wet Bescherming Klokkenluiders             | 18 Feb 2023 (250+); 17 Dec 2023 (50-249) | Directive floor + anonymous reporting obligation (pending) | Huis voor Klokkenluiders                                                |
| **Ireland [IE]**        | Protected Disclosures (Amendment) Act 2022 | 1 Jan 2023                               | Directive floor                                            | Office of Protected Disclosures Commissioner (Ombudsman)                |
| **Spain [ES]**          | Ley 2/2023                                 | 13 March 2023                            | Directive floor                                            | Replaces regional fragmentation; national authority                     |
| **Italy [IT]**          | D.Lgs. 24/2023                             | 9 March 2023                             | Narrowed (Commission noted gaps)                           | ANAC as authority; scope limitations flagged                            |
| **Belgium [BE]**        | Multiple implementing acts                 | 2022-2023                                | Directive floor                                            | Sector-fragmented approach                                              |
| **Denmark [DK]**        | Lov om beskyttelse af whistleblowere       | June 2021                                | Directive floor                                            | First implementer in EU                                                 |
| **Sweden [SE]**         | Visselblåsarlagen (2021:890)               | Sept 2021                                | Directive floor                                            | Second implementer in EU                                                |
| **Poland [PL]**         | Ustawa o ochronie sygnalistów              | July 2024                                | Narrowed (Commission noted gaps)                           | Late implementation; scope limitations persist                          |
| **Austria [AT]**        | HinweisgeberInnenschutzgesetz              | March 2023                               | Directive floor                                            | BAB as authority                                                        |
| **Czech Republic [CZ]** | Zákon o ochraně oznamovatelů               | 1 Aug 2023                               | Directive floor                                            | Ministry of Justice authority                                           |
| **Hungary [HU]**        | Various                                    | 2023                                     | Significantly narrowed                                     | Commission identified major gaps — do not assume compliance             |
| **Romania [RO]**        | Various                                    | 2023                                     | Narrowed                                                   | Commission identified scope gaps                                        |
| **Bulgaria [BG]**       | Various                                    | 2023                                     | Narrowed                                                   | Commission identified restricted coverage                               |
| **Greece [GR]**         | Various                                    | 2023                                     | Narrowed                                                   | Commission identified inadequate scope                                  |

**[VERIFY] all entries against current national official sources — transpositions continue to be amended as Commission infringement pressure continues.**

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Directive (EU) 2019/1937 full text (EUR-Lex)
- European Commission compliance assessment report, July 2024
- CJEU infringement proceedings and penalty decisions (2023-2024)
- National transposing laws for Germany (HinSchG), France (Loi 2022-401), Netherlands
  (Wet BK), Ireland (PDA 2022), Spain (Ley 2/2023), Italy (D.Lgs. 24/2023), Denmark,
  Sweden, Poland, Austria, Czech Republic
- OneTrust, NAVEX Global, Bird & Bird, DLA Piper, Clifford Chance, Baker McKenzie,
  Covington & Burling, Seyfarth Shaw, Morrison Foerster, Reed Smith, Skadden practice
  guidance (2021–2025)
- Transparency International EU whistleblower assessment (2024)
- Integrityline, Resolver, Mitratech compliance implementation guides
- National Whistleblower Center resource library

Legalcode original synthesis. Not imported from any external skill source.
