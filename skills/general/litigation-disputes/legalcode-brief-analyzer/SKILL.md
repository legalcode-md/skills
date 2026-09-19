---
name: legalcode-brief-analyzer
description: Analyze legal briefs for argument strength, authority quality, factual support, logical coherence,
  and persuasive effectiveness. Operates as "code review for legal writing" — systematically evaluating
  brief structure (IRAC/CRAC/CREAC), standard-of-review alignment, citation quality and currency, statement
  of facts persuasiveness, counter-argument anticipation, and court-rules compliance. Supports own-brief
  review (improve before filing) and opposing-brief deconstruction (find weaknesses to exploit). Produces
  structured findings with classification (STRONG / NEEDS WORK / VULNERABLE / CRITICAL), confidence-scored
  assessments, actionable rewrite suggestions, and a Glass Box audit trail. Jurisdiction-agnostic at baseline
  with [JURISDICTION-SPECIFIC] markers for US federal, England & Wales, and Australia. Integrates with
  legalcode-mcp for live authority validation via WebSearch.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Brief Analyzer

> **Disclaimer**: This skill provides a framework for AI-assisted legal brief
> analysis. It does not constitute legal advice. All outputs must be reviewed by
> qualified legal counsel licensed in the relevant jurisdiction before use in any
> proceeding. Procedural rules, evidentiary standards, and case law change
> frequently; verify all authoritative sources before relying on any conclusion.
> AI analysis may miss nuances of advocacy strategy, judicial temperament, and
> local practice that experienced practitioners would recognize. Any cited
> authority marked `[VERIFY]` has not been independently validated and must be
> confirmed before reliance.

---

## Purpose and Scope

This skill performs comprehensive quality analysis of legal briefs — motions,
memoranda of law, appellate briefs, skeleton arguments, and written submissions —
evaluating them across ten dimensions of effectiveness. It is designed for two
primary use cases:

1. **Own-Brief Review** (pre-filing quality assurance): Systematically identify
   weaknesses in your own brief before submission, with actionable rewrite
   suggestions and priority-ranked findings.

2. **Opposing-Brief Deconstruction** (strategic exploitation): Analyze the
   opposing party's brief to identify logical gaps, authority weaknesses, factual
   overstatements, and unexploited concessions.

The skill applies established legal writing frameworks (IRAC, CRAC, CREAC),
scoring criteria from major advocacy competitions, and judicial perspectives on
brief effectiveness to produce confidence-scored, citation-linked assessments.

**Covers:**

- **Argument structure**: IRAC/CRAC/CREAC compliance, issue framing, rule synthesis, application depth
- **Standard of review**: Correct identification and consistent application throughout the brief
- **Authority quality**: Binding vs. persuasive hierarchy, case currency, adverse authority omissions, citation format compliance
- **Factual foundation**: Statement of facts persuasiveness, record support, characterization accuracy
- **Logical coherence**: Fallacy detection, burden allocation, statutory interpretation methodology
- **Counter-argument anticipation**: Pre-emption completeness, strawman avoidance, strongest-argument engagement
- **Writing quality**: Clarity, concision, active voice usage, sentence structure, precision of language
- **Court-rules compliance**: Page/word limits, formatting requirements, certificate of compliance, citation format
- **Strategic effectiveness**: Theme development, theory of the case coherence, disposition pathway
- **Persuasive impact**: Opening strength, closing effectiveness, overall readability, narrative flow

**Does not:**

- Replace counsel's judgment on advocacy strategy or judicial temperament
- Serve as a citator or provide definitive authority status (flags for verification)
- Generate new legal arguments (identifies gaps, does not fill them)
- Make final filing-readiness determinations
- Assess factual merits beyond record-support analysis
- Waive any privilege (analyzes structure, not substance of privileged communications)

**Related skills:**

- `legalcode-contract-review` — Clause-by-clause contract analysis
- `legalcode-case-timeline-builder` — Litigation chronology construction
- `legalcode-early-case-assessment` — Pre-discovery case evaluation
- `legalcode-privilege-review` — Privilege classification for productions
- `legalcode-legal-risk-assessment` — Risk scoring and impact analysis

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the forum, governing
procedural rules, and citation conventions first, then localize analysis
dimensions accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Brief formatting rules (page/word limits, typeface, margins, binding)
- Citation format convention (Bluebook, OSCOLA, AGLC, McGill Guide)
- Standard of review nomenclature and applicable tests
- Authority hierarchy (constitutional structure, court levels, binding scope)
- Procedural rule references for motions practice and appellate briefs
- Ethical obligations regarding adverse authority (Rule 3.3 / SRA Code / ASCR)
- Statement of facts requirements (appendix/record references)
- Oral argument connection points (if brief supports upcoming argument)

**Reference anchors frequently needed:**

- **U.S. federal**: FRAP Rules 28-32; FRCP Rules 12, 56; SCOTUS Rule 24; Bluebook (21st ed.) [VERIFY]
- **England & Wales**: CPR Part 52, PD 52A (skeleton arguments); CPR Part 23 (applications); OSCOLA (4th ed.) [VERIFY]
- **Australia**: Federal Court Rules 2011 (Cth); High Court Rules 2004; AGLC (4th ed.) [VERIFY]
- **Canada**: Federal Courts Rules SOR/98-106; provincial rules vary; McGill Guide (10th ed.) [VERIFY]

---

## Interactive Clarification

Use interactive clarification whenever the answer materially changes analysis
scope, evaluation criteria, or output emphasis. If information is already
provided, skip the question. Proceed with stated defaults when the user does
not respond.

**CLARIFY block 1: Analysis objective**

- Options: `own-brief review (pre-filing QA)`, `opposing-brief deconstruction`, `comparative analysis (own vs. opposing)`, `academic/educational evaluation`
- Default: `own-brief review (pre-filing QA)`
- Why it matters: Own-brief review emphasizes fixable weaknesses with rewrite suggestions; opposing-brief deconstruction emphasizes exploitable gaps and response strategy. Comparative analysis evaluates both briefs side by side.

**CLARIFY block 2: Brief type**

- Options: `appellate brief (opening)`, `appellate brief (response/answering)`, `appellate brief (reply)`, `motion brief (movant)`, `motion brief (opposition)`, `motion brief (reply)`, `trial brief`, `amicus brief`, `skeleton argument (UK)`, `outline of submissions (AU)`, `memorandum of law`, `petition for review/certiorari`
- Default: `appellate brief (opening)`
- Why it matters: Different brief types have different structural requirements, page limits, and evaluation emphases. Reply briefs cannot raise new issues; amicus briefs have standing requirements; skeleton arguments have distinct format rules.

**CLARIFY block 3: Side and posture**

- Options: `appellant/petitioner/movant`, `appellee/respondent/opponent`, `amicus curiae`, `intervenor`, `cross-appellant`
- Default: `appellant/petitioner/movant`
- Why it matters: Changes burden allocation analysis, determines whether standard-of-review framing is correct, and affects counter-argument completeness expectations.

**CLARIFY block 4: Court and jurisdiction**

- Options: `U.S. federal circuit (specify)`, `U.S. district court (specify)`, `U.S. Supreme Court`, `state court (specify)`, `England & Wales (specify level)`, `Australia (specify court)`, `Canada (specify court)`, `other (specify)`
- Default: `U.S. federal circuit`
- Why it matters: Determines applicable formatting rules, citation convention, authority hierarchy, and standard-of-review nomenclature. Some courts have strong preferences on brief style (e.g., 7th Circuit disfavors block quotes; SCOTUS has strict word limits).

**CLARIFY block 5: Available materials**

- Options: `brief only`, `brief + record excerpts`, `brief + lower court opinion`, `brief + opposing brief`, `full briefing set (all briefs + record + opinions below)`
- Default: `brief only`
- Why it matters: With only the brief, analysis focuses on internal quality. With the record, the tool can verify factual support. With the opposing brief, it can assess counter-argument completeness. Full briefing sets enable the most comprehensive analysis.

**CLARIFY block 6: Focus areas (multi-select)**

- Options: `argument structure`, `standard of review`, `authority quality`, `factual foundation`, `logical coherence`, `counter-arguments`, `writing quality`, `court-rules compliance`, `strategic effectiveness`, `all dimensions`
- Default: `all dimensions`
- Why it matters: Allows focused analysis when the user has specific concerns. Analyzing all dimensions produces the most comprehensive report but takes longer.

**CLARIFY block 7: Review depth**

- Options: `quick scan (high-level, 15-minute read)`, `standard review (section-by-section)`, `deep dive (paragraph-by-paragraph with line edits)`, `competition-grade (full rubric scoring)`
- Default: `standard review (section-by-section)`
- Why it matters: Quick scan is appropriate for early drafts or time-sensitive review. Deep dive is appropriate for final pre-filing QA. Competition-grade applies full scoring rubric with numerical grades per dimension.

**CLARIFY block 8: Standard of review (if known)**

- Options: `de novo`, `clearly erroneous`, `abuse of discretion`, `substantial evidence`, `plain error`, `mixed (specify per issue)`, `unknown / determine from brief`, `Wednesbury unreasonableness (UK)`, `House v The King (AU)`
- Default: `unknown / determine from brief`
- Why it matters: If the user knows the applicable standard, the tool can immediately assess whether the brief correctly identifies and consistently applies it. If unknown, the tool will attempt to determine it from the brief text and flag any inconsistencies.

---

## Workflow

### Step 1: Accept brief input

Accept the brief in any of these formats:

- **File path**: Read the file directly (PDF, DOCX, TXT, MD)
- **Pasted text**: Accept inline brief text
- **URL**: Fetch the brief from a web source (PACER, court website, SSRN)
- **Multiple files**: For briefing sets, accept paths to all documents

If the brief is a PDF, use Bash to convert:

```bash
# Attempt pandoc first, fall back to pdftotext
pandoc "$FILE" -t markdown -o "${FILE%.pdf}.md" 2>/dev/null || pdftotext "$FILE" "${FILE%.pdf}.txt"
```

### Step 2: Gather context via interactive clarification

Run through CLARIFY blocks 1-8, skipping any already answered by the initial
prompt. Record all responses (and defaults used) in the Glass Box audit trail.

### Step 3: Structural analysis

Map the brief's architecture against expected structure for its type:

**For appellate briefs (US federal, FRAP 28):**

1. Corporate disclosure statement (FRAP 26.1)
2. Table of contents
3. Table of authorities
4. Jurisdictional statement
5. Statement of the issues presented
6. Statement of the case / Statement of facts
7. Summary of the argument
8. Argument (with point headings)
9. Conclusion (with specific relief requested)
10. Certificate of compliance (FRAP 32(g))
11. Certificate of service

**For skeleton arguments (England & Wales):**

1. Case caption and references
2. Summary of the nature of the dispute (1-2 paragraphs)
3. Chronology and dramatis personae (separate or incorporated)
4. List of issues
5. Discussion of each issue with propositions of law and authority
6. Conclusion with time estimate

**For outline of submissions (Australia, Federal Court):**

1. Case details and parties
2. Issues for determination
3. Outline of propositions relied upon
4. Brief reference to evidence
5. Estimated hearing time

Assess: Are all required sections present? Are they in correct order? Are point
headings argumentative (not merely topical)?

### Step 4: Standard of review analysis

Identify each legal issue in the brief and the standard of review applied:

| Issue     | Standard Applied    | Correct Standard    | Assessment                 |
| --------- | ------------------- | ------------------- | -------------------------- |
| [Issue 1] | [What brief states] | [What it should be] | MATCH / MISMATCH / UNCLEAR |

**Red flags:**

- Brief does not state standard of review at all
- Brief applies de novo to factual findings
- Brief applies abuse of discretion to pure legal questions
- Brief conflates standards across issues
- Brief states standard but argues under a different one
- [JURISDICTION-SPECIFIC] Brief uses U.S. standard nomenclature in non-U.S. forum

### Step 5: Authority quality audit

For each cited authority, assess:

**5a. Hierarchy classification:**

| Authority Level         | Binding Weight                   | Examples                                              |
| ----------------------- | -------------------------------- | ----------------------------------------------------- |
| **Controlling**         | Must follow                      | Supreme/highest court of jurisdiction on point        |
| **Strongly persuasive** | Should follow absent good reason | Same circuit/division, recent, on point               |
| **Persuasive**          | May follow                       | Sister circuits, respected courts, close analogy      |
| **Weakly persuasive**   | Minimal weight                   | Dissents, dicta, distinguishable facts, trial courts  |
| **Secondary**           | Informational                    | Treatises, law reviews, Restatements, practice guides |

**5b. Currency check (flag for verification):**

- Has the case been reversed, vacated, or overruled? `[VERIFY CURRENCY]`
- Is there subsequent negative treatment? `[CHECK SUBSEQUENT HISTORY]`
- Is the statutory provision still current? `[CHECK AMENDMENT STATUS]`

**5c. Adverse authority assessment:**

- Are there obvious controlling cases not cited?
- Does the brief cite authority for a proposition but ignore the same case's statements on a different relevant issue?
- Has the brief complied with ethical obligations to cite known adverse authority?
  - [JURISDICTION-SPECIFIC]: ABA Model Rule 3.3(a)(2) (US), SRA Code para 1.4 (UK), ASCR Rule 19 (AU) [VERIFY]

**5d. Citation format compliance:**

- Does citation format match the required convention?
  - [JURISDICTION-SPECIFIC]: Bluebook (US), OSCOLA (UK), AGLC (AU)
- Are parentheticals informative and accurate?
- Are pinpoint citations provided for all quoted material?
- Are string citations used appropriately (not padding)?

### Step 6: Factual foundation assessment

Evaluate the statement of facts and factual assertions throughout:

**6a. Record support:**

- Does every material factual assertion cite to the record?
- Are citations pinpointed (page:line, not just "Tr.")?
- Do the citations actually support the propositions stated?
- Are record citations in the correct format? [JURISDICTION-SPECIFIC]

**6b. Persuasive narrative:**

- Does the statement of facts tell a coherent story?
- Is the narrative organized effectively (chronological, thematic, or hybrid)?
- Are facts presented in favorable-but-accurate framing?
- Does the statement of facts support the theory of the case?

**6c. Characterization accuracy:**

- Are inferences clearly distinguished from established facts?
- Is testimony fairly characterized (not taken out of context)?
- Are material facts omitted that would change the picture?
- Do characterization words ("merely," "significant," "critical") match the record support?

### Step 7: Logical reasoning evaluation

Assess the quality of legal reasoning throughout the argument:

**7a. Argument structure per issue:**

| Component                | Present? | Quality | Notes                                  |
| ------------------------ | -------- | ------- | -------------------------------------- |
| Issue identification (I) | ☐        | —       | Clear, focused question presented?     |
| Rule statement (R)       | ☐        | —       | Synthesized from multiple authorities? |
| Application (A)          | ☐        | —       | Fact-specific, not conclusory?         |
| Conclusion (C)           | ☐        | —       | Follows logically from application?    |

**7b. Fallacy detection:**

Check for these common legal writing fallacies:

| Fallacy                            | Detection Pattern                                                             | Severity   |
| ---------------------------------- | ----------------------------------------------------------------------------- | ---------- |
| **Conclusory reasoning**           | Application section merely restates rule without fact-specific analysis       | HIGH       |
| **Ignoring adverse authority**     | Known controlling cases on point are not addressed                            | CRITICAL   |
| **Slippery slope**                 | Claims consequence chain without evidence for each link                       | MEDIUM     |
| **Straw man**                      | Mischaracterizes opposing argument then refutes the mischaracterization       | HIGH       |
| **False equivalence**              | Equates materially different situations without addressing distinctions       | MEDIUM     |
| **Appeal to irrelevant authority** | Cites non-binding authority without acknowledging its limited weight          | LOW-MEDIUM |
| **Post hoc reasoning**             | Assumes causation from temporal sequence in causation arguments               | HIGH       |
| **Selective quotation**            | Omits qualifying language from quoted authority                               | CRITICAL   |
| **Burden shifting**                | Implicitly shifts burden of proof/persuasion without acknowledging it         | HIGH       |
| **Conflating standards**           | Applies one standard while arguing under another                              | HIGH       |
| **Dicta reliance**                 | Treats non-essential judicial statements as binding holdings                  | MEDIUM     |
| **Overstatement of holding**       | Describes case as holding X when it only assumed X arguendo                   | HIGH       |
| **Cherry-picking facts**           | Uses facts favorable to position while ignoring contrary facts in same source | HIGH       |

**7c. Statutory interpretation methodology:**

- If the brief interprets a statute, which interpretive canon does it use?
- Is the chosen methodology consistent throughout?
- Are counter-canons addressed (e.g., if relying on legislative history, is textualist objection noted)?
- [JURISDICTION-SPECIFIC]: Post-_Loper Bright_ (2024), has the brief correctly addressed deference to agency interpretation? [VERIFY]

### Step 8: Counter-argument analysis

Assess how well the brief anticipates and addresses opposing positions:

**For own-brief review:**

- Does each major argument address the strongest counter-argument?
- Are counter-arguments engaged substantively (not dismissed with "defendant's argument fails")?
- Are there obvious counter-arguments that are completely unaddressed?
- Does the brief distinguish unfavorable authority rather than ignoring it?

**For opposing-brief deconstruction:**

- What are the opponent's strongest arguments?
- What are the opponent's weakest arguments?
- Where are the logical gaps?
- What concessions does the brief make (explicitly or implicitly)?
- What arguments from the opening brief are not addressed?
- Are there internal contradictions between arguments?

### Step 9: Writing quality and persuasion assessment

**9a. Writing mechanics:**

| Metric                  | Target                                            | Assessment                      |
| ----------------------- | ------------------------------------------------- | ------------------------------- |
| Active voice usage      | >80% of sentences                                 | [calculate approximate ratio]   |
| Average sentence length | 20-25 words                                       | [calculate approximate average] |
| Nominalizations         | Minimal (prefer verbs over -tion/-ment nouns)     | [flag examples]                 |
| Legalese density        | Low (avoid "hereinbefore", "said contract")       | [flag examples]                 |
| Transition usage        | Present between all major sections and arguments  | [assess flow]                   |
| Pronoun clarity         | Every pronoun has a clear, unambiguous antecedent | [flag ambiguities]              |
| Parallel construction   | Used in lists, comparisons, point headings        | [flag violations]               |

**9b. Persuasive techniques:**

| Technique                                                                | Present? | Effectiveness |
| ------------------------------------------------------------------------ | -------- | ------------- |
| Strong opening paragraph (theory of the case stated immediately)         | ☐        | —             |
| Point headings that are persuasive conclusions, not neutral topics       | ☐        | —             |
| Short paragraphs for key points (emphasis through white space)           | ☐        | —             |
| Strategic use of quotation (only when language matters, not for padding) | ☐        | —             |
| Effective use of narrative in statement of facts                         | ☐        | —             |
| Closing that requests specific relief with confidence                    | ☐        | —             |
| Consistent theory/theme threaded throughout                              | ☐        | —             |

**9c. Common writing problems to flag:**

- Block quotes longer than 50 words without explanation of significance
- Excessive footnotes (moving substantive argument to footnotes)
- Passive voice obscuring agency ("mistakes were made")
- Repetition without emphasis purpose
- Weak verb choices ("it is clear that" → "the record establishes")
- Buried conclusions (key point in middle of long paragraph)

### Step 10: Deliver findings

Compile all findings into the Output Format Template (see below). Apply
classification and confidence scoring to each finding. Generate the Glass Box
audit trail. Present findings in priority order (CRITICAL first, then
VULNERABLE, then NEEDS WORK, then STRONG observations).

---

## Argument Structure Patterns

This section provides detailed reference for evaluating argument structure
against established legal writing frameworks.

### IRAC (Issue, Rule, Application, Conclusion)

The foundational legal reasoning framework. Each argument should:

1. **Issue**: State the legal question precisely. Effective issue statements
   contain built-in favorable framing without being argumentative. Compare:
   - Weak: "Whether the contract was breached."
   - Strong: "Whether Defendant's failure to deliver conforming goods within
     the contractually specified 30-day window constitutes a material breach
     entitling Plaintiff to terminate."

2. **Rule**: Synthesize applicable legal rules from relevant authorities.
   A strong rule section does not merely quote a single case — it synthesizes
   a legal standard from multiple authorities:
   - Weak: "Under Smith v. Jones, a material breach occurs when there is a
     substantial failure to perform."
   - Strong: "A breach is material when it goes to the essence of the contract
     and defeats the purpose of the agreement. Smith v. Jones, 500 F.3d at 105.
     Courts apply a multi-factor test considering: (1) the extent of non-performance,
     (2) the likelihood of cure, (3) adequacy of damages, and (4) whether the
     breaching party acted in good faith. Restatement (Second) of Contracts § 241."

3. **Application**: Apply the rule to the specific facts. This is where most
   weak briefs fail — they state the rule and then leap to the conclusion
   without walking through each element with fact-specific analysis:
   - Weak: "Here, Defendant clearly breached the contract."
   - Strong: "Each factor weighs in Plaintiff's favor. First, Defendant's
     non-performance was substantial — it delivered zero of the 500 units
     ordered. JA 45. Second, cure is impossible because the delivery window
     has long closed. JA 67. Third..."

4. **Conclusion**: State the conclusion that follows from the application.
   Must be specific about relief sought.

### CRAC (Conclusion, Rule, Application, Conclusion)

Preferred by many appellate practitioners because it leads with the conclusion,
giving the reader a roadmap. The opening conclusion serves as a thesis statement
for the section. Particularly effective in point headings.

### CREAC (Conclusion, Rule, Explanation, Application, Conclusion)

Adds an "Explanation" step between Rule and Application. The Explanation
illustrates how courts have applied the rule in analogous cases, providing
a bridge between abstract rule and specific application. Most effective when
the rule requires interpretation or the case law is factually analogous.

### Structural Assessment Checklist

For each argument in the brief, verify:

- [ ] Issue is framed as a specific legal question (not a topic heading)
- [ ] Rule is synthesized from multiple authorities (not single-case reliance)
- [ ] Rule includes applicable test/elements/factors where relevant
- [ ] Application walks through each element/factor with specific facts
- [ ] Application cites record evidence for each factual assertion
- [ ] Application distinguishes or addresses unfavorable facts/cases
- [ ] Conclusion follows logically from application (no logical leap)
- [ ] Conclusion specifies what the court should do (not just "should win")
- [ ] Point heading for the section is argumentative (contains a conclusion)
- [ ] Transitions connect this argument to the broader theory of the case

---

## Court Rules Quick Reference

### US Federal — Appellate Briefs (FRAP)

| Rule           | Requirement                             | Limit/Detail                                                                                   |
| -------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| FRAP 28(a)     | Required sections for appellant's brief | Disclosure, TOC, TOA, jurisdiction, issues, facts, summary, argument, conclusion, certificates |
| FRAP 28(b)     | Appellee's brief                        | Same as 28(a); need not include jurisdiction/issues if satisfied with appellant's statements   |
| FRAP 28(c)     | Reply brief                             | Responds only to arguments in appellee's brief; no new issues                                  |
| FRAP 29        | Amicus briefs                           | Requires consent or leave of court; 7-day filing deadline                                      |
| FRAP 32(a)(4)  | Page size                               | 8.5 × 11 inches                                                                                |
| FRAP 32(a)(5)  | Type style                              | 14-point proportional or 12-point monospaced                                                   |
| FRAP 32(a)(6)  | Type face                               | Plain, roman style (no script, italic for emphasis only)                                       |
| FRAP 32(a)(7)  | Length — principal briefs               | 13,000 words or 30 pages                                                                       |
| FRAP 32(a)(7)  | Length — reply briefs                   | 6,500 words or 15 pages                                                                        |
| FRAP 32(a)(7)  | Length — amicus briefs                  | 6,500 words or one-half principal brief limit                                                  |
| FRAP 32(g)     | Certificate of compliance               | Required: word count method stated, count, typeface/type style                                 |
| SCOTUS Rule 24 | Merits briefs                           | 15,000-word limit for opening/response; 6,000 words for reply                                  |

**Common circuit-specific variations** [VERIFY current versions]:

- **7th Circuit**: Operating Procedure 6 — disfavors long block quotes; expects footnotes used sparingly; requires short argument summary up front
- **9th Circuit**: Circuit Rule 28-2.7 — addendum of pertinent statutes/regulations required; 14,000-word limit for some brief types
- **D.C. Circuit**: Handbook of Practice — Certificate of Parties, Rulings Under Review, and Related Cases required
- **5th Circuit**: Local Rule 28.2.1 — statement of issues with reference to record and ruling; brief must be "readable"
- **2nd Circuit**: Local Rule 28.1 — special appendix rules; jurisdictional statement requirements

### England & Wales — Skeleton Arguments

| Requirement       | Detail                                                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Format            | Paginated, A4, double-spaced, numbered paragraphs                                                           |
| Length            | Not more than 25 pages for appeal skeletons (PD 52A para 5.10) [VERIFY]                                     |
| Content           | Summary of nature of dispute, chronology, issues, discussion with propositions and authority, time estimate |
| Filing deadline   | Appellant: with appeal notice or 21 days after notice; Respondent: 14 days before hearing [VERIFY]          |
| Authority bundle  | Separate bundle of authorities, organized by category, paginated                                            |
| Neutral citations | Required: [2024] EWCA Civ 123 format                                                                        |
| Dramatis personae | Required for complex cases with multiple parties                                                            |

### Australia — Federal Court Outline of Submissions

| Requirement     | Detail                                                                       |
| --------------- | ---------------------------------------------------------------------------- |
| Format          | Numbered paragraphs, A4                                                      |
| Length          | Generally 20-30 pages (practice notes vary by division) [VERIFY]             |
| Content         | Issues, propositions of law, brief reference to evidence                     |
| Filing deadline | Varies by practice note; typically 3-5 business days before hearing [VERIFY] |
| Court book      | Applicant responsible for court book with key documents                      |
| Citation format | AGLC (4th ed.): medium-neutral citations + authorized report                 |

---

## Standard of Review — Detailed Reference

### US Federal Standards

| Standard                 | Applies To                                                        | Test                                                                                                                 | Appellant's Burden                                                                 | Key Phrases to Check                                            |
| ------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **De novo**              | Legal questions, statutory interpretation, constitutional issues  | Appellate court decides independently; no deference                                                                  | Show the lower court got the law wrong                                             | "We review de novo", "questions of law"                         |
| **Clearly erroneous**    | Findings of fact (bench trial)                                    | Affirm unless "definite and firm conviction" of error                                                                | Show finding not supported by evidence; not just that another finding was possible | "clearly erroneous", "definite and firm conviction"             |
| **Abuse of discretion**  | Evidentiary rulings, discovery orders, sanctions, case management | Affirm unless "no reasonable person" could agree                                                                     | Show decision was arbitrary, irrational, or based on legal error                   | "abuse of discretion", "no reasonable person"                   |
| **Substantial evidence** | Agency factual findings (APA review)                              | Affirm if "reasonable mind" could accept evidence as adequate                                                        | Show evidence insufficient for any reasonable conclusion                           | "substantial evidence", "reasonable mind"                       |
| **Plain error**          | Unpreserved issues                                                | (1) error, (2) plain, (3) affecting substantial rights, (4) seriously affecting fairness/integrity/public reputation | Show all four prongs (very high bar)                                               | "plain error", "forfeited", "not preserved"                     |
| **Mixed questions**      | Law-fact mix                                                      | Standard depends on whether question is more legal or factual                                                        | Varies — argue for favorable standard                                              | Check whether brief correctly identifies the dominant character |

### England & Wales Standards [VERIFY]

| Standard                        | Applies To                    | Test                                                                          |
| ------------------------------- | ----------------------------- | ----------------------------------------------------------------------------- |
| **Error of law**                | Legal questions               | Appeal court substitutes own view                                             |
| **Perversity**                  | Findings of fact              | No reasonable tribunal could have reached the conclusion                      |
| **Procedural irregularity**     | Process issues                | Decision unjust because of serious procedural or other irregularity           |
| **Wednesbury unreasonableness** | Judicial review of discretion | Decision so unreasonable that no reasonable decision-maker could have made it |

### Australia Standards [VERIFY]

| Standard             | Applies To              | Test                                                                                                       |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Error of law**     | Legal questions         | Full Federal Court determines correct position                                                             |
| **House v The King** | Discretionary decisions | Error of principle, irrelevant consideration, failure to consider relevant matter, or plainly unreasonable |
| **No evidence**      | Factual findings        | No evidence at all, or so lacking that finding unreasonable                                                |

### Standard-of-Review Red Flags

- Brief states "de novo" for factual findings from trial
- Brief states "clearly erroneous" for a legal interpretation question
- Brief argues "abuse of discretion" for summary judgment (legal question → de novo)
- Brief does not identify the standard at all (violates FRAP 28(a)(9)(B))
- Brief states one standard but frames argument under another (e.g., says "de novo" but argues "the judge got the facts wrong")
- Brief applies US standard terminology in a UK or AU proceeding
- Brief does not account for _Loper Bright Enterprises v. Raimondo_ (2024) when addressing agency deference [VERIFY]

---

## Scoring Rubric (Competition-Grade Mode)

When review depth is set to `competition-grade`, apply numerical scoring
across all dimensions. This rubric is adapted from major advocacy competition
scoring criteria.

### Scoring Scale

| Score    | Classification | Description                                                   |
| -------- | -------------- | ------------------------------------------------------------- |
| **9-10** | STRONG         | Excellent; publishable quality; competition-winning           |
| **7-8**  | COMPETITIVE    | Good; above-average practitioner quality; minor issues only   |
| **5-6**  | NEEDS WORK     | Average; adequate but with identifiable weaknesses            |
| **3-4**  | VULNERABLE     | Below average; significant weaknesses that would be exploited |
| **1-2**  | DEFICIENT      | Fundamentally flawed; major revision or rewrite needed        |

### Dimension Weights

| Dimension               | Weight   | Rationale                                                   |
| ----------------------- | -------- | ----------------------------------------------------------- |
| Argument Structure      | 15%      | Foundation; if structure fails, everything fails            |
| Standard of Review      | 10%      | Critical for appellate briefs; dispositive if wrong         |
| Authority Quality       | 15%      | Credibility depends on authority support                    |
| Factual Foundation      | 12%      | Record support is necessary condition for appellate success |
| Logical Reasoning       | 15%      | Core analytical quality; distinguishes strong from weak     |
| Counter-Arguments       | 10%      | Shows thoroughness and intellectual honesty                 |
| Writing Quality         | 8%       | Important but secondary to substance                        |
| Statement of Facts      | 7%       | Persuasive narrative matters but weighs less than argument  |
| Court-Rules Compliance  | 3%       | Binary (compliant or not); low weight but mandatory         |
| Strategic Effectiveness | 5%       | Holistic assessment; synthesis of all other dimensions      |
| **Total**               | **100%** |                                                             |

### Scoring Methodology

For each dimension:

1. Score each criterion within the dimension (1-10)
2. Average criterion scores for the dimension score
3. Apply dimension weight to get weighted contribution
4. Sum weighted contributions for overall score
5. Map overall score to classification:
   - 8.5-10.0 → STRONG
   - 7.0-8.4 → COMPETITIVE
   - 5.0-6.9 → NEEDS WORK
   - 3.0-4.9 → VULNERABLE
   - 1.0-2.9 → DEFICIENT

### Score Calibration Guidelines

To maintain consistency, use these anchor points:

**10/10 (Exceptional)**:

- The kind of brief that wins "Best Brief" awards
- Every authority is binding, current, and directly on point
- Application section walks through each element with specific facts and record cites
- Writing is clear, concise, and compelling
- No identifiable weaknesses

**7/10 (Good)**:

- Competent practitioner work that would satisfy a supervising partner
- Mostly binding authority with good rule synthesis
- Application is fact-specific but could be more thorough in places
- Writing is clear; minor improvements possible
- 1-2 identifiable but non-critical weaknesses

**5/10 (Average)**:

- Adequate for filing but would benefit from another revision
- Mix of binding and persuasive authority; rule synthesis is thin
- Application is sometimes conclusory
- Writing has clarity issues; some passive voice and nominalization
- Multiple identifiable weaknesses, none critical

**3/10 (Below Average)**:

- Below the standard expected for the forum
- Heavy reliance on persuasive authority; missing controlling cases
- Application is largely conclusory ("clearly satisfies the test")
- Writing quality impedes understanding
- Significant weaknesses that opposing counsel would exploit

**1/10 (Deficient)**:

- Should not be filed in current form
- Wrong standard of review or fundamentally flawed legal theory
- No fact-specific application
- Writing quality suggests lack of competent review
- Would likely result in sanctions or summary denial

---

## Persuasive Techniques Assessment

### Opening Paragraph Analysis

The first paragraph of the argument section is the most important paragraph
in the brief. Assess:

| Criterion             | Strong Indicator                                 | Weak Indicator                                                                      |
| --------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Theory stated         | First sentence tells the court why you win       | First sentence recites procedural history                                           |
| Specific vs. abstract | Uses concrete facts and specific legal standards | Uses abstractions ("justice requires")                                              |
| Relief requested      | Makes clear what the court should do             | Leaves the reader guessing what is sought                                           |
| Tone                  | Confident without being strident                 | Either tentative ("we respectfully suggest") or aggressive ("it is beyond dispute") |
| Length                | 4-8 sentences; one focused paragraph             | Runs 2+ pages before getting to the point                                           |

### Point Heading Assessment

Effective point headings function as a persuasive outline — a reader who reads
only the headings should understand the argument and why it should prevail.

| Type                      | Example                                                                                                                            | Assessment                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Argumentative (ideal)** | "The District Court Erred by Applying Heightened Scrutiny Where Rational Basis Review Applies to Regulations of Commercial Speech" | STRONG — states conclusion with specificity                     |
| **Topical (weak)**        | "The Standard of Review"                                                                                                           | NEEDS WORK — tells topic but not argument                       |
| **Conclusory (weak)**     | "The District Court Erred"                                                                                                         | NEEDS WORK — too vague; does not tell reader how or why         |
| **Question-format**       | "Did the District Court Err in Applying Heightened Scrutiny?"                                                                      | NEEDS WORK — point headings should be assertions, not questions |

### Block Quote Assessment

Block quotes should be used sparingly and only when exact language matters:

- **Appropriate**: Statutory text, contractual language, key holding language
- **Inappropriate**: Background facts, procedural history, general legal standards
- **Red flag**: Block quotes longer than 50 words without preceding or following explanatory sentence
- **Red flag**: More than 3 block quotes per page
- **Red flag**: Block quote used to pad argument length
- **Red flag**: Block quote from non-binding source for routine proposition

### Footnote Usage Assessment

| Usage                                     | Assessment                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------ |
| Substantive argument in footnotes         | VULNERABLE — courts may treat as waived; 7th Cir. has criticized this [VERIFY] |
| String citations in footnotes             | Acceptable — keeps text clean                                                  |
| Procedural/background detail in footnotes | Acceptable — de-emphasizes non-essential information                           |
| Excessive footnotes (>3 per page)         | NEEDS WORK — disrupts reading flow                                             |
| "See also" citations in footnotes         | Acceptable — supplements without cluttering                                    |

---

## Statutory Interpretation Methodology Assessment

When the brief interprets a statute, assess which interpretive tools are used
and whether they are applied correctly and consistently.

### Textualist Canons

| Canon                    | Correct Use                                                                 | Misuse Pattern                                                      |
| ------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Plain meaning**        | Word given ordinary meaning; dictionary citation to contemporaneous edition | Cherry-picking one dictionary when others support opposing meaning  |
| **Noscitur a sociis**    | Word interpreted by reference to surrounding words                          | Ignoring that the word has independent meaning beyond its neighbors |
| **Ejusdem generis**      | General term following specific terms limited to same class                 | Applying when general term intentionally broader                    |
| **Expressio unius**      | Expression of one thing excludes others                                     | Applying when list is illustrative ("including but not limited to") |
| **Whole act rule**       | Same word means the same thing throughout statute                           | Ignoring that context can change meaning                            |
| **Surplusage avoidance** | Every word has meaning; no redundancy                                       | Treating intentionally duplicative terms as surplus                 |

### Purposivist Tools

| Tool                      | Correct Use                                     | Misuse Pattern                                                             |
| ------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------- |
| **Legislative history**   | Committee reports, floor statements of sponsors | Using colloquy of non-sponsoring member; citing post-enactment history     |
| **Legislative purpose**   | Purpose stated in preamble or findings section  | Inventing purpose not supported by text or history                         |
| **Remedial construction** | Broad reading of remedial statutes              | Stretching text beyond its natural reading under guise of remedial purpose |

### Post-Chevron Landscape [VERIFY]

After _Loper Bright Enterprises v. Raimondo_, 144 S. Ct. 2244 (2024):

- Chevron deference is overruled
- Courts apply _Skidmore_ deference (agency interpretation persuasive based on thoroughness, reasoning, consistency, and other indicia of care)
- Briefs that still invoke Chevron deference should be flagged as CRITICAL
- Briefs challenging agency action should address the new standard
- [JURISDICTION-SPECIFIC]: This applies only to US federal courts; state Chevron-like doctrines may still apply

---

## Deep Brief Analysis Framework

The following ten dimensions form the core evaluation framework. Each dimension
is scored on a 4-level classification with confidence thresholds.

### Dimension 1: Argument Structure

| Criterion            | STRONG                                                                        | NEEDS WORK                                                       | VULNERABLE                                                        | CRITICAL                                                    |
| -------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| Issue framing        | Issues presented as concrete questions with built-in favorable framing        | Issues identified but stated neutrally or abstractly             | Issues unclear, overlapping, or improperly framed                 | Issues missing, misstated, or fundamentally flawed          |
| Rule synthesis       | Rules synthesized from multiple authorities into coherent framework           | Rules stated from single authority, adequate but thin            | Rules stated conclusorily without authority support               | Rules wrong, incomplete, or based on inapplicable authority |
| Application depth    | Fact-specific application that walks through each element with record support | Application addresses elements but somewhat conclusory in places | Application is largely conclusory ("clearly satisfies")           | Application missing or disconnected from facts              |
| Point headings       | Argumentative, specific, persuasive — miniature brief                         | Adequate but somewhat generic or merely topical                  | Weak, vague, or non-argumentative                                 | Missing, misleading, or contradicted by argument below      |
| Organizational logic | Each section builds on prior sections; reader never feels lost                | Generally logical but with some jarring transitions              | Organization obscures the argument; reader must reconstruct logic | No discernible organizational logic                         |

### Dimension 2: Standard of Review

| Criterion               | STRONG                                                               | NEEDS WORK                                               | VULNERABLE                                             | CRITICAL                                            |
| ----------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------- |
| Identification          | Correct standard identified for each issue with supporting authority | Correct standard stated but without supporting authority | Standard stated but wrong or inconsistent across brief | Standard not identified or fundamentally misapplied |
| Application consistency | Arguments consistently framed within stated standard throughout      | Mostly consistent with occasional drift                  | Frequently argues under different standard than stated | Arguments incompatible with stated standard         |
| Burden acknowledgment   | Correctly states and addresses burden of proof/persuasion            | Acknowledges burden but does not consistently address it | Ignores or misstates burden                            | Implicitly shifts burden to wrong party             |

### Dimension 3: Authority Quality

| Criterion             | STRONG                                                  | NEEDS WORK                                                | VULNERABLE                                                         | CRITICAL                                                                 |
| --------------------- | ------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Hierarchy compliance  | Controlling authority cited for each key proposition    | Mostly binding authority with some persuasive gap-filling | Heavy reliance on persuasive authority when binding exists         | Key propositions supported only by non-binding or inapplicable authority |
| Currency              | All authorities current; subsequent history clean       | Most authorities current; 1-2 may need checking           | Multiple authorities with unknown or concerning subsequent history | Key authorities overruled, vacated, or superseded                        |
| Adverse authority     | All known adverse authority addressed and distinguished | Most adverse authority addressed; minor gaps              | Significant adverse authority unaddressed                          | Controlling adverse authority deliberately ignored                       |
| Citation format       | Fully compliant with applicable convention              | Mostly compliant with minor format errors                 | Inconsistent format, missing pinpoints                             | Pervasive format errors, no pinpoints, wrong convention                  |
| Parenthetical quality | Informative, accurate, adds value                       | Present but generic or occasionally misleading            | Sporadic, uninformative, or missing for key citations              | Missing, misleading, or mischaracterizing cited authority                |

### Dimension 4: Factual Foundation

| Criterion                 | STRONG                                                      | NEEDS WORK                                       | VULNERABLE                                              | CRITICAL                                            |
| ------------------------- | ----------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------- | --------------------------------------------------- |
| Record support            | Every material fact cited to specific record location       | Most facts supported; some general references    | Multiple material facts unsupported or vaguely cited    | Key facts unsupported; assertions contradict record |
| Narrative quality         | Compelling, coherent story that supports theory of the case | Adequate chronology but lacks narrative drive    | Disorganized, confusing, or fails to support argument   | Misleading, inaccurate, or internally contradictory |
| Characterization accuracy | Fair, accurate characterization; inferences clearly marked  | Generally accurate with occasional overstatement | Multiple overstatements or misleading characterizations | Material misrepresentations of record evidence      |
| Completeness              | All material facts included, favorable and unfavorable      | Most material facts included; minor omissions    | Significant favorable-only selection                    | Material omissions that would change analysis       |

### Dimension 5: Logical Reasoning

| Criterion                | STRONG                                                             | NEEDS WORK                                   | VULNERABLE                                            | CRITICAL                                                          |
| ------------------------ | ------------------------------------------------------------------ | -------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------- |
| Deductive validity       | Arguments follow logically from premises; no gaps                  | Generally sound with minor logical gaps      | Multiple logical leaps or unexamined assumptions      | Fundamental logical errors; conclusion does not follow            |
| Fallacy avoidance        | No identifiable fallacies                                          | 1-2 minor informal fallacies                 | Multiple fallacies or 1 significant formal fallacy    | Arguments rest on fallacious reasoning                            |
| Interpretive methodology | Consistent, appropriate interpretive framework                     | Methodology adequate but not fully developed | Inconsistent methodology or misapplied canons         | Wrong interpretive framework or no methodology at all             |
| Analogical reasoning     | Factual parallels developed with precision; distinctions addressed | Analogies drawn but not fully developed      | Analogies superficial or ignore material distinctions | Analogies to clearly distinguishable cases without acknowledgment |

### Dimension 6: Counter-Argument Anticipation

| Criterion             | STRONG                                                    | NEEDS WORK                                                           | VULNERABLE                                   | CRITICAL                                                    |
| --------------------- | --------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| Completeness          | All foreseeable counter-arguments addressed substantively | Major counter-arguments addressed; minor ones omitted                | Significant counter-arguments unaddressed    | Obvious dispositive counter-arguments completely ignored    |
| Quality of engagement | Strongest form of counter-argument engaged, not straw man | Counter-arguments addressed but sometimes weakened before refutation | Counter-arguments addressed superficially    | Counter-arguments strawmanned or dismissed without analysis |
| Unfavorable authority | Distinguished with specificity and candor                 | Distinguished but somewhat formulaically                             | Mentioned but not meaningfully distinguished | Ignored or mischaracterized                                 |

### Dimension 7: Writing Quality

| Criterion             | STRONG                                           | NEEDS WORK                                        | VULNERABLE                                                  | CRITICAL                                                        |
| --------------------- | ------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| Clarity               | Every sentence conveys its meaning on first read | Generally clear; occasional re-reading needed     | Frequently unclear; ambiguous constructions                 | Pervasively unclear; reader cannot follow argument              |
| Concision             | No wasted words; each sentence earns its place   | Generally concise with some padding               | Verbose; arguments diluted by unnecessary repetition        | Excessively long; key arguments buried in verbiage              |
| Voice and tone        | Confident, professional, appropriately assertive | Adequate tone; occasionally tentative or strident | Inconsistent tone; inappropriately combative or deferential | Unprofessional tone; ad hominem, sarcasm, or excessive rhetoric |
| Grammar and mechanics | Error-free                                       | Minor errors that do not impede understanding     | Noticeable errors that distract from argument               | Pervasive errors that undermine credibility                     |

### Dimension 8: Statement of Facts

| Criterion          | STRONG                                                                         | NEEDS WORK                                                          | VULNERABLE                                             | CRITICAL                                                      |
| ------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------- |
| Organization       | Clear organizing principle; reader understands story immediately               | Adequate organization; generally chronological                      | Disorganized; reader must reconstruct story            | No discernible organization; facts scattered throughout brief |
| Persuasion         | Facts selected and ordered to support theory; unfavorable facts contextualized | Generally supportive of argument; some facts could be better framed | Neutral recitation that fails to advance the narrative | Facts inadvertently undermine own argument                    |
| Record integration | Seamless record citations; reader can verify every assertion                   | Most assertions cited; citations generally accurate                 | Sporadic citations; some assertions unverifiable       | Few or no record citations; assertions unsupported            |
| Completeness       | All material facts, including unfavorable ones, fairly presented               | Most material facts present; minor omissions                        | Significant omissions; one-sided presentation          | Material facts omitted or misrepresented                      |

### Dimension 9: Court-Rules Compliance

| Criterion         | STRONG                                                                  | NEEDS WORK                                            | VULNERABLE                                        | CRITICAL                                                  |
| ----------------- | ----------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------- |
| Formatting        | Fully compliant with all applicable rules (type size, margins, spacing) | Mostly compliant; minor deviations                    | Multiple formatting violations                    | Briefs likely to be rejected or struck for non-compliance |
| Length            | Well within limits with no wasted space                                 | Within limits but could be more concise               | At or slightly over limits                        | Over limits; requires leave of court or will be rejected  |
| Required sections | All required sections present and properly labeled                      | Most required sections present; minor labeling issues | Required sections missing or improperly formatted | Fundamental structural non-compliance                     |
| Certificates      | All required certificates included and accurate                         | Certificates present but with minor errors            | Certificates missing or with material errors      | No certificates of compliance or service                  |

### Dimension 10: Strategic Effectiveness

| Criterion           | STRONG                                                           | NEEDS WORK                                                | VULNERABLE                                            | CRITICAL                                                             |
| ------------------- | ---------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- |
| Theory of the case  | Clear, consistent theme that unifies all arguments               | Theme present but not fully developed or consistent       | No clear unifying theory; arguments feel disconnected | Theory undermined by own arguments or concessions                    |
| Disposition pathway | Clear path for court to rule in favor; specific relief requested | General path visible; relief requested but vague          | Unclear what ruling is sought or how court gets there | No clear path to relief; brief reads as grievance not legal argument |
| Issue selection     | Issues carefully selected; strongest arguments emphasized        | Most arguments worth making; some weak arguments included | Weak arguments dilute strong ones; no prioritization  | Frivolous arguments undermine credibility of legitimate ones         |
| Audience awareness  | Tailored to specific court/judge; appropriate level of context   | Generally appropriate for the forum                       | Mismatch between brief style and forum expectations   | Fundamentally inappropriate for the audience                         |

---

## Classification System

Each finding is classified into one of four severity levels:

| Classification | Definition                                                                             | Confidence Threshold | Action                                                                   |
| -------------- | -------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------ |
| **STRONG**     | Effective, well-executed element; no changes needed                                    | ≥ 0.80               | Note as strength; no action required                                     |
| **NEEDS WORK** | Adequate but improvable; enhancing would strengthen the brief                          | ≥ 0.60               | Provide specific improvement suggestion                                  |
| **VULNERABLE** | Weakness that a competent opposing counsel would exploit or a court would notice       | ≥ 0.80               | Provide rewrite suggestion with explanation; prioritize for revision     |
| **CRITICAL**   | Fundamental flaw that could result in sanctions, waiver, or dispositive adverse ruling | ≥ 0.90               | Provide urgent rewrite with detailed explanation; must fix before filing |

**Classification decision rules:**

- A finding is CRITICAL only if confidence ≥ 0.90 AND the flaw is potentially dispositive, sanctionable, or constitutes ethical violation
- A finding is VULNERABLE only if confidence ≥ 0.80 AND the flaw would likely be noticed and exploited
- A finding is NEEDS WORK only if confidence ≥ 0.60 AND improvement would materially strengthen the brief
- A finding is STRONG only if confidence ≥ 0.80 AND the element represents genuinely effective advocacy
- If confidence falls below the threshold, downgrade one level and flag the uncertainty

---

## Opposing Brief Analysis Mode

When the analysis objective is `opposing-brief deconstruction`, shift emphasis
from improvement suggestions to exploitation opportunities:

### Opposing Brief Workflow

1. **Read the opposing brief in full** before beginning analysis. Note first
   impressions: What is the strongest argument? What feels weakest?

2. **Map the argument structure**: Create an outline of every argument and
   sub-argument. Identify the logical chain for each.

3. **Identify the linchpin**: What is the single argument or factual claim that
   the entire opposing position depends on? If you defeat this, does the rest
   collapse?

4. **Authority audit**: For each cited authority:
   - Is it actually on point, or does the brief stretch it?
   - Is the parenthetical accurate?
   - Is there contrary language in the same case that was omitted?
   - Is the case still good law? `[VERIFY CURRENCY]`
   - Is it binding in this forum?

5. **Factual claims audit**: For each material factual assertion:
   - Is it supported by the record citation given?
   - Does the record citation actually say what the brief claims?
   - Are there contrary facts in the record not mentioned?
   - Are characterizations fair or overstatements?

6. **Concession mining**: Identify every concession, admission, or narrowing:
   - Explicit concessions ("Plaintiff does not dispute that...")
   - Implicit concessions (arguments conspicuously not made)
   - Scope limitations ("Even assuming arguendo...")
   - Abandoned positions (arguments raised below but dropped on appeal)

7. **Counter-argument gaps**: Identify your strongest arguments that the
   opposing brief either fails to address or addresses inadequately.

8. **Internal contradictions**: Look for positions within the brief that are
   in tension with each other. Does an argument on issue 1 undermine the
   position on issue 3?

### Opposing Brief Output Additions

In addition to the standard findings, produce:

- **Exploitation Priority Matrix**: Ranked list of weaknesses by impact × exploitability
- **Response Strategy Suggestions**: For each major opposing argument, suggest response approach
- **Concession Inventory**: Complete list of concessions with citation to brief page
- **Missing Authority List**: Key cases the opponent should have cited but didn't
- **Factual Vulnerability Map**: Material facts claimed without adequate support

---

## Actionable Output Per Finding

Each finding follows this template:

```yaml
finding:
  id: "F-001"
  dimension: "Authority Quality"
  criterion: "Adverse authority"
  classification: "VULNERABLE"
  confidence: 0.85
  summary: "Brief does not address Smith v. Jones (2023), the controlling circuit authority on the applicable limitation period, which holds the opposite of the brief's position."
  location: "Argument Section III.B, pages 24-28"
  impact: "Opposing counsel will cite Smith v. Jones in response; court will question credibility if not addressed. Could be dispositive on limitations issue."
  current_text: "The statute of limitations is three years. See Generic v. Citation, 500 F.3d 100, 105 (Xth Cir. 2020)."
  suggested_fix: "Acknowledge Smith v. Jones and distinguish on factual grounds — specifically, [factual distinction]. Alternative: argue Smith v. Jones was wrongly decided and seek reconsideration en banc or certiorari."
  priority: "Tier 1 — Must fix before filing"
  self_interrogation:
    pass_1_legal_chain: "Smith v. Jones is a published panel opinion in the same circuit, directly on point. The brief's position cannot survive without addressing it."
    pass_2_completeness: "Checked for subsequent cases limiting Smith v. Jones; none found [VERIFY]."
    pass_3_adversarial: "Opposing counsel would argue Smith v. Jones controls and brief's failure to cite it violates Rule 3.3(a)(2). This is the strongest counter-argument."
```

---

## Prioritization Framework

### Tier 1 — Must Fix (CRITICAL + high-impact VULNERABLE)

- Findings that could result in sanctions, waiver, or case loss
- Missing controlling adverse authority
- Fundamental standard-of-review errors
- Material misrepresentations of record or authority
- Court-rules violations that would result in rejection

### Tier 2 — Should Fix (VULNERABLE + high-impact NEEDS WORK)

- Findings that opposing counsel will exploit
- Logical gaps that undermine otherwise strong arguments
- Authority quality issues on important propositions
- Factual foundation weaknesses on material points
- Counter-argument gaps on foreseeable issues

### Tier 3 — Consider Fixing (NEEDS WORK + STRONG observations)

- Writing quality improvements
- Additional authority that would strengthen existing arguments
- Structural reorganization suggestions
- Persuasion technique enhancements
- Citation format cleanup

---

## Citation Quality Gates

Apply these gates before delivery. If any fail, revise the relevant finding.

| Gate           | Rule                                                                            | Fail Action                                                     |
| -------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Source**     | Every finding cites specific brief page/section and dimension/criterion         | Add location or mark `[LOCATION NEEDED]`                        |
| **Format**     | Citations use consistent format (page:line or section reference)                | Normalize citation format                                       |
| **Currency**   | Authority cited in findings has been flagged for verification if status unknown | Add `[VERIFY CURRENCY]`                                         |
| **Domain**     | Jurisdiction-specific statements limited to selected forum                      | Remove jurisdiction bleed; add `[JURISDICTION-SPECIFIC]` marker |
| **Confidence** | Confidence score aligns with classification threshold requirements              | Downgrade classification if confidence insufficient             |

---

## Self-Interrogation (For VULNERABLE and CRITICAL Findings)

Apply three passes before finalizing high-impact findings:

**Pass 1 — Legal Chain Integrity**
Does the claimed weakness actually exist? Re-read the brief passage. Is there
a plausible reading that cures the identified problem? Would a charitable
reading by the court excuse this flaw?

**Pass 2 — Completeness**
What information would change this assessment? Is there a case, record excerpt,
or procedural rule that the analyst might be missing? Flag any gap in the
analyst's knowledge that could affect the conclusion.

**Pass 3 — Adversarial Challenge**
Would the brief's author have a reasonable response to this finding? What is
the strongest defense of the passage as written? If the defense is plausible,
downgrade the classification and note the uncertainty.

If unresolved after Pass 3, maintain the classification but add an explicit
uncertainty note to the finding.

---

## Confidence Scoring

| Level        | Range     | Interpretation                                                          | Action                                                   |
| ------------ | --------- | ----------------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.00 | Clear error visible on face of brief; no reasonable alternative reading | Report as stated                                         |
| **High**     | 0.80-0.94 | Strong evidence of weakness; charitable reading unlikely to cure        | Report with brief caveat                                 |
| **Probable** | 0.60-0.79 | More likely than not a weakness but alternative reading exists          | Report with alternative reading noted                    |
| **Possible** | 0.40-0.59 | May be a weakness depending on context not visible in brief             | Flag for human review; do not classify above NEEDS WORK  |
| **Unlikely** | 0.00-0.39 | Probably not a real weakness; analyst uncertainty dominates             | Exclude from main findings; note in appendix if relevant |

---

## Sub-Agent Architecture (For Large or Multi-Brief Analysis)

When analyzing a briefing set (>50 pages combined) or performing comparative
analysis, delegate to parallel sub-agents:

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR (Opus)                       │
│                                                             │
│   Accepts input → Creates analysis plan → Delegates →       │
│   Synthesizes findings → Applies classification →            │
│   Generates report                                          │
└─────────┬───────────┬───────────┬───────────┬──────────────┘
          │           │           │           │
          ▼           ▼           ▼           ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Structure   │ │  Authority   │ │   Factual    │ │   Writing    │
│  Analyst     │ │  Auditor     │ │  Verifier    │ │   Quality    │
│  (Sonnet)    │ │  (Sonnet)    │ │  (Sonnet)    │ │  (Haiku)     │
│              │ │              │ │              │ │              │
│ Dims 1,2,6  │ │ Dims 3,5     │ │ Dims 4,8     │ │ Dims 7,9     │
│              │ │              │ │              │ │              │
│ Structure,   │ │ Authority    │ │ Factual      │ │ Writing      │
│ Standard of  │ │ quality,     │ │ foundation,  │ │ quality,     │
│ Review,      │ │ Logical      │ │ Statement    │ │ Court-rules  │
│ Counter-args │ │ reasoning    │ │ of facts     │ │ compliance   │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
                                                          │
                                                          ▼
                                                   ┌──────────────┐
                                                   │  Strategic   │
                                                   │  Evaluator   │
                                                   │  (Opus)      │
                                                   │              │
                                                   │ Dim 10       │
                                                   │              │
                                                   │ Strategic    │
                                                   │ effectiveness│
                                                   │ + synthesis  │
                                                   └──────────────┘
```

**Delegation via Task tool:**

```
Task(subagent_type="general-purpose", model="sonnet", prompt="...")
```

Each sub-agent receives:

- The relevant sections of the brief
- The specific dimensions to evaluate
- The CLARIFY context (court, jurisdiction, standard of review, side)
- The finding template and classification rules
- Instructions to return structured YAML findings

The orchestrator:

- Merges findings from all sub-agents
- Resolves conflicting assessments (e.g., if Structure Analyst and Authority Auditor disagree on whether an argument is VULNERABLE)
- Applies global classification
- Generates the unified report
- Creates the Glass Box audit trail

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-brief-analyzer"
  skill_version: "1.0"
  topic: "legal brief quality analysis"
  jurisdiction: "[selected jurisdiction or jurisdiction-agnostic]"

  # Analysis metadata
  analysis_mode: "[own-brief review | opposing-brief deconstruction | comparative]"
  brief_type: "[appellate opening | motion | skeleton argument | ...]"
  court: "[court name and level]"
  side: "[appellant | appellee | movant | ...]"
  review_depth: "[quick scan | standard | deep dive | competition-grade]"

  # Input summary
  input_summary:
    brief_page_count: "[count]"
    brief_word_count: "[count]"
    additional_materials: "[list of additional documents provided]"
    focus_areas: "[list of selected dimensions]"

  # CLARIFY responses
  clarify_responses:
    block_1_objective: "[response or default used]"
    block_2_brief_type: "[response or default used]"
    block_3_side: "[response or default used]"
    block_4_court: "[response or default used]"
    block_5_materials: "[response or default used]"
    block_6_focus: "[response or default used]"
    block_7_depth: "[response or default used]"
    block_8_standard: "[response or default used]"

  # Analysis summary
  findings_summary:
    total_findings: "[count]"
    critical: "[count]"
    vulnerable: "[count]"
    needs_work: "[count]"
    strong: "[count]"
    overall_assessment: "[STRONG | COMPETITIVE | NEEDS WORK | VULNERABLE | DEFICIENT]"

  # Dimension scores (competition-grade only)
  dimension_scores:
    argument_structure: "[classification]"
    standard_of_review: "[classification]"
    authority_quality: "[classification]"
    factual_foundation: "[classification]"
    logical_reasoning: "[classification]"
    counter_argument: "[classification]"
    writing_quality: "[classification]"
    statement_of_facts: "[classification]"
    court_rules: "[classification]"
    strategic_effectiveness: "[classification]"

  # Authority audit
  authority_audit:
    total_citations: "[count]"
    binding_authority: "[count]"
    persuasive_authority: "[count]"
    secondary_sources: "[count]"
    flagged_for_currency_check: "[count]"
    adverse_authority_gaps: "[count]"
    format_errors: "[count]"

  # Sub-agent execution (if used)
  subagent_execution:
    agents_spawned: "[count]"
    agent_models: "[list]"
    total_tokens: "[approximate count]"

  # Limitations and caveats
  limitations:
    - "Authority currency not independently verified — all [VERIFY CURRENCY] flags require citator check"
    - "Analysis based on brief text only; oral argument dynamics not assessed"
    - "[additional context-specific limitations]"

  # Research performed
  research_performed:
    web_searches: "[count]"
    authority_lookups: "[count]"
    rule_verifications: "[count]"

  completed_at: "[ISO timestamp]"
```

---

## Anti-Patterns

Avoid these failure modes in brief analysis:

### Analysis Process Anti-Patterns

1. **Skipping full read-through** — Beginning analysis without reading the entire brief first; context from later sections may change early assessments
2. **Anchoring on first impression** — Letting initial reaction dominate; apply systematic framework before concluding
3. **Confirmation bias in classification** — Finding what you expect to find; challenge every CRITICAL and VULNERABLE finding via Self-Interrogation
4. **Ignoring brief type** — Applying appellate brief standards to a motion brief or vice versa
5. **Wrong jurisdiction lens** — Using US federal standards for a state court brief or UK skeleton argument standards for a US brief

### Authority Assessment Anti-Patterns

6. **Assuming cited cases are correctly characterized** — Always verify parentheticals against actual holdings; brief authors sometimes misstate holdings
7. **Treating all citations equally** — Not distinguishing binding from persuasive; a brief citing 20 persuasive cases but no controlling authority is VULNERABLE
8. **Currency assumption** — Assuming cited cases are still good law without flagging for verification
9. **Missing adverse authority you don't know about** — Be transparent about the limits of analysis; flag `[VERIFY: check for adverse authority in this area]`
10. **Counting citations instead of weighing them** — A single controlling case outweighs twenty string citations

### Reasoning Evaluation Anti-Patterns

11. **Punishing advocacy** — Characterizing legitimate persuasive framing as "bias" or "misleading"; advocates are supposed to advocate
12. **Demanding both sides in a brief** — A brief is not an academic paper; it should not present both sides neutrally — it should present its client's position persuasively while fairly addressing counter-arguments
13. **Applying wrong standard** — Evaluating a reply brief for arguments that belong in the opening brief; reply briefs respond to the answering brief
14. **Confusing strong advocacy with fallacy** — Forceful argument is not the same as straw man; only flag as fallacy when the logical structure is actually flawed
15. **Imposing academic structure** — Not every effective brief follows rigid IRAC; some briefs effectively use narrative, thematic, or hybrid structures

### Output Anti-Patterns

16. **Vague findings** — "The argument could be stronger" without specifying how, where, and why
17. **No suggested fixes** — Identifying problems without actionable solutions; every VULNERABLE or CRITICAL finding must include a rewrite suggestion
18. **Classification inflation** — Marking everything as CRITICAL destroys signal; reserve CRITICAL for genuinely dispositive or sanctionable issues
19. **Classification deflation** — Marking genuine problems as NEEDS WORK to avoid seeming harsh; err on the side of candor
20. **Ignoring strengths** — Only reporting weaknesses; noting STRONG elements provides balance and helps prioritize effort
21. **Excessive findings** — 50+ findings overwhelm the reader; group minor issues and focus on the 10-15 most impactful
22. **Missing the forest for the trees** — Cataloguing citation format errors while missing that the brief's core theory is legally untenable

### Ethical Anti-Patterns

23. **Opining on factual merits** — The skill assesses brief quality, not whether the underlying claims are meritorious
24. **Making privilege determinations** — If the brief references privileged communications, flag but do not analyze substance
25. **Suggesting unethical tactics** — Never recommend concealing adverse authority, mischaracterizing facts, or other Rule 3.3/3.4 violations [VERIFY rule numbers per jurisdiction]

---

## Writing Standards

Apply these standards to all skill output:

1. **Active voice**: Use active voice in all findings and suggestions. "The brief fails to cite Smith v. Jones" not "Smith v. Jones is not cited by the brief."
2. **Section citations**: Every finding must reference the specific brief section, page, and (where possible) paragraph or line.
3. **Concision**: Findings should be 2-4 sentences. Extended discussion belongs in the suggested_fix field, not the summary.
4. **Specificity**: Name the case, the page, the rule, the exact problem. "Authority quality is weak" is not a finding.
5. **Balanced tone**: Professional, direct, constructive. Not academic, not adversarial. The goal is to help improve the brief (own-brief mode) or to accurately assess it (opposing mode).
6. **Confidence calibration**: If uncertain about a finding, say so explicitly rather than hedging with weasel words. "Confidence: 0.65 — this may be addressed by materials not provided" is better than "It seems like this might possibly be an issue."
7. **No legal advice**: The skill provides analytical observations, not legal conclusions. Frame findings as "the brief does not address X" rather than "the law requires X."

---

## Ethical Obligations Quick Reference

### Duty to Cite Adverse Authority

Lawyers have an ethical obligation to disclose directly adverse, controlling
legal authority to the tribunal, even if opposing counsel fails to cite it.

| Jurisdiction              | Rule                          | Scope                                                                           | Consequence of Violation                                       |
| ------------------------- | ----------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **US (ABA Model Rules)**  | Rule 3.3(a)(2)                | Directly adverse controlling authority in the jurisdiction                      | Discipline; potential sanctions; court loses trust in advocate |
| **US (state variations)** | Varies by state bar           | Some states apply broader duty than ABA model [VERIFY]                          | State-specific discipline                                      |
| **England & Wales**       | SRA Code of Conduct, para 1.4 | Duty not to mislead the court; includes by omission                             | Professional misconduct; wasted costs order [VERIFY]           |
| **Australia**             | ASCR Rule 19                  | Must inform court of all relevant decisions known, including adverse            | Professional misconduct [VERIFY]                               |
| **Canada**                | Model Code Rule 5.1-2(e)      | Duty to cite directly relevant authorities that have not been cited by opponent | Law society discipline [VERIFY]                                |

**Assessment criteria for adverse authority compliance:**

1. Identify the key legal propositions in the brief
2. For each proposition, determine the controlling authority
3. Check whether any controlling authority supports the opposite conclusion
4. If adverse controlling authority exists and is not cited:
   - And the omission appears deliberate → CRITICAL (ethical violation)
   - And the omission may be inadvertent → VULNERABLE (still must be addressed)
5. Distinguish between "adverse" (goes against the position) and "not helpful"
   (merely doesn't support it) — only directly adverse controlling authority
   triggers the duty

### Duty of Candor Regarding Facts

| Jurisdiction             | Rule                          | Scope                                                                  |
| ------------------------ | ----------------------------- | ---------------------------------------------------------------------- |
| **US (ABA Model Rules)** | Rule 3.3(a)(1)                | Must not make false statements of fact or law to tribunal              |
| **US (ABA Model Rules)** | Rule 3.3(a)(3)                | Must not offer evidence known to be false                              |
| **England & Wales**      | SRA Code of Conduct, para 1.4 | Must not mislead the court                                             |
| **Australia**            | ASCR Rule 19.1                | Must not deceive or knowingly or recklessly mislead the court [VERIFY] |

### Frivolous Arguments

| Jurisdiction              | Rule                                    | Standard                                                                                                |
| ------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **US (FRCP)**             | Rule 11(b)                              | Certification that claims/defenses are warranted by existing law or nonfrivolous argument for extension |
| **US (FRAP)**             | Rule 38                                 | Damages and single or double costs for frivolous appeals                                                |
| **US (28 U.S.C. § 1927)** | Vexatious multiplication of proceedings | Attorney liability for excess costs                                                                     |
| **England & Wales**       | CPR 3.4(2)(a)                           | Court may strike out statement of case disclosing no reasonable grounds [VERIFY]                        |
| **Australia**             | Federal Court Act s 37N                 | Duty to not engage in conduct that would unreasonably obstruct [VERIFY]                                 |

---

## Record Citation Assessment

### US Federal Record Citation Formats

| Record Type           | Expected Format                  | Example               |
| --------------------- | -------------------------------- | --------------------- |
| Joint appendix        | JA [page]                        | JA 145                |
| Record on appeal      | R. [doc].[page] or ROA [page]    | R. 25.3 or ROA 567    |
| Transcript            | Tr. [page]:[line]                | Tr. 145:3-12          |
| Deposition            | [Name] Dep. [page]:[line]        | Smith Dep. 67:14-68:2 |
| Exhibit               | Ex. [number] at [page]           | Ex. 12 at 3           |
| Docket entry          | Dkt. [number]                    | Dkt. 45               |
| Supplemental appendix | SA [page]                        | SA 23                 |
| Sealed record         | [Same format] (filed under seal) | JA 345 (sealed)       |

### Record Citation Quality Checklist

- [ ] Every material factual assertion has a record citation
- [ ] Citations are pinpointed (page and line, not just "the record")
- [ ] Citation format is consistent throughout the brief
- [ ] Citations are accurate (spot-check: do 3-5 citations actually say what the brief claims?)
- [ ] Record citations appear in both the statement of facts AND the argument section
- [ ] Citations distinguish between evidence types (testimony vs. documentary vs. stipulated)
- [ ] For summary judgment briefs: facts stated in form required by local rules
- [ ] For appellate briefs: citations reference appendix/record page numbers, not trial court docket

### Red Flags in Record Citations

| Red Flag                             | Detection Pattern                                                       | Assessment |
| ------------------------------------ | ----------------------------------------------------------------------- | ---------- |
| No record citations                  | Statement of facts lacks any citations                                  | CRITICAL   |
| General citations only               | "See generally the record" or "Tr. passim"                              | VULNERABLE |
| Testimony mischaracterization        | Brief says witness "testified that X" but transcript shows equivocation | CRITICAL   |
| Selective quotation from testimony   | Quotes favorable answer, omits qualifying follow-up                     | VULNERABLE |
| Reliance on counsel statements       | Citing attorney representations rather than evidence                    | VULNERABLE |
| Unsworn material treated as evidence | Citing unverified declarations or letters                               | NEEDS WORK |
| Outdated record references           | Citations to superseded pleading or withdrawn exhibit                   | NEEDS WORK |

---

## Brief Analysis Quick-Start Checklist

For a rapid initial assessment, run through this checklist before detailed
dimension analysis. Each item takes 30-60 seconds to verify.

### Structural Quick Check (2 minutes)

- [ ] All required sections present for this brief type?
- [ ] Table of contents accurate and matches actual headings?
- [ ] Table of authorities complete and matches actual citations?
- [ ] Word/page count within limits?
- [ ] Certificates of compliance and service present?

### Substantive Quick Check (5 minutes)

- [ ] Is the standard of review stated?
- [ ] Does the opening paragraph state the theory of the case?
- [ ] Are point headings argumentative (not just topical)?
- [ ] Does each argument section follow IRAC/CRAC structure?
- [ ] Are there record citations in the statement of facts?
- [ ] Does the conclusion request specific relief?

### Authority Quick Check (3 minutes)

- [ ] Is there at least one binding authority per major proposition?
- [ ] Are parentheticals provided for key citations?
- [ ] Are there any obvious "table stakes" cases missing?
- [ ] Citation format consistent and matches forum convention?
- [ ] Any cases that seem old enough to warrant currency check?

### Writing Quick Check (2 minutes)

- [ ] Are there block quotes longer than 50 words without explanation?
- [ ] Is substantive argument buried in footnotes?
- [ ] Are there excessive nominalizations or passive constructions?
- [ ] Is the brief within a reasonable length for its complexity?
- [ ] Does the brief read as one cohesive document (not stitched together)?

### Red Flag Quick Check (2 minutes)

- [ ] Any factual assertions without record support?
- [ ] Any "clearly" or "obviously" without supporting analysis?
- [ ] Any arguments that seem to apply the wrong standard?
- [ ] Any authority that seems distinguishable without acknowledgment?
- [ ] Any ad hominem or unprofessional tone?

If the quick check reveals 3+ red flags, recommend `deep dive` review depth.

---

## External Tool Integration

### legalcode-mcp (Legal Research)

When available, use legalcode-mcp for:

- Case currency verification (checking subsequent history)
- Adverse authority searches
- Rule/statute currency checks
- Citation format validation

### WebSearch (Live Research)

Use WebSearch for:

- Verifying whether a cited case has been overruled or limited
- Checking current rule text when brief cites a procedural rule
- Finding key cases in an area of law to assess citation completeness
- Verifying court-specific formatting requirements

**Search patterns:**

```
"[case name]" subsequent history OR overruled OR reversed OR vacated
"[rule number]" current text OR amendment OR effective date
[legal issue] [jurisdiction] controlling authority OR leading case
[court name] local rules brief formatting requirements
```

### Task Tool (Sub-Agent Delegation)

Use the Task tool for:

- Parallel analysis of multi-brief sets
- Deep-dive research on specific authority questions
- Comparative analysis between own brief and opposing brief
- Extended writing quality analysis with line-by-line suggestions

---

## Output Format Template

### Brief Analysis Report

```markdown
# Brief Analysis Report

**Brief:** [Title or filename]
**Court:** [Court name]
**Case:** [Case caption, if known]
**Brief Type:** [Opening/Response/Reply/Motion/etc.]
**Side:** [Appellant/Appellee/Movant/etc.]
**Analysis Mode:** [Own-Brief Review / Opposing-Brief Deconstruction]
**Review Depth:** [Quick Scan / Standard / Deep Dive / Competition-Grade]
**Date:** [Analysis date]

---

## Executive Summary

[2-3 paragraph overview: overall assessment, critical findings count,
strongest and weakest dimensions, primary recommendation]

**Overall Classification:** [STRONG / COMPETITIVE / NEEDS WORK / VULNERABLE / DEFICIENT]

| Dimension               | Classification   | Key Finding        |
| ----------------------- | ---------------- | ------------------ |
| Argument Structure      | [classification] | [one-line summary] |
| Standard of Review      | [classification] | [one-line summary] |
| Authority Quality       | [classification] | [one-line summary] |
| Factual Foundation      | [classification] | [one-line summary] |
| Logical Reasoning       | [classification] | [one-line summary] |
| Counter-Arguments       | [classification] | [one-line summary] |
| Writing Quality         | [classification] | [one-line summary] |
| Statement of Facts      | [classification] | [one-line summary] |
| Court-Rules Compliance  | [classification] | [one-line summary] |
| Strategic Effectiveness | [classification] | [one-line summary] |

---

## Tier 1 Findings — Must Fix

[CRITICAL and high-impact VULNERABLE findings, each using the finding template]

---

## Tier 2 Findings — Should Fix

[VULNERABLE and high-impact NEEDS WORK findings]

---

## Tier 3 Findings — Consider Fixing

[NEEDS WORK findings and STRONG observations]

---

## Authority Audit

### Citation Statistics

| Category                   | Count   |
| -------------------------- | ------- |
| Total citations            | [count] |
| Binding authority          | [count] |
| Persuasive authority       | [count] |
| Secondary sources          | [count] |
| Flagged for currency check | [count] |

### Adverse Authority Gaps

[List of potentially missing adverse authorities with explanation]

### Citation Format Issues

[List of format errors by type]

---

## Unsupported Assertions

[List of factual or legal assertions in the brief that lack adequate support,
with location and suggested fix]

---

## Counter-Argument Exposure

[List of counter-arguments the brief fails to address, with assessment of
impact and suggested approach]

---

## Court-Rules Compliance Checklist

| Requirement               | Status | Notes                          |
| ------------------------- | ------ | ------------------------------ |
| Word/page limit           | ✅/❌  | [count vs. limit]              |
| Typeface/margins          | ✅/❌  | [observed vs. required]        |
| Required sections         | ✅/❌  | [missing sections if any]      |
| Table of contents         | ✅/❌  | [accuracy of page numbers]     |
| Table of authorities      | ✅/❌  | [completeness]                 |
| Certificate of compliance | ✅/❌  | [accuracy]                     |
| Certificate of service    | ✅/❌  | [present/absent]               |
| Citation format           | ✅/❌  | [convention used vs. required] |

---

## Recommendations

### Immediate (Before Filing)

[Tier 1 action items in priority order]

### Short-Term (Next Draft Revision)

[Tier 2 improvements in priority order]

### Enhancement (If Time Permits)

[Tier 3 suggestions]

---

## Glass Box Audit Trail

[YAML Glass Box block — see template above]
```

---

## Authority Subsequent History Quick Reference

When flagging authorities for currency check, use these markers:

### Subsequent History Markers

| Marker                    | Meaning                               | Impact on Citation                                       |
| ------------------------- | ------------------------------------- | -------------------------------------------------------- |
| **aff'd**                 | Affirmed by higher court              | Strengthens authority                                    |
| **rev'd**                 | Reversed by higher court              | Authority likely invalid on reversed issue               |
| **vacated**               | Vacated by higher court or same court | Authority has no precedential value                      |
| **overruled**             | Expressly overruled by later case     | Authority is bad law; citing it is CRITICAL error        |
| **overruled in part**     | Partially overruled                   | Check whether overruled portion is the cited proposition |
| **abrogated by statute**  | Legislature changed the rule          | Authority reflects old law; verify statutory change      |
| **distinguished**         | Later case found factual differences  | Authority still valid but may be narrow                  |
| **limited**               | Later case narrowed holding           | Authority valid but scope reduced                        |
| **criticized**            | Later court expressed disagreement    | Authority still valid but weakened; note criticism       |
| **questioned**            | Later court expressed doubt           | Authority still valid but reliability uncertain          |
| **superseded by statute** | Statute replaced common-law rule      | Authority reflects old law                               |
| **cert. denied**          | Supreme Court declined review         | Neutral — denial has no precedential value               |
| **cert. granted**         | Supreme Court accepted review         | Authority may be reversed; flag `[CERT PENDING]`         |

### Currency Check Workflow

1. For each cited authority, determine if the brief provides subsequent history
2. Flag any authority without subsequent history as `[VERIFY CURRENCY]`
3. If WebSearch or legalcode-mcp is available, check key authorities:
   ```
   "[case name]" AND (overruled OR reversed OR vacated OR abrogated)
   ```
4. For authorities critical to the brief's theory, also check:
   ```
   "[case name]" AND (distinguished OR limited OR criticized)
   ```
5. If an authority is flagged with negative treatment, classify the finding
   based on the importance of the authority:
   - Key authority overruled → CRITICAL
   - Key authority limited/distinguished → VULNERABLE
   - Secondary authority with negative treatment → NEEDS WORK
   - Supporting citation criticized → Flag but typically not classified

---

## Common Weaknesses by Brief Type

### Appellate Opening Brief

| Common Weakness                  | Detection Pattern                                            | Frequency               |
| -------------------------------- | ------------------------------------------------------------ | ----------------------- |
| Wrong standard of review         | Brief argues facts de novo when clearly erroneous applies    | Very common             |
| Failure to preserve issue        | Brief raises issue not raised below; no plain error argument | Common                  |
| Insufficient record citations    | Statement of facts lacks pinpoint cites to appendix/record   | Common                  |
| No theory of the case            | Brief is a series of disconnected legal points               | Common                  |
| Argument order wrong             | Weakest argument first; strongest argument buried            | Occasional              |
| Point headings not argumentative | "The Standard of Review" instead of persuasive assertion     | Very common             |
| Application is conclusory        | "Clearly," "obviously" instead of fact-specific analysis     | Very common             |
| Ignoring adverse authority       | Known controlling cases not addressed                        | Occasional but CRITICAL |
| Block quote reliance             | Pages of block quotes with minimal analysis                  | Common                  |
| Summary repeats argument         | Summary of argument merely repeats rather than previewing    | Common                  |

### Appellate Response/Answering Brief

| Common Weakness                   | Detection Pattern                                               | Frequency               |
| --------------------------------- | --------------------------------------------------------------- | ----------------------- |
| Failure to address all issues     | Response skips appellant's arguments entirely                   | Occasional but CRITICAL |
| Defensive posture only            | Fails to affirmatively argue strengths of lower court ruling    | Common                  |
| Adopting appellant's framing      | Uses appellant's issue formulations instead of reframing        | Common                  |
| No independent statement of facts | Relies on appellant's facts instead of presenting own narrative | Common                  |
| Waiver arguments over-emphasized  | Spends pages on waiver when merits response is stronger         | Occasional              |
| Standard of review not leveraged  | Fails to emphasize deferential standard as a strength           | Common                  |

### Reply Brief

| Common Weakness                       | Detection Pattern                                                   | Frequency               |
| ------------------------------------- | ------------------------------------------------------------------- | ----------------------- |
| Raising new issues                    | Arguments not responsive to answering brief                         | Occasional but CRITICAL |
| Mere repetition                       | Restates opening brief without addressing response                  | Common                  |
| Ignoring concessions made by appellee | Fails to highlight appellee's concessions                           | Common                  |
| New evidence or authority             | Introduces material not in opening brief                            | Occasional              |
| Tone becomes combative                | Frustration with opposing position leads to unprofessional language | Occasional              |
| Fails to identify points of agreement | Misses opportunity to narrow issues                                 | Common                  |

### Motion Brief (Summary Judgment, Dismissal, etc.)

| Common Weakness                            | Detection Pattern                                                 | Frequency  |
| ------------------------------------------ | ----------------------------------------------------------------- | ---------- |
| Statement of undisputed facts insufficient | For MSJ: facts not stated as numbered paragraphs with citations   | Common     |
| Wrong legal standard                       | Confusion between 12(b)(6) and 56 standards                       | Occasional |
| Viewing facts in wrong light               | Movant fails to view facts in non-movant's favor                  | Common     |
| "Genuine dispute" not addressed            | Moving party does not explain why no genuine dispute exists       | Common     |
| Failing to meet Local Rule 56 requirements | Missing separate statement of facts, response to opponent's facts | Common     |

### Skeleton Argument (England & Wales)

| Common Weakness                    | Detection Pattern                                          | Frequency       |
| ---------------------------------- | ---------------------------------------------------------- | --------------- |
| Too long                           | Exceeds page guidance in PD 52A                            | Common [VERIFY] |
| No propositions of law stated      | Discussion without clear propositions to be argued         | Occasional      |
| Chronology missing or incomplete   | No standalone or integrated chronology                     | Common          |
| Time estimate unrealistic          | Time estimate does not match complexity of issues          | Occasional      |
| Bundle references missing          | No cross-references to the hearing bundle                  | Common          |
| Authorities not properly presented | Failure to use neutral citations or highlight key passages | Occasional      |

---

## Exploitation Priority Matrix (Opposing Mode)

When deconstructing an opposing brief, rank each identified weakness using
this impact × exploitability matrix:

### Impact Assessment

| Level           | Definition                             | Examples                                                                                                    |
| --------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Dispositive** | If exploited, could win the case       | Wrong standard of review on central issue; controlling adverse authority not cited; key fact misrepresented |
| **Significant** | Materially strengthens response        | Logical gap in core argument; weak authority for key proposition; factual overstatement                     |
| **Moderate**    | Worthwhile to exploit if space permits | Secondary argument weakness; formatting non-compliance; minor authority issue                               |
| **Minor**       | Cosmetic or unlikely to affect outcome | Citation format errors; writing quality issues; minor organizational problems                               |

### Exploitability Assessment

| Level         | Definition                                          | Examples                                                                                                              |
| ------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Easy**      | Can be demonstrated clearly and concisely           | Case clearly overruled; quote demonstrably taken out of context; record citation does not support claim               |
| **Moderate**  | Requires some development but straightforward       | Authority distinguishable on specific facts; logical gap identifiable with analysis; omitted adverse authority exists |
| **Difficult** | Requires extensive development or uncertain outcome | Arguable mischaracterization; debatable logical flaw; authority currency uncertain                                    |

### Priority Matrix

|                        | Easy to Exploit               | Moderate to Exploit              | Difficult to Exploit                      |
| ---------------------- | ----------------------------- | -------------------------------- | ----------------------------------------- |
| **Dispositive Impact** | Priority 1 — Lead with this   | Priority 1 — Invest the space    | Priority 2 — Develop if page count allows |
| **Significant Impact** | Priority 1 — Quick win        | Priority 2 — Develop in argument | Priority 3 — Consider mentioning          |
| **Moderate Impact**    | Priority 2 — Include          | Priority 3 — Consider            | Priority 4 — Skip unless pattern          |
| **Minor Impact**       | Priority 3 — Footnote at best | Priority 4 — Skip                | Priority 4 — Skip                         |

---

## Concession Detection Patterns

When analyzing an opposing brief, look for these concession patterns:

### Explicit Concessions

- "Plaintiff does not dispute that..."
- "Even assuming arguendo that..."
- "Setting aside the question of..."
- "Regardless of whether..."
- "While Defendant concedes that..."

### Implicit Concessions (Arguments Not Made)

- Issues raised in the lower court but dropped on appeal → waived/conceded
- Standard boilerplate arguments conspicuously absent
- Failure to challenge specific factual findings → accepted
- Failure to address a ground for the lower court's ruling → conceded [VERIFY: whether this is jurisdictional]

### Scope-Limiting Language

- "In this particular case..." (concedes the general rule doesn't help)
- "The narrow question here..." (concedes broader point)
- "On these specific facts..." (concedes the rule may cut differently on other facts)
- "At this stage of the proceedings..." (concedes the argument may fail later)

### Abandoned Positions

- Compare opening brief issues with reply brief — any dropped issues?
- Compare lower court briefing with appellate briefing — any dropped arguments?
- Compare motion to dismiss brief with summary judgment brief — evolved positions?

---

## Localization Notes

When adapting this skill for a specific jurisdiction, update these elements:

### US Federal Localization

- Court-rules checklist: Use FRAP 28-32 requirements
- Citation format: Bluebook (21st ed.)
- Standard of review: De novo / clearly erroneous / abuse of discretion
- Authority hierarchy: SCOTUS → circuit → district (within circuit) → other circuits (persuasive)
- Ethical obligations: ABA Model Rule 3.3(a)(2)
- Record references: Joint appendix citations (JA XX)

### England & Wales Localization

- Court-rules checklist: CPR Part 52, PD 52A for skeleton arguments
- Citation format: OSCOLA (4th ed.)
- Standard of review: Appeal allowed only if wrong in law, unjust due to serious procedural irregularity
- Authority hierarchy: UKSC → Court of Appeal → High Court → Crown Court
- Ethical obligations: SRA Code of Conduct, para 1.4
- Statement of facts: Chronology and dramatis personae format
- Key difference: Skeleton arguments are much shorter (typically 20-25 pages) [VERIFY]

### Australia Localization

- Court-rules checklist: Federal Court Rules 2011, relevant practice notes
- Citation format: AGLG (4th ed.)
- Standard of review: House v The King (1936) 55 CLR 499 for discretionary decisions [VERIFY]
- Authority hierarchy: HCA → Full Federal Court → single judge Federal Court → state courts
- Ethical obligations: Australian Solicitors' Conduct Rules, Rule 19 [VERIFY]
- Statement of facts: "Outline of submissions" format
- Key difference: Emphasis on conciseness; submissions typically 20-30 pages [VERIFY]

### Canada Localization

- Court-rules checklist: Federal Courts Rules SOR/98-106 or provincial rules
- Citation format: McGill Guide (10th ed.)
- Standard of review: _Canada (Minister of Citizenship and Immigration) v. Vavilov_ (2019 SCC 65) framework — correctness vs. reasonableness [VERIFY]
- Authority hierarchy: SCC → provincial appellate → provincial trial → federal courts
- Ethical obligations: Federation of Law Societies Model Code of Professional Conduct, Rule 5.1-2(e) [VERIFY]
- Bilingual considerations: Brief may need to address law in both English and French
- Key difference: Factums (briefs) have strict formatting requirements varying by province; SCC limits factums to 40 pages [VERIFY]

### Localization Checklist

When localizing this skill for a specific jurisdiction, verify the following:

- [ ] **Court-rules section**: All formatting rules reference the correct jurisdiction's rules
- [ ] **Citation format**: Citation convention matches the forum's requirement
- [ ] **Standard of review**: Nomenclature and tests match the jurisdiction
- [ ] **Authority hierarchy**: Binding/persuasive distinctions reflect the court structure
- [ ] **Ethical rules**: Adverse authority duty references the correct professional conduct rule
- [ ] **Record citation format**: Record reference format matches local convention
- [ ] **CLARIFY blocks**: Options in CLARIFY blocks include jurisdiction-appropriate brief types
- [ ] **Anti-patterns**: Jurisdiction-specific anti-patterns added (e.g., UK footnote conventions differ from US)
- [ ] **Scoring rubric weights**: Adjust weights if jurisdiction values different dimensions differently (e.g., UK values conciseness more heavily)
- [ ] **Common weaknesses**: Brief-type tables include jurisdiction-specific brief types
- [ ] **Output template**: Compliance checklist reflects jurisdiction requirements
- [ ] **[VERIFY] markers**: All jurisdiction-specific rule references verified against current versions
- [ ] **[JURISDICTION-SPECIFIC] markers**: All markers replaced with hardcoded jurisdiction-specific content

---

## Reply Brief and Surreply Analysis

### Reply Brief — Special Rules

Reply briefs have unique constraints that affect analysis:

1. **No new issues**: A reply brief may only respond to arguments raised in the
   answering/response brief. New issues raised for the first time in a reply
   brief are waived or will be stricken. Flag any argument in a reply brief that
   does not respond to a specific point in the answering brief.

2. **No new evidence**: Generally, new evidence or authority not cited in the
   opening brief cannot be introduced in a reply brief without leave of court.
   Exceptions: authority issued after the opening brief was filed; rebuttal of
   new arguments raised by respondent. [VERIFY per jurisdiction]

3. **Shorter word limit**: Reply briefs typically have half the word limit of
   principal briefs (FRAP 32(a)(7): 6,500 words for replies vs. 13,000 for
   principal briefs). Assess whether the reply efficiently uses its limited space.

4. **Concession harvesting**: The most effective reply briefs begin by
   cataloguing what the opposing brief concedes (explicitly or by silence),
   narrowing the issues still in dispute. Check whether the reply does this.

5. **Point-by-point vs. thematic**: Some reply briefs respond point-by-point
   to the answering brief; others reorganize thematically. Either approach is
   valid. Assess whether the chosen approach effectively addresses all arguments.

### Reply Brief Assessment Criteria

| Criterion     | STRONG                                                                  | VULNERABLE                                                 |
| ------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| Scope         | Responds only to arguments in answering brief                           | Raises new issues not in opening brief                     |
| Opening       | Identifies concessions and narrows issues                               | Restates opening brief arguments                           |
| Coverage      | Addresses all material opposing arguments                               | Skips significant arguments (conceding by silence?)        |
| Efficiency    | Uses limited space on highest-impact responses                          | Wastes space on minor points or repetition                 |
| Tone          | Professional, focused, responsive                                       | Defensive, combative, or dismissive                        |
| New authority | Only authority issued after opening or directly rebutting new arguments | Introduces significant new authority without justification |

### Surreply / Further Submissions

Surreplies are generally disfavored and require leave of court. If analyzing
a surreply:

- **Threshold question**: Was the surreply properly authorized? If not, flag.
- **New matter test**: Does the surreply only address genuinely new arguments
  raised for the first time in the reply? Or does it merely re-argue points
  already briefed?
- **Necessity**: Would the court benefit from this additional briefing, or does
  it merely prolong the dispute?

---

## Provenance

This skill was created as a Legalcode original synthesis using multi-agent
research methodology.

**Research methodology:**

- 6 parallel research agents (Opus) conducted domain-specific web research
- Research domains: legal writing structure, court rules, reasoning patterns, authority assessment, scoring frameworks, opposing analysis
- Findings synthesized into unified skill by orchestrator agent

**Key reference frameworks:**

- IRAC/CRAC/CREAC argument structure (standard legal writing pedagogy)
- Bryan Garner, _The Winning Brief_ (legal writing best practices) [VERIFY]
- Scalia & Garner, _Making Your Case_ (appellate advocacy) [VERIFY]
- Major moot court competition rubrics (ABA, Jessup, Vis) [VERIFY]
- FRAP Rules 28-32 (US federal appellate brief requirements) [VERIFY]
- CPR Part 52 / PD 52A (England & Wales appellate practice) [VERIFY]
- Federal Court Rules 2011 (Australia) [VERIFY]
- ABA Model Rule 3.3(a)(2) (duty to cite adverse authority) [VERIFY]
- _Loper Bright Enterprises v. Raimondo_ (2024) — post-Chevron deference [VERIFY]

**Research artifacts:**

- Research findings from 6 parallel agents available in team workspace
- Web search results cached for verification

**Skill version:** 1.0
**Created:** 2026-02-28
**Created by:** Legalcode multi-agent research pipeline
