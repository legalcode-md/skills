---
title: Cloud Service Agreement — Iceland (Lög nr. 7/1936 + EEA-imported DSA/Data Act/AI Act)
jurisdictions: [is]
statutes: [Lög-7/1936, Lög-16/2016, Lög-30/2002, Lög-90/2018, Lög-70/2022, AI-Act-via-EEA, Data-Act-via-EEA, NIS2-via-EEA]
supervisory_authority: Persónuvernd / Neytendastofa
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

> **Bilingual usage.** When the parties publish a parallel Icelandic-language version of this agreement (filed alongside as `is-isl.md`), the **Icelandic-language text controls** in any dispute, regulatory submission, or court proceeding. This English text is operative only as the parties' agreed working language for negotiation and day-to-day administration. Each Party shall record its full legal name, registered office, and Icelandic identification number (kennitala) in the Order Form (Pöntunarform). Required identifying fields:
>
> - **Vendor (Þjónustusala):** `{{Vendor Legal Name}}`, kennitala `{{Vendor Kennitala}}`, registered office `{{Vendor Address}}`
> - **Customer (Viðskiptamaður):** `{{Customer Legal Name}}`, kennitala `{{Customer Kennitala}}`, registered office `{{Customer Address}}`
> - **Persónuvernd registration (OPTIONAL — only if Vendor maintains a controller registration):** `{{Persónuvernd Registration Number}}`

---

## 1. Plain-language summary

This section explains, in everyday terms, what the rest of the agreement says. The Vendor (Þjónustusala) provides a cloud-based software service, and the Customer (Viðskiptamaður) pays subscription fees to use it. The Customer keeps ownership of the data it loads into the Service (Notendaefni); the Vendor keeps ownership of the underlying software and platform. Each side promises to keep the other's confidential information private (Trúnaðarupplýsingar). The Service is offered with a defined uptime commitment in the SLA, and personal data is processed according to the Data Processing Addendum at Exhibit C, which reflects the Icelandic Data Protection Act (Lög nr. 90/2018) and the EU General Data Protection Regulation as incorporated into the EEA Agreement.

This Cloud Service Agreement is intended for business-to-business use between commercial entities (Aðilar) established or operating in Iceland or in another EEA Member State. It is not designed for consumer transactions; where a Customer qualifies as a consumer under **Lög nr. 16/2016 um neytendasamninga**, separate consumer-facing terms must be used. The agreement is organised so a reader can understand the core deal in the first eight sections and then turn to specialised topics in later sections. Where Icelandic statutory terminology applies, the Icelandic term appears once in parentheses next to the English term. Where an obligation is imported from EU law via the EEA Joint Committee process, the clause is annotated `[VERIFY]` so a verifying lawyer can confirm current incorporation status before execution.

> Plain-language wrappers are explanatory; the operative text follows each summary.

## 2. Agreement structure (Master Agreement + Order Forms)

This section describes how the documents fit together. The agreement is a Master Agreement (rammasamningur) that covers the legal terms once, with one or more Order Forms (Pöntunarform) that record the specific things being purchased — modules, seat counts, pricing, term length. Either Party may sign more than one Order Form under this Master Agreement.

2.1 **Components.** This Cloud Service Agreement consists of (a) these master terms; (b) each executed Order Form (Pöntunarform); (c) Exhibit A (Service description and SLA); (d) Exhibit B (Acceptable Use Policy); (e) Exhibit C (Data Processing Addendum, IS variant); (f) Exhibit D (Security overview); and (g) any other addenda the Parties expressly incorporate in writing.

2.2 **Order of precedence.** In the event of conflict, documents control in the following order: (i) an executed Order Form (only as to its scope); (ii) Exhibit C (Data Processing Addendum); (iii) these master terms; (iv) Exhibits A, B, and D; (v) any Vendor policies referenced by URL. Nothing in a Vendor URL-referenced policy may reduce a Customer right granted in the master terms or in Exhibit C.

2.3 **Effectiveness.** This agreement becomes effective on the date of the first executed Order Form (the "Effective Date"). Each subsequent Order Form is itself effective on its own signature date and is governed by the master terms in force on that signature date, except that Exhibit C and the data-protection clauses always reflect the most recent version of Lög nr. 90/2018 and the GDPR as in force.

2.4 **Amendment.** The master terms may be amended only by a written instrument signed by both Parties. Order Forms may be amended by a signed change order or, where the Parties agree in writing, by an exchange of countersigned electronic documents per **eIDAS Regulation 910/2014 via the EEA Agreement** and **Lög nr. 28/2001 um rafrænar undirskriftir**.

2.5 **Affiliates.** A Customer Affiliate (tengdur aðili) may sign an Order Form referencing this Master Agreement; that Affiliate becomes the contracting Customer for that Order Form, and the entity that signed the master terms acts as guarantor of the Affiliate's payment obligations unless the Order Form expressly says otherwise.

## 3. Definitions

This section defines the key terms used throughout. Each English term is followed, on first use, by the corresponding Icelandic statutory term.

3.1 "**Affiliate**" (tengdur aðili) means an entity that controls, is controlled by, or is under common control with a Party, where "control" means more than 50% of voting equity or the power to direct management.

3.2 "**Aðili / Party**" means either the Vendor or the Customer; "**Aðilar / Parties**" means both.

3.3 "**Confidential Information**" (Trúnaðarupplýsingar) means non-public information disclosed by one Party to the other that is marked confidential or that a reasonable recipient would understand to be confidential given its nature and the circumstances of disclosure.

3.4 "**Customer Data**" (Notendaefni) means any data, content, or material that the Customer or its Authorised Users submit to, or generate within, the Service, including Customer Personal Data as defined in Exhibit C.

3.5 "**Customer Materials**" (Notendaefni — efnislegt) means any materials (other than Customer Data) that the Customer provides to the Vendor for use in connection with the Service.

3.6 "**Documentation**" (skjölun) means the user-facing technical documentation that the Vendor publishes for the Service.

3.7 "**Effective Date**" (gildistökudagur) has the meaning given in §2.3.

3.8 "**Fees**" (þóknun) means the amounts payable for the Service as set out in an Order Form.

3.9 "**Order Form**" (Pöntunarform) means a written ordering document executed by both Parties that references this agreement and identifies the Services purchased, the quantities, the pricing, and the term.

3.10 "**Personal Data**" (persónuupplýsingar) has the meaning given in Article 4(1) of the GDPR as incorporated into the EEA Agreement and as transposed by **Lög nr. 90/2018 um persónuvernd og vinnslu persónuupplýsinga**.

3.11 "**Service**" (Þjónusta) means the cloud service identified in the applicable Order Form, including the Documentation and any Updates.

3.12 "**Service Level Agreement**" or "**SLA**" (þjónustustigssamningur) means the availability and support commitments set out in Exhibit A.

3.13 "**Subscription Term**" (áskriftartímabil) means the period set out in an Order Form during which the Customer is entitled to access and use the Service.

3.14 "**Vendor**" (Þjónustusala) means the entity identified as such on the Order Form.

3.15 "**Customer**" (Viðskiptamaður) means the entity identified as such on the Order Form.

3.16 "**EEA Joint Committee Decision**" means a decision of the Joint Committee of the EEA Agreement that incorporates an EU instrument into the EEA legal framework and thereby into Icelandic law.

3.17 Other defined terms appear inline and are capitalised on first use.

## 4. Use of the Service

This section says what the Customer may do with the Service. The Vendor grants the Customer a right to use the Service for its internal business operations during the Subscription Term, in accordance with the Documentation, the Acceptable Use Policy at Exhibit B, and applicable law.

4.1 **Right of use.** The Vendor grants the Customer a non-exclusive, non-transferable, non-sublicensable right to access and use the Service during the Subscription Term solely for the Customer's internal business purposes and those of its Authorised Users.

4.2 **Authorised Users.** The Customer may permit its employees, contractors, and Affiliates to use the Service as Authorised Users, provided that (a) each Authorised User is bound by use restrictions at least as protective as those in this agreement; (b) the Customer remains responsible for each Authorised User's acts and omissions; and (c) the number of Authorised Users does not exceed any seat or volume limit recorded on the Order Form.

4.3 **Updates.** The Vendor may issue Updates to the Service from time to time. The Vendor will not materially reduce the core functionality described in the Order Form during a Subscription Term without the Customer's prior written consent or unless required by law or by an order of a competent authority.

4.4 **Service availability.** Availability and support commitments are governed by Exhibit A.

4.5 **Audit log access.** The Customer is entitled to access the audit logs generated by its own use of the Service for the duration of the Subscription Term and for the export period set out in §6.

## 5. Customer responsibilities & restrictions

This section says what the Customer must and must not do. The Customer is responsible for its own users, its own content, and for following Icelandic and EEA laws when using the Service.

5.1 **General restrictions.** The Customer shall not, and shall not permit any third party to: (a) reverse-engineer, decompile, or disassemble the Service except to the extent permitted by mandatory law (including **Lög nr. 73/1972 um höfundarétt**); (b) use the Service to develop a competing product; (c) bypass any usage limit; (d) remove proprietary notices; or (e) use the Service for any unlawful purpose.

5.2 **Acceptable use.** The Customer shall comply with the Acceptable Use Policy at Exhibit B.

5.3 **Sanctions compliance.** The Customer represents and warrants that, in connection with its use of the Service, it shall comply with **Lög nr. 96/2016 um þvingunaraðgerðir alþjóðlegra stofnana** (the Icelandic Act on Implementation of International Sanctions), with the related implementing regulations issued by the Ministry for Foreign Affairs, and with applicable EEA, EU, and UN restrictive measures. The Customer shall not use the Service in or for the benefit of any country, person, or entity subject to comprehensive sanctions, and shall not use the Service to make available any item, technology, or service that is subject to Icelandic or EEA export controls without the required authorisation.

5.4 **Anti-money-laundering.** The Customer shall comply with **Lög nr. 64/2019 um varnir gegn peningaþvætti og fjármögnun hryðjuverka** (the Icelandic Anti-Money-Laundering and Counter-Terrorism-Financing Act) to the extent applicable to the Customer's own business, and shall not use the Service to facilitate any activity prohibited under that Act.

5.5 **Anti-bribery.** The Customer shall comply with **Almenn hegningarlög nr. 19/1940**, sections 109 and 264a (bribery and corruption offences), and with any applicable foreign anti-bribery laws (including the UK Bribery Act 2010 where the Customer's operations bring it into scope).

5.6 **Whistleblower protection.** The Customer shall not retaliate against any person who reports, in good faith, a suspected breach of law arising from use of the Service, consistent with **Lög nr. 40/2020 um vernd uppljóstrara** `[VERIFY current title and number — Iceland's Whistleblower Protection Act has been amended; confirm 40/2020 is the current operative number at execution]`.

5.7 **Customer infrastructure.** The Customer is responsible for providing and maintaining the network connectivity, end-user devices, and credentials needed to access the Service.

5.8 **Account credentials.** The Customer shall safeguard its account credentials, shall require multi-factor authentication where the Service offers it, and shall promptly notify the Vendor of any suspected unauthorised access.

## 6. Customer Data

This section explains who owns the Customer's data, how the Vendor may use it, and what happens to it when the agreement ends. The Customer keeps ownership of its data; the Vendor only processes it to provide and improve the Service consistent with this agreement and Exhibit C.

6.1 **Ownership.** As between the Parties, the Customer retains all right, title, and interest in and to the Customer Data, including all Customer Personal Data.

6.2 **Limited licence to Vendor.** The Customer grants the Vendor a non-exclusive, worldwide, royalty-free licence to host, copy, transmit, display, and process the Customer Data solely as required to (a) provide and maintain the Service; (b) prevent or address technical or security issues; (c) comply with the Customer's documented instructions; and (d) comply with applicable law. This licence terminates on the deletion of the Customer Data in accordance with §6.5.

6.3 **Personal data.** Where the Customer Data includes Personal Data, the processing of that Personal Data is governed by the Data Processing Addendum at Exhibit C, which reflects Articles 28 and 32 of the GDPR as incorporated into the EEA Agreement and as transposed by **Lög nr. 90/2018 um persónuvernd og vinnslu persónuupplýsinga**, and is supervised by **Persónuvernd**.

6.4 **Data portability and switching (Data Act).** Subject to verification of the EEA Joint Committee Decision incorporating **Regulation (EU) 2023/2854 (the Data Act)** into the EEA Agreement and of Iceland-specific transposition `[VERIFY EEA Joint Committee Decision and IS transposition]`, the Vendor shall:

  (a) make the Customer Data available to the Customer in a structured, commonly used, and machine-readable format on request during the Subscription Term and for the export period set out in §6.5;

  (b) facilitate the Customer's switch to another provider of an equivalent service, including by providing reasonable cooperation and the technical interfaces and metadata necessary for switching, consistent with **Articles 23 to 25 of the Data Act**;

  (c) not impose unreasonable contractual, technical, or commercial obstacles to switching; and

  (d) not charge switching fees beyond those expressly permitted by the Data Act and only for the period during which such fees remain permitted.

6.5 **Export and deletion at end of Subscription Term.** During the Subscription Term and for `{{Export Window — default 30 days}}` after expiry or termination, the Vendor shall make the Customer Data available for export in the format described in Exhibit A. After that period, the Vendor shall delete the Customer Data within `{{Deletion Window — default 90 days}}`, except where retention is required by law, by Exhibit C, or for back-up rotation that is itself subject to deletion.

> **Dual-perspective drafting note (§6).** A Vendor-favourable revision narrows §6.2(b) to "service operation and security incident response" and adds a Customer-borne fee for non-standard export formats. A Customer-favourable revision broadens §6.4 to extend Data Act switching support beyond the Subscription Term and removes any switching-related charge.

## 7. Confidentiality

This section requires each Party to keep the other's non-public information secret. Confidential information may only be used to perform the agreement and may not be shared except as the agreement allows.

7.1 **Obligations.** Each Party (the "Recipient") shall (a) use the other Party's Confidential Information only to perform this agreement; (b) protect it with at least the degree of care it uses for its own confidential information of similar importance, and never less than reasonable care; and (c) limit access to those of its personnel, advisers, and contractors who need to know and who are bound by written confidentiality obligations no less protective than this section.

7.2 **Exclusions.** Confidential Information does not include information that the Recipient can show is (a) publicly available without breach of this agreement; (b) already known to the Recipient without confidentiality restriction before disclosure; (c) independently developed by the Recipient without use of the other Party's Confidential Information; or (d) lawfully obtained from a third party without confidentiality restriction.

7.3 **Compelled disclosure.** If the Recipient is required by law, court order, or competent authority to disclose Confidential Information, it shall (where lawful) give the disclosing Party prompt notice and reasonable cooperation so the disclosing Party may seek a protective order.

7.4 **Trade secrets.** The Parties acknowledge that some Confidential Information may also qualify as a trade secret protected under **Directive (EU) 2016/943 on trade secrets** as incorporated into the EEA Agreement and as transposed into Icelandic law. Nothing in this section limits the additional remedies available for trade-secret misappropriation under that regime.

7.5 **Survival.** Confidentiality obligations survive termination for `{{Confidentiality Survival — default 5 years}}` and indefinitely for items that qualify as trade secrets, until they cease to qualify as such.

## 8. Fees, billing, taxes

This section explains how money flows. Fees are set on the Order Form, are payable in the currency stated there, and are subject to Icelandic VAT (VSK) where applicable.

8.1 **Fees.** The Customer shall pay the Fees as recorded on the Order Form. Unless the Order Form says otherwise, Fees are stated in `{{Currency — default ISK}}` and are exclusive of taxes.

8.2 **Invoicing.** The Vendor shall invoice the Customer in accordance with the Order Form. Unless the Order Form says otherwise, invoices are payable within `{{Payment Term — default 30 days}}` of the invoice date.

8.3 **Disputed amounts.** The Customer may withhold payment of an amount it disputes in good faith, provided that it (a) pays the undisputed portion when due; (b) gives the Vendor written notice of the dispute within ten (10) business days of the invoice date; and (c) cooperates in good faith to resolve the dispute.

8.4 **Price changes.** The Vendor may increase the Fees applicable to a renewal Subscription Term by giving the Customer not less than `{{Price-Change Notice — default 60 days}}` written notice before the start of the renewal term. A price increase exceeding `{{Price-Increase Cap — default 7%}}` over the immediately preceding term entitles the Customer to terminate the affected Order Form by written notice given before the start of the renewal term.

8.5 **Consumer-contract carve-out.** This agreement is intended for business-to-business use. **Lög nr. 16/2016 um neytendasamninga** applies only where the Customer qualifies as a consumer (neytandi) within the meaning of that Act. A Customer that is acting wholly or mainly within its trade, business, craft, or profession is generally not within the scope of the Consumer Contracts Act, and the consumer-protection rules in that Act do not apply to this agreement.

8.6 **Late payment interest.** Late payments accrue interest in accordance with **Lög nr. 38/2001 um vexti og verðtryggingu** (the Act on Interest and Indexation) at the rate prescribed for commercial debts, calculated from the due date until payment is received `[VERIFY current statutory rate at execution; the Central Bank of Iceland publishes the applicable rate periodically]`. Interest is computed on a daily basis and capitalised monthly. The Vendor may also recover reasonable costs of collection to the extent permitted by law.

8.7 **VAT and indirect taxes.** Fees are exclusive of value-added tax (virðisaukaskattur, VSK / MOMS). Where Icelandic VAT is chargeable, the Vendor shall add VAT at the applicable rate and issue a tax-compliant invoice consistent with **Lög nr. 50/1988 um virðisaukaskatt**. For cross-border B2B supplies of electronically supplied services within the EEA, the reverse-charge mechanism applies as transposed from the EU VAT Directive (originally the Sixth Directive — Sjötta tilskipun), and the Customer shall account for VAT in its own jurisdiction where required. Each Party is responsible for its own income, corporation, and similar taxes.

8.8 **Withholding tax.** If the Customer is required by law to withhold tax on Fees, it shall (a) gross up the payment so that the Vendor receives the amount it would have received absent the withholding, except where a double-tax treaty between Iceland and the Customer's jurisdiction permits a reduced rate on submission of a valid certificate of residence; and (b) provide the Vendor with the official tax receipt within thirty (30) days of withholding.

> **Dual-perspective drafting note (§8).** A Vendor-favourable revision shortens the payment term, removes the disputed-amounts withhold right, and applies a higher late-payment uplift. A Customer-favourable revision extends the payment term, requires line-item invoices, and caps annual Fee escalations to a published consumer price index figure published by Hagstofa Íslands.

## 9. Term, renewal, termination & suspension

This section explains how long the agreement lasts, how it renews, and how each side may end it. Termination must be in writing; suspension is reserved for serious situations.

9.1 **Term.** This agreement starts on the Effective Date and continues until all Order Forms have expired or been terminated.

9.2 **Order Form term and renewal.** Each Order Form has the Subscription Term stated on it. Unless the Order Form says otherwise, an Order Form auto-renews for successive `{{Renewal Term — default 12 months}}` periods, unless a Party gives written notice of non-renewal at least `{{Renewal Notice — default 60 days}}` before the end of the then-current term.

9.3 **Termination for cause.** Either Party may terminate this agreement or any Order Form by written notice if the other Party (a) commits a material breach and fails to cure it within thirty (30) days of written notice; (b) becomes insolvent, enters into a composition with creditors, or has a winding-up order made against it (gjaldþrotaúrskurður) under **Lög nr. 21/1991 um gjaldþrotaskipti**; or (c) ceases or threatens to cease doing business.

9.4 **Effects of termination.** On termination, (a) the Customer's right to access the Service ends; (b) all unpaid Fees for the unexpired portion of the Subscription Term, where the Customer terminates other than for Vendor breach, become immediately due; (c) the Vendor shall provide data export and deletion as set out in §6.5; and (d) clauses that by their nature should survive (including confidentiality, IP, payment, indemnity, liability, and dispute resolution) survive.

9.5 **Unconscionability flag (Lög nr. 7/1936 § 36).** The Parties acknowledge that under **§ 36 of Lög nr. 7/1936 um samningsgerð, umboð og ógilda löggerninga** (the Contracts Act), an Icelandic court may set aside or modify a contract term if it is unreasonable to invoke the term (ósanngjarnt að bera þá fyrir sig). The threshold for B2B unconscionability is materially higher than for B2C, but a court may still review terms governing termination, renewal length, and post-termination data handling. The Parties have negotiated this agreement at arm's length and consider §§ 9.2 and 9.4 to be reasonable in light of the commercial bargain. Either Party may seek judicial review under § 36 in accordance with applicable law.

9.6 **Switching and exit assistance (Data Act).** On termination, in addition to §6.5, the Vendor shall provide the switching support required by **Articles 23 to 25 of the Data Act (Regulation (EU) 2023/2854) as incorporated into the EEA Agreement** `[VERIFY transposition]`, including reasonable cooperation, interface documentation, and the metadata necessary for the Customer to migrate to another provider.

9.7 **Suspension.** The Vendor may suspend the Service, in whole or in part and on prior written notice where reasonably practicable, if (a) the Customer's use poses an imminent security risk to the Service or to other customers; (b) the Customer's use is in material breach of the Acceptable Use Policy and the Customer has failed to cure within five (5) business days of notice; (c) the Vendor is required to suspend by law or by an order of a competent authority; or (d) Fees remain materially overdue and unpaid for more than thirty (30) days after a written demand. Suspension under (d) does not relieve the Customer of its payment obligations.

> **Dual-perspective drafting note (§9).** A Vendor-favourable revision shortens cure periods, broadens the suspension grounds, and applies post-termination access fees. A Customer-favourable revision lengthens cure periods, requires the Vendor to maintain an export-only mode for ninety (90) days after suspension, and limits suspension solely to imminent security risk.

## 10. Service Level Agreement

This section sets the basic service-availability commitment. Detailed metrics and credits are in Exhibit A.

10.1 **Availability commitment.** The Vendor shall use commercially reasonable efforts to make the Service available at least `{{Uptime Commitment — default 99.9%}}` of each calendar month, measured as set out in Exhibit A.

10.2 **Service credits.** Where the Vendor fails to meet the availability commitment, the Customer's exclusive remedy is the service-credit schedule in Exhibit A, except in the case of (a) a Vendor breach of Exhibit C; or (b) liability that cannot be excluded under §16.6.

10.3 **Exclusions.** The availability commitment excludes downtime caused by (a) scheduled maintenance announced in accordance with Exhibit A; (b) emergency security maintenance; (c) Customer-side issues, including network or device faults; (d) force majeure events under §18.3; and (e) third-party services not under the Vendor's control.

10.4 **Reporting.** The Vendor shall provide quarterly availability reporting and shall make the underlying measurement methodology available to the Customer on reasonable request.

## 11. Security & data protection

This section sets the security and privacy floor. Personal-data processing details are in Exhibit C.

11.1 **Security programme.** The Vendor shall maintain an information-security programme that is reasonable in light of the nature of the Service and the categories of Customer Data processed, and that is consistent with the security overview at Exhibit D.

11.2 **Notification of security incidents.** The Vendor shall notify the Customer without undue delay, and in any event consistent with the timescales in Exhibit C, of any confirmed Personal Data Breach affecting Customer Personal Data.

11.3 **Pen tests and audits.** Once per twelve-month period, on at least thirty (30) days' notice, the Customer (or its independent auditor bound by confidentiality) may audit the Vendor's compliance with this section, subject to the audit-cooperation provisions in Exhibit C.

11.4 **Sub-processors.** The Vendor may engage sub-processors consistent with Exhibit C and shall remain responsible for their acts and omissions.

11.5 **GDPR baseline.** Personal Data is processed in accordance with **Article 32 of the GDPR** as incorporated into the EEA Agreement and **Article 27 of Lög nr. 90/2018**, and consistent with the technical and organisational measures described in Exhibit C.

11.6 **NIS2 (Directive (EU) 2022/2555).** Where either Party is an "essential" or "important" entity within the meaning of **Directive (EU) 2022/2555** as incorporated into the EEA Agreement and transposed into Icelandic law `[VERIFY EEA incorporation and IS transposition]`, that Party shall (a) comply with the cybersecurity risk-management and incident-notification requirements applicable to it; and (b) cooperate reasonably with the other Party's compliance, including by providing information needed to satisfy supply-chain risk obligations under Article 21(2)(d) of NIS2.

11.7 **DORA (Regulation (EU) 2022/2554).** Where the Customer is a financial entity supervised by **Fjármálaeftirlitið (FME)** or another EEA competent authority and the Service qualifies as an information and communication technology service to that entity, the **Digital Operational Resilience Act** as incorporated into the EEA Agreement and transposed into Icelandic law applies `[VERIFY EEA incorporation and IS transposition]`. The Parties shall execute the DORA addendum at Exhibit C-1 (where applicable) to record the contractual provisions required by Article 30 of DORA, including audit rights, exit strategies, and incident-reporting interfaces.

11.8 **Independent assurance.** The Vendor shall maintain at least one of the following during the Subscription Term: (a) a current **ISO/IEC 27001** certification covering the Service; or (b) a current **SOC 2 Type II** report covering the Service. The Vendor shall make the relevant certificate or report available to the Customer under confidentiality on reasonable request.

11.9 **Persónuvernd notification.** Where the Vendor acts as the Customer's processor, the Vendor shall provide the information needed to enable the Customer (as controller) to notify Persónuvernd of a Personal Data Breach within seventy-two (72) hours of becoming aware of the breach, consistent with Article 33 of the GDPR and Article 28 of Lög nr. 90/2018.

> **Dual-perspective drafting note (§11).** A Vendor-favourable revision narrows audit rights to questionnaire-based assurance with site visits only after a confirmed breach. A Customer-favourable revision adds an explicit right to receive penetration-test executive summaries and to require remediation timelines for findings rated high or critical.

## 12. Trials & beta features

This section says that trials and beta features are offered "as is" and may be withdrawn. Production reliance on a beta feature is at the Customer's risk.

12.1 **Trials.** The Vendor may offer the Service or specified modules on a free or evaluation basis for a stated period. Trials are provided "as is" and "as available", with no SLA, no warranty (other than as required by mandatory law), and no liability beyond the cap in §16.5.

12.2 **Beta features.** A Vendor-designated beta, preview, or early-access feature is provided for evaluation and may be modified, restricted, or withdrawn at any time. The Customer shall not place a beta feature into a production-critical workflow without an express written acknowledgment that it does so at its own risk.

12.3 **Feedback.** Where the Customer voluntarily provides feedback on a trial or beta feature, the Vendor may use that feedback on a non-exclusive, royalty-free, perpetual basis, provided that the feedback is not used in a way that identifies the Customer or its users without consent.

## 13. Third-party services & integrations

This section makes clear that third-party services are governed by their own terms and that the Vendor is not responsible for their performance.

13.1 **Customer-selected integrations.** Where the Customer enables an integration with a third-party service (a "Third-Party Service"), the Customer authorises the Vendor to exchange the data necessary to operate that integration. The Customer's relationship with the Third-Party Service is governed by the Third-Party Service's own terms, and the Vendor is not responsible for the Third-Party Service.

13.2 **Vendor-bundled third-party components.** Where the Vendor bundles a third-party component as part of the Service, the Vendor remains responsible for that component as part of the Service, except to the extent the component's licence terms (such as an open-source licence) flow through to the Customer; in that case, the licence terms are made available in Exhibit A.

13.3 **Marketplace listings.** A listing in a Vendor marketplace does not constitute an endorsement by the Vendor unless expressly stated.

## 14. Intellectual property

This section sets ownership: the Vendor owns the Service; the Customer owns its Customer Data; each side keeps its pre-existing IP.

14.1 **Vendor IP.** As between the Parties, the Vendor retains all right, title, and interest in the Service, the Documentation, and all related intellectual property, including all derivative works and improvements, subject only to the licence to use granted in §4.1.

14.2 **Customer IP.** As between the Parties, the Customer retains all right, title, and interest in the Customer Data and the Customer Materials, subject only to the licence granted in §6.2.

14.3 **Icelandic copyright.** The Service and the Documentation are protected as literary works under **Lög nr. 73/1972 um höfundarétt** (the Icelandic Copyright Act), and any reproduction or adaptation requires the Vendor's authorisation except as permitted by mandatory exceptions in that Act.

14.4 **Patents.** Nothing in this agreement transfers ownership of any patent. The Vendor's grant of patent rights, if any, is limited to those patents the Vendor owns or controls and that are necessarily infringed by the Customer's permitted use of the Service in accordance with the Documentation; this is consistent with **Lög nr. 17/1991 um einkaleyfi**.

14.5 **Trade secrets.** Trade secrets are protected as set out in §7.4 and under **Directive (EU) 2016/943** as incorporated into the EEA Agreement and transposed into Icelandic law.

14.6 **Trade marks.** Each Party retains its trade marks. Neither Party may use the other Party's name, logo, or trade marks without prior written consent, except that the Vendor may list the Customer's name and logo in a public customer list unless the Customer opts out by written notice.

## 15. AI & machine learning

This section says how AI features in the Service work, who owns AI Output, and the limits of relying on AI.

15.1 **No training on Customer Data.** Unless the Customer expressly opts in by signed written instrument, the Vendor shall not use Customer Data, Customer Materials, or Customer prompts to train, fine-tune, or otherwise improve any AI model that is offered to other customers or to the public. Aggregated, irreversibly de-identified service telemetry is permitted to the extent it cannot reasonably be linked to the Customer or to any natural person.

15.2 **Use of third-party models.** Where the Service uses a third-party foundation model, the Vendor shall identify the model provider and the high-level data-handling posture in Exhibit A or in the Documentation, and shall flow down the no-training-on-Customer-Data commitment in §15.1 in its agreement with the model provider, except where mandatory law or the model provider's audited posture already prohibits training on inference inputs.

15.3 **Human oversight.** AI features that produce outputs intended to be acted on (such as classifications, recommendations, or generated text) shall be designed to allow a human user to review, edit, or override the output before it is used.

15.4 **Logging.** Where the Service offers a generative-AI feature, the Vendor shall maintain reasonable logs of prompts and outputs sufficient to support security investigations and the Customer's compliance obligations, subject to retention limits set out in Exhibit C.

15.5 **Documentation of capabilities.** The Vendor shall describe the intended purpose, known limitations, and material residual risks of any AI feature in Exhibit A or in the Documentation.

15.6 **EU AI Act (Regulation (EU) 2024/1689) via the EEA Agreement.** Subject to verification of the EEA Joint Committee Decision incorporating **Regulation (EU) 2024/1689 (the AI Act)** into the EEA Agreement and to Iceland-specific transposition and commencement `[VERIFY EEA Joint Committee Decision and Iceland-specific commencement]`:

  (a) **Article 5 — prohibited practices.** The Vendor shall not place on the market, put into service, or use any AI system that engages in a practice prohibited by Article 5, and the Customer shall not use the Service in a manner that would constitute such a prohibited practice.

  (b) **Article 6 — high-risk classification.** Where the Service or a feature of the Service falls within a high-risk classification under Article 6 and Annex III, the Parties shall execute a high-risk addendum at Exhibit A allocating the obligations of the provider, deployer, importer, and distributor as defined in the AI Act.

  (c) **Article 50 — transparency for AI interacting with humans.** Where an AI feature interacts directly with end users, the Vendor shall implement disclosures so end users are informed they are interacting with an AI system, except where this is obvious from the circumstances or is otherwise excused by Article 50.

  (d) **Article 13 — transparency for high-risk.** For any high-risk feature, the Vendor shall provide the Customer (as deployer) with the information required by Article 13 to enable the Customer to interpret and use the output appropriately.

  (e) **Article 25 — GPAI obligations.** Where the Service uses a general-purpose AI model, the Vendor shall comply with the obligations applicable to providers and deployers of general-purpose AI models under Article 25 and the related provisions of Chapter V, including reasonable transparency about training-data summaries to the extent required.

15.7 **Customer prompt warranty.** The Customer represents and warrants that prompts and inputs it submits to AI features of the Service shall comply with applicable Icelandic law and EEA law, including (without limitation) **Lög nr. 73/1972 um höfundarétt**, **Lög nr. 90/2018** and the GDPR, **Almenn hegningarlög nr. 19/1940**, and the AI Act prohibitions in §15.6(a).

15.8 **Ownership of AI Output.** As between the Parties and to the extent any AI Output is eligible for protection under Icelandic law, the Customer owns the AI Output that is generated for the Customer through its use of the Service, subject to (a) the Vendor's underlying rights in the Service and the model; (b) any third-party rights in inputs or training material; and (c) the limitations imposed by Icelandic and EEA copyright law on protectability of AI-generated content.

15.9 **No-warranty for AI Output.** The Customer acknowledges that AI features can produce inaccurate, biased, or otherwise unsuitable output. AI Output is not a substitute for professional advice. The Customer shall not rely on AI Output for medical, legal, financial, safety-critical, or other regulated decisions without independent human review by a qualified professional. Use of AI Output is at the Customer's own risk and is subject to the warranty disclaimers and liability limits in §16.

> **Dual-perspective drafting note (§15).** A Vendor-favourable revision narrows §15.1 to permit aggregated abuse-detection training and adds a Customer indemnity for unlawful prompts. A Customer-favourable revision tightens §15.1 to a flat no-training prohibition, requires written notice before any model substitution, and obliges the Vendor to maintain a documented evaluation and red-teaming programme for AI features.

## 16. Warranties, disclaimers & limitations of liability

This section sets out what each Party promises about the Service, what is disclaimed, and the cap on damages. Mandatory Icelandic law cannot be excluded.

16.1 **Mutual warranties.** Each Party warrants that (a) it has authority to enter into this agreement; (b) its execution and performance do not violate any other agreement to which it is a party; and (c) it shall comply with applicable law in performing under this agreement.

16.2 **Vendor service warranty.** The Vendor warrants that, during the Subscription Term, the Service will perform in material conformity with the Documentation. The Customer's exclusive remedy for breach of this warranty (and the Vendor's sole liability) is, at the Vendor's option, (a) re-performance of the deficient functionality; or (b) termination of the affected Order Form and a pro-rata refund of pre-paid Fees attributable to the deficient period.

16.3 **Disclaimer.** Except as expressly set out in this agreement, the Service is provided "as is" and "as available". The Vendor disclaims all other warranties, whether express, implied, or statutory, including warranties of merchantability, fitness for a particular purpose, non-infringement, and uninterrupted or error-free operation, in each case to the maximum extent permitted by law.

16.4 **Consumer-warranty carve-out (Lög nr. 16/2016).** Statutory consumer-warranty rights under **Lög nr. 16/2016 um neytendasamninga** apply only where the Customer qualifies as a consumer. A Customer that is not a consumer cannot rely on those rights.

16.5 **Liability cap.** Subject to §16.6, each Party's aggregate liability under this agreement (in contract, tort, statute, or otherwise) is capped at the greater of (a) the Fees paid or payable by the Customer to the Vendor in the twelve (12) months immediately preceding the event giving rise to liability; and (b) `{{Liability Cap Floor — default ISK 15,000,000 (approximately EUR 100,000)}}`. Neither Party is liable for indirect, special, consequential, or exemplary damages, lost profits, lost revenue, lost goodwill, or loss of data (other than the cost of restoring data from the most recent back-up where the Vendor was contractually responsible for the back-up).

16.6 **Mandatory carve-outs (Icelandic mandatory law).** Nothing in this agreement excludes or limits liability that cannot be excluded or limited under Icelandic mandatory law, including liability for (a) fraud or fraudulent misrepresentation; (b) gross negligence (stórfellt gáleysi); (c) wilful misconduct (ásetningur); (d) death or personal injury caused by negligence; or (e) any other liability that mandatory Icelandic law prohibits a Party from excluding.

16.7 **Unconscionability flag (§ 36 of Lög nr. 7/1936).** As noted in §9.5, an Icelandic court may set aside or modify a contract term under **§ 36 of Lög nr. 7/1936** (Contracts Act) if the term is unreasonable to invoke (the doctrine of ósanngirnis). The Parties acknowledge the liability cap and disclaimers in this section reflect the commercial bargain and the price; either Party retains the statutory right to seek judicial review under § 36.

16.8 **Dependent obligations.** The liability cap does not apply to the Customer's obligation to pay undisputed Fees.

> **Dual-perspective drafting note (§16).** A Vendor-favourable revision keeps a single 12-month-Fees cap, broadens the consequential-loss exclusion, and adds a ninety-day claim-notification deadline. A Customer-favourable revision adds a super-cap (commonly 2× the cap) for confidentiality and Exhibit C breaches and removes the consequential-loss exclusion for IP-indemnity claims.

## 17. Indemnification & insurance

This section sets out who covers what in third-party claims, plus minimum insurance levels.

17.1 **Vendor IP indemnity.** The Vendor shall defend the Customer against any third-party claim alleging that the Customer's use of the Service in accordance with this agreement infringes a third party's intellectual-property right, and shall indemnify the Customer for damages and reasonable costs finally awarded by a competent court or agreed in settlement, subject to §17.3 and §17.4.

17.2 **Customer indemnity.** The Customer shall defend the Vendor against any third-party claim arising out of (a) Customer Data or Customer Materials, including their content, processing, or transmission through the Service; (b) the Customer's use of the Service in breach of this agreement; (c) the Customer's prompts or inputs to AI features in breach of §15.7; or (d) the Customer's breach of §5 (sanctions, AML, anti-bribery, whistleblower).

17.3 **Indemnity exclusions.** The Vendor's indemnity in §17.1 does not apply to claims arising from (a) the Customer's modification of the Service; (b) the combination of the Service with materials not provided by the Vendor where the claim would not have arisen but for that combination; (c) the Customer's use of the Service after notice of an alleged infringement; or (d) Customer Data or Customer Materials.

17.4 **Procedure.** The indemnified Party shall (a) give the indemnifying Party prompt written notice of the claim; (b) give the indemnifying Party sole control over defence and settlement (except that any settlement that imposes a non-monetary obligation on the indemnified Party requires its consent, not unreasonably withheld); and (c) provide reasonable cooperation at the indemnifying Party's expense. Failure to give prompt notice does not relieve the indemnifying Party of its obligations except to the extent it is prejudiced by the delay.

17.5 **Insurance.** The Vendor shall maintain, throughout the Subscription Term, insurance with reputable insurers in not less than the following amounts:

  (a) **Professional indemnity / errors and omissions ("E&O")** — `{{E&O Limit — default ISK 750,000,000 (approximately EUR 5,000,000)}}` per claim and in the aggregate;

  (b) **Public liability** — `{{Public Liability Limit — default ISK 300,000,000 (approximately EUR 2,000,000)}}` per claim;

  (c) **Cyber liability** — `{{Insurance Cyber Limit — default ISK 750,000,000 (approximately EUR 5,000,000)}}` per claim and in the aggregate, covering data-breach response, regulatory investigation costs (including Persónuvernd proceedings), and third-party data-subject claims; and

  (d) **Employer's liability** — at the level required by **Lög nr. 55/1980 um starfskjör launafólks** and other applicable Icelandic labour-market legislation (vinnumarkaðarslög) `[VERIFY current statutory minimum at execution]`.

The Vendor shall provide certificates of insurance on reasonable written request.

> **Dual-perspective drafting note (§17).** A Vendor-favourable revision caps total indemnity payouts at the §16.5 liability cap and excludes patent-infringement claims for any modifications (including Customer-suggested ones). A Customer-favourable revision raises insurance minimums, requires the Vendor to obtain an additional-insured endorsement, and adds a remediation duty (replace, modify, or refund) on a confirmed infringement.

## 18. General provisions

This section gathers the standard housekeeping items: notices, force majeure, assignment, governing law, forum, and electronic signatures.

18.1 **Notices.** Notices under this agreement shall be sent by email to the address recorded on the Order Form, with a copy by registered post (ábyrgðarbréf) to the Party's registered office. The Order Form shall record, for each Party: full legal name; kennitala (Vendor: `{{Vendor Kennitala}}`; Customer: `{{Customer Kennitala}}`); registered office address; primary email for legal notices; and primary email for security and breach notifications.

18.2 **Compliance with law.** Each Party shall comply with applicable Icelandic, EEA, EU, and UN law in connection with this agreement, including (a) sanctions and export controls under **Lög nr. 96/2016 um þvingunaraðgerðir alþjóðlegra stofnana**; (b) anti-money-laundering rules under **Lög nr. 64/2019**; (c) anti-bribery offences under **Almenn hegningarlög nr. 19/1940**; and (d) whistleblower protection under **Lög nr. 40/2020 um vernd uppljóstrara** `[VERIFY current title and number]`.

18.3 **Force majeure.** Neither Party is liable for any delay or failure to perform (other than payment obligations) caused by circumstances beyond its reasonable control (óviðráðanlegar aðstæður), including acts of God, war, civil unrest, pandemic, government order, telecommunications or utility outage, cyberattack not attributable to the affected Party's negligence, and volcanic activity affecting Icelandic infrastructure. The affected Party shall give prompt notice and shall use reasonable efforts to mitigate. If a force-majeure event continues for more than sixty (60) consecutive days, either Party may terminate the affected Order Form by written notice.

18.4 **Assignment.** Neither Party may assign or transfer this agreement, in whole or in part, without the other Party's prior written consent (such consent not to be unreasonably withheld), except that either Party may assign to (a) an Affiliate; or (b) a successor in interest in connection with a merger, reorganisation, or sale of substantially all of the assets of the assigning Party's business to which this agreement relates, in each case on written notice to the other Party. Any purported assignment in breach of this section is void.

18.5 **Independent contractors.** The Parties are independent contractors. Nothing in this agreement creates a partnership, agency, joint venture, or employment relationship.

18.6 **Entire agreement.** This agreement (including the Order Forms and Exhibits) is the entire agreement between the Parties on its subject matter and supersedes all prior or contemporaneous communications and proposals on that subject.

18.7 **Counterparts and electronic signatures.** This agreement may be executed in counterparts, each of which is an original and which together form one instrument. The Parties may sign by qualified or advanced electronic signature consistent with **Regulation (EU) No 910/2014 (eIDAS)** as incorporated into the EEA Agreement and with **Lög nr. 28/2001 um rafrænar undirskriftir** (the Icelandic Electronic Signatures Act). Scanned copies and PDF copies are deemed originals for evidentiary purposes.

18.8 **Governing law.** This agreement is governed by Icelandic law (íslensk lög), excluding its conflict-of-laws rules and the United Nations Convention on Contracts for the International Sale of Goods. For cross-EEA disputes, jurisdiction and recognition of judgments are governed by the **Lugano Convention 2007** to the extent applicable as between Iceland and the relevant EEA/EFTA State or EU Member State `[VERIFY current applicability of the Lugano Convention 2007 as between Iceland and the counterparty's jurisdiction at execution]`.

18.9 **Forum.** The Parties submit to the exclusive jurisdiction of `{{Forum Court — default Héraðsdómur Reykjavíkur (Reykjavík District Court)}}`, with appeals as permitted under **Lög nr. 91/1991 um meðferð einkamála** (Code of Civil Procedure). The Parties may agree in writing to refer a dispute to arbitration under **Lög nr. 53/1989 um samningsbundna gerðardóma** in lieu of court proceedings; absent such written agreement, this §18.9 controls.

18.10 **No class actions.** The Parties acknowledge that Icelandic civil procedure does not recognise the US-style class action; collective redress, where available, is limited to procedures expressly provided for in Icelandic or EEA law. This section is declaratory only and does not waive any individual statutory right.

18.11 **Severability.** If any provision is held invalid or unenforceable by a court of competent jurisdiction, the remaining provisions continue in effect, and the invalid provision shall be reformed to the minimum extent necessary to render it enforceable.

18.12 **Waiver.** A failure to enforce a provision is not a waiver of any subsequent breach.

18.13 **Order of language.** This English text is operative as the working language. Where the Parties have published an Icelandic-language version (`is-isl.md`), the Icelandic text controls per the bilingual usage callout above.

---

## Exhibits

- **Exhibit A — Service description and SLA.** Service modules, availability commitment, support response times, scheduled maintenance windows, service-credit schedule, and AI feature descriptions per §15.5.
- **Exhibit B — Acceptable Use Policy.** Prohibited uses; reporting channels; suspension triggers.
- **Exhibit C — Data Processing Addendum (IS variant).** Article 28 GDPR / Article 25 Lög nr. 90/2018 processor terms; sub-processor list; international-transfer mechanism (SCCs as adopted into the EEA Agreement); breach-notification timescales; audit cooperation; EEA-incorporated DORA addendum at Exhibit C-1 where applicable.
- **Exhibit D — Security overview.** Information-security controls; certifications (ISO 27001 / SOC 2 Type II per §11.8); penetration-testing programme.

---

## Appendix — Merge fields used

- `{{Vendor Legal Name}}`
- `{{Vendor Address}}`
- `{{Vendor Kennitala}}`
- `{{Customer Legal Name}}`
- `{{Customer Address}}`
- `{{Customer Kennitala}}`
- `{{Persónuvernd Registration Number}}` `[OPTIONAL]`
- `{{Currency — default ISK}}`
- `{{Payment Term — default 30 days}}`
- `{{Price-Change Notice — default 60 days}}`
- `{{Price-Increase Cap — default 7%}}`
- `{{Renewal Term — default 12 months}}`
- `{{Renewal Notice — default 60 days}}`
- `{{Confidentiality Survival — default 5 years}}`
- `{{Export Window — default 30 days}}`
- `{{Deletion Window — default 90 days}}`
- `{{Uptime Commitment — default 99.9%}}`
- `{{Liability Cap Floor — default ISK 15,000,000 (approximately EUR 100,000)}}` (a.k.a. `{{ISK Liability Cap Floor}}`)
- `{{E&O Limit — default ISK 750,000,000 (approximately EUR 5,000,000)}}`
- `{{Public Liability Limit — default ISK 300,000,000 (approximately EUR 2,000,000)}}`
- `{{Insurance Cyber Limit — default ISK 750,000,000 (approximately EUR 5,000,000)}}`
- `{{Forum Court — default Héraðsdómur Reykjavíkur}}`

---

## Appendix — Authoritative references

**Primary Icelandic legislation (althingi.is — public domain).**

- Lög nr. 7/1936 um samningsgerð, umboð og ógilda löggerninga (Contracts Act, including § 36 unconscionability) — https://www.althingi.is/lagas/nuna/1936007.html
- Lög nr. 16/2016 um neytendasamninga (Consumer Contracts Act) — https://www.althingi.is/lagas/nuna/2016016.html
- Lög nr. 30/2002 um rafræn viðskipti og aðra rafræna þjónustu (E-Commerce Act)
- Lög nr. 90/2018 um persónuvernd og vinnslu persónuupplýsinga (Data Protection Act)
- Lög nr. 70/2022 um sókn vegna brota á persónuvernd (data-protection collective redress) `[VERIFY title and applicability]`
- Lög nr. 73/1972 um höfundarétt (Copyright Act)
- Lög nr. 17/1991 um einkaleyfi (Patents Act)
- Lög nr. 38/2001 um vexti og verðtryggingu (Interest and Indexation Act)
- Lög nr. 50/1988 um virðisaukaskatt (Value-Added Tax Act)
- Lög nr. 96/2016 um þvingunaraðgerðir alþjóðlegra stofnana (International Sanctions Act)
- Lög nr. 64/2019 um varnir gegn peningaþvætti og fjármögnun hryðjuverka (AML/CTF Act)
- Lög nr. 40/2020 um vernd uppljóstrara (Whistleblower Protection Act) `[VERIFY current title and number]`
- Lög nr. 28/2001 um rafrænar undirskriftir (Electronic Signatures Act)
- Lög nr. 21/1991 um gjaldþrotaskipti (Bankruptcy Act)
- Lög nr. 91/1991 um meðferð einkamála (Code of Civil Procedure)
- Lög nr. 53/1989 um samningsbundna gerðardóma (Arbitration Act)
- Almenn hegningarlög nr. 19/1940 (General Penal Code, including §§ 109 and 264a on bribery)

**Supervisory authorities.**

- Persónuvernd (Icelandic Data Protection Authority) — https://www.personuvernd.is/
- Neytendastofa (Consumer Agency) — https://www.neytendastofa.is/
- Fjármálaeftirlitið (FME) — financial entities (relevant to §11.7 DORA)
- Hagstofa Íslands (Statistics Iceland) — for CPI references in §8 dual-perspective notes

**EU/EEA instruments (eur-lex.europa.eu — public domain) referenced in this template.**

- Regulation (EU) 2016/679 (GDPR) — incorporated into EEA Agreement
- Regulation (EU) No 910/2014 (eIDAS) — incorporated into EEA Agreement
- Directive (EU) 2016/943 (Trade Secrets) — incorporated into EEA Agreement
- Directive (EU) 2022/2555 (NIS2) — `[VERIFY EEA Joint Committee Decision and IS transposition]`
- Regulation (EU) 2022/2554 (DORA) — `[VERIFY EEA Joint Committee Decision and IS transposition]`
- Regulation (EU) 2023/2854 (Data Act) — `[VERIFY EEA Joint Committee Decision and IS transposition]`
- Regulation (EU) 2024/1689 (AI Act) — `[VERIFY EEA Joint Committee Decision and Iceland-specific commencement]`
- Lugano Convention 2007 on jurisdiction and the recognition and enforcement of judgments in civil and commercial matters — `[VERIFY current applicability]`

**EFTA Surveillance Authority** — https://www.eftasurv.int/ (oversight of EEA-incorporated EU acts in Iceland, Liechtenstein, and Norway).

**Permissively licensed baselines consulted (clean-room; no verbatim runs of five or more words).**

- Common Paper CSA v2.1, Order Form, AI Addendum `[CC-BY-4.0]`
- Bonterms Cloud Terms / PSA `[CC-BY-4.0/CC0]`
- GitHub site-policy `[CC0]`; Mozilla Public License 2.0 docs `[MPL-2.0]`

---

## Companion Icelandic-language draft

A parallel Icelandic-language draft is forthcoming as `is-isl.md`. When published and executed alongside this English text, the Icelandic text controls per the bilingual usage callout above.

---

## Not legal advice

This template is provided for informational and drafting-aid purposes only. It is not legal advice, does not create an attorney–client relationship, and does not substitute for review by qualified Icelandic counsel admitted before the Icelandic courts (lögmenn). Icelandic law, EU law incorporated through the EEA Agreement, and the supervisory practice of Persónuvernd, Neytendastofa, FME, and the EFTA Surveillance Authority change over time, and the `[VERIFY]` flags in this document mark items that should be confirmed against the current state of the law and the EEA Joint Committee's incorporation register before execution. The drafter is responsible for adapting the template to the specific facts of any transaction.
