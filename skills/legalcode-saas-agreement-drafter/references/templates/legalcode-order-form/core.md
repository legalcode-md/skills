---
title: Order Form (Jurisdiction-Neutral Baseline)
jurisdictions: [global]
audience: [B2B]
license: MIT
last_updated: 2026-04-29
---

# Order Form

**Order Form Number:** `{{Order Form Number}}`
**Order Form Effective Date:** `{{Order Form Effective Date}}`

---

## 1. Plain-language summary

This Order Form attaches to the Master Agreement titled `{{Master Agreement Title}}` dated `{{Master Agreement Date}}` (the **CSA**) between `{{Vendor Legal Name}}` (**Vendor**) and `{{Customer Legal Name}}` (**Customer**). It records the specific commercial terms — services, quantities, fees, term, and order-specific elections — for this subscription. Both Parties have already signed the CSA, which sets out the legal framework. This Order Form sits as Exhibit A to that CSA.

If anything in this Order Form conflicts with the CSA, the CSA wins, except where Section 8 of this Order Form expressly says otherwise. Schedules 1, 2, and 3 are part of this Order Form and have the same force as the numbered sections.

---

## 2. Parties & contacts

The Parties to this Order Form are listed below, together with the contacts each side designates for legal notices, billing, and operations.

| Field | Vendor | Customer |
|---|---|---|
| Legal name | `{{Vendor Legal Name}}` | `{{Customer Legal Name}}` |
| Registered address | `{{Vendor Address}}` | `{{Customer Address}}` |
| Signatory name | `{{Vendor Signatory Name}}` | `{{Customer Signatory Name}}` |
| Signatory title | `{{Vendor Signatory Title}}` | `{{Customer Signatory Title}}` |
| Notice email (legal) | `{{Vendor Notice Email}}` | `{{Customer Notice Email}}` |
| Billing / AR email | `{{Vendor AR Email}}` | `{{Customer Billing Email}}` |
| Operational contact | `{{Vendor Ops Contact}}` | `{{Customer Ops Contact}}` |
| Purchase order number | n/a | `{{Customer PO Number}}` *(OPTIONAL — only if Customer requires a PO reference)* |

A change to any contact above takes effect when the changing Party gives written notice using the notice mechanism in CSA §17 (Notices) or Section 9 of this Order Form.

---

## 3. Order details (services, quantities, term)

The subscription details for this Order are summarised below; full line-item detail is in Schedule 1.

- **Service Name:** `{{Service Name}}`
- **Service Description:** `{{Service Description}}`
- **Initial Term Length:** `{{Initial Term Length}}`
- **Initial Term Start Date:** `{{Initial Term Start}}`
- **Initial Term End Date:** `{{Initial Term End}}`
- **Subscribed Quantity:** `{{Subscribed Quantity}}` (e.g., "100 user seats", "5,000,000 API calls / month", or "10 GB storage")
- **Unit of Measure:** `{{Unit}}`
- **Overage Rate:** `{{Overage Rate}}` (e.g., "USD 12 per additional user / month")
- **True-Up Frequency:** `{{True-Up Frequency}}` (default "quarterly")
- **Provisioning Date:** `{{Provisioning Date}}` *(OPTIONAL — only if different from Initial Term Start)*

See **Schedule 1** for full line-item breakdown of services, SKUs, and quantities.

---

## 4. Fees & payment terms

Fees for this Order are summarised below; the full invoice schedule is in Schedule 2.

- **Total Order Value (Initial Term):** `{{Total Order Value}}` `{{Currency}}`
- **Annual Fee:** `{{Annual Fee}}` `{{Currency}}`
- **Billing Frequency:** `{{Billing Frequency}}` (default "Annual in advance")
- **Payment Terms:** `{{Payment Terms}}` (default "Net 30 from invoice date")
- **Invoice Currency:** `{{Currency}}`
- **Late Fee:** as set in CSA §6 (Fees & Payment).
- **Taxes:** Fees are exclusive of VAT, GST, sales, use, and similar transaction taxes; Customer is responsible for those amounts unless Customer provides a valid exemption certificate. Each Party bears its own income taxes.
- **Withholding:** if any deduction or withholding is required by law, Customer will gross up the payment so Vendor receives the contracted amount, subject to CSA §6.

See **Schedule 2** for the dated invoice schedule, including any prepayment, milestone, or quarterly true-up invoices.

---

## 5. Renewal terms

This Order renews on the elections below; either Party may opt out by giving non-renewal notice within the window stated.

- **Auto-Renewal:** `{{Auto-Renewal}}` (default "Yes")
- **Renewal Term Length:** `{{Renewal Term Length}}` (default "same length as the Initial Term")
- **Non-Renewal Notice Window:** `{{Non-Renewal Notice Window}}` (default "30 days before the end of the then-current term")
- **Annual Price Cap on Renewal:** `{{Annual Price Cap}}` (default "the lesser of 7% or the year-on-year change in the consumer price index published by `{{CPI Source}}`")
- **Notice channel for non-renewal:** the notice email listed in Section 2.

If Auto-Renewal is set to "No", this Order ends at the close of the Initial Term unless the Parties sign a new Order Form.

---

## 6. Service level (cross-reference SLA)

Service levels are governed by the SLA at CSA Exhibit B (`legalcode-sla`); this section records any Order-specific upgrades.

- **Default uptime tier:** as set in CSA Exhibit B (the `legalcode-sla`).
- **Order-specific uptime tier:** `{{Uptime Tier}}` (default "as set in CSA Exhibit B").
- **Premium support tier:** `{{Premium Support Tier}}` *(OPTIONAL — only if Customer has purchased a premium support plan)*.
- **Service credit cap:** as set in CSA Exhibit B unless expressly varied in Section 8.

Nothing in this section enlarges Vendor's liability beyond the cap stated in CSA §13 (Limitation of Liability).

---

## 7. Data residency, AI training, security tier

This section captures deal-specific elections about where Customer Data is processed, whether it may be used for AI model training, and the security tier that applies.

- **Data residency:** `{{Data Residency}}` (default "Vendor's primary processing region as disclosed in the Documentation").
- **Region pinning premium:** `{{Region Pinning Premium}}` *(OPTIONAL — only if Customer requires its data to be pinned to a specific region beyond Vendor's default)*.
- **AI training opt-in:** `{{AI Training Opt-In}}` (default "No — Vendor will NOT use Customer Data to train general-purpose AI models").
- **Model improvement using aggregated, de-identified telemetry:** permitted per CSA §8 unless Customer ticks "No" here: `{{Telemetry Opt-Out}}`.
- **Security tier:** `{{Security Tier}}` (default "Standard"; alternatives: "HIPAA", "FedRAMP Moderate", "FedRAMP High", "IL5", or sector-specific).
- **HIPAA BAA election:** see Schedule 3 if checked. *(OPTIONAL — only if Customer transmits PHI through the Service.)*
- **Sub-processor list reference:** as published at `{{Sub-Processor List URL}}` and incorporated by reference into the CSA's Data Processing Addendum.

Where this section conflicts with the CSA's data-protection terms, the CSA controls except as Section 8 expressly varies it.

---

## 8. Order-specific overrides to the CSA

Default: **None — all CSA terms apply unchanged.**

The Parties may use this section to record any term that varies, supplements, or supersedes the CSA solely for this Order. Only the items expressly listed below override the CSA; everything else in the CSA continues to apply in full.

- Override 1: `{{Override 1}}` *(OPTIONAL — e.g., "Liability cap raised to two times fees paid in the prior 12 months")*
- Override 2: `{{Override 2}}` *(OPTIONAL — e.g., "Customer-specific indemnity carve-out for `{{Carve-Out Topic}}`")*
- Override 3: `{{Override 3}}` *(OPTIONAL)*

Order-Form overrides control over CSA terms only where this Order Form expressly says so (cross-reference CSA §2 (Structure) and §18 (Order of Precedence)).

---

## 9. Notices for this Order

Legal notices use the addresses and email in Section 2 and the notice mechanism in CSA §17 (Notices).

- **Operational and ticketing notices** (incidents, change windows, support escalations) may be sent to the operational contact in Section 2 by email or through the Vendor's support portal at `{{Support Portal URL}}`.
- **Billing notices** (invoice queries, dunning, refund requests) go to the billing / AR email in Section 2.
- **Security notices** (incident reports, vulnerability disclosures) go to `{{Vendor Security Contact}}` and `{{Customer Security Contact}}`, with a copy by the legal-notice channel for any incident that triggers a CSA §10 (Security) reporting obligation.

Notices given through operational channels do not satisfy CSA §17 unless the CSA expressly permits it for that notice type.

---

## 10. Signature block

Each Party signs below; counterpart and electronic signatures are valid per CSA §18.

> **`{{Vendor Legal Name}}`**
>
> By: ___________________________
> Name: `{{Vendor Signatory Name}}`
> Title: `{{Vendor Signatory Title}}`
> Date: ___________________________
>
> **`{{Customer Legal Name}}`**
>
> By: ___________________________
> Name: `{{Customer Signatory Name}}`
> Title: `{{Customer Signatory Title}}`
> Date: ___________________________

Counterparts and electronic signatures (eIDAS Regulation (EU) 910/2014, the U.S. E-SIGN Act, and Icelandic Lög nr. 28/2001 um rafrænar undirskriftir) are valid per CSA §18.

---

## Schedule 1 — Subscribed Services & Quantities

| Service / SKU | Description | Quantity | Unit | Initial Term Fee | Overage Rate | Notes |
|---|---|---|---|---|---|---|
| `{{Service Name}}` | `{{Service Description}}` | `{{Subscribed Quantity}}` | `{{Unit}}` | `{{Annual Fee}}` `{{Currency}}` | `{{Overage Rate}}` | `{{Schedule 1 Notes}}` |
| `{{Add-On SKU}}` | `{{Add-On Description}}` | `{{Add-On Quantity}}` | `{{Add-On Unit}}` | `{{Add-On Fee}}` `{{Currency}}` | `{{Add-On Overage}}` | *(OPTIONAL — additional SKU)* |
| `{{Add-On SKU 2}}` | `{{Add-On Description 2}}` | `{{Add-On Quantity 2}}` | `{{Add-On Unit 2}}` | `{{Add-On Fee 2}}` `{{Currency}}` | `{{Add-On Overage 2}}` | *(OPTIONAL — additional SKU)* |

Add additional rows as needed. Quantities measured per the metering methodology in the Documentation; true-ups occur per Section 3.

---

## Schedule 2 — Fees & Payment Schedule

| Invoice Date | Invoice Period | Amount | Currency | Payment Due | Description |
|---|---|---|---|---|---|
| `{{Initial Term Start}}` | Year 1 | `{{Annual Fee}}` | `{{Currency}}` | Net 30 | Initial Term annual fee |
| `{{Year 2 Invoice Date}}` | Year 2 | `{{Year 2 Fee}}` | `{{Currency}}` | Net 30 | *(OPTIONAL — only if multi-year)* |
| `{{Year 3 Invoice Date}}` | Year 3 | `{{Year 3 Fee}}` | `{{Currency}}` | Net 30 | *(OPTIONAL — only if multi-year)* |
| `{{True-Up Invoice Date}}` | True-up | as measured | `{{Currency}}` | Net 30 | Quarterly / annual true-up against Schedule 1 |
| `{{Milestone Invoice Date}}` | Milestone | `{{Milestone Amount}}` | `{{Currency}}` | Net 30 | *(OPTIONAL — only if milestone billing applies)* |

Add rows for multi-year prepayment, ramped billing, or milestone invoices as applicable. Currency and payment terms above default to the values in Section 4 unless this schedule states otherwise.

---

## Schedule 3 — Order-Specific Addenda

Tick each addendum that applies. An unticked addendum is not part of this Order.

- [ ] **HIPAA BAA** — Vendor and Customer execute the Business Associate Agreement (companion `legalcode-baa` template). *(OPTIONAL — only if PHI is involved.)*
- [ ] **FedRAMP** — Vendor's Service is operated in a FedRAMP-authorized environment at `{{FedRAMP Level}}` (Moderate / High); ATO date: `{{ATO Date}}`. *(OPTIONAL — only if FedRAMP authorization is required.)*
- [ ] **PCI-DSS** — Vendor's Service is operated in a PCI-DSS-compliant environment for cardholder data; AOC date: `{{AOC Date}}`. *(OPTIONAL — only if cardholder data flows through the Service.)*
- [ ] **GDPR Article 28 DPA** — Vendor and Customer execute the Data Processing Agreement (companion `legalcode-dpa` template). *(OPTIONAL — only if EU/UK personal data is involved.)*
- [ ] **Sector-specific addenda** — `{{Sector-Specific Addenda}}` (e.g., "GLBA Safeguards", "FERPA", "ITAR / EAR", "AICPA SOC 2"). *(OPTIONAL — list any sector-specific obligations.)*
- [ ] **Custom security questionnaire** — Vendor has completed Customer's security questionnaire dated `{{Security Questionnaire Date}}`. *(OPTIONAL — only if Customer requires a completed questionnaire.)*
- [ ] **Other** — `{{Other Addendum}}`. *(OPTIONAL — describe any other addendum the Parties want to attach.)*

Each ticked addendum is incorporated into this Order. If an addendum conflicts with the CSA, the conflict is resolved per CSA §18 (Order of Precedence) unless Section 8 of this Order expressly says otherwise.

---

## Appendix A — Merge fields used

The following Mustache merge fields appear in this template:

- `{{Order Form Number}}`
- `{{Order Form Effective Date}}`
- `{{Master Agreement Title}}`
- `{{Master Agreement Date}}`
- `{{Vendor Legal Name}}`
- `{{Vendor Address}}`
- `{{Vendor Signatory Name}}`
- `{{Vendor Signatory Title}}`
- `{{Vendor Notice Email}}`
- `{{Vendor AR Email}}`
- `{{Vendor Ops Contact}}`
- `{{Vendor Security Contact}}`
- `{{Customer Legal Name}}`
- `{{Customer Address}}`
- `{{Customer Signatory Name}}`
- `{{Customer Signatory Title}}`
- `{{Customer Notice Email}}`
- `{{Customer Billing Email}}`
- `{{Customer Ops Contact}}`
- `{{Customer Security Contact}}`
- `{{Customer PO Number}}`
- `{{Service Name}}`
- `{{Service Description}}`
- `{{Initial Term Length}}`
- `{{Initial Term Start}}`
- `{{Initial Term End}}`
- `{{Subscribed Quantity}}`
- `{{Unit}}`
- `{{Overage Rate}}`
- `{{True-Up Frequency}}`
- `{{Provisioning Date}}`
- `{{Total Order Value}}`
- `{{Annual Fee}}`
- `{{Currency}}`
- `{{Billing Frequency}}`
- `{{Payment Terms}}`
- `{{Auto-Renewal}}`
- `{{Renewal Term Length}}`
- `{{Non-Renewal Notice Window}}`
- `{{Annual Price Cap}}`
- `{{CPI Source}}`
- `{{Uptime Tier}}`
- `{{Premium Support Tier}}`
- `{{Data Residency}}`
- `{{Region Pinning Premium}}`
- `{{AI Training Opt-In}}`
- `{{Telemetry Opt-Out}}`
- `{{Security Tier}}`
- `{{Sub-Processor List URL}}`
- `{{Override 1}}`
- `{{Override 2}}`
- `{{Override 3}}`
- `{{Carve-Out Topic}}`
- `{{Support Portal URL}}`
- `{{Schedule 1 Notes}}`
- `{{Add-On SKU}}` / `{{Add-On Description}}` / `{{Add-On Quantity}}` / `{{Add-On Unit}}` / `{{Add-On Fee}}` / `{{Add-On Overage}}`
- `{{Add-On SKU 2}}` / `{{Add-On Description 2}}` / `{{Add-On Quantity 2}}` / `{{Add-On Unit 2}}` / `{{Add-On Fee 2}}` / `{{Add-On Overage 2}}`
- `{{Year 2 Invoice Date}}` / `{{Year 2 Fee}}`
- `{{Year 3 Invoice Date}}` / `{{Year 3 Fee}}`
- `{{True-Up Invoice Date}}`
- `{{Milestone Invoice Date}}` / `{{Milestone Amount}}`
- `{{FedRAMP Level}}`
- `{{ATO Date}}`
- `{{AOC Date}}`
- `{{Sector-Specific Addenda}}`
- `{{Security Questionnaire Date}}`
- `{{Other Addendum}}`

---

## Appendix B — Authoritative references

The following permissively licensed baselines were consulted while drafting this template; no consecutive run of five or more words is traceable to any of them.

- Common Paper — Order Form `[CC-BY-4.0]` *(primary baseline)*
- Common Paper — Cloud Services Agreement v2.1 Order Form exhibit `[CC-BY-4.0]`
- Bonterms — Cloud Terms Order Form attachments `[CC-BY-4.0]`
- GitHub — `site-policy` repository `[CC0]`
- Mozilla — public legal templates `[MPL-2.0]`
- eIDAS Regulation (EU) 910/2014 (referenced for electronic-signature recognition) `[VERIFY — citation only, not a drafting baseline]`
- U.S. E-SIGN Act, 15 U.S.C. §§ 7001 et seq. (referenced for electronic-signature recognition) `[VERIFY — citation only]`
- Icelandic Lög nr. 28/2001 um rafrænar undirskriftir (referenced for electronic-signature recognition) `[VERIFY — confirm current consolidated version]`

No content was drawn from any AWS, Microsoft, Google, Salesforce, Atlassian, or Stripe Order Form.

---

## Appendix C — Not legal advice

This template is provided for general informational purposes only. It is not legal advice and does not create a lawyer-client relationship between Fordæmi ehf., its affiliates, or the authors and any reader, downloader, or user. Laws, regulations, and market norms differ by jurisdiction, sector, and deal posture, and they change over time. Before signing any Order Form, each Party should obtain advice from a qualified lawyer admitted in the relevant jurisdiction who has reviewed the specific facts, risk profile, and applicable law. Use of this template is at the user's own risk and is governed by the licence terms set out in the frontmatter.
