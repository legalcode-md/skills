---
title: Cloud Service Agreement (Jurisdiction-Neutral Baseline)
jurisdictions: [global]
posture: dual-perspective (customer-favorable / vendor-favorable / market-standard)
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

# Cloud Service Agreement

**This Cloud Service Agreement (the "Agreement" or "CSA") is entered into between {{Vendor Legal Name}}, a {{Vendor Entity Type}} organized under the laws of {{Vendor Jurisdiction}} with its principal place of business at {{Vendor Address}} ("Vendor"), and {{Customer Legal Name}}, a {{Customer Entity Type}} organized under the laws of {{Customer Jurisdiction}} with its principal place of business at {{Customer Address}} ("Customer"), each a "Party" and together the "Parties," effective {{Effective Date}}.**

---

## 1. Plain-language summary

*Plain-language: This section is a non-binding orientation for readers; the binding terms appear in Sections 2 through 18 and any executed Order Form.*

This Agreement is the master contract that governs Customer's subscription to Vendor's cloud-delivered software (the "Cloud Service"). It is intentionally modular. The terms in this CSA cover topics that rarely change between deals — definitions, confidentiality, payment mechanics, security baselines, liability, and governing law. The commercial details of each subscription — products, quantities, term, fees, discounts, and any deal-specific edits — are written separately on each Order Form.

If a customer is reviewing this document for the first time, the practical reading order is: this summary, then Section 2 (how the documents fit together), then Section 9 (how the contract starts, renews, and ends), then Section 16 (warranties and liability), then any Order Form specific to that customer.

A subscription is a commitment to use the Cloud Service for a fixed Initial Term, normally with automatic renewal. The fee structure is paid in advance unless the Order Form specifies otherwise. Customer keeps ownership of the data it loads into the Cloud Service. Vendor keeps ownership of the Cloud Service itself and any underlying technology. Several common protections that consumers expect — control over personal data, return of data on exit, and a clear notice path for breaches — are preserved here, scaled to a business-to-business deal.

Renewal and cancellation work as follows: unless the Order Form changes the default, the subscription auto-renews for successive Renewal Terms equal to the Initial Term, and either Party may stop the renewal by giving notice at least {{Non-Renewal Notice Window}} days before the renewal date. Termination for material breach is available on a {{Cure Period}}-day cure notice. The data-export window after termination is set in Section 6.4.

This summary does not modify the operative provisions. Where the summary and the operative text differ, the operative text controls.

---

## 2. Agreement structure (Master Agreement + Order Forms)

*Plain-language: This CSA sits at the top; specific subscriptions live on Order Forms; conflicts are resolved by an explicit precedence rule.*

**2.1 Master Agreement.** This CSA is the master agreement between the Parties for the Cloud Service. It applies to every Order Form that references it, whether signed today or in the future, and to every Statement of Work, Exhibit, and addendum incorporated by reference.

**2.2 Order Forms.** Each subscription, free tier, pilot, or trial is captured on a separate Order Form, in the form of Exhibit A or in any other written form signed (including electronically) by both Parties. Each Order Form is a separate contract for the products and quantities listed on it, but is governed by this CSA. An Order Form takes effect on the later of the date signed by the second Party or the start date written on the face of the Order Form.

**2.3 Order of precedence.** Unless an Order Form expressly states that a specific term overrides this CSA, this CSA controls if there is a conflict. The order of precedence is, from highest to lowest: (i) the Order Form, but only for terms that the Order Form expressly designates as overriding this CSA and only as to the subscription on that Order Form; (ii) the Data Processing Agreement at Exhibit C and any signed amendment to it; (iii) this CSA; (iv) any Acceptable Use Policy or Service Level Agreement referenced in the Order Form; and (v) the Documentation.

**2.4 Free, pilot, and trial Order Forms.** An Order Form may identify a subscription as free, pilot, evaluation, beta, or trial. Section 12 governs those subscriptions. To the extent Section 12 conflicts with another Section, Section 12 controls but only for the subscription so identified.

**2.5 No purchase orders or click-throughs override.** Pre-printed terms on Customer purchase orders, vendor onboarding portals, click-through wraps, or shrink-wraps have no legal effect on this CSA, even if signed or accepted by an authorized signatory, unless the document expressly references this CSA by title and date and is signed by both Parties.

**2.6 Affiliate Order Forms.** A Customer Affiliate may sign an Order Form directly under this CSA. When it does, the Affiliate is the "Customer" for that Order Form, the Affiliate is solely responsible for that Order Form's obligations, and Customer is not jointly liable unless Customer expressly guarantees the obligation in writing.

---

## 3. Definitions

*Plain-language: Defined terms used throughout the CSA. Capitalized terms have the meanings given in this Section, in the Order Form, or where defined elsewhere in this CSA.*

**3.1 "Affiliate"** means, with respect to a Party, any entity that directly or indirectly controls, is controlled by, or is under common control with that Party, where "control" means ownership of more than fifty percent (50%) of the voting equity or the power to direct management and policies.

**3.2 "AI Output"** means any text, code, image, audio, video, embedding, classification, decision, recommendation, or other content generated by the Cloud Service in response to Customer Inputs, including any automated derivative of Customer Data produced by a machine-learning component of the Cloud Service.

**3.3 "Authorized User"** means an individual employee, contractor, or agent of Customer or its authorized Affiliates whom Customer permits to access the Cloud Service under credentials provisioned for that individual.

**3.4 "Cloud Service"** means the cloud-delivered software-as-a-service product or products identified in an Order Form, including any updates, upgrades, patches, hotfixes, or new releases that Vendor makes generally available during the term and any associated Documentation.

**3.5 "Confidential Information"** has the meaning given in Section 7.

**3.6 "Customer Data"** means electronic data, content, files, records, and personal data that Customer or any Authorized User submits to, stores in, or transmits through the Cloud Service. Customer Data does not include Vendor's operational or telemetry data about the Cloud Service or aggregated, irreversibly de-identified data described in Section 15.2.

**3.7 "Customer Inputs"** means prompts, queries, instructions, files, and parameters that Customer or an Authorized User submits to the Cloud Service to obtain AI Output.

**3.8 "Customer Materials"** means any tools, templates, configurations, content, or other materials that Customer provides or makes available to Vendor in connection with this Agreement, other than Customer Data.

**3.9 "Documentation"** means the user-facing technical documentation for the Cloud Service that Vendor publishes at {{Documentation URL}} or otherwise delivers to Customer, as updated from time to time.

**3.10 "Effective Date"** means the date set forth in the preamble of this CSA or, if none, the date of the first executed Order Form.

**3.11 "Fees"** means the subscription fees, usage fees, professional-service fees, and any other charges set forth in an Order Form.

**3.12 "Initial Term"** means the initial subscription period for an Order Form as set forth on the face of that Order Form.

**3.13 "Order Form"** means a written ordering document signed by both Parties that references this CSA and identifies one or more subscriptions, in substantially the form of Exhibit A.

**3.14 "Renewal Term"** means each successive subscription period that begins after the Initial Term, as described in Section 9.

**3.15 "Service Level Agreement" or "SLA"** means the service-level commitments set forth in Exhibit B or the document referenced in an Order Form as the applicable SLA.

**3.16 "Subprocessor"** means a third party that processes Customer personal data on Vendor's behalf, as described in Exhibit C.

**3.17 "Third-Party Services"** means software, services, content, or systems provided by a party other than Vendor that Customer chooses to integrate with, or use through, the Cloud Service.

**3.18 "Trials"** means free, pilot, evaluation, or beta subscriptions identified as such on an Order Form, as governed by Section 12.

**3.19 "Vendor Materials"** means the Cloud Service, the Documentation, and any tools, models, software, scripts, configuration, know-how, and other materials Vendor uses to provide or improve the Cloud Service, including all intellectual property rights therein.

---

## 4. Use of the Service

*Plain-language: Vendor grants Customer a limited subscription right to use the Cloud Service for its internal business purposes during the term, subject to the restrictions in Section 5 and the volume scope in the Order Form.*

**4.1 Subscription right.** Subject to Customer's compliance with this CSA and timely payment of Fees, Vendor hereby grants Customer a non-exclusive, non-transferable (except as permitted by Section 18.6), non-sublicensable, worldwide right during the term of each Order Form to access and use the Cloud Service identified in that Order Form solely for Customer's internal business purposes.

**4.2 Authorized Users and capacity.** The subscription right is limited to the number of Authorized Users, instances, environments, transactions, or other capacity unit identified on the Order Form (the "Subscription Scope"). The default capacity unit is per-Authorized-User. Customer is responsible for provisioning and de-provisioning Authorized Users, ensuring credentials are not shared, and keeping a current roster.

**4.3 Affiliate use.** Customer's Affiliates listed on the Order Form (or, if none are listed, any Affiliate that Customer wishes to onboard) may use the Cloud Service under the same Subscription Scope, provided that Customer remains primarily responsible for each Affiliate's compliance with this Agreement and is jointly liable for any Affiliate breach.

**4.4 Geographic scope.** Customer may access the Cloud Service from any jurisdiction not prohibited by Section 18.3 (Compliance with laws). Vendor is not obligated to provide localized support, language support, or in-region hosting unless the Order Form so provides.

**4.5 Reservation of rights.** All rights not expressly granted in this Agreement are reserved by Vendor or its licensors. Nothing in this Agreement is a sale, transfer, or assignment of any intellectual property right.

---

## 5. Customer responsibilities & restrictions

*Plain-language: Customer is responsible for what it and its users do with the Cloud Service, and there are specific things Customer must not do.*

**5.1 Compliance with laws.** Customer shall use the Cloud Service in compliance with all applicable laws, including export-control, sanctions, anti-corruption, anti-money-laundering, consumer-protection, employment, and data-protection laws, and shall obtain all consents and permissions needed for Customer Data and Customer Inputs to be processed by the Cloud Service.

**5.2 Authorized User conduct.** Customer is responsible for the acts and omissions of its Authorized Users and Affiliates as if they were Customer's own. Customer shall require each Authorized User to comply with this Agreement and the Acceptable Use Policy at Exhibit D.

**5.3 Account security.** Customer shall (i) keep credentials, API keys, tokens, and seed phrases confidential; (ii) enable and use any multi-factor authentication, single-sign-on, or similar security feature that Vendor makes available; (iii) promptly notify Vendor of any actual or suspected unauthorized access; and (iv) not allow any person other than the Authorized User to whom credentials are issued to use those credentials.

**5.4 Restrictions.** Customer shall not, and shall not permit any Authorized User or third party to:

(a) sell, resell, license, sublicense, distribute, rent, lease, or time-share the Cloud Service, or otherwise make it available to any third party other than Authorized Users;

(b) reverse-engineer, decompile, disassemble, or otherwise attempt to derive the source code, model weights, or underlying algorithms of the Cloud Service, except to the extent that applicable law expressly permits and Customer has first asked Vendor in writing for the interoperability information needed and Vendor has not provided it within a reasonable period;

(c) copy, modify, translate, or create derivative works of the Cloud Service or the Documentation, except as the Documentation itself permits;

(d) circumvent, disable, or interfere with security, rate-limiting, authentication, license-enforcement, or other technical-protection features of the Cloud Service;

(e) conduct competitive benchmarking, vulnerability scanning, load testing, or penetration testing of the Cloud Service without Vendor's prior written consent (which Vendor shall not unreasonably withhold for in-scope penetration tests of Customer's own tenant);

(f) scrape, harvest, or systematically extract data from the Cloud Service other than data Customer is entitled to access through documented APIs;

(g) use the Cloud Service to develop, train, fine-tune, or evaluate any product or service that competes with the Cloud Service;

(h) upload or transmit malware, ransomware, time bombs, logic bombs, worms, or any code intended to disrupt, damage, or gain unauthorized access to systems; or

(i) use the Cloud Service in violation of the Acceptable Use Policy at Exhibit D.

**5.5 Equipment and connectivity.** Customer is responsible for procuring and maintaining the network connectivity, hardware, browsers, and other equipment needed to access the Cloud Service, and for any third-party fees associated with that access.

**5.6 Cooperation.** Customer shall provide Vendor with the cooperation, information, and access reasonably required for Vendor to perform its obligations under this Agreement, including timely review of materials and timely designation of decision-makers.

---

## 6. Customer Data

*Plain-language: Customer owns its data; Vendor processes the data only to run the service; on exit, Customer can pull the data back; default rules for AI training and deletion are dual-perspective.*

**6.1 Ownership.** As between the Parties, Customer retains all right, title, and interest in and to Customer Data and Customer Materials, including all intellectual-property rights therein. Vendor acquires no ownership interest in Customer Data or Customer Materials by virtue of this Agreement.

**6.2 Processing license.** Customer hereby grants Vendor a worldwide, royalty-free, non-exclusive license, during the term and any post-termination tail period contemplated by Section 6.4, to host, copy, transmit, display, and otherwise process Customer Data and Customer Materials solely as necessary to (i) provide the Cloud Service to Customer, (ii) prevent or address fraud, security, or technical issues, (iii) comply with law, and (iv) carry out the limited improvement uses permitted by Section 15. The license does not extend to any other use.

**6.3 Customer responsibilities for Customer Data.** Customer represents that it has all rights, consents, and authority necessary for Vendor to process Customer Data as contemplated by this Agreement, that Customer Data does not infringe any third-party right, and that Customer has provided any notices required by data-protection laws.

**6.4 Return and deletion on termination.**

> **Customer-favorable:** Within ten (10) days after termination or expiration of an Order Form, Vendor shall make Customer Data available for export through documented APIs and through one or more bulk-download formats reasonable for the volume of Customer Data. Customer shall have ninety (90) days from termination to complete the export. Vendor shall delete Customer Data from active systems within thirty (30) days after the export window closes and shall purge Customer Data from backup media within one hundred eighty (180) days. Vendor shall provide a written certificate of deletion on request.

> **Vendor-favorable:** Vendor shall make Customer Data available for export for fifteen (15) days after termination through the same self-service tools that were available during the term. After that fifteen-day window, Vendor may delete Customer Data without further notice. Vendor is not obligated to retain, restore, or recreate any Customer Data that Customer fails to export during the window. Backups containing Customer Data are subject to Vendor's standard retention schedule and overwrite cycle.

> **Market-standard compromise (recommended default):** Vendor shall make Customer Data available for export for {{Return Window}} days (default thirty (30) days) after termination or expiration of the relevant Order Form, through the same export tools available during the term. After the export window closes, Vendor shall delete Customer Data from active production systems within thirty (30) days. Customer Data residing on backup or disaster-recovery media shall be retained only until the expiry of Vendor's then-current backup-retention cycle (not to exceed ninety (90) days), shall not be returned to active processing, and shall be subject to the same confidentiality and security obligations as during the term.

**6.5 AI/ML training on Customer Data.**

> **Customer-favorable:** Vendor shall not use Customer Data, Customer Inputs, or AI Output to train, fine-tune, evaluate, or improve any machine-learning model, whether dedicated to Customer or shared across Vendor's customer base, unless Customer has expressly opted in on the Order Form. Diagnostic logging is permitted only as needed to debug a specific incident reported by Customer and only with data minimization.

> **Vendor-favorable:** Vendor may use Customer Data, Customer Inputs, and AI Output to train, fine-tune, evaluate, and improve the Cloud Service and Vendor's models, including general-purpose models, unless Customer opts out on the Order Form. Customer's opt-out applies prospectively only.

> **Market-standard compromise (recommended default):** Vendor shall not use Customer Data, Customer Inputs, or AI Output to train or fine-tune any general-purpose model that is exposed to other customers. Vendor may use Customer Data, Customer Inputs, and AI Output (i) to train, tune, or evaluate models or features used solely on Customer's tenant, (ii) for diagnostic, abuse-detection, security, and fraud-prevention purposes, and (iii) for irreversibly de-identified, aggregated analytics as described in Section 15.2.

**6.6 Personal data.** Where Customer Data includes personal data, the Data Processing Agreement at Exhibit C governs Vendor's processing of that personal data, and Vendor processes that personal data only in accordance with Customer's documented instructions, the DPA, and applicable law.

**6.7 Backups.** Vendor maintains commercially reasonable backup and disaster-recovery measures for Customer Data, but Customer remains responsible for retaining its own copies of Customer Data outside the Cloud Service to the extent Customer's risk tolerance requires. Backups are not a substitute for Customer's own retention policies.

---

## 7. Confidentiality

*Plain-language: Each Party protects the other's non-public information, with standard exclusions and a court-order protocol.*

**7.1 Definition.** "Confidential Information" means any non-public information disclosed by one Party (the "Discloser") to the other (the "Recipient") that is identified as confidential at the time of disclosure or that a reasonable person would understand to be confidential given its nature and the circumstances of disclosure. Confidential Information includes the terms of this Agreement and each Order Form, product roadmaps, pricing, security documentation, and Customer Data.

**7.2 Obligations.** Recipient shall (i) use Confidential Information only to perform under this Agreement; (ii) protect Confidential Information using at least the same degree of care it uses for its own confidential information of like kind, and in any event no less than a reasonable degree of care; and (iii) limit access to its employees, contractors, advisors, and Affiliates who have a need to know and who are bound by written confidentiality obligations at least as protective as those in this Section.

**7.3 Exclusions.** Section 7.2 does not apply to information that Recipient can show: (a) was lawfully in Recipient's possession without confidentiality restriction before receipt from Discloser; (b) is or becomes publicly available through no act or omission of Recipient; (c) is lawfully obtained from a third party not under a confidentiality obligation owed to Discloser; or (d) is independently developed by Recipient without reference to or use of Discloser's Confidential Information.

**7.4 Compelled disclosure.** If Recipient is required by court order, subpoena, regulatory demand, or other legal process to disclose Confidential Information, Recipient shall, to the extent legally permitted, provide Discloser with prompt prior notice so that Discloser may seek a protective order or other appropriate remedy. Recipient shall cooperate, at Discloser's expense, with reasonable efforts to limit the scope of the disclosure, and shall disclose only the portion of Confidential Information that Recipient's counsel advises is legally required.

**7.5 Equitable relief.** The Parties acknowledge that breach of this Section may cause irreparable harm for which monetary damages would be an inadequate remedy, and that the non-breaching Party is entitled to seek injunctive relief without the requirement of posting a bond.

**7.6 Survival.** This Section survives termination of this Agreement for five (5) years, except that obligations relating to trade secrets continue for as long as the information qualifies as a trade secret under applicable law.

---

## 8. Fees, billing, taxes

*Plain-language: Customer pays the Fees on the Order Form on the agreed cadence; price changes are bounded; taxes are separate.*

**8.1 Fees.** Customer shall pay the Fees set forth on each Order Form. Unless an Order Form provides otherwise, Fees are payable in the currency stated on the Order Form (defaulting to U.S. dollars), are non-cancelable, and amounts paid are non-refundable except as expressly stated in this Agreement.

**8.2 Billing cadence.** Vendor shall invoice Customer in advance on a {{Billing Frequency}} basis (defaulting to annual). Usage-based, overage, and professional-service Fees are invoiced in arrears at the end of the relevant billing period. Each invoice is sent to {{Billing Contact Email}}.

**8.3 Annual price changes.**

> **Customer-favorable:** Vendor shall not increase Fees during any then-current Initial Term or Renewal Term. At the start of each Renewal Term, Vendor may increase Fees by no more than the lesser of three percent (3%) and the trailing-twelve-month change in the Consumer Price Index for All Urban Consumers (U.S. City Average), provided that Vendor gives Customer at least ninety (90) days' prior written notice.

> **Vendor-favorable:** Vendor may adjust Fees at any time upon thirty (30) days' prior notice. Renewal Term Fees default to Vendor's then-current list price unless the Order Form expressly fixes pricing.

> **Market-standard compromise (recommended default):** Fees are fixed during the then-current Initial Term or Renewal Term. Vendor may increase Fees for the next Renewal Term by no more than {{Annual Price Cap}} (default seven percent (7%)) over the Fees paid in the immediately preceding term, provided that Vendor gives Customer at least sixty (60) days' prior written notice before the renewal date. This cap does not apply to (i) new products or capacity added by Customer, or (ii) Fees in the first Renewal Term following a multi-year discount that was expressly identified as ramped or promotional on the Order Form.

**8.4 Taxes.** Fees are exclusive of all taxes, levies, duties, or similar governmental assessments, including value-added, sales, use, withholding, and similar taxes ("Taxes"). Customer is responsible for Taxes other than Taxes assessable against Vendor based on Vendor's net income, property, or employees. If Vendor has the legal obligation to pay or collect Taxes for which Customer is responsible, Vendor shall invoice Customer and Customer shall pay that amount unless Customer provides Vendor with a valid tax-exemption certificate. If applicable law requires withholding on amounts payable to Vendor, Customer shall pay the additional amounts necessary so that the net amount received by Vendor equals the amount Vendor would have received absent withholding (gross-up).

**8.5 Payment terms.**

> **Customer-favorable:** Invoices are due Net 60 days from receipt by Customer's accounts-payable department. Invoices not delivered to {{Billing Contact Email}} are deemed not received.

> **Vendor-favorable:** Invoices are due Net 15 days from invoice date and are payable by automatic credit-card or ACH debit unless Customer is expressly invoiced on terms.

> **Market-standard compromise (recommended default):** Invoices are due {{Payment Terms}} (default Net 30 days) from invoice date. Customer shall pay all undisputed Fees by wire transfer, ACH, or other method specified on the invoice, in immediately available funds.

**8.6 Late charges.** Past-due undisputed amounts accrue interest at {{Late Fee Rate}} per month (default one and one-half percent (1.5%) per month) or the maximum rate permitted by applicable law, whichever is lower, calculated daily and compounded monthly, plus all reasonable costs of collection (including reasonable attorneys' fees).

**8.7 Disputed invoices.** Customer shall give Vendor written notice of any good-faith dispute over an invoice within thirty (30) days after the invoice date, identifying the disputed amount and the basis for the dispute. The undisputed portion remains due on the original due date. The Parties shall negotiate in good faith to resolve the dispute within thirty (30) days after notice. Amounts not disputed within the thirty-day window are deemed accepted.

**8.8 Suspension for non-payment.** Vendor may suspend the Cloud Service for non-payment as set forth in Section 9.7.

**8.9 Currency and bank charges.** Customer is responsible for any bank fees, foreign-exchange spreads, and intermediary-bank charges associated with payment.

---

## 9. Term, renewal, termination & suspension

*Plain-language: Each subscription has a fixed term, renews on the cadence stated on the Order Form, and can be ended for material breach (with cure) or, in some cases, for convenience.*

**9.1 CSA term.** This CSA begins on the Effective Date and continues until the later of the expiration or termination of the last Order Form and the discharge of all surviving obligations.

**9.2 Order Form term.** Each Order Form begins on its start date and continues for the Initial Term stated on its face (defaulting to {{Initial Term}}, twelve (12) months).

**9.3 Renewal.**

> **Customer-favorable:** No Order Form renews automatically. At least sixty (60) days before the end of the Initial Term, Vendor shall send Customer a renewal proposal. The Order Form expires at the end of the Initial Term unless Customer expressly opts in to renewal in writing.

> **Vendor-favorable:** Each Order Form renews automatically for successive Renewal Terms equal in length to the Initial Term, unless Customer gives written notice of non-renewal at least ninety (90) days before the end of the then-current term. Customer may not stop a renewal that has already taken effect.

> **Market-standard compromise (recommended default):** Each Order Form renews automatically for successive Renewal Terms of {{Renewal Term}} (default twelve (12) months) unless either Party gives written notice of non-renewal at least {{Non-Renewal Notice Window}} (default thirty (30) days) before the end of the then-current term. Vendor shall send a renewal reminder to Customer's billing and notice contacts at least sixty (60) days before the renewal date. If Vendor fails to send the renewal reminder, the non-renewal notice window is extended day-for-day by the delay.

**9.4 Effect of non-renewal.** A timely notice of non-renewal causes the relevant Order Form to expire at the end of the then-current term. Other Order Forms are not affected. Sections 6.4, 7, 14, 16, 17, and 18 survive expiration.

**9.5 Termination for cause.**

> **Customer-favorable:** Customer may terminate this CSA or any Order Form for material breach by Vendor on ten (10) days' written notice if Vendor has not cured the breach. Vendor may terminate only on sixty (60) days' written notice and only after a non-cure determination by independent counsel agreed by the Parties.

> **Vendor-favorable:** Either Party may terminate for material breach on sixty (60) days' written notice if the breach is not cured within sixty (60) days. Customer's failure to pay any undisputed Fee is a material breach, and Vendor may terminate immediately for any payment default that continues for more than fifteen (15) days after notice.

> **Market-standard compromise (recommended default):** Either Party may terminate this CSA, or any individual Order Form, for material breach by the other Party that is not cured within {{Cure Period}} (default thirty (30) days) after written notice describing the breach with reasonable specificity. For repeated breaches of the same nature, no cure period is required if the breaching Party has already received a cure notice for a substantially similar breach within the preceding twelve (12) months. Either Party may terminate immediately on written notice if the other Party (i) becomes the subject of a voluntary or involuntary insolvency, receivership, or assignment for the benefit of creditors that is not dismissed within sixty (60) days, or (ii) ceases to do business as a going concern.

**9.6 Termination for convenience.**

> **Customer-favorable:** Customer may terminate any Order Form for convenience on thirty (30) days' written notice and shall receive a pro-rata refund of pre-paid Fees for the unused portion of the term. Vendor has no termination-for-convenience right.

> **Vendor-favorable:** Neither Party may terminate for convenience. Customer remains liable for all Fees through the end of the then-current term.

> **Market-standard compromise (recommended default):** Termination for convenience is not available unless the relevant Order Form expressly provides for it, in which case the terminating Party shall give the notice period stated on the Order Form (defaulting to ninety (90) days). Vendor may decline to renew an Order Form on the standard non-renewal notice in Section 9.3 without that being a termination for convenience. If Customer terminates for convenience and the Order Form does not specify the financial consequence, Customer shall pay all Fees through the end of the then-current term.

**9.7 Suspension.** Vendor may suspend Customer's access to the Cloud Service:

(a) **for non-payment**, after any undisputed amount has been outstanding for more than ten (10) days following a payment-default notice;

(b) **for security or abuse**, immediately and without notice if Vendor reasonably believes that continued access poses a material security, integrity, or availability risk to the Cloud Service or to other customers, or that Customer or an Authorized User is violating Section 5.4 or the Acceptable Use Policy in a manner that cannot be addressed by less-disruptive means; or

(c) **as required by law**, if Vendor is required by court order, regulator, or applicable law to suspend the Cloud Service.

Vendor shall use commercially reasonable efforts to (i) notify Customer of the suspension and the reasons for it, (ii) limit the suspension to the affected components or Authorized Users, and (iii) restore access promptly once the underlying issue is resolved. A suspension is not a termination, and Fees continue to accrue during a suspension other than a suspension caused solely by Vendor.

**9.8 Effect of termination.** On termination or expiration of an Order Form, (i) Customer's right to access the Cloud Service under that Order Form ends; (ii) Customer shall pay all Fees accrued through the effective date of termination; (iii) Vendor shall make Customer Data available for export per Section 6.4; (iv) each Party shall return or destroy the other's Confidential Information, subject to standard archival exceptions; and (v) Customer shall cease use of any Vendor Materials.

**9.9 Survival.** Sections 1 (only as to non-binding orientation), 3, 5.4, 6.1, 6.4, 7, 8 (as to amounts accrued before termination), 9.4, 9.7, 9.8, 9.9, 14, 15.4, 16, 17, and 18 survive termination of this Agreement.

---

## 10. Service Level Agreement

*Plain-language: Vendor commits to a defined uptime; if Vendor misses, Customer's remedy is service credits, calculated as set out in Exhibit B.*

**10.1 Service-level commitment.** Vendor shall make the Cloud Service available with a monthly uptime percentage of at least {{Uptime Commitment}} (default 99.9%) measured as set forth in Exhibit B (the "Uptime Commitment"). The Uptime Commitment excludes Scheduled Maintenance, Customer-caused unavailability, force-majeure events, and the carve-outs identified in Exhibit B.

**10.2 Service credits.** If Vendor fails to meet the Uptime Commitment in a calendar month, Customer is entitled to service credits as set forth in Exhibit B. Service credits are calculated as a percentage of the monthly Fees for the affected component and are applied as a credit against future invoices.

**10.3 Sole and exclusive remedy.** Service credits are Customer's sole and exclusive remedy, and Vendor's sole and exclusive liability, for any failure to meet the Uptime Commitment. This Section 10.3 does not limit Customer's right to terminate for material breach under Section 9.5 if Vendor fails to meet the Uptime Commitment for {{SLA Termination Threshold}} (default three (3)) consecutive calendar months.

**10.4 Reporting.** Vendor shall make uptime reporting available through a status page or service-credit dashboard. Customer must request a service credit in writing within sixty (60) days after the end of the affected month, or the credit is forfeited.

**10.5 Cross-reference.** The full Service Level Agreement, including measurement methodology, downtime definitions, and credit table, is set forth in Exhibit B and the companion `legalcode-sla` template.

---

## 11. Security & data protection

*Plain-language: Vendor maintains a written security program that meets industry standards; Customer can verify it; breaches are notified on a defined timeline; personal data flows through the DPA.*

**11.1 Security program.** Vendor shall maintain a written information-security program designed to protect the confidentiality, integrity, and availability of Customer Data, that is aligned with one or more recognized industry frameworks (including, where applicable, SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, NIST CSF, or PCI DSS to the scope it applies). The program includes administrative, technical, and physical safeguards, including access control, encryption in transit and (where applicable) at rest, vulnerability management, secure software-development practices, logging, incident response, business continuity, vendor risk management, and personnel training. Vendor shall not materially decrease the protection afforded by the program during the term.

**11.2 Technical and organizational measures.** The technical and organizational measures (TOMs) that implement the security program are described in Exhibit C and Annex 2 of the Data Processing Agreement.

**11.3 Compliance reports.** Vendor shall, on request not more than once per twelve-month period, make available to Customer under non-disclosure (i) Vendor's most recent SOC 2 Type II report or ISO/IEC 27001 certificate (or equivalent), (ii) a current penetration-test summary, and (iii) responses to a reasonable security questionnaire substantially aligned with CAIQ or SIG-Lite.

**11.4 Audit rights.**

> **Customer-favorable:** Customer may, on thirty (30) days' notice, conduct on-site audits of Vendor's controls relevant to the Cloud Service, including interviews of personnel and inspection of documentation, no more than once per year and at Customer's expense (except where the audit reveals a material non-compliance, in which case Vendor bears reasonable costs). Customer may also commission a third-party auditor of its choice.

> **Vendor-favorable:** Customer's audit right is satisfied by access to Vendor's then-current SOC 2 Type II report and a written response to a security questionnaire, in each case no more than once per twelve-month period. No on-site audits are permitted, and Customer shall not commission third-party penetration testing of the Cloud Service.

> **Market-standard compromise (recommended default):** Once per twelve-month period, Customer (or its independent third-party auditor, subject to a non-disclosure agreement and excluding any auditor that is a competitor of Vendor) may, on thirty (30) days' written notice, audit Vendor's compliance with this Section by reviewing Vendor's SOC 2 Type II report, ISO/IEC 27001 certification (where issued), the latest penetration-test executive summary, and Vendor's responses to a reasonable security questionnaire. On-site audits are available only (i) where required by Customer's regulator, (ii) following a confirmed Security Breach affecting Customer Data, or (iii) where Vendor's reports do not address Customer's documented regulatory obligation. Customer shall conduct audits during normal business hours and in a manner that does not unreasonably disrupt Vendor's operations. Customer shall bear its own audit costs unless the audit reveals a material non-compliance, in which case Vendor shall reimburse Customer's reasonable out-of-pocket costs.

**11.5 Security-breach notification.**

> **Customer-favorable:** Vendor shall notify Customer of any Security Breach within twenty-four (24) hours after Vendor becomes aware. The notice shall include a preliminary impact assessment and shall be supplemented within seventy-two (72) hours with a detailed forensic update.

> **Vendor-favorable:** Vendor shall notify Customer of a confirmed Security Breach without undue delay after Vendor's incident-response team has confirmed that Customer Data was affected.

> **Market-standard compromise (recommended default):** Vendor shall notify Customer of a confirmed Security Breach affecting Customer Data without undue delay and in any event within {{Breach Notification SLA}} (default seventy-two (72) hours) after Vendor's incident-response team confirms the breach. The initial notice shall describe the nature of the breach, the categories and approximate volume of Customer Data affected (to the extent then known), and the steps Vendor is taking. Vendor shall provide further updates as material new information becomes available and shall cooperate reasonably with Customer's regulatory and customer-notification obligations. The DPA at Exhibit C controls notification of personal-data breaches.

**11.6 Personal-data processing.** Where Vendor processes personal data on Customer's behalf, the Data Processing Agreement at Exhibit C governs that processing, including the processor's obligations, the Subprocessor regime, cross-border transfer mechanisms, data-subject-rights cooperation, and personal-data-breach notifications. The default relationship is controller (Customer) to processor (Vendor) for the Cloud Service.

**11.7 Defined term.** "Security Breach" means a confirmed unauthorized access to, acquisition of, or disclosure of Customer Data that is not the result of Customer's act or omission. Reconnaissance, attempted-but-unsuccessful access, and access by Authorized Users are not Security Breaches.

---

## 12. Trials & beta features

*Plain-language: Free, pilot, evaluation, and beta access is provided AS IS, may end at any time, and is governed by lighter terms than paid subscriptions.*

**12.1 Trials and beta scope.** Vendor may make Trials or beta features available, with or without a fee, on an Order Form or via a self-service signup. "Beta features" means features identified in the Documentation or in the user interface as alpha, beta, preview, early-access, experimental, or similar, even if accessed under a paid Order Form.

**12.2 AS IS basis.** Trials and beta features are provided AS IS and AS AVAILABLE, without any warranty of any kind, express or implied, including any implied warranty of merchantability, fitness for a particular purpose, accuracy, or non-infringement. The Service Level Agreement does not apply.

**12.3 No production use; non-essential data.** Customer shall not use Trials or beta features for production workloads or for processing data that Customer cannot afford to lose, including special categories of personal data, payment-card data, or regulated data unless the Order Form expressly so permits.

**12.4 Discontinuation; data deletion.** Vendor may modify or discontinue any Trial or beta feature at any time and without notice. Vendor may delete data uploaded into a Trial or beta feature on termination of that Trial or beta feature. If Customer converts a Trial subscription to a paid subscription before the end of the trial period, configuration and data created during the trial will be preserved unless the Order Form for the paid subscription says otherwise.

**12.5 Liability cap for Trials.** Notwithstanding Section 16.5, Vendor's total aggregate liability arising out of or relating to a Trial (including any beta feature accessed under a Trial) is capped at U.S. $100, except for the carve-outs in Section 16.7.

**12.6 Feedback.** Customer's feedback on a Trial or beta feature is licensed to Vendor under Section 14.5.

---

## 13. Third-party services & integrations

*Plain-language: Customer may integrate the Cloud Service with third-party services, but Vendor is not responsible for those third-party services.*

**13.1 Customer-elected integrations.** Customer may enable integrations between the Cloud Service and Third-Party Services, either through the Cloud Service's marketplace, through Vendor-published APIs, or through Customer-developed connectors.

**13.2 Authorization to exchange data.** When Customer enables a Third-Party Service integration, Customer authorizes Vendor to transmit Customer Data to and receive data from that Third-Party Service to the extent necessary to operate the integration. The Third-Party Service is not a Subprocessor for purposes of the DPA unless Vendor expressly identifies it as such.

**13.3 Customer's risk.** Customer's use of any Third-Party Service is governed by Customer's separate agreement with the Third-Party Service provider. Vendor is not responsible for any Third-Party Service, including its availability, security, accuracy, content, or compliance, and Vendor disclaims all liability arising from Third-Party Services to the maximum extent permitted by law.

**13.4 Suspension or removal.** Vendor may suspend or remove a Third-Party Service integration if (i) the Third-Party Service ceases to be available, (ii) the Third-Party Service is acting in a manner that compromises the Cloud Service, or (iii) Vendor's agreement with the Third-Party Service provider has been terminated. Vendor shall use commercially reasonable efforts to give Customer reasonable advance notice unless Vendor reasonably believes that immediate action is necessary.

**13.5 No endorsement.** Listing of a Third-Party Service in Vendor's marketplace or Documentation is not an endorsement.

---

## 14. Intellectual property

*Plain-language: Each side keeps what it brought to the table; Customer keeps Customer Data; feedback is licensed to Vendor; logos may be used with consent.*

**14.1 Vendor IP.** As between the Parties, Vendor retains all right, title, and interest in and to the Cloud Service, the Documentation, Vendor Materials, and all derivatives, modifications, and improvements thereto, including all intellectual-property rights therein. No license is granted to Customer to the source code, model weights, or underlying architecture of the Cloud Service. The subscription right in Section 4 is the only license granted to Customer to the Cloud Service.

**14.2 Customer IP.** As between the Parties, Customer retains all right, title, and interest in and to Customer Data and Customer Materials, including all intellectual-property rights therein. The license to Vendor in Section 6.2 is the only license granted to Vendor to Customer Data.

**14.3 Pre-existing IP.** Each Party retains ownership of intellectual property it owned or licensed before the Effective Date or that it develops independently of this Agreement.

**14.4 Improvements.** Improvements, modifications, and derivatives of the Cloud Service that Vendor develops in the course of providing the Cloud Service to Customer (whether at Customer's request or otherwise) are owned by Vendor.

**14.5 Feedback license.** If Customer or any Authorized User provides feedback, suggestions, ideas, or recommendations regarding the Cloud Service ("Feedback"), Customer hereby grants Vendor a perpetual, irrevocable, worldwide, royalty-free, fully paid-up, non-exclusive, sublicensable license to use, reproduce, modify, distribute, display, and exploit the Feedback for any purpose, including incorporation into the Cloud Service. Customer is not obligated to provide Feedback. Vendor shall not identify Customer as the source of any Feedback without Customer's prior written consent.

**14.6 Trademark license for identification.** Customer grants Vendor a non-exclusive, royalty-free, worldwide license to use Customer's name and logo solely to identify Customer as a customer of Vendor, in accordance with Customer's then-current trademark guidelines (if any), on Vendor's customer-list webpage and similar marketing materials. Customer may revoke this license at any time on written notice, and Vendor shall remove the references within thirty (30) days. Any use beyond identification (case studies, press releases, joint announcements) requires Customer's prior written approval.

**14.7 No implied licenses.** Except as expressly granted in this Agreement, no license is granted by implication, estoppel, exhaustion, or otherwise.

---

## 15. AI & machine learning

*Plain-language: This Section governs how AI features in the Cloud Service handle Customer Data, who owns AI Output, and how the parties allocate risk for AI-specific issues.*

**15.1 Training restriction.**

> **Customer-favorable:** Vendor shall not use any Customer Data, Customer Inputs, or AI Output to train, fine-tune, retrieve from, or evaluate any model unless Customer expressly opts in on the Order Form for a specific, named model and a specific purpose. Diagnostic logging is permitted only as needed to debug a specific Customer-reported incident, only with data minimization, and only for the duration needed to resolve the incident.

> **Vendor-favorable:** Vendor may use Customer Data, Customer Inputs, and AI Output to train, fine-tune, evaluate, and improve any model used in the Cloud Service, including general-purpose foundation models offered to other customers, unless Customer opts out in writing. Customer's opt-out applies prospectively only and does not require Vendor to delete data previously used in training.

> **Market-standard compromise (recommended default):** Vendor shall not use Customer Data, Customer Inputs, or AI Output to train or fine-tune any general-purpose model that is exposed to other customers or to the public. Vendor may use Customer Data, Customer Inputs, and AI Output (i) to train, tune, retrieve from, or evaluate models or features used solely on Customer's tenant or solely for Customer's benefit, (ii) for diagnostic, abuse-detection, security, fraud-prevention, and safety purposes, and (iii) for irreversibly de-identified, aggregated analytics as described in Section 15.2. Vendor shall not use special categories of personal data or sensitive data for any training purpose.

**15.2 Aggregated and de-identified data.** Vendor may collect and use usage and performance data and other operational data about how the Cloud Service is configured and used and may de-identify and aggregate Customer Data so that the resulting data does not identify Customer, any Authorized User, any individual data subject, or any organization, and cannot, in light of reasonable measures, be re-identified. Vendor may use that aggregated, irreversibly de-identified data to operate, secure, monitor, benchmark, and improve the Cloud Service and Vendor's other products and services. Vendor shall not publish or sell aggregated data in a form that identifies Customer.

**15.3 AI Output ownership.**

> **Customer-favorable:** As between the Parties, Customer owns all AI Output generated for Customer through the Cloud Service. Vendor hereby assigns to Customer all right, title, and interest Vendor may have in AI Output, to the extent assignable under applicable law. Vendor may not use AI Output other than as strictly necessary to deliver the Cloud Service to Customer.

> **Vendor-favorable:** Vendor retains all right, title, and interest in AI Output. Vendor grants Customer a perpetual, worldwide, non-exclusive, royalty-free license to use AI Output for Customer's internal business purposes during the term and after termination.

> **Market-standard compromise (recommended default):** As between the Parties, Customer owns AI Output generated for Customer through the Cloud Service, subject to (i) any third-party rights in materials reflected in the AI Output and (ii) Vendor's reservation of a non-exclusive, royalty-free, worldwide license to use AI Output to operate, secure, debug, evaluate, and improve the Cloud Service in a manner that does not identify Customer. Customer is solely responsible for determining whether AI Output is sufficiently original, accurate, lawful, and non-infringing for Customer's intended use.

**15.4 No warranty for AI Output.** AI Output is generated by probabilistic models. AI Output may be inaccurate, incomplete, biased, hallucinated, offensive, or otherwise unsuitable for a particular purpose. Customer shall (i) review AI Output before relying on it, (ii) not present AI Output as professional advice (medical, legal, tax, financial, or otherwise) without competent human review, and (iii) not rely on AI Output as the sole basis for decisions that have legal, financial, or safety significance. The disclaimers in Section 16.3 apply to AI Output to the maximum extent permitted by law.

**15.5 Prompt injection, model bias, and other AI risks.** Customer acknowledges that machine-learning systems are subject to risks including prompt injection, jailbreaking, training-data poisoning, model drift, hallucination, and bias. Vendor commits to commercially reasonable mitigations consistent with industry practice (input filtering, output filtering, system-prompt hardening, evaluation pipelines, red-teaming, and incident response) and to remediate confirmed safety issues with reasonable promptness, but Vendor does not warrant that the Cloud Service is free from these risks. Customer shall not deploy AI features in regulated, high-stakes, or safety-critical contexts without independent human-in-the-loop review.

**15.6 Customer Inputs hygiene.** Customer shall not submit Customer Inputs containing (i) special categories of personal data unless the Order Form expressly permits, (ii) payment-card data outside a designated payment-card module, (iii) protected health information unless covered by an executed Business Associate Addendum, (iv) classified or export-controlled information, or (v) content that infringes third-party rights or violates the Acceptable Use Policy.

**15.7 AI transparency.** Vendor shall publish, in the Documentation or in a model card, a high-level description of the categories of models in use in the Cloud Service, the categories of training data, known limitations, and material updates. Vendor shall give Customer reasonable advance notice of material changes that would change the risk profile of the Cloud Service for Customer.

---

## 16. Warranties, disclaimers & limitations of liability

*Plain-language: Vendor stands behind the basics, disclaims the rest, and caps the maximum exposure of either side, with named carve-outs.*

**16.1 Mutual warranties.** Each Party represents and warrants that (i) it has the corporate power and authority to enter into this Agreement and to perform its obligations, (ii) execution and performance do not violate any other contract or law to which it is subject, and (iii) it shall comply with all laws applicable to its performance.

**16.2 Vendor warranties.** Vendor warrants that, during the term:

(a) the Cloud Service will materially conform to the Documentation;

(b) Vendor will not knowingly insert into the Cloud Service any virus, ransomware, time bomb, logic bomb, worm, or other malicious code; and

(c) Vendor will maintain the security program described in Section 11.1.

**16.3 Disclaimer.** EXCEPT FOR THE EXPRESS WARRANTIES IN SECTIONS 16.1 AND 16.2, THE CLOUD SERVICE, AI OUTPUT, DOCUMENTATION, AND ANY OTHER MATERIALS OR SERVICES PROVIDED BY VENDOR UNDER THIS AGREEMENT ARE PROVIDED "AS IS" AND "AS AVAILABLE." TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, VENDOR DISCLAIMS ALL WARRANTIES, EXPRESS, IMPLIED, OR STATUTORY, INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, TITLE, NON-INFRINGEMENT, AND ANY WARRANTY ARISING FROM COURSE OF DEALING, COURSE OF PERFORMANCE, OR USAGE OF TRADE. VENDOR DOES NOT WARRANT THAT THE CLOUD SERVICE WILL BE UNINTERRUPTED, ERROR-FREE, OR SECURE AGAINST UNAUTHORIZED INTRUSION, OR THAT AI OUTPUT WILL BE ACCURATE OR FIT FOR ANY PARTICULAR PURPOSE. NOTHING IN THIS SECTION LIMITS NON-WAIVABLE CONSUMER WARRANTIES UNDER APPLICABLE LAW; FOR JURISDICTIONS THAT DO NOT ALLOW EXCLUSION OF IMPLIED WARRANTIES, THE EXCLUSIONS APPLY TO THE MAXIMUM EXTENT PERMITTED.

**16.4 Sole remedy for service non-conformance.** If Vendor breaches Section 16.2(a), Customer's sole and exclusive remedy and Vendor's sole and exclusive liability is, at Vendor's option, to (i) re-perform the non-conforming portion of the Cloud Service, or (ii) terminate the affected Order Form and refund the prorated portion of pre-paid Fees attributable to the period after the date of termination. Customer must give Vendor notice of the non-conformance within thirty (30) days after the non-conformance is observed. This remedy does not apply to non-conformances caused by Customer Data, Customer Materials, Third-Party Services, Customer's breach of Section 5, or modifications made by anyone other than Vendor.

**16.5 Limitation of liability — cap.**

> **Customer-favorable:** Each Party's total aggregate liability arising out of or relating to this Agreement is capped at the greater of (i) two times (2x) the Fees paid or payable by Customer under the affected Order Form during the twenty-four (24) months immediately preceding the event giving rise to the claim, and (ii) {{Liability Cap Floor}} (default U.S. $1,000,000).

> **Vendor-favorable:** Each Party's total aggregate liability arising out of or relating to this Agreement is capped at the Fees paid or payable by Customer under the affected Order Form during the twelve (12) months immediately preceding the event giving rise to the claim. There is no minimum cap floor.

> **Market-standard compromise (recommended default):** Subject to Section 16.7, each Party's total aggregate liability arising out of or relating to this Agreement, regardless of the form of action and whether in contract, tort, statute, or otherwise, is capped at the greater of (i) {{Liability Cap Multiplier}} (default one and one-half times (1.5x)) the Fees paid or payable by Customer under the affected Order Form during the twelve (12) months immediately preceding the event giving rise to the claim, and (ii) {{Liability Cap Floor}} (default U.S. $100,000). The greater of the two amounts applies.

**16.6 Limitation of liability — exclusion of indirect damages.**

> **Customer-favorable:** Neither Party shall be liable for indirect, incidental, special, consequential, exemplary, or punitive damages (including lost profits, lost revenue, or lost data) arising out of or relating to this Agreement, except that this exclusion does not apply to (i) breach of confidentiality, (ii) indemnity obligations, (iii) gross negligence, willful misconduct, or fraud, or (iv) Customer's payment obligations.

> **Vendor-favorable:** TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, NEITHER PARTY SHALL BE LIABLE FOR INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES (INCLUDING LOST PROFITS, LOST REVENUE, LOST DATA, COST OF COVER, OR LOSS OF GOODWILL) ARISING OUT OF OR RELATING TO THIS AGREEMENT, REGARDLESS OF THE FORM OF ACTION AND EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, WITH NO CARVE-OUTS.

> **Market-standard compromise (recommended default):** TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, AND SUBJECT TO SECTION 16.7, NEITHER PARTY SHALL BE LIABLE FOR INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES (INCLUDING LOST PROFITS, LOST REVENUE, LOST DATA, COST OF COVER, OR LOSS OF GOODWILL) ARISING OUT OF OR RELATING TO THIS AGREEMENT, REGARDLESS OF THE FORM OF ACTION AND EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

**16.7 Carve-outs.** The limitations in Sections 16.5 and 16.6 do not apply to: (i) a Party's indemnification obligations under Section 17; (ii) breach of Section 7 (Confidentiality); (iii) breach of Section 5.4 (Restrictions) or the Acceptable Use Policy; (iv) infringement, misappropriation, or violation of the other Party's intellectual-property rights; (v) gross negligence, willful misconduct, or fraud; (vi) Customer's payment obligations under Section 8; or (vii) liability that cannot be limited under applicable law. For Sections 16.7(i) through (iv), each Party's aggregate liability is capped at three times (3x) the cap calculated under Section 16.5 (the "Super-Cap"). The Super-Cap does not apply to clauses 16.7(v), (vi), or (vii).

**16.8 Insurance cross-reference.** Vendor maintains the insurance set forth in Section 17.6.

**16.9 Allocation.** The Parties acknowledge that the limitations of liability in this Section reflect the allocation of risk that is the basis of the bargain, that Fees would be substantially higher absent these limitations, and that the limitations apply notwithstanding the failure of any limited or exclusive remedy.

---

## 17. Indemnification & insurance

*Plain-language: Vendor defends Customer against IP infringement claims about the Cloud Service; Customer defends Vendor against claims arising from Customer Data and Customer's misuse; both sides carry insurance.*

**17.1 Vendor IP indemnity.**

> **Customer-favorable:** Vendor shall defend, indemnify, and hold Customer harmless from and against any third-party claim, action, suit, or proceeding ("Claim") alleging that Customer's use of the Cloud Service infringes, misappropriates, or violates any intellectual-property right or right of publicity of any third party, and shall pay the damages and costs (including reasonable attorneys' fees) finally awarded by a court of competent jurisdiction or agreed in settlement. The indemnity covers AI Output and includes claims for misappropriation of trade secrets and right-of-publicity claims.

> **Vendor-favorable:** Vendor shall defend Customer against a third-party Claim alleging that the unmodified Cloud Service, used in accordance with the Documentation, directly infringes a U.S. patent, U.S. registered copyright, or U.S. registered trademark of the third party. Vendor's only obligation is to defend; Vendor's only payment obligation is for damages awarded by a court of competent jurisdiction. The indemnity does not cover AI Output, Customer Materials, Customer Data, modifications, combinations, open-source components, beta features, or claims arising from Customer's use after a workaround is offered.

> **Market-standard compromise (recommended default):** Vendor shall defend Customer against a third-party Claim alleging that the Cloud Service, when used by Customer in accordance with this Agreement and the Documentation, infringes, misappropriates, or violates a third party's patent, copyright, trademark, or trade secret, and shall pay damages and costs (including reasonable attorneys' fees) finally awarded against Customer or agreed in settlement by Vendor.

**17.2 IP indemnity exclusions.** Vendor's IP indemnity in Section 17.1 does not apply to Claims arising from: (i) Customer Data, Customer Inputs, or Customer Materials; (ii) modifications to the Cloud Service made by anyone other than Vendor; (iii) combinations of the Cloud Service with software, hardware, data, or services not provided by Vendor, where the infringement would not have arisen but for the combination; (iv) Customer's continued use of the Cloud Service after Vendor has notified Customer to stop; (v) Trials and beta features; (vi) Third-Party Services; or (vii) AI Output to the extent the alleged infringement arises from Customer Inputs.

**17.3 IP indemnity mitigation.** If a Claim under Section 17.1 is made or, in Vendor's reasonable opinion, is likely, Vendor may, at its option and expense: (a) procure for Customer the right to continue using the Cloud Service; (b) modify or replace the affected portion of the Cloud Service so that it is non-infringing while substantially preserving functionality; or (c) if (a) and (b) are not commercially reasonable, terminate the affected Order Form and refund the prorated portion of pre-paid Fees attributable to the period after the date of termination. Section 17.1 and this Section 17.3 state Vendor's entire liability and Customer's exclusive remedy for IP claims arising from the Cloud Service.

**17.4 Customer indemnity.** Customer shall defend, indemnify, and hold Vendor harmless from and against any third-party Claim arising from or relating to: (i) Customer Data, Customer Inputs, or Customer Materials, including any allegation that Customer Data infringes a third party's intellectual-property right or violates applicable law; (ii) Customer's or its Authorized Users' breach of Section 5.4 or the Acceptable Use Policy; (iii) Customer's gross negligence, willful misconduct, or fraud; or (iv) Customer's use of the Cloud Service in regulated or safety-critical contexts in violation of Section 15.5.

**17.5 Mutual indemnity for confidentiality breach.**

> **Customer-favorable:** Each Party shall defend, indemnify, and hold the other harmless from and against third-party Claims arising from a breach by the indemnifying Party of Section 7 (Confidentiality), and the Super-Cap in Section 16.7 does not apply to this indemnity.

> **Vendor-favorable:** No mutual confidentiality indemnity. Each Party's recovery for breach of Section 7 is limited to direct damages within the Section 16.5 cap.

> **Market-standard compromise (recommended default):** Each Party shall defend, indemnify, and hold the other harmless from and against third-party Claims arising from the indemnifying Party's breach of Section 7 (Confidentiality), subject to the cap in Section 16.5 and the Super-Cap in Section 16.7.

**17.6 Indemnity procedure.** The indemnified Party shall (i) give the indemnifying Party prompt written notice of the Claim (delay does not relieve the indemnifying Party except to the extent prejudiced); (ii) tender sole control of the defense and settlement to the indemnifying Party (provided that the indemnifying Party shall not settle in a manner that imposes a non-monetary obligation, an admission of fault, or an injunction on the indemnified Party without the indemnified Party's prior written consent, which shall not be unreasonably withheld); and (iii) provide reasonable cooperation, at the indemnifying Party's expense. The indemnified Party may participate in the defense at its own expense with counsel of its choice.

**17.7 Insurance.** During the term and for one (1) year after, Vendor shall maintain at its expense the following insurance with insurers having a Best's rating of A- or better:

(a) **Commercial general liability** with limits of at least {{CGL Limit}} (default U.S. $1,000,000 per occurrence / $2,000,000 aggregate);

(b) **Professional liability / errors-and-omissions** with limits of at least {{E&O Limit}} (default U.S. $5,000,000 per claim / aggregate);

(c) **Cyber liability / technology errors-and-omissions** with limits of at least {{Insurance Cyber Limit}} (default U.S. $5,000,000 per claim / aggregate), covering data-breach response, regulatory defense, third-party privacy claims, and network-security liability;

(d) **Workers' compensation** at statutory limits where required by law; and

(e) **Employer's liability** at limits commensurate with industry practice in the relevant jurisdiction.

On Customer's reasonable request, Vendor shall furnish a certificate of insurance evidencing the coverages and shall name Customer as an additional insured under the commercial general liability policy where commercially reasonable. Cancellation of any required policy shall be subject to thirty (30) days' prior notice where the policy permits.

**17.8 Sole remedies.** Section 17.1 and Section 17.4 state each Party's sole and exclusive remedy and the indemnifying Party's entire liability for the Claims described therein.

---

## 18. General provisions

*Plain-language: The boilerplate that lets the Agreement function — notices, force majeure, assignment, signatures, governing law, and dispute resolution.*

**18.1 Notices.** Notices under this Agreement shall be in writing and delivered to the addresses on the Order Form (or, if none, the addresses in the preamble), with copies to {{Notice Email Vendor}} and {{Notice Email Customer}}. Notices may be delivered by (i) personal delivery, (ii) nationally recognized courier, (iii) certified mail return-receipt, or (iv) email with confirmation of receipt (auto-replies do not count). Notice is effective on the earlier of receipt and the second business day after sending. Operational, billing, and product-update notices may be delivered through the Cloud Service's in-product notification mechanism. Notices of breach, termination, indemnification, or litigation must use one of clauses (i) through (iv).

**18.2 Force majeure.** Neither Party is liable for any delay or failure to perform (other than payment obligations) caused by an event beyond its reasonable control, including acts of God, war, terrorism, riot, civil unrest, government action, embargo, pandemic, epidemic, labor disruption, internet or telecommunications failure of an upstream provider, energy failure, or natural disaster (a "Force Majeure Event"). The affected Party shall give prompt notice and use commercially reasonable efforts to mitigate. If a Force Majeure Event affecting Vendor's performance of the Cloud Service continues for more than thirty (30) consecutive days, Customer may terminate the affected Order Form and receive a prorated refund of pre-paid Fees for unused services from the date of the Force Majeure Event.

**18.3 Compliance with laws; export and sanctions.** Each Party shall comply with all applicable laws in performing under this Agreement, including (i) export-control laws of the United States, the European Union, the United Kingdom, and other relevant jurisdictions, (ii) economic-sanctions programs administered by the U.S. Department of the Treasury Office of Foreign Assets Control (OFAC), the European Union, the United Kingdom, and the United Nations, (iii) anti-corruption and anti-bribery laws including the U.S. Foreign Corrupt Practices Act and the U.K. Bribery Act, and (iv) anti-money-laundering laws. Customer represents that it is not a sanctioned party, is not located in a comprehensively sanctioned jurisdiction, and shall not allow Authorized Users in such jurisdictions to access the Cloud Service.

**18.4 Anti-corruption.** Neither Party shall offer or accept any bribe, kickback, or improper payment in connection with this Agreement. Each Party shall maintain books and records sufficient to evidence compliance with anti-corruption laws.

**18.5 Government end users.** If Customer is a U.S. federal government entity, the Cloud Service and Documentation are "commercial items" as defined in 48 C.F.R. 2.101, and the U.S. government acquires only the rights granted to other end users under this Agreement, consistent with 48 C.F.R. 12.211, 12.212, 227.7202-1, and 227.7202-4.

**18.6 Assignment.** Neither Party may assign this Agreement, in whole or in part, without the other Party's prior written consent (not to be unreasonably withheld), except that either Party may assign this Agreement, on notice but without consent, to (i) an Affiliate or (ii) a successor in interest in connection with a merger, acquisition, reorganization, or sale of all or substantially all of its assets, provided that the successor is not a competitor of the non-assigning Party as of the date of assignment. Any attempted assignment in violation of this Section is void. The Agreement binds and benefits permitted successors and assigns.

**18.7 Subcontracting.** Vendor may subcontract any of its obligations under this Agreement, provided that Vendor remains responsible for the acts and omissions of its subcontractors and that Subprocessors processing personal data are governed by the DPA at Exhibit C.

**18.8 Independent contractors.** The Parties are independent contractors. Nothing in this Agreement creates an agency, partnership, joint venture, employment, or fiduciary relationship.

**18.9 No third-party beneficiaries.** Except for the indemnified parties identified in Section 17, this Agreement does not create any rights in favor of any third party.

**18.10 Entire agreement.** This Agreement, together with each Order Form and the Exhibits incorporated by reference, is the entire agreement between the Parties on its subject matter and supersedes all prior or contemporaneous agreements, proposals, statements, and understandings, written or oral, on that subject matter.

**18.11 Amendments.** Any amendment, modification, or waiver of any provision of this Agreement is effective only if in writing and signed by an authorized representative of each Party (electronic signatures count). No course of dealing, course of performance, or failure to enforce a provision is a waiver. Vendor may update operational documents (the AUP, the SLA, the Documentation, and the Subprocessor list) on notice as set forth in those documents, provided that the updates do not materially decrease the Cloud Service or Vendor's security or privacy commitments.

**18.12 Severability.** If any provision of this Agreement is held to be invalid, illegal, or unenforceable, the remaining provisions remain in full force and effect, and the invalid provision shall be reformed to the minimum extent necessary to make it valid, legal, and enforceable while preserving the Parties' original intent. If reformation is not possible, the provision shall be severed.

**18.13 Counterparts; electronic signatures.** This Agreement and each Order Form may be executed in counterparts, each of which is an original and all of which together constitute one instrument. Signatures delivered by electronic means (including DocuSign, Adobe Sign, or PDF email) are valid and binding. The Parties consent to electronic signatures and electronic records under the U.S. ESIGN Act, the Uniform Electronic Transactions Act, and Regulation (EU) 910/2014 (eIDAS), and shall not contest the validity of an electronic signature solely because it is electronic.

**18.14 Governing law.** This Agreement is governed by the laws of {{Governing Law}}, without regard to its conflict-of-laws principles. The United Nations Convention on Contracts for the International Sale of Goods does not apply.

**18.15 Forum and dispute resolution.** The Parties shall attempt in good faith to resolve any dispute arising out of or relating to this Agreement through escalation to senior executives of each Party for at least thirty (30) days before initiating formal proceedings. Thereafter:

(a) **Default forum:** The courts located in {{Forum}} have exclusive jurisdiction, and each Party waives any objection to venue or forum non conveniens.

(b) **OPTIONAL — only if the Order Form selects arbitration:** The dispute shall be finally resolved by binding arbitration administered by {{Arbitration Body}} (default the International Chamber of Commerce or the American Arbitration Association under its Commercial Arbitration Rules) under the rules in effect at the time of filing, by a single arbitrator, seated in {{Arbitration Seat}}, conducted in English, with judgment on the award entered in any court of competent jurisdiction. The arbitrator may not consolidate claims or arbitrate on a class basis without both Parties' consent.

(c) **Equitable relief carve-out:** Notwithstanding clauses (a) and (b), either Party may seek temporary or preliminary equitable relief in any court of competent jurisdiction to protect its intellectual property or Confidential Information.

(d) **Jury waiver (if available under the chosen law):** EACH PARTY KNOWINGLY, VOLUNTARILY, AND INTENTIONALLY WAIVES ANY RIGHT TO TRIAL BY JURY IN ANY ACTION ARISING OUT OF OR RELATING TO THIS AGREEMENT TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW.

**18.16 Headings; interpretation.** Section headings are for convenience only and do not affect interpretation. "Including" means "including without limitation." Singular includes plural and vice versa. References to "days" mean calendar days unless "business days" is specified. References to "Section" or "Exhibit" are to a section or exhibit of this Agreement unless otherwise stated.

**18.17 Publicity.** Other than the trademark license in Section 14.6, neither Party shall issue any press release, customer-success story, case study, or similar public statement referencing the other Party without the other Party's prior written consent.

**18.18 Order of precedence (cross-reference).** Section 2.3 controls conflicts among the documents that make up this Agreement.

---

## Exhibit A — Order Form (skeleton)

*This is a skeleton; the companion `legalcode-order-form` template is the full version. The Order Form on file controls.*

**Order Form No.:** `{{Order Form Number}}`
**Order Form Date:** `{{Order Form Date}}`
**Master Agreement:** Cloud Service Agreement dated `{{Effective Date}}` between Vendor and Customer.

**1. Parties.**
- Vendor: `{{Vendor Legal Name}}`
- Customer: `{{Customer Legal Name}}`
- Customer Affiliates covered: `{{Affiliate List}}`

**2. Cloud Service.**
- Product(s): `{{Product Names}}`
- Edition / SKU: `{{SKU}}`
- Hosting region: `{{Hosting Region}}`

**3. Subscription Scope.**
- Capacity unit: `{{Capacity Unit}}` (e.g., per-Authorized-User, per-tenant, per-API-call)
- Subscribed quantity: `{{Subscribed Users}}` / `{{Subscribed Capacity}}`
- Overage handling: `{{Overage Treatment}}`

**4. Term.**
- Start date: `{{Subscription Start Date}}`
- Initial Term: `{{Initial Term}}` (default 12 months)
- Renewal Term: `{{Renewal Term}}` (default 12 months, auto-renewing per Section 9.3 unless `{{Non-Renewal Notice Window}}` notice given)

**5. Fees.**
- Subscription Fee: `{{Subscription Fee}}` per `{{Billing Period}}`
- Setup / Implementation Fee: `{{Setup Fee}}`
- Usage / Overage rate: `{{Overage Rate}}`
- Discount(s) and ramp: `{{Discount Schedule}}`
- Total contract value: `{{TCV}}`

**6. Billing & payment.**
- Billing frequency: `{{Billing Frequency}}` (default annual in advance)
- Payment terms: `{{Payment Terms}}` (default Net 30)
- Currency: `{{Currency}}`
- Annual price-increase cap: `{{Annual Price Cap}}` (per Section 8.3 default)

**7. Contacts.**
- Vendor billing: `{{Vendor Billing Contact}}` / `{{Vendor Billing Email}}`
- Vendor notice: `{{Notice Email Vendor}}`
- Customer billing: `{{Customer Billing Contact}}` / `{{Billing Contact Email}}`
- Customer notice: `{{Notice Email Customer}}`
- Customer security contact: `{{Customer Security Contact}}`

**8. SLA.** Exhibit B / `legalcode-sla` applies, with `{{Uptime Commitment}}` (default 99.9%).

**9. DPA.** Exhibit C / `legalcode-dpa` applies if Customer Data includes personal data.

**10. Order-Form-specific overrides.** None, unless expressly listed below: `{{Express Overrides}}`.

**Signatures.** Authorized signature blocks for Vendor and Customer (electronic signatures permitted under Section 18.13).

---

## Exhibit B — Service Level Agreement (skeleton)

*This is a skeleton; the companion `legalcode-sla` template is the full version.*

**1. Uptime Commitment.** Vendor commits to a monthly uptime of `{{Uptime Commitment}}` (default 99.9%), measured as set forth below.

**2. Measurement.** Monthly uptime is calculated as `(Total Minutes − Downtime Minutes − Excluded Minutes) / (Total Minutes − Excluded Minutes)`, expressed as a percentage. "Downtime" means a period in which the production endpoint of the Cloud Service is unavailable to Customer's Authorized Users for more than `{{Continuous Downtime Threshold}}` (default five (5)) consecutive minutes, as confirmed by Vendor's monitoring or Customer's good-faith report.

**3. Exclusions.** Excluded from Downtime: (i) Scheduled Maintenance announced at least `{{Maintenance Notice Window}}` (default forty-eight (48) hours) in advance; (ii) Emergency Maintenance with as much notice as is reasonable; (iii) Force Majeure Events; (iv) failures attributable to Customer Data, Customer Materials, Customer-side configuration, Third-Party Services, or Customer's network; (v) Trials and beta features.

**4. Service credits.** If monthly uptime falls below the Uptime Commitment, Customer is entitled to credits as follows (illustrative; the companion `legalcode-sla` controls):

| Monthly uptime | Credit (% of monthly Fees) |
| --- | --- |
| < 99.9% but >= 99.0% | 10% |
| < 99.0% but >= 95.0% | 25% |
| < 95.0% | 50% |

**5. Support response.** Vendor shall respond to severity-tagged support requests within `{{Support Response P1}}` for Severity 1, `{{Support Response P2}}` for Severity 2, and `{{Support Response P3}}` for Severity 3, as further defined in `legalcode-sla`.

**6. Sole remedy.** Service credits are Customer's sole and exclusive remedy for any failure to meet the Uptime Commitment, except as provided in Section 10.3 of the CSA (right to terminate after `{{SLA Termination Threshold}}` consecutive months below the Uptime Commitment).

**7. Cross-reference.** The full SLA, including incident severity definitions, status-page commitments, support hours, and credit-claim procedure, is set forth in `legalcode-sla`.

---

## Exhibit C — Data Processing Agreement (cross-reference)

*Plain-language: Personal-data processing under this CSA is governed by the companion `legalcode-dpa`, incorporated by reference.*

The Data Processing Agreement (`legalcode-dpa`), as executed between the Parties or as published by Vendor and accepted by Customer's continued use of the Cloud Service, is incorporated into this CSA by reference and applies to all processing of personal data Customer (or its Authorized Users) submits to or generates within the Cloud Service. The DPA covers: roles (controller / processor by default; joint-controllership where expressly designated); processing instructions; Subprocessors and the Subprocessor change-notice mechanism; cross-border transfer mechanisms (EU SCCs, UK IDTA, Swiss addendum, and other recognized mechanisms `[VERIFY]` for Customer's jurisdiction); data-subject-rights cooperation; security and TOMs (Annex 2); personal-data-breach notification (within 72 hours of confirmed breach affecting personal data, see DPA §X `[VERIFY]`); audit rights (aligned with CSA Section 11.4); and post-termination return / deletion of personal data (aligned with CSA Section 6.4).

If there is a conflict between this CSA and the DPA on the processing of personal data, the DPA controls. If there is a conflict between the DPA and an Order Form on personal-data terms, the Order Form controls only where it expressly identifies the term as overriding the DPA.

---

## Exhibit D — Acceptable Use Policy (cross-reference)

*Plain-language: Use of the Cloud Service is governed by the companion `legalcode-aup`, incorporated by reference.*

The Acceptable Use Policy (`legalcode-aup`) at `{{AUP URL}}`, as updated from time to time, is incorporated into this CSA by reference. The AUP prohibits, among other things: (i) unlawful, infringing, or fraudulent use; (ii) transmission of malware, spam, or content that violates third-party rights; (iii) use that compromises the security, integrity, availability, or performance of the Cloud Service; (iv) circumvention of authentication or rate limits; (v) reverse engineering and competitive benchmarking (cross-reference Section 5.4); (vi) generation of content that violates child-safety, terrorism, or other prohibited-content rules; and (vii) high-risk uses (medical-decision support, weapons systems, mass surveillance) absent express written authorization. Vendor may update the AUP on reasonable notice; material changes that increase Customer's compliance burden take effect at the start of the next Renewal Term unless Customer agrees to an earlier effective date or applicable law requires earlier compliance. Vendor may suspend or terminate per Section 9 for AUP breach.

---

## Appendix 1 — Merge fields used

| Merge field | Description | Default |
| --- | --- | --- |
| `{{Vendor Legal Name}}` | Vendor's full legal name | — |
| `{{Vendor Entity Type}}` | Vendor's entity form (Inc., GmbH, ehf., LLC, etc.) | — |
| `{{Vendor Jurisdiction}}` | Vendor's jurisdiction of organization | — |
| `{{Vendor Address}}` | Vendor's principal place of business | — |
| `{{Customer Legal Name}}` | Customer's full legal name | — |
| `{{Customer Entity Type}}` | Customer's entity form | — |
| `{{Customer Jurisdiction}}` | Customer's jurisdiction of organization | — |
| `{{Customer Address}}` | Customer's principal place of business | — |
| `{{Effective Date}}` | CSA effective date | first Order Form date |
| `{{Documentation URL}}` | URL for product Documentation | — |
| `{{Affiliate List}}` | List of Customer Affiliates covered | — |
| `{{Subscribed Users}}` | Authorized-User cap | — |
| `{{Subscribed Capacity}}` | Capacity-based scope | — |
| `{{Overage Treatment}}` | How overage above Subscription Scope is billed | — |
| `{{Initial Term}}` | Length of Initial Term | 12 months |
| `{{Renewal Term}}` | Length of each Renewal Term | 12 months |
| `{{Non-Renewal Notice Window}}` | Days of notice to stop auto-renewal | 30 days |
| `{{Cure Period}}` | Days to cure material breach | 30 days |
| `{{Return Window}}` | Days post-termination to export Customer Data | 30 days |
| `{{Billing Frequency}}` | Invoicing cadence | annual in advance |
| `{{Billing Period}}` | Period covered by each invoice | matches Billing Frequency |
| `{{Payment Terms}}` | Days from invoice to payment due | Net 30 |
| `{{Late Fee Rate}}` | Interest on past-due amounts | 1.5% / month |
| `{{Annual Price Cap}}` | Cap on year-over-year price increase | 7% |
| `{{Subscription Fee}}` | Periodic fee | — |
| `{{Setup Fee}}` | One-time onboarding fee | — |
| `{{Overage Rate}}` | Per-unit overage rate | — |
| `{{Discount Schedule}}` | Ramp / discount detail | — |
| `{{TCV}}` | Total contract value | — |
| `{{Currency}}` | Billing currency | USD |
| `{{Billing Contact Email}}` | Customer billing email | — |
| `{{Vendor Billing Contact}}` | Vendor billing-contact name | — |
| `{{Vendor Billing Email}}` | Vendor billing email | — |
| `{{Notice Email Vendor}}` | Vendor notice email | — |
| `{{Notice Email Customer}}` | Customer notice email | — |
| `{{Customer Security Contact}}` | Customer security POC | — |
| `{{Hosting Region}}` | Cloud-Service hosting region | — |
| `{{Uptime Commitment}}` | Monthly uptime SLA | 99.9% |
| `{{Continuous Downtime Threshold}}` | Minutes that count as Downtime | 5 minutes |
| `{{Maintenance Notice Window}}` | Hours of maintenance notice | 48 hours |
| `{{Support Response P1}}` | Sev-1 response SLA | 1 hour |
| `{{Support Response P2}}` | Sev-2 response SLA | 4 business hours |
| `{{Support Response P3}}` | Sev-3 response SLA | 1 business day |
| `{{SLA Termination Threshold}}` | Consecutive months SLA missed before termination right | 3 months |
| `{{Breach Notification SLA}}` | Hours to notify confirmed Security Breach | 72 hours |
| `{{Liability Cap Multiplier}}` | Multiplier on 12 months Fees | 1.5x |
| `{{Liability Cap Floor}}` | Minimum liability cap | USD 100,000 |
| `{{CGL Limit}}` | Commercial general liability limits | USD 1M / 2M aggregate |
| `{{E&O Limit}}` | Professional / E&O liability limits | USD 5M |
| `{{Insurance Cyber Limit}}` | Cyber liability limits | USD 5M |
| `{{Governing Law}}` | Choice of law | — |
| `{{Forum}}` | Choice of forum | — |
| `{{Arbitration Body}}` | If arbitration elected | ICC or AAA |
| `{{Arbitration Seat}}` | Seat of arbitration | — |
| `{{Order Form Number}}` | Order Form identifier | — |
| `{{Order Form Date}}` | Order Form execution date | — |
| `{{Product Names}}` | Cloud-Service products covered | — |
| `{{SKU}}` | Edition / SKU | — |
| `{{Capacity Unit}}` | Unit of subscription scope | per-Authorized-User |
| `{{Subscription Start Date}}` | Order Form start date | — |
| `{{Express Overrides}}` | Order-Form-specific deviations from CSA | none |
| `{{AUP URL}}` | URL of the Acceptable Use Policy | — |

---

## Appendix 2 — Authoritative references

The following permissively-licensed baselines informed the structure of this template. No consecutive run of five or more words has been copied from any of them. Each is cited with its license tag.

- **Common Paper, Cloud Service Agreement v2.1** — `[CC-BY-4.0]`. Primary structural baseline for Master Agreement / Order Form decomposition, definitions, and standard terms.
- **Common Paper, Order Form** — `[CC-BY-4.0]`. Reference for Exhibit A skeleton.
- **Common Paper, AI Addendum** — `[CC-BY-4.0]`. Reference for Section 15 (AI & machine learning), including training-restriction posture and AI Output ownership patterns.
- **Bonterms, Cloud Terms** — `[CC-BY-4.0]`. Reference for cloud-specific operational language, suspension framework, and SLA cross-referencing.
- **Bonterms, Professional Services Agreement v1.2** — `[CC0]`. Reference for indemnity and insurance patterns adaptable to Cloud Services.
- **GitHub `site-policy`** — `[CC0]`. Reference for plain-language framing, acceptable-use cross-reference, and security/breach notification language.
- **Mozilla legal templates** — `[MPL-2.0]`. Reference for community-friendly disclaimer drafting and clean-room style.

`[VERIFY]` items in this draft:
- The Documentation URL placeholder, the AUP URL placeholder, the DPA-specific clause numbers in Exhibit C, and the recognized cross-border-transfer mechanisms appropriate to the Customer's jurisdiction. These should be confirmed against the live `legalcode-dpa` and `legalcode-aup` templates when this CSA is instantiated for a specific deal.

---

## Not legal advice

This template is a starting point for negotiating a Cloud Service Agreement. It is not legal advice and does not create an attorney-client relationship. Cloud and SaaS contracts vary by industry, jurisdiction, deal size, regulatory regime, and risk appetite, and the dual-perspective options provided here represent common positions rather than the only defensible ones. Before signing or sending this template, a Party should have a qualified attorney licensed in the relevant jurisdiction review the document in light of the specific commercial context, applicable laws (including data-protection, consumer-protection, sectoral, and export-control regimes), and the Party's own contracting policies. The author and Legalcode disclaim all liability for use of this template.
