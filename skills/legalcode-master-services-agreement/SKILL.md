---
name: legalcode-master-services-agreement
description: >
  Draft and review Master Services Agreements (MSAs) with SOW/Order Form frameworks from
  both service provider and client perspectives — generate clause-by-clause guidance, flag
  market deviations, and produce auditable dual-perspective analysis with confidence-scored
  redlines. Use when drafting or negotiating MSAs, professional services agreements, managed
  services contracts, IT services agreements, consulting framework agreements, or any
  engagement model using a master agreement with modular statements of work or order forms.
  Covers scope of services and deliverables, pricing models (T&M, fixed-fee, milestone,
  hybrid), change order procedures, IP ownership and work-for-hire provisions, confidentiality,
  representations and warranties, liability caps, indemnification, insurance requirements,
  data protection, key personnel and subcontracting, termination for cause and convenience,
  transition/wind-down assistance, and governing law with dispute resolution. Includes SOW
  template and Order Form template as annexes. Jurisdiction-agnostic with localization markers
  for US, UK, and AU. Produces structured guidance with Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Master Services Agreement

> **Disclaimer**: This skill provides a framework for AI-assisted MSA drafting and review.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. IP assignment formality
> requirements, implied warranty terms, unfair contract terms rules, and data protection
> obligations vary materially across US, UK, and Australian law — verify jurisdiction-specific
> requirements against authoritative sources before finalizing any agreement. Statutory and
> case law references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

---

## Purpose and Scope

This skill drafts and reviews Master Services Agreements that allocate commercial, operational,
and compliance risk between a service provider and its client. It provides clause-by-clause
guidance from **both service provider and client perspectives**, identifies deviations from
market standards or organizational playbooks, and surfaces MSA-specific issues: SOW/Order Form
framework design, pricing model risk, change control, deliverables acceptance, IP ownership
and assignment formalities, key personnel obligations, transition assistance, and insurance
coverage.

**Covers:**
- Framework MSAs with modular Statements of Work (professional services: consulting, IT, creative)
- Framework MSAs with modular Order Forms (recurring services: managed services, outsourcing)
- Hybrid MSA/SOW/Order Form structures combining bespoke and recurring service lines
- Dual-perspective analysis: service-provider-favorable vs. client-favorable positions with redlines
- Pricing model analysis: T&M, fixed-fee, milestone-based, retainer, and hybrid pricing structures
- Change control procedures: bilateral, unilateral, and hybrid change order mechanisms
- IP ownership: foreground/background IP allocation, work-for-hire (US), assignment formalities (UK/AU)
- Acceptance testing: criteria definition, review periods, deemed acceptance, cure obligations
- Key personnel: naming requirements, replacement approval, IR35 and worker classification
- Insurance: professional indemnity, public liability, cyber, workers' compensation — market minimums
- Data protection: GDPR/UK GDPR/Australian Privacy Act obligations for processor/controller classification
- Termination: cause triggers, cure periods, convenience termination, termination fees
- Transition/wind-down: knowledge transfer, cooperation obligations, successor provider provisions
- Quality-verified output with Glass Box audit trail and confidence scoring

**Does not:**
- Draft SaaS/cloud subscription agreements (see `legalcode-saas-agreement-drafter`)
- Perform clause-by-clause review of any commercial agreement (see `legalcode-contract-review`)
- Replace specialized counsel for complex outsourcing, regulated-sector engagements (financial services,
  healthcare, government), or high-value strategic partnerships
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**
- `legalcode-saas-agreement-drafter` — for SaaS subscription and platform agreements
- `legalcode-contract-review` — clause-by-clause review of any commercial agreement
- `legalcode-nda-triage` — for screening standalone NDAs embedded in MSA schedules
- `legalcode-dpa-review-and-negotiation` — specialized DPA clause analysis under GDPR/UK GDPR/CCPA
- `legalcode-contract-risk-scorer` — quantified risk scoring of final MSA terms
- `legalcode-redline-generator` — standalone redline generation from analyzed positions

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The MSA's own governing law clause determines which legal
framework applies. The drafting process identifies the governing law early and adapts the analysis
accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States**
- IP ownership: Work-for-hire doctrine (17 U.S.C. § 101) — applies only to specific categories
  (works made within scope of employment, or nine categories of specially commissioned works
  where parties agree in writing). For software and most deliverables, a written assignment is
  required; "work-for-hire" language alone may be insufficient if the work does not qualify [VERIFY]
- Copyright assignment: must be in writing signed by assignor; no specific witnessing requirement
- UCC Article 2 applicability: courts are split on whether services-dominant contracts involve goods;
  predominantly services contracts are not subject to UCC Article 2 (apply common law) [VERIFY]
- CISG: applies by default to international sales between US and foreign commercial entities; commonly
  excluded by express opt-out in governing law clause
- Liability limitation: unconscionability doctrine (state law) constrains extreme exclusions; conspicuous
  form required for some warranty disclaimers under UCC §2-316 if goods are involved [VERIFY]
- Non-compete enforceability: state-specific — void in California (Cal. Bus. & Prof. Code § 16600),
  enforceable with limits in New York, Texas, and others [VERIFY]
- Arbitration: Federal Arbitration Act (9 U.S.C.) governs enforceability of arbitration agreements;
  class action waivers generally enforceable in commercial B2B contracts [VERIFY]

**United Kingdom**
- IP ownership: No work-for-hire doctrine. Copyright in contractor-created works belongs to the
  contractor by default unless assigned. Copyright assignment must be in writing signed by or
  on behalf of the assignor (Copyright, Designs and Patents Act 1988, s.90(3)). Design right
  assignment must also be in writing (CDPA 1988, s.222(3)). Patent assignment must be in writing
  signed by the assignor and assignee (Patents Act 1977, s.30(6)) [VERIFY]
- Moral rights: Cannot be assigned, only waived. Authors retain right of integrity and attribution
  (CDPA 1988, ss.77-85). Waiver must be in writing; blanket waivers are enforceable in B2B [VERIFY]
- Contractor vs employee: IR35 / off-payroll working rules (ITEPA 2003, Pt. 2, Ch. 8 and Ch. 10)
  — engaging contractors through personal service companies may trigger deemed employment status;
  medium/large clients bear responsibility for status determination from April 2021 [VERIFY]
- Limitation of liability: Unfair Contract Terms Act 1977 (UCTA) — in B2B contracts, exclusions
  must satisfy the reasonableness test (s.11 and Schedule 2). Death/personal injury exclusions
  are void (s.2(1)). Negligence exclusions require reasonableness (s.2(2)). Contracts Act 1999 —
  third-party rights may attach unless excluded [VERIFY]
- Governing law and dispute resolution: Civil Procedure Rules; no jury trials in commercial disputes;
  "loser pays" is the default costs principle; LCIA or ICC arbitration common for high-value disputes

**Australia**
- IP ownership: No work-for-hire doctrine for contractors. Copyright in contractor-created works
  belongs to the contractor unless assigned. Copyright assignment must be in writing (Copyright
  Act 1968, s.196(3)). Patent assignment must be in writing signed by assignor and assignee
  (Patents Act 1990, s.14) and should be registered with IP Australia [VERIFY]
- Unfair contract terms: Australian Consumer Law (Competition and Consumer Act 2010, Sch. 2)
  — small business contract unfair terms provisions (effective November 2023: definition of
  small business contract expanded; civil penalties introduced) [VERIFY]
- Privacy Act 1988: Australian Privacy Principles (APPs) apply to entities with annual turnover
  above AUD 3 million (and certain other entities). Notifiable Data Breaches (NDB) scheme —
  eligible data breaches must be notified to OAIC and affected individuals as soon as practicable
  [VERIFY]
- Warranty and implied terms: Australian Consumer Law consumer guarantees (s.60-64A) cannot be
  excluded for consumers. For B2B: implied fitness for purpose terms may apply if not excluded [VERIFY]
- Proportionate liability: Civil Liability Acts in most states limit joint and several liability for
  economic loss; proportionate liability schemes affect indemnity and contribution arrangements [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the user's
perspective or context, the workflow pauses and asks when:

- The answer changes which side's position to analyze (service provider vs. client)
- The service type (IT consulting, managed services, creative, outsourcing) affects clause priorities
- Pricing model (T&M, fixed-fee, milestone, hybrid) changes risk allocation analysis
- IP sensitivity requires jurisdiction-specific assignment formality guidance
- Regulatory context (GDPR, Australian Privacy Act, HIPAA) changes mandatory clause requirements
- Deal context (strategic partnership, commodity engagement, critical outsourcing) affects posture

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
- **Existing MSA** (PDF, DOCX, URL, or pasted text) for review, analysis, and redlines
- **Drafting request** ("Draft service-provider-side MSA for IT consulting" or "Draft customer-friendly
  managed services framework agreement")
- **SOW or Order Form request** ("Draft a fixed-fee SOW template" or "Create a T&M Order Form for
  ongoing support services")
- **Clause request** ("Draft a change control procedure with deemed approval" or "Draft a transition
  assistance clause for a 2-year managed services engagement")
- **Playbook review** ("Does our standard MSA protect us against IP ownership disputes on deliverables?")

If no input is provided, prompt the user to supply one.

### Step 2: Gather Perspective and Business Context

**⟁ CLARIFY** — Before beginning, ask:

1. **Which side are you on?**
   - Options: Service Provider / Vendor, Client / Customer, Both (analyzing for alignment or benchmarking)
   - *Why this matters*: Provider and client positions on IP ownership, liability caps, change control,
     acceptance, and payment terms are fundamentally opposed. The entire analysis flips.

2. **Service type?**
   - Options: IT / Technology Consulting, Managed Services / Outsourcing, Professional Services
     (legal, finance, strategy), Creative / Marketing Services, Software Development, Mixed / Multi-service
   - *Why this matters*: Service type affects IP sensitivity (highest in software/creative), change control
     complexity (highest in fixed-scope software), and insurance requirements (professional indemnity
     minimums vary by sector).

3. **Pricing model?**
   - Options: Time & Materials (T&M), Fixed-Fee / Lump Sum, Milestone-Based, Retainer, Hybrid (mixed)
   - *Why this matters*: T&M — client bears scope risk; provider bills actuals. Fixed-fee — provider bears
     cost risk; scope disputes create liability. Milestone — accountability structure changes acceptance
     obligations. Hybrid — requires careful SOW structure to avoid ambiguity.

4. **IP sensitivity?**
   - Options: High (software, code, creative works, product IP — custom-developed for client),
     Standard (reports, analyses, work product incorporated into client's business),
     Low (commoditized services, no bespoke deliverables)
   - *Why this matters*: High IP sensitivity triggers jurisdiction-specific assignment formality requirements,
     background IP protection, and moral rights waiver provisions.

5. **Regulatory scope?**
   - Options: GDPR / UK GDPR (EU/UK client or personal data flows), Australian Privacy Act (AU),
     HIPAA (US health data), CCPA (US/California), No identified data processing obligations, Not yet assessed
   - Allow multiple. *Why this matters*: Determines whether a Data Processing Agreement/Addendum is required,
     what breach notification timelines apply, and whether the provider is a data processor or controller.

6. **Deal context?**
   - Free text with examples: "5-year outsourcing deal — $10M value, provider has leverage,"
     "Startup client, first enterprise engagement," "Critical infrastructure migration — must-have provider,"
     "Commodity IT support — multiple providers competing"
   - *Why this matters*: Deal size, strategic importance, and negotiation leverage determine how hard to push
     and what to concede.

If partial context is provided, proceed with stated assumptions: "I'm assuming service-provider side,
IT consulting, T&M pricing, high IP sensitivity, GDPR scope. Let me know if that's wrong."

### Step 3: Load Playbook or Market Standards

Check for an organizational MSA playbook in local settings (e.g., `legal.local.md`).

The playbook should define:
- **Standard positions**: Preferred terms per clause (liability cap formula, IP ownership default,
  change control approval thresholds, insurance minimums, payment terms)
- **Acceptable ranges**: Terms that can be agreed without escalation (cap 6-24 months of fees,
  payment Net 30-60, key personnel replacement approval within 10-30 days)
- **Escalation triggers**: Terms requiring senior sign-off (uncapped liability, full IP assignment
  without license-back, unlimited subcontracting rights, no transition assistance)
- **Deal workflow**: Routing by deal size or risk level

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user and ask which approach:
- **Option A: Set up playbook now** — Define standard positions for 8 key MSA clauses (liability cap,
  IP ownership, change control threshold, key personnel approval, payment terms, termination notice,
  insurance minimums, data protection approach). More precise outputs; 15-20 minutes upfront.
- **Option B: Proceed with market standards** — Use widely-accepted market positions for the stated
  service type and deal size. Faster; may not reflect organizational preferences.
- **Option C: Provide positions as we go** — Start the analysis and ask about preferred position when
  it matters for each clause.

Label all output: "Based on [organizational playbook / professional services market standards]."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law (from the agreement or the user's drafting intent). Then use
**legalcode-mcp** to build a working legal reference for this analysis.

**⟁ CLARIFY** — If any of the following apply, ask the user:
- No governing law clause found → flag as RED and ask which jurisdiction applies
- Multiple conflicting governing law references → ask which governs the main body
- Unusual jurisdiction for the deal type → confirm intentional

**With legalcode-mcp connected (preferred):**
Search for jurisdiction-relevant authority covering:
- IP assignment formality requirements (CDPA s.90(3) UK; Copyright Act 1968 s.196(3) AU;
  17 U.S.C. § 101 work-for-hire categories US)
- Limitation of liability enforceability (UCTA 1977 reasonableness UK; ACL unfair terms AU;
  unconscionability doctrine US states)
- Data protection mandatory processing terms (GDPR Art. 28; UK GDPR; Australian Privacy Act APPs)
- IR35 / off-payroll working obligations (UK)
- Unfair contract terms for small business contracts (ACL Sch. 2 Part 2-3, AU)
- Implied terms that cannot be excluded (Supply of Goods and Services Act 1982 UK [VERIFY];
  ACL consumer guarantees AU for applicable contracts)
- Penalty clause enforceability (UK — rule against penalties post-*Cavendish Square* [VERIFY];
  AU — similar common law test)
- Proportionate liability schemes (state Civil Liability Acts, AU)

Save results to `/tmp/legalcode-msa-authority.md`. Mark all legalcode-mcp-sourced citations as
VERIFIED in Glass Box.

**Without legalcode-mcp:**
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`

### Step 5: Dual-Perspective Clause Analysis — All 16 Topic Areas

Read the entire MSA (and any incorporated SOWs, schedules, or Order Forms) before flagging issues.
Clauses interact: a low liability cap combined with an uncapped IP indemnity may leave the provider
exposed beyond expectations. Review holistically first, then clause-by-clause.

Analyze systematically across all 16 MSA topic areas (see **MSA Clause Architecture** below).
For each area, assess:

| Criterion | What to Evaluate |
|-----------|-----------------|
| **Presence** | Is this topic covered? Missing entirely? Addressed in a schedule or SOW? |
| **Perspective** | Does current language favor provider, client, or is it balanced? |
| **Market deviation** | How far is this from professional services market standard? |
| **Classification** | GREEN (acceptable), YELLOW (negotiate), RED (escalate) |
| **Compliance gap** | Does this clause create or cure a regulatory obligation? |

For each topic area, produce both a **service-provider-side assessment** and a **client-side
assessment**, noting where positions diverge.

**⟁ CLARIFY** — For complex agreements (30+ pages, multiple SOWs, or incorporated schedules):
- Ask whether to perform full analysis (all 16 topic areas) or priority review (stated focus areas
  plus all RED items)
- If the MSA incorporates documents by reference (SOW templates, rate cards, standard T&Cs),
  ask whether to include those in the analysis

### Step 6: Missing Clause and Gap Detection

After analyzing clauses present, identify material topics entirely absent from the agreement.

**Common MSA missing-clause issues:**

| Missing Clause | Provider Risk | Client Risk | Classification |
|----------------|--------------|-------------|----------------|
| No change control procedure | Scope creep, unpaid work | Uncontrolled cost escalation | RED (both) |
| No acceptance procedure | Dispute over completion | Subjective sign-off risk | RED (both) |
| No IP ownership clause | Default rules apply (may favor provider) | Client may not own deliverables | RED (client), YELLOW (provider) |
| No liability cap | Unlimited exposure | Potentially unrecoverable loss | RED (provider), YELLOW (client) |
| No DPA when GDPR/AU Privacy Act applies | Regulatory fine | Regulatory fine | RED (both) |
| No key personnel clause (critical engagement) | Loss of client relationship | Unplanned resource changes | YELLOW–RED |
| No transition assistance | Harmful exit scenario | Lock-in risk | RED (client), YELLOW (provider) |
| No background IP protection | Background IP exposed to assignment | May receive narrower-than-needed license | RED (provider) |
| No subcontracting restriction | Client uncertain who performs work | Quality and confidentiality risk | YELLOW |
| No force majeure | No relief for unforeseeable events | No relief for unforeseeable events | YELLOW (both) |

**⟁ CLARIFY** — When missing clause severity depends on context:
- "No change control procedure found. Is this a fixed-fee or T&M engagement? If fixed-fee, this is RED."
- "No acceptance criteria in the SOW. Are deliverables clearly defined elsewhere? If not, both parties
  lack a mechanism to close out the engagement."
- "No DPA found. Will the provider process personal data covered by GDPR, UK GDPR, or the Australian
  Privacy Act? If yes, this is RED."

### Step 7: Flag Deviations Using Three-Tier Classification

For each deviation from playbook or market standard, classify using the **Deviation Severity
Classification** below. For each:

- **GREEN**: Note for awareness; no action required.
- **YELLOW**: Generate specific redline language with fallback position; estimate business impact.
- **RED**: Explain the specific risk (with legal basis where verifiable), provide market-standard
  alternative language, estimate exposure, recommend escalation.

**⟁ CLARIFY** — For borderline classifications:
- **YELLOW vs. RED**: "The liability cap is set at 3 months' fees. For a 2-year engagement, this
  is well below market standard. Should I classify as YELLOW (negotiate) or RED (escalate)?
  Depends on your risk tolerance and whether there are uncapped indemnities."
- **GREEN vs. YELLOW**: "IP ownership defaults to the provider unless deliverables are assigned.
  This is standard in the UK (no work-for-hire doctrine), but the client may expect ownership.
  Is this a concern?"

### Step 8: Generate Guidance with Redlines

For each YELLOW and RED deviation, generate guidance using the **Redline Format** below.
Before generating redlines:

**⟁ CLARIFY** — Ask about negotiation posture if not already clear:
- **Relationship dynamic**: New client relationship, repeat engagement, or sole-source essential
  provider? Affects tone.
- **Volume of redlines**: If many YELLOW items exist: "I've found [N] items worth negotiating.
  Do you want guidance on all of them, or focus on the top [X] highest-impact?"

### Step 9: Perspective-Flip Analysis

For each material clause (YELLOW/RED), include a parallel analysis for the opposing perspective:

- **Provider-side analysis**: "Client will likely push back on this because..."
- **Client-side analysis**: "Provider will typically resist this because..."

This prevents preparing a negotiation position without understanding the counterparty's legitimate concerns.

### Step 10: SOW / Order Form Framework Review

If an SOW or Order Form is provided or requested, apply the **SOW Completeness Checklist** and
**Order Form Completeness Checklist** from the Annex Templates section. For each element:
- Present: assess quality and clarity
- Absent: classify as REQUIRED, RECOMMENDED, or OPTIONAL for the stated service type and pricing model

**⟁ CLARIFY** — If the SOW uses fixed-fee pricing but lacks acceptance criteria:
- "This is a fixed-fee SOW with no acceptance criteria. Without defined acceptance triggers, the
  provider risks never achieving final payment. Should I flag this as RED and draft acceptance
  language, or is the client willing to accept completion without formal sign-off?"

### Step 11: Compliance Flag (if applicable)

If GDPR, UK GDPR, Australian Privacy Act, or HIPAA obligations were identified in Step 2:
- Cross-reference relevant MSA provisions against the compliance requirements
- Flag missing or inadequate compliance provisions with [COMPLIANCE-REQUIRED]
- Recommend specific addenda (DPA, BAA, Data Security Annex)
- Assign RED classification to any unmet mandatory obligation

### Step 12: Business Impact and Negotiation Strategy

Provide a summary covering:
- **Overall risk profile**: High-level risk assessment across IP, liability, commercial, and compliance
  dimensions
- **Top 3-5 issues**: Most important items to resolve, with severity, perspective, and legal basis
- **Negotiation sequencing**: Which issues to lead with, what to concede, how to trade-link
- **Pricing-model-specific risks**: Highlight risks specific to the stated pricing model
- **Timeline considerations**: Urgency factors affecting negotiation approach

**⟁ CLARIFY** — If deal context is unclear:
- "Can you walk away from this engagement, or is this provider/client essential?" — determines
  whether strategy is assertive or accommodating.
- "Who signs off internally? Legal only, or also operations/finance?" — determines how to frame
  escalation.

### Step 13: Quality Verification

Before delivering the analysis, run the quality checks defined in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED item, run the 3-pass Self-Interrogation. Revise if any pass reveals a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: all 16 topic areas addressed (present or flagged absent).
5. Dual-perspective validation: each material clause includes guidance for both sides.
6. SOW/Order Form completeness if applicable.
7. Generate the Glass Box Audit Trail and append to output.

---

## MSA Clause Architecture — 16 Topic Areas

Analyze the MSA systematically across these 16 topic areas. Use **Deep** tier for the most
material and contested clauses; **Standard** tier for important but less contested provisions.

| # | Topic Area | Depth | Provider Focal Points | Client Focal Points |
|---|------------|-------|----------------------|---------------------|
| 1 | **Framework Structure (MSA/SOW/Order Form)** | Deep | MSA governs; SOW/Order Forms are subordinate; conflict resolution favoring MSA | SOW/Order Form specifics override MSA where conflict; right to issue new SOWs without re-negotiating MSA |
| 2 | **Scope of Services and Deliverables** | Deep | Broad scope definition, exclusions listed in SOW; no implied obligations; dependencies on client | Precise deliverable specifications; acceptance criteria; client assumptions and responsibilities; scope freeze mechanism |
| 3 | **Pricing and Payment** | Deep | T&M rates + true-up; invoicing on milestones; expenses at cost; interest on late payment | Budget caps on T&M; milestone payment tied to acceptance; disputed invoice procedure; no pay-when-paid |
| 4 | **Change Control** | Deep | Bilateral change order process; no work proceeds without written authorization; provider's right to price changes | Change orders priced at agreed rates; provider cannot stop work pending change order; deemed approval if client fails to respond |
| 5 | **Intellectual Property** | Deep | Provider retains background IP; client receives license (not assignment) of deliverables; foreground IP owned by provider unless expressly assigned | Client owns all deliverables (commissioned work); provider retains tools and methods only; background IP licensed for deliverables use |
| 6 | **Acceptance Testing** | Deep | Deemed acceptance if client fails to respond within review period; provider's right to cure before rejection; no retroactive rejection | Objective acceptance criteria; client's right to reject for any material non-conformance; cure period before acceptance triggers payment |
| 7 | **Liability Caps and Exclusions** | Deep | Cap at 12 months' fees paid; exclude consequential damages; carveout only for death/personal injury and fraud | Cap at aggregate fees paid (or uncapped for IP breach and data breach); consequential damages carveout for loss of data and business disruption |
| 8 | **Indemnification** | Deep | Mutual indemnity for own IP infringement; narrow scope; client indemnifies for client-provided materials | Provider indemnifies for IP infringement in deliverables; data breach caused by provider; gross negligence/willful misconduct uncapped |
| 9 | **Representations and Warranties** | Deep | Professional standards warranty; non-infringement warranty limited to materials provided; no fitness for purpose | Services warranty (professional, workmanlike); non-infringement warranty for all deliverables; compliance warranty; remedy for warranty breach |
| 10 | **Confidentiality** | Standard | Mutual; term of 3-5 years; standard carveouts; return/destroy on termination; injunctive relief right | Indefinite for trade secrets; client data treated as confidential; provider staff under NDA; right to seek injunction |
| 11 | **Key Personnel and Subcontracting** | Standard | Right to replace key personnel with reasonable notice; broad subcontracting right with flow-down of obligations | Named key personnel; prior consent for replacement; prior consent for subcontracting; flow-down of MSA obligations to subcontractors |
| 12 | **Insurance** | Standard | Professional indemnity, public/general liability, cyber liability (where applicable), workers' compensation; certificates on request | Insurance to market minimums for service type and deal size; additional insured status; certificates before work commences |
| 13 | **Data Protection** | Standard | Provider as data processor if processing client personal data; standard DPA terms; breach notification at 72h post-discovery | GDPR Art. 28 / UK GDPR / Australian Privacy Act mandatory DPA; sub-processor controls; breach notification; cross-border transfer mechanisms |
| 14 | **Term and Termination** | Standard | Auto-renewal; termination for cause with 30-day cure; termination for convenience by client on 90 days' notice with payment for work to date | Termination for cause with 14-day cure; termination for convenience with 30 days' notice; no termination fees; survival of obligations |
| 15 | **Transition and Wind-Down Assistance** | Standard | Transition assistance for reasonable period at then-current rates; limited cooperation obligations; hard end date | Minimum 6-month transition assistance at fixed rates; successor provider non-interference; knowledge transfer; data handover |
| 16 | **Governing Law and Disputes** | Standard | Provider's jurisdiction; senior executive escalation before formal proceedings; binding arbitration for high-value disputes | Neutral jurisdiction; mediation before arbitration; client's right to seek injunctive relief in courts; no class action waiver (B2C) |

---

## Pricing Model Framework

### Time and Materials (T&M)

**Risk allocation**: Client bears scope risk. Provider bills actual time at agreed rates plus reimbursable expenses.

**Key provisions:**
- **Rate schedule**: Named individuals or role categories with blended rates; rate escalation mechanism (CPI or fixed % per year)
- **Budget authorization**: Spending authorization thresholds; obligation to notify client when approaching cap
- **Invoicing frequency**: Weekly, bi-weekly, or monthly; timesheet format and approval process
- **Expense reimbursement**: Pre-approved categories; receipts required above threshold; travel at actuals or capped rates
- **True-up mechanism**: Quarterly or annual reconciliation if minimum commitment applies

**Common YELLOW issues:**
- No budget cap or authorization threshold: client has no cost control mechanism; can generate surprise invoices
- Rate escalation clause without notice period: provider can unilaterally increase rates without giving client time to plan
- No timesheet approval process: billing disputes arise when client questions hours after the fact

**Provider-side redline** (if client demands fixed budget):
> "Provider will notify Client in writing when cumulative fees reach 80% of the authorized budget.
> Client may authorize additional budget in writing or direct Provider to cease work on the affected
> SOW. Provider has no obligation to perform work beyond the authorized budget."

**Client-side redline** (if no cap protection):
> "Provider's aggregate fees under each SOW shall not exceed the authorized budget set out in such
> SOW without prior written authorization from Client's designated representative."

### Fixed-Fee / Lump Sum

**Risk allocation**: Provider bears cost overrun risk. Fee is fixed regardless of actual effort, unless
scope changes through the change control process.

**Key provisions:**
- **Scope definition**: Unambiguous deliverable specifications and acceptance criteria are essential;
  vague scope is the primary driver of fixed-fee disputes
- **Change control**: Mandatory bilateral change order process (see below); price impact of changes
  to be agreed before additional work commences
- **Milestone payments**: Link payment to acceptance of specific deliverables, not just passage of time
- **Exclusions list**: Explicitly list what is NOT included in the fixed fee (client dependencies,
  integration with third-party systems, travel, certain environments)

**Common RED issues:**
- No change control procedure on fixed-fee: every client request for changes becomes a scope dispute
- Payment tied to "completion" without defining acceptance criteria: provider can never finalize
- Unilateral client right to expand scope without price impact

### Milestone-Based

**Risk allocation**: Shared. Provider is accountable for deliverable quality; client controls payment release.

**Key provisions:**
- **Milestone table**: Each milestone with: description, deliverables, due date, payment trigger, percentage
  of total fee
- **Acceptance criteria**: Objective, measurable criteria for each milestone (not "client satisfaction")
- **Review period**: Client's time to accept or reject (typically 10-20 business days)
- **Cure period**: Provider's right to remediate rejected deliverables before triggering default
- **Deemed acceptance**: If client fails to accept or reject within review period without written objection,
  milestone is deemed accepted and payment is triggered

**Common disputes:**
- Acceptance criteria that are subjective ("meets client's requirements") rather than objective
- No deemed acceptance: client delays indefinitely; provider cannot invoice
- No cure period: client rejects; provider has no right to remediate before being in default

### Retainer

**Risk allocation**: Provider earns retainer regardless of utilization; client bears underutilization risk.

**Key provisions:**
- **Scope of retainer services**: Defined availability, response time, and service categories covered
- **Monthly hours / capacity**: Number of hours or days available; carryforward or use-it-or-lose-it
- **Excluded services**: Work outside retainer scope billed at T&M or via separate SOW
- **Minimum term**: Typically 3-12 months; early termination fee for provider if client terminates early

### Hybrid Pricing

**Risk allocation**: Varies by component. Requires careful SOW design to avoid ambiguity.

**Key provisions:**
- **Clear delineation**: Explicitly identify which services are fixed-fee and which are T&M in each SOW
- **Separate tracking**: Separate budgets, invoices, and change control processes for each pricing component
- **Order of precedence**: If conflict between pricing mechanisms, which governs?

---

## Change Control Framework

A robust change control procedure is essential in fixed-fee and milestone-based engagements.
This framework adapts to T&M and hybrid engagements as a voluntary cost-control mechanism.

### Trigger Events

Change control is triggered by any of:
- Expansion of deliverable scope beyond the SOW description
- Change to acceptance criteria or success metrics
- Change to project timeline or milestone dates affecting other deliverables
- Change to client-provided resources, systems, or access that affects provider's workload
- Regulatory changes requiring modification of deliverables
- Addition of new deliverables not included in the SOW

### Change Request Documentation

The party requesting a change submits a **Change Request (CR)** including:
- Description of the requested change
- Reason and business justification
- Proposed impact on: scope, timeline, acceptance criteria, fees
- Provider's assessment: effort estimate, fee impact, schedule impact

### Approval Thresholds

| Change Value | Approval Authority | Timing |
|---|---|---|
| Up to $[X] / [X]% of SOW value | Designated project managers | Within [5] business days |
| $[X] to $[Y] | Senior management on both sides | Within [10] business days |
| Above $[Y] | Executive / legal sign-off | Within [15] business days |

### Deemed Approval

If client fails to approve, reject, or request further information within the approval period:
- Provider sends written reminder
- After [5] additional business days: change is **deemed approved** at provider's proposed terms

**Provider-side rationale**: Prevents indefinite delay that blocks provider from proceeding.

**Client-side counter**: Deemed approval should only apply to non-material changes. For material
scope increases, require affirmative approval.

### No-Work-Ahead Rule

Provider must not commence changed work before a Change Order is signed by both parties.
Exception: provider may proceed with emergency changes to prevent material harm, subject to
client ratification within [2] business days.

---

## IP Ownership Framework

### Background IP vs. Foreground IP

**Background IP**: IP that a party owned or developed before or independently of the engagement.

**Foreground IP**: IP created specifically for the engagement (deliverables, reports, software, creative works).

### Standard Market Positions

| IP Category | Provider-Side Default | Client-Side Standard | Balanced Position |
|-------------|----------------------|---------------------|-------------------|
| Provider background IP (tools, methods, platform, pre-existing code) | Provider retains all; licenses to client for scope of engagement | Provider retains; perpetual license for client's use of deliverables | Provider retains; perpetual, irrevocable, royalty-free license for client's business use of deliverables |
| Third-party IP incorporated into deliverables | Licensed through provider; provider to procure sub-licenses | Client's prior approval for any third-party IP; provider to obtain perpetual sub-license | Provider discloses third-party IP; client approves; provider procures sub-license at no additional cost |
| Foreground IP (deliverables created specifically for client) | Provider retains; grants license to client | Client owns; provider retains license for similar future work | Negotiated: client owns if paid for in full; provider retains generic tools/methods |
| IP developed jointly | Co-ownership (each can exploit independently) | Client owns with license-back to provider | Co-ownership with defined exploitation rights |
| Feedback and improvements | Provider owns all improvements arising from client feedback | Client owns improvements arising from client's input | Provider owns platform improvements; client owns deliverable-specific improvements |

### Jurisdiction-Specific Assignment Formalities

**United States** [VERIFY]:
- Work-for-hire: applies only to (a) works made by employees in scope of employment, OR (b) nine
  categories of specially commissioned works (including compilations, parts of a collective work,
  translations, instructional texts, tests, answer material for tests, atlases, supplementary works,
  and motion pictures/audiovisual works) where parties agree in writing that work is made for hire
- Software deliverables often do NOT qualify as work-for-hire for independent contractors
- For IP not qualifying as work-for-hire: requires a signed written assignment
- Timing: assignment of future copyright is enforceable in equity in the US [VERIFY]

**United Kingdom** [VERIFY]:
- No work-for-hire doctrine: contractors own their IP by default
- Copyright assignment: must be in writing AND signed by or on behalf of the assignor
  (CDPA 1988, s.90(3))
- Design right assignment: must be in writing (CDPA 1988, s.222(3))
- Patent assignment: must be in writing signed by both parties (Patents Act 1977, s.30(6));
  should be registered at UKIPO
- Moral rights: cannot be assigned; can be waived in writing; add express waiver for B2B
- Future works: assignment of future copyright is effective in equity under s.91(1) CDPA;
  where company is assignee, consideration may not be required [VERIFY]
- Practical implication: MSA itself can be the assignment vehicle if it contains the required
  signed written assignment language

**Australia** [VERIFY]:
- No work-for-hire doctrine for contractors: Copyright Act 1968, s.35(6) provides that the
  person who engages a contractor owns copyright in certain specific categories (commissioned
  photographs, portraits, engravings) but NOT software or general works
- Copyright assignment: must be in writing (Copyright Act 1968, s.196(3))
- Patent assignment: must be in writing signed by both assignor and assignee; should be registered
  with IP Australia (Patents Act 1990, s.14)
- Trade mark assignment: must be in writing; should be registered with IP Australia
- Design right assignment: must be in writing

### Recommended IP Assignment Clause (Jurisdiction-Agnostic)

```
IP ASSIGNMENT

1. Background IP: Each party retains all Intellectual Property Rights in its Background IP.
   "Background IP" means all IP Rights owned or licensed by a party prior to the Commencement
   Date, or developed independently of this Agreement.

2. Foreground IP: Subject to payment of all fees due under the applicable SOW, Provider assigns
   to Client all Intellectual Property Rights in the Deliverables ("Foreground IP"), with effect
   from the date of creation. [JURISDICTION-SPECIFIC: In the UK, this assignment is made pursuant
   to s.90(3) CDPA 1988 and is signed by Provider as assignor. In Australia, this assignment is
   made pursuant to s.196(3) of the Copyright Act 1968 and is signed by both parties.]

3. License-back: Client grants Provider a non-exclusive, royalty-free license to use the Foreground
   IP for the purpose of performing services for Client and for Provider's internal training and
   methodology development, provided that no Client Confidential Information is disclosed.

4. Tools and Methods: Provider retains all Intellectual Property Rights in its general tools,
   methodologies, processes, know-how, and generic software components ("Provider Tools"). To the
   extent Provider Tools are embedded in Deliverables, Provider grants Client a perpetual,
   irrevocable, royalty-free, non-exclusive license to use Provider Tools solely as embedded in
   and for the purpose of using the Deliverables.

5. Moral Rights Waiver: [JURISDICTION-SPECIFIC UK/AU: Each individual author employed or engaged
   by Provider hereby irrevocably waives all moral rights (including rights of attribution and
   integrity) in the Deliverables to the fullest extent permitted by applicable law.]

6. Third-Party IP: Provider shall disclose to Client any third-party IP (including open source
   software) incorporated into Deliverables. Provider shall obtain all necessary sub-licenses for
   Client's use of third-party IP in the Deliverables, at no additional cost to Client.
```

---

## Acceptance Testing Framework

### Acceptance Procedure

1. **Submission**: Provider notifies Client in writing that a Deliverable (or Milestone) is ready
   for acceptance review, attaching the Deliverable and referencing the applicable acceptance criteria.

2. **Review period**: Client has [10–20] business days to review the Deliverable against the
   acceptance criteria set out in the SOW.

3. **Acceptance**: Client accepts the Deliverable by written notice, OR by failing to provide a
   written rejection notice within the review period (deemed acceptance).

4. **Rejection**: Client rejects the Deliverable by written notice specifying, in reasonable
   detail, how the Deliverable fails to meet the acceptance criteria.

5. **Cure period**: Provider has [10] business days to remediate and resubmit.

6. **Second review**: Client has a second review period of [10] business days. If the Deliverable
   is still rejected, the parties escalate using the dispute resolution process.

### Acceptance Criteria Design

**Objective criteria (preferred):**
- Passes specified test cases with [X]% pass rate
- Conforms to functional specifications in Exhibit A
- Processes [X] transactions per second under [Y] load conditions
- Complies with [specific regulatory standard]

**Subjective criteria (avoid where possible):**
- "Meets Client's satisfaction" — unenforceable without further definition
- "Professional quality" — disputed; add "as measured against [benchmark]"
- "Fit for purpose" — define the purpose against which fitness is measured

### Deemed Acceptance Anti-Pattern

**Problem**: No deemed acceptance provision means the client can delay acceptance indefinitely,
blocking the provider's final invoice. Common in fixed-fee and milestone-based agreements.

**Solution**: Include deemed acceptance tied to the review period. The provider should give
a follow-up notice if the client fails to respond, then deemed acceptance takes effect after
a short additional period (e.g., 5 business days after follow-up notice).

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than the organizational standard position or professional
services market standard. No negotiation needed.

**All of the following must be true:**
- Clause is present and unambiguous
- Falls within playbook's acceptable range or professional services market standard
- No material compliance risk
- No obligations the party cannot fulfill

### YELLOW — Negotiate

The clause deviates from market standard in a material way, but the risk is manageable and
the clause is typically negotiable.

**Any of the following triggers YELLOW:**
- Liability cap below 12 months' fees (client-side) or above 24 months' fees (provider-side)
- No change control procedure in a fixed-fee or milestone-based engagement
- Unilateral IP assignment of background IP or provider tools (client-side)
- Provider retains foreground IP with license-only (client-side in high-IP-sensitivity engagement)
- Key personnel replacement without client approval (client-side)
- Unrestricted subcontracting without flow-down obligations (client-side)
- Transition assistance limited to 30 days or less in a multi-year engagement (client-side)
- Payment terms beyond Net 60 (provider-side)
- Governing law in a jurisdiction that significantly disadvantages one party without business reason
- Absence of IR35 / employment status compliance clause for UK contractor arrangements

### RED — Escalate

The clause presents a material legal, financial, or compliance risk that cannot be accepted
without senior legal sign-off.

**Any of the following triggers RED:**
- No liability cap at all (provider-side)
- Liability cap below 3 months' fees in a multi-year engagement (client-side)
- Full assignment of background IP (provider-side)
- No IP ownership clause where client is paying for bespoke deliverables (client-side)
- No change control procedure in a fixed-fee engagement (both sides)
- No DPA when personal data subject to GDPR/UK GDPR/Australian Privacy Act is processed
- No acceptance procedure in a milestone-payment engagement (both sides)
- Uncapped indemnification for any category of breach (provider-side, unless gross negligence/fraud)
- Automatic assignment of client's IP or data to provider
- No transition assistance in a multi-year outsourcing or managed services engagement (client-side)
- Governing law or jurisdiction clause that creates unenforceable obligations
- Subcontracting provision allowing provider to use any subcontractor without client approval in a
  regulated, security-sensitive, or high-IP-value engagement

### [COMPLIANCE-REQUIRED] — Regulatory Gap

A mandatory regulatory obligation is unmet. Must be remediated before signature.

---

## MSA Clause Depth Analysis

### 1. Framework Structure: MSA / SOW / Order Form

**MSA governs; SOWs and Order Forms are subordinate.** The MSA sets the legal framework (IP ownership,
liability, confidentiality, termination). SOWs / Order Forms define specific commercial and operational
terms for each engagement.

**Order of precedence**: The MSA should contain an explicit order of precedence clause. Recommended:
1. The applicable SOW or Order Form (for commercial terms specific to that engagement)
2. This MSA (for all other terms)
3. Any exhibits or schedules to the MSA

**Conflict resolution**: Identify which document prevails in case of conflict. A common formulation:
"In case of conflict between the MSA and any SOW, the SOW prevails for commercial terms specific to
that engagement; the MSA prevails for all other terms."

**SOW vs. Order Form distinction:**
- **Statement of Work (SOW)**: Used for bespoke, deliverable-based, or project-based engagements.
  Should include: scope narrative, deliverables table, milestones, acceptance criteria, resource list,
  pricing, client dependencies, assumptions, exclusions.
- **Order Form**: Used for recurring, subscription-like, or standard service lines. Should include:
  service description (by reference to Service Schedule), fees, billing period, term, renewal,
  service credits, applicable SLAs.

### 2. Scope of Services and Deliverables

**Critical drafting principles:**

*Deliverables table (fixed-fee and milestone engagements):*
| Deliverable | Description | Format | Due Date | Acceptance Criteria | Milestone Fee |
|-------------|-------------|--------|----------|--------------------:|:-------------:|
| [Name] | [Specific description] | [PDF, code, report] | [Date] | [Objective criteria] | [$X] |

*Client dependencies clause*: Explicitly list what the provider needs from the client (access,
data, approvals, review time). Failure to provide should trigger timeline relief and, if fixed-fee,
a change order mechanism.

*Exclusions clause*: Explicitly list what is NOT included in the scope. "The Services do not include:
(a) integration with third-party systems other than those listed in Exhibit A; (b) hardware
procurement or installation; (c) services governed by a separate SOW."

### 3. Pricing and Payment

**Invoice dispute procedure**: A missed element in many MSAs. Provider should include:
- Client has [20] business days to dispute an invoice in writing with reasonable detail
- Undisputed portion payable by due date; disputed portion held pending resolution
- Dispute resolution process mirrors the main dispute resolution clause

**Expenses reimbursement**: Define permitted expense categories, approval thresholds, and submission
deadlines. Avoid open-ended "reasonable expenses" without a cap or prior approval requirement.

**Late payment**: UK — Late Payment of Commercial Debts (Interest) Act 1998 allows 8% + Bank of England
base rate on B2B debts automatically [VERIFY]. US — specify interest rate (market: 1.5% per month or
18% per annum). AU — specify interest; courts may imply reasonable rate [VERIFY].

### 4. Indemnification

**Core structure:**

*IP indemnification (provider obligation):*
Provider indemnifies client against third-party IP infringement claims arising from provider's
deliverables, provided that: (a) client gives prompt written notice; (b) provider controls the
defense; (c) client cooperates; (d) client does not make admissions or settlements without consent.

**Carveouts (provider's indemnity does NOT cover):**
- Modifications to deliverables made by client or a third party without provider's consent
- Combination of deliverables with third-party products not specified by provider
- Client's failure to implement updates or patches provided by provider
- Infringement resulting from client-provided specifications or content

*Data breach indemnification:* Where provider processes client personal data as a processor,
provider should indemnify client for losses arising from provider's breach of the DPA and applicable
data protection law. Scope this to provider-caused breaches only.

*Mutual indemnification for third-party bodily injury and property damage.*

### 5. Insurance Schedule

Market-standard insurance requirements vary by service type, jurisdiction, and deal size:

| Coverage Type | Professional Services | IT/Tech Services | Managed Services | Notes |
|---------------|----------------------|-----------------|-----------------|-------|
| Professional Indemnity / E&O | $1M–$5M per claim | $2M–$10M per claim | $5M–$10M per claim | UK: "Professional Indemnity"; US/AU: "Errors & Omissions" |
| Public / General Liability | $2M–$5M | $2M–$5M | $5M–$10M | US: "Commercial General Liability"; UK/AU: "Public Liability" |
| Cyber / Data Protection | N/A – YELLOW | $1M–$5M | $2M–$10M | Required when processing client personal data at scale |
| Workers' Compensation / Employer's Liability | Statutory | Statutory | Statutory | US: varies by state; UK: £5M minimum (Employers' Liability (Compulsory Insurance) Act 1969); AU: statutory |

**Key insurance provisions:**
- Provider must maintain coverage throughout the MSA term and for [3] years post-termination
  (tail coverage or "run-off" coverage for professional indemnity)
- Provider must deliver certificates of insurance before commencing work and on renewal
- Client may require to be named as additional insured on commercial general liability policy

[JURISDICTION-SPECIFIC] UK: Employers' Liability (Compulsory Insurance) Act 1969 requires minimum
£5M cover for employer's liability [VERIFY]. AU: Workers' compensation is state-regulated; requirements
vary by state [VERIFY].

### 6. Termination and Transition

**Termination for cause:**
- Material breach that is: (i) not capable of remedy; OR (ii) capable of remedy and not remedied
  within [30] business days of written notice
- Insolvency, administration, or cessation of business (no cure period)
- Regulatory sanction preventing performance

**Termination for convenience:**
- Client's right: termination on [30–90] days' written notice. Provider paid for all work completed
  to date; no termination fee unless minimum commitment applies.
- Provider's right: [90] days' notice; typically more constrained than client's right
- Provider-side redline: "Client shall pay for all services performed and expenses incurred up to
  the termination date, plus a termination fee of [X]% of remaining SOW value."
- Client-side redline: "Provider may not terminate for convenience during an active SOW without
  Client's written consent."

**Transition and wind-down assistance:**
- Duration: minimum [3] months for short engagements; [6–12] months for multi-year outsourcing
- Scope: knowledge transfer, documentation, assistance to successor provider, data handover
- Pricing: at fixed rates (provider-side: then-current rates; client-side: rates frozen at exit)
- Successor provider cooperation: provider must cooperate with incoming successor; no disparagement
  of client or successor; no poaching client personnel
- Data return/destruction: provider returns or destroys all client data within [30] days of
  transition completion; certification of destruction on request

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify MSA type, parties' sides, pricing model, IP sensitivity, and governing law.
Classify complexity (standard engagement / bespoke high-value / strategic outsourcing). Identify
which statutes and principles are engaged (UCTA, CDPA, Copyright Act, Privacy Act, GDPR, etc.).

**DO**: Execute the clause-by-clause analysis, missing clause detection, SOW review (if applicable),
and pricing-model-specific risk assessment. Generate redlines.

**CHECK**: Run Citation Quality Gates. For each RED item, run Self-Interrogation. Verify all 16
topic areas addressed. Confirm dual-perspective analysis complete.

**ACT**: Record any new patterns (novel clause structure, emerging market position). Flag heuristics
for future reviews. If review changes understanding of a standard position, note for playbook update.

### Citation Quality Gates

Run these 5 gates silently before delivering any output:

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow a consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments (UCTA, CDPA, Copyright Act, Privacy Act, ACL unfair terms 2023) | Flag "[CHECK CURRENCY — may have been amended]" |
| **Domain** | Analysis stays within the MSA's governing law — no US work-for-hire assumptions in UK analysis | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated — IP assignment formalities and unfair terms rules vary by jurisdiction | Add confidence qualifier |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the cited
statute or principle? Would a court in this jurisdiction actually reach this conclusion? Is
there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**: Have all relevant statutes and regulations been considered? Are there
IP assignment formality requirements, unfair terms rules, or data protection obligations missed?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS acceptable? Under what
commercial circumstances might a reasonable lawyer accept this risk? Is the RED classification
proportionate, or is this YELLOW with mitigations?

If any pass reveals a weakness, revise before delivery. Mark audit trail with `self_interrogation:
PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law, clear statute, no ambiguity | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., work-for-hire scope, unfair terms borderline) | Flag for professional review with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: legalcode-master-services-agreement
  date_of_analysis: "[YYYY-MM-DD]"
  mode: "[Review existing MSA / Drafting from scratch / SOW review / Clause request]"
  agreement_reference: "[File name, URL, or 'Pasted text' with word count]"
  governing_law: "[Jurisdiction or 'Not specified']"

  # Perspective and context
  draft_perspective: "[Service Provider / Client / Both]"
  service_type: "[IT Consulting / Managed Services / Professional Services / Creative / Software Development / Mixed]"
  pricing_model: "[T&M / Fixed-Fee / Milestone / Retainer / Hybrid]"
  ip_sensitivity: "[High / Standard / Low]"
  deal_context: "[Brief description or 'Not provided']"
  playbook_used: "[Organizational playbook / Professional services market standards / Options provided as we go]"

  # Compliance flags
  gdpr_uk_gdpr_scope: "[Yes / No / Not assessed]"
  au_privacy_act_scope: "[Yes / No / Not assessed]"
  hipaa_baa_required: "[Yes / No / Not assessed]"
  dpa_required: "[Yes — GDPR / Yes — UK GDPR / Yes — AU Privacy Act / No / Not assessed]"
  ir35_uk_applicable: "[Yes / No / Not assessed]"

  # IP-specific fields
  ip_assignment_jurisdiction: "[US (work-for-hire analysis) / UK (CDPA s.90(3)) / AU (Copyright Act s.196(3)) / Multiple / Not assessed]"
  background_ip_protection_present: "[Yes / No / Partial]"
  foreground_ip_assigned_to_client: "[Yes / No / License only / Not addressed]"
  moral_rights_waiver: "[Present / Absent / N/A (US) / Required]"
  assignment_formalities_met: "[Yes / No / [VERIFY] required]"

  # Pricing model
  change_control_present: "[Yes / No — RED for fixed-fee]"
  acceptance_procedure_present: "[Yes / No — RED for milestone]"
  deemed_acceptance_present: "[Yes / No]"

  # Analysis quality
  topic_areas_covered: "[N of 16]"
  deviations_found: "GREEN: [N] / YELLOW: [N] / RED: [N] / COMPLIANCE-REQUIRED: [N]"
  perspective_flip_completed: "[Yes / No]"
  sow_order_form_reviewed: "[Yes / No / N/A]"

  # Source quality
  external_tools_used: "[legalcode-mcp / None — manual verification required]"
  citations_verified: "[N verified] / [N marked VERIFY]"
  research_reference_file: "[/tmp/legalcode-msa-authority.md or 'Not created']"
  legalcode_mcp: "[Connected / Not connected]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE — no RED items]"

  # Confidence
  confidence_overall: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[IP assignment formalities require jurisdiction-specific verification]"
    - "[UCTA reasonableness test is fact-specific — counsel verification recommended for liability caps]"
    - "[ACL unfair terms provisions for small business contracts: verify current thresholds]"

  reviewer: "AI-assisted — requires qualified legal review before execution"
```

---

## Anti-Patterns

What NOT to do when drafting or reviewing MSAs. These are MSA-specific — not generic contract failures.

**Scope and Change Control Anti-Patterns:**

1. **Fixed-fee without a change control procedure**: No mechanism to price scope changes converts
   every client request into a scope dispute. The provider either eats the cost or faces a relationship
   breakdown. Always include a bilateral change order process with clear approval thresholds and a
   no-work-ahead rule.

2. **Vague SOW scope on a fixed-fee engagement**: "Deliver a comprehensive digital strategy" is not
   a deliverable — it is a dispute waiting to happen. Every fixed-fee SOW must have a deliverables
   table with specific outputs, formats, and objective acceptance criteria.

3. **Client dependencies buried in general assumptions**: The provider's ability to perform depends
   on the client providing access, data, approvals, and personnel. Burying these dependencies in
   general assumptions rather than explicit client obligations means the provider cannot rely on
   them for timeline relief or change orders when the client fails to cooperate.

4. **Unilateral change order pricing**: Provider submits change request; client has no obligation
   to respond or approve by any deadline; work stops indefinitely. Always include deemed approval
   provisions with clear timelines.

**IP Anti-Patterns:**

5. **Assuming work-for-hire outside the US**: Applying US work-for-hire reasoning to UK or Australian
   engagements is a fundamental drafting error. There is no work-for-hire doctrine in the UK (CDPA
   s.90(3) requires written assignment) or Australia (Copyright Act s.196(3)). A UK MSA that states
   "deliverables shall be deemed works made for hire" does not transfer copyright — a signed written
   assignment is required. [VERIFY]

6. **IP assignment without protecting background IP**: A blanket "all IP created under this agreement
   is assigned to client" clause can inadvertently capture the provider's pre-existing tools, methods,
   and reusable components. Always carve out background IP and generic provider tools, granting only
   a license for their use in the deliverables.

7. **No license-back to provider**: After assigning foreground IP to the client, the provider has no
   right to use similar methodologies or even prior work product without the client's consent. A
   license-back is essential to allow the provider to work for future clients using the same approaches.

8. **Third-party IP without sub-licensing**: Provider uses open-source code, stock imagery, or
   third-party APIs in deliverables without disclosing or procuring appropriate sub-licenses. Client
   may receive deliverables it cannot legally use. Always require provider disclosure of third-party
   IP and procurement of perpetual sub-licenses at no additional cost.

9. **Moral rights overlooked in UK/AU**: UK and Australian copyright law preserves moral rights
   (attribution, integrity) that cannot be assigned. A UK or AU IP assignment without a moral rights
   waiver leaves the client exposed to claims from the individual author. Always include an express
   moral rights waiver in UK and AU agreements. [VERIFY]

**Acceptance and Payment Anti-Patterns:**

10. **No deemed acceptance provision**: Client accepts "when satisfied" — which may be never. The
    provider completes work, the client delays acceptance, and the provider cannot invoice. Milestone
    payment engagements without deemed acceptance effectively give the client an indefinite right to
    delay payment.

11. **Subjective acceptance criteria**: "Deliverables must meet Client's reasonable satisfaction" is
    not enforceable. Both parties end up in a dispute about what "reasonable satisfaction" means.
    Write objective, measurable acceptance criteria in every SOW.

12. **Retroactive rejection**: Client accepts a deliverable (or fails to reject within the review period),
    then attempts to reject it months later when discovering problems. Include deemed acceptance and a
    clear cut-off for raising defects post-acceptance.

13. **Final payment tied to final acceptance without interim invoicing**: On a long engagement, provider
    performs months of work without payment until final acceptance. Milestone invoicing tied to
    intermediate deliverables is essential for cash flow management.

**Liability and Indemnification Anti-Patterns:**

14. **Indemnity for "any breach" effectively uncapping liability**: An indemnity obligation triggered
    by "any breach of this Agreement" is functionally uncapped — it covers every obligation in the
    MSA, including minor payment delays or administrative failures. Scope indemnities to material
    categories: IP infringement, data breach, gross negligence, personal injury.

15. **Liability cap that doesn't interact with uncapped indemnities**: A liability cap of 12 months'
    fees is meaningless if the same agreement contains an uncapped IP indemnity or data breach
    indemnity covering the same losses. Map the cap and its carveouts carefully.

16. **No gross negligence / willful misconduct carveout**: A liability cap that applies to gross
    negligence and willful misconduct is commercially unreasonable and may be void under UCTA (UK)
    or unconscionability doctrine (US states). Always carve out death/personal injury, fraud, and
    willful misconduct from the liability cap.

**Transition and Exit Anti-Patterns:**

17. **No transition assistance obligation**: At the end of a multi-year outsourcing engagement, if
    the provider has no obligation to assist with transition, the client is at the provider's mercy.
    The provider can demand commercial rates for knowledge transfer, withhold documentation, and
    refuse to cooperate with the incoming provider. Always include a defined transition assistance
    obligation with scope, duration, and pricing.

18. **Transition pricing at "then-current market rates"**: Provider insists on charging market rates
    for transition assistance, which may be inflated during a contentious exit. Client-side: lock
    in transition rates at the contracted rate schedule; or agree a fixed transition fee at the start
    of the engagement.

19. **No data return/destruction obligation**: Provider retains client data post-termination without
    any obligation to return or destroy it. Under GDPR, UK GDPR, and Australian Privacy Act, this
    may constitute an ongoing unlawful processing obligation. Always require return or destruction
    of all client data within a defined period after termination.

**Regulatory and Compliance Anti-Patterns:**

20. **No DPA when provider processes personal data**: Any MSA where the provider accesses or processes
    personal data (employee data, customer data, health information) without a Data Processing
    Agreement is non-compliant with GDPR, UK GDPR, and/or Australian Privacy Act obligations.
    The DPA must be executed before data processing begins — not added as an afterthought.

21. **IR35 / off-payroll working ignored in UK engagements**: UK client engaging a provider through
    a personal service company must determine employment status under IR35 from April 2021 (medium
    and large businesses). Ignoring this creates tax liability for the client. Include an express
    IR35 compliance clause and status determination obligation. [VERIFY]

22. **Penalty clause risk on milestone payment structures**: Delay penalties and "liquidated damages"
    for late delivery must be proportionate to the actual loss suffered (UK: post-*Cavendish Square*
    penalty doctrine; AU: similar common law rule). An excessive delay penalty is unenforceable.
    Draft milestone delay provisions as genuine pre-estimates of loss. [VERIFY]

---

## Writing Standards

Before delivering any output, apply these quality gates:

1. **Redline specificity**: Every redline must include specific proposed language, not just a
   description of what to change. "Require written IP assignment" is not a redline — provide the
   actual clause text.

2. **Perspective discipline**: In dual-perspective mode, distinguish service provider and client
   positions clearly. Do not present provider-favorable positions as "balanced."

3. **Active voice throughout**: "Provider must assign all foreground IP to Client" not "Assignment
   of foreground IP is required."

4. **MSA terminology consistency**: Once defined, use terms consistently: "Deliverables," "Services,"
   "SOW," "Order Form," "Change Order," "Background IP," "Foreground IP." Do not alternate between
   synonyms.

5. **Quantified obligations**: "Provider shall maintain 99.5% uptime as measured on a monthly basis"
   not "Provider shall use reasonable efforts to maintain system availability."

6. **Jurisdiction markers**: Every legal claim tied to a specific jurisdiction must carry
   [JURISDICTION-SPECIFIC] in the section heading or [VERIFY] on the specific citation.

7. **Audience calibration**: MSA negotiations involve legal, procurement, finance, and operational
   stakeholders. Write findings in plain language without sacrificing precision. A finding
   understood only by lawyers will be ignored by the operations team that runs the engagement.

8. **Completeness before delivery**: Run the 16-topic checklist before delivery. An MSA analysis
   that omits the IP ownership review, change control assessment, or SOW acceptance procedure
   is materially incomplete.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp at Step 4 to gather jurisdiction-specific legal authority. Search for:
- 17 U.S.C. § 101 work-for-hire categories and their application to software (US)
- CDPA 1988 s.90(3) copyright assignment formalities and s.91(1) future works (UK)
- Copyright Act 1968 s.196(3) assignment requirements and s.35(6) commissioned works (AU)
- Patents Act 1977 s.30(6) assignment requirements (UK)
- Patents Act 1990 s.14 assignment requirements (AU)
- UCTA 1977 reasonableness factors and Schedule 2 guidelines (UK)
- ACL unfair contract terms provisions for small business contracts post-November 2023 (AU)
- Late Payment of Commercial Debts Act 1998 (UK) — interest rate and notice requirements
- GDPR Art. 28 mandatory DPA terms and EDPB guidance
- UK GDPR / Data Protection Act 2018 processor obligations
- Australian Privacy Act APPs and NDB scheme notification obligations
- IR35 / ITEPA 2003 off-payroll working rules (UK)
- *Cavendish Square Holding BV v Makdessi* [2015] UKSC 67 — penalty doctrine (UK) [VERIFY]

Save to `/tmp/legalcode-msa-authority.md`. Mark all legalcode-mcp-sourced citations as VERIFIED
in the Glass Box.

### Without legalcode-mcp

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural completeness and prompt engineering quality rather than legal authority depth
- Emphasize that IP assignment formalities require jurisdiction-specific legal verification

---

## Output Format Template

Structure every analysis output as follows:

---

# MSA Analysis — [Agreement Name or Drafting Scope]

**Date**: [YYYY-MM-DD]
**Perspective**: [Service Provider / Client / Both]
**Governing Law**: [Jurisdiction]
**Service Type**: [IT Consulting / Managed Services / Professional Services / Creative / Software Dev]
**Pricing Model**: [T&M / Fixed-Fee / Milestone / Retainer / Hybrid]
**IP Sensitivity**: [High / Standard / Low]
**Based On**: [Organizational playbook / Professional services market standards]
**Completeness**: [N of 16 topic areas analyzed]

---

## Executive Summary

**Overall Risk Profile**: [HIGH / MEDIUM / LOW]
**Key Issues**: [3–5 bullet points — the most important items to resolve before signature]
**Immediate Action Required**: [Yes — RED / COMPLIANCE-REQUIRED items identified | No — proceed with YELLOW negotiations]

**Issue Count**: GREEN: [N] / YELLOW: [N] / RED: [N] / COMPLIANCE-REQUIRED: [N]

---

## Clause-by-Clause Analysis

### [Topic Area] — [GREEN / YELLOW / RED / COMPLIANCE-REQUIRED] | Confidence: [Level]

**Status**: [Present and acceptable / Deviates from market standard / Absent]

**Provider Position** (current or proposed language): "[Direct quote or summary]"
**Client-side standard**: "[What client should expect or push for]"
**Deviation**: "[How this deviates from market standard]"

**Business impact** (provider perspective): "[Consequences if provider accepts client's position]"
**Business impact** (client perspective): "[Consequences if client accepts provider's position]"

**Legal basis**: "[Statute, regulation, or market practice — or [VERIFY]]" [Confidence: X.XX]

**Provider-side redline** (if current language favors client):
> [Specific alternative language]

**Client-side redline** (if current language favors provider):
> [Specific alternative language]

**Fallback position** (if primary redline is rejected):
> [Compromise language]

**Risk Scoring**:
- Business impact: [HIGH / MEDIUM / LOW]
- Enforceability risk: [HIGH / MEDIUM / LOW]
- Negotiation difficulty: [HIGH / MEDIUM / LOW]
- Compliance risk: [HIGH / MEDIUM / LOW]

**Negotiation tier**: [Tier 1 Must-Have / Tier 2 Should-Have / Tier 3 Nice-to-Have]

[Repeat for each of 16 topic areas]

---

## IP Analysis Summary

**Assignment formalities met**: [Yes / No / [VERIFY] required for [jurisdiction]]
**Background IP protected**: [Yes / No / Partial]
**Foreground IP assigned to client**: [Yes / No / License only]
**Moral rights waiver**: [Present / Required but absent / N/A]
**Third-party IP disclosed**: [Yes / No / Not addressed]

---

## SOW / Order Form Analysis [if applicable]

**SOW Completeness**: [N of required elements present]
**Missing elements**: [List]
**Acceptance criteria**: [Objective / Subjective / Absent]
**Deemed acceptance**: [Present / Absent]
**Change control integrated**: [Yes / No]

---

## Compliance Flags

| Obligation | Clause Status | Gap | Classification |
|-----------|--------------|-----|----------------|
| GDPR / UK GDPR Art. 28 DPA | [Present / Absent] | [Description] | [GREEN / COMPLIANCE-REQUIRED] |
| AU Privacy Act DPA | [Present / Absent / N/A] | [Description] | [GREEN / COMPLIANCE-REQUIRED / N/A] |
| HIPAA BAA | [Present / Absent / N/A] | [Description] | [GREEN / COMPLIANCE-REQUIRED / N/A] |
| UK IR35 compliance clause | [Present / Absent / N/A] | [Description] | [GREEN / YELLOW / N/A] |

---

## Negotiation Strategy

**Tier 1 — Must Resolve Before Signature:**
[List with specific issues, legal basis, and recommended resolution]

**Tier 2 — Prioritize in Negotiation:**
[List with specific issues and recommended redlines]

**Tier 3 — Concede Under Pressure:**
[List with items that can be traded to win Tier 1 and 2 positions]

**Trade-link opportunities:**
[Specific pairs: e.g., "Concede on 6-month liability cap to win full IP assignment"]

**Negotiation posture**: [Assertive / Accommodating / Collaborative] — [reason]

---

## Glass Box Audit Trail

```yaml
[Glass Box YAML — see Glass Box section above]
```

---

## Annex A: Statement of Work (SOW) Template

---

**STATEMENT OF WORK NO. [___]**
**Under Master Services Agreement dated [DATE]**

**Client**: [Legal name and address]
**Service Provider**: [Legal name and address]
**SOW Effective Date**: [DATE]

---

### 1. Services Description
[Narrative description of the services to be performed]

### 2. Deliverables

| # | Deliverable | Description | Format | Due Date | Acceptance Criteria |
|---|-------------|-------------|--------|----------|---------------------|
| 1 | [Name] | [Specific description] | [PDF / Code / Report] | [Date] | [Objective criteria] |
| 2 | | | | | |

### 3. Milestones and Payment Schedule (Milestone-Based)

| # | Milestone | Description | Due Date | Payment Trigger | Fee (%) |
|---|-----------|-------------|----------|-----------------|---------|
| 1 | [Name] | [Description] | [Date] | Acceptance of Deliverable(s) [list] | [XX%] |
| 2 | | | | | |

*(Total = 100% of SOW value: $[AMOUNT])*

### 4. Pricing (T&M / Fixed-Fee)

**Time & Materials:**
| Role | Rate | Estimated Hours | Estimated Fee |
|------|------|----------------|---------------|
| [Senior Consultant] | $[X]/hr | [N] | $[Y] |
| [Junior Consultant] | $[X]/hr | [N] | $[Y] |
**Authorized Budget: $[TOTAL] — Provider must notify Client when 80% is reached**

**Fixed Fee:**
Total SOW Fee: $[AMOUNT], payable per Milestone Schedule above.

### 5. Expenses
Pre-approved expense categories: [Travel, accommodation, subsistence at actuals / up to $X per day].
All expenses require receipts and submitted within 30 days of incurrence.

### 6. Personnel

| Name / Role | Status |
|-------------|--------|
| [Name] — [Role] | Key Personnel — replacement requires Client approval |
| [Name] — [Role] | Standard Personnel |

### 7. Client Dependencies
Provider's obligations are conditional on Client providing:
- [ ] [Specific access / system / data / approvals]
- [ ] [Named client personnel for review and approval]
- [ ] [Review periods as specified in acceptance procedure]

Failure to provide client dependencies within [5] business days of Provider's written request
entitles Provider to a corresponding extension of timeline and, on fixed-fee SOWs, a change order.

### 8. Assumptions and Exclusions
**Assumptions** (incorporated into fee estimate):
- [E.g., "Client systems are accessible 99% during business hours"]
- [E.g., "Integration limited to systems identified in Exhibit A"]

**Exclusions** (not included in Services):
- [E.g., "Hardware procurement or installation"]
- [E.g., "Third-party software licensing costs"]
- [E.g., "Services governed by a separate SOW"]

### 9. Acceptance Procedure
The acceptance procedure set out in Section [X] of the MSA applies. Acceptance criteria for each
Deliverable are set out in the table above. Review period: [10] business days. Cure period: [10]
business days following rejection notice.

### 10. Change Control
All changes to this SOW are subject to the change control procedure set out in Section [X] of the MSA.

### 11. Governing Terms
This SOW is governed by the MSA. In case of conflict between this SOW and the MSA: this SOW prevails
for commercial terms specific to this engagement; the MSA prevails for all other terms.

**Signed for and on behalf of CLIENT:**
Name: _____________________________ Title: ________________________
Signature: _________________________ Date: _________________________

**Signed for and on behalf of SERVICE PROVIDER:**
Name: _____________________________ Title: ________________________
Signature: _________________________ Date: _________________________

---

## Annex B: Order Form Template

---

**ORDER FORM NO. [___]**
**Under Master Services Agreement dated [DATE]**

**Client**: [Legal name and address]
**Service Provider**: [Legal name and address]
**Order Form Effective Date**: [DATE]

---

### 1. Services

| Service | Description | Reference | Volume / Scope |
|---------|-------------|-----------|---------------|
| [Service Line A] | [Brief description] | [Service Schedule A] | [Units / hours / users] |
| [Service Line B] | [Brief description] | [Service Schedule B] | [Units / hours / users] |

### 2. Fees and Billing

| Service | Unit Price | Volume | Monthly Fee | Annual Fee |
|---------|-----------|--------|-------------|-----------|
| [Service A] | $[X] / unit | [N] | $[Y] | $[Z] |
| **Total** | | | **$[Y]** | **$[Z]** |

**Billing period**: [Monthly / Quarterly / Annual] in advance
**Payment terms**: Net [30] days from invoice date

### 3. Term and Renewal

**Initial term**: [12 / 24 / 36] months from Order Form Effective Date
**Auto-renewal**: Renews for successive [12]-month periods unless either party gives [60] days'
written notice of non-renewal before the end of the then-current term.

### 4. Service Level Agreement

[Reference applicable SLA schedule, or state key metrics:]
- Availability: [99.5%] measured monthly
- Response time for Priority 1 incidents: [2] hours
- Resolution time for Priority 1 incidents: [8] hours

Service credit regime: [reference Service Schedule or state credits]

### 5. Key Contacts

| Role | Client | Service Provider |
|------|--------|-----------------|
| Contract Manager | [Name / email] | [Name / email] |
| Technical Lead | [Name / email] | [Name / email] |
| Billing Contact | [Name / email] | [Name / email] |

### 6. Governing Terms
This Order Form is governed by the MSA. In case of conflict: this Order Form prevails for commercial
terms specific to this Order Form; the MSA prevails for all other terms.

**Signed for and on behalf of CLIENT:**
Name: _____________________________ Title: ________________________
Signature: _________________________ Date: _________________________

**Signed for and on behalf of SERVICE PROVIDER:**
Name: _____________________________ Title: ________________________
Signature: _________________________ Date: _________________________

---

## Localization Notes

This skill is jurisdiction-agnostic and designed for use with any governing law. When adapting
for specific jurisdictions:

**United States**: Verify work-for-hire applicability (17 U.S.C. § 101) for each deliverable type.
Include express assignment for deliverables not qualifying as work-for-hire. Address state-specific
non-compete restrictions (void in California). Include arbitration clause if desired with FAA
enforceability. Check UCC Article 2 applicability for deliverables with significant goods component.

**United Kingdom**: Use CDPA-compliant IP assignment language signed by the assignor (s.90(3)).
Include moral rights waiver. Assess UCTA reasonableness for limitation of liability clauses —
particularly for professional liability. Include IR35 / off-payroll working status determination
clause. Use Late Payment of Commercial Debts (Interest) Act 1998 rate for late payment interest.
Consider LCIA or ICC arbitration for high-value disputes.

**Australia**: Use Copyright Act 1968-compliant IP assignment language signed by both parties
(s.196(3)); register patent assignments with IP Australia. Assess ACL unfair terms provisions for
small business contracts (expanded thresholds post-November 2023). Include Privacy Act / NDB
scheme obligations where personal data is processed. Consider proportionate liability implications
for damages calculations under state Civil Liability Acts.

**Cross-border engagements**: If the MSA governs services delivered across multiple jurisdictions,
the IP assignment clause must be compliant with the most formality-demanding jurisdiction (typically
UK/AU requiring signed written assignment). Include a GDPR / UK GDPR / Australian Privacy Act DPA
where personal data flows across borders.

---

## Multi-Stakeholder Mapping

For every MSA, identify ALL affected stakeholders:

| Stakeholder | Role | Affected Clauses | Impact | Action Required |
|-------------|------|-----------------|--------|-----------------|
| Client | Primary party | All | Primary | Sign / Negotiate |
| Service Provider | Primary party | All | Primary | Sign / Negotiate |
| Client data subjects | Third party | Data protection, IP | Indirect | DPA required |
| Subcontractors | Third party | Subcontracting, IP, confidentiality | Indirect | Flow-down obligations |
| Key personnel | Internal (provider) | Personnel, IP (moral rights), non-compete | Indirect | Employment contract alignment |
| Successor provider | Third party | Transition, IP, data handover | Indirect | Cooperation obligation |
| Regulator | Regulator | Data protection, compliance | Compliance | Breach notification readiness |

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis incorporating:
- Structural patterns from `legalcode-contract-review` and `legalcode-saas-agreement-drafter`
  (Legalcode gold standards)
- 2-agent research pipeline:
  - Agent 1 (Structural Analysis): MSA core clause architecture, SOW/Order Form framework,
    pricing model risk frameworks, IP assignment formalities (CDPA s.90(3), Copyright Act 1968
    s.196(3), 17 U.S.C. § 101), acceptance testing best practices, change control procedures,
    transition assistance provisions, insurance market standards, anti-assignment/change-of-control
    provisions, dispute resolution and governing law patterns
  - Agent 2 (Prompt Engineering & Quality): Dual-perspective clause analysis design, interactive
    clarification framework for MSA contexts, SOW vs Order Form distinction, change control
    governance patterns, anti-hallucination safeguards for IP formality requirements
- Jurisdictions covered: US (federal + state overlays), UK (English law, CDPA, UCTA, IR35),
  AU (Copyright Act 1968, Patents Act 1990, ACL, Privacy Act 1988)
- All statutory citations marked [VERIFY] require verification against authoritative sources before
  legal reliance
- IP assignment formality requirements are jurisdiction-specific and fact-sensitive — always verify
  with qualified local counsel before finalizing
