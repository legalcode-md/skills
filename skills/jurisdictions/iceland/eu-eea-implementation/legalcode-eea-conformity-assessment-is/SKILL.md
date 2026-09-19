---
name: legalcode-eea-conformity-assessment-is
description: Run an ESA-style assessment of Icelandic implementation of an EU act incorporated into the
  EEA Agreement. Build or validate a provision-level samanburðartafla; retrieve the act, Joint Committee
  Decision, Icelandic measures, pre-law, guidance, and case law through Legalcode MCP; then separately
  test notification, transposition completeness, substantive conformity, State-attributable application,
  legal certainty, enforceability, institutions, sanctions, and remedies. Use for ministry self-review,
  Form 1 or correlation-table review, ESA correspondence or complaints, implementation bills, post-enactment
  audits, under-implementation, incorrect transposition, systemic bad application, and paired gold-plating
  review. Triggers on samraemisathugun, conformity check, samanburdartafla, EEA transposition, ESA implementation
  review, or whether Iceland correctly implemented or applies an EEA act.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode EEA Conformity Assessment — Iceland

> **Fyrirvari / Disclaimer:** Use this skill as an evidence-assembly and preliminary
> assessment framework, not as legal advice or an ESA decision. Require review by an
> Icelandic lawyer with EEA expertise before relying on a finding in legislation,
> litigation, an ESA submission, or advice to a client. Never invent a source, mapping,
> quotation, or legal consequence. Mark unresolved propositions `[VERIFY]`.

## Purpose and boundary

Determine, provision by provision, whether Iceland has achieved the legal result required
by an EEA-incorporated act. Test legal effect rather than textual similarity. Treat this as
the Icelandic, EFTA-pillar counterpart to `legalcode-eu-conformity-assessment` and the
substantive complement to `legalcode-anti-gold-plating-is`:

- **Conformity** asks whether sufficient national law delivers the correct legal result.
- **Application** asks whether State-attributable administration and enforcement apply it correctly.
- **Gold-plating** asks whether Iceland went beyond the EEA requirement.

Keep four assessment tracks separate throughout the work:

1. **notification** — what Iceland communicated to ESA and with what explanatory documents;
2. **transposition completeness** — whether every required legal result was implemented;
3. **substantive conformity** — whether the national rules deliver the correct legal result; and
4. **application** — whether State-attributable administration or enforcement applies those
   rules correctly in practice.

Never use success or failure on one track as a substitute for a finding on another.

Cover directives and the national-discretion or implementation provisions of regulations.
Do not assess an act until its EEA incorporation, Joint Committee Decision adaptations,
entry into force, and any constitutional reservation have been confirmed. Do not treat a
notification, correlation-table entry, explanatory memorandum, scoreboard status, or ESA
silence as proof of conformity.

This skill is self-contained but may invoke these sibling skills when their artifacts do
not exist:

| Need                             | Use                                      |
| -------------------------------- | ---------------------------------------- |
| Versioned obligation register    | `legalcode-eu-directive-analyzer`        |
| EEA incorporation and JCD status | `legalcode-eea-incorporation-tracker`    |
| Icelandic NIM inventory          | `legalcode-eu-transposition-tracker`     |
| Correlation table                | `legalcode-eu-correlation-table-builder` |
| EU/EEA substantive test          | `legalcode-eu-conformity-assessment`     |
| Over-implementation              | `legalcode-anti-gold-plating-is`         |

## Governing framework

Apply Article 7 EEA to distinguish regulations from directives and to test whether the
required result has been made part of Icelandic law. Apply the relevant EEA Annex,
Protocol 1, the incorporating Joint Committee Decision and its adaptations, Protocol 35,
Act No. 2/1993, the Surveillance and Court Agreement, and verified EFTA Court authority.
Use CJEU authority only after checking temporal relevance, textual correspondence,
homogeneity, and any EEA adaptation.

Apply this authority hierarchy and label the role of every verdict-driving source:

1. EEA Agreement, Protocols, relevant Annex, JCD and authentic incorporated act;
2. controlling or authoritative EFTA Court judgments as applicable, enacted Icelandic law,
   and authoritative Icelandic judgments;
3. ESA decisions, reasoned opinions and current enforcement positions;
4. CJEU authority relevant through homogeneity analysis;
5. Commission conformity methodology as a persuasive comparator only; and
6. preparatory works, guidance, commentary and other explanatory material.

When Iceland exercises an option, derogation or discretion, also test applicable primary EEA
law, proportionality, equal treatment, fundamental rights and free-movement constraints.

### EEA remedial firewall

Do not import EU-pillar direct-effect or `Marleasing` conclusions into Iceland unchanged.
For every defect, separate:

1. Iceland's international EEA implementation obligation;
2. the status and priority of the Icelandic implementing rule;
3. the available EEA-consistent interpretation under Icelandic law;
4. any Protocol 35 priority issue;
5. any possible State-liability or other remedy; and
6. whether an individual or undertaking can actually invoke the rule.

When national procedural rules govern enforcement, test both equivalence and effectiveness.

Never mark a defective Icelandic transposition “cured” merely because an EU directive
provision would satisfy an EU direct-effect test. Retrieve current EFTA Court authority
through Legalcode for the exact remedial proposition.

Read `references/assessment-method.md` before classifying any provision. Read
`references/legalcode-mcp-playbook.md` before source retrieval. Use
`assets/conformity-assessment-template-en.md` for an English report or
`assets/samraemisathugun-template.md` for an Icelandic report. Do not mix templates.

## Intake and clarification

Ask only questions that materially change the run. Gather in one batch when absent:

- EU act identifier and version; Icelandic act, regulation, or bill; target date.
- Purpose: ministry self-review, bill drafting, ESA response/complaint, client advice,
  litigation support, or academic analysis.
- Scope: all operative provisions, named articles, or triage followed by deep review.
- Output: Icelandic, English, or bilingual; Markdown only or Markdown plus JSON/CSV. Treat the
  selected language as a document-wide lock for every authored heading, table label, narrative,
  finding, matrix header, filename, and audit note. A bilingual output must use deliberately
  paired complete sections, not mixed-language headings and body text.
- Whether to run the paired gold-plating module.

For a request using “complete”, “full”, “comprehensive”, “end-to-end”, or
“heildstæð”, default to all operative provisions, English report language unless the user selects
Icelandic, a machine-readable matrix, pre-law trace for every material defect, and paired
gold-plating screening.

## Workflow

### 1. Open the matter and freeze scope

Create `samraemi-{matter-id}/` with `sources/`, `evidence/`, `matrix/`, `findings/`, `audit/`,
and `deliverables/`. Record the act version, assessment date, target legal date, purpose,
assumptions, exclusions, and user decisions. Preserve source files; never overwrite raw
evidence with normalized text.

### 2. Confirm EEA applicability first

Verify the complete act family: base act, delegated and implementing acts needed for the
required result, amendments, corrigenda, recasts, repeals, annexes and binding standards
incorporated by reference. Then verify EEA relevance, JCD number and date, Annex or Protocol,
adaptations, entry into force, transposition deadline, Article 103 constitutional-notification
status, provisional application, and any Article 102 suspension. Assign one applicability state
for the target date before any conformity verdict:

| Applicability state                      | Consequence                                                                                                                                                                 |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NOT_INCORPORATED`                       | No Icelandic EEA implementation duty under this act yet.                                                                                                                    |
| `INCORPORATED_NOT_EFFECTIVE`             | JCD exists but was not in force on the target date.                                                                                                                         |
| `CONSTITUTIONAL_PENDING_PRE_PROVISIONAL` | Article 103 requirements remain unresolved and the six-month provisional-application point has not been reached; run readiness review unless the JCD supplies another rule. |
| `CONSTITUTIONAL_PENDING_PROVISIONAL`     | Article 103 requirements remain unresolved, but the JCD applies provisionally; assess from the provisional-application date.                                                |
| `CONSTITUTIONAL_PENDING_NO_PROVISIONAL`  | Requirements remain unresolved and a Party has notified that provisional application cannot occur; run readiness review only.                                               |
| `RELEVANT_EEA_PART_SUSPENDED`            | The relevant Annex/Protocol part was suspended under Article 102 on the target date; state the precise scope and temporal effect.                                           |
| `EFFECTIVE_DEADLINE_PENDING`             | Run a readiness review, not a breach verdict.                                                                                                                               |
| `EFFECTIVE_DEADLINE_PASSED`              | Run the full current or historical conformity assessment.                                                                                                                   |
| `OUT_OF_SCOPE`                           | The provision does not apply to Iceland as adapted.                                                                                                                         |

Do not issue a current-breach verdict for `NOT_INCORPORATED`, `INCORPORATED_NOT_EFFECTIVE`,
`CONSTITUTIONAL_PENDING_PRE_PROVISIONAL`, `CONSTITUTIONAL_PENDING_NO_PROVISIONAL`, or
`RELEVANT_EEA_PART_SUSPENDED`. A provisionally
applicable JCD is not exempt from assessment merely because constitutional requirements remain
pending. Do not use the unadapted EU text as the only baseline. For regulations, test
incorporation “as such”, JCD adaptations, and only the national measures required or permitted;
do not run directive-style transposition analysis over provisions needing no domestic measure.

### 3. Assemble a source manifest through Legalcode MCP

Use the configured Legalcode MCP connector and the iterative workflow in
`references/legalcode-mcp-playbook.md`. Keep retrieval separate from legal assessment. Require
an evidence package containing exact internal `sourceRef`, source type, jurisdiction, official URL,
authority role, citation, fetched status, short excerpt, confidence, gaps, and strongest answer
basis. Retrieve at minimum:

- incorporated EU/EEA act and authentic Icelandic text where available;
- JCD and adaptations;
- every Form 1 notification, including earlier partial notifications, and the ESA implementation
  status record for the target date;
- every notified national implementing measure, its full title, English title or abbreviation,
  official link, promulgation date, effective date and notified role;
- consolidated Icelandic act plus regulations and commencement provisions;
- original bill, greinargerð, article notes, samanburðartafla, committee materials, amendments,
  opinions, consultation drafts, and relevant debates;
- Icelandic administrative guidance and implementing practice;
- ESA decisions or correspondence and EFTA Court/CJEU authority relevant to the legal test.

Use exact identifier search before keywords. Fetch every verdict-driving source. Log gaps;
never silently replace missing Icelandic or EEA text with an English summary.

### 4. Build the obligation register

Split the controlling EEA act below article level whenever one provision contains multiple
legal propositions. Assign a stable ID and record:

- deontic operator, addressee, beneficiary, required result, trigger, deadline, exception;
- definition and recital dependencies;
- delegated or implementing acts, annexes, corrigenda, recasts, repeals and incorporated
  standards necessary to give the proposition its current meaning;
- minimum, maximum, or mixed harmonisation;
- State option, derogation, reporting/cooperation duty, or institutional obligation;
- JCD adaptation and Iceland-specific effect;
- whether the obligation is capable of affecting rights, duties, remedies, sanctions, or
  practical access.

Do not omit provisions merely because they address the State, ESA, reporting, competent
authorities, institutional design, or inter-agency cooperation.

### 5. Build or validate the samanburðartafla

Map every obligation ID to all relevant Icelandic provisions. Allow 1:1, 1:N, N:1, existing
general framework, administrative measure, option not exercised, no separate measure
required, and no mapping. For every internal cell, include exact national text, pinpoint
citation, internal `sourceRef`, official URL, effective date, English translation where needed,
Form 1 provenance, Iceland's explanation or no-measure rationale, mapping rationale, and
unresolved dependencies. Keep `sourceRef` in the internal evidence ledger; use official
citations and URLs in the lawyer-facing report.

Also run the reverse map from each identified Icelandic implementation provision back to a
directive obligation. Send unmatched national provisions to the gold-plating screen; do not
assume every unmatched provision is unlawful.

### 6. Run four separate assessment tracks

Assign one state on every applicable track for each obligation. Do not collapse them into a
single verdict.

| Track                      | States                                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Notification               | `NOT_NOTIFIED`, `PARTIALLY_NOTIFIED`, `NOTIFIED_INADEQUATE_EXPLANATION`, `FULLY_NOTIFIED`, `NOT_APPLICABLE`, `NOT_ASSESSABLE`                    |
| Transposition completeness | `COMPLETE`, `PARTIAL_TRANSPOSITION`, `NOT_TRANSPOSED`, `EMPTY_SHELL`, `NO_SPECIFIC_MEASURE_REQUIRED`, `NOT_APPLICABLE`, `NOT_ASSESSABLE`         |
| Substantive conformity     | `CONFORMING`, `PARTIALLY_CONFORMING`, `INCORRECTLY_IMPLEMENTED`, `NOT_APPLICABLE`, `NOT_ASSESSABLE`                                              |
| Application                | `NOT_ASSESSED`, `NO_BAD_APPLICATION_IDENTIFIED`, `ISOLATED_APPLICATION_INCIDENT`, `SYSTEMIC_BAD_APPLICATION`, `NOT_APPLICABLE`, `NOT_ASSESSABLE` |

Treat a bare notification without the measure or a sufficiently precise link as a notification
defect. Assign `EMPTY_SHELL` where a national measure merely authorizes or promises a future
rule, methodology, institution or procedure but does not itself deliver the required result.
Classify separately timed reporting, action-plan, facility-creation and operational duties on
the application track unless the act makes their establishment part of transposition itself.

### 7. Run the substantive correspondence test

Apply the ten correspondence tests in `references/assessment-method.md` on their proper tracks:
use applicability as the gate, completeness on the transposition track, and the remaining tests
for substantive conformity and practical enforceability. Compare the combined legal effect of all
mapped measures, not isolated sentences.

Do not treat a broader national definition as non-conforming merely because it is broader.
Identify the resulting legal consequence and test whether the extension changes the required
result, creates material uncertainty or confusion, discriminates, or impedes EEA rights.
For open norms or administrative discretion, retrieve authoritative judicial or administrative
interpretations and test whether application is sufficiently stable and consistent.

For “general law is sufficient” or “no measure required”, require a written justification
identifying the rule, its binding quality, accessibility, stable application, enforcement path,
and absence of a conflicting special rule. Administrative practice alone cannot replace a
binding norm when the EEA obligation requires enforceable rights or duties.

### 8. Classify and remediate

Keep all four track states separate from applicability, implementation basis, practical
severity, evidence status, confidence and remediation. A complete but incorrectly transposed
rule is `COMPLETE` on transposition and `INCORRECTLY_IMPLEMENTED` on conformity. A conforming
rule can still have `SYSTEMIC_BAD_APPLICATION`. An isolated private or administrative incident
does not change the substantive-conformity verdict.

Assign severity separately:

- **CRITICAL** — removes or materially defeats a right, duty, remedy, supervision function,
  or market-access condition; creates immediate ESA or systemic exposure.
- **HIGH** — material scope, enforcement, sanction, institutional, or recurring operational gap.
- **MEDIUM** — remediable ambiguity, incomplete procedure, or limited class/time-period gap.
- **LOW** — technical, documentary, or low-impact defect that still warrants correction.

For each defect or not-assessable finding on any track, state the exact amendment, regulation,
administrative action, guidance, notification correction, evidence request, or lawyer decision needed. Do not offer
guidance as the cure where legislation or binding secondary rules are necessary.

### 9. Trace causation and practical operation

Use `legalcode_trace` through Legalcode MCP to identify when and why the defect entered the
Icelandic measure. Check bill text, article notes, consultation drafts, opinions, committee
changes, floor amendments, regulations, commencement, and later amendments. Identify the
actor and whether the correlation table disclosed the issue.

Then test real usability: competent authority, procedure, standing, deadlines, forms, fees,
appeal/review, sanctions, resources, data flows, and whether affected persons can rely on the
rule. Mark any conclusion based only on legislative history as untested in practice.

Before assigning an application defect, identify the attributable State actor and distinguish a
private breach, an isolated official error, an authoritative administrative interpretation, and
a repeated or systemic State practice. Record frequency, consistency, duration, affected class,
supervisory response, final national decisions and available remedies. Do not infer systemic bad
application from one unresolved complaint.

### 10. Apply the ESA procedural lens when relevant

For an ESA response, complaint or enforcement-risk assessment, record the applicable stage:
pre-complaint or information request, complaint screening, letter of formal notice, reasoned
opinion, or possible Article 31 SCA referral. Record attribution to an EEA EFTA State, response
deadline, requested evidence, national remedies, and ESA's enforcement discretion. Treat ESA's
burden to establish a failure separately from Iceland's duty to cooperate and substantively
answer sufficiently supported evidence. Never present the skill's finding as an ESA decision.

### 11. Challenge material findings

For every CRITICAL or HIGH finding, run three passes:

1. **Legal-chain pass:** Does fetched authority support every link from EEA obligation to
   Icelandic defect and consequence?
2. **Completeness pass:** Did the review miss a regulation, general rule, JCD adaptation,
   transitional provision, case, or administrative mechanism?
3. **Hostile pass:** State the strongest conformity and operational-equivalence argument.
   Explain why it succeeds, fails, or requires human resolution.

For an ESA-facing finding, add an evidence-burden pass: identify what proves the alleged failure,
what remains inference, what rebuttal Iceland has supplied, and whether the record supports more
than a presumption.

Record the original verdict, challenge, revised verdict, and reviewer gate. A material finding
cannot be final while its strongest counterargument remains unanswered.

### 12. Verify, deliver, and hand off

Run the five citation gates: authoritative source, exact pinpoint and quotation, currency,
EEA/Iceland domain fit, and confidence. Re-fetch at least every CRITICAL/HIGH authority and a
sample of lower-severity rows. Confirm that row counts reconcile across the obligation register,
matrix, findings, and executive summary.

Run a separate language-consistency gate over every authored deliverable before delivery:

1. confirm the selected output language in the matter scope and internal audit record;
2. confirm the matching report template was used;
3. scan every heading, table header, filename, narrative paragraph, finding label, matrix column,
   unresolved-item list, and audit note for unintended language switching;
4. permit source-language text only for exact quotations, official names/titles, party names,
   search queries, and citations, clearly identified as such; and
5. fail delivery and revise the artifacts if a heading/table language differs from its body or if
   an English-only/Icelandic-only run contains untranslated authored labels.

For filesystem-backed runs, execute the deterministic language gate before delivery:

```bash
node skills/jurisdictions/iceland/compliance/legalcode-eea-conformity-assessment-is/scripts/check-output-language.mjs \
  --language en \
  --root <matter-directory>
```

Use `--language is` for an Icelandic run. The checker excludes preserved raw sources but scans all
authored Markdown, CSV, YAML, and JSON artifacts and rejects template-label or filename mixing.

Run the report-boundary gate against the lawyer-facing report:

```bash
node skills/jurisdictions/iceland/compliance/legalcode-eea-conformity-assessment-is/scripts/check-report-boundary.mjs \
  --report <matter-directory>/deliverables/conformity-assessment-report.md
```

Fail delivery if the report contains an internal-artifact link or reference, audit terminology,
MCP or repository defect material, internal source identifiers, or local workflow paths.

Deliver the lawyer-facing report without references to local support files, internal audit data,
MCP defects, repository issues, or approval plumbing. Keep the full matrix, source manifest, and
unresolved-evidence register as separately identifiable supporting materials. Always create the
machine-readable internal audit record under `audit/`. Create a human-readable audit appendix
under `audit/` when the user requests one; never append it to, link it from, or mention it in the
lawyer-facing report. Ensure the report and audit appendix can be shared independently.
Offer the paired `legalcode-anti-gold-plating-is` run for national provisions with no EEA
counterpart and the general `legalcode-eu-conformity-assessment` for EU-pillar comparison.

## Confidence and human gates

| Level        | Score     | Required action                                                                 |
| ------------ | --------- | ------------------------------------------------------------------------------- |
| Definite     | 0.95–1.00 | State plainly; preserve source chain.                                           |
| High         | 0.80–0.94 | State with any narrow caveat.                                                   |
| Probable     | 0.60–0.79 | Explain competing indicators; lawyer review.                                    |
| Possible     | 0.40–0.59 | Use `NOT_ASSESSABLE` or a clearly provisional readiness view; request evidence. |
| Insufficient | 0.00–0.39 | Do not assert a conformity verdict.                                             |

Require explicit human approval before: sending an ESA communication; publishing a ministry
position; filing in court; finalizing a bill; or converting a `NOT_ASSESSABLE`, `Possible`, or
`Insufficient` row into a definitive verdict.

## Internal audit record and optional audit appendix

Treat the audit record as internal workflow metadata, not as legal analysis and not as a report
section. Always create the machine-readable record in `audit/internal-audit-record.yaml`. Use the
plain label **internal audit record**; do not use unexplained product jargon in user-facing
material.

When the user requests an audit appendix, create `audit/audit-appendix.md` as a separate document.
Include scope decisions, source coverage, unresolved evidence, verification results, challenge
history, human gates, and relevant MCP or repository defects. Clearly label the appendix
`Internal — Audit Appendix`. Do not include it in `deliverables/`, and do not reference it from the
legal report. Keep product defects and GitHub issue links in the audit appendix or findings area,
never in the legal report.

```yaml
internal_audit:
  visibility: internal_only
  skill: legalcode-eea-conformity-assessment-is
  matter_id: "[id]"
  assessed_at: "[ISO-8601]"
  target_date: "[date]"
  output_language: "[English/Icelandic/bilingual]"
  report_template: "[path]"
  language_consistency_check: "[passed/failed]"
  eu_act: "[CELEX/ELI]"
  jcd: "[number/date]"
  eea_annex_protocol: "[location]"
  icelandic_measures: ["[law/regulation/sourceRef]"]
  legalcode_mcp: "[connected/not connected]"
  evidence_packages: ["[path]"]
  obligations_total: 0
  applicability_state: "[state]"
  notification_tally:
    {
      not_notified: 0,
      partially_notified: 0,
      notified_inadequate_explanation: 0,
      fully_notified: 0,
      not_applicable: 0,
      not_assessable: 0,
    }
  transposition_tally:
    {
      complete: 0,
      partial_transposition: 0,
      not_transposed: 0,
      empty_shell: 0,
      no_specific_measure_required: 0,
      not_applicable: 0,
      not_assessable: 0,
    }
  conformity_tally:
    {
      conforming: 0,
      partially_conforming: 0,
      incorrectly_implemented: 0,
      not_applicable: 0,
      not_assessable: 0,
    }
  application_tally:
    {
      not_assessed: 0,
      no_bad_application_identified: 0,
      isolated_application_incident: 0,
      systemic_bad_application: 0,
      not_applicable: 0,
      not_assessable: 0,
    }
  severity_tally: { critical: 0, high: 0, medium: 0, low: 0 }
  fetched_verdict_sources: "0/0"
  forms_1_reviewed: []
  esa_procedural_stage: "[not relevant/stage]"
  state_attribution_findings: []
  paired_gold_plating_run: false
  changed_after_challenge: []
  assumptions: []
  gaps: []
  human_decisions: []
```

## Anti-patterns

Never:

1. treat notification or a completed table as substantive conformity;
2. compare only EUR-Lex English when an authentic Icelandic EEA text controls;
3. skip the JCD, adaptations, Protocol 1, entry into force, or target date;
4. copy EU direct-effect analysis into the EEA-EFTA pillar;
5. treat conforming interpretation, Protocol 35, or State liability as curing defective implementation;
6. equate verbatim wording with equivalent legal effect;
7. accept “general law suffices” without a binding-rule and enforceability demonstration;
8. omit State-only, reporting, authority-design, or inter-agency duties;
9. ignore regulations, commencement rules, transitional provisions, or later amendments;
10. infer `NOT_TRANSPOSED` from a search miss;
11. use an unfetched search snippet as verdict evidence;
12. let recitals create a free-standing obligation absent operative-text support;
13. confuse under-implementation with gold-plating;
14. treat ESA silence or scoreboard status as approval;
15. issue a CRITICAL/HIGH finding without hostile review;
16. report a percentage while unresolved obligations are hidden from its denominator;
17. bury uncertainty in prose instead of using `NOT_ASSESSABLE` and confidence;
18. expose internal MCP/tool chatter in the lawyer-facing report;
19. treat a Form 1 notification or explanatory document as proof of completeness or conformity;
20. combine notification, transposition, conformity and application into one verdict;
21. treat a private breach or isolated official error as systemic State-attributable application;
22. ignore provisional application under Article 103 or suspension under Article 102;
23. presume a broader national definition is defective without identifying a legal or practical harm;
24. classify a future delegation or promised measure as completed transposition; or
25. rely on a source without labelling whether it is binding, an enforcement position,
    persuasive methodology, or explanatory material; or
26. mix authored headings, table labels, filenames, or audit fields from one language with body
    text in another, except for clearly identified official names, quotations, and citations; or
27. expose or link the internal audit record, audit appendix, unresolved-evidence register, MCP
    defect log, GitHub issues, local paths, source references, or approval plumbing in the
    lawyer-facing report unless the user expressly requests a combined audit bundle.

## Writing and output standards

Default to professional English legal prose. If the user selects Icelandic, use professional
Icelandic legal prose throughout instead. Never combine headings or table labels in one language
with narrative content in another. Preserve official names, untranslated source titles, exact
quotations, party names, and EU/EEA identifiers in their authoritative form; add a translation in
parentheses only where it aids comprehension. Lead with the result and consequence. Use one
obligation per row and one finding ID per defect. Quote sparingly and exactly. Distinguish facts,
source statements, legal assessment, inference, and recommended action.

Produce at minimum:

1. executive summary and scope;
2. EEA applicability and source manifest;
3. Form 1/notification review and national-measures inventory;
4. obligation register;
5. a provision-by-provision conformity matrix showing all four track states;
6. findings with severity, confidence, counterargument, and remediation;
7. practical-enforceability, State-attribution and institutional analysis;
8. ESA procedural analysis when relevant;
9. unresolved evidence and its substantive effect, stated directly in the report rather than by
   linking an internal register; and
10. a curated primary-authorities list with official links and exact pinpoints.

Create separately from the report:

1. a machine-readable internal audit record under `audit/`; and
2. when requested, a human-readable audit appendix under `audit/`.

Never number either audit artifact as a report section. Never use the report to direct the reader
to internal files. Keep operational debugging and product-remediation tasks out of the legal
remediation plan.

For English output, use English filenames such as `conformity-assessment-report.md` and
`conformity-matrix.csv`. For Icelandic output, use Icelandic filenames consistently. Do not use an
Icelandic filename for an English deliverable or vice versa.

## External tool integration and degradation

Use the configured Legalcode MCP Pro connector as the primary legal retrieval surface. Follow
the repository's iterative Legalcode search pattern directly; do not shell out to another
model CLI. Call `legalcode_discover` before unfamiliar searches, use `legalcode_search`
for ranked or exact retrieval, `legalcode_fetch` before reliance, `legalcode_trace` for
deterministic relations, and `legalcode_analyze` only for aggregate coverage questions.

If MCP is unavailable, proceed only with user-supplied or independently verified official
primary materials. Set `legalcode_mcp: not connected` and record the retrieval path. Base
confidence on authority coverage, authenticity, currency and pinpoint verification—not connector
availability alone. Mark missing controlling authority `[VERIFY]` and keep only affected rows
`NOT_ASSESSABLE`. Do not silently substitute general web commentary for missing controlling text.

## Provenance

Created by Legalcode on 2026-07-21 as an Icelandic EEA-EFTA specialization of
`legalcode-eu-conformity-assessment`, `legalcode-eu-correlation-table-builder`,
`legalcode-eea-incorporation-tracker`, and `legalcode-anti-gold-plating-is`. The workflow is
informed by the ESA-style conformity process described in Valdimar Hjartarson,
“Samræmisathuganir Eftirlitsstofnunar EFTA”, and must be updated when verified EFTA Court,
ESA, EEA, or Icelandic authority changes the governing test.
