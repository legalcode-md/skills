---
name: legalcode-data-processing-agreement-drafter
description: >
  Draft Data Processing Agreements (DPAs) from scratch for controller-to-processor,
  controller-to-controller (joint), and processor-to-sub-processor relationships.
  Produces GDPR Article 28-compliant, UK GDPR, CCPA/CPRA service provider, Brazil LGPD,
  and India DPDP Act-aligned DPA clauses and full agreements with jurisdiction-specific
  annexes. Covers subject matter and duration, processing instructions and scope
  limitations, data categories and data subject types, controller/processor obligations,
  sub-processor management and notification mechanisms, technical and organizational
  security measures (TOMs), data breach notification SLAs, data subject rights
  assistance, DPIA and prior consultation support, international data transfer
  mechanisms (EU SCCs 2021, UK IDTA, adequacy decisions, BCRs), audit and inspection
  rights, data return and deletion on termination, and liability allocation.
  Includes EU, UK, Brazil LGPD, and India DPDP annexes. Use when creating a new DPA
  from scratch, generating a DPA template for a vendor program, building sub-processor
  flow-down agreements, adding a DPA addendum to a master services agreement, drafting
  multi-jurisdiction DPAs for SaaS platforms, or designing a DPA program across
  multiple processing relationships and regimes. Supports both controller-side and
  processor-side drafting with dual-perspective clause options and negotiation
  guidance. Jurisdiction-agnostic baseline with multi-regime modular annexes.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode DPA Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of Data Processing
> Agreements. It does not constitute legal advice. All outputs should be reviewed by a qualified
> legal professional or Data Protection Officer licensed or operating in the relevant jurisdiction
> before execution. Privacy laws and regulatory guidance evolve rapidly — verify current
> applicability before relying on any requirement, deadline, or mechanism described here. The UK
> Data (Use and Access) Act 2025, CPPA regulatory updates, ANPD resolutions, and DPDP Act rules
> are subject to phased implementation; verify the current status before execution. Statutory and
> regulatory references cited from training data carry hallucination risk — verify against
> authoritative sources before relying on them. Mark any unverified citation with **[VERIFY]**.

---

## Purpose and Scope

This skill drafts Data Processing Agreements and data processing addenda from scratch or by
adapting existing templates. It covers all mandatory GDPR Article 28 clause categories, generates
jurisdiction-specific annexes for UK, California, Brazil, and India, and produces dual-perspective
clause language for both controller-side and processor-side drafting.

**Covers:**
- Drafting complete DPAs from scratch for any controller/processor relationship
- Adapting or supplementing existing DPA templates to meet current regulatory requirements
- Controller-to-processor DPAs (GDPR Art. 28 / UK GDPR / CCPA service provider / LGPD operator)
- Controller-to-controller arrangements (GDPR Art. 26 joint controller agreements)
- Processor-to-sub-processor flow-down DPAs (cascading obligations downstream)
- Multi-regime modular output: GDPR base DPA + UK Addendum + California Exhibit + Brazil Annex + India Annex
- Technical and Organizational Measures (TOM) specification in Annex form
- Sub-processor authorization frameworks (specific and general authorization mechanisms)
- International transfer mechanism selection and clause generation (EU SCCs 2021, UK IDTA, adequacy, BCRs)
- Dual-perspective drafting: controller-favorable, processor-favorable, and market-standard compromise positions
- Quality-verified output with Glass Box audit trail and confidence scoring

**Does not:**
- Review or negotiate existing DPAs (see `legalcode-dpa-review-and-negotiation`)
- Provide legal advice or replace qualified DPO or counsel review
- Cover all global privacy regimes — primary coverage is EU/UK/US(CA)/BR/IN; for PDPA Singapore,
  APPI Japan, Australian Privacy Act 1988, and PIPEDA Canada, see jurisdiction-specific skills
- Conduct Data Protection Impact Assessments (see `legalcode-dpia-generator`)
- Assess breach notification obligations post-incident (see `legalcode-breach-severity-assessment`)
- Assess cross-border transfer adequacy (see `legalcode-cross-border-transfer-assessment`)
- Guarantee compliance or regulatory approval

**Related skills:**
- `legalcode-dpa-review-and-negotiation` — review and negotiate an existing DPA clause-by-clause
- `legalcode-cross-border-transfer-assessment` — deep transfer mechanism analysis
- `legalcode-dpia-generator` — generate Data Protection Impact Assessments
- `legalcode-breach-severity-assessment` — assess breach notification obligations
- `legalcode-dsar-workflow-builder` — build data subject request response workflows
- `legalcode-saas-agreement-drafter` — draft full SaaS MSAs including DPA addendum coordination

---

## Jurisdiction and Governing Law

This skill drafts DPAs applicable under five primary data processing regimes. A single DPA may
need to satisfy multiple regimes simultaneously (a SaaS vendor processing EU, UK, US, and Brazilian
personal data needs all four addenda). The skill identifies applicable regimes in Step 2 and
generates modular output accordingly.

### Regime Overview

| Regime | Primary Instrument | Mandatory DPA? | Key Authority | Transfer Mechanism |
|--------|--------------------|---------------|---------------|-------------------|
| **EU GDPR** | Regulation (EU) 2016/679, Art. 28 | Yes — controller/processor | EDPB | EU SCCs 2021, adequacy decisions, BCRs |
| **UK GDPR** | UK GDPR + DPA 2018 + Data (Use and Access) Act 2025 | Yes — mirrors EU GDPR Art. 28 | ICO | UK IDTA, UK Addendum to EU SCCs, adequacy |
| **CCPA/CPRA** | Cal. Civil Code §1798.100 et seq.; CPPA Regs § 7050 et seq. | Yes — service provider contracts | CPPA | N/A (domestic regime; foreign transfer follows other applicable law) |
| **LGPD (Brazil)** | Lei Geral de Proteção de Dados, Law 13,709/2018, Arts. 37–39 | Required — operator agreements | ANPD | Brazilian SCCs (mandatory as of 2024 grace period end), adequacy |
| **DPDP Act (India)** | Digital Personal Data Protection Act 2023, §§ 8, 9, 10 | Required — data processor agreements | DPBI (Data Protection Board of India) | Rules pending; transfer to countries on whitelist |

### Multi-Regime Strategy

A GDPR-compliant base DPA typically provides the highest-common-denominator requirements and
substantially satisfies LGPD and partially satisfies CCPA/CPRA. Gaps remain:

- **CCPA/CPRA**: Prohibitions on sale/sharing and cross-context behavioral advertising not in GDPR
- **UK GDPR**: Post-Brexit transfer mechanisms (IDTA) cannot rely on EU SCCs alone
- **LGPD**: Brazilian SCCs (Resolução CD/ANPD nº 19/2024) mandatory for international transfers
- **DPDP Act**: Rules under § 40 pending notification; whitelist-based transfer approach differs

**Recommended structure**: GDPR-compliant base DPA + jurisdiction-specific addenda as modular annexes.

[JURISDICTION-SPECIFIC] For each regime in scope, identify any member-state or local implementing
legislation that imposes requirements beyond the baseline (e.g., German BDSG § 22 healthcare data,
French CNIL sector guidance, California CPPA additional CPRA regulations, ANPD resolutions on
international transfers, DPDP Act rules when notified).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses and asks
when:

- The answer changes the DPA variant, scope, or applicable regimes
- Party roles are ambiguous (controller/processor/joint controller/independent controller)
- The drafting posture (controller-side vs. processor-side) affects clause generation
- Regime applicability is unclear and checking all regimes would materially increase scope
- A sub-processor tier introduces additional flow-down obligations

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

Accept one of these inputs:

- **Drafting request**: "Draft a DPA for our SaaS platform processing EU, UK, and Brazilian data"
- **Adapting an existing template**: Paste existing DPA or provide file path for adaptation
- **Specific clause request**: "Draft the sub-processor clause for a GDPR/LGPD dual-regime DPA"
- **Flow-down DPA request**: "Draft a sub-processor DPA for us to impose on our third-party vendors"
- **Joint controller request**: "Draft an Art. 26 arrangement for our joint analytics platform"

If no input is provided, prompt the user to supply one. If only a master agreement is provided
without a DPA, ask whether personal data is being processed and whether a DPA addendum is needed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured options:

1. **Which side are you on?**
   - Options: **Controller** (you control the purpose/means; drafting DPA terms to impose on processor),
     **Processor** (you process on behalf of a controller; responding to controller's DPA requirements),
     **Both** (building a bilateral negotiated DPA template)
   - *Why this matters*: Controller-side drafting maximizes audit rights, breach notification speed,
     and liability protections. Processor-side drafting balances compliance with operational feasibility.

2. **What type of DPA is needed?**
   - Options: **Controller-to-Processor** (Art. 28 DPA), **Controller-to-Controller** (Art. 26 joint
     arrangement), **Processor-to-Sub-Processor** (flow-down DPA), **Service Provider Addendum**
     (CCPA/CPRA), **Multi-variant** (all of the above for a platform DPA program)
   - *Why this matters*: Each variant has fundamentally different obligations and structure.
     Art. 26 joint arrangements require mutual obligation clauses; Art. 28 DPAs are controller-led.

3. **Which regimes apply?**
   - Options: **EU GDPR only**, **UK GDPR only**, **Both EU and UK GDPR**, **CCPA/CPRA also in scope**,
     **LGPD (Brazil) also in scope**, **India DPDP Act also in scope**, **All regimes**, **Let me
     determine from the context**
   - Allow multiple selections.
   - *Why this matters*: Determines which modular annexes to generate. Missing a regime creates
     compliance exposure.

4. **Any existing organizational DPA template or playbook?**
   - Options: **Yes — load from local settings or provide path**, **No — use regulatory baseline**,
     **I'll describe key positions as we go**
   - *Why this matters*: Org-specific templates (e.g., "we require 24-hour breach notification" or
     "we never accept general sub-processor authorization") change the clause defaults and
     negotiate posture throughout.

5. **Business context and processor type?**
   - Options: **SaaS/cloud platform** (high-volume, multi-tenant, standard terms),
     **Professional services** (bespoke, negotiated, custom data handling),
     **Sub-processor / downstream vendor** (further downstream; flow-down obligations apply),
     **Strategic partner** (joint processing with shared benefit)
   - *Why this matters*: A high-volume SaaS processor warrants general sub-processor authorization
     with notification mechanism; a bespoke professional services provider may warrant specific
     authorization for each sub-processor.

If the user provides partial context, proceed with reasonable assumptions and state them explicitly.
Default assumptions: controller side, GDPR applies, controller-to-processor variant, no playbook
(use Art. 28 regulatory baseline).

### Step 3: Verify Party Roles

Before generating DPA language, verify that the controller/processor role assignment matches the
operational reality. **Role misclassification is one of the most consequential DPA failures.**

Apply the EDPB Guidelines 07/2020 decision tree [VERIFY]:

**Step 3a — Who determines the purpose?**
- One party alone determines purpose → that party is the controller; other is processor or
  independent controller
- Both parties together determine purpose → candidate joint controllers (Art. 26, not Art. 28)
- One party executes processing as told by the other → candidate processor

**Step 3b — Who determines the essential means?**
- "Essential means" = which data, legal basis, retention period, data subject categories → controller function
- "Non-essential means" = technical tool selection, software implementation → does not trigger controller status

**Step 3c — Joint Controller Indicators (Art. 26 scenario)**
- Both parties benefit from the same processing outcomes independently
- Processing impossible without both parties' active contribution
- Both parties can independently determine to use or stop using the data

**Consequences table:**

| Role | Applicable Instrument | Key Obligation |
|------|----------------------|---------------|
| Controller | GDPR Art. 6/9 lawful basis + Art. 28 DPA with processor | Demonstrate lawful basis; respond to data subjects |
| Processor | GDPR Art. 28 DPA | Process only on documented instructions |
| Joint Controller | GDPR Art. 26 arrangement | Determine respective responsibilities; make arrangement available to data subjects |
| Independent Controller | Own privacy notice + Art. 6/9 basis | No DPA required; each has separate obligations |
| Sub-Processor | Flow-down Art. 28 DPA from processor | Same obligations as processor but vis-à-vis the direct processor |

**⟁ CLARIFY** — If role assignment is ambiguous:
- "The context suggests [Party A] may be a joint controller rather than a processor, because
  [indicator]. Should I generate an Art. 26 joint controller arrangement instead of an Art. 28 DPA?"
- "The processor appears to use the data for its own service optimization. This could make it a
  joint controller for those purposes. How should I handle this?"

If role misclassification is confirmed: **do not proceed with Art. 28 DPA**; generate the
appropriate instrument for the confirmed role.

### Step 4: Load DPA Template / Playbook

Check for an organization-specific DPA template or playbook in local settings (e.g., `legal.local.md`
or similar configuration files).

A DPA playbook defines:
- **Standard positions**: Preferred language for each major DPA clause type
- **Acceptable ranges**: Terms that can be accepted without escalation
- **Escalation triggers**: Terms requiring DPO, senior counsel, or executive sign-off
- **Approved sub-processor list**: Known approved sub-processors and their certification status

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Regulatory baselines** — Use GDPR Art. 28, EDPB guidelines, ICO guidance, CPPA
  regulations, and ANPD resolutions as the baseline. Mark all generated language as "Regulatory
  minimum — not organizational positions."
- **Option B: Provide positions as we go** — Start drafting and pause at each major clause to
  ask about the organization's preferred position.
- **Option C: Set up a baseline now** — Walk through defining standard positions for the 15
  DPA clause categories. Slower upfront but produces reusable playbook for all future DPAs.

If proceeding without a playbook: label all output "Based on regulatory baselines — not
organizational positions."

### Step 5: Gather Legal Authority

Use **legalcode-mcp** to gather jurisdiction-relevant authority before drafting clause language.

**Research targets:**

1. **GDPR Art. 28 and its supplements:**
   - EDPB Guidelines 07/2020 on controller/processor concepts [VERIFY]
   - EDPB Opinion 22/2024 on obligations in reliance on processors and sub-processors [VERIFY]
   - Art. 29 Working Party Opinion 1/2010 on controller/processor concepts [VERIFY]
   - EDPB Recommendations 01/2020 on supplementary measures for transfers [VERIFY]

2. **UK GDPR:**
   - ICO guidance on controller/processor obligations [VERIFY]
   - UK IDTA (International Data Transfer Agreement, effective 21 March 2022) [VERIFY]
   - Data (Use and Access) Act 2025 — phased implementation Jun 2025–Jun 2026 [VERIFY]

3. **CCPA/CPRA:**
   - Cal. Civil Code §1798.140(ag) definition of "service provider" [VERIFY]
   - Cal. Civil Code §1798.140(ah) definition of "third party" [VERIFY]
   - CPPA regulations §§ 7050–7053 on service provider contracts [VERIFY]

4. **LGPD:**
   - Arts. 37–39 on operator obligations [VERIFY]
   - Resolução CD/ANPD nº 19/2024 on Brazilian SCCs for international transfers [VERIFY]
   - ANPD guidance on operator agreement requirements [VERIFY]

5. **India DPDP Act:**
   - §§ 8, 9, 10 on data fiduciary/processor obligations [VERIFY]
   - § 40 on transfer of personal data outside India (whitelist approach) [VERIFY]
   - Rules notified under DPDP Act 2023 (check publication status) [VERIFY]

Save the most relevant results to `/tmp/legalcode-dpa-drafter-research.md`. Mark all
legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**
- Mark all statutory and case law references throughout the DPA with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural quality, clause completeness, and dual-perspective generation

### Step 6: Select DPA Architecture

Based on the context gathered in Steps 2–5, determine which DPA components to generate:

| Component | Generate When | Regime |
|-----------|--------------|--------|
| **Core DPA (15 clauses)** | Always | GDPR Art. 28 baseline |
| **Annex A: Processing Schedule** | Always | GDPR Art. 28(3) preamble |
| **Annex B: Technical and Organizational Measures** | Always | GDPR Art. 32 |
| **Annex C: Sub-Processor Authorization** | Sub-processors exist or expected | GDPR Art. 28(2) |
| **UK Addendum** | UK data subjects or UK-established processor | UK GDPR + DUA Act 2025 |
| **California Exhibit** | CA residents' data; CCPA/CPRA in scope | CCPA/CPRA §§ 7050–7053 |
| **Brazil Annex** | Brazilian data subjects; LGPD in scope | LGPD Arts. 37–39 + ANPD SCCs |
| **India Annex** | Indian data subjects; DPDP Act in scope | DPDP Act §§ 8–10 (rules pending) |
| **Art. 26 Joint Controller Arrangement** | Joint controller confirmed in Step 3 | GDPR Art. 26 |
| **Sub-Processor Flow-Down DPA** | Processor-to-sub-processor requested | GDPR Art. 28(4) |

**⟁ CLARIFY** — If generating a full DPA program would be very large:
- "I can generate the full DPA with all [N] components, or focus on the highest-priority
  components first. Which do you prefer?"

### Step 7: Draft Core DPA Clauses

Draft all 15 DPA clause categories. For each clause, generate:
1. **REQUIRED** minimum language (regulatory floor)
2. **Controller-favorable position** (maximizes controller protections)
3. **Processor-favorable position** (balances compliance with operational feasibility)
4. **Market-standard compromise** (where the two sides typically land)

Mark each clause with its classification (see **Clause Classification** below).
Flag any clause that differs between GDPR/UK/CCPA/LGPD/DPDP regimes.

### Step 8: Draft Jurisdiction-Specific Annexes

For each regime confirmed in scope in Step 2, generate the applicable annex or addendum using
the templates in the **Jurisdiction-Specific Annexes** section below.

### Step 9: Quality Verification

Before delivering the draft, run all quality checks (see **Quality Assurance Framework**):
1. **Citation Quality Gates** (5 gates) — run silently, revise any failures
2. **Self-Interrogation** (3-pass) — for every REQUIRED clause with HIGH severity consequences
3. **Confidence Scoring** — assign confidence to each clause analysis
4. **Completeness check** — confirm all 15 clause categories present
5. **Regime coverage matrix** — confirm each in-scope regime fully addressed
6. **Dual-perspective validation** — confirm each material clause has controller and processor views
7. **Glass Box Audit Trail** — generate YAML and append to output

### Step 10: Deliver DPA Draft

Structure output per **Output Format Template** below. Include:
- Executive summary with regime coverage matrix
- Full DPA draft (clauses 1–15)
- All applicable annexes and addenda
- Dual-perspective negotiation notes (as inline comments)
- Tier 1/2/3 negotiation priorities
- Glass Box audit trail

---

## DPA Architecture: 15-Clause Framework

### Classification Legend

| Classification | Meaning |
|---------------|---------|
| **REQUIRED** | Mandated by applicable statute — omission creates direct regulatory violation |
| **CONDITIONALLY REQUIRED** | Required only if specified condition applies (e.g., cross-border transfer, specific data type) |
| **RECOMMENDED** | Not explicitly mandated but strongly advised by regulatory guidance or best practice |
| **OPTIONAL** | Commonly included for commercial clarity but not required by any applicable statute |

---

### Clause 1: Parties, Recitals, and Definitions — REQUIRED

**Purpose**: Establishes the parties' roles, the legal basis for the DPA, and defines key terms
consistently with applicable data protection law.

**REQUIRED elements:**
- [ ] Identify the Controller (name, address, registration number)
- [ ] Identify the Processor (name, address, registration number)
- [ ] Define "Personal Data," "Processing," "Data Subject" consistent with applicable regime
- [ ] Reference the main commercial agreement (MSA, SaaS agreement, services agreement)
- [ ] State order of precedence (DPA governs over main agreement for data protection matters)
- [ ] Identify applicable data protection law

**Controller-favorable language:**
> "This DPA supplements and forms part of the Agreement. In the event of conflict between this
> DPA and the Agreement, this DPA takes precedence with respect to matters of data protection.
> Capitalized terms used in this DPA but not defined herein have the meaning given in Regulation
> (EU) 2016/679 (GDPR)."

**Processor-favorable language:**
> "This DPA supplements the Agreement and does not modify it. Defined terms in the Agreement
> apply to this DPA unless otherwise specified. In the event of conflict, the Agreement governs
> except to the extent this DPA addresses specific data protection compliance obligations."

**[JURISDICTION-SPECIFIC]** UK GDPR requires reference to the UK GDPR and DPA 2018. CCPA/CPRA
requires use of "Business" and "Service Provider" (not "Controller" and "Processor"). LGPD uses
"Controlador" and "Operador."

---

### Clause 2: Subject Matter, Duration, Nature, and Purpose — REQUIRED

**Regulatory basis:** GDPR Art. 28(3) preamble; LGPD Art. 37 [VERIFY]

**Purpose**: Specifies the scope, duration, and nature of the processing relationship.

**REQUIRED elements:**
- [ ] Subject matter (what service gives rise to the processing)
- [ ] Duration (term of DPA, aligned with main service term plus post-termination period)
- [ ] Nature of processing (what operations are performed: collection, storage, analysis, disclosure)
- [ ] Purpose of processing (why the controller processes — specific, not circular)
- [ ] Type of personal data (specific data categories processed)
- [ ] Categories of data subjects (whose data is processed)

**Controller-favorable language (Article 28 minimum, with specificity requirement):**
> "The Processor shall Process Personal Data solely in accordance with the documented instructions
> of the Controller as set out in Annex A (Processing Schedule) to this DPA. The subject matter,
> duration, nature, and purpose of Processing, the types of Personal Data, and the categories of
> Data Subjects are as specified in Annex A. Any change to the Processing Schedule requires prior
> written agreement of the Controller."

**Common deficiencies:**
- Subject matter defined only as "providing the services" (too vague; EDPB requires specificity)
- No duration specified or duration is "indefinite"
- Purpose defined as "as required to provide the services" (circular, not independently verifiable)
- Data categories listed as "personal data" without specificity

**[JURISDICTION-SPECIFIC]** CCPA/CPRA requires the contract to specify the "specific purposes"
for which personal information is disclosed. LGPD requires description of the processing activities
and categories of personal data (Art. 37). DPDP Act requires description of processing activities.

---

### Clause 3: Processing Instructions Mechanism — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(a) [VERIFY]

**Purpose**: Establishes how the controller issues and the processor executes documented processing
instructions.

**REQUIRED elements:**
- [ ] Processor processes only on documented instructions from controller
- [ ] Instructions can be issued through the Agreement, this DPA, and written amendments
- [ ] Processor must notify controller if an instruction would violate applicable data protection law
- [ ] Processor's obligation to suspend processing pending controller response if instructed illegally
- [ ] Instructions mechanism covers international transfers (not just operational instructions)

**Controller-favorable language:**
> "The Processor shall Process Personal Data only on the documented instructions of the Controller,
> including with regard to transfers of Personal Data to a third country or an international
> organization, unless required to do so by Union or Member State law to which the Processor is
> subject; in such a case, the Processor shall inform the Controller of that legal requirement
> before Processing, unless that law prohibits such information on important grounds of public
> interest. The Controller's instructions are deemed to include the processing activities described
> in Annex A and any subsequent written instructions issued by the Controller's authorized
> representatives."

**EDPB Opinion 22/2024 note** [VERIFY]: The EDPB has clarified that including the wording from
Art. 28(3)(a) in sub-processing contracts is "highly recommended but not mandatory." Parties can
adopt similar phrases like "unless required to do so by law or binding order of a governmental body."

**Common deficiencies:**
- No provision for processor to challenge instructions on legality grounds
- Instructions mechanism does not cover transfers to third countries
- No specification of who can issue instructions (creates unauthorized instruction risk)
- Oral instructions permitted without written confirmation requirement

---

### Clause 4: Confidentiality of Processing Personnel — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(b) [VERIFY]

**Purpose**: Ensures that persons authorized to process personal data are bound by confidentiality.

**REQUIRED elements:**
- [ ] Authorized persons are bound to confidentiality (contractual obligation, statutory, or equivalent)
- [ ] List or description of authorized persons or categories
- [ ] Processor's obligation to ensure authorized persons are limited to those needed

**Market-standard language:**
> "The Processor shall ensure that persons authorized to Process Personal Data have committed
> themselves to confidentiality or are under an appropriate statutory obligation of confidentiality.
> The Processor shall ensure that access to Personal Data is limited to those persons who need
> access to perform the services described in Annex A."

**Note**: Statutory confidentiality (e.g., healthcare professionals' statutory duties) satisfies
this obligation; explicit contractual terms are not required if statutory equivalent exists [VERIFY].

---

### Clause 5: Security of Processing (Technical and Organizational Measures) — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(c) + Art. 32 [VERIFY]

**Purpose**: Requires the processor to implement appropriate technical and organizational security
measures. **A DPA that merely references Art. 32 without specifying measures is non-compliant.**

**REQUIRED elements:**
- [ ] Reference to Art. 32 measures (or equivalent under applicable regime)
- [ ] Concrete TOM specification (either in-clause or by reference to Annex B)
- [ ] Encryption and pseudonymization obligations
- [ ] Ongoing confidentiality, integrity, availability, and resilience of systems
- [ ] Ability to restore availability and access to personal data after incident
- [ ] Regular testing, assessment, and evaluation of TOM effectiveness
- [ ] Risk-proportionate approach to security measures

**Controller-favorable language:**
> "The Processor shall implement and maintain the technical and organizational measures specified
> in Annex B (Technical and Organizational Measures). The Processor shall not materially reduce
> the security measures described in Annex B without prior written notice to the Controller. The
> Controller retains the right to require additional security measures proportionate to the risk
> profile of the processing upon reasonable notice."

**Processor-favorable language:**
> "The Processor shall implement and maintain technical and organizational measures that provide
> a level of security appropriate to the risk, taking into account the state of the art, the costs
> of implementation, and the nature, scope, context, and purposes of Processing. The Processor
> may update security measures from time to time, provided that any updates do not materially
> reduce the security level described in Annex B."

**See TOM Framework section below for Annex B content guidance.**

---

### Clause 6: Sub-Processor Controls — REQUIRED

**Regulatory basis:** GDPR Art. 28(2) and Art. 28(3)(d) [VERIFY]; EDPB Opinion 22/2024 [VERIFY]

**Purpose**: Controls the processor's ability to engage sub-processors and establishes flow-down
of DPA obligations.

**Authorization types:**
- **Specific authorization**: Controller must approve each and every sub-processor individually
- **General authorization**: Processor may engage sub-processors from a maintained list; processor
  must notify controller of intended changes to allow objection

**REQUIRED elements (for general authorization):**
- [ ] Controller provides general written authorization to engage listed sub-processors (Annex C)
- [ ] Processor must inform controller of intended additions or replacements (notification window)
- [ ] Controller has right to object to new sub-processors (with objection process)
- [ ] Processor must impose same DPA obligations on each sub-processor
- [ ] Processor remains liable to controller for sub-processor's performance

**EDPB Opinion 22/2024 note** [VERIFY]: Controllers retain **ultimate responsibility** for
sub-processor selection. The initial processor should propose sub-processors that provide sufficient
guarantees, but the responsibility for verifying those guarantees remains with the controller.
Controllers should have identity information on all processors and sub-processors readily available.

**Controller-favorable language (with meaningful objection right):**
> "The Processor shall not engage a sub-processor without the prior specific or general written
> authorization of the Controller. Where the Processor is given general written authorization to
> engage sub-processors, the Processor shall notify the Controller at least [30] days in advance
> of any intended additions or replacements to the list in Annex C. The Controller may object to
> the proposed change within [20] business days on reasonable grounds related to data protection.
> If the Controller objects and the Processor proceeds, the Controller may terminate the Agreement
> on [30] days' notice without penalty. Where the Processor engages a sub-processor, the Processor
> shall impose on the sub-processor the same data protection obligations as those set out in this
> DPA. If the sub-processor fails to fulfil its data protection obligations, the Processor shall
> remain fully liable to the Controller for the performance of those obligations."

**Processor-favorable language (with limited objection right):**
> "The Processor may engage sub-processors listed in Annex C. The Processor shall provide
> [14] days' written notice before engaging a new sub-processor. The Controller may object to
> a new sub-processor solely on reasonable data protection grounds by notifying the Processor
> within [10] business days of notice. If the Processor cannot provide the services without the
> objected-to sub-processor, the parties shall negotiate in good faith to resolve the concern."

**[JURISDICTION-SPECIFIC]** CCPA/CPRA: Service providers may not disclose personal information
to sub-service providers without entering a written contract imposing CCPA-equivalent obligations.
LGPD Art. 37: Operators must contract with sub-operators and ensure equivalent protection.

---

### Clause 7: Data Subject Rights Assistance — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(e) [VERIFY]; GDPR Arts. 12–22 [VERIFY]

**Purpose**: Requires the processor to assist the controller in responding to data subject requests
(access, rectification, erasure, portability, objection, restriction).

**REQUIRED elements:**
- [ ] Processor assists controller in responding to data subject requests
- [ ] Timeframe for processor to provide assistance (typically within [5–10] business days)
- [ ] Scope of assistance (providing data in usable format, confirming deletion, etc.)
- [ ] Cost allocation for assistance beyond reasonable scope
- [ ] Processor must not respond directly to data subjects unless authorized

**Controller-favorable language:**
> "The Processor shall promptly notify the Controller if the Processor receives a request from
> a Data Subject regarding any Personal Data. The Processor shall not respond to any such request
> directly without the Controller's prior authorization. Taking into account the nature of the
> Processing, the Processor shall assist the Controller by appropriate technical and organizational
> measures, insofar as this is possible, in fulfilling the Controller's obligation to respond to
> requests from Data Subjects to exercise their rights under Chapter III of the GDPR, including
> rights of access, rectification, erasure, restriction, portability, and objection. The Processor
> shall provide such assistance within [5] business days of a request from the Controller."

**[JURISDICTION-SPECIFIC]** CCPA/CPRA: Service providers must cooperate with businesses in
responding to consumer rights requests (opt-out, deletion, correction) [VERIFY]. LGPD: Operators
must assist controllers in responding to data subjects' rights requests under LGPD Arts. 17–22 [VERIFY].
UK Data (Use and Access) Act 2025 [VERIFY]: New proportionate DSAR standard may affect scope of
processor assistance obligations — verify current ICO guidance.

---

### Clause 8: DPIA and Prior Consultation Support — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(f) [VERIFY]

**Purpose**: Requires the processor to assist the controller in conducting Data Protection Impact
Assessments and prior consultations with supervisory authorities.

**REQUIRED elements:**
- [ ] Processor assists with DPIA process when required
- [ ] Processor assists with prior consultation with supervisory authority if required
- [ ] Scope of assistance includes providing information about processing

**Market-standard language:**
> "Taking into account the nature of the Processing and the information available to the Processor,
> the Processor shall assist the Controller in ensuring compliance with the obligations pursuant to
> Articles 35 and 36 of the GDPR relating to data protection impact assessments and prior
> consultations with supervisory authorities. The Processor shall provide the Controller with
> reasonable access to information and personnel as required for such assistance."

---

### Clause 9: Data Breach Notification — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(f) + Art. 33 [VERIFY]

**Purpose**: Establishes the processor's obligation to notify the controller of personal data
breaches and to assist with investigation and remediation.

**REQUIRED elements:**
- [ ] Processor notifies controller of breach without undue delay after becoming aware
- [ ] Minimum notification timeline (commonly 24–48 hours, to ensure controller meets Art. 33's 72-hour window)
- [ ] Minimum content of notification (Art. 33(3) categories: nature, data categories, approximate numbers)
- [ ] Processor's ongoing obligation to provide additional information as it becomes available
- [ ] Processor cooperation with investigation and remediation
- [ ] No public disclosure without controller authorization

**Controller-favorable language:**
> "In the event of a Personal Data Breach, the Processor shall notify the Controller without
> undue delay and in any event within [24] hours after becoming aware of the breach. The
> notification shall include, to the extent available: (a) a description of the nature of the
> Personal Data Breach including, where possible, the categories and approximate number of Data
> Subjects concerned and the categories and approximate number of Personal Data records concerned;
> (b) the name and contact details of the data protection officer or other contact point where more
> information can be obtained; (c) the likely consequences of the Personal Data Breach; and (d)
> the measures taken or proposed to be taken by the Processor to address the Personal Data Breach,
> including measures to mitigate its possible adverse effects. The Processor shall cooperate fully
> with the Controller in investigating the breach and taking remediation steps."

**Processor-favorable language:**
> "In the event of a Personal Data Breach involving Controller's Personal Data, the Processor
> shall notify the Controller without undue delay after becoming aware of the breach. Where not
> all information required under Art. 33(3) GDPR is available at the time of notification, the
> Processor may provide information in phases. The Processor shall use reasonable efforts to
> assist the Controller in investigating and remediating the breach."

**Note on timing**: "Without undue delay" under GDPR Art. 33 means within 72 hours for the
controller's notification to the supervisory authority. To preserve this window, DPAs commonly
require processor notification within 24–48 hours (not 72 hours). A 72-hour processor notification
window leaves the controller no time to assess and notify the authority.

**[JURISDICTION-SPECIFIC] LGPD (Brazil)**: ANPD Resolution CD/ANPD No. 2/2022 requires breach
notification to both the ANPD and affected data subjects within **3 business days** of awareness
— materially shorter than GDPR's 72-hour window [VERIFY]. A DPA covering Brazilian data should
specify processor-to-controller notification within **24 hours** of awareness to ensure the
controller can meet the 3-business-day deadline.

**[JURISDICTION-SPECIFIC] DPDP Act (India)**: Breach notification must be made "without delay" to
the Data Fiduciary, who then notifies the Data Protection Board. Rules specify timelines; verify
current DPDP Rules 2025 requirements [VERIFY].

---

### Clause 10: Audit Rights and Information Provision — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(h) [VERIFY]

**Purpose**: Ensures the controller can verify the processor's compliance with its DPA obligations.

**REQUIRED elements:**
- [ ] Processor makes available all information necessary to demonstrate compliance
- [ ] Processor allows for and contributes to audits and inspections
- [ ] Process for conducting inspections (frequency, notice, format, cost)
- [ ] Third-party audit reliance option (processor can offer certification reports)

**Controller-favorable language:**
> "The Processor shall make available to the Controller all information necessary to demonstrate
> compliance with the obligations laid down in this DPA and shall allow for and contribute to
> audits and inspections conducted by the Controller or a mandated auditor. The Processor shall
> permit the Controller or its representative to inspect the Processor's premises, systems, and
> records relating to the Processing of Personal Data upon [15] business days' written notice,
> exercisable up to [twice] per calendar year, subject to reasonable confidentiality obligations.
> The Processor may satisfy this obligation by providing audit reports (SOC 2 Type II, ISO 27001
> certification, or equivalent) upon request, but shall permit on-site inspection if the Controller
> has reasonable grounds to believe audit reports are insufficient."

**Processor-favorable language:**
> "The Processor shall make available all information reasonably necessary to demonstrate
> compliance with this DPA and shall allow for audits conducted by the Controller or a mandated
> auditor no more than once per calendar year, upon [30] business days' written notice, and
> subject to confidentiality restrictions protecting the Processor's trade secrets and third-party
> data. The Processor may satisfy audit obligations by providing relevant certification reports
> (SOC 2 Type II, ISO 27001) as a substitute for on-site audits except where the Controller
> demonstrates a specific, articulable compliance concern."

---

### Clause 11: Data Return or Deletion on Termination — REQUIRED

**Regulatory basis:** GDPR Art. 28(3)(g) [VERIFY]

**Purpose**: Requires the processor to return or delete all personal data upon termination.

**REQUIRED elements:**
- [ ] Controller's choice: return or deletion of all personal data (including copies held by sub-processors)
- [ ] Timeline for return/deletion (typically [30–60] days after termination)
- [ ] Deletion confirmation / deletion certificate
- [ ] Exception for legal retention obligations (processor notifies controller and protects data)
- [ ] Post-termination confidentiality obligations survive

**Market-standard language:**
> "Upon termination or expiry of the Agreement, the Processor shall, at the choice of the
> Controller, delete or return to the Controller all Personal Data, and delete existing copies,
> unless Union or Member State law requires storage of the Personal Data. The Processor shall
> complete such deletion or return within [30] calendar days of the Controller's request and shall
> provide written certification of deletion to the Controller. If the Controller does not specify
> a preference within [30] days of termination, the Processor shall delete all Personal Data.
> The Processor shall ensure that any sub-processors are obligated to comply with equivalent
> return or deletion obligations."

**Common deficiencies:**
- No deletion certificate requirement (creates proof-of-compliance gap)
- No timeline for return/deletion
- Backups not included in deletion obligation
- No provision for legal retention exceptions

---

### Clause 12: International Data Transfer Mechanism — CONDITIONALLY REQUIRED

**Regulatory basis:** GDPR Arts. 44–49 [VERIFY]; UK GDPR Art. 46 [VERIFY]; LGPD Arts. 33–34 [VERIFY]

**Condition**: Required if personal data is transferred outside the EEA (for GDPR), outside the
UK (for UK GDPR), outside Brazil (for LGPD), or outside India (for DPDP Act).

**Transfer mechanism options:**

| Mechanism | Availability | Requirements |
|-----------|-------------|-------------|
| **Adequacy decision** | Available for adequacy-recognized countries | Verify currency of decision; no supplementary measures required if adequate |
| **EU SCCs 2021** | Module 1 (C2C), Module 2 (C2P), Module 3 (P2P), Module 4 (P2C) | Execute applicable module; conduct Transfer Impact Assessment (TIA) for high-risk destinations |
| **UK IDTA** | UK transfers post-Brexit | ICO-approved template (effective 21 March 2022); or UK Addendum to EU SCCs 2021 |
| **BCRs** | Intra-group transfers | Prior approval from lead DPA required; complex but provides comprehensive coverage |
| **Art. 49 derogations** | Specific limited circumstances | Explicit consent, necessity for contract performance, public interest, vital interests |
| **Brazil SCCs** | Brazilian international transfers | Resolução CD/ANPD nº 19/2024 mandatory SCCs [VERIFY] |

**Schrems II requirement** (C-311/18) [VERIFY]: SCCs alone may be insufficient for transfers to
countries with surveillance laws (e.g., US pre-Privacy Shield adequacy). Conduct Transfer Impact
Assessment (TIA) for high-risk destinations and implement supplementary measures if TIA reveals
unacceptable risk.

**EU SCCs 2021 Module selection:**
- **Module 1**: Controller-to-Controller
- **Module 2**: Controller-to-Processor ← most common for DPAs
- **Module 3**: Processor-to-Processor (for sub-processor flow-down)
- **Module 4**: Processor-to-Controller (e.g., processor uses data for own purposes)

**Critical architecture note**: **Module 2 EU SCCs (C2P) serve simultaneously as:**
(1) the international transfer mechanism replacing Art. 46, AND
(2) a standalone GDPR Art. 28 DPA (Annex I-B covers processing description; Annex II covers TOMs).
When integrating Module 2 SCCs into a commercial agreement, do not add a separate conflicting Art. 28
DPA in the main body — the SCCs alone satisfy both requirements if properly completed. Ensure all
three SCC Annexes are fully completed (I-A: parties; I-B: processing description; I-C: supervisory
authority; II: TOMs; III: sub-processor list). [VERIFY current Commission guidance on Module 2 DPA function]

**[JURISDICTION-SPECIFIC]** The US EU-US Data Privacy Framework (2023 adequacy decision) is
currently valid [VERIFY currency]. Transfers to US processors certified under DPF may rely on
the adequacy decision without SCCs. Monitor for potential challenges. UK adequacy for EU post-Brexit
remains in effect but the EU-UK adequacy decision expires; verify renewal status [VERIFY].

---

### Clause 13: Controller Obligations — RECOMMENDED

**Purpose**: Addresses the controller's obligations to the processor (often overlooked in
controller-drafted DPAs).

**RECOMMENDED elements:**
- [ ] Controller warrants that it has a lawful basis to provide the personal data
- [ ] Controller is responsible for accuracy and completeness of personal data provided
- [ ] Controller must inform the processor of changes to legal basis or applicable regimes
- [ ] Controller must provide timely responses to processor requests for instructions

**Market-standard language:**
> "The Controller warrants that it has a valid lawful basis for Processing the Personal Data under
> applicable Data Protection Law, including for disclosing the Personal Data to the Processor for
> the purposes described in Annex A. The Controller is solely responsible for the accuracy, quality,
> and legality of the Personal Data and the means by which it was obtained. The Controller shall
> promptly respond to the Processor's requests for Processing instructions in accordance with
> applicable timelines."

---

### Clause 14: Liability Allocation — RECOMMENDED

**Regulatory basis:** GDPR Art. 82 [VERIFY]

**Purpose**: Allocates liability between controller and processor for data protection failures.

**RECOMMENDED elements:**
- [ ] Each party liable for breaches of its own data protection obligations
- [ ] Processor liable for non-compliance with this DPA or acting outside controller instructions
- [ ] Processor not liable for damages caused solely by the controller's instructions
- [ ] Coordination on claims by data subjects or regulatory authorities
- [ ] Reference to limitation of liability in the main agreement (with carve-out for data protection fines)

**[JURISDICTION-SPECIFIC]** GDPR Art. 82 provides for joint and several liability between
controller and processor for data subjects. The DPA should address the internal allocation between
the parties without prejudicing data subject rights. Note: GDPR Art. 83 administrative fines
cannot be contractually allocated away from the party responsible for the violation.

---

### Clause 15: Term, Termination, and Survival — RECOMMENDED

**Purpose**: Sets the DPA term, termination triggers, and survival of obligations.

**RECOMMENDED elements:**
- [ ] DPA term tied to the main agreement term
- [ ] DPA automatically terminates upon main agreement termination
- [ ] Controller right to terminate DPA if Processor materially breaches data protection obligations
- [ ] Survival of confidentiality, deletion, and audit obligations post-termination

---

## Multi-Regime Compliance Matrix

For each clause, this matrix identifies the specific requirements per regime to ensure multi-regime
DPAs are fully compliant.

| Clause | EU GDPR | UK GDPR | CCPA/CPRA | LGPD | DPDP Act (India) |
|--------|---------|---------|-----------|------|-----------------|
| **Subject Matter** | Art. 28(3) preamble — specificity required | Mirrors EU GDPR | Specify "specific purposes" §7051(a)(1) | Art. 37 — processing activities + data categories | § 8(5) — data fiduciary must specify purposes [VERIFY] |
| **Instructions** | Art. 28(3)(a) — documented instructions only | Mirrors EU GDPR | Service provider cannot use PI for own purposes §1798.140(ag) | Art. 39 — operator acts per controller instructions | § 8(1) — processor acts only per data fiduciary instructions [VERIFY] |
| **Confidentiality** | Art. 28(3)(b) — contractual or statutory | Mirrors EU GDPR | Implicit in service provider definition | Art. 37 — confidentiality required | Not explicitly addressed; implied [VERIFY] |
| **Security** | Art. 28(3)(c) + Art. 32 | Mirrors; ICO guidance on encryption expectations | CPPA regs require security obligations §7051(a)(3) | Art. 46 — security measures required | § 8(5) — appropriate safeguards required [VERIFY] |
| **Sub-Processors** | Art. 28(2) + Art. 28(3)(d) | Mirrors; IDTA must flow down | Sub-service providers must receive equivalent obligations | Art. 37 — operators must impose same obligations on sub-operators | Not explicitly addressed; implied obligation [VERIFY] |
| **Data Subject Rights** | Art. 28(3)(e) — assist with DSARs | Mirrors; DUAA 2025 proportionate search standard [VERIFY] | Assist with consumer rights requests §7051(a)(5) | Art. 37 — assist with LGPD rights requests | § 8(3) — processor must assist fiduciary [VERIFY] |
| **DPIA Support** | Art. 28(3)(f) | Mirrors | Not required | Not explicitly required | Not currently required [VERIFY] |
| **Breach Notification** | Art. 28(3)(f) — processor notifies controller "without undue delay"; 72hr controller-to-SA | Mirrors EU; ICO is authority; DUAA 2025 no change to timeline | CCPA breach notification under Civil Code §1798.150 (separate obligation) [VERIFY] | Art. 48 — ANPD + data subjects within **3 business days** (CD/ANPD No. 2/2022) [VERIFY] | DPDP Rules 2025 — "without delay"; data fiduciary notifies Board; Rules effective May 2027 [VERIFY] |
| **Audit Rights** | Art. 28(3)(h) | Mirrors | CPPA regs allow audit rights §7051(a)(7) | Art. 37 — inspection rights | § 8(2) — processor must enable compliance verification [VERIFY] |
| **Data Return/Deletion** | Art. 28(3)(g) | Mirrors | CPPA regs require deletion procedures §7051(a)(8) | Art. 37 — data handling on termination | § 8(4) — delete personal data per instruction [VERIFY] |
| **Transfer Mechanism** | Arts. 44–49 + TIA for Schrems II | UK IDTA or UK Addendum to EU SCCs | N/A (domestic regime) | Arts. 33–34 + ANPD SCCs mandatory | § 16 — whitelist of countries [VERIFY] |
| **Joint Controller** | Art. 26 — arrangement required | Mirrors | N/A | Not explicitly addressed | Not explicitly addressed |

---

## Technical and Organizational Measures (TOM) Framework

**Every DPA must specify concrete TOMs.** A TOM annex that merely says "encryption and access
control" is insufficient. Use this framework to generate Annex B content.

### TOM Categories and Minimum Specifications

**1. Access Control and Authentication**
- [ ] Multi-factor authentication (MFA) required for access to systems processing Personal Data
- [ ] Role-based access control (RBAC) with minimum necessary privilege
- [ ] Review access rights at least annually; revoke upon role change or departure
- [ ] Log and monitor all access attempts

**2. Encryption and Pseudonymization**
- [ ] Encryption in transit: TLS 1.2+ (TLS 1.3 preferred) for all data in transit
- [ ] Encryption at rest: AES-256 or equivalent for all stored Personal Data
- [ ] Encryption key management policy (key rotation, separation of duties)
- [ ] Pseudonymization applied where technically feasible and appropriate

**3. System Resilience and Availability**
- [ ] Redundant systems and failover capabilities for critical processing systems
- [ ] Recovery Point Objective (RPO) and Recovery Time Objective (RTO) defined
- [ ] Disaster recovery plan tested at least annually
- [ ] Business continuity plan covering data protection incidents

**4. Vulnerability and Patch Management**
- [ ] Critical security patches applied within [30] days of release
- [ ] Regular vulnerability scanning (at least quarterly)
- [ ] Annual penetration testing by independent third party
- [ ] Vulnerability disclosure and remediation process documented

**5. Incident Detection and Response**
- [ ] 24/7 monitoring and alerting for security incidents
- [ ] Documented incident response procedure aligned with breach notification obligations
- [ ] Designated data breach response team with clear escalation paths
- [ ] Log retention for at least [12] months for forensic purposes

**6. Physical Security**
- [ ] Data centers with access control, CCTV, and environmental monitoring
- [ ] Secure disposal of physical media containing Personal Data
- [ ] Clean desk and clear screen policies for personnel

**7. Staff Training and Awareness**
- [ ] Annual data protection training for all staff with access to Personal Data
- [ ] Background checks where permitted by applicable law
- [ ] Specific training for staff processing special categories of data

**8. Third-Party and Supply Chain Security**
- [ ] Due diligence on all sub-processors and data recipients
- [ ] Annual security assessments for critical sub-processors
- [ ] Contractual security requirements imposed on all sub-processors

**[JURISDICTION-SPECIFIC]** UK GDPR / ICO: Encryption standards recommended but no
prescription [VERIFY]. CCPA/CPRA: CPPA regs adopt "reasonable security procedures" standard [VERIFY].
NIS2 Directive (EU cloud service providers): Additional security obligations for processors qualifying
as Digital Service Providers (DSPs) operating in the EU [VERIFY].

---

## Sub-Processor Management Framework

### Authorization Types

**Specific Authorization:**
- Each sub-processor individually approved by the controller before engagement
- Appropriate for: high-sensitivity processing, small number of sub-processors, bespoke services
- Risk: slows processor's operational flexibility; may require frequent amendments

**General Authorization (with notification mechanism):**
- Controller grants blanket authorization subject to prior notification of changes
- Notification period: [30] days recommended; shorter for time-sensitive operational needs
- Objection mechanism: controller may object on data protection grounds within notification period
- Appropriate for: SaaS platforms with many sub-processors (cloud infrastructure, email,
  monitoring tools), standard commercial services

**EDPB Opinion 22/2024 note** [VERIFY]: General authorization does not reduce the controller's
obligation to verify that sub-processors provide sufficient guarantees. Controllers should receive
and evaluate the processor's representations about sub-processor security.

### Sub-Processor Flow-Down Language (Annex C)

Generate a list in Annex C format:

```
| Sub-Processor | Role | Location | Data Processed | TOM Certification | Controller-Approved |
|---------------|------|----------|---------------|------------------|---------------------|
| [Name]        | [e.g., Cloud hosting] | [Country/Region] | [Data types] | [SOC 2 / ISO 27001] | [Yes/Pending] |
```

**Flow-Down DPA Template (Processor-to-Sub-Processor):**
When the processor engages a sub-processor, the processor must impose obligations "by contract
or other legal act under Union or Member State law" (GDPR Art. 28(4) [VERIFY]) that are
"essentially the same" as those imposed on the processor by the controller's DPA.

Generate a stripped-down flow-down DPA for the processor-to-sub-processor relationship
using Module 3 of the EU SCCs 2021 (P2P) [VERIFY] as the basis, with the processor taking
the role of the "controller" in the flow-down relationship.

---

## International Transfer Mechanism Selector

Use this selector to identify the correct transfer mechanism for cross-border data flows.

### EU GDPR Transfer Selector

```
1. Is the destination country covered by an EU adequacy decision?
   → Yes: Transfer is permitted. Reference the adequacy decision in the DPA.
   → No: Go to 2.

2. Is the processor established in the US and certified under the EU-US Data Privacy Framework?
   → Yes: Transfer permitted under DPF adequacy decision. Verify certification at
     dataprivacyframework.gov [VERIFY currency of adequacy decision].
   → No: Go to 3.

3. Are standard contractual clauses (EU SCCs 2021) available?
   → Yes: Execute Module 2 (C2P) or Module 3 (P2P). Conduct TIA for high-risk destinations
     (e.g., countries with broad surveillance laws). Document supplementary measures if needed.
   → No available SCC: Consider BCRs (intra-group only), Art. 49 derogations (limited use).

4. Is the transfer intra-group?
   → Yes: BCRs are available as an alternative. Requires prior DPA approval. Time-intensive
     but provides comprehensive coverage for all group-level transfers.
```

### UK GDPR Transfer Selector

```
1. Is the destination country recognized by the UK as adequate?
   → Yes: Transfer permitted under UK adequacy regulations. Verify current status.
   → No: Go to 2.

2. Use either:
   (a) UK IDTA (International Data Transfer Agreement, effective 21 March 2022): ICO-approved
       template. Must be executed for each transfer or category of transfers.
   (b) UK Addendum to EU SCCs 2021: Allows use of EU SCCs with UK law modifications.

Note: UK transfers cannot rely on EU SCCs alone (post-Brexit). IDTA or UK Addendum is required.
[VERIFY currency of ICO guidance under the Data (Use and Access) Act 2025]
```

### Brazil LGPD Transfer Selector

```
1. Is the destination country/organization recognized as adequate by Brazil (ANPD)?
   → Yes: Transfer permitted.
   → No: Go to 2.

2. Use Brazilian SCCs: Resolução CD/ANPD nº 19/2024 mandates SCCs for international transfers
   from Brazilian controllers/operators. Grace period for existing contracts ended [VERIFY].
   → Sign and execute the ANPD-approved SCC template for transfers outside Brazil.
```

---

## Clause Classification and Prioritization

### Clause Status Classifications

| Classification | Definition |
|---------------|-----------|
| **REQUIRED** | Statutory mandate — omission creates direct regulatory violation |
| **CONDITIONALLY REQUIRED** | Required when a specified condition exists (cross-border transfer, specific data type) |
| **RECOMMENDED** | Strongly advised by regulatory guidance or professional best practice; omission creates compliance risk |
| **OPTIONAL** | Commercially useful for clarity but not required by applicable statute |

### Tier 1 — Must-Haves (Non-Negotiable Compliance Floor)

Every Art. 28 DPA must include, verbatim or substantively:

1. Subject matter, duration, nature, and purpose (with data categories and data subjects) — Art. 28(3) preamble
2. Processing instructions mechanism — Art. 28(3)(a)
3. Confidentiality of personnel — Art. 28(3)(b)
4. Security of processing with concrete TOM specification — Art. 28(3)(c) + Art. 32
5. Sub-processor controls with authorization mechanism — Art. 28(2) + Art. 28(3)(d)
6. Data subject rights assistance — Art. 28(3)(e)
7. DPIA and prior consultation support — Art. 28(3)(f)
8. Breach notification — Art. 28(3)(f)
9. Audit rights and information provision — Art. 28(3)(h)
10. Data return or deletion on termination — Art. 28(3)(g)

**If ANY Tier 1 element is absent, the DPA does not satisfy GDPR Art. 28.**

### Tier 2 — Should-Haves (Material Compliance and Risk)

11. International transfer mechanism (conditionally required but material compliance gap if transfer occurs without it)
12. Controller obligations (warranty of lawful basis; processor needs this protection)
13. Liability allocation (GDPR Art. 82; prevents processor bearing disproportionate risk)

### Tier 3 — Nice-to-Haves (Concession Candidates)

14. Term and survival provisions (commercially useful but not GDPR-required)
15. Boilerplate (entire agreement, severability, governing law, dispute resolution)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, article, or regulatory guidance | Add citation or mark "[UNVERIFIED — DPO/counsel to confirm]" |
| **Format** | Citations follow consistent format: Reg./Law name, article/section, jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments or repeal | Flag "[CHECK CURRENCY — may have been amended or superseded]" |
| **Domain** | Analysis stays within the applicable regime's law; no jurisdictional bleed | Remove or flag cross-jurisdiction assumptions |
| **Confidence** | Uncertainty explicitly stated, never hidden | Add confidence qualifier |

### Self-Interrogation for REQUIRED Clauses

For any Tier 1 REQUIRED clause flagged as deficient or missing, apply this 3-pass review:

**Pass 1 — Regulatory Chain Integrity**: Does the compliance requirement follow directly from
the cited statutory provision? Would the relevant supervisory authority (EDPB/ICO/CPPA/ANPD/DPBI)
reach this conclusion?

**Pass 2 — Completeness**: Have all applicable sub-requirements been addressed? Are there
regime-specific variations under any in-scope regime not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that the proposed clause language is
overly aggressive? Under what operational circumstances might a reasonable processor resist
this clause? Is there a commercially viable compromise that still satisfies the statutory minimum?

Mark audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law, clear statute, unambiguous provision | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments, reasonable minds could differ | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities | Flag for DPO/counsel review with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

Apply confidence scoring to:
- Role classification determination (controller/processor/joint controller)
- Each clause's compliance status per applicable regime
- Transfer mechanism selection
- TIA risk assessment outcomes

---

## Glass Box Audit Trail

Every DPA drafter output MUST include this audit section:

```yaml
glass_box:
  document: "[DPA title / 'DPA Draft for [Controller] and [Processor]']"
  document_type: "[Controller-to-Processor DPA / Joint Controller Arrangement / Sub-Processor DPA]"
  parties:
    controller: "[Controller name]"
    processor: "[Processor name]"
  role_determination: "[Controller/Processor/Joint Controller/Independent Controller]"
  role_confidence: "[Definite/High/Probable/Possible]"
  governing_law: "[Jurisdiction identified from DPA or user intent]"
  regimes_in_scope:
    - "[EU GDPR: Yes/No]"
    - "[UK GDPR: Yes/No]"
    - "[CCPA/CPRA: Yes/No]"
    - "[LGPD (Brazil): Yes/No]"
    - "[DPDP Act (India): Yes/No]"
  playbook_used: "[Organization DPA template / GDPR Art. 28 baseline / Market standards]"
  clauses_drafted: "[number — should be 10–15 depending on scope]"
  tier1_clauses_present: "[N]/10 mandatory GDPR Art. 28 clauses"
  annexes_generated:
    - "[Annex A: Processing Schedule — Yes/No]"
    - "[Annex B: TOM Specification — Yes/No]"
    - "[Annex C: Sub-Processor List — Yes/No]"
    - "[UK Addendum — Yes/No]"
    - "[California Exhibit — Yes/No]"
    - "[Brazil Annex — Yes/No]"
    - "[India Annex — Yes/No]"
  regime_coverage:
    eu_gdpr: "[COMPLETE / PARTIAL — list gaps]"
    uk_gdpr: "[COMPLETE / PARTIAL — list gaps]"
    ccpa_cpra: "[COMPLETE / NOT IN SCOPE / PARTIAL]"
    lgpd: "[COMPLETE / NOT IN SCOPE / PARTIAL]"
    dpdp: "[COMPLETE / NOT IN SCOPE / PARTIAL]"
  transfer_mechanism_selected: "[EU SCCs 2021 Module 2 / UK IDTA / Adequacy / BCRs / TIA required]"
  sub_processor_authorization: "[Specific / General with notification / Not applicable]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[/tmp/legalcode-dpa-drafter-research.md / Not created]"
  statutes_consulted:
    - "GDPR Art. 28 — [VERIFIED / UNVERIFIED]"
    - "GDPR Art. 32 — [VERIFIED / UNVERIFIED]"
    - "GDPR Arts. 44–49 — [VERIFIED / UNVERIFIED]"
    - "UK GDPR Art. 28 — [VERIFIED / UNVERIFIED]"
    - "Data (Use and Access) Act 2025 — [VERIFIED / UNVERIFIED]"
    - "Cal. Civil Code §1798.140 — [VERIFIED / UNVERIFIED]"
    - "LGPD Arts. 37–39 — [VERIFIED / UNVERIFIED]"
    - "DPDP Act 2023 §§ 8–10 — [VERIFIED / UNVERIFIED]"
  regulatory_guidance_consulted:
    - "EDPB Guidelines 07/2020 — [VERIFIED / UNVERIFIED]"
    - "EDPB Opinion 22/2024 — [VERIFIED / UNVERIFIED]"
    - "ICO guidance on controller/processor — [VERIFIED / UNVERIFIED]"
    - "CPPA regulations §§ 7050–7053 — [VERIFIED / UNVERIFIED]"
    - "ANPD Resolução CD/ANPD nº 19/2024 — [VERIFIED / UNVERIFIED]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "[Regimes not covered in this draft]"
    - "[Sub-processor tiers not verified]"
    - "[DPDP Act rules not yet notified — pending verification]"
  reviewer_note: "AI-assisted generation — requires qualified DPO/counsel review before execution"
```

---

## Anti-Patterns

What NOT to do when drafting Data Processing Agreements:

1. **Boilerplate without customization** — The EDPB has explicitly cautioned against using
   generic DPA templates without adapting them to the actual processing relationship [VERIFY].
   Every DPA must specify the actual data categories, data subject types, processing operations,
   and retention periods for the specific relationship.

2. **Role assignment without analysis** — Assigning controller/processor roles in the DPA
   without verifying the operational reality. If the processor independently determines
   processing purposes (e.g., for service improvement, analytics, or model training), it may
   be a joint controller requiring Art. 26, not a processor requiring Art. 28.

3. **"Comply with applicable law" as a substitute for specific obligations** — A clause that
   says "Processor will comply with all applicable data protection laws" is not a DPA. Art. 28
   requires specific enumeration of each mandatory obligation. Vague compliance clauses fail
   regulatory review.

4. **Vague sub-processor authorization** — Blanket authorization to "use third-party service
   providers" without notification mechanism or objection right fails Art. 28(2). The authorization
   must be specific or general-with-notification; silent blanket permission is non-compliant.

5. **Toothless objection rights** — A sub-processor objection right that says the controller
   "may object" without specifying what happens if the controller objects (i.e., processor cannot
   proceed, or controller may terminate) provides no protection. The consequence of objection
   must be specified.

6. **72-hour breach notification window for processor** — The controller has 72 hours to notify
   the supervisory authority. Giving the processor 72 hours to notify the controller leaves no
   time for the controller to assess and escalate. Use 24–48 hours for processor-to-controller
   notification.

7. **TOMs by reference only** — A TOM annex that says "Processor will maintain appropriate
   security consistent with ISO 27001" without specifying concrete measures does not satisfy
   Art. 32 [VERIFY]. Concrete measures (encryption standards, penetration testing frequency,
   MFA requirements) must be specified or incorporated by reference to a sufficiently detailed
   certification scope.

8. **Deletion certificate gap** — Requiring the processor to "delete personal data upon
   termination" without requiring deletion certification leaves the controller unable to
   demonstrate compliance to supervisory authorities or data subjects.

9. **Backup carve-out without timeline** — Excluding backup copies from deletion obligation
   is sometimes commercially necessary, but must include a specific timeline for backup
   cycle expiry (e.g., "backup copies will be overwritten within [90] days in the normal
   course of backup retention"). Open-ended backup carve-outs effectively negate the
   deletion obligation.

10. **Transfer mechanism as afterthought** — Signing a DPA that governs EU/UK data processing
    without addressing the cross-border transfer mechanism creates a Schrems II gap. Transfers
    from EEA to third countries require an active transfer mechanism; lack of one is a direct
    GDPR violation [VERIFY].

11. **SCCs without Transfer Impact Assessment** — Selecting EU SCCs 2021 as the transfer
    mechanism without conducting a Transfer Impact Assessment (TIA) for high-risk destinations
    is non-compliant post-Schrems II. The TIA obligation exists regardless of which SCC module
    is used.

12. **UK transfers on EU SCCs alone** — Post-Brexit, EU SCCs are not recognized by the ICO
    as a valid transfer mechanism for UK-to-third-country transfers. UK IDTA or UK Addendum
    to EU SCCs is required for UK-origin personal data transfers.

13. **CCPA service provider terms copied from GDPR** — CCPA service provider contracts have
    unique prohibitions (no sale, no sharing, no use for cross-context behavioral advertising,
    no retention for the business's own commercial purposes) that have no GDPR equivalent. Do not
    copy GDPR processor language; generate CCPA-specific prohibitions [VERIFY].

14. **Treating LGPD as a GDPR clone** — While LGPD was inspired by GDPR, key differences
    exist: LGPD uses "controlador/operador" (not controller/processor), LGPD Art. 37 imposes
    specific operator agreement requirements, and Brazil's international transfer mechanism
    (ANPD SCCs, Resolução CD/ANPD nº 19/2024) differs from EU SCCs [VERIFY].

15. **Ignoring EDPB Opinion 22/2024** — The EDPB's October 2024 opinion clarified that
    controllers remain ultimately responsible for verifying that sub-processors provide
    sufficient guarantees, even when that initial assessment is delegated to the primary
    processor. DPAs should reflect this by requiring processors to provide controllers with
    information about their entire sub-processor chain [VERIFY].

16. **Audit rights without confidentiality protection** — Unlimited audit rights without
    confidentiality carve-outs expose the processor's trade secrets, third-party data, and
    infrastructure details. Balanced audit rights specify purpose, frequency, confidentiality
    obligations, and the option to substitute independent audit reports (SOC 2, ISO 27001).

17. **Single-pass drafting** — Drafting a DPA in one pass without checking for internal
    consistency: do the termination clauses align with the data return/deletion timelines?
    Does the audit clause reference the TOM annex? Does the sub-processor clause flow down
    the breach notification timeline correctly?

18. **Ignoring the processor perspective** — Controller-only DPA drafting that ignores
    processor operational feasibility typically results in either non-execution or
    extensive redline negotiations. Generate dual-perspective language upfront to identify
    likely pushback and prepare compromise positions.

19. **Missing AI/model training prohibition** — Failing to include an explicit prohibition on
    the processor using controller's personal data to train, fine-tune, or improve the
    processor's own AI models, large language models, or automated decision systems. As AI
    vendors increasingly claim broad license to "improve services" using customer data, an
    explicit prohibition is essential for DPAs covering any SaaS AI product. Omission of
    this clause is particularly serious for special category data [VERIFY GDPR recital 47 scope].

20. **"Sign-and-forget" DPA approach** — EDPB Opinion 22/2024 explicitly rejects the practice
    of signing a DPA and never revisiting it. Controllers must conduct ongoing verification that
    processors continue to provide "sufficient guarantees." A DPA should include provisions for
    annual TOM review, updated sub-processor lists, and re-assessment of security certifications
    (e.g., verifying SOC 2 Type II reports are current and in scope).

---

## Writing Standards

Apply plain-language discipline to all DPA clause language:

**For generated clause text (to be incorporated into the DPA):**
- Active voice: "The Processor shall notify..." not "Notification shall be provided..."
- Name the actor clearly: "The Controller shall specify..." not "It shall be specified..."
- One obligation per sentence. Long obligation clauses create interpretation disputes.
- Concrete specifics: "within 24 hours" not "as soon as practicable"
- Cite the applicable legal provision in-clause when appropriate: "to assist the Controller in
  fulfilling its obligations under Article 28(3)(e) of the GDPR..."
- Avoid defined-term proliferation: define key terms once; do not create synonyms

**For internal rationale notes (shared with user):**
- Confidence qualifiers where appropriate: "GDPR Art. 33 clearly requires..." vs.
  "The ICO has indicated, though without binding guidance, that..."
- Explain the negotiation risk: "Processor will likely resist this because..."
- Flag verification: any unverified citation marked [VERIFY]

**Quality gates before delivery:**
1. Can a privacy professional (not a specialized lawyer) understand the clause without reference
   to external materials?
2. Is every obligation clear as to: who does what, by when, in what format, at whose cost?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or creating deniability? If yes, fix.
5. Could any sentence be shorter without losing a material obligation? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**
- In Step 5, search for current regulatory requirements, EDPB/ICO/CPPA/ANPD guidance, and
  recent enforcement actions relevant to each DPA clause
- Verify currency of GDPR Art. 28 requirements, CCPA/CPRA regulations, LGPD provisions, and
  DPDP Act rules against authoritative sources
- For DPDP Act (India): search for latest rules notification status (rules pending as of 2025 [VERIFY])
- Check EU-US DPF adequacy decision currency and US-UK data bridge status
- Save results to `/tmp/legalcode-dpa-drafter-research.md`

**Without legalcode-mcp:**
- Mark all statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with structural quality and dual-perspective generation
- Focus on clause completeness (Tier 1/2/3 completeness check)
- Include prominent notice that legal citations require independent verification

---

## Output Format Template

Structure the final deliverable as:

```markdown
## DPA Draft Summary

**Document**: Data Processing Agreement — [Controller Name] (Controller) and [Processor Name] (Processor)
**Date**: [date]
**Your Side**: [Controller / Processor / Neutral]
**DPA Variant**: [Controller-to-Processor / Sub-Processor / Joint Controller Arrangement]
**Governing Law**: [jurisdiction]
**Regimes in Scope**: [EU GDPR / UK GDPR / CCPA/CPRA / LGPD / DPDP Act]
**Draft Basis**: [Organization DPA template / GDPR Art. 28 regulatory baseline / Market standards]

---

## Tier 1 Compliance Checklist (GDPR Art. 28)

| Clause | Status | Notes |
|--------|--------|-------|
| Subject matter, duration, nature, purpose (Annex A) | ✅ Drafted / ⚠️ Needs input | [note] |
| Processing instructions mechanism | ✅ Drafted | |
| Confidentiality of personnel | ✅ Drafted | |
| Security / TOM (Annex B) | ✅ Drafted / ⚠️ Customize | |
| Sub-processor controls (Annex C) | ✅ Drafted | |
| Data subject rights assistance | ✅ Drafted | |
| DPIA support | ✅ Drafted | |
| Breach notification | ✅ Drafted | |
| Audit rights | ✅ Drafted | |
| Data return / deletion | ✅ Drafted | |

---

## Regime Coverage Matrix

| Regime | Covered? | Component | Gap / Note |
|--------|----------|-----------|------------|
| EU GDPR | ✅ Yes | Core DPA | — |
| UK GDPR | [✅/⚠️] | UK Addendum | [note if needed] |
| CCPA/CPRA | [✅/⚠️/N/A] | California Exhibit | [note] |
| LGPD (Brazil) | [✅/⚠️/N/A] | Brazil Annex | [note] |
| DPDP Act (India) | [✅/⚠️/N/A] | India Annex | Rules pending [VERIFY] |

---

## Data Processing Agreement

**Between:**
[CONTROLLER LEGAL NAME], a [entity type] incorporated under the laws of [jurisdiction],
with registered address at [address] ("Controller")

**and:**

[PROCESSOR LEGAL NAME], a [entity type] incorporated under the laws of [jurisdiction],
with registered address at [address] ("Processor")

---

### 1. Parties, Definitions, and Precedence

[Insert Clause 1 language — use controller-favorable or balanced variant]

### 2. Subject Matter, Duration, Nature, and Purpose

[Insert Clause 2 language — reference Annex A]

### 3. Processing Instructions

[Insert Clause 3 language]

### 4. Confidentiality

[Insert Clause 4 language]

### 5. Security of Processing

[Insert Clause 5 language — reference Annex B]

### 6. Sub-Processor Controls

[Insert Clause 6 language — reference Annex C]

### 7. Data Subject Rights Assistance

[Insert Clause 7 language]

### 8. DPIA and Prior Consultation Support

[Insert Clause 8 language]

### 9. Data Breach Notification

[Insert Clause 9 language]

### 10. Audit Rights and Information Provision

[Insert Clause 10 language]

### 11. Data Return or Deletion

[Insert Clause 11 language]

### 12. International Data Transfers

[Insert Clause 12 language — reference applicable transfer mechanism]

### 13. Controller Obligations

[Insert Clause 13 language]

### 14. Liability

[Insert Clause 14 language]

### 15. Term, Termination, and Survival

[Insert Clause 15 language]

---

## Annex A: Processing Schedule

**Subject Matter of Processing**: [Description of the service and why it involves personal data]

**Duration**: The term of the Agreement and [30] days thereafter for deletion/return.

**Nature of Processing**: [e.g., hosting, storage, analysis, transmission, combination]

**Purposes of Processing**: [Specific purposes as instructed by the Controller — e.g., "to provide
the SaaS platform services described in the Agreement including user account management, feature
delivery, and product analytics strictly limited to improving services provided to Controller."]

**Categories of Personal Data**:
- [Category 1, e.g., Contact data: name, email, telephone]
- [Category 2, e.g., Transactional data: order history, payment records]
- [Special categories (if any): health data, biometric data — note heightened sensitivity]

**Categories of Data Subjects**:
- [Category 1, e.g., Controller's employees]
- [Category 2, e.g., Controller's customers / end users]

---

## Annex B: Technical and Organizational Measures

[Insert TOM specifications per TOM Framework above]

---

## Annex C: Sub-Processor Authorization

**Authorization Type**: [Specific / General with notification mechanism]

**Approved Sub-Processors**:

[Insert sub-processor table per Sub-Processor Framework above]

**Notification Process** (for general authorization):
New sub-processors will be notified to Controller at [email/URL/platform] at least [30] days
before engagement. Controller may object within [20] business days on data protection grounds.

---

## [If applicable] UK Addendum

[See UK Jurisdiction-Specific Annex below]

---

## [If applicable] California Exhibit: CCPA/CPRA Service Provider Terms

[See California Jurisdiction-Specific Annex below]

---

## [If applicable] Brazil Annex: LGPD Operator Agreement

[See Brazil Jurisdiction-Specific Annex below]

---

## [If applicable] India Annex: DPDP Act Data Processor Agreement

[See India Jurisdiction-Specific Annex below]

---

## Negotiation Notes [For Internal Use]

**Tier 1 — Must-Haves (Non-Negotiable):**
[List any Tier 1 gaps in the draft with recommended action]

**Tier 2 — Should-Haves (Strong Preferences):**
[List any Tier 2 items with processor likely resistance and compromise positions]

**Tier 3 — Concession Candidates:**
[List any Tier 3 items the controller can trade in negotiations]

---

## Glass Box Audit Trail

[Insert YAML audit block per Glass Box template above]
```

---

## Jurisdiction-Specific Annexes

### UK Addendum (UK GDPR + Data (Use and Access) Act 2025)

**Key differences from EU GDPR:**
- **Transfer mechanism**: UK IDTA (effective 21 March 2022) or UK Addendum to EU SCCs is required
  for UK-origin transfers to third countries. EU SCCs alone do not satisfy UK requirements [VERIFY].
- **Supervisory authority**: ICO (Information Commissioner's Office), not EDPB or national DPA
- **DSAR proportionality** (Data (Use and Access) Act 2025) [VERIFY]: Controller only needs to
  conduct a "reasonable and proportionate search" in response to DSARs. Processor assistance
  obligations should align with this proportionate standard.
- **Adequacy**: UK has made its own adequacy decisions post-Brexit; verify current list from ICO.

**UK Addendum Clause:**
> "This UK Addendum applies to any Processing of Personal Data governed by the UK GDPR and the
> Data Protection Act 2018 (UK Data Protection Law). The parties agree that the terms of this DPA
> apply to UK-origin Personal Data mutatis mutandis. For any transfer of UK-origin Personal Data
> to a third country, the parties shall execute and maintain the UK International Data Transfer
> Agreement (UK IDTA) issued by the ICO, or the UK Addendum to the EU Standard Contractual Clauses
> 2021. References to 'GDPR' in this DPA shall be construed as references to the UK GDPR for
> UK-origin Personal Data."

[JURISDICTION-SPECIFIC] Verify implementation timeline of the Data (Use and Access) Act 2025;
several provisions implement in phases between June 2025 and June 2026 [VERIFY].

---

### California Exhibit (CCPA/CPRA Service Provider Terms)

**Key CCPA/CPRA-specific requirements** (Cal. Civil Code §1798.140(ag); CPPA Regs §§ 7050–7053) [VERIFY]:

**Mandatory service provider contract prohibitions:**
- [ ] Service provider may not **sell or share** personal information
- [ ] Service provider may not **retain, use, or disclose** personal information for any commercial
  purpose other than the business purpose specified in the contract or as permitted by the CCPA/CPRA
- [ ] Service provider may not **retain, use, or disclose** personal information outside the direct
  business relationship between the service provider and the business
- [ ] Service provider may not **combine** personal information received from the business with
  personal information received from other sources, except as permitted by CCPA/CPRA
- [ ] Service provider must **cooperate** with the business in responding to consumer rights requests
- [ ] Service provider must **certify** it understands the restrictions and will comply

**California Exhibit Clause:**
> "Service Provider certifies that it understands the restrictions set forth in this Exhibit and
> will comply with them. Service Provider shall not: (a) sell or share Personal Information (as
> defined by the CCPA/CPRA) received from Business; (b) retain, use, or disclose Personal
> Information for any purpose other than the Business Purposes specified in Annex A; (c) retain,
> use, or disclose Personal Information for a commercial purpose other than those Business
> Purposes; (d) retain, use, or disclose Personal Information outside the direct business
> relationship between Service Provider and Business; or (e) combine Personal Information
> received from Business with Personal Information received from other sources, except as
> permitted by the CCPA/CPRA and its implementing regulations. Service Provider shall promptly
> notify Business if it receives a Consumer request under the CCPA/CPRA that relates to
> Personal Information processed under this Agreement."

[JURISDICTION-SPECIFIC] Note: CCPA/CPRA uses "Business" and "Service Provider" rather than
"Controller" and "Processor." CPPA may issue new regulations — verify currency [VERIFY].

---

### Brazil Annex (LGPD Arts. 37–39 + ANPD SCCs)

**Key LGPD-specific requirements** (Lei 13,709/2018, Arts. 37–39) [VERIFY]:

- **Art. 37**: The controller (Controlador) and operator (Operador) must keep a record of the
  personal data processing activities
- **Art. 38**: The controller must carry out a personal data impact report (similar to DPIA)
- **Art. 39**: The operator shall perform the processing solely according to the instructions
  provided by the controller and shall not perform any processing contrary to such instructions
- **International transfers**: Brazilian SCCs (Resolução CD/ANPD nº 19/2024) are now mandatory
  for international transfers from Brazilian controllers/operators [VERIFY currency of ANPD SCCs]

**Brazil Annex Clause:**
> "This Brazil Annex applies to any Processing of Personal Data governed by Brazil's Lei Geral
> de Proteção de Dados (LGPD), Law 13,709/2018. The Operador (Processor) shall perform the
> Processing of Dados Pessoais (Personal Data) solely according to the instructions provided by
> the Controlador (Controller) as specified in Annex A. The Operador shall not perform any
> Processing contrary to the Controller's instructions or applicable Brazilian data protection
> law. For any international transfer of Brazilian Personal Data to third countries, the parties
> shall execute the Standard Contractual Clauses approved by the ANPD (Resolução CD/ANPD nº
> 19/2024) or rely on an adequacy decision recognized by Brazil [VERIFY]. The parties shall
> maintain the records of Processing activities required under LGPD Art. 37."

---

### India Annex (DPDP Act 2023 — Rules Pending)

**Implementation status**: The Digital Personal Data Protection Rules, 2025 were formally enacted
on **13 November 2025**. However, most substantive compliance obligations (consent, privacy notice,
security requirements) take effect on **13 May 2027** [VERIFY]. This Annex reflects the DPDP Act
2023 and Rules 2025 as enacted; verify implementation dates and any amendments with qualified
Indian data protection counsel before execution.

**Key DPDP Act-specific requirements** (DPDP Act 2023 §§ 8–10) [VERIFY]:

- **§ 8(1)**: A Data Processor shall Process personal data only in accordance with the instructions
  of the Data Fiduciary and for the purposes specified in the contract
- **§ 8(2)**: A Data Processor must enable the Data Fiduciary to comply with its obligations
- **§ 8(3)**: A Data Processor must notify the Data Fiduciary of any Personal Data Breach without
  delay (timeline specified in rules — verify when notified)
- **§ 8(4)**: A Data Processor must erase personal data upon request by the Data Fiduciary or
  when the purpose is fulfilled, whichever is earlier
- **§ 8(5)**: A Data Fiduciary must implement appropriate technical and organizational measures
  to ensure the Data Processor complies
- **§ 16**: Transfer of personal data outside India only to countries on DPBI whitelist [VERIFY]

**India Annex Clause:**
> "This India Annex applies to any Processing of Personal Data (as defined in the DPDP Act)
> governed by India's Digital Personal Data Protection Act, 2023. The Data Processor shall
> Process Personal Data only in accordance with the instructions of the Data Fiduciary as
> specified in Annex A, and for the specific purposes described therein. The Data Processor
> shall notify the Data Fiduciary of any Personal Data Breach without undue delay upon becoming
> aware. The Data Processor shall erase Personal Data upon instruction from the Data Fiduciary
> or upon fulfilment of the purpose specified in Annex A. The Data Fiduciary shall implement
> appropriate technical and organizational measures to ensure the Data Processor complies with
> these obligations. International transfers of Personal Data shall only be made to countries
> listed in the DPBI whitelist under DPDP Act § 16 [VERIFY currency of whitelist].
>
> **Note**: The DPDP Act rules have not yet been fully notified. This Annex reflects the DPDP Act
> 2023 as enacted. Parties shall review and update this Annex upon notification of applicable
> rules. [VERIFY current rule notification status]"

---

## Localization Notes

When localizing this skill to a specific jurisdiction or sector:

1. **Germany (BDSG)**: § 22 BDSG imposes additional requirements for health, biometric, and
   special category data processing. German DPOs have enhanced consultation obligations. [VERIFY]
2. **France (CNIL guidance)**: CNIL has sector-specific DPA guidance for healthcare, fintech,
   and HR processing. Check CNIL guidance for applicable sectors. [VERIFY]
3. **Healthcare (HIPAA BAA)**: US-regulated healthcare processors require a HIPAA Business
   Associate Agreement (BAA) in addition to GDPR DPA. Use `legalcode-saas-agreement-drafter`
   for HIPAA BAA integration guidance.
4. **Financial services**: FS-sector processors may face additional security obligations under
   DORA (EU Digital Operational Resilience Act, applicable from January 2025) or equivalent
   national regulation. [VERIFY]
5. **NIS2 (EU cloud processors)**: SaaS and cloud service providers qualifying as digital
   service providers under NIS2 Directive (2022/2555) face enhanced security obligations
   beyond GDPR Art. 32 that should be reflected in TOM specifications. [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis drawing on GDPR Art. 28 regulatory
baseline, EDPB Guidelines 07/2020, EDPB Opinion 22/2024 on processor and sub-processor
obligations, ICO guidance, UK IDTA framework, CPPA CCPA/CPRA regulations, LGPD Arts. 37–39,
ANPD Resolução CD/ANPD nº 19/2024, and DPDP Act 2023. Structural patterns adapted from the
`legalcode-dpa-review-and-negotiation`, `legalcode-contract-review`, and
`legalcode-saas-agreement-drafter` reference skills. Complements `legalcode-dpa-review-and-negotiation`
(which reviews existing DPAs) by providing the corresponding drafting workflow.
