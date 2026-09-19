---
name: legalcode-mediation-preparation
description: Prepare comprehensive mediation materials including opening and confidential mediation statements,
  BATNA/WATNA/MLATNA analysis, settlement range development with probability-weighted outcomes, zone of
  possible agreement (ZOPA) identification, and strategic concession planning. Use when preparing for
  a commercial mediation session, selecting a mediator, organizing pre-mediation discovery and evidence,
  confirming settlement authority and decision-maker attendance, drafting opening statements, or developing
  phase-by-phase negotiation tactics.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Prepare comprehensive mediation materials including opening and confidential mediation statements, BATNA/WATNA/MLATNA analysis, settlement range development with probability-weighted outcomes, zone of possible agreement (ZOPA) identification, and strategic concession planning. Use when preparing for a commercial mediation session, selecting a mediator, organizing pre-mediation discovery and evidence, confirming settlement authority and decision-maker attendance, drafting opening statements, or developing phase-by-phase negotiation tactics. Evaluates cost-benefit of settlement vs. continued litigation with risk-adjusted present value analysis. Covers mediator selection criteria, multi-party coordination, joint session and caucus strategy, impasse diagnosis, and exit protocols. Supports evaluative and facilitative mediation approaches from claimant, defendant, or multi-party perspectives. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for US, UK, and AU mediation practice and settlement enforceability. Integrates with legalcode-settlement-negotiation for settlement corridor modeling, legalcode-early-case-assessment for merits input, and legalcode-damages-calculation for exposure quantification.


# Legalcode Mediation Preparation

> **Disclaimer**: This skill provides a framework for AI-assisted mediation preparation in
> civil disputes. It does not constitute legal advice, mediation strategy, or a substitute
> for qualified legal counsel and professional mediators licensed in the relevant
> jurisdiction. Settlement positions, BATNA/WATNA/MLATNA assessments, and concession
> strategies produced by this skill are analytical frameworks, not binding representations.
> Mediation procedures, confidentiality protections, and settlement enforceability vary
> significantly by jurisdiction and dispute type. All outputs should be reviewed by
> qualified legal counsel before use. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill prepares a comprehensive mediation package for civil disputes proceeding to
mediation. It operationalizes the full pre-mediation workflow — from mediator selection
and brief drafting to BATNA/WATNA analysis, concession planning, and impasse exit
protocols — into a decision-ready deliverable.

This skill is **operationally distinct** from `legalcode-settlement-negotiation`, which
builds the macro settlement framework. Use both skills in sequence: run
`legalcode-settlement-negotiation` first to establish the settlement corridor and
probability model, then run this skill to operationalize those parameters for the
mediation event itself. If no prior settlement analysis exists, this skill can build
BATNA/WATNA/MLATNA from scratch.

**Covers:**

- BATNA (Best Alternative to Negotiated Agreement), WATNA (Worst Alternative to
  Negotiated Agreement), and MLATNA (Most Likely Alternative to Negotiated Agreement)
  analysis with probability weighting
- ZOPA (Zone of Possible Agreement) identification, corridor mapping, and gap analysis
- Risk-adjusted present value (RAPV) comparison of settlement vs. continued litigation
- Settlement range development: floor, target, ceiling with confidence scoring
- Mediation statement drafting: opening (shared) and confidential (mediator-only)
- Mediator selection criteria: evaluative vs. facilitative style, experience, neutrality
- Pre-mediation discovery organization: evidence summary, damages package, liability brief
- Settlement authority confirmation and decision-maker attendance logistics
- Opening statement preparation: narrative strategy, tone, credibility signaling
- Phase-by-phase mediation tactics: opening, joint session, caucus, impasse, closing
- Concession planning: cadence, sequencing, magnitude, package deal engineering
- Multi-party coordination: co-claimant/co-defendant alignment, competing interests
- Impasse diagnosis: genuine vs. tactical; mediator adjudication options; exit protocols
- Non-monetary term valuation: release scope, confidentiality, behavioral commitments

**Does not:**

- Replace qualified legal counsel, mediators, or binding legal advice
- Draft final settlement agreements or term sheets (see `legalcode-settlement-negotiation`
  and contract drafting skills)
- Provide forensic accounting or economic expert opinions
- Apply to criminal proceedings, plea negotiations, or sentencing
- Guarantee mediation success — mediation depends on party autonomy and process dynamics

**Related skills:**

- `legalcode-settlement-negotiation` — Macro BATNA/WATNA framework and concession design
- `legalcode-early-case-assessment` — Merits, exposure, and procedural leverage input
- `legalcode-damages-calculation` — Granular damages quantification for the corridor
- `legalcode-litigation-risk-assessment` — Full four-dimensional litigation risk matrix
- `legalcode-privilege-review` — Protecting mediation preparation materials as work product

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the substantive governing law
and the mediation forum first, then localize the analysis.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

**Mediation procedure and confidentiality:**

- Mediator qualification requirements (certification, licensing, ethical rules)
- Mediation statement privilege and confidentiality scope
- Admissibility of mediator communications in subsequent proceedings
- Court-ordered vs. voluntary mediation obligations

**Settlement enforceability:**

- Written settlement agreement requirements (when oral agreements bind)
- Court approval requirements (class actions, minor parties, protected persons)
- Tax treatment of settlement proceeds (income vs. capital vs. damages exclusion)

**Reference anchors frequently needed:**

**United States (Federal):**

- FRE Rule 408: Settlement offer admissibility protection [VERIFY]
- Uniform Mediation Act (UMA), adopted in 12+ states: Mediator privilege [VERIFY]
- FRCP Rule 16(c)(2)(I): Court-ordered mediation authority [VERIFY]
- FRCP Rule 68: Offer of judgment and cost consequences [VERIFY]
- Cal. Evidence Code §§1115–1128: California Mediation Confidentiality Act [VERIFY]
- IRC §104(a)(2): Exclusion of physical injury damages from gross income [VERIFY]

**United Kingdom:**

- CPR Part 36: Offers to settle and cost consequences of rejection [VERIFY]
- CPR Part 3.1(2)(f): Court power to order ADR [VERIFY]
- CPR 1.4(2)(e) (amended October 1, 2024): Active case management includes ADR [VERIFY]
- _Churchill v Merthyr Tydfil CBC_ [2023] EWCA Civ 1416: Court may compel ADR [VERIFY]
- Calderbank letters: Without-prejudice cost protection [VERIFY]
- Tomlin Orders: Consent orders with confidential schedule [VERIFY]

**Australia:**

- Federal Court Act 1976 (Cth) §53A: Court-ordered mediation [VERIFY]
- National Mediation Accreditation System (NMAS): Mediator standards [VERIFY]
- Federal Court Rules 2011 Div 26.2: Compulsory ADR referral [VERIFY]
- _Tapoohi v Lewenberg_ [2003] VSC 410: Enforceability of mediation agreements [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses
and asks when:

- The answer would materially change the mediation strategy
- Multiple valid approaches exist and the user's business context matters
- Stakeholder authorization or multi-party dynamics create forks
- Mediator style preference affects the analytical direction

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

### Step 1: Accept the Matter Input

Accept input in any of these formats:

- **File**: Mediation order, court scheduling order, demand letter, prior ECA, or damages memo
- **URL**: Link to a matter in a case management system or CLM
- **Pasted text**: Summary of facts, claims, defenses, and current posture
- **Prior skill output**: ECA, settlement-negotiation, or litigation-risk-assessment output

If no matter summary is provided, prompt the user for minimum inputs:

1. Nature of claims and defenses (legal theories)
2. Key facts and timeline
3. Parties and their relationships
4. Procedural stage and current posture
5. Governing law and mediation forum
6. Any prior settlement discussions or demands

### Step 2: Gather Mediation Context

**⟁ CLARIFY** — Before beginning, ask these questions. Present as structured options.
Skip any question the user has already answered.

1. **Mediation objective**:
   - Options: Establish realistic settlement corridor, Prepare mediator brief and opening
     statement, Evaluate a received settlement offer, Plan contingency impasse scenarios,
     Full preparation (all of above)
   - _Why this matters_: Controls depth, output format, and analytical emphasis.

2. **Your side and role**:
   - Options: Claimant/Plaintiff, Defendant/Respondent, Co-claimant (aligned),
     Co-defendant (aligned), Multi-party with competing interests, In-house decision-maker,
     Neutral evaluation
   - _Why this matters_: The entire analysis — corridor anchoring, concession cadence,
     opening tone — depends on which side you represent.

3. **Procedural stage**:
   - Options: Pre-suit (dispute, no claim filed), Early litigation (complaint filed,
     pre-discovery), Active discovery (information-gathering underway), Late litigation
     (trial within 6 months), Post-trial / appeal, Mediation already underway
   - _Why this matters_: Discovery completeness directly affects BATNA/WATNA confidence.
     Early mediation carries information uncertainty that must be explicitly modeled.

4. **Mediator profile** (if mediator already selected):
   - Style: Evaluative (mediator provides assessment) / Facilitative (mediator facilitates
     dialogue) / Transformative (focuses on relationship) / Hybrid / Unknown
   - Experience: Extensive (100+ mediations in this area) / Moderate (20–99) / Limited
   - Credentials: Retired judge / Senior litigator / Industry expert / Generalist / Unknown
   - _Why this matters_: Evaluative mediators conduct reality tests that can shift
     positions; facilitative mediators depend on parties' own movement. Opening strategy
     and caucus posture differ significantly.

5. **Settlement authority and constraints**:
   - Options: Full settlement authority confirmed, Insurance carrier approval required,
     Board/committee approval threshold defined, Regulatory review implications, Multiple
     stakeholders with competing authority
   - _Why this matters_: Mediation can collapse if settlement authority is absent or
     conditional. Identifying constraints early prevents ratification failure.

6. **Multi-party dynamics** (if applicable):
   - Options: Single claimant / single defendant, Co-claimants (aligned interests),
     Co-claimants (competing interests), Allied defendants (aligned), Allied defendants
     (competing), Guarantor or indemnitor in the mix, Not applicable
   - _Why this matters_: Multi-party disputes require pre-mediation alignment meetings.
     Misaligned co-parties are a leading cause of mediation failure.

7. **Prior settlement analysis available?**:
   - Options: Yes — output from legalcode-settlement-negotiation available,
     Yes — internal settlement analysis available, No — build BATNA/WATNA from scratch,
     Partial — some elements only
   - _Why this matters_: If prior corridor analysis exists, Steps 5–6 can be populated
     directly rather than re-derived, saving significant analysis time.

8. **Non-monetary term priorities** (multi-select):
   - Options: Release scope (known vs. unknown claims), Confidentiality of settlement,
     Admission of fault / apology, Injunctive relief or behavioral commitments,
     Ongoing business relationship preservation, IP licensing or transfer,
     Structured payment schedule, None — monetary only
   - _Why this matters_: Non-monetary terms often unlock deadlocks when monetary
     corridors do not overlap. Identifying priorities early shapes the concession plan.

If the user provides partial context, proceed with reasonable defaults and **state
assumptions explicitly** before delivering analysis.

### Step 3: Load Prior Case Assessment

Check whether a prior legal analysis is available to inform the mediation preparation:

**From `legalcode-early-case-assessment` output** (preferred): Use the element-level merits
assessment, evidence quality matrix, and damages exposure range directly. Note the
assessment date and whether discovery has materially progressed since then.

**From `legalcode-litigation-risk-assessment` output**: Use the four-dimensional risk
matrix, three-branch cost-benefit analysis, and strategic recommendations.

**From `legalcode-settlement-negotiation` output**: Use the settlement corridor, BATNA,
WATNA, and concession strategy analysis directly and cross-reference for consistency.

**If no prior analysis is available:**

**⟁ CLARIFY** — Inform the user that no prior assessment was found, and ask:

- **Option A: Run a simplified merit assessment now** — Conduct a focused element-level
  analysis of the core claims and defenses before building the mediation package. More
  thorough but requires more input.
- **Option B: Proceed with information provided** — Build the mediation analysis on stated
  facts and positions, explicitly flagging where merit uncertainty affects the corridor.
- **Option C: Mediation brief only** — Skip corridor analysis and focus on drafting the
  mediation statement and opening strategy from the facts provided.

Document the basis and uncertainty level in the Glass Box audit trail.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the substantive governing law, the procedural forum, and the mediation institution
or ad hoc rules. Then gather relevant legal authority.

**Using legalcode-mcp (if connected):** Search for:

1. Mediation confidentiality statutes and case law in the applicable jurisdiction
2. Settlement agreement enforceability requirements
3. Court-ordered ADR obligations and consequences for non-participation
4. Fee-shifting rules applicable to settlement offers (Part 36, Rule 68, etc.)
5. Tax treatment of settlement proceeds in the applicable jurisdiction
6. Mediation-specific ethical rules for attorneys (competence, client communication)

Save results to `/tmp/legalcode-mediation-research.md`.

**If legalcode-mcp is not connected:** Proceed with general knowledge; mark all
jurisdiction-specific references [VERIFY]; note in the Glass Box.

### Step 5: BATNA / WATNA / MLATNA Analysis

Build the three-scenario alternatives framework. If a prior settlement analysis exists,
import those values and validate; otherwise build from the current matter context.

#### 5a. Your BATNA (Best Alternative to Negotiated Agreement)

Model the best realistic outcome if mediation fails and the dispute proceeds to trial,
arbitration, or continued litigation.

| Scenario Component                           | Assessment | Confidence |
| -------------------------------------------- | ---------- | ---------- |
| Probability of prevailing on liability       | [X%]       | [Level]    |
| Expected damages if successful               | $[X]–$[X]  | [Level]    |
| Litigation timeline to judgment              | [Months]   | [Level]    |
| Total projected litigation cost              | $[X]       | [Level]    |
| Risk-adjusted present value (RAPV)           | $[X]       | [Level]    |
| BATNA net value (RAPV minus litigation cost) | $[X]       | [Level]    |

**BATNA Classification:**

- **STRONG BATNA**: Net value exceeds any realistic settlement corridor. You have
  incentive to litigate if settlement falls below this floor.
- **ADEQUATE BATNA**: Net value within the settlement corridor. Settlement is rational
  if the process and relationship costs are material.
- **WEAK BATNA**: Net value below the settlement floor. Settlement at any reasonable
  amount is preferable to trial outcome uncertainty.

#### 5b. Your WATNA (Worst Alternative to Negotiated Agreement)

Model the worst realistic outcome if mediation fails.

| Scenario Component                  | Assessment | Confidence |
| ----------------------------------- | ---------- | ---------- |
| Probability of adverse judgment     | [X%]       | [Level]    |
| Adverse damages / award against you | $[X]       | [Level]    |
| Litigation cost to adverse judgment | $[X]       | [Level]    |
| Total worst-case exposure           | $[X]       | [Level]    |
| Risk-adjusted worst-case value      | $[X]       | [Level]    |

#### 5c. Your MLATNA (Most Likely Alternative to Negotiated Agreement)

The probability-weighted expected outcome — more realistic than either BATNA or WATNA.

```
MLATNA = P(win) × BATNA_gross + P(lose) × (-WATNA_exposure) - Litigation_cost
```

Perform sensitivity analysis on key assumptions:

| Assumption            | Base Case | Adverse Shift      | Favorable Shift    |
| --------------------- | --------- | ------------------ | ------------------ |
| Liability probability | [X%]      | -[Y]% → new MLATNA | +[Y]% → new MLATNA |
| Damages ceiling       | $[X]      | -[Y]% → $[Z]       | +[Y]% → $[Z]       |
| Litigation cost       | $[X]      | +[Y]% → $[Z]       | -[Y]% → $[Z]       |

#### 5d. Counterparty BATNA/WATNA Estimation

Estimate the opposing party's alternatives:

| Counterparty Factor             | Estimate                              | Confidence | Source            |
| ------------------------------- | ------------------------------------- | ---------- | ----------------- |
| Counterparty BATNA              | $[X]                                  | [Level]    | [Inference basis] |
| Counterparty WATNA              | $[X]                                  | [Level]    | [Inference basis] |
| Cash flow / financial capacity  | [Description]                         | [Level]    | [Inference basis] |
| Strategic litigation incentives | [Precedent / Reputation / Deterrence] | [Level]    | [Inference basis] |
| Insurance coverage position     | [Known / Unknown / Estimated]         | [Level]    | [Inference basis] |

**⟁ CLARIFY** — If counterparty BATNA is unknown or estimated: "I am proceeding with
an inferred counterparty BATNA of $[X] based on [basis]. If you have information that
would refine this estimate (financial filings, prior demands, counsel reputation), please
provide it — this is the single most sensitive variable in the corridor analysis."

### Step 6: Settlement Range and ZOPA Identification

#### 6a. Your Settlement Corridor

| Settlement Term                  | Value | Basis                                                             |
| -------------------------------- | ----- | ----------------------------------------------------------------- |
| **Floor (walk-away)**            | $[X]  | [MLATNA minus relationship/business cost of continued litigation] |
| **Target**                       | $[X]  | [Fair value accounting for litigation risk, cost, timing]         |
| **Ceiling (maximum acceptable)** | $[X]  | [WATNA discount — maximum you would pay to avoid worst case]      |

For claimants: Floor = minimum acceptable; Ceiling = maximum demand.
For defendants: Floor = minimum offer; Ceiling = maximum payment to avoid trial.

#### 6b. ZOPA Mapping

```
Defendant FLOOR ──────────────────────────── Defendant CEILING (= Defendant WATNA)
                                     │
           [ZONE OF POSSIBLE AGREEMENT]
                                     │
Claimant FLOOR (= Claimant WATNA)  ───────── Claimant CEILING
```

| ZOPA Analysis                            | Assessment                 | Confidence |
| ---------------------------------------- | -------------------------- | ---------- |
| Does a ZOPA appear to exist?             | [Yes / No / Narrow / Wide] | [Level]    |
| ZOPA width (if positive)                 | $[Low]–$[High]             | [Level]    |
| Primary mediation target within ZOPA     | $[X]                       | [Level]    |
| Probability of settlement if ZOPA exists | [X%]                       | [Level]    |

**If no ZOPA appears to exist:**

**⟁ CLARIFY** — "The current assessment suggests the parties' corridors do not overlap.
This does not mean settlement is impossible — it means the corridors are based on
different assumptions. Options:

- (A) Re-examine BATNA assumptions — are any key inputs (liability probability, damages
  ceiling, litigation cost) being modeled differently by each side?
- (B) Model non-monetary terms — is there creative deal structure (payment terms, mutual
  release, behavioral commitments, ongoing relationship) that could bridge the gap?
- (C) Identify timing events — are there upcoming developments (expert reports, motions,
  discovery completion) that would narrow positions?
- (D) Proceed with negative ZOPA analysis — document the gap and plan the opening strategy
  to enable corridor movement during mediation."

#### 6c. Risk-Adjusted Present Value (RAPV) Comparison

| Branch            | Expected Value | Timeline    | Legal Cost | RAPV    |
| ----------------- | -------------- | ----------- | ---------- | ------- |
| Settle at floor   | $[Floor]       | [Immediate] | $[Low]     | $[RAPV] |
| Settle at target  | $[Target]      | [Immediate] | $[Low]     | $[RAPV] |
| Litigate (MLATNA) | $[MLATNA]      | [Months]    | $[High]    | $[RAPV] |
| Litigate (BATNA)  | $[BATNA]       | [Months]    | $[High]    | $[RAPV] |
| Litigate (WATNA)  | $[WATNA]       | [Months]    | $[High]    | $[RAPV] |

Recommend settlement if: RAPV(Target) > RAPV(MLATNA) and risk tolerance is balanced or
conservative. Recommend persistence if: RAPV(BATNA) materially exceeds any settlement
offer and risk tolerance is aggressive.

### Step 7: Mediator Selection Criteria

Evaluate the mediator (or guide selection if not yet appointed) across five dimensions:

#### 7a. Mediator Style Assessment

| Style              | When to Choose                                                                                                 | Avoid If                                                           |
| ------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Evaluative**     | Numerical deadlock; parties need external reality check; high legal complexity                                 | Relationship repair is a priority; parties want to control outcome |
| **Facilitative**   | Relationship preservation matters; parties are willing to move without being told to; confidentiality critical | Parties are far apart and need neutral pressure to move            |
| **Transformative** | Ongoing relationship; emotional dimensions dominate; communication breakdown                                   | Pure commercial dispute with no relationship dimension             |
| **Hybrid**         | Complex commercial disputes with both legal and relationship dimensions                                        | Not applicable                                                     |

**Preferred style for this matter**: [Evaluative / Facilitative / Transformative / Hybrid]
**Rationale**: [Based on the ZOPA analysis, mediator style matters because...]

#### 7b. Mediator Qualification Checklist

- [ ] Subject-matter expertise: Experience in [dispute type, industry, legal area]
- [ ] Jurisdictional knowledge: Familiar with [governing law jurisdiction]
- [ ] Conflict check: No prior representation of either party or their affiliates
- [ ] Track record: Confirmed settlement rate in comparable disputes
- [ ] Availability: Can commit to mediation on [preferred date] with preparation time
- [ ] [JURISDICTION-SPECIFIC] Certification: Meets applicable mediator qualification standards
      (e.g., NMAS in AU, CEDR accreditation in UK, state court roster requirements in US) [VERIFY]
- [ ] Logistical: Location, virtual capacity, support (co-mediator if multi-party)

#### 7c. Mediator Bias Risk Assessment

| Risk Factor                                       | Present? | Impact | Mitigation                             |
| ------------------------------------------------- | -------- | ------ | -------------------------------------- |
| Prior representation of counterparty's law firm   | Yes/No   | HIGH   | Decline this mediator                  |
| Industry affiliation favoring counterparty        | Yes/No   | MEDIUM | Request explanation; monitor           |
| Institutional relationship with mediator provider | Yes/No   | LOW    | Note; monitor joint session tone       |
| Fee arrangement creating incentive to prolong     | Yes/No   | MEDIUM | Agree on capped hourly vs. fixed fee   |
| Prior public statements on similar legal issues   | Yes/No   | MEDIUM | Research and prepare counter-narrative |

**Overall bias risk**: [LOW / MEDIUM / HIGH — rationale]

### Step 8: Pre-Mediation Preparation Checklist

#### 8a. Evidence and Documents

- [ ] Liability evidence: Organized and summarized for mediator (not overwhelming volume)
- [ ] Damages documentation: Quantified with methodology (expert opinion if available)
- [ ] Key timeline: Chronology of events supporting your position
- [ ] Prior demands and offers: Complete negotiation history with dates and amounts
- [ ] Insurance information: Applicable policy limits, coverage position, carrier authority
- [ ] Expert opinions: Summary of retained experts' expected positions (if available)
- [ ] Settlement-blocking issues: Identify and plan to resolve before mediation

#### 8b. Authority Confirmation and Decision-Maker Logistics

Confirm at least 10 business days before mediation:

- [ ] **Settlement authority holder** identified and committed to attend in person
- [ ] **Authority amount** explicitly stated in internal authorization (not left to day-of)
- [ ] **Board/committee approval** obtained for authority at or above threshold
- [ ] **Insurance carrier representative** confirmed (if coverage applies)
- [ ] **Ratification risk assessed**: Does negotiator speak for entire organization, or
      must a board/committee ratify? Resolve this before mediation — post-mediation ratification
      failures destroy goodwill and often produce worse outcomes.
- [ ] **[JURISDICTION-SPECIFIC]** Written authority notice filed with court if required
      (e.g., Florida Rule 1.720 requires pre-mediation notice of attendees with authority) [VERIFY]
- [ ] **Virtual attendance confirmed** if any party or authority holder is remote
- [ ] **Backup authority holder** identified for emergency absence

**⟁ CLARIFY** — "Who is the settlement authority holder for this matter, and will they
be physically present? If board or committee approval is required, what is the highest
amount already authorized? Options:

- (A) Full settlement authority confirmed — I will proceed with that amount
- (B) Conditional authority (board approval required above $X) — I will note this as a
  constraint and flag ratification risk in the preparation
- (C) Authority not yet confirmed — I will include pre-mediation authority confirmation
  as a Tier 1 action item"

#### 8c. Client Preparation

- [ ] Explain mediation process: joint session, caucus structure, role of mediator
- [ ] Calibrate client expectations: Outcomes are uncertain; mediation is not court
- [ ] Set settlement authority: Client understands floor, target, ceiling and has approved
- [ ] Prepare client for emotional dynamics: Counterparty will present their version
- [ ] Review client's opening statement role (if client will speak in joint session)
- [ ] Practice difficult questions the mediator may ask in caucus
- [ ] Agree on communication protocol: Who speaks to mediator; when to consult with client

### Step 9: Mediation Statement Drafting

Produce two distinct mediation statements: the **opening statement** (shared with
counterparty and mediator) and the **confidential statement** (mediator only).

#### 9a. Opening (Shared) Mediation Statement

Structure and guidelines:

**Section 1 — Party Introduction and Dispute Overview** (1–2 paragraphs):

- Who you represent, who the counterparty is, and the nature of the dispute
- Frame in neutral, professional terms — not adversarial
- Summarize the amount at stake and the key legal issues

**Section 2 — Key Facts** (objective, organized chronologically):

- Present facts that support your position, but avoid exaggeration
- Acknowledge undisputed facts to establish credibility with the mediator
- Reference key documents without excessive detail (mediator will read selectively)

**Section 3 — Legal Position** (concise, not a brief):

- Identify governing law and the legal theories at issue
- State the strength of your position without dismissing counterparty entirely
- Note any dispositive legal questions that affect corridor width

**Section 4 — Damages/Exposure Summary**:

- Quantify your damages or exposure in ranges, not false precision
- Reference methodology (lost profits analysis, comparable transactions, etc.)
- Include prejudgment interest and fee-shifting if applicable [JURISDICTION-SPECIFIC]

**Section 5 — Impediments to Settlement and Proposed Path Forward**:

- What has prevented settlement so far
- What you believe would allow resolution
- Invitation to explore settlement (cooperative tone)

**Length guidance**: 10–15 pages; bullet-point style with headings is more effective than
dense prose. Avoid the tone of a trial brief — the audience is a neutral, not a judge.

#### 9b. Confidential (Mediator-Only) Statement

Include information not appropriate for the shared brief:

- **Your real settlement authority**: Floor, target, ceiling with explicit dollar amounts
- **Leverage assessment**: What pressures drive the other side toward settlement
- **Settlement priorities**: Which terms are CORE (non-negotiable), TARGET (preferred),
  and FLEXIBLE (tradeable)
- **Client emotional/psychological dynamics**: What the client needs besides money
  (apology, acknowledgment, ongoing relationship, confidentiality)
- **Multi-party coordination**: Internal alignment issues among co-parties
- **Walk-away triggers**: What would cause you to terminate mediation and return to
  litigation, and what event would trigger escalation of authority

**Confidentiality caution**: Assume the mediator may hint at your positions to the
counterparty (directly or indirectly). Do not write anything in the confidential brief
that would destroy your negotiating position if the other side learned of it.

### Step 10: Concession Strategy and Phase-by-Phase Tactics

#### 10a. Opening Position and Anchor

**Anchoring principle**: The first number anchors the negotiation. An opening demand or
offer outside the mediator's credibility range signals desperation or unreasonableness
and undermines your position. Calibrate the opening to:

- Materially beyond your target (for negotiating room) but not extreme
- Explainable with reference to damages evidence and litigation risk
- Mediator-credible (a mediator who thinks your opening is absurd will tell you so)

**Opening position calculation**:

| Opening Element              | Value | Basis                                                    |
| ---------------------------- | ----- | -------------------------------------------------------- |
| Claimed damages (unadjusted) | $[X]  | [Damages methodology]                                    |
| Opening demand / offer       | $[X]  | [Damages ± litigation risk premium ± negotiation buffer] |
| Distance from target         | $[X]  | [Must leave room to move credibly]                       |
| Expected counterparty anchor | $[X]  | [Based on counterparty BATNA estimate]                   |

#### 10b. Concession Cadence Design

Design concession timing and magnitude as a deliberate pattern, not an improvised
response:

| Round             | Trigger                                 | Your Move                | Magnitude                            | Rationale to Mediator                                                  |
| ----------------- | --------------------------------------- | ------------------------ | ------------------------------------ | ---------------------------------------------------------------------- |
| 1 (Opening)       | Initial exchange                        | [Opening position]       | N/A                                  | "Based on documented damages of $X and litigation costs to trial"      |
| 2 (Post-caucus 1) | Mediator brings counterparty's position | Move [$X], toward [$Y]   | [Large — 30-40% of gap]              | "We're moving in good faith; our floor reflects X risk"                |
| 3 (Post-caucus 2) | Mediator signals gap is narrowing       | Move [$X], toward [$Y]   | [Moderate — 20-25% of remaining gap] | "We're at our reasonable range; this reflects litigation cost savings" |
| 4 (Late stage)    | Mediator reports resistance             | Move [$X] conditionally  | [Small — 10% or specific term trade] | "We'll move on X if they resolve Y"                                    |
| Final             | Mediator proposes bridge                | Accept / counter at [$Y] | [Minimal if gap is bridgeable]       | "This is our best and final"                                           |

**Diminishing pattern**: Each concession should be smaller than the last. Constant
large concessions signal that you have much more room to move.

**Leverage event timing**: Identify events between now and mediation that would shift
bargaining power and time concession moves accordingly.

| Event           | Date   | Effect on Your Leverage       | Action                          |
| --------------- | ------ | ----------------------------- | ------------------------------- |
| [Motion ruling] | [Date] | [Favorable/Adverse]           | [Delay or accelerate mediation] |
| [Expert report] | [Date] | [Strengthens/weakens damages] | [Use in opening or withhold]    |
| [Trial date]    | [Date] | [Pressure on counterparty]    | [Reference timeline in caucus]  |

#### 10c. Non-Monetary Term Trading

**CORE terms** (non-negotiable — will not trade):

- [Identify items that must appear in any settlement]

**TARGET terms** (strongly preferred — will trade for monetary value):

- [Identify items you want but would exchange for better monetary terms]

**FLEXIBLE terms** (tradeable — low-cost concessions with potential high counterparty value):

- Confidentiality of settlement amount
- Non-disparagement clause
- Mutual release of known and unknown claims
- Structured payment schedule vs. lump sum
- Reference letter or neutral attestation
- Ongoing business relationship preservation terms

**Package deal engineering**: If monetary corridor does not overlap, explore packages that
combine monetary and non-monetary elements. Example: "We will accept $1.8M (below our
target of $2M) if you include a three-year non-disparagement agreement and release all
IP claims through 2028." The non-monetary terms may be worth more than the $200K gap.

#### 10d. Phase-by-Phase Execution

**Phase 1 — Opening Joint Session:**

- Purpose: Educate mediator, signal good faith to counterparty, establish credibility
- Tone: Professional, confident, non-antagonistic — avoid inflammatory opening statements
- Length: 10–20 minutes; yield time to mediator quickly
- Content: High-level facts, legal position, damages summary, desire to resolve
- Client role: Decide in advance whether client speaks. Client statement can humanize the
  dispute and signal settlement intent; but unprepared clients can derail the session.
- Do not: Deliver a trial brief orally; attack counterparty counsel; make demands

**Phase 2 — Caucus with Mediator (your side):**

- Purpose: Develop a candid relationship with the mediator as reality-tester
- Share: Your real authority, key priorities, what the counterparty needs to give you
- Do not share: Your exact walk-away floor or ceiling unless strategically useful
- Mediation intelligence: Mediators often reveal more about the other side's position
  than they intend. Listen carefully to what the mediator emphasizes.
- Reality testing: Welcome the mediator's critical assessment — if the mediator says
  your position is unrealistic, verify whether this is a genuine assessment or a tactic.
- Sign of movement: Mediators often frame counterparty movement as their own idea.
  "What if we could get them to $X?" usually means they already have a number in mind.

**Phase 3 — Counterparty Caucus (they meet with mediator):**

- Use this time productively: Review sensitivity analysis, consult with client, refine
  non-monetary term priorities, review impasse triggers
- Do not: Make concessions with the mediator before they return with counterparty movement

**Phase 4 — Negotiation Rounds:**

- Apply concession cadence from 10b
- Respond to mediator's bridge proposals with conditional language: "We could reach $X
  if [condition], but we need movement on [term]"
- Use package trades to break numerical deadlocks (10c)
- Monitor time pressure: Late-day settlements are more likely — plan key concessions for
  the afternoon session when fatigue and time pressure favor movement

**Phase 5 — Impasse Diagnosis and Management:**

- **Genuine impasse**: Corridors do not overlap; further concessions would exceed authority
  or BATNA. Recognize that not all disputes settle at first mediation.
- **Tactical impasse**: Counterparty is using impasse posture to extract a final concession.
  Probe: "If we could resolve [specific issue], would you be in position to settle today?"
- **Mediator adjudication**: For evaluative mediators, consider requesting a mediator's
  recommendation (non-binding). This gives both sides a face-saving path to acceptance.
- **Bracketing**: Propose confidential brackets to test whether corridors overlap without
  committing to a number. "Off-the-record — if the number were between $X and $Y, would
  there be room to talk?" Mediators frequently facilitate this.

**Phase 6 — Closing and Documentation:**

- If agreement reached: Execute a term sheet or memorandum of understanding before leaving
  the room. Oral agreements in mediation are vulnerable to disputes about terms.
- [JURISDICTION-SPECIFIC] Verify whether the signed MOU creates a binding contract or
  requires a formal agreement. In many US jurisdictions, a signed mediation settlement is
  immediately enforceable. In UK, Tomlin Orders consent is preferred for court matters.
  In AU, settlement terms should be incorporated into a Deed of Settlement. [VERIFY]
- If mediation concludes without agreement: Request mediator feedback on what each side
  needs to move. Schedule a follow-up if the gap is narrow.

### Step 11: Impasse Exit Protocol

If mediation fails or appears likely to fail, implement this exit protocol before
terminating:

**Pre-exit checklist:**

- [ ] Has mediator attempted bracketing to test whether corridors overlap?
- [ ] Have non-monetary terms been fully explored as value-gap bridges?
- [ ] Has mediator issued (or could issue) an evaluative opinion or mediator's proposal?
- [ ] Have you identified whether impasse is genuine or tactical?
- [ ] Is there a specific condition under which counterparty would settle
      (information, concession, or timing event)?

**Post-mediation options:**

- **Continued bilateral negotiation**: Mediation often unlocks movement that continues
  informally after the session ends. Keep the channel open.
- **Second mediation session**: If gap is narrow, a follow-up session may succeed.
- **Co-mediation**: Bring a second mediator with different expertise or style.
- **Neutral expert evaluation**: For technical disputes, a binding or non-binding neutral
  expert assessment may break the factual deadlock.
- **Mini-trial or early neutral evaluation**: Judicial officer or neutral panel gives
  non-binding assessment — often more persuasive than mediator's opinion.
- **Return to litigation**: If no path to settlement exists, proceed with trial preparation.
  Mediation failure often provides intelligence about counterparty's litigation readiness.

---

## Position Classification

### Your Mediation Position

| Classification | Definition                                                                                                                                     | Strategic Implication                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **STRONG**     | Clear legal merit, strong evidence, contained exposure, favorable BATNA. Your litigation alternative is attractive relative to counterparty's. | Open near (but above) your target. Move slowly and in decreasing increments. Do not feel pressure to settle at first mediation.                                                |
| **ADEQUATE**   | Mixed merits or factual gaps; moderate exposure; BATNA is viable but carries material uncertainty.                                             | Open with room to move. Calibrate concessions to mediator feedback. Evaluate non-monetary terms to close gap.                                                                  |
| **WEAK**       | Legal or factual gaps; high exposure; BATNA is poor relative to any reasonable settlement.                                                     | Open at a credible starting point but be prepared to move more significantly. Prioritize settling even at a discount to target. Non-monetary terms may be especially valuable. |

### Counterparty's Estimated Position

Apply the same classification (STRONG / ADEQUATE / WEAK) to the counterparty's position.
Then use the matrix to determine mediation feasibility:

| Your Position | Counterparty's Position | Mediation Feasibility                                                       | Recommended Approach                                                             |
| ------------- | ----------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| STRONG        | STRONG                  | CHALLENGING — both sides have viable alternatives                           | Mediator needs to find creative solutions; non-monetary terms critical           |
| STRONG        | ADEQUATE                | PROMISING — counterparty has reason to settle                               | Apply pressure; move slowly; let counterparty come to you                        |
| STRONG        | WEAK                    | VERY PROMISING — settle early to avoid risk of appeal or enforcement issues | Propose reasonable settlement; do not overreach                                  |
| ADEQUATE      | STRONG                  | CHALLENGING — you need the deal more than counterparty does                 | Open close to target; show movement quickly; use non-monetary leverage           |
| ADEQUATE      | ADEQUATE                | PROMISING — both sides have settlement incentives                           | Standard mediation dynamic; mediator-orchestrated cadence works well             |
| ADEQUATE      | WEAK                    | PROMISING — counterparty needs the deal                                     | Anchor high; move deliberately; insist on prompt full payment                    |
| WEAK          | STRONG                  | VERY CHALLENGING — you need settlement; they can litigate                   | Propose aggressive settlement; use non-monetary creative structures              |
| WEAK          | ADEQUATE                | CHALLENGING                                                                 | Open realistically; avoid antagonizing counterparty; focus on relationship value |
| WEAK          | WEAK                    | PROMISING — both sides benefit from settlement                              | Mutual interest in settlement; mediator can facilitate quickly                   |

---

## Prioritization Framework

### Tier 1 — Must Address Before Mediation

Issues that, if unresolved, will cause mediation to fail or create binding exposure:

- Settlement authority not confirmed at required level
- Multi-party alignment not achieved among co-parties
- Insurance carrier position unclear or adverse
- Ratification risk unresolved (negotiator cannot bind the organization)
- Key decision-maker unavailable for the scheduled date
- [JURISDICTION-SPECIFIC] Pre-mediation filing or notice obligations not met

### Tier 2 — Should Address Before Mediation (High Strategic Value)

Issues that materially affect mediation effectiveness:

- Mediator credibility assessment not completed (bias risk unchecked)
- BATNA/WATNA modeling incomplete or based on pre-discovery estimates
- Non-monetary term priorities not identified or authorized
- Confidential statement not prepared
- Client opening statement role not decided or rehearsed
- Impasse exit protocol not established

### Tier 3 — Enhances Preparation (Tactical Improvements)

Issues that improve effectiveness but are not prerequisites:

- Full sensitivity analysis on BATNA/WATNA assumptions
- Detailed concession cadence with mediator-specific tactical notes
- Non-monetary package deal options fully documented
- Leverage timeline with event-by-event concession guidance
- Post-mediation follow-up plan if session concludes without agreement

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise.

| Gate           | Rule                                                                                                                      | Fail Action                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Source**     | Every legal/process claim cites a specific statute, mediation rule, ADR framework, or settlement enforceability principle | Add citation or mark "[UNVERIFIED — counsel to confirm]"                   |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                               | Fix format                                                                 |
| **Currency**   | Every cited provision checked for amendments (e.g., 2024 CPR amendments to ADR obligations, FRCP 2020 amendments)         | Flag "[CHECK CURRENCY — may have been amended]"                            |
| **Domain**     | Analysis stays within mediation context; no litigation-only assumptions imported without justification                    | Remove or flag with "[JURISDICTION-SPECIFIC — verify under mediation law]" |
| **Confidence** | All BATNA/WATNA estimates, settlement corridors, and leverage assessments carry explicit confidence levels                | Add confidence qualifier; lower score if necessary                         |

### Self-Interrogation for High-Priority Items

For any Tier 1 issue or WEAK position classification, apply this 3-pass self-interrogation:

**Pass 1 — Settlement Corridor Validity:**

- Does the BATNA/WATNA assessment rest on realistic litigation outcomes, or does it
  assume a higher win probability than the evidence supports?
- Is the corridor actually acceptable to both sides, or have we set our floor assuming
  the counterparty's desperation?
- Have we modeled the counterparty's likely BATNA, not just guessed it?

**Pass 2 — Completeness of Leverage Assessment:**

- Have all non-financial levers been identified (time pressure, reputational harm,
  relationship preservation, CEO's risk tolerance)?
- Are there information asymmetries where we may be underestimating the counterparty's
  leverage (hidden assets, insurance, corporate backing)?
- Have we assessed whether the mediator's style or prior relationships favor either party?

**Pass 3 — Mediation Strategy Challenge:**

- What is the strongest argument that our opening position is too extreme or too modest?
- Would a reasonable mediator recommend settlement within our corridor, or tell us it is
  unrealistic?
- Is there a settlement structure (payment terms, non-monetary elements, phased resolution)
  that could break a numerical deadlock we have not yet explored?

Mark the audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                         | Action                                                |
| ------------ | --------- | --------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.00 | Settled law, clear statute, established principle               | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions                | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ                | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain — competing authorities or incomplete facts | Flag for counsel review with both sides presented     |
| **Unlikely** | 0.00–0.39 | Weak basis, speculative                                         | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

Apply confidence scoring to: liability probability, BATNA/WATNA values, corridor width,
counterparty BATNA estimate, mediator credibility assessment, and settlement probability.

---

## Glass Box Audit Trail

Every mediation preparation output MUST include this Glass Box section:

```yaml
glass_box:
  skill_name: "legalcode-mediation-preparation"
  matter: "[Case name / matter reference]"
  preparation_date: "[date]"
  mediation_objective: "[Establish corridor / Prepare brief / Evaluate offer / Full preparation]"

  # Party and stakeholder profile
  user_side: "[Claimant / Defendant / Multi-party]"
  opposing_party: "[Name and role]"
  governing_law: "[Jurisdiction for substantive law]"
  mediation_forum: "[Institution / Ad hoc / Court-annexed]"
  procedural_stage: "[Pre-suit / Early litigation / Discovery / Late-stage / Post-trial]"
  multi_party_issues: "YES / NO — [description if YES]"

  # BATNA/WATNA and corridor
  your_batna: "$[value] (confidence=[level])"
  your_watna: "$[value] (confidence=[level])"
  your_mlatna: "$[value] (confidence=[level])"
  counterparty_batna_estimated: "$[value] (confidence=[level])"
  settlement_corridor: "$[floor]–$[ceiling], target $[target] (confidence=[level])"
  zopa_status: "[Positive / Narrow / Negative / Unknown]"
  rapv_settlement_vs_litigation: "$[delta] in favor of [settlement/litigation]"

  # Mediator assessment
  mediator_identified: "YES / NO"
  mediator_style: "[Evaluative / Facilitative / Transformative / Hybrid / Unknown]"
  mediator_bias_risk: "[LOW / MEDIUM / HIGH — rationale]"
  mediator_experience_level: "[Extensive / Moderate / Limited / Unknown]"

  # Authority and logistics
  settlement_authority_confirmed: "YES / NO / CONDITIONAL"
  decision_maker_attendance: "CONFIRMED / PENDING / REMOTE"
  insurance_carrier_position: "[Known / Unknown / Adverse]"
  ratification_risk: "[NONE / LOW / MEDIUM / HIGH — explanation]"

  # Analysis basis
  prior_eca_available: "YES (dated [date]) / NO"
  prior_settlement_analysis_available: "YES (dated [date]) / NO"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-mediation-research.md or 'Not created']"
  citations_verified: "[N VERIFIED] / [N [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no Tier 1 issues)"

  # Confidence aggregation
  overall_confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limiting_factor: "[What constrains confidence — e.g., pre-discovery BATNA, unknown mediator, uncertain counterparty leverage]"

  # Deliverables produced
  deliverables:
    - "BATNA/WATNA/MLATNA analysis: YES / NO"
    - "ZOPA identification and corridor: YES / NO"
    - "Opening mediation statement: YES / NO"
    - "Confidential mediator statement: YES / NO"
    - "Concession strategy and cadence: YES / NO"
    - "Phase-by-phase tactics: YES / NO"
    - "Impasse exit protocol: YES / NO"

  # Limitations
  limitations:
    - "[Scope limitation, pre-discovery uncertainty, missing counterparty information, etc.]"
  reviewer: "AI-assisted — requires qualified legal counsel and mediator collaboration before use"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in mediation preparation:

1. **Beginning mediation without a defined settlement corridor** — Entering mediation
   without a documented floor, target, and ceiling means the client is improvising under
   time pressure. Authority vacuums create ratification failures. Establish the corridor
   before the session begins.

2. **Anchoring to "fair value" rather than expected value** — Fair value (objective market
   assessment) and settlement value (what an informed party would accept given BATNA) are
   different numbers. A party with a STRONG BATNA may rationally refuse fair value if
   litigation produces a better RAPV outcome. Anchor to expected value, not principle.

3. **Assuming BATNA is fixed** — BATNA shifts continuously as discovery progresses, motions
   are resolved, witnesses are deposed, and costs accumulate. A pre-discovery BATNA analysis
   may be wildly inaccurate by the time of late-stage mediation. Reassess at every milestone.

4. **Over-disclosing to the mediator** — A mediator is not your advocate. Information
   shared in caucus — including your real floor — can influence the mediator's "reality
   testing" of the other side. Disclose your authority and priorities strategically, not
   exhaustively. If the mediator asks for your walk-away threshold, answer with a range, not
   a precise number.

5. **Treating mediator feedback as objective fact** — "The other side is unmovable on this
   issue" is the mediator's perception (and sometimes a negotiating tactic). Cross-check
   mediator feedback against your own direct interactions and the counterparty's documented
   positions before over-conceding on a point the mediator labels as fixed.

6. **Selecting a mediator without conflict and bias checking** — A mediator with prior
   representation of counterparty's firm, institutional relationships with the industry
   defendant, or prior public statements adverse to your legal theory is not neutral in
   practice. Check mediator credentials rigorously before accepting appointment.

7. **Ignoring multi-party alignment as a pre-mediation requirement** — Co-claimants or
   co-defendants with competing interests will negotiate against each other in the mediator's
   presence, destroying leverage. Achieve internal alignment before the session begins, or
   mediation will fail regardless of how well you prepare.

8. **Presenting authority as conditional without resolving the condition** — "We can settle
   up to $X, but the board needs to approve anything above $Y" signals to the mediator and
   counterparty that the deal is not done even if you agree. Either obtain full authority
   before mediation or be transparent about approval timelines so they can be managed.

9. **Skipping the confidential statement** — A shared mediation brief without a confidential
   supplement leaves the mediator without the information they need to move the counterparty
   effectively. The mediator cannot help you if they do not know your real priorities,
   floor, and client psychology. Always provide a confidential brief.

10. **Using the opening statement as a trial brief** — An aggressive, precedent-citing,
    legal-theory-dense opening statement antagonizes the counterparty (who must sit and
    listen) and reduces mediator rapport. Mediation opening statements should be persuasive
    narratives, not appellate briefs. Save the legal analysis for caucus.

11. **Failing to prepare client for emotional dynamics** — Clients who have not experienced
    mediation are often shocked to hear the other side's narrative presented sympathetically.
    An unprepared client who emotionally reacts to counterparty's opening can derail
    mediation before the first caucus.

12. **Treating apology/acknowledgment as pure legal liability** — Some disputes resolve
    because one party needs acknowledgment of wrongdoing or an apology, not additional money.
    An assessment that treats any admission as dangerous for trial may miss the key settlement
    lever. A carefully worded "without admission of liability" acknowledgment may be the
    cheapest and most effective tool in the mediator's toolkit.

13. **Building settlement authority as binary (settle/walk)** — A two-point authority
    structure ("we can settle at $2M or we will try the case") gives the negotiator no room
    to respond dynamically to mediator feedback. Build a graduated authority structure with
    distinct amounts approved for different stages of movement.

14. **Missing the impasse exit protocol** — Entering mediation without a defined walk-away
    trigger means the client may be pressured into settlement below BATNA by session fatigue.
    Define in advance what constitutes a genuine impasse and what the next steps are if
    mediation ends without agreement.

15. **Treating structured settlement structures as exotic** — Payment terms, IP licensing,
    staged releases, ongoing relationship terms, and mutual non-disparagement clauses may
    bridge a monetary gap that no amount of numerical negotiation can close. These structures
    are routine mediation tools, not unusual accommodations. Build non-monetary terms into
    the preparation from the outset.

16. **Ignoring tax and accounting consequences** — A settlement that appears attractive as a
    gross number may be materially different net of taxes, accounting treatment, or
    regulatory disclosure requirements. Engage tax counsel before final authority is set.
    [JURISDICTION-SPECIFIC] Tax treatment of settlement proceeds varies significantly by
    jurisdiction, claim type, and settlement structure. [VERIFY]

17. **No documentation before leaving the room** — Oral settlements reached in mediation
    are vulnerable to disputes about specific terms. Execute a term sheet, memorandum of
    understanding, or agreed-upon term list before the session ends. A mediator who helps
    write the term sheet can accelerate this dramatically.

18. **Assuming counterparty's counsel drives settlement** — Opposing counsel's incentives
    (contingency fee structure, client relationship, litigation budget constraints) often
    differ from their client's interests. An opposing counsel on contingency may resist
    settlement below their minimum ROI even if the client wants to resolve. Model opposing
    counsel's incentives separately from the opposing party's BATNA.

19. **Skipping the post-mediation follow-up plan** — Mediation that ends in impasse
    frequently produces informal settlement within days or weeks. A party that has no follow-
    up plan after a failed session misses the window when counterparty movement is most
    likely. Define post-mediation engagement steps (mediator follow-up, continued bilateral
    negotiation, next session timing) before the first session concludes.

20. **Single-pass analysis without sensitivity testing** — Building a BATNA/WATNA model
    and corridor without testing it against adverse assumptions produces false confidence.
    Every key assumption — liability probability, damages ceiling, litigation cost, counterparty
    BATNA — should be sensitivity-tested before the analysis is delivered. One unfavorable
    discovery result or adverse ruling should not collapse the entire mediation preparation.

---

## Writing Standards

Apply plain-language discipline to all mediation preparation output:

**For the shared mediation statement** (read by mediator and counterparty):

- Neutral professional tone — not advocacy
- Bullet points and headings over prose blocks
- Active voice: "We seek recovery of $2.3M" not "Recovery of $2.3M is sought by claimant"
- Acknowledge undisputed facts; mediators recognize credibility when you concede minor points
- State damages in ranges with methodology — false precision reduces mediator credibility

**For the confidential mediator statement:**

- Candid and businesslike — mediators prefer directness to strategic hedging
- Include the real floor and ceiling with context; mediators need to understand your range
- Explain client psychology in plain terms: "Our client needs an apology more than another
  $50K — this is a potential settlement lever if the other side can provide it privately"
- Flag walk-away triggers and ratification constraints explicitly

**For internal analysis** (BATNA/WATNA, concession plan, Glass Box):

- Precise — include dollar ranges, confidence levels, probability weightings
- Conditional — state assumptions explicitly and flag sensitivity
- Actionable — every analysis section should lead to a decision or action item

**Quality gates before delivery:**

1. Does every authority claim cite a specific rule, statute, or case, or is it marked [VERIFY]?
2. Does every dollar figure carry a confidence level and basis statement?
3. Have all Tier 1 items been resolved or flagged as outstanding before mediation?
4. Has the Glass Box been completed with all key parameters?
5. Has the Self-Interrogation been run for any WEAK position or Tier 1 issue?
6. Are the shared and confidential statements clearly separated and appropriately labelled?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for mediation confidentiality statutes, court-ordered ADR obligations,
  settlement enforceability rules, and fee-shifting consequences for the applicable
  jurisdiction
- In Step 5, use verified legal authority to calibrate BATNA/WATNA (merits input)
- Save results to `/tmp/legalcode-mediation-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus on structural quality, corridor modeling, and process preparation rather than
  detailed legal authority analysis
- Recommend that counsel verify all jurisdiction-specific mediation rules before use

---

## Output Format Template

Deliver the mediation preparation package in five structured parts:

---

```markdown
# Mediation Preparation Package — [Matter Name]

**Prepared for**: [Side and Organization]
**Mediation Date**: [Date or TBD]
**Mediator**: [Name, Style, Institution, or "TBD"]
**Governing Law**: [Jurisdiction]
**Preparation Date**: [Date]

---

## PART 1: EXECUTIVE MEDIATION SNAPSHOT

| Parameter                                      | Assessment                               | Confidence |
| ---------------------------------------------- | ---------------------------------------- | ---------- |
| Your BATNA (net)                               | $[X]                                     | [Level]    |
| Your WATNA (net)                               | $[X]                                     | [Level]    |
| Your MLATNA                                    | $[X]                                     | [Level]    |
| Estimated Counterparty BATNA                   | $[X]                                     | [Level]    |
| Settlement Corridor (floor / target / ceiling) | $[X] / $[X] / $[X]                       | [Level]    |
| ZOPA Status                                    | [Positive / Narrow / Negative / Unknown] | [Level]    |
| RAPV: Settlement vs. Litigation                | $[X] in favor of [settlement/litigation] | [Level]    |
| Your Position Strength                         | [STRONG / ADEQUATE / WEAK]               | [Level]    |
| Counterparty Position Strength (est.)          | [STRONG / ADEQUATE / WEAK]               | [Level]    |
| Mediation Feasibility                          | [PROMISING / CHALLENGING / UNLIKELY]     | [Level]    |
| Overall Preparation Confidence                 | [HIGH / MEDIUM / LOW]                    | —          |

---

## PART 2: BATNA / WATNA / MLATNA ANALYSIS

### 2a. Your Alternatives (if mediation fails)

[Complete BATNA/WATNA/MLATNA tables from Step 5]

### 2b. Counterparty Alternatives (estimated)

[Counterparty estimation table from Step 5d]

### 2c. ZOPA Mapping

[ZOPA diagram and table from Step 6b]

### 2d. Risk-Adjusted Present Value Comparison

[RAPV table from Step 6c]

### 2e. Sensitivity Analysis

[Key assumption sensitivities — what changes if X goes wrong]

---

## PART 3: MEDIATION STATEMENTS

### 3a. Opening (Shared) Mediation Statement

[Full mediation statement per 9a structure — appropriate for submission to mediator
and sharing with counterparty]

### 3b. Confidential Supplement (Mediator Only)

[Settlement authority, real priorities, client psychology, walk-away triggers —
NOT for sharing with counterparty]

---

## PART 4: CONCESSION STRATEGY AND EXECUTION PLAN

### 4a. Opening Position and Anchor

[Opening position calculation from Step 10a]

### 4b. Concession Cadence

[Concession round table from Step 10b]

### 4c. Non-Monetary Term Priorities

[CORE / TARGET / FLEXIBLE term analysis from Step 10c]

### 4d. Phase-by-Phase Execution Tactics

[Opening, caucus, negotiation round, and impasse tactics from Step 10d]

### 4e. Leverage Timeline

[Leverage event timing table from Step 10b]

---

## PART 5: PRE-MEDIATION CHECKLIST AND AUTHORITY CONFIRMATION

### 5a. Tier 1 — Must-Complete Before Mediation

| Item                                | Status          | Owner   | Due    |
| ----------------------------------- | --------------- | ------- | ------ |
| Settlement authority confirmed      | ✅ / ⚠️ PENDING | [Owner] | [Date] |
| Multi-party alignment achieved      | ✅ / ⚠️ PENDING | [Owner] | [Date] |
| Insurance carrier position resolved | ✅ / ⚠️ PENDING | [Owner] | [Date] |
| Decision-maker attendance confirmed | ✅ / ⚠️ PENDING | [Owner] | [Date] |
| Mediator conflict check completed   | ✅ / ⚠️ PENDING | [Owner] | [Date] |

### 5b. Tier 2 — Should-Complete Before Mediation

[Remaining preparation items]

### 5c. Impasse Exit Protocol

| Trigger                                                       | Action                                                    |
| ------------------------------------------------------------- | --------------------------------------------------------- |
| Counterparty does not move below $[X] after [N] caucus rounds | Request mediator's proposal; if rejected, declare impasse |
| Time runs past [time] without agreement                       | Propose continued session or schedule follow-up           |
| Counterparty refuses to address [specific term]               | Terminate and resume litigation preparation               |

---

## QUALITY AND AUDIT TRAIL

[Glass Box YAML block — see template above]
```

---

## Localization Notes

**United States:**

- Mediation statements filed with court-annexed programs may lose privilege protection
  under some state statutes. Verify with local ADR program rules before filing.
- FRE Rule 408 protects offers to settle from admissibility, but the precise scope varies
  by circuit. Statements made in mediation may or may not be protected depending on state
  mediation privilege law. [VERIFY]
- California's mediation confidentiality statute (Evidence Code §§1115–1128) is among the
  broadest, protecting virtually all mediation communications. [VERIFY]

**United Kingdom:**

- The October 2024 CPR amendments create active judicial encouragement of ADR with cost
  consequences for unreasonable refusal. Model these cost consequences into the RAPV. [VERIFY]
- CPR Part 36 offers carry specific cost consequences if counterparty rejects and fails to
  beat the offer at trial. Coordinate mediation strategy with any outstanding Part 36 offer.
  [VERIFY]
- Tomlin Orders are the standard mechanism for incorporating mediated settlement terms into
  court proceedings (with confidential schedule). [VERIFY]

**Australia:**

- Federal Court's powers under s.53A extend to compulsory mediation referrals with
  statutory sanctions for non-compliance. [VERIFY]
- NMAS accreditation standards govern mediator qualification for court-connected processes.
  Confirm mediator NMAS registration for court-annexed mediations. [VERIFY]
- State-based civil liability legislation in some Australian states may restrict recovery
  of certain damages types (e.g., non-economic loss caps). Incorporate these statutory
  limits into the WATNA modeling. [JURISDICTION-SPECIFIC] [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis developed for the Legalcode
litigation skill collection. Legal framework informed by primary research on
BATNA/WATNA/MLATNA methodology (Harvard Negotiation Project), mediation statement
structure (ABA Litigation Section, JAMS, AAA mediation guides), mediator selection
criteria (CEDR, ACICA, FINRA ADR), and phase-by-phase tactics (Miles Mediation, ADR
Times). Structural architecture adapts patterns from `legalcode-settlement-negotiation`
(BATNA/WATNA corridor methodology), `legalcode-deposition-preparation` (credibility
assessment framework adapted for mediator assessment), and `legalcode-litigation-risk-
assessment` (prioritization tiers, Glass Box design, quality assurance framework). UK
jurisdictional markers reflect the October 2024 CPR amendments and _Churchill v Merthyr
Tydfil_ [2023] EWCA Civ 1416. Australian markers reflect Federal Court Act s.53A and
NMAS accreditation standards. All statutory references marked [VERIFY] where not
confirmed against authoritative sources.
