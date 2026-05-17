---
title: Master Services Agreement (UK)
jurisdiction: uk
statutes:
  - Late Payment of Commercial Debts (Interest) Act 1998
  - Housing Grants Construction & Regeneration Act 1996 (LDEDCA 2009)
  - ITEPA 2003 Pt 2 Ch 8 + Ch 10 (IR35 / off-payroll)
  - CDPA 1988 (IP / moral rights)
  - UCTA 1977 + Misrepresentation Act 1967
  - UK GDPR + DPA 2018 + DUAA 2025
  - NIS Regulations 2018
  - Modern Slavery Act 2015
  - Bribery Act 2010
  - Companies Act 2006
license: MIT
last_updated: 2026-04-29
---

# {{MSA Title}} (United Kingdom)

**Effective Date:** {{MSA Effective Date}}

**Parties:**

- **{{Provider Legal Name}}**, a company incorporated in {{Provider Country}} with company number {{Provider Companies House Number}} and registered office at {{Provider Address}} ("**{{Provider Short Name}}**" or "**Provider**").
- **{{Client Legal Name}}**, a company incorporated in {{Client Country}} with company number {{Client Companies House Number}} and registered office at {{Client Address}} ("**{{Client Short Name}}**" or "**Client**").

Each a "**Party**" and together the "**Parties**".

---

## Merge fields used in this document

In addition to the common merge fields listed in the pack README, the UK variant uses the following:

```
{{Provider Companies House Number}}        # eight-character company number
{{Client Companies House Number}}          # eight-character company number
{{Provider VAT Number}}                    # GB-prefixed VAT registration
{{Client VAT Number}}                      # GB-prefixed VAT registration
{{IR35 Status}}                            # "Outside" / "Inside" / "Not Applicable"
{{SDS Issuer}}                             # "Client" / "End-Client" / "Not Applicable"
{{Construction Operations Toggle}}         # "Yes — within Part II HGCRA scope" / "No"
{{NIS Operator Class}}                     # "OES" / "RDSP" / "Not Applicable"
{{Public Sector Toggle}}                   # "Yes — Procurement Act 2023 flow-down" / "No"
{{Modern Slavery Threshold Met}}           # "Yes — Client turnover ≥ £36m" / "No"
{{Cyber Essentials Required}}              # "Cyber Essentials" / "Cyber Essentials Plus" / "Not required"
{{ICO Registration Number}}                # if Provider is a controller in its own right
{{LCIA Toggle}}                            # "Courts of England" / "LCIA Arbitration"
{{Statutory Interest Rate}}                # "BoE base rate + 8%"
{{Recovery Cost Schedule}}                 # "£40 / £70 / £100 per Reg. 5A"
{{Operational Resilience Toggle}}          # "Yes — FCA SS1/21" / "No"
{{Deed Execution Required}}                # "Yes — IP assignment by deed" / "No"
{{Subscription Reminder Toggle}}           # "Yes — DMCCA Pt 4" / "No"
```

---

## 1. Plain-language summary

This Agreement is the framework under which {{Provider Short Name}} provides professional services to {{Client Short Name}}; each engagement is described in a Statement of Work or Order Form that hangs off these terms. Pricing, deliverables, milestones and the names of any key personnel sit in the SOW; the legal architecture — payment timing, intellectual property, confidentiality, liability, insurance, data protection — sits here. If a SOW and this Agreement disagree, this Agreement wins on legal architecture; the SOW wins on commercial particulars (fees, scope, dates), but only where the SOW is signed by an authorised signatory of each Party. The Agreement is governed by the laws of England and Wales, drafted in UK English, and built around the statutory floor of the Late Payment of Commercial Debts (Interest) Act 1998, the Construction Act payment regime where applicable, the Companies Act 2006, the Bribery Act 2010, the Modern Slavery Act 2015, the UK GDPR and the IR35 / off-payroll-working framework in ITEPA 2003. Neither Party will be in employment with the other; Provider remains an independent contractor and is responsible for its own tax, National Insurance and pension obligations except where the IR35 deemed-employer rules transfer that obligation to {{Client Short Name}} as set out in section 7. Plain-language summaries appear at the start of every numbered section so a non-lawyer can read this end-to-end without losing the thread.

The Parties intend this document to be legally binding on signature by both authorised signatories, and to remain effective for the Initial Term of {{Initial Term Length}}, automatically renewing for successive {{Renewal Term Length}} periods unless either Party gives notice as set out in section 16.

---

## 2. Definitions

This section defines the terms used in capitalised form throughout the rest of the Agreement; everything else takes its ordinary English meaning.

2.1 "**Acceptance Criteria**" means the objective, measurable tests for a Deliverable set out in the relevant SOW, or, if none, the tests set out in Annex C.

2.2 "**Acceptance Period**" means {{Acceptance Period}} days from delivery of a Deliverable, during which Client may test that Deliverable against the Acceptance Criteria.

2.3 "**Agreement**" means this Master Services Agreement, including all annexes, all SOWs and all Order Forms incorporated by reference, as amended in accordance with section 19.

2.4 "**Background IP**" means Intellectual Property Rights owned or licensed by a Party (a) before the Effective Date or (b) developed independently of the Services, in either case used or made available by that Party in performing the Services.

2.5 "**Business Day**" means any day other than a Saturday, Sunday or bank holiday in England and Wales.

2.6 "**Change Order**" means a written amendment to a SOW issued in accordance with section 6.

2.7 "**Confidential Information**" has the meaning given in section 10.

2.8 "**Construction Operations**" has the meaning given in section 105 of the Housing Grants, Construction and Regeneration Act 1996 (as amended). Where {{Construction Operations Toggle}} indicates "Yes", the payment provisions in sections 109–113 of that Act apply to this Agreement and to each affected SOW.

2.9 "**Deemed Acceptance Window**" means {{Deemed Acceptance Window}} days from delivery, after which a Deliverable is deemed accepted if Client has not issued a written notice of rejection identifying the failed Acceptance Criteria.

2.10 "**Deliverable**" means any work product, document, code, design, specification, configuration, dataset or other output identified as such in a SOW, in tangible or intangible form.

2.11 "**Foreground IP**" means Intellectual Property Rights created in the course of performing the Services, other than Background IP and other than Open-Source Components.

2.12 "**Insolvency Event**" means, in respect of a Party, any of: (a) a resolution to wind up (other than a solvent reorganisation), (b) the appointment of an administrator, administrative receiver, receiver, liquidator, supervisor or similar officer, (c) entry into a voluntary arrangement or scheme of arrangement with creditors, (d) inability to pay debts within the meaning of section 123 of the Insolvency Act 1986, or (e) any analogous event under the law of any other jurisdiction.

2.13 "**Intellectual Property Rights**" or "**IP**" means copyright and related rights, database rights, design rights (registered or unregistered), patents, trade marks, rights in confidential information, semiconductor topography rights, rights in domain names, moral rights, and all other intellectual or industrial property rights, in each case whether registered or unregistered and in any jurisdiction.

2.14 "**IR35**" means the rules in Chapter 8 and Chapter 10 of Part 2 of the Income Tax (Earnings and Pensions) Act 2003 ("ITEPA"), including the off-payroll working rules in Chapter 10 as amended.

2.15 "**Open-Source Component**" means any software (including libraries, frameworks and datasets) made available under an Open-Source Initiative-approved or Free Software Foundation-approved licence.

2.16 "**Personal Data**" has the meaning given in Article 4(1) of the UK GDPR.

2.17 "**Personnel**" means the directors, employees, consultants, agents and Subcontractors of a Party engaged in performing or receiving the Services.

2.18 "**Restricted Transfer**" means a transfer of Personal Data to a third country or international organisation that is restricted under Chapter V of the UK GDPR.

2.19 "**Services**" means the professional services described in any SOW, together with any associated Deliverables.

2.20 "**SOW**" means a Statement of Work issued under this Agreement substantially in the form of Annex A; "**Order Form**" means an alternative purchase document for recurring or managed services. The two terms are interchangeable for the purposes of this Agreement except where context requires otherwise.

2.21 "**Subcontractor**" means any third party engaged by Provider to perform any part of the Services.

2.22 "**UK GDPR**" means Regulation (EU) 2016/679 as it forms part of the law of England and Wales, Scotland and Northern Ireland by virtue of the European Union (Withdrawal) Act 2018, as amended (including by the Data Protection Act 2018 and the Data (Use and Access) Act 2025 ("**DUAA 2025**")).

---

## 3. Engagement structure

This Agreement is the master contract; SOWs and Order Forms are the operating layer. No work is authorised, no fee is owed and no Deliverable is contracted unless and until a SOW or Order Form referencing this Agreement has been signed by both Parties. The signature method is {{SOW Approval Method}}.

3.1 **Framework.** This Agreement governs all Services performed by Provider for Client during the Term. Each SOW is a separate, self-contained engagement that incorporates this Agreement by reference; nothing in a SOW creates an obligation on either Party to commission or accept any further SOW.

3.2 **Order of precedence.** Where there is a conflict, the order of precedence is: (a) any executed Change Order, (b) the SOW or Order Form, (c) the body of this Agreement, (d) any annex. The SOW prevails over this Agreement only on commercial particulars (fees, scope, dates, named personnel, milestones) and only where it expressly identifies the conflicting provision and the Parties' intention to vary it.

3.3 **No purchase commitment.** This Agreement does not commit Client to purchase any Services. Provider is not granted exclusivity. Client may engage other providers for any services, including services materially similar to those covered by a current SOW, save where the relevant SOW expressly grants exclusivity for a defined scope and period.

3.4 **Authorised signatories.** Each Party warrants that the individual signing each SOW or Order Form has the authority to bind that Party. A SOW may be signed electronically; the Parties acknowledge the validity of electronic signatures under section 7 of the Electronic Communications Act 2000 and (as retained) the eIDAS framework [VERIFY post-REUL retention status of Regulation (EU) No 910/2014].

3.5 **Purchase orders.** Any purchase order Client issues is for Client's internal accounting only. Pre-printed terms on a purchase order do not bind Provider unless they are expressly incorporated into a signed SOW.

---

## 4. Scope of Services and SOW process

The Services for any given engagement are whatever the relevant SOW says they are; this section describes how a SOW comes into existence and what it must contain to be enforceable.

4.1 **Required SOW contents.** Each SOW must, at a minimum, identify: (a) the Services and Deliverables; (b) the fee model (fixed-fee, time-and-materials, capped T&M, milestone-based, retainer or other); (c) the rate card or fixed fees; (d) the expected start and end dates and any milestones; (e) any named key Personnel and the {{IR35 Status}} of each; (f) the Acceptance Criteria, or a reference to Annex C; (g) any Client-furnished materials, environments or dependencies; (h) any deviations from this Agreement (which must expressly cite the section being varied).

4.2 **Drafting and approval.** Either Party may propose a SOW. Drafting is iterative. The SOW becomes binding only when signed by an authorised signatory of each Party using {{SOW Approval Method}}. Until that point, neither Party is bound by any draft, term sheet, exchange of emails or oral statement, however detailed.

4.3 **Provider obligations on Service delivery.** Provider will perform the Services with the reasonable skill and care to be expected of a competent professional providing services of the same type, in accordance with the SOW and any documented standards referenced in it. Provider will use suitably qualified Personnel, will manage Client-furnished materials with reasonable care, and will comply with Client's reasonable security, on-site and conduct policies as notified in writing.

4.4 **Client obligations on Service delivery.** Client will provide the Client-furnished materials, environments, decisions and access set out in the SOW, on the dates set out in the SOW. Where Client delay or default causes Provider to incur additional cost or to miss a milestone, Provider's obligations on time and budget are adjusted on a Business-Day-for-Business-Day basis and Provider may charge for any avoidable additional cost actually incurred, subject to a duty to mitigate.

4.5 **Termination of a single SOW.** A SOW may be terminated independently of this Agreement in accordance with section 16. Termination of a SOW does not affect the validity of any other SOW or this Agreement.

---

## 5. Fees, expenses and invoicing  *— DUAL-PERSPECTIVE*

The first sentence is the floor: Provider invoices in accordance with the SOW; Client pays within {{Payment Terms}} of receipt of a valid VAT invoice; late payment attracts statutory interest at {{Statutory Interest Rate}} plus reasonable recovery costs under regulation 5A of the Late Payment of Commercial Debts Regulations 2002 (as amended). Beyond that floor, the Parties may select one of the three drafting postures below.

5.1 **Invoicing mechanics.** Provider issues VAT invoices monthly in arrears, or at the cadence specified in the SOW, in {{Currency}}. Each invoice references the relevant SOW and Provider's VAT number ({{Provider VAT Number}}). Where the supply is subject to the post-Brexit B2B reverse charge for cross-border services [VERIFY current HMRC position on place-of-supply rules], the invoice will state "Reverse charge: customer to account for VAT" and no VAT will be charged.

5.2 **Late payment — statutory interest.** If Client fails to pay any undisputed sum by its due date, Provider is entitled, without further notice, to: (a) statutory interest at the Bank of England base rate in force on the day the debt becomes overdue plus 8 percentage points, accruing daily until paid, under section 4 of the Late Payment of Commercial Debts (Interest) Act 1998 [VERIFY current BoE base rate at the time the cause of action arises]; (b) reasonable recovery costs under regulation 5A — being £40 where the unpaid sum is up to £999.99, £70 where it is between £1,000 and £9,999.99, and £100 where it is £10,000 or more, plus any further reasonable costs of recovering the debt to the extent those costs exceed the fixed sum; and (c) suspension of further work under section 16.

5.3 **Disputed invoices.** Client may withhold payment of any individual line item it disputes in good faith, provided Client (a) pays the undisputed balance by the due date and (b) gives written notice within ten Business Days of the invoice date identifying the disputed line and the basis for the dispute. The Parties will use reasonable efforts to resolve any disputed line within twenty Business Days; failing resolution, either Party may invoke section 18.

5.4 **Construction Operations payments.** Where {{Construction Operations Toggle}} is "Yes":
(a) the Parties intend that the payment provisions of this Agreement comply with sections 109 to 113 of the Housing Grants, Construction and Regeneration Act 1996 (as amended by Part 8 of the Local Democracy, Economic Development and Construction Act 2009);
(b) the SOW must specify the dates on which payments become due, the final date for payment (no later than 30 days after the due date unless varied by SOW) and the basis for calculating the sums due;
(c) Client will issue a payment notice within five Business Days of the due date specifying the sum it considers due and the basis for it; if no payment notice is issued, the sum claimed in Provider's payment application becomes the notified sum;
(d) Client may issue a pay-less notice no later than five Business Days before the final date for payment specifying any amount it intends to withhold and the grounds; and
(e) any clause purporting to make payment to Provider conditional on Client receiving payment from a third party (a "pay-when-paid" provision) is, except where permitted by section 113, of no effect.

5.5 **Expenses.** Provider's reasonable, pre-approved, out-of-pocket expenses (travel, accommodation, third-party tooling) are reimbursable at cost on production of receipts and in line with any expenses policy referenced in the SOW. No mark-up is added unless the SOW expressly so provides.

5.6 **Taxes.** All fees are exclusive of VAT, which is chargeable at the prevailing rate. Each Party is responsible for its own corporation tax, business rates and similar imposts. Withholding obligations are addressed in section 7 (IR35) and section 19 (cross-border).

> **5-A. Client-favourable variant.** For Client-side drafting: net {{Payment Terms}} runs from receipt of a *correctly addressed and undisputed* VAT invoice; Client may consolidate all SOW invoicing into a single monthly statement; statutory interest accrues only on amounts undisputed at the time of the cause of action; Provider must give 10 Business Days' written notice and an opportunity to cure before invoking suspension under section 5.2(c); rate-card increases require 90 days' written notice and apply only to new SOWs and to SOW renewals after the notice period expires; expense pre-approvals must be obtained line-by-line above £500 per item; foreign exchange exposure beyond the SOW Currency sits with Provider unless the SOW specifies a hedge.

> **5-B. Provider-favourable variant.** For Provider-side drafting: net {{Payment Terms}} runs from invoice date; statutory interest accrues from the day after the due date without further notice; Provider may suspend Services on five Business Days' written notice for any undisputed amount unpaid for more than 15 days past the due date; rate-card increases of up to CPI + 2% per annum apply automatically on each anniversary of the SOW; expense pre-approvals are deemed given where the SOW includes a stated expenses budget; FX risk is shared 50/50 outside a stated hedge; Provider may charge a 1.5% per month administration fee on any payment processed by cheque or by means other than electronic bank transfer.

> **5-C. Market-standard variant.** Net 30 from receipt of a valid VAT invoice; one round of dispute notice within 10 Business Days; statutory interest at BoE base + 8% on undisputed amounts overdue for more than 10 Business Days; suspension on 10 Business Days' notice and continuing default; rate-card review annually with 60 days' written notice; expenses pre-approved in budget bands set in the SOW; FX risk follows the SOW Currency unless the SOW specifies otherwise.

---

## 6. Change control and Change Orders  *— DUAL-PERSPECTIVE*

Either Party may propose a Change Order; nothing changes the scope, fees or schedule of a SOW unless and until both Parties sign a written Change Order describing the change.

6.1 **Process.** A Change Order request is raised in writing and identifies the proposed change to scope, Deliverables, fees, schedule, key Personnel or Acceptance Criteria. Provider gives a written impact assessment within five Business Days (cost, schedule, dependencies, risks). The Parties negotiate in good faith. Once both Parties sign the Change Order, the SOW is amended; until then, the SOW continues unaltered.

6.2 **Pending changes.** Provider continues to perform the SOW as written while a Change Order is under discussion. Provider is not obliged to perform any work outside the current SOW pending signature; if Client directs Provider in writing to proceed at risk, the impact assessment becomes the basis of any later true-up.

6.3 **De minimis changes.** Either Party may treat a change as de minimis where it does not affect fees, schedule or named key Personnel; such changes may be confirmed by exchange of email between the Parties' designated contract managers.

6.4 **Records.** All Change Orders form part of the SOW. Provider maintains a Change Order log and provides it to Client on reasonable request.

> **6-A. Client-favourable variant.** Provider gives the impact assessment within three Business Days; impact-assessment time is non-billable; if the Change Order would increase the SOW total by more than 10%, Client may terminate the SOW for convenience without further fee subject to payment for work properly performed up to the date of termination; pricing for additional work follows the rate card applicable on the date of the original SOW; named key Personnel cannot be substituted via a Change Order without Client's written consent.

> **6-B. Provider-favourable variant.** The impact assessment is itself a chargeable deliverable at the SOW rate card; if Client requests that Provider proceed at risk, Provider may invoice on a T&M basis at the SOW rate card and Client agrees to true-up on Change Order signature; Provider may decline a Change Order that would conflict with other commitments or risk Provider's professional standards.

> **6-C. Market-standard variant.** Impact assessment within five Business Days at no separate charge; pending changes paused unless directed at risk; rate-card pricing as of Change Order signature; named key Personnel substitutions require written consent not to be unreasonably withheld.

---

## 7. Personnel, key personnel and subcontracting

This section sits at the intersection of three statutory regimes — IR35 / off-payroll working under ITEPA 2003, worker classification under the Employment Rights Act 1996 and the Equality Act 2010, and right-to-work checks under the Immigration Act 2016. Provider is engaged as an independent contractor; the working arrangements between Provider and its Personnel are Provider's responsibility, save where the off-payroll rules transfer that responsibility to Client by operation of law.

7.1 **Independent contractor status.** Provider performs the Services as an independent contractor. Nothing in this Agreement creates a partnership, joint venture, agency, employment or worker relationship between the Parties or between Client and any Provider Personnel. Provider is responsible for income tax, National Insurance contributions, pension auto-enrolment under the Pensions Act 2008, holiday pay, sick pay and any other entitlement of its own Personnel, save as expressly varied by the IR35 regime described below.

7.2 **IR35 status — single individual route (Chapter 8 ITEPA).** Where Provider supplies the Services personally through an intermediary (for example, a personal service company) and Client is a small company within the meaning of section 60A of ITEPA, the obligation to assess whether the engagement is "inside" IR35 sits with Provider's intermediary and the burden of any consequent PAYE/NICs liability sits with that intermediary.

7.3 **IR35 status — Chapter 10 (off-payroll working in the public and medium/large private sector).** Where Client is a public authority or a medium/large company within section 60A ITEPA, Client (or the deemed-employer entity in the chain) is responsible for issuing a Status Determination Statement ("**SDS**") under section 61T ITEPA in respect of any individual who would but for the intermediary be regarded as an employee of Client. Client will provide the SDS to Provider and to the worker before the Services start, will issue any reasonable disagreement response within 45 days under section 61T(8), and will operate PAYE/NICs as deemed employer where the SDS records the engagement as "inside" IR35. The current {{IR35 Status}} for the engagement is "{{IR35 Status}}", issued by {{SDS Issuer}}; this is reviewed at the start of each SOW and on any material change in working arrangements.

7.4 **CEST and supporting reasoning.** The Parties acknowledge that HMRC's Check Employment Status for Tax tool ("**CEST**") output is one input into a status determination but is not determinative. The SDS issuer must take reasonable care to consider all relevant factors, including the right of substitution, mutuality of obligation, control, financial risk and the employment-status case law (notably *Ready Mixed Concrete (South East) v MoPNI* [1968] 2 QB 497, *Pimlico Plumbers v Smith* [2018] UKSC 29, *Uber BV v Aslam* [2021] UKSC 5 and the HMRC manuals current at the time of the determination).

7.5 **Apportionment of IR35 liabilities.** Where IR35 applies and the engagement is "inside":
(a) Client (or its deemed-employer fee-payer) accounts for income tax and primary and secondary Class 1 NICs in respect of the deemed-direct-payment to the worker;
(b) the contract value paid to Provider is reduced by an amount equal to the deemed-direct-payment so that the gross cost to Client is held materially constant;
(c) where the SDS is issued late, withdrawn or proved incorrect through Client's failure to take reasonable care, Client indemnifies Provider against any tax, NICs, interest or penalty assessed on Provider's intermediary that arises from that failure; and
(d) where Provider's information to Client was materially false and led to the wrong determination, Provider indemnifies Client.

7.6 **Agency-worker overlay (Conduct Regulations 2003).** Where Provider acts as an employment business within the meaning of section 13 of the Employment Agencies Act 1973, the Parties' arrangements take into account the Conduct of Employment Agencies and Employment Businesses Regulations 2003. Either Party may, by written notice given before the supply of any individual, opt out of regulations 14 to 17 to the extent permitted by regulation 32, but only for individuals supplied through their own limited company or other corporate vehicle and not for any work-seeker who is an "individual" within the meaning of those Regulations. The opt-out does not bind any worker who is not party to it.

7.7 **Worker classification (ERA 1996 / Equality Act 2010).** Provider acknowledges that nothing in this Agreement is intended to confer worker status under section 230(3)(b) of the Employment Rights Act 1996 on any of Provider's Personnel in their relationship with Client. Provider is responsible for ensuring that its own contractual arrangements with its Personnel comply with the National Minimum Wage Act 1998 and the National Living Wage [VERIFY current rate], the Working Time Regulations 1998, the Pensions Act 2008 (auto-enrolment) and the Equality Act 2010 (including the duty to make reasonable adjustments for disabled employees). Each Party will not discriminate, harass or victimise any of the other Party's Personnel on any of the protected characteristics in the Equality Act 2010.

7.8 **Right to work.** Provider warrants that it has carried out, and will keep current, right-to-work checks under the Immigration Act 2016 and the Home Office "Code of practice on preventing illegal working" for all of its Personnel performing the Services. Provider will provide evidence of those checks within ten Business Days of Client's reasonable written request, redacting Personal Data not necessary for verification.

7.9 **Key Personnel.** Personnel identified as "key Personnel" in a SOW may not be removed from the engagement, except: (a) where the individual leaves Provider's employment or engagement; (b) where the individual is incapacitated; or (c) on Client's prior written consent. Replacements for key Personnel must be of equivalent skill and experience and acceptable to Client (acceptance not to be unreasonably withheld). Where Provider replaces a key person without consent except as permitted above, Client may treat the breach as material under section 16.

7.10 **Subcontracting.** Provider may not subcontract any material part of the Services without Client's prior written consent, save to those Subcontractors listed in Annex B (which Annex Provider may update from time to time on at least 20 Business Days' written notice, Client retaining a right of reasonable objection during that period). Provider remains liable for the acts and omissions of its Subcontractors as if they were its own. Provider's contracts with Subcontractors must be back-to-back on the IR35, data protection, confidentiality, IP, anti-bribery and modern-slavery clauses of this Agreement.

7.11 **Non-solicitation.** During the Term and for 12 months following its end, neither Party will solicit for employment any individual of the other Party who has been substantially involved in the Services, save that nothing in this clause prevents (a) general advertising not directed at any specific individual, (b) hiring an individual who applies in response to such advertising, or (c) hiring an individual whose employment with the other Party has ended at least six months before the approach.

---

## 8. Acceptance and Deliverables

This section explains how Client accepts a Deliverable, how it rejects one, and what happens at the end of the Acceptance Period.

8.1 **Delivery.** Provider delivers each Deliverable in accordance with the SOW. Delivery is effected by the means stated in the SOW or, in default, by transmission of the Deliverable to {{Client Notice Email}} or upload to a delivery location agreed by the Parties.

8.2 **Acceptance testing.** Within the Acceptance Period, Client tests the Deliverable against the Acceptance Criteria. Acceptance Criteria are objective, measurable and stated in the SOW; absent a SOW-specific definition, the Acceptance Criteria are those set out in Annex C.

8.3 **Acceptance.** Client accepts the Deliverable by: (a) written notice of acceptance; (b) using the Deliverable in production for any purpose other than testing; or (c) failing to issue a written notice of rejection within the Deemed Acceptance Window.

8.4 **Rejection.** If Client reasonably considers that a Deliverable fails the Acceptance Criteria, Client issues a written notice of rejection within the Acceptance Period identifying the specific failed criteria and supporting evidence. Provider has a reasonable cure period (default 15 Business Days, unless varied by SOW) to remediate and re-deliver. The acceptance cycle in this section 8 then repeats once for the re-delivered Deliverable.

8.5 **Persistent failure.** If a Deliverable fails Acceptance after two cycles of remediation, Client may at its option (a) accept the Deliverable subject to a fee reduction reasonably reflecting the deficit, (b) require further remediation at Provider's cost, or (c) terminate the affected SOW for cause under section 16 and recover any fees paid for the rejected Deliverable, less the value Client has retained.

8.6 **Partial acceptance.** Where a SOW contemplates discrete Deliverables, Client may accept some and reject others; rejection of one Deliverable does not stop time running on Acceptance of the others.

8.7 **Effect of acceptance.** Acceptance does not waive (a) any warranty in section 12, (b) any indemnity in section 13, or (c) any right Client has against latent defects that could not reasonably have been discovered during the Acceptance Period.

---

## 9. Intellectual property  *— DUAL-PERSPECTIVE*

The first sentence is the floor: Foreground IP in Deliverables vests in the Party identified in the SOW (default {{IP Ownership Default}}); each Party retains its Background IP and grants the other a licence only to the extent strictly required to use or deliver the Services; Open-Source Components are flagged and licensed separately. The Parties acknowledge the framework of the Copyright, Designs and Patents Act 1988 ("**CDPA**") and that, since 1 August 1989, copyright in commissioned works does not automatically vest in the commissioner — express assignment is required.

9.1 **Background IP.** Each Party retains all right, title and interest in its Background IP. Provider grants Client a non-exclusive, non-transferable, royalty-free licence to use Provider's Background IP solely to the extent embedded in or required to use a Deliverable accepted under section 8, for the internal business purposes of Client and its group companies for the term of the relevant Deliverable's useful life. Client grants Provider a non-exclusive, non-transferable, royalty-free licence to use Client's Background IP solely to the extent required to perform the Services, for the duration of the relevant SOW.

9.2 **Foreground IP — assignment (default).** Subject to clauses 9.4 (Open-Source) and 9.6 (moral rights) and conditional on payment of the fees properly invoiced for the Services giving rise to the Foreground IP, Provider, with full title guarantee, assigns to Client all Foreground IP in the Deliverables, by way of present assignment of present and future rights under sections 90 and 91 CDPA. Where the assignment requires execution as a deed (for example, to satisfy section 44 of the Companies Act 2006 in respect of the conferring entity) the Parties will execute a separate deed of assignment substantially in the form attached to the SOW; {{Deed Execution Required}} indicates whether deed execution is required for this engagement.

9.3 **Foreground IP — alternative (licence).** Where the SOW so specifies, Provider retains Foreground IP and grants Client a perpetual, irrevocable, worldwide, non-exclusive, royalty-free, sublicensable licence to use, copy, modify, distribute and prepare derivative works of the Foreground IP for Client's internal business purposes; sublicensing to Client's contractors and group companies is permitted on back-to-back terms.

9.4 **Open-Source Components.** Provider may incorporate Open-Source Components into Deliverables only in accordance with {{Open Source Policy}}. Provider maintains a software bill of materials ("**SBOM**") listing each Open-Source Component, its version, its licence and any copyleft obligations, and provides the SBOM to Client on delivery. Provider will not incorporate any Open-Source Component subject to a copyleft licence (GPL, AGPL, LGPL, MPL beyond file-scope, or any other licence with a "viral" copyleft effect on combined or derivative works) without Client's prior written consent.

9.5 **Database rights.** The Parties acknowledge that database rights subsist under the Copyright and Rights in Databases Regulations 1997. Where a Deliverable consists of or includes a database, the Foreground-IP rules in 9.2 / 9.3 apply equally to the database right and the underlying compilation.

9.6 **Moral rights.** Each natural-person author employed or engaged by Provider whose work is included in a Deliverable irrevocably and unconditionally waives, in favour of Client and its successors, the moral rights conferred by Chapter IV of Part I of the CDPA (including sections 77 to 89) to the extent such rights may be waived in writing under section 87 CDPA. Provider warrants that it holds, and will procure, all necessary written waivers and consents from its Personnel to give effect to this clause.

9.7 **Employee creators.** Provider acknowledges that, under section 11(2) of the CDPA, copyright in works made by an employee in the course of employment vests in the employer. Provider warrants that it has employment terms with each employee-author covering Foreground IP arising in the course of those employees' duties, and that those terms are sufficient to support the assignment in clause 9.2.

9.8 **Pre-existing third-party IP.** Where a Deliverable necessarily incorporates third-party IP not made available to Provider on terms permitting on-pass to Client, Provider identifies that IP in the SOW and procures a separate licence for Client at Client's cost (such cost agreed in advance).

> **9-A. Client-favourable variant.** All Foreground IP vests in Client at the moment of creation, including by way of present assignment of future rights; Provider warrants it has obtained all necessary moral-rights waivers (CDPA s.87) before any Personnel begins work on the Deliverable; Provider grants Client a perpetual, royalty-free licence to all Background IP embedded in any Deliverable, for any purpose (including resale of products incorporating that Background IP) on an irrevocable basis; the Open-Source policy is "Client pre-approval"; Provider gives a full IP indemnity (see section 13).

> **9-B. Provider-favourable variant.** Provider retains Foreground IP and grants Client a non-exclusive, non-sublicensable licence limited to internal business use within the named end-user count in the SOW; resale and OEM redistribution of the Deliverable are excluded; Provider's Background IP licence excludes any field of use beyond the SOW; Open-Source Components under permissive licences may be used without prior approval, subject only to SBOM disclosure; Provider's IP indemnity is capped at the fees paid for the affected Deliverable in the 12 months before the claim.

> **9-C. Market-standard variant.** Foreground IP assigned to Client conditional on payment; Background IP licensed on a perpetual, royalty-free basis limited to Deliverable use; Open-Source policy is "permissive only with notice"; moral-rights waivers obtained; IP indemnity follows section 13 with the standard cap and carve-outs.

---

## 10. Confidentiality

The first sentence is the floor: each Party will keep the other Party's Confidential Information confidential, will use it only as required to perform or receive the Services, and will protect it with the same degree of care it uses for its own information of comparable sensitivity (and in any event no less than reasonable care). The English-law equitable duty of confidence, the Trade Secrets (Enforcement, etc.) Regulations 2018 and any pre-engagement non-disclosure agreement between the Parties are layered on top of this section without conflict.

10.1 **Definition.** "**Confidential Information**" means any non-public information disclosed by or on behalf of one Party (the "**Discloser**") to the other (the "**Recipient**") that is identified as confidential or that a reasonable person would understand to be confidential from the nature of the information or the circumstances of disclosure.

10.2 **Carve-outs.** Confidential Information does not include information that the Recipient can show: (a) was lawfully in its possession without obligation of confidence before receipt; (b) is or becomes publicly known otherwise than through Recipient's act or omission; (c) is lawfully obtained from a third party without obligation of confidence; or (d) is independently developed by the Recipient without reference to the Discloser's Confidential Information.

10.3 **Permitted disclosures.** The Recipient may disclose Confidential Information: (a) to its Personnel and professional advisers on a need-to-know basis, subject to equivalent confidentiality obligations; (b) to the extent required by law, regulation or order of a court or competent regulatory authority, giving the Discloser as much advance notice as is lawful and cooperating in any reasonable application for a protective order; or (c) to its bona fide investors and acquirers under a customary non-disclosure obligation, but only summary information about the existence and high-level commercial terms of the engagement.

10.4 **Whistle-blowing carve-out.** Nothing in this section restricts a Recipient or any of its Personnel from making a "qualifying disclosure" within Part IVA of the Employment Rights Act 1996 (whistle-blowing) or a report to a competent regulator that is permitted or required by law.

10.5 **Trade secrets.** Where any Confidential Information also constitutes a "trade secret" within the meaning of the Trade Secrets (Enforcement, etc.) Regulations 2018, the Discloser retains all rights and remedies under those Regulations in addition to its rights under this section.

10.6 **Return or destruction.** On termination or expiry of this Agreement (or of the relevant SOW), the Recipient promptly returns or, at the Discloser's election, destroys all Confidential Information of the Discloser, save that the Recipient may retain copies (a) on routine backup media until those backups are recycled in the ordinary course, (b) in working papers required by law or professional standards, and (c) as required to prosecute or defend claims, in each case subject to continuing confidentiality.

10.7 **Survival.** This section survives termination for five years, except in respect of trade secrets, which remain protected for so long as they qualify as trade secrets.

---

## 11. Data protection and information security

The first sentence is the floor: where Provider processes Personal Data on behalf of Client, the Parties enter the data-processing-agreement at section 11.2 below and Provider's processing is governed by Article 28 UK GDPR; where Provider is an independent controller in respect of any Personal Data, that processing is governed by the controller-to-controller framework in section 11.3; either way, Provider implements information-security controls appropriate to the risk and to the nature of the Personal Data.

11.1 **Roles.** For each SOW, the Parties will record whether Provider is acting as a processor of Client (Article 28 UK GDPR), a controller in its own right, or a joint controller with Client; the default is processor unless the SOW states otherwise. Where Provider is acting as a processor, sections 11.2 and 11.4 to 11.13 apply; where Provider is a controller, sections 11.3 and 11.4 to 11.13 apply.

11.2 **Processor terms (Article 28 UK GDPR / DPA 2018).** Where Provider is a processor:
(a) Provider processes Personal Data only on the documented instructions of Client (the SOW being the documented instruction), unless required to do otherwise by domestic law (in which case Provider notifies Client of the requirement, save where prohibited by law);
(b) Provider ensures that persons authorised to process the Personal Data have committed to confidentiality or are under an appropriate statutory duty of confidentiality;
(c) Provider takes all measures required pursuant to Article 32 UK GDPR (security of processing);
(d) Provider engages sub-processors only with Client's general or specific written authorisation (Annex B serves as general authorisation; sub-processors not on Annex B require specific written authorisation);
(e) Provider assists Client in fulfilling its obligations to respond to requests from data subjects under Articles 12–22 UK GDPR;
(f) Provider assists Client with Articles 32–36 obligations (security, breach notification, data-protection impact assessments, prior consultation);
(g) at Client's choice, Provider deletes or returns all Personal Data after the end of the provision of services and deletes existing copies, unless retention is required by law;
(h) Provider makes available to Client all information necessary to demonstrate compliance with Article 28, and allows for and contributes to audits, including inspections, conducted by Client or another auditor mandated by Client. Audits are at Client's cost, on reasonable prior notice (not less than 20 Business Days save for incident-driven audits), no more than once in any 12-month period save where required by a regulator or following a personal-data breach, and conducted in a manner that does not compromise the confidentiality or operations of Provider's other clients.

11.3 **Controller terms.** Where Provider is a controller in respect of Personal Data, each Party complies with the UK GDPR and the DPA 2018 in its capacity as a controller; provides the other with such cooperation and information as is reasonably required to allow the other to comply with its own obligations; and gives notice without undue delay of any personal-data breach in its systems that affects the other's data subjects.

11.4 **Restricted Transfers.** Where the Services involve a Restricted Transfer, the Parties enter into the ICO's International Data Transfer Agreement ("**IDTA**") or the Addendum to the EU SCCs (Module 2 (controller-to-processor) or Module 3 (processor-to-processor) as applicable), in each case in the form published by the ICO at the time of the transfer. The IDTA / Addendum is incorporated into this Agreement by reference and prevails over any inconsistent provision of this section 11. The Parties will conduct a transfer-risk assessment ("**TRA**") in line with ICO guidance and update it on material change.

11.5 **Security controls.** Provider implements technical and organisational measures appropriate to the risk, taking account of the state of the art, the cost of implementation and the nature, scope, context and purposes of processing. Without limitation, those measures include: (a) access control and the principle of least privilege; (b) encryption in transit (TLS 1.2+) and at rest where the Personal Data is sensitive or involves special-category data within Article 9 UK GDPR; (c) logging and monitoring sufficient to detect and investigate suspicious activity; (d) backup, restore and disaster-recovery procedures appropriate to the SOW recovery objectives; (e) secure software development, including code review and dependency management; and (f) supply-chain security including the controls in section 11.7.

11.6 **Cyber Essentials / NIS / Operational Resilience overlays.** Where {{Cyber Essentials Required}} is "Cyber Essentials" or "Cyber Essentials Plus", Provider holds the relevant certification and maintains it in force during the Term; certificates are provided to Client on request. Where {{NIS Operator Class}} is "OES" or "RDSP", the Parties acknowledge that the Network and Information Systems Regulations 2018 apply to the relevant Party and the Services are provided so as to support that Party's compliance, including the security and incident-reporting duties under regulations 10–12. *OPTIONAL — only if Operational Resilience applies.* Where {{Operational Resilience Toggle}} is "Yes" and Client is regulated by the FCA or PRA, Provider supports Client's operational-resilience obligations under FCA SYSC 15A / PRA SS1/21, including by mapping important business services, identifying impact tolerances and participating in scenario testing on reasonable notice. Provider will reference the NCSC Cyber Assessment Framework as the baseline maturity model.

11.7 **Sub-processor security.** Provider imposes on each sub-processor data-protection and security obligations that are at least as protective as those in this section. Provider remains liable for the acts and omissions of each sub-processor as if they were its own.

11.8 **Personal-data breach notification.** Provider notifies Client of any personal-data breach affecting Client's Personal Data without undue delay and in any event within 48 hours of becoming aware. The notification includes, to the extent then known: the nature of the breach, the categories and approximate number of data subjects and records, the likely consequences, the measures taken or proposed and the contact details of Provider's data-protection officer or equivalent. Provider continues to update the notification as facts emerge and supports Client's notifications to the ICO and to data subjects.

11.9 **PECR overlay.** *OPTIONAL — only if the Services involve electronic communications, cookies or direct marketing.* Where the Services involve direct marketing, cookie placement, location data or traffic data, Provider supports Client's compliance with the Privacy and Electronic Communications (EC Directive) Regulations 2003 ("**PECR**"), including the consent and information requirements of regulations 6 (cookies) and 22 (electronic-mail marketing).

11.10 **DUAA 2025.** The Parties acknowledge the changes introduced by the Data (Use and Access) Act 2025 to the UK GDPR and DPA 2018 framework, including changes to the accountability framework, recognised legitimate interests, automated-decision-making rules and the regulator's structure. Provider will support Client's compliance with the DUAA 2025 changes as they take effect [VERIFY commencement of each Part of DUAA 2025 — the Act is being commenced in tranches and not all provisions are in force at the date of this Agreement].

11.11 **Data Protection Officer.** Where either Party is required to appoint a DPO under Article 37 UK GDPR or chooses to do so voluntarily, that Party provides the DPO's contact details to the other on request and updates them on change.

11.12 **Audit cost-sharing.** Where an audit under section 11.2(h) reveals material non-compliance, Provider bears the reasonable cost of the audit; otherwise, Client bears the cost.

11.13 **Records of processing.** Each Party maintains records of processing under Article 30 UK GDPR sufficient to demonstrate compliance and provides extracts to the other on reasonable request.

---

## 12. Representations and warranties  *— DUAL-PERSPECTIVE*

Each Party warrants to the other that it has the corporate authority to enter into this Agreement and that doing so does not breach any other obligation owed by it.

12.1 **Mutual warranties.** Each Party warrants on the Effective Date and continuously during the Term that:
(a) it is duly incorporated and validly existing under the laws of its place of incorporation;
(b) it has full power, authority and capacity to enter into and perform this Agreement and each SOW;
(c) execution and performance do not breach any law, regulation, contract, court order or constitutional document binding on it;
(d) it has all permissions, licences and registrations required to perform its obligations, including, in the case of Provider, any registration with the ICO under the Data Protection (Charges and Information) Regulations 2018; and
(e) it complies with all applicable anti-bribery, anti-tax-evasion, anti-money-laundering and sanctions laws, including the Bribery Act 2010, the Criminal Finances Act 2017 and the Proceeds of Crime Act 2002.

12.2 **Provider warranties.** Provider warrants additionally that:
(a) it will perform the Services with the reasonable skill and care to be expected of a competent professional providing services of the same type;
(b) Deliverables will, on Acceptance, conform to the Acceptance Criteria;
(c) Deliverables will not, when used as contemplated by the SOW, knowingly infringe any third-party Intellectual Property Right;
(d) Provider has, and will retain, the rights necessary to grant the IP rights granted under section 9;
(e) Provider has not been the subject of any unspent conviction within section 7 of the Bribery Act 2010 or under the Criminal Finances Act 2017 and is not aware of any matter that would reasonably be expected to lead to such a conviction;
(f) Deliverables, when delivered, will be free of malware (viruses, trojans, ransomware, logic bombs, time bombs and similar malicious code); and
(g) Provider's modern-slavery statement under section 54 of the Modern Slavery Act 2015, where the threshold is met, is current and published.

12.3 **Client warranties.** Client warrants that:
(a) Client materials provided to Provider, and Client's use of Deliverables as contemplated by the SOW, do not infringe any third-party right; and
(b) Client has the right to share with Provider all Personal Data and other information shared in connection with the Services.

12.4 **Disclaimer.** To the maximum extent permitted by law, and subject to the reasonableness test in sections 2 and 3 of the Unfair Contract Terms Act 1977 ("**UCTA**") and section 3 of the Misrepresentation Act 1967, the Parties exclude all warranties, conditions and other terms not expressly set out in this Agreement, including any implied terms as to satisfactory quality, fitness for purpose or non-infringement, save that nothing in this Agreement excludes or limits any term implied by section 13 of the Supply of Goods and Services Act 1982 (services to be performed with reasonable care and skill) where it cannot lawfully be excluded.

> **12-A. Client-favourable variant.** Provider gives an express warranty that Deliverables conform to the SOW for 12 months after Acceptance and that Provider will remediate non-conforming Deliverables at Provider's cost; Provider warrants compliance with all applicable laws (not just the major ones listed); Provider warrants that no malware-scanning issues will arise on a date later than the Effective Date for any defect originating in code Provider authored; the warranty disclaimer is narrow.

> **12-B. Provider-favourable variant.** Warranties are limited to those expressly set out and run for 90 days after Acceptance; remediation is Provider's sole obligation and Client's sole remedy for breach of warranty; everything else is excluded subject only to the UCTA carve-outs (death, personal injury, fraud, the section 13 SOGSA implied term where it cannot lawfully be excluded).

> **12-C. Market-standard variant.** Express warranties for six months after Acceptance; remediation as primary remedy; right to elect refund / re-perform / damages where remediation fails; UCTA carve-outs preserved; standard exclusions for satisfactory quality / fitness for purpose / non-infringement subject to express IP warranty in 12.2(c).

---

## 13. Indemnification  *— DUAL-PERSPECTIVE*

The first sentence is the floor: Provider indemnifies Client against IP-infringement claims arising out of Deliverables; Client indemnifies Provider against claims arising from Client materials or Client misuse of Deliverables; both indemnities are subject to the limitations in section 14 except where stated otherwise.

13.1 **Provider IP indemnity.** Provider will defend, indemnify and hold harmless Client from and against any third-party claim that a Deliverable, when used as contemplated by the SOW, infringes the third party's Intellectual Property Right enforceable in the United Kingdom or another jurisdiction expressly identified in the SOW, and any reasonable legal costs and damages or settlement amounts agreed by Provider. Provider's obligations under this clause are conditional on Client (a) giving prompt written notice of the claim, (b) giving Provider sole control of the defence and settlement (save that Provider may not settle on terms that admit liability, impose a restraint on Client or require a payment by Client without Client's consent, not to be unreasonably withheld), and (c) providing reasonable cooperation at Provider's cost.

13.2 **Mitigation.** If a claim under 13.1 is made or, in Provider's reasonable opinion, is likely to be made, Provider may at its option and cost (a) procure for Client the right to continue using the affected Deliverable, (b) modify the Deliverable so that it is non-infringing while remaining substantially equivalent in functionality, or (c) replace the Deliverable with a non-infringing equivalent. Where (a) to (c) are not commercially reasonable, Provider may terminate the affected SOW or the affected Deliverable's licence and refund the fees paid for the affected Deliverable in the 12 months before the claim, on a pro rata basis.

13.3 **IP-indemnity carve-outs.** Provider has no obligation under 13.1 to the extent the claim arises from: (a) Client materials or instructions; (b) modifications made by or for Client other than by Provider; (c) combination of the Deliverable with anything not supplied by Provider, where the infringement would not have occurred but for the combination; (d) use of the Deliverable other than as contemplated by the SOW; (e) Open-Source Components, in respect of which the upstream licence governs; or (f) Client's continued use of an allegedly infringing Deliverable after Provider has provided a non-infringing alternative under 13.2.

13.4 **Client indemnity.** Client will defend, indemnify and hold harmless Provider from and against any third-party claim arising from (a) Client materials, (b) Client's use of Deliverables other than as contemplated by the SOW, or (c) Client's breach of the data-protection or confidentiality obligations of this Agreement, in each case under the same procedural conditions as 13.1.

13.5 **Sole remedy.** The indemnities in this section state each Party's sole financial obligation in respect of third-party-IP claims and Client-materials claims respectively; this does not limit either Party's rights to injunctive relief.

> **13-A. Client-favourable variant.** Provider's IP indemnity is uncapped; covers any jurisdiction in which Client uses Deliverables in the ordinary course; mitigation options exclude termination unless Client consents; carve-out (e) (Open-Source) is narrowed to copyleft components only.

> **13-B. Provider-favourable variant.** Provider's IP indemnity is capped at the fees paid for the affected Deliverable in the 12 months before the claim; covers only the United Kingdom; mitigation options include termination with pro-rata refund as a self-help remedy.

> **13-C. Market-standard variant.** Provider's IP indemnity capped at the higher of (i) fees paid in the 12 months before the claim and (ii) {{Liability Cap Floor}}; covers United Kingdom plus any jurisdiction in the SOW; mitigation per 13.2; carve-outs as 13.3.

---

## 14. Limitation of liability  *— DUAL-PERSPECTIVE*

The first sentence is the floor: subject to the carve-outs in 14.1 (which are required by law and cannot be excluded), each Party's total aggregate liability arising under or in connection with this Agreement is capped at {{Liability Cap Multiplier}} times the fees paid or payable to Provider under the affected SOW in the 12 months before the cause of action arose, with a floor of {{Liability Cap Floor}}; neither Party is liable for indirect, special, consequential or punitive losses, or for loss of profits, revenue, business, goodwill, reputation, anticipated savings or data, in each case to the extent excluded by law.

14.1 **Carve-outs that cannot be excluded.** Nothing in this Agreement excludes or limits liability for:
(a) death or personal injury caused by negligence (UCTA section 2(1));
(b) fraud or fraudulent misrepresentation;
(c) any liability that cannot lawfully be excluded or limited (including under section 12 of the Sale of Goods Act 1979 or section 2 of the Supply of Goods and Services Act 1982 to the extent those terms are implied);
(d) wilful default or breach of section 10 (Confidentiality) involving misuse of trade secrets;
(e) Provider's payment obligations and Client's payment obligations to each other; and
(f) liability under the indemnities in section 13 to the extent expressly stated to be uncapped.

14.2 **UCTA reasonableness.** The Parties confirm that the limitations and exclusions in this section have been agreed having regard to: (a) the Parties' relative bargaining positions, including their respective ability to obtain alternative providers; (b) the price agreed and the availability of insurance; (c) the customary practice in their industries; and (d) the express opportunity each Party has had to take legal advice. The Parties consider the provisions to satisfy the requirement of reasonableness under sections 2 and 3 UCTA and section 3 of the Misrepresentation Act 1967.

14.3 **Misrepresentation Act 1967.** Each Party's liability for misrepresentation that induces it to enter this Agreement (other than fraudulent misrepresentation) is governed by the limits in this section, subject to the section 3 reasonableness test of the Misrepresentation Act 1967.

14.4 **Aggregation.** All claims by either Party under or in connection with the Agreement, however they arise (including in contract, tort, statute or restitution), are aggregated for the purposes of the cap.

14.5 **Equitable remedies.** Nothing in this section limits the right of either Party to seek injunctive or equitable relief in respect of breach of section 9 (IP), section 10 (Confidentiality) or section 11 (Data protection).

> **14-A. Client-favourable variant.** Cap is the higher of (i) 2× fees paid under the affected SOW in the prior 12 months and (ii) £5m; cap doubles for breaches of section 11 (Data protection); IP indemnity uncapped; "consequential loss" exclusion narrowed to losses neither Party could reasonably have foreseen on the Effective Date; loss of data is recoverable to the extent attributable to Provider's failure to take reasonable backups under section 11.5.

> **14-B. Provider-favourable variant.** Cap is the lower of (i) 1× fees paid under the affected SOW in the prior 12 months and (ii) £1m; consequential loss exclusion broad; loss of data, profit, revenue, savings and goodwill all expressly excluded; cap applies even to data-protection claims save for the regulator-fine carve-out under 14.6.

> **14-C. Market-standard variant.** Cap is the higher of (i) 1× fees paid under the affected SOW in the prior 12 months and (ii) {{Liability Cap Floor}}; data-protection cap at 2× the general cap; IP indemnity capped at the same level as data-protection cap; consequential loss excluded subject to UCTA reasonableness.

14.6 **Regulator-imposed sanctions.** Where a regulator (including the ICO) imposes a fine or sanction on Client because of Provider's breach, the resulting fine is recoverable as direct loss to the extent permitted by law and is subject to the cap as enhanced for data-protection claims (where applicable in the chosen variant).

---

## 15. Insurance

This section sets the insurance floor; the SOW may raise but not lower it. Cover is to be placed with insurers of good standing rated A- or better by AM Best, S&P or Moody's, or otherwise an FCA-authorised insurer or member of the Association of British Insurers.

15.1 **Provider insurance.** Provider maintains, at its own cost, during the Term and for at least six years after the end of the Term:
(a) Professional Indemnity insurance with a minimum limit of {{PI Insurance Minimum}} per claim and in the aggregate (typical range £2m–£10m, set by reference to the SOW value and risk profile);
(b) Public Liability insurance with a minimum limit of {{PL Insurance Minimum}} per occurrence (typical range £5m–£10m);
(c) Employers' Liability insurance with a minimum limit of {{WC Insurance Minimum}} (statutory minimum £5m under the Employers' Liability (Compulsory Insurance) Act 1969);
(d) Cyber and Data Protection insurance with a minimum limit of {{Cyber Insurance Minimum}} per claim, including ICO-fine cover (where insurable), forensic costs, breach-notification costs and third-party privacy liability (typical range £1m–£5m); and
(e) where directors are personally exposed by the engagement, Directors' & Officers' insurance at a level appropriate to the risk.

15.2 **Evidence of cover.** Provider provides Client with broker certificates of cover on request, no more than once per year save where Client has reasonable cause to suspect cover has lapsed or is inadequate.

15.3 **Notice of changes.** Provider notifies Client without undue delay of any cancellation, non-renewal or material reduction of cover.

15.4 **Subrogation.** Provider procures that its insurers waive subrogation rights against Client in respect of claims arising under this Agreement, to the extent obtainable on commercially reasonable terms.

15.5 **Run-off cover.** Where Provider's insurance is written on a claims-made basis, Provider procures run-off cover for the periods in 15.1 sufficient to cover claims first made during run-off but referable to acts during the Term.

15.6 **Insurance does not increase liability.** The existence or limit of any policy does not increase the liability cap in section 14.

---

## 16. Term and termination  *— DUAL-PERSPECTIVE*

The first sentence is the floor: this Agreement begins on the Effective Date and runs for the Initial Term, automatically renewing for successive Renewal Terms unless either Party gives {{Termination Notice Window}} days' written notice before the end of the then-current Term, save that any SOW with a fixed term continues unaffected by the expiry of this Agreement until the SOW itself ends.

16.1 **Termination of the Agreement.**
(a) **For convenience.** Either Party may terminate this Agreement for convenience on {{Termination Notice Window}} days' prior written notice, provided that all SOWs in flight survive their stated end dates unless terminated independently.
(b) **For material breach.** Either Party may terminate this Agreement for material breach if the other Party fails to cure the breach within {{Cure Period}} days of written notice identifying the breach with reasonable particularity, save that no cure period is required for breaches incapable of cure (including breach of section 10 involving misuse of trade secrets).
(c) **For Insolvency Event.** Either Party may terminate immediately on written notice if the other suffers an Insolvency Event, subject to any moratorium under Part A1 of the Insolvency Act 1986.
(d) **For repudiatory breach.** Common-law rights of termination for repudiatory breach are preserved; nothing in this section excludes or limits the right of an innocent Party to accept a repudiatory breach as terminating the Agreement.
(e) **For change of control.** Either Party may terminate on 30 days' written notice if the other Party undergoes a change of control to an entity that competes with the terminating Party in a material way.

16.2 **Termination of a SOW.** A SOW may be terminated independently of this Agreement on the same grounds as 16.1(a)–(d); termination of one SOW does not affect any other SOW. *OPTIONAL — only if Construction Operations apply.* Where {{Construction Operations Toggle}} is "Yes", Provider may suspend or terminate the affected SOW for non-payment under section 112 HGCRA on the giving of seven days' notice, the right of suspension being exercisable in respect of the whole or any part of the obligations affected.

16.3 **Effect of termination.** On termination of this Agreement or any SOW:
(a) Client pays Provider for all Services properly performed up to the effective date of termination, including any non-cancellable third-party costs already committed at Client's authorisation;
(b) Provider delivers all Foreground IP and work-in-progress for which Client has paid (or for which Client agrees to pay), in editable form;
(c) each Party returns or destroys the other's Confidential Information per section 10.6;
(d) the data-protection provisions of section 11 continue to apply for so long as Provider holds Client Personal Data;
(e) any obligation that by its nature should survive (sections 9, 10, 11, 13, 14, 15 (run-off), 16.3, 17, 18 and 19) survives.

16.4 **Force majeure.** Neither Party is in breach of this Agreement to the extent its failure to perform is caused by an event beyond its reasonable control, including act of God, war, civil disorder, terrorism, pandemic or epidemic, government action (including lockdowns and quarantines), failure of national infrastructure (power, telecommunications, transport), labour dispute (other than disputes affecting only that Party's own workforce) or sanction imposed by a competent authority. The affected Party gives prompt written notice with details and cure plan; the obligations affected are suspended for the duration of the event; either Party may terminate the affected SOW (or, where the event affects all SOWs, this Agreement) on written notice if the event continues for more than 60 consecutive days.

> **16-A. Client-favourable variant.** Termination for convenience on 30 days' notice without further fee beyond Services properly performed; Provider may not invoke section 112 HGCRA suspension where the unpaid amount is the subject of a good-faith dispute under section 5.3; change-of-control termination by Client only; force-majeure termination right by Client after 30 days continuing event.

> **16-B. Provider-favourable variant.** Termination for convenience by Client requires the higher of {{Termination Notice Window}} days or the time remaining on the affected SOW, plus an early-termination charge equal to 30% of the unbilled SOW value; Provider may suspend on five Business Days' written notice for any undisputed amount unpaid for more than 15 days; force-majeure right exercisable by either Party after 60 days; non-cancellable third-party committed costs payable in full on termination for any cause.

> **16-C. Market-standard variant.** Termination for convenience on 60 days' notice; pay-for-services-rendered plus pro-rata fixed fees; Provider may suspend after 10 Business Days' continuing default; force-majeure mutual termination right after 60 days.

---

## 17. Transition assistance and wind-down  *— DUAL-PERSPECTIVE*

The first sentence is the floor: on termination or expiry of this Agreement or any SOW for any cause (including for cause), Provider provides Client with reasonable transition assistance to allow Client or its replacement provider to take over the Services without undue disruption.

17.1 **Transition period.** The transition period is up to 90 days from the effective date of termination (or such longer period as the Parties agree in writing), during which Provider performs the transition services on a T&M basis at the SOW rate card (or as varied by the SOW). The transition obligation is not optional: it applies even where Client terminates for Provider's material breach, save that in those circumstances Provider's fees for the transition are reduced to the rate card discount Client would have enjoyed had the breach not occurred.

17.2 **Transition services.** On Client's reasonable written request, transition services include: (a) handover of documentation, source code, designs, configurations and credentials necessary to operate or develop the Deliverables; (b) reasonable knowledge-transfer sessions with Client or its replacement provider; (c) cooperation with the replacement provider; (d) deletion or return of Personal Data per section 11.2(g); and (e) such other reasonable assistance as the SOW or Client specifies in writing.

17.3 **Records and exit data.** Provider returns Client data in a structured, commonly used and machine-readable format. Where the data sits in a Provider-proprietary format, Provider provides reasonable assistance to translate or export it. Provider may charge time at the SOW rate card for translation work that exceeds five Business Days of effort.

17.4 **Termination for Provider's breach.** Where the termination is for Provider's material breach, Client may set off any reasonable transition cost (including the rate-card cost of the transition services and any additional costs of the replacement provider attributable to delay caused by Provider) against amounts owed to Provider, subject to section 14 cap.

> **17-A. Client-favourable variant.** Transition period extends to 180 days at Client's election; transition services are at no charge for breaches caused by Provider; Provider's documentation, escrowed source and decryption keys are released to Client immediately on any termination for cause; reasonable cooperation includes parallel running for up to 60 days at SOW rate card.

> **17-B. Provider-favourable variant.** Transition period 60 days; Provider's hourly rates apply unaltered; Client must prepay the estimated transition cost; Provider's cooperation is conditional on Client being current on all undisputed invoices.

> **17-C. Market-standard variant.** Transition period 90 days; rate-card pricing; modest pre-payment for periods longer than 30 days; cooperation conditional on payment-current status, save for the cost-discount where Client terminates for Provider's breach.

---

## 18. Dispute resolution and governing law

This section sets the law that governs the Agreement and the forum where disputes are resolved. The Parties prefer engaged negotiation and structured escalation before litigation; nothing in this section delays an application for urgent equitable relief.

18.1 **Governing law.** This Agreement, and any non-contractual obligations arising out of or in connection with it, are governed by the laws of England and Wales.

18.2 **Negotiation and escalation.** Before commencing court proceedings or arbitration in respect of any dispute (other than an application for interim or injunctive relief), the Parties' contract managers will negotiate in good faith for at least 15 Business Days. If unresolved, the dispute is escalated to a senior officer of each Party (typically director-level or above) for a further 15 Business Days. If still unresolved, either Party may invoke the chosen forum.

18.3 **Forum — courts of England.** Where {{LCIA Toggle}} is "Courts of England", the Parties submit to the exclusive jurisdiction of the courts of England in respect of all disputes, save that either Party may apply to any competent court for interim or protective relief.

18.4 **Forum — LCIA arbitration.** Where {{LCIA Toggle}} is "LCIA Arbitration":
(a) any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, will be referred to and finally resolved by arbitration under the LCIA Rules in force at the time of the reference;
(b) the seat of arbitration is London;
(c) the language of the arbitration is English;
(d) the number of arbitrators is one for disputes where the amount in controversy is below £1m and three otherwise;
(e) the Arbitration Act 1996 applies; and
(f) the Parties expressly preserve the right to seek interim or injunctive relief in any court of competent jurisdiction notwithstanding the agreement to arbitrate.

18.5 **No jury trial.** The civil-jury point is not material: the courts of England do not generally try civil claims of this kind by jury. The Parties acknowledge that no jury-trial waiver is required as a matter of English law.

18.6 **Costs.** In court proceedings, the costs follow the event subject to the court's discretion. In LCIA arbitration, the tribunal allocates costs in accordance with the LCIA Rules.

18.7 **Limitation periods.** Nothing in this Agreement is intended to vary the limitation periods under the Limitation Act 1980; for the avoidance of doubt, claims under a SOW executed as a deed are subject to the 12-year limitation period under section 8 Limitation Act 1980, and other contractual claims to the six-year period under section 5.

18.8 **Injunctive relief.** Each Party may seek interim or final injunctive relief in any court of competent jurisdiction in respect of breach (or threatened breach) of section 9 (IP), section 10 (Confidentiality) or section 11 (Data protection), without first exhausting the escalation in 18.2.

---

## 19. General provisions and signature block

This section gathers the boilerplate that is necessary but did not fit anywhere else.

19.1 **Notices.** Notices under this Agreement are given in writing to the address listed at the head of the Agreement (with email copy to the relevant Notice Email) and are deemed delivered (a) on the second Business Day after posting by recorded delivery within the United Kingdom or (b) on the day of receipt confirmation for email. Either Party may update its notice address by notice given under this section.

19.2 **Entire agreement.** This Agreement, together with all SOWs, Order Forms and annexes, constitutes the entire agreement between the Parties on its subject matter and supersedes all prior agreements, representations and understandings (other than (a) any non-disclosure agreement, the surviving terms of which roll into section 10, and (b) any signed master purchasing or framework arrangement that expressly survives). For the avoidance of doubt, nothing in this clause excludes liability for fraudulent misrepresentation. Any non-fraudulent representation made by a Party that is not set out in this Agreement is excluded subject to the section 3 reasonableness test of the Misrepresentation Act 1967.

19.3 **Amendments.** Amendments to this Agreement (other than amendments to a SOW, which follow section 6) require a written instrument signed by an authorised signatory of each Party.

19.4 **Severance.** If any provision of this Agreement is or becomes illegal, invalid or unenforceable, the remainder of the Agreement remains in force; the Parties will substitute the offending provision with a valid and enforceable provision that achieves, so far as possible, the same commercial result.

19.5 **No waiver.** No failure or delay to exercise a right is a waiver of that right; a waiver is effective only if in writing and signed by the waiving Party.

19.6 **Assignment.** Neither Party may assign or novate this Agreement without the other's prior written consent, save that either Party may assign or novate without consent to a successor in connection with a merger, reorganisation or sale of substantially all the assets of the business to which the Agreement relates, on written notice. *OPTIONAL — only if {{Deed Execution Required}} is "Yes".* Any assignment of IP under section 9 that requires execution as a deed (for example, to satisfy section 44 of the Companies Act 2006) is to be executed as a deed substantially in the form attached to the relevant SOW.

19.7 **Third-party rights.** A person who is not a party to this Agreement has no right under the Contracts (Rights of Third Parties) Act 1999 to enforce any of its terms. The Parties may rescind or vary this Agreement without the consent of any third party.

19.8 **Anti-bribery (Bribery Act 2010).** Each Party warrants that it has in place adequate procedures designed to prevent the giving or receiving of bribes within the meaning of section 7 of the Bribery Act 2010 (the "**adequate procedures**" defence to corporate failure-to-prevent-bribery). Each Party will not, in connection with this Agreement, engage in any conduct that would give rise to liability for the other under the Bribery Act 2010 or analogous legislation. Each Party will support the other's investigation of any reasonable concern of bribery on reasonable notice and during business hours.

19.9 **Anti-tax-evasion (Criminal Finances Act 2017).** Each Party warrants that it has in place reasonable procedures to prevent the facilitation of tax evasion within the meaning of sections 45 and 46 of the Criminal Finances Act 2017. Provider's training and supervision of its Personnel and Subcontractors include appropriate measures to support that defence.

19.10 **Modern slavery (Modern Slavery Act 2015).** Where {{Modern Slavery Threshold Met}} is "Yes", each Party publishes an annual statement under section 54 of the Modern Slavery Act 2015 and provides a link to the current statement on request. Each Party requires its Subcontractors and suppliers performing material parts of the Services to comply with equivalent modern-slavery obligations and conducts proportionate risk assessment of its own and its Subcontractors' supply chains.

19.11 **Sanctions and export control.** Each Party complies with applicable economic and trade sanctions and export-control laws, including the United Kingdom's regimes administered by HM Treasury (OFSI), the Department for Business and Trade (Export Control Joint Unit) and where applicable equivalent regimes of the European Union, the United States and the United Nations. Neither Party will use the Services for any purpose prohibited by those regimes.

19.12 **Public-sector flow-downs.** *OPTIONAL — only if {{Public Sector Toggle}} is "Yes".* Where Client is a contracting authority within the meaning of the Procurement Act 2023 [VERIFY commencement of the Procurement Act 2023 and any transitional provisions], Provider supports Client's compliance with that Act and with the Public Contracts Regulations 2015 (to the extent they continue to apply on a transitional basis), including by providing data necessary for the Procurement Act 2023's transparency notices and supplier-conduct obligations. Provider will cooperate with Client's obligations under the Freedom of Information Act 2000 and the Public Services Network ("**PSN**") code of compliance where applicable.

19.13 **DMCCA 2024.** *OPTIONAL — only if {{Subscription Reminder Toggle}} is "Yes".* Where Provider supplies subscription services to a small or medium-sized Client and the Digital Markets, Competition and Consumers Act 2024 ("**DMCCA**") subscription regime applies, Provider supports Client's reminder-notice and cancellation obligations under Part 4 DMCCA [VERIFY phased commencement of Part 4 DMCCA].

19.14 **Counterparts and electronic execution.** This Agreement may be executed in any number of counterparts. The Parties acknowledge the validity of electronic signatures under section 7 of the Electronic Communications Act 2000 and the retained eIDAS framework [VERIFY post-REUL retention status]. Each counterpart, when executed and delivered, is an original; all counterparts together constitute one Agreement.

19.15 **No partnership or agency.** Nothing in this Agreement creates a partnership, joint venture, employment or fiduciary relationship between the Parties.

19.16 **Costs.** Each Party bears its own costs of preparing, negotiating and entering into this Agreement.

19.17 **Set-off.** Save as expressly set out in this Agreement, neither Party may set off any liability of the other against amounts owed to the other.

19.18 **Conflicts of interest.** Provider will declare to Client, before commencing any SOW, any actual or potential conflict of interest and will follow Client's reasonable instructions on managing or avoiding the conflict.

19.19 **Cooperation.** The Parties cooperate in good faith on the matters described in this Agreement, including (but not limited to) regulator-driven investigations under section 11.

19.20 **Signature block.**

Executed by the Parties on the dates below by their authorised signatories.

For and on behalf of **{{Provider Legal Name}}** (company number {{Provider Companies House Number}}):

Signature: ___________________________________________
Name: {{Provider Signatory Name}}
Title: {{Provider Signatory Title}}
Date: ____________________

For and on behalf of **{{Client Legal Name}}** (company number {{Client Companies House Number}}):

Signature: ___________________________________________
Name: {{Client Signatory Name}}
Title: {{Client Signatory Title}}
Date: ____________________

*OPTIONAL — only if {{Deed Execution Required}} is "Yes".* If executed as a deed, each Party's signature must be witnessed (in the case of an individual signing) or executed in accordance with section 44 of the Companies Act 2006 (in the case of a company), as recorded on a separate deed of execution attached to the relevant SOW.

---

## Annex A — Statement of Work template

This Annex A is a short-form SOW template for use under this Agreement; for longer or more sophisticated engagements, use the companion `legalcode-sow` pack, which carries acceptance, milestone, change-control and pricing detail in modular form.

**Statement of Work No. [•]**, dated [•], under the {{MSA Title}} between {{Provider Legal Name}} and {{Client Legal Name}} dated {{MSA Effective Date}}.

A.1 **Engagement summary.** [Brief description of the Services and outcomes.]

A.2 **Services and Deliverables.** [Itemised list of Services and Deliverables, with milestones and acceptance criteria. Cross-reference Annex C where relevant.]

A.3 **Fee model and pricing.** [Fixed-fee / T&M / capped T&M / milestone-based / retainer, with a rate card if T&M.]

A.4 **Term.** Start date: [•]. End date or condition for end: [•].

A.5 **Key Personnel and IR35 Status.** Named key personnel (with role and status under {{IR35 Status}} for the engagement); where IR35 applies, attach the SDS issued by {{SDS Issuer}}.

A.6 **Subcontractors.** Pre-approved subcontractors are those in Annex B; any others require Client's specific written consent.

A.7 **Client-furnished materials and dependencies.** [List of materials, environments, accesses, decisions and the dates they are due.]

A.8 **Acceptance criteria.** [Specific or default to Annex C.]

A.9 **Construction Operations toggle.** {{Construction Operations Toggle}} — if "Yes", the payment provisions of HGCRA apply to this SOW.

A.10 **IP allocation.** Default per section 9; any deviation in IP ownership or licence is set out here.

A.11 **Data protection roles.** Provider acts as [processor / controller / joint controller] for the Personal Data described in this SOW.

A.12 **Restricted Transfers.** Where applicable, the IDTA / Addendum is incorporated by reference; the TRA is at [•].

A.13 **Variations from the Agreement.** [Identify any clause of the Agreement that this SOW varies, with the agreed substitute language.]

A.14 **Signatures.** As per the signature block of the Agreement.

---

## Annex B — Approved subcontractors and key personnel

This Annex lists the Subcontractors and key Personnel pre-approved as at the Effective Date; updates are made by notice under section 7.10.

| Subcontractor / Person | Role | Location | IR35 status (if individual) | Right-to-work check date |
|------------------------|------|----------|-----------------------------|---------------------------|
| [•]                    | [•]  | [•]      | [•]                         | [•]                       |
| [•]                    | [•]  | [•]      | [•]                         | [•]                       |

---

## Annex C — Service standards and acceptance criteria framework

This Annex sets the baseline acceptance criteria where the SOW does not specify them. The Parties may vary by SOW.

C.1 **Functional fit.** Deliverables substantially conform to the functional and non-functional requirements expressly recorded in the SOW.

C.2 **Quality.** Deliverables are produced to the standard of a competent professional providing services of the same type and are free of material defects.

C.3 **Documentation.** Deliverables are accompanied by documentation reasonably sufficient for an experienced professional in the field to operate, maintain and evolve the Deliverable.

C.4 **Security.** Deliverables and the development environment used to produce them comply with section 11.5 and any Cyber Essentials, NIS or operational-resilience overlay applicable under section 11.6.

C.5 **Open-Source compliance.** Open-Source Components are licensed in accordance with section 9.4 and are listed in the SBOM accompanying the Deliverable.

C.6 **Accessibility.** Where the Deliverable is a customer-facing digital service, it conforms to WCAG 2.2 AA or the equivalent standard required by Client policy.

C.7 **Modern-slavery and ethical-sourcing.** Materials used in the Deliverable are sourced consistently with the modern-slavery commitments in section 19.10.

C.8 **Acceptance review.** Client conducts the acceptance review with reasonable diligence within the Acceptance Period; Client's failure to conduct the review does not stop the Deemed Acceptance Window from running.

---

## Appendix — Merge fields (reference)

In addition to the common merge fields documented in the pack README, the UK variant uses the merge fields listed at the head of this document. Search-and-replace each before signing; do not leave any `{{Field Name}}` placeholder in a signed document.

## Appendix — Authoritative references

- Late Payment of Commercial Debts (Interest) Act 1998 — https://www.legislation.gov.uk/ukpga/1998/20 — OGL
- Late Payment of Commercial Debts Regulations 2002 (and 2013 amendment) — https://www.legislation.gov.uk/uksi/2002/1674 — OGL
- Housing Grants, Construction and Regeneration Act 1996 (as amended by LDEDCA 2009) — https://www.legislation.gov.uk/ukpga/1996/53 — OGL
- Income Tax (Earnings and Pensions) Act 2003, Pt 2 Chs 8 and 10 — https://www.legislation.gov.uk/ukpga/2003/1 — OGL
- HMRC ESM (Employment Status Manual) and CEST tool — https://www.gov.uk/guidance/check-employment-status-for-tax — OGL
- Conduct of Employment Agencies and Employment Businesses Regulations 2003 — https://www.legislation.gov.uk/uksi/2003/3319 — OGL
- Employment Rights Act 1996 (s.230 worker definition) — https://www.legislation.gov.uk/ukpga/1996/18 — OGL
- Equality Act 2010 — https://www.legislation.gov.uk/ukpga/2010/15 — OGL
- Pensions Act 2008 — https://www.legislation.gov.uk/ukpga/2008/30 — OGL
- Immigration Act 2016 — https://www.legislation.gov.uk/ukpga/2016/19 — OGL
- Copyright, Designs and Patents Act 1988, esp. ss.11, 77–89, 90–91 — https://www.legislation.gov.uk/ukpga/1988/48 — OGL
- Copyright and Rights in Databases Regulations 1997 — https://www.legislation.gov.uk/uksi/1997/3032 — OGL
- Unfair Contract Terms Act 1977 — https://www.legislation.gov.uk/ukpga/1977/50 — OGL
- Misrepresentation Act 1967 — https://www.legislation.gov.uk/ukpga/1967/7 — OGL
- Sale of Goods Act 1979 / Supply of Goods and Services Act 1982 — https://www.legislation.gov.uk/ukpga/1979/54 — OGL
- UK GDPR + Data Protection Act 2018 + Data (Use and Access) Act 2025 — https://www.legislation.gov.uk/ — OGL
- Privacy and Electronic Communications (EC Directive) Regulations 2003 — https://www.legislation.gov.uk/uksi/2003/2426 — OGL
- ICO International Data Transfer Agreement and Addendum — https://ico.org.uk/ — OGL
- Network and Information Systems Regulations 2018 — https://www.legislation.gov.uk/uksi/2018/506 — OGL
- NCSC Cyber Assessment Framework — https://www.ncsc.gov.uk/ — OGL
- Cyber Essentials and Cyber Essentials Plus — https://www.ncsc.gov.uk/cyberessentials — OGL
- FCA SYSC 15A and PRA SS1/21 (Operational Resilience) — https://www.handbook.fca.org.uk/ — OGL
- Modern Slavery Act 2015, s.54 — https://www.legislation.gov.uk/ukpga/2015/30 — OGL
- Bribery Act 2010 (esp. s.7 corporate offence and adequate-procedures defence) — https://www.legislation.gov.uk/ukpga/2010/23 — OGL
- Criminal Finances Act 2017 (ss.45–46) — https://www.legislation.gov.uk/ukpga/2017/22 — OGL
- Companies Act 2006 (esp. s.44 execution) — https://www.legislation.gov.uk/ukpga/2006/46 — OGL
- Procurement Act 2023 — https://www.legislation.gov.uk/ukpga/2023/54 — OGL
- Digital Markets, Competition and Consumers Act 2024 — https://www.legislation.gov.uk/ukpga/2024/13 — OGL
- Electronic Communications Act 2000, s.7 — https://www.legislation.gov.uk/ukpga/2000/7 — OGL
- Limitation Act 1980 — https://www.legislation.gov.uk/ukpga/1980/58 — OGL
- Insolvency Act 1986 — https://www.legislation.gov.uk/ukpga/1986/45 — OGL
- Trade Secrets (Enforcement, etc.) Regulations 2018 — https://www.legislation.gov.uk/uksi/2018/597 — OGL
- Employers' Liability (Compulsory Insurance) Act 1969 — https://www.legislation.gov.uk/ukpga/1969/57 — OGL
- LCIA Arbitration Rules — https://www.lcia.org/ — referenced under licence to cite
- Bonterms Professional Services Agreement v1.2 — https://bonterms.com/forms/professional-services-agreement/ — CC0
- Common Paper Standard Services Agreement — https://commonpaper.com/standards/services-agreement/ — CC-BY-4.0
- Common Paper SOW — https://commonpaper.com/standards/services-agreement/ — CC-BY-4.0

## Appendix — Not legal advice

This template is a clean-room drafting starting point released under MIT. It is not legal advice and is not a substitute for legal advice. The Parties should engage qualified counsel admitted in England and Wales (or, for cross-border engagements, in each relevant jurisdiction) before signing. Time-sensitive items flagged with [VERIFY] above must be checked against current law and current data at the time of signing. The drafter takes no responsibility for errors, omissions or outcomes arising from the use of this template; users adopt and adapt at their own risk.
