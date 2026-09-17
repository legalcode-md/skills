---
name: legalcode-eu-transposition-tracker
description: Maintains the per-Member-State implementation matrix for any EU directive across the 27 EU
  Member States and (where the act is EEA-relevant) the 3 EEA EFTA states (Iceland, Norway, Liechtenstein).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Maintains the per-Member-State implementation matrix for any EU directive across the 27 EU Member States and (where the act is EEA-relevant) the 3 EEA EFTA states (Iceland, Norway, Liechtenstein). Tracks for each MS-directive pair: the National Implementing Measure (NIM) citation in national identifier format (BGBl, JORF, SFS, Dz.U., Stjtíð. A, etc.), transposition status (planned / draft / partial / complete / overdue), notification status to the Commission under Art. 260(3) TFEU, the directive transposition deadline, and links to the national authoritative source (parliament bill page, official journal entry, ministry portal). Anchored on TFEU Art. 288(3) (the binding-as-to-result, free-as-to-form rule for directives), TFEU Art. 260(3) (penalty payments at first referral for failure to notify transposition — the Lisbon innovation first applied in *Commission v Belgium*, Case C-543/17, ECLI:EU:C:2019:573, OJ C 270/15, 12.8.2019), the Commission's Better Regulation Toolbox 2023 Chapter 4 completeness-check methodology, the Single Market and Competitiveness Scoreboard transposition-deficit methodology, the ESA Internal Market Scoreboard for the EFTA pillar under Art. 31 SCA, and the N-Lex / MNE national execution measures database. Designed around the NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022, p. 80), CSRD Directive (Directive (EU) 2022/2464, CELEX 32022L2464), CSDDD Directive (Directive (EU) 2024/1760, CELEX 32024L1760, transposition deadline 26 July 2026), and the Whistleblower Protection Directive (Directive (EU) 2019/1937, CELEX 32019L1937) as worked examples — but is directive-agnostic. Operating modes: government self-assessment; legal-firm comparative client briefing; company operational-deadline planning; trade federation pre-deadline engagement scoreboarding. Produces a canonical JSON matrix consumed by `legalcode-eu-correlation-table-builder`, `legalcode-eu-conformity-assessment`, `legalcode-eu-gold-plating-detector`, and `legalcode-eu-infringement-procedure-tracker`, plus AKN4EU per-MS NIM document references, a LegalRuleML aggregate-assertion stub, a Markdown 30-row comparison table, and a Glass Box audit trail with per-cell provenance. Jurisdictional scope: EU-27 plus 3 EEA EFTA states (IS, NO, LI) when the directive is EEA-relevant.


# Legalcode EU Transposition Tracker

> **Disclaimer**: This skill provides a framework for AI-assisted EU directive
> transposition tracking. It does not constitute legal advice and does not create an
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

This skill builds and maintains the **per-Member-State implementation matrix** for a
given EU directive. The matrix is the single artefact that converts an abstract
EU-level obligation register into the concrete national-law landscape that companies,
firms, ministries and federations actually have to operate against.

A directive is, by Art. 288(3) TFEU, "binding, as to the result to be achieved, upon each
Member State to which it is addressed, but [leaves] to the national authorities the choice
of form and methods." The transposition matrix is the systematic record of how each MS
has exercised that choice — or has failed to. It is the document the Commission keeps for
its completeness check and conformity check (Better Regulation Toolbox 2023 Ch. 4); the
document the Single Market and Competitiveness Scoreboard aggregates across all directives
to compute the **transposition deficit** (the percentage of MS-directive pairs whose
National Implementing Measures have not been notified to the Commission by the deadline);
the document law firms publish as comparative trackers; and the document a federation
uses to prioritise where to engage during the transposition window.

The matrix is **not** a conformity assessment. It records _whether_ and _with what NIM_,
not _whether the NIM correctly transposes the underlying directive obligations_ — that
is the job of the sibling skill `legalcode-eu-conformity-assessment`. It is also not a
correlation table (the Commission-format Article-to-NIM-provision crosswalk that DG-level
self-assessments require) — that is `legalcode-eu-correlation-table-builder`. The matrix
is the input that allows those downstream artefacts to be built; it answers
**"who, when, with what instrument, and notified or not"**, not **"correctly transposed
on the merits."**

**Covers:**

- Per-MS National Implementing Measure (NIM) discovery for any directive: primary
  legislation, secondary regulation, both, or split across multiple acts
- Status classification under the seven-tier taxonomy: not-yet-planned / planned / draft /
  partial / complete / overdue / withdrawn
- Notification status to the Commission (notified / partially notified / not notified)
  under the Art. 260(3) TFEU regime, including correlation-table requirement and the
  declaratory commitment that notification triggers
- Transposition deadline computation: the directive's stated transposition date, plus any
  staggered or delayed deadlines for specific provisions
- EEA-pillar coordination: when the directive is EEA-relevant, tracking the Joint Committee
  Decision adoption status as the precursor to IS / NO / LI domestic incorporation
  (handed off to and from `legalcode-eea-incorporation-tracker`)
- Transposition-deficit calculation per the Single Market and Competitiveness Scoreboard
  methodology (% of MS-directive pairs notified by deadline)
- Risk scoring per MS-directive pair: overdue + Art. 260(3) exposure; pre-deadline + risk
  of being late; historical-compliance weighting
- Authoritative-source provenance for every cell of the matrix: source URL, fetch date,
  evidence quote
- Output in four standards-aligned formats: Markdown, canonical JSON, AKN4EU XML stubs
  per MS NIM, LegalRuleML aggregate-assertion stub
- Glass Box audit trail with per-cell evidence so that the matrix is reproducible and
  defensible against regulator, board, or partner challenge

**Does not:**

- Run the per-Article conformity check — verdict per provision (correct / partial /
  incorrect / not transposed). That is `legalcode-eu-conformity-assessment`.
- Build the Commission-format two-column correlation table (directive Article ↔ NIM
  provision). That is `legalcode-eu-correlation-table-builder`.
- Detect gold-plating (where the NIM exceeds the EU minimum). That is
  `legalcode-eu-gold-plating-detector`.
- Track TFEU 258 / 260 infringement procedures or ESA Art. 31 SCA cases. That is
  `legalcode-eu-infringement-procedure-tracker`.
- Track the EEA Joint Committee Decision pipeline itself. That is
  `legalcode-eea-incorporation-tracker`.
- Extract the obligation register from the directive — it consumes one. That is the
  foundation skill `legalcode-eu-directive-analyzer`.
- Provide legal advice on whether a specific NIM correctly transposes a specific
  obligation; this is a matrix-keeping skill, not a merits-review skill.

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes /
produces the following artefacts:

- **Consumes**: obligation register from `legalcode-eu-directive-analyzer` (the canonical
  list of articles + obligations a directive imposes on MS, plus directive-level metadata
  including CELEX, ELI, transposition deadline, EEA relevance flag).
- **Produces**: per-MS implementation matrix (canonical JSON schema defined below)
  consumed by `legalcode-eu-correlation-table-builder` (per-MS NIM citation feeds the
  right-hand column of the correlation table); `legalcode-eu-conformity-assessment` (per-MS
  NIM is what gets compared to the directive obligations); `legalcode-eu-gold-plating-detector`
  (compares NIM substance to the directive baseline to flag national over-implementation);
  `legalcode-eu-infringement-procedure-tracker` (overdue MS + Art. 260(3) exposure feed
  the LFN / reasoned-opinion timeline). When the directive is EEA-relevant, the EFTA
  pillar (IS, NO, LI) is coordinated with `legalcode-eea-incorporation-tracker`.

Sibling skills (use whichever is appropriate for the user's stage in the lifecycle):

- `legalcode-eu-directive-analyzer` — extracts the obligation register from a directive
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix (this skill)
- `legalcode-eu-correlation-table-builder` — directive-to-NIM correlation table
- `legalcode-eu-conformity-assessment` — per-article transposition verdict
- `legalcode-eu-gold-plating-detector` — flags national over-implementation
- `legalcode-eea-incorporation-tracker` — EEA Joint Committee Decision tracking
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 procedure timeline

The shared reference pack (CELEX/ELI/ECLI playbook, MS identifier playbook,
official-journal map, EEA glossary) lives co-located with the foundation skill at
`references/eu-legislative-data/`.

See [shared EU legislative-data pack](references/eu-legislative-data/).

---

## Jurisdiction and Governing Law

This skill operates across the European Union and (when the directive is EEA-relevant)
the EFTA pillar of the European Economic Area.

**EU primary law foundation:**

- **Art. 288(3) TFEU** — directives are binding as to result, leaving choice of form and
  methods to MS. Authoritative ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`. This is the
  constitutional basis for the very concept of "transposition" — without Art. 288(3)
  there would be no per-MS NIM, just direct application as for regulations.
- **Art. 291(1) TFEU** — Member States adopt all measures of national law necessary to
  implement legally binding Union acts. This is the implementation-duty companion to the
  transposition duty in Art. 288(3).
- **Art. 4(3) TEU** — principle of sincere cooperation; obliges MS to take "any
  appropriate measure, general or particular," to ensure fulfilment of obligations
  arising from the Treaties or Union acts. Cited routinely in late-transposition
  infringement proceedings.
- **Art. 258 TFEU** — Commission's infringement procedure for failure to fulfil a Treaty
  obligation. The classic letter-of-formal-notice → reasoned-opinion → CJEU-referral
  ladder for _all_ infringement types, including failure to transpose on time.
- **Art. 260(2) TFEU** — penalty payment after non-compliance with a Court judgment under
  Art. 258, requiring a second Commission referral for the financial penalty.
- **Art. 260(3) TFEU** — **first-referral penalty for failure to notify transposition of a
  legislative directive** (Lisbon innovation, in force 1 December 2009; first applied in
  _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573). This is the single most
  important provision for this skill: the matrix's "notified to Commission" column is the
  variable that triggers Art. 260(3).
- **Art. 4(3) TEU + Art. 17(1) TEU** — Commission's role as "guardian of the Treaties,"
  the mandate behind the completeness check.

**EU case-law foundation:**

- **_Commission v Belgium_**, Case C-543/17, ECLI:EU:C:2019:573 — first application of
  Art. 260(3); CJEU imposed a EUR 5,000-per-day periodic penalty payment. Confirms that
  Art. 260(3) operates _at the first referral_ and does not require a prior Art. 258
  judgment, which is its Lisbon innovation. Cite this case in any matrix where the
  notification column shows "not notified" past the deadline.
- **_Commission v Italy_**, Case 22/87, ECLI:EU:C:1989:45 — early authority that mere
  administrative practice is insufficient for transposition; transposition requires
  binding national legal measures. Relevant when the matrix records "informal
  guidance" as the only national instrument.
- **_Commission v Germany (TSE)_**, Case C-518/07, ECLI:EU:C:2010:125 — transposition
  must be "complete, clear, and precise" so that data subjects / addressees can know
  the full extent of their rights. Cited where partial transposition is recorded.
- **_Francovich_**, Joined Cases C-6/90 and C-9/90, ECLI:EU:C:1991:428 — MS liability for
  damages caused by failure to transpose a directive correctly and on time. Relevant
  context for "overdue" rows in the matrix.
- **_Marleasing_**, Case C-106/89, ECLI:EU:C:1990:395 — duty of conforming interpretation;
  national courts must interpret pre-existing national law in light of directives even
  before transposition. Relevant for "no NIM but pre-existing national law plausibly
  conforms" edge cases.
- **_CILFIT_**, Case C-283/81, ECLI:EU:C:1982:335 — equal authenticity of all 24 EU
  language versions. Apply when the directive's transposition obligation reads
  differently across language versions.

**EEA pillar foundation (when the directive is EEA-relevant):**

- **Art. 7 EEA** — incorporated EU acts must be made part of internal legal order of
  the EFTA states. Direct analogue of Art. 288(3) TFEU on the EFTA side, but operating
  through Joint Committee Decisions (JCDs).
- **Art. 102 EEA** — Joint Committee Decision procedure for incorporating new EU
  legislation into the EEA Annexes.
- **Art. 103 EEA** — constitutional reservations / parliamentary approval suspension;
  delays the entry into force of a JCD until the constitutional reservation is lifted.
  Critical for IS and NO whose parliaments must approve EEA-relevant acts with
  significant national-law impact (e.g., GDPR, NIS2).
- **Art. 31 SCA (Surveillance and Court Agreement)** — ESA monitoring mandate, the
  EFTA-pillar analogue of Art. 258 TFEU. ESA brings infringement actions before the
  EFTA Court when EFTA states fail to transpose incorporated acts. ESA Internal Market
  Scoreboard tracks the EFTA-pillar transposition deficit.

**Methodology references:**

- **Better Regulation Toolbox 2023, Chapter 4** (Compliance, Implementation and
  Preparing Proposals): Commission's published methodology for the **completeness check**
  (does the NIM cover the entire directive at all?) and the **conformity check** (does
  the NIM substantively transpose each provision?). The completeness check is the
  threshold inquiry that precedes any conformity assessment, and is what the matrix's
  "notified" column enables. Source:
  `https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`.
- **Single Market and Competitiveness Scoreboard transposition methodology** —
  transposition deficit is computed as the percentage of directives in force whose
  national transposition measures have not been notified to the Commission by the
  transposition deadline; the long-standing political target was 1.0% but the more
  recent emphasis is on per-MS performance and infringement reduction. Source:
  `https://single-market-scoreboard.ec.europa.eu/`.
- **ESA Internal Market Scoreboard** — EFTA-pillar analogue published twice yearly by
  EFTA Surveillance Authority covering transposition performance of IS, NO and LI.
  Source: `https://www.efta.int/`.
- **N-Lex / MNE database** (national execution measures) — the authoritative record of
  what each MS has notified to the Commission as transposition.
  Source: `https://eur-lex.europa.eu/collection/n-law/mne.html`.

**National-law sources (high level — see "Member State and EEA EFTA State Coverage"
section below for the full table):**

- Each MS publishes its laws in an official journal (BGBl, JORF, GU, Dz.U., etc.) and
  most expose machine-readable parliament data (Bundestag DIP, Assemblée nationale
  data API, Riksdagen API, Storting API, Althingi).

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

- Persona: Legal firm (comparative client briefing)
- Scope: EU-27 only (do not auto-add EFTA pillar unless directive is EEA-relevant)
- Refresh mode: Greenfield (build matrix from scratch rather than updating prior matrix)
- Source preference: Authoritative national sources (parliament, official journal) with
  published-tracker fallback flagged as "secondary"
- Status taxonomy: Seven-tier (not-yet-planned / planned / draft / partial / complete /
  overdue / withdrawn) — the default

---

## Workflow

### Step 1: Accept Input

Accept any of the following input shapes:

- **Target-directive identifier**: CELEX (e.g. `32022L2555` for NIS2), ELI URL
  (`https://eur-lex.europa.eu/eli/dir/2022/2555/oj`), or short title with year. The CELEX
  is canonical; if only a short title is given, the skill must resolve to a CELEX before
  proceeding.
- **Pre-built obligation register** from `legalcode-eu-directive-analyzer`. If supplied,
  consume the directive metadata block (CELEX, ELI, transposition deadline(s),
  EEA-relevance flag, addressee categories) without re-fetching.
- **Prior matrix in canonical JSON** for an update / refresh run. The skill diffs against
  the prior matrix and emits a delta plus the new full matrix.
- **Persona description triggering a new exercise** (e.g. "We are the Belgian Federal
  Public Service Justice and we need a self-assessment of NIS2 transposition status
  relative to peer MS").

Minimum context to proceed:

- Directive CELEX (or unambiguous resolution thereto)
- Persona / operating mode (CLARIFY in Step 2)
- Scope: EU-27 only, or EU-27 + 3 EFTA states (CLARIFY in Step 4)

If no input is provided, ask the user for at minimum the target directive.

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

**Persona-specific output emphasis (this skill specifically):**

| Persona          | Primary matrix view                                                                                                               | Secondary outputs                                                                                                             | Risk-scoring weight                                                                                                                           |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Government       | Own-MS row in deep detail; peer MS for benchmarking; Commission-notification readiness                                            | Self-assessment of own row vs. completeness checklist (Better Regulation Toolbox Ch. 4); Art. 260(3) self-exposure assessment | Heavy weight on "notified vs. not notified" because Art. 260(3) penalty triggers off this column                                              |
| Legal firm       | Comparative cross-MS table sorted by status tier; visual heat-map of status and deadline-to-go                                    | Client-facing briefing with executive summary; per-MS deep dive on request                                                    | Balanced — clients ask both "which MS are late" (overdue + Art. 260(3)) and "where are surprises likely" (pre-deadline + historical lateness) |
| Company          | Operational deadline calendar per MS where the company operates; per-MS NIM citation only for those MS                            | Operational change checklist keyed to NIM effective dates                                                                     | Heavy weight on operational deadline (effective date of the NIM) rather than transposition deadline                                           |
| Trade federation | Pre-deadline engagement opportunity scoreboard: which MS are still in "draft" or "planned" status during the transposition window | Position-paper scaffolding noting comparative MS approaches and gold-plating signals                                          | Heavy weight on "pre-deadline draft" (engagement opportunity) and historical gold-plating pattern                                             |

The matrix data structure is the same across personas — what differs is the surface
presentation and the risk-scoring weights. Step 8 onwards branches on persona; Steps 3–7
are common.

⟁ CLARIFY — Operating Mode

In addition to persona, identify the operating mode within that persona:

1. **Greenfield matrix build** — no prior matrix; build from scratch.
2. **Update / refresh** — prior matrix provided; identify what has changed.
3. **Pre-deadline scan** — directive transposition deadline is in the future; matrix
   focuses on planning / drafting / consultation activity per MS rather than
   already-adopted NIMs.
4. **Post-deadline audit** — transposition deadline has passed; matrix focuses on overdue
   MS and Commission notification gaps, with Art. 260(3) exposure callout.
5. **Single-MS deep dive** — full matrix produced for completeness, but most analytical
   weight on one MS (typically the user's own).

**Why this matters**: A pre-deadline scan does not flag any MS as "overdue" because the
deadline has not yet passed; a post-deadline audit treats every "not notified" cell as
red. The same matrix data has different colouring depending on mode.

### Step 3: Resolve the Directive

If an obligation register from `legalcode-eu-directive-analyzer` was supplied, consume
its directive metadata block:

```yaml
directive_metadata:
  celex: "32022L2555"
  eli: "https://eur-lex.europa.eu/eli/dir/2022/2555/oj"
  short_title: "NIS2 Directive"
  formal_title: "Directive (EU) 2022/2555 of 14 December 2022 on measures for a high common level of cybersecurity across the Union"
  oj_reference: "OJ L 333, 27.12.2022, p. 80"
  in_force_date: "2023-01-16"
  transposition_deadline: "2024-10-17"
  staggered_deadlines: []
  eea_relevance: "pending JCD assessment"
  legal_basis: "Art. 114 TFEU"
  addressees: ["Member States"]
```

If no obligation register is supplied, fetch the directive metadata directly:

1. Resolve the CELEX from the input (use ELI if provided; resolve short-title via
   EUR-Lex search).
2. Fetch the OJ entry to confirm the formal title, OJ reference, and language coverage.
3. Read the directive's transposition article (typically the second-to-last article;
   for NIS2 this is Art. 41) to extract:
   - Headline transposition deadline.
   - Any provision-specific staggered deadlines.
   - Any optional later application dates conditional on national choice.
4. Read the directive's EEA-relevance recital (typically the final recital in the
   preamble) to flag whether the act is EEA-relevant. If yes, the EFTA pillar enters
   scope; if not, only the EU-27.
5. Note the legal basis (the TFEU article cited in the citation block — Art. 114, Art.
   53(1), Art. 50, etc.). Legal basis affects whether the directive is "legislative" in
   the sense of Art. 289 TFEU; **only legislative directives engage Art. 260(3) TFEU**,
   so this is the data point that determines whether non-notification can trigger a
   first-referral penalty payment.

### Step 4: Establish Member State Scope

⟁ CLARIFY — Member State Scope

A "directive" applies, by Art. 288(3) TFEU, only to the Member States to which it is
addressed. In practice, EU directives are addressed to all 27 EU MS. EEA EFTA states
(Iceland, Norway, Liechtenstein) are not bound by EU directives directly — they are
bound only by acts that have been incorporated into the EEA Agreement via Joint
Committee Decision under Art. 102 EEA. So the right scope depends on:

1. **EU-27 only**: Default for all directives. The matrix has 27 rows.
2. **EU-27 + 3 EFTA**: If the directive is EEA-relevant _and_ a Joint Committee
   Decision has been adopted. The matrix has 30 rows. For each EFTA row, the analogue
   of "transposition" is "domestic incorporation following the JCD" (and any
   constitutional-reservation suspension under Art. 103 EEA).
3. **Subset**: The user wants only specific MS rows (e.g., the company operates in
   six MS). Always retain the full 27 (or 30) for the canonical JSON; subset only the
   surface presentation.

**Why this matters**: Including the EFTA pillar without an adopted JCD produces a
misleading matrix because there is no domestic-implementation duty in IS / NO / LI
yet — only an EEA-pillar processing pipeline tracked by `legalcode-eea-incorporation-tracker`.
Conversely, omitting the EFTA pillar for an EEA-relevant directive that has been
incorporated misses three rows that companies and firms actually need.

**Coordinate with `legalcode-eea-incorporation-tracker`**: if the directive is flagged
EEA-relevant in Step 3, hand off the EEA-pillar status query to that skill and consume
its output. If the JCD has been adopted, include IS / NO / LI in the matrix; if not,
exclude them (and note in Glass Box that the EFTA pillar will become trackable once the
JCD is adopted). If the JCD has been adopted _but_ a constitutional reservation is in
force in IS or NO, mark that row as "JCD adopted, Art. 103 EEA reservation pending"
rather than as "transposition pending."

### Step 5: Per-MS Status Discovery

For each MS row in scope, populate the following data points:

1. **NIM identification**: the National Implementing Measure(s) the MS has adopted (or
   is drafting) to transpose this directive. NIMs may be:
   - A single primary act (most common; e.g., a national law replicating the directive
     structure).
   - A primary act plus secondary regulation (common where the directive includes
     technical standards delegated to executive bodies).
   - A bundle of amending acts touching multiple existing codes (common in MS with
     codified law, e.g., DE amending several BGBl laws to transpose one directive).
   - Pre-existing legislation deemed already to transpose (rare; requires Art. 4(3) TEU
     justification and is contested by Commission completeness check, see _Commission v
     Italy_ C-22/87).

2. **NIM citation in national identifier format**:
   - DE: BGBl. Teil I, Jahrgang, Nummer, Seite (e.g., "BGBl. I 2024, Nr. 44, S. 1532").
   - FR: JORF n°YYYY/N du DD MMMM YYYY (e.g., "JORF n°0245 du 19 octobre 2024 texte n° 3").
   - IT: GU Serie Generale n. NNN del DD-MM-YYYY.
   - ES: BOE núm. NNN, de DD MMMM YYYY (e.g., "BOE núm. 252, de 19 octubre 2024").
   - PL: Dz.U. YYYY poz. NNNN.
   - SE: SFS YYYY:NNNN.
   - DK: LOV nr NNNN af DD/MM/YYYY (with Lovtidende reference).
   - FI: SäädK NNNN/YYYY (Sähköinen Säädöskokoelma).
   - IS: Stjórnartíðindi A-deild, lög nr. NN/YYYY (e.g., "lög nr. 90/2018" for the
     Icelandic GDPR transposition).
   - NO: LOV-YYYY-MM-DD-NN (Lovdata identifier).
   - LI: LGBl. YYYY Nr. NNN.
   - For all 30 MS / EFTA rows, see "NIM Citation Format" section below for the
     authoritative format and the ELI national namespace where available.

3. **National-source URL**: parliament bill page, official journal entry, ministry
   portal, or Lovdata-equivalent. Prefer the official-journal entry as authoritative;
   fall back to parliament bill page if the OJ entry is paywalled or not yet available
   (common in the days between adoption and OJ publication).

4. **Adoption / signing date**: the date the legislature adopted (or the executive
   signed, as locally relevant) the NIM. Distinguish from "publication date" (when it
   appears in the OJ) and "entry into force" (when it becomes binding) and "application
   date" (when its substantive provisions begin to apply, which may be later than entry
   into force).

5. **Effective / application date**: the date from which the NIM substantively applies.
   This is the date the company persona cares about most, as it is the operational
   deadline — not the transposition deadline.

6. **Coverage scope of the NIM**: full directive, or a partial / specific-chapter
   transposition? Many MS transpose a directive in stages where the directive itself
   has staggered application dates.

**Discovery method (in priority order):**

1. **N-Lex / MNE database** — the Commission's authoritative record of notified national
   transposition measures. If the MS has notified, the NIM appears in N-Lex with the
   official-journal reference. Source:
   `https://eur-lex.europa.eu/collection/n-law/mne.html`. Use the MNE search filtered by
   directive CELEX to get the canonical MS list of notified measures.
2. **EUR-Lex national law search** — for each MS, the EUR-Lex "national law" view shows
   measures notified as transposing the directive. This is a cross-check against MNE.
3. **National parliament APIs** — for MS with machine-readable parliament data
   (Riksdagen, Storting, Folketinget, Bundestag DIP, Assemblée nationale, Althingi), query
   for bills referencing the directive's CELEX or short title. This catches drafts and
   bills in committee that have not yet been adopted, and so cannot yet be in MNE.
4. **National official-journal search** — for MS without rich parliament APIs, search the
   national OJ for the directive's short title or CELEX (most national OJs include
   citation to the transposed directive in the explanatory memorandum or recital block).
5. **Legalcode `search_laws` tool**, where available, filtered to the MS jurisdiction
   and the directive subject area, as a cross-check.
6. **Published trackers** (Linklaters NIS2 tracker, Ropes & Gray CSDDD tracker,
   Herbert Smith Freehills DORA tracker, etc.) as **secondary sources only**. These are
   high-quality but not authoritative; flag any cell sourced primarily from a published
   tracker with `source_tier: "secondary-tracker"` and surface it in the Glass Box.

If the discovery yields **no NIM** for a MS:

- Before the deadline: status = "planned" (if any draft or consultation evidence exists)
  or "not-yet-planned" (if no draft / consultation / parliamentary motion is found).
- After the deadline: status = "overdue" and notification = "not notified".

If the discovery yields **a draft but no adopted NIM**:

- Status = "draft" if the draft is in the national legislative pipeline (committee,
  consultation, government bill stage).
- Mark adoption_date as null and effective_date as null.

If the discovery yields **a NIM that covers only some chapters of the directive**:

- Status = "partial".
- Record the scope-of-coverage explicitly in the matrix (which chapters / articles are
  covered, which are not).
- Notification status may be "partially notified" if the MS has notified what exists.

### Step 6: Per-MS Status Classification

Apply the seven-tier status taxonomy. Definitions are normative and must be applied
consistently across the matrix.

| Status              | Definition                                                                                                                                                                                                                                                                       | Required evidence                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **not-yet-planned** | No public evidence of a draft, consultation, parliamentary motion, or ministerial roadmap. The MS has not begun transposition work that is publicly visible.                                                                                                                     | Negative evidence: search of parliament API + national OJ + ministry website returns no result; absence in MNE.                          |
| **planned**         | A public roadmap, public consultation, or parliamentary motion exists but no draft text. Could include a published timetable from the responsible ministry.                                                                                                                      | Positive evidence: ministry roadmap URL, public consultation URL, or parliament motion record.                                           |
| **draft**           | A draft NIM text exists in the national legislative pipeline (government bill, committee bill, consultation draft). Not yet adopted.                                                                                                                                             | Positive evidence: bill URL, draft text URL, parliament committee record.                                                                |
| **partial**         | An NIM has been adopted but covers only some of the directive's articles or chapters, with a remainder still in draft, planned, or not-yet-planned.                                                                                                                              | Positive evidence: NIM citation, plus an explicit gap analysis showing which articles are covered and which are not.                     |
| **complete**        | An NIM (or a coordinated set of NIMs) has been adopted that on its face addresses every article requiring transposition.                                                                                                                                                         | Positive evidence: NIM citation(s), MNE notification entry, completeness check (Better Regulation Toolbox Ch. 4) confirms full coverage. |
| **overdue**         | The transposition deadline has passed and the MS has not adopted a complete NIM. May overlap with "partial" or "draft" — both can be overdue.                                                                                                                                    | Deadline date < today; matrix records the deadline-overdue period in days.                                                               |
| **withdrawn**       | An NIM was adopted but subsequently repealed or annulled (e.g., by a constitutional court or a substantive amendment that voids the original transposition). Rare but real (e.g., partial annulment of national NIS1 transposition by the Belgian Constitutional Court in 2018). | Positive evidence: repeal-act citation or constitutional-court judgment.                                                                 |

**Status is per-MS, not per-Article**: this skill records one status per MS-directive
pair. Per-Article verdicts (correct / partial / incorrect / not transposed) are
`legalcode-eu-conformity-assessment`'s job, not this skill's. If a MS has adopted an
NIM that covers all articles, status here is "complete" — even if some of that coverage
is later judged "partial" or "incorrect" on the merits by the conformity skill.

**Notification is a separate variable**: an MS can be "complete" (NIM adopted) but
"not notified" (Commission has not been informed). Art. 260(3) TFEU triggers off
notification, not adoption. Track the two columns independently.

**Notification statuses:**

- `notified`: MS has notified the Commission of full transposition; an MNE entry exists
  and the MS has supplied a correlation table per Better Regulation Toolbox Ch. 4
  guidance.
- `partially-notified`: MS has notified some NIMs but acknowledges remaining gaps.
- `not-notified`: no MNE entry; Commission has not been informed.
- `notified-disputed`: MS has notified but the Commission's completeness check has
  questioned coverage (this typically appears as an EU-Pilot inquiry; see
  `legalcode-eu-infringement-procedure-tracker` for the procedural follow-up).

### Step 7: Compute the Transposition Deficit

Apply the Single Market and Competitiveness Scoreboard methodology.

**Definition** (Single Market and Competitiveness Scoreboard): the transposition deficit
for an MS is the proportion of EU directives in force whose National Implementing Measures
have **not** been notified to the Commission by the transposition deadline. This skill
operates at single-directive granularity, so the per-MS deficit is binary (notified /
not notified) for the directive in scope.

**Aggregate matrix-level metric** (this skill's contribution):

Transposition deficit for this directive = (number of MS where status ≠ notified by
deadline) / (number of MS in scope).

**Computation rules:**

- Pre-deadline: deficit is null. The Scoreboard methodology does not assess deficit
  before the deadline because the obligation has not yet matured. Mark the deficit
  cell as `n/a (pre-deadline)`.
- On or after the deadline: compute deficit. Surface the count of overdue + not-notified
  MS, the count of overdue + partially-notified MS, and the count of complete +
  notified MS.
- For the EFTA pillar, the analogous metric is the ESA Internal Market Scoreboard
  EEA-pillar transposition deficit; compute it separately because the EEA-pillar
  deadline is the JCD-adoption + national-incorporation timeline, not the EU-pillar
  directive deadline.

**Worked example (illustrative — verify before relying on)**:

For NIS2 (transposition deadline 17 October 2024), as of early 2026 published Linklaters
and Herbert Smith Freehills trackers indicate that a substantial majority of EU MS had
not adopted complete NIMs by the deadline. Use the published trackers as the secondary
source baseline, flag every cell sourced from them with `source_tier: secondary-tracker`,
and then verify each row against the MS's own OJ before treating any specific number as
authoritative. The Commission opened Art. 258 LFNs against multiple MS in November 2024
specifically for non-notification of NIS2 transposition; the appropriate citation for
those LFNs is the Commission's monthly infringement-decisions package.

### Step 8: Identify Risk Cases

Risk scoring varies by persona (per Step 2). Compute the following risk dimensions for
every MS row:

1. **Overdue + Art. 260(3) exposure**: status is "overdue" _and_ notification is
   "not-notified" _and_ the directive is legislative within the meaning of Art. 289 TFEU
   (i.e., adopted under ordinary or special legislative procedure, not by delegation).
   When all three are true, the MS is exposed to a first-referral penalty payment under
   Art. 260(3) TFEU on the Commission's discretion.

2. **Pre-deadline + risk of being late**: deadline is in the future, but the status is
   "not-yet-planned" or "planned" with no evidence of an active legislative pipeline,
   _and_ the MS has a documented historical pattern of late transposition (see
   "Risk Scoring" reference section below for how to weight historical pattern).

3. **Partial + completion-gap risk**: status is "partial" with a documented gap. Risk
   score increases as the deadline approaches and the gap remains unfilled.

4. **Notified-disputed + EU-Pilot exposure**: notification is "notified-disputed",
   indicating the Commission has questioned coverage. Risk feeds into the
   `legalcode-eu-infringement-procedure-tracker` inquiry stream.

5. **Withdrawn + re-transposition risk**: status is "withdrawn"; the MS must re-adopt
   an NIM, and is exposed to the Art. 258 / 260 ladder until it does.

For each MS row, emit a `risk_dimensions` block in the canonical JSON with one entry per
applicable dimension, plus a roll-up `headline_risk_tier` of CRITICAL / HIGH / MEDIUM /
LOW / NONE following the rubric in the "Risk Scoring" reference section.

### Step 9: Per-Persona Outputs Branching

#### Government / EU institution branch

- Emit own-MS row with full detail block (all citation fields, completeness-check
  self-assessment, Art. 260(3) self-exposure assessment).
- Emit peer-MS rows for benchmarking (typically the four largest MS plus any MS in the
  same regulatory cluster or geographic region).
- Produce a notification-readiness checklist tied to Better Regulation Toolbox Ch. 4:
  is the correlation table prepared? has the MS supplied a declaratory commitment? has
  the NIM been published in the national OJ?
- For ESA-pillar MS (IS, NO, LI), produce the ESA-readiness analogue.

#### Legal-firm branch

- Emit the full 27 (or 30) row matrix sorted by status tier, with a colour-coded
  Markdown table.
- Produce an executive summary identifying CRITICAL / HIGH risk MS for client briefing.
- For each high-risk MS, produce a one-paragraph deep dive with NIM citation,
  notification status, deadline-to-go (or deadline-overdue), and a sentence on
  enforcement exposure.
- Produce the JSON payload for downstream automated consumption.

#### Company branch

- Filter the matrix to MS where the company operates (default: ask the user for the
  list; if not supplied, emit full matrix and flag for filtering).
- Sort by effective / application date of the NIM (operational deadline) ascending.
- Produce an operational-deadline calendar.
- For each MS where the company operates, produce a one-line readout:
  `[MS]: [status] | NIM: [citation] | effective: [date] | gap-to-go: [days]`.

#### Trade-federation branch

- Sort the matrix by status: "draft" and "planned" rows first (engagement opportunity),
  then "partial" (advocacy on remaining provisions), then "complete" (lessons-learned
  for federation members in other MS).
- Produce a comparative-pattern summary: where MS are diverging in approach, where
  they are converging, where gold-plating signals are visible (cross-reference
  `legalcode-eu-gold-plating-detector` for a substantive gold-plating inquiry).
- Produce a per-MS engagement contact list keyed to the MS responsible-ministry
  for this directive.

### Step 10: Emit Outputs

Produce all four output formats:

1. Markdown comparison table (30 or 27 rows × N status columns) — see Output Format
   Template below.
2. Canonical JSON matrix conforming to the schema below — primary machine-readable
   artefact.
3. AKN4EU per-MS NIM document references — XML stubs referencing each MS NIM as
   `<akomaNtoso>` with `<doc>` children appropriate to the national instrument type.
4. LegalRuleML stub showing how the aggregate "MS X has transposed obligation Y"
   assertion is expressed (as a Constitutive rule with Source, Party, and the directive
   ELI as the underlying obligation referent).
5. Glass Box audit trail — every status assertion must have a provenance entry with
   source URL, fetch date, and evidence quote.

---

## Member State and EEA EFTA State Coverage

This reference section lists every MS and EFTA state with its parliament data source,
official journal name, primary national legal database, and the canonical NIM citation
format. For full identifier-format detail, see the shared
[EU legislative-data pack](references/eu-legislative-data/).

### EU-27

| MS                  | Parliament data                                                                 | Official journal                                                         | Primary legal database                                          | NIM citation format                                                             |
| ------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Austria (AT)        | Parlament.gv.at                                                                 | BGBl (Bundesgesetzblatt)                                                 | RIS (Rechtsinformationssystem) `https://www.ris.bka.gv.at`      | BGBl. I Nr. NNN/YYYY                                                            |
| Belgium (BE)        | LaChambre.be / DeKamer.be / Senate.be                                           | Moniteur belge / Belgisch Staatsblad `https://www.ejustice.just.fgov.be` | Justel                                                          | M.B. DD-MM-YYYY (date, p.)                                                      |
| Bulgaria (BG)       | Parliament.bg                                                                   | Държавен вестник (State Gazette)                                         | Lex.bg                                                          | ДВ бр. NN от DD.MM.YYYY                                                         |
| Croatia (HR)        | Sabor.hr                                                                        | Narodne novine `https://narodne-novine.nn.hr`                            | NN                                                              | NN broj N/YYYY                                                                  |
| Cyprus (CY)         | ParliamentaryCommittees.gov.cy                                                  | Επίσημη Εφημερίδα (Government Gazette)                                   | CyLaw                                                           | E.E. Παρ. N(I) Αρ. NNNN                                                         |
| Czech Republic (CZ) | PSP.cz / Senat.cz                                                               | Sbírka zákonů                                                            | Zákony pro lidi                                                 | č. NN/YYYY Sb.                                                                  |
| Denmark (DK)        | Folketinget.dk; data API `https://oda.ft.dk`                                    | Lovtidende                                                               | Retsinformation `https://www.retsinformation.dk`                | LOV nr NNNN af DD/MM/YYYY                                                       |
| Estonia (EE)        | Riigikogu.ee                                                                    | Riigi Teataja `https://www.riigiteataja.ee`                              | RT                                                              | RT I, DD.MM.YYYY, N                                                             |
| Finland (FI)        | Eduskunta.fi                                                                    | Säädöskokoelma (Statute Book) `https://www.finlex.fi`                    | Finlex                                                          | NNNN/YYYY                                                                       |
| France (FR)         | AssembleeNationale.fr; data API `https://data.assemblee-nationale.fr`; Senat.fr | Journal officiel `https://www.legifrance.gouv.fr`                        | Légifrance                                                      | JORF n°NNNN du DD MMMM YYYY texte n° N                                          |
| Germany (DE)        | Bundestag.de; DIP `https://dip.bundestag.de`; Bundesrat.de                      | Bundesgesetzblatt `https://www.recht.bund.de`                            | Gesetze im Internet `https://www.gesetze-im-internet.de`        | BGBl. I YYYY, S. NNNN (formerly Nr. NN; current "Tagesnummer" format from 2023) |
| Greece (EL)         | Hellenicparliament.gr                                                           | Φύλλο Εφημερίδος της Κυβερνήσεως (FEK)                                   | Et.gr                                                           | ΦΕΚ N/YYYY                                                                      |
| Hungary (HU)        | Parlament.hu                                                                    | Magyar Közlöny                                                           | Net.jogtar.hu                                                   | NNNN. évi N. törvény                                                            |
| Ireland (IE)        | Oireachtas.ie; data API                                                         | Iris Oifigiúil                                                           | electronic Irish Statute Book `https://www.irishstatutebook.ie` | No. N of YYYY                                                                   |
| Italy (IT)          | Camera.it / Senato.it                                                           | Gazzetta Ufficiale `https://www.gazzettaufficiale.it`                    | Normattiva                                                      | GU Serie Generale n. NNN del DD-MM-YYYY                                         |
| Latvia (LV)         | Saeima.lv                                                                       | Latvijas Vēstnesis `https://www.vestnesis.lv`                            | Likumi.lv                                                       | LV NN, DD.MM.YYYY                                                               |
| Lithuania (LT)      | LRS.lt                                                                          | Teisės aktų registras (TAR)                                              | e-tar.lt                                                        | TAR YYYY-NN-NN, Nr. NNN                                                         |
| Luxembourg (LU)     | ChD.lu                                                                          | Mémorial A                                                               | Legilux `https://legilux.public.lu`                             | Mém. A YYYY, N. NNN                                                             |
| Malta (MT)          | Parlament.mt                                                                    | Government Gazette                                                       | Justice Services `https://legislation.mt`                       | Cap. NNN                                                                        |
| Netherlands (NL)    | Tweedekamer.nl; data API; Eerstekamer.nl                                        | Staatsblad `https://www.officielebekendmakingen.nl`                      | wetten.overheid.nl                                              | Stb. YYYY, NNN                                                                  |
| Poland (PL)         | Sejm.gov.pl; Senat.gov.pl                                                       | Dziennik Ustaw `https://dziennikustaw.gov.pl`                            | ISAP                                                            | Dz.U. YYYY poz. NNNN                                                            |
| Portugal (PT)       | Parlamento.pt                                                                   | Diário da República `https://dre.pt`                                     | DRE                                                             | DR 1.ª série, n.º NNN, DD-MM-YYYY                                               |
| Romania (RO)        | CDep.ro / Senat.ro                                                              | Monitorul Oficial al României                                            | Legislatie.just.ro                                              | M.Of. nr. NNN/DD.MM.YYYY                                                        |
| Slovakia (SK)       | NRSR.sk                                                                         | Zbierka zákonov                                                          | Slov-Lex `https://www.slov-lex.sk`                              | č. NN/YYYY Z. z.                                                                |
| Slovenia (SI)       | DZ-RS.si                                                                        | Uradni list RS `https://www.uradni-list.si`                              | PIS                                                             | UL RS, št. N/YY                                                                 |
| Spain (ES)          | Congreso.es / Senado.es                                                         | Boletín Oficial del Estado `https://www.boe.es`                          | BOE                                                             | BOE núm. NNN, de DD MMMM YYYY                                                   |
| Sweden (SE)         | Riksdagen.se; data API `https://data.riksdagen.se`                              | Svensk författningssamling                                               | Svensk författningssamling.se                                   | SFS YYYY:NNNN                                                                   |

### EEA EFTA states (when directive is EEA-relevant)

| State              | Parliament data                                      | Official journal  | Primary legal database         | NIM citation format           |
| ------------------ | ---------------------------------------------------- | ----------------- | ------------------------------ | ----------------------------- |
| Iceland (IS)       | Althingi.is `https://www.althingi.is`                | Stjórnartíðindi   | Althingi.is laws section       | Stj. A-deild, lög nr. NN/YYYY |
| Norway (NO)        | Stortinget.no; data API `https://data.stortinget.no` | Norsk Lovtidend   | Lovdata `https://lovdata.no`   | LOV-YYYY-MM-DD-NN             |
| Liechtenstein (LI) | Landtag.li                                           | Landesgesetzblatt | LiLex `https://www.gesetze.li` | LGBl. YYYY Nr. NNN            |

**Notes on EFTA-pillar coverage:**

- The EFTA states are in scope only when the directive is EEA-relevant _and_ a Joint
  Committee Decision under Art. 102 EEA has been adopted (or is about to be) to
  incorporate it into the EEA Annexes.
- For each EFTA row, the analogue of "transposition deadline" is the JCD-adoption
  date plus the JCD-specified incorporation period (typically 6–18 months from JCD
  adoption, varying by act).
- Constitutional reservations under Art. 103 EEA (parliamentary approval suspension in
  IS or NO) delay JCD entry into force; reflect this in the matrix as
  "JCD adopted, Art. 103 reservation pending" rather than as "transposition pending."
- Liechtenstein has no Art. 103 reservation tradition; LI typically follows JCD timelines
  closely.
- Hand off the EFTA-pillar status query to `legalcode-eea-incorporation-tracker` and
  consume its output rather than duplicating that pipeline here.

---

## Transposition Status Taxonomy

The seven-tier taxonomy (Step 6 above) is the normative classification scheme. This
section defines the evidence required for each tier and the common edge cases.

### not-yet-planned

**Definition**: No public evidence of a draft, consultation, parliamentary motion, or
ministerial roadmap.

**Evidence required (negative)**: search of (a) MS parliament API, (b) national OJ, (c)
ministry website, (d) MNE database returns no result related to the directive's CELEX
or short title.

**Edge cases:**

- _Pre-existing legislation deemed sufficient_: an MS may take the position that
  pre-existing national law already transposes the directive, and therefore that no
  new NIM is needed. This is rarely accepted by the Commission's completeness check
  (see _Commission v Italy_ C-22/87 — administrative practice is not transposition).
  If this position is publicly stated, classify as "complete (pre-existing)" with a
  notation flagging Commission-completeness-check exposure, _not_ as "not-yet-planned."
- _Public consultation announced but no draft_: classify as "planned," not
  "not-yet-planned."

### planned

**Definition**: Public roadmap, public consultation, or parliamentary motion exists; no
draft text yet.

**Evidence required**: at least one of: ministry roadmap URL, public consultation URL
(with consultation period dates), or parliament motion record number.

**Edge cases:**

- _Roadmap announced post-deadline_: classify as "overdue + planned." A planned status
  is overlay on the deadline timeline; "overdue" is not a separate status, it is a
  modifier (see "overdue" below).

### draft

**Definition**: A draft NIM text exists in the national legislative pipeline.

**Evidence required**: bill URL, draft text URL, parliament committee record, or
government bill register entry.

**Edge cases:**

- _Multiple competing drafts_: where opposition or coalition partners have introduced
  alternative drafts, record only the government / responsible-ministry draft as the
  matrix's primary draft, but note alternatives in the per-MS notes block.
- _Draft published but withdrawn_: status reverts to "planned" or "not-yet-planned" if
  the withdrawal is final; if withdrawn for re-drafting, status is still "draft" with a
  note.

### partial

**Definition**: An NIM has been adopted but covers only some of the directive's articles
or chapters.

**Evidence required**: NIM citation + an explicit gap analysis showing which articles
are covered. The gap analysis should be expressed as a list of directive Article numbers
flagged covered / not covered.

**Edge cases:**

- _Staggered transposition planned_: the MS has adopted Phase 1 and a Phase 2 draft is
  in the pipeline. Classify as "partial" plus note the Phase 2 draft status as a
  sub-row.
- _Adopted with carve-outs_: the NIM transposes most provisions but explicitly excludes
  certain ones pending later adoption. Treat carve-outs as the un-covered set.

### complete

**Definition**: An NIM (or a coordinated set of NIMs) has been adopted that on its face
addresses every article requiring transposition.

**Evidence required**: NIM citation(s), MNE notification entry confirming the MS's
self-assessment of completeness, and ideally a correlation table per Better Regulation
Toolbox Ch. 4.

**Edge cases:**

- _Complete on its face but conformity-disputed_: the matrix's "complete" status is
  facial; the conformity assessment may later judge specific articles "incorrect" or
  "partial" on the merits. The matrix records "complete" + notification status; the
  conformity skill records the on-the-merits verdict separately. Do not conflate.
- _Complete via an omnibus act_: where the MS adopts a single act that transposes
  multiple directives, list the omnibus act as the NIM with a note pointing to the
  other directives also transposed.

### overdue

**Definition**: The transposition deadline has passed and the MS has not adopted a
complete NIM (or has not notified, depending on exact framing — but as a status this
focuses on adoption; notification is tracked separately).

**Evidence required**: deadline date < today; matrix records the days-overdue.

**Status interaction**: "overdue" is the primary status when adoption has not occurred
by the deadline. "overdue" can co-exist with "draft," "partial," or "planned" as a
modifier — but for the matrix's primary status column, use "overdue" once the deadline
has passed without complete adoption.

### withdrawn

**Definition**: An NIM was adopted but subsequently repealed or annulled.

**Evidence required**: repeal-act citation or constitutional-court / supreme-court
judgment annulling the NIM.

**Edge cases:**

- _Partial annulment_: the constitutional court has annulled some provisions of the NIM
  but left others standing. Classify as "partial" if the remaining provisions still
  transpose part of the directive; classify as "withdrawn" only if the annulment
  removes the substantive transposition.

---

## Notification to Commission

Notification is the act by which an MS formally communicates to the Commission that it
has adopted national measures to transpose a directive. Notification is procedurally and
legally distinct from adoption: an MS can adopt an NIM but fail to notify, and the
notification gap (not the adoption gap) is what triggers Art. 260(3) TFEU.

### What notification consists of

Per Better Regulation Toolbox 2023 Ch. 4 and Commission practice, a complete notification
includes:

1. **The text(s) of the NIM(s)** — typically the OJ-published text plus any
   ministerial regulations and technical standards that form part of the transposition.
2. **A correlation table** — a Commission-format two-column table mapping each provision
   of the directive to the corresponding provision(s) of the NIM. This is the Commission's
   primary tool for the conformity check (and is the artefact produced by sibling skill
   `legalcode-eu-correlation-table-builder`).
3. **A declaratory commitment** — the MS states that the NIM(s) constitute full
   transposition of the directive within the meaning of Art. 288(3) TFEU. The declaratory
   commitment is what triggers the legal effect of notification: it converts the MS's
   silent default position (no notification = potentially overdue) into a positive
   claim of compliance that the Commission can then check.
4. **Coverage scope** — for partial notifications, the MS states which articles or
   chapters are covered.

### Why notification is the critical column

The "notified to Commission" column of the matrix is the column that drives Art. 260(3)
TFEU exposure. Per _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573 (judgment
of 8 July 2019, OJ C 270/15, 12.8.2019), Art. 260(3) operates at the **first referral**
to the CJEU under Art. 258 — meaning the Commission can simultaneously seek a
declaration of failure to fulfil treaty obligations _and_ a financial penalty in the
same action, without the second-referral ladder of Art. 260(2). The trigger for
Art. 260(3) is **failure to notify transposition measures**, not failure to transpose
on the merits. So:

- An MS that has adopted a complete NIM but has not notified the Commission is exposed
  to Art. 260(3) just as much as an MS that has not adopted at all.
- An MS that has notified an inadequate NIM (one that does not in fact transpose the
  directive correctly) is _not_ exposed to Art. 260(3) on the basis of that notification;
  the Commission's recourse there is the ordinary Art. 258 procedure (or, post-judgment,
  Art. 260(2)).
- This is why this skill records adoption status and notification status as **two
  independent columns**.

### Types of notification status

- `notified`: full notification with declaratory commitment; MNE entry exists.
- `partially-notified`: MS has notified some NIMs but acknowledges remaining gaps.
- `not-notified`: no MNE entry; Commission has not been informed.
- `notified-disputed`: MS has notified but the Commission's completeness check has
  questioned coverage. This typically appears as an EU-Pilot inquiry and may escalate
  to an Art. 258 LFN. Hand off to `legalcode-eu-infringement-procedure-tracker` for
  tracking the LFN / reasoned-opinion timeline.

### Article 260(3) qualification check

For each MS row marked "not-notified" past the deadline, run this qualification check:

1. Is the directive a **legislative directive** within the meaning of Art. 289 TFEU
   (adopted under ordinary or special legislative procedure, not by delegation)? If
   no, Art. 260(3) does not apply.
2. Has the **transposition deadline passed**? If no, Art. 260(3) does not apply yet.
3. Has the MS **failed to notify** transposition measures? If yes, Art. 260(3) applies.
4. Has the Commission **opened an Art. 258 procedure** for non-notification (LFN sent)?
   This is the procedural gate to Art. 260(3); the Commission must initiate Art. 258
   first, but can request the Art. 260(3) penalty in the same referral.

If all four are yes, the MS row's `art_260_3_exposure` field is `true`. Surface this in
the risk dimensions (Step 8) and the executive summary.

### Declaratory commitment language

A typical declaratory commitment in a notification reads (translating from MS
practice):

> "The Government of [MS] hereby notifies the European Commission, in accordance with
> Article 41 of Directive (EU) 2022/2555, that the following national measures
> [list] have been adopted by [MS] for the purpose of transposing the said directive
> in full into national law as of [effective date]."

The matrix should record whether the MS's notification includes such a declaratory
commitment in full, in part (notification of partial transposition), or not at all (a
mere transmission of texts without an attestation that they constitute transposition).

---

## NIM Citation Format

Each MS has its own canonical citation format for primary and secondary national law.
The matrix's `nim_citation` field must use the canonical national format, _not_ an
ad-hoc translation. The shared
[EU legislative-data pack](references/eu-legislative-data/)
covers the full identifier playbook; this section provides the matrix-relevant summary.

### Canonical formats by MS

- **Germany (DE)**: `BGBl. I YYYY, S. NNNN` for primary federal law (post-2023 form
  using "Tagesnummer"; pre-2023 form was `BGBl. I YYYY Nr. NN, S. NNNN`). Example:
  "BGBl. I 2024, S. 1532". For sub-federal (Land) law, use `[Land] GVBl. YYYY S. NNN`
  (e.g., "Bayer. GVBl. 2024 S. 312"). For secondary regulation, use the same series
  but referenced as a Verordnung.
- **France (FR)**: `JORF n°NNNN du DD MMMM YYYY texte n° N` for laws and decrees.
  Example: "JORF n°0245 du 19 octobre 2024 texte n° 3". Cite Légifrance URL where
  available (`https://www.legifrance.gouv.fr/jorf/id/...`).
- **Italy (IT)**: `GU Serie Generale n. NNN del DD-MM-YYYY` for legge and decreto
  legislativo. Example: "GU Serie Generale n. 245 del 19-10-2024". Cite Normattiva
  URL where available.
- **Spain (ES)**: `BOE núm. NNN, de DD MMMM YYYY`. Example: "BOE núm. 252, de 19
  octubre 2024".
- **Poland (PL)**: `Dz.U. YYYY poz. NNNN`. Example: "Dz.U. 2024 poz. 1532".
- **Sweden (SE)**: `SFS YYYY:NNNN`. Example: "SFS 2024:1532".
- **Denmark (DK)**: `LOV nr NNNN af DD/MM/YYYY` (Lovtidende format).
- **Finland (FI)**: `NNNN/YYYY` (Säädöskokoelma reference; Finlex stable URL preferred
  for citation).
- **Austria (AT)**: `BGBl. I Nr. NNN/YYYY`.
- **Netherlands (NL)**: `Stb. YYYY, NNN` (Staatsblad).
- **Belgium (BE)**: `M.B. DD-MM-YYYY (p. NNNN)` for Moniteur belge / Belgisch Staatsblad.
- **Iceland (IS)**: `lög nr. NN/YYYY` (Stjórnartíðindi A-deild).
- **Norway (NO)**: `LOV-YYYY-MM-DD-NN` (Lovdata identifier).
- **Liechtenstein (LI)**: `LGBl. YYYY Nr. NNN`.

For all other MS, see the shared identifier pack.

### ELI national namespaces

Where the MS exposes ELI URIs for national law, prefer the ELI URI as the canonical
citation alongside the human-readable form. ELI URIs follow the pattern
`http://[national-domain]/eli/[type]/[year]/[number]/oj` or a national variant
documented in the ELI register (`https://eur-lex.europa.eu/eli-register/technical_information.html`).

Example (FR ELI):
`https://www.legifrance.gouv.fr/eli/loi/2024/10/19/2024-1234/jo/texte`.

### Multi-instrument NIMs

Where the transposition is split across multiple instruments (a primary law plus
secondary regulations), record all instruments in the `nim_citation` field as a list:

```yaml
nim_citation:
  - type: "primary"
    citation: "BGBl. I 2024, S. 1532"
    eli: "..."
  - type: "secondary"
    citation: "BGBl. I 2024, S. 1789"
    eli: "..."
```

---

## Risk Scoring

Risk scoring per MS-directive pair quantifies the exposure surface for the matrix's
risk dimensions (Step 8). Risk is scored on a 1–5 likelihood × 1–5 impact scale (1–25
range), aggregated to CRITICAL / HIGH / MEDIUM / LOW / NONE.

### Likelihood scale

| Score | Label          | Definition                                                                                                |
| ----- | -------------- | --------------------------------------------------------------------------------------------------------- |
| 1     | Negligible     | No realistic prospect of materialising into infringement / penalty exposure within the matrix horizon.    |
| 2     | Unlikely       | Theoretical exposure but the MS is on a clear remediation path and has Commission-level engagement.       |
| 3     | Possible       | Exposure is real and the MS is not actively remediating; Commission inquiry plausible within 6–12 months. |
| 4     | Likely         | Exposure is documented (LFN, EU-Pilot, public Commission statement) or near-certain given pattern.        |
| 5     | Almost Certain | Exposure is realised (LFN issued, reasoned opinion sent, or CJEU referral in progress).                   |

### Impact scale

| Score | Label      | Definition                                                                                                                                                       |
| ----- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Negligible | Procedural correspondence only; no penalty exposure; no operational impact on persona.                                                                           |
| 2     | Minor      | EU-Pilot inquiry; remedial commitment letter; minor reputational signal.                                                                                         |
| 3     | Moderate   | Art. 258 LFN open; remedial action required within months; moderate political signal.                                                                            |
| 4     | Major      | Art. 258 reasoned opinion issued; CJEU referral imminent; significant penalty risk under Art. 260(3) for non-notification cases; reputational exposure.          |
| 5     | Critical   | CJEU judgment + lump sum / periodic penalty payment imposed; or Commission monthly infringement decision actively pursued; major political and budgetary impact. |

### Risk = Likelihood × Impact, rolled up to tier

| Score                               | Tier         |
| ----------------------------------- | ------------ |
| ≥ 16                                | **CRITICAL** |
| 9–15                                | **HIGH**     |
| 4–8                                 | **MEDIUM**   |
| 1–3                                 | **LOW**      |
| n/a (no exposure dimension applies) | **NONE**     |

### Historical-pattern weighting

Some MS have documented patterns of late transposition; this should weight the
likelihood score for "pre-deadline + risk of being late" rows. Use the Single Market
and Competitiveness Scoreboard published per-MS transposition-deficit data as the
weighting baseline:

- MS with transposition deficit consistently above the EU average for the most recent
  Scoreboard year(s): +1 to likelihood for "pre-deadline + risk of being late" cases.
- MS with transposition deficit consistently at or below the EU average: no adjustment.
- MS with active Art. 258 / 260 cases on related directives: +1 to likelihood for any
  exposure dimension.

Mark all historical-pattern adjustments explicitly in the risk-scoring rationale so
the basis is auditable in the Glass Box.

### Persona-specific risk weighting

| Persona          | Heaviest weight                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| Government       | "Overdue + Art. 260(3) exposure" — directly drives penalty exposure for own MS   |
| Legal firm       | Balanced — clients ask both about overdue MS and surprises                       |
| Company          | "Operational deadline gap" — when can we operate compliantly                     |
| Trade federation | "Pre-deadline draft" + "historical gold-plating pattern" — engagement priorities |

---

## EEA Pillar Coordination

When the directive is EEA-relevant, the matrix's EFTA-pillar rows (IS, NO, LI) must be
coordinated with `legalcode-eea-incorporation-tracker`.

### EEA-relevance flag

Every EU directive contains a recital block stating whether the act is EEA-relevant.
The text typically reads "This act is text with EEA relevance" or, less commonly, "This
act is not text with EEA relevance." The flag determines whether the JCD pipeline
applies at all.

For directives flagged EEA-relevant:

1. **Pre-JCD**: The act is EEA-relevant but no JCD has been adopted. The EFTA pillar
   does not yet have a domestic-implementation duty for IS / NO / LI. Mark EFTA rows
   as "n/a (JCD pending)" and hand off the JCD pipeline status to
   `legalcode-eea-incorporation-tracker`.
2. **JCD adopted, in force**: A JCD under Art. 102 EEA has been adopted and has
   entered into force (no Art. 103 reservation pending). The EFTA states have a
   domestic-implementation duty; populate the IS / NO / LI rows with the same status
   taxonomy as EU MS, where the analogue of the directive transposition deadline is
   the JCD-specified incorporation deadline.
3. **JCD adopted, Art. 103 reservation pending**: A JCD has been adopted but is not
   yet in force because IS or NO has invoked its constitutional reservation under
   Art. 103 EEA. Mark the affected EFTA row as "JCD adopted, Art. 103 reservation
   pending"; this is not "transposition pending" because the upstream EEA-pillar
   instrument has not yet entered into force.
4. **Specific adaptations**: Some JCDs include EEA-specific adaptations of the directive
   (e.g., references to Commission committees replaced by references to Joint
   Committee bodies). Note such adaptations in the per-MS notes block, since they
   affect the substantive content the EFTA states must transpose.

### ESA monitoring (the Art. 31 SCA analogue)

ESA Internal Market Scoreboard tracks the EFTA-pillar transposition deficit using the
same methodology as the Single Market Scoreboard. When the ESA Scoreboard publishes a
new edition, refresh the EFTA rows. ESA Art. 31 SCA infringement procedures are tracked
separately by `legalcode-eu-infringement-procedure-tracker` (which covers both the
EU-pillar Art. 258 / 260 procedures and the EFTA-pillar Art. 31 SCA procedures).

---

## Anti-Patterns for EU Transposition Tracking

What NOT to do when building the per-MS transposition matrix:

1. **Conflating adoption with notification** — The single most consequential error.
   Adoption is the national-law act; notification is the communication to the
   Commission. Art. 260(3) TFEU triggers off non-notification, not non-adoption — so
   an MS that has adopted but not notified is still exposed to first-referral penalty
   payments under _Commission v Belgium_ C-543/17. Track adoption-status and
   notification-status as two independent columns; never collapse them.

2. **Recording status without provenance** — Every cell of the matrix must trace to a
   primary source: MNE entry, national OJ entry, parliament bill page, or ministry
   portal. Cells sourced from secondary trackers (Linklaters, HSF, Ropes) must be
   flagged `source_tier: secondary-tracker` and verified against the primary source
   before the matrix is delivered to a regulator, board, or partner. The Glass Box
   audit trail must show source URL + fetch date + evidence quote for every cell.

3. **Assuming the directive's headline transposition deadline applies to all
   articles** — Many directives have staggered transposition deadlines for specific
   provisions (e.g., NIS2 Art. 41(1) is the headline; specific implementing acts have
   later application). Read the transposition article in full and capture every
   sub-deadline in the directive metadata. For each MS row, status must be assessed
   against the _applicable_ deadline for the cell, not just the headline.

4. **Treating EU directives as binding on EEA EFTA states** — IS, NO, LI are bound only
   by EU acts that have been incorporated via Joint Committee Decision under Art. 102
   EEA. A directive that is "in force" in the EU is not yet "in force" in the EEA
   pillar until JCD adoption. Always check the EEA-relevance flag and the JCD status
   before populating EFTA rows. Coordinate with `legalcode-eea-incorporation-tracker`.

5. **Confusing "transposition complete" with "conformity confirmed"** — Status
   "complete" in this matrix is a facial finding: the NIM has been adopted and on its
   face addresses every article requiring transposition. It does _not_ mean the NIM
   correctly transposes the directive on the merits. Conformity is a separate
   downstream artefact (`legalcode-eu-conformity-assessment`). Mixing the two
   produces false positives in the "complete" column and undermines downstream
   conformity work.

6. **Missing partial transposition across multiple national instruments** — Many MS
   transpose a directive across a primary law plus secondary regulations plus
   amending acts. A search that finds only the primary law may miss the secondary
   regulation that completes the transposition; conversely, a search that finds only
   one of multiple amending acts may misclassify the MS as "partial" when it is
   actually "complete" once all instruments are read together. Always run the
   discovery method against MNE first (which lists all notified instruments in one
   place), then cross-check against the parliament API.

7. **Treating administrative practice as transposition** — A directive cannot be
   transposed by mere administrative practice or non-binding guidance, per
   _Commission v Italy_, Case 22/87, ECLI:EU:C:1989:45. If the MS's discovery yields
   only a circular, ministerial guidance, or non-binding code, classify as
   "not-yet-planned" or "draft" (depending on whether binding legislation is in the
   pipeline), not "complete."

8. **Citing a directive in pre-existing law as evidence of transposition** —
   "Pre-existing law deemed sufficient" is rarely accepted by the Commission's
   completeness check. If the MS has not adopted any new instrument and instead
   takes the position that pre-existing law transposes, classify as "complete
   (pre-existing, deemed)" with explicit notation that the position is exposed to
   completeness-check challenge — _not_ as plain "complete."

9. **Using a single language version of the directive for transposition deadline
   computation** — Per CILFIT, Case C-283/81, ECLI:EU:C:1982:335, all 24 official
   language versions are equally authentic. Where the transposition article reads
   differently across language versions (rare but possible), reconcile before
   computing the deadline. In practice, the OJ-published English / French / German
   versions are the customary working set for legal practice.

10. **Recording NIM citations in ad-hoc translation rather than canonical national
    format** — Citing "German Federal Law Gazette I 2024 page 1532" instead of "BGBl.
    I 2024, S. 1532" breaks downstream tooling that expects canonical national
    citations and undermines the matrix's machine-readability. Always use the
    canonical national format from the "NIM Citation Format" section above.

11. **Flagging the matrix as static** — A transposition matrix has a half-life of
    weeks (during the active transposition window) or months (post-deadline as
    overdue MS catch up). Always emit a `last_refreshed` timestamp at the matrix and
    per-cell levels, plus a `next_review_due` timestamp keyed to either the next MS
    parliament session, the next MNE update, or a fixed cadence (typically monthly
    during the transposition window, quarterly thereafter). A stale matrix is worse
    than no matrix because it generates false confidence.

12. **Over-aggregating to a single status when an MS has split-instrument
    transposition** — If the MS has adopted the primary law (covering Chapters I–IV)
    but the secondary regulation for Chapter V is still in draft, the status is
    "partial" with a specific gap recorded — not "complete" because the primary law
    is adopted, and not "draft" because Chapters I–IV are adopted. Use the partial
    status with gap analysis; this is what downstream conformity tooling needs.

13. **Skipping the Art. 260(3) qualification check** — Not every "not notified past
    deadline" cell triggers Art. 260(3). The qualification check (legislative
    directive, deadline passed, non-notification, Art. 258 procedure opened) must be
    run before flagging Art. 260(3) exposure. Flagging Art. 260(3) exposure for a
    non-legislative directive (e.g., a directive adopted by delegation, or a
    Commission directive under Art. 290 / 291 TFEU) is wrong — Art. 260(3) applies
    only to legislative directives within the meaning of Art. 289 TFEU.

14. **Assuming the EU-27 always equals 27 rows** — Brexit changed the composition of
    the EU on 1 February 2020. Some directives in force in the EU-28 era have
    distinct UK-transposition records that are now historical, not current EU-pillar
    data. UK is in scope only for directives in force pre-Brexit; for directives
    adopted post-Brexit, UK is out of scope entirely (and any UK regulatory analogue
    is tracked separately as UK domestic law, e.g., the UK NIS2-equivalent NIS
    Regulations 2018 [VERIFY current UK status post-Brexit]).

15. **Treating "draft" as a single status across very different stages of national
    legislative procedure** — A "draft" can be (a) a public-consultation draft from
    the responsible ministry, (b) a government bill introduced in parliament, (c) a
    bill in committee, (d) a bill adopted by one chamber but not the other (in
    bicameral systems), (e) a bill adopted by both chambers but awaiting promulgation
    / royal assent. Each stage represents very different transposition risk. Use the
    `draft_stage` sub-field to capture the precise stage; do not flatten to a single
    "draft" status without further detail.

16. **Sourcing primarily from law-firm trackers and treating them as authoritative** —
    Linklaters, HSF, Ropes, A&O Shearman publish high-quality NIM trackers for major
    directives (NIS2, CSDDD, AI Act). They are excellent secondary sources and often
    the fastest path to a comprehensive overview. But they are not the primary
    source: the primary source is MNE plus the national OJ. Always cross-check
    tracker entries against the primary source; flag any cell sourced only from a
    tracker as `source_tier: secondary-tracker`. Trackers can be wrong (missed
    instruments, outdated entries, misclassified status), and the Glass Box must be
    able to absorb a regulator's challenge without depending on a tracker as the
    sole basis.

17. **Omitting the per-cell Glass Box entry for cells assessed via negative
    evidence** — When a status of "not-yet-planned" is recorded, the matrix must
    show that the discovery method was actually run and produced no result. A blank
    Glass Box entry for such a cell is indistinguishable from "we did not check," and
    is fatal to the matrix's defensibility. Always record what was searched (which
    parliament API, which OJ, which MNE search) and the result (no entries found
    referencing CELEX X / short-title Y).

18. **Confusing transposition deadlines with application dates** — The transposition
    deadline is the date by which the MS must have adopted the NIM. The application
    date is the date from which the NIM substantively applies. They can differ by
    months or years. NIS2 (CELEX 32022L2555) has a 17 October 2024 transposition
    deadline; specific provisions become applicable on staggered dates from early 2025. The matrix must record both: `transposition_deadline` for the matrix-level
    status and `effective_date` for the per-MS NIM operational date. Companies care
    most about the application date; governments care most about the transposition
    deadline.

19. **Recording withdrawn NIMs without recording the resulting transposition gap** —
    If a constitutional court annuls a NIM, the MS reverts to a transposition gap
    until it re-adopts. The matrix's status must reflect the resulting gap, not just
    the historical adoption. Use the "withdrawn" status plus a note pointing to the
    re-adoption pipeline, if any.

20. **Failing to coordinate with the EEA-incorporation tracker on EEA-relevant
    directives** — When the directive is EEA-relevant, populating IS / NO / LI rows
    without reference to JCD status produces a misleading matrix. The EFTA-pillar
    transposition duty exists only after JCD adoption (and after any Art. 103 EEA
    reservation has been lifted). Always check JCD status — via
    `legalcode-eea-incorporation-tracker` — before treating IS / NO / LI rows as
    EU-MS analogues.

---

## Writing Standards

Follow these standards when producing transposition-tracker outputs:

1. **Deontic operators**: Use _must_ for legal obligations the MS owes under EU law
   (transposition duty, notification duty); use _shall_ in quoted directive text but
   not in commentary; use _may_ for permitted but optional MS choices (e.g., longer
   transposition periods conditional on national choice). Reserve _should_ for
   recommendations from soft-law guidance such as Better Regulation Toolbox.

2. **Citation density**: Every cell of the matrix must be cited. The minimum citation
   set per cell is (a) the NIM citation in canonical national format, (b) the source
   URL, (c) the fetch date. CRITICAL and HIGH risk rows additionally require the
   evidence quote in the Glass Box.

3. **Language-version reconciliation**: When the directive reads differently across
   language versions (rare for transposition deadlines, more common for substantive
   obligations), record the working language used and flag for reconciliation. Default
   working language is the matrix-output language (typically English or the user's
   working language); do not assume the English version controls.

4. **EEA-relevance flag treatment**: Always state explicitly whether the directive is
   EEA-relevant, even when the answer is no. A blank EEA-relevance field is
   ambiguous; an explicit "not EEA-relevant" with citation to the directive's recital
   block is unambiguous.

5. **CELEX / ELI / ECLI in prose vs. footnotes**: In prose, write CELEX numbers in
   the form "CELEX 32022L2555" or "Directive (EU) 2022/2555 (CELEX 32022L2555)". In
   structured fields (JSON, AKN4EU), use the bare CELEX. ELI URIs are always written
   in full URL form; ECLI is always written in dotted form (e.g.,
   "ECLI:EU:C:2019:573").

6. **Active voice, named owner**: Where the matrix flags a remediation action ("MS X
   must notify the Commission"), name the responsible national entity (typically the
   responsible ministry), not just "the MS". This makes the matrix actionable for a
   government persona.

7. **No false precision in dates**: Use the date format the source uses. If the
   national OJ records the adoption date as "19 octobre 2024" without a more precise
   timestamp, do not invent a timestamp. If only the year is known (e.g., for
   "planned" status with a vague roadmap), record `2026-Q3` or `2026` — not
   `2026-09-15` — and flag confidence as POSSIBLE or VERIFY.

8. **Confidence transparency**: Every status assertion carries a confidence level
   (VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED). Use the same scale as the rest
   of the Legalcode skill family. Default mappings:
   - MNE entry confirmed + national-OJ entry confirmed: VERIFIED.
   - MNE entry confirmed but national-OJ entry not yet checked: LIKELY.
   - National-OJ entry confirmed but no MNE entry yet: LIKELY.
   - Secondary-tracker entry only, not yet cross-checked: POSSIBLE.
   - Inferred from negative evidence (no entry found): VERIFY.
   - No discovery run: ASSUMED.

9. **[VERIFY] markers inline**: Place [VERIFY] immediately after any unconfirmed
   claim, not in a footnote. Reviewers must see it where the claim appears. A row
   with multiple unverified claims gets multiple [VERIFY] markers.

10. **Persona-appropriate language**: A government self-assessment uses the
    declaratory voice ("Belgium has notified..."); a firm comparative briefing uses
    the analytical voice ("Belgium's notification status as of [date] is..."); a
    company operational brief uses the imperative voice ("Belgium NIS2 effective from
    [date]; ensure compliance by..."). Tune the surface language to the persona; the
    underlying matrix data is unchanged.

11. **No anchoring on the EU average where the EU average is stale or irrelevant** —
    Single Market and Competitiveness Scoreboard publishes per-edition averages, but
    these are aggregate across all directives. For a single-directive matrix,
    citation to the EU average is informative context, not a benchmark for risk
    scoring. Cite explicitly which Scoreboard edition the average is taken from.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When `legalcode-mcp` is available, use it to:

1. Run `search_laws` filtered to each MS jurisdiction with the directive's CELEX or
   short title as the query. This catches MS-specific national-law indexes that may
   surface NIMs faster than MNE for very recent adoptions.
2. Resolve ELI URIs for both the EU directive and national NIMs to confirm
   identifier accuracy.
3. Cross-check secondary-tracker entries against the primary national-OJ entry.
4. Save research output to `/tmp/legalcode-eu-transposition-tracker-research.md` and
   note in Glass Box: `legalcode_mcp: "Connected — research file at [path]"`.

### Without legalcode-mcp

Proceed with built-in reference tables (the per-MS table in the "Member State and EEA
EFTA State Coverage" section) and direct fetches against:

- N-Lex / MNE: `https://eur-lex.europa.eu/collection/n-law/mne.html`
- EUR-Lex national-law search: filter by directive CELEX
- National parliament APIs (per the "Member State and EEA EFTA State Coverage" table)
- National official journals (per the same table)

Mark all status assertions sourced solely from secondary trackers with
`source_tier: "secondary-tracker"` and apply downward confidence adjustments:

- MNE-confirmed entries: LIKELY (0.80) baseline (downgrade if national-OJ check is
  not run).
- National-OJ-confirmed entries: LIKELY (0.80) baseline (upgrade to VERIFIED only
  with MNE cross-check).
- Secondary-tracker-only entries: POSSIBLE (0.55) at most, with explicit `[VERIFY]`
  marker.
- Inferred from negative evidence: VERIFY (0.40), with the search method recorded in
  Glass Box.

### Related Skills Integration

| Trigger                                             | Invoke this skill                                 |
| --------------------------------------------------- | ------------------------------------------------- |
| Need obligation register before building matrix     | `legalcode-eu-directive-analyzer`                 |
| Need Article-by-Article correlation table           | `legalcode-eu-correlation-table-builder`          |
| Need conformity verdict per Article                 | `legalcode-eu-conformity-assessment`              |
| Need gold-plating analysis on the NIM               | `legalcode-eu-gold-plating-detector`              |
| Need EEA Joint Committee Decision pipeline status   | `legalcode-eea-incorporation-tracker`             |
| Need TFEU 258 / 260 procedure timeline              | `legalcode-eu-infringement-procedure-tracker`     |
| Need cross-MS privacy comparison (non-EU framework) | `legalcode-multi-jurisdiction-privacy-comparison` |

### National data sources

For Step 5 (Per-MS Status Discovery), the following national sources are first-line:

- **Riksdagen (SE)**: `https://data.riksdagen.se` — bills and adopted SFS by query.
- **Storting (NO)**: `https://data.stortinget.no` — Storting bills and adopted laws.
- **Folketinget (DK)**: `https://oda.ft.dk` — Folketing bills.
- **Bundestag (DE)**: `https://dip.bundestag.de` — German federal bills and adopted
  laws.
- **Assemblée nationale (FR)**: `https://data.assemblee-nationale.fr` — French
  National Assembly proceedings.
- **Althingi (IS)**: `https://www.althingi.is` — Icelandic parliament bills.
- **Eduskunta (FI)**: data exposed via Finlex.
- **Tweede Kamer (NL)**: data API exposed via the parliament's open-data programme.
- **Sejm (PL)**: data exposed via Sejm's open-data programme.
- **Camera dei deputati / Senato (IT)**: data exposed via Normattiva and the
  parliaments' websites.

For MS without a documented data API, fall back to the national OJ search and the
ministry portal.

---

## Output Format Template

The matrix is emitted in four formats: Markdown, JSON, AKN4EU, and LegalRuleML. All
four reference the same underlying data; the JSON is the canonical machine-readable
form, and the others are projections for human review and interoperability.

### 1. Markdown comparison table

```
## EU Transposition Matrix — [Directive short title]

Directive: [Directive (EU) YYYY/NNNN] — [Formal title] — CELEX [CELEXID] — OJ [reference]
Transposition deadline: [date]
EEA-relevance: [yes / no / pending JCD]
Matrix scope: [EU-27 / EU-27 + EFTA-3 / subset]
Last refreshed: [YYYY-MM-DD]
Persona / mode: [persona] / [operating mode]

### Headline metrics

- MS in scope: [N]
- Status COMPLETE + NOTIFIED: [N]
- Status COMPLETE + NOT-NOTIFIED: [N]
- Status PARTIAL: [N]
- Status DRAFT: [N]
- Status PLANNED / NOT-YET-PLANNED: [N]
- Status OVERDUE: [N]
- Status WITHDRAWN: [N]
- Transposition deficit (this directive): [%] (n/a if pre-deadline)
- MS exposed to Art. 260(3) TFEU first-referral penalty: [N]

### Per-MS status

| MS | Status | NIM citation | Notification | Adoption date | Effective date | Risk | Confidence | Source |
|----|--------|--------------|--------------|---------------|----------------|------|------------|--------|
| AT | [status] | [citation] | [notif-status] | [date] | [date] | [tier] | [level] | [URL] |
| BE | ... |
| BG | ... |
| ... |
| SE | ... |
| --- EFTA pillar (if EEA-relevant + JCD adopted) --- |
| IS | ... |
| NO | ... |
| LI | ... |

### Risk callouts

- CRITICAL risk MS: [list with one-line reason each]
- HIGH risk MS: [list]
- Art. 260(3) TFEU exposure: [list of MS]
```

### 2. Canonical JSON schema

```json
{
  "$schema": "https://schemas.legalcode/eu-transposition-matrix/v1.json",
  "matrix_id": "matrix-32022L2555-2026Q2",
  "directive": {
    "celex": "32022L2555",
    "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj",
    "short_title": "NIS2 Directive",
    "formal_title": "Directive (EU) 2022/2555 of 14 December 2022 ...",
    "oj_reference": "OJ L 333, 27.12.2022, p. 80",
    "in_force_date": "2023-01-16",
    "transposition_deadline": "2024-10-17",
    "staggered_deadlines": [
      {
        "applies_to_articles": ["3(2)", "12-13"],
        "deadline": "2025-04-17",
        "rationale": "Implementing-act-dependent provisions"
      }
    ],
    "is_legislative_directive": true,
    "art_289_basis": "Art. 114 TFEU, ordinary legislative procedure",
    "eea_relevance": "pending JCD assessment",
    "addressees": ["Member States"]
  },
  "matrix_metadata": {
    "matrix_scope": "EU-27",
    "last_refreshed": "2026-04-28",
    "next_review_due": "2026-05-28",
    "persona": "legal-firm",
    "operating_mode": "post-deadline-audit",
    "skill_version": "legalcode-eu-transposition-tracker@1.0.0"
  },
  "headline_metrics": {
    "ms_in_scope": 27,
    "status_complete_notified": 0,
    "status_complete_not_notified": 0,
    "status_partial": 0,
    "status_draft": 0,
    "status_planned": 0,
    "status_not_yet_planned": 0,
    "status_overdue": 0,
    "status_withdrawn": 0,
    "transposition_deficit_pct": null,
    "ms_with_art_260_3_exposure": []
  },
  "rows": [
    {
      "ms_code": "DE",
      "ms_name": "Germany",
      "row_type": "eu-27",
      "status": "draft",
      "draft_stage": "government bill in Bundestag committee",
      "nim_citations": [
        {
          "type": "primary",
          "citation": "[BGBl. citation when adopted]",
          "eli": null,
          "national_source_url": "https://dip.bundestag.de/...",
          "adoption_date": null,
          "effective_date": null
        }
      ],
      "transposition_deadline_applied": "2024-10-17",
      "days_overdue": 558,
      "notification_status": "not-notified",
      "notification_date": null,
      "notification_correlation_table_supplied": false,
      "notification_declaratory_commitment": null,
      "art_260_3_exposure": true,
      "art_258_lfn_status": "LFN sent November 2024 [VERIFY exact date]",
      "risk_dimensions": [
        {
          "dimension": "overdue + Art. 260(3) exposure",
          "likelihood": 5,
          "impact": 4,
          "score": 20,
          "tier": "CRITICAL",
          "rationale": "Deadline 17 Oct 2024 passed; no NIM adopted; Commission opened Art. 258 LFN [VERIFY]; Art. 260(3) qualification check satisfied (legislative directive Art. 114 basis; deadline passed; non-notification; Art. 258 procedure opened)."
        }
      ],
      "headline_risk_tier": "CRITICAL",
      "confidence": "LIKELY",
      "confidence_score": 0.78,
      "evidence_glass_box_ref": "row-DE-evidence-001",
      "notes": "[Verbatim per-MS notes — split-instrument transposition planned across IT-SiG and BSIG amendment]"
    },
    {
      "ms_code": "FR",
      "ms_name": "France",
      "row_type": "eu-27",
      "status": "draft",
      "draft_stage": "government bill in Assemblée nationale, first reading",
      "nim_citations": [
        {
          "type": "primary",
          "citation": "[JORF citation when adopted]",
          "eli": null,
          "national_source_url": "https://www.assemblee-nationale.fr/...",
          "adoption_date": null,
          "effective_date": null
        }
      ],
      "transposition_deadline_applied": "2024-10-17",
      "days_overdue": 558,
      "notification_status": "not-notified",
      "art_260_3_exposure": true,
      "art_258_lfn_status": "[VERIFY]",
      "risk_dimensions": [
        {
          "dimension": "overdue + Art. 260(3) exposure",
          "likelihood": 5,
          "impact": 4,
          "score": 20,
          "tier": "CRITICAL"
        }
      ],
      "headline_risk_tier": "CRITICAL",
      "confidence": "POSSIBLE",
      "confidence_score": 0.6,
      "evidence_glass_box_ref": "row-FR-evidence-001",
      "notes": "Loi de programmation militaire 2024 included partial cyber provisions [VERIFY scope vs. NIS2]; standalone NIS2 transposition bill SREN follow-up referenced [VERIFY]"
    },
    {
      "ms_code": "SE",
      "ms_name": "Sweden",
      "row_type": "eu-27",
      "status": "draft",
      "nim_citations": [
        {
          "type": "primary",
          "citation": "[SFS citation when adopted]",
          "eli": null,
          "national_source_url": "https://www.regeringen.se/...",
          "adoption_date": null,
          "effective_date": null
        }
      ],
      "transposition_deadline_applied": "2024-10-17",
      "notification_status": "not-notified",
      "art_260_3_exposure": true,
      "headline_risk_tier": "CRITICAL",
      "confidence": "POSSIBLE",
      "notes": "SOU 2024:18 (cybersecurity inquiry report) published; government bill announced [VERIFY current stage]"
    },
    {
      "ms_code": "PL",
      "ms_name": "Poland",
      "row_type": "eu-27",
      "status": "draft",
      "nim_citations": [
        {
          "type": "primary",
          "citation": "[Dz.U. citation when adopted]",
          "eli": null,
          "national_source_url": "https://www.sejm.gov.pl/...",
          "adoption_date": null,
          "effective_date": null
        }
      ],
      "transposition_deadline_applied": "2024-10-17",
      "notification_status": "not-notified",
      "art_260_3_exposure": true,
      "headline_risk_tier": "CRITICAL",
      "confidence": "POSSIBLE",
      "notes": "Amendment to Krajowy System Cyberbezpieczeństwa (KSC) Act referenced as the planned NIS2 transposition vehicle [VERIFY current status]"
    },
    {
      "ms_code": "IS",
      "ms_name": "Iceland",
      "row_type": "efta-pillar",
      "status": "n/a (JCD pending)",
      "eea_pipeline_status": "EEA-relevance assessment ongoing; no JCD adopted yet [VERIFY]",
      "transposition_deadline_applied": null,
      "notification_status": "n/a",
      "art_260_3_exposure": false,
      "art_31_sca_exposure": false,
      "headline_risk_tier": "NONE",
      "confidence": "VERIFY",
      "notes": "NIS2 EEA-relevance designation pending; coordinate with legalcode-eea-incorporation-tracker for JCD pipeline status"
    }
  ],
  "glass_box_audit": {
    "evidence_entries": [
      {
        "ref": "row-DE-evidence-001",
        "ms_code": "DE",
        "source_url": "https://dip.bundestag.de/...",
        "source_tier": "primary-parliament",
        "fetched_at": "2026-04-28T10:00:00Z",
        "evidence_quote": "[verbatim text from Bundestag bill page identifying NIS2 transposition status]"
      }
    ]
  }
}
```

### 3. AKN4EU XML stub (per-MS NIM document reference)

For each MS row with an adopted (or draft) NIM, emit an AKN4EU stub that references
the NIM as a national act:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:eu="http://publications.europa.eu/resource/akn/eu/v1">
  <act name="act" contains="originalVersion">
    <meta>
      <identification source="#legalcode-eu-transposition-tracker">
        <FRBRWork>
          <FRBRthis value="/akn/de/act/2024/[BGBl-id]"/>
          <FRBRuri value="/akn/de/act/2024/[BGBl-id]"/>
          <FRBRdate date="2024-XX-XX" name="adopted"/>
          <FRBRauthor href="#bundestag"/>
          <FRBRcountry value="de"/>
          <FRBRsubtype value="bundesgesetz"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/de/act/2024/[BGBl-id]/deu@2024-XX-XX"/>
          <FRBRuri value="/akn/de/act/2024/[BGBl-id]/deu@2024-XX-XX"/>
          <FRBRdate date="2024-XX-XX" name="published"/>
          <FRBRauthor href="#bundestag"/>
          <FRBRlanguage language="deu"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/de/act/2024/[BGBl-id]/deu@2024-XX-XX.xml"/>
          <FRBRuri value="/akn/de/act/2024/[BGBl-id]/deu@2024-XX-XX.xml"/>
          <FRBRdate date="2026-04-28" name="manifest"/>
          <FRBRauthor href="#legalcode-eu-transposition-tracker"/>
          <FRBRformat value="xml"/>
        </FRBRManifestation>
      </identification>
      <references source="#legalcode-eu-transposition-tracker">
        <TLCReference href="https://eur-lex.europa.eu/eli/dir/2022/2555/oj"
                      showAs="Directive (EU) 2022/2555 (NIS2)"
                      eId="dir-2022-2555"/>
        <TLCReference href="https://dip.bundestag.de/..."
                      showAs="Bundestag bill page"
                      eId="bundestag-bill"/>
      </references>
      <classification source="#legalcode-eu-transposition-tracker">
        <keyword value="transposition" showAs="Transposition of EU directive"/>
        <keyword value="cybersecurity" showAs="Cybersecurity"/>
        <keyword value="nis2" showAs="NIS2 Directive transposition"/>
      </classification>
      <lifecycle source="#legalcode-eu-transposition-tracker">
        <eventRef date="2024-10-17" type="generation"
                  source="#dir-2022-2555" eId="transposition-deadline"/>
        <eventRef date="2024-XX-XX" type="amendment"
                  source="#bundestag-bill" eId="adoption"/>
      </lifecycle>
    </meta>
    <preface>
      <p>[National-act preface text]</p>
    </preface>
    <body>
      <p>[Body would be populated when the NIM text is consumed — for the matrix
        artefact this stub references the FRBR identifier only and does not duplicate
        body text.]</p>
    </body>
  </act>
</akomaNtoso>
```

For each `<TLCReference>` entry, the matrix's evidence Glass Box must contain the
corresponding source URL + fetch date.

For draft NIMs (not yet adopted), the `<FRBRdate name="adopted">` is replaced with
`<FRBRdate name="proposed">` and the FRBR-Manifestation date carries the bill's
introduction date rather than its adoption date.

### 4. LegalRuleML aggregate-assertion stub

LegalRuleML is not a natural fit for tracker-matrix data because the matrix records
transposition status, not the underlying obligations. However, a useful round-trip
representation is the aggregate assertion "MS X has transposed obligation Y by NIM Z" —
expressed as a Constitutive rule whose Source is the directive's ELI, whose Party is
the MS, and whose binding statement is the NIM citation:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
                  xmlns:ruleml="http://ruleml.org/spec">
  <lrml:Constitutive key="ts-de-nis2-aggregate"
                     timestamp="2026-04-28T10:00:00Z">
    <lrml:Source>
      <lrml:appliesSource keyref="#dir-2022-2555-eli"/>
    </lrml:Source>
    <lrml:Party>
      <lrml:hasRole keyref="#mem-state-de"/>
    </lrml:Party>
    <lrml:appliesRules>
      <lrml:hasStatement key="stmt-de-nis2-status">
        <ruleml:Implies>
          <ruleml:if>
            <ruleml:Atom>
              <ruleml:Rel iri="#has-transposed"/>
              <ruleml:Var>x</ruleml:Var>
              <ruleml:Ind iri="#dir-2022-2555"/>
              <ruleml:Ind iri="#nim-de-bgbl-2024-XXXX"/>
            </ruleml:Atom>
          </ruleml:if>
          <ruleml:then>
            <ruleml:Atom>
              <ruleml:Rel iri="#status"/>
              <ruleml:Var>x</ruleml:Var>
              <ruleml:Ind iri="#status-complete"/>
            </ruleml:Atom>
          </ruleml:then>
        </ruleml:Implies>
      </lrml:hasStatement>
    </lrml:appliesRules>
  </lrml:Constitutive>

  <!-- Companion notification assertion -->
  <lrml:Constitutive key="ts-de-nis2-notification"
                     timestamp="2026-04-28T10:00:00Z">
    <lrml:Source>
      <lrml:appliesSource keyref="#tfeu-art-260-3"/>
    </lrml:Source>
    <lrml:Party>
      <lrml:hasRole keyref="#mem-state-de"/>
    </lrml:Party>
    <lrml:appliesRules>
      <lrml:hasStatement key="stmt-de-nis2-notification">
        <ruleml:Implies>
          <ruleml:if>
            <ruleml:Atom>
              <ruleml:Rel iri="#has-notified"/>
              <ruleml:Var>x</ruleml:Var>
              <ruleml:Ind iri="#dir-2022-2555"/>
            </ruleml:Atom>
          </ruleml:if>
          <ruleml:then>
            <ruleml:Atom>
              <ruleml:Rel iri="#notification-status"/>
              <ruleml:Var>x</ruleml:Var>
              <ruleml:Ind iri="#notif-not-notified"/>
            </ruleml:Atom>
          </ruleml:then>
        </ruleml:Implies>
      </lrml:hasStatement>
    </lrml:appliesRules>
  </lrml:Constitutive>
</lrml:LegalRuleML>
```

The LegalRuleML stub is an interoperability artefact rather than a primary deliverable;
its purpose is to allow a downstream policy-as-code engine, the LEOS round-trip toolchain,
or a parliamentary-tooling pipeline (UK National Archives, Italian Senate) to consume the
matrix data as deontic rules over the directive's underlying obligation register.

### 5. Glass Box audit trail

Every status assertion must have a Glass Box entry. The audit trail is a YAML block
emitted alongside the JSON.

```yaml
glass_box:
  skill_name: "legalcode-eu-transposition-tracker"
  matrix_id: "[matrix-id]"
  assessment_date: "[YYYY-MM-DD]"
  assessed_by: "AI-assisted; must be validated by qualified EU and Member State counsel"
  directive_celex: "[CELEX]"
  directive_short_title: "[short title]"
  matrix_scope: "[EU-27 / EU-27 + EFTA-3]"
  persona: "[persona]"
  operating_mode: "[mode]"
  legalcode_mcp: "[Connected — research file at /tmp/legalcode-eu-transposition-tracker-research.md / Not connected]"

  per_cell_evidence:
    - cell_ref: "row-DE-status"
      ms_code: "DE"
      column: "status"
      asserted_value: "draft"
      source_tier: "primary-parliament"
      source_url: "https://dip.bundestag.de/..."
      fetched_at: "[YYYY-MM-DDTHH:MM:SSZ]"
      evidence_quote: |
        [verbatim quote from source]
      confidence: "LIKELY"
      confidence_score: 0.80
      verify_markers: []

    - cell_ref: "row-DE-notification"
      ms_code: "DE"
      column: "notification_status"
      asserted_value: "not-notified"
      source_tier: "primary-mne"
      source_url: "https://eur-lex.europa.eu/collection/n-law/mne.html?...celex=32022L2555&country=DE"
      fetched_at: "[YYYY-MM-DDTHH:MM:SSZ]"
      evidence_quote: |
        "No measures notified for Member State Germany."
      confidence: "VERIFIED"
      confidence_score: 0.95
      verify_markers: []

    - cell_ref: "row-DE-art-260-3"
      ms_code: "DE"
      column: "art_260_3_exposure"
      asserted_value: true
      source_tier: "derived"
      source_url: null
      derivation: |
        Art. 260(3) qualification check:
          (1) directive is legislative within Art. 289 TFEU (Art. 114 ordinary legislative procedure): YES
          (2) transposition deadline 17 October 2024 has passed: YES
          (3) MS has not notified: YES (per row-DE-notification)
          (4) Commission has opened Art. 258 procedure: [VERIFY — LFN reportedly sent November 2024]
        All four conditions satisfied → Art. 260(3) exposure = true.
      fetched_at: "[YYYY-MM-DDTHH:MM:SSZ]"
      confidence: "LIKELY"
      confidence_score: 0.78
      verify_markers:
        - "[VERIFY] LFN exact date and reference"

    - cell_ref: "row-IS-status"
      ms_code: "IS"
      column: "status"
      asserted_value: "n/a (JCD pending)"
      source_tier: "derived"
      source_url: null
      derivation: |
        Cross-reference with legalcode-eea-incorporation-tracker:
          NIS2 EEA-relevance designation [VERIFY current status];
          no Joint Committee Decision adopted as of fetch date;
          per Art. 7 EEA + Art. 102 EEA, EFTA states have no domestic-implementation
          duty until JCD adoption.
      fetched_at: "[YYYY-MM-DDTHH:MM:SSZ]"
      confidence: "VERIFY"
      confidence_score: 0.45
      verify_markers:
        - "[VERIFY] confirm with EEA-incorporation tracker"

  assumptions:
    - "Default working language: English; directive transposition deadlines reconciled against English OJ version only"
    - "Secondary-tracker data (Linklaters NIS2 tracker, HSF NIS2 tracker) used as discovery starting point; primary-source verification run for CRITICAL and HIGH risk cells only"
    - "Historical-pattern weighting based on Single Market and Competitiveness Scoreboard editions through [YYYY]"

  limitations:
    - "Per-Article conformity verdicts are not produced by this skill; the matrix records facial transposition status, not on-the-merits conformity"
    - "Gold-plating signals are not assessed here; cross-reference legalcode-eu-gold-plating-detector"
    - "Exact dates of Commission infringement decisions [VERIFY] against the Commission's monthly infringement-decisions package"
    - "EFTA-pillar rows depend on legalcode-eea-incorporation-tracker output; absence of that output leaves IS / NO / LI cells at VERIFY confidence"

  reviewer_note: |
    AI-assisted matrix. Every CRITICAL or HIGH risk cell, every cell sourced from a
    secondary tracker, and every cell with [VERIFY] markers must be validated by
    qualified EU and Member State counsel before regulatory submission, board
    presentation, or use in infringement-procedure analysis.
```

---

## Worked example: NIS2 Directive (CELEX 32022L2555) — 5-MS slice

This worked example shows how the matrix is populated for the NIS2 Directive
(Directive (EU) 2022/2555 of 14 December 2022 on measures for a high common level of
cybersecurity across the Union, CELEX 32022L2555, OJ L 333, 27.12.2022, p. 80) for a
five-Member-State slice (Germany, France, Sweden, Poland, Iceland) as of early 2026.
The transposition deadline was **17 October 2024** (NIS2 Art. 41(1)).

**Important [VERIFY] flags throughout this example**: the exact NIM citations,
adoption dates, and Art. 258 LFN dates below should be verified against the primary
sources (national OJ entries; Commission monthly infringement-decisions package) before
relying on this example for any specific assertion. Where a published tracker
(Linklaters NIS2 tracker `https://www.linklaters.com/...`; Herbert Smith Freehills
NIS2 tracker; Ropes & Gray client alerts) was the discovery starting point, the cell
is marked `source_tier: secondary-tracker` and the corresponding [VERIFY] flag is set
explicitly.

### Germany (DE)

- **Status**: draft (government bill in Bundestag committee). Germany announced its
  NIS2-Umsetzungsgesetz (NIS2-UmsuCG) and an accompanying amendment to the BSI-Gesetz
  during 2024; the bill was reported to the Bundestag but had not been adopted by the
  17 October 2024 deadline. [VERIFY current Bundestag DIP entry — published trackers
  reported the bill in committee through Q1 2026.]
- **NIM citation**: pending adoption (would be cited as `BGBl. I YYYY, S. NNNN` once
  promulgated).
- **National source**: Bundestag DIP `https://dip.bundestag.de` filtered by NIS2
  short title.
- **Notification status**: not-notified (no MNE entry as of fetch date [VERIFY against
  N-Lex / MNE]).
- **Art. 260(3) exposure**: true. NIS2 is a legislative directive (Art. 114 TFEU,
  ordinary legislative procedure); deadline 17 October 2024 has passed;
  non-notification is documented; Commission opened an Art. 258 LFN against Germany
  for non-notification of NIS2 in the November 2024 monthly infringement-decisions
  package [VERIFY exact reference].
- **Headline risk tier**: CRITICAL.
- **Confidence**: LIKELY — primary-source parliament data confirms draft status;
  Art. 258 LFN reference [VERIFY] against Commission package.

### France (FR)

- **Status**: draft. France introduced a NIS2-transposition bill (the
  "projet de loi relative à la résilience des activités d'importance vitale, à la
  protection des infrastructures critiques, à la cybersécurité et à la résilience
  opérationnelle numérique du secteur financier" — colloquially "loi cybersécurité")
  in the Assemblée nationale; the bill incorporates NIS2, CER and DORA transposition
  in a single omnibus instrument [VERIFY current legislative stage]. Pre-existing
  cyber provisions in the Loi de programmation militaire 2024 (LPM 2024) cover certain
  NIS2 elements but do not constitute full transposition [VERIFY scope].
- **NIM citation**: pending adoption (would be cited as `JORF n°NNNN du DD MMMM YYYY
texte n° N`).
- **National source**: Assemblée nationale data API
  `https://data.assemblee-nationale.fr` filtered by directive 2022/2555.
- **Notification status**: not-notified [VERIFY].
- **Art. 260(3) exposure**: true (same qualification check satisfied as DE).
- **Headline risk tier**: CRITICAL.
- **Confidence**: POSSIBLE — secondary-tracker data is rich but national-source
  confirmation not yet completed for this example. [VERIFY against Légifrance and
  Assemblée nationale.]

### Sweden (SE)

- **Status**: draft. Sweden published the inquiry report SOU 2024:18 (NIS2 inquiry)
  and the government's NIS2 transposition bill was introduced in the Riksdag during
  2024 [VERIFY current Riksdagen entry]. Sweden missed the 17 October 2024 deadline.
- **NIM citation**: pending adoption (would be cited as `SFS YYYY:NNNN`).
- **National source**: Riksdagen data API `https://data.riksdagen.se` filtered by
  directive 2022/2555 / NIS2.
- **Notification status**: not-notified [VERIFY against MNE].
- **Art. 260(3) exposure**: true.
- **Headline risk tier**: CRITICAL.
- **Confidence**: POSSIBLE — published-tracker references suggest near-completion;
  Riksdagen API entry [VERIFY].

### Poland (PL)

- **Status**: draft. Poland's NIS2 transposition is structured as an amendment to
  the existing Krajowy System Cyberbezpieczeństwa (KSC, the Polish national
  cybersecurity system act of 5 July 2018, Dz.U. 2018 poz. 1560) [VERIFY current
  Sejm bill entry]. Poland missed the 17 October 2024 deadline.
- **NIM citation**: pending adoption (would be cited as `Dz.U. YYYY poz. NNNN`).
- **National source**: Sejm bill page `https://www.sejm.gov.pl` filtered by KSC
  amendment / NIS2.
- **Notification status**: not-notified [VERIFY].
- **Art. 260(3) exposure**: true.
- **Headline risk tier**: CRITICAL.
- **Confidence**: POSSIBLE.

### Iceland (IS) — EFTA pillar

- **Status**: n/a (JCD pending). NIS2 is text with EEA relevance per the directive's
  preamble [VERIFY recital reference]. As of early 2026, the EEA Joint Committee had
  not yet adopted a JCD incorporating NIS2 into the EEA Annexes [VERIFY against
  EEA-Lex `https://www.efta.int/eealaw`]. Until JCD adoption (and any Art. 103 EEA
  reservation lifting), Iceland has no domestic-implementation duty under the
  directive. The relevant pre-existing Icelandic cybersecurity legislation is lög
  nr. 78/2019 on cybersecurity [VERIFY scope vs. NIS2].
- **NIM citation**: not yet applicable.
- **National source**: Althingi.is `https://www.althingi.is`.
- **Notification status**: n/a.
- **Art. 260(3) exposure**: false (TFEU does not apply to EFTA states).
- **Art. 31 SCA exposure**: false (no incorporated obligation yet).
- **Headline risk tier**: NONE.
- **Confidence**: VERIFY — coordinate with `legalcode-eea-incorporation-tracker` for
  JCD pipeline status.

### Headline metrics for this 5-MS slice (illustrative)

- Status COMPLETE + NOTIFIED: 0
- Status DRAFT (overdue): 4 (DE, FR, SE, PL)
- Status n/a (JCD pending): 1 (IS)
- MS exposed to Art. 260(3) TFEU: 4 (DE, FR, SE, PL)
- Transposition deficit (this slice): 4/4 = 100% of EU-pillar MS in scope (well above
  Single Market and Competitiveness Scoreboard EU-pillar averages [VERIFY recent
  edition for baseline])

This worked example is illustrative. Every published tracker, every secondary-tracker
citation, and every Commission infringement reference must be verified against the
primary source before any of the values above are relied on for advice, board
reporting, or regulatory submission.

---

## Localization Notes

When adapting this skill to a specific MS or to a specific directive:

1. **MS-specific sources**: Replace generic parliament-API references with the
   specific MS's data endpoint (per the "Member State and EEA EFTA State Coverage"
   table). Where the MS does not expose a data API, document the OJ search URL and
   ministry portal as the substitute.
2. **MS-specific NIM citation format**: Use the canonical national format from the
   "NIM Citation Format" section. Do not translate to an English equivalent.
3. **EEA-relevance**: For directives that may or may not be EEA-relevant, run the
   recital-block read first; do not assume. Coordinate with
   `legalcode-eea-incorporation-tracker` before treating EFTA rows as parallel to
   EU rows.
4. **Language-version reconciliation**: Default to the OJ-published English / French /
   German triad as the working set; for substantive transposition-obligation
   ambiguities, expand to all 24 official versions per CILFIT (Case C-283/81,
   ECLI:EU:C:1982:335).
5. **Brexit historical context**: For directives in force pre-Brexit, the matrix's
   historical record may include a UK row; for directives adopted post-Brexit, UK is
   out of EU-pillar scope. Mark all UK-historical cells with the dates of UK EU
   membership as the period covered.
6. **Persona localisation**: A Belgian government persona will care about the
   Moniteur belge / Belgisch Staatsblad as the primary national OJ; a Swedish
   government persona will care about Riksdagen + SFS. Tune the surface presentation
   accordingly while preserving the canonical underlying matrix.
7. **Per-MS notes block**: Use the `notes` field on each row to capture MS-specific
   context (split-instrument transposition, omnibus acts, parliamentary configuration,
   constitutional-court annulment exposure, etc.) that the canonical schema does not
   accommodate.

---

## Provenance

Created by Legalcode (2026-04-28). Original synthesis based on:

- Better Regulation Toolbox 2023, Chapter 4 (Compliance, Implementation and Preparing
  Proposals): `https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`
- TFEU Art. 288(3): `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`
- TFEU Art. 258, 260(2), 260(3): EUR-Lex consolidated TFEU
- TEU Art. 4(3): EUR-Lex consolidated TEU (sincere-cooperation principle)
- _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573 (judgment of 8 July
  2019, OJ C 270/15, 12.8.2019) — first application of Art. 260(3) TFEU
- _Commission v Italy_, Case 22/87, ECLI:EU:C:1989:45 — administrative practice
  insufficient as transposition
- _Commission v Germany (TSE)_, Case C-518/07, ECLI:EU:C:2010:125 — transposition
  must be "complete, clear, and precise"
- _Francovich_, Joined Cases C-6/90 and C-9/90, ECLI:EU:C:1991:428 — MS damages
  liability for failure to transpose
- _Marleasing_, Case C-106/89, ECLI:EU:C:1990:395 — duty of conforming interpretation
- _CILFIT_, Case C-283/81, ECLI:EU:C:1982:335 — equal authenticity of language
  versions
- EEA Agreement Art. 7, 102, 103: `https://www.efta.int/legal-texts/eea`
- Surveillance and Court Agreement Art. 31 — ESA monitoring mandate
- Single Market and Competitiveness Scoreboard transposition methodology:
  `https://single-market-scoreboard.ec.europa.eu/`
- ESA Internal Market Scoreboard: `https://www.efta.int/`
- N-Lex / MNE database: `https://eur-lex.europa.eu/collection/n-law/mne.html`
- EUR-Lex Cellar SPARQL endpoint: `https://publications.europa.eu/webapi/rdf/sparql`
- ELI register technical information:
  `https://eur-lex.europa.eu/eli-register/technical_information.html`
- Akoma Ntoso (OASIS LegalDocML 1.0, 2018) AKN4EU subschema for EU institutions
- LegalRuleML (OASIS, 2021): `https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`
- NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022,
  p. 80) — used as the worked example throughout
- CSRD Directive (Directive (EU) 2022/2464, CELEX 32022L2464); CSDDD Directive
  (Directive (EU) 2024/1760, CELEX 32024L1760, transposition deadline 26 July 2026);
  Whistleblower Protection Directive (Directive (EU) 2019/1937, CELEX 32019L1937) —
  referenced in description and methodology
- Published transposition trackers (Linklaters, Herbert Smith Freehills, Ropes & Gray,
  A&O Shearman) — used as secondary-source baselines; every cell sourced from a
  tracker is flagged `source_tier: secondary-tracker` and requires primary-source
  verification before regulatory or board use
- All statutory, regulatory, case-law and CELEX/ELI/ECLI references carry
  hallucination risk and must be verified against authoritative sources (EUR-Lex,
  CURIA, national official journals, MNE) before use in regulatory submissions,
  infringement proceedings, or board reporting
