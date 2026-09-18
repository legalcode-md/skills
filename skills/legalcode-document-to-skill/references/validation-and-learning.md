# Validate the package and learn from revisions

Read this before delivery and when incorporating samples, feedback or edits.

## Check the generated instructions

Before first delivery or after a substantial instruction change, apply the delivery check in [skill-authoring-practices.md](skill-authoring-practices.md). Check the actual generated entrypoint and supporting files, including their activation scope and loading directions. Record material exceptions and why the document requires them; a valid file structure alone does not establish good skill behaviour.

## Check matter isolation

Search the completed package for the identifying details recorded during intake: names, abbreviations, inflected forms, addresses, matter identifiers, dates, amounts and distinctive factual descriptions. Read it for old-matter arguments and conclusions that a name search will miss. Review writing-profile examples and JSON examples as well as the template and SKILL.md. Approved firm identity is different from a previous client's identity.

Review DOCX contents beyond printed text. Inspect XML text and attributes, relationships, retained links, notes and media. Check that logos are authorised house assets and that retained images do not contain old matter details. Do not distribute original client documents or identifying source paths as part of a reusable shared package.

`make_template.py` removes supported tracked changes, directly hidden runs, comments and selected metadata, relationships and parts. It refuses documents whose styles/defaults declare hidden text because inherited visibility is not resolved by this cleaner. Resolve that in a reviewed working copy before proceeding. The tool is not a complete anonymiser: arbitrary attributes, retained images, fields and unsupported structures require review. A successful exit and clean visible text do not prove that the package contains no client data.

## Exercise the delivered workflow

Use the generated folder and its actual documented generation command. An ordinary trial should fill relevant fields and include representative prose. Add cases only where needed to cover meaningful alternatives, repeated blocks of different lengths, missing inputs or longer text affecting pagination. Mutually exclusive choices cannot all be validated by one completed document.

A held-back sample can be useful if sufficient representative evidence remains. If it is used to derive the trial brief or fix the skill, state that limitation; subsequent tests are no longer independent of it. Synthetic new-matter facts also work. Supply the reasoning, positions and authority needed for a legal-writing trial rather than asking the style profile to invent them.

A fresh reader or separate agent can test whether the package is self-contained when delegation is available and authorised. Otherwise use a focused self-check and state that it was not independent. Record actual gaps without a quota. A tester's suggestion is feedback, not evidence of house practice. Resolve it against the sources or the lawyer's instruction.

Evaluate these properties separately:

| Property | Evidence |
|---|---|
| Functional behaviour | Fields fill; unresolved choices remain visible; optional blocks and repeated items behave as documented; computed values and references are correct |
| Form | Template and output retain intended typography, layout, sections, numbering, headers and footers |
| House writing | Perspective, vocabulary, phrasing, paragraph development and contextual tone follow supported patterns |
| Professional quality | Precise, coherent, grammatical, consistent and appropriate to the recipient, with restrained claims of certainty |
| Meaning | Attribution, factual status, legal modality, conditions, exceptions and conclusions remain supported |
| Matter isolation | No old-matter facts, conclusions or identifying details survive in reusable material |

`inspect_docx.py --compare` checks a subset of declared formatting. Exit 1 reports detected differences for investigation; differences can be intentional when sections are omitted. Exit 0 does not establish identical appearance. It compares defaults, common style values and styles used only in one document, numbering summaries, first-section page geometry, header/footer feature summaries and the set of direct formatting signatures. It does not compare complete page layout, all section details, image placement or font substitution.

Render and inspect source and trial using suitable available tools when appearance matters. Check page breaks, letterhead, tables, long passages, signatures and numbering. Word and other renderers can differ; identify the renderer used. If rendering is unavailable, report exactly what was checked and leave visual fidelity unverified. Do not delegate an available check merely because the responsible lawyer will also review the draft.

For substantial writing guidance, a useful comparison is the same brief drafted with and without the profile, holding facts, template and substantive instructions constant. Assess the result against the house samples, not the evaluator's preferred style. Use plausible alternatives; generic polish is insufficient evidence of fidelity. Such a comparison is warranted when the added guidance's value is uncertain, not for every small wording edit.

Repair the package rather than only correcting the trial output. Rerun affected checks, including writing checks after material profile changes. Keep the handover accurate about what passed, what failed and what remains untested. Do not claim improved lawyer-specific writing quality from script tests alone.

## Incorporate approved revisions

Compare the skill's draft with the lawyer's accepted revision and classify each meaningful edit:

- Fact correction or changed matter instruction: update the matter; do not learn a general style rule.
- Substantive legal or negotiation change: confirm its intended reusable scope before changing a precedent or decision rule.
- Template correction: repair the layout or input contract and test affected output.
- Reusable style preference: propose or apply the supported rule within the user's authorised update scope, with its audience and document context.

Keep a compact candidate-rule record in private working material: sanitised before/after example, classification, proposed instruction, scope, reason, supporting occurrences, status and version changed. Repetition strengthens evidence but does not automatically make a permanent firm-wide rule. Preserve accepted versions so changes can be reversed. Do not run background learning or store whole private drafts in the shared package.

Update the canonical home of the rule: template for operative wording, writing profile for expression, drafting rules for choices. Resolve conflicts with existing instructions; do not append a growing list of exceptions or forbidden phrases. Distinguish the date of the samples, the profile update and any actual legal verification.
