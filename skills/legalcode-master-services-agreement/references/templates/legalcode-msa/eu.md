---
title: Master Services Agreement (EU/EEA)
jurisdiction: eu
statutes:
  - Reg. (EU) 2016/679 (GDPR)
  - Dir. 2011/7/EU (Late Payment)
  - Dir. 2016/943 (Trade Secrets)
  - Reg. (EU) 910/2014 (eIDAS)
  - Reg. (EU) 2023/2854 (Data Act)
  - Reg. (EU) 2024/1689 (AI Act)
  - DE BGB §§ 305–310 / 126a / 314 (AGB / Schriftform / extraordinary termination)
  - DE GeschGehG §§ 1–4
license: MIT
last_updated: 2026-04-29
---

# {{MSA Title}} — EU/EEA Variant

**Effective Date:** {{MSA Effective Date}}

**Provider:** {{Provider Legal Name}}, a {{Provider Legal Form}} organised under the laws of {{Provider Country}}, registered with {{HR Number}}, having its registered seat at {{Provider Address}} ("**{{Provider Short Name}}**").

**Client:** {{Client Legal Name}}, a {{Client Legal Form}} organised under the laws of {{Client Country}}, registered with {{Client HR Number}}, having its registered seat at {{Client Address}} ("**{{Client Short Name}}**").

Each a "**Party**" and together the "**Parties**".

---

## Merge fields specific to this variant

In addition to the common fields listed in the pack README, this EU/EEA
variant uses:

```
{{Provider Legal Form}}        # GmbH / SAS / SpA / BV / SARL / SCE / SE / etc.
{{HR Number}}                  # HRB-#### (DE) / RCS Paris #### (FR) / REA #### (IT) / KBO (BE) / KvK (NL)
{{Client Legal Form}}          # Counterparty entity form
{{Client HR Number}}           # Counterparty registry number
{{VAT ID Provider}}            # e.g. DE######### / FR##########
{{VAT ID Client}}              # client VAT number for reverse-charge (Art. 196 VAT Directive)
{{Schriftform Threshold}}      # default EUR 50,000 — amendments above this require text-form per § 126a BGB
{{NIS2 Class}}                 # "Essential" / "Important" / "Out of scope" — per Reg. (EU) 2022/2555
{{DORA Status}}                # "Financial Entity" / "Critical ICT Third-Party Provider" / "N/A" — per Reg. (EU) 2022/2554
{{CRA Status}}                 # "Product with digital elements – Important / Critical / Default" / "N/A" — per Reg. (EU) 2024/2847
{{AI Act Tier}}                # "Prohibited" / "High-risk" / "Limited risk" / "Minimal risk" / "GPAI" / "N/A"
{{Data Importer Country}}      # third country where Provider or sub-processor is established (for SCC Module selection)
{{SCC Module}}                 # "C2P" / "P2P" / "P2C" / "C2C" — Decision (EU) 2021/914
{{Posted Workers Member State}}# host MS where personnel are physically deployed (Dir. 96/71/EC scope)
{{Whistleblower Channel URL}}  # internal-reporting channel under Dir. (EU) 2019/1937 / DE HinSchG / FR Loi Sapin II
{{Language Default}}           # English / German / French / Italian — controlling language (English is default)
{{Translation Election}}       # bilingual translation language, if any
{{ECB Reference Date}}          # date for fixing the ECB main refinancing rate for late-payment interest
{{Arbitration Seat}}           # Dublin / Stockholm / Vienna / Paris / Frankfurt
{{Arbitral Institution}}       # ICC / SCC / VIAC / DIS / NAI
{{eIDAS Signature Level}}      # "Qualified" / "Advanced" / "Simple" — Reg. (EU) 910/2014
```

---

## 1. Plain-language summary

This Section is a non-binding overview; the operative terms are in the Sections that follow. {{Provider Short Name}} agrees to perform professional services for {{Client Short Name}} under one or more Statements of Work ("SOWs") that the Parties sign under this framework. This Master Services Agreement ("**MSA**") records the legal and commercial baseline that applies across every SOW: who owns what, how invoices are paid, how disputes get resolved, and how either Party may exit. It is governed by EU and EEA law, with the host-country choices stated in §18, and it incorporates the GDPR processor terms, Late Payment Directive remedies, and trade-secret protections that apply automatically in the EU/EEA. Where this MSA is signed by a German party or its substantive performance occurs in Germany, the German overlay provisions (notably the AGB transparency review under §§ 305–310 BGB, the text-form (`Textform`) regime under § 126a BGB for material amendments, and the trade-secret reasonable-protection-measures notice under §§ 1–4 GeschGehG) apply in addition to the general terms. If a clause in this summary appears to conflict with an operative clause, the operative clause controls. Read the rest before signing.

## 2. Definitions

Defined terms have the meanings given in this Section, in the SOW, or where the context indicates a more specific meaning. Capitalisation is consistent throughout this MSA.

**"Acceptance Criteria"** means the criteria stated in the relevant SOW (or, absent stated criteria, conformity in all material respects with the SOW description) against which Deliverables are tested.

**"Affiliate"** means any entity that controls, is controlled by, or is under common control with a Party, where "control" means the direct or indirect ownership of more than fifty per cent of the voting rights or equivalent equity interest, as defined under the law of the relevant Member State.

**"Background IP"** means Intellectual Property Rights owned or licensed by a Party prior to the Effective Date or developed independently of any SOW.

**"Confidential Information"** has the meaning given in §10 and includes "trade secrets" as defined in Article 2(1) of Directive (EU) 2016/943 and §§ 1–2 GeschGehG.

**"Controller"** and **"Processor"** have the meanings given in Articles 4(7) and 4(8) GDPR.

**"Deliverable"** means a tangible or intangible work product identified as such in a SOW, including software, source code, documentation, configurations, designs, training materials, reports, and data sets.

**"DPA"** means the data-processing addendum entered into by the Parties (or the data-protection annex incorporated into a SOW) reflecting Article 28 GDPR and, where transfers occur, the Standard Contractual Clauses adopted by Decision (EU) 2021/914.

**"Foreground IP"** means Intellectual Property Rights created, conceived, reduced to practice, or first fixed in a tangible medium under or in performance of a SOW.

**"Force Majeure"** means an event beyond a Party's reasonable control that could not have been avoided by reasonable measures, including acts of war, civil unrest, public-authority action, pandemic measures, and infrastructure outages of a non-localised character.

**"Intellectual Property Rights"** or **"IPR"** means patents, utility models, copyrights and related rights (including moral rights, to the extent assignable), database rights under Directive 96/9/EC, design rights (registered and unregistered), trade-mark rights, trade-secret rights under Directive (EU) 2016/943, and any equivalent or analogous rights in any jurisdiction, in each case whether registered, unregistered, or capable of registration.

**"Open Source Component"** means software made available under a licence approved by the Open Source Initiative or by the Free Software Foundation, or otherwise described in a SOW as open source.

**"Personal Data"** has the meaning given in Article 4(1) GDPR.

**"Services"** means the professional and managed services described in a SOW.

**"SOW"** means a Statement of Work signed under this MSA, in the form of Annex A or such other form as the Parties countersign.

**"Sub-processor"** means a Processor engaged by {{Provider Short Name}} to process Personal Data on behalf of {{Client Short Name}}.

**"Working Day"** means a day other than a Saturday, Sunday, or public holiday at the registered seat of the Party from whom performance is required.

## 3. Engagement structure (MSA + SOW / Order Form framework)

This Section explains how the MSA, SOWs, Order Forms, the DPA, and any other annexes fit together. This MSA is a framework agreement and is not, on its own, a commitment by either Party to engage or supply services. Each engagement is created by a separately countersigned SOW or Order Form that incorporates this MSA by reference. {{Client Short Name}} is not obliged to issue any SOW, and {{Provider Short Name}} is not obliged to accept any SOW it has not countersigned. The Parties may execute SOWs in the form set out in Annex A, or in any other written form (including a {{SOW Approval Method}}) that records the elements listed in §4.2.

3.1 **Order of precedence.** Where there is a conflict between documents, the order of precedence is: (a) the DPA (with respect to Personal Data); (b) the operative SOW (with respect only to the engagement under that SOW); (c) this MSA; (d) Annexes A–C; (e) any policy or addendum incorporated by reference. A SOW may not vary §9 (Intellectual Property), §10 (Confidentiality), §11 (Data Protection), §13 (Indemnification), §14 (Limitation of Liability), or §18 (Governing Law) unless the variation expressly references the relevant Section of this MSA and is signed by an authorised signatory of each Party.

3.2 **Affiliate participation.** A {{Client Short Name}} Affiliate may sign a SOW in its own name; that Affiliate is then the contracting client under that SOW and inherits the rights and obligations of {{Client Short Name}} under this MSA solely for that engagement. {{Provider Short Name}} may use Affiliates as performance entities only where identified in Annex B and where the contracting Provider entity remains primarily liable.

3.3 **No exclusivity.** Nothing in this MSA grants exclusivity, minimum spend, or volume commitments. Each Party is free to engage with competitors of the other.

3.4 **Effective Date and continuation.** This MSA takes effect on the Effective Date and continues in force for the Initial Term and any renewals stated in §16, irrespective of whether SOWs are active.

## 4. Scope of services & SOW process

This Section sets out how Services are scoped, agreed, and changed. {{Provider Short Name}} will perform the Services described in each SOW with the standard of care of a competent provider of comparable services in the EU/EEA market, applying the relevant professional standards, generally accepted methodologies, and any additional standards stated in Annex C.

4.1 **Statement of Work elements.** Every SOW must, at minimum, set out: (a) the description of the Services; (b) any Deliverables and their Acceptance Criteria; (c) the timeline or milestones; (d) the fees, fee model (fixed-fee, time-and-materials, capped T&M, retainer, or hybrid), and invoicing cadence; (e) the named key personnel (if any); (f) assumptions and dependencies; and (g) any deviation from this MSA. Any element absent from a SOW is governed by this MSA.

4.2 **Acceptance of SOWs.** A SOW takes effect only when both Parties have countersigned it through {{SOW Approval Method}}. Performance prior to countersignature is undertaken at {{Provider Short Name}}'s risk and does not give rise to a payment obligation unless ratified by a subsequent countersignature.

4.3 **No deemed scope.** Work that exceeds the scope of an executed SOW is not performed under this MSA unless the Parties have first executed a Change Order under §6 or a new SOW. {{Provider Short Name}} is entitled to suspend any work that the Parties have not yet documented in this manner without that suspension constituting breach.

4.4 **Provider standards.** {{Provider Short Name}} will (a) comply with applicable EU/EEA and Member-State law in performing the Services; (b) maintain the certifications and accreditations stated in Annex C, where any are listed; (c) follow {{Client Short Name}}'s reasonable on-site and information-security policies provided to it in advance and given a fair time to implement; and (d) act in good faith ("Treu und Glauben" within the meaning of § 242 BGB where the German overlay applies).

## 5. Fees, expenses & invoicing  *(DUAL-PERSPECTIVE)*

This Section sets out how {{Client Short Name}} pays {{Provider Short Name}} and what happens if it pays late. Fees are stated in {{Currency}}, exclusive of VAT and any other indirect taxes. Where the supply is a cross-border B2B service within the meaning of Article 196 of Council Directive 2006/112/EC (the VAT Directive), the reverse-charge mechanism applies and {{Client Short Name}} is the person liable for the VAT in its Member State; {{Provider Short Name}}'s invoice will reflect this and reference the applicable VAT identification numbers. Where the place-of-supply rules require Provider-charged VAT, {{Provider Short Name}} will charge it at the prevailing rate.

### 5.1 [Client-favourable] Fees, expenses & invoicing

5.1.1 **Fees.** {{Provider Short Name}} will invoice the fees stated in each SOW. No invoice may be issued in advance of the milestone, period, or Deliverable to which it relates, and no fee accrues for time spent on rework arising from {{Provider Short Name}}'s failure to meet the SOW description.

5.1.2 **Expenses.** Reimbursable expenses are limited to those pre-approved in writing by {{Client Short Name}} in accordance with {{Client Short Name}}'s travel-and-expense policy. Daily-rate or per-diem charges are reimbursed only at the published rate; markups, "handling fees", and currency-conversion premia are not reimbursable.

5.1.3 **Invoicing format.** Invoices must comply with Directive 2014/55/EU on electronic invoicing (and the European e-invoicing standard EN 16931) and any applicable Member-State e-invoicing regime (for example, Italy's Sistema di Interscambio (SdI) or France's Chorus / forthcoming PDP regime [VERIFY commencement and current status of FR e-invoicing reform]). Each invoice must reference the SOW number, the {{Client Short Name}} purchase-order number (if any), the period covered, and the VAT details required by Article 226 VAT Directive.

5.1.4 **Payment terms.** Net {{Payment Terms}} from receipt of a conforming invoice. {{Client Short Name}} may withhold any portion of an invoice that is the subject of a good-faith dispute notified within ten Working Days of receipt; the undisputed balance is paid on time.

5.1.5 **Audit.** {{Client Short Name}} or its appointed auditor (subject to confidentiality) may, on reasonable notice and not more than once per twelve-month period, audit {{Provider Short Name}}'s books and records relating to T&M charges and reimbursable expenses for the preceding twenty-four months. Overcharges of more than three per cent in aggregate are repaid with interest at the rate stated in §5.4.1, and the audit cost is borne by {{Provider Short Name}}.

### 5.2 [Provider-favourable] Fees, expenses & invoicing

5.2.1 **Fees.** {{Provider Short Name}} invoices monthly in arrears (for T&M Services) or on the milestone schedule (for fixed-fee Services). Invoices are presumed correct unless disputed in writing within ten Working Days of receipt; failure to dispute within that window is a waiver of the objection.

5.2.2 **Expenses.** Reasonable, documented out-of-pocket expenses incurred in performing the Services (including travel at economy or equivalent class for journeys over four hours, accommodation at three- to four-star equivalent, ground transport, and visa/work-authorisation fees) are passed through at cost without markup.

5.2.3 **Statutory late-payment interest.** Where {{Client Short Name}} fails to pay any undisputed amount by the due date, {{Provider Short Name}} is entitled to charge interest at the higher of (a) the rate stated in {{Late Fee Rate}} or (b) the rate determined under Directive 2011/7/EU on combating late payment in commercial transactions, namely the European Central Bank main refinancing rate in force on the first calendar day of the relevant half-year as at {{ECB Reference Date}} plus eight (8) percentage points [VERIFY current ECB MRO rate]. Interest accrues automatically from the day after the due date without the need for a reminder, in accordance with Article 3 of the Directive.

5.2.4 **Recovery costs.** In addition to interest, {{Provider Short Name}} is entitled to a fixed sum of forty euros (EUR 40, or its {{Currency}} equivalent) per overdue invoice as compensation for recovery costs under Article 6(1) of Directive 2011/7/EU, plus reasonable additional recovery costs (including reasonable lawyers' or external collection-agency fees) under Article 6(3). The Parties acknowledge that the Late Payment Directive has been transposed into the law of every EU/EEA Member State (for example, in Germany by the Gesetz zur Bekämpfung von Zahlungsverzug im Geschäftsverkehr; in France by the loi de modernisation de l'économie ("LME"); in Italy by D.Lgs. 231/2002 as amended; in Spain by Ley 3/2004 [VERIFY MS-specific transposition versions in force]) and that the rights stated here are the contractual expression of the Directive's mandatory minimum.

5.2.5 **Suspension.** {{Provider Short Name}} may, on five Working Days' written notice, suspend Services and withhold Deliverables for any undisputed amount overdue by more than fifteen Working Days, without that suspension constituting breach.

### 5.3 [Market-standard] Fees, expenses & invoicing

5.3.1 **Fees.** {{Provider Short Name}} invoices monthly in arrears for time-and-materials engagements and on the milestone schedule for fixed-fee engagements. Each invoice is itemised by SOW, by individual where T&M, and by milestone where fixed-fee.

5.3.2 **Expenses.** Reasonable, documented out-of-pocket expenses are passed through at cost. Expenses individually exceeding {{Currency}} 1,000 require {{Client Short Name}}'s prior written consent (which may be by email).

5.3.3 **E-invoicing.** {{Provider Short Name}} delivers invoices in the format required by Directive 2014/55/EU (EN 16931) and the applicable Member-State regime, where {{Client Short Name}} is a contracting authority or a private undertaking subject to mandatory e-invoicing.

5.3.4 **Payment terms.** {{Payment Terms}} from receipt of a conforming invoice. The Parties record that this period does not exceed the maximum permitted by Article 3(5) of Directive 2011/7/EU (sixty days, or such longer period as is expressly agreed in writing and not grossly unfair within the meaning of Article 7).

5.3.5 **Late-payment interest.** Interest on any undisputed overdue amount accrues at the rate set out in §5.2.3, plus the EUR 40 minimum recovery sum and any additional reasonable recovery costs under Article 6 of Directive 2011/7/EU.

5.3.6 **Disputed amounts.** {{Client Short Name}} pays the undisputed portion of any invoice on time and notifies any dispute in writing within ten Working Days of receipt, with reasonable particulars. The Parties resolve disputed amounts in good faith; unresolved disputes are escalated under §18.

5.3.7 **VAT and reverse charge.** Where Article 196 VAT Directive applies, the supply is reverse-charged and the invoice carries the legend required by Article 226(11a) VAT Directive. Where Member-State digital-reporting or e-invoicing rules require additional metadata, the Parties cooperate to supply it.

5.4.1 **Reference rate for interest.** For purposes of this §5, references to "ECB MRO" mean the European Central Bank main refinancing operations interest rate in force on the first calendar day of the relevant half-year (as published on the ECB's website). For Parties seated in non-euro EEA Member States that have transposed Directive 2011/7/EU using the national central-bank reference rate (for example, Sweden, Denmark, Norway, Iceland), the local equivalent reference rate plus eight percentage points applies [VERIFY current rates and MS-specific equivalents].

## 6. Change control & change orders  *(DUAL-PERSPECTIVE)*

This Section explains how the Parties change a SOW. Changes to scope, fees, or timeline take effect only through a written Change Order signed by both Parties. A Change Order may be a stand-alone document or an amendment to the existing SOW; it must identify the SOW it amends, describe the change, and state any fee or schedule impact.

### 6.1 [Client-favourable] Change control

6.1.1 **No automatic change.** No statement, email, or oral communication binds {{Client Short Name}} to a change unless a Change Order is countersigned by an authorised signatory.

6.1.2 **Re-scope without payment.** If {{Provider Short Name}} forms the view that work is out of scope, it must say so in writing within five Working Days of identifying the issue and pause the work in question; if it instead performs the work without first proposing a Change Order, the work is deemed in scope and not separately payable.

6.1.3 **Schriftform Threshold.** Where a Change Order would, alone or together with previously executed Change Orders to the same SOW, increase the SOW value by more than {{Schriftform Threshold}} (default EUR 50,000), the Change Order is executed in `Textform` within the meaning of § 126a BGB (qualified electronic signature or a hand-written signature on a paper original; a simple email confirmation is not sufficient).

### 6.2 [Provider-favourable] Change control

6.2.1 **Change request triggers.** A Change Order is required where (a) {{Client Short Name}} requests a change; (b) {{Client Short Name}} fails to meet a stated dependency or assumption; (c) third-party software, infrastructure, or interfaces relied on under the SOW change in a way that materially affects performance; or (d) regulatory developments require the Services to be adjusted.

6.2.2 **Reasonable estimates suffice.** Where {{Provider Short Name}} cannot fix a precise fee impact at the point of the Change Order, it provides a not-to-exceed estimate; that estimate, once countersigned, is the binding price ceiling.

6.2.3 **Resumption rights.** {{Provider Short Name}} may stand its team down for the duration of an unsigned Change Order request and re-mobilise on countersignature; documented stand-down and re-mobilisation costs are payable through the next invoice.

### 6.3 [Market-standard] Change control

6.3.1 **Change request.** Either Party may submit a written Change Request describing the proposed change, the reason for it, and the proposing Party's preliminary view of the fee, schedule, or scope impact.

6.3.2 **Response.** {{Provider Short Name}} responds within ten Working Days with a written Change Order proposal containing the description of the change, the impact on fees, the impact on the schedule, the impact on dependencies, any new assumptions, and any new acceptance criteria.

6.3.3 **Effect of signature.** A Change Order takes effect only when countersigned by both Parties using {{SOW Approval Method}}. Until countersigned, the original SOW continues unchanged and {{Provider Short Name}} performs to the existing scope.

6.3.4 **Schriftform and material amendments.** Where the German overlay applies and the cumulative impact of executed Change Orders to a SOW exceeds {{Schriftform Threshold}}, the Change Order from which the threshold is exceeded is executed in `Textform` per § 126a BGB.

## 7. Personnel, key personnel & subcontracting

This Section governs who performs the Services and what {{Client Short Name}} can expect from them. {{Provider Short Name}} is the employer or principal of the personnel it deploys and is solely responsible for their wages, social-security contributions, taxes, and benefits.

7.1 **Worker classification.** {{Provider Short Name}} performs the Services as an independent provider. Nothing in this MSA creates an employment relationship between {{Client Short Name}} and any individual of {{Provider Short Name}} or its sub-providers. {{Provider Short Name}} acknowledges the EU and Member-State legal framework on worker classification and warrants that it has assessed the relationship under that framework, including (a) German social-security risk under § 7a SGB IV (Statusfeststellungsverfahren) and the case law on `Scheinselbstständigkeit` / `Bogusbeschäftigung`; (b) French rules on `salariat déguisé` and the use of `portage salarial` where individual contractors are deployed; (c) Italian `lavoro parasubordinato` rules under Articles 2 and 409 c.p.c.; (d) Spanish `falsos autónomos` framework; and (e) the line of CJEU case law on platform-worker reclassification, including Case C-692/19 *B* (heard 22 April 2020) and the platform-work directive as transposed in the host Member State [VERIFY transposition status of Dir. (EU) 2024/2831 in the relevant MS].

7.2 **Posted Workers.** Where {{Provider Short Name}}'s personnel will physically perform Services in {{Posted Workers Member State}} other than the Member State of their normal employment, {{Provider Short Name}} complies with Directive 96/71/EC as amended by Directive (EU) 2018/957, and the Enforcement Directive 2014/67/EU, including the host-State minimum wage and core working conditions, the prior posting declaration required by the host MS, and the maintenance of an A1 portable document for each posted individual evidencing the home-MS social-security regime.

7.3 **Background checks.** {{Provider Short Name}} carries out the background checks (criminal record, employment history, professional credentials) lawful in the Member State of employment and reasonable for the role. {{Provider Short Name}} does not collect or share data beyond what is necessary, lawful, and proportionate within the meaning of Article 5(1)(c) GDPR.

7.4 **Key Personnel.** Personnel identified as "Key Personnel" in a SOW or in Annex B are committed to the engagement at the percentage of time stated. {{Provider Short Name}} will not reassign Key Personnel without {{Client Short Name}}'s prior written consent (not to be unreasonably withheld), except where the individual leaves {{Provider Short Name}}, becomes incapacitated, or for genuine disciplinary or performance reasons.

7.5 **Replacement obligation.** Where Key Personnel become unavailable, {{Provider Short Name}} proposes a replacement of equivalent skill within ten Working Days, and {{Client Short Name}} may interview and reasonably reject the candidate (with the replacement obligation continuing).

7.6 **Removal on request.** {{Client Short Name}} may, acting reasonably and stating its grounds, request the removal of any individual personnel from the engagement; {{Provider Short Name}} replaces that individual within ten Working Days without affecting the SOW timetable, save where the removal request is itself the cause of slippage.

7.7 **Subcontracting.** {{Provider Short Name}} may use sub-providers only where (a) listed in Annex B; (b) the sub-provider is bound to terms no less protective than this MSA, including this §7 and §10; (c) {{Provider Short Name}} remains primarily liable for the sub-provider's performance and acts and omissions; and (d) where Personal Data is involved, the sub-provider is engaged as a Sub-processor in accordance with §11 and the DPA. Engagement of a Sub-processor that processes Personal Data is also subject to the prior-authorisation regime in §11.5.

7.8 **Non-solicitation.** During the Term and for twelve months after, neither Party will, without the other's prior written consent, knowingly solicit for employment or engagement any individual employed or engaged by the other and materially involved in the Services. General advertising and recruitment of individuals who approach a Party of their own initiative is permitted, as is hiring such individuals.

7.9 **Whistleblower duty of cooperation.** Where personnel of {{Provider Short Name}} report a concern through {{Whistleblower Channel URL}} or any equivalent channel established under Directive (EU) 2019/1937 (and its national transpositions, including the German Hinweisgeberschutzgesetz (HinSchG), the French Loi Sapin II, the Italian Whistleblowing Decree (D.Lgs. 24/2023), and similar instruments in other Member States [VERIFY MS-specific status]), {{Provider Short Name}} ensures that no retaliation occurs and that the channel is operated in accordance with applicable law.

## 8. Acceptance & deliverables

This Section sets out how Deliverables are reviewed and accepted. Where a SOW identifies Deliverables, {{Provider Short Name}} delivers them in the form, format, and on the date stated in the SOW, accompanied by reasonable documentation enabling {{Client Short Name}} to test against the Acceptance Criteria.

8.1 **Acceptance review.** {{Client Short Name}} has {{Acceptance Period}} from delivery to test each Deliverable against the Acceptance Criteria and to either accept it or notify {{Provider Short Name}} in writing of the specific failures observed.

8.2 **Cure.** {{Provider Short Name}} has fifteen Working Days (or such other period as the SOW specifies) to remedy notified failures and re-submit the Deliverable. The cure-and-resubmission cycle may be repeated once unless the SOW specifies otherwise; persistent failure to meet the Acceptance Criteria is a material breach for purposes of §16.

8.3 **Deemed acceptance.** Where {{Client Short Name}} does not deliver an acceptance notice or rejection notice within {{Deemed Acceptance Window}} after delivery, the Deliverable is deemed accepted. Use in production of a Deliverable is also acceptance, save for use under express reservation while the Acceptance Criteria are still being tested.

8.4 **Partial acceptance.** Where a Deliverable substantially conforms but contains discrete defects, the Parties may agree to accept it with a defect list and a cure plan. Acceptance with a cure plan does not reduce {{Provider Short Name}}'s warranty obligations under §12.

8.5 **§ 640 BGB analogue (DE).** Where the German overlay applies, the Acceptance Criteria-based regime in this §8 is the contractual expression of `Abnahme` for purposes of § 640 BGB; the Parties exclude tacit acceptance ("`fiktive Abnahme`") under § 640(2) BGB except as stated in §8.3.

## 9. Intellectual property (foreground / background / open-source)  *(DUAL-PERSPECTIVE)*

This Section sets out who owns and may use the IPR created and used in the Services. The default position is set in §9.1 ({{IP Ownership Default}}); the dual-perspective sub-sections vary that default. EU/EEA-specific IPR formalities (moral rights, database rights, German § 31 UrhG buy-out, French Article L.121-1 CPI inalienable moral rights, and trade-secret protections under Directive (EU) 2016/943) apply as set out below.

### 9.1 [Client-favourable] IP ownership

9.1.1 **Foreground IP assignment.** {{Provider Short Name}} hereby assigns to {{Client Short Name}}, with effect from creation and to the fullest extent assignable under applicable law, all right, title, and interest in and to all Foreground IP. To the extent any Foreground IP cannot be assigned under applicable law (including non-assignable moral rights under French Article L.121-1 CPI, German § 13 UrhG, Italian Art. 22 Legge sul diritto d'autore, and equivalent provisions in other Member States), {{Provider Short Name}} grants {{Client Short Name}} a worldwide, perpetual, irrevocable, royalty-free, fully paid-up, exclusive (subject to §9.1.4), transferable, sub-licensable licence to use that Foreground IP for any purpose.

9.1.2 **Moral-rights non-assertion.** To the extent moral rights or `droit moral` are inalienable as a matter of mandatory law (notably French Article L.121-1 CPI, German §§ 12–14 UrhG, Italian Art. 20 LDA, and Spanish Article 14 LPI), {{Provider Short Name}} undertakes — and procures from each individual author employed or engaged by it — an irrevocable covenant not to assert those rights against {{Client Short Name}}, its successors, assigns, sub-licensees, and permitted transferees, save where assertion is required by mandatory law or to prevent a serious distortion or attribution-related harm to the author's reputation.

9.1.3 **§ 31 UrhG buy-out (DE).** Where the German overlay applies, the assignment in §9.1.1 is intended to be the broadest grant permissible under §§ 31, 31a, and 32a UrhG, including all currently known types of use and (subject to §9.1.5) types of use not yet known at the Effective Date ("`unbekannte Nutzungsarten`"). The Parties have addressed the equitable-remuneration implications under § 32 / § 32a UrhG in the fee structure of each SOW; the contractual remuneration is intended to be a "Buy-Out-Vergütung" and to satisfy § 32 UrhG, save for the residual non-waivable claims under § 32a UrhG ("Fairness-Paragraph").

9.1.4 **Background IP licence.** {{Provider Short Name}} retains its Background IP and grants {{Client Short Name}} a worldwide, perpetual, irrevocable, royalty-free, sub-licensable licence to use, reproduce, modify, and create derivative works of any Background IP that is incorporated into a Deliverable, solely to the extent necessary for {{Client Short Name}} to use that Deliverable for any internal or external business purpose.

9.1.5 **Future use types (DE-specific safeguard).** Where the German overlay applies, {{Provider Short Name}} may revoke the grant relating to an unknown type of use under § 31a(1) UrhG only where the SOW remuneration does not provide separate equitable compensation for that type of use; the Parties record their intention that the SOW remuneration includes such compensation.

9.1.6 **Database rights.** Where the Services produce a "database" within the meaning of Article 1 of Directive 96/9/EC, {{Provider Short Name}} assigns to {{Client Short Name}} the sui-generis database right and any related rights of authors of the database, on the same terms as §9.1.1.

### 9.2 [Provider-favourable] IP ownership

9.2.1 **Provider retains; Client gets a licence.** {{Provider Short Name}} retains all right, title, and interest in and to its Foreground IP and Background IP. {{Provider Short Name}} grants {{Client Short Name}} a worldwide, non-exclusive, royalty-free (within the SOW fees), non-transferable, non-sublicensable (save to its Affiliates and contractors acting on its behalf) licence to use the Deliverables for {{Client Short Name}}'s internal business purposes for the period stated in the SOW (or, absent a stated period, in perpetuity).

9.2.2 **Improvements and tooling.** Improvements, methodologies, frameworks, libraries, and reusable components created by {{Provider Short Name}} in the course of any engagement are {{Provider Short Name}}'s Background IP and may be re-used in other engagements.

9.2.3 **Moral rights.** {{Provider Short Name}} retains attribution rights to the extent inalienable under applicable law, but waives or covenants not to assert those rights as against {{Client Short Name}} except where attribution is required by mandatory law or by good professional practice for the type of Deliverable concerned.

### 9.3 [Market-standard] IP ownership

9.3.1 **Default rule.** The default rule for this MSA is {{IP Ownership Default}}. Each SOW may state a different rule for its specific Deliverables.

9.3.2 **Foreground IP.** Subject to the SOW-level variation, all Foreground IP first reduced to a tangible medium specifically for {{Client Short Name}} under a SOW vests in {{Client Short Name}} on creation and, to the extent the foregoing is not effective under applicable law, is hereby assigned by {{Provider Short Name}} to {{Client Short Name}}. Foreground IP that is not specific to a Deliverable for {{Client Short Name}} (including general improvements, frameworks, and tooling) is retained by {{Provider Short Name}}.

9.3.3 **Background IP and embedded components.** {{Provider Short Name}} retains Background IP. Where Background IP is incorporated into a Deliverable, {{Provider Short Name}} grants {{Client Short Name}} a worldwide, perpetual, irrevocable, royalty-free (within SOW fees), sub-licensable licence to use, copy, modify, distribute, and create derivative works of that Background IP solely as part of, and to the extent necessary to use, the Deliverable.

9.3.4 **Open Source policy.** {{Provider Short Name}} only incorporates Open Source Components into Deliverables where {{Open Source Policy}} permits and where, before incorporation, {{Provider Short Name}} has confirmed that the licence terms of those components are compatible with {{Client Short Name}}'s intended use. {{Provider Short Name}} maintains a software bill of materials ("SBOM") in a CRA-compatible format (cyclonedx or SPDX) sufficient to satisfy Article 13 and Annex II of Regulation (EU) 2024/2847 (CRA) for any Deliverable that is a "product with digital elements" [VERIFY commencement and applicability].

9.3.5 **OSS disclosure.** {{Provider Short Name}} discloses in writing all Open Source Components incorporated into a Deliverable, together with the applicable licence and any reciprocal-licence ("copyleft") obligations triggered by intended use; {{Client Short Name}} may, before acceptance, require substitution of any component the licence of which is incompatible with its intended use.

9.3.6 **Moral rights.** Each Party records that moral rights and `droit moral` may be inalienable in some Member States and gives a non-assertion covenant on the same terms as §9.1.2 with respect to the Deliverables in fact assigned or licensed under the applicable SOW.

9.3.7 **Trade secrets.** Confidential Information includes "trade secrets" within the meaning of Article 2(1) of Directive (EU) 2016/943 (the "Trade Secrets Directive") and the implementing law in each Member State (notably the German GeschGehG of 26 April 2019). The protective measures set out in §10 are intended to be the "reasonable steps to keep [the trade secret] secret" required by Article 2(1)(c) of the Directive and § 2(1) GeschGehG.

## 10. Confidentiality

This Section governs how the Parties handle each other's non-public information. Each Party ("Receiving Party") will hold the other's Confidential Information in strict confidence and use it only to perform under, or take the benefit of, this MSA.

10.1 **Definition.** "Confidential Information" means any information disclosed by or on behalf of one Party (the "Disclosing Party") that is marked or identified as confidential, or that a reasonable person in the circumstances would understand to be confidential, including (without limitation) business plans, financial data, customer and supplier lists, technical know-how, source code, security designs, pricing, and Personal Data.

10.2 **Standard of care.** The Receiving Party uses no less than the standard of care it uses for its own confidential information of a comparable nature, and in any event a reasonable standard of care, and limits access to those of its personnel, Affiliates, professional advisers, auditors, and sub-providers who need to know it for the purposes of this MSA and who are bound by obligations of confidentiality at least as protective as those in this §10.

10.3 **Carve-outs.** Confidential Information does not include information that the Receiving Party can demonstrate (a) was already lawfully in its possession without confidentiality obligation; (b) becomes publicly available without breach by it; (c) is lawfully obtained from a third party without confidentiality obligation; or (d) is independently developed without reference to the Disclosing Party's Confidential Information.

10.4 **Compelled disclosure.** Where the Receiving Party is compelled by law, regulation, or a competent authority's order to disclose Confidential Information, it gives prompt notice to the Disclosing Party (where lawful) so that the Disclosing Party can seek protective relief, and it discloses only what is legally required and uses reasonable efforts to obtain confidential treatment.

10.5 **Term of obligation.** The obligations in this §10 last for the Term of the MSA and (a) for five (5) years following expiry or termination, for general Confidential Information; (b) for as long as the information qualifies as a trade secret under Directive (EU) 2016/943 / § 2 GeschGehG, for trade-secret information; and (c) for as long as required by applicable law, for Personal Data.

10.6 **GeschGehG reasonable-protection-measures notice (DE).** Where the German overlay applies, the Parties record that the measures in this §10, in the technical and organisational measures attached to the DPA, and in any specific information-security schedule attached to a SOW are intended to be the "angemessene Geheimhaltungsmaßnahmen" required by §§ 1–2 GeschGehG. The Disclosing Party may give the Receiving Party written notice that specific information is to be treated as a trade secret with heightened protective measures (including need-to-know access lists and disclosure-logging); failure to give such a notice does not, on its own, defeat trade-secret status under § 2(1) GeschGehG.

10.7 **Whistleblower carve-out.** Nothing in this §10 prevents a person from reporting suspected illegal conduct to a competent authority, nor from disclosing information protected under Directive (EU) 2019/1937 (and its Member-State transpositions, including the DE HinSchG, FR Loi Sapin II, and IT D.Lgs. 24/2023) [VERIFY MS-specific status]. Disclosure made in accordance with that Directive does not breach this §10 or the applicable trade-secret rules under Article 5 of Directive (EU) 2016/943 / § 5 GeschGehG.

10.8 **Return or destruction.** On expiry or termination, or earlier on the Disclosing Party's written request, the Receiving Party returns or, at the Disclosing Party's election, destroys all Confidential Information in its possession (subject to lawful retention requirements and back-up retention pending overwriting) and certifies destruction in writing on request.

## 11. Data protection & information security

This Section sets out the GDPR allocation between the Parties and incorporates the operative DPA. Each Party complies with Regulation (EU) 2016/679 (GDPR), the EU ePrivacy framework (currently Directive 2002/58/EC as amended), and the data-protection law of each relevant Member State.

11.1 **Roles.** Where {{Provider Short Name}} processes Personal Data on behalf of {{Client Short Name}} under a SOW, {{Client Short Name}} is the Controller (or a Processor passing instructions under its own controller mandate) and {{Provider Short Name}} is the Processor (or, as relevant, the Sub-processor). Where the Parties act as joint Controllers, an Article 26 GDPR arrangement is documented in the relevant SOW. Where {{Provider Short Name}} acts as an independent Controller (for example, for its own personnel administration or for billing records), each Party acts on its own legal basis and is responsible for its own Article 13/14 information notices.

11.2 **Article 28 GDPR.** {{Provider Short Name}} processes Personal Data only on documented instructions from {{Client Short Name}} (including with regard to transfers), maintains the confidentiality of Personal Data, implements appropriate technical and organisational measures ("TOMs") satisfying Article 32 GDPR (with reference to ENISA guidance and ISO/IEC 27001-aligned controls where Annex C so requires), assists {{Client Short Name}} with data-subject rights, breach notification, DPIAs, and prior-consultation under Articles 12–22, 32–34, and 35–36, deletes or returns Personal Data on termination, and provides the information necessary to demonstrate compliance and submits to audits as set out in the DPA.

11.3 **DPA precedence.** Where there is any conflict between this §11 and the DPA in respect of Personal Data, the DPA prevails. The DPA set out in `legalcode-dpa` (or the equivalent annex executed by the Parties) is incorporated by reference and forms part of this MSA.

11.4 **International transfers.** Where Personal Data is transferred to a third country outside the EEA in the absence of an adequacy decision, the transfer is governed by the Standard Contractual Clauses adopted by Commission Implementing Decision (EU) 2021/914, in the {{SCC Module}} module appropriate to the role allocation, with the docking-clause and additional-safeguards measures as set out in the DPA. References in this MSA to the EU-US Data Privacy Framework apply only where {{Data Importer Country}} is the United States and the Provider (or the relevant Sub-processor) is on the active DPF list maintained by the US Department of Commerce; the Parties acknowledge that the Framework's adequacy decision (Commission Implementing Decision (EU) 2023/1795) has been the subject of legal challenge and may be amended or invalidated [VERIFY current status of Schrems-III-style litigation and DPF adequacy].

11.5 **Sub-processors.** {{Provider Short Name}} may engage Sub-processors only with {{Client Short Name}}'s prior general or specific authorisation, on terms no less protective than those in this §11 and the DPA, and on giving advance notice of any new or replacement Sub-processor with a reasonable opportunity for {{Client Short Name}} to object. The current list of authorised Sub-processors is maintained in Annex B.

11.6 **Personal-data breach notification.** {{Provider Short Name}} notifies {{Client Short Name}} of any personal-data breach (Article 4(12) GDPR) without undue delay and in any event within forty-eight (48) hours of becoming aware, providing the information required by Article 33(3) GDPR to support {{Client Short Name}}'s seventy-two (72)-hour supervisory-authority notification timeline. {{Provider Short Name}} cooperates without charge in {{Client Short Name}}'s investigation, mitigation, and notification activities under Articles 33–34 GDPR.

11.7 **Information security.** {{Provider Short Name}} implements appropriate TOMs reflecting the state of the art, the nature, scope, context and purposes of processing, and the risk to data subjects, with specific reference to Article 32(1)(a)–(d) GDPR. Annex C of this MSA, together with the security-measures schedule attached to the DPA, sets out the agreed minimum TOMs. {{Provider Short Name}} maintains certifications stated in Annex C (for example, ISO/IEC 27001 / SOC 2 Type II / Cyber Essentials Plus where listed) and provides current attestation reports on request, subject to confidentiality.

11.8 **NIS2 obligations.** Where {{Client Short Name}} is an "essential" or "important" entity under Directive (EU) 2022/2555 (NIS2), {{Provider Short Name}} cooperates with {{Client Short Name}}'s incident-handling and supply-chain-security obligations under Articles 21 and 23 NIS2, including supply-chain risk assessments, incident reporting on the timelines required of {{Client Short Name}} (including the 24-hour early warning, 72-hour notification, and one-month final report), and information-sharing with the relevant CSIRT or competent authority as required. The classification of the Parties is recorded in {{NIS2 Class}}. Where {{Provider Short Name}} is itself an essential or important entity, it complies with NIS2 in its own right and the cooperation obligation runs both ways.

11.9 **DORA obligations.** Where {{Client Short Name}} is a "financial entity" under Regulation (EU) 2022/2554 (DORA) and {{Provider Short Name}} provides "ICT services" within the meaning of Article 3(21) DORA, {{Provider Short Name}} cooperates with {{Client Short Name}}'s ICT third-party risk-management framework, including the contractual elements required by Article 30 DORA, the right of access, inspection and audit (Article 30(3)(e)), assistance with incident reporting and threat-led penetration testing, and exit-strategy support. Where {{Provider Short Name}} is designated a "Critical ICT Third-Party Provider" under Article 31 DORA, it complies with the lead-overseer regime in its own right. The classification is recorded in {{DORA Status}} [VERIFY current designation status].

11.10 **CRA obligations.** Where any Deliverable is a "product with digital elements" within the meaning of Article 3(1) of Regulation (EU) 2024/2847 (CRA), {{Provider Short Name}} delivers it in compliance with the essential requirements in Annex I CRA (including secure-by-design, vulnerability handling, and SBOM), provides the technical documentation in Annex II CRA, and supports {{Client Short Name}} in any conformity-assessment that {{Client Short Name}} must perform as a manufacturer, importer, or distributor. The classification is recorded in {{CRA Status}} [VERIFY commencement (CRA staged application) and applicability].

11.11 **AI Act obligations.** Where any Deliverable is or incorporates an "AI system" or "general-purpose AI model" within the meaning of Articles 3(1) and 3(63) of Regulation (EU) 2024/1689 (AI Act), {{Provider Short Name}} states in the SOW the AI Act risk tier ({{AI Act Tier}}) and complies with the applicable obligations: prohibited practices (Article 5) in no circumstances; high-risk AI providers' obligations (Articles 8–22) where applicable; transparency obligations (Article 50) where applicable; and GPAI obligations (Articles 53–55) where applicable. {{Provider Short Name}} provides the technical and instruction-for-use documentation that {{Client Short Name}} reasonably requires to fulfil any deployer obligations [VERIFY phased commencement: prohibitions from 2 February 2025; GPAI from 2 August 2025; high-risk AI from 2 August 2026 / 2027].

11.12 **Data Act portability.** Where Regulation (EU) 2023/2854 (Data Act) applies (in particular Article 4 user-access and Articles 23–31 cloud-switching obligations), {{Provider Short Name}} cooperates with {{Client Short Name}}'s exercise of those rights and supports portability of {{Client Short Name}} data and Deliverables to a successor provider on commercially reasonable terms, including the maximum migration period and exit-charge constraints set by the Data Act [VERIFY Article 31 transition rules and applicability to the specific service].

## 12. Representations & warranties  *(DUAL-PERSPECTIVE)*

This Section states what each Party promises about itself, the Services, and the Deliverables. Each Party represents and warrants to the other that, as at the Effective Date and on each SOW execution: (a) it is duly organised and validly existing under the law of its jurisdiction of incorporation; (b) it has the corporate authority to enter into and perform this MSA and each SOW; (c) signature does not violate its constitutional documents, any other agreement, or any applicable law; and (d) there is no proceeding, judgment, or order pending or threatened that would impair its performance.

### 12.1 [Client-favourable] Warranties

12.1.1 **Performance warranty.** {{Provider Short Name}} warrants that the Services will be performed by suitably skilled personnel, in a professional and workmanlike manner, with the standard of care and skill of a competent provider of comparable services in the EU/EEA market.

12.1.2 **Conformity warranty.** {{Provider Short Name}} warrants that each Deliverable will conform in all material respects to the SOW description and Acceptance Criteria for a period of ninety (90) days from acceptance and that {{Provider Short Name}} will, at no additional charge, re-perform Services or remedy Deliverables that fail this warranty during the warranty period.

12.1.3 **IPR non-infringement.** {{Provider Short Name}} warrants that the Services and Deliverables, when used as contemplated in the SOW, will not infringe any third-party Intellectual Property Right valid in the EU/EEA at the date of acceptance.

12.1.4 **Open Source.** {{Provider Short Name}} warrants that no Open Source Component is incorporated into a Deliverable except as disclosed under §9.3.5, and that no incorporated Open Source Component imposes a copyleft obligation that would compel {{Client Short Name}} to license or disclose its proprietary code as a result of use of the Deliverable as contemplated in the SOW.

12.1.5 **Compliance.** {{Provider Short Name}} warrants that the Services are performed in compliance with EU/EEA and Member-State law applicable to it, including data-protection law, applicable export-control law (notably Regulation (EU) 2021/821 dual-use), competition law (Articles 101–102 TFEU and Member-State equivalents), labour law, and applicable sanctions regimes.

12.1.6 **Malicious code.** {{Provider Short Name}} warrants that, to its actual knowledge after reasonable testing, no Deliverable contains viruses, malware, time bombs, or back doors that are not disclosed and consented to in the SOW.

### 12.2 [Provider-favourable] Warranties

12.2.1 **Limited performance warranty.** {{Provider Short Name}} warrants that it will perform the Services with the care and skill of a competent EU/EEA provider of comparable services. {{Provider Short Name}}'s sole obligation, and {{Client Short Name}}'s sole remedy, for breach of this warranty is, at {{Provider Short Name}}'s election, re-performance or refund of the fees paid for the non-conforming portion of the Services. This is a `Werkvertrag`-style obligation focused on the agreed `Werk` rather than a guarantee of business outcome.

12.2.2 **No implied warranties.** Save as expressly stated in this §12.2, all conditions, warranties, and representations (whether express, implied, statutory, customary, or otherwise) are excluded to the maximum extent permitted by applicable law, including any implied warranty of merchantability, satisfactory quality, fitness for a particular purpose, or non-infringement. Where mandatory consumer protections apply, this exclusion does not affect those rights.

12.2.3 **Client warranties.** {{Client Short Name}} warrants that it has the right to provide all materials, instructions, and Personal Data made available to {{Provider Short Name}}, that {{Client Short Name}}'s instructions are lawful, and that {{Client Short Name}} has obtained any consents and made any notifications required for {{Provider Short Name}}'s lawful processing.

### 12.3 [Market-standard] Warranties

12.3.1 **Performance.** {{Provider Short Name}} warrants that the Services will be performed by suitably qualified personnel in a professional and workmanlike manner, with the standard of care and skill of a competent EU/EEA provider of comparable services.

12.3.2 **Conformity.** {{Provider Short Name}} warrants that each Deliverable will conform in all material respects to the SOW description and Acceptance Criteria for ninety (90) days from acceptance; the sole remedy for breach is re-performance, repair, or refund of fees paid for the non-conforming Deliverable.

12.3.3 **IP non-infringement.** Subject to §13, {{Provider Short Name}} warrants that the Deliverables, when used as contemplated in the SOW, will not, to its knowledge, infringe any third-party IPR.

12.3.4 **Compliance.** Each Party warrants that it complies with applicable EU/EEA and Member-State law in performing this MSA, including GDPR, the AI Act (Reg. (EU) 2024/1689), the CRA (Reg. (EU) 2024/2847), the Data Act (Reg. (EU) 2023/2854), and applicable sanctions and export-control law.

12.3.5 **DE-AGB transparency reservation.** Where the German overlay applies, the Parties record that the warranty regime in this §12.3 has been individually negotiated within the meaning of § 305(1) sentence 3 BGB and is intended to be transparent and balanced for purposes of §§ 305c and 307 BGB. To the extent any limitation in §12.2 is, in a B2B context, found to be unduly disadvantageous under § 307 BGB, the limitation is to be replaced by the closest enforceable equivalent; severance under §19.7 applies.

12.3.6 **No general fitness-for-purpose.** Other than the warranties expressly stated in this §12.3, no warranty is given as to fitness for a specific business purpose, save where {{Client Short Name}}'s specific purpose is recorded in the SOW and the SOW expressly extends the conformity warranty to that purpose.

## 13. Indemnification  *(DUAL-PERSPECTIVE)*

This Section sets out who pays for third-party claims and on what conditions. The indemnification framework here operates as a contractual allocation; it does not limit either Party's right to seek independent statutory remedies (including under §§ 280, 311 BGB, French Article 1240 Code civil, or equivalent), subject to §14.

### 13.1 [Client-favourable] Indemnification

13.1.1 **Provider IP indemnity.** {{Provider Short Name}} will defend and hold {{Client Short Name}} (and its Affiliates, employees, officers, and directors) harmless from any third-party claim that the Services or Deliverables, used as contemplated in the SOW, infringe any IPR valid in the EU/EEA, and will pay damages and costs awarded by a competent court or arbitral tribunal or agreed in settlement.

13.1.2 **Procurement of right or replacement.** {{Provider Short Name}} may, at its cost and election, (a) procure for {{Client Short Name}} the right to continue using the affected Deliverable, (b) modify the affected Deliverable to be non-infringing while preserving its functionality, or (c) replace it with a non-infringing equivalent. If none of (a)–(c) is commercially reasonable, {{Provider Short Name}} refunds the fees paid for the affected Deliverable on a straight-line three-year amortisation basis.

13.1.3 **Carve-outs.** {{Provider Short Name}} has no IPR-indemnity obligation to the extent the claim arises from (a) {{Client Short Name}}'s use of a Deliverable in combination with materials not supplied or approved by {{Provider Short Name}} where the infringement would not have occurred but for that combination; (b) {{Client Short Name}}'s modification of a Deliverable other than by {{Provider Short Name}}'s direction; or (c) {{Client Short Name}}'s instructions or specifications that were the proximate cause of the infringement.

13.1.4 **Data-protection and confidentiality indemnity.** {{Provider Short Name}} will indemnify {{Client Short Name}} for losses, fines, claims, and reasonable defence costs arising from {{Provider Short Name}}'s breach of §10 (Confidentiality), §11 (Data Protection), or the DPA, including supervisory-authority fines under Article 83 GDPR to the extent attributable to that breach. This indemnity is subject to §14, save as set out in §14.3 (uncapped categories).

### 13.2 [Provider-favourable] Indemnification

13.2.1 **Client indemnity for inputs.** {{Client Short Name}} will defend and hold {{Provider Short Name}} harmless from any third-party claim that arises from (a) materials, specifications, instructions, or Personal Data provided by {{Client Short Name}} to {{Provider Short Name}}; (b) {{Client Short Name}}'s use of a Deliverable in violation of applicable law or the SOW; or (c) {{Client Short Name}}'s combination of a Deliverable with third-party items not supplied by {{Provider Short Name}}.

13.2.2 **Limited Provider IP indemnity.** {{Provider Short Name}}'s indemnity obligation is limited to (a) procuring rights to continue use, (b) modification, (c) replacement, or (d) refund of fees as set out in §13.1.2; {{Client Short Name}}'s sole remedies are those set out in §13.1.2.

13.2.3 **Carve-outs.** No indemnity is owed by {{Provider Short Name}} where the claim derives from {{Client Short Name}}'s instructions, specifications, modifications, or combinations as set out in §13.1.3.

### 13.3 [Market-standard] Indemnification

13.3.1 **Provider IP indemnity.** {{Provider Short Name}} indemnifies {{Client Short Name}} for third-party claims that the Services or Deliverables (used as contemplated in the SOW) infringe IPR valid in the EU/EEA, on the terms in §13.1.1–13.1.3.

13.3.2 **Provider data indemnity.** {{Provider Short Name}} indemnifies {{Client Short Name}} for losses arising from {{Provider Short Name}}'s breach of §11 / the DPA on the terms in §13.1.4, subject to §14.

13.3.3 **Client indemnity for inputs.** {{Client Short Name}} indemnifies {{Provider Short Name}} for losses arising from {{Client Short Name}}'s breach of §12.2.3 (right to provide inputs and lawful instructions) and from any third-party claim premised on {{Client Short Name}}'s materials, instructions, or modifications, on the terms in §13.2.1, subject to §14.

13.3.4 **Procedure.** The indemnified Party must (a) give prompt written notice of the claim (and any delay only reduces the indemnity to the extent the indemnifying Party is prejudiced); (b) give the indemnifying Party sole control of defence and settlement, save that no settlement may impose non-monetary obligations on the indemnified Party without consent; and (c) reasonably cooperate at the indemnifying Party's expense.

## 14. Limitation of liability  *(DUAL-PERSPECTIVE)*

This Section caps each Party's exposure under or in connection with the MSA. The cap operates subject to mandatory rules of the governing law and the rules in §14.3.

### 14.1 [Client-favourable] Liability cap

14.1.1 **Cap.** Each Party's aggregate liability arising out of or in connection with this MSA and all SOWs, regardless of cause of action, is limited to the greater of (a) {{Liability Cap Multiplier}} times the fees paid and payable by {{Client Short Name}} under this MSA in the twelve months preceding the first event giving rise to liability, or (b) {{Liability Cap Floor}}.

14.1.2 **Carve-outs.** The cap in §14.1.1 does not apply to liability arising from (a) personal injury or death; (b) intentional acts (`Vorsatz`) or gross negligence (`grobe Fahrlässigkeit`) of a Party or its officers and directors (which under § 309 No 7(b) BGB cannot be excluded or limited even in B2B); (c) breach of §10 trade-secret obligations; (d) breach of §11 / the DPA causing supervisory-authority fines under Article 83 GDPR; (e) the IPR indemnity in §13; or (f) liability that may not be limited under mandatory law (including statutory product-liability claims and consumer rights).

### 14.2 [Provider-favourable] Liability cap

14.2.1 **Cap.** {{Provider Short Name}}'s aggregate liability arising out of or in connection with this MSA and all SOWs is limited to {{Liability Cap Multiplier}} times the fees paid and payable to {{Provider Short Name}} under the SOW that gave rise to the claim in the twelve months preceding the first event giving rise to liability, or {{Liability Cap Floor}} in the aggregate, whichever is the lesser.

14.2.2 **Excluded losses.** Neither Party is liable for indirect, consequential, special, exemplary, or punitive losses; loss of profits, revenue, anticipated savings, business opportunity, goodwill, or data (other than the cost of restoring data from back-ups maintained as required by the SOW), regardless of whether the relevant Party was advised of the possibility of those losses.

14.2.3 **Mandatory carve-outs.** §14.2.1 and §14.2.2 do not exclude or limit liability that may not be excluded or limited under mandatory law, including liability for personal injury or death, intent, gross negligence, fraud, or under the Product Liability Directive (Council Directive 85/374/EEC as recast by Directive (EU) 2024/2853 [VERIFY recast commencement]).

### 14.3 [Market-standard] Liability cap

14.3.1 **Cap.** Each Party's aggregate liability arising out of or in connection with this MSA and all SOWs is limited to the greater of (a) {{Liability Cap Multiplier}} times the fees paid and payable by {{Client Short Name}} under the SOW that gave rise to the claim in the twelve months preceding the first event giving rise to liability, or (b) {{Liability Cap Floor}}.

14.3.2 **Excluded losses.** Subject to §14.3.3, neither Party is liable for indirect, consequential, special, exemplary, or punitive losses, or for loss of profits, revenue, anticipated savings, goodwill, opportunity, or data (other than the cost of restoring back-ups maintained as required by the SOW), regardless of whether the relevant Party was advised of the possibility.

14.3.3 **Carve-outs.** The cap in §14.3.1 and the exclusion in §14.3.2 do not apply to:

(a) personal injury, death, or damage to tangible property caused by a Party's negligence;
(b) intentional acts (`Vorsatz`) or gross negligence (`grobe Fahrlässigkeit`), where exclusion or cap-limitation is not permitted under § 309 No 7 BGB or the equivalent provision in the relevant Member State;
(c) fraud or fraudulent misrepresentation;
(d) breach by either Party of §10 (Confidentiality / trade secrets), where the breach is intentional or grossly negligent;
(e) the indemnity obligations in §13.1.1 / §13.1.4 / §13.3.1 / §13.3.2 (subject to a separate super-cap of two (2) times the cap in §14.3.1, save where mandatory law prevents the super-cap);
(f) {{Client Short Name}}'s payment obligations for accepted Deliverables;
(g) liability under the EU Product Liability Directive (Directive (EU) 2024/2853 [VERIFY recast commencement] / Council Directive 85/374/EEC) and any equivalent national-law product-liability regime;
(h) supervisory-authority administrative fines under Article 83 GDPR, to the extent attributable to a Party's own breach of §11 or the DPA; and
(i) any other liability that may not be excluded or limited under mandatory law.

14.3.4 **AGB transparency (DE).** Where the German overlay applies, the cap in §14.3.1 and the exclusion in §14.3.2 are intended to comply with §§ 305c, 307, and 309 No 7 BGB. The Parties acknowledge that, in the B2B context governed by § 310(1) BGB, a `mittelbar` cap of fees-paid is recognised as conformant where (i) it carves out intent, gross negligence, personal injury and death, fraud, the cardinal-duty doctrine ("`Kardinalpflichten`"), and product-liability claims; and (ii) it leaves intact mandatory remedies including supervisory-authority fines under GDPR. To the extent any element of this §14 is found to be unduly disadvantageous under § 307 BGB, severance under §19.7 applies and the closest enforceable equivalent will be substituted.

14.3.5 **Cardinal duties (DE).** Liability for breach of `Kardinalpflichten` (essential contractual duties on which a Party may typically rely) is limited to typical, foreseeable damages of the kind that the breaching Party should reasonably have foreseen at the date of conclusion, and is not excluded; for these purposes the cap in §14.3.1 continues to apply unless the breach falls within §14.3.3(b).

## 15. Insurance

This Section sets out the insurance each Party must maintain. {{Provider Short Name}} maintains, at its own cost, with reputable insurers authorised in the EU/EEA, the following minimum cover throughout the Term and for at least three (3) years (or, for product-liability cover, six (6) years) following expiry or termination:

15.1 **Professional indemnity / `Berufshaftpflicht` / `RC Pro`.** Cover of not less than {{PI Insurance Minimum}} per claim and in the aggregate for civil liability arising from professional negligence, errors, or omissions in the Services.

15.2 **Public / general liability / `Betriebshaftpflicht` / `RC Exploitation`.** Cover of not less than {{PL Insurance Minimum}} per claim and in the aggregate for third-party bodily injury and property damage.

15.3 **Cyber.** Cover of not less than {{Cyber Insurance Minimum}} per claim for cyber events (including data-breach response, business-interruption, ransomware, and third-party data-protection liability), having regard to the ENISA Cloud-Security guidance and to the technological state-of-the-art for the Services. Cover should not be subject to broad war-or-cyber-war exclusions that would defeat the purpose of cyber cover for ordinary criminal activity.

15.4 **Employer's liability / workers' compensation equivalent.** Where {{Provider Short Name}} employs personnel deployed in connection with the Services, cover of not less than {{WC Insurance Minimum}} per claim, in compliance with the host-Member-State social-security and accident-insurance regime (for example, the German `Berufsgenossenschaft` regime; the French `accidents du travail / maladies professionnelles` regime; the Italian INAIL regime).

15.5 **D&O cover.** Where required by Annex C or by a SOW, directors-and-officers cover of not less than the amount stated.

15.6 **Certificate of currency.** {{Provider Short Name}} provides a current certificate of currency (or local equivalent — `Versicherungsbestätigung` (DE), `attestation d'assurance` (FR), `certificato di copertura` (IT)) on signature, on each renewal, and on reasonable request. EU/EEA insurance certificates are the customary evidence; an ACORD certificate of insurance is not required and may be substituted with the local equivalent.

15.7 **No subrogation.** {{Provider Short Name}} procures that its insurers waive subrogation against {{Client Short Name}} to the extent permitted by the applicable policy and law.

15.8 **Notice of material change.** {{Provider Short Name}} promptly notifies {{Client Short Name}} of any cancellation, non-renewal, or material reduction of cover required under this §15.

## 16. Term & termination  *(DUAL-PERSPECTIVE)*

This Section sets out how long the MSA lasts and how either Party may exit.

16.1 **Term.** This MSA takes effect on the Effective Date and continues for the Initial Term of {{Initial Term Length}}. Thereafter it renews automatically for successive {{Renewal Term Length}} periods unless either Party gives notice of non-renewal at least {{Termination Notice Window}} before the end of the then-current Term.

### 16.2 [Client-favourable] Termination

16.2.1 **Termination for convenience.** {{Client Short Name}} may terminate this MSA or any SOW for convenience on {{Termination Notice Window}}'s prior written notice. {{Client Short Name}} pays for Services performed and Deliverables accepted up to the effective date of termination; no termination fee or "minimum take" is owed for unperformed work, save where a SOW expressly includes a non-cancellable component (for example, a pre-paid licence fee for a third-party tool).

16.2.2 **Termination for cause.** {{Client Short Name}} may terminate this MSA or any SOW immediately on written notice where {{Provider Short Name}} (a) commits a material breach not cured within {{Cure Period}} of written notice; (b) repeats a previously cured breach within twelve months; (c) becomes insolvent (`Insolvenzantrag` (DE), `procédure collective` (FR), `procedura concorsuale` (IT)) or enters comparable proceedings; or (d) experiences a change of control to a competitor or a sanctioned person.

### 16.3 [Provider-favourable] Termination

16.3.1 **Termination for cause only.** {{Client Short Name}} may not terminate the MSA or an active SOW for convenience before the end of the Initial Term except by paying a termination fee equal to the unpaid amounts that would have been payable through the end of the Initial Term, less mitigation that {{Provider Short Name}} could reasonably achieve.

16.3.2 **Provider termination rights.** {{Provider Short Name}} may terminate this MSA or any SOW (a) for non-payment of any undisputed amount overdue by more than thirty (30) days following written notice; (b) for material breach not cured within {{Cure Period}}; or (c) for {{Client Short Name}}'s insolvency or comparable proceedings.

### 16.4 [Market-standard] Termination

16.4.1 **For convenience.** Either Party may terminate this MSA (but not an active SOW that the Parties have not specifically permitted to terminate for convenience) on {{Termination Notice Window}} prior written notice, save that any active SOW continues to be governed by this MSA until that SOW expires or is itself terminated.

16.4.2 **For cause.** Either Party may terminate this MSA or any SOW immediately on written notice for the other Party's (a) material breach not cured within {{Cure Period}} of written notice; or (b) insolvency or comparable proceedings.

16.4.3 **Extraordinary termination (DE § 314 BGB).** Notwithstanding any other provision of this MSA, either Party retains its right of extraordinary termination under § 314 BGB (or the equivalent provision of the applicable governing law) for `wichtiger Grund` (good cause); this right cannot be excluded by contract and any cap on termination rights in this §16 does not apply where § 314 BGB grounds exist.

16.4.4 **Effect of termination.** On termination, (a) {{Provider Short Name}} ceases work on the affected SOW(s) save for any agreed wind-down activities (§17); (b) {{Client Short Name}} pays for Services performed and Deliverables accepted up to the effective date; (c) each Party returns or destroys the other's Confidential Information (§10.8) and Personal Data (§11 / DPA); (d) accrued rights and remedies survive; (e) those provisions intended to survive (including §§ 9, 10, 11, 13, 14, 18, and 19) survive.

16.4.5 **Consumer carve-out (B2C only).** *OPTIONAL — only if a consumer touchpoint exists.* Where the Services or any Deliverable is supplied to a "consumer" within the meaning of Article 2(1) of Directive 2011/83/EU, the consumer's right of withdrawal (`Widerrufsrecht`) under Articles 9–16 of that Directive applies and prevails over this §16, including the fourteen (14)-day cooling-off period and the requirement to notify withdrawal using the model form. This provision does not apply to a B2B engagement.

## 17. Transition assistance & wind-down  *(DUAL-PERSPECTIVE)*

This Section governs how Services hand over to {{Client Short Name}} or to a successor on expiry or termination.

### 17.1 [Client-favourable] Transition assistance

17.1.1 **Transition Period.** On expiry, non-renewal, or termination for any reason other than termination for cause by {{Provider Short Name}} for non-payment, {{Provider Short Name}} provides transition assistance for up to one hundred eighty (180) days at the rates stated in the SOW (or, if none, at {{Provider Short Name}}'s then-current published rates with a documented reasonable-rate adjustment).

17.1.2 **Scope of assistance.** Transition assistance includes (a) knowledge transfer; (b) documentation of operational and security configurations; (c) handover of code repositories, environments, credentials, and access logs; (d) cooperation with the successor; (e) export of {{Client Short Name}} data in a structured, commonly used, and machine-readable format compatible with Article 4 / Article 23 et seq. of the Data Act; and (f) certified deletion of {{Client Short Name}} data once handover is confirmed.

17.1.3 **No degradation.** During the Transition Period, {{Provider Short Name}} maintains the level of Service stated in the SOW and does not allocate resources in a way that materially degrades performance.

### 17.2 [Provider-favourable] Transition assistance

17.2.1 **Limited transition.** Transition assistance is limited to ninety (90) days of cooperation at {{Provider Short Name}}'s then-current rates and is conditional on {{Client Short Name}} being current on all undisputed amounts owing.

17.2.2 **Out-of-scope work.** Transition activities not described in the SOW are out of scope and are subject to a Change Order under §6.

### 17.3 [Market-standard] Transition assistance

17.3.1 **Period.** Transition assistance is provided for up to one hundred and twenty (120) days from the effective date of termination, at the rates stated in the SOW or, if none, at {{Provider Short Name}}'s then-current rates.

17.3.2 **Deliverables on exit.** {{Provider Short Name}} delivers the data, code, documentation, and credentials necessary for {{Client Short Name}} (or its successor) to continue equivalent services, in formats compatible with Articles 23–31 of the Data Act where the Services fall within the Data Act's portability scope [VERIFY service-by-service applicability].

17.3.3 **Records and personal-data deletion.** {{Provider Short Name}} returns or, at {{Client Short Name}}'s election, deletes all Personal Data and Confidential Information at the end of the Transition Period, on the terms of §10.8 and the DPA, and provides a written certification of deletion within thirty (30) days.

17.3.4 **NIS2 / DORA / sectoral cooperation.** Where {{Client Short Name}} is subject to NIS2 or DORA exit-strategy obligations, {{Provider Short Name}} cooperates to enable orderly exit consistent with Article 30(3)(g) DORA (where applicable) and Article 21(2)(d) NIS2 supply-chain controls.

## 18. Dispute resolution & governing law

This Section sets out which law governs and where disputes are heard.

18.1 **Governing law.** This MSA and any non-contractual obligations arising out of or in connection with it are governed by the law of {{Governing Law}} (default: Ireland, English-language and common-law-flavoured), excluding its conflict-of-laws rules. The UN Convention on Contracts for the International Sale of Goods (CISG) does not apply.

18.2 **Alternative governing-law elections.** *OPTIONAL — only if the parties prefer a civil-law seat.* The Parties may elect Dutch law (Netherlands), German law (Germany — `Kaufmanns-` and BGB-flavoured), French law (France — `droit civil`), Belgian law, Luxembourg law, or another EU/EEA Member State's law in the SOW or in §19.10; an elected Member-State law replaces Irish law for this MSA on countersignature of that election. Where the elected law is German, §§ 305–310 BGB and § 126a BGB apply automatically and the AGB transparency review is part of judicial scrutiny.

18.3 **Jurisdiction.** Subject to §18.4, the Parties submit to the exclusive jurisdiction of the courts of {{Venue}} for any dispute arising out of or in connection with this MSA, in accordance with Article 25 of Regulation (EU) No 1215/2012 (Brussels I-bis Recast). Where {{Governing Law}} is Ireland, the Parties choose the courts of Dublin.

18.4 **Arbitration alternative.** *OPTIONAL — only if elected on signature.* The Parties may, by election in the signature block or in a SOW, refer disputes instead to arbitration under the {{Arbitration Rules}} (default: ICC) of the {{Arbitral Institution}}, seated at {{Arbitration Seat}} (default: Dublin; alternatives: Stockholm under SCC Rules, Vienna under VIAC Rules, Paris under ICC Rules, Frankfurt under DIS Rules), conducted in the {{Language Default}}. The arbitral tribunal consists of one arbitrator for disputes below {{Currency}} 1,000,000 and three arbitrators for disputes at or above that threshold. The award is final and binding and may be enforced under the New York Convention 1958.

18.5 **Pre-dispute escalation.** Before commencing court or arbitration proceedings, the Parties escalate the dispute in writing to a senior representative of each Party, who confer in good faith for thirty (30) days. This obligation does not prevent a Party from seeking interim or injunctive relief at any time, including provisional measures under Article 35 Brussels I-bis Recast.

18.6 **Injunctive relief.** Either Party may seek interim, conservatory, or injunctive relief from any court of competent jurisdiction (including under Articles 31 and 35 Brussels I-bis Recast) without first complying with §18.5.

18.7 **Mediation election.** *OPTIONAL — only if Parties elect.* Either Party may at any time propose mediation under the rules of the chosen institution (for example, the ICC International Centre for ADR or the WIPO Arbitration and Mediation Center). Mediation does not pause the running of any limitation or statute-of-prescription period; the Parties record their agreement that they will, where lawful, suspend running of `Verjährung` (DE) or `prescription` (FR) for the duration of any agreed mediation.

## 19. General provisions & signature block

19.1 **Notices.** Notices under this MSA are given in writing in the {{Language Default}} (with translation election as set out in §19.8) to the addresses on the cover page (or to {{Provider Notice Email}} / {{Client Notice Email}} for ordinary contractual notices) and are deemed received (a) on personal delivery; (b) on the second Working Day after posting by registered post in the EU/EEA; or (c) on the Working Day after dispatch by email, save that termination notices, notices of breach, and notices invoking §16.4.3 (extraordinary termination) are also given in writing on paper or by qualified electronic signature.

19.2 **Schriftform / Textform (DE).** Where the German overlay applies, this MSA is amended only in `Textform` within the meaning of § 126a BGB (qualified electronic signature or original signature on paper). For amendments above {{Schriftform Threshold}}, `Textform` is mandatory; for amendments below the threshold, ordinary email correspondence is sufficient. The "double-written-form" clause has been individually negotiated within the meaning of § 305(1) sentence 3 BGB; the Parties record their intention that this clause is not an inadequately disadvantageous standard term under § 307 BGB.

19.3 **eIDAS signature.** This MSA may be signed in counterparts using qualified electronic signatures, advanced electronic signatures, or simple electronic signatures within the meaning of Articles 25–34 of Regulation (EU) 910/2014 (eIDAS). The Parties intend signatures at level {{eIDAS Signature Level}} (default: advanced) and acknowledge that qualified electronic signatures are equivalent to handwritten signatures for purposes of mandatory `Schriftform` requirements (Article 25(2) eIDAS / § 126a BGB).

19.4 **Assignment and change of control.** Neither Party may assign or transfer this MSA without the other's prior written consent, save that either Party may assign to an Affiliate or to a successor in connection with a merger, sale of substantially all assets, or restructuring, on prior notice to the other and provided that the assignee assumes all obligations.

19.5 **Sub-contracting.** Sub-contracting of {{Provider Short Name}}'s obligations is subject to §7.7. {{Client Short Name}} may not delegate its payment obligations save by assignment under §19.4.

19.6 **No waiver.** Failure or delay in exercising any right under this MSA does not waive that right or any other right; a waiver must be in writing and signed.

19.7 **Severance.** If any provision of this MSA is held by a court of competent jurisdiction or arbitral tribunal to be invalid or unenforceable, that provision is severed and the remainder continues in force; the Parties replace the severed provision with the closest enforceable equivalent that gives effect to their original intention. Where the German overlay applies, the Parties record that they reject any general "salvatorische Klausel" presumption against the dispositive law of § 306 BGB; severance must give effect to the closest enforceable equivalent and does not default to dispositive law where the dispositive law would be markedly different from the Parties' commercial bargain.

19.8 **Language and Toubon Law.** This MSA is executed in {{Language Default}} (default: English), which is the controlling language. The Parties may agree on a translation in {{Translation Election}} (German, French, or Italian) for convenience, in which case the {{Language Default}} version controls in any conflict. Where the Services are physically performed in France for a French-language consumer, French Law No 94-665 of 4 August 1994 (the "Toubon Law") may require a French version; the Parties cooperate in good faith to produce a French translation in those cases, the controlling-language stipulation continuing to apply between the Parties as a matter of contract.

19.9 **Force Majeure.** A Party is not in breach to the extent it is prevented from performing by Force Majeure, and is excused for as long as the Force Majeure subsists, provided it gives prompt notice and uses reasonable efforts to mitigate. Force Majeure does not extend to payment obligations save where the underlying payment infrastructure is itself unavailable.

19.10 **Entire agreement.** This MSA, the DPA, the SOWs, and the Annexes are the entire agreement between the Parties on its subject matter and supersede all prior negotiations, arrangements, and statements (save for prior NDAs, which roll into §10 unless expressly superseded). This clause does not exclude liability for fraud or fraudulent misrepresentation.

19.11 **Counterparts.** This MSA may be signed in counterparts (including electronic counterparts under §19.3), each of which is an original and which together form one document.

19.12 **No partnership or agency.** Nothing in this MSA creates a partnership, joint venture, employment, or agency relationship; neither Party may bind the other.

19.13 **Third-party rights.** Save where expressly stated, no person other than the Parties has any right under this MSA. Affiliates that sign a SOW under §3.2 take direct rights under that SOW.

19.14 **§ 102 GWB notice (DE).** *OPTIONAL — only where this MSA functions as a procurement framework subject to public-procurement law.* Where this MSA is a "framework agreement" within the meaning of § 103(5) GWB or Article 33 of Directive 2014/24/EU, the Parties record that the framework rules do not exclude an award procedure for individual SOWs where required by mandatory public-procurement law; the Parties cooperate to comply with those rules.

19.15 **Anti-bribery and sanctions.** Each Party complies with applicable anti-bribery and anti-corruption law (including the OECD Anti-Bribery Convention, the German `Korruptionsbekämpfungsgesetz`, the French `Loi Sapin II` anti-corruption duties, and the UK Bribery Act 2010 to the extent it has extraterritorial effect on either Party) and applicable sanctions law (EU restrictive measures and Member-State implementing acts).

19.16 **Survival.** §§ 9, 10, 11, 12 (with respect to representations true at signature), 13, 14, 16.4.4, 17, 18, and this §19 survive expiry or termination to the extent necessary to give effect to their terms.

19.17 **Reading conventions.** Words importing the singular include the plural and vice versa. References to a statute or regulation are references to it as amended, replaced, or recast (and to its national implementing acts where the EU instrument is a Directive). Headings are for convenience only.

---

### Signature block

Signed for and on behalf of:

**{{Provider Legal Name}}** ({{Provider Legal Form}}, {{HR Number}})
By: ____________________________
Name: {{Provider Signatory Name}}
Title: {{Provider Signatory Title}}
Date: __________________________
VAT ID: {{VAT ID Provider}}

**{{Client Legal Name}}** ({{Client Legal Form}}, {{Client HR Number}})
By: ____________________________
Name: {{Client Signatory Name}}
Title: {{Client Signatory Title}}
Date: __________________________
VAT ID: {{VAT ID Client}}

The Parties intend execution by qualified or advanced electronic signature under Article 25 of Regulation (EU) 910/2014 (eIDAS); for Schriftform-mandatory amendments under § 126a BGB the Parties will use a qualified electronic signature or wet-ink signature on paper original.

---

## Annex A — Statement of Work (SOW) template

Use the dedicated `legalcode-sow` template for a fully-developed SOW pack. The minimum elements that must appear in any SOW under this MSA are listed below.

**SOW Header.** SOW Number; Effective Date; reference to this MSA (title and Effective Date); Provider entity and Client entity (and any Affiliate signing under §3.2); SOW currency (default {{Currency}}); SOW points of contact (commercial and technical for each Party).

**1. Description of Services.** A narrative description of what {{Provider Short Name}} will do, including any service levels and performance metrics.

**2. Deliverables and Acceptance Criteria.** Each Deliverable identified by name, format, target acceptance date, and the criteria against which it is tested. Where the SOW does not state specific Acceptance Criteria, the conformity standard in §8 applies.

**3. Timeline / Milestones.** A schedule with start date, milestones, and target completion date; dependencies on {{Client Short Name}}'s inputs are flagged.

**4. Fees.** Fee model (fixed-fee, T&M with rate card, capped T&M, retainer, hybrid); invoicing cadence; expense pre-approval thresholds; any fee escalators (typically tied to a published EU index such as Eurostat HICP).

**5. Key Personnel and approved Sub-providers.** Named individuals, role, percentage of time committed, and replacement protocol; sub-providers from Annex B, with role and Sub-processor flag where Personal Data is involved.

**6. Personal-data processing particulars.** Categories of data subjects, categories of Personal Data, processing purposes, processing operations, retention periods, sub-processors, and transfer particulars (referenced into the DPA).

**7. AI / NIS2 / DORA / CRA classification.** AI Act risk-tier flag ({{AI Act Tier}}), CRA classification ({{CRA Status}}), NIS2 essential/important flag ({{NIS2 Class}}), and DORA flag ({{DORA Status}}) for the engagement.

**8. Assumptions and dependencies.** What {{Provider Short Name}} relied on in pricing the SOW; failure of which triggers a Change Order under §6.

**9. SOW-specific deviations from the MSA.** Any Section of the MSA varied for this engagement, drafted in compliance with §3.1.

**10. Signature block.** Authorised signatures of both Parties (eIDAS-compliant), and Affiliate signature where §3.2 applies.

---

## Annex B — Approved subcontractors & key personnel

The Parties record below the sub-providers and Key Personnel approved at the Effective Date. Updates are made by countersigned addendum (or, for Sub-processors, on the prior-authorisation regime in §11.5 / the DPA).

**Approved sub-providers (general).**

| Sub-provider | Service | Country | Sub-processor under §11? |
|--------------|---------|---------|--------------------------|
| {{Subcontractor Name}} | {{Subcontractor Service}} | {{Subcontractor Country}} | Yes / No |
| ... | ... | ... | ... |

**Approved Sub-processors (Personal Data).**

| Sub-processor | Processing role | Data Importer Country | SCC Module | Onward transfers? |
|---------------|------------------|------------------------|------------|---------------------|
| {{Subprocessor Name}} | {{Subprocessor Role}} | {{Data Importer Country}} | {{SCC Module}} | Yes / No |
| ... | ... | ... | ... | ... |

**Key Personnel.**

| Individual | Role | Engagement | % Commitment | Replacement protocol |
|------------|------|-------------|----------------|------------------------|
| {{Key Person Name}} | {{Key Person Role}} | {{SOW Reference}} | {{Commitment %}} | §7.5 |
| ... | ... | ... | ... | ... |

**A1 portable documents.** For each posted-worker individual, {{Provider Short Name}} maintains a current A1 (Article 19 of Regulation (EC) 987/2009). Copies are made available on reasonable request.

---

## Annex C — Service standards & acceptance criteria framework

This Annex sets out the agreed framework for measuring quality of Service and assessing Deliverables. It does not, on its own, create a binding service-level commitment unless adopted by reference in a SOW.

**C.1 Service standards.** Where a SOW commits to a service-level standard (availability, response time, throughput, etc.), the SOW states the metric, the measurement methodology, the reporting frequency, the credit or remedy for failure, and any cap on credits or remedies.

**C.2 Reporting cadence.** Default: monthly written report covering progress against milestones, hours billed (T&M), risks, change-request status, and any incident or near-incident affecting {{Client Short Name}} data.

**C.3 Acceptance criteria framework.** Acceptance Criteria for Deliverables follow these categories (one or more selected per Deliverable in the SOW):

(a) functional acceptance against named test cases;
(b) conformity acceptance against the SOW description;
(c) standards acceptance (ISO/IEC 27001, ISO/IEC 9001, ISO/IEC 25010, ENISA Cloud-Security guidance, AI Act conformity assessment where applicable);
(d) regulatory acceptance (data-protection impact assessment sign-off, NIS2 risk-assessment sign-off, DORA register-of-information sign-off);
(e) security acceptance (penetration-test report against agreed scope; vulnerability remediation against CVSS thresholds; SBOM cross-checked for open-source licence compliance).

**C.4 Defect classification.**

| Severity | Description | Target response | Target resolution |
|----------|-------------|------------------|--------------------|
| 1 (Critical) | Production down or material data loss | 1 hour | 8 hours |
| 2 (Major) | Material function impaired, no workaround | 4 hours | 1 Working Day |
| 3 (Minor) | Minor function impaired, workaround available | 1 Working Day | 5 Working Days |
| 4 (Cosmetic) | Cosmetic / non-blocking | 5 Working Days | Next release |

**C.5 Security baseline.** {{Provider Short Name}} maintains, at minimum: information-security policy aligned with ISO/IEC 27001; access control on least-privilege basis; encryption in transit (TLS 1.2 or higher) and at rest (AES-256 or equivalent) for Personal Data and trade secrets; vulnerability management with timely patching; logging and monitoring with retention not less than the period required by Article 30 GDPR; secure SDLC with code-review for security-relevant changes; incident-response plan tested at least annually; supply-chain security (sub-provider due diligence and contractual flow-down).

**C.6 ENISA reference.** TOMs are aligned with ENISA's published guidance on cloud security, secure software development, and incident response, as updated from time to time. Where a SOW specifies a different baseline, the SOW prevails.

---

## Appendix 1 — Merge fields (consolidated)

The merge fields used in this template are consolidated below for ease of search-and-replace; per-jurisdiction additions are marked **(EU)**.

```
{{MSA Title}}
{{MSA Effective Date}}
{{Provider Legal Name}}
{{Provider Legal Form}}                 (EU)
{{Provider Short Name}}
{{Provider Address}}
{{Provider Country}}
{{HR Number}}                           (EU)
{{VAT ID Provider}}                     (EU)
{{Provider Signatory Name}}
{{Provider Signatory Title}}
{{Provider Notice Email}}
{{Provider AR Email}}
{{Client Legal Name}}
{{Client Legal Form}}                   (EU)
{{Client Short Name}}
{{Client Address}}
{{Client Country}}
{{Client HR Number}}                    (EU)
{{VAT ID Client}}                       (EU)
{{Client Signatory Name}}
{{Client Signatory Title}}
{{Client Notice Email}}
{{Client AP Email}}
{{Initial Term Length}}
{{Renewal Term Length}}
{{Termination Notice Window}}
{{Cure Period}}
{{Currency}}
{{Payment Terms}}
{{Late Fee Rate}}
{{ECB Reference Date}}                  (EU)
{{Liability Cap Multiplier}}
{{Liability Cap Floor}}
{{PI Insurance Minimum}}
{{PL Insurance Minimum}}
{{Cyber Insurance Minimum}}
{{WC Insurance Minimum}}
{{IP Ownership Default}}
{{Open Source Policy}}
{{Acceptance Period}}
{{Deemed Acceptance Window}}
{{SOW Approval Method}}
{{Governing Law}}
{{Venue}}
{{Arbitration Rules}}
{{Arbitral Institution}}                (EU)
{{Arbitration Seat}}                    (EU)
{{Schriftform Threshold}}               (EU)
{{NIS2 Class}}                          (EU)
{{DORA Status}}                         (EU)
{{CRA Status}}                          (EU)
{{AI Act Tier}}                         (EU)
{{Data Importer Country}}               (EU)
{{SCC Module}}                          (EU)
{{Posted Workers Member State}}         (EU)
{{Whistleblower Channel URL}}           (EU)
{{Language Default}}                    (EU)
{{Translation Election}}                (EU)
{{eIDAS Signature Level}}               (EU)
{{Subcontractor Name}}
{{Subcontractor Service}}
{{Subcontractor Country}}
{{Subprocessor Name}}
{{Subprocessor Role}}
{{Key Person Name}}
{{Key Person Role}}
{{SOW Reference}}
{{Commitment %}}
```

---

## Appendix 2 — Authoritative references

The following EU and Member-State sources have been consulted as authoritative references during clean-room drafting. No verbatim text was used; only structure, statutory citations, and regulatory frameworks were drawn upon.

**EU regulations and directives**
- Regulation (EU) 2016/679 (GDPR)
- Commission Implementing Decision (EU) 2021/914 (Standard Contractual Clauses for international transfers)
- Commission Implementing Decision (EU) 2023/1795 (EU-US Data Privacy Framework adequacy)
- Directive 2011/7/EU (combating late payment in commercial transactions)
- Directive (EU) 2016/943 (trade-secret protection)
- Regulation (EU) 910/2014 (eIDAS)
- Council Directive 2006/112/EC (VAT, including Article 196 reverse charge)
- Directive 2014/55/EU (electronic invoicing in public procurement)
- Directive 96/9/EC (databases / sui generis right)
- Directive 96/71/EC and Directive (EU) 2018/957 (Posted Workers)
- Directive 2014/67/EU (Posted Workers Enforcement)
- Regulation (EU) 1215/2012 (Brussels I-bis Recast)
- Directive (EU) 2019/1937 (Whistleblowers)
- Regulation (EU) 2022/2554 (DORA)
- Directive (EU) 2022/2555 (NIS2)
- Regulation (EU) 2023/2854 (Data Act)
- Regulation (EU) 2024/1689 (AI Act)
- Regulation (EU) 2024/2847 (Cyber Resilience Act, CRA)
- Council Directive 85/374/EEC and Directive (EU) 2024/2853 (Product Liability)
- Directive 2014/24/EU (Public Procurement)
- Directive 2011/83/EU (Consumer Rights)
- Regulation (EU) 2021/821 (Dual-Use Export Control)
- Regulation (EC) 987/2009 Article 19 (A1 portable documents)
- Directive (EU) 2024/2831 (Platform Work)

**Member-State law (illustrative; consult local counsel)**
- DE: BGB §§ 126a, 305–310, 314, 640; UrhG §§ 12–14, 31, 31a, 32, 32a; GeschGehG §§ 1–4; HinSchG; SGB IV § 7a; GWB §§ 102–103
- FR: Code civil Art. 1240; CPI Art. L.121-1 / L.131-1 et seq.; Loi Toubon (No 94-665); Loi Sapin II; LME (Loi de modernisation de l'économie)
- IT: D.Lgs. 231/2002 (late payment transposition); D.Lgs. 24/2023 (whistleblower); Legge sul diritto d'autore Arts. 20–22 (moral rights)
- ES: Ley 3/2004 (late payment transposition); Ley de Propiedad Intelectual Art. 14 (moral rights)
- BE / NL / LU / IE: equivalent transpositions and statutes of general application

**Permissive baselines consulted (clean-room only — no verbatim use)**
- Bonterms Professional Services Agreement (PSA) v1.2 — `[CC0]`
- Common Paper Standard Services Agreement — `[CC-BY-4.0]`
- Common Paper SOW — `[CC-BY-4.0]`
- GitHub `site-policy` — `[CC0]`
- Mozilla legal templates — `[MPL-2.0]`
- Linux Foundation / Apache Software Foundation services agreement patterns — `[Apache-2.0]`
- EUR-Lex, EDPB guidelines, ENISA publications, national-DPA model clauses — `[public domain / open government]`

**Blocked baselines (not consulted; explicitly excluded).**
AWS PSA, Microsoft services agreements, Google Cloud PSA, IBM MSA, Salesforce PSA, Atlassian Services Agreement, SAP / Accenture / Deloitte / PwC framework agreements, and any CC-BY-SA / CC-BY-NC / CC-BY-ND / unspecified-licence template.

---

## Appendix 3 — Not-legal-advice closer

This template is provided for general informational purposes only and is **not legal advice**. It is a starting point for negotiation, not a finished agreement. Before signing, each Party should obtain advice from qualified counsel in the relevant Member State or EEA jurisdiction. In particular:

- Confirm that the IP-ownership default in §9 matches what the SOWs actually produce; software, marketing materials, designs, training corpora, and reports may warrant different defaults, and the moral-rights handling in civil-law Member States is irreducible.
- Confirm that the liability cap in §14 and the insurance minimums in §15 are commercially internally consistent and reflect the cover that is actually in force.
- Confirm the DPA reference in §11 points to a current DPA that reflects the parties' actual processing roles, transfer routes, sub-processors, and TOMs; do not rely on §11 alone.
- Confirm classification under NIS2 / DORA / CRA / AI Act / Data Act before signature; classification flags drive compliance obligations and are time-sensitive (commencement is staged).
- Confirm that the Schriftform threshold and `Textform` mechanism reflect the actual approval workflow in each Party.
- Confirm that the late-payment interest reference (ECB MRO + 8 percentage points) aligns with the most recent ECB rate published on the relevant {{ECB Reference Date}}.
- Confirm that the EU-US Data Privacy Framework adequacy decision remains in force at the time of signature; if challenged or invalidated, the Parties should fall back to SCCs (Decision 2021/914) without further amendment.

The Parties record that this template was assembled in clean-room form from the permissively-licensed baselines listed in Appendix 2 and from EU and national public-sector materials; no proprietary or restrictively-licensed source has been used.

— End of {{MSA Title}} (EU/EEA variant) —
