---
name: legalcode-summary-judgment-analysis
description: Analyze summary judgment motions and oppositions for legal sufficiency, evidentiary support,
  procedural compliance, and strategic positioning. Use when evaluating whether to file a summary judgment
  motion, assessing the strength of a pending motion (own or opposing), drafting or reviewing statements
  of undisputed facts, analyzing evidentiary gaps and admissibility issues, or preparing opposition strategy.
  Covers both movant and non-movant perspectives with jurisdiction-agnostic baseline and [JURISDICTION-SPECIFIC]
  markers for US federal (FRCP Rule 56), England & Wales (CPR Part 24), and Australia (Federal Court Rules
  2011 s 31A). Produces confidence-scored assessments with Glass Box audit trail, actionable recommendations,
  and litigation strategy guidance.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Summary Judgment Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted summary judgment analysis.
> It does not constitute legal advice. All outputs must be reviewed by qualified legal
> counsel licensed in the relevant jurisdiction before use in any proceeding. Procedural
> rules, evidentiary standards, and case law change frequently; verify all authoritative
> sources before relying on any conclusion. AI analysis may miss nuances of judicial
> temperament, local practice, and advocacy strategy that experienced practitioners would
> recognize. Any cited authority marked `[VERIFY]` has not been independently validated
> and must be confirmed before reliance.

---

## Purpose and Scope

This skill performs comprehensive analysis of summary judgment motions and oppositions,
evaluating them across multiple dimensions of legal sufficiency, evidentiary support, and
strategic effectiveness. It is designed for three primary use cases:

1. **Motion Analysis (Movant Perspective)**: Evaluate whether a summary judgment motion
   should be filed, assess the strength of a pending motion, and identify evidentiary gaps
   or procedural deficiencies before filing.

2. **Opposition Analysis (Non-Movant Perspective)**: Analyze an opposing party's summary
   judgment motion to identify weaknesses, develop response strategy, and assess the risk
   of adverse judgment.

3. **Pre-Filing Assessment**: Determine whether summary judgment is strategically
   advisable and identify what additional evidence or discovery is needed before moving.

The skill applies the governing legal standards for dispositive motions, scoring criteria
for evidentiary sufficiency, and practical advocacy frameworks to produce confidence-scored,
citation-linked assessments.

**Covers:**

- **Legal standard compliance**: Whether the motion correctly states and applies the
  applicable summary judgment standard
- **Statement of undisputed facts (SUF)**: Quality, completeness, persuasive framing,
  and record support for each fact
- **Evidentiary sufficiency**: Whether cited evidence is admissible, properly authenticated,
  and actually supports the propositions stated
- **Legal argument quality**: IRAC/CRAC structure, authority hierarchy, statutory
  interpretation methodology, and counter-argument anticipation
- **Procedural compliance**: Filing deadlines, formatting requirements, local rule
  compliance (e.g., Rule 56.1 statements), certification requirements
- **Genuine dispute identification**: Whether material factual disputes exist that
  preclude summary judgment
- **Strategic positioning**: Timing, burden allocation, and litigation posture assessment
- **Opposition strategy**: Response approaches, Rule 56(d) discovery requests, and
  evidence marshaling

**Does not:**

- Replace counsel's judgment on case strategy or judicial temperament
- Serve as a citator or provide definitive authority status (flags for verification)
- Draft summary judgment motions or oppositions (analyzes existing or planned filings)
- Make final filing-readiness determinations
- Assess factual merits beyond evidentiary support analysis

**Related skills:**

- `legalcode-brief-analyzer` — General brief quality analysis
- `legalcode-early-case-assessment` — Pre-discovery litigation evaluation
- `legalcode-evidence-admissibility-analysis` — Detailed evidentiary review
- `legalcode-litigation-risk-assessment` — Risk scoring and impact analysis
- `legalcode-discovery-request-drafter` — Discovery planning for summary judgment support

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the forum and governing
procedural rules first, then localize analysis dimensions accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Summary judgment legal standard and burden allocation
- Statement of facts requirements (format, citation style, rule compliance)
- Filing deadlines and notice requirements
- Local rules (e.g., SDNY Local Rule 56.1, NDCA Local Rule 56)
- Evidentiary requirements and authentication standards
- Briefing page/word limits
- Oral argument conventions
- Standard of appellate review for summary judgment denials

**Reference anchors frequently needed:**

### US Federal (FRCP Rule 56)

- **Standard**: "The court shall grant summary judgment if the movant shows that there is
  no genuine dispute as to any material fact and the movant is entitled to judgment as a
  matter of law." FRCP 56(a) [VERIFY]
- **Timing**: May move "at any time until 30 days after the close of all discovery" unless
  local rule or court order specifies otherwise. FRCP 56(b) [VERIFY]
- **Evidence**: Must cite "particular parts of materials in the record" — depositions,
  documents, ESI, affidavits, declarations, stipulations, admissions, interrogatory
  answers. FRCP 56(c)(1)(A) [VERIFY]
- **Non-movant burden**: Cannot rely on mere pleadings; must "set out specific facts
  showing a genuine issue for trial." Celotex Corp. v. Catrett, 477 U.S. 317 (1986) [VERIFY]
- **Viewing standard**: Evidence viewed "in the light most favorable to the non-moving
  party." Anderson v. Liberty Lobby, Inc., 477 U.S. 242 (1986) [VERIFY]
- **Materiality**: A fact is "material" if it "might affect the outcome of the suit under
  the governing law." Anderson [VERIFY]
- **Genuineness**: A dispute is "genuine" if "the evidence is such that a reasonable jury
  could return a verdict for the nonmoving party." Anderson [VERIFY]
- **Discovery incomplete**: Non-movant may seek deferral under Rule 56(d) by showing
  "specific facts" not yet available through discovery [VERIFY]
- **No 2024-2025 amendments**: Rule 56 unchanged in recent amendment cycles [VERIFY]

### England & Wales (CPR Part 24)

- **Standard**: Court may give summary judgment if "the claimant has no real prospect of
  succeeding on the claim or issue" OR "the defendant has no real prospect of successfully
  defending the claim or issue" AND "there is no other compelling reason why the case or
  issue should be disposed of at a trial." CPR 24.2 [VERIFY]
- **"Real prospect"**: More than fanciful but need not be more than arguable. Swain v.
  Hillman [2001] 1 All ER 91 [VERIFY]
- **Timing**: Claimant may apply after defendant files acknowledgment of service or
  defence. CPR 24.4 [VERIFY]
- **Evidence**: Application made using Form N244 with evidence filed 3-7 days before
  hearing. CPR 24.5 [VERIFY]
- **October 2023 changes**: Part 24 substituted, PD 24 revoked; core test unchanged [VERIFY]
- **No striking out trespassers**: Exception for possession claims against residential
  tenants occupying under a tenancy [VERIFY]

### Australia (Federal Court)

- **Standard**: Court may give judgment if satisfied "a party has no reasonable prospect
  of successfully prosecuting the proceeding or that part of the proceeding" OR
  "successfully defending the proceeding or that part." Federal Court of Australia Act 1976
  (Cth) s 31A(2) [VERIFY]
- **"No reasonable prospect"**: Lower threshold than "certain and concluded determination"
  under old law. General Steel Industries Inc v Commissioner for Railways (NSW) (1964)
  112 CLR 125 [VERIFY]
- **Procedure**: Application under Federal Court Rules 2011 r 26.01 [VERIFY]
- **Strike out**: Deficient pleadings may be struck under r 16.21; typically opportunity
  to amend given [VERIFY]
- **2024 amendments**: Federal Court Legislation Amendment Rules 2024 (May 22, 2024)
  addressed procedural matters but not summary judgment standard [VERIFY]

---

## Interactive Clarification

Use interactive clarification whenever the answer materially changes analysis scope,
evaluation criteria, or output emphasis. If information is already provided, skip the
question. Proceed with stated defaults when the user does not respond.

**CLARIFY block 1: Analysis objective**

- Options: `pre-filing assessment (should we move?)`, `movant motion review (strengthen our motion)`, `opposition analysis (attack their motion)`, `opposition strategy (build our response)`, `comprehensive (evaluate both sides)`
- Default: `comprehensive (evaluate both sides)`
- Why it matters: Pre-filing focuses on viability and evidentiary gaps; movant review emphasizes strengthening; opposition focuses on identifying weaknesses and genuine disputes.

**CLARIFY block 2: Your side**

- Options: `movant (plaintiff/claimant moving for SJ)`, `movant (defendant moving for SJ)`, `non-movant (opposing SJ motion)`, `evaluating for strategy (not yet filed)`
- Default: `evaluating for strategy (not yet filed)`
- Why it matters: Determines burden allocation analysis and framing of recommendations.

**CLARIFY block 3: Procedural posture**

- Options: `pre-discovery`, `mid-discovery`, `post-discovery`, `after motion filed, before opposition`, `after opposition filed, before reply`, `after reply, before hearing`
- Default: `post-discovery`
- Why it matters: Affects availability of Rule 56(d) deferrals, completeness of evidentiary record, and strategic options.

**CLARIFY block 4: Court and jurisdiction**

- Options: `US federal district (specify)`, `US federal circuit (specify)`, `US state court (specify)`, `England & Wales High Court`, `England & Wales County Court`, `Australia Federal Court`, `Australia state/territory (specify)`, `other (specify)`
- Default: `US federal district`
- Why it matters: Determines applicable procedural rules, local rules, and legal standard variations.

**CLARIFY block 5: Claim/defense types**

- Options: `contract claims`, `tort claims (specify)`, `statutory claims (specify)`, `constitutional claims`, `multiple/mixed claims`
- Default: `multiple/mixed claims`
- Why it matters: Different claims have different elements; summary judgment viability varies significantly by claim type.

**CLARIFY block 6: Available materials**

- Options: `motion only`, `motion + exhibits`, `motion + opposition`, `motion + opposition + reply`, `full briefing + record excerpts`, `preliminary assessment (no motion yet)`
- Default: `motion + opposition`
- Why it matters: With only the motion, analysis is one-sided. With full briefing, the tool can assess both sides' arguments and likely outcome.

**CLARIFY block 7: Analysis depth**

- Options: `quick scan (high-level viability)`, `standard review (element-by-element)`, `deep dive (fact-by-fact with evidentiary audit)`, `competition-grade (full scoring)`
- Default: `standard review (element-by-element)`
- Why it matters: Quick scan for early strategy decisions; deep dive for pre-filing quality assurance or critical opposition.

**CLARIFY block 8: Key issues (if known)**

- Prompt: "Are there specific claims, defenses, or factual disputes you want me to focus on?"
- Default: `all material issues`
- Why it matters: Allows targeted analysis when time is limited or specific issues are outcome-determinative.

---

## Workflow

### Step 1: Accept input materials

Accept materials in any of these formats:

- **File path(s)**: Read documents directly (PDF, DOCX, TXT, MD)
- **Pasted text**: Accept inline motion/opposition text
- **URL**: Fetch from PACER, court website, or document management system
- **Multiple files**: For full briefing sets, accept paths to all documents

If documents are PDFs, convert:

```bash
# Attempt pandoc first, fall back to pdftotext
pandoc "$FILE" -t markdown -o "${FILE%.pdf}.md" 2>/dev/null || pdftotext "$FILE" "${FILE%.pdf}.txt"
```

Identify and categorize each document:

- Motion for summary judgment
- Statement of undisputed facts / Rule 56.1 statement
- Memorandum of law in support
- Opposition / Response
- Counter-statement of facts
- Reply brief
- Declarations / Affidavits
- Exhibits / Record excerpts

### Step 2: Gather context via interactive clarification

Run through CLARIFY blocks 1-8, skipping any already answered by the initial prompt.
Record all responses (and defaults used) in the Glass Box audit trail.

### Step 3: Identify governing legal standard

Based on the jurisdiction identified:

1. **State the applicable standard explicitly** — Quote the governing rule (FRCP 56,
   CPR 24, s 31A, or local equivalent)

2. **Identify burden allocation**:
   - Who bears the initial burden? (movant)
   - What must the movant show? (no genuine dispute + entitlement to judgment)
   - How does burden shift? (production vs. persuasion)
   - What must non-movant do to survive? (show genuine dispute, not mere denials)

3. **Note any local rule requirements**:
   - Rule 56.1 statement format (e.g., SDNY, NDIL)
   - Response requirements (paragraph-by-paragraph, additional facts)
   - Page/word limits for briefs
   - Exhibit formatting and tabbing requirements

4. **Flag jurisdiction-specific variations**:
   - [US Federal] Celotex/Anderson/Matsushita trilogy analysis required
   - [England & Wales] "Compelling reason" for trial separate inquiry
   - [Australia] "No reasonable prospect" — lower bar than "hopeless"

### Step 4: Analyze statement of undisputed facts (SUF)

The SUF is often the most important document in summary judgment practice. Analyze:

**4a. Structural quality:**

| Criterion                           | Assessment    | Notes                                  |
| ----------------------------------- | ------------- | -------------------------------------- |
| **Numbered paragraphs**             | Required      | Each fact separately numbered          |
| **One fact per paragraph**          | Best practice | Compound facts are harder to dispute   |
| **Logical organization**            | Persuasive    | Chronological, thematic, or by element |
| **Headings/subheadings**            | Recommended   | Organize by claim/defense element      |
| **Pinpoint citations**              | Required      | Page:line, not just "Depo."            |
| **Citation to admissible evidence** | Required      | Not just pleadings or argument         |

**4b. Fact-by-fact analysis:**

For each material fact in the SUF:

| Fact # | Fact Statement | Cited Evidence | Admissible? | Actually Supports? | Disputed? | Materiality  |
| ------ | -------------- | -------------- | ----------- | ------------------ | --------- | ------------ |
| 1      | [statement]    | [cite]         | Y/N/?       | Y/N/?              | Y/N       | HIGH/MED/LOW |

**4c. Red flags in SUF:**

- Facts stated without any citation
- Citations to inadmissible evidence (hearsay, unauthenticated documents)
- Citations that do not actually support the proposition
- Characterizations beyond what the evidence shows
- Legal conclusions disguised as facts
- Compound facts containing both undisputed and disputed elements
- Facts immaterial to any claim or defense element
- Missing facts required to establish elements

**4d. For opposition counter-statements:**

- Does the response address every fact? (Failure to respond may = admission)
- Are denials supported by contrary evidence?
- Are "disputes" genuine or merely semantic?
- Are additional facts properly supported?
- Do additional facts create genuine issues?

### Step 5: Element-by-element legal analysis

Map each claim and defense to its legal elements, then assess whether summary judgment
is appropriate on each:

**5a. Claim/Defense element mapping:**

| Claim/Defense | Element             | Movant Evidence | Non-Movant Evidence | Dispute? | SJ Appropriate? |
| ------------- | ------------------- | --------------- | ------------------- | -------- | --------------- |
| [Breach of K] | 1. Valid contract   | [cite]          | [cite]              | Y/N      | Y/N             |
|               | 2. Performance by P | [cite]          | [cite]              | Y/N      | Y/N             |
|               | 3. Breach by D      | [cite]          | [cite]              | Y/N      | Y/N             |
|               | 4. Damages          | [cite]          | [cite]              | Y/N      | Y/N             |

**5b. For each element, assess:**

- Is the element contested?
- What evidence supports the movant's position?
- What evidence supports the non-movant's position?
- Are there genuine disputes of material fact?
- Could a reasonable jury find for the non-movant?
- Is the movant entitled to judgment as a matter of law?

**5c. Affirmative defense analysis (critical for plaintiff-movants):**

If the movant is the plaintiff, they must also negate or address all affirmative defenses:

| Affirmative Defense    | Raised? | Addressed by Movant? | Evidence? | Genuine Dispute? |
| ---------------------- | ------- | -------------------- | --------- | ---------------- |
| Statute of limitations | Y/N     | Y/N                  | [cite]    | Y/N              |
| Waiver                 | Y/N     | Y/N                  | [cite]    | Y/N              |
| Estoppel               | Y/N     | Y/N                  | [cite]    | Y/N              |
| [etc.]                 |         |                      |           |                  |

**Common movant failure**: Not addressing affirmative defenses at all — automatic denial.

### Step 6: Evidentiary sufficiency audit

Evaluate the evidentiary foundation for both sides:

**6a. Evidence inventory:**

| Evidence Type | Description   | Party      | Admissible? | Authentication? | Issues                      |
| ------------- | ------------- | ---------- | ----------- | --------------- | --------------------------- |
| Declaration   | [name]        | Movant     | Y/N         | Y/N             | [hearsay, foundation, etc.] |
| Deposition    | [name]        | Both       | Y/N         | Y/N             | [completeness, context]     |
| Document      | [description] | Movant     | Y/N         | Y/N             | [authentication, hearsay]   |
| Expert Report | [name]        | Non-movant | Y/N         | Y/N             | [Daubert, foundation]       |

**6b. Admissibility issues to flag:**

- **Hearsay**: Out-of-court statements offered for truth
- **Authentication**: Documents not properly authenticated
- **Foundation**: Declarant lacks personal knowledge
- **Best evidence**: Copies without accounting for original
- **Expert opinion**: Not properly disclosed, Daubert issues
- **Privilege**: Privileged materials cited without waiver analysis
- **Sham affidavit**: Declaration contradicts prior deposition testimony

**6c. Evidentiary gaps:**

| Gap           | Party Affected    | Impact       | Can Be Cured? | How?                           |
| ------------- | ----------------- | ------------ | ------------- | ------------------------------ |
| [description] | Movant/Non-movant | HIGH/MED/LOW | Y/N           | [discovery, declaration, etc.] |

### Step 7: Legal argument quality assessment

Evaluate the memoranda of law:

**7a. Structure and organization:**

| Component                              | Present? | Quality | Notes                       |
| -------------------------------------- | -------- | ------- | --------------------------- |
| Standard of review stated correctly    | Y/N      | —       | [quote the stated standard] |
| Elements identified for each claim     | Y/N      | —       |                             |
| IRAC/CRAC for each issue               | Y/N      | —       |                             |
| Headings are argumentative conclusions | Y/N      | —       |                             |
| Authority hierarchy respected          | Y/N      | —       | Binding > persuasive        |
| Adverse authority addressed            | Y/N      | —       | Rule 3.3 compliance         |

**7b. Authority quality:**

| Authority   | Binding/Persuasive | On Point? | Current? | Properly Cited? |
| ----------- | ------------------ | --------- | -------- | --------------- |
| [case name] | [level]            | Y/N       | [VERIFY] | Y/N             |

**7c. Logical fallacies to flag:**

- Conclusory reasoning (asserting conclusions without connecting to evidence)
- Ignoring adverse authority (ethical violation in many jurisdictions)
- Mischaracterizing evidence or case holdings
- Conflating legal and factual disputes
- Treating disputed facts as undisputed
- Applying wrong standard of review

### Step 8: Procedural compliance check

**8a. Filing deadlines:**

| Requirement                    | Deadline | Met? | Notes                               |
| ------------------------------ | -------- | ---- | ----------------------------------- |
| Motion filed within time limit | [date]   | Y/N  | FRCP 56(b): 30 days after discovery |
| Opposition filed timely        | [date]   | Y/N  | Local rules vary                    |
| Reply filed timely             | [date]   | Y/N  |                                     |
| Notice requirements            | [rule]   | Y/N  |                                     |

**8b. Format compliance:**

| Requirement                  | Compliant? | Notes                |
| ---------------------------- | ---------- | -------------------- |
| Page/word limits             | Y/N        | [specify limit]      |
| Font and margin requirements | Y/N        |                      |
| Rule 56.1 statement format   | Y/N        | [specify local rule] |
| Certificate of service       | Y/N        |                      |
| Certificate of word count    | Y/N        |                      |
| Exhibit tabbing              | Y/N        |                      |

**8c. Local rule compliance:**

Check local rules for specific requirements:

- SDNY Local Rule 56.1: Separate statement required
- NDCA Local Rule 56: Statement integrated in brief
- CDCA Local Rule 56: Separate statement with specific format
- [Check applicable local rules for the specific district]

### Step 9: Genuine dispute assessment

The core question: Are there genuine disputes of material fact?

**9a. Dispute classification:**

For each purported dispute:

| Disputed Fact | Movant Evidence | Non-movant Evidence | Genuine? | Material? | Dispositive? |
| ------------- | --------------- | ------------------- | -------- | --------- | ------------ |
| [fact]        | [cite]          | [cite]              | Y/N      | Y/N       | Y/N          |

**9b. Genuine dispute criteria:**

A dispute is **genuine** if:

- Evidence exists on both sides
- A reasonable jury could credit either version
- The non-movant's evidence is admissible
- The dispute is not merely semantic

A dispute is **NOT genuine** if:

- Non-movant offers only conclusory denials
- Non-movant relies on pleadings, not evidence
- Non-movant's evidence is inadmissible
- No reasonable jury could credit the non-movant's version
- The "dispute" is actually a legal dispute, not factual

**9c. Materiality criteria:**

A fact is **material** if:

- It affects an element of a claim or defense
- The outcome might change based on this fact
- It is relevant under the governing substantive law

A fact is **NOT material** if:

- It is merely background or context
- It does not affect any claim or defense element
- It is relevant only to excluded issues

### Step 10: Strategic assessment and recommendations

Based on the analysis, provide strategic guidance:

**10a. Outcome prediction:**

| Outcome                          | Likelihood | Rationale                  |
| -------------------------------- | ---------- | -------------------------- |
| Summary judgment granted in full | [0-100%]   | [reasons]                  |
| Summary judgment granted in part | [0-100%]   | [on which claims/defenses] |
| Summary judgment denied          | [0-100%]   | [reasons]                  |
| Oral argument likely to matter   | Y/N        | [why]                      |

**10b. For movants (strengthening the motion):**

- Evidence to add before filing
- Facts to include in supplemental declaration
- Authority to add or strengthen
- Arguments to bolster
- Procedural issues to cure

**10c. For non-movants (opposition strategy):**

- Strongest grounds for denial
- Evidence needed to create genuine disputes
- Rule 56(d) request viability (if discovery incomplete)
- Arguments for "compelling reason" for trial (CPR 24)
- Counter-motion viability

**10d. Settlement implications:**

- How does this motion affect settlement posture?
- If motion likely to be granted, settlement value adjusts down
- If motion likely to be denied, settlement value adjusts up
- Timing considerations for settlement discussions

### Step 11: Quality verification

Before delivering the analysis, run quality checks:

**11a. Citation Quality Gates:**

| Gate       | Rule                                         | Status    | Notes |
| ---------- | -------------------------------------------- | --------- | ----- |
| Source     | Every legal claim cites specific authority   | PASS/FAIL |       |
| Format     | Citations in proper jurisdiction format      | PASS/FAIL |       |
| Currency   | Authorities checked for overruling/amendment | PASS/FAIL |       |
| Domain     | Analysis stays within selected jurisdiction  | PASS/FAIL |       |
| Confidence | Uncertainty explicitly stated                | PASS/FAIL |       |

**11b. Self-Interrogation (for HIGH/CRITICAL findings):**

For each outcome-determinative conclusion:

1. **Legal chain integrity**: Does the conclusion follow from cited authority and facts?
2. **Completeness**: Have all relevant authorities and facts been considered?
3. **Adversarial challenge**: What is the strongest counter-argument?

**11c. Confidence scoring:**

| Conclusion   | Confidence                               | Rationale |
| ------------ | ---------------------------------------- | --------- |
| [conclusion] | Definite/High/Probable/Possible/Unlikely | [basis]   |

### Step 12: Deliver findings

Compile all findings into the Output Format Template (see below). Present findings in
priority order (CRITICAL issues first, then HIGH, then MEDIUM, then ADVISORY observations).

---

## Summary Judgment Analysis Framework

Evaluate all 10 domains unless explicitly scoped down:

| Domain                   | What to Assess                    | Evidence Signals                 | Common Red Flags                               |
| ------------------------ | --------------------------------- | -------------------------------- | ---------------------------------------------- |
| 1. Legal standard        | Correct statement and application | Rule quoted, burden allocated    | Wrong standard, burden confusion               |
| 2. SUF quality           | Completeness, persuasion, support | Numbered facts, pinpoint cites   | Missing cites, compound facts                  |
| 3. Element coverage      | Every element addressed           | Claim/defense mapping            | Missing elements, affirmative defenses ignored |
| 4. Evidentiary support   | Admissibility, authentication     | Declarations, authenticated docs | Hearsay, unauthenticated, sham affidavits      |
| 5. Genuine disputes      | Material fact disputes identified | Conflicting evidence             | Mere denials, semantic disputes                |
| 6. Legal argument        | IRAC structure, authority quality | Binding cases, synthesis         | Conclusory, adverse authority ignored          |
| 7. Procedural compliance | Deadlines, format, local rules    | Timely filing, proper format     | Late, wrong format, missing Rule 56.1          |
| 8. Counter-argument      | Anticipation and rebuttal         | Pre-emptive addressing           | Ignoring obvious counters                      |
| 9. Credibility           | Issues requiring jury assessment  | Witness demeanor matters         | Pure credibility contests                      |
| 10. Strategic fit        | Timing, leverage, settlement      | Phase-appropriate filing         | Premature motion, discovery incomplete         |

---

## Risk Classification

Classify each finding using this litigation-specific framework:

| Class        | Meaning                                                            | Typical Response                                              |
| ------------ | ------------------------------------------------------------------ | ------------------------------------------------------------- |
| **CRITICAL** | Dispositive deficiency — motion will fail or succeed on this issue | Immediate attention; may require withdrawal or major revision |
| **HIGH**     | Material weakness significantly affecting likelihood of success    | Address before filing or in reply; major opposition argument  |
| **MEDIUM**   | Noteworthy issue that could be raised but is not dispositive       | Cure if possible; prepare response argument                   |
| **LOW**      | Minor issue or best-practice suggestion                            | Note for future filings                                       |
| **ADVISORY** | Strategic observation, not a deficiency                            | Consider for overall strategy                                 |

---

## Actionable Output Per Finding

For each MEDIUM/HIGH/CRITICAL finding, provide:

- **Finding summary**: One-sentence description
- **Why it matters**: Impact on motion outcome
- **Evidence/Authority basis**: What supports this finding
- **Verification status**: `VERIFIED` or `[VERIFY]`
- **Recommended action**: Specific step to take
- **Owner**: Attorney, paralegal, expert, client
- **Priority**: Immediate / Near-term / If time permits
- **Expected effect**: How addressing this changes the analysis

---

## Prioritization Framework

| Tier       | Label     | Criteria                                               | Timing                                     |
| ---------- | --------- | ------------------------------------------------------ | ------------------------------------------ |
| **Tier 1** | Immediate | CRITICAL items; dispositive issues; deadline-sensitive | Before filing / Before opposition deadline |
| **Tier 2** | Near-term | HIGH items affecting outcome probability               | Within current briefing cycle              |
| **Tier 3** | If Time   | MEDIUM items improving quality                         | If resources permit                        |

---

## Citation Quality Gates

Before delivery, run these gates on every legal proposition:

| Gate           | Rule                                                      | Fail Action                   |
| -------------- | --------------------------------------------------------- | ----------------------------- |
| **Source**     | Every legal standard, element, or rule links to authority | Add source or mark `[VERIFY]` |
| **Format**     | Citations in jurisdiction-appropriate format              | Normalize citation            |
| **Currency**   | Check for overruling, superseding authority               | Add `[CHECK CURRENCY]`        |
| **Domain**     | Analysis stays within selected jurisdiction               | Remove jurisdiction bleed     |
| **Confidence** | Align certainty with evidentiary/legal support            | Add confidence qualifier      |

---

## Self-Interrogation (For CRITICAL Findings)

Apply a three-pass challenge before finalizing any CRITICAL or outcome-determinative finding:

**Pass 1 — Legal Chain Integrity**

- Does the conclusion follow logically from the cited authority and evidence?
- Would the court actually reach this conclusion on this record?

**Pass 2 — Completeness Test**

- What contrary authority or evidence would change this conclusion?
- Have all relevant arguments been considered?

**Pass 3 — Adversarial Challenge**

- What is the strongest counter-argument?
- Under what circumstances would the opposite conclusion be correct?

If any pass reveals weakness, revise before delivery.

---

## Confidence Scoring

| Level        | Range     | Interpretation                                                | Action                        |
| ------------ | --------- | ------------------------------------------------------------- | ----------------------------- |
| **Definite** | 0.95-1.00 | Clear authority, strong evidence, straightforward application | State with confidence         |
| **High**     | 0.80-0.94 | Strong support, minor uncertainties                           | State with brief caveat       |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ              | Present both sides            |
| **Possible** | 0.40-0.59 | Material uncertainty, competing considerations                | Flag for senior review        |
| **Unlikely** | 0.00-0.39 | Weak support, speculative                                     | Do not rely; note uncertainty |

---

## Glass Box Audit Trail

Every summary judgment analysis MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-summary-judgment-analysis"
  mode: "Created from scratch"
  topic: "summary judgment motion analysis"
  jurisdiction: "[selected jurisdiction]"
  court: "[specific court if known]"
  side_analyzed: "[movant/non-movant/both]"
  procedural_posture: "[pre-filing/post-motion/etc.]"
  claims_analyzed:
    - "[claim 1]"
    - "[claim 2]"
  defenses_analyzed:
    - "[defense 1]"
  materials_reviewed:
    - "[motion]"
    - "[opposition]"
    - "[exhibits]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path or 'Not created']"
  source_skills_analyzed: "legalcode reference standard"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  key_assumptions:
    - "[assumption 1]"
    - "[assumption 2]"
  limitations:
    - "[limitation 1]"
  confidence: "HIGH | MEDIUM | LOW — [rationale]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Avoid these failure modes in summary judgment analysis:

1. **Ignoring burden allocation** — Analyzing without clarity on who bears the burden at
   each stage. The movant always has the initial burden; how it shifts depends on whether
   movant bears the ultimate burden of proof (plaintiff vs. defendant movant).

2. **Treating all facts as equally material** — Not every disputed fact matters. Focus
   analysis on facts that affect claim/defense elements, not peripheral details.

3. **Confusing legal disputes with factual disputes** — Summary judgment is appropriate
   when facts are undisputed but parties disagree on legal consequences. Do not conflate
   these with genuine factual disputes.

4. **Ignoring affirmative defenses** — Plaintiff-movants must address every affirmative
   defense. Missing even one can doom the motion. This is the most common movant error.

5. **Accepting "genuine dispute" claims at face value** — Not every asserted dispute is
   genuine. Evaluate whether the non-movant's evidence actually creates a dispute a
   reasonable jury could resolve in their favor.

6. **Overlooking admissibility issues** — Evidence cited in summary judgment must be
   reducible to admissible form at trial. Hearsay, unauthenticated documents, and
   foundation problems are fatal.

7. **Ignoring local rules** — Many summary judgment motions fail on local rule
   technicalities (e.g., improper Rule 56.1 statement format). Always check local rules.

8. **Missing the standard of review** — Different claims have different standards. A
   Rule 12(b)(6) motion is not the same as Rule 56. Ensure the correct standard is
   applied throughout.

9. **Conclusory outcome predictions** — Predicting outcomes without tracing the reasoning
   through each element and each disputed fact. Show your work.

10. **Ignoring credibility-dependent issues** — Some issues inherently require credibility
    determinations that preclude summary judgment. Recognize when jury assessment is
    necessary.

11. **Applying wrong jurisdiction's standard** — Using FRCP 56 analysis for a CPR Part 24
    motion, or vice versa. The standards differ in meaningful ways.

12. **Missing the "compelling reason" inquiry (UK)** — In England & Wales, even if there
    is no real prospect of success, summary judgment may be denied if there is a
    compelling reason for trial. This is a separate analysis.

13. **Overlooking Rule 56(d) opportunities** — When discovery is incomplete, the non-movant
    should seek deferral under Rule 56(d). Analyze whether this option was or should be
    pursued.

14. **Sham affidavit doctrine ignorance** — Declarations that contradict prior deposition
    testimony without adequate explanation may be disregarded. Flag these issues.

15. **Single-pass analysis** — Summary judgment motions are complex. Read all materials
    completely before analyzing. Cross-references and interactions between sections matter.

---

## Writing Standards

Apply plain-language discipline to all output:

**For internal analysis:**

- Plain language, no jargon without definition
- Active voice: "The movant must show" not "It must be shown by the movant"
- Short sentences, one point per sentence
- Tables for structured assessments
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a litigation partner quickly identify the key issues?
2. Are all outcome-determinative conclusions supported by specific evidence/authority?
3. Are confidence levels appropriate given the evidentiary record?
4. Are recommendations actionable and prioritized?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for current authority on summary judgment standards
- Verify that cited cases have not been overruled
- Find additional authority supporting or undermining arguments
- Mark all legalcode-mcp-sourced citations as `VERIFIED`

**Without legalcode-mcp:**

- Mark all case law and statutory references with `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Include prominent notice that citations require independent verification
- Focus on structural analysis, evidentiary sufficiency, and procedural compliance

---

## Output Format Template

````markdown
# Summary Judgment Analysis — [Case Name/Caption]

## 1. Executive Summary

**Motion**: [Movant name] motion for [full/partial] summary judgment on [claims/defenses]
**Court**: [Court and jurisdiction]
**Your side**: [Movant/Non-movant]
**Procedural posture**: [Stage of litigation]
**Analysis date**: [Date]

**Bottom line**: [1-2 sentence assessment of likely outcome]

**Overall confidence**: [0.00-1.00 + label]

---

## 2. Governing Legal Standard

**Applicable rule**: [FRCP 56 / CPR 24 / s 31A / etc.]
**Standard**: [Quote the standard]
**Burden allocation**:

- Initial burden: [Who bears it, what must they show]
- Shifted burden: [How burden shifts to non-movant]
- Ultimate standard: [What the court must find to grant SJ]

**Local rules applicable**: [List any local rule requirements]

---

## 3. Claims and Defenses Matrix

### Claims

| Claim     | Elements   | Movant Coverage          | Genuine Disputes | SJ Viability |
| --------- | ---------- | ------------------------ | ---------------- | ------------ |
| [Claim 1] | [Elements] | Complete/Partial/Missing | Y/N              | HIGH/MED/LOW |

### Affirmative Defenses

| Defense     | Raised | Movant Addressed | Genuine Dispute | Impact       |
| ----------- | ------ | ---------------- | --------------- | ------------ |
| [Defense 1] | Y/N    | Y/N              | Y/N             | [assessment] |

---

## 4. Statement of Undisputed Facts Analysis

**Overall quality**: [STRONG / ADEQUATE / WEAK]

### Critical Issues

| Issue   | Fact # | Problem       | Severity          | Recommendation |
| ------- | ------ | ------------- | ----------------- | -------------- |
| [issue] | [#]    | [description] | CRITICAL/HIGH/MED | [action]       |

### Fact-by-Fact Assessment

[Summary table or narrative of key facts, evidence support, and dispute status]

---

## 5. Evidentiary Sufficiency

### Evidence Inventory

| Evidence      | Type   | Party   | Admissible | Issues   |
| ------------- | ------ | ------- | ---------- | -------- |
| [description] | [type] | [party] | Y/N/?      | [issues] |

### Evidentiary Gaps

| Gap   | Impact       | Can Cure? | How?     |
| ----- | ------------ | --------- | -------- |
| [gap] | HIGH/MED/LOW | Y/N       | [method] |

---

## 6. Genuine Dispute Analysis

### Material Fact Disputes

| Fact   | Movant Evidence | Non-movant Evidence | Genuine? | Material? |
| ------ | --------------- | ------------------- | -------- | --------- |
| [fact] | [cite]          | [cite]              | Y/N      | Y/N       |

### Assessment

[Narrative assessment of whether genuine disputes of material fact exist]

---

## 7. Legal Argument Assessment

### Movant's Arguments

| Argument | Structure | Authority Quality    | Persuasiveness | Issues   |
| -------- | --------- | -------------------- | -------------- | -------- |
| [arg]    | IRAC/weak | Strong/Adequate/Weak | HIGH/MED/LOW   | [issues] |

### Non-movant's Arguments (if opposition reviewed)

| Argument | Structure | Authority Quality    | Persuasiveness | Issues   |
| -------- | --------- | -------------------- | -------------- | -------- |
| [arg]    | IRAC/weak | Strong/Adequate/Weak | HIGH/MED/LOW   | [issues] |

---

## 8. Procedural Compliance

| Requirement             | Status              | Notes     |
| ----------------------- | ------------------- | --------- |
| Filing deadline         | COMPLIANT/DEFICIENT | [details] |
| Rule 56.1 statement     | COMPLIANT/DEFICIENT | [details] |
| Page/word limits        | COMPLIANT/DEFICIENT | [details] |
| Local rule requirements | COMPLIANT/DEFICIENT | [details] |

---

## 9. Outcome Prediction

| Outcome            | Likelihood | Rationale         |
| ------------------ | ---------- | ----------------- |
| SJ granted in full | [X]%       | [reasons]         |
| SJ granted in part | [X]%       | [on which claims] |
| SJ denied          | [X]%       | [reasons]         |

**Key drivers**: [What factors most influence the outcome]

---

## 10. Strategic Recommendations

### For Movant

| Priority | Recommendation | Expected Impact |
| -------- | -------------- | --------------- |
| Tier 1   | [action]       | [impact]        |
| Tier 2   | [action]       | [impact]        |

### For Non-movant

| Priority | Recommendation | Expected Impact |
| -------- | -------------- | --------------- |
| Tier 1   | [action]       | [impact]        |
| Tier 2   | [action]       | [impact]        |

### Settlement Implications

[How this motion affects settlement posture and timing]

---

## 11. Quality Assurance

**Citation Quality Gates**: [All passed / Issues identified]
**Self-Interrogation**: [Performed for CRITICAL items / Not applicable]
**Confidence calibration**: [Assessment of overall confidence level]

---

## 12. Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-summary-judgment-analysis"
  [... full audit trail ...]
```
````

```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified statutory and case law references
3. Add jurisdiction-specific procedural requirements (local rules, filing deadlines)
4. Add jurisdiction-specific evidentiary standards
5. Include leading cases from the jurisdiction
6. Update the frontmatter name and description

**Potential variants:**
- `legalcode-summary-judgment-analysis-us-federal` — Deep US federal coverage with circuit splits
- `legalcode-summary-judgment-analysis-ew` — England & Wales CPR Part 24 focus
- `legalcode-summary-judgment-analysis-australia` — Australian Federal Court focus
- `legalcode-summary-judgment-analysis-sdny` — SDNY Local Rule 56.1 specific

---

## Provenance

Legalcode original skill created on 2026-03-02. Research-backed creation using:
- Reference standard: `legalcode-contract-review` and `legalcode-brief-analyzer`
- Related skills analyzed: `legalcode-early-case-assessment`, `legalcode-litigation-risk-assessment`
- Research sources:
  - FRCP Rule 56 and commentary (current through 2025)
  - CPR Part 24 (England & Wales, as amended October 2023)
  - Federal Court of Australia Act 1976 (Cth) s 31A
  - Celotex/Anderson/Matsushita trilogy analysis
  - Thomson Reuters Summary Judgment practice guides
  - Practice tips from federal litigation practitioners
```
