---
title: Service Level Agreement — United Kingdom
jurisdictions: [uk, gb]
statutes: [NIS-Regs-2018-SI-506, UK-GDPR, DPA-2018, DUAA-2025, FCA-Handbook, PRA-Rulebook]
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

# Service Level Agreement — United Kingdom

**Vendor:** {{Vendor Legal Name}} ("{{Vendor Short Name}}"), Companies House registered number {{Companies House Number}} `[OPTIONAL]`, ICO Registration {{ICO Registration Number}} `[OPTIONAL]`.

**Customer:** {{Customer Legal Name}} ("{{Customer Short Name}}").

**Effective date:** {{Effective Date}}. **Last updated:** {{Last Updated Date}}.

This Service Level Agreement (the "**SLA**") forms Exhibit B to the parties' Cloud Service Agreement (the "**CSA**") or, where executed standalone, governs the service-level commitments between the parties for the {{Service Name}} cloud service. The SLA is drafted as a business-to-business instrument and is governed by the laws of England and Wales unless the CSA designates Scotland or Northern Ireland.

The SLA reads alongside the parties' Data Processing Agreement (the "**DPA**"). Where the SLA refers to a personal data breach, the DPA's notification machinery is the controlling text; this SLA addresses the operational availability and incident-response timing that supports the DPA.

---

## 1. Plain-language summary

In short: {{Vendor Short Name}} commits to keep the {{Service Name}} service available {{Uptime Tier}} of the time, to respond to support tickets within set windows, to issue service credits when it falls short, and to coordinate incident reporting so {{Customer Short Name}} can meet its UK GDPR Article 33, NIS Regulations 2018, and (where applicable) FCA or PRA operational-resilience obligations.

This SLA uses **dual-perspective drafting** in the sections most often negotiated — §4 (uptime tier), §5 (excluded downtime), §6 (support targets), §7 (credit cap), §11 (recovery objectives), and §14 (termination threshold). Each carries three labelled variants: **Customer-favourable**, **Vendor-favourable**, and **Market-standard**. Pick one per section, delete the others, and reconcile the resulting picks so the document is internally consistent.

The first sentence of each section restates the operative point in plain English. Provisions flagged `[VERIFY]` mark areas that move with regulation: the Cyber Security and Resilience Bill is in flight, the Data (Use and Access) Act 2025 (the "**DUAA**") is being commenced in stages, the FCA SYSC 15A.6 framework continues to be refined, and ICO penalty ceilings are subject to ministerial revision.

This SLA is not legal advice. Have it reviewed by qualified UK counsel before adoption.

---

## 2. Definitions

In short: this section explains key terms used in the SLA. UK GDPR, DPA 2018, NIS Regulations 2018, FCA Handbook, and PRA Rulebook terms carry their statutory meaning.

**2.1 "Available"** — an Authorised User can authenticate, send a request, and receive a substantive response, measured by the {{Uptime Measurement Method}}.

**2.2 "Availability Percentage"** — the figure produced by the §4.2 formula for a calendar month, to two decimal places.

**2.3 "CAF"** — the NCSC Cyber Assessment Framework. **2.4 "Cyber Essentials"** — the NCSC-backed CE / CE+ schemes operated by IASME `[VERIFY current operator]`.

**2.5 "Excluded Downtime"** — the categories listed in §5. **2.6 "FCA"** — the Financial Conduct Authority. **2.7 "PRA"** — the Prudential Regulation Authority of the Bank of England. **2.8 "ICO"** — the Information Commissioner's Office. **2.10 "NCSC"** — the National Cyber Security Centre.

**2.9 "Major ICT Incident"** — an ICT incident that, were it to affect a firm in scope of FCA SYSC 15A.6 or PRA SS1/21, would meet the regulator's threshold for disruption of an important business service beyond impact tolerance.

**2.11 "NIS Regulations"** — the Network and Information Systems Regulations 2018 (SI 2018/506). **2.12 "OES"** — Operator of Essential Services (NIS Regs reg.8). **2.13 "RDSP"** — Relevant Digital Service Provider (NIS Regs reg.1(3)).

**2.14 "Personal Data Breach"** — Article 4(12) UK GDPR. **2.15 "Severity Level" / P1–P4** — Annex A. **2.16 "Status Page"** — {{Status Page URL}}. **2.17 "Total Minutes"** — minutes in the calendar month.

**2.18 "UK GDPR"** — the GDPR as part of UK law under EUWA 2018 s.3, read with the DPA 2018.

---

## 3. Scope of services covered

In short: this SLA covers the production environment of the Service. Sandbox, beta, and trial environments are excluded unless an Order Form says otherwise.

**3.1 In-scope environments.** The availability and support commitments below apply to the production tier of the Service identified on the relevant Order Form. Sandbox, development, staging, beta, evaluation, and free-trial environments are provided on a best-efforts basis with no SLA.

**3.2 In-scope features.** Core platform functionality (authentication, primary read/write API, primary user interface) is covered. Optional add-ons, AI/ML features in preview, and third-party integrations are covered only where the Order Form expressly lists them.

**3.3 Vendor regulatory classification under UK law.** {{Vendor Short Name}}'s status under UK cyber and operational-resilience regimes is set out below and may be amended by notice to {{Customer Short Name}}.

(a) **NIS Regulations 2018 — `{{Vendor NIS Class}}`** (OES / RDSP / Not in scope). RDSPs are supervised by the ICO; OESes are supervised by the sectoral competent authority (Ofgem, Ofcom/DfT, DWI/Defra, DHSC, etc.).

(b) **FCA — `{{Vendor FCA Class}}`**. Where {{Customer Short Name}} is FCA-authorised and subject to SYSC 15A.6, {{Vendor Short Name}} accepts the cooperation obligations in §11 and §17 as a third party supporting an important business service.

(c) **PRA — `{{Vendor PRA Class}}`**. Where {{Customer Short Name}} is PRA-regulated, equivalent obligations apply under the PRA Rulebook and SS1/21.

(d) **Online Safety Act 2023.** Where {{Customer Short Name}} provides a regulated user-to-user or search service, {{Vendor Short Name}} supports {{Customer Short Name}}'s Ofcom transparency reporting under §10.

**3.4 Out of scope.** Not covered: connectivity from {{Customer Short Name}}'s network to the public internet; failures of {{Customer Short Name}}'s end-user devices, browsers, or identity provider; misconfiguration by {{Customer Short Name}}; and any matter covered by Excluded Downtime in §5.

---

## 4. Service Availability commitment

In short: {{Vendor Short Name}} commits to a monthly Availability Percentage of {{Uptime Tier}} for the production Service.

**4.1 Commitment.** {{Vendor Short Name}} will use commercially reasonable efforts to make the production Service Available, measured per §4.2, at not less than {{Uptime Tier}} for each calendar month of the Subscription Term.

**4.2 Calculation formula.** For each calendar month:

```
Availability % = ((Total Minutes − Unplanned Downtime Minutes) / Total Minutes) × 100
```

where Unplanned Downtime Minutes excludes Excluded Downtime under §5. The figure is rounded to two decimal places. {{Vendor Short Name}} measures availability using the {{Uptime Measurement Method}}.

**4.3 Dual-perspective drafting.**

> **Customer-favourable.** Commit not less than 99.95%; Annex B credits cap at 50% of Monthly Service Fee; credits do not displace damages for material breach.

> **Market-standard.** Commit {{Uptime Tier}} (default 99.9%); Annex B credits are exclusive financial remedy, capped at 30%, subject to the §14 termination right for material breach.

> **Vendor-favourable.** Target {{Uptime Tier}} (default 99.5%); Annex B credits are sole and exclusive remedy, capped at 15%.

**4.4 Reasonableness review.** Any exclusivity-of-remedy limitation is subject to the s.11 UCTA 1977 reasonableness test; §9 is drafted to satisfy that test in ordinary commercial dealings between parties of comparable bargaining power.

---

## 5. Excluded Downtime

In short: certain categories of unavailability do not count against the Availability Percentage.

**5.1 General exclusions.** "Excluded Downtime" means unavailability caused by:

(a) Scheduled Maintenance announced under §12; (b) Emergency Maintenance announced under §12; (c) force majeure (as defined in the CSA), including widespread internet failure, undersea-cable cuts, large-scale DDoS beyond commercially reasonable mitigation, and pandemic-related staff incapacity; (d) acts or omissions of {{Customer Short Name}}, its Authorised Users, or its third-party integrations; (e) use inconsistent with the Documentation or AUP; (f) suspension under the CSA for non-payment, AUP breach, security risk, or regulator direction; (g) failures of public internet, DNS, or third-party authentication providers outside {{Vendor Short Name}}'s direct control; (h) any beta, preview, sandbox, or evaluation feature; (i) failures attributable to a third-party service the Customer has chosen to integrate; (j) actions taken at {{Customer Short Name}}'s written request, including uncoordinated penetration or load tests; (k) performance below an SLA-bound threshold for less than the minimum measurement interval in §4.2;

(l) **Service interruption mandated by the ICO, FCA, PRA, NCSC, or any other UK supervisory or competent authority**, including any direction under the NIS Regulations 2018, the Online Safety Act 2023, or the financial-services supervisory regime; and

(m) **National security or counter-terrorism direction under the Investigatory Powers Act 2016**, including a technical capability notice (s.253) or national-security notice (s.252), the existence or content of which {{Vendor Short Name}} may be lawfully prohibited from disclosing.

**5.2 Dual-perspective drafting.**

> **Customer-favourable.** Categories (g), (i), (j) excluded only where {{Vendor Short Name}} shows with contemporaneous logs that the third-party or customer-side cause is the primary cause; mixed causes count pro-rata.

> **Market-standard.** Reasonable, good-faith assessment using contemporaneous monitoring data; on request a written explanation of any contested exclusion within 15 Business Days.

> **Vendor-favourable.** {{Vendor Short Name}}'s reasonable assessment of (a)–(m) is final save for manifest error.

---

## 6. Support response & resolution targets

In short: support tickets are triaged P1 to P4. {{Vendor Short Name}} commits to first-response and resolution targets per the matrix in Annex A.

**6.1 Channels.** {{Customer Short Name}} may raise tickets through {{Support Channels}}. P1 incidents may be escalated to {{Vendor Short Name}}'s on-call engineer through the channel marked "P1" on the Status Page.

**6.2 Hours.** Support is provided {{Support Hours}}. The default Support time zone is **London (GMT in winter, BST in summer)**. Where the Order Form specifies a global follow-the-sun model, the relevant regional centre handles the ticket according to its local time.

**6.3 Severity definitions.** Annex A sets out the P1 to P4 definitions and targets. P1 means the production Service is unavailable to substantially all Authorised Users or there is severe data loss or a confirmed security incident affecting Customer Data. P2 means major-feature impairment with a workaround. P3 means minor-feature impairment. P4 means a question, documentation request, or cosmetic issue.

**6.4 Targets.** Default first-response targets: {{P1 Response Target}} (default 15 minutes), {{P2 Response Target}} (default 1 hour), {{P3 Response Target}} (default 4 Business Hours), and {{P4 Response Target}} (default 1 Business Day). P1 resolution or workaround target: {{P1 Resolution Target}} (default 4 hours).

**6.5 Dual-perspective drafting.**

> **Customer-favourable.** Resolution targets binding; P1 resolution miss triggers a 1-day Monthly Service Fee credit per occurrence in addition to §4 credits.

> **Market-standard.** Response targets binding; resolution targets good-faith. Written post-incident review for any P1 within ten Business Days.

> **Vendor-favourable.** Response targets are good-faith; missing a target is not in itself a breach where {{Vendor Short Name}} is using continuous reasonable efforts to triage and resolve.

**6.6 Out-of-scope tickets.** Tickets relating to features explicitly out of scope under §3, third-party integrations, or matters listed in §5 are handled on a best-efforts basis without commitment.

---

## 7. Service Credits

In short: where {{Vendor Short Name}} fails to meet the Availability Percentage in §4, {{Customer Short Name}} earns Service Credits per Annex B.

**7.1 Credit ladder.** Annex B sets out the Service Credit ladder by Availability Percentage achieved. Default values mirror typical market pricing for the chosen uptime tier.

**7.2 Cap.** Total Service Credits in any calendar month do not exceed {{Credit Cap Percent}} (default 30%) of the Monthly Service Fee for the affected production Service.

**7.3 Calculation base.** Credits are calculated against the Monthly Service Fee actually billed for the affected production Service, excluding one-off implementation fees, professional services fees, and pass-through usage charges from third parties unless the Order Form provides otherwise.

**7.4 Stacking.** Where {{Customer Short Name}} is entitled to a credit for both an availability shortfall under §4 and a support-target breach under §6 (Customer-favourable variant only), the credits stack up to the cap.

**7.5 UCTA reasonableness.** The parties acknowledge that the cap and the exclusivity provision in §9 are subject to the Unfair Contract Terms Act 1977 reasonableness test where applicable. They are drafted on the footing that the parties are businesses of comparable bargaining power dealing in commercial cloud services and that the availability of damages for material breach (§14) and for non-excludable matters (§16) is preserved.

**7.6 Dual-perspective drafting.**

> **Customer-favourable.** Cap 50% of Monthly Service Fee; credits do not displace damages for material breach; the cap is computed before any DPA-side liability.

> **Market-standard.** Cap 30%; credits exclusive for matters covered, subject to §9 and non-excludable matters in §16.

> **Vendor-favourable.** Cap 15%; credits sole and exclusive for any availability or support-target failure.

---

## 8. Credit request procedure

In short: {{Customer Short Name}} must request credits in writing within {{Credit Window Days}} of the affected month.

**8.1 Form of request.** A request must (a) identify the calendar month; (b) cite the relevant ticket numbers, Status Page incident IDs, or independent monitoring evidence; and (c) state the credit claimed.

**8.2 Window.** A request submitted more than {{Credit Window Days}} (default 60 days) after the end of the affected calendar month is waived, save where {{Customer Short Name}} demonstrates that {{Vendor Short Name}}'s reporting under §10 was inaccurate or incomplete.

**8.3 Channel.** Requests are submitted to the contractual notice address in the CSA or, if more practical, through the Support portal as a P3 ticket marked "SLA Credit Request".

**8.4 Response time.** {{Vendor Short Name}} acknowledges receipt within five (5) Business Days and issues a determination within fifteen (15) Business Days.

---

## 9. Credit issuance & exclusivity as remedy

In short: approved credits are applied to the next invoice. Service Credits are the exclusive financial remedy for the matters they cover, subject to UCTA reasonableness and non-excludable matters.

**9.1 Issuance.** Approved credits appear as a line item on the next invoice after determination, or, where {{Customer Short Name}} has prepaid in full, are issued as a refund within thirty (30) days of the end of the Subscription Term.

**9.2 No cash redemption.** Credits are not redeemable for cash except on termination as set out in §9.1.

**9.3 Exclusivity.** Subject to §9.4, Service Credits are {{Customer Short Name}}'s exclusive financial remedy for any failure of {{Vendor Short Name}} to meet the Availability Percentage in §4 or, where the Vendor-favourable variant of §6 is selected, the support-response targets.

**9.4 Carve-outs.** §9.3 does not limit: (a) {{Customer Short Name}}'s right to terminate for material breach of this SLA under §14; (b) any non-excludable liability under sections 2(1) and 6(1)–(2) of the Unfair Contract Terms Act 1977 (death and personal injury caused by negligence; statutory implied terms as to title); (c) liability for fraud or fraudulent misrepresentation; (d) liability for breach of confidentiality or for breach of the DPA; or (e) any other liability that cannot lawfully be excluded under English law.

**9.5 Reasonableness reservation.** Should a court of competent jurisdiction find the exclusivity-as-remedy provision unreasonable under section 11 UCTA in {{Customer Short Name}}'s circumstances, the Service Credits remain payable and the Cap continues to apply only to the extent it remains reasonable; the balance of any liability for the same matter is governed by the CSA's overall liability framework.

---

## 10. Performance reporting & status page

In short: {{Vendor Short Name}} publishes incidents on the Status Page in near-real time and issues a monthly SLA report.

**10.1 Status Page.** The Status Page at {{Status Page URL}} publishes ongoing-incident notices, post-incident reviews, and the rolling availability figure for the trailing thirty (30) days.

**10.2 Monthly report.** Within {{Reporting Cadence}} (default ten Business Days) of each month-end, {{Vendor Short Name}} publishes a monthly SLA report in the format at Annex C, including (a) Availability Percentage; (b) total Excluded Downtime by category; (c) ticket volume by Severity Level; (d) median and 95th-percentile first-response times; and (e) any Service Credits earned.

**10.3 RSS / webhook.** The Status Page exposes a public RSS feed and a webhook endpoint for incident notices to allow {{Customer Short Name}}'s monitoring stack to subscribe.

**10.4 Online Safety Act assistance.** Where {{Customer Short Name}} is in scope of the Online Safety Act 2023 transparency-reporting regime, {{Vendor Short Name}} will provide on reasonable request the operational data within its possession (for example, uptime histograms and incident breakdowns) that {{Customer Short Name}} requires for its annual Ofcom transparency report.

---

## 11. Disaster recovery & business continuity

In short: {{Vendor Short Name}} maintains documented disaster-recovery and business-continuity plans, and aligns to NCSC Cyber Essentials, the Cyber Assessment Framework where applicable, ISO 27001/27017, and the FCA / PRA operational-resilience expectations.

**11.1 RTO / RPO.** {{Vendor Short Name}} commits to a Recovery Time Objective of {{RTO}} (default 4 hours) and a Recovery Point Objective of {{RPO}} (default 1 hour) for the production Service.

**11.2 Plans.** {{Vendor Short Name}} maintains documented disaster-recovery and business-continuity plans, tested at least annually. Test summaries are made available under NDA on reasonable request.

**11.3 Geographic redundancy.** Production data is replicated across at least two UK or EEA regions. Cross-region failover is exercised at least annually.

**11.4 Backups.** Encrypted backups are retained for the period stated in the DPA. Restoration tests are run at least quarterly.

**11.5 NCSC Cyber Essentials.** {{Vendor Short Name}} maintains `{{NCSC Cyber Essentials Level}}` (one of: Cyber Essentials / Cyber Essentials Plus / Not certified) for the in-scope environment. Where Cyber Essentials Plus is selected, {{Vendor Short Name}} renews the certification annually and provides the certificate to {{Customer Short Name}} on request.

**11.6 NCSC Cyber Assessment Framework.** Where {{Customer Short Name}} is in UK critical national infrastructure or the public sector, {{Vendor Short Name}} engages with {{Customer Short Name}}'s CAF mapping across the four CAF objectives (manage risk; protect against attack; detect events; minimise impact) and provides evidence packs supporting "achieved / partially / not achieved" determinations. `[VERIFY current CAF version]`.

**11.7 NCSC Active Cyber Defence.** Where applicable, {{Vendor Short Name}} integrates with ACD services (takedown, mail check, web check, protective DNS) and shares telemetry summaries on request.

**11.8 ISO 27001 / 27017.** {{Vendor Short Name}} maintains ISO 27001, and ISO 27017 where applicable, with certificates available on request.

**11.9 ISAE 3000 / SOC 2 Type II.** {{Vendor Short Name}} obtains an annual ISAE 3000 or SOC 2 Type II report, available under NDA.

**11.10 FCA SYSC 15A.6 (Customer FCA-regulated).** {{Vendor Short Name}} (a) cooperates in identifying important business services and impact tolerances; (b) supplies mapping data on its part of the resource chain; (c) participates in severe-but-plausible scenario testing on reasonable request; and (d) provides data demonstrating that {{Customer Short Name}} can remain within impact tolerance. `[VERIFY current SYSC 15A version]`.

**11.11 PRA SS1/21 (Customer PRA-regulated).** Equivalent obligations apply under SS1/21 and the PRA Rulebook Operational Resilience and Outsourcing parts.

**11.12 Dual-perspective drafting (RTO / RPO).**

> **Customer-favourable.** RTO 1 hour, RPO 15 minutes; miss triggers a 5% Monthly Service Fee credit per occurrence on top of §4 credits.

> **Market-standard.** RTO 4 hours, RPO 1 hour; misses reported in the monthly SLA report and trigger a written post-incident review.

> **Vendor-favourable.** RTO 24 hours, RPO 24 hours as good-faith targets; no credit consequences absent gross negligence.

---

## 12. Scheduled & emergency maintenance

In short: routine maintenance happens during a published window with notice; emergency maintenance happens with as much notice as the security or stability of the Service permits.

**12.1 Scheduled Maintenance.** {{Vendor Short Name}} performs Scheduled Maintenance during {{Maintenance Window}} (default Saturdays 02:00–06:00 UTC) with at least {{Maintenance Notice Window}} (default seven days) notice through the Status Page and email.

**12.2 Emergency Maintenance.** Where a security vulnerability, infrastructure failure, or supplier emergency requires immediate action, {{Vendor Short Name}} performs Emergency Maintenance with {{Emergency Notice Window}} (default two hours) notice where reasonably feasible, or as soon as practicable thereafter.

**12.3 Communication.** Both Scheduled and Emergency Maintenance windows are recorded on the Status Page and excluded from the Availability Percentage calculation per §5.

**12.4 Exceptional regulatory or law-enforcement direction.** Where the ICO, FCA, PRA, NCSC, the courts, or another competent UK authority issues a direction requiring an unscheduled change to or interruption of the Service, {{Vendor Short Name}} treats the change as Emergency Maintenance and provides such notice as the lawful direction permits.

---

## 13. Service degradation vs. outage

In short: not every problem is an outage. This section explains how slow performance, partial-feature failure, and full outage are treated.

**13.1 Outage.** A full outage is unavailability of the production Service to substantially all Authorised Users for at least the minimum measurement interval. An outage counts in full against the Availability Percentage.

**13.2 Partial failure.** Where a discrete major feature is unavailable but the remainder of the Service is functional, the affected period counts pro-rata against the Availability Percentage based on the fraction of monthly active users or API calls affected (as recorded by {{Vendor Short Name}}'s telemetry).

**13.3 Degradation.** Sustained latency or error-rate degradation that exceeds the threshold defined on the Status Page (default p95 latency above 2× rolling baseline, or 5xx error rate above 1%, in each case for at least five consecutive minutes) is treated as a partial failure and reported as a P1 or P2 per Annex A.

**13.4 Minor incidents.** Brief or localised incidents below the threshold are recorded internally and surfaced in the monthly SLA report but do not in themselves count against the Availability Percentage.

---

## 14. Material SLA breach & termination right

In short: persistent SLA failure gives {{Customer Short Name}} a right to terminate for material breach without further cure period.

**14.1 Right to terminate.** {{Customer Short Name}} may terminate the affected Order Form for material breach if the Availability Percentage falls below the committed {{Uptime Tier}} for {{Termination Threshold}} (default any three (3) calendar months in any rolling six-month period) or if there is a single calendar month with Availability Percentage below 95%.

**14.2 Refund on termination.** Where {{Customer Short Name}} terminates under §14.1, {{Vendor Short Name}} refunds pre-paid Fees pro-rated to the date of termination for the affected production Service.

**14.3 Damages preserved.** Termination under §14 does not preclude damages for material breach where the parties have not adopted the Vendor-favourable variant of §9, subject to the CSA's overall liability framework and to UCTA reasonableness.

**14.4 Dual-perspective drafting.**

> **Customer-favourable.** Trigger on any two consecutive months below the committed level or a single month below 98%; damages preserved subject to the CSA cap.

> **Market-standard.** Trigger on any three of any rolling six months below the committed level, or a single month below 95%; Service Credits remain exclusive for the triggering months.

> **Vendor-favourable.** Trigger only on three consecutive months below the committed level; this is the sole and exclusive remedy for that pattern.

---

## 15. Changes to this SLA

In short: {{Vendor Short Name}} may improve the SLA but may not materially worsen it without {{Customer Short Name}}'s consent.

**15.1 Improvements.** {{Vendor Short Name}} may unilaterally raise the Availability Percentage, shorten response targets, broaden Excluded Downtime in {{Customer Short Name}}'s favour, or expand reporting on notice through the Status Page.

**15.2 Material adverse change.** Any change that materially reduces the Availability Percentage, broadens Excluded Downtime, lengthens response or resolution targets, lowers RTO / RPO commitments, or reduces the Service Credit ladder requires {{Customer Short Name}}'s prior written consent.

**15.3 Regulatory updates.** Where a change is necessary to comply with a UK statute, statutory instrument, or regulator direction (including the Cyber Security and Resilience Bill once enacted, the DUAA, or an FCA / PRA rulebook update), {{Vendor Short Name}} may make the change on the minimum notice the law allows and will document the regulatory basis on the Status Page.

---

## 16. Survival & order of precedence

In short: the SLA reads with the CSA. The CSA's order-of-precedence clause governs conflicts.

**16.1 Survival.** Sections 7 (Service Credits earned but not yet issued), 8 (credit request), 9 (issuance), 16 (this section), and any incident-reporting obligations triggered before termination survive expiry or termination of the Order Form.

**16.2 Order of precedence.** This SLA is Exhibit B to the CSA. The CSA's order-of-precedence clause governs any conflict, with the DPA prevailing on data-protection terms, the SLA prevailing on service-level terms, and the Master Agreement prevailing on general terms.

**16.3 Severability.** Where any provision of this SLA is held to be unenforceable, the remainder continues in force and the parties will negotiate in good faith a replacement clause that achieves the closest lawful effect.

---

## 17. Incident-response coordination for UK breach notification

In short: where an incident triggers UK GDPR Art. 33, the NIS Regulations 2018, FCA SYSC 15A.6, or the PRA Rulebook, {{Vendor Short Name}} delivers timely information so {{Customer Short Name}} can meet its deadlines.

**17.1 UK GDPR Article 33 — Personal Data Breach.** Where {{Vendor Short Name}} acts as processor and becomes aware of a Personal Data Breach, it notifies {{Customer Short Name}} (the controller) without undue delay. The notification SLA is **{{Vendor Breach SLA}}** (default 24 hours from awareness). {{Customer Short Name}} retains the onward 72-hour notification to the ICO under Art. 33(1) and any Art. 34 notification to data subjects. Notification content is governed by the DPA.

**17.2 NIS Regulations 2018 — incident reporting.** (a) If {{Vendor Short Name}} is an OES, it notifies its designated competent authority within 72 hours under reg.11. (b) If {{Vendor Short Name}} is an RDSP, it notifies the ICO within 72 hours under reg.12 of any incident with substantial impact. (c) {{Vendor Short Name}} will inform {{Customer Short Name}} of any NIS reporting that may indirectly affect {{Customer Short Name}}, so far as lawfully able.

**17.3 FCA SYSC 15A.6 — operational resilience.** Where {{Customer Short Name}} is FCA-authorised, {{Vendor Short Name}} commits to **{{Major ICT Incident SLA}}** (default 2 hours from awareness) for initial notification of any Major ICT Incident affecting an important business service. Fuller technical assessment follows within 24 hours. {{Customer Short Name}} retains its onward duties under PRIN 11 / SUP 15.3 and SYSC 15A.6.

**17.4 PRA Rulebook / SS1/21.** Where {{Customer Short Name}} is PRA-regulated, the same 2-hour SLA supports notifications under the PRA Rulebook Notifications Part and SS1/21.

**17.5 Investigatory Powers Act 2016.** Good-faith compliance with a technical capability notice (s.253), national-security notice (s.252), or warrant compelling {{Vendor Short Name}} to disable or modify the Service is not a breach of this SLA. {{Vendor Short Name}} discloses the existence and scope only so far as law permits.

**17.6 Online Safety Act 2023.** Where {{Customer Short Name}} provides an in-scope user-to-user or search service, on request {{Vendor Short Name}} supplies operational metrics relevant to {{Customer Short Name}}'s annual Ofcom transparency report (ss.64–66 OSA 2023).

**17.7 Cyber Security and Resilience Bill (DSIT, expected 2025–2026).** `[VERIFY Bill status at adoption]`. Likely to expand NIS scope (for example, to managed service providers and some data-centre operators), to widen incident reporting, and to add ICO and sectoral powers. {{Vendor Short Name}} will update §17 through the §15.3 regulatory-update mechanism on commencement.

---

## 18. Insurance & cyber liability

In short: {{Vendor Short Name}} carries cyber and PI insurance per the CSA, calibrated to UK GDPR ceilings and incident-response costs.

**18.1 Cover.** Cyber and PI cover per the CSA insurance clause, with cyber cover not less than {{Insurance Cyber Limit}} (default GBP 5,000,000) per occurrence for the production tier.

**18.2 ICO penalty ceilings.** UK GDPR maxima are the higher of GBP 17.5M or 4% of global turnover for the most serious infringements, and the higher of GBP 8.7M or 2% otherwise `[VERIFY against any DUAA-driven adjustment]`. The CSA cap applies to non-statutory liabilities; statutory penalties are borne by the levied party as a matter of public law.

**18.3 Evidence.** Annual certificate of insurance available on request.

---

## 19. Governing law & supervision

In short: governed by the law selected in the CSA. ICO, FCA, PRA, and other UK regulators retain their statutory supervisory powers regardless of contract.

**19.1 Governing law.** England and Wales, or the alternative UK jurisdiction selected on the Order Form.

**19.2 ICO powers preserved.** Nothing limits ICO powers under the DPA 2018 and UK GDPR (investigation, audit, enforcement notices, administrative fines).

**19.3 FCA / PRA direct examination.** Where {{Customer Short Name}} is FCA- or PRA-regulated, those regulators may (under the FCA Handbook, PRA Rulebook, or s.165A FSMA 2000 where applicable) require direct access to {{Vendor Short Name}}'s records, premises, and personnel relating to outsourced services supporting {{Customer Short Name}}'s regulated activity. {{Vendor Short Name}} cooperates consistently with §17.5 and confidentiality obligations.

**19.4 Other supervisory authorities.** Sectoral authorities (Ofgem, Ofcom, DfT, DWI, DHSC, Welsh and Scottish Ministers, etc.) retain statutory powers for OES sectors.

---

## 20. Optional appendix — Data (Use and Access) Act 2025 (DUAA)

In short: the DUAA reshapes parts of the UK data-protection regime. Provisions affect incident reporting, automated decision-making, and ICO enforcement. `[VERIFY — DUAA phased commencement; some provisions may not be in force at adoption]`.

**20.1 ICO powers.** The DUAA expands the ICO's investigatory and enforcement toolkit (new information- and assessment-notice powers; refreshed governance arrangements with the ICO becoming the Information Commission `[VERIFY]`; refined procedural rules). On commencement, {{Vendor Short Name}} cooperates with ICO action affecting the Service.

**20.2 Penalty ceilings.** ICO ceilings remain aligned with UK GDPR (the higher of GBP 17.5M or 4% of global turnover for the most serious infringements; GBP 8.7M or 2% otherwise) `[VERIFY against latest ICO guidance]`. The DUAA refines procedure rather than raising the caps.

**20.3 Automated decision-making (Article 22).** The DUAA broadens permitted solely automated decisions subject to safeguards (human review; representations; the right to contest). Where the Service contributes AI Output to such a decision, the DPA governs safeguards; this SLA supports human-review workflows through §6 response targets.

**20.4 Smart data, DVS, and complaints.** Where smart-data, digital-verification-services, or ICO-complaints provisions commence and apply, {{Vendor Short Name}} updates the Service and this SLA through §15.3.

**20.5 Phased commencement.** Several DUAA provisions commence by ministerial order. References to DUAA sections mean the provision as in force at the relevant time. `[VERIFY commencement orders at adoption]`.

---

## Annex A — Severity matrix

In short: this matrix defines P1 to P4 and the response and resolution targets that apply.

| Severity | Definition | First-response target | Resolution / workaround target | Channels |
|---|---|---|---|---|
| **P1 — Critical** | Production Service unavailable to substantially all Authorised Users; severe data loss; confirmed security incident affecting Customer Data. | {{P1 Response Target}} (default 15 minutes) | {{P1 Resolution Target}} (default 4 hours) | Pager + Status Page + ticket |
| **P2 — High** | Major-feature impairment with workaround; degraded performance affecting a substantial subset of Authorised Users. | {{P2 Response Target}} (default 1 hour) | 1 Business Day | Ticket + Status Page where customer-visible |
| **P3 — Medium** | Minor-feature impairment; cosmetic but functional defect. | {{P3 Response Target}} (default 4 Business Hours) | 5 Business Days | Ticket |
| **P4 — Low** | Question, documentation request, cosmetic issue without functional impact. | {{P4 Response Target}} (default 1 Business Day) | Best efforts | Ticket |

Severity is initially assessed by {{Customer Short Name}} when raising the ticket and may be reclassified by {{Vendor Short Name}} acting reasonably on the basis of the technical facts. Disputes about severity classification are raised under the dispute-resolution clause of the CSA.

---

## Annex B — Service Credit calculation

In short: this annex gives the Service Credit ladder by Availability Percentage achieved.

**B.1 Default ladder for a {{Uptime Tier}} = 99.9% commitment.**

| Monthly Availability Percentage achieved | Service Credit (% of Monthly Service Fee) |
|---|---|
| ≥ 99.9% | 0% |
| ≥ 99.0% and < 99.9% | 10% |
| ≥ 98.0% and < 99.0% | 15% |
| ≥ 95.0% and < 98.0% | 25% |
| < 95.0% | 30% (or {{Credit Cap Percent}}) |

**B.2 Worked example.** Monthly Service Fee for the affected production Service: GBP 10,000. Achieved Availability Percentage in the calendar month: 98.4%. Applicable credit row: 15%. Credit issued: GBP 1,500, applied as a line item on the next invoice.

**B.3 Stacking with support credits.** Where the Customer-favourable variant of §6 is adopted, support-target breach credits stack with the table above up to the cap.

**B.4 Adjustment for chosen uptime tier.** Where the parties adopt a tier other than 99.9%, the parties agree the equivalent credit ladder by reference to the same ratio of achieved-to-committed downtime; default ladders for 99.5%, 99.95%, and 99.99% commitments are available on request from {{Vendor Short Name}}.

---

## Annex C — Sample monthly SLA report format

In short: this annex shows the structure of the monthly report under §10.

```
{{Service Name}} — SLA report — {{Month YYYY}}

1. Headline: Availability [99.94%] vs committed {{Uptime Tier}};
   Status [met / missed]; Service Credits [£0 / £X].
2. Incidents: ID, severity, start, duration, cause, excluded? Y/N, URL.
3. Excluded Downtime by category: Scheduled / Emergency / force majeure /
   customer-side / regulator direction (§5(l)) / IPA 2016 (§5(m)).
4. Support metrics: tickets by severity; median and p95 first-response.
5. RTO / RPO: recovered incidents and performance against §11.1.
6. Action items: post-incident reviews, certification renewals.
7. Notes: regulator coordination, planned changes.
```

---

## Merge fields used

```
{{Vendor Legal Name}} / {{Vendor Short Name}}
{{Customer Legal Name}} / {{Customer Short Name}}
{{Service Name}} / {{Service URL}} / {{Status Page URL}}
{{Effective Date}} / {{Last Updated Date}}
{{Companies House Number}}                # OPTIONAL
{{ICO Registration Number}}               # OPTIONAL
{{Uptime Tier}}                           # default "99.9%"
{{Uptime Measurement Method}}             # default "synthetic monitoring at 1-minute intervals"
{{Maintenance Window}}                    # default "Saturdays 02:00–06:00 UTC"
{{Maintenance Notice Window}}             # default "seven (7) days"
{{Emergency Notice Window}}               # default "two (2) hours where feasible"
{{Credit Cap Percent}}                    # default "30%"
{{Credit Window Days}}                    # default "60 days"
{{Reporting Cadence}}                     # default "ten (10) Business Days after month-end"
{{P1 Response Target}} / {{P1 Resolution Target}}   # 15 min / 4 hours
{{P2 Response Target}} / {{P3 Response Target}} / {{P4 Response Target}}
{{Support Hours}} / {{Support Channels}}
{{RTO}} / {{RPO}}                         # 4 hours / 1 hour
{{Termination Threshold}}                 # default "any 3 of any rolling 6 months"
{{Vendor NIS Class}}                      # OES / RDSP / Not in scope
{{Vendor FCA Class}} / {{Vendor PRA Class}}
{{NCSC Cyber Essentials Level}}           # CE / CE+ / Not certified
{{Vendor Breach SLA}}                     # default "24 hours" (UK GDPR Art. 33)
{{Major ICT Incident SLA}}                # default "2 hours" (SYSC 15A.6 / SS1/21)
{{Insurance Cyber Limit}}                 # default "GBP 5,000,000"
{{Month YYYY}}
```

---

## Authoritative references

Clean-room drafted from the following permissively-licensed sources; no verbatim text was used.

- **legislation.gov.uk** `[OGL]` — NIS Regulations 2018 (SI 2018/506); DPA 2018; UK GDPR (via EUWA 2018 s.3); DUAA 2025; Investigatory Powers Act 2016; Online Safety Act 2023; UCTA 1977; FSMA 2000.
- **ico.org.uk** `[OGL]` — personal-data-breach guidance; NIS guidance for RDSPs; enforcement framework; UK GDPR fining guidance.
- **ncsc.gov.uk** `[OGL]` — Cyber Essentials / CE+; Cyber Assessment Framework (CAF); incident-management guidance; Active Cyber Defence services.
- **fca.org.uk** — FCA Handbook (SYSC 15A; SUP 15; PRIN 11).
- **bankofengland.co.uk** — PRA Rulebook (Operational Resilience and Outsourcing parts); SS1/21.
- **ofcom.org.uk** `[OGL]` — Online Safety Act transparency-reporting guidance.
- **gov.uk / DSIT** `[OGL]` — Cyber Security and Resilience Bill policy paper.
- **Bonterms SLA** `[CC-BY-4.0]` — clause structure and credit-ladder pattern (primary baseline).
- **Common Paper CSA SLA exhibit v2.1** `[CC-BY-4.0]` — exhibit pattern.
- **GitHub site-policy** `[CC0]`; **Mozilla legal templates** `[MPL-2.0]`; **Linux Foundation / Apache project SLAs** `[Apache-2.0]`.

---

## Not legal advice

This SLA template is provided for general informational purposes and does not constitute legal advice. UK statutory and regulatory obligations evolve continuously: the Cyber Security and Resilience Bill is progressing through Parliament, the DUAA 2025 is being commenced in stages, the FCA SYSC 15A framework continues to be refined, and NCSC Cyber Essentials and CAF schemes are revised periodically. ICO penalty ceilings, FCA Handbook references, and PRA Rulebook references may have changed since the date in the front-matter. Adoption of this template should follow review by qualified UK counsel familiar with the parties' regulatory posture, the in-scope Service architecture, and the relevant supervisory authorities. The dual-perspective drafting choices in §4, §5, §6, §7, §11, and §14 are commercial allocations that must be reconciled with the parties' risk appetite and with the order of precedence in the parent CSA.
