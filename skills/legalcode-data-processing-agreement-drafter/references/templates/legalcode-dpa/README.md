# legalcode-dpa

Source: skill-bundled template for `legalcode-data-processing-agreement-drafter`
License: MIT (see LICENSE.md)
Maintainer: Fordæmi ehf. (Legalcode)
Last updated: 2026-04-28

## Documents

| File | Document Type | Use when |
|------|--------------|----------|
| `core.md` | Jurisdiction-neutral controller↔processor DPA | You operate in a jurisdiction not covered below, you want the dual-perspective master before specialising, or you are drafting a sub-processor flow-down. |
| `us.md` | US — CCPA/CPRA Service Provider Exhibit + multi-state | You target US business customers and need a CCPA service-provider/contractor addendum; typically attached to an MSA rather than a standalone DPA. |
| `eu.md` | EU/EEA — GDPR Art. 28 + DE-DSGVO + CH-FDPIC + SCCs Modules 1–4 | You process EU/EEA personal data, including Swiss data. Includes the SCCs annex builder for all four transfer modules. |
| `uk.md` | UK — UK GDPR + DPA 2018 + IDTA + UK Addendum | You target UK business customers post-Brexit. Includes both the standalone UK IDTA and the UK Addendum to the EU SCCs. |
| `is.md` | Iceland — Act 90/2018 (Persónuverndarlög) + EEA framing | You operate in Iceland or have Icelandic data subjects. EEA-framed transfer rules apply. |

## How to use

1. Pick the file matching the controller's primary jurisdiction (the EU
   variant covers EEA + DE + CH).
2. Decide your drafting posture: controller-favorable, processor-favorable,
   or market-standard compromise. Each clause flags the three positions
   where they materially diverge.
3. Search-and-replace every merge field (Mustache-style: `{{Field Name}}`).
4. Fill in **Annex 1** (description of processing), **Annex 2** (TOMs),
   **Annex 3** (sub-processor list), and **Annex 4** (transfer mechanism).
5. Have the resulting DPA reviewed by qualified counsel and your DPO
   before execution.
6. For sub-processor flow-down DPAs, start from `core.md` and use the
   "flow-down" subsection in §9 as the primary clause set.

## Canonical 19-section structure + 4 annexes

Every variant in this pack follows the same numbering:

1. Plain-language summary
2. Definitions
3. Subject matter, duration, nature & purpose of processing
4. Categories of data subjects and types of personal data
5. Roles & responsibilities
6. Documented processing instructions
7. Confidentiality of personnel
8. Security measures (TOMs)
9. Sub-processors (general/specific authorization + flow-down)
10. Data subject rights assistance
11. Assistance with controller compliance (DPIA, prior consultation, breach assistance)
12. Personal data breach notification
13. Records of processing (Art. 30)
14. International data transfers
15. Audits & inspections
16. Return or deletion on termination
17. Liability & indemnity
18. Governing law, jurisdiction, dispute resolution
19. Order of precedence & miscellaneous

**Annex 1** — Description of processing (Art. 28(3) particulars)
**Annex 2** — Technical and Organizational Measures (TOMs)
**Annex 3** — Sub-processor list
**Annex 4** — International transfer mechanism (jurisdiction-specific)

## Companion templates

- `legalcode-privacy-policy` — paired with this DPA's Art. 13/14 transparency obligations
- `legalcode-csa` — Cloud / SaaS Subscription Agreement; this DPA attaches as an exhibit
- `legalcode-msa` — Master Services Agreement; this DPA attaches as an exhibit
- `legalcode-cross-border-transfer-assessment` — companion skill for TIA / TRA

## Merge field convention

All variable inputs use Mustache-style `{{Field Name}}` placeholders. The
common merge fields across all variants:

```
{{Controller Legal Name}}        # controller's full registered name
{{Controller Short Name}}        # how the controller is referred in prose
{{Controller Address}}           # registered address
{{Controller Country}}           # for choice-of-law header
{{Controller Email Privacy}}     # privacy@…
{{Controller Email DPO}}         # OPTIONAL — DPO if appointed
{{Controller Representative}}    # OPTIONAL — Art. 27 GDPR rep / UK rep
{{Processor Legal Name}}         # processor's full registered name
{{Processor Short Name}}         # how the processor is referred in prose
{{Processor Address}}            # registered address
{{Processor Country}}            # for transfer determination
{{Processor Email Privacy}}      # privacy@…
{{Processor Email DPO}}          # OPTIONAL — DPO if appointed
{{Processor Representative}}     # OPTIONAL — Art. 27 GDPR rep / UK rep
{{Service Name}}                 # the service the processing supports
{{Service URL}}                  # primary URL
{{MSA Title}}                    # parent agreement this DPA attaches to
{{MSA Effective Date}}           # parent agreement effective date
{{Effective Date}}               # YYYY-MM-DD when DPA takes effect
{{Last Updated Date}}            # YYYY-MM-DD of last revision
{{Governing Law}}                # choice of law for the DPA
{{Subprocessor List URL}}        # public-facing subprocessor page
{{Notification Window}}          # sub-processor opposition window — typically "30 days"
{{Breach Notification SLA}}      # processor's notification window — typically "without undue delay and within 48 hours"
```

Each per-jurisdiction file lists any additional merge fields it requires
in a "Merge fields" section near the top of the document.

## Provenance

This template was assembled by clean-room drafting from the following
permissively-licensed reference points (no text was copied verbatim;
structure and clause-headings were used as drafting guides):

- Common Paper DPA v1.0 — CC-BY 4.0 (multi-regime cross-jurisdiction baseline)
- Common Paper Standard DPA — CC-BY 4.0 (controller↔processor structure)
- Bonterms DPA — CC-BY 4.0 (compromise/dual-perspective clause patterns)
- EU Commission Standard Contractual Clauses 2021/914 — Public domain
- ICO International Data Transfer Agreement (IDTA) — Open Government Licence (OGL)
- ICO International Data Transfer Addendum to EU SCCs — Open Government Licence (OGL)
- ICO Sample Processor Contract — Open Government Licence (OGL)
- GitHub `subprocessors.md` — CC0 1.0 (subprocessor-list pattern)
- oprvc DSGVO Mustertexte — CC0 1.0 (German-specific paragraph references)
- Mozilla MPL DPA references — MPL 2.0 (security/TOMs structure)

**Blocked baselines (not consulted):** TermsFeed, OneTrust, Iubenda,
SimplifyMyTerms, and any other unspecified-license or CC-BY-NC/CC-BY-ND/
CC-BY-SA DPA templates.

## Do NOT use as-is

This is a starting point, not the finished product. You must:

- Fill out Annex 1 with the actual subject matter, duration, nature, and
  purpose of processing for your specific engagement.
- Tailor Annex 2 (TOMs) to the specific security controls your processor
  has implemented and certified (ISO 27001, SOC 2, NIST 800-53, etc.).
- Maintain Annex 3 as a live, dated list of sub-processors with a
  notification mechanism (link to a published page that you update).
- Decide which transfer mechanism in Annex 4 actually applies to your
  flows (SCCs Modules 1–4, IDTA, UK Addendum, BCRs, derogations).
- For CCPA/CPRA: confirm the parties' relationship type — service
  provider, contractor, or third party — and the corresponding
  sale/sharing/cross-context behavioral advertising prohibitions.
- Confirm the dual-perspective drafting choice for §17 (liability) before
  execution. The neutral default is market-standard compromise; revise
  upward or downward depending on your bargaining position.
