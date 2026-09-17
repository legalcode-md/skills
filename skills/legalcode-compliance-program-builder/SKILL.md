---
name: legalcode-compliance-program-builder
description: Build comprehensive corporate compliance programs aligned with DOJ Evaluation of Corporate
  Compliance Programs (ECCP) September 2024, UK Ministry of Justice Adequate Procedures under the Bribery
  Act 2010 (MoJ Six Principles), ISO 37301:2021 Compliance Management Systems, US Sentencing Guidelines
  §8B2.1 seven elements, and Transparency International Business Principles for Countering Bribery. Use
  when building a new compliance program from scratch, assessing and maturing an existing program, preparing
  for DOJ/SFO enforcement defense, pursuing ISO 37301 certification, or producing board-level compliance
  program assessment documentation.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Build comprehensive corporate compliance programs aligned with DOJ Evaluation of Corporate Compliance Programs (ECCP) September 2024, UK Ministry of Justice Adequate Procedures under the Bribery Act 2010 (MoJ Six Principles), ISO 37301:2021 Compliance Management Systems, US Sentencing Guidelines §8B2.1 seven elements, and Transparency International Business Principles for Countering Bribery. Use when building a new compliance program from scratch, assessing and maturing an existing program, preparing for DOJ/SFO enforcement defense, pursuing ISO 37301 certification, or producing board-level compliance program assessment documentation. Covers governance structure, risk assessment methodology, code of conduct development, policies and procedures library, training and communication programs, third-party due diligence, confidential reporting mechanisms, internal investigation protocols, monitoring and testing programs, incentive and disciplinary frameworks, and continuous improvement processes. Produces implementation roadmap with phased milestones, RACI matrix, resource requirements, and board-ready compliance program assessment. Jurisdiction-agnostic with US/UK/EU markers; cross-references ISO 37301, COSO ERM, NIST RMF. Three operating modes: Build New Program, Optimize Existing Program, Assessment Only.


# Legalcode Compliance Program Builder

> **Disclaimer**: This skill provides a framework for AI-assisted corporate compliance
> program design and assessment. It does not constitute legal advice and does not create
> an attorney-client relationship. All outputs should be reviewed by qualified legal
> counsel and compliance professionals licensed in the relevant jurisdictions before use.
> Laws, regulations, and enforcement priorities change; verify current applicability
> before relying on any provision described here. Statutory references, case citations,
> and regulatory guidance cited from memory carry hallucination risk — always verify
> against authoritative sources before relying on them in compliance decisions or
> enforcement matters. ISO standards require licence purchase for full text; consult
> the official ISO 37301:2021 publication for authoritative requirements.

---

## Purpose and Scope

This skill designs and assesses corporate compliance programs against the major global
frameworks: the DOJ's Evaluation of Corporate Compliance Programs (ECCP), the UK Bribery
Act Adequate Procedures defense, ISO 37301:2021, the US Sentencing Guidelines §8B2.1
seven-element framework, and Transparency International's Business Principles. It adapts
to three modes: building a new program from scratch, optimizing an existing program, or
conducting an assessment-only audit.

**Covers:**

- Governance structure design (reporting lines, board oversight, CCO authority)
- Enterprise compliance risk assessment (inherent risk → controls → residual risk)
- Code of conduct development and rollout strategy
- Policies and procedures library (15+ core documents)
- Training and communication program design (five curriculum tiers)
- Third-party due diligence program (three-tier risk-based framework)
- Confidential reporting mechanism design (hotline/helpline + investigation routing)
- Internal investigation protocol (triggers, privilege strategy, evidence, discipline)
- Monitoring and testing program (continuous monitoring + periodic controls testing)
- Incentive and disciplinary framework (compensation metrics, clawback, discipline matrix)
- Continuous improvement processes (program feedback loops, board reporting cadence)
- Implementation roadmap with phased milestones and resource requirements
- Cross-framework compliance mapping (DOJ ECCP ↔ USSG §8B2.1 ↔ UK Adequate Procedures ↔ ISO 37301 ↔ TI BPCB)
- Board-ready compliance program assessment documentation

**Does not:**

- Provide legal advice or substitute for qualified compliance counsel
- Guarantee immunity from enforcement action — no compliance program is a guarantee
- Cover sector-specific compliance programs in depth (HIPAA, GLBA, FINRA, FDA GxP —
  flag these overlays and refer to dedicated skills)
- Conduct actual investigations or review specific documents for wrongdoing
- Draft jurisdiction-specific statutes or regulations not described in this skill
- Perform financial fraud risk assessment (see legalcode-legal-risk-assessment)

**Related skills:**

- `legalcode-regulatory-change-tracker` — ongoing regulatory landscape monitoring
- `legalcode-ai-governance-framework-builder` — AI/technology governance overlay
- `legalcode-incident-response-plan-builder` — incident response integration
- `legalcode-dpia-generator` — GDPR data protection compliance overlay
- `legalcode-independent-contractor-classification` — labor compliance overlay

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The primary regulatory driver (DOJ ECCP, UK
Bribery Act, ISO 37301, or all three) is determined in Step 2. The skill produces content
that satisfies all major frameworks simultaneously where they align, with jurisdiction-
specific overlays marked throughout.

[JURISDICTION-SPECIFIC: United States] When the organization is subject to DOJ
jurisdiction: apply the full ECCP September 2024 three-question framework (well-designed?
adequately resourced and empowered? works in practice?). Verify US Sentencing Guidelines
§8B2.1 seven elements. For regulated industries, layer FINRA, OCC, HIPAA, or SEC
compliance program overlays as applicable. Clawback pilot program (2023): all Criminal
Division resolutions now require compliance-related compensation criteria.

[JURISDICTION-SPECIFIC: United Kingdom] When the organization is subject to the Bribery
Act 2010: design the program to satisfy Section 7's "adequate procedures" defence using
MoJ's Six Principles. Note that the UK standard prohibits facilitating payments (unlike
the US FCPA's now-abolished facilitation payment exception). _R v Skansen Interiors
Limited_ (2018) [VERIFY for subsequent developments] confirmed that generic policies
without specific anti-bribery content, active training, and designated responsibility do
not constitute "adequate procedures." The bar is high; SFO has described it as such.

[JURISDICTION-SPECIFIC: European Union] For EU-based organizations or those processing
EU personal data: layer in GDPR compliance (Art. 5(2) accountability principle), CSRD
sustainability due diligence reporting obligations (Directive 2022/2464), the EU Whistleblower
Protection Directive (Directive 2019/1937 — mandatory internal and external reporting
channels for companies with 50+ employees), and CSDDD supply chain due diligence
(Directive 2024/1760, scope: 5,000+ employees globally). The EU AMLR (effective
July 10, 2027) imposes new CDD and beneficial ownership requirements. [VERIFY all
enforcement dates before relying on them.]

[JURISDICTION-SPECIFIC: Global / Multinational] For organizations operating across
multiple jurisdictions: conduct a jurisdiction matrix mapping every country of operation
to its applicable anti-corruption law, data privacy law, AML/CTF law, and sector
regulatory overlay. Identify the highest-standard requirement in each domain and design
the program to meet that standard globally, with local supplementation as needed.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the organization's context, the workflow pauses and asks when:

- The answer changes which regulatory framework(s) apply
- Multiple valid program design approaches exist (centralized vs. federated governance)
- The operating mode (build/optimize/assess) determines the scope of deliverables
- Risk tolerance or budget constraints affect which program elements to prioritize

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

### Step 1: Determine Operating Mode

**⟁ CLARIFY** — Which of these best describes your goal?

1. **Build New Program** — Design a compliance program from scratch; no formal program exists
   - _Output_: Full program documentation suite (Phases 1-4 deliverables)
   - _Timeline_: 12-18 months to full implementation
   - _Default batch_: Use this mode

2. **Optimize Existing Program** — Assess and improve a program that already exists
   - _Output_: Gap analysis + remediation roadmap + priority improvements
   - _Timeline_: 4-8 weeks assessment; 3-6 months remediation

3. **Assessment Only** — Produce a compliance program maturity assessment without building
   - _Output_: Maturity scorecard + domain-by-domain ratings + board summary
   - _Timeline_: 2-3 weeks assessment

4. **Board Presentation** — Produce board-ready compliance program status documentation
   - _Output_: Executive summary, heat map, investment case, peer benchmarking
   - _Timeline_: 1 week

---

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Before analysis, gather the following context. Present as structured
options where possible.

**2a. Organization Profile:**

- Industry sector: (Financial services / Healthcare / Technology / Manufacturing /
  Government contractor / Professional services / Consumer / Other)
- Approximate size: (Under 250 employees / 250-2,500 / 2,500-25,000 / 25,000+)
- Geographic footprint: (Domestic only / Predominantly one country / Multi-regional /
  Global with operations in 10+ countries)
- Ownership/listed status: (Privately held / PE-backed / Publicly listed / Government)

**2b. Primary Regulatory Driver:**

- What is the primary compliance risk driving this program?
  - Anti-corruption/anti-bribery (FCPA, UK Bribery Act, local equivalents)
  - Data privacy and cybersecurity (GDPR, CCPA, HIPAA, NIS2)
  - Financial crime/AML-CTF (BSA, MLCA, EU AMLR)
  - Sector-specific (FDA/GxP, FINRA/SEC, healthcare, defense)
  - ESG/supply chain due diligence (CSDDD, CSRD, modern slavery)
  - General corporate compliance (all of the above)
  - [JURISDICTION-SPECIFIC: identify the highest-priority regulatory exposure first]

**2c. Governance Maturity (Existing State):**

- Current compliance function: (None / Part-time / Dedicated CCO / Team / Embedded)
- Board/audit committee engagement: (None / Ad hoc / Periodic reports / Active oversight)
- Existing program documentation: (None / Ad hoc policies / Partial program / Formal)

**2d. Primary Framework Alignment:**

- Which framework(s) must the program satisfy?
  - DOJ ECCP 2024 (US enforcement defense priority)
  - UK Bribery Act MoJ Six Principles (SFO defense priority)
  - ISO 37301:2021 (certification objective)
  - All three (multinational / highest-standard design)
  - US Sentencing Guidelines §8B2.1 (culpability score reduction)
  - Default (align to all applicable, jurisdiction markers throughout)

**2e. Risk Tolerance and Priority:**

- Conservative (maximize defensibility; comprehensive documentation; external review)
- Balanced (meet minimum regulatory expectations; prioritize high-risk areas)
- Progressive (pragmatic; focus on cultural change; lighter documentation)

**State any assumptions explicitly if context is incomplete** (e.g., "Assuming
anti-corruption is the primary driver and the organization has no formal compliance
infrastructure — correct these if inaccurate and I will adjust the analysis").

---

### Step 3: Regulatory Landscape Assessment

Before designing the program, assess which regulatory regimes apply. Work through
this checklist:

**Anti-Corruption / Anti-Bribery:**

- [ ] Is the organization a US issuer, US domestic concern, or foreign company listing on
      a US exchange? → FCPA (15 U.S.C. §§78dd-1, 78dd-2, 78dd-3) applies
- [ ] Does the organization conduct business in or through the UK, or are any of its
      associated persons in the UK? → Bribery Act 2010 §7 applies
- [ ] Does the organization operate in jurisdictions with local anti-bribery laws? →
      [JURISDICTION-SPECIFIC: Brazil FCPA equivalent (Law 12.846/2013); France Sapin II
      (Law 2016-1691); German Act to Combat Corruption; Italy D.Lgs. 231/2001; Canada
      CFPOA; Australia Criminal Code Act 1995 Part 12.7]

**Financial Crime / AML-CTF:**

- [ ] Is the organization a "financial institution" under the BSA (31 U.S.C. §5312)? →
      Full AML program requirements apply
- [ ] Does the organization have EU nexus? → EU AMLR effective July 10, 2027 [VERIFY]
- [ ] Does the organization have beneficial ownership reporting obligations? →
      US CTA (31 U.S.C. §5336); EU AMLD5/6; FATF recommendations

**Data Privacy / Cybersecurity:**

- [ ] Does the organization process personal data of EU residents? → GDPR, NIS2 apply
- [ ] Does the organization operate in California? → CCPA/CPRA apply
- [ ] Sector overlay: healthcare (HIPAA), financial services (GLBA/GLB), telecom (CPNI)?

**Employment / Labor:**

- [ ] Does the organization have EU employees (50+)? →
      EU Whistleblower Protection Directive 2019/1937: mandatory internal channel
- [ ] Does the organization have UK employees? →
      Public Interest Disclosure Act 1998; Employment Rights Act 2025 [VERIFY]

**Supply Chain / ESG:**

- [ ] Does the organization exceed 5,000 employees globally or €1.5B EU net turnover? →
      CSDDD (Directive 2024/1760) applies from July 2029 [VERIFY final timeline]
- [ ] Is the organization listed on a regulated market or large company per CSRD scope? →
      CSRD sustainability reporting with anti-corruption disclosures

**US Sentencing Guidelines:**

- [ ] Is the organization at risk of federal criminal prosecution? →
      USSG §8B2.1 seven elements; effective program yields -3 culpability score points

Produce a regulatory applicability summary table. For each applicable regime, note the
primary obligation, most recent key development, and whether the organization has any
known exposure.

---

### Step 4: Program Gap Analysis

Assess the current state of the organization's compliance program across the nine core
domains. For Build New Program mode, all domains default to Level 1 (Ad Hoc). For
Optimize mode, assess current state per domain.

Use the **Compliance Program Maturity Model** (see Section: Program Maturity Model) to
rate each domain. Classify each domain:

| Rating         | Description                                                               |
| -------------- | ------------------------------------------------------------------------- |
| **EFFECTIVE**  | Level 4-5: Proactive, data-driven, embedded in operations and culture     |
| **ADEQUATE**   | Level 3: Documented, standardized, functional, meets minimum expectations |
| **DEVELOPING** | Level 2: Informal, inconsistent, partial, or paper-based only             |
| **INADEQUATE** | Level 1: Absent, reactive only, or fails minimum regulatory expectations  |

**Nine Core Domains:**

| #   | Domain                              | Current Rating | Priority |
| --- | ----------------------------------- | -------------- | -------- |
| 1   | Governance & Board Oversight        |                |          |
| 2   | Risk Assessment                     |                |          |
| 3   | Code of Conduct & Policies          |                |          |
| 4   | Training & Communication            |                |          |
| 5   | Third-Party Due Diligence           |                |          |
| 6   | Confidential Reporting Mechanisms   |                |          |
| 7   | Internal Investigation Protocol     |                |          |
| 8   | Monitoring & Testing                |                |          |
| 9   | Incentives & Disciplinary Framework |                |          |

**Priority rules:**

- Any domain rated INADEQUATE where regulatory exposure is HIGH → CRITICAL (address in Phase 1)
- Any domain rated DEVELOPING with HIGH regulatory exposure → HIGH (Phase 1-2)
- Any domain rated DEVELOPING with MEDIUM regulatory exposure → MEDIUM (Phase 2-3)
- ADEQUATE domains → LOW (Phase 3-4 optimization)
- EFFECTIVE domains → MONITOR (Phase 4 continuous improvement)

---

### Step 5: Governance Structure Design

Design the compliance governance architecture. Present three models for selection:

**⟁ CLARIFY** — Which governance model fits the organization?

**Model A: Centralized** (single CCO function manages all compliance)

- Best for: Organizations under 5,000 employees; single-product; single-jurisdiction
- Structure: CCO → Compliance Officers (functional) → All employees
- Board reporting: CCO reports directly to Audit/Risk Committee
- Advantage: Consistency, accountability, clear ownership
- Risk: Single point of failure; can become siloed from business

**Model B: Federated** (business unit compliance liaisons with central standards)

- Best for: Multi-divisional organizations; regulated industries with separate compliance needs
- Structure: Chief Compliance Officer → BU Compliance Officers → Employees
- Central function: Sets standards, monitors, reports; BUs execute
- Board reporting: CCO consolidates BU reports to board
- Advantage: Contextually relevant compliance advice; scales better
- Risk: Inconsistency across BUs; matrix reporting conflicts

**Model C: Hybrid** (central CCO + embedded compliance champions)

- Best for: 2,500+ employees; moderate complexity; cost-conscious
- Structure: CCO + small central team → Compliance Champions (part-time, embedded in BUs)
- Champions: First point of contact; trained to escalate; not investigators
- Board reporting: CCO via Audit Committee; BU champions in monthly operating reviews
- Advantage: Broad reach; relatively cost-efficient
- Risk: Champions lack authority; need careful training and formal role definition

**For each governance model, produce:**

1. **Governance Charter** — Purpose, authority, scope, reporting line, independence protections,
   resource allocation mandate, board access guarantee

2. **Roles and Responsibilities (RACI)** — For the following activities:

| Activity           | CCO | GC  | Board/AC | CISO | HR  | BU Head | Int. Audit | CFO | Ext. Counsel |
| ------------------ | --- | --- | -------- | ---- | --- | ------- | ---------- | --- | ------------ |
| Policy development | A   | C   | I        | C    | C   | C       | I          | I   | C            |
| Risk assessment    | A   | C   | I        | C    | C   | R       | C          | I   | C            |
| Training delivery  | R   | C   | I        | C    | A   | C       | I          | I   | —            |
| Third-party DD     | A   | C   | I        | C    | I   | R       | C          | C   | C            |
| Hotline management | A   | C   | I        | —    | C   | I       | C          | I   | C            |
| Investigations     | A   | C   | C        | R    | C   | I       | I          | I   | C            |
| Discipline         | C   | C   | I        | —    | A   | R       | I          | I   | C            |
| Board reporting    | A   | C   | R        | C    | I   | I       | C          | I   | C            |
| Monitoring/audit   | C   | I   | I        | C    | I   | I       | A          | I   | I            |
| M&A integration    | A   | C   | I        | C    | C   | R       | C          | C   | C            |

(A = Accountable; R = Responsible; C = Consulted; I = Informed)

3. **Board Mandate Template** — Resolution language authorizing compliance function,
   specifying CCO appointment/removal procedures, Audit Committee charter amendment,
   and compliance budget floor.

---

### Step 6: Program Components Development

Develop each of the nine program domains in depth. Apply the **Self-Interrogation** (see
Quality Frameworks) for any domain rated INADEQUATE at Step 4.

#### Domain 1: Risk Assessment

**Objective:** Identify, assess, and prioritize compliance risks on an ongoing basis.

**Methodology (Inherent Risk → Controls → Residual Risk):**

_Step 1 — Regulatory Universe Construction_
Catalogue all applicable regulations, laws, industry standards, and contractual obligations
(from Step 3 output). For each obligation, identify: business activities affected, geographic
application, enforcement body, maximum penalty, and historical enforcement trend.

_Step 2 — Risk Category Mapping_
Organize risks into the standard compliance risk taxonomy:

- Anti-corruption/anti-bribery
- Financial crime (AML, sanctions, fraud)
- Data privacy and cybersecurity
- Employment and labor practices
- Competition/antitrust
- Environmental, health, safety
- Export controls and trade compliance
- Financial reporting and disclosure
- Consumer protection / product liability
- Sector-specific overlay [JURISDICTION-SPECIFIC]

_Step 3 — Inherent Risk Assessment (per category and business unit)_

Rate each risk combination (category × business unit/process) on:

| Dimension      | High (3)                                                                                                  | Medium (2)                                                              | Low (1)                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Likelihood** | High probability of non-compliance without controls; sector/geography places org in elevated-risk context | Moderate probability; org has some exposure but not a high-risk outlier | Low probability; limited exposure; not a priority regulatory target   |
| **Impact**     | Material financial penalty (>1% revenue), criminal exposure, or significant reputational harm             | Regulatory sanction, civil penalty, moderate reputational impact        | Minor penalty, administrative correction, limited reputational impact |

Inherent Risk Score = Likelihood × Impact (scale 1-9)

_Step 4 — Control Effectiveness Assessment_

For each high/medium-inherent-risk area, assess existing controls:

| Level            | Design                                            | Operation                                                       |
| ---------------- | ------------------------------------------------- | --------------------------------------------------------------- |
| **Strong (1)**   | Controls fully address the regulatory requirement | Controls operating as designed; evidence of effective operation |
| **Adequate (2)** | Controls partially address the requirement        | Controls generally operating; minor exceptions                  |
| **Weak (3)**     | Controls absent, incomplete, or misdesigned       | Controls not operating; or not tested                           |

Residual Risk Score = Inherent Risk Score × Control Effectiveness Level

_Step 5 — Risk Register_
Produce a risk register in heat map format. Residual risks scoring 6-9 = HIGH (Priority 1);
3-6 = MEDIUM (Priority 2); 1-3 = LOW (Priority 3).

**Governance:** Risk assessment owned by CCO; validated by Internal Audit; approved by
Audit Committee. Cadence: full assessment annually; event-triggered updates on material
business change, significant enforcement action, or internal incident.

[JURISDICTION-SPECIFIC: ISO 37301 Clause 4.6 requires risk assessment as a "shall"
(mandatory) element. DOJ ECCP asks: "Does the company periodically assess the risk of
criminal conduct and take appropriate steps to design, implement, or modify each element
to reduce identified risks?"]

---

#### Domain 2: Code of Conduct

**Objective:** Establish and communicate the organization's ethical standards and legal
obligations in a clear, accessible document.

**Required Provisions (minimum 11 sections):**

1. **Message from Leadership** — CEO and board chair statement of commitment; zero-tolerance
   tone; link between compliance and organizational values

2. **Who and What It Covers** — All employees, officers, directors, contractors, agents;
   global application; subsidiary coverage; language versions required

3. **Anti-Corruption and Anti-Bribery** — Prohibition on bribing anyone (public official
   or private party); prohibition on receiving bribes; gifts and hospitality policy
   (monetary thresholds, approval requirements, recording obligations);
   [JURISDICTION-SPECIFIC: UK — facilitation payments prohibited outright; US — FCPA
   narrow facilitation payment exception eliminated in DOJ 2023 guidance; document any
   residual exception with legal counsel review]

4. **Conflicts of Interest** — Definition; disclosure and recusal procedure; outside
   business activities; personal investments; family member employment; Board approval
   requirements for senior officers

5. **Competition/Antitrust** — No price-fixing, market allocation, bid-rigging; competitor
   interactions; information exchange restrictions; pre-clearance for association
   memberships [JURISDICTION-SPECIFIC: EU Art. 101-102 TFEU; US Sherman Act §1-2;
   UK Competition Act 1998]

6. **Data Privacy and Confidentiality** — Handling of personal data; confidential
   information obligations; data breach reporting path; clean desk standards;
   AI/technology use restrictions (cross-reference AI AUP if applicable)

7. **Records Integrity and Financial Reporting** — Accurate books and records obligation;
   prohibition on false entries; document retention periods; no off-the-books accounts
   [JURISDICTION-SPECIFIC: FCPA books and records provisions; UK Bribery Act Principle 6
   monitoring includes records review]

8. **Use of Company Assets and Systems** — Appropriate use; prohibition on personal misuse;
   monitoring disclosure; AI and technology use policy cross-reference

9. **Anti-Harassment and Workplace Respect** — Protected characteristics; zero tolerance;
   reporting paths; non-retaliation; manager obligations

10. **Environment, Health, and Safety** — Basic safety obligations; environmental
    commitments; incident reporting path; [JURISDICTION-SPECIFIC: OSHA 29 C.F.R. §1904
    US; UK Health and Safety at Work Act 1974; EU Directive 89/391/EEC]

11. **How to Report and Seek Guidance** — Confidential reporting channel details; manager
    escalation path; open-door policy; external regulator reporting rights; non-retaliation
    commitment with enforcement examples; whistleblower protections
    [JURISDICTION-SPECIFIC: EU Whistleblower Directive 2019/1937 — mandatory internal
    channel for organizations with 50+ employees; UK PIDA 1998]

12. **Consequences of Violations** — Range of disciplinary measures (written warning through
    termination); referral to law enforcement; personal liability exposure; no position
    protects from consequences

**Localization Guidance:** Produce a base global version plus supplements for high-risk
jurisdictions (at minimum: US, UK, EU, and any country with 500+ employees or significant
government-facing operations). Supplements address: local mandatory reporting obligations,
jurisdiction-specific gift/hospitality limits, local disciplinary procedure requirements.

**Communication and Rollout:** (1) CEO launch communication; (2) Company-wide training
module; (3) Annual acknowledgment with comprehension check; (4) New-hire onboarding module;
(5) Manager training on administering the Code.

---

#### Domain 3: Policies and Procedures Library

**Objective:** Comprehensive written policies governing the organization's highest-risk
compliance areas.

**Core Policy Suite (minimum 15 documents):**

| #   | Policy                                            | Primary Framework                                          | Review Frequency |
| --- | ------------------------------------------------- | ---------------------------------------------------------- | ---------------- |
| 1   | Anti-Corruption and Anti-Bribery Policy           | FCPA, UK Bribery Act, local laws                           | Annual           |
| 2   | Gifts, Hospitality and Entertainment Policy       | FCPA, Bribery Act Principle 1                              | Annual           |
| 3   | Conflicts of Interest Policy                      | USSG Element 1; ECCP Q1                                    | Annual           |
| 4   | Third-Party Due Diligence Policy                  | ECCP Q1; Bribery Act Principle 4; ISO 37301 Cl.8.3         | Annual           |
| 5   | Confidential Reporting and Non-Retaliation Policy | ECCP Q2; EU Directive 2019/1937; USSG Element 5            | Annual           |
| 6   | Internal Investigation Policy                     | ECCP Q3; USSG Element 7                                    | Annual           |
| 7   | Disciplinary and Consequence Management Policy    | USSG Element 6; ECCP Q2                                    | Annual           |
| 8   | Records Retention and Destruction Policy          | FCPA books/records; SOX (if listed); UK Companies Act 2006 | Biennial         |
| 9   | Data Privacy Policy                               | GDPR Art. 5; CCPA; HIPAA (if applicable)                   | Annual           |
| 10  | Information Security / Acceptable Use Policy      | ISO 27001; NIST CSF; NIS2                                  | Annual           |
| 11  | Competition/Antitrust Policy                      | Sherman Act; EU Art. 101; UK CMA                           | Annual           |
| 12  | Export Controls and Trade Compliance Policy       | US EAR/ITAR; EU Dual-Use Reg.                              | Annual           |
| 13  | Sanctions and Financial Crime Policy              | OFAC; UK OFSI; EU sanctions                                | Annual           |
| 14  | Speaking with the Media and Social Media Policy   | Reg FD (if public co.); reputation management              | Annual           |
| 15  | Political Contributions and Lobbying Policy       | FECA; FCPA; TI BPCB                                        | Annual           |
| 16  | Whistleblower Protection Policy                   | Dodd-Frank §922; NLRA; EU Directive                        | Annual           |
| 17  | AI and Emerging Technology Use Policy             | EU AI Act; NIST AI RMF; ABA Opinion 512                    | 6-monthly        |

Each policy must include: (1) statement of purpose, (2) scope (who/what/where covered),
(3) definitions of key terms, (4) substantive requirements, (5) prohibited conduct with
examples, (6) approval/exception procedures, (7) reporting path for violations, (8)
consequences of violations, (9) document owner, approval date, and next review date.

**Policy Governance:** All policies must be: (a) approved by the CCO and General Counsel;
(b) ratified by the Board/Audit Committee for policies relating to senior officer conduct;
(c) accessible to all covered persons in their working language; (d) version-controlled
with change history maintained.

---

#### Domain 4: Training and Communication

**Objective:** Ensure all relevant persons understand their compliance obligations and
can act on them in practical situations.

**Five Curriculum Tiers:**

| Tier                  | Audience                                                                     | Frequency                   | Format                                    | Minimum Duration | Assessment                              |
| --------------------- | ---------------------------------------------------------------------------- | --------------------------- | ----------------------------------------- | ---------------- | --------------------------------------- |
| 1: Board/Executive    | Directors, C-suite                                                           | Annual + on material change | Facilitated session or interactive module | 2 hours          | Discussion/attestation                  |
| 2: Manager            | All people managers                                                          | Annual + new manager        | Interactive module + role-play scenarios  | 3 hours          | Comprehension test (80% pass threshold) |
| 3: Employee (General) | All employees                                                                | Annual                      | Interactive module                        | 1 hour           | Comprehension test                      |
| 4: High-Risk Role     | Finance, sales, procurement, legal, government affairs, third-party managers | Annual + role change        | Role-specific interactive module          | 2 hours          | Scored assessment + certification       |
| 5: Third Party        | Agents, distributors, JV partners, contractors with government touchpoints   | Onboarding + annual         | Online module or in-person                | 1 hour           | Attestation + comprehension check       |

**DOJ ECCP Training Evaluation Factors:**

- Does training address the specific risk profile of the organization? (Not generic)
- Is training calibrated to employees' roles and responsibilities?
- Is effectiveness measured? (comprehension testing, not just completion tracking)
- Are employees in high-risk roles receiving enhanced training?
- Is leadership visibly engaging with training? (Tone at the top)
- Are lessons from prior incidents incorporated?

[JURISDICTION-SPECIFIC: US — DOJ ECCP 2024 specifically asks whether training addresses
AI/emerging technology risks. UK — Bribery Act Principle 5 requires training "appropriate
to such individuals' respective roles." EU — Whistleblower Directive Art. 7 requires
training for persons who receive reports. ISO 37301 — Clause 7.2 requires competence
assessment; training records must be maintained.]

**Training Effectiveness Metrics:**

- Completion rate by tier and business unit (target: 95% within 30 days of assignment)
- Comprehension score distribution (flag BUs/roles with <80% average pass rate)
- Knowledge retention (follow-up quiz 90 days after initial training; target >70% retention)
- Reporting rate correlation (increased training should correlate with increased reporting volume)
- Culture survey results (speaking-up, comfort reporting, trust in process)

---

#### Domain 5: Third-Party Due Diligence

**Objective:** Manage compliance risk introduced by agents, intermediaries, distributors,
suppliers, and other business partners acting on behalf of the organization.

**Three-Tier Risk Framework:**

**Tier 1 — Enhanced Due Diligence (Highest Risk)**

_Trigger factors_ (any single factor → Tier 1):

- Government-facing role (licenses, permits, customs facilitation, government contracts)
- Operations in high-risk jurisdiction (TI CPI score < 50; FATF grey/black list)
- Payment structure: success fees, non-standard timing, requests for cash payments
- Government official involvement in referral or recommendation
- Opaque or complex ownership structure (offshore, shell companies)
- Prior adverse media, enforcement action, or sanctions history

_Required checks:_

- Enhanced background investigation (adverse media 10-year lookback; Google, Dow Jones,
  MSCI, or equivalent screening tool)
- Ultimate beneficial ownership verification to ≥10% threshold
- Politically Exposed Person (PEP) screening — all principals and owners
- Sanctions screening (OFAC, EU, UK OFSI, UN)
- Registration and licensing verification
- Reference checks (2+ independent; not organization-nominated only)
- Site visit or virtual audit for highest-risk relationships
- Legal entity and organizational chart verification
- Anti-bribery contractual provisions + audit rights + termination for cause
- Annual recertification; event-triggered re-screening

**Tier 2 — Standard Due Diligence**

_Trigger factors:_ Standard commercial vendors, suppliers, professional service providers
in moderate-risk jurisdictions without government touchpoints.

_Required checks:_

- Sanctions screening (OFAC, EU, UK OFSI, UN)
- Basic adverse media (abbreviated, 5-year lookback)
- Ownership verification (public records)
- Anti-bribery contractual representations
- Biennial recertification

**Tier 3 — Basic Screening**

_Trigger factors:_ Low-value domestic vendors, commodity suppliers, no government
touchpoints, low-risk jurisdiction, no compliance-sensitive services.

_Required checks:_

- Sanctions screening at onboarding
- Self-certification questionnaire
- Re-screening only on change of circumstances (new ownership, adverse news)

**Full Lifecycle Requirements (DOJ ECCP 2024):**

1. _Pre-engagement:_ Document business rationale; initial tier determination; approval
   for Tier 1 by CCO before engagement
2. _Procurement:_ RFP includes mandatory compliance representations
3. _Risk assessment:_ Formal tier determination documented; DD scope defined
4. _Due diligence:_ Conduct and document all required checks; CCO sign-off for Tier 1
5. _Contracting:_ Compliance representations; audit rights (Tier 1 mandatory); termination for cause
6. _Onboarding:_ Training delivery; policy receipt acknowledgment; introduction to reporting channel
7. _Ongoing monitoring:_ Transaction monitoring for anomalies; event-triggered reviews;
   annual certification (Tier 1); AI/data analytics tools for pattern detection
8. _Termination:_ Compliance review; document retention per policy

**Red Flag Escalation:** Define escalation path when a red flag is identified post-onboarding.
CCO must be notified within 24 hours of any sanctions hit or credible corruption allegation.

---

#### Domain 6: Confidential Reporting Mechanisms

**Objective:** Provide multiple, accessible, confidential channels for employees and
third parties to report potential violations without fear of retaliation.

**Channel Design:**

| Channel           | Availability                  | Anonymity                    | Provider                |
| ----------------- | ----------------------------- | ---------------------------- | ----------------------- |
| Telephone hotline | 24/7, toll-free, multilingual | Optional anonymous           | Third-party recommended |
| Web form          | Always-on, device-agnostic    | Optional anonymous           | Third-party recommended |
| Email alias       | Business hours monitoring     | Confidential (not anonymous) | Internal or third-party |
| Mobile app        | Always-on                     | Optional anonymous           | Third-party             |
| Ombudsperson      | Business hours                | Fully confidential           | Internal (senior role)  |

**Design Principles:**

- Third-party administration is best practice for independence and anonymity integrity
- Anonymity must be technically genuine (no IP logging, no metadata capture)
- Multi-language capability matching workforce composition
- Reports involving senior management (VP+) must automatically route to Board/Audit Committee
  chair (bypass management chain)

[JURISDICTION-SPECIFIC: EU — Whistleblower Directive 2019/1937 requires organizations
with 50+ employees to establish internal reporting channels; reports must be acknowledged
within 7 days; feedback on action taken within 3 months. UK — PIDA 1998 "qualifying
disclosures" include criminal offences, legal obligation breaches, miscarriages of justice,
health/safety dangers, environmental damage, cover-up of the above. US — Dodd-Frank
§922 (SEC) and §806 (SOX) whistleblower protections; DOJ 2024 ECCP evaluates speak-up
culture effectiveness. ISO 37301 — Clause 8.5 requires "reporting channels" as a
mandatory "shall" element.]

**Investigation Routing Decision Tree:**

```
Report received
    │
    ├─► Subject is senior management (VP+)? → Escalate to Board/Audit Committee directly
    │
    ├─► Subject is CCO? → Escalate to GC + Board Chair; CCO recused
    │
    ├─► Involves potential criminal conduct? → Engage outside counsel; assess privilege
    │   strategy; consider voluntary disclosure obligations
    │
    ├─► Involves data breach/cybersecurity incident? → Activate incident response plan;
    │   parallel compliance investigation
    │
    └─► Standard investigation → CCO-directed; assign investigator;
        open case file; acknowledge reporter within 5 business days
```

**Governance and Metrics:**
Report the following metrics to the Audit Committee quarterly:

- Total reports received (by channel, by category)
- Reports by substantiation outcome (substantiated / unsubstantiated / inconclusive)
- Average case closure time (target: 60 days for complex; 30 days for simple)
- Retaliation complaints received and outcomes
- Anonymous vs. identified report ratio (target: >40% identified indicates strong speak-up culture)
- Repeat allegation patterns by business unit or process

**Non-Retaliation Framework:** Define prohibited retaliatory conduct explicitly; enforce
discipline (including termination) for any confirmed retaliation; designate alternate
reporting path for retaliation complaints (independent of the CCO if CCO manages original investigation).

---

#### Domain 7: Internal Investigation Protocol

**Objective:** Investigate allegations of compliance violations fairly, thoroughly, and
consistently, with appropriate privilege protections and documented findings.

**Investigation Trigger Criteria:**

| Trigger                                                            | Response Level                                                    |
| ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Report via confidential channel                                    | Standard investigation triage                                     |
| Manager escalation of potential violation                          | Standard investigation triage                                     |
| Whistleblower complaint to regulator (DOJ/SFO/SEC notice received) | Immediate CCO + GC + outside counsel activation                   |
| Government subpoena or search warrant                              | Immediate outside counsel; legal hold activation                  |
| Indication of senior management involvement                        | Board/Audit Committee immediate notification                      |
| Financial fraud indicators                                         | CFO + external auditor notification; potential restatement review |
| Data breach with personal data exposure                            | Activate incident response plan (parallel track)                  |

**Investigation Phases:**

_Phase 1 — Intake and Triage (1-2 business days)_

- Document the allegation (preserve original report)
- Assess preliminary credibility (specific, plausible, not demonstrably false)
- Determine investigation level: internal (CCO-directed) vs. external (outside counsel)
- Privilege strategy decision: if significant legal exposure → outside counsel direction
  from the outset; all work product under Upjohn/common law privilege
- Conflict-of-interest check: Is any potential investigator a subject or witness?
- Legal hold: If documents may be relevant to a legal matter, issue immediately

_Phase 2 — Investigation Planning (within 5 business days)_

- Define scope (allegations, time period, business unit, persons of interest)
- Assign investigator (CCO or designate; independent of subject's reporting line)
- Identify document sources; request preservation of relevant records
- Prepare investigation plan (scope, timeline, personnel, estimated cost)
- If senior management or director involved: notify Board/Audit Committee promptly

_Phase 3 — Evidence Gathering_

- Document review: preserve and analyze emails, financial records, contracts,
  communications; chain of custody documentation required
- Witness interviews (see Interview Protocol below)
- Third-party records (if available)
- Data analytics where applicable (transaction patterns, access logs)

_Interview Protocol:_

1. Opening Upjohn warning (if outside counsel): explain who the lawyer represents,
   privilege ownership, right to personal counsel [JURISDICTION-SPECIFIC: UK equivalent
   — "We represent the company, not you personally; you may retain your own solicitor"]
2. Factual questions: open-ended first; specific follow-up
3. Do not reveal other witnesses' testimony
4. Conclude: ask if anything important has not been covered
5. Memoranda of interview within 24 hours; distribute on need-to-know basis only

_Phase 4 — Analysis and Findings_

- Apply legal standards to facts (did conduct breach the policy or law?)
- Credibility assessment
- Confidence scoring: HIGH (>80%), PROBABLE (60-79%), INCONCLUSIVE (<60%)
- Identify remediation recommendations

_Phase 5 — Reporting and Disposition_

- Investigation report: (a) allegation summary, (b) methodology, (c) findings of fact,
  (d) legal/policy analysis, (e) conclusion, (f) remediation recommendations
- Distribution: CCO, GC, appropriate executive; Board/AC if senior subject
- Disposition: substantiated → disciplinary process; unsubstantiated → close file + communicate outcome;
  inconclusive → consider additional steps; potential crime → discuss voluntary disclosure with outside counsel

_Phase 6 — Corrective Action and Lessons Learned_

- Disciplinary action (see Domain 9)
- Remediation of identified control failure
- Root cause analysis: why did the violation occur? What control was missing or weak?
- Policy/procedure update if systemic gap identified
- Share lessons learned in aggregate (anonymized) with compliance training program
- Trend analysis: are repeat patterns emerging by BU, function, or leadership?

[DOJ ECCP 2024: "Does the company analyze and address the root causes of any violations
or compliance failures? Does it incorporate lessons learned from its own compliance
incidents and those affecting peer companies in its industry?"]

---

#### Domain 8: Monitoring and Testing

**Objective:** Continuously monitor for compliance failures and periodically test the
effectiveness of key controls.

**Three Monitoring Types:**

**Type A — Continuous/Automated Monitoring (Ongoing):**

- Transaction screening: payments to third parties; expense reports; petty cash
- Access control monitoring: segregation of duties violations; privileged access
- Data analytics: anomaly detection in procurement, payments, and vendor data
- Policy attestation tracking: completion rates, overdue attestations
- Sanctions and PEP screening: real-time against updated lists
- AI-assisted monitoring for high-risk patterns [DOJ ECCP 2024 requirement]

**Type B — Periodic Controls Testing (Structured):**

| Risk Level      | Testing Frequency    | Method                                                |
| --------------- | -------------------- | ----------------------------------------------------- |
| HIGH controls   | Monthly or quarterly | Transactional sampling; controls walk-through         |
| MEDIUM controls | Semi-annual          | Statistical sampling; self-assessment with CCO review |
| LOW controls    | Annual               | Management self-assessment                            |

Controls testing distinguishes:

- _Design effectiveness_: Does the control's design address the regulatory requirement?
- _Operating effectiveness_: Is the control actually operating as designed? (Testing requires evidence)

**Type C — Independent Audit:**

- Internal Audit conducts planned compliance audits per annual audit plan
- Internal Audit reports functionally to Audit Committee (independence requirement)
- External auditors provide additional assurance for financial compliance
- Regulatory examinations for regulated industries
- Periodic third-party program effectiveness assessment (every 2-3 years for large programs)

**Board Reporting Standards:**

Quarterly: Key metrics dashboard to Audit Committee

- Risk assessment changes (new/elevated risks)
- Significant control failures and remediation status
- Investigation summary (number, categories, closure rate — no names)
- Training completion rates by tier
- Hotline volume trends
- Regulatory developments with business impact

Annual: Comprehensive compliance program report to Board

- Program effectiveness assessment against DOJ ECCP three questions
- Gap analysis vs. prior year targets
- Year-ahead priorities and investment requirements
- External benchmarking (if available)
- CCO attestation of program adequacy

[JURISDICTION-SPECIFIC: ISO 37301 — Clause 9.1 requires monitoring, measurement,
analysis, and evaluation as "shall" (mandatory) elements; Clause 9.3 requires management
review. DOJ ECCP 2024: "Are companies appropriately leveraging data analytics tools to
create efficiencies in compliance operations and measure the effectiveness of components
of compliance programs?" USSG §8B2.1(b)(5): monitoring and auditing to detect criminal
conduct is a mandatory element.]

---

#### Domain 9: Incentives and Disciplinary Framework

**Objective:** Reinforce compliance through consistent positive incentives and proportionate,
non-discriminatory discipline for violations.

**Compliance Performance Metrics for Compensation:**

Incorporate into annual performance evaluations for all employees:

1. Training completion (timely, on first attempt for scored assessments)
2. Policy attestation compliance (on time, no exceptions)
3. Code of conduct adherence (no substantiated violations)
4. Cooperation with compliance investigations (no obstruction)
5. Proactive risk reporting (discretionary positive credit for good-faith reports)

For senior leaders and executives, include in performance review and bonus determination:

1. Compliance program implementation milestones within their area of responsibility
2. Third-party DD compliance rate for their function
3. Training completion rates for their team
4. Investigation cooperation / no adverse findings
5. Tone-setting behavior (visible compliance commitment)

[DOJ ECCP 2024 — Compensation Clawback Pilot (March 2023, ongoing): "All DOJ Criminal
Division corporate resolutions will include mandates to adopt compliance-related
compensation and bonus criteria." Companies must withhold bonuses from violators and
provide incentives for compliance-promoting behavior. Clawback of compensation from
wrongdoers can yield up to 25% fine reduction. [VERIFY current program status with
outside DOJ counsel before use in enforcement context.]]

**Disciplinary Matrix:**

Apply the following framework consistently across all business units and levels:

| Violation Severity                                                                  | First Occurrence                              | Repeat Occurrence                    | Senior Leader                    |
| ----------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------ | -------------------------------- |
| **CRITICAL**: Criminal conduct, fraud, bribery, deliberate data breach, obstruction | Termination + law enforcement referral        | —                                    | Same + Board notification        |
| **SERIOUS**: Significant policy violation, reckless disregard, retaliation          | Final written warning or termination          | Termination                          | Termination + Board notification |
| **MODERATE**: Material policy breach, negligent conduct, failure to report          | Written warning + mandatory remedial training | Final written warning or termination | Final written warning            |
| **MINOR**: Technical policy breach, good-faith error                                | Verbal warning + coaching                     | Written warning                      | Written warning                  |

**Consistency audit:** Annually, the CCO and HR should review all disciplinary actions for
consistency — were similar violations treated similarly across different BUs, levels, and
demographic groups? Disparate treatment creates both legal exposure and cultural damage.

[JURISDICTION-SPECIFIC: UK Employment Rights Act 2025 + ACAS Code of Practice require
fair process in disciplinary proceedings (written notice, opportunity to respond, right
to be accompanied). EU employment laws vary by member state — local legal review required
before discipline. US: at-will employment in most states, but wrongful termination claims
still require documented fair process. ISO 37301 — Clause 8.4 addresses non-compliance
and corrective actions as "shall" requirements.]

---

## Program Maturity Model

Assess the compliance program against five maturity levels. Each level represents the
cumulative capability from levels below it.

| Level | Stage      | Governance                                                           | Risk Assessment                                         | Policies                                              | Training                                  | Reporting                                          | Monitoring                             |
| ----- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------- | -------------------------------------------------- | -------------------------------------- |
| **1** | Ad Hoc     | No formal function; compliance driven by individuals                 | None or ad hoc                                          | None or unwritten                                     | None or generic                           | No formal channel                                  | Reactive                               |
| **2** | Developing | Part-time compliance lead; no board mandate                          | Some informal risk awareness                            | Basic, inconsistent policies                          | Mandatory but completion-only             | Channel exists; not widely known                   | Manual; inconsistent                   |
| **3** | Defined    | Dedicated CCO; regular board reporting                               | Annual documented risk assessment                       | Comprehensive, approved policies                      | Role-differentiated; comprehension tested | Accessible, multi-channel; process documented      | Annual controls testing                |
| **4** | Managed    | CCO with board access; compliance embedded in HR/Finance/Procurement | Risk analytics; event-triggered updates                 | Policy exceptions tracked; approval workflow          | Metrics-driven; culture survey            | Metrics tracked; trend analysis                    | Continuous monitoring; data analytics  |
| **5** | Optimizing | CCO on ExCo; compliance embedded in strategy; peer benchmarking      | Predictive risk analytics; competitor incident analysis | Policies updated in real time with regulatory changes | AI-personalized; behavioral analytics     | Speak-up index benchmarked; reporter feedback loop | AI-assisted; real-time board dashboard |

**Minimum Regulatory Expectation (DOJ/SFO defensibility): Level 3**
**ISO 37301 Certification Target: Level 3 (all "shall" elements met)**
**Best-in-Class / DOJ declination-worthy: Level 4-5**

---

## Cross-Framework Alignment Matrix

Every program element satisfies multiple regulatory frameworks simultaneously:

| Domain               | DOJ ECCP 2024                   | USSG §8B2.1 | UK Bribery Act MoJ                 | ISO 37301:2021         | TI BPCB                |
| -------------------- | ------------------------------- | ----------- | ---------------------------------- | ---------------------- | ---------------------- |
| Governance & Board   | Q2 (empowered?)                 | Element 2   | Principle 2 (top-level commitment) | Clause 5.1-5.3         | Leadership             |
| Risk Assessment      | Q1 (well-designed?) + §8B2.1(c) | §8B2.1(c)   | Principle 3 (risk assessment)      | Clause 4.6 (mandatory) | Risk-based design      |
| Code of Conduct      | Q1                              | Element 1   | Principle 1 + 5                    | Clause 8.2             | Programme design       |
| Training             | Q1                              | Element 4   | Principle 5 (communication)        | Clauses 7.2-7.4        | Training               |
| Third-Party DD       | Q1                              | Element 1   | Principle 4 (due diligence)        | Clause 8.3 (mandatory) | Third parties          |
| Monitoring           | Q3 (works in practice?)         | Element 5   | Principle 6 (monitoring)           | Clause 9.1 (mandatory) | Monitoring             |
| Reporting/Speak-Up   | Q2 + Q3                         | Element 5   | Principle 6                        | Clause 8.5 (mandatory) | Reporting              |
| Discipline           | Q2                              | Element 6   | Principle 2                        | Clause 8.4             | Culture enforcement    |
| Response/Improvement | Q3                              | Element 7   | Principle 6                        | Clause 10              | Continuous improvement |

A program meeting all nine domains at Level 3+ provides a defensible basis across all
five frameworks simultaneously. Jurisdiction-specific supplements address areas where
frameworks diverge (UK facilitation payment prohibition; EU whistleblower channel
mandatory timing requirements; ISO 37301 certification audit requirements).

---

### Step 7: Implementation Roadmap

Produce a phased implementation roadmap tailored to the organization's operating mode,
maturity baseline, and regulatory priority.

**Standard Four-Phase Roadmap (12-18 Months for Build New Program mode):**

#### Phase 0 — Foundation (Months 1-3) — CRITICAL

_Deliverables:_

- Governance charter authorizing compliance function
- Board/Audit Committee mandate and reporting framework
- CCO appointment (or designation of responsibility if CCO not yet hired)
- Initial enterprise compliance risk assessment (may be preliminary)
- Code of conduct (initial version; finalize in Phase 1)
- Confidential reporting channel operational
- CCO access to all organizational data systems established

_DOJ ECCP relevance:_ Phase 0 demonstrates "top management commitment" and "empowered
compliance function" — the two most commonly cited deficiencies in DOJ ECCP assessments.

_Board gating:_ Board resolution authorizing compliance program; Audit Committee charter
amendment for compliance oversight; budget appropriation.

_Resource requirements (by organization size):_

- Small (<500): $30K-$75K; 0.5-1.0 FTE
- Mid-market (500-5K): $150K-$400K; 2-3 FTE + external advisors
- Large (5K+): $500K-$1.5M; 3-10 FTE + external advisors

#### Phase 1 — Core Program (Months 4-9) — HIGH PRIORITY

_Deliverables:_

- Finalized Code of Conduct with distribution and acknowledgment
- Core policy library (at minimum: anti-corruption, conflicts, third-party DD,
  investigation, discipline, records retention)
- Risk assessment (full enterprise; heat map)
- Training program — Tiers 1-3 launched; completion targets set
- Third-party due diligence program operational (triage + Tier 1 process)
- Investigation protocol documented and CCO-directed investigations commenced
- RACI matrix approved and communicated

_Board gating:_ CCO reports Phase 1 status; board approves Code of Conduct; Audit
Committee receives first compliance metrics dashboard.

_Resource requirements:_

- Small: $75K-$150K Phase 1; 1.0-2.0 FTE
- Mid-market: $400K-$1M; 4-6 FTE; LMS technology; GRC platform (optional)
- Large: $1.5M-$3M; 6-15 FTE; GRC platform; training platform; third-party screening

#### Phase 2 — Operational Depth (Months 10-15) — MEDIUM PRIORITY

_Deliverables:_

- Full policy library (all 15+ documents)
- Training program — Tiers 4-5 launched; comprehension testing operational
- Third-party due diligence — full lifecycle management; Tier 2 process operational
- Controls testing — first cycle of key controls testing
- Monitoring dashboard — initial metrics reporting to board
- Compensation metrics — compliance criteria integrated in performance reviews

_Board gating:_ First annual compliance program report; board reviews training metrics,
risk register, hotline statistics.

#### Phase 3 — Optimization and Continuous Improvement (Month 16+) — ONGOING

_Deliverables:_

- Data analytics monitoring — automated transaction screening operational
- Annual risk assessment cycle (second year: validate risk register against incidents)
- Program effectiveness review — third-party assessment; culture survey
- Lessons learned integration — incident root cause analysis feeding training updates
- ISO 37301 readiness (if certification objective): gap analysis against all "shall" clauses
- Peer benchmarking (CCCA/SCCE annual survey data)
- Board reporting — mature metrics dashboard with year-over-year trend analysis

**Accelerated Roadmap (for Optimize mode):** Conduct gap analysis in weeks 1-2;
produce prioritized remediation backlog; implement quick wins (hotline, risk assessment,
Code of Conduct acknowledgment) in months 1-2; address structural gaps (governance,
investigation protocol, monitoring) in months 3-6.

---

### Step 8: Quality Verification

Before delivering any output, run these quality checks silently. Revise failures before
delivery.

---

## Quality Frameworks

### Citation Quality Gates

Run these five gates against every regulatory reference before delivery:

| Gate           | Rule                                                                                                                                                                              | Fail Action                                                     |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, official guidance, or recognized principle                                                                                | Add citation or mark "[UNVERIFIED]"                             |
| **Format**     | Citations follow a recognizable format for the jurisdiction (US: statute number and section; UK: Act name + year + section; EU: Regulation/Directive with OJ reference)           | Fix format                                                      |
| **Currency**   | Every cited provision checked for amendments; DOJ ECCP checked against September 2024 update; ISO 37301 cited as 2021 edition                                                     | Flag "[CHECK CURRENCY — law may have changed]"                  |
| **Domain**     | Analysis stays within the applicable regulatory framework; no cross-contamination of jurisdictions (e.g., don't apply UK facilitation payment prohibition as if it applies in US) | Flag "[JURISDICTION-SPECIFIC: applies in X only]"               |
| **Confidence** | Uncertainty about how a provision applies in context is explicitly stated                                                                                                         | Add confidence qualifier per Confidence Scoring framework below |

### Self-Interrogation for High-Severity Items

For any domain rated INADEQUATE where the regulatory exposure is HIGH, apply this
three-pass review before delivering findings:

**Pass 1 — Legal Chain Integrity:** Does the gap assessment follow logically from the
cited regulatory requirement? Would a DOJ prosecutor or SFO investigator reach the same
conclusion about adequacy? What specific DOJ ECCP question or USSG element does this
gap affect?

**Pass 2 — Completeness:** Have all applicable frameworks been considered? Is the gap
present in DOJ ECCP AND UK Adequate Procedures AND ISO 37301, or only one? Are there
compensating controls elsewhere in the program that partially mitigate the gap?

**Pass 3 — Challenge:** What is the strongest argument that the organization's existing
practices ARE adequate? Under what circumstances would a court or enforcement agency
accept the current state? Document this argument; include it in the board presentation
as "management's position."

### Confidence Scoring

| Level        | Range     | Meaning                                                                        | Action                                                          |
| ------------ | --------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear regulatory requirement with published authority; well-established        | State with confidence                                           |
| **High**     | 0.80-0.94 | Strong authority; minor interpretive questions                                 | State with brief caveat                                         |
| **Probable** | 0.60-0.79 | Good arguments; enforcement practice may vary; jurisdiction-specific questions | State with reasoning and contra-indicators                      |
| **Possible** | 0.40-0.59 | Genuinely uncertain; enforcement guidance unclear                              | Flag for legal counsel review with both sides                   |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                                        | Do not assert; flag "[UNCERTAIN — verify with outside counsel]" |

---

## Glass Box Audit Trail

Append this template to every compliance program output:

```yaml
glass_box:
  skill: "legalcode-compliance-program-builder"
  assessment_date: "[YYYY-MM-DD]"
  organization: "[name or 'Not disclosed']"
  operating_mode: "[Build New / Optimize / Assessment Only / Board Presentation]"
  primary_jurisdiction: "[US / UK / EU / Multinational — list]"
  frameworks_applied: "[DOJ ECCP Sept 2024 / UK Bribery Act MoJ Principles / ISO 37301:2021 / USSG §8B2.1 / TI BPCB — check all applied]"
  legalcode_mcp_connected: "[Yes / No — if No, all citations require manual verification]"
  domain_ratings:
    governance_board_oversight: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    risk_assessment: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    code_of_conduct_policies: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    training_communication: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    third_party_due_diligence: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    confidential_reporting: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    investigation_protocol: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    monitoring_testing: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
    incentives_discipline: "[EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]"
  overall_maturity_level: "[1-5]"
  critical_gaps: "[List domains rated INADEQUATE with HIGH regulatory exposure]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  key_assumptions:
    - "[Assumption 1 — e.g., 'Anti-corruption is primary driver; adjust if primary driver differs']"
    - "[Assumption 2 — e.g., 'Organization not yet subject to CSDDD scope threshold']"
  limitations:
    - "[Limitation 1 — e.g., 'Personnel competence not assessed; recommend HR/external review']"
    - "[Limitation 2 — e.g., 'Program effectiveness requires empirical testing to verify']"
  verification_checklist:
    - "[ ] DOJ ECCP September 2024 version confirmed as current"
    - "[ ] UK Bribery Act MoJ guidance — verify for any post-2010 updates or case law"
    - "[ ] ISO 37301:2021 — confirm edition is current; verify certification body requirements"
    - "[ ] EU Whistleblower Directive — confirm member state transposition in relevant jurisdictions"
    - "[ ] Clawback pilot program — verify current status with DOJ Criminal Division"
    - "[ ] CSDDD scope threshold — confirm current employee/turnover thresholds [amended post-Omnibus I]"
  reviewer: "AI-assisted assessment — requires review by qualified compliance counsel before reliance"
```

---

## Anti-Patterns

These are the most common — and most costly — compliance program design failures. Apply
this catalogue at Step 8 before delivery.

### Governance Anti-Patterns

1. **No independent CCO** — Compliance function reporting to General Counsel only, with
   no direct Board/Audit Committee access. DOJ ECCP explicitly evaluates CCO independence.
   _Fix: CCO reports to CEO operationally; direct access to Audit Committee chair;
   no GC intermediation for reporting._

2. **Under-resourced CCO** — Senior CCO title with a team of one and a budget that is
   10% of the sales department's expense account. DOJ ECCP asks whether the compliance
   function is adequately resourced relative to business operations.
   _Fix: Benchmark compliance headcount against revenue, transaction volume, and
   peer companies. Document benchmarking analysis for board._

3. **Compliance as legal department annex** — Compliance is a junior function of Legal,
   with no independent authority, no direct business access, and a CCO who is outranked
   by the GC on all compliance decisions.
   _Fix: CCO and GC are peers; their roles are complementary not hierarchical on compliance._

4. **Board mandate without board engagement** — A compliance charter exists on paper but
   the Board has never received a substantive compliance briefing.
   _Fix: Annual substantive compliance briefing to Board; Audit Committee receives quarterly
   metrics dashboard; CCO meets individually with independent directors annually._

### Risk Assessment Anti-Patterns

5. **One-and-done risk assessment** — The risk assessment was conducted once at program
   launch and has not been updated despite significant business changes.
   _Fix: Mandatory annual cycle + event-triggered updates for M&A, new market entry,
   significant enforcement action in sector, internal incident._

6. **Risk assessment conducted by compliance alone** — Business unit heads were never
   consulted; risk assessment does not reflect operational reality.
   _Fix: Risk assessment requires business unit interviews; CCO validates with Internal
   Audit; Audit Committee approves the final risk register._

7. **Controls not assessed separately from risk** — Risk assessment conflates inherent
   risk with residual risk. A high-risk area with weak controls looks the same as a
   low-risk area.
   _Fix: Three-part methodology: inherent risk → control effectiveness → residual risk._

### Code of Conduct Anti-Patterns

8. **Generic global code with no localization** — A single English-language document
   covering 40 countries, none of whom received it in their working language.
   _Fix: Core global code + jurisdiction supplements; translation into all languages
   covering 5%+ of workforce._

9. **Code of Conduct never updated** — The Code mentions no social media, no AI, no
   data privacy obligations, and references a regulator that no longer exists.
   _Fix: Annual review; update within 90 days of material regulatory change._

### Training Anti-Patterns

10. **Completion-only tracking** — Training completion rates are reported to the Board
    as a proxy for program effectiveness, but there is no comprehension testing.
    _Fix: All employee and manager training requires comprehension testing at 80%
    pass threshold; Board receives comprehension rates, not just completion rates._

11. **One-size training** — Board members receive the same training as line workers;
    sales representatives receive the same training as IT staff.
    _Fix: Role-differentiated curriculum; high-risk roles receive enhanced training
    specific to their risk exposures (see Tier 4 requirements)._

12. **No training on AI/emerging technology risks** — DOJ ECCP 2024 explicitly requires
    this. Organizations with no AI-specific compliance training are exposed.
    _Fix: Add AI/technology risk module to annual training; update annually._

### Third-Party Due Diligence Anti-Patterns

13. **Self-certification only** — Tier 1 vendors are asked to certify their own compliance.
    There is no independent verification.
    _Fix: Tier 1 due diligence requires independent adverse media screening, sanctions
    screening, and UBO verification — not just a questionnaire._

14. **No periodic re-screening** — A Tier 1 agent engaged four years ago has not been
    re-screened despite a change of ownership.
    _Fix: Annual Tier 1 recertification; event-triggered re-screening for all tiers._

15. **Business rationale not documented** — The organization cannot explain to a DOJ
    investigator why it engaged a particular agent in a particular market.
    _Fix: Document business rationale for every third-party engagement before onboarding;
    retain documentation indefinitely for Tier 1 agents._

### Confidential Reporting Anti-Patterns

16. **Hotline known only to headquarters** — Reports per 100 employees are extremely low
    in international operations because employees there don't know the channel exists.
    _Fix: Annual communication of reporting channel details to all employees in all
    jurisdictions in their working language; include in new-hire orientation._

17. **Management investigates their own team's allegations** — The subject's manager
    conducts the investigation, is briefed on reporter identity, and has access to the file.
    _Fix: Investigators must be independent of subjects; any report about a manager
    routes around that manager's chain entirely._

18. **No feedback loop to reporters** — Reporters never receive any acknowledgment or
    outcome communication, leading to perception that reports disappear.
    _Fix: Acknowledge receipt within 5 business days; provide non-disclosing outcome
    communication within 30 days of case closure._

### Monitoring Anti-Patterns

19. **No data analytics** — DOJ ECCP 2024 explicitly evaluates whether companies are
    using data analytics for compliance monitoring. A manually intensive program that
    cannot detect patterns is less defensible.
    _Fix: Even basic data analytics (expense report anomaly flags, third-party payment
    pattern analysis) demonstrates proactive monitoring._

20. **Internal audit reports to management** — Internal audit independence is compromised
    when audit results are filtered through management before reaching the Audit Committee.
    _Fix: Internal audit function reports functionally to Audit Committee; unrestricted
    direct access. This is also an NYSE/NASDAQ listing requirement for public companies._

21. **Compliance metrics dashboard optimized for good news** — Board presentations show
    only completion rates and low violation counts, omitting substantive analysis of
    whether the program is working.
    _Fix: Board dashboard includes trend data, comparison to prior periods, benchmarking
    against industry, and frank assessment of gaps._

22. **No post-investigation lessons learned process** — Investigations conclude, discipline
    is imposed, and the file is closed — but the control failure that enabled the misconduct
    is never addressed.
    _Fix: Root cause analysis is mandatory for all substantiated investigations; findings
    feed policy updates and training content within 90 days._

---

## Writing Standards

Apply these standards to every compliance program output before delivery:

1. **Plain language first** — Every policy and procedure must be understandable by an
   employee without legal training. If a compliance professional would not find it
   ambiguous, but a line manager would, rewrite it for the line manager.

2. **Imperative voice** — Write requirements as clear obligations: "You must disclose all
   conflicts of interest." Not: "Employees are encouraged to consider disclosing interests."

3. **Examples for abstract obligations** — Every prohibition benefits from at least one
   concrete example. "You may not give gifts worth more than $100 to any customer or
   supplier — for example, tickets to a sporting event worth $200 would require prior
   written approval."

4. **No ambiguous wording in CRITICAL requirements** — Words like "generally," "normally,"
   "typically," and "as appropriate" are forbidden in core prohibitions. Reserve hedged
   language for genuinely discretionary matters.

5. **Consistent defined terms** — Define terms once in each document; use them consistently.
   Do not use "gift" and "benefit" interchangeably if they have different meanings.

6. **One policy, one version** — Every published policy must carry: version number,
   approval date, CCO and GC approval signatures, next scheduled review date.
   Superseded versions must be clearly archived, not circulating alongside current versions.

7. **Verification before delivery** — Before delivering any output referencing regulatory
   authority, verify: (a) statute/regulation is current, (b) citation format is correct,
   (c) confidence level is explicitly stated for any interpretive claim.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
Search for:

- DOJ ECCP latest version (confirm September 2024 is most current)
- UK MoJ Bribery Act guidance updates
- ISO 37301:2021 certification body requirements
- USSG 2025 Guidelines Manual Chapter 8
- EU Whistleblower Directive member state transposition status
- Relevant recent enforcement actions (DOJ, SFO, SEC, EU) in the organization's sector
- Sector-specific compliance overlays (HIPAA, GLBA, FINRA, etc.)

Save research to `/tmp/legalcode-compliance-program-research.md`. Mark all MCP-sourced
citations as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**
Proceed with repository analysis and general knowledge. Mark all statutory/regulatory
citations with [VERIFY]. Note in Glass Box: `legalcode_mcp_connected: "No — all
citations require manual verification against authoritative sources."` Focus the output
on structural quality, workflow design, and framework application rather than specific
regulatory depth.

**GRC Platform Integration:**
When available, structure monitoring dashboards, risk registers, and reporting templates
for direct import into:

- **ServiceNow GRC**: JSON format for policy acknowledgment, incident tracking
- **Workiva**: XBRL-compatible for CSRD/ESG compliance reporting
- **OneTrust**: Privacy-layer compliance; DPA management; cookie/consent integration
- **MetricStream**: Risk and compliance management; audit trail export
- **NAVEX (EthicsPoint)**: Hotline intake; case management; investigation workflow

---

## Output Format Template

Every compliance program output should follow this structure:

---

### COMPLIANCE PROGRAM ASSESSMENT

**Organization:** [name]
**Date:** [YYYY-MM-DD]
**Prepared by:** [AI-assisted | reviewed by: _____]
**Mode:** [Build New / Optimize / Assessment Only / Board Presentation]
**Framework(s) Applied:** [DOJ ECCP 2024 / UK Bribery Act MoJ / ISO 37301:2021 / USSG §8B2.1]

---

#### EXECUTIVE SUMMARY

_One-paragraph summary of overall compliance program maturity, primary gaps, and
recommended prioritization. Written for a board member without legal training._

| Overall Maturity Level     | Primary Gaps         | Immediate Priorities |
| -------------------------- | -------------------- | -------------------- |
| Level [1-5] — [Stage name] | [Domain 1, Domain 2] | [Phase 0 actions]    |

---

#### DOMAIN ASSESSMENT SCORECARD

| Domain                        | Current Rating                             | Regulatory Exposure | Priority | Phase |
| ----------------------------- | ------------------------------------------ | ------------------- | -------- | ----- |
| 1. Governance & Board         | [EFFECTIVE/ADEQUATE/DEVELOPING/INADEQUATE] | [HIGH/MEDIUM/LOW]   |          |       |
| 2. Risk Assessment            |                                            |                     |          |       |
| 3. Code of Conduct & Policies |                                            |                     |          |       |
| 4. Training & Communication   |                                            |                     |          |       |
| 5. Third-Party Due Diligence  |                                            |                     |          |       |
| 6. Confidential Reporting     |                                            |                     |          |       |
| 7. Investigation Protocol     |                                            |                     |          |       |
| 8. Monitoring & Testing       |                                            |                     |          |       |
| 9. Incentives & Discipline    |                                            |                     |          |       |

---

#### REGULATORY APPLICABILITY SUMMARY

| Framework                      | Applicable? | Primary Obligation | Most Recent Key Update | Known Exposure |
| ------------------------------ | ----------- | ------------------ | ---------------------- | -------------- |
| DOJ ECCP 2024                  |             |                    |                        |                |
| UK Bribery Act §7              |             |                    |                        |                |
| ISO 37301:2021                 |             |                    |                        |                |
| USSG §8B2.1                    |             |                    |                        |                |
| EU Whistleblower Directive     |             |                    |                        |                |
| [Sector overlay if applicable] |             |                    |                        |                |

---

#### GAP FINDINGS AND RECOMMENDATIONS

For each domain rated DEVELOPING or INADEQUATE:

**Domain [N]: [Name]**

- **Current State:** [Description of what exists today]
- **Gap:** [Specific gap against regulatory expectation, with citation]
- **Risk:** [What enforcement/legal risk this creates; confidence level]
- **Recommendation:** [Specific action with owner, timeline, and success metric]
- **Phase:** [Phase 0 / Phase 1 / Phase 2 / Phase 3]
- **Priority:** [CRITICAL / HIGH / MEDIUM / LOW]

---

#### CROSS-FRAMEWORK ALIGNMENT STATUS

| Domain     | DOJ ECCP                         | UK Adequate Procedures            | ISO 37301                      | USSG §8B2.1                     |
| ---------- | -------------------------------- | --------------------------------- | ------------------------------ | ------------------------------- |
| [Domain 1] | [Q1/Q2/Q3 — Met/Partial/Not Met] | [Principle — Met/Partial/Not Met] | [Clause — Met/Partial/Not Met] | [Element — Met/Partial/Not Met] |

---

#### IMPLEMENTATION ROADMAP

| Phase                      | Months | Key Deliverables                                                     | Owner                | Resources | Board Gate               |
| -------------------------- | ------ | -------------------------------------------------------------------- | -------------------- | --------- | ------------------------ |
| Phase 0: Foundation        | 1-3    | Governance charter, CCO mandate, initial risk assessment, hotline    | CCO                  | $[budget] | Board resolution         |
| Phase 1: Core Program      | 4-9    | Code of Conduct, core policies, training launch, third-party program | CCO + HR             | $[budget] | Audit Committee review   |
| Phase 2: Operational Depth | 10-15  | Full policy library, monitoring dashboard, controls testing          | CCO + Internal Audit | $[budget] | Annual compliance report |
| Phase 3: Optimization      | 16+    | Data analytics, program effectiveness review, ISO 37301 readiness    | CCO                  | $[budget] | Board benchmarking       |

---

#### BOARD-READY COMPLIANCE PROGRAM SUMMARY

_This section is designed for board presentation. One page maximum._

- **Program Maturity:** Level [N] — [Stage]
- **Regulatory Exposure (primary):** [High / Medium / Low] — [Primary driver and rationale]
- **Critical Gaps Requiring Immediate Action:** [Number] gap(s) — see detail in Gap Findings
- **Recommended Investment (Year 1):** $[range] / [N] FTE — see Implementation Roadmap Phase 0-1
- **DOJ/SFO Defensibility Assessment:** [Yes / Partial / Not Yet] — based on current program state
- **ISO 37301 Certification Readiness:** [Ready / 12-18 months to ready / Not applicable]
- **Next Board Review Recommended:** [Quarterly until Critical gaps closed; then annual]

---

_[Glass Box Audit Trail — append here]_

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis. Research pipeline:
2-agent parallel research (structural analysis of `legalcode-regulatory-change-tracker`,
`legalcode-incident-response-plan-builder`, and `legalcode-ai-governance-framework-builder`
as reference standards; web-backed legal research via WebSearch covering DOJ ECCP September
2024, UK Bribery Act MoJ Six Principles, R v Skansen Interiors Limited (2018), ISO
37301:2021 vs. ISO 19600:2014 comparison, US Sentencing Guidelines §8B2.1 (2025 edition),
Transparency International Business Principles for Countering Bribery (third edition),
compliance risk assessment methodology, third-party due diligence tier framework, hotline
effectiveness research, monitoring and testing standards, compliance maturity model, and
4-phase implementation roadmap best practices). No legalcode-mcp connections; all
citations require verification against authoritative sources. Cross-references: DOJ ECCP
September 2024; UK MoJ Bribery Act 2010 Guidance; ISO 37301:2021; USSC 2025 Guidelines
Manual Chapter 8; EU Directive 2019/1937 (Whistleblower); EU CSDDD Directive 2024/1760;
EU AMLR (effective July 10, 2027).
