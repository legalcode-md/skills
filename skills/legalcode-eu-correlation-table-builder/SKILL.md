---
name: legalcode-eu-correlation-table-builder
description: Generates the Commission-required two-column correlation table that every Member State must
  submit alongside its transposition notification under Art. 288 TFEU and the Joint Political Declarations
  of 28 September 2011 (OJ C 369, 17.12.2011, p. 14) and 27 October 2011 (OJ C 369, 17.12.2011, p. 15)
  on explanatory documents.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generates the Commission-required two-column correlation table that every Member State must submit alongside its transposition notification under Art. 288 TFEU and the Joint Political Declarations of 28 September 2011 (OJ C 369, 17.12.2011, p. 14) and 27 October 2011 (OJ C 369, 17.12.2011, p. 15) on explanatory documents. Maps each operative provision of an EU directive — for example, NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022, p. 80), CSRD Directive (EU) 2022/2464 (CELEX 32022L2464), CSDDD Directive (EU) 2024/1760 (CELEX 32024L1760), or the Whistleblower Protection Directive 2019/1937 — to the corresponding provision(s) in a Member State's National Implementing Measure (NIM). Supports two operating modes: (1) populated table for actual transposition notification, and (2) blank scaffold mode used during drafting to plan the article-by-article mapping before the NIM is finalised. Identifies coverage gaps (directive obligations with no NIM counterpart — feed to `legalcode-eu-conformity-assessment`) and over-coverage rows (NIM provisions with no directive counterpart — feed to `legalcode-eu-gold-plating-detector`). Produces Markdown human-review tables, JSON schema, AKN4EU XML stubs (`<doc class="correlationTable">`), and LegalRuleML satisfaction assertions, plus a Glass Box audit trail with per-cell provenance. Operates under TFEU Art. 260(3) — failure to notify transposition of a legislative directive triggers first-referral penalties (first applied in *Commission v Belgium*, Case C-543/17, ECLI:EU:C:2019:573). Serves four personas: government / EU institution (dominant — they submit the table), legal firms preparing client comparative briefings, companies tracing obligations through the NIM, and trade federations. EU-27 plus EEA EFTA (IS, NO, LI) jurisdictional scope.


# Legalcode EU Correlation Table Builder

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of the
> Commission-format two-column correlation table required for transposition notification
> of EU directives. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs should be reviewed by qualified legal counsel
> licensed in the relevant jurisdictions before use. This skill does not replace formal
> legal review by qualified EU and Member State counsel. It produces a structured
> framework to support a human-led review — not a substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and Member State
> implementing measures must be verified against authoritative sources (EUR-Lex, CURIA,
> national official journals) before use in regulatory submissions, infringement
> proceedings, or board reporting. EU law evolves continuously; transposition status,
> infringement procedures, and consolidated text versions change frequently. The 24
> official EU language versions of every act are equally authentic; reconcile divergent
> versions before relying on any single language for a definitive interpretation
> (CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95).

## Purpose and Scope

A correlation table (sometimes called "transposition table", "concordance table",
"tableau de correspondance" in French, or "Entsprechungstabelle" in German) is the
single artefact every Member State must submit to the Commission alongside its
transposition notification of an EU directive. The Commission relies on this table to
run the completeness and conformity checks that determine whether transposition is
"on time and correct" — the trigger conditions for an Art. 258 TFEU infringement
procedure, and (since Lisbon) for the first-referral pecuniary penalty under Art.
260(3) TFEU when a Member State has failed to notify transposition of a legislative
directive (first applied in _Commission v Belgium_, Case C-543/17,
ECLI:EU:C:2019:573).

The legal basis of the correlation table requirement is the joint political declarations
of 28 September 2011 (Member States and Commission) and 27 October 2011 (European
Parliament, Council and Commission) on explanatory documents (OJ C 369, 17.12.2011, pp.
14 and 15). Every directive adopted since 1 November 2011 carries a transposition
recital that re-states the political commitment of Member States to provide an
explanatory document, "which may take the form of a correlation table or other
documents serving the same purpose", whenever this is justified.

This skill builds correlation tables in the Commission two-column format, supports
either populated (post-drafting notification) or scaffold (pre-drafting planning) mode,
and emits the table in four standards-based representations (Markdown, JSON, AKN4EU,
LegalRuleML) with a deterministic Glass Box audit trail.

**Covers:**

- Population of the Commission two-column format (left: directive article; right: NIM
  provision) at article-paragraph-subparagraph granularity
- Blank scaffold mode for ministries planning a transposition before the NIM is drafted
- Mapping pattern classification (1-to-1, 1-to-N, N-to-1, partial, deferred, no
  transposition required)
- Coverage-gap identification (directive operative provisions with no NIM mapping)
- Over-coverage detection (NIM provisions with no directive counterpart — gold-plating
  signal handed to `legalcode-eu-gold-plating-detector`)
- Schema validation (every directive operative article appears exactly once; every
  mapping cell has provenance and a justification field)
- Multilingual rendering — directive text in the procedural language of the notification
  - at least one official Union language
- Ingestion of upstream artefacts: the obligation register from
  `legalcode-eu-directive-analyzer`, and the per-MS NIM citation from
  `legalcode-eu-transposition-tracker`
- Emission of standards-based outputs: AKN4EU `<doc class="correlationTable">`,
  LegalRuleML satisfaction assertions, JSON correlation schema, Markdown human review
- Glass Box audit trail — per-cell provenance (who/when/source), language version
  reconciliation log, mapping-pattern reasoning trace

**Does not:**

- Reach a conformity verdict (correct / partial / incorrect / not transposed) — that is
  the job of `legalcode-eu-conformity-assessment`, which consumes this table as input
- Categorise gold-plating findings against the published HLG (2014) /
  UK BIS (2013) / CFA Society Poland (2024) typologies — that is the job of
  `legalcode-eu-gold-plating-detector`
- Track the EEA Joint Committee Decision incorporation pipeline — see
  `legalcode-eea-incorporation-tracker` for IS / NO / LI
- Maintain TFEU 258 / 260 procedural timelines — see
  `legalcode-eu-infringement-procedure-tracker`
- Translate or certify NIM text — language reconciliation is for analysis only;
  authoritative translations are produced by national official journals and the EU
  Publications Office
- Provide legal advice on transposition correctness — every CRITICAL or HIGH coverage
  gap and every over-coverage flag must be reviewed by qualified counsel in the
  Member State concerned before regulatory submission

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes /
produces the following artefacts:

- **Consumes**: obligation register (versioned, per-article) from
  `legalcode-eu-directive-analyzer`; per-MS NIM citation and transposition status
  metadata from `legalcode-eu-transposition-tracker`.
- **Produces**: populated or scaffold correlation table (Commission two-column format)
  in Markdown, JSON, AKN4EU, and LegalRuleML; coverage-gap list (input to
  `legalcode-eu-conformity-assessment`); over-coverage flag list (input to
  `legalcode-eu-gold-plating-detector`).

Sibling skills (use whichever is appropriate for the user's stage in the lifecycle):

- `legalcode-eu-directive-analyzer` — extracts the obligation register from a directive
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix
- `legalcode-eu-correlation-table-builder` — directive-to-NIM correlation table (this skill)
- `legalcode-eu-conformity-assessment` — per-article transposition verdict
- `legalcode-eu-gold-plating-detector` — flags national over-implementation
- `legalcode-eea-incorporation-tracker` — EEA Joint Committee Decision tracking
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 procedure timeline

The shared EU legislative-data reference pack (CELEX/ELI/ECLI conventions, AKN4EU
schema notes, language regime, transposition recital library, JPD 2011 references)
lives co-located with the foundation skill. See
[shared EU legislative-data pack](references/eu-legislative-data/).

---

## Jurisdiction and Governing Law

The correlation table requirement applies across all 27 EU Member States. In the EEA
EFTA pillar (Iceland, Norway, Liechtenstein), the analogous artefact is the
notification of national implementing measures to the EFTA Surveillance Authority
under Art. 7 EEA and the Protocol 1 adaptations, with constitutional reservations
managed via Art. 103 EEA. Use this skill for both EU-27 and EEA EFTA notifications,
adjusting the destination institution (Commission DG vs. ESA Internal Market Affairs)
accordingly.

[JURISDICTION-SPECIFIC: EU-27] The correlation table is submitted via the Commission's
Member State Notification (MNE) workflow. Format: DOCX template per directive (each DG
publishes its own variant — DG CONNECT for NIS2, DG FISMA for DORA, DG ENV for
sustainability files). Underlying legal basis: TFEU Art. 288 (binding result of
directives), TFEU Art. 4(3) (sincere cooperation), and the Joint Political
Declarations of 28 September 2011 and 27 October 2011 on explanatory documents.
Failure to notify a complete table for a legislative directive engages Art. 260(3)
TFEU on first referral.

[JURISDICTION-SPECIFIC: EEA EFTA — Iceland, Norway, Liechtenstein] After the directive
is incorporated into an EEA Annex by Joint Committee Decision (Art. 102 EEA), each
EEA EFTA State notifies its NIM to ESA. Constitutional reservations (Art. 103 EEA)
suspend obligations until the relevant national parliamentary approval is given —
Storting (NO), Althingi (IS), Landtag (LI). Use this skill to build the correlation
table that accompanies the ESA notification under Art. 31 SCA monitoring. The
Commission DG channels do not apply.

[JURISDICTION-SPECIFIC: United Kingdom] Out of scope post-Brexit for new EU
directives. For retained EU law preserved by the European Union (Withdrawal) Act 2018
(as amended by REUL 2023), correlation analysis is not required as a notification
artefact but may be useful internally for retained-law audits. Mark all outputs
"[NOT APPLICABLE — UK third country since 1 February 2020 transition exit, 1 January
2021 implementation period exit]".

[JURISDICTION-SPECIFIC: Switzerland] Out of scope. Switzerland is not bound by the
acquis through EEA. Bilateral agreement implementing measures follow their own
notification regime and do not use the Commission correlation-table format.

The Member State language used in the table:

- The right-hand column (NIM) is rendered in the official language of the NIM as
  published in the national official journal.
- The left-hand column (directive) must use at least the procedural language of the
  notification (typically English), with the option of a parallel column in the
  national language. The 24 EU language versions are equally authentic (Reg. 1/1958;
  _CILFIT_ C-283/81 ECLI:EU:C:1982:335; _Codan_ C-236/97 ECLI:EU:C:1998:208;
  _EMU Tabac_ C-296/95 ECLI:EU:C:1998:152). Reconcile divergent versions before fixing
  the directive-column wording — see the Multilingualism Reconciliation Protocol
  below.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you reach a CLARIFY
marker, ask the user before proceeding — do not silently assume defaults. Only ask when
the answer will materially change the analysis; if the context has already been provided,
skip that question and proceed.

Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4 questions per
  call, 2–4 options each, header ≤ 12 characters. Pass the CLARIFY options as the `options`
  array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a `canUseTool`
  callback):** emit the CLARIFY questions as numbered plain text and **stop until the user
  replies**. Do not proceed with assumed answers.

When you proceed with partial context, state every assumption explicitly so the user can
correct it.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. **[Option A]**: [Description]
2. **[Option B]**: [Description]
3. **[Option C]**: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction]
```

For batch / non-interactive runs, use these defaults:

- Persona: Government / EU institution (dominant persona for this skill)
- Operating mode: Populated correlation table (post-NIM-drafting, pre-notification)
- Granularity: Article-paragraph-subparagraph
- Procedural language of the directive column: English (with [VERIFY] flag for the
  national language)
- Schema validation strictness: Full (warn on every missing provenance field)
- Render targets: Markdown + JSON + AKN4EU + LegalRuleML stub + Glass Box

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Directive CELEX / ELI** — e.g. `32022L2555` or
  `https://eur-lex.europa.eu/eli/dir/2022/2555/oj` for NIS2; the skill resolves the
  consolidated text and operative articles
- **NIM citation** — the national act, decree, or regulation transposing the directive
  in the target Member State (e.g. for Germany NIS2: the
  _NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz_ / NIS2UmsuCG; for Sweden
  CSRD: the amending acts to ÅRL ch. 6 and ABL ch. 8)
- **Obligation register** — output of `legalcode-eu-directive-analyzer` for the same
  directive (preferred — eliminates duplicate parsing)
- **Per-MS implementation matrix** — output of `legalcode-eu-transposition-tracker`
  (preferred — provides the NIM citation, status, and effective dates)
- **Partial table** — an in-progress correlation table that needs completion or
  schema validation
- **Blank scaffold request** — a directive plus a target MS where the NIM has not yet
  been finalised; the skill produces the empty left column and a plan-ahead checklist

Minimum required context to proceed:

- Directive identifier (CELEX or ELI)
- Target Member State (ISO 3166-1 alpha-2 code; or "EFTA-IS / EFTA-NO / EFTA-LI" for
  the EEA pillar)
- Operating mode: populated, scaffold, or partial-completion
- Procedural language of the notification (default: EN; flag national language)

If no input is provided, ask the user to supply the directive identifier and target
MS before proceeding.

### Step 2: Establish Persona and Operating Mode

⟁ CLARIFY — Persona

Treyst-style EU compliance work serves four distinct persona profiles whose deliverables
diverge sharply. The same directive analysis becomes a transposition draft for a ministry,
a comparative briefing for a law firm, an impact assessment for a company, or a policy
position for a trade federation.

1. **Government / EU institution**: Drafting national implementing measures, running
   internal conformity checks, preparing Commission notification packages, producing
   self-assessment for ESA (EFTA pillar) or DG-level review.
2. **Legal firm**: Producing client advisories, comparative cross-MS tables for client
   briefings, gap analyses for client compliance programmes.
3. **Company**: Building internal compliance impact assessments, identifying operational
   changes required, scoping internal policy updates, preparing for regulator engagement.
4. **Trade federation**: Industry-wide impact summaries, draft policy positions for
   engagement during legislative or transposition phases.

**Why this matters**: Persona determines output format, level of detail, audience
language, citation density, and which workflow branches to execute. A government
self-assessment requires correlation tables in Commission format; a company impact
assessment requires obligation extraction filtered to private-actor addressees; a
federation position needs comparative scoreboarding across MS.

Persona influence on the correlation-table workflow: **Government / EU institution**
is the dominant persona — they actually submit the table. Output target: the
Commission DOCX template variant for the relevant DG plus AKN4EU machine-readable
representation; schema validation strict; every cell carries provenance.
**Legal firm**: Markdown comparative table; AKN4EU optional; citation density high.
**Company**: filtered table showing only addressee-relevant rows (e.g. only NIS2
obligations addressed to "essential entities", not those addressed to competent
authorities). **Trade federation**: comparative correlation table across multiple
MS for the same directive (run once per MS, join the JSON outputs).

⟁ CLARIFY — Operating Mode

1. **Populated table for notification**: The NIM is final and ready to be notified to
   the Commission. Produce the Commission DOCX-format table with every directive
   operative article mapped to its NIM counterpart.
2. **Blank scaffold for drafting**: The NIM is being drafted. Produce the empty left
   column (every operative directive article enumerated) so the drafting team can
   plan the mapping before fixing the legislative architecture.
3. **Partial completion**: The user provides an in-progress table; the skill validates
   schema, flags missing rows, and proposes mappings for unmapped directive articles.
4. **Comparative cross-MS**: For legal-firm or trade-federation personas, the same
   directive across multiple MS — typically NIS2 / CSRD / CSDDD / GDPR / Whistleblower
   Directive 2019/1937 — to surface divergent transposition strategies.

**Why this matters**: Mode determines whether the right column starts populated or
empty, whether coverage gaps are normal (scaffold mode) or actionable findings
(populated mode), and whether the AKN4EU stub serialises a `correlationTable` doc or
a `correlationScaffold` doc.

⟁ CLARIFY — Render Targets

Which output formats does the user need? (Tick any combination.)

1. **Markdown two-column table** — human review (always produced).
2. **JSON correlation schema** — machine consumption by sibling skills E and F (always
   produced).
3. **AKN4EU XML** — for LEOS ingestion or institutional records (default ON for
   government persona; default OFF otherwise).
4. **LegalRuleML satisfaction assertions** — for policy-as-code engines (default ON
   for government and legal-firm personas).
5. **Commission DOCX template** — final notification artefact (default ON for
   government persona; mock-up only).

**Why this matters**: Render target governs the level of structural validation. A DOCX
notification artefact must round-trip through the AKN4EU representation to ensure no
metadata is silently lost.

### Step 3: Resolve Directive Articles

The left-hand column of the correlation table is enumerated from the **operative
articles** of the directive — articles establishing rights, obligations, definitions
that constrain operative provisions, and final provisions (transposition deadline,
addressees, entry into force). Recitals do **not** populate the left column (they are
interpretive context, not operative law — see _Casa Fleischhandels-GmbH v BALM_,
Case 215/88, ECLI:EU:C:1989:331; _Nilsson, Hagelgren and Arrborn_, Case C-162/97,
ECLI:EU:C:1998:554).

**3a. Source the directive text:**

In priority order:

1. **Obligation register from `legalcode-eu-directive-analyzer`** — preferred.
   Consume the per-article structured output (article number, paragraph, subparagraph,
   addressee, deontic operator, EEA-relevance flag).
2. **Consolidated text from EUR-Lex** at the directive ELI — e.g.
   `https://eur-lex.europa.eu/eli/dir/2022/2555/oj`. The consolidated version reflects
   subsequent amendments and corrigenda; the original adoption text is in the OJ
   reference.
3. **Original OJ text** if no consolidated version exists (typically directives less
   than 18 months old with no corrigenda).

**3b. Extract operative articles:**

Apply the following rules:

| Article type                                         | Include in left column?                                | Notes                                                                                     |
| ---------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Definitions article (typically Art. 2 or Art. 3)     | YES, where definitions constrain operative obligations | Some MS transpose definitions in a single national act section                            |
| Subject matter / scope                               | YES                                                    | Right column is the corresponding scope provision in the NIM                              |
| Operative obligations                                | YES, paragraph-by-paragraph                            | Article 21(2)(a) NIS2 ≠ Article 21(2)(b); separate rows                                   |
| Sanctions / penalties                                | YES                                                    | Right column is the national administrative penalty regime                                |
| Competent authorities designation                    | YES                                                    | Right column is the national authority designation                                        |
| Reporting and review obligations                     | YES                                                    | Right column is national reporting obligation                                             |
| Entry into force, addressees, transposition deadline | YES                                                    | The "transposition deadline" article shows when the NIM had to enter into force           |
| Recitals                                             | NO                                                     | Recitals are interpretive; cite them as evidence under specific articles in the Glass Box |
| Annexes (operative)                                  | YES, treat each Annex item as a row                    | NIS2 Annex I (essential entities sectors) and Annex II (important entities) populate rows |
| Annexes (declaratory)                                | YES if cross-referenced from operative provisions      | Otherwise OPTIONAL with [VERIFY] note                                                     |

**3c. Choose granularity:**

⟁ CLARIFY — Granularity

1. **Article-only**: One row per directive article. Compact; loses paragraph-level
   precision.
2. **Article-paragraph**: One row per article paragraph (recommended Commission default).
   Compromise between volume and precision.
3. **Article-paragraph-subparagraph (point-letter)**: One row per atomic operative unit
   (e.g. Art. 21(2)(a), Art. 21(2)(b), each on its own row). Highest precision; needed
   for conformity assessment by sibling skill E.

**Why this matters**: Granularity determines whether the conformity check downstream
can pinpoint where transposition succeeds or fails. Article-only granularity hides
incomplete transposition of complex articles; subparagraph granularity is the only
level at which `legalcode-eu-conformity-assessment` can deliver per-provision verdicts.

Default for government persona: article-paragraph-subparagraph.
Default for company / federation persona: article-paragraph.

**3d. Tag each row with metadata:**

For each directive row populated in the left column, capture:

| Field                          | Description                                                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `directive_article`            | Canonical citation: "Art. 21(2)(a)"                                                                                     |
| `directive_eli`                | ELI URI: `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng#art_21.2.a` (use the article fragment convention)          |
| `addressee`                    | "Member States" / "essential entities" / "important entities" / "competent authorities" / "Commission" / "ENISA" / etc. |
| `deontic_operator`             | OBLIGATION / PROHIBITION / PERMISSION / DEFINITION / OPTION / DEROGATION                                                |
| `transposition_required`       | YES / NO / IMPLICIT (NO for procedural articles addressed only to the Commission or final provisions; YES otherwise)    |
| `eea_relevance`                | YES / NO / DEFERRED (DEFERRED if EEA Joint Committee Decision is pending)                                               |
| `language_versions_reconciled` | List of language versions consulted (e.g. EN / DE / FR for NIS2)                                                        |
| `provenance`                   | OJ reference + consolidated-text date + analyst initials + timestamp                                                    |

Rows where `transposition_required = NO` (e.g. Art. 1 "subject matter", Art. 41 "entry
into force", Art. 42 "addressees" in NIS2) MUST still appear in the table — annotate
the right column "Pas de transposition nécessaire" / "Keine Umsetzung erforderlich" /
"No transposition required" per Member State language convention.

### Step 4: Resolve NIM Provisions

The right-hand column is the corresponding provision in the National Implementing
Measure. In some Member States the NIM is a single new act (e.g. Germany's
NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz / NIS2UmsuCG for NIS2); in
others it is a package of amendments to existing codes (e.g. Sweden's CSRD
transposition amends ÅRL ch. 6 and ABL ch. 8 alongside the
_lag om vissa stora företags hållbarhetsrapportering_).

**4a. Source the NIM text:**

In priority order:

1. **Per-MS implementation matrix from `legalcode-eu-transposition-tracker`** —
   preferred. Consume the structured NIM citation, official journal reference,
   effective date, and any consolidation status.
2. **National official journal** — the definitive source per Member State (DE
   Bundesgesetzblatt at `https://www.recht.bund.de`; FR JORF at
   `https://www.legifrance.gouv.fr`; IT Gazzetta Ufficiale at
   `https://www.gazzettaufficiale.it`; ES BOE at `https://www.boe.es`; SE SFS at
   `https://svenskforfattningssamling.se`; and the analogous national OJ resolver
   for every other Member State and EEA EFTA State). The shared EU legislative-data
   reference pack carries the full per-MS index of national OJ resolvers and
   parliament APIs; see
   [shared EU legislative-data pack](references/eu-legislative-data/).
3. **N-Lex aggregator** — `https://eur-lex.europa.eu/collection/n-law/mne.html` — the
   Commission's portal to national execution measures; metadata layer over national
   official journals.
4. **National parliament APIs** — for early-stage / draft NIM tracking (when the act
   has been adopted by parliament but not yet published in the national journal).
   Common endpoints: Riksdagen (SE) `https://data.riksdagen.se`; Storting (NO)
   `https://data.stortinget.no`; Folketinget (DK) `https://oda.ft.dk`; Althingi (IS)
   `https://www.althingi.is`; Bundestag (DE) `https://dip.bundestag.de`; Assemblée
   nationale (FR) `https://data.assemblee-nationale.fr`. Full list in the shared
   reference pack.

**4b. Extract NIM provisions:**

Capture the following metadata for each NIM provision that may appear in the right
column:

| Field                                        | Description                                                                                                                                          |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nim_citation`                               | Canonical national citation (e.g. "§ 30 Abs. 1 BSIG", "Art. L. 1332-6-7 CPCE", "art. 21, comma 2, lett. a, decreto legislativo 138/2024")            |
| `nim_act`                                    | Short title of the NIM (e.g. "BSIG-neu" or "NIS2UmsuCG", "decreto legislativo 138/2024", "lagen om åtgärder för en hög gemensam cybersäkerhetsnivå") |
| `nim_oj_ref`                                 | National OJ reference (e.g. "BGBl. I Nr. [TBD], [date]")                                                                                             |
| `nim_effective_date`                         | Date the provision enters into force                                                                                                                 |
| `nim_provenance_url`                         | Stable URL to the consolidated text                                                                                                                  |
| `nim_text_excerpt`                           | A short verbatim excerpt (≤ 300 characters) demonstrating the operative wording                                                                      |
| `language_of_text`                           | ISO 639-1 code (de / fr / it / es / sv / etc.)                                                                                                       |
| `analyst_translation_to_procedural_language` | Where the directive column is in EN, the analyst's working translation; flagged as non-authoritative                                                 |

**4c. Drafting-stage sources where final NIM is not yet published:** when the user
is mid-transposition, the NIM may exist only as a government bill
(_Regierungsentwurf_, _projet de loi_), a committee-stage amendment package, or an
approved act not yet promulgated. Cite the most recent stable version with a
[VERIFY: pre-promulgation] tag and the consultation date. After promulgation,
re-run the skill — never deliver a Commission notification table based on an
unpublished bill.

### Step 5: Map Article-by-Article

This is the analytical core of the skill. For each directive row produced in Step 3,
identify the corresponding NIM provision(s) and classify the mapping pattern.

**5a. Mapping patterns:**

| Pattern                       | Description                                                                                                                                                         | Right-column entry                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **1-to-1**                    | One directive provision is transposed in exactly one NIM provision                                                                                                  | Single citation                                                                                                |
| **1-to-N**                    | One directive provision is transposed across multiple NIM provisions (often when a single EU obligation requires both a substantive and a procedural national rule) | List of citations, comma-separated, with brief role label per citation                                         |
| **N-to-1**                    | Multiple directive provisions are transposed in one combined NIM provision                                                                                          | Same NIM citation will appear in multiple rows of the table; flag in Glass Box for downstream conformity check |
| **Partial**                   | The NIM transposes part of the directive provision but not all (e.g. transposes Art. 21(2)(a)–(g) but omits (h), (i), (j))                                          | NIM citation + "PARTIAL — omits [specific subparagraphs]" annotation                                           |
| **Deferred**                  | The directive provision falls within a national constitutional reservation or an opted-deferral (e.g. EEA Art. 103 reservation; sector-specific carve-out)          | "[DEFERRED — see [reservation]]"                                                                               |
| **No transposition required** | Article addressed exclusively to Commission, ENISA, ESMA, EFTA Surveillance Authority, or other Union actors; or article on entry into force / addressees           | "Pas de transposition nécessaire" / "Keine Umsetzung erforderlich"                                             |
| **Pre-existing law**          | Existing national provision predating the directive already satisfies the obligation; no new transposition act needed                                               | NIM citation + "[PRE-EXISTING — adopted before directive]"                                                     |
| **No mapping found**          | Coverage gap — the NIM contains no provision corresponding to the directive obligation                                                                              | "[GAP — no NIM provision identified]" + escalate to coverage-gap list                                          |

**5b. Mapping methodology:** for each directive row, run this sequence:

1. **Keyword search** of the NIM text for the directive's substantive concept
   (e.g. for NIS2 Art. 21(2)(a) "policies on risk analysis and information system
   security", search "Risikoanalyse", "Informationssicherheitskonzept", etc.).
2. **Cross-reference the national explanatory memorandum** (_Begründung_, _exposé
   des motifs_, _relazione illustrativa_) — many MS publish internal correspondence
   tables there; these are the authoritative starting point as they reflect
   ministry intent.
3. **Verify deontic match** — directive OBLIGATION must transpose as NIM OBLIGATION,
   not PERMISSION (_Commission v Italy_, C-129/00, ECLI:EU:C:2003:656; _Commission
   v United Kingdom_, C-484/04, ECLI:EU:C:2006:526).
4. **Verify addressee match** — an obligation directed at "essential entities"
   cannot be discharged by binding "all undertakings" without specifying the
   essentiality criterion.
5. **Verify scope match** — definitions, exemptions, derogations must align.
6. **Classify the pattern** from the table in 5a; capture provenance (ministry
   source, analyst initials, date, URL).

**5c. Multilingualism reconciliation:** Apply the Multilingualism Reconciliation
Protocol (see dedicated section below) for any row where the directive concept is at
risk of translation drift. Record the reconciled interpretation in the Glass Box.

**5d. Scaffold mode behaviour:**

In scaffold mode (no NIM yet drafted), Step 5 produces an empty right column with
proposed mapping notes:

- `[SCAFFOLD — to be drafted]` for every directive row
- A "drafting hint" field with the suggested transposition technique:
  - "Direct transposition into existing [act / code]"
  - "New standalone act required"
  - "Implementing regulation required (delegated to ministry)"
  - "No transposition required"
- A "complexity flag": LOW (1-to-1 likely) / MEDIUM (1-to-N likely) / HIGH (cross-
  reference into multiple existing codes likely; check for conflicts)

### Step 6: Identify Coverage Gaps

A **coverage gap** is a directive operative provision (`transposition_required = YES`)
that has no NIM mapping. Each coverage gap is a candidate transposition deficiency
under Art. 258 TFEU and a potential first-referral target under Art. 260(3) TFEU.

**6a. Gap detection rule:**

For each row in the populated table:

```
IF directive_article.transposition_required == YES
   AND nim_provision IS NULL
   AND mapping_pattern != "Pre-existing law"
   AND mapping_pattern != "Deferred"
THEN flag as coverage gap
```

**6b. Coverage-gap severity classification:**

| Severity     | Criteria                                                                                                                                                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL** | Operative obligation directly addressed to a regulated entity class (e.g. "essential entities shall...") with no NIM equivalent. Ready-to-cite in Art. 258 LFN.   |
| **HIGH**     | Definitional or scoping provision (e.g. definition of "essential entity") missing — leaves operative obligations without statutory anchor.                        |
| **MEDIUM**   | Procedural / administrative obligation missing (e.g. competent authority designation absent or unclear).                                                          |
| **LOW**      | Reporting / review obligation missing (e.g. "Member States shall by [date] report to the Commission..."); typically curable post-LFN without litigation exposure. |

**6c. Hand-off contract to `legalcode-eu-conformity-assessment`:** Coverage gaps
are emitted as a structured list in the JSON output under `coverage_gaps` (schema
in the Output Format Template) carrying `directive_article`, `directive_eli`,
`directive_text_excerpt`, `addressee`, `deontic_operator`, `severity`, `rationale`,
`verification_notes`, and `provenance`. The conformity assessment skill consumes
this list to deliver per-provision verdicts: **correct** / **partial** /
**incorrect** / **not transposed**. This skill does not deliver verdicts — it
identifies and structures the input.

### Step 7: Identify Over-Coverage

An **over-coverage** entry is a NIM provision that appears in the right column but has
no directive counterpart in the left column. This is the canonical signal of
**gold-plating** — national over-implementation of EU minimum standards.

**7a. Detection rule:**

After the article-by-article mapping is complete, run an inverse sweep:

```
FOR EACH NIM provision visible in the right column:
   IF nim_provision IS NOT cited in any row of the populated table
      OR nim_provision is cited only with annotation "[ADDED — beyond directive scope]"
   THEN flag as over-coverage candidate
```

**7b. Over-coverage taxonomy:**

Over-coverage rows fall into recognised categories. The full categorisation is the job
of `legalcode-eu-gold-plating-detector`; this skill captures the raw flag with enough
metadata for the downstream skill to work. Reference categories (HLG 2014; UK BIS
2013; CFA Society Poland 2024):

| Category                        | Description                                                                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Substantive over-implementation | NIM imposes stricter substantive obligation than directive (e.g. stricter incident reporting deadline)                                  |
| Scope extension                 | NIM extends application beyond the directive scope (e.g. covers all financial entities where directive covers only credit institutions) |
| Earlier effective date          | NIM enters into force earlier than directive deadline                                                                                   |
| Stricter penalty                | NIM penalty exceeds directive minimum-maximum                                                                                           |
| Additional procedural step      | NIM adds approval or filing step not required by directive                                                                              |
| Goldplated definition           | NIM definition narrower or broader than directive                                                                                       |
| Belt-and-braces                 | NIM duplicates an obligation already imposed by directly applicable EU law (regulation)                                                 |

**7c. Hand-off contract to `legalcode-eu-gold-plating-detector`:** Over-coverage
rows are emitted in the JSON output under `over_coverage_flags` (schema in the
Output Format Template) carrying `nim_provision`, `nim_text_excerpt`,
`directive_minimum`, `candidate_category`, `verification_notes`, and `provenance`.
The detector skill applies the published HLG / UK BIS / CFA categorisation rubric
and produces a typed gold-plating finding.

### Step 8: Validate Against Schema

Before emitting outputs, run an internal schema validation pass to catch the most
common defects in correlation tables.

**8a. Validation rules:**

| Rule                           | Check                                                                                         | Failure                          |
| ------------------------------ | --------------------------------------------------------------------------------------------- | -------------------------------- |
| **R1 Article uniqueness**      | Every directive operative article appears in exactly one row                                  | Merge duplicates; warn           |
| **R2 Provenance**              | Every populated cell has `provenance` (analyst, timestamp, source URL)                        | Block emission                   |
| **R3 Citation format**         | Directive citations use CELEX/ELI; NIM citations use national format                          | Reformat or flag                 |
| **R4 Deontic match**           | Directive OBLIGATION → NIM OBLIGATION (not PERMISSION)                                        | Warn + Glass Box note            |
| **R5 Addressee match**         | Directive addressee maps to a parallel NIM addressee class                                    | Warn                             |
| **R6 Language reconciliation** | ≥2 language versions consulted for any high-translation-risk row                              | Block unless waived in Glass Box |
| **R7 Coverage closure**        | Coverage gaps explicitly listed; no implicit `[GAP — ?]`                                      | Block                            |
| **R8 Over-coverage closure**   | Over-coverage flags explicitly listed                                                         | Block                            |
| **R9 Effective date sanity**   | NIM effective date ≤ directive deadline OR explicit late-transposition flag                   | Warn                             |
| **R10 Authority citation**     | JPDs (28 Sept 2011 + 27 Oct 2011) and Better Regulation Toolbox 2023 Ch. 4 cited in Glass Box | Block                            |

**8b. Adversarial 3-pass review for CRITICAL coverage gaps:**

For every coverage gap classified CRITICAL, run a 3-pass adversarial review before
emitting the finding (mirrors the rigour of `legalcode-policy-gap-analysis` Step 8):

- **Pass 1 — Mapping integrity**: is the gap the result of a missed search term, or
  is the obligation truly absent? Re-run the keyword search in at least two language
  versions of the NIM if the NIM is multilingual (e.g. Belgium FR/NL).
- **Pass 2 — Compensating provisions**: is there a pre-existing national provision
  that already satisfies the obligation (mapping pattern "Pre-existing law")? If so,
  re-classify and remove from coverage-gap list.
- **Pass 3 — Enforcement reality**: is this gap one that the Commission has
  historically flagged in completeness checks for similar directives? Cite at least
  one comparable LFN or reasoned opinion in the Glass Box where available; mark
  [VERIFY] otherwise.

### Step 9: Emit Outputs

Render the validated correlation table in each requested format. Schemas and full
examples in the Output Format Template below.

- **Markdown two-column table** — human review (always produced).
- **JSON correlation schema** — consumed by sibling skills E and F (always produced).
- **AKN4EU XML** — `<doc class="correlationTable">` stub; doc-class extension
  documented below.
- **LegalRuleML** — satisfaction-assertion stubs expressing "directive Art X is
  satisfied by NIM provision Y".
- **Commission DOCX (optional, government persona)** — populated mock-up of the
  standard two-column layout. The actual DG-specific template must be obtained from
  the Commission MNE workflow before notification.
- **Glass Box audit trail** — YAML.

---

## Commission Two-Column Format

The Commission does not publish a single binding DOCX template that every Member
State must use. Each Directorate-General publishes a template variant for files in
its policy area, and each Member State maintains a national template aligned to the
Commission's two-column expectation. The common denominator: two columns side by
side; **left** = directive operative article in the procedural language of the
notification (typically EN), at minimum the article citation, optionally verbatim
text; **right** = NIM provision in the notifying MS's official language, at minimum
the article citation, optionally verbatim text or analyst summary; **header** with
directive identification (CELEX, ELI, OJ ref) and NIM identification (act short
title, OJ ref, effective date); **footer / metadata block** with MS, notifying
ministry, contact, date, language regime, version.

**Common DG template variants** (illustrative — verify with the relevant DG before
use; the table below synthesises widely-observed practice and is **not** a list of
bindingly published Commission templates):

| DG                      | Policy area                                                      | Variant feature                                                                                    |
| ----------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| DG CONNECT              | NIS2, CRA, DSA, DMA                                              | Two-column DOCX, EN left + national right; optional "Comments" column                              |
| DG FISMA                | DORA, MiFID II, Prospectus, AIFMD                                | Two-column DOCX with explicit "transposition technique" column (direct / amendment / consolidated) |
| DG ENV                  | Environmental directives (Water Framework, Industrial Emissions) | Two-column DOCX with annex-by-annex sub-tables                                                     |
| DG EMPL                 | Working Time, Whistleblower 2019/1937                            | Two-column DOCX with "national context note" footer                                                |
| DG FISMA + DG ENV joint | CSRD Directive (EU) 2022/2464                                    | Two-column DOCX with ESRS standard cross-references                                                |
| DG JUST                 | Consumer Rights, GDPR-cluster directives                         | Two-column DOCX                                                                                    |
| SG                      | Horizontal                                                       | Secretariat-General "master template"; falls back to bilateral DG                                  |

[VERIFY] each DG's current template directly with the Member State Notification
(MNE) workflow before submitting.

**Common metadata fields across variants**: directive title (full + short), CELEX,
OJ reference and adoption date, transposition deadline (Art. 41 NIS2: 17 October
2024; CSRD Art. 5 sequencing 2024–2028; CSDDD Art. 37 deadline 26 July 2026); MS
and notifying ministry; NIM short title, OJ ref, effective date; method of
transposition (direct adoption / amendment / combination); constitutional approval
flag (relevant for EEA pillar Art. 103 EEA reservation).

---

## Article-Level Granularity

Granularity is the single most consequential design choice in a correlation table.
It cascades through every downstream artefact: the conformity assessment (skill E)
cannot deliver per-provision verdicts at a coarser granularity than the table itself;
the gold-plating detector (skill F) cannot isolate over-coverage at coarser
granularity; the infringement procedure tracker (skill H) cannot pinpoint LFN bullets
at coarser granularity. Step 3c above defines the three levels (article-only;
article-paragraph; article-paragraph-subparagraph). Three additional rules govern
edge cases:

**Operative vs. recital — a hard line:** Recitals do not populate the left column.
They are interpretive (_Casa Fleischhandels-GmbH v BALM_, Case 215/88,
ECLI:EU:C:1989:331; _Nilsson_, Case C-162/97, ECLI:EU:C:1998:554) and not directly
enforceable. They may, however, be cited in the Glass Box as evidence supporting the
interpretation of an operative article. NIS2 has 144 recitals and 46 articles; the
table contains rows only for articles.

**Complex articles with multi-level structure** (e.g. Art. 23 NIS2 paragraphs (1)–
(11), each with subparagraphs and internal cross-references): treat each operative
atom (paragraph, subparagraph, point) as a separate row. Where a single subparagraph
carries multiple distinct obligations (early-warning duty + final-report duty), split
into two rows with notation "Art. 23(4)(a) [first sentence]" / "Art. 23(4)(a)
[second sentence]" and record the split decision in the Glass Box.

**Annex granularity:** operative annexes (NIS2 Annex I, Annex II — sectoral lists)
populate one row per annex item. Multi-element annex items (NIS2 Annex I "Energy"
carries 6 sub-sectors) populate one row per sub-sector. Where the NIM collapses these
into a single national list, the right column carries the same citation across
multiple rows (N-to-1) and the consolidation is flagged in Glass Box.

---

## Mapping Patterns

The mapping pattern is the structural relationship between the directive provision
(left) and the NIM provision (right). Pattern classification has consequences: the
conformity assessment downstream treats partial mappings as candidate non-conformity;
the gold-plating detector treats over-coverage as a substantive flag; the
infringement tracker treats coverage gaps as candidate Art. 258 bullets. Step 5a
above lists the eight patterns in tabular form. Each is illustrated below with a
worked example.

**1-to-1 — definitions and compact obligations** (cleanest mapping):

```
Art. 6(1) NIS2 ("'network and information system' means...")
  → § 2 Nr. 6 BSIG-neu (definition of "Netz- und Informationssystem")
```

**1-to-N — directive obligation split across substantive + procedural NIM rules**:

```
Art. 23(4) NIS2 (incident notification — early warning, intermediate, final)
  → § 32(2) BSIG-neu (early warning duty)
  → § 32(3) BSIG-neu (intermediate report)
  → § 32(4) BSIG-neu (final report)
```

The right column lists each NIM citation comma-separated with a role label.

**N-to-1 — directive sub-atoms consolidated into one NIM provision** (catalogue style,
common in DE/AT):

```
Art. 21(2)(a)–(j) NIS2 (ten risk-management measures)
  → § 30(2) BSIG-neu Nrn. 1–10 (catalogue of ten measures)
```

The same NIM citation appears in multiple table rows — once per directive sub-atom.
Flag in Glass Box for downstream conformity assessment.

**Partial — directive sub-atom incompletely transposed** (subtype of coverage gap;
the unmapped subparagraphs become CRITICAL coverage-gap entries):

```
Art. 21(2) NIS2 sub-atoms (a)–(j)
  → § 30(2) Nrn. 1–7 BSIG-neu (transposes (a)–(g); (h)–(j) ABSENT — coverage gap)
```

**Deferred — constitutional reservation or sector-specific opt-out** (most common in
the EEA pillar under Art. 103 EEA):

```
Art. 21 NIS2 → [DEFERRED — Storting approval pending under Art. 103 EEA;
                Joint Committee Decision date — see legalcode-eea-incorporation-tracker]
```

**No transposition required — directive provision addressed to Union institutions or
meta-provisions**:

- Art. 1 NIS2 (subject matter) — declaratory
- Art. 31 NIS2 (Cooperation Group) — Commission/ENISA addressee
- Arts. 41–43 NIS2 (transposition deadline / entry into force / addressees) — meta
  provisions

Right-column entry: "Pas de transposition nécessaire" / "Keine Umsetzung erforderlich"
/ "No transposition required" in the language of the NIM.

**Pre-existing law — prior national provision already satisfies the obligation**
(Art. 288 TFEU does not require new legislation where pre-existing legislation
already achieves the directive's prescribed result). Cite the pre-existing act with
year:

```
Art. 13 GDPR (information to be provided)
  → 2 § personuppgiftslagen (1998:204) [PRE-EXISTING — repealed and replaced by GDPR
     + dataskyddslagen 2018:218]
```

**No mapping found — terminal pathology**: the NIM has no provision corresponding to
the directive obligation. Feeds Step 6 (coverage gaps) and the conformity assessment
downstream.

---

## Completeness Check

The completeness check is the Commission's first analytical pass on a transposition
notification. It asks one question: is every operative provision of the directive
covered by some NIM provision?

The methodology is set out in the Better Regulation Toolbox 2023, Chapter 4 (Compliance,
Implementation and Preparing Proposals). Toolbox Ch. 4 distinguishes:

- **Completeness check**: every operative provision has at least one NIM
  counterpart (this skill produces the input to that check).
- **Conformity check**: each NIM counterpart is substantively faithful to the
  directive obligation (the job of `legalcode-eu-conformity-assessment`).

**Completeness gap = directive operative provision with no NIM mapping.**

Each completeness gap identified by this skill is:

- Logged in the JSON `coverage_gaps` array (Step 6c)
- Severity-classified (CRITICAL / HIGH / MEDIUM / LOW per Step 6b)
- Adversarially reviewed (Step 8b 3-pass review for CRITICAL gaps)
- Emitted to `legalcode-eu-conformity-assessment` for verdict assignment

A persistent completeness gap at the date of the transposition deadline is a
candidate for an Art. 258 TFEU letter of formal notice and, if the Member State has
failed to notify any transposition measure, the first-referral pecuniary penalty
under Art. 260(3) TFEU (first applied in _Commission v Belgium_, Case C-543/17,
ECLI:EU:C:2019:573).

The Commission's enforcement track record on completeness checks is maintained in
the Single Market Scoreboard
(`https://single-market-scoreboard.ec.europa.eu/`) — citing the most recent
edition of the scoreboard in the Glass Box improves the credibility of severity
classifications.

---

## Over-Coverage / Gold-Plating Signal

The mirror image of the completeness check is the over-coverage check: does the NIM
contain provisions that go beyond what the directive requires? Over-coverage is the
canonical signal of **gold-plating** — national over-implementation of EU minimum
standards.

Gold-plating is not always inappropriate. It is permissible under Art. 288 TFEU
where Member States choose more stringent measures, **provided** the directive does
not prescribe maximum harmonisation. For maximum-harmonisation directives, going
beyond the directive is unlawful (see _Lenders v Commission_-style analysis in
consumer-protection files; CJEU case law on consumer credit and unfair commercial
practices).

Whether the directive permits or prohibits gold-plating is determined by the
directive's harmonisation level, set by the legislator and recorded in the directive
recitals and articles. This skill records the harmonisation flag (consumed from the
upstream `legalcode-eu-directive-analyzer` output) but does not adjudicate the
appropriateness of gold-plating findings — that is the job of
`legalcode-eu-gold-plating-detector`.

**This skill's role:** identify and structure over-coverage candidates; classify
them against the published HLG (2014) / UK BIS (2013) / CFA Society Poland (2024)
typologies; emit a structured flag list to the detector skill. (See Step 7b for the
taxonomy.)

**Authoritative sources for the gold-plating typology:**

- High Level Group on Administrative Burdens, _Final report on the better
  application of EU directives_ (2014):
  `https://ec.europa.eu/futurium/en/system/files/ged/hlg_16_0008_00_conclusions_and_recomendations_on_goldplating_final.pdf`
- UK BIS, _Gold-Plating Review: The Operation of the Transposition Principles in
  the Government's Guiding Principles for EU Legislation_ (2013).
- CFA Society Poland, _Gold-plating in EU Capital Markets — Comparison of
  MiFID II / Prospectus / AIFMD across Member States_ (2024).

---

## Worked Example: NIS2 ↔ Germany NIS2UmsuCG

The German transposition of NIS2 is the canonical worked example. Germany's
_NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz_ (NIS2UmsuCG) was the
subject of multiple federal-government drafts and an extensive Linklaters (Berlin)
draft tracker. The final BGBl. publication must be verified against the federal
official journal at `https://www.recht.bund.de` before any cell is treated as
authoritative; pending that verification, the rows below are flagged
[VERIFY: pre-promulgation tracker]. The transposition deadline was 17 October 2024;
Germany did not transpose by deadline, generating an Art. 258 LFN scenario tracked
by the Commission Single Market Scoreboard. The _Regierungsentwurf_ introduces a
new BSIG (BSIG-neu) replacing the prior BSIG, with §§ 28–32 BSIG-neu carrying the
operative cybersecurity risk-management and reporting obligations.

**Header row:**

```
Directive: NIS2 — Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022,
  p. 80, ELI https://eur-lex.europa.eu/eli/dir/2022/2555/oj
Transposition deadline: 17 October 2024 (Art. 41(1))
Notifying MS: Germany
NIM: NIS2UmsuCG, establishing a new BSIG-neu replacing the prior BSIG
NIM OJ ref: BGBl. I [VERIFY: pending federal-official-journal publication]
NIM effective date: [VERIFY against Regierungsentwurf 22 July 2024]
Procedural language: EN (directive column) / DE (NIM column)
Glass Box: language reconciliation EN-DE; Art. 21(2) terminology checked against IATE
```

**Five-row slice:**

```
| # | Directive provision (EN)             | NIM provision (DE)                          | Pattern | Notes |
|---|--------------------------------------|---------------------------------------------|---------|-------|
| 1 | Art. 21(2)(a): "policies on risk     | § 30(2) Nr. 1 BSIG-neu: "Konzepte in Bezug  | 1-to-1  | [VERIFY: pre-promulgation tracker] Linklaters draft tracker (Berlin) consulted; final wording may differ in BGBl. EN/DE reconciliation: "policies" → "Konzepte" (IATE-confirmed). |
|   | analysis and information system      | auf die Risikoanalyse und Sicherheit von    |         | |
|   | security" (essential entities)       | Informationssystemen"                       |         | |
| 2 | Art. 21(2)(b): "incident handling"   | § 30(2) Nr. 2 BSIG-neu: "Bewältigung von    | 1-to-1  | [VERIFY] EN "incident handling" → DE "Bewältigung von Sicherheitsvorfällen". IATE confirms equivalence. |
|   |                                      | Sicherheitsvorfällen"                       |         | |
| 3 | Art. 21(2)(c): "business continuity, | § 30(2) Nr. 3 BSIG-neu: "Aufrechterhaltung  | 1-to-1  | [VERIFY] Verify all three sub-elements (BCM + DR + crisis mgmt) match in final wording. |
|   | such as backup management and        | des Betriebs, wie Backup-Management und     |         | |
|   | disaster recovery, and crisis        | Wiederherstellung nach einem Notfall sowie  |         | |
|   | management"                          | Krisenmanagement"                           |         | |
| 4 | Art. 21(2)(d): "supply chain         | § 30(2) Nr. 4 BSIG-neu: "Sicherheit der     | 1-to-1  | [VERIFY] Direct lexical match. |
|   | security..."                         | Lieferkette..."                             |         | |
| 5 | Art. 21(2)(j): "the use of multi-    | § 30(2) Nr. 10 BSIG-neu: "Einsatz von       | 1-to-1  | [VERIFY] EN "continuous authentication solutions" → DE "kontinuierliche Authentisierung"; IATE check confirms. |
|   | factor authentication or continuous  | Lösungen zur Multi-Faktor-Authentisierung   |         | |
|   | authentication solutions..."         | oder kontinuierlichen Authentisierung..."   |         | |
```

**Coverage-gap example for the same directive (illustrative, [VERIFY] flagged):**

```
| Art. 21(4): "Member States shall ensure that, where an entity finds that..." (corrective measures) |
| [GAP — no NIM provision identified in Linklaters tracker] |
```

This GAP row would feed Step 6 — coverage-gap list — at severity HIGH (procedural
obligation feeding into competent-authority practice; not directly addressed to
regulated entities but missing it weakens the supervisory architecture).

**Over-coverage example (illustrative, [VERIFY] flagged):**

```
| § 32(1) BSIG-neu: "Wesentliche Einrichtungen müssen Sicherheitsvorfälle binnen 12  |
| Stunden melden..." [if confirmed in BGBl. — directive Art. 23(4)(a) prescribes      |
| 24-hour early warning] | OVER-COVERAGE → flag to gold-plating detector              |
```

**Glass Box authority anchors for this worked example:** the JPDs of 28 September
2011 (OJ C 369, p. 14) and 27 October 2011 (OJ C 369, p. 15); Better Regulation
Toolbox 2023 Chapter 4 (completeness-check methodology); TFEU Art. 260(3) first
applied in _Commission v Belgium_ (C-543/17, ECLI:EU:C:2019:573); Council Resolution
of 8 June 1993 (OJ C 166, 17.06.1993, p. 1); Linklaters NIS2 transposition tracker
(Berlin office) — practitioner source consulted [date]; **final BGBl. publication of
NIS2UmsuCG required before any production submission** [VERIFY]; BfDI guidance on
NIS2 supervision [VERIFY current edition]; Bundestag dip portal
(`https://dip.bundestag.de`). Full URLs in the Provenance section.

---

## AKN4EU correlationTable doc class

The AKN4EU subschema does not currently publish a binding `correlationTable` doc
class. AKN4EU is built on OASIS LegalDocML 1.0 (Akoma Ntoso, 2018), and the EU
institutional adaptation focuses on `<bill>`, `<act>`, `<judgment>`, and generic
`<doc>` document classes. This skill therefore adopts a documented extension —
`<doc class="correlationTable">` — piggy-backing on the generic `<doc>` element
with a typed `class` attribute. Structural choices: (1) root `<akomaNtoso>` with
namespace `http://docs.oasis-open.org/legaldocml/ns/akn/3.0`; (2) `<doc
class="correlationTable" name="correlationTable">`; (3) standard `<meta>` with
`<identification>` (FRBR Work + Expression; Manifestation produced at serialisation
time); (4) `<references>` block with `<TLCRef>` elements for the directive ELI, NIM
reference, and JPD anchors; (5) `<mainBody>` with `<table>` carrying one `<tr>` per
row, `<td>` for left (directive) / right (NIM) / pattern / notes; (6)
`<authorialNote>` blocks per row for analyst, timestamp, source URL. These choices
are recorded in the skill output Glass Box so a downstream LEOS ingester can adapt.

---

## Multilingualism Reconciliation Protocol

The 24 official EU language versions are equally authentic (Reg. 1/1958). Where the
left-column directive text and the right-column NIM text are in different languages
— almost always the case — the analyst must reconcile language versions before
fixing the wording. The protocol is:

1. State the directive language version consulted (default: EN as procedural
   language) and the NIM language version (always the official NIM language).
2. Where the directive concept is at risk of translation drift, consult at least
   one other language version of the directive as a check. Common high-risk
   terms: "appropriate" / "geeignet" / "approprié" (proportionality standard);
   "shall" / "doit" / "muss" (OBLIGATION vs. PERMISSION); "where appropriate" /
   "soweit angemessen" / "le cas échéant" (soft-permission carve-outs); "without
   delay" / "unverzüglich" / "sans retard" (time-bound triggers); "significant" /
   "erheblich" / "rilevante" (threshold qualifiers).
3. Use IATE (`https://iate.europa.eu/`) for technical terminology disputes —
   especially in cybersecurity (NIS2, CRA), AI (AI Act 2024/1689), financial
   services (DORA, MiFID II), sustainability (CSRD ESRS standards).
4. Apply the CJEU rule: where language versions diverge, interpret in light of the
   purpose and general scheme of the act — _CILFIT_ (C-283/81, ECLI:EU:C:1982:335);
   _Codan_ (C-236/97, ECLI:EU:C:1998:208); _EMU Tabac_ (C-296/95,
   ECLI:EU:C:1998:152). Record the reconciled interpretation in the Glass Box
   `language_reconciliation` array, one entry per high-risk term, with the
   language versions consulted and the reconciled meaning chosen.

---

## Confidence Scoring

Assign a confidence level to every mapping cell.

| Level        | Score Range | Definition                                                                                                                         | Action                                                         |
| ------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **VERIFIED** | 0.90–1.00   | NIM citation confirmed against national OJ; directive citation against EUR-Lex consolidated text; both language versions consulted | State without qualification                                    |
| **LIKELY**   | 0.70–0.89   | NIM citation from reliable practitioner source (Linklaters, A&O, ministry explanatory memorandum); not OJ-verified                 | State with brief caveat                                        |
| **POSSIBLE** | 0.50–0.69   | Good-faith inference from drafts; not promulgated; semantic match plausible                                                        | State with explicit reasoning; flag [VERIFY]                   |
| **VERIFY**   | 0.30–0.49   | Pre-promulgation only; mapping plausible but unconfirmed                                                                           | Flag "[VERIFY: pre-promulgation]"                              |
| **ASSUMED**  | < 0.30      | Placeholder based on typical national transposition pattern                                                                        | Do not include in Commission notification without verification |

**Default confidence levels by source:** national OJ text → VERIFIED (0.95); adopted
but unpublished act → LIKELY (0.80); government bill → POSSIBLE (0.60); pre-bill
ministry consultation draft → VERIFY (0.40); practitioner draft tracker → LIKELY
(0.75); Single Market Scoreboard snapshot → LIKELY (0.80); inferred mapping with
no NIM source → ASSUMED (0.20).

---

## Anti-Patterns

What NOT to do when building a correlation table:

1. **Treating recitals as operative text** — Populating the left column with recitals
   produces a malformed table. Recitals are interpretive (see _Casa
   Fleischhandels-GmbH v BALM_, Case 215/88, ECLI:EU:C:1989:331; _Nilsson_, Case
   C-162/97, ECLI:EU:C:1998:554), not directly enforceable. Cite recitals only in the
   Glass Box as evidence supporting the interpretation of an article.

2. **Article-only granularity for complex articles** — Using one row per article when
   articles carry ten or more distinct sub-obligations (NIS2 Art. 21(2)(a)–(j); DORA
   Art. 6 ICT risk management framework; CSRD Art. 19a sustainability reporting
   elements). Loses the precision needed for completeness and conformity checks.
   Use article-paragraph-subparagraph granularity for any article carrying more than
   one operative atom.

3. **Silent translation drift / ignoring language regime equality** — Treating the
   NIM language version (or English) as definitive without reconciling against at
   least one other directive language version. The 24 official languages are
   equally authentic (Reg. 1/1958; _CILFIT_; _Codan_; _EMU Tabac_); the procedural
   language of the notification appears in the left column for convenience, not
   because it is privileged. Always record the language reconciliation in the
   Glass Box.

4. **Missing the inverse sweep** — Building only the directive-to-NIM map and not
   running the inverse sweep (NIM-to-directive). Misses over-coverage and silently
   conceals gold-plating signals from sibling skill F. Always run both directions.

5. **Conflating "no transposition required" with "coverage gap"** — Articles
   addressed only to Commission, ENISA, ESMA, ESA, or other Union actors require
   no transposition. Marking them as "GAP" produces false-positive coverage gaps.
   Use the explicit "Pas de transposition nécessaire" / "Keine Umsetzung
   erforderlich" entry.

6. **Pre-promulgation citations treated as final** — Citing a _Regierungsentwurf_
   or _projet de loi_ as the NIM in a table delivered for Commission notification.
   Pre-promulgation citations must carry a "[VERIFY: pre-promulgation]" tag; the
   table must be re-run after publication in the national OJ before submission.

7. **Bundling N-to-1 mappings into a single row** — When the NIM consolidates
   multiple directive provisions into one national provision, the temptation is to
   write a single row "Art. 21(2)(a)–(j) → § 30(2) BSIG-neu". This conceals the
   per-subparagraph completeness check. Write one row per directive sub-atom; let
   the same NIM citation appear in multiple rows; record the consolidation in the
   Glass Box.

8. **Skipping the deontic match check** — A directive obligation transposed as a
   national permission is a transposition defect (_Commission v Italy_, C-129/00,
   ECLI:EU:C:2003:656; _Commission v United Kingdom_, C-484/04, ECLI:EU:C:2006:526).
   Always verify the deontic operator on each side of the row matches.

9. **Ignoring constitutional reservations in the EEA pillar** — In IS / NO / LI,
   reservations under Art. 103 EEA suspend obligations until the relevant national
   parliament gives approval. Mark such rows "[DEFERRED — [Storting / Althingi /
   Landtag] approval pending]", not as a coverage gap. Coordinate with
   `legalcode-eea-incorporation-tracker`.

10. **Per-cell provenance / language metadata missing** — Recording provenance only
    at the table level, or capturing right-column NIM text without
    `language_of_text` and `nim_provenance_url`. Every cell must carry its own
    audit trail (analyst, timestamp, source URL, language version) so it can be
    verified or reconciled later.

11. **Ignoring annex granularity** — Treating annexes as a single block when the
    annex carries multiple operative items (NIS2 Annex I lists Energy, Transport,
    Banking, Health, Drinking water, Wastewater, Digital infrastructure, ICT B2B
    services, Public administration, Space). Each annex item is an operative atom;
    populate one row per item.

12. **Treating "pre-existing law" as "no transposition required"** — Different
    patterns. "Pre-existing law" is a legitimate transposition technique relying on
    prior national legislation and requires a citation to the prior act. "No
    transposition required" is reserved for directive provisions addressed to Union
    institutions or for meta-provisions.

13. **Late-transposition tables without flag** — Where the NIM enters into force
    after the directive transposition deadline, the table must record the
    late-transposition status in the metadata block and flag CRITICAL severity for
    any coverage gaps remaining at the deadline date — those rows drive Art. 258
    LFNs and Art. 260(3) penalties.

14. **Stale tables after directive amendment / skipping authority anchors** — A
    directive amended by a corrigendum or amending directive requires the table to
    be regenerated; record the consolidated-text date in the Glass Box. Every
    Glass Box must cite the JPDs of 28 September 2011 (OJ C 369, p. 14) and 27
    October 2011 (OJ C 369, p. 15) and the Better Regulation Toolbox 2023 Ch. 4 —
    skipping these citations breaks the audit trail and weakens severity
    classifications.

---

## Writing Standards

Follow these standards when producing correlation table outputs:

1. **Article citation format (directive)**: `Art. [number]([paragraph])([subparagraph])
[short directive name]`. Example: "Art. 21(2)(a) NIS2". Include CELEX
   parenthetically on first reference per artefact.

2. **Article citation format (NIM)**: national convention. Examples:
   DE `§ 30(2) Nr. 1 BSIG-neu`; FR `art. L. 1332-6-7 CPCE`; IT
   `art. 21, comma 2, lett. a, decreto legislativo 138/2024`; SE `30 § [act]`; NL
   `artikel 30, lid 2, onderdeel a [act]`. Format per the shared EU
   legislative-data reference pack.

3. **Deontic operator labelling**: each row records the deontic operator from the
   directive provision (OBLIGATION / PROHIBITION / PERMISSION / DEFINITION / OPTION
   / DEROGATION). Verify NIM operator matches.

4. **Per-cell provenance, [VERIFY] markers, and confidence level inline**: every
   populated cell carries provenance (analyst, timestamp, source URL, language
   version); [VERIFY] sits inline immediately after any unconfirmed claim
   ("§ 30(2) Nr. 10 BSIG-neu [VERIFY: pre-promulgation]"); the JSON / AKN4EU / Glass
   Box include the confidence level (VERIFIED / LIKELY / POSSIBLE / VERIFY /
   ASSUMED) for every row.

5. **CELEX / ELI / ECLI in prose**: spell out on first use, abbreviate after.
   "Directive (EU) 2022/2555 (NIS2; CELEX 32022L2555; ELI
   `https://eur-lex.europa.eu/eli/dir/2022/2555/oj`)" — first use; "NIS2" thereafter.

6. **EEA-relevance flag**: every row carries `eea_relevance: YES / NO / DEFERRED`.
   The Joint Committee Decision date determines transition into the EEA Annex;
   until adopted, EEA EFTA mapping is DEFERRED.

7. **Language reconciliation entry**: where the analyst consulted multiple
   language versions of the directive, record the comparison in the Glass Box
   `language_reconciliation` array.

8. **Late-transposition status**: where the NIM effective date exceeds the
   directive transposition deadline, record the late-transposition delta in the
   Glass Box (NIM date − deadline date in days) and flag CRITICAL severity for any
   unmapped operative provisions remaining at the deadline.

9. **Active voice**: "the NIM transposes Art. 21(2)(a) at § 30(2) Nr. 1 BSIG-neu",
   not the passive form.

10. **One row per operative atom**: never bundle multiple operative atoms into a
    single row, even when the NIM consolidates. Use N-to-1 mapping pattern with
    repeated NIM citation across rows.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When legalcode-mcp is available:

1. Use it in Step 3 to fetch consolidated directive text from EUR-Lex by ELI.
2. Use it in Step 4 to fetch NIM text from N-Lex or the relevant national OJ
   resolver.
3. Use it in Step 5 to consult IATE for high-risk terminology disputes.
4. Use it in Step 6 to consult the Single Market Scoreboard for the Member State's
   transposition track record on similar directives.
5. Use it in Step 8 to verify completeness against published Commission scoreboards.

Save research results to `/tmp/legalcode-correlation-research.md` and note in Glass
Box: `legalcode_mcp: "Connected — research file at [path]"`.

### Without legalcode-mcp

Proceed with built-in reference tables (national OJ index in Step 4a, language
regime in the Multilingualism Reconciliation Protocol). Mark all unverified
citations with [VERIFY] and apply downward confidence adjustments:

- NIM citations from practitioner trackers: LIKELY → POSSIBLE
- Language reconciliation when only one language consulted: LIKELY → VERIFY
- Single Market Scoreboard claims: LIKELY → VERIFY

### Sibling Skill Integration Triggers

| Trigger                                                   | Invoke This Skill                             |
| --------------------------------------------------------- | --------------------------------------------- |
| Need the directive obligation register first              | `legalcode-eu-directive-analyzer`             |
| Need the per-MS NIM citation and effective date           | `legalcode-eu-transposition-tracker`          |
| Coverage gaps identified — need conformity verdicts       | `legalcode-eu-conformity-assessment`          |
| Over-coverage flagged — need gold-plating categorisation  | `legalcode-eu-gold-plating-detector`          |
| EEA EFTA pillar — need Joint Committee Decision tracking  | `legalcode-eea-incorporation-tracker`         |
| Late transposition — need Art. 258/260 procedure timeline | `legalcode-eu-infringement-procedure-tracker` |

---

## Output Format Template

### 1. Markdown two-column table (human review)

```
# Correlation Table — [Directive short title] → [Member State NIM short title]

**Directive:** [Full title], [CELEX], [OJ reference], [ELI URI]
**Transposition deadline:** [date] ([Art.])
**Notifying Member State:** [MS]
**NIM:** [Full title and abbreviation]
**NIM OJ ref:** [national OJ reference]
**NIM effective date:** [date]
**Procedural language:** [EN / national language]
**Granularity:** [article / article-paragraph / article-paragraph-subparagraph]
**Operating mode:** [Populated / Scaffold / Partial / Comparative]
**Date prepared:** [YYYY-MM-DD]
**Analyst:** [identifier]

| # | Directive provision (procedural language) | NIM provision (national language) | Pattern | Notes |
|---|-------------------------------------------|----------------------------------|---------|-------|
| 1 | Art. 1(1) [Subject matter]               | [Pas de transposition / Keine Umsetzung] | No transposition required | Declaratory; not addressed to MS |
| 2 | Art. 2(1) [Scope]                        | § X [Geltungsbereich]            | 1-to-1  | [VERIFY] |
| ...                                                                                                                           |
| N | Art. 41 [Transposition]                  | [Pas de transposition / Keine Umsetzung] | No transposition required | Meta-provision |

## Coverage gaps (CRITICAL / HIGH / MEDIUM / LOW)

[List from Step 6]

## Over-coverage flags

[List from Step 7]

## Authority anchors

- Joint Political Declaration of 28 September 2011 of Member States and the
  Commission on explanatory documents (OJ C 369, 17.12.2011, p. 14)
- Joint Political Declaration of 27 October 2011 of the European Parliament, the
  Council and the Commission on explanatory documents (OJ C 369, 17.12.2011, p. 15)
- Better Regulation Toolbox 2023, Chapter 4
- TFEU Art. 260(3) — first-referral penalty for failure to notify
  (*Commission v Belgium*, Case C-543/17, ECLI:EU:C:2019:573)
- Council Resolution of 8 June 1993 on the quality of drafting of Community
  legislation (OJ C 166, 17.06.1993, p. 1)
```

### 2. JSON correlation schema

```json
{
  "correlation_table": {
    "schema_version": "1.0",
    "skill_name": "legalcode-eu-correlation-table-builder",
    "operating_mode": "populated | scaffold | partial | comparative",
    "directive": {
      "short_title": "NIS2",
      "full_title": "Directive (EU) 2022/2555 of 14 December 2022 ...",
      "celex": "32022L2555",
      "oj_reference": "OJ L 333, 27.12.2022, p. 80",
      "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj",
      "transposition_deadline": "2024-10-17",
      "consolidated_text_date": "YYYY-MM-DD",
      "harmonisation_level": "minimum | maximum | mixed",
      "eea_relevance": "yes | no | deferred"
    },
    "member_state": {
      "iso_code": "DE",
      "notifying_ministry": "BMI",
      "nim_short_title": "NIS2UmsuCG",
      "nim_full_title": "NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz",
      "nim_oj_reference": "BGBl. I [VERIFY]",
      "nim_effective_date": "YYYY-MM-DD",
      "transposition_method": "new_act | amendment_to_existing | combination",
      "transposition_status": "transposed | partial | not_transposed",
      "language_of_nim": "de"
    },
    "metadata": {
      "granularity": "article | article-paragraph | article-paragraph-subparagraph",
      "procedural_language": "en",
      "date_prepared": "YYYY-MM-DD",
      "analyst": "string",
      "version": "1.0"
    },
    "rows": [
      {
        "row_id": "R-001",
        "directive_article": "Art. 21(2)(a)",
        "directive_eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng#art_21.2.a",
        "directive_text_excerpt": "policies on risk analysis and information system security",
        "addressee": "essential entities",
        "deontic_operator": "OBLIGATION",
        "transposition_required": true,
        "eea_relevance": "yes",
        "nim_provisions": [
          {
            "nim_citation": "§ 30(2) Nr. 1 BSIG-neu",
            "nim_act": "BSIG-neu",
            "nim_text_excerpt": "Konzepte in Bezug auf die Risikoanalyse und Sicherheit von Informationssystemen",
            "language_of_text": "de",
            "analyst_translation_to_procedural_language": "policies on risk analysis and information system security",
            "nim_provenance_url": "https://www.recht.bund.de/...",
            "deontic_operator": "OBLIGATION"
          }
        ],
        "mapping_pattern": "1-to-1",
        "partial_omissions": [],
        "language_reconciliation": [
          {
            "term": "policies",
            "directive_versions_consulted": ["en", "de"],
            "reconciled_meaning": "Konzepte (IATE)"
          }
        ],
        "confidence_level": "LIKELY",
        "confidence_score": 0.78,
        "verification_notes": "[VERIFY: pre-promulgation tracker]",
        "provenance": {
          "analyst": "string",
          "timestamp": "YYYY-MM-DDThh:mm:ssZ",
          "source": "Linklaters NIS2 tracker, [date]"
        }
      }
    ],
    "coverage_gaps": [
      {
        "directive_article": "Art. 21(2)(j)",
        "directive_eli": "...",
        "directive_text_excerpt": "MFA / continuous authentication...",
        "addressee": "essential entities",
        "deontic_operator": "OBLIGATION",
        "severity": "CRITICAL | HIGH | MEDIUM | LOW",
        "rationale": "string",
        "verification_notes": "[VERIFY]",
        "provenance": { "analyst": "string", "timestamp": "..." }
      }
    ],
    "over_coverage_flags": [
      {
        "nim_provision": "§ 32(1) BSIG-neu",
        "nim_text_excerpt": "...binnen 12 Stunden melden...",
        "directive_minimum": "Art. 23(4)(a) NIS2: 24-hour early warning",
        "candidate_category": "Substantive over-implementation — stricter reporting deadline",
        "verification_notes": "[VERIFY]",
        "provenance": { "analyst": "string", "timestamp": "..." }
      }
    ],
    "schema_validation": {
      "rules_checked": [
        "R1",
        "R2",
        "R3",
        "R4",
        "R5",
        "R6",
        "R7",
        "R8",
        "R9",
        "R10"
      ],
      "warnings": [],
      "blocked_emission": false
    },
    "authority_anchors": [
      "Joint Political Declaration of 28 September 2011 (OJ C 369, 17.12.2011, p. 14)",
      "Joint Political Declaration of 27 October 2011 (OJ C 369, 17.12.2011, p. 15)",
      "Better Regulation Toolbox 2023 Chapter 4",
      "TFEU Art. 260(3) — Commission v Belgium (Case C-543/17, ECLI:EU:C:2019:573)",
      "Council Resolution of 8 June 1993 (OJ C 166, 17.06.1993, p. 1)"
    ]
  }
}
```

### 3. AKN4EU XML stub (`<doc class="correlationTable">`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <doc name="correlationTable" class="correlationTable">
    <meta>
      <identification source="#legalcode-correlation-table-builder">
        <FRBRWork>
          <FRBRthis value="/akn/eu/doc/correlationTable/2022/2555/de/main"/>
          <FRBRuri value="/akn/eu/doc/correlationTable/2022/2555/de"/>
          <FRBRalias value="NIS2 ↔ Germany NIS2UmsuCG correlation table" name="shortTitle"/>
          <FRBRdate date="2024-10-17" name="directiveTranspositionDeadline"/>
          <FRBRauthor href="#legalcode"/>
          <FRBRcountry value="eu"/>
          <FRBRsubtype value="correlationTable"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/eu/doc/correlationTable/2022/2555/de/main/eng@/main"/>
          <FRBRuri value="/akn/eu/doc/correlationTable/2022/2555/de/eng@"/>
          <FRBRdate date="YYYY-MM-DD" name="versionDate"/>
          <FRBRauthor href="#legalcode-analyst"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
        <!-- FRBRManifestation omitted from stub; produced at serialisation time with format="application/akn+xml" -->
      </identification>
      <references source="#legalcode-correlation-table-builder">
        <TLCRef eId="dir_nis2"
                href="https://eur-lex.europa.eu/eli/dir/2022/2555/oj"
                showAs="NIS2 Directive (Directive (EU) 2022/2555)"/>
        <TLCRef eId="nim_de_nis2umsucg"
                href="https://www.recht.bund.de/eli/de/bgbl/[VERIFY]"
                showAs="NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz"/>
        <TLCRef eId="jpd_2011_september"
                href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:C:2011:369:0014"
                showAs="Joint Political Declaration 28 September 2011"/>
        <TLCRef eId="jpd_2011_october"
                href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:C:2011:369:0015"
                showAs="Joint Political Declaration 27 October 2011"/>
      </references>
      <classification source="#legalcode-correlation-table-builder">
        <keyword value="correlation-table" showAs="Correlation Table"/>
        <keyword value="transposition-notification" showAs="Transposition Notification"/>
        <keyword value="nis2" showAs="NIS2"/>
        <keyword value="cybersecurity" showAs="Cybersecurity"/>
      </classification>
    </meta>
    <preface>
      <p>Correlation Table — NIS2 Directive (Directive (EU) 2022/2555) ↔ Germany
        NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz (NIS2UmsuCG).</p>
    </preface>
    <mainBody>
      <table>
        <tr>
          <th><p>Directive provision (EN)</p></th>
          <th><p>NIM provision (DE)</p></th>
          <th><p>Pattern</p></th>
          <th><p>Notes</p></th>
        </tr>
        <tr eId="row_001">
          <td>
            <ref href="#dir_nis2/art_21.2.a">Art. 21(2)(a)</ref>
            <p>policies on risk analysis and information system security</p>
          </td>
          <td>
            <ref href="#nim_de_nis2umsucg/sec_30.2.1">§ 30(2) Nr. 1 BSIG-neu</ref>
            <p>Konzepte in Bezug auf die Risikoanalyse und Sicherheit von
              Informationssystemen</p>
          </td>
          <td><p>1-to-1</p></td>
          <td>
            <authorialNote marker="*" placement="bottom">
              <p>[VERIFY: pre-promulgation tracker — Linklaters NIS2 transposition
                tracker, [date]]. Language reconciliation EN-DE: "policies" → "Konzepte"
                (IATE-confirmed).</p>
            </authorialNote>
          </td>
        </tr>
        <!-- Additional rows for each directive operative atom -->
      </table>
    </mainBody>
  </doc>
</akomaNtoso>
```

**Documented choices for the AKN4EU `correlationTable` doc class extension:**

1. The `class="correlationTable"` attribute is a Legalcode-published convention; the
   public AKN4EU subschema does not currently prescribe a binding doc class for
   correlation tables.
2. `<TLCRef>` (Top Level Class Reference) is used to register the directive, the NIM,
   and the JPD authority anchors as resolvable identifiers within the table's
   reference space.
3. `<authorialNote>` carries per-row provenance (analyst, timestamp, source URL, and
   language reconciliation summary).
4. The FRBR identification block uses `subtype="correlationTable"` to distinguish
   this doc class from other AKN doc classes.
5. The `eId` values follow the pattern `row_NNN` for table rows; downstream LEOS
   ingesters can use these IDs as stable anchors.

These choices are recorded in the Glass Box for any institutional consumer that
needs to adapt or normalise the representation.

### 4. LegalRuleML satisfaction-assertion stub

LegalRuleML is not directly used to express a correlation between two acts — its
primary deontic vocabulary describes obligations, permissions, and prohibitions
within a single legal source. This skill therefore emits a _satisfaction-assertion_
stub: a `<lrml:Constitutive>` block expressing the assertion "directive Art X
obligation is satisfied by NIM provision Y", which a downstream policy-as-code
engine can use to chain the directive obligation to the operative national rule.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML
    xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
    xmlns:ruleml="http://ruleml.org/spec">
  <lrml:Source key="src_directive_nis2">
    <lrml:Reference refersTo="https://eur-lex.europa.eu/eli/dir/2022/2555/oj">
      <lrml:Description>NIS2 Directive (Directive (EU) 2022/2555)</lrml:Description>
    </lrml:Reference>
  </lrml:Source>
  <lrml:Source key="src_nim_de_nis2umsucg">
    <lrml:Reference refersTo="urn:de:bgbl:nis2umsucg:2024">
      <lrml:Description>NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz
        [VERIFY: pre-promulgation]</lrml:Description>
    </lrml:Reference>
  </lrml:Source>

  <!-- Directive obligation: Art. 21(2)(a) NIS2 — essential entity must maintain
       policies on risk analysis and information system security. -->
  <lrml:Prescriptive key="oblig_nis2_art_21_2_a">
    <lrml:hasSource keyref="src_directive_nis2"/>
    <ruleml:Rule>
      <ruleml:if><ruleml:Atom><ruleml:Rel>essentialEntity</ruleml:Rel><ruleml:Var>x</ruleml:Var></ruleml:Atom></ruleml:if>
      <ruleml:then>
        <lrml:Obligation>
          <ruleml:Atom><ruleml:Rel>maintainPolicy</ruleml:Rel><ruleml:Var>x</ruleml:Var><ruleml:Ind>riskAnalysisAndInformationSystemSecurity</ruleml:Ind></ruleml:Atom>
        </lrml:Obligation>
      </ruleml:then>
    </ruleml:Rule>
  </lrml:Prescriptive>

  <!-- NIM obligation: § 30(2) Nr. 1 BSIG-neu — wesentliche Einrichtung führt
       Konzept Risikoanalyse + Informationssystemsicherheit. (Same form as above
       with national rel/ind names.) -->
  <lrml:Prescriptive key="oblig_nim_de_sec_30_2_1">
    <lrml:hasSource keyref="src_nim_de_nis2umsucg"/>
    <!-- structurally parallel Rule with rel="fuehrt" / ind="konzeptRisikoanalyse..." -->
  </lrml:Prescriptive>

  <!-- Satisfaction assertion: directive Art. 21(2)(a) is satisfied by § 30(2) Nr. 1 -->
  <lrml:Constitutive key="satisfies_art_21_2_a">
    <ruleml:Atom>
      <ruleml:Rel>satisfies</ruleml:Rel>
      <ruleml:Ind keyref="oblig_nim_de_sec_30_2_1"/>
      <ruleml:Ind keyref="oblig_nis2_art_21_2_a"/>
    </ruleml:Atom>
    <lrml:appliesIn jurisdiction="DE"/>
    <lrml:hasStrength value="LIKELY"/>
  </lrml:Constitutive>
</lrml:LegalRuleML>
```

**Note**: this LegalRuleML stub is not a complete policy-as-code rendering of either
the directive or the NIM; it is a satisfaction-assertion bridge between the two,
designed for downstream engines that already carry the underlying obligation models.
The `<lrml:hasStrength>` slot mirrors the confidence level of the row.

### 5. Glass Box audit trail (YAML)

```yaml
glass_box:
  skill_name: "legalcode-eu-correlation-table-builder"
  schema_version: "1.0"
  assessment_date: "[YYYY-MM-DD]"
  analyst: "[Role — AI-assisted; must be validated by qualified EU/MS counsel]"
  operating_mode: "[Populated / Scaffold / Partial / Comparative]"
  legalcode_mcp: "[Connected at /tmp/legalcode-correlation-research.md / Not connected]"

  directive:
    short_title: "NIS2"
    celex: "32022L2555"
    eli: "https://eur-lex.europa.eu/eli/dir/2022/2555/oj"
    transposition_deadline: "2024-10-17"
    harmonisation_level: "minimum"
    eea_relevance: "deferred"

  member_state:
    iso_code: "DE"
    notifying_ministry: "BMI (Bundesministerium des Innern und für Heimat)"
    nim_short_title: "NIS2UmsuCG"
    nim_oj_reference: "BGBl. I [VERIFY]"
    nim_effective_date: "[YYYY-MM-DD]"
    transposition_status: "transposed_late"
    late_transposition_delta_days: "[N — NIM date − 2024-10-17]"

  granularity_decision:
    chosen: "article-paragraph-subparagraph"
    rationale: |
      Government persona; conformity assessment downstream requires per-subparagraph
      precision.

  language_reconciliation:
    - row_id: "R-001"
      term_at_risk: "policies"
      directive_versions_consulted: ["en", "de"]
      reconciled_meaning: 'EN "policies" → DE "Konzepte" (IATE-confirmed)'
    - row_id: "R-007"
      term_at_risk: "appropriate"
      directive_versions_consulted: ["en", "de", "fr"]
      reconciled_meaning: |
        EN "appropriate" / DE "geeignet" / FR "approprié" — CILFIT/EMU Tabac
        applied: reconciled in light of Art. 21(1) proportionality clause.

  schema_validation:
    rules_checked: ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"]
    warnings:
      - {
          rule: "R6",
          row_id: "R-014",
          message: "Only EN consulted; DE version not checked.",
        }
    blocked_emission: false

  rows_summary:
    {
      total: "[N]",
      operative: "[N]",
      no_transposition_required: "[N]",
      pre_existing_law: "[N]",
      deferred: "[N]",
    }

  coverage_gaps:
    total: "[N]"
    by_severity: { CRITICAL: "[N]", HIGH: "[N]", MEDIUM: "[N]", LOW: "[N]" }
    examples:
      - directive_article: "Art. 21(2)(j)"
        severity: "CRITICAL"
        rationale: "[Specific finding]"
        adversarial_3pass:
          pass_1_mapping_integrity: "[Re-search outcome]"
          pass_2_compensating_provisions: "[Pre-existing law search outcome]"
          pass_3_enforcement_reality: "[Comparable LFN cited or [VERIFY]]"

  over_coverage_flags:
    total: "[N]"
    by_category:
      {
        substantive_over_implementation: "[N]",
        scope_extension: "[N]",
        earlier_effective_date: "[N]",
        stricter_penalty: "[N]",
        additional_procedural_step: "[N]",
        goldplated_definition: "[N]",
        belt_and_braces: "[N]",
      }

  authority_anchors:
    - "Joint Political Declaration of 28 September 2011 (OJ C 369, 17.12.2011, p. 14)"
    - "Joint Political Declaration of 27 October 2011 (OJ C 369, 17.12.2011, p. 15)"
    - "Better Regulation Toolbox 2023, Chapter 4"
    - "TFEU Art. 260(3) — Commission v Belgium (Case C-543/17, ECLI:EU:C:2019:573)"
    - "Council Resolution of 8 June 1993 (OJ C 166, 17.06.1993, p. 1)"
    - "Reg. 1/1958; CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95 — language regime"

  assumptions:
    - "Pre-promulgation source consulted; final BGBl. text not yet published."
    - "Granularity choice ratified by user."

  limitations:
    - "AKN4EU correlationTable doc class extension is Legalcode-published, not a binding AKN4EU schema element."
    - "LegalRuleML stub is a satisfaction-assertion bridge, not a complete obligation rendering."

  reviewer_note: |
    AI-assisted draft. All rows carrying [VERIFY] markers must be validated against
    the authoritative national official journal text and against the EUR-Lex
    consolidated directive text before submission to the Commission MNE workflow.
    All CRITICAL coverage gaps and over-coverage flags must be reviewed by qualified
    Member State counsel before regulatory submission, infringement proceedings, or
    board reporting.
```

### 6. Commission DOCX template (mock-up — government persona only)

The Commission DOCX is a render-only artefact; the canonical structured form is the
JSON above. The DOCX mock-up uses the two-column layout with the metadata block at
the top, the row table in the body, and the authority-anchors footer. The actual
DG-specific template must be obtained from the Member State Notification (MNE)
workflow before any final submission.

**Header block (MS-completed):**

```
Member State: [Germany / Federal Republic]
Notifying ministry: [Bundesministerium des Innern und für Heimat]
Contact: [Name, email, phone]
Directive: [NIS2 Directive — Directive (EU) 2022/2555]
NIM: [NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz]
NIM OJ ref: [BGBl. I [VERIFY]]
NIM effective date: [YYYY-MM-DD]
Transposition deadline (directive): 17 October 2024
Notification date: [YYYY-MM-DD]
Procedural language: EN (directive column) / DE (NIM column)
```

**Row table** — populated from the JSON `rows` array.

**Footer**:

```
Method of transposition: [direct adoption / amendment to existing act / combination]
Constitutional approval flag: [N/A for EU-27 / [Storting / Althingi / Landtag] approval pending for EEA EFTA]
Joint Political Declarations cited: 28 September 2011 (OJ C 369, p. 14); 27 October 2011 (OJ C 369, p. 15)
Better Regulation Toolbox 2023 Chapter 4 referenced.
```

---

## Localization Notes

When adapting this skill for a specific Member State or EEA EFTA State:

1. **National citation format**: replace the right-column citation format with the
   national convention (BGBl., JORF, GU, BOE, SFS, Lovtidende, Staatsblad, etc.) and
   use the country-specific parliament API for pre-promulgation tracking (full list
   in the shared EU legislative-data reference pack).
2. **Procedural language**: most MS notify in English; some notify in their national
   language with an accompanying English translation. Verify with the MS Permanent
   Representation before fixing the procedural language in the table header.
3. **DG template variant**: confirm with the relevant DG (CONNECT, FISMA, ENV,
   EMPL, JUST, etc.) that the DOCX layout matches their current template.
4. **EEA EFTA pillar (IS / NO / LI)**: destination is ESA Internal Market Affairs,
   not the Commission. Add Art. 31 SCA monitoring framing and Art. 102/103 EEA
   Joint Committee Decision sequencing in the metadata block; mark deferred rows
   under Art. 103 EEA reservation. Coordinate with `legalcode-eea-incorporation-tracker`.
5. **Multilingual NIMs** (e.g. Belgium FR/NL, Cyprus EL/EN, Finland FI/SV, Malta
   MT/EN): the right column may need both language versions side by side or in
   alternating rows; document the choice in the Glass Box.
6. **Late-transposition MS**: if the NIM enters into force after the deadline, flag
   the late-transposition delta in the metadata block and treat outstanding coverage
   gaps at the deadline date as CRITICAL severity.

---

## Provenance

Created by Legalcode (2026-04-28). Original synthesis based on:

- **EU primary law and EEA primary text**: TFEU Art. 288 (instrument hierarchy;
  ELI `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`); Art. 4(3)
  (sincere cooperation); Arts. 258, 260(2), 260(3) (infringement and pecuniary
  penalty); Art. 7, 102, 103 EEA (incorporation, JCD, constitutional reservation);
  Art. 31 SCA (ESA monitoring).

- **Joint Political Declarations on explanatory documents** — legal basis of the
  correlation-table requirement: 28 September 2011 (Member States + Commission)
  (OJ C 369, 17.12.2011, p. 14); 27 October 2011 (Parliament + Council + Commission)
  (OJ C 369, 17.12.2011, p. 15).

- **Council Resolution of 8 June 1993** on the quality of drafting of Community
  legislation (OJ C 166, 17.06.1993, p. 1) — historical antecedent.

- **Methodology**: Better Regulation Toolbox 2023, Chapter 4
  (`https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`).

- **Multilingualism**: Reg. 1/1958
  (`https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`); _CILFIT_ (C-283/81,
  ECLI:EU:C:1982:335); _Codan_ (C-236/97, ECLI:EU:C:1998:208); _EMU Tabac_
  (C-296/95, ECLI:EU:C:1998:152).

- **CJEU case law on transposition technique and infringement**: _Commission v
  Belgium_ (C-543/17, ECLI:EU:C:2019:573 — first Art. 260(3) application);
  _Commission v Italy_ (C-129/00, ECLI:EU:C:2003:656 — transposition by permission
  where directive imposes obligation); _Commission v United Kingdom_ (C-484/04,
  ECLI:EU:C:2006:526 — same principle); _Casa Fleischhandels-GmbH v BALM_ (215/88,
  ECLI:EU:C:1989:331) and _Nilsson, Hagelgren and Arrborn_ (C-162/97,
  ECLI:EU:C:1998:554 — recitals are interpretive, not operative).

- **Standards**: Akoma Ntoso (OASIS LegalDocML 1.0, 2018) base schema for AKN4EU
  (`https://op.europa.eu/o/opportal-service/euvoc-download-handler?cellarURI=http%3A%2F%2Fpublications.europa.eu%2Fresource%2Fdistribution%2Fcdm%2F20210701-0%2Fzip%2Fcdm_20210701-0.rdf.zip&fileName=cdm.zip`);
  ELI (`https://eur-lex.europa.eu/eli-register/technical_information.html`); ECLI;
  CELEX; LegalRuleML (OASIS, 2021;
  `https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`).

- **Sources / data feeds**: EUR-Lex Cellar SPARQL
  (`https://publications.europa.eu/webapi/rdf/sparql`); EUR-Lex web service; N-Lex
  (`https://eur-lex.europa.eu/collection/n-law/mne.html`); OEIL; CURIA; EEA-Lex;
  IATE (`https://iate.europa.eu/`); Single Market Scoreboard
  (`https://single-market-scoreboard.ec.europa.eu/`); national official journals
  and parliament APIs (see Step 4a and the shared EU legislative-data reference
  pack).

- **Worked-example sources (NIS2 ↔ Germany NIS2UmsuCG)**: NIS2 Directive
  (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022, p. 80,
  ELI `https://eur-lex.europa.eu/eli/dir/2022/2555/oj`); Linklaters NIS2
  transposition tracker (Berlin office) — practitioner source; **all rows flagged
  [VERIFY] pending publication of the NIS2UmsuCG in the Bundesgesetzblatt**;
  Bundestag dip portal (`https://dip.bundestag.de`); BfDI guidance on NIS2
  supervision [VERIFY current edition].

- **Gold-plating typology references** (consumed by sibling skill F): High Level
  Group on Administrative Burdens, _Final report on the better application of EU
  directives_ (2014;
  `https://ec.europa.eu/futurium/en/system/files/ged/hlg_16_0008_00_conclusions_and_recomendations_on_goldplating_final.pdf`);
  UK BIS, _Gold-Plating Review_ (2013); CFA Society Poland, _Gold-plating in EU
  Capital Markets_ (2024).

All statutory and regulatory references carry hallucination risk and should be
verified against authoritative sources (EUR-Lex, CURIA, national official journals)
before use in regulatory submissions, infringement proceedings, or board reporting.
The 24 official EU language versions of every act are equally authentic;
reconcile divergent versions before relying on any single language for a definitive
interpretation.
