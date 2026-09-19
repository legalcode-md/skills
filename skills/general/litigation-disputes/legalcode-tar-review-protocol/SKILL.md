---
name: legalcode-tar-review-protocol
description: Design, validate, and document Technology-Assisted Review (TAR) and Continuous Active Learning
  (CAL) protocols for litigation document review with full defensibility documentation. Use when designing
  a predictive coding workflow, selecting between TAR 1.0 and TAR 2.0/CAL, structuring seed set methodology,
  planning elusion testing and statistical validation, documenting proportionality under FRCP 26(b)(1),
  integrating privilege screens, building issue coding hierarchies, or preparing a defensibility report
  for production. Also use when reviewing an opposing party's TAR protocol for objections, responding
  to court questions about review methodology, or preparing a joint protocol stipulation. Produces a complete
  TAR Protocol Document with statistical confidence levels and court-ready defensibility report. US federal/state
  primary; UK/AU markers included.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode TAR Review Protocol

> **Disclaimer**: This skill provides a framework for AI-assisted design and documentation
> of Technology-Assisted Review (TAR) and Continuous Active Learning (CAL) protocols for
> litigation eDiscovery. It does not constitute legal advice or procedural guidance. All
> outputs should be reviewed by qualified litigation counsel licensed in the relevant
> jurisdiction and, where applicable, a certified eDiscovery professional, before
> implementation. Rules of civil procedure, local rules, and standing orders change; verify
> current applicability before relying on any provision described here. Case law and
> procedural references cited from memory carry hallucination risk — verify against
> authoritative sources, current court rules, and vendor documentation before relying on
> them. Statistical thresholds described here are guidelines, not mandatory minimums; courts
> apply proportionality analysis case by case.

## Purpose and Scope

This skill designs and documents TAR/CAL protocols for defensible litigation document
review. It selects the appropriate technology approach for the document corpus, builds the
seed set and training methodology, designs statistical validation including elusion testing,
integrates privilege screen workflows, structures issue coding hierarchies, documents FRCP
26(b)(1) proportionality, and produces a complete defensibility report with confidence
levels meeting court acceptance standards per Da Silva Moore (2012), Rio Tinto (2015),
Livingston (2020), and Lawson (2020).

**Covers:**

- TAR 1.0 (predictive coding) vs. TAR 2.0 (Continuous Active Learning / CAL) selection
- Seed set construction: size, SME selection, document sampling, richness assessment
- Training round procedures: iteration design, stopping criteria, performance tracking
- Statistical validation: control set design, elusion testing, precision/recall metrics
- Quality control checkpoints: periodic sampling, reviewer consistency, corrective action
- Privilege screen integration: pre-TAR/parallel/post-TAR workflows, FRE 502(d) orders
- Issue coding hierarchy design: responsiveness vs. issue separation, multi-label strategy
- FRCP 26(b)(1) proportionality documentation: 6-factor analysis, cost-benefit framework
- Defensibility report production: statistical confidence levels, chain of custody, audit trail
- Opposing-party protocol review: objection identification and response strategy
- Joint stipulation drafting: vendor-neutral protocol language, dispute-resolution mechanism
- Generative AI integration considerations: LLM review, privilege risks, validation updates
- UK e-disclosure (Pyrrho standard) and Australian Federal Court annotations

**Does not:**

- Draft discovery requests or responses (see `legalcode-discovery-request-drafter`)
- Conduct the actual document review or operate TAR software
- Provide legal advice or replace counsel, eDiscovery professionals, or statisticians
- Apply exclusively to any single jurisdiction — US federal primary; jurisdictional markers
  for state court, UK, and AU variations
- Guarantee court acceptance of any specific recall or precision threshold

## Jurisdiction and Governing Law

This skill is US-federal-primary with jurisdiction-specific markers for state courts, the
United Kingdom, and Australia.

**US Federal Standard**: FRCP 26(b)(1) proportionality governs discovery scope. TAR is an
accepted methodology when transparent, documented, and proportional. No mandatory recall
threshold exists; courts analyze case-specific proportionality.

[JURISDICTION-SPECIFIC — US State Courts]: Many states have adopted discovery rules
mirroring the 2015 FRCP amendments. California (CRC 3.1000-3.1020), New York (CPLR
3101), and Texas (TRCP 196) each have unique e-discovery provisions. Verify applicable
state rules before finalizing any protocol.

[JURISDICTION-SPECIFIC — United Kingdom]: The Pyrrho standard governs TAR in English
proceedings. _Pyrrho Investments Ltd v MWB Property Ltd_ [2016] EWHC 256 (Ch) established
that TAR is permissible under CPR 31 where proportionate and agreed or court-approved.
The Disclosure Pilot (CPR PD 51U, now transitioning to CPR Part 57AD) requires Enhanced
Disclosure and Technology Questionnaires. UK practitioners should follow the Pyrrho
checklist (10 factors) rather than the US FRCP framework.

[JURISDICTION-SPECIFIC — Australia]: The Federal Court of Australia's Practice Note CM 5
and Technology in Litigation guidelines permit TAR with court approval. The Australian
eDiscovery standard (AS 5037-2008, under review) and the ALRC Report 131 provide framework
guidance. [VERIFY] current FCA Practice Notes before implementing TAR in Australian
proceedings.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
case strategy or methodology preferences, the workflow pauses and asks when:

- The choice would materially affect protocol design (e.g., TAR 1.0 vs. CAL changes the
  entire seed set and validation architecture)
- Case-specific proportionality factors need to be established before statistical thresholds
  can be recommended
- Privilege exposure is case-specific and requires counsel judgment
- The stage of the matter affects which protocol elements are negotiable vs. fixed
- Local rules or judge-specific standing orders may override the general framework

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

- **Describe the matter**: Provide case details (jurisdiction, document volume, custodians,
  case type, discovery request scope, budget, timeline)
- **Protocol to review**: Upload or paste an existing TAR protocol for defensibility review
- **Scenario**: Describe a specific TAR design challenge (e.g., "low-richness dataset,
  opposing counsel demanding 95% recall")
- **Dispute-specific**: Request help drafting objections to an opposing-party protocol or
  preparing a joint stipulation

If no input is provided, prompt the user to supply case details.

### Step 2: Gather Context

**⟁ CLARIFY** — Before designing the protocol, ask the user these questions. Present
as structured options where possible:

1. **What is your role in this matter?**
   - Options: Producing party (designing own protocol), Receiving party (reviewing opponent's
     protocol), Both parties in a joint protocol, Outside counsel advising on protocol,
     eDiscovery consultant, Court-appointed neutral
   - _Why this matters_: The role determines whether the skill focuses on protocol design,
     protocol review, or joint drafting. A producing-party protocol is optimized for
     defensibility; a receiving-party review focuses on objection identification.

2. **What is the approximate document volume?**
   - Options: Under 50,000 documents, 50K–500K, 500K–5 million, Over 5 million
   - _Why this matters_: Volume drives the choice between TAR 1.0 and CAL, seed set size,
     and number of training rounds. TAR 2.0/CAL is generally superior for all volumes but
     especially effective for low-richness collections.

3. **Has a court order or ESI stipulation been entered?**
   - Options: No order yet (designing fresh), Existing order governs (protocol must comply),
     Order required before production (submit for approval), Joint protocol being negotiated
   - _Why this matters_: An existing court order or scheduling order may mandate specific
     protocol elements, transparency requirements, or validation metrics.

4. **What is the estimated richness (% responsive documents)?**
   - Options: Very low (<5%), Low (5–15%), Medium (15–40%), High (>40%), Unknown
   - _Why this matters_: Richness fundamentally affects seed set construction, training
     efficiency, elusion testing sample size, and recall achievability. Very low richness
     requires special handling.

5. **Has opposing counsel cooperated on the TAR methodology?**
   - Options: Full cooperation (joint protocol), Partial cooperation (agreed on some points),
     No cooperation yet, Adversarial (dispute anticipated), Opposing party objecting to TAR
   - _Why this matters_: Cooperation level affects transparency requirements, protocol
     negotiation strategy, and whether a court order or stipulation is preferable.

If the user provides partial context, proceed with stated assumptions and note them
explicitly. For batch/non-interactive runs, assume producing-party role, medium volume
(500K–5M), no order yet, unknown richness, and partial cooperation.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Identify the applicable procedural framework before designing any protocol elements.

1. **Confirm the jurisdiction**: Federal district, state court, UK, AU, or multi-jurisdiction
   parallel proceedings.

2. **Research the applicable rules** using **legalcode-mcp** (if connected):
   - Applicable discovery rules (FRCP 26, 34, 37; or state equivalents)
   - Any standing orders from the assigned judge on ESI and TAR
   - Recent TAR case law in the circuit or district
   - Scheduling order requirements for discovery methodology disclosure

3. **Save results** to a local reference file: `/tmp/legalcode-tar-authority.md` structured as:

   ```markdown
   # Legal Authority Reference — TAR Protocol

   ## Jurisdiction: [court/district]

   ## Date Gathered: [date]

   ### Procedural Rules

   - [Rule, current text, relevance to TAR protocol design]

   ### Applicable Case Law

   - [Case, citation, key holding for this protocol]

   ### Judge-Specific Orders or Preferences

   - [Judge, standing order, citation, requirement]

   ### Agreed ESI Protocol or Protective Order

   - [Any existing stipulation or court order on point]
   ```

4. **Use this file throughout the design**. Mark any citation sourced from legalcode-mcp
   as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark every procedural and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the key authority compiled in this skill, but flag for counsel verification

**⟁ CLARIFY** — If any of the following are true, ask before proceeding:

- **No judge or district identified**: Ask which court; different judges in the same
  district may have materially different TAR preferences.
- **Multiple coordinated proceedings**: Ask whether a single master protocol governs
  or each case has its own requirements.

### Step 4: Select the TAR Approach

Evaluate the case facts against the selection criteria table and recommend the appropriate
TAR approach.

#### TAR 1.0 vs. TAR 2.0 (CAL) Selection Criteria

| Factor                  | TAR 1.0 (Predictive Coding)                                    | TAR 2.0 / CAL (Continuous Active Learning)                         |
| ----------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Training model**      | Fixed phases; training ends before review                      | Continuous; training and review run simultaneously                 |
| **Seed set**            | Required: 500–5,000+ docs; SME-coded before review             | Reduced; algorithm prioritizes likely-relevant docs first          |
| **Minimum corpus**      | Typically ≥50,000 documents to train effectively               | Can operate on corpora as small as 500 documents                   |
| **Richness**            | Struggles with very low richness (<5%); larger seed set needed | More efficient for low-richness corpora                            |
| **SME involvement**     | Concentrated at training phase; then review team takes over    | Distributed throughout; SME available for continuous feedback      |
| **Stopping criterion**  | Statistical: when precision/recall plateaus on control set     | Functional: when marginal yield from additional review is low      |
| **Validation**          | Large control set required (500+ docs); elusion test at end    | Elusion test still required; control set smaller                   |
| **Court acceptance**    | Well-established; Da Silva Moore (2012), Rio Tinto (2015)      | Accepted and growing; Livingston (2020) [VERIFY state courts]      |
| **Transparency burden** | Seed set contents often subject to disclosure demands          | Less transparent by design; may increase opposing-counsel scrutiny |
| **Best for**            | Large corpora, high richness, where training phases workable   | Most corpora; preferred by Grossman-Cormack research (2014)        |

**Recommendation logic:**

- **Use TAR 2.0/CAL** when: corpus is any size, richness is unknown or low, budget
  favors efficiency, or matter timeline is compressed.
- **Use TAR 1.0** when: opposing counsel insists on seeing the seed set, court has
  specifically approved TAR 1.0 in a prior order, or platform limitations require it.
- **Hybrid approach**: Start with CAL for responsiveness screening; apply TAR 1.0 control
  set validation methodology for statistical validation.

**⟁ CLARIFY** — If the document volume is under 50,000 or the richness is likely above
40%, ask whether TAR is necessary at all versus keyword search with manual review:

- Very small corpora may not produce statistically valid TAR results
- Very high richness may make manual review equally efficient
- Present cost-benefit comparison before committing to TAR

### Step 5: Design the Seed Set and Training Methodology

#### 5a. Data Population Definition

Before constructing the seed set, define the document population precisely:

1. **Total document count**: Post-deduplication, post-NIST-filter, and post-date-range-cull
2. **Custodians**: Full custodian list with document counts per custodian
3. **Source systems**: Email server, shared drives, messaging platforms (Slack/Teams),
   databases, hard copy scans
4. **Date range**: Start and end dates for collection; any date-range exclusions
5. **Exclusions already applied**: System files, privileged-domain emails, previously
   produced documents, family-level deduplication decisions
6. **Richness estimation**: Estimated percentage of responsive documents; basis for estimate

Document these definitions in the Protocol: **Section III — Data Population Definition**.

#### 5b. Seed Set Construction

**TAR 1.0 Seed Set:**

| Parameter               | Requirement                                                            | Notes                                                           |
| ----------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Minimum size**        | 500–1,000 documents                                                    | Larger seed sets reduce bias risk                               |
| **Construction method** | Random stratified sample OR keyword-guided selection                   | Random preferred for statistical validity                       |
| **SME selection**       | Senior attorney or domain expert with deep matter knowledge            | Must understand what "responsive" means for each request        |
| **SME qualification**   | Document: education, bar admission, matter role, eDiscovery experience | Required for chain of custody                                   |
| **Richness target**     | Seed set richness should approximate corpus richness (±10%)            | Over-seeding with responsive docs biases algorithm              |
| **Independence**        | Seed documents excluded from control/validation set                    | Same documents should not be used for both training and testing |
| **Documentation**       | Log: document IDs, coding decisions, SME name, date, coding rationale  | Required for defensibility report                               |

**TAR 2.0 / CAL Seed Set:**

- Begin with attorney query (issue description), a small number of known-relevant documents
  (as few as 1–10), or a short keyword search to identify initial training documents
- No large pre-coded seed set required; the algorithm starts prioritizing based on initial
  relevance signals and continuously updates
- **SME Availability**: SME must be available throughout the review, not just at initiation

**Richness Challenges — Very Low Richness (<5%):**

- Standard random sampling will yield few relevant documents per training round
- **Mitigation options**:
  1. Pre-filter with broad keyword search before TAR to increase working richness
  2. Use CAL (better suited to low richness than TAR 1.0)
  3. Increase seed set size significantly for TAR 1.0 (2,000–5,000 documents)
  4. Document the richness limitation prominently in the proportionality analysis

**⟁ CLARIFY** — If the corpus is very large (>1M documents) and the estimated richness
is below 5%, ask whether a pre-culling approach (keywords + date + custodian filters before
TAR) is preferable to pure TAR to manage cost and improve training quality.

#### 5c. Training Round Design (TAR 1.0)

| Round Parameter         | Design Decision                                                               | Documentation Requirement                              |
| ----------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Rounds planned**      | Typically 3–10+ rounds, depending on performance curve                        | Log number of rounds anticipated; actual may vary      |
| **Documents per round** | 200–1,000 for precision; reduce as performance plateaus                       | Log per-round document count                           |
| **Performance metric**  | Precision/recall measured against control set after each round                | Log metrics per round; target plateau identification   |
| **Stopping criterion**  | Recall improvement per round falls below threshold (e.g., <2%) on control set | Document the specific stopping rule adopted            |
| **Control set**         | Random sample of 500+ documents; SME-coded as "gold standard"                 | Separate from seed set; not used for training          |
| **Overfitting check**   | Monitor precision; if falls while recall rises, may be overfitting            | Document any overfitting signals and corrective action |

### Step 6: Design Statistical Validation

#### 6a. Control Set (TAR 1.0)

The control set is the held-out "gold standard" against which TAR performance is measured:

| Parameter         | Requirement                                                                             |
| ----------------- | --------------------------------------------------------------------------------------- |
| **Size**          | Minimum 500 documents; 1,500+ preferred for ±2% margin at 95% CI                        |
| **Construction**  | Random sample from the full corpus (not from seed set)                                  |
| **Review**        | SME-reviewed and coded before TAR training begins                                       |
| **Coding**        | Binary: responsive / non-responsive (+ privileged flag)                                 |
| **Re-review**     | Control set reviewed after each training round; results compared to TAR classifications |
| **Documentation** | Log: document IDs, SME coding, date, any disagreements resolved                         |

Control set metrics to track per round:

- **Precision**: Fraction of TAR-identified responsive documents that are actually responsive
  (per control set ground truth)
- **Recall**: Fraction of control-set-responsive documents that TAR correctly identified
- **F1 Score**: Harmonic mean of precision and recall (optional; useful for optimization)
- **Learning curve**: Plot of recall vs. training rounds to identify plateau point

#### 6b. Elusion Testing

Elusion testing validates that the "null set" (documents TAR marked non-responsive that
will not be reviewed) does not contain a material proportion of relevant documents.

**Elusion Test Design:**

| Parameter                      | Standard                                                                         | Source                                      |
| ------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------- |
| **Confidence level**           | 95%                                                                              | Industry standard; Lawson, court acceptance |
| **Margin of error**            | ±2% (preferred) or ±5% (proportionally acceptable)                               | ACEDS; EDRM TAR Guidelines 2019             |
| **Sample size at ±2%, 95% CI** | ~1,533 documents                                                                 | Normal approximation formula                |
| **Sample size at ±5%, 95% CI** | ~385 documents                                                                   | Normal approximation formula                |
| **Sample selection**           | Random stratified sample of null-set documents                                   | Must be random; not convenience sample      |
| **Review standard**            | SME-reviewed against the same responsiveness definition used throughout          | Consistency critical                        |
| **Acceptance threshold**       | Elusion rate consistent with achieved recall (e.g., if recall=80%, elusion ~20%) | No universal bright-line; case-specific     |

**Sample Size Calculation (to include in protocol):**

```
n = (Z² × p × (1-p)) / e²

Where:
  n = required sample size
  Z = Z-score for confidence level (1.96 for 95% CI)
  p = estimated prevalence (use 50% for conservative maximum)
  e = margin of error (0.02 for ±2%, 0.05 for ±5%)

At p=0.50, 95% CL, ±2% margin: n ≈ 2,401 (conservative)
At p=0.50, 95% CL, ±5% margin: n ≈ 385 (conservative)
```

**Elusion Test Results Interpretation:**

| Elusion Rate | Interpretation                           | Action                                                            |
| ------------ | ---------------------------------------- | ----------------------------------------------------------------- |
| ≤ 5%         | Low elusion; strong recall               | Document and proceed to production                                |
| 6–15%        | Moderate elusion; assess proportionality | Conduct additional targeted review of high-confidence null docs   |
| 16–30%       | High elusion; below-standard recall      | Additional training rounds or expanded review; document rationale |
| > 30%        | TAR likely not performing adequately     | Halt and reassess protocol; consider keyword supplementation      |

**⟁ CLARIFY** — If the elusion rate falls between 6–30%, present the following options
before deciding on next steps:

- "The elusion rate is [X]%. This means approximately [X]% of responsive documents may
  remain in the null set. Options: (1) Accept this elusion rate and document the
  proportionality rationale — case-specific factors may justify this; (2) Conduct additional
  training rounds to improve recall; (3) Manually review the high-confidence null documents
  identified above a risk threshold. Which approach is proportionate for this matter?"

#### 6c. Precision and Recall Framework

**Terminology (use consistently throughout the protocol):**

| Term                 | Definition                                            | Formula                                       |
| -------------------- | ----------------------------------------------------- | --------------------------------------------- |
| **Recall**           | % of all responsive documents found by TAR            | Relevant found ÷ Total relevant in corpus     |
| **Precision**        | % of TAR-identified docs that are actually responsive | Relevant identified ÷ Total identified by TAR |
| **Elusion**          | % of responsive docs that ended up in the null set    | 1 − Recall                                    |
| **Richness**         | % of corpus that is responsive                        | Total responsive ÷ Total corpus               |
| **Recall@threshold** | Recall at a specific TAR confidence cutoff            | Calculated per cutoff setting                 |

**Accepted Recall Thresholds (case law):**

- 75–80% recall: Found acceptable in multiple federal courts (case-specific proportionality)
- 85% recall: Upper bound enforced in _Lawson v. Spirit AeroSystems_ before cost-shifting
- No mandatory minimum; courts apply Rule 26(b)(1) proportionality analysis
- "A party cannot insist on 100% recall — such a standard does not exist even in manual
  review" (_Hyles v. New York City_, 2016) [VERIFY exact quote]

**Documenting the Chosen Threshold:**

The protocol must justify the chosen recall target with the Rule 26(b)(1) proportionality
analysis (see Step 8). Never present the recall threshold as a technical default; present
it as a reasoned proportionality determination.

### Step 7: Integrate Privilege Screen

Privilege review must be integrated into the TAR workflow before training data contaminates
the algorithm with privileged communications.

#### Privilege Screen Workflow Options

| Approach                      | When Used                              | Advantage                                      | Risk                                   |
| ----------------------------- | -------------------------------------- | ---------------------------------------------- | -------------------------------------- |
| **Pre-TAR privilege filter**  | Preferred when counsel list is known   | Ensures privileged docs excluded from training | May miss privilege if list incomplete  |
| **Parallel review**           | Large privilege universe               | Simultaneous responsiveness + privilege coding | Requires coordinated workflows         |
| **Post-TAR privilege screen** | When TAR runs on responsiveness only   | Simple TAR; clean separation                   | Privileged docs may be in training set |
| **Integrated coding**         | CAL platforms that support multi-label | Efficiency                                     | More complex; CAL performance may vary |

**Recommended Workflow (Pre-TAR Privilege Filter + Post-TAR Privilege Screen):**

1. **Pre-filter step**: Extract all documents from known privilege domains (attorney email
   domains, legal hold folders, outside counsel servers). Mark as "privilege review required"
   and exclude from TAR training universe.

2. **TAR runs on culled corpus**: Produce responsive/non-responsive classifications on the
   non-privilege-filtered corpus.

3. **Post-TAR privilege review**: TAR-designated responsive documents go through privilege
   review before production. Privileged documents logged on privilege log.

4. **FRE 502(d) Order**: Always seek a Rule 502(d) clawback order before production. This
   eliminates the need to prove "reasonable precautions" under Rule 502(b) if privileged
   documents are inadvertently produced.

**FRE 502(d) Order — Required Protocol Element:**

```
REQUIRED Protocol Language: "The parties have agreed and the Court has entered an Order
pursuant to FRE 502(d) providing that the production of any privileged or work-product
protected document shall not constitute a waiver of any privilege or protection. [Party A]
will promptly notify [Party B] of any inadvertently produced privileged document within
[X] business days of discovery. Upon notification, [Party B] will promptly return or
destroy the document and shall not retain any copies or use the document in any way."
```

[JURISDICTION-SPECIFIC — UK]: UK proceedings do not have a direct FRE 502(d) equivalent.
Parties may rely on CPR 31.20 (inadvertent disclosure) and agree clawback terms in the
Disclosure Review Document or an agreed confidentiality order. [VERIFY] current practice.

**2025-2026 AI Privilege Warning**: Using third-party generative AI tools (e.g.,
consumer-level ChatGPT, Gemini) to process documents may waive attorney-client privilege
by disclosing to a non-agent third party (per _U.S. v. Heppner_, S.D.N.Y. 2025; [VERIFY]
as developing law). Any TAR platform using third-party LLM APIs must be vetted by counsel
for privilege implications before processing privileged documents.

### Step 8: Document Proportionality Under FRCP 26(b)(1)

The protocol must contain a standalone proportionality analysis. This is the primary
defense against challenges to TAR costs, recall targets, and scope decisions.

#### Rule 26(b)(1) Six-Factor Analysis

Apply each factor explicitly to the matter:

| Factor                          | Analysis Questions                                                            | Protocol Documentation                                                           |
| ------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **1. Importance of issues**     | Is this case high-stakes (constitutional, class action, significant damages)? | Describe the issues; note relevance to discovery scope                           |
| **2. Amount in controversy**    | What is the damages claim or injunctive value?                                | State amount; note proportional discovery budget                                 |
| **3. Parties' relative access** | Does only the producing party have the documents?                             | Describe access asymmetry; note custodian list                                   |
| **4. Parties' resources**       | Do parties have comparable or asymmetric resources?                           | Note resource disparity if relevant; affects cost-shifting risk                  |
| **5. Importance of discovery**  | Are these documents central or peripheral to the claims?                      | Describe how reviewed documents will be used at trial or for dispositive motions |
| **6. Burden vs. benefit**       | Does TAR cost match the litigation value?                                     | Provide estimated TAR cost vs. estimated value of discovery yield                |

**Recall Threshold Proportionality Justification:**

The chosen recall target must be tied to the proportionality analysis. Use this framework:

```markdown
## Proportionality-Based Recall Determination

**Documents in corpus**: [number]
**Estimated richness**: [%]
**Estimated responsive documents**: [number] (corpus × richness)
**Recall target**: [%]
**Estimated responsive documents to be found**: [number] (responsive × recall)
**Estimated responsive documents remaining in null set**: [number]
**TAR estimated cost**: $[amount]
**Manual review alternative cost**: $[amount]
**TAR cost savings**: $[amount] ([%] reduction)

**Proportionality finding**: At [X]% recall, TAR will identify approximately [number]
responsive documents. The cost of achieving [X+5]% recall (additional training rounds
and elusion testing) would be approximately $[additional cost], producing an estimated
[additional documents] additional responsive documents. Under Rule 26(b)(1), this
additional cost is [proportionate / not proportionate] to the likely benefit given
[case-specific factors].
```

**Cost-Shifting Risk**: _Lawson v. Spirit AeroSystems_ (D. Kan. 2020) established that
courts may shift TAR costs to the requesting party when: (1) achieved recall is reasonable
(85% in that case), (2) the responsive yield from additional review is low (3.3%), and
(3) further review costs are disproportionate to benefit. Document these metrics throughout
the review to preserve cost-shifting arguments.

### Step 9: Design Issue Coding Hierarchy

Issue coding layers additional analytical depth onto the responsiveness determination
produced by TAR.

#### Responsiveness vs. Issue Coding Separation

| Layer                         | Function                                                                  | TAR Integration                                   |
| ----------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------- |
| **Layer 1 — Responsiveness**  | Is this document responsive to any discovery request? (binary)            | TAR primary output                                |
| **Layer 2 — Request Mapping** | Which specific discovery request(s) is this responsive to?                | Post-TAR; manual coding against request list      |
| **Layer 3 — Issue Coding**    | Which legal issues does this document bear on?                            | Post-TAR; using separate algorithm pass or manual |
| **Layer 4 — Hot Documents**   | Is this document particularly significant (admission, key communication)? | Human SME judgment; cannot be fully automated     |

**Recommended separation**: Run TAR on Layer 1 only. Apply Layers 2–4 as post-TAR
workflows. This keeps the TAR training objective clean (responsiveness) and avoids
multi-label complexity degrading algorithm performance.

#### Issue Code Design Principles

1. **Mutually exclusive at same level**: Each document should be codeable to exactly one
   node at each level of the hierarchy (though a document may map to multiple issues)
2. **Exhaustive**: Every responsive document fits somewhere in the hierarchy
3. **Concrete definitions**: Each issue code has a written definition that reviewers can
   apply consistently
4. **Hierarchy maximum depth**: No more than 3 levels (parent → category → specific issue)
   to maintain reviewer consistency
5. **Verification sampling**: After issue coding, sample 5–10% of coded documents per
   issue to verify consistency

**Sample Issue Code Structure (contract dispute):**

```
Responsiveness (Layer 1)
├── Contract Formation
│   ├── Offer and Acceptance
│   ├── Consideration
│   └── Authority to Contract
├── Breach
│   ├── Performance Obligations
│   ├── Non-Performance Evidence
│   └── Excuse and Justification
├── Damages
│   ├── Actual Damages Evidence
│   ├── Mitigation Evidence
│   └── Causation Evidence
└── Communications
    ├── Internal Communications
    ├── External Communications
    └── Board/Executive Level
```

**Multi-Label TAR Limitations**: If the case requires TAR to classify documents against
multiple simultaneous issues (not just responsiveness), note in the protocol that:

- Current TAR algorithms are optimized for single-label classification
- Multi-label TAR requires either separate TAR projects per issue (expensive) or hybrid
  manual + TAR approach
- Discuss with your platform vendor before committing to multi-label TAR

**⟁ CLARIFY** — For matters with complex multi-issue discovery (e.g., class action with
10+ distinct claim types), ask whether the issue hierarchy should be addressed in the
initial protocol or deferred to a second-phase workflow document after TAR responsiveness
screening is complete.

### Step 10: Define Quality Control Checkpoints

#### QC Checkpoint Schedule

| Checkpoint                  | Trigger                                 | What to Review                                                                   | Documentation                                    |
| --------------------------- | --------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Baseline QC**             | Before training begins                  | Seed set consistency; SME coding accuracy; platform configuration                | Log: seed set QC report                          |
| **Mid-training QC**         | After every 3 training rounds (TAR 1.0) | Precision/recall curve; any divergence from expected performance                 | Log: per-round metrics                           |
| **Interim elusion test**    | At 50% of estimated review (CAL)        | Early elusion sampling to confirm trajectory                                     | Log: interim elusion report                      |
| **Reviewer consistency QC** | Every 50,000 documents reviewed         | Random sample 100–200 documents re-reviewed by SME                               | Log: consistency rate; corrective action if <95% |
| **Final elusion test**      | Before production cut                   | Full elusion test per Section 6b                                                 | Log: final elusion report                        |
| **Pre-production QC**       | Before first production                 | Review sample of production set for privilege, confidentiality, and issue coding | Log: pre-production QC report                    |

**Corrective Action Protocol:**

- If reviewer consistency falls below 95%: pause production, re-calibrate reviewers,
  re-review disputed documents, document root cause
- If interim elusion rate is unexpectedly high: add training rounds, investigate seed set
  quality, consider SME re-involvement, document corrective steps
- If TAR performance plateaus early: investigate data quality issues, check for duplicate
  document problems, verify that culling did not over-exclude

### Step 11: Assess Protocol Defensibility

Apply the Defensibility Classification framework to every material protocol design decision.

#### Protocol Defensibility Classification

### DEFENSIBLE — Meets Court Standards

Protocol elements that align with established case law, professional guidance (EDRM,
Sedona Conference), and are unlikely to draw successful challenge.

**Characteristics:**

- Seed set constructed via documented methodology with qualified SME
- Elusion testing at 95% CI / ±2-5% margin of error
- Recall target proportionate to case needs per Rule 26(b)(1) analysis
- Privilege screen workflow documented with FRE 502(d) order
- Training rounds and stopping criteria documented with performance metrics
- Opposing counsel notified of TAR use and protocol disclosed in advance
- Control set held out from training; reviewed by qualified SME

**Examples:**

- CAL protocol with 80% recall, 95% CI / ±5% elusion test, proportionality analysis
  citing Lawson ($750K case value, 3.3% yield from additional review)
- Seed set of 1,000 randomly selected documents, SME-reviewed, chain of custody documented
- FRE 502(d) order entered; privileged domains pre-filtered before TAR training

**Action**: Document and proceed.

### REQUIRES REVISION — Needs Strengthening Before Finalization

Protocol elements that are common in practice but may draw challenge and should be
improved before submitting to court or disclosing to opposing counsel.

**Characteristics:**

- Elusion testing at ±5% CI where ±2% would be more defensible and proportionate
- Recall target not yet tied to specific Rule 26(b)(1) proportionality analysis
- SME qualifications documented but thin (one review matter, no formal eDiscovery training)
- Control set constructed but smaller than 500 documents
- Training stopping criterion stated but not precisely defined (e.g., "when performance
  is adequate" rather than specific metric)
- No FRE 502(d) order yet (intent to pursue but not completed)
- Issue coding hierarchy designed but definitions not yet written for each code

**Examples:**

- Protocol states 75% recall target with no FRCP 26(b)(1) analysis to justify it
- Elusion testing planned but sample size not specified
- Privilege screen described as "standard attorney review" without specifics

**Action**: Identify each element needing strengthening; provide revised protocol language.

### NON-DEFENSIBLE — Fails Professional Standards

Protocol elements that are materially deficient, likely to draw successful challenge,
and must be corrected before use.

**Characteristics:**

- No elusion testing planned or discussed
- No documented stopping criterion for training; training ended "when team felt ready"
- Seed set constructed entirely by junior reviewers without SME involvement
- Privileged documents included in training set without segregation protocol
- Recall target stated as "as high as possible" without any metric or measurement
- No proportionality analysis; protocol treats TAR as unlimited discovery obligation
- Opposing counsel not notified of TAR use despite agreed ESI protocol requiring disclosure
- Production made from TAR without pre-production QC or privilege review

**Examples:**

- Protocol states only: "We used predictive coding. All responsive documents were reviewed."
- No chain of custody for seed set; SME not identified; training rounds not documented
- Elusion test run with convenience sample (not random); results not documented

**Action**: Halt production pending remediation. Identify specific deficiencies. Provide
corrective protocol language for each.

### Step 12: Draft Protocol Document

Using all prior steps, produce the complete TAR Protocol Document following the template
in the **Output Format Template** section below.

**⟁ CLARIFY** — Before drafting, confirm:

- Is this a producing-party internal protocol, a joint stipulation for court filing, or
  an objection memorandum responding to an opposing-party protocol?
- Should the protocol be written in neutral technical language (court filing) or advocacy
  framing (brief defending protocol)?
- Is there a page limit from the court or opposing counsel?

### Step 13: Quality Verification

Before delivering any protocol document or defensibility analysis, run the quality
checks in the **Quality Assurance Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For any NON-DEFENSIBLE-classified element, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material statistical threshold stated.
4. Verify that all 14 Protocol Document sections have been addressed (present or noted
   as not applicable with justification).
5. Generate the Glass Box Audit Trail and append to the output.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                 | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific case, rule, or established principle                              | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow consistent, recognizable legal citation format                                  | Fix format                                               |
| **Currency**   | Every cited provision checked for subsequent history, amendments, or repeal                          | Flag "[CHECK CURRENCY — verify current version]"         |
| **Domain**     | Analysis stays within the applicable jurisdiction and procedural framework                           | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. Statistical thresholds presented as guidelines, not rules | Add confidence qualifier                                 |

### Self-Interrogation for NON-DEFENSIBLE Items

For any protocol element classified as NON-DEFENSIBLE, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the deficiency assessment follow logically from
the cited authority? Would a court in this jurisdiction actually strike this protocol
element? Are there remediation steps that could cure the deficiency before challenge?

**Pass 2 — Completeness**: Have all relevant case law, procedural rules, and professional
guidance been considered? Are there alternative protocol designs that achieve similar
efficiency while addressing the deficiency? Have cost-shifting implications been analyzed?

**Pass 3 — Challenge**: What is the strongest argument that this protocol element IS
defensible? Under what circumstances (case complexity, document volume, proportionality
factors) might a court accept this approach? Is the NON-DEFENSIBLE classification
proportionate, or is REQUIRES REVISION more accurate?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material statistical threshold or protocol design decision, assign a confidence
level:

| Level        | Range     | Meaning                                                       | Action                                                |
| ------------ | --------- | ------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled principle; court-accepted; professional consensus     | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions              | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; courts vary by district or case type          | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; developing case law or novel application | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; minority position                    | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Guidance for TAR-Specific Scoring:**

- Recall thresholds: PROBABLE (no universal standard; case-specific)
- Elusion test at 95% CI / ±2-5%: DEFINITE (professional consensus)
- TAR acceptance in federal court: DEFINITE (established since 2012)
- CAL acceptance in state courts: HIGH–PROBABLE (jurisdiction-specific)
- Generative AI as TAR in lieu of supervised learning: POSSIBLE–PROBABLE (emerging)

---

## Severity Classification Summary

| Classification        | Criteria                                                                                                                                               | Action                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| **DEFENSIBLE**        | Meets case law standards (Da Silva Moore, Rio Tinto, Livingston); aligns with EDRM/Sedona guidance; elusion test at 95% CI; proportionality documented | Document; proceed                                            |
| **REQUIRES REVISION** | Acceptable but improvable; likely to draw challenge; statistical threshold present but underdocumented                                                 | Strengthen before disclosure; specific revisions recommended |
| **NON-DEFENSIBLE**    | Fails professional standards; likely to be challenged successfully; must be corrected before production                                                | Halt; remediate; redraft before use                          |

---

## Negotiation Priority Framework

When presenting a joint protocol or defending a disputed protocol element, organize by
negotiation priority:

### Tier 1 — Non-Negotiable (Protocol Integrity)

Protocol elements where deviation creates material defensibility risk:

- Documented elusion testing with statistical sampling (no production without it)
- SME involvement in seed set or ongoing training — not junior-reviewer-only
- FRE 502(d) order or documented clawback agreement before production
- Privilege domain pre-filter and post-TAR privilege review before production
- Written responsiveness definitions; not implicit assumptions
- Chain of custody documentation for seed set and training data

### Tier 2 — Strong Preferences (May Negotiate With Justification)

Protocol elements where the preferred approach is defensible but alternatives exist:

- Specific recall target (75% vs. 80% vs. 85%: all acceptable with proportionality analysis)
- Elusion test margin of error (±2% preferred vs. ±5% acceptable for smaller matters)
- Seed set size (1,000+ preferred vs. 500+ minimum for TAR 1.0)
- Control set disclosure to opposing counsel (disclose metrics, not documents)
- Number of training rounds and stopping criteria granularity

### Tier 3 — Concession Candidates

Protocol elements that are preferable but can be conceded strategically:

- TAR platform identity disclosure (not required if vendor-neutral protocol)
- Specific document identifiers for seed set (may be protected work product)
- Intermediate training metrics (can share final report without per-round disclosure)
- Issue coding hierarchy details (may defer to second-phase document)

**Negotiation strategy**: Lead with Tier 1. Never concede Tier 1 without escalation. Trade
Tier 3 disclosure for Tier 2 flexibility. Frame all concessions in terms of proportionality,
not capitulation.

---

## Localization Notes

### UK — Pyrrho Standard [JURISDICTION-SPECIFIC]

_Pyrrho Investments Ltd v MWB Property Ltd_ [2016] EWHC 256 (Ch) established 10 factors
for TAR approval in English proceedings. UK practitioners must address each:

1. **Reasonableness**: TAR more cost-effective than manual review for this corpus
2. **Proportionality**: Cost proportionate to value of claim under CPR 44.3
3. **Predictive coding = appropriate tool**: Justify why predictive coding suits this data
4. **Protocol agreed**: Parties have cooperated on protocol or court has approved
5. **Transparency**: Both parties understand how the system works
6. **Sampling methodology**: Control set and elusion testing approach
7. **Quality assurance**: How errors will be identified and corrected
8. **Privilege**: How privileged documents are protected
9. **Random sampling check**: Post-production quality check
10. **Reasonable search**: Under CPR 31.7, confirms TAR = reasonable search

[VERIFY] current CPR Part 57AD (Disclosure Pilot successor) requirements before filing.

### Australia [JURISDICTION-SPECIFIC]

Federal Court of Australia's Practice Note CM 5 permits TAR where the Court approves.
Key requirements: (a) early disclosure of proposed TAR methodology; (b) agreed or
court-approved protocol; (c) proportionality assessment. [VERIFY] current FCA practice
notes; guidance has been updated since 2020.

---

## Anti-Patterns

What NOT to do when designing or reviewing TAR protocols:

1. **Treating recall thresholds as industry standards** — There is no universally mandated
   recall percentage. Citing "80% is standard" without a case-specific proportionality
   analysis exposes the protocol to challenge. Always anchor the recall target to the Rule
   26(b)(1) proportionality factors for this specific matter.

2. **Constructing the seed set with junior reviewers** — Seed set quality drives the entire
   TAR 1.0 model. A seed set coded by paralegals or first-year associates without SME
   supervision will produce biased training data. Document SME qualifications for every
   person who touches training documents.

3. **Using the same documents for training and validation** — The control set must be
   entirely independent of the seed set. Using overlapping documents inflates apparent
   precision/recall metrics and produces a false sense of validation quality.

4. **Skipping the elusion test** — Elusion testing is the industry standard for validating
   TAR review completeness. A protocol that omits elusion testing is NON-DEFENSIBLE
   regardless of how well-designed the training was.

5. **Convenience sampling for elusion test** — The elusion sample must be random. Using
   a convenient subset (e.g., "we reviewed the most recently created null documents") does
   not produce statistically valid results and may be challenged as cherry-picking.

6. **No FRE 502(d) order** — Proceeding to production without a clawback order under
   Rule 502(d) requires proving "reasonable precautions" under Rule 502(b) if privilege
   is inadvertently produced. This is an avoidable exposure. Seek the 502(d) order first.

7. **Sending documents to third-party AI tools without privilege analysis** — Using
   consumer-level LLMs (e.g., ChatGPT, Gemini) to process or classify documents may waive
   attorney-client privilege. Verify that any AI-assisted TAR platform is operating as an
   agent of counsel, not a third-party service (see _Heppner_, S.D.N.Y. 2025 [VERIFY]).

8. **Over-representing responsive documents in the seed set** — A seed set that is 50%
   responsive when the corpus is only 5% responsive will bias the algorithm to over-predict
   relevance, inflating precision but reducing recall. Seed set richness should approximate
   corpus richness.

9. **Not disclosing TAR use to opposing counsel** — While parties are not required to use
   TAR (_Hyles_, 2016), failing to disclose TAR use when it is the methodology chosen may
   violate meet-and-confer obligations and damage credibility with the court. Early,
   proactive disclosure is the defensible approach.

10. **Stopping training arbitrarily** — Declaring training "complete" because the team
    ran out of time, budget, or patience, without a documented stopping criterion tied to
    performance metrics, is a common ground for protocol challenge. The stopping criterion
    must be pre-defined and documented in the protocol.

11. **Using TAR for a corpus that is too small** — TAR 1.0 requires sufficient documents
    to train a statistically reliable model. For TAR 1.0 on corpora under 50,000 documents,
    the statistical foundation may be insufficient. Use CAL, keyword search with sampling,
    or manual review instead.

12. **Claiming TAR produced "all" relevant documents** — TAR does not guarantee 100%
    recall. Claiming in a certification that all responsive documents have been reviewed
    and produced misrepresents what TAR achieves. Use precise language: "TAR identified
    responsive documents with an estimated recall of [X]% at a 95% confidence level."

13. **Not monitoring reviewer consistency** — TAR is only as good as the consistency of
    the humans coding training documents. If two reviewers disagree on responsiveness for
    30% of documents, the training signal is corrupted. Build reviewer consistency QC into
    the workflow.

14. **Conflating issue coding with responsiveness coding in TAR training** — Training the
    algorithm on issue codes (not just responsiveness) introduces multi-label complexity
    that degrades performance. Keep TAR focused on responsiveness; apply issue codes as a
    separate post-TAR step.

15. **Ignoring proportionality documentation until challenged** — The proportionality
    analysis under Rule 26(b)(1) must be built into the protocol from the start, not
    retrofitted as a brief when opposing counsel objects. Courts expect proactive
    proportionality analysis; after-the-fact justifications are less persuasive.

16. **Treating protocol templates as fill-in-the-blank exercises** — A TAR protocol that
    copies a template without adapting statistical thresholds, seed set sizes, and
    proportionality analysis to the specific matter is not a defensible document. Every
    material parameter must be justified with case-specific facts.

17. **Omitting limitations and risk disclosures** — A protocol that does not acknowledge
    what TAR cannot detect (privileged documents if pre-filter failed, foreign-language
    documents if not in training set, handwritten records not OCR'd) is incomplete. Courts
    and opposing counsel expect honest limitations statements.

18. **No chain of custody for training data** — Every document in the seed set, control
    set, and SME-reviewed elusion sample must have a documented chain of custody: who
    reviewed it, when, what they coded, and why. Without this, the protocol cannot be
    audited or defended in a discovery dispute.

19. **Assuming court approval is automatic** — While TAR is now widely accepted, courts
    in some districts expect proactive disclosure at the scheduling conference and may
    have judge-specific preferences on protocol disclosure, validation reports, and
    transparency. Research the specific judge and district before finalizing the protocol.

20. **Not updating the protocol when circumstances change** — If the document corpus
    changes materially (new custodians added, date range expanded), the existing TAR
    training may no longer be representative. A protocol amendment may be required; this
    is not automatic.

---

## Writing Standards

Apply plain-language discipline to all TAR protocol documents:

**For protocol text shared with opposing counsel or filed with court:**

- Plain language; avoid eDiscovery jargon when plain alternatives exist
- Active voice: "The producing party will conduct elusion testing" not "Elusion testing will be conducted"
- Short sentences; one point per sentence
- Define all technical terms on first use (TAR, CAL, seed set, elusion, recall, precision)
- Specific, not vague: cite the exact sample size, not "sufficient sampling"
- Quantify every threshold: "95% confidence level, ±2% margin of error" not "high statistical confidence"

**For internal defensibility analysis:**

- Same plain-language standards
- Technical legal analysis may include more terminology
- Every statistical claim backed by formula or citation
- Confidence qualifiers on all recall/precision estimates
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a federal judge unfamiliar with eDiscovery understand the protocol's core methodology?
2. Can opposing counsel identify every material protocol element clearly enough to object
   to specific elements if desired?
3. Is every statistical threshold specified with its confidence level and margin of error?
4. Are any phrases vague or circular (e.g., "appropriate validation")?
5. Does the proportionality analysis address all six Rule 26(b)(1) factors explicitly?

---

## External Tool Integration

### legalcode-mcp (Primary Research Tool)

**With legalcode-mcp connected:**

- In Step 3, search for applicable discovery rules, judge-specific standing orders,
  recent TAR case law in the relevant district or circuit
- Search for any published opinions from the assigned judge on ESI and TAR protocols
- Verify that cited cases have not been overruled or distinguished in the relevant circuit
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Note in Glass Box: `legalcode_mcp: "Not connected"`
- All case law references from memory must be marked [VERIFY]
- Focus on structural protocol design quality rather than case-specific legal authority

### TAR Platforms (Operational Integration)

This skill is vendor-neutral. The protocol document produced here should be transferable
to any of these platforms with no material changes:

| Platform                     | TAR Type         | Notes                                              |
| ---------------------------- | ---------------- | -------------------------------------------------- |
| Relativity (Active Learning) | TAR 2.0 / CAL    | Market leader; extensive court acceptance          |
| DISCO                        | TAR 2.0          | Cloud-native; strong UI; good for mid-size matters |
| Everlaw                      | TAR 2.0          | Collaboration-focused; growing adoption            |
| Reveal (Brainspace)          | TAR 2.0 + GenAI  | AI-enhanced; "aji" feature                         |
| Nuix                         | Processing + TAR | Best-in-class processing; TAR capabilities vary    |

**Platform-Neutral Language**: Write all protocol documents using functional descriptions
(e.g., "continuous active learning with iterative SME feedback") rather than vendor names.
This prevents disputes if the vendor or platform changes, and avoids appearing to endorse
any particular commercial product.

**Graceful Degradation**: If platform-specific features are unavailable (e.g., CAL
algorithm on an older platform), document the fallback approach (e.g., "TAR 1.0 with
10 training rounds using 1,000-document seed set") and confirm this fallback is still
DEFENSIBLE under the applicable standards.

---

## Output Format Template

Use this template for all TAR Protocol Documents:

---

```markdown
# TAR Review Protocol

## [Case Caption]

## [Court and Case Number]

## Protocol Version: [1.0] | Date: [date] | Prepared by: [party or firm]

---

## Executive Summary

[2–3 paragraph summary: why TAR, which approach (TAR 1.0 / CAL), estimated corpus,
target recall, validation approach, timeline.]

---

## Section I — Purpose and Scope

**Scope**: This protocol governs technology-assisted review of ESI produced in response
to [Requesting Party's] [Document Requests Nos. X–Y, dated ___].

**TAR Approach**: [TAR 1.0 predictive coding / TAR 2.0 Continuous Active Learning (CAL)]

**Platforms**: [Vendor-neutral description or specific platform if agreed]

**Not Governed by This Protocol**: [Any documents excluded — e.g., hard copy, structured
data, third-party custodians with separate agreements]

---

## Section II — Legal and Procedural Framework

**Governing Rules**: [FRCP 26(b)(1), applicable local rules, scheduling order reference]

**Court Orders**: [Any ESI order, protective order, or scheduling order governing TAR]

**Authority**: This protocol is designed consistent with the standards articulated in:

- _Da Silva Moore v. Publicis Groupe_, 287 F.R.D. 182 (S.D.N.Y. 2012) [VERIFY]
- _Rio Tinto PLC v. Vale S.A._, 306 F.R.D. 125 (S.D.N.Y. 2015) [VERIFY]
- _Livingston v. City of Chicago_, No. 16 C 10156 (N.D. Ill. 2020) [VERIFY]
- _Lawson v. Spirit AeroSystems, Inc._, 2020 WL 6343292 (D. Kan. 2020) [VERIFY]
- EDRM TAR Guidelines (2019)

---

## Section III — Data Population Definition

| Parameter                     | Value                                         |
| ----------------------------- | --------------------------------------------- |
| Total documents (pre-culling) | [number]                                      |
| Post-deduplication, post-NIST | [number]                                      |
| Custodians                    | [list or number]                              |
| Source systems                | [email / shared drive / messaging / etc.]     |
| Date range                    | [start] to [end]                              |
| Exclusions applied            | [privilege domains, system files, NIST, etc.] |
| Estimated richness            | [%]                                           |

---

## Section IV — TAR Methodology

**Approach**: [TAR 1.0 / TAR 2.0 CAL — with selection rationale]

**Overview**: [2–3 sentence plain-language description of how the algorithm works]

**Training process**: [Seed set construction → training rounds → stopping criterion / or
CAL: initial query → continuous learning → stopping criterion]

---

## Section V — Seed Set Construction

| Parameter                | Value                                                                |
| ------------------------ | -------------------------------------------------------------------- |
| Seed set size            | [number]                                                             |
| Construction method      | [random sample / keyword-guided / other]                             |
| SME name and credentials | [attorney name, bar number, role in matter]                          |
| Coding date(s)           | [date range]                                                         |
| Richness check           | [% responsive in seed set vs. estimated corpus richness]             |
| Document identifiers     | [hash list maintained in chain of custody log — may be work product] |

---

## Section VI — Training Workflow

**TAR 1.0:**

| Round | Documents     | Precision | Recall | Notes                         |
| ----- | ------------- | --------- | ------ | ----------------------------- |
| 1     | [N]           | [%]       | [%]    | Initial training              |
| 2–N   | [N per round] | [%]       | [%]    | [Improvement per round]       |
| Final | [N]           | [%]       | [%]    | Performance plateau confirmed |

**Stopping Criterion**: Training declared complete when recall improvement per round
falls below [X]% on the control set for [N] consecutive rounds.

**TAR 2.0 / CAL:**
[Describe continuous learning; SME review cadence; stopping criterion based on marginal
yield < [X] documents per [N] reviewed]

---

## Section VII — Validation Methodology

### Control Set (TAR 1.0)

- Size: [number] documents
- Construction: Random sample, excluded from seed set
- SME reviewer: [name, credentials]
- Review date: [date]

### Elusion Test

- Confidence level: 95%
- Margin of error: ±[%]
- Sample size: [number] documents (per formula: n = (1.96² × 0.5 × 0.5) / e²)
- Sample selection: Random stratified from null set
- SME reviewer: [name]
- Acceptance criterion: Elusion rate below [%]; consistent with recall target

### Results Summary

| Metric       | Value | CI   | Assessment                     |
| ------------ | ----- | ---- | ------------------------------ |
| Precision    | [%]   | ±[%] | DEFENSIBLE / REQUIRES REVISION |
| Recall       | [%]   | ±[%] | DEFENSIBLE / REQUIRES REVISION |
| Elusion rate | [%]   | ±[%] | DEFENSIBLE / REQUIRES REVISION |

---

## Section VIII — Privilege Integration

**Approach**: [Pre-TAR filter / parallel / post-TAR]

**Privilege domains pre-filtered**: [attorney email domains, legal hold folders, etc.]

**FRE 502(d) Order**: [Entered / Pending / Will be sought before production]
Reference: [Order date/docket number if entered]

**Post-TAR privilege review**: All TAR-designated responsive documents reviewed for
privilege before production. Privilege log to be produced by [date].

---

## Section IX — Quality Control

| Checkpoint           | Trigger                 | Reviewer   | Metrics                  | Status               |
| -------------------- | ----------------------- | ---------- | ------------------------ | -------------------- |
| Baseline QC          | Before training         | [SME]      | Seed set consistency     | [PASS / IN PROGRESS] |
| Mid-training QC      | Every 3 rounds          | [attorney] | Precision/recall curve   | [PASS / IN PROGRESS] |
| Reviewer consistency | Every 50K docs          | [SME]      | Consistency rate ≥ 95%   | [PASS / IN PROGRESS] |
| Final elusion test   | Pre-production          | [SME]      | Elusion rate ≤ [%]       | [PASS / IN PROGRESS] |
| Pre-production QC    | Before first production | [counsel]  | Privilege + issue coding | [PASS / IN PROGRESS] |

---

## Section X — Issue Coding Hierarchy

[Insert issue code tree per Section 9 above]

---

## Section XI — Team Composition

| Role                  | Name                     | Credentials                        | Responsibility                               |
| --------------------- | ------------------------ | ---------------------------------- | -------------------------------------------- |
| Lead counsel          | [name]                   | [bar admission, experience]        | Protocol oversight; production certification |
| TAR project manager   | [name]                   | [CEDS/ACE credentials, experience] | Day-to-day workflow; metrics tracking        |
| Subject matter expert | [name]                   | [credentials, matter knowledge]    | Seed set coding; elusion test review; QC     |
| Review team           | [N attorneys/paralegals] | [qualifications]                   | Document review under supervision            |
| Platform vendor       | [name]                   | [platform, certifications]         | Technical implementation                     |

---

## Section XII — Timeline and Resources

| Milestone                | Estimated Date | Notes                                 |
| ------------------------ | -------------- | ------------------------------------- |
| Seed set coding complete | [date]         |                                       |
| Training complete        | [date]         |                                       |
| Elusion test complete    | [date]         |                                       |
| First production         | [date]         |                                       |
| Substantial completion   | [date]         |                                       |
| Estimated cost (TAR)     | $[amount]      | vs. manual review estimate: $[amount] |

---

## Section XIII — Proportionality Justification

**Rule 26(b)(1) Factors:**

1. Importance of issues: [analysis]
2. Amount in controversy: $[amount] — TAR cost represents [%] of claim value
3. Parties' relative access: [analysis]
4. Parties' resources: [analysis]
5. Importance of discovery: [analysis]
6. Burden vs. benefit: TAR at [recall]% costs $[X] vs. manual review cost $[Y], saving
   $[Z] ([%] reduction) while achieving estimated [recall]% recall

**Recall Threshold Justification**: The [X]% recall target is proportionate because
[case-specific reasoning]. Achieving [X+5]% recall would require [additional rounds/cost]
at an additional cost of approximately $[Y], producing an estimated [Z] additional
responsive documents — a yield of [%] — which is not proportionate under Rule 26(b)(1)(B).

---

## Section XIV — Transparency and Dispute Resolution

**Disclosure to opposing counsel**: [Producing party] will disclose this protocol to
[Receiving party] no later than [date]. Receiving party may comment within [N] days.

**Validation report sharing**: [Producing party] will share the elusion test results and
final precision/recall metrics no later than [N] days before the production deadline.

**Dispute resolution**: Any dispute about this protocol not resolved by meet-and-confer
will be submitted to [the Court / discovery referee / special master].

---

## Defensibility Assessment Summary

| Section                  | Classification                                        | Notes    |
| ------------------------ | ----------------------------------------------------- | -------- |
| TAR approach selection   | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| Seed set construction    | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| Training workflow        | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| Elusion testing          | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| Privilege integration    | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| Proportionality analysis | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| QC checkpoints           | DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE       | [reason] |
| **Overall Protocol**     | **[DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE]** |          |

---

## Glass Box Audit Trail

[See YAML block below]
```

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-tar-review-protocol"
  mode: "Protocol Design / Protocol Review / Joint Stipulation"
  case: "[Case caption and docket number]"
  court: "[Court and district]"
  producing_party: "[Party name]"
  tar_approach: "TAR 1.0 (Predictive Coding) / TAR 2.0 (CAL)"
  document_corpus:
    total: "[number]"
    post_culling: "[number]"
    estimated_richness: "[%]"
  seed_set:
    size: "[number]"
    sme: "[name and credentials]"
    construction_method: "[random / keyword-guided / other]"
    chain_of_custody: "Documented / Not documented"
  validation:
    elusion_test_confidence: "95%"
    elusion_test_margin: "±[%]"
    elusion_sample_size: "[number]"
    recall_achieved: "[%]"
    precision_achieved: "[%]"
    elusion_rate: "[%]"
  privilege:
    fre_502d_order: "Entered / Pending / Not sought"
    pre_filter_applied: true/false
    privilege_domains_filtered: "[list]"
  proportionality:
    rule_26b1_factors_addressed: true/false
    recall_threshold_justified: true/false
    cost_benefit_documented: true/false
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  case_law_consulted:
    - "Da Silva Moore, 287 F.R.D. 182 — [VERIFIED / UNVERIFIED]"
    - "Rio Tinto PLC v. Vale S.A., 306 F.R.D. 125 — [VERIFIED / UNVERIFIED]"
    - "Livingston v. City of Chicago — [VERIFIED / UNVERIFIED]"
    - "Lawson v. Spirit AeroSystems, 2020 WL 6343292 — [VERIFIED / UNVERIFIED]"
    - "Hyles v. New York City — [VERIFIED / UNVERIFIED]"
    - "Pyrrho Investments Ltd v. MWB Property Ltd [2016] EWHC 256 (Ch) — [VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  overall_defensibility: "DEFENSIBLE / REQUIRES REVISION / NON-DEFENSIBLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Statistical thresholds are case-specific; no mandatory recall minimum exists"
    - "Case law developing for generative AI review; [VERIFY] current authority"
    - "State court rules vary; verify applicable rules before production"
    - "UK/AU markers require verification against current practice notes"
  reviewer: "AI-assisted — requires qualified litigation counsel and eDiscovery professional review"
```

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis drawing on:

- Primary legal authority: _Da Silva Moore v. Publicis Groupe_, 287 F.R.D. 182 (S.D.N.Y.
  2012); _Rio Tinto PLC v. Vale S.A._, 306 F.R.D. 125 (S.D.N.Y. 2015); _Pyrrho
  Investments Ltd v MWB Property Ltd_ [2016] EWHC 256 (Ch); _Hyles v. New York City_,
  2016 U.S. Dist. LEXIS 100390; _Livingston v. City of Chicago_ (N.D. Ill. 2020);
  _Lawson v. Spirit AeroSystems, Inc._, 2020 WL 6343292 (D. Kan. 2020)
- Professional standards: EDRM TAR Guidelines (January 2019); Sedona Conference
  Principles; Grossman and Cormack, "Evaluation of Machine-Learning Protocols for
  Technology-Assisted Review in Electronic Discovery" (2014 ACM SIGIR)
- Quality framework: Adapted from `legalcode-contract-review` quality assurance
  architecture (Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box
  Audit Trail, Anti-Patterns, Writing Standards, Output Format Template)
- Agent team research: 2-agent parallel research pipeline (legal authority research +
  reference standard structural analysis)

All case law references marked [VERIFY] require verification against current authority
before use in any court filing or production certification.
