---
name: legalcode-ai-fundamental-rights-impact-assessment
description: Conduct Fundamental Rights Impact Assessments (FRIA) as required under EU AI Act Art. 27
  (Regulation 2024/1689) for deployers of high-risk AI systems. Use when a covered deployer must produce
  a FRIA before first deployment of a high-risk AI system; when performing a pre-deployment rights review
  of an Annex III AI system; when integrating a FRIA with an existing DPIA; when responding to a market
  surveillance authority request for FRIA documentation; or when building an organisational FRIA programme.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conduct Fundamental Rights Impact Assessments (FRIA) as required under EU AI Act Art. 27 (Regulation 2024/1689) for deployers of high-risk AI systems. Applies to public authorities deploying any Annex III system (excluding Point 2 critical infrastructure), private entities providing public services (education, healthcare, social services, housing, justice), and financial sector deployers of creditworthiness or insurance-pricing AI. Assesses impact across the full EU Charter of Fundamental Rights: human dignity (Art. 1), privacy and data protection (Arts. 7-8), freedom of expression (Art. 11), equality and non-discrimination (Art. 21), rights of the child (Art. 24), rights of the elderly (Art. 25), persons with disabilities (Art. 26), right to good administration (Art. 41), and right to an effective remedy (Art. 47). Includes three-gate eligibility determination, Charter article-by-article rights analysis, vulnerable group impact assessment, cumulative impact analysis across co-deployed AI systems, four-part proportionality evaluation (legitimate aim, suitability, necessity, balancing), and human oversight adequacy review. Generates FRIA documentation meeting EU AI Act Art. 27(1)-(4) regulatory requirements and structured for notification to the market surveillance authority under Art. 27(3). Cross-references GDPR Art. 35 DPIA to avoid duplication while ensuring full Charter coverage. Integrates affected-stakeholder consultation record and FRIA refresh obligation planning. Use when a covered deployer must produce a FRIA before first deployment of a high-risk AI system; when performing a pre-deployment rights review of an Annex III AI system; when integrating a FRIA with an existing DPIA; when responding to a market surveillance authority request for FRIA documentation; or when building an organisational FRIA programme. Produces a complete FRIA document suitable for regulatory submission, internal governance, and stakeholder transparency.


# Legalcode AI Fundamental Rights Impact Assessment (FRIA)

> **Disclaimer**: This skill provides a framework for AI-assisted Fundamental Rights
> Impact Assessment under EU AI Act Article 27. It does not constitute legal advice,
> a determination of regulatory compliance, or authorisation to deploy an AI system.
> All outputs require review by qualified legal counsel and, where appropriate,
> fundamental rights experts before any deployment decision. The EU AI Act
> (Regulation 2024/1689) is recent legislation; implementing guidance from the AI
> Office, market surveillance authorities, and national data protection authorities
> continues to evolve. As of the enforcement deadline (August 2, 2026), several
> implementing acts and the standardised AI Office FRIA questionnaire template had
> not yet been published — verify current requirements against official EUR-Lex text
> and AI Office publications. Statutory, regulatory, case-law, and Charter references
> cited from training-data knowledge carry hallucination risk — verify against
> authoritative primary sources before relying on them. Mark all unverified references
> [VERIFY].

---

## Purpose and Scope

This skill conducts structured Fundamental Rights Impact Assessments (FRIAs) as
required under Article 27 of Regulation (EU) 2024/1689 (the EU AI Act). The FRIA is
a **deployer obligation** — distinct from the provider's Article 9 risk management
system — requiring specified deployer categories to assess and document the impact of
high-risk AI deployment on the fundamental rights protected by the EU Charter.

**Covers:**

- Three-gate eligibility determination (deployer category, system scope, timing)
- Charter of Fundamental Rights article-by-article impact analysis (nine rights clusters)
- Vulnerable group impact assessment (ten enumerated groups with specific criteria)
- Cumulative impact analysis across co-deployed AI systems
- Four-part proportionality evaluation (legitimate aim, suitability, necessity, balancing)
- Human oversight adequacy assessment per Art. 27(1)(e)
- Affected stakeholder consultation design and record
- GDPR DPIA cross-reference and integration (Art. 27(4))
- Risk materialisation measures and complaint mechanism design
- FRIA document drafting meeting Art. 27(1) mandatory content requirements
- Market surveillance authority notification preparation (Art. 27(3))
- FRIA refresh obligation planning and update triggers
- EU AI database registration cross-check (Art. 49)

**Does not:**

- Constitute a DPIA under GDPR Article 35 (the FRIA complements, not replaces, the DPIA)
- Substitute for the provider's Article 9 risk management system or Annex IV technical documentation
- Conduct the Algorithmic Impact Assessment / fairness metric testing (see `legalcode-algorithmic-impact-assessment`)
- Assess general EU AI Act high-risk compliance requirements (Arts. 9-17) — see `legalcode-eu-ai-act-high-risk-compliance`
- Apply outside the EU AI Act's territorial scope or to non-covered deployer categories
- Guarantee regulatory compliance or authorise deployment

**Related skills:**

- `legalcode-dpia-generator` — GDPR Art. 35 DPIA; conduct before or concurrently with the FRIA; integrate per Art. 27(4)
- `legalcode-algorithmic-impact-assessment` — AIA/algorithmic fairness; run before or alongside the FRIA for non-discrimination dimension depth
- `legalcode-eu-ai-act-high-risk-compliance` — provider and deployer obligations audit; establishes the risk classification context the FRIA presupposes
- `legalcode-ai-governance-framework-builder` — organisational AI governance; the FRIA operates within the governance structures this skill designs

---

## Jurisdiction and Governing Law

This skill applies **EU law exclusively** — specifically:

| Instrument                                                                    | Role in FRIA                                                         |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Regulation (EU) 2024/1689 (EU AI Act), Arts. 7, 26, 27, 49, 71                | Primary obligation; eligibility, content, notification, registration |
| EU Charter of Fundamental Rights (2000/C 364/01)                              | Rights framework for the substantive assessment                      |
| Regulation (EU) 2016/679 (GDPR), Art. 35, 36, 82                              | DPIA integration and data protection dimension                       |
| Directive (EU) 2016/680 (Law Enforcement Directive), Art. 27                  | Parallel DPIA for law enforcement processing                         |
| Treaty on European Union (TEU), Art. 5(4)                                     | Proportionality principle                                            |
| Convention for the Protection of Human Rights and Fundamental Freedoms (ECHR) | Interpretive background for Charter rights                           |

**Territorial scope of the AI Act:** The Act applies to:

- Deployers established or located in the EU
- Deployers outside the EU using high-risk AI systems affecting persons in the EU

**[JURISDICTION-SPECIFIC] — Member State variation:** The AI Act is directly applicable
in all 27 Member States without transposition. However, Member States exercise discretion on:

- National market surveillance authority designation and scope
- Sector-specific AI governance guidance (healthcare, justice, migration)
- Public law definitions governing "body governed by public law" FRIA trigger
- National AI regulatory sandbox frameworks (Arts. 57-63)
- Additional national rules for law enforcement and migration AI (Annex III Points 6-7)

**Key enforcement dates:**

| Date            | Event                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------- |
| 1 August 2024   | AI Act entered into force                                                                      |
| 2 February 2025 | Prohibited practices (Art. 5) applied                                                          |
| 2 August 2025   | Member States must designate market surveillance authorities; GPAI obligations applied         |
| 2 August 2026   | **Article 27 FRIA obligation applies; all high-risk system obligations (Arts. 6-49) enforced** |
| 2 August 2027   | Annex I systems and systems already on market before August 2026 must comply                   |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when the answer would change the
direction or depth of the assessment.

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

Accept the FRIA trigger in any of these formats:

- **AI system description**: Name, vendor, purpose, Annex III category, and deployer context
- **Technical documentation**: Annex IV documentation or provider Art. 13 instructions for use
- **Prior assessment**: An existing DPIA, AIA, or earlier FRIA draft to extend or update
- **Procurement documentation**: Contract, tender, or pre-deployment governance record

If no system description is provided, ask the user to supply the system name, the
deployer's sector, and the intended use case.

---

### Step 2: Gather Deployer Context

**⟁ CLARIFY** — Before beginning the eligibility determination, gather:

1. **Deployer legal category** (determines Art. 27 applicability)
   - Options: Body governed by public law (municipal, regional, or national authority); Private entity providing public services (education, healthcare, social services, housing, administration of justice); Credit institution or insurance undertaking deploying Annex III Point 5(b)/(c) AI; None of the above (private commercial deployer)
   - _Why this matters_: Article 27 applies only to specified deployer categories. A purely commercial deployer deploying a high-risk AI system does not face a FRIA obligation under Art. 27, though other Art. 26 obligations apply.

2. **Annex III system category** (determines which rights are most at stake)
   - Options: Biometric (Point 1); Education / vocational training (Point 3); Employment and workers management (Point 4); Essential private/public services — creditworthiness, benefits, emergency (Point 5); Law enforcement (Point 6); Migration, asylum, border control (Point 7); Administration of justice / democratic processes (Point 8); Critical infrastructure (Point 2 — note: excluded from FRIA)
   - _Why this matters_: Each Annex III category creates a distinct rights risk profile. Law enforcement and migration AI implicate Art. 47, Art. 48, and non-discrimination rights most acutely; education AI implicates children's rights; creditworthiness AI implicates Art. 17, Art. 21, and Art. 36.

3. **Affected population characteristics**
   - Options: General adult population; Includes vulnerable groups (specify); Predominantly children or young persons; Predominantly elderly persons; Predominantly persons with disabilities; Predominantly migrants or asylum seekers; Unknown
   - _Why this matters_: Vulnerable group exposure escalates the assessment depth required for Charter Arts. 21, 24, 25, 26 and triggers intersectionality analysis.

4. **Existing DPIA status**
   - Options: DPIA completed and current; DPIA in progress; DPIA not yet started; DPIA not required (system does not process personal data); Unsure
   - _Why this matters_: A completed DPIA provides the privacy/data-protection foundation (Charter Arts. 7-8) that the FRIA cross-references. Art. 27(4) permits integrated DPIA/FRIA documentation.

5. **Stakeholder consultation status**
   - Options: Consultation completed (provide record); Consultation planned but not yet conducted; No consultation planned; Unsure whether consultation is appropriate
   - _Why this matters_: Recital 96 explicitly encourages deployers (particularly public sector) to involve representatives of affected groups. Omitting consultation is a documented FRIA anti-pattern and may expose the deployer to challenge.

6. **Deployment timeline and urgency**
   - Options: First deployment imminent (within 6 weeks); Standard lead time (2-3 months); Planning stage (6+ months); Updating an existing FRIA for a modified or continuing deployment
   - _Why this matters_: Determines scope depth and consultation feasibility. Art. 27 requires FRIA before first use — a FRIA conducted after deployment is procedurally defective.

**Default assumptions (batch mode):** Public sector deployer; Annex III scope to be determined in Gate 1; general population with possible vulnerable group exposure; DPIA not yet started; no consultation conducted; standard lead time.

**State assumptions explicitly.** If proceeding with defaults, begin the output with: "Assumed: [list assumptions] — please correct any inaccuracies and the assessment will be re-run accordingly."

---

### Step 3: Three-Gate Eligibility Determination

Before conducting the substantive rights analysis, apply three sequential eligibility
gates. Output a clear determination for each gate.

#### Gate 1 — Deployer Category (Article 27(1))

Assess whether the deployer falls within the three Article 27 categories:

**Category A — Public Law Bodies:**
Bodies governed by public law, including any entity:

- Established for the specific purpose of meeting needs in the general interest
- Not having an industrial or commercial character
- Subject to management supervision by the State, regional authorities, or other bodies governed by public law, OR having a supervisory board majority appointed by public authorities

_Examples:_ Municipal administrations, national employment agencies, courts, immigration authorities, public health services, public universities

**Category B — Private Entities Providing Public Services:**
Private bodies that deploy high-risk AI systems in their capacity as providers of:

- Education and vocational training services
- Healthcare services
- Social services
- Housing services
- Administration of justice

**Category C — Regulated Financial Sector Deployers:**
Deployers of AI systems falling specifically within Annex III:

- Point 5(b): AI used to evaluate the creditworthiness of natural persons or establish their credit score (excluding fraud detection systems)
- Point 5(c): AI used for risk assessment and pricing for life insurance or health insurance

**Gate 1 Output:**

- `FRIA_CATEGORY_A` — public law body deploying any Annex III system (except Point 2)
- `FRIA_CATEGORY_B` — private public-service provider deploying relevant Annex III systems
- `FRIA_CATEGORY_C` — credit or insurance institution deploying Point 5(b)/(c) AI
- `FRIA_NOT_REQUIRED` — none of the three categories applies; document basis and proceed to Art. 26 deployer obligations only
- `INSUFFICIENT_FACTS` — deployer category cannot be determined from available information; request clarification

**If `FRIA_NOT_REQUIRED`:** Stop FRIA workflow. Confirm the deployer still has Art. 26 general deployer obligations. Recommend `legalcode-eu-ai-act-high-risk-compliance` for the full deployer compliance audit.

---

#### Gate 2 — System Scope (Annex III Coverage)

Confirm that the AI system is:

1. A high-risk AI system listed in Annex III (Points 1-8)
2. Not excluded from the FRIA requirement by falling under Annex III **Point 2** (critical infrastructure: digital infrastructure, road traffic, water, gas, heating, electricity supply)

**Gate 2 Output:**

- `IN_SCOPE` — Annex III system confirmed, Point 2 exclusion does not apply
- `EXCLUDED_POINT_2` — AI system is Annex III Point 2 critical infrastructure; FRIA not required; Art. 26 obligations still apply
- `HIGH_RISK_CLASSIFICATION_NEEDED` — Annex III category unclear; trigger `legalcode-eu-ai-act-high-risk-compliance` to determine risk classification first
- `NOT_HIGH_RISK` — system does not meet Annex III high-risk criteria; FRIA not required

**⟁ CLARIFY** — If Annex III classification is uncertain, ask the user to describe the system's function, sector, and decision output. Reference the Annex III category table to determine the correct classification.

---

#### Gate 3 — Pre-Deployment Timing (Article 27(2))

Confirm whether the FRIA is being conducted before first use, as required.

**Gate 3 Output:**

- `PRE_DEPLOYMENT` — FRIA is being conducted before first use of the system; no procedural defect
- `UPDATE` — FRIA is being updated for a modified system or changed deployment context; note Art. 27(2) update obligation; review whether the original FRIA may still be relied upon for unchanged elements
- `POST_DEPLOYMENT_DEFECT` — FRIA is being conducted after the system has already been deployed; flag as **procedural violation of Art. 27**; continue assessment for remediation but prominently note the timing failure and recommend immediate notification to the market surveillance authority

---

**Eligibility Summary Block (output before proceeding):**

```
## FRIA Eligibility Determination

Deployer category:     [FRIA_CATEGORY_A / B / C / NOT_REQUIRED / INSUFFICIENT_FACTS]
System scope:          [IN_SCOPE / EXCLUDED_POINT_2 / CLASSIFICATION_NEEDED / NOT_HIGH_RISK]
Timing status:         [PRE_DEPLOYMENT / UPDATE / POST_DEPLOYMENT_DEFECT]

Overall determination: [FRIA_REQUIRED — proceed to Step 4]
                       [FRIA_NOT_REQUIRED — stop; document basis]
                       [INSUFFICIENT_FACTS — request: (list missing information)]
```

---

### Step 4: Gather Provider Documentation

Before conducting the rights analysis, collect the provider's Art. 13 information and
Art. 11 Annex IV technical documentation that the deployer should have received.

The following provider documentation directly feeds into the FRIA (Article 27(1)(d)
requires the deployer to assess risks "taking into account the information given by
the provider pursuant to Article 13"):

| Required Provider Document          | Art. Reference | Relevance to FRIA                                                                 |
| ----------------------------------- | -------------- | --------------------------------------------------------------------------------- |
| Instructions for use (general)      | Art. 13(1)     | Defines how system must be deployed; basis for Art. 27(1)(e) oversight assessment |
| Known and foreseeable risks         | Art. 13(2)(b)  | Input into Art. 27(1)(d) risk identification                                      |
| Performance metrics and limitations | Art. 13(2)(c)  | Supports proportionality (suitability) analysis                                   |
| Human oversight measures by design  | Art. 13(2)(d)  | Foundation for Art. 27(1)(e) oversight description                                |
| Known biases and mitigation         | Art. 13(2)(e)  | Essential for Art. 21 non-discrimination analysis                                 |
| Technical documentation (Annex IV)  | Art. 11        | Supports system description and proportionality assessment                        |
| Bias testing and fairness data      | Art. 9(7)      | Feeds non-discrimination analysis (Charter Art. 21)                               |
| Incident and malfunction log        | Art. 26(5)     | Informs risk materialisation history for updated FRIAs                            |

**⟁ CLARIFY** — If provider documentation is unavailable or incomplete, ask:

- Has the deployer received the Art. 13 instructions for use?
- Has the deployer received Annex IV technical documentation?
- If documentation is missing, note this as a **deployer compliance gap** under Art. 26(1) — deployers must obtain and review provider documentation before deployment.

**If provider documentation is absent:** Proceed with the available information but mark all Art. 27(1)(d) risk assessments as [INCOMPLETE — AWAITING PROVIDER DOCUMENTATION]. Flag the gap prominently in the FRIA output.

---

### Step 5: Legal Authority Research

Gather applicable legal authority to inform the rights analysis.

#### 5a. With legalcode-mcp Connected (Preferred)

Search for:

- EU AI Act Art. 27 implementing acts and official guidance
- AI Office FRIA questionnaire template (Art. 27(5))
- EDPB guidance on GDPR–AI Act interplay
- FRA reports on AI and fundamental rights
- Relevant CJEU case law on Charter rights and automated decision-making
- National market surveillance authority guidance (by Member State if known)

Save to `/tmp/legalcode-fria-research.md`:

```markdown
# FRIA Legal Authority Research

## Date: [date]

## AI System: [system name]

### EU AI Act Provisions

### Charter Authority

### EDPB/DPA Guidance

### FRA Reports

### Case Law

### National Authority Guidance
```

#### 5b. Without legalcode-mcp

Mark all statutory and Charter references in the FRIA output with [VERIFY]. Note in the Glass Box: `legalcode_mcp: "Not connected"`. Focus depth on structural analysis rather than precise citation.

**Key primary sources to consult:**

- EUR-Lex: Regulation (EU) 2024/1689 (official text)
- AI Act Service Desk: ai-act-service-desk.ec.europa.eu
- ECNL/DIHR: "A Guide to Fundamental Rights Impact Assessments under the EU AI Act"
- FRA: "Assessing High-risk Artificial Intelligence: Fundamental Rights Risks" (2025)
- EDPB Opinion 28/2024

---

### Step 6: Charter Rights Impact Analysis

Assess the deployment's impact across nine fundamental rights clusters. For each
cluster, apply the full analytical framework:

1. **How this right is engaged** by the specific AI system and deployment context
2. **Assessment questions** to evaluate rights impact (system-specific)
3. **Evidence review** from provider documentation and available testing data
4. **Severity classification**: MINIMAL / LOW / MEDIUM / HIGH rights impact
5. **Mitigation measures** identified

Apply the **Self-Interrogation** protocol (see Quality Frameworks) to all MEDIUM and
HIGH impact findings before finalising the classification.

---

#### Dimension A — Human Dignity and Integrity (Charter Arts. 1 and 3)

**Rights engaged:**

- Art. 1: Every person has an inviolable right to dignity. Automated systems that reduce individuals to risk scores, algorithmic profiles, or categorical labels without individual consideration engage this right.
- Art. 3: Right to integrity of the person. Biometric and physiological monitoring AI may affect bodily integrity.

**Assessment questions:**

- [ ] Does the system produce outputs (risk scores, profiling labels, algorithmic categories) that dehumanise or stigmatise individuals?
- [ ] Are subjects of AI decisions reduced to numeric scores without any individualised consideration of circumstances?
- [ ] Are fully automated decisions issued in contexts where the person cannot make their case (employment, benefits, asylum)?
- [ ] Does the system involve real-time biometric identification or emotion detection that affects bodily or psychological integrity without genuine consent?
- [ ] Are the outputs communicated in ways that respect the dignity of the persons concerned?

**Risk indicators:** Fully automated decisions with no human review; stigmatising labels (e.g., "high risk individual," "likely fraudster"); real-time biometric surveillance in public spaces; emotion detection or physiological monitoring.

---

#### Dimension B — Privacy and Data Protection (Charter Arts. 7 and 8)

**Rights engaged:**

- Art. 7: Right to respect for private and family life. AI systems process and infer information about private life, family circumstances, and relationships.
- Art. 8: Right to protection of personal data. All high-risk AI systems requiring FRIA also process personal data.

**Assessment questions:**

- [ ] Has a DPIA under GDPR Art. 35 been conducted? (If yes, cross-reference findings; do not duplicate analysis.)
- [ ] Does the system make inferences about private life, family relationships, or home environment from behavioral or transactional data?
- [ ] Are data minimisation and purpose limitation principles respected in the AI deployment context?
- [ ] Does the system create new data linkages or inferences beyond the original consent or legal basis?
- [ ] Does the system process special categories of personal data (GDPR Art. 9: health, ethnicity, political opinions, criminal records, biometrics)?
- [ ] Are individuals meaningfully informed that AI processes their data?

**Integration with DPIA:** Where a DPIA has been conducted, record the following in the FRIA:

```
DPIA reference: [document title, date, DPO reviewer]
DPIA finding on privacy risk: [HIGH / MEDIUM / LOW]
FRIA complement: [list any Charter Arts. 7-8 elements not covered by the DPIA]
```

**Risk indicators:** Large-scale processing of sensitive categories; behavioral profiling; location or communications monitoring; data collected for one purpose repurposed for AI training.

---

#### Dimension C — Freedom of Thought, Expression, and Religion (Charter Arts. 10 and 11)

**Rights engaged:**

- Art. 10: Thought, conscience, and religion. Behavioral profiling may expose or infer religious or ideological beliefs.
- Art. 11: Freedom of expression and information. AI surveillance and monitoring systems may chill expression.

**Assessment questions:**

- [ ] Could awareness of AI monitoring cause individuals to self-censor their communications, association, or public behaviour?
- [ ] Does the system make inferences about religious, political, or ideological beliefs from behavioral or linguistic data?
- [ ] Is the system used in law enforcement or public space monitoring where the chilling effect on expression is foreseeable?
- [ ] Are AI-influenced decisions made based on expressed views, social connections, or public statements?
- [ ] Does the system expose religious affiliation through proxy variables or behavioural patterns?

**Risk indicators:** Predictive policing systems using social media data; social scoring systems; workplace monitoring of communications; educational surveillance tools monitoring student expression.

---

#### Dimension D — Equality and Non-Discrimination (Charter Arts. 20, 21, 22, 23)

**Rights engaged:**

- Art. 20: Equality before the law — consistent treatment regardless of characteristics.
- Art. 21: Non-discrimination on grounds of sex, race, colour, ethnic or social origin, genetic features, language, religion or belief, political or any other opinion, membership of a national minority, property, birth, disability, age, sexual orientation.
- Art. 22: Cultural, religious, and linguistic diversity.
- Art. 23: Gender equality.

**Assessment questions (apply all):**

- [ ] Has the provider conducted and disclosed disparate impact testing across all Charter Art. 21 protected grounds?
- [ ] Does the system use input variables that serve as proxies for protected characteristics (e.g., zip code / postcode for race or ethnicity; surname for national origin; credit history for socioeconomic origin; job title patterns for gender)?
- [ ] What are the false positive / false negative rate differentials across demographic groups? Are error rates distributed equitably?
- [ ] Is the training data representative of the populations the system will serve? What minority groups are underrepresented?
- [ ] Are the performance metrics reported by the provider population-wide averages that may mask poor performance on minority subgroups?
- [ ] Has the system been tested on data from linguistic and cultural minority communities relevant to the deployment context?
- [ ] Has gender-disaggregated bias testing been conducted?
- [ ] Does the system perform equally across age groups (relevant for elderly and youth populations)?

**Key distinction from AIA:** The FRIA assesses non-discrimination as a **rights violation**, not merely a statistical disparity. Even a technically "accurate" system may infringe Charter Art. 21 if it produces discriminatory outcomes. Refer to `legalcode-algorithmic-impact-assessment` for the full fairness-metric analysis; incorporate AIA findings into this FRIA dimension.

**Risk indicators:** Disparate impact in system outputs; use of proxy variables; training data reflecting historical discrimination; reported bias without documented remediation; system deployed in areas with documented historical discrimination (criminal justice, immigration, creditworthiness).

---

#### Dimension E — Rights of Specific Groups (Charter Arts. 24, 25, 26)

**Rights engaged:**

- Art. 24: Rights of the child — children's best interests must be a primary consideration.
- Art. 25: Rights of the elderly.
- Art. 26: Integration of persons with disabilities.

**Assessment questions — Children (Art. 24):**

- [ ] Are children among the affected population (directly or indirectly)?
- [ ] Has the system been specifically validated for use affecting children at the relevant developmental stage?
- [ ] Are parental/guardian consent mechanisms in place where required?
- [ ] Does the system comply with children's data protection requirements (GDPR Art. 8)?
- [ ] Are outputs communicated in a child-accessible format where children are direct subjects?

**Assessment questions — Elderly Persons (Art. 25):**

- [ ] Has age bias testing been conducted? Is age used as a variable in a way that may constitute ageism?
- [ ] Do output formats and interfaces accommodate persons with lower digital literacy?
- [ ] Are contestation pathways accessible to elderly individuals who may not use digital channels?

**Assessment questions — Persons with Disabilities (Art. 26):**

- [ ] Has the system been tested on users with a range of disabilities (physical, cognitive, sensory, neurological)?
- [ ] Are inputs and outputs accessible to persons using assistive technology?
- [ ] Does the system systematically disadvantage persons with disabilities through its decision criteria or assumptions?
- [ ] Are alternative assessment pathways maintained for persons who cannot interact with the AI system?

**Risk indicators:** Educational proctoring software; healthcare AI; social services AI; employment AI; benefits eligibility systems; any system where affected population includes children, elderly persons, or persons with disabilities.

---

#### Dimension F — Labor Rights (Charter Arts. 27-31)

**Rights engaged:**

- Art. 27: Workers' right to information and consultation.
- Art. 28: Right of collective bargaining.
- Art. 30: Protection against unjustified dismissal.
- Art. 31: Fair and just working conditions.

**Assessment questions:**

- [ ] Are workers subject to AI monitoring, performance management, or task allocation?
- [ ] Have workers and their representatives been informed and consulted about AI deployment per Art. 27?
- [ ] Does algorithmic management undermine workers' ability to seek redress for unfair treatment?
- [ ] Could AI-influenced performance assessments contribute to unjustified dismissal without meaningful human judgment?
- [ ] Does the AI system affect collective bargaining by making individual worker behaviour individually trackable and penalisable?
- [ ] Are working conditions affected by AI-determined task allocation, pacing, or scheduling?

**Risk indicators:** Employment AI; workplace monitoring systems; algorithmic task allocation; AI-assisted performance evaluation; hiring and promotion AI.

---

#### Dimension G — Access to Essential Services and Social Rights (Charter Arts. 34, 35, 36)

**Rights engaged:**

- Art. 34: Social security and social assistance.
- Art. 35: Right to health.
- Art. 36: Access to services of general economic interest.

**Assessment questions:**

- [ ] Does the system deny access to social benefits, healthcare, or essential services based on algorithmic risk scores without individualised assessment?
- [ ] What is the rate of wrongful denial, and what effective recourse exists?
- [ ] Has the AI system been validated across the demographic diversity of the population it serves (particularly for healthcare AI)?
- [ ] Are the most vulnerable persons (homeless, unbanked, disabled) able to access the system and contest decisions?
- [ ] Does the system create self-reinforcing poverty traps through algorithmic decisions about credit, insurance, or benefits?

**Risk indicators:** Benefits eligibility systems; fraud detection in social assistance; healthcare triage AI; credit scoring with disparate access outcomes; AI systems affecting access to utilities or housing.

---

#### Dimension H — Right to Good Administration and Effective Remedy (Charter Arts. 41 and 47)

**Rights engaged:**

- Art. 41: Right to have matters handled impartially, within a reasonable time, with a reasoned decision. Right to be heard before an adverse individual measure.
- Art. 47: Right to an effective remedy and to a fair trial. Right to legal aid where necessary.

This dimension is the **most frequently omitted** Charter right in FRIA practice. Assess it with particular care.

**Assessment questions:**

- [ ] Can individuals who are subject to AI-influenced decisions understand that AI was used and how it contributed to the outcome?
- [ ] Are meaningful contestation procedures available and accessible to affected individuals?
- [ ] Does the AI system's opacity prevent effective challenge? Can the reasoning be explained to a standard that allows legal challenge?
- [ ] Are AI recommendations presented to human decision-makers in ways that create automation bias (i.e., human reviewers effectively ratify AI decisions without genuine independent review)?
- [ ] Do overseers have sufficient competence, time, information, and authority to meaningfully intervene?
- [ ] Is the AI's contribution to the decision transparent in the decision record in a way that allows subsequent judicial review?
- [ ] Are complaint mechanisms effective and accessible, including for persons with limited digital literacy or legal knowledge?
- [ ] Are processing timeframes reasonable, and does AI use comply with legal deadlines for administrative decisions?

**Art. 48 supplement (law enforcement and justice AI):**

- [ ] Does the system produce outputs that presuppose guilt or danger without individualised evidence?
- [ ] Are outputs used in ways that effectively reverse the burden of proof?
- [ ] Are recidivism scores or risk classifications used in bail, sentencing, or detention decisions?

**Risk indicators:** Fully automated administrative decisions with no genuine human review; opaque AI systems where explanation is not possible; law enforcement and justice AI; migration and asylum AI; systems where complaint rate is very low (possibly indicating inaccessibility of complaint mechanisms).

---

#### Dimension I — Proportionality: Is the Deployment Justified? (TEU Art. 5(4); Charter Art. 52(1))

This dimension is **unique to the FRIA** and is not replicated in the DPIA or AIA. Apply the four-part proportionality test:

**Part 1 — Legitimate Aim (Legal Basis Test)**

- What specific public interest objective, legal mandate, or service obligation justifies deployment?
- Is the objective expressly sanctioned by law? For public authorities: what statutory mandate authorises this specific use of AI?
- Is the objective sufficiently important to justify interference with the identified fundamental rights?
- Document: `legal_basis: [statute/provision] | objective: [stated aim] | importance: [HIGH/MEDIUM/LOW]`

**Part 2 — Suitability (Rational Connection Test)**

- Is the AI system rationally capable of achieving the legitimate aim?
- Has the system been validated for accuracy and reliability in **this specific deployment context and population**?
- What evidence does the provider supply of effectiveness? Is it independently verified?
- The "zero question": Is any AI deployment needed at all, or could the objective be achieved by non-AI means?
- Document: `evidence_of_effectiveness: [source] | validation_in_context: [YES/NO/PARTIAL] | alternatives_considered: [list]`

**Part 3 — Necessity (Least Restrictive Means Test)**

- Could the legitimate aim be achieved through means less restrictive of fundamental rights?
- Have non-AI alternatives been genuinely considered and rejected with documented reasoning?
- If AI is used, has the least rights-intrusive configuration been chosen?
- Is the scope of AI deployment limited to what is strictly necessary for the objective?
- Document: `alternatives_assessed: [list] | least_restrictive_option_chosen: [YES/NO] | scope_limited: [YES/NO]`

**Part 4 — Proportionality Stricto Sensu (Balancing Test)**

- Do the benefits of AI deployment outweigh the fundamental rights costs?
- Are the most severely affected groups those who receive the fewest benefits?
- Is the rights interference proportionate to the gains, even after mitigation?
- Document: `benefit_distribution: [who benefits] | rights_cost_distribution: [who bears cost] | residual_impact_after_mitigation: [level] | proportionate: [YES / YES WITH CONDITIONS / NO]`

**Overall Proportionality Conclusion:**

- `PROPORTIONATE`: Deployment proceeds; document conditions if any
- `PROPORTIONATE WITH CONDITIONS`: Deployment permitted only with specific mitigations identified
- `DISPROPORTIONATE`: Deployment is not justified; recommend redesign or rejection

---

### Step 7: Vulnerable Group Impact Assessment

Conduct a focused assessment for each vulnerable group potentially affected by the deployment. Escalate findings from Step 6 that are concentrated in vulnerable groups.

Apply **intersectionality analysis**: assess compound effects for individuals with multiple vulnerability characteristics (e.g., a disabled migrant woman faces cumulative risks across multiple dimensions that exceed the sum of individual group analyses).

| Vulnerable Group                                     | Charter Basis    | Escalated Concerns | Specific Questions                                                                 |
| ---------------------------------------------------- | ---------------- | ------------------ | ---------------------------------------------------------------------------------- |
| Children                                             | Art. 24          | Dimension E        | See Dimension E assessment questions                                               |
| Elderly persons                                      | Art. 25          | Dimensions D, E, H | See Dimension E; digital access assessment                                         |
| Persons with disabilities                            | Art. 26          | Dimensions D, E, H | See Dimension E; accessibility assessment                                          |
| Racial and ethnic minorities                         | Art. 21          | Dimension D        | Disparate impact analysis; proxy variable review; training data representativeness |
| Religious minorities                                 | Arts. 10, 21     | Dimensions C, D    | Inference/exposure risks; disparate impact                                         |
| LGBTQ+ persons                                       | Art. 21          | Dimensions A, D    | Outing risk; disparate impact in employment/healthcare                             |
| Persons in poverty / socioeconomically disadvantaged | Arts. 34, 36     | Dimension G        | Access barriers; poverty trap reinforcement                                        |
| Migrants, asylum seekers, refugees                   | Arts. 18, 19, 21 | Dimensions A, D, H | Validation on affected populations; language barriers; bias in training data       |
| Persons with limited digital literacy                | Arts. 41, 47     | Dimension H        | Alternative access pathways; contestation accessibility                            |
| Persons with mental health conditions                | Arts. 21, 26     | Dimensions D, E    | Pathologisation risk; non-neurotypical behavior accommodation                      |

**Cumulative Impact Analysis:**

Assess whether this AI system interacts with or compounds the effects of **other AI systems** deployed by the same organisation or operating in the same sector:

1. **AI-on-AI interactions**: Map AI systems that share data, output chains, or decision pipelines with the system under assessment. Assess whether a rights-risk in System A is amplified when combined with System B.
2. **Population-level compounding**: If the affected population is subject to multiple algorithmic decisions (e.g., employment AI + credit scoring AI + benefits eligibility AI), assess whether the cumulative impact on individuals is disproportionate even if each system individually passes the rights test.
3. **Societal-level effects**: Assess whether AI deployment at scale could erode trust in public institutions, chill participation in public life, or systematically entrench historical inequalities in the affected community.

Document cumulative impact findings separately from individual system findings.

---

### Step 8: Human Oversight Adequacy Assessment (Article 27(1)(e))

Assess whether the human oversight measures, as described in the provider's instructions for use, are effectively implemented and genuinely protective in the specific deployment context.

**Oversight adequacy criteria:**

| Criterion                  | Assessment Questions                                                                                                               | Evidence                                                |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Competence**             | Do human overseers have the technical and domain knowledge to evaluate AI outputs critically?                                      | Training records; qualification requirements            |
| **Authority**              | Do overseers have genuine authority to override AI recommendations without organisational pressure?                                | Governance documentation; escalation procedures         |
| **Information**            | Are AI recommendations presented with sufficient context (uncertainty, confidence level, known limitations) for meaningful review? | UI/output design; provider instructions                 |
| **Time**                   | Do overseers have sufficient time to meaningfully review each AI recommendation?                                                   | Process throughput data; time-per-case records          |
| **Non-automation bias**    | What is the AI recommendation reversal rate? Is it so low that human review is effectively nominal?                                | Operational statistics; post-deployment monitoring data |
| **Independence**           | Are overseers free from incentive structures that reward alignment with AI recommendations?                                        | Performance metrics; KPIs affecting overseers           |
| **Explanation capability** | Can overseers explain AI decisions to affected individuals in a way that enables contestation?                                     | Art. 13 information; explanation tooling                |

**Oversight adequacy classification:**

| Finding    | Meaning                                                                                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ADEQUATE` | Human oversight is meaningful and protective in this deployment context                                                                                     |
| `NOMINAL`  | Human oversight exists in form but is ineffective in practice (automation bias, time pressure, authority gap); flag as MEDIUM rights risk under Dimension H |
| `ABSENT`   | Required human oversight is not implemented; flag as HIGH rights risk; deployment should not proceed without remediation                                    |

---

### Step 9: Stakeholder Consultation Record

Document the consultation process, or identify the gap if consultation was not conducted.

**Consultation framework:**

1. **Who to consult** (Recital 96 guidance): Representatives of groups likely to be affected; civil society organisations; independent fundamental rights experts; trade unions (for employment AI); disability organisations (where persons with disabilities are affected); child rights organisations (where children are affected).

2. **Consultation methods**: Structured interviews; written submission periods; focus groups; public consultation; engagement with existing advocacy or representative bodies.

3. **Documentation required**:
   - Names/descriptions of groups consulted (appropriately anonymised)
   - Dates and format of consultation
   - Summary of concerns raised
   - How concerns were addressed in the FRIA or deployment design
   - Where concerns could not be addressed: documented reasoning

4. **If consultation was not conducted**: Document the reason and assess whether this constitutes a material gap. For high-impact systems (MEDIUM or HIGH overall rights impact), absent consultation should be flagged as a significant FRIA quality deficit.

---

### Step 10: Remediation Framework

For each MEDIUM or HIGH severity rights impact finding, produce a remediation record:

| Field                              | Content                                                               |
| ---------------------------------- | --------------------------------------------------------------------- |
| **Finding ID**                     | FRIA-[system]-[dimension]-[number] (e.g., FRIA-CreditAI-D-01)         |
| **Charter basis**                  | Specific Charter article(s)                                           |
| **Severity**                       | MINIMAL / LOW / MEDIUM / HIGH                                         |
| **Rights impact description**      | Specific harm to identified persons or groups                         |
| **Evidence basis**                 | Provider documentation, testing data, consultation findings           |
| **Proposed mitigation**            | Specific, actionable mitigation (not generic "add oversight")         |
| **Alternative considered**         | Less rights-intrusive alternatives assessed                           |
| **Responsible party**              | Named role or team responsible for implementation                     |
| **Implementation deadline**        | Date by which mitigation must be in place before deployment           |
| **Verification evidence**          | What evidence will demonstrate the mitigation is effective            |
| **Residual risk after mitigation** | MINIMAL / LOW (acceptable) or MEDIUM / HIGH (requires further action) |
| **Escalation path**                | Who approves the residual risk; what governance process applies       |

---

### Step 11: DPIA Cross-Reference and Integration (Article 27(4))

If a DPIA has been or will be conducted, produce an integration record per Art. 27(4):

| DPIA Element                                       | FRIA Coverage                      | Integration Action                                           |
| -------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| Processing purpose (GDPR Art. 6)                   | Charter Art. 8 — legal basis       | Cross-reference DPIA legal basis; do not duplicate           |
| Data subjects' rights (GDPR Arts. 12-22)           | Charter Art. 47 — effective remedy | Extend DPIA rights analysis to full Charter Art. 47 scope    |
| Risk to rights and freedoms (GDPR Art. 35(1))      | Charter Arts. 7-8 only             | Ensure FRIA covers full Charter scope beyond privacy         |
| Necessity and proportionality (GDPR Art. 35(7)(b)) | Charter Art. 52(1) proportionality | Align DPIA necessity analysis with FRIA proportionality test |
| Risk management measures (GDPR Art. 35(7)(d))      | FRIA Dimension H — remedy          | Cross-reference; FRIA extends to all rights dimensions       |

**Integrated document option:** Per Art. 27(4), the FRIA and DPIA may be consolidated into a single integrated document. Label the integrated document clearly: "Integrated DPIA and Fundamental Rights Impact Assessment — GDPR Article 35 and EU AI Act Article 27."

If integration is elected, the integrated document must satisfy both GDPR Art. 35(7) and AI Act Art. 27(1) mandatory content requirements. Use the output template in Step 12 with the DPIA Annex structure.

---

### Step 12: Apply Quality Frameworks

Before drafting the final FRIA document, apply all three quality frameworks:

#### 12a. Citation Quality Gates

Run these five gates silently for every legal reference before including it in the FRIA:

| Gate           | Rule                                                                         | Fail Action                       |
| -------------- | ---------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every Charter or AI Act claim cites the specific article                     | Add citation or mark [UNVERIFIED] |
| **Format**     | All citations follow EUR-Lex or official Charter format                      | Fix format                        |
| **Currency**   | Every cited provision checked against current AI Act text (post-amendments)  | Flag [CHECK CURRENCY]             |
| **Domain**     | Analysis stays within EU law scope; no extrapolation to non-EU jurisdictions | Remove or flag                    |
| **Confidence** | Uncertainty explicitly stated                                                | Add confidence qualifier          |

#### 12b. Self-Interrogation for HIGH Severity Findings

For any finding classified as HIGH rights impact, apply this three-pass review:

**Pass 1 — Legal Chain Integrity**: Does the rights-impact conclusion follow logically from the Charter article and the specific AI deployment facts? Would a fundamental rights expert or court reach the same conclusion?

**Pass 2 — Completeness**: Have all relevant Charter provisions been considered for this finding? Are there regulatory dimensions (sector-specific law, Member State law) not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that the rights impact is less severe than classified? What would the deployer's counsel say? Under what circumstances might the risk be acceptable?

If any pass reveals a material weakness in the classification, revise before finalising.

#### 12c. Confidence Scoring

| Level        | Range     | Meaning                                        | Action                                       |
| ------------ | --------- | ---------------------------------------------- | -------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled Charter/AI Act interpretation          | State with confidence                        |
| **High**     | 0.80-0.94 | Strong authority, minor interpretive questions | State with brief caveat                      |
| **Probable** | 0.60-0.79 | Good arguments; regulatory guidance pending    | State with reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuine uncertainty; evolving guidance         | Flag for professional review with both sides |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                        | Do not assert; flag [UNCERTAIN]              |

Apply confidence scoring to all HIGH severity findings and all proportionality conclusions.

---

### Step 13: Draft and Deliver the FRIA Document

Structure the final FRIA as specified in the Output Format Template (see below). Ensure:

1. All Art. 27(1)(a)-(f) mandatory elements are present and substantively addressed
2. All MEDIUM and HIGH findings have remediation records (Step 10)
3. The proportionality conclusion is clearly stated (Step 6, Dimension I)
4. The human oversight adequacy conclusion is stated (Step 8)
5. The DPIA integration record is complete if applicable (Step 11)
6. The stakeholder consultation record is complete or gaps are noted (Step 9)
7. The Glass Box audit trail is appended (see Quality Frameworks)
8. Notification obligation is noted (Art. 27(3)) with MSA contact reference

**Notification obligation reminder:** After completing the FRIA, the deployer must notify
the competent market surveillance authority using the AI Office template (Art. 27(3)).
If the template has not yet been published, note this and confirm the MSA contact for
notification when the template is released [VERIFY: AI Office template publication status].

**EU AI database registration check (Art. 49):** Before deployment, confirm the AI
system is registered in the EU AI database. If not registered, the deployer must not
deploy and must inform the provider or distributor. Reference the registration in the FRIA.

---

## Severity Classification

Classify each rights dimension finding:

| Level       | Meaning                                                                                                                  | Threshold                                                                                                  | Action                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **MINIMAL** | Rights engagement is negligible; no material impact identified                                                           | Impact on an identifiable group is theoretical or demonstrably remote                                      | Document; no mitigation required                                                                 |
| **LOW**     | Rights engagement is marginal; impact is minor and mitigable                                                             | Impact affects a small number of individuals; existing safeguards are adequate                             | Document; verify safeguards are in place                                                         |
| **MEDIUM**  | Rights engagement is material; impact affects identifiable groups and may be unlawful without mitigation                 | Disparate impact, inadequate oversight, or contestation barriers identified                                | Mitigation required before deployment; remediation record mandatory                              |
| **HIGH**    | Rights engagement is severe; impact may be fundamentally incompatible with Charter rights or rights of vulnerable groups | Direct, serious, or systemic violation of fundamental rights; disproportionate impact on vulnerable groups | **Do not deploy without resolution; escalate to senior governance; external review recommended** |

**Overall FRIA conclusion:**

| Conclusion                   | Meaning                                                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `CLEARED_FOR_DEPLOYMENT`     | All dimensions MINIMAL or LOW; proportionality assessment PROPORTIONATE                                           |
| `DEPLOYMENT_WITH_CONDITIONS` | One or more MEDIUM findings; all mitigations implemented; proportionality PROPORTIONATE WITH CONDITIONS           |
| `DEPLOYMENT_DEFERRED`        | One or more HIGH findings that are pending remediation; deployment must wait for verified mitigation              |
| `DEPLOYMENT_NOT_RECOMMENDED` | Deployment is disproportionate or fundamentally incompatible with Charter rights; recommend redesign or rejection |

---

## Prioritisation Framework

After completing the rights analysis, prioritise findings for governance action:

**Priority 1 — Stop-Ship Issues:** Any `HIGH` severity finding OR a `DISPROPORTIONATE` proportionality conclusion. Deployment must not proceed until these are resolved with verified evidence.

**Priority 2 — Deployment Conditions:** Any `MEDIUM` severity finding with a defined, implementable mitigation that can be completed before deployment. These are conditions for proceeding, not optional improvements.

**Priority 3 — Post-Deployment Monitoring:** Any `LOW` severity finding where risk is accepted and monitored. Set review triggers and monitoring metrics for post-deployment surveillance.

**Priority 4 — Future FRIA Improvements:** Structural gaps (missing consultation, incomplete provider documentation) that should be remediated for the next FRIA cycle.

---

## Anti-Patterns

### Assessment Methodology Anti-Patterns

1. **Treating the FRIA as a DPIA with a different cover page** — The most common failure mode. The DPIA covers Charter Arts. 7-8 only. The FRIA must cover the full Charter. A DPIA-only analysis is a material FRIA failure, not an acceptable shortcut.

2. **Conducting the FRIA after deployment** — Art. 27 requires the FRIA before first use. Post-deployment FRIAs are procedurally defective and expose the deployer to regulatory enforcement. If discovered, the deployer should immediately notify the MSA and remediate.

3. **Delegating FRIA completion to the AI system provider** — The FRIA is a deployer obligation. Providers supply Art. 13 information to inform the deployer's FRIA; they do not conduct it. A provider's own risk management documentation under Art. 9 does not substitute for the deployer's FRIA.

4. **Failing to ask the "zero question"** — The FRIA must include a genuine necessity analysis: could the public interest objective be achieved without AI? Omitting this analysis undermines the fundamental purpose of the FRIA as a rights-protective instrument.

5. **Assessing rights dimensions in isolation without cumulative analysis** — Individual dimension-by-dimension analysis that treats each Charter right as independent misses the compounding and intersectional effects that make AI the most significant rights challenge.

6. **Superficial non-discrimination analysis** — Concluding "we don't use race/gender as input variables, so there is no discrimination risk." The most significant discrimination risks arise from proxy variables, training data bias, and optimisation for aggregate accuracy that produces systematic harm to minority groups.

7. **Treating nominal human oversight as effective** — Documenting that "a human reviews each AI recommendation" without assessing whether the review is genuine. Automation bias, time pressure, and authority gaps can render human oversight ineffective while giving the appearance of compliance.

8. **Excluding affected communities from consultation** — Conducting the FRIA entirely internally without engaging representatives of the populations affected. Recital 96 explicitly encourages consultation; ENNHRI identifies it as essential for effective FRIAs.

9. **One-time assessment without update planning** — Filing the FRIA before deployment and never revisiting it. Art. 27(2) requires update when relevant factors change. Without a defined update schedule and trigger conditions, the FRIA becomes stale.

10. **Assessing harm only at the individual level, missing group and societal impacts** — Art. 27(1)(c) explicitly covers "groups of persons." Societal-level harms (erosion of trust, chilling effects, systemic entrenchment of inequalities) must be assessed alongside individual harms.

### Document Quality Anti-Patterns

11. **Generic FRIA template applied without system-specific tailoring** — A FRIA that could equally apply to any AI system is not a FRIA — it is a compliance template. Every FRIA must reflect the specific AI system, deployment context, affected population, and organisational structure.

12. **Missing Charter Art. 47 analysis (right to effective remedy)** — The most frequently omitted Charter right in practice. If individuals cannot understand, contest, or challenge AI-influenced decisions, this right is directly engaged. Never omit it.

13. **Proportionality analysis absent or superficial** — Stating "deployment is proportionate" without articulating the legitimate aim, evidence of suitability, alternatives considered, and balancing reasoning. Proportionality is the core justificatory framework for rights limitations; it must be substantiated.

14. **Mitigation measures without owners, deadlines, and verification evidence** — Mitigation commitments that say "we will add human oversight" without specifying who, by when, and how effectiveness will be verified are not enforceable governance commitments.

15. **Cross-referencing the DPIA without verifying it covers the full Charter scope** — The DPIA covers Arts. 7-8 only. A FRIA that defers all rights analysis to the DPIA and adds only a brief note on other rights is materially incomplete. The FRIA must genuinely address the non-privacy Charter rights.

16. **Submitting FRIA without cross-referencing the EU AI database registration** — Deployers of Annex III systems must ensure the system is registered before deployment (Art. 49). The FRIA should document the registration status.

17. **Failing to document the notification obligation** — Art. 27(3) requires notification to the market surveillance authority. A FRIA that is completed but never notified is a compliance failure. The FRIA document should include a notification checklist.

18. **Invisible FRIA — no transparency toward affected individuals** — FRIAs are governance documents, but affected individuals have a Charter Art. 47 right to understand AI's role in decisions affecting them. FRIAs should include a public summary and a complaint mechanism description accessible to affected persons.

19. **Insufficient fundamental rights expertise on the FRIA team** — Assigning the FRIA to a technical compliance team without fundamental rights expertise. ENNHRI requires that FRIAs be "performed with fundamental rights expertise." For high-impact systems, an independent human rights expert review is best practice.

20. **FRIA that fails the "would it have changed the deployment decision?" test** — A FRIA that is written after the deployment decision has been made and merely documents that decision cannot function as a rights-protective instrument. If FRIA findings had no influence on deployment design, conditions, or scope, the FRIA failed its purpose.

---

## Writing Standards

Apply plain-language discipline to all FRIA output:

**For regulatory submissions** (shared with market surveillance authority):

- Clear, formal register appropriate for regulatory correspondence
- Active voice: "The system processes applicant data to generate credit scores" not "Applicant data is processed to generate credit scores by the system"
- Short sentences; one legal point per sentence
- Specific Charter articles and AI Act provisions cited, not vague references to "applicable law"
- Confidence qualifiers where interpretive uncertainty exists

**For internal governance** (board, senior management, DPO):

- Same plain-language standards
- Business impact framing alongside rights analysis
- Traffic-light formatting for severity classifications
- Glass Box audit trail appended

**For affected individuals** (public summary):

- Non-technical language accessible to persons without legal training
- Explain what AI does, how it affects them, and what they can do if they disagree
- Complaint mechanism contact details

**Quality gates before delivery:**

1. Does the FRIA address all six mandatory elements of Art. 27(1)(a)-(f)?
2. Is every Charter article finding supported by specific system facts, not generic AI risk?
3. Is proportionality reasoning substantiated or merely asserted?
4. Is every HIGH severity finding assigned to a named owner with a specific deadline?
5. Would an affected individual be able to identify and exercise their contestation right from this document?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current EU AI Office guidance and FRIA template publications (Art. 27(5))
- Search for Member State market surveillance authority designation and contact details
- Search for EDPB and DPA guidance on GDPR-AI Act interplay
- Search for FRA sector-specific guidance on AI and fundamental rights
- Save results to `/tmp/legalcode-fria-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all legal references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Consult official EUR-Lex text for Art. 27 authority
- Use ECNL/DIHR FRIA Guide and FRA 2025 report as interim methodology guidance
- Note any unverified regulatory guidance that may have been published after August 2025

**Trigger for `legalcode-dpia-generator`:** Invoke this skill when a DPIA is required (GDPR Art. 35 trigger) or when the deployer wishes to integrate the FRIA and DPIA into a single document per Art. 27(4). The DPIA generator provides the privacy-rights foundation; this skill extends it to the full Charter.

**Trigger for `legalcode-algorithmic-impact-assessment`:** For comprehensive non-discrimination analysis under Dimension D, invoke the AIA skill to generate fairness metrics, disparate impact testing specifications, and bias root cause analysis. Incorporate AIA findings into the FRIA Dimension D assessment.

---

## Glass Box Audit Trail

Append the following YAML block to every FRIA output:

```yaml
glass_box:
  skill_name: "legalcode-ai-fundamental-rights-impact-assessment"
  version: "1.0"
  date_conducted: "[ISO 8601 date]"
  ai_system_name: "[system name and version]"
  deployer_name: "[deployer organisation]"
  deployer_category: "[FRIA_CATEGORY_A / B / C]"
  annex_iii_category: "[Point 1-8]"
  fria_eligibility_determination: "[FRIA_REQUIRED / NOT_REQUIRED / INSUFFICIENT_FACTS]"
  timing_status: "[PRE_DEPLOYMENT / UPDATE / POST_DEPLOYMENT_DEFECT]"
  overall_fria_conclusion: "[CLEARED / WITH_CONDITIONS / DEFERRED / NOT_RECOMMENDED]"
  charter_articles_assessed:
    - "Art. 1 (dignity)"
    - "Art. 7 (private life)"
    - "Art. 8 (data protection)"
    - "Art. 10 (religion/conscience)"
    - "Art. 11 (expression)"
    - "Arts. 20-23 (equality/non-discrimination)"
    - "Art. 24 (children)"
    - "Art. 25 (elderly)"
    - "Art. 26 (disabilities)"
    - "Arts. 27-31 (labor rights)"
    - "Arts. 34-36 (essential services/health)"
    - "Arts. 41/47 (administration/remedy)"
    - "Art. 48 (presumption of innocence)"
  high_severity_findings: "[number]"
  medium_severity_findings: "[number]"
  proportionality_conclusion: "[PROPORTIONATE / WITH_CONDITIONS / DISPROPORTIONATE]"
  oversight_adequacy: "[ADEQUATE / NOMINAL / ABSENT]"
  dpia_status: "[CONDUCTED / IN_PROGRESS / NOT_STARTED / INTEGRATED]"
  consultation_status: "[CONDUCTED / PLANNED / NOT_CONDUCTED / JUSTIFIED_OMISSION]"
  provider_art13_documentation: "[COMPLETE / PARTIAL / ABSENT]"
  eu_ai_database_registration: "[CONFIRMED / PENDING / UNKNOWN]"
  notification_obligation_noted: "[YES / N/A]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-fria-research.md / Not created]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  self_interrogation_applied_to: "[list of HIGH findings]"
  limitations:
    - "[Any scope limitations, absent provider documentation, consultation gaps]"
  reviewer: "AI-assisted — requires qualified legal and fundamental rights expert review"
```

---

## Output Format Template

Structure the FRIA document as follows. Adapt section headings as appropriate for the specific deployment context. For integrated DPIA/FRIA, append DPIA sections as Annex A.

```markdown
# Fundamental Rights Impact Assessment

## AI Act Article 27 — [Organisation Name]

**Document Reference**: FRIA-[System]-[Date]
**Version**: [1.0 / 2.0]
**Prepared by**: [Role/Team]
**Reviewed by**: [Legal Counsel / Fundamental Rights Expert]
**DPO Consulted**: [Name if applicable]
**Date**: [ISO 8601]
**Next Review Date**: [date or trigger conditions]
**EU AI Database Registration No.**: [if registered]
**Market Surveillance Authority**: [MSA name and contact]

---

## Section 1 — Executive Summary

[3-5 sentences summarising the AI system, its purpose, the overall FRIA conclusion,
and the most significant rights findings and conditions.]

Overall FRIA conclusion: [CLEARED FOR DEPLOYMENT / WITH CONDITIONS / DEFERRED / NOT RECOMMENDED]

Key conditions for deployment (if any):

- [Condition 1 — owner — deadline]
- [Condition 2 — owner — deadline]

---

## Section 2 — FRIA Eligibility Determination

[Reproduce the eligibility determination from Step 3, Gates 1-3.]

Deployer category: [A / B / C]
System scope (Annex III): [Point and category]
Timing status: [Pre-deployment / Update / Post-deployment defect]

---

## Section 3 — AI System Description (Article 27(1)(a) and (b))

**System name and version**: [as registered or described by provider]
**Provider**: [name and contact]
**System function**: [plain-language description of what the AI system does]
**Decision output**: [type of decision or recommendation produced]
**Deployment context**: [specific organisational process; how the AI output is used in practice]
**Intended period of use**: [start date; frequency; duration of each use]
**Human oversight design**: [per provider instructions for use]
**EU AI database registration**: [number / status]

---

## Section 4 — Affected Persons and Groups (Article 27(1)(c))

**Primary affected persons**: [categories of individuals directly subject to AI decisions]
**Secondary affected persons**: [individuals indirectly affected]
**Affected groups including vulnerable groups**:

- [Group 1 — estimated scale — vulnerable group classification]
- [Group 2 — estimated scale — vulnerable group classification]

---

## Section 5 — Rights Impact Analysis (Article 27(1)(d))

### Dimension A — Human Dignity (Arts. 1, 3)

**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Confidence**: [level]
**Key findings**: [specific system-based findings, not generic]
**Evidence**: [provider documentation, testing data, consultation findings relied upon]

### Dimension B — Privacy and Data Protection (Arts. 7, 8)

**DPIA cross-reference**: [document reference / integrated / pending]
**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Confidence**: [level]
**Key findings**: [beyond DPIA scope — non-privacy Arts. 7-8 dimensions]

### Dimension C — Freedom of Thought and Expression (Arts. 10, 11)

**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Confidence**: [level]
**Key findings**: [specific findings]

### Dimension D — Equality and Non-Discrimination (Arts. 20-23)

**AIA findings cross-reference**: [if AIA conducted — reference findings]
**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Confidence**: [level]
**Key findings**: [proxy variables, disparate impact, training data gaps]

### Dimension E — Rights of Specific Groups (Arts. 24, 25, 26)

**Vulnerable groups affected**: [list]
**Classification**: [MINIMAL / LOW / MEDIUM / HIGH per group]
**Key findings**: [per group]

### Dimension F — Labor Rights (Arts. 27-31)

**Applies**: [YES / NO — if no, state basis]
**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Key findings**: [if applicable]

### Dimension G — Essential Services and Social Rights (Arts. 34-36)

**Applies**: [YES / NO]
**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Key findings**: [if applicable]

### Dimension H — Right to Good Administration and Effective Remedy (Arts. 41, 47)

**Classification**: [MINIMAL / LOW / MEDIUM / HIGH]
**Confidence**: [level]
**Key findings**: [contestation access, explanation capability, complaint mechanisms]
**Art. 48 supplement** (law enforcement/justice AI only): [findings]

---

## Section 6 — Vulnerable Group and Cumulative Impact Assessment

**Vulnerable groups assessed**: [list from Step 7]
**Intersectionality findings**: [compound effects identified]
**Cumulative AI-on-AI impact**: [co-deployed AI systems assessed; cumulative findings]
**Societal-level impact**: [if identified]

---

## Section 7 — Human Oversight Adequacy (Article 27(1)(e))

**Oversight adequacy conclusion**: [ADEQUATE / NOMINAL / ABSENT]
**Competence assessment**: [findings]
**Authority assessment**: [findings]
**Information adequacy**: [findings]
**Reversal rate (if available)**: [data / unavailable]
**Gaps identified**: [specific deficiencies and required improvements]

---

## Section 8 — Proportionality Assessment (Article 52(1) Charter)

**Legitimate aim**: [stated aim and legal basis]
**Suitability**: [evidence of effectiveness; validation data; "zero question" assessment]
**Necessity**: [alternatives considered; rejection reasoning; scope limitation]
**Proportionality stricto sensu**: [benefit/cost distribution; vulnerable group weighting]
**Proportionality conclusion**: [PROPORTIONATE / WITH CONDITIONS / DISPROPORTIONATE]
**Conditions (if any)**: [specific conditions]

---

## Section 9 — Risk Materialisation Measures (Article 27(1)(f))

**Complaint mechanism**: [description; how to access; response timeframe]
**Internal governance arrangements**: [responsible role; escalation path; oversight body]
**Incident response triggers**: [what constitutes a rights incident; reporting chain]
**Affected individual notification**: [how individuals are informed of AI use and rights]

---

## Section 10 — Remediation Roadmap

| Finding ID | Charter Basis | Severity | Impact        | Mitigation | Owner  | Deadline | Verification |
| ---------- | ------------- | -------- | ------------- | ---------- | ------ | -------- | ------------ |
| [ID]       | [Art.]        | [level]  | [description] | [action]   | [role] | [date]   | [evidence]   |

---

## Section 11 — Stakeholder Consultation Record

**Consultation conducted**: [YES / NO / PARTIAL]
**Groups consulted**: [list]
**Consultation dates and format**: [dates; methods]
**Summary of concerns raised**: [substantive concerns]
**How concerns were addressed**: [FRIA changes; design changes; accepted residual risk]
**Gaps and justification** (if consultation not conducted): [reasoning]

---

## Section 12 — DPIA Integration Record (Article 27(4))

**DPIA reference**: [document title; date; version]
**Integration approach**: [separate complementary documents / single integrated document]
**DPIA rights finding**: [HIGH / MEDIUM / LOW]
**FRIA complement**: [specific Charter rights covered by FRIA beyond DPIA scope]

---

## Section 13 — FRIA Notification and Registration

**Notification obligation**: Article 27(3) — notify market surveillance authority using AI Office template
**Market surveillance authority**: [MSA name; contact; notification address]
**AI Office template status**: [available / not yet published — verify before notification]
**EU AI database registration**: [confirmed / pending / system not yet registered]

---

## Section 14 — FRIA Update Schedule

**Next mandatory review date**: [date or event trigger]
**Update triggers**:

- Material modification of AI system
- Change in deployment context or affected population
- New risk information from post-market monitoring
- Provider notification of system change
- Market surveillance authority request
- Annual review (best practice)

**Responsible role for monitoring triggers**: [named role]

---

## Section 15 — Glass Box Audit Trail

[Reproduce the Glass Box YAML block from the Quality Frameworks section]
```

---

## Localization Notes

While the FRIA obligation is EU-wide, Member State variations affect FRIA implementation:

**[JURISDICTION-SPECIFIC]** Investigate and apply local rules for:

- **National market surveillance authority** designated for the relevant sector (digital, healthcare, finance, employment)
- **Data protection authority** cross-referencing (some DPAs have indicated they will cooperate with AI Act supervision)
- **Public law body definition** under national administrative law (varies significantly; e.g., France: public établissement; Germany: Behörde / Körperschaft des öffentlichen Rechts)
- **Sector-specific guidance** from national financial supervisors (BaFin, AMF, FCA post-Brexit does not apply), healthcare authorities, and judicial councils
- **National AI sandbox** participation (Arts. 57-63) may affect applicable requirements
- **Language requirements** for public sector FRIA documents (some Member States may require documentation in the national language for submission to national MSAs)

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis. Research basis:

- EU AI Act Regulation (EU) 2024/1689, Arts. 7, 26, 27, 49, 71 (EUR-Lex official text)
- EU Charter of Fundamental Rights (2000/C 364/01), Arts. 1-54
- ECNL + Danish Institute for Human Rights, "A Guide to Fundamental Rights Impact Assessments under the EU AI Act" (2024/2025)
- FRA, "Assessing High-risk Artificial Intelligence: Fundamental Rights Risks" (2025)
- FRA, "Getting the Future Right – Artificial Intelligence and Fundamental Rights" (2020)
- ENNHRI Statement on Ensuring Effective FRIAs under the EU AI Act (April 2025)
- EDPB Opinion 28/2024 on AI Models and Data Protection (December 2024)
- Freshfields Technology Quotient, "EU AI Act unpacked #6: Fundamental rights impact assessment"
- A&O Shearman, "Zooming in on AI #13: EU AI Act – Focus on FRIA"
- CEDPO Micro-Insight Paper on FRIAs
- AI Act Service Desk (ai-act-service-desk.ec.europa.eu), Articles 26, 27; Recital 96
- ScienceDirect: "The Fundamental Rights Impact Assessment (FRIA) in the AI Act: Roots, legal obligations and key elements"
- Pattern libraries: `legalcode-algorithmic-impact-assessment`, `legalcode-eu-ai-act-high-risk-compliance`, `legalcode-dpia-generator`
- 2-agent research pipeline (structural-analyst + legal-research-agent)

All statutory references carry hallucination risk — verify against EUR-Lex before relying on them.
