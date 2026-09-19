# Form, inputs and drafting choices

Read this when choosing a base, constructing the template or changing its input contract.

## Inspect the actual form

Prefer an approved blank precedent or maintained template over reconstructing one from negotiated documents. Otherwise select the sample that best represents the intended form; recency alone does not establish approval. Read the documents end to end, including headers, footers, notes and attachments. Record identifying details for the later package review.

Inspect whether appearance comes from named styles, direct run formatting, tables, text boxes, sections, page breaks or fixed positioning. Inspect numbering, fields, repeated headers and footer relationships. The styles alone may not carry the form. Preserve approved firm branding; party identities vary with the matter. Where the intended firm identity is unresolved, keep an explicit placeholder rather than silently choosing one.

The supplied helpers target ordinary DOCX packages using standard `word/document.xml` parts and conventional `w:` markup. Their text edits are not a general OOXML conversion engine. For unsupported structures, complex drawings, PDFs or other source types, use suitable available tools and document approximations. Prefer the source DOCX to reconstructing its PDF. Preserve originals and verify converted layout; do not label inferred PDF formatting an exact recovery.

## Decide what is reusable

With multiple completed documents, `compare_samples.py` offers candidates:

| Label | Investigate | Usual representation |
|---|---|---|
| FIXED | House wording or a coincidental shared fact? | Approved wording stays; shared years, staff or rate cards may still vary |
| SLOTTED | Which differing words come from inputs? | Named blanks with explicit transformations |
| REWRITTEN | What job does the passage perform? | A passage blank with drafting guidance |
| OPTIONAL | Is there a supported selection condition? | A choice, with an unresolved condition left explicit |
| ONLY | Bespoke content, a concession or one of several alternatives? | Remove matter content; retain supported alternatives |

With one sample, use the same distinctions by reading and mark uncertainty. A difference between signed contracts does not establish the firm's preferred position or authority to concede. Record accepted negotiations as observations; use the lawyer's confirmed preference to select an opening position or fallback.

For each nontrivial field or decision, map the input source to output locations, required form, transformation, dependencies and missing-value behaviour. A paired intake form and completed document can reveal this mapping directly. For alternatives, record the preferred option, acceptable alternatives and selection conditions only where supported. Keep a compact conflict record: instruction, contrary evidence, resolution or open question.

Support inflection and agreement explicitly. Distinct grammatical cases and sentence-initial capitalisation can need distinct blanks; the script does not infer them. Identify derived dates, totals, clause numbers and cross-references. The generator substitutes values; it does not calculate or guarantee updated Word fields. Compute only from an explicit supported rule and verify the result in the delivered document.

## Build a usable template

The template should show the whole intended framework, approved standard wording and notes where prose must be written. For a memo, opinion or pleading, remove the old matter's narrative, argument, authorities and conclusions. Keep neutral section functions and supported headings or alternatives. Do not force every possible heading into every new matter.

`make_template.py --help` describes `edits.json`. Edits run in this order: paragraph deletions, paragraph replacements, insertions, string replacements. Paragraph selectors match the first containing paragraph, case-sensitively. Insertions can anchor on earlier edits. Strings written by an edit are final and are not processed by later string replacements. Use distinct anchors and read the output; ambiguous matches can target the wrong paragraph.

Replaced paragraphs inherit paragraph and first-run formatting. Mark **bold**, *italic* and __underline__ explicitly where a rewritten paragraph needs different inline emphasis. Insertions can use `"like"` to copy another paragraph's formatting. Preserve empty paragraphs and page breaks that serve layout; explain an intentional removal of a break belonging only to the old matter.

Use the document's language for blanks and notes:

- `[Name]` is a value; `[Name: what belongs here]` includes guidance. Notes must not contain square brackets and the whole bracketed expression must fit the helper's 700-character limit. Missing values stay visibly highlighted.
- A paragraph beginning `[IF choice]` is kept for true, removed for false and left marked when undecided. The marker also works at the start of a line within a paragraph. Supported equivalents include `EF`, `HVIS`, `OM`, `WENN`, `FALLS`, `SI`, `SE`, `JOS` and `ALS` in capitals.
- `[IF NOT choice]` uses the same positive key and represents its false branch. Supported negative forms include `EKKI`, `IKKE`, `INTE`, `NICHT`, `PAS`, `NO`, `EI` and `NIET`. If removing a clause changes nearby grammar, explicitly model both supported sentence forms.
- Lists of strings repeat the containing paragraph or row; lists of objects repeat adjacent paragraphs containing those field names. Give list fields names used nowhere else. An empty list removes the block. The generator processes choices, lists, then scalar values.
- Instruction paragraphs begin with `[NOTE]` or a supported translated marker shown in `--help`. With `"instruction": true` they appear in grey italics in the template and are removed from generated documents. Use them where a passage note cannot hold the necessary advice.

Keep new clauses and alternatives tied to source evidence or the lawyer's instructions. A template structure is not permission to invent substantive terms.

## Package the input contract

Keep a small field table in the generated SKILL.md. Move complex section and clause-selection rules to `references/drafting-rules.md`, linked with an explicit loading condition. Add `examples/values.json` when a runnable synthetic example clarifies lists, branches or dependent values. Match actual marker names; never use a completed client's values as sample data.

Copy `assets/create_docx.py` unchanged into the generated skill unless a demonstrated template requirement justifies adapting and testing it. It refuses to replace an existing output unless `--force` is supplied, and never replaces its template. Use a fresh filename for a revised draft unless replacing that draft is intended.

For fixed forms the template does most of the work. Heavily negotiated agreements need an approved precedent and confirmed positions. Opinions and pleadings need new-matter reasoning and authorities. Execution requirements such as signing authority or registry requirements are substantive inputs, not something inferred from visual similarity.
