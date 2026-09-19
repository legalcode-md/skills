---
name: legalcode-litigation-risk-assessment
description: Evaluate litigation risk across four dimensions — legal merit, factual strength, damages
  exposure, and reputational/strategic risk — to produce risk matrices with confidence-weighted probability
  assessments, cost-benefit analysis across three resolution branches (litigate, settle, mediate), and
  strategic recommendations. Use when deciding whether to file or defend a claim, re-evaluating litigation
  posture at a case milestone, advising a board or executive team on litigation exposure, preparing for
  settlement negotiations, or building a litigation budget with risk-adjusted spend scenarios. Supports
  pre-litigation (demand letter stage), early litigation (pre-discovery), mid-case (post-discovery), and
  late-case (trial approaching) assessment phases. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers for US federal/state, England & Wales, Australia, and EU commercial courts.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Litigation Risk Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted litigation risk assessment
> in civil disputes. It does not constitute legal advice, litigation strategy, or a substitute
> for qualified legal counsel licensed in the relevant jurisdiction. Risk assessments,
> probability estimates, damages ranges, and strategic recommendations produced by this skill
> are analytical frameworks, not binding representations or professional opinions. Litigation
> outcomes are inherently uncertain; no risk model can guarantee accuracy. Laws, procedural
> rules, and case law change; verify current applicability before relying on any provision
> described here. Statutory and case law references cited from memory carry hallucination
> risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

Use this skill to produce a structured, defensible four-dimensional litigation risk
assessment that supports go/no-go decisions, settlement posture, board-level reporting,
and litigation budget management across the full lifecycle of a civil dispute.

**Covers:**

- Legal merit assessment: element-by-element claim and defense analysis, burden of proof, threshold issues
- Factual strength scoring: evidence quality, witness credibility, document coverage, discovery risk
- Damages exposure modeling: expected value ranges, treble/punitive multipliers, fee-shifting, mitigation
- Reputational and strategic risk: media profile, precedent sensitivity, leadership credibility, collateral harm
- Integrated four-dimensional risk matrix with confidence-weighted composite score
- Three-branch cost-benefit analysis: litigate to judgment, settle now, mediate
- Sensitivity analysis on key assumptions (probability, damages, costs)
- Strategic recommendation with conditional triggers and escalation paths
- Pre-litigation through late-case reassessment workflows
- Jurisdiction-agnostic baseline with US/UK/AU/EU localization markers

**Does not:**

- Draft pleadings, demand letters, or settlement agreements (see `legalcode-complaint-drafter`, `legalcode-settlement-negotiation`)
- Perform detailed damages calculation (see `legalcode-damages-calculation` for granular methodology)
- Replace Early Case Assessment (see `legalcode-early-case-assessment` for element-level merits depth)
- Provide legal advice or substitute for licensed counsel
- Cover criminal proceedings, regulatory enforcement actions (different frameworks), or arbitration-specific procedures

**Related skills:**

- `legalcode-early-case-assessment` — Deep element-level merits analysis; feeds into Step 5 of this skill
- `legalcode-damages-calculation` — Granular damages quantification; feeds into Step 7
- `legalcode-settlement-negotiation` — BATNA/WATNA/ZOPA corridor modeling; consumes output of this skill
- `legalcode-legal-risk-assessment` — Enterprise-wide risk context; use for portfolio or board-level framing
- `legalcode-privilege-review` — Protecting this assessment as work product

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the substantive governing law,
the procedural forum, and the court system at the start of every assessment and localize
accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

**Legal merits:**

- Burden and standard of proof (civil preponderance vs. balance of probabilities vs. clear and convincing)
- Elements required to establish each cause of action under the governing law
- Available defenses and their legal elements
- Threshold issues (standing, limitation periods, forum jurisdiction)

**Damages:**

- Compensatory damages scope and methodology (foreseeability, causation, mitigation duty)
- Punitive or exemplary damages availability and constitutional/statutory limits
- Treble damages under specific statutes (antitrust, trade secrets, IP)
- Fee-shifting rules (American Rule vs. English Rule vs. statutory fee-shifting)
- Non-economic damages caps and limitations
- Prejudgment/postjudgment interest rates and compounding

**Procedural:**

- Pre-action obligations (US: no general obligation; UK: Pre-Action Protocols required; AU: National Court Framework)
- Costs and costs-shifting rules (loser pays in UK/AU; American Rule in US with exceptions)
- Disclosure/discovery scope and proportionality (FRCP vs. CPR vs. Federal Court Rules)
- ADR obligations and court powers (UK: mandatory ADR consideration; AU: judicial early neutral evaluation)
- Interim relief standards and timing

**Reputational:**

- Confidentiality of proceedings (public vs. private courts; commercial court in-camera procedures)
- Media access to filings and hearings
- Court-ordered confidentiality of settlement terms

**[JURISDICTION-SPECIFIC] Reference anchors frequently needed:**

- **US federal**: FRCP 8, 12(b)(6), 12(c), 56; 28 U.S.C. § 1927 (sanctions); Clayton Act (15 U.S.C. § 15 treble damages); DTSA (18 U.S.C. § 1836); 17 U.S.C. § 504-505 (copyright fee-shifting) [VERIFY]
- **England & Wales**: CPR Parts 1, 3, 16, 24, 36, 44; Pre-Action Conduct Practice Direction; Woolf Reforms (1999); Jackson Reforms (2013) cost budgeting; CPR 44.3(2)(a) proportionality [VERIFY]
- **Australia**: Federal Court Act 1976 (Cth) s.37M; Federal Court Rules 2011; CPN-1 Commercial and Corporations National Practice Area; Trade Practices Act / Competition and Consumer Act 2010; ALRC 75 costs principles [VERIFY]
- **EU**: Directive 2014/104/EU (antitrust damages); Directive 2016/943/EU (trade secrets); Brussels I Recast (jurisdiction); ECHR Art. 6 (fair trial) [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **⟁ CLARIFY**) at key decision points
where the answer materially changes the risk assessment or strategy recommendation. The
skill pauses and asks when:

- The scope, side, or assessment phase is unclear
- Risk appetite or organizational constraints would change the recommendation
- The governing law is uncertain or multiple jurisdictions may apply
- Key assumptions about probability or damages would benefit from user input before modeling

If the user has already provided the information, skip the question and proceed. For
batch or automated runs, proceed with stated defaults and mark assumptions explicitly.

---

## Workflow

### Step 1: Accept Litigation Input

Accept the matter description in any of these formats:

- **Pleadings**: Filed complaint, counterclaim, answer, or defence
- **Pre-litigation materials**: Demand letter, cease-and-desist, regulatory investigation notice
- **Matter summary**: Narrative description of claims, parties, facts, and current posture
- **Prior assessment**: Existing ECA, litigation budget, or risk memo to be updated

**If the input is insufficient**, identify the minimum required information:

1. Nature of claims/defenses (legal theories asserted)
2. Key facts and timeline
3. Parties and their relationships
4. Procedural stage (pre-demand → complaint → discovery → trial approaching)
5. Governing law and forum

Prompt the user to supply missing elements before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask these questions. Present as structured
options where possible. Skip any that the user has already answered.

1. **Whose perspective?**
   - Options: Claimant/Plaintiff, Defendant/Respondent, Third-party defendant, Both sides (conflict check), Neutral evaluation
   - _Why this matters_: The entire risk framing — burden of proof, damages exposure, recommendation — flips based on side.

2. **Assessment objective?**
   - Options: Go/no-go decision (file or defend), Settlement posture and authority, Board/executive risk update, Litigation budget and reserves, Full assessment (all dimensions), Mid-case reassessment at milestone
   - _Why this matters_: Controls depth, output format, and which dimensions receive the most analytical weight.

3. **Procedural stage?**
   - Options: Pre-demand (no claim yet filed), Early litigation (complaint filed, pre-discovery), Mid-case (discovery substantially complete), Late-case (trial within 6 months), Post-judgment (appeal or enforcement)
   - _Why this matters_: The information base, uncertainty level, and strategic options available differ dramatically by stage.

4. **Risk appetite?**
   - Options: Conservative (minimize downside; settle early if exposure is significant), Balanced (weigh cost and risk against merit), Aggressive (pursue or defend vigorously; settle only on favorable terms)
   - _Why this matters_: The same risk profile produces different recommendations depending on the client's tolerance for uncertainty and spend.

5. **Financial constraints?**
   - Options: No cap (full litigation budget available), Soft cap (budget preference, not a hard limit), Hard cap (defined maximum spend), Reserve required (need specific dollar reserve set)
   - _Why this matters_: Budget constraints directly affect whether the three-branch cost-benefit analysis (litigate/settle/mediate) is feasible or academic.

6. **Prior ECA or damages analysis available?**
   - Options: Yes — will provide or has been run already, No — run from scratch, Partial — some elements only
   - _Why this matters_: If a prior ECA exists, Steps 5 and 7 can be populated from it rather than re-analyzed, saving significant time.

If the user provides partial context, proceed with what you have, but **state your assumptions
explicitly**: e.g., "I am proceeding as if you are the defendant with a balanced risk appetite —
let me know if either assumption is wrong."

### Step 3: Load Risk Appetite Profile

Check whether the organization or client has a litigation risk playbook in local settings
(e.g., `legal.local.md`, `litigation-playbook.md`, or similar configuration).

A litigation risk playbook defines:

- **Default risk appetite** (conservative/balanced/aggressive by matter type)
- **Reserve methodology** (how to set litigation reserves for accounting purposes)
- **Settlement authority thresholds** (who can approve settlements at what amounts)
- **Board reporting triggers** (what risk levels require board notification)
- **Outside counsel budget parameters** (phase-based budget approval process)
- **Mandatory ADR requirements** (whether the organization requires mediation before trial)

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user and ask:

- **Option A: Proceed with ISO 31000-aligned defaults** — Use standard probability × impact scoring with balanced risk appetite. Label the assessment: "Based on ISO 31000 general standards — not organizational positions."
- **Option B: Define key parameters now** — Answer 3-5 questions to calibrate the model (settlement authority level, board trigger threshold, mandatory ADR policy).
- **Option C: I will calibrate after seeing results** — Run the full assessment first, then revisit parameters if the recommendations require authority escalation.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law and procedural forum. Then gather legal authority needed for
the merits and damages analysis.

**Using legalcode-mcp (if connected):**

Search for jurisdiction-relevant authority across:

1. Elements of each cause of action asserted (statutory text, leading cases defining elements)
2. Available defenses and their legal basis
3. Damages rules for the specific claim type (compensatory methodology, available multipliers)
4. Limitation periods and any tolling doctrine applicable
5. Fee-shifting statute (if applicable to this claim type)
6. Pre-action protocol or procedural obligations applicable to this forum
7. Recent case law on claims/defenses in this area that may shift probability estimates

Save the most relevant results to a local temporary reference file:

```markdown
# Legal Authority Reference — [Matter Name]

## Governing Law: [Jurisdiction]

## Date Gathered: [date]

## Procedural Forum: [Court/Tribunal]

### Claim Elements

- [Cause of action, elements, key cases] — VERIFIED (legalcode-mcp)

### Defense Elements

- [Defense, elements, key cases] — VERIFIED (legalcode-mcp)

### Damages Framework

- [Statute/principle, methodology, caps, multipliers] — VERIFIED (legalcode-mcp)

### Fee-Shifting

- [Statute/rule, conditions, direction of shifting] — VERIFIED (legalcode-mcp)

### Pre-Action / Procedural

- [Protocol, obligation, consequence of non-compliance] — VERIFIED (legalcode-mcp)
```

**If legalcode-mcp is not connected:**

- Proceed with general legal knowledge plus jurisdiction markers
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`

### Step 5: Legal Merit Assessment

Assess the legal strength of each claim and primary defense. Use element-level analysis.

**5a. Claim Viability Map**

For each cause of action asserted:

| Element     | Description          | Satisfied?               | Evidence Basis | Confidence  | Risk Notes    |
| ----------- | -------------------- | ------------------------ | -------------- | ----------- | ------------- |
| [Element 1] | [What must be shown] | ✓ Yes / ✗ No / ? Unclear | [Evidence]     | [0.00-1.00] | [Gaps, risks] |
| [Element 2] | [What must be shown] | ✓/✗/?                    | [Evidence]     | [Score]     | [Gaps]        |

**Claim-level legal merit score** = Composite of element scores weighted by criticality.
A single missing essential element collapses the entire claim, regardless of other scores.

**Claim Legal Merit Classification:**

| Classification | Score Range | Meaning                                                                              |
| -------------- | ----------- | ------------------------------------------------------------------------------------ |
| **STRONG**     | 0.75–1.00   | All elements appear satisfied; no single fatal gap                                   |
| **VIABLE**     | 0.55–0.74   | Most elements satisfied; one or more elements contested or uncertain                 |
| **MARGINAL**   | 0.35–0.54   | Multiple elements weak or contested; survival risk                                   |
| **WEAK**       | 0.00–0.34   | Fatal gap in at least one essential element; high dismissal or summary judgment risk |

**5b. Defense Viability Map**

For each asserted or available defense:

| Defense     | Basis               | Elements Met? | Strength                    | Confidence | Strategic Value             |
| ----------- | ------------------- | ------------- | --------------------------- | ---------- | --------------------------- |
| [Defense 1] | [Statute/principle] | ✓/✗/?         | STRONG/VIABLE/MARGINAL/WEAK | [Score]    | [Impact on overall posture] |

**⟁ CLARIFY** — If threshold issues are present (standing, limitation period, jurisdiction,
forum non conveniens, or failure to state a claim), ask:
"There appears to be a potential threshold defense: [issue]. Should I analyze this first?
If this defense succeeds, it moots the entire merits analysis. Options:

- (A) Analyze threshold issue first — if STRONG, recommend motion practice before full assessment
- (B) Analyze threshold issue in parallel with merits — provide full picture
- (C) Proceed without — threshold issue already litigated or strategically decided not to pursue"

**5c. Governing Law Uncertainty**

[JURISDICTION-SPECIFIC] Flag if the governing law creates significant legal merit uncertainty:

- **US**: Circuit splits on key issues; state law variations; unsettled federal preemption
- **UK**: Evolving test under [case]; no Court of Appeal authority; departing from commercial court guidance
- **AU**: Split between Federal Court and state courts; no High Court authority
- **EU**: CJEU precedent not yet applied in this jurisdiction; national implementation variations

Mark any such uncertainties with `[LEGAL UNCERTAINTY — affects confidence score]`

### Step 6: Factual Strength Assessment

Score the quality and coverage of available evidence. Factual strength is assessed
independently from legal merit — strong law with weak facts creates a different risk
profile than weak law with overwhelming facts.

**6a. Evidence Quality Matrix**

For each key factual element:

| Fact Issue | Evidence Available                             | Source   | Reliability  | Admissibility Risk | Contradiction Risk | Gap               |
| ---------- | ---------------------------------------------- | -------- | ------------ | ------------------ | ------------------ | ----------------- |
| [Key fact] | [Document / Witness / Expert / Circumstantial] | [Source] | HIGH/MED/LOW | LOW/MED/HIGH       | LOW/MED/HIGH       | [What is missing] |

**Evidence Reliability Scale:**

- **HIGH**: Primary documents, contemporaneous records, corroborated by multiple sources
- **MEDIUM**: Single-source, secondary evidence, or relies on witness recollection
- **LOW**: Disputed, derived, dependent on inference chains, or sole witness with credibility risk

**6b. Witness Credibility Assessment**

| Witness     | Role              | Importance                  | Credibility  | Preparation Risk | Impeachment Risk |
| ----------- | ----------------- | --------------------------- | ------------ | ---------------- | ---------------- |
| [Name/Role] | Fact/Expert/Mixed | Critical/Important/Marginal | HIGH/MED/LOW | LOW/MED/HIGH     | LOW/MED/HIGH     |

**6c. Document Coverage Assessment**

| Category   | Coverage                | Gaps              | Discovery Risk | Spoliation Risk |
| ---------- | ----------------------- | ----------------- | -------------- | --------------- |
| [Doc type] | Complete/Partial/Absent | [What is missing] | LOW/MED/HIGH   | LOW/MED/HIGH    |

**6d. Factual Strength Score**

| Dimension                  | Score (1-5) | Weight | Weighted Score  |
| -------------------------- | ----------- | ------ | --------------- |
| Evidence quality           | [Score]     | 30%    | [Weighted]      |
| Document coverage          | [Score]     | 25%    | [Weighted]      |
| Witness strength           | [Score]     | 25%    | [Weighted]      |
| Expert support             | [Score]     | 20%    | [Weighted]      |
| **Total Factual Strength** |             | 100%   | **[Composite]** |

**Factual Strength Classification:**

| Classification | Score Range | Meaning                                                |
| -------------- | ----------- | ------------------------------------------------------ |
| **STRONG**     | 4.0–5.0     | Comprehensive, reliable evidence; low gaps             |
| **ADEQUATE**   | 3.0–3.9     | Good core evidence; manageable gaps                    |
| **THIN**       | 2.0–2.9     | Evidence exists but material gaps or credibility risks |
| **WEAK**       | 1.0–1.9     | Evidence is sparse, unreliable, or heavily contested   |

**⟁ CLARIFY** — For mid-case or late-case assessments, ask:
"Have key depositions, expert reports, or document production been completed? Factual
strength assessments made before these milestones carry significantly more uncertainty.
Should I:

- (A) Proceed with current evidence assessment, noting pre-milestone uncertainty
- (B) Flag this as requiring reassessment after [specific upcoming event]
- (C) Run a sensitivity analysis showing how the score would change if key evidence goes against you"

### Step 7: Damages Exposure Modeling

Build a three-scenario damages exposure model (pessimistic / base case / optimistic) for
both sides (if applicable). Integrate with `legalcode-damages-calculation` for granular
methodology if available.

**7a. Damages Category Inventory**

Identify all available damages categories for this claim type:

| Category                       | Available?   | Calculation Method  | Low (P10) | Base (P50)  | High (P90) |
| ------------------------------ | ------------ | ------------------- | --------- | ----------- | ---------- |
| Compensatory — economic        | Yes/No       | [Method]            | $[Low]    | $[Base]     | $[High]    |
| Compensatory — non-economic    | Yes/No       | [Method]            | $[Low]    | $[Base]     | $[High]    |
| Punitive / exemplary           | Yes/No/Maybe | [Standard required] | $0        | $[Base]     | $[High]    |
| Statutory damages              | Yes/No       | [Per violation]     | $[Min]    | $[Base]     | $[Max]     |
| Fee-shifting (attorneys' fees) | Yes/No       | [Standard]          | $0        | $[Estimate] | $[High]    |
| Interest (prejudgment)         | Yes/No       | [Rate/method]       | $[Low]    | $[Base]     | $[High]    |

**[JURISDICTION-SPECIFIC] Multiplier/enhancement analysis:**

- **US antitrust (Clayton Act § 4)**: Mandatory treble of proved damages + attorneys' fees [VERIFY]
- **US DTSA (trade secrets)**: Exemplary damages up to 2× compensatory for willful misappropriation; fee-shifting [VERIFY]
- **US patent (35 U.S.C. § 284)**: Up to 3× enhanced damages for willful infringement [VERIFY]
- **UK**: No punitive trebling; aggravated + exemplary damages in narrow categories (Rookes v. Barnard) [VERIFY]
- **AU**: Exemplary damages for intentional torts; civil liability statutory restrictions in some states [VERIFY]
- **EU antitrust (Directive 2014/104/EU)**: Single damages + full compensatory; passing-on defense [VERIFY]

**7b. Expected Value Calculation**

For each scenario:

```
Expected Value (EV) = P(liability) × Damages(scenario) − Litigation Costs(scenario)

Where:
P(liability) = Probability of establishing liability (informed by Steps 5 and 6)
Damages(scenario) = Damages amount in that scenario
Litigation Costs(scenario) = Projected legal spend to reach judgment under that scenario
```

| Scenario          | P(liability) | Damages | Litigation Costs | EV (Plaintiff) | Net Exposure (Defendant) |
| ----------------- | ------------ | ------- | ---------------- | -------------- | ------------------------ |
| Pessimistic (P10) | [Low prob]   | $[Low]  | $[High spend]    | $[EV]          | $[Exposure]              |
| Base Case (P50)   | [Base prob]  | $[Base] | $[Base spend]    | $[EV]          | $[Exposure]              |
| Optimistic (P90)  | [High prob]  | $[High] | $[Low spend]     | $[EV]          | $[Exposure]              |

**7c. Damages Exposure Classification**

| Classification  | Threshold                             | Meaning                                                       |
| --------------- | ------------------------------------- | ------------------------------------------------------------- |
| **EXISTENTIAL** | > 25% of annual revenue or $100M+     | Case outcome could threaten viability                         |
| **MATERIAL**    | 5–25% of annual revenue or $10M–$100M | Significant financial impact; board-level visibility required |
| **SIGNIFICANT** | 1–5% of annual revenue or $1M–$10M    | Material but manageable; requires senior management attention |
| **MANAGEABLE**  | < 1% of annual revenue or < $1M       | Limited financial impact; proportionate response appropriate  |

**⟁ CLARIFY** — If treble damages or statutory multipliers apply, ask:
"The applicable statute [name] provides for [treble/2x/enhanced] damages on proof of
[willfulness/intentionality/knowing violation]. The evidence of [willfulness] appears
[strong/weak/uncertain]. Should I:

- (A) Include full multiplier in the pessimistic and base case models
- (B) Include multiplier only in the pessimistic (worst case) scenario
- (C) Exclude multiplier and model as a separate sensitivity scenario"

### Step 8: Reputational and Strategic Risk Assessment

Assess the non-monetary risks of the litigation — the dimensions that may outweigh
financial exposure for certain clients or matters.

**8a. Reputational Risk Factors**

| Factor                          | Score (1-5) | Assessment                                                    | Notes                            |
| ------------------------------- | ----------- | ------------------------------------------------------------- | -------------------------------- |
| **Media profile**               | [1-5]       | [Likely to attract / unlikely to attract media attention]     | Industry, parties, claim novelty |
| **Public record risk**          | [1-5]       | [Filings public / confidential; exhibits filed / sealed]      | Court rules on sealing           |
| **Precedent sensitivity**       | [1-5]       | [Adverse ruling would set binding or persuasive precedent]    | Jurisdiction, court level        |
| **Regulatory spillover**        | [1-5]       | [Could trigger regulatory investigation, audit, or action]    | Industry, regulators             |
| **Customer / partner impact**   | [1-5]       | [Existing customers / partners may react adversely to case]   | Contractual triggers, trust      |
| **Employee / workforce impact** | [1-5]       | [Case may affect morale, retention, or employment claims]     | Workplace issues asserted        |
| **Leadership credibility**      | [1-5]       | [Named individuals; deposition exposure of executives]        | Individual defendants            |
| **Competitor advantage**        | [1-5]       | [Litigation gives competitor market intelligence or leverage] | Trade secrets, discovery         |

**Reputational Risk Score** = Average of applicable factors

**Reputational Risk Classification:**

| Classification | Score Range | Meaning                                                                                    |
| -------------- | ----------- | ------------------------------------------------------------------------------------------ |
| **CRITICAL**   | 4.0–5.0     | High media, regulatory, and precedent risk; reputational harm may dwarf financial exposure |
| **ELEVATED**   | 3.0–3.9     | Meaningful reputational exposure; requires communication and stakeholder strategy          |
| **MODERATE**   | 2.0–2.9     | Limited reputational risk; standard litigation posture appropriate                         |
| **LOW**        | 1.0–1.9     | Minimal reputational dimension; purely commercial dispute                                  |

**8b. Strategic Risk Factors**

Beyond reputation, identify strategic dimensions that affect the recommendation:

| Strategic Factor                                                      | Present?       | Impact on Recommendation                                                  |
| --------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------- |
| Precedent risk: adverse ruling would bind future claims               | Yes/No/Unclear | If YES, more weight to litigation/appeal; less weight to early settlement |
| Relationship value: ongoing commercial relationship with counterparty | Yes/No         | If YES, settlement and mediation more valuable                            |
| Portfolio risk: multiple related claims that could follow             | Yes/No         | If YES, precedent-setting or quick settlement may prevent wave of claims  |
| Discovery risk: sensitive business information subject to disclosure  | Yes/No         | If YES, consider protective orders, sealing, and early ADR                |
| Insurance coverage: litigation costs or exposure covered by policy    | Yes/No         | If YES, consult insurance counsel; may affect settlement authority        |
| Regulatory parallel: concurrent regulatory proceeding on same conduct | Yes/No         | If YES, coordinate litigation and regulatory strategy carefully           |
| Judgment enforceability: counterparty has assets to satisfy judgment  | Yes/No         | If NO for claimant, recalibrate value of full litigation path             |

### Step 9: Build the Four-Dimensional Litigation Risk Matrix

Integrate the four dimensions into a consolidated litigation risk matrix. This is the
core analytical output of the skill.

**9a. Dimension Scores Summary**

| Dimension         | Classification                              | Composite Score | Confidence                                 |
| ----------------- | ------------------------------------------- | --------------- | ------------------------------------------ |
| Legal Merit       | STRONG/VIABLE/MARGINAL/WEAK                 | [0.00-1.00]     | [Definite/High/Probable/Possible/Unlikely] |
| Factual Strength  | STRONG/ADEQUATE/THIN/WEAK                   | [1.00-5.00]     | [Level]                                    |
| Damages Exposure  | EXISTENTIAL/MATERIAL/SIGNIFICANT/MANAGEABLE | $[Range]        | [Level]                                    |
| Reputational Risk | CRITICAL/ELEVATED/MODERATE/LOW              | [1.00-5.00]     | [Level]                                    |

**9b. Composite Risk Score**

Weight and aggregate the four dimensions into a composite risk score:

```
Composite Risk Score = (Legal Merit × W1) + (Factual Strength × W2) +
                       (Damages Exposure × W3) + (Reputational Risk × W4)

Default weights (adjust per risk appetite profile):
  W1 (Legal Merit)      = 30%
  W2 (Factual Strength) = 25%
  W3 (Damages Exposure) = 30%
  W4 (Reputational Risk) = 15%

For conservative risk appetite: increase W3 (Damages) and W4 (Reputation) weights
For aggressive risk appetite: increase W1 (Legal Merit) weight
```

**9c. Overall Litigation Risk Classification**

| Classification | Score     | Meaning for Claimant                                          | Meaning for Defendant                                                     |
| -------------- | --------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **CRITICAL**   | 0.80–1.00 | Exceptional case; enforce aggressively                        | Existential threat; immediate settlement or aggressive defense justified  |
| **HIGH**       | 0.60–0.79 | Strong case; litigation cost-justified with realistic damages | Significant exposure; settlement seriously considered; strengthen defense |
| **MEDIUM**     | 0.40–0.59 | Viable case with material uncertainty; evaluate ROI carefully | Manageable exposure; defense viable; explore ADR to reduce uncertainty    |
| **LOW**        | 0.00–0.39 | Marginal or weak case; litigation value questionable          | Limited exposure; defense likely cost-effective; monitor only             |

**9d. Risk Matrix Visualization**

Present the two most significant dimensions as a 2×2 matrix with narrative placement:

```
LITIGATION RISK MATRIX (Legal Merit vs. Factual Strength)

                    FACTUAL STRENGTH
                    WEAK       STRONG
                  ┌──────────┬──────────┐
LEGAL    STRONG   │ MEDIUM   │ HIGH/    │
MERIT             │ (Facts   │ CRITICAL │
                  │ kill     │          │
                  │ good law)│          │
         ─────────┼──────────┼──────────┤
         WEAK     │ LOW      │ MEDIUM   │
                  │ (Both    │ (Facts   │
                  │ weak)    │ can't    │
                  │          │ save     │
                  │          │ bad law) │
                  └──────────┴──────────┘
```

Place the matter in the appropriate quadrant with a brief narrative explanation of what
drives the classification and what changes would shift it.

### Step 10: Three-Branch Cost-Benefit Analysis

Compare the expected value of each resolution path.

**10a. Branch Definitions**

| Branch                   | Description                                         | Timeline                  | Spend Model        |
| ------------------------ | --------------------------------------------------- | ------------------------- | ------------------ |
| **Litigate to Judgment** | Full litigation through trial or summary judgment   | [Forum-specific estimate] | Phase-based budget |
| **Settle Now**           | Negotiate settlement at current posture             | Immediate to 3 months     | Limited spend      |
| **Mediate**              | Structured mediation with pre-mediation preparation | 1-4 months                | Moderate spend     |

**10b. Cost-Benefit Table**

| Branch               | Projected Legal Spend | Probability of Favorable Outcome | Expected Recovery / Savings  | Net Expected Value | Timeline to Resolution | Risk-Adjusted NPV       |
| -------------------- | --------------------- | -------------------------------- | ---------------------------- | ------------------ | ---------------------- | ----------------------- |
| Litigate to Judgment | $[Spend]              | [P%]                             | $[Recovery/Savings]          | $[EV]              | [Months]               | $[NPV at discount rate] |
| Settle Now           | $[Spend]              | [Certainty — negotiated]         | $[Settlement range]          | $[EV]              | [Months]               | $[NPV]                  |
| Mediate              | $[Spend]              | [P% of successful mediation]     | $[Expected settlement range] | $[EV]              | [Months]               | $[NPV]                  |

**[JURISDICTION-SPECIFIC] Adjust for:**

- **UK Part 36**: Non-acceptance of a Part 36 offer can impose cost sanctions if the offeree fails to beat the offer at trial. Model the Part 36 consequence as a separate scenario. [VERIFY]
- **US Rule 68**: Defendant offer of judgment — if not accepted and claimant fails to obtain more favorable judgment, claimant pays defendant's post-offer costs (for claims with fee-shifting). [VERIFY]
- **AU Calderbank letters**: Without-prejudice-save-as-to-costs offers used to obtain costs penalties similar to Part 36; no formal mechanism but courts give weight to unreasonable non-acceptance. [VERIFY]
- **US Class Actions**: Early settlement before class certification avoids class-wide exposure but may face fairness hearing; late settlement after certification requires court approval. [VERIFY]

**10c. Branch Recommendation Matrix**

| Condition                                                          | Recommended Branch                                          | Rationale                                                  |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------- |
| Legal Merit STRONG + Factual STRONG + Damages MATERIAL/EXISTENTIAL | Litigate to Judgment OR negotiate from position of strength | High chance of favorable resolution; damages justify spend |
| Legal Merit VIABLE + Factual THIN + Damages SIGNIFICANT            | Mediate                                                     | Uncertain outcome; mediation resolves factual uncertainty  |
| Legal Merit WEAK + any other dimension                             | Early Settlement OR Abandon                                 | Cost of litigation exceeds realistic EV                    |
| Reputational Risk CRITICAL + Legal Merit VIABLE                    | Mediate or Settle Confidentially                            | Reputational harm may exceed financial exposure            |
| Relationship value HIGH                                            | Mediate                                                     | Preserving relationship may outweigh litigation economics  |
| Portfolio risk HIGH (wave of claims)                               | Litigate to dismissal or Settle with broad release          | Precedent-setting strategy; silence demand                 |

**⟁ CLARIFY** — If the three-branch cost-benefit analysis produces a close call between
two branches (EVs within 15% of each other), present the result to the user:
"The cost-benefit analysis shows [Branch A] and [Branch B] are closely matched in expected
value ($[A] vs. $[B]). The decision turns on [key differentiator: risk tolerance / timeline
/ relationship / reputational factors]. How should I weight those factors for this matter?"

### Step 11: Confidence Aggregation and Sensitivity Analysis

**11a. Confidence Aggregation**

Each dimension was scored with an associated confidence level. Aggregate to an overall
assessment confidence:

```
Overall Confidence = MIN(dimension confidences) as the binding constraint,
                     adjusted upward if the binding constraint is a non-critical dimension

Example:
  Legal Merit: HIGH (0.85) — strong authority, minor interpretation questions
  Factual Strength: PROBABLE (0.65) — good evidence, key document not yet reviewed
  Damages: HIGH (0.80) — well-documented economic loss
  Reputational: DEFINITE (0.95) — media profile assessment based on court filings

Overall Confidence = PROBABLE (0.65) — the factual strength uncertainty sets the ceiling
                     because factual strength carries 25% weight in composite score
```

**11b. Sensitivity Analysis: Key Assumption Scenarios**

Identify the 3-5 assumptions that most affect the composite score, and show how the
recommendation changes if they move adversely:

| Assumption                   | Base Case Value    | Adverse Scenario | Effect on Composite Score | Effect on Recommendation |
| ---------------------------- | ------------------ | ---------------- | ------------------------- | ------------------------ |
| P(liability)                 | [Base %]           | [Adverse % −15%] | [Score change]            | [Recommendation change?] |
| Key evidence admissibility   | Assumed admissible | Excluded         | [Score change]            | [Recommendation change?] |
| Damages (base case)          | $[Base]            | $[Base × 0.60]   | [Score change]            | [Recommendation change?] |
| Treble damages applicability | Excluded           | Included         | [Score change]            | [Recommendation change?] |
| Key witness credibility      | Favorable          | Impeached        | [Score change]            | [Recommendation change?] |

**Flag any assumption whose adverse scenario would shift the overall recommendation
from one branch to another.** These are the critical uncertainties that should drive
near-term information-gathering.

**11c. Confidence Scoring Reference**

| Level        | Range     | Meaning                                                   | Action                                                   |
| ------------ | --------- | --------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95–1.00 | Settled law/facts, no material ambiguity                  | Assert with confidence                                   |
| **High**     | 0.80–0.94 | Strong authority/evidence, minor uncertainties            | Assert with brief caveat                                 |
| **Probable** | 0.60–0.79 | Good basis, reasonable alternative interpretations remain | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities or facts       | Flag for counsel review; present both sides              |
| **Unlikely** | 0.00–0.39 | Weak basis, speculative                                   | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

### Step 12: Generate Recommendations and Risk Profile Narrative

**12a. Strategic Recommendation**

Produce a tiered recommendation with conditional triggers:

**Primary Recommendation:** [Litigate / Settle / Mediate] — [one-sentence rationale]

**Triggers that would change this recommendation:**

- If [specific event/discovery/ruling] → Reconsider to [alternative branch]
- If [specific event/discovery/ruling] → Escalate to [board/outside counsel/settlement authority]

**Immediate Actions (next 30 days):**

1. [Specific action — e.g., serve/respond to discovery, retain expert, initiate ADR]
2. [Action]
3. [Action]

**Near-Term Actions (30-90 days):**

1. [Action]
2. [Action]

**⟁ CLARIFY** — If the recommendation is Settle or Mediate, ask:
"The assessment supports early resolution. Before finalizing the recommendation, I need
to check settlement authority. What is the settlement authority limit for this matter
(who can approve and at what amount)? Should I flag escalation requirements in the
deliverable?"

**12b. Risk Profile Narrative**

Write a one-to-two-paragraph plain-language executive summary positioning the litigation
within the context of the assessed risk dimensions. Format for a non-lawyer audience:

```markdown
## Litigation Risk Profile: [Matter Name]

**Date**: [Date] **Side**: [Claimant/Defendant] **Stage**: [Stage]

[Paragraph 1 — What this case is about and overall risk classification]:
This litigation presents a [CRITICAL/HIGH/MEDIUM/LOW] overall risk profile based on
[strong/adequate/weak] legal merit, [strong/adequate/thin/weak] factual evidence,
[existential/material/significant/manageable] damages exposure, and [critical/elevated/
moderate/low] reputational risk. [1-2 sentences on the key drivers of the assessment.]

[Paragraph 2 — Recommendation and rationale]:
Based on this assessment, the recommended approach is to [branch + reasoning]. The
decision is [highly confident / probable / uncertain] at this stage given [key uncertainties].
The most critical near-term action is [specific action] because [reason it would most change
the risk picture]. Legal spend budget should be [range] with a [contingency] reserve.
```

---

## Risk Classification Reference

### Overall Litigation Risk

| Classification | Composite Score | Claimant Posture                      | Defendant Posture                                    | Default Recommendation                                          |
| -------------- | --------------- | ------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| **CRITICAL**   | 0.80–1.00       | Exceptional case; pursue aggressively | Existential; settle or defend with maximum resources | Litigate (claimant) / Settle or defend aggressively (defendant) |
| **HIGH**       | 0.60–0.79       | Strong case; ROI positive             | Significant exposure; cost-benefit close             | Litigate or negotiate from strength                             |
| **MEDIUM**     | 0.40–0.59       | Viable but uncertain; manage spend    | Manageable; defense viable                           | Mediate or settle within authority                              |
| **LOW**        | 0.00–0.39       | Marginal; question ROI                | Limited exposure; cost-effective defense likely      | Early settlement or defense without full spend                  |

### Dimension-Level Classification Summary

| Dimension                    | Strong / Best    | Good               | Weak                 | Critical / Worst |
| ---------------------------- | ---------------- | ------------------ | -------------------- | ---------------- |
| Legal Merit                  | STRONG (0.75+)   | VIABLE (0.55-0.74) | MARGINAL (0.35-0.54) | WEAK (0.00-0.34) |
| Factual Strength             | STRONG (4.0-5.0) | ADEQUATE (3.0-3.9) | THIN (2.0-2.9)       | WEAK (1.0-1.9)   |
| Damages Exposure (Defendant) | MANAGEABLE       | SIGNIFICANT        | MATERIAL             | EXISTENTIAL      |
| Reputational Risk            | LOW              | MODERATE           | ELEVATED             | CRITICAL         |

---

## Prioritization Framework

Organize findings and actions by urgency:

### Tier 1 — Immediate (0-72 hours)

Issues that, if not addressed within 72 hours, cannot be remedied:

- Limitation period expiry within 14 days
- Preservation/litigation hold obligation not yet implemented
- Pre-action protocol obligation due (UK/AU)
- Interim relief application window closing
- Settlement offer expiry (Part 36 / Rule 68 / Calderbank)
- Critical evidence at risk of destruction or spoliation

### Tier 2 — Near-Term (3-30 days)

Issues that materially affect risk trajectory:

- Expert retention before exclusion deadline
- Discovery production obligation deadlines
- Key witness interview or deposition scheduling
- Motion practice filing window (motion to dismiss, summary judgment)
- Insurance notification obligations
- Settlement authority escalation

### Tier 3 — Programmatic (30+ days)

Important but not time-sensitive:

- Mid-case reassessment scheduling milestones
- Legal budget review and reserve adjustment
- Stakeholder communication planning
- Regulatory parallel coordination
- Outside counsel budget approval for next phase

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                   | Fail Action                                                                |
| -------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, case, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]"                   |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction            | Fix citation format                                                        |
| **Currency**   | Every cited provision checked for amendments, repeal, or superseding authority         | Flag "[CHECK CURRENCY — may have been amended]"                            |
| **Domain**     | Analysis stays within the matter's governing law; no jurisdiction bleed                | Remove or flag with "[JURISDICTION-SPECIFIC — verify under governing law]" |
| **Confidence** | Uncertainty explicitly stated, not hidden; if uncertain, say so                        | Add confidence qualifier; lower score if necessary                         |

### Self-Interrogation for CRITICAL/HIGH Findings

For any finding classified as CRITICAL or HIGH risk, apply this 3-pass challenge:

**Pass 1 — Legal Chain Integrity**:

- Does the risk classification follow logically from the cited authority and established facts?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument opposing counsel will make that could succeed?

**Pass 2 — Completeness**:

- Have all relevant statutes, regulations, cases, and procedural rules been considered?
- Are there threshold issues or defenses not yet analyzed that could change the picture?
- Have damages categories been fully inventoried — including fee-shifting and multipliers?

**Pass 3 — Challenge**:

- What is the strongest argument that this risk is actually lower?
- Under what circumstances might a court rule against the CRITICAL/HIGH classification?
- Is the classification proportionate, or could a reasonable litigator accept this risk?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### PDCA Quality Cycle

**PLAN**: Confirm matter context, governing law, assessment stage, side, and risk appetite.
Identify which dimensions need the most analytical depth based on the matter facts.

**DO**: Execute the 12-step workflow. Run the four-dimensional assessment. Build cost-benefit.
Score confidence.

**CHECK**: Run Citation Quality Gates. Apply Self-Interrogation for CRITICAL/HIGH items.
Confirm all 4 dimensions addressed. Verify jurisdiction-specific rules are correctly applied.

**ACT**: Note critical uncertainties that require information-gathering. Schedule reassessment
milestones. Flag escalation requirements. Record emerging patterns for future reference.

---

## Glass Box Audit Trail

Every risk assessment output MUST include a Glass Box section. This makes the reasoning
traceable and auditable — especially important when the assessment is used to authorize
settlement or litigation spend.

```yaml
glass_box:
  skill_name: "legalcode-litigation-risk-assessment"
  matter: "[Matter name / file reference]"
  side: "[Claimant / Defendant / Neutral]"
  assessment_stage: "[Pre-demand / Early litigation / Mid-case / Late-case]"
  governing_law: "[Jurisdiction]"
  forum: "[Court / Tribunal]"
  assessment_date: "[date]"
  risk_appetite: "[Conservative / Balanced / Aggressive]"
  playbook_used: "[Playbook name or 'ISO 31000 defaults']"
  # Dimension scores
  legal_merit_score: "[Classification — Composite Score — Confidence]"
  factual_strength_score: "[Classification — Composite Score — Confidence]"
  damages_exposure: "[Classification — Range — Confidence]"
  reputational_risk_score: "[Classification — Score — Confidence]"
  # Composite
  composite_risk_score: "[Score]"
  overall_classification: "[CRITICAL / HIGH / MEDIUM / LOW]"
  overall_confidence: "[Definite / High / Probable / Possible / Unlikely] — [rationale]"
  # Recommendation
  recommended_branch: "[Litigate / Settle / Mediate]"
  recommendation_confidence: "[Score]"
  # Quality assurance
  legalcode_mcp: "Connected / Not connected — manual verification required"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or [VERIFY]]"
  case_law_consulted:
    - "[Case — VERIFIED or [VERIFY]]"
  citations_verified: "[number VERIFIED] / [number [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL/HIGH findings)"
  # Confidence aggregation
  confidence_binding_dimension: "[Which dimension sets the ceiling and why]"
  # Sensitivity
  critical_uncertainties:
    - "[Assumption — adverse scenario — effect on recommendation]"
  # Limitations
  limitations:
    - "[Scope limitation, unreviewed evidence, missing jurisdiction research, etc.]"
  reviewer: "AI-assisted — requires qualified legal review before use in litigation decisions"
```

---

## Anti-Patterns

What NOT to do when conducting a litigation risk assessment:

1. **Assessing only legal merit** — Legal merit is one of four dimensions. A legally perfect claim with weak evidence and massive damages exposure may be more dangerous than a legally uncertain claim with overwhelming evidence and capped damages. Always assess all four dimensions.

2. **Conflating legal merit with win probability** — Legal merit assesses whether the claim is legally sound. Win probability requires merging legal merit, factual strength, evidence quality, and judicial/jury risk. They are different questions.

3. **Ignoring the costs side of expected value** — An EV calculation that omits litigation costs dramatically overstates the value of litigation to the claimant and understates the cost-effectiveness of settlement. Always incorporate spend into the EV formula.

4. **Confusing pre-discovery and post-discovery confidence** — A pre-discovery assessment is built on incomplete information. It should carry lower confidence and wider ranges than a post-discovery assessment. Never present pre-discovery probability estimates with the same confidence as post-discovery ones.

5. **Omitting fee-shifting from damages exposure** — In fee-shifting statutes (US IP, antitrust, employment; UK/AU loser-pays default), attorneys' fees can rival or exceed the underlying damages award. A risk assessment that misses fee-shifting materially underestimates exposure.

6. **Treating treble and punitive damages as unlikely outliers** — For claims under antitrust, trade secrets (DTSA), or patent willful infringement, trebling is mandatory if proved. These multipliers belong in the base case or pessimistic scenario, not as an exotic outlier.

7. **Assigning single-point probability estimates as definite** — All probability estimates are uncertain. Present ranges or explicit confidence levels. A "60% chance of prevailing" presented without a confidence qualifier may be anywhere from 40% to 75% depending on unknown facts.

8. **Ignoring jurisdiction bleed** — The American Rule (each party pays own fees), loser-pays (UK/AU default), treble damages (US), aggravated damages (UK), exemplary damages (AU), and CJEU single-damages rule (EU antitrust) are jurisdiction-specific. Never import one jurisdiction's damages regime into another.

9. **Underweighting reputational risk for high-profile matters** — In cases involving executive misconduct, product safety, or civil rights, reputational harm from discovery disclosures, testimony, and public filings may far exceed the financial stakes. Always assess reputation as a separate dimension.

10. **Failing to model discovery as a cost driver** — US-style discovery is the single largest cost driver in federal litigation. Any cost-benefit analysis that treats discovery as a small fraction of total spend is likely to be materially wrong. Obtain phase-based budget estimates from litigation counsel before finalizing the model.

11. **Skipping the sensitivity analysis** — A single-point risk assessment that does not test key assumptions gives a false sense of precision. Identify the 3-5 assumptions that most affect the conclusion and show how the recommendation changes if they move adversely.

12. **Assuming all evidence will be admitted** — Admissibility challenges (Daubert/FRE 702 for experts, hearsay, authentication) can eliminate key evidence. A factual strength score that assumes all available evidence will be admitted may be materially over-optimistic.

13. **Treating the recommendation as a final answer** — Litigation risk assessments have a shelf life measured in months, not years. A mid-case reassessment after key depositions, expert reports, or dispositive rulings is not optional — it is how the model stays calibrated.

14. **Ignoring the counterparty's BATNA** — For settlement analysis, the recommendation is meaningless without modeling whether the counterparty has a rational incentive to settle within the assessed corridor. A CRITICAL case for the claimant may be MEDIUM for an over-insured defendant who gains discovery value from litigation.

15. **Conflating "weak case" with "no settlement value"** — Even a LOW risk claim may have nuisance value (defendant's cost of defense exceeds the claim value) or strategic value (claimant needs discovery). Model these dimensions before recommending abandonment.

16. **Forgetting parallel proceedings** — Concurrent regulatory investigations, parallel civil proceedings, or arbitrations based on the same facts can dramatically change risk through collateral estoppel, res judicata, document disclosure obligations, or regulatory sanction exposure. Always check for parallel proceedings.

17. **Producing a risk assessment without escalation triggers** — A risk assessment that delivers a recommendation without defining the conditions that would require escalation (spend authorization, settlement authority, board notification) is operationally incomplete.

18. **Assessing without checking limitation periods** — Limitation periods can moot an otherwise strong claim overnight. Check the applicable limitation period and any tolling doctrines before any other analysis. A claim past its limitation period has zero merit, regardless of factual or legal strength.

---

## Writing Standards

Apply plain-language discipline to all risk assessment output:

**For executive summaries and risk profile narratives:**

- Plain language, no jargon. Write for a CFO, not a litigator.
- Active voice: "The claim faces a significant burden" not "A significant burden is faced by the claim."
- Short sentences. One point per sentence.
- Lead with the conclusion: state the overall classification before explaining why.
- Quantify: "$3M–$8M exposure" is clearer than "significant financial exposure."

**For technical analysis sections:**

- Use tables for comparative information (evidence matrix, cost-benefit table, sensitivity analysis).
- Use numbered steps for workflow instructions.
- Use checkboxes for checklists.
- Cite jurisdiction-specific legal authority when available; mark [VERIFY] when uncertain.
- Label every probability estimate with its confidence level.

**Quality gates before delivery:**

- [ ] All four dimensions assessed and scored
- [ ] Cost-benefit analysis includes all three branches
- [ ] Confidence levels stated for each dimension score
- [ ] At least 3 sensitivity assumptions tested
- [ ] Escalation triggers and immediate actions specified
- [ ] Glass Box audit trail completed
- [ ] Self-interrogation run for CRITICAL/HIGH findings
- [ ] Citation Quality Gates passed
- [ ] Executive summary written in plain language

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes, regulations, cases, and procedural rules
- Save research to `/tmp/legalcode-risk-assessment-authority.md`
- Use verified authority to score legal merit with higher confidence
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box
- Re-run legalcode-mcp if the matter is mid-case and recent rulings may have shifted the law

**Without legalcode-mcp:**

- Proceed with general legal knowledge plus jurisdiction markers
- Mark all citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Increase the width of probability ranges to reflect greater legal authority uncertainty
- Focus analytical depth on the factual strength and damages dimensions where legalcode-mcp
  adds less value

**Integration with other Legalcode skills:**

- Output from `legalcode-early-case-assessment` feeds Step 5 (Legal Merit Assessment)
- Output from `legalcode-damages-calculation` feeds Step 7 (Damages Exposure Modeling)
- Output of this skill feeds `legalcode-settlement-negotiation` as the merits and exposure input

---

## Localization Notes

This skill is jurisdiction-agnostic. When working on jurisdiction-specific matters,
supplement the [JURISDICTION-SPECIFIC] markers with verified local content:

**United States:**

- Research applicable circuit court splits on claim elements and evidentiary standards
- Identify fee-shifting statutes applicable to the claim type (Copyright Act, DTSA, Clayton Act, FLSA, etc.)
- Check treble damages availability (antitrust, trade secrets, patent willful infringement)
- Assess class action risk separately if facts could support a class (Rule 23 requirements, CAFA jurisdiction)
- Review relevant state law variations if state claims brought alongside federal claims

**England & Wales:**

- Apply CPR Part 36 analysis: has any Part 36 offer been made? What are the cost consequences?
- Apply Woolf proportionality principles: is the litigation proportionate to the amount in dispute?
- Identify applicable Pre-Action Protocol obligations and assess compliance risk
- Assess indemnity costs exposure for unreasonable conduct (CPR 44.3)
- Consider Commercial Court costs management orders (budgets approved by court)

**Australia:**

- Apply Federal Court Act s.37M just and efficient resolution principles
- Assess CPN-1 requirements for Commercial and Corporations matters
- Identify applicable state civil liability legislation caps on damages
- Review proportionality obligations under ALRC 75 principles
- Assess Calderbank letter strategy if settlement is possible

**EU / Civil Law Systems:**

- Note absence of US-style discovery; European disclosure is typically more limited
- Apply single-damages rule under Directive 2014/104/EU for antitrust matters
- Assess Trade Secrets Directive 2016/943/EU requirements for trade secret protection adequacy
- Note absence of jury trials in most EU jurisdictions; assess bench trial risk profile
- Identify mandatory ADR requirements under applicable EU directives or national law

---

## Output Format Template

Every assessment delivers the following structured output:

```markdown
# Litigation Risk Assessment: [Matter Name]

**Date**: [Date] **Side**: [Claimant/Defendant] **Stage**: [Stage]
**Governing Law**: [Jurisdiction] **Forum**: [Court/Tribunal]

---

## Overall Classification: [CRITICAL / HIGH / MEDIUM / LOW]

**Composite Score**: [X.XX] **Confidence**: [Level]
**Recommended Branch**: [Litigate / Settle / Mediate]

---

## Executive Summary

[Risk Profile Narrative — 2 paragraphs, plain language]

---

## Four-Dimensional Risk Matrix

| Dimension         | Classification   | Score       | Confidence  |
| ----------------- | ---------------- | ----------- | ----------- |
| Legal Merit       | [Classification] | [Score]     | [Level]     |
| Factual Strength  | [Classification] | [Score]     | [Level]     |
| Damages Exposure  | [Classification] | [Range]     | [Level]     |
| Reputational Risk | [Classification] | [Score]     | [Level]     |
| **Composite**     | **[Overall]**    | **[Score]** | **[Level]** |

[Risk Matrix 2×2 visual — Legal Merit vs. Factual Strength with placement notation]

---

## Damages Exposure

| Scenario          | P(liability) | Damages | Litigation Costs | Net EV |
| ----------------- | ------------ | ------- | ---------------- | ------ |
| Pessimistic (P10) | [%]          | $[Low]  | $[Spend]         | $[EV]  |
| Base Case (P50)   | [%]          | $[Base] | $[Spend]         | $[EV]  |
| Optimistic (P90)  | [%]          | $[High] | $[Spend]         | $[EV]  |

[Fee-shifting / multiplier analysis if applicable]

---

## Three-Branch Cost-Benefit Analysis

| Branch               | Spend    | P(Favorable) | Expected Value | Timeline | NPV    |
| -------------------- | -------- | ------------ | -------------- | -------- | ------ |
| Litigate to Judgment | $[Spend] | [%]          | $[EV]          | [Months] | $[NPV] |
| Settle Now           | $[Spend] | [Negotiated] | $[Range]       | [Months] | $[NPV] |
| Mediate              | $[Spend] | [%]          | $[Range]       | [Months] | $[NPV] |

---

## Sensitivity Analysis

| Assumption     | Base   | Adverse   | Effect on Score | Effect on Recommendation |
| -------------- | ------ | --------- | --------------- | ------------------------ |
| [Assumption 1] | [Base] | [Adverse] | [Δ Score]       | [Change?]                |
| [Assumption 2] | [Base] | [Adverse] | [Δ Score]       | [Change?]                |
| [Assumption 3] | [Base] | [Adverse] | [Δ Score]       | [Change?]                |

---

## Strategic Recommendations

**Primary**: [Branch + rationale]

**Conditional paths**:

- If [event] → [Alternative branch]
- If [event] → Escalate to [authority level]

**Immediate Actions (0-30 days)**:

1. [Action + owner + deadline]
2. [Action + owner + deadline]
3. [Action + owner + deadline]

**Near-Term Actions (30-90 days)**:

1. [Action]
2. [Action]

---

## Quality and Audit Trail

[Glass Box YAML block — see template above]
```

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis developed for the Legalcode
litigation skill collection, integrating structural patterns from `legalcode-early-case-assessment`
(procedural leverage mapping, element-level merits), `legalcode-damages-calculation`
(damages methodology, multiplier analysis), `legalcode-settlement-negotiation` (decision
tree probability modeling, BATNA/WATNA economics), and `legalcode-legal-risk-assessment`
(enterprise risk scoring, playbook configuration, ISO 31000 alignment). Legal research
informed by primary sources on US expected value litigation analysis, UK Woolf/Jackson
proportionality reforms, Australian Federal Court Act s.37M, and EU antitrust and trade
secrets directives. All statutory references marked [VERIFY] where not confirmed against
current authoritative sources.
