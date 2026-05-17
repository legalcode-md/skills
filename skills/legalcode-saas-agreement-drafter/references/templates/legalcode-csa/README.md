# legalcode-csa

Source: skill-bundled template for `legalcode-saas-agreement-drafter`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

A modern, modular Cloud / SaaS Subscription Agreement (CSA). Designed
for B2B SaaS sellers using a Master Agreement + Order Form pattern:
the CSA is signed once and governs all subsequent subscription orders
captured on a separate Order Form (`legalcode-order-form`).

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline (dual-perspective: customer / vendor / market-standard) | You operate in a jurisdiction not covered below, or you want the master before specialising. |
| `us.md` | US — Delaware/NY default + CCPA service-provider terms + state auto-renewal + export controls | Either party is US-based; covers DTSA, FTC Click-to-Cancel, CCPA service-provider obligations, ROSCA, and state-by-state auto-renewal. |
| `eu.md` | EU/EEA — DSA + DCD/SGD + Data Act + DE-AGB | Either party is EU/EEA-based. Includes German AGB-Kontrolle overlay and EU Data Act portability. |
| `uk.md` | UK — UK CRA + DMCCA 2024 + DUAA 2025 | Either party is UK-based. Includes DMCCA Pt 4 subscription contract overlay. |
| `is.md` | Iceland — Lög nr. 16/2016 + EEA-imported DSA/Data Act | Either party is Iceland-based. EEA framing for digital-services rules. |

## How to use

1. Pick the file matching the controlling-law jurisdiction.
2. Decide your drafting posture — customer-side, vendor-side, or
   market-standard. The dual-perspective sections (§6 Customer Data,
   §8 Fees, §9 Term/Termination, §11 Security, §15 AI/ML, §16
   Warranties/Liability, §17 Indemnification) carry three labelled
   variants.
3. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
4. Complete the four exhibits (or attach companion templates):
   - **Exhibit A** — Order Form (`legalcode-order-form`)
   - **Exhibit B** — SLA (`legalcode-sla`)
   - **Exhibit C** — DPA (`legalcode-dpa`)
   - **Exhibit D** — AUP (`legalcode-acceptable-use-policy` or §7 of `legalcode-tos`)
5. Have the resulting CSA reviewed by qualified counsel before execution.

## Canonical 18-section structure + 4 exhibits

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. Agreement structure (Master Agreement + Order Forms)
3. Definitions
4. Use of the Service
5. Customer responsibilities & restrictions
6. Customer Data
7. Confidentiality
8. Fees, billing, taxes
9. Term, renewal, termination & suspension
10. Service Level Agreement
11. Security & data protection
12. Trials & beta features
13. Third-party services & integrations
14. Intellectual property
15. AI & machine learning
16. Warranties, disclaimers & limitations of liability
17. Indemnification & insurance
18. General provisions

**Exhibit A** — Order Form template (cross-references `legalcode-order-form`)
**Exhibit B** — Service Level Agreement (cross-references `legalcode-sla`)
**Exhibit C** — Data Processing Agreement (cross-references `legalcode-dpa`)
**Exhibit D** — Acceptable Use Policy (cross-references `legalcode-acceptable-use-policy` or `legalcode-tos` §7/Annex A)

## Companion templates

- `legalcode-order-form` — paired with §2; the per-subscription order
- `legalcode-sla` — paired with §10; uptime, support, credits
- `legalcode-dpa` — paired with §11; processor obligations
- `legalcode-msa` — alternative pattern (services + deliverables, not subscription-based)
- `legalcode-tos` — for self-serve B2B/B2C signups (no Order Form)
- `legalcode-privacy-policy` — paired with §6 (Customer Data)

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Vendor Legal Name}}        # full registered name of the SaaS provider
{{Vendor Short Name}}        # how the vendor is referred in prose
{{Vendor Address}}           # registered address
{{Vendor Country}}           # for choice-of-law header
{{Vendor Email Legal}}       # legal/contracts contact
{{Vendor Email Support}}     # support contact
{{Customer Legal Name}}      # full registered name of the customer
{{Customer Short Name}}      # how the customer is referred in prose
{{Customer Address}}         # registered address
{{Customer Country}}         # for transfer determination
{{Customer Email Legal}}     # legal/contracts contact
{{Service Name}}             # the SaaS product
{{Service URL}}              # primary URL
{{MSA Effective Date}}       # YYYY-MM-DD when CSA takes effect
{{Last Updated Date}}        # YYYY-MM-DD of last revision
{{Initial Term}}             # default subscription term length (e.g., "12 months")
{{Renewal Term}}             # default renewal length (e.g., "12 months")
{{Non-Renewal Notice Window}}# days before renewal to give notice (e.g., "30 days")
{{Payment Terms}}            # net days (e.g., "Net 30")
{{Currency}}                 # USD / EUR / GBP / ISK
{{Late Fee Rate}}            # default late-fee rate (e.g., "1.5% per month or maximum allowed by law")
{{Annual Price Cap}}         # max annual price increase on renewal (e.g., "the lesser of 7% or CPI")
{{Liability Cap Multiplier}} # cap as multiple of fees (e.g., "12 months of fees paid")
{{Liability Cap Floor}}      # absolute floor for cap (e.g., "USD 100,000")
{{Indemnity IP Threshold}}   # IP claim threshold for indemnity (commonly no threshold)
{{Insurance Cyber Limit}}    # cyber insurance per occurrence (e.g., "USD 5M")
{{Governing Law}}            # choice of law for the CSA
{{Forum}}                    # exclusive forum / arbitration seat
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- Common Paper CSA v2.1 — CC-BY-4.0 (primary baseline)
- Common Paper Order Form — CC-BY-4.0 (Exhibit A pattern)
- Common Paper AI Addendum — CC-BY-4.0 (§15 AI/ML clause patterns)
- Bonterms Cloud Terms — CC-BY-4.0 (alternate clause patterns)
- Bonterms PSA v1.2 — CC0 (for some general-provisions language)
- GitHub `site-policy` — CC0 (clause-heading conventions)
- Mozilla legal templates — MPL-2.0 (regional-overlay pattern)
- legislation.gov.uk + ico.org.uk + cma.gov.uk — Open Government Licence
- EU public-domain materials (eur-lex Data Act, DSA, DCD, SGD, Modernisation, etc.)

**Blocked baselines (not consulted):** AWS Customer Agreement, Microsoft
Customer Agreement, Google Cloud terms, Salesforce MSA, Atlassian
Customer Agreement, Stripe Services Agreement, OneNDA, TermsFeed,
Iubenda, FreePrivacyPolicy, and any other proprietary or unspecified-
license cloud/SaaS templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Confirm both parties' legal names, addresses, signing authority, and
  parent-entity controls.
- Pick a market-appropriate liability cap and carve-outs for your stage
  and deal size.
- Decide AI/ML training and output policies in §15 — these are the most
  bargained-over clauses in 2025–26 enterprise SaaS deals.
- Wire in a real SLA in Exhibit B; placeholder uptime numbers without
  monitoring will become an enforcement liability.
- Layer in jurisdiction-specific consumer protections if any individual
  subscriber is a consumer (the CSA is built B2B; for self-serve mixed-
  audience use the `legalcode-tos` pack instead).
- Confirm export controls and sanctions clauses match your actual
  customer geography and regulated-data exposure.
