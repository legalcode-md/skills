# legalcode-privacy-policy

Source: https://legalcode.md/templates/legalcode-privacy-policy
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline | You operate in a jurisdiction not covered below, or you want to understand the shared structure before specialising. |
| `us.md` | US — CCPA/CPRA + multi-state (CO, VA, CT, UT) | You target US consumers and need CCPA "Notice at Collection" + state-specific addenda. |
| `eu.md` | EU/EEA — GDPR + DE-DSGVO | You process personal data of EU/EEA residents. Includes German DSGVO specifics. |
| `uk.md` | UK — UK GDPR + DPA 2018 (ICO-aligned) | You target UK consumers / users post-Brexit. |
| `is.md` | Iceland — Act 90/2018 (Persónuverndarlög) | You operate in Iceland or process personal data of Icelandic residents. |

## How to use

1. Pick the file matching your primary jurisdiction.
2. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
3. Decide which optional sections apply (each section is annotated with
   "OPTIONAL — only if X" where applicable).
4. Have the resulting policy reviewed by qualified counsel for your
   jurisdiction before publishing.
5. Set up a recurring review cadence — privacy law changes frequently
   (CPRA enforcement updates, EDPB guidelines, ICO consultation outcomes,
   Persónuvernd opinions). Recommended: quarterly review.

## Canonical 17-section structure

Every variant in this pack follows the same section numbering. This
makes it easy to compare jurisdictions side-by-side and to assemble a
multi-jurisdiction policy with regional addenda.

1. Plain-language summary
2. Scope & definitions
3. Who we are (controller / business identity)
4. Personal data we collect
5. Sources of personal data
6. Purposes of processing
7. Legal bases (GDPR jurisdictions) / Categories of disclosure (US)
8. Recipients & subprocessors
9. International data transfers
10. Retention
11. Security measures
12. Cookies & similar technologies
13. Children's data
14. Your rights & how to exercise them
15. Automated decision-making & profiling
16. Changes to this policy
17. Contact & complaints

## Companion templates

- `legalcode-cookie-policy` — paired with §12; ePrivacy / GPC / CCPA opt-out flows
- `legalcode-dpa` — Data Processing Agreement for B2B controller↔processor relationships
- `legalcode-tos` — Terms of Service / EULA
- `legalcode-acceptable-use-policy` — DSA / OSA / §230-aware UGC rules

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Company Legal Name}}        # full registered name
{{Company Short Name}}        # how you refer to yourself in prose
{{Company Address}}           # registered address
{{Company Country}}           # for jurisdiction header
{{Company Email Privacy}}     # privacy@…
{{Company Email DPO}}         # OPTIONAL — DPO if appointed
{{Company DPA Representative}}# OPTIONAL — Art. 27 GDPR rep for non-EU controllers
{{Service Name}}              # product/service this policy applies to
{{Service URL}}               # primary URL
{{Effective Date}}            # YYYY-MM-DD when policy takes effect
{{Last Updated Date}}         # YYYY-MM-DD of last revision
{{Supervisory Authority}}     # OPTIONAL — primary supervisory body (set by jurisdiction file)
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- GitHub `general-privacy-statement.md` — CC0 1.0 (US/multi-jurisdiction baseline)
- GitHub `candidate-privacy-policy.md` — CC0 1.0 (HR/recruiting variant reference)
- GitHub `cookies.md` — CC0 1.0 (cookie-disclosure pattern)
- GitHub `subprocessors.md` — CC0 1.0 (subprocessor-list pattern)
- Mozilla `firefox_privacy_notice.md` / `mozilla_privacy_policy.md` — MPL 2.0 (regional-overlay pattern)
- oprvc DSGVO Mustertexte — CC0 1.0 (German vendor-specific paragraph references)
- EU Commission Standard Contractual Clauses 2021/914 — Public domain (transfer mechanism)

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Tailor every "we collect X" sentence to what your service actually collects.
- Verify that the listed legal bases match your actual processing activities.
- Keep the subprocessor list current (link to a published page that you
  update as vendors change).
- Maintain a Record of Processing Activities (Art. 30 register) — this
  policy is the public-facing tip of that iceberg.
