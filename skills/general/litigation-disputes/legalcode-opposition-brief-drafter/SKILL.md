---
name: legalcode-opposition-brief-drafter
description: Draft opposition briefs and responsive memoranda by systematically analyzing the movant's
  arguments, identifying legal and factual weaknesses, marshaling contrary evidence, and constructing
  counter-arguments. Use when opposing motions to dismiss (Rule 12(b)), summary judgment (Rule 56), motions
  in limine, preliminary injunctions, or other dispositive and non-dispositive motions. Covers argument
  deconstruction, genuine dispute identification, evidentiary marshaling, authority counter-research,
  burden analysis, and persuasive brief drafting. Supports US federal (FRCP), England & Wales (CPR), and
  Australia (Federal Court Rules) with jurisdiction-agnostic baseline and [JURISDICTION-SPECIFIC] markers.
  Produces court-ready opposition briefs with IRAC/CRAC structure, point headings, authority citations,
  and Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Opposition Brief Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted opposition brief
> drafting. It does not constitute legal advice. All outputs must be reviewed, verified,
> and signed by qualified legal counsel licensed in the relevant jurisdiction before
> filing with any court. Procedural rules, briefing standards, and case law change
> frequently; verify all authoritative sources before relying on any conclusion.
> AI-generated briefs may contain errors in legal analysis, factual characterization,
> or citation accuracy — all arguments must be verified against actual evidence and
> case law. Any cited authority marked `[VERIFY]` has not been independently validated
> and must be confirmed before reliance. Filing a brief constitutes professional
> certification that the arguments are well-grounded in fact and law.

---

## Purpose and Scope

This skill drafts opposition briefs and responsive memoranda by systematically analyzing
the movant's brief, identifying weaknesses in their arguments, marshaling contrary facts
and law, and constructing persuasive counter-arguments. The skill applies established
legal writing frameworks (IRAC, CRAC, CREAC), standards for burden allocation, and
effective advocacy strategies to produce court-ready responsive briefs.

The skill operates in three primary modes:

1. **Full Draft Mode**: Generates a complete opposition brief from the movant's brief,
   record materials, and legal research — including introduction, statement of issues,
   statement of facts, argument sections with point headings, and conclusion.

2. **Argument Development Mode**: Develops specific counter-arguments in response to
   identified arguments from the movant's brief, producing IRAC-structured responses
   with authority and evidentiary support.

3. **Strategy Analysis Mode**: Analyzes the movant's brief to identify exploitable
   weaknesses, concessions, and gaps without producing full drafted content — used
   for early opposition planning.

**Covers:**

- **Argument deconstruction**: Breaking down movant's arguments to identify logical gaps, unsupported assertions, and authority weaknesses
- **Genuine dispute identification**: Finding material fact disputes that preclude summary judgment
- **Evidentiary marshaling**: Organizing record evidence to support counter-arguments and create genuine issues
- **Authority counter-research**: Identifying distinguishing cases, negative treatment of cited authority, and favorable precedent
- **Burden analysis**: Applying correct burden allocation for the motion type and procedural posture
- **Standard of review exploitation**: Framing arguments to maximize favorable standard application
- **Procedural objections**: Identifying timeliness, waiver, and procedural defects in the movant's filing
- **Persuasive drafting**: IRAC/CRAC structure, argumentative point headings, effective fact presentation
- **Reply anticipation**: Addressing likely reply arguments proactively where strategically advantageous
- **Cross-jurisdictional**: US federal (FRCP), US state courts, England & Wales (CPR), Australia (Federal Court)

**Does not:**

- Replace counsel's professional judgment on advocacy strategy or case theory
- Certify compliance with Rule 11 or professional conduct rules (only counsel may sign)
- Conduct independent factual investigation beyond provided materials
- Provide final legal opinions on case merits
- File documents with any court
- Make ultimate determinations on evidentiary admissibility
- Guarantee outcomes or predict judicial decisions

**Related skills:**

- `legalcode-brief-analyzer` — Analyzes briefs for argument strength and authority quality
- `legalcode-summary-judgment-analysis` — Summary judgment motion evaluation
- `legalcode-discovery-request-drafter` — Discovery for evidence gathering
- `legalcode-early-case-assessment` — Pre-motion case evaluation
- `legalcode-case-timeline-builder` — Builds chronologies from document corpora
- `legalcode-evidence-admissibility-analysis` — Evidentiary assessment

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the forum, governing procedural
rules, and applicable substantive law first, then adapt opposition format, burden
allocation, and authority requirements accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Briefing page/word limits and formatting requirements
- Response deadlines and extension procedures
- Local rules for responsive briefs (e.g., separate statement requirements)
- Standard of review nomenclature and application
- Burden allocation for the specific motion type
- Citation format convention (Bluebook, OSCOLA, AGLC)
- Authority hierarchy and binding precedent scope
- Counter-statement of facts requirements
- Surreply rules and procedures

**Reference anchors frequently needed:**

### US Federal (FRCP)

**Motion to Dismiss (Rule 12(b)):**

- **Standard**: Court accepts all well-pleaded factual allegations as true and draws
  reasonable inferences in plaintiff's favor. Ashcroft v. Iqbal, 556 U.S. 662 (2009);
  Bell Atl. Corp. v. Twombly, 550 U.S. 544 (2007) [VERIFY]
- **Burden**: Plaintiff must plead facts plausibly suggesting entitlement to relief;
  conclusory allegations and legal conclusions not accepted as true [VERIFY]
- **Key opposition strategy**: Emphasize factual plausibility, distinguish authority,
  show inference is reasonable

**Summary Judgment (Rule 56):**

- **Standard**: "The court shall grant summary judgment if the movant shows that there
  is no genuine dispute as to any material fact and the movant is entitled to judgment
  as a matter of law." FRCP 56(a) [VERIFY]
- **Burden (movant-defendant)**: Movant must point to absence of evidence in record
  supporting plaintiff's claim. Celotex Corp. v. Catrett, 477 U.S. 317 (1986) [VERIFY]
- **Burden (non-movant)**: Must "set out specific facts showing a genuine issue for
  trial." Cannot rely on mere pleadings. Anderson v. Liberty Lobby, Inc., 477 U.S. 242
  (1986) [VERIFY]
- **Viewing standard**: Evidence viewed "in the light most favorable to the non-moving
  party." [VERIFY]
- **Key opposition strategy**: Identify genuine disputes, cite admissible evidence,
  show reasonable jury could find for non-movant

**Preliminary Injunction (Rule 65):**

- **Standard**: Four-factor test: (1) likelihood of success on merits, (2) irreparable
  harm, (3) balance of hardships, (4) public interest. Winter v. NRDC, 555 U.S. 7 (2008)
  [VERIFY]
- **Key opposition strategy**: Attack weakest factor, show adequate legal remedies exist,
  emphasize harm to defendant from injunction

**Motion in Limine:**

- **Standard**: Federal Rules of Evidence 402, 403; expert testimony under Daubert v.
  Merrell Dow Pharms., 509 U.S. 579 (1993) [VERIFY]
- **Key opposition strategy**: Show relevance, demonstrate probative value outweighs
  prejudice, address authentication and foundation

### England & Wales (CPR)

**Application to Strike Out (CPR 3.4):**

- **Standard**: Court may strike if statement of case discloses no reasonable grounds,
  is an abuse of process, or fails to comply with rules. CPR 3.4(2) [VERIFY]
- **Key opposition strategy**: Show arguable case exists, distinguish authority

**Summary Judgment (CPR Part 24):**

- **Standard**: Court may give summary judgment if "no real prospect of succeeding"
  and "no other compelling reason" for trial. CPR 24.2 [VERIFY]
- **"Real prospect"**: More than fanciful but need not be probable. Swain v. Hillman
  [2001] 1 All ER 91 [VERIFY]
- **Key opposition strategy**: Show real prospect exists, identify compelling reasons
  for trial, request further disclosure if needed

**Interim Injunctions:**

- **Standard**: American Cyanamid guidelines — serious question to be tried, balance
  of convenience, adequacy of damages. American Cyanamid Co v Ethicon Ltd [1975] AC 396
  [VERIFY]
- **Key opposition strategy**: Show damages adequate remedy, balance favors defendant

### Australia (Federal Court)

**Summary Judgment (s 31A Federal Court Act):**

- **Standard**: "No reasonable prospect of successfully prosecuting or defending."
  Lower threshold than General Steel "certain or concluded" test. [VERIFY]
- **Key opposition strategy**: Show reasonable prospect exists, identify triable issues

---

## Interactive Clarification

Use interactive clarification whenever the answer materially changes drafting approach,
argument selection, or strategic emphasis. If information is already provided, skip the
question. Proceed with stated defaults when the user does not respond.

**CLARIFY block 1: Drafting mode**

- Options: `full draft (complete opposition brief)`, `argument development (specific counter-arguments)`, `strategy analysis (identify weaknesses, no full draft)`
- Default: `full draft (complete opposition brief)`
- Why it matters: Full draft produces court-ready brief; argument development focuses on specific issues; strategy analysis is for early planning.

**CLARIFY block 2: Motion type being opposed**

- Options: `motion to dismiss (12(b)(6) or equivalent)`, `motion to dismiss (12(b)(1) jurisdiction)`, `motion to dismiss (12(b)(2) personal jurisdiction)`, `summary judgment (movant is defendant)`, `summary judgment (movant is plaintiff)`, `preliminary injunction`, `motion in limine`, `motion to compel`, `motion for sanctions`, `other (specify)`
- Default: `summary judgment (movant is defendant)`
- Why it matters: Different motions have different burdens, standards, and opposition strategies.

**CLARIFY block 3: Your client's role**

- Options: `plaintiff/claimant opposing defendant's motion`, `defendant opposing plaintiff's motion`, `cross-claimant/counter-claimant`, `third-party defendant`, `intervenor`
- Default: `plaintiff/claimant opposing defendant's motion`
- Why it matters: Determines burden allocation, procedural posture, and argument framing.

**CLARIFY block 4: Court and jurisdiction**

- Options: `US federal district court (specify)`, `US federal circuit (for appeals)`, `US state court (specify)`, `England & Wales High Court`, `England & Wales County Court`, `Australia Federal Court`, `Australia state court (specify)`, `other (specify)`
- Default: `US federal district court`
- Why it matters: Determines applicable rules, briefing limits, formatting, local requirements.

**CLARIFY block 5: Available materials**

- Options: `movant's brief only`, `movant's brief + exhibits`, `movant's brief + my prior filings`, `movant's brief + full record`, `movant's brief + full record + prior briefing`, `preliminary (no brief yet, anticipating motion)`
- Default: `movant's brief + exhibits`
- Why it matters: More materials enable better counter-argument development and evidentiary marshaling.

**CLARIFY block 6: Claims/defenses at issue**

- Prompt: "Which claims or defenses does the motion target?"
- Default: `all claims/defenses`
- Why it matters: Allows focused opposition on specific issues; some claims may be abandoned or not worth defending.

**CLARIFY block 7: Strategic priority**

- Options: `survive the motion (minimum necessary)`, `aggressive defense (attack every weakness)`, `position for appeal (preserve all arguments)`, `encourage settlement (show strength for negotiation)`, `preserve discovery rights (defeat premature disposition)`
- Default: `survive the motion (minimum necessary)`
- Why it matters: Affects argument selection, emphasis, and briefing strategy.

**CLARIFY block 8: Known strengths and weaknesses**

- Prompt: "Are there specific strengths in your position or weaknesses in movant's arguments you want to emphasize? Any arguments you want to avoid?"
- Default: `I will identify from analysis`
- Why it matters: Client knowledge of case may reveal strategic considerations not apparent from briefs.

---

## Workflow

### Step 1: Accept input materials

Accept materials in any of these formats:

- **File path(s)**: Read documents directly (PDF, DOCX, TXT, MD)
- **Pasted text**: Accept inline brief text
- **URL**: Fetch from PACER, court website, or document management system
- **Multiple files**: For full briefing sets, accept paths to all documents

If documents are PDFs, convert:

```bash
# Attempt pandoc first, fall back to pdftotext
pandoc "$FILE" -t markdown -o "${FILE%.pdf}.md" 2>/dev/null || pdftotext "$FILE" "${FILE%.pdf}.txt"
```

Identify and categorize each document:

- Movant's motion / brief / memorandum
- Movant's statement of facts (if separate)
- Movant's exhibits / declarations / evidence
- Complaint / Answer / operative pleading
- Prior court orders
- Relevant discovery materials
- Prior briefing in the case

### Step 2: Gather context via interactive clarification

Run through CLARIFY blocks 1-8, skipping any already answered by the initial prompt.
Record all responses (and defaults used) in the Glass Box audit trail.

### Step 3: Deconstruct movant's arguments

Systematically break down the movant's brief to identify every argument and its support:

**3a. Argument inventory:**

| #   | Argument    | Supporting Authority | Supporting Facts | Strength     | Vulnerability |
| --- | ----------- | -------------------- | ---------------- | ------------ | ------------- |
| 1   | [statement] | [cases/statutes]     | [record cites]   | HIGH/MED/LOW | [weakness]    |

**3b. Logical structure analysis:**

For each argument, assess:

- Is the rule stated correctly and completely?
- Does the application connect facts to rule elements?
- Are there gaps between rule and conclusion?
- Does authority actually support the proposition?
- Are there hidden assumptions or unstated premises?

**3c. Identify concessions and admissions:**

- What facts does the movant concede (explicitly or implicitly)?
- What legal standards does the movant accept?
- Where does the movant's argument implicitly strengthen your position?
- What arguments does the movant NOT make (and why)?

**3d. Flag factual mischaracterizations:**

| Movant's Characterization | Actual Record       | Citation | Impact       |
| ------------------------- | ------------------- | -------- | ------------ |
| [what movant says]        | [what record shows] | [cite]   | HIGH/MED/LOW |

### Step 4: Authority counter-research

Research the legal landscape to build your opposition arguments:

**4a. Analyze movant's cited authority:**

| Case/Statute | Movant's Use         | Distinguishing Factors       | Negative Treatment   | Counter-Use                 |
| ------------ | -------------------- | ---------------------------- | -------------------- | --------------------------- |
| [citation]   | [how movant uses it] | [factual/legal distinctions] | [subsequent history] | [how to use against movant] |

**4b. Search for favorable authority:**

Use **legalcode-mcp** or WebSearch to find:

- Cases with similar facts that reached different conclusions
- Cases limiting or criticizing movant's cited authority
- Authority establishing standards favorable to your client
- Recent developments in the area of law
- Secondary sources supporting your position

**4c. Build authority reference file:**

Save the most relevant results into a local temporary reference file:

```markdown
# Opposition Authority Reference — [Case Name]

## Motion Type: [type]

## Date: [date]

### Favorable Precedent

- [Case, citation, key holding, why favorable]

### Distinguishing Movant's Cases

- [Movant's case, factual distinction, legal distinction, counter-argument]

### Standard of Review Authority

- [Case, standard articulated, application]

### Burden Allocation

- [Authority establishing burden on movant or supporting non-movant position]
```

**If legalcode-mcp is not connected:**

- Mark all legal authority with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with provided materials and general legal knowledge

### Step 5: Identify genuine disputes of material fact (Summary Judgment)

For summary judgment oppositions, this is the most critical step:

**5a. Element-by-element fact mapping:**

| Claim Element | Movant's Position    | Record Evidence (Non-movant) | Dispute?               | Materiality  |
| ------------- | -------------------- | ---------------------------- | ---------------------- | ------------ |
| [element]     | [movant's assertion] | [cite to record]             | GENUINE/COLORABLE/NONE | HIGH/MED/LOW |

**5b. Genuine dispute criteria:**

A dispute is GENUINE if:

- There is competent, admissible evidence supporting the non-movant's version
- A reasonable jury could credit the non-movant's evidence
- The dispute is not merely "metaphysical doubt" or "scintilla"

A dispute is MATERIAL if:

- The fact affects an essential element of a claim or defense
- Resolution of the fact could change the outcome under governing law

**5c. Evidence marshaling:**

For each genuine dispute:

| Disputed Fact | Movant's Evidence | Non-movant's Evidence | Resolution Requires Credibility Assessment? |
| ------------- | ----------------- | --------------------- | ------------------------------------------- |
| [fact]        | [cite]            | [cite]                | YES/NO                                      |

**5d. Inference arguments:**

Summary judgment requires viewing evidence in the non-movant's favor. Identify all
reasonable inferences that favor your client:

| Evidence | Inference Favorable to Non-movant | Why Reasonable |
| -------- | --------------------------------- | -------------- |
| [cite]   | [inference]                       | [reasoning]    |

### Step 6: Develop counter-arguments

For each movant argument identified in Step 3, develop a counter-argument:

**6a. Counter-argument structure (IRAC/CRAC):**

For each response:

1. **Issue**: Frame the issue favorably to non-movant
2. **Rule**: State the legal standard correctly (with authority)
3. **Application**: Apply rule to facts, citing record evidence
4. **Conclusion**: State why movant's argument fails

**6b. Counter-argument types:**

| Type                         | When to Use                       | Example                                                  |
| ---------------------------- | --------------------------------- | -------------------------------------------------------- |
| **Direct refutation**        | Movant's argument is simply wrong | "The statute does not apply because..."                  |
| **Factual contradiction**    | Record contradicts movant's facts | "Movant claims X, but the record shows Y"                |
| **Authority distinction**    | Movant's cases are inapplicable   | "Unlike [case], here the defendant..."                   |
| **Burden failure**           | Movant has not met threshold      | "Movant failed to address [element]"                     |
| **Procedural objection**     | Motion is improper                | "This argument was waived by..."                         |
| **Alternative theory**       | Different legal framework applies | "Even if [movant's theory], plaintiff prevails under..." |
| **Genuine dispute creation** | Facts are contested               | "The parties dispute [fact], requiring trial"            |

**6c. Argument prioritization:**

| Priority      | Criteria                                        | Treatment                            |
| ------------- | ----------------------------------------------- | ------------------------------------ |
| **Primary**   | Strongest arguments; likely to be dispositive   | Lead with these; fullest development |
| **Secondary** | Strong supporting arguments                     | Include but with less space          |
| **Tertiary**  | Arguments to preserve for appeal                | Raise but need not fully develop     |
| **Omit**      | Weak arguments that could undermine credibility | Do not include                       |

### Step 7: Draft the opposition brief

Produce a court-ready opposition brief following proper structure and format:

**7a. Brief architecture:**

**US Federal District Court format:**

1. Caption and case number
2. Title (e.g., "Plaintiff's Opposition to Defendant's Motion for Summary Judgment")
3. Table of Contents (for longer briefs)
4. Table of Authorities (for longer briefs)
5. Introduction / Preliminary Statement (1-2 pages)
6. Statement of Issues (if required by local rule)
7. Statement of Facts / Counter-Statement of Facts
8. Legal Standard
9. Argument (with point headings)
10. Conclusion
11. Signature block
12. Certificate of Service

**England & Wales Skeleton Argument format:**

1. Title and court reference
2. Introduction (1-2 paragraphs)
3. Chronology reference
4. Summary of issues
5. Submissions on each issue (with propositions of law)
6. Conclusion with time estimate

**7b. Key drafting principles:**

**Introduction (must accomplish):**

- State what the motion is and why it should be denied
- Identify the fatal flaw in movant's position (one sentence)
- Frame the case theory favorably
- Preview the strongest arguments

**Statement of Facts (must accomplish):**

- Present facts in narrative form favorable to non-movant
- Cite to record for every material fact
- Include facts movant omitted that hurt their position
- Avoid argument (save for argument section)
- Use present tense for timeless facts, past for events

**Argument section (must accomplish):**

- Use argumentative point headings (not neutral topic headings)
- Lead with strongest arguments
- Apply IRAC/CRAC for each issue
- Cite authority for every legal proposition
- Connect law to specific facts of this case
- Distinguish movant's authority rather than ignoring it
- Address movant's best arguments directly
- Use short paragraphs and clear transitions

**Conclusion (must accomplish):**

- State specific relief requested
- May briefly summarize why motion fails
- Never introduce new arguments

**7c. Point heading examples:**

| Weak (Topic Heading)       | Strong (Argumentative)                                                            |
| -------------------------- | --------------------------------------------------------------------------------- |
| "Standard of Review"       | "Summary Judgment Is Inappropriate Where, As Here, Material Facts Are Disputed"   |
| "Breach of Contract Claim" | "Defendant's Admitted Failure to Deliver Conforming Goods Establishes Breach"     |
| "Personal Jurisdiction"    | "Defendant's Purposeful Contacts With This Forum Establish Specific Jurisdiction" |

### Step 8: Procedural compliance check

Verify the opposition brief complies with all applicable rules:

**8a. Filing deadline:**

| Jurisdiction     | Default Deadline                   | Extension Procedure             |
| ---------------- | ---------------------------------- | ------------------------------- |
| US Federal (SJ)  | 21 days after service (FRCP 56(b)) | Motion under FRCP 6(b) [VERIFY] |
| US Federal (MTD) | Per scheduling order or 21 days    | Motion under FRCP 6(b) [VERIFY] |
| England & Wales  | Per court directions               | Application to court            |
| Local rules      | [Check local rule]                 | [Check local rule]              |

**8b. Formatting requirements:**

| Requirement               | US Federal                                           | Check     |
| ------------------------- | ---------------------------------------------------- | --------- |
| Page/word limit           | 25 pages or 7,000 words (opposition to SJ)           | [count]   |
| Font                      | 14-point for proportional; 12-point for monospaced   | [verify]  |
| Margins                   | 1 inch all sides                                     | [verify]  |
| Line spacing              | Double-spaced (except headings/footnotes/quotations) | [verify]  |
| Certificate of compliance | Required for word-count briefs                       | [include] |

[JURISDICTION-SPECIFIC] Check local rules for additional requirements (e.g., NDCA
requires separate Rule 56 counter-statement; SDNY requires Rule 56.1 counter-statement).

**8c. Service requirements:**

- CM/ECF filing and service (US federal)
- Certificate of service included
- All parties served

### Step 9: Quality verification

Before finalizing, verify the opposition brief against quality standards:

**9a. Completeness check:**

| Element                                    | Present | Quality |
| ------------------------------------------ | ------- | ------- |
| Every movant argument addressed            | ☐       | —       |
| Legal standard correctly stated            | ☐       | —       |
| Authority cited for all legal propositions | ☐       | —       |
| Record cited for all factual assertions    | ☐       | —       |
| Genuine disputes identified with evidence  | ☐       | —       |
| Point headings are argumentative           | ☐       | —       |
| Introduction frames case favorably         | ☐       | —       |
| Conclusion states specific relief          | ☐       | —       |
| Format complies with rules                 | ☐       | —       |

**9b. Citation quality gates:**

Run these gates before delivery:

| Gate          | Rule                                                   | Fail Action                   |
| ------------- | ------------------------------------------------------ | ----------------------------- |
| **Authority** | Every legal proposition cites authority                | Add citation or mark [VERIFY] |
| **Currency**  | Cases checked for overruling/negative treatment        | Flag [CHECK CURRENCY]         |
| **Pinpoint**  | Record citations pinpointed (page:line)                | Add pinpoint or flag          |
| **Format**    | Citations follow correct format (Bluebook/OSCOLA/AGLC) | Fix format                    |
| **Support**   | Cited authority actually supports proposition stated   | Verify or remove              |

**9c. Self-interrogation for key arguments:**

For each primary argument, apply 3-pass adversarial review:

**Pass 1 — Logical integrity**: Does this argument follow logically from the cited
authority and facts? Would a neutral reader find it persuasive?

**Pass 2 — Anticipate reply**: How will movant respond to this argument? Have I
addressed their likely counter?

**Pass 3 — Challenge**: What is the weakest part of this argument? Should I
strengthen it or reframe it?

### Step 10: Deliver opposition brief

Compile all components into the final opposition brief. Generate the Glass Box audit
trail. Present the brief with:

1. Complete formatted opposition brief
2. Summary of key arguments and their classification
3. List of evidence/authority relied upon
4. Procedural compliance certification
5. Glass Box audit trail

---

## Severity Classification

Classification system for arguments and findings:

### Argument Strength (Your Opposition)

| Level         | Criteria                                                                         | Usage                                          |
| ------------- | -------------------------------------------------------------------------------- | ---------------------------------------------- |
| **STRONG**    | Well-supported by binding authority, clear record evidence, logically compelling | Lead arguments; request denial based on these  |
| **SOLID**     | Good authority support, reasonable record evidence, persuasive reasoning         | Supporting arguments; strengthen overall brief |
| **COLORABLE** | Arguable position with some support; may not prevail but worth raising           | Include to preserve for appeal or show dispute |
| **WEAK**      | Limited support; likely to fail but no downside to raising                       | Consider omitting unless preservation required |

### Movant's Argument Vulnerability

| Level           | Criteria                                                                  | Response Strategy                                        |
| --------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| **FATAL FLAW**  | Argument fails on its face; misreads law or ignores controlling authority | Lead with direct refutation; may warrant denial          |
| **VULNERABLE**  | Significant weakness in authority, facts, or logic                        | Attack specifically; show why argument fails             |
| **CONTESTABLE** | Reasonable argument but reasonable responses exist                        | Develop counter-argument; show dispute                   |
| **STRONG**      | Movant's argument is well-supported                                       | Address directly; do not ignore; may need to distinguish |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output:

| Gate         | Rule                                                  | Fail Action                   |
| ------------ | ----------------------------------------------------- | ----------------------------- |
| **Source**   | Every legal proposition cites specific authority      | Add citation or mark [VERIFY] |
| **Format**   | All citations follow Bluebook/OSCOLA/AGLC correctly   | Fix format                    |
| **Currency** | Cases checked for negative treatment                  | Flag [CHECK CURRENCY]         |
| **Record**   | Every factual assertion cites to specific record page | Add cite or flag              |
| **Support**  | Cited source actually supports the stated proposition | Verify accuracy               |

---

## Self-Interrogation for Key Arguments

For any argument classified as PRIMARY or upon which the motion's denial depends:

**Pass 1 — Legal Foundation**: Is this argument legally correct? Does the cited
authority actually support this proposition? Would a law clerk verify it?

**Pass 2 — Factual Foundation**: Is every factual assertion supported by admissible
record evidence? Are characterizations fair and accurate?

**Pass 3 — Adversarial Challenge**: What is movant's best response? Have I anticipated
and addressed it? What is the weakest link in this argument?

---

## Confidence Scoring

| Level         | Range     | Meaning                                         | Action                          |
| ------------- | --------- | ----------------------------------------------- | ------------------------------- |
| **Definite**  | 0.95-1.0  | Clear rule, binding authority, undisputed facts | State with confidence           |
| **High**      | 0.80-0.94 | Strong authority, minor questions               | State with brief caveat         |
| **Probable**  | 0.60-0.79 | Good arguments, could differ                    | State with reasoning            |
| **Possible**  | 0.40-0.59 | Genuinely uncertain                             | Flag for counsel review         |
| **Uncertain** | 0.0-0.39  | Weak basis, speculative                         | Do not assert; flag [UNCERTAIN] |

---

## Glass Box Audit Trail

Every opposition brief produced includes this audit metadata:

```yaml
glass_box:
  skill_name: "legalcode-opposition-brief-drafter"
  motion_type: "[motion to dismiss / summary judgment / preliminary injunction / etc.]"
  court: "[court name]"
  jurisdiction: "[jurisdiction]"
  client_role: "[plaintiff / defendant / etc.]"
  mode: "[full draft / argument development / strategy analysis]"
  movant_arguments_analyzed: [number]
  counter_arguments_developed: [number]
  primary_arguments: [number]
  genuine_disputes_identified: [number]
  authority_sources:
    - legalcode_mcp: "[Connected / Not connected]"
    - websearch: "[Used / Not used]"
    - provided_materials: "[List of documents]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  page_word_count: "[pages] / [words]"
  local_rules_checked: "[list]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns (What NOT to Do)

1. **Ignoring movant's strongest arguments**: Address the best arguments against you
   directly. Silence suggests you have no answer.

2. **Over-relying on procedural objections**: If you have substantive defenses, lead
   with them. Procedural arguments alone rarely succeed.

3. **Mischaracterizing the record**: Every factual assertion must be supportable by
   citation. Misstatements destroy credibility.

4. **String-citing without explanation**: Long citation strings without parentheticals
   or explanation suggest padding, not strength.

5. **Arguing facts in Statement of Facts**: Save argument for the Argument section.
   State facts neutrally (but selectively) in Statement of Facts.

6. **Neutral point headings**: "The Statute of Limitations" tells the court nothing.
   "Plaintiff Filed Within the Three-Year Limitations Period" makes an argument.

7. **Burying the lead**: Put your strongest argument first, not buried in section IV.
   Judges may not read the whole brief carefully.

8. **Ignoring adverse authority**: If movant cites a case that hurts you, distinguish
   it — do not pretend it does not exist.

9. **Conclusory application**: "The elements are met because the facts support them"
   is not analysis. Connect specific facts to specific elements.

10. **Excessive block quotes**: Block quotes over 50 words suggest you cannot synthesize.
    Quote sparingly; explain why the language matters.

11. **Failing to cite the record**: For summary judgment, every disputed fact must cite
    evidence. "Plaintiff disputes this" without a cite is worthless.

12. **Raising new claims or theories**: Opposition briefs respond to the motion filed,
    not raise new claims. New theories may be waived or stricken.

13. **Personal attacks on opposing counsel**: Attack arguments, not lawyers. Ad hominem
    arguments undermine credibility.

14. **Missing the standard of review**: If you do not correctly articulate the standard
    and show how it applies, you have not framed the analysis.

15. **Waiving arguments by not raising them**: If you want to preserve an argument for
    appeal, you must raise it. Silence is waiver.

---

## Writing Standards

Apply these standards before delivering any brief:

**Clarity**:

- One idea per sentence
- One argument per paragraph
- Define technical terms on first use
- Use parallel construction in lists

**Concision**:

- Eliminate throat-clearing ("It is important to note that...")
- Prefer active voice (>80% of sentences)
- Cut nominalizations (use verbs, not -tion/-ment nouns)
- Remove intensifiers that add nothing ("very," "clearly," "obviously")

**Precision**:

- Use exact statutory language when invoking a statute
- Quote key language from controlling cases
- Pinpoint citations (page number, not just case name)
- Distinguish "holding" from "dicta"

**Persuasion**:

- Lead with your strongest point
- Use argumentative point headings
- Frame issues favorably without mischaracterizing
- Anticipate and address counter-arguments

**Before delivery, verify**:

- Word/page count within limits
- All citations verified or marked [VERIFY]
- All record citations include pinpoint
- Point headings are argumentative conclusions
- Introduction previews key arguments
- Conclusion requests specific relief

---

## External Tool Integration

**legalcode-mcp** (if connected):

- Search for case law supporting opposition arguments
- Verify currency of movant's cited authority
- Find distinguishing cases and negative treatment
- Research jurisdiction-specific standards and procedures

**WebSearch** (if legalcode-mcp unavailable):

- Court rules and local requirements
- Recent case law developments
- Secondary source analysis

**Graceful degradation**:
If external tools are not connected, proceed with:

- Analysis of provided materials
- General legal knowledge
- All authority marked [VERIFY]
- Note in Glass Box: `external_tools: "Not connected"`

---

## Localization Notes

This skill is jurisdiction-agnostic at baseline. When localizing:

**For US state courts**:

- Check whether state follows federal summary judgment standard
- Verify state-specific briefing limits and formats
- Note any state-specific burden allocation rules
- Adjust citation format if state uses regional reporter

**For England & Wales**:

- Use skeleton argument format, not US brief format
- Apply American Cyanamid for interim injunctions
- Use OSCOLA citation format
- Note CPR requirements for evidence and costs

**For Australia**:

- Apply s 31A "no reasonable prospect" standard
- Use AGLC citation format
- Note Federal Court procedural requirements
- Address costs implications

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original skill synthesizing best practices
from appellate advocacy, summary judgment practice, and motion practice across US federal,
England & Wales, and Australian jurisdictions. Incorporates structural patterns from
legalcode-brief-analyzer, legalcode-summary-judgment-analysis, and legalcode-complaint-drafter.

---

## Output Format Template

```markdown
# [TITLE: PLAINTIFF'S/DEFENDANT'S OPPOSITION TO [MOTION TYPE]]

## Caption

[Court name]
[Case caption]
[Case number]

## Table of Contents

[For briefs over 10 pages]

## Table of Authorities

[For briefs over 10 pages]

---

## Introduction

[1-2 pages maximum. State what motion is being opposed and why it should be denied.
Identify the fatal flaw in movant's position. Frame the case theory favorably.
Preview strongest arguments.]

---

## Statement of Issues

[If required by local rule. Frame issues favorably.]

1. Whether [issue framed favorably to non-movant]...
2. Whether [issue framed favorably to non-movant]...

---

## Statement of Facts / Counter-Statement of Facts

[Present facts in narrative form favorable to non-movant. Cite record for every
material fact. Include facts movant omitted. For summary judgment, each fact must
cite admissible evidence.]

---

## Legal Standard

[State applicable standard with authority. For summary judgment: burden on movant,
non-movant need only show genuine dispute, evidence viewed in non-movant's favor.]

---

## Argument

### I. [ARGUMENTATIVE POINT HEADING STATING CONCLUSION]

[IRAC structure: Issue, Rule, Application, Conclusion. Cite authority for legal
propositions. Cite record for factual assertions. Address movant's argument directly.
Distinguish movant's authority.]

### II. [ARGUMENTATIVE POINT HEADING STATING CONCLUSION]

[Continue for each argument...]

---

## Conclusion

For the foregoing reasons, [Plaintiff/Defendant] respectfully requests that the Court
deny [Defendant's/Plaintiff's] [Motion Type] in its entirety [and grant such other
relief as the Court deems just and proper].

Dated: [Date]

Respectfully submitted,

---

[Attorney name]
[Bar number]
[Firm name]
[Address]
[Phone]
[Email]
Counsel for [Plaintiff/Defendant]

---

## Certificate of Service

I hereby certify that on [date], I electronically filed the foregoing with the Clerk
of Court using the CM/ECF system, which will send notification of such filing to all
counsel of record.

---

[Attorney name]
```
