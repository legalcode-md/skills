---
name: legalcode-eu-ai-act-high-risk-compliance
description: >
  EU AI Act (Regulation 2024/1689) high-risk AI system compliance assessment covering
  risk classification determination (Annex I and Annex III categories), risk management
  system requirements (Art. 9), data governance and training data requirements (Art. 10),
  technical documentation (Art. 11, Annex IV), record-keeping and logging (Art. 12),
  transparency and provision of information to deployers (Art. 13), human oversight
  design (Art. 14), accuracy, robustness, and cybersecurity (Art. 15), quality management
  system (Art. 17), conformity assessment procedures (Art. 43, Annex VI/VII), CE marking
  and EU declaration of conformity (Art. 49, 71), post-market monitoring (Art. 72), and
  serious incident reporting (Art. 73). Use when a provider or deployer needs to assess
  EU AI Act compliance for a high-risk AI system, prepare for conformity assessment,
  build or audit a quality management system, gap-analyse an existing system against the
  August 2026 enforcement deadline, or determine whether a system falls within the
  high-risk or prohibited categories. Cross-references GDPR Article 35 DPIA requirements
  and ISO/IEC 42001:2023. Produces risk classification determinations, gap analysis
  reports, compliance checklists, remediation action plans, and conformity assessment
  preparation documentation.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode EU AI Act High-Risk Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted EU AI Act compliance
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. The EU
> AI Act is recent legislation (entered into force August 2024); regulatory guidance,
> harmonised standards, and national competent authority positions continue to evolve.
> Statutory and regulatory references cited from training-data knowledge carry
> hallucination risk — verify against the official EUR-Lex text and current regulator
> guidance before relying on them. Mark all unverified references [VERIFY].

---

## Purpose and Scope

This skill assesses whether a specific AI system meets the requirements of the EU AI Act
(Regulation (EU) 2024/1689) for high-risk AI systems. It guides providers and deployers
through the complete compliance lifecycle — from initial risk classification through
conformity assessment preparation, post-market monitoring, and incident reporting
readiness.

**Covers:**
- High-risk classification screening (Annex I + Annex III categories; Article 6
  "significant risk" carve-out)
- Prohibited AI practices screening (Annex I — to identify out-of-scope systems)
- Risk management system audit (Article 9 — 4-element lifecycle assessment)
- Data governance and training data review (Article 10)
- Technical documentation gap analysis (Article 11, Annex IV)
- Record-keeping and logging capability assessment (Article 12)
- Transparency and instructions-for-use review (Article 13)
- Human oversight design evaluation (Article 14)
- Accuracy, robustness, and cybersecurity assessment (Article 15)
- Quality management system gap analysis (Article 17; prEN 18286 alignment)
- Conformity assessment path determination (Article 43; Annex VI vs. Annex VII)
- CE marking and EU Declaration of Conformity preparation (Articles 49, 71)
- Post-market monitoring plan review (Article 72)
- Serious incident reporting readiness (Article 73)
- Provider vs. deployer obligation mapping (Articles 16, 25, 26)
- GDPR DPIA cross-reference (Article 35 GDPR, Recital 95 AI Act)
- ISO/IEC 42001:2023 alignment check

**Does not:**
- Constitute legal advice or replace qualified EU AI Act counsel
- Cover GPAI model obligations (Chapter V, Arts. 51-56) except as cross-references
- Cover prohibited AI practices enforcement procedure (Chapters III, VII)
- Address national implementing legislation beyond EU AI Act baseline
- Cover the EU AI Liability Directive (separate instrument, under negotiation)
- Assess non-EU AI governance frameworks (US NIST AI RMF, UK AI Safety Act, NIST
  CSF) except as voluntary alignment benchmarks

**Related skills:**
- `legalcode-dpia-generator` — for GDPR DPIA where AI system processes personal data
- `legalcode-cross-border-transfer-assessment` — for international data transfers
- `legalcode-regulatory-change-tracker` — for tracking EU AI Act implementation updates

---

## Jurisdiction and Governing Law

This skill applies **EU law** — specifically Regulation (EU) 2024/1689 (the EU AI Act),
which entered into force on 1 August 2024 and applies in phases through 2027.

**Territorial scope:** The AI Act applies to:
- Providers placing AI systems on the EU market or putting them into service in the EU
- Providers outside the EU whose systems produce outputs used in the EU
- Deployers of AI systems established or located in the EU
- Importers and distributors in the AI value chain

**[JURISDICTION-SPECIFIC]** The AI Act is directly applicable in all 27 EU Member States
without national transposition. However, Member States retain discretion in:
- Designating national competent authorities (NCAs) and market surveillance authorities
- Setting administrative fine levels within AI Act maxima
- Enacting sector-specific AI governance guidance (healthcare, finance, law enforcement)
- Establishing national AI regulatory sandboxes (Arts. 57-63)
- Determining penalties for natural persons (Art. 99(6))

When assessing systems in a specific Member State, consult the relevant NCA's guidance
and any sector-specific regulatory positions. Key NCAs include: Germany (BNetzA/BSI),
France (CNIL/DGCCRF), Netherlands (AP/ACM), Italy (AGCM/AGID).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's context, the workflow pauses and asks when:

- The answer would change the direction of the assessment (provider vs. deployer)
- The system's high-risk classification is ambiguous and user context resolves it
- Multiple valid conformity assessment paths exist and organisational preference matters
- Scope decisions need to be made (full assessment vs. targeted gap analysis)

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

## Implementation Timeline

| Date | Event | Key obligations |
|------|-------|----------------|
| 1 Aug 2024 | AI Act enters into force | Countdown begins |
| 2 Feb 2025 | **Prohibited practices apply** | Annex I prohibitions enforceable; ban on unacceptable-risk systems (Art. 5) |
| 2 Aug 2025 | **GPAI obligations apply** | Chapter V (Arts. 51-56) for GPAI models; NCAs must be designated; EU AI Office operational |
| 2 Aug 2026 | **HIGH-RISK OBLIGATIONS APPLY** | Arts. 9-17, 43, 49, 72, 73 enforceable; Annex III high-risk systems must be compliant; enforcement begins |
| 2 Feb 2026 | PMM plan template | Commission implementing act on Art. 72 PMM plan template due |
| 2 Aug 2027 | Full implementation | Annex I (regulated product) high-risk systems placed on market before Aug 2026 must comply |

> **Primary deadline for this skill: 2 August 2026.** Systems placed on the EU market on
> or after that date must meet all high-risk requirements before placement. Systems already
> on market have until 2 August 2027 if they fall under Annex I (regulated products sector).

---

## Workflow

### Step 1: Accept Input

Accept the AI system description in any of these formats:
- **System description**: A written description of the AI system, its intended purpose,
  the data it uses, and the decisions it influences
- **Technical documentation**: Draft or partial Annex IV technical documentation
- **Questionnaire answers**: Responses to structured questions about the system
- **Existing compliance artefacts**: Prior risk assessments, DPIA, vendor documentation,
  or internal audit reports

If no description is provided, prompt the user to supply one before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask these questions. Skip any already
answered in the initial prompt.

1. **What is your role in the AI value chain?**
   - Options: Provider (we develop/place on market), Deployer (we use a third-party
     system), Both (we develop and deploy our own system), Importer/Distributor, Not yet
     determined
   - *Why this matters*: The AI Act places the majority of obligations on providers
     (Art. 16). Deployers have narrower obligations (Art. 26). If a deployer puts their
     name on the system, makes a substantial modification, or changes the intended purpose
     to create high-risk classification, they become the provider (Art. 25) — the
     assessment shifts entirely.

2. **Which high-risk category do you believe applies (if any)?**
   - Options: Biometrics (Annex III, point 1), Critical infrastructure (point 2),
     Education/vocational training (point 3), Employment/HR (point 4), Essential services
     (credit/insurance/public benefits) (point 5), Law enforcement (point 6),
     Migration/asylum/border control (point 7), Administration of justice/democratic
     processes (point 8), Regulated product sector (Annex I — machinery, medical
     devices, vehicles), Unsure — need classification help
   - *Why this matters*: The category determines which conformity assessment path applies
     (internal control vs. mandatory notified-body involvement), which accuracy/bias
     metrics are most relevant, and which sector regulators have jurisdiction.

3. **What is your current compliance posture?**
   - Options: Greenfield — designing the system now, Existing system — needs gap
     analysis before Aug 2026, Existing system — already partially compliant, Vendor
     system — assessing a third-party provider's compliance
   - *Why this matters*: A greenfield system can be built with compliance by design. An
     existing system needs a remediation roadmap. A vendor system assessment focuses on
     provider documentation review and deployer due diligence.

4. **What is your primary output need?**
   - Options: Full compliance assessment (all 13 requirement areas), Targeted gap
     analysis (specific articles only), Conformity assessment preparation checklist,
     QMS framework documentation, Classification determination only
   - *Why this matters*: A full assessment takes significantly more depth than a targeted
     gap analysis. The output format is tailored to the primary need.

### Step 3: Gather Legal Authority

Before beginning the assessment, search for and save the most relevant regulatory
authority to a temporary reference file. Create `/tmp/eu-ai-act-compliance-research.md`:

```markdown
# EU AI Act Compliance Research — [System Name]
## Date: [date]
## Role: [Provider / Deployer / Both]
## Annex III category: [category]

### Primary Legislation
- EU AI Act (Regulation (EU) 2024/1689), OJ L 2024/1689, 12 July 2024
- GDPR (Regulation (EU) 2016/679) — for personal data processing
- Relevant sector regulation: [identify if Annex I regulated product]

### Regulator Guidance
- [EU AI Office guidance, if available: search artificialintelligenceact.eu]
- [Relevant NCA guidance: search [national-authority].gov.eu]
- [EDPB guidance on AI and GDPR: search edpb.europa.eu]
- [Sector-specific guidance: identify regulator, search their site]

### Harmonised Standards
- prEN 18286 (QMS for AI Act regulatory purposes) — public enquiry Oct 2025; not yet
  in force; cited in OJ when available [VERIFY currency]
- CEN/CENELEC JTC 21 harmonised standards under AI Act mandate M/594 [VERIFY progress]

### ISO 42001 Alignment
- ISO/IEC 42001:2023 — AI Management System: voluntary; aligns with Art. 17 QMS but
  does not automatically demonstrate AI Act compliance [VERIFY]
```

**With legalcode-mcp connected:** Search for current regulator guidance, enforcement
decisions, and amendments. Save all relevant results to the reference file. Mark
legalcode-mcp-sourced citations as VERIFIED.

**Without legalcode-mcp:** Proceed with training-data knowledge. Mark all statutory
and regulatory references [VERIFY]. Note in the Glass Box: `legalcode_mcp: "Not connected"`.

### Step 4: Step 0 — Prohibited Practices Screen

**⟁ CLARIFY** — Before assessing high-risk compliance, screen for prohibited practices.
If any of the following describes the system, stop and flag immediately — these systems
are prohibited regardless of other compliance measures (Art. 5, effective 2 Feb 2025):

| Prohibited practice | Basis | Significance |
|--------------------|-------|-------------|
| Subliminal techniques that circumvent free will | Art. 5(1)(a) | Absolute prohibition; no exceptions |
| Exploiting vulnerabilities of specific groups (age, disability) to distort behaviour | Art. 5(1)(b) | Absolute prohibition |
| Social scoring by public authorities for general purpose | Art. 5(1)(c) | Absolute prohibition; some exceptions for internal organisational assessment |
| Real-time remote biometric identification in public spaces (law enforcement) | Art. 5(1)(d) | Prohibited except narrow law enforcement exceptions (national security, missing persons, serious crime) |
| Biometric categorisation inferring political, religious, philosophical beliefs, race, or sexual orientation | Art. 5(1)(e) | Absolute prohibition (new addition in final text) |
| Emotion recognition in workplace and education (except safety or medical purposes) | Art. 5(1)(f) | Absolute prohibition outside narrow exceptions |
| Predictive policing based solely on profiling of individuals | Art. 5(1)(g) | Absolute prohibition |
| Untargeted facial recognition scraping from internet or CCTV | Art. 5(1)(h) | Absolute prohibition |

If the system involves any of the above: **flag as PROHIBITED — immediate legal review
required. Do not proceed with high-risk compliance assessment for this system.**

Ask the user to confirm: "Does your system involve any of the above practices? If yes,
immediate counsel escalation is required before any deployment."

### Step 5: Annex III High-Risk Classification Screening

Determine whether the system falls within an Annex III high-risk category. Apply the
two-stage Article 6 test:

**Stage 1: Does the system fall within an Annex III category?**

| Annex III point | Category | Key sub-categories |
|-----------------|----------|-------------------|
| **1** | Biometrics | Remote biometric identification; biometric categorisation based on sensitive characteristics; emotion recognition |
| **2** | Critical infrastructure | Safety components in management of road traffic, supply of water, gas, heating, or electricity; digital infrastructure |
| **3** | Education and vocational training | Admissions or access allocation; evaluation/assessment of learners; detection of prohibited behaviour during exams |
| **4** | Employment and workers management | Recruitment/selection (CV screening, job ad targeting, interview evaluation); promotion/termination decisions; performance monitoring for contract matters |
| **5** | Essential private and public services | Credit scoring; creditworthiness assessment; life/health insurance risk assessment and pricing; public benefits eligibility; emergency services dispatch prioritisation |
| **6** | Law enforcement | Individual risk assessment (recidivism, criminality prediction); polygraph-like tools; evidence reliability assessment; crime prediction; profiling |
| **7** | Migration, asylum, and border control | Risk assessment for irregular migration; visa/residence permit eligibility; asylum application assessment; document authenticity detection in border control |
| **8** | Administration of justice and democratic processes | Research law for specific cases; judicial outcome prediction; influence on elections or referenda |

**Stage 2: Does the system pose a significant risk of harm? (Art. 6(2) carve-out)**

An Annex III system is **not** considered high-risk if it does not pose a significant
risk of harm to health, safety, or fundamental rights of natural persons, provided:
- The AI system is intended to perform a narrow procedural task
- The AI system is intended to improve the result of a previously completed human activity
- The AI system is intended to detect decision-making patterns or deviations from prior
  decision-making patterns and is not meant to replace or influence the human assessment
- The AI system is intended to perform a preparatory task to an assessment relevant for
  the purposes listed in Annex III

**⟁ CLARIFY** — If the system is in an Annex III category but appears to qualify for
the carve-out: "Does your system (a) only assist humans reviewing prior decisions without
making or influencing the assessment itself, or (b) perform a narrow preparatory task
without influencing the outcome? If yes, document the carve-out basis. Under Art. 6(3),
providers must proactively register the carve-out determination and it is rebuttably
presumed high-risk if challenged."

**Classification output:**
- `HIGH-RISK (Annex III)` — Proceed with full compliance assessment (Steps 6-16)
- `HIGH-RISK (Annex I regulated product)` — Refer to sector-specific conformity
  assessment rules (e.g., MDR for medical devices, Machinery Regulation, AI Act
  requirements apply in addition to sector rules)
- `NOT HIGH-RISK (carve-out)` — Document the carve-out basis; assess for general-purpose
  AI obligations (Chapter V) and transparency obligations (Art. 50) as applicable
- `NOT HIGH-RISK (not in scope)` — Document basis; note transparency obligations

### Step 6: Core Requirements Assessment (Articles 9-15, 17)

For each requirement, classify as:
- `GREEN` — Requirement met with adequate documentation and controls
- `YELLOW` — Requirement approach identified; gaps in implementation or documentation
- `RED` — Requirement not addressed; non-compliant; deployment blocked until remedied

---

#### Requirement 1: Risk Management System (Article 9)

Article 9 requires a **continuous, iterative** risk management process throughout the
entire lifecycle. The system is not a one-time document — it must be continuously updated.

**Four mandatory elements:**

| Element | What it requires | Checklist |
|---------|-----------------|-----------|
| **1. Risk identification and analysis** | Identify known and reasonably foreseeable risks when used as intended AND under reasonably foreseeable misuse. Consider vulnerable groups (Art. 9(9): specific attention to persons under 18). | ☐ Systematic risk log maintained<br>☐ Foreseeable misuse scenarios documented<br>☐ Vulnerable group impact assessed<br>☐ Residual risks identified |
| **2. Risk estimation and evaluation** | Estimate the likelihood and severity of harm. Include both direct and indirect harms (impacts on fundamental rights). | ☐ Likelihood × severity matrix applied<br>☐ Fundamental rights impact assessed<br>☐ Cascade/systemic risks considered |
| **3. Risk management measures** | Adopt targeted measures to address identified risks. Measures must be appropriate to the risk and must eliminate or reduce residual risks to acceptable levels. | ☐ Technical controls implemented<br>☐ Organisational controls implemented<br>☐ Residual risk acceptance documented<br>☐ Measures tested for effectiveness |
| **4. Testing for adequacy** | Test that risk management measures are adequate and effective. Testing must be representative of the intended purpose and real-world conditions. | ☐ Testing plan documents methodology<br>☐ Real-world conditions simulated<br>☐ Results and outcomes documented<br>☐ Post-market feedback loop established |

**Key classification signals:**
- `RED`: No risk log exists; or risks identified but no measures taken; or measures not
  tested
- `YELLOW`: Risk log exists but lacks foreseeable misuse analysis; or testing not yet
  completed; or vulnerable group impact not assessed
- `GREEN`: Systematic, documented risk log; measures tested and effective; regular review
  scheduled

---

#### Requirement 2: Data and Data Governance (Article 10)

**Training, validation, and testing datasets must meet:**

| Requirement | What it requires | Checklist |
|-------------|-----------------|-----------|
| **Relevance** | Datasets must be relevant for the intended purpose | ☐ Dataset selection rationale documented |
| **Representativeness** | Datasets must reflect the population on which the system will operate (geographic, contextual, behavioural) | ☐ Population mapping completed<br>☐ Demographic representation analysed |
| **Free of errors** | Datasets sufficiently free of errors for the intended purpose | ☐ Data quality audit conducted<br>☐ Error rate documented |
| **Completeness** | Datasets have required statistical properties for the intended purpose | ☐ Completeness assessment conducted |
| **Bias examination** | Examine for possible biases that could produce discriminatory outcomes | ☐ Bias audit conducted (at minimum pre-deployment)<br>☐ Bias metrics documented<br>☐ Mitigation measures documented |
| **Data governance practices** | Address design choices, data collection procedures, preparation processing, labelling, storage, aggregation, retention | ☐ Data governance policy documented<br>☐ Data provenance tracked |
| **Special category data** | If training includes special-category data (Art. 9 GDPR): document necessity, apply additional technical safeguards (e.g., anonymisation where feasible) | ☐ Special-category data inventory complete<br>☐ Art. 9 GDPR legal basis documented |

**[JURISDICTION-SPECIFIC]** Article 10(5) permits use of special-category data for bias
monitoring/correction with appropriate safeguards. Some Member States have additional
restrictions on biometric and health data in AI training. Research national supervisory
authority guidance.

**Key classification signals:**
- `RED`: No bias audit; or special-category data used without GDPR legal basis
- `YELLOW`: Bias audit conducted but mitigation incomplete; or representativeness gaps
  documented but not addressed
- `GREEN`: Systematic data governance policy; bias audit with documented mitigations;
  representativeness assessment completed

---

#### Requirement 3: Technical Documentation (Article 11, Annex IV)

Technical documentation must be drawn up **before the system is placed on the market**
and kept up to date. The Commission may adopt delegated acts to amend Annex IV.

**Annex IV required content:**

| Section | Required content | Status |
|---------|-----------------|--------|
| **1. General description** | Name, version, description of intended purpose; for GPAI-based systems: identity of GPAI model provider | ☐ / ☐ |
| **2. Development process** | Design choices and architecture; methods and steps for training and testing; pre-trained components used; computational resources; optimisation techniques; validation procedures | ☐ / ☐ |
| **3. System information** | General description of system operation; interaction with hardware/software; hardware specifications; AI system in market and applicable versions | ☐ / ☐ |
| **4. Monitoring and control** | Human oversight measures built into the system; technical means for logging (Art. 12); measures for robustness and cybersecurity | ☐ / ☐ |
| **5. Accuracy, robustness, cybersecurity** | Declared accuracy metrics; testing methodology; cybersecurity architecture | ☐ / ☐ |
| **6. Instruction for deployers** | Concise, complete instructions in accordance with Art. 13 | ☐ / ☐ |
| **7. Predetermined changes** | For continuously learning systems: description of changes pre-determined by provider at initial conformity assessment that are not substantial modifications | ☐ / ☐ |
| **8. EU Declaration of Conformity** | Copy appended | ☐ / ☐ |

**Key classification signals:**
- `RED`: Technical documentation not initiated; or missing entire sections (e.g., no
  development process documentation)
- `YELLOW`: Partial documentation; gaps in sections 2 (development process) or 5
  (accuracy metrics); not updated to reflect current version
- `GREEN`: Complete Annex IV documentation; updated to current system version; copies
  retained for 10 years post-market (Art. 18)

---

#### Requirement 4: Record-Keeping and Logging (Article 12)

High-risk AI systems must **automatically generate logs** while operating. Logs must
enable monitoring and verification, particularly for market surveillance.

**Required logging capabilities:**

| Log type | When required | Retention |
|----------|--------------|-----------|
| Recording of each operational period (start/end timestamps) | Always | As appropriate to intended purpose |
| Reference database used for verification | When AI uses databases | Duration of system use + post-deployment period |
| Input data submitted to verification | Biometric identification systems (with appropriate data protection rules) | Limited to strict necessity |
| Identity of natural persons performing oversight | For remote biometric ID and other Art. 14(5) systems | Documented oversight logs |
| Output identification data | Always | Appropriate to intended purpose |

**[JURISDICTION-SPECIFIC]** For biometric systems: Member States may restrict log
retention through data protection law. Cross-reference with GDPR Art. 5(1)(e) storage
limitation principle and DPO consultation.

**Key classification signals:**
- `RED`: System cannot generate logs at all; or biometric ID system stores excessive
  input data
- `YELLOW`: Logging capability exists but retention policy not documented; or log format
  not compliant with Art. 12 requirements
- `GREEN`: Automatic logging enabled; retention policy documented and tested; logs
  accessible to market surveillance authorities on request

---

#### Requirement 5: Transparency and Provision of Information to Deployers (Article 13)

High-risk AI systems must operate **transparently** and be accompanied by instructions
for use in digital format (or accompanying documentation for embedded systems).

**Instructions for use must include:**

| Required element | What to document |
|-----------------|-----------------|
| **Provider identity** | Name, address of provider; for EU-registered representative (Art. 22): their details |
| **System characteristics** | Intended purpose; level of accuracy, robustness, cybersecurity; known limitations; AI-generated outputs if applicable |
| **Performance metrics** | Accuracy levels and relevant metrics; discriminatory error rates across demographic groups (if applicable to the use case) |
| **Intended purpose scope** | Specific deployment contexts for which the system is validated; contexts NOT suitable for use |
| **Human oversight information** | Measures designed into the system; how the human oversight person should interpret outputs; limitations on output interpretation |
| **IT environment requirements** | Hardware, software, cybersecurity requirements |
| **Maintenance requirements** | Calibration, servicing, update requirements; expected lifetime |
| **Logging reference** | Where logs are stored; how to access them for oversight |

**Key classification signals:**
- `RED`: No instructions for use exist; or instructions too technical for deployers to
  understand operational limitations
- `YELLOW`: Instructions exist but incomplete — missing accuracy/limitation section or
  human oversight guidance
- `GREEN`: Complete, accessible instructions covering all Annex IV(6) elements; available
  in languages required by Member States where marketed

---

#### Requirement 6: Human Oversight (Article 14)

High-risk AI systems must be designed with **built-in human oversight measures** enabling
deployers to effectively monitor, interpret, and override the system.

**Required oversight capabilities (provider obligations — design-level):**

| Capability | Requirement | Checklist |
|-----------|------------|-----------|
| **Understandability** | Human overseers must be able to understand capabilities and limitations; detect anomalies, dysfunctions, and unexpected performance | ☐ System outputs interpretable by non-technical overseers<br>☐ Anomaly detection outputs documented |
| **Non-automaticity** | Human overseers must be able to decide NOT to use the system's output and not over-rely on automation | ☐ Output clearly marked as AI-generated<br>☐ Override mechanism exists and is documented |
| **Override capability** | Ability to interrupt, stop, or override the system | ☐ Manual override implemented<br>☐ Stop-the-line procedure documented |
| **Feedback mechanism** | Deployers must be able to report issues to the provider | ☐ Issue reporting channel documented in instructions |

**Special rule for remote biometric identification (Art. 14(5)):** Any action or decision
based on real-time remote biometric identification used by law enforcement must be
verified and confirmed by at least two competent natural persons independently of the AI
system, unless urgency makes this impractical.

**Deployer obligations (Art. 26(2)):** Deployers must assign human oversight to competent
natural persons and provide them with the necessary authority, resources, and training.

**Key classification signals:**
- `RED`: No override mechanism exists in the system architecture; or instructions do not
  explain how to interpret outputs or activate override
- `YELLOW`: Override mechanism exists but not adequately documented; or deployer has not
  designated an oversight person
- `GREEN`: Human oversight built into system design; override tested and documented; Art.
  14 requirements reflected in instructions for use and QMS

---

#### Requirement 7: Accuracy, Robustness, and Cybersecurity (Article 15)

**Accuracy requirements:**

| Dimension | Requirement | Checklist |
|-----------|------------|-----------|
| **Accuracy level** | Achieve appropriate level of accuracy for the intended purpose throughout lifecycle; declare accuracy level and relevant metrics in instructions for use | ☐ Accuracy metrics defined<br>☐ Metrics declared in instructions<br>☐ Accuracy tested across relevant sub-groups |
| **Robustness** | Resilient to errors, faults, inconsistencies in inputs and operating environment; technical redundancy/fail-safe where needed | ☐ Robustness testing documented<br>☐ Fail-safe plans documented |
| **Feedback loop prevention** | Continuously learning systems: eliminate or reduce risk of biased outputs feeding future training data (feedback loops) | ☐ Feedback loop risk assessment conducted<br>☐ Mitigation controls documented |
| **Cybersecurity** | Resilient against unauthorised third-party attempts to alter use, outputs, or performance by exploiting system vulnerabilities | ☐ Cybersecurity architecture documented<br>☐ Penetration testing or equivalent conducted<br>☐ Vulnerability management process documented |

**Key classification signals:**
- `RED`: Accuracy metrics not defined or not tested; or continuously learning system
  with no feedback loop controls; or no cybersecurity controls
- `YELLOW`: Accuracy defined but not tested at sub-group level; or cybersecurity
  documented but not tested
- `GREEN`: Accuracy metrics defined, declared, and tested; robustness tested; cybersecurity
  controls implemented and reviewed against known AI attack patterns (adversarial ML,
  model inversion, prompt injection where applicable)

---

#### Requirement 8: Quality Management System (Article 17)

Providers must put in place a **documented QMS** in written policies, procedures, and
instructions covering all aspects of high-risk AI compliance. Proportionate to organisation
size — but the degree of rigor must ensure compliance.

**QMS mandatory components:**

| Component | What it must address | Checklist |
|-----------|---------------------|-----------|
| **Regulatory compliance strategy** | How the organisation ensures ongoing AI Act compliance; roles and responsibilities | ☐ Documented<br>☐ Responsibility matrix assigned |
| **Design and development procedures** | Techniques and procedures for design, development, and validation | ☐ Documented<br>☐ Referenced in technical documentation |
| **Data management systems** | Data acquisition, collection, analysis, labelling, storage, filtration, aggregation, retention | ☐ Documented<br>☐ Aligned with Art. 10 |
| **Risk management procedures** | How Art. 9 risk management is conducted and documented | ☐ Documented<br>☐ Linked to risk log |
| **Quality control and assurance** | Examination, test, and validation procedures | ☐ Documented<br>☐ Test results retained |
| **Post-market monitoring** | How PMM plan (Art. 72) is maintained and acted upon | ☐ Documented<br>☐ PMM plan completed |
| **Incident reporting** | Procedures for identifying and reporting serious incidents (Art. 73) | ☐ Documented<br>☐ Thresholds and contacts defined |
| **Communication with authorities** | Procedures for market surveillance authority interactions | ☐ Documented<br>☐ Contact list maintained |
| **Record-keeping** | Document management, retention periods (10 years for conformity docs), access controls | ☐ Documented<br>☐ Retention schedule in place |
| **Resource management** | Budget, personnel, expertise to maintain compliance | ☐ Documented<br>☐ Ownership assigned |
| **Accountability framework** | Who is accountable for what; escalation paths | ☐ Documented<br>☐ Board/executive sign-off obtained |

**Note on prEN 18286:** The draft EU AI Act harmonised standard for QMS entered public
enquiry October 2025. Once cited in the Official Journal, conformity with prEN 18286
creates a rebuttable presumption of AI Act QMS compliance. [VERIFY: OJ citation status]

**Integration with existing QMS (Art. 17(3)):** Providers subject to QMS requirements
under sector-specific EU law (e.g., MDR for medical devices, ISO 9001 in regulated
sectors) may integrate AI Act QMS requirements into those existing systems, provided
equivalent safeguards are maintained.

**Key classification signals:**
- `RED`: No QMS exists; or major components (incident reporting, post-market monitoring)
  completely absent
- `YELLOW`: QMS framework exists but lacks specific AI Act components (e.g., no PMM
  procedure, no incident reporting thresholds, no Art. 9 linkage)
- `GREEN`: Complete, documented QMS; all 11 components present; updated to reflect
  current system version; reviewed at least annually

---

### Step 7: Conformity Assessment Path Determination (Article 43)

**⟁ CLARIFY** — The conformity assessment path depends on the Annex III category and
whether harmonised standards have been applied. Ask: "Have you applied all relevant
harmonised standards (CEN/CENELEC standards under AI Act mandate M/594) to your system?
If not, you may require notified body involvement."

**Path determination:**

| Condition | Required path | Notes |
|-----------|-------------|-------|
| **Annex III, point 1 (biometric ID)** AND **did not apply harmonised standards** | **Annex VII** — Notified body mandatory | Third-party assessment of QMS and technical documentation |
| **Annex III, point 1** AND **applied harmonised standards** | Provider may choose **Annex VI** or **Annex VII** | Self-assessment permitted but notified body may strengthen trust |
| **Annex III, points 2-8** AND any standard/specification status | **Annex VI** — Internal control (self-assessment) | No notified body required for non-biometric Annex III systems |
| **Annex I (regulated product sector)** | Sector-specific conformity assessment | AI Act requirements must be integrated into sector conformity process (MDR, Machinery Reg., etc.) |

**Annex VI — Internal Control procedure (self-assessment):**

| Step | Action |
|------|--------|
| 1 | Verify QMS complies with Art. 17 |
| 2 | Examine technical documentation for compliance with Arts. 8-15 |
| 3 | Verify design/development process and PMM plan are consistent with technical documentation |
| 4 | Draw up EU Declaration of Conformity (Art. 49) |
| 5 | Affix CE marking (Art. 71) |
| 6 | Register in EU AI database (Art. 71) before market placement |

**Annex VII — Quality Management System and Technical Documentation Assessment (notified body):**

| Step | Action |
|------|--------|
| 1 | Apply to an accredited notified body (EU AI Office publishes list) |
| 2 | Submit QMS application |
| 3 | Notified body examines QMS and technical documentation |
| 4 | Notified body issues Union technical documentation assessment certificate |
| 5 | Certificate validity: 4 years (renewable); must notify notified body of system changes |
| 6 | Draw up EU Declaration of Conformity and affix CE marking |

### Step 8: EU Declaration of Conformity and CE Marking (Articles 49, 71)

**EU Declaration of Conformity must declare:**
- Provider name and address
- EU AI Act compliance (all Arts. 8-15, 17 requirements met)
- AI system identity (name, version, intended purpose)
- Conformity assessment procedure followed (Annex VI or VII)
- Reference to harmonised standards or common specifications applied
- Date and place of issue; authorised signatory

**CE marking requirements (Art. 71):**
- CE marking affixed before placing on EU market or putting into service
- Visible, legible, and indelible marking on the AI system, its packaging, or accompanying documentation
- Where CE marking cannot be affixed (e.g., software-only systems), mark on packaging or documentation

**EU AI database registration (Art. 71(1)):**
- Provider must register in EU AI database **before** market placement
- Deployers of Annex III systems used in public bodies must also register (Art. 49(2))
- Registration includes: provider info, system name/version, intended purpose, Annex III category, conformity assessment reference, certification status

### Step 9: Post-Market Monitoring (Article 72)

**Post-market monitoring plan (PMM plan):**

The PMM plan is a mandatory component of technical documentation (Annex IV). Commission
implementing act establishing PMM plan template due by 2 February 2026 — [VERIFY: issued].

**PMM system requirements:**

| Element | Requirement |
|---------|------------|
| **Active data collection** | Systematically collect, document, and analyse relevant data on system performance throughout its lifetime |
| **Deployer data** | Data may be provided by deployers or collected from other sources |
| **Continuous compliance evaluation** | Data must enable ongoing assessment of compliance with Arts. 8-15 |
| **AI interaction analysis** | Where relevant, analyse interaction with other AI systems |
| **Serious incident triggering** | PMM data that reveals a serious incident must trigger Art. 73 reporting |
| **Substantial modification triggering** | PMM findings that reveal need for substantial modification require new conformity assessment |

**Deployer reporting obligations (Art. 26(5)):** Deployers must inform the provider of
any serious incidents they become aware of, enabling the provider to fulfil Art. 73.

**Integration:** Providers subject to existing sector-specific monitoring obligations
(e.g., MDR post-market surveillance) may integrate AI Act PMM into those systems where
equivalent safeguards are maintained.

### Step 10: Serious Incident Reporting Readiness (Article 73)

**Definition of "serious incident"** (Art. 3(49)):
An incident or malfunction directly or indirectly resulting in:
- (a) Death or serious harm to health of a natural person
- (b) Serious and irreversible disruption to management/operation of critical infrastructure
- (c) Infringement of EU law obligations intended to protect fundamental rights
- (d) Serious harm to property or the environment

**Reporting timelines:**

| Severity | Who reports | Deadline |
|----------|------------|---------|
| General serious incident | Provider (or deployer to provider who then reports) | **15 days** after causal link established (or reasonable likelihood thereof) |
| Death of a person | Provider | **10 days** after causal link established or suspected |
| Widespread infringement or large-scale serious incident | Provider | **2 days** after awareness |
| Incomplete initial report | Provider | Permissible; must follow up with complete report |

**Report to:** Market surveillance authority of the Member State where incident occurred
(deployers report to both the competent authority of their Member State and the provider).

**Reporting readiness checklist:**

| Element | Status |
|---------|--------|
| ☐ Serious incident thresholds documented in QMS | |
| ☐ Internal triage procedure for potential serious incidents documented | |
| ☐ Contact details for relevant Member State market surveillance authorities maintained | |
| ☐ Deployer communication channel for incident notification established | |
| ☐ Legal review of "causal link" threshold documented | |
| ☐ 2-day/10-day/15-day clock management procedure documented | |
| ☐ Root cause investigation procedure documented (without altering system before informing authority) | |
| ☐ EU AI Office notified if incident has multiple Member State impact | |

**Key classification signals:**
- `RED`: No incident reporting procedure; no contact details for market surveillance
  authorities; no awareness of reporting timelines
- `YELLOW`: Incident reporting procedure exists but lacks AI Act-specific thresholds;
  or deployer communication channel not established
- `GREEN`: Complete incident reporting procedure covering all three timelines;
  tested against scenarios; market surveillance authority contacts maintained; QMS
  linkage documented

### Step 11: GDPR DPIA Cross-Reference

**⟁ CLARIFY** — Does the AI system process personal data (directly or indirectly)?
If no personal data processing: this step is not applicable. If yes: proceed.

**DPIA trigger analysis:**

A GDPR DPIA (Art. 35) is required if processing is "likely to result in a high risk to
the rights and freedoms of natural persons." High-risk AI systems processing personal
data will almost always require a DPIA. Specific triggers:

| Trigger | Applies to |
|---------|-----------|
| Systematic and extensive evaluation of personal aspects based on automated processing | Employment, credit, insurance Annex III systems |
| Processing of special-category data on large scale | Biometric, health, racial/ethnic origin |
| Systematic monitoring of publicly accessible area on large scale | Remote biometric ID, critical infrastructure systems |
| Innovative technology or new organisational context | Most high-risk AI systems |

**Coordination principle (Recital 95 AI Act):** The AI Act conformity assessment does
NOT replace the GDPR DPIA. Both assessments must be conducted. However, they can and
should be coordinated to share factual findings and avoid duplication:
- Art. 9 risk assessment findings inform GDPR DPIA harm analysis
- DPIA's data protection safeguards inform Art. 9 risk management measures
- GDPR DPIA result feeds back into Art. 15 accuracy and fundamental rights impact

**Action:** If not already initiated, trigger `legalcode-dpia-generator` skill for the
personal data processing component. Record cross-reference in both documents.

---

### Step 12: Severity Classification and Overall Compliance Determination

**Overall compliance classification (4-tier):**

| Classification | Meaning | Action |
|---------------|---------|--------|
| **COMPLIANT** | All applicable AI Act requirements met; conformity assessment ready | Proceed to CE marking and registration |
| **PARTIAL** | Material compliance achieved; specific gaps require remediation; system may not be placed on market until gaps resolved | Prioritised remediation roadmap; target compliance date |
| **NON-COMPLIANT** | Significant violations across multiple requirement areas; deployment blocked | Comprehensive remediation programme; estimated timeline and cost |
| **CRITICAL** | Risk to fundamental rights, safety, or legality; or prohibited practice identified | Immediate legal escalation; suspend any market placement |

**Per-requirement classification summary:**

| Requirement | Article | Classification | Key gap (if any) | Priority |
|-------------|---------|---------------|-----------------|---------|
| Prohibited practices screen | Art. 5 | | | |
| High-risk classification | Art. 6 / Annex III | | | |
| Risk management system | Art. 9 | | | |
| Data governance | Art. 10 | | | |
| Technical documentation | Art. 11 / Annex IV | | | |
| Record-keeping / logging | Art. 12 | | | |
| Transparency / instructions | Art. 13 | | | |
| Human oversight | Art. 14 | | | |
| Accuracy / robustness / security | Art. 15 | | | |
| Quality management system | Art. 17 | | | |
| Conformity assessment | Art. 43 | | | |
| CE marking / Declaration | Arts. 49, 71 | | | |
| Post-market monitoring | Art. 72 | | | |
| Serious incident reporting | Art. 73 | | | |
| GDPR DPIA | GDPR Art. 35 | | | |

### Step 13: Quality Verification

Before delivering output, run the quality frameworks below. See [Quality Assurance
Framework] section for full procedures.

1. Run Citation Quality Gates (5 gates)
2. Apply Self-Interrogation to all RED findings (3-pass)
3. Verify all [VERIFY] and [CHECK CURRENCY] tags are present where needed
4. Confirm output follows the Output Format Template
5. Complete the Glass Box audit trail

---

## Severity Classification System

### Per-Requirement Classification

| Tier | Symbol | Meaning |
|------|--------|---------|
| **COMPLIANT** | ✅ | Requirement met; documentation adequate; controls tested |
| **PARTIAL** | ⚠️ | Requirement partially addressed; gaps identified; remediation path clear |
| **NON-COMPLIANT** | ❌ | Requirement not addressed or materially deficient; deployment blocked |
| **NOT APPLICABLE** | ➖ | Requirement does not apply to this system (with documented basis) |

### Overall Classification

| Classification | When to use |
|---------------|------------|
| **COMPLIANT** | All requirements GREEN or NOT APPLICABLE; conformity assessment ready |
| **PARTIAL** | Mix of GREEN and YELLOW findings; no RED findings; or isolated RED with documented remediation timeline |
| **NON-COMPLIANT** | One or more RED findings without remediation timeline; or multiple YELLOW findings in core requirements |
| **CRITICAL** | Prohibited practice identified; or imminent serious incident risk; or fundamental rights violation without remediation |

---

## Actionable Output Per Finding

For each identified gap, document using this template:

```
Finding ID: [AI-001, AI-002, ...]
Article: [EU AI Act Art. X / Annex X]
Requirement area: [Risk management / Data governance / ...]
Classification: [COMPLIANT / PARTIAL / NON-COMPLIANT]
Finding: [Specific description of the gap or failure]
Business impact if unresolved: [Enforcement risk, market access blocked, fundamental
  rights exposure, fine exposure (up to €15M or 3% global turnover)]
Recommended action: [Specific, measurable action — not "improve documentation" but
  "Draft and approve Art. 9 risk log template using the structure in Annex IV(2) by
  [date]; assign risk management owner by [date]"]
Remediation owner: [Role or team]
Target date: [Specific date — relative to 2 August 2026 deadline]
Evidence required: [What proves this is complete, e.g., "Signed-off Art. 9 risk log
  with at least 5 identified risk scenarios, approved by AI governance lead and
  retained in QMS document management system"]
Escalation: [If NON-COMPLIANT: Legal/AI governance lead sign-off required before
  market placement; if CRITICAL: Immediate legal escalation + board notification]
```

---

## Prioritization Framework

### Tier 1 — Critical / Pre-Market Blocker

Must resolve before placing on EU market. These issues block CE marking and registration:
- Any prohibited practice identified (Art. 5)
- No risk management system at all (Art. 9)
- No conformity assessment completed (Art. 43)
- No EU Declaration of Conformity (Art. 49)
- No CE marking (Art. 71)
- Not registered in EU AI database (Art. 71)
- No instructions for use at all (Art. 13)

### Tier 2 — High / Enforcement Deadline Blocker

Must resolve by 2 August 2026. Material non-compliance with core requirements:
- Risk management system lacks one or more of the four mandatory elements
- Bias audit not conducted or materially deficient
- Technical documentation missing entire sections (e.g., no development process, no
  accuracy metrics)
- Human oversight override mechanism not implemented
- QMS missing major components (no PMM procedure, no incident reporting procedure)
- Logging capability not implemented

### Tier 3 — Medium / Best Practice Compliance

Should resolve within 90 days of market placement:
- Risk management system conducted but not reviewed in last 12 months
- Technical documentation exists but not updated to current system version
- Instructions for use technically accurate but difficult for deployers to understand
- QMS documented but audit/review cycle not established
- PMM plan exists but data collection not operationalised
- Incident reporting procedure exists but market surveillance authority contacts not
  verified

### Tier 4 — Low / Continuous Improvement

Address over time (ongoing programme):
- ISO/IEC 42001 certification (voluntary but strengthens QMS presumption)
- Harmonised standard conformity beyond current requirements
- Advanced bias monitoring with continuous production data analysis
- Stakeholder feedback integration into PMM
- Participation in EU AI regulatory sandbox

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate | Rule | Fail action |
|------|------|------------|
| **Source** | Every legal claim cites a specific EU AI Act article, recital, Annex, or official regulator guidance | Add citation or mark [VERIFY] |
| **Format** | All citations follow: "EU AI Act Art. X / Recital Y / Annex Z / [Regulator] [guidance title]" | Fix format to standardised pattern |
| **Currency** | Every provision checked against the August 2024 OJ final text; regulator guidance checked for superseding updates | Flag [CHECK CURRENCY] for pre-2024 guidance; note EU AI Act final text vs. proposal versions |
| **Domain** | Analysis stays within EU AI Act framework; non-EU frameworks (NIST AI RMF, UK AI Safety, etc.) noted separately as voluntary benchmarks | Isolate non-EU analysis; do not conflate with legal obligations |
| **Confidence** | Uncertainty explicitly stated; no YELLOW findings presented as GREEN; no PARTIAL findings as COMPLIANT | Add confidence qualifier with rationale |

### Self-Interrogation for NON-COMPLIANT Findings

For any finding classified NON-COMPLIANT, apply this 3-pass adversarial review before
delivering:

**Pass 1 — Legal Chain Integrity**
Does the NON-COMPLIANT classification follow logically from the cited article and recital?
Would a market surveillance authority actually reach this conclusion on these specific
facts? Is this based on settled regulatory interpretation or on an emerging position?

**Pass 2 — Completeness**
Have all relevant AI Act provisions, recitals, and regulator guidance been considered?
Are there sector-specific exemptions or accommodations (e.g., SME proportionality
provisions, regulatory sandbox protections) that apply? Have all available mitigations
been evaluated?

**Pass 3 — Challenge**
What is the strongest argument that this finding should be classified PARTIAL rather
than NON-COMPLIANT? Under what circumstances might a market surveillance authority
accept a lesser standard? If the challenge is strong, downgrade to PARTIAL and specify
what additional information or control would be needed to confirm NON-COMPLIANT.

If any pass reveals a weakness: revise the classification and document the revision in
the Glass Box audit trail with `self_interrogation: "REVISED — [reason]"`.

### Confidence Scoring

| Level | Range | Meaning | Prescribed action |
|-------|-------|---------|------------------|
| **Definite** | 0.95–1.0 | Settled law; clear statutory text; explicit Art./Annex requirement | State with confidence |
| **High** | 0.80–0.94 | Strong basis; consistent with clear legislative intent; regulator guidance confirms | State with brief caveat |
| **Probable** | 0.60–0.79 | Good interpretive basis; regulatory position not yet confirmed in enforcement; reasonable competing view | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; evolving area; no regulator guidance yet; competing views in literature | Flag for legal review; present both sides |
| **Unlikely** | 0.00–0.39 | Weak basis; speculative; contradicted by regulatory text or emerging guidance | Do not assert; flag [UNCERTAIN]; escalate to qualified counsel |

---

## Glass Box Audit Trail

Include this YAML block at the end of every compliance assessment output:

```yaml
glass_box:
  skill_name: "legalcode-eu-ai-act-high-risk-compliance"
  topic: "EU AI Act (Regulation 2024/1689) High-Risk AI System Compliance Assessment"
  ai_system_name: "[System name or description]"
  ai_system_version: "[Version]"
  annex_iii_category: "[Category or 'Not high-risk — basis: ...']"
  role_assessed: "[Provider / Deployer / Both]"
  assessment_date: "[YYYY-MM-DD]"
  assessor: "[Name or role of assessor]"
  target_deadline: "2 August 2026 (high-risk enforcement date)"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  prohibited_practices_screen: "PASSED / FAILED — [brief summary]"
  high_risk_classification: "HIGH-RISK / NOT HIGH-RISK / CARVE-OUT — [basis]"
  overall_classification: "COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL"
  requirement_summary:
    art_9_risk_management: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_10_data_governance: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_11_technical_docs: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_12_logging: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_13_transparency: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_14_human_oversight: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_15_accuracy_robustness: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_17_qms: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_43_conformity_assessment: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_49_71_ce_marking: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_72_pmm: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    art_73_incident_reporting: "[COMPLIANT / PARTIAL / NON-COMPLIANT]"
    gdpr_dpia: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT APPLICABLE]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation_applied: "[number of NON-COMPLIANT findings reviewed]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires review by a qualified EU AI Act legal counsel"
```

---

## Anti-Patterns

Do not do the following when conducting or documenting an EU AI Act high-risk compliance
assessment.

1. **Treating the Art. 6(2) "significant risk" carve-out as an automatic exemption.**
   The carve-out requires proactive provider determination and documentation. It is
   rebuttably presumed that Annex III systems ARE high-risk — the burden is on the
   provider to demonstrate the carve-out applies. Providers who rely on the carve-out
   without documentation expose themselves to enforcement risk; market surveillance
   authorities can overturn undocumented carve-out claims without notice.

2. **Conflating provider and deployer obligations.** The bulk of AI Act obligations fall
   on providers. Deployers have a narrower but real obligation set (Art. 26: assign
   human oversight, use within intended purpose, monitor for risks, report incidents).
   A deployer who assumes the provider has handled "all the compliance" and does nothing
   is not compliant — particularly regarding human oversight designation (Art. 26(2)).

3. **Missing the Art. 25 provider-by-modification trigger.** A deployer who puts their
   name or trademark on a third-party high-risk AI system, makes a substantial
   modification, or changes the intended purpose to create high-risk classification,
   automatically assumes full provider obligations. "Substantial modification" remains
   vaguely defined; document the basis for any determination that a modification is
   NOT substantial.

4. **Treating risk management as a one-time document.** Article 9 requires a
   "continuous iterative process planned and run throughout the entire lifecycle."
   Filing a risk log before market placement and never updating it is a common
   audit failure pattern. The PMM plan must feed back into the risk management
   system; new incident data, user feedback, and operational performance must
   trigger risk log review.

5. **Bias audit conducted only on training data, not production performance.** Article
   10 requires data quality and bias assessment during development, but Article 72
   post-market monitoring requires ongoing analysis of production data. Systems
   experiencing distribution shift — where production data differs from training data
   — may exhibit bias that training-time audits did not catch. Establish production
   bias monitoring from day one.

6. **Technical documentation written after conformity assessment rather than during
   development.** Article 11 requires technical documentation to be drawn up before
   market placement and kept up to date throughout development. Creating documentation
   retroactively is both harder (institutional knowledge may be lost) and suspect to
   market surveillance authorities examining its authenticity. Build documentation
   as part of the development workflow, not as a pre-launch compliance sprint.

7. **Instructions for use written for engineers, not deployers.** Article 13 exists
   to enable deployers to use the system appropriately and deploy effective human
   oversight. Instructions drafted in highly technical language that a deployer's
   non-technical compliance officer cannot understand fail the Art. 13 purpose.
   Test instructions with intended deployer audiences before market placement.

8. **Treating human oversight as a declaration rather than a design requirement.**
   Article 14 requires human oversight to be built into the system design — not
   added as a policy statement in the instructions. A system that produces outputs
   that are practically impossible to override (e.g., because automated decisions
   are executed within milliseconds of output) does not comply with Art. 14
   regardless of what the instructions say.

9. **Conducting Annex VI self-assessment without the documented rigor of a notified-body
   review.** The internal control path (Annex VI) is self-assessment — but it must be
   conducted with the same analytical rigor as if a notified body were reviewing.
   Superficial internal assessments that check boxes without genuine analysis are an
   audit failure pattern highlighted by the Notified Body Coordination Group's 2025
   conformity assessment framework review.

10. **Failing to coordinate the AI Act conformity assessment with the GDPR DPIA.**
    Recital 95 AI Act explicitly notes that conformity assessment does not replace
    GDPR DPIA requirements. Running both assessments entirely in parallel without
    coordination leads to duplicated effort and inconsistent findings — the Art. 9
    risk scenarios should inform and align with the GDPR DPIA harm analysis. A
    supervisory authority reviewing a DPIA for a high-risk AI system will expect
    cross-references to the AI Act compliance documentation.

11. **Post-market monitoring as a paper plan with no operational data collection.**
    Many organisations draft a PMM plan to satisfy Annex IV requirements but do not
    operationalise it — there is no actual data collection, no feedback channel from
    deployers, no analysis of operational logs. When a serious incident occurs or a
    market surveillance inspection happens, the absence of PMM data is a serious
    aggravating factor. PMM must be live from day one of market placement.

12. **Not establishing incident reporting thresholds in advance.** Article 73 requires
    reports within 2, 10, or 15 days depending on severity — starting from the moment
    awareness is established. Organisations that try to decide whether an incident is
    "serious" in real time, without pre-defined thresholds and triage procedures,
    routinely miss reporting deadlines. Define thresholds for each category of serious
    incident in the QMS before market placement and test the procedure.

13. **Relying on GPAI model provider's compliance to cover downstream obligations.**
    Where a high-risk AI system is built on top of a GPAI model (e.g., large language
    model foundation), the provider of the high-risk system cannot rely entirely on the
    GPAI model provider's AI Act compliance. The high-risk system provider must still
    comply with Arts. 9-17, 43 in respect of their own system — even if built on a
    compliant GPAI model. The GPAI provider's obligations under Chapter V are separate
    and concurrent, not a substitute.

14. **SME proportionality as a blanket exemption from core requirements.**
    Article 17(2) states that QMS implementation "shall be proportionate to the size
    of the provider's organisation" — but then immediately provides: "providers shall,
    in any event, respect the degree of rigor and the level of protection required to
    ensure compliance." The proportionality provision affects documentation depth and
    formality, not the substance of the requirements. A startup must still have a risk
    management system, data governance procedures, and logging capability — even if
    these are lighter-weight than an enterprise QMS.

15. **Treating harmonised standards as mandatory.** The AI Act operates on a "new
    legislative framework" model: harmonised standards are voluntary, but conformity
    with a harmonised standard cited in the Official Journal creates a rebuttable
    presumption of compliance. This means non-application of harmonised standards
    (e.g., prEN 18286 for QMS) does not automatically mean non-compliance — but the
    provider must demonstrate compliance through other means. Conversely, mechanically
    applying a harmonised standard without understanding whether it genuinely addresses
    the specific system's risks does not guarantee compliance.

16. **Not registering in the EU AI database before market placement.** Article 71(1)
    requires providers to register the AI system in the EU AI database operated by
    the European Commission before placing on the market. Many providers focus on CE
    marking and conformity assessment but forget registration — which is a separate
    legal obligation with its own timeline. Deployers of Annex III systems used in
    public bodies must also register (Art. 49(2)).

17. **Ignoring Article 50 transparency obligations for AI systems that interact with
    natural persons.** Article 50 (transparency obligations for certain AI systems,
    separate from Art. 13) requires high-risk AI systems that interact with natural
    persons to inform those persons that they are interacting with an AI system, unless
    this is obvious from context. Emotion recognition and biometric categorisation
    systems must notify persons on whose data they operate. These are end-user-facing
    obligations distinct from the deployer-facing instructions for use under Art. 13.

---

## Writing Standards

Apply these standards before delivering any EU AI Act compliance assessment output.

**Plain language discipline:**
- Write in active voice: "The provider must establish a risk management system" not
  "A risk management system must be established by the provider"
- Name the actor: "The deployer must assign a human oversight person" not "A human
  oversight person must be assigned"
- One point per sentence in the findings register; short sentences in analysis sections
- Avoid vague qualifiers ("may," "might") in COMPLIANT findings; use them in PARTIAL
  findings to convey genuine uncertainty

**Precision in legal claims:**
- Every legal claim cites the specific AI Act article, recital, or Annex
- Every [VERIFY] tag includes a brief explanation of what needs verification and why
- Never state a PARTIAL finding as COMPLIANT; never round up confidence from POSSIBLE
  to PROBABLE

**Quality gates before delivery:**
1. Can a compliance officer who is not an AI Act specialist understand each finding
   and recommended action?
2. Can the finding owner take the recommended action without additional legal advice?
3. Is every legal claim supported by a citation or marked [VERIFY]?
4. Does the output match the structure in the Output Format Template?
5. Has the Glass Box audit trail been completed with all mandatory fields?
6. Have all NON-COMPLIANT findings been through the three-pass self-interrogation?
7. Does the output state the overall classification clearly and prominently (not buried
   at the end)?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool
for retrieving EU AI Act provisions, regulator guidance, and case law.

**With legalcode-mcp connected (preferred):**
- In Step 3, search for current EU AI Office guidance on Annex III categories
- Search for national competent authority guidance in the target Member State(s)
- Verify currency of prEN 18286 harmonised standard (OJ citation status)
- Search for sector-specific AI governance guidance (EBA, ESMA, EFSA, EMEA, etc.)
- Search for EDPB guidance on AI and GDPR for DPIA cross-reference
- Save the most relevant results to `/tmp/eu-ai-act-compliance-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Proceed with training-data knowledge of EU AI Act final text (OJ 12 July 2024)
- Mark all regulatory guidance references [VERIFY] — these evolve rapidly
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Recommend the user consult:
  - Official EU AI Act text: eur-lex.europa.eu (Regulation (EU) 2024/1689)
  - EU AI Act explanation: artificialintelligenceact.eu
  - EU AI Office: digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
  - AI Act Service Desk: ai-act-service-desk.ec.europa.eu

---

## Output Format Template

Every EU AI Act compliance assessment must follow this template:

```markdown
# EU AI Act High-Risk Compliance Assessment — [AI System Name]

**Organisation**: [Name or "Not specified"]
**Assessment date**: [YYYY-MM-DD]
**Assessor**: [Name/role]
**AI system version**: [Version]
**Role assessed**: [Provider / Deployer / Both]
**Annex III category**: [Category or "Not applicable — [basis]"]
**Primary enforcement deadline**: 2 August 2026

---

## Executive Summary

**Overall classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

| Requirement area | Article | Classification | Confidence |
|-----------------|---------|---------------|-----------|
| Prohibited practices screen | Art. 5 | ✅ / ❌ | HIGH / PROBABLE |
| High-risk classification | Art. 6 / Annex III | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Risk management system | Art. 9 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Data governance | Art. 10 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Technical documentation | Art. 11 / Annex IV | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Record-keeping / logging | Art. 12 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Transparency / instructions | Art. 13 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Human oversight | Art. 14 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Accuracy / robustness / security | Art. 15 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Quality management system | Art. 17 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Conformity assessment | Art. 43 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| CE marking / Declaration | Arts. 49, 71 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Post-market monitoring | Art. 72 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| Serious incident reporting | Art. 73 | ✅ / ⚠️ / ❌ | HIGH / PROBABLE |
| GDPR DPIA | GDPR Art. 35 | ✅ / ⚠️ / ❌ / ➖ | HIGH / PROBABLE |

**Key finding**: [One sentence — what drives the overall outcome]
**Recommended next action**: [One sentence — highest priority action]
**Estimated time to compliance**: [X weeks / months — relative to current gaps]

---

## Classification Determination

### Prohibited Practices Screen
[Whether system involves any Art. 5 prohibited practice — PASSED or FAILED with basis]

### High-Risk Classification
[Whether system is within Annex III or Annex I; carve-out analysis if applicable]
**Classification**: [HIGH-RISK (Annex III, point X) / NOT HIGH-RISK / CARVE-OUT]
**Confidence**: [Level and rationale]

---

## Requirement-by-Requirement Assessment

### Risk Management System (Article 9)
**Classification**: ✅ COMPLIANT / ⚠️ PARTIAL / ❌ NON-COMPLIANT

| Element | Status | Finding |
|---------|--------|---------|
| Risk identification and analysis | ✅ / ⚠️ / ❌ | [Detail] |
| Risk estimation and evaluation | ✅ / ⚠️ / ❌ | [Detail] |
| Risk management measures | ✅ / ⚠️ / ❌ | [Detail] |
| Testing adequacy | ✅ / ⚠️ / ❌ | [Detail] |

[Repeat structure for each of Arts. 10, 11, 12, 13, 14, 15, 17, 43, 49/71, 72, 73]

---

## Findings and Remediation Plan

| Finding ID | Article | Classification | Finding | Recommended action | Owner | Due | Evidence |
|-----------|---------|---------------|---------|-------------------|-------|-----|---------|
| AI-001 | Art. X | ❌ NON-COMPLIANT | [Description] | [Specific action] | [Role] | [Date] | [Evidence] |
| AI-002 | Art. X | ⚠️ PARTIAL | [Description] | [Specific action] | [Role] | [Date] | [Evidence] |

---

## Conformity Assessment Preparation

**Path**: Annex VI (internal control) / Annex VII (notified body required)
**Notified body**: [Name or "Not yet selected"]
**Harmonised standards applied**: [List or "None — alternative compliance approach"]
**EU Declaration of Conformity**: Drafted / Not yet drafted
**CE marking**: Applied / Not yet applied
**EU database registration**: Completed / Not yet completed / Registration number: [X]

---

## GDPR DPIA Status

**Personal data processing**: Yes / No
**DPIA required**: Yes / No / Assessment required
**DPIA status**: Completed / In progress / Not yet initiated
**Cross-reference**: [Link to DPIA or legalcode-dpia-generator output]

---

## Post-Market Monitoring and Incident Reporting

**PMM plan status**: Documented and operational / Documented but not operational /
Not documented
**Incident reporting procedure**: Documented / Not documented
**Market surveillance authority contacts**: Maintained / Not yet established

---

## Prioritised Action Plan

**Tier 1 — Resolve before market placement (critical):**
1. [Action with owner and date]

**Tier 2 — Resolve by 2 August 2026 (high):**
1. [Action with owner and date]

**Tier 3 — Resolve within 90 days of deployment (medium):**
1. [Action with owner and date]

**Tier 4 — Continuous improvement (ongoing):**
1. [Action with programme owner]

---

## Quality Assurance

**Citation Quality Gates**: All 5 passed / [Gate X failed — corrected]
**Self-Interrogation**: Applied to [N] NON-COMPLIANT findings / [REVISED: detail]
**[VERIFY] items**: [List items requiring verification by qualified counsel]
**[CHECK CURRENCY] items**: [List items requiring currency verification]

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section]
```

---

## Localization Notes

To create a Member State-specific variant of this skill:

1. Research the designated national competent authority and market surveillance authority
   for the relevant sector in the target Member State
2. Research Member State-specific AI governance guidance and regulatory sandboxes
3. Research sector-specific regulator positions (e.g., national financial regulator on
   AI in credit scoring; national health authority on AI in diagnostics)
4. Replace `[JURISDICTION-SPECIFIC]` markers with verified Member State content
5. Cross-reference with national data protection authority guidance on AI and GDPR
6. Identify whether the Member State has any national AI legislation that supplements
   the EU AI Act (noting that the EU AI Act is directly applicable and cannot be
   derogated by Member States in most areas, but Member States retain discretion in
   law enforcement, SME support, and regulatory sandbox design)
7. Check national language requirements for instructions for use (Art. 13) and EU
   Declaration of Conformity (Art. 49)

---

## ISO/IEC 42001 Alignment Reference

ISO/IEC 42001:2023 (AI Management System) provides a voluntary framework that aligns
with AI Act obligations without replacing them:

| ISO 42001 Clause | AI Act Article | Alignment Notes |
|-----------------|---------------|----------------|
| 6.1 — Risk assessment and treatment | Art. 9 | ISO 42001 risk assessment directly informs Art. 9 risk management system |
| 6.2 — AI objectives | Art. 9, Art. 17 | AI objectives and KPIs feed into QMS regulatory compliance strategy |
| 8.4 — AI system impact assessment | Art. 9, GDPR Art. 35 | AI impact assessment overlaps with Art. 9 and GDPR DPIA |
| 9.1 — Monitoring, measurement, analysis | Art. 72 | Monitoring and measurement framework informs PMM plan |
| 10.1 — Non-conformity and corrective action | Art. 73 | Corrective action procedures integrate with incident reporting |

**ISO 42001 certification does not automatically demonstrate AI Act compliance** —
the regulatory requirements of Arts. 9-17 go beyond ISO 42001 in specific areas
(conformity assessment, CE marking, registration). However, certification strengthens
a provider's compliance posture and may be viewed favourably by market surveillance
authorities and notified bodies.

---

## Provider vs. Deployer Quick Reference

| Obligation | Provider (Art. 16) | Deployer (Art. 26) |
|-----------|-------------------|--------------------|
| Quality management system (Art. 17) | ✅ Mandatory | ➖ Not required |
| Technical documentation (Art. 11) | ✅ Mandatory | ➖ Not required (but must obtain from provider) |
| Record-keeping / logging design (Art. 12) | ✅ Must build into system | ➖ Must retain logs generated by system |
| Instructions for use (Art. 13) | ✅ Must provide | ➖ Must use in accordance with |
| Human oversight design (Art. 14) | ✅ Must build into system | ✅ Must designate competent oversight person |
| Conformity assessment (Art. 43) | ✅ Mandatory | ➖ Not required |
| CE marking + registration (Arts. 49, 71) | ✅ Mandatory | ✅ Must register if public-body deployer |
| Post-market monitoring (Art. 72) | ✅ Must establish PMM plan | ✅ Must report data to provider |
| Serious incident reporting (Art. 73) | ✅ Must report to authorities | ✅ Must report to provider AND competent authority |
| GDPR DPIA (GDPR Art. 35) | ✅ As controller/processor | ✅ As controller for own processing |

**Deployer becomes provider (Art. 25)** when they:
- (a) Put their name or trademark on the system
- (b) Make a substantial modification to the high-risk AI system
- (c) Change the intended purpose in a way that creates high-risk classification

---

## Administrative Fine Exposure

| Violation | Maximum fine | Notes |
|-----------|-------------|-------|
| Prohibited AI practices (Art. 5) | €35,000,000 or 7% of global annual turnover (whichever higher) | Absolute prohibition — no compliance defence |
| High-risk AI system requirements (Arts. 8-15, 17, 43-49, 71-73) | €15,000,000 or 3% of global annual turnover (whichever higher) | Core compliance failures |
| Incorrect/misleading information to notified bodies or authorities | €7,500,000 or 1% of global annual turnover (whichever higher) | Documentation and cooperation failures |
| SMEs and startups | NCAs must apply proportionality; percentage-based fines apply; fixed amounts apply where higher | Proportionality does not eliminate core requirements |

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis.

Primary legal sources: EU AI Act (Regulation (EU) 2024/1689), Official Journal L 2024/1689,
12 July 2024, entered into force 1 August 2024; Articles 1-99 and Annexes I-VII. GDPR
(Regulation (EU) 2016/679), Articles 35, 22, 5(1)(c). ISO/IEC 42001:2023 — Information
Technology — Artificial Intelligence — Management System. prEN 18286 — AI — Quality
Management System for EU AI Act Regulatory Purposes (public enquiry October 2025;
[VERIFY: OJ citation status]). EU AI Office guidance (digital-strategy.ec.europa.eu);
AI Act Service Desk (ai-act-service-desk.ec.europa.eu). DLA Piper, "Latest wave of
obligations under the EU AI Act take effect" (August 2025). Orrick, "The EU AI Act:
6 Steps to Take Before 2 August 2026" (November 2025). Future of Privacy Forum,
"Conformity Assessments under the EU AI Act" (April 2025). MIT Sloan Management Review,
"Organizations Face Challenges in Timely Compliance With the EU AI Act."

Research methodology: 2-agent research pipeline — Agent 1 (structural analysis of
legalcode-contract-review, legalcode-breach-severity-assessment, and
legalcode-legitimate-interest-assessment reference skills, extracting all quality
frameworks, output templates, and structural patterns) + Agent 2 (deep legal research
on EU AI Act Annex III, Arts. 9-17, 43, 72, 73, provider/deployer distinction, and
implementation timeline via web search). Primary legislation verified against OJ text.
All legal references should be verified against current authoritative sources before
reliance. Research conducted 2026-03-01.
