---
name: legalcode-settlement-negotiation
description: Structure settlement negotiation frameworks with probability-weighted outcome modeling, risk-adjusted
  present values, and decision tree analysis. Use when preparing for settlement discussions, evaluating
  opponent's position, building a negotiation playbook, or advising clients on walk-away thresholds across
  civil disputes. Covers BATNA/WATNA/ZOPA analysis, opening position calculation, concession strategy,
  non-monetary terms, confidentiality provisions, release scope, and probability-weighted damages modeling.
  Supports both claimant and defendant perspectives. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers for US, UK, and AU practice. Integrates with legalcode-early-case-assessment for merits input
  and legalcode-damages-calculation for exposure quantification.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Settlement Negotiation

> **Disclaimer**: This skill provides a framework for AI-assisted settlement negotiation
> analysis in civil disputes. It does not constitute legal advice, litigation strategy, or
> a substitute for qualified legal counsel licensed in the relevant jurisdiction. Settlement
> positions, valuation ranges, and negotiation tactics produced by this skill are analytical
> frameworks, not binding representations. Laws governing settlement enforceability, ADR
> procedures, confidentiality, and release scope vary significantly by jurisdiction and
> dispute type. Verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them.

---

## Purpose and Scope

Use this skill to build a structured, defensible settlement negotiation framework before,
during, or after entering negotiations in civil disputes. The skill operationalizes
BATNA/WATNA/ZOPA analysis, probability-weighted outcome modeling, and concession strategy
into a decision-ready playbook.

**Covers:**

- BATNA (Best Alternative to Negotiated Agreement) analysis with probability weighting
- WATNA (Worst Alternative to Negotiated Agreement) modeling and scenario testing
- ZOPA (Zone of Possible Agreement) identification and corridor mapping
- Opening position calculation and anchoring strategy
- Concession pattern design (sequencing, timing, magnitude)
- Leverage point identification and timeline mapping
- Non-monetary terms analysis (injunctive relief, admissions, behavioral commitments)
- Confidentiality provision structure and enforceability
- Release scope drafting guidance (known vs. unknown claims, reservation of rights)
- Structured payment and alternative settlement consideration
- Settlement playbook generation for plaintiff and defense perspectives
- Decision tree analysis with sensitivity testing
- Multi-stakeholder authorization mapping

**Does not:**

- Replace qualified legal counsel or binding legal advice
- Produce final settlement agreements or term sheets (see drafting skills)
- Provide forensic accounting or economic expert opinions
- Apply to criminal proceedings, sentencing, or plea negotiations (different framework)
- Cover arbitration award negotiations or public procurement disputes

**Related skills:**

- `legalcode-early-case-assessment` — Merits and exposure input for settlement modeling
- `legalcode-damages-calculation` — Granular damages quantification and probability weighting
- `legalcode-legal-risk-assessment` — Enterprise-wide risk context
- `legalcode-privilege-review` — Protecting settlement analysis as work product

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the substantive governing law
and the procedural forum first, then localize all settlement analysis accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

**Settlement procedure:**

- Offer mechanics and acceptance requirements
- Court approval requirements (class actions, minor parties, protected persons)
- ADR/mediation obligations and pre-action protocols
- Mediator qualification and confidentiality rules

**Financial effects:**

- Tax treatment of settlement proceeds (income vs. capital)
- Structured settlement regulatory framework
- Fee-shifting and costs consequences of settlement offers

**Substantive release issues:**

- Known vs. unknown claims waiver requirements (CCP §1542 equivalents)
- Class action release scope and notice requirements
- Regulatory/governmental settlement constraints

**Reference anchors frequently needed:**

**United States (Federal):**

- Rule 68 (FRCP): Offers of judgment and cost consequences [VERIFY]
- Rule 408 (FRE): Settlement offer admissibility protection [VERIFY]
- Rule 23(e): Class action settlement approval process [VERIFY]
- Cal. CCP §1542: Known vs. unknown claims waiver (California) [VERIFY]
- IRC §104: Exclusion of settlement proceeds from gross income [VERIFY]

**United Kingdom (England & Wales):**

- CPR Part 36 (amended October 2024): Offers to settle, costs consequences, fixed
  recoverable costs for fast/intermediate track claims under £100,000 [VERIFY]
- Calderbank letters: Without prejudice save as to costs — _Calderbank v Calderbank_ [1975] [VERIFY]
- Tomlin Orders: Court-approved consent orders with confidential settlement schedule [VERIFY]
- CPR r.21.10: Settlement approval for protected parties (children, persons under disability) [VERIFY]
- Bank of Credit and Commerce SA v Ali [2001] UKHL 8: Unknown claims release principles [VERIFY]

**Australia:**

- Federal Court Rules 2011 Div 26.2: Offers of compromise [VERIFY]
- UCPR (NSW) r.20.26: Offers of compromise and costs consequences [VERIFY]
- AMDRAS (effective 1 July 2025): Australian Mediator and Dispute Resolution Accreditation
  Standards (replaced NMAS; new tiers: Mediator / Advanced Mediator / Leading Mediator) [VERIFY]
- FCA s.33V: Approval of class action settlements [VERIFY]
- Lendlease v Pallas (HCA 2025): Pre-mediation class closure orders confirmed [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer changes the fundamental framing of the analysis
- Plaintiff and defendant perspectives require different modeling approaches
- Business priorities override purely legal optimization
- Authorization constraints affect which settlement options are realistic

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

### Step 1: Accept Matter Input

Accept the matter description in any of these formats:

- **Litigation file or pleadings**: Case summary, complaint, key motions, expert reports
- **Prior assessment**: Output from `legalcode-early-case-assessment` or similar
- **Free-text brief**: Narrative description of claims, parties, and current posture
- **Data inputs**: Damages model, expert reports, key evidence inventory

If no matter information is provided, prompt the user to supply key inputs: dispute type,
parties, claims asserted, current procedural stage, damages estimate, governing law/forum.

### Step 2: Gather Context via CLARIFY

**⟁ CLARIFY** — Before modeling, gather these five decision inputs:

1. **Negotiation objective** — What should this analysis produce?
   - Options: `Establish settlement corridor`, `Prepare opening position`,
     `Evaluate opponent's offer`, `Build full negotiation playbook`, `Design mediation proposal`
   - _Why this matters_: Controls depth of scenario modeling vs. position evaluation.

2. **Your side and role** — Whose perspective should this analysis take?
   - Options: `Claimant/plaintiff counsel`, `Defendant/respondent counsel`,
     `In-house decision-maker (claimant)`, `In-house decision-maker (defendant)`,
     `Neutral mediator`, `Joint evaluation`
   - _Why this matters_: BATNA/WATNA are mirror images across the table; perspective
     determines what to optimize.

3. **Procedural stage and time horizon** — Where are you in the dispute?
   - Options: `Pre-suit / demand phase`, `Early litigation (pre-discovery)`,
     `Mid-litigation (active discovery)`, `Late litigation (trial imminent)`,
     `Post-trial / appeal`, `Mediation underway or scheduled`
   - _Why this matters_: Stage determines leverage dynamics, walk-away cost, and
     corridor urgency.

4. **Risk appetite and business priorities** — What drives the settlement objective?
   - Options: `Business continuity critical (avoid disruption)`,
     `Time-value is decisive (close quickly)`,
     `Principle/precedent matters (willing to litigate longer)`,
     `Relationship preservation important`,
     `Pure economics (optimize net present value)`
   - Allow multiple selections.
   - _Why this matters_: Risk appetite changes whether to push corridor or accept quickly.

5. **Probability weighting approach** — How should the corridor be modeled?
   - Options: `Gross damages only (separate BATNA probability)`,
     `Probability-weighted expected value (multiply damages × win probability)`,
     `Scenario branches (separate optimistic/realistic/conservative)`,
     `Let me specify liability probability explicitly`
   - _Why this matters_: Different approaches suit different client communication needs
     and internal authorization frameworks.

State assumptions explicitly for any question the user does not answer.

### Step 3: Map the Dispute Structure

Capture the full dispute architecture before any valuation:

1. **Claim inventory** — List every claim, cross-claim, and counterclaim:

   | Claim                | Party      | Legal Basis        | Damages Category | Likely Range | Liability Strength |
   | -------------------- | ---------- | ------------------ | ---------------- | ------------ | ------------------ |
   | [Breach of contract] | [Claimant] | [UCC / Common law] | [Lost profits]   | [$X-$Y]      | [High/Med/Low]     |

2. **Defense inventory** — For each claim, map available defenses:

   | Defense               | Applicable to | Strength | Evidence Base         | Jurisdiction Note         |
   | --------------------- | ------------- | -------- | --------------------- | ------------------------- |
   | [Failure to mitigate] | [Claim 1]     | [Med]    | [Mitigation evidence] | [[JURISDICTION-SPECIFIC]] |

3. **Counterclaim exposure** — Model any claims the opposing party holds:
   - Do not ignore plausible counterclaims; they form part of the defendant's BATNA
     and the claimant's own downside scenario

4. **Authorization hierarchy** — Who must approve settlement at each threshold?

   | Threshold | Approver                  | Turnaround | Constraints                   |
   | --------- | ------------------------- | ---------- | ----------------------------- |
   | Below $X  | [Litigation counsel / GC] | [24h]      | [Insurance consent required?] |
   | $X to $Y  | [GC / CFO]                | [72h]      | [Board notification]          |
   | Above $Y  | [CEO / Board]             | [7d+]      | [Regulatory disclosure?]      |

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the governing law and forum, then use **legalcode-mcp** to build a working legal
reference file for this analysis.

**legalcode-mcp** is the Legalcode law, regulatory, and case law database.

```
legalcode-mcp searches for this analysis:
1. Offer of judgment / Part 36 mechanics and cost consequences in [forum]
2. ADR obligations and pre-action protocols in [forum]
3. Settlement release language requirements for [claim type] in [jurisdiction]
4. Class action / collective action settlement approval requirements (if applicable)
5. Tax treatment of [claim type] settlement proceeds in [jurisdiction]
6. Without prejudice / Rule 408 protection scope in [forum]
7. Recent comparable settlements in [claim type/industry] (if available)
```

Save results to `/tmp/legalcode-settlement-research.md`.

**Without legalcode-mcp:**

- Mark all jurisdiction-specific references [VERIFY]
- Note: `legalcode_mcp: "Not connected"` in Glass Box
- Focus on modeling quality and structural rigor

### Step 5: Build the BATNA / WATNA Model

The BATNA and WATNA are the anchors for every settlement position. Build them first,
before setting any opening demand or offer.

**⟁ CLARIFY** — For BATNA modeling:

"What is your best realistic alternative if settlement fails entirely? Consider:

- `Full litigation to judgment` — what would a favorable outcome look like?
- `Arbitration` — is this an option? Faster/cheaper than trial?
- `Regulatory complaint` — is a regulatory path available that creates parallel pressure?
- `Walk away / write off` — is abandoning the claim or defense the actual BATNA?
- `Business restructuring` — does the party have a business solution that reduces exposure?"

#### 5a. BATNA Analysis

For **each** side (your side and counterparty):

```
BATNA Template:

Outcome:              [Describe the best alternative outcome]
Legal path:           [Litigation / Arbitration / Regulatory / Other]
Probability of achieving BATNA outcome:  [0.XX — Definite/High/Probable/Possible/Unlikely]
Expected value if BATNA achieved:        $[Damages recovered / Liability avoided]
Timeline to BATNA resolution:            [Months to trial + enforcement]
Expected legal spend to reach BATNA:     $[Phase-by-phase cost estimate]
Execution risks:                         [Evidence gaps, legal uncertainty, enforcement risk]
Risk-adjusted BATNA value:              = (Probability × Outcome Value) – Legal Spend

BATNA Net Present Value (if lengthy):   = Risk-adjusted BATNA Value × PV discount factor
```

**Decision tree methodology (for complex multi-node disputes):** Map each litigation
decision node with probability branches and outcome values, then calculate expected value
by backward induction — rolling back from terminal nodes, multiplying values by
probabilities at each node, and summing across branches.

```
Example decision tree (plaintiff's BATNA):
  Node 1: Summary judgment → P(granted for defendant) = 0.25; P(denied) = 0.75
  Node 2: Trial liability → P(plaintiff wins) = 0.60; P(defendant wins) = 0.40
  Node 3: Damages if win → E(damages) = $2M
  Node 4: Appeal → P(reversal) = 0.15; P(affirmed) = 0.85

  Terminal value (win → affirmed) = $2M × 0.75 × 0.60 × 0.85 = $765,000
  Net of litigation costs ($300K to trial) = $465,000

  Plaintiff MAS = risk-adjusted BATNA net of costs = ~$465,000
  Any offer above $465,000 exceeds BATNA → rational to settle
```

[JURISDICTION-SPECIFIC] Apply jurisdiction's discount rate for future litigation cash flows.
Many US practitioners use 8-12% nominal; UK and AU practice varies. Confirm with client.

#### 5b. WATNA Analysis

For each side:

```
WATNA Template:

Outcome:              [Describe the worst realistic alternative outcome]
Probability of WATNA:                    [0.XX]
Value if WATNA occurs:                   $[Damages lost / Liability incurred]
Timeline:                                [Months to adverse judgment + enforcement]
Additional costs (legal spend + disruption): $[Estimate]
Risk-adjusted WATNA value:              = (Probability × Adverse Outcome) + Legal Spend

Include:
- Adverse judgment scenario
- Costs award against (if applicable)
- Reputational/regulatory spillover
- Business disruption during litigation
- Collateral damage (customer/supplier/employee relations)
```

#### 5c. ZOPA Identification

The Zone of Possible Agreement exists where:

```
ZOPA exists when:
  Claimant's walk-away (minimum acceptable settlement) < Defendant's walk-away (maximum acceptable settlement)

Claimant's MAS (Minimum Acceptable Settlement):
  = Risk-adjusted BATNA value (net) + small risk premium for certainty
  = MAX(WATNA baseline, net settlement value where litigation is irrational)

Defendant's MAS (Maximum Acceptable Settlement):
  = Risk-adjusted BATNA value (net) + small premium for dispute resolution
  = MIN(BATNA ceiling, net present value of judgment exposure)

If Claimant MAS > Defendant MAS: ZOPA does not exist → mediation or impasse likely
If Claimant MAS < Defendant MAS: ZOPA exists → settlement is rational for both
ZOPA Width = Defendant MAS – Claimant MAS
```

**⟁ CLARIFY** — If ZOPA appears to not exist, ask:
"The BATNA analysis suggests the parties' walk-away positions may not overlap. This means
settlement on purely economic terms may be irrational for one side. Should I:
(A) Re-examine BATNA assumptions (probability estimates may need calibration)
(B) Model non-monetary terms that could bridge the gap
(C) Identify timing events that would shift one side's BATNA before settling
(D) Proceed — model the gap and recommend how to shift it"

### Step 6: Calculate Opening Position and Anchor

Opening position strategy depends on whether the framework is positional or interest-based.

#### 6a. Positional Opening (Traditional / Adversarial)

Determine opening based on research-anchored aspiration levels:

**For claimants:**

```
Opening demand calculation (positional):
1. Identify ceiling damages (best-case interpretation, all claims)
2. Apply high-end multiplier for contingencies (+10-25% above ceiling)
3. Flag jurisdictional limits (caps, fee-shifting consequences of unreasonable demand)
4. Target: Opening = 1.5-3× target settlement (depending on counterparty profile)

Anchoring research: locate comparable verdicts/settlements to justify opening
[JURISDICTION-SPECIFIC] Check Rule 68/Part 36 consequences of unreasonable demands
```

**For defendants:**

```
Opening offer calculation (positional):
1. Identify floor damages (best-case defense interpretation)
2. Apply nuisance-value baseline for cost-of-defense analysis
3. Consider any counterclaimant leverage as offset to opening offer
4. Target: Opening = 30-60% of anticipated target settlement
```

[JURISDICTION-SPECIFIC] In UK Part 36 practice, the opening offer carries formal cost
consequences if not beaten at trial. Opening too low creates Part 36 risk. Calibrate
opening with reference to realistic trial range, not positional aspiration. [VERIFY]

#### 6b. Principled Opening (Interest-Based / Negotiation Theory)

Apply the four principles of interest-based negotiation (Fisher & Ury):

1. **Separate the people from the problem** — Open with acknowledgment of shared interest
   in resolution before position statement
2. **Focus on interests, not positions** — Lead with the interest served by resolution;
   avoid demand framing until interests are acknowledged
3. **Generate options before settling** — Propose a menu of settlement structures rather
   than a single figure
4. **Insist on objective criteria** — Anchor opening to documented market comparables,
   published verdict databases, or regulatory settlement benchmarks

**⟁ CLARIFY** — Ask client:
"Do you prefer a positional or principled opening approach?

- `Positional`: Start with an anchored demand, expect counter-demand, negotiate toward
  target. Faster, but may increase adversarial temperature.
- `Principled`: Open with framework and interests; invite counterparty to jointly explore
  settlement options. Better for relationship-sensitive matters; counterparty may exploit
  if they are positional."

#### 6c. Anchoring Analysis

Before confirming opening position, run this anchoring check:

| Factor                                    | Finding               | Impact on Opening            |
| ----------------------------------------- | --------------------- | ---------------------------- |
| Comparable verdicts (favoring you)        | $[Range / None found] | [Raises / Lowers / Neutral]  |
| Comparable settlements (favoring you)     | $[Range / None found] | [Raises / Lowers / Neutral]  |
| Regulatory benchmark                      | $[If applicable]      | [Sets floor / ceiling]       |
| Counterparty's stated or implied position | $[Known / Unknown]    | [Inform, don't anchor to it] |
| Part 36/Rule 68 cost risk of demand       | [Yes / No / NA]       | [Constrain opening?]         |
| Insurance coverage limit (defendant)      | $[Known / Unknown]    | [May cap realistic ceiling]  |

### Step 7: Model Settlement Corridor

Build the three-point settlement corridor with explicit assumptions:

```
Settlement Corridor:

Floor (minimum realistic settlement):
  = MAX(Claimant MAS, Nuisance value baseline)
  $[Low]

Target (expected settlement under realistic assumptions):
  = Midpoint of risk-adjusted BATNA values ± negotiation friction
  $[Target]

Ceiling (maximum realistic defendant payment):
  = MIN(Defendant MAS, Insurance/financial capacity ceiling)
  $[High]

Corridor width: $[High – Low]
Target confidence: [0.XX — level from Confidence Scoring table]
```

**⟁ CLARIFY** — Present corridor to user and ask:
"Based on BATNA/WATNA modeling, the settlement corridor is $[Low]–$[High] with target
at $[Target]. Before proceeding:

- Is this corridor consistent with your client's business expectations?
- Are there authorization or insurance constraints that change the ceiling or floor?
- Should I adjust any BATNA probability assumptions before building negotiation scenarios?"

#### 7a. Probability-Weighted Settlement Value (if requested)

For clients who want expected value rather than range:

```
Expected Value Model:

EV(Claimant) = Σ (Scenario probability × Net outcome)

Scenario 1 — Win at trial:      P(win) × Damages_win – Legal spend to trial
Scenario 2 — Partial win:       P(partial) × Damages_partial – Legal spend to trial
Scenario 3 — Lose:              P(lose) × 0 – Legal spend to trial – Costs award risk
Scenario 4 — Settlement at $X:  P(settle) × $X – Legal spend to settlement

Settlement is preferred when EV(Settlement) > EV(Litigate)

[JURISDICTION-SPECIFIC] Include fee-shifting and costs consequences in EV calculation.
UK/AU costs exposure can significantly reduce EV(Litigate) for uncertain claimants.
```

#### 7b. Sensitivity Analysis

Test the corridor against key assumption changes:

| Variable              | Base Case  | Adverse Shift             | Favorable Shift           | Corridor Sensitivity      |
| --------------------- | ---------- | ------------------------- | ------------------------- | ------------------------- |
| Liability probability | [P]        | [P–15%] → $[New corridor] | [P+15%] → $[New corridor] | [High/Med/Low]            |
| Damages ceiling       | $[X]       | −20% → $[New]             | +20% → $[New]             | [High/Med/Low]            |
| Legal spend to trial  | $[Y]       | +50% → $[New EV]          | −25% → $[New EV]          | [Med]                     |
| Costs award risk      | $[Z]       | Triggered → $[New EV]     | Waived → $[New EV]        | [[JURISDICTION-SPECIFIC]] |
| Time to trial         | [N months] | +6 months → PV discount   | −3 months → Urgency shift | [Med/Low]                 |

### Step 8: Design Concession Strategy

A concession strategy determines when, how much, and in what sequence to move.

#### 8a. Concession Pattern Rules

**Diminishing concessions principle**: Each concession should be smaller than the last.
This signals approach to a floor rather than willingness to concede indefinitely.

```
Concession pattern (recommended for positional approach):
Move 1: Large — [25-35% of gap from opening to target]. Signals good faith.
Move 2: Medium — [15-20% of gap]. Responds to counterparty movement.
Move 3: Small — [8-12% of gap]. Signals slowing approach to floor.
Move 4+: Micro — [2-5% of remaining gap or freeze]. Signals finality.
```

**⟁ CLARIFY** — Ask: "What is your counterparty's typical negotiation profile?

- `Institutional repeat player`: Match their move cadence; they will mirror your pattern
- `One-shot party with high emotion`: Larger early move to de-escalate; slower later
- `Sophisticated transactional negotiator`: Principled approach preferred
- `Unknown`: Default to diminishing concession pattern"

#### 8b. Leverage Events and Concession Timing

Map each leverage event to optimal concession timing:

| Leverage Event            | Date   | Effect                                              | Recommended Move                                                      |
| ------------------------- | ------ | --------------------------------------------------- | --------------------------------------------------------------------- |
| Discovery close-out       | [Date] | Reduces defendant's uncertainty                     | Make next concession before this date to capture good-faith credit    |
| Expert report served      | [Date] | Strengthens/weakens your damages position           | Hold until report is served; use report to justify or revise position |
| Dispositive motion ruling | [Date] | Binary shift if granted                             | Consider contingent offer tied to ruling outcome                      |
| Mediation session         | [Date] | Mediator reality-checks both sides                  | Largest moves timed for mediation session                             |
| Trial date                | [Date] | Maximum urgency; high-cost-of-continued-negotiation | Reserve final concession for trial proximate window                   |

[JURISDICTION-SPECIFIC] UK Part 36 offers have formal timing mechanics (21-day periods)
that interact with concession timing. The "relevant period" and cost consequences of late
acceptance differ from open-ended offers. [VERIFY]

#### 8c. Package Deal and Logrolling

Identify terms with asymmetric value across parties for trade:

| Term                       | Value to You                      | Value to Counterparty      | Trade Opportunity                                |
| -------------------------- | --------------------------------- | -------------------------- | ------------------------------------------------ |
| Payment amount             | High (claimant) / Low (defendant) | Opposite                   | Primary trade axis                               |
| Payment timing             | Medium                            | Often High (cashflow)      | Lump sum for higher amount; structured for lower |
| Admission of liability     | High (precedent)                  | High (coverage/reputation) | May be harder to trade                           |
| Non-disparagement          | Medium                            | Medium                     | Standard trade element                           |
| Confidentiality            | Variable                          | High (reputational)        | Trade publicity for dollars                      |
| Injunctive relief          | High (where conduct continues)    | High (operational cost)    | Negotiate narrow scope                           |
| Release breadth            | Medium                            | High (certainty)           | Broad release for increased payment              |
| Attorney's fees            | Medium (each side)                | Medium (each side)         | Each bears own, or partial recovery              |
| Reference letter / apology | Low (legal) / High (emotional)    | Low (legal)                | Low-cost face-saving for claimant                |

### Step 9: Analyze Non-Monetary Terms and Ancillary Provisions

Settlement often involves non-monetary terms that are as consequential as the payment.

#### 9a. Release Scope Analysis

**⟁ CLARIFY** — Before drafting release guidance, ask:
"What claims should the release cover?

- `All claims to date` — General release, known and unknown, all parties
- `Specific claims only` — Limited to claims in the action
- `Mutual release` — Both sides release each other
- `Unilateral release` — Only one side releases
- `Reserve unknown claims` — Known claims only (equivalent of §1542 carve-out)"

**Known vs. Unknown Claims:**

[JURISDICTION-SPECIFIC] The scope of releasable claims varies significantly:

- **US (California)**: Cal. CCP §1542 (amended January 1, 2019 — must use current statutory
  language verbatim). Provides that a general release does not extend to claims the releasing
  party does not know exist at execution. To validly waive unknown claims: (1) quote the
  current statute verbatim; (2) include a separate signature or initials line specifically
  acknowledging the §1542 waiver; (3) establish actual knowing waiver — broad "any and all
  claims" language alone is insufficient. [VERIFY]
- **US (federal/other states)**: Majority rule requires clear language to release unknown
  claims; "any and all claims" is generally sufficient but state law varies significantly.
  Research applicable state equivalent before drafting. [VERIFY]
- **UK**: Governed by common law contractual construction. _Bank of Credit and Commerce SA
  v Ali_ [2001] UKHL 8 established the "cautionary principle" — courts are slow to infer
  surrender of unknown rights absent clear language. However, sophisticated commercial
  parties can release unknown claims with explicit drafting. Enumerate claim categories with
  particularity; do not rely on broad "all claims" language alone. [VERIFY]
- **AU**: Governed by common law; recitals in a deed of release are critical to define scope.
  Courts look to what both parties reasonably understood they were agreeing to. Most
  comprehensive settlements are executed as deeds (not contracts) for enforceability without
  consideration issues. _Grant v John Grant & Sons Pty Limited_ (HCA): special interpretive
  rules apply to releases. [VERIFY]

**Release drafting checklist:**

- [ ] Identify all releasors and releasees (include affiliated entities, officers, directors if appropriate)
- [ ] Enumerate or describe covered claims (suit caption vs. subject matter vs. all claims)
- [ ] Decide whether unknown claims are released (and applicable statutory waiver)
- [ ] Include reservation of rights for any ongoing obligations
- [ ] Carve out claims that are genuinely not being settled (government regulatory claims?)
- [ ] Anti-assignment of claims provisions (if party has assigned claims to third party)
- [ ] Covenant not to sue vs. release distinction (different remedies for breach)

#### 9b. Confidentiality Provisions

Analyze whether a confidentiality obligation is appropriate and enforceable:

**⟁ CLARIFY** — "Should the settlement be confidential?

- `Full confidentiality` — Terms, existence, and parties are confidential
- `Terms confidential only` — Existence may be acknowledged; terms are sealed
- `No confidentiality` — Public settlement (often for government parties or class actions)
- `Conditional` — Confidential unless required by law, court order, or regulatory reporting"

**Enforceability considerations:**

[JURISDICTION-SPECIFIC]

- **US**: Generally enforceable in civil disputes; courts are moving toward greater
  transparency (particularly post-#MeToo). FLSA collective action settlements cannot
  be confidential (Cheeks doctrine, 2d Cir.). Class action settlements require court
  approval and public notice. [VERIFY]
- **UK**: Confidentiality in settlements is well-established; "Tomlin Orders" allow
  confidential terms to be recorded as a schedule (not on the face of the court order).
  Gagging clauses in employment settlements are subject to restrictions post-2019. [VERIFY]
- **AU**: Enforceable generally; class action settlements under FCA s.33V require court
  approval. Some jurisdictions have rules limiting confidentiality in workplace matters. [VERIFY]

**Confidentiality provision checklist:**

- [ ] Define what is confidential (amount, terms, existence, parties)
- [ ] Define who may know (counsel, financial advisors, tax authorities, insurers)
- [ ] Exceptions for legal/regulatory compelled disclosure
- [ ] Clawback provision if breach occurs (return of settlement?)
- [ ] Permitted disclosure to court for enforcement
- [ ] Survival clause (confidentiality survives termination of agreement)
- [ ] Liquidated damages for breach (if monetary amount is important to keep secret)

#### 9c. Non-Monetary Term Valuation

Assign approximate value to each non-monetary term for trade purposes:

| Term                          | Estimated Value to Claimant     | Estimated Value to Defendant         | Notes                            |
| ----------------------------- | ------------------------------- | ------------------------------------ | -------------------------------- |
| Admission of liability        | [High — precedent; insurance]   | [High — denials in insurance policy] | [JURISDICTION-SPECIFIC]          |
| Public apology                | [High — emotional/reputational] | [Low-Medium — face-saving cost]      | Context-dependent                |
| Non-disparagement (mutual)    | [Medium]                        | [Medium]                             | Standard in commercial           |
| Injunctive undertaking        | [High — prevents future harm]   | [High — operational cost]            | Scope matters                    |
| Reference / non-opposition    | [Medium — HR/commercial]        | [Low cost]                           | Employment disputes              |
| Behavioral commitments        | [High — ongoing protection]     | [High — compliance cost]             |                                  |
| Future contract / business    | [High — commercial value]       | [Medium]                             | Be careful: FCPA/corruption risk |
| Technology transfer / license | [High]                          | [Depends on IP strategy]             | [JURISDICTION-SPECIFIC]          |
| Regulatory cooperation        | [Low-Medium]                    | [Medium — can limit exposure]        | Government interest              |

---

## Settlement Term Classification

Classify each settlement element into one of three disposition categories:

| Class      | Label             | Meaning                                                               | Response                                                 |
| ---------- | ----------------- | --------------------------------------------------------------------- | -------------------------------------------------------- |
| `CORE`     | Non-negotiable    | Absent this term, settlement will not proceed; walk-away trigger      | Hold firm; do not trade                                  |
| `TARGET`   | Strong preference | Important to your client; meaningful movement acceptable to close gap | Move only in exchange for significant counter-concession |
| `FLEXIBLE` | Tradeable         | Can be conceded to preserve CORE and TARGET terms                     | Use as concession currency                               |

Apply this classification to every settlement term before entering negotiations. The
classification should be reviewed and updated as negotiations progress and new information
emerges.

---

## Actionable Output Per Finding

For each identified gap or issue in the settlement framework, provide:

| Element                       | Classification         | Gap                               | Recommended Action                                                         | Owner      | Priority |
| ----------------------------- | ---------------------- | --------------------------------- | -------------------------------------------------------------------------- | ---------- | -------- |
| [Settlement amount gap]       | [CORE/TARGET/FLEXIBLE] | $[Spread]                         | [Make second move of $X]                                                   | [Counsel]  | [Tier 1] |
| [Release scope unclear]       | [CORE]                 | [Unknown claims not addressed]    | [Draft §1542 waiver / equivalent]                                          | [Counsel]  | [Tier 1] |
| [Confidentiality not agreed]  | [TARGET]               | [Counterparty resists]            | [Propose partial confidentiality — terms only]                             | [Counsel]  | [Tier 2] |
| [Authorization delay]         | [Structural]           | [Board approval needed]           | [Estimate approval timeline; request matching extension from counterparty] | [GC/Board] | [Tier 1] |
| [Non-monetary term leveraged] | [FLEXIBLE]             | [Admission of liability demanded] | [Deny admission; increase payment by $X to compensate]                     | [Counsel]  | [Tier 2] |

---

## Prioritization Framework

| Tier     | Label               | Criteria                                                                                              | Action Timeline                         |
| -------- | ------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `Tier 1` | Immediate           | BATNA/WATNA calculation errors; authorization constraints; walk-away threshold not established        | Resolve before any negotiation session  |
| `Tier 2` | Pre-negotiation     | Opening position set; release scope confirmed; confidentiality agreed; leverage point timeline mapped | Complete before first substantive offer |
| `Tier 3` | Negotiation cadence | Concession strategy calibrated; scenario responses prepared; non-monetary term trades modeled         | Review at each negotiation session      |
| `Tier 4` | Agreement drafting  | Term sheet confirmed; release scope finalized; ancillary provisions agreed                            | After corridor is accepted              |

---

## Deep Analysis: Settlement Negotiation Domains

Evaluate all 10 domains unless explicitly scoped down.

| Domain                     | What to Assess                                          | Key Signals                                                       | Settlement Impact                                   |
| -------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| 1. Liability exposure      | Probability and magnitude of adverse judgment           | Legal authority, evidence quality, comparable verdicts            | Drives floor/ceiling of corridor                    |
| 2. Damages exposure        | Range of recoverable damages with probability weighting | Expert reports, financial records, comparable awards              | Sets the quantum dimension of corridor              |
| 3. Counterparty BATNA      | What counterparty gains by rejecting settlement         | Their litigation posture, financial capacity, BATNA alternatives  | Determines counterparty's walk-away; shapes ZOPA    |
| 4. Leverage timeline       | Events that shift bargaining power over time            | Trial date, motion calendar, discovery deadlines, business cycles | Drives concession timing and urgency                |
| 5. Authorization structure | Who can say "yes" and under what constraints            | Client hierarchy, insurance consent clauses, regulatory approvals | May create timing bottlenecks                       |
| 6. Financial capacity      | Can counterparty actually pay?                          | Credit, insurance limits, asset availability, restructuring risk  | Sets hard ceiling independent of legal exposure     |
| 7. Non-monetary dimensions | What non-cash terms matter to each side                 | Confidentiality, admission, injunction, ongoing relationship      | Expands tradeable space beyond dollars              |
| 8. Procedural leverage     | Motions, evidence rulings, and process events           | Upcoming motion calendar, disclosure burden, costs exposure       | Can shift BATNA without changing substantive merits |
| 9. External factors        | Events outside the litigation that affect settlement    | Regulatory investigation, business transaction, market conditions | May create urgency or constraint on either side     |
| 10. Communication strategy | How each side presents positions                        | Tone, channel, sequencing, face-saving needs                      | Affects whether corridor is reached in practice     |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any settlement analysis. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                                | Fail Action                                                               |
| -------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Source**     | Every legal proposition (Rule 408, Part 36, §1542, etc.) cites a specific statute, rule, or case    | Add citation or mark `[UNVERIFIED — counsel to confirm]`                  |
| **Format**     | Citations use a consistent, jurisdiction-recognizable format                                        | Fix format                                                                |
| **Currency**   | Check for statutory amendments (particularly procedural rules and tax treatment)                    | Flag `[CHECK CURRENCY]`                                                   |
| **Domain**     | Keep substantive law analysis within the governing law jurisdiction                                 | Remove or flag jurisdictional bleed                                       |
| **Confidence** | Settlement valuations are forward-looking and uncertain; explicitly state confidence level for each | Add confidence qualifier; do not mask settlement uncertainty as precision |

---

## Self-Interrogation for Settlement Positions

For any settlement position or walk-away threshold classified as CORE (non-negotiable),
or for any probability estimate on which the corridor materially depends, apply this
3-pass review before delivery:

**Pass 1 — Settlement Logic Integrity**

- Does this settlement position follow logically from the BATNA/WATNA analysis?
- Would a reasonable experienced litigator in this jurisdiction agree with the corridor?
- Is there a critical assumption that, if wrong, would materially move the corridor?

**Pass 2 — Completeness of Modeling**

- Have all viable settlement structures been considered (lump-sum, structured payments,
  non-monetary terms, hybrid packages)?
- Have all leverage events been identified and mapped to the concession timeline?
- Has the counterparty's BATNA been modeled, not just assumed?

**Pass 3 — Adversarial Challenge**

- What is the strongest argument opposing counsel would make against this corridor?
- What concession would opposing counsel demand that we have not prepared for?
- Is the walk-away threshold realistically defensible to the client's decision-makers?

If any pass reveals weakness, revise before delivery. Mark the Glass Box:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

Assign a confidence level to each material settlement element:

| Level        | Range     | Meaning                                                       | Action                                                |
| ------------ | --------- | ------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, strong evidence, established settlement pattern  | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority/evidence, minor uncertainties                | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Defensible but reasonable practitioners would differ          | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuinely uncertain; counterparty may see it very differently | Flag for counsel review with both sides modeled       |
| **Unlikely** | 0.0-0.39  | Weak basis or highly speculative                              | Do not assert; flag `[UNCERTAIN — counsel to advise]` |

**Note**: A case with HIGH confidence in liability may still have POSSIBLE confidence in
settlement outcome — because settlement outcome depends on counterparty behavior, business
constraints, and information asymmetry, not just legal merits. Report both separately.

---

## Glass Box Audit Trail

Every settlement analysis MUST include a Glass Box section to make the reasoning auditable:

```yaml
glass_box:
  skill_name: "legalcode-settlement-negotiation"
  matter: "[Matter name/identifier]"
  negotiation_objective: "[Establish corridor / Prepare opening / Evaluate offer / Build playbook]"
  side_represented: "[Claimant / Defendant / Neutral / In-house]"
  governing_law: "[Substantive jurisdiction]"
  forum: "[Procedural forum]"
  procedural_stage: "[Pre-suit / Early / Discovery / Trial imminent / Post-trial]"
  claim_types: "[List of claims]"

  positions_modeled:
    your_batna: "$[Risk-adjusted value] (P=[probability], confidence=[level])"
    your_watna: "$[Risk-adjusted value] (P=[probability], confidence=[level])"
    counterparty_batna_estimated: "$[Estimated value] (confidence=[level])"
    settlement_corridor: "$[Low]–$[High], target $[Target]"

  models_built:
    batna_watna: "yes"
    zopa_analysis: "yes"
    opening_position: "yes"
    concession_strategy: "yes"
    leverage_timeline: "yes"
    scenario_analysis: "yes"
    non_monetary_terms: "yes"
    release_analysis: "yes"

  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-settlement-research.md or 'Not created']"

  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or [VERIFY]]"

  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or [VERIFY]]"

  citations_verified: "[N VERIFIED] / [N [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  probability_weighting_approach: "[Gross damages separate / Probability-weighted EV / Scenario branches]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"

  key_assumptions:
    - "[Liability probability assumption and basis]"
    - "[Damages ceiling/floor assumption and basis]"
    - "[Counterparty BATNA assumption and basis]"
    - "[Authorization constraint assumption]"

  data_gaps:
    - "[Missing market comparables]"
    - "[Counterparty financial capacity uncertain]"
    - "[Insurance coverage limits unknown]"

  limitations:
    - "Settlement analysis is forward-looking and contingent on stated assumptions"
    - "Counterparty walk-away point estimated; actual may differ materially"
    - "Probability estimates based on stated facts; subject to revision on new evidence"
    - "Does not constitute legal advice or a binding settlement recommendation"

  reviewer: "AI-assisted — requires qualified legal counsel review before negotiation"
```

---

## Anti-Patterns

Avoid these settlement negotiation failure modes:

1. **Starting with a settlement recommendation before establishing BATNA/WATNA**
   The settlement corridor has no anchor without knowing what each party's best and worst
   litigation alternatives are. BATNA/WATNA are not optional — they are the primary
   calculation inputs. A settlement corridor stated without BATNA/WATNA analysis is
   guesswork dressed as strategy.

2. **Treating settlement as binary instead of a phased leverage strategy**
   Settlement negotiations are not a single event but a multi-stage process where
   leverage shifts as litigation milestones are reached (discovery completion, expert
   reports, motion rulings, trial date proximity). Presenting a single static settlement
   figure ignores this dynamic.

3. **Single-point settlement estimates without ranges**
   Settlement outcomes are probabilistic. Stating "settle at $5M" without a range hides
   genuine uncertainty behind false precision. Ranges acknowledge the reality that
   counterparty behavior, evidence development, and procedural outcomes all affect where
   the deal actually closes.

4. **Ignoring the counterparty's BATNA**
   Modeling only your client's alternatives while treating the counterparty's walk-away as
   opaque is half an analysis. Settlement is rational only when both parties' alternatives
   are modeled. A claimant who assumes the defendant is desperate to settle, when the
   defendant's BATNA is actually strong, will systematically overprice the case.

5. **Conflating liability probability with settlement value**
   A 70% probability of winning does not mean the settlement should be 70% of the
   damages amount. Settlement value is affected by litigation cost, time value, risk
   aversion, trial risk, fee-shifting, and non-monetary considerations — not just liability
   probability. Mechanical probability discounting undersells strong cases and oversells
   weak ones.

6. **Anchoring only on damages, ignoring procedural leverage**
   Discovery burden, spoliation risk, motion calendar, and fee-shifting exposure are
   independent leverage sources that can shift corridor without affecting underlying
   damages. A defendant with a spoliation problem, or a claimant with a Part 36 offer
   outstanding, has leverage that does not flow from the merits.

7. **Missing leverage event timing**
   Failing to map when leverage events occur (expert deadline, motion ruling, trial date)
   and how each shifts the corridor means concession timing is arbitrary. The best move
   timed poorly is worse than a smaller move well-timed.

8. **Jurisdiction bleed in settlement law**
   Applying US Rule 408 privilege to UK settlement negotiations (where without prejudice
   privilege has different scope). Applying California §1542 unknown claims analysis to
   an English law release. Applying Part 36 cost consequences to non-UK proceedings.
   Settlement law is procedural and jurisdiction-specific; localize every procedural
   element.

9. **Not modeling alternative settlement structures**
   Assuming the settlement must be a lump-sum cash payment ignores structured payments,
   asset transfers, license grants, behavioral undertakings, and hybrid packages. Many
   impasses dissolve when the parties discover that what one side prizes (certainty of
   cash) differs from what the other side prizes (timing/structure). Structured creativity
   expands the ZOPA.

10. **Treating admissions and confidentiality as fixed**
    Admission of liability and public disclosure are often the highest-value tradeable
    terms but are routinely treated as non-negotiable by one side. A defendant who will
    pay $200K more to avoid an admission of liability is expressing a real and tradeable
    preference. If counsel fails to surface this, both clients leave value on the table.

11. **Presenting settlement recommendation without stating what would move it**
    A settlement corridor without documented triggers for revision is analytically
    incomplete. What adverse discovery finding would lower the ceiling? What favorable
    motion ruling would raise the floor? The corridor must be conditional, not static.

12. **Hidden uncertainty instead of escalating it**
    Stating a settlement position with HIGH confidence when key liability, damages, or
    counterparty information is genuinely uncertain. The temptation to appear decisive
    is dangerous — wrong settlement positions cost real money. Flag genuine uncertainty
    for counsel review; do not mask it as analytical precision.

13. **Ignoring authorization hierarchy and insurance consent clauses**
    A claimant counsel who negotiates past the counterparty's insurance limits, or a
    defendant counsel who agrees to terms without insurance consent where required by
    policy, risks an agreement that cannot be performed. Authority and insurance consent
    must be mapped before negotiations begin.

14. **Reusing stale verdict and settlement comparables**
    Jury verdict databases and published settlement reports age quickly. A verdict from
    five years ago in the same case type may be substantially higher or lower than current
    market due to case law shifts, inflation, jury pool changes, or post-COVID court
    dynamics. Always note the vintage of comparables.

15. **Designing for only one scenario**
    Building a settlement strategy around a single anticipated negotiation path — "they
    will make a lowball offer, we will counter with X, they will move to Y" — fails to
    prepare for actual counterparty behavior. Model at least three scenarios (optimistic,
    realistic, conservative) with distinct concession responses for each.

16. **Failing to prepare face-saving for the counterparty**
    Parties sometimes need a way to justify settlement to their principals (client,
    board, insurer, media) that is distinct from the actual settlement rationale. A
    defendant's GC may need to explain why they paid $X to a board that wanted to
    fight. Effective settlement counsel helps the opposing party explain the deal to
    their side — not by compromising position, but by framing the settlement in terms
    the counterparty can defend.

17. **Confusing your BATNA with your WATNA**
    BATNA is what you achieve if negotiations fail AND you pursue your best alternative.
    WATNA is what happens if negotiations fail AND things go poorly. Conflating them
    produces a distorted corridor — typically one that is either too aggressive (treating
    BATNA as certain) or too cautious (treating WATNA as the baseline).

---

## Writing Standards

Apply plain-language discipline to all settlement analysis output:

**For client-facing materials:**

- Plain language. No litigation jargon without explanation.
- Active voice: "The defendant pays $X by [date]" not "Payment of $X shall be made by defendant."
- Specific numbers with confidence qualifiers, not vague ranges: "$4.2M–$5.8M (Probable)"
  not "somewhere in the low-to-mid single millions."
- Short sentences. One point per sentence.

**For negotiation position papers:**

- Anchored to objective criteria (comparable verdicts, regulatory benchmarks, cost analysis)
- Avoid emotional language; maintain professional tone even in adversarial framing
- Do not overstate certainty — opposing counsel will challenge your claims

**Quality gates before delivery:**

1. Can a senior business decision-maker understand the corridor and its assumptions without a legal briefing?
2. Can litigation counsel defend every probability estimate to a skeptical colleague?
3. Is every legal proposition marked as VERIFIED or [VERIFY]?
4. Are any probability estimates stated with more confidence than the evidence supports?
5. Is the counterparty's BATNA modeled, or only assumed?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for offer mechanics, Part 36/Rule 68/UCPR offer rules in the forum
- Verify settlement confidentiality enforceability in the jurisdiction
- Locate comparable settlements or verdicts in similar disputes
- Check currency of statutory provisions (particularly tax treatment changes)
- Mark verified citations in the Glass Box: `VERIFIED (legalcode-mcp)`

**Without legalcode-mcp:**

- Mark all jurisdiction-specific procedural and tax references [VERIFY]
- Note: `legalcode_mcp: "Not connected"` in Glass Box
- Focus analysis on BATNA/WATNA modeling, corridor construction, and concession strategy
  (the quantitative framework is largely jurisdiction-agnostic)
- Flag all statutory procedure elements for counsel verification

---

## Output Format Template

Structure the settlement analysis deliverable as:

````markdown
# Settlement Negotiation Analysis — [Matter Name]

**Date**: [Date]
**Prepared by**: AI-assisted (legalcode-settlement-negotiation); counsel review required
**Side represented**: [Claimant / Defendant / Neutral]
**Governing law**: [Jurisdiction]
**Procedural forum**: [Court / Arbitral body]
**Procedural stage**: [Pre-suit / Discovery / Trial imminent]
**Negotiation objective**: [Establish corridor / Prepare opening / Evaluate offer / Playbook]

---

## 1. Executive Settlement Snapshot

| Element                                    | Value              | Confidence         |
| ------------------------------------------ | ------------------ | ------------------ |
| Your BATNA (risk-adjusted)                 | $[X]               | [0.XX — Level]     |
| Your WATNA (risk-adjusted)                 | $[X]               | [0.XX — Level]     |
| Counterparty BATNA (estimated)             | $[X]               | [0.XX — Level]     |
| Settlement floor (your MAS)                | $[X]               | [0.XX — Level]     |
| Settlement ceiling (counterparty MAS est.) | $[X]               | [0.XX — Level]     |
| **Settlement corridor**                    | **$[Low]–$[High]** | **[0.XX — Level]** |
| **Target settlement**                      | **$[Target]**      | **[0.XX — Level]** |

**ZOPA status**: [Exists — $[Width] wide / Does not exist — gap of $[Amount] / Uncertain]
**Opening position (recommended)**: $[Amount] — [Positional / Principled] approach
**Overall settlement recommendation**: [Settle / Continue litigation / Mediate / Other]

---

## 2. BATNA / WATNA Analysis

### Your BATNA

- **Best alternative**: [Describe litigation/arbitration/regulatory path]
- **Probability of achieving**: [0.XX — Level]
- **Expected outcome if achieved**: $[Amount]
- **Time to BATNA resolution**: [Months]
- **Expected cost to reach BATNA**: $[Amount]
- **Risk-adjusted BATNA value**: $[Amount] (net of costs)
- **Key execution risks**: [List]

### Your WATNA

- **Worst realistic outcome**: [Describe adverse judgment / costs / collateral]
- **Probability of WATNA**: [0.XX — Level]
- **Expected value if WATNA occurs**: $[Adverse amount]
- **Additional costs**: $[Legal spend + costs award]
- **Risk-adjusted WATNA value**: $[Amount]

### Counterparty BATNA (Estimated)

- **Their best alternative**: [Estimate]
- **Estimated probability**: [0.XX — confidence in estimate]
- **Key constraints they face**: [Financial / Authorization / Regulatory / Reputational]
- **Information gaps**: [What we do not know about their BATNA]

### ZOPA Analysis

- **Your MAS**: $[Minimum Acceptable Settlement]
- **Counterparty MAS (estimated)**: $[Maximum Acceptable Settlement]
- **ZOPA**: $[MAS gap] — [Exists / Does not exist / Uncertain]

---

## 3. Claim and Defense Inventory

| Claim / Defense | Party | Legal Basis | Damages Range | Liability Strength | Confidence |
| --------------- | ----- | ----------- | ------------- | ------------------ | ---------- |
| [Claim 1]       |       |             | $[Low-High]   | [High/Med/Low]     | [0.XX]     |

---

## 4. Settlement Corridor

| Scenario                | Opening | Target | Floor | Ceiling |
| ----------------------- | ------- | ------ | ----- | ------- |
| Optimistic              | $[O]    | $[T]   | $[F]  | $[C]    |
| Realistic (recommended) | $[O]    | $[T]   | $[F]  | $[C]    |
| Conservative            | $[O]    | $[T]   | $[F]  | $[C]    |

**Sensitivity table**: [See Step 7b analysis]

---

## 5. Leverage Point Timeline

| Event                  | Date   | Effect               | Recommended Action                 |
| ---------------------- | ------ | -------------------- | ---------------------------------- |
| [Discovery close-out]  | [Date] | [Impact on corridor] | [Hold / Move / Offer by this date] |
| [Expert report served] | [Date] | [Impact]             | [Action]                           |
| [Motion ruling]        | [Date] | [Impact]             | [Action]                           |
| [Trial date]           | [Date] | [Maximum urgency]    | [Reserve final move]               |

---

## 6. Concession Strategy

**Opening position**: $[Amount] (Approach: [Positional / Principled])
**Concession pattern**:

| Move             | Trigger                 | Amount | Cumulative Position | Notes                            |
| ---------------- | ----------------------- | ------ | ------------------- | -------------------------------- |
| Move 1 (Opening) | [First contact]         | $[X]   | $[Position]         | [Anchored to comparable verdict] |
| Move 2           | [Counterparty response] | $[X]   | $[Position]         | [Good-faith signal]              |
| Move 3           | [Discovery close-out]   | $[X]   | $[Position]         | [Diminishing concession]         |
| Move 4 (Final)   | [Trial-proximate]       | $[X]   | $[Position = floor] | [Signal finality]                |

---

## 7. Settlement Term Trade Matrix

| Term                   | Classification | Your Priority | Counterparty Priority | Trade Opportunity                 |
| ---------------------- | -------------- | ------------- | --------------------- | --------------------------------- |
| Payment amount         | [CORE]         | [High]        | [High]                | [Primary axis]                    |
| Confidentiality        | [TARGET]       | [Medium]      | [High]                | [Trade for amount]                |
| Admission of liability | [CORE]         | [High]        | [High]                | [Hard trade — may be uncrossable] |
| Payment timing         | [FLEXIBLE]     | [Low]         | [High]                | [Lump sum ↔ structured]           |
| Release breadth        | [FLEXIBLE]     | [Low]         | [High]                | [Broaden in exchange for payment] |
| Attorney's fees        | [FLEXIBLE]     | [Low-Medium]  | [Low-Medium]          | [Package trade]                   |
| [Other terms]          |                |               |                       |                                   |

**Recommended trade sequence**:

1. [First trade: offer on Term X in exchange for Y]
2. [Fallback: if blocked, move to Term Y for Z]
3. [Final package: full terms if monetary gap remains]

---

## 8. Non-Monetary Terms Analysis

### Release Scope

- **Recommended scope**: [All claims / Specific claims / Mutual]
- **Unknown claims**: [Waived with §1542 equivalent / Preserved / Not applicable]
- **Reservation of rights**: [Specify what is NOT released]
- **[JURISDICTION-SPECIFIC]**: [Apply local release requirements]

### Confidentiality

- **Recommended approach**: [Full / Terms-only / None]
- **Enforceability issues**: [Any jurisdiction-specific limits]
- **Permitted carve-outs**: [Tax, legal disclosure, regulatory]

---

## 9. Prioritization and Action Register

| Tier   | Action                                    | Owner               | Due                   | Expected Outcome                       |
| ------ | ----------------------------------------- | ------------------- | --------------------- | -------------------------------------- |
| Tier 1 | [Confirm walk-away threshold with client] | [GC / Counsel]      | [Before next session] | [Authorization clarity]                |
| Tier 1 | [Map insurance consent requirements]      | [Risk team]         | [Immediately]         | [Prevent post-agreement surprise]      |
| Tier 2 | [Research comparable verdicts]            | [Counsel]           | [Before first offer]  | [Anchor support]                       |
| Tier 2 | [Draft release language]                  | [Counsel]           | [Before term sheet]   | [Reduce drafting delay post-agreement] |
| Tier 3 | [Model structured payment alternative]    | [Finance / Counsel] | [Before mediation]    | [Expand ZOPA if monetary gap persists] |

---

## 10. Quality Verification

**Citation Quality Gates**: [PASS / NEEDS REVISION — specify gates failed]
**Self-Interrogation**: [PASS / REVISED — summary of changes]
**Confidence summary**: [Overall confidence in corridor and key assumptions]

---

## 11. Glass Box Audit Trail

```yaml
[Insert glass_box block per template above]
```
````

---

## 12. Recommended Next Steps

1. [Share corridor analysis with decision-makers for authorization confirmation]
2. [Schedule BATNA calibration session with litigation counsel]
3. [Identify mediator if mediation path preferred]
4. [Prepare opening position paper with comparable support]
5. [Map insurance consent process and timeline]

```

---

## Tax Implications — Settlement Proceeds

Tax treatment affects the net value of any settlement and must be factored into BATNA
calculations. This is jurisdiction-specific; advise the client to obtain independent tax
advice before finalizing terms.

**[JURISDICTION-SPECIFIC] Key principles:**

**United States (IRC §104):**
- Physical injury or sickness settlements: Excludable from gross income (IRC §104(a)(2))
- Punitive damages: Always taxable as ordinary income, even in physical injury cases [VERIFY]
- Emotional distress (non-physical): Taxable unless flowing from a physical injury [VERIFY]
- Employment discrimination (no physical injury): Fully taxable as ordinary income [VERIFY]
- Allocation in the agreement: The IRS looks to the "origin of the claim" — clear allocation
  between claim types is required and should reflect adversarial negotiation for IRS scrutiny

**United Kingdom (ITEPA 2003):**
- Personal injury settlements: Tax-free under ITEPA 2003 s.406 (psychiatric injury included;
  injury to feelings does not qualify) [VERIFY]
- Termination payments: £30,000 exemption applies to qualifying termination payments;
  *Mathur v HMRC* [2024] confirmed broad reading of "in connection with" termination [VERIFY]
- Lost earnings component: Fully taxable as income regardless of settlement framing [VERIFY]
- Interest element of awards: Taxable as income under s.369 ITTOIA 2005 [VERIFY]

**Australia (ITAA 1997):**
- Personal injury compensation: Generally non-assessable; s.118-37 ITAA 1997 exempts
  structured personal injury settlement payments from both income tax and CGT [VERIFY]
- Workers compensation lump sums (global settlement): Non-assessable non-exempt income [VERIFY]
- Employment discrimination — lost income component: Taxable; non-economic loss component:
  generally capital (not income), not assessable [VERIFY]
- GST: Compensation payments generally not subject to GST; payments including a property
  transfer component may attract GST on the supply element [VERIFY]

**Practice note:** When drafting settlement agreements, allocate amounts between claim types
explicitly and record the allocation as the result of adversarial bargaining. Misallocated
or unallocated amounts create tax uncertainty and IRS/HMRC/ATO scrutiny risk.

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace all [JURISDICTION-SPECIFIC] markers with verified local law
2. Replace all [VERIFY] tags with confirmed statutory or case law citations
3. Add jurisdiction-specific offer mechanics (Part 36 / Rule 68 / UCPR Offers)
4. Add jurisdiction-specific confidentiality limits and court approval requirements
5. Add tax treatment of settlement proceeds in the target jurisdiction
6. Add local ADR/mediation framework and accreditation requirements
7. Update the frontmatter name and description to reference the jurisdiction

**Suggested jurisdiction-specific variants to create:**
- `legalcode-settlement-negotiation-us` — Federal and state civil settlement (Rule 68,
  Rule 408, FLSA Cheeks doctrine, class settlement Rule 23(e))
- `legalcode-settlement-negotiation-ew` — England & Wales (Part 36, Calderbank,
  Tomlin Orders, CPR r.21 approvals)
- `legalcode-settlement-negotiation-au` — Australia (UCPR/FCR offers, NMAS, FCA s.33V)

---

## Provenance

Legalcode original skill created 2026-03-01. Created from scratch (Mode A) using:
- Reference standard: `skills/general/contracts/legalcode-contract-review/SKILL.md`
- Reference litigation skills: `skills/general/litigation/legalcode-early-case-assessment/SKILL.md`,
  `skills/general/litigation/legalcode-damages-calculation/SKILL.md`
- Structural analysis agent: Reviewed all three reference skills for workflow design,
  CLARIFY patterns, quality frameworks, and output template structure
- Legal research agent: Web-searched BATNA/WATNA/ZOPA methodology, Harvard Negotiation
  Project (Fisher & Ury "Getting to Yes"), asymmetric information in litigation models,
  time pressure research, anti-reliance provisions in settlement agreements, jurisdiction-
  specific settlement law (Rule 68/408/23(e) US; Part 36/Calderbank UK; UCPR/FCA AU)
- Frameworks adapted from Harvard Negotiation Project (Fisher, Ury & Patton), Landes-
  Posner-Gould asymmetric information model, and Legalcode quality framework standards
```
