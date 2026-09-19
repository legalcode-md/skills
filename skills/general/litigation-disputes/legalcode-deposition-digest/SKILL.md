---
name: legalcode-deposition-digest
description: Summarize deposition transcripts by topic with page-line citations, internal contradictions,
  prior statement inconsistencies, and follow-up areas. Use when digesting Rule 30(b)(6) corporate designee
  depositions, expert witness depositions, adverse party depositions, or fact witness depositions in federal
  or state civil litigation.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Summarize deposition transcripts by topic with page-line citations, internal contradictions, prior statement inconsistencies, and follow-up areas. Use when digesting Rule 30(b)(6) corporate designee depositions, expert witness depositions, adverse party depositions, or fact witness depositions in federal or state civil litigation. Supports four digest formats: topical (organized by subject matter), chronological (event timeline), page-line (sequential with key testimony flagged), and witness-comparison (cross-referencing testimony across multiple depositions). Identifies admissions, evasions, lack-of-knowledge responses, document-related testimony, and impeachment material. Tracks exhibit references with testimony context. Flags testimony relevant to specific claims, defenses, or motion arguments. Produces witness credibility assessment, deposition-to-deposition contradiction matrix, and designated testimony recommendations for summary judgment or trial. Calibrated to US federal practice (FRCP 30–32; FRE 801, 613, 608–609, 901) with [JURISDICTION-SPECIFIC] markers for state variants.


# Legalcode Deposition Digest

> **Disclaimer**: This skill provides a framework for AI-assisted deposition digest
> preparation. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use or
> submission to any court, tribunal, or opposing party. Federal and state procedural
> rules—including the FRCP and local court rules—are amended regularly; verify current
> applicability before relying on any provision described here. Statutory, case law, and
> evidence-rule references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them. Deposition analysis has tactical,
> strategic, and ethical dimensions that require experienced counsel judgment. AI-generated
> page-line citations must be verified against the original transcript before use in any
> court filing.

## Purpose and Scope

Use this skill to produce a structured, evidentiary-grade digest of one or more deposition
transcripts after the deposition has concluded.

**This skill:**

- Summarizes deposition testimony by topic, chronology, or page-line sequence
- Identifies and classifies admissions, evasions, lack-of-knowledge responses, expert
  deficiencies, and impeachment opportunities
- Classifies each finding by evidentiary character (ADMISSION, HELPFUL, QUALIFIED,
  EVASION, IMPEACHMENT), severity (RED/YELLOW/GREEN), and evidentiary sufficiency
  (STRONG/ADEQUATE/WEAK/INADMISSIBLE)
- Distinguishes sworn from unsworn prior inconsistent statements for FRE 801(d)(1)(A)
  substantive vs. FRE 613 impeachment-only purposes
- Tracks exhibit references and authentication testimony
- Flags 30(b)(6) corporate designee knowledge gaps and preparation failures
- Conducts Daubert vulnerability analysis for expert witness depositions
- Maps testimony to claim/defense elements for summary judgment or trial prep
- Produces cross-deposition contradiction matrices for multi-witness analysis
- Identifies designated testimony candidates for summary judgment and trial
- Generates a follow-up discovery priority register based on gaps revealed

**This skill does not:**

- Replace reading the full transcript or attending the deposition
- Constitute legal advice or guarantee any evidentiary ruling
- Draft briefs, motions, or court submissions (see `legalcode-motion-to-dismiss-drafter`,
  `legalcode-summary-judgment-analysis`, or `legalcode-opposition-brief-drafter`)
- Prepare deposition outlines or question sequences (see `legalcode-deposition-preparation`)
- Verify AI-generated page-line citations — that verification obligation rests with counsel

**Companion skills:**

- `legalcode-deposition-preparation` — Pre-deposition: outline design, impeachment prep,
  exhibit strategy
- `legalcode-summary-judgment-analysis` — Post-digest: using deposition testimony to
  build or oppose summary judgment motions
- `legalcode-early-case-assessment` — Pre-deposition: case theory alignment and discovery
  strategy
- `legalcode-litigation-budget` — Cost-benefit analysis of deposition strategy

## Jurisdiction and Governing Law

This skill is calibrated to **US federal practice** (FRCP, FRE) as the primary framework.
State and international deposition contexts are addressed with [JURISDICTION-SPECIFIC]
markers throughout.

### US Federal Anchors [VERIFY current version before relying]

| Rule                                          | Substance                                                                                | Digest Relevance                                      |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **FRCP 30**                                   | Taking oral depositions; 7-hour limit; objection rules; 30(b)(6) notice                  | Sets scope, time limits, improper objection standards |
| **FRCP 30(c)(2)**                             | Objection form: concise, non-argumentative, non-suggestive                               | Objection flagging in digest                          |
| **FRCP 30(b)(6)**                             | Corporate designee preparation obligation; "reasonably available" info                   | 30(b)(6) knowledge-gap analysis                       |
| **FRCP 30(d)(2)**                             | Sanctions for impeding, delaying, or frustrating fair examination                        | Evasion → sanctions flag                              |
| **FRCP 32(a)(2)**                             | Any party may use any deposition for impeachment without unavailability showing          | Impeachment-purpose use                               |
| **FRCP 32(a)(3)**                             | Adverse party deposition usable for **any purpose** (no unavailability needed)           | Admission/substantive use                             |
| **FRCP 32(a)(4)**                             | Non-party deposition for any purpose if witness unavailable (death, distance, illness)   | Unavailability threshold                              |
| **FRCP 56(c)**                                | Summary judgment requires citation to "particular parts" of record including depositions | Designated testimony format                           |
| **FRE 801(d)(2)**                             | Party admissions are not hearsay; admissible substantively                               | Admission classification                              |
| **FRE 801(d)(1)(A)**                          | Prior inconsistent sworn statement at deposition: substantive, not just impeachment      | Sworn-vs.-unsworn fork                                |
| **FRE 613**                                   | Prior inconsistent statement (any form): admissible for impeachment                      | Impeachment purpose only                              |
| **FRE 608/609**                               | Witness character for truthfulness; prior convictions                                    | Credibility section                                   |
| **FRE 901**                                   | Authentication foundation; testimony identifying exhibits                                | Exhibit tracking                                      |
| **FRE 106**                                   | Rule of completeness: opponent may require additional context                            | Counter-designation trigger                           |
| _Daubert v. Merrell Dow_, 509 U.S. 579 (1993) | Expert methodology: tested, peer-reviewed, error rate, generally accepted                | Expert deficiency analysis                            |
| _Tome v. United States_, 513 U.S. 150 (1995)  | Prior consistent statements must predate motive to fabricate                             | Rehabilitation assessment                             |

[JURISDICTION-SPECIFIC] Always verify for:

- **State rules**: Deposition scope, time limits, objection practices, and 30(b)(6)
  equivalents vary substantially across state courts. Many states follow CCP (California),
  CPLR (New York), or Texas Rules.
- **Expert qualification**: Some states use _Frye_ general-acceptance standard (not Daubert).
  Identify governing state before applying Daubert analysis. [VERIFY]
- **Designation timing**: Local rules govern pre-trial deposition designation deadlines
  (commonly: designations 10 days pre-trial, counter-designations 5 days, objections
  2 days — but this varies widely by district/court). [VERIFY local rules]
- **England & Wales**: CPR Part 34 governs witness statements; oral depositions are rare.
  Cross-examination rights differ from US model. [VERIFY]

## Interactive Clarification

This skill uses **interactive clarification** (CLARIFY blocks) before beginning analysis.
When information is already provided, skip the relevant question. Present options as a
structured list. For each question, include a brief "Why this matters" note.

For batch or non-interactive runs, use these defaults: propounding side, comprehensive
analysis, jurisdiction-agnostic (federal), single deposition, no prior materials, no
playbook. State defaults explicitly at the start of the digest.

## Workflow

### Step 1: Accept Input

Accept the deposition in any of these forms:

- **Transcript file**: Plain text, PDF, or Word document of the certified court reporter
  transcript. Page-line format preferred.
- **Transcript excerpt**: Pasted testimony sections (note: partial transcript may limit
  analysis completeness; flag gaps).
- **Multi-transcript set**: Multiple deposition transcripts for witness-comparison analysis.
- **Exhibit log**: Separately provided list of exhibits marked during the deposition.
- **Prior materials** (optional): Prior deposition transcripts, interrogatory answers,
  written statements, expert reports (FRCP 26(a)(2)), or documents marked as exhibits.
- **Playbook** (optional): Case-strategy document defining claim/defense elements, known
  vulnerabilities, conceded issues, and litigation objectives.

If only a partial transcript is provided, note the limitation prominently in the digest.
If no exhibit log is provided, create one from exhibit references identified in the
transcript.

### Step 2: Gather Context (CLARIFY Blocks)

**CLARIFY Block 1: Analysis Objective**
Ask the user to select the primary purpose:

- `Extract admissions and map to claim/defense elements`
- `Assess witness credibility and identify prior inconsistencies`
- `Evaluate expert witness testimony for Daubert/methodological vulnerabilities`
- `Prepare testimony designations for summary judgment motion`
- `Prepare trial designation packet`
- `Comprehensive — all of the above`

_Why this matters_: Pre-SJ/pre-filing digests focus on admissions and element mapping;
pre-trial digests focus on credibility and impeachment value; expert digests require
Daubert framework analysis. The purpose determines output depth and prioritization.

**CLARIFY Block 2: Which Side Are You Analyzing From?**

- `Propounding (our deposition — extracting facts favorable to our case theory)`
- `Defending (opposing party's deposition of our witness — assessing exposure)`
- `Both / settlement evaluation (objective analysis of what testimony does for each side)`

_Why this matters_: RED/GREEN classification flips based on side. The same testimony
that is a RED admission for the opposing party is a GREEN support for the propounding
party. This must be established before classification begins.

**CLARIFY Block 3: Witness Type and Role**

- `Rule 30(b)(6) corporate designee (organization-binding testimony)`
- `Opposing party (individual) — adverse party deposition`
- `Opposing expert witness`
- `Our own expert witness (friendly)`
- `Fact witness favorable to our case`
- `Fact witness adverse or neutral`
- `Rule 30(b)(6) designee of our own organization (check for harmful testimony)`

_Why this matters_: Corporate designee testimony binds the organization under FRE
801(d)(2)(D) and FRCP 32(a)(3). Expert testimony is analyzed against Daubert criteria.
Adverse party testimony is admissible as substantive party-opponent admission. The
foundation requirements and legal significance differ by role.

**CLARIFY Block 4: Case Phase and Strategic Objective**

- `Pre-summary-judgment (identifying elements for SJ motion or opposing SJ)`
- `Pre-trial and trial preparation (credibility and designation planning)`
- `Settlement evaluation (assessing damages/liability corridor)`
- `Post-deposition remediation (our witness — preparing for follow-up deposition)`
- `Appellate-stage (documenting trial record)`

_Why this matters_: The output format and prioritization changes materially by phase.
Pre-SJ work focuses on element sufficiency; pre-trial focuses on credibility sequencing;
settlement focuses on quantifiable exposure.

**CLARIFY Block 5: Deposition Scope and Available Prior Materials**
Select all that apply:

- `Single deposition (standalone analysis)`
- `Part of multi-witness sequence (cross-deposition comparison needed)`
- `Follow-up deposition (testing prior inconsistencies from earlier transcript)`
- `Deposition on topics from prior interrogatory answers (direct comparison available)`

Prior materials available (multi-select):

- Prior deposition transcript of same witness
- Prior interrogatory answers
- Prior written statements (unsworn)
- Expert report (FRCP 26(a)(2)) — relevant if this is expert deposition
- Documents marked as exhibits in this deposition
- Other party's deposition transcripts

_Why this matters_: Multi-deposition analysis requires cross-witness consistency checks.
Prior sworn materials (interrogatory answers, prior depositions) enable FRE 801(d)(1)(A)
substantive inconsistency analysis, not just FRE 613 impeachment.

**CLARIFY Block 6: Digest Format Selection**

- `Page-line digest (sequential; complete record; standard citation format)`
- `Topical digest (organized by subject matter clusters; best for motion writing)`
- `Chronological digest (organized by event timeline; best for narrative cases)`
- `Witness-comparison matrix (cross-referencing multiple depositions on key questions)`
- `Designated testimony packet (curated excerpts for SJ or trial submission)`
- `Comprehensive — generate topical digest with page-line citations and designation recommendations`

_Why this matters_: Page-line digests preserve the full evidentiary record; topical
digests maximize utility for brief writing; witness-comparison matrices expose
cross-witness contradictions. Choose based on the downstream litigation task.

**CLARIFY Block 7: Playbook or Case Theory**

- `Load case-strategy playbook from file (provide path or paste)`
- `Provide key claim/defense elements now (list the elements you need testimony to support
or rebut)`
- `Use general litigation standards without case-specific playbook`

_Why this matters_: A case playbook enables element-by-element mapping. Without it,
the digest uses general evidentiary categories. If elements are provided, the digest
assesses testimony sufficiency against each element explicitly.

### Step 3: Load Legal Authority

Before beginning analysis, load the governing legal framework for the jurisdiction and
dispute type.

**3a. Via legalcode-mcp (if connected):**
Search for:

- Current FRCP Rule 30, 32, 56 text (or applicable state equivalent)
- Applicable FRE rules (801, 613, 608, 609, 901)
- Local rules on deposition procedure and designation deadlines
- Daubert/Frye standard applicable in the forum [VERIFY]
- Key Circuits on 30(b)(6) preparation obligations and sanctions [VERIFY]

Save results to `/tmp/deposition-digest-research-[case-name].md`. Mark confirmed
citations as VERIFIED. Mark unconfirmed ones as [VERIFY].

**3b. Without legalcode-mcp:**
Proceed using the Rule and FRE anchors in the Jurisdiction section above. Mark all
citations with [VERIFY]. Note in the Glass Box: `legalcode_mcp: "Not connected"`.

**3c. Load the playbook (if provided):**
Extract key claim/defense elements, known vulnerabilities, conceded issues, and
litigation objectives. Organize as an element map for use in Step 5.

### Step 4: First-Pass Read and Witness Profile

Before detailed analysis, conduct a first-pass read of the full transcript to establish:

**4a. Witness Profile:**

- Name, title, current employer, and relationship to the litigation
- Deposition date, location, duration (pages / hours)
- Counsel present for each party
- Topics noticed (for 30(b)(6)) or general subject matter
- Exhibits marked (count and initial identification)

**4b. Transcript Quality Check:**

- Note any certification, errata, or read-and-sign provisions
- Identify portions where transcript is unclear ("[inaudible]", "[crosstalk]")
- Flag any interruptions, recesses, or off-the-record segments
- Identify objections with instruction not to answer (note privilege basis if stated)

**4c. Preliminary Credibility Impressions:**

- Identify any immediately apparent hedging language patterns
- Note any questions answered with excessive qualification
- Flag pages with unusual objection density

### Step 5: Element-by-Element Analysis

Map the transcript against claim/defense elements (from playbook if provided, otherwise
use general litigation framework). For each element:

**5a. What testimony exists on this element?**

- Quote the testimony verbatim (do NOT paraphrase admissions or key concessions)
- Record exact page:line citation
- Note context (what question preceded the answer?)

**5b. Classify the testimony:**

**Finding Type (Content-Based):**

| Type                       | Tag                           | Definition                                                                                                            | FRE Character                                                                      |
| -------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **ADMISSION**              | `[ADMISSION]`                 | Party-opponent statement adverse to their litigation position                                                         | FRE 801(d)(2): substantively admissible                                            |
| **HELPFUL TESTIMONY**      | `[HELPFUL]`                   | Testimony supporting our case theory                                                                                  | Generally admissible; credibility determines weight                                |
| **QUALIFIED/AMBIGUOUS**    | `[QUALIFIED]`                 | Testimony that appears favorable but is materially limited by qualifications                                          | Use with caution; opponent will highlight qualifier                                |
| **EVASION**                | `[EVASION]`                   | Response that fails to commit to a factual position; witness redirects or avoids                                      | Possible grounds for motion to compel; cross-examination material                  |
| **NO RECALL**              | `[NO RECALL]`                 | "I don't recall" — current memory failure; witness may later claim refreshed recollection                             | Preserves impeachment option if later testimony changes                            |
| **NO KNOWLEDGE**           | `[NO KNOWLEDGE]`              | "I don't know" — affirmative denial of knowledge; witness cannot later testify to the fact without severe impeachment | Foundation challenge: if no knowledge, testimony may be inadmissible under FRE 602 |
| **DOCUMENT TESTIMONY**     | `[EXHIBIT: No.]`              | Testimony identifying, authenticating, or describing a marked exhibit                                                 | FRE 901 authentication; essential for document admissibility                       |
| **IMPEACHMENT**            | `[IMPEACH: type]`             | Statement inconsistent with prior testimony, document, or co-witness (sub-types below)                                | Depends on sworn vs. unsworn status                                                |
| **INTERNAL CONTRADICTION** | `[INTERNAL: p.X:Y vs. p.A:B]` | Within this deposition, witness contradicts earlier testimony                                                         | No external source needed; powerful impeachment                                    |
| **EXPERT OPINION**         | `[OPINION]`                   | Expert's conclusion or ultimate opinion                                                                               | Subject to Daubert/Frye challenge                                                  |
| **EXPERT BASIS**           | `[BASIS]`                     | Data, methodology, or assumptions underlying expert opinion                                                           | Auditability; challenge pathway                                                    |
| **DAUBERT RISK**           | `[DAUBERT RISK]`              | Methodology not tested, not peer-reviewed, error rate unknown, or not generally accepted                              | Grounds for exclusion motion                                                       |
| **30(b)(6) KNOWLEDGE GAP** | `[30b6 GAP]`                  | Designee claims ignorance on a noticed topic — potential FRCP 30(b)(6) violation                                      | Grounds for FRCP 37 sanctions; motion to compel follow-up deposition               |

**Impeachment Sub-Types:**

| Sub-Type                  | Tag                     | Prior Statement Character       | FRE Treatment                                                   |
| ------------------------- | ----------------------- | ------------------------------- | --------------------------------------------------------------- |
| Internal contradiction    | `[IMPEACH: INTERNAL]`   | Same deposition                 | No hearsay issues; direct comparison                            |
| Prior sworn deposition    | `[IMPEACH: SWORN-DEPO]` | Prior deposition transcript     | FRE 801(d)(1)(A): substantively admissible                      |
| Prior sworn interrogatory | `[IMPEACH: SWORN-ROG]`  | Interrogatory answer (sworn)    | FRE 801(d)(1)(A): substantively admissible                      |
| Prior sworn hearing/trial | `[IMPEACH: SWORN-PROC]` | Testimony at prior proceeding   | FRE 801(d)(1)(A): substantively admissible                      |
| Prior unsworn statement   | `[IMPEACH: UNSWORN]`    | Email, note, informal interview | FRE 613: impeachment only, not substantive                      |
| Document conflict         | `[IMPEACH: DOCUMENT]`   | Contemporaneous document        | FRE 613 for verbal statement; document independently admissible |

**5c. Severity Classification (RED/YELLOW/GREEN):**

| Level      | Definition — Propounding Side                                                                              | Definition — Defending Side                                                                                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **RED**    | Finding is harmful, contradicts case theory, or is a major concession that materially weakens our position | Finding is a significant admission, credibility failure, or Daubert vulnerability that significantly strengthens opponent's case |
| **YELLOW** | Finding is ambiguous, partly helpful but qualified, or a minor concession that is manageable               | Finding is a qualified admission or moderate credibility concern that is explainable but creates some exposure                   |
| **GREEN**  | Finding is supportive, benign, or confirms a favorable narrative element                                   | Finding is unhelpful to opponent, confirms our case facts, or establishes witness credibility                                    |

**5d. Evidentiary Sufficiency Grade:**

| Grade            | Meaning                                                                                                | Admissibility Assessment                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **STRONG**       | Testimony is clear, specific, firsthand, and admissible under FRE                                      | Rely as primary evidence; cite in briefs; use at trial                   |
| **ADEQUATE**     | Testimony is somewhat clear but has minor foundation issues or qualifications                          | Use with corroboration; prepare for foundation challenge                 |
| **WEAK**         | Testimony is vague, speculative, or based on questionable foundation                                   | Do not rely as primary evidence; seek corroborating evidence             |
| **INADMISSIBLE** | Testimony violates FRE (hearsay with no exception, speculation, privilege, lack of personal knowledge) | Do not cite; flag for follow-up discovery to find admissible alternative |

### Step 6: Expert Witness Daubert Analysis

Apply only when deponent is an expert witness. Analyze the four Daubert factors (_Daubert
v. Merrell Dow Pharmaceuticals_, 509 U.S. 579 (1993)) [VERIFY applicable standard — some
states use Frye; verify forum]:

**Factor 1: Testing**

- Has the underlying theory or technique been tested?
- Can it be tested?
- Did the expert perform testing for this case or rely on general principles?

**Factor 2: Peer Review and Publication**

- Has the methodology been subjected to peer review?
- Has it been published in peer-reviewed journals?
- Did the expert cite publications supporting the methodology used here?

**Factor 3: Known or Potential Error Rate**

- Is the error rate known or estimated?
- Are there established standards controlling technique operation?
- Did the expert acknowledge uncertainty ranges?

**Factor 4: General Acceptance**

- Is the methodology generally accepted in the relevant scientific/technical community?
- Did the expert acknowledge any significant dissent or competing methodologies?

**Additional Daubert vulnerabilities to flag:**

- Expert retained specifically for litigation; over 50% of income from litigation work
- Expert only works for one side of cases (plaintiff-only or defense-only)
- Opinion not based on "sufficient facts or data" (FRE 702(b))
- Methodology not consistently applied (cherry-picking data)
- Scope concessions: "I didn't review X," "I wasn't asked to consider Y"
- Extrapolation beyond the supporting data
- Reliance on discredited or non-peer-reviewed materials
- Failure to rule out alternative causation theories

[JURISDICTION-SPECIFIC]: State courts vary on whether they apply Daubert, Frye (general
acceptance only), or a hybrid standard. [VERIFY] the governing standard before framing
Daubert challenges.

### Step 7: 30(b)(6) Corporate Designee Analysis

Apply only when deponent is a Rule 30(b)(6) designee. Conduct an organizational
obligation audit:

**7a. Topic Coverage Audit:**
For each topic in the 30(b)(6) notice:

- Did the designee testify substantively on the topic?
- Did the designee claim ignorance (flag as `[30b6 GAP]`)?
- Was the ignorance explainable (topic was not reasonably available to the organization)
  or potentially sanctionable (organization failed to prepare)?
- Designee's obligation extends to "information known or reasonably available to the
  organization" — not just the designee's personal knowledge. [VERIFY]

**7b. Preparation Obligation Check:**

- Did the designee demonstrate knowledge beyond personal experience (indicating preparation)?
- Did the designee admit they were not prepared on specific topics?
- Was there evidence of improper preparation instructions (coaching to claim ignorance)?

**7c. Binding Effect Assessment:**

- Testimony of a 30(b)(6) designee on noticed topics binds the organization
- Flag any testimony where the designee purported to limit or disclaim the organizational
  binding effect ("I'm only speaking for my department" is typically insufficient)
- For adverse party 30(b)(6): all testimony usable for any purpose under FRCP 32(a)(3);
  no unavailability showing required

**7d. Sanctions Potential:**
If the designee systematically failed on noticed topics:

- Note as FRCP 37(d)(1)(A)(i) potential violation
- Flag for motion for sanctions, including possible preclusion, adverse inference, or
  default [VERIFY sanctions standard in forum]

### Step 8: Exhibit Foundation Audit

For each exhibit marked during the deposition, document:

| Exhibit No. | Description       | Introduction Page:Line | Authentication Testimony          | FRE 901 Basis                                                         | Foundation Status           | Objections                |
| ----------- | ----------------- | ---------------------- | --------------------------------- | --------------------------------------------------------------------- | --------------------------- | ------------------------- |
| Ex. 1       | [Doc description] | [Page:Line]            | [Summary of witness ID testimony] | [FRE 901(b) sub-rule: e.g., b(1) testimony of witness with knowledge] | COMPLETE / PARTIAL / ABSENT | [Any objection and basis] |

**Authentication basis types:**

- FRE 901(b)(1): Testimony of a witness with knowledge that the item is what it is claimed
- FRE 901(b)(4): Distinctive characteristics (appearance, contents, substance)
- FRE 901(b)(9): System or process evidence producing an accurate result

**Flag as `[FOUNDATION GAP]`** any exhibit where:

- The witness disclaimed knowledge of the document
- The witness could not authenticate it
- The witness provided only partial foundation (e.g., recognized document but could not
  establish chain of custody)
- Opposing counsel objected to the foundation and the objection was not cured

### Step 9: Credibility Assessment

Conduct a structured credibility assessment combining transcript-based analysis with
comparison to prior materials.

**9a. Hedging Language and Demeanor Markers (Transcript-Based):**
Flag specific instances of:

- Uncertainty qualifiers: "I think," "I believe," "as far as I know," "I'm not sure but"
  — preserve verbatim; do NOT paraphrase these away
- Sudden recall recovery: claimed no recall, then recalled in detail after document shown
  — tag as `[SUDDEN RECALL: p.X vs. p.Y]`
- Excessive clarification requests: "What do you mean by that?" pattern when questions
  are clear — may signal evasion
- Expanding/contracting narratives: first answer is brief; later answers on same topic
  add significant new detail or significantly contract prior description
- Volunteered information: witness goes well beyond question scope — may signal either
  genuine candor or strategic framing

**Research caution**: Academic research confirms that no single verbal marker reliably
indicates deception. Tag credibility concerns based on factual inconsistencies, not
behavioral speculation. A witness's credibility assessment in this digest must be grounded
in _specific, articulable factual inconsistencies_, not general impressions.

**9b. Cross-Source Consistency Matrix:**

| Source                       | Prior Statement      | Deposition Testimony | Consistent?    | FRE Classification                            | Impact           |
| ---------------------------- | -------------------- | -------------------- | -------------- | --------------------------------------------- | ---------------- |
| Prior deposition (sworn)     | [Text + cite]        | [Text + p.:l.]       | Yes/No/Partial | FRE 801(d)(1)(A) if inconsistent: substantive | RED/YELLOW/GREEN |
| Interrogatory answer (sworn) | [Text + rog no.]     | [Text + p.:l.]       | Yes/No/Partial | FRE 801(d)(1)(A) if inconsistent: substantive | RED/YELLOW/GREEN |
| Email / note (unsworn)       | [Text + doc cite]    | [Text + p.:l.]       | Yes/No/Partial | FRE 613: impeachment only                     | RED/YELLOW/GREEN |
| Other deponent testimony     | [Text + depo cite]   | [Text + p.:l.]       | Yes/No/Partial | Extrinsic: other witness                      | RED/YELLOW/GREEN |
| Expert analysis / report     | [Text + report cite] | [Text + p.:l.]       | Yes/No/Partial | Expert opinion                                | RED/YELLOW/GREEN |
| Documentary evidence         | [Document cite]      | [Text + p.:l.]       | Yes/No/Partial | Document independently admissible             | RED/YELLOW/GREEN |

**9c. Prior Rehabilitation Assessment:**
If the witness's credibility has been attacked, assess potential rehabilitation material:

- FRE 608(a): Can a character witness testify to truthfulness? Is there a track record?
- Prior consistent statements: Only admissible under FRE 801(d)(1)(B) to rebut charges
  of recent fabrication and only if made _before_ the motive to fabricate arose (_Tome_,
  513 U.S. 150). [VERIFY]

### Step 10: Multi-Witness Comparison (If Multiple Depositions Provided)

If more than one deposition transcript is provided, generate a **Contradiction Matrix**:

**Format:** Rows = key factual questions / events. Columns = witnesses. Cells = testimony
summary + citation. Use color-coding (or notation in plain text) for:

- `[CONFIRM]`: Both/all witnesses agree
- `[CONFLICT: W1 vs. W2]`: Witnesses contradict each other
- `[ONE SIDE]`: Only one witness testified on this topic; others silent or evasive

**Multi-witness analysis steps:**

1. Identify the 10-20 most outcome-determinative factual questions in the case
2. Map each witness's testimony on each question
3. For each conflict: assess which version is more credible and why (supported by
   documents, corroborating witnesses, or contemporaneous evidence)
4. Flag conflicts for cross-examination at trial
5. Identify witnesses whose testimony corroborates opponent's narrative — flag as RED
   for the relevant party

### Step 11: Follow-Up Discovery and Strategic Implications

After completing the transcript analysis, identify what the deposition reveals about
remaining discovery needs and strategic implications.

**11a. Evidence Gap Register:**

| Gap                   | Why It Matters         | Can Close? | How?                                         | Priority   |
| --------------------- | ---------------------- | ---------- | -------------------------------------------- | ---------- |
| [Topic X not covered] | [Impact if unresolved] | Yes/No     | [Document request / follow-up depo / expert] | Tier 1/2/3 |

**11b. Follow-Up Deposition Needs:**

- Did opposing counsel's witness admit ignorance on critical topics that require
  organizational knowledge? → 30(b)(6) follow-up deposition on those topics
- Did any witness reference unidentified documents or conversations? → Document requests
  and possible additional depositions
- For expert depositions: Are there additional experts whose work was relied on? Are
  supplemental reports needed?

**11c. Settlement Corridor Implications:**
Assess whether this deposition testimony moves the settlement corridor:

- RED admissions from opposing party → strengthens our position; note specific leverage
  points
- RED findings about our own witness → note exposure; consider whether to counter with
  expert or additional fact witnesses
- Quantify if possible: does this testimony affect damages calculation? (e.g., 30(b)(6)
  testimony on revenue/profits directly affects disgorgement or lost profits damages)

**11d. Playbook Updates:**
If a case-strategy playbook was loaded in Step 3, note:

- Which elements now have strong evidentiary support from this deposition
- Which elements remain unsupported and require additional discovery
- Which previously-conceded issues were reopened or qualified by testimony

### Step 12: Quality Verification Before Delivery

Apply all quality gates before generating the final digest output.

#### Citation Quality Gates

Run these 5 gates silently. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                           | Fail Action                                             |
| -------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Source**     | Every page-line citation references a specific page and line number in the provided transcript | Add citation or mark "[CITATION NEEDED]"                |
| **Format**     | Citations use consistent format: `[Witness] Dep. [Page]:[Line Start]-[Line End], [Date]`       | Fix format                                              |
| **Accuracy**   | Quoted testimony matches the source transcript verbatim                                        | Correct quote or mark "[PARAPHRASED — VERIFY]"          |
| **Domain**     | Analysis stays within the deposition provided; no invented testimony                           | Remove or flag any statement not grounded in transcript |
| **Confidence** | Uncertainty about classification, admissibility, or implications is stated explicitly          | Add confidence qualifier                                |

#### Self-Interrogation for RED Findings

For each finding classified RED, apply this 3-pass review:

**Pass 1 — Evidentiary Chain**: Does the legal characterization (e.g., ADMISSION under
FRE 801(d)(2)) follow correctly from the witness's role and the statement made? Would a
court/judge actually reach this conclusion?

**Pass 2 — Completeness**: Have all relevant portions of the transcript on this topic
been reviewed? Is the RED classification based on isolated testimony that may be explained
by context elsewhere in the transcript?

**Pass 3 — Challenge**: What is the strongest argument that this finding is not as harmful
as classified? Under what circumstances might a reasonable attorney accept this risk
without concern? What rehabilitation or counter-evidence might exist?

#### Confidence Scoring

Apply to each finding's overall reliability and impact assessment:

| Level        | Range     | Meaning                                                 | Action                                                   |
| ------------ | --------- | ------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95–1.00 | Clear statement; clear legal character; no ambiguity    | State with confidence                                    |
| **High**     | 0.80–0.94 | Strong statement with minor qualifications              | State with brief caveat                                  |
| **Probable** | 0.60–0.79 | Good basis but witness hedged or context is complex     | State with reasoning and note qualifier                  |
| **Possible** | 0.40–0.59 | Genuinely ambiguous; could be interpreted multiple ways | Flag both interpretations; recommend professional review |
| **Unlikely** | 0.00–0.39 | Weak basis; speculative characterization                | Do not assert; flag "[UNCERTAIN]"                        |

---

## Deep Analysis Reference: Key Testimony Categories

### Category 1: Admissions Under FRE 801(d)(2)

An admission is a statement by the opposing party (or their agent/designee) that is
adverse to their litigation position. To classify a statement as a party-opponent
admission:

**Checklist:**

- [ ] Identify the speaker: is the deponent the opposing party, an officer, director,
      managing agent, or 30(b)(6) designee of the opposing party?
- [ ] Identify the statement: does the statement concede a fact that the opposing party
      must disprove to prevail?
- [ ] Assess admissibility: FRE 801(d)(2) applies regardless of whether deponent testifies
      at trial; FRCP 32(a)(3) allows use for any purpose at trial
- [ ] Note the confidence level and evidentiary sufficiency grade

**Common admission types in litigation:**

- Knowledge of a defect or problem before the adverse event
- Awareness of a legal obligation and failure to comply
- Authorization of the action at issue
- Receipt of notice or warning
- Deviation from standard practice or internal policy
- Acknowledgment that a representation was made (or not made)
- Concession that a document is accurate, complete, or binding
- Admission that a particular individual had authority

### Category 2: Prior Inconsistent Statements

The sworn vs. unsworn distinction is the critical fork:

**If prior statement was sworn (prior deposition, interrogatory answer, hearing testimony):**

- The inconsistency is admissible as _substantive evidence_ under FRE 801(d)(1)(A)
- The prior statement is not merely for impeachment — it can be used to prove the fact
  asserted in the prior statement
- Tag: `[IMPEACH: SWORN-[type]]`

**If prior statement was unsworn (email, note, informal interview, social media):**

- The inconsistency is admissible only for _impeachment_ (to attack credibility)
- It cannot be used as substantive evidence of the fact asserted
- Extrinsic evidence admissible under FRE 613 if witness is given opportunity to explain
- Tag: `[IMPEACH: UNSWORN]`

**Impeachment sequence for use at trial:**

1. Commit witness to current testimony (deposition or trial)
2. Establish conditions of prior statement (sworn, opportunity to review/correct,
   context)
3. Confront witness with inconsistency
4. Allow witness to explain or deny
5. If denied or implausibly explained: introduce prior statement as extrinsic evidence
   (for sworn statements: substantive; for unsworn: impeachment only)

### Category 3: 30(b)(6) Organizational Testimony

Unlike individual depositions, 30(b)(6) testimony carries special rules:

**What the designee must know:**
The organization must make "a conscientious, good-faith effort" to prepare the designee
with "all information reasonably available" on noticed topics — not just what the
individual designee personally knows. [VERIFY in applicable circuit]

**Binding effect:**
The designee's testimony on noticed topics binds the organization. A party cannot later
disavow 30(b)(6) testimony by claiming the designee was wrong or not fully informed.
This is the "any purpose" rule of FRCP 32(a)(3).

**Knowledge gap flags (`[30b6 GAP]`):**
When a 30(b)(6) designee claims ignorance on a noticed topic:

- Note the specific topic from the notice
- Assess whether the organization's failure to prepare the designee on this topic is
  sanctionable under FRCP 37(d)
- Flag as a priority item for follow-up motion practice

### Category 4: Expert Witness Testimony Analysis

Expert testimony requires additional analytical layers beyond factual testimony:

**Opinion vs. Basis distinction:**

- Opinions are conclusions; they can be excluded if the methodology fails Daubert
- Bases are the factual inputs; they must be "sufficient facts or data" under FRE 702(b)
- A well-founded opinion based on contested facts is different from an opinion based on
  methodologically flawed analysis

**Key Daubert vulnerabilities to flag in deposit:**

1. Expert testified the methodology has not been tested or cannot be tested
2. Expert cannot identify published peer-reviewed support for the methodology used here
3. Expert cannot state an error rate or admitted the error rate is unknown
4. Expert acknowledged the methodology is not generally accepted in the field
5. Expert admitted relying on data provided by retaining counsel rather than independent
   sources
6. Expert's opinion is based on a single variable, ignoring alternative explanations
7. Expert admitted not reviewing key documents or reports that might change the opinion
8. Expert's financial relationship to one side raises bias concern under FRE 608(b)

---

## Prioritization Framework

After classifying all findings, organize them into three priority tiers:

### Tier 1 — Immediate (0-72 hours)

Items requiring immediate action:

- RED admissions that directly establish an element or defeat a defense — notify client
  and trial team immediately
- Daubert vulnerabilities that support an exclusion motion with dispositive effect —
  begin drafting motion to exclude
- 30(b)(6) knowledge gaps warranting sanctions motion — send meet-and-confer letter
- Privilege assertions that may need court review — file motion to compel if appropriate
- Transcript errors or page-line citation errors requiring errata review

### Tier 2 — Near-Term (3-14 days)

Items requiring prompt attention:

- Follow-up depositions or document requests identified in Step 11
- Counter-designation preparation based on testimony discovered
- Amended contentions or case theory revisions based on new admissions
- Expert rebuttal planning if adverse expert testimony revealed significant vulnerabilities
- Settlement position re-evaluation if testimony moves the corridor materially

### Tier 3 — Background (2+ weeks)

Items for systematic incorporation:

- Updating case-strategy playbook with confirmed element support
- Integrating digest findings into trial narrative outline
- Organizing designated testimony packet for pre-trial exchange
- Coordinating with other counsel on multi-witness contradiction strategy
- Preparing cross-examination outline based on credibility weaknesses identified

---

## Anti-Patterns

The following are common deposition digest failures. Verify the output does not exhibit
any of these before delivery.

1. **Assuming evasion means admission**: Witness evasion ("I don't recall") does not
   equal admission. Evasion may indicate memory failure (potential FRE 602 inadmissibility),
   evasion-based impeachment credibility issue, or sanctions-worthy conduct. Analyze each
   separately.

2. **Paraphrasing away legally significant qualifiers**: Summary says "witness confirmed X."
   Actual transcript says "I think X was probably the case." The hedging language is legally
   significant — it may reduce weight, signal credibility issues, or mean the statement is
   insufficient for summary judgment. Preserve qualifiers verbatim in admission flags.

3. **Conflating credibility with accuracy**: A demeanor-based impression that the witness
   was "evasive" does not establish that the testimony is factually wrong. Credibility
   (reliability of witness) is distinct from accuracy (whether testimony aligns with
   objective facts). Base credibility flags on specific, articulable inconsistencies —
   not general impressions.

4. **Missing the significance of non-testimony**: What the witness did NOT testify to can
   be as important as what they said. A 30(b)(6) designee who testified to no knowledge on
   a noticed topic created a potential sanctions ground. A witness who never denied knowledge
   of X may be implicitly conceding it. Review omissions as carefully as admissions.

5. **Treating partial agreements as total victories**: Witness agrees with the premise of a
   question but qualifies the agreement materially ("Yes, we did X, but only because Y").
   The qualifier changes the evidentiary significance. Classify as QUALIFIED, not ADMISSION.

6. **Ignoring witness knowledge and foundation requirements**: Testimony is only as strong
   as the witness's personal knowledge base under FRE 602. If a witness testifies to events
   they did not personally observe, that testimony may be inadmissible. Flag foundation issues
   separately from substantive analysis.

7. **Assuming prior inconsistency automatically wins impeachment**: Witness testified
   differently than in a prior email. But if the witness can explain the difference
   plausibly (e.g., "I was wrong in the email; here's the correct version"), the
   impeachment backfires. Assess explainability before classifying as high-impact.

8. **Failing to distinguish sworn from unsworn prior inconsistencies**: Prior inconsistent
   sworn testimony is admissible substantively under FRE 801(d)(1)(A). Prior inconsistent
   unsworn statements are admissible for impeachment only under FRE 613. Conflating these
   overstates or understates evidentiary impact. Always identify the FRE classification.

9. **Treating expert opinion testimony as undifferentiated facts**: Expert opinions are
   different from fact testimony in both admissibility requirements (Daubert) and weight
   (subject to competing expert). An expert saying "the defect caused the injury" is not
   the same as the witness saying "the product failed." Classify and weight accordingly.

10. **Ignoring the scope of 30(b)(6) binding obligations**: If the deponent is a 30(b)(6)
    designee of an adverse party, their testimony binds the organization — even if they
    were poorly prepared. Do not treat 30(b)(6) designee testimony as merely one person's
    view. Flag the binding character explicitly.

11. **Failing to audit expert witness bias**: Compensation amount, exclusive side
    representation, and prior testimony patterns are cross-examination material, not
    disqualifying factors by themselves. Note them as credibility evidence, not
    disqualification arguments. Daub the Daubert analysis to methodology, not to bias alone.

12. **Missing internal contradictions by not cross-referencing**: A 200-page deposition may
    have witness testimony on a topic in multiple places. Without cross-referencing all
    testimony on a topic, an internal contradiction may be missed. Use topical organization
    (Step 5) specifically to surface these.

13. **Citing AI-generated page-line citations without verification**: AI models hallucinate
    page-line numbers. Every page-line citation in a digest that will be filed or shared
    with opposing counsel must be verified against the original certified transcript.
    Failure to verify exposes counsel to sanctions and credibility damage.

14. **Over-weighting demeanor as credibility evidence**: Written transcript demeanor
    analysis ("witness seemed nervous based on excessive qualification") is inherently
    weaker than factual inconsistency analysis. Courts and juries are skeptical of
    demeanor-based arguments. Ground credibility analysis in factual inconsistencies,
    not transcript impressions.

15. **Treating the deposition digest as the final word**: A deposition is one data point in
    the case. Even strong admissions can be undermined by other evidence, expert testimony,
    subsequent developments, or trial persuasion. Explicitly note what remains uncertain and
    what follow-up is needed.

16. **Omitting adverse testimony from our own witness's deposition**: When analyzing a
    deposition of our own witness (defending), the natural temptation is to catalog only
    the helpful testimony. The digest must honestly capture all harmful testimony as well —
    this is the only way to prepare effective rehabilitation and counter-designations.

---

## Writing Standards

Apply these plain-language standards before delivering the digest:

1. **Preserve verbatim for key findings**: Admissions, key concessions, and qualified
   statements must be quoted verbatim, not paraphrased. Paraphrase only in the "Summary"
   column of tables; always retain the verbatim quote in the "Testimony" column.

2. **Cite specifically**: Every factual claim must include a page:line citation. Never say
   "the witness testified that X" without the page:line reference.

3. **State the FRE classification**: Every admission, inconsistency, or prior statement
   must include the FRE characterization (e.g., "FRE 801(d)(2)(A): party admission;
   substantive use").

4. **Flag uncertainty explicitly**: If classification is uncertain, say so with a confidence
   score rather than choosing a classification and omitting the caveat.

5. **Distinguish side clearly**: Every analysis section must be framed from the perspective
   established in CLARIFY Block 2. If analyzing from both sides, use a two-column format.

6. **Avoid advocacy language in the digest body**: "Devastating admission," "fatal flaw,"
   "clearly shows" are advocacy language for the brief — not appropriate in the digest itself.
   The digest is an analytical tool. Advocacy is for the motion or argument that cites it.

7. **Use active voice in summary sentences**: "Witness admitted X" not "It was admitted
   by the witness that X." Short, direct sentences convey findings more clearly.

8. **Quality gate before delivery**: Run the 5 Citation Quality Gates (Step 12) before
   generating any output. Do not deliver the digest until all gates pass.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current FRCP Rule 30, 32, 56 and applicable FRE rules
- Search for forum-specific local rules on deposition procedure and designation deadlines
- Search for Daubert/Frye standard in the applicable jurisdiction
- Search for current circuit authority on 30(b)(6) preparation obligations
- Save results to `/tmp/deposition-digest-research-[case-name].md`
- Mark all confirmed citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Use the Rule anchors in the Jurisdiction section above
- Mark all citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural quality of the digest (element mapping, classification, consistency
  analysis) rather than jurisdiction-specific legal depth

---

## Output Format Template

````markdown
# Deposition Digest — [Witness Name], [Witness Role]

## Case: [Case Caption / Case Number]

## Digest Prepared: [Date]

---

### I. Executive Summary

**Witness**: [Name], [Title / Role in Case]
**Deposition Date**: [Date] | **Duration**: [Hours / Pages]
**Analysis Side**: [Propounding / Defending / Both]
**Case Phase**: [Pre-SJ / Pre-Trial / Settlement / Other]
**Digest Format**: [Topical / Page-Line / Chronological / Witness-Comparison / Designated]

**Key Findings**:

- [1-2 sentence summary of most important finding]
- [1-2 sentence summary of second most important finding]
- [Add as needed]

**Overall Assessment**: [HIGHLY HELPFUL / MIXED / HARMFUL] to [our/their] case.
**Aggregate Confidence**: [Level] — [1 sentence rationale]

---

### II. Witness and Deposition Context

| Field                    | Detail                                                        |
| ------------------------ | ------------------------------------------------------------- |
| Witness Name             |                                                               |
| Witness Role             | [Party / Officer / Expert / Fact Witness / 30(b)(6) Designee] |
| Employer / Organization  |                                                               |
| Deposition Date          |                                                               |
| Duration                 |                                                               |
| Attorneys Present        |                                                               |
| 30(b)(6) Topics Noticed  | [List or "N/A"]                                               |
| Prior Materials Reviewed | [List]                                                        |
| Total Exhibits Marked    |                                                               |

---

### III. Admissions and Key Findings — Element-by-Element

#### Claim/Defense Element: [Element Name]

| Topic   | Testimony (verbatim) | Citation               | Tag         | Severity | Sufficiency | Confidence  | Action      |
| ------- | -------------------- | ---------------------- | ----------- | -------- | ----------- | ----------- | ----------- |
| [topic] | "[exact quote]"      | [Dep. Page:Line, Date] | [ADMISSION] | RED      | STRONG      | 0.88 — High | [Next step] |

**Finding**: [1-2 sentence analytical summary of significance to this element]
**Why it matters**: [Legal impact — does this satisfy the element? Defeat a defense?]
**FRE Character**: [e.g., FRE 801(d)(2)(A): party-opponent admission; substantively
admissible; FRCP 32(a)(3): usable for any purpose at trial]
**Recommended action**: [Flag for SJ brief / Counter-designate / Prepare rebuttal]

[Repeat for each element]

---

### IV. Expert Witness Analysis (if applicable)

**Expert**: [Name] | **Field**: [Discipline] | **Retained by**: [Party]
**Report Date**: [Date] | **Prior Testimony**: [Yes/No — disclosure]

#### Daubert Assessment

| Factor             | Analysis  | Status                      | Confidence  |
| ------------------ | --------- | --------------------------- | ----------- |
| Testing            | [Summary] | SATISFIES / PARTIAL / FAILS | [0.00-1.00] |
| Peer Review        | [Summary] | SATISFIES / PARTIAL / FAILS | [0.00-1.00] |
| Error Rate         | [Summary] | SATISFIES / PARTIAL / FAILS | [0.00-1.00] |
| General Acceptance | [Summary] | SATISFIES / PARTIAL / FAILS | [0.00-1.00] |

**Overall Daubert Risk**: [LOW / MEDIUM / HIGH] — [1-2 sentence rationale]
**Key Concessions**: [List with citation]
**Scope Gaps**: [What expert did not review or opine on]
**Bias Indicators**: [Financial relationship, exclusive-side history]

---

### V. Credibility Assessment

| Credibility Factor                          | Assessment                             | Evidence            | Severity         | Citation                  |
| ------------------------------------------- | -------------------------------------- | ------------------- | ---------------- | ------------------------- |
| Consistency with prior sworn statements     | [Consistent/Inconsistent/Partial]      | [Summary]           | RED/YELLOW/GREEN | [Dep. Page:Line]          |
| Internal consistency within this deposition | [Consistent/Inconsistent/Partial]      | [Summary]           | RED/YELLOW/GREEN | [Page:Line vs. Page:Line] |
| Candor and response patterns                | [Straightforward/Evasive/Inconsistent] | [Examples]          | RED/YELLOW/GREEN | [Page:Line]               |
| Knowledge and foundation                    | [Strong/Adequate/Weak]                 | [Assessment]        | RED/YELLOW/GREEN | [Page:Line]               |
| Demeanor markers (transcript-based)         | [Observations]                         | [Specific examples] | RED/YELLOW/GREEN | [Page:Line]               |

**Credibility Overall**: [RELIABLE / MIXED / UNRELIABLE]
**Bias Indicators**: [None / Some / Significant — describe]
**Usefulness at Trial**: [Strong / Adequate / Weak / Potentially Counter-Productive]

---

### VI. Impeachment Opportunities

| Topic   | Prior Statement (verbatim)  | Deposition Testimony (verbatim) | Consistency  | FRE Classification          | Impact | Use at Trial?     |
| ------- | --------------------------- | ------------------------------- | ------------ | --------------------------- | ------ | ----------------- |
| [topic] | "[prior]" — [source + cite] | "[current]" — [Dep. Page:Line]  | INCONSISTENT | [801(d)(1)(A): substantive] | RED    | Yes — High Impact |

---

### VII. 30(b)(6) Knowledge Gap Audit (if applicable)

| Noticed Topic       | Coverage              | Designee Response                            | Sanctions Potential | Flag                |
| ------------------- | --------------------- | -------------------------------------------- | ------------------- | ------------------- |
| [Topic from notice] | FULL / PARTIAL / NONE | [Summary of testimony or claim of ignorance] | LOW/MEDIUM/HIGH     | [30b6 GAP] or Clear |

---

### VIII. Exhibit Foundation Audit

| Exhibit No. | Description | Authentication Testimony | FRE 901 Basis | Foundation Status           | Objections |
| ----------- | ----------- | ------------------------ | ------------- | --------------------------- | ---------- |
|             |             |                          |               | COMPLETE / PARTIAL / ABSENT |            |

---

### IX. Cross-Deposition Contradiction Matrix (if multiple depositions)

| Key Issue | Witness A Testimony (cite) | Witness B Testimony (cite) | Consistency          | Impact           |
| --------- | -------------------------- | -------------------------- | -------------------- | ---------------- |
| [Issue]   | [Summary — Dep. Page:Line] | [Summary — Dep. Page:Line] | [CONFIRM / CONFLICT] | RED/YELLOW/GREEN |

---

### X. Designated Testimony Recommendations

**For Summary Judgment:**

| Designation           | Citation              | Supporting Element | Opponent Counter-Designation Risk | Priority   |
| --------------------- | --------------------- | ------------------ | --------------------------------- | ---------- |
| [Excerpt description] | [Dep. Page:Line-Line] | [Element]          | LOW/MEDIUM/HIGH                   | Tier 1/2/3 |

**Designations to Block (if defending):**

| Designation           | Citation              | Harm Assessment | Counter-Designation |
| --------------------- | --------------------- | --------------- | ------------------- |
| [Excerpt description] | [Dep. Page:Line-Line] | [Assessment]    | [Proposed counter]  |

---

### XI. Follow-Up Discovery Priority Register

| Priority | Gap               | Action   | Owner                       | Due      | Expected Outcome  |
| -------- | ----------------- | -------- | --------------------------- | -------- | ----------------- |
| Tier 1   | [Gap description] | [Action] | [Attorney/Paralegal/Expert] | 72h      | [Expected result] |
| Tier 2   | [Gap description] | [Action] |                             | 2 weeks  |                   |
| Tier 3   | [Gap description] | [Action] |                             | 30+ days |                   |

---

### XII. Settlement and Strategic Implications

- **Settlement corridor impact**: [Quantify if possible; note direction]
- **Key leverage points revealed**: [List from RED findings for our side]
- **Exposure points revealed**: [List from RED findings against our side]
- **Playbook updates**: [Elements now confirmed; elements remaining unestablished]
- **Next priority action**: [Most important single next step]

---

### XIII. Quality Assurance Record

- **Citation Quality Gates**: [All passed / Issues identified]
- **Self-Interrogation (RED findings)**: [Performed / Not applicable — no RED findings]
- **Evidentiary foundation audit**: [Complete]
- **Verbatim preservation**: [All key admissions quoted verbatim]

---

### XIV. Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-deposition-digest"
  deposition_type: "[30(b)(6) / expert / adverse-party / friendly-witness / fact-witness]"
  witness_name: "[name]"
  deposition_date: "[date]"
  transcript_pages: "[count or 'partial']"
  topics_noticed: "[list or 'not applicable']"
  jurisdiction: "[court and jurisdiction]"
  side_analyzed: "[propounding / defending / both]"
  case_phase: "[pre-SJ / pre-trial / settlement / post-trial]"
  digest_format: "[topical / page-line / chronological / witness-comparison / designated]"
  prior_materials_reviewed:
    - "[e.g., Prior deposition — [Witness], [Date]]"
    - "[e.g., Interrogatory Answers — [Set No.]]"
    - "[e.g., Expert Report — [Expert], [Date]]"
  playbook_loaded: "[Yes — [file] / No — general standards used]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  admissions_identified: "[count]"
  impeachment_opportunities: "[count]"
  knowledge_gaps: "[count or 'N/A — not 30(b)(6)']"
  daubert_risks: "[count or 'N/A — not expert deposition']"
  red_findings: "[count]"
  yellow_findings: "[count]"
  green_findings: "[count]"
  key_assumptions:
    - "[assumption about incomplete transcript / missing prior materials]"
    - "[assumption about governing law if not confirmed]"
  limitations:
    - "[e.g., Partial transcript analyzed — pp. 1-150 only]"
    - "[e.g., No prior materials provided — consistency analysis limited]"
    - "[e.g., legalcode-mcp not connected — all citations marked [VERIFY]]"
  confidence: "[HIGH | MEDIUM | LOW] — [rationale]"
  reviewer:
    "AI-assisted — requires qualified legal review and citation verification
    against original certified transcript before use in any court submission"
```
````

```

---

## Localization Notes

This skill's primary framework is US federal practice. When analyzing depositions in
other jurisdictions, note the following localization requirements:

**US State Courts**: [JURISDICTION-SPECIFIC] Many states have deposition procedures
substantially similar to the FRCP, but key differences include: time limits, scope of
30(b)(6) equivalents, objection protocols, and expert disclosure requirements. California
CCP § 2025; New York CPLR Article 31; Texas Rules of Civil Procedure §§ 199-203.
[VERIFY applicable state rules before applying federal analysis.]

**England & Wales**: [JURISDICTION-SPECIFIC] Oral depositions (CPR Part 34) are rare in
England & Wales; written witness statements are the primary form of witness evidence.
Hearsay and evidence rules differ substantially from US FRE. The deposition digest format
does not translate directly to witness statement analysis. Consult a qualified English
solicitor or barrister for equivalent analysis.

**International Arbitration**: [JURISDICTION-SPECIFIC] Deposition practice in international
arbitration (ICC, LCIA, SIAC, AAA-ICDR) is not standardized. IBA Rules on the Taking of
Evidence in International Arbitration govern many proceedings. Witness statement formats
and oral testimony procedures differ from US court depositions. [VERIFY applicable
arbitration rules.]

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis from:
- 2-agent parallel research pipeline (Structural Analysis Agent + Legal Research Agent)
- US federal framework: FRCP Rules 30, 32, 56; FRE Rules 801, 613, 608, 609, 901
- Daubert v. Merrell Dow Pharmaceuticals, 509 U.S. 579 (1993)
- Tome v. United States, 513 U.S. 150 (1995)
- ABA litigation practice resources and law review analysis
- Industry benchmark research: Deposely, Lexitas, CaseMark, U.S. Legal Support platforms
- Structural patterns adapted from: legalcode-deposition-preparation (companion skill),
  legalcode-early-case-assessment (quality framework patterns), legalcode-summary-judgment-
  analysis (evidentiary analysis patterns), legalcode-contract-review (gold standard
  classification and quality framework patterns)
- Classification system: 3-tier (Finding Type × Severity × Evidentiary Sufficiency)
  adapted from legalcode-contract-review GREEN/YELLOW/RED framework
```
