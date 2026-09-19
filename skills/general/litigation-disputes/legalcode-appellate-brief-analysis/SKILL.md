---
name: legalcode-appellate-brief-analysis
description: Perform comprehensive appellate-specific analysis of opening briefs, response briefs, reply
  briefs, and petitions for review.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Perform comprehensive appellate-specific analysis of opening briefs, response briefs, reply briefs, and petitions for review. Evaluates preservation of error, standard of review alignment, harmless error vulnerability, jurisdictional sufficiency, record appendix compliance, and appellate advocacy effectiveness. Distinct from general brief analysis by focusing on appellate-specific doctrines: issue preservation, waiver analysis, plain error review availability, mootness/ripeness, harmless error burden, and reversibility assessment. Supports three modes: pre-filing readiness (strengthen your brief), opposing brief vulnerability assessment (identify exploitable weaknesses), and appellate outcome prediction (likelihood of reversal/affirmance). Produces confidence-scored findings with Glass Box audit trail, actionable recommendations, and strategic guidance for oral argument. Jurisdiction-agnostic at baseline with [JURISDICTION-SPECIFIC] markers for US federal (FRAP), England & Wales (CPR Part 52), and Australia (Federal Court Rules).


# Legalcode Appellate Brief Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted appellate brief analysis.
> It does not constitute legal advice. All outputs must be reviewed by qualified legal
> counsel licensed in the relevant jurisdiction before use in any proceeding. Appellate
> procedural rules, standards of review, and case law change frequently; verify all
> authoritative sources before relying on any conclusion. AI analysis may miss nuances
> of judicial temperament, panel composition, circuit culture, and oral argument dynamics
> that experienced appellate practitioners would recognize. Any cited authority marked
> `[VERIFY]` has not been independently validated and must be confirmed before reliance.

---

## Purpose and Scope

This skill performs **appellate-specific analysis** of briefs filed in intermediate
appellate courts and courts of last resort. It evaluates briefs through the lens of
appellate doctrine, focusing on issues that are unique to or dispositive in appellate
practice.

**Key distinction from legalcode-brief-analyzer**: While `legalcode-brief-analyzer`
evaluates general brief quality (IRAC structure, authority quality, writing mechanics),
this skill focuses on appellate-specific doctrines that determine whether an appeal
will succeed or fail:

- **Preservation of error** and waiver analysis
- **Standard of review** selection and consistent application
- **Harmless error** vulnerability and burden allocation
- **Jurisdictional sufficiency** (notice of appeal, final judgment, collateral order)
- **Justiciability** (mootness, ripeness, standing on appeal)
- **Record appendix** compliance and completeness
- **Appellate remedy** appropriateness (reversal, vacatur, remand, affirmance)

The skill is designed for three primary use cases:

1. **Pre-Filing Readiness Assessment**: Evaluate your own appellate brief before filing
   to identify preservation gaps, standard of review errors, and harmless error
   vulnerabilities that could doom the appeal.

2. **Opposing Brief Vulnerability Assessment**: Analyze the opposing party's appellate
   brief to identify unpreserved issues, waived arguments, concessions, and weaknesses
   to exploit in your response.

3. **Appellate Outcome Prediction**: Assess the likelihood of reversal, affirmance, or
   remand based on the strength of preserved issues, standard of review alignment, and
   harmless error analysis.

**Covers:**

- **Preservation analysis**: Did the party preserve the issue below? Is plain error
  review available? What is the waiver risk?
- **Standard of review alignment**: Is the brief framing arguments consistent with the
  applicable standard? Is it maximizing or minimizing deference appropriately?
- **Harmless error assessment**: If error is found, can the opposing party show
  harmlessness? What is the prejudice burden?
- **Jurisdictional review**: Is the appeal from a final judgment? Was the notice of
  appeal timely? Are interlocutory issues properly certified?
- **Justiciability screening**: Has mootness developed? Is the issue ripe? Does
  standing persist on appeal?
- **Record appendix audit**: Does the appendix contain all necessary materials? Are
  record citations accurate and complete?
- **Appellate remedy analysis**: What remedy is sought? Is it appropriate given the
  error alleged? What happens on remand?
- **Panel/court composition analysis**: Are there signals about judicial philosophy
  or circuit precedent that affect likelihood of success?
- **Oral argument preparation**: What issues are likely to draw questions? Where are
  the hot spots?

**Does not:**

- Perform full writing quality analysis (see `legalcode-brief-analyzer` for that)
- Draft appellate briefs (see `legalcode-opposition-brief-drafter` for drafting)
- Serve as a citator (flags for verification, does not confirm authority status)
- Replace appellate counsel's judgment on strategy or panel dynamics
- Assess factual merits beyond record support analysis

**Related skills:**

- `legalcode-brief-analyzer` — General brief quality analysis (IRAC, authority, writing)
- `legalcode-summary-judgment-analysis` — Summary judgment motion analysis
- `legalcode-early-case-assessment` — Pre-discovery litigation evaluation
- `legalcode-opposition-brief-drafter` — Drafting opposition/response briefs
- `legalcode-case-timeline-builder` — Litigation chronology construction

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the appellate court and
governing procedural rules first, then localize all analysis dimensions accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Appellate procedural rules (FRAP, CPR Part 52, Federal Court Rules)
- Standards of review nomenclature and applicable tests
- Preservation requirements and waiver doctrine
- Harmless error standards (constitutional vs. non-constitutional)
- Notice of appeal timing and content requirements
- Final judgment rule and exceptions (collateral order, certified interlocutory)
- Record appendix requirements (joint appendix, deferred appendix, excerpts)
- Briefing page/word limits and format requirements
- Oral argument customs and panel composition

---

## Reference Anchors by Jurisdiction

### US Federal (FRAP)

**Notice of Appeal**:

- **Timing**: 30 days from entry of judgment (60 days if US is a party). FRAP 4(a)(1)
  [VERIFY]
- **Jurisdictional**: Bowles v. Russell, 551 U.S. 205 (2007) — timely filing is
  jurisdictional; cannot be waived or extended by equitable tolling [VERIFY]
- **Content**: Must specify judgment appealed and parties. FRAP 3(c) [VERIFY]
- **Cross-appeal**: 14 days after first notice or within original period. FRAP 4(a)(3)
  [VERIFY]

**Final Judgment Rule**:

- **General rule**: Appeals only from "final decisions." 28 U.S.C. Section 1291 [VERIFY]
- **Collateral order doctrine**: Cohen v. Beneficial Industrial Loan Corp., 337 U.S.
  541 (1949) — immediately appealable if (1) conclusive, (2) important, (3) effectively
  unreviewable on appeal from final judgment [VERIFY]
- **Certified interlocutory**: 28 U.S.C. Section 1292(b) — district court certifies
  controlling question of law; circuit grants leave [VERIFY]
- **Mandamus**: As safety valve for otherwise unreviewable orders. 28 U.S.C. Section
  1651 [VERIFY]

**Standards of Review**:
| Standard | Applies To | Appellant Burden | Key Language |
|----------|-----------|------------------|--------------|
| **De novo** | Questions of law, statutory interpretation, constitutional issues | Show legal error | "We review de novo" |
| **Clear error** | Factual findings (bench trial) | Definite and firm conviction of mistake | "Clearly erroneous" |
| **Abuse of discretion** | Evidentiary rulings, sanctions, case management | No reasonable basis | "Abuse of discretion" |
| **Substantial evidence** | Agency factfinding (APA) | No reasonable mind could accept | "Substantial evidence" |
| **Plain error** | Unpreserved issues | (1) error, (2) plain, (3) substantial rights, (4) integrity | "Forfeited but plain" |
| **Mixed questions** | Law/fact mix | Depends on dominant character | Varies by issue |

**Harmless Error**:

- **Non-constitutional**: "More probable than not" affected outcome. FRE 103; FRCP 61
  [VERIFY]
- **Constitutional (Chapman)**: Harmless beyond a reasonable doubt. Chapman v.
  California, 386 U.S. 18 (1967) [VERIFY]
- **Structural error**: Never harmless — automatic reversal (denial of counsel, biased
  judge, denial of public trial) [VERIFY]

**Preservation Requirements**:

- **General rule**: Must raise issue in district court with sufficient specificity to
  allow ruling. FRE 103(a); FRCP 46 [VERIFY]
- **Waiver vs. forfeiture**: Waiver = intentional relinquishment; forfeiture = failure
  to raise. Plain error review applies to forfeiture, not waiver [VERIFY]
- **Contemporaneous objection**: For trial errors, objection at time of ruling. FRE
  103(a)(1) [VERIFY]
- **Post-trial motions**: Some issues require Rule 50/59 motion to preserve for appeal
  [VERIFY]

**Plain Error Review** (Federal):

- Four prongs: (1) Error occurred; (2) Error was "plain" (clear or obvious); (3) Error
  affected substantial rights (prejudice); (4) Error seriously affects fairness,
  integrity, or public reputation of judicial proceedings
- Puckett v. United States, 556 U.S. 129 (2009) [VERIFY]
- Fourth prong rarely satisfied — "reserved for exceptional cases" [VERIFY]

**December 2025 FRAP Amendments**:

- Rule 6 (bankruptcy appeals): Clarified procedures for direct appeals and record
  handling [VERIFY]
- Rule 39 (costs): Modified allocation defaults and post-judgment reconsideration
  procedures [VERIFY]
- No changes to Rules 3, 4, 28, or core appellate doctrines [VERIFY]

### England & Wales (CPR Part 52)

**Permission to Appeal**:

- Required for most appeals; may be granted by lower court or Court of Appeal [VERIFY]
- Test: Real prospect of success OR other compelling reason. CPR 52.6(1) [VERIFY]

**Standards**:
| Standard | Applies To | Test |
|----------|-----------|------|
| **Appeal allowed** | Error of law, serious procedural or other irregularity causing injustice | CPR 52.21 [VERIFY] |
| **Review not rehearing** | General principle | CPR 52.21(1) [VERIFY] |
| **Fresh evidence** | Ladd v Marshall criteria | (1) Not obtainable at trial, (2) would have influenced result, (3) apparently credible [VERIFY] |
| **Perversity** | Factual findings | No reasonable tribunal could have reached conclusion [VERIFY] |

**Skeleton Arguments**:

- Length: Not more than 25 pages for appeal skeletons. PD 52A para 5.10 [VERIFY]
- Content: Summary of dispute, chronology, issues, discussion with propositions and
  authority [VERIFY]
- Filing: Appellant 21 days after notice; respondent 14 days before hearing [VERIFY]

**October 2023 Changes**:

- Part 52 substituted; PD 52 revoked; core "real prospect" test unchanged [VERIFY]

### Australia (Federal Court)

**Leave to Appeal**:

- Required for interlocutory decisions. FCR 36.01 [VERIFY]
- Test: Whether decision attended with sufficient doubt AND substantial injustice if
  leave refused [VERIFY]

**Standards**:
| Standard | Applies To | Test |
|----------|-----------|------|
| **Error of law** | Legal questions | Full Federal Court determines correct position |
| **House v The King** | Discretionary decisions | Error of principle, irrelevant consideration, plainly unreasonable |
| **No evidence** | Factual findings | No evidence at all or finding unreasonable |

**Appeal Books**:

- Appeal book required with relevant documents [VERIFY]
- Outline of submissions: 20-30 pages typical [VERIFY]

---

## Interactive Clarification

Use interactive clarification whenever the answer materially changes analysis scope,
evaluation criteria, or output emphasis. If information is already provided, skip the
question. Proceed with stated defaults when the user does not respond.

**CLARIFY block 1: Analysis objective**

- Options: `pre-filing readiness (strengthen your brief)`, `opposing brief vulnerability
(identify weaknesses to exploit)`, `appellate outcome prediction (likelihood assessment)`,
  `comprehensive (all modes)`
- Default: `pre-filing readiness (strengthen your brief)`
- Why it matters: Pre-filing focuses on fixable weaknesses; opposing brief mode emphasizes
  exploitable gaps and response strategy; prediction mode assesses outcome likelihood.

**CLARIFY block 2: Brief type**

- Options: `opening brief (appellant/petitioner)`, `response/answering brief
(appellee/respondent)`, `reply brief`, `petition for certiorari/review`, `opposition
to petition`, `amicus brief`, `cross-appeal brief`
- Default: `opening brief (appellant/petitioner)`
- Why it matters: Opening briefs bear burden of showing error and preservation; response
  briefs can argue waiver, harmless error, and alternative affirmance grounds; reply
  briefs have limited scope.

**CLARIFY block 3: Your side**

- Options: `appellant/petitioner (seeking reversal)`, `appellee/respondent (seeking
affirmance)`, `cross-appellant`, `amicus curiae`, `evaluating neutrally`
- Default: `appellant/petitioner (seeking reversal)`
- Why it matters: Determines burden allocation analysis and framing of recommendations.
  Appellants must show error AND prejudice; appellees need only show one of: no error,
  waiver, or harmless error.

**CLARIFY block 4: Court and jurisdiction**

- Options: `US federal circuit (specify)`, `US Supreme Court`, `US state appellate
(specify)`, `US state supreme (specify)`, `England & Wales Court of Appeal`, `England
& Wales Supreme Court`, `Australia Federal Court Full Court`, `Australia High Court`,
  `other (specify)`
- Default: `US federal circuit`
- Why it matters: Determines applicable procedural rules, standards of review, and
  circuit/court precedent culture.

**CLARIFY block 5: Appeal posture**

- Options: `appeal from final judgment`, `interlocutory appeal (certified)`, `collateral
order appeal`, `mandamus/prohibition`, `habeas corpus`, `bankruptcy appeal`, `agency
review (APA)`, `other specialized appeal`
- Default: `appeal from final judgment`
- Why it matters: Interlocutory and collateral order appeals have additional jurisdictional
  requirements; agency appeals have different standards; habeas has unique procedural rules.

**CLARIFY block 6: Issues on appeal**

- Prompt: "What are the primary issues on appeal? (List briefly or state 'review the
  brief to identify')"
- Default: `review the brief to identify`
- Why it matters: If issues are known, can immediately assess preservation status and
  standard of review alignment. If unknown, will extract from brief.

**CLARIFY block 7: Preservation concerns**

- Options: `no known preservation issues`, `some issues may be unpreserved`, `preservation
is the central concern`, `plain error will be argued`, `unknown — assess from record`
- Default: `unknown — assess from record`
- Why it matters: If preservation is already known to be problematic, analysis can focus
  on plain error availability and harm mitigation.

**CLARIFY block 8: Available materials**

- Options: `brief only`, `brief + lower court opinion`, `brief + record excerpts`, `brief
  - opposing brief`, `full briefing set + record + opinions`, `brief + oral argument
    transcript (if available)`
- Default: `brief only`
- Why it matters: With the lower court opinion, can assess whether arguments track the
  actual ruling. With the opposing brief, can identify exploitation opportunities. With
  oral argument transcript, can assess how issues played with the panel.

**CLARIFY block 9: Analysis depth**

- Options: `quick scan (high-level viability)`, `standard review (issue-by-issue)`,
  `deep dive (element-by-element with record audit)`, `full appellate assessment (outcome
prediction with confidence intervals)`
- Default: `standard review (issue-by-issue)`
- Why it matters: Quick scan for early strategy decisions; deep dive for pre-filing
  quality assurance or critical opposition work; full assessment for prediction.

---

## Workflow

### Step 1: Accept input materials

Accept materials in any of these formats:

- **File path(s)**: Read documents directly (PDF, DOCX, TXT, MD)
- **Pasted text**: Accept inline brief text
- **URL**: Fetch from PACER, court website, SSRN, or document management system
- **Multiple files**: For full briefing sets, accept paths to all documents

If documents are PDFs, convert:

```bash
pandoc "$FILE" -t markdown -o "${FILE%.pdf}.md" 2>/dev/null || pdftotext "$FILE" "${FILE%.pdf}.txt"
```

Identify and categorize each document:

- Opening brief (appellant/petitioner)
- Response/answering brief (appellee/respondent)
- Reply brief
- Joint appendix / Record excerpts
- Lower court opinion(s)
- Trial transcript excerpts
- Petition for certiorari/review
- Oral argument transcript

### Step 2: Gather context via interactive clarification

Run through CLARIFY blocks 1-9, skipping any already answered by the initial prompt.
Record all responses (and defaults used) in the Glass Box audit trail.

### Step 3: Jurisdictional sufficiency check

Before analyzing substance, verify that the appeal is properly before the court:

**3a. Notice of appeal / Leave to appeal:**

| Requirement                       | Assessment  | Notes                                     |
| --------------------------------- | ----------- | ----------------------------------------- |
| **Timely filed**                  | Y/N/Unknown | [Check if brief states compliance]        |
| **Proper parties named**          | Y/N/Unknown | [All necessary parties?]                  |
| **Final judgment / Proper basis** | Y/N/Unknown | [Final, interlocutory, collateral order?] |
| **Leave granted (if required)**   | Y/N/N-A     | [For interlocutory or permission appeals] |

**3b. Finality issues:**

- Is the judgment appealed final under the jurisdiction's rules?
- If interlocutory: Was certification obtained? Was leave granted?
- If collateral order: Does the order satisfy all three Cohen prongs?
- Are there outstanding claims or parties that defeat finality?

**3c. Justiciability screening:**

| Issue                    | Status                  | Impact                                                |
| ------------------------ | ----------------------- | ----------------------------------------------------- |
| **Mootness**             | Live controversy?       | [Settlement, changed circumstances, statutory change] |
| **Ripeness**             | Ready for adjudication? | [Contingent, hypothetical, speculative harms?]        |
| **Standing (appellate)** | Injury persists?        | [Appellant still aggrieved?]                          |

If jurisdictional issues are identified, classify as **CRITICAL** — they are threshold
and dispositive.

### Step 4: Issue identification and extraction

Map every issue raised in the brief:

**4a. Issue inventory:**

| Issue # | Issue Statement | Standard of Review         | Preservation Status             | Brief Section  |
| ------- | --------------- | -------------------------- | ------------------------------- | -------------- |
| 1       | [issue]         | [de novo/clear error/etc.] | [Preserved/Unpreserved/Unclear] | [page/section] |
| 2       | [issue]         | [standard]                 | [status]                        | [location]     |

**4b. For each issue, document:**

- How the brief frames the issue
- What the brief states as the standard of review
- Where the brief claims preservation occurred
- The record cite for the preservation (objection, motion, ruling)
- Whether the issue was raised below in substantially the same form

**4c. Issue selection assessment:**

- Are the strongest issues leading?
- Are weak issues diluting strong ones?
- Are there "kitchen sink" issues that undermine credibility?
- Are issues properly separated or improperly combined?

### Step 5: Preservation of error analysis

This is often the most critical appellate analysis. For each issue:

**5a. Preservation checklist:**

| Criterion                                       | Issue 1     | Issue 2 | Issue 3 |
| ----------------------------------------------- | ----------- | ------- | ------- |
| **Raised below**                                | Y/N/Unclear |         |         |
| **Timely raised**                               | Y/N/Unclear |         |         |
| **Specifically raised** (not just "foundation") | Y/N         |         |         |
| **Ruling obtained**                             | Y/N         |         |         |
| **Ruling on the record**                        | Y/N         |         |         |
| **Same legal theory below and on appeal**       | Y/N         |         |         |
| **Post-trial motion required?**                 | Y/N/N-A     |         |         |
| **Post-trial motion filed?**                    | Y/N/N-A     |         |         |

**5b. Waiver vs. Forfeiture:**

For each unpreserved issue, classify:

| Issue   | Waiver or Forfeiture? | Plain Error Available? | Why?                                             |
| ------- | --------------------- | ---------------------- | ------------------------------------------------ |
| [issue] | Waiver / Forfeiture   | Y/N                    | [Waiver = intentional; forfeiture = inadvertent] |

**5c. Plain error viability (for forfeited issues):**

If plain error review applies, assess each prong:

| Prong                     | Assessment   | Notes                                 |
| ------------------------- | ------------ | ------------------------------------- |
| **1. Error**              | Y/N/Arguable | [Was there actually an error?]        |
| **2. Plain**              | Y/N/Arguable | [Was it clear at time of appeal?]     |
| **3. Substantial rights** | Y/N/Arguable | [Did it affect outcome?]              |
| **4. Fairness/integrity** | Y/N/Arguable | [Seriously affects judicial process?] |

**Red flags in preservation:**

- Brief asserts issue was "raised" but cites only a general pleading, not a specific
  objection or motion
- Brief cites a different legal theory below than is argued on appeal
- Objection was made but overruled; no contemporaneous exception preserved
- Issue raised for the first time in post-trial motion (may be insufficient)
- Issue raised only in footnote or passing reference below
- Issue raised but then abandoned during trial

### Step 6: Standard of review analysis

**6a. Standard identification per issue:**

| Issue     | Brief's Stated Standard | Correct Standard    | Assessment                  |
| --------- | ----------------------- | ------------------- | --------------------------- |
| [issue 1] | [what brief says]       | [what it should be] | CORRECT / INCORRECT / MIXED |

**6b. Standard of review red flags:**

- Brief states de novo review for factual findings
- Brief applies clear error to pure legal question
- Brief argues abuse of discretion for summary judgment (legal question = de novo)
- Brief conflates standards across issues
- Brief states standard but frames argument inconsistent with it
- Brief does not state standard at all (violates FRAP 28(a)(9)(B))
- Brief applies wrong jurisdiction's standard nomenclature
- [POST-LOPER BRIGHT] Brief invokes Chevron deference (overruled 2024) [VERIFY]

**6c. Standard of review leverage assessment (for appellees):**

For appellee/respondent briefs, assess whether the brief maximizes deferential standards:

| Issue     | Deferential Standard Available? | Brief Exploits Deference?      |
| --------- | ------------------------------- | ------------------------------ |
| [issue 1] | Y/N                             | Fully / Partially / Not at all |

### Step 7: Harmless error vulnerability analysis

**7a. Error classification:**

For each alleged error, classify:

| Error     | Type                                             | Harmless Error Standard | Burden               |
| --------- | ------------------------------------------------ | ----------------------- | -------------------- |
| [error 1] | Constitutional / Non-constitutional / Structural | [standard]              | [appellant/appellee] |

**7b. Harmless error framework:**

| Error Type                   | Standard                                | Burden on                     | Effect                     |
| ---------------------------- | --------------------------------------- | ----------------------------- | -------------------------- |
| **Non-constitutional**       | More probable than not affected outcome | Appellant to show prejudice   | Reversible if prejudicial  |
| **Constitutional (Chapman)** | Harmless beyond a reasonable doubt      | Appellee to show harmlessness | Reversible unless harmless |
| **Structural**               | Per se reversible                       | N/A                           | Automatic reversal         |

**7c. Prejudice assessment:**

For each error, assess the likelihood of showing prejudice (for appellant) or
harmlessness (for appellee):

| Error     | Prejudice Showing    | Harmlessness Defense | Overall Assessment                  |
| --------- | -------------------- | -------------------- | ----------------------------------- |
| [error 1] | Strong/Weak/Moderate | Strong/Weak/Moderate | Likely reversible / Likely harmless |

**Factors affecting harmless error analysis:**

- Was the error isolated or pervasive?
- Was there overwhelming evidence of guilt/liability independent of the error?
- Did the error affect central vs. peripheral issue?
- Was the error cumulative with other errors?
- Did counsel exploit the error (e.g., argue erroneously admitted evidence)?
- What would the outcome likely have been absent the error?

### Step 8: Record and appendix compliance

**8a. Appendix completeness:**

| Required Element            | Present? | Location  | Notes                    |
| --------------------------- | -------- | --------- | ------------------------ |
| **Docket entries**          | Y/N      | JA [page] | [Complete or selective?] |
| **Judgment/order appealed** | Y/N      | JA [page] | [Correct version?]       |
| **Lower court opinion**     | Y/N      | JA [page] |                          |
| **Notice of appeal**        | Y/N      | JA [page] |                          |
| **Relevant pleadings**      | Y/N      | JA [page] |                          |
| **Key transcript excerpts** | Y/N      | JA [page] | [All cited portions?]    |
| **Key exhibits**            | Y/N      | JA [page] | [All cited exhibits?]    |

**8b. Record citation audit:**

Sample 5-10 record citations from the brief and verify:

| Brief Citation | Appendix Location | Accurate? | Notes                            |
| -------------- | ----------------- | --------- | -------------------------------- |
| JA 45          | [check]           | Y/N       | [Does it say what brief claims?] |
| Tr. 123:4-10   | [check]           | Y/N       |                                  |

**8c. Record citation red flags:**

- Citations to materials not in the appendix
- General citations ("see Tr." without page/line)
- Citations that do not support the proposition stated
- Missing preservation moments (where objection should be cited)
- Missing key evidence supporting dispositive facts

### Step 9: Argument structure and appellate advocacy assessment

**9a. Theory of the case:**

- Is there a clear, unifying theme across all issues?
- Do all arguments point toward a single theory of reversal (or affirmance)?
- Is the requested remedy clear and consistent with the theory?

**9b. Issue ordering:**

| Assessment                                      | Classification |
| ----------------------------------------------- | -------------- |
| Strongest issue leads                           | STRONG         |
| Issues in logical order but strongest not first | NEEDS WORK     |
| Weakest or frivolous issue leads                | VULNERABLE     |
| No discernible organizational logic             | CRITICAL       |

**9c. Response brief effectiveness (for appellee briefs):**

| Criterion                             | Assessment |
| ------------------------------------- | ---------- |
| Addresses every issue raised          | Y/N        |
| Offers alternative affirmance grounds | Y/N        |
| Leverages deferential standards       | Y/N        |
| Argues waiver where available         | Y/N        |
| Argues harmless error where available | Y/N        |
| Has independent statement of facts    | Y/N        |
| Reframes issues favorably             | Y/N        |

**9d. Reply brief constraints (for reply briefs):**

| Criterion                               | Assessment |
| --------------------------------------- | ---------- |
| Responds only to answering brief        | Y/N        |
| No new issues raised                    | Y/N        |
| Highlights appellee's concessions       | Y/N        |
| Addresses new authorities from appellee | Y/N        |
| No new evidence introduced              | Y/N        |

### Step 10: Appellate remedy analysis

**10a. Remedy requested:**

| Remedy                                           | Sought? | Appropriate? | Notes |
| ------------------------------------------------ | ------- | ------------ | ----- |
| **Reversal with instructions to enter judgment** | Y/N     | [assessment] |       |
| **Reversal and remand for new trial**            | Y/N     | [assessment] |       |
| **Reversal and remand for further proceedings**  | Y/N     | [assessment] |       |
| **Vacatur and remand**                           | Y/N     | [assessment] |       |
| **Affirmance**                                   | Y/N     | [assessment] |       |
| **Modification of judgment**                     | Y/N     | [assessment] |       |

**10b. Remedy-error alignment:**

Does the requested remedy match the error alleged?

| Error   | Natural Remedy               | Requested Remedy      | Alignment        |
| ------- | ---------------------------- | --------------------- | ---------------- |
| [error] | [what would normally follow] | [what brief requests] | Match / Mismatch |

**Common remedy issues:**

- Requesting entry of judgment when remand for new trial is the most appellate court
  could order
- Requesting vacatur when affirmance with modification is more appropriate
- Not specifying what should happen on remand
- Requesting remedy that exceeds scope of appealed issues

### Step 11: Opposing brief exploitation (for opposing brief analysis mode)

When analyzing the opposing party's brief, identify:

**11a. Preservation vulnerabilities:**

| Issue   | Preservation Problem             | Exploitation Strategy                              |
| ------- | -------------------------------- | -------------------------------------------------- |
| [issue] | [unpreserved / waived / unclear] | [Argue waiver; if forfeited, argue no plain error] |

**11b. Concession inventory:**

| Page   | Concession                        | Strategic Value |
| ------ | --------------------------------- | --------------- |
| [page] | [explicit or implicit concession] | [how to use it] |

**11c. Internal contradictions:**

| Location 1     | Location 2     | Contradiction                  |
| -------------- | -------------- | ------------------------------ |
| [page/section] | [page/section] | [description of inconsistency] |

**11d. Unaddressed arguments:**

| Your Argument              | Addressed by Opponent? | Exploitation                        |
| -------------------------- | ---------------------- | ----------------------------------- |
| [argument from your brief] | Y/N/Inadequately       | [If not addressed, hammer in reply] |

**11e. Harmless error vulnerability:**

If the opposing brief establishes error, assess:

- How strong is their prejudice showing?
- What harmless error arguments are available?
- Is there overwhelming untainted evidence?

### Step 12: Appellate outcome prediction

**12a. Issue-by-issue viability:**

| Issue     | Preservation                     | Standard   | Merits Strength      | Harmless Error Risk | Overall Viability   |
| --------- | -------------------------------- | ---------- | -------------------- | ------------------- | ------------------- |
| [issue 1] | Preserved / Plain Error / Waived | [standard] | Strong/Moderate/Weak | High/Medium/Low     | HIGH / MEDIUM / LOW |

**12b. Outcome probability (for full assessment mode):**

| Outcome                                | Probability | Rationale                             |
| -------------------------------------- | ----------- | ------------------------------------- |
| **Full reversal**                      | [0-100%]    | [reasons]                             |
| **Partial reversal (on which issues)** | [0-100%]    | [reasons]                             |
| **Remand without reversal**            | [0-100%]    | [reasons]                             |
| **Affirmance**                         | [0-100%]    | [reasons]                             |
| **Dismissal (jurisdictional)**         | [0-100%]    | [if jurisdictional issues identified] |

**12c. Circuit/panel factors:**

- Does the circuit have relevant precedent favoring one side?
- Are there circuit splits relevant to the issues?
- Is en banc review a possibility if panel rules adversely?
- Is certiorari a realistic option if circuit affirms?
- [If panel known] Any judicial philosophy indicators?

### Step 13: Quality verification

Before delivering the analysis, run quality checks:

**13a. Citation Quality Gates:**

| Gate           | Rule                                      | Status    |
| -------------- | ----------------------------------------- | --------- |
| **Source**     | Every legal proposition cites authority   | PASS/FAIL |
| **Format**     | Citations in proper format                | PASS/FAIL |
| **Currency**   | Authorities flagged for verification      | PASS/FAIL |
| **Domain**     | Analysis limited to selected jurisdiction | PASS/FAIL |
| **Confidence** | Uncertainty explicitly stated             | PASS/FAIL |

**13b. Self-Interrogation (for CRITICAL findings):**

For each outcome-determinative finding (especially preservation and jurisdictional
issues):

1. **Legal chain integrity**: Does this finding follow from the cited rules and record?
2. **Completeness**: Have all relevant doctrines been considered (e.g., all exceptions
   to waiver)?
3. **Adversarial challenge**: What is the strongest counter-argument?

**13c. Confidence scoring:**

| Finding   | Confidence                               | Rationale |
| --------- | ---------------------------------------- | --------- |
| [finding] | Definite/High/Probable/Possible/Unlikely | [basis]   |

### Step 14: Deliver findings

Compile all findings into the Output Format Template (see below). Present findings in
priority order: CRITICAL (jurisdictional, preservation waiver) first, then HIGH
(standard of review errors, weak harmless error showing), then MEDIUM, then ADVISORY.

---

## Appellate-Specific Analysis Framework

Evaluate all 12 appellate domains unless explicitly scoped down:

| Domain                        | What to Assess                                       | Critical Signals                        | Common Red Flags                               |
| ----------------------------- | ---------------------------------------------------- | --------------------------------------- | ---------------------------------------------- |
| 1. Jurisdictional sufficiency | Finality, timeliness, proper basis                   | Notice of appeal, final judgment, leave | Late notice, nonfinal order, no leave          |
| 2. Justiciability             | Mootness, ripeness, standing                         | Live controversy, actual injury         | Settlement, changed law, hypothetical          |
| 3. Issue preservation         | Raised below, timely, specifically, ruling obtained  | Objection on record, ruling             | General objection, no ruling, different theory |
| 4. Plain error availability   | Four prongs satisfied for unpreserved issues         | Clear error, prejudice, integrity       | Prong 3 or 4 not satisfied                     |
| 5. Standard of review         | Correct identification and consistent application    | Standard stated, arguments aligned      | Wrong standard, argument drift                 |
| 6. Harmless error exposure    | Constitutional/non-constitutional, burden allocation | Prejudice shown, overwhelming evidence  | Weak prejudice showing                         |
| 7. Record appendix compliance | Completeness, citation accuracy                      | All materials included, accurate cites  | Missing key materials, inaccurate cites        |
| 8. Argument structure         | Theory coherence, issue ordering, advocacy           | Clear theme, strongest first            | Kitchen sink, no theme                         |
| 9. Reply brief scope          | Only responds to answering brief                     | No new issues, highlights concessions   | New arguments, new evidence                    |
| 10. Remedy appropriateness    | Error-remedy alignment                               | Reversal/remand matches error           | Overreaching remedy                            |
| 11. Oral argument preparation | Hot spots, likely questions                          | Preservation, standard, harmless        | Unprepared for waiver/harmless questions       |
| 12. Strategic positioning     | Circuit precedent, panel composition                 | Favorable precedent cited               | Adverse precedent unaddressed                  |

---

## Risk Classification

Classify each finding using this appellate-specific framework:

| Class        | Meaning                                                                                 | Typical Response                                                                  |
| ------------ | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **CRITICAL** | Jurisdictional defect, complete waiver, or guaranteed affirmance — appeal will fail     | Immediate attention; may require dismissal acknowledgment or withdrawal           |
| **HIGH**     | Significant preservation or standard of review problem affecting multiple issues        | Address before filing; likely subject of motion to dismiss or affirmance argument |
| **MEDIUM**   | Noteworthy weakness but not dispositive — harmless error likely, weak prejudice showing | Cure if possible; prepare response argument                                       |
| **LOW**      | Minor issue or best-practice suggestion                                                 | Note for improvement                                                              |
| **ADVISORY** | Strategic observation, not a deficiency                                                 | Consider for oral argument preparation                                            |

---

## Actionable Output Per Finding

For each MEDIUM/HIGH/CRITICAL finding, provide:

- **Finding summary**: One-sentence description
- **Appellate doctrine**: Which doctrine applies (preservation, harmless error, etc.)
- **Impact**: Effect on appeal outcome
- **Record/authority basis**: What supports this finding
- **Verification status**: `VERIFIED` or `[VERIFY]`
- **Recommended action**: Specific step to take
- **Priority**: Immediate / Near-term / If time permits
- **Expected effect**: How addressing this changes the analysis

---

## Prioritization Framework

| Tier       | Label     | Criteria                                                                              | Timing                    |
| ---------- | --------- | ------------------------------------------------------------------------------------- | ------------------------- |
| **Tier 1** | Immediate | CRITICAL items: jurisdictional defects, complete waiver, structural errors            | Before filing / Emergency |
| **Tier 2** | Near-term | HIGH items: preservation gaps, standard of review errors, weak harmless error showing | Within briefing cycle     |
| **Tier 3** | If Time   | MEDIUM items: record citation gaps, argument ordering, remedy alignment               | If resources permit       |

---

## Citation Quality Gates

Before delivery, run these gates on every legal proposition:

| Gate           | Rule                                                                  | Fail Action                   |
| -------------- | --------------------------------------------------------------------- | ----------------------------- |
| **Source**     | Every preservation, standard, or harmless error claim cites authority | Add source or mark `[VERIFY]` |
| **Format**     | Citations in jurisdiction-appropriate format                          | Normalize citation            |
| **Currency**   | Check for overruling or superseding authority                         | Add `[CHECK CURRENCY]`        |
| **Domain**     | Analysis stays within selected jurisdiction                           | Remove jurisdiction bleed     |
| **Confidence** | Align certainty with evidentiary/legal support                        | Add confidence qualifier      |

---

## Self-Interrogation (For CRITICAL Findings)

Apply three-pass challenge before finalizing any jurisdictional or preservation finding:

**Pass 1 — Legal Chain Integrity**

- Does the finding follow logically from the applicable rule?
- Would the court actually reach this conclusion on this record?
- Is there a procedural mechanism to cure the defect?

**Pass 2 — Completeness Test**

- Are there exceptions to the doctrine that might apply (e.g., futility exception to
  waiver, implicit ruling exception)?
- What contrary authority would change this conclusion?

**Pass 3 — Adversarial Challenge**

- What is the strongest argument against this finding?
- Under what circumstances would the opposite conclusion be correct?

If any pass reveals weakness, revise before delivery.

---

## Confidence Scoring

| Level        | Range     | Interpretation                                   | Action                        |
| ------------ | --------- | ------------------------------------------------ | ----------------------------- |
| **Definite** | 0.95-1.00 | Clear rule, unambiguous record                   | Report with confidence        |
| **High**     | 0.80-0.94 | Strong support, minor uncertainties              | Report with brief caveat      |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | Present both sides            |
| **Possible** | 0.40-0.59 | Material uncertainty                             | Flag for senior review        |
| **Unlikely** | 0.00-0.39 | Weak support, speculative                        | Do not rely; note uncertainty |

---

## Glass Box Audit Trail

Every appellate brief analysis MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-appellate-brief-analysis"
  mode: "Created from scratch"
  topic: "appellate brief analysis"
  jurisdiction: "[selected jurisdiction]"
  court: "[specific appellate court]"
  side_analyzed: "[appellant/appellee/both]"
  brief_type: "[opening/response/reply/petition]"
  appeal_posture: "[from final judgment/interlocutory/collateral order/etc.]"
  issues_analyzed:
    - issue: "[issue 1]"
      preservation: "[preserved/unpreserved/plain error]"
      standard: "[de novo/clear error/abuse of discretion/etc.]"
    - issue: "[issue 2]"
      preservation: "[status]"
      standard: "[standard]"
  materials_reviewed:
    - "[opening brief]"
    - "[lower court opinion]"
    - "[appendix excerpts]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path or 'Not created']"
  source_skills_analyzed: "legalcode reference standard + legalcode-brief-analyzer"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  key_assumptions:
    - "[assumption 1]"
    - "[assumption 2]"
  limitations:
    - "[limitation 1]"
  confidence: "HIGH | MEDIUM | LOW — [rationale]"
  reviewer: "AI-assisted — requires qualified appellate counsel review"
```

---

## Anti-Patterns

Avoid these failure modes in appellate brief analysis:

### Preservation Analysis Anti-Patterns

1. **Treating all objections as preserving** — A general objection ("I object") often
   does not preserve the specific issue. Verify the objection was specific enough to
   alert the trial court to the claimed error.

2. **Ignoring the "same theory" requirement** — An issue raised on one legal theory
   below cannot be argued on a different theory on appeal. Check that the appellate
   argument matches what was raised.

3. **Assuming plain error is automatic** — Plain error review is not a guaranteed
   fallback. Prong 4 (integrity) is rarely satisfied. Do not treat unpreserved issues
   as merely requiring "plain error" without assessing all four prongs.

4. **Missing futility and other exceptions** — Some jurisdictions recognize exceptions
   to waiver: futility, implicit ruling, change in law, structural error. Check for
   applicable exceptions.

5. **Conflating waiver and forfeiture** — Waiver (intentional) precludes all review;
   forfeiture (inadvertent) permits plain error review. The distinction matters.

### Standard of Review Anti-Patterns

6. **Accepting the brief's stated standard uncritically** — Briefs frequently misstate
   the standard of review to make their case seem stronger. Independently verify.

7. **Ignoring mixed questions** — Many appellate issues are "mixed" (law and fact).
   The standard depends on which character dominates. Do not assume de novo.

8. **Applying wrong jurisdiction's terminology** — "Abuse of discretion" means different
   things in different systems. Verify the test matches the jurisdiction.

### Harmless Error Anti-Patterns

9. **Ignoring harmless error as independent ground** — Even if error is established,
   the appeal fails if the error was harmless. Always assess harmless error exposure.

10. **Misidentifying error type** — Constitutional errors have different harmless error
    standards than non-constitutional errors. Structural errors are per se reversible.
    Classification matters.

11. **Treating prejudice as automatic** — Appellants often assert prejudice conclusorily.
    Verify that the prejudice showing is actually developed with record support.

### Jurisdictional Anti-Patterns

12. **Skipping jurisdictional analysis** — Jurisdictional defects are threshold and
    dispositive. Always check finality, timeliness, and proper appellate basis first.

13. **Assuming interlocutory orders are appealable** — Most interlocutory orders are
    not immediately appealable. Verify certification or collateral order doctrine applies.

14. **Ignoring mootness developments** — Cases can become moot after the notice of
    appeal. Settlement, statutory change, or changed circumstances may moot the appeal.

### Output Anti-Patterns

15. **Vague preservation findings** — "Issue may not be preserved" is not actionable.
    Identify the specific preservation failure and the specific consequence.

16. **Not connecting findings to remedy** — Each finding should connect to what it
    means for the appeal outcome. Will it result in waiver? Affirmance? Remand?

17. **Ignoring strategic implications** — Appellate analysis should inform oral argument
    preparation. Identify hot spots the panel is likely to probe.

18. **Single-pass analysis** — Appellate briefs are complex. Read all materials
    completely before analyzing. Cross-references between preservation moments, argument
    sections, and record citations matter.

---

## Writing Standards

Apply plain-language discipline to all output:

**For internal analysis:**

- Plain language, no jargon without definition
- Active voice: "The appellant failed to preserve" not "Preservation was not achieved"
- Short sentences, one point per sentence
- Tables for structured assessments
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can an appellate partner quickly identify jurisdictional and preservation issues?
2. Are standard of review determinations supported by authority?
3. Is harmless error vulnerability assessed for each alleged error?
4. Are recommendations actionable and prioritized?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Verify current appellate procedure rules (FRAP, CPR Part 52, etc.)
- Check that cited cases have not been overruled
- Research circuit-specific preservation and harmless error standards
- Mark all legalcode-mcp-sourced citations as `VERIFIED`

**Without legalcode-mcp:**

- Mark all case law and rule references with `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Include prominent notice that citations require independent verification
- Focus on structural analysis using the procedural rules as stated in this skill

---

## Output Format Template

````markdown
# Appellate Brief Analysis — [Case Name/Caption]

## 1. Executive Summary

**Appeal**: [Appellant name] appeals from [judgment type] in [lower court]
**Court**: [Appellate court]
**Your side**: [Appellant/Appellee]
**Appeal posture**: [From final judgment / Interlocutory / Collateral order / etc.]
**Analysis date**: [Date]

**Bottom line**: [1-2 sentence assessment of appeal viability or opposing brief
vulnerability]

**Overall confidence**: [0.00-1.00 + label]

---

## 2. Jurisdictional Sufficiency

| Requirement                                 | Status                      | Notes     |
| ------------------------------------------- | --------------------------- | --------- |
| Notice of appeal timely                     | Y/N/Unknown                 | [details] |
| Final judgment / Proper basis               | Y/N/Unknown                 | [details] |
| Justiciability (mootness/ripeness/standing) | No issues / Potential issue | [details] |

**Jurisdictional assessment**: [CLEAR / POTENTIAL ISSUE / DEFICIENT]

---

## 3. Issue Inventory

| Issue # | Issue   | Standard of Review | Preservation                          | Viability    |
| ------- | ------- | ------------------ | ------------------------------------- | ------------ |
| 1       | [issue] | [standard]         | Preserved / Unpreserved / Plain Error | HIGH/MED/LOW |
| 2       | [issue] | [standard]         | [status]                              | [viability]  |

---

## 4. Preservation Analysis

### Fully Preserved Issues

| Issue   | Preservation Moment       | Record Cite | Notes   |
| ------- | ------------------------- | ----------- | ------- |
| [issue] | [objection/motion/ruling] | [cite]      | [notes] |

### Preservation Concerns

| Issue   | Problem            | Plain Error Available? | Prong Assessment               |
| ------- | ------------------ | ---------------------- | ------------------------------ |
| [issue] | [specific problem] | Y/N                    | [prong-by-prong if applicable] |

---

## 5. Standard of Review Alignment

| Issue   | Brief's Standard | Correct Standard | Alignment                   |
| ------- | ---------------- | ---------------- | --------------------------- |
| [issue] | [stated]         | [correct]        | CORRECT / INCORRECT / MIXED |

**Standard of review assessment**: [ALIGNED / MISALIGNED — details]

---

## 6. Harmless Error Vulnerability

| Error   | Type            | Standard   | Prejudice Showing | Harmlessness Defense | Assessment                          |
| ------- | --------------- | ---------- | ----------------- | -------------------- | ----------------------------------- |
| [error] | Const/Non-const | [standard] | Strong/Weak       | Strong/Weak          | Likely reversible / Likely harmless |

---

## 7. Record Appendix Compliance

| Element                 | Present | Notes |
| ----------------------- | ------- | ----- |
| Judgment appealed       | Y/N     |       |
| Lower court opinion     | Y/N     |       |
| Key transcript excerpts | Y/N     |       |
| Preservation moments    | Y/N     |       |

**Record audit (sample citations)**: [Accurate / Issues found — details]

---

## 8. Outcome Prediction

| Outcome          | Probability | Rationale                  |
| ---------------- | ----------- | -------------------------- |
| Full reversal    | [X]%        | [reasons]                  |
| Partial reversal | [X]%        | [on which issues]          |
| Affirmance       | [X]%        | [reasons]                  |
| Dismissal        | [X]%        | [if jurisdictional issues] |

**Key drivers**: [What factors most influence outcome]

---

## 9. Strategic Recommendations

### For Appellant/Petitioner

| Priority | Recommendation | Expected Impact |
| -------- | -------------- | --------------- |
| Tier 1   | [action]       | [impact]        |
| Tier 2   | [action]       | [impact]        |

### For Appellee/Respondent

| Priority | Recommendation | Expected Impact |
| -------- | -------------- | --------------- |
| Tier 1   | [action]       | [impact]        |
| Tier 2   | [action]       | [impact]        |

### Oral Argument Hot Spots

| Issue   | Likely Questions        | Preparation Notes |
| ------- | ----------------------- | ----------------- |
| [issue] | [anticipated questions] | [how to prepare]  |

---

## 10. Detailed Findings

### Tier 1 — Immediate (CRITICAL)

[Detailed findings using the finding template]

### Tier 2 — Near-Term (HIGH)

[Detailed findings]

### Tier 3 — If Time (MEDIUM)

[Detailed findings]

---

## 11. Quality Assurance

**Citation Quality Gates**: [All passed / Issues identified]
**Self-Interrogation**: [Performed for CRITICAL items]
**Confidence calibration**: [Assessment]

---

## 12. Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-appellate-brief-analysis"
  [... full audit trail ...]
```
````

```

---

## Common Appellate Weaknesses by Brief Type

### Opening Brief (Appellant)

| Weakness | Detection Pattern | Frequency |
|----------|------------------|-----------|
| Unpreserved issue raised without plain error argument | No objection/motion cited; no plain error analysis | Very common |
| Wrong standard of review | De novo for facts, clear error for law | Common |
| Weak prejudice showing | Conclusory "harmful" without analysis | Very common |
| Missing preservation record cites | Asserts "objected" without transcript cite | Common |
| Kitchen sink issues | 5+ issues diluting strongest argument | Occasional |
| Remedy overreach | Requests judgment entry when remand appropriate | Common |
| No theory of the case | Disconnected legal points | Common |

### Response/Answering Brief (Appellee)

| Weakness | Detection Pattern | Frequency |
|----------|------------------|-----------|
| Fails to argue waiver | Unpreserved issues not identified | Common |
| No harmless error argument | Error conceded without harmless analysis | Very common |
| Fails to leverage deference | Does not emphasize deferential standard | Common |
| No alternative affirmance grounds | Single theory only | Common |
| Adopts appellant's issue framing | Uses opponent's formulations | Common |
| No independent statement of facts | Relies on appellant's facts | Common |

### Reply Brief

| Weakness | Detection Pattern | Frequency |
|----------|------------------|-----------|
| Raises new issues | Arguments not responsive to response brief | Occasional — CRITICAL |
| Ignores appellee's waiver arguments | No response to preservation attack | Common |
| Ignores harmless error arguments | No response to harmlessness claim | Common |
| Mere repetition | Restates opening without addressing response | Common |

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified procedural rules and case law
3. Add court-specific procedural requirements (local rules, filing deadlines, panel practices)
4. Add circuit/court-specific preservation and harmless error standards
5. Include leading cases from the jurisdiction on each appellate doctrine
6. Update the frontmatter name and description

**Potential variants:**
- `legalcode-appellate-brief-analysis-9th-cir` — Ninth Circuit specific
- `legalcode-appellate-brief-analysis-ew` — England & Wales CPR Part 52 focus
- `legalcode-appellate-brief-analysis-scotus` — Supreme Court certiorari focus

---

## Provenance

Legalcode original skill created on 2026-03-02. Research-backed creation using:
- Reference standard: `legalcode-contract-review` quality framework
- Related skills analyzed: `legalcode-brief-analyzer`, `legalcode-summary-judgment-analysis`
- Research sources:
  - FRAP Rules 3, 4, 28, 30 (current through December 2025 amendments)
  - CPR Part 52, PD 52A (England & Wales, as amended October 2023)
  - Federal Court of Australia Rules
  - Bowles v. Russell, 551 U.S. 205 (2007) — jurisdictional timing
  - Chapman v. California, 386 U.S. 18 (1967) — constitutional harmless error
  - Puckett v. United States, 556 U.S. 129 (2009) — plain error four prongs
  - Celotex/Anderson trilogy for summary judgment standard of review
  - Thomson Reuters Appellate Practice guides
  - Practice tips from federal appellate practitioners
```
