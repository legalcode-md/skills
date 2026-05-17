---
title: Service Level Agreement (Jurisdiction-Neutral Baseline)
jurisdictions: [global]
posture: dual-perspective (customer-favorable / vendor-favorable / market-standard)
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

# Service Level Agreement

**This Service Level Agreement (the "SLA") is issued by {{Vendor Legal Name}} ("Vendor") to {{Customer Legal Name}} ("Customer") in connection with Customer's subscription to {{Service Name}} (the "Service"). It takes effect on {{Effective Date}}, was last updated on {{Last Updated Date}}, and is incorporated by reference into the Master Agreement between the Parties.**

This SLA is drafted in three labelled variants — Customer-favorable, Vendor-favorable, and Market-standard compromise — for clauses where the underlying bargain materially differs by perspective. Other clauses are drafted to a single market-standard form. Pick one variant per labelled clause; do not retain all three in the executed document.

---

## 1. Plain-language summary

*Plain-language: This section is a non-binding orientation. The binding obligations live in Sections 2 through 16 and the three Annexes. Where the summary and the operative text differ, the operative text controls.*

This SLA makes two promises about {{Service Name}}: an uptime promise that the production Service will be available a high percentage of each calendar month, and a support promise that issues will be acknowledged and worked toward resolution within published targets that scale with severity. Both are measured monthly and both have exclusions listed in Section 5.

When Vendor misses a monthly uptime number, Customer receives a Service Credit: a percentage of that month's fees for the Affected Service, calculated under Annex B, capped under Section 7, and applied against a future invoice (not paid in cash). Service Credits are the sole and exclusive remedy for ordinary SLA misses, subject to the Section 14 termination right. To claim a credit, Customer submits a written request within {{Credit Window Days}} of the affected month with the evidence in Section 8, and Vendor validates against monitoring records and Status Page logs.

Two backstops sit alongside the credit regime. Sustained misses across multiple months trigger a termination right with a pro-rata refund (Section 14). Regardless of credits, Vendor commits to disaster-recovery, business-continuity, and reporting practices (Sections 10 and 11). The Status Page at {{Status Page URL}} is the canonical real-time source of truth.

This SLA is subordinate to the Master Agreement on topics outside its subject matter (confidentiality, liability caps, indemnities, governing law) but takes precedence on availability, support targets, and Service Credits per Section 16. An Order Form may override merge-field defaults for a specific subscription.

---

## 2. Definitions

*Plain-language: Capitalized terms used in this SLA have the meanings given here, in the Master Agreement, or in the Order Form. If a term is defined in more than one place, the SLA's definition controls for purposes of this SLA.*

**2.1 "Service Availability"** means, for any calendar month, the percentage calculated as:

> `Service Availability = (Total Minutes in the Month − Total Excluded Minutes) ÷ (Total Minutes in the Month) × 100%`

where "Total Minutes in the Month" is the actual minutes in that calendar month and "Total Excluded Minutes" is total Downtime minus Excluded Downtime for that month. Rounded to two decimal places.

**2.2 "Monthly Uptime Percentage"** is an alias of Service Availability.

**2.3 "Downtime"** means a period during which the in-scope Service is Unavailable, measured in whole minutes from the first to the last minute of unavailability. Periods shorter than the Minimum Downtime Increment in Section 4 are not counted.

**2.4 "Unavailable"** means, for a given in-scope Service, that the Service satisfies the unavailability test stated for that Service in Section 4. The default test is: more than five percent (5%) of well-formed requests from any Customer account return server-side errors (HTTP 5xx or equivalent) sustained over a five-minute interval, OR no successful API call is recorded from any Customer account in a five-minute interval where Vendor's monitoring confirms the absence is server-side.

**2.5 "Excluded Downtime"** means time excluded from the Service Availability calculation per Section 5.

**2.6 "Service Credit"** means a credit calculated per Annex B, capped per Section 7, applied per Section 9.

**2.7 "P1," "P2," "P3," "P4"** mean the severity classifications in Section 6 and Annex A.

**2.8 "Scheduled Maintenance"** and **2.9 "Emergency Maintenance"** have the meanings in Section 12.

**2.10 "RTO"** means Recovery Time Objective: the maximum target elapsed time, measured from disaster declaration, within which Vendor commits to restore the Service to a usable state (Section 11).

**2.11 "RPO"** means Recovery Point Objective: the maximum target period of data loss measured backward from disaster declaration (Section 11).

**2.12 "Status Page"** means Vendor's public service-status page at {{Status Page URL}}, including incident-history archive and any machine-readable feed.

**2.13 "In-Scope Service(s)"** means the Service(s) covered by this SLA per Section 3.

**2.14 "Order Form"** means the ordering document under the Master Agreement that subscribes Customer to the Service.

**2.15 "Master Agreement"** means the master subscription contract between the Parties into which this SLA is incorporated.

**2.16 "Acceptable Use Policy"** means Vendor's then-current AUP referenced by the Master Agreement.

**2.17 "Affected Service"** means the In-Scope Service for which a Service Credit is being calculated.

**2.18 "Monthly Fees"** means the recurring fees paid or accrued by Customer for the Affected Service for the calendar month of the SLA miss, prorated for billing periods longer than one month.

---

## 3. Scope of services covered

*Plain-language: This SLA applies to the production environment of the Service. Sandboxes, betas, free tiers, mobile clients, and Customer-controlled systems are outside scope unless an Order Form says otherwise.*

**3.1 In-Scope Services.** This SLA applies to the production environment of {{Service Name}} as identified on the Order Form, accessed at {{Service URL}}, and to any additional Service expressly listed as in-scope on an Order Form.

**3.2 Out-of-scope by default.** Unless expressly designated as in-scope on an executed Order Form, the following are not covered, and any unavailability does not count as Downtime:

- (a) Sandbox, staging, development, preview, and other non-production environments;
- (b) Trial subscriptions, pilots, evaluations, and beta or early-access features (however labelled);
- (c) Free-tier and no-cost subscriptions;
- (d) Integrations with, or features dependent on, third-party services not operated by Vendor;
- (e) Customer-controlled infrastructure, including networks, devices, identity providers, VPN, and proxies;
- (f) Mobile applications and SDKs running on Customer-controlled devices, where responsiveness depends on client-side conditions;
- (g) On-premises, customer-managed, or self-hosted components;
- (h) Professional services, training, and one-time engagements; and
- (i) Any feature excluded from the SLA in the Documentation as of the Order Form date.

**3.3 Per-Service measurement.** Where multiple In-Scope Services are designated, Service Availability and Service Credits are calculated separately for each. A miss on one Service does not entitle Customer to a credit on another.

**3.4 Tier-specific commitments.** Order Form tier values (for example, a Premium or Enterprise tier with elevated targets) override the defaults in this SLA while the tier is in effect.

---

## 4. Service Availability commitment

*Plain-language: Vendor commits to a monthly uptime percentage. If Vendor misses, Customer is entitled to Service Credits per Annex B. The commitment level depends on the bargain struck in the Order Form; this Section sets the menu.*

**4.1 Commitment.** Vendor shall provide Service Availability of at least {{Uptime Tier}} per calendar month, measured per the methodology described in Section 4.4.

**4.2 Dual-perspective on uptime tier.**

**Customer-favorable:** Default uptime tier is 99.95% per calendar month, with a 99.99% Premium option Customer may elect. The contractual tier is a floor, not a goal; sustained operation above the floor is expected.

**Vendor-favorable:** Default uptime tier is 99.5% per calendar month. Higher tiers require an express Order Form provision and may carry additional fees. Aspirational internal targets do not bind Vendor.

**Market-standard compromise (recommended default):** Default uptime tier is 99.9% per calendar month, with a 99.95% Premium tier available on the Order Form for production-critical Services.

**4.3 Downtime budget by tier.** For convenience, allowable Downtime per 30-day month at common tiers:

| Uptime tier | Allowable Downtime per 30-day month |
|------------:|------------------------------------:|
| 99.5% | ~3h 36m (216 min) |
| 99.9% | ~43m 12s (43.2 min) |
| 99.95% | ~21m 36s (21.6 min) |
| 99.99% | ~4m 19s (4.32 min) |

Illustrative; the operative calculation in Section 2.1 uses actual minutes in the relevant month.

**4.4 Measurement methodology.** Service Availability is measured per {{Uptime Measurement Method}}. The default methodology is one-minute synthetic monitoring from at least three external geographic regions, supplemented by Vendor's internal request-success telemetry, applying the unavailability test in Section 2.4 unless the Documentation publishes an alternative test for a specific Service. The Minimum Downtime Increment is one (1) minute.

**4.5 Service-specific unavailability tests.** For Services with unique behaviour (for example, asynchronous batch endpoints), the Parties may agree a tailored unavailability test on the Order Form or in the Documentation. Otherwise Section 2.4 controls.

**4.6 Single source of truth.** The Status Page incident log, supplemented by Vendor's monitoring records, is the canonical source of Service Availability data. Customer may submit corrective evidence per Section 8.

---

## 5. Excluded Downtime

*Plain-language: Several categories of unavailability do not count against Service Availability. The list below is the market-standard scope; see the dual-perspective subsection for narrower and broader variants.*

**5.1 Excluded categories.** None of the following count as Downtime; time spent in these categories is Excluded Downtime:

- (a) **Scheduled Maintenance** per Section 12.1, including its notice and window requirements;
- (b) **Emergency Maintenance** per Section 12.2, including its good-faith standard;
- (c) **Force majeure events** meeting the Master Agreement's force majeure definition (natural disasters, war, civil unrest, government action, pandemic, labour action beyond Vendor's reasonable control);
- (d) Failures of the public Internet, public DNS, public certificate authorities, or third-party networks outside Vendor's perimeter and reasonable control, including upstream-carrier outages;
- (e) Customer misuse, misconfiguration, or unauthorized integrations, including Customer-side rate-limit exhaustion, misissued credentials, and use violating the Documentation or AUP;
- (f) Beta, preview, trial, and experimental features or Services;
- (g) Service degradation not satisfying the "Unavailable" test (Section 2.4), including sub-threshold latency or partial-feature impairments;
- (h) Customer's failure to follow the Documentation, including failure to apply Vendor-issued SDK updates or required migrations within stated windows;
- (i) Suspension for non-payment, AUP violation, or permitted security action;
- (j) Network paths outside Vendor's perimeter, including last-mile, Customer egress, proxies, and corporate VPN concentrators; and
- (k) Time during which Customer has refused, blocked, or failed to apply a Vendor patch, hotfix, or required configuration change identified in writing as necessary to maintain Service Availability.

**5.2 Optional exclusion — DDoS.** **OPTIONAL — only if disputed.** Distributed denial-of-service attacks against the Service or its upstream providers, to the extent the attack volume materially exceeds the mitigation thresholds published by Vendor's then-current DDoS mitigation provider, and only while Vendor is acting reasonably to mitigate. Retain only where mitigation posture is genuinely strained; otherwise DDoS unavailability counts as Downtime.

**5.3 Dual-perspective on excluded-downtime scope.**

**Customer-favorable:** Narrows 5.1(a), (b), (d), and (i): (a) requires the full Maintenance Notice Window of advance notice; (b) requires Vendor to demonstrate the threat was genuine and not reasonably preventable; (d) excludes failures of third-party networks within Vendor's chosen architecture (cloud provider, CDN, identity provider) that Vendor knew or should have known were single points of failure; (i) excludes suspensions later determined to have been wrongful. Section 5.2 (DDoS) is omitted in full.

**Vendor-favorable:** All of 5.1(a)–(k) and 5.2 apply as drafted, plus (l) time during which Vendor has notified Customer of a known issue and a workaround, and (m) time during which Customer's monthly usage exceeds the highest committed quota by more than ten percent (10%) and the unavailability is causally linked to the overage.

**Market-standard compromise (recommended default):** Section 5.1 as drafted, with Section 5.2 retained only where the underlying DDoS exposure is real and disclosed in the Order Form. No additions.

**5.4 Burden.** Vendor bears the burden of demonstrating that a period of unavailability falls within an Excluded Downtime category. Status Page entries, monitoring records, and incident-response timelines are sufficient absent contrary proof.

---

## 6. Support response & resolution targets

*Plain-language: Customer raises support issues at one of four severity levels. Vendor commits to a response time (first human acknowledgment) and a resolution / workaround time (restoration or documented bypass) for each level. Targets and details are in Annex A.*

**6.1 Severity definitions.**

- **P1 (Critical):** The Service is Unavailable for all users; data loss is imminent or occurring; or a security incident with active exploitation is in progress.
- **P2 (High):** A major feature is unavailable; significant performance degradation is affecting a substantial subset of users or workflows; or a security incident has been detected without active exploitation.
- **P3 (Medium):** A non-critical feature is degraded or unavailable; a workaround is available; or the issue affects a small subset of users.
- **P4 (Low):** Cosmetic issues; documentation questions; feature requests; and other matters with no operational impact.

**6.2 Response and resolution.** "Response" means the first substantive human acknowledgment by a Vendor support engineer; auto-replies do not qualify. "Resolution" means restoration of the Affected Service to the committed tier or a documented workaround that restores the impacted workflow. Targets per Annex A.

**6.3 Dual-perspective on response and resolution targets.**

**Customer-favorable:** P1 — 15 min response / 4 h resolution; P2 — 30 min / 6 h; P3 — 4 business hours / 3 business days; P4 — 1 business day / best effort.

**Vendor-favorable:** P1 — 1 h / 24 h; P2 — 4 h / 3 business days; P3 — 2 business days / 10 business days; P4 — 5 business days / best effort.

**Market-standard compromise (recommended default):** P1 — 30 min / 8 h; P2 — 1 h / 8 h workaround; P3 — 4 business hours / 5 business days; P4 — 1 business day / best effort.

These values populate {{P1 Response Target}}, {{P1 Resolution Target}}, {{P2 Response Target}}, {{P3 Response Target}}, and {{P4 Response Target}} in Annex A.

**6.4 Support hours.** Support is staffed per {{Support Hours}}. Default coverage is 24×7 for P1 and P2, and Vendor's published business hours (typically 09:00–17:00 Monday–Friday in Vendor's primary support region, excluding Vendor holidays) for P3 and P4.

**6.5 Support channels.** Customer shall raise tickets via {{Support Channels}}. Default channels are a designated ticketing system or portal, an email alias for new tickets, and a paging endpoint (telephone or pager) for genuine P1 incidents. Other channels are not subject to these targets.

**6.6 Severity classification.** Customer proposes the initial severity. Vendor may reclassify in writing on receipt, acting reasonably and with a brief explanation. Disagreements are resolved in favour of the higher proposed severity until the facts are clarified.

**6.7 Customer obligations.** Targets are conditional on Customer providing the information needed to investigate: symptom, time of first impact, affected accounts or environments, reproduction steps where available, and any prior related ticket numbers. Targets pause while Customer is responding to a Vendor request for specified further information.

---

## 7. Service Credits

*Plain-language: When Vendor misses the monthly uptime tier, Customer is entitled to a Service Credit calculated as a percentage of the Affected Service's Monthly Fees. Credits are capped, do not roll forward indefinitely, and are not paid in cash.*

**7.1 Calculation.** Service Credits are calculated per Annex B as a percentage of Monthly Fees for the Affected Service for the calendar month of the miss. The percentage scales with the size of the miss. Calculation is performed separately for each Affected Service.

**7.2 Dual-perspective on credit cap.**

**Customer-favorable:** Credits are capped at 100% of Monthly Fees for the Affected Service for the affected month. Where the cap is reached and Service Availability remains below tier into the next month, Customer's exclusive remedy expands to include the termination right in Section 14.

**Vendor-favorable:** Credits are capped at 10% of Monthly Fees for the Affected Service for the affected month, regardless of miss size or duration.

**Market-standard compromise (recommended default):** Credits are capped at {{Credit Cap Percent}} of Monthly Fees for the Affected Service for the affected month (default 30%).

**7.3 Per-month, per-service.** Credits accrue per calendar month per Affected Service. Multiple incidents in a single month aggregate into one monthly miss; Customer is not entitled to separate credits for separate incidents that together produce one monthly Service Availability number.

**7.4 Carryforward.** Validated credits exceeding the next invoice carry forward for up to {{Credit Carryforward Months}} (default six (6)) months. Unused credits expire after that, except on Customer's non-renewal or termination per Section 14, where they are paid out per Section 9.4.

**7.5 No cash; no offset.** Credits are not refundable in cash, exchangeable for other consideration, or creditable against amounts owed under any agreement other than the Master Agreement and its Order Forms.

**7.6 Credits cannot exceed amounts paid.** A Service Credit cannot exceed the Monthly Fees paid for the Affected Service for the relevant month. The credit base is actual fees paid or accrued, not list price.

---

## 8. Credit request procedure

*Plain-language: Customer claims a credit by submitting a written request within sixty days of the affected month, with specified evidence. Vendor validates and responds within thirty days.*

**8.1 Window.** Customer shall submit a credit request within {{Credit Window Days}} (default sixty (60) days) after the end of the calendar month of the SLA miss. Late requests are waived for that month except where Customer demonstrates Vendor materially concealed the underlying facts.

**8.2 Required contents.** A credit request shall include:

- (a) The calendar month claimed;
- (b) Total Downtime asserted in minutes, with start and end timestamps in UTC;
- (c) Severity classifications of the underlying incidents where applicable;
- (d) Vendor support-ticket numbers where Customer raised tickets;
- (e) Status Page references, monitoring records, error logs, or other evidence; and
- (f) The Customer accounts and environments affected.

**8.3 Submission channel.** Requests shall be submitted via the support-ticket channel designated for billing matters or, if none, via the Customer-success contact in the Order Form. Requests raised through other channels are not deemed received until logged in the designated channel.

**8.4 Validation.** Vendor shall validate the request against (i) the Status Page incident log, (ii) Vendor's monitoring records, (iii) Vendor's support-ticket records, and (iv) the Excluded Downtime categories in Section 5. Where records disagree, Vendor shall describe the discrepancy and propose a resolution.

**8.5 Response window.** Vendor shall respond in writing within thirty (30) days of receipt, either (i) confirming the credit amount and the invoice it will apply to, (ii) rejecting with reasons, or (iii) requesting specified further information, in which case the response window extends by the time Customer takes to provide it.

**8.6 Disputes.** Where Customer disputes Vendor's response, the Parties shall attempt good-faith resolution between commercial contacts within fifteen (15) business days. Unresolved disputes are subject to the Master Agreement's dispute-resolution clause.

---

## 9. Credit issuance & exclusivity as remedy

*Plain-language: Validated credits appear on the next invoice. Service Credits are the only remedy for ordinary SLA misses, except for the termination right in Section 14. Vendor will not pay credits in cash except on Customer's exit when the credits exceed remaining commitments.*

**9.1 Form of credit.** Validated credits are issued as a percentage applied to Customer's next invoice for the Affected Service. For annual-in-advance billing without a near-term invoice, the credit applies at the next renewal or, on Customer's request, is prorated against the current annual fee on the billing portal.

**9.2 Exclusive remedy.** Subject to Sections 9.4 and 14, Service Credits are Customer's sole and exclusive financial remedy for Vendor's failure to meet any commitment in this SLA. Customer waives any other damages claim for SLA misses to the extent permitted under the Master Agreement's governing law, except where the SLA miss also constitutes a breach for which the Master Agreement preserves a separate remedy.

**9.3 No waiver of other rights.** Section 9.2 does not limit Customer's rights under the Master Agreement for matters that are not SLA misses, including confidentiality breaches, security incidents under the Data Processing Agreement, intellectual-property indemnities, and AUP breaches.

**9.4 Cash refund on Customer exit.** Where Customer terminates the Master Agreement for cause or terminates this SLA for material breach under Section 14, Vendor shall pay out unused validated credits in cash within thirty (30) days of the effective termination date, capped at the lesser of (i) the unused-credit balance and (ii) remaining pre-paid fees for the Affected Service.

**9.5 Tax.** Service Credits are deemed price reductions for tax purposes. Where local law characterizes a credit differently, the Parties shall cooperate on appropriate invoice annotations.

---

## 10. Performance reporting & status page

*Plain-language: Vendor publishes a real-time Status Page and delivers a monthly SLA report. Customer can request raw monitoring data on reasonable notice.*

**10.1 Status Page.** Vendor shall maintain a public Status Page at {{Status Page URL}}, updated in approximately real time during incidents and maintenance. The Status Page shall distinguish operational, degraded, and outage states for each major Service component; provide an incident-history archive going back at least six (6) months; and offer a machine-readable feed (RSS, JSON, or equivalent).

**10.2 Monthly report.** Vendor shall deliver a monthly SLA report substantially in the form of Annex C, on the cadence {{Reporting Cadence}} (default monthly), via email or the Customer dashboard, within ten (10) business days after the end of each calendar month.

**10.3 Report contents.** The monthly report shall include the items in Annex C.

**10.4 Raw monitoring data on request.** On reasonable written notice, Customer may request the underlying monitoring data for a specified month. Default disclosure is the aggregated time-series data Vendor uses to compute Service Availability. Where Customer demonstrates a legitimate audit, regulatory, or incident-investigation need, Vendor shall provide granular incident-level data subject to the Master Agreement's confidentiality terms.

**10.5 Notification of incidents.** Vendor shall publish a Status Page entry for any P1 or P2 incident within fifteen (15) minutes of detection, update at intervals of no more than sixty (60) minutes for the duration, and post a written incident summary within five (5) business days of resolution with a preliminary root-cause analysis and remediation plan.

**10.6 Annual review.** Where the Master Agreement term exceeds one year, the Parties shall meet at least annually to review SLA performance, support trends, and proposed adjustments to in-scope Services or tiers.

---

## 11. Disaster recovery & business continuity

*Plain-language: Vendor commits to recovery objectives, periodic disaster-recovery testing, and minimum backup retention. The recovery objectives differ by perspective.*

**11.1 Business continuity program.** Vendor shall maintain a documented business-continuity and disaster-recovery program covering the Service, reviewed at least annually, addressing personnel, facilities, communications, and technical recovery.

**11.2 Dual-perspective on RTO and RPO.**

**Customer-favorable:** RTO is one (1) hour and RPO is fifteen (15) minutes for production Services. RTO is measured from disaster declaration; RPO is measured backward from disaster declaration to the most recent recoverable data point.

**Vendor-favorable:** RTO is twenty-four (24) hours and RPO is twenty-four (24) hours. RTO and RPO are operational targets, not warranties; missing them is not, by itself, an SLA breach for credit purposes.

**Market-standard compromise (recommended default):** RTO is {{RTO}} (default four (4) hours for production tier) and RPO is {{RPO}} (default one (1) hour for production tier). Premium tiers may carry shorter RTO and RPO on the Order Form.

**11.3 DR testing.** Vendor shall conduct full or partial DR exercises at least {{DR Test Cadence}} (default annually), document the results, and address material findings within a reasonable period.

**11.4 DR test results.** On reasonable written notice and subject to confidentiality, Vendor shall make a redacted summary of the most recent DR test results available to Customer, including the scenario, measured RTO and RPO achieved, and open remediation items.

**11.5 Backup retention.** Vendor shall retain encrypted backups of Customer Data for at least {{Backup Retention}} (default thirty (30) days), with access strictly controlled and key custody segregated from production credentials.

**11.6 Geographic redundancy.** {{Geo Redundancy}}. The default is that production data is replicated, in near real time, across at least two availability zones within the same region. Multi-region replication is available on the Order Form at additional cost.

**11.7 No warranty of zero loss.** RTO and RPO are commitments to design, exercise, and operate to those objectives. Achievement is not guaranteed for events exceeding the program's design assumptions.

---

## 12. Scheduled & emergency maintenance

*Plain-language: Maintenance is excluded from Downtime if it follows the rules below: notice, defined window, and good-faith standards.*

**12.1 Scheduled Maintenance.** Vendor may take the Service offline or into a degraded state during the maintenance window {{Maintenance Window}} (default Saturdays 02:00–06:00 UTC), provided Vendor publishes the maintenance to the Status Page and to the Customer-facing notice channel at least {{Maintenance Notice Window}} (default seven (7) days) in advance. Scheduled Maintenance within these constraints does not count as Downtime.

**12.2 Emergency Maintenance.** Vendor may carry out Emergency Maintenance outside the scheduled window in response to a credible threat to security, integrity, or availability — including critical vulnerability patching, urgent capacity intervention, and incident response. Vendor shall provide {{Emergency Notice Window}} (default two (2) hours' notice where feasible) via the Status Page and the Customer-facing notice channel; where prior notice is infeasible, Vendor may proceed and shall publish a contemporaneous notice and a post-incident summary. Emergency Maintenance carried out in good faith does not count as Downtime.

**12.3 Limits.** Scheduled Maintenance shall not exceed eight (8) hours per calendar month or twenty (20) hours per calendar quarter in aggregate, except where Customer expressly agrees otherwise on the Order Form or for a specific upgrade.

**12.4 Customer-disruptive changes.** Where maintenance requires Customer action (re-authentication, schema migration, SDK upgrade), Vendor shall describe the action in the notice and, where reasonably possible, offer a deferred or staggered upgrade path.

**12.5 No masking of Downtime.** Maintenance initiated to address an in-progress unscheduled outage is Emergency Maintenance only to the extent of genuine emergency-response activity; the precipitating unavailability remains Downtime.

---

## 13. Service degradation vs. outage

*Plain-language: Not every problem is an outage. Outages trigger credits; sub-threshold degradation does not, but Vendor still owes root-cause analysis and remediation when degradation is sustained.*

**13.1 Outage.** An "Outage" is a period of Downtime per Section 2.3. Outages reduce Service Availability and may trigger Service Credits per Annex B.

**13.2 Degradation.** "Degradation" is a period during which the Service is operational but performance is materially worse than Vendor's published baseline (latency above a stated threshold, increased error rate below the unavailability threshold, partial-feature impairment). Degradation does not count as Downtime unless it satisfies the Section 2.4 unavailability test.

**13.3 Root-cause analysis for sustained degradation.** Where Degradation persists more than {{Degradation Threshold Hours}} (default four (4) hours) on an In-Scope Service, Vendor shall, regardless of any SLA credit threshold: (a) open a Status Page incident; (b) investigate the root cause; (c) deliver a written root-cause analysis to Customer within ten (10) business days of resolution; and (d) track remediation to closure.

**13.4 Repeated degradation.** Where the same root cause produces Degradation in three (3) or more months in any rolling six (6) months, Customer may, on written notice, require Vendor to deliver a remediation plan with target dates and quarterly progress updates until closure.

**13.5 No double recovery.** A period counted as Downtime cannot also generate a separate degradation-track remedy; Section 13 remedies are operational, not financial.

---

## 14. Material SLA breach & termination right

*Plain-language: Sustained or repeated SLA misses that drop the Service below the committed tier across multiple months entitle Customer to terminate the affected Order Form (or the Master Agreement, where the Service is the only Service) and recover a pro-rata refund of unused pre-paid fees. The threshold differs by perspective.*

**14.1 Dual-perspective on termination threshold.**

**Customer-favorable:** Customer may terminate the affected Order Form for material SLA breach on written notice where Service Availability for the Affected Service falls below the committed tier in any two (2) consecutive calendar months.

**Vendor-favorable:** Customer may terminate the affected Order Form for material SLA breach on written notice where Service Availability falls below the committed tier in six (6) consecutive calendar months, provided Customer has notified Vendor in writing of the intention to exercise the right after the third consecutive month and given Vendor a reasonable opportunity to cure.

**Market-standard compromise (recommended default):** Customer may terminate the affected Order Form for material SLA breach on written notice where Service Availability falls below the committed tier in {{Termination Threshold}} (default three (3) consecutive calendar months OR any three (3) of any rolling six (6) calendar months).

**14.2 Notice and waiver.** Termination notice shall be delivered within thirty (30) days after the close of the qualifying month. A failure to deliver notice within that window waives the right for that qualifying period only (not later qualifying periods).

**14.3 Pro-rata refund.** On termination under this Section 14, Vendor shall refund, within thirty (30) days of the effective termination date, a pro-rata portion of the Affected Service's pre-paid fees attributable to the unused remainder of the term, reduced by Service Credits already issued for the same period.

**14.4 Scope of termination.** Termination under this Section 14 is scoped to the affected Order Form by default. Where the affected Order Form is the only Order Form, termination coincides with termination of the Master Agreement to the extent then exclusively supporting that Order Form.

**14.5 No prejudice to accrued credits.** Termination does not extinguish accrued unused credits; those are paid out per Section 9.4.

**14.6 Carve-out.** The termination right and pro-rata refund in this Section 14 are an express exception to the exclusive-remedy clause in Section 9.2.

---

## 15. Changes to this SLA

*Plain-language: Vendor may update this SLA on notice. Material decreases — lower tier, narrower scope, lower cap — require Customer's affirmative consent or a no-penalty exit window.*

**15.1 General changes.** Vendor may modify this SLA on at least thirty (30) days' prior written notice via the Status Page or Customer-facing notice channel and, where the Master Agreement designates a customer-success contact, also to that contact. Clarifying changes, improvements to Customer, and methodology changes that do not reduce substantive commitments take effect at the end of the notice period.

**15.2 Material decreases.** Where a proposed change would (i) reduce the committed Service Availability tier, (ii) narrow the in-scope Services, (iii) reduce Service Credit percentages or cap, (iv) extend Excluded Downtime adverse to Customer, (v) lengthen response or resolution targets, (vi) lengthen RTO or RPO, or (vii) tighten the credit-request window or evidence requirements, Vendor shall not impose the change unilaterally. Vendor shall instead either:

- (a) Obtain Customer's affirmative written consent (electronic acceptance acceptable); or
- (b) Grant Customer a right to terminate the affected Order Form without penalty, with a pro-rata refund of unused pre-paid fees, by written notice within thirty (30) days after the change takes effect.

**15.3 Order-Form-specific commitments.** Where the Order Form sets a specific value for a merge field (for example, a fixed uptime tier or credit cap), that value cannot be changed unilaterally during the term of that Order Form; Section 15.2 applies.

**15.4 No retroactive change.** Changes take effect prospectively. Availability, Credits, and remedies for any month already begun are determined under the SLA in force at the start of that month.

**15.5 Versioning.** Vendor shall maintain a public version history identifying, for each version, the effective date and a brief summary of substantive changes, retained at least six (6) years.

---

## 16. Survival & order of precedence

*Plain-language: This SLA controls availability and support topics; the Master Agreement controls everything else. Pending credits, accrued claims, and audit/reporting rights for the period survive termination.*

**16.1 Order of precedence.** Where this SLA conflicts with another contract document, the order of precedence, from highest to lowest, is:

- (a) the Order Form, only as to terms it expressly designates as overriding this SLA;
- (b) this SLA;
- (c) the Master Agreement; and
- (d) the Acceptable Use Policy.

This order of precedence is limited to the subject matter of this SLA: availability, support targets, Service Credits, maintenance, status reporting, disaster recovery, and related definitions. Other topics are governed by the Master Agreement.

**16.2 Survival.** The following obligations survive termination or expiration: (i) Customer's right to claim Service Credits accrued during the term, exercisable for sixty (60) days after the effective termination date; (ii) Vendor's obligation to deliver the final monthly SLA report; (iii) any obligation to pay out unused validated credits per Section 9.4; (iv) the dispute-resolution clauses incorporated from the Master Agreement; (v) confidentiality and data-handling obligations applicable to monitoring data delivered under Section 10.4; and (vi) any provision that by its nature is intended to survive.

**16.3 Audit and reporting rights.** Customer's rights under Sections 10.4 and 11.4 survive as needed to investigate closing months, not to exceed twelve (12) months after termination.

**16.4 No assignment by reference.** This SLA cannot be assigned independently of the Master Agreement; a permitted assignment of the Master Agreement carries this SLA with it.

---

## Annex A — Severity matrix

Merge fields {{P1 Response Target}}, {{P1 Resolution Target}}, {{P2 Response Target}}, {{P3 Response Target}}, and {{P4 Response Target}} are populated from the perspective table in Section 6.3.

| Severity | Definition | Response Target | Resolution / Workaround | Support Hours |
|----------|-----------|-----------------|-------------------------|---------------|
| P1 (Critical) | Service Unavailable for all users; data loss imminent or occurring; security incident with active exploitation | {{P1 Response Target}} | {{P1 Resolution Target}} | 24×7 |
| P2 (High) | Major feature unavailable; significant performance degradation affecting a substantial subset of users; security incident without active exploitation | {{P2 Response Target}} | 8 hours (workaround) | 24×7 |
| P3 (Medium) | Non-critical feature degraded; workaround available; small user subset affected | {{P3 Response Target}} | 5 business days | Business hours |
| P4 (Low) | Cosmetic; documentation question; feature request; no operational impact | {{P4 Response Target}} | Best effort | Business hours |

Notes:

- Response is the first substantive human acknowledgment by a Vendor support engineer; auto-replies do not qualify.
- Resolution / workaround means restoration to the committed tier or a documented bypass for the impacted workflow.
- Targets pause while Customer is responding to a Vendor request for specified information.

---

## Annex B — Service Credit calculation table

Default credit schedule for a committed tier of 99.9%. For other tiers, Vendor will provide an equivalent table with breakpoints scaled proportionally.

| Monthly Uptime Percentage for the Affected Service | Service Credit (% of Monthly Fees for the Affected Service) |
|-------------------------------------------------:|------------------------------------------------------------:|
| ≥ 99.9% (committed tier met) | 0% |
| < 99.9% but ≥ 99.0% | 10% |
| < 99.0% but ≥ 95.0% | 25% |
| < 95.0% | 50%, subject to the {{Credit Cap Percent}} cap (default 30%) |

Application notes:

- Each row is a step function; no partial credits between breakpoints.
- The Section 7.2 cap controls the maximum credit per month even where the calculated percentage exceeds the cap.
- For non-default tiers (for example, 99.95% Premium), the schedule shifts: "committed tier met" begins at the new tier, with breakpoints recalibrated.
- The Monthly Fees base is actual fees paid or accrued (Section 2.18), not list price.

---

## Annex C — Sample monthly SLA report format

The monthly report delivered under Section 10.2 shall include:

1. **Reporting period** — calendar month and year, UTC start and end timestamps.
2. **Total minutes in the month** — actual minutes.
3. **Total Downtime** — minutes, with per-incident breakdown (start, end, duration, severity, one-line root-cause label).
4. **Total Excluded Downtime** — minutes, broken down by Section 5 category (Scheduled Maintenance, Emergency Maintenance, Force Majeure, Internet/DNS, Customer-side, Beta, Sub-threshold Degradation, Documentation non-compliance, Suspension, External network paths, Customer non-application of patches; and DDoS if elected).
5. **Net Downtime** — minutes after subtracting Excluded Downtime.
6. **Monthly Uptime Percentage** — calculated per Section 2.1, rounded to two decimals.
7. **Credit calculation** — Annex B row applied, percentage before cap, cap applied, resulting credit amount in Customer's billing currency.
8. **Top 5 incidents** — for each: ticket link or Status Page incident ID, severity, duration, services affected, brief root-cause summary.
9. **Maintenance windows used** — Scheduled and Emergency Maintenance events with duration and description.
10. **Year-to-date trend** — narrative of rolling twelve-month uptime, month-by-month figures, flag for any month below the committed tier.
11. **Open remediation items** — root-cause analyses and remediation plans with target dates for Section 13 items.

The report is emailed to Customer's designated SLA-report contact and made available in the Customer dashboard for at least twelve (12) months after publication.

---

## Merge fields used

The following Mustache-style merge fields are used in this template. A value should be supplied for each field at the time the SLA is finalized.

- {{Vendor Legal Name}}
- {{Vendor Short Name}}
- {{Customer Legal Name}}
- {{Customer Short Name}}
- {{Service Name}}
- {{Service URL}}
- {{Status Page URL}}
- {{Effective Date}}
- {{Last Updated Date}}
- {{Uptime Tier}}
- {{Uptime Measurement Method}}
- {{Maintenance Window}}
- {{Maintenance Notice Window}}
- {{Emergency Notice Window}}
- {{Credit Cap Percent}}
- {{Credit Window Days}}
- {{Credit Carryforward Months}}
- {{Reporting Cadence}}
- {{P1 Response Target}}
- {{P1 Resolution Target}}
- {{P2 Response Target}}
- {{P3 Response Target}}
- {{P4 Response Target}}
- {{Support Hours}}
- {{Support Channels}}
- {{RTO}}
- {{RPO}}
- {{DR Test Cadence}}
- {{Backup Retention}}
- {{Geo Redundancy}}
- {{Termination Threshold}}
- {{Degradation Threshold Hours}}

---

## Authoritative references

Clean-room drafting from the following permissively-licensed sources. No text was copied verbatim; structure, headings, and operative concepts served as drafting guides.

- **Bonterms SLA** — `[CC-BY-4.0]`. Primary structural baseline for the dual-perspective availability and credit framework.
- **Common Paper Cloud Service Agreement v2.1, SLA exhibit** — `[CC-BY-4.0]`. Reference for the SLA-as-exhibit pattern, credit-window mechanics, and credit-as-exclusive-remedy.
- **GitHub `site-policy`** — `[CC0]`. Clause-heading and plain-language summary conventions.
- **Mozilla legal templates** — `[MPL-2.0]`. Regional-overlay pattern and change-control mechanics (Section 15).
- **Linux Foundation / Apache project SLAs** — `[Apache-2.0]`. Operational-reporting patterns (Section 10) and DR program structure (Section 11).
- **ICO, NCSC, ENISA, and similar government cyber/incident guidance** — Open Government Licence / public domain. Incident-notification and degradation-tracking patterns.

**Blocked baselines (not consulted):** AWS SLAs, Microsoft Online Service Level Agreement, Google Workspace SLA, Salesforce SLA, Atlassian SLAs, Stripe SLAs, Cloudflare SLAs, OneDrive SLAs, and any other proprietary or unspecified-license cloud/SaaS SLA template.

---

## Not legal advice

This SLA template is a drafting starting point provided for general informational and operational purposes. It is not legal advice, and using it does not create a lawyer-client relationship with the Legalcode project, Fordæmi ehf., or any contributor. Service-level commitments are commercially significant: the appropriate uptime tier, credit cap, response and resolution targets, RTO and RPO, termination threshold, and excluded-downtime scope all depend on Vendor's actual operational capability, Customer's regulatory and risk profile, and the Master Agreement's governing law. Before executing an SLA based on this template, both Parties should engage qualified counsel and Vendor's engineering and operations leadership to confirm the commitments are achievable and enforceable.
