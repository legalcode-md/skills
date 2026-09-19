---
name: legalcode-case-summarizer
description: 'Summarize case law into structured, citation-quality briefs covering holding, key facts,
  reasoning, concurrence/dissent, procedural history, and precedential value. Use when building a case
  library, preparing for trial or arbitration, conducting legal research on a doctrinal issue, mapping
  the development of a legal doctrine, performing due diligence on the strength of legal authority, or
  analyzing opposing counsel''s cited cases. Supports single-case deep summaries, batch processing of
  multiple cases, proper citation formatting (Bluebook, OSCOLA, AGLC, McGill Guide), and precedent chain
  mapping showing how a case fits into the broader development of a legal rule. Jurisdiction-agnostic
  at baseline with localization markers for US federal, England & Wales, and Australia. Also triggers
  on: "brief this case," "summarize this opinion," "what did the court hold in X," "map the precedent
  on Y," "is case X still good law," "digest these cases."'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Case Summarizer

> **Disclaimer**: This skill provides a framework for AI-assisted case law summarization.
> It does not constitute legal advice. All outputs must be reviewed by qualified legal
> counsel licensed in the relevant jurisdiction before reliance in any proceeding, brief,
> or legal document. Case law evolves; decisions may be appealed, overruled, distinguished,
> or superseded by statute after the date of summary. Any holding, reasoning, or citator
> status described in this output must be independently verified against an authoritative
> primary source before use. References to unreported, foreign, or historical cases carry
> elevated hallucination risk — verify every citation before relying on it.

---

## Purpose and Scope

This skill summarizes judicial decisions into structured, professionally formatted case
briefs. It is designed for legal researchers, litigators, transactional lawyers, and
compliance professionals who need to rapidly understand, compare, and apply case law.

**Covers:**

- Single-case deep-dive summaries (full IRAC/FIRAC structure)
- Batch case digests (standardized entries for a case library)
- Precedent chain mapping (how a rule evolved across multiple cases)
- Citator-status assessment (is this case still good law?)
- Relevance assessment (does this case apply to a specific legal issue?)
- Proper citation formatting (Bluebook, OSCOLA, AGLC, McGill Guide)
- Concurrence and dissent analysis (tracking minority reasoning for future doctrine)
- Cross-jurisdictional comparative summaries

**Does not:**

- Apply legal holdings to specific client facts (requires qualified counsel)
- Substitute for reading the full opinion on issues of first impression or high stakes
- Provide definitive citator status (use Westlaw KeyCite, LexisNexis Shepard's, or
  vLex for authoritative citator information)
- Draft arguments, briefs, or pleadings (see `legalcode-brief-analyzer` and related skills)
- Advise on jurisdictional choice-of-law rules

**Related skills:**

- `legalcode-brief-analyzer` — Evaluate and improve legal briefs
- `legalcode-early-case-assessment` — Pre-discovery case evaluation
- `legalcode-case-timeline-builder` — Litigation chronology construction
- `legalcode-legal-memorandum` — Structure legal analysis memoranda
- `legalcode-litigation-risk-assessment` — Risk scoring for active matters

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Citation format, authority hierarchy, and
court nomenclature vary significantly across jurisdictions — identify the forum and apply
the correct conventions before producing any output.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- **Citation format**: Bluebook (US), OSCOLA (UK/international), AGLC (Australia),
  McGill Guide (Canada), or house style for the client/matter
- **Court hierarchy**: The binding/persuasive distinction depends entirely on where the
  summarized case was decided relative to the forum court
- **Reporter conventions**: Official reporters, unofficial reporters, neutral citations,
  and parallel citation requirements differ across jurisdictions
- **Precedent doctrine**: Common law stare decisis differs from civil law precedent norms;
  horizontal vs. vertical stare decisis rules differ by court system
- **Citator resources**: KeyCite (Westlaw), Shepard's (Lexis), Casetext CARA, vLex,
  CaseMine, Jade (Australia), BAILII — availability varies by jurisdiction

**Reference anchors frequently needed:**

| Jurisdiction        | Court Hierarchy (High → Low)                   | Citation Format              | Key Citator                  |
| ------------------- | ---------------------------------------------- | ---------------------------- | ---------------------------- |
| **US Federal**      | SCOTUS → Circuit Court → District Court        | Bluebook 22nd ed. (May 2025) | Westlaw KeyCite              |
| **England & Wales** | UKSC → EWCA → EWHC                             | OSCOLA 4th ed.               | Lexis Shepard's / Westlaw UK |
| **Australia**       | HCA → FCAFC / State CA → FCA / State SC        | AGLC 4th ed.                 | Jade.io                      |
| **Canada**          | SCC → FCA / Provincial CA → FC / Provincial SC | McGill Guide 10th ed.        | Westlaw Canada               |
| **EU / CJEU**       | CJEU Grand Chamber → Chamber → General Court   | EU Citation Rules            | EUR-Lex                      |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The input provides a case name but no citation, and multiple cases share that name
- The summarization mode (deep-dive vs. digest vs. batch) is ambiguous
- The relevance focus (which legal issue to foreground) is unclear
- The citation format required is not specified
- The citator status of a case is uncertain and would change how to use it

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

Accept case law input in any of these formats:

- **Full citation**: `Palsgraf v. Long Island R.R. Co., 248 N.Y. 339 (1928)`
- **Case name only**: "Palsgraf" or "Carlill v Carbolic Smoke Ball Co"
- **URL**: Link to a judicial opinion on a court website, legal database, or PACER/CourtListener
- **Document upload**: PDF or text of the judicial opinion
- **Pasted text**: Opinion text pasted directly into the conversation
- **Topic/issue**: "Summarize the leading cases on promissory estoppel in English law"
- **Batch list**: Multiple cases provided as a numbered or bulleted list
- **Opposing brief**: "Summarize the cases cited by opposing counsel in their motion"

If only a case name is provided (no citation, no text), use **legalcode-mcp** or WebSearch
to locate the correct citation and opinion before proceeding. If multiple cases share the
same name, present the candidates to the user.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options. Skip questions already answered by the input:

1. **Summarization mode**: What type of output do you need?
   - **Deep Summary**: Full FIRAC analysis with holding, reasoning, dissent, and
     relevance assessment — for a key case you need to understand thoroughly
   - **Digest Entry**: Standardized short-form entry for a case library or table of
     authorities — covers citation, holding, and one-sentence significance
   - **Batch Digest**: Digest entries for multiple cases — optimized for processing
     10–100 cases into a structured case library
   - **Precedent Chain Map**: Trace the development of a legal rule across multiple cases
     over time — shows how doctrine evolved
   - **Comparative Summary**: Side-by-side comparison of multiple cases on the same issue
   - _Why this matters_: Each mode produces a different depth and format of output.

2. **Legal issue focus**: What issue are you researching?
   - Free text. Prompt with examples: "proximate causation in tort," "standing under
     Article III," "GDPR lawful basis for processing," "termination for convenience clauses"
   - _Why this matters_: A case often covers multiple legal issues. Knowing the focus
     lets the summary foreground the relevant holding and relegate other issues.

3. **Forum and perspective**: Where will this case be cited or used?
   - Options: US federal court, US state court (specify state), England & Wales, Scotland,
     Australia (specify state/territory), Canada, EU/CJEU, Other (specify)
   - _Why this matters_: The binding/persuasive classification and citation format depend
     on the forum.

4. **Citation format**: Which citation format should the output use?
   - Options: Bluebook (US), OSCOLA (UK/international), AGLC (Australia), McGill Guide
     (Canada), House style (specify), None required
   - _Why this matters_: A Bluebook citation for a UK case looks different from OSCOLA.

5. **Citator check**: Should the skill assess whether the case is still good law?
   - Options: Yes — perform citator assessment, No — skip citator analysis
   - _Why this matters_: Citator assessment requires external verification; for time-
     sensitive batch jobs the user may prefer to run their own check.

If the user provides partial context, proceed with reasonable defaults and state assumptions
explicitly (e.g., "I'm assuming Bluebook format — let me know if you need OSCOLA").

### Step 3: Locate and Retrieve the Opinion

**If the full opinion text is not already provided:**

1. Use **legalcode-mcp** to locate the full text of the opinion. Search by citation or
   case name.
2. If legalcode-mcp is not connected, use **WebSearch** and **WebFetch** to locate the
   opinion on authoritative free sources:
   - US cases: CourtListener (courtlistener.com), Google Scholar, Justia, PACER
   - UK cases: BAILII (bailii.org), legislation.gov.uk, National Archives
   - Australian cases: AustLII (austlii.edu.au), Jade.io
   - EU/CJEU: EUR-Lex (eur-lex.europa.eu)
   - Canadian cases: CanLII (canlii.org)

3. Verify the citation before proceeding:
   - Confirm the reporter, volume, page/paragraph number, and year
   - Confirm the full case name (parties and exact styling)
   - Note whether a neutral citation exists (post-2000 UK/AU/CA cases)
   - Check for any subsequent history noted in the opinion itself

**⟁ CLARIFY** — If the opinion cannot be located via legalcode-mcp or free sources:

- Inform the user that the case could not be retrieved
- Ask whether the user can supply the opinion text directly
- Offer to proceed with a summary based on available secondary sources, with the output
  clearly marked as `[SECONDARY SOURCE ONLY — opinion not reviewed]`

### Step 4: Extract Opinion Metadata

Before drafting the summary, extract the following metadata from the opinion:

| Field                  | What to Extract                                                  |
| ---------------------- | ---------------------------------------------------------------- |
| **Full citation**      | Parties, reporter, volume, page, court, year                     |
| **Neutral citation**   | If available (e.g., `[2023] UKSC 14`, `[2023] HCA 21`)           |
| **Decision date**      | Date of judgment (not date of oral argument)                     |
| **Court**              | Specific court and panel (e.g., "Second Circuit, 3-judge panel") |
| **Author**             | Authoring judge(s) of the majority opinion                       |
| **Concurrences**       | Judges who concurred separately and the basis                    |
| **Dissents**           | Judges who dissented and the basis                               |
| **Procedural posture** | How the case reached this court                                  |
| **Prior history**      | Lower court decisions leading to this appeal                     |
| **Subsequent history** | Any known subsequent history (cert. denied, appeal pending)      |
| **Topics / keywords**  | Legal topics covered (for indexing)                              |

### Step 5: Draft the Case Summary

Structure the summary using the **Case Summary Format** defined in the Output Format
Template section. Tailor depth to the selected summarization mode:

#### 5a. Deep Summary Mode

Produce a full FIRAC analysis:

**Facts** — Summarize only the legally material facts. Apply these principles:

- Include facts the court explicitly relies on in its reasoning
- Exclude procedural facts unless they are legally significant
- Preserve the factual framing the majority uses — this affects which rule applies
- Note any disputed facts and how the court resolved them
- Flag facts that dissenting judges weigh differently

**Issue(s)** — State each legal question the court decides, precisely:

- Frame issues using the **whether-when-and** structure: "Whether [legal rule applies] when
  [specific factual context] and [dispositive limiting condition]." This structure prevents
  the issue from being stated either too broadly (loses utility) or too narrowly (limits
  precedential reach).
- Identify primary issue (the one the holding directly addresses)
- Identify secondary issues (alternative grounds, subsidiary questions)
- Note issues the court **declines to decide** (expressly deferred or dismissed as moot) —
  these undecided questions are often as important to the user as what was decided

**Rule(s)** — State the legal rule the court applies to each issue:

- Cite the statute, regulation, or prior precedent from which the rule derives
- Note whether the court is applying, extending, limiting, or departing from prior rule
- Identify whether the rule is announced for the first time (case of first impression)
- Flag circuit splits, conflicting authorities, or competing formulations the court addresses

**Application / Reasoning** — Summarize how the court applies the rule to the facts:

- Follow the majority's own reasoning structure
- Identify key analytical moves (analogies, distinctions, policy arguments)
- Note reliance on canons of statutory construction (if statutory interpretation case)
- Flag any reasoning the court acknowledges is contested or policy-driven
- Identify the weakest points in the majority's reasoning (often where the dissent attacks)

**Holding** — State the holding precisely:

- **Quote the operative language verbatim** where possible — legal precision lives in
  exact word choice. Paraphrasing introduces error. Use the court's own formulation of
  the test, standard, or rule, with a pinpoint citation to the page or paragraph.
- Classify each legal proposition extracted using the **Holding Type Classification**:
  HOLDING / DICTA / ASSUMED / UNSETTLED (see below)
- Note whether the holding is narrow or broad
- Flag any ambiguity in the scope of the holding (if the dissent or subsequent cases
  have questioned the holding's scope, note this)
- State the **Outcome Status**: AFFIRMED / REVERSED / REVERSED AND REMANDED / REMANDED /
  AFFIRMED IN PART AND REVERSED IN PART / VACATED / DISMISSED

**Concurrences** — For each separately concurring opinion:

- Identify the author and joining judges
- State whether it is a concurrence in the judgment only or the reasoning as well
- Summarize the basis for the separate concurrence
- Flag whether the concurrence narrows the majority's holding

**Dissents** — For each dissenting opinion:

- Identify the author and joining judges
- Summarize the primary grounds for dissent
- Note whether the dissent attacks the majority's facts, rule, or application
- Flag whether the dissent's reasoning has been adopted in subsequent cases
  (a dissent that later becomes the majority is a marker of doctrinal instability)

**What the Court Did NOT Decide** — Explicitly identify:

- Issues the court **expressly reserved** for another day ("We do not decide whether...")
- Questions addressed only **arguendo** (assumed without deciding)
- Issues the court **dismissed as moot**, unripe, or lacking jurisdiction
- Any **circuit splits** the court acknowledged without resolving
- Issues raised in **dissent** that the majority declined to address

This section is as important as the holding itself. Opposing counsel will exploit gaps in
what the court decided. Surfacing undecided questions prevents over-reliance on the case.

**Significance / Relevance Assessment** — Assess the case's value:

- Classify its precedential status (see Precedential Status Classification below)
- State adverse implications: how opposing counsel would use this case; what facts
  distinguish your matter from the case's holding
- Identify the legal proposition(s) for which it can be cited
- Note any limitations on its applicability (limited to specific facts, narrow rule)
- Note any subsequent cases that have applied, limited, or distinguished this holding

#### 5b. Digest Entry Mode

Produce a standardized short-form entry:

```
**[Full Citation]**
*[Neutral citation if available]*

**Issue**: [One sentence]
**Holding**: [One sentence]
**Significance**: [One sentence — the legal proposition for which this case stands]
**Citator status**: [GOOD LAW / QUESTIONED / CAUTION / BAD LAW] — [source]
**Notes**: [Any limitations, circuit split, or key dissent]
```

#### 5c. Batch Digest Mode

For batches of 10+ cases, process each case using the Digest Entry format and organize
the output as a structured table followed by individual entries. Apply batch processing
protocol:

1. Process cases in citation order (oldest to newest) to build chronological context
2. Group related cases by legal proposition if the user provided a topic focus
3. Flag any case in the batch where the opinion could not be retrieved
4. Flag any case where the citation appears to be incorrect or does not match
5. After all individual entries, produce a **Synthesis Section** summarizing:
   - The core legal proposition supported by the batch
   - The trend in the doctrine (expanding, contracting, unsettled)
   - Any circuit/jurisdiction splits within the batch
   - The single strongest case in the batch for the user's identified issue

**⟁ CLARIFY** — For batches of 50+ cases:

- Ask whether the user wants a full digest entry for each case or a
  **tiered batch**: deep summaries for the 5 most material cases + digest entries
  for the remainder
- Ask whether there is a specific issue or proposition the batch should be organized around

#### 5d. Precedent Chain Map Mode

Trace the development of a legal rule across time:

1. Identify the **foundational case** where the rule was first announced or clearly stated
2. Map **subsequent developments** in chronological order:
   - Cases that **affirmed or applied** the rule
   - Cases that **limited** the rule's scope
   - Cases that **extended** the rule to new contexts
   - Cases that **questioned** or created tension with the rule
   - Cases that **overruled** or **superseded** the rule (by decision or statute)
3. Produce a **Doctrine Timeline** showing the rule's evolution
4. Assess the current state of the rule: settled, developing, contested, or defunct

### Step 6: Citator Status Assessment

For each case summarized, assess its current citator status. This is distinct from the
precedential classification (binding/persuasive) — citator status tells you whether the
case is still good law regardless of its authority level.

Apply the **Citator Status Classification** below. Where legalcode-mcp is connected,
use it to retrieve citator information. Where not connected, use WebSearch to check for
subsequent history and mark the assessment with [VERIFY].

### Step 7: Quality Verification

Before delivering, run the quality checks defined in the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For any HIGH-SIGNIFICANCE case (key precedent, case of first impression, or case
   the user will cite in a brief), run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to all holdings and reasoning summaries.
4. Verify completeness: confirm all required summary sections are present for the
   selected mode.
5. Generate the Glass Box Audit Trail.

### Step 8: Deliver Output

Structure the final deliverable using the Output Format Template. Append the Glass Box
Audit Trail. For batch mode, include a batch processing summary.

---

## Case Summary Depth Tiers

| Tier                  | Mode         | Sections                                                | Typical Use                                                        |
| --------------------- | ------------ | ------------------------------------------------------- | ------------------------------------------------------------------ |
| **Tier 1 — Deep**     | Deep Summary | All FIRAC sections + concurrence/dissent + significance | Key cases for briefing, case preparation, or doctrinal research    |
| **Tier 2 — Standard** | Digest Entry | Citation, issue, holding, significance, citator status  | Case library building, table of authorities, research memo support |
| **Tier 3 — Micro**    | Batch Micro  | Citation + one-line holding                             | Volume processing, preliminary screening, citation checking        |

---

## Precedential Status Classification

Classify every summarized case by its precedential status relative to the user's forum:

### BINDING (Green)

The case is binding precedent the forum court must follow, absent distinguishing facts
or an overruling decision.

**Applies when:**

- The case was decided by a court that sits above the forum court in the same judicial
  hierarchy
- The forum court has explicitly adopted the rule from another jurisdiction's precedent
- The case is from the same court (horizontal precedent in jurisdictions that recognize it)

**Action**: Cite with confidence. Confirm the case is not overruled.

### PERSUASIVE (Yellow)

The case is not binding but may be cited to support an argument. The forum court may
adopt its reasoning.

**Applies when:**

- The case is from a court in a different but related jurisdiction (e.g., another US
  Circuit, another common law country's highest court)
- The case is from a lower court in the same hierarchy (persuasive as to reasoning)
- The case is from a parallel court in the same hierarchy
- The case is from a jurisdiction whose law is respected but not binding

**Action**: Cite as persuasive. Identify why the forum court should find it compelling
(quality of reasoning, widespread adoption, policy alignment).

### DISTINGUISHABLE (Neutral)

The case was initially identified as potentially applicable but, on analysis, can be
distinguished on its facts or the applicable rule.

**Applies when:**

- The material facts differ in a legally significant way
- The rule announced was limited to specific factual circumstances
- A subsequent case has distinguished the holding in the relevant context

**Action**: Note the distinction clearly. Identify which facts or legal principle
creates the distinguishing line.

### QUESTIONED / TENSION (Orange)

The case remains technically good law but has been criticized, limited, or placed in
tension with subsequent decisions.

**Applies when:**

- A higher or same-level court has questioned the reasoning without overruling
- Circuit or jurisdictional splits have developed around the holding
- The case has been limited to narrow facts by subsequent cases
- Concurrences or dissents have foreshadowed doctrinal instability

**Action**: Flag the tension. Identify which subsequent cases create tension and why.
Advise the user to verify current citator status before relying on it.

### OVERRULED / SUPERSEDED (Red)

The case is no longer good law on the relevant point.

**Applies when:**

- A court with authority to do so has expressly overruled the holding
- A legislature has enacted a statute that supersedes the common law rule
- The case's underlying precedent was overruled, undermining its foundation
- A constitutional amendment or fundamental doctrine shift has displaced the rule

**Action**: Do not cite as precedent. Identify the overruling/superseding authority.
Note whether any portion of the case remains good law on other issues.

---

## Holding Type Classification

For every legal proposition extracted from a case, classify it by **Holding Type**. This
is orthogonal to Precedential Status — a proposition can be BINDING precedent but only
DICTA, which means it is technically binding but with more limited stare decisis effect.

| Type              | Definition                                                                                                                                     | Stare Decisis Effect                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **HOLDING**       | Necessary to the decision; the court could not have reached its outcome without this proposition. Common law equivalent: _ratio decidendi_.    | Binding on the _ratio decidendi_                                              |
| **DICTA**         | Said in passing; not necessary to the outcome; the court would have reached the same result without it. Common law equivalent: _obiter dicta_. | Persuasive only; no stare decisis obligation                                  |
| **ASSUMED**       | Assumed without deciding (arguendo); the court proceeded on the premise without resolving it                                                   | None — cannot be cited as authority for the assumed point                     |
| **UNSETTLED**     | The court acknowledged the question and declined to resolve it, or noted conflicting authority                                                 | Flags an open question; no authority for any position                         |
| **OVERRULING**    | The court expressly discards a prior precedent                                                                                                 | The prior case loses precedential value on the overruled point                |
| **DISTINGUISHED** | The court limits a prior case to its specific facts                                                                                            | Prior case remains good law but not applicable to the current factual pattern |

### Application Rules

1. When in doubt between HOLDING and DICTA, apply the **but-for test**: Would the court's
   disposition change if this proposition were false? If yes → HOLDING. If no → DICTA.

2. **Multi-factor tests**: If the court announces a multi-factor test, every factor is
   part of the HOLDING even if not all factors are disputed in the instant case.

3. **Plurality opinions**: When no single rationale commands a majority of the full court,
   identify the **narrowest grounds** for the judgment using the _Marks_ rule [VERIFY for
   US jurisdictions]. Label each rationale with the number of judges joining it.

4. **Always include a pinpoint citation** for any proposition labeled HOLDING. A holding
   without a page or paragraph reference is not usable in a brief.

---

## Citation Format Reference

### Bluebook (US — 22nd Edition, May 2025)

**22nd edition changes**: New AI-generated content citation rules (Rule 18); `(citation
modified)` parenthetical replaces the prior `(cleaned up)` practice; Tribal Nation
citation guidance added (Rule 22). For pre-2025 legal work, 21st edition rules remain
cited in many jurisdictions — confirm which edition is required.

**Core structure (Rule 10):**

```
Case Name, Volume Reporter First-Page, Pinpoint-Page (Court Year).
```

**Key court-specific rules:**

- **SCOTUS** — Cite to U.S. Reports. **Omit court abbreviation** in parenthetical —
  the U.S. reporter signals SCOTUS. Include year only.
  `Marbury v. Madison, 5 U.S. (1 Cranch) 137 (1803).`
  `Sweatt v. Painter, 339 U.S. 629, 632 (1950).`
- **Courts of Appeals** — Cite to Federal Reporter. Include both circuit and year.
  `United States v. Carroll, 87 F.4th 1214, 1221 (11th Cir. 2023).`
- **District Courts** — Cite to Federal Supplement. Include specific district and year.
  `Doe v. Roe, 123 F. Supp. 3d 456, 461 (S.D.N.Y. 2000).`
- **State highest courts** — Omit court abbreviation if the reporter unambiguously
  identifies the state, or if it is the state's highest court.
  `Seeco, Inc. v. Hales, 22 S.W.3d 157 (Ark. 2000).`

**Reporter abbreviations (Table T1):**

```
U.S.              — United States Reports (SCOTUS)
S. Ct.            — Supreme Court Reporter (SCOTUS, interim)
F. / F.2d / F.3d / F.4th  — Federal Reporter (Courts of Appeals)
F. Supp. / F. Supp. 2d / F. Supp. 3d  — Federal Supplement (District Courts)
F. App'x          — Federal Appendix (unpublished circuit opinions)
```

**Short form (after first full citation):**

```
Carroll, 87 F.4th at 1225.    (party name + reporter + at + pinpoint)
Id. at 463.                   (same source, different page/paragraph)
Id.                           (same source, same page)
```

**Note**: `supra` may NOT be used for cases (Rule 4.2 — cases are expressly excluded).

**Prior and subsequent history (Rule 10.7):**

```
aff'd, aff'g, rev'd, vacated, cert. denied, remanded, overruled by
```

Omit cert. denied unless decided within the past two years or particularly relevant.

**Parentheticals:**

```
Carroll, 87 F.4th at 1225 (holding that...).
Carroll, 87 F.4th at 1225 (citation modified).   [22nd ed. replaces (cleaned up)]
```

### OSCOLA (UK — 4th Edition)

**Modern cases with neutral citation:**

```
[Year] Court Case-Number (Court, Year) [Neutral Citation] Reporter Volume Page
R (Miller) v Secretary of State for Exiting the European Union [2017] UKSC 5, [2018] AC 61
```

**Older cases (no neutral citation):**

```
[Year] or (Year) Volume Reporter Page (starting page)
Donoghue v Stevenson [1932] AC 562 (HL)
```

**Court abbreviations:**

```
UKSC  — UK Supreme Court
UKPC  — Privy Council
EWCA Civ — Court of Appeal (Civil)
EWCA Crim — Court of Appeal (Criminal)
EWHC (Admin) — High Court, Administrative Court
EWHC (Comm) — High Court, Commercial Court
```

**Pinpoint paragraphs** (use paragraph numbers, not page numbers for neutral-cited cases):

```
Jones v Smith [2020] EWCA Civ 123 [45]–[48].
```

**Short form:**

```
Miller (n 3) [25]. (where n 3 is the footnote of the full citation)
```

### AGLC (Australia — 4th Edition)

**Cases with neutral citation:**

```
Party v Party [Year] Court CaseNo, Paragraph
Mabo v Queensland (No 2) (1992) 175 CLR 1, 66–67.
```

**Neutral citation format (post-2000 typically):**

```
[Year] HCA CaseNo     — High Court of Australia
[Year] FCAFC CaseNo   — Full Federal Court
[Year] FCA CaseNo     — Federal Court (single judge)
[Year] NSWCA CaseNo   — NSW Court of Appeal
[Year] NSWSC CaseNo   — NSW Supreme Court
```

**Pinpoint** — Paragraph numbers, not pages, for cases with neutral citations.

**Short form:** Abbreviated party name, first citation footnote number:

```
Mabo (No 2) (n 3) 70.
```

### McGill Guide (Canada — 10th Edition)

**Key distinction from OSCOLA**: Canadian neutral citation years are **not** in brackets —
the year is a bare prefix, not a volume identifier. `2001 SCC 1` not `[2001] SCC 1`.

**Cases with neutral citation:**

```
Style of Cause, Neutral Citation, [Year if needed] Volume Reporter Page.
R v Latimer, 2001 SCC 1, [2001] 1 SCR 3.
R v Jordan, 2016 SCC 27, para 14, [2016] 1 SCR 631, 638.
```

**Cases without neutral citation (pre-rollout):**

```
R v Smith, [1987] 1 SCR 1045.
```

**CanLII fallback (when no neutral citation and no print reporter available):**

```
R v Name, [Year] Court CaseNo (CanLII).
```

**Court abbreviations:**

```
SCC   — Supreme Court of Canada
FCA   — Federal Court of Appeal
FC    — Federal Court
ONCA  — Ontario Court of Appeal
ONSC  — Ontario Superior Court of Justice
BCCA  — British Columbia Court of Appeal
BCSC  — BC Supreme Court
ABKB  — Alberta Court of King's Bench
QCCA  — Quebec Court of Appeal
```

**Citator note (Canada):** CanLII (canlii.org) is the primary free source. QuickLaw
(Lexis) and Westlaw Canada for commercial citator services.

---

## Precedent Chain Mapping

When operating in Precedent Chain Map mode, apply this framework:

### Chain Elements

| Element           | Definition                                                        | Mapping Action                            |
| ----------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| **Founding case** | The case that first clearly announces the rule                    | Identify and feature prominently          |
| **Affirmed**      | Cases that apply the rule without modification                    | Note as supporting the rule               |
| **Extended**      | Cases that apply the rule to a new fact pattern or area of law    | Note the extension and its scope          |
| **Limited**       | Cases that apply the rule but restrict its scope                  | Note the limiting principle               |
| **Distinguished** | Cases that decline to apply the rule on factual or legal grounds  | Note the distinguishing principle         |
| **Questioned**    | Cases that criticize the rule without overruling                  | Note as signs of doctrinal instability    |
| **Overruled**     | Cases that expressly overrule the prior holding                   | Note as the terminus of the prior rule    |
| **Superseded**    | Legislative or constitutional developments that displace the rule | Note statute/amendment and effective date |

### Doctrine Timeline Format

```
[YEAR] [Case Citation] — [FOUNDING / EXTENDED / LIMITED / DISTINGUISHED /
                           QUESTIONED / OVERRULED / SUPERSEDED]
       Holding in one sentence.
       Effect on doctrine: [how this case changed the state of the law]
```

### Conflict and Split Mapping

When multiple courts have taken different positions on the same rule:

1. Identify the jurisdictions / circuits on each side of the split
2. State the holding in each competing line of cases
3. Assess which line has more courts, more recent authority, or more compelling reasoning
4. Note whether a higher court has resolved the split (or noted its existence without
   resolving it)
5. Advise on the litigation strategy implications: which forum's rule applies to the
   user's matter, and is forum shopping relevant?

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivering if any
gate fails.

| Gate           | Rule                                                                                                  | Fail Action                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Source**     | Every case citation provides full citation with reporter and year                                     | Locate full citation or mark `[CITATION INCOMPLETE — verify]`                      |
| **Format**     | All citations follow the correct format for the specified convention (Bluebook, OSCOLA, AGLC, McGill) | Fix format errors before delivery                                                  |
| **Currency**   | Every case checked for subsequent history (especially overruling, reversal, or supersession)          | Flag `[CHECK CITATOR — verify still good law]`                                     |
| **Domain**     | Case summaries stay within the scope of the actual opinion text                                       | Remove or mark `[BEYOND OPINION — verify]` for anything not sourced in the opinion |
| **Confidence** | Uncertainty about holdings, reasoning, or status is explicitly stated, not hidden                     | Add `[VERIFY]` tag and confidence qualifier                                        |

### Self-Interrogation for HIGH-SIGNIFICANCE Cases

For any case classified as HIGH SIGNIFICANCE (key precedent, case of first impression,
or case identified as central to a user's matter), apply this 3-pass review:

**Pass 1 — Accuracy Chain**:

- Does the stated holding follow from the actual disposition in the case?
- Would the authoring court recognize this summary of its reasoning?
- Are there qualifications in the opinion that limit the holding stated?

**Pass 2 — Completeness**:

- Have all holdings been captured (not just the primary one)?
- Have significant concurrences been assessed for their narrowing effect on the majority?
- Has the subsequent history been reviewed for limiting or overruling decisions?

**Pass 3 — Challenge**:

- What is the strongest argument that this case does NOT stand for the proposition stated?
- Are there subsequent decisions that limit this case to its specific facts?
- Is there a competing line of authority that a court might prefer?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence level to each holding summary and precedential status classification:

| Level        | Range     | Meaning                                                               | Action                                             |
| ------------ | --------- | --------------------------------------------------------------------- | -------------------------------------------------- |
| **Definite** | 0.95–1.0  | Holding clearly stated in the opinion; citator confirmed              | State with confidence                              |
| **High**     | 0.80–0.94 | Holding apparent from the opinion; citator not independently verified | State with brief caveat                            |
| **Probable** | 0.60–0.79 | Holding derived from reasoning; some ambiguity in scope               | State with explicit reasoning and `[VERIFY]` flag  |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations                        | Flag for counsel review with both interpretations  |
| **Unlikely** | 0.0–0.39  | Speculative; opinion text not reviewed directly                       | Do not assert; flag `[UNCERTAIN — review opinion]` |

---

## Glass Box Audit Trail

Every case summary output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-case-summarizer"
  mode: "[Deep Summary / Digest / Batch / Precedent Chain / Comparative]"
  cases_summarized: "[number]"
  citation_format: "[Bluebook / OSCOLA / AGLC / McGill / None]"
  forum: "[jurisdiction or 'Not specified']"
  issue_focus: "[stated issue focus or 'General']"
  legalcode_mcp: "Connected / Not connected"
  opinion_text_reviewed: "Yes (full) / Yes (partial) / No (secondary sources only)"
  citator_assessment: "Performed / Skipped (user request) / Not available"
  cases_not_retrieved:
    - "[Citation — reason not retrieved]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / Not applicable"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when summarizing case law:

1. **Summarizing from the headnotes only** — Headnotes (West/Lexis) are editorial
   summaries, not the court's language. They may mischaracterize the holding or
   omit important qualifications. Always read the opinion text. Mark output as
   `[HEADNOTE ONLY — opinion not reviewed]` if a full opinion is unavailable.

2. **Conflating the holding with dicta** — Dicta (statements not necessary to the
   decision) do not bind future courts. A court may say many things; only what it
   actually decides on the facts presented is the holding. Identify dicta separately
   and mark it as such.

3. **Stating the broadest possible holding** — Courts decide the case before them.
   Overstating the holding (e.g., "the court held that all indemnification clauses
   are unenforceable") misrepresents what the court actually decided and may mislead
   a lawyer who relies on the summary without reading the opinion.

4. **Ignoring concurrences that narrow the majority** — When a justice concurs only in
   the judgment and not the majority's reasoning, the majority opinion may not represent
   the actual holding if the concurrence provides the critical fifth vote on narrower
   grounds. _See Marks v. United States_ [VERIFY] for the US doctrine on this.

5. **Fabricating citations** — AI systems can hallucinate reporter volumes, page numbers,
   and even entire cases. Never deliver a case citation that has not been verified against
   the actual opinion or an authoritative database. If the citation cannot be verified,
   mark it `[UNVERIFIED — confirm before use]` explicitly.

6. **Treating persuasive authority as binding** — A well-reasoned decision from another
   circuit or jurisdiction is persuasive, not binding. Do not classify it as BINDING
   without confirming the court hierarchy relationship. Never describe a case as
   "controlling" without confirming it is actually in the binding authority chain for
   the relevant forum.

7. **Ignoring citator status** — A case may appear authoritative but have been overruled,
   distinguished, or limited by a more recent decision. Never summarize a case as good
   authority without noting that citator status should be verified.

8. **Describing dissents as holdings** — A dissent, no matter how influential or widely
   cited, is not the holding of the court. Dissents may foreshadow future doctrinal
   development but must be labeled clearly as minority opinions.

9. **Applying US citation conventions to UK or Australian cases** — Bluebook format
   does not apply outside the US. OSCOLA has different conventions for parallel citations,
   year placement (square brackets vs. round brackets), and pinpoints (paragraphs, not
   pages). Always apply the correct convention for the jurisdiction.

10. **Omitting the procedural posture** — The standard of review applied depends on how
    the case reached the appellate court (de novo, clear error, abuse of discretion, etc.).
    Omitting procedural posture makes it impossible to understand why the court deferred
    or did not defer to the lower tribunal's findings.

11. **Treating circuit splits as resolved when they are not** — If two circuit courts
    have split on an issue and the Supreme Court has not resolved it, say so. Do not
    choose a side and present it as settled law.

12. **Missing the limiting language** — Courts frequently announce rules with limiting
    language ("In this narrow context...", "We hold only that..."). Omitting limiting
    language overstates the breadth of the holding and misrepresents the state of the law.

13. **Presenting legislative history or policy arguments as holdings** — When a court
    recites legislative history or policy rationale, that context informs interpretation
    but is not itself a legal holding. Label it as reasoning, not ruling.

14. **Failing to note when the majority's reasoning fractures** — In some landmark cases,
    the majority agrees on the outcome but splits on the rationale. In these plurality
    situations (common in US constitutional law), identifying the narrowest grounds for
    the judgment (the _Marks_ rule [VERIFY]) is essential for understanding what the
    case actually holds.

15. **Skipping the concurrence/dissent in batch mode** — For batch processing, it is
    tempting to summarize only the majority. But concurrences that narrow the holding and
    dissents that foreshadow overruling are material for assessing precedential risk. At
    minimum, note whether a significant concurrence or dissent exists, even in digest
    format.

16. **Confusing the date of argument with the date of decision** — The year in a citation
    refers to the date of decision, not argument. For rapidly evolving areas of law, use
    the decision date to assess the currency of the holding.

17. **Ignoring subsequent statutory developments** — A common law rule may be correct as
    case law but superseded by statute enacted after the decision. Always check whether
    legislation has displaced the common law rule being summarized.

18. **Over-summarizing a nuanced opinion** — Compression introduces error. When a case
    turns on subtle distinctions (e.g., originalism vs. living constitutionalism, contractual
    interpretation canons), the nuance matters. A one-sentence summary may strip out the
    qualification that determines whether the case applies.

19. **Paraphrasing the holding instead of quoting it** — Summarizing the holding in your
    own words loses the exact word choice that courts and practitioners rely on. A court
    that uses "materially misleading" means something different from "misleading." Quote
    the operative language with a pinpoint citation. Reserve paraphrase for context and
    explanation, not for the holding itself.

20. **Compressing a multi-factor test into a one-sentence rule** — When a case announces
    a balancing test or multi-element standard (e.g., the Winter injunction factors, the
    _Twombly/Iqbal_ plausibility standard, the _Daubert_ reliability criteria), summarizing
    it as a single proposition strips out the factor structure. State each factor or
    element explicitly so the summary can be used to apply the test.

21. **Missing the undecided questions** — Every deep summary must include a section on
    what the court expressly declined to decide, assumed arguendo, or dismissed as moot.
    Lawyers over-rely on cases by reading the holding broadly. Surfacing the undecided
    questions is often the most litigation-critical part of the summary.

---

## Writing Standards

Apply plain-language discipline to all case summary output:

**For holdings:**

- One sentence. Subject-verb-object.
- Name the actor (the court, not "it was held that")
- Use past tense: "The court held that..." not "The court holds that..."
- State the legal consequence: "...entitling the plaintiff to damages" or "...defeating
  the plaintiff's claim"
- Include the specific standard, test, or element the court applied

**For reasoning summaries:**

- Short paragraphs, one argument per paragraph
- Distinguish the court's reasoning ("The court reasoned that...") from the court's
  holding ("The court held that...")
- Identify the key pivot: the single factual or legal distinction that drove the result
- Use the court's own terminology for newly announced tests or standards

**For significance assessments:**

- Start with the legal proposition: "This case establishes that..."
- State the scope limitation if narrow: "...but only where..."
- State the citation value: "Cite for the proposition that..."
- Note competing authority: "But see [Case X] (reaching the opposite conclusion in [jurisdiction])"

**Quality gates before delivery:**

1. Can a first-year law associate understand the holding and significance from this summary?
2. Does the stated holding match what the court's disposition (affirmed/reversed/remanded) implies?
3. Is every case citation complete and format-compliant?
4. Is every unverified citation clearly marked `[VERIFY]`?
5. Are all `[JURISDICTION-SPECIFIC]` markers present where the analysis is not universal?
6. Does the output use the citation format specified by the user?

---

## External Tool Integration

### legalcode-mcp (Preferred)

**With legalcode-mcp connected:**

- In Step 3, search for the full opinion text using citation or case name
- In Step 6, retrieve citator status and subsequent history
- For precedent chain mapping, search for all cases citing the foundational case
- For batch processing, use legalcode-mcp to retrieve multiple opinions efficiently
- Mark all legalcode-mcp-sourced citations and status assessments as VERIFIED in the
  Glass Box audit trail

**Without legalcode-mcp:**

- Use WebSearch + WebFetch to retrieve opinions from free sources (CourtListener, BAILII,
  AustLII, CanLII, EUR-Lex)
- Mark all citator assessments with `[VERIFY — use KeyCite/Shepard's for authoritative status]`
- Note in Glass Box: `legalcode_mcp: "Not connected — free sources used"`
- Focus summaries on opinion text analysis rather than comprehensive citator tracking

### Free Legal Databases by Jurisdiction

| Jurisdiction    | Free Source                       | Coverage                                        |
| --------------- | --------------------------------- | ----------------------------------------------- |
| US Federal      | CourtListener (courtlistener.com) | All federal courts, extensive                   |
| US Federal      | Google Scholar                    | Federal + state courts, limited citator         |
| US Federal      | Justia.com                        | Federal + state, some citator                   |
| US Federal      | PACER                             | All federal, fee-per-page                       |
| England & Wales | BAILII (bailii.org)               | All reported cases, comprehensive               |
| Australia       | AustLII (austlii.edu.au)          | All jurisdictions, comprehensive                |
| Australia       | Jade.io                           | Cases with citator data, free tier limited      |
| Canada          | CanLII (canlii.org)               | All jurisdictions, comprehensive                |
| EU/CJEU         | EUR-Lex (eur-lex.europa.eu)       | All CJEU/GC decisions                           |
| International   | WorldLII (worldlii.org)           | Multi-jurisdiction portal                       |
| International   | vLex (vlex.com)                   | 1B+ documents, global jurisdictions, Vincent AI |

**Commercial citator reference** (for when free-source citator data is insufficient):

- **US**: Westlaw KeyCite (red stop sign = overruled/reversed; yellow flag = distinguished/limited/questioned) or LexisNexis Shepard's
- **UK**: Westlaw UK or LexisNexis Legal
- **Australia**: Jade.io (subscription) or LexisNexis AU
- **Canada**: Westlaw Canada or CanLII (free, limited negative treatment markers)
- **Note**: Automated citator signals are a starting point only — always read the citing cases to determine the actual scope and impact of any negative treatment

---

## Output Format Template

### Deep Summary Format

```markdown
## Case Summary — [Case Name]

> ⚠️ AI-Assisted Draft — Requires Attorney Review Before Reliance

### Executive Snapshot

**Citation**: [Short-form citation]
**Outcome**: [AFFIRMED / REVERSED / REVERSED AND REMANDED / etc.]
**Precedential weight**: [BINDING / PERSUASIVE / UNPUBLISHED] — [forum]
**Citator status**: [GOOD LAW / QUESTIONED / CAUTION / BAD LAW]
**Bottom line**: [One sentence — what this case means for the user's identified issue]
**Primary holding**: [One sentence verbatim or close paraphrase — with pinpoint citation]
**Confidence**: [Level] ([score])

---

### Full Citation

**Full citation**: [Properly formatted citation per the specified convention]
**Neutral citation**: [If available]
**Parallel citations**: [If required or available]
**Decision date**: [Date]
**Court**: [Specific court and panel]
**Authors**: Majority: [Judge]. Concurrence(s): [Judge(s)]. Dissent(s): [Judge(s)].

---

### Procedural History

[How the dispute arose, lower court decisions, how the case reached this court,
and the procedural standard of review applied on appeal]

---

### Key Facts

[Legally material facts only — the facts the court's reasoning actually turns on]

---

### Legal Issue(s)

1. [Primary issue — "Whether..."]
2. [Secondary issue(s) if any]
3. [Issues declined or deferred]

---

### Holdings Table

| Issue     | Holding (verbatim / close paraphrase) | Pinpoint   | Type    | Confidence  |
| --------- | ------------------------------------- | ---------- | ------- | ----------- |
| [Issue 1] | "[Quoted operative language]"         | [p.X / ¶Y] | HOLDING | [0.00–1.00] |
| [Issue 2] | "[...]"                               | [p.X]      | DICTA   | [0.00–1.00] |

**Outcome Status**: [AFFIRMED / REVERSED / REVERSED AND REMANDED / etc.]
**Dicta noted**: [Key statements made in passing — not holding, but potentially cited]

---

### Reasoning (Majority)

[Structured summary following the court's own analytical sequence. One paragraph per
major analytical step. Identify key analogies, distinctions, canons applied, and
policy arguments.]

---

### Concurrence(s)

**[Judge name], concurring [in the judgment / in part]:**
[Basis for the separate concurrence. Note if it narrows the majority holding.]

---

### Dissent(s)

**[Judge name], dissenting:**
[Primary grounds for dissent. Note if the dissent has been influential in subsequent
cases or foreshadows doctrinal change.]

---

### What the Court Did NOT Decide

- **Expressly reserved**: [Questions the court left for another day]
- **Assumed arguendo**: [Points assumed without deciding]
- **Moot / unripe / no jurisdiction**: [Issues dismissed on procedural grounds]
- **Acknowledged splits without resolving**: [Any circuit/jurisdiction splits noted]

---

### Precedential Status

**Classification**: [BINDING / PERSUASIVE / DISTINGUISHABLE / QUESTIONED / OVERRULED]
**Binding in**: [Courts where this is binding precedent]
**Persuasive for**: [Courts/jurisdictions where this is persuasive authority]
**Key limitation**: [Any limiting principle that constrains the holding's scope]

---

### Relevance Assessment

**Cite for**: [The specific legal proposition(s) for which this case can be cited]
**Do not cite for**: [Common misuses or overstatements of this case's holding]
**Distinguished when**: [Fact patterns that defeat application of this case]
**Adverse use**: [How opposing counsel would use this case; how to distinguish it]
**Related cases**: [Cases that affirm, limit, or conflict with this holding]

---

### Glass Box Audit Trail

[YAML block per Glass Box section]
```

### Digest Entry Format

```markdown
| Field                | Content                                                |
| -------------------- | ------------------------------------------------------ |
| **Citation**         | [Full citation]                                        |
| **Neutral citation** | [If available]                                         |
| **Court / Year**     | [Court name] / [Year]                                  |
| **Issue**            | [One sentence]                                         |
| **Holding**          | [One sentence]                                         |
| **Significance**     | [Legal proposition for citation]                       |
| **Citator status**   | [GOOD LAW / QUESTIONED / CAUTION / BAD LAW] — [source] |
| **Notes**            | [Key limitations, splits, dissent significance]        |
```

### Batch Digest Format

```markdown
## Case Digest: [Topic/Issue]

**Date compiled**: [Date]
**Cases processed**: [N] | **Retrieved**: [N] | **Not retrieved**: [N]
**Forum**: [Jurisdiction] | **Citation format**: [Convention]

---

### Summary Table

| Citation | Issue   | Holding   | Status   | Notes   |
| -------- | ------- | --------- | -------- | ------- |
| [Case 1] | [Issue] | [Holding] | [Status] | [Notes] |
| ...      |         |           |          |         |

---

### Individual Entries

#### [Case 1 — Full Citation]

[Digest entry format]

#### [Case 2 — Full Citation]

[...]

---

### Synthesis

**Core proposition**: [The legal rule supported by this body of cases]
**Trend**: [Expanding / Contracting / Settled / Unsettled]
**Jurisdiction splits**: [Any splits identified]
**Strongest case for your issue**: [Citation and why]
**Weakest cases / distinguishing risks**: [Cases that cut against or are easily distinguished]

---

### Glass Box Audit Trail

[YAML block]
```

### Precedent Chain Map Format

```markdown
## Precedent Chain: [Legal Rule or Doctrine Name]

**Compiled for**: [User's issue focus]
**Forum**: [Jurisdiction(s)]
**Chain length**: [N cases] | **Span**: [Year range]

---

### Doctrine Timeline

| Year   | Citation   | Status     | Effect on Doctrine                    |
| ------ | ---------- | ---------- | ------------------------------------- |
| [Year] | [Citation] | FOUNDING   | [Rule announced — one sentence]       |
| [Year] | [Citation] | AFFIRMED   | [Rule applied — one sentence]         |
| [Year] | [Citation] | EXTENDED   | [Rule extended to — one sentence]     |
| [Year] | [Citation] | LIMITED    | [Rule limited by — one sentence]      |
| [Year] | [Citation] | QUESTIONED | [Tension created by — one sentence]   |
| [Year] | [Citation] | OVERRULED  | [Overruling rationale — one sentence] |

---

### Current State of the Doctrine

**Rule as it stands**: [One paragraph — current best statement of the rule]
**Settled elements**: [What is no longer contested]
**Open questions**: [What remains unresolved or contested]
**Circuit/jurisdiction splits**: [Any unresolved splits]
**Legislative developments**: [Any statutes that affect the common law rule]

---

### Glass Box Audit Trail

[YAML block]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To localize for a specific jurisdiction:

1. **Replace citation format** — Confirm the correct citation convention (Bluebook, OSCOLA,
   AGLC, McGill, or other) and apply it consistently throughout
2. **Set the authority hierarchy** — Identify the binding/persuasive chain for the forum
   court and calibrate the Precedential Status Classification accordingly
3. **Confirm citator resources** — Identify which citator database is authoritative for
   the jurisdiction (KeyCite, Shepard's, Jade, CanLII)
4. **Adapt procedural nomenclature** — Ensure the procedural posture section uses correct
   local terms (e.g., "leave to appeal" vs. "certiorari"; "obiter dicta" vs. "dicta")
5. **Check precedent doctrine** — Civil law jurisdictions do not follow common law stare
   decisis; adapt the precedential status classification for jurisdictions where cases
   persuade rather than bind
6. **Add jurisdiction-specific anti-patterns** — Add items to the anti-patterns catalogue
   reflecting local traps (e.g., UK practitioners must note the difference between UKSC
   and House of Lords decisions post-2009)

**Common localization adjustments:**

| Jurisdiction        | Key Adjustment                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **US**              | Apply Bluebook; distinguish federal circuit splits; note SCOTUS grant/denial of cert                                           |
| **England & Wales** | Apply OSCOLA; use neutral citations post-1999; note Practice Statement 1966 [VERIFY] for UKSC departure from its own precedent |
| **Australia**       | Apply AGLC; note High Court's willingness to depart from its own precedent and from English authority                          |
| **Canada**          | Apply McGill Guide; note bijural context (common law + civil law in Quebec)                                                    |
| **EU/CJEU**         | Note primacy of EU law; distinguish preliminary rulings from direct actions                                                    |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis combining FIRAC case briefing
methodology, multi-jurisdictional citation format standards (Bluebook 21st ed., OSCOLA 4th
ed., AGLC 4th ed., McGill Guide 10th ed.), precedent chain mapping frameworks, citator
status classification, and the Legalcode quality assurance frameworks (Citation Quality
Gates, Self-Interrogation, Confidence Scoring, Glass Box audit trail). Informed by
structural patterns from `legalcode-brief-analyzer` and `legalcode-legal-memorandum`
skills, and adapted to the unique requirements of case law summarization for litigation,
research, and compliance workflows.
