---
title: Order Form — United Kingdom (DMCCA 2024 + UK CRA + Late Payment)
jurisdictions: [uk, gb]
statutes: [DMCCA-2024, UK-CRA-2015, DUAA-2025, UK-GDPR, DPA-2018, Late-Payment-Act-1998, Modern-Slavery-2015]
audience: [B2B]
license: MIT
last_updated: 2026-04-29
---

# Order Form — United Kingdom

**Order Form Number:** `{{Order Form Number}}`
**Order Form Effective Date:** `{{Order Form Effective Date}}`

---

## 1. Plain-language summary

This Order Form is a short commercial schedule under the Master Agreement titled `{{Master Agreement Title}}` dated `{{Master Agreement Date}}` (the **CSA**) between `{{Vendor Legal Name}}` (**Vendor**) and `{{Customer Legal Name}}` (**Customer**), recording the bargained deal points for one subscription.

If a term here conflicts with the CSA, the CSA prevails save where Section 8 expressly says otherwise. Schedules 1, 2, and 3 form part of this Order Form. The governing law is England and Wales unless the CSA states otherwise.

---

## 2. Parties & contacts

Companies House registrations, ICO registration details (for UK GDPR purposes), and contact channels are listed below.

| Field | Vendor | Customer |
|---|---|---|
| Legal name | `{{Vendor Legal Name}}` | `{{Customer Legal Name}}` |
| Company number (Companies House) | `{{Vendor Company Number}}` | `{{Customer Company Number}}` |
| Registered office | `{{Vendor Address}}` | `{{Customer Address}}` |
| ICO registration number (where applicable) | `{{Vendor ICO Reg No}}` | `{{Customer ICO Reg No}}` |
| Signatory name | `{{Vendor Signatory Name}}` | `{{Customer Signatory Name}}` |
| Signatory title | `{{Vendor Signatory Title}}` | `{{Customer Signatory Title}}` |
| Notice email (legal) | `{{Vendor Notice Email}}` | `{{Customer Notice Email}}` |
| Billing / AR email | `{{Vendor AR Email}}` | `{{Customer Billing Email}}` |
| Operational contact | `{{Vendor Ops Contact}}` | `{{Customer Ops Contact}}` |
| Purchase order reference | n/a | `{{Customer PO Number}}` *(OPTIONAL — only if Customer requires a PO reference)* |

ICO registration numbers cross-reference the Data Protection Act 2018 controller-registration regime and feed into CSA Exhibit C (the UK GDPR DPA). A contact change takes effect on written notice via CSA §17 (Notices) or Section 9.

---

## 3. Order details (services, quantities, term)

Headline subscription details below; SKU breakdown in Schedule 1.

- **Service Name / Description:** `{{Service Name}}` — `{{Service Description}}`
- **Initial Term:** `{{Initial Term Length}}` from `{{Initial Term Start}}` to `{{Initial Term End}}`
- **Subscribed Quantity / Unit:** `{{Subscribed Quantity}}` `{{Unit}}` (e.g., "100 user seats")
- **Overage Rate:** `{{Overage Rate}}` (e.g., "GBP 12 per additional user / month")
- **True-Up Frequency:** `{{True-Up Frequency}}` (default "quarterly")
- **Provisioning Date:** `{{Provisioning Date}}` *(OPTIONAL — if different from Initial Term Start)*

---

## 4. Fees & payment terms

Headline fees below; dated schedule in Schedule 2; statutory late-payment provisions apply alongside.

- **Total Order Value (Initial Term):** `{{Total Order Value}}` `{{Currency}}`
- **Annual Fee:** `{{Annual Fee}}` `{{Currency}}`
- **Billing Frequency:** `{{Billing Frequency}}` (default "Annual in advance")
- **Payment Terms:** `{{Payment Terms}}` (default "Net 30")
- **Invoice Currency:** `{{Currency}}` (default GBP)
- **Contractual late fee:** per CSA §6.

### 4.5 Late Payment of Commercial Debts (Interest) Act 1998

For B2B supplies in the course of business, statutory interest accrues on any sum unpaid by the agreed payment date at **8 percentage points above the Bank of England base rate** in force on the day the debt becomes overdue `[VERIFY current Bank of England base rate]`. Any contractual late-fee election in the CSA operates alongside, and not in place of, this statutory remedy; the statutory floor cannot be waived below without a substantial remedy.

### 4.6 Late Payment of Commercial Debts Regulations 2013

Vendor is also entitled to a fixed-sum recovery cost per overdue invoice on the sliding scale:

- **GBP 40** where the unpaid debt is less than GBP 1,000;
- **GBP 70** where the unpaid debt is GBP 1,000 or more but less than GBP 10,000;
- **GBP 100** where the unpaid debt is GBP 10,000 or more.

Reasonable additional recovery costs above the fixed sum are claimable as further compensation under the Regulations.

### 4.7 VAT and cross-border treatment

Fees are exclusive of VAT. Vendor will issue a VAT invoice in `{{Currency}}` (default GBP) compliant with the Value Added Tax Act 1994 and current HMRC guidance. Where the supply qualifies for the **B2B reverse charge** (e.g., certain cross-border digital services to a business outside the UK), Vendor will mark the invoice "reverse charge applies" and Customer will self-account `[VERIFY post-Brexit VAT rules and current HMRC guidance]`. Each Party bears its own direct taxes; if a deduction or withholding is required by law, Customer will gross up so Vendor receives the contracted amount, subject to CSA §6.

Refer to **Schedule 2** for the dated invoice schedule.

---

## 5. Renewal terms

This Order renews on the elections below; either Party may opt out within the stated window. Additional DMCCA 2024 reminder / cancellation rules may apply where Customer is a consumer or SME-treated-as-consumer.

- **Auto-Renewal:** `{{Auto-Renewal}}` (default "Yes")
- **Renewal Term Length:** `{{Renewal Term Length}}` (default "same as Initial Term")
- **Non-Renewal Notice Window:** `{{Non-Renewal Notice Window}}` (default "30 days before end of current term")
- **Annual Price Cap on Renewal:** `{{Annual Price Cap}}` (default "lower of 7% or the year-on-year CPIH change published by ONS")
- **Non-Renewal Channel:** Section 2 Vendor notice email or `{{Cancellation URL}}`.

### 5.1 DMCCA 2024 Part 4 — subscription contract reminders

**DMCCA 2024 Part 4** applies mainly to consumer and certain SME-treated-as-consumer arrangements; pure B2B is generally out of scope `[VERIFY DMCCA Pt 4 phased commencement]`. Where Customer is in scope, Vendor will:

- issue renewal reminders within Pt 4 Chapter 2 timing `[VERIFY commencement]`;
- provide a clear non-renewal route via `{{Vendor Notice Email}}` or `{{Cancellation URL}}`; and
- include a plain-English summary of renewal price, term length, and any cap.

If Auto-Renewal is "No", the Order ends at the close of the Initial Term. Pure B2B Parties may waive these reminder mechanics in Section 8.

---

## 6. Service level (cross-reference SLA)

Governed by CSA Exhibit B (the `legalcode-sla` UK variant); this section records Order-specific upgrades only.

- **Order-specific uptime tier:** `{{Uptime Tier}}` (default "as set in CSA Exhibit B").
- **Premium support tier:** `{{Premium Support Tier}}` *(OPTIONAL)*.
- **Service credit cap:** per CSA Exhibit B unless varied in Section 8.
- **Operational-resilience reporting (FCA / PRA Customers):** see §7.7 and CSA SLA UK §11.10–11.11.

Nothing here enlarges liability beyond CSA §13.

---

## 7. Data residency, AI training, security tier

Deal-specific elections anchored in the UK GDPR / DPA 2018 framework.

### 7.1 Data residency

`{{Data Residency}}` (default "United Kingdom" or "EEA + UK under the UK adequacy regulations"). Region pinning premium: `{{Region Pinning Premium}}` *(OPTIONAL)*.

### 7.2 UK GDPR and DPA 2018

Processing of personal data is governed by **CSA Exhibit C** (UK DPA variant), incorporating Article 28 of the UK GDPR and Part 2 of the Data Protection Act 2018, ICO guidance, and the UK IDTA / UK Addendum to the EU SCCs for restricted transfers.

### 7.3 AI training opt-in

`{{AI Training Opt-In}}` (default "No — Vendor will not use Customer Data to train general-purpose AI models"). De-identified telemetry is permitted per CSA §8 unless Customer ticks "No" via `{{Telemetry Opt-Out}}`.

### 7.4 Data (Use and Access) Act 2025

Where Customer relies on a recognised legitimate interest introduced or clarified by **DUAA 2025**, the Parties will document the lawful basis and balancing test in CSA Exhibit C `[VERIFY DUAA 2025 phased commencement]`, and Vendor will furnish the Article 30 records of processing.

### 7.5 Security tier

`{{Security Tier}}` (default "NCSC Cyber Essentials"; alternatives: "Cyber Essentials Plus", "ISO 27001", "ISO 27017", or sector-specific). Vendor will keep certification current through the term and share the current certificate or AoC on request.

### 7.6 NIS Regulations 2018 entity classification

`{{NIS Entity Class}}` ("OES" / "RDSP" / "N/A"). Where Customer is OES or RDSP under the **NIS Regulations 2018**, Vendor will cooperate with reporting and audit obligations per CSA SLA UK §17.2.

### 7.7 FCA / PRA operational resilience

Where Customer is FCA / PRA-regulated, Customer will flag the Service as an Important Business Service or material outsourcing where applicable, and Vendor will support resilience, impact-tolerance, incident reporting, and exit planning per CSA SLA UK §11.10–11.11. SYSC, SUP, and the PRA Rulebook (Outsourcing, Operational Resilience) feed in by reference.

### 7.8 Sub-processor list

Published at `{{Sub-Processor List URL}}` and incorporated by reference into the CSA's DPA.

Where this section conflicts with the CSA's data-protection terms, the CSA controls save as Section 8 expressly varies it.

---

## 8. Order-specific overrides to the CSA

Default: **None — all CSA terms apply unchanged.** Only items expressly listed below override the CSA; everything else continues to apply.

- Override 1: `{{Override 1}}` *(OPTIONAL — e.g., "Liability cap raised to 2× fees paid in prior 12 months")*
- Override 2: `{{Override 2}}` *(OPTIONAL — e.g., "Indemnity carve-out for `{{Carve-Out Topic}}`")*
- Override 3: `{{Override 3}}` *(OPTIONAL)*

### 8.1 Sector-specific flow-downs

Where applicable, the corresponding flow-down terms in the CSA Annex (UK Sector Flow-Downs) take effect:

- **FCA-regulated Customer:** Vendor cooperates with FCA Handbook compliance (SYSC 8, SYSC 13, SYSC 15A) and applicable outsourcing / resilience guidance.
- **PRA-regulated Customer:** Vendor cooperates with PRA Rulebook compliance (Outsourcing, Operational Resilience, SS2/21).
- **Online Safety Act 2023 in-scope Customer:** Vendor supports category obligations per CSA §6 (UGC) and the `legalcode-tos` UK variant.
- **Bribery Act 2010:** each Party represents that it has adequate procedures designed to prevent bribery on its behalf under section 7.
- **Modern Slavery Act 2015:** any Party meeting the turnover threshold publishes a current section 54 statement and shares it on request `[VERIFY current Modern Slavery Act threshold]`.

### 8.2 DUAA-specific overrides

Additional measures required by Customer's reliance on a DUAA-introduced legitimate interest, beyond CSA Exhibit C: `{{DUAA Override}}` *(OPTIONAL)*.

Order-Form overrides control over CSA terms only where this Order Form expressly says so (cross-reference CSA §2 and §18).

---

## 9. Notices for this Order

Legal notices use the contacts in Section 2 and the mechanism in CSA §17. UK postal notices must go to the registered office in Section 2 with delivery confirmation (recorded delivery or equivalent courier).

- **Operational notices** (incidents, change windows, support escalations) — to the Section 2 ops contact or via Vendor's support portal at `{{Support Portal URL}}`.
- **Billing notices** — to the Section 2 billing / AR email.
- **Security and data-breach notices** (incident reports, vulnerability disclosures, UK GDPR Article 33 / 34) — to `{{Vendor Security Contact}}` and `{{Customer Security Contact}}`, copied via the legal channel for any CSA §10 reporting obligation.
- **DMCCA Pt 4 cancellation notices** (where applicable) — via `{{Cancellation URL}}` or by emailing `{{Vendor Notice Email}}` with the subject line "Non-renewal — Order Form `{{Order Form Number}}`".

Operational-channel notices do not satisfy CSA §17 unless the CSA expressly permits it.

---

## 10. Signature block

Each Party signs below; counterparts and electronic signatures are valid per CSA §18.

> **{{Vendor Legal Name}}** (Company No. `{{Vendor Company Number}}`)
> By: ___________________________  
> Name: `{{Vendor Signatory Name}}`  
> Title: `{{Vendor Signatory Title}}`  
> Date: ___________________________
>
> **{{Customer Legal Name}}** (Company No. `{{Customer Company Number}}`)
> By: ___________________________  
> Name: `{{Customer Signatory Name}}`  
> Title: `{{Customer Signatory Title}}`  
> Date: ___________________________

Counterparts and electronic signatures executed under retained eIDAS, the Electronic Communications Act 2000, and SI 2016/696 (as updated) are valid `[VERIFY post-REUL retention]`. The **Contracts (Rights of Third Parties) Act 1999** is excluded save where a benefit is expressly granted (see CSA §18.11).

---

## Schedule 1 — Subscribed Services & Quantities

| Service / SKU | Description | Quantity | Unit | Initial Term Fee | Overage | Notes |
|---|---|---|---|---|---|---|
| `{{Service Name}}` | `{{Service Description}}` | `{{Subscribed Quantity}}` | `{{Unit}}` | `{{Annual Fee}}` `{{Currency}}` | `{{Overage Rate}}` | `{{Schedule 1 Notes}}` |
| `{{Add-On SKU}}` | `{{Add-On Description}}` | `{{Add-On Quantity}}` | `{{Add-On Unit}}` | `{{Add-On Fee}}` `{{Currency}}` | `{{Add-On Overage}}` | *(OPTIONAL)* |
| `{{Add-On SKU 2}}` | `{{Add-On Description 2}}` | `{{Add-On Quantity 2}}` | `{{Add-On Unit 2}}` | `{{Add-On Fee 2}}` `{{Currency}}` | `{{Add-On Overage 2}}` | *(OPTIONAL)* |

Add rows as needed. Quantities are measured per the Documentation; true-ups follow Section 3.

---

## Schedule 2 — Fees & Payment Schedule

| Invoice Date | Invoice Period | Amount | Currency | Payment Due | Description |
|---|---|---|---|---|---|
| `{{Initial Term Start}}` | Year 1 | `{{Annual Fee}}` | `{{Currency}}` | Net 30 | Initial Term annual fee |
| `{{Year 2 Invoice Date}}` | Year 2 | `{{Year 2 Fee}}` | `{{Currency}}` | Net 30 | *(OPTIONAL — multi-year)* |
| `{{Year 3 Invoice Date}}` | Year 3 | `{{Year 3 Fee}}` | `{{Currency}}` | Net 30 | *(OPTIONAL — multi-year)* |
| `{{True-Up Invoice Date}}` | True-up | as measured | `{{Currency}}` | Net 30 | True-up against Schedule 1 |
| `{{Milestone Invoice Date}}` | Milestone | `{{Milestone Amount}}` | `{{Currency}}` | Net 30 | *(OPTIONAL — milestone billing)* |

Currency and payment terms default to Section 4 unless this schedule states otherwise. Statutory interest and fixed-sum recovery costs apply on overdue invoices per Sections 4.5–4.6.

---

## Schedule 3 — Order-Specific Addenda

Tick each addendum that applies. An unticked addendum is not part of this Order.

- [ ] **UK GDPR Article 28 DPA** — execute the companion `legalcode-dpa` UK variant. *(OPTIONAL — personal data only.)*
- [ ] **UK GDPR Article 28(3)(g) return / deletion on termination** — Customer's election (return or delete) under the DPA UK variant.
- [ ] **DMCCA Pt 4 confirmation** — Customer band: ☐ consumer, ☐ SME-treated-as-consumer, ☐ pure business. The first two bands trigger Section 5.1 reminder rules `[VERIFY DMCCA Pt 4 commencement]`.
- [ ] **Online Safety Act 2023** — Customer is an in-scope user-to-user / search service; Vendor supports OSA obligations per CSA §6 (UGC) and the `legalcode-tos` UK variant.
- [ ] **NCSC Cyber Essentials / Cyber Essentials Plus** — Vendor certified at `{{Security Tier}}`, valid through `{{CE Expiry Date}}`.
- [ ] **NIS Regulations 2018** — NIS class `{{NIS Entity Class}}`; cooperation per SLA UK §17.2.
- [ ] **FCA / PRA operational resilience** — cross-reference SLA UK §11.10. *(OPTIONAL.)*
- [ ] **Modern Slavery Act 2015 §54 statement** — published at `{{Modern Slavery Statement URL}}` `[VERIFY current Modern Slavery Act threshold]`.
- [ ] **Custom security questionnaire** — completed `{{Security Questionnaire Date}}`. *(OPTIONAL.)*
- [ ] **Other** — `{{Other Addendum}}`. *(OPTIONAL.)*

Each ticked addendum is incorporated into this Order; conflicts with the CSA are resolved per CSA §18 save as Section 8 expressly says otherwise.

---

## Appendix A — Merge fields used

Order metadata: `{{Order Form Number}}`, `{{Order Form Effective Date}}`, `{{Master Agreement Title}}`, `{{Master Agreement Date}}`.

Vendor: `{{Vendor Legal Name}}`, `{{Vendor Company Number}}`, `{{Vendor Address}}`, `{{Vendor ICO Reg No}}`, `{{Vendor Signatory Name}}`, `{{Vendor Signatory Title}}`, `{{Vendor Notice Email}}`, `{{Vendor AR Email}}`, `{{Vendor Ops Contact}}`, `{{Vendor Security Contact}}`.

Customer: `{{Customer Legal Name}}`, `{{Customer Company Number}}`, `{{Customer Address}}`, `{{Customer ICO Reg No}}`, `{{Customer Signatory Name}}`, `{{Customer Signatory Title}}`, `{{Customer Notice Email}}`, `{{Customer Billing Email}}`, `{{Customer Ops Contact}}`, `{{Customer Security Contact}}`, `{{Customer PO Number}}`.

Service / term: `{{Service Name}}`, `{{Service Description}}`, `{{Initial Term Length}}`, `{{Initial Term Start}}`, `{{Initial Term End}}`, `{{Subscribed Quantity}}`, `{{Unit}}`, `{{Overage Rate}}`, `{{True-Up Frequency}}`, `{{Provisioning Date}}`.

Fees: `{{Total Order Value}}`, `{{Annual Fee}}`, `{{Currency}}`, `{{Billing Frequency}}`, `{{Payment Terms}}`.

Renewal: `{{Auto-Renewal}}`, `{{Renewal Term Length}}`, `{{Non-Renewal Notice Window}}`, `{{Annual Price Cap}}`, `{{Cancellation URL}}`.

SLA / data / security: `{{Uptime Tier}}`, `{{Premium Support Tier}}`, `{{Data Residency}}`, `{{Region Pinning Premium}}`, `{{AI Training Opt-In}}`, `{{Telemetry Opt-Out}}`, `{{Security Tier}}`, `{{CE Expiry Date}}`, `{{NIS Entity Class}}`, `{{Sub-Processor List URL}}`, `{{Modern Slavery Statement URL}}`.

Overrides / addenda: `{{Override 1}}`, `{{Override 2}}`, `{{Override 3}}`, `{{Carve-Out Topic}}`, `{{DUAA Override}}`, `{{Support Portal URL}}`, `{{Schedule 1 Notes}}`, `{{Security Questionnaire Date}}`, `{{Other Addendum}}`.

Add-on / multi-year fields: `{{Add-On SKU}}`/`{{Add-On Description}}`/`{{Add-On Quantity}}`/`{{Add-On Unit}}`/`{{Add-On Fee}}`/`{{Add-On Overage}}` (and `*2` variants); `{{Year 2 Invoice Date}}`/`{{Year 2 Fee}}`, `{{Year 3 Invoice Date}}`/`{{Year 3 Fee}}`, `{{True-Up Invoice Date}}`, `{{Milestone Invoice Date}}`/`{{Milestone Amount}}`.

---

## Appendix B — Authoritative references

Permissively licensed baselines and primary-source materials consulted; no consecutive run of five or more words is traceable to any of them.

- Common Paper — Order Form `[CC-BY-4.0]` *(primary baseline)*; CSA v2.1 Order Form exhibit `[CC-BY-4.0]`
- Bonterms — Cloud Terms Order Form attachments `[CC-BY-4.0]`
- GitHub `site-policy` `[CC0]`; Mozilla public legal templates `[MPL-2.0]`
- legislation.gov.uk `[OGL]`: DMCCA 2024 `[VERIFY commencement]`; UK CRA 2015; DUAA 2025 `[VERIFY commencement]`; UK GDPR (retained) and DPA 2018 `[VERIFY post-REUL retention]`; Late Payment of Commercial Debts (Interest) Act 1998; Late Payment Regulations 2013; NIS Regulations 2018; Online Safety Act 2023; Modern Slavery Act 2015 `[VERIFY threshold]`; Bribery Act 2010; Contracts (Rights of Third Parties) Act 1999; Electronic Communications Act 2000 and SI 2016/696 `[VERIFY post-REUL retention]`
- ico.org.uk `[OGL]` — UK GDPR, Article 28, IDTA / UK Addendum guidance
- cma.gov.uk `[OGL]` — DMCCA 2024 implementation guidance `[VERIFY status]`
- ncsc.gov.uk `[OGL]` — Cyber Essentials / Cyber Essentials Plus scheme
- fca.org.uk `[OGL]` — FCA Handbook (SYSC, SUP) and operational-resilience policy
- gov.uk `[OGL]` — HMRC VAT guidance, post-Brexit cross-border digital services `[VERIFY current HMRC guidance]`

No content was drawn from any AWS, Microsoft, Google, Salesforce, Atlassian, or Stripe Order Form.

---

## Appendix C — Not legal advice

This template is for general informational purposes only. It is not legal advice and does not create a solicitor-client or other lawyer-client relationship between Fordæmi ehf., its affiliates, or the authors and any reader. Laws, regulator guidance, and market norms differ by jurisdiction, sector, and deal posture, and they change over time; the UK regime in particular is in active flux as DMCCA 2024 and DUAA 2025 phase in and as HMRC, the ICO, the CMA, the FCA, and the PRA publish updated guidance. Before signing any Order Form, each Party should obtain advice from a solicitor admitted in England and Wales (or another relevant UK jurisdiction) who has reviewed the specific facts, risk profile, and applicable law. Use of this template is at the user's own risk and is governed by the licence terms in the frontmatter.
