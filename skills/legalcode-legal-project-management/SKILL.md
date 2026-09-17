---
name: legalcode-legal-project-management
description: Structure and execute legal project management (LPM) across the full matter lifecycle — from
  scope definition and task decomposition through resource allocation, budget tracking, milestone management,
  risk identification, stakeholder communication, and post-matter review. Applies IILPM Define → Plan
  → Deliver → Close methodology and CLOC Core 12 operational competency framework. Use when opening a
  new legal matter, managing an active litigation or transaction, building a matter plan for outside counsel,
  conducting a mid-matter health check, setting up a budget with LEDES/UTBMS tracking, establishing alternative
  fee arrangements (AFAs), creating a risk register for a complex matter, drafting a communication plan
  for a legal engagement, or running a post-matter retrospective. Jurisdiction-agnostic. Works for in-house
  legal departments, law firms, and legal operations professionals.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Legal Project Management

> **Disclaimer**: This skill provides a framework for AI-assisted legal project management.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Legal deadlines, filing
> requirements, and regulatory obligations are jurisdiction-specific — verify all timelines
> and requirements with counsel licensed in the applicable jurisdiction. Methodological
> references (IILPM, CLOC, UTBMS/LEDES codes, EVM formulas) are cited from research and
> carry standard hallucination risk — verify against authoritative sources before relying
> on them operationally.

---

## Purpose and Scope

This skill structures legal project management for any type of matter — litigation,
transactions, regulatory, advisory, or legal operations initiatives. It applies the
industry's leading methodologies (IILPM and CLOC) to transform unstructured legal work
into managed projects with clear scopes, budgets, milestones, and accountability.

**Covers:**

- Matter intake and scope statement development
- Work Breakdown Structure (WBS) using UTBMS task codes
- Resource allocation and staffing plan (LACI matrix)
- Budget development with phase-level tracking and EAC
- Milestone management with RAG (Red/Amber/Green) status
- Risk register creation and ongoing management
- Stakeholder communication plan and status reporting
- Alternative fee arrangement (AFA) selection and structuring
- Outside counsel guideline (OCG) compliance monitoring
- Post-matter review and lessons learned capture
- Matter health assessment with escalation triggers

**Does not:**

- Provide legal advice on the substantive merits of any matter
- Replace qualified legal counsel for substantive legal analysis
- Manage actual billing or invoice processing (requires an ELM system)
- Draft legal documents (see contract drafting and review skills)

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Legal project management methodology transcends
jurisdictional boundaries and applies to legal work in any country or legal system.

[JURISDICTION-SPECIFIC] Where this skill references legal deadlines, court filing
requirements, or regulatory timelines, those elements are jurisdiction-specific. Always:

- Verify court-imposed deadlines against local rules and applicable standing orders
- Confirm regulatory filing windows with jurisdiction-specific counsel
- Check mandatory billing format requirements (LEDES is standard in the US/UK but
  not universal)
- Verify AFA enforceability and professional responsibility implications under the
  applicable jurisdiction's rules of professional conduct

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the matter type, scope, or user's role, the workflow pauses and asks when:

- The answer would change the structure of the matter plan
- Multiple valid LPM approaches exist (e.g., fixed-fee vs. hourly, agile vs. phased)
- Budget or timeline context is needed to calibrate recommendations
- Matter type determines the applicable UTBMS code set

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

## IILPM Methodology Overview

The International Institute of Legal Project Management (IILPM) defines the gold standard
four-phase lifecycle for all legal matters, regardless of type or complexity:

```
Define → Plan → Deliver → Close
```

**Phase 1 — Define**: Understand the client's actual needs (legal and business), scope
the matter, identify stakeholders, and establish success criteria.

**Phase 2 — Plan**: Build the work breakdown structure, staffing plan, budget, risk
register, and communication plan before execution begins.

**Phase 3 — Deliver**: Execute per the plan; track budget-to-actual; manage scope
changes; update the risk register; communicate to stakeholders.

**Phase 4 — Close**: Deliver the final work product; conduct the post-matter review;
capture lessons learned; update pricing data; close the file.

**The most common LPM failure mode** is skipping or minimizing the Define and Plan
phases and jumping immediately to delivery. A well-scoped matter with a clear WBS and
budget takes hours to plan but saves days of rework.

---

## Workflow

### Step 1: Accept Matter Input

Accept the matter in any of these formats:

- **Matter description**: Free-text description of the legal engagement
- **Existing matter brief**: Document describing the parties, dispute, or transaction
- **Active matter**: A matter already underway needing a health check or plan
- **Post-matter**: A closed matter needing a retrospective review

If no matter information is provided, prompt the user to describe the engagement.

### Step 2: Gather Context

**⟁ CLARIFY** — Before building the matter plan, ask these questions. Present structured
options where possible:

1. **Matter type and phase:**
   - Options: **Litigation** (dispute, arbitration, regulatory investigation, enforcement),
     **Transaction** (M&A, financing, joint venture, restructuring),
     **Regulatory/Advisory** (regulatory compliance, government filing, opinions),
     **Legal Operations** (process improvement, technology deployment, policy development),
     **Mixed** (multiple concurrent workstreams)
   - _Why this matters_: Determines the applicable UTBMS code set (L-codes for litigation,
     P-codes for transactions, C-codes for counseling) and the milestone framework.

2. **Your role in this matter:**
   - Options: **In-house counsel** (managing outside counsel and internal team),
     **Outside counsel** (law firm managing client engagement),
     **Legal operations** (building systems or processes for a legal department),
     **Legal administrator** (tracking and reporting on a legal portfolio)
   - _Why this matters_: Determines communication direction, budget control levers, and
     the level of client-facing vs. internal content in the plan.

3. **Current phase:**
   - Options: **Opening** (new matter, building the plan from scratch),
     **Active** (matter underway, need health check or plan improvement),
     **Closing** (matter wrapping up, need close-out and retrospective)
   - _Why this matters_: Determines which IILPM phases to execute now vs. retrospectively.

4. **Fee arrangement:**
   - Options: **Hourly** (standard billing at agreed rates),
     **Fixed fee** (agreed price for the full matter or a phase),
     **Capped fee** (hourly with a billing ceiling),
     **Phased fixed fee** (separate fixed prices per phase),
     **Hybrid** (combination), **Not yet determined**
   - _Why this matters_: Determines budget tracking methodology, scope change handling,
     and the material deviation clause requirements.

5. **Budget envelope:**
   - Free text: Approved total budget, if known. If not yet determined, state "TBD."
   - _Why this matters_: Phase-level budgets must sum to the approved total; budget
     alerts are calibrated to the approved amount.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly (e.g., "I'm assuming this is an active litigation matter in the delivery phase
— correct me if that's wrong").

### Step 3: Define Phase — Matter Scope Statement

Build the matter scope statement using the components below. This is the foundational
document for all subsequent planning.

**Scope Statement Components:**

| Component                  | Description                                                                  | Why It Matters                                         |
| -------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Matter title**           | Short descriptive name                                                       | Identifier for tracking and reporting                  |
| **Project justification**  | Why this matter is being undertaken (legal and business context)             | Connects legal work to business value                  |
| **Objectives**             | Legal outcomes + business outcomes sought                                    | Defines success criteria for post-matter review        |
| **In-scope items**         | Explicit list of included workstreams                                        | Prevents scope creep by fixing boundaries              |
| **Out-of-scope items**     | Explicit exclusions — equally important as inclusions                        | The single most effective scope creep prevention tool  |
| **Key deliverables**       | Briefs, opinions, transaction documents, regulatory filings                  | Milestone anchors for progress tracking                |
| **Assumptions**            | Conditions assumed true; if false, scope or budget must be revisited         | Manages expectations when assumptions break            |
| **Constraints**            | Hard limits (budget ceiling, statutory deadlines, regulatory filing windows) | Non-negotiable boundaries                              |
| **Key milestones**         | Summary timeline (see Step 6 for full milestone plan)                        | Executive-level progress markers                       |
| **Budget envelope**        | Total approved budget + AFA structure                                        | Financial baseline                                     |
| **Fee arrangement**        | AFA type and material deviation clause if fixed-fee                          | Controls billing relationship                          |
| **Risk triggers**          | Events that will require scope change discussion                             | Proactive change control                               |
| **Change control process** | How scope changes are requested, evaluated, and approved                     | The mechanism that prevents "scope creep by agreement" |

**⟁ CLARIFY** — For the out-of-scope section, ask:

- "What work is explicitly NOT included in this matter that the client might reasonably
  assume is included?" (Examples: related appeals in a trial engagement; tax advice in a
  corporate transaction; employment claims arising from the same facts as a commercial
  dispute)

Vague scope statements are the primary cause of scope creep. Every assumption that is not
written down is a future disagreement.

### Step 4: Plan Phase — Work Breakdown Structure

Build the Work Breakdown Structure (WBS) decomposing the matter into work packages.

**WBS Construction Rules:**

- Follow the 100% rule: The WBS must capture 100% of the work within the agreed scope
- Each work package must be assignable to a single responsible person (L in the LACI matrix)
- Tasks should be estimable with reasonable confidence (2–40 hours per package)
- Align work packages to UTBMS codes for billing integration

**Standard WBS by Matter Type:**

**Litigation (L-codes):**

```
L100  Case Assessment & Administration
  L110  Fact Investigation/Development
  L120  Analysis/Strategy
  L130  Experts/Consultants
  L140  Document/File Management
  L150  Budgeting
  L160  Settlement/ADR
L200  Pre-Trial Pleadings & Motions
  L210  Pleadings
  L230  Court-Mandated Conferences
  L240  Dispositive Motions
  L250  Other Motions
L300  Discovery
  L310  Written Discovery
  L320  Document Production
  L330  Depositions
  L340  Expert Discovery
  L350  Discovery Motions
L400  Trial Preparation & Trial
  L410  Fact Witnesses
  L420  Expert Witnesses
  L440  Trial Support
  L450  Trial Attendance
L500  Appeal
  L510  Appellate Motions
  L520  Appellate Briefs
  L530  Oral Argument
L600  e-Discovery (if applicable)
  L610  Processing
  L620  Review
  L630  Production
```

**Transaction (P-codes):**

```
P100  Planning
P200  Fact Development / Due Diligence
P300  Document Drafting
P400  Negotiation
P500  Closing
P600  Post-Closing
```

**Counseling (C-codes):**

```
C100  General Advice
C200  Negotiations (non-transactional)
C300  Corporate/Entity Work
C400  Labor and Employment
C500  Tax / Benefits
```

**Activity Codes (appended to phase codes):**
| Code | Activity |
|------|----------|
| A101 | Planning |
| A102 | Research |
| A103 | Drafting |
| A104 | Document Review/Analysis |
| A105 | Communication (internal) |
| A106 | Communication (external) |
| A107 | Appearance/Attendance |
| A108 | File Management |

**⟁ CLARIFY** — For matters with high uncertainty (e.g., early-stage litigation with
unknown discovery volume), ask:

- "How much of the WBS can we define now vs. rolling-wave planning (plan near-term phases
  in detail, future phases at summary level)?"
- Rolling-wave is appropriate when: the matter is adversarial and opponent's strategy is
  unknown; regulatory matter with uncertain agency timeline; transaction with unclear due
  diligence scope.

### Step 5: Plan Phase — Resource Allocation and LACI Matrix

Assign the right people to the right tasks using the LACI matrix (Legal PM's adaptation
of the RACI model).

**LACI Role Definitions:**
| Role | Meaning | Who holds it |
|------|---------|-------------|
| **L** — Leading | Single person who owns the work package; produces the output | One person per work package |
| **A** — Assisting | Team members contributing effort; supporting the L | Multiple people |
| **C** — Consulted | Subject matter experts whose input is needed but who do not own or produce | Optional per work package |
| **I** — Informed | Stakeholders who receive updates on the outcome but do not contribute | Typically partners, clients, in-house leads |

**Why LACI, not RACI:** Legal professionals bear professional responsibility and
accountability by virtue of their license. Every L and A is already individually
accountable to their bar or law society obligations. The LACI model emphasizes leadership
and contribution rather than remapping accountability.

**LACI Matrix Template:**

```
Work Package   | Timekeeper A (Partner) | Timekeeper B (Senior Assoc.) | Timekeeper C (Associate) | Client / In-house | Expert
---------------|------------------------|------------------------------|--------------------------|-------------------|-------
L120 Strategy  | L                      | A                            | A                        | C                 | C
L110 Fact Inv. | I                      | L                            | A                        | I                 | -
L330 Depos.    | A                      | L                            | A                        | I                 | C
L420 Expert    | L                      | A                            | I                        | I                 | A
L160 ADR       | L                      | A                            | I                        | C                 | -
```

**Staffing Calibration:**

- Avoid concentration risk: no single timekeeper should be L for >60% of work packages
- Match task complexity to timekeeper level (routine research → junior; strategy → senior)
- Plan for coverage: identify backup L designations for critical-path tasks
- Check utilization: confirm each assigned timekeeper has capacity given other commitments
- Include development goals: assign stretch work packages to associates for growth

**Outside Counsel Staffing Controls (via OCGs):**

- Specify staffing expectations per task type (e.g., "L120 Strategy: partner-led;
  L320 Document Production: associate-led with partner review")
- Require pre-approval for timekeepers above the agreed rate tier
- Set maximum timekeeper count per phase to prevent over-staffing
- Require notification of staffing changes mid-matter

### Step 6: Plan Phase — Budget Development and Tracking

Build the phase-level budget and establish tracking discipline.

**Phase-Level Budget Template:**

| Phase                    | UTBMS   | Budget Hours | Budget ($) | % of Total | EAC Trigger |
| ------------------------ | ------- | ------------ | ---------- | ---------- | ----------- |
| Case Assessment (L100)   | L100    | —            | $          | —          | —           |
| Pre-Trial Motions (L200) | L200    | —            | $          | —          | —           |
| Discovery (L300)         | L300    | —            | $          | —          | —           |
| Trial Prep/Trial (L400)  | L400    | —            | $          | —          | —           |
| Expert Costs (E)         | E-codes | —            | $          | —          | —           |
| Contingency reserve      | —       | —            | $ (10–15%) | —          | —           |
| **Total (BAC)**          |         |              | **$**      | **100%**   |             |

**Earned Value Management (EVM) for Legal:**
| Metric | Formula | What It Shows |
|--------|---------|---------------|
| BAC | Approved total budget | Financial baseline |
| AC | Fees and expenses incurred to date | Actual cash outflow |
| EV | % work complete × BAC | Budgeted value of work accomplished |
| ETC | Projected remaining cost | Forward-looking cost estimate |
| EAC | AC + ETC | Total projected cost at completion |
| CPI | EV / AC | Cost efficiency ratio (1.0 = on budget; <1.0 = overspending) |
| SPI | EV / PV | Schedule efficiency ratio (1.0 = on schedule; <1.0 = behind) |

**EAC Calculation Methods:**

- When initial scope estimate was flawed: `EAC = AC + ETC (new bottom-up estimate)`
- When current spending rate will continue: `EAC = BAC / CPI`
- When remaining work will proceed per original plan: `EAC = AC + (BAC − EV)`

**Budget Alert Thresholds:**
| Threshold | Status | Required Action |
|-----------|--------|-----------------|
| >80% of budget consumed | AMBER | Outside counsel must notify client; EAC required |
| >90% of budget consumed | RED | Formal approval required for additional spend; executive briefing |
| >105% of budget reached (overrun) | CRITICAL | Stop-work until budget supplement approved; RCA required |
| CPI < 0.85 for two consecutive tracking periods | AMBER | Budget reforecast required; root cause analysis |

**AFA-Specific Budget Controls:**

| AFA Type                | Budget Tracking Approach                          | Material Deviation Trigger                     |
| ----------------------- | ------------------------------------------------- | ---------------------------------------------- |
| Fixed fee (full matter) | Scope compliance monitoring; not budget-to-actual | Client requests outside agreed scope statement |
| Phased fixed fee        | Track phase completion vs. phase price            | Phase deliverables not met; new phase added    |
| Capped fee              | Standard budget-to-actual up to cap               | Approaching cap threshold (85%)                |
| Collared fee (±10%)     | Track against target price + collar band          | EAC exceeds upper collar                       |
| Hybrid                  | Mixed tracking per component                      | As applicable per component type               |

**Material Deviation Clause Components (for fixed-fee agreements):**

- Scope change definition: what constitutes a change (specific, not "any additional work")
- Quantification method: how additional fees are calculated (hourly rate, per-unit, % uplift)
- Approval process: who approves, what documentation is required, turnaround time
- Impact on timeline: whether scope changes trigger deadline extensions

### Step 7: Plan Phase — Milestone Management

Build the milestone plan working backward from the latest non-negotiable deadline.

**⟁ CLARIFY** — Identify your hard deadlines:

- Court-imposed deadlines (answer due, discovery cutoff, trial date) — absolute, non-negotiable
- Regulatory filing windows — absolute unless extension granted
- Contractual deadlines (closing date, option exercise periods) — negotiable but costly
- Client internal deadlines (board approval, earnings call, regulatory announcement) — internal constraint

**Milestone Status Framework (RAG):**
| Status | Indicator | Meaning | Action |
|--------|-----------|---------|--------|
| **GREEN** | On track | Milestone will be met on time within budget | Standard progress update |
| **AMBER** | At risk | Milestone may be missed; warning condition | Action plan required within 48 hours; notify matter lead |
| **RED** | Critical | Milestone will be missed or is already missed | Immediate escalation; executive briefing within 24 hours |

**Milestone Plan Template:**

| #   | Milestone                   | Owner (L)   | Target Date | Hard/Soft | Buffer Days | Status        | Notes |
| --- | --------------------------- | ----------- | ----------- | --------- | ----------- | ------------- | ----- |
| M1  | Scope statement approved    | Matter lead | T+5         | Soft      | 5           | 🟢            |       |
| M2  | LACI matrix finalized       | Matter lead | T+7         | Soft      | 3           | 🟢            |       |
| M3  | Budget approved             | Client/GC   | T+10        | Soft      | 5           | 🟢            |       |
| M4  | [Phase 1 deliverable]       | [Owner]     | [Date]      | Hard/Soft | [N]         | 🟢/🟡/🔴      |       |
| M5  | [Regulatory/court deadline] | [Owner]     | [Date]      | **Hard**  | 0           | 🔴 if at risk |       |

**Deadline Management Principles:**

- Set internal deadlines at least 5 business days before external/hard deadlines
- Build court/regulatory deadlines into the calendar system, not just the milestone plan
- Never set a single milestone owner without a designated backup for court deadlines
- Treat any milestone with zero buffer as AMBER immediately upon any delay signal

### Step 8: Plan/Deliver Phase — Risk Register

Build and maintain the risk register across the matter lifecycle.

**Risk Categories for Legal Matters:**

| Category                 | Examples                                                                                                        |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Scope**                | Client requests outside agreed scope; regulatory changes mid-matter; new facts altering legal theory            |
| **Schedule**             | Judicial deadline compression; government agency delays; counterparty delay tactics; key witness unavailability |
| **Resource**             | Key attorney departure; outside counsel overcommitment; budget freeze; vendor capacity constraints              |
| **Budget**               | Discovery volume exceeds projections; expert costs underestimated; prolonged regulatory proceedings             |
| **Legal/Regulatory**     | Adverse rulings; precedent-setting decisions undercutting legal theory; new enforcement guidance                |
| **Client**               | Decision-maker change; business priority shift; unrealistic outcome expectations; approval bottlenecks          |
| **Information/Evidence** | Privilege waiver; missing/destroyed evidence; witness credibility; confidential data mishandling                |

**Risk Scoring Matrix:**

```
Impact →        1-Negligible  2-Minor  3-Moderate  4-Major  5-Critical
Probability ↓
5 - Very High       5           10        15          20        25
4 - High            4            8        12          16        20
3 - Medium          3            6         9          12        15
2 - Low             2            4         6           8        10
1 - Very Low        1            2         3           4         5

Score 15–25: RED   → Immediate escalation + mitigation required
Score  8–12: AMBER → Enhanced monitoring + contingency plan required
Score  1–6:  GREEN → Accept and document; standard monitoring
```

**Risk Register Template:**

| ID  | Risk Description                | Category | Probability | Impact     | Score | Status   | Response                                                                     | Owner   | Due    | Last Updated |
| --- | ------------------------------- | -------- | ----------- | ---------- | ----- | -------- | ---------------------------------------------------------------------------- | ------- | ------ | ------------ |
| R01 | Discovery volume 3× projected   | Budget   | 3-Medium    | 4-Major    | 12    | 🟡 AMBER | Mitigate: phase-limited e-discovery protocol; volume cap in ESI protocol     | [Owner] | [Date] |              |
| R02 | Key witness departs company     | Schedule | 2-Low       | 5-Critical | 10    | 🟡 AMBER | Mitigate: early deposition; preservation subpoena; backup witness identified | [Owner] | [Date] |              |
| R03 | Adverse summary judgment ruling | Legal    | 2-Low       | 5-Critical | 10    | 🟡 AMBER | Contingency: settlement authority request; appeal plan                       | [Owner] | [Date] |              |

**Risk Response Framework:**

- **Avoid**: Remove the risk source (e.g., narrow scope to exclude a high-risk workstream)
- **Accept**: Document and tolerate within risk appetite (low-probability, low-impact risks)
- **Transfer**: Share with third parties (insurance coverage, co-counsel on specialized risk)
- **Mitigate**: Reduce probability or impact (early filing, backup resources, scope limitation)

**Risk Register Update Cadence:**

- Litigation/complex transactions: weekly review at standing status meetings
- Advisory matters: monthly review
- Any RED risk: immediate review, do not wait for scheduled meeting
- New risk identified: add to register within 48 hours of identification

### Step 9: Deliver Phase — Stakeholder Communication

Build and execute the communication plan to keep all stakeholders appropriately informed.

**Stakeholder Analysis Matrix:**

| Stakeholder              | Role                    | Interest | Influence | Communication Strategy                                                    |
| ------------------------ | ----------------------- | -------- | --------- | ------------------------------------------------------------------------- |
| GC / Senior Partner      | Matter authority        | High     | High      | Manage closely — frequent, detailed briefings; flag RED items immediately |
| Client business lead     | Approval authority      | High     | High      | Weekly executive summaries; decisions surfaced promptly                   |
| In-house team            | Day-to-day coordination | High     | Medium    | Regular operational updates; LACI task assignments                        |
| Outside counsel          | Execution               | High     | Medium    | Kickoff, milestone reviews, OCG compliance; budget alerts                 |
| Finance / Procurement    | Budget oversight        | Medium   | High      | Monthly budget-to-actual; accrual reporting; EAC updates                  |
| Regulator                | External stakeholder    | Low      | High      | Formal communications per matter requirements                             |
| Opposing party / counsel | Adversarial             | Low      | High      | Formal only; no informal updates                                          |

**Communication Plan Components:**

| Stakeholder          | Format             | Frequency                              | Content                                                      | Owner         |
| -------------------- | ------------------ | -------------------------------------- | ------------------------------------------------------------ | ------------- |
| GC / Senior Partner  | Executive briefing | Weekly (active) / Bi-weekly (advisory) | RAG status, top risks, budget flash, decisions needed        | Matter lead   |
| Client business lead | Status memo        | Bi-weekly                              | Progress vs. milestones, key decisions, budget status        | Lead attorney |
| Internal team        | Stand-up           | Weekly (active)                        | WBS progress, blockers, upcoming milestones                  | Matter lead   |
| Outside counsel      | Status call        | Bi-weekly                              | Work product status, budget-to-actual, risk register updates | Lead attorney |
| Finance              | Budget report      | Monthly                                | Actuals, accruals, EAC, phase-level variance                 | Matter lead   |

**Status Report Template (RAG Format):**

```
MATTER STATUS REPORT
Matter: [Name]         Period: [Date range]
Phase: [Current phase] Overall Status: 🟢 GREEN / 🟡 AMBER / 🔴 RED

EXECUTIVE SUMMARY
[2-3 sentences: what happened this period, current status, next critical step]

MILESTONE STATUS
M[N] [Milestone name]: 🟢 Complete / 🟢 On track / 🟡 At risk / 🔴 Delayed
[One-line update for each milestone in the current period]

BUDGET STATUS
Approved (BAC):    $[X]
Incurred (AC):     $[X]  ([Y]% of BAC)
Projected (EAC):   $[X]  [▲ OVER / ▼ UNDER] by $[Z] ([W]%)
CPI:               [X] (>1.0 = under budget; <1.0 = over budget rate)

OPEN RISKS
[List active AMBER and RED risks from risk register; one line each]

DECISIONS REQUIRED
[List any decisions that require client or GC approval before work can proceed]

NEXT STEPS
[3-5 bullet points: what happens in the next reporting period]

BUDGET ALERT: [If applicable: "EAC exceeds BAC by $X. Formal approval required before
additional expenditure. See attached EAC analysis."]
```

**⟁ CLARIFY** — Ask the user about communication boundaries before finalizing the plan:

- "Is there a 'no surprises' rule? (i.e., must anything material be escalated before a
  scheduled report?)"
- "Who has authority to approve scope changes and budget supplements in this matter?"
- "Does outside counsel communicate directly with the client, or through in-house counsel?"

### Step 10: Close Phase — Post-Matter Review

Execute the post-matter retrospective to capture lessons learned and improve future
matter management.

**⟁ CLARIFY** — For the post-matter review, ask:

- "Was the matter outcome: favorable / unfavorable / settlement / mixed?"
- "Were there budget variances? (Over/under and by how much?)"
- "Were there any significant process failures to analyze?"

**Post-Matter Review Agenda (60–90 minutes):**

**Section 1 — Outcome Assessment**

- What was the legal outcome? What was the business outcome?
- Did the matter achieve its stated objectives (from the scope statement)?
- Was the outcome affected by LPM decisions (e.g., resource allocation, risk response)?

**Section 2 — Budget Performance**

- Approved BAC vs. actual AC: dollar and percentage variance
- Which phases drove variance? What were the root causes?
- Were early warning indicators identified and acted on promptly?
- Should future budget models for this matter type be recalibrated?

**Section 3 — Timeline Performance**

- Were milestones met? For any that were missed: root cause? Could it have been prevented?
- Were any court or regulatory deadlines at risk? How were they managed?
- What buffering or scheduling decisions worked well?

**Section 4 — Scope Management**

- Was the scope well-defined at the outset?
- How many scope changes occurred? Were they managed through the change control process?
- What out-of-scope assumptions were incorrect?

**Section 5 — Communication Effectiveness**

- Did all stakeholders feel appropriately informed?
- Were there communication failures (surprises, delays in escalation, unclear decisions)?
- Would any stakeholder change the communication format or frequency?

**Section 6 — Risk Management**

- Which risks materialized? Were they in the risk register?
- Which risks were identified but not flagged? Why?
- Were risk responses effective when triggered?

**Section 7 — Team Performance**

- Were the right people on the right tasks (LACI review)?
- Were workloads balanced? Were development goals achieved?
- Did outside counsel perform per expectations?

**Section 8 — Lessons Learned and Action Items**

- What three things worked well and should be repeated?
- What three things would you change if starting this matter again?
- What updates to templates, checklists, or playbooks should result?

**Post-Matter Review Outputs:**

- Lessons learned document → input to future matter templates
- Revised matter plan templates (incorporate lessons into standard forms)
- Updated pricing data → calibrate future AFA models for this matter type
- Knowledge management entries → precedents, playbooks, clause libraries
- Outside counsel performance assessment → annual panel review input

---

## Matter Health Assessment Framework

### Health Status Classification

Apply this three-tier framework to assess the current state of an active matter:

**GREEN — On Track**
All conditions met: budget within 80% of approved; no milestones delayed; all RED and
AMBER risks have active response plans; communication plan being executed; scope stable.

**Action**: Standard progress update. No escalation required.

---

**AMBER — At Risk**
Any one of the following: budget consumed between 80–90% with significant work remaining;
milestone delayed but recovery plan in place; new HIGH-probability or HIGH-impact risk
identified; scope change in progress without approved change order; communication plan
falling behind schedule; CPI between 0.85 and 0.95 for two consecutive periods.

**Action**: Matter lead prepares action plan within 48 hours. Notify senior partner or
GC. Brief client on status. Update risk register. Prepare EAC reforecast.

---

**RED — Critical**
Any one of the following: budget exceeded without approved supplement; court or
regulatory deadline at risk; key milestone will be missed with no recovery path; risk
materialized and no response plan in place; scope dispute with client unresolved; outside
counsel invoiced in breach of OCGs and not remediated; key resource (L on critical-path
task) lost without replacement.

**Action**: Immediate escalation to GC or senior management. Executive briefing within
24 hours. Formal approval required before additional expenditure. Engage matter management
team to deploy contingency plan. Document root cause.

---

**CRITICAL — Imminent Deadline or Malpractice Risk**
Any one of the following: court filing deadline within 48 hours and work not complete;
statutory deadline at risk of being missed; privilege waiver or adverse discovery ruling
has occurred; work product error discovered that could affect the client's legal position.

**Action**: All-hands emergency mobilization. GC / senior partner notified immediately.
Malpractice risk assessment. Engage professional responsibility counsel if needed.
Document all actions contemporaneously.

---

### Actionable Response by Status Level

**For each AMBER finding:**

1. Identify the root cause (scope change? resource gap? underestimation? adversarial disruption?)
2. Assess whether the AMBER will self-resolve or escalate to RED
3. Build a specific recovery plan with named owner and deadline
4. Update the risk register with the AMBER trigger as an identified risk
5. Prepare a one-paragraph client briefing paragraph for the next status report

**For each RED finding:**

1. Immediate notification to matter authority (GC, senior partner, client relationship partner)
2. Root cause analysis (same session — do not defer)
3. Contingency plan activation (identify the best available option from plans A/B/C)
4. Budget supplement or scope modification request (with supporting analysis)
5. Document all decisions and actions in the matter file contemporaneously
6. Post-matter review scheduled at close (do not wait — book the date now)

---

## AFA Selection and Structuring Framework

Select the appropriate fee arrangement based on matter characteristics:

| AFA Type                  | Best For                                                                                        | Key Scope Requirements                                                                  | Key Risk                                                                      |
| ------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Fixed/Flat Fee**        | Routine, repeatable matters with narrow variability (standard contract review, routine filings) | Explicit scope statement; detailed in/out-of-scope list; change order process           | Scope creep eats margin — firm bears overrun risk                             |
| **Capped Fee**            | Uncertain matters with estimable maximum (contested motion practice, regulatory response)       | Cap amount; tasks included in cap; billing increments up to cap                         | Firm bears overrun risk above cap; client loses visibility below cap          |
| **Phased Fixed Fee**      | Multi-phase matters where each phase has a definable scope (transactions, complex litigation)   | Phase definitions with clear entry/exit criteria; termination pricing per phase         | Early termination pricing must be addressed; phase boundary disputes          |
| **Collared Fee**          | Predictable matters with minor uncertainty (advisory opinions, repeat transaction types)        | Target price + collar band (typically ±10–15%); adjustment mechanism above/below collar | Collar calculation disputes; requires accurate baseline estimate              |
| **Blended Rate**          | Multi-tier teams where task mix is uncertain (general outside counsel relationships)            | Agreed blended rate per matter type; no pre-approval for team composition changes       | Staffing gaming (senior attorneys replaced by juniors to improve realization) |
| **Contingency**           | Plaintiff-side disputes; personal injury; class actions                                         | Recovery definition; percentage agreed; expenses allocation                             | Ethics rules vary by jurisdiction [JURISDICTION-SPECIFIC] [VERIFY]            |
| **Reverse Contingency**   | Defense matters (cost savings-based)                                                            | Baseline "savings expected without counsel"; savings definition; sharing formula        | Savings definition disputes; court-imposed outcomes vs. counsel strategy      |
| **Subscription/Retainer** | Ongoing advisory relationships (general counsel outsourcing, recurring regulatory work)         | Monthly scope cap (hours or matter types); overage mechanism; unused hours policy       | Scope creep; firm under-resources the relationship at flat rate               |

**AFA Implementation Checklist:**

- [ ] Scope statement completed and approved before AFA price agreed
- [ ] Material deviation clause included (what triggers a price adjustment)
- [ ] Adjustment quantification method agreed (hourly rate × excess hours, per-unit, % uplift)
- [ ] Change order approval process documented
- [ ] Phase exit criteria defined (for phased fixed fee)
- [ ] Termination pricing agreed (if matter terminates mid-way)
- [ ] Professional responsibility compliance confirmed [JURISDICTION-SPECIFIC] [VERIFY]

---

## CLOC Core 12 — Legal Operations Integration

Map matter management activities to the CLOC Core 12 competencies for legal department
maturity assessment:

| CLOC Competency                | LPM Integration Points                                                     |
| ------------------------------ | -------------------------------------------------------------------------- |
| **Financial Management**       | Phase-level budgeting; EAC tracking; AFA management; variance analysis     |
| **Firm and Vendor Management** | OCG compliance; panel firm performance; AFA negotiation; diversity metrics |
| **Practice Operations**        | Matter templates; WBS standards; milestone frameworks; change control      |
| **Project/Program Management** | Matter plan; LACI matrix; risk register; communication plan                |
| **Knowledge Management**       | Post-matter lessons learned; precedent capture; playbook updates           |
| **Business Intelligence**      | KPI dashboards; cost-per-matter-type; cycle time; budget adherence rate    |
| **Technology**                 | ELM system integration; e-billing (LEDES); matter management platform      |
| **Service Delivery Models**    | Build/buy/borrow decisions; staffing tier calibration; AFA selection       |

**CLOC Maturity Self-Assessment for LPM:**
| Maturity Level | LPM Characteristics |
|----------------|---------------------|
| **Reactive** | No formal matter plans; budgets created after-the-fact; no risk registers; communication ad hoc |
| **Emerging** | Matter plans for large matters only; some phase-level budgets; inconsistent milestone tracking |
| **Developing** | Formal plans for all matters above threshold; consistent budget tracking; regular status reports; some post-matter reviews |
| **Leading** | All matters planned; EVM applied; risk registers updated regularly; OCG compliance enforced; post-matter reviews mandatory; KPIs tracked and benchmarked |

**Target state for most in-house legal departments:** Developing → Leading over a 12–18
month LPM deployment program.

---

## Legal Operations KPIs Reference

Track these KPIs to measure LPM effectiveness over time:

**Financial KPIs:**
| KPI | Formula | Benchmark |
|-----|---------|----------|
| Budget Adherence Rate | % of matters closing within approved budget | >75% (leading departments) |
| Cost Per Matter (by type) | Total spend ÷ matter count (by type) | Compare to prior year and peer benchmarks |
| AFA Adoption Rate | AFA matters ÷ total matters | >50% (CLOC leading benchmark) |
| Outside Counsel Spend as % of Revenue | OC spend ÷ company revenue | <0.5% for well-managed departments [VERIFY] |

**Efficiency KPIs:**
| KPI | Formula | Target |
|-----|---------|--------|
| Matter Cycle Time (by type) | Open date to close date by matter type | Benchmark against prior period |
| Budget Alert Response Time | Days from alert trigger to recovery plan | <5 business days |
| Post-Matter Review Completion Rate | Reviews completed ÷ reviews required | 100% for matters above threshold |

**Outside Counsel KPIs:**
| KPI | Formula | OCG Trigger |
|-----|---------|------------|
| OCG Compliance Rate | Compliant invoices ÷ total invoices | >95% before auto-approval enabled |
| Budget Proactivity | Alerts raised before 80% threshold ÷ total matters | Track trend; flag firms below 50% |
| Diversity Hours Rate | Hours by diverse timekeepers ÷ total hours | Per department diversity commitment |
| Realization Rate | Value of hours invoiced ÷ total billable hours worked | Identify write-off patterns |

---

## Quality Assurance Framework

### PDCA Quality Cycle Applied to LPM

**PLAN**: Build the scope statement, WBS, LACI matrix, budget, milestone plan, risk
register, and communication plan before delivery begins. A matter without a plan is
managed reactively.

**DO**: Execute per the plan. Track budget-to-actual weekly. Update milestones with RAG
status. Update the risk register at each status meeting. Communicate per the communication
plan. Manage scope changes through the change control process.

**CHECK**: Conduct the mid-matter health assessment at each major milestone. Run the
Citation Quality Gates before any external deliverable. Verify that all AMBER and RED
triggers are being monitored with response plans. Confirm that the EAC is current.

**ACT**: Capture lessons learned as the matter progresses, not just at close. Feed
process improvements back into matter templates. Update AFA pricing models with actual
cost data. Identify outside counsel performance trends.

### Citation Quality Gates

Run these 5 gates silently before delivering any LPM output to external stakeholders:

| Gate           | Rule                                                                                      | Fail Action                                                                         |
| -------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Source**     | Every methodology reference cites a specific framework, standard, or established practice | Add citation or mark "[UNVERIFIED — verify against authoritative source]"           |
| **Format**     | All UTBMS/LEDES references use the correct code format                                    | Verify against current UTBMS code set [VERIFY]                                      |
| **Currency**   | UTBMS codes, AFA market practice, and EVM formulas checked for current applicability      | Flag "[CHECK CURRENCY — codes may have been updated]"                               |
| **Domain**     | LPM advice stays within project management scope; legal substance deferred to counsel     | Flag any substantive legal conclusions as "[LEGAL SUBSTANCE — verify with counsel]" |
| **Confidence** | Uncertainty about matter-specific projections explicitly stated                           | Add confidence qualifier to any forecast or estimate                                |

### Self-Interrogation for RED/CRITICAL Items

For any matter classified as RED or CRITICAL, apply this 3-pass self-interrogation:

**Pass 1 — Factual Chain Integrity**: Does the RED classification follow logically from
the facts? Is the risk trigger real or anticipated? Would a reasonable LPM practitioner
reach the same escalation decision?

**Pass 2 — Completeness**: Have all response options been identified? Are there recovery
paths not yet considered? Has the root cause been traced to its source (not just the
symptom)?

**Pass 3 — Challenge**: What is the strongest argument that this is AMBER, not RED?
Under what conditions could the matter recover to GREEN without escalation? Is the
classification proportionate to the actual risk?

If any pass reveals that the classification is too severe or incomplete, revise before
delivering. Mark the audit trail with `self_interrogation: PASS` or
`self_interrogation: REVISED`.

### Confidence Scoring

Apply confidence levels to all projections and estimates in the matter plan:

| Level        | Range     | Meaning                                                   | Action                                                                                |
| ------------ | --------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Hard deadline or contractual commitment; no uncertainty   | State as fact                                                                         |
| **High**     | 0.80–0.94 | Strong historical basis; comparable matter data available | State with brief caveat                                                               |
| **Probable** | 0.60–0.79 | Reasonable estimate with acknowledged uncertainty         | State with explicit assumption basis and range                                        |
| **Possible** | 0.40–0.59 | Genuinely uncertain; early-stage matter with limited data | Present as range; flag for review at first major milestone                            |
| **Unlikely** | 0.0–0.39  | Highly speculative; insufficient basis to project         | Do not present as estimate; flag as "[INSUFFICIENT BASIS — reassess at [milestone]"]" |

---

## Glass Box Audit Trail

Every matter plan and health assessment MUST include a Glass Box section:

```yaml
glass_box:
  skill_name: "legalcode-legal-project-management"
  matter_name: "[Matter name/number]"
  matter_type: "[Litigation / Transaction / Regulatory / Advisory / Legal Operations]"
  iilpm_phase: "[Define / Plan / Deliver / Close]"
  user_role: "[In-house counsel / Outside counsel / Legal operations / Administrator]"
  fee_arrangement: "[Hourly / Fixed / Capped / Phased Fixed / Hybrid / TBD]"
  utbms_code_set: "[L-codes / P-codes / C-codes / Mixed]"
  budget_bac: "$[approved budget or 'Not established']"
  budget_ac: "$[incurred to date or 'N/A']"
  budget_eac: "$[current estimate at completion or 'N/A']"
  matter_status: "[GREEN / AMBER / RED / CRITICAL]"
  open_risks: "[number] RED / [number] AMBER / [number] GREEN"
  milestones_at_risk: "[number or 'None']"
  legalcode_mcp: "Connected / Not connected"
  methodology_references:
    - "IILPM Define-Plan-Deliver-Close framework [VERIFY current framework version]"
    - "CLOC Core 12 Competencies [VERIFY current edition]"
    - "UTBMS code set [VERIFY currency against current ABA/ACC code set]"
    - "LEDES 1998B format [VERIFY current applicable standard]"
    - "PMBOK EVM formulas [VERIFY against current PMBOK edition]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale, e.g., 'MEDIUM — new matter with limited historical data']"
  limitations:
    - "[Any scope limitations, e.g., 'Budget projection assumes no discovery disputes']"
    - "[Any missing information, e.g., 'Opposing party strategy unknown — risk register will evolve']"
    - "[Jurisdiction assumptions, e.g., 'US federal litigation — verify for state court rules']"
  reviewer: "AI-assisted — requires qualified legal professional review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in legal project management:

1. **Skipping the Define phase** — Opening a matter and immediately assigning tasks
   without a written scope statement. The Define phase takes hours; the rework from an
   undefined scope takes weeks. A matter without a scope statement is not a project —
   it is a promise waiting to be broken.

2. **Vague scope statements** — Writing scope statements with language like "all necessary
   legal services" or "assist with the dispute." Every assumption not documented is a
   future disagreement. Explicit out-of-scope lists are as important as in-scope lists.

3. **Scope creep by agreement** — Both inside and outside counsel informally agreeing to
   expand scope without a change order, budget adjustment, or written confirmation.
   This pattern creates billing surprises and accountability failures at the worst moments.

4. **Total-level budgeting without phase-level breakdown** — A single $500K budget with
   no phase allocation provides no early warning capability. Overruns in discovery are
   invisible until the bill arrives. Phase-level budgets are the minimum required for
   proactive management.

5. **No EAC reforecast discipline** — Tracking actuals against the original budget but
   never updating the estimate at completion. The EAC is the management instrument; the
   budget-to-actual is the rearview mirror. Matter leads who do not maintain a current
   EAC are managing in the dark.

6. **Reporting actual hours without accounting for WIP** — Monthly budget reports that
   omit outside counsel work-in-progress (unbilled time) create false comfort. Require
   monthly WIP accruals from outside counsel for all matters above budget thresholds.

7. **Single-owner risk register** — The risk register updated only by the matter lead
   and not reviewed at team meetings. Risks are identified at every level of the team.
   Stand-up meetings should include a standing risk register update item.

8. **Treating court deadlines as flexible** — Court-imposed deadlines are absolute. A
   milestone plan that treats them like soft targets creates malpractice risk. Every
   court or regulatory deadline must have a buffer internal deadline at least 5 business
   days earlier, with a single named owner and a designated backup.

9. **LACI matrix with no Leading role assigned** — Listing all senior timekeepers as
   "Assisting" with no single Leading designation on a work package creates the "everyone
   responsible = no one responsible" failure mode. Critical-path tasks must have a single L.

10. **Communication plan designed for the matter lead, not the stakeholders** — Sending
    technical litigation updates to finance teams, or executive summaries to the litigation
    team. Communication calibration requires understanding what each audience needs and
    tailoring format and frequency accordingly.

11. **Status reports without escalation triggers** — A status report that says "all is
    well" when the CPI is 0.82 is not a status report; it is a false assurance. Every
    status report must surface any AMBER or RED trigger, even if the matter lead believes
    it will self-resolve.

12. **Post-matter review avoidance** — The most consistently skipped phase in legal PM.
    Teams cite time pressure and the desire to move to the next matter. This creates a
    compounding learning deficit. Post-matter reviews for matters above a threshold should
    be booked at matter opening, not at close.

13. **AFA without a material deviation clause** — A fixed-fee agreement with no mechanism
    for scope-driven price adjustments is an agreement to litigate about scope. The
    material deviation clause is not optional — it is the structural protection for both
    sides.

14. **Outside counsel selected before scope is defined** — Engaging outside counsel and
    then building the scope statement around their capabilities. Matter scope should be
    defined first; counsel selection criteria should flow from scope requirements. This
    prevents overstaffing and specialization mismatches.

15. **Ignoring OCG compliance until invoice dispute** — Treating outside counsel guidelines
    as aspirational rather than contractual. OCG violations compound: a firm that knows
    guidelines are not enforced will continue billing in ways that generate billing disputes.
    e-Billing system enforcement at invoice receipt is more effective than retroactive dispute.

16. **Risk register populated once and never updated** — A risk register created at matter
    opening and not reviewed again is a legal liability, not a management tool. Active
    matters generate new risks at every hearing, deposition, and status meeting. The register
    must be a living document.

17. **Confusing matter success with process success** — A matter that achieves a favorable
    outcome despite poor LPM practices reinforces bad habits. Post-matter reviews must
    evaluate process quality independent of outcome. A well-managed matter can have an
    unfavorable outcome; a poorly-managed matter can win by luck.

---

## Writing Standards

Apply plain-language discipline to all LPM outputs:

**For status reports** (shared with senior stakeholders and clients):

- Plain language; no legal or project management jargon
- Active voice: "The team will file the motion by [date]" not "The motion will be filed by the team"
- One point per sentence; short sentences
- RAG status must appear in the first line — the reader should know the status before reading the body
- Numbers must be explicit: "$245K incurred of $300K approved (82%)" not "most of the budget has been used"

**For scope statements** (shared with outside counsel and clients):

- Defined terms must be used consistently throughout
- In-scope and out-of-scope lists must use parallel structure
- Every assumption must be testable: "We assume no more than 500,000 pages of responsive documents" is testable; "We assume discovery will be manageable" is not
- Change control process must be specific: who, how, in what timeframe

**Quality gates before delivery:**

1. Can a non-lawyer business stakeholder understand the executive summary without assistance?
2. Is the matter status unambiguous in the first paragraph?
3. Are all budget figures concrete (not ranges or approximations, unless explicitly a projection)?
4. Are all escalation triggers and responsible owners named?
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-specific filing deadlines and mandatory procedures
  that affect the milestone plan
- In Step 4, verify current UTBMS code applicability for the matter type and jurisdiction
- In Step 8, search for regulatory developments that may affect the risk register
- Mark all legalcode-mcp-sourced references as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all UTBMS code references with [VERIFY] against current ABA/ACC code set
- Mark all jurisdiction-specific deadline references with [JURISDICTION-SPECIFIC] [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the matter plan on structural quality (scope, WBS, budget framework, risk categories)
  rather than jurisdiction-specific content depth

**With an ELM system connected (e.g., TeamConnect, SimpleLegal, Legal Tracker):**

- Use the ELM's UTBMS code set rather than the generic set in this skill
- Pull budget-to-actual data from the ELM rather than re-entering
- Feed the matter plan's milestone dates into the ELM matter management record
- Route OCG compliance monitoring through the ELM's invoice review workflow

**Without an ELM system:**

- Use spreadsheet templates for budget-to-actual tracking
- Note in the Glass Box: `elm_system: "Not integrated — manual tracking required"`
- Recommend ELM deployment if the organization manages >50 concurrent matters

---

## Localization Notes

This skill is jurisdiction-agnostic but requires local adaptation in these areas:

| Element                                    | Localization Required                                                                                                                                          |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **UTBMS codes**                            | Standard in US; adopted in parts of UK/Australia/Canada; verify local billing standard requirements [JURISDICTION-SPECIFIC]                                    |
| **LEDES format**                           | LEDES 1998B (US standard); LEDES XML formats for international use; some jurisdictions use local standards [JURISDICTION-SPECIFIC]                             |
| **AFA ethics rules**                       | Contingency fees prohibited in many civil law jurisdictions (France, Germany); conditional fee rules vary in UK and Australia [JURISDICTION-SPECIFIC] [VERIFY] |
| **Court deadlines**                        | Jurisdiction-specific; verify against local court rules, standing orders, and applicable procedural codes [JURISDICTION-SPECIFIC]                              |
| **Statutory limitation periods**           | Affect milestone urgency for regulatory filings and appeal windows; verify per jurisdiction [JURISDICTION-SPECIFIC] [VERIFY]                                   |
| **Professional responsibility**            | Billing practices, fee arrangements, and communication standards are regulated by local bars/law societies [JURISDICTION-SPECIFIC] [VERIFY]                    |
| **Outside counsel diversity requirements** | Vary by client OCG; not legally mandated but increasingly contractual [VERIFY current market practice]                                                         |

---

## Output Format Template

Use this template for the matter plan deliverable:

```markdown
# Matter Plan: [Matter Name]

**Matter ID**: [Number]
**Opened**: [Date]
**Matter Lead**: [Name, role]
**IILPM Phase**: [Define / Plan / Deliver / Close]
**Overall Status**: 🟢 GREEN / 🟡 AMBER / 🔴 RED

---

## 1. Scope Statement

**Matter justification**: [Why this matter is being undertaken]
**Objectives**:

- Legal: [Legal outcomes sought]
- Business: [Business outcomes sought]
  **In scope**: [Explicit list]
  **Out of scope**: [Explicit list — equally important]
  **Key deliverables**: [List]
  **Assumptions**: [List — each must be testable]
  **Constraints**: [Hard limits on budget, timeline, scope]
  **Fee arrangement**: [AFA type and terms]
  **Change control**: [Who approves, how, in what timeframe]

---

## 2. Work Breakdown Structure (WBS)

[UTBMS-coded work packages organized by phase]

---

## 3. LACI Matrix

[Table: work packages × team members, with L/A/C/I designations]

---

## 4. Budget

| Phase | UTBMS | Budget ($) | Incurred ($) | % Used | EAC ($) | Status |
| ----- | ----- | ---------- | ------------ | ------ | ------- | ------ |

[Rows per phase]

**BAC (approved total)**: $[X]
**AC (incurred to date)**: $[X] ([Y]%)
**EAC (current projection)**: $[X] ([▲/▼] $[Z] vs. BAC)
**CPI**: [X]

---

## 5. Milestone Plan

| #   | Milestone | Owner | Target | Hard/Soft | Buffer | Status |
| --- | --------- | ----- | ------ | --------- | ------ | ------ |

[Rows per milestone]

---

## 6. Risk Register

| ID  | Risk | Category | P   | I   | Score | Status | Response | Owner |
| --- | ---- | -------- | --- | --- | ----- | ------ | -------- | ----- |

[Rows per risk — include all active risks]

---

## 7. Stakeholder Communication Plan

| Stakeholder | Format | Frequency | Content | Owner |
| ----------- | ------ | --------- | ------- | ----- |

[Rows per stakeholder group]

---

## 8. Open Issues

| #   | Issue | Owner | Due | Status |
| --- | ----- | ----- | --- | ------ |

[Rows for open issues requiring decisions]

---

## Glass Box Audit Trail

[YAML block as defined in the Glass Box section above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis applying the IILPM
Define-Plan-Deliver-Close methodology, CLOC Core 12 operational competency framework,
PMBOK Earned Value Management adapted to legal work, and UTBMS/LEDES billing code
standards to a production-quality AI skill for legal project management. Research
conducted via web search across IILPM, CLOC, ACC, Brightflag, PERSUIT, and legal
operations practitioner sources. All methodology references marked [VERIFY] should be
confirmed against current editions of the relevant framework documentation.
