---
title: Service Level Agreement — EU/EEA (DORA + NIS2 + CRA + Data Act)
jurisdictions: [eu, eea, de]
statutes: [DORA-2022/2554, NIS2-2022/2555, CRA-2024/2847, Data-Act-2023/2854, GDPR, ePrivacy-2002/58/EC, BSI-KritisV]
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

# Service Level Agreement — EU/EEA Variant

**Parties.** This Service Level Agreement (the "SLA") applies between `{{Vendor Legal Name}}` ("Vendor") and `{{Customer Legal Name}}` ("Customer") and forms Exhibit B of the Cloud Service Agreement between the Parties dated `{{CSA Effective Date}}` (the "CSA"). Where this SLA is used on a stand-alone basis, references to the CSA mean the master subscription, professional-services or framework agreement under which the Service is delivered. The "Effective Date" of this SLA is `{{Effective Date}}`.

**Audience.** This SLA is drafted for B2B engagements between EU- or EEA-established Parties. Where Customer is a financial entity in scope of Regulation (EU) 2022/2554 ("DORA"), an essential or important entity in scope of Directive (EU) 2022/2555 ("NIS2"), or a manufacturer placing a product with digital elements on the Union market within Regulation (EU) 2024/2847 ("CRA"), this SLA assumes those regimes apply alongside the contractual commitments and does not displace any mandatory regulatory obligation.

---

## 1. Plain-language summary

This Section is a non-binding orientation drafted in clear and intelligible language. The binding wording is set out in Sections 2 to 20 and the Annexes; in case of conflict, the operative Sections govern.

This SLA describes how reliably Vendor will run the hosted service identified in the Order Form (the "Service"), how quickly Vendor will answer support requests, and what credits Customer receives if the Service falls below the agreed availability tier. It is an Exhibit to the CSA and inherits its definitions, governing-law and limitation-of-liability provisions, except where varied here. It coordinates with EU incident-notification regimes — GDPR Article 33 (personal-data breaches), NIS2 Article 23 (significant incidents), DORA Article 19 (major ICT incidents at financial entities), and CRA Article 14 (actively-exploited vulnerabilities and severe incidents in products with digital elements). Section 17 reflects those timelines and applies alongside, not in place of, the contractual commitments in Sections 4 to 14.

Service Credits are the exclusive contractual remedy for missing the availability commitment, but Customer's mandatory rights under Article 82 GDPR, Article 23 NIS2, and the DORA penalty regime are preserved.

---

## 2. Definitions

This Section defines the capitalised terms used throughout this SLA. Capitalised terms not defined here have the meaning given in the CSA.

**"Availability"** means, for a given calendar month, the percentage calculated under Section 4.

**"Business Hours"** means 09:00 to 18:00 local time at `{{Support Time Zone}}` on a Working Day.

**"Calendar Month"** means a Gregorian calendar month.

**"Covered Service"** means each Service component listed in Section 3 and any service component identified as covered in an Order Form.

**"Disaster"** means a partial or total unavailability of one or more Covered Services that triggers Vendor's business-continuity plan under Section 11.

**"DORA"** means Regulation (EU) 2022/2554 on digital operational resilience for the financial sector.

**"Excluded Downtime"** has the meaning given in Section 5.

**"ICT-related Incident"** has the meaning given in Article 3(8) DORA, and "Major ICT-related Incident" has the meaning given in Article 3(10) DORA.

**"Maintenance Window"** means the recurring time period defined in Section 12 during which Vendor performs scheduled maintenance.

**"Major Outage"** means a Severity 1 incident as classified in Annex A.

**"Monthly Uptime Percentage"** has the meaning given in Section 4.

**"NIS2"** means Directive (EU) 2022/2555 on measures for a high common level of cybersecurity across the Union.

**"Personal Data Breach"** has the meaning given in Article 4(12) of Regulation (EU) 2016/679 (the General Data Protection Regulation, "GDPR").

**"Product with Digital Elements"** has the meaning given in Article 3(1) of the CRA.

**"Service Credit"** means a credit issued in accordance with Sections 7 to 9, expressed as a percentage of the Monthly Service Fees for the affected Covered Service.

**"Severity"** means the classification (Severity 1 to Severity 4) given to an incident in Annex A.

**"Significant Incident"** has the meaning given in Article 23(3) NIS2.

**"Total Minutes"** means the total number of minutes in the relevant Calendar Month.

**"Working Day"** means a day other than a Saturday, Sunday or public holiday in Vendor's principal place of operation.

Other terms are defined where they first appear and reused with the same meaning. References to statutes include national implementations and successor instruments. Singular includes plural and vice versa.

---

## 3. Scope of services covered

This Section identifies which parts of the Service are subject to the availability commitment and which regulatory regimes inform the SLA.

**Covered Services.** This SLA covers the production tenant of the Service identified in the Order Form, including the following components: (a) the customer-facing web application at `{{Service URL}}`; (b) the application programming interface ("API") at `{{API URL}}`; (c) the data plane at which Customer Data is stored and processed; and (d) the authentication, authorisation and identity layer that gates access to the foregoing. Sandbox, development, staging and trial tenants are excluded from the availability commitment but receive support on a commercially reasonable basis.

**Regulatory scope flags.** The Parties acknowledge the following characterisation as of the Effective Date, which informs Sections 11 and 17:

- **DORA scope.** Vendor is `{{Vendor DORA Class}}` (e.g., "ICT third-party service provider for a financial entity per Article 3(19) DORA," or "not in scope"). Where in scope, §§ 11.5, 11.6 and 17.3 apply. Where Customer is a financial entity, the rights of its competent authority and the European Supervisory Authorities ("ESAs" — EBA, EIOPA, ESMA) under Articles 31 to 44 DORA are preserved.
- **NIS2 scope.** Vendor is `{{Vendor NIS2 Class}}` ("essential," "important," or "not in scope"), based on Vendor's principal sector under Annexes I and II of NIS2 and Vendor's size. Where in scope, § 11.7 and § 17.2 apply.
- **CRA scope.** The Service `{{CRA Scope Statement}}` (e.g., "includes a Product with Digital Elements placed on the Union market per Article 3(1) CRA"). Where in scope, § 17.4 applies once the relevant CRA provisions become applicable. `[VERIFY CRA commencement and exact timelines]`
- **GDPR Article 32 scope.** Vendor processes Personal Data on behalf of Customer and is subject to Article 32 GDPR under the DPA.

**Geographic scope.** Availability is measured globally for the production tenant unless an Order Form specifies a regional commitment. Where Customer subscribes to a regional tenant (for example, an EU-only data-residency configuration), Availability is measured for that region.

---

## 4. Service Availability commitment

This Section sets the uptime target and the formula used to measure it.

**Target.** Vendor commits that the Monthly Uptime Percentage for each Covered Service will meet or exceed `{{Uptime Tier}}` (the "Availability Target") in each Calendar Month.

**Formula.** Monthly Uptime Percentage is calculated as:

> Monthly Uptime Percentage = ((Total Minutes − Downtime Minutes − Excluded Downtime) ÷ (Total Minutes − Excluded Downtime)) × 100

where "Downtime Minutes" means the sum of minutes during which the Covered Service was Unavailable (defined below), and "Excluded Downtime" has the meaning given in Section 5.

**Definition of Unavailable.** A Covered Service is "Unavailable" when external synthetic monitoring against the Covered Service's primary endpoint, run from at least three geographically distributed observation points, returns connection errors, HTTP 5xx responses, or response latencies in excess of `{{Latency Threshold}}` (default: ten (10) seconds) for two consecutive observations one minute apart. Brief degradations that do not meet the consecutive-observation test are tracked under Section 13 (Service degradation vs. outage) but do not count as Downtime Minutes.

**Measurement method.** Availability is measured by `{{Uptime Measurement Method}}` (default: Vendor's third-party synthetic-monitoring provider) and reconciled against Vendor's internal observability stack monthly. Customer may, on reasonable request and at Customer's cost, audit the measurement methodology under the audit rights in the DPA / CSA. Measurement records are retained for at least twelve (12) months.

**Dual-perspective drafting note.**

- **Vendor-favourable.** 99.5% target (≈3.6h/month); Vendor-operated measurement; limited dispute right.
- **Market-standard.** 99.9% target (≈43.2m/month); third-party synthetic monitoring; raw data on request.
- **Customer-favourable.** 99.95%–99.99% target (≈21.6m–4.4m/month); jointly-selected independent monitoring is authoritative absent manifest error.

A target Vendor cannot meet is a target Customer should not accept.

---

## 5. Excluded Downtime

This Section lists the categories of unavailability that are excluded from the SLA calculation and from the credit regime.

The following periods are not counted as Downtime Minutes and do not reduce Monthly Uptime Percentage:

- (a) Scheduled Maintenance performed in accordance with Section 12;
- (b) Emergency Maintenance performed in accordance with Section 12, provided Vendor has issued the notice required by that Section;
- (c) Force-majeure events as defined in the CSA, including natural disasters, armed conflict, civil unrest, government action and pandemic-related orders;
- (d) Failures of Customer-controlled equipment, networks or software, including Customer's local-area network, Customer's identity provider where Customer operates it, and Customer's misconfiguration;
- (e) Outages of public internet infrastructure or domain-name-system providers outside Vendor's control;
- (f) Outages caused by Customer's breach of the Acceptable Use Policy or by traffic that constitutes a denial-of-service attack against Customer's tenant where the attack is not mitigated by Vendor's standard protections;
- (g) Suspension imposed under the CSA for non-payment, security incident, or violation of the Acceptable Use Policy;
- (h) Beta, preview, evaluation, alpha or trial features expressly excluded from the SLA;
- (i) Customer's failure to maintain a supported client version where Vendor has provided reasonable notice of the supported version;
- (j) Failures of third-party services not under Vendor's contractual control where Vendor has used commercially reasonable mitigation;
- (k) Periods during which Vendor restricts Customer's access in good faith to comply with a binding court order or law-enforcement request;
- (l) Service interruption mandated by an EU institution, a Member-State competent authority or a supervisory authority — including a supervisory order issued under DORA Article 42, NIS2 Article 32, or a corresponding national security or telecommunications regulator's order — provided Vendor furnishes the notice required by Section 17 to the extent permitted by the order;
- (m) Periods of Service restriction implemented as part of a coordinated cyber-attack response under guidance issued by the European Union Agency for Cybersecurity ("ENISA"), under the NIS2 cooperative-defence procedure (Articles 14 to 16 NIS2 — the EU-CyCLONe procedure for large-scale incident response), or under a recommendation of Customer's national computer security incident response team (the "National CSIRT"), again subject to Vendor's notice obligations under Section 17.

**Dual-perspective drafting note.**

- **Vendor-favourable.** Categories are exhaustive; a single demonstrated cause excludes the incident.
- **Market-standard.** Vendor documents each invocation in the monthly report with timestamp, root cause and category; Vendor demonstrates the cause on request.
- **Customer-favourable.** Vendor must prove on the balance of probabilities and with documentary evidence both that the cause falls within an enumerated category and that the outage could not have been mitigated by commercially reasonable measures Vendor was contractually obliged to take.

---

## 6. Support response & resolution targets

This Section sets out how quickly Vendor will respond to and resolve support requests once Customer has reported them through the agreed channel.

**Channels.** Customer reports requests via `{{Support Channels}}` (default: portal at `{{Support Portal URL}}` and email `{{Support Email}}`). For Severity 1, Customer must also use the paging channel `{{On-call Paging Channel}}`.

**Hours.** Vendor provides support during `{{Support Hours}}` (default: 24x7 for Severity 1 and 2; Business Hours for Severity 3 and 4).

**Time zone and regional toggles.** Unless an Order Form specifies otherwise, Vendor's primary `{{Support Time Zone}}` is "Central European Time" (Europe/Brussels). Vendor offers the following regional toggles for customers whose primary operations are in the relevant region:

- **Iberian region.** `{{Support Time Zone}}` = "Western European Time" (Europe/Lisbon / Europe/Madrid).
- **Nordic region.** `{{Support Time Zone}}` = "Central European Time" (Europe/Stockholm / Europe/Copenhagen) or "Western European Summer Time" where applicable.
- **Baltic region.** `{{Support Time Zone}}` = "Eastern European Time" (Europe/Tallinn / Europe/Riga / Europe/Vilnius).
- **Eastern European region.** `{{Support Time Zone}}` = "Eastern European Time" (Europe/Bucharest / Europe/Sofia / Europe/Athens).

**Severity matrix.** Severity classification, response targets and resolution targets are set out in Annex A. By default:

| Severity | First response | Update cadence | Resolution / workaround |
|----------|----------------|----------------|--------------------------|
| Severity 1 (production outage) | `{{P1 Response Target}}` (default: 15 minutes) | Every 60 minutes | `{{P1 Resolution Target}}` (default: 4 hours) |
| Severity 2 (major degradation) | `{{P2 Response Target}}` (default: 1 hour) | Every 4 hours | 1 Working Day |
| Severity 3 (minor issue) | `{{P3 Response Target}}` (default: 4 Business Hours) | Daily | 5 Working Days |
| Severity 4 (question / cosmetic) | `{{P4 Response Target}}` (default: 1 Working Day) | Weekly | Best effort |

**Resolution vs. workaround.** A target is met when Vendor delivers either a permanent fix or a documented workaround that materially restores the affected functionality. Vendor will not knowingly close a ticket on a workaround basis without informing Customer.

**Dual-perspective drafting note.**

- **Vendor-favourable.** Targets are objectives, not warranties; misses do not generate credits.
- **Market-standard.** Severity 1 and 2 response targets are firm commitments; missing by more than 100% triggers a defined credit; resolution times remain best-effort.
- **Customer-favourable.** Both response and resolution targets are firm commitments; three or more misses in a rolling 90-day period for the same Severity escalate under Section 14.

---

## 7. Service Credits

This Section sets out the credits Customer receives if Monthly Uptime Percentage falls below the Availability Target.

**Tiered credits.** Service Credits are calculated as a percentage of the Monthly Service Fees for the affected Covered Service in the Calendar Month in which the Availability Target was missed. The default tiered table is set out in Annex B and reproduced below for reference at the 99.9% Availability Target:

| Monthly Uptime Percentage | Service Credit |
|---------------------------|----------------|
| < 99.9% but ≥ 99.0% | 10% |
| < 99.0% but ≥ 95.0% | 25% |
| < 95.0% | 50% |

Higher Availability Targets use a steeper schedule; lower targets use a shallower schedule. The full schedules for 99.5%, 99.9%, 99.95% and 99.99% targets are set out in Annex B.

**Credit cap.** The maximum aggregate Service Credit in any Calendar Month is `{{Credit Cap Percent}}` (default: 30%) of the Monthly Service Fees for the affected Covered Service.

**Currency and offset.** Service Credits are denominated in the currency of the relevant invoice (default: euro) and applied as a credit against the next invoice issued under the CSA. Where the CSA terminates before the credit is fully applied, Vendor will refund the unapplied balance within thirty (30) days of termination.

**Dual-perspective drafting note.**

- **Vendor-favourable.** Single tier (10% for any miss below 99.9%); 10% monthly cap.
- **Market-standard.** Three-tier schedule above; 30% monthly cap.
- **Customer-favourable.** Five-tier schedule with steeper percentages (25% / 50% / 75% / 100%); cap removed for outages exceeding `{{Major Outage Hours}}` (e.g., eight (8) hours).

---

## 8. Credit request procedure

This Section explains how Customer claims a Service Credit.

**Automatic vs. claimed credits.** Where Vendor's monitoring identifies a missed Availability Target, Vendor will issue the Service Credit automatically on the next invoice and reflect it in the monthly report under Section 10. Customer may also submit a written claim via the Support Portal within `{{Credit Window Days}}` (default: sixty (60) days) of the end of the Calendar Month in which the alleged missed target occurred. Claims submitted after that period are time-barred unless Vendor has not delivered the monthly report due under Section 10.

**Required content.** A claim must include (a) the affected Covered Service; (b) the dates and times of the alleged Downtime; (c) any logs, screenshots, error codes or third-party monitoring evidence Customer relies on; and (d) the estimated business impact (for prioritisation only — quantum is set by Annex B).

**Vendor evaluation.** Vendor will evaluate each claim within fifteen (15) Working Days, accept or reject it with reasons in writing, and apply any accepted credit to the next invoice. Disputes about the existence or quantum of a credit are escalated under the dispute-resolution clause of the CSA.

---

## 9. Credit issuance & exclusivity as remedy

This Section explains the legal status of Service Credits.

**Sole contractual remedy.** Service Credits are Customer's sole and exclusive contractual remedy for Vendor's failure to meet the Availability Target, the support response targets, or the support resolution targets, in each case where the failure is otherwise compensable under this SLA. The Parties agree that the credits represent a reasonable pre-estimate of the loss likely to result from such failures and are not a penalty.

**Mandatory regulatory remedies preserved.** The exclusivity in the preceding paragraph does not displace:

- (a) Customer's right to compensation under Article 82 GDPR;
- (b) Penalties, fines or remedies under Article 23 NIS2, and administrative fines under Article 34 NIS2;
- (c) The DORA penalty regime, including Articles 50–53 DORA and the powers of competent authorities and the ESAs under Articles 31–44 DORA;
- (d) Compensation, remedies or fines under Chapter VI CRA;
- (e) Any other mandatory EU or Member-State provision that cannot be derogated from by agreement, including consumer law;
- (f) Termination rights for material breach under the CSA (including Section 14 below) and surviving damages claims subject to the CSA limitation-of-liability cap.

**No double recovery.** Where Customer has received a Service Credit and subsequently recovers damages for the same loss under a regime preserved above, the Service Credit is set off against the damages recovery on a euro-for-euro basis, to the extent permitted by mandatory law.

---

## 10. Performance reporting & status page

This Section explains how Vendor reports SLA performance and how Customer is kept informed.

**Status page.** Vendor maintains a publicly accessible status page at `{{Status Page URL}}` showing real-time status of each Covered Service, current incidents, planned maintenance windows and a rolling 90-day history. Entries are posted within 15 minutes of Vendor identifying an incident. Customer may subscribe by email, RSS or webhook.

**Monthly report.** Within 15 Working Days after each Calendar Month, Vendor delivers a "Monthly SLA Report" in the format at Annex C, covering: (a) Monthly Uptime Percentage per Covered Service; (b) incidents with Severity, start/end times, root cause and remediation; (c) Excluded Downtime invoked with category and reason; (d) Service Credits applied or proposed; (e) any change to the Availability Target or measurement method.

**Cadence.** Default `{{Reporting Cadence}}` = monthly. Customer-favourable: weekly summaries plus a quarterly executive review. Vendor-favourable: quarterly for Customers below an agreed annual contract value.

**Customer information rights.** During an active Severity 1 incident, Vendor will (i) post status updates per Section 6 cadence, (ii) notify Customer's nominated technical and security contacts directly, and (iii) where the incident is reasonably likely to be a Personal Data Breach or a Significant Incident, escalate per Section 17.

---

## 11. Disaster recovery & business continuity

This Section sets out Vendor's resilience commitments in the event of a Disaster.

**Business continuity plan.** Vendor maintains a documented business continuity and disaster-recovery plan ("BCP/DR Plan") covering the Covered Services. The BCP/DR Plan is reviewed at least annually and tested at least once every twelve (12) months. A summary of the BCP/DR Plan is made available to Customer on reasonable request, subject to the confidentiality clause of the CSA.

**Recovery objectives.** Vendor commits to the following objectives for declared Disasters:

- **Recovery Time Objective (RTO):** `{{RTO}}` (default: four (4) hours).
- **Recovery Point Objective (RPO):** `{{RPO}}` (default: one (1) hour).

These are objectives, not warranties, and missing them in a Disaster does not by itself constitute a material breach. Repeated misses of RTO or RPO across multiple Disasters within a rolling twelve-month period may be escalated under Section 14.

**Backups and redundancy.** Vendor maintains backups of Customer Data at a frequency consistent with the RPO and stores them in geographically separate EEA facilities unless Customer has expressly elected a non-EEA region in the Order Form. Production runs across at least two independent availability zones in the primary region.

**Communication during Disasters.** Vendor will (a) post an incident notice within 15 minutes of declaration, (b) update nominated contacts at least every 60 minutes until closure, and (c) on closure deliver a written incident report within 10 Working Days covering root cause, remediation, lessons learned and process changes.

**§11.5 — DORA Article 11 ICT business continuity policy.** Where Customer is a financial entity within Article 2 DORA (a "Financial-Entity Customer"), Vendor maintains a documented ICT business continuity policy aligned with Article 11 DORA — covering Article 11(2) objectives and outputs, Article 11(6) testing of response and recovery plans, and Article 11(7) crisis communication. Relevant components are made available to the Financial-Entity Customer and, on reasonable request, to its competent authority and the relevant ESA. `[VERIFY DORA RTS commencement]`

**§11.6 — DORA Articles 6 and 7 ICT risk-management framework.** Vendor's ICT risk-management framework is maintained in alignment with Articles 6 and 7 DORA and the Commission's regulatory technical standards thereunder — governance (Art. 5), identification of supporting ICT assets (Art. 8), protection and prevention (Art. 9), detection (Art. 10), and learning and evolution (Art. 13). The framework is audited by an independent third party at least every two (2) years; the executive summary is available to Financial-Entity Customers on request.

**§11.7 — NIS2 Article 21 cybersecurity risk-management measures.** Where in NIS2 scope, Vendor implements the measures in Article 21(2) NIS2 across the ten enumerated areas: (i) risk-analysis and information-system security policies; (ii) incident handling; (iii) business continuity (backup, DR, crisis management); (iv) supply-chain security; (v) security in network and information-system acquisition, development and maintenance (including vulnerability handling and disclosure); (vi) effectiveness assessment; (vii) basic cyber hygiene and training; (viii) cryptography and, where appropriate, encryption; (ix) HR security, access control and asset management; (x) MFA or continuous authentication, and secured voice / video / text and emergency communications.

**§11.8 — ENISA cloud cybersecurity guidelines.** Vendor's security architecture aligns with applicable ENISA guidelines on cloud cybersecurity, including the ENISA Cloud Security for Healthcare Services and the ENISA Procurement Guidelines for Cybersecurity in Hospitals where the Customer's sector applies, and with horizontal ENISA recommendations for cloud service providers. Material deviations are documented in Vendor's security policy made available to Customer on reasonable request.

**§11.9 — EU Cybersecurity Certification Scheme for Cloud Services (EUCS).** Vendor's certification posture under the European Union Cybersecurity Certification Scheme for Cloud Services is `{{EUCS Assurance Level}}` (e.g., "basic," "substantial," "high," or "not yet certified"). Where certified, Vendor's certificate identifier is `{{EUCS Certificate ID}}`, and Vendor will inform Customer of any change in certification status that affects the Covered Services within thirty (30) days of the change. `[VERIFY EUCS adoption]`

**Dual-perspective drafting note.**

- **Vendor-favourable.** RTO/RPO 24h; single-region backups.
- **Market-standard.** RTO 4h / RPO 1h; backups in two EEA regions.
- **Customer-favourable.** RTO 1h / RPO 5m; geo-replicated active-active; quarterly DR-test reports.

---

## 12. Scheduled & emergency maintenance

This Section explains when Vendor takes the Service down for maintenance and how it tells Customer.

**Scheduled Maintenance.** Vendor performs Scheduled Maintenance during `{{Maintenance Window}}` (default: Saturdays 02:00–06:00 `{{Support Time Zone}}`), with at least `{{Maintenance Notice Window}}` (default: 7 days) prior notice via the status page and, for changes materially affecting Customer integration points, by email to nominated technical contacts. Up to `{{Scheduled Maintenance Cap Hours}}` (default: 8) per Calendar Month is Excluded Downtime under Section 5(a); time over the cap counts as Downtime Minutes unless Customer has expressly consented in writing.

**Emergency Maintenance.** Vendor may perform Emergency Maintenance outside the recurring window where reasonably necessary to address (a) a security vulnerability (including under Article 12 CRA or ENISA's coordinated-vulnerability-disclosure scheme); (b) a Significant Incident or ICT-related Incident; (c) a binding regulatory order; or (d) an imminent threat of data loss or material degradation. Vendor provides as much advance notice as is feasible (target `{{Emergency Notice Window}}`, default 2 hours) via the status page and direct notification to nominated technical and security contacts.

**Notification minimum.** Even where advance notice is not feasible, Vendor will, no later than the start of Emergency Maintenance, post a notice identifying affected Covered Services, expected duration, and reason at a level of detail consistent with Vendor's confidentiality and security obligations.

---

## 13. Service degradation vs. outage

This Section distinguishes a brief degradation from a measurable outage and explains how each is treated.

A Covered Service is in a state of "degradation" when (a) it remains nominally available but exhibits elevated error rates, elevated latency, or partial functional unavailability that does not meet the Unavailable test in Section 4; or (b) one or more non-critical features are unavailable while the core platform continues to operate. Degradation does not, by itself, generate Service Credits; it is reported on the status page, tracked in the monthly report under Section 10, and may be escalated to a Severity 2 incident under Annex A where it materially impairs Customer's use.

A Covered Service is in a state of "outage" when it meets the Unavailable test in Section 4. Outages are tracked as Downtime Minutes and, subject to Excluded Downtime, generate Service Credits per Section 7.

**Repeated degradation escalation.** Where the same Covered Service experiences three (3) or more degradation events in a rolling thirty (30) day period, each lasting more than fifteen (15) minutes, Customer may by written notice request a root-cause analysis under Section 11; if the analysis is not delivered within ten (10) Working Days, the cumulative degradation time counts as Downtime Minutes from the third event onward.

---

## 14. Material SLA breach & termination right

This Section gives Customer a termination right where Vendor consistently fails to meet the SLA.

**Material breach trigger.** It is a material breach of the CSA, entitling Customer to terminate the affected Order Form without penalty for the unused prepaid term, where any of the following occurs:

- (a) Monthly Uptime falls below `{{Termination Threshold}}` (default: 95%) in any Calendar Month;
- (b) Monthly Uptime falls below the Availability Target in `{{Consecutive Termination Months}}` (default: 3) consecutive months;
- (c) Monthly Uptime falls below the Availability Target in `{{Aggregate Termination Months}}` (default: 3) months in any rolling six-month period;
- (d) A single outage exceeds `{{Single Outage Termination Hours}}` (default: 24) consecutive hours;
- (e) Vendor misses RTO or RPO in two (2) or more declared Disasters within a rolling 12-month period.

**Procedure.** Customer must give Vendor written notice and a 30-day cure period before terminating, except for (d) (non-curable once concluded). Termination is without prejudice to (i) accrued Service Credits, (ii) damages or other remedies available under the CSA limitation-of-liability clause, and (iii) preserved regulatory remedies under Section 9.

**Refund.** Vendor refunds unused prepaid Fees within 30 days of termination and cooperates with the data-export and termination-assistance procedures in the CSA.

**Dual-perspective drafting note.**

- **Vendor-favourable.** Termination only on (b); 30-day cure; pro-rata refund only.
- **Market-standard.** All five triggers; 30-day cure for (a), (b), (c), (e); no cure for (d).
- **Customer-favourable.** Triggers above plus right to terminate the entire CSA where the breach affects Customer's ability to comply with DORA Article 28 (third-party-risk-management); damages and migration costs preserved subject to the CSA cap.

---

## 15. Changes to this SLA

This Section explains when Vendor may amend the SLA.

Vendor may amend this SLA on no less than thirty (30) days' prior notice to Customer, provided the amendments do not materially reduce Customer's rights, the Availability Target, the credit schedule or the support targets set out in Annex A. Where an amendment would materially reduce any of those rights, Vendor will obtain Customer's prior written consent or — at Vendor's option — give Customer the right to terminate the affected Order Form without penalty for the unused portion of the prepaid term, and to receive a pro-rata refund of any prepaid Fees.

This change-control approach is consistent with Article 19 of the Data Act on contract terms for data sharing and with the modification framework of Directive (EU) 2019/770 (the Digital Content Directive, "DCD") for B2C deployments by analogy.

---

## 16. Survival & order of precedence

This Section explains how this SLA fits with the rest of the contract documents.

**Survival.** The following Sections survive termination of the SLA: Section 8 (claims for credits accrued before termination), Section 9 (preserved remedies), Section 10 (delivery of any monthly report covering a period before termination), Section 17 (incident-response coordination, to the extent the underlying obligations under GDPR, NIS2, DORA or the CRA themselves survive), Section 18 (insurance, with respect to events occurring during the term), Section 19 (governing law and supervision) and this Section.

**Order of precedence.** Where there is a conflict between this SLA and another Contract Document of the CSA, the order of precedence in the CSA governs. In summary, mandatory provisions of EU and Member-State law that cannot be derogated from by agreement prevail, the DPA controls solely with respect to Personal Data and Article 28 GDPR matters, the executed Order Form prevails for the commercial terms it expressly varies, and the Master CSA prevails over this SLA, the Acceptable Use Policy and any policy incorporated by reference.

---

## 17. Incident-response coordination for EU breach notification

This Section coordinates Vendor's contractual notification obligations with the mandatory EU notification regimes that apply to Personal Data Breaches, Significant Incidents under NIS2, Major ICT-related Incidents under DORA, and severe incidents and actively-exploited vulnerabilities under the CRA.

**§17.1 — GDPR Article 33: Personal Data Breach notification.** Where Vendor processes Personal Data on behalf of Customer (the controller), Vendor notifies Customer of any Personal Data Breach affecting Customer's Personal Data without undue delay after becoming aware (Article 33(2) GDPR). To enable Customer to comply with the seventy-two (72) hour deadline in Article 33(1) GDPR, Vendor's contractual SLA for notification to Customer is `{{Vendor Breach SLA}}` (default: twenty-four (24) hours from Vendor becoming aware). The notification contains, to the extent then known, the categories and approximate number of data subjects and records concerned, the likely consequences, the measures taken or proposed, and a contact point, and is supplemented as more is known.

**§17.2 — NIS2 Article 23: Significant Incident reporting.** Where Vendor is in NIS2 scope (Section 3), Vendor reports Significant Incidents to its competent National CSIRT under the Article 23(4) NIS2 cascade:

- **Early warning:** within 24 hours of becoming aware, indicating any suspicion of unlawful or malicious cause and any cross-border impact;
- **Incident notification:** within 72 hours of becoming aware, updating the early warning with initial severity, impact and indicators of compromise;
- **Intermediate report:** on request of the National CSIRT or competent authority;
- **Final report:** within 1 month of the incident notification, with a detailed description, threat type or root cause, mitigation, and cross-border impact.

Vendor informs Customer of any reporting obligation to a National CSIRT, ENISA or another Member State's CSIRT that may indirectly affect Customer or requires Customer's cooperation, to the extent legally permitted.

**§17.3 — DORA Article 19: ICT-related Incident reporting (financial entities).** Where Customer is a Financial-Entity Customer, Customer reports Major ICT-related Incidents to its competent authority under Article 19 DORA, classified under Article 18 DORA and the relevant Commission Implementing Regulation. To support that obligation, Vendor commits to a `{{Major ICT Incident SLA}}` (default: two (2) hours) initial notification to Customer for any ICT-related Incident reasonably likely to constitute a Major ICT-related Incident materially affecting the Covered Services. The two-hour SLA is intentionally faster than sectoral deadlines so Customer has time to triage, classify and report. The notification includes, to the extent then known, affected Covered Services, time of detection, preliminary Article 18 classification, and a Vendor incident contact.

Vendor cooperates in good faith with Customer's regulatory reporting, including supplementary technical information, root-cause analyses, and reasonable access to incident-response personnel. Where Vendor is itself a "critical ICT third-party service provider" under Article 31 DORA, Vendor may be subject to direct supervisory examination by the Lead Overseer (EBA, EIOPA or ESMA) under Articles 35 to 38 DORA and will not invoke Customer confidentiality to obstruct an examination conducted in accordance with DORA.

**§17.4 — CRA Article 14: Active exploitation and severe incident reporting.** Where the Service includes a Product with Digital Elements within the meaning of Article 3(1) CRA, Vendor will, once the relevant CRA provisions become applicable, report to ENISA in accordance with Article 14 CRA:

- Actively-exploited vulnerabilities affecting the product within `{{CRA Active Exploitation Window}}` (default target: twenty-four (24) hours of becoming aware) as an early warning, with the incident-notification update and final report timeframes prescribed by Article 14 CRA; and
- Severe incidents affecting the security of the product within twenty-four (24) hours (early warning), seventy-two (72) hours (incident notification), and fourteen (14) days (final report), in each case via the single reporting platform designated by ENISA under Article 14 CRA.

Vendor will inform Customer of any such report that affects the Covered Services, to the extent legally permitted, and of any user-notification obligation under Article 14(8) CRA. `[VERIFY CRA commencement and exact timelines]`

**§17.5 — ePrivacy Article 4(3): Telecom-specific Personal Data Breach notification.** Where Vendor or Customer qualifies as a provider of a publicly available electronic-communications service, the additional Personal Data Breach notification regime in Article 4(3) of Directive 2002/58/EC (the "ePrivacy Directive") and Commission Regulation (EU) 611/2013 applies, including notification to the competent national supervisory authority within twenty-four (24) hours of detection where feasible, and the prescribed content of the notification. Vendor will identify in advance whether the Service falls within this scope and, where it does, will coordinate notifications with Customer.

**Notification mechanics.** Notifications under this Section 17 are sent to the contacts nominated in the Order Form (or, where none is nominated, to Customer's nominated technical and security contacts) and copied to `{{Customer Security Email}}`. Vendor's incident contact is `{{Vendor Security Email}}`, with regulatory-reporting questions routed via `{{ENISA Reporting Email}}` and Vendor's National CSIRT contact `{{National CSIRT}}` where relevant.

---

## 18. Insurance & cyber liability

This Section refers to Vendor's insurance and explains how it interacts with regulatory penalties.

Vendor maintains the insurance coverage required under Section 17 of the CSA (or, where this SLA is used stand-alone, under the equivalent CSA-clause insurance requirement), including a cyber-liability policy with a minimum aggregate limit of `{{Insurance Cyber Limit}}` (default: EUR 5,000,000 for production-tier subscriptions; tiered upward for Financial-Entity Customers and other DORA-in-scope deployments per the Order Form). On reasonable request, Vendor will provide a certificate of insurance evidencing the coverage.

**Coverage limits and regulatory fines.** Customer acknowledges that most cyber-liability policies do not cover regulatory fines or penalties imposed under GDPR Article 83, NIS2 Article 34, DORA Articles 50 to 53, or analogous Member-State sanctioning regimes, and that the existence of cyber-liability insurance does not relieve Vendor of its primary regulatory responsibility. Where Vendor's policy excludes such fines, Vendor will identify the exclusion to Customer at the time of issuing the certificate.

---

## 19. Governing law & supervision

This Section confirms how this SLA is governed and recognises EU supervisory rights.

**Governing law and forum.** This SLA is governed by, and the dispute-resolution clause operates under, the governing-law and forum provisions of the CSA. Where this SLA is used stand-alone, the EU/EEA default is the law of the Member State of Customer's establishment, and the courts of `{{Forum City}}` have exclusive jurisdiction, in each case subject to mandatory rules of consumer law where applicable.

**Supervisory examination of Vendor (DORA).** For Financial-Entity Customers, the rights of Customer's competent authority and the relevant Lead Overseer (the EBA, EIOPA or ESMA) under Articles 31 to 44 DORA — including the right to a direct supervisory examination of Vendor under Article 35 DORA where Vendor is designated as a critical ICT third-party service provider — are preserved, and Vendor will cooperate in good faith with any such examination. Reasonable Vendor costs of cooperation are addressed in the Order Form.

**Cooperation with Member-State supervisory authorities.** Vendor cooperates in good faith with national data-protection authorities (for example, the German Federal Commissioner for Data Protection and Freedom of Information ("BfDI") and the relevant Land authorities, the French Commission nationale de l'informatique et des libertés, the Irish Data Protection Commission, and Persónuvernd in Iceland), with national NIS2 competent authorities and CSIRTs, and with ENISA, in each case to the extent required by applicable law.

---

## 20. Germany overlay

This Section adds Germany-specific overlays where Customer or Vendor is established in Germany or where the Service is provided to a German federal authority. It supplements, and does not replace, the rest of this SLA.

**KRITIS scope (BSI-KritisV).** Where Customer or Vendor is an operator of critical infrastructure under Section 2(10) of the BSI-Gesetz and the Verordnung zur Bestimmung kritischer Infrastrukturen ("BSI-KritisV"), the threshold values in the BSI-KritisV Annexes apply, and the operator-of-essential-services obligations under Sections 8a and 8b BSI-Gesetz layer on top of NIS2 as transposed into German law. Vendor's classification is `{{Vendor KRITIS Class}}` ("operator of critical infrastructure," "covered as digital service provider," or "not in KRITIS scope"). `[VERIFY current BSI-KritisV thresholds]`

**IT-Sicherheitsgesetz 2.0 and KRITIS-Dachgesetz.** Vendor monitors developments in the KRITIS-Dachgesetz (the proposed cross-sector critical-infrastructure umbrella act) and the IT-Sicherheitsgesetz 2.0 / 3.0 amendments to the BSI-Gesetz, and will update its compliance posture and this SLA's Germany overlay as the German legislator finalises those instruments. `[VERIFY IT-Sicherheitsgesetz 2.0 status]`

**Dual-supervisory complexity.** German Personal Data Breach notification is split between the BfDI (for Customers and processing within federal competence) and the relevant Land data-protection authority (each, a "Land-LDA") for state-level processing. Where Vendor is uncertain which authority is competent, Vendor will notify Customer and align the regulatory-notification routing with Customer's data-protection officer.

**BSI IT-Grundschutz.** Vendor's information-security management system is informed by the BSI-Standards 200-1 (Information Security Management Systems), 200-2 (IT-Grundschutz Methodology) and 200-3 (Risk Analysis based on IT-Grundschutz) and, where applicable, by ISO/IEC 27001 mapped to IT-Grundschutz. Vendor's most recent BSI-Grundschutz or ISO 27001 certification status is `{{Vendor IT-Grundschutz Status}}`, and any change is notified to Customer within thirty (30) days.

**BaFin / Bundesbank supervision (DORA).** Where Customer is a financial entity supervised by the Bundesanstalt für Finanzdienstleistungsaufsicht ("BaFin") or the Deutsche Bundesbank, those authorities are competent for DORA supervision in Germany and the rights set out in Section 19 are exercisable by them, alongside the Lead Overseer for any critical ICT third-party service provider designation.

**Operating language.** Reporting and operational SLA artefacts (status-page entries, monthly reports, root-cause analyses, incident notifications under Section 17) are delivered in English unless Customer is a Bundesbehörde, Landesbehörde or other German public authority that requires a German-language version under Section 23 of the Verwaltungsverfahrensgesetz ("VwVfG") or analogous Land-level provisions, in which case Vendor will provide a German-language version on request, with translation costs allocated as set out in the Order Form.

---

## Annex A — Severity matrix

This Annex defines the four Severity levels referenced in Section 6 and Annex B.

| Severity | Definition | First response | Update cadence | Resolution / workaround |
|----------|------------|----------------|----------------|--------------------------|
| Severity 1 | Production outage of a Covered Service or critical-feature loss preventing Customer's normal use; no available workaround. Includes events likely to be classified as a Significant Incident under NIS2 Article 23, a Major ICT-related Incident under DORA Article 18, or a severe incident under CRA Article 14. | `{{P1 Response Target}}` (default: 15 minutes) | Every 60 minutes | `{{P1 Resolution Target}}` (default: 4 hours) |
| Severity 2 | Major degradation or non-critical feature outage materially affecting Customer's use; a partial workaround may exist. | `{{P2 Response Target}}` (default: 1 hour) | Every 4 hours | 1 Working Day |
| Severity 3 | Minor issue not materially affecting Customer's use; workaround available; cosmetic or low-impact functional issue. | `{{P3 Response Target}}` (default: 4 Business Hours) | Daily | 5 Working Days |
| Severity 4 | Question, configuration request, documentation issue, or feature request. | `{{P4 Response Target}}` (default: 1 Working Day) | Weekly | Best effort |

**Severity assignment.** Severity is initially assigned by Customer when raising the ticket and may be re-assigned by Vendor with prompt notification to Customer if Vendor reasonably considers a different Severity is warranted. Disputes about Severity are escalated under the dispute-resolution clause of the CSA.

---

## Annex B — Service Credit calculation

This Annex sets out the Service Credit schedule referenced in Section 7.

**Combined schedule by Availability Target.**

| Tier | Sub-target band 1 | Credit | Band 2 | Credit | Band 3 | Credit |
|------|-------------------|--------|--------|--------|--------|--------|
| 99.5% (Vendor-favourable) | <99.5% ≥99.0% | 5% | <99.0% ≥95.0% | 10% | <95.0% | 25% |
| 99.9% (market-standard) | <99.9% ≥99.0% | 10% | <99.0% ≥95.0% | 25% | <95.0% | 50% |
| 99.95% (Customer-favourable) | <99.95% ≥99.5% | 15% | <99.5% ≥99.0% | 30% | <99.0% | 50% |
| 99.99% (Financial-Entity) | <99.99% ≥99.9% | 20% | <99.9% ≥99.0% | 40% | <99.0% | 75%* |

\* Cap removed for outages exceeding `{{Major Outage Hours}}` at the 99.99% tier.

**Worked example.** Monthly Service Fees = EUR 10,000. Monthly Uptime Percentage = 99.4% under the 99.9% target. Applicable credit = 25% = EUR 2,500, applied against the next invoice (within the 30% / EUR 3,000 cap).

---

## Annex C — Sample monthly SLA report format

This Annex sets out the report format referenced in Section 10.

**1. Executive summary.** One paragraph stating Monthly Uptime Percentage per Covered Service against the Availability Target, total Service Credits applied, and any open material risks.

**2. Availability table.** Columns: Covered Service, Total Minutes, Downtime Minutes, Excluded Downtime, Monthly Uptime Percentage, Availability Target, Met (Yes/No).

**3. Incident log.** Each incident by ID, Severity, start and end time (UTC and `{{Support Time Zone}}`), affected Covered Service(s), root cause, remediation, link to public post-mortem.

**4. Excluded Downtime log.** Each invocation of Excluded Downtime under Section 5, with category (a)–(m), supporting reason, Customer notification timestamp.

**5. Service Credit log.** Each Service Credit (automatic or claimed), Calendar Month, percentage, euro value, invoice applied.

**6. Regulatory-incident summary.** Where an incident in the period was reported under GDPR Article 33, NIS2 Article 23, DORA Article 19 or CRA Article 14: brief summary, recipient authority, reporting-deadline status. Otherwise a single line confirming none occurred.

**7. Forward-looking section.** Planned Scheduled Maintenance windows, planned changes to the Availability Target or measurement method, anticipated changes to Vendor's certifications (EUCS, ISO 27001, BSI-Grundschutz).

---

## Merge fields used

Mustache-style merge fields used in this template. Search-and-replace each before execution.

```
Parties / Service:    {{Vendor Legal Name}}, {{Customer Legal Name}}, {{CSA Effective Date}},
                      {{Effective Date}}, {{Service Name}}, {{Service URL}}, {{API URL}},
                      {{Status Page URL}}, {{Documentation URL}}, {{Forum City}}
Support:              {{Support Portal URL}}, {{Support Email}}, {{Support Channels}},
                      {{Support Hours}}, {{Support Time Zone}}, {{On-call Paging Channel}}
Security contacts:    {{Vendor Security Email}}, {{Customer Security Email}},
                      {{ENISA Reporting Email}}, {{National CSIRT}}
Regulatory scope:     {{Vendor DORA Class}} (FE-ICT-TPP / N/A),
                      {{Vendor NIS2 Class}} (essential / important / N/A),
                      {{CRA Scope Statement}}, {{EUCS Assurance Level}} (basic / substantial / high / N/A),
                      {{EUCS Certificate ID}}, {{Vendor KRITIS Class}},
                      {{Vendor IT-Grundschutz Status}}
Availability:         {{Uptime Tier}}, {{Uptime Measurement Method}}, {{Latency Threshold}}
Maintenance:          {{Maintenance Window}}, {{Maintenance Notice Window}},
                      {{Emergency Notice Window}}, {{Scheduled Maintenance Cap Hours}}
Credits:              {{Credit Cap Percent}}, {{Credit Window Days}}, {{Major Outage Hours}}
Reporting:            {{Reporting Cadence}}
Severity targets:     {{P1 Response Target}}, {{P1 Resolution Target}}, {{P2 Response Target}},
                      {{P3 Response Target}}, {{P4 Response Target}}
DR:                   {{RTO}}, {{RPO}}
Termination:          {{Termination Threshold}}, {{Consecutive Termination Months}},
                      {{Aggregate Termination Months}}, {{Single Outage Termination Hours}}
Incident SLAs:        {{Vendor Breach SLA}} (default 24h GDPR Art. 33),
                      {{Major ICT Incident SLA}} (default 2h DORA Art. 19),
                      {{CRA Active Exploitation Window}} (default 24h)
Insurance:            {{Insurance Cyber Limit}} (default EUR 5,000,000)
```

---

## Authoritative references

Public, permissively-licensed or public-domain materials that informed this template. Listed for verification, not incorporated.

- **EU primary legislation (eur-lex.europa.eu).** Reg. (EU) 2022/2554 (DORA); Dir. (EU) 2022/2555 (NIS2); Reg. (EU) 2024/2847 (CRA); Reg. (EU) 2023/2854 (Data Act); Reg. (EU) 2016/679 (GDPR); Dir. 2002/58/EC (ePrivacy) and Reg. (EU) 611/2013; Dir. (EU) 2019/770 (DCD); Reg. (EU) 2022/2065 (DSA, clear-language reference); Commission Implementing Decision (EU) 2021/914 (SCCs).
- **EU agencies.** ENISA guidelines on cloud cybersecurity, coordinated-vulnerability-disclosure, EU-CyCLONe. EDPB Guidelines 9/2022 on personal-data-breach notification.
- **ESAs.** EBA, EIOPA, ESMA joint regulatory technical standards under DORA.
- **Germany.** BSI-Standards 200-1 / 200-2 / 200-3 (IT-Grundschutz); BSI-KritisV at gesetze-im-internet.de (public domain); BfDI; BaFin and Deutsche Bundesbank.
- **Permissively-licensed drafting baselines.** Bonterms SLA (CC-BY-4.0); Common Paper CSA v2.1 SLA exhibit (CC-BY-4.0); GitHub `site-policy` (CC0); Mozilla legal templates (MPL-2.0); Linux Foundation and Apache SLAs (Apache-2.0).

No proprietary cloud-provider SLA template was consulted. No five-or-more-word verbatim run from any source appears in the operative text.

---

## Not legal advice

This template is provided "as is" under the MIT license in `LICENSE.md`. It is a starting point, not legal advice, and not a substitute for legal advice. Use does not create a lawyer-client relationship between Fordæmi ehf. (or any contributor) and the user. Every deployment must be reviewed by qualified counsel admitted in the relevant Member State(s) and by Vendor's Head of Engineering or SRE before signing. Mandatory EU and Member-State provisions — consumer-protection, data-protection, employment, and sector-specific financial, telecommunications and critical-infrastructure rules — apply regardless of anything here and prevail over inconsistent terms. `[VERIFY]` flags mark items that must be confirmed against current authoritative sources before execution.
