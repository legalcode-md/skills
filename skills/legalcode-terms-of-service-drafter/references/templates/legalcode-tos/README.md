# legalcode-tos

Source: skill-bundled template for `legalcode-terms-of-service-drafter`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline (B2C/B2B toggle) | You operate in a jurisdiction not covered below, or you want the master before specialising. |
| `us.md` | US — Section 230 + DMCA + state auto-renewal + arbitration | You target US consumers; covers CA/NY/OR/CO/IL auto-renewal, FTC Click-to-Cancel, Section 230 platform immunity, DMCA safe harbor. |
| `eu.md` | EU/EEA — DSA + Consumer Rights Directive + Sale of Goods + DE-AGB | You target EU/EEA consumers or operate a hosting / marketplace / very-large-online-platform service. Includes German AGB-Kontrolle overlay. |
| `uk.md` | UK — UK CRA 2015 + DMCCA 2024 + Online Safety Act 2023 | You target UK consumers post-Brexit. Includes Online Safety Act category-1/2A/2B duties. |
| `is.md` | Iceland — consumer protection + EEA-imported DSA | You operate in Iceland or target Icelandic consumers. EEA framing for digital-services rules. |

## How to use

1. Pick the file matching your primary jurisdiction.
2. Decide your audience: **B2C** (consumer), **B2B** (business customer), or **mixed**. Each clause flags where the two diverge.
3. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
4. Decide which optional sections apply (each annotated with "OPTIONAL — only if X").
5. Have the resulting Terms reviewed by qualified counsel before publishing.
6. Set up a recurring review cadence — platform-regulation law changes
   frequently (DSA enforcement updates, FTC Click-to-Cancel rulemaking,
   DMCCA commencement, Online Safety Act phase-in). Recommended: quarterly.

## Canonical 20-section structure

Every variant in this pack follows the same section numbering. This makes
it easy to compare jurisdictions side-by-side and to assemble a
multi-jurisdiction Terms with regional supplements.

1. Plain-language summary
2. Acceptance & eligibility
3. Definitions
4. Account registration & security
5. License & access rights
6. User-generated content (UGC)
7. Acceptable use
8. Intellectual property (platform IP)
9. Third-party services & links
10. Subscription, billing, auto-renewal, refunds
11. Trials, free tier & beta
12. Term, suspension, termination
13. Disclaimers (warranties)
14. Limitation of liability
15. Indemnification
16. Dispute resolution
17. Governing law & jurisdiction
18. Changes to these Terms
19. Notices & communications
20. Miscellaneous

## Required annexes

- **Annex A** — Acceptable Use Policy (content/conduct rules; DSA Art. 14 + Online Safety Act-aligned)
- **Annex B** — Notice-and-takedown procedure (DMCA / e-Commerce Directive / Online Safety / DSA Statement of Reasons)
- **Annex C** — Subscription, billing & auto-renewal disclosures (jurisdiction-specific)

## Companion templates

- `legalcode-privacy-policy` — paired with §6 (UGC) and §19 (notices)
- `legalcode-cookie-policy` — paired with §10 (billing identifiers and analytics)
- `legalcode-acceptable-use-policy` — Annex A may incorporate by reference
- `legalcode-eula` — for downloadable / installed software (see drafter skill)
- `legalcode-csa` — Cloud / SaaS Subscription Agreement for paid B2B tiers

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Company Legal Name}}        # full registered name
{{Company Short Name}}        # how the company is referred in prose
{{Company Address}}           # registered address
{{Company Country}}           # for choice-of-law header
{{Company Email Legal}}       # legal@ or terms@
{{Company Email Support}}     # support contact
{{Service Name}}              # product/service this Terms applies to
{{Service URL}}               # primary URL
{{Effective Date}}            # YYYY-MM-DD when Terms takes effect
{{Last Updated Date}}         # YYYY-MM-DD of last revision
{{Minimum Age}}               # account-creation age floor (commonly 13/16/18)
{{Subscription Term}}         # default subscription period
{{Renewal Notice Window}}     # days before auto-renewal (jurisdiction-driven)
{{Cancellation URL}}          # one-click cancellation page
{{Refund Policy URL}}         # link to refund policy
{{Governing Law}}             # choice of law for the Terms
{{Forum}}                     # exclusive forum / arbitration seat
{{Privacy Policy URL}}        # link to companion privacy policy
{{Acceptable Use Policy URL}} # link to AUP if separate
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- GitHub `site-policy` Terms of Service — CC0 1.0 (multi-jurisdiction baseline)
- Bonterms Online Terms of Service — CC-BY-4.0 (B2C / B2B structure)
- Common Paper Cloud Service Agreement v2.1 — CC-BY-4.0 (subscription / billing patterns)
- Mozilla `Firefox_Terms` / `mozilla.org_terms` — MPL-2.0 (regional-overlay pattern)
- EU Digital Services Act (Regulation (EU) 2022/2065) — public domain
- EU Consumer Rights Directive (2011/83/EU) — public domain
- ICO / CMA online platform guidance — Open Government Licence (OGL)
- US legislation.gov, oag.ca.gov, FTC.gov — US public-domain government works

**Blocked baselines (not consulted):** TermsFeed, OneTrust, Iubenda,
SimplifyMyTerms, FreePrivacyPolicy, and any other unspecified-license
or CC-BY-NC/CC-BY-ND/CC-BY-SA Terms templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Tailor every "we provide X" sentence to what your service actually offers.
- Confirm which jurisdictions actually apply to your user base (the
  multi-jurisdiction approach is opt-in per market).
- For UGC platforms, complete Annex A (AUP) and Annex B (notice-and-takedown).
- For paid/subscription services, complete Annex C with jurisdiction-correct
  auto-renewal and cancellation disclosures.
- For platforms operating in the EU above the Art. 33 threshold, layer in
  VLOP / VLOSE obligations separately (this template covers Arts. 14–27,
  not the full Section 5 risk-management regime).
- For UK platforms in scope of the Online Safety Act, layer in OSA
  category-1/2A/2B duties (illegal content risk assessment, child safety
  duties, transparency reporting) — this template flags these but does
  not produce the underlying risk assessments.
- Have arbitration and class-action waiver clauses reviewed against
  current case law in each forum before relying on them.
