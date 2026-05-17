---
title: Order Form — EU/EEA (Data Act + GDPR + Late Payment + DE-AGB)
jurisdictions: [eu, eea, de]
statutes: [Data-Act-2023/2854, GDPR, Late-Payment-2011/7, AI-Act-2024/1689, BGB, GeschGehG]
audience: [B2B]
license: MIT
last_updated: 2026-04-29
---

# Order Form — EU/EEA Variant

**Order Form No.:** `{{Order Form Number}}`
**Order Form Date:** `{{Order Form Date}}`
**Master Agreement:** `{{Master Agreement Title}}` dated `{{Master Agreement Date}}` (the "**CSA**")

This Order Form is governed by the CSA. Where this Order Form and the CSA conflict, the CSA controls except for items expressly identified in §8 (Order-specific overrides) of this Order Form.

---

## 1. Plain-language summary

This section explains, in plain words, what the Parties are buying and selling under this Order Form.

`{{Customer Short Name}}` subscribes to `{{Service Name}}` from `{{Vendor Short Name}}` for `{{Initial Term Length}}` starting `{{Initial Term Start}}`. Initial-Term value: `{{Total Order Value}}` `{{Currency}}`, billed `{{Billing Frequency}}` on `{{Payment Terms}}`. Data hosted in `{{Data Residency}}` (default: EEA). AI-training opt-in: `{{AI Training Opt-In}}` (default: No). This Order Form attaches to the CSA and applies EU/EEA defaults: late-payment interest (Dir. 2011/7/EU), VAT reverse-charge (Art. 196 VAT Directive) for cross-border B2B, GDPR Art. 28 terms in the companion DPA, Data Act portability/switching commitments (Reg. 2023/2854), and Schriftform thresholds (§ 126a BGB) for German Customers.

This summary is informational. Operative obligations live in §§2–10 and the CSA.

---

## 2. Parties & contacts

This section identifies who is signing and where notices go.

### 2.1 Vendor

| Field | Value |
|---|---|
| Legal name | `{{Vendor Legal Name}}` |
| Legal-entity number | `{{Vendor Legal Entity Number}}` (e.g., Handelsregister-Nr., SIRET, RCS, KvK-nr., VAT-id) |
| Registered address | `{{Vendor Address}}` |
| Country of incorporation | `{{Vendor Country}}` |
| Notice email (legal) | `{{Vendor Notice Email}}` |
| Accounts-receivable email | `{{Vendor AR Email}}` |
| Signatory | `{{Vendor Signatory Name}}`, `{{Vendor Signatory Title}}` |

### 2.2 Customer

| Field | Value |
|---|---|
| Legal name | `{{Customer Legal Name}}` |
| Legal-entity number | `{{Customer Legal Entity Number}}` (e.g., Handelsregister-Nr., SIRET, RCS, KvK-nr., VAT-id) |
| Registered address | `{{Customer Address}}` |
| Country of incorporation | `{{Customer Country}}` |
| Notice email (legal) | `{{Customer Notice Email}}` |
| Billing email (AP) | `{{Customer Billing Email}}` |
| Purchase-order number (OPTIONAL) | `{{Customer PO Number}}` |
| Signatory | `{{Customer Signatory Name}}`, `{{Customer Signatory Title}}` |

### 2.3 Schriftform note (DE Customers)

OPTIONAL — only if `{{Customer Country}}` is Germany or this Order has liability allocations over `{{German Schriftform Threshold}}` (default EUR 50,000). Where § 126 BGB Schriftform applies, the Parties satisfy it via qualified electronic signature under § 126a BGB. See §10. `[VERIFY MS-specific form requirements]`

### 2.4 Authorised contacts

OPTIONAL — operational contacts beyond §2 legal-notice contacts. Authorised users and admin contacts are listed at `{{Authorized Users URL}}` or attached to Schedule 1.

---

## 3. Order details (services, quantities, term)

This section names the product, the volume, and the duration.

### 3.1 Service

`{{Vendor Short Name}}` provides `{{Service Name}}` to `{{Customer Short Name}}` as a hosted service per the CSA. Functional scope, modules, and add-ons appear in **Schedule 1**.

### 3.2 Subscribed quantity and overage

Subscribed quantity: `{{Subscribed Quantity}}` (units in Schedule 1: seats, API calls, GB, etc.). Overage is billed at `{{Overage Rate}}` per unit and reconciled `{{True-Up Frequency}}`.

### 3.3 Initial Term

| Field | Value |
|---|---|
| Initial Term length | `{{Initial Term Length}}` |
| Initial Term start | `{{Initial Term Start}}` |
| Initial Term end | `{{Initial Term End}}` |

### 3.4 Permitted Affiliates

OPTIONAL — only if Customer Affiliates use the Service under this Order. Permitted Affiliates are listed at `{{Affiliates URL}}` or attached as a sub-schedule to Schedule 1. Affiliates are bound by the CSA.

---

## 4. Fees & payment terms

This section sets price, currency, invoice cadence, late-payment consequences, and VAT handling.

### 4.1 Fees and currency

The annualised fee is `{{Annual Fee}}` `{{Currency}}` (default: EUR). The total contract value across the Initial Term is `{{Total Order Value}}` `{{Currency}}`. A line-by-line price schedule appears in **Schedule 2**.

### 4.2 Billing cadence and payment

Vendor invoices on a `{{Billing Frequency}}` basis. Each invoice is due `{{Payment Terms}}` (default: Net 30) from invoice date. Customer pays in `{{Currency}}` to the bank details on each invoice.

### 4.3 Disputed amounts

Customer must notify Vendor in writing of any disputed amount within fifteen (15) calendar days of invoice date. Undisputed amounts remain due. Disputed amounts in good-faith dispute do not accrue late-payment interest.

### 4.4 Taxes

Fees exclude all taxes. Customer pays applicable taxes other than those on Vendor's net income, employment, or property.

### 4.5 Late-payment statutory interest (Directive 2011/7/EU)

For B2B Customers in an EU Member State, undisputed overdue amounts accrue statutory late-payment interest at the rate set by the Member State implementing Directive 2011/7/EU, being not less than **eight (8) percentage points above the European Central Bank reference rate** in force on the first day of the relevant half-year (or the equivalent national reference rate in non-euro Member States). The reference-rate snapshot is recorded as `{{ECB Reference Rate Date}}` on each invoice. Article 7 prohibits B2B terms falling below the statutory rate; nothing here purports to do so.

### 4.6 Recovery costs (Directive 2011/7/EU, Article 6)

In addition to §4.5 interest, Vendor is entitled to a flat **EUR 40 per overdue invoice** plus reasonable additional collection costs actually incurred, consistent with Article 6 as transposed in the Member State of Customer's establishment.

### 4.7 VAT (Article 196 reverse charge)

Where Vendor and Customer are both VAT-registered businesses in different EU Member States, Vendor invoices without VAT and Customer self-accounts under the reverse-charge mechanism per Article 196 of Directive 2006/112/EC. Each Party warrants its VAT ID is valid and VIES-confirmed. Where the reverse charge does not apply, Vendor charges and remits VAT at the applicable rate.

### 4.8 Multi-currency and hedging

Default invoice currency is EUR. Where `{{Currency}}` differs, Customer bears any FX risk between invoice and payment dates. Hedging is Customer's responsibility. Vendor will not offer mid-Term re-pricing solely on currency movement unless agreed in §8.

### 4.9 Payment for hosted services

Payment for hosted-service Fees is not contingent on acceptance or deliverables, except as Schedule 2 or §8 expressly states.

---

## 5. Renewal terms

This section covers what happens when the Initial Term ends.

### 5.1 Auto-renewal default

This Order Form auto-renews for `{{Renewal Term Length}}` (default: same as Initial Term). Flag: `{{Auto-Renewal}}` (default: Yes).

### 5.2 Non-renewal notice

Either Party may prevent auto-renewal by written notice at least `{{Non-Renewal Notice Window}}` days (default: 30) before the then-current term ends. Customer may submit non-renewal via `{{Vendor Notice Email}}` or, where offered, `{{Cancellation URL}}`.

### 5.3 Modernisation Directive transparency

OPTIONAL — only if Vendor's offering meets the "online marketplace" threshold under Dir. 2019/2161/EU or its national transposition. Where applicable, Vendor provides pre-contractual transparency on ranking parameters, price personalisation, and cancellation pathways. `[VERIFY MS-specific transposition]`

### 5.4 Renewal-price cap

Unless agreed otherwise in writing, per-unit price on renewal will not increase by more than `{{Annual Price Cap}}` (default: the lesser of 7% or local CPI for the prior 12 months) over the immediately preceding term.

### 5.5 No mid-Term termination for convenience

Neither Party may terminate this Order Form for convenience during a then-current term, except as the CSA expressly permits.

---

## 6. Service level (cross-reference SLA)

This section points to the SLA and notes any upgrades.

### 6.1 SLA reference

The Service is subject to the SLA in CSA **Exhibit B (EU variant)** or the standalone SLA referenced in the CSA. The default uptime tier applies unless §6.2 says otherwise.

### 6.2 Uptime-tier upgrade

OPTIONAL — only if `{{Uptime Tier}}` is non-default. Schedule 1 records the upgraded commitment, service credits, and incident-response time changes.

### 6.3 Sector-specific resilience

OPTIONAL — only if Customer is subject to DORA (Reg. 2022/2554), NIS2 (Dir. 2022/2555), or sector resilience rules (BaFin BAIT/VAIT, BSI KritisV). RTOs, RPOs, and incident-notification windows are recorded in §8 or a sub-schedule. `[VERIFY DORA Art. 30 register-of-information requirements]`

---

## 7. Data residency, AI training, security tier

This is the EU-specific data, AI, and security section. It interacts with the companion DPA and the Data Act.

### 7.1 Data residency

Hosted region is `{{Data Residency}}` (default: "EEA"). Member-State or city-level pinning is OPTIONAL and, if elected, is recorded in Schedule 1. Vendor will not store Customer Personal Data outside the elected region without Customer's prior written instruction or the use of a transfer mechanism permitted by Chapter V GDPR.

### 7.2 EU sovereignty stack (OPTIONAL)

OPTIONAL — only if Customer requires alignment with a recognised EU sovereignty framework. Customer elects `{{Sovereignty Stack}}`, which may be one of: SecNumCloud (FR — ANSSI), C5 (DE — BSI), ENS (ES — CCN), or GAIA-X-aligned hosting. Vendor confirms current alignment status and any conditions in Schedule 3. `[VERIFY EUCS adoption status, GAIA-X label currency]`

### 7.3 Data Act portability and switching (Reg. 2023/2854, Arts. 4 / 23–25)

Consistent with Articles 4 and 23–25 of the Data Act: (a) Customer retains the right to access, port, and reuse data Customer generates through use of the Service; (b) Vendor will support switching by exporting Customer data and (where relevant) configuration in **structured, commonly used, machine-readable formats** with reasonable documentation; (c) Vendor will use commercially reasonable efforts to remove technical, contractual, and economic obstacles to switching, and will progress toward elimination of egress fees for switching on the timeline contemplated by the Data Act `[VERIFY commencement timing for Arts. 23–25, including the January 2027 target]`; (d) specific deliverables, formats, and timelines are recorded in Schedule 3 or the companion DPA.

### 7.4 AI training opt-in

`{{AI Training Opt-In}}` (default: "No"). If "Yes", this is Customer's express, documented instruction permitting Vendor to use Customer Data (excluding Customer Personal Data unless additionally and separately authorised in the DPA) to train models. The scope, retention, and any de-identification requirements are recorded in Schedule 3. The default is opt-out: Customer Data is not used for model training.

### 7.5 EU AI Act tier flag (Reg. 2024/1689)

`{{AI Act Risk Class}}` is one of: prohibited / high-risk / limited-risk / minimal-risk / GPAI. Vendor confirms classification under Reg. 2024/1689 and provides tier-appropriate documentation per Schedule 3 (e.g., technical documentation, instructions for use, conformity-assessment status, GPAI transparency). `[VERIFY phased AI Act commencement and per-class obligations]`

### 7.6 NIS2 / DORA flag

`{{NIS2 Entity Class}}` is one of: essential / important / N/A. Where Customer is an essential / important entity under NIS2 or a financial entity under DORA, Vendor will support Customer's incident-reporting, supply-chain risk-management, and (for DORA) information-register obligations. Where DORA Article 30 contractual provisions apply, terms attach as a sub-schedule. `[VERIFY MS-specific NIS2 transposition]`

### 7.7 Security tier

Baseline `{{Security Tier}}`. Acceptable values include ISO/IEC 27001, 27017, 27018, 27701, EUCS (basic / substantial / high), or sector frameworks (BSI C5, BaFin BAIT/VAIT, ANSSI SecNumCloud). Current attestations and valid-through dates are recorded in Schedule 3. `[VERIFY EUCS adoption status]`

### 7.8 Sub-region and cross-border (B2B EEA)

OPTIONAL — only if the Parties wish to permit specific sub-regions or restrict to specific Member States. Permitted sub-regions are listed in Schedule 1. Any cross-border processing outside the elected region is governed by Chapter V GDPR and the companion DPA (including SCCs where relevant).

### 7.9 Trade secrets (Dir. 2016/943 / GeschGehG)

Customer Data and Vendor Materials may include trade secrets within Dir. 2016/943 and national transpositions (in Germany, GeschGehG). Each Party will maintain reasonable steps under those laws to keep such information secret.

---

## 8. Order-specific overrides to the CSA

This section lists every clause where this Order Form changes the CSA. Anything not listed here remains as in the CSA.

### 8.1 Override format

Each override states: (a) the CSA section changed; (b) the new wording or value; (c) whether the change applies only to this Order Form or more broadly.

### 8.2 Standing overrides

OPTIONAL — only if any apply. Otherwise leave blank.

- **Liability cap variation:** [describe]
- **Indemnity carve-outs:** [describe]
- **Acceptance criteria for Schedule-1 deliverables:** [describe]
- **Service-credit mechanics in lieu of CSA defaults:** [describe]
- **DPA amendments:** see companion `legalcode-dpa` EU variant; record any amendment here as well

### 8.3 Sector-specific flow-downs

OPTIONAL — only where Customer's regulatory status requires it. Tick all that apply and attach the corresponding sub-schedule:

- [ ] **DORA Art. 30** — financial-entity Customers (register-of-information, exit-strategy)
- [ ] **eIDAS Reg. 910/2014 / 2024/1183** — QTSP Customers
- [ ] **MDR / IVDR (Regs. 2017/745, 2017/746)** — medical-device / IVD manufacturer Customers
- [ ] **PSD2 / DORA** — payment-services Customers
- [ ] **MiCA (Reg. 2023/1114)** — crypto-asset service-provider Customers
- [ ] **AIFMD / UCITS** — asset-management Customers
- [ ] **BaFin BAIT / VAIT / KAIT** — German regulated entities
- [ ] **GDPR Art. 9 / 10 special categories** — additional safeguards in DPA

`[VERIFY current sector framework versions]`

### 8.4 Flow-down language

Where a flow-down is selected, the operative contractual language attaches as a sub-schedule and forms part of the CSA for the duration of this Order.

---

## 9. Notices for this Order

This section says how to send legal notices for this Order specifically.

### 9.1 Notice channels

Legal notices are valid if sent to the postal address and notice email in §2 for the receiving Party. Operational notices follow the CSA channels and any portal in use.

### 9.2 Electronic signature (eIDAS)

Consistent with Reg. 910/2014 (eIDAS) as updated by Reg. 2024/1183, the Parties may execute using an advanced or qualified electronic signature. Each Party is responsible for using a signature-creation tool that meets the relevant assurance level.

### 9.3 Schriftform (DE Customers)

OPTIONAL — only if `{{Customer Country}}` is Germany. Where § 126 BGB Schriftform applies and electronic form is not excluded, the Parties satisfy it via a qualified electronic signature under § 126a BGB. For Order Forms exceeding `{{German Schriftform Threshold}}` (default EUR 50,000) or with material liability allocations, a QTS signature from an EU Trusted List provider is recommended. `[VERIFY MS-specific form requirements]`

### 9.4 Counterparts and language

This Order Form may be executed in counterparts (electronic or wet-ink), each an original. Executed in English; where a translation is appended, the English version controls except where mandatory local law requires otherwise (e.g., Toubon Law for French public entities). `[VERIFY MS-specific language rules]`

---

## 10. Signature block

The persons below sign on behalf of the Parties and warrant authority to bind.

> **{{Vendor Legal Name}}** ({{Vendor Legal Entity Number}})
> By: ___________________________
> Name: `{{Vendor Signatory Name}}`
> Title: `{{Vendor Signatory Title}}`
> Date: ___________________________
> Place: ___________________________
>
> **{{Customer Legal Name}}** ({{Customer Legal Entity Number}})
> By: ___________________________
> Name: `{{Customer Signatory Name}}`
> Title: `{{Customer Signatory Title}}`
> Date: ___________________________
> Place: ___________________________

Counterparts and electronic signatures are valid per CSA §18 and §9.2. For German Customers, a QTS signature under § 126a BGB is recommended for Order Forms over `{{German Schriftform Threshold}}` (default EUR 50,000) or where § 126 BGB Schriftform applies.

---

## Schedule 1 — Subscribed Services & Quantities

A short, structured list of what is being bought and at what quantity.

| Line | Service / Module | Unit | Subscribed Quantity | Overage Rate (`{{Currency}}` per unit) | Notes |
|---|---|---|---|---|---|
| 1.1 | `{{Service Name}}` (base) | `{{Unit}}` | `{{Subscribed Quantity}}` | `{{Overage Rate}}` | |
| 1.2 | [add-on, if any] | | | | |
| 1.3 | [uptime upgrade] | tier | `{{Uptime Tier}}` | n/a | upgrades default SLA |
| 1.4 | [data-residency pin] | region | `{{Data Residency}}` | n/a | EEA / Member State / city |
| 1.5 | [sub-region permits] | region(s) | [list] | n/a | |

True-up cadence: `{{True-Up Frequency}}`.

---

## Schedule 2 — Fees & Payment Schedule

A short, structured list of when invoices issue and for what amount.

| Invoice # | Period covered | Issue date | Amount (`{{Currency}}`) | Notes |
|---|---|---|---|---|
| 1 | `{{Initial Term Start}}` – [period end] | `{{Initial Term Start}}` | [amount] | first invoice |
| 2 | [period] | [issue date] | [amount] | |
| ... | | | | |
| n | [period end] | `{{Initial Term End}}` | [amount] | final Initial-Term invoice |

Payment terms: `{{Payment Terms}}` (default Net 30). Invoice currency: `{{Currency}}` (default EUR). VAT: handled per §4.7. Late-payment interest under §4.5 from the day after due date for undisputed amounts. Recovery costs under §4.6.

---

## Schedule 3 — Order-Specific Addenda (EU)

Tick each addendum that applies. Each ticked item attaches as a sub-schedule (or cross-references the companion document).

- [ ] **GDPR Article 28 DPA** — execute companion `legalcode-dpa` EU variant (Art. 28(3), Chap. V transfers, sub-processor list, TOMs)
- [ ] **EU AI Act tier confirmation** — `{{AI Act Risk Class}}` under Reg. 2024/1689 with tier-appropriate documentation `[VERIFY phased commencement]`
- [ ] **EUCS assurance level** — basic / substantial / high `[VERIFY EUCS adoption]`
- [ ] **Data Act Art. 23–25 switching readiness** — export formats, switching deliverables, phased egress-fee elimination
- [ ] **GAIA-X / sovereignty-stack alignment** — `{{Sovereignty Stack}}` `[OPTIONAL]`
- [ ] **DORA Art. 30 ICT-services contractual provisions** — financial-entity Customers
- [ ] **MDR / IVDR flow-down** — medical-device or IVD manufacturer Customers
- [ ] **PSD2 / DORA payment-services flow-down** — payment / e-money Customers
- [ ] **eIDAS QTSP flow-down** — qualified trust service provider Customers
- [ ] **MiCA flow-down** — crypto-asset service provider Customers
- [ ] **NIS2 entity-class confirmation** — `{{NIS2 Entity Class}}` plus any incident-notification annex
- [ ] **BaFin BAIT / VAIT / KAIT** — German regulated entities
- [ ] **Other sector-specific addenda** — list as needed
- [ ] **Custom security questionnaire** — completed `{{Security Questionnaire Date}}`
- [ ] **Schriftform confirmation (DE)** — QES used where § 126a BGB applies

Each ticked item is incorporated by reference. Where an addendum and this Order Form conflict, the more protective term for the affected regulatory regime controls.

---

## Merge fields used

Mustache-style fields used in this template. Replace each before execution.

**Common (shared with core):** `{{Order Form Number}}`, `{{Order Form Date}}`, `{{Master Agreement Title}}`, `{{Master Agreement Date}}`, `{{Vendor Legal Name}}`, `{{Vendor Short Name}}`, `{{Vendor Address}}`, `{{Vendor Country}}`, `{{Vendor Signatory Name}}`, `{{Vendor Signatory Title}}`, `{{Vendor Notice Email}}`, `{{Vendor AR Email}}`, `{{Customer Legal Name}}`, `{{Customer Short Name}}`, `{{Customer Address}}`, `{{Customer Country}}`, `{{Customer Signatory Name}}`, `{{Customer Signatory Title}}`, `{{Customer Notice Email}}`, `{{Customer Billing Email}}`, `{{Customer PO Number}}` (OPTIONAL), `{{Service Name}}`, `{{Initial Term Length}}`, `{{Initial Term Start}}`, `{{Initial Term End}}`, `{{Renewal Term Length}}`, `{{Auto-Renewal}}`, `{{Non-Renewal Notice Window}}`, `{{Annual Price Cap}}`, `{{Currency}}`, `{{Payment Terms}}`, `{{Billing Frequency}}`, `{{Total Order Value}}`, `{{Annual Fee}}`, `{{Subscribed Quantity}}`, `{{Unit}}`, `{{Overage Rate}}`, `{{True-Up Frequency}}`, `{{Uptime Tier}}`, `{{Data Residency}}`, `{{AI Training Opt-In}}`, `{{Authorized Users URL}}`, `{{Affiliates URL}}`.

**EU/EEA-specific:** `{{Vendor Legal Entity Number}}` (Handelsregister-Nr., SIRET, RCS, KvK-nr., VAT-id), `{{Customer Legal Entity Number}}` (same), `{{ECB Reference Rate Date}}` (half-year snapshot for §4.5), `{{German Schriftform Threshold}}` (default EUR 50,000), `{{AI Act Risk Class}}` (prohibited / high-risk / limited-risk / minimal-risk / GPAI), `{{NIS2 Entity Class}}` (essential / important / N/A), `{{Sovereignty Stack}}` (SecNumCloud / C5 / ENS / GAIA-X-aligned, OPTIONAL), `{{Security Tier}}` (ISO 27001 / EUCS basic|substantial|high / C5 / SecNumCloud / etc.), `{{Cancellation URL}}` (Modernisation Directive transparency channel, OPTIONAL), `{{Security Questionnaire Date}}` (OPTIONAL).

---

## Authoritative references

Public-domain and permissively-licensed sources used as drafting guides. No verbatim text was copied.

- **EUR-Lex (public domain):** Reg. 2023/2854 (Data Act, Arts. 4, 23–25); Reg. 2016/679 (GDPR, Art. 28, Chap. V); Dir. 2011/7/EU (Late Payment, Arts. 3, 6, 7); Dir. 2006/112/EC (VAT, Art. 196); Reg. 2024/1689 (AI Act); Dir. 2022/2555 (NIS2); Reg. 2022/2554 (DORA, Art. 30); Reg. 910/2014 and Reg. 2024/1183 (eIDAS / eIDAS 2.0); Dir. 2019/2161 (Modernisation); Dir. 2016/943 (Trade Secrets); Reg. 2017/745 (MDR); Reg. 2017/746 (IVDR); Dir. 2015/2366 (PSD2); Reg. 2023/1114 (MiCA).
- **EU regulators:** EDPB (Art. 28 / transfers / processor guidance); European Commission (AI portal, Data Act guidance); ENISA (EUCS).
- **National:** gesetze-im-internet.de (BGB §§ 126, 126a; GeschGehG); BSI (C5); BfDI; ANSSI (SecNumCloud); CCN (ENS).
- **Permissive baselines:** Common Paper Order Form `[CC-BY-4.0]`; Common Paper CSA v2.1 Order Form exhibit `[CC-BY-4.0]`; Bonterms Cloud Terms Order Form attachments `[CC-BY-4.0]`; GitHub `site-policy` `[CC0]`; Mozilla legal templates `[MPL-2.0]`.

`[VERIFY]` flags mark items where commencement dates, transposition status, or framework adoption may have moved since `last_updated`. Confirm against the current EUR-Lex consolidated text before execution.

---

## Not legal advice

This template is provided for general informational purposes only. It is not legal advice and does not create a lawyer-client relationship. EU law is enacted at Union level but applied at Member-State level: thresholds, statutory-interest mechanics, Schriftform rules, sector framework adoptions, and translation requirements vary across the EEA. Have this Order Form reviewed by counsel qualified in the relevant Member State and any applicable sector regime before execution. Fordæmi ehf. (Legalcode) and the contributors disclaim all liability for use without such review.
