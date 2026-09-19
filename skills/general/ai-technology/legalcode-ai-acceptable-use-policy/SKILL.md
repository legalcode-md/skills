---
name: legalcode-ai-acceptable-use-policy
description: Drafts or reviews an organization's AI Acceptable Use Policy (AUP) — governing which AI tools
  employees may use, under what conditions, and with what safeguards. Use when establishing AI governance
  foundations, conducting gap analysis against EU AI Act Art. 4 (AI literacy), ISO 42001, NIST AI RMF,
  or sector-specific requirements (HIPAA, FINRA, legal professional ethics rules), or updating existing
  policies for evolving AI tool landscapes.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts or reviews an organization's AI Acceptable Use Policy (AUP) — governing which AI tools employees may use, under what conditions, and with what safeguards. Covers permitted and prohibited AI uses, data handling restrictions (confidential information, PII/PHI, privileged communications), employee disclosure obligations for AI-generated content, intellectual property considerations for AI-generated work product, ethical walls between AI-assisted and human-only processes, security requirements for AI tool access, training and certification obligations, incident reporting for AI errors and bias, accountability and oversight requirements, and vendor-specific guidance for ChatGPT/OpenAI, Claude/Anthropic, Microsoft Copilot, and Google Gemini. Use when establishing AI governance foundations, conducting gap analysis against EU AI Act Art. 4 (AI literacy), ISO 42001, NIST AI RMF, or sector-specific requirements (HIPAA, FINRA, legal professional ethics rules), or updating existing policies for evolving AI tool landscapes. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for local enforcement provisions. Produces a customizable AUP document, approved-tool registry, data-handling matrix, implementation roadmap, and compliance checklist.


# Legalcode AI Acceptable Use Policy

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and review of
> organizational AI governance policies. It does not constitute legal advice. All outputs
> should be reviewed by qualified legal counsel, a data protection officer, and relevant
> compliance professionals before adoption or publication. Laws, regulations, and AI
> platform terms of service change rapidly; verify current applicability before relying
> on any provision described here. Regulatory and statutory references cited from memory
> or web research carry hallucination risk — verify against authoritative sources before
> relying on them.

## Purpose and Scope

This skill drafts and reviews organizational AI Acceptable Use Policies (AUPs). An AI
AUP is the foundational governance document that communicates to all employees which AI
tools are approved, under what conditions they may be used, and what safeguards are
required. It translates the organization's AI risk appetite into enforceable employee
obligations.

**Covers:**

- Drafting a complete AI AUP from organizational context
- Reviewing an existing AI AUP for regulatory gaps and best-practice shortfalls
- Building or auditing an Approved AI Tool Registry with tiered data-sensitivity controls
- Drafting prohibited-use clauses with regulatory basis
- Designing data handling rules by data classification category
- Drafting employee disclosure and transparency obligations
- Identifying IP ownership risks from AI-generated work product
- Designing ethical walls between AI-assisted and human-only processes
- Security access requirements for AI tools
- Training and certification program design
- Incident reporting procedures for AI errors, bias, and security events
- Vendor-specific guidance for major AI platforms
- Alignment assessment against EU AI Act Art. 4, ISO 42001, NIST AI RMF, ABA Model Rules,
  and applicable sector regulations

**Does not:**

- Provide legal advice or substitute for qualified legal review
- Replace a Data Protection Impact Assessment (DPIA) for high-risk AI processing
- Cover AI model development, procurement, or deployment governance (see
  `legalcode-ai-governance-framework-builder` for the broader governance framework)
- Apply to a single jurisdiction exclusively — jurisdiction-agnostic with
  [JURISDICTION-SPECIFIC] markers throughout

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Every organization operates under multiple
overlapping frameworks (employment law, data protection, professional licensing,
sector regulation) that vary significantly by jurisdiction. The skill identifies the
governing frameworks early and applies [JURISDICTION-SPECIFIC] markers throughout.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **EU/EEA**: EU AI Act Arts. 4 (AI literacy), 9–14 (high-risk AI obligations), 26
  (obligations of deployers), 50 (transparency obligations); GDPR Arts. 5–7, 13–14,
  22 (automated decision-making); national AI strategies and pending AI Liability Directive
- **United Kingdom**: UK AI Regulation pro-innovation principles (DSIT framework);
  UK GDPR / Data Protection Act 2018; ICO guidance on AI and data protection
- **United States (Federal)**: Executive Order 14110 (Safe, Secure, Trustworthy AI);
  NIST AI RMF 1.0 (2023); FTC Act unfair/deceptive practices guidance; EEOC guidance
  on AI in employment; banking/financial sector AI guidance (OCC, FDIC, Federal Reserve)
- **United States (States)**: Colorado AI Act (SB 24-205); Illinois AI Video Interview Act;
  California CPRA automated decision-making regulations; New York City Local Law 144
  (automated employment decision tools)
- **Professional Licensing (Legal)**: ABA Model Rules 1.1 (competence), 1.6
  (confidentiality), 5.1–5.3 (supervision), 3.3 (candor); state bar ethics opinions
  on lawyer AI use (Florida, California, Texas, New York, Virginia opinions)
- **Professional Licensing (Healthcare)**: HIPAA Security Rule; FDA AI/ML-Based Software as
  a Medical Device (SaMD) guidance; state medical board AI guidance
- **Financial Services**: SEC AI/ML guidance; FINRA Regulatory Notice 20-06; MAS guidelines;
  FCA/PRA AI model risk expectations

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The answer would change the direction of the policy design
- Multiple valid regulatory frameworks may apply
- The organization's risk appetite affects policy strictness
- The AI tool landscape creates policy design forks

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

Accept input in any of these formats:

- **Existing AUP**: A drafted or adopted AI acceptable use policy for gap analysis and
  review — submit as file, URL, or pasted text
- **Policy outline or scope**: Key decisions already made (approved tools, prohibited uses,
  industry) that should form the basis of a new AUP
- **Request to draft from scratch**: Provide organizational context (industry, size,
  jurisdictions, current AI tool landscape) and this skill will draft a complete AUP
- **Regulatory mapping request**: Ask which regulatory requirements apply to the
  organization's AI use and what each requires in a policy

If no input is provided, ask the user to supply one of the above.

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options where possible. Skip any already answered. Defaults for batch runs shown in
brackets.

1. **Primary goal**
   - Options: Draft new AUP from scratch, Review/gap-analyze existing AUP, Map
     regulatory requirements only, Update existing AUP for new tool adoption, Other
   - _Why this matters_: Determines whether the output is a new policy document, a gap
     analysis report, or a regulatory mapping.
   - Default: Draft new AUP from scratch

2. **Industry and sector**
   - Options: Legal services (law firm/in-house), Financial services (banking, insurance,
     investment), Healthcare/life sciences, Technology/software, Government/public sector,
     Education, Retail/consumer goods, Other
   - _Why this matters_: Determines which sector regulations apply, what special data
     categories are in scope, and what professional licensing ethics rules govern.
   - Default: General commercial organization

3. **Primary operating jurisdictions**
   - Options: EU/EEA only, US only, UK only, Global (multiple jurisdictions), Specific
     jurisdictions (user specifies)
   - _Why this matters_: Determines which regulatory frameworks are mandatory vs.
     aspirational, and where [JURISDICTION-SPECIFIC] content should be filled in.
   - Default: Global with [JURISDICTION-SPECIFIC] markers

4. **Current AI tool landscape**
   - Options: Using widely available commercial tools (ChatGPT, Claude, Copilot, Gemini),
     Using enterprise-licensed tools only, Using custom/proprietary AI systems, Mixed
     landscape (all of the above), Not yet assessed
   - _Why this matters_: Shapes the Approved Tool Registry design and vendor-specific
     guidance sections.
   - Default: Mixed landscape

5. **Risk tolerance**
   - Options: Conservative (restrict AI until proven safe), Moderate (permit AI with
     documented controls), Progressive (enable AI broadly with monitoring), Regulatory
     minimum only
   - _Why this matters_: Determines the strictness of the prohibited use definitions,
     data handling tiers, and required human oversight thresholds.
   - Default: Moderate

If the user provides partial context, state assumptions explicitly and proceed.

### Step 3: Load Existing AUP or Policy Context

If reviewing an existing AUP:

- Read the document in full
- Note: (a) date of adoption, (b) tools covered, (c) regulatory references cited,
  (d) missing sections, (e) definitions provided

If drafting from scratch:

- Note the organizational context from Step 2
- Use the core policy framework in Sections 1–12 below to structure the new policy
- Load any existing organizational policies that the AUP must align with (data protection
  policy, information security policy, IT acceptable use policy, HR handbook)

**⟁ CLARIFY** — If organizational policies are available for cross-reference, ask:
"Do you have existing organizational policies I should align with (data protection, IT
security, HR handbook)? If yes, please share them."
Default: Assume no existing policies available; flag alignment as a required next step.

### Step 4: Research Applicable Regulatory Requirements

Identify which regulatory frameworks apply based on Step 2 context. For each applicable
framework, map its specific requirements to AUP sections.

#### 4a. Core Cross-Jurisdictional Frameworks

| Framework                                   | Scope                              | Key AUP Requirement                                                             |
| ------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------- |
| **ISO 42001** (AI Management System)        | Voluntary; most jurisdictions      | AI governance policy; risk assessment; AI literacy program; incident management |
| **NIST AI RMF 1.0**                         | US-origin; widely adopted globally | Map/Measure/Manage/Govern functions → AUP governs the "Govern" function         |
| **OECD AI Principles** (2019, updated 2024) | 42+ countries                      | Transparency, accountability, human oversight, robustness                       |

#### 4b. Mandatory Jurisdiction-Specific Requirements

[JURISDICTION-SPECIFIC — EU/EEA]:

- **EU AI Act Art. 4**: Deployers must ensure employees have sufficient AI literacy for
  their role. **Effective from February 2, 2025** for all deployers (the first obligation
  to apply under the EU AI Act). Requires: literacy training programs calibrated to AI
  system complexity and role exposure; documentation of training activities. The
  obligation applies to all organizations deploying AI in the EU/EEA, including non-EU
  organizations with EU operations. [VERIFY against final implementing measures and EDPB
  guidance]
- **EU AI Act Art. 26**: Deployers of high-risk AI systems must: assign human oversight,
  conduct monitoring, document use, ensure fundamental rights impact assessments where
  required, suspend use if risks emerge
- **EU AI Act Art. 50**: Transparency obligations for certain AI systems (GPAI-generated
  synthetic content must be labeled as AI-generated; chatbot users must know they're
  interacting with AI)
- **GDPR Art. 22**: Right not to be subject to solely automated decision-making with
  legal or similarly significant effects without human review

[JURISDICTION-SPECIFIC — US]:

- **NIST AI RMF Govern 1.1–1.7**: Policies, processes, and procedures for AI risk
  management; accountability structures; documentation requirements
- **EEOC AI in Employment**: Disparate impact liability for employers using AI in
  employment decisions; reasonable accommodation obligations; mandatory human oversight
  for adverse employment decisions
- **State AI Laws** [VERIFY currency]: Colorado SB 24-205 (algorithmic discrimination
  in consequential decisions); Illinois AI Video Interview Act; NYC Local Law 144
  (automated employment decision tools — annual bias audits mandatory)

[JURISDICTION-SPECIFIC — Legal Profession (all jurisdictions)]:

- **ABA Formal Opinion 512 (2024)** — Primary authority for lawyer AI obligations.
  Maps AI use to existing Model Rules. Key holdings: (a) lawyers may NOT bill clients
  for time saved by AI efficiency as a pass-through cost; (b) all AI-generated citations
  must be independently verified; (c) client confidences must not enter consumer AI tools
  without adequate data protections; (d) supervising attorneys are responsible for
  subordinate and non-lawyer staff AI use. [VERIFY: jurisdiction may require review of
  applicable state bar opinion in addition to ABA guidance]
- **ABA Model Rule 1.1** (Competence): Maintaining competence includes understanding
  benefits and risks of relevant AI technology. Competent use of AI tools that generate
  legal research requires verification of citations. [VERIFY against your state bar]
- **ABA Model Rule 1.5** (Fees): Lawyers may not bill clients for AI time savings as
  separate charges. Efficiency gains from AI do not justify higher fees. Engagement
  letters and retainer agreements should address AI use and billing methodology. [VERIFY:
  ABA Formal Opinion 512; state bar billing opinions]
- **ABA Model Rule 1.6** (Confidentiality): Reasonable measures to prevent unauthorized
  disclosure of client confidences. Requires assessment of whether AI tool's data
  handling provides reasonable security; no input of client confidences into tools
  that train on inputs or retain data without adequate protections
- **ABA Model Rules 5.1–5.3** (Supervision): Supervising lawyer is responsible for
  competent use of AI by subordinates and non-lawyer staff

**legalcode-mcp** — If connected, search for:

- Current text of EU AI Act Arts. 4, 26, 50
- Recent state bar ethics opinions on AI in legal practice (FL, CA, TX, NY 2024-2025)
- ISO 42001 clause 6.1.2 (AI risk assessment requirements)

Save results to `/tmp/ai-aup-regulatory-research.md`. Mark all verified citations
`[VERIFIED — legalcode-mcp]`. Mark all unverified citations `[VERIFY]`.

**⟁ CLARIFY** — After mapping the regulatory frameworks:
"Based on your industry and jurisdictions, the following regulations appear mandatory:
[list]. Does this match your understanding? Are there sector-specific regulations not
listed that should be included?"
Default: Proceed with mapped regulations, mark all as [VERIFY].

### Step 5: Design the Approved AI Tool Registry

Build or review the Approved AI Tool Registry — the organization's catalog of AI tools
employees may use, with tier-based data-handling restrictions.

**Tool Tier System:**

| Tier        | Label                       | Definition                                                                                            | Default Data Restriction                                                         |
| ----------- | --------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Tier 1**  | Approved — Unrestricted     | Enterprise-licensed with DPA, no model training on inputs, data residency confirmed, SSO/MFA enforced | All data classifications up to organization's highest non-regulated tier         |
| **Tier 2**  | Approved — Restricted       | No enterprise agreement OR trains on inputs by default OR no confirmed data residency                 | Internal/non-sensitive data only; no PII, PHI, trade secrets, client confidences |
| **Tier 3**  | Tolerated — Read-Only Tasks | Free-tier or consumer-grade tools; no data protection agreement                                       | Public information only; no organizational data                                  |
| **Blocked** | Prohibited                  | Cannot satisfy data protection, security, or compliance requirements                                  | Prohibited from all use                                                          |

**Vendor-Specific Registry Starting Points** (as of research date; verify currency):

| Tool                   | Default Tier                             | Key Data Handling Notes                                                                                                                               | Enterprise Upgrade Available             |
| ---------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **ChatGPT (OpenAI)**   | Tier 2 (consumer) / Tier 1 (enterprise)  | Consumer: inputs may be used for model training unless opted out; Enterprise/API: no training on inputs by default, SOC 2 Type II, GDPR DPA available | Yes — ChatGPT Enterprise / Team          |
| **Claude (Anthropic)** | Tier 2 (consumer) / Tier 1 (enterprise)  | Consumer: inputs used to improve models unless opted out; Enterprise/API: no training on inputs, GDPR DPA available, SOC 2 Type II                    | Yes — Claude Enterprise / API            |
| **Microsoft Copilot**  | Tier 1 (M365 enterprise)                 | M365 Copilot: Microsoft 365 data boundary, no training on tenant data, GDPR compliant, existing M365 admin controls apply                             | Via M365 E3/E5 subscription              |
| **Google Gemini**      | Tier 2 (Workspace) / Tier 1 (Enterprise) | Workspace: data not used for model training in enterprise tier; Gemini Advanced (consumer): review current terms; Vertex AI: enterprise controls      | Yes — Google Workspace Enterprise        |
| **GitHub Copilot**     | Tier 1 (Business/Enterprise)             | Enterprise tier: no training on private code; Business tier: no training on private code if setting enabled; Individual tier: may use snippets        | Yes — GitHub Copilot Business/Enterprise |
| **Perplexity AI**      | Tier 3 (consumer)                        | No enterprise DPA widely available as of research; review current terms before organizational use                                                     | Check current availability               |

> ⚠️ **Vendor Terms Change Frequently** — The above reflects general understanding as of
> 2026-03. Verify current terms directly with each vendor before use. Data handling
> provisions, enterprise upgrade availability, and DPA terms can change without notice.
> Mark each entry [VERIFY — current vendor terms] in the registry.

**Registry Review Checklist for Each Tool:**

- [ ] Data processing agreement (DPA) or data handling addendum executed?
- [ ] Does the vendor train on organizational inputs by default?
- [ ] Is there a documented opt-out from training data use?
- [ ] Where is data stored? Is data residency in an acceptable jurisdiction?
- [ ] What are data retention and deletion provisions?
- [ ] Is SSO/MFA integration available and enforced?
- [ ] Does the vendor have SOC 2 Type II, ISO 27001, or equivalent attestation?
- [ ] Is there a process for employees to request addition of a new tool to the registry?
- [ ] How often is the registry reviewed and updated?

**⟁ CLARIFY** — Present the registry framework and ask:
"Which AI tools does your organization currently use? I'll assign each to a tier and
apply the appropriate data restrictions."
Default: Use the major vendor starting points above; recommend IT-led full audit as
implementation step.

### Step 6: Draft Prohibited Uses

Prohibited-use clauses define what employees may never do with AI tools, regardless of
which tool is used. Each prohibition should be grounded in a regulatory requirement,
professional obligation, or documented organizational risk.

**Core Prohibitions — Applicable Across Most Organizations:**

1. **High-risk automated decisions without human review**: Employees must not use AI
   tools to make final decisions (without qualified human review) on:
   - Employment matters: hiring, promotion, termination, performance evaluation [VERIFY:
     EEOC guidance; EU AI Act Annex III Item 4 (high-risk employment AI)]
   - Credit or lending decisions affecting consumer rights
   - Medical diagnosis or treatment recommendations
   - Legal advice or legal document finalization intended for client reliance
   - Law enforcement identification or surveillance [Prohibited under EU AI Act Arts. 5]
   - [JURISDICTION-SPECIFIC: add sector-specific high-stakes decisions]

2. **Input of highly regulated data without Tier 1 tool and DPA**: Employees must not
   input the following data categories into any AI tool below Tier 1 (or without explicit
   DPO approval):
   - Personal data (names + identifiers) of individuals [GDPR; CCPA/CPRA; PDPA; LGPD]
   - Protected health information (PHI) [HIPAA Security Rule; EU AI Act high-risk category]
   - Client confidential communications and legal advice (attorney-client privilege)
   - Attorney work product
   - Classified or national security information
   - Non-public material financial information (insider trading risk) [VERIFY: SEC; FINRA
     Regulatory Notice 20-06]
   - Trade secrets and confidential proprietary information

3. **AI-generated hallucinations as established fact**: Employees must not cite,
   represent, or submit AI-generated citations, case names, statutory references, or
   factual claims as verified without independent verification from authoritative sources.
   Applies especially to: legal filings and briefs, regulatory submissions, financial
   disclosures, published research or analysis [See ABA Rule 3.3 (candor); Fed. R. Civ.
   P. 11; EU AI Act Art. 26(1)(c)]

4. **AI-generated content representing human opinion without disclosure**: Employees must
   not submit AI-generated content as solely their own original opinion, expert judgment,
   or testimony in any context requiring individual professional responsibility (legal
   filings, medical notes, audit opinions, published articles)

5. **Biometric data processing for surveillance**: Employees must not use AI tools for
   real-time biometric identification or emotional recognition in the workplace without
   explicit legal authorization [EU AI Act Art. 5 (prohibited practices); BIPA (Illinois);
   GDPR Art. 9 (special categories)]

6. **Discriminatory AI use in employment**: Employees must not use AI tools to make
   employment decisions in ways that create unlawful disparate impact on protected classes
   without bias audit and compliance verification [EEOC; EU AI Act Annex III; NYCHRL]

7. **Unauthorized model fine-tuning or training on organizational data**: Employees must
   not submit organizational data to AI tools for the purpose of fine-tuning or training
   a model not controlled by the organization, unless expressly authorized by IT and Legal

8. **Undisclosed AI-generated client communications**: Employees must not send AI-generated
   content to clients, regulators, or courts without review, approval, and disclosure
   where required by professional rules or contractual obligations

9. **AI-generated legal advice without supervision**: Non-lawyers must not use AI tools
   to generate legal advice for external parties without attorney supervision [ABA Rules
   5.1–5.3; unauthorized practice of law statutes — [JURISDICTION-SPECIFIC]]

10. **Use of Blocked/Prohibited tools**: Employees must not use AI tools on the
    organization's Blocked list, even for personal use on organizational devices or
    networks. Using a personal device on organizational WiFi to access a Blocked tool
    is equally prohibited if organizational data is involved.

**Sector-Specific Additional Prohibitions:**

[JURISDICTION-SPECIFIC — Financial Services]:

- No AI-generated investment recommendations distributed to clients without suitability
  review, human oversight, and applicable disclosure [FINRA Rule 2111; MiFID II Article 25;
  VERIFY with current regulator guidance]
- No input of material non-public information (MNPI) into any AI tool — insider trading
  risk regardless of tool security [VERIFY: SEC Regulation FD; market abuse regimes]

[JURISDICTION-SPECIFIC — Healthcare]:

- No use of AI diagnostic tools on patient data without explicit physician review and
  documentation in patient record [VERIFY: FDA SaMD guidance; HIPAA; state medical
  board rules]
- No PHI input into AI tools without executed Business Associate Agreement (BAA) with
  vendor [HIPAA §164.308]

[JURISDICTION-SPECIFIC — Legal Profession]:

- No input of client confidences, privileged communications, or work product into any
  AI tool that has not been evaluated and approved through the firm's AI governance
  process [ABA Rule 1.6; state bar ethics opinions — VERIFY your jurisdiction]

### Step 7: Design Data Handling Rules

Create or review the organization's data handling matrix — the mapping of data
classifications to permitted AI tools and required safeguards.

**Data Classification Taxonomy:**

| Level       | Label                  | Examples                                                                                                                 | AI Tool Restriction                                              | Approval Required               |
| ----------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | ------------------------------- |
| **Level 0** | Public                 | Published press releases, public website content, publicly filed documents                                               | Any Tier 1–3 tool                                                | None                            |
| **Level 1** | Internal               | Internal memos, non-sensitive operational documents, internal presentations                                              | Tier 1 or Tier 2 only                                            | Manager awareness               |
| **Level 2** | Confidential           | Business strategy, unreleased product plans, supplier contracts, financial projections                                   | Tier 1 only (with DPA)                                           | Manager approval                |
| **Level 3** | Restricted — PII       | Personal data of employees or customers (names + identifiers, contact info, HR records)                                  | Tier 1 only (with DPA + DPIA where required)                     | DPO or Legal approval           |
| **Level 4** | Restricted — Regulated | PHI (HIPAA), special-category data (GDPR Art. 9), MNPI, privileged communications, trade secrets                         | Tier 1 only (with DPA + BAA/DPA as required + explicit approval) | C-suite or Legal + DPO sign-off |
| **Level 5** | Prohibited — Absolute  | Classified government information, certain export-controlled technical data, biometric data for real-time identification | No AI tool permitted                                             | N/A — contact Legal             |

**Data Handling Rules by Category:**

**For client confidences and legal privilege:**

- Never input into any AI tool unless: (a) the tool is Tier 1 with executed DPA, and
  (b) the responsible lawyer has assessed privilege preservation risk
- Document each instance of privileged material input into an AI tool in the matter file
- [JURISDICTION-SPECIFIC: some jurisdictions (UK, Australia) have specific rules on
  privilege and third-party AI systems — VERIFY]

**For personal data (PII/GDPR-regulated):**

- Conduct a DPIA before deploying any AI tool that processes personal data at scale
- Ensure a lawful basis under GDPR Art. 6 exists for AI-assisted processing [VERIFY]
- Data subjects have rights (access, erasure, portability) that extend to AI-processed data
- No automated-only decisions with legal effect without GDPR Art. 22 safeguards [VERIFY]

**For PHI (US healthcare):**

- BAA required with all AI tool vendors before any PHI is processed
- Minimum necessary standard applies to PHI inputs [HIPAA §164.514(d)]
- Document AI tool use in audit logs per HIPAA Security Rule [VERIFY]

**Cross-Border Data Transfers:**

- Verify AI tool data residency before inputting regulated data
- EU-to-US transfers require Standard Contractual Clauses (SCCs) or equivalent [VERIFY
  current transfer mechanism requirements post-Schrems II; EU-US Data Privacy Framework
  status]
- Some jurisdictions prohibit certain categories of data leaving the jurisdiction
  (China PIPL; Russia data localization; [JURISDICTION-SPECIFIC])

### Step 8: Draft Employee Obligations

Define employee-facing obligations in plain language suitable for policy publication.

**Verification and Accuracy Obligations:**

1. Review all AI-generated content before use or submission. AI tools produce plausible
   but potentially incorrect, incomplete, or outdated content.
2. Independently verify all legal citations, case names, statutory references, and
   factual claims generated by AI tools using authoritative primary sources before
   including them in any work product.
3. Document the verification steps taken for any AI-generated legal or regulatory content
   used in client-facing or regulatory submissions.
4. Never submit AI-generated content to a court, regulatory body, or opposing party
   without: (a) independent citation verification, (b) attorney review and signature,
   and (c) any disclosure required by applicable court rules.

**Disclosure Obligations:**

1. **Internal disclosure**: Disclose use of AI tools to your supervisor or team lead for
   any significant deliverable where AI was used in drafting, research, or analysis.
2. **Client disclosure**: Disclose use of AI tools to clients where required by engagement
   letter, client policy, professional ethics rules, or explicit client instruction. When
   in doubt, disclose. [JURISDICTION-SPECIFIC: some bar associations require disclosure
   of all AI use in legal representation — VERIFY your jurisdiction]
3. **Court/tribunal disclosure**: Follow applicable court rules and standing orders on AI
   disclosure. Certify compliance with any applicable AI disclosure requirement in
   filings. [JURISDICTION-SPECIFIC: many courts now have standing AI disclosure orders —
   VERIFY for each court/tribunal]
4. **Regulatory disclosure**: Disclose AI use to regulators where required by applicable
   regulatory guidance. [VERIFY applicable sector requirements]
5. **AI-generated content labeling**: Label AI-generated drafts, reports, or outputs
   as such (e.g., "AI-assisted draft — for review only") before circulating internally
   until final human review and approval is documented.

**Prompt Engineering and Data Input Obligations:**

1. Before entering any information into an AI tool, classify the data using the
   organization's Data Classification Taxonomy.
2. Enter only data at or below the restriction level of the tool's assigned tier.
3. Anonymize or pseudonymize personal data before input where feasible without defeating
   the purpose of the AI task.
4. Do not enter unnecessarily detailed personal information — use minimum necessary data.
5. Do not enter passwords, authentication credentials, API keys, or access tokens into
   AI chat interfaces.
6. Keep a brief record of prompts and outputs used in significant matters (e.g., save
   to matter file or project folder) to enable supervision, audit, and client disclosure.

**Competence and Judgment Obligations:**

1. Use AI tools only for tasks within your professional competence. Understand what the
   AI tool does and what it does not do before relying on its outputs.
2. Maintain your own professional judgment — do not treat AI outputs as authoritative
   or substitute for professional expertise.
3. Apply heightened scrutiny to AI outputs in areas where errors carry significant legal,
   financial, health, or reputational consequences.
4. Complete required AI literacy training before first use of approved tools and annually
   thereafter. Role-specific advanced training required for employees whose work involves
   frequent or high-stakes AI use.

### Step 9: Intellectual Property Considerations

Address IP ownership, copyright risk, and work product attribution for AI-assisted outputs.

**Copyright in AI-Generated Content:**

[JURISDICTION-SPECIFIC — United States]:

- Content generated entirely by AI without human creative authorship is not protected by
  copyright under current USPTO and Copyright Office guidance (2023–2024). This means:
  (a) the organization cannot own copyright in purely AI-generated work product, and
  (b) third parties cannot claim copyright infringement for using it.
- Content with sufficient human authorship is protectable, but only the human-authored
  elements. [VERIFY: ongoing Copyright Office proceedings on AI and authorship as of
  2025-2026; this area is actively developing]
- Practical implication: Where the organization relies on copyright to protect work product
  (software code, creative content, legal documents), ensure sufficient human creative
  contribution beyond editing or selecting AI outputs.

[JURISDICTION-SPECIFIC — EU/UK]:

- EU copyright law requires a human author for copyright protection; AI-generated works
  without human authorship are generally not protected [VERIFY: pending EU AI Act + EU
  Copyright Directive Art. 4 interaction; UK government AI copyright consultation 2024]
- Human-authored works that incorporate AI-generated elements may still be protected in
  the human-authored portions

**Training Data and Third-Party IP:**

- AI tools may have been trained on copyrighted material. Some vendors (Anthropic,
  Microsoft, Google, OpenAI) offer IP indemnification for enterprise customers in certain
  circumstances — [VERIFY: current indemnification scope and terms for each vendor before
  relying on it]
- Employees must not use AI tools to reproduce or closely paraphrase substantial portions
  of copyrighted third-party content in ways that could constitute infringement

**Assignment and Ownership:**

- Define in employment agreements and contractor agreements that work product produced
  with the assistance of AI tools is assigned to the organization to the extent it
  constitutes copyrightable work product [JURISDICTION-SPECIFIC: review applicable
  work-for-hire and assignment laws]
- Disclosure of material AI use in creating a patentable invention is required for patent
  applications — an AI system cannot be listed as an inventor under current law in most
  jurisdictions [VERIFY: USPTO AI inventorship guidance 2024; EPO decisions]

### Step 10: Security Requirements for AI Tool Access

Define technical and access security requirements for approved AI tool use.

**Access Control Requirements:**

- All Tier 1 AI tools must be accessed via Single Sign-On (SSO) integrated with
  organizational identity provider (IdP)
- Multi-factor authentication (MFA) is mandatory for all AI tool access on organizational
  accounts
- Individual employee accounts must be used — no shared accounts or credentials
- Role-based access control (RBAC) should restrict AI tool access to employees with
  documented business need and completed training
- AI tool access should be revoked within [24 hours / next business day] of employee
  departure or role change

**Network and Device Requirements:**

- Tier 1 and Tier 2 tools should be accessed from organizational devices on
  organizational networks or approved VPN
- Personal device use of Tier 1 tools with organizational data requires MDM enrollment
  and organizational account authentication
- Public WiFi networks must not be used to access AI tools containing organizational data
  above Level 1 (Internal)

**Data Residency and Sovereignty:**

- Confirm data residency region for each Tier 1 tool before approving for regulated data
- EU/EEA data must remain within EU/EEA or be protected by adequate transfer mechanism
  [JURISDICTION-SPECIFIC — VERIFY current GDPR transfer requirements]
- [JURISDICTION-SPECIFIC: China, Russia, and other data localization jurisdictions may
  require local data residency — VERIFY with local counsel]

**Logging and Monitoring:**

- Tier 1 tools must provide audit logs of employee access and data inputs sufficient to
  support an incident investigation
- Significant AI tool use in legal or regulated matters should be documented in matter
  files or audit trails
- IT must conduct quarterly reviews of AI tool access logs for anomalous behavior

**Shadow IT Prevention:**

> **Shadow AI Risk**: Research indicates that approximately 93% of employees share
> confidential data with unauthorized AI tools when no sanctioned alternative is
> available (Kiteworks research, 2024 [VERIFY]). This statistic underscores that
> permissive policy design with a clear sanctioned pathway reduces risk more effectively
> than blanket prohibition.

- IT must maintain a centralized inventory of all AI tools in use (sanctioned and
  detected unauthorized)
- DLP (Data Loss Prevention) controls should be configured to detect and alert on data
  being sent to unsanctioned AI tools where technically feasible
- Employees discovering unauthorized AI tool use must report it via the incident
  reporting channel

### Step 11: Ethical Walls and Human-Only Processes

Define the processes that require human decision-making and may not be delegated entirely
to AI.

**Human-in-the-Loop Requirements:**

The following decision categories require qualified human review, cannot be made by AI
alone, and must document the human decision-maker:

| Process Category                                                         | Human Review Requirement                                                                  | Documentation Required                                                       |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Employment decisions** (hiring, firing, promotion, performance rating) | Qualified HR professional and hiring manager final approval; AI may assist but not decide | Decision rationale with human reviewer identified; bias review documentation |
| **Legal advice to clients**                                              | Supervising attorney review of all AI-generated legal analysis before client delivery     | Matter file entry; reviewer signature or equivalent                          |
| **Legal filings and court submissions**                                  | Attorney review and signature; citation verification                                      | Independent citation check; filing certification per court rules             |
| **Medical diagnosis or treatment plans**                                 | Licensed physician review of AI-generated diagnostic support                              | Patient record entry; physician signature                                    |
| **Credit/lending decisions** (consumer)                                  | Human underwriter review for adverse actions; adverse action notice                       | Adverse action letter; underwriter review documentation                      |
| **Regulatory submissions**                                               | Qualified professional review before submission                                           | Review documentation; professional certification                             |
| **Termination of rights or contracts**                                   | Business decision-maker approval                                                          | Approval chain documentation                                                 |
| **GDPR/automated decision-making with legal effect**                     | Human review upon request; prior to adverse decision                                      | GDPR Art. 22 safeguards documented                                           |
| **High-value financial transactions**                                    | Qualified approver sign-off above threshold [define threshold]                            | Approval documentation per financial controls policy                         |
| **Disciplinary or grievance decisions**                                  | HR and management review                                                                  | Documentation per HR policy                                                  |

**Ethical Wall — AI-Assisted vs. Human-Only:**

Some processes within the organization may warrant complete exclusion of AI tools to
maintain confidentiality, privilege, or integrity:

- **Cross-matter conflicts of interest analysis**: To prevent cross-contamination of
  client data through shared AI tool interfaces, conflicts checks may require human-only
  processes or AI tools with explicit matter isolation. As of early 2026, AI-specific
  ethical wall enforcement is emerging as a technical category — e.g., Harvey/Intapp
  integration announced February 2026 for per-matter AI isolation in legal practice
  management platforms [VERIFY current platform capabilities; VERIFY applicable
  professional rules in your jurisdiction]
- **Whistleblower and grievance investigation**: Investigation of reports should limit AI
  tool use to minimize risk of processing sensitive personal data outside of protected
  channels
- **Board-level deliberations and privileged board communications**: Consider whether AI
  tools with shared data infrastructure should be excluded from board-level document
  drafting and communications
- [JURISDICTION-SPECIFIC: sector-specific ethical walls (e.g., Chinese Wall in financial
  services) may have AI-tool implications — VERIFY with compliance counsel]

### Step 12: Training and Certification

Define the required AI literacy training program.

**Training Tiers:**

| Tier                      | Audience                                               | Content                                                                                                               | Frequency                          | Certification                        |
| ------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------ |
| **Foundation**            | All employees                                          | AI basics, data classification, prohibited uses, incident reporting, tool tiers                                       | Annual; at onboarding              | Annual certification acknowledgment  |
| **Practitioner**          | Employees using AI for regular work tasks              | Deep tool training, prompt engineering best practices, verification techniques, IP and confidentiality implications   | At tool adoption; annual refresher | Tool-specific competence attestation |
| **Supervisor**            | Managers supervising AI-assisted work                  | Supervision obligations (ABA 5.1–5.3 equivalent), quality review of AI outputs, incident escalation                   | At role assumption; annual         | Supervisor-level certification       |
| **Advanced / Specialist** | Legal, compliance, data, security, AI governance roles | Regulatory deep-dive, risk assessment, DPIA, audit, incident investigation, advanced bias and hallucination detection | As needed; semi-annual             | Advanced certification or CPD credit |

**EU AI Act Art. 4 Compliance** [VERIFY against final implementing guidance]:

- Deployers must ensure their staff have sufficient AI literacy to use AI systems for
  their intended purpose and are aware of potential risks
- Document: (a) training program scope, (b) employees trained, (c) completion dates,
  (d) AI system categories covered, (e) competence assessments where conducted

**Practical Training Requirements:**

- Use case–specific walkthroughs (e.g., "How to use Claude for contract drafting — what
  to check, what not to input")
- Hallucination recognition exercises (e.g., review AI-generated research with planted
  false citations)
- Data classification exercises
- Incident recognition and reporting procedure walkthrough
- Role-play: when to escalate to Legal or IT
- External vendor training resources: leverage ChatGPT Enterprise training, Microsoft
  Copilot Adoption Hub, Anthropic Claude documentation

**Tracking and Enforcement:**

- Training completion tracked in LMS (Learning Management System) or equivalent
- Access to Tier 1 tools restricted until Foundation training certified
- Non-completion triggers HR escalation per existing performance policy
- Annual re-certification required to maintain Tier 1 tool access

### Step 13: Incident Reporting Procedures

Define how employees report AI-related incidents and how the organization responds.

**Incident Categories:**

| Category                                  | Examples                                                                                                                                                         | Severity                                                |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Type 1 — Data Incident**                | Accidentally inputted Level 3/4 data into wrong-tier tool; AI tool suffered a vendor data breach                                                                 | High — report within [24 hours]                         |
| **Type 2 — Output Error**                 | AI tool generated false legal citation submitted to court; AI-generated factual error included in regulatory filing; AI output contained PII from another matter | High — report within [24 hours]                         |
| **Type 3 — Bias/Discrimination Incident** | AI-assisted employment decision flagged for potential disparate impact; AI tool produced discriminatory output                                                   | High — report within [24 hours]; escalate to HR + Legal |
| **Type 4 — Security Incident**            | Unauthorized employee access to AI tool; credential compromise; AI tool used to exfiltrate data                                                                  | Critical — report immediately                           |
| **Type 5 — Compliance Incident**          | AI-generated content published without required disclosure; AI tool used in violation of court AI standing order                                                 | High — report within [24 hours]; escalate to Legal      |
| **Type 6 — Policy Violation**             | Employee used Blocked tool; AI tool used for prohibited purpose; no disclosure made for required disclosure                                                      | Medium — report within [48 hours]                       |
| **Type 7 — Near-Miss**                    | Employee caught a potential AI error before submission; employee stopped themselves from inputting regulated data                                                | Low — report through regular feedback channel           |

**Reporting Channels:**

- Primary: [Organization incident reporting system / email to AI.incidents@organization.com]
- Escalation: Legal and Compliance team
- Anonymized reporting: [Whistleblower hotline] for reports involving potential legal or
  ethics violations
- Vendor reporting: For vendor-side data breaches, follow vendor incident response
  procedure + notify DPO/Legal within 24 hours

**Response Procedure:**

1. Acknowledge receipt within [4 business hours]
2. Assess severity and assign category (Type 1–7)
3. For Type 1–4: convene AI Incident Response Team (Legal, IT, DPO, relevant business
   unit head) within [24 hours]
4. Preserve evidence: AI tool access logs, prompts, outputs, timestamps
5. Determine regulatory notification obligations (GDPR breach notification 72-hour clock;
   sector-specific requirements) [VERIFY applicable triggers and timelines]
6. Implement immediate containment: revoke access if security incident; preserve evidence
   if data incident
7. Root cause analysis within [10 business days]
8. Remediation plan and policy update if applicable
9. Retrospective report to AI Governance Committee
10. Employee follow-up: training, discipline, or recognition as appropriate

**Whistleblower Protections:**

- Employees reporting AI incidents in good faith shall not be subject to retaliation
- [JURISDICTION-SPECIFIC: EU Whistleblower Directive 2019/1937 requires formal reporting
  channels and protection for whistleblowers across member states — VERIFY transposition
  in your jurisdiction; US federal and state whistleblower statutes — VERIFY applicable
  statutes]

### Step 14: Accountability and Oversight

Define the governance structure that makes the AI AUP enforceable.

**AI Governance Roles:**

| Role                                      | Accountabilities                                                                                      | Reporting Line          |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------- |
| **AI Governance Lead / Chief AI Officer** | Policy ownership; tool registry maintenance; incident oversight; regulatory alignment                 | C-suite / Board         |
| **AI Committee** (cross-functional)       | Policy approval; high-risk use case review; annual policy review; breach escalation                   | Board / Audit Committee |
| **Data Protection Officer (DPO)**         | GDPR/data protection compliance; DPIA oversight; regulatory notification                              | Legal / Compliance      |
| **CISO / IT Security**                    | Tool security assessment; access controls; DLP monitoring; incident technical response                | CTO / COO               |
| **Legal / Compliance**                    | Professional ethics compliance; court rule compliance; regulatory monitoring; incident legal response | General Counsel         |
| **HR**                                    | Training program; policy enforcement; employment-decision AI oversight                                | CHRO                    |
| **Business Unit AI Champions**            | Embedded compliance; team training; incident first-response                                           | Business Unit Heads     |
| **Individual Employees**                  | Policy compliance; verification obligations; incident reporting                                       | Manager                 |

**Policy Enforcement:**

- Violations of this Policy may constitute a disciplinary offense under the organization's
  [HR/Employee Handbook] and may result in disciplinary action up to and including
  termination for serious or repeated violations
- Violations involving potential client harm, court rule violations, or regulatory
  breaches will be escalated to Legal and may result in mandatory external reporting
- [JURISDICTION-SPECIFIC: in the EU, deployers of high-risk AI systems may face regulatory
  enforcement action for non-compliance with EU AI Act — VERIFY]

**Annual Policy Review:**

- This Policy shall be reviewed at least annually, or more frequently when:
  - New AI tools are adopted at scale
  - New regulatory requirements take effect
  - A material AI incident occurs
  - AI platform terms of service materially change
- Review should be led by the AI Governance Lead with input from Legal, IT, DPO, and HR

---

## Severity Classification Framework

When reviewing an existing AI AUP (or assessing policy provisions), classify each element:

### GREEN — Aligned

Policy provision fully complies with applicable regulations, aligns with industry best
practice, creates enforceable obligations, and provides adequate operational guidance.
No material legal risk identified.

**Examples:**

- Prohibited-use clause cites specific regulatory authority (e.g., EU AI Act Art. 5)
- Data handling matrix distinguishes PII from PHI and applies tool-tier restrictions
- Training requirements reference EU AI Act Art. 4 and specify completion tracking

**Action**: Include as-is. Mark compliance status as VERIFIED. Note any routine
improvement opportunities.

### YELLOW — Gap or Weakness

Policy provision is directionally correct but has one or more of: missing regulatory
citation, incomplete coverage, operational ambiguity, no enforcement mechanism, or
requires jurisdiction-specific supplementation.

**Examples:**

- Prohibits AI for "sensitive decisions" without defining what is sensitive or which
  regulatory authority prohibits it
- Requires data classification before AI input but uses a classification taxonomy
  misaligned with GDPR special categories
- Training requirement exists but no completion tracking or consequence for non-completion
- Approved tool list exists but has no versioning, no update cadence, and no vendor DPA
  verification

**Action**: Flag with specific improvement recommendation. Provide revised language.
Assign remediation owner and timeline. Flag for legal counsel verification where
regulatory basis is uncertain.

### RED — Legal Gap or Enforceability Risk

Policy provision is missing, legally incorrect, creates enforceability problems, or
leaves the organization exposed to regulatory enforcement, professional discipline, or
liability.

**Examples:**

- No prohibition on inputting privileged communications into AI tools
- No process for lawyers to verify AI-generated citations before filing
- No GDPR Art. 22 safeguard for automated employment decisions
- No incident reporting procedure for data breaches via AI tool vendor
- Claims copyright ownership in entirely AI-generated work product without human
  authorship analysis

**Action**: Flag for immediate legal review. Do not publish policy with this gap.
Provide specific remediation language. Identify applicable regulatory authority.
Estimate exposure.

### PROHIBITED — Violates Law or Creates Liability

Policy provision would, if implemented, require or authorize employees to violate
applicable law, professional ethics rules, or fundamental rights.

**Examples:**

- Policy instructs employees to enter PHI into a tool without a BAA
- Policy states the organization owns copyright in all AI-generated outputs without
  qualification (may be false and deceptive to clients or employees)
- Policy permits real-time biometric identification AI in jurisdictions where this is
  banned under EU AI Act Art. 5

**Action**: Remove entirely before publication. Document removal decision with legal
basis. Escalate to General Counsel.

---

## Prioritization Framework

Prioritize AUP provisions and remediation items using these tiers:

### Tier 1 — Must-Have (Mandatory Baseline)

Provisions without which the organization faces near-certain regulatory non-compliance,
professional discipline risk, or material liability exposure:

- Prohibited-use clause covering high-risk automated decisions without human review
- Data handling rules for regulated data (PHI, PII, privileged communications)
- Incident reporting procedure for data incidents and output errors
- Employee verification obligation for AI-generated content
- Tool registry with at least Tier classification for the organization's most-used AI tools
- Training requirement with completion tracking for employees using AI tools
- EU AI Act Art. 4 literacy program (EU/EEA deployers) [VERIFY effective date and scope]

### Tier 2 — Should-Have (Strong Best Practice)

Provisions that significantly reduce risk and are expected by sophisticated clients,
regulators, and auditors:

- Vendor-specific guidance for each major AI platform in use
- Approved tool registry with DPA verification status for each tool
- IP ownership analysis for AI-generated work product
- Ethical walls and human-only process list
- Disclosure template for client-facing AI use disclosures
- Shadow IT detection and reporting procedure
- Quarterly access log review

### Tier 3 — Nice-to-Have (Advanced Maturity)

Provisions for organizations seeking mature AI governance or subject to heightened
regulatory scrutiny:

- Per-matter or per-project AI tool use tracking in matter management systems
- AI output quality auditing program (sampling and review of AI-generated deliverables)
- Third-party AI governance audit
- Regulatory-specific annexes (EU AI Act, NY Cyberspace Authority, etc.)
- ISO 42001 certification roadmap

---

## Quality Assurance Frameworks

### Citation Quality Gates

Run these 5 gates before delivering any regulatory analysis or policy provision. If any
gate fails, revise before delivering.

| Gate           | Rule                                                                                                                     | Fail Action                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Source**     | Every regulatory requirement cites a specific statute, regulation, or authoritative guidance document                    | Add citation or mark "[UNVERIFIED — counsel to confirm]"        |
| **Format**     | All citations use consistent, recognizable format for the jurisdiction (e.g., GDPR Art. 22(1); 29 U.S.C. § 1001)         | Fix format                                                      |
| **Currency**   | Every cited provision checked for amendments, repeal, or implementing guidance updates                                   | Flag "[CHECK CURRENCY — may have been amended]"                 |
| **Domain**     | Analysis stays within applicable jurisdictions; no assumption of universal applicability for jurisdiction-specific rules | Remove or mark with [JURISDICTION-SPECIFIC]                     |
| **Confidence** | Uncertainty explicitly stated; rapidly-evolving AI regulation areas flagged as developing                                | Add confidence qualifier; flag "[ACTIVELY DEVELOPING — verify]" |

### Self-Interrogation for RED or PROHIBITED Items

For any item classified as RED or PROHIBITED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited statute or regulatory guidance? Would a regulator or court actually reach this
conclusion? Is there a plausible counter-argument the organization could make?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and guidance documents
been considered? Are there sector-specific or jurisdiction-specific dimensions not yet
addressed? Are there recent developments (new AI regulations, new court AI disclosure
orders, new bar opinions) that affect the analysis?

**Pass 3 — Challenge**: What is the strongest argument that the policy provision IS
acceptable? Under what circumstances might a reasonable compliance professional accept
this gap? Is the RED classification proportionate, or is this actually YELLOW with
mitigations available?

Record in audit trail: `self_interrogation: "PASS / REVISED"`

### Confidence Scoring

| Level        | Range     | Meaning                                                                      | Action                                                   |
| ------------ | --------- | ---------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, enacted statute, clear regulatory requirement                   | State with confidence                                    |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions, recent regulatory guidance | State with brief caveat                                  |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ; actively developing area   | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities, pending legislation              | Flag for counsel review with both sides of the argument  |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative, contrary to prevailing authority                    | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

**AI Regulatory Note**: Because AI regulation is rapidly evolving, many provisions that
are Probable today (0.60–0.79) may become Definite (0.95+) within 12 months of new
regulation taking effect. Flag all actively-developing regulatory areas with
"[ACTIVELY DEVELOPING — verify before publication]".

### Glass Box Audit Trail

Include this YAML block in every AI AUP deliverable:

```yaml
glass_box:
  policy_type: "AI Acceptable Use Policy"
  mode: "[Drafted from scratch / Gap-analyzed from existing / Regulatory mapping only]"
  organization_type: "[financial services / healthcare / legal / technology / government / other]"
  ai_maturity_level: "[1 = No formal policy / 2 = Draft policy / 3 = Published policy / 4 = Monitored / 5 = Audited + certified]"
  jurisdictions_covered: "[list]"
  applicable_regulations:
    - "[EU AI Act Arts. 4, 26, 50 — VERIFIED/UNVERIFIED]"
    - "[ISO 42001 — VERIFIED/UNVERIFIED]"
    - "[NIST AI RMF — VERIFIED/UNVERIFIED]"
    - "[Sector-specific regulation — VERIFIED/UNVERIFIED]"
    - "[Data protection law — VERIFIED/UNVERIFIED]"
    - "[Professional ethics rules — VERIFIED/UNVERIFIED]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  policy_scope: "[employee headcount; tool categories covered; exclusions from scope]"
  approved_tool_registry_included: "Yes / No"
  approved_tools_count: "[number of tools with tier classification]"
  prohibited_use_categories: "[count]"
  data_classification_levels: "[count]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED/PROHIBITED items)"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Regulatory scope: which frameworks are NOT addressed]"
    - "[Tool coverage: which AI tools are NOT specifically covered]"
    - "[Jurisdiction gaps: which operating jurisdictions are NOT specifically addressed]"
    - "[Actively developing areas: list areas where law is developing]"
  reviewer: "AI-assisted — requires qualified legal counsel, DPO, and compliance review before publication"
  implementation_readiness: "[Draft Only / Stakeholder-Review-Ready / Publication-Ready]"
```

---

## Anti-Patterns

Avoid these common failures in AI acceptable use policy design:

1. **Blanket bans that create shadow IT** — Prohibiting all employee AI tool use without
   exceptions or an approved-tool path drives employees to use AI tools covertly, reducing
   organizational visibility and increasing risk. Balance prohibition with a clear
   sanctioned pathway.

2. **Tool-agnostic requirements without tool-specific guidance** — "Do not input
   confidential data" without identifying which tools are approved for which data classes
   is unenforceable and unworkable. Pair every prohibition with a specific operational
   pathway.

3. **Publishing without inventorying current shadow IT** — Drafting an AUP without first
   surveying what AI tools employees actually use results in a policy that immediately
   conflicts with reality. Survey current usage before drafting approved-tool tiers.

4. **Prohibited-use clauses without regulatory basis** — "AI may not be used for hiring
   decisions" without citing the EEOC guidance, state AI employment law, or EU AI Act
   Annex III loses credibility and enforceability. Every prohibition should cite its
   regulatory or business-risk basis.

5. **Disclosure obligations without defining the scope of "AI use"** — Does the disclosure
   obligation apply to generative AI only? All AI/ML? Auto-complete and spell-check? The
   policy must define the scope of the term "AI" it regulates or employees cannot
   self-comply.

6. **Data handling rules that conflict with vendor terms** — Requiring that "no vendor
   will use organizational data for training" when vendor T&Cs explicitly permit training
   use (unless opted out) creates an unenforceable gap. Reconcile policy rules with
   actual vendor T&Cs — or require enterprise upgrades that change the T&Cs.

7. **Training requirements without enforcement mechanics** — Mandating AI literacy training
   without: (a) tracking completion, (b) restricting tool access until trained, and
   (c) specifying consequences for non-completion creates a paper-only policy.

8. **Static approved-tool lists without a versioning or update process** — An approved
   list that is not updated when vendors change terms, new tools emerge, or security issues
   are discovered becomes dangerously misleading. Define review cadence and version control.

9. **Copyright ownership overclaiming** — Asserting organizational ownership of copyright
   in all AI-generated outputs ignores copyright office guidance that fully AI-generated
   content lacks copyright protection. This may deceive clients, investors, or employees
   about the value of AI-generated deliverables.

10. **Jurisdiction universalism — applying one policy to all jurisdictions without
    localization** — EU AI Act requirements differ materially from US requirements, and
    sector-specific rules vary by country. A policy that treats all jurisdictions as
    identical will be non-compliant in multiple locations simultaneously.

11. **Ignoring the legal privilege dimension** — Policies that address PII and PHI but
    omit attorney-client privilege and work product protection for legal services
    organizations expose the organization to professional discipline and privilege waiver
    risk.

12. **Human-in-the-loop provisions without defining who the human is** — "AI decisions
    require human review" without specifying the required qualifications, authority level,
    documentation requirement, and accountability creates illusory oversight.

13. **No safe harbor or reporting channel for good-faith AI incidents** — Employees who
    discover AI errors, bias, or data incidents will not report them if the policy only
    punishes violations without protecting good-faith reporters. Include incident reporting
    as a protected, encouraged activity.

14. **Failing to address vendor-side incidents** — An AI AUP focused only on employee
    obligations without provisions for responding to vendor data breaches or terms-of-service
    changes leaves a gap in the incident response framework.

15. **Publishing a policy but not operationalizing it** — The most comprehensive AUP
    creates no protection if employees have not been trained, tools have not been classified,
    access controls have not been implemented, and no one owns policy enforcement. An AUP
    is the beginning of an AI governance program, not the end of it.

---

## Writing Standards

Apply plain-language discipline to all output:

**For policy language (audience: all employees):**

- Plain language. Assume no legal background. Write at a 10th-grade reading level.
- Active voice: "You must not input trade secrets into any Tier 2 or Tier 3 tool" not
  "Trade secrets are prohibited from being entered into Tier 2 or Tier 3 tools"
- Short sentences. One rule per sentence.
- Name the actor: "Employees must...", "The AI Governance Lead must...", "IT must..."
- Specific, not vague: list concrete examples of prohibited inputs rather than abstract
  categories ("client names and contact information" not "personal data")

**For regulatory analysis and gap reports (audience: legal, compliance, and DPO):**

- Technical depth appropriate for qualified professional audience
- Plain-language summaries for executive stakeholders who are not lawyers
- Confidence qualifiers explicitly stated for all regulatory interpretations
- [VERIFY] and [ACTIVELY DEVELOPING] markers preserved throughout

**For training materials and implementation guides (audience: employees and managers):**

- Scenario-based examples (Q&A format): "Can I use ChatGPT to draft a client letter?
  It depends — see the data classification guide"
- Decision trees where helpful: "What tool tier am I using? → What data am I inputting?
  → Is this permitted?"
- Active voice emphasizing employee choice and responsibility: "You are responsible for
  verifying AI outputs"

**Quality gates before delivery:**

1. Can an employee with no legal background read the policy and know what to do?
2. Can IT and HR operationalize the policy without constant legal clarification?
3. Is every regulatory requirement backed by a specific citation (or marked [VERIFY])?
4. Are all examples concrete, realistic, and recognizable to the target organization?
5. Does any sentence exceed two lines? If yes, break it into shorter sentences.
6. Are any defined terms used before they are defined? If yes, restructure.
7. Are all [JURISDICTION-SPECIFIC] markers present for provisions that are not
   universally applicable?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current text of EU AI Act Arts. 4, 26, 50 and any implementing acts
- Search for recent state bar ethics opinions on AI use in legal practice
- Search for current GDPR guidance from EDPB on AI and automated decision-making
- Search for ISO 42001 clause-by-clause requirements
- Search for sector-specific regulatory AI guidance (OCC, FDIC, FINRA, FDA, etc.)
- Save results to `/tmp/ai-aup-regulatory-research.md`
- Mark all legalcode-mcp-sourced citations as [VERIFIED — legalcode-mcp]

**Without legalcode-mcp:**

- Use available web research for regulatory frameworks
- Mark all statutory and regulatory citations as [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus quality effort on structural completeness and operational clarity; note that
  regulatory citation verification requires manual legal review

**Alignment with `legalcode-ai-governance-framework-builder`:**

- The AI Governance Framework Builder (`skills/general/compliance/legalcode-ai-governance-framework-builder/SKILL.md`) covers the broader organizational AI governance program
- This AUP skill covers the employee-facing acceptable use layer only
- When using both skills: the governance framework sets organizational AI risk appetite;
  this AUP translates that appetite into enforceable employee obligations
- Cross-reference the governance framework's AI Maturity Model when assessing current
  state in Step 2

---

## Output Format Template

Structure the final deliverable in one of these formats depending on mode:

---

### Format A: New AI Acceptable Use Policy (Draft Document)

```markdown
# [Organization Name] AI Acceptable Use Policy

**Policy Version**: [1.0]
**Effective Date**: [Date]
**Policy Owner**: [AI Governance Lead / General Counsel]
**Review Date**: [Annual review date]
**Classification**: [Internal — All Employees]

---

## 1. Purpose and Scope

[1–2 paragraphs: why this policy exists; who it applies to; what AI tools it covers;
what it does not cover]

---

## 2. Definitions

| Term                 | Definition                                                            |
| -------------------- | --------------------------------------------------------------------- |
| **AI Tool**          | [definition of what counts as an AI tool for purposes of this policy] |
| **Generative AI**    | [...]                                                                 |
| **Approved AI Tool** | [...]                                                                 |
| **Level [X] Data**   | [...]                                                                 |

---

## 3. Approved AI Tools Registry

| Tool     | Vendor   | Tier   | Permitted Data Classification | Data Protection Agreement | Last Reviewed |
| -------- | -------- | ------ | ----------------------------- | ------------------------- | ------------- |
| [Tool 1] | [Vendor] | [Tier] | [Max level]                   | [DPA status]              | [Date]        |

---

## 4. Permitted Uses

[Organized by use case category]

---

## 5. Prohibited Uses

[Numbered list with regulatory basis for each prohibition]

---

## 6. Data Handling Rules

[Data classification matrix with tool tier mapping]

---

## 7. Employee Obligations

[Verification, disclosure, prompt engineering, competence obligations in plain language]

---

## 8. Intellectual Property

[IP ownership, copyright, assignment, patent inventorship guidance]

---

## 9. Security Requirements

[Access control, MFA, device and network requirements, logging]

---

## 10. Ethical Walls and Human-Only Processes

[Specific list of processes requiring human decision-making]

---

## 11. Training and Certification

[Required training by tier, completion tracking, access gating]

---

## 12. Incident Reporting

[How to report; categories; timelines; whistleblower protections]

---

## 13. Accountability

[Governance structure; enforcement; disciplinary consequences]

---

## 14. Policy Review

[Review frequency; trigger events; change process]

---

_This policy was AI-assisted in drafting. It has been reviewed by [Legal Counsel /
Compliance] before publication. It does not constitute legal advice._
```

---

### Format B: Gap Analysis Report (Existing AUP Review)

```markdown
## AI Acceptable Use Policy — Gap Analysis

**Policy Reviewed**: [Policy name and version]
**Organization**: [Name]
**Reviewer**: AI-assisted (legalcode-ai-acceptable-use-policy skill)
**Date of Analysis**: [Date]
**Regulatory Baseline**: [EU AI Act / ISO 42001 / NIST AI RMF / Sector-specific]
**Overall Assessment**: [GREEN / YELLOW / RED]
**Confidence Level**: [HIGH / MEDIUM / LOW]

---

## Executive Summary

[2–3 sentences: overall policy quality; top 3 gaps; recommended immediate actions]

---

## Regulatory Compliance Assessment

| Regulation                     | Applicable   | Requirement   | Addressed   | Status             | Notes |
| ------------------------------ | ------------ | ------------- | ----------- | ------------------ | ----- |
| EU AI Act Art. 4 (AI Literacy) | [Yes/No/N/A] | [requirement] | [Section X] | [GREEN/YELLOW/RED] | [...] |
| ISO 42001 Clause 6             | [...]        | [...]         | [...]       | [...]              | [...] |
| [Sector regulation]            | [...]        | [...]         | [...]       | [...]              | [...] |

---

## Section-by-Section Analysis

### [Section Name] — [GREEN / YELLOW / RED] | Confidence: [level]

**Policy says**: [summary of existing provision]
**Best practice / regulatory requirement**: [what is required or expected]
**Gap**: [description of shortfall, if any]
**Business/legal impact**: [consequences of the gap]
**Recommended language** (if YELLOW or RED):

> [Specific proposed policy language]

[Repeat for each section]

---

## Missing Sections

| Missing Section | Priority Tier | Regulatory Driver | Recommended Action |
| --------------- | ------------- | ----------------- | ------------------ |
| [Section]       | Tier [1/2/3]  | [Regulation]      | [Action]           |

---

## Implementation Roadmap

| Priority   | Action   | Owner  | Timeline | Regulatory Driver |
| ---------- | -------- | ------ | -------- | ----------------- |
| Immediate  | [action] | [role] | [date]   | [regulation]      |
| Short-term | [...]    | [...]  | [...]    | [...]             |

---

## Glass Box Audit Trail

[YAML block]
```

---

## Localization Notes

When localizing this skill for a specific jurisdiction:

**EU/EEA:**

- Replace [JURISDICTION-SPECIFIC — EU/EEA] markers with verified EU AI Act and GDPR
  citation text
- Add jurisdiction-specific data protection authority (DPA) reference and reporting
  procedures for each member state
- Include EU AI Act Art. 4 literacy obligation implementation plan
- Address EU AI Act Annex III high-risk AI system categories relevant to the organization

**United Kingdom:**

- Apply UK GDPR and Data Protection Act 2018 rather than EU GDPR (post-Brexit divergence)
- Reference ICO AI guidance and ICO DPIA guidance
- Reference UK government AI regulation framework (DSIT pro-innovation approach)
- Note: UK has not adopted the EU AI Act; check current UK AI regulation developments

**United States:**

- Select applicable state AI laws (Colorado SB 24-205, Illinois AIVPA, NYC Local Law 144)
- Apply EEOC AI in employment guidance
- Apply sector-specific frameworks (FRB/OCC/FDIC for banking; FDA for medical devices;
  FTC for consumer AI; SEC/FINRA for investment)
- Address state privacy laws (CCPA/CPRA; other state privacy laws) as applicable

**Legal Services (All Jurisdictions):**

- Replace [JURISDICTION-SPECIFIC — Legal Profession] markers with applicable bar ethics
  opinions for each jurisdiction where lawyers practice
- Privilege analysis should be reviewed by qualified local counsel for each jurisdiction

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis. Research sources:

- EU AI Act (Regulation (EU) 2024/1689) — primary source [VERIFY current status and
  implementing measures]
- NIST AI Risk Management Framework 1.0 (2023) — primary source
- ISO/IEC 42001:2023 (AI Management Systems) — primary source [VERIFY]
- ABA Model Rules of Professional Conduct (Rules 1.1, 1.6, 5.1–5.3) — primary source [VERIFY
  with applicable state bar]
- EEOC enforcement guidance on AI in employment — primary source [VERIFY currency]
- USPTO and US Copyright Office AI authorship guidance (2023–2024) — primary source [VERIFY
  latest guidance]
- Enterprise AI governance research: Liminal AI Governance Guide; DSIT AI Governance
  Framework; Responsible AI Labs knowledge hub — web research [VERIFY against authoritative
  sources]
- Structural patterns adapted from `legalcode-contract-review` and
  `legalcode-ai-governance-framework-builder` reference skills in this repository
