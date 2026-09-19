---
name: legalcode-strategic-equilibrium-analysis
description: 'Analyze multi-party legal and business strategy problems using a game-theory workflow: identify
  visible and hidden players, map incentives and constraints, enumerate strategy space, eliminate dominated
  moves, build a simplified payoff matrix, identify likely Nash equilibria, and recommend concrete move
  sequences with counter-strategy defenses. Use when assessing disputes, litigation posture, settlement
  leverage, regulatory standoffs, board conflicts, internal investigations, commercial negotiations, founder
  disputes, partnership breakdowns, enforcement risk, or any high-stakes legal matter where multiple actors
  are making interdependent decisions. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for
  legal constraints, procedure, and regulatory power.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Strategic Equilibrium Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted strategic analysis of
> legal and quasi-legal situations. It does not constitute legal advice, litigation
> strategy advice, regulatory advice, or investment advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use.
> Strategic recommendations depend heavily on facts, timing, authority, and opponent
> behavior. Laws, procedural rules, and market conditions change; verify current
> applicability before relying on any conclusion. Any legal or factual proposition not
> independently verified should be marked `[VERIFY]`.

## Purpose and Scope

Use this skill when the core problem is **strategic interdependence**: the user's best move
depends on what other actors are likely to do, and those actors are themselves reacting to
the user's choices.

This skill does:

- Map every relevant player, including hidden players and indirect beneficiaries
- Identify incentives, constraints, blind spots, and information asymmetries
- Enumerate strategy space, including unconventional game-changing moves
- Eliminate dominated strategies
- Build a simplified payoff matrix and identify cooperative, zero-sum, and trap outcomes
- Find likely Nash equilibria and explain what they mean in plain language
- Recommend immediate, signaling, contingency, and game-changing moves
- Predict likely opponent responses and provide counter-strategies
- Produce an auditable, confidence-scored strategic decision pack

This skill does not:

- Replace jurisdiction-specific legal advice from licensed counsel
- Guarantee that opponents behave rationally or consistently
- Produce false mathematical precision where the evidence does not support it
- Substitute for deep merits analysis when the matter first needs legal element mapping
- Cover criminal-defense strategy, intelligence operations, or coercive conduct outside
  lawful professional boundaries

**Typical use cases:**

- Litigation and pre-litigation posture decisions
- Settlement leverage and mediation preparation
- Regulatory or enforcement response planning
- Board, founder, shareholder, or JV control conflicts
- Internal investigations with parallel stakeholder pressure
- Commercial negotiations where counterparties, insurers, lenders, or regulators matter
- Crisis decisions where the user needs to understand second-order effects

**Related skills:**

- `legalcode-early-case-assessment` for element-level merits and evidence review
- `legalcode-litigation-risk-assessment` for four-dimensional litigation risk scoring
- `legalcode-settlement-negotiation` for corridor modeling and concession design
- `legalcode-legal-risk-assessment` for portfolio-style legal exposure mapping
- `legalcode-internal-investigation` for fact-development and privilege structure

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Strategy logic travels across
jurisdictions, but legal constraints do not. Identify the governing law, procedural forum,
regulatory regime, and decision-maker power early, then localize all move recommendations.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Available causes of action, defenses, and remedies
- Procedural leverage points and timing rules
- Injunction, preservation, privilege, and sanctions exposure
- Settlement, mediation, offer, and cost-shifting mechanics
- Regulator powers, reporting obligations, and enforcement triggers
- Director, fiduciary, employment, competition, or securities constraints
- Publicity/confidentiality rules and disclosure duties

Strategic analysis is only as good as the constraints map. A move that looks optimal in
the abstract may be illegal, sanctionable, value-destructive, or infeasible in the actual
forum.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Do not silently
assume facts that materially change the equilibrium.

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

Clarify when:

- The user's role or side is unclear
- The time horizon or decision deadline changes the best move
- Hidden players may materially alter the game
- Legal or regulatory constraints are uncertain
- The user's objective is ambiguous (win outright, settle, preserve relationship, delay,
  avoid precedent, control narrative, minimize downside)

---

## Workflow

### Step 1: Accept the Situation

Start with this exact opening question when context is missing:

> **Describe the competitive situation, negotiation, or strategic decision you need to analyze. Who are the players and what's at stake?**

Accept inputs in any of these forms:

- Matter summary or free-text narrative
- Pleadings, contracts, regulator letters, board materials, emails, or investigation notes
- Existing litigation or negotiation analysis to be stress-tested
- A discrete strategic question: "Should we file, settle, wait, threaten, concede, escalate, or redesign the deal?"

If the user provides only a vague problem statement, request the minimum inputs needed to
identify players, stakes, and constraints.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask these questions before analysis if they are not already answered:

1. **Whose side are we analyzing from?**
   - Options: Claimant / Plaintiff, Defendant / Respondent, Negotiating buyer, Negotiating
     seller, Internal decision-maker, Neutral evaluator, Mixed / multi-client
   - _Why this matters_: Strategy quality collapses if perspective is wrong.

2. **Primary objective?**
   - Options: Maximize win probability, Improve settlement position, Delay and preserve
     optionality, Reach business resolution, Minimize downside, Protect precedent or
     reputation, Prepare for board / regulator / insurer conversation
   - _Why this matters_: The same equilibrium can be good for one objective and bad for another.

3. **Decision horizon?**
   - Options: Immediate (24-72h), Near-term (1-2 weeks), Medium-term (this quarter),
     Strategic (longer than 90 days)
   - _Why this matters_: Some moves are optimal only because of timing pressure.

4. **Risk appetite?**
   - Options: Conservative, Balanced, Aggressive
   - _Why this matters_: Changes whether to trade certainty for upside.

5. **Relationship objective?**
   - Options: Preserve relationship, Relationship expendable, Unknown
   - _Why this matters_: Determines whether cooperative equilibria should be prioritized.

6. **Hard constraints?**
   - Free text or checklist: budget cap, board approval, regulator sensitivity, privilege
     concerns, litigation hold, funding limits, PR risk, insurance consent, contractual
     standstill, employee morale, election cycle, financing window
   - _Why this matters_: Constraints are often what make a theoretical strategy impossible.

If the user gives only partial context, proceed with explicit assumptions:

- "I am assuming you are analyzing this from the defendant side."
- "I am assuming relationship preservation is secondary."
- "I am assuming no immediate injunction deadline unless you tell me otherwise."

### Step 3: Establish the Governing Frame

Before modeling incentives, identify the legal and practical frame of the game.

Build a **frame sheet** covering:

- Governing law and forum
- Current stage (pre-dispute, pre-filing, filed case, post-discovery, deal negotiation, board conflict, regulatory inquiry)
- Decision deadline or triggering event
- Known hard constraints
- Missing information that could change the game materially

Use **legalcode-mcp** if connected to verify:

- Applicable legal constraints on proposed moves
- Regulator powers and deadlines
- Cost-shifting, injunction, privilege, or disclosure rules
- Any statutory or case-law issues that reshape leverage

If legalcode-mcp is not connected:

- Mark legal propositions `[VERIFY]`
- Continue with structural strategy analysis
- Flag legal-dependent moves for counsel confirmation before use

### Step 4: Phase 1 — Player Identification and Incentive Mapping

Identify **every player** in the game, not just the obvious named parties.

Always check for:

- Formal counterparties
- Decision-makers behind the named party
- Regulators
- Courts, arbitrators, or adjudicators
- Insurers
- Lenders or investors
- Board members or special committees
- Employees, unions, whistleblowers, or works councils
- Key customers or suppliers
- Co-defendants, indemnitors, auditors, experts, or media
- Political or public-interest actors if reputational pressure matters

For each player, map:

- **Primary incentive**
- **Secondary incentive**
- **Worst-case scenario they are trying to avoid**
- **Information advantage**
- **Blind spot / likely misread**
- **Leverage source**
- **Constraint**

Use this table:

| Player   | Role   | Primary Incentive | Secondary Incentive | Avoiding What? | Information Edge | Blind Spot | Leverage | Constraint |
| -------- | ------ | ----------------- | ------------------- | -------------- | ---------------- | ---------- | -------- | ---------- |
| [Player] | [Role] | [...]             | [...]               | [...]          | [...]            | [...]      | [...]    | [...]      |

**Hidden-player test**: If removing a player would change the user's optimal move, that
player belongs in the analysis even if they are not at the table yet.

### Step 5: Phase 2 — Strategy Space

List **all plausible actions** available to each material player.

For each player, include:

- The obvious move
- The "do nothing / wait" move
- The bluff or signaling move
- The escalation move
- The de-escalation or cooperative move
- The procedural move
- The information-forcing move
- The coalition-building move
- The game-changing move

For the user's side, always consider whether the game can be changed by:

- Bringing in a new decision-maker
- Splitting issues instead of bundling them
- Creating a deadline or removing one
- Changing forum
- Changing remedy sought
- Changing narrative or evidence order
- Creating or removing optionality
- Turning a bilateral conflict into a multi-party coalition
- Turning a multi-party conflict into a bilateral negotiation

Use this table:

| Player   | Strategy | Type                                                             | Preconditions | Expected Signal | Upside | Downside | Dominated? |
| -------- | -------- | ---------------------------------------------------------------- | ------------- | --------------- | ------ | -------- | ---------- |
| [Player] | [Move]   | Standard / Cooperative / Escalatory / Procedural / Game-changing | [...]         | [...]           | [...]  | [...]    | Yes / No   |

**Dominated-strategy rule**:

- Mark a strategy as dominated only if it is worse than another available move across every
  realistic opponent response.
- Do not eliminate a move merely because it is risky.
- Keep "do nothing" unless it is truly inferior on timing, information, and leverage.

### Step 6: Phase 3 — Payoff Matrix

Build a simplified payoff matrix for the **2-4 most realistic strategy collisions**. Do
not generate a fake full matrix if the game is too complex. Simplify the state space first.

Use the rating scale:

- `+2` strong positive outcome
- `+1` modest positive outcome
- `0` neutral / mixed
- `-1` modest negative outcome
- `-2` severe negative outcome

For each collision, identify whether the result is:

- `COOPERATIVE` — both sides improve
- `ZERO-SUM` — one side improves at the other's expense
- `TRAP` — both sides get worse outcomes than an available alternative
- `ASYMMETRIC` — one side bears most downside while the other remains protected

Recommended table:

| User Strategy | Opponent Strategy | User Payoff | Opponent Payoff | Other Player Effects      | Outcome Type | Why This Happens |
| ------------- | ----------------- | ----------: | --------------: | ------------------------- | ------------ | ---------------- |
| [Move A]      | [Move B]          |          +1 |              -1 | Regulator: 0; Insurer: +1 | ZERO-SUM     | [...]            |

If the game has more than two material players:

- Build a primary matrix for the main conflict pair
- Add an `Other Player Effects` column instead of pretending the rest do not matter
- Note where a third player's response changes the ranking of outcomes

### Step 7: Phase 4 — Nash Equilibrium Analysis

Identify the most plausible equilibrium or equilibria.

Use the following tests:

1. **Best-response test**

- For each player, ask whether changing strategy alone would improve their payoff.
- If no player can improve by unilateral deviation, the outcome is a Nash equilibrium.

2. **Credibility test**

- Is the strategy actually executable given legal, reputational, budget, or governance constraints?

3. **Stability test**

- Would small information changes break the equilibrium?

4. **Preference test**

- Is the equilibrium favorable, merely tolerable, or a trap for the user?

Classify the result:

| Classification | Meaning                                                              | Typical Implication                                |
| -------------- | -------------------------------------------------------------------- | -------------------------------------------------- |
| `FAVORABLE`    | Stable equilibrium materially advances the user's objective          | Preserve or reinforce it                           |
| `WORKABLE`     | Stable enough, but gains are limited or shared                       | Proceed with caution and protect edges             |
| `CONTESTED`    | Equilibrium depends on fragile assumptions, signaling, or sequencing | Tight monitoring and contingency planning required |
| `TRAP`         | Likely equilibrium is structurally bad for the user or for everyone  | Change the game rather than play it straight       |
| `UNSTABLE`     | No robust equilibrium yet; sequencing determines outcome             | Move first only with a clear leverage plan         |

Explain in plain language:

- What the likely equilibrium is
- Why players are likely to settle there
- Why it is or is not good for the user
- What would shift the equilibrium

If multiple equilibria exist, rank them by:

- Plausibility
- Speed of arrival
- Required assumptions
- Dependency on hidden players

### Step 8: Phase 5 — Optimal Move Sequence

Turn the analysis into a concrete move sequence.

Always provide these four moves:

1. **Immediate move**

- What to do today or in the next 24-72 hours
- Must be specific, executable, and time-bound

2. **Signaling move**

- What to reveal, conceal, emphasize, or delay
- Must state the behavioral effect sought from the opponent

3. **Contingency move**

- What to do if the opponent deviates from the expected path
- Must identify the trigger and the response

4. **Game-changing move**

- How to permanently change incentives, players, forum, or stakes
- Examples: add insurer, escalate to board, bifurcate issues, seek standstill, narrow ask,
  change forum, invoke covenant, add evidence, split settlement from precedent issue

Use this table:

| Move Type | Instruction            | Timing | Intended Effect | Preconditions | Legal / Practical Check |
| --------- | ---------------------- | ------ | --------------- | ------------- | ----------------------- |
| Immediate | [Specific instruction] | 24h    | [...]           | [...]         | VERIFIED / [VERIFY]     |

The move sequence must be action-oriented, not motivational.

### Step 9: Phase 6 — Counter-Strategy Defense

Predict the **two most likely opponent responses** to the recommended move sequence.

For each likely response, provide:

- Why the opponent would choose it
- What signal would show it is coming
- The user's immediate counter
- The move that would trap the user if mishandled
- The avoidance rule

Use this table:

| Likely Opponent Response | Why They Choose It | Early Warning Signal | Immediate Counter | Trap to Avoid | Avoidance Rule |
| ------------------------ | ------------------ | -------------------- | ----------------- | ------------- | -------------- |
| [Response]               | [...]              | [...]                | [...]             | [...]         | [...]          |

### Step 10: Quality-Assure and Deliver

Before delivery, check:

- Hidden players included?
- Dominated strategies actually eliminated?
- Payoff scores justified, not guessed?
- Equilibrium labeled correctly?
- Moves are lawful, feasible, and sequenced?
- Counter-strategy section addresses realistic responses rather than straw men?
- Unverified legal propositions marked `[VERIFY]`?

Deliver the final report using the output template below.

---

## Deep Strategic Analysis Framework

Use this framework silently while working.

### A. Player Audit

Assess whether each player is:

- Rational and incentive-driven
- Political and face-saving
- Constrained by internal governance
- Constrained by law or procedure
- Prone to overreaction
- Under-informed
- Looking for exit, precedent, or delay

### B. Incentive Distortion Checks

Look for distortions that change behavior:

- Insurance coverage or indemnity backstops
- Bonus, fundraise, election, or reporting deadlines
- Personal liability vs. entity liability separation
- Agency problems between decision-maker and principal
- Reputational asymmetry
- Information leakage risk
- Cost asymmetry
- Sunk-cost escalation

### C. Strategy-Space Completeness Checks

Never stop at the first obvious moves. Check for:

- File / threaten / settle / wait
- Seek interim relief
- Ask for standstill
- Divide monetary and non-monetary terms
- Change venue or decision-maker
- Add factual development before making a demand
- Use outside validator or mediator
- Bundle issues or deliberately unbundle them
- Shift from public to private channel or vice versa

### D. Payoff Discipline

Do not assign numbers casually. Anchor each payoff to:

- Economic effect
- Legal effect
- Timing effect
- Relationship effect
- Reputational effect
- Optionality effect

If the evidence is too thin for scoring, say so and reduce confidence rather than inventing certainty.

---

## Strategic Status Classification

Classify each material strategic finding using this system:

| Status       | Meaning                                                               | Typical Action               |
| ------------ | --------------------------------------------------------------------- | ---------------------------- |
| `ADVANTAGE`  | User holds credible leverage or can create it cheaply                 | Press or preserve            |
| `NEUTRAL`    | No clear side advantage; result depends on execution quality          | Tighten facts and sequencing |
| `VULNERABLE` | Opponent or hidden player can punish current posture                  | Mitigate before escalating   |
| `TRAP`       | Current path predictably worsens user outcome or destroys optionality | Stop and redesign the game   |

Use `TRAP` sparingly. Reserve it for situations where the current game structure itself is
the problem.

## Actionable Output Per Finding

For each `VULNERABLE` or `TRAP` finding, provide:

- One-sentence finding
- Why it matters
- Which player benefits from the current structure
- Recommended move
- Timing
- Evidence / authority status (`VERIFIED` or `[VERIFY]`)
- Confidence score

## Prioritization Framework

Use these tiers:

| Tier     | Label                     | Criteria                                                                                                              | Timing     |
| -------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------- |
| `Tier 1` | Immediate leverage / risk | Irreversible deadline, privilege risk, injunction exposure, board escalation, regulator touchpoint, narrative lock-in | 0-72 hours |
| `Tier 2` | Near-term positioning     | Facts, coalition building, controlled signaling, targeted concession, settlement corridor shaping                     | 3-14 days  |
| `Tier 3` | Structural redesign       | Forum shifts, governance changes, financing changes, relationship redesign, precedent strategy                        | 2+ weeks   |

## Citation Quality Gates

Run these five gates before delivery:

| Gate       | Rule                                                                             | Fail Action                      |
| ---------- | -------------------------------------------------------------------------------- | -------------------------------- |
| Source     | Every legal or factual claim tied to a document, authority, or stated assumption | Add source or mark `[VERIFY]`    |
| Format     | Legal citations and source attributions use recognizable format                  | Normalize citation / attribution |
| Currency   | Deadlines, rules, and authority checked for current applicability                | Add `[CHECK CURRENCY]`           |
| Domain     | Do not confuse legal entitlement, practical leverage, and reputational pressure  | Separate the analysis and revise |
| Confidence | Degree of certainty matches evidentiary support                                  | Lower confidence and qualify     |

## Self-Interrogation

Apply this three-pass review for `TRAP` findings and major move recommendations:

1. **Incentive Integrity**

- Does the move actually change incentives, or only express a preference?

2. **Constraint Completeness**

- What legal, procedural, governance, insurance, funding, or reputational constraint was left out?

3. **Reverse-Game Challenge**

- If the opponent knows this recommendation, what is their best counter and does the plan still hold?

If the move fails any pass, revise it or downgrade confidence.

## Confidence Scoring

| Level      | Range     | Meaning                                                    | Action                            |
| ---------- | --------- | ---------------------------------------------------------- | --------------------------------- |
| `Definite` | 0.95-1.00 | Incentives and constraints strongly support the conclusion | Present as primary path           |
| `High`     | 0.80-0.94 | Strong support, limited uncertainty                        | Present with a short caveat       |
| `Probable` | 0.60-0.79 | Best current read, but material uncertainty remains        | Present competing risks           |
| `Possible` | 0.40-0.59 | Outcome depends on missing facts or fragile assumptions    | Flag for validation before action |
| `Unlikely` | 0.00-0.39 | Weak support or too much uncertainty                       | Do not rely without new facts     |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-strategic-equilibrium-analysis"
  topic: "multi-party strategic equilibrium analysis"
  jurisdiction: "[jurisdiction / forum / regulator]"
  legalcode_mcp: "Connected / Not connected"
  source_materials:
    - "[contracts / pleadings / emails / board materials / narrative]"
  strategy_frame: "[litigation / negotiation / regulatory / governance / mixed]"
  user_side: "[plaintiff / defendant / buyer / seller / internal / neutral]"
  primary_objective: "[objective]"
  players_identified: "[count]"
  hidden_players_flagged: "[count]"
  dominant_strategies_found: "[count]"
  dominated_strategies_eliminated: "[count]"
  equilibrium_classification: "[FAVORABLE / WORKABLE / CONTESTED / TRAP / UNSTABLE]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  confidence: "HIGH / MEDIUM / LOW"
  key_assumptions:
    - "[assumption 1]"
    - "[assumption 2]"
  game_change_levers:
    - "[lever 1]"
    - "[lever 2]"
  limitations:
    - "[missing facts / unverified law / timing uncertainty]"
  reviewer: "AI-assisted; human legal review required"
```

## Anti-Patterns

Avoid these failure modes:

1. Treating the named parties as the only players.
2. Ignoring regulators, insurers, boards, lenders, or employees who can change payoffs.
3. Confusing legal merit with strategic leverage.
4. Recommending escalation without checking whether the threat is credible.
5. Forgetting the "do nothing" strategy.
6. Calling a move dominated when it is merely uncomfortable.
7. Building a payoff matrix that is too large to reason about honestly.
8. Using made-up numerical precision to disguise uncertainty.
9. Recommending a move that destroys optionality without acknowledging it.
10. Ignoring time asymmetry and deadline pressure.
11. Modeling the opponent as rational when the real driver is politics, ego, or agency cost.
12. Missing internal governance constraints such as board approval, insurer consent, or investor veto.
13. Treating a cooperative outcome as weakness when it is actually Pareto-superior.
14. Failing to identify prisoner's-dilemma traps.
15. Giving a move sequence without a signaling theory behind it.
16. Predicting only implausible opponent responses and calling that risk analysis.
17. Forgetting that disclosure, privilege, or publicity can change the game.
18. Delivering a recommendation without stating the assumption that most threatens it.

## Writing Standards

Follow these writing rules:

- Write like a calm strategist, not an advocate performing confidence.
- Prefer short, declarative sentences over rhetoric.
- Distinguish clearly between facts, inferences, and assumptions.
- Use plain language to explain equilibrium logic.
- Give instructions, not slogans.
- Avoid moralizing, chest-thumping, or motivational framing.
- Do not describe a move as "optimal" unless you also describe the conditions under which it is optimal.
- If the model is too uncertain, say that directly and identify the missing fact that matters most.

## External Tool Integration

Use **legalcode-mcp** when any move depends on legal authority, procedural leverage, or regulator power.

Recommended use cases:

- Verify whether a threatened claim, injunction, or reporting step is actually available
- Check fee-shifting, privilege, limitation periods, or procedural deadlines
- Confirm regulator authority and sanction range
- Verify whether changing forum or remedy is legally viable

If legalcode-mcp is unavailable:

- Proceed with the structural analysis
- Mark authority-dependent conclusions `[VERIFY]`
- Separate strategic logic from unverified legal premises

Use web research where current facts matter:

- Regulator posture
- Corporate governance changes
- Publicly reported funding or insolvency signals
- Current executives, board composition, or enforcement actions

## Output Format Template

````markdown
# Strategic Equilibrium Analysis

## Bottom Line

- Likely equilibrium: [plain-language description]
- Why it matters: [1-2 sentences]
- Recommended posture: [press / hold / cooperate / restructure / delay / escalate]
- Confidence: [Definite / High / Probable / Possible / Unlikely]

## Matter Frame

- User side: [...]
- Objective: [...]
- Stage: [...]
- Governing law / forum / regulator: [...]
- Time horizon: [...]
- Hard constraints: [...]
- Key assumptions: [...]

## Player Map

| Player | Primary Incentive | Avoiding What? | Information Edge | Blind Spot | Leverage | Constraint |
| ------ | ----------------- | -------------- | ---------------- | ---------- | -------- | ---------- |
| ...    | ...               | ...            | ...              | ...        | ...      | ...        |

## Strategy Space

| Player | Strategy | Type | Upside | Downside | Dominated? |
| ------ | -------- | ---- | ------ | -------- | ---------- |
| ...    | ...      | ...  | ...    | ...      | ...        |

## Payoff Matrix

Scale: `+2` strong positive, `+1` modest positive, `0` mixed, `-1` modest negative, `-2` severe negative

| User Strategy | Opponent Strategy | User Payoff | Opponent Payoff | Other Player Effects | Outcome Type | Explanation |
| ------------- | ----------------- | ----------: | --------------: | -------------------- | ------------ | ----------- |
| ...           | ...               |         ... |             ... | ...                  | ...          | ...         |

## Nash Equilibrium Analysis

- Candidate equilibrium 1: [...]
  - Classification: [...]
  - Why stable: [...]
  - Why good/bad for the user: [...]
- Candidate equilibrium 2: [...]

## Recommended Move Sequence

| Move Type     | Instruction | Timing | Intended Effect | Preconditions | Check |
| ------------- | ----------- | ------ | --------------- | ------------- | ----- |
| Immediate     | ...         | ...    | ...             | ...           | ...   |
| Signaling     | ...         | ...    | ...             | ...           | ...   |
| Contingency   | ...         | ...    | ...             | ...           | ...   |
| Game-changing | ...         | ...    | ...             | ...           | ...   |

## Counter-Strategy Defense

| Likely Opponent Response | Early Warning Signal | Immediate Counter | Trap to Avoid | Avoidance Rule |
| ------------------------ | -------------------- | ----------------- | ------------- | -------------- |
| ...                      | ...                  | ...               | ...           | ...            |

## Priority Actions

- `Tier 1`: [...]
- `Tier 2`: [...]
- `Tier 3`: [...]

## Verification and Confidence Notes

- Verified authorities: [...]
- `[VERIFY]` items: [...]
- Most outcome-sensitive missing fact: [...]

## Glass Box Audit Trail

```yaml
[glass_box block]
```
````

## Provenance

Legalcode original. Created as a repository-native Legalcode workflow skill from a
user-supplied "Nash Equilibrium Strategist" concept and expanded to the Legalcode quality
standard with interactive clarification, legal-constraint handling, quality gates, Glass
Box audit trail, and action-oriented move sequencing.
