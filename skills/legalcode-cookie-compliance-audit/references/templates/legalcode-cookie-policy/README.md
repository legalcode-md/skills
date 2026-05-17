# legalcode-cookie-policy

Source: skill-bundled template for `legalcode-cookie-compliance-audit`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

A short, modern cookie / similar-technologies policy. Designed to pair
with `legalcode-privacy-policy` (privacy-policy §12 cross-references this
file's category list and consent flow).

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline | You operate in a jurisdiction not covered below, or you want the master before specialising. |
| `us.md` | US — CCPA/CPRA opt-out + GPC + multi-state | You target US consumers; covers Sale/Sharing opt-out under CCPA, GPC honor obligation in CO/CT/TX, state-specific cookie/tracker disclosures. |
| `eu.md` | EU/EEA — ePrivacy Art. 5(3) + GDPR consent + DE-TTDSG | You target EU/EEA users. Includes German TTDSG/TDDDG overlay. |
| `uk.md` | UK — PECR Reg. 6 + ICO 2023 cookies guidance | You target UK users post-Brexit. Includes ICO consent UX expectations. |
| `is.md` | Iceland — Lög nr. 70/2022 + EEA-imported ePrivacy | You operate in Iceland or target Icelandic users. |

## How to use

1. Pick the file matching your primary jurisdiction.
2. Run a cookie audit (use the parent `legalcode-cookie-compliance-audit`
   skill or a tool such as Cookiebot, OneTrust, Osano, etc.) to populate
   **Annex A — Cookie Inventory**.
3. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
4. Choose the consent UX described in **Annex B** that matches your
   jurisdiction's regulator expectations (the EU/UK variants require
   "reject all" with equal prominence to "accept all"; the US variants
   support an opt-out model under CCPA).
5. Have the resulting policy reviewed by qualified counsel before
   publishing.
6. Re-run the cookie inventory at least quarterly — third-party tags
   and tracking pixels change frequently.

## Canonical 14-section structure + 2 annexes

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. What cookies and similar technologies are
3. Why we use them
4. Categories of cookies we use
5. Specific cookies we use (cross-reference Annex A)
6. Third-party cookies & subprocessors
7. Your choices & how to manage cookies
8. Browser controls
9. Global Privacy Control (GPC) & Do Not Track (DNT)
10. How we obtain and record consent
11. International data transfers
12. Children's data
13. Changes to this policy
14. Contact & complaints

**Annex A** — Cookie inventory (table to be populated by audit)
**Annex B** — Consent banner UX requirements (jurisdiction-specific)

## Companion templates

- `legalcode-privacy-policy` — primary parent; §12 cross-references this file
- `legalcode-tos` — site terms (separate from this cookie policy)
- `legalcode-dpa` — required when third-party cookies share data with subprocessors

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Company Legal Name}}        # full registered name
{{Company Short Name}}        # how the company is referred in prose
{{Company Address}}           # registered address
{{Company Email Privacy}}     # privacy@…
{{Company Email DPO}}         # OPTIONAL — DPO if appointed
{{Service Name}}              # product/service this policy applies to
{{Service URL}}               # primary URL
{{Effective Date}}            # YYYY-MM-DD when policy takes effect
{{Last Updated Date}}         # YYYY-MM-DD of last revision
{{Cookie Banner Vendor}}      # OPTIONAL — Cookiebot / OneTrust / Osano / in-house
{{Cookie Settings URL}}       # link to cookie preferences center
{{Privacy Policy URL}}        # link to companion privacy policy
{{Cookie Audit Date}}         # YYYY-MM-DD of most recent audit
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- GitHub `cookies.md` — CC0 1.0 (cookie-disclosure pattern)
- oprvc DSGVO cookie Mustertexte — CC0 1.0 (German vendor-specific paragraph references)
- Mozilla cookie pages — MPL 2.0 (regional-overlay pattern)
- ICO cookies and similar technologies guidance — Open Government Licence v3.0
- EDPB Guidelines 2/2023 on technical scope of Art. 5(3) ePrivacy Directive — public domain
- ePrivacy Directive 2002/58/EC + national implementations — public domain
- US: CPPA regulations + state AG guidance — public domain

**Blocked baselines (not consulted):** TermsFeed, Cookiebot proprietary,
OneTrust proprietary, Iubenda, FreePrivacyPolicy, IAB TCF (proprietary),
and any other unspecified-license or CC-BY-NC/CC-BY-ND/CC-BY-SA cookie
templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Run an actual cookie audit and populate **Annex A** with the cookies
  your service actually sets. A policy that lists cookies you don't use
  is misleading; missing cookies are a regulator finding.
- Implement the consent UX described in **Annex B**. The policy text
  describes what the user can do; the consent banner has to actually
  enable it.
- Honor Global Privacy Control (GPC) signals in jurisdictions where it
  is required (CA, CO, CT, TX as of 2025; check current state).
- For EU/UK: equal prominence "Accept all" / "Reject all" buttons; no
  pre-ticked boxes for non-essential cookies; no cookie walls (where
  consent is the only access path) without justification.
- Maintain a record of consent (what was consented to, when, what banner
  version) for at least 12 months for audit purposes.
- Re-audit at least quarterly, or whenever a new third-party tag is added.
