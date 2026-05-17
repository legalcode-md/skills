---
name: legalcode-ai-provisions-reviewer
description: >
  Reviews contracts for AI-specific provisions: IP ownership of AI-generated outputs,
  AI usage restrictions and acceptable-use policies, training data rights (inputs/outputs
  as training material), liability allocation for AI errors and hallucinations, transparency
  and explainability requirements, algorithmic audit rights, bias monitoring and disparate
  impact obligations, human oversight and human-in-the-loop requirements, AI governance
  and responsible-AI clauses, and missing AI governance terms. Flags contracts that lack
  adequate AI safeguards, identifies one-sided AI risk transfers, generates redlines, and
  produces a confidence-scored, auditable AI governance analysis. Use when reviewing SaaS
  agreements, professional services contracts, technology licenses, vendor contracts,
  employment agreements, or any commercial contract where either party uses, deploys,
  procures, or integrates AI systems. Applies EU AI Act 2024/1689, GDPR Art. 22, NIST AI
  RMF, NYC Local Law 144 (AEDT), Colorado SB 205 (2024), US Copyright Office AI guidance
  (Jan 2025), and UK IP Office AI position. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers. Severity classification: GREEN / YELLOW / RED / [AI-GOVERNANCE-GAP].
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode AI Provisions Reviewer

> **Disclaimer**: This skill provides a framework for AI-assisted review of AI-related
> contract provisions. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use. The
> law governing AI is evolving rapidly — statutes, regulations, and guidance cited here
> may have been amended or superseded. Verify currency before relying on any provision.
> Statutory and case law references carry hallucination risk — verify against authoritative
> primary sources before relying on them.

---

## Purpose and Scope

This skill reviews existing contracts for AI-related provisions, identifies gaps in AI
governance coverage, classifies deviations by severity, generates actionable redlines, and
produces a confidence-scored, auditable analysis.

**Covers:**
- IP ownership of AI-generated outputs and AI-assisted work product
- AI usage restrictions, acceptable-use policies, and tool prohibitions
- Training data rights: using inputs, outputs, or data to train, fine-tune, or improve AI models
- Liability allocation for AI errors, hallucinations, and autonomous AI decisions
- Transparency, explainability, and algorithmic audit rights
- Bias monitoring, disparate impact obligations, and algorithmic accountability
- Human oversight requirements: human-in-the-loop, meaningful human control
- AI governance: responsible AI clauses, incident reporting, model cards, ethics by reference
- AI data protection overlays: GDPR Art. 22 automated decision-making, DPIA triggers
- Vendor AI supply chain: sub-processor AI use, model provider dependencies, deprecation risk
- Missing AI governance terms: flagging contracts that are silent on AI entirely

**Does not:**
- Draft new AI contracts (use a drafting-specific skill)
- Provide legal advice or replace qualified counsel
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Assess the underlying AI system for technical safety (a separate engineering and risk function)

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The contract's governing law clause determines
the applicable legal framework. This skill identifies the governing law early and adapts
the AI governance analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **EU**: EU AI Act 2024/1689 (in force 2 August 2024; prohibited practices 2 Feb 2025;
  GPAI obligations 2 Aug 2025; high-risk obligations 2 Aug 2026) + GDPR Art. 22 (automated
  decision-making) + Art. 35 DPIA requirements for high-risk AI processing [VERIFY currency]
- **UK**: No dedicated AI Act yet; UK AI regulation takes a principles-based approach via
  existing regulators (ICO, FCA, CMA); UK IP Office AI and IP consultation (2024); UK GDPR
  / DPA 2018 Art. 22 equivalent [VERIFY currency]
- **US — Federal**: NIST AI RMF (2023, voluntary); Executive Order 14110 (Oct 2023, partially
  revoked/modified 2025 — verify current status); US Copyright Office AI Copyright Study Parts
  1-3 (2024-2025); FTC Act §5 unfair or deceptive practices applied to AI [VERIFY currency]
- **US — State**: Colorado SB 205 (2024, effective 1 Feb 2026) — consequential AI decisions;
  Illinois AEDT / NYC Local Law 144 — automated employment decision tools, annual bias audits;
  California AB 2930 (status: [VERIFY current enactment status]) [VERIFY currency]
- **Japan**: Act on the Protection of Personal Information (APPI) 2022 amendments; Ministry
  of Economy, Trade and Industry AI governance guidelines [VERIFY currency]
- **China**: Provisions on the Administration of Generative AI Services (2023); Algorithmic
  Recommendation Provisions (2022) [VERIFY currency]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer changes the direction of the AI governance analysis
- Multiple valid approaches exist and the user's preference matters
- The contract's AI usage context is unclear (what AI is being used for)
- Risk tolerance or regulatory exposure level is needed to classify severity correctly

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

### Step 1: Accept the Contract

Accept the contract in any of these formats:
- **File**: PDF, DOCX, or other document format
- **URL**: Link to a contract in a CLM, cloud storage, or document system
- **Pasted text**: Contract text pasted directly into the conversation
- **Specific clause or section**: User may provide only the AI-related sections for targeted review

If no contract is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the AI provisions review, ask these questions:

1. **Which side are you on?**
   - Options: AI Vendor/Provider, Customer/Buyer/Deployer, Employer (AI used internally),
     Employee (reviewing AI-related employment terms), Partner, Other
   - *Why this matters*: The analysis reverses depending on which party bears the AI governance
     obligations and which party benefits from AI usage restrictions.

2. **What AI is involved in this contract?** (Select all that apply)
   - Options: Generative AI (LLMs, image/text generation), Predictive/Decision-making AI,
     Automated employment decisions (hiring, performance, termination), AI in professional
     services delivery, AI in regulated sectors (healthcare, finance, legal), General/unclear AI use
   - Allow multiple selections.
   - *Why this matters*: Generative AI triggers IP ownership and training data concerns;
     decision-making AI triggers transparency, bias, and human oversight requirements;
     regulated-sector AI triggers heightened compliance obligations.

3. **Regulatory exposure**: Which regulatory regimes apply?
   - Options: EU AI Act scope (EU market or EU-established counterparty), GDPR/UK GDPR
     (personal data processed), US employment AI laws (Colorado, NYC, Illinois), All of the
     above, Uncertain — help me assess, None obvious
   - Allow multiple.
   - *Why this matters*: Determines which mandatory compliance requirements are non-negotiable
     versus aspirational.

4. **What is the deal context?**
   - Free text. Prompt with examples: procurement of AI-enabled software, engaging a
     professional services firm that uses AI tools, deploying AI for internal HR decisions,
     AI-generated deliverables under a services contract, joint AI development.
   - *Why this matters*: Shapes which AI provision categories are most material for this deal.

5. **Does an AI addendum, schedule, or policy exist?**
   - Options: Yes (attach it), No, Unclear
   - *Why this matters*: Many counterparties now incorporate AI usage policies or addenda by
     reference. Reviewing only the main agreement may miss critical AI terms.

### Step 3: Identify Governing Law and Regulatory Scope

Read the contract's governing law clause and identify:
1. **Governing jurisdiction(s)** — note if multiple schedules reference different laws
2. **Applicable AI regulatory regime** — EU AI Act, US state laws, UK principles-based regime, etc.
3. **Data protection regime** — GDPR, UK GDPR, CCPA/CPRA, etc. (relevant to AI personal data processing)
4. **Sector-specific AI regulation** — financial services (FCA, SEC), healthcare (FDA, MDR), legal services

**⟁ CLARIFY** — If the contract is silent on governing law, flag it and ask the user which
jurisdiction to apply for the AI governance analysis.

### Step 4: Gather AI-Relevant Legal Authority

Use **legalcode-mcp** to gather current legal authority for the identified jurisdiction(s)
before analyzing AI provisions.

**Search for:**
- AI Act provisions applicable to the contract's AI use case (risk tier, obligations)
- Current GDPR/UK GDPR guidance on automated decision-making and AI data processing
- Applicable national/state AI laws (Colorado SB 205, NYC LL144, etc.)
- Copyright Office guidance on AI-generated works ownership
- Any regulatory guidance on AI in the relevant sector

Save results to `/tmp/legalcode-ai-provisions-authority.md`.

**If legalcode-mcp is not connected:**
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using general knowledge; flag that legal authority has not been independently verified

### Step 5: AI Provision Scan

Scan the entire contract — including recitals, schedules, annexes, and incorporated
policies — for any AI-related language. Search for:

**Explicit AI terms**: "artificial intelligence", "AI", "machine learning", "large language
model", "LLM", "generative AI", "automated decision", "algorithmic", "model", "neural
network", "ChatGPT", "Copilot", "Claude", or any named AI system.

**Implicit AI indicators**: "automated processing", "predictive analytics", "data-driven
decisions", "intelligent automation", "computer-generated", "system-generated outputs."

**⟁ CLARIFY** — If the contract is entirely silent on AI but the deal clearly involves AI
systems (e.g., the software being procured is AI-enabled), flag this as a potential
[AI-GOVERNANCE-GAP] and ask:
- "This contract appears silent on AI. Given the AI-enabled nature of this service, should
  I review what AI governance provisions are missing?"

### Step 6: AI Provision Analysis

Analyze each AI topic area using the **AI Provision Analysis Reference** section below.
For each area, assess: (a) whether the contract addresses it, (b) if addressed, how it
deviates from standard positions, and (c) if absent, whether the gap is material.

**⟁ CLARIFY** — For contracts with no AI-specific provisions at all, ask before classifying:
- "This contract has no AI-specific provisions. Given the deal context, should I assess
  only what is missing (gap analysis), or also analyze whether general IP/liability/data
  clauses adequately cover AI scenarios without amendment?"

### Step 7: Classify Deviations

Classify each AI governance finding using the severity system in **AI Governance Severity
Classification** below:
- **GREEN**: Adequate AI governance provision present
- **YELLOW**: Present but insufficient, one-sided, or below market standard — negotiate
- **RED**: Material AI governance risk, likely void/non-compliant provision, or creates
  unacceptable liability exposure — escalate
- **[AI-GOVERNANCE-GAP]**: Provision entirely absent where it should be present given the
  AI use case — must be added before execution

**⟁ CLARIFY** — For borderline YELLOW/RED classifications where the severity depends on the
organization's AI risk tolerance or regulatory exposure, present both interpretations and ask.

### Step 8: Generate Redlines

For each YELLOW and RED finding, generate a specific redline using the **Redline Format**
below. For each [AI-GOVERNANCE-GAP], provide draft language to insert.

**⟁ CLARIFY** — Before generating redlines:
- "I've found [N] AI governance issues. Should I generate redlines for all, or focus on
  Tier 1 (must-resolve) and Tier 2 (strong preference) items only?"

### Step 9: AI Governance Summary

Produce an overall AI governance assessment covering:
- **AI governance maturity score**: Proportion of applicable AI governance areas addressed
- **Top 3 AI risks**: Most critical issues with severity and recommended action
- **Regulatory compliance gaps**: Any non-negotiable regulatory requirements missing
- **Negotiation strategy**: Which AI provisions to lead with, what to concede

### Step 10: Quality Verification

Before delivering:
1. Run the 5 Citation Quality Gates silently — revise failures before delivery
2. For every RED or [AI-GOVERNANCE-GAP] item, run the 3-pass Self-Interrogation
3. Assign Confidence Scores to each material AI provision analysis
4. Verify all 12 AI provision areas have been assessed (present, absent, or N/A)
5. Generate the Glass Box Audit Trail and append to output

---

## AI Provision Analysis Reference

### 1. IP Ownership of AI-Generated Outputs

**Key elements to review:**
- Whether the contract addresses ownership of AI-generated works, outputs, or deliverables
- Which party retains IP rights in works created using AI tools
- Whether "work-for-hire" or assignment provisions contemplate AI-assisted creation
- Whether AI outputs are warranted as non-infringing or as original works
- Whether the AI system used is identified and whether its output may be subject to
  third-party rights (open-weight model licenses, training data copyright claims)

**Common issues:**
- Contract assigns all deliverables as "work-for-hire" or by assignment without addressing
  that AI-generated content may not qualify for copyright protection [JURISDICTION-SPECIFIC]
- Vendor retains broad background IP rights that could encompass AI-generated outputs
  produced specifically for the customer
- No representation or warranty as to the copyright status of AI-generated deliverables
- License grants to AI outputs are too narrow (e.g., limited to internal use only when
  commercial exploitation is the contract's purpose)
- "Human authorship" assumption in IP clauses that may not hold for AI-heavy workflows

**Standard positions:**
- Customer/deployer: Explicit assignment or exclusive license of all AI-generated work
  product; representation that deliverables do not infringe third-party rights
- AI vendor: AI outputs provided "as-is" for IP purposes; no warranty that AI outputs
  are copyrightable; ownership of underlying model and training data

**[JURISDICTION-SPECIFIC] Key variations:**
- **US**: US Copyright Office policy (January 2025 AI Copyright Study Part 2): prompts
  alone do not confer copyright; human-perceptible authorship must survive the AI process;
  AI-only outputs are not copyrightable. Work-for-hire categories in 17 U.S.C. §101 do
  not include AI-generated works. [VERIFY currency]
- **UK**: UK IP Office position (2024 consultation): exploring AI-generated works exception
  under CDPA 1988 s.9(3) (computer-generated works with no human author); outcome
  pending. [VERIFY currency]
- **EU**: EU AI Act does not directly address copyright. EU Copyright Directive 2019/790
  Art. 4 TDM exception and opt-out provisions relevant to training data. CJEU Cofemel
  originality standard (author's own intellectual creation) may exclude most AI outputs.
  [VERIFY currency]

---

### 2. AI Usage Restrictions and Acceptable-Use Policies

**Key elements to review:**
- Whether the contract restricts or prohibits the use of AI tools in performing services
- Whether specific AI tools or categories are named or prohibited
- Acceptable-use policies incorporated by reference (are they current and accessible?)
- Whether AI usage restrictions create professional liability exposure
- Whether AI tool restrictions apply to subcontractors and employees

**Common issues:**
- Blanket prohibition on AI use incorporated by reference to a policy not provided or
  that can be unilaterally updated by one party
- AI restrictions that would make the contract unperformable given the service provider's
  workflows (functionally equivalent to a prohibition on software tools)
- No carve-out for AI tools used internally (background infrastructure) vs. AI-generated
  client deliverables
- Restrictions that apply to humans but not to sub-processors' AI systems
- No definition of what constitutes "AI use" (ambiguous scope)

**Standard positions:**
- Customer/deployer: Right to approve AI tools used in service delivery; transparency
  about AI use in deliverables; prohibition on using proprietary data as training material
- Service provider: Ability to use market-standard AI tools as productivity aids; carve-out
  for AI tools not applied to customer-specific data; right to update tools on notice

---

### 3. Training Data Rights

**Key elements to review:**
- Whether the vendor can use customer inputs, outputs, or data to train, fine-tune,
  improve, or evaluate AI models
- Whether there is an opt-out mechanism for AI training
- Whether training data restrictions extend to affiliated entities, sub-processors,
  or model providers
- Whether the contract addresses use of customer data in "synthetic data" generation
- Whether restrictions apply to foundation model training vs. customer-specific fine-tuning

**Common issues:**
- Broad "product improvement" or "service improvement" license that implicitly permits
  AI training without explicit disclosure
- Opt-out buried in privacy settings or acceptable-use policy rather than in the contract
- Training restrictions in the main agreement superseded by the AI provider's sub-processor
  terms (which the customer never reviews)
- No distinction between aggregate/anonymized data use and customer-identifiable data use
  for training
- No prohibition on using customer data to train models deployed for competitors
- "Feedback" or "suggestions" clause that grants the vendor a perpetual, irrevocable,
  royalty-free license — effectively enabling training on any customer content

**Standard positions:**
- Customer: Explicit prohibition on using customer data (inputs, outputs, metadata) to
  train AI models without written consent; opt-in rather than opt-out; extends to all
  sub-processors and model providers
- Vendor: Aggregate, anonymized product improvement use permitted; customer-specific
  fine-tuning requires separate agreement and customer controls

**[JURISDICTION-SPECIFIC] Key variations:**
- **EU**: GDPR Art. 6 legal basis required for AI training on personal data; purpose
  limitation principle limits repurposing; EU AI Act Art. 10 data governance requirements
  for high-risk AI training datasets. [VERIFY currency]
- **US**: No federal training data restriction law; FTC Act §5 "unfair or deceptive
  practices" may apply to misleading training data policies; proposed FTC AI rule (status
  pending — [VERIFY currency])
- **Copyright dimension**: CJEU and UK courts are addressing TDM (text and data mining)
  opt-out rights for AI training. [VERIFY currency]

---

### 4. Liability for AI Errors and Hallucinations

**Key elements to review:**
- Whether liability for AI-generated errors (hallucinations, inaccuracies, outdated
  information) is addressed
- Whether AI error liability is capped at a lower level than other liability
- Whether disclaimers for AI outputs are broad enough to effectively eliminate liability
- Whether professional indemnity applies to AI-assisted professional advice
- Whether the contract allocates liability for decisions made in reliance on AI outputs

**Common issues:**
- Broad disclaimer for AI outputs ("results provided as-is, no warranty of accuracy")
  that eliminates the vendor's responsibility for foreseeable AI failures in high-stakes contexts
- No allocation of liability for consequential damages arising from AI hallucinations in
  downstream decisions (e.g., wrong medical, legal, or financial AI-generated advice)
- Limitation of liability cap applies globally without carving out AI-caused harm in
  regulated sectors
- Indemnification for IP infringement does not cover AI-generated content that copies
  training data (memorization risk)
- No representation that AI outputs have been subject to human review before delivery
- "Human oversight" representations in the contract that are contradicted by the actual
  service delivery model (human rubber-stamp without genuine review)

**Standard positions:**
- Customer: Vendor liable for AI errors in proportion to reliance foreseen at contract
  formation; professional indemnity covers AI-assisted professional services; AI error
  damages carved out of overall liability cap for regulated-sector use cases
- Vendor: Standard disclaimer for AI accuracy; cap applies globally; no liability for
  customer decisions made without following vendor's prescribed review process

**[JURISDICTION-SPECIFIC] Key variations:**
- **EU**: EU AI Act Art. 22 and Annex III high-risk AI systems require human oversight
  before consequential decisions; Product Liability Directive 2024/2853 (in force Nov 2024,
  transposition Dec 2026) extends product liability to AI systems and software. [VERIFY]
- **EU AI Act high-risk categories** (Annex III): Critical infrastructure, education,
  employment, essential services access, law enforcement, migration, administration of
  justice, democratic processes — heightened obligations apply. [VERIFY]
- **US**: No specific AI error liability statute; common law negligence and products
  liability frameworks being applied; FTC guidance on AI-driven consumer harm. [VERIFY]

---

### 5. Transparency and Explainability Requirements

**Key elements to review:**
- Whether the contract requires disclosure that AI is being used
- Whether the customer has the right to explanations of AI outputs or decisions
- Whether explainability requirements apply to automated decisions affecting individuals
- Whether the AI system's training data, model architecture, or decision logic can be
  audited or reviewed
- Whether AI-generated content must be labeled or disclosed to end users

**Common issues:**
- No disclosure obligation for AI use in service delivery (customer receives AI-generated
  deliverables without knowing)
- Explainability requirements limited to "meaningful information" without specifying what
  that means in practice
- Audit rights for AI systems structurally unenforceable (vendor claims model architecture
  is a trade secret)
- No requirement to disclose when AI system output has been presented without human review
- Contract requires explainability but service does not technically support it (XAI
  capability gap)
- No update obligation when AI model is changed, retrained, or replaced

**Standard positions:**
- Customer: Right to know AI is being used; right to explanation of AI outputs used in
  decisions affecting the customer or its users; annual AI system disclosure; right to
  object to AI-only decisions on significant matters
- Vendor: Transparency about AI use without disclosing proprietary model architecture;
  system-level explanations rather than per-decision mechanistic explanations

**[JURISDICTION-SPECIFIC] Key variations:**
- **EU (GDPR Art. 22)**: Right not to be subject to solely automated decisions producing
  significant legal or similarly significant effects; right to explanation and human review.
  [VERIFY]
- **EU AI Act Art. 13**: High-risk AI systems must provide transparency sufficient for
  deployers to use the system appropriately. [VERIFY]
- **EU AI Act Art. 50**: Transparency obligations for AI-generated content (deepfakes,
  chatbots must disclose they are AI). [VERIFY]
- **US — Illinois AEDT**: Annual bias audit disclosure for automated employment decisions.
  NYC Local Law 144: annual bias audit and public notice requirements for employers using
  AEDTs. [VERIFY currency]

---

### 6. Bias Monitoring and Disparate Impact Obligations

**Key elements to review:**
- Whether the contract requires the AI vendor to conduct bias audits or assessments
- Whether disparate impact or discriminatory outcomes from AI are addressed
- Whether bias testing results are disclosed to the customer
- Whether the customer has recourse for discriminatory AI outcomes
- Whether anti-discrimination representations extend to AI-driven decisions

**Common issues:**
- Anti-discrimination representations and warranties do not contemplate AI-driven
  discrimination (clause drafted for human decision-making only)
- No contractual basis for demanding bias audit results from AI vendor
- Vendor's bias audit conducted by an AI-provider-affiliated entity (conflict of interest)
- No remediation obligation if bias audit reveals discriminatory outcomes
- Contract assumes AI is a neutral tool; no allocation of liability for disparate impact
  caused by the vendor's AI system

**Standard positions:**
- Customer: Annual independent bias audit using methodology at least equivalent to NYC LL
  144 standard; bias audit results disclosed to customer; remediation plan required if
  audit reveals material disparate impact; vendor liable for regulatory fines resulting
  from undisclosed discriminatory AI outcomes
- Vendor: Bias audits conducted; results disclosed in aggregate or at system level;
  customer responsible for compliance with employment discrimination laws in their
  specific deployment

**[JURISDICTION-SPECIFIC] Key variations:**
- **US — NYC Local Law 144** (effective July 2023): Employers and employment agencies
  using AEDTs for NYC hiring/promotion decisions must conduct annual independent bias
  audits and publish results. [VERIFY currency]
- **US — Colorado SB 205** (effective 1 Feb 2026): Developers and deployers of high-risk
  AI in consequential decisions must implement risk management programs addressing
  algorithmic discrimination; annual impact assessment disclosure. [VERIFY currency]
- **US — Illinois**: Illinois Human Rights Act amended to cover AI-based employment
  decisions; state prohibits use of AI if it has disparate impact without justification.
  [VERIFY currency]
- **EU**: EU AI Act Annex III high-risk uses (employment, essential services, education)
  require bias testing and ongoing monitoring. [VERIFY]

---

### 7. Human Oversight and Human-in-the-Loop Requirements

**Key elements to review:**
- Whether the contract requires human review or approval of AI outputs before they are
  acted upon or delivered
- Whether human oversight obligations are specific and measurable or aspirational
- Whether the contract allocates liability differently based on whether human oversight
  was performed
- Whether the "human" in the oversight process has sufficient information to exercise
  genuine oversight (or is a rubber stamp)
- Whether human oversight requirements can be waived by the customer

**Common issues:**
- Human oversight provision is aspirational ("vendor will use reasonable efforts to ensure
  human review") rather than a binding obligation
- Human oversight requirement satisfied by a cursory review process that does not
  constitute genuine oversight
- No baseline qualification or independence requirements for the human reviewer
- Liability carve-out for AI errors conditioned on customer performing human oversight —
  effectively transferring risk to the customer for the vendor's AI failures
- No override or escalation mechanism when human reviewer disagrees with AI output

**Standard positions:**
- Customer: Human review required before any AI output is used in a consequential decision
  or delivered to an end user; human reviewer must have access to sufficient context to
  exercise genuine oversight; customer retains right to override AI output in all cases
- Vendor: Human oversight obligation on deployer/customer for consequential use cases;
  vendor provides tools and information to support oversight; vendor not liable for
  customer's failure to implement prescribed oversight process

**[JURISDICTION-SPECIFIC] Key variations:**
- **EU AI Act Art. 14**: Deployers of high-risk AI must ensure oversight by competent
  natural persons able to: understand the system's capabilities and limitations, monitor
  for anomalies, intervene and override, and not excessively rely on the system. [VERIFY]
- **EU AI Act Art. 22**: Deployers of high-risk AI must assign human oversight to persons
  with authority and competence. [VERIFY]
- **NIST AI RMF**: GOVERN function requires accountability for AI impacts; MANAGE function
  includes response and recovery from AI incidents. (Voluntary in US context) [VERIFY]

---

### 8. AI Governance: Responsible AI, Incident Reporting, and Model Cards

**Key elements to review:**
- Whether the vendor has a published Responsible AI policy incorporated into the contract
- Whether AI incident reporting obligations are defined (what constitutes an "AI incident,"
  reporting timeline, notification obligations)
- Whether system cards, model cards, or AI impact assessments are provided or disclosed
- Whether the vendor must maintain a log of significant AI model changes (retraining,
  architecture changes, significant performance degradation)
- Whether there are AI ethical standards or principles by reference

**Common issues:**
- Responsible AI policy incorporated by reference but vendor can unilaterally amend it
  without notice
- No definition of "AI incident" — in practice, this means vendor determines unilaterally
  what requires reporting
- Model cards or system documentation provided voluntarily with no contractual obligation
  to keep them updated or notify customer of material changes
- AI ethics principles stated aspirationally with no enforcement mechanism
- No right to audit compliance with stated Responsible AI commitments

**Standard positions:**
- Customer: Contractual incorporation of vendor's Responsible AI policy with material
  amendment notification rights; defined AI incident reporting (48-72 hours for material
  incidents); model card or equivalent provided and kept current; annual AI governance
  attestation from vendor
- Vendor: Right to update Responsible AI policy with reasonable notice; AI incident
  reporting scoped to incidents that materially affect service performance or customer data

---

### 9. Data Protection Overlays for AI Processing

**Key elements to review:**
- Whether the contract and DPA address AI-specific data processing risks
- Whether automated decision-making using personal data is covered by GDPR Art. 22
  or equivalent national provisions
- Whether a DPIA (Data Protection Impact Assessment) has been conducted for high-risk
  AI processing
- Whether AI-generated inferences, profiles, or scores derived from personal data are
  treated as personal data subject to data protection obligations
- Whether GDPR Art. 25 (privacy by design) standards are applied to AI system design

**Common issues:**
- DPA addresses data processing generally but omits AI-specific obligations (no mention of
  automated decision-making rights, no DPIA trigger for high-risk AI)
- AI-generated inferences (e.g., sentiment scores, credit risk predictions) not classified
  as personal data in the DPA — creates exposure under GDPR interpretation
- No restriction on using special category personal data (health, race, religion) to
  train or improve AI models
- DPIA obligation nominally on the customer without vendor cooperation obligations
- No right to object to automated profiling under GDPR Art. 21 built into the service

**Standard positions:**
- Customer: Vendor must support DPIA requirements; GDPR Art. 22 rights explicitly
  preserved; no automated decisions on special category data without explicit consent or
  legal basis; vendor provides privacy impact information for AI system components
- Vendor: Customer is controller and responsible for legal basis; vendor provides
  processing record (ROPA) information; will not process special category data for AI
  training without explicit agreement

**[JURISDICTION-SPECIFIC]: EU GDPR, UK GDPR, Brazil LGPD, Canada PIPEDA/provincial
privacy laws, and US state laws each have different automated decision-making rights and
DPIA-equivalent requirements. [VERIFY applicable regime]**

---

### 10. Vendor AI Supply Chain: Sub-Processors and Model Dependencies

**Key elements to review:**
- Whether the contract discloses the AI models and providers used in service delivery
- Whether sub-processor AI usage is subject to the same restrictions as the primary vendor
- Whether the customer has approval rights over material changes to the AI models used
- Whether model deprecation, end-of-life, or discontinuation creates a business continuity
  risk not addressed in the contract
- Whether the contract addresses lock-in risk from proprietary AI systems (data portability,
  model portability, migration assistance)

**Common issues:**
- AI vendor uses GPT-4, Claude, Gemini, or other third-party foundation models but the
  customer contract imposes training data restrictions only on the vendor (not flowing
  down to model providers)
- No sub-processor list or notification obligation for changes to AI model providers
- No continuity provision for AI model deprecation (what happens when the underlying
  model the service is built on is discontinued or significantly changed?)
- Customer data may be processed by the AI vendor's sub-processor under that sub-processor's
  terms — which permit training or secondary use not prohibited by the main contract
- Lock-in: AI-generated data, fine-tuned models, embeddings, or workflow configurations
  not portable on termination

**Standard positions:**
- Customer: Full disclosure of AI model providers used in service delivery; flow-down of
  training data restrictions to all sub-processors; notification (30 days) before material
  change to AI model used in service delivery; data portability on termination includes
  AI-generated artifacts
- Vendor: Sub-processor list maintained; material change notification provided; data
  portability for customer data; AI model selection at vendor's discretion with reasonable
  notice of changes

---

### 11. AI in Employment and HR Decisions

**Key elements to review:**
- Whether AI is used in any employment decisions covered by the contract (hiring, screening,
  performance assessment, compensation, termination)
- Whether AI employment decision obligations (bias audit, notice, explanation) are met
- Whether employees are informed that AI is being used in decisions about them
- Whether the employer/HR platform vendor has allocated regulatory compliance obligations

**Common issues:**
- SaaS HR platform uses AI for candidate screening or performance analytics without
  disclosing applicable bias audit obligations to the employer-customer
- Contract is silent on NYC Local Law 144 compliance obligations despite the customer's
  New York headcount
- No provision for individual employee rights (right to explanation, right to human review,
  right to opt out) in AI-assisted HR decisions
- ATS (Applicant Tracking System) AI features enabled by default; customer unaware of
  AEDT implications

**[JURISDICTION-SPECIFIC] Key variations:**
- **US — NYC Local Law 144** (effective July 2023): Annual bias audit; public notice on
  job posting that AEDT is used; notify NYC candidates/employees at least 10 business days
  before use; accommodation request right. [VERIFY currency]
- **US — Colorado SB 205** (effective 1 Feb 2026): Developer and deployer obligations for
  high-risk AI in consequential employment decisions; annual impact assessments; disclosure
  to individuals. [VERIFY currency]
- **US — Illinois ART Act** (2020): Employers using AI video interview analysis must notify
  applicants and obtain consent; cannot use AI interview data to discriminate on protected
  basis. [VERIFY currency]
- **EU AI Act Annex III**: Employment and worker management AI (recruitment, performance
  monitoring, task allocation) classified as high-risk. [VERIFY]

---

### 12. Missing AI Governance Terms (Gap Analysis)

When the contract is silent on AI, evaluate whether the absence creates material risk
given the deal context.

**Always material gaps (flag as [AI-GOVERNANCE-GAP]):**
- No IP ownership provision when AI-generated content is a core deliverable
- No training data restriction when personal data or trade secrets will be processed
- No bias audit obligation when AI is used in regulated employment or credit decisions
- No GDPR Art. 22 protection when AI is used to make automated decisions about individuals
- No liability allocation for AI errors when AI outputs are used in high-stakes decisions

**Context-dependent gaps (assess based on deal context):**
- No AI disclosure obligation (material if customer or their end users do not know AI is used)
- No model change notification (material if specific AI model performance was a procurement factor)
- No human oversight requirement (material if AI used for professional advice delivery)
- No AI incident reporting (material for enterprise, regulated-sector, or high-value deals)

---

## AI Governance Severity Classification

### GREEN — Adequate AI Governance

The contract appropriately addresses the AI governance risk area for the deal context.
Either the provision is market-standard and balanced, or the absence of a provision is
appropriate (e.g., no AI disclosure needed because AI is not used).

**Action**: Note as adequate. No negotiation needed.

### YELLOW — Insufficient or One-Sided AI Governance

The contract addresses the area but insufficiently — the provision is vague, one-sided,
can be unilaterally modified by one party, or falls below market standard for the deal
type without reaching an unacceptable risk level.

**Examples:**
- Training data opt-out exists but is buried in privacy settings rather than in the contract
- Bias audit obligation present but no disclosure of results to customer
- Human oversight required but no definition of what constitutes genuine oversight
- AI incident reporting timeline is 30 days (below market standard of 48-72 hours for material incidents)

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Material AI Governance Risk

The contract creates or ignores a material AI governance risk — likely to cause liability,
regulatory exposure, or unacceptable business harm. Requires senior counsel review or
deal escalation.

**Examples:**
- Vendor retains unlimited right to use customer data (including personal data) to train AI models
- No limitation of liability carve-out for AI errors in regulated-sector high-stakes decisions
- AI-generated professional deliverables warranted as original human work product
- Contract in scope of NYC Local Law 144 with no bias audit obligation
- GDPR Art. 22 automated decision-making rights not preserved for data subjects

**Action**: Explain specific risk with legal basis. Provide market-standard alternative
language. Estimate exposure. Recommend escalation path.

### [AI-GOVERNANCE-GAP] — Required Provision Absent

A provision that must be present given the AI use case and regulatory exposure is entirely
absent from the contract. Not a matter of negotiating better terms — the provision must
be added before execution.

**Examples:**
- Contract silent on IP ownership of AI-generated deliverables when AI content is the
  core service output
- No training data restriction despite sensitive personal data and trade secrets being
  processed through the vendor's AI system
- No bias audit provision for an AI system used in NYC-covered employment decisions
- No DPA when AI system processes personal data at scale

**Action**: Draft insert language. Flag as non-negotiable addition. Recommend obtaining
an AI-specific addendum or schedule.

---

## Redline Format

For each AI governance redline:

```
**AI Provision Area**: [Area number and name from Analysis Reference]
**Clause reference**: [Section or clause number in the contract]
**Current language**: "[Exact quote from contract, or 'ABSENT — no provision']"
**Issue**: [1-2 sentences describing the AI governance problem]
**Proposed redline**: "[Specific alternative language, ready to insert]"
**Rationale**: [Brief, professional rationale suitable for sharing with counterparty's counsel]
**Legal basis**: [Relevant statute, regulation, principle — or "General AI governance market practice"]
**Confidence**: [Confidence level and range from scoring framework]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

---

## Negotiation Priority Framework

### Tier 1 — Must Resolve Before Signature

AI governance issues where execution without resolution is unacceptable:
- Missing or fatally deficient training data restriction for personal data or trade secrets
- Missing IP ownership provision when AI-generated deliverables are the core subject matter
- Regulatory compliance gap: missing bias audit for NYC LL144-covered employment AI;
  missing GDPR Art. 22 protection for automated decisions affecting data subjects
- Missing liability allocation for AI errors in regulated-sector or high-stakes decisions
- Vendor retains unlimited right to use customer data for AI model training

### Tier 2 — Prioritize in Negotiation

AI governance issues that materially affect risk but have room to negotiate:
- AI incident reporting timeline and scope
- Bias audit disclosure — aggregate results vs. granular disclosure
- Human oversight requirement specificity
- Model change notification periods
- AI data portability on termination
- Responsible AI policy amendment notification rights

### Tier 3 — Concede Under Pressure

AI governance issues that improve the position but can be strategically conceded:
- Specific AI tool disclosure (vs. category-level disclosure)
- System card or model card update frequency
- Annual AI governance attestation format
- AI ethics principles and policy by reference (if core substantive obligations are secured)

**Strategy**: Lead with Tier 1. Use Tier 3 concessions to secure Tier 2 wins.
Never concede on Tier 1 without escalation and documented decision-maker sign-off.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, or established AI governance principle | Add citation or mark [VERIFY] |
| **Format** | All citations follow a consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited AI law/regulation checked for amendments, repeal, or implementation stage — AI regulation is changing rapidly | Flag [CHECK CURRENCY — AI law evolves fast] |
| **Domain** | Analysis stays within the contract's governing law scope — no AI regulatory assumptions from other jurisdictions bleeding in | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden — especially for unsettled AI copyright and liability questions | Add confidence qualifier |

### Self-Interrogation for RED and [AI-GOVERNANCE-GAP] Items

For any item classified RED or [AI-GOVERNANCE-GAP], apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited AI regulation or principle? Would a regulator or court in this jurisdiction actually
reach this conclusion? Is the cited provision currently in force (not in a future
implementation stage)? Is the EU AI Act risk tier classification accurate for this use case?

**Pass 2 — Completeness**: Have all relevant AI regulatory regimes been considered?
Are there AI-specific sector regulations (FDA for medical AI, FCA for financial services
AI) not yet addressed? Are there data protection dimensions (GDPR Art. 22, DPIA
obligation) that interact with the AI clause analysis?

**Pass 3 — Challenge**: What is the strongest argument that this AI governance gap or
provision is acceptable? Under what circumstances might a reasonable counterparty decline
to add this provision? Is there an alternative contractual mechanism (insurance, escrow,
audit right) that could mitigate the risk without requiring a new provision?

If any pass reveals a weakness, revise the analysis before delivery.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled AI law, clear in-force statute, no ambiguity | State with confidence |
| **High** | 0.80-0.94 | Strong authority with minor interpretation questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good arguments but AI law is developing rapidly; reasonable minds could differ | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., AI copyright ownership, liability for hallucinations in new use cases) | Flag for professional review; present both sides |
| **Unlikely** | 0.0-0.39 | Weak basis, speculative, or AI regulation not yet in force | Do not assert; flag [UNCERTAIN — AI law not yet settled] |

---

## Glass Box Audit Trail

Every AI provisions review MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: legalcode-ai-provisions-reviewer
  date_of_analysis: "[YYYY-MM-DD]"
  contract: "[Contract title or description]"
  contract_type: "[SaaS / Professional Services / License / Employment / Other]"
  user_side: "[Vendor / Customer / Employer / Employee / Other]"
  governing_law: "[Jurisdiction identified from contract or 'Not specified']"

  # AI use case context
  ai_use_case: "[Generative AI / Predictive AI / Employment AI / Professional Services AI / Other]"
  ai_systems_named: "[List of named AI systems in contract, or 'None named']"
  regulated_sector: "[Healthcare / Financial services / Employment / General commercial / Other]"

  # Regulatory scope
  eu_ai_act_scope: "[Yes — [risk tier] / No / Uncertain]"
  gdpr_art22_applicable: "[Yes / No / Not assessed]"
  us_employment_ai_law: "[NYC LL144 / Colorado SB 205 / Illinois / None / Not assessed]"
  dpia_triggered: "[Yes / No / Not assessed]"

  # AI provision coverage
  ai_provision_areas_assessed: "[N of 12]"
  provisions_present: "[N]"
  provisions_absent_material: "[N — list areas]"
  deviations_found: "GREEN: [N] / YELLOW: [N] / RED: [N] / AI-GOVERNANCE-GAP: [N]"
  ai_addendum_reviewed: "[Yes / No / Not applicable]"

  # Quality
  legalcode_mcp: "[Connected / Not connected — manual verification required]"
  authority_reference_file: "[/tmp/legalcode-ai-provisions-authority.md or 'Not created']"
  citations_verified: "[N verified] / [N marked VERIFY]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE — no RED or GAP items]"
  confidence_overall: "[HIGH / MEDIUM / LOW] — [rationale]"

  limitations:
    - "AI law is evolving rapidly — verify currency of all cited AI regulations before relying on them"
    - "EU AI Act implementation dates vary by obligation type — verify applicable dates for this use case"
    - "US AI regulation is largely voluntary (NIST AI RMF) or state-level — verify applicable state law"
    - "[Any deal-specific scope limitations or assumptions]"

  reviewer: "AI-assisted — requires qualified legal review before execution"
```

---

## Anti-Patterns

What NOT to do when reviewing AI provisions. These are AI governance-specific failures,
not generic contract review errors.

**IP and Ownership Anti-Patterns:**

1. **Treating AI outputs as automatically copyrightable**: Assuming that because a
   service delivers "creative" or "professional" content, that content enjoys copyright
   protection. The US Copyright Office (Jan 2025) and most major jurisdictions require
   human authorship. AI-generated works may be unprotected — a material IP ownership
   issue for contracts where the output IS the product.

2. **Applying work-for-hire doctrine to AI content**: Assuming that standard work-for-hire
   or assignment language captures AI-generated content. Work-for-hire applies to works
   created by human employees or in specific categories of commissioned works. A purely
   AI-generated deliverable may fall outside these categories entirely.

3. **Missing the training data copyright dimension**: Reviewing the AI output IP question
   but ignoring whether the AI system was trained on copyrightable content that may expose
   the vendor (and by indemnity, the customer) to infringement claims.

**Training Data Anti-Patterns:**

4. **Accepting "product improvement" at face value**: "Product improvement" and "service
   improvement" licenses are the standard mechanism by which AI vendors claim permission
   to train on customer data. Always treat these clauses as implicit training data grants
   and flag accordingly.

5. **Failing to flow restrictions down**: Training data restrictions in the main agreement
   that do not extend to the vendor's AI model sub-processors (OpenAI, Anthropic, Google,
   etc.) are materially incomplete. The sub-processor may independently permit training
   use that the main contract prohibits.

6. **Treating opt-out as equivalent to opt-in**: AI training opt-outs in settings menus
   are materially weaker than contractual opt-in requirements. Do not treat them as
   equivalent protections.

**Liability Anti-Patterns:**

7. **Missing the hallucination liability gap**: Standard limitation of liability analysis
   flags uncapped indemnities and absence of caps. It often misses the specific AI
   hallucination scenario: where the AI produces confidently wrong output, the customer
   relies on it without adequate human review, and harm results. The question of who bears
   this risk must be explicitly analyzed.

8. **Ignoring AI-specific product liability developments**: EU Product Liability Directive
   2024/2853 (effective November 2024, transposition December 2026) extends product
   liability to software and AI systems. A limitation of liability clause that predates this
   regime may not adequately account for it. [VERIFY jurisdiction applicability]

9. **Conflating technical AI limitations with contractual disclaimers**: "AI may produce
   inaccurate results" is a technical accuracy disclosure. It is not a legal liability
   shield. Assess whether the disclaimer constitutes a valid limitation under the governing
   law's reasonableness requirements (e.g., UCTA in England) or unconscionability doctrine.

**Regulatory Compliance Anti-Patterns:**

10. **Treating EU AI Act as uniformly applicable**: The EU AI Act has different obligation
    types, different implementation dates, and different obligations for providers vs.
    deployers. Stating that a contract "complies with the EU AI Act" without specifying
    which obligations, for which party, at which implementation stage, is meaningless.

11. **Ignoring the US state-level patchwork**: US AI regulation is state-law-driven
    (Colorado, NYC, Illinois, and more). A US contract that does not engage with applicable
    state AI laws because "there is no federal AI law" has material compliance gaps.

12. **Missing the employment AI trigger**: Contracts for SaaS HR tools, ATS systems,
    or performance management platforms often contain employment AI functionality. Standard
    contract review may miss NYC Local Law 144 or Colorado SB 205 obligations because the
    reviewer is treating it as a general technology contract.

**Governance and Process Anti-Patterns:**

13. **Accepting aspirational responsible AI language as binding**: "We are committed to
    responsible AI" is not a contractual obligation. Only specific, measurable, and
    enforceable AI governance commitments (incident reporting timelines, audit rights,
    bias audit obligations) provide actual contractual protection.

14. **Failing to assess AI policy incorporation-by-reference risk**: If AI governance
    obligations are incorporated by reference to a vendor's AI policy or code of conduct,
    the vendor can unilaterally amend those obligations without contract amendment. Flag
    every incorporation-by-reference and assess whether the customer needs amendment
    notification rights or a consent requirement.

15. **Treating AI contract review as a one-time event**: AI law is evolving rapidly. A
    contract signed in 2024 may need AI governance provisions that did not exist as legal
    requirements at signing but become mandatory in 2025-2026 (EU AI Act phased
    implementation, Colorado SB 205 effective date). Consider whether the contract includes
    a mechanism to update AI provisions as the law changes — or at minimum, flag the
    temporal risk.

16. **Reviewing only explicit AI provisions**: Many AI governance risks arise from general
    contract provisions that were not drafted with AI in mind. The IP assignment clause,
    data processing restrictions, indemnification scope, and limitation of liability cap
    all have AI implications. Always assess general provisions for AI governance adequacy.

17. **Ignoring the AI sub-processor cascade**: The vendor's AI capability is often built
    on a stack of sub-processors — cloud, model provider, infrastructure. Standard
    sub-processor analysis checks data protection flow-down. AI governance review must
    also check training data restrictions, IP ownership, and model-change notification
    flow-down.

---

## Writing Standards

Apply plain-language discipline to all AI provisions review output:

1. **Specify the AI use case**: Never write "AI is used here." Always name the use case:
   "The vendor uses a large language model to generate the legal summaries that are the
   primary deliverable under this contract." Specificity determines severity.

2. **Distinguish law from aspiration**: AI governance includes both binding legal
   requirements (EU AI Act, NYC LL144, GDPR Art. 22) and best-practice guidance (NIST AI
   RMF, ISO 42001). Label each clearly — "required by [regulation]" vs. "consistent with
   AI governance best practice."

3. **Qualify unsettled AI law explicitly**: Many AI governance questions are legally
   unsettled (AI copyright ownership, AI product liability scope, hallucination liability).
   State the uncertainty explicitly: "The law on this point is unsettled. Current US
   Copyright Office guidance suggests X, but this interpretation is not confirmed by
   courts." Never present AI law uncertainty as settled.

4. **Date-stamp implementation milestones**: EU AI Act obligations apply at different
   dates for different risk tiers. Always specify: "This obligation takes effect [date]
   under EU AI Act Art. [X]." Do not state "the EU AI Act requires" without specifying
   the applicable implementation date.

5. **Propose specific redline language**: Vague AI governance redlines ("add language
   about training data") do not move negotiations. Every redline must be specific,
   ready-to-insert contract language.

6. **Label confidence levels on AI law analysis**: Use the confidence scoring framework
   for every AI law claim. "The EU AI Act classifies this as a high-risk AI system
   (High confidence, 0.85)" is more useful than an unqualified assertion.

7. **Active voice for all issue descriptions**: "The contract permits the vendor to use
   customer data for AI training" not "AI training use of customer data is permitted by the
   contract." Name the actor. Name the action.

8. **Distinguish contract-level from operational-level**: Some AI governance requirements
   (bias monitoring, incident response procedures, model documentation) may be operational
   matters implemented outside the contract. Distinguish between what the contract must
   say and what the deployment process must do — both are important, but only one is a
   contract review matter.

---

## External Tool Integration

This skill integrates with **legalcode-mcp** for AI law and regulatory research.

**With legalcode-mcp connected (preferred):**
- Search for current EU AI Act implementation status and guidance for the applicable
  risk tier
- Verify current text of GDPR Art. 22 and applicable supervisory authority guidance on
  automated decision-making
- Search for current status of applicable US state AI laws (Colorado SB 205, NYC LL144,
  Illinois, California)
- Verify US Copyright Office AI guidance publication status and key holdings
- Search for sector-specific AI regulation if the deal is in healthcare, financial
  services, or other regulated sectors
- Save results to `/tmp/legalcode-ai-provisions-authority.md`
- Mark all legalcode-mcp citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all AI regulatory citations with [VERIFY] and [CHECK CURRENCY — AI law evolves fast]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using general AI governance knowledge; focus enhancement on structural quality,
  workflow completeness, and AI governance gap identification
- Remind the user to verify the regulatory citation currency before relying on the analysis

---

## Output Format Template

Structure every AI provisions review as follows:

---

# AI Provisions Review — [Contract Name or Description]

**Date**: [YYYY-MM-DD]
**Reviewer Perspective**: [Vendor / Customer / Employer / Employee / Other]
**Contract Type**: [SaaS / Professional Services / License / Employment / Other]
**Governing Law**: [Jurisdiction or "Not specified — assumed [X]"]
**AI Use Case**: [Summary of AI use in this contract]
**Regulatory Scope**: [EU AI Act (tier: [X]) / GDPR Art. 22 / NYC LL144 / Colorado SB 205 / Other / None identified]
**AI Addendum**: [Reviewed / Not provided / Not applicable]
**AI Provision Areas Assessed**: [N of 12]

---

## AI Governance Risk Summary

**Overall AI Governance Rating**: [STRONG / ADEQUATE / WEAK / INADEQUATE]
**Critical Issues**: [N RED + [AI-GOVERNANCE-GAP] items]
**Issue Breakdown**: GREEN: [N] | YELLOW: [N] | RED: [N] | [AI-GOVERNANCE-GAP]: [N]
**Immediate Action Required**: [Yes — [specific reason] / No]

**Top 3 AI Governance Issues**:
1. [Most critical issue — severity — brief description]
2. [Second issue — severity — brief description]
3. [Third issue — severity — brief description]

---

## AI Provision Analysis

### Area 1: IP Ownership of AI Outputs — [GREEN / YELLOW / RED / AI-GOVERNANCE-GAP] | Confidence: [Level]

**Status**: [Addressed / Partially addressed / Absent]
**Current provision**: "[Quote from contract or 'No provision found']"
**Issue**: [Description of the AI governance problem]
**Legal basis**: [Statute or market standard — with [VERIFY] if needed]
**Recommended redline / Insert**: > [Specific language]
**Fallback**: > [Alternative position]
**Priority**: [Tier 1 / 2 / 3]

[Repeat for each of the 12 AI provision areas assessed]

---

## Regulatory Compliance Matrix

| Regulation | Applicable? | Clause Present? | Gap | Classification |
|-----------|------------|----------------|-----|----------------|
| EU AI Act (high-risk) | [Yes/No/Uncertain] | [Yes/No/Partial] | [Description] | [GREEN/YELLOW/RED/GAP] |
| GDPR Art. 22 | [Yes/No/Uncertain] | [Yes/No/Partial] | [Description] | [GREEN/YELLOW/RED/GAP] |
| NYC Local Law 144 | [Yes/No/Uncertain] | [Yes/No/Partial] | [Description] | [GREEN/YELLOW/RED/GAP] |
| Colorado SB 205 | [Yes/No/Uncertain] | [Yes/No/Partial] | [Description] | [GREEN/YELLOW/RED/GAP] |
| US Copyright Office AI guidance | [Yes/No/Uncertain] | [Yes/No/Partial] | [Description] | [GREEN/YELLOW/RED/GAP] |
| [Sector-specific AI regulation] | [Yes/No/Uncertain] | [Yes/No/Partial] | [Description] | [GREEN/YELLOW/RED/GAP] |

---

## AI Governance Negotiation Strategy

**Tier 1 — Must Resolve Before Signature:**
- [Issue 1 with brief justification]
- [Issue 2]

**Tier 2 — Prioritize in Negotiation:**
- [Issue 1]
- [Issue 2]

**Tier 3 — Concede Under Pressure:**
- [Issue 1]

**Trade-link opportunities:**
- [Concede X to secure Y]

**Recommended AI addendum/schedule**: [Yes — suggested scope / Not necessary / Consider for renewal]

---

## Glass Box Audit Trail

```yaml
glass_box:
  [YAML template populated with actual analysis values]
```

---

## Localization Notes

[Jurisdiction-specific notes on AI regulation applicable to this contract's governing law]

---

## Next Steps

- [ ] [Action item 1 — responsible party — deadline]
- [ ] Obtain AI addendum or schedule if not already in place
- [ ] Verify EU AI Act risk tier with in-house AI/regulatory counsel if EU AI Act in scope
- [ ] Verify current status of US state AI law compliance obligations if US employment AI used
- [ ] Schedule AI governance review at next contract renewal

---

## Localization Notes

**EU / EEA contracts**: EU AI Act 2024/1689 phased implementation requires tracking which
obligations are in force. Prohibited practices (Art. 5) apply from 2 February 2025. GPAI
model obligations (Art. 51-55) from 2 August 2025. High-risk AI system obligations (Annex
III) from 2 August 2026. General-purpose AI obligations from 2 August 2026. GDPR Art. 22
applies now for automated decisions on individuals. [VERIFY current dates]

**UK contracts**: No dedicated UK AI Act yet. Principles-based approach via existing sector
regulators (ICO for data protection, FCA for financial services, CMA for competition). UK
IP Office AI consultation (2024) outcomes — verify current status. UK GDPR / DPA 2018
apply to automated decision-making. [VERIFY currency]

**US contracts**: Heavily state-law-dependent. NYC Local Law 144 applies to AEDTs used
for NYC hiring/promotion. Colorado SB 205 effective 1 February 2026. Illinois ART Act
(2020) for AI video interviews. California AI law landscape developing — verify current
status. No comprehensive federal AI law — NIST AI RMF is voluntary. [VERIFY currency]

**APAC contracts**: Japan has updated APPI guidelines for AI; Ministry of Economy AI
governance guidelines. China: Generative AI Provisions (2023) and Algorithmic
Recommendation Provisions (2022) impose transparency and registration obligations. Singapore:
Model AI Governance Framework (2019, 2020 update). [VERIFY jurisdiction-specific requirements]

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis. Legal research foundation:
EU AI Act 2024/1689 text and implementation timeline; US Copyright Office AI Copyright
Study Parts 1-3 (2024-2025); GDPR Arts. 22/25/35; NYC Local Law 144; Colorado SB 205;
Illinois ART Act; NIST AI RMF (2023); EU Product Liability Directive 2024/2853; UK IP
Office AI consultation materials; NIST AI 600-1 (Adversarial Machine Learning); market
practice research on AI contract addenda (2024-2026). Structural quality pattern: adapted
from legalcode-contract-review and legalcode-technology-license-review gold standard
frameworks. All statutory and regulatory citations carry [VERIFY] markers due to rapid
evolution of AI law.
