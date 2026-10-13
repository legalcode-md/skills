# PowerPoint examples and drafting skills

Read this for `.pptx` sources or a generated presentation skill. PPTX can supply
both writing evidence and the reusable house presentation template. For legacy
`.ppt`, re-save as `.pptx` in a suitable presentation editor first. Preserve the
original and check the conversion. Do not pass PPTX to the DOCX helpers.

## Inspect and learn

Use `scripts/inspect_pptx.py` for slide order, dimensions in EMUs, shape text and
positions, backgrounds, fill/outline declarations, fonts, text formatting, theme
schemes, layout/master/theme inheritance links, hidden slides, notes and an
inventory of retained parts. `--text --include-notes` exposes speaker notes separately; `--json` writes
the inspection to a private working file. The inspector does not render, OCR
images, extract chart datasets or prove that a package is sanitised.

Render the deck with an available local presentation editor or renderer. Learn
the slide sequence, slide roles, title hierarchy, content density, typography,
colour palette, alignment, margins, recurring diagrams and citation placement.
Inspect masters, layouts and themes as well as direct formatting. XML shape order
may differ from visual reading order. Grouped shapes and overlapping text need
visual review. An image-only slide needs local OCR or manual reading; report any
unread content. Do not treat a blank text extraction as an empty slide.

The report's `design_sources` follows each slide's layout, master and theme links.
`style_sources` records declarations at each source, including direct font names,
theme font references, font sizes, colours and background fills. These declarations
are evidence for the house form; the inspector does not resolve every inherited
property or font substitution into its final rendered value.

`compare_samples.py a.pptx b.pptx` compares text from displayed slides in actual
presentation order, including table cells. It excludes hidden slides and notes;
use the inspector to review those separately. It does not compare slide layouts
or reliably pair slides that have moved. Mixed DOCX/PPTX/PDF samples can contribute
writing evidence; keep each medium's layout rules distinct.

Learn concise slide phrasing and narrative speaker prose separately. Notes may
contain private rehearsal material or substantive facts; they are not automatically
approved audience text. Record when speaker notes belong in the new output.

## Prepare the presentation template

Prefer an approved blank deck, or build the template from a sanitised copy of the
representative source PPTX. Preserve the source's complete house design:

- Slide backgrounds, including solid, gradient and image fills, whether applied
  directly or inherited from layouts and masters.
- Theme colour palettes and colour mappings, text/shape colours, outlines, fills,
  effects and transparency. Keep theme references so inherited colours continue
  to behave as the source intended.
- Font families and theme fonts, sizes, weight, italics, bullets, spacing,
  alignment, text-box margins and fitting behaviour. Retain embedded font parts
  where supplied and authorised.
- Slide dimensions, masters, layouts, placeholder roles, positions, logos,
  approved background images and other reusable graphical assets.

Retain these in `template.pptx`; descriptions of the design are not a substitute
for bundling the actual reusable form. Filling blanks must use that template.
When additional slides are needed, use the corresponding house layout or a
reviewed copy of the matching source slide, preserving its inheritance and assets.
Do not silently substitute a generic theme, recreate a blank deck or flatten the
slides into screenshots. Record deliberate design changes requested by the user.
Remove old-matter details without discarding approved house backgrounds or branding.
If identifying content is baked into a background image, replace that asset with
a sanitised equivalent and review the result.

Check that the target renderer has the required fonts or can use the deck's
embedded fonts. If a font is unavailable, report the substitution or seek a material
choice; do not claim an exact match. Where useful, bundle learned design rules in
`references/presentation-style.md` and link them from the generated skill for use
when adding slides. Keep the template authoritative for the actual design.

Identify which slides are fixed, optional or repeated and the evidence for each
selection rule. Replace old facts, figures, authorities and conclusions with named
blanks or neutral slide functions. Chart data must come from the new matter.

For simple text substitutions, the portable helper can prepare named blanks:

```bash
python3 assets/create_pptx.py --template sample.pptx --replace edits.json output/template.pptx
```

`edits.json` is a JSON object such as
`{"Example client": "[Client name]", "Old conclusion": "[Conclusion: new-matter conclusion]"}`.
Replacements match exact case-sensitive text within DrawingML paragraphs, including
split runs. They apply to slides, notes, masters and layouts, so inspect all matches.
Missing replacement anchors fail before writing. Edits use original text in one
pass; replacement values do not become new edit targets. Keep this file private.

This operation only replaces text. Before distribution, inspect and sanitise the
whole ZIP: hidden and unused slides, notes and notes masters, comments and authors,
document properties and custom XML, shape names and alternative text, hyperlinks
and external relationships, media, thumbnails, embedded workbooks and other files,
chart caches and underlying data, and masters/layouts. Text blanks do not remove
old figures from charts or identifying content inside images. Remove or replace
unapproved content with a suitable local tool, repair relationships and validate
the deck. Do not distribute a partially sanitised source as a template.

## Package and generate

Deliver `SKILL.md`, `template.pptx`, `create_pptx.py`, `LICENSE.md` and
`references/runtime-compatibility.md`, plus supported writing/design rules and
synthetic examples when useful. Copy `assets/create_pptx.py` beside the template;
it has no dependency on the builder or third-party packages. Adapt the common
drafting scaffold's template, commands, review criteria and output extension for
PPTX. Keep operative house wording in the presentation template.

```bash
python3 create_pptx.py --list
python3 create_pptx.py --text
python3 create_pptx.py values.json new-deck.pptx
```

Values use field names without brackets or guidance, for example
`{"Client name": "Synthetic Client", "Conclusion": "Synthetic trial conclusion."}`.
The helper supports single-line text and numeric values, including blanks split
across runs. Replacement text inherits the first affected run's appearance.
Missing values remain bracketed and are reported; they are not highlighted.
It does not implement DOCX choice/note markers, repeated slides, lists, multiline
or rich-text values, inflection, chart updates, media edits or animations. Do not
put those markers into a PPTX expecting them to execute. Use an available local
presentation tool for those requirements, and bundle any additional generator,
dependencies and runtime instructions required by the actual delivered package.

Untouched parts retain their bytes. Existing output requires `--force` for an
intended replacement; even then the source/template cannot be overwritten.
Ordinary transitional OOXML with `ppt/presentation.xml` is supported. Unsupported
Strict OOXML or unusual part naming needs re-saving and conversion review or a
suitable presentation tool. Neither unchanged XML nor successful generation
establishes rendered fidelity.

## Validate and hand over

Run the actual generator from an isolated copy of the delivered folder with
synthetic values. Check slide order, content, notes, links, chart sources, retained
parts and unresolved blanks. Compare the template and trial's design declarations:

```bash
python3 scripts/inspect_pptx.py --compare output/template.pptx trial.pptx
```

Exit 1 flags differences in template structure or retained assets for review.
The check ignores DrawingML text contents and compares backgrounds, formatting,
theme/master/layout parts, geometry, relationships and media/embedded font bytes.
It also reports intentional structural changes such as added slides or revised
links; review those against the brief. It does not check chart datasets or embedded
workbooks, resolve effective inherited appearance or establish rendered fidelity.
Compare against the sanitised template after intentional source edits, then render
the source and trial to verify that the supported house design was carried over.

Render every delivered slide and relevant notes;
check wrapping, overflow, clipping, contrast, citations and layout after filling
long realistic values. Check backgrounds, colours, font families and sizes, theme
inheritance, images and alignment against the source. Check speaker-note content separately. If a renderer is
unavailable, state that appearance is unverified. Report untested optional/repeated
slide variants and any unresolved input without inventing substantive content.
