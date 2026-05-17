---
name: legalcode-ai-governance-framework-builder
description: >
  Builds comprehensive organizational AI governance frameworks aligned with ISO/IEC
  42001:2023 (AI Management System) and the NIST AI Risk Management Framework (AI RMF
  1.0). Covers governance structure (AI ethics committee, RACI matrix, reporting lines),
  policy development suite (acceptable use, risk classification, procurement, training
  data), risk management lifecycle (MAP, MEASURE, MANAGE, GOVERN functions), risk-tiered
  use case approval workflows, model lifecycle management (development, testing, deployment,
  monitoring, retirement), vendor and third-party AI assessment criteria, AI incident
  response procedures, and ongoing monitoring and audit programs. Use when an organization
  needs to establish, audit, or mature its AI governance posture; prepare for ISO 42001
  certification; align with NIST AI RMF; satisfy EU AI Act deployer obligations; respond
  to board or investor AI governance inquiries; or produce a customizable AI governance
  documentation suite with an implementation roadmap. Produces governance framework
  documentation, policy templates, workflow designs, RACI matrices, and a phased
  implementation roadmap.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode AI Governance Framework Builder

> **Disclaimer**: This skill provides a framework for AI-assisted organizational AI
> governance design. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional, AI governance specialist, or compliance officer before
> use. ISO 42001, NIST AI RMF, and applicable regulations evolve; verify current versions
> and regulatory requirements before relying on any provision described here. Statutory,
> regulatory, and standards references cited from training-data knowledge carry hallucination
> risk — verify against official sources (ISO.org, NIST AI RMF, applicable regulators)
> before relying on them. Mark all unverified references [VERIFY].

---

## Purpose and Scope

This skill builds a comprehensive AI governance framework tailored to the organization's
industry, size, AI maturity, and regulatory environment. It operationalizes the two most
widely adopted AI governance standards — ISO/IEC 42001:2023 (AI Management System) and
the NIST AI Risk Management Framework AI RMF 1.0 — while also addressing sector-specific
regulatory obligations (EU AI Act, HIPAA AI guidance, financial services AI governance,
and others as applicable).

**Covers:**
- Governance structure design (AI committee, board oversight, roles and responsibilities)
- Full AI governance policy suite (acceptable use, risk classification, procurement, training data, model lifecycle)
- Risk-tiered AI use case classification and approval workflow
- Model lifecycle management framework (development, validation, deployment, monitoring, retirement)
- Third-party and vendor AI assessment process
- AI incident response procedures and escalation framework
- Ongoing monitoring, audit, and review program
- ISO/IEC 42001:2023 alignment assessment (Clauses 4–10)
- NIST AI RMF 1.0 alignment assessment (GOVERN, MAP, MEASURE, MANAGE)
- Phased implementation roadmap with prioritized milestones
- Governance documentation suite (template library)

**Does not:**
- Constitute legal advice or replace qualified AI governance counsel
- Provide a substitute for formal ISO 42001 certification audit
- Cover technical AI safety research (adversarial robustness, interpretability) beyond governance-relevant requirements
- Address GPAI model-provider obligations under EU AI Act Chapter V in detail (use `legalcode-eu-ai-act-high-risk-compliance` for EU AI Act Article 6/Annex III high-risk assessments)
- Conduct DPIA for AI systems processing personal data (use `legalcode-dpia-generator`)
- Assess individual AI system bias or fairness in depth (cross-reference specialized fairness tools)

**Related skills:**
- `legalcode-eu-ai-act-high-risk-compliance` — EU AI Act Annex III high-risk classification and conformity assessment
- `legalcode-dpia-generator` — GDPR DPIA for AI systems processing personal data
- `legalcode-data-mapping-workflow` — AI training data inventory and lineage mapping
- `legalcode-incident-response-plan-builder` — full cybersecurity/data breach IRP (cross-reference for AI incident response)
- `legalcode-regulatory-change-tracker` — monitoring ongoing AI regulatory developments
- `legalcode-vendor-ai-assessment` — deep-dive vendor AI due diligence (if available)

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill built on globally recognized frameworks (ISO 42001,
NIST AI RMF). The governance framework should be adapted to the organization's operating
jurisdictions using the [JURISDICTION-SPECIFIC] markers below.

**Framework alignment:**
- **ISO/IEC 42001:2023** — global AI Management System standard; audit/certification pathway available
- **NIST AI RMF 1.0** — voluntary, sector-agnostic framework; widely referenced by US government, financial services, and healthcare
- **EU AI Act (Regulation 2024/1689)** — mandatory for EU market participants; enforcement timeline 2025-2026
- **NIST AI RMF + Executive Order 14110 / OMB M-24-10** — [JURISDICTION-SPECIFIC: US federal agencies; verify with current OMB guidance]

[JURISDICTION-SPECIFIC] When localizing, research and apply sector-specific AI governance requirements:
- **EU**: EU AI Act deployer obligations (Arts. 25-27); GDPR Art. 22 automated decision-making; NIS2 for AI in critical infrastructure
- **United States**: NIST AI RMF; sector regulator guidance (OCC/Federal Reserve for financial AI; OCR HIPAA AI guidance for health AI; SEC AI-related disclosure obligations; FTC AI guidance); state AI laws (Colorado SB 205, Texas HB 4497, California SB 1047 [VERIFY status])
- **United Kingdom**: ICO AI Auditing Framework; National AI Strategy; AI Safety Institute guidance
- **Canada**: ISED Voluntary Code of Conduct on the Responsible Development of Advanced Generative AI Systems; Algorithmic Impact Assessment (Treasury Board); AIDA [VERIFY status]
- **Australia**: National AI Framework; voluntary AI Safety Standard; Privacy Act AI guidance (OAIC)
- **China**: Generative AI Regulation (CAC); Algorithm Recommendation Regulation [VERIFY current versions]
- **Singapore**: Model AI Governance Framework (PDPC/IMDA); AI Verify testing framework
- **Financial services**: BCBS guidance on AI/ML in banking; EBA/ESA AI guidance; FINRA AI governance requirements; SEC AI model risk management
- **Healthcare**: FDA Software as a Medical Device (SaMD); HHS OCR HIPAA AI guidance; ONC health IT AI certification
- **Government/defence**: NIST AI RMF for DoD; ISO 42001 government sector annexes

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the organization's context, the workflow pauses and asks when:

- The answer changes the governance model design or scope
- Multiple valid architectural approaches exist (centralized vs. federated governance)
- Industry-specific regulatory overlay is needed
- The organization's AI maturity level determines what to prioritize
- Risk tolerance decisions affect classification thresholds

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

Accept the engagement brief in any of these formats:
- **Organization description**: Industry, size, AI use cases in scope, current governance state
- **Existing policies**: Any current AI policy, acceptable use policy, or governance documentation for gap analysis
- **Regulatory driver**: Specific regulation or framework to align with (ISO 42001, NIST AI RMF, EU AI Act, etc.)
- **Scope specification**: Which framework components are needed (full suite vs. specific policies)
- **Maturity assessment request**: Baseline assessment against ISO 42001 or NIST AI RMF

If no input is provided, prompt: "Please describe your organization, industry, current AI usage, and primary governance objective."

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Ask these questions before proceeding. Present as structured options:

1. **Organization type and industry:**
   - Options: Financial services / banking, Healthcare / life sciences, Technology / software, Manufacturing / industrial, Retail / e-commerce, Government / public sector, Professional services (legal, consulting), Energy / utilities, Other
   - *Why this matters*: Industry determines which sector-specific AI regulations apply (HIPAA for health AI, BCBS for financial AI, FDA SaMD for medical AI) and what risk tolerance is appropriate.

2. **Primary AI use cases (select all that apply):**
   - Options: Customer-facing AI (chatbots, recommendations), Internal productivity tools (coding assistants, document review), AI in HR/hiring decisions, AI in credit/lending/insurance decisions, AI in medical diagnosis or clinical decision support, Generative AI / LLMs for content creation, AI for fraud detection and security, AI in manufacturing/supply chain, AI for data analytics and forecasting
   - *Why this matters*: High-stakes use cases (hiring, lending, medical) trigger stricter governance requirements; consumer-facing AI has transparency obligations; GPAI/LLM use requires different controls than narrow AI.

3. **Current AI governance maturity:**
   - Options:
     - **Level 1 — Ad Hoc**: No formal AI governance; using AI tools informally; no policies
     - **Level 2 — Emerging**: Some AI policies exist (e.g., acceptable use) but no formal framework; informal oversight
     - **Level 3 — Defined**: Formal AI governance structure in place; policies documented; risk classification exists but inconsistently applied
     - **Level 4 — Managed**: Mature governance framework; systematic model lifecycle management; audit program active
     - **Level 5 — Optimizing**: Continuous improvement cycle; board-level AI oversight; ISO 42001 certified or pursuing certification
   - *Why this matters*: Lower maturity organizations need foundation-building (policies, roles) before process controls; higher maturity organizations need gap analysis and optimization.

4. **Governance model preference:**
   - Options:
     - **Centralized**: Single AI governance committee owns all decisions; enterprise-wide policies uniformly applied; strong central oversight
     - **Federated**: Central framework and standards with business-unit autonomy; decentralized implementation; designated AI owners per BU
     - **Hybrid**: Central policy-setting and high-risk approvals; BU-level execution and monitoring for standard-risk AI
   - *Why this matters*: Organizational structure and AI distribution determine feasibility; federated models work better for large enterprises with diverse AI needs; centralized models suit mid-size organizations or those with concentrated AI risk.

5. **Primary framework alignment objective:**
   - Options:
     - **ISO 42001 certification pathway** — Full AIMS per ISO/IEC 42001:2023 Clauses 4–10; audit-ready documentation
     - **NIST AI RMF alignment** — Map controls to GOVERN/MAP/MEASURE/MANAGE; US regulatory positioning
     - **EU AI Act deployer compliance** — Focus on Arts. 25-27; use case risk classification per Annex III
     - **General best-practice framework** — Comprehensive governance without formal certification target
     - **Multiple frameworks** — Cross-walk ISO 42001 + NIST AI RMF + applicable regulations
   - *Why this matters*: Determines documentation format, required elements, and certification roadmap.

6. **Output scope:**
   - Options:
     - **Full governance documentation suite** — All 8 governance documents + roadmap
     - **Framework and policy outline only** — Structure and key provisions, not full text
     - **Gap analysis against existing policies** — Assess current state vs. target framework
     - **Specific components** — Select which documents are needed
   - *Why this matters*: Full suite is appropriate for organizations building from scratch; gap analysis is appropriate for organizations with existing policies; specific components suit targeted improvements.

7. **Highest-priority risk tolerance:**
   - Options:
     - **Conservative**: Avoid all high-risk AI use cases until governance is mature; extensive review for any consequential AI use
     - **Balanced**: Risk-proportionate controls; high-risk AI subject to rigorous process; low-risk AI fast-tracked
     - **Progressive**: Enable AI innovation; lightweight governance for most use cases; intensive controls reserved for clearly high-risk scenarios
   - *Why this matters*: Risk tolerance drives classification threshold design, approval workflow stringency, and which AI use cases require full review vs. expedited review.

### Step 3: Research Regulatory Landscape

Based on the organization's industry and jurisdictions identified in Step 2:

1. **Identify applicable AI regulations** using the [JURISDICTION-SPECIFIC] guidance in the Jurisdiction section. List each applicable regulation with: name, citation, effective date, and key obligations relevant to the organization.

2. **Check for sector-specific requirements** that override or supplement the general framework:
   - Financial services: BCBS Principles for Operational Resilience; OCC model risk management (SR 11-7) [VERIFY if AI-specific update published]
   - Healthcare: FDA's AI/ML-based SaMD action plan; OCR HIPAA AI guidance
   - Government: NIST AI RMF for agencies (per EO 14110); OMB M-24-10
   - Critical infrastructure: NIS2 Art. 23 incident reporting for AI-caused incidents

3. **Map applicable frameworks** to the governance components in Step 7 using the ISO 42001 / NIST AI RMF crosswalk in the Deep Analysis section.

**If legalcode-mcp is connected:** Search for current AI governance regulations in applicable jurisdictions. Save results to `/tmp/legalcode-ai-gov-research.md`. Mark legalcode-mcp-sourced citations as VERIFIED.

**If legalcode-mcp is not connected:** Proceed with framework knowledge documented in this skill. Mark all specific regulatory citations with [VERIFY]. Note in Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`.

### Step 4: Assess Current Governance State

If the organization has provided existing AI policies, governance documents, or maturity self-assessment:

1. **Map existing elements** against the 8 governance components in Step 7
2. **Identify gaps**: Components absent entirely (GAP-ABSENT), components partially addressed (GAP-PARTIAL), and components meeting the target standard (COMPLIANT)
3. **Classify each gap** by severity:

| Gap Severity | Definition | Example |
|---|---|---|
| **CRITICAL** | Required by applicable regulation; absent or clearly non-compliant | No AI incident reporting procedure; EU AI Act Art. 73 requires one |
| **HIGH** | Required by ISO 42001 or NIST AI RMF; material risk if absent | No AI risk classification system; all AI deployed without risk assessment |
| **MEDIUM** | Best practice; creates governance risk if absent | No formal model validation step before deployment |
| **LOW** | Enhancement; appropriate for higher maturity organizations | No formal AI skills development program |

4. **Produce a gap summary table** (used in the output roadmap):

| Governance Component | Status | Gap Severity | Priority | Owner |
|---|---|---|---|---|
| [Component name] | [COMPLIANT / GAP-PARTIAL / GAP-ABSENT] | [CRITICAL/HIGH/MEDIUM/LOW] | [1-4] | [Role/TBD] |

**⟁ CLARIFY** — If existing documentation is provided, confirm: "Should I prioritize filling the CRITICAL and HIGH gaps first (recommended), or address all components comprehensively in a single pass?"

### Step 5: Design Governance Structure

Design the organizational AI governance structure appropriate to the organization's size, maturity, and governance model preference.

#### 5a. Governance Bodies

**For all organizations — Core Bodies:**

| Body | Purpose | Membership | Meeting Cadence | Decision Authority |
|---|---|---|---|---|
| **AI Governance Committee (AGC)** | Cross-functional oversight; policy approval; high-risk use case sign-off; escalation body for AI risk | CTO/CIO (Chair), CLO/General Counsel, CPO/DPO, CISO, CHRO (if people-use AI), Business Unit heads (rotating), CFO (for high-cost AI projects) | Quarterly (at minimum); as-needed for major AI deployments or incidents | Approve/reject Tier 3 (High Risk) use cases; set enterprise AI policy; report to Board |
| **AI Review Board (ARB)** or **AI Center of Excellence (CoE)** | Technical and risk review for proposed AI use cases; model validation; vendor assessment; Tier 2 approvals | Head of AI/ML, Data Science leads, Risk/Compliance, Legal, IT Security, relevant Business Unit | Monthly; as-needed for use case pipeline | Approve/reject Tier 2 (Limited Risk) use cases; flag Tier 3 for AGC escalation |
| **AI Owners (per use case)** | Accountable for individual AI system from deployment to retirement | Business Unit lead responsible for the AI application | Continuous | Day-to-day operational decisions; escalate to ARB for changes or incidents |

**For enterprises (>1,000 employees) — Enhanced Structure:**

| Enhanced Body | Purpose |
|---|---|
| **Board AI Subcommittee** (or integration with existing Risk/Audit Committee) | Board-level oversight; annual AI governance report; major incident notification; strategic AI risk review |
| **Chief AI Officer (CAIO)** | Enterprise-wide AI strategy; governance program ownership; external AI regulatory engagement |
| **AI Ethics Advisory Panel** | Independent ethical review for AI systems with significant societal impact; external perspective; advisory only |

[JURISDICTION-SPECIFIC] **EU**: Consider whether a "human oversight" role per EU AI Act Art. 14 is required for high-risk systems. **US regulated industries**: Model Risk Management (SR 11-7) functions may absorb AI governance functions in banks.

#### 5b. Roles and Responsibilities (RACI)

| Activity | AGC | ARB/CoE | AI Owner | CISO | Legal/CLO | DPO | HR | Audit |
|----------|:---:|:-------:|:--------:|:----:|:---------:|:---:|:--:|:-----:|
| Set enterprise AI policy | **A** | R | C | C | C | C | C | I |
| Risk-classify AI use cases | I | **A** | R | C | C | C | I | I |
| Approve Tier 3 (High Risk) deployments | **A** | R | C | C | C | C | I | I |
| Approve Tier 2 (Limited Risk) deployments | I | **A** | R | C | I | I | I | I |
| Approve Tier 1 (Minimal Risk) deployments | I | I | **A** | I | I | I | I | I |
| Model validation before deployment | I | **A** | R | C | I | I | I | I |
| Vendor AI due diligence | I | R | C | R | **A** | C | I | I |
| AI incident response (declaration) | **A** | C | R | R | C | C | I | I |
| AI incident regulatory notification | C | I | C | C | **A** | **A** | — | I |
| Monitor deployed AI systems | I | C | **A** | C | I | C | I | I |
| Annual AI governance audit | C | C | C | C | C | C | I | **A** |
| AI training and awareness | I | C | C | I | C | C | **A** | I |
| Board AI governance report | **A** | C | I | C | C | I | I | C |

#### 5c. Reporting Lines

Design the reporting hierarchy adapted to the selected governance model:

**Centralized model:**
```
Board of Directors / Board Risk Committee
    └── AI Governance Committee (AGC)
        ├── AI Review Board (ARB) / Center of Excellence
        │   ├── AI Owners (Business Unit Level)
        │   └── Model Validators (Technical)
        ├── AI Ethics Advisory Panel (Advisory)
        └── Functional Oversight: CISO | Legal | DPO | Audit
```

**Federated model:**
```
Board of Directors
    └── AI Governance Committee (AGC) [Enterprise Policy + Tier 3 decisions]
        ├── Business Unit AI Governance Leads [Tier 1-2 decisions + execution]
        │   └── AI Owners (per use case)
        ├── Central AI CoE [Standards, tooling, guidance, training]
        └── Enterprise Risk, Legal, CISO, DPO [Cross-cutting oversight]
```

### Step 6: Develop AI Risk Classification System

Build the risk classification framework that will be applied to all AI use cases in the approval workflow.

#### 6a. Risk Classification Tiers

**Default four-tier classification** (adapts EU AI Act structure with NIST AI RMF risk categorization):

| Tier | Classification | Criteria (any one criterion triggers classification) | Approval Path | Review Frequency |
|------|---------------|-----------------------------------------------------|---------------|-----------------|
| **TIER 4** | **Unacceptable Risk** | AI that manipulates persons through subliminal techniques; AI-based social scoring by public authorities; real-time biometric surveillance in public spaces (absent narrow exceptions); exploitation of vulnerable groups; AI-enabled violations of fundamental rights | **PROHIBITED** — Do not deploy. Document decision. | N/A |
| **TIER 3** | **High Risk** | Consequential decisions affecting employment, credit, insurance, housing, or education; medical diagnosis or treatment recommendations; critical infrastructure management; law enforcement AI; AI in recruitment, performance evaluation, or termination; AI subject to EU AI Act Annex III high-risk classification | **AGC approval required** — Full impact assessment + independent validation + human oversight + monitoring plan + legal review | Quarterly monitoring; annual re-assessment |
| **TIER 2** | **Limited Risk** | Customer-facing AI with significant interaction (chatbots, virtual assistants, recommendation engines); AI generating synthetic content; AI with moderate reputational or operational risk; AI processing sensitive personal data in non-consequential ways | **ARB approval required** — Abbreviated impact assessment + transparency disclosure + monitoring plan | Semi-annual monitoring; biannual re-assessment |
| **TIER 1** | **Minimal Risk** | Internal productivity tools with no consequential output; AI-assisted drafting where human reviews all output; AI for non-sensitive data analytics; widely used commercial AI tools with established track record | **AI Owner self-approval** — Registration in model inventory + basic documentation + opt-out where applicable | Annual review |

[JURISDICTION-SPECIFIC] Adapt tier criteria to applicable regulatory classification:
- **EU AI Act**: Tier 3 criteria must encompass all Annex III categories (use `legalcode-eu-ai-act-high-risk-compliance` for detailed Annex III screening)
- **Colorado SB 205**: "Consequential decisions" definition and required algorithmic impact assessments [VERIFY effective date and current text]
- **Financial services**: SR 11-7 "model risk" classification overlays on AI governance tiers
- **Healthcare**: FDA SaMD risk classification (Class I/II/III) cross-references for medical AI

#### 6b. Risk Classification Assessment Criteria

For each proposed AI use case, score these dimensions:

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Decision impact** | Advisory/informational; human reviews all output | Assists decisions with human override capability | Automated decisions with limited or no human review |
| **Population affected** | Internal team (<50 people) | Internal org-wide or limited external | External customers, applicants, or vulnerable groups |
| **Data sensitivity** | Non-personal, public data | Internal or pseudonymized personal data | Special-category, financial, health, biometric, or children's data |
| **Reversibility** | Decisions easily reversed; no lasting harm | Decisions reversible with effort; limited lasting impact | Decisions difficult to reverse; potential lasting harm |
| **Regulatory exposure** | No specific AI regulation applies | Sector regulatory guidance applies | Mandatory regulatory requirement applies |
| **Reputational risk** | Low public visibility | Some public visibility; isolated incident risk | High public visibility; systemic risk |

**Scoring thresholds** (adapt to risk tolerance preference from Step 2):

| Total Score | Default Classification | Conservative Org | Progressive Org |
|------------|----------------------|-----------------|----------------|
| 6 | Tier 1 | Tier 1 | Tier 1 |
| 7-9 | Tier 1–2 (ARB decides) | Tier 2 | Tier 1 |
| 10-12 | Tier 2 | Tier 2–3 (ARB decides) | Tier 2 |
| 13-15 | Tier 3 | Tier 3 | Tier 2–3 (ARB decides) |
| 16-18 | Tier 3 or Tier 4 | Tier 4 assessment | Tier 3 |

#### 6c. Prohibited AI Checklist (Tier 4 Screening)

Apply this checklist to every use case before classification. If any item is checked, classify as Tier 4:

- [ ] AI that deploys subliminal, manipulative, or deceptive techniques to influence behavior in harmful ways
- [ ] AI-based scoring of persons for general social/civic trustworthiness by public authorities
- [ ] Real-time remote biometric identification in publicly accessible spaces (outside narrow legal exceptions)
- [ ] AI inferences based on protected characteristics (race, religion, sex, national origin, disability) in prohibited decision contexts
- [ ] AI designed to exploit vulnerabilities (age, disability, socioeconomic status) to cause harm
- [ ] AI facial emotion recognition in workplace or educational settings without lawful basis [JURISDICTION-SPECIFIC: verify current status, especially EU AI Act prohibitions]
- [ ] Predictive policing AI targeting individuals based on profiling absent individual-level evidence [VERIFY applicable jurisdiction]
- [ ] Any AI use explicitly prohibited by applicable sector regulation

### Step 7: Design the Governance Policy Suite

Draft or outline the following governance documents. The scope and depth of each document depends on the Output Scope selected in Step 2.

#### Document 1: Enterprise AI Governance Policy

**Purpose**: Master governance document establishing organizational commitment, scope, principles, and accountability structure.

**Required sections:**
1. **Policy Statement** — Organization's commitment to responsible AI; alignment with values and legal obligations
2. **Scope** — Which AI systems, which business units, which jurisdictions are covered; exclusions
3. **AI Principles** — (minimum 6, adapted to organization): Fairness and non-discrimination; Transparency and explainability; Human oversight and control; Privacy and data governance; Safety and reliability; Accountability; [JURISDICTION-SPECIFIC: add local principles, e.g., EU Charter of Fundamental Rights alignment for EU entities]
4. **Governance Structure** — Reference to governance bodies from Step 5; decision authority matrix
5. **Risk Classification** — Reference to Tier 1–4 framework from Step 6; use case approval process
6. **Policy Hierarchy** — Relationship of this policy to subordinate policies (acceptable use, procurement, lifecycle, etc.)
7. **Enforcement and Consequences** — How violations are handled; disciplinary framework
8. **Review Cadence** — Annual review; trigger-based review (major incident, new regulation)
9. **Definitions** — AI system, generative AI, high-risk AI, AI owner, model, etc.

**⟁ CLARIFY** — "Should the AI principles be adapted to a specific existing ethical framework (e.g., EU Ethics Guidelines for Trustworthy AI 'ALTAI', OECD AI Principles, IEEE Ethically Aligned Design, or a proprietary company values framework)?"

#### Document 2: AI Acceptable Use Policy (AUP)

**Purpose**: Communicates to all employees what AI tools they may use, under what conditions, and with what safeguards.

**Required sections:**
1. **Approved AI Tools** — Categories of approved tools; approved tooling list (reference internal registry); approval process for new tools
2. **Prohibited Uses** — Explicit prohibitions: inputting confidential data into unvetted AI tools; using AI for protected-characteristic decisions without approval; using AI to circumvent internal controls; using AI outputs without human review for high-stakes decisions; generating misleading content attributed to humans; prohibited per Tier 4 checklist
3. **Data Handling Rules** — What data classes may be input to which AI tools; confidentiality obligations; prohibition on inputting regulated data (PHI, PII, trade secrets) into public AI services unless contractually authorized
4. **Disclosure Requirements** — When to disclose AI use to clients/customers/counterparties; labeling of AI-generated content
5. **Training Requirement** — Mandatory AI literacy training before using AI tools; completion tracking
6. **Reporting Obligation** — How to report AI-related concerns, bias observations, or incidents; whistleblower protection

[JURISDICTION-SPECIFIC] **EU AI Act Art. 4**: AI literacy obligation for all personnel using or overseeing AI systems (applies from 2 February 2025). Policy must reference the organization's AI literacy program.

#### Document 3: AI Risk Classification and Use Case Approval Procedure

**Purpose**: Operationalizes the risk classification framework (Step 6) as a procedural workflow.

**Use Case Intake Form template** (to be completed by AI Owner for every new use case):

```
AI USE CASE INTAKE FORM
=======================
Use Case Name: ___________________________________
Business Unit / Owner: ___________________________
Brief Description: ________________________________
AI System / Vendor: ______________________________
Data Inputs (describe): __________________________
Outputs / Actions taken: _________________________
Affected population: _____________________________
Date of first deployment (planned): _______________

TIER CLASSIFICATION WORKSHEET
------------------------------
Decision Impact (1-3): ___
Population Affected (1-3): ___
Data Sensitivity (1-3): ___
Reversibility (1-3): ___
Regulatory Exposure (1-3): ___
Reputational Risk (1-3): ___
TOTAL SCORE: ___ → PROPOSED TIER: ___

Tier 4 Prohibited Checklist (any checked = PROHIBITED): [ ] All clear / [ ] Item(s) flagged

REVIEWER SIGN-OFF
-----------------
AI Owner: _________________ Date: ___________
ARB Review (Tier 2-3): ____ Date: ___________
AGC Approval (Tier 3): _____ Date: ___________
```

**Approval workflow decision tree:**

```
New AI Use Case Identified
         |
         v
Step 1: Tier 4 Prohibited Checklist
  PROHIBITED item found → Do not deploy; document; escalate to Legal
  All clear →
         |
         v
Step 2: Tier Classification Score (1-18)
  Tier 4 (any prohib. criterion) → Prohibited
  Tier 3 (13-18 or Annex III) → Step 4
  Tier 2 (7-12) → Step 3
  Tier 1 (6) → Step 5
         |
         v
Step 3: ARB Review (Tier 2)
  Documentation: Impact assessment (abbreviated) + transparency disclosure plan
  Review time: 10 business days standard
  Decision: APPROVE / APPROVE WITH CONDITIONS / REJECT / ESCALATE TO AGC
         |
         v
Step 4: AGC Review (Tier 3)
  Documentation: Full impact assessment + independent validation report + human
  oversight design + regulatory review + monitoring plan
  Review time: 21 business days
  Decision: APPROVE / APPROVE WITH CONDITIONS / REJECT / REFER TO BOARD
         |
         v
Step 5: Registration in Model Inventory
  All approved use cases → add to model registry with: Tier, Owner, Approval date,
  Review date, Monitoring obligations
         |
         v
Step 6: Deployment with monitoring obligations active
```

#### Document 4: AI Procurement and Vendor Assessment Policy

**Purpose**: Governs the acquisition of AI tools, systems, and services from third parties.

**Pre-procurement AI assessment checklist:**

**Mandatory assessment questions (all vendors providing AI systems):**

| Category | Questions |
|----------|-----------|
| **System transparency** | Can the vendor explain how the AI system makes decisions? Is model documentation (model card, system card, technical sheet) available? What are the known limitations? |
| **Data practices** | What data is used to train the model? Does the vendor use customer data for training? Where is data stored and processed? What are the data retention terms? Can the organization opt out of data use for training? |
| **Bias and fairness** | Has the system been tested for bias across demographic groups? What were the results? Is a fairness assessment report available? Has the system been independently audited? |
| **Security and adversarial robustness** | What security testing has been conducted? Is the system certified against OWASP ML Top 10 or equivalent? What are the vendor's protections against prompt injection, data poisoning, and adversarial inputs? |
| **Regulatory compliance** | Is the vendor ISO 42001 certified? SOC 2 Type II? Does the vendor provide EU AI Act compliance declarations? What regulatory certifications apply? |
| **Incident response** | What are the vendor's SLAs for AI system failures? How does the vendor notify customers of incidents? What is the vendor's AI incident log/history? |
| **Contractual rights** | Does the contract include: right to audit AI system; model change notification rights; data deletion rights; SLAs for AI accuracy and uptime; indemnification for AI-caused harm; right to terminate for AI regulatory non-compliance? |
| **Supply chain risk** | Does the AI system use third-party models (LLM APIs, open-source models)? What oversight does the vendor apply to its AI supply chain? Are subprocessor AI use restrictions in place? |

**Risk-tiered procurement scrutiny:**
- **Tier 3 AI vendors**: Full assessment + independent vendor AI audit + legal review of AI provisions in contract + AGC sign-off
- **Tier 2 AI vendors**: Standard assessment + ARB review + procurement team legal review
- **Tier 1 AI vendors**: Abbreviated questionnaire (data practices + security + incident response) + AI Owner review

**Contract AI provisions checklist** (minimum required for Tier 2-3 AI vendor contracts):
- [ ] Scope of AI system and permitted use cases defined
- [ ] Data processing terms: what customer data is used; opt-out from training use
- [ ] Model change notification: provider must notify of material model updates ≥ 30 days before effective date
- [ ] Accuracy and performance SLAs with remediation obligations
- [ ] Audit rights: organization may audit AI system bias, accuracy, and security at least annually
- [ ] AI incident notification: provider must notify within [48-72 hours] of known AI system failure or bias event affecting organization
- [ ] Indemnification for AI-caused harm (proportionate; vendor accountability for system defects)
- [ ] Termination for regulatory non-compliance: right to terminate if AI system becomes non-compliant with applicable law
- [ ] Data deletion on termination: all training data derived from organization's data deleted within [30 days]
- [ ] Portability: data and outputs in portable format on termination; no vendor lock-in for core data

[JURISDICTION-SPECIFIC] **EU AI Act**: Deployers contracting with providers of high-risk AI systems must ensure the contract reflects Art. 25-26 obligations; providers must make technical documentation available; deployers must have meaningful human oversight capability. **US financial services**: OCC model risk management (SR 11-7) extends to vendor-provided models; banks must apply same validation standards to vendor AI as to internal models.

#### Document 5: AI Model Lifecycle Management Policy

**Purpose**: Governs each phase of the AI model lifecycle from conception to retirement.

**Lifecycle stages and governance gates:**

**STAGE 1 — Concept and Approval**
- Gate 1.1: Use case intake form submitted; Tier classification determined
- Gate 1.2: Approval obtained per Tier (Tier 1: AI Owner; Tier 2: ARB; Tier 3: AGC)
- Gate 1.3: AI Owner designated; AI system registered in model inventory
- Gate 1.4: Data governance review (are training data sources authorized, licensed, bias-checked?)
- Required documentation: Use Case Intake Form; Tier classification worksheet; approval record

**STAGE 2 — Development**
- Gate 2.1: Training data lineage documented (source, collection date, license, data quality assessment, demographic representation check)
- Gate 2.2: Model documentation (model card) prepared: purpose, architecture, training data, known limitations, performance benchmarks, intended use, out-of-scope uses
- Gate 2.3: Bias and fairness testing conducted across relevant demographic groups; results documented
- Gate 2.4: Security testing: input validation, output filtering, adversarial robustness
- Required documentation: Data inventory; model card draft; bias testing report; security assessment

**STAGE 3 — Validation (pre-deployment)**
- Gate 3.1: Independent validation by person/team other than developer
- Gate 3.2: Testing on representative production-like data (held-out test set)
- Gate 3.3: Performance benchmarking against defined acceptance criteria
- Gate 3.4: Human oversight mechanism verified and tested (ability to override AI output)
- Gate 3.5: Regulatory compliance review (Tier 3): applicable law, notification obligations, documentation
- Required documentation: Validation report; test results; acceptance criteria sign-off; legal review (Tier 3)

**STAGE 4 — Deployment**
- Gate 4.1: All validation gates cleared; approval documentation in place
- Gate 4.2: Monitoring infrastructure active (performance dashboard, drift detection, incident alerting)
- Gate 4.3: Rollback procedure documented and tested
- Gate 4.4: User/operator training completed; responsible AI disclosures in place (Tier 2-3)
- Gate 4.5: Model registry updated with deployment date, version, owner, monitoring schedule
- Required documentation: Deployment checklist; monitoring configuration; rollback plan; training records

**STAGE 5 — Monitoring and Maintenance**
- Monitoring metrics (adapt to use case):
  - **Performance drift**: Compare current accuracy/F1/AUC to baseline at regular cadence (Tier 3: weekly; Tier 2: monthly; Tier 1: quarterly)
  - **Bias drift**: Re-run fairness tests when input data distribution changes or at scheduled intervals
  - **Data quality**: Monitor input data for distribution shift, anomalies, or schema changes
  - **Usage pattern**: Monitor for use cases outside the approved scope
  - **Incident tracking**: Log all AI-related complaints, errors, near-misses; escalate per AI Incident Response Procedure
- Trigger-based re-validation: Mandatory re-validation upon any of: material model update; significant drift detected; major incident; change in regulatory requirements; business use case expansion
- Required documentation: Monitoring dashboard; drift reports; re-validation records; incident log

**STAGE 6 — Retirement**
- Gate 6.1: Impact assessment of decommissioning (dependent systems, downstream effects)
- Gate 6.2: Data handling: determine retention vs. deletion of training data per data retention schedule; document decision
- Gate 6.3: Archive model artifacts for regulatory audit trail
- Gate 6.4: Affected users/operators notified of decommissioning date (minimum 30 days notice for Tier 2-3)
- Gate 6.5: Model registry updated to RETIRED status; audit trail preserved
- Required documentation: Decommissioning decision record; data deletion/retention log; final performance report; archive record

#### Document 6: AI Incident Response Procedure

**Purpose**: Provides a playbook for detecting, assessing, responding to, and reporting AI-specific failures, harms, and incidents.

**AI Incident definition**: An AI incident is any unplanned event involving an AI system that results in, or has the potential to result in:
- Harm to individuals (physical, psychological, financial, reputational, or rights violation)
- Material AI system error affecting consequential decisions
- Bias or discriminatory outcome affecting protected groups
- Security compromise of AI system (adversarial attack, data poisoning, model extraction)
- Material degradation in AI system performance below defined thresholds
- Regulatory notification obligation trigger (EU AI Act Art. 73, sector regulations)

**AI Incident Severity Classification:**

| Severity | Definition (any single criterion triggers) | Response SLA | Escalation |
|----------|-------------------------------------------|-------------|------------|
| **AI-P1 (Critical)** | Confirmed harm to individuals; fundamental rights violation; EU AI Act Art. 73 serious incident trigger; safety-critical system failure; systemic bias affecting protected class | Immediate (within 2 hours): AI Owner → AGC + Legal + CISO | AGC + Legal + Board notification; EU AI Act Art. 73 notification to national MSA within [15 days for non-serious; 2 days for serious harm to health/safety] [VERIFY current Art. 73 timelines] |
| **AI-P2 (High)** | Potential harm under investigation; significant performance degradation in Tier 3 system; bias event under assessment; regulator inquiry received | Within 4 hours: AI Owner → ARB + Legal | AGC notification within 24 hours; regulatory notification assessment within 48 hours |
| **AI-P3 (Medium)** | Performance drift exceeding threshold; Tier 2 system anomaly; user complaint of potential bias; data quality issue affecting model inputs | Within 24 hours: AI Owner → ARB | Monitoring team alerted; re-validation scheduled; corrective action plan within 5 business days |
| **AI-P4 (Low)** | Minor performance degradation; Tier 1 system anomaly; user usability complaint with no harm | Within 5 business days: AI Owner | Log incident; monthly review; incorporate in annual governance report |

**AI Incident Response Steps:**

1. **Detect**: AI system triggers alert OR user/operator reports incident to AI Owner via [reporting channel]
2. **Log**: AI Owner records incident in AI incident log with: date/time, AI system, description, affected population estimate, initial severity assessment
3. **Contain** (AI-P1/P2): AI Owner may disable/limit AI system pending assessment; document containment action
4. **Classify**: ARB or AGC (depending on severity) confirms severity; determines if human override is needed; assesses harm scope
5. **Investigate**: Root cause analysis; data issue? Model drift? Adversarial attack? Coding error? Misuse?
6. **Notify regulators** (if triggered):
   - EU AI Act Art. 73: Notify national market surveillance authority of "serious incident" — within 15 calendar days for general serious incidents; within 2 calendar days for risk to health/safety or death [VERIFY current Art. 73 text and timing guidance]
   - Sector regulations: see [JURISDICTION-SPECIFIC] guidance
   - Data breach overlap: If AI incident involves personal data breach, invoke `legalcode-incident-response-plan-builder` for data breach notification in parallel
7. **Remediate**: Fix root cause; re-validate if required; deploy corrected version or retire system
8. **Review**: Post-incident review within 10 business days; lessons learned; governance policy update if needed

[JURISDICTION-SPECIFIC] **EU AI Act Art. 73 serious incident reporting** (as of August 2026 enforcement date): Providers of high-risk AI systems must notify national market surveillance authority. Commission draft guidance published August 2025 [VERIFY current guidance]. Deployers must report to providers; providers report to MSA. Keep own incident record regardless.

#### Document 7: AI Monitoring and Audit Program

**Purpose**: Defines the ongoing oversight, measurement, and audit activities that keep the AI governance framework effective.

**Monitoring cadences:**

| Activity | Tier 3 | Tier 2 | Tier 1 |
|----------|--------|--------|--------|
| Performance dashboard review | Weekly | Monthly | Quarterly |
| Bias/fairness spot-check | Monthly | Quarterly | Semi-annual |
| Drift detection automated scan | Continuous | Continuous | Monthly |
| Model registry review | Quarterly | Semi-annual | Annual |
| Vendor AI security review | Annual + trigger | Annual | Every 2 years |
| Use case scope review | Quarterly | Semi-annual | Annual |
| Regulatory update scan | Continuous (via `legalcode-regulatory-change-tracker`) | | |

**Annual AI Governance Audit:**

The AI Governance Committee shall conduct (or commission) an annual audit covering:

1. **Model Inventory Completeness**: Are all AI systems in scope registered? Are any shadow AI instances identified?
2. **Policy Compliance**: Are Tier classification and approval workflows being followed? Sample review of 10-20% of active use cases
3. **Incident Review**: Aggregate review of all AI incidents logged in the year; trend analysis; recurring issues
4. **Vendor AI Compliance**: Spot-check vendor AI assessment completeness; contract AI provisions present?
5. **Training Compliance**: Are all personnel with AI system responsibilities current on required AI training?
6. **Regulatory Currency**: Has the governance framework been updated to reflect new regulations effective in the audit period?
7. **ISO 42001 / NIST AI RMF Alignment Check**: Gap analysis against applicable framework(s); progress on prior-year recommendations

**Board reporting:**
- Annual AI Governance Report to Board/Board Risk Committee
- Contents: AI portfolio summary (active systems by tier); material incidents; regulatory developments; audit findings; maturity progress; upcoming regulatory deadlines; resource requests

#### Document 8: AI Training Data Governance Policy

**Purpose**: Governs the sourcing, quality, consent, and lifecycle management of data used to train, fine-tune, or evaluate AI systems.

**Required provisions:**

1. **Data sourcing authorization**: All training data must have documented authorization (license, consent, right to use for AI training). Prohibited sources: scraped data without license for AI use; synthetic data with undisclosed provenance; data subject to pending litigation or regulatory hold
2. **Data quality standards**: Minimum representativeness requirements; bias pre-assessment before training; data provenance documentation (source, collection date, geographic coverage, demographic coverage)
3. **Consent and GDPR compliance**: Personal data used in training must have valid legal basis (consent or legitimate interest assessment per `legalcode-legitimate-interest-assessment`); data subjects have right to object to AI training use [JURISDICTION-SPECIFIC: verify current interpretations, especially post-CJEU guidance on AI training consent]
4. **Data minimization**: Use minimum personal data necessary; prefer synthetic, anonymized, or non-personal data where feasible
5. **Retention and deletion**: Training datasets retained for audit trail purposes for the lifetime of the model plus [3 years] [VERIFY against applicable record retention requirements]; deleted securely on model retirement
6. **Documentation**: Maintain data sheet for every training dataset: name, source, license, volume, demographic coverage, bias assessment results, date of last review

### Step 8: Build Implementation Roadmap

Produce a phased implementation roadmap based on the organization's current maturity level and identified gaps.

#### Roadmap Design Principles

- **Backward-plan from regulatory deadlines**: Calculate milestones from applicable law enforcement dates
- **Risk-first sequencing**: CRITICAL and HIGH gaps before MEDIUM and LOW
- **Quick wins in Phase 1**: Implement governance structure and model inventory first — these enable everything else
- **Iterative documentation**: Draft policies before perfecting them; deploy with monitoring
- **Resource-realistic**: Name owners; estimate effort in person-days; flag dependencies

#### Phased Roadmap Template

**Phase 1 — Foundation (Months 1-3):**
| Milestone | Owner | Effort | Deliverable |
|---|---|---|---|
| Establish AI Governance Committee (AGC) | CEO/CTO | 2 days | AGC charter; first meeting scheduled |
| Designate AI Review Board (ARB) | CTO/AGC | 1 day | ARB terms of reference; member list |
| Build AI system inventory (all current AI) | ARB + BU leads | 5-10 days | Model registry v1 (all active AI use cases) |
| Draft Enterprise AI Governance Policy | Legal + AGC | 5 days | Policy draft v1; circulated for comment |
| Draft AI Acceptable Use Policy | HR + Legal + ARB | 3 days | AUP draft v1 |
| Conduct Tier 4 screening on all registered AI | ARB + Legal | 3 days | No Tier 4 found OR prohibited AI removed |
| Classify all registered AI by Tier 1-3 | ARB | 5 days | Model registry updated with tier classifications |
| Establish AI incident reporting channel | CISO + AI Owner | 1 day | Reporting channel live; employees notified |

**Phase 2 — Policy and Process (Months 4-6):**
| Milestone | Owner | Effort | Deliverable |
|---|---|---|---|
| Finalize and approve AI Governance Policy | AGC | 2 days | Approved policy; published to all staff |
| Finalize and approve AI AUP | HR + Legal | 2 days | Approved AUP; training deployed |
| Develop AI Risk Classification and Approval Procedure | ARB + Legal | 5 days | Approval workflow live; intake form deployed |
| Develop AI Model Lifecycle Management Policy | ARB + Engineering | 7 days | Lifecycle policy draft; validation gates defined |
| Draft AI Vendor Assessment Process | Legal + Procurement | 3 days | Vendor questionnaire; contract checklist |
| Deploy mandatory AI literacy training | HR + L&D | 5 days | Training module live; completion tracking |
| ISO 42001 / NIST AI RMF gap assessment | Compliance + ARB | 5 days | Gap report; prioritized remediation list |

**Phase 3 — Operationalization (Months 7-9):**
| Milestone | Owner | Effort | Deliverable |
|---|---|---|---|
| Apply lifecycle management to all Tier 3 AI systems | ARB + AI Owners | 10-20 days | Tier 3 systems fully lifecycle-managed |
| Apply lifecycle management to all Tier 2 AI systems | ARB + AI Owners | 10-20 days | Tier 2 systems in lifecycle management |
| Implement AI monitoring dashboards | Engineering + ARB | 5-10 days | Monitoring active for Tier 2-3 systems |
| Deploy AI Incident Response Procedure | CISO + Legal + ARB | 3 days | IR procedure approved; IR team trained |
| Conduct first AI governance tabletop exercise | AGC + ARB | 2 days | Tabletop report; gaps identified; updated |
| Apply vendor AI assessment to active vendors | Procurement + Legal | 5-10 days | Vendors assessed; contract gaps identified |

**Phase 4 — Maturity and Certification (Months 10-12+):**
| Milestone | Owner | Effort | Deliverable |
|---|---|---|---|
| First annual AI governance audit | Audit + Compliance | 5-10 days | Audit report; remediation items |
| Board AI governance report | AGC + CAIO | 2 days | Board report presented |
| ISO 42001 readiness assessment (if certification target) | Compliance + External Auditor | 10 days | Readiness report; pre-certification gap list |
| Update governance framework for regulatory developments | Legal + ARB | 2 days/quarter | Updated policies; regulatory calendar |
| Publish AI governance transparency statement (optional) | Communications + Legal | 3 days | Published; linked from website |

---

## ISO 42001 / NIST AI RMF Crosswalk

Map your governance framework elements to the applicable standard for audit readiness.

### ISO/IEC 42001:2023 Clause Alignment

| ISO 42001 Clause | Clause Title | Governance Framework Component |
|---|---|---|
| Clause 4 | Organizational Context | Step 2 (Org context); regulatory landscape (Step 3); stakeholder identification |
| Clause 5 | Leadership | Governance structure (Step 5); Enterprise AI Governance Policy (Doc 1) |
| Clause 6 | Planning | Risk classification (Step 6); gap analysis (Step 4); use case approval (Doc 3) |
| Clause 7 | Support | AI training program (Doc 2 AUP); resources; competence; documentation requirements |
| Clause 8 | Operation | Model lifecycle (Doc 5); vendor assessment (Doc 4); approval workflow (Doc 3) |
| Clause 9 | Performance Evaluation | Monitoring and audit program (Doc 7); performance metrics; management review |
| Clause 10 | Improvement | Post-incident review; corrective actions; continual improvement cycle |
| Annex A Controls | AIMS Controls | Controls mapped to: data governance, AI system impact assessment, risk treatment, responsible AI practices, third-party controls |

**ISO 42001 Statement of Applicability (SoA)**: For certification pathway, produce an SoA document listing each Annex A control, whether it applies, and if not, the justification for exclusion. Include reference to the governance document that implements each control.

### NIST AI RMF 1.0 Function Alignment

| AI RMF Function | Sub-categories | Governance Framework Mapping |
|---|---|---|
| **GOVERN** | GOVERN 1: Policies, processes, procedures established | Enterprise AI Policy (Doc 1); AUP (Doc 2); all policy documents |
| | GOVERN 2: Accountability assigned | RACI matrix (Step 5b); AI Owner designation |
| | GOVERN 3: Organizational teams aware of AI risk | AI literacy training (Doc 2); governance reporting |
| | GOVERN 4: Organizational teams are committed to AI risk management | AGC and ARB establishment; board oversight |
| | GOVERN 5: Policies/processes for TEVV (test, eval, verify, validate) | Lifecycle management Stage 3 (validation) |
| | GOVERN 6: AI risk management policies for third-party relationships | Vendor assessment (Doc 4) |
| **MAP** | MAP 1: Context established | Org context (Step 2); regulatory landscape (Step 3) |
| | MAP 2: Scientific understanding and risk categorization | Risk classification (Step 6); impact assessment |
| | MAP 3: AI risks, benefits, and impacts enumerated | Use case intake form (Doc 3); impact assessment |
| | MAP 4: Risks and benefits of impacts are mapped | Risk classification scoring; approval workflow |
| | MAP 5: Practices for communicating impacts | Transparency disclosures; AUP requirements |
| **MEASURE** | MEASURE 1: Methods identified to measure AI risks | Monitoring metrics (Doc 7); performance benchmarks |
| | MEASURE 2: AI risk metrics and monitoring | Monitoring program (Doc 7); drift detection |
| | MEASURE 3: Internal experts identified | ARB composition; skills inventory |
| | MEASURE 4: Feedback processes incorporated | Post-incident review; annual audit |
| **MANAGE** | MANAGE 1: Risks are prioritized | Risk tier classification; gap severity prioritization |
| | MANAGE 2: Strategies applied to maximize benefit/minimize harm | Lifecycle management; approval workflow gates |
| | MANAGE 3: Responses deployed | Incident response procedure (Doc 6) |
| | MANAGE 4: Residual risks communicated | Board reporting; governance transparency statement |

---

## Deep Topic Analysis

### AI Governance Anti-Patterns

#### Anti-Pattern 1: Shadow AI inventory
Deploying AI tools without registration in the model inventory. Governance frameworks are only as comprehensive as the AI they cover. Mitigation: Regular discovery scans; mandatory procurement routing for any AI spend; employee reporting obligation in AUP.

#### Anti-Pattern 2: Checkbox risk classification
Treating risk classification as a compliance form rather than a genuine risk assessment. AI Owners game the scoring to avoid Tier 3 review. Mitigation: ARB spot-audits of Tier 1 self-approvals; anonymous reporting channel; sample re-classification by ARB.

#### Anti-Pattern 3: Governance bodies without authority
Establishing AI committees that advise but do not decide. AI deployments bypass governance because there are no actual gating mechanisms. Mitigation: Define binding approval authority in governance structure; tie procurement/deployment infrastructure to approval workflow.

#### Anti-Pattern 4: Vendor AI outsourcing governance
Treating "the vendor handles it" as a sufficient governance position for third-party AI. Mitigation: Vendor assessment policy (Doc 4); contract AI provisions checklist; deployer remains accountable under EU AI Act Arts. 25-27 regardless of vendor contractual indemnities.

#### Anti-Pattern 5: Bias testing at launch only
Conducting fairness assessments once before deployment and never again. Models drift; training data biases can manifest over time; demographic shifts in user population create new fairness risks. Mitigation: Scheduled recurring bias monitoring cadence in Doc 7.

#### Anti-Pattern 6: AI incident under-reporting
AI system errors not reported because AI Owner fears remediation burden or reputational risk. Mitigation: Blameless incident culture; near-miss reporting incentivized; whistleblower protection in AUP; incident log reviewed quarterly (not just when problems escalate).

#### Anti-Pattern 7: Governance for AI, not the whole AI ecosystem
Governing the organization's own AI systems but ignoring AI embedded in third-party software (CRM AI features, ERP AI suggestions, cloud platform AI). Mitigation: Vendor AI assessment applies to embedded AI in SaaS; procurement policy requires disclosure of AI features.

#### Anti-Pattern 8: Static classification
Classifying a use case once at intake and never re-classifying despite material changes in scope, affected population, or regulatory environment. Mitigation: Re-classification trigger in lifecycle management Stage 5; trigger-based re-validation protocol.

#### Anti-Pattern 9: Training as compliance theater
Deploying AI literacy training that is perfunctory checkbox completion rather than building genuine capability. Mitigation: Role-differentiated training (AI Owners need deeper training than general employees); competency assessment post-training; content updated for AI tool evolution.

#### Anti-Pattern 10: AI governance separate from enterprise risk
Running AI governance as a separate program disconnected from existing ERM, third-party risk, and data governance programs. AI risk should integrate with enterprise risk management, not run parallel to it. Mitigation: NIST AI RMF explicitly aligns with COSO ERM; ISO 42001 uses ISO 31000 risk framework.

#### Anti-Pattern 11: Post-deployment oversight collapse
Robust pre-deployment governance but minimal monitoring after deployment. Lifecycle Stage 5 monitoring is typically the weakest link. Mitigation: Monitoring obligations tied to approval; documented monitoring dashboards; ARB quarterly review of monitoring metrics.

#### Anti-Pattern 12: Principles without procedures
Elaborate AI principles documents ("We believe in fairness and transparency") with no operational procedures that implement them. Principles must map to specific policies, workflows, and controls. Mitigation: Every principle in Doc 1 must cross-reference at least one operational procedure that implements it.

#### Anti-Pattern 13: Ignoring generative AI specifically
Treating generative AI (LLMs, image generators, code generators) under the same governance framework as narrow AI without additional controls. Generative AI has distinct risks: hallucination, copyright infringement of training data, prompt injection, confidential data leakage. Mitigation: AUP must specifically address generative AI; Tier 2 default minimum for any customer-facing generative AI; data input prohibition for confidential information into external LLM APIs.

#### Anti-Pattern 14: Documentation as the product
Building elaborate governance documentation that is never operationalized. Documentation is the artifact; operationalization is the goal. Mitigation: Implementation roadmap with specific owners and deadlines; governance effectiveness measured by behavior change, not document count.

#### Anti-Pattern 15: Governance without board engagement
AI governance that never reaches the board level, leaving directors unaware of material AI risks. Mitigation: Annual AI governance board report; board AI risk education; AI risk in board risk register; major incidents reported to board within [48 hours].

#### Anti-Pattern 16: Assuming one-size-fits-all model lifecycle
Applying the same validation rigor to a simple rules-based system and a deep neural network for credit decisions. Mitigation: Lifecycle management gates calibrated by Tier; Tier 3 requires independent validation; Tier 1 requires registration only.

#### Anti-Pattern 17: Privacy/AI governance silo
AI governance and privacy governance operated separately without coordination. Mitigation: DPO participates in AGC; DPIA and AI impact assessment conducted jointly for AI systems processing personal data; cross-reference in policies.

#### Anti-Pattern 18: Regulatory tunnel vision
Governing only for the current known regulations and missing emerging requirements. Mitigation: `legalcode-regulatory-change-tracker` integration in monitoring program (Doc 7); quarterly regulatory scan.

#### Anti-Pattern 19: Overlooking internal AI tools
Focusing governance on external-facing AI while neglecting internal tools (HR analytics, management reporting AI, internal recommendation systems). Internal AI affecting employment decisions is often Tier 3. Mitigation: AUP applies to all AI regardless of internal/external classification; HR AI systematically Tier 2-3.

#### Anti-Pattern 20: Treating AI governance as a one-time project
Building the governance framework as a finite project rather than an ongoing program. AI evolves; regulations change; the organization's AI portfolio changes. Mitigation: Permanent AGC with regular cadence; annual review of all governance components; annual board report.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates before delivering any governance framework output. If any gate fails, revise before delivery.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every regulatory or standards claim cites a specific instrument (ISO 42001 Clause X; EU AI Act Art. Y; NIST AI RMF GOVERN Z.1) | Add citation or mark "[UNVERIFIED]" |
| **Format** | All citations follow a recognizable format for the instrument | Fix format |
| **Currency** | Every cited provision checked against current version (ISO 42001 is December 2023; EU AI Act is Reg. 2024/1689; NIST AI RMF is January 2023) | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within the scope of AI governance; no unauthorized crosswalk into unrelated law | Remove or flag scope bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden | Add confidence qualifier |

### Self-Interrogation for Tier 3 and Tier 4 Classifications

For any AI system classified as Tier 3 (High Risk) or Tier 4 (Prohibited), apply this 3-pass review:

**Pass 1 — Classification Integrity**: Does the risk score follow logically from the objective facts about the AI system? Would a regulator applying EU AI Act Annex III or a model risk manager applying SR 11-7 reach the same classification? Are any criteria over- or under-weighted?

**Pass 2 — Completeness**: Have all relevant risk dimensions been assessed? Has the regulatory overlay for the applicable jurisdiction been applied? Is the human oversight design evaluated, not just the AI system itself?

**Pass 3 — Challenge**: What is the strongest argument for a lower tier classification? Under what circumstances might a reasonable risk professional accept a Tier 2 classification for this use case? Document the contra-argument and why Tier 3 is nonetheless warranted.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled in ISO 42001 / NIST AI RMF; regulatory text clear | State with confidence |
| **High** | 0.80-0.94 | Strong authority; minor interpretive questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good authority; emerging regulatory position; some uncertainty | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuine uncertainty; rapidly evolving regulatory area | Flag for professional review; present both sides |
| **Unlikely** | 0.0-0.39 | Weak basis; speculative | Do not assert; flag "[UNCERTAIN]"; recommend specialist engagement |

---

## Writing Standards

Governance documentation produced by this skill must meet these quality standards before delivery:

1. **Plain-language discipline**: Every policy sentence should be understandable by the people who must follow it, not just by lawyers. Avoid nominalizations ("the provision of training" → "train employees"). Active voice throughout.

2. **Precision over generality**: "AI Owners must register all AI systems within 30 days of approval" is better than "AI systems should be tracked." Governance documents that do not specify who, what, by when, and how are unenforceable.

3. **Testability**: Every governance requirement should be testable in an audit. "The organization has an AI governance committee" can be verified. "The organization takes AI governance seriously" cannot.

4. **Internal consistency**: Policy cross-references must be accurate. If Doc 3 says "escalate to AGC per Doc 1," Doc 1 must describe the AGC's authority. Verify all cross-references before delivery.

5. **Completeness markers**: Use [TBD] for elements that require organization-specific input (committee member names, specific tool lists, approved vendor lists). Do not leave unmarked gaps.

6. **Version control**: All governance documents should carry a version number, effective date, and next review date. Include in every document header.

**Quality gates before delivery:**
1. Can a non-compliance employee understand their obligations from reading the AUP?
2. Does every policy have a named owner and review date?
3. Does the RACI matrix have at least one "A" (Accountable) for every activity?
4. Are all Tier 4 prohibitions derived from explicit criteria, not just intuition?
5. Does the roadmap have enough specificity to be actionable (owner + deadline + deliverable for each milestone)?
6. Have all [JURISDICTION-SPECIFIC] markers been either filled with verified content or explicitly left for local counsel to complete?

---

## Glass Box Audit Trail

Every AI governance framework output MUST include a Glass Box audit section. This makes the design reasoning traceable and auditable.

```yaml
glass_box:
  skill_name: "legalcode-ai-governance-framework-builder"
  mode: "AI governance framework creation"
  topic: "Organizational AI governance framework"
  jurisdiction: "Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers"
  organization_type: "[Industry from Step 2]"
  ai_maturity_level: "[Level 1-5 from Step 2]"
  governance_model: "[Centralized / Federated / Hybrid from Step 2]"
  framework_alignment: "[ISO 42001 / NIST AI RMF / EU AI Act / Multiple]"
  output_scope: "[Full suite / Outline / Gap analysis / Specific components]"
  risk_tolerance: "[Conservative / Balanced / Progressive]"
  documents_produced:
    - doc1_ai_governance_policy: "[Produced / Outlined / Not in scope]"
    - doc2_acceptable_use_policy: "[Produced / Outlined / Not in scope]"
    - doc3_risk_classification_procedure: "[Produced / Outlined / Not in scope]"
    - doc4_vendor_assessment_policy: "[Produced / Outlined / Not in scope]"
    - doc5_model_lifecycle_policy: "[Produced / Outlined / Not in scope]"
    - doc6_incident_response_procedure: "[Produced / Outlined / Not in scope]"
    - doc7_monitoring_audit_program: "[Produced / Outlined / Not in scope]"
    - doc8_training_data_policy: "[Produced / Outlined / Not in scope]"
    - implementation_roadmap: "[Produced / Outlined / Not in scope]"
  regulatory_overlays_applied: "[List of jurisdiction-specific regulatory layers applied]"
  gaps_identified: "[Number of gaps found if gap analysis mode]"
  legalcode_mcp: "Connected / Not connected — [note]"
  research_reference_file: "[Path if created, or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Sector-specific AI regulations not fully assessed — requires local counsel review]"
    - "[Technical AI safety (adversarial robustness, formal verification) not covered]"
    - "[DPIA for personal data processing not covered — use legalcode-dpia-generator]"
    - "[Any other scope limitations]"
  reviewer: "AI-assisted — requires review by qualified legal professional and AI governance specialist"
```

---

## External Tool Integration

### With legalcode-mcp (preferred)

When legalcode-mcp is connected:
1. Search for current AI governance regulations in the organization's applicable jurisdictions
2. Search for ISO 42001 and NIST AI RMF current guidance and interpretations
3. Search for sector-specific AI governance requirements (financial, healthcare, government)
4. Save results to `/tmp/legalcode-ai-gov-research.md`
5. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

### With legalcode-regulatory-change-tracker

Invoke `legalcode-regulatory-change-tracker` to:
- Identify AI governance regulatory changes effective in the past 12 months
- Identify upcoming AI regulatory effective dates requiring policy updates
- Generate a compliance calendar for AI regulatory obligations

### Without legalcode-mcp

- Proceed with framework knowledge documented in this skill
- Mark all specific statutory citations, regulatory thresholds, and effective dates with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that organization's legal counsel verify all regulatory citations before relying on them

### Related Skill Integration Points

| Trigger | Invoke Skill |
|---------|-------------|
| AI system processes personal data → DPIA needed | `legalcode-dpia-generator` |
| Tier 3 AI system uses EU data → GDPR cross-border transfer assessment | `legalcode-cross-border-transfer-assessment` |
| Vendor AI contract review needed | `legalcode-contract-review` with AI governance playbook |
| EU AI Act Annex III classification needed | `legalcode-eu-ai-act-high-risk-compliance` |
| AI-related data breach occurs | `legalcode-incident-response-plan-builder` |
| AI regulatory change tracking needed | `legalcode-regulatory-change-tracker` |
| AI training data inventory and lineage mapping | `legalcode-data-mapping-workflow` |

---

## Output Format Template

Produce the governance framework in this structure:

```markdown
# AI Governance Framework — [Organization Name / Engagement Reference]

## Executive Summary

**Engagement scope**: [Full framework / Gap analysis / Specific components]
**Organization**: [Industry, size, jurisdiction]
**Primary frameworks aligned**: [ISO 42001 / NIST AI RMF / EU AI Act / Other]
**Current maturity level**: [Level 1-5]
**Key findings** (gap analysis mode): [N critical gaps / N high gaps / N medium gaps]
**Roadmap summary**: [3-4 sentence summary of recommended implementation path]

---

## Part 1: Governance Structure

### 1.1 AI Governance Committee
[Charter, membership, decision authority, meeting cadence]

### 1.2 AI Review Board
[Terms of reference, membership, approval authority]

### 1.3 RACI Matrix
[Full RACI table per Step 5b]

### 1.4 Reporting Lines Diagram
[Textual representation of reporting hierarchy]

---

## Part 2: AI Risk Classification Framework

### 2.1 Risk Tier Definitions
[Tier 1-4 definitions, criteria, approval paths — per Step 6]

### 2.2 Risk Scoring Worksheet
[Scoring table and threshold matrix]

### 2.3 Tier 4 Prohibited AI Checklist
[Full checklist]

---

## Part 3: Governance Policy Suite

### Document 1: Enterprise AI Governance Policy
[Full policy text or outline with [TBD] markers for org-specific content]

### Document 2: AI Acceptable Use Policy
[Full policy text or outline]

### Document 3: AI Risk Classification and Use Case Approval Procedure
[Full procedure with intake form template and decision tree]

### Document 4: AI Procurement and Vendor Assessment Policy
[Policy with assessment checklist and contract provisions checklist]

### Document 5: AI Model Lifecycle Management Policy
[Full lifecycle stages with governance gates]

### Document 6: AI Incident Response Procedure
[Full procedure with severity classification and response playbook]

### Document 7: AI Monitoring and Audit Program
[Monitoring cadences, annual audit scope, board reporting template]

### Document 8: AI Training Data Governance Policy
[Data sourcing rules, quality standards, documentation requirements]

---

## Part 4: Framework Alignment Assessment

### 4.1 ISO 42001 Alignment
[Clause-by-clause mapping; gap summary if gap analysis mode]

### 4.2 NIST AI RMF Alignment
[Function/sub-category mapping; gap summary if gap analysis mode]

### 4.3 Applicable Regulatory Overlay
[Jurisdiction-specific regulatory requirements applied]

---

## Part 5: Implementation Roadmap

### 5.1 Phase 1 — Foundation (Months 1-3)
[Milestone table with owners, effort, deliverables]

### 5.2 Phase 2 — Policy and Process (Months 4-6)
[Milestone table]

### 5.3 Phase 3 — Operationalization (Months 7-9)
[Milestone table]

### 5.4 Phase 4 — Maturity (Months 10-12+)
[Milestone table]

### 5.5 Regulatory Compliance Calendar
[Key AI regulatory deadlines applicable to the organization]

---

## Part 6: Quality and Audit Documentation

### 6.1 Gap Summary (if gap analysis mode)
[Gap table per Step 4]

### 6.2 Glass Box Audit Trail
[YAML block per Glass Box template]

---

*Review by qualified legal professional and AI governance specialist required before use.*
*Version [1.0] | Prepared [date] | Next review [date+1 year]*
```

---

## Localization Notes

When adapting this governance framework to a specific jurisdiction:

1. **EU**: Replace [JURISDICTION-SPECIFIC: EU] markers with verified EU AI Act, GDPR, and NIS2 obligations. Use `legalcode-eu-ai-act-high-risk-compliance` for Annex III high-risk classification detail. Verify transposition status of NIS2 in relevant member states.

2. **United States**: Add sector-specific overlays (HIPAA AI guidance, OCC/Fed guidance, SEC disclosure obligations, FTC AI guidance). Verify state AI law applicability (Colorado, Texas, Illinois, California) against org's jurisdictions. Update NIST AI RMF guidance per latest OMB memoranda.

3. **United Kingdom**: Add ICO AI Auditing Framework alignment; National AI Strategy references; AI Safety Institute guidance for advanced AI systems. [VERIFY current UK AI regulatory status post-2025 AI Regulation Bill developments]

4. **Canada**: Add ISED Voluntary Code of Conduct; Treasury Board AIA requirements for public sector; AIDA if enacted [VERIFY]. Quebec Law 25 AI-specific provisions apply to automated decisions.

5. **Australia**: Add National AI Framework voluntary commitments; OAIC Privacy Act AI guidance; ASIC/APRA AI governance expectations for regulated entities.

6. **Financial services (any jurisdiction)**: Basel BCBS Principles for Operational Resilience; applicable central bank/regulator AI guidance; model risk management standards (SR 11-7 or equivalent). Tier 3 classification is default for any AI in credit, underwriting, market risk, or fraud detection.

7. **Healthcare (any jurisdiction)**: FDA SaMD framework for medical AI; HIPAA OCR AI guidance for US; MDR/IVDR AI classification in EU; TGA SaMD for Australia. Medical AI is Tier 3 by default; Tier 4 for autonomous treatment decisions without human oversight.

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis building a comprehensive AI governance framework builder skill aligned with ISO/IEC 42001:2023, NIST AI Risk Management Framework 1.0, and the EU AI Act (Regulation 2024/1689). Research-backed by web search analysis of current AI governance best practices, ISO 42001 clause structure, NIST AI RMF functional alignment, enterprise AI governance frameworks (McKinsey, Deloitte, KPMG, EY, IBM, AWS), AI lifecycle governance literature, vendor assessment practices, and AI incident response requirements. Complementary to `legalcode-eu-ai-act-high-risk-compliance` (EU-specific assessment) and `legalcode-incident-response-plan-builder` (full cybersecurity IRP). Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for regional adaptation.
