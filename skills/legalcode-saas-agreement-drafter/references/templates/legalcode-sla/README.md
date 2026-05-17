# legalcode-sla

Source: skill-bundled template for `legalcode-saas-agreement-drafter`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

A modern Service Level Agreement (SLA). Designed to plug in as
**Exhibit B** of `legalcode-csa` (Cloud / SaaS Subscription Agreement)
or to stand alone for non-CSA engagements. Covers both **availability**
SLAs (uptime + service credits) and **support** SLAs (severity-based
response and resolution targets).

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral baseline (dual-perspective: customer / vendor / market-standard) | You operate in a jurisdiction not covered below, or you want the master before specialising. |
| `us.md` | US — state breach-notification + insurance defaults + arbitration | Either party is US-based; covers state-by-state breach notification timing influencing incident SLAs. |
| `eu.md` | EU/EEA — DORA + NIS2 + Cyber Resilience Act + Data Act incident reporting | Either party is EU/EEA-based. Includes German overlay (BfDI / BSI-KritisV cross-references). |
| `uk.md` | UK — NIS Regulations 2018 + NCSC Cyber Essentials + DUAA 2025 | Either party is UK-based. |
| `is.md` | Iceland — Persónuvernd 72-hour breach SLA + EEA-imported NIS2/DORA | Either party is Iceland-based. |

## How to use

1. Pick the file matching the controlling-law jurisdiction.
2. Decide your drafting posture — customer-side, vendor-side, or
   market-standard. The dual-perspective sections (§4 uptime tier, §5
   excluded downtime, §6 support targets, §7 credit cap, §11 RTO/RPO,
   §14 termination threshold) carry three labelled variants.
3. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
4. Pick uptime tier(s) for each in-scope service (production / sandbox /
   API / data-plane separately if needed). Common tiers: 99.5 / 99.9 /
   99.95 / 99.99.
5. Configure severity matrix in **Annex A**. Confirm response and
   resolution targets are operationally realistic for your team's
   on-call coverage.
6. Wire the credit-calculation formula in **Annex B** to your billing
   system; credits are issued automatically against the next invoice or
   on request per §8.
7. Have the resulting SLA reviewed by qualified counsel **and** the
   Vendor's Head of Engineering / SRE — an unenforceable SLA from a
   product standpoint is as bad as one with a legal defect.

## Canonical 16-section structure + 3 annexes

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. Definitions
3. Scope of services covered
4. Service Availability commitment
5. Excluded Downtime
6. Support response & resolution targets
7. Service Credits
8. Credit request procedure
9. Credit issuance & exclusivity as remedy
10. Performance reporting & status page
11. Disaster recovery & business continuity
12. Scheduled & emergency maintenance
13. Service degradation vs. outage
14. Material SLA breach & termination right
15. Changes to this SLA
16. Survival & order of precedence

**Annex A** — Severity matrix (P1 / P2 / P3 / P4 with response and
resolution targets)
**Annex B** — Service Credit calculation table (uptime tier × credit %)
**Annex C** — Sample monthly SLA report format

## Companion templates

- `legalcode-csa` — primary parent; this SLA attaches as Exhibit B
- `legalcode-order-form` — uptime tier may be set per-Order rather than
  per-CSA
- `legalcode-dpa` — incident notification timelines coordinate with the
  DPA's GDPR Art. 33 / state breach laws

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Vendor Legal Name}}        # full registered name of the SaaS provider
{{Vendor Short Name}}        # how the vendor is referred in prose
{{Customer Legal Name}}      # full registered name of the customer
{{Customer Short Name}}      # how the customer is referred in prose
{{Service Name}}             # the SaaS product
{{Service URL}}              # primary URL
{{Status Page URL}}          # public status / health page
{{Effective Date}}           # YYYY-MM-DD when SLA takes effect
{{Last Updated Date}}        # YYYY-MM-DD of last revision
{{Uptime Tier}}              # default uptime % (e.g., "99.9%")
{{Uptime Measurement Method}}# how uptime is measured ("synthetic monitoring at 1-minute intervals", etc.)
{{Maintenance Window}}       # default maintenance window ("Saturdays 02:00–06:00 UTC")
{{Maintenance Notice Window}}# advance notice of scheduled maintenance ("seven (7) days")
{{Emergency Notice Window}}  # advance notice of emergency maintenance ("two (2) hours where feasible")
{{Credit Cap Percent}}       # max service credits as % of monthly fees ("30%")
{{Credit Window Days}}       # days customer has to claim credit ("60 days")
{{Reporting Cadence}}        # uptime report cadence ("monthly")
{{P1 Response Target}}       # severity-1 first response ("15 minutes")
{{P1 Resolution Target}}     # severity-1 resolution / workaround ("4 hours")
{{P2 Response Target}}       # severity-2 first response ("1 hour")
{{P3 Response Target}}       # severity-3 first response ("4 business hours")
{{P4 Response Target}}       # severity-4 first response ("1 business day")
{{Support Hours}}            # 24×7 / business-hours / regional
{{Support Channels}}         # ticket / chat / phone / pager
{{RTO}}                      # recovery time objective ("4 hours")
{{RPO}}                      # recovery point objective ("1 hour")
{{Termination Threshold}}    # consecutive months below SLA before termination right ("3 consecutive months" or "any 3 of 6 months")
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- Bonterms SLA — CC-BY-4.0 (primary baseline)
- Common Paper CSA v2.1 (SLA exhibit pattern) — CC-BY-4.0
- GitHub `site-policy` — CC0 (clause-heading conventions)
- Mozilla legal templates — MPL-2.0 (regional-overlay pattern)
- Linux Foundation / Apache project SLAs — Apache-2.0 (operational-reporting patterns)
- ICO + NCSC + ENISA + EU/UK government cyber/incident guidance — Open Government Licence / public domain

**Blocked baselines (not consulted):** AWS SLAs, Microsoft Online Service
Level Agreement, Google Workspace SLA, Salesforce SLA, Atlassian SLAs,
Stripe SLAs, Cloudflare SLAs, OneDrive SLAs, and any other proprietary
or unspecified-license cloud/SaaS SLA templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Pick uptime tiers your team can actually operate. A 99.99% commitment
  permits 4.4 minutes of downtime per month. Don't commit to numbers
  you can't measure or maintain.
- Calibrate the **Excluded Downtime** list (§5) to your actual
  architecture — if you depend on a CDN, list it; if you have planned
  weekly maintenance, define the window.
- Configure the severity matrix (Annex A) with your support team's real
  on-call coverage. P1 with 15-minute response means a paged engineer
  24×7.
- Wire the credit formula (Annex B) to your billing system. Manual
  credit issuance scales poorly above 50 customers.
- Confirm the termination threshold (§14) is symmetric — Customer's
  ability to terminate for repeated SLA breach is a material right.
- Consider whether SLA should be a **service-credit-only** remedy
  (typical) vs. preserving damages for material breach (Customer-favored).
