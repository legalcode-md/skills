---
title: Service Level Agreement — United States
jurisdictions: [us, us-ca, us-ny, us-tx, us-de]
statutes: [State-breach-notification-laws, NYDFS-Reg-500, MA-201-CMR-17, TX-SB-820, NIST-CSF, CISA, FTC-Act]
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

# Service Level Agreement — United States Variant

> Clean-room template assembled from permissively licensed baselines (Bonterms `[CC-BY-4.0]`, Common Paper CSA `[CC-BY-4.0]`, GitHub `[CC0]`, Mozilla `[MPL-2.0]`, Linux Foundation / Apache `[Apache-2.0]`) and US public-domain government materials (NIST SP 800-61, NIST SP 800-34, NIST CSF, CISA, FTC, state AG breach statutes). This SLA is an exhibit to, and governed by, the Master Cloud Services Agreement (the "**CSA**") executed between **{{Vendor Legal Name}}** ("**Vendor**") and **{{Customer Legal Name}}** ("**Customer**").

---

## 1. Plain-language summary

This section gives a non-binding overview; later sections control on conflict. Vendor commits to **{{Uptime Percentage}}** (default `99.9%`) monthly availability at the production endpoint. When monthly availability falls below the target, Customer may claim a Service Credit computed as a percentage of the affected Service's monthly fee, capped at **{{Monthly Credit Cap}}** (default `30%`). Severity-1 incidents receive a `15-minute` initial response, `24×7`. Other tickets are handled during **{{Support Time Zone}}** (default `US Eastern Time`) business hours under §6 and Annex A. Service Credits are the sole and exclusive monetary remedy for missed targets, subject to the termination right in §14 and to mandatory state law. Incident notification, state breach-notification timelines, NYDFS Reg 500, the SEC Cyber Disclosure Rule, insurance, and dispute resolution are in §§17–19. This SLA is not legal advice and should be reviewed by qualified US counsel.

---

## 2. Definitions

This section defines repeating terms; capitalized words not defined here take their CSA meanings.

- "**Available**" — the Service is reachable at the production endpoint, returns HTTP `2xx` (or documented protocol equivalent) to Vendor's external synthetic probes, and operates within published functional tolerances.
- "**Calendar Month**" — a calendar month measured in **{{Measurement Time Zone}}** (default `UTC`).
- "**Customer Data**" — as defined in the CSA, including any Personal Information, Protected Health Information ("PHI"), or Cardholder Data ("CHD") in the Service.
- "**Downtime**" — any continuous period of `≥1` minute during which the Service is not Available, excluding Excluded Downtime.
- "**Incident**" — a discrete event or sustained condition causing Downtime or Service Degradation.
- "**Monthly Service Fee**" — recurring fee for the affected Service for the Calendar Month, excluding usage overages, professional services, and one-time fees.
- "**Personal Information**" or "**PI**" — as defined under the relevant US state breach-notification statute (e.g., Cal. Civ. Code §1798.82(h)).
- "**Service**" — the cloud offering identified in the Order Form.
- "**Service Credit**" — the credit calculated under §7 and Annex B.
- "**Service Degradation**" — measurable performance loss not amounting to full unavailability (see §13).
- "**Severity Level**" — P1 / P2 / P3 / P4 per Annex A.
- "**Status Page**" — Vendor's incident-communications page at **{{Status Page URL}}**.
- "**Uptime Percentage**" — for any Calendar Month, `[(Total Minutes − Downtime Minutes − Excluded Downtime Minutes) ÷ (Total Minutes − Excluded Downtime Minutes)] × 100`.

---

## 3. Scope of services covered

This section identifies what is measured. The SLA covers production-tier components identified in the Order Form, accessed through the documented production endpoint(s). It does **not** cover (a) sandbox, beta, preview, alpha, or "Early Access" features, (b) third-party integrations outside Vendor's operational control, (c) Customer-side networks, devices, or identity providers, or (d) features marked "no SLA" in the Documentation.

**HIPAA / PHI.** If Vendor processes PHI under a Business Associate Agreement ("**BAA**"), the BAA may impose elevated availability, breach-notification, and audit-log retention obligations; the BAA controls over this SLA for PHI workloads.

**PCI-DSS / CHD.** If the Service processes CHD within PCI-DSS scope, the CHD environment is segregated and governed by the PCI-DSS Addendum; if the Addendum sets stricter targets, the stricter target controls.

**Customer perspective:** Confirm every endpoint, region, and feature it relies upon is on the Order Form. **Vendor perspective:** SLA scope tracks what Vendor operationally controls.

---

## 4. Service Availability commitment

This section sets the uptime target and verification method. Vendor commits to Uptime Percentage of at least **{{Uptime Percentage}}** (default `99.9%`) per Calendar Month for production region(s) on the Order Form. Availability is measured by external synthetic monitoring (probe interval `≤60` seconds, distributed across at least three US regions), with raw data retained for `13` months. A minute counts as Down only if a majority of probes fail and the failure is not Excluded Downtime under §5.

Equivalent monthly Downtime budgets at common targets (illustrative, based on a 30-day month / `43,200` total minutes):

| Target | Maximum Downtime / month |
|--------|--------------------------|
| `99.0%` | ~`7h 12m` |
| `99.5%` | ~`3h 36m` |
| `99.9%` | ~`43m 12s` |
| `99.95%` | ~`21m 36s` |
| `99.99%` | ~`4m 19s` |

**Customer perspective:** Higher targets command premium pricing and tighter exclusions. **Vendor perspective:** A single regional sub-provider event can consume the entire monthly budget at `99.99%`.

OPTIONAL — only if the Order Form elects multi-region or active-active topology: a higher Uptime target may apply to the failover SKU.

---

## 5. Excluded Downtime

This section lists conditions that do not count against the uptime budget; Vendor bears the burden of substantiating each invocation.

- (a) **Scheduled Maintenance** under §12;
- (b) **Emergency Maintenance** under §12, with contemporaneous Status Page notice and a post-incident report within `5` business days;
- (c) **Force majeure** as defined in the CSA;
- (d) **Customer-caused** outages, including tenant misconfiguration, exceeding rate limits, exhausting purchased capacity, faulty Customer code, or credential mismanagement;
- (e) **Third-party network failures** outside Vendor's direct control (upstream ISP, DNS registrar, CA, public cloud sub-provider regional event), unless Vendor pledged a higher posture on the Order Form;
- (f) **Suspension** under the CSA (non-payment, abuse, security);
- (g) **Beta / preview features** and components flagged "no SLA";
- (h) **Customer Equipment** failures (end-user devices, VPN concentrators, corporate appliances);
- (i) **DoS attacks against Customer's tenant only**, where Vendor applied commercially reasonable mitigation;
- (j) **Internet-routing pathologies** beyond Vendor's edge (e.g., BGP route leaks);
- (k) **Customer-authorized changes** that Vendor warned may cause an outage;
- **(l) Government-ordered service interruption**, including national-security emergency, FBI / CISA / DHS directives, or any federal or state directive where compliance is legally compelled;
- **(m) Subpoena-compelled service modification**, including a court order, search warrant, or National Security Letter requiring Vendor to alter, suspend, or limit functionality, where Vendor uses commercially reasonable efforts to narrow scope.

**Customer perspective:** Review (e), (l), (m) — jurisdiction-driven and risk-shifting. **Vendor perspective:** These exclusions underwrite the headline target.

---

## 6. Support response & resolution targets

This section sets ticket acknowledgment and work targets by severity. Severity is initially set by Customer and may be reclassified by Vendor under Annex A with documentation in the ticket. Targets run from ticket creation to Vendor's first substantive (non-automated) response.

| Severity | Initial Response | Status Update Cadence | Workaround / Resolution Target | Hours of Coverage |
|---|---|---|---|---|
| **P1 — Critical** | `15` minutes | Hourly | Continuous effort until workaround | `24×7` |
| **P2 — High** | `1` business hour | Every `4` business hours | Workaround within `1` business day | Business hours (`{{Support Time Zone}}`) |
| **P3 — Medium** | `1` business day | Every `2` business days | Resolution in next regular release | Business hours |
| **P4 — Low** | `3` business days | Weekly | Backlog / roadmap | Business hours |

"**Business hours**" means `08:00–18:00` **{{Support Time Zone}}** (default `US Eastern Time`), Mon–Fri excluding US federal holidays. P1 coverage is `24×7×365`. Tickets via **{{Support Portal URL}}**; for P1, Customer may also page **{{P1 Pager Number}}**.

**Customer perspective:** Align ticket-routing and on-call contacts to the matrix. **Vendor perspective:** P1 should be reserved for production-impacting events.

OPTIONAL — only if the Order Form elects Premier / Mission-Critical support: tightened targets in the Premier Support Schedule replace the table above.

---

## 7. Service Credits

This section translates SLA misses into refunds; math is in Annex B, request mechanics in §8. If Uptime Percentage falls below target, Customer is eligible for a Service Credit against the Monthly Service Fee for the affected Service:

| Monthly Uptime % | Service Credit (% of Monthly Service Fee) |
|---|---|
| < `99.9%` and ≥ `99.0%` | `10%` |
| < `99.0%` and ≥ `95.0%` | `25%` |
| < `95.0%` | `30%` (cap = **{{Monthly Credit Cap}}**) |

Total Service Credits in any Calendar Month will not exceed **{{Monthly Credit Cap}}** (default `30%`) of that month's Monthly Service Fee, regardless of Incident count.

**FTC "negative option" note.** Service Credits are a remedy for non-conforming performance, not a recurring charge; the Parties do not treat them as a "negative option feature" under the FTC's Click-to-Cancel rule, 16 C.F.R. Part 425 `[VERIFY current rule text and effective date]`. Nothing here circumvents any consumer-protection statute that would otherwise apply.

**Customer perspective:** Track Downtime against Customer's own monitoring; §10 grants inspection rights. **Vendor perspective:** The cap is an underwriting parameter.

---

## 8. Credit request procedure

This section sets the only valid path to claim a credit; missing the window or channel forfeits the credit. Customer must submit a written claim via **{{Support Portal URL}}** with subject "**SLA Credit Request — [Month YYYY]**" within `30` days after month-end. The claim must include:

1. Account identifier and affected region(s);
2. Calendar Month at issue;
3. Downtime statement (start, end, duration) referencing Customer monitoring or Status Page entries;
4. Asserted Uptime Percentage and credit calculation; and
5. Ticket numbers for relied-upon Incidents.

Vendor acknowledges within `5` business days and issues a written determination within `30` days, citing probe and incident data. Disputes follow §19 informal escalation before further action.

**Customer perspective:** Clocks run from month-end. **Vendor perspective:** A defined window prevents stale claims.

---

## 9. Credit issuance & exclusivity as remedy

This section explains how credits are paid and limits SLA-only claims, with carve-outs. Approved Service Credits are issued against the next invoice or — if Customer is no longer paying — as a refund to the original payment method, within `45` days of approval. Credits do not accrue interest and expire if unused within `12` months.

**Service Credits are the sole and exclusive remedy for any failure to meet the §4 availability commitment or the §6 support targets**, except (a) as provided in §14 (Material SLA Breach & Termination Right), and (b) where exclusive-remedy clauses are prohibited or limited by mandatory state law (e.g., the New Jersey Truth-in-Consumer-Contract Act for B2C; for B2B, Service Credits are typically enforceable as exclusive remedy under California, New York, Texas, and Delaware law, subject to unconscionability review under Cal. Civ. Code §1670.5 and analogous standards).

This exclusivity does not limit (i) Customer's CSA rights to security, confidentiality, indemnification, or data processing, (ii) BAA or PCI-DSS Addendum rights, or (iii) §17 / §18 rights.

**Customer perspective:** Preserve non-SLA rights in the parent CSA. **Vendor perspective:** Bounded liability makes the credit math underwritable.

---

## 10. Performance reporting & status page

This section sets reporting obligations. Vendor operates a public Status Page at **{{Status Page URL}}**. For each P1 / P2 Incident affecting Customer, Vendor will publish (a) initial acknowledgment within `30` minutes of confirmation, (b) updates per §6 cadence, (c) a closure notice, and (d) a Root-Cause Analysis ("**RCA**") within `10` business days, covering timeline, contributing factors, impact, remediation, and prevention.

Vendor delivers a quarterly availability report within `15` calendar days after each Calendar Quarter (Annex C). Customer may request an ad-hoc report once per Calendar Month, with delivery within `10` business days.

**Customer perspective:** Subscribe to Status Page notifications. **Vendor perspective:** Public reporting is a credibility tool — do not over-promise cadence.

---

## 11. Disaster recovery & business continuity

This section sets recovery targets aligned to US frameworks. Vendor maintains and tests a written Disaster Recovery ("**DR**") / Business Continuity ("**BC**") program with Recovery Time Objective ("**RTO**") and Recovery Point Objective ("**RPO**") targets for regional or systemic failures.

| Metric | Target |
|---|---|
| **RTO (Recovery Time Objective)** | **{{RTO Hours}}** (default `4` hours) |
| **RPO (Recovery Point Objective)** | **{{RPO Hours}}** (default `1` hour) |
| **DR test frequency** | At least annually; tabletop and partial-failover exercises documented |
| **Backup retention** | Encrypted backups retained for at least `30` days, with quarterly restore validation |

§11.1 Vendor notifies Customer without undue delay when a DR event is invoked.
§11.2 Vendor provides the executive summary of its most recent DR test on request, subject to confidentiality.
§11.3 Vendor will not unilaterally degrade the production region during a DR event without first attempting in-region recovery, unless doing so would prolong customer impact.
§11.4 Backup encryption keys are managed under the key-management policy referenced in the CSA security exhibit.
§11.5 Vendor's continuity planning is structurally consistent with **NIST SP 800-34 Rev. 1 (Contingency Planning Guide)** as a planning reference, not a binding control set.
§11.6 If Vendor or Customer is a Covered Entity under **23 NYCRR Part 500** ("**NYDFS Reg 500**"), the Parties coordinate incident-response and continuity practices to support **§500.16** (incident response plan) and §500.17 (notification) `[VERIFY current Reg 500 text after amendments]`.
§11.7 If Vendor processes Personal Information of Massachusetts residents, Vendor maintains a written information-security program structurally consistent with **201 CMR 17.04** (encryption in transit / at rest, access controls, program review) `[VERIFY 201 CMR 17 specifics]`.
§11.8 If Customer is a Texas K-12 school district or charter school, Vendor's controls are consistent with **Texas SB 820 (87R)** and Texas Education Code §11.175 (district cybersecurity policy and DIR coordination) `[VERIFY current Texas statute citations]`.

**Customer perspective:** Map RTO / RPO to dependent business processes; RPO `1` hour means up to one hour of writes may be lost. **Vendor perspective:** RTO / RPO are pricing levers; tighter targets require multi-region topology on the Order Form.

---

## 12. Scheduled & emergency maintenance

This section sets when and how Vendor takes maintenance windows. Scheduled Maintenance is announced `≥7` days in advance via Status Page and email to **{{Customer Notification Email}}**, performed within the standard window `Saturday 04:00–08:00 UTC` (see conversion table), and counted as Excluded Downtime. Emergency Maintenance may be performed on as little notice as is reasonable to address a security vulnerability, prevent data loss, or comply with a regulatory directive; Vendor posts contemporaneous Status Page notice and a written post-incident report within `5` business days.

UTC-to-US conversion table for the standard maintenance window (`Saturday 04:00–08:00 UTC`):

| US Time Zone | Local Window |
|---|---|
| `US Eastern Time` (`UTC−5` standard / `UTC−4` daylight) | `Fri 23:00 – Sat 03:00` (standard) / `Sat 00:00 – 04:00` (daylight) |
| `US Central Time` (`UTC−6` / `UTC−5`) | `Fri 22:00 – Sat 02:00` / `Fri 23:00 – Sat 03:00` |
| `US Mountain Time` (`UTC−7` / `UTC−6`) | `Fri 21:00 – Sat 01:00` / `Fri 22:00 – Sat 02:00` |
| `US Pacific Time` (`UTC−8` / `UTC−7`) | `Fri 20:00 – Sat 00:00` / `Fri 21:00 – Sat 01:00` |
| `Alaska Time` (`UTC−9` / `UTC−8`) | `Fri 19:00 – Sat 23:00` / `Fri 20:00 – Sat 00:00` |
| `Hawaii–Aleutian Time` (`UTC−10`, no DST) | `Fri 18:00 – 22:00` |

OPTIONAL — only if Customer's workload cannot tolerate weekend windows: an alternate maintenance window may be elected on the Order Form for an upcharge.

---

## 13. Service degradation vs. outage

This section distinguishes "slow" from "down". **Service Degradation** means the Service is reachable but below documented functional tolerances — e.g., p95 API latency exceeding the published SLO by more than `2×` for `15` consecutive minutes, error rate above `5%` for `15` consecutive minutes, or a critical workflow failing on `≥25%` of attempts in a `15`-minute window. An **Outage** is non-Availability per §2.

Sustained Service Degradation that materially impairs Customer's documented critical workflows for `≥60` continuous minutes is treated as Downtime for §4 and §7. Brief or isolated excursions are not Downtime. Vendor's performance SLOs are at **{{SLO Documentation URL}}**; SLOs are operational targets and do not by themselves create credit obligations.

---

## 14. Material SLA breach & termination right

This section provides an exit when SLA failures accumulate. Customer may terminate the affected Service (or the entire Order Form) for material breach, with payment only of fees accrued through termination, if any of the following occurs:

- **Chronic Outage:** Uptime Percentage below `99.0%` in any single Calendar Month, **or** below the contracted target in any `3` Calendar Months within a rolling `12`-month period.
- **Chronic P1 Failure:** Vendor misses the P1 Initial Response target on `≥3` occasions in any `30`-day period.
- **Chronic Notification Failure:** Vendor misses the §17 notification window on `≥2` occasions in any `12`-month period.

Customer gives written notice of breach with a cure period of **{{Termination Cure Period}}** (default `30` days, set as a California-law-compatible default consistent with Cal. Civ. Code §1670.5 unconscionability standards and Delaware-law expectations). If Vendor does not cure, Customer may terminate by written notice and receives a pro-rata refund of prepaid, unused fees. Termination is in addition to, not in lieu of, prior Service Credits earned.

**Customer perspective:** Safety valve when credits stop being a real remedy. **Vendor perspective:** Cure period must allow structural remediation while remaining enforceable.

---

## 15. Changes to this SLA

This section explains how the SLA changes during the term. Vendor may modify this SLA, but any modification that materially diminishes Customer's rights (e.g., reducing Uptime Percentage, expanding Excluded Downtime non-trivially, lengthening P1 Initial Response, or reducing credit percentages) requires `30` days' prior written notice to **{{Customer Notification Email}}** and applies prospectively from the next Renewal Term. Customer may reject the change by written notice during the notice period, in which case the unmodified SLA continues for the balance of the current Term.

Non-material changes (clarifications, typo fixes, URL updates, annex refreshes, Customer-favorable improvements) may take effect without notice but are reflected in `last_updated`.

---

## 16. Survival & order of precedence

This section says what survives and which document wins on conflict. The following survive expiration or termination: unpaid Service Credits for pre-termination periods (§§7–9), RCA / reporting / post-incident obligations for in-Term Incidents (§10), confidentiality of incident-response materials (§17), `13`-month availability-data retention (§4), and any CSA survival clause expressly incorporating SLA terms.

Order of precedence (high to low): (1) executed BAA for PHI; (2) PCI-DSS Addendum for CHD; (3) the DPA to the CSA; (4) the CSA body; (5) this SLA; (6) the Documentation; (7) Vendor policies / guidelines. A more specific provision controls over a more general one within the same instrument.

---

## 17. Incident-response coordination for US breach notification

This section explains how Vendor supports Customer's compliance with state breach-notification statutes, on top of CSA / DPA security obligations. A security incident affecting Customer Data may trigger Customer notification under federal law and the breach-notification statutes of the fifty states, DC, and US territories.

### 17.1 Vendor cooperation

If a security incident affecting Customer Data triggers — or in Vendor's reasonable judgment may trigger — Customer notification under any US state breach-notification statute (including **Cal. Civ. Code §1798.82**, **N.Y. Gen. Bus. Law §899-aa**, **Mass. Gen. Laws ch. 93H** with **201 CMR 17**, **Tex. Bus. & Com. Code §521.053**, **Fla. Stat. §501.171**, **Ala. Code §8-38-1 et seq.**, or similar), Vendor will:

- (a) **Notify Customer within `24` hours** of confirmation — deliberately tighter than typical state deadlines (`30` / `45` / `60` days) so Customer can draft notices, brief state AG contacts, and meet statutory clocks;
- (b) **Provide draft notification language** for Customer's review, including factual description, PI categories affected, incident date / estimated date, containment steps, and consumer-protective recommendations;
- (c) **Cooperate with Customer's notification efforts** to consumers, state AGs, and other regulators (e.g., HHS-OCR for PHI, FTC), responding promptly to AG inquiries routed through Customer;
- (d) **Make available forensic logs and incident-response artifacts** subject to confidentiality and legal-hold, including engagement records for any forensic vendor (e.g., **{{Forensic Vendor}}**); and
- (e) **Preserve relevant evidence** with reference to **NIST SP 800-61 Rev. 2** and the **CISA Incident Response Playbook** as planning references.

### 17.2 Interaction with DPA timelines

The `24`-hour Vendor → Customer SLA in §17.1(a) does **not** waive any tighter notification clock in the DPA (Exhibit C of the CSA) or in any data-protection law. Where two clocks apply, the **stricter timeline applies**.

### 17.3 State breach-notification timeline summary (illustrative)

For situational awareness only; statutes change frequently and definitions of "Personal Information," "breach," and triggering harms vary. Drafters should consult current state statutes and AG guidance.

| State | Notification Deadline (to consumer) | Reporting Trigger |
|---|---|---|
| **CA** (Cal. Civ. Code §1798.82) | "Most expedient time possible" / "Without unreasonable delay" | Reasonable belief of unauthorized acquisition of unencrypted Personal Information |
| **NY** (Gen. Bus. Law §899-aa, as amended by SHIELD Act) | "Most expedient time possible" / "Without unreasonable delay" | Same trigger; expanded definition of Personal Information includes biometric and account-credential elements |
| **TX** (Bus. & Com. Code §521.053) | `60` days | Same trigger |
| **FL** (Stat. §501.171) | `30` days | Same trigger; Florida AG must be notified at `≥500` affected residents |
| **MA** (Gen. Laws ch. 93H) | "As soon as practicable and without unreasonable delay" | Same trigger; AG and OCABR notified concurrently |
| **AL** (Code §8-38-1 et seq.) | `45` days | Same trigger |

`[VERIFY each row — several states have amended notification windows, expanded PI definitions, or added regulator-notification thresholds.]`

### 17.4 NYDFS Reg 500 notification (financial entities)

If Customer is a Covered Entity under **23 NYCRR Part 500**, Customer must under **§500.17(a)** notify the NY Department of Financial Services within `72` hours of determining a "Cybersecurity Event" occurred. Vendor provides the factual record needed for that filing on the §17.1(a) timeline and, if instructed in writing, copies **{{NYDFS Notification Email}}**. `[VERIFY current §500.17 thresholds; whether ransomware-payment notification under §500.17(c) applies.]`

### 17.5 SEC Cybersecurity Disclosure Rule (public-company customers)

If Customer is a registrant subject to **17 C.F.R. §229.106 (Reg S-K Item 106)** and Form 8-K Item 1.05, Customer must disclose a material cybersecurity incident on 8-K within `4` business days of determining materiality. Vendor provides the factual record (timeline, data categories, containment, residual risk) supporting Customer's materiality assessment. `[VERIFY current rule text and the AG-endorsed national-security delay.]`

---

## 18. Insurance & remedies coordination

This section explains how Service Credits sit alongside Vendor's insurance program. Vendor maintains the insurance described in **CSA §17.4**, including (at minimum) Commercial General Liability ("**CGL**"), Privacy / Cyber Liability ("**Cyber**"), and (where required) Errors & Omissions ("**E&O**") and Crime coverage at CSA-specified limits. Vendor furnishes certificates of insurance ("**COIs**") on request and notifies Customer of material reduction or non-renewal.

Service Credits do not preclude, exhaust, or set off Customer's recovery under Vendor's Cyber policy or any other insurance for first-party losses suffered by Customer (e.g., forensic costs, notification costs, insurable regulatory fines, credit-monitoring, PR expense). Where insurance and a Service Credit address the same loss, Customer will not double-recover but may elect which remedy to pursue first.

**Customer perspective:** Align Customer Cyber retentions and clocks with Vendor's program. **Vendor perspective:** Insurance and credits address different risk layers and are additive.

---

## 19. Governing law & dispute resolution

This section says which law governs and how SLA disputes are resolved. This SLA is governed by **CSA §18** (US-variant default: State of Delaware, without regard to conflict-of-laws principles). SLA disputes follow the CSA mechanism, expected to be:

1. **Informal escalation.** Either Party may invoke `30`-day informal escalation by written notice to the other's designated business owner; the Parties meet at least once during the period.
2. **Mediation.** If unresolved, non-binding mediation under **{{Arbitration Provider}}** rules (default `AAA` Commercial Mediation; `JAMS` / `NAM` acceptable alternatives).
3. **Arbitration or court.** If unresolved within `60` days of demand, binding arbitration under **{{Arbitration Provider}}** rules (default `AAA` Commercial Arbitration), seated in **{{Arbitration Seat}}** (default `Wilmington, Delaware`), or to courts identified in CSA §18 if a court-litigation election is preserved.

Each Party waives class, collective, and representative actions to the maximum extent permitted by law. B2B class waivers are generally enforceable under the Federal Arbitration Act (`9 U.S.C. §§1–16`) and in state courts that follow that line of authority, subject to unconscionability review.

Nothing here prevents either Party from seeking emergency injunctive relief to protect IP, confidential information, or data-protection obligations.

---

## Annex A — Severity definitions

Severity matrix for §6; initially set by Customer, reclassifiable by Vendor with documented reasoning.

**P1 — Critical.** Service wholly unavailable for substantially all users; or a security incident affecting Customer Data is in progress; or Customer Data is at material risk of loss. No workaround. Examples: full production outage, active ransomware, mass authentication failure, regional outage in Customer's only licensed region.

**P2 — High.** A core function is impaired for a significant subset of users; a workaround exists but is materially burdensome. Examples: major API endpoint at `>25%` error rate, single-tenant outage, severe latency breaching §13 thresholds, partial write loss.

**P3 — Medium.** Non-core function impaired, or core function impaired for a small subset; reasonable workaround exists. Examples: minor UI defect, non-critical report failure, intermittent slowness within tolerances.

**P4 — Low.** Cosmetic issue, documentation request, feature request, or general inquiry. No business impact.

Reclassification: Vendor may reclassify when reproducible facts change impact (e.g., reported P1 contained to a single user with a workaround). Reclassification is documented in the ticket. Customer may dispute via §19 informal escalation.

---

## Annex B — Service Credit calculation worked examples

This annex shows how to compute credits under §7, using a `30`-day month (`43,200` total minutes).

**Worked example 1 — Single multi-hour outage.**
- Customer Monthly Service Fee: `$10,000`
- Total minutes: `43,200`; Excluded Downtime: `0`
- Downtime: one event of `4` hours `30` minutes = `270` minutes
- Uptime % = `(43,200 − 270) / 43,200 × 100` = `99.375%`
- `99.375%` falls in the `< 99.9% and ≥ 99.0%` band → `10%` credit
- Credit = `$10,000 × 10%` = **`$1,000`**

**Worked example 2 — Sustained chronic outage exceeding the cap.**
- Customer Monthly Service Fee: `$10,000`
- Downtime: `12` hours = `720` minutes
- Uptime % = `(43,200 − 720) / 43,200 × 100` ≈ `98.333%`
- `98.333%` falls in the `< 99.0% and ≥ 95.0%` band → `25%` credit
- Credit = `$10,000 × 25%` = **`$2,500`**

**Worked example 3 — Severe outage above the cap.**
- Customer Monthly Service Fee: `$10,000`
- Downtime: `48` hours = `2,880` minutes
- Uptime % = `(43,200 − 2,880) / 43,200 × 100` ≈ `93.333%`
- `93.333%` falls in the `< 95.0%` band → `30%` credit
- Cap (`{{Monthly Credit Cap}}` default `30%`) applies → **`$3,000`**

**Worked example 4 — Mixed Excluded Downtime.**
- Customer Monthly Service Fee: `$10,000`
- Downtime: `120` minutes (counted) + `60` minutes (Excluded — Scheduled Maintenance under §5(a))
- Uptime % = `((43,200 − 60) − 120) / (43,200 − 60) × 100` = `99.722%`
- `99.722%` falls in the `< 99.9% and ≥ 99.0%` band → `10%` credit
- Credit = **`$1,000`**

Customer must follow §8 within `30` days of month-end. Credits are issued under §9.

---

## Annex C — Sample monthly availability report

Non-binding template for §10 monthly reports.

**Service Availability Report — `[Service Name]` — `[Month YYYY]`**

- **Customer:** `[Customer Legal Name]`
- **Service / Region:** `[Service Name] / [us-east-1, us-west-2, ...]`
- **Reporting Period:** `[YYYY-MM-01 00:00 UTC] to [YYYY-MM-DD 23:59 UTC]`
- **Total Minutes in Period:** `[43,200]`
- **Excluded Downtime (minutes, by §5 category):** `(a) [n], (b) [n], (c) [n], ... (m) [n]`
- **Counted Downtime (minutes):** `[n]`
- **Uptime Percentage:** `[xx.xxx%]` (target `{{Uptime Percentage}}`)
- **Incident summary:**

| Incident ID | Start (UTC) | End (UTC) | Duration | Severity | Excluded? | Brief description |
|---|---|---|---|---|---|---|
| `INC-2026-0042` | `2026-MM-DD HH:MM` | `2026-MM-DD HH:MM` | `mm:ss` | P1 | No | Auth gateway 5xx errors |
| `INC-2026-0043` | `2026-MM-DD HH:MM` | `2026-MM-DD HH:MM` | `mm:ss` | P2 | No | Latency degradation in `us-east-1` |
| `INC-2026-0044` | `2026-MM-DD HH:MM` | `2026-MM-DD HH:MM` | `mm:ss` | — | Yes (§5(a)) | Scheduled Maintenance |

- **Support ticket compliance:**

| Severity | Tickets opened | P-target hits | P-target misses | Median initial response |
|---|---|---|---|---|
| P1 | `n` | `n` | `n` | `mm:ss` |
| P2 | `n` | `n` | `n` | `hh:mm` |
| P3 | `n` | `n` | `n` | `dd:hh` |
| P4 | `n` | `n` | `n` | `dd:hh` |

- **DR posture:** RTO target `{{RTO Hours}}`; RPO target `{{RPO Hours}}`; DR exercises performed in period: `[summary]`.
- **Service Credits owed (preliminary):** `$[n]` (`[band]` band; subject to §8 request).
- **Notes / forward-looking remediations:** `[free text]`.

---

## Merge fields used

The following Mustache merge fields appear in this template; defaults are listed where applicable.

- `{{Vendor Legal Name}}`
- `{{Customer Legal Name}}`
- `{{Uptime Percentage}}` — default `99.9%`
- `{{Monthly Credit Cap}}` — default `30%`
- `{{Support Time Zone}}` — default `US Eastern Time`
- `{{Measurement Time Zone}}` — default `Coordinated Universal Time (UTC)`
- `{{Termination Cure Period}}` — default `30 days`
- `{{Status Page URL}}`
- `{{SLO Documentation URL}}`
- `{{Support Portal URL}}`
- `{{P1 Pager Number}}`
- `{{Customer Notification Email}}`
- `{{Arbitration Provider}}` — default `AAA` (acceptable alternatives: `JAMS`, `NAM`)
- `{{Arbitration Seat}}` — default `Wilmington, Delaware`
- `{{NYDFS Notification Email}}` — for NYDFS Reg 500 Covered Entities
- `{{Forensic Vendor}}` — incident-response forensic vendor on retainer
- `{{RTO Hours}}` — default `4 hours`
- `{{RPO Hours}}` — default `1 hour`

---

## Authoritative references

Public-domain or permissively licensed sources referenced; inclusion is not endorsement, and drafters should verify currency.

- **NIST Cybersecurity Framework (CSF) 2.0** — https://www.nist.gov/cyberframework
- **NIST SP 800-61 Rev. 2, "Computer Security Incident Handling Guide"** — https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
- **NIST SP 800-34 Rev. 1, "Contingency Planning Guide for Federal Information Systems"** — https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final
- **CISA Incident Response Playbook (federal civilian executive branch)** — https://www.cisa.gov/
- **FTC, "Data Breach Response: A Guide for Business"** — https://www.ftc.gov/business-guidance
- **FTC Click-to-Cancel Rule, 16 C.F.R. Part 425** `[VERIFY current effective date and rule text]`
- **California Civil Code §1798.82 (data-breach notification)** — https://leginfo.legislature.ca.gov/
- **New York General Business Law §899-aa (SHIELD Act)** — https://www.dfs.ny.gov/
- **Texas Business & Commerce Code §521.053** — https://statutes.capitol.texas.gov/
- **Florida Statutes §501.171** — http://www.leg.state.fl.us/
- **Massachusetts General Laws ch. 93H and 201 CMR 17** — https://www.mass.gov/
- **Alabama Code §8-38-1 et seq.** — https://alison.legislature.state.al.us/
- **23 NYCRR Part 500 (NYDFS Cybersecurity Regulation)** — https://www.dfs.ny.gov/industry_guidance/cybersecurity
- **17 C.F.R. §229.106 / Form 8-K Item 1.05 (SEC Cybersecurity Disclosure Rule)** — https://www.sec.gov/
- **Texas SB 820 (87R) and Texas Education Code §11.175** — https://capitol.texas.gov/
- **Federal Arbitration Act, 9 U.S.C. §§1–16** — https://www.law.cornell.edu/uscode/
- **Bonterms Mutual Cloud Terms / SLA addenda** `[CC-BY-4.0]` — https://bonterms.com/
- **Common Paper Cloud Service Agreement (CSA) SLA exhibit** `[CC-BY-4.0]` — https://commonpaper.com/
- **GitHub open-source legal templates** `[CC0]` — https://github.com/github/site-policy

---

## Not legal advice

This template is a clean-room SLA drafting aid published under the MIT license. It is not legal advice, does not create an attorney-client relationship, and is not a substitute for review by qualified US counsel admitted in the relevant jurisdiction(s). Statutory and regulatory citations are illustrative; statutes are amended frequently, and several items are flagged `[VERIFY]`. Before relying on this template, the drafter should (a) confirm the current text of every cited statute and rule, (b) tailor carve-outs and merge-field defaults to the transaction, (c) reconcile this SLA with the CSA, DPA, any BAA, and any PCI-DSS Addendum, and (d) consider sector overlays (HIPAA, GLBA, FERPA, FISMA / FedRAMP, CJIS, ITAR / EAR) that may impose stricter requirements.
