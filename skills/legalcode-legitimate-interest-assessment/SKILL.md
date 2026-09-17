---
name: legalcode-legitimate-interest-assessment
description: Conduct a three-part Legitimate Interest Assessment (LIA) under GDPR Art. 6(1)(f), UK GDPR,
  and Swiss FADP (nDSG). Use when evaluating whether a controller's legitimate interest can lawfully ground
  processing under the Purpose test (is the interest lawful, clearly articulated, real and present?),
  the Necessity test (is processing strictly necessary and proportionate?), and the Balancing test (do
  controller interests outweigh data subject rights?). Also use when documenting LIA records for supervisory
  authority review, assessing direct marketing, fraud prevention, employee monitoring, profiling, intra-group
  transfers, network security, or any other processing relying on Art. 6(1)(f). Covers UK Recognised Legitimate
  Interests (DUA Act 2025) and Swiss Art. 31(1)(b) FADP overriding private interest. Produces a structured,
  auditable LIA documentation package with GREEN/YELLOW/RED per-test classification, APPROVED/CONDITIONAL/REJECTED
  overall outcome, remediation plan, and Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Legitimate Interest Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted Legitimate Interest
> Assessment under GDPR Art. 6(1)(f), UK GDPR, and Swiss FADP. It does not constitute
> legal advice. All outputs must be reviewed by a qualified privacy counsel or Data
> Protection Officer licensed or operating in the relevant jurisdiction before any reliance
> or action. Laws, regulatory guidance, adequacy decisions, and enforcement posture change —
> verify currency before relying on any legal conclusion. Statutory, case law, and
> regulatory references cited from training data carry hallucination risk — verify against
> authoritative sources before use. Mark any unverified citation **[VERIFY]**.

---

## Purpose and Scope

This skill conducts a complete, structured Legitimate Interest Assessment for any
proposed processing activity relying on Art. 6(1)(f) GDPR as its lawful basis.

**This skill covers:**

- The three-part LIA test — Purpose, Necessity, and Balancing — applied sequentially
- Classification of each test component (GREEN / YELLOW / RED) and overall outcome
  (APPROVED / CONDITIONAL / REJECTED)
- UK GDPR parallel analysis including Recognised Legitimate Interests (Data (Use and
  Access) Act 2025, Schedule 4/Annex 1)
- Swiss FADP/nDSG Art. 31(1)(b) overriding private or public interest justification
- Legitimate interest taxonomy — which categories of interest pass the purpose test
- Necessity stress-testing — minimum data, minimum means, minimum retention
- Balancing matrix — four EDPB-aligned factors (rights/freedoms, impact, expectations,
  safeguards)
- Safeguards catalogue — measures that can tip the balance in the controller's favour
- Alternative lawful basis assessment — if LIA fails, identify viable fallback
- Remediation plan for CONDITIONAL outcomes
- Auditable LIA record suitable for supervisory authority review and data subject requests
- ROPA update guidance (Art. 30) and privacy notice disclosure requirements (Arts. 13/14)
- DPIA trigger assessment — when a positive LIA also requires a DPIA

**This skill does not:**

- Provide legal advice or replace qualified privacy counsel
- Guarantee regulatory approval or protect against enforcement action
- Cover special-category processing under Art. 9 independently — Art. 9 requires a
  separate condition alongside Art. 6(1)(f); this skill flags the Art. 9 intersection
  but does not perform a full Art. 9 analysis
- Draft SCCs, DPAs, or other data transfer instruments — see `legalcode-cross-border-transfer-assessment`
- Conduct a full DPIA — see `legalcode-dpia-generator`
- Apply to non-GDPR regimes (CCPA, LGPD, PIPA, PDPA) — see jurisdiction-specific skills

**Complementary skills:**

- `legalcode-dpia-generator` — required when LIA identifies high risk to data subjects
- `legalcode-cross-border-transfer-assessment` — where Art. 6(1)(f) processing involves
  cross-border transfers under Chapter V
- `legalcode-dsar-workflow-builder` — for operationalising Art. 21 right to object
- `legalcode-privacy-policy-drafter` — for transparency obligations under Arts. 13/14

---

## Jurisdiction and Governing Law

This skill operates across three parallel regimes that share GDPR Art. 6(1)(f) as
their common origin but diverge in case law, guidance, and legislative development.

| Regime         | Primary Instrument                                                         | Supervisory Authority | Key Guidance                                                        |
| -------------- | -------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------- |
| **EU GDPR**    | Regulation (EU) 2016/679, Art. 6(1)(f)                                     | Lead SA + EDPB        | EDPB Guidelines 1/2024 (adopted 8 Oct 2024)                         |
| **UK GDPR**    | UK GDPR (retained) + Data (Use and Access) Act 2025                        | ICO                   | ICO Legitimate Interests Guidance (under review post-DUA 2025)      |
| **Swiss FADP** | Federal Act on Data Protection (nDSG), effective 1 Sep 2023, Art. 31(1)(b) | FDPIC                 | FDPIC guidance [VERIFY — comprehensive guidance pending as of 2026] |

**Primary legal authority (EU GDPR):**

- Art. 6(1)(f) — The lawful basis itself: "necessary for the purposes of the legitimate
  interests pursued by the controller or by a third party, except where such interests
  are overridden by the interests or fundamental rights and freedoms of the data subject"
- Arts. 5(1)(a)(b)(c)(e) — Lawfulness, purpose limitation, data minimisation, storage limitation
- Art. 5(2) — Accountability: ability to demonstrate compliance
- Arts. 13(1)(d) and 14(2)(b) — Transparency: must disclose legitimate interests in privacy notices
- Art. 21 — Right to object: Art. 21(1) general right (Art. 6(1)(f) grounds); Art. 21(2)
  absolute right to object to direct marketing; controller must show "compelling legitimate
  grounds" to override an Art. 21(1) objection per EDPB Guidelines 1/2024
- Art. 22 — Automated decision-making: Art. 6(1)(f) cannot ground solely automated
  decisions producing legal or similarly significant effects
- Art. 30 — ROPA: must record the lawful basis
- Art. 35 — DPIA: required when LIA identifies high risk to data subjects' rights

**Key recitals:**

- Recital 47 — Direct marketing as legitimate interest; controller-subject relationship;
  reasonable expectations; "or by a third party"
- Recital 48 — Intra-group administrative transfers as legitimate interest (not a blank check)
- Recital 49 — Network and information security
- Recital 50 — Fraud prevention, criminal acts, threats to public security

**Key case law:**

- CJEU C-621/22 (KNLTB, 4 October 2024) — Commercial interests can constitute legitimate
  interests; categorical exclusion of commercial interests is too strict; balancing test
  remains the critical hurdle
- CJEU C-446/21 (Schrems v Meta, 4 October 2024) — Data minimisation (Art. 5(1)(c))
  prohibits unlimited data aggregation for targeted advertising; no legitimate interest
  overrides data subjects' rights at that scale
- CJEU C-184/20 (OT v Vyriausioji tarnybinės etikos komisija, 2022) — Necessity test is
  strict; disclosure of special-category data as part of processing must be individually
  necessary, not merely incidental
- LinkedIn €310M fine (Irish DPC, 24 October 2024) — Art. 6(1)(f) reliance for
  behavioural advertising at scale found unlawful; users' interests overrode commercial interest
- Amazon France Logistique €32M fine (CNIL, December 2023) — Granular employee monitoring
  failed necessity and balancing tests; aggregated weekly data would have sufficed
- Experian (ICO enforcement 2020, Tribunal 2023) — Switching from consent to LI for
  same-purpose processing is not appropriate

[JURISDICTION-SPECIFIC] Before final output, localise:

- Mandatory sector-specific restrictions on Art. 6(1)(f) use (health, children, employment,
  financial services, telecommunications)
- National derogations or restrictions enacted under Art. 23 GDPR
- Supervisory authority enforcement posture and published decisions in the applicable jurisdiction
- UK-specific: Recognised Legitimate Interests (DUA Act 2025, Schedule 4/Annex 1) —
  no balancing test required for specified purposes; commencement regulations pending
- Swiss-specific: Employer monitoring governed partly by Art. 328b Swiss Code of Obligations;
  FDPIC guidance on Art. 31 FADP [VERIFY currency]

---

## Interactive Clarification

This skill uses **CLARIFY** prompts at decision points where the user's answer
materially changes the direction or outcome of the assessment. When marked **CLARIFY**,
pause and ask the user before proceeding. If the information is already available, skip
the prompt and proceed.

CLARIFY topics in this skill:

1. Jurisdiction (EU / UK / Swiss / all three)
2. Data subject categories (employees, consumers, general public, children, vulnerable)
3. Data categories (ordinary personal data vs. special category under Art. 9)
4. Processing type (direct marketing, fraud prevention, profiling, monitoring, etc.)
5. Risk tolerance (conservative/pragmatic approach to CONDITIONAL findings)
6. Whether a DPIA has already been conducted

---

## Workflow

### Step 1: Accept Input

Accept the processing activity description in any of these formats:

- **Free text description**: "We want to process [data] for [purpose] by [means]"
- **ROPA extract**: Existing record of processing from the organisation's Art. 30 register
- **Project brief or technical specification**: Product or feature documentation
- **Existing LIA document**: A prior LIA to reassess or update

If no description is provided, prompt the user to supply one. At minimum, collect:

- Processing purpose (what is the organisation trying to achieve?)
- Categories of data (what personal data is involved?)
- Data subjects (who does the data relate to?)
- Processing means (how is the data collected, used, shared, stored?)
- Retention period (how long will the data be kept?)

### Step 2: Gather Context

**CLARIFY** — Before beginning the LIA, ask the user these questions. Present them as
structured options where possible:

1. **Which jurisdiction(s) apply?**
   - Options: EU GDPR only, UK GDPR only, Swiss FADP only, EU + UK, EU + UK + Swiss, Other
   - _Why this matters_: The three regimes share the same three-part test structure but
     diverge significantly in guidance, case law, and legislative developments. UK GDPR
     now has Recognised Legitimate Interests (DUA Act 2025) which eliminates the balancing
     test for specific purposes. Swiss FADP uses a different doctrinal model (Art. 31 FADP
     overriding private interest).

2. **Who are the data subjects?**
   - Options: Employees/staff, Consumers/customers, General public, Children (under 18),
     Patients or health service users, People in financial difficulty, Multiple groups
   - _Why this matters_: Vulnerable data subjects (employees, children, patients, people
     in financial difficulty) attract heightened protection and shift the balancing test
     against the controller. Power imbalance in employer-employee relationships makes
     consent unreliable and LI more demanding to justify.

3. **What is the nature of the data?**
   - Options: Ordinary personal data, Special-category data (Art. 9 — racial/ethnic origin,
     political opinions, religious beliefs, trade union membership, health, sex life, biometric,
     genetic), Criminal offence data (Art. 10), Financial data, Location data, Children's data
   - _Why this matters_: Special-category and criminal offence data require separate legal
     conditions beyond Art. 6(1)(f). Any special-category data significantly increases the
     necessity and balancing burden. Financial and location data are high-sensitivity ordinary
     data requiring stronger justification.

4. **What type of processing is being assessed?**
   - Options: Direct marketing, Fraud prevention/detection, Network and information security,
     Employee monitoring/management, Profiling/analytics, Intra-group administrative transfer,
     Pursuing legal claims, Research or product improvement, Other commercial purpose
   - _Why this matters_: Determines which EDPB guidance, recitals, and case law apply
     directly; some categories have recognised treatment (Recitals 47-50) that establishes
     a baseline, while others (profiling, employee monitoring) carry heightened scrutiny.

5. **Risk tolerance / approach?**
   - Options: Conservative (prefer to flag CONDITIONAL outcomes and require explicit
     mitigations before proceeding), Pragmatic (accept CONDITIONAL outcomes with documented
     mitigations and proceed), Strict (any YELLOW requires escalation to legal counsel)
   - _Why this matters_: Affects how borderline balancing outcomes are classified and whether
     CONDITIONAL processing requires additional safeguards before reliance.

6. **Has a DPIA been conducted?**
   - Options: Yes — DPIA already completed, No — DPIA not yet conducted, No — DPIA
     trigger not assessed
   - _Why this matters_: If the LIA identifies high risk to data subjects' rights, a DPIA
     (Art. 35) is mandatory. A completed DPIA can substitute for the LIA since it covers
     the same ground in greater depth (ICO). Alerts the skill to recommend DPIA where needed.

### Step 3: Identify the Legitimate Interest (Purpose Test — Stage 1)

Apply the three sub-criteria from EDPB Guidelines 1/2024 to determine whether a legitimate
interest exists. This is the **gateway** stage — failure here terminates the assessment.

**3a. Articulate the interest**

Ask the user to state the specific interest the controller is pursuing. An interest must be:

- **Specific, not generic** ("prevent credit card fraud on our payment platform" not "security")
- **The controller's own interest or a third party's** — if third party, identify the connection
  to the controller's activities
- **Distinguishable from the processing itself** — the interest is a goal; the processing
  is the means

**3b. Apply the three sub-criteria**

| Sub-criterion                         | Test                                                                                                           | Failure indicator                                                                                                                        |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Lawful**                            | Is the interest not contrary to law? Does it not conflict with other GDPR provisions or sector-specific rules? | Purpose contrary to law; unlawful objective; purpose that violates other GDPR rules; public authority acting in official capacity        |
| **Clearly and precisely articulated** | Is the interest specific and concrete? Can it be written in one sentence without vague business-speak?         | Vague objectives ("analytics," "business improvement," "service enhancement"); multiple conflated purposes; undetermined future interest |
| **Real and present**                  | Does the interest exist now? Is it based on current facts, not speculation about future needs?                 | Hypothetical future interest; speculative benefit; interest that may arise if certain events occur                                       |

**3c. Third-party interests (Recital 47; EDPB Guidelines 1/2024)**

If relying on a third party's legitimate interest:

- Identify the third party and their specific interest
- Demonstrate the connection between the controller's activities and the third party's interest
- Apply the same three sub-criteria to the third party's interest
- Note: EDPB recognises four categories of third-party legitimate interest: (a) legal claims
  (establishment, exercise, or defence); (b) transparency and accountability disclosures;
  (c) scientific research; (d) general public interest

**3d. Purpose test classification**

- **GREEN**: Interest clearly identified, lawful, specific, real and present
- **YELLOW**: Interest stated but ambiguous, conflates multiple purposes, or requires
  clarification before proceeding
- **RED**: Interest not identified, unlawful, overly vague, speculative, or excluded by law

**CLARIFY** if Stage 1 classification is YELLOW: Present the ambiguity to the user and
ask for clarification before proceeding to the necessity test. A vague purpose cannot be
stress-tested for necessity.

**Stage 1 gate:** If Stage 1 is RED → LIA assessment terminates. Recommend alternative
lawful basis. Proceed to Step 9.

### Step 4: Test Necessity and Proportionality (Necessity Test — Stage 2)

The necessity test requires that processing be **strictly necessary** (not merely useful,
helpful, or convenient) to achieve the identified legitimate interest. Apply three
stress-questions:

**4a. Does processing achieve the purpose?**

Does the specific processing activity have a direct, causal connection to the identified
legitimate interest? Marginal or indirect contribution fails the necessity test.

**4b. Are there less intrusive alternatives?**

Actively examine alternatives. The controller bears the burden of demonstrating that no
less intrusive means would be equally effective. Consider:

- Could the same interest be achieved with fewer data categories?
- Could pseudonymisation or anonymisation serve the same purpose?
- Could aggregated rather than individual-level data suffice?
- Could the same purpose be achieved with a shorter retention period?
- Could the same interest be achieved with a less privacy-invasive processing method?

If any realistic less intrusive alternative exists and the controller has not explained
why it was rejected, the necessity test is at risk.

**4c. Data minimisation stress-test**

| Dimension            | Question                                                                                              | Red flag                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Data volume**      | Are only data categories strictly necessary to achieve the purpose included?                          | Collecting "nice to have" data categories alongside necessary ones           |
| **Processing scope** | Is the processing activity itself strictly necessary, or does it go beyond what the purpose requires? | Processing includes steps not needed for the stated purpose                  |
| **Retention**        | Is the retention period limited to what is strictly necessary for the stated purpose?                 | Retention period tied to "maximum legal period" rather than purpose duration |
| **Access**           | Is access to the data limited to those with a genuine operational need?                               | Broad internal access not tied to the purpose                                |

**4d. Necessity test classification**

- **GREEN**: Processing strictly necessary; no less intrusive alternative achieves same
  result; data volume, scope, and retention proportionate
- **YELLOW**: Necessity plausible but not comprehensively documented; some less intrusive
  alternatives exist but may be less effective; retention period could be shorter
- **RED**: Processing not strictly necessary; clear less intrusive alternatives not
  considered; data volume or retention significantly exceeds what purpose requires

**Stage 2 gate:** If Stage 2 is RED → LIA test fails. A failed necessity test cannot be
salvaged by safeguards in the balancing test. Proceed to Step 9 (alternative basis).

### Step 5: Identify Rights and Freedoms at Risk

Before conducting the balancing test, identify the specific rights and interests of data
subjects that the processing engages. This analysis feeds directly into Step 6.

**Categories of impact to assess:**

| Category                            | Specific harms to consider                                                                           |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Privacy and dignity**             | Loss of control over personal information; exposure of private matters; surveillance chilling effect |
| **Economic harm**                   | Financial loss; credit harm; employment discrimination; loss of business opportunities               |
| **Non-discrimination**              | Profiling that perpetuates or creates discriminatory outcomes based on protected characteristics     |
| **Autonomy and self-determination** | Loss of ability to make free choices; manipulation; reduced freedom of action                        |
| **Physical safety**                 | Safety risks arising from data exposure (e.g., location data, domestic violence victims)             |
| **Reputational harm**               | Damage to reputation arising from inaccurate data or inappropriate disclosure                        |
| **Barriers to rights exercise**     | Making it difficult to exercise data subject rights; digital exclusion                               |

**Vulnerability assessment:**

| Data subject group                            | Heightened protection required?                                                      |
| --------------------------------------------- | ------------------------------------------------------------------------------------ |
| Children (under 18)                           | YES — enhanced protection across all EDPB guidance                                   |
| Employees                                     | YES — power imbalance in employment relationship; effective consent often impossible |
| Patients / health service users               | YES — heightened sensitivity; health data attracts Art. 9                            |
| People in financial difficulty                | YES — heightened vulnerability to exploitation                                       |
| General consumers (B2C)                       | MODERATE — greater protection than B2B counterparties                                |
| Business contacts (B2B)                       | LOWER — professional context; reduced expectation of privacy                         |
| Members of the public (no prior relationship) | MODERATE to HIGH — no prior relationship; weaker reasonable expectations             |

**Output**: Produce a preliminary risk register listing each harm category engaged,
its severity (LOW / MEDIUM / HIGH), and its likelihood (UNLIKELY / POSSIBLE / PROBABLE).
This register drives the balancing test in Step 6.

### Step 6: Conduct the Balancing Test (Balancing Test — Stage 3)

Apply the EDPB Guidelines 1/2024 four-factor balancing methodology. The controller must
demonstrate that its legitimate interest (and the necessity of the processing) outweighs
the interests, rights, and fundamental freedoms of data subjects.

**Factor 1: Nature of Data and Processing Circumstances**

| Sub-factor        | Assessment questions                                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Sensitivity       | Is the data ordinary personal data, high-sensitivity ordinary data (financial, location), or special-category (Art. 9)? |
| Processing method | Automated vs. manual? Large-scale vs. targeted? Combined with other datasets?                                           |
| Data source       | Collected directly from data subjects? Obtained from third parties? Scraped from public sources?                        |
| Risk of misuse    | Could the data facilitate discrimination, identity fraud, physical harm, financial exploitation?                        |

**Factor 2: Likely Impact on Data Subjects**

| Impact dimension | Assessment questions                                                               |
| ---------------- | ---------------------------------------------------------------------------------- |
| Nature of impact | Financial loss? Reputational harm? Discrimination? Physical harm? Chilling effect? |
| Likelihood       | Is harm likely in normal operations, or only in case of breach/misuse?             |
| Severity         | Reversible/minor harm vs. irreversible/severe harm?                                |
| Scope            | Number of data subjects affected; geographic extent                                |
| Irreversibility  | Can data subjects recover from the harm?                                           |

**Factor 3: Reasonable Expectations of Data Subjects**

The test is **objective** — not whether each data subject actually expects the processing,
but whether a reasonable person in the same circumstances would. Key questions:

- Did data subjects provide data in this context expecting it to be used for this purpose?
- Is there an existing relationship between controller and data subject? (Existing customer
  vs. member of public has different expectation baseline)
- Was the processing purpose disclosed at the point of collection (Arts. 13/14)?
- Would data subjects be surprised to learn of this use? If yes, reasonable expectations
  are not met.
- Is this processing "common practice" in the relevant sector? Note: common practice alone
  does not establish reasonable expectations — sector knowledge not shared by data subjects
  should largely be disregarded (EDPB 1/2024).

**Factor 4: Safeguards Implemented (or Available)**

List all technical, organisational, and contractual measures in place that mitigate
identified harms. Note: GDPR-baseline compliance alone (basic encryption, standard
security measures) does not count as a safeguard for balancing purposes — measures
must go **beyond** legal minimums to tip the balance in the controller's favour.

See Step 7 (Safeguards Assessment) for the full safeguards catalogue.

**Balancing conclusion:**

| Outcome                     | Indicators                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Controller prevails**     | Controller interest is strong and specific; data subjects would reasonably expect the processing; impact is low-to-moderate; effective safeguards implemented |
| **Ambiguous / Conditional** | Controller interest is real but modest; impact is moderate; data subjects may not fully expect the processing; safeguards partially address identified harms  |
| **Data subject prevails**   | Data subject rights clearly override; impact is high; data subjects would not reasonably expect processing; safeguards cannot adequately mitigate harms       |

**Balancing test classification**

- **GREEN**: Balancing clearly favours controller; data subject rights not materially impaired
- **YELLOW**: Balancing is close; data subject protections (safeguards, opt-out, transparency)
  required before reliance on Art. 6(1)(f)
- **RED**: Balancing favours data subjects; controller's interest does not outweigh; the
  processing "overrides" the data subject's interests within the meaning of Art. 6(1)(f)

**CLARIFY** if balancing is YELLOW: Present the specific factors on each side and ask
the user whether additional safeguards can be implemented or documented. If yes, identify
which safeguards would tip the balance (see Step 7). If no, recommend moving to Step 9
(alternative basis).

### Step 7: Assess Safeguards

Identify safeguards available or already implemented. For YELLOW balancing outcomes,
assess whether specific safeguards can tip the balance in the controller's favour.
For GREEN outcomes, document existing safeguards as evidence of the balancing analysis.

**Safeguards catalogue (in descending order of impact on the balancing test):**

| Safeguard                                           | Description                                                                                                                                                                                                           | Balancing impact                                            |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Transparent privacy notice (Arts. 13/14)**        | Disclosure of specific legitimate interest in privacy notice at collection. EDPB considers this an "integral precondition" to lawful Art. 6(1)(f) processing, not merely a transparency obligation.                   | HIGH — mandatory regardless of balancing outcome            |
| **Easy, prominent opt-out (Art. 21)**               | Operational opt-out mechanism for Art. 21 right to object; for direct marketing, Art. 21(2) opt-out must be provided at or before first communication. Absence of genuine opt-out significantly weakens balancing.    | HIGH — strengthens reasonable expectations and autonomy     |
| **Data minimisation beyond minimum**                | Processing fewer data categories than the maximum that could theoretically serve the purpose; using aggregated rather than granular individual data (e.g., weekly vs. daily-level performance data).                  | HIGH — demonstrates proportionality                         |
| **Strict retention limits**                         | Retention periods shorter than the legal maximum, tied specifically to the purpose duration; automated deletion at period end.                                                                                        | HIGH — demonstrates time-proportionality                    |
| **Access controls**                                 | Restricting internal access to only those with a genuine operational need for the specific purpose (role-based access control, audit logs).                                                                           | MEDIUM-HIGH — limits exposure                               |
| **Pseudonymisation**                                | Replacing direct identifiers with pseudonyms where the purpose can be served without direct identification. Note: pseudonymised data remains personal data under GDPR.                                                | MEDIUM — reduces sensitivity                                |
| **Anonymisation or aggregation**                    | If the purpose can be fully achieved with anonymised or aggregate data, the data protection issue disappears. If truly anonymous data would serve the purpose, processing identifiable data fails the necessity test. | HIGH (necessity) — if feasible                              |
| **Additional encryption**                           | Encryption beyond Art. 32 minimums; EU-controlled encryption where only the EU entity holds keys.                                                                                                                     | MEDIUM — reduces breach risk                                |
| **Audit trails and accountability**                 | Maintaining records of the LIA and processing decisions; periodic reassessment schedule.                                                                                                                              | MEDIUM — demonstrates accountability                        |
| **Codes of conduct or certification (Arts. 40-42)** | Participation in an approved code of conduct or certification scheme demonstrates best practice.                                                                                                                      | LOW-MEDIUM — contextual; strengthens accountability posture |

**Safeguards output**: For each safeguard identified, document whether it is (a) already
implemented, (b) planned (with implementation timeline), or (c) not applicable. This
drives the remediation plan for CONDITIONAL outcomes.

### Step 8: Jurisdiction-Specific Parallel Analysis

After completing the three-part test, apply the applicable jurisdiction-specific frameworks.

#### 8a. EU GDPR — Detailed Analysis

**Primary authority**: EDPB Guidelines 1/2024 (adopted 8 October 2024)

**Purpose test (EU)**:

- Apply the three EDPB sub-criteria strictly: lawful, clearly and precisely articulated,
  real and present
- Third-party interests require demonstrated connection to controller's activities; EDPB
  identifies four recognised third-party LI categories (legal claims, transparency,
  research, public interest)
- Public authorities acting in an official capacity are excluded from Art. 6(1)(f)

**Necessity test (EU)**:

- "Strictly necessary" standard — not "useful" or "proportionate" in a loose sense
- Controller bears burden of actively examining and documenting alternatives
- Directly linked to Art. 5(1)(c) data minimisation

**Balancing test (EU)**:

- EDPB 1/2024 four-factor methodology applies
- "Reasonable expectations" test is objective — CJEU confirmed in C-621/22 (KNLTB)
  that members' reasonable expectations that their data would not be shared with sponsors
  for payment defeated the balancing test despite commercial interest being lawful
- Privacy notice disclosure of the specific legitimate interest is a precondition to
  lawfulness, not merely a transparency obligation
- Compelling legitimate grounds to override an Art. 21(1) objection are interpreted
  narrowly (grounds "essential" for severe penalty avoidance per EDPB 1/2024)

**EU enforcement context (as of 2026)**:

- LinkedIn €310M (DPC Ireland, October 2024): Behavioural advertising at scale
- Amazon France €32M (CNIL, December 2023): Granular employee monitoring
- CJEU C-446/21 (October 2024): Unlimited data aggregation for advertising
- CJEU C-621/22 (October 2024): Commercial interests can qualify but reasonable
  expectations remained the decisive hurdle

#### 8b. UK GDPR — Detailed Analysis

**Primary authority**: ICO Legitimate Interests Guidance (under review post-DUA Act 2025);
UK Data (Use and Access) Act 2025 (Royal Assent 19 June 2025)

**Core equivalence**: UK GDPR Art. 6(1)(f) is substantively identical to EU GDPR post-Brexit.
The ICO's three-part framework (purpose, necessity, balancing) mirrors the EDPB's approach.

**Key UK divergence — Recognised Legitimate Interests (DUA Act 2025, Schedule 4/Annex 1)**:

The DUA Act 2025 inserts Annex 1 into UK GDPR, creating "Recognised Legitimate Interests"
for specified processing purposes. For recognised purposes, **only the necessity test
applies** — the balancing test is eliminated.

| Recognised purpose category                                      | Balancing test required?                            |
| ---------------------------------------------------------------- | --------------------------------------------------- |
| National security and defence                                    | NO                                                  |
| Public security                                                  | NO                                                  |
| Detection, investigation, or prevention of crime                 | NO                                                  |
| Responding to requests from bodies acting in the public interest | NO                                                  |
| Safeguarding vulnerable individuals                              | NO                                                  |
| Intra-group administrative transfer                              | Annex 1 listed but STILL requires LIA documentation |
| Direct marketing (to existing customers)                         | Annex 1 listed but STILL requires LIA documentation |
| Network and information security                                 | Annex 1 listed but STILL requires LIA documentation |

**Implementation status (as of March 2026)**: Schedule 4 / Annex 1 provisions are not
yet in force — secondary legislation (commencement regulations) required. ICO guidance
expected Q1 2026. Monitor commencement regulations before relying on Recognised LI.

**UK-specific approach to LIA documentation**:

- ICO frames the LIA as a "light-touch risk assessment" though substantive content is equivalent
- ICO provides a downloadable Word LIA template
- If LIA identifies potential high risks, a DPIA is required — DPIA can substitute for
  separate LIA (ICO explicitly confirms this)
- ICO notes that for direct marketing and intra-group transfers, a brief LIA is insufficient
  — a more detailed assessment is needed

**UK case law**:

- Experian (ICO enforcement 2020; Tribunal 2023): Switching from consent to LI for the
  same-purpose processing is not appropriate; original basis constrains subsequent processing
- Consistent with CJEU case law on reasonable expectations and proportionality

[JURISDICTION-SPECIFIC] UK-specific: Verify current ICO guidance under the DUA Act 2025;
check commencement regulations for Annex 1 Recognised Legitimate Interests; verify ICO
updated enforcement approach; check sector-specific ICO decisions in relevant industry.

#### 8c. Swiss FADP (nDSG) — Detailed Analysis

**Primary authority**: Federal Act on Data Protection (nDSG), effective 1 September 2023;
Art. 31(1)(b) FADP; Swiss Federal Data Protection Ordinance (DPO)

**Doctrinal difference**: The Swiss FADP uses an **inverted** model compared to GDPR:

- GDPR: Processing requires a lawful basis always
- Swiss FADP: Processing is prima facie lawful; a justification is only required if
  processing constitutes a violation of the data subject's **personality rights (Persönlichkeitsrechte)**

**Swiss justification ground**: Art. 31(1)(b) FADP — "overriding private or public interest"

This is the Swiss analogue to GDPR Art. 6(1)(f). There is no formal codified three-part
test in the statute; the framework is established through judicial interpretation.

**Art. 31(2) FADP illustrative examples** (non-exhaustive):

- Direct connection to contract conclusion or performance with the data subject
- Research, journalistic and editorial purposes (with appropriate privacy protections)
- Certain employment-related processing

**Practical alignment**: Organisations subject to both GDPR and Swiss FADP should run a
GDPR-aligned LIA and document it — this satisfies FADP requirements even though FADP is
less prescriptive. Running one GDPR-equivalent LIA with Swiss add-ons is the recommended
approach for dual-compliance organisations.

**Employer monitoring (Swiss law)**: Employer interests may be justified by Art. 31(1)(b)
FADP as an overriding private interest, but Art. 328b Swiss Code of Obligations limits
the data that employers may process about employees — monitoring must be necessary for
the employment relationship and proportionate.

[JURISDICTION-SPECIFIC] Verify: (a) Whether FDPIC has issued comprehensive guidance on
Art. 31 FADP equivalent to EDPB 1/2024; (b) Relevant Federal Supreme Court jurisprudence
on proportionality and overriding private interest; (c) Sector-specific Swiss regulations
that restrict or supplement Art. 31 FADP.

#### 8d. Multi-Jurisdiction Comparative Summary

| Dimension                        | EU GDPR                          | UK GDPR                                              | Swiss FADP                       |
| -------------------------------- | -------------------------------- | ---------------------------------------------------- | -------------------------------- |
| Three-part test codified?        | YES (Art. 6(1)(f) + EDPB 1/2024) | YES (Art. 6(1)(f) + ICO)                             | NO (Art. 31 — case-by-case)      |
| "Strictly necessary" standard?   | YES (EDPB 1/2024)                | YES (ICO)                                            | Similar (proportionality)        |
| Balancing test required?         | YES (always)                     | YES (standard LI) / NO (Recognised LI once in force) | Implied (overriding requirement) |
| Recognised/automatic categories? | NO                               | YES (Annex 1 — once in force)                        | YES (Art. 31(2) examples)        |
| Key latest guidance              | EDPB Guidelines 1/2024           | ICO (review pending DUA)                             | FDPIC [VERIFY currency]          |
| Most demanding balancing test?   | YES — EDPB 1/2024 strict         | Similar to EU                                        | Less prescriptive                |

### Step 9: Alternative Lawful Basis Assessment

If Stage 1 or Stage 2 fails (RED), or if Stage 3 balancing fails (RED), or if the
overall outcome is REJECTED, assess alternative lawful bases under Art. 6(1):

| Basis                    | Art.    | When applicable                                                                                                                           | Assessment                                                                   |
| ------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Consent**              | 6(1)(a) | Where data subject can freely, specifically, and informedly consent; freely given consent possible (not in employment without safeguards) | Preferred for direct marketing to non-customers; avoids LIA complexity       |
| **Contract**             | 6(1)(b) | Processing strictly necessary for performance of a contract to which the data subject is party, or pre-contractual steps                  | Must be genuinely necessary for the specific contract, not merely convenient |
| **Legal obligation**     | 6(1)(c) | Processing required by a legal obligation under EU or Member State law                                                                    | Must cite the specific legal obligation                                      |
| **Vital interests**      | 6(1)(d) | Processing necessary to protect life (processing cannot be done on another basis)                                                         | Very narrow; last resort for life-threatening situations                     |
| **Public task**          | 6(1)(e) | Processing by a public authority or controller performing a public task under official authority                                          | Primarily for public sector; requires legal basis in EU/Member State law     |
| **Legitimate interests** | 6(1)(f) | The basis being assessed — if failed, cannot be used                                                                                      | N/A                                                                          |

**CLARIFY** if no viable alternative basis is identified: Inform the user that the
processing cannot be lawfully conducted in its current form under Art. 6. Options are:
(a) redesign the processing so a lawful basis applies; (b) obtain freely-given consent
as a redesigned basis; (c) do not conduct the processing.

### Step 10: Overall Classification and Recommendation

Synthesise the three-part test results into an overall classification.

**Per-component classification summary:**

| Test Component           | Classification       | Confidence             | Key finding |
| ------------------------ | -------------------- | ---------------------- | ----------- |
| Stage 1 — Purpose Test   | GREEN / YELLOW / RED | HIGH/PROBABLE/POSSIBLE | [Summary]   |
| Stage 2 — Necessity Test | GREEN / YELLOW / RED | HIGH/PROBABLE/POSSIBLE | [Summary]   |
| Stage 3 — Balancing Test | GREEN / YELLOW / RED | HIGH/PROBABLE/POSSIBLE | [Summary]   |

**Overall LIA classification:**

| Classification  | Trigger                                                                                               | Meaning                                                                                                                                                                      |
| --------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **APPROVED**    | All three stages GREEN, or YELLOW stages with documented mitigations that address all identified gaps | Controller may rely on Art. 6(1)(f) as the lawful basis, subject to transparency requirements and operational Art. 21 opt-out. Document the LIA record.                      |
| **CONDITIONAL** | One or more stages YELLOW; no stages RED; specific mitigations required                               | Controller may rely on Art. 6(1)(f) only after implementing the specified mitigations. Do not commence processing until mitigations are confirmed. Reassess within [X] days. |
| **REJECTED**    | Any stage RED; balancing clearly favours data subjects                                                | Controller may not rely on Art. 6(1)(f) for this processing. Consider alternative lawful basis or redesign the processing.                                                   |

**Recommendation statement** (include in output):

- If APPROVED: "This processing may rely on GDPR Art. 6(1)(f) as the lawful basis.
  Ensure the specific legitimate interest is disclosed in the privacy notice, an Art. 21
  opt-out mechanism is operational, and the LIA record is retained for supervisory review."
- If CONDITIONAL: "This processing may rely on GDPR Art. 6(1)(f) only after implementing
  the following mitigations: [list]. Target completion: [date]. Do not commence processing
  until confirmed. Reassess the LIA if processing changes materially."
- If REJECTED: "This processing cannot rely on Art. 6(1)(f). The LIA test fails at
  [Stage X] because [reason]. Recommended next step: [alternative basis / processing
  redesign / abandon processing]."

### Step 11: Documentation and Output

Generate the complete LIA documentation package:

**11a. LIA Record** (per processing activity)

- Processing activity name and description
- Data categories and data subjects
- Purpose test documentation (three sub-criteria)
- Necessity test documentation (three stress-questions)
- Balancing test documentation (four-factor methodology)
- Safeguards implemented or planned
- Overall classification and recommendation
- Date of assessment, assessor name/role, next reassessment date
- Version history (for ongoing reassessments)

**11b. ROPA Update** (Art. 30)

- Add "Art. 6(1)(f) — legitimate interests of the controller: [specific interest]" to
  the lawful basis field in the ROPA entry for this processing activity
- Note that a LIA record exists and where it is stored

**11c. Privacy Notice Disclosure** (Arts. 13(1)(d) and 14(2)(b))

- Required language: Disclose the specific legitimate interest in the privacy notice.
  This is a precondition to lawful processing under Art. 6(1)(f) per CJEU and EDPB
  1/2024, not merely a transparency obligation.
- Suggested disclosure format: "We process [data] for [purpose] on the basis of our
  legitimate interest in [specific interest]. You have the right to object to this
  processing — see [link to Art. 21 mechanism]."

**11d. DPIA Trigger Check**

- If the balancing test identifies HIGH likelihood/severity risks to data subjects'
  rights, assess whether a DPIA is required (Art. 35).
- DPIA triggers include: large-scale profiling, systematic monitoring, sensitive data
  at scale, novel technology, any process likely to result in high risk.
- If DPIA is required, initiate `legalcode-dpia-generator`.
- Note: A completed DPIA can substitute for the separate LIA record (ICO confirms).

**11e. Art. 21 Opt-Out Mechanism Check**

- Confirm that an operational right-to-object mechanism exists for this processing.
- For direct marketing: Art. 21(2) opt-out must be provided no later than at first
  communication. Absence of this opt-out significantly undermines the balancing test.
- For other Art. 6(1)(f) processing: Art. 21(1) mechanism must be accessible.
- Confirm process for honouring objections within one calendar month (Art. 12(3)).

**11f. Reassessment Triggers**

- Document the conditions under which the LIA must be reassessed:
  - Material change to processing purpose, data categories, or data subjects
  - New regulatory guidance from the competent supervisory authority
  - New case law affecting the balancing test
  - Enforcement action against comparable processing by another controller
  - Data subject complaints or regulatory enquiries relating to this processing
  - Breach incident affecting this processing activity

---

## Deep Topic Analysis Framework

### Framework 1: Legitimate Interest Taxonomy

Recognised categories of legitimate interest with typical assessment outcomes:

| Category                                                     | Purpose test                                                                | Necessity test                                                                                | Balancing test                                                                                               | Typical overall                                                          |
| ------------------------------------------------------------ | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **Fraud prevention / detection**                             | GREEN — Recital 50; EDPB 1/2024                                             | YELLOW — "strictly necessary" data and monitoring scope                                       | GREEN if proportionate; RED if systematic, blanket surveillance                                              | APPROVED if well-scoped                                                  |
| **Network and information security**                         | GREEN — Recital 49; EDPB 1/2024                                             | YELLOW — content analysis beyond metadata may fail                                            | GREEN for technical security measures; YELLOW-RED for extensive content monitoring                           | APPROVED for proportionate technical measures                            |
| **Direct marketing (existing customers)**                    | GREEN — Recital 47; EDPB 1/2024                                             | YELLOW — limited to data needed for marketing; no excessive profiling                         | YELLOW — existing relationship helps; opt-out mechanism is critical; Art. 21(2) absolute right               | CONDITIONAL — robust opt-out required                                    |
| **Direct marketing (no prior relationship)**                 | GREEN — Recital 47                                                          | YELLOW-RED — data source matters; bought lists vs. organic                                    | RED-YELLOW — absent relationship weakens balancing; electronic marketing also requires PECR/ePrivacy consent | CONDITIONAL to REJECTED — highly fact-specific                           |
| **Intra-group administrative transfers**                     | GREEN — Recital 48 (not a blank check; each transfer needs assessment)      | YELLOW — employee data requires additional attention; not automatic pass                      | YELLOW — employee data involves power imbalance; proportionality required                                    | CONDITIONAL — per-transfer basis                                         |
| **Employee monitoring — proportionate**                      | YELLOW — must specify purpose precisely; not vague "performance management" | YELLOW — must use minimum necessary data; aggregated preferred over granular                  | YELLOW-RED — employer-employee power imbalance; Amazon France (CNIL 2023) sets ceiling                       | CONDITIONAL — specific, proportionate, less intrusive means demonstrated |
| **Employee monitoring — extensive/real-time**                | YELLOW — purpose may be legitimate but must be specific                     | RED — granular real-time monitoring typically fails necessity where aggregated data suffices  | RED — power imbalance; disproportionate means; Amazon France illustrates ceiling                             | REJECTED — redesign required                                             |
| **Profiling / analytics (targeted, limited)**                | YELLOW — must articulate specific commercial or operational benefit         | YELLOW — data minimisation critical; scope must match purpose                                 | YELLOW — scale, granularity, and Art. 22 interaction; reasonable expectations key                            | CONDITIONAL — data minimisation, opt-out, no automated decisions         |
| **Profiling / analytics (behavioural advertising at scale)** | GREEN — commercial interest lawful (CJEU KNLTB Oct 2024)                    | RED-YELLOW — unlimited aggregation of on/off platform data fails Art. 5(1)(c) (CJEU C-446/21) | RED — users' interests override at scale (LinkedIn €310M, DPC Oct 2024)                                      | REJECTED — consent required for targeted advertising at scale            |
| **Pursuing legal claims**                                    | GREEN — EDPB third-party LI category                                        | GREEN — limited to data needed for specific claim                                             | GREEN — clear necessity, proportionate to litigation context                                                 | APPROVED if limited to specific claim                                    |
| **Research / product improvement**                           | YELLOW — must be specific research objective, not vague "improvement"       | YELLOW — anonymised data preferred; if identifiable data necessary, explain why               | YELLOW — scale and re-identification risk matter; anonymisation strengthens balancing                        | CONDITIONAL — anonymisation or aggregation required where feasible       |
| **Credit assessment / sharing with CRAs**                    | GREEN — ICO named example; serves data subjects' and public interest        | GREEN — limited to credit-relevant data                                                       | GREEN — existing relationship; transparent process; independent oversight                                    | APPROVED — well-established practice with regulatory framework           |

### Framework 2: Necessity Stress-Test Protocol

Apply these ten questions systematically to every processing activity. Each "yes" answer
below strengthens necessity; each "no" requires explanation and may indicate failure.

1. Does this specific data (not more, not less) directly enable the identified interest?
2. Have we documented why each category of data is necessary (not merely useful)?
3. Have we documented at least one alternative approach we considered and rejected (with reasons)?
4. Could pseudonymised or anonymised data achieve the same purpose? (If yes, necessity fails for personal data)
5. Could aggregated data achieve the same purpose? (If yes, granular individual data fails necessity)
6. Is the retention period tied to the specific purpose duration, not the maximum legal period?
7. Is access to the data restricted to only those with a specific operational need?
8. Are we processing in the context in which the data was originally collected, or has the context shifted?
9. Have we considered whether a less intrusive processing method would achieve the same result?
10. Can we demonstrate that the processing is the minimum necessary given the identified purpose?

### Framework 3: Balancing Matrix

Score each factor from 1 (strongly favours data subjects) to 5 (strongly favours controller).
A total score below 10 suggests the balancing test fails; 10-15 is conditional; above 15
favours the controller (indicative only — the matrix informs but does not replace judgment).

| Factor                       | Sub-factors                                                                        | Controller score (1-5) | Notes |
| ---------------------------- | ---------------------------------------------------------------------------------- | ---------------------- | ----- |
| **Nature of data**           | Sensitivity, source, combination potential                                         |                        |       |
| **Processing circumstances** | Scale, automation, combination, profile-building                                   |                        |       |
| **Reasonable expectations**  | Prior relationship, disclosure at collection, context-consistency                  |                        |       |
| **Likely impact**            | Harm probability, harm severity, vulnerability of data subjects                    |                        |       |
| **Safeguards**               | Transparency, opt-out, minimisation, encryption, retention limits, access controls |                        |       |

**Interpretation:**

- Score 20-25: Strongly favours controller → GREEN
- Score 14-19: Balanced / conditional → YELLOW (specify which factors need improvement)
- Score 1-13: Strongly favours data subjects → RED

---

## Actionable Output per Finding

For each identified gap or failure, document using this template:

```
Finding ID: [LI-001, LI-002, ...]
Test component: [Purpose / Necessity / Balancing]
Legal / guidance basis: [GDPR Art. X / EDPB Guidelines 1/2024, § X / ICO guidance]
Severity: [RED / YELLOW / GREEN]
Finding: [Specific description of the gap or failure]
Business impact if unresolved: [What happens if this is not addressed — enforcement risk,
  processing invalidity, data subject harm, reputational harm]
Recommended action: [Specific, measurable action — not "improve documentation" but
  "Add the following language to the privacy notice at Section 3: [draft language]"]
Remediation owner: [Role or team]
Target date: [Specific date]
Evidence required: [What proves this is complete — e.g., "Updated privacy notice
  deployed to production website and archived copy retained"]
Escalation: [If RED: Legal/DPO sign-off required before processing commences]
```

---

## Prioritization Framework

Prioritize remediation actions across a three-tier system:

**Tier 1 — Must Fix Before Processing (Block)**

- Any RED finding in any of the three test components
- Privacy notice does not disclose the specific legitimate interest (Arts. 13/14 precondition)
- No operational Art. 21 opt-out mechanism for direct marketing (Art. 21(2))
- Processing involves special-category data without a separate Art. 9 condition
- Processing would constitute a solely automated decision (Art. 22 — LI cannot ground this)

**Tier 2 — Must Fix Within 30 Days (Conditional)**

- YELLOW findings in necessity test where alternatives were not documented
- YELLOW findings in balancing test where safeguards are planned but not yet implemented
- ROPA entry not updated with Art. 6(1)(f) as the lawful basis
- Reassessment date not documented

**Tier 3 — Continuous Improvement (Recommended)**

- Enhancing access controls beyond current minimum
- Implementing additional pseudonymisation where feasible
- Expanding privacy notice detail beyond the minimum required
- Establishing a periodic LIA review process (even without a trigger event)
- Participating in relevant codes of conduct or certification schemes (Arts. 40-42)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                           | Fail action                                                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites GDPR article, EDPB guidance, ICO guidance, or a specific enforcement decision                                                          | Add citation or mark [VERIFY]                                                                 |
| **Format**     | Citations identify instrument, article/section, and date (for guidance)                                                                                        | Fix format to: "GDPR Art. X / EDPB Guidelines 1/2024, § X / LinkedIn €310M (DPC, Oct 2024)"   |
| **Currency**   | Guidance citations checked for amendments — EDPB 1/2024 supersedes WP29 06/2014; DUA Act 2025 amends UK GDPR; FDPIC Swiss guidance [VERIFY]                    | Flag [CHECK CURRENCY] for WP29 06/2014 citations; confirm EDPB 1/2024 is the current guidance |
| **Domain**     | Analysis stays within the three-part LIA test; Art. 9 special-category analysis is flagged as requiring separate treatment; non-GDPR regimes are not conflated | Remove or flag jurisdictional bleed; separate Art. 9 issues                                   |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                                                                      | Add confidence qualifier; do not present YELLOW findings as GREEN                             |

### Self-Interrogation for RED Findings

For any finding classified RED, apply this three-pass adversarial review:

**Pass 1 — Legal Chain Integrity**
Does the RED classification follow logically from the cited authority? Would a supervisory
authority or court actually reach this conclusion on the specific facts? Is the finding
based on settled law or on an interpretation that could reasonably go the other way?

**Pass 2 — Completeness**
Have all relevant GDPR articles, EDPB guidance provisions, national supervisory authority
guidance, and case law been considered? Are there sector-specific factors that affect this
specific processing type? Have the mitigating safeguards been fully evaluated?

**Pass 3 — Challenge**
What is the strongest argument that this finding should be classified YELLOW rather than
RED? Under what circumstances might a reasonable DPO or privacy counsel accept this risk?
If the challenge is strong, downgrade to YELLOW and specify what additional information
would be needed to confirm RED.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                                         | Prescribed action                                              |
| ------------ | --------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statutory text, confirmed by CJEU or consistent supervisory authority practice               | State with confidence                                          |
| **High**     | 0.80–0.94 | Strong authority (EDPB guidelines, multiple SA decisions, clear recital support) with minor questions remaining | State with brief caveat                                        |
| **Probable** | 0.60–0.79 | Good arguments supported by guidance; could reasonably differ; limited enforcement data in this specific sector | State with reasoning and contra-indicators                     |
| **Possible** | 0.40–0.59 | Genuinely uncertain; evolving area; conflicting guidance; pending CJEU referral                                 | Flag for professional review; present both sides               |
| **Unlikely** | 0.00–0.39 | Weak basis; speculative; contradicted by authority                                                              | Do not assert; flag [UNCERTAIN]; escalate to qualified counsel |

---

## Glass Box Audit Trail

Include this YAML block at the end of every LIA output:

```yaml
glass_box:
  skill_name: "legalcode-legitimate-interest-assessment"
  topic: "Legitimate Interest Assessment — GDPR Art. 6(1)(f)"
  processing_activity: "[Activity name or description]"
  controller: "[Organisation name or placeholder]"
  jurisdiction: "[EU GDPR / UK GDPR / Swiss FADP / Multiple]"
  assessment_date: "[YYYY-MM-DD]"
  assessor: "[Name/role of assessor]"
  next_reassessment: "[Date or trigger condition]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  purpose_test: "[GREEN / YELLOW / RED] — [confidence level]"
  necessity_test: "[GREEN / YELLOW / RED] — [confidence level]"
  balancing_test: "[GREEN / YELLOW / RED] — [confidence level]"
  overall_classification: "APPROVED / CONDITIONAL / REJECTED"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  dpia_required: "Yes / No / Assessment pending"
  art_21_mechanism: "Operational / Planned (date) / Not applicable"
  privacy_notice_updated: "Yes / No / Required"
  ropa_updated: "Yes / No / Required"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review by a privacy counsel or DPO"
```

---

## Anti-Patterns

Do not do the following when conducting or documenting a Legitimate Interest Assessment.

1. **Listing "legitimate interest" in a privacy notice without conducting a genuine LIA.**
   Regulatory investigations routinely expose controllers who list Art. 6(1)(f) as a
   basis in privacy notices without any documented assessment. This was a pervasive
   pattern in the ICO's data broker investigation (Experian 2020) and is an immediate
   enforcement flag.

2. **Treating Recital 47 as an automatic pass for direct marketing.** Recital 47 names
   direct marketing as an example of a legitimate interest at the purpose test stage only.
   It does not exempt direct marketing from the necessity or balancing tests. Controllers
   must still demonstrate necessity and conduct the balancing test.

3. **Using Art. 6(1)(f) as a "last resort" when other bases are unavailable.** The EDPB
   explicitly rejects this approach. Art. 6(1)(f) requires its own affirmative justification.
   If the only reason for invoking LI is that consent cannot be obtained, the assessment
   must address why LI independently justifies the processing — not merely why consent failed.

4. **Conflating "useful" with "necessary."** Necessity means strictly necessary: no less
   intrusive alternative achieves the same purpose equally effectively. Data that is
   convenient, helpful, or efficiency-improving but not strictly necessary fails the test.

5. **Skipping the necessity test and proceeding directly to balancing.** The three-part
   test is sequential and cumulative. A failed necessity test cannot be rescued by a
   favourable balancing outcome. Each stage must be passed independently.

6. **Counting GDPR-baseline compliance as a safeguard in the balancing test.** Basic
   encryption, standard security measures, and Art. 32-compliant technical measures do
   not count as safeguards that tip the balancing test in the controller's favour. Safeguards
   must go beyond legal minimums (EDPB Guidelines 1/2024).

7. **Ignoring the power imbalance in employment relationships.** Employees are data subjects
   in a structurally unequal relationship with their employer. The balancing test weighs
   significantly against the controller when data subjects are employees. Consent is
   generally unreliable in employment contexts precisely because of this imbalance.

8. **Relying on "common practice in the industry" to establish reasonable expectations.**
   Industry-specific knowledge that data subjects would not share does not establish
   reasonable expectations for the purposes of the balancing test. The EDPB 1/2024
   explicitly cautions against this approach.

9. **Switching from consent to legitimate interest for the same processing purpose.**
   Where data was originally collected under consent, switching to Art. 6(1)(f) for the
   same purpose is not appropriate (confirmed in Experian ICO/Tribunal 2023). The original
   lawful basis constrains subsequent processing.

10. **Conducting LI-based profiling that tips into solely automated decision-making with
    legal effects.** Art. 22 GDPR does not include Art. 6(1)(f) as a permitted ground for
    solely automated decisions producing legal or similarly significant effects. If LI-based
    profiling feeds into automated decisions at this level, a separate Art. 22 legal basis
    (consent or contractual necessity) is required.

11. **Failing to provide an operational Art. 21 opt-out mechanism.** Even where LI is
    validly established, data subjects retain the right to object under Art. 21. For direct
    marketing (Art. 21(2)), the right to object is absolute and must be offered no later
    than at the first communication. Failure to honour objections is a separate violation
    independent of the LIA's validity.

12. **Conducting a LIA once and never reassessing.** Processing activities change;
    regulatory guidance evolves; enforcement practice shifts. The KNLTB (October 2024)
    and LinkedIn (October 2024) decisions both resulted from processing that may have
    passed an earlier assessment but failed under current standards. Set reassessment
    triggers and periodic review schedules.

13. **Confusing Art. 6(1)(f) scope with Art. 9 scope.** Even if the Art. 6(1)(f) LIA is
    valid, processing of special-category data (health, biometric, genetic, religious, etc.)
    also requires a separate Art. 9(2) condition. Art. 6(1)(f) alone is not sufficient
    for special-category processing.

14. **Treating UK Recognised Legitimate Interests as already in force (as of early 2026).**
    Schedule 4 / Annex 1 to the UK GDPR (DUA Act 2025) are not yet commenced. Commencement
    regulations are required. Do not rely on Recognised LI provisions until those regulations
    are in force and ICO guidance is published.

15. **Documenting an LIA without specifying the reassessment date and triggers.** An LIA
    record without a defined reassessment schedule fails the Art. 5(2) accountability
    requirement in practice. Controllers must be able to show that they actively maintain
    and review their LIA documentation, not merely that they conducted it once.

16. **Attempting to use Art. 6(1)(f) for unlimited, undifferentiated data aggregation
    for advertising.** Post-CJEU C-446/21 (Schrems v Meta, October 2024), the data
    minimisation principle (Art. 5(1)(c)) prohibits unlimited, time-unbounded aggregation
    of personal data for targeted advertising regardless of the lawful basis. No legitimate
    interest justification can override this structural limit.

17. **Treating the Swiss FADP overriding private interest as identical to GDPR Art. 6(1)(f).**
    While the Swiss FADP was aligned with GDPR standards, it uses an inverted doctrinal
    model (Art. 31 requires justification only when personality rights are violated, not
    always). Mechanically applying GDPR LIA criteria to Swiss-only processing may be
    over-restrictive; conversely, assuming the Swiss test is laxer without verifying FDPIC
    guidance may expose controllers to compliance gaps.

---

## Writing Standards

Apply these standards before delivering any LIA output.

**Plain language discipline:**

- Write in active voice: "The controller processes employee location data" not "Employee
  location data is processed by the controller"
- Name the actor: "The organisation must update its privacy notice" not "The privacy
  notice must be updated"
- One point per sentence; short sentences in the analysis
- Avoid vague qualifiers ("may," "might," "could") in GREEN findings; use them in YELLOW
  findings to convey genuine uncertainty

**Precision in legal claims:**

- Every legal claim cites its authority (GDPR article, EDPB paragraph, or ICO guidance section)
- Every [VERIFY] tag includes a brief explanation of what needs verification and why
- Never state a YELLOW finding as GREEN; never round up confidence from POSSIBLE to PROBABLE

**Quality gates before delivery:**

1. Can a non-lawyer understand the finding and the recommended action?
2. Can the controller take the recommended action without further legal advice?
3. Is every legal claim supported by a citation or marked [VERIFY]?
4. Does the output match the structure in the Output Format Template?
5. Has the Glass Box audit trail been completed with all mandatory fields?
6. Have all RED findings been through the three-pass self-interrogation?
7. Does the output state the overall classification clearly and early (not buried at the end)?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool
for retrieving jurisdiction-specific statutes, supervisory authority decisions, and case law.

**With legalcode-mcp connected (preferred):**

- In Step 8, search for jurisdiction-specific LIA guidance from the competent supervisory
  authority and relevant national case law
- Verify currency of EDPB Guidelines 1/2024, ICO updated guidance (post-DUA 2025), and
  FDPIC Swiss guidance
- Search for sector-specific enforcement decisions relevant to the processing type
- Save the most relevant results to a local reference file (e.g., `/tmp/lia-research-[date].md`)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with repository analysis and training-data knowledge
- Mark all statutory and case law references with [VERIFY] and note: "Verify currency
  and accuracy against the current EDPB, ICO, and FDPIC guidance"
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Recommend the user consult the ICO, EDPB, and FDPIC websites directly for current guidance
- Focus the assessment on structural quality, workflow design, and process documentation
  rather than detailed legal substance depth

**Key authoritative online sources (verify currency before each use):**

- EDPB Guidelines 1/2024: edpb.europa.eu
- ICO Legitimate Interests Guidance: ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/
- Swiss FDPIC: edoeb.admin.ch
- DUA Act 2025 (UK legislation): legislation.gov.uk

---

## Output Format Template

Every LIA output must follow this template:

```markdown
# Legitimate Interest Assessment — [Processing Activity Name]

**Organisation**: [Name or "Not specified"]
**Assessment date**: [YYYY-MM-DD]
**Assessor**: [Name/role]
**Jurisdiction(s)**: [EU GDPR / UK GDPR / Swiss FADP]
**Processing activity**: [One-sentence description]
**Next reassessment due**: [Date or trigger condition]

---

## Executive Summary

**Overall classification**: APPROVED / CONDITIONAL / REJECTED

| Test                     | Classification       | Confidence                 |
| ------------------------ | -------------------- | -------------------------- |
| Stage 1 — Purpose Test   | GREEN / YELLOW / RED | HIGH / PROBABLE / POSSIBLE |
| Stage 2 — Necessity Test | GREEN / YELLOW / RED | HIGH / PROBABLE / POSSIBLE |
| Stage 3 — Balancing Test | GREEN / YELLOW / RED | HIGH / PROBABLE / POSSIBLE |

**Key finding**: [One sentence — what drives the overall outcome]

**Recommended action**: [One sentence — what the controller must do next]

---

## Stage 1 — Purpose Test

**Identified legitimate interest**: [Specific statement of the interest]

**Three sub-criteria analysis:**

| Sub-criterion                     | Assessment  | Evidence / Notes         |
| --------------------------------- | ----------- | ------------------------ |
| Lawful                            | PASS / FAIL | [Citation and reasoning] |
| Clearly and precisely articulated | PASS / FAIL | [Citation and reasoning] |
| Real and present                  | PASS / FAIL | [Citation and reasoning] |

**Third-party interest?** [Yes / No — if Yes, connection to controller's activities: ...]

**Purpose test classification**: [GREEN / YELLOW / RED]
**Confidence**: [Level and rationale]

---

## Stage 2 — Necessity Test

**Stress-test results:**

| Question                               | Answer                      | Finding       |
| -------------------------------------- | --------------------------- | ------------- |
| Direct causal connection?              | [Yes/No]                    | [Explanation] |
| Less intrusive alternative considered? | [Yes/No + what alternative] | [Explanation] |
| Data minimisation — volume?            | [Adequate / Excessive]      | [Explanation] |
| Data minimisation — retention?         | [Proportionate / Excessive] | [Explanation] |
| Access restriction?                    | [In place / Missing]        | [Explanation] |

**Necessity test classification**: [GREEN / YELLOW / RED]
**Confidence**: [Level and rationale]

---

## Stage 3 — Balancing Test

**Rights and freedoms at risk:**
[Preliminary risk register — harms, severity, likelihood]

**Four-factor balancing analysis:**

**Factor 1 — Nature of data and processing circumstances**
[Analysis]

**Factor 2 — Likely impact on data subjects**
[Analysis]

**Factor 3 — Reasonable expectations of data subjects**
[Analysis]

**Factor 4 — Safeguards implemented or available**
[Safeguards list with status: implemented / planned / not applicable]

**Balancing test classification**: [GREEN / YELLOW / RED]
**Confidence**: [Level and rationale]

---

## Jurisdiction-Specific Analysis

### EU GDPR (if applicable)

[Key EU-specific points: EDPB 1/2024 application, relevant enforcement context]

### UK GDPR (if applicable)

[Key UK-specific points: ICO guidance, DUA Act 2025 Recognised LI status, relevant UK enforcement]

### Swiss FADP (if applicable)

[Key Swiss-specific points: Art. 31(1)(b) application, FDPIC guidance status]

---

## Findings and Remediation Plan

| Finding ID | Stage   | Severity     | Finding       | Action            | Owner  | Due    | Evidence   |
| ---------- | ------- | ------------ | ------------- | ----------------- | ------ | ------ | ---------- |
| LI-001     | [Stage] | [RED/YELLOW] | [Description] | [Specific action] | [Role] | [Date] | [Evidence] |

---

## Privacy Notice and ROPA Requirements

**Privacy notice update required?** [Yes / No]
**Required disclosure**: [Draft language for privacy notice, if applicable]
**ROPA update required?** [Yes / No — lawful basis field: "Art. 6(1)(f) — [specific interest]"]
**DPIA required?** [Yes — trigger legalcode-dpia-generator / No / Assessment required]
**Art. 21 opt-out operational?** [Yes / No / Required]

---

## Overall Classification and Recommendation

**Classification**: APPROVED / CONDITIONAL / REJECTED

**Recommendation**: [Full recommendation statement per Step 10]

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section]
```

---

## Localization Notes

To create a jurisdiction-specific variant of this skill for a Member State or national
jurisdiction:

1. Research the competent supervisory authority's published guidance on Art. 6(1)(f) —
   most EU SAs have issued sector-specific guidance that supplements EDPB Guidelines 1/2024
2. Research national derogations enacted under Art. 23 GDPR that restrict Art. 6(1)(f) use
   in specific sectors (employment, health, finance, telecommunications)
3. Research national case law on legitimate interest balancing
4. Replace [JURISDICTION-SPECIFIC] markers with verified local legal content
5. Add jurisdiction-specific enforcement examples to the anti-patterns section
6. Check national data protection law for any additional documentation requirements
7. Verify: Some Member States require notification to the supervisory authority for
   specific categories of Art. 6(1)(f) processing — research local notification obligations

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis.

Primary legal sources: GDPR (EU) 2016/679; UK GDPR (retained EU law); UK Data (Use and
Access) Act 2025; Swiss Federal Act on Data Protection (nDSG/FADP), effective 1 September
2023; EDPB Guidelines 1/2024 on processing based on Art. 6(1)(f) (adopted 8 October 2024);
WP29 Opinion 06/2014 on legitimate interests (partially superseded); ICO Legitimate Interests
Guidance; CJEU C-621/22 (KNLTB, 4 October 2024); CJEU C-446/21 (Schrems v Meta,
4 October 2024); CJEU C-184/20 (OT, 2022); Irish DPC LinkedIn Decision (24 October 2024,
€310M); CNIL Amazon France Logistique Decision (December 2023, €32M); Experian ICO
Enforcement Notice (2020) and Information Tribunal outcome (2023).

Research methodology: 2-agent research pipeline — Agent 1 (structural analysis of
legalcode-contract-review, legalcode-dpia-generator, and legalcode-cross-border-transfer-assessment
reference skills) + Agent 2 (deep legal research via web search covering EDPB 1/2024, ICO
guidance, Swiss FADP, enforcement actions 2022-2025, and CJEU case law). All legal
references should be verified against current authoritative sources before reliance.
