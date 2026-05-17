# legalcode-order-form

Source: skill-bundled template for `legalcode-saas-agreement-drafter`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-29

A short, modern Order Form. Designed to plug in as **Exhibit A** of
`legalcode-csa` (Cloud / SaaS Subscription Agreement). The Order Form
records the commercial particulars of a single subscription (services,
quantities, term, fees, contacts) and any deal-specific overrides to
the CSA. Order Forms are intentionally concise — bring legal text into
the CSA, not the Order Form.

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline | You operate in a jurisdiction not covered below, or you want the master before specialising. |
| `us.md` | US — Delaware/NY default + state PO + auto-renewal disclosures | Customer is US-based; covers state-by-state purchase-order rules, NY Truth-in-Lending, IL/CA auto-renewal disclosures embedded in the Order Form. |
| `eu.md` | EU/EEA — Data Act + late-payment + VAT + DE-AGB | Customer is EU/EEA-based. Includes German overlay for written-form / Schriftform requirements and B2B late-payment statutory interest. |
| `uk.md` | UK — DMCCA 2024 Pt 4 (where applicable to SME) + UK CRA + late-payment | Customer is UK-based. Includes DMCCA Pt 4 reminder-notice flagging if Customer is SME. |
| `is.md` | Iceland — Lög nr. 16/2016 carve-out + EEA-imported Data Act + kennitala | Customer is Iceland-based. Bilingual labels in signature block. |

## How to use

1. Pick the file matching the Customer's primary jurisdiction.
2. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
3. Complete **Schedule 1** (Subscribed Services & Quantities) and
   **Schedule 2** (Fees & Payment Schedule).
4. Decide which optional sections apply (each annotated with
   "OPTIONAL — only if X").
5. Have both Parties sign the Order Form. The CSA must be in place
   first (or signed contemporaneously).

## Canonical 10-section structure + 3 schedules

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. Parties & contacts
3. Order details (services, quantities, term)
4. Fees & payment terms
5. Renewal terms
6. Service level (cross-reference SLA)
7. Data residency, AI training, security tier
8. Order-specific overrides to the CSA
9. Notices for this Order
10. Signature block

**Schedule 1** — Subscribed Services & Quantities (table)
**Schedule 2** — Fees & Payment Schedule (table)
**Schedule 3** — Order-Specific Addenda (BAA / HIPAA / FedRAMP / sector-specific)

## Companion templates

- `legalcode-csa` — primary parent; this Order Form attaches as Exhibit A
- `legalcode-sla` — referenced in §6; Order Form may upgrade default uptime tier
- `legalcode-dpa` — referenced in §7; Order Form may set data-residency overrides
- `legalcode-msa` — alternative pattern (services / SOWs, not subscription-based)

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Order Form Number}}        # unique identifier (e.g., "OF-2026-0042")
{{Order Form Date}}          # YYYY-MM-DD
{{Master Agreement Title}}   # parent CSA title
{{Master Agreement Date}}    # parent CSA effective date
{{Vendor Legal Name}}        # full registered name of the SaaS provider
{{Vendor Short Name}}        # how the vendor is referred in prose
{{Vendor Address}}           # registered address
{{Vendor Country}}           # for choice-of-law header
{{Vendor Signatory Name}}    # name of signing officer
{{Vendor Signatory Title}}   # title of signing officer
{{Vendor Notice Email}}      # legal/contracts contact
{{Vendor AR Email}}          # accounts-receivable contact
{{Customer Legal Name}}      # full registered name of the customer
{{Customer Short Name}}      # how the customer is referred in prose
{{Customer Address}}         # registered address
{{Customer Country}}         # for transfer determination
{{Customer Signatory Name}}  # name of signing officer
{{Customer Signatory Title}} # title of signing officer
{{Customer Notice Email}}    # legal/contracts contact
{{Customer Billing Email}}   # accounts-payable contact
{{Customer PO Number}}       # OPTIONAL — Customer's purchase order number
{{Service Name}}             # the SaaS product
{{Initial Term Length}}      # e.g., "12 months", "24 months", "36 months"
{{Initial Term Start}}       # YYYY-MM-DD
{{Initial Term End}}         # YYYY-MM-DD
{{Renewal Term Length}}      # default same as Initial Term
{{Auto-Renewal}}             # "Yes" / "No"
{{Non-Renewal Notice Window}}# days before renewal (default 30)
{{Annual Price Cap}}         # max annual % increase on renewal (default "the lesser of 7% or CPI")
{{Currency}}                 # USD / EUR / GBP / ISK / etc.
{{Payment Terms}}            # "Net 30", "Net 60", or due-on-receipt
{{Billing Frequency}}        # annual / semi-annual / quarterly / monthly
{{Total Order Value}}        # total contract value over Initial Term
{{Annual Fee}}               # annualized fee
{{Subscribed Quantity}}      # users / API calls / GB / etc.
{{Overage Rate}}             # rate per unit above Subscribed Quantity
{{True-Up Frequency}}        # quarterly / annual
{{Uptime Tier}}              # SLA upgrade if any
{{Data Residency}}           # region / country / "no preference"
{{AI Training Opt-In}}       # "Yes" / "No" (default No)
{{Authorized Users URL}}     # link to authorized-users list (or attach as Schedule)
{{Affiliates URL}}           # link to permitted-affiliates list
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- Common Paper Order Form — CC-BY-4.0 (primary baseline)
- Common Paper CSA v2.1 (Order Form exhibit pattern) — CC-BY-4.0
- Bonterms Cloud Terms Order Form attachments — CC-BY-4.0
- GitHub `site-policy` — CC0 (general structure)
- Mozilla legal templates — MPL-2.0 (regional-overlay pattern)
- legislation.gov.uk + ec.europa.eu + state AG sites — Open Government Licence / public domain

**Blocked baselines (not consulted):** AWS Order Forms, Microsoft order
documents, Google Cloud order forms, Salesforce MSA Order Forms,
Atlassian order forms, Stripe order forms, OneDrive, and any other
proprietary or unspecified-license cloud/SaaS Order Form templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Confirm Schedule 1 quantities, overage rates, and true-up cadence
  match your billing system.
- Confirm Schedule 2 currency, payment cadence, and tax handling
  match the Customer's procurement / AP rules.
- For US: confirm state-specific auto-renewal disclosure language is
  present at clear-and-conspicuous prominence (CA ARLDA, NY GBL §527-a,
  IL ARLDA, etc.).
- For EU/UK: confirm the late-payment statutory interest and VAT rules.
- For Iceland: include kennitala on both sides of the signature block.
- Sign **after** the CSA is in place. An Order Form without a CSA is
  ambiguous about which terms govern.
