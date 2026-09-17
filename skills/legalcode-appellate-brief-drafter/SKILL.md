---
name: legalcode-appellate-brief-drafter
description: Draft appellate briefs for US federal circuit courts (FRAP), US state appellate courts, and
  UK Court of Appeal proceedings. Use when drafting an opening brief, appellant's brief, appellee's response
  brief, reply brief, or cross-appeal brief; when structuring grounds of appeal and standard-of-review
  arguments; when preparing a record appendix or joint appendix; when writing UK skeleton arguments and
  assembling appeal bundles; or when checking compliance with FRAP Rule 28/32, circuit-specific local
  rules, or CPR Part 52.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft appellate briefs for US federal circuit courts (FRAP), US state appellate courts, and UK Court of Appeal proceedings. Use when drafting an opening brief, appellant's brief, appellee's response brief, reply brief, or cross-appeal brief; when structuring grounds of appeal and standard-of-review arguments; when preparing a record appendix or joint appendix; when writing UK skeleton arguments and assembling appeal bundles; or when checking compliance with FRAP Rule 28/32, circuit-specific local rules, or CPR Part 52. Also triggers on "appellate brief," "opening brief," "brief on appeal," "standard of review," "grounds of appeal," "record on appeal," "appellant," "appellee," "skeleton argument," "notice of appeal," "jurisdictional statement," "table of authorities," or "circuit court brief." Covers FRAP Rules 28, 30, and 32; all twelve federal circuits plus the Federal Circuit; California Court of Appeal, New York Appellate Division, Texas courts of appeals, Florida DCA; and UK CPR Part 52, Practice Directions 52A–52E, and UKSC Rules.


# Legalcode Appellate Brief Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted appellate brief
> drafting. It does not constitute legal advice. All outputs must be reviewed, verified,
> and signed by qualified legal counsel licensed in the relevant jurisdiction before
> filing with any court. Procedural rules, word limits, and local rules change
> frequently — verify current applicability before relying on any provision described
> here. AI-generated briefs may contain errors in legal analysis, factual
> characterization, standard-of-review selection, or citation accuracy. All arguments
> must be verified against actual evidence and current case law. Any cited authority
> marked `[VERIFY]` has not been independently validated and must be confirmed before
> reliance. Filing a brief constitutes counsel's professional certification that it is
> well-grounded in fact and law and is not interposed for improper purpose.

---

## Purpose and Scope

This skill drafts appellate briefs by structuring the argument theory, selecting the
correct standard of review, organizing record citations, applying FRAP and circuit-specific
formatting rules, and producing court-ready output. The skill covers both US federal
and UK appellate proceedings.

**Covers:**

- **Opening / Appellant's brief**: Full FRAP Rule 28(a) structure with all mandatory
  sections, standard-of-review arguments, record-based argument development, and appendix
  designation
- **Appellee's / Response brief**: Counter-argument structure, cross-appeal framing,
  alternative holding arguments, and harmless-error responses
- **Reply brief**: Narrowed rebuttal structure, avoidance of new arguments, concession
  mapping
- **US Federal**: FRAP Rules 28, 30, and 32; all twelve numbered circuits plus the
  Federal Circuit and DC Circuit; local rule compliance
- **US State**: California Court of Appeal, New York Appellate Division (1st–4th Depts.),
  Texas Courts of Appeals, Florida District Courts of Appeal, with framework for other
  state appellate courts
- **UK Court of Appeal**: CPR Part 52, Practice Directions 52A–52E, skeleton arguments,
  core bundle assembly, permission-to-appeal applications
- **UK Supreme Court**: UKSC Rules 2009, Form 1 applications, Form 3 statements of
  facts and issues
- **Standard of review analysis**: De novo, abuse of discretion, clearly erroneous,
  substantial evidence, plain error, and hybrid standards — selection and argumentation
- **Record preparation**: Joint appendix, excerpts of record, deferred appendix,
  designation of record, UK core bundle / supplemental bundle
- **Preservation analysis**: Issue preservation, waiver, forfeiture, and plain-error
  rescue strategies

**Does not:**

- Replace counsel's strategic judgment about which issues to raise or abandon
- Certify appellate jurisdiction (counsel must verify timely notice of appeal)
- Independently verify the factual record (counsel must review all cited documents)
- Provide legal advice or substitute for qualified appellate counsel
- File documents with any court

**Related skills:**

- `legalcode-brief-analyzer` — Evaluate brief argument strength and citation quality
- `legalcode-opposition-brief-drafter` — Draft responsive briefs at trial court level
- `legalcode-complaint-drafter` — Trial-level pleading drafting
- `legalcode-legal-memorandum` — Office memoranda analyzing appeal prospects
- `legalcode-litigation-risk-assessment` — Pre-appeal risk/cost analysis
- `legalcode-early-case-assessment` — Issue preservation and appellate posture audit

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware with primary coverage for US federal and UK appellate
procedure. Identify the appellate forum at the outset and apply the corresponding rules.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Brief format and mandatory sections
- Word / page limits and certificate of compliance requirements
- Filing deadlines and extension procedures
- Record / appendix assembly rules
- Citation format (Bluebook for US federal; OSCOLA for UK; regional or state-specific
  formats for state courts)
- Authority hierarchy and binding vs. persuasive precedent scope
- Permission-to-appeal requirements (UK and some US state courts)
- En banc / full court procedures
- Costs regime (UK: costs follow the event; US: generally each side bears own costs)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The forum or procedural posture is ambiguous
- Multiple valid argument theories exist
- Standard-of-review selection would materially change argument strategy
- Preservation status is uncertain and affects issue selection
- Reply-brief scope rules may limit what can be raised

Use the **⟁ CLARIFY** pattern throughout. Present structured options with brief
explanations of why the answer matters. Skip any clarification already answered.

---

## Workflow

### Step 1: Accept Input Materials

Accept materials in any of these formats:

- **File path(s)**: Read documents directly (PDF, DOCX, TXT, MD)
- **Pasted text**: Accept inline text for the lower-court opinion, trial briefs, or
  key record excerpts
- **URL**: Fetch from PACER/ECF, court website, or document management system

If PDFs, convert:

```bash
pandoc "$FILE" -t markdown -o "${FILE%.pdf}.md" 2>/dev/null \
  || pdftotext "$FILE" "${FILE%.pdf}.txt"
```

Identify and categorize each document provided:

- Lower-court decision / opinion being appealed
- Prior briefs (trial-level or prior appellate)
- Record excerpts / appendix materials
- Notice of appeal
- Any scheduling or briefing orders

### Step 2: Gather Context via Interactive Clarification

**⟁ CLARIFY block 1 — Brief type**

- Options: `opening / appellant's brief`, `appellee's response brief`,
  `reply brief (appellant)`, `cross-appeal opening`, `cross-appeal response`,
  `amicus curiae brief`, `UK skeleton argument — permission stage`,
  `UK skeleton argument — full appeal`
- Default: `opening / appellant's brief`
- _Why_: Different brief types have different mandatory sections, word limits,
  and strategic constraints.

**⟁ CLARIFY block 2 — Appellate forum**

- Options: `US federal circuit court (specify which)`, `US Supreme Court`,
  `US state appellate court (specify state/court)`, `UK Court of Appeal (Civil Division)`,
  `UK Court of Appeal (Criminal Division)`, `UK Supreme Court`, `other (specify)`
- Default: `US federal circuit court — 9th Circuit`
- _Why_: Determines applicable procedural rules, word limits, format requirements,
  and citation conventions.

**⟁ CLARIFY block 3 — Your client's role**

- Options: `appellant (lost below, bringing appeal)`, `appellee (won below, defending)`,
  `cross-appellant (also appealing part of the judgment)`,
  `cross-appellee (defending cross-appeal)`, `amicus curiae`
- Default: `appellant (lost below, bringing appeal)`
- _Why_: Determines brief structure, argument framing, and standard-of-review posture.

**⟁ CLARIFY block 4 — Nature of lower-court ruling**

- Options: `final judgment after bench trial`, `final judgment after jury trial`,
  `summary judgment granted`, `motion to dismiss granted`, `preliminary injunction order`,
  `class certification order`, `administrative agency final order`,
  `interlocutory order (specify basis for appellate jurisdiction)`,
  `UK — first-instance judgment`, `UK — first appeal (seeking second appeal)`
- Default: `summary judgment granted`
- _Why_: Determines available standards of review and whether factual findings are
  entitled to deference.

**⟁ CLARIFY block 5 — Issues on appeal**

- Prompt: "Which issues do you intend to raise on appeal? List each issue, and for
  each, indicate whether it was raised and preserved in the lower court."
- Default: I will identify from the lower-court opinion.
- _Why_: Issue selection and preservation status are the most important strategic
  decisions in any appeal. Unpreserved issues require plain-error analysis.

**⟁ CLARIFY block 6 — Available materials**

- Options: `lower-court opinion only`, `opinion + key briefs`,
  `opinion + trial record + briefs`, `opinion + full record`,
  `full record including trial transcripts`, `UK — judgment + trial bundle`
- Default: `opinion + key briefs`
- _Why_: More record access improves argument development and record citations.

**⟁ CLARIFY block 7 — Playbook / style guide**

- Options: `firm style guide (attach or describe)`,
  `court-specific preferences (specify)`,
  `no specific guide — use Legalcode defaults`
- Default: `no specific guide — use Legalcode defaults`
- _Why_: Some firms or judges have strong preferences on brief structure and style.

### Step 3: Analyze the Lower-Court Decision

Systematically read the lower-court opinion to map the decision for appeal:

**3a. Decision inventory:**

| Issue   | Lower Court's Ruling | Rationale   | Reviewability               | Preservation Status       |
| ------- | -------------------- | ----------- | --------------------------- | ------------------------- |
| [issue] | [ruling]             | [reasoning] | [de novo / AoD / CE / etc.] | [preserved / unpreserved] |

**3b. Error identification:**

For each ruling, identify the theory of error:

- **Legal error**: Court misapplied a statute, misread case law, or used wrong legal standard → reviewable de novo
- **Factual error**: Court's fact-finding was clearly erroneous or against the manifest weight of evidence → clearly-erroneous or substantial-evidence standard
- **Discretionary error**: Court's exercise of discretion was unreasonable, arbitrary, or based on wrong legal standard → abuse of discretion
- **Constitutional error**: Structural constitutional error or violation of fundamental rights → typically de novo
- **Procedural error**: Violation of procedural rules causing prejudice → abuse of discretion or harmless-error analysis

**3c. Preservation map:**

For each error theory, determine:

1. Was the issue raised in the lower court at all?
2. Was it raised at the right time (before the ruling, not after)?
3. Was it preserved with specificity (vague objections may be insufficient)?
4. Was it renewed after an unfavorable ruling if required?

**⟁ CLARIFY** — For issues with uncertain preservation status, present the question
to the user:

- "Issue [X] appears unpreserved — I found no objection in the record. Do you want me
  to (a) analyze whether plain-error review applies and build a plain-error argument,
  (b) flag it for counsel's review only, or (c) omit it from the brief?"

### Step 4: Select the Standard of Review

Standard-of-review selection is the single most important analytical decision in any
appeal. For each issue on appeal, apply the selection framework below.

#### Standard of Review Framework

| Standard                   | Applies To                                                                                                                                                                       | Deference                                                                     | Strategic Implication                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **De Novo**                | Questions of law; statutory construction; constitutional issues; grant of Rule 12(b)(6) motion; grant of summary judgment on legal grounds; jury instructions as a matter of law | No deference — court reviews as if seeing the issue fresh                     | Most favorable to appellant; argue the law is wrong                                            |
| **Abuse of Discretion**    | Most procedural rulings; evidentiary decisions under FRE; discovery orders; class certification; preliminary injunctions; case management; fee awards; many equitable rulings    | Substantial deference — overturned only if "no reasonable jurist" could agree | Hardest to win; must show unreasonableness, not mere disagreement                              |
| **Clearly Erroneous**      | Factual findings after bench trial (FRCP 52(a)); credibility determinations; mixed law-fact findings (factual component)                                                         | Heavy deference — even if appellate court would have found differently        | Very hard to win; must show definite conviction that lower court erred                         |
| **Substantial Evidence**   | Administrative agency fact-findings; jury verdicts (sufficiency); NLRB and agency adjudications                                                                                  | Deferential — upheld if any rational factfinder could have found that way     | Hardest appellate standard; argue no rational basis                                            |
| **Plain Error**            | Unpreserved errors not objected to below                                                                                                                                         | Very demanding — four prongs must all be satisfied                            | Rarely won; use only when issue is important and error is egregious                            |
| **Harmless Error**         | Preserved errors subject to harmless-error review                                                                                                                                | Upheld if error did not affect substantial rights                             | Government bears burden on constitutional errors; appellant on others [VERIFY by jurisdiction] |
| **De Novo + Fact-Finding** | Summary judgment (whether genuine dispute exists)                                                                                                                                | De novo on whether a dispute exists; facts viewed in non-movant's favor       | Frame as pure legal issue; emphasize favorable facts                                           |

[JURISDICTION-SPECIFIC] **UK Appellate Review Standards:**

- **Error of law**: Reviewed without deference (analogous to de novo) [VERIFY]
- **Wrong exercise of discretion**: Overturned only if plainly wrong; factors wrongly taken into account; or irrelevant factors considered [VERIFY]
- **Perverse / irrational finding**: Very high bar — decision must be so clearly wrong no reasonable judge could have reached it [VERIFY]
- **Permission threshold**: Must show real prospect of success or other compelling reason [VERIFY CPR 52.6]

#### Plain Error Analysis (US Federal — Unpreserved Issues)

Before including any unpreserved issue, verify all four prongs [VERIFY]:

1. **Error**: Was there in fact a legal or constitutional error?
2. **Plain**: Was the error "clear and obvious" under current law (not just arguable)?
3. **Substantial rights**: Did the error affect the outcome of the proceeding?
4. **Fundamental fairness / integrity**: Would leaving the error uncorrected seriously affect the fairness, integrity, or public reputation of judicial proceedings?

Plain error rarely succeeds and should generally be reserved for structural constitutional
errors or egregious legal mistakes with clear, obvious authority.

### Step 5: Build the Legal Authority File

While developing arguments, build a working authority file for the brief:

**5a. Use legalcode-mcp (if connected):**

Search for:

- Controlling circuit or jurisdiction precedent on each issue on appeal
- Negative treatment of lower court's cited authority
- Recent circuit-level developments in the relevant area of law
- Statutory text and legislative history for statutory-construction arguments
- UK — binding Court of Appeal and Supreme Court authority; relevant Practice Directions

Save results to `/tmp/legalcode-appellate-authority.md`:

```markdown
# Appellate Authority Reference — [Case Name]

## Forum: [Circuit / UK CA / etc.]

## Date: [date]

### Controlling Authority (Issue 1: [Name])

- [Case, citation, key holding, how it supports argument]

### Authority Distinguishing Lower Court's Reasoning

- [Case, citation, distinction, why favorable]

### Standard of Review Authority

- [Case, citation, standard articulated]

### Adverse Authority to Distinguish

- [Case, citation, factual/legal distinction]
```

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using provided materials and general legal knowledge

**5b. Check circuit-specific local rules:**

```bash
# Check for local rule references in provided documents
grep -i "local rule\|L\.R\.\|local civ\|local app" "$RECORD_FILE"
```

Key circuit-specific rules to verify [VERIFY all current rules]:

| Circuit   | Notable Local Rules                                                                         |
| --------- | ------------------------------------------------------------------------------------------- |
| 1st       | 1st Cir. R. 32.0 (word limits); L.R. 28.0 (citations)                                       |
| 2nd       | 2d Cir. R. 32.1 (short appendix for pro se); Case Management Orders                         |
| 3rd       | 3d Cir. L.A.R. 28 (statement of related cases); LAR 31 (filing deadlines)                   |
| 4th       | 4th Cir. R. 28(a) (facts must cite JA); R. 34(a) (oral argument default)                    |
| 5th       | 5th Cir. R. 28.2 (citation requirements); IOP 28.2.1 (record citations: ROA.\_\_\_)         |
| 6th       | 6th Cir. R. 28(a) (record cites); 32(a) (certificate of compliance)                         |
| 7th       | 7th Cir. R. 28 (required sections); Circuit Rule 32 (record cites: R.\_\_\_)                |
| 8th       | 8th Cir. R. 28A (certificate of compliance); appendix as separate volume                    |
| 9th       | 9th Cir. R. 28-2 (brief contents); R. 32-1 (word limits may differ for cross-appeals)       |
| 10th      | 10th Cir. R. 28.2 (additional brief requirements); R. 32.1 (reproduction of statutes)       |
| 11th      | 11th Cir. R. 28-1 (required sections); R. 31-1 (filing deadlines)                           |
| DC Cir.   | DC Cir. R. 28 (disclosure statement rules); most important authorities marked with asterisk |
| Fed. Cir. | Fed. Cir. R. 28 (confidential materials); specialized rules for patent appeals              |

### Step 6: Select Issues and Build Argument Theory

**6a. Issue selection framework:**

| Issue   | Standard of Review | Preserved? | Strength         | Word Allocation |
| ------- | ------------------ | ---------- | ---------------- | --------------- |
| [issue] | [standard]         | Y / N      | HIGH / MED / LOW | [words]         |

Issue selection principles:

- **Lead with your best issue** — courts read introductions and issue statements carefully
- **Do not "kitchen-sink"** — more than 4-5 issues dilutes impact and signals weakness
- **Abandon weak issues** — a weak issue invites skepticism about the strong ones
- **Always include the strongest preserved issue** — if you must choose, preserve your best
- **De novo issues are easier to win** — lead with legal errors, not factual ones
- **Do not abandon issues for appeal** — but do triage for word budget

**⟁ CLARIFY** — If there are more than 5 candidate issues:

- "I've identified [N] potential issues. I recommend focusing on [top 3-4] because
  [brief reason for each]. Should I (a) proceed with the recommended issues only,
  (b) include all [N] issues, or (c) include the recommended issues plus preserve
  specific others for error?"

**6b. Argument theory:**

For each selected issue, develop the argument theory:

1. **What error did the lower court make?** (specific legal or factual error)
2. **What is the correct legal standard?** (with authority)
3. **How does the correct standard apply to the facts?** (with record citations)
4. **What is the relief requested?** (reversal, remand for new trial, remand with
   instructions, modification)
5. **What is the appellee's most likely response?** (anticipate and address)

### Step 7: Draft the Appellate Brief

Produce court-ready output following the applicable format. Apply the template in the
Output Format section at the end of this skill.

#### 7a. US Federal Appellate Brief Structure (FRAP Rule 28)

**Required sections for appellant's brief (Rule 28(a)):**

| Section                       | Rule     | Purpose                                                                      | Drafting Notes                                                                                                                                                           |
| ----------------------------- | -------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Disclosure Statement**      | 26.1     | Identify corporate parents / 10% shareholders                                | Required for non-governmental entities; often omitted by individual parties                                                                                              |
| **Table of Contents**         | 28(a)(2) | List all sections and subheadings with page numbers                          | Generate last; must match headings exactly                                                                                                                               |
| **Table of Authorities**      | 28(a)(3) | List all cases, statutes, rules with page numbers                            | Cases alphabetically; statutes/rules by title; mark most-cited [DC Cir. only: asterisk]                                                                                  |
| **Jurisdictional Statement**  | 28(a)(4) | Establish subject matter + appellate jurisdiction                            | Four components: district court SMJ basis + statute; appellate jurisdiction basis + statute; filing dates establishing timeliness; assertion of finality                 |
| **Statement of Issues**       | 28(a)(5) | Frame each question presented                                                | Argumentative framing preferred; one sentence per issue; order from most to least favorable standard                                                                     |
| **Statement of the Case**     | 28(a)(6) | Facts + procedural history                                                   | Two sub-parts: (i) nature of the case, course of proceedings, and disposition below; (ii) statement of facts with record citations — every material fact must cite JA/ER |
| **Summary of Argument**       | 28(a)(7) | Preview arguments — "must contain a succinct, clear, and accurate statement" | Do not merely repeat headings; synthesize; 1-3 pages; court often reads this first                                                                                       |
| **Argument**                  | 28(a)(8) | Main body with point headings and citations                                  | IRAC/CRAC structure; standard of review stated at start of each issue; every legal proposition cites authority; every factual assertion cites record                     |
| **Conclusion**                | 28(a)(9) | State precise relief sought                                                  | One paragraph; very specific — "reverse and remand with instructions to enter judgment for appellant," not "reverse"                                                     |
| **Certificate of Compliance** | 32(g)    | Certify word count / type volume                                             | Required if brief uses word/line-count limits; state method used                                                                                                         |

**Appellee's brief (Rule 28(b)):**

- Same structure except: may omit sections already adequately covered in appellant's
  brief (disclosure, jurisdictional statement, statement of issues, statement of case)
  — but only if adopting appellant's presentation
- Must include counter-statement of facts if appellant's facts are disputed or incomplete
- Address appellee's own affirmative grounds for affirmance (alternative holdings,
  harmless error, waiver)

**Reply brief (Rule 28(c)):**

- May only respond to arguments in appellee's brief — no new arguments
- Omit sections covered in appellant's opening brief
- Shorter word limit: 6,500 words (or 15 pages if elected)
- Focus on: (i) correcting mischaracterizations; (ii) addressing new arguments or
  authority in appellee's brief; (iii) conceding unwinnable points to focus the court

#### 7b. FRAP Word and Page Limits (Rule 32)

Current limits (effective December 1, 2016; check local rules for circuit modifications) [VERIFY current rules]:

| Brief Type                                                                 | Word Limit   | Alternative Page Limit | Line Limit  |
| -------------------------------------------------------------------------- | ------------ | ---------------------- | ----------- |
| Principal brief (opening / response)                                       | 13,000 words | 30 pages               | 1,300 lines |
| Reply brief                                                                | 6,500 words  | 15 pages               | 650 lines   |
| Amicus brief                                                               | 6,500 words  | 15 pages               | 650 lines   |
| Cross-appeal principal brief (appellant's response + cross-appeal opening) | 15,300 words | 35 pages               | 1,530 lines |
| Cross-appeal response + reply (appellee's cross-reply + appellant's reply) | 13,000 words | 30 pages               | 1,300 lines |

**Type requirements (Rule 32(a)(5)–(6)):**

- Proportionally spaced: 14-point font minimum
- Monospaced: no more than 10.5 characters per inch
- Line spacing: double-spaced body; single-spaced headings, footnotes, quotations
- Margins: at least 1 inch on all four sides

**Certificate of compliance (Rule 32(g)):**
State the number of words using the word-processor's word-count feature (excluding
cover, disclosure statement, TOC, TOA, statement of related cases, signature block,
certificate of service, and certificate of compliance itself).

**⟁ CLARIFY** — If the draft brief exceeds word limits:

- "The draft is [X] words over the [13,000 / 6,500] word limit. I recommend trimming
  by: (a) condensing argument sections [list which], (b) shortening the statement of
  facts, or (c) combining issues that share the same standard of review. Which approach
  do you prefer?"

#### 7c. Record Citations

All factual assertions in the brief must cite to the record. Different circuits use
different record citation formats [VERIFY per circuit]:

| Forum                | Record Citation Format                                        | Example             |
| -------------------- | ------------------------------------------------------------- | ------------------- |
| US Federal (general) | Joint Appendix page: `J.A. ___`                               | `J.A. 42`           |
| 5th Circuit          | Record on Appeal: `ROA.___`                                   | `ROA.1523`          |
| 7th Circuit          | Record: `R. ___, at ___`                                      | `R. 47, at 3`       |
| 9th Circuit          | Excerpts of Record: `ER ___`                                  | `ER 112`            |
| California           | Clerk's Transcript: `CT ___`; Reporter's Transcript: `RT ___` | `CT 45; RT 112:3-8` |
| New York             | Record: `R. ___`; Appendix: `App. ___`                        | `App. A-42`         |
| UK Court of Appeal   | Bundle reference: `[A/42]` or `[Core Bundle/42]`              | `[CB/42]`           |

**Record citation best practices:**

- Cite to the specific page in the record, not just the exhibit or document title
- For transcripts, include page and line number (e.g., `Tr. 112:3-8`)
- For depositions, include deponent name, page, and line
- For declarations/affidavits, cite to the specific paragraph or page
- For exhibits, cite to exhibit number and internal page if paginated

#### 7d. Appendix / Record Assembly (FRAP Rule 30)

The joint appendix contains the portions of the record to which the parties primarily
refer. Parties typically stipulate to contents; if not, appellant designates.

**Mandatory contents (Rule 30(a)(1)):**

- The relevant docket entries
- The relevant portions of any pleadings, findings of fact, jury instructions, charge,
  and any other parts of the record that the parties direct the court to consider
- The judgment, order, or decision in question

**Recommended contents:**

- Notice of appeal
- Lower-court opinion / decision being appealed
- All relevant orders cited in the brief
- Key documentary evidence cited in the brief
- Relevant deposition excerpts (cited portions only)
- Relevant statutory or regulatory text (if not reproduced in the brief)

**Deferred appendix (Rule 30(c)):**

- Permitted unless the court orders otherwise
- Appendix filed within 14 days after appellee's reply brief is due
- Parties cite record documents in the brief; appendix assembled after briefing

**⟁ CLARIFY** — For large records:

- "The record is extensive. Do you want me to (a) identify all documents that should
  be in the appendix based on the citations in the brief, (b) identify only mandatory
  contents plus the most frequently cited documents, or (c) help you negotiate appendix
  contents with opposing counsel?"

#### 7e. UK Court of Appeal — Skeleton Arguments and Bundles (CPR Part 52)

[JURISDICTION-SPECIFIC] UK practice differs fundamentally from US brief practice.

**Permission to appeal (CPR 52.3–52.6):**

- Required for most civil appeals
- Sought first from lower court (at the hearing or within 21 days of decision) [VERIFY]
- If refused, seek from Court of Appeal on paper; if refused on paper, oral renewal
- **Test**: Real prospect of success OR some other compelling reason [VERIFY CPR 52.6]
- Grounds of appeal must identify each specific error of law, fact, or exercise of
  discretion with precision — vague grounds are insufficient

**Skeleton argument requirements (Practice Direction 52A–52E):**

| Element     | Requirement                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------- |
| Length      | Must not exceed 25 pages without permission [VERIFY PD 52A para 5.1]                           |
| Format      | Numbered paragraphs; double-spaced or 1.5-spaced; 12-point minimum                             |
| Contents    | Numbered propositions of law with authority references; chronology if helpful                  |
| Structure   | (1) Introduction; (2) Issues; (3) Submissions on each issue; (4) Conclusion with time estimate |
| Authorities | List separately; bundle only those actually relied upon                                        |
| Filing      | Skeleton filed and served at least 7 days before hearing [VERIFY per court listing notice]     |

**Bundle requirements (Practice Direction 52B para 6):**

| Bundle                  | Contents                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Core bundle**         | The judgment appealed; grounds of appeal; order appealed; relevant court below documents (pleadings, key orders); skeleton arguments |
| **Supplemental bundle** | All other documents to which skeletons refer; trial transcripts; exhibits (in index order)                                           |

**Grounds of appeal (CPR 52.4, PD 52A):**

- Must be set out in numbered paragraphs
- State the specific finding of fact, exercise of discretion, or point of law being challenged
- State the legal basis for the challenge with authority
- May not raise new grounds without permission

**UK Supreme Court (UKSC Rules 2009):**

- Leave (permission) required from UKSC or Court of Appeal [VERIFY UKSC Rule 10]
- Application must raise point of general public importance [VERIFY]
- Form 1: Application for permission to appeal
- Form 3: Statement of facts and issues (agreed if possible; otherwise separate)
- Statement of facts and issues limited to 20 pages [VERIFY UKSC Practice Direction 3]
- Appendix containing relevant legislation, international conventions, domestic rules

### Step 8: Write Point Headings

Point headings are the most-read parts of an appellate brief. Every argument section
must begin with an argumentative heading stating the conclusion.

**Point heading formula:**

> [Standard of review] + [error / correct rule] + [result it compels]

**Examples:**

| Weak (Topic Heading) | Strong (Argumentative Conclusion)                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| "Standard of Review" | "The District Court's Grant of Summary Judgment Is Subject to De Novo Review"                                                                 |
| "The Contract"       | "The Unambiguous Contract Language Required Delivery by March 1, Entitling Appellant to Judgment as a Matter of Law"                          |
| "Hearsay Exception"  | "The Admission of Plaintiff's Medical Records Was Harmless Because Three Other Witnesses Established the Same Diagnoses"                      |
| "Jurisdiction"       | "The District Court Possessed Subject-Matter Jurisdiction Under 28 U.S.C. § 1331 Because Appellant's Claims Arise Under Federal Law"          |
| "The Evidence"       | "No Rational Jury Could Have Found That Defendant Acted in Good Faith Given His Own Contemporaneous Emails Admitting Knowledge of the Defect" |

**Sub-heading principles:**

- Sub-headings should advance the argument, not merely describe it
- Roman numerals (I, II, III) for major argument sections
- Capital letters (A, B, C) for sub-arguments
- Arabic numerals (1, 2, 3) for supporting points if needed
- Every heading appears in the Table of Contents exactly as written in the brief

### Step 9: Draft Key Sections

#### Statement of Issues

The statement of issues is read first by clerks and judges. Frame each issue to favor
your position while remaining accurate.

**US federal format (Rule 28(a)(5)):**

- One sentence per issue (though complex issues may require compound sentences)
- Embed the key facts, standard, and conclusion: "Whether the district court erred
  as a matter of law in [action], given [key fact], where [governing rule]."
- Order issues from most favorable standard of review (de novo) to least favorable
- Limit to issues that are genuinely contested and worth raising

**UK format (Grounds of Appeal):**

- Number each ground
- State the legal basis with specificity: "The judge erred in law in holding that
  [proposition], because [authority/reason]."
- Identify whether the challenge is to a finding of fact, exercise of discretion,
  or question of law

#### Statement of the Case / Facts

**Structure:**

1. **Introductory overview** (1-2 paragraphs): Who are the parties, what is the case
   about, how did it end up on appeal — written to favor appellant
2. **Procedural history**: Complaint filed, key motions, trial, verdict, judgment,
   notice of appeal
3. **Statement of facts**: Narrative form, favorable to appellant, every fact cited
   to record

**Drafting principles for Statement of Facts:**

- Select facts strategically — include only facts that matter to the legal issues
- Tell the story from your client's perspective (accurate but selective)
- Lead with the most compelling facts (injustice narrative if available)
- Use present tense for timeless background facts; past tense for events
- Every material fact must cite to the record — no citation, no fact
- Do not argue in the facts section — save argument for the Argument section
- Include adverse facts that the court will see anyway — ignoring them signals weakness

#### Summary of Argument

The Summary of Argument is often read before the full Argument. It should:

- State the argument as a series of propositions, not mere issue labels
- Convey the "why you should win" story in 1-3 pages
- Reference the applicable standards of review
- Note the most compelling authority
- Be self-contained — a reader who only reads the Summary should understand why you win

#### The Argument

Apply IRAC/CRAC structure for each issue:

1. **Point heading** — argumentative conclusion (see Step 8)
2. **Standard of review** — state early in each section with authority
3. **Rule** — state the governing legal standard with binding authority
4. **Application** — apply rule to the specific facts with record citations
5. **Conclusion** — state what the court should do

**For preserved legal errors (de novo review):**

- Lead with the correct legal rule and authority
- Show how the lower court applied a different (wrong) rule
- Apply the correct rule to show you win under it

**For preserved factual errors (clearly erroneous / substantial evidence):**

- Acknowledge the deference standard — do not pretend it does not exist
- Show that even under deferential review, the error is undeniable
- Focus on objective, documentary evidence rather than credibility findings
- Point to the specific finding and the record that contradicts it

**For unpreserved issues (plain error):**

- Acknowledge the plain-error standard before arguing it
- Address all four prongs separately
- Focus on egregious or structural errors with obvious authority
- Do not bury a plain-error issue — address it as a freestanding section

**For harmless-error responses (appellee):**

- Argue harmlessness as an alternative ground for affirmance
- Specify the evidence that establishes the error was harmless
- For constitutional errors: argue harmlessness beyond a reasonable doubt [VERIFY standard per issue]

### Step 10: Compliance Check

Before finalizing, verify the brief against all procedural requirements:

**10a. FRAP Rule 28 completeness:**

| Required Element                            | Present | Notes |
| ------------------------------------------- | ------- | ----- |
| Disclosure statement (if required)          | ☐       |       |
| Table of Contents                           | ☐       |       |
| Table of Authorities                        | ☐       |       |
| Jurisdictional Statement (all 4 components) | ☐       |       |
| Statement of Issues                         | ☐       |       |
| Statement of the Case (nature + facts)      | ☐       |       |
| Summary of Argument                         | ☐       |       |
| Argument with standard of review per issue  | ☐       |       |
| Conclusion with specific relief             | ☐       |       |
| Certificate of Compliance                   | ☐       |       |
| Certificate of Service                      | ☐       |       |

**10b. Word count verification:**

```bash
# Count words (excluding sections exempt from limit under Rule 32(f))
wc -w "$BRIEF_FILE"
```

- Opening / response brief: ≤ 13,000 words [VERIFY current FRAP Rule 32 and local rules]
- Reply brief: ≤ 6,500 words [VERIFY]
- Check circuit local rules for any modifications

**10c. Format verification (Rule 32(a)):**

| Requirement                                               | Check |
| --------------------------------------------------------- | ----- |
| 14-point proportional font OR ≤ 10.5 char/inch monospaced | ☐     |
| 1-inch margins all sides                                  | ☐     |
| Double-spaced body text                                   | ☐     |
| Certificate of compliance included                        | ☐     |

**10d. Record citation spot-check:**

Review every factual assertion in the Statement of the Case and Argument sections.
Each must cite to a specific page in the record. Flag any unsupported assertions.

**10e. Table of Authorities accuracy:**

Verify every case, statute, rule, and secondary source cited in the brief appears in
the Table of Authorities with correct page references.

### Step 11: Quality Verification

Run all quality frameworks before delivery.

**11a. Citation Quality Gates** (run silently; revise before delivering):

| Gate          | Rule                                                                                                                    | Fail Action                            |
| ------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Authority** | Every legal proposition cites specific, identified authority                                                            | Add citation or mark `[VERIFY]`        |
| **Pinpoint**  | All case citations include reporter and page; all record citations include specific page/line                           | Add pinpoint or flag                   |
| **Currency**  | Cases checked for overruling, negative treatment, or subsequent history affecting their precedential value              | Flag `[CHECK CURRENCY]`                |
| **Support**   | Cited authority actually supports the proposition for which it is cited (not merely tangentially related)               | Verify accuracy or restate proposition |
| **Format**    | Citations follow correct format: Bluebook for federal, applicable state citation manual for state courts, OSCOLA for UK | Fix format                             |

**11b. Self-Interrogation for key arguments** (run for every issue classified HIGH):

**Pass 1 — Legal Foundation**: Is the legal rule stated correctly under binding authority
in this circuit / jurisdiction? Would a law clerk in this circuit agree with how the
authority is characterized?

**Pass 2 — Record Foundation**: Is every factual assertion accurate and supported by
a specific record citation? Are quotations from the record verbatim and in context?

**Pass 3 — Adversarial Challenge**: What is the appellee's best response to this
argument? Have I anticipated it and addressed it? What is the weakest link in this
argument chain, and have I strengthened or acknowledged it?

**11c. Confidence Scoring** (for each argument section):

| Level         | Range     | Meaning                                                                             | Action                                     |
| ------------- | --------- | ----------------------------------------------------------------------------------- | ------------------------------------------ |
| **Definite**  | 0.95-1.0  | Binding authority directly on point; facts undisputed in record                     | State with confidence                      |
| **High**      | 0.80-0.94 | Strong circuit authority; minor factual questions                                   | State with brief caveat                    |
| **Probable**  | 0.60-0.79 | Good arguments but circuit has not directly addressed; or facts have some ambiguity | State with reasoning and contra-indicators |
| **Possible**  | 0.40-0.59 | Genuinely uncertain; conflicting authority or fact issues                           | Flag for counsel review with both sides    |
| **Uncertain** | 0.0-0.39  | Weak basis; argument speculative                                                    | Do not assert; flag `[UNCERTAIN]`          |

---

## Severity Classification

Classification system for brief-quality issues and argument strength:

### Argument Strength (Your Brief)

| Level           | Criteria                                                                                             | Usage                                 |
| --------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CONTROLLING** | Binding authority in this circuit directly on point; de novo standard; record clearly supports       | Lead argument; most likely to succeed |
| **STRONG**      | Favorable persuasive authority or strong circuit-level support; well-preserved; clear record support | Primary argument sections             |
| **COLORABLE**   | Arguable position with some support; may not prevail; necessary to preserve for further review       | Raise but allocate fewer words        |
| **WEAK**        | Limited support; speculative; undermines credibility to raise                                        | Consider omitting; counsel to decide  |

### Brief Quality Issues

| Classification  | Criteria                                                                                                                    | Action                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **FATAL**       | Jurisdictional defect; brief exceeds word limit; mandatory section missing; untimely filing                                 | Must cure before filing            |
| **MATERIAL**    | Unpreserved issue raised without plain-error analysis; factual assertion without record citation; cited authority overruled | Must address before filing         |
| **SIGNIFICANT** | Weak or non-argumentative point headings; overly long statement of facts; block quotes exceeding one page                   | Should fix; affects persuasiveness |
| **MINOR**       | Style inconsistencies; citation format variations; footnote formatting                                                      | Fix if time permits                |

---

## Prioritization Framework

When the brief is too long or there are competing demands on limited word budget:

| Priority                         | Criteria                                                                                                                                     | Word Budget Guidance                               |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Tier 1 — Must Include**        | Issues with de novo standard; issues directly dispositive of the appeal; strongest-authority arguments                                       | 60-70% of word budget                              |
| **Tier 2 — Should Include**      | Issues with meaningful preserved errors; alternative grounds for reversal                                                                    | 20-30% of word budget                              |
| **Tier 3 — Consider Preserving** | Unpreserved issues requiring plain-error analysis; arguments primarily for future appeals                                                    | 5-10% of word budget; may be omitted if over limit |
| **Omit**                         | Weak arguments that invite skepticism; duplicative arguments already covered; issues not preserved and not qualifying for plain-error review | Zero allocation                                    |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate         | Rule                                                                                       | Fail Action                                    |
| ------------ | ------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| **Source**   | Every legal claim cites a specific case, statute, regulation, or rule                      | Add citation or mark `[VERIFY]`                |
| **Format**   | All citations follow Bluebook (US federal), applicable state format, or OSCOLA (UK)        | Fix format                                     |
| **Currency** | Every cited case checked for negative treatment; every cited statute checked for amendment | Flag `[CHECK CURRENCY]`                        |
| **Support**  | Cited source actually supports the stated proposition                                      | Verify or remove                               |
| **Record**   | Every factual assertion cites a specific record page or appendix page                      | Add cite or flag as `[RECORD CITATION NEEDED]` |

---

## Self-Interrogation for High-Severity Arguments

For any argument classified CONTROLLING or STRONG, and for any issue that is dispositive
of the appeal, apply this 3-pass review before including in the brief:

**Pass 1 — Legal Chain Integrity**: Does the argument follow logically from the cited
authority to this case's facts? Would a neutral judge or law clerk find the chain
persuasive? Is the standard of review correctly identified and does the argument work
under that standard?

**Pass 2 — Record Completeness**: Have I cited all record evidence that supports this
argument? Have I addressed the most damaging record evidence against this argument? Are
my record quotations verbatim and in full context?

**Pass 3 — Adversarial Challenge**: What is the opposing side's best response? What is
the weakest link in my argument? Under what circumstances would my argument lose even
if the court agrees with my legal theory? Have I addressed that?

---

## Anti-Patterns (What NOT to Do)

1. **Kitchen-sinking**: Raising every conceivable issue dilutes the strong ones and
   signals lack of confidence. Limit to the 3-5 strongest preserved issues.

2. **Misstating the standard of review**: Arguing "the district court erred" without
   specifying why under the correct standard is not analysis. Every argument section
   must open by identifying and applying the applicable standard.

3. **Facts without record citations**: Every factual assertion must cite a specific
   record location. "As the evidence showed" is not a citation. Courts disregard
   uncited factual assertions.

4. **Arguing in the Statement of Facts**: Facts belong in the Statement of Facts;
   argument belongs in the Argument section. Mixing them weakens both.

5. **Abandoning the standard in application**: Correctly stating the de novo standard
   and then applying it as if it were abuse-of-discretion review (or vice versa) is a
   structural error that courts notice.

6. **Neutral point headings**: "The District Court's Analysis of the Statute" is not
   a point heading — it is a table of contents entry. Every heading must state a
   conclusion.

7. **Non-argumentative Summary of Argument**: A summary that merely lists the section
   headings is a missed opportunity. The Summary should tell the court why you win,
   not what topics you cover.

8. **Ignoring adverse circuit authority**: If the circuit has a case against you,
   distinguish it or acknowledge its limits — do not pretend it does not exist.
   Courts will notice.

9. **Exceeding word limits**: Even by one word, this is a FRAP violation that can
   result in the brief being rejected. Count before filing.

10. **Missing the jurisdictional statement components**: FRAP 28(a)(4) requires all
    four components. Omitting filing dates or the assertion of finality is a
    correctable error that wastes court time.

11. **Citing secondary sources as authority for legal rules**: Treatises, law review
    articles, and Restatements are persuasive, not binding. Never cite a secondary
    source as if it were controlling authority.

12. **Misusing "clearly erroneous" vs. "abuse of discretion"**: These are distinct
    standards. Clearly erroneous applies to factual findings; abuse of discretion
    applies to discretionary rulings. Conflating them undermines credibility.

13. **Failure to address harmless error (appellee)**: When defending below, always
    argue harmlessness as an alternative ground for affirmance. Do not concede error
    when you can argue the error was harmless.

14. **Raising new arguments in reply**: A reply brief may only respond to arguments
    in the appellee's brief. New arguments in a reply are waived and may be stricken.

15. **Ignoring plain-error requirements for unpreserved issues**: If an issue was not
    raised below, do not argue it as if it were a preserved, de novo issue. Acknowledge
    the plain-error standard and address all four prongs.

16. **UK — Failing to identify specific legal errors in grounds of appeal**: UK grounds
    of appeal must identify each specific error. "The judge was wrong" is not a ground.
    "The judge erred in law in applying [X] test, because [authority] requires [Y]" is.

17. **UK — Filing a US-style brief instead of a skeleton argument**: UK courts use
    skeleton arguments with numbered propositions and authority lists, not US-style
    "briefs" with full narrative arguments. The format difference matters.

18. **Over-quoting**: Block quotations over one page suggest inability to synthesize.
    Quote only the most critical language; paraphrase the rest with citation.

19. **Attacking the lower-court judge personally**: Attack the reasoning, not the
    judge. Personal attacks on the trial judge or magistrate damage credibility
    and may be sanctionable.

20. **Waiting until the last section to state the standard of review**: The standard
    of review should appear at the start of each argument section, not buried or
    relegated to a standalone "Standard of Review" section that the court reads
    separately from the argument.

---

## Writing Standards

Apply these standards before delivering any appellate brief:

**Clarity:**

- One legal proposition per sentence
- One argument per paragraph
- Define all technical legal terms on first use
- Use parallel construction in lists and series

**Concision:**

- Eliminate throat-clearing ("It is important to note that...", "As stated above...")
- Active voice throughout (>80% of sentences)
- Cut nominalizations: prefer "the court held" over "the court made a holding"
- Remove meaningless intensifiers ("clearly," "obviously," "undeniably" — these annoy
  courts; let the argument speak for itself)

**Precision:**

- Use exact statutory language when invoking a statute (quote and cite)
- Quote key language from controlling cases (sparingly; the most important phrase)
- Pinpoint citations throughout — page number for every case; page and line for record
- Distinguish "holding" from "dictum" explicitly where it matters

**Persuasion:**

- Lead with your strongest argument
- Frame each issue from your client's perspective without misrepresenting facts
- Anticipate and address the opposing party's best argument in each section
- Use short, declarative sentences for key propositions

**Before delivery, verify:**

- Word / page count within applicable limits
- All citations verified or marked `[VERIFY]`
- All record citations include specific page/line reference
- All point headings are argumentative conclusions
- Statement of Issues frames each issue favorably
- Summary of Argument synthesizes rather than merely lists
- Conclusion states specific relief requested
- Certificate of Compliance included if required

---

## External Tool Integration

**legalcode-mcp** (if connected):

- Search for binding circuit authority on each issue
- Check negative treatment and overruling history of all cited cases
- Research jurisdiction-specific procedural standards and recent circuit developments
- Verify current statutory text and any recent amendments
- UK: Search for binding Court of Appeal and UKSC authority

**WebSearch** (if legalcode-mcp unavailable):

- Verify current circuit local rules and any recent amendments
- Check court websites for any emergency standing orders or COVID-related rule changes
- Find recent law review articles or secondary sources on novel legal questions

**Graceful degradation:**
If external tools are not connected:

- Mark all case law and statutory citations with `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with analysis of provided materials and general legal knowledge
- Flag that independent authority verification is required before filing

---

## Localization Notes

**For US state appellate courts:**

- Check whether state follows FRAP structure (most do with variations) or has its own
  distinct format
- Verify state-specific word or page limits (most states have them; they vary widely)
- Check whether state requires separate appendix or incorporates it into the brief
- Verify citation format (many states use regional reporters or state citation manuals)
- Note any state-specific standards of review that differ from federal analogs
- Check whether state intermediate court of appeal is typically the final forum or if
  further review is common

**California:**

- Cal. Rules of Court, rules 8.200–8.278 govern Court of Appeal briefs [VERIFY]
- Opening brief: 14,000 words [VERIFY]; reply brief: 7,000 words [VERIFY]
- Appellant's appendix instead of joint appendix (CT and RT references)
- Standard of review: de novo for questions of law; substantial evidence for jury
  verdicts; abuse of discretion for most trial court rulings [VERIFY]

**New York:**

- CPLR Article 55 and 22 NYCRR Part 1250 govern Appellate Division briefs [VERIFY]
- Word and page limits vary by Department [VERIFY per Department]
- Appendix practice: settled record or reproduced record options [VERIFY]
- Citation: New York Official Reports preferred [VERIFY]

**Texas:**

- Texas Rules of Appellate Procedure (TRAP) govern; rules 38–39 cover briefs [VERIFY]
- Opening brief: 27,000 words [VERIFY]; reply brief: 14,000 words [VERIFY]
- Record references: Clerk's Record (CR) and Reporter's Record (RR) [VERIFY]

**Florida:**

- Florida Rules of Appellate Procedure Rule 9.210 governs brief format [VERIFY]
- Word limits depend on brief type; check current rules [VERIFY]
- Record on appeal: index and record volumes; appendices permitted [VERIFY]

**UK Court of Appeal:**

- CPR Part 52 and Practice Directions 52A–52E
- Skeleton arguments, not US-style briefs
- Core bundle required; supplemental bundle for additional documents
- Costs: generally costs follow the event at appeal [VERIFY]
- Permission to appeal required in most civil appeals

**UK Supreme Court:**

- UKSC Rules 2009 and current Practice Directions
- Must raise a point of law of general public importance [VERIFY]
- Application process: Form 1; if granted, Form 3 statement of facts and issues
- 20-page limit on statement of facts and issues [VERIFY]
- Panel typically of 5 justices; important cases may use 7 or 9 [VERIFY]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-appellate-brief-drafter"
  brief_type: "[opening / response / reply / UK skeleton]"
  forum: "[circuit / state court / UK Court of Appeal / UK Supreme Court]"
  case_name: "[case name]"
  appellant_appellee: "[appellant / appellee]"
  issues_on_appeal: [number]
  standards_of_review_identified:
    - "[issue 1]: [standard]"
    - "[issue 2]: [standard]"
  preserved_issues: [number]
  unpreserved_issues_with_plain_error: [number]
  word_count: [number]
  word_limit: [number]
  within_limit: "[yes / no — X words over]"
  record_citations_verified: "[number verified] / [number total factual assertions]"
  authority_sources:
    legalcode_mcp: "[Connected / Not connected]"
    websearch: "[Used / Not used]"
    provided_materials: "[list documents]"
  citations_marked_verify: [number]
  appendix_designated: "[yes / no / deferred]"
  local_rules_checked: "[list rules checked]"
  certificate_of_compliance_included: "[yes / no]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "[Any issues flagged as needing counsel review]"
  reviewer: "AI-assisted — requires qualified appellate counsel review before filing"
```

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original skill synthesizing best practices
from US federal appellate procedure (FRAP Rules 28, 30, 32), circuit-specific local
rules, US state appellate practice, UK Civil Procedure Rules Part 52 and Practice
Directions 52A–52E, and UKSC Rules 2009. Incorporates structural patterns from
`legalcode-opposition-brief-drafter`, `legalcode-brief-analyzer`, and
`legalcode-complaint-drafter`. Research based on FRAP text (December 1, 2024
amendments), circuit local rules, CPR Part 52, and current appellate advocacy
best practices. All cited rules and standards should be independently verified
before use.

---

## Output Format Template

````markdown
# [APPELLANT'S / APPELLEE'S] BRIEF

## [Court Name]

**Case No.** [number]
**[Case caption: [PARTY A], Appellant, v. [PARTY B], Appellee]**
**[On Appeal from the United States District Court for the [District]]**
**[Lower Court Case No. [number]; Honorable [Judge Name]]**

---

## Corporate Disclosure Statement (Rule 26.1)

[State whether any parent corporations or publicly held companies own 10% or more
of the party's stock, or state "None."]

---

## Table of Contents

[Comprehensive listing of all sections with page numbers]

| Section                                         | Page |
| ----------------------------------------------- | ---- |
| Corporate Disclosure Statement                  | i    |
| Table of Authorities                            | ii   |
| Jurisdictional Statement                        | 1    |
| Statement of Issues                             | 2    |
| Statement of the Case                           | 3    |
| Summary of Argument                             | [X]  |
| Argument                                        | [X]  |
| &nbsp;&nbsp;&nbsp;&nbsp;I. [POINT HEADING ONE]  | [X]  |
| &nbsp;&nbsp;&nbsp;&nbsp;II. [POINT HEADING TWO] | [X]  |
| Conclusion                                      | [X]  |
| Certificate of Compliance                       | [X]  |
| Certificate of Service                          | [X]  |

---

## Table of Authorities

**Cases**

| Case                           | Page(s)        |
| ------------------------------ | -------------- |
| [Case name, reporter citation] | [page numbers] |

**Statutes and Rules**

| Authority         | Page(s)        |
| ----------------- | -------------- |
| [Statute or rule] | [page numbers] |

**Other Authorities**

| Authority                    | Page(s)        |
| ---------------------------- | -------------- |
| [Treatise, secondary source] | [page numbers] |

---

## Jurisdictional Statement

**Subject-Matter Jurisdiction of the District Court**: [Statutory basis, e.g.,
"The district court had subject-matter jurisdiction pursuant to 28 U.S.C. § 1331
because Plaintiff's claims arise under [federal statute]."]

**Appellate Jurisdiction**: [Statutory basis, e.g., "This Court has jurisdiction
pursuant to 28 U.S.C. § 1291 because the district court entered a final judgment
on [date]."]

**Timeliness**: [Filing dates: "Judgment was entered on [date]. Appellant filed
its notice of appeal on [date], within [30] days as required by FRAP 4(a)(1)(A)."]

**Finality**: [Assertion that the judgment is final and disposes of all claims.]

---

## Statement of Issues

1. Whether [issue framed favorably to appellant / appellee], where [key fact],
   under [governing standard] — reviewed [de novo / for abuse of discretion].

2. Whether [issue framed favorably to appellant / appellee]...

---

## Statement of the Case

### Nature of the Case

[1-2 paragraphs: who the parties are, what the case is about, how it ended up
on appeal — written to favor client without misrepresenting facts.]

### Procedural History

[Chronological procedural narrative: complaint filed, key motions and rulings,
trial, verdict or decision, final judgment, notice of appeal. Cite to record for
each event: JA ___ / ER ___ / ROA.___]

### Statement of Facts

[Narrative of relevant facts, favorable to client, every material fact cited to
record. Use transitions to guide the reader. Include all facts needed to support
arguments. Include adverse facts the court will see anyway — address them
favorably or acknowledge and minimize.]

---

## Summary of Argument

[1-3 pages. Synthesize why you win on each issue. Do not merely restate the point
headings. Explain the key legal rule, how it applies to your facts, and what
relief it requires. Reference the applicable standards of review. Mention the most
compelling authority. Self-contained — a reader who reads only this section should
understand your theory.]

---

## Argument

### I. [ARGUMENTATIVE POINT HEADING — FIRST ISSUE]

**Standard of Review.** [The district court's [ruling] is reviewed [de novo /
for abuse of discretion / for clear error]. [Authority for standard.]]

[IRAC/CRAC structure:]

**A. [Sub-heading if needed]**

[Rule: State the governing legal standard with binding authority. Application:
Apply rule to the specific facts with record citations. Conclusion: State why
the lower court erred and what this court should do.]

**B. [Sub-heading if needed]**

[Continue argument...]

### II. [ARGUMENTATIVE POINT HEADING — SECOND ISSUE]

**Standard of Review.** [State applicable standard with authority.]

[Continue argument structure...]

---

## Conclusion

For the foregoing reasons, [Appellant/Appellee] respectfully requests that this
Court [state precise relief: "reverse the district court's grant of summary
judgment and remand with instructions to enter judgment in favor of Appellant" /
"affirm the judgment in all respects" / etc.].

Dated: [Date]

Respectfully submitted,

---

[Attorney Name]
[Bar Number]
[Firm Name]
[Address]
[Phone]
[Email]
Counsel for [Appellant/Appellee]

---

## Certificate of Compliance (Rule 32(g))

This brief complies with the type-volume limitation of Fed. R. App. P.
32(a)(7)(B) because it contains [X] words, excluding the parts of the brief
exempted by Fed. R. App. P. 32(f). This brief complies with the typeface
requirements of Fed. R. App. P. 32(a)(5) and the type-style requirements of
Fed. R. App. P. 32(a)(6) because it has been prepared in a proportionally spaced
typeface using [word processor] in [font name and size].

---

[Attorney Name]

---

## Certificate of Service

I hereby certify that on [date], I electronically filed the foregoing brief with
the Clerk of the Court using the CM/ECF system. All participants in the case are
registered CM/ECF users and will be served by the CM/ECF system.

---

[Attorney Name]

---

## Glass Box Audit Trail

```yaml
[Insert completed glass_box YAML block]
```
````
