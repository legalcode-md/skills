---
name: legalcode-plain-language
description: Rewrites legal text for specified audiences while maintaining legal accuracy and precision.
  Use when asked to "make this simpler," "translate this to plain English," "rewrite this for clients,"
  "check readability," "plain language review," "accessibility audit," "consumer-friendly version," "grade
  level check," or when a document must comply with plain language regulations such as the US Plain Writing
  Act 2010, SEC Rule 421 plain English, CFPB mortgage disclosures, GDPR Article 12(1) clear and plain
  language, UK Consumer Rights Act 2015 plain and intelligible, FCA Consumer Duty 2023, South Africa CPA
  s.22, ISO 24495-1:2023, ISO 24495-2:2025, or state-level insurance readability mandates (Florida/Connecticut
  Flesch RE ≥45, New York grade ≤8, Pennsylvania FK grade ≤9).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Rewrites legal text for specified audiences while maintaining legal accuracy and precision. Covers legalese simplification, active-voice conversion, jargon replacement, archaic-phrase elimination, readability scoring (Flesch-Kincaid Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG, Coleman-Liau), and plain language compliance assessment. Use when asked to "make this simpler," "translate this to plain English," "rewrite this for clients," "check readability," "plain language review," "accessibility audit," "consumer-friendly version," "grade level check," or when a document must comply with plain language regulations such as the US Plain Writing Act 2010, SEC Rule 421 plain English, CFPB mortgage disclosures, GDPR Article 12(1) clear and plain language, UK Consumer Rights Act 2015 plain and intelligible, FCA Consumer Duty 2023, South Africa CPA s.22, ISO 24495-1:2023, ISO 24495-2:2025, or state-level insurance readability mandates (Florida/Connecticut Flesch RE ≥45, New York grade ≤8, Pennsylvania FK grade ≤9). Applies to contracts, privacy policies, terms of service, regulatory disclosures, informed consent forms, insurance policies, court filings, correspondence, and any legal text requiring plain language treatment.


# Legalcode Plain Language

> **Disclaimer**: This skill provides a framework for AI-assisted plain language conversion of
> legal text. It does not constitute legal advice. Plain language rewriting that changes the
> substantive meaning of a legal provision can alter legal rights and obligations. All rewritten
> output must be reviewed by a qualified legal professional licensed in the relevant jurisdiction
> before use. Readability scores are proxies, not guarantees of comprehension. Statutory and
> regulatory citations carry hallucination risk — verify against authoritative sources before
> relying on them.

## Purpose and Scope

This skill converts legal text into plain language for a specified audience while preserving
legal accuracy. It audits readability, identifies legalese patterns, classifies each finding,
produces rewritten alternatives, and generates a compliance assessment against applicable plain
language mandates.

**Covers:**

- Readability scoring (Flesch Reading Ease, FKGL, Gunning Fog, SMOG, Coleman-Liau)
- Legalese identification: archaic phrases, Latin terms, doublets/triplets, passive voice,
  nominalizations, long sentences, vague terms ("shall," "reasonable," "forthwith")
- Rewriting with legal precision preserved
- Audience calibration (general public, business executive, in-house counsel, specialist)
- Jurisdictional plain language compliance check (US, UK, EU, AU, SA, ISO)
- Pre/post readability comparison
- Preservation catalogue: defined terms, terms of art, statutory language that must not change

**Does not:**

- Provide legal advice or replace qualified counsel
- Guarantee legal enforceability of rewritten provisions
- Substitute for jurisdiction-specific legal review
- Assess substantive legal correctness of the original text

**Two modes:**

- **AUDIT**: Score and classify only — no rewriting. Delivers a readability report and
  finding catalogue, flags each item as MUST-SIMPLIFY / SHOULD-SIMPLIFY / CONSIDER / PRESERVE.
- **REWRITE**: Full rewriting mode — produces simplified alternatives for all MUST-SIMPLIFY
  and SHOULD-SIMPLIFY items alongside the audit report.

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default. The document's governing law, target audience,
and applicable regulatory mandates determine which plain language standards apply.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **US Federal**: Plain Writing Act 2010 (Pub. L. 111-274); SEC Rule 421(d) (prospectuses);
  CFPB TRID (mortgage disclosures); 45 CFR 46 / 21 CFR 50 (informed consent)
- **US States**: NY Gen. Obligations Law §5-702 (grade ≤8, consumer contracts ≤$50K);
  NJ N.J.S.A. 56:12-1; PA insurance FK grade ≤9; FL/CT insurance Flesch RE ≥45
- **EU**: Unfair Contract Terms Directive 93/13/EEC (consumer standard terms — plain, intelligible);
  GDPR Art. 12(1) (privacy notices — clear and plain language); EU AI Act Art. 50 (AI disclosures)
- **UK**: Consumer Rights Act 2015 (plain and intelligible, prominent); FCA Consumer Duty 2023
  (clear, fair and not misleading; eradicate jargon)
- **South Africa**: Consumer Protection Act 68 of 2008 s.22 (understandable without undue effort)
- **Australia**: ACL 2011 (unfair terms; plain language practice)
- **International**: ISO 24495-1:2023 (any text-based document; 4 pillars: relevance, findability,
  understanding, usability); ISO 24495-2:2025 (legal communications specifically)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The target audience is unclear and it would change the target readability score
- The mode (AUDIT vs. REWRITE) has not been specified
- Compliance jurisdiction is needed to check regulatory mandates
- Terms of art are ambiguous — preserving them may restrict simplification
- The legal precision / accessibility trade-off requires a user judgment call

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

### Step 1: Accept the Document

Accept the legal text in any format:

- **File**: PDF, DOCX, TXT, or similar
- **URL**: Link to a document accessible by the Read tool
- **Pasted text**: Text pasted directly into the conversation
- **Section**: A specific clause, section, or provision from a larger document

If no text is provided, prompt the user to supply it.

### Step 2: Gather Context

**⟁ CLARIFY** — Before proceeding, ask (skip questions already answered in the prompt):

1. **Mode**: Audit only, or audit + rewrite?
   - **AUDIT**: Produce a readability report and finding catalogue with no rewriting.
     Best when the user wants to understand the problem before committing to rewrites.
   - **REWRITE**: Produce the full audit AND rewritten plain-language alternatives.
     Best when the user wants a draft to work from immediately.
   - _Why this matters_: Determines the scope of the output and whether legal precision
     trade-offs need to be discussed.

2. **Target audience**: Who will read this document?
   - **General public / consumers**: Grade 6–8 target; Flesch RE ≥60.
   - **Small business owners**: Grade 8–10; Flesch RE ≥50.
   - **Corporate executives (non-legal)**: Grade 10–12; Flesch RE ≥40.
   - **In-house counsel / business lawyers**: Grade 12–14; Flesch RE ≥30.
   - **Specialist legal practitioners**: Grade 14–16; Flesch RE ≥25.
   - _Why this matters_: The entire scoring target and rewriting depth depends on this.

3. **Compliance jurisdiction** (if applicable):
   - Options: US Federal, US state (specify which), EU, UK, South Africa, Australia,
     ISO 24495 (international), No specific mandate — use best-practice targets,
     Multiple jurisdictions (specify)
   - _Why this matters_: Compliance mode adds a regulatory pass/fail determination to
     the audit. If there is a statutory readability floor, the skill will report whether
     the document meets it.

4. **Document type** (if not obvious from the text):
   - Options: Consumer contract, Insurance policy, Privacy policy / privacy notice,
     Terms of service, Mortgage / financial disclosure, Informed consent, Court filing,
     Internal legal memo, Regulatory submission, Correspondence, Other
   - _Why this matters_: Determines applicable default readability mandates and which
     preservation categories apply (e.g., informed consent has strict FDA/IRB requirements).

5. **Preservation list** (optional):
   - Ask the user to list any defined terms, brand names, or specific phrases that must
     not be changed, even if they reduce readability.
   - _Why this matters_: Prevents inadvertent redefinition of contractual terms.

If the user provides partial context, proceed with reasonable defaults and state
assumptions explicitly.

### Step 3: Compute Baseline Readability Scores

Compute all five standard readability scores on the original text before any changes.

**If Python is available** (preferred — most accurate):

```python
import textstat

# text = the full document or passage
scores = {
    "flesch_reading_ease":       textstat.flesch_reading_ease(text),
    "flesch_kincaid_grade":      textstat.flesch_kincaid_grade(text),
    "gunning_fog":               textstat.gunning_fog(text),
    "smog_index":                textstat.smog_index(text),        # needs 30+ sentences
    "coleman_liau_index":        textstat.coleman_liau_index(text),
    "consensus_grade_level":     textstat.text_standard(text),
    "avg_sentence_length_words": textstat.avg_sentence_length(text),
    "avg_syllables_per_word":    textstat.avg_syllables_per_word(text),
    "difficult_word_count":      textstat.difficult_words(text),
    "word_count":                textstat.lexicon_count(text),
    "sentence_count":            textstat.sentence_count(text),
}
```

Install if needed: `pip install textstat`

**If Python is unavailable**: Compute manually using the formulas in **Readability Scoring
Reference** below, or report the qualitative assessment only and mark scores as [ESTIMATED].

Produce a **Baseline Scorecard** comparing each score to the target for the declared audience.
See **Audience Target Scores** table in the reference sections.

**⟁ CLARIFY** — If the text is shorter than 30 sentences, note that SMOG requires 30+
sentences for reliable scoring. Ask whether the user wants to proceed with the shorter
passage or combine with adjacent sections to reach the minimum.

### Step 4: Identify Legalese Patterns

Scan the document systematically for these 9 pattern categories. For each finding, note the
exact passage, the category, and a preliminary classification (MUST-SIMPLIFY / SHOULD-SIMPLIFY /
CONSIDER / PRESERVE).

| #   | Pattern Category                        | What to Detect                                                                                                                                                                      | Initial Classification                                                         |
| --- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1   | **Archaic here/there/where- words**     | herein, hereof, hereto, hereunder, hereafter, heretofore, therein, thereof, thereto, thereunder, therewith, wherein, wherefore                                                      | MUST-SIMPLIFY (general) / PRESERVE (statutory quote)                           |
| 2   | **Ceremonial deadwood**                 | WITNESSETH, Know all men by these presents, Comes now, IN WITNESS WHEREOF, Now therefore, by and between, made and entered into                                                     | MUST-SIMPLIFY                                                                  |
| 3   | **Archaic single-word substitutes**     | forthwith, aforesaid, aforementioned, said (used as "the"), such (used as "the"), same (used as pronoun), heretofore, henceforth                                                    | MUST-SIMPLIFY                                                                  |
| 4   | **Redundant doublets and triplets**     | null and void, cease and desist, any and all, each and every, terms and conditions, free and clear, last will and testament, rest residue and remainder, promise agree and covenant | MUST-SIMPLIFY                                                                  |
| 5   | **Latin and foreign phrases**           | inter alia, arguendo, prima facie, ab initio, ipso facto, mutatis mutandis, in toto, pari passu, vel non, viz., vide, i.e./e.g. used ambiguously                                    | MUST-SIMPLIFY (general audience) / PRESERVE (genuine terms of art — see below) |
| 6   | **Passive voice obligation clauses**    | "shall be paid," "is required to," "notice shall be deemed given," "repairs shall be made" — any obligation where the actor is not named                                            | MUST-SIMPLIFY (obligation clauses) / CONSIDER (findings of fact)               |
| 7   | **Nominalizations (zombie nouns)**      | make a determination, conduct an examination, provide assistance, give consideration to, effect a termination, be in violation of                                                   | SHOULD-SIMPLIFY                                                                |
| 8   | **Ambiguous "shall"**                   | Any use of "shall" — must be parsed as mandatory duty (→ must), permission (→ may), future fact (→ will), or definition (→ is/means)                                                | MUST-SIMPLIFY                                                                  |
| 9   | **Overlong sentences**                  | Any sentence >40 words: MUST-SIMPLIFY; 25–40 words: SHOULD-SIMPLIFY; 20–25 words: CONSIDER                                                                                          | Scale by length                                                                |
| 10  | **Vague quantifiers without standards** | reasonable, promptly, material, substantial, forthwith, as soon as practicable, best efforts, satisfactory — any vague standard without a definition                                | SHOULD-SIMPLIFY (add definition or timeframe)                                  |
| 11  | **Wordy prepositional phrases**         | pursuant to, in the event that, prior to, subsequent to, with respect to, in accordance with, for the purpose of, notwithstanding the foregoing, to the extent that                 | SHOULD-SIMPLIFY                                                                |

**Populate a Finding Register** (see Output Format Template) with each identified item.

### Step 5: Classify Each Finding

Apply the four-tier classification to every item in the Finding Register:

| Classification      | Meaning                                                                                                                   | Action Required                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **MUST-SIMPLIFY**   | Creates a comprehension barrier for the target audience; plain equivalent exists without precision loss                   | Replace in REWRITE mode; flag prominently in AUDIT mode |
| **SHOULD-SIMPLIFY** | Clear improvement available; minor precision trade-off possible or none; improves score meaningfully                      | Replace in REWRITE mode; recommend in AUDIT mode        |
| **CONSIDER**        | Optional improvement; some judgment required; minimal score impact                                                        | Flag as optional in both modes; note trade-off          |
| **PRESERVE**        | Term of art, defined term, statutory language, or phrase carrying legal significance not captured by any plain substitute | Do not change; annotate with reason                     |

**Apply Self-Interrogation before PRESERVE classification**: Run the 3-pass test in the
**Quality Assurance Framework** before designating any item PRESERVE. A PRESERVE designation
is a positive determination, not a default.

**Automatic PRESERVE triggers** (do not reclassify without user approval):

- Capitalized defined terms already introduced in the document (e.g., "Intellectual Property
  Rights," "Effective Date") — the term must not change after introduction
- Statutory text that must be reproduced verbatim (e.g., HIPAA authorization language,
  TILA disclosure boxes, Miranda warnings)
- Genuine terms of art with no adequate plain equivalent and legal consequence depending on
  the precise term: habeas corpus, certiorari, res judicata, mens rea, estoppel, laches,
  bona fide, force majeure [VERIFY whether force majeure is defined in the document]
- Proper nouns: party names, jurisdiction names, regulator names, statute titles
- Precision-loaded commercial terms where synonyms create different legal standards:
  "best efforts" vs. "commercially reasonable efforts" vs. "reasonable efforts"; "material
  breach" vs. "breach"; "time is of the essence"

**⟁ CLARIFY** — For any ambiguous PRESERVE vs. MUST-SIMPLIFY borderline (e.g., a Latin
phrase that is a term of art in a specialist context but opaque to the target audience),
present both options to the user:

> "Inter alia" appears 4 times. For a general public audience, this is typically replaced
> with "among other things." However, if this document will also be read by lawyers who
> expect the Latin form, preserving it is defensible. Which approach should I use here?

### Step 6: Rewrite (REWRITE mode only)

For every MUST-SIMPLIFY and SHOULD-SIMPLIFY item, produce a rewritten alternative following
the **Rewriting Techniques** reference below.

Structure each rewrite as:

```
**Finding [#]** | [Category] | [Classification]
Original:   "[exact quoted text]"
Rewritten:  "[plain alternative]"
Technique:  [What technique was applied — e.g., active voice, doublet elimination, sentence split]
Precision note: [Any legal precision trade-off, or "None — legal meaning unchanged"]
```

**Core rewriting principles** (see full details in Rewriting Techniques section):

1. Name the actor; use active voice; specify who does what by when
2. Use "must" for obligations, "may" for permissions, "will" for future facts
3. Break sentences at 25 words using periods, lists, or colons
4. Replace doublets with the single most precise word
5. Replace archaic here/there/where- words with the specific noun they refer to
6. Replace nominalizations with their root verbs
7. Use "you" and "we" for consumer documents

**⟁ CLARIFY** — When a rewrite would change substantive legal meaning (e.g., replacing
"best efforts" with "reasonable efforts" changes the standard), present the trade-off:

> "Section 4.2 requires 'best efforts' — a higher standard than 'commercially reasonable
> efforts.' Replacing it with 'all reasonable steps' for readability would change the
> obligation. Options: (A) Keep 'best efforts' as PRESERVE; (B) Replace and flag for
> counsel review; (C) Add a plain-language gloss in parentheses."

### Step 7: Compute Post-Rewrite Scores

After completing all rewrites, re-run the full readability scorecard on the rewritten text.

Report the improvement delta for each metric and confirm whether the document now meets:

- The audience target (see Audience Target Scores)
- Any applicable regulatory floor (see Jurisdictional Compliance section)

If the post-rewrite score still fails a regulatory threshold, identify which remaining
passages are the primary contributors to the low score and escalate them for further
simplification.

**⟁ CLARIFY** — If meeting the regulatory floor requires simplifying PRESERVE items or
changing legal meaning, present this conflict explicitly:

> "After rewriting all MUST-SIMPLIFY and SHOULD-SIMPLIFY items, the Flesch RE is 41 —
> below Florida's insurance requirement of 45. The remaining gap comes from [X] retained
> technical terms. To reach 45, I would need to simplify these. Options: (A) Add plain-
> language glossary notes alongside the retained terms; (B) Simplify them and flag for
> counsel review; (C) Accept the current score and note the compliance gap."

### Step 8: Compliance Assessment

If a compliance jurisdiction was specified in Step 2, run the Jurisdictional Compliance
Assessment.

For each applicable mandate:

1. State the requirement (statute, score threshold, or qualitative standard)
2. State the original score / status
3. State the post-rewrite score / status (REWRITE mode) or estimated post-rewrite projection
4. Classify: **COMPLIANT** / **PARTIAL** / **NON-COMPLIANT**

See **Jurisdictional Compliance Requirements** reference section for current standards.

Flag any mandate that cannot be met by readability rewriting alone (e.g., formatting
requirements — type size, line length, white space — that require document design changes
beyond text editing).

### Step 9: Quality Verification

Before delivering the output:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every regulatory citation in the compliance assessment, run the Citation Currency
   check — laws change. Mark any citation you cannot verify as [VERIFY].
3. For any PRESERVE designation that seems counterintuitive, run the 3-pass
   Self-Interrogation.
4. Verify: does every rewritten provision carry the same legal obligation as the original?
   If uncertain, mark the provision with [PRECISION REVIEW — counsel to confirm].
5. Generate the Glass Box Audit Trail and append to the output.

---

## Readability Scoring Reference

### Formula Quick Reference

| Metric                                | Formula                                               | Output                  | Notes                                                    |
| ------------------------------------- | ----------------------------------------------------- | ----------------------- | -------------------------------------------------------- |
| **Flesch Reading Ease (FRE)**         | 206.835 − (1.015 × ASL) − (84.6 × ASW)                | 0–100 (higher = easier) | Industry standard; used in many statutes                 |
| **Flesch-Kincaid Grade Level (FKGL)** | (0.39 × ASL) + (11.8 × ASW) − 15.59                   | US grade (0–∞)          | Most widely cited; used in PA, FL, CT laws               |
| **Gunning Fog Index**                 | 0.4 × [ASL + 100 × (complex words / words)]           | Grade level             | "Complex words" = 3+ syllable words (excl. proper nouns) |
| **SMOG Index**                        | 1.043 × √(polysyllables × 30/sentences) + 3.129       | Grade level             | Most reliable for healthcare; needs 30+ sentences        |
| **Coleman-Liau Index (CLI)**          | (5.89 × chars/words) − (0.3 × sentences/words) − 15.8 | Grade level             | Character-based; no syllable counting needed             |

_ASL = average sentence length (words per sentence); ASW = average syllables per word_

### Audience Target Scores

| Audience                                | FK Grade Level | Flesch RE | Gunning Fog | Notes                                                        |
| --------------------------------------- | -------------- | --------- | ----------- | ------------------------------------------------------------ |
| General public / consumers              | ≤8             | ≥60       | ≤8          | US average adult reads at grade 7–8                          |
| Healthcare patients (consent)           | ≤8             | ≥60       | ≤8          | FDA/IRB standard; SMOG preferred metric                      |
| Small business owners                   | ≤10            | ≥50       | ≤10         | Familiar with basic commercial terms                         |
| Corporate executives (non-legal)        | ≤12            | ≥40       | ≤12         | High education; prefer brevity                               |
| In-house counsel / business lawyers     | ≤14            | ≥30       | ≤14         | Technical terms acceptable                                   |
| Specialist practitioners (IP, tax, M&A) | ≤16            | ≥25       | ≤16         | Full technical vocabulary acceptable                         |
| Judges                                  | ≤14            | ≥30       | ≤14         | Prefer clear reasoning; readability correlates with outcomes |
| Regulators                              | ≤13            | ≥35       | ≤13         | Use regulatory terms of art                                  |

### Benchmark: How Legal Documents Actually Score

| Document Type                         | Actual Avg Flesch RE | Actual Avg Grade Level | vs. Target                                 |
| ------------------------------------- | -------------------- | ---------------------- | ------------------------------------------ |
| Privacy policies (top 1M sites, 2018) | ~39.8                | ~12.78                 | Far below target of ≥60/≤8                 |
| HIPAA privacy notices                 | ~20–30               | ~14.5                  | Far below target of ≥60/≤8                 |
| Harvard Law Review                    | ~30–35               | ~14–16                 | Appropriate for specialist audience        |
| US Supreme Court briefs               | ~32–42               | ~14                    | Appropriate for specialist audience        |
| Legal contracts (average)             | ~20–30               | ~14–18                 | Far above grade 8 for consumer-facing docs |

---

## Legalese Identification Catalogue

### Here/There/Where- Words: Full Replacement Table

| Avoid                  | Replace With                                               |
| ---------------------- | ---------------------------------------------------------- |
| herein                 | in this [agreement / section / document]                   |
| hereinafter            | [delete; introduce the defined term directly on first use] |
| hereof                 | of this [agreement]                                        |
| hereto                 | to this [agreement]                                        |
| hereunder              | under this [agreement]                                     |
| hereafter / henceforth | from this date; from now on                                |
| heretofore             | until now; previously; before this agreement               |
| therein                | in that; in it                                             |
| thereof                | of that; of it                                             |
| thereto                | to that                                                    |
| thereunder             | under that; under it                                       |
| therewith              | with that; with it                                         |
| wherein                | in which                                                   |
| wherefore              | therefore; for these reasons                               |
| whereby                | by which; under which                                      |
| thereby                | by doing so; as a result                                   |

### Ceremonial Deadwood: Complete Removal List

Remove the following phrases entirely. They add no legal content.

| Remove                                                                                                                                                                 | Notes                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WITNESSETH                                                                                                                                                             | No legal function. Replace with "The parties agree:"                                                                                                                                                      |
| Know all men by these presents                                                                                                                                         | Archaic and sexist. Delete entirely.                                                                                                                                                                      |
| Comes now / Now, comes                                                                                                                                                 | Delete. Begin with the party's name.                                                                                                                                                                      |
| In consideration of the mutual covenants herein contained, and for other good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged | Legally, consideration is established by the parties' obligations; this recital adds nothing except length. Simplify to: "In consideration of the promises set out in this agreement, the parties agree:" |
| IN WITNESS WHEREOF                                                                                                                                                     | Delete or replace with a simple signature block header.                                                                                                                                                   |
| Now, therefore                                                                                                                                                         | Delete the preamble; begin directly with "The parties agree:"                                                                                                                                             |
| by and between                                                                                                                                                         | Between                                                                                                                                                                                                   |
| Made and entered into as of                                                                                                                                            | Replace with effective date statement                                                                                                                                                                     |

### Redundant Doublets and Triplets

Use the single most precise word from the pair:

| Doublet / Triplet            | Use Instead                         |
| ---------------------------- | ----------------------------------- |
| null and void                | void                                |
| cease and desist             | stop                                |
| any and all                  | all                                 |
| each and every               | each                                |
| free and clear               | free; unencumbered                  |
| last will and testament      | will                                |
| terms and conditions         | terms                               |
| rules and regulations        | rules (or regulations — choose one) |
| over and above               | above; more than                    |
| promise, agree, and covenant | agree                               |
| right, title, and interest   | ownership interest                  |
| rest, residue, and remainder | remainder                           |
| give, devise, and bequeath   | give                                |
| null, void, and of no effect | void                                |
| sole and exclusive           | sole (or exclusive — choose one)    |
| signed and sealed            | signed                              |
| order and direct             | order (or direct — choose one)      |
| type and kind                | type                                |
| true and correct             | accurate                            |
| full and complete            | complete                            |

### Latin Phrases: Replace or Preserve

**Replace** (plain equivalent exists and is adequate for most contexts):

| Latin            | Plain Replacement                             |
| ---------------- | --------------------------------------------- |
| inter alia       | among other things                            |
| ab initio        | from the beginning                            |
| arguendo         | for the sake of argument                      |
| ipso facto       | automatically; by that fact alone             |
| mutatis mutandis | with the necessary changes                    |
| in toto          | entirely; in full                             |
| de facto         | in practice; effectively                      |
| vel non          | or not [often just delete]                    |
| viz.             | namely                                        |
| vide             | see                                           |
| nunc pro tunc    | retroactive to [date]; effective as of [date] |
| pari passu       | equally; on equal footing; at the same rate   |
| pro rata         | proportionally; in proportion                 |
| ad hoc           | for this purpose; specially arranged          |

**Preserve** as genuine terms of art (no adequate plain equivalent; significant legal meaning):

| Preserve      | Reason                                                                              |
| ------------- | ----------------------------------------------------------------------------------- |
| habeas corpus | Constitutional writ; specific procedural meaning                                    |
| certiorari    | Appellate procedure; specific legal concept                                         |
| mens rea      | Criminal intent; precise criminal law concept                                       |
| res judicata  | Finality doctrine; specific legal bar                                               |
| estoppel      | Equitable doctrine; no single-word equivalent                                       |
| laches        | Equitable doctrine tied to delay and prejudice                                      |
| mandamus      | Specific writ commanding a government act                                           |
| prima facie   | Widely understood in legal practice; [CONSIDER adding gloss for consumer documents] |
| bona fide     | Widely used in commercial contexts; [CONSIDER adding gloss]                         |

**Action for preserved Latin**: For consumer-facing documents, add a parenthetical gloss
immediately after first use: _"res judicata (the court's previous decision is final and
cannot be relitigated)"_.

### "Shall" Replacement Matrix

| Context                           | Replace "shall" with | Example                                                  |
| --------------------------------- | -------------------- | -------------------------------------------------------- |
| Duty imposed on a party           | must                 | "Buyer must pay the invoice within 30 days"              |
| Contractual promise / future fact | will                 | "Seller will deliver the goods by [date]"                |
| Permission or discretion          | may                  | "Either party may terminate this agreement"              |
| Definition                        | means / is           | "Effective Date means the date this agreement is signed" |
| Prohibition                       | must not             | "The Licensee must not sublicense without consent"       |

### Wordy Phrase Replacements

| Verbose                                 | Plain                                 |
| --------------------------------------- | ------------------------------------- |
| pursuant to                             | under; as required by; according to   |
| in the event that                       | if                                    |
| prior to                                | before                                |
| subsequent to                           | after                                 |
| with respect to / with regard to        | about; on; for                        |
| in accordance with                      | under; following                      |
| for the purpose of                      | to                                    |
| notwithstanding the foregoing           | despite the above; regardless of this |
| to the extent that                      | if; to the degree that                |
| at such time as                         | when                                  |
| in the amount of                        | for; of                               |
| subject to the terms and conditions     | under this agreement                  |
| during the term of this agreement       | while this agreement is in effect     |
| it is agreed by and between the parties | the parties agree                     |
| the party of the first part             | [party's name]                        |
| on or before                            | by                                    |
| in connection with                      | about; in; for                        |

### Nominalization Conversion Table

Convert zombie nouns back into active verbs:

| Nominalization          | Verb Form          |
| ----------------------- | ------------------ |
| make a determination    | determine          |
| conduct an examination  | examine            |
| provide assistance to   | assist; help       |
| give consideration to   | consider           |
| reach an agreement      | agree              |
| make payment            | pay                |
| effect a termination    | terminate          |
| bring a claim           | claim; sue         |
| be in violation of      | violate            |
| provide notification    | notify             |
| make application        | apply              |
| give approval           | approve            |
| form the intention      | intend             |
| grant an exemption      | exempt             |
| take action             | act                |
| have knowledge of       | know               |
| exercise discretion     | decide; choose     |
| undertake an obligation | be obligated; must |

---

## Rewriting Techniques

### Core Principles

**1. Active voice: Name the actor**
Identify who must do what by when. Every obligation clause needs: actor + active verb + object + deadline or condition.

- Passive: "Repairs shall be made within 30 days"
- Active: "The Landlord must make repairs within 30 days"

**2. Use the correct obligation word**

- "Must" for obligations; "may" for permissions; "will" for future facts; "must not" for prohibitions.
- Never use "shall" — it is among the most litigated words in contract law.

**3. Short sentences (target ≤20 words average)**
Break long sentences by:

- Creating two sentences with a period
- Using a colon + vertical list (three or more parallel items)
- Extracting preconditions into a separate sentence

**4. Eliminate throat-clearing**
Remove ceremonial openings ("WITNESSETH," "NOW THEREFORE") and go straight to the obligation.

**5. One idea per sentence**
Compound sentences with multiple conditions should be split into:

- A lead-in sentence stating the main rule
- A list of conditions or exceptions

**6. Use "you" and "we" for consumer documents**
Replace "the Tenant," "the Applicant," "the Consumer" with "you" and "we" throughout.
Exception: formal contracts between businesses should retain third-person party names.

**7. Move definitions to the end (for consumer documents)**
Front-loaded definitions sections impede reading. Define terms at first use with a
parenthetical, then reference a glossary at the end for full definitions.

**8. Use tables for comparative or conditional information**
Conditions, fee schedules, permitted uses, and exceptions are clearer as tables than
as narrative paragraphs.

### When NOT to Simplify

**Category 1: Capitalized defined terms in effect**
Once a term is defined and capitalized, use it consistently. Never substitute a synonym
mid-document — this destroys the definitional structure and can shift legal meaning.

**Category 2: Statutory language that must track the statute**
Regulated industries (financial services, healthcare, employment) often require exact
statutory language. Changing the words may change the legal effect. Quote exactly;
add a plain-language summary after if needed.

**Category 3: Precision-loaded commercial terms**
These terms have specific legal consequences that plain synonyms do not capture:

- "best efforts" (unlimited obligation) vs. "commercially reasonable efforts" vs.
  "reasonable efforts" (graduated obligations — courts distinguish them)
- "time is of the essence" (makes deadlines strict conditions; breach entitles termination)
- "notwithstanding any other provision" (conflict resolution mechanism — do not delete)
- "material breach" (triggers termination rights in most governing law frameworks)
- "irrevocable" (cannot be undone — precision matters)

**Category 4: Terms of art with genuine legal content**
See the PRESERVE list in the Legalese Identification Catalogue above.

---

## Severity Classification System

### Document-Level Severity

Classify the document as a whole after scoring:

| Classification   | Flesch RE (general public target) | FK Grade | Meaning                                                            | Action                                                                                                          |
| ---------------- | --------------------------------- | -------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **CLEAR**        | ≥60                               | ≤8       | Meets or exceeds the target for the declared audience              | AUDIT: No action needed. REWRITE: No scope.                                                                     |
| **READABLE**     | 45–59                             | 9–10     | Within range; some improvements available                          | AUDIT: Flag SHOULD-SIMPLIFY items. REWRITE: Target MUST-SIMPLIFY items.                                         |
| **COMPLEX**      | 30–44                             | 11–13    | Substantially below target; significant legalese present           | AUDIT: Prioritize finding catalogue by severity. REWRITE: Full treatment.                                       |
| **INACCESSIBLE** | <30                               | ≥14      | Impenetrable to the intended audience; fundamental rework required | AUDIT + REWRITE: Treat as full rewrite project; may need structural reorganization, not just word substitution. |

_Note: Adjust thresholds for specialist audiences using the Audience Target Scores table._

### Finding-Level Classification

Each individual finding is classified as:

| Classification  | Symbol | Meaning                                                           |
| --------------- | ------ | ----------------------------------------------------------------- |
| MUST-SIMPLIFY   | 🔴     | Comprehension barrier; plain equivalent exists; no precision loss |
| SHOULD-SIMPLIFY | 🟡     | Clear improvement; minor or no precision trade-off                |
| CONSIDER        | 🔵     | Optional; judgment call; minimal score impact                     |
| PRESERVE        | ✅     | Do not change; legal precision requires exact wording             |

---

## Jurisdictional Compliance Requirements

| Jurisdiction  | Law                                      | Document Type                                            | Standard                                                 | Score Threshold                                             |
| ------------- | ---------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- |
| US Federal    | Plain Writing Act 2010 (Pub. L. 111-274) | Government documents to public                           | Plain, clear, concise                                    | No numerical score; qualitative                             |
| US Federal    | SEC Rule 421(d) (1998)                   | Prospectus cover, summary, risk factors                  | 6 plain English principles                               | No numerical score; qualitative                             |
| US Federal    | CFPB TRID (2015)                         | Mortgage disclosures (Loan Estimate, Closing Disclosure) | Standardized plain forms                                 | Standardized form compliance                                |
| US Federal    | 45 CFR 46 / 21 CFR 50                    | Informed consent forms                                   | Understandable to the subject                            | Target grade 6–8 per IRB standard                           |
| New York      | Gen. Obligations Law §5-702              | Consumer contracts ≤$50,000                              | Grade 8 or lower; min. 8pt type                          | FK grade ≤8 [VERIFY current enforcement]                    |
| New Jersey    | N.J.S.A. 56:12-1                         | Consumer contracts                                       | Plain language + style requirements                      | Qualitative + structural                                    |
| Pennsylvania  | Insurance Code                           | Insurance policies                                       | FK grade ≤9                                              | FKGL ≤9                                                     |
| Florida       | Insurance Code                           | Insurance policies                                       | Flesch RE ≥45                                            | FRE ≥45                                                     |
| Connecticut   | Insurance regulations                    | Insurance policies                                       | Flesch RE ≥45                                            | FRE ≥45                                                     |
| 30+ US states | Various insurance codes                  | Insurance policies                                       | Flesch RE ≥40–50 (varies by state)                       | [VERIFY specific state threshold]                           |
| EU            | Dir. 93/13/EEC                           | Consumer standard terms                                  | Plain, intelligible; economic consequences clear         | Qualitative                                                 |
| EU            | GDPR Art. 12(1)                          | Privacy notices                                          | Clear and plain language; child-appropriate for children | Qualitative; target ≥60 FRE best practice                   |
| EU            | EU AI Act Art. 50                        | AI system disclosures                                    | Clear disclosure in plain language                       | Qualitative                                                 |
| UK            | Consumer Rights Act 2015                 | Consumer contracts                                       | Plain and intelligible; prominent                        | Qualitative                                                 |
| UK            | FCA Consumer Duty 2023                   | Financial services communications                        | Clear, fair, not misleading; no jargon                   | Qualitative; FCA may publish specific guidance [VERIFY]     |
| South Africa  | CPA 68 of 2008 s.22                      | All consumer-facing documents                            | Understandable without undue effort                      | Qualitative; considers vocabulary, structure, illustrations |
| Australia     | ACL 2011                                 | Consumer contracts                                       | Unfair terms fairness; plain language practice           | Qualitative                                                 |
| International | ISO 24495-1:2023                         | Any text-based document                                  | Relevance, Findability, Understanding, Usability         | 4-pillar framework                                          |
| International | ISO 24495-2:2025                         | Legal communications                                     | Guidelines for legal plain language                      | Substantive guidance                                        |

**[VERIFY]** all threshold values before citing in a compliance assessment — statutes and
regulations are amended. Use legalcode-mcp or official government sources to confirm current
requirements.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify document type, audience, compliance jurisdiction, and any user-provided
preservation list. Classify the baseline readability severity (CLEAR / READABLE / COMPLEX /
INACCESSIBLE). Identify which pattern categories are most heavily present.

**DO**: Systematically apply the Legalese Identification Catalogue. Populate the Finding
Register. Apply rewrites (REWRITE mode).

**CHECK**: Run Citation Quality Gates. Verify all PRESERVE designations via 3-pass
Self-Interrogation. Re-score post-rewrite. Run compliance assessment if applicable.

**ACT**: Note any provisions where legal precision constrains further simplification.
Flag them for qualified counsel review. Append Glass Box audit trail.

### Citation Quality Gates

Run these 5 gates silently before delivering any compliance citation. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                       | Fail Action                         |
| -------------- | -------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every statutory citation names the specific law, section, and jurisdiction | Add citation or mark "[UNVERIFIED]" |
| **Format**     | Citations follow a consistent, recognizable format                         | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal                     | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Compliance assessment stays within the declared governing law scope        | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden                                  | Add confidence qualifier            |

### Self-Interrogation for PRESERVE Designations

For any item designated PRESERVE that is not on the Automatic PRESERVE Triggers list, apply
this 3-pass test:

**Pass 1 — Substitution Test**: Is there truly no plain English substitute that carries
the same legal meaning? Search the legalese catalogue and consider paraphrase options.
Would a court in the governing jurisdiction recognize a plain substitute as equivalent?

**Pass 2 — Audience Test**: Even if legal precision requires the exact term, can a
parenthetical gloss be added for the lay audience without changing the operative clause?
If yes, the answer is PRESERVE + GLOSS, not simple PRESERVE.

**Pass 3 — Context Test**: Is this term actually functioning as a term of art here, or is
it being used loosely? (Example: "bona fide" is sometimes used as mere emphasis — "a bona
fide effort" — where "genuine" would be both more readable and equally precise.)

If any pass reveals a substitution is possible, reclassify from PRESERVE to SHOULD-SIMPLIFY
or CONSIDER, and update the Finding Register.

### Confidence Scoring

| Level        | Range     | Meaning                           | Action                                     |
| ------------ | --------- | --------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law, clear statute        | State with confidence                      |
| **High**     | 0.80–0.94 | Strong authority, minor questions | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good arguments; could differ      | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain               | Flag for professional review               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative           | Do not assert; flag "[UNCERTAIN]"          |

Apply Confidence Scoring to:

- Every regulatory compliance determination ("This document meets the Florida insurance
  standard" should be Definite/High or not made)
- Every PRESERVE determination for genuine terms of art (is this truly a term of art?)
- Any rewrite where precision equivalence is not certain

---

## Prioritization Framework

When there are many findings, prioritize rewrites in this order:

### Priority 1 — Compliance-Blocking (Address First)

Findings that cause the document to fail a statutory plain language requirement. These are
non-negotiable if the document must comply.

- Text scoring below the applicable regulatory floor (e.g., FL/CT insurance Flesch RE <45)
- Missing mandatory disclosures or headings required by the applicable standard
- Ambiguous obligation terms in consumer contracts subject to §5-702 or equivalent

### Priority 2 — Comprehension Barriers (Material Impact)

MUST-SIMPLIFY items that will cause comprehension failures for the target audience:

- Obligation clauses in passive voice (target audience cannot identify who owes the duty)
- "Shall" in obligation clauses (ambiguous; may be misread as permissive)
- Sentences >40 words
- Archaic ceremonial language throughout the document
- Latin phrases with no parenthetical gloss for general audiences

### Priority 3 — Readability Improvements (Score Improvement)

SHOULD-SIMPLIFY items that measurably improve the readability score:

- Sentences 25–40 words
- Nominalizations and wordy prepositional phrases
- Redundant doublets
- here/there/where- words

### Priority 4 — Polish (Optional)

CONSIDER items with minimal score impact:

- Stylistic improvements
- Optional restructuring
- Alternative phrasing where current text is already adequate

---

## Anti-Patterns

Explicit catalogue of what NOT to do when applying plain language to legal text:

1. **Simplifying defined terms after introduction** — Once "Intellectual Property Rights" is
   defined, replacing it with "IP" or "intellectual property" mid-document destroys the
   definitional chain. Always use the defined term consistently after introduction.

2. **Replacing precision-loaded terms with vague equivalents** — "Commercially reasonable
   efforts" and "best efforts" are different legal standards with different case law. Replacing
   one with "reasonable efforts" to improve readability changes the substantive obligation.
   This is a legal error disguised as a readability improvement.

3. **Adding readability without removing legalese** — Adding short headings and bullet points
   while leaving walls of legalese unchanged produces a document that looks accessible but
   still fails readability tests. Address the sentence-level language, not just the structure.

4. **Assuming all passive voice is always wrong** — Federal plain language guidance recognizes
   valid passive voice uses: when the actor is unknown, when the result (not the actor) is the
   sentence's focus, in legislative/regulatory findings of fact. Flag passive voice in obligation
   clauses but do not mechanically convert all passive constructions.

5. **Auto-converting "shall" to "must" everywhere** — "Shall" can be mandatory (→ must),
   permissive (→ may), or descriptive of a future fact (→ will). Converting every instance to
   "must" changes permissive provisions to mandatory ones — a substantive error. Parse each
   use before converting.

6. **Stripping "notwithstanding" clauses** — "Notwithstanding any other provision of this
   agreement" is a conflict-resolution mechanism. Deleting it removes a priority rule. Replace
   with "Despite anything else in this agreement" — do not delete.

7. **Readability score gaming** — Artificially shortening sentences to hit a Flesch RE threshold
   while creating choppy, incomplete thoughts. The score is a proxy for comprehension; chasing
   the number without improving actual clarity defeats the purpose.

8. **Glossing defined terms mid-document** — Adding a parenthetical plain-language gloss every
   time a defined term appears creates clutter and inconsistency. Add the gloss at first use
   and first use only; after that, use the term alone.

9. **Changing the legal precision of limitation clauses** — "Consequential damages," "indirect
   damages," and "special damages" are often defined by case law or the contract's definitions
   clause. Replacing them with "damages you couldn't have expected" changes the scope of the
   exclusion and may affect enforceability under UCTA or equivalent [VERIFY per jurisdiction].

10. **Over-simplifying force majeure triggers** — "Events beyond a party's reasonable control"
    is legally different from "acts of God" or a specific enumerated list. The scope determines
    what excuses performance. Simplifying the language without preserving the scope is a
    substantive change.

11. **Using "you" and "we" inconsistently** — If the decision is made to use second-person
    in a consumer document, apply it throughout. Mixing "you" in some sections and "the
    Customer" in others creates confusion about which obligations are the reader's.

12. **Deleting consideration recitals in consumer contracts** — Some jurisdictions treat
    the presence of a consideration clause as relevant evidence. The language should be
    simplified, not deleted.

13. **Applying readability scores to sentence fragments** — Definitions sections, headings,
    signature blocks, and short listed items artificially inflate readability scores when
    included in the corpus. Score the operative language (obligations, representations,
    conditions) separately from structural elements.

14. **Reporting compliance without verification** — Stating "this document complies with
    the Florida insurance readability requirement" without verifying the current threshold
    and the correct scoring methodology. Always mark regulatory compliance determinations
    with a confidence score and [VERIFY] if not confirmed against an authoritative source.

15. **Treating readability as the only accessibility goal** — Plain language also involves
    document design: type size, line length, white space, heading hierarchy, and the use of
    tables and visuals. A document can achieve Flesch RE 65 but still be inaccessible due
    to 6-point type, no headings, and a single unbroken paragraph. Flag design issues
    separately from language issues.

16. **Preserving legalese in consumer correspondence** — Letters and emails from lawyers to
    clients are not exempt from plain language standards. The same principles apply: name
    the actor, use short sentences, avoid doublets, and explain technical terms.

17. **Ignoring structural problems** — Sometimes a provision is incomprehensible not because
    of its words but because of its logical structure: nested conditions, multiple exceptions to
    exceptions, and circuitous "provided that" chains. Readability scoring will not catch
    these. Analyze logic, not just vocabulary.

---

## Writing Standards

Apply plain-language discipline to the plain-language output itself:

**For the audit report and finding catalogue:**

- Describe each finding in active voice: "Section 3.2 uses passive voice in an obligation
  clause" not "Passive voice was detected."
- Be specific: quote the exact text, cite the exact section, state the exact issue.
- Score first, qualitative assessment second. Never lead with an unsupported conclusion.

**For rewritten provisions:**

- The rewrite must be shorter than or the same length as the original (never longer).
- No meta-commentary in the rewrite itself (no "[simplified version]" labels within the text).
- Legal terms retained as PRESERVE must appear exactly as in the original.
- Use consistent terminology within each rewritten provision.

**Quality gates before delivery:**

1. Can the target audience read and act on the rewritten provisions without external help?
2. Does every rewritten provision carry the same legal obligation as the original?
3. Is every PRESERVE designation justified in the Finding Register?
4. Is every compliance determination backed by a specific statutory citation (or marked [VERIFY])?
5. Has the post-rewrite readability score been computed and compared to both the audience
   target and any applicable regulatory floor?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool for
verifying jurisdictional plain language mandates, current statutory requirements, and case law
on plain language enforceability.

**With legalcode-mcp connected (preferred):**

- Verify current plain language statutes for the applicable jurisdiction (thresholds are
  amended; do not rely on memory)
- Check for recent plain language enforcement actions or case law (GDPR Art. 12 enforcement;
  FCA Consumer Duty decisions; state insurance regulator actions)
- Confirm whether specific document types are subject to mandatory plain language requirements
  in the governing jurisdiction
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory threshold citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on the structural and linguistic analysis rather than regulatory compliance
  determinations
- Flag any compliance assessment as [PROVISIONAL — verify current statutory thresholds
  against authoritative sources before relying on this assessment]

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Plain Language Report

**Document**: [title / identifier]
**Document Type**: [consumer contract / insurance policy / privacy policy / etc.]
**Target Audience**: [audience tier]
**Mode**: [AUDIT / REWRITE]
**Compliance Jurisdiction**: [if applicable, or "Best practice — no specific mandate identified"]
**Date of Analysis**: [date]

---

## Baseline Readability Scorecard

| Metric                      | Score                             | Audience Target | Status                                  |
| --------------------------- | --------------------------------- | --------------- | --------------------------------------- |
| Flesch Reading Ease         | [score]                           | ≥[target]       | 🔴 INACCESSIBLE / 🟡 COMPLEX / 🟢 CLEAR |
| Flesch-Kincaid Grade        | [grade]                           | ≤[target]       | [status]                                |
| Gunning Fog Index           | [score]                           | ≤[target]       | [status]                                |
| SMOG Index                  | [score or "N/A — < 30 sentences"] | ≤[target]       | [status]                                |
| Coleman-Liau Index          | [score]                           | ≤[target]       | [status]                                |
| Avg Sentence Length (words) | [avg]                             | ≤20             | [status]                                |
| Avg Syllables per Word      | [avg]                             | ≤1.5            | [status]                                |
| Word Count                  | [count]                           | —               | —                                       |
| Sentence Count              | [count]                           | —               | —                                       |

**Document Severity**: [CLEAR / READABLE / COMPLEX / INACCESSIBLE]

---

## Compliance Assessment [if applicable]

| Mandate              | Requirement             | Baseline Status                       | Post-Rewrite Status |
| -------------------- | ----------------------- | ------------------------------------- | ------------------- |
| [Statute / standard] | [threshold or standard] | [COMPLIANT / PARTIAL / NON-COMPLIANT] | [status]            |

---

## Finding Register

| #   | Section | Pattern Category | Exact Text | Classification     | Notes    |
| --- | ------- | ---------------- | ---------- | ------------------ | -------- |
| 1   | [§X.X]  | [Category]       | "[quote]"  | 🔴 MUST-SIMPLIFY   | [note]   |
| 2   | [§X.X]  | [Category]       | "[quote]"  | 🟡 SHOULD-SIMPLIFY | [note]   |
| 3   | [§X.X]  | [Category]       | "[quote]"  | ✅ PRESERVE        | [reason] |
| ... |         |                  |            |                    |          |

**Summary:**

- 🔴 MUST-SIMPLIFY: [N] items
- 🟡 SHOULD-SIMPLIFY: [N] items
- 🔵 CONSIDER: [N] items
- ✅ PRESERVE: [N] items

---

## Rewrites [REWRITE mode only]

[For each MUST-SIMPLIFY and SHOULD-SIMPLIFY item:]

**Finding [#]** | [Pattern Category] | 🔴/🟡

- **Section**: [§X.X]
- **Original**: "[exact quoted text]"
- **Rewritten**: "[plain alternative]"
- **Technique**: [active voice / doublet elimination / sentence split / etc.]
- **Precision note**: [No change to legal meaning / OR: [specific trade-off — flag for counsel]]

---

## Post-Rewrite Scorecard [REWRITE mode only]

| Metric               | Before   | After   | Δ Change | Target Met? |
| -------------------- | -------- | ------- | -------- | ----------- |
| Flesch Reading Ease  | [before] | [after] | [+/-N]   | [Yes / No]  |
| Flesch-Kincaid Grade | [before] | [after] | [+/-N]   | [Yes / No]  |
| Gunning Fog          | [before] | [after] | [+/-N]   | [Yes / No]  |
| Avg Sentence Length  | [before] | [after] | [+/-N]   | [Yes / No]  |

---

## Recommendations

[Summary of key findings and recommended next steps. For AUDIT mode, this is the action plan.
For REWRITE mode, this covers any items requiring qualified counsel review.]

---

## Glass Box Audit Trail

[See Glass Box Audit Trail Template below]
```

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-plain-language"
  mode: "AUDIT / REWRITE"
  document_type: "[consumer contract / insurance policy / etc.]"
  target_audience: "[audience tier]"
  compliance_jurisdiction: "[jurisdiction or 'None specified']"

  baseline_scores:
    flesch_reading_ease: "[score]"
    fkgl: "[grade]"
    gunning_fog: "[score]"
    smog: "[score or 'N/A — insufficient sentences']"
    coleman_liau: "[score]"
    avg_sentence_length_words: "[avg]"
    document_severity: "CLEAR / READABLE / COMPLEX / INACCESSIBLE"

  post_rewrite_scores: # REWRITE mode only; omit for AUDIT
    flesch_reading_ease: "[score]"
    fkgl: "[grade]"
    gunning_fog: "[score]"
    audience_target_met: "Yes / No"
    regulatory_floor_met: "Yes / No / Not applicable"

  findings_summary:
    must_simplify: "[N]"
    should_simplify: "[N]"
    consider: "[N]"
    preserve: "[N]"
    rewrites_produced: "[N or 'Not applicable (AUDIT mode)']"

  compliance_assessments:
    - mandate: "[Statute or standard]"
      determination: "COMPLIANT / PARTIAL / NON-COMPLIANT"
      confidence: "[Definite / High / Probable / Possible / Unlikely]"

  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED — marked [VERIFY]]"

  precision_flags:
    - "[Any provision where rewrite changed or may have changed legal meaning — flag for counsel]"

  self_interrogation_preserve:
    items_challenged: "[N PRESERVE items put through 3-pass test]"
    reclassified: "[N reclassified after failing Self-Interrogation]"

  confidence: "HIGH / MEDIUM / LOW — [rationale]"

  limitations:
    - "[Any scope limitations: short text / SMOG insufficient sentences / etc.]"
    - "[Regulatory compliance determinations require verification against current authoritative sources]"

  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Localization Notes

For jurisdiction-specific variants, research and apply:

**US State Insurance Mandates [VERIFY current thresholds per state]:**

- Each state's insurance code specifies the applicable readability formula, minimum score,
  and which documents are covered. Over 30 states have enacted requirements; 18 states
  currently have none. Verify the specific state's insurance department requirements before
  rendering a compliance determination.

**GDPR / UK GDPR Privacy Notices:**

- "Clear and plain language" is a qualitative standard; no numerical threshold is set.
- For children's services, the privacy notice must use child-appropriate language — typically
  grade 6 or below.
- Post-GDPR research (2023) found that privacy policy readability did not improve substantially
  despite the mandate; regulators have not heavily enforced the language clarity provision.
  This does not mean non-compliance is low-risk — it means enforcement has lagged.

**ISO 24495-2:2025 (Legal Communications):**

- Published August 2025. The standard applies to any legal document and establishes guidelines
  for ensuring readers can act on legal communications without external assistance.
- The standard is not a statutory mandate in itself but may be adopted by reference by courts
  or regulators assessing "understandability."

**Non-English Documents:**

- Readability formulas are calibrated for English. Equivalent formulas exist for German
  (Lesbarkeitsindex / LIX), French (Flesch adaptation), and other languages.
- [JURISDICTION-SPECIFIC] Where a multilingual jurisdiction requires plain language in both
  English and a local language (e.g., South Africa's 11 official languages; Welsh/English in
  Wales), apply equivalent local-language scoring.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- US Plain Language Action and Information Network (PLAIN) Federal Plain Language Guidelines
- ISO 24495-1:2023 and ISO 24495-2:2025 (plain language in legal communications)
- SEC Rule 421(d) plain English requirements (1998)
- Bryan Garner, _Legal Writing in Plain English_ (2nd ed.) — shall/must/may framework and
  nominalization analysis
- Richard Wydick, _Plain English for Lawyers_ — sentence length and structure guidance
- Singapore Law Reform Committee, _Plain English for Latin Expressions_ (2025)
- US PLAIN / CFPB / FDA plain language guidance
- State insurance plain language mandates (FL, CT, PA, NY, NJ) — [VERIFY current thresholds]
- FCA Consumer Duty 2023 (UK)
- GDPR Article 12(1) (EU)
- Legalcode repository quality frameworks adapted from legalcode-contract-review reference standard
