# legalcode-msa

Source: skill-bundled template for `legalcode-master-services-agreement`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-29

A modern Master Services Agreement (MSA) for professional and managed
services. Designed as a **framework agreement** that pairs with one or
more Statements of Work (SOWs — see `legalcode-sow`) or Order Forms
(see `legalcode-order-form`) to scope individual engagements. The MSA
records the legal and commercial baseline; SOWs/Orders carry the
deal-specific particulars.

This template is service-oriented (deliverables, milestones, T&M,
fixed-fee, key personnel, IP assignment) — distinct from
`legalcode-csa`, which is subscription/SaaS-oriented.

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline (dual-perspective: client / provider / market-standard) | You operate in a jurisdiction not covered below, or you want the master before specialising. |
| `us.md` | US — DE/NY default + work-for-hire + IRS independent-contractor + state insurance defaults + FAA arbitration | Either party is US-based; covers federal IP assignment formalities, classification (DOL §541, ABC test states), and state-by-state late-payment rules. |
| `eu.md` | EU/EEA — Late Payment Directive + GDPR Art. 28 + worker-classification + DE-AGB + EU IP assignment formalities | Either party is EU/EEA-based. Includes German overlay (Schriftform / § 31 UrhG buy-out / GeschGehG) and EU-wide moral-rights handling. |
| `uk.md` | UK — UK CRA B2B + IR35 / off-payroll working + LDEDC late-payment + Equality Act + DUAA 2025 | Either party is UK-based. Includes IR35 status determination, JCT-style payment provisions, and UK GDPR processor terms. |
| `is.md` | Iceland — Lög nr. 38/2001 statutory interest + kennitala + EEA-imported AI Act / Data Act + bilingual signature | Either party is Iceland-based. Bilingual labels in signature block; EEA-import election for digital obligations. |

## How to use

1. Pick the file matching the controlling-law jurisdiction.
2. Decide your drafting posture — client-side, provider-side, or
   market-standard. The dual-perspective sections (§5 fees, §6 change
   control, §9 IP ownership, §12 warranties, §13 indemnity, §14
   liability cap, §16 termination, §17 transition) carry three labelled
   variants.
3. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
4. Attach at least one SOW (use `legalcode-sow`) or Order Form (use
   `legalcode-order-form`). The MSA alone is incomplete.
5. Confirm insurance minimums (§15) match the actual coverage your
   broker has bound. Don't promise PI/cyber limits you don't carry.
6. For US: confirm work-for-hire categories (17 USC §101) actually
   apply to the deliverables — most do not, so a present-tense
   assignment is also required.
7. Have the resulting MSA reviewed by qualified counsel. SOW templates
   are governed by the MSA — drafting errors in the MSA propagate to
   every SOW.

## Canonical 19-section structure + 3 annexes

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. Definitions
3. Engagement structure (MSA + SOW / Order Form framework)
4. Scope of services & SOW process
5. Fees, expenses & invoicing
6. Change control & change orders
7. Personnel, key personnel & subcontracting
8. Acceptance & deliverables
9. Intellectual property (foreground / background / open-source)
10. Confidentiality
11. Data protection & information security
12. Representations & warranties
13. Indemnification
14. Limitation of liability
15. Insurance
16. Term & termination
17. Transition assistance & wind-down
18. Dispute resolution & governing law
19. General provisions & signature block

**Annex A** — Statement of Work (SOW) template (cross-reference
`legalcode-sow` for fuller pack)
**Annex B** — Approved subcontractors & key personnel
**Annex C** — Service standards & acceptance criteria framework

## Companion templates

- `legalcode-sow` — primary attachment; carries deliverables, fees,
  milestones, and acceptance criteria for individual engagements
- `legalcode-order-form` — alternative attachment for recurring /
  managed-services pricing
- `legalcode-mutual-nda` — pre-engagement confidentiality (rolls into
  §10 once MSA is signed)
- `legalcode-dpa` — referenced from §11; required where Provider
  processes Client personal data
- `legalcode-csa` — alternative pattern (subscription, not services)
- `legalcode-independent-contractor-agreement` — alternative for
  individual contractors (different worker-classification posture)

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{MSA Title}}                # e.g., "Master Services Agreement"
{{MSA Effective Date}}       # YYYY-MM-DD
{{Provider Legal Name}}      # full registered name of the services provider
{{Provider Short Name}}      # how the provider is referred in prose
{{Provider Address}}         # registered address
{{Provider Country}}         # for choice-of-law header
{{Provider Signatory Name}}  # name of signing officer
{{Provider Signatory Title}} # title of signing officer
{{Provider Notice Email}}    # legal/contracts contact
{{Provider AR Email}}        # accounts-receivable contact
{{Client Legal Name}}        # full registered name of the client
{{Client Short Name}}        # how the client is referred in prose
{{Client Address}}           # registered address
{{Client Country}}           # for transfer determination
{{Client Signatory Name}}    # name of signing officer
{{Client Signatory Title}}   # title of signing officer
{{Client Notice Email}}      # legal/contracts contact
{{Client AP Email}}          # accounts-payable contact
{{Initial Term Length}}      # default "24 months"
{{Renewal Term Length}}      # default "12 months"
{{Termination Notice Window}}# days of notice for convenience termination
{{Cure Period}}              # days to cure material breach (default 30)
{{Currency}}                 # USD / EUR / GBP / ISK / etc.
{{Payment Terms}}            # "Net 30", "Net 45", or due-on-receipt
{{Late Fee Rate}}            # statutory or contract rate
{{Liability Cap Multiplier}} # 1× / 2× fees-paid / fixed amount
{{Liability Cap Floor}}      # absolute floor in {{Currency}}
{{PI Insurance Minimum}}     # professional indemnity minimum
{{PL Insurance Minimum}}     # public liability minimum
{{Cyber Insurance Minimum}}  # cyber/data-breach minimum
{{WC Insurance Minimum}}     # workers' compensation (US) / employer's liability (UK)
{{IP Ownership Default}}     # "Client owns deliverables" / "Provider retains; Client gets license"
{{Open Source Policy}}       # "permissive only" / "any with notice" / "Client pre-approval"
{{Acceptance Period}}        # days for Client to accept/reject deliverables
{{Deemed Acceptance Window}} # days after delivery if no response
{{SOW Approval Method}}      # "countersigned PDF" / "purchase order" / "DocuSign"
{{Governing Law}}            # state / country governing the MSA
{{Venue}}                    # courts / arbitral seat
{{Arbitration Rules}}        # AAA / JAMS / ICC / LCIA / Nordic Arbitration Centre
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- Bonterms Professional Services Agreement (PSA) v1.2 — CC0 (primary baseline)
- Common Paper Standard Services Agreement — CC-BY-4.0
- Common Paper SOW — CC-BY-4.0 (Annex A pattern)
- GitHub `site-policy` — CC0 (general structure)
- Mozilla legal templates — MPL-2.0 (regional-overlay pattern)
- Linux Foundation / Apache project services agreements — Apache-2.0 (IP pattern)
- legislation.gov.uk + ec.europa.eu + state AG sites — Open Government Licence / public domain

**Blocked baselines (not consulted):** AWS PSA, Microsoft services
agreements, Google Cloud PSA, IBM Master Services Agreement, Salesforce
PSA, Atlassian Services Agreement, Accenture / Deloitte / PwC framework
agreements, and any other proprietary or unspecified-license MSA
templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Confirm the IP-ownership default (§9) matches what the SOWs actually
  produce. Software deliverables, marketing materials, and reports may
  warrant different defaults; "all deliverables" rarely fits cleanly.
- Confirm the liability cap (§14) and insurance minimums (§15) are
  internally consistent — a 2× fees cap with a £1M PI floor is
  underwater for many SOW values.
- For US: pair work-for-hire with a present-tense assignment — pure
  WFH only attaches to nine enumerated categories (17 USC §101).
- For UK: confirm IR35 status determination (CEST output preserved)
  before any individual contractor is named in §7.
- For EU: confirm the chosen Schriftform threshold (DE) matches your
  actual approval workflow; € 50,000 is a default, not a rule.
- For Iceland: include kennitala on both sides of the signature block
  and in §11 controller/processor designations.
- Sign the MSA **before** the first SOW. An SOW that predates the MSA
  is ambiguous about which terms govern.
