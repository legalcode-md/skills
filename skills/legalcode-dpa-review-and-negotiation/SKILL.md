---
name: legalcode-dpa-review-and-negotiation
description: Review and negotiate Data Processing Agreements (DPAs) clause-by-clause against GDPR Article
  28 mandatory requirements, UK GDPR equivalents, CCPA/CPRA service provider contract provisions, and
  LGPD operator obligations. Use when reviewing a DPA or data processing addendum from a vendor, SaaS
  provider, or sub-processor; when drafting or negotiating DPA terms as a controller, processor, or sub-processor;
  when auditing existing DPAs for compliance gaps; or when building a DPA review program across multiple
  regimes.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review and negotiate Data Processing Agreements (DPAs) clause-by-clause against GDPR Article 28 mandatory requirements, UK GDPR equivalents, CCPA/CPRA service provider contract provisions, and LGPD operator obligations. Covers subject matter and duration, nature and purpose of processing, data categories and data subject types, controller instructions mechanism, confidentiality of personnel, sub-processor controls (specific and general authorization), security obligations (Art. 32 / technical and organizational measures), data subject rights assistance, DPIA and prior-consultation support, breach notification requirements, audit rights, data return and deletion on termination, and international transfer mechanisms (EU SCCs, UK IDTA, adequacy decisions). GREEN/YELLOW/RED classification with confidence scores, redline suggestions, fallback positions, and negotiation priority tiers. Use when reviewing a DPA or data processing addendum from a vendor, SaaS provider, or sub-processor; when drafting or negotiating DPA terms as a controller, processor, or sub-processor; when auditing existing DPAs for compliance gaps; or when building a DPA review program across multiple regimes.


# Legalcode DPA Review and Negotiation

> **Disclaimer**: This skill provides a framework for AI-assisted Data Processing Agreement
> review and negotiation. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional or Data Protection Officer licensed or operating in the
> relevant jurisdiction before use. Privacy laws and regulatory guidance evolve; verify
> current applicability before relying on any requirement, deadline, or mechanism described
> here. Statutory and case law references cited from training data carry hallucination risk —
> verify against authoritative sources before relying on them. Mark any unverified citation
> with **[VERIFY]**.

---

## Purpose and Scope

This skill reviews existing Data Processing Agreements and data processing addenda against
the mandatory requirements of GDPR Article 28, UK GDPR, CCPA/CPRA service provider contract
provisions, and LGPD operator obligations. It identifies compliance gaps, classifies their
severity, generates actionable redline suggestions with fallback positions, and produces a
confidence-scored, auditable analysis.

**Covers:**

- Clause-by-clause analysis of any DPA or data processing addendum
- Role classification verification (controller/processor/sub-processor determination)
- Compliance gap classification (GREEN / YELLOW / RED)
- Redline generation with fallback positions for each gap
- Multi-regime coverage: EU GDPR, UK GDPR, CCPA/CPRA, and LGPD (Brazil)
- International transfer mechanism review (EU SCCs, UK IDTA, adequacy decisions, BCRs)
- Missing clause detection (items required by statute but absent from the DPA)
- Negotiation priority framework for controllers and processors
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new DPAs from scratch (see `gdpr-data-processing-addendum` for EU drafting)
- Provide legal advice or replace qualified DPO or counsel review
- Cover all global privacy regimes — focused on EU/UK/US(CA)/BR; see jurisdiction-specific
  skills for other regimes (PDPA Singapore, APPI Japan, Australia Privacy Act, etc.)
- Guarantee regulatory approval or exemption from enforcement
- Assess breach notification obligations (see `legalcode-breach-severity-assessment`)
- Conduct Data Protection Impact Assessments (see `legalcode-dpia-generator`)

**Related skills:**

- `legalcode-dsar-workflow-builder` — execute data subject access requests
- `legalcode-cross-border-transfer-assessment` — deep international transfer analysis
- `legalcode-breach-severity-assessment` — assess breach notification obligations
- `legalcode-dpia-generator` — generate Data Protection Impact Assessments
- `gdpr-data-processing-addendum` — draft EU GDPR DPAs from scratch

---

## Jurisdiction and Governing Law

This skill covers four major data processing regimes. The applicable regimes are identified
in Step 2 based on the parties' locations, the data subjects' locations, the nature of the
services, and the contract's governing law.

### Regime Overview

| Regime            | Primary Instrument                                            | Mandatory DPA?                 | Key Authority |
| ----------------- | ------------------------------------------------------------- | ------------------------------ | ------------- |
| **EU GDPR**       | Regulation (EU) 2016/679, Art. 28                             | Yes — controller/processor     | EDPB          |
| **UK GDPR**       | UK GDPR (retained EU law) + DPA 2018                          | Yes — mirrors EU GDPR Art. 28  | ICO           |
| **CCPA/CPRA**     | Cal. Civil Code §1798.100 et seq. + CPRA amendments           | Yes — for service providers    | CPPA          |
| **LGPD (Brazil)** | Lei Geral de Proteção de Dados (Law 13,709/2018), Arts. 37-39 | Required — operator agreements | ANPD          |

### Multi-Regime Applicability

A single DPA may need to satisfy multiple regimes simultaneously (e.g., a SaaS vendor
processing EU, UK, US, and Brazilian personal data). The review assesses each regime's
requirements independently, then identifies the intersection:

- **Baseline**: GDPR Art. 28 typically provides the highest-common-denominator requirements.
  A GDPR-compliant DPA often substantially satisfies LGPD and partially satisfies CCPA/CPRA.
- **Gaps remain**: CCPA/CPRA has unique prohibitions (sale/sharing, cross-context advertising)
  not covered by GDPR. UK GDPR requires UK-specific transfer mechanisms (IDTA) post-Brexit.
- **Addenda approach**: Many controllers use a GDPR-compliant base DPA with jurisdiction-
  specific addenda for UK, California, and Brazil data.

[JURISDICTION-SPECIFIC] For each regime in scope, identify any member-state or local
implementing legislation that imposes additional DPA requirements beyond the baseline
(e.g., German BDSG, French CNIL sector guidance, California CPRA regulations, ANPD
resolutions).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer changes the scope or direction of the analysis
- Party roles are ambiguous and role misclassification would materially affect the review
- The DPA involves multiple regimes and coverage priorities need to be set
- The user is on the controller or processor side (the entire analysis flips)

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

### Step 1: Accept the DPA

Accept the DPA or data processing addendum in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a DPA in a CLM, vendor portal, or cloud storage
- **Pasted text**: DPA text pasted directly into the conversation
- **Partial DPA**: Specific clauses or sections extracted from a larger agreement

If no DPA is provided, prompt the user to supply one. If only a master agreement is provided
without a data processing addendum, flag the absence as a potential RED gap and ask whether
personal data is being processed under the agreement.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present them as structured
options where possible:

1. **Which side are you on?**
   - Options: Controller reviewing a processor's DPA, Processor reviewing a controller's
     DPA requirements, Sub-processor reviewing a processor's flow-down DPA, Neutral review
     (auditing an existing DPA for compliance)
   - _Why this matters_: The analysis of acceptable vs. unacceptable terms differs
     fundamentally depending on which party bears which obligations. A controller wants
     strong audit rights; a processor may push back on unlimited audit scope.

2. **Which regimes apply?**
   - Options: EU GDPR only, UK GDPR only, Both EU and UK GDPR, CCPA/CPRA (California) also
     in scope, LGPD (Brazil) also in scope, All four regimes, Let me determine from the DPA
   - _Why this matters_: Determines which mandatory requirements to check the DPA against.
     Checking only EU GDPR on a DPA that also covers UK and California data leaves material
     gaps.

3. **Is this a new DPA (negotiation in progress) or an existing DPA (compliance audit)?**
   - Options: New DPA — negotiation in progress (maximize redlines), Existing DPA — audit
     for compliance gaps (identify gaps with remediation steps), DPA renewal — existing
     terms being updated
   - _Why this matters_: Negotiation mode generates redlines with fallback positions. Audit
     mode generates gap assessments with remediation timelines and escalation paths.

4. **Is there an existing playbook or standard DPA template your organization uses?**
   - Options: Yes — load from local settings, No — use GDPR Art. 28 and regime baselines,
     I'll describe our key positions during the review
   - _Why this matters_: Organization-specific positions (e.g., "we require 24-hour breach
     notification, not 72-hour" or "we never accept unlimited audit scope carve-outs") change
     the severity classification and redline posture.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly. Default assumptions: user is on controller side, EU GDPR applies, negotiation
mode, no playbook (use regulatory baselines).

### Step 3: Load the DPA Playbook

Check for an organization-specific DPA review playbook or standard positions in local
settings (e.g., `legal.local.md` or similar configuration files).

A DPA playbook should define:

- **Standard positions**: Preferred language for each major DPA clause type
- **Acceptable ranges**: Terms that can be accepted without escalation
- **Escalation triggers**: Terms requiring DPO, senior counsel, or executive sign-off
- **Approved sub-processor list**: Known approved sub-processors and their TOM certifications

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Proceed with regulatory baselines** — Use GDPR Art. 28, ICO guidance, CPPA
  regulations, and ANPD guidance as the minimum bar. Faster, but may not reflect the
  organization's specific risk appetite or negotiation positions.
- **Option B: I'll provide key positions as we go** — Start the review and pause at each
  major clause type to ask about the organization's preferred position.
- **Option C: Set up a baseline now** — Walk through defining standard positions for the
  10 highest-impact DPA clause types before reviewing. Takes time upfront; makes this and
  all future reviews more precise.

If proceeding without a playbook, label the review: "Based on regulatory baselines (GDPR
Art. 28 / ICO guidance / CPPA regulations / ANPD guidance) — not organizational positions."

### Step 4: Verify Party Roles

Before analyzing the DPA, verify that the controller/processor role assignment is legally
correct. Role misclassification is one of the most consequential DPA failures.

**⟁ CLARIFY** — If the DPA assigns roles that may not match the operational reality:

- "The DPA classifies [Party A] as the controller and [Party B] as the processor. Does
  [Party B] determine the purposes and means of processing, or does [Party A] retain sole
  control over those decisions? If [Party B] independently determines purposes, they may be
  a joint controller, not a processor — which requires a different legal instrument (Art.
  26, not Art. 28)."

Assess using the EDPB controller/processor criteria [VERIFY]:

- **Controller**: Determines purposes AND means of processing. Holds the lawful basis.
- **Processor**: Processes on documented instructions only. No independent purpose.
- **Joint controller**: Two or more parties jointly determine purposes and means. Requires
  Art. 26 arrangement, not Art. 28 DPA.
- **Independent controller**: Receives data for own purposes — no DPA, separate agreements
  with data subjects.

Flag role misclassification as RED — it is a foundational GDPR compliance failure.

### Step 5: Gather Jurisdiction-Relevant Legal Authority

Read the DPA's governing law clause and identify the applicable regimes. Then use
**legalcode-mcp** to build a working legal reference file.

**Research targets:**

1. Current EDPB guidelines on Art. 28 (EDPB Guidelines 07/2020 on controller/processor)
   [VERIFY]
2. ICO guidance on controller/processor contracts and IDTA requirements [VERIFY]
3. CPPA regulations on service provider and contractor contracts (11 CCR § 7051) [VERIFY]
4. ANPD resolutions and guidance on operator contracts under LGPD [VERIFY]
5. Applicable adequacy decisions and transfer mechanism status for the data flows in the DPA
6. Any relevant enforcement decisions or sector-specific guidance

Save the most relevant results to `/tmp/legalcode-dpa-authority.md`. Structure as:

```markdown
# Legal Authority Reference — DPA Review

## Date: [date]

## Regimes in scope: [list]

### EU GDPR Art. 28 Authority

- [Authority — VERIFIED (legalcode-mcp) or UNVERIFIED]

### UK GDPR Authority

- [Authority — VERIFIED or UNVERIFIED]

### CCPA/CPRA Authority

- [Authority — VERIFIED or UNVERIFIED]

### LGPD Authority

- [Authority — VERIFIED or UNVERIFIED]

### Transfer Mechanism Status

- [Transfer mechanism, current status — VERIFIED or UNVERIFIED]
```

**If legalcode-mcp is not connected:**

- Mark all statutory and regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with the analysis using general regulatory knowledge, flagging citations for
  independent verification

### Step 6: Clause-by-Clause Analysis

Analyze the DPA systematically against all 12 DPA clause categories below. Read the entire
DPA before flagging issues — clauses interact (e.g., a weak breach notification clause may
be partially mitigated by a strong security annex).

**⟁ CLARIFY** — For complex DPAs with multiple schedules, annexes, or cross-referenced
master agreements:

- Ask the user whether to perform a **full review** of all 12 categories or a **priority
  review** focused on the highest-risk categories for this specific relationship.
- If the DPA incorporates external documents (e.g., a security annex at a URL, or "subject
  to Processor's standard TOM annex"), ask whether the user wants those documents reviewed.
- For multi-party DPAs (e.g., a processor-to-sub-processor flow-down), confirm whether to
  review both the controller-processor layer and the sub-processor layer.

Cover all 12 clause categories. For each, assess against the applicable regime(s) and note
whether the clause is present, absent, or materially deficient.

| #   | Clause Category                              | Depth    | Key Review Points                                                                   |
| --- | -------------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| 1   | Subject Matter, Duration, Nature and Purpose | Deep     | Art. 28(3) preamble — specificity, processing scope, duration                       |
| 2   | Processing Instructions Mechanism            | Deep     | Art. 28(3)(a) — documented instructions, transfer restrictions, legality challenge  |
| 3   | Confidentiality of Personnel                 | Standard | Art. 28(3)(b) — contractual commitment, statutory obligation alternative            |
| 4   | Security of Processing                       | Deep     | Art. 28(3)(c) + Art. 32 — TOMs, encryption, pseudonymization, resilience, testing   |
| 5   | Sub-Processor Controls                       | Deep     | Art. 28(3)(d) + Art. 28(2) — authorization type, notification, objection, flow-down |
| 6   | Data Subject Rights Assistance               | Deep     | Art. 28(3)(e) + Arts. 12-22 — scope, timing, cost allocation                        |
| 7   | DPIA and Prior Consultation Support          | Standard | Art. 28(3)(f) — cooperation obligation, information provision                       |
| 8   | Breach Notification                          | Deep     | Art. 28(3)(f) + Art. 33 — timing, minimum content, remediation cooperation          |
| 9   | Audit Rights and Information Provision       | Deep     | Art. 28(3)(h) — inspection rights, third-party audit reliance, confidentiality      |
| 10  | Data Return or Deletion on Termination       | Deep     | Art. 28(3)(g) — choice, format, timeline, deletion certificate, backups             |
| 11  | International Transfer Mechanisms            | Deep     | Arts. 44-49 / UK IDTA — mechanism selection, adequacy, TIA, onward transfer         |
| 12  | Liability, Precedence, and Boilerplate       | Standard | Consistency with master agreement, liability structure, governing law               |

For CCPA/CPRA-scoped data: additionally review the CCPA/CPRA service provider provisions
(see **Section: CCPA/CPRA Service Provider Contract Analysis** below).

For LGPD-scoped data: additionally review the LGPD operator provisions (see **Section:
LGPD Operator Contract Analysis** below).

### Step 7: Missing Clause Detection

After analyzing present clauses, check for required provisions entirely absent from the
DPA. A missing mandatory clause is as serious as a deficient one.

For each of the 12 categories:

- If the clause category is entirely absent, flag it as potentially RED
- Assess whether the absence is acceptable (rare) or a compliance gap (common)
- Classify the absence as GREEN (not required here), YELLOW (recommended), or RED (required)

**Common missing clause failures:**

- No processing instructions mechanism — controller cannot demonstrate compliance (RED)
- No sub-processor notification mechanism — violates Art. 28(2) (RED)
- No breach notification provision — controller cannot meet Art. 33 72-hour deadline (RED)
- No data return/deletion clause — violates Art. 28(3)(g) (RED)
- No audit rights clause — Art. 28(3)(h) requires it (RED)
- No international transfer mechanism despite cross-border data flows (RED)
- No security clause / TOM annex — Art. 32 obligation cannot be assessed (RED)
- No data subject rights assistance provision — Art. 28(3)(e) requires it (YELLOW to RED)

**⟁ CLARIFY** — When a gap's severity depends on operational context not yet known:

- "The DPA has no international transfer mechanism. Does [Processor] process data outside
  the EEA/UK? If yes, this is RED. If all processing is within the EEA/UK, it may be
  unnecessary."
- "There is no security annex or TOM specification. Does this DPA incorporate security
  requirements by reference to a separate agreement or certification (e.g., ISO 27001 cert,
  SOC 2 Type II)? If yes, assess whether that incorporation is adequate."

### Step 8: Classify Deviations

Apply the three-tier classification system (defined in **Deviation Severity Classification**
below) to each gap or deficiency found. For each finding:

- **GREEN**: Note for awareness. No action required.
- **YELLOW**: Generate specific redline language, provide a fallback position, assess
  compliance impact of accepting as-is.
- **RED**: Explain the specific regulatory risk (citing the legal basis), provide
  compliant alternative language, assess enforcement exposure, and recommend remediation
  path.

**⟁ CLARIFY** — For borderline classifications, present both interpretations and ask:

- "The breach notification clause requires notification 'within a reasonable time.' This
  is ambiguous — it may or may not satisfy Art. 33's 72-hour window. Should I classify this
  as YELLOW (negotiate to specify 24 hours) or RED (non-compliant on its face)?"
- "The audit rights clause limits audits to once per year with 60 days' notice. This is
  common in the market but more restrictive than bare minimum. Is this acceptable for your
  organization, or should I flag it?"

### Step 9: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, confirm negotiation posture:

- **Relationship dynamic**: Is this a take-it-or-leave-it vendor DPA, a negotiable
  addendum, or a bilateral negotiation? Affects the tone and volume of redlines.
- **Volume decision**: If there are many YELLOW items, ask: "I've found [N] items worth
  negotiating. Do you want redlines for all of them, or focus on the top [X] by compliance
  impact?"

For each YELLOW and RED finding, generate a redline using the format in **Redline Format**
below.

### Step 10: Regime-Specific Gap Analysis

For each regime confirmed in scope (Step 2), run a targeted gap analysis using the regime-
specific checklists in the **Regime-Specific Analysis** sections below. Identify any gaps
not already caught in the clause-by-clause analysis.

### Step 11: Negotiation Priority and Remediation Summary

Provide a summary covering:

- **Overall compliance assessment**: HIGH / MEDIUM / LOW compliance against each applicable
  regime
- **Top 5 issues**: Most important gaps with severity, regime, and one-line summary
- **Negotiation strategy**: For negotiation mode — which issues to lead with, what to
  concede, how to sequence. For audit mode — remediation priorities with timelines.
- **Regime coverage gaps**: If the DPA does not address a regime that applies (e.g., no
  CCPA addendum despite California data subjects), flag it as a structural gap.

**⟁ CLARIFY** — If the business context would affect the strategy:

- "Can you walk away from this processor relationship, or is the service essential?"
- "Has your DPO already reviewed this DPA? If yes, are there specific provisions they
  flagged that I should prioritize?"

### Step 12: Quality Verification

Before delivering the analysis, run the quality checks defined in **Quality Assurance
Framework**:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 12 clause categories addressed (present or flagged absent).
5. Verify multi-regime coverage: confirm each applicable regime's requirements were checked.
6. Generate the Glass Box Audit Trail and append it to the output.

---

## Role Classification Reference

### Controller vs. Processor vs. Joint Controller Decision Tree

Use the following decision criteria (EDPB Guidelines 07/2020) [VERIFY]:

**Step 1 — Who determines the purpose of the processing?**

- One party alone determines purpose → that party is the controller; the other is a candidate
  processor or independent controller.
- Both parties together determine purpose → candidate joint controllers.
- One party is told the purpose by the other and merely executes → candidate processor.

**Step 2 — Who determines the means of processing?**

- Determining the "essential means" (which data, whose data, which legal basis, retention
  period, data subjects) → controller function. Even if the counterparty determines
  technical means, if the other party controls essential means, it is the controller.
- Determining only "non-essential means" (which software tool to use, technical
  implementation) → does not make a party a controller.

**Step 3 — Joint Controller Indicators**

- Both parties benefit from the processing outcomes
- Both parties independently use the same data for their own purposes
- The processing could not happen without both parties' active contribution
- Example: Facebook Ireland/Custom Audiences — CJEU C-210/16 [VERIFY]

**Consequences of role:**
| Role | Instrument | Key Obligation |
|------|-----------|----------------|
| Controller | GDPR Art. 6/9 legal basis | Must demonstrate lawful basis; responds to data subjects |
| Processor | GDPR Art. 28 DPA | Must act only on documented instructions |
| Joint Controller | GDPR Art. 26 arrangement | Must determine respective responsibilities by contract |
| Independent Controller | Direct privacy notice | No DPA; each has own obligations to data subjects |

---

## Clause Analysis Reference

### 1. Subject Matter, Duration, Nature, and Purpose

**Mandatory elements (GDPR Art. 28(3) preamble):**
The DPA must specify:

- Subject matter of the processing (what service gives rise to the processing)
- Duration of the processing (term of the DPA, aligned with main service term)
- Nature of the processing (what processing operations are performed)
- Purpose of the processing (why the processing is performed, as instructed by the controller)
- Type of personal data (categories of data being processed)
- Categories of data subjects (whose personal data is being processed)

**Common deficiencies:**

- [ ] Subject matter defined only as "providing the services" without reference to processing
      activities — too vague to be GDPR-compliant
- [ ] No duration specified, or duration is "indefinite" rather than aligned with the
      service term plus post-termination deletion period
- [ ] Purpose defined as "as required to provide the services" — circular, not independently
      verifiable
- [ ] Data categories listed at highest level only (e.g., "personal data") without any
      specificity about the types processed
- [ ] Data subject categories omitted or listed as "end users" without segmentation
      (customers, employees, prospects may all have different lawful bases)

**Red flags:**

- Purpose that grants the processor unlimited discretion to use data "for any lawful purpose"
- Data category description that includes special categories (health, biometric, children's
  data, etc.) without acknowledgment of the heightened sensitivity

[JURISDICTION-SPECIFIC] UK GDPR requires the same specificity. CCPA/CPRA requires the
contract to specify the "specific purposes" for which personal information is disclosed.
LGPD requires description of the processing activities and categories of personal data.

### 2. Processing Instructions Mechanism

**Mandatory elements (GDPR Art. 28(3)(a)):**
The processor must process personal data only on documented instructions from the controller.
The DPA must establish:

- The mechanism for issuing and recording instructions
- What constitutes a valid instruction (written, authorized personnel only, etc.)
- The processor's obligation to notify the controller if an instruction would violate
  applicable law — and the right to suspend processing if no response
- How transfers to third countries are handled in the instructions framework

**Common deficiencies:**

- [ ] Instructions mechanism is vague — no description of how instructions are issued
- [ ] No provision for the processor to challenge instructions on legality grounds
- [ ] Instructions can be oral — no written requirement
- [ ] No specification of which personnel can issue instructions (creates risk of
      unauthorized instructions)
- [ ] No "safety valve" — processor not required to notify controller of potentially
      unlawful instructions

**Red flags:**

- Processor has discretion to "interpret" or "expand" instructions where unclear, rather
  than reverting to the controller for clarification
- Instructions mechanism does not cover transfers — creates Art. 28(3)(a) gap for any
  cross-border routing

[JURISDICTION-SPECIFIC] UK GDPR equivalent: same. CCPA/CPRA equivalent: service provider
must process only for the "specified purposes" in the contract. LGPD Art. 39: operator
must process in accordance with controller's instructions.

### 3. Confidentiality of Personnel

**Mandatory elements (GDPR Art. 28(3)(b)):**
Persons authorized to process personal data must have committed to confidentiality or be
under a statutory obligation of confidentiality.

**Common deficiencies:**

- [ ] Clause requires confidentiality "of the processor" as an entity, not of individual
      authorized personnel — does not satisfy the requirement at the individual level
- [ ] Relies only on the processor's internal policies without contractual commitment
- [ ] No requirement for confidentiality obligation to survive employment termination
- [ ] Sub-processors excluded from the confidentiality personnel requirement

**Red flags:**

- No confidentiality obligation at all (RED — Art. 28(3)(b) is mandatory)
- Confidentiality limited to the DPA term only, not ongoing

### 4. Security of Processing

**Mandatory elements (GDPR Art. 28(3)(c) and Art. 32):**
The processor must implement appropriate technical and organizational measures (TOMs) to
ensure a level of security appropriate to the risk. The DPA must address:

- Pseudonymization and encryption of personal data (where appropriate)
- Ability to ensure ongoing confidentiality, integrity, availability, and resilience
- Ability to restore availability and access to personal data promptly after a physical
  or technical incident
- A process for regularly testing, assessing, and evaluating the effectiveness of TOMs

**Common deficiencies:**

- [ ] Security clause simply parrots Art. 32 language without specifying actual measures
      — vague obligation that does not constitute genuine compliance
- [ ] No security annex or TOM specification attached or incorporated
- [ ] Security standards referenced are aspirational, not binding (e.g., "processor will
      aim to maintain ISO 27001 certification" rather than "processor maintains ISO 27001")
- [ ] No obligation to update TOMs as the threat landscape evolves
- [ ] Testing and evaluation obligations absent
- [ ] No obligation to notify controller of material changes to security posture

**Red flags:**

- No security obligation at all in the DPA and no separate security agreement
- Security clause effectively excludes processor liability for security failures
- "Appropriate to the risk" without any reference to what risk assessment was performed
  or who determined the risk level

[JURISDICTION-SPECIFIC] UK GDPR equivalent: same (Art. 32 retained). CCPA/CPRA: service
provider must "implement reasonable security procedures and practices appropriate to the
nature of the personal information" (Cal. Civ. Code § 1798.150 [VERIFY]). LGPD Art. 46:
operators must adopt security measures to protect personal data.

### 5. Sub-Processor Controls

**Mandatory elements (GDPR Art. 28(2) and Art. 28(3)(d)):**
The processor must not engage a sub-processor without "prior specific or general written
authorisation of the controller." This requires:

**Specific authorization**: Controller approves each sub-processor by name before engagement.
**General authorization**: Controller provides blanket approval for a category or list of
sub-processors, BUT the processor must notify the controller of any intended changes (adding
or replacing sub-processors) and the controller has the right to object.

The DPA must also require the processor to:

- Impose the same data protection obligations on the sub-processor as in the Art. 28 DPA
- Remain fully liable to the controller for the sub-processor's performance

**Common deficiencies:**

- [ ] DPA uses general authorization but provides no notification mechanism for sub-processor
      changes — violates Art. 28(2)
- [ ] Notification period is too short (e.g., 5 days' notice before making a change) to
      allow meaningful objection
- [ ] Sub-processor list is not provided or is not accessible (DPA says "on request" only)
- [ ] Flow-down obligation is vague — does not require "the same" obligations, only
      "equivalent" or "similar" obligations
- [ ] No mechanism for objection — controller has no practical ability to prevent a
      sub-processor change
- [ ] Processor liability for sub-processor acts is disclaimed or limited
- [ ] International sub-processors included in the general authorization without specific
      transfer mechanism reference

**Red flags:**

- Blanket authorization for "any sub-processors the processor deems necessary" without any
  notification, list, or objection mechanism (RED — violates Art. 28(2) directly)
- Processor disclaims liability for sub-processor acts (RED — violates Art. 28(4))
- Sub-processors outside EEA/UK without any transfer mechanism reference

[JURISDICTION-SPECIFIC] CCPA/CPRA: service provider may not further disclose personal
information to a "third party" without contract containing equivalent restrictions (CPRA
§ 1798.140(ag) [VERIFY]). LGPD: operator must cooperate with controller in managing
sub-operator relationships.

### 6. Data Subject Rights Assistance

**Mandatory elements (GDPR Art. 28(3)(e) and Arts. 12-22):**
The processor must assist the controller with its obligation to respond to requests for
the exercise of data subjects' rights, including:

- Right of access (Art. 15)
- Right to rectification (Art. 16)
- Right to erasure ("right to be forgotten") (Art. 17)
- Right to restriction of processing (Art. 18)
- Right to data portability (Art. 20)
- Right to object (Art. 21)
- Rights related to automated decision-making (Art. 22)

**Common deficiencies:**

- [ ] Assistance obligation is vague — no timeline for processor to respond to rights
      assistance requests from the controller
- [ ] Assistance limited only to access requests, omitting erasure and restriction rights
- [ ] No mechanism — DPA states a duty but gives no practical procedure
- [ ] Cost allocation not addressed — who bears the cost of a burdensome DSAR that requires
      extensive processor search and retrieval?
- [ ] Data portability assistance not addressed for machine-readable export
- [ ] Processor may not be technically capable of the erasure it has agreed to perform —
      no attestation of technical capability

**Red flags:**

- No data subject rights assistance obligation whatsoever (YELLOW to RED)
- Assistance obligation is subject to "reasonable efforts" — potentially inadequate to
  meet tight regulatory deadlines

### 7. DPIA and Prior Consultation Support

**Mandatory elements (GDPR Art. 28(3)(f)):**
The processor must assist the controller with:

- Ensuring compliance with security obligations (Art. 32)
- Data Protection Impact Assessments (Art. 35)
- Prior consultation with supervisory authorities (Art. 36)

**Common deficiencies:**

- [ ] DPIA cooperation obligation is entirely absent
- [ ] Assistance is conditional on the processor's "reasonable commercial judgment" rather
      than triggered by the controller's legal obligations
- [ ] No obligation to provide the processor's own risk assessments, TOM documentation,
      or TIA to support the controller's DPIA

**Red flags:**

- Processor expressly disclaims obligation to support DPIAs or prior consultation
- Processor conditions DPIA support on additional fees without a cap or rate schedule

### 8. Breach Notification

**Mandatory elements (GDPR Art. 28(3)(f) and Art. 33):**
The processor must notify the controller "without undue delay" after becoming aware of a
personal data breach. The DPA must address:

- The notification trigger (processor's awareness of a breach)
- The notification timeline (must enable the controller to meet its 72-hour supervisory
  authority notification window; in practice, processors typically commit to 24-48 hours)
- Minimum notification content (nature, categories and approximate number of data subjects
  affected, categories and approximate number of records affected, DPO contact, likely
  consequences, measures taken or proposed)
- Cooperation obligations post-notification (investigation, remediation, regulatory
  correspondence)

**Common deficiencies:**

- [ ] Notification timeline is "within a reasonable time" or "as soon as reasonably
      practicable" — not specific enough to enable the controller to meet Art. 33 [VERIFY]
- [ ] Notification timeline is 72 hours or longer — leaves no buffer for the controller
      to assess and file its own notification
- [ ] Minimum notification content not specified — processor can satisfy the obligation
      with a one-line notice
- [ ] Cooperation obligations post-notification are vague or absent
- [ ] "Breach" is defined narrowly in the DPA (e.g., "confirmed" breach only, excluding
      suspected breaches from the trigger)
- [ ] No obligation to preserve forensic evidence
- [ ] Notification is subject to "materiality" or "significance" threshold that is not
      aligned with GDPR's risk-based trigger

**Red flags:**

- No breach notification obligation at all (RED — required by Art. 28(3)(f))
- Notification timeline longer than 48 hours (YELLOW — leaves controller with minimal
  headroom to meet 72-hour window)
- Breach definition excludes unauthorized access that the processor did not confirm
  (potential Art. 33 exposure for the controller)

[JURISDICTION-SPECIFIC] UK GDPR: same 72-hour supervisory authority deadline, but
notification goes to ICO. CCPA/CPRA: no equivalent processor breach notification
requirement in the statute, but processors typically commit to notification as a
contractual best practice. LGPD Art. 48: operators must notify the controller of security
incidents that may result in relevant risk within "a reasonable period" (ANPD Resolution
No. 2/2022 suggests 3 business days for initial notice to the ANPD) [VERIFY].

### 9. Audit Rights and Information Provision

**Mandatory elements (GDPR Art. 28(3)(h)):**
The processor must:

- Make available all information necessary to demonstrate compliance with Art. 28
- Allow for and contribute to audits and inspections conducted by the controller or a
  mandated auditor

**Common deficiencies:**

- [ ] "Information provision" obligation is limited to what the processor "considers
      relevant" — processor controls what evidence the controller sees
- [ ] Audit right exists on paper but is practically illusory — requires 90+ days' notice,
      limited to once per 3 years, cannot cover sub-processors
- [ ] Audit scope is limited to "compliance with this DPA" rather than including security
      posture, sub-processor controls, and TOMs
- [ ] Controller's audit right does not extend to sub-processors
- [ ] No provision for mandatory disclosure of third-party audit reports (ISO 27001, SOC 2)
      as an alternative to on-site audit
- [ ] Audit findings can be challenged by the processor without independent resolution
      mechanism
- [ ] Audit right is deleted or watered down in the main agreement without corresponding
      deletion here

**Red flags:**

- No audit right at all (RED — required by Art. 28(3)(h))
- Audit right that cannot be exercised in practice (effectively equivalent to no right)
- No third-party report alternative — controller must conduct expensive on-site audit with
  no substitution option

### 10. Data Return or Deletion on Termination

**Mandatory elements (GDPR Art. 28(3)(g)):**
At the controller's choice, the processor must:

- Delete or return all personal data to the controller after the end of the provision
  of services
- Delete existing copies, unless Union or Member State law requires storage

**Common deficiencies:**

- [ ] Controller's choice is removed — DPA unilaterally specifies deletion only (removing
      the right to receive the data back)
- [ ] Return format is not specified — data may be returned in an unusable format
- [ ] Timeline for deletion/return is vague or very long (e.g., "within a reasonable period"
      or "within 180 days")
- [ ] Backup and disaster recovery copies excluded from the deletion obligation without
      clear timeline for backup rotation
- [ ] No deletion certification required — controller cannot prove compliance
- [ ] Return condition omits data held by sub-processors — gap in coverage
- [ ] Legal retention carve-out is too broad — processor can retain "any data required
      by law" without specifying which laws or providing notice of what is retained

**Red flags:**

- No deletion/return provision at all (RED — required by Art. 28(3)(g))
- Processor retains a perpetual license to use the data after termination
- Deletion obligation does not cover backups (common weakness — often exploited)

### 11. International Transfer Mechanisms

**Mandatory elements (GDPR Arts. 44-49 / UK IDTA):**
Transfers of personal data to third countries require a lawful transfer mechanism:

- **Adequacy decision**: Commission/ICO has determined the receiving country provides
  adequate protection
- **Standard Contractual Clauses (EU SCCs)**: Commission Decision (EU) 2021/914 — new
  modular SCCs (replacing 2010 SCCs, which became invalid for new contracts after
  27 September 2021 [VERIFY])
- **UK IDTA**: UK International Data Transfer Agreement — required for UK data transfers
  since 21 March 2024 (old EU SCCs are no longer valid for UK-to-third-country transfers)
  [VERIFY]
- **UK Addendum**: UK Addendum to EU SCCs (alternative to standalone IDTA, combining the
  EU SCCs with a UK-specific addendum)
- **Binding Corporate Rules**: For intra-group transfers only
- **Derogations** (Art. 49): Explicit consent, necessary for performance, important public
  interest, legal claims, vital interests, public register — narrow and not suitable for
  systematic transfers

**Common deficiencies:**

- [ ] DPA grants global processing rights without specifying transfer mechanisms for non-EEA
      destinations
- [ ] Old EU SCCs (2010 decisions) still referenced — no longer valid for new processing
      [VERIFY]
- [ ] UK data flows governed only by EU SCCs without UK IDTA or Addendum — invalid since
      March 2024 [VERIFY]
- [ ] Transfer mechanism is referenced but not attached or incorporated by reference
- [ ] Module selection is incorrect (e.g., Controller-to-Controller SCCs used for a
      Controller-to-Processor relationship)
- [ ] No Transfer Impact Assessment (TIA) process referenced for high-risk destinations
- [ ] Adequacy decision relied upon for a jurisdiction where adequacy has been revoked or
      is under challenge (e.g., US Privacy Shield history [VERIFY])
- [ ] Sub-processors in non-adequate countries not covered by the transfer mechanism

**Red flags:**

- No transfer mechanism at all with cross-border processing ongoing (RED — GDPR Chapter V
  violation)
- Old EU SCCs (2010) still in use without transition provisions for new processing
- US-based sub-processors listed without transfer mechanism reference (common gap)
- Data flow map not attached — parties cannot determine which mechanisms apply to which flows

[JURISDICTION-SPECIFIC] UK transfers: UK IDTA or UK Addendum required. CCPA/CPRA: no
explicit transfer mechanism requirement equivalent to GDPR Chapter V — CCPA restricts use
of personal information rather than imposing transfer mechanism requirements. LGPD: transfer
mechanisms available include adequacy, contractual clauses, specific consent, and ANPD-
approved mechanisms (Arts. 33-36 LGPD) [VERIFY].

### 12. Liability, Precedence, and Boilerplate

**Key elements:**

- [ ] DPA defines its precedence over the main agreement for data protection matters
      (or the main agreement is defined as controlling — inconsistency is a gap)
- [ ] Liability structure in the DPA is consistent with the main agreement (e.g., if the
      main agreement caps liability, the DPA should state whether the cap applies to data
      protection failures and whether GDPR fines/supervisory authority costs are carved out)
- [ ] DPA term is aligned with the main service agreement (or longer if retention is needed)
- [ ] Governing law for the DPA is specified (and is consistent with applicable regimes)
- [ ] Amendment procedure is specified — how are sub-processor list updates and new annexes
      incorporated?

**Red flags:**

- DPA and main agreement have conflicting liability caps or limitations that leave ambiguity
  about what applies in the event of a data breach
- DPA excludes regulatory fines from the processor's liability — attempts to disclaim
  liability for GDPR Art. 83 fines that the controller suffers because of the processor's
  breach of the DPA [VERIFY whether such exclusions are effective]
- No governing law for the DPA — the instrument governing processing obligations may be
  applied differently than the parties intend

---

## Regime-Specific Analysis

### EU GDPR — Article 28 Completeness Checklist

The following Art. 28(3)(a)-(h) elements are mandatory. Each must be present and
substantively adequate:

| Requirement                                              | Art. 28(3) Para | Mandatory? | Status                             |
| -------------------------------------------------------- | --------------- | ---------- | ---------------------------------- |
| Process only on documented instructions                  | (a)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Instruction covers transfers to third countries          | (a)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Confidentiality of authorized personnel                  | (b)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Technical and organizational security measures (Art. 32) | (c)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Sub-processor: prior authorization                       | (d)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Sub-processor: same obligations imposed (flow-down)      | (d)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Sub-processor: processor remains liable                  | (4)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Assist with data subject rights (Arts. 12-22)            | (e)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Assist with Art. 32 security obligations                 | (f)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Assist with DPIAs (Art. 35)                              | (f)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Assist with prior consultation (Art. 36)                 | (f)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Delete or return data after end of services              | (g)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Provide information to demonstrate compliance            | (h)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |
| Allow and contribute to audits / inspections             | (h)             | YES        | ☐ Present / ☐ Absent / ☐ Deficient |

**Scoring**: 14 mandatory elements. Count of ABSENT + DEFICIENT determines overall
compliance posture:

- 0 gaps: HIGH COMPLIANCE
- 1-3 gaps: MEDIUM COMPLIANCE (address before next supervisory audit)
- 4+ gaps: LOW COMPLIANCE (material enforcement risk — remediate immediately)

### UK GDPR — Specific Differences

The UK GDPR mirrors EU GDPR Art. 28 in all substantive respects. Additional UK-specific
checks:

- [ ] Transfer mechanism for UK data: UK IDTA or UK Addendum to EU SCCs in place (not
      just EU SCCs, which became invalid for UK-to-third-country transfers on 21 March 2024)
      [VERIFY]
- [ ] ICO identified as the supervisory authority for UK data subjects (not EDPB)
- [ ] If DPA references "GDPR" without qualification, confirm whether it encompasses UK
      GDPR (i.e., does "GDPR" in the DPA include "UK GDPR"?)
- [ ] Data (Use and Access) Act 2025 (Royal Assent June 2025): check whether any DUA Act
      provisions affecting processor obligations have commenced and are reflected [VERIFY]
- [ ] Age of consent: 13 for UK (not 16 as in EU) — relevant if children's data is in scope
- [ ] If relying on adequacy for UK-to-EU transfers: EU-UK adequacy decision confirmed
      pending review (adequacy reviews scheduled) [VERIFY current status]

### CCPA/CPRA — Service Provider Contract Checklist

For California personal information in scope, the service provider contract must include
these mandatory prohibitions and obligations (Cal. Code Regs. tit. 11, § 7051) [VERIFY]:

| Requirement                                                                                         | CPRA Reg. / Statute | Status               |
| --------------------------------------------------------------------------------------------------- | ------------------- | -------------------- |
| Prohibition on selling or sharing personal information                                              | § 7051(a)(1)        | ☐ Present / ☐ Absent |
| Prohibition on retaining, using, or disclosing PI for any purpose other than the specified purposes | § 7051(a)(2)        | ☐ Present / ☐ Absent |
| Prohibition on retaining, using, or disclosing PI outside the direct business relationship          | § 7051(a)(3)        | ☐ Present / ☐ Absent |
| Prohibition on combining PI with PI from other sources (with exceptions)                            | § 7051(a)(4)        | ☐ Present / ☐ Absent |
| Business's right to take reasonable steps to ensure compliance                                      | § 7051(b)           | ☐ Present / ☐ Absent |
| Service provider must notify business if it cannot meet CCPA/CPRA obligations                       | § 7051(c)           | ☐ Present / ☐ Absent |
| Cooperation with consumer rights requests                                                           | § 7051(d)           | ☐ Present / ☐ Absent |
| Right to audit / inspect                                                                            | § 7051(e)           | ☐ Present / ☐ Absent |

**Additional CPRA considerations:**

- Sensitive personal information (SPI) restrictions — does the DPA address SPI separately?
- Opt-out rights for cross-context behavioral advertising — are restrictions specified?
- Data minimization and purpose limitation — explicit contractual acknowledgment?
- Breach notification to the business (contractual best practice, not strictly required
  by CCPA/CPRA but essential operationally)

### LGPD (Brazil) — Operator Contract Checklist

For Brazilian personal data in scope, the operator agreement must satisfy (Arts. 37-39, 46,
48 LGPD) [VERIFY with ANPD Resolution guidance]:

| Requirement                                                                    | LGPD Article              | Status               |
| ------------------------------------------------------------------------------ | ------------------------- | -------------------- |
| Written operator contract with description of processing activities            | Art. 37                   | ☐ Present / ☐ Absent |
| Operator processes only in accordance with controller's instructions           | Art. 39                   | ☐ Present / ☐ Absent |
| Security measures appropriate to protect personal data                         | Art. 46                   | ☐ Present / ☐ Absent |
| Security incident notification to controller (ANPD recommends 3 business days) | Art. 48                   | ☐ Present / ☐ Absent |
| Data return or deletion at end of services                                     | (Art. 39 / good practice) | ☐ Present / ☐ Absent |
| Operator remains liable to controller for failures                             | Art. 42(1)                | ☐ Present / ☐ Absent |
| Sub-operator provisions equivalent to processor flow-down                      | (Art. 39 / good practice) | ☐ Present / ☐ Absent |

**LGPD transfer considerations:**

- International transfers permitted to countries with adequate protection (ANPD adequacy
  list) or subject to contractual clauses based on ANPD model clauses [VERIFY]
- Standard contractual clauses approved by ANPD or specific binding corporate rules
- LGPD does not directly adopt EU SCCs — ANPD has its own mechanism framework [VERIFY]
- Note that LGPD Art. 33 requirements for international transfers may differ from GDPR
  Chapter V [VERIFY current ANPD adequacy decisions]

---

## Deviation Severity Classification

### GREEN — Compliant

The clause meets or exceeds the mandatory requirements of the applicable regime(s). Minor
variations that are commercially reasonable and do not reduce the level of protection.

**Examples:**

- Breach notification committed within 24 hours (exceeds GDPR 72-hour window — better
  than required)
- Sub-processor list updated monthly with 14 days' advance notice before changes (exceeds
  minimum requirement)
- Security annex specifies ISO 27001 certification plus SOC 2 Type II (exceeds Art. 32
  minimum)
- DPA has both EU SCCs and UK IDTA attached for cross-border transfers

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Partially Compliant (Negotiate)

The clause is present but falls below the mandatory standard or market best practice in a
way that creates regulatory risk or practical operational gaps. Requires attention and
likely negotiation but is not immediately fatal to the DPA.

**Examples:**

- Breach notification "within 72 hours" — technically possible to satisfy Art. 33 timeline
  but leaves controller no buffer time
- Sub-processor general authorization with 30-day notification period — notification
  period may be adequate but is on the short side of market practice
- Audit right exists but limited to "reasonable" scope — too vague to be operationally
  reliable
- Security clause references "industry-standard measures" without specifying what those are

**Action**: Generate specific redline language. Provide fallback position. Assess compliance
impact of accepting as-is.

### RED — Non-Compliant (Escalate)

The clause is absent, materially deficient, or affirmatively conflicts with mandatory
requirements. Creates immediate regulatory enforcement risk and requires remediation before
the DPA can be relied upon.

**Examples:**

- No breach notification obligation whatsoever
- Blanket sub-processor authorization with no notification mechanism
- No data return or deletion obligation on termination
- No audit rights clause at all
- Cross-border transfers with no mechanism (processing data in the US without EU SCCs,
  UK IDTA, or adequacy decision)
- Processor retains right to use data for own purposes after termination
- Role misclassification — parties labeled as controller/processor when facts suggest joint
  controllership

**Action**: Explain the specific regulatory risk (citing legal basis). Provide compliant
alternative language. Assess enforcement exposure (GDPR Art. 83: up to €10M or 2% of
global annual turnover [VERIFY]). Recommend remediation timeline.

---

## Redline Format

For each YELLOW or RED finding, generate a redline using this format:

```
**Clause**: [Section reference and clause title]
**Finding**: [YELLOW / RED — brief description of the gap]
**Regime(s)**: [EU GDPR Art. 28 / UK GDPR / CCPA/CPRA / LGPD]
**Current language**: "[Exact quote from the DPA, or 'ABSENT' if missing]"
**Proposed language**: "[Specific compliant alternative language, ready to insert]"
**Rationale**: [1-2 sentences explaining the gap and why the proposed language fixes it;
  suitable for sharing with the counterparty's counsel]
**Legal basis**: [Specific statutory provision, regulatory guidance, or principle]
**Confidence**: [Definite / High / Probable — per Confidence Scoring framework]
**Priority**: [Tier 1 Must-Have / Tier 2 Should-Have / Tier 3 Nice-to-Have]
**Fallback**: [Alternative position if primary redline is rejected; minimum acceptable language]
```

### Redline Best Practices

1. **Be specific**: Provide exact compliant language. A redline that says "add breach
   notification" without providing the language is not a redline — it is a comment.

2. **Reference the statute**: Every redline for a mandatory requirement must cite the
   specific provision. "GDPR Art. 28(3)(f) requires breach notification without undue
   delay" not "this may cause compliance issues."

3. **Offer a fallback**: If the primary redline is commercially aggressive (e.g., requesting
   24-hour breach notification), always offer a fallback (e.g., "48 hours at minimum").

4. **Distinguish mandatory from preferred**: Separate requirements that are mandatory by
   statute from those that represent best practice. A processor can agree to the mandatory
   floor; best practice is negotiable.

5. **Account for processor perspective**: Understand why the processor drafted the clause
   as it did. Broad sub-processor authorization exists because notification lists are
   operationally burdensome. Redlines that acknowledge the processor's concern while
   meeting regulatory requirements land better.

6. **Check for downstream consequences**: Redlining the breach notification clause may
   affect the liability clause. Tightening the audit rights may affect the security
   certification reliance clause. Review interactions before finalizing.

7. **Mark uncertain citations**: If the statutory reference is cited from memory rather
   than a verified source, mark it [VERIFY].

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Regulatory Non-Negotiables)

Issues where proceeding without resolution creates immediate regulatory enforcement risk.
The controller cannot sign the DPA without these:

- Missing or non-existent breach notification obligation (RED — Art. 28(3)(f) violation)
- No audit rights (RED — Art. 28(3)(h) violation)
- No deletion/return obligation on termination (RED — Art. 28(3)(g) violation)
- Blanket sub-processor authorization with no notification mechanism (RED — Art. 28(2))
- No processing instructions mechanism (RED — Art. 28(3)(a))
- Cross-border transfers without a lawful mechanism (RED — GDPR Chapter V violation)
- Role misclassification (RED — affects the entire legal framework of the agreement)
- CCPA/CPRA: No prohibition on selling or sharing personal information (RED)
- CCPA/CPRA: No restriction on use outside the business relationship (RED)

### Tier 2 — Should-Haves (Compliance Best Practice)

Issues that materially affect compliance posture but have negotiation room:

- Breach notification timeline of 72 hours or more (negotiate to 24-48 hours)
- Sub-processor notification period that is too short to allow meaningful objection
  (negotiate to 14-30 days)
- Security clause without specific TOMs or TOM annex (obtain security annex or
  certification evidence)
- Data subject rights assistance without a specified timeline or mechanism
- Deletion obligation that does not explicitly cover backups and sub-processor data
- DPIA cooperation obligation that is vague or conditional on additional fees
- International transfer without Transfer Impact Assessment process

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the compliance position but can be conceded strategically to secure
Tier 1 and Tier 2 wins:

- Audit frequency greater than once per year (negotiate down from three or more years)
- Security certifications beyond Art. 32 minimum (ISO 27001, SOC 2 Type II)
- Breach notification content that is more detailed than the regulatory minimum
- Sub-processor list updates more frequent than required
- Specific TOM standards that go beyond "appropriate to the risk"

**Negotiation strategy**: Lead with Tier 1 items — these are non-negotiable by law.
Explain to the counterparty's counsel that these provisions are legally required, not
organizational preferences. Trade Tier 3 concessions to secure Tier 2 wins. Never sign
a DPA that fails Tier 1 — the controller cannot cure a statutory violation by accepting
risk.

---

## Quality Assurance Framework

### PDCA Quality Cycle

Apply structured discipline to every DPA review:

**PLAN**: Identify the DPA, parties, applicable regimes, user's side, and playbook position.
Classify DPA type (Art. 28 standalone, addendum to SaaS agreement, processor-to-sub-
processor flow-down, multi-party arrangement). Identify which mandatory requirements apply
and what legal research is needed.

**DO**: Execute the clause-by-clause analysis and missing clause detection. Run regime-
specific checklists. Generate redlines. Classify severity.

**CHECK**: Run Citation Quality Gates. For any RED item, run the Self-Interrogation. Verify
all statutory references. Confirm all 12 clause categories addressed and all applicable
regime checklists completed.

**ACT**: Record any emerging DPA market practices noted during the review (e.g., new AI
data processing provisions, emerging ANPD guidance). Flag insights for playbook update.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                               | Fail Action                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Source**     | Every compliance assertion cites a specific statutory provision, regulation, or regulatory guidance                                | Add citation or mark as "[UNVERIFIED — DPO/counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., "GDPR Art. 28(3)(f)" not "Article 28")                               | Fix format                                                      |
| **Currency**   | Every cited provision checked against current text — GDPR not amended; but CPRA, DUA Act, ANPD resolutions may have recent changes | Flag "[CHECK CURRENCY — recent amendments possible]"            |
| **Domain**     | Analysis stays within the regime in scope. No cross-contamination between EU GDPR and CCPA/CPRA concepts without explicit flag     | Remove or flag regime bleed                                     |
| **Confidence** | Uncertainty explicitly stated, not hidden. If unsure whether a requirement is mandatory or best practice, say so                   | Add confidence qualifier                                        |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the compliance failure follow directly from the cited statutory provision?
- Is the absence or deficiency actually required to be in the DPA, or could it be in a
  separate instrument that satisfies the obligation?
- Is there a supervisory authority or court decision confirming this element is non-
  negotiable?

**Pass 2 — Completeness**:

- Has the DPA been read as a whole, including all annexes, schedules, and incorporated
  documents? Could the missing element be addressed elsewhere?
- Are there regime-specific exceptions that might permit the approach taken by the DPA?
- Have all relevant EDPB, ICO, CPPA, and ANPD guidance documents been considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause, as drafted, satisfies the requirement?
- Under what circumstances would a regulator accept this language during an audit?
- Is this RED because of clear statutory violation, or because it falls below best practice
  (which might be YELLOW rather than RED)?

If any pass reveals a weakness, revise the classification before delivery. Mark the audit
trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                 | Action                                                    |
| ------------ | --------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled requirement — clear statutory text, no interpretation dispute                   | State with confidence                                     |
| **High**     | 0.80-0.94 | Strong regulatory authority, minor questions about application to this fact pattern     | State with brief caveat                                   |
| **Probable** | 0.60-0.79 | Good regulatory guidance, but reasonable practitioners could disagree about application | State with reasoning and contra-indicators                |
| **Possible** | 0.40-0.59 | Genuinely uncertain — conflicting guidance, novel situation                             | Flag for DPO/counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                                                 | Do not assert; flag "[UNCERTAIN — DPO/counsel to advise]" |

---

## Glass Box Audit Trail

Every DPA review output MUST include a Glass Box audit section at the end. This makes the
reasoning traceable and defensible in regulatory correspondence:

```yaml
glass_box:
  dpa_name: "[DPA title and date]"
  dpa_type: "[Controller-Processor / Processor-Sub-processor / Multi-Party / Addendum]"
  user_side: "[Controller / Processor / Sub-processor / Neutral Audit]"
  regimes_in_scope:
    - "[EU GDPR / UK GDPR / CCPA/CPRA / LGPD — mark each confirmed in scope]"
  playbook_used: "[Playbook name / 'Regulatory baselines only']"
  mode: "[Negotiation / Compliance Audit / Renewal]"
  role_classification: "[Verified correct / Potential issue — [describe]]"
  clauses_reviewed: "[number of categories reviewed]"
  clauses_present: "[number]"
  clauses_absent: "[number] — [list]"
  mandatory_elements_checked: "[X of 14 EU GDPR Art. 28 elements]"
  eu_gdpr_compliance: "HIGH / MEDIUM / LOW — [number of gaps]"
  uk_gdpr_compliance: "[HIGH / MEDIUM / LOW / N/A]"
  ccpa_cpra_compliance: "[HIGH / MEDIUM / LOW / N/A]"
  lgpd_compliance: "[HIGH / MEDIUM / LOW / N/A]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[path to temp file / 'Not created']"
  statutes_consulted:
    - "GDPR Regulation (EU) 2016/679 Art. 28 — [VERIFIED (legalcode-mcp) / UNVERIFIED]"
    - "[Additional statutes as applicable]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no RED items)]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats about the review]"
  reviewer: "AI-assisted — requires qualified DPO or legal review before reliance"
```

---

## Multi-Stakeholder Mapping

A DPA analysis is not purely bilateral. Identify ALL affected stakeholders:

| Stakeholder             | Role        | Affected DPA Provisions                                     | Compliance Impact                              | Action Required                                |
| ----------------------- | ----------- | ----------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Controller              | Primary     | All                                                         | Primary — responsible to supervisory authority | Sign / Negotiate                               |
| Processor               | Primary     | All                                                         | Must comply with DPA obligations               | Sign / Negotiate                               |
| Data subjects           | Third party | Rights assistance, breach notification, transfer mechanisms | Indirect — rights depend on DPA adequacy       | None direct; ensure Art. 28(3)(e) adequate     |
| Sub-processors          | Third party | Sub-processor flow-down, transfer mechanisms                | Must receive equivalent obligations            | Sub-processor DPA required                     |
| Supervisory authority   | Regulator   | All — audit source                                          | Enforcement                                    | 72-hour breach notification; audit cooperation |
| Data Protection Officer | Internal    | All                                                         | Advisory / oversight                           | DPO sign-off before execution                  |
| Legal / compliance      | Internal    | All                                                         | Review and approval                            | Legal sign-off                                 |
| Procurement             | Internal    | Liability, precedence, commercial terms                     | Alignment with main agreement                  | Commercial review                              |

This mapping prevents the common failure of reviewing a DPA as a purely bilateral
document when it has regulatory, operational, and third-party consequences.

---

## Anti-Patterns

Explicit catalogue of what NOT to do in DPA review and negotiation:

1. **Treating all DPAs as equivalent** — A SaaS vendor DPA and a payroll processor DPA
   present very different risks and should be reviewed with different intensity. Apply risk-
   based prioritization: higher-risk processing (special categories, children's data, large-
   scale processing) warrants deeper review.

2. **Ignoring the operative reality of instructions** — The instructions mechanism must
   work in practice, not just on paper. A DPA that says "processor acts on documented
   instructions" but the service is fully automated with no instruction mechanism is
   non-compliant. Check how instructions are actually given and recorded operationally.

3. **Accepting "general authorization" for sub-processors without a list** — GDPR Art.
   28(2) requires general authorization to be accompanied by notification of changes and a
   right to object. A blanket authorization without a list or notification mechanism does
   not satisfy Art. 28. This is a frequent RED gap in SaaS vendor DPAs.

4. **Treating old EU SCCs as still valid** — The 2010 EU SCCs ceased to be available for
   new processing from 27 September 2021 and all processing from 27 December 2022 (EU law).
   For UK data transfers, old SCCs stopped being valid on 21 March 2024. Reviewing a DPA
   without checking SCC vintage is a material omission.

5. **Equating "industry standard security" with Art. 32 compliance** — "Industry standard"
   is not a legal standard. Art. 32 requires measures appropriate to the risk taking into
   account state of the art, implementation costs, and nature of the processing. Press for
   a specific TOM annex or certification rather than accepting vague security language.

6. **Overlooking the backup deletion gap** — Many DPAs state personal data will be deleted
   "within 30 days of termination" but have no provision for backup copies. Processors
   routinely retain backups for 90-180 days. If the DPA does not address backups explicitly,
   the deletion obligation is not effectively discharged.

7. **Accepting 72-hour breach notification** — While GDPR Art. 33 gives the controller 72
   hours to notify the supervisory authority, a processor commitment of 72 hours to notify
   the controller leaves no time for the controller to assess, investigate, and file. Best
   practice and market standard is 24-48 hours from processor to controller.

8. **Reviewing the DPA in isolation from the main agreement** — DPA liability caps,
   indemnification provisions, and limitation clauses must be checked against the main
   agreement. A strong DPA paired with a severely limited main agreement may effectively
   neutralize the DPA's protections.

9. **Confusing controller/processor with vendor/customer** — The controller/processor
   classification is a legal determination based on who determines purposes and means of
   processing. It does not map to commercial relationships: a vendor can be a controller
   (if it determines processing purposes), and a customer can be a processor (if it
   processes on behalf of its own customer's controller).

10. **Ignoring LGPD and CCPA/CPRA obligations in a GDPR-first review** — A GDPR-compliant
    DPA does not automatically satisfy CCPA/CPRA (which has unique prohibitions on sale/
    sharing of personal information) or LGPD (which has its own transfer mechanism
    requirements). A multi-regime assessment requires explicit coverage of each regime.

11. **Accepting audit rights that cannot be exercised in practice** — An audit right that
    requires 90 days' notice, is limited to once every three years, cannot be delegated to
    a third-party auditor, and cannot access sub-processors is an audit right in name only.
    Test audit rights for practical operability, not just textual presence.

12. **Failing to check the data flow map against the transfer mechanisms** — A DPA may have
    excellent transfer mechanism provisions but if the schedule does not accurately map
    which data flows to which countries under which mechanisms, the mechanisms cannot be
    relied upon. Annex I / the data flow map must be current and accurate.

13. **Not flagging special category data processing gaps** — If the DPA's data schedule
    includes health data, biometric data, criminal records, children's data, or other
    special category data (Art. 9 GDPR), the review should flag whether the DPA provides
    enhanced protection appropriate to the heightened sensitivity. Many DPAs treat all
    personal data identically regardless of sensitivity.

14. **Assuming deletion is equivalent to return** — Art. 28(3)(g) gives the controller a
    choice of deletion or return. Some processors' DPAs unilaterally specify deletion only,
    removing the controller's right to receive its data back in a usable format. This is a
    negotiation point, not a mandatory preference.

15. **Skipping the jurisdiction-specific checklists** — Running only the Art. 28 checklist
    when UK GDPR, CCPA/CPRA, and LGPD all apply leaves regime-specific gaps undetected.
    Each applicable regime's checklist must be completed independently.

16. **Not verifying the transfer mechanism module selection** — EU SCCs (2021 Decision) have
    four modules: C2C (Controller-to-Controller), C2P (Controller-to-Processor), P2C
    (Processor-to-Controller), P2P (Processor-to-Processor). Using the wrong module
    structurally invalidates the SCC. Verify the module matches the actual data flow
    relationship.

17. **Treating DPIA support as optional** — GDPR Art. 35 requires DPIAs for high-risk
    processing. The processor's obligation to cooperate with DPIAs is mandatory under
    Art. 28(3)(f). A DPA that conditions DPIA cooperation on additional fees or the
    processor's discretion effectively limits the controller's ability to comply with Art. 35.

---

## Writing Standards

Apply plain-language discipline to all DPA review outputs:

**For redline rationales** (shared with the counterparty's counsel):

- Plain language. No data protection jargon that the counterparty's non-legal staff cannot
  understand.
- Active voice: "Article 28(3)(f) requires the processor to notify the controller without
  undue delay" not "Notification is required under the applicable provision."
- Short sentences. One point per sentence.
- Name the actor: "The processor must..." not "It is required that..."
- Specific, not vague: cite the exact provision rather than "this may have compliance issues."

**For internal analysis**:

- Same plain-language standards
- May include more technical statutory analysis and cross-regime comparison
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can a non-lawyer DPO or compliance manager understand the executive summary?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every compliance assertion backed by a specific statutory provision (or flagged [VERIFY])?
4. Are any phrases vague or hedging? If yes, fix them.
5. Could any sentence be shorter without losing meaning? If yes, shorten.
6. Does the output distinguish clearly between EU GDPR, UK GDPR, CCPA/CPRA, and LGPD
   requirements? No cross-contamination of regime-specific concepts.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 5, search for current EDPB guidelines (particularly EDPB 07/2020 on controller/
  processor [VERIFY]), ICO DPA guidance, CPPA § 7051 regulations, and ANPD resolutions
- Search for current adequacy decision status for the data flows in the DPA
- Verify whether the EU SCCs version referenced in the DPA is the 2021 Decision (current)
  or the superseded 2010 decisions
- Verify UK IDTA requirements and the 21 March 2024 deadline for old SCC replacement
- For RED items, search for enforcement decisions and case law to support the classification
- Save research results to `/tmp/legalcode-dpa-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and regulatory guidance references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice that legal citations require independent verification by the
  DPO or qualified counsel
- Focus the analysis on structural and organizational gaps rather than legal certainty
  of specific interpretations
- Do not create the local authority reference file

**With a CLM or vendor management system connected:**

- Check whether this DPA has been previously reviewed and what the prior review found
- Check whether the processor is on an approved vendor list and what approval conditions apply
- Recommend whether the DPA should trigger a vendor risk assessment workflow

---

## Output Format Template

Structure the final DPA review deliverable as:

```markdown
## DPA Review Summary

**Document**: [DPA name/identifier]
**Parties**: [Controller: X] / [Processor: Y]
**Your Side**: [Controller / Processor / Auditor]
**Regimes in Scope**: [EU GDPR / UK GDPR / CCPA/CPRA / LGPD]
**Mode**: [Negotiation / Compliance Audit]
**Review Basis**: [Regulatory baselines / [Playbook name]]
**Date of Review**: [date]

---

## Key Findings

| Priority  | Clause   | Finding             | Regime   | Status                 |
| --------- | -------- | ------------------- | -------- | ---------------------- |
| 🔴 Tier 1 | [Clause] | [Brief description] | [Regime] | ABSENT / NON-COMPLIANT |
| 🟡 Tier 2 | [Clause] | [Brief description] | [Regime] | PARTIAL                |
| 🟢        | [Clause] | [Compliant note]    | [Regime] | COMPLIANT              |

---

## Overall Compliance Assessment

| Regime          | Compliance Level          | Mandatory Gaps | Critical Issues |
| --------------- | ------------------------- | -------------- | --------------- |
| EU GDPR Art. 28 | HIGH / MEDIUM / LOW       | [N of 14]      | [list]          |
| UK GDPR         | HIGH / MEDIUM / LOW / N/A | [N]            | [list]          |
| CCPA/CPRA       | HIGH / MEDIUM / LOW / N/A | [N]            | [list]          |
| LGPD            | HIGH / MEDIUM / LOW / N/A | [N]            | [list]          |

---

## Missing Mandatory Provisions

[List of required clauses absent from the DPA, with severity and regime basis]

---

## Clause-by-Clause Analysis

[For each of the 12 clause categories: present / absent / deficient + findings per regime]

### 1. Subject Matter, Duration, Nature and Purpose

**Status**: [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Finding**: [...]
**Redline** (if applicable): [...]

[Continue for all 12 categories...]

---

## Regime-Specific Gap Analysis

### EU GDPR Art. 28 Checklist

[Table from Regime-Specific Analysis section, completed]

### UK GDPR Specific Checks (if in scope)

[...]

### CCPA/CPRA Service Provider Checklist (if in scope)

[...]

### LGPD Operator Checklist (if in scope)

[...]

---

## Redlines

[For each YELLOW and RED item: full redline using Redline Format]

---

## Negotiation Priority Summary

**Tier 1 — Must-Haves (address before signing):**

1. [Issue 1 — Regime — brief description]

**Tier 2 — Should-Haves (negotiate):**

1. [Issue 1 — Regime — brief description]

**Tier 3 — Nice-to-Haves (concession candidates):**

1. [Issue 1 — brief description]

**Recommended approach**: [1-2 sentence negotiation strategy]

---

## Glass Box Audit Trail

[YAML block from Glass Box Audit Trail template, completed]
```

---

## Localization Notes

This skill is jurisdiction-aware with explicit multi-regime support. When extending to
additional regimes not covered by this skill:

- **PDPA (Singapore)**: For Singapore personal data processed by the operator, review the
  `singapore-pdpa-data-breach-notification-operations` skill and supplement the DPA review
  with PDPC guidance on data intermediary agreements [VERIFY].
- **APPI (Japan)**: For Japanese personal information, review the `japan-appi-personal-data-
breach-reporting-and-notification-operations` skill and check APPI Art. 24 requirements
  for outsourcing agreements [VERIFY].
- **Australian Privacy Act**: For Australian personal information, use the
  `australia-privacy-act-ndb-breach-notification-operations` skill and check APP 8 and
  contract requirements under the Privacy (Enhancing Online Safety) Act [VERIFY].
- **PIPEDA (Canada)**: For Canadian personal information processed by service providers,
  check PIPEDA Schedule 1 Principle 7 (safeguards) and PIPEDA contractual requirement for
  processors [VERIFY].
- **Member-state law**: EU member states may impose additional requirements beyond GDPR
  Art. 28 minimum in regulated sectors (financial services, health, telecoms). Check
  national implementing legislation for the controller's establishment jurisdiction.

---

## Provenance

Created by Legalcode on 2026-03-01. Legalcode original synthesis. Based on primary legal
sources: GDPR Regulation (EU) 2016/679 (particularly Art. 28), UK GDPR (retained EU law),
CPRA amendments to CCPA (Cal. Civ. Code § 1798.100 et seq.), LGPD (Lei 13,709/2018),
EDPB Guidelines 07/2020 on controller/processor concepts [VERIFY], ICO guidance on
controller/processor contracts [VERIFY], CPPA regulations (11 CCR § 7051) [VERIFY], ANPD
guidance on operator agreements [VERIFY], Commission Implementing Decision (EU) 2021/914
(new EU SCCs), and UK IDTA requirements. No external skill content imported. Reviewed
against the Legalcode 18-element quality standard.
