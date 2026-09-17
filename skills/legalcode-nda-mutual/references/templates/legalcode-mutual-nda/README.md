# legalcode-mutual-nda

Source: skill-bundled template for `legalcode-nda-mutual`
License: Legalcode Skills Source-Available License 1.0 (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

A short, modern, mutual (two-way) Non-Disclosure Agreement. Designed as
a clean-room replacement for templates that ship under restrictive
licenses (e.g., oneNDA, which is CC-BY-ND and therefore not modifiable
for commercial reuse).

## Documents

| File      | Document Type                                                     | Use when                                                                                                                                                                      |
| --------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `core.md` | Jurisdiction-neutral baseline                                     | You operate in a jurisdiction not covered below, or you want the master before specialising.                                                                                  |
| `us.md`   | US — DTSA + state trade-secret + whistleblower notice             | Either party is US-based; covers Defend Trade Secrets Act 18 USC §1836, 18 USC §1833(b) immunity notice, state UTSA variants, California Bus. & Prof. Code §16600 carve-outs. |
| `eu.md`   | EU — Trade Secrets Directive 2016/943 + DE-AGB                    | Either party is EU/EEA-based. Includes German AGB-Kontrolle overlay for §§ 305–310 BGB.                                                                                       |
| `uk.md`   | UK — Trade Secrets (Enforcement etc.) Regs 2018 + UK contract law | Either party is UK-based. Includes UK CRA fairness considerations and post-Brexit governing-law conventions.                                                                  |
| `is.md`   | Iceland — Lög nr. 7/1936 + EEA-imported Trade Secrets             | Either party is Iceland-based. EEA framing for trade-secret protection.                                                                                                       |

## How to use

1. Pick the file matching the parties' primary jurisdiction (if mixed,
   pick the controlling-law jurisdiction).
2. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
3. Complete **Annex A** (description of the discussion / purpose) and
   **Annex B** (signature block).
4. Decide which optional clauses apply (each annotated with
   "OPTIONAL — only if X").
5. Have the resulting MNDA reviewed by qualified counsel before execution.

## Canonical 16-section structure + 2 annexes

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. Parties & purpose
3. Definitions
4. Confidential Information
5. Permitted disclosures & use
6. Standard of care
7. Exclusions
8. Compelled disclosure
9. Term & duration of obligations
10. Return or destruction of materials
11. No license; ownership
12. Residuals (OPTIONAL)
13. Remedies & equitable relief
14. Notices
15. Governing law & jurisdiction
16. Miscellaneous

**Annex A** — Description of discussion / purpose particulars
**Annex B** — Signature block

## Companion templates

- `legalcode-one-way-nda` — disclosing-party-only NDA (evaluation, RFP, etc.)
- `legalcode-dpa` — Data Processing Agreement (when personal data is shared)
- `legalcode-msa` / `legalcode-csa` — for ongoing commercial relationships
- `legalcode-design-partner-agreement` — early-stage commercial pilots

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Party A Legal Name}}        # full registered name of Party A
{{Party A Short Name}}        # how Party A is referred in prose
{{Party A Address}}           # registered address
{{Party A Country}}           # for choice-of-law header
{{Party A Notice Email}}      # legal/contracts contact
{{Party B Legal Name}}        # full registered name of Party B
{{Party B Short Name}}        # how Party B is referred in prose
{{Party B Address}}           # registered address
{{Party B Country}}           # for choice-of-law header
{{Party B Notice Email}}      # legal/contracts contact
{{Purpose}}                   # short description of the discussion
{{Effective Date}}            # YYYY-MM-DD when MNDA takes effect
{{Disclosure Period}}         # how long disclosures are accepted under MNDA — typically "two (2) years"
{{Confidentiality Term}}      # how long confidentiality obligations survive — typically "five (5) years"
{{Trade-Secret Term}}         # how long trade-secret obligations survive — typically "for so long as the information remains a trade secret"
{{Governing Law}}             # choice of law for the MNDA
{{Forum}}                     # exclusive forum
{{Return Window}}             # post-termination return window — typically "thirty (30) days"
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- Bonterms Mutual NDA — CC0 1.0 (primary structural baseline)
- Common Paper Mutual NDA — CC-BY-4.0 (clause patterns)
- GitHub `site-policy` (where any MNDA snippets exist) — CC0 1.0
- mgifford/nda — CC0 1.0 (short-form patterns)
- Mozilla legal templates — MPL-2.0 (where applicable)
- US legislation (uscode.house.gov) — public domain
- EU Trade Secrets Directive 2016/943 — public domain
- UK Trade Secrets (Enforcement etc.) Regulations 2018 (legislation.gov.uk) — Open Government Licence

**Blocked baselines (not consulted):** oneNDA (CC-BY-ND), TermsFeed,
PandaDoc proprietary templates, Iubenda, NDA-templates with unspecified
licences, and any other CC-BY-NC/CC-BY-ND/CC-BY-SA NDA templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Confirm both parties' legal names, addresses, and signing authority.
- Define **{{Purpose}}** narrowly — overly broad purpose statements
  invite overreach claims.
- Pick a confidentiality term that matches your industry norms (commonly
  3–5 years for general business; trade-secret obligations indefinite).
- For US engagements involving employees/contractors, ensure the
  18 USC §1833(b) whistleblower notice is included (if missing, exemplary
  damages and attorney fees are unavailable in DTSA claims).
- For EU engagements, confirm the Trade Secrets Directive transposition
  in the controlling-law Member State.
- For sensitive technical disclosures, consider whether a separate
  Technical Information Exchange Agreement (TIEA) or a more bespoke
  Evaluation Agreement is needed.
