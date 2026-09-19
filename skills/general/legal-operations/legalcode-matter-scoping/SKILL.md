---
name: legalcode-matter-scoping
description: Generate comprehensive legal matter scope statements, fee arrangement analyses, staffing
  plans, phased budgets, milestone frameworks, and competitive-bid RFP templates. Use when engaging outside
  counsel, responding to a legal services RFP, structuring a panel tender, building an alternative-fee-arrangement
  (AFA) proposal, budgeting a litigation or transaction, planning a regulatory matter, or reviewing an
  existing engagement for scope creep. Covers hourly, fixed/flat, capped, blended, and portfolio fee arrangements
  with pros/cons analysis. Supports in-house legal departments, law firm business development, legal operations
  teams, CLO offices, and external counsel preparing engagement letters. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Matter Scoping

> **Disclaimer**: This skill provides a framework for AI-assisted legal matter scoping,
> budgeting, and RFP preparation. It does not constitute legal advice. Scope estimates,
> fee projections, and budgets are planning tools only — actual costs depend on matter
> complexity, facts discovered, and decisions made by counsel. All outputs should be
> reviewed by a qualified legal professional before use in engagement letters, proposals,
> or procurement decisions. Laws governing professional obligations, fee agreements, and
> competitive procurement vary by jurisdiction — verify current requirements before
> relying on any provision described here.

## Purpose and Scope

This skill generates production-ready legal matter scoping deliverables. It structures
the scoping conversation, produces a complete Scope Statement, selects the right fee
arrangement model, builds a staffing and budget framework, defines milestones and KPIs,
and — where required — drafts an RFP template or competitive bid submission.

**Covers:**

- Matter scope statement development (objectives, deliverables, in/out of scope, assumptions)
- Fee arrangement analysis and selection: hourly, fixed/flat, capped, blended, portfolio
- Staffing plan framework: partner/associate/paralegal/specialist ratios and task allocation
- Phased budget model with contingency reserves and escalation triggers
- Milestone architecture and matter performance KPIs
- RFP template generation for competitive outside-counsel selection
- Competitive bid process support (panel tender, beauty parade, evaluation criteria)
- Scope change control procedures and scope-creep prevention framework

**Does not:**

- Provide legal advice or constitute a professional engagement
- Replace a qualified legal professional's judgment on matter strategy
- Guarantee budget accuracy — estimates are planning tools only
- Apply to any single jurisdiction exclusively — [JURISDICTION-SPECIFIC] markers flag
  where local professional rules, procurement law, or fee regulations apply

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. Matter scoping principles apply across legal systems.

[JURISDICTION-SPECIFIC] Flag when localizing:

- **Professional rules on fee agreements**: ABA Model Rule 1.5 (US), SRA Code 2019
  (England/Wales), Solicitors Practice Regulations (Ireland), provincial law society
  rules (Canada) — most require fee agreements to be communicated in writing [VERIFY]
- **Contingency/success-fee restrictions**: Many civil law jurisdictions restrict or
  prohibit contingency fees (Germany, France, civil law EU generally) [VERIFY]
- **Public procurement rules**: Government and public-sector legal services procurement
  may require formal tender processes under EU Procurement Directive 2014/24/EU, UK PCR
  2015, US FAR, or equivalent national rules [VERIFY]
- **Billing transparency requirements**: Some jurisdictions require itemized billing,
  pre-approval of significant cost items, or disclosure of sub-contractor costs [VERIFY]
- **Mandatory engagement letter content**: Local bar rules may specify minimum content
  for retainer agreements (scope, fees, billing cycle, file-retention policies) [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming matter type, fee model, or budget range, the workflow pauses and asks when:

- The answer would materially change the scope statement or fee recommendation
- Multiple fee models are viable and the choice depends on the user's risk appetite
- The matter phase or complexity is unclear and affects budget sizing
- Competitive bid requirements may impose procedural constraints

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

### Step 1: Accept the Request

Accept matter scoping requests in any of these formats:

- **New matter description**: Free-text description of the matter, counterparty, and
  business context
- **Existing engagement letter or SOW**: Document to review for scope gaps or revisions
- **RFP request**: Instruction to draft an RFP for outside counsel selection
- **Budget review request**: Existing budget to analyse for completeness and risk

If no context is provided, ask the user to describe the matter and their primary goal
(scope statement, budget, RFP, or all three).

### Step 2: Gather Matter Context

**⟁ CLARIFY** — Before building anything, gather this context. Present as structured
options where possible:

1. **Matter type**: What kind of legal matter is this?
   - Options: Commercial litigation, Arbitration, Regulatory investigation, M&A /
     corporate transaction, Contract drafting/negotiation, Employment matter,
     IP dispute/prosecution, Real estate transaction, Compliance programme build,
     Outsourced legal function (portfolio), Other (describe)
   - _Why this matters_: Matter type determines scope architecture, fee model
     suitability, staffing mix, and typical phase structure.

2. **Perspective**: Who is generating this scoping document?
   - Options: In-house legal (scoping work for outside counsel), Law firm (responding
     to RFP or preparing engagement letter), Legal operations (building a procurement
     framework), Other
   - _Why this matters_: In-house and firm perspectives differ on what the document
     emphasises — in-house focuses on cost certainty and control; firms focus on
     adequate scope and risk allocation.

3. **Fee model preference**: Is there a target fee arrangement?
   - Options: Hourly (full flexibility), Fixed/flat (cost certainty priority),
     Capped (hybrid — hourly up to a maximum), Blended/portfolio (multi-matter package),
     Not decided — run the full fee analysis to recommend the best fit
   - _Why this matters_: The fee model determines the structure of the budget, the
     risk allocation, and the contract monitoring approach.

4. **Budget range**: What is the expected order of magnitude?
   - Options: Under $50K, $50K–$250K, $250K–$1M, $1M–$5M, Over $5M, Not known yet —
     use the scoping process to determine this
   - _Why this matters_: Budget range calibrates contingency percentages, staffing tier
     ratios, and whether the matter justifies competitive procurement.

5. **Deliverable needed**: What should the output include?
   - Options: Scope statement only, Scope + fee analysis, Full scoping pack (scope +
     fee + staffing + budget + milestones), RFP template, Competitive bid submission,
     All of the above
   - Allow multiple selections.

6. **Timeline**: When must work begin, and what is the expected duration?
   - Free text. Prompt: "E.g., 'Start immediately, expected 6 months', or 'RFP to
     be issued in 3 weeks for a 2-year panel appointment.'"
   - _Why this matters_: Duration directly affects total budget, phasing, staffing
     continuity, and fee model viability.

If the user provides partial context, state assumptions explicitly (e.g., "I'm assuming
this is from the in-house perspective and you want a full scoping pack — correct this
if wrong") and proceed.

### Step 3: Identify Applicable Professional Rules

Identify the jurisdiction where the engaging legal professional is admitted and the
jurisdiction of the matter.

**⟁ CLARIFY** — If the jurisdiction is unclear, ask:

- "Which jurisdiction's professional conduct rules apply to the engaging lawyer?"
  (This determines engagement letter minimum content, fee transparency requirements,
  and any restrictions on certain fee types.)

Use **legalcode-mcp** (if connected) to verify:

- Local bar/law society rules on fee agreements and retainers
- Any public procurement requirements applicable to the engaging entity
- Restrictions on alternative fee arrangements (contingency, success fees)

Mark all references with VERIFIED (legalcode-mcp) or [VERIFY] (unverified).

**If legalcode-mcp is not connected:**

- Mark all professional-rule references with [VERIFY]
- Proceed with the general framework; flag jurisdiction-specific requirements for
  counsel to verify before use in binding documents.

### Step 4: Build the Scope Statement

A complete scope statement has five components. Develop each in sequence:

#### 4a. Matter Objectives

Define the specific legal outcomes the matter must achieve. Objectives must be
SMART: Specific, Measurable, Achievable, Relevant, Time-bound.

**⟁ CLARIFY** — If the user's description mixes objectives with tactics, ask:

- "Let's separate the objective from the approach. The objective is the outcome you
  need (e.g., 'defend the company against claim X', 'execute the acquisition of Y by
  [date]', 'achieve regulatory clearance for Z'). Tactics are how we get there. Can
  you confirm the top 1-3 objectives?"

#### 4b. In-Scope Work

List specific deliverables, tasks, and work streams that are explicitly included.
Use action-oriented language (verb + object):

- Draft/negotiate [specific document]
- Conduct [specific investigation or analysis]
- Represent the company in [specific proceedings]
- Advise on [specific question]
- File [specific document or application]

**⟁ CLARIFY** — For complex matters with multiple possible work streams, present a
checklist of typical tasks for the matter type and ask the user to confirm inclusion:

- "For a commercial litigation matter, typical in-scope tasks include: pleadings,
  discovery/disclosure, expert evidence, pre-trial motions, trial preparation, and trial.
  Which of these are in scope? Are there additional tasks specific to this matter?"

#### 4c. Out-of-Scope Work

Explicitly list what is NOT included. This is as important as the in-scope list —
omissions here create scope creep and budget disputes.

Common out-of-scope exclusions:

- Related but distinct claims or proceedings
- Work on behalf of affiliates not named as parties
- Advice on non-legal matters (commercial strategy, PR, communications)
- Regulatory filings in jurisdictions not listed in-scope
- Translation services, e-discovery vendor management (unless explicitly in-scope)
- Post-resolution implementation of settlement or judgment
- Appeals (unless separately scoped)

#### 4d. Assumptions

Document the factual assumptions on which the scope and budget are based. Unmet
assumptions are the most common source of budget overruns. Each assumption should
state:

- **The assumption**: What is assumed to be true
- **The trigger**: What happens if this assumption proves wrong
- **The cost consequence**: Estimated impact on scope/budget if assumption is wrong

Common assumptions:

- The matter will be resolved without trial / hearing
- The counterparty will not bring cross-claims beyond those described
- Document volume will not exceed [X] GB / [Y] documents
- Key witnesses are available and cooperative
- No additional jurisdictions will be added to the scope
- Regulatory/court timelines will be as currently projected

#### 4e. Scope Classification Matrix

Assess each scope element against the **Scope Completeness Classification**:

| Status       | Meaning                                                       | Action                    |
| ------------ | ------------------------------------------------------------- | ------------------------- |
| **COMPLETE** | Element is fully defined, deliverable is unambiguous          | Include as stated         |
| **PARTIAL**  | Element exists but needs further definition or boundaries     | Develop before finalising |
| **MISSING**  | Critical element absent — scope will be incomplete without it | Add before use            |

Minimum requirements for COMPLETE status:

- Objectives: at least one SMART objective per major work stream
- In-scope: all deliverables have a clear completion criterion
- Out-of-scope: at least three exclusions that prevent the most common scope-creep scenarios
- Assumptions: every major cost driver is covered by an assumption statement
- Scope change procedure: documented (see Anti-Patterns §15 and §16)

### Step 5: Fee Arrangement Analysis

Analyse the matter characteristics and recommend the optimal fee arrangement. Run all
five models against the matter profile:

#### Fee Arrangement Selection Framework

| Model             | Best Fit                                                                                                                                     | Pros                                                                                          | Cons                                                                                                              | Risk Allocation                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Hourly**        | Complex, unpredictable matters where scope cannot be defined upfront; novel legal questions; matters requiring strategic judgment throughout | Maximum flexibility; no under-scoping risk for the firm; scalable as facts develop            | Cost unpredictability for client; incentivises hours over efficiency; limited cost control                        | Risk on client                             |
| **Fixed/Flat**    | Well-defined, repeatable, or bounded matters (standard NDA review, routine filings, defined transaction phases)                              | Full cost certainty for client; incentivises firm efficiency; easy to budget                  | Firm under-estimates risk = quality erosion; scope creep risk is high; requires detailed scope definition upfront | Risk on firm                               |
| **Capped**        | Moderate complexity with partially knowable scope; client wants cost ceiling with hourly flexibility                                         | Cost ceiling provides client protection; firm bills hourly up to the cap                      | Firm may inflate the cap; effort reduction risk after cap is hit; no reward for exceeding cap                     | Shared — cap boundary is the tension point |
| **Blended/Mixed** | Multi-phase matters where early phases are uncertain but later phases are predictable; matters with routine + complex components             | Balances predictability and flexibility; can mix models by phase                              | Harder to negotiate and monitor; complexity in billing reconciliation; does not provide overall cost certainty    | Shared                                     |
| **Portfolio**     | High-volume, repeatable matters handled across a defined period (e.g., annual panel, employment disputes, contract reviews)                  | Predictability at portfolio level; firm efficiency gains from volume; enables fiscal planning | Difficult to price without historical data; cross-matter subsidisation risk; poor fit if volume is uncertain      | Shared — requires mature historical data   |

**⟁ CLARIFY** — If multiple models score comparably, present the trade-off to the user:

- "This matter scores well for both Fixed/Flat (defined phases) and Capped (some
  residual uncertainty). Fixed/Flat gives you cost certainty but requires a detailed
  SOW now. Capped gives you a ceiling with flexibility, but risk-of-effort-reduction
  once the cap is hit. Which risk are you more concerned about?"

#### Fee Model Scoring Matrix

Score the matter on six dimensions (1 = argues against this model, 5 = strongly supports it):

| Dimension                 | Question                                       | Hourly | Fixed | Capped | Blended | Portfolio |
| ------------------------- | ---------------------------------------------- | ------ | ----- | ------ | ------- | --------- |
| **Scope certainty**       | How well-defined is the scope?                 | 1-5    | 5-1   | 3      | 3       | 5-1       |
| **Complexity**            | How novel or unpredictable is the legal work?  | 5-1    | 1-5   | 3      | 3       | 1-5       |
| **Matter duration**       | Short/bounded vs. long/open-ended?             | 3      | 5-1   | 3      | 3       | 1-5       |
| **Budget certainty need** | How important is cost certainty to the client? | 1      | 5     | 4      | 3       | 4         |
| **Historical data**       | Do past matters provide reliable cost data?    | 3      | 5-1   | 3      | 3       | 5-1       |
| **Volume**                | Is this one matter or many similar matters?    | 3      | 3     | 3      | 3       | 5         |

Score each model. The highest-scoring model is the primary recommendation. Present
the top two models with reasoning and trade-offs.

#### AFA Risk Allocation Statement

For each recommended fee model, include an explicit risk allocation statement for the
engagement letter:

```
Fee Model: [Model]
Client bears the risk of: [list — e.g., scope expansion, additional jurisdictions,
  novel factual developments, counterparty-driven complexity]
Firm bears the risk of: [list — e.g., internal inefficiency, staffing decisions,
  under-estimated task effort within agreed scope]
Shared risks (trigger scope/fee review): [list — e.g., major new claims added,
  regulatory expansion of the matter, force majeure events]
```

### Step 6: Staffing Plan

Build a staffing plan allocating tasks to seniority levels. Use the CLOC/ACC staffing
efficiency principle: work should be done at the lowest cost level consistent with
the quality required.

#### Staffing Levels and Task Allocation

| Level                           | Rate tier | Best allocated to                                                                              |
| ------------------------------- | --------- | ---------------------------------------------------------------------------------------------- |
| **Relationship partner**        | Highest   | Client relationship, strategy, key negotiations, court appearances, board-level reporting      |
| **Matter partner / lead**       | High      | Day-to-day matter strategy, senior document review, deposition/witness prep, key court filings |
| **Senior associate**            | Mid-high  | Core analysis, drafting, research on novel issues, managing document review teams              |
| **Associate**                   | Mid       | Research, first-draft documents, discovery/disclosure management, document review              |
| **Paralegal / legal assistant** | Low-mid   | Document collection, organisation, filing, administrative tasks, first-pass review             |
| **Specialist / consultant**     | Variable  | Expert witnesses, technical specialists, local counsel in additional jurisdictions             |

#### Staffing Efficiency Checks

Flag these inefficiencies — they drive cost without proportionate value:

- **Over-staffing**: Partners doing associate-level research or drafting
- **Under-staffing**: Associates doing work that requires partner judgment but not flagged
- **Leverage imbalance**: Leverage ratio (non-partner timekeepers / partners) below 1.5x
  for a matter that should be associate-heavy
- **Unplanned specialist spend**: Costs for experts, e-discovery, or local counsel not
  captured in original scope

#### Staffing Plan Template

```
Matter: [Name]
Phase: [Name]

| Timekeeper | Level | Estimated Hours | Hourly Rate | Subtotal | Key Tasks |
|------------|-------|----------------|-------------|----------|-----------|
| [Name/role] | Partner | [X] | [£/$/€X] | [X] | [Strategy, client liaison] |
| [Name/role] | Sr. Associate | [X] | [X] | [X] | [Core drafting, analysis] |
| [Name/role] | Associate | [X] | [X] | [X] | [Research, document review] |
| [Name/role] | Paralegal | [X] | [X] | [X] | [Bundling, filing, admin] |
| [Specialist] | Expert | [X] | [X] | [X] | [Technical analysis] |

Phase subtotal: [X]
Disbursements estimate: [X]
Phase total: [X]
```

**⟁ CLARIFY** — If hourly rates are not provided, ask:

- "Do you have standard rates for these timekeepers, or should I use market-benchmark
  ranges for [jurisdiction]? Note that actual rates should be agreed in the engagement
  letter — any rates I use here are illustrative planning estimates only."

### Step 7: Budget Framework

Build a phased budget covering all stages of the matter from instruction to resolution.

#### Phase Architecture by Matter Type

**Litigation / Arbitration:**
| Phase | Typical % of total budget | Key cost drivers |
|-------|--------------------------|-----------------|
| Pre-action / Investigation | 5–10% | Fact-gathering, legal research, pre-action correspondence |
| Pleadings | 10–15% | Statement of claim/defence, initial motions |
| Disclosure / Discovery | 25–40% | Document collection, review, e-discovery, production |
| Experts | 10–20% | Expert reports, expert witness preparation |
| Pre-trial / Pre-hearing | 10–15% | Evidence bundling, witness prep, final pleadings |
| Trial / Hearing | 15–25% | Court/tribunal attendance, real-time support |
| Post-decision | 5–10% | Enforcement, appeals (if in scope) |

**Transaction (M&A, Real Estate, Finance):**
| Phase | Typical % of total budget | Key cost drivers |
|-------|--------------------------|-----------------|
| Due Diligence | 25–35% | Document review, report drafting |
| Drafting & Negotiation | 30–40% | Principal documents, negotiations |
| Conditions & Regulatory | 10–20% | Regulatory filings, competition clearance |
| Signing & Closing | 10–15% | Closing deliverables, condition satisfaction |
| Post-closing | 5–10% | Integration, regulatory notifications |

**Compliance / Regulatory:**
| Phase | Typical % of total budget | Key cost drivers |
|-------|--------------------------|-----------------|
| Assessment | 20–30% | Gap analysis, current-state review |
| Remediation Design | 25–35% | Policy drafting, programme design |
| Implementation Support | 30–40% | Training, system changes, monitoring |
| Ongoing Advisory | 10–15% | Queries, regulatory updates, audits |

#### Contingency Reserve Guidelines

| Matter Complexity                 | Scope Certainty | Contingency |
| --------------------------------- | --------------- | ----------- |
| Low (routine, precedented)        | High            | 5–10%       |
| Medium (some unknowns)            | Moderate        | 10–20%      |
| High (novel issues, adversarial)  | Low             | 20–35%      |
| Very high (investigation, crisis) | Very low        | 35–50%      |

**Contingency Governance Rules** — include in every budget:

- Contingency may only be accessed with written approval from [designated authority]
- Contingency status reported monthly: spent / committed / released / remaining
- Unused contingency is not automatically carried forward to the next phase
- Contingency does not cover scope additions — those require a scope change procedure

#### Budget Escalation Triggers

Define thresholds that require a budget review and re-approval:

```
Escalation Trigger Table:
| Threshold | Action |
|-----------|--------|
| 80% of phase budget consumed | Alert to matter supervisor |
| 100% of phase budget consumed | Mandatory review before proceeding |
| New claim / regulatory development added | Scope change procedure (see §8) |
| Discovery volume exceeds [X] documents | Mid-phase review |
| Counterparty files unexpected cross-claims | Budget revision required |
| Expert requirement identified | Specialist budget line added |
```

**⟁ CLARIFY** — If matter is high-value (over $1M), recommend:

- "For matters over $1M, consider quarterly budget review meetings between in-house
  and outside counsel to review budget vs. actuals by phase. Should I include this
  as a KPI in the matter plan?"

### Step 8: Scope Change Control

Every scoping document must include a scope change procedure. This is the single
most effective control against scope creep.

#### Scope Change Procedure Template

```
SCOPE CHANGE PROCEDURE — [Matter Name]

1. Change Request: Any party proposing a scope change submits a written
   Change Request Form describing:
   - The proposed change to scope
   - The reason for the change
   - Estimated cost impact (additional fees and disbursements)
   - Estimated timeline impact
   - Impact on existing milestones

2. Review: [Designated in-house contact] reviews the Change Request within
   [X] business days and either approves, rejects, or requests clarification.

3. Authorisation: Scope changes above [£/$X] require sign-off from
   [designated authority (e.g., GC, CFO above threshold)].

4. Documentation: Approved changes are documented as an amendment to the
   Scope Statement and reflected in a revised budget and timeline.

5. No-Start Rule: Outside counsel must not commence out-of-scope work before
   written approval is received, except in genuine emergencies where failure
   to act would prejudice the client's legal position (in which case, verbal
   approval must be sought immediately and confirmed in writing within 24 hours).
```

### Step 9: Milestone and KPI Framework

Define measurable checkpoints and performance metrics for the matter.

#### Milestone Architecture

For each phase, define:

- **Completion criterion**: What must be delivered or achieved for the phase to close
- **Target date**: Planned completion date
- **Responsible party**: In-house counsel, outside counsel, or shared
- **Gate review**: Does this milestone require formal sign-off before proceeding?

#### Matter KPI Framework

| KPI                             | Definition                                    | Target                                   | Measurement Frequency |
| ------------------------------- | --------------------------------------------- | ---------------------------------------- | --------------------- |
| **Budget adherence**            | Actual spend vs. budget by phase              | Within 10% per phase                     | Monthly               |
| **Milestone achievement**       | Milestones hit on target date                 | ≥90% on time                             | Per milestone         |
| **Responsiveness**              | Response time to client queries               | ≤24 hrs (urgent) / 48 hrs (standard)     | Per query             |
| **Matter cycle time**           | Total duration from instruction to resolution | Benchmark for matter type                | End of matter         |
| **Cost per matter**             | Total cost from instruction to resolution     | Benchmark for matter type                | End of matter         |
| **Outside counsel utilisation** | Hours billed at each seniority level vs. plan | Within 15% of staffing plan              | Monthly               |
| **Scope change requests**       | Number of approved scope changes              | Track (no target — measure for learning) | Per change            |
| **Client satisfaction**         | Post-matter review score (if applicable)      | ≥4/5 or equivalent                       | End of matter         |

**⟁ CLARIFY** — For portfolio/panel arrangements covering multiple matters, ask:

- "Should I include portfolio-level KPIs (e.g., average cost per matter type, total
  outside counsel spend vs. budget, matter volume by category, year-over-year cost
  trend)? These are relevant for panel governance and annual firm performance reviews."

### Step 10: RFP Template Generation (if required)

If the deliverable includes an RFP for outside counsel selection, generate a complete
RFP template with these five sections:

#### RFP Template Structure

**SECTION 1: Company and Matter Overview**

```
[Company/Organisation Name] invites proposals from qualified law firms for the
provision of legal services in connection with [matter description].

Company Overview:
- Name, registered address, nature of business
- Legal department structure (in-house headcount, jurisdictions served)
- Current outside counsel arrangements (panel / ad hoc)

Matter Overview:
- Matter type and description
- Estimated duration: [range]
- Estimated complexity: [Low / Medium / High]
- Geographic scope: [Jurisdictions]
- Budget range (if disclosing): [range]
- Expected start date: [date]
```

**SECTION 2: Scope of Services**

```
The successful firm will provide:
[List of in-scope services from §4b of the scope statement]

The following services are NOT included in this RFP:
[List of out-of-scope exclusions from §4c]

Key assumptions on which proposals should be based:
[List of assumptions from §4d]
```

**SECTION 3: Proposal Requirements**

Firms responding to this RFP must address:

| Requirement                   | Details                                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Team composition**          | Identify proposed team by role, seniority, and relevant experience. Provide CVs.                                                       |
| **Fee proposal**              | Propose a fee arrangement. Specify model (hourly/fixed/capped/blended). Provide rates by timekeeper.                                   |
| **Matter plan**               | Provide a phased matter plan with estimated hours per phase, milestones, and timeline.                                                 |
| **Relevant experience**       | Provide three comparable matters handled in the past 36 months (matter type, outcome, team size, cost range — anonymised if required). |
| **Legal project management**  | Describe the firm's approach to budget monitoring, billing transparency, and scope change management.                                  |
| **Technology and efficiency** | Describe how the firm uses technology to improve efficiency and reduce cost (AI tools, e-discovery platforms, knowledge management).   |
| **Diversity and inclusion**   | Provide team diversity data and the firm's D&I policy summary (where applicable).                                                      |
| **References**                | Provide two client references familiar with the proposed team.                                                                         |

**SECTION 4: Evaluation Criteria**

Proposals will be evaluated on:

| Criterion                            | Weight |
| ------------------------------------ | ------ |
| Technical expertise and experience   | 30%    |
| Proposed team and resourcing         | 20%    |
| Fee proposal (value and structure)   | 25%    |
| Matter plan quality and LPM approach | 15%    |
| Cultural fit and communication style | 10%    |

**⟁ CLARIFY** — Ask the user whether to adjust evaluation weights:

- "Do you want to weight price more heavily (e.g., for a commoditised matter type)
  or expertise more heavily (e.g., for a novel high-stakes matter)? I'll adjust the
  evaluation criteria accordingly."

**SECTION 5: Process and Timeline**

```
RFP issued: [date]
Clarification questions deadline: [date] (submit to [contact name/email])
Clarification responses issued: [date]
Proposal submission deadline: [date], [time], [timezone]
Shortlist notification: [date]
Presentations / interviews (shortlisted firms): [date range]
Selection decision: [date]
Engagement commencement: [date]

Submission instructions:
- Format: PDF (and editable Word for fee tables)
- Maximum length: [X] pages (excluding CVs and references)
- Submit to: [email / portal]
- Reference: [RFP reference number]
```

### Step 11: Quality Verification

Before delivering the scoping package, run these quality checks:

1. **Completeness check**: Confirm all MISSING scope elements from §4e are resolved
2. **Fee model consistency**: Confirm the budget format matches the recommended fee model
3. **Assumptions coverage**: Confirm every major cost driver has a corresponding assumption
4. **KPIs linked to milestones**: Confirm KPIs have measurement mechanisms
5. **Citation Quality Gates**: Run 5 gates (see Quality Assurance Framework)
6. **Self-Interrogation**: For any MISSING elements or HIGH-risk fee model mismatches,
   run the 3-pass self-interrogation
7. **Confidence Scoring**: Assign confidence to each fee estimate and budget range
8. **Glass Box Audit Trail**: Generate and append (see Glass Box section)

---

## Scope Completeness Classification

### COMPLETE — Fully Defined

The scope element is unambiguous, all deliverables have clear completion criteria,
and no reasonable reader could interpret the boundary differently.

**Examples:**

- "Draft and negotiate the Share Purchase Agreement and all agreed transaction documents
  through to execution. Excluded: post-closing integration, regulatory filings in
  jurisdictions other than England and the Netherlands."
- "Represent the company in the Employment Tribunal proceedings in claim ET/123/2025
  through to final hearing, including preliminary hearings, case management conferences,
  and up to three days at final hearing."

**Action**: Include as stated in the scope statement.

### PARTIAL — Defined but Incomplete

The element is present but lacks sufficient boundary definition, completion criteria,
or exclusion language to prevent scope disputes.

**Examples:**

- "Advise on employment law matters" — no limit on number of queries, no boundary on
  which employment issues are included, no exclusion of litigation
- "Handle the transaction" — no specification of which documents, which jurisdictions,
  or what "complete" means

**Action**: Develop further before finalising. Use the 4e Scope Classification Matrix
to identify what is missing.

### MISSING — Absent and Required

A critical element is absent from the scope statement. A scope statement with MISSING
elements must not be used in an engagement letter until resolved.

**Examples:**

- No dispute resolution procedure for fee disputes
- No governing law or professional rules reference
- No scope change procedure
- No definition of "completion" or "resolution" for the matter

**Action**: Add the missing element. If the user is unable to define it yet, mark
as a PLACEHOLDER and flag for resolution before signing the engagement letter.

---

## Fee Arrangement Issue Classification

Assess any issues identified in a fee arrangement proposal or existing engagement:

### STRONG — Well-Structured

The fee arrangement clearly allocates risk, has adequate scope definition, and
includes appropriate monitoring mechanisms.

**Action**: Note for awareness. No change required.

### ADEQUATE — Functional but Improvable

The fee arrangement is workable but has gaps that could cause disputes (e.g., scope
definitions are broad, contingency governance is absent, escalation triggers are not
defined).

**Action**: Recommend specific improvements. Generate remediation language.

### WEAK — At Risk

The fee arrangement has structural deficiencies likely to cause cost disputes, scope
creep, or quality degradation (e.g., capped fee with no scope statement, fixed fee
with no assumptions, no change control procedure).

**Action**: Restate the deficiency clearly, explain the specific risk, and provide
market-standard remediation language.

---

## Prioritisation Framework

Organise scope and fee issues by priority:

### Tier 1 — Pre-Engagement Blockers

Issues that must be resolved before an engagement letter is signed or an RFP is issued:

- MISSING scope elements that are essential to the matter
- No governing law or professional rules reference
- No scope change procedure
- Fee model mismatched to matter type in a way that creates material risk
- Assumptions that, if unmet, would double or treble the budget
- Compliance with local bar or procurement rules not confirmed

### Tier 2 — Pre-Work Preferences

Issues that should be resolved before substantive work begins but will not prevent
engagement:

- PARTIAL scope elements where additional definition is recommended
- Contingency governance rules not documented
- Budget escalation triggers not defined
- KPIs not agreed
- Staffing plan reviewed but not formally approved

### Tier 3 — Improvement Candidates

Issues that improve the scoping quality but can be addressed during the matter:

- Budget phase splits that could be refined as the matter develops
- Additional performance metrics beyond the minimum KPI set
- RFP evaluation weightings that could be optimised
- Template improvements based on post-matter review

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise.

| Gate           | Rule                                                                                                                | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every reference to professional rules, procurement law, or industry benchmarks cites a specific authority           | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognisable format for the jurisdiction                                         | Fix format                                               |
| **Currency**   | Every cited rule or benchmark checked for amendments                                                                | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the matter's governing professional rules. No assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated — if a budget estimate is speculative, say so                                         | Add confidence qualifier                                 |

### Self-Interrogation for MISSING Elements and HIGH-RISK Fee Mismatches

For any element classified MISSING or any fee model classified WEAK, apply this
3-pass review before delivering:

**Pass 1 — Logical Chain**: Does the risk assessment follow logically from the scope
analysis? Would a reasonable legal operations professional or outside counsel partner
reach the same conclusion on these facts?

**Pass 2 — Completeness**: Have all relevant professional rules, procurement requirements,
and matter characteristics been considered? Is there a regulatory dimension not yet
addressed?

**Pass 3 — Challenge**: What is the strongest argument that this gap is acceptable?
Under what commercial circumstances might a reasonable client proceed with the
incomplete scope or mismatched fee model?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit
trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material scope element, budget estimate, or fee recommendation, assign a
confidence level:

| Level        | Range     | Meaning                                                           | Action                                                               |
| ------------ | --------- | ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled scope, clear market practice, verified professional rules | State with confidence                                                |
| **High**     | 0.80–0.94 | Strong basis, minor questions remain                              | State with brief caveat                                              |
| **Probable** | 0.60–0.79 | Good basis but matter-specific variables could shift the estimate | State with explicit reasoning and sensitivity notes                  |
| **Possible** | 0.40–0.59 | Genuinely uncertain — early stage, limited facts                  | Flag for review with both sides of the range                         |
| **Unlikely** | 0.0–0.39  | Speculative basis                                                 | Do not assert; flag as "[ESTIMATE ONLY — requires further analysis]" |

---

## Glass Box Audit Trail

Every matter scoping output MUST include a Glass Box audit section. This makes
reasoning traceable and auditable:

```yaml
glass_box:
  matter: "[Matter name and description]"
  matter_type: "[Litigation / Transaction / Compliance / etc.]"
  perspective: "[In-house / Law firm / Legal ops]"
  fee_model_recommended: "[Hourly / Fixed / Capped / Blended / Portfolio]"
  fee_model_rationale: "[1-2 sentence summary of scoring]"
  scope_completeness:
    complete: "[number of COMPLETE elements]"
    partial: "[number of PARTIAL elements — list]"
    missing: "[number of MISSING elements — list]"
  budget_confidence: "[HIGH / MEDIUM / LOW — rationale]"
  contingency_applied: "[%]"
  phases_budgeted: "[number]"
  staffing_plan_included: "[Yes / No]"
  kpis_defined: "[Yes / No — number of KPIs]"
  rfp_template_generated: "[Yes / No]"
  legalcode_mcp: "Connected / Not connected"
  professional_rules_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review before use in binding documents"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in legal matter scoping:

1. **Scoping without historical data** — Building a budget for a matter type the firm
   or department has handled before without reviewing past matter costs, durations,
   and outcomes. Historical data is the most reliable input for any estimate. If no
   data exists, state this explicitly and widen the confidence interval.

2. **Treating the scope statement as optional** — Beginning work under a general
   retainer or a verbal description of the matter, without a written scope statement.
   Omissions in the scope statement become disputes about what was included.

3. **One-line scope descriptions** — "Handle all legal matters related to the
   acquisition" is not a scope statement. It provides no boundary, no deliverable list,
   no exclusions, and no assumption set. A scope statement that fits in one sentence
   has not been scoped.

4. **Choosing the fee model before scoping the matter** — Committing to a fixed fee
   before the scope statement is COMPLETE. Fixed fees require defined scope; without
   a scope statement, the firm prices the uncertainty rather than the work.

5. **No assumptions documentation** — Providing a budget without recording the
   assumptions on which it is based. When actual costs exceed the budget, there is no
   shared reference point for diagnosing why.

6. **Scope creep without change control** — Allowing additional work to proceed without
   a written scope change and revised budget. Each individual addition seems minor;
   collectively they double the matter cost. The absence of a change control procedure
   is the leading cause of fee disputes.

7. **Over-levering the cap** — Setting a capped fee at a level that provides false
   security. A cap set at the P50 estimate (50th percentile cost) means the firm
   absorbs costs 50% of the time — and responds by reducing effort once the cap is
   reached. A cap at P85 or higher, with an agreed scope statement, is more protective.

8. **Partner-heavy staffing plans** — Allocating partner time to tasks that could be
   performed by senior associates (document review, research, drafting first drafts of
   standard provisions). CLOC/ACC benchmarks show partner-heavy matters cost 30–50%
   more than appropriately leveraged matters for equivalent quality on routine work.

9. **Contingency as a slush fund** — Treating contingency as unallocated spend that
   outside counsel can draw on without approval. Contingency must have governance:
   who approves it, what triggers access, and how remaining contingency is reported.

10. **Ignoring disbursements** — Building a fee budget without estimating disbursements
    (filing fees, travel, expert fees, e-discovery platform costs, translation, court
    reporters). In complex matters, disbursements can equal 20–30% of total cost.

11. **Single-phase budgets** — Providing a total matter budget without phase splits.
    A single number cannot be monitored. Budget by phase enables early warning when
    one phase is over-running before the entire budget is consumed.

12. **RFP without evaluation criteria** — Issuing an RFP to law firms without defining
    how proposals will be evaluated. Firms optimise for what is scored; without
    evaluation criteria, the RFP produces proposals that are not comparable.

13. **Beauty parade without follow-up** — Shortlisting firms based on written proposals
    without interviewing the proposed team. The proposal author and the matter team
    are often different. The interview reveals the actual team's capability and the
    chemistry with the client.

14. **KPIs without measurement mechanisms** — Defining matter KPIs without specifying
    how they will be measured, who will measure them, and what happens when a KPI is
    missed. A KPI without a measurement mechanism is a wish, not a performance tool.

15. **Assuming uniform fee regulations** — Advising on fee arrangements without checking
    jurisdiction-specific professional rules. Contingency fees are restricted or
    prohibited in many civil law jurisdictions. Advertising hourly rates may be regulated.
    Fee-splitting rules vary significantly. [VERIFY local rules before finalising any
    fee arrangement.]

16. **No scope review at matter inflection points** — Treating the scope statement as
    fixed from instruction to resolution. Complex matters change — regulatory developments,
    new claims, counterparty strategy shifts. Build scope review checkpoints into the
    matter plan at major milestones.

17. **Conflating 'in scope' with 'agreed deliverables'** — Listing work streams as
    in-scope without defining what 'done' looks like for each. "Manage litigation" is
    in-scope work; "file and serve a fully particularised Particulars of Claim" is an
    agreed deliverable. The latter is measurable; the former is not.

18. **Ignoring the post-matter review** — Closing a matter without capturing actual
    vs. budgeted costs, phase durations, scope change causes, and team performance.
    Post-matter review data is the historical database for every future scope estimate
    in the same matter category.

---

## Writing Standards

Apply these standards to all scoping output:

**For scope statements** (may be shared with outside counsel or used in engagement letters):

- Plain language — no jargon or filler
- Active voice: "Outside counsel will draft..." not "Drafting will be undertaken by..."
- Short sentences — one obligation per sentence
- Name the responsible party: "the Company" or "outside counsel" — not "the party" or "it"
- Use defined terms consistently once established
- Specific, not vague: "file a Statement of Claim by [date]" not "commence proceedings"

**For budget narratives**:

- State the basis of every estimate: "Based on comparable matters handled in [period],
  estimated at [X] hours at [Y] rate"
- State confidence intervals where estimates are uncertain: "Estimate range: $X–$Y,
  depending on [specific variable]"
- Flag where assumptions drive cost: "This budget assumes [X]. If [X] proves incorrect,
  add [Y] to the budget."

**For RFPs**:

- Direct, professional tone — RFPs are business documents, not legal documents
- Lead with the company's objectives, not administrative requirements
- Evaluation criteria must be specific enough that a rational firm can optimise for them

**Quality gates before delivery:**

- [ ] No MISSING scope elements unresolved
- [ ] Fee model recommendation supported by scoring matrix
- [ ] All budget estimates have stated confidence levels
- [ ] Assumptions documented and linked to budget impact
- [ ] Scope change procedure included
- [ ] RFP (if required) has all five sections complete
- [ ] Professional rules references marked VERIFIED or [VERIFY]
- [ ] Glass Box audit trail generated

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal authority source.

**With legalcode-mcp connected (preferred):**

- Verify local bar/law society rules on fee agreement content and transparency
- Verify restrictions on alternative fee arrangements in the applicable jurisdiction
- Verify public procurement requirements (EU/UK/US/national) applicable to the matter
- Save verified references to `/tmp/legalcode-matter-scoping-authority.md`
- Mark all legalcode-mcp-sourced references as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed with the general framework
- Mark all professional-rule references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural quality, scope architecture, and fee model analysis

---

## Localization Notes

Matter scoping frameworks are substantially universal, but these elements require
local verification:

| Element                             | Local variation                                                            | Marker                  |
| ----------------------------------- | -------------------------------------------------------------------------- | ----------------------- |
| Fee agreement content               | Bar rules specify minimum content and format                               | [JURISDICTION-SPECIFIC] |
| Contingency/success fees            | Restricted or prohibited in many civil law jurisdictions                   | [JURISDICTION-SPECIFIC] |
| Rate transparency                   | Some jurisdictions require published or pre-approved rates                 | [JURISDICTION-SPECIFIC] |
| Public procurement                  | EU 2014/24/EU, UK PCR 2015, US FAR, national equivalents                   | [JURISDICTION-SPECIFIC] |
| Billing cycle                       | Local norms vary — monthly, milestone-based, stage-payment                 | [JURISDICTION-SPECIFIC] |
| Dispute resolution for fee disputes | Some bars require mandatory mediation before fee disputes can be litigated | [JURISDICTION-SPECIFIC] |
| Client money and billing accounts   | Trust accounting, IOLTA, SRA accounts rules, etc.                          | [JURISDICTION-SPECIFIC] |
| Privilege and confidentiality       | Engagement letter must not inadvertently waive privilege                   | [JURISDICTION-SPECIFIC] |

---

## Output Format Template

Deliver the matter scoping package in this format:

---

# Matter Scoping Package — [Matter Name]

**Prepared by**: [In-house / Firm name]
**Date**: [Date]
**Matter type**: [Type]
**Perspective**: [In-house / Firm]
**Version**: [Draft / Final]

---

## 1. Matter Scope Statement

### 1.1 Objectives

- Objective 1: [SMART statement]
- Objective 2: [if applicable]

### 1.2 In-Scope Work

| #   | Deliverable   | Completion Criterion     | Responsible Party            |
| --- | ------------- | ------------------------ | ---------------------------- |
| 1   | [Deliverable] | [What "done" looks like] | [Outside counsel / In-house] |

### 1.3 Out-of-Scope Exclusions

- [Exclusion 1]
- [Exclusion 2]
- [Exclusion 3+]

### 1.4 Assumptions

| #   | Assumption   | If Wrong: Cost Impact | Trigger for Re-scoping   |
| --- | ------------ | --------------------- | ------------------------ |
| 1   | [Assumption] | [+/- X%]              | [Specific trigger event] |

### 1.5 Scope Classification Summary

- COMPLETE: [N elements]
- PARTIAL: [N elements — list and remediation plan]
- MISSING: [N elements — list and required action]

---

## 2. Fee Arrangement Analysis

### 2.1 Recommended Model: [Model name]

**Scoring summary**:
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Scope certainty | [1-5] | [1 sentence] |
| Complexity | [1-5] | [1 sentence] |
| Duration | [1-5] | [1 sentence] |
| Budget certainty need | [1-5] | [1 sentence] |
| Historical data | [1-5] | [1 sentence] |
| Volume | [1-5] | [1 sentence] |
| **Total** | **/30** | |

**Risk allocation statement:**

- Client bears the risk of: [list]
- Firm bears the risk of: [list]
- Shared risks triggering review: [list]

### 2.2 Fee Model Classification: [STRONG / ADEQUATE / WEAK]

[If ADEQUATE or WEAK: specific issue and remediation language]

---

## 3. Staffing Plan

[Staffing plan table per §6]

---

## 4. Budget Framework

### 4.1 Phase Budget

| Phase              | Fees    | Disbursements | Subtotal | % of Total |
| ------------------ | ------- | ------------- | -------- | ---------- |
| [Phase 1]          | [X]     | [X]           | [X]      | [X]%       |
| [Phase 2]          | [X]     | [X]           | [X]      | [X]%       |
| Contingency ([X]%) | [X]     | [X]           | [X]      | [X]%       |
| **Total**          | **[X]** | **[X]**       | **[X]**  | **100%**   |

Confidence: [Level] — [rationale]

### 4.2 Contingency Governance

[Rules per §7]

### 4.3 Budget Escalation Triggers

[Trigger table per §7]

---

## 5. Scope Change Procedure

[Change procedure template per §8]

---

## 6. Milestone and KPI Framework

### 6.1 Milestones

| #   | Milestone   | Target Date | Completion Criterion | Gate Review? |
| --- | ----------- | ----------- | -------------------- | ------------ |
| 1   | [Milestone] | [Date]      | [Criterion]          | Yes/No       |

### 6.2 Matter KPIs

[KPI table per §9]

---

## 7. RFP Template (if applicable)

[Full five-section RFP per §10]

---

## 8. Priority Issues

### Tier 1 — Pre-Engagement Blockers

[List any Tier 1 issues with remediation actions]

### Tier 2 — Pre-Work Preferences

[List any Tier 2 issues]

### Tier 3 — Improvement Candidates

[List any Tier 3 items]

---

## 9. Glass Box Audit Trail

[YAML block per Glass Box section]

---

_Generated by legalcode-matter-scoping. AI-assisted — requires review by a qualified
legal professional before use in binding documents._

---

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- CLOC Matter Lifecycle Management Framework (Intake / Planning / Execution / Review)
- ACC Law Department Management Benchmarking Reports (2024/2025 data)
- ABA Model Rules of Professional Conduct (Rule 1.5 — fee agreements)
- CLOC Core 12 legal operations competency framework
- Persuit, Brightflag, ArgoPoint, Wolters Kluwer, and Seyfarth Shaw legal operations
  research on matter scoping, alternative fee arrangements, and outside counsel management
- ABA Law Practice Magazine 2025 (AFAs through process improvement and AI)
- Legal billing benchmarks: Brightflag 2025, Legal.io, LegalBillReview.com 2026

All professional-rule references are marked [VERIFY] unless verified via legalcode-mcp.
Users must verify currency and applicability of all cited rules before relying on them
in binding documents.
