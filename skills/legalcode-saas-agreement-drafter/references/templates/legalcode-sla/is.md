---
title: Service Level Agreement — Iceland
jurisdictions: [is]
statutes: [Lög-90/2018-Persónuverndarlög, Lög-78/2019-Netöryggislög, Lög-70/2022-Fjarskiptalög, NIS2-via-EEA, DORA-via-EEA, GDPR-via-EEA]
supervisory_authority: Persónuvernd / FME / CERT-IS
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

> **Bilingual usage.** When the Parties publish a parallel Icelandic-language version of this SLA (filed alongside as `is-isl.md`), the **Icelandic-language text controls** in any dispute, regulatory submission, or court proceeding before an Icelandic court or supervisory authority. This English text is operative only as the Parties' agreed working language. References to Icelandic statutes (lög nr.) cite althingi.is consolidated text in force on `{{Effective Date}}`. `[VERIFY]` flags items a qualified Icelandic-admitted lawyer should confirm before execution.

---

## 1. Plain-language summary

This Service Level Agreement (þjónustustigssamningur) records what the Vendor (Þjónustusala) commits to keep the Service (Þjónusta) running for, how fast Customer (Viðskiptamaður) tickets are answered, and what credit is owed when targets are missed. It also coordinates breach- and incident-notification timelines across Iceland's principal supervisors: Persónuvernd for personal-data breaches under **Lög nr. 90/2018**, CERT-IS and the relevant sectoral authority under **Lög nr. 78/2019** (as updated by EEA-incorporated NIS2), Fjármálaeftirlitið (FME) under EEA-incorporated DORA, and PFS under **Lög nr. 70/2022**. The document attaches as an Exhibit of the parent Cloud Service Agreement (`legalcode-csa` IS variant). Plain-English summaries open every section; Icelandic statutory terms appear once on first use; merge fields use Mustache `{{Field Name}}` placeholders.

---

## 2. Definitions

This section defines recurring vocabulary. Undefined capitalised terms take their meaning from the parent Cloud Service Agreement or **Lög nr. 90/2018 um persónuvernd og vinnslu persónuupplýsinga** (Persónuverndarlög).

2.1 "**Service Level**" (Þjónustustig) — a measurable availability / response / resolution commitment in this SLA or the Order Form (Pöntunarform).

2.2 "**Availability**" (Aðgengi) — for any calendar month, the percentage of total Service Minutes during which the Service was reachable and substantially functional, measured per §10 excluding §5 categories.

2.3 "**Downtime**" (Niðritími) — any continuous period during which the Service is not Available.

2.4 "**Service Minutes**" — days in the calendar month × 1,440.

2.5 "**Severity**" (Forgangur) — priority level assigned per Annex A (P1 Critical through P4 Low).

2.6 "**Response Time**" / "**Resolution Time**" — elapsed time from properly-formatted ticket receipt to (respectively) the Vendor's substantive first response and delivery of a permanent fix or Workaround restoring material functionality.

2.7 "**Service Credit**" (Afsláttur) — monetary credit applied to a future invoice as the contractual remedy for a Service Level miss, calculated under Annex B and capped per §7.3.

2.8 "**Excluded Downtime**" — unavailability falling within §5; does not count against Availability.

2.9 "**Scheduled Maintenance**" / "**Emergency Maintenance**" — Vendor-initiated work announced under §12.1 with `{{Maintenance Notice Window}}` notice (Scheduled), or unscheduled work for an active or imminent threat announced under §12.2 with `{{Emergency Notice Window}}` notice where feasible.

2.10 "**Disaster Recovery / Business Continuity**" (Áfallaviðbragðsáætlun) — Vendor's documented plan for restoring the Service after major disruption, including §11 RTO `{{RTO}}` and RPO `{{RPO}}`.

2.11 "**Incident Notification**" (Atvikatilkynning) — written communication confirming a §17-threshold event and providing the §17 information.

2.12 "**Persónuvernd**" — Icelandic Data Protection Authority (GDPR Art. 51 / Lög nr. 90/2018). "**FME**" — Fjármálaeftirlitið. "**CERT-IS**" — Iceland's national computer-security incident response team (cert.is). "**PFS**" — Póst- og fjarskiptastofnun (Lög nr. 70/2022).

2.13 "**Lög nr. 90/2018**" — Persónuverndarlög. "**Lög nr. 78/2019**" — Act on the Security of Network and Information Systems of Critical Infrastructure, as amended (NIS2 EEA-transposition `[VERIFY]`). "**Lög nr. 70/2022**" — Fjarskiptalög.

2.14 "**Major ICT Incident**" — an event meeting the EEA-incorporated DORA Art. 18 materiality threshold, applicable where the Customer is FME-regulated.

---

## 3. Scope of services covered

Identifies what the SLA covers and which Vendor regulatory characterisation applies; classifications drive §11 and §17.

3.1 **Covered Services.** The Service Levels apply to `{{Service Name}}` at `{{Service URL}}`, and only to the production environment plus any non-production environment expressly listed on the Order Form. Free-tier, evaluation, and beta or early-access components are excluded unless the Order Form so states.

3.2 **NIS-Iceland class.** The Vendor's classification under **Lög nr. 78/2019 um öryggi net- og upplýsingakerfa mikilvægra innviða** (transposing the original NIS Directive, anticipated to be amended for Directive (EU) 2022/2555 (NIS2) once incorporated into the EEA Agreement `[VERIFY EEA NIS2 transposition status]`) is recorded as `{{Vendor NIS-IS Class}}`: (a) **essential entity** (mikilvægur aðili); (b) **important entity** (þýðingarmikill aðili); or (c) **N/A**. Where (a) or (b) applies, §11.5, §17.2, and §17.5 apply in full.

3.3 **DORA class.** Where the Customer is FME-supervised, the Vendor's classification under **Regulation (EU) 2022/2554 (DORA)** as EEA-incorporated `[VERIFY EEA DORA transposition status]` is recorded as `{{Vendor DORA Class}}`: (a) **ICT third-party service provider** under DORA Arts. 28–30; or (b) **N/A**. Where (a) applies, §11.9 and §17.3 apply in full and the Order Form records whether the Service supports a "critical or important function".

3.4 **Telecommunications scope.** Where the Vendor provides electronic communications services within **Lög nr. 70/2022 um fjarskipti**, the Vendor is in scope of PFS supervision and §17.4 applies.

3.5 **Scope exclusions.** The SLA does not cover: (a) Customer-side networks, devices, or configuration; (b) third-party software the Customer integrates; (c) public-internet transit; or (d) experimental / preview / beta features.

---

## 4. Service Availability commitment

This section sets the uptime commitment, default `{{Uptime Tier}}` measured monthly. Three drafting postures.

4.1 **Headline commitment.** For each calendar month during the Subscription Term, the Service shall be Available for at least `{{Uptime Tier}}` of Service Minutes, calculated under §4.4 and excluding §5 Excluded Downtime.

4.2 **Customer-favoured posture (OPTIONAL — only for regulated financial entities, public-sector bodies, or critical-infrastructure operators).** 99.95% monthly Availability, one-minute synthetic monitoring from ≥3 geographically separated probes, downtime from first failed probe.

4.3 **Vendor-favoured posture (OPTIONAL — only for early-stage or volume-discounted Services).** 99.5% monthly Availability, five-minute single-region monitoring, downtime only after two consecutive failed probes.

4.4 **Measurement.** Measured by `{{Uptime Measurement Method}}` (default synthetic monitoring at one-minute intervals, geographically distributed). On material telemetry divergence, the Parties reconcile in good faith and the Vendor produces raw monitoring data within 10 business days of a written request.

4.5 **Multi-component.** Order Form may set a separate Uptime Tier per component (API plane, UI plane, etc.).

4.6 **No DST adjustment.** Service Minutes = 1,440 per day. Iceland (Atlantic/Reykjavik, UTC+0) does not observe DST; SLA windows operate on a fixed UTC offset.

---

## 5. Excluded Downtime

This section lists categories of unavailability that do not count against Availability. Expansive exclusions hollow out a strong tier — review carefully.

5.1 Excluded Downtime: (a) Scheduled Maintenance (§12.1); (b) Emergency Maintenance (§12.2); (c) force-majeure events per the parent CSA (natural disaster, volcanic eruption, geomagnetic storm, severe weather, pandemic-response, war, civil unrest, embargo); (d) Customer-side infrastructure, networks, devices, or third-party software, including public-internet transit; (e) Customer misuse, misconfiguration, or credential-handling failure; (f) Vendor suspension exercised under the parent CSA; (g) beta / preview / experimental / early-access features excluded under §3.5(d); (h) Customer failure to meet a documented technical prerequisite within 30 days of publication; (i) DoS / malicious attack where industry-standard proportionate protections are in place; (j) outages from a Customer-directed third-party upstream; (k) Customer refusal or delay of an Update reasonably necessary for stability or security; (l) **Iceland-specific** — service interruption mandated by Persónuvernd, FME, PFS, CERT-IS, or any other Icelandic supervisory authority acting within its statutory powers, including under public-emergency provisions; and (m) **Iceland-specific** — government-ordered modification under **Lög nr. 82/2008 um almannavarnir** (Civil Protection Act) or equivalent emergency or pandemic-preparedness legislation, including any ordered by Almannavarnadeild.

5.2 **Customer-favoured posture (OPTIONAL — only if the Service supports critical functions or special-category personal data).** Strike (h), (j), and (k); require Vendor evidence that each Excluded Downtime claim was operationally unavoidable.

5.3 **Vendor-favoured posture (OPTIONAL — only for non-production scope).** Add an exclusion for Customer-initiated load-test traffic exceeding documented rate limits.

5.4 **Documentation.** The Vendor identifies each Excluded Downtime instance in the §10 monthly report and supplies substantiating telemetry within 15 business days of a request.

---

## 6. Support response & resolution targets

This section sets how fast the Vendor responds to and resolves Customer support requests, by Severity. Default support time zone is **Atlantic/Reykjavik (UTC+0)** (Iceland does not observe DST); "business hours" = 09:00–17:00 Reykjavik on weekdays excluding Icelandic statutory holidays.

6.1 **Classification.** Tickets are classified per Annex A. Reclassification disputes go to the named technical lead under §6.8.

6.2 **Response (default).** P1 `{{P1 Response Target}}` (default 15 min, 24×7); P2 `{{P2 Response Target}}` (default 1 hr, 24×7); P3 `{{P3 Response Target}}` (default 4 business hr); P4 `{{P4 Response Target}}` (default 1 business day).

6.3 **Resolution.** P1 `{{P1 Resolution Target}}` (default 4 hr — fix or Workaround); P2 1 business day; P3 5 business days; P4 next regularly scheduled release.

6.4 **Customer-favoured posture (OPTIONAL — only if 24×7 support is mandated).** P3 response 2 business hours; P3 resolution 2 business days; P4 response 4 business hours.

6.5 **Vendor-favoured posture (OPTIONAL — only where support entitlement is business-hours-only).** Targets apply only during business hours; out-of-hours tickets accrue from next business hour.

6.6 **Channels and hours.** `{{Support Channels}}` (default web ticketing and email) on `{{Support Hours}}` (default 24×7 P1 / P2; business hours P3 / P4) measured against `{{Support Time Zone}}` (default Atlantic/Reykjavik, UTC+0).

6.7 **Language.** First-line in English by default; Icelandic second-line and incident-coordination available where the Order Form so provides (reasonable additional charges unless folded into base subscription).

6.8 **Escalation.** Each Party names a primary and a backup escalation contact. Missed-target escalations are acknowledged by the named Vendor contact within 30 min during business hours / 1 hr outside.

6.9 **Holiday calendar.** "Business day" excludes Icelandic statutory holidays per **Lög nr. 32/1997 um almenna frídaga** (1 Jan; Maundy Thursday; Good Friday; Easter Monday; Sumardagurinn fyrsti; 1 May; Ascension; Whit Monday; 17 June; Frídagur verslunarmanna; 24 Dec afternoon; 25–26 Dec; 31 Dec afternoon). The Order Form may substitute an Affiliate-aligned calendar.

---

## 7. Service Credits

Financial remedy when uptime or support targets are missed: a percentage of monthly Fees, capped to protect Vendor margin while creating real incentive.

7.1 **Availability credits.** Where Availability falls below the Uptime Tier, the Customer is entitled to a Service Credit per Annex B (default 99.9% grid: ≥99.0%/<99.9% → 10%; ≥95.0%/<99.0% → 25%; <95.0% → 50%, subject to cap).

7.2 **Support credits.** Missed P1 +5%; missed P2 +2%, additive up to the Cap. Customer-favoured drafting may extend to P3.

7.3 **Cap.** Total credits per month are capped at `{{Credit Cap Percent}}` (default 30%) of that month's Fees for the affected Service.

7.4 **Customer-favoured posture (OPTIONAL — only where uptime is mission-critical).** Raise cap to 50%; add cumulative 100%-of-prior-twelve-months cap for chronic underperformance.

7.5 **Vendor-favoured posture (OPTIONAL — only for low-margin or volume-discounted plans).** Apply cap on a calendar-quarter basis; exclude support credits.

7.6 **No double recovery.** A credit for an Availability miss is not stackable with a support-target credit from the same incident; Customer is entitled to the higher.

7.7 **Currency and form.** Issued in the invoice currency (default ISK for Customers established in Iceland); non-refundable in cash unless subscription terminates with a positive balance, in which case unused credit is paid out within 30 days.

---

## 8. Credit request procedure

How the Customer claims a credit. Most disputes turn on whether the request was filed correctly and on time.

8.1 **Window.** Submitted within `{{Credit Window Days}}` (default 60 days) after the end of the affected month. Late requests forfeit unless the §10 report itself disclosed the miss — then 30 days from report publication.

8.2 **Required information.** (a) Customer entity / account ID; (b) month at issue; (c) alleged miss; (d) affected Service component; (e) Customer's good-faith credit calculation; (f) supporting telemetry.

8.3 **Review.** Vendor acknowledges within 5 business days; accepts / partial-accepts / declines within 20 business days, with substantiating telemetry on decline.

8.4 **Escalation.** Disagreements escalate per §6.8 and, failing resolution within 10 business days, to the parent CSA dispute-resolution path.

8.5 **Auto-issuance (OPTIONAL).** Vendor may auto-credit affected accounts for misses identified in its own monthly report, without a request.

---

## 9. Credit issuance & exclusivity as remedy

When credits are paid; their status as the monetary remedy for SLA misses, preserving non-waivable Customer rights under Icelandic and EEA law.

9.1 **Issuance.** Accepted credits are applied against the next-issued invoice; otherwise paid out per §7.7.

9.2 **Sole monetary remedy.** Subject to §9.3, Service Credits are the Customer's sole and exclusive monetary remedy for the Vendor's failure to meet a Service Level under this SLA.

9.3 **Preserved Customer rights — Iceland-specific.** Service Credits do not displace Customer's rights under **Lög nr. 7/1936 § 36** (ósanngirnis unconscionability) where SLA terms are challenged as unfair, nor mandatory regulatory damages under **GDPR Article 82** as transposed by **Lög nr. 90/2018** (compensation for material or non-material damage), nor the §14 termination right, nor any non-waivable Customer right under EEA-incorporated DORA for FME-regulated Customers, nor the Customer's right to seek injunctive relief for confidentiality, intellectual-property, or personal-data breaches under the parent CSA.

9.4 **Customer-favoured posture (OPTIONAL — only where Customer is critical-infrastructure or a financial entity).** Strike §9.2 and treat Credits as one available remedy alongside contract and statute.

9.5 **Vendor-favoured posture (OPTIONAL — only where this SLA stands alone).** Confirm Credits sit within, not in addition to, any aggregate liability cap in the parent CSA.

---

## 10. Performance reporting & status page

How performance is communicated: a real-time public status page and a periodic written report.

10.1 **Status page.** Public page at `{{Status Page URL}}` showing current health, ongoing incidents, and ≥90 days of incident summaries; updated ≥ every 30 min during active P1 / P2.

10.2 **Monthly report.** Vendor publishes a `{{Reporting Cadence}}` (default monthly) report by the 15th of the following month, covering: (a) measured Availability per component; (b) P1 / P2 incident summaries with duration, root cause, remediation; (c) §5 Excluded Downtime with basis; (d) support metrics (volumes; median and 95th-percentile response and resolution by severity); (e) credits already auto-issued. Annex C is the default template.

10.3 **Customer-favoured posture (OPTIONAL — only where uptime is contractually material).** Add a quarterly business review covering trend analysis, capacity planning, and committed remediation.

10.4 **Vendor-favoured posture (OPTIONAL — only for high-volume low-touch plans).** Discharge the report obligation through equivalent self-service portal data.

10.5 **Telemetry retention.** ≥13 months, aligning with parent CSA Exhibit C audit-log defaults.

---

## 11. Disaster recovery & business continuity

How the Vendor restores the Service after major disruption, including Iceland-specific regulatory overlays.

11.1 **Plan.** The Vendor maintains a written disaster-recovery and business-continuity plan (Áfallaviðbragðsáætlun) covering scope, recovery priorities, RTO and RPO, alternate-site arrangements, communications, and escalation.

11.2 **Objectives.** Default RTO `{{RTO}}` (4 hr); default RPO `{{RPO}}` (1 hr). Tighter per-Service objectives may be set in the Order Form.

11.3 **Testing.** Tested at least annually; outcomes documented; redacted summary provided on request.

11.4 **Customer-favoured posture (OPTIONAL — only if RTO/RPO is critical to Customer operations).** RTO ≤ 1 hr, RPO ≤ 15 min; semi-annual tests; full unredacted test reports under confidentiality.

11.5 **Lög nr. 78/2019 — security management.** Where the Vendor is an essential or important entity within **Lög nr. 78/2019 um öryggi net- og upplýsingakerfa mikilvægra innviða** (anticipated to be amended for NIS2 once EEA-incorporated `[VERIFY]`), the Vendor maintains technical, operational, and organisational measures proportionate to the risks and consistent with the Act's risk-management requirements.

11.6 **CERT-IS coordination.** For national-impact or critical-infrastructure incidents, the Vendor coordinates with **CERT-IS** (cert.is) at `{{CERT-IS Reporting Email}}` consistent with Iceland's national framework and the EU/EEA cooperative cyber-defence framework.

11.7 **Lög nr. 90/2018 Art. 27 — security of processing.** Vendor maintains measures appropriate to the risk under **Lög nr. 90/2018 Art. 27** (mirroring GDPR Art. 32), further described in Exhibit C of the parent CSA: (a) pseudonymisation and encryption where appropriate; (b) ongoing confidentiality, integrity, availability, resilience; (c) timely post-incident restoration; (d) regular testing and evaluation.

11.8 **Certification.** The Vendor maintains — or pursues with a documented roadmap — **ISO/IEC 27001** certification, and for cloud-delivered Services **ISO/IEC 27017**. Current certificates available on request.

11.9 **DORA via EEA — financial-entity Customers.** Where the Customer is FME-regulated and the Vendor is an ICT third-party service provider under §3.3, the Vendor complies with the ICT business-continuity policy and testing obligations under EEA-incorporated **DORA Arts. 11 and 25**, including operational-resilience testing scenarios proportionate to the Customer's critical or important functions.

11.10 **Recovery communications.** Updates to the Customer at intervals ≤ 60 min during an active P1 incident, with named incident-commander details supplied promptly after declaration.

---

## 12. Scheduled & emergency maintenance

Vendor-initiated work on the Service.

12.1 **Scheduled Maintenance.** Within `{{Maintenance Window}}` (default Saturdays 02:00–06:00 UTC = Reykjavik local, given permanent UTC+0). Notice ≥ `{{Maintenance Notice Window}}` (default 7 calendar days) by status-page post and email.

12.2 **Emergency Maintenance.** Notice as feasible — at least `{{Emergency Notice Window}}` (default 2 hours where feasible) — by status-page post. Excluded Downtime under §5(b).

12.3 **Customer-favoured posture (OPTIONAL — only where the default window is Customer peak-load).** Move the window; non-security notice 14 calendar days; same-day post-mortem for any Emergency Maintenance > 30 min.

12.4 **Vendor-favoured posture (OPTIONAL — only for early-stage Services).** Permit a second mid-week window with 5 calendar-day notice.

12.5 **Public-holiday avoidance.** No non-essential Maintenance during the Icelandic Christmas / New Year period (24 Dec – 2 Jan) or on the National Day (17 June) without express Customer agreement.

---

## 13. Service degradation vs. outage

Distinguishes partial impairment from full unavailability. Both are reported; credits flow primarily for outages.

13.1 **Outage.** A period during which the Service is not Available within §2.2. Counts fully against Availability.

13.2 **Degradation.** A period during which the Service is Available but a specific function or performance characteristic falls materially below documented levels (e.g., latency above p95, error rates above baseline, or a non-critical feature unavailable).

13.3 **Credit treatment.** Degradations do not, by default, count against Availability and do not trigger Availability credits, but they do count toward §10 reporting and may trigger support credits where the underlying ticket misses a Severity target.

13.4 **Customer-favoured posture (OPTIONAL — only for time-critical workflows).** Add a "performance SLA" capping latency p95 at a stated millisecond figure; exceedance is an Availability miss.

13.5 **Vendor-favoured posture (OPTIONAL — only for non-real-time Services).** Latency, throughput, and concurrency are best-efforts only.

13.6 **Public communications.** Outage or degradation, the Vendor describes the event accurately on the status page; mislabelling does not alter Availability calculation but may evidence bad faith for §14 purposes.

---

## 14. Material SLA breach & termination right

Threshold at which repeated misses justify Customer termination of the affected subscription without penalty.

14.1 **Threshold.** A Material SLA Breach occurs where the Vendor fails to meet the Uptime Tier in `{{Termination Threshold}}` (default 3 consecutive months, or any 3 of a rolling six-month period).

14.2 **Termination right.** On occurrence, Customer may terminate the affected subscription on 30 days' written notice without early-termination charge, with pro-rata refund of pre-paid Fees for the unexpired Subscription Term. Exercisable within 90 days of the third qualifying month; non-exercise does not waive the right for any subsequent breach.

14.3 **Customer-favoured posture (OPTIONAL — only for critical-function Services or FME-regulated Customers).** Threshold 2 consecutive months; add severity-based trigger (≥ 3 missed P1 resolutions in any rolling six-month period).

14.4 **Vendor-favoured posture (OPTIONAL — only for low-margin or volume-discounted plans).** Threshold 4 consecutive months; refunds limited to credits issued and unused.

14.5 **Parent-agreement coordination.** This right is additional to — does not replace — any termination-for-breach right in the parent CSA.

14.6 **Regulatory-driven termination.** Where FME or the Customer's sectoral supervisor directs exit under EEA-incorporated DORA Art. 28(7) or equivalent, Customer may terminate without termination charge on regulator-required notice.

---

## 15. Changes to this SLA

Vendor-proposed changes.

15.1 **Non-material.** Clarifications, typo fixes, and visibility-increasing reporting features may be made on 30 days' status-page or trust-centre notice.

15.2 **Material.** Reductions in Uptime Tier, expansion of Excluded Downtime, weakening of Severity targets, or reductions in credit caps require Customer prior written consent (normally amended Order Form), with ≥ 60 days' notice and good-faith consideration of objections.

15.3 **Customer-favoured posture (OPTIONAL — only where the Service is integrated into a regulated operating model).** Any change to incident-notification timelines or RTO/RPO is material regardless of nominal magnitude.

15.4 **Vendor-favoured posture (OPTIONAL — only for low-touch self-service plans).** Changes by published notice; Customer may terminate without penalty within the notice period.

15.5 **Regulatory-driven.** Where required by Persónuvernd, FME, PFS, CERT-IS, an EEA-incorporated EU instrument, or any other competent authority, the Vendor implements on the mandated timeline; not a Material SLA Breach.

---

## 16. Survival & order of precedence

Which clauses survive termination and how this SLA fits with the parent CSA and the Order Form.

16.1 **Survival.** §§ 7 (credits accrued pre-termination), 8, 9, 14 (where invoked), 17 (events during the Subscription Term), 18, and this §16 survive to the extent necessary.

16.2 **Order of precedence.** Where this SLA attaches as an Exhibit: (i) executed Order Form (scope-limited); (ii) parent CSA Data Processing Addendum (Exhibit C); (iii) this SLA; (iv) parent CSA master terms; (v) other exhibits and policies. Nothing in this SLA reduces a Customer right granted in the parent CSA's data-protection or confidentiality provisions.

16.3 **Severability.** If any clause is held invalid by a competent Icelandic court or supervisory authority, the remaining clauses continue, and the Parties negotiate in good faith a replacement achieving the original commercial intent within Icelandic and EEA law.

16.4 **No-waiver.** Failure to enforce a miss or exercise a remedy is not a waiver of any other.

---

## 17. Incident-response coordination — Iceland breach notification

Coordinates incident-reporting obligations across Iceland's principal supervisory regimes (Persónuvernd, sectoral / CERT-IS, FME under DORA, PFS for telecom). Read with parent CSA Exhibit C.

17.1 **GDPR Art. 33 + Lög nr. 90/2018 — personal-data breach.** Where an incident is a "personal-data breach" within GDPR Art. 4(12) and **Lög nr. 90/2018**: (a) the Vendor (as processor / vinnsluaðili) notifies the Customer in writing **without undue delay** after becoming aware (Art. 33(2)); (b) Vendor's contractual SLA for that notification is `{{Vendor Breach SLA}}` (default 24 hours from awareness); (c) the notification follows the Exhibit C content list and at minimum includes nature of the breach (with categories and approximate numbers of data subjects and records where possible), DPO or contact-point details, likely consequences, and measures taken or proposed to address and mitigate; (d) the Customer (as controller) notifies **Persónuvernd** at `{{Persónuvernd Reporting Email}}` (default postur@personuvernd.is) within **72 hours** of becoming aware unless unlikely to result in a risk to the rights and freedoms of natural persons (Art. 33(1)); (e) where high-risk to data subjects, the Customer communicates to data subjects without undue delay under Art. 34, with reasonable Vendor assistance.

17.2 **Lög nr. 78/2019 — NIS-equivalent reporting.** Where the Vendor is classified under §3.2 as essential or important: (a) the Vendor reports significant incidents to **CERT-IS** at `{{CERT-IS Reporting Email}}` and (where required) to the relevant sectoral competent authority within Act-mandated timelines; (b) once Directive (EU) 2022/2555 (NIS2) is EEA-incorporated and Icelandic-transposed `[VERIFY EEA NIS2 transposition status]`, the expected cascade is **early-warning within 24 hours**, **incident notification within 72 hours**, and **final report within 1 month** of the incident notification; (c) the Vendor keeps the Customer informed of any material development relevant to the Customer's own regulatory or contractual reporting, subject to confidentiality and law-enforcement constraints.

17.3 **DORA via EEA — ICT-related incident reporting (financial entities).** Where the Customer is FME-regulated and the Vendor is an ICT third-party service provider under §3.3: (a) the Customer reports Major ICT-related Incidents to **Fjármálaeftirlitið (FME)** consistent with EEA-incorporated **DORA Art. 19** and any Icelandic implementing regulations `[VERIFY EEA DORA transposition status]`; (b) to support that reporting, the Vendor commits to **`{{Major ICT Incident SLA}}`** (default 2 hours from awareness) initial notification for any incident reasonably believed to meet the DORA Art. 18 materiality threshold; (c) Vendor provides reasonable assistance in preparing intermediate and final DORA reports, including documented root-cause analysis and remediation plan.

17.4 **Lög nr. 70/2022 — telecom-specific breach notification.** Where the Vendor provides electronic communications services within **Lög nr. 70/2022 um fjarskipti**, the Vendor notifies **Póst- og fjarskiptastofnun (PFS)** of security incidents and integrity-affecting events under the Act's timelines and content-requirements `[VERIFY current PFS reporting interface]`, and keeps the Customer informed where the Customer has onward reporting obligations.

17.5 **CERT-IS — national-impact incidents.** For incidents with national-impact significance — affecting critical infrastructure, large numbers of Icelandic users, or cross-border supply chains — the Vendor cooperates with **CERT-IS** under Iceland's national framework and the EU/EEA cooperative cyber-defence framework, including timely sharing of indicators of compromise, attribution (where reasonably available), and remediation status, subject to confidentiality and law-enforcement constraints.

17.6 **Joint communications.** The Parties coordinate public communication of any notifiable incident so statements are consistent, accurate, and timed to avoid prejudicing supervisory investigations. Neither Party names the other publicly without consent except as required by law or competent authority.

---

## 18. Insurance & cyber liability

Confirms Vendor insurance proportionate to risk and addresses regulatory-fines exposure under Iceland's transposed GDPR regime.

18.1 **Coverage.** Vendor maintains, with insurers of recognised EEA standing, the policies specified in parent CSA §17, including cyber-liability or technology-E&O cover with per-claim and aggregate limits ≥ `{{Insurance Cyber Limit}}` (default ISK 750,000,000 ≈ EUR 5,000,000 at indicative reference rates).

18.2 **Evidence.** Certificate of insurance on reasonable request; 30 days' written notice of any cancellation or material reduction.

18.3 **Persónuvernd administrative fines.** Administrative fines imposed by **Persónuvernd** under Lög nr. 90/2018, mirroring GDPR Art. 83 ceilings as transposed `[VERIFY current króna-denominated ceilings and any indexation mechanism]`, may be uninsurable in some markets or as a matter of public policy. Allocation is governed by the parent CSA's indemnification and liability provisions; nothing in this SLA shifts a fine the law requires a particular Party to bear.

18.4 **Deductibles.** Each Party bears its own cyber-liability deductibles unless the parent CSA allocates differently.

---

## 19. Governing law & supervision

Confirms governing law and preserves Icelandic supervisory powers.

19.1 **Governing law.** Governed by the law applicable to the parent CSA under its §18. Where the IS-variant default applies, that law is **Icelandic law**, excluding conflict-of-laws rules and the UN CISG.

19.2 **Forum.** Disputes per the parent CSA dispute-resolution clause. Where the IS-variant default applies, the parties submit to **Héraðsdómur Reykjavíkur** as court of first instance, with appeal to the Landsréttur and ultimately the Hæstiréttur.

19.3 **Preserved supervisory powers.** Nothing in this SLA limits the supervisory and enforcement powers of Persónuvernd (Lög nr. 90/2018), FME (EEA-incorporated DORA), PFS (Lög nr. 70/2022), CERT-IS and the relevant sectoral authority (Lög nr. 78/2019), or Neytendastofa. Each Party complies with lawful directions of these authorities and reasonably assists the other in its own compliance.

19.4 **Cross-border claims — Lugano.** Where a counter-party or claim has its centre of gravity in another Lugano Convention 2007 contracting state, the Parties acknowledge the **Lugano Convention 2007** on jurisdiction and judgment-recognition as the applicable conflict-of-jurisdictions instrument `[VERIFY current applicability and any post-Brexit refinements]`. Where Lugano does not apply, Brussels-recast or general private-international-law rules apply by default.

19.5 **EFTA Surveillance Authority.** Where an EU-derived obligation is enforced via the EEA framework, the Parties acknowledge the supervisory role of the **EFTA Surveillance Authority (ESA)** over Iceland's EEA compliance.

---

## Annex A — Severity matrix

Severity is assigned by the Customer at ticket creation, subject to reclassification per §6.1.

| Band | Description | Response | Resolution | Coverage |
|------|------------|----------|------------|----------|
| **P1 — Critical** | Service unavailable; loss of core function for all or substantially all users; data integrity at risk; active personal-data breach within GDPR Art. 33 / Lög nr. 90/2018 | `{{P1 Response Target}}` (default 15 min) | `{{P1 Resolution Target}}` (default 4 hr) — fix or Workaround | 24×7 |
| **P2 — High** | Major function degraded; significant business impact; no practical workaround | `{{P2 Response Target}}` (default 1 hr) | 1 business day | 24×7 |
| **P3 — Medium** | Non-critical; functional workaround exists; limited business impact | `{{P3 Response Target}}` (default 4 business hr) | 5 business days | Business hours |
| **P4 — Low** | Minor; cosmetic; documentation gap; feature request | `{{P4 Response Target}}` (default 1 business day) | Next regularly scheduled release | Business hours |

Customer-favoured tightening per §6.4; reclassification disputes per §6.1.

---

## Annex B — Service Credit calculation

Pick the grid for the contracted `{{Uptime Tier}}`; the Vendor's billing system implements the credit at month-end (§8.5) or on request (§8.1). All bands subject to the §7.3 Cap.

**99.9% tier (default):** ≥99.9% → 0; ≥99.0%/<99.9% → 10%; ≥95.0%/<99.0% → 25%; <95.0% → 50%.

**99.95% tier (Customer-favoured, financial-services-grade):** ≥99.95% → 0; ≥99.5%/<99.95% → 15%; ≥99.0%/<99.5% → 30%; <99.0% → 50%.

**99.5% tier (Vendor-favoured, early-stage / discounted):** ≥99.5% → 0; ≥99.0%/<99.5% → 5%; ≥95.0%/<99.0% → 15%; <95.0% → 30%.

**Support credits (additive):** missed P1 → 5%; missed P2 → 2%; missed P3 (Customer-favoured only) → 1%.

**Worked example.** 99.9% tier; monthly Fees ISK 1,200,000; Availability 98.4% (single 11.5-hour outage). Band 25% + 1 missed P1 resolution +5% = 30% × 1,200,000 = **ISK 360,000**, at the default Credit Cap; applied automatically against the next invoice per §9.1.

---

## Annex C — Sample monthly performance report

The Vendor publishes a monthly report substantially in this form. Numerical fields are supplied; narrative fields are at least one paragraph.

```
Service: {{Service Name}}
Reporting period: YYYY-MM-01 to YYYY-MM-DD (Atlantic/Reykjavik, UTC+0)
Report published: YYYY-MM-15

1. Availability summary
   Service Minutes; Excluded Downtime (§5); Adjusted Service Minutes;
   Measured Availability (% to four decimal places); Uptime Tier
   ({{Uptime Tier}}); tier met / missed.

2. Incident summary (P1 / P2 only)
   Per incident: ID; start/end (UTC = Reykjavik local); duration;
   affected component(s); impact summary; root cause (post-mortem
   reference); remediation; Excluded Downtime classification under §5.

3. Support metrics
   P1 / P2 volumes, median and 95th-percentile response and resolution;
   P3 / P4 volumes, median response (business hours); severity
   reclassifications.

4. Service Credits
   Auto-issued (§8.5); pending Customer requests; total applied.

5. Regulatory incident-notifications (§17 cross-reference)
   Art. 33(2) breaches notified to Customer; CERT-IS NIS-Iceland
   notifications (where Vendor in scope); DORA major-ICT-incident
   notifications (where applicable); PFS notifications (where ECS).

6. Forward-looking notes
   Planned Scheduled Maintenance; capacity / scaling actions; open
   remediation items with target dates.
```

---

## Merge fields used

Iceland-specific fields (apply global search-and-replace before execution):

```
{{Vendor Kennitala}}              # 10-digit Icelandic national-registry number
{{Customer Kennitala}}            # Customer's kennitala
{{Vendor NIS-IS Class}}           # essential | important | N/A — §3.2
{{Vendor DORA Class}}             # ICT third-party for FE | N/A — §3.3
{{CERT-IS Reporting Email}}       # per cert.is published contact
{{Persónuvernd Reporting Email}}  # default postur@personuvernd.is
{{Status Page URL}}               # public Vendor status page
{{Vendor Breach SLA}}             # GDPR Art. 33(2) SLA (default 24 h)
{{Major ICT Incident SLA}}        # DORA Art. 18 SLA (default 2 h)
{{Insurance Cyber Limit}}         # default ISK 750,000,000 ≈ EUR 5,000,000
```

Pack-common fields used unchanged: `{{Vendor Legal Name}}`, `{{Customer Legal Name}}`, `{{Service Name}}`, `{{Service URL}}`, `{{Effective Date}}`, `{{Last Updated Date}}`, `{{Uptime Tier}}`, `{{Uptime Measurement Method}}`, `{{Maintenance Window}}`, `{{Maintenance Notice Window}}`, `{{Emergency Notice Window}}`, `{{Credit Cap Percent}}`, `{{Credit Window Days}}`, `{{Reporting Cadence}}`, `{{P1/P2/P3/P4 Response Target}}`, `{{P1 Resolution Target}}`, `{{Support Hours}}`, `{{Support Channels}}`, `{{Support Time Zone}}`, `{{RTO}}`, `{{RPO}}`, `{{Termination Threshold}}`.

---

## Authoritative references

Drafting was guided by the following permissively-licensed and public-domain sources. No five-or-more-word verbatim runs were taken; structure and clause-headings were used as drafting guides only.

- **althingi.is** — consolidated text of Lög nr. 7/1936 (Samningalög), Lög nr. 32/1997 (almenna frídaga), Lög nr. 73/1972 (höfundarétt), Lög nr. 82/2008 (almannavarnir), Lög nr. 90/2018 (persónuverndarlög), Lög nr. 78/2019 (öryggi net- og upplýsingakerfa), Lög nr. 70/2022 (fjarskiptalög)
- **personuvernd.is** — breach-notification, processor, and Art. 27 / 32 guidance
- **fme.is** — outsourcing, ICT-risk, and DORA implementation guidance
- **cert.is** — CERT-IS contact and incident-handling guidance
- **pfs.is** — telecom-incident reporting under Lög nr. 70/2022
- **eur-lex.europa.eu** — GDPR (2016/679), NIS2 (2022/2555), DORA (2022/2554), eIDAS (910/2014)
- **EFTA Surveillance Authority (eftasurv.int)** — EEA incorporation of EU acquis
- **Bonterms SLA** — CC-BY-4.0 (primary structural baseline)
- **Common Paper CSA SLA exhibit** — CC-BY-4.0 (severity matrix and credit grid)
- **GitHub site-policy** — CC0 (clause-heading conventions)
- **Mozilla legal templates** — MPL-2.0 (regional-overlay pattern)
- **Linux Foundation / Apache project SLAs** — Apache-2.0 (operational-reporting patterns)

---

## Companion Icelandic-language draft

A parallel Icelandic-language draft — `is-isl.md` — is forthcoming. When published, the Icelandic-language version controls in any dispute, regulatory submission, or court proceeding (see the bilingual-usage callout above §1). Until then, this English text is the operative SLA as the Parties' agreed working language.

---

## Not legal advice

This template is provided for general information and as a starting point for drafting. It is not legal advice and does not create a lawyer-client relationship between Fordæmi ehf., the Legalcode authors, and any reader. Iceland's and the EEA's regulatory landscape — particularly NIS2 and DORA transposition status, current Persónuvernd fine ceilings in ISK, the present text of Lög nr. 78/2019, the published PFS reporting interface, and the continuing applicability of the Lugano Convention 2007 — changes; each `[VERIFY]` marker flags an item that a qualified Icelandic-admitted lawyer (and where DORA applies, a qualified financial-services regulatory lawyer) should confirm before execution. Use of this template is at the user's risk.
