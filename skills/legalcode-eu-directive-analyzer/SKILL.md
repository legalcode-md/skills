---
name: legalcode-eu-directive-analyzer
description: >
  Extracts a versioned, machine-readable obligation register from any EU directive
  identified by CELEX or supplied as text. The register is the foundation artefact
  consumed by every other skill in the seven-skill EU Legislative Compliance suite:
  the per-Member-State implementation matrix, the Commission-format correlation table,
  the per-article conformity verdict, the gold-plating detector, the EEA Joint Committee
  Decision tracker, and the TFEU 258/260 infringement procedure tracker. For each
  operative provision the skill emits one row carrying the article reference, the
  deontic operator (must / shall / may / shall-not / should), the addressee (Member
  State / national competent authority / private actor / EU institution / individual),
  the compliance deadline (transposition deadline first, then ongoing application
  dates and review-clause dates), a Member-State-option flag where the directive grants
  national discretion, recital cross-references, IATE-aligned key terms in all 24
  authentic language versions, and a citation chain from CELEX through the European
  Legislation Identifier (ELI) URI down to article, paragraph, and sentence. Worked
  examples are drawn from NIS2 (Directive (EU) 2022/2555, CELEX 32022L2555), AI Act
  (Regulation (EU) 2024/1689, CELEX 32024R1689 — used for contrast), CSRD (Directive
  (EU) 2022/2464, CELEX 32022L2464), CSDDD (Directive (EU) 2024/1760, CELEX 32024L1760),
  GDPR (Regulation (EU) 2016/679, CELEX 32016R0679 — for contrast), and DORA (Regulation
  (EU) 2022/2554). Anchored in TFEU Art. 288 (instrument hierarchy) and TFEU Art. 4(3)
  (sincere cooperation, the textual foundation of the transposition obligation), with
  CJEU doctrine on direct effect (Becker C-8/81; Marshall C-152/84; Faccini Dori
  C-91/92) and consistent interpretation (Von Colson C-14/83; Marleasing C-106/89).
  Outputs are emitted in four formats — Markdown (human review), JSON (canonical
  machine schema consumed by sibling skills), Akoma Ntoso AKN4EU XML (round-trip to
  LEOS), and LegalRuleML (round-trip to policy-as-code engines). Operating modes:
  fresh-extract, update-existing, EEA-scope, contested-language-version. Personas:
  government / EU institution, legal firm, company, trade federation. Jurisdictional
  scope: EU-27 plus the three EEA-EFTA states (Iceland, Liechtenstein, Norway) where
  the directive is incorporated into the EEA Annexes by Joint Committee Decision.
allowed-tools: Read, Write, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode EU Directive Analyzer

> **Disclaimer**: This skill provides a framework for AI-assisted EU directive
> obligation extraction. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs should be reviewed by qualified legal
> counsel licensed in the relevant jurisdictions before use. This skill does not
> replace formal legal review by qualified EU and Member State counsel. It produces
> a structured framework to support a human-led review — not a substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and Member State
> implementing measures must be verified against authoritative sources (EUR-Lex, CURIA,
> national official journals) before use in regulatory submissions, infringement
> proceedings, or board reporting. EU law evolves continuously; transposition status,
> infringement procedures, and consolidated text versions change frequently. The 24
> official EU language versions of every act are equally authentic; reconcile divergent
> versions before relying on any single language for a definitive interpretation
> (CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95).

## Purpose and Scope

This skill takes an EU directive — identified by CELEX number, ELI URI, or supplied
as full text — and produces a versioned **obligation register**. The register is the
canonical machine-readable representation of every operative obligation, permission,
and prohibition carried by the directive, the entities those provisions are addressed
to, the deadlines by which those entities must act, and the recital and cross-reference
context required for purposive interpretation.

The register is the **foundation artefact** of the seven-skill EU Legislative Compliance
suite. Every downstream skill — transposition tracker, correlation-table builder,
conformity assessment, gold-plating detector, EEA incorporation tracker, infringement
procedure tracker — consumes the register. Consequently, the schema published in this
skill is load-bearing: schema changes here propagate across the suite, so any breaking
change must be versioned and announced in the `schema_version` field documented below.

The register's job is to make a directive **operationally tractable** for the actors
who must comply with it: a ministry drafting a national implementing measure (NIM),
a law firm advising a client on operational impact, a company sizing a compliance
programme, or a trade federation drafting a position paper during transposition. The
same source text — Directive (EU) 2022/2555 (NIS2) — produces materially different
deliverables for each persona, and the register's row-level granularity is what makes
that branching possible without re-parsing the directive every time.

**Covers:**
- CELEX → ELI → 24 authentic language version identifier resolution.
- Structural classification: recitals (interpretive — *Roquette Frères* C-110/03),
  definitions, operative articles (the source of obligations), and final
  provisions (transposition deadline, entry into force, addressees, repeal).
- One register row per operative obligation: deontic operator, addressee,
  deadline, MS-option flag, recital and internal cross-references, citation chain.
- Member-State option and derogation cataloguing — the directive's "flexibility
  surface" feeding the gold-plating detector.
- Compliance-deadline taxonomy: transposition deadline (TEU Art. 4(3) sincere
  cooperation; TFEU Art. 260(3) penalty exposure on non-notification), application
  date, review clause, sunset clause, phased deadlines.
- Cross-reference mapping (recitals ↔ articles; article ↔ article; directive ↔
  external acts).
- Reconciliation across the 24 authentic language versions using IATE; divergences
  flagged per *CILFIT* (C-283/81), *Codan* (C-236/97), *EMU Tabac* (C-296/95).
- EEA-relevance assessment per Art. 7 EEA (OJ flag + subject-matter scoping).
- Deterministic source-validation: every operative provision produces exactly one
  register row or carries a documented exclusion reason.
- Four-format output: Markdown, JSON (canonical schema), AKN4EU XML (LEOS
  round-trip), LegalRuleML (policy-as-code round-trip).
- Glass Box audit trail capturing row provenance, language reconciliation
  decisions, and exclusion reasons.

**Does not:**
- Track per-MS transposition status (`legalcode-eu-transposition-tracker`).
- Build the two-column correlation table (`legalcode-eu-correlation-table-builder`).
- Issue per-article conformity verdicts (`legalcode-eu-conformity-assessment`).
- Detect national over-implementation (`legalcode-eu-gold-plating-detector`).
- Track EEA Joint Committee Decisions (`legalcode-eea-incorporation-tracker`).
- Track TFEU 258/260 or ESA Art. 31 SCA procedures
  (`legalcode-eu-infringement-procedure-tracker`).
- Provide legal advice or substitute for qualified counsel.
- Translate the directive — IATE-based reconciliation is not translation.
- Analyse regulations as if they were directives. Regulations (TFEU Art. 288(2))
  are directly applicable; where a regulation is supplied, the skill emits a
  register but flags transposition-deadline, MS-option, and gold-plating columns
  as not applicable.

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes
/ produces the following artefacts:

- **Consumes**: a CELEX identifier (e.g. `32022L2555`), an ELI URI, or the
  directive text itself. Optionally, a pre-existing partial register for the same
  directive can be supplied for incremental update.
- **Produces**: the canonical obligation register in four output formats — Markdown
  (human review), JSON (canonical machine schema, load-bearing for sibling skills),
  AKN4EU XML (LEOS round-trip), LegalRuleML (policy-as-code round-trip).

Sibling skills:

- `legalcode-eu-directive-analyzer` — extracts the obligation register (this skill).
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix; consumes the
  register to know what each MS must transpose, by when, with how much discretion.
- `legalcode-eu-correlation-table-builder` — Commission-format two-column table;
  uses the register's article column as the left column.
- `legalcode-eu-conformity-assessment` — per-article verdict (correct / partial /
  incorrect / not transposed); each register row is the unit of assessment.
- `legalcode-eu-gold-plating-detector` — flags national over-implementation; uses
  the MS-option flag column.
- `legalcode-eea-incorporation-tracker` — Joint Committee Decision tracking; uses
  the EEA-relevance flag.
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 timeline; uses
  transposition and application deadlines for risk scoring.

The **shared reference pack** carrying language regime, IATE quick-reference, ELI
template, AKN4EU subschema, and Member State NIM publication channels lives co-located
with this skill at:
`skills/general/compliance/legalcode-eu-directive-analyzer/references/eu-legislative-data/`

Sibling skills cross-reference the pack via:
`See [shared EU legislative-data pack](../../legalcode-eu-directive-analyzer/references/eu-legislative-data/)`

---

## Jurisdiction and Governing Law

This skill operates in the EU/EEA legal order. The instrument hierarchy is set by
the Treaty on the Functioning of the European Union (TFEU) Article 288:

> "To exercise the Union's competences, the institutions shall adopt regulations,
> directives, decisions, recommendations and opinions. … A directive shall be binding,
> as to the result to be achieved, upon each Member State to which it is addressed,
> but shall leave to the national authorities the choice of form and methods."
>
> — TFEU Art. 288(3), consolidated at
> `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`

The transposition obligation flows from TFEU Art. 4(3) (sincere cooperation):

> "Pursuant to the principle of sincere cooperation, the Union and the Member States
> shall, in full mutual respect, assist each other in carrying out tasks which flow
> from the Treaties. The Member States shall take any appropriate measure, general or
> particular, to ensure fulfilment of the obligations arising out of the Treaties or
> resulting from the acts of the institutions of the Union."
>
> — TEU Art. 4(3) (note: sincere cooperation lives in the TEU, not the TFEU; the
> register and the audit trail must use the correct treaty reference)

The penalty regime for non-transposition of legislative directives sits in TFEU
Art. 260(3) (Lisbon innovation; first applied in *Commission v Belgium*,
Case C-543/17, ECLI:EU:C:2019:573).

Direct-effect doctrine governs whether private parties can rely on an un-transposed
directive against a Member State (vertical direct effect, *Becker*, Case C-8/81,
ECLI:EU:C:1982:7) and confirms that directives have **no horizontal direct effect**
between private parties (*Marshall*, Case C-152/84, ECLI:EU:C:1986:84; reaffirmed in
*Faccini Dori*, Case C-91/92, ECLI:EU:C:1994:292). The interpretive obligation —
that national courts must construe national law in conformity with the directive
"so far as possible" — was established in *Von Colson* (Case C-14/83,
ECLI:EU:C:1984:153) and extended in *Marleasing* (Case C-106/89, ECLI:EU:C:1990:395).

Multilingualism is governed by Council Regulation No 1 of 1958
(`https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`), which establishes the 24
official languages. All language versions of an act published in the OJ are equally
authentic. Where they diverge, *CILFIT* (Case C-283/81, ECLI:EU:C:1982:335),
*Codan* (Case C-236/97, ECLI:EU:C:1998:208), and *EMU Tabac* (Case C-296/95,
ECLI:EU:C:1998:152) require that the provision be interpreted by reference to
purpose and general scheme rather than by privileging a single language.

For EEA-relevant directives, incorporation into the EEA Agreement is governed by
EEA Art. 7 (incorporation procedure), Art. 102 (Joint Committee Decision), and
Art. 103 (constitutional reservations / parliamentary approval suspension). Once
incorporated, ESA monitors implementation under Art. 31 SCA (Surveillance and
Court Agreement) for the EFTA pillar (Iceland, Liechtenstein, Norway).

[JURISDICTION-SPECIFIC: EU-27] Directives bind every Member State as to result; each
Member State chooses form and methods (TFEU Art. 288(3)). The transposition deadline
is a hard deadline; non-notification triggers TFEU Art. 260(3) lump-sum and penalty-
payment exposure on first CJEU referral.

[JURISDICTION-SPECIFIC: EEA-EFTA — Iceland, Liechtenstein, Norway] Directives apply
only after incorporation by Joint Committee Decision (EEA Art. 102) and any
constitutional-reservation lift (EEA Art. 103). Where Art. 103 is invoked, the
directive's EEA application is suspended pending parliamentary approval. The skill
flags EEA-relevance but does not track JCD adoption — that is `legalcode-eea-
incorporation-tracker`'s remit.

[JURISDICTION-SPECIFIC: Switzerland] Switzerland is not in the EEA; EU directives
do not apply. Bilateral agreements may incorporate specific acquis, but those are
out of scope for this skill.

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
- Persona: Company (most general; least optimised but always-correct)
- Operating mode: Fresh-extract
- Working language: English (`eng`) for the directive parse; reconcile divergence
  flags against French (`fra`) and German (`deu`) as drafting-language sanity checks
- Output formats: emit all four (Markdown, JSON, AKN4EU, LegalRuleML)
- EEA-relevance: trust the OJ "(Text with EEA relevance)" flag where present;
  otherwise flag as `unknown` for the EEA tracker to resolve

---

## Workflow

### Step 1: Accept Input

Accept input in any of these forms:

- **CELEX identifier**: e.g. `32022L2555` (NIS2). The 11-character CELEX is the most
  precise identifier — sector digit (`3` = legal acts), four-digit year (`2022`), type
  letter (`L` = directive; `R` = regulation; `D` = decision), four-digit running
  number (`2555`).
- **ELI URI**: e.g. `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng`. ELI is the
  HTTP URI scheme; the path component carries domain (`eli`), type (`dir`), year
  (`2022`), running number (`2555`), point in the law lifecycle (`oj` for
  OJ-as-published; `oj/2024-04-15` for a specific consolidated version), and
  language token (`eng`, `fra`, `deu`, etc.).
- **Directive title + OJ reference**: e.g. "Directive (EU) 2022/2555 of 14 December
  2022 on measures for a high common level of cybersecurity across the Union, OJ L
  333, 27.12.2022, p. 80". Lowest-precision identifier; the skill resolves it to a
  CELEX before proceeding.
- **Pasted text**: the full text of the directive, where the user is working from a
  draft not yet published in OJ (e.g. a Council general approach text), or where
  EUR-Lex retrieval is unavailable. The skill flags pasted-text input as
  `provenance: pasted` in the Glass Box and applies stricter source-validation.
- **Pre-existing partial register**: a JSON file in this skill's schema, where the
  user is updating an earlier extraction (for example, after a Commission corrigendum
  or after the 24th language version was published). The skill performs an
  incremental merge and flags every changed row.

Minimum required context to proceed:
- One of the four identifier forms above, **or** the pasted directive text.
- The persona (next step), unless the user has already declared one.
- The operating mode (next step), unless the user has already declared one.

If no input is provided, ask the user to supply a CELEX identifier or paste the
directive text. Do not invent a directive to analyse.

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

**Persona-driven branches in the workflow:**

| Persona | Filter applied to register | Output emphasis |
|---|---|---|
| Government / EU institution | All addressees retained; MS-option column populated with `national_discretion_zone` flag for transposition drafting | Markdown register + AKN4EU XML (LEOS round-trip); LegalRuleML for downstream NIM-as-code |
| Legal firm | All addressees retained; the `addressee_class` filter is exposed in JSON for client-specific filtering downstream | Markdown register with deep recital cross-references; JSON for client-side spreadsheet workflows |
| Company | Filter to `addressee_class ∈ {private_actor, individual}`; MS Member State and EU institution rows are summarised, not row-by-row | Markdown register filtered to private-actor obligations, with operational impact column |
| Trade federation | All addressees retained; per-row `national_discretion_zone` flag highlighted to identify lobbying surface | Markdown register foregrounding MS-option rows; JSON for cross-MS scoreboarding |

⟁ CLARIFY — Operating Mode

The skill supports four operating modes that change which steps execute and which
outputs are emitted.

1. **Fresh-extract**: First-time extraction of the obligation register from a directive.
   Executes Steps 3–11 in full.
2. **Update-existing**: Incremental update of a previously-emitted register, e.g.
   after a corrigendum, an OJ-published rectification, or the late publication of
   the 24th language version. Executes Step 3 (re-resolve identifiers), Step 8
   (re-reconcile across language versions), and Step 11 (re-emit outputs); skips
   Steps 4–7 for unchanged articles.
3. **EEA-scope**: Extracts the register **and** runs the EEA-relevance assessment in
   detail (Step 9 includes the EEA-Annex subject-matter classification). Hands off
   the EEA-relevance flag to `legalcode-eea-incorporation-tracker`.
4. **Contested-language-version**: A specific language-version divergence has been
   raised (typically by counsel or a national parliament). Steps 3–7 execute
   normally; Step 8 expands into a multi-language reconciliation table with
   *CILFIT* methodology applied to every contested term.

**Why this matters**: Modes 2–4 trim or expand the workflow. Running fresh-extract on
an update wastes effort; running update-existing on a fresh case under-validates the
register against source.

### Step 3: Resolve Identifiers

Map the input onto the complete identifier triple **CELEX → ELI → 24 language URIs**.

- **3a. CELEX.** Sector digit `3` for legal acts in force, `5` for proposals,
  `6` for case law. Directive type letter is `L`; regulation `R`; decision `D`.
  Worked-example CELEX values used throughout this skill:

  | Input | CELEX | Type | Note |
  |---|---|---|---|
  | NIS2 | `32022L2555` | Directive | Transposition deadline 17 October 2024 |
  | AI Act | `32024R1689` | Regulation | Directly applicable; flag inapplicable columns |
  | CSRD | `32022L2464` | Directive | Phased application by undertaking size |
  | CSDDD | `32024L1760` | Directive | Transposition deadline 26 July 2026 |
  | GDPR | `32016R0679` | Regulation | Contrast |
  | DORA | `32022R2554` | Regulation | Contrast |
  | Whistleblower Directive | `32019L1937` | Directive | Transposed by 17 December 2021 |

- **3b. ELI URI.** Template:
  `https://eur-lex.europa.eu/eli/dir/{year}/{number}/oj/{lang_token}` (replace
  `dir` with `reg` for regulations). Consolidated versions append a date:
  `/oj/2024-04-15/eng`. Spec:
  `https://eur-lex.europa.eu/eli-register/technical_information.html`.

- **3c. 24 language tokens** (ISO 639-3): `bul`, `ces`, `dan`, `deu`, `ell`,
  `eng`, `est`, `fin`, `fra`, `gle`, `hrv`, `hun`, `ita`, `lav`, `lit`, `mlt`,
  `nld`, `pol`, `por`, `ron`, `slk`, `slv`, `spa`, `swe`. All 24 equally
  authentic (Reg. 1/1958; *CILFIT* C-283/81). Missing versions: record in Glass
  Box; set `language_coverage` accordingly.

- **3d. EEA-relevance.** The OJ marker "(Text with EEA relevance)" sits
  immediately after the title. Present → `eea_relevance: declared`; absent →
  `not_declared` (subject to subject-matter scoping in Step 9). The flag captures
  EU-side intent only; EEA application requires a JCD under Art. 102 EEA.

- **3e. Adopting institutions and legal basis.** Read the "Having regard to"
  citations block. Capture legal basis (NIS2 cites TFEU Art. 114 — internal
  market harmonisation), adopting institutions (Parliament + Council under OLP),
  and any EESC / CoR opinions cited.

### Step 4: Parse Operative Articles

Distinguish four structural zones; each is treated differently:

| Zone | Treatment |
|---|---|
| **Preamble / citations** ("Having regard to …") | Metadata (legal basis, procedure, opinions). Not obligation rows. |
| **Recitals (numbered "Whereas …")** | NIS2 has 142. Captured for purposive interpretation; cross-referenced from operative articles. **Not** themselves a source of obligation (*Roquette Frères* C-110/03). |
| **Definitions article(s)** | Glossary; disambiguates addressees. Not obligation rows. |
| **Operative articles** | Source of register rows. One operative provision → one row. |
| **Final provisions** | Transposition; entry into force; addressees; repeal. Populate `transposition_deadline` and `entry_into_force_date`. |

- **4a. Article-boundary detection.** Rigid structure: arabic numerals for
  articles; parenthesised arabic for paragraphs; letters for points; roman or
  arabic in parentheses for indents. Deepest routine citation: `Art. 21(2)(d)`
  (NIS2 supply-chain control); some directives go to `Art. 21(2)(d)(i)`.
- **4b. Final-provision cues.** Transposition ("Member States shall bring into
  force the laws, regulations and administrative provisions necessary to comply
  …"); review ("By [date], the Commission shall review …"); entry into force
  ("on the [Nth] day following … publication in the Official Journal …");
  addressees ("This Directive is addressed to the Member States"); repeal.
- **4c. Annexes.** Annex content referenced from an operative article inherits
  that article's deontic status. Always cite as "Art. 3(1) and Annex I", not
  "Annex I" alone.

### Step 5: Extract Obligations

Walk every operative article. For each operative provision (typically one sentence
or clause), produce one register row populated with the schema in **Obligation
Register Schema**.

- **5a. Deontic operator.** Read the verb; apply the **Deontic Operator Taxonomy**.
  EU directives are formulaic — `shall` (English), `doit` (French), `muss` /
  `haben zu` (German). Operative `should` is anomalous; flag.
- **5b. Addressee.** Read the subject; classify per the **Addressee Taxonomy**
  (member_state / national_competent_authority / private_actor / eu_institution /
  individual).
- **5c. Deadline.** Three types: transposition deadline (from the transposition
  article); application date (may lag transposition for phased rules — CSRD
  applies to large undertakings from FY2024, SMEs from FY2026, third-country
  groups from FY2028); ongoing deadlines (review clauses, sunset clauses,
  periodic-reporting deadlines, e.g. NIS2 Art. 40 review by 17 October 2027).
- **5d. MS-option flag.** Cues: "Member States may …", "may decide that …",
  "may provide that …", "by way of derogation … may …", "shall ensure that …
  For that purpose, Member States may choose …". Every MS-option sets
  `ms_option_flag: true` with `ms_option_type` from Step 6 typology.
- **5e. Recital cross-references.** Capture every recital cited explicitly ("as
  referred to in recital (54)") or substantively linked.
- **5f. Internal and external cross-references.** Internal: "in accordance with
  Article 23(1)". External: "in accordance with Regulation (EU) 2016/679",
  "Directive 2000/31/EC". Each external reference resolves to a CELEX.
- **5g. Sentence-level provenance.** Article + paragraph + point + sentence
  number; the canonical English text in `obligation_text_eng`; other 23 languages
  in the `language_versions` map.

### Step 6: Identify MS Options and Derogations

A focused second pass enumerating the directive's Member-State flexibility surface
— the input to `legalcode-eu-gold-plating-detector`.

- **6a. Every MS-option clause.** For each occurrence, populate `ms_option_id`
  (`MS-OPT-{article}-{paragraph}-{seq}`); `ms_option_type` (`permission` /
  `conditional_permission` / `regulatory_option` / `implementation_discretion` /
  `derogation` / `extension`); `discretion_scope` (one-sentence description);
  `default_result`; `gold_plating_risk_zone` (`low` for tight derogations; `high`
  for open "Member States may impose stricter measures" clauses).
- **6b. Derogations.** Sub-class of MS-options where the default rule is
  suspended for specified MS, sectors, or periods. Capture sunset dates.
- **6c. Harmonisation framing.** Minimum harmonisation (NIS2: "Member States may
  … adopt or maintain provisions ensuring a higher level of cybersecurity") opens
  the gold-plating surface; maximum harmonisation (rare; some consumer-protection
  directives) closes it. This framing dominates the downstream gold-plating
  analysis.

### Step 7: Map Cross-References

- **7a. Recital ↔ article matrix.** Bidirectional. Explicit "as referred to in
  recital (N)" phrasing is deterministic; derived overlaps are marked
  `derived: true` for human review.
- **7b. Internal article cross-reference graph.** Directed graph between
  articles; downstream skills follow obligation chains via this graph.
- **7c. External act cross-references.** Resolve every reference to another EU
  act to CELEX + ELI. Where a referenced act is not yet adopted (e.g. a
  Commission Implementing Regulation pending), flag
  `pending_secondary_legislation: true`.
- **7d. International standards / soft law.** NIS2 Art. 21 references "European
  or international standards" (ISO/IEC 27001, ENISA guidelines). Captured but
  treated as informative, not operative.

### Step 8: Reconcile Across Language Versions

All 24 language versions are equally authentic (Reg. 1/1958; *CILFIT* C-283/81).
Cross-check the English extraction against at least French (frequent drafting
language) and German (large-economy MS), and ideally all 24.

- **8a. IATE-aligned key-term reconciliation.** Retrieve IATE entries
  (`https://iate.europa.eu/`) for every defined term. Where IATE conflicts with
  the directive's defined term, prefer the directive (*lex specialis*) and note
  the IATE divergence.
- **8b. Apply CILFIT methodology to divergence.** Where language versions
  diverge, *CILFIT* (C-283/81), *Codan* (C-236/97), and *EMU Tabac* (C-296/95)
  require interpretation "in the light of the versions in all the other
  [official] languages" and "by reference to the purpose and general scheme".
  Record the divergence in `language_divergence`, capture candidate
  interpretations, identify the recital(s) establishing purpose, tentatively
  privilege the purpose-consistent reading, flag for counsel.
- **8c. Mark coverage gaps.** Set `language_coverage: N/24` and list languages
  reconciled; downstream skills must surface the gap.
- **8d. Drafting-language heritage.** Modern drafting is predominantly anglophone
  (post-2004); historically French. Note where historical drafting heritage
  affects interpretation.

### Step 9: Compute Compliance Deadlines

- **9a. Transposition deadline** — from the transposition article (NIS2 Art. 41(1):
  17 October 2024; CSDDD Art. 37: 26 July 2026). Applies to every Member-State
  row absent an explicit per-provision carve-out.
- **9b. Application date** — where the directive prescribes a substantive date
  later than transposition (CSRD phases: large undertakings FY2024 → SMEs FY2026
  → third-country groups FY2028), populate per-row `application_date` and
  capture the phasing in `application_phasing`.
- **9c. Review clauses** — Commission obligations (NIS2 Art. 40: review by
  17 October 2027 and every 36 months thereafter). EU-institution addressee.
- **9d. Sunset clauses** — fixed-date expiry of a derogation; populate
  `sunset_date`.
- **9e. Periodic-reporting deadlines** — recurring obligations (NIS2 Art. 23:
  early warning within 24h, incident notification within 72h, final report within
  1 month). Each emits its own row with the recurrence pattern.

### Step 10: Validate Against Source

The deterministic correctness pass. Every operative provision must produce exactly
one register row or carry a documented exclusion reason; over- and under-extraction
are both errors.

- **10a. Operative-provision count.** Walk every paragraph and point; confirm a
  row exists for each sentence-level obligation. Multiple obligations in one
  paragraph produce multiple rows.
- **10b. Exclusion register.** Reasons: `definitional` (inherited by other rows);
  `structural` (procedural — publication, addressees, entry into force);
  `descriptive` (restates Treaty rule or scope without new obligation);
  `cross_reference_only` (references another act without fresh obligation).
- **10c. Counter-checks.** Every MS row has a `transposition_deadline`; every
  row has a citation chain; MS-option flagged-row count matches "Member States
  may" cue count; article numbering is contiguous (corrigenda excepted).
- **10d. Self-interrogation: "What did I miss?"** Which clauses might counsel
  argue operative that I treated as descriptive? Where is the addressee ambiguous
  (a "competent authority" may be national, EU, or both)? Document every
  borderline judgment in the Glass Box.

### Step 11: Emit Outputs

Emit the four output formats per the **Output Format Template** section. Persona
filtering applies at this step (see Step 2 table). The outputs are:

1. **Markdown** — human review format, with full citations and a tabular register
   rendering.
2. **JSON** — canonical machine schema; consumed by every sibling skill.
3. **AKN4EU XML** — Akoma Ntoso AKN4EU subschema; round-trips to LEOS and other
   parliamentary tooling.
4. **LegalRuleML** — OASIS LegalRuleML 1.0 stub; round-trips to deontic-logic and
   policy-as-code engines.

Each output format must validate against its respective schema. Stubs in this skill
are real, not placeholders — see the worked NIS2 Art. 21 example below.

---

## Obligation Register Schema

This is the canonical schema. It is **load-bearing** for downstream skills; any change
must be versioned via `schema_version`.

```json
{
  "schema_version": "1.0.0",
  "directive": {
    "celex": "32022L2555",
    "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
    "short_title": "NIS2 Directive",
    "formal_title": "Directive (EU) 2022/2555 of the European Parliament and of the Council of 14 December 2022 on measures for a high common level of cybersecurity across the Union, amending Regulation (EU) No 910/2014 and Directive (EU) 2018/1972, and repealing Directive (EU) 2016/1148 (NIS 2 Directive)",
    "oj_reference": "OJ L 333, 27.12.2022, p. 80",
    "legal_basis": ["TFEU Art. 114"],
    "adopting_institutions": ["European Parliament", "Council"],
    "procedure": "ordinary_legislative_procedure",
    "transposition_deadline": "2024-10-17",
    "entry_into_force": "2023-01-16",
    "eea_relevance": "declared",
    "language_coverage": "24/24",
    "language_versions": {
      "eng": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
      "fra": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/fra",
      "deu": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/deu"
    }
  },
  "register": [
    {
      "row_id": "OBL-32022L2555-021-002-001",
      "article": "21",
      "paragraph": "2",
      "point": null,
      "sentence_no": 1,
      "deontic_operator": "shall",
      "addressee_class": "private_actor",
      "addressee_specific": "essential and important entities",
      "obligation_text_eng": "The measures referred to in paragraph 1 shall be based on an all-hazards approach that aims to protect network and information systems and the physical environment of those systems from incidents, and shall include at least the following: …",
      "transposition_deadline": "2024-10-17",
      "application_date": "2024-10-18",
      "ms_option_flag": false,
      "ms_option_type": null,
      "recital_xrefs": [49, 77, 78, 79],
      "internal_xrefs": ["Art. 21(1)", "Annex I", "Annex II"],
      "external_xrefs": [],
      "iate_terms": [
        {
          "term_eng": "essential entities",
          "term_fra": "entités essentielles",
          "term_deu": "wesentliche Einrichtungen",
          "iate_id": "3622139"
        }
      ],
      "language_divergence": [],
      "citation_chain": {
        "celex": "32022L2555",
        "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
        "article": "Art. 21(2)",
        "oj_page": "L 333/107"
      },
      "confidence": "VERIFIED",
      "provenance": {
        "source": "eur-lex",
        "extracted_at": "2026-04-28T00:00:00Z",
        "extractor": "legalcode-eu-directive-analyzer@1.0.0"
      }
    }
  ],
  "ms_options": [
    {
      "ms_option_id": "MS-OPT-32022L2555-021-005-001",
      "article": "21",
      "paragraph": "5",
      "ms_option_type": "implementation_discretion",
      "discretion_scope": "Member States may, with regard to entities falling within the scope of this Directive, adopt or maintain provisions ensuring a higher level of cybersecurity, in compliance with their obligations under Union law.",
      "default_result": "Minimum harmonisation per Art. 21(2) controls list",
      "gold_plating_risk_zone": "high",
      "harmonisation_framing": "minimum"
    }
  ],
  "exclusions": [
    {
      "article": "1",
      "paragraph": "1",
      "exclusion_reason": "descriptive",
      "note": "Subject-matter clause; describes scope without imposing obligation."
    }
  ],
  "glass_box": {
    "extraction_at": "2026-04-28T00:00:00Z",
    "operating_mode": "fresh-extract",
    "persona": "company",
    "skill_version": "1.0.0",
    "language_reconciliation_decisions": [],
    "exclusion_count": 12,
    "row_count": 287,
    "ms_option_count": 34
  }
}
```

**Field-level contract:**

| Field | Type | Notes |
|---|---|---|
| `schema_version` | semver string | Bump major on breaking change to register row shape |
| `directive.celex` | 11-char string | Sector + year + type letter + running number |
| `directive.eli` | URI | Canonical OJ-as-published ELI |
| `directive.transposition_deadline` | ISO 8601 date | Empty for regulations |
| `directive.eea_relevance` | enum | `declared` / `not_declared` / `unknown` |
| `directive.language_coverage` | string | `N/24` where N is languages reconciled |
| `register[*].row_id` | string | `OBL-{celex}-{article}-{paragraph}-{seq}` |
| `register[*].deontic_operator` | enum | `shall` / `must` / `may` / `shall_not` / `should` |
| `register[*].addressee_class` | enum | `member_state` / `national_competent_authority` / `private_actor` / `eu_institution` / `individual` |
| `register[*].ms_option_flag` | boolean | True when paragraph grants MS discretion |
| `register[*].recital_xrefs` | array of integers | Recital numbers cited or substantively linked |
| `register[*].confidence` | enum | `VERIFIED` / `LIKELY` / `POSSIBLE` / `VERIFY` / `ASSUMED` |

---

## Deontic Operator Taxonomy

EU directives use a small set of deontic operators. Disambiguation is critical
because the operator drives the LegalRuleML rule type emitted in Step 11 and the
conformity verdict in `legalcode-eu-conformity-assessment`.

| Operator | English cue | French cue | German cue | LegalRuleML | Notes |
|---|---|---|---|---|---|
| **shall** | "shall", "is/are required to" | "doit", "doivent" | "muss", "müssen", "haben zu" | `<lrml:Obligation>` | The standard mandatory operator. In EU drafting, `shall` is used uniformly; `must` is rare and treated as a synonym of `shall`. |
| **must** | "must" | "doit" | "muss" | `<lrml:Obligation>` | Treated as synonymous with `shall` in EU directives. Modern Commission drafting prefers `shall`. |
| **may** | "may", "is/are entitled to" | "peut", "peuvent" | "kann", "können", "darf" | `<lrml:Permission>` | Permissive. Where addressed to Member States, almost always indicates a national-discretion zone (see **Addressee Taxonomy**). |
| **shall not** | "shall not", "is/are prohibited from" | "ne doit/peut pas" | "darf nicht", "dürfen nicht" | `<lrml:Prohibition>` | Mandatory negative. Distinct from absence of permission; the directive expressly forbids the conduct. |
| **should** | "should" | "devrait" | "sollte" | (no rule emitted) | Recital-level; **not operative**. Where `should` appears in an operative article (very rare; usually a drafting error subject to corrigendum), flag for verification. |
| **shall ensure that** | "shall ensure that …", "shall require …" | "veille à ce que" | "stellt sicher, dass", "sorgt dafür, dass" | `<lrml:Obligation>` with nested `<lrml:Obligation>` | Result-obligation pattern. The Member State has a duty of result; the addressee of the nested obligation is typically a private actor. Common in NIS2, GDPR-derived directives, and consumer-protection directives. |
| **shall be deemed** | "shall be deemed", "is to be regarded as" | "est réputé", "doit être considéré comme" | "gilt als" | `<lrml:Constitutive>` | Constitutive (definitional) rather than prescriptive. Records a legal fact rather than imposing a duty. |

**Disambiguation rules:**

1. **`should` in an operative article**: flag for verification. The directive may be
   defective; a corrigendum may be pending; or the term may be vestigial from a
   working version. Default to treating as `shall` only with explicit user
   confirmation.

2. **`shall ensure that`**: this is a two-level obligation. The Member State (level 1)
   has a duty of result; the level-2 addressee (typically a private actor) has the
   substantive obligation. Emit two register rows: one for the Member State (with
   addressee `member_state` and the result obligation) and one for the substantive
   addressee (with the operational obligation). Both rows carry the same
   transposition deadline.

3. **`may` addressed to Member States**: always sets `ms_option_flag: true` and
   triggers the gold-plating-risk-zone evaluation in Step 6.

4. **`may` addressed to a private actor or individual**: a permission, not a Member
   State option. Emits `<lrml:Permission>` and is captured as a permission row, not
   an MS-option row.

5. **Negative phrasings**: "without prejudice to", "notwithstanding", and "by way
   of derogation from" are not deontic operators but conditional connectors. Capture
   the connection in `internal_xrefs` and emit the operator from the substantive
   verb that follows.

6. **Modal stacking**: phrases like "shall be entitled to" combine `shall` (obligation
   on the Member State to grant the entitlement) with an entitlement (permission for
   the rights-holder). Emit two rows: one obligation on the MS, one permission for
   the rights-holder.

---

## Addressee Taxonomy

Five canonical addressee classes. The taxonomy drives the persona filter in Step 2,
the LegalRuleML `<lrml:Party>` element in Step 11, and downstream conformity
assessment.

| Class | Definition | Example | Citation chain implication |
|---|---|---|---|
| **`member_state`** | The Member State as a legal person; Treaty-level addressee. | "Member States shall bring into force the laws, regulations and administrative provisions necessary to comply with this Directive by 17 October 2024" (NIS2 Art. 41(1)) | Transposition deadline applies; non-notification triggers TFEU Art. 260(3) exposure. |
| **`national_competent_authority`** | A specific authority designated by the Member State; sub-state. | "Member States shall designate one or more competent authorities responsible for cybersecurity and the supervisory tasks referred to in Chapter VII" (NIS2 Art. 8(1)) | Authority is the operative actor; failure to designate is a transposition gap. |
| **`private_actor`** | A natural or legal person within the directive's substantive scope. | "Essential and important entities shall take appropriate and proportionate technical, operational and organisational measures …" (NIS2 Art. 21(1)) | No direct horizontal effect (Marshall, Faccini Dori); enforceable only via NIM. |
| **`eu_institution`** | The Commission, the Council, the Parliament, an EU agency (ENISA, EBA, ESMA, EIOPA, EU-LISA, EUIPO), the EDPS, the CJEU. | "By 17 October 2027, the Commission shall review the functioning of this Directive and report to the European Parliament and to the Council" (NIS2 Art. 40) | EU-internal obligation; not a transposition obligation. |
| **`individual`** | A natural person to whom the directive grants rights. | Data-subject rights in GDPR Art. 15; consumer rights in consumer-protection directives. | Vertical direct effect available against the State (Becker); horizontal effect requires national transposition (Marshall). |

**Disambiguation rules:**

1. **"Competent authority"**: in NIS2, "competent authority" is a Member State
   designation (Art. 8); in some financial-services directives, "competent authority"
   means an EU body (ESMA). Read the directive's definitions article. Default to
   `national_competent_authority` for non-financial-services directives; verify for
   financial-services.

2. **"Operator"**: a directive-specific defined term. Resolve via the definitions
   article. NIS2 distinguishes "essential entities" (Annex I sectors) from "important
   entities" (Annex II sectors); the addressee chain in the register must capture
   the distinction.

3. **"The Union" / "the Member States and the Union"**: dual-addressee pattern (TFEU
   Art. 4(3) flavour). Emit two rows: one with addressee `eu_institution` and one
   with addressee `member_state`.

4. **"Persons" / "any person"**: where a directive uses "person" without qualification,
   it usually means natural and legal persons within the substantive scope. Resolve
   via context. For consumer-protection directives, `individual`. For
   financial-services directives, `private_actor` (with sub-class as defined by
   the directive — credit institution, investment firm, etc.).

5. **"Member States may, in addition, …"**: dual-addressee pattern. The MS-option
   flag fires; the MS is the addressee of the option; if the MS exercises the option,
   the substantive obligation flows to a private actor downstream. Emit one row for
   the MS option and (where the option includes a default substantive rule) one row
   for the substantive addressee.

---

## Recital Treatment

Recitals are the numbered "Whereas" paragraphs at the start of the directive (NIS2
has 142). They are **interpretive**, not operative: they explain why the operative
articles exist, what mischief they aim to remedy, and how they relate to the rest
of EU law.

The CJEU position is settled. *Roquette Frères* (Case C-110/03,
ECLI:EU:C:2005:430) is one of many authorities holding that recitals do not have
binding legal force on their own, but they inform purposive interpretation under
*CILFIT* methodology. The skill follows this position rigorously:

1. **Recitals are not register rows.** A directive with 142 recitals does not produce
   142 obligation rows. Recitals appear only in the `recital_xrefs` array of
   operative obligation rows.

2. **Recitals inform purposive interpretation.** Where a register row's substantive
   meaning is contested (Step 8 language reconciliation), the cross-referenced
   recital is the primary source for purposive interpretation. *CILFIT* directs the
   interpreter to "the purpose and general scheme" — that purpose is most often
   stated in the recitals.

3. **`should` in a recital is not operative.** Recital `should`s ("should ensure",
   "should be supported") are aspirational; they do not generate obligations.
   Recital `should`s often signal where the legislator wanted more but settled for
   less — they are interpretive context, not operative law.

4. **Recital-to-article mapping is bidirectional.** Step 7a builds a matrix tying
   each recital to the operative article(s) it informs. Where a recital is not
   linked to any operative article, flag: it may indicate a drafting issue or a
   recital that supports the directive's scope as a whole.

5. **Recital citation format.** In the register and in the citation chain, format as
   "Recital (N)" — parenthesised number — per the Inter-institutional Style Guide.
   In the JSON, use a plain integer (`recital_xrefs: [49, 77, 78, 79]`).

---

## EEA-Relevance Assessment

The European Economic Area (EEA) extends parts of the EU acquis to Iceland,
Liechtenstein, and Norway via the EEA Agreement. The mechanism is two-step:

1. **EU side**: the directive is published with "(Text with EEA relevance)" in the
   OJ if the Council/Parliament intends it to apply in the EEA.
2. **EEA side**: the EEA Joint Committee adopts a Joint Committee Decision (JCD)
   incorporating the directive into the relevant EEA Annex (Art. 102 EEA). Until
   the JCD is adopted, the directive does not apply in the EFTA pillar. Where an
   EFTA state invokes a constitutional reservation under Art. 103 EEA, EEA
   application is suspended pending parliamentary approval.

This skill performs the **assessment** but not the **tracking**. Tracking JCD
status, Art. 103 reservations, and ESA Art. 31 SCA monitoring is the remit of
`legalcode-eea-incorporation-tracker`.

**Assessment procedure:**

1. **Read the OJ flag.** The "(Text with EEA relevance)" marker appears immediately
   after the directive's title in the OJ publication. Where present, set
   `eea_relevance: declared`.

2. **Subject-matter scoping.** Where the marker is absent, check whether the
   directive's substantive scope falls within an EEA Annex. The most common scopes
   covered in EEA Annexes:
   - Annex II — Technical regulations, standards, testing and certification
   - Annex IV — Energy
   - Annex IX — Financial services
   - Annex XI — Electronic communications, audiovisual services, information society
   - Annex XX — Environment
   - Annex XXI — Statistics
   Where the directive's primary substantive scope falls within an EEA Annex,
   set `eea_relevance: probable_undeclared` and flag for the EEA tracker.

3. **Pure-EU-competence carve-outs.** Some areas of EU law are explicitly outside
   the EEA: Common Agricultural Policy, Common Foreign and Security Policy,
   citizenship, the Schengen acquis (largely; complex interaction with Iceland and
   Norway via separate agreements), criminal law cooperation (largely). Where a
   directive's scope is pure-EU-competence, set `eea_relevance: outside_eea_scope`.

4. **Hand-off to the EEA tracker.** The register's `eea_relevance` field is the
   input to `legalcode-eea-incorporation-tracker`, which performs the JCD adoption
   timeline analysis and flags Art. 103 reservations.

---

## Citation Chain Template

Every register row carries a citation chain that lets a reader walk from the abstract
identifier (CELEX) through the URI (ELI) to the granular textual location (article,
paragraph, point, sentence) in the OJ.

**Required components, in order:**

1. **CELEX**: 11-character string (e.g. `32022L2555`).
2. **Short title + formal title**: "NIS2 Directive (Directive (EU) 2022/2555 of 14
   December 2022 on measures for a high common level of cybersecurity across the
   Union, …)".
3. **OJ reference**: "OJ L 333, 27.12.2022, p. 80" (issue, date, starting page).
4. **ELI URI** (English version): `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng`.
5. **Article + paragraph + point**: "Art. 21(2)(d)" (granular control list reference).
6. **Sentence indicator** (where granularity below the point is needed): "first
   sentence", "second indent".
7. **OJ page** (for the granular reference): "L 333/107".

**Format in prose** (Markdown rendering):

> Essential and important entities shall take appropriate and proportionate
> technical, operational and organisational measures … (NIS2 Directive Art. 21(1),
> CELEX 32022L2555, OJ L 333, 27.12.2022, p. 107; ELI
> `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng`).

**Format in JSON** (machine schema): a `citation_chain` object with `celex`,
`short_title`, `oj_reference`, `eli`, `article`, `paragraph`, `point`,
`sentence_indicator`, and `oj_page` keys (see worked example below).

**Format in AKN4EU**: the `<akn:ref>` element uses the ELI as `href` with a
fragment pointer (e.g. `#art_21__para_1`).

**Format in LegalRuleML**: the `<lrml:LegalSource>` element references the ELI
URI via `<ruleml:Rel iri="...">` with a per-row source key (`src-{celex}-{art}-
{para}`); each `<lrml:Prescriptive>` block includes `<lrml:hasSource keyref="…"/>`.

---

## Worked Example: NIS2 Art. 21 (Cybersecurity Risk-Management Measures)

This example shows the full pipeline for a single operative obligation. It is the
canonical worked example for the skill; downstream sibling skills cross-reference
it.

**Source provision** (NIS2, Directive (EU) 2022/2555, Art. 21(1), OJ L 333/107):

> 1. Member States shall ensure that essential and important entities take appropriate
> and proportionate technical, operational and organisational measures to manage the
> risks posed to the security of network and information systems which those entities
> use for their operations or for the provision of their services, and to prevent or
> minimise the impact of incidents on recipients of their services and on other
> services.

**Extraction logic:**

This is a `shall ensure that` two-level obligation (see **Deontic Operator Taxonomy**).
Two register rows are produced:

- **Row A (Member State result obligation)**: addressee `member_state`; deontic
  `shall`; the result is that essential and important entities take the listed
  measures.
- **Row B (private actor substantive obligation)**: addressee `private_actor`
  (specifically, "essential and important entities" — defined in NIS2 Art. 3 by
  reference to Annexes I and II); deontic `shall` (inherited from the Member-State-
  imposed mandate); the substantive obligation is to take the measures.

Both rows carry transposition deadline 17 October 2024 (NIS2 Art. 41(1)) and
application date 18 October 2024. Recital cross-references include Recitals (49)
(risk-management measures), (77) (proportionality), (78) (all-hazards), (79)
(supply chain).

### Markdown rendering

```markdown
| Row ID | Article | Deontic | Addressee | Obligation | Deadline | MS Option | Recitals |
|---|---|---|---|---|---|---|---|
| OBL-32022L2555-021-001-A | Art. 21(1) | shall | member_state | Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage cybersecurity risk. | 2024-10-17 (transposition) | No | (49), (77), (78), (79) |
| OBL-32022L2555-021-001-B | Art. 21(1) | shall | private_actor (essential and important entities) | Essential and important entities shall take appropriate and proportionate technical, operational and organisational measures to manage cybersecurity risk. | 2024-10-18 (application) | No | (49), (77), (78), (79) |

Cross-references: Annex I (essential-entity sectors); Annex II (important-entity sectors); Art. 21(2)(a)–(j) (granular control list); Art. 3 (definitions).

Citation chain: CELEX 32022L2555; ELI https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng;
OJ L 333, 27.12.2022, p. 107.
```

### JSON rendering

```json
{
  "register": [
    {
      "row_id": "OBL-32022L2555-021-001-A",
      "article": "21", "paragraph": "1", "sentence_no": 1,
      "deontic_operator": "shall",
      "addressee_class": "member_state",
      "addressee_specific": "Member States",
      "obligation_text_eng": "Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures …",
      "transposition_deadline": "2024-10-17",
      "application_date": "2024-10-17",
      "ms_option_flag": false,
      "recital_xrefs": [49, 77, 78, 79],
      "internal_xrefs": ["Art. 3", "Art. 21(2)", "Annex I", "Annex II"],
      "iate_terms": [
        {"term_eng": "essential entities", "term_fra": "entités essentielles", "term_deu": "wesentliche Einrichtungen", "iate_id": "3622139"},
        {"term_eng": "important entities", "term_fra": "entités importantes", "term_deu": "wichtige Einrichtungen", "iate_id": "3622140"}
      ],
      "citation_chain": {
        "celex": "32022L2555",
        "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
        "article": "Art. 21(1)", "oj_page": "L 333/107"
      },
      "confidence": "VERIFIED"
    },
    {
      "row_id": "OBL-32022L2555-021-001-B",
      "article": "21", "paragraph": "1",
      "deontic_operator": "shall",
      "addressee_class": "private_actor",
      "addressee_specific": "essential and important entities (NIS2 Art. 3, Annexes I and II)",
      "obligation_text_eng": "Essential and important entities shall take appropriate and proportionate technical, operational and organisational measures …",
      "transposition_deadline": "2024-10-17",
      "application_date": "2024-10-18",
      "ms_option_flag": false,
      "recital_xrefs": [49, 77, 78, 79],
      "internal_xrefs": ["Art. 3", "Art. 21(2)", "Annex I", "Annex II"],
      "citation_chain": {
        "celex": "32022L2555",
        "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
        "article": "Art. 21(1)", "oj_page": "L 333/107"
      },
      "confidence": "VERIFIED"
    }
  ]
}
```

### AKN4EU XML rendering

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:akn="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <doc name="obligationRegister">
    <meta>
      <identification source="#legalcode-eu-directive-analyzer">
        <FRBRWork>
          <FRBRthis value="https://eur-lex.europa.eu/eli/dir/2022/2555"/>
          <FRBRuri value="https://eur-lex.europa.eu/eli/dir/2022/2555"/>
          <FRBRdate date="2022-12-14" name="adoption"/>
          <FRBRauthor href="#europeanParliament"/>
          <FRBRauthor href="#council"/>
          <FRBRcountry value="EU"/>
          <FRBRsubtype value="directive"/>
          <FRBRnumber value="2555"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng"/>
          <FRBRuri value="https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
      </identification>
    </meta>
    <mainBody>
      <article eId="art_21">
        <num>Article 21</num>
        <heading>Cybersecurity risk-management measures</heading>
        <paragraph eId="art_21__para_1">
          <num>1.</num>
          <content>
            <p>
              <akn:ref href="#row-OBL-32022L2555-021-001-A">
                Member States shall ensure that essential and important entities
                take appropriate and proportionate technical, operational and
                organisational measures to manage the risks posed to the security
                of network and information systems …
              </akn:ref>
            </p>
          </content>
        </paragraph>
      </article>
    </mainBody>
  </doc>
</akomaNtoso>
```

### LegalRuleML rendering

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
                  xmlns:ruleml="http://ruleml.org/spec">
  <lrml:LegalSources>
    <lrml:LegalSource key="src-nis2-21-1">
      <ruleml:Rel iri="https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng#art_21__para_1"/>
    </lrml:LegalSource>
  </lrml:LegalSources>
  <lrml:Prescriptive key="rule-nis2-21-1-A">
    <lrml:hasSource keyref="src-nis2-21-1"/>
    <lrml:Obligation>
      <lrml:Party iri="#party-member-state" type="bearer"/>
      <ruleml:Atom>
        <ruleml:Rel>ensureCybersecurityRiskManagement</ruleml:Rel>
        <ruleml:Var>EssentialOrImportantEntity</ruleml:Var>
      </ruleml:Atom>
    </lrml:Obligation>
  </lrml:Prescriptive>
  <lrml:Prescriptive key="rule-nis2-21-1-B">
    <lrml:hasSource keyref="src-nis2-21-1"/>
    <lrml:Obligation>
      <lrml:Party iri="#party-essential-and-important-entities" type="bearer"/>
      <ruleml:Atom>
        <ruleml:Rel>takeAppropriateAndProportionateMeasures</ruleml:Rel>
        <ruleml:Var>NetworkAndInformationSystems</ruleml:Var>
      </ruleml:Atom>
    </lrml:Obligation>
  </lrml:Prescriptive>
  <lrml:Party key="party-member-state" iri="#member_state"/>
  <lrml:Party key="party-essential-and-important-entities"
              iri="https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng#art_3"/>
</lrml:LegalRuleML>
```

The granular control list at Art. 21(2)(a)–(j) (policies on risk analysis, incident
handling, business continuity, supply chain security, etc.) produces 10 additional
register rows, each with addressee `private_actor` and deontic `shall`, all
inheriting the transposition deadline of 17 October 2024 and cross-referencing
Recitals (77)–(89) (proportionality and the controls catalogue).

---

## Anti-Patterns

What NOT to do when extracting an obligation register from an EU directive:

1. **Treating recitals as operative.** The most common failure mode. Recitals
   explain why operative articles exist; they are not themselves a source of
   obligation (*Roquette Frères* C-110/03). A register that produces 142 rows from
   142 NIS2 recitals is wrong — recitals appear as `recital_xrefs` on operative rows,
   never as standalone rows. What to do instead: enumerate operative articles only;
   use the recital cross-reference matrix (Step 7a) to capture interpretive context.

2. **Conflating regulations and directives.** EU Regulations (TFEU Art. 288(2))
   are directly applicable; they impose no transposition obligation. Running this
   skill against GDPR (Reg. 2016/679) without flagging it as a regulation produces
   spurious `transposition_deadline` and `ms_option_flag` columns. What to do
   instead: in Step 3a, read the CELEX type letter (`L` for directive, `R` for
   regulation, `D` for decision); for regulations, mark transposition columns as
   not applicable and skip Step 6 entirely.

3. **Ignoring the 24-language equal-authenticity rule.** Extracting solely from the
   English version and treating divergence as a translator's error rather than as a
   *CILFIT*-grade reconciliation problem. Where a French or German version uses a
   stronger or weaker deontic operator, the divergence is operatively significant.
   What to do instead: in Step 8, retrieve at least the English, French, German
   versions for cross-check; flag every divergence in `language_divergence`; apply
   purposive interpretation under *CILFIT*.

4. **Inventing CELEX or ECLI identifiers.** Hallucinating identifiers that look
   plausible but do not resolve on EUR-Lex or CURIA. The CELEX format constraints
   are deterministic (sector + year + type + running number); fabricated CELEX values
   will fail the citation gate. What to do instead: never invent. If an identifier
   cannot be retrieved, mark the row `confidence: VERIFY` with a note that the
   citation needs human resolution.

5. **Treating "Member States may" as an obligation.** "Member States may, with
   regard to entities falling within the scope, adopt or maintain provisions ensuring
   a higher level of cybersecurity" (NIS2 Art. 5) is a permission to gold-plate, not
   an obligation. Mistaking it as an obligation triggers spurious conformity verdicts
   downstream. What to do instead: read the deontic operator; `may` triggers
   `<lrml:Permission>` and `ms_option_flag: true` per the **Deontic Operator
   Taxonomy**.

6. **Missing the `shall ensure that` two-level pattern.** "Member States shall ensure
   that essential and important entities take appropriate measures" is a result
   obligation on the Member State *and* an operational obligation on the entity. A
   register that produces only one row loses the addressee distinction. What to do
   instead: emit two rows per the **Deontic Operator Taxonomy** disambiguation rule
   (Row A on the Member State; Row B on the substantive addressee).

7. **Ignoring corrigenda.** EU acts are sometimes corrected after publication via
   formal corrigendum (a separate OJ publication that modifies the original text).
   Extracting from the original OJ text without applying the corrigendum produces
   a register inconsistent with the binding text. What to do instead: in Step 3,
   retrieve the consolidated ELI version (`/oj/{date}/{lang}`) where available;
   note the corrigendum status in directive metadata; in update-existing mode,
   surface every changed row.

8. **Using "should" as if it were "shall".** Recital `should` is aspirational;
   operative `should` is anomalous and almost always indicates a drafting bug or
   recital text mis-classified as operative. Treating either as binding produces
   spurious obligations. What to do instead: in operative articles, treat `should`
   as `confidence: VERIFY` and flag for human review per the **Deontic Operator
   Taxonomy** disambiguation rule.

9. **Privileging the English version because it is convenient.** Modern EU drafting
   is predominantly anglophone, but the French version often carries historical
   precedence and the German version reflects large-economy MS perspective. Taking
   English as authoritative and ignoring divergence with French and German violates
   *CILFIT* and *Codan*. What to do instead: in Step 8, treat all 24 languages as
   equally authentic; document the interpretive process for any divergence.

10. **Misidentifying the transposition deadline.** The transposition article is
    typically the penultimate or third-from-last article (NIS2: Art. 41(1) for
    transposition; Art. 42 for entry into force; Art. 45 for addressees). Where the
    directive is amended by a later directive, the transposition deadline of the
    amending directive may be different — and is the operative date for the amended
    obligations. What to do instead: read the transposition article in full; where
    the directive amends an earlier act, capture both transposition deadlines
    against the relevant rows; flag any phased deadlines.

11. **Failing the source-validation pass.** Producing a register without checking
    that every operative provision generated exactly one row (or carries a
    documented exclusion reason) leaves silent gaps. Downstream skills will inherit
    those gaps and produce false-negative conformity verdicts. What to do instead:
    run Step 10 deterministically; record exclusions explicitly; never accept a
    register without a documented exclusion register.

12. **Ignoring annexes that are referenced from operative articles.** Annexes that
    contain technical lists (NACE codes; control catalogues; sectoral scope
    definitions) inherit operative status when referenced from an operative article.
    A register that captures Art. 21(2) but ignores Annex I (essential-entity
    sectors) loses the substantive scope. What to do instead: in Step 4c, capture
    annex content with the article that incorporates it; treat annex-referenced
    technical detail as operative.

13. **Treating MS-options uniformly.** Member State options are not a single class.
    A pure derogation under tight conditions (e.g. NIS2 Art. 2(7) — entities of
    primary public administration excluded by MS) is low-risk for gold-plating; an
    open "Member States may impose stricter measures" clause is high-risk. What to
    do instead: in Step 6a, populate `ms_option_type` and `gold_plating_risk_zone`
    from the textual cue typology; pass the granular flag to the gold-plating
    detector.

14. **Generating LegalRuleML without parties and sources.** A LegalRuleML stub
    that emits `<lrml:Obligation>` without `<lrml:Party>` (the bearer of the
    obligation) and `<lrml:Source>` (the legal source) does not round-trip; policy-
    as-code engines reject it. What to do instead: every `<lrml:Prescriptive>` block
    must include both `<lrml:Party>` (with `type="bearer"`) and `<lrml:hasSource>`
    referencing the directive's ELI URI.

15. **AKN4EU stub without FRBR identification.** Akoma Ntoso requires the full
    FRBR identification chain (`<FRBRWork>`, `<FRBRExpression>`, `<FRBRManifestation>`).
    Stubs without the FRBR chain do not validate against the AKN4EU subschema; LEOS
    rejects them on import. What to do instead: every AKN4EU emission includes
    minimum `<FRBRWork>` (the abstract directive) and `<FRBRExpression>` (the
    language-specific version); `<FRBRManifestation>` is included where the OJ
    page reference is available.

16. **Treating EEA-relevance as binary EU-side declaration.** The OJ "(Text with
    EEA relevance)" flag is an EU-side intent marker; actual EEA application
    requires a Joint Committee Decision under EEA Art. 102. Treating the OJ flag
    as dispositive of EEA-pillar applicability is wrong. What to do instead: set
    `eea_relevance` to one of `declared` / `not_declared` / `probable_undeclared` /
    `outside_eea_scope` / `unknown`; hand off JCD tracking to
    `legalcode-eea-incorporation-tracker`.

17. **Missing internal cross-references and delegated/implementing acts.**
    Operative articles routinely cross-reference each other ("the requirements
    set out in Article 21(2) shall apply to the entities referred to in Article
    3(1)"); recent directives also delegate detailed rule-making to the
    Commission via TFEU Art. 290 (delegated acts) and Art. 291 (implementing
    acts). A register that omits the internal graph or the delegated/
    implementing tail cannot support downstream conformity assessment or
    forecast the regulatory surface. What to do instead: in Step 7b, build the
    directed internal cross-reference graph and populate `internal_xrefs`; in
    Step 7c, capture every reference to a delegated/implementing act and flag
    `pending_secondary_legislation: true` where the act is not yet adopted.

18. **Ignoring phased application or skipping the Glass Box.** Some directives
    apply in waves (CSRD: large undertakings from FY2024; listed SMEs from
    FY2026; large non-EU groups from FY2028); a register that emits a single
    application date misrepresents the phasing. Likewise, a register without
    an audit trail leaves regulators, boards, and counsel unable to interrogate
    the extraction. What to do instead: in Step 9b, capture per-row application
    dates where the directive distinguishes by addressee class or undertaking
    size and populate `application_phasing`; populate the Glass Box on every
    emission with skill version, operating mode, language-reconciliation
    decisions, exclusion counts, and assumptions.

21. **Treating IATE as authoritative against the directive's defined term, or
    emitting only one output format.** IATE is the Commission's terminology
    database, authoritative for general EU terminology — but the directive's own
    definitions article prevails as *lex specialis*; where they conflict, the
    directive wins. Likewise, downstream skills consume different formats
    (conformity assessment reads JSON; LEOS round-trip needs AKN4EU; policy-
    as-code needs LegalRuleML; counsel needs Markdown); emitting only one
    format breaks downstream pipelines. What to do instead: prefer the
    directive over IATE on conflict, noting the divergence; emit all four
    formats per Step 11; bump `schema_version` (semver) on breaking change.

22. **Treating "without prejudice to" as a deontic operator, or conflating
    entry-into-force with application date.** "Without prejudice to Regulation
    (EU) 2016/679" is a connector that subordinates the current rule to another
    act; it is not itself deontic. A directive's entry into force (typically 20
    days after OJ publication) is distinct from its application date
    (transposition deadline + 1 for MS obligations; the substantive application
    date for phased rules). What to do instead: capture connectors in
    `external_xrefs` and emit the deontic operator from the substantive verb
    that follows; populate `entry_into_force_date`, `transposition_deadline`,
    and `application_date` as three distinct fields per Step 9.

---

## Writing Standards

1. **Deontic operator usage.** Use `must` for skill-internal mandatory rules;
   `shall` only when quoting directive text; `may` for permissive guidance.
   Never use `should` in operative skill prose.
2. **CELEX / ELI / ECLI format.** In prose, short title + parenthetical CELEX
   on first use: "NIS2 Directive (CELEX 32022L2555)". In citation chains
   (footnote, JSON), include the ELI URI. ECLI format: "Case C-X/YY,
   ECLI:EU:C:YYYY:N" — always include the full identifier.
3. **Article reference format.** "Art. N(M)(p)" — abbreviate Article as Art.,
   parenthesise paragraph and point. Ranges: "Art. 21(2)(a)–(j)" with em-dash.
4. **Citation density.** Every legal claim cited. "Directives bind Member
   States as to result" needs TFEU Art. 288(3). No EU-law assertion without a
   citation.
5. **Language reconciliation.** Capture all verified versions in `iate_terms`
   and `language_divergence`; never present English-only as if 24 versions were
   reviewed. State coverage as `N/24`.
6. **EEA-relevance flag.** Populate `eea_relevance` with one of the enum
   values; never leave empty. `unknown` with a Glass Box note where uncertain.
7. **`[VERIFY]` markers inline.** Place immediately after the unconfirmed
   claim, not in a footnote.
8. **Active voice, imperative for skill prose.** "Resolve the CELEX to an ELI
   URI" not "the CELEX should be resolved". Passive voice only for directive
   quotation.
9. **Confidence transparency.** Every row has `confidence`. Do not present
   `ASSUMED` rows as fact in Markdown; flag `[CONFIDENCE: ASSUMED]`.
10. **One obligation per row.** Art. 21(2) (a)–(j) produces ten rows, not one.
    `shall ensure that` produces two rows (one for the MS, one for the
    substantive addressee).
11. **Recital citation format.** "Recital (N)" parenthesised in prose; integer
    in JSON. Multiple: "Recitals (49), (77), (78), (79)".
12. **Glass Box inline.** Reference the Glass Box for every row at
    `confidence: VERIFY` or below.
13. **No false precision in deadlines.** "By 17 October 2024" → `2024-10-17`.
    "Within three years of entry into force" → compute and flag `[VERIFY
    computed deadline]`.
14. **AKN4EU validation.** Every emitted XML must validate against the AKN4EU
    subschema. Where validation cannot be performed in-session, mark
    `<!-- VALIDATION: pending -->` and flag in Glass Box.
15. **LegalRuleML completeness.** Every `<lrml:Prescriptive>` has `<lrml:Party
    type="bearer">` and `<lrml:hasSource>` referencing the ELI URI.
16. **Schema version bump policy.** Major for breaking changes; minor for
    additive; patch for docs. Sibling skills declare the schema version they
    consume.
17. **No invented enforcement actions.** Cite only real cases (*Becker*,
    *Marshall*, *Faccini Dori*, *Von Colson*, *Marleasing*, *CILFIT*). Never
    invent ECLI identifiers.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Per project CLAUDE.md: delegate to the `legalcode-search-agent` subagent rather
than calling `mcp__legalcode__*` directly. Use in Step 3 and Step 8 to:

1. Resolve CELEX → ELI mappings against the EUR-Lex Cellar SPARQL endpoint
   (`https://publications.europa.eu/webapi/rdf/sparql`).
2. Retrieve the directive in multiple language versions for cross-check.
3. Verify amendments, corrigenda, and consolidated versions (NIS2 amends Reg.
   910/2014 and Dir. 2018/1972, for example).
4. Pull IATE entries for defined terms.
5. Confirm the OJ "(Text with EEA relevance)" flag against the published PDF.
6. Cross-check ECLI references for cited case law (*Becker*, *Marshall*,
   *Faccini Dori*, *Von Colson*, *Marleasing*, *CILFIT*, *Codan*, *EMU Tabac*,
   *Roquette Frères*) against CURIA / InfoCuria.

Save research to `/tmp/legalcode-eu-directive-research.md`; note in Glass Box:
`legalcode_mcp: "Connected — research file at [path]"`.

### Without legalcode-mcp

Use the shared reference pack at `references/eu-legislative-data/` (IATE quick-
reference, ELI templates, AKN4EU subschema notes, MS NIM publication channels).
Mark unverified citations with `[VERIFY]` and note `legalcode_mcp: "Not
connected — references require independent verification"`.

Confidence adjustments: CELEX/ELI `LIKELY` → `POSSIBLE`; language reconciliation
`LIKELY` → `POSSIBLE` if fewer than three languages reconciled; case-law ECLI
`LIKELY` → `VERIFY` if not retrieved from CURIA.

### Related Skills Integration

| Trigger | Invoke this skill |
|---|---|
| Per-MS implementation matrix needed | `legalcode-eu-transposition-tracker` |
| Commission-format correlation table needed | `legalcode-eu-correlation-table-builder` |
| Per-article transposition verdict needed | `legalcode-eu-conformity-assessment` |
| National over-implementation analysis | `legalcode-eu-gold-plating-detector` |
| EEA Joint Committee Decision tracking | `legalcode-eea-incorporation-tracker` |
| Infringement procedure timeline | `legalcode-eu-infringement-procedure-tracker` |
| General EU/UK/multi-MS comparison | `legalcode-multi-jurisdiction-privacy-comparison` (where privacy-domain) or relevant domain skill |
| Policy-gap-style adequacy assessment of national policies | `legalcode-policy-gap-analysis` |

---

## Output Format Template

Each emission carries four output formats. Persona filtering (Step 2) applies at
this step.

### 1. Markdown (Human Review)

A Markdown emission contains, in order:

- **Directive header**: short title, formal title, CELEX, ELI, OJ reference,
  transposition deadline, entry into force, EEA-relevance enum, language
  coverage `N/24`, schema version, operating mode, persona.
- **Register table**: columns Row ID, Article, Deontic, Addressee, Obligation
  (truncated to 120 chars), Deadline, MS Option, Recitals.
- **MS options table**: columns Option ID, Article, Type, Discretion Scope,
  Default Result, Gold-Plating Risk.
- **Cross-references**: recital ↔ article matrix; internal cross-reference
  graph; external references (other EU acts cited).
- **Compliance deadlines table**: transposition, entry into force, application
  (with phasing notes), review, sunset.
- **Exclusion register**: every clause not captured as a row, with reason.
- **Citation**: full short title + formal title + CELEX + OJ reference + ELI.

### 2. JSON (Canonical Machine Schema)

Full schema in **Obligation Register Schema**. Optional fields
(`language_divergence`, `external_xrefs`) default to empty arrays.

### 3. AKN4EU XML (LEOS Round-Trip)

`<akomaNtoso>` root with `<doc name="obligationRegister">`. The FRBR chain
(`<FRBRWork>`, `<FRBRExpression>`) is mandatory; `<FRBRManifestation>` is
included where an OJ page is known. Each row appears as an `<article>`
containing `<paragraph>` elements with `<akn:ref>` cross-references. Pattern
shown in **Worked Example** above.

### 4. LegalRuleML (Policy-as-Code Round-Trip)

`<lrml:LegalRuleML>` root with `<lrml:LegalSources>` (one `<lrml:LegalSource>`
per directive, ELI URI as `iri` on `<ruleml:Rel>`); `<lrml:Prescriptive>` blocks
(one per row; `<lrml:Obligation>` / `<lrml:Permission>` / `<lrml:Prohibition>`
matching the deontic operator; `<lrml:Party type="bearer">`; `<lrml:hasSource
keyref="…"/>`); and `<lrml:Constitutive>` blocks for definitions. Pattern in
**Worked Example** above.

### 5. Glass Box Audit Trail

Every emission produces a Glass Box block (YAML for review; JSON for processing).

```yaml
glass_box:
  skill_name: "legalcode-eu-directive-analyzer"
  skill_version: "1.0.0"
  schema_version: "1.0.0"
  extraction_at: "[ISO 8601]"
  operating_mode: "[fresh-extract / update-existing / EEA-scope / contested-language-version]"
  persona: "[government / legal-firm / company / trade-federation]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-eu-directive-research.md or Not created]"
  directive:
    celex: "[celex]"
    eli: "[uri]"
    formal_title: "[title]"
    oj_reference: "[OJ L NNN, DD.MM.YYYY, p. NN]"
  extraction_metrics:
    operative_articles: [N]
    register_rows: [N]
    ms_options: [N]
    exclusions: [N]
    recital_count: [N]
    language_coverage: "[N]/24"
  language_reconciliation_decisions:
    - row_id: "OBL-…"
      languages_compared: ["eng", "fra", "deu"]
      divergence_detected: false
      cilfit_purposive_check: "n/a"
      confidence: "VERIFIED"
  exclusion_register:
    - article: "Art. N(M)"
      reason: "[descriptive / definitional / structural / cross_reference_only]"
      note: "[short note]"
  ms_option_inventory:
    harmonisation_framing: "[minimum / maximum / mixed]"
    derogation_count: [N]
    discretion_count: [N]
    gold_plating_risk_zones: { low: [N], medium: [N], high: [N] }
  source_validation:
    every_operative_provision_one_row: true
    every_ms_obligation_has_transposition_deadline: true
    every_row_has_citation_chain: true
    self_interrogation_what_did_i_miss: "[short note]"
  assumptions: ["[Assumption 1]", "[Assumption 2]"]
  limitations: ["[Scope limitation]", "[Not assessed — e.g. delegated acts]"]
  reviewer_note: "AI-assisted extraction — every register row at confidence
    VERIFY or below requires validation by qualified EU/Member State counsel
    before regulatory or board use. Citation chains have not been independently
    verified against EUR-Lex unless legalcode_mcp is Connected."
```

---

## Localization Notes

When adapting this skill for specific national or sectoral contexts:

1. **Regulations vs. directives.** This skill is built for directives. Where the
   user supplies a regulation (AI Act, GDPR, DORA, DSA, DMA), it emits a
   register but flags transposition-deadline, MS-option, and gold-plating
   columns as not applicable. Do not run the transposition tracker, correlation-
   table builder, or gold-plating detector for regulations.

2. **Multi-pillar acts.** Acts straddling multiple legal bases (NIS2 amends
   Reg. 910/2014 and Dir. 2018/1972) capture parent-directive obligations only;
   amendments to other acts go in `external_xrefs` and require separate
   extraction passes.

3. **EFTA / EEA pillar.** For EEA-relevant directives, the `eea_relevance` flag
   is the input to `legalcode-eea-incorporation-tracker`. The EU-27 transposition
   deadline runs from OJ publication; the EFTA pillar's deadline begins on JCD
   adoption (Art. 102 EEA), modulated by any Art. 103 reservations.

4. **Member State language vs. EEA language regime.** The 24 official EU
   languages do not include Icelandic, Norwegian, or Liechtenstein-Standard
   German. The EEA Agreement adds Icelandic and Norwegian. For ESA Art. 31
   monitoring, use the EEA-published version, not the EU-only version.

5. **Pre-Lisbon directives.** Directives before 1 December 2009 may cite the EC
   Treaty rather than TFEU. Capture as `legal_basis` but cross-reference the
   equivalent TFEU article.

6. **Drafting-language heritage.** Modern drafting is predominantly anglophone;
   historically French. For directives drafted in French, the French version
   often clarifies ambiguity in English. Note in directive metadata.

7. **Sectoral overlay.** For sector-specific directives, the relevant ESA
   (ESMA, EBA, EIOPA, BEREC, ACER) issues Level 2/3 measures. Capture
   references in `external_xrefs`; Level 2/3 extraction is the remit of a
   sector-specific skill.

---

## Provenance

Created by Legalcode (2026-04-28). Foundation skill of the seven-skill EU
Legislative Compliance suite, drafted per the suite design brief at
`skills/general/compliance/_eu-suite-design-brief.md`.

**Primary EU/EEA law cited in this skill:**
- TFEU Art. 288 (instrument hierarchy) —
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`
- TEU Art. 4(3) (sincere cooperation — basis of transposition obligation)
- TFEU Art. 258, 260(2), 260(3) (infringement procedure and penalties)
- TFEU Art. 290, 291 (delegated and implementing acts)
- EEA Arts. 7, 102, 103; Art. 31 SCA
- Council Regulation No 1 of 1958 —
  `https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`

**Case law cited:**
- *CILFIT*, C-283/81, ECLI:EU:C:1982:335
- *Codan*, C-236/97, ECLI:EU:C:1998:208
- *EMU Tabac*, C-296/95, ECLI:EU:C:1998:152
- *Becker*, C-8/81, ECLI:EU:C:1982:7
- *Marshall*, C-152/84, ECLI:EU:C:1986:84
- *Faccini Dori*, C-91/92, ECLI:EU:C:1994:292
- *Von Colson*, C-14/83, ECLI:EU:C:1984:153
- *Marleasing*, C-106/89, ECLI:EU:C:1990:395
- *Roquette Frères*, C-110/03, ECLI:EU:C:2005:430
- *Commission v Belgium*, C-543/17, ECLI:EU:C:2019:573

**Methodology:**
- Better Regulation Toolbox 2023, Chapter 4 —
  `https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`
- Inter-institutional Style Guide (Publications Office)

**Standards:**
- Akoma Ntoso (OASIS LegalDocML 1.0, 2018), AKN4EU subschema
- ELI (European Legislation Identifier) —
  `https://eur-lex.europa.eu/eli-register/technical_information.html`
- ECLI; CELEX; LegalRuleML 1.0 (OASIS, 2021) —
  `https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`

**Worked-example sources:**
- NIS2 (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022, p. 80)
- AI Act (Regulation (EU) 2024/1689, CELEX 32024R1689) — contrast
- CSRD (Directive (EU) 2022/2464, CELEX 32022L2464)
- CSDDD (Directive (EU) 2024/1760, CELEX 32024L1760)
- GDPR (Regulation (EU) 2016/679, CELEX 32016R0679) — contrast
- DORA (Regulation (EU) 2022/2554, CELEX 32022R2554) — contrast

**Data sources (via legalcode-mcp / legalcode-search-agent where Connected):**
EUR-Lex Cellar SPARQL (`https://publications.europa.eu/webapi/rdf/sparql`),
EUR-Lex web service, IATE (`https://iate.europa.eu/`), CURIA, N-Lex, OEIL,
EEA-Lex, Single Market Scoreboard.

**Shared reference pack:**
`skills/general/compliance/legalcode-eu-directive-analyzer/references/eu-legislative-data/`
— co-located; cross-referenced by sibling skills.

**Citations flagged for verification before regulatory or board use:**
- The IATE entry IDs in the worked-example JSON (`3622139`, `3622140`) are
  illustrative placeholders; verify against IATE before consumption.
- The OJ page reference `L 333/107` for NIS2 Art. 21 — cross-check against the
  OJ PDF.
- All CELEX values cited in Step 3a's table — verify on EUR-Lex retrieval.
- Transposition deadlines (NIS2: 17 October 2024, Art. 41(1); CSDDD: 26 July
  2026, Art. 37) — verifiable on EUR-Lex; verify before use.

**Reviewer note:** AI-assisted drafting — every register row at confidence
`VERIFY` or below requires validation by qualified EU and Member State counsel
before regulatory submission, infringement procedure participation, or board
reporting. The JSON schema is load-bearing across the suite; bump
`schema_version` and announce to all sibling skills on any breaking change.
