---
name: legalcode-algorithmic-impact-assessment
description: Conduct comprehensive algorithmic impact assessments (AIAs) for AI systems that make or substantially
  influence consequential decisions affecting individuals. Use when deploying AI systems subject to regulatory
  transparency or accountability requirements; preparing for EU AI Act Article 27 Fundamental Rights Impact
  Assessment (FRIA); conducting NYC LL 144 annual bias audits; satisfying Colorado SB 24-205 pre-deployment
  impact assessment obligations; completing California CPRA ADMT risk assessments; assessing employment,
  credit, housing, healthcare, insurance, education, or criminal justice automated decision systems for
  disparate impact; or building an organizational algorithmic impact assessment program.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conduct comprehensive algorithmic impact assessments (AIAs) for AI systems that make or substantially influence consequential decisions affecting individuals. Covers system classification and purpose documentation, training data and data governance analysis, fairness metrics evaluation (demographic parity / impact ratio, equalized odds, calibration / predictive parity, individual fairness, counterfactual fairness), disparate impact testing across all legally relevant protected classes, proxy feature and protected characteristic inference analysis, bias detection and root cause analysis, transparency and explainability audit (model card completeness, LIME/SHAP/feature importance), human oversight mechanism assessment, appeal and contestation procedure review, and ongoing monitoring framework design. Aligned with EU AI Act (Regulation 2024/1689) Articles 9, 10, 14, 27, and Annex III high-risk system categories; NYC Local Law 144 bias audit requirements for automated employment decision tools; Colorado AI Act (SB 24-205, effective June 30 2026) consequential decision impact assessment obligations; California CPRA Automated Decisionmaking Technology (ADMT) Regulations (effective January 1 2026); NIST AI Risk Management Framework (AI RMF 1.0) MAP and MEASURE functions; IEEE 7003-2024 algorithmic bias considerations; and ISO/IEC TR 24027 bias identification guidance. Integrates EEOC Title VII adverse impact guidance, CFPB ECOA adverse action and less-discriminatory-alternative requirements, FTC Section 5 unfairness doctrine, and Fair Housing Act / Fair Credit Reporting Act overlays. Use when deploying AI systems subject to regulatory transparency or accountability requirements; preparing for EU AI Act Article 27 Fundamental Rights Impact Assessment (FRIA); conducting NYC LL 144 annual bias audits; satisfying Colorado SB 24-205 pre-deployment impact assessment obligations; completing California CPRA ADMT risk assessments; assessing employment, credit, housing, healthcare, insurance, education, or criminal justice automated decision systems for disparate impact; or building an organizational algorithmic impact assessment program. Produces comprehensive AIA reports with fairness metrics scorecards, disparate impact findings, bias root cause analysis, transparency audit, human oversight evaluation, remediation roadmaps, compliance mapping, and Glass Box audit trails suitable for regulatory submission and internal governance.


# Legalcode Algorithmic Impact Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted algorithmic impact assessment.
> It does not constitute legal advice, regulatory compliance certification, or authorization to
> deploy an AI system. All outputs require review by qualified legal counsel, AI governance
> specialists, and domain experts before any deployment decision. Applicable regulations (EU AI
> Act, NYC Local Law 144, Colorado SB 24-205, California CPRA ADMT, NIST AI RMF) are recent,
> actively evolving, and subject to ongoing regulatory interpretation — verify current requirements
> before relying on any provision described here. Technical fairness metrics themselves carry
> model risk: no single metric captures all dimensions of algorithmic fairness, and metrics can
> conflict with each other when base rates differ across demographic groups. Statutory, regulatory,
> case-law, and technical references cited from training-data knowledge carry hallucination risk —
> verify against authoritative primary sources before relying on them. Mark all unverified
> references [VERIFY].

---

## Purpose and Scope

This skill conducts systematic algorithmic impact assessments of AI systems that make or
substantially influence decisions with material legal or practical consequences for individuals
and groups. It identifies, quantifies, and supports remediation of risks of unfair, discriminatory,
opaque, or inadequately overseen automated decision-making.

**Covers:**

- AI system type classification and consequential decision category determination
- Applicable regulatory framework identification (EU AI Act Annex III, NYC LL 144, Colorado SB 24-205,
  California CPRA ADMT, NIST AI RMF, EEOC, CFPB, FHA, FTC)
- Training data governance analysis (representativeness, completeness, bias examination)
- Fairness metrics analysis across ten assessment dimensions:
  1. Demographic parity and group-level impact ratios
  2. Equalized odds and error rate parity
  3. Calibration and predictive parity
  4. Individual fairness and decision consistency
  5. Proxy feature and protected characteristic inference
  6. Transparency and model card completeness
  7. Human oversight and appeal procedure adequacy
  8. Ongoing monitoring and feedback loop prevention
  9. Sector-specific and vulnerable group protections (conditional)
  10. Disparate impact and intersectional discrimination (conditional)
- Protected class coverage mapping (US federal, NYC, Colorado, California, EU Charter, GDPR Art. 9)
- Bias root cause analysis (training data, feature engineering, model architecture, deployment context,
  feedback loops)
- Transparency and explainability audit (LIME, SHAP, model card, decision explanation)
- Human oversight design and appeal mechanism review (EU AI Act Art. 14, NYC LL 144, Colorado SB 24-205)
- EU AI Act Article 27 Fundamental Rights Impact Assessment (FRIA) preparation
- NYC Local Law 144 bias audit documentation support
- Colorado AI Act impact assessment documentation
- California CPRA ADMT risk assessment documentation
- Remediation roadmap with prioritized mitigation options and deployment gates
- Ongoing monitoring plan design

**Does not:**

- Provide definitive legal determination of algorithmic discrimination (only qualified counsel can)
- Execute fairness metric computation (the assessor supplies data; this skill identifies applicable
  metrics, interprets results, and supports analysis)
- Replace human domain experts, affected community consultation, or regulatory review
- Guarantee regulatory compliance or authorize deployment
- Assess AI systems that do not influence consequential decisions (purely informational outputs with no
  decision weight)
- Apply any single jurisdiction's law as universal — this is a jurisdiction-agnostic framework with
  [JURISDICTION-SPECIFIC] markers throughout

**Related skills:**

- `legalcode-eu-ai-act-high-risk-compliance` — EU AI Act high-risk system conformity assessment
  (Articles 9–17, conformity procedures, CE marking, technical documentation)
- `legalcode-ai-governance-framework-builder` — Organizational AI governance framework aligned with
  ISO/IEC 42001:2023 and NIST AI RMF
- `legalcode-dpia-generator` — GDPR Article 35 Data Protection Impact Assessment (complements FRIA
  under EU AI Act Art. 27)
- `legalcode-ai-acceptable-use-policy` — Organizational AI acceptable use policy drafting

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The AIA framework applies across jurisdictions. Which
regulatory obligations apply to any particular system depends on where the system is deployed,
who it affects, the deployer's legal category, and the decision domain.

[JURISDICTION-SPECIFIC] When localizing, verify and apply:

**European Union — EU AI Act (Regulation (EU) 2024/1689)**

- Application timeline: Art. 5 prohibited practices: February 2, 2025 | GPAI obligations: August 2,
  2025 | Full high-risk system provisions (including Art. 27 FRIA): August 2, 2026
- Art. 5: Prohibited practices (biometric categorization by sensitive characteristics, social scoring,
  real-time remote biometric identification in public spaces without authorization)
- Arts. 9–15: Core high-risk system requirements (risk management, data governance, documentation,
  logging, transparency, human oversight, accuracy)
- Art. 10(5): Targeted exception permitting processing of GDPR Art. 9 special-category data strictly
  for bias monitoring and correction in high-risk AI systems
- Art. 14: Human oversight design — systems must allow overseers to understand, monitor, and override
- Art. 26: Deployer obligations — implement instructions of use; assign qualified oversight; monitor
- Art. 27: FRIA — applies to bodies governed by public law AND private entities providing public
  services AND deployers of Annex III credit/insurance systems — must be completed BEFORE deployment
- Art. 29: Deployer obligations — ongoing monitoring; report unforeseen risks to provider
- Annex III: Eight high-risk categories (biometric; critical infrastructure; education; employment;
  essential private/public services; law enforcement; migration; justice)
- Annex IV: Technical documentation 13-element checklist
- Art. 99 Penalties: Up to EUR 35 million / 7% worldwide annual turnover for Art. 5 violations;
  EUR 30 million / 6% for high-risk system violations [VERIFY exact tier for FRIA/Art. 27 failures]
- Cross-reference: GDPR Art. 35 DPIA requirements apply alongside or separately from FRIA

**United States — NYC Local Law 144 (Effective: January 1, 2023; Enforcement: July 5, 2023)**

- Applies to employers and employment agencies using AEDTs to screen candidates or employees for
  employment or promotion in New York City
- Annual independent bias audit required (auditor must be impartial and have no direct financial interest)
- Audit must calculate: selection rate, scoring rate, and impact ratio by sex, race/ethnicity, and
  intersectional (sex × race/ethnicity) categories using EEO-1 reporting categories
- Protected demographic categories with less than 2% of data may be excluded but must be reported
- Candidate notification: at least 10 business days before AEDT use; must disclose what the tool
  evaluates and instructions for requesting an alternative selection process
- Employer must publish bias audit summary on website; must retain compliance records
- Enforcement: DCWP; civil penalties USD $375–1,500 per violation per day
- As of late 2025, formal enforcement actions sparse — private litigation under NYC Human Rights Law
  is the primary current legal risk vector

**United States — Colorado AI Act (SB 24-205, effective June 30, 2026)**

- Applies to developers and deployers of "high-risk AI systems" — systems making or substantially
  contributing to "consequential decisions" in employment, education, financial services, essential
  government services, healthcare, housing, legal services, and insurance
- Deployers must: implement a risk management policy and program (NIST AI RMF, ISO 42001, or
  equivalent); complete an impact assessment before deployment, annually, and within 90 days of
  material modification; notify consumers when a high-risk AI system is used in a consequential
  decision; provide opportunity to correct inaccurate data; provide appeal with human review
- Developer obligations: use reasonable care to protect against algorithmic discrimination; disclose
  known risks to deployers; disclose identified risks of algorithmic discrimination to CO AG within
  90 days of discovery
- Enforcement: Colorado Attorney General; no private right of action [VERIFY penalty amounts under
  Colorado CCPA enforcement provisions applicable to SB 24-205]
- Safe harbor: deployers presumed to use reasonable care if they (a) implement qualifying risk
  management program, (b) complete required impact assessments, (c) conduct annual deployment reviews,
  (d) comply with notice requirements

**United States — California CPRA Automated Decisionmaking Technology (ADMT) Regulations**

- Regulations finalized September 23, 2025; effective January 1, 2026; significant-decisions
  compliance required by January 1, 2027
- "Significant decisions" include employment, education, financial services, housing, healthcare
- Consumer rights: opt out of ADMT for significant decisions; request information about ADMT use;
  appeal adverse decisions with qualified human review; receive explanation of how ADMT was used
- Risk assessments required for ADMT use in significant decisions — must be completed before use,
  updated on significant changes, retained for 3+ years
- [VERIFY: Current CPPA enforcement guidance and whether additional California AI legislation
  (successor to AB 2930) was enacted in 2025–2026 California legislative session]

**Canada — AIDA (Artificial Intelligence and Data Act)**

- STATUS: AIDA (contained in Bill C-27) died on the order paper on January 6, 2025 when Parliament
  was prorogued following Prime Minister Trudeau's resignation. AIDA has NOT been enacted into law
  as of the date this skill was created (March 2026). Include AIDA-aligned guidance as best practice
  but do NOT represent AIDA compliance as a legal obligation.
- Monitor for re-introduction; the AIDA framework remains an influential model for Canadian AI
  governance best practice
- [VERIFY: Current status of Canadian federal AI regulation and any successor legislation or policy]

**United States — Federal Frameworks (Voluntary and Regulatory)**

- EO 14110 (Safe, Secure, Trustworthy AI, Oct 2023): Rescinded by President Trump on January 20, 2025. No longer a binding directive. Agency guidance documents produced under EO 14110 remain
  available as voluntary best-practice resources.
- NIST AI RMF 1.0 (January 2023): Voluntary framework; widely adopted as industry standard for AI
  risk management. Four functions: GOVERN, MAP, MEASURE, MANAGE. MAP and MEASURE functions directly
  address AIA methodology.
- NIST SP 1270 (Bias in AI, March 2022): Foundational guidance on identifying and managing bias.
  Defines systemic bias (data/design), statistical/computational bias (sampling/measurement), and
  cognitive bias (human judgment).
- EEOC May 2023 Technical Assistance (Title VII and AI Employment Selection): Confirms algorithmic
  selection tools constitute "selection procedures" under UGESP; four-fifths rule applies; employer
  bears full Title VII responsibility for discriminatory vendor tools.
- CFPB May 2022 Circular: Adverse action notice requirements apply to AI credit decisions; specific
  reasons must be provided even for black-box models.
- CFPB LDA Obligation: Fair lending compliance requires searching for Less Discriminatory Alternatives
  (LDAs) when using AI credit models [VERIFY current CFPB leadership priorities under 2025
  administration change].
- FTC Section 5 Unfairness: Applies to discriminatory AI systems (Rite Aid, December 2023 — FTC's
  first use of Section 5 unfairness against allegedly discriminatory AI; facial recognition with
  racially disparate misidentification). Algorithmic disgorgement (forced deletion of AI models and
  training data) is an available remedy.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked with **⟁ CLARIFY**.
At each CLARIFY point, present structured options with explanatory context (why the answer matters).
If the user has already provided the information, skip the question and proceed.

For batch or non-interactive runs, proceed with the following defaults and state them explicitly:

- System type: As described in the input
- Decision context: As described in the input
- Jurisdiction: Jurisdiction-agnostic assessment with applicable regulatory markers noted
- Risk tolerance: Balanced (apply standard fairness thresholds; escalate material disparities)

---

## Workflow

### Step 1: Accept Input and System Description

Accept the AI system in any of these formats:

- **Model documentation**: Technical model card, architecture description, vendor system sheet
- **System description**: Textual description of the system purpose, inputs, outputs, and decision context
- **Deployment data**: Historical performance records, prediction logs, outcome data
- **Code or specification**: Training pipeline, inference logic, feature engineering description
- **Audit or bias report**: Prior independent assessment or compliance report

If no documentation is provided, prompt the user to supply at minimum a system description
before proceeding.

### Step 2: Gather Context

⟁ CLARIFY — Before beginning the assessment, ask these questions (skip any already answered):

**1. AI System Type**
What type of AI system is this?

- Classification (predicts a category — e.g., hire/no-hire, credit approval, fraud/not fraud)
- Regression (predicts a continuous value — e.g., credit score, risk score, pricing)
- Ranking (orders items — e.g., candidate ranking, search results, recommendation feed)
- Generative (creates content — e.g., automated decision letters, risk narrative summaries)
- Ensemble / hybrid (multiple component models)
  _Why this matters: Different AI types carry different fairness risks. Classification systems
  require disparate impact rate analysis; ranking systems require position bias assessment; regression
  systems require calibration analysis by group._

**2. Decision Context**
What consequential decision does this AI system make or substantially influence?

- Employment (hiring, promotion, termination, performance monitoring, compensation)
- Credit/lending (approval, pricing, terms, credit limits, adverse action)
- Insurance (underwriting, pricing, claims)
- Education (admissions, scholarships, academic tracking, recommendations)
- Housing (tenant screening, rental approval, mortgage underwriting)
- Healthcare (triage, diagnosis support, treatment recommendations, benefits authorization)
- Criminal justice (risk assessment, pretrial release, sentencing, supervision)
- Essential public/government services (benefits, housing assistance, public safety)
- Content/platform (content moderation, content recommendation)
- Other (describe)
  _Why this matters: Each domain has specific protected characteristics, regulatory overlays (EEOC for
  employment, CFPB for credit, HUD/FHA for housing), and relevant fairness metrics._

**3. Automation Level**
What is the human role in the final decision?

- Fully automated: AI makes the final decision; human role is post-hoc review only
- Assisted: AI recommends; human reviews the recommendation and makes the final decision
- Informational: AI provides supporting analysis; human may disregard
- Advisory: AI suggests; human retains full discretion
  _Why this matters: Fully automated decisions trigger mandatory appeal rights and stronger human
  oversight obligations under EU AI Act Art. 14, Colorado SB 24-205, and California CPRA ADMT._

**4. Affected Population**
Who does this system affect and at what scale?

- Internal employees only (under 500 people)
- Organization-wide employees (over 500 people)
- Customers or applicants regionally or nationally
- Public users without specific targeting
- Vulnerable groups (youth, elderly, persons with disabilities, protected minorities, low-income)
  _Why this matters: Vulnerable group exposure triggers stricter requirements. Large scale amplifies
  harm from any disparity._

**5. Available Data**
What data do you have for the assessment?

- Full deployment data with outcomes (ideal for fairness metric calculation)
- Model documentation and training/test data (pre-deployment assessment)
- Model description only (no data — theoretical assessment)
- Vendor system (limited transparency; black-box assessment)
  _Why this matters: Determines which fairness metrics can be calculated vs. inferred, and the
  confidence level achievable for each assessment dimension._

**6. Primary Regulatory Driver**
What is the primary legal or governance reason for this assessment?

- EU AI Act (Annex III high-risk system — Art. 27 FRIA obligation)
- NYC Local Law 144 (employment tool — annual bias audit obligation)
- Colorado AI Act SB 24-205 (consequential decision — pre-deployment impact assessment)
- California CPRA ADMT Regulations (significant decision — risk assessment)
- EEOC / Title VII (employment adverse impact analysis)
- CFPB / ECOA (credit adverse impact and LDA analysis)
- FHA / Fair Housing (housing disparate impact)
- NIST AI RMF (internal governance)
- Multiple simultaneous regulatory obligations (list)
- Internal AI governance / best practice (no specific regulatory deadline)
  _Why this matters: Sets the baseline documentation requirements, protected classes, and
  fairness metric standards for the assessment._

**7. Organizational Playbook**
Does your organization have an AI governance policy, risk classification framework, or bias standard?

- Yes, with defined fairness thresholds (provide or describe)
- Yes, general policy (no specific thresholds)
- No, use regulatory baseline
  _Why this matters: If defined thresholds exist, I will assess against them and note deviations.
  Without a playbook, I will use regulatory minimums and best-practice standards._

### Step 3: Load Organizational AI Risk Framework

Check for the organization's AI governance playbook or bias mitigation standards
(e.g., `ai-governance.local.md`, risk classification policy, bias standard document).

If found, extract:

- **Fairness thresholds** — Organization's acceptable disparity level for each metric
- **Protected classes** — Organization's full list of characteristics to assess (may exceed legal minimum)
- **Escalation triggers** — What disparity level or finding type requires leadership sign-off
- **Risk tolerance** — Conservative / balanced / progressive

If no playbook is found, proceed with regulatory minimums and state explicitly:
_"No organizational playbook found. Assessment uses applicable regulatory standards (EU AI Act,
EEOC four-fifths rule, NYC LL 144 impact ratio requirements) as the baseline. All thresholds are
regulatory minimums, not organizational positions."_

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Research applicable legal frameworks and authoritative guidance.

**With legalcode-mcp connected (preferred):**

Search for:

- Current EU AI Act provisions (Arts. 9, 10, 14, 27, Annex III, Annex IV)
- EU AI Office guidance on FRIA requirements and Annex III high-risk determination
- NYC DCWP current guidance and interpretations on Local Law 144
- Colorado AG guidance on SB 24-205 algorithmic impact assessment requirements
- California CPPA guidance on ADMT regulations and risk assessment requirements
- EEOC Technical Assistance on AI and Title VII (May 2023); CFPB May 2022 Circular on adverse action
- FTC enforcement guidance (Rite Aid consent order; algorithmic disgorgement standard)
- Enforcement actions by national DPAs on GDPR Art. 22 automated decision-making (CJEU C-203/22)
- Relevant case law on disparate impact in employment (Title VII), credit (ECOA), housing (FHA)
- Industry-specific guidance (NAIC insurance AI principles; ONC healthcare AI; FDA medical AI)
- IEEE 7003-2024 and ISO/IEC TR 24027 technical standards

Save findings to: `/tmp/aia-regulatory-authority.md`

**Without legalcode-mcp:**

Mark all regulatory citations with [VERIFY]. Note in Glass Box: `external_tools_used: "None — manual
verification required"`. Include notice: "All regulatory citations require independent verification by
qualified legal counsel before deployment decisions."

Authoritative sources for manual verification:

- EU AI Act text: eur-lex.europa.eu (Regulation (EU) 2024/1689)
- EU AI Office: digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- NYC LL 144: nyc.gov/site/dca/about/automated-employment-decision-tools.page
- Colorado SB 24-205: leg.colorado.gov/bills/sb24-205
- California CPPA ADMT: cppa.ca.gov
- NIST AI RMF: nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- EEOC May 2023 Technical Assistance: eeoc.gov
- CFPB May 2022 Circular: consumerfinance.gov

### Step 5: System Type and Regulatory Scope Determination

Before analyzing fairness dimensions, confirm the regulatory scope of the assessment.

**5a. EU AI Act High-Risk Classification**

If the system may be subject to EU AI Act:

[JURISDICTION-SPECIFIC — EU] Check Annex III categories:

1. Biometric identification and categorization of persons
2. Critical infrastructure management
3. Education and vocational training (admissions, assessment, tracking)
4. Employment and workers management (recruitment, screening, promotion, termination, task allocation,
   performance monitoring)
5. Essential private services (creditworthiness, life/health insurance) and essential public services
   (benefits, emergency services)
6. Law enforcement (crime prediction, profiling, risk assessment of individuals)
7. Migration, asylum, border control
8. Administration of justice and democratic processes

If an Annex III category applies: the Art. 27 FRIA obligation is triggered for qualifying deployers
(public bodies, private entities providing public services, credit/insurance deployers under Annex III).

⟁ CLARIFY — "Is the deployer (a) a body governed by public law, (b) a private entity providing
services generally available to the public (banking, insurance, utility), or (c) a private employer
or business?" Answer determines FRIA obligation.

**5b. NYC LL 144 Scope Confirmation**

[JURISDICTION-SPECIFIC — NYC] Confirm AEDT scope:

- Does the system issue a score, classification, or recommendation?
- Is the output used to substantially assist or replace discretionary employment decisions?
- Are affected persons candidates or employees in New York City?

If all three: NYC LL 144 bias audit obligation applies.

**5c. Colorado SB 24-205 Scope Confirmation**

[JURISDICTION-SPECIFIC — Colorado, effective June 30, 2026]

- Is the system a high-risk AI system? (Consequential decision in an enumerated domain?)
- Is the deployer subject to Colorado law?

If yes: Pre-deployment impact assessment, annual reassessment, and consumer notification required.

**5d. California CPRA ADMT Scope Confirmation**

[JURISDICTION-SPECIFIC — California, effective January 1, 2027 for significant decisions]

- Does the system make or substantially contribute to a significant decision?
- Is the consumer a California resident?

If yes: Risk assessment and consumer rights (opt-out, explanation, appeal) apply.

**5e. EEOC/CFPB/FHA Scope Confirmation**

[JURISDICTION-SPECIFIC — US Federal]

- Employment selection tool → Title VII disparate impact / EEOC UGESP four-fifths rule
- Credit model → ECOA adverse action; LDA obligation; CFPB oversight
- Housing system → FHA disparate impact doctrine; HUD guidance

Document applicable frameworks in the AIA report.

### Step 6: Fairness Metrics Analysis — Ten Assessment Dimensions

For each dimension below:

1. Determine applicability to this system and decision context
2. Identify which regulatory framework(s) require or recommend this metric
3. If deployment data is available: assess measured performance against thresholds
4. If data is unavailable: assess prospectively from model design and training data description
5. Classify each dimension: ACCEPTABLE / MONITOR / MITIGATE / PROHIBIT
6. Assign confidence: HIGH / PROBABLE / UNCERTAIN / UNVERIFIABLE
7. Identify root causes for any dimension rated MONITOR, MITIGATE, or PROHIBIT

---

#### Dimension 1: Demographic Parity and Group-Level Impact Ratios

**What it measures:** Whether different demographic groups receive outcomes at equal rates
(selection rates, approval rates, referral rates, positive prediction rates).

**Regulatory basis:**

- NYC LL 144: Impact ratio (selection rate or scoring rate for each demographic category divided by
  the highest-performing category's rate) — explicitly required; reported publicly
- EEOC UGESP four-fifths rule: If any group's selection rate falls below 80% of the majority group's
  rate, adverse impact is presumed — employer must justify tool as job-related and consistent with
  business necessity, and must show no less discriminatory alternative exists
- EU AI Act Art. 9: Bias examination of training data and model outputs [VERIFY explicit Art. 9
  requirement for outcome rate parity vs. bias examination generally]

**Applicable protected classes (US):** Race/ethnicity, sex, age (40+), national origin, religion,
disability, familial status (housing), marital status (credit) — as applicable to the decision domain.
NYC LL 144 requires sex + race/ethnicity + intersectional categories using EEO-1 reporting categories.

**Assessment checklist:**

- [ ] Performance measured separately by demographic group?
- [ ] Impact ratios calculated for all required protected characteristics?
- [ ] Intersectional categories assessed (sex × race/ethnicity at minimum for NYC LL 144)?
- [ ] Groups with fewer than 2% of data identified and documented?
- [ ] Impact ratios meet the four-fifths rule threshold (selection rate ≥ 80% of highest-performing
      group) for all assessed categories?
- [ ] If any group falls below 80%: root cause identified? (See Dimension 5 for proxy analysis)
- [ ] Mitigation options identified if threshold violated?

**Threshold:** Impact ratio ≥ 0.80 (four-fifths rule) for each protected group under US law.
[JURISDICTION-SPECIFIC] EU and other jurisdictions may apply different thresholds.

---

#### Dimension 2: Equalized Odds and Error Rate Parity

**What it measures:** Whether different demographic groups experience equal true positive rates
(TPR — correctly identified positives) and false positive rates (FPR — incorrectly flagged negatives).

**Why it matters:** Unequal error rates produce asymmetric harm. If an AI crime-risk-prediction tool
has a higher FPR for Black defendants than white defendants, Black defendants face higher rates of
false detention. If a hiring tool has a lower TPR for women than men, qualified women are screened out
at disproportionate rates.

**Mathematical constraint:** Equalized odds (equal TPR and FPR across groups) and demographic parity
(equal selection rates) cannot simultaneously hold unless base rates are equal across groups. Where
base rates differ, choose the metric most appropriate to the decision context and document the rationale.

**Assessment checklist:**

- [ ] Confusion matrix calculated separately for each demographic group?
- [ ] True positive rates (recall, sensitivity) compared across groups?
- [ ] False positive rates compared across groups?
- [ ] False negative rates (consequences of missing a qualified individual) assessed?
- [ ] Error rate disparities identified and quantified?
- [ ] Decision rationale documented for which metric (equalized odds vs. demographic parity) takes
      priority in this deployment context?
- [ ] Root cause of error rate disparity identified if present?

**Applicable contexts:** Criminal justice (FPR parity critical), medical diagnosis (TPR parity
critical for ensuring equal disease detection), employment (TPR parity to ensure equal qualified
candidate identification).

---

#### Dimension 3: Calibration and Predictive Parity

**What it measures:** Whether the system's predicted probability or score corresponds to actual
outcome rates for each demographic group (a risk score of 70% should reflect a 70% actual event rate
across all groups).

**The COMPAS example:** COMPAS recidivism prediction tool was found to satisfy calibration (predictive
parity) but not equalized odds — demonstrating the mathematical incompatibility of these metrics when
base rates differ. This is not a flaw to be solved by one metric; it requires deliberate choice of
priority metric based on context. [VERIFY: ProPublica COMPAS analysis (Angwin et al., 2016) — widely
cited but contested; Northpointe response and subsequent academic literature debate]

**Assessment checklist:**

- [ ] System provides risk scores or probability estimates (not just binary decisions)?
- [ ] Calibration curves (predicted probability vs. actual outcome rate) plotted by demographic group?
- [ ] Calibration error quantified by group?
- [ ] Miscalibrated groups identified (especially if system over-predicts risk for any group)?
- [ ] Business consequences of miscalibration assessed (over-reliance on scores for miscalibrated groups)?
- [ ] Recalibration or group-specific threshold adjustment considered as mitigation?

**Applicable contexts:** Credit scoring (score of X should mean the same default probability across
race groups), insurance pricing (risk of X should reflect equal actual event rates), criminal justice
risk tools.

---

#### Dimension 4: Individual Fairness and Decision Consistency

**What it measures:** Whether similar individuals receive similar outcomes; whether decisions are
internally consistent for comparable cases.

**Counterfactual fairness (special case):** Would the individual's outcome change if only their
protected characteristic were changed while everything else remained the same?

**Assessment checklist:**

- [ ] Can the system's decision boundary be inspected for consistency?
- [ ] Counterfactual analysis conducted? (If individual's sex or race changed with no other change,
      would outcome change?)
- [ ] Decision explanations (LIME, SHAP) consistent for similar cases?
- [ ] Unexplained variance in decisions for similar individuals identified?
- [ ] Feature importance stable across demographic groups (same features drive decisions for all groups)?

**Data requirement:** Model inspection access (not available for all vendor black-box systems).

⟁ CLARIFY — If system is a vendor black-box with no model access: "We cannot conduct counterfactual
analysis without model access. Should I (a) request model documentation from the vendor, (b) conduct
a proxy consistency assessment using aggregate output patterns, or (c) note this dimension as
UNVERIFIABLE and escalate to MITIGATE pending data gathering?"

---

#### Dimension 5: Proxy Features and Protected Characteristic Inference

**What it measures:** Whether the system uses protected characteristics directly as input features,
or whether it infers them through proxy features that are highly correlated with protected characteristics.

**Regulatory basis:**

- EU AI Act Art. 10(3): High-risk AI data must be "free of errors and complete" and representative
  [VERIFY: Art. 10(3) specific language on proxy features]; Art. 10(5) permits processing of special
  categories only for bias detection — not for decisional use
- ECOA/FHA case law: Disparate impact claims succeed when a neutral criterion (proxy) produces
  discriminatory outcomes without sufficient business justification

**Common proxy features by protected class:**
| Protected Class | Common Proxies | Domain Examples |
|----------------|----------------|----------------|
| Race/ethnicity | Zip code, neighborhood, surname, school attended, commute distance | Credit scoring, insurance pricing, hiring |
| Sex/gender | Parental leave history, years out of workforce, part-time history | Employment |
| Age | Years of experience, graduation year, "digital native" | Employment |
| National origin | Language proficiency, accent, place of birth, visa type | Employment, housing |
| Religion | Day of week availability, holiday requests, dress code history | Employment |
| Disability | Medical leave history, accommodation requests | Employment |

**Assessment checklist:**

- [ ] Complete list of input features documented?
- [ ] Direct protected characteristic features identified and either excluded or justified?
- [ ] Feature correlation analysis performed? (Correlations between input features and protected
      characteristics quantified)
- [ ] High-correlation proxies (>0.3 correlation with any protected characteristic) identified?
- [ ] Proxy features removed, constrained, or fairness-constrained in model?
- [ ] Feature importance analysis shows no proxy is a dominant decision driver?
- [ ] For vendor systems: vendor documentation reviewed for proxy feature disclosure?

⟁ CLARIFY — "Do you have access to a list of all model input features and their correlation with
demographic characteristics? If not, can we obtain this from the vendor or data science team?"

---

#### Dimension 6: Transparency and Model Card Completeness

**What it measures:** Whether the system's purpose, inputs, performance, limitations, and fairness
properties are documented and explainable to stakeholders, regulators, and affected persons.

**Regulatory basis:**

- EU AI Act Art. 13: High-risk AI systems must be sufficiently transparent to allow deployers to
  understand system capabilities and limitations; instructions of use must include performance metrics
  by group [VERIFY specific Art. 13 language on group performance disclosure]
- EU AI Act Art. 50: Transparency for persons interacting with certain AI systems (emotion
  recognition; biometric categorization; deepfakes)
- GDPR Art. 22 / CJEU C-203/22 (Dun & Bradstreet Austria, 2024): Right to explanation of automated
  decisions includes right to understand the procedure and principal criteria applied — the algorithm
  itself need not be disclosed, but counterfactual explanations are an acceptable form of explanation
- NYC LL 144: Published bias audit summary with selection rates and impact ratios
- CFPB May 2022 Circular: Adverse action notices must state specific reasons — AI-generated model
  codes are insufficient; human-interpretable reasons required
- Colorado SB 24-205: Principal reason(s) for adverse consequential decision must be provided;
  degree and manner of AI contribution must be disclosed
- California CPRA ADMT: Explanation of how ADMT was used and what data informed the decision

**Model card assessment checklist:**

- [ ] System model card or technical documentation exists?
- [ ] Intended use and decision context documented?
- [ ] Performance metrics documented (overall AND by demographic group)?
- [ ] Known limitations documented (data characteristics, fairness/bias limitations, out-of-scope uses)?
- [ ] Fairness metrics and thresholds documented?
- [ ] Training data described (size, source, collection period, demographic composition)?
- [ ] Validation methodology documented?
- [ ] Human oversight and override mechanisms documented?
- [ ] Instructions for use documented?

**Decision explanation assessment:**

- [ ] Tool or procedure exists to explain individual decisions to affected persons? (LIME, SHAP,
      rule extraction, counterfactual explanation, human reviewer)?
- [ ] Explanations can be produced in human-readable, non-technical terms?
- [ ] Adverse action notices/communications provide specific, actionable reasons?
- [ ] Persons are informed when an AI system is used in their evaluation?

---

#### Dimension 7: Human Oversight Adequacy and Appeal Procedure

**What it measures:** Whether humans are meaningfully integrated into the decision-making process,
and whether affected persons have access to review and contestation procedures.

**Regulatory basis:**

- EU AI Act Art. 14: High-risk AI systems must be designed for effective human oversight — overseers
  must understand capabilities and limitations, detect anomalies, and be able to override or halt the system
- EU AI Act Art. 26: Deployers must implement human oversight per instructions; assign qualified,
  authorized overseers
- NYC LL 144: Opportunity for candidate to request alternative selection process (accommodation)
- Colorado SB 24-205: Appeal right with human review when technically feasible; right to correct
  inaccurate personal data
- California CPRA ADMT: Appeal of adverse significant decision reviewed by qualified human
- GDPR Art. 22: Right not to be subject to solely automated decisions producing significant effects,
  unless exceptions apply (consent, necessary for contract, authorized by law) — and even then, right
  to obtain human intervention and contest the decision

**Human oversight assessment checklist:**

- [ ] Is there meaningful human review before the final consequential decision? (Not just rubber-stamping)
- [ ] Is the human overseer trained to understand system capabilities and limitations?
- [ ] Does the human overseer have authority to override the system's output?
- [ ] Is the human overseer resourced and supported to make independent judgments?
- [ ] Can the human overseer identify and escalate anomalies (unexpectedly large disparities, edge cases)?
- [ ] Appeal procedure documented?
- [ ] Affected persons informed of their right to request human review or appeal?
- [ ] Appeal process is accessible (timing, format, burden on the individual)?
- [ ] If appeal succeeds: effective remedy available (decision reversal, corrected record, compensation)?
- [ ] Appeal statistics tracked and monitored for disparities?

⟁ CLARIFY — "What is the actual human role in the final decision? Can you describe the standard
review procedure and how often human reviewers override system recommendations?"

---

#### Dimension 8: Ongoing Monitoring and Feedback Loop Prevention

**What it measures:** Whether system performance is measured post-deployment, fairness degradation is
detected early, and feedback loops (where system outputs feed back into training data, amplifying bias)
are controlled.

**Regulatory basis:**

- EU AI Act Art. 9: Risk management is a continuous process — risk management system must be updated
- EU AI Act Art. 72 / Annex IV: Post-market monitoring plan required; serious incident reporting
  within 72 hours for high-risk systems (Art. 73 timelines) [VERIFY Art. 73 reporting timelines for
  different severity levels]
- EU AI Act Art. 29(4): Deployers must monitor operation on an ongoing basis; report unforeseen risks
- Colorado SB 24-205: Annual impact assessment; reassessment within 90 days of material modification
- NYC LL 144: Annual independent bias audit

**Monitoring framework assessment checklist:**

- [ ] Documented plan to monitor fairness metrics post-deployment?
- [ ] Monitoring metrics defined (which fairness dimensions, which protected characteristics)?
- [ ] Monitoring frequency defined (real-time, daily, weekly, monthly, quarterly)?
- [ ] Alert thresholds defined (at what disparity level does an alert trigger)?
- [ ] Outcome data collection designed and operational (can fairness be remeasured post-deployment)?
- [ ] Feedback loop risk assessed: does system output feed into training data for future versions?
- [ ] If feedback loop risk exists: controls in place to prevent bias amplification?
- [ ] Incident reporting procedure for fairness degradation events?
- [ ] AIA refresh cadence defined (minimum: annual; trigger-based for major system changes)?

---

#### Dimension 9 (Conditional): Sector-Specific and Vulnerable Group Protections

_Assess this dimension if the system affects vulnerable groups (youth, elderly, persons with disabilities,
racial or ethnic minorities, low-income populations, linguistic minorities) or operates in a
heightened-regulation sector._

**Sector-specific regulatory overlays:**

| Sector           | Key Frameworks                                                                                | Specific Obligations                                                               |
| ---------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Employment       | EEOC Title VII, ADA, ADEA, NLRA, NYC LL 144, IL AI Video Interview Act [VERIFY]               | Job-relatedness defense; ADA accommodation alternative; age ≥40 special attention  |
| Credit/lending   | ECOA, FCRA, CFPB                                                                              | Adverse action notice specificity; less discriminatory alternative (LDA) analysis  |
| Housing          | FHA, state fair housing laws, HUD guidance                                                    | Race, national origin, familial status, disability disparate impact screening      |
| Healthcare       | HIPAA (PHI governance), FDA (SaMD if medical device), ONC                                     | Patient safety primary; clinical outcome parity by demographic group               |
| Criminal justice | Varies by state; due process, equal protection; Rite Aid as analogy for non-criminal contexts | High evidentiary standard for disparate impact findings; judicial oversight        |
| Insurance        | NAIC AI Principles, state insurance regulations                                               | Credit-based insurance scoring disparate impact [VERIFY current state regulations] |
| Education        | Title IX, IDEA (disability), FERPA (privacy)                                                  | Disability accommodation; gender parity in AI-based academic assessment            |

**Vulnerable group subgroup analysis:**

- [ ] Fairness metrics calculated separately for vulnerable subgroups?
- [ ] Vulnerable groups identified in the assessment scope?
- [ ] Intersectional analysis performed (e.g., Black women; elderly Latina applicants)?
- [ ] Disparities for vulnerable groups are no greater than for general population?
- [ ] Additional protections designed for vulnerable groups?
- [ ] GDPR Art. 9 / EU AI Act Art. 10(5): Special-category personal data handled with required safeguards?

---

#### Dimension 10 (Conditional): Disparate Impact and Pattern-Level Discrimination

_Assess this dimension for all US-law-subject systems and EU systems involving Art. 21 Charter grounds._

**Disparate impact doctrine:**
US law: A facially neutral policy or algorithm violates anti-discrimination law if it produces a
significantly adverse impact on a protected class and is not justified by business necessity (or
where a less discriminatory alternative exists). Source: Griggs v. Duke Power Co. (1971) for
employment [VERIFY case citation]; _Texas Dept of Housing and Community Affairs v. Inclusive
Communities Project, Inc._ (2015) for FHA [VERIFY].

**Assessment checklist:**

- [ ] Disparate impact analysis performed across all applicable protected classes?
- [ ] Any group's selection/approval rate below 80% of majority group rate? (Four-fifths rule)
- [ ] Historical bias in training data assessed? (Was training data collected during a period of
      documented discrimination in this domain?)
- [ ] System perpetuating historical inequities? (E.g., trained on historical hiring decisions that
      reflected discriminatory practices)
- [ ] Intersectional disparate impact assessed? (Not just single-axis: race alone or sex alone, but
      their combinations)
- [ ] Business necessity justification prepared for any disparity identified?
- [ ] Less discriminatory alternative analysis performed? (Is there a model that achieves similar
      business objectives with smaller disparate impact?)

**The LDA analysis:** For credit decisions (CFPB), the less discriminatory alternative obligation
requires demonstrators to show no feasible alternative model would produce significantly smaller
disparate impact while meeting legitimate business needs. Document the LDA analysis.

---

### Step 7: Root Cause Analysis

For any dimension rated MONITOR, MITIGATE, or PROHIBIT:

1. **Identify the specific disparity** — Which protected characteristics or demographic groups
   experience worse outcomes? Quantify the gaps (magnitude, confidence, affected population size).

2. **Root cause analysis** — Assess whether the disparity is caused by:

   | Root Cause Factor                        | Indicators                                                                                                                                              | Mitigation Path                                                                                              |
   | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
   | **Training data composition**            | Underrepresentation of affected group in training data; historical discrimination reflected in labels                                                   | Rebalance training data; apply fairness-aware weighting; collect additional data for underrepresented groups |
   | **Feature engineering — proxy features** | High correlation between input feature and protected characteristic (>0.3 Pearson correlation); feature importance shows proxy is a top decision driver | Remove proxy feature; apply fairness constraint; use causal feature engineering                              |
   | **Model architecture**                   | Certain algorithms amplify minority-group errors (e.g., ensemble methods that average over majority-heavy training data)                                | Change algorithm; apply fairness-aware training objective; use fairness post-processing                      |
   | **Deployment context mismatch**          | System trained on population A, deployed for population B with different characteristic distributions                                                   | Retrain on representative data; constrain deployment to validated population; apply deployment correction    |
   | **Label bias**                           | Training labels reflect human biases (e.g., labels are past human decisions that were discriminatory)                                                   | Relabel using objective criteria; apply label debiasing; retrain without biased labels                       |
   | **Feedback loop**                        | System's own predictions used to generate training labels for next version; bias compounds over iterations                                              | Break feedback loop; add human review step to training data generation; monitor for drift                    |

3. **Document findings** in the structured format below (see Output Format Template).

### Step 8: Severity Classification and Overall Risk Determination

After completing all ten fairness dimensions, classify each dimension and determine the overall AIA
classification using the four-tier system.

---

## Severity Classification System

Each fairness dimension is classified using this four-tier action-oriented system:

| Tier  | Label          | Definition                                                                                                                                                                                                     | Deployment Recommendation                                                                                                                                          | Regulatory Implication                                                                                                                          |
| ----- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **ACCEPTABLE** | Dimension meets organizational and regulatory fairness thresholds. No material disparities across protected groups. All required safeguards in place.                                                          | Deploy now with standard monitoring.                                                                                                                               | Compliant with applicable frameworks.                                                                                                           |
| **2** | **MONITOR**    | Dimension approaches threshold but not yet violated. Small disparities present (<20% below threshold). Safeguards partially in place but can be strengthened.                                                  | Deploy with enhanced monitoring plan (increased frequency, lower alert thresholds). Requires AI Governance sign-off.                                               | Likely compliant. Requires demonstrated monitoring. May trigger questions on regulatory inquiry.                                                |
| **3** | **MITIGATE**   | Dimension violates threshold. Material disparities present. Root cause identified. Feasible mitigation exists but not yet implemented or validated.                                                            | Deploy only AFTER mitigations are implemented and pre-deployment validation demonstrates improvement. Deployment gates must be satisfied.                          | Potential non-compliance. Regulatory exposure if deployed without documented mitigations and monitoring.                                        |
| **4** | **PROHIBIT**   | Dimension fails materially and severely. Disparities are 50%+ beyond threshold. Regulatory prohibition applies. No feasible mitigation without fundamental redesign. System causes or risks irreversible harm. | Do not deploy. Fundamental redesign required. If already deployed: immediate containment (restrict use, implement hard human overrides, develop remediation plan). | Non-compliant. High enforcement and litigation risk. Potential regulatory sanction. Algorithmic disgorgement a possible remedy (FTC precedent). |

**Classification decision rules:**

- **ACCEPTABLE**: Fairness dimension meets applicable threshold + human oversight and appeal procedures
  adequate + transparency requirements met. Confidence: HIGH or PROBABLE.

- **MONITOR**: Disparity is 0–20% below threshold, OR disparity is within threshold but approaching
  with narrow margin, OR root cause is understood but mitigation is not yet implemented, OR confidence
  is only PROBABLE and enhanced validation would reduce uncertainty. Deployment acceptable with enhanced
  monitoring commitment.

- **MITIGATE**: Disparity exceeds threshold by 20–50%, OR regulatory requirement is mandatory (not
  best practice), OR affected group is a vulnerable population, OR confidence is UNCERTAIN (requires
  pre-deployment validation before deployment approval).

- **PROHIBIT**: Disparity exceeds threshold by more than 50%, OR prohibited practice detected (EU AI
  Act Art. 5; discriminatory feature use that cannot be corrected), OR disparity affects a vulnerable
  group and no feasible pre-deployment mitigation exists, OR UNVERIFIABLE confidence for critical dimensions.

**Overall AIA classification:**

- Most severe dimension rating applies to the overall classification
- Exception: A single MITIGATE finding with a clearly feasible, short-timeline mitigation may be
  classified overall as MITIGATE (rather than PROHIBIT) with explicit deployment gates

⟁ CLARIFY — For borderline MONITOR/MITIGATE or MITIGATE/PROHIBIT findings:
"The disparity on [dimension] places this at the border between [tier A] and [tier B]. Given your
organization's risk tolerance ([conservative/balanced/progressive]) and the regulatory obligation ([X]),
should I classify this as [tier A, conservative] or [tier B, progressive] and document the rationale?"

---

## Prioritization Framework

Findings are prioritized for remediation by combination of severity, magnitude, population, regulatory
driver, and timeline urgency.

| Priority              | Criteria                                                                                                                                                                                   | Response Timeline                                                                        | Escalation                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **TIER 1 — CRITICAL** | PROHIBIT classification OR EU AI Act Art. 5 prohibited practice OR material violation of mandatory regulatory requirement OR affects majority of user population OR irreversible harm risk | Immediate halt / no deployment                                                           | Board or C-suite; external legal counsel; regulatory notification if required |
| **TIER 2 — HIGH**     | MITIGATE classification AND affects >10% of users OR violates multiple fairness dimensions OR regulatory enforcement expected within 6 months                                              | Implement before deployment; max 2 weeks for initial mitigation plan                     | AI Governance Committee; General Counsel; Chief Risk Officer                  |
| **TIER 3 — MEDIUM**   | MONITOR classification OR MITIGATE affecting <10% of users AND feasible mitigation timeline is short                                                                                       | Address within 2–4 weeks; acceptable as condition of deployment with enhanced monitoring | AI Review Board or Center of Excellence; Compliance; Product owner            |
| **TIER 4 — LOW**      | ACCEPTABLE with minor monitoring enhancements OR single dimension requiring minor adjustment                                                                                               | Standard post-deployment monitoring                                                      | AI Owner; Data Science team                                                   |

**Escalation triggers (immediate escalation to AI Governance Committee):**

- [ ] Prohibited AI practice detected (EU AI Act Art. 5; discriminatory feature with no feasible removal)
- [ ] Material disparity affecting vulnerable group (youth, elderly, protected minority, low-income)
- [ ] Consequential decision (employment termination, credit denial, housing rejection, bail decision)
- [ ] Disparity exceeds organizational threshold by more than 50%
- [ ] Technical mitigation is not feasible without fundamental model redesign
- [ ] Regulatory deadline is within 8 weeks
- [ ] Deployed system shows fairness degradation post-deployment

---

## Citation Quality Gates

Run these 5 gates before finalizing any AIA report. If any gate fails, revise before delivery.

| Gate                             | Rule                                                                                                                                                                                                                                                                                    | Fail Action                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Gate 1 — EU AI Act**           | Every EU AI Act citation includes article number and paragraph (e.g., "Art. 27(1)"). Annex III citations include specific point number. Enforcement provisions cite penalty tier with [VERIFY] if uncertain.                                                                            | Add citation specificity or mark [VERIFY]                      |
| **Gate 2 — US Regulatory**       | NYC LL 144 citations include section and subsection. Colorado SB 24-205 includes section and current effective date (June 30, 2026). EEOC/CFPB/FTC guidance cited with document title and date. Canada AIDA status noted as NOT IN FORCE. EO 14110 noted as RESCINDED January 20, 2025. | Correct status and citation                                    |
| **Gate 3 — Fairness Metrics**    | Every metric is named using standard terminology (demographic parity, equalized odds, etc.). Threshold values sourced from regulatory requirement, academic standard, or documented organizational policy. Tool or calculation method cited where metric was computed.                  | Add source for threshold or label as organizational preference |
| **Gate 4 — Disparity Magnitude** | Every disparity finding states: actual measurement, threshold, gap size, affected groups, confidence level, and sample sizes. If N is small: note statistical reliability limitation.                                                                                                   | Add quantification or escalate confidence to UNCERTAIN         |
| **Gate 5 — Root Cause**          | Root cause claim backed by specific evidence (feature correlation, data analysis, model inspection). Root cause is specific (not vague). Alternative root causes considered and ruled out.                                                                                              | Add evidence or qualify as hypothetical pending investigation  |

---

## Self-Interrogation: Three-Pass Review

Apply this to all MITIGATE and PROHIBIT findings before finalizing the report.

**Pass 1 — Clarity and Actionability**
Can a non-technical business stakeholder (product manager, compliance officer without data science
background) read the finding and understand what was found, who is affected, how severely, and what
must be done?

Checklist:

- [ ] Active voice: "The system disadvantages [group] because [reason]"
- [ ] Magnitude stated numerically: "14% below the 80% threshold" not "somewhat lower"
- [ ] Business impact: "affects approximately [N] job applicants per year"
- [ ] Recommended action: specific, sequenced, with named owner and timeline
- [ ] Success criteria: objective and measurable

**Pass 2 — Evidence and Evidentiary Burden**
Is every factual claim in this finding backed by data (measurement, analysis) or marked with
appropriate uncertainty language?

| Claim Type                     | Minimum Evidence                                                         | If Not Available                                              |
| ------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Disparity exists               | Fairness metric measured on deployment data or holdout test set          | Mark UNCERTAIN; escalate to MITIGATE                          |
| Root cause is X                | Feature correlation analysis, model inspection, or controlled experiment | Mark as hypothetical; note investigation needed               |
| Mitigation will work           | Validation on holdout or test environment                                | Mark as planned mitigation; require pre-deployment validation |
| Regulatory requirement applies | Primary source (statute text, official guidance)                         | Mark [VERIFY]; note source needed                             |

**Pass 3 — Proportionality**
Is the severity tier (ACCEPTABLE / MONITOR / MITIGATE / PROHIBIT) proportionate to the actual
disparity magnitude and regulatory context?

Calibration table:
| Disparity Magnitude | Regulatory Driver | Affected Population | Recommended Tier |
|--------------------|--------------------|--------------------|--------------------|
| <5% below threshold | Best practice | Non-vulnerable, small | ACCEPTABLE or MONITOR |
| 5–20% below threshold | Best practice or emerging guidance | Any | MONITOR |
| 20–50% below threshold | Mandatory regulatory requirement | Non-vulnerable | MITIGATE |
| Any magnitude | Mandatory regulatory requirement | Vulnerable group | MITIGATE or PROHIBIT |
| >50% below threshold or regulatory prohibition | Any | Any | PROHIBIT |

---

## Confidence Scoring Framework

| Level            | Definition                                                                                                                              | When to Use                                                                 | Action                                                                            |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **HIGH**         | Direct measurement on representative deployment data. Disparity material (>5%) and statistically significant (p<0.05). N>100 per group. | Deployed system with outcome data                                           | State with confidence. Deploy recommendation is definitive.                       |
| **PROBABLE**     | Measured on limited data (small sample, partial outcome data) or inferred from model inspection with strong supporting evidence.        | Pre-deployment holdout test; N=50–100 per group; model inspection available | State with caveat. Recommend pre-deployment validation for MITIGATE findings.     |
| **UNCERTAIN**    | Based on theoretical analysis, simulation, or model description. Material assumptions required. No deployment data.                     | Prototype; vendor black-box; missing outcome data                           | Do not base ACCEPTABLE classification on UNCERTAIN confidence. Escalate one tier. |
| **UNVERIFIABLE** | Required data is inaccessible or unavailable. Cannot make determination.                                                                | Vendor refusal to disclose; data not collected                              | Escalate finding to MITIGATE or PROHIBIT pending information gathering.           |

**Impact on deployment decisions:** UNVERIFIABLE confidence on any Tier 1 or Tier 2 escalation
criterion → automatic escalation to MITIGATE pending data gathering.

---

## Anti-Patterns: What NOT to Do in Algorithmic Impact Assessment

1. **One-dimensional fairness focus** — Assessing only demographic parity while ignoring equalized
   odds, calibration, individual consistency, and intersectionality. Fairness is multi-dimensional;
   a system can satisfy one metric while severely violating another. Assess all applicable dimensions.

2. **Proxy feature blindness** — Concluding that because the system does not directly use race, sex,
   or other protected characteristics, it is fair. Zip code, name, graduation year, employment history,
   and dozens of other features act as proxies. Always perform a feature correlation analysis.

3. **Aggregate-only analysis** — Reporting accuracy or performance metrics only at the overall population
   level, not by demographic subgroup. A 90% overall accuracy can mask 95% accuracy for one group and
   70% for another. Every fairness metric must be computed separately by group.

4. **Treating demographic groups as monolithic** — Analyzing "race" as a single category without
   disaggregating by subgroup (Black, Hispanic, Asian, Indigenous, Pacific Islander). Similarly for
   gender (beyond binary), national origin, disability type, and age ranges. Disaggregate.

5. **Ignoring intersectionality** — Assessing race and sex separately but not combinations. The largest
   fairness gaps often appear at intersections (e.g., Black women, elderly Latino men). Include
   intersectional metrics, especially for NYC LL 144 compliance (which explicitly requires them).

6. **Confidence without measurement** — Claiming "the model is fair" based on model architecture review
   without actual measurement of outcomes by demographic group on real or representative data.

7. **Comparing against biased human baseline** — Measuring whether the system performs "as well as"
   human decision-makers, without accounting for the possibility that human decision-makers themselves
   were biased. Fairness baseline is equity, not status quo human behavior.

8. **Ignoring feedback loops** — Failing to assess whether system outputs feed into training data for
   future model versions, amplifying biases over successive retraining cycles. Explicitly assess and
   control feedback loops.

9. **Treating mitigation as done when only planned** — Documenting "fairness-aware training will be
   applied" without actually implementing, testing, and validating the mitigation pre-deployment.
   Plans are not results. Require validated evidence before clearing for deployment.

10. **Accepting thresholds without justification** — Applying the four-fifths rule or other standard
    thresholds without asking whether they are appropriate for the specific domain, population, and
    regulatory context. Different domains may warrant different thresholds. Document the rationale.

11. **Deploying first, assessing later** — Conducting the AIA after the system is in production rather
    than before. The AI Act, Colorado SB 24-205, and California CPRA ADMT all require pre-deployment
    assessment. Post-deployment discovery causes harm before remediation begins.

12. **Insufficient sample size per group** — Reporting fairness metrics with N<50 per demographic group,
    which is too small for statistical confidence. Note limitations explicitly; escalate confidence to
    UNCERTAIN and tier to MITIGATE until sufficient data is available.

13. **Ignoring feature importance** — Not analyzing which input features are actually driving decisions.
    A seemingly harmless feature may turn out to be the primary decision driver and a proxy for
    protected characteristics. Feature importance analysis is a required element of every AIA.

14. **Confusing explainability with fairness** — Assuming that because a decision can be explained, it
    is fair. A decision can be fully explained and still be discriminatory. Explainability and fairness
    are separate dimensions; both are required.

15. **Neglecting human oversight as a fairness mechanism** — Assuming that a fair algorithm makes human
    oversight optional. Even a statistically fair algorithm produces unfair results in edge cases.
    Human oversight is a risk control independent of and complementary to algorithmic fairness. Do not
    rely on algorithm fairness as the sole safety mechanism.

16. **Conflating legal compliance with ethical sufficiency** — Meeting the legal minimum does not mean
    the system is ethically acceptable or that affected communities find it legitimate. Both legal
    compliance and ethical legitimacy should be assessed.

17. **Excluding affected communities from the assessment** — Conducting the AIA entirely from a
    technical and legal perspective without any consultation with persons who will be affected by the
    system's decisions. Community input identifies harms that statistical analysis misses.

18. **Static assessment with no refresh cadence** — Treating an AIA as a one-time stamp of approval.
    Systems change. Data distributions shift. Regulations evolve. Define a minimum annual review and
    trigger-based reassessment for material system changes.

19. **Hiding disparities in technical language** — Burying a material finding in mathematical notation
    that business leaders and compliance officers cannot decode. Every finding must be explained in
    plain language with quantified business impact.

20. **Confusing correlation with causation in root cause analysis** — Observing that a feature
    correlates with a protected characteristic and concluding it causes discrimination, or conversely,
    treating absence of observed correlation as absence of proxy risk. Correlation is evidence;
    causation requires additional investigation. Label claims appropriately.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp in Step 4 to search for:

- EU AI Act Arts. 9, 10, 14, 27, 29 current text and EU AI Office interpretive guidance
- National DPA guidance on GDPR Art. 22 automated decision-making (CJEU C-203/22)
- NYC DCWP Local Law 144 current rules and interpretations
- Colorado AG SB 24-205 guidance and rule-making developments
- California CPPA ADMT Regulation guidance
- EEOC Title VII AI technical assistance (May 2023) and ADA AI guidance (June 2023)
- CFPB adverse action and LDA guidance; FTC Section 5 enforcement in AI (Rite Aid precedent)
- FHA disparate impact case law (HUD v. Inclusive Communities Project, applicable circuit court decisions)
- IEEE 7003-2024 and ISO/IEC TR 24027 current versions
- NIST AI RMF Playbook MEASURE function guidance

Mark all legalcode-mcp-sourced citations as VERIFIED in Glass Box.

### Without legalcode-mcp

Mark all regulatory and technical citations with [VERIFY]. Note in Glass Box:
`external_tools_used: "None — manual verification required"`

Include in AIA report:
_"All regulatory and legal citations in this assessment require independent verification by qualified
legal counsel before any deployment decision is made."_

### Fairness Analysis Tooling Integration

For organizations with access to fairness analysis libraries:

- **Fairlearn (Microsoft):** demographic_parity_ratio(); equalized_odds_ratio(); calibration analysis
- **AI Fairness 360 (IBM AIF360):** Comprehensive bias metrics including individual fairness, counterfactual
- **LIME (Ribeiro et al.):** Local explanation for individual decisions; consistency analysis
- **SHAP (Lundberg & Lee):** Feature importance by demographic group; consistency across subpopulations
- **What-If Tool (Google):** Counterfactual fairness analysis; side-by-side demographic comparison

Document tool versions and parameters in Glass Box. If no tooling is available, escalate affected
dimensions to UNCERTAIN confidence and note in remediation roadmap that tool acquisition or vendor
testing is required.

---

## Writing Standards

### Plain Language Discipline

1. **Active voice**: "The system screens out women at twice the rate of men" not "Women are screened out"
2. **Name the actor**: "Dimension 1 (Demographic Parity) finds that Hispanic applicants are approved at
   a rate 34% below the majority group" not "Disparities were found"
3. **Quantify every disparity**: "18% below the 80% threshold" not "below the standard"
4. **Business impact before technical detail**: State the business/human consequence, then the metric
5. **No unexplained acronyms**: First use: "equalized odds (equal true positive and false positive rates
   across demographic groups)"; subsequent uses: "equalized odds"
6. **Severity calibration**: Language matches tier — "PROHIBIT: system must not be deployed" not "concerns
   were identified"

### Quality Gates Before Delivery

- ✅ **Readability**: Can a non-technical compliance officer read the Executive Summary, understand the top
  3 issues, and describe the required actions without consulting a data scientist?
- ✅ **Actionability**: For each MITIGATE or PROHIBIT finding: specific action, owner, timeline, and
  success criteria stated.
- ✅ **Evidence**: Every claim backed by data or marked [VERIFY] / [UNCERTAIN] / [UNVERIFIABLE].
- ✅ **Citation specificity**: Every regulatory requirement cited with article/section and source.
- ✅ **Proportionality**: Severity tier matches actual disparity magnitude and regulatory context.
- ✅ **Coverage**: All 8–10 dimensions addressed; N/A dimensions explained.
- ✅ **Compliance mapping**: Clear regulatory compliance status for each applicable framework.

---

## Output Format Template

Use this template for all AIA reports. Populate every section; mark sections N/A with explanation.

---

### AIA Executive Summary

**System Name**: [Name, vendor, version]
**Assessment Date**: [YYYY-MM-DD]
**Decision Context**: [Employment / Credit / Housing / Healthcare / Other]
**Automation Level**: [Fully automated / Assisted / Informational / Advisory]
**Affected Population**: [Estimated number; description; geographic scope]
**Assessment Type**: [Pre-deployment / Annual audit / Post-modification / Post-incident]
**Primary Regulatory Driver**: [EU AI Act / NYC LL 144 / Colorado SB 24-205 / California CPRA ADMT /
EEOC / CFPB / NIST AI RMF / Internal governance]
**Data Basis**: [Full deployment data / Holdout test data / Model documentation only / Vendor description]
**Assessment Confidence**: [HIGH / PROBABLE / UNCERTAIN — explain]

---

### Overall AIA Classification

**Classification**: **[ACCEPTABLE / MONITOR / MITIGATE / PROHIBIT]**

| Dimension              | Classification                               | Confidence                             | Key Finding                                                                |
| ---------------------- | -------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| 1. Demographic Parity  | [ACCEPTABLE / MONITOR / MITIGATE / PROHIBIT] | [HIGH/PROBABLE/UNCERTAIN/UNVERIFIABLE] | [e.g., "Impact ratio 0.74 for Hispanic applicants — below 0.80 threshold"] |
| 2. Equalized Odds      | [tier]                                       | [level]                                | [finding]                                                                  |
| 3. Calibration         | [tier]                                       | [level]                                | [finding]                                                                  |
| 4. Individual Fairness | [tier]                                       | [level]                                | [finding]                                                                  |
| 5. Proxy Features      | [tier]                                       | [level]                                | [finding]                                                                  |
| 6. Transparency        | [tier]                                       | [level]                                | [finding]                                                                  |
| 7. Human Oversight     | [tier]                                       | [level]                                | [finding]                                                                  |
| 8. Monitoring          | [tier]                                       | [level]                                | [finding]                                                                  |
| 9. Vulnerable Groups   | [tier / N/A]                                 | [level]                                | [finding]                                                                  |
| 10. Disparate Impact   | [tier / N/A]                                 | [level]                                | [finding]                                                                  |
| **Overall**            | **[most severe tier]**                       | **[lowest confidence]**                |                                                                            |

---

### Deployment Recommendation

**Can this system be deployed?**

- **ACCEPTABLE**: ✅ Deploy now with standard monitoring. No material disparities identified.
- **MONITOR**: ✅ Deploy with enhanced monitoring (higher frequency, lower alert threshold, escalation
  plan in place). Requires AI Governance Committee sign-off before deployment.
- **MITIGATE**: ⚠️ Deploy only after documented mitigations are implemented AND pre-deployment validation
  demonstrates improvement. Deployment gates below must be satisfied. Timeline: [X weeks].
- **PROHIBIT**: ❌ Do not deploy. System requires fundamental redesign before deployment can be
  considered. If deployed: immediate remediation plan required.

**Regulatory Compliance Status:**
| Framework | Compliance Status | Key Gaps |
|-----------|------------------|----------|
| EU AI Act (Arts. 9, 10, 14, 27) | [Compliant / Partial / Non-Compliant / N/A] | [Gaps if any] |
| NYC Local Law 144 | [Compliant / Partial / Non-Compliant / N/A] | [Gaps if any] |
| Colorado SB 24-205 | [Compliant / Partial / Non-Compliant / N/A] | [Gaps if any] |
| California CPRA ADMT | [Compliant / Partial / Non-Compliant / N/A] | [Gaps if any] |
| EEOC / Title VII | [Compliant / Partial / Non-Compliant / N/A] | [Gaps if any] |
| CFPB / ECOA | [Compliant / Partial / Non-Compliant / N/A] | [Gaps if any] |
| NIST AI RMF | [Addressed / Partial / Not Addressed / N/A] | [Gaps if any] |

---

### Fairness Metrics Summary

| Dimension          | Metric Used                         | Threshold                 | Measured Result            | Status      | Confidence | Sample Sizes                      |
| ------------------ | ----------------------------------- | ------------------------- | -------------------------- | ----------- | ---------- | --------------------------------- |
| Demographic Parity | Impact ratio (selection rate ratio) | ≥ 0.80 (four-fifths rule) | 0.74 (Hispanic applicants) | ❌ VIOLATED | HIGH       | Total N = 3,200; Hispanic N = 420 |
| ...                | ...                                 | ...                       | ...                        | ...         | ...        | ...                               |

---

### Root Cause Analysis

**[Dimension Name] — Root Cause Findings**

| Root Cause Factor                                                                                                        | Evidence                                                                                              | Confidence | Severity | Mitigation Feasible                           |
| ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ---------- | -------- | --------------------------------------------- |
| [e.g., Training data composition — Hispanic applicants underrepresented in training data (8% vs. 22% in applicant pool)] | [Feature distribution analysis; comparison of training set demographic composition to applicant pool] | HIGH       | HIGH     | Yes — rebalance training data and retrain     |
| [e.g., Proxy feature — zip code correlates with Hispanic ethnicity at r=0.48]                                            | [Correlation analysis]                                                                                | PROBABLE   | MEDIUM   | Yes — remove zip code; assess accuracy impact |

---

### Recommended Mitigations

**[Dimension and Finding]**

| Mitigation Option                                     | Type                | Implementation                                                  | Effort                 | Impact on Fairness                                               | Timeline  |
| ----------------------------------------------------- | ------------------- | --------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------- | --------- |
| Rebalance training data for underrepresented groups   | Technical — Data    | Oversample underrepresented group; retrain; validate on holdout | Medium (2–3 weeks)     | Reduce demographic parity gap by ~[X]%                           | 3–4 weeks |
| Remove proxy feature (zip code)                       | Technical — Feature | Re-engineer model without zip code; retrain; validate           | Low–Medium (1–2 weeks) | Reduce proxy-driven disparity; potential minor accuracy loss     | 2–3 weeks |
| Post-processing threshold adjustment by group         | Technical — Output  | Apply group-specific decision thresholds to equalize rates      | Low (immediate)        | Reduces demographic parity gap to within threshold               | 1–2 weeks |
| Require human review for cases near decision boundary | Process             | Define boundary; route edge cases to human reviewer             | Medium                 | Reduces disparity to near-zero in boundary cases; increases cost | 3–4 weeks |

**Recommended approach**: [Rationale for mitigation combination]
**Success criteria**: [Specific metric improvement target]
**Timeline to implementation**: [Date]

---

### Prioritized Remediation Roadmap

**If MITIGATE or PROHIBIT classification:**

| Priority | Task                                       | Owner  | Due Date | Success Criteria                                    | Risk if Delayed |
| -------- | ------------------------------------------ | ------ | -------- | --------------------------------------------------- | --------------- |
| 1        | Implement mitigation #1: [specific action] | [Role] | [Date]   | [Metric improves from X to Y; validated on holdout] | Cannot deploy   |
| 2        | [next mitigation]                          |        |          |                                                     |                 |

**Deployment gates (all must be satisfied before deployment):**

- [ ] All Priority 1 mitigations implemented and pre-deployment validation passed
- [ ] Human oversight and appeal procedure documented, tested, and staff trained
- [ ] Monitoring plan operational with alert thresholds configured
- [ ] AI Governance Committee approval documented
- [ ] Regulatory compliance verified by qualified counsel (if applicable regulatory obligation)

---

### Ongoing Monitoring Plan

| Monitoring Metric             | Target Threshold  | Frequency   | Alert Threshold     | Data Collection Requirement |
| ----------------------------- | ----------------- | ----------- | ------------------- | --------------------------- |
| [Fairness dimension + metric] | [threshold value] | [frequency] | [trigger for alert] | [outcome data required]     |

**Monitoring roles:**

- Data collection owner: [Role]
- Metrics calculation owner: [Role]
- Alert response owner: [Role]
- Escalation path: [AI Governance Committee / General Counsel / Regulator as appropriate]

**AIA refresh cadence:** Annual minimum; trigger-based for: (a) major system change (>10% of training
data, algorithm change, feature addition); (b) fairness degradation alert; (c) regulatory change;
(d) material change in deployment context or affected population.

---

### Glass Box Audit Trail

```yaml
glass_box:
  ai_system: "[System name, vendor, version]"
  assessment_date: "[YYYY-MM-DD]"
  assessor: "[Name, title, organization]"
  decision_context: "[Employment / Credit / Housing / Healthcare / Other]"
  automation_level: "[Fully automated / Assisted / Informational / Advisory]"
  affected_population: "[Number, description, geographic scope]"
  applicable_regulatory_frameworks:
    - "[EU AI Act Regulation (EU) 2024/1689 — Arts. 9, 10, 14, 27]"
    - "[NYC Local Law 144]"
    - "[Colorado SB 24-205, effective June 30 2026]"
    - "[California CPRA ADMT Regulations, effective Jan 1 2026]"
    - "[EEOC Title VII Technical Assistance May 2023]"
    - "[CFPB ECOA adverse action and LDA guidance]"
    - "[NIST AI RMF 1.0 — MAP and MEASURE functions]"

  data_sources:
    deployment_data: "[Yes / No / Partial — describe]"
    holdout_test_data: "[Yes / No]"
    training_data_description: "[Description: size, source, collection period, demographic composition]"
    outcome_data: "[Yes / No — describe what outcomes were available]"
    data_currency: "[Date range of data]"

  fairness_dimensions:
    assessed: 10
    acceptable: "[count]"
    monitor: "[count]"
    mitigate: "[count]"
    prohibit: "[count]"

  protected_characteristics_analyzed:
    - "Race/ethnicity (EEO-1 categories)"
    - "Sex/gender"
    - "Age (40+)"
    - "National origin"
    - "Disability"
    - "[Other applicable characteristics]"

  intersectional_analysis: "[Yes / No / Partial — describe]"
  vulnerable_subgroups_analyzed: "[Yes / No / Partial — describe]"

  regulatory_compliance_status:
    eu_ai_act_high_risk_arts_9_10_14_27: "[Compliant / Partial / Non-Compliant / N/A]"
    nyc_ll_144_aedt_bias_audit: "[Compliant / Partial / Non-Compliant / N/A]"
    colorado_sb_24_205_impact_assessment: "[Compliant / Partial / Non-Compliant / N/A]"
    california_cpra_admt_risk_assessment: "[Compliant / Partial / Non-Compliant / N/A]"
    eeoc_title_vii_adverse_impact: "[Compliant / Partial / Non-Compliant / N/A]"
    cfpb_ecoa_adverse_action: "[Compliant / Partial / Non-Compliant / N/A]"
    nist_ai_rmf_map_measure: "[Addressed / Partial / Not Addressed / N/A]"

  root_cause_analysis: "[Conducted for all MITIGATE/PROHIBIT dimensions / Partial / Not conducted]"
  root_causes_identified:
    - "[Root cause, confidence level]"

  mitigations_evaluated: "[Yes / No]"
  mitigation_options_identified: "[count]"
  pre_deployment_mitigation_feasible: "[Yes (timeline: X weeks) / Partial / No (fundamental redesign required)]"

  human_oversight: "[Level: Fully automated / Assisted / Informational / Advisory]"
  human_oversight_compliant: "[Yes / Partial / No — describe gaps]"
  appeal_procedure: "[Documented and operational / Documented not operational / Not documented]"
  appeal_procedure_compliant: "[Yes / Partial / No — describe gaps]"

  monitoring_plan: "[Documented and operational / Documented / Not documented]"
  monitoring_metrics: "[List key fairness metrics to be monitored]"
  monitoring_frequency: "[Real-time / Daily / Weekly / Monthly / Quarterly]"
  feedback_loop_risk: "[High / Medium / Low — explain]"
  feedback_loop_controls: "[Yes / Partial / No — describe]"

  external_tools_used:
    legalcode_mcp: "[Connected (citations VERIFIED) / Not connected ([VERIFY] markers used)]"
    fairness_libraries: "[Fairlearn / AIF360 / None — describe]"
    explainability_tools: "[LIME / SHAP / None — describe]"
  authority_reference_file: "[/tmp/aia-regulatory-authority.md / Not created]"
  citations_verified: "[N VERIFIED / N marked [VERIFY]]"

  self_interrogation:
    pass_1_clarity: "[PASS / REVISED — describe changes]"
    pass_2_evidence: "[PASS / REVISED — describe changes]"
    pass_3_proportionality: "[PASS / REVISED — describe changes]"
    overall: "[PASS / ESCALATED — describe]"

  citation_quality_gates:
    gate_1_eu_ai_act: "[PASS / FAILED: describe]"
    gate_2_us_regulatory: "[PASS / FAILED: describe]"
    gate_3_fairness_metrics: "[PASS / FAILED: describe]"
    gate_4_disparity_magnitude: "[PASS / FAILED: describe]"
    gate_5_root_cause: "[PASS / FAILED: describe]"
    overall: "[PASS / FAILED]"

  overall_classification: "[ACCEPTABLE / MONITOR / MITIGATE / PROHIBIT]"
  deployment_recommendation: >
    [Deploy now / Deploy with enhanced monitoring (AI Governance sign-off required) /
    Deploy only after mitigations implemented and validated (deployment gates defined) /
    Do not deploy — fundamental redesign required]

  confidence_overall: "[HIGH / PROBABLE / UNCERTAIN / UNVERIFIABLE]"
  confidence_rationale: "[Brief explanation]"

  limitations:
    - "[Limitation: outcome data unavailable for [group]; assessment is prospective]"
    - "[Limitation: vendor system — model inspection not available; proxy analysis based on output patterns only]"
    - "[Limitation: Canada AIDA not in force (January 2026); guidance only]"
    - "[Other limitation]"

  escalation_flags:
    - "[Flag: PROHIBIT classification — AI Governance Committee sign-off required before any deployment decision]"
    - "[Flag: Material disparity affecting vulnerable group]"
    - "[Flag: Regulatory enforcement deadline approaching: describe]"

  reviewer: >
    AI-assisted assessment — requires review by (1) qualified legal counsel licensed in applicable
    jurisdiction, (2) AI/data science expert for fairness metric validation, and (3) domain expert
    (employment / credit / housing / healthcare as applicable) before final deployment decision.

  review_checklist:
    - "[ ] Legal counsel reviewed regulatory compliance status and gaps"
    - "[ ] Data science expert validated fairness metrics and root cause analysis"
    - "[ ] Domain expert reviewed sector-specific requirements"
    - "[ ] Affected community consulted (if applicable)"
    - "[ ] AI Governance Committee approval documented (if MONITOR, MITIGATE, or PROHIBIT)"
    - "[ ] Deployment decision documented with rationale and authorized signatory"
```

---

## Localization Notes

This skill is jurisdiction-agnostic. When adapting for specific jurisdictions:

**EU Member States:** Supplement with national DPA guidance on GDPR Art. 22 automated decisions and
member-state AI Act implementing regulations. Some member states have additional national AI legislation
[VERIFY: current national AI Acts in DE, FR, IT, ES as of 2026].

**UK:** UK AI Act not yet enacted as of early 2026. ICO guidance on automated decision-making under
UK GDPR applies. Monitor UK AI regulation developments [VERIFY: UK AI Act status as of assessment date].

**Canada:** Federal AIDA not enacted. Provincial human rights codes apply. Quebec Act Respecting the
Protection of Personal Information in the Private Sector (Law 25) contains automated decision
provisions [VERIFY: current Quebec Law 25 AIA obligations].

**Australia:** Privacy Act 1988 (Cth) and OAIC guidance on automated decision-making. Productivity
Commission AI regulation review underway [VERIFY: current AU AI regulation status].

**US States beyond NYC/Colorado/California:** Illinois AI Video Interview Act (employment video
interviews) [VERIFY citation]; Maryland, New Jersey, Vermont, and other states with pending or enacted
AI accountability legislation [VERIFY current status by state].

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis using 2-agent research pipeline: (1) Structural
Analyst agent analyzing reference skills (legalcode-contract-review, legalcode-eu-ai-act-high-risk-compliance,
legalcode-ai-governance-framework-builder) for structural patterns and quality frameworks; (2) Legal
Research agent conducting deep web research on EU AI Act (Regulation 2024/1689) Arts. 5/9/10/14/27/29/99
and Annexes III/IV; NYC Local Law 144 (effective January 2023, enforcement July 2023); Colorado SB 24-205
(signed May 2024, effective June 30 2026); California CPRA ADMT Regulations (finalized September 2025,
effective January 2026); Canada AIDA (Bill C-27, died January 2025 — NOT in force); NIST AI RMF 1.0;
IEEE 7003-2024; ISO/IEC TR 24027; EEOC May 2023 Title VII AI Technical Assistance; CFPB May 2022
adverse action Circular; FTC Rite Aid consent order (December 2023); CJEU C-203/22 (GDPR Art. 22
right to explanation); Griggs v. Duke Power Co. (Title VII disparate impact); fairness metrics
literature (demographic parity, equalized odds, calibration, individual fairness, counterfactual
fairness). Ten-dimension fairness assessment framework, four-tier classification system
(ACCEPTABLE/MONITOR/MITIGATE/PROHIBIT), 20 anti-patterns, Glass Box audit trail, Citation Quality
Gates, Self-Interrogation, and Confidence Scoring adapted from Legalcode quality standards.
