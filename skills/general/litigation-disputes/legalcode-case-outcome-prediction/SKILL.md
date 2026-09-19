---
name: legalcode-case-outcome-prediction
description: Generate structured litigation outcome predictions using probabilistic analysis of legal
  merits, factual strength, procedural posture, judicial tendencies, and historical case data. Use when
  advising clients on case viability, evaluating settlement versus trial decisions, preparing for board
  or executive briefings, modeling expected value across resolution branches, or assessing litigation
  portfolio risk. Covers plaintiff and defendant perspectives across civil litigation, arbitration, and
  regulatory proceedings. Produces confidence-scored probability assessments with sensitivity analysis,
  outcome scenario trees, decision thresholds, and Glass Box audit trails. Jurisdiction-agnostic with
  [JURISDICTION-SPECIFIC] markers for US federal/state, England & Wales, Australia, EU member states,
  and common arbitration regimes.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Case Outcome Prediction

> **Disclaimer**: This skill provides a framework for AI-assisted litigation outcome
> prediction. It does not constitute legal advice, guarantee any outcome, or substitute
> for qualified legal counsel licensed in the relevant jurisdiction. Litigation outcomes
> are inherently uncertain and depend on factors that cannot be fully modeled, including
> judicial discretion, witness credibility at trial, jury composition, procedural rulings,
> and unforeseen evidence. Probability assessments are analytical frameworks based on
> available information, not actuarial predictions. Historical outcome data has inherent
> selection bias (settled cases are not reflected) and may not generalize to the instant
> matter. Any statutory, regulatory, or case law references cited from memory carry
> hallucination risk and MUST be verified against authoritative sources before reliance.
> This skill uses predictive modeling techniques that may be considered "automated
> decision-making" under certain regulations — confirm compliance with applicable AI
> governance requirements before use.

---

## Purpose and Scope

Use this skill to produce structured, defensible litigation outcome predictions that
support strategic decision-making across the litigation lifecycle: from initial case
assessment through trial preparation and settlement negotiations.

**Covers:**

- **Multi-factor outcome modeling**: Legal merits, factual strength, procedural posture, and external factors weighted and integrated
- **Scenario tree construction**: Win/lose/partial outcomes at each procedural stage with conditional probabilities
- **Probability calibration**: Historical base rates, jurisdiction-specific adjustments, case-specific modifiers
- **Decision threshold analysis**: When to settle, when to litigate, when to appeal
- **Expected value calculation**: Integrating outcome probability with damages and costs
- **Sensitivity analysis**: How changes in key assumptions affect the prediction
- **Judicial tendency assessment**: Forum-specific considerations and judicial track records (where available)
- **Comparative case analysis**: How similar cases resolved and what distinguishes this case
- **Confidence scoring**: Explicit quantification of prediction uncertainty
- **Bias and limitation disclosure**: Transparent about what the model cannot capture

**Does not:**

- Replace the judgment of experienced trial counsel on jury selection, witness demeanor, or courtroom dynamics
- Provide actuarial guarantees of outcomes
- Access real-time judicial analytics databases (relies on available information and general patterns)
- Account for corruption, judicial misconduct, or other anomalies
- Model criminal proceedings (different frameworks apply)
- Substitute for jurisdiction-specific legal advice

**Related skills:**

- `legalcode-litigation-risk-assessment` — Four-dimensional risk analysis feeding into outcome prediction
- `legalcode-early-case-assessment` — Pre-discovery merits and evidence evaluation
- `legalcode-summary-judgment-analysis` — Dispositive motion viability assessment
- `legalcode-settlement-negotiation` — BATNA/WATNA/ZOPA modeling using outcome predictions
- `legalcode-damages-calculation` — Granular damages quantification for expected value calculation
- `legalcode-appellate-brief-analysis` — Appeal success probability assessment

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the procedural forum, substantive
governing law, and appellate structure at the start of every prediction and localize
accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

**Procedural Framework:**

- Burden of proof and standard (preponderance vs. balance of probabilities vs. clear and convincing)
- Dispositive motion availability and success rates (motion to dismiss, summary judgment)
- Trial format (bench vs. jury; panel composition)
- Appellate structure and standard of review
- Time to trial and procedural complexity

**Outcome Distribution Factors:**

- Historical plaintiff win rates by claim type
- Settlement rates and timing patterns
- Damages distribution patterns (median vs. mean awards)
- Fee-shifting rules affecting expected value

**Decision-Maker Analysis:**

- Judicial track record data availability
- Jury demographics and tendencies (US jury trials)
- Arbitrator selection and institutional rules
- Specialized court or tribunal considerations

**[JURISDICTION-SPECIFIC] Reference anchors frequently needed:**

- **US Federal**: FRCP 12(b)(6), 56 success rates by circuit; Lex Machina / Westlaw Edge analytics (if accessible); Markman hearing outcomes in patent; class certification rates [VERIFY]
- **US State**: Varies significantly by state; plaintiff-friendly vs. defense-friendly reputations; venue selection implications [VERIFY]
- **England & Wales**: CPR Part 24 (summary judgment); Part 36 offers and costs consequences; Commercial Court outcomes; Technology and Construction Court patterns [VERIFY]
- **Australia**: Federal Court s.31A; proportionality requirements; costs-shifting; model litigant obligations for government [VERIFY]
- **EU**: CJEU preliminary reference likelihood; national court variability; Brussels I enforcement [VERIFY]
- **Arbitration**: ICC, LCIA, AAA/ICDR, SIAC statistics on duration, costs, and outcomes [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **CLARIFY**) at key decision points
where the answer materially changes the prediction methodology or output. The skill pauses
and asks when:

- The procedural stage or scope is unclear
- The prediction objective determines which outcome scenarios to model
- Key assumptions about liability probability or damages require input
- The user's decision threshold (e.g., settlement authority) affects the analysis framing

If the user has already provided the information, skip the question and proceed. For
batch or automated runs, proceed with stated defaults and mark assumptions explicitly.

---

## Workflow

### Step 1: Accept Case Input

Accept the case description in any of these formats:

- **Complaint/Defence**: Filed pleadings establishing claims and defenses
- **Case summary**: Narrative of dispute, parties, legal theories, and current posture
- **Prior assessments**: Existing ECA, litigation risk assessment, or outcome memo to update
- **Ruling or decision**: Post-motion or post-trial posture for appeal prediction
- **Portfolio entry**: Summary data for portfolio-level outcome modeling

**Minimum required information** to proceed:

1. Nature of claims/defenses (legal theories)
2. Procedural stage (pre-suit → complaint filed → discovery → trial approaching → post-judgment)
3. Forum and governing law
4. Parties and their relative resources
5. High-level factual summary

Prompt the user to supply missing elements before proceeding.

### Step 2: Gather Context

**CLARIFY** — Before beginning the prediction, ask these questions. Present as structured
options where possible. Skip any that the user has already answered.

1. **Prediction objective?**
   - Options: Case viability assessment (should we proceed?), Settlement vs. trial decision, Board/executive briefing, Expected value for budgeting/reserves, Appeal decision, Portfolio risk assessment, Full outcome analysis
   - Default: Full outcome analysis
   - _Why this matters_: Determines depth, scenario selection, and output format.

2. **Whose perspective?**
   - Options: Plaintiff/Claimant, Defendant/Respondent, Neutral evaluation (both sides), Third-party observer (insurer, investor, acquirer)
   - Default: Neutral evaluation (both sides)
   - _Why this matters_: Frames the prediction around the relevant decision points and risk tolerance.

3. **Procedural stage?**
   - Options: Pre-suit (demand/negotiation), Early litigation (complaint filed, pre-discovery), Mid-case (discovery ongoing), Late-case (discovery complete, trial approaching), Post-trial (judgment entered, appeal pending), Appellate (appeal briefed/argued)
   - Default: Mid-case
   - _Why this matters_: The outcome tree and relevant scenarios change dramatically by stage.

4. **Primary outcome of interest?**
   - Options: Liability only (will plaintiff prevail?), Damages only (if liable, how much?), Both liability and damages, Specific issue resolution (e.g., summary judgment, class certification), Time to resolution
   - Default: Both liability and damages
   - _Why this matters_: Focuses the prediction on the decision-relevant dimension.

5. **Comparative data availability?**
   - Options: I have access to judicial analytics (Lex Machina, Westlaw Edge, etc.), I can provide similar case outcomes, No comparative data — use general patterns, I want the skill to identify comparable cases
   - Default: No comparative data — use general patterns
   - _Why this matters_: Higher-quality comparative data enables better calibration but may not be available.

6. **Risk tolerance for decision threshold?**
   - Options: Conservative (avoid adverse outcomes; settle if >30% loss probability), Balanced (weigh EV; settle if EV-negative), Aggressive (litigate unless >70% loss probability), Specify custom threshold
   - Default: Balanced
   - _Why this matters_: The recommendation changes based on the user's risk appetite.

If the user provides partial context, proceed with stated defaults and **explicitly flag
assumptions**: e.g., "Proceeding with plaintiff perspective, mid-case stage, full
liability and damages prediction — adjust if incorrect."

### Step 3: Load Prediction Configuration

Check whether the organization has a litigation prediction playbook in local settings
(e.g., `legal.local.md`, `litigation-playbook.md`, or similar configuration).

A prediction playbook may define:

- **Base rate sources**: Which databases or historical data to reference
- **Confidence thresholds**: When to flag predictions as "too uncertain to rely on"
- **Settlement authority levels**: Dollar thresholds for escalation
- **Risk weighting preferences**: How to weight legal vs. factual vs. procedural factors
- **Disclosure requirements**: What must be included in board-level reports

**If no playbook is configured:**

**CLARIFY** — Inform the user and ask:

- **Option A: Proceed with academic base rates and general patterns** — Use published outcome studies and general litigation statistics. Label: "Based on general statistical patterns — not organization-specific calibration."
- **Option B: Provide comparative cases now** — Supply 3-5 similar cases and their outcomes for calibration.
- **Option C: Conservative defaults** — Use conservative assumptions (higher uncertainty ranges, lower confidence scores).

### Step 4: Gather Jurisdiction-Relevant Authority and Base Rates

Identify the forum, governing law, and claim types. Then gather:

**Using legalcode-mcp (if connected):**

1. Relevant statutes defining claim elements and defenses
2. Leading cases on burden of proof and standard for each claim type
3. Dispositive motion standards and recent rulings
4. Damages frameworks and recent award ranges
5. Procedural rules affecting timing and trial format

**Outcome statistics (if available):**

1. Win rates by claim type in this forum
2. Summary judgment grant rates
3. Median/mean damages awards
4. Settlement rates and timing
5. Appeal success rates

Save results to a local temporary reference file:

```markdown
# Outcome Prediction Authority — [Matter Name]

## Date: [date]

## Forum: [Court/Tribunal]

## Governing Law: [Jurisdiction]

### Claim Elements and Standards

- [Claim type]: [Elements, burden, leading authority] — VERIFIED (legalcode-mcp) or [VERIFY]

### Historical Outcome Data

- Plaintiff win rate for [claim type]: [X]% (source: [cite]) [VERIFY]
- Summary judgment grant rate: [X]% (source: [cite]) [VERIFY]
- Median damages award: $[X] (source: [cite]) [VERIFY]

### Procedural Benchmarks

- Average time to trial: [X] months (source: [cite]) [VERIFY]
- Settlement rate: [X]% (source: [cite]) [VERIFY]
```

**If legalcode-mcp is not connected:**

- Proceed with general legal knowledge and publicly available statistics
- Mark all statistical claims with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — statistical claims require verification"`

### Step 5: Assess Legal Merit Probability

Build an element-level merit assessment for each claim and primary defense. This forms the
legal foundation of the outcome prediction.

**5a. Claim Viability Scoring**

For each cause of action:

| Element     | Required Showing | Evidence Quality          | Probability Met | Confidence  | Notes          |
| ----------- | ---------------- | ------------------------- | --------------- | ----------- | -------------- |
| [Element 1] | [Standard]       | STRONG/ADEQUATE/THIN/WEAK | [0.00-1.00]     | [0.00-1.00] | [Risk factors] |
| [Element 2] | [Standard]       | [Quality]                 | [Prob]          | [Conf]      | [Notes]        |

**Claim-level probability** = Product of element probabilities (assuming independence) OR
weighted combination (if elements are correlated).

**5b. Defense Viability Scoring**

For each defense:

| Defense     | Legal Basis         | Evidence Quality | Probability Success | Confidence  | Impact if Successful                              |
| ----------- | ------------------- | ---------------- | ------------------- | ----------- | ------------------------------------------------- |
| [Defense 1] | [Statute/principle] | [Quality]        | [0.00-1.00]         | [0.00-1.00] | Full bar / Partial mitigation / Damages reduction |

**5c. Net Liability Probability**

Integrate claim and defense probabilities:

```
P(Liability) = P(All claim elements met) × (1 - P(Complete defense success))

Where multiple claims exist:
P(Some liability) = 1 - Product of (1 - P(Liability on claim i)) for all claims i
```

**Legal Merit Classification:**

| Classification  | Probability | Meaning                                 |
| --------------- | ----------- | --------------------------------------- |
| **STRONG**      | 0.75-1.00   | High likelihood of prevailing on merits |
| **VIABLE**      | 0.55-0.74   | More likely than not to prevail         |
| **CONTESTED**   | 0.45-0.54   | Genuine toss-up                         |
| **CHALLENGING** | 0.25-0.44   | Uphill battle but not hopeless          |
| **WEAK**        | 0.00-0.24   | Low likelihood of success               |

### Step 6: Assess Factual Strength Probability

Factual strength affects both liability probability and credibility at trial.

**6a. Key Fact Assessment**

| Fact Issue        | Evidence        | Source Quality | Contradiction Risk | Probability Proved | Weight                      |
| ----------------- | --------------- | -------------- | ------------------ | ------------------ | --------------------------- |
| [Critical fact 1] | [Evidence type] | HIGH/MED/LOW   | LOW/MED/HIGH       | [0.00-1.00]        | CRITICAL/IMPORTANT/MARGINAL |
| [Critical fact 2] | [Evidence]      | [Quality]      | [Risk]             | [Prob]             | [Weight]                    |

**6b. Witness Credibility Assessment**

| Witness | Role        | Importance         | Credibility  | Impeachment Risk | Net Impact |
| ------- | ----------- | ------------------ | ------------ | ---------------- | ---------- |
| [Name]  | Fact/Expert | CRITICAL/IMPORTANT | HIGH/MED/LOW | LOW/MED/HIGH     | +/0/-      |

**6c. Factual Strength Score**

Composite score (1-5 scale):

- Evidence quality: [Score] × 30%
- Witness strength: [Score] × 25%
- Document coverage: [Score] × 25%
- Expert support: [Score] × 20%
  = **Total: [Weighted composite]**

| Classification | Score   | Impact on Outcome Probability |
| -------------- | ------- | ----------------------------- |
| **STRONG**     | 4.0-5.0 | +10-20% to base probability   |
| **ADEQUATE**   | 3.0-3.9 | No material adjustment        |
| **THIN**       | 2.0-2.9 | -10-20% from base probability |
| **WEAK**       | 1.0-1.9 | -20-40% from base probability |

### Step 7: Assess Procedural and Forum Factors

Procedural posture and forum characteristics materially affect outcomes.

**7a. Dispositive Motion Risk**

| Motion Type         | Moving Party | Probability of Grant | Timing  | Impact if Granted                               |
| ------------------- | ------------ | -------------------- | ------- | ----------------------------------------------- |
| Motion to dismiss   | [Party]      | [0.00-1.00]          | [Stage] | Case ends / Claim dismissed / Amendment allowed |
| Summary judgment    | [Party]      | [0.00-1.00]          | [Stage] | Full judgment / Partial / Denied                |
| Class certification | [Party]      | [0.00-1.00]          | [Stage] | Certified / Denied                              |

**7b. Forum Factor Assessment**

[JURISDICTION-SPECIFIC] Evaluate forum-specific factors:

| Factor                  | Assessment                                        | Impact on Prediction     | Confidence  |
| ----------------------- | ------------------------------------------------- | ------------------------ | ----------- |
| Judge track record      | [Plaintiff-leaning / Neutral / Defense-leaning]   | +/-[X]%                  | [0.00-1.00] |
| Jury vs. bench trial    | [Which expected]                                  | [Impact description]     | [0.00-1.00] |
| Local rules complexity  | [Simple / Moderate / Complex]                     | [Timeline / cost impact] | [0.00-1.00] |
| Venue reputation        | [Plaintiff-friendly / Neutral / Defense-friendly] | +/-[X]%                  | [0.00-1.00] |
| Appeal risk/opportunity | [Likelihood, standard of review]                  | [Impact]                 | [0.00-1.00] |

**7c. Procedural Stage Adjustment**

The current stage affects both probability precision and the relevance of different factors:

| Stage            | Key Uncertainty Drivers                    | Probability Precision | Dominant Factors                 |
| ---------------- | ------------------------------------------ | --------------------- | -------------------------------- |
| Pre-suit         | Unknown evidence, unknown defense strategy | Wide (0.3-0.7 base)   | Legal merit, industry patterns   |
| Early litigation | Pleading sufficiency, initial discovery    | Moderate (0.2-0.8)    | MTD survival, initial evidence   |
| Mid-case         | Discovery outcomes, expert strength        | Narrowing (0.15-0.85) | Evidence quality, SJ viability   |
| Late-case        | Full record, known trial issues            | Narrow (0.1-0.9)      | Trial factors, judicial rulings  |
| Appellate        | Standard of review, record fixed           | Narrow (0.1-0.9)      | Legal error, abuse of discretion |

### Step 8: Build Outcome Scenario Tree

Construct a decision tree showing possible outcomes at each procedural branch point.

**8a. Scenario Tree Structure**

```
[Current Stage]
├── Dispositive Motion Phase
│   ├── Motion Granted (P = [X])
│   │   └── [Outcome: Case ends / Claim dismissed / Appeal]
│   └── Motion Denied (P = [1-X])
│       └── [Continue to next phase]
├── Settlement Phase
│   ├── Settlement (P = [Y])
│   │   └── [Outcome: Terms depend on negotiation]
│   └── No Settlement (P = [1-Y])
│       └── [Continue to trial]
├── Trial Phase
│   ├── Plaintiff Win (P = [W])
│   │   ├── Full Liability (P = [W1] | Win)
│   │   │   └── Damages: [Range]
│   │   └── Partial Liability (P = [W2] | Win)
│   │       └── Damages: [Range]
│   ├── Defense Win (P = [1-W])
│   │   └── [Outcome: Judgment for defendant]
│   └── Mistrial / Hung Jury (P = [M])
│       └── [Retry / Settlement]
└── Appeal Phase
    ├── Affirm (P = [A])
    ├── Reverse (P = [R])
    └── Remand (P = [1-A-R])
```

**8b. Key Probabilities Summary**

| Scenario                       | Probability | Confidence | Key Drivers |
| ------------------------------ | ----------- | ---------- | ----------- |
| Motion to dismiss granted      | [P]         | [C]        | [Factors]   |
| Summary judgment (plaintiff)   | [P]         | [C]        | [Factors]   |
| Summary judgment (defendant)   | [P]         | [C]        | [Factors]   |
| Settlement pre-trial           | [P]         | [C]        | [Factors]   |
| Plaintiff win at trial         | [P]         | [C]        | [Factors]   |
| Defendant win at trial         | [P]         | [C]        | [Factors]   |
| Appeal success (if applicable) | [P]         | [C]        | [Factors]   |

### Step 9: Calculate Expected Value

Integrate probability estimates with damages/cost projections.

**9a. Damages Distribution**

| Scenario              | Probability | Damages (P10) | Damages (P50) | Damages (P90) |
| --------------------- | ----------- | ------------- | ------------- | ------------- |
| Full plaintiff win    | [P]         | $[Low]        | $[Med]        | $[High]       |
| Partial plaintiff win | [P]         | $[Low]        | $[Med]        | $[High]       |
| Defense win           | [P]         | $0            | $0            | $0            |

**9b. Cost Projection**

| Phase             | Plaintiff Costs | Defendant Costs | Fee-Shifting Impact |
| ----------------- | --------------- | --------------- | ------------------- |
| Through discovery | $[Range]        | $[Range]        | [Rule]              |
| Through trial     | $[Range]        | $[Range]        | [Rule]              |
| Through appeal    | $[Range]        | $[Range]        | [Rule]              |

**9c. Expected Value Calculation**

For each party:

```
EV = Sum over all scenarios of: P(scenario) × [Damages(scenario) - Costs(scenario)]

EV (Plaintiff) = P(Win) × E[Damages | Win] - Costs - P(Lose) × [Fee-shifting exposure if applicable]
EV (Defendant) = -P(Plaintiff Win) × E[Damages | Win] - Costs - [Counterclaim EV if applicable]
```

| Metric                       | Plaintiff | Defendant |
| ---------------------------- | --------- | --------- |
| Expected value (base case)   | $[X]      | $[X]      |
| Expected value (optimistic)  | $[X]      | $[X]      |
| Expected value (pessimistic) | $[X]      | $[X]      |
| Breakeven settlement value   | $[X]      | $[X]      |

### Step 10: Sensitivity Analysis

Identify which assumptions most affect the prediction and model their impact.

**10a. Key Assumption Sensitivity**

| Assumption        | Base Value | Range Tested   | Impact on EV | Sensitivity  |
| ----------------- | ---------- | -------------- | ------------ | ------------ |
| P(Liability)      | [X]%       | [Low]-[High]%  | $[Delta]     | HIGH/MED/LOW |
| Damages if liable | $[X]       | $[Low]-$[High] | $[Delta]     | HIGH/MED/LOW |
| P(SJ granted)     | [X]%       | [Low]-[High]%  | $[Delta]     | HIGH/MED/LOW |
| P(Settlement)     | [X]%       | [Low]-[High]%  | $[Delta]     | HIGH/MED/LOW |
| Cost to trial     | $[X]       | $[Low]-$[High] | $[Delta]     | HIGH/MED/LOW |

**10b. Tornado Diagram Interpretation**

Rank assumptions by sensitivity (highest impact first). The top 3-5 drivers should receive
the most attention in evidence gathering, legal research, and strategic planning.

**10c. Scenario Stress Testing**

| Stress Scenario              | Description | P(Liability) | EV Change | Recommendation |
| ---------------------------- | ----------- | ------------ | --------- | -------------- |
| Key witness unavailable      | [Impact]    | [P]          | $[Delta]  | [Action]       |
| Adverse SJ ruling            | [Impact]    | [P]          | $[Delta]  | [Action]       |
| Unfavorable expert exclusion | [Impact]    | [P]          | $[Delta]  | [Action]       |
| Fee-shifting invoked         | [Impact]    | [P]          | $[Delta]  | [Action]       |

### Step 11: Generate Decision Recommendations

Based on the outcome prediction and the user's stated risk tolerance, provide actionable
recommendations.

**11a. Decision Threshold Analysis**

| Decision Point          | Threshold                                 | Current Assessment | Recommendation |
| ----------------------- | ----------------------------------------- | ------------------ | -------------- |
| File suit               | >40% win probability and EV-positive      | [Assessment]       | [Recommend]    |
| Continue litigation     | >30% win probability or EV-positive       | [Assessment]       | [Recommend]    |
| Accept settlement at $X | EV of settlement > EV of trial            | [Assessment]       | [Recommend]    |
| Move for SJ             | >50% grant probability                    | [Assessment]       | [Recommend]    |
| Appeal                  | >40% reversal probability and EV-positive | [Assessment]       | [Recommend]    |

**11b. Strategic Recommendations**

Provide 3-5 strategic recommendations based on the prediction:

1. **[High priority]**: [Recommendation with rationale tied to outcome drivers]
2. **[Medium priority]**: [Recommendation]
3. **[Medium priority]**: [Recommendation]
4. **[Ongoing]**: [Recommendation for information gathering that would improve prediction]
5. **[Contingent]**: [If X happens, then Y recommendation]

**11c. Information Value Assessment**

Identify what additional information would most improve the prediction:

| Information                 | Current Uncertainty | Potential Impact        | Cost/Effort to Obtain | Priority |
| --------------------------- | ------------------- | ----------------------- | --------------------- | -------- |
| [Expert opinion on X]       | HIGH                | +/-[X]% on P(Liability) | $[Cost]               | HIGH     |
| [Additional discovery on Y] | MED                 | +/-[X]% on damages      | $[Cost]               | MED      |
| [Judicial analytics data]   | MED                 | Better calibration      | $[Cost]               | MED      |

### Step 12: Quality Verification

Before delivering the prediction, run quality assurance checks.

**12a. Coherence Check**

- Do all probabilities sum appropriately at each branch? (Mutually exclusive events sum to 1)
- Is the overall P(Plaintiff Win) consistent with the element-level analysis?
- Does the EV calculation correctly integrate probabilities and values?
- Are confidence intervals appropriately wide given the procedural stage?

**12b. Base Rate Anchoring**

- Is the prediction anchored to a credible base rate?
- Does the prediction deviate from the base rate? If so, is the deviation justified by case-specific factors?
- Flag if deviation exceeds +/-30% from base rate without explicit justification.

**12c. Bias Check**

Review for common prediction biases:

- **Overconfidence**: Are confidence intervals too narrow?
- **Anchoring**: Is the prediction over-reliant on a single data point?
- **Availability**: Is the prediction influenced by recent high-profile cases that may not be representative?
- **Confirmation**: Has contrary evidence been adequately weighted?
- **Base rate neglect**: Have historical outcome rates been considered?

---

## Risk Classification (Outcome-Specific)

Classify the overall case outcome risk:

| Classification  | Criteria                                        | Recommended Posture                                               |
| --------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| **FAVORABLE**   | >70% win probability, EV strongly positive      | Pursue aggressively; consider acceleration                        |
| **BALANCED**    | 45-70% win probability, EV moderately positive  | Litigate with settlement optionality                              |
| **UNCERTAIN**   | 35-55% win probability, EV near zero            | High-value information gathering; active settlement exploration   |
| **UNFAVORABLE** | 20-35% win probability, EV negative             | Settle if reasonable terms available; damage limitation           |
| **ADVERSE**     | <20% win probability, EV significantly negative | Exit strategy; settlement at defensive terms; voluntary dismissal |

---

## Actionable Output Per Scenario

For each key scenario in the outcome tree, provide:

| Scenario     | Probability | Confidence | Damages Range | Cost to Reach | EV    | Action           |
| ------------ | ----------- | ---------- | ------------- | ------------- | ----- | ---------------- |
| [Scenario 1] | [P]         | [C]        | $[Range]      | $[Cost]       | $[EV] | [Recommendation] |
| [Scenario 2] | [P]         | [C]        | $[Range]      | $[Cost]       | $[EV] | [Recommendation] |

---

## Prioritization Framework

Use these tiers for prediction-driven actions:

| Tier       | Label     | Criteria                                                                       | Timeline   |
| ---------- | --------- | ------------------------------------------------------------------------------ | ---------- |
| **Tier 1** | Immediate | Decisions needed before next procedural deadline; high-sensitivity assumptions | 0-72 hours |
| **Tier 2** | Near-term | Evidence gathering to reduce uncertainty; settlement exploration               | 1-4 weeks  |
| **Tier 3** | Strategic | Long-term positioning; portfolio implications; precedent considerations        | 1+ months  |

---

## Citation Quality Gates

Before delivery, run these gates on every statistical claim and legal proposition:

| Gate           | Rule                                                     | Fail Action              |
| -------------- | -------------------------------------------------------- | ------------------------ |
| **Source**     | Every statistical claim cites a source or marks [VERIFY] | Add source or mark       |
| **Format**     | Citations use recognizable format                        | Normalize                |
| **Currency**   | Statistics are from recent periods (ideally <5 years)    | Flag if stale            |
| **Relevance**  | Base rates are from comparable cases/forums              | Flag mismatch            |
| **Confidence** | Uncertainty is explicitly stated                         | Add confidence qualifier |

---

## Self-Interrogation for High-Stakes Predictions

For any prediction that would drive a decision threshold (file/don't file, settle/litigate,
appeal/accept), apply this 3-pass review:

**Pass 1 — Probability Calibration**:

- Is this probability consistent with historical base rates?
- What would a prediction market or seasoned trial lawyer estimate?
- Am I overweighting recent or salient information?

**Pass 2 — Completeness**:

- Have all material claims and defenses been evaluated?
- Are there procedural pathways I haven't modeled?
- What evidence am I missing that could shift the prediction?

**Pass 3 — Adversarial Challenge**:

- What would opposing counsel argue about this prediction?
- What is the strongest case for a different outcome?
- If I had to defend this prediction in court, what would be my weakest points?

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                      | Action                              |
| ------------ | --------- | -------------------------------------------- | ----------------------------------- |
| **Definite** | 0.95-1.00 | Outcome is near-certain (rare in litigation) | Present with minimal caveats        |
| **High**     | 0.80-0.94 | Strong evidentiary and legal basis           | Present with brief uncertainty note |
| **Probable** | 0.60-0.79 | More likely than not but genuine uncertainty | Present with explicit reasoning     |
| **Possible** | 0.40-0.59 | Could go either way                          | Flag as uncertain; widen ranges     |
| **Unlikely** | 0.00-0.39 | Unlikely outcome but non-zero                | Present as contingency scenario     |

**Meta-confidence** — Confidence in the confidence:

- **Calibrated**: Prediction based on substantial comparable data and thorough analysis
- **Estimated**: Reasonable estimate but limited comparable data
- **Speculative**: High uncertainty; treat ranges as indicative only

---

## Glass Box Audit Trail

Every outcome prediction MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-case-outcome-prediction"
  matter: "[Matter name/identifier]"
  forum: "[Court/Tribunal]"
  governing_law: "[Jurisdiction]"
  claims_analyzed: "[List]"
  defenses_analyzed: "[List]"
  procedural_stage: "[Stage]"
  prediction_objective: "[Objective from Step 2]"
  user_side: "[Plaintiff/Defendant/Neutral]"
  base_rate_source: "[Source or 'General patterns']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  key_probabilities:
    liability: "[P] (confidence: [C])"
    plaintiff_win_at_trial: "[P] (confidence: [C])"
    settlement_pre_trial: "[P] (confidence: [C])"
  expected_value_plaintiff: "$[X] (range: $[Low] to $[High])"
  expected_value_defendant: "$[X] (range: $[Low] to $[High])"
  sensitivity_drivers:
    - "[Driver 1]: [Impact]"
    - "[Driver 2]: [Impact]"
  citations_verified: "[count VERIFIED] / [count UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  prediction_confidence: "HIGH / MEDIUM / LOW — [rationale]"
  meta_confidence: "Calibrated / Estimated / Speculative"
  key_assumptions:
    - "[Assumption 1]"
    - "[Assumption 2]"
  limitations:
    - "[Limitation 1]"
    - "[Limitation 2]"
  bias_check: "PASS / FLAGS: [list any biases identified]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in case outcome prediction:

1. **Point estimates without ranges** — A prediction of "65% win probability" without confidence intervals or sensitivity analysis is false precision. Always provide ranges.

2. **Base rate neglect** — Ignoring historical outcome rates for similar cases and over-relying on case-specific analysis. Start with the base rate and adjust.

3. **Outcome determinism** — Treating litigation outcomes as deterministic when they are inherently probabilistic. Even "slam dunk" cases sometimes lose.

4. **Anchoring on pleadings** — Over-weighting the allegations as stated rather than the evidence available to prove them.

5. **Single-scenario modeling** — Predicting only "win or lose" without modeling partial outcomes, settlement scenarios, and procedural branches.

6. **Ignoring settlement** — Most civil cases settle. A prediction that doesn't model settlement probability is incomplete.

7. **Overconfidence in early stages** — Providing precise probability estimates before discovery when the evidence base is speculative.

8. **Static predictions** — Treating the prediction as final rather than updatable as new information emerges. Build in update triggers.

9. **Conflating probability and confidence** — A 60% win probability with HIGH confidence is different from 60% with LOW confidence. Both dimensions matter.

10. **Ignoring costs** — Win probability without expected value calculation ignores the fact that a "win" with massive legal costs may be a net loss.

11. **Assuming rationality** — Assuming opposing party will settle when it's EV-rational. Parties litigate for non-economic reasons (principle, reputation, deterrence).

12. **Forum blindness** — Applying general statistics to a specific forum without adjusting for known judicial tendencies or venue characteristics.

13. **Expert overconfidence** — Over-weighting the user's (or counsel's) confidence in the case without testing assumptions against base rates.

14. **Ignoring appellate risk** — A trial win with high reversal probability on appeal has lower net value than the face outcome suggests.

15. **Selection bias in comparisons** — Using win rates from litigated cases without accounting for the fact that settled cases (often the strongest/weakest) are excluded.

---

## Writing Standards

Apply plain-language discipline to all output:

**For predictions:**

- State probability ranges, not false precision
- Use active voice: "Plaintiff has a 60% chance of prevailing" not "There is a 60% probability that the plaintiff may prevail"
- Separate what is known from what is assumed
- Quantify uncertainty explicitly
- Avoid hedge words that obscure rather than clarify ("somewhat likely," "may potentially")

**For recommendations:**

- Tie to specific probability thresholds
- State what would change the recommendation
- Provide actionable next steps

**Quality gates before delivery:**

1. Can a non-lawyer decision-maker understand the key probabilities and recommendation?
2. Is every statistical claim sourced or flagged [VERIFY]?
3. Are all assumptions explicit?
4. Could the prediction be defended in a board meeting?
5. Would updating the prediction after new evidence be straightforward?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** for legal research and verification.

**With legalcode-mcp connected:**

- Verify claim elements and standards for the relevant jurisdiction
- Check for recent case law that might affect outcome probabilities
- Validate damages frameworks and award ranges
- Confirm procedural rules and deadlines
- Mark verified authority as VERIFIED in the audit trail

**Without legalcode-mcp:**

- Proceed with general legal knowledge
- Mark all legal and statistical claims with [VERIFY]
- Note: `legalcode_mcp: "Not connected — legal propositions require independent verification"`
- Focus on structural analysis and relative probability assessment rather than absolute calibration

**With judicial analytics tools (Lex Machina, Westlaw Edge, etc.):**

- Integrate forum-specific outcome statistics
- Incorporate judge-specific ruling patterns
- Use comparable case outcomes for calibration
- Note data source in Glass Box

**Without judicial analytics:**

- Use published academic studies and general statistics
- Widen confidence intervals appropriately
- Note limitation in Glass Box

---

## Output Format Template

Structure the final deliverable as:

````markdown
# Case Outcome Prediction — [Matter Name]

## 1. Executive Summary

**Matter**: [Description]
**Parties**: [Plaintiff vs. Defendant]
**Forum**: [Court/Tribunal]
**Governing Law**: [Jurisdiction]
**Procedural Stage**: [Stage]
**Prediction Date**: [Date]

### Key Findings

- **Overall Outcome Probability**: [X]% chance of [Party] prevailing (confidence: [Level])
- **Expected Value**: Plaintiff: $[X] | Defendant: $[X]
- **Recommended Posture**: [FAVORABLE / BALANCED / UNCERTAIN / UNFAVORABLE / ADVERSE]
- **Primary Recommendation**: [One-line recommendation]

---

## 2. Probability Assessment

### Liability Analysis

| Claim/Defense        | Probability | Confidence | Key Drivers |
| -------------------- | ----------- | ---------- | ----------- |
| [Claim 1]            | [P]%        | [C]        | [Drivers]   |
| [Defense 1]          | [P]%        | [C]        | [Drivers]   |
| **Net P(Liability)** | **[P]%**    | **[C]**    | —           |

### Outcome Scenario Summary

| Scenario           | Probability | Damages Range | EV Contribution |
| ------------------ | ----------- | ------------- | --------------- |
| Full plaintiff win | [P]%        | $[Range]      | $[EV]           |
| Partial win        | [P]%        | $[Range]      | $[EV]           |
| Defense win        | [P]%        | $0            | $[EV]           |
| Settlement         | [P]%        | $[Range]      | $[EV]           |

---

## 3. Outcome Scenario Tree

[Visual or textual representation of the decision tree with probabilities at each branch]

---

## 4. Expected Value Analysis

| Party     | EV (Pessimistic) | EV (Base) | EV (Optimistic) | Breakeven Settlement |
| --------- | ---------------- | --------- | --------------- | -------------------- |
| Plaintiff | $[X]             | $[X]      | $[X]            | $[X]                 |
| Defendant | $[X]             | $[X]      | $[X]            | $[X]                 |

---

## 5. Sensitivity Analysis

### Key Drivers (Ranked by Impact)

1. [Driver 1]: +/-[X]% impact on EV
2. [Driver 2]: +/-[X]% impact on EV
3. [Driver 3]: +/-[X]% impact on EV

### Stress Scenarios

| Scenario     | Impact        | Revised EV | Recommendation |
| ------------ | ------------- | ---------- | -------------- |
| [Scenario 1] | [Description] | $[X]       | [Action]       |
| [Scenario 2] | [Description] | $[X]       | [Action]       |

---

## 6. Decision Recommendations

### Decision Threshold Analysis

| Decision     | Threshold   | Current      | Recommendation |
| ------------ | ----------- | ------------ | -------------- |
| [Decision 1] | [Threshold] | [Assessment] | [Recommend]    |
| [Decision 2] | [Threshold] | [Assessment] | [Recommend]    |

### Strategic Actions

1. **[Priority]**: [Action with rationale]
2. **[Priority]**: [Action]
3. **[Priority]**: [Action]

### Information Value Assessment

| Information Gap | Impact   | Priority   |
| --------------- | -------- | ---------- |
| [Gap 1]         | [Impact] | [Priority] |
| [Gap 2]         | [Impact] | [Priority] |

---

## 7. Methodology and Limitations

### Approach

[Brief description of prediction methodology]

### Key Assumptions

- [Assumption 1]
- [Assumption 2]

### Limitations

- [Limitation 1]
- [Limitation 2]

### Update Triggers

- [Event that would trigger prediction update]
- [Event that would trigger prediction update]

---

## 8. Glass Box Audit Trail

```yaml
[Full Glass Box YAML block]
```
````

```

---

## Localization Notes

This skill is jurisdiction-agnostic. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local statistics and patterns
2. Add forum-specific judicial analytics integration
3. Incorporate local procedural rules and timing patterns
4. Add jurisdiction-specific anti-patterns (e.g., German bifurcation, UK Part 36)
5. Update base rate sources to jurisdiction-specific data
6. Add local language terminology where appropriate

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining probabilistic litigation
modeling, expected value calculation, decision analysis frameworks, sensitivity analysis,
and Bayesian updating principles into a structured case outcome prediction skill.
Incorporates best practices from litigation analytics, legal decision science, and risk
assessment methodologies. Quality frameworks (Citation Gates, Self-Interrogation,
Confidence Scoring, Glass Box) adopted from the legalcode-contract-review reference
standard.
```
