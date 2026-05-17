---
title: Order Form — United States
jurisdictions: [us, us-ca, us-ny, us-il, us-tx, us-de]
statutes: [CCPA, ARLDA-CA, GBL-527-a-NY, ARLDA-IL, ROSCA, FTC-Click-to-Cancel, UCC-2-201]
audience: [B2B]
license: MIT
last_updated: 2026-04-29
---

# Order Form — United States

> Baselines: Common Paper Order Form / CSA v2.1 `[CC-BY-4.0]`, Bonterms Cloud Terms `[CC-BY-4.0]`, GitHub `[CC0]`, Mozilla `[MPL-2.0]`, US public-domain government materials. Clean-room drafting; no 5+-word verbatim runs.

---

## 1. Plain-language summary

This Order Form sets out what `{{Customer Legal Name}}` is buying from `{{Vendor Legal Name}}`, the price, the term, and any special arrangements. It is governed by the parties' Cloud Services Agreement (the "CSA") dated `{{CSA Effective Date}}`; any conflict is resolved in favor of this Order Form for matters addressed here. Capitalized terms not defined here have the meaning given in the CSA. Nothing here is legal, tax, or compliance advice.

---

## 2. Parties & contacts

This section identifies the contracting parties and the people who receive operational notices.

**Vendor (Provider).**
- Legal name: `{{Vendor Legal Name}}`
- Form of entity / state of formation: `{{Vendor Entity Form}}` / `{{Vendor State of Formation}}`
- Principal place of business: `{{Vendor Address}}`
- Order contact (commercial): `{{Vendor Commercial Contact Name}}`, `{{Vendor Commercial Contact Email}}`
- Billing contact: `{{Vendor Billing Email}}`
- Legal notices contact: `{{Vendor Notice Email}}`
- Security / incident contact: `{{Vendor Security Email}}`

**Customer.**
- Legal name: `{{Customer Legal Name}}`
- Form of entity / state of formation: `{{Customer Entity Form}}` / `{{Customer State of Formation}}`
- Billing address: `{{Customer Billing Address}}`
- Order contact (commercial): `{{Customer Commercial Contact Name}}`, `{{Customer Commercial Contact Email}}`
- Accounts-payable / invoice intake email: `{{Customer AP Email}}`
- Purchase-order intake email `[OPTIONAL]`: `{{Customer PO Intake Email}}`
- Legal notices contact: `{{Customer Notice Email}}`
- Security / privacy contact: `{{Customer Security Email}}`

**OPTIONAL — only if Customer issues a purchase order.** Customer's PO Number `{{Customer PO Number}}` is for Customer's internal reference and AP matching only. The legal terms are exclusively the CSA and this Order Form. Preprinted, click-through, or electronically attached terms on Customer's PO, vendor portal, or supplier-registration form are expressly rejected and have no force, even if Vendor processes the PO for invoicing. This is Vendor's express objection under UCC §2-207 to any additional or different terms. Vendor accepts a PO term only via a written addendum signed by a duly authorized officer that specifically identifies and accepts that term.

---

## 3. Order details (services, quantities, term)

This section describes the Services Customer is purchasing, how much of each, and for how long.

- **Service offering(s):** `{{Service Offering Name}}` — `{{Service Edition or Tier}}`
- **Quantity unit (license, seat, workspace, environment, transaction, GB-month, request, token):** `{{Quantity Unit}}`
- **Quantity:** `{{Quantity}}`
- **Subscription Start Date:** `{{Subscription Start Date}}`
- **Initial Term Length:** `{{Initial Term Length}}` (default 12 months)
- **Initial Term End Date:** `{{Initial Term End Date}}`
- **Implementation / onboarding services `[OPTIONAL]`:** `{{Onboarding SOW Reference}}`
- **Order-form-level usage cap `[OPTIONAL]`:** `{{Usage Cap}}`
- **Overage handling `[OPTIONAL]`:** `{{Overage Rate}}` per `{{Overage Unit}}` invoiced `{{Overage Cadence}}`

Mid-term Quantity uplifts may be made by written request and Vendor confirmation; any uplift is co-terminous and pro-rated under §4. Downward adjustments are permitted only at renewal unless the CSA expressly allows true-down.

---

## 4. Fees & payment terms

This section sets the price, the invoicing cadence, and tax / late-fee mechanics.

- **§4.1 Subscription fee:** `{{Annual Subscription Fee Amount}}` `{{Currency}}` per `{{Billing Period}}`.
- **§4.2 One-time fees `[OPTIONAL]`:** `{{One-Time Fee Description}}` — `{{One-Time Fee Amount}}` `{{Currency}}`.
- **§4.3 Invoice cadence:** `{{Invoice Cadence}}` (default annual in advance). First invoice on Subscription Start Date.
- **§4.4 Payment terms:** Net `{{Net Days}}` (default 30) from invoice date. Payment method: `{{Payment Method}}` (ACH, wire, credit card, or Customer's accredited procurement portal).

**§4.5 Tax handling.** Fees are exclusive of sales, use, gross-receipts, VAT, excise, and similar transaction taxes ("Transaction Taxes"). Customer is responsible for Transaction Taxes properly assessed in any US state or local jurisdiction, except taxes on Vendor's net income, franchise, payroll, property, or employees. On request, Customer will deliver a current resale or exemption certificate (e.g., MTC Uniform Sales & Use Tax Exemption Certificate or direct-pay permit). The parties will exchange a current IRS Form W-9 (US persons) or Form W-8 series (e.g., W-8BEN-E) before first payment, as required by 26 U.S.C. §3406 and §1441 et seq.

**§4.6 Late fees.** Late payments accrue interest at the rate in CSA §4.5 — typically the lesser of 1.5 percent per month or the maximum rate permitted by applicable state law. Several states cap commercial interest below this figure (e.g., Connecticut may cap at 12 percent APR `[VERIFY]`); in any such state the maximum lawful rate applies. Vendor may suspend Services for non-payment per CSA §4.

---

## 5. Renewal terms

This section explains how the subscription rolls over, how to stop it, and how the price can change.

> ### AUTOMATIC RENEWAL DISCLOSURE
>
> **This Order Form automatically renews.** Unless either party gives written notice of non-renewal, this Order Form renews for successive `{{Renewal Term Length}}` periods (default 12 months). To stop auto-renewal, give the other party `{{Non-Renewal Notice Window}}` (default 30) days' written notice before the end of the then-current term.
>
> **How to cancel.** Customer may cancel auto-renewal at any time via (a) the self-serve cancellation page at `{{Cancellation URL}}`, or (b) written notice to `{{Vendor Notice Email}}`. The cancellation method requires no more steps than the original sign-up.
>
> **Renewal price.** The renewal price will not increase by more than `{{Annual Price Cap}}` (default the lesser of 7 percent or the trailing 12-month change in the US BLS CPI-U, US City Average, All Items) above the prior term's annual fee, unless Customer agrees in writing.
>
> **Reminder.** Vendor will send Customer a renewal reminder by email to the §2 address not less than 30 and not more than 60 days before each automatic renewal, stating the renewal date, renewal price, and cancellation method.
>
> **State-specific notice.** This disclosure is intended to satisfy applicable US auto-renewal statutes: Cal. Bus. & Prof. Code §17602 (CA ARLDA), N.Y. GBL §527-a, Illinois ARLDA (815 ILCS 601), ROSCA (15 U.S.C. §§8401–8405), FTC Click-to-Cancel Rule (16 CFR Part 425) `[VERIFY commencement]`, and analogous OR (HB 2479), CO (HB 21-1063 `[VERIFY]`), and TX `[VERIFY]` statutes.

To renew on different commercial terms, the parties will execute an amendment or successor Order Form referencing this one by date and Order ID; absent that, the auto-renewal block above controls.

---

## 6. Service level (cross-reference SLA)

This section adopts the standard SLA and flags any upgrades.

Services are delivered subject to the SLA in CSA Exhibit B. Standard availability target, credit schedule, and exclusions apply unless an upgrade is selected as a Schedule 1 line item. **OPTIONAL — only if Customer is purchasing an upgrade.** Upgraded tier `{{Upgraded SLA Tier}}` (e.g., 99.95 percent uptime, sub-15-minute Sev-1 response, premium support); incremental fee in §4 / Schedule 1. SLA carve-outs continue unmodified. Service credits are Customer's exclusive remedy except where the CSA provides a chronic-failure termination right.

---

## 7. Data residency, AI training, security tier

This section configures where Customer Data lives, model-training opt-ins, and the security baseline.

- **§7.1 Primary processing region:** United States.
- **§7.2 Sub-region:** `{{Sub-Region}}` — one of US-East, US-West, US-Central (or "no preference").
- **§7.3 Backup / disaster-recovery region:** `{{DR Region}}` (default same primary region; cross-region DR available on request).
- **§7.4 Public-sector posture `[OPTIONAL — only for US government Customers or contractors processing government data]`:** FedRAMP `{{FedRAMP Level}}` (Low / Moderate / High), ATO `{{ATO Date}}`, DoD Impact Level `{{DoD Impact Level}}` (IL2 / IL4 / IL5 / IL6), CJIS Security Policy `{{CJIS Version}}`, StateRAMP / TX-RAMP / AZ-RAMP cross-recognition `{{StateRAMP Status}}`.
- **§7.5 HIPAA posture `[OPTIONAL — only if Customer is a Covered Entity or Business Associate processing PHI]`:** Vendor will execute the BAA at Schedule 3 (`legalcode-baa` companion). PHI handling is restricted to the HIPAA-eligible environment at `{{HIPAA Environment URL}}`.
- **§7.6 AI / model-training opt-in:** Default **No**. Customer Data, Confidential Information, prompts, completions, embeddings, and derived telemetry will not be used to train, fine-tune, or improve any general-purpose or third-party model. Aggregated, de-identified telemetry to operate, secure, and improve the Services is permitted per CSA §7. Colorado AI Act `[VERIFY effective date]` and California ADMT apply where the Services support consequential decision-making; Vendor provides impact-assessment artifacts on request.
- **§7.7 Privacy-law role designation:** CCPA / CPRA — `{{Service Provider Designation}}` (default "Service Provider" under Cal. Civ. Code §1798.140(ag); alternative "Contractor" under §1798.140(j) where Vendor receives PI under a written contract satisfying §1798.140(j)(1)(A)–(D)). Multi-state controller / processor terms (CO CPA, VA CDPA, CT CTDPA, UT UCPA, TX TDPSA, OR OCPA, successors) are addressed in CSA Exhibit C and incorporated by reference.
- **§7.8 Security tier:** `{{Security Tier}}` — Standard / Enhanced / Regulated. Tier-specific controls, attestations, and audit cadence are in CSA Exhibit D.

---

## 8. Order-specific overrides to the CSA

This section lists changes to the CSA that apply only to this Order Form.

Any term in this section overrides the corresponding CSA term solely for the Services under this Order Form and only for its term.

- **§8.1 Commercial overrides `[OPTIONAL]`:** `{{Commercial Override Description}}` — e.g., deal-specific liability-cap multiplier, bespoke termination-for-convenience window, or non-standard publicity right.
- **§8.2 Federal flow-downs `[OPTIONAL — federal Customers / primes / subcontractors]`:** FAR / DFARS clauses flow down only as commercial-item terms under FAR 12.301 and 52.244-6, and only to the extent self-deleting clauses are inapplicable: FAR 52.227-14 `[VERIFY alternates]`, FAR 52.227-19, DFARS 252.227-7013 / 7014, DFARS 252.204-7012. Conflicting non-commercial-item clauses are not accepted.
- **§8.3 State-government flow-downs `[OPTIONAL — state, local, tribal, or territorial Customers]`:**
  - California: Cal. Lab. Code §1102.5 whistleblower references `[VERIFY]`; iran-contracting and slavery-disclosure statutes where applicable.
  - Texas: SB 820 (K-12) `[VERIFY]`.
  - Florida: SB 7026 / Cybersecurity Act `[VERIFY]`.
  - New York: ITS-15 alignment and NYSOC incident timelines `[VERIFY]`.
- **§8.4 HIPAA BAA flow-down `[OPTIONAL — only if §7.5 is selected]`:** The BAA at Schedule 3 prevails over any conflicting term as to PHI under 45 CFR §160.103.
- **§8.5 Insurance overrides `[OPTIONAL]`:** `{{Insurance Override Description}}` — e.g., per-occurrence limits, additional-insured endorsements, waiver of subrogation.
- **§8.6 Audit overrides `[OPTIONAL]`:** `{{Audit Override Description}}` — e.g., on-site assessment cadence beyond SOC 2 Type II report delivery.

---

## 9. Notices for this Order

This section says where to send legal notices about this Order Form specifically.

Notices (renewal, non-renewal, suspension, breach, termination) are validly given by (a) overnight courier with tracking and signature, (b) US certified mail, return receipt requested, or (c) email with delivery confirmation. A notice is effective on the earlier of actual receipt, two business days after courier dispatch, or three business days after USPS deposit. Email notices are effective on confirmed delivery if a courier or postal copy is dispatched within 48 hours.

**To Vendor:**
- Postal: `{{Vendor Notice Postal Address}}`
- Attn: `{{Vendor Notice Attn}}`
- Email: `{{Vendor Notice Email}}`

**To Customer:**
- Postal: `{{Customer Notice Postal Address}}`
- Attn: `{{Customer Notice Attn}}`
- Email: `{{Customer Notice Email}}`

A change-of-address notice is given under this section and takes effect the next business day.

---

## 10. Signature block

This section captures binding signatures from both parties.

Signatures may be handwritten, facsimile, scanned PDF, or via a compliant e-signature platform satisfying E-SIGN (15 U.S.C. §§7001 et seq.), UETA as enacted in the governing state, and (for NY) ESRA (N.Y. State Tech. Law §§301–309). Electronic signatures have the same legal effect as handwritten signatures. Counterparts together form one instrument.

Each signatory represents that they have corporate authority to bind their party. For orders with TCV at or above USD 100,000, Customer's signatory must hold Vice President or higher office (or, for non-corporate entities, a comparable executive position).

| Vendor | Customer |
|---|---|
| `{{Vendor Legal Name}}` | `{{Customer Legal Name}}` |
| Signature: ______________________ | Signature: ______________________ |
| Name: `{{Vendor Signatory Name}}` | Name: `{{Customer Signatory Name}}` |
| Title: `{{Vendor Signatory Title}}` | Title: `{{Customer Signatory Title}}` |
| Date: `{{Vendor Signature Date}}` | Date: `{{Customer Signature Date}}` |

---

## Schedule 1 — Line items, quantities, and pricing

| # | Service / SKU | Quantity | Unit | Unit price `{{Currency}}` | Term | Line total `{{Currency}}` |
|---|---|---|---|---|---|---|
| 1 | `{{SKU 1}}` | `{{Qty 1}}` | `{{Unit 1}}` | `{{Unit Price 1}}` | `{{Term 1}}` | `{{Line Total 1}}` |
| 2 | `{{SKU 2}}` | `{{Qty 2}}` | `{{Unit 2}}` | `{{Unit Price 2}}` | `{{Term 2}}` | `{{Line Total 2}}` |
| 3 | `{{SKU 3}}` | `{{Qty 3}}` | `{{Unit 3}}` | `{{Unit Price 3}}` | `{{Term 3}}` | `{{Line Total 3}}` |
| | | | | **Subtotal:** | | `{{Subtotal}}` |
| | | | | **Discount:** | | `{{Discount Amount}}` |
| | | | | **Total Contract Value (excl. tax):** | | `{{TCV}}` |

## Schedule 2 — Permitted affiliates

Customer Affiliates entitled to use the Services. Each Affiliate's use is on the same terms and counts against Customer's Quantity.

| Affiliate legal name | State of formation | Relationship to Customer | Effective date |
|---|---|---|---|
| `{{Affiliate 1}}` | `{{Affiliate 1 State}}` | `{{Affiliate 1 Relationship}}` | `{{Affiliate 1 Effective Date}}` |
| `{{Affiliate 2}}` | `{{Affiliate 2 State}}` | `{{Affiliate 2 Relationship}}` | `{{Affiliate 2 Effective Date}}` |

## Schedule 3 — Compliance addenda checklist

Check each addendum that applies. Each checked item is incorporated by reference; unchecked items do not apply.

- [ ] **HIPAA BAA** — incorporates `legalcode-baa`; PHI for a Covered Entity or upstream Business Associate.
- [ ] **FedRAMP** — Moderate / High / IL5; ATO `{{ATO Date}}`; sponsor `{{FedRAMP Sponsor}}`.
- [ ] **PCI-DSS** — PCI-DSS environment; AOC `{{AOC Date}}` under NDA.
- [ ] **CJIS** — Policy version `{{CJIS Version}}`; §5.12 personnel screening.
- [ ] **GLBA Safeguards Rule** — financial-services Customers under 16 CFR Part 314.
- [ ] **FERPA** — K-12 / higher-ed under 20 U.S.C. §1232g; school-official designation accepted.
- [ ] **ITAR / EAR** — US export controls (22 CFR 120-130 / 15 CFR 730-774); cleared-facility / US-person handling confirmed.
- [ ] **State data security** — NYDFS Reg 500, MA 201 CMR 17.00, TX SB 820, TX TDPSA, OR OCPA, WA My Health My Data Act where applicable.
- [ ] **State auto-renewal** — confirms §5 complies with CA ARLDA, NY GBL §527-a, OR HB 2479, IL ARLDA, CO HB 21-1063 `[VERIFY]`, TX `[VERIFY]`.
- [ ] **CCPA Notice at Collection** — required if the Service collects PI from Customer's California consumers per Cal. Civ. Code §1798.100(a).
- [ ] **Custom security questionnaire** — Customer questionnaire dated `{{Security Questionnaire Date}}` incorporated under CSA Exhibit D.

---

## Appendix A — Merge fields used

- **Customer / Vendor:** Legal Name, Entity Form, State of Formation, addresses (Billing / Notice Postal / Attn), Commercial / AP / Billing / Notice / Security emails, PO Intake Email, PO Number, Signatory Name / Title, Signature Date.
- **Order:** CSA Effective Date, Service Offering Name, Edition / Tier, Quantity Unit, Quantity, Subscription Start Date, Initial Term Length / End Date, Onboarding SOW Reference, Usage Cap, Overage Rate / Unit / Cadence.
- **Fees / renewal:** Annual Subscription Fee Amount, Currency, Billing Period, One-Time Fee Description / Amount, Invoice Cadence, Net Days, Payment Method, Renewal Term Length, Non-Renewal Notice Window, Annual Price Cap, Cancellation URL.
- **Configuration:** Upgraded SLA Tier, Sub-Region, DR Region, FedRAMP Level / Sponsor, ATO Date, DoD Impact Level, CJIS Version, StateRAMP Status, HIPAA Environment URL, Service Provider Designation, Security Tier, Commercial / Insurance / Audit Override Description, AOC Date, Security Questionnaire Date.
- **Schedules:** SKU / Qty / Unit / Unit Price / Term / Line Total 1..3; Subtotal; Discount Amount; TCV; Affiliate 1..2 with State / Relationship / Effective Date.

## Appendix B — Authoritative references

- California OAG — CCPA / CPRA: oag.ca.gov/privacy/ccpa
- Cal. Bus. & Prof. Code §17602 (ARLDA); Cal. Civ. Code §1798.100, §1798.140: leginfo.legislature.ca.gov
- N.Y. GBL §527-a; N.Y. State Tech. Law §§301–309 (ESRA): nysenate.gov
- NYDFS 23 NYCRR Part 500: dfs.ny.gov
- 815 ILCS 601 (Illinois ARLDA): ilga.gov
- ROSCA, 15 U.S.C. §§8401–8405: govinfo.gov
- FTC Click-to-Cancel Rule, 16 CFR Part 425 `[VERIFY commencement]`: ftc.gov
- 45 CFR Parts 160 / 164 (HIPAA): hhs.gov/hipaa
- 16 CFR Part 314 (GLBA Safeguards): ftc.gov
- 20 U.S.C. §1232g (FERPA): ed.gov
- FedRAMP PMO: fedramp.gov
- DFARS: acquisition.gov
- EAR: bis.doc.gov; ITAR: pmddtc.state.gov
- NIST SP 800-53, 800-171, 800-66: nist.gov
- US Copyright Office DMCA §512: copyright.gov/dmca
- Texas SB 820 `[VERIFY]`: capitol.texas.gov
- Florida SB 7026 `[VERIFY]`: flsenate.gov
- Oregon HB 2479: oregonlegislature.gov
- Colorado HB 21-1063 `[VERIFY codification]`; Colorado AI Act `[VERIFY effective date]`: leg.colorado.gov
- Massachusetts 201 CMR 17.00: mass.gov
- Common Paper CSA v2.1 — `[CC-BY-4.0]`: commonpaper.com
- Bonterms Cloud Terms — `[CC-BY-4.0]`: bonterms.com

## Appendix C — `[VERIFY]` flags

- FTC Click-to-Cancel Rule (16 CFR Part 425) commencement / staggered effective dates.
- Connecticut commercial-late-payment interest cap (12 percent APR) — confirm statute and exceptions.
- Colorado HB 21-1063 auto-renewal codification (current C.R.S. cite).
- Texas SB 820 (K-12 cybersecurity) flow-down specifics.
- Florida SB 7026 cybersecurity provisions for state-agency Customers.
- New York ITS-15 information-security alignment (current ITS policy version).
- Texas TBCA-related auto-renewal specifics.
- Colorado AI Act effective date and applicability scope.
- FAR 52.227-14 / DFARS 252.227-7013 / 7014 current alternates.

---

## Not legal advice

This template is a drafting starting point for general information only. It is not legal advice, does not create an attorney-client relationship, and does not substitute for review by qualified US counsel in the relevant state. US contract, tax, privacy, sectoral-compliance, and consumer-protection rules vary by state, industry, and counterparty type, and change frequently. Both parties should have any Order Form generated from this template reviewed by their own qualified advisors. Use is at the user's own risk; authors and licensors disclaim all warranties and liability to the maximum extent permitted by law.
