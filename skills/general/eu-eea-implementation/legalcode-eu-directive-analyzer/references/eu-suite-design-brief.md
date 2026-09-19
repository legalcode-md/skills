# EU Legislative Compliance Suite — Design Brief

**STATUS:** Drafting brief for an 8-agent parallel build. Once all skills are landed
this file may be deleted or moved into the reference pack as historical context.

This brief is the single source of truth for how every skill in the seven-skill EU
Legislative Compliance suite must be written. Every drafting agent must read it in
full and honour every constraint.

---

## 1. The seven skills in the suite

| Letter | Skill name (folder)                           | Job                                                                                                                           |
| ------ | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| B      | `legalcode-eu-directive-analyzer`             | Extracts a versioned **obligation register** from any EU directive. Foundation skill — every other skill consumes its output. |
| C      | `legalcode-eu-transposition-tracker`          | Maintains the per-Member-State **implementation matrix** for a given directive.                                               |
| D      | `legalcode-eu-correlation-table-builder`      | Builds the **Commission-format two-column correlation table** (directive Article ↔ National Implementing Measure).            |
| E      | `legalcode-eu-conformity-assessment`          | Runs the formal **per-article conformity check** — verdict per provision: correct / partial / incorrect / not transposed.     |
| F      | `legalcode-eu-gold-plating-detector`          | Flags where the NIM exceeds the EU minimum, by published category.                                                            |
| G      | `legalcode-eea-incorporation-tracker`         | Tracks the **EEA Joint Committee Decision** process for incorporating EU acts (IS/NO/LI).                                     |
| H      | `legalcode-eu-infringement-procedure-tracker` | Tracks **TFEU 258/260 procedures** and ESA Art. 31 SCA cases per MS-directive pair.                                           |

Skill A (legislative monitor) is deferred — handled outside this skill suite via MCP /
email service per the user's direction.

## 2. File paths

Each skill writes to:
`skills/general/compliance/<skill-name>/SKILL.md`

The **shared reference pack** (one copy only, no duplication) lives co-located with the
foundation skill at:
`skills/general/compliance/legalcode-eu-directive-analyzer/references/eu-legislative-data/`

Sibling skills cross-reference the pack via:
`See [shared EU legislative-data pack](eu-legislative-data/)`

## 3. Frontmatter (exact format — copy verbatim)

```yaml
---
name: <skill-name>
description: >
  <Comprehensive multi-line description, 150–300 words. Must cite specific named
  EU instruments by short title + CELEX (e.g. "NIS2 Directive (Directive (EU) 2022/2555,
  CELEX 32022L2555)", "AI Act (Regulation (EU) 2024/1689, CELEX 32024R1689)",
  "GDPR (Regulation (EU) 2016/679, CELEX 32016R0679)", "DORA (Regulation (EU) 2022/2554)",
  "CSRD (Directive (EU) 2022/2464)", "CSDDD (Directive (EU) 2024/1760)"). Must reference
  the relevant TFEU article(s) (288, 258, 260) where applicable. Must list operating
  modes and personas served. End with EU/EEA jurisdictional scope statement.>
allowed-tools: Read, Write, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---
```

## 4. Section order (use these exact headings, in this order)

```
# <Skill Title>

> **Disclaimer**: <two paragraphs — see template below>

## Purpose and Scope
## Jurisdiction and Governing Law
## Interactive Clarification
## Workflow
## <Domain-specific reference sections — varies per skill, see per-skill spec>
## Anti-Patterns
## Writing Standards
## External Tool Integration
## Output Format Template
## Localization Notes
## Provenance
```

The "Purpose and Scope" section must include a **Sibling Skills in the Suite**
subsection naming the other six skills and the artefact contract for handoff.

## 5. Disclaimer template (use verbatim, swap `<topic>` for skill-specific phrase)

```
> **Disclaimer**: This skill provides a framework for AI-assisted <topic>. It does not
> constitute legal advice and does not create an attorney-client relationship. All outputs
> should be reviewed by qualified legal counsel licensed in the relevant jurisdictions
> before use. This skill does not replace formal legal review by qualified EU and Member
> State counsel. It produces a structured framework to support a human-led review — not a
> substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and Member State
> implementing measures must be verified against authoritative sources (EUR-Lex, CURIA,
> national official journals) before use in regulatory submissions, infringement
> proceedings, or board reporting. EU law evolves continuously; transposition status,
> infringement procedures, and consolidated text versions change frequently. The 24
> official EU language versions of every act are equally authentic; reconcile divergent
> versions before relying on any single language for a definitive interpretation
> (CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95).
```

## 6. Interactive Clarification preamble (verbatim — DO NOT modify)

```
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

## 7. Persona branching (every skill, in Step 2 — verbatim)

```

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

```

The rest of the workflow must branch on this answer where output format diverges.

## 8. Citation requirements (NON-NEGOTIABLE)

- Every EU act cited: short title + formal title + CELEX + OJ reference.
  Example: "NIS2 Directive (Directive (EU) 2022/2555 of 14 December 2022 on measures for a
  high common level of cybersecurity across the Union, CELEX 32022L2555, OJ L 333,
  27.12.2022, p. 80)."
- TFEU articles: "Art. 288 TFEU" with at least one citation to consolidated EUR-Lex ELI
  on first use: `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`.
- Case law: ECLI required. Example: "*Commission v Belgium*, Case C-543/17, ECLI:EU:C:2019:573".
- All citations must be **real and verifiable**. No invented case numbers, no placeholder
  citations, no `[XX]` references that look real but aren't.
- Where you would be tempted to invent: omit instead, or cite to a published source that
  is verifiable (Better Regulation Toolbox 2023 Ch. 4, Single Market Scoreboard).

## 9. Standards-based outputs — first-class (this is our differentiator)

Where the skill emits structured legal content (obligation register, transposition matrix,
correlation table, conformity verdicts, gold-plating findings, infringement timeline), the
**Output Format Template** must include all four:

1. **Markdown** — human review format with full citations.
2. **JSON** — machine-readable schema, fully specified with field types.
3. **Akoma Ntoso (AKN4EU)** — XML stub conformant to the LegalDocML AKN4EU subschema used
   by LEOS and EU institutions. Reference: `https://op.europa.eu/o/opportal-service/euvoc-download-handler?cellarURI=http%3A%2F%2Fpublications.europa.eu%2Fresource%2Fdistribution%2Fcdm%2F20210701-0%2Fzip%2Fcdm_20210701-0.rdf.zip&fileName=cdm.zip`
   Use root element `<akomaNtoso>` with appropriate `<doc>` / `<judgment>` / `<act>`
   children depending on the artefact type.
4. **LegalRuleML** — XML stub representing obligations as deontic rules (Obligation,
   Permission, Prohibition) with `<lrml:Constitutive>` / `<lrml:Prescriptive>` blocks,
   `<lrml:Party>` for addressees, `<lrml:Source>` referencing the directive ELI.
   Reference: `https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`

The point of the standards layer is round-trippability — round-trip to LEOS, round-trip
to policy-as-code engines, round-trip to the Italian Senate / UK National Archives
parliamentary tooling. **Write real, validating XML stubs**, not placeholders.

## 10. Cross-references between sibling skills (mandatory subsection)

In "Purpose and Scope", include a `### Sibling Skills in the Suite` subsection like this:

```

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes /
produces the following artefacts:

- **Consumes**: <e.g. "obligation register from `legalcode-eu-directive-analyzer`">
- **Produces**: <e.g. "per-MS implementation matrix consumed by `legalcode-eu-correlation-table-builder` and `legalcode-eu-conformity-assessment`">

Sibling skills (use whichever is appropriate for the user's stage in the lifecycle):

- `legalcode-eu-directive-analyzer` — extracts the obligation register from a directive
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix
- `legalcode-eu-correlation-table-builder` — directive-to-NIM correlation table
- `legalcode-eu-conformity-assessment` — per-article transposition verdict
- `legalcode-eu-gold-plating-detector` — flags national over-implementation
- `legalcode-eea-incorporation-tracker` — EEA Joint Committee Decision tracking
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 procedure timeline

```

## 11. Length target

- Substantive skills (B–H): 1,200–1,500 lines. Match the rigour of
  `legalcode-policy-gap-analysis` (1,408 lines) and `legalcode-dpa-review-and-negotiation`
  (1,491 lines).
- Reference pack (under directive-analyzer): one `INDEX.md` (~150 lines) plus 4-5
  topic files (~150-300 lines each) = ~800-1,200 lines total across files.

## 12. Quality bar

- Read `skills/general/compliance/legalcode-policy-gap-analysis/SKILL.md` before drafting.
  Match its section rigour, citation density, anti-pattern depth, and writing standards.
- **No placeholders**. Every section must contain substantive content. If a section header
  doesn't apply to your skill, omit it; never leave a "TODO" or "TBD".
- All workflow steps must have concrete, executable instructions.
- All CLARIFY blocks must have real options that materially branch the analysis (not
  cosmetic choices).
- Anti-Patterns section must list **at least 8 specific anti-patterns** with explanations
  of why each is wrong and what to do instead.
- Writing Standards section must specify: deontic operator usage (must / shall / may),
  citation density (every legal claim cited), language-version reconciliation rules,
  how to handle EEA-relevance flags, how to format CELEX/ELI/ECLI in prose vs. footnotes.

## 13. Authoritative grounding (use these — they are real and verified)

### TFEU primary text
- Art. 288 TFEU — instrument hierarchy (regulations / directives / decisions).
  ELI: `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`
- Art. 258 TFEU — infringement procedure (LFN → reasoned opinion → CJEU referral).
- Art. 260(2) TFEU — penalty payment after non-compliance with Art. 258 judgment.
- Art. 260(3) TFEU — first-referral penalty for failure to notify transposition of a
  legislative directive (Lisbon innovation, first applied in *Commission v Belgium*
  C-543/17, ECLI:EU:C:2019:573).

### EEA primary text
- Art. 7 EEA — incorporation of EU acts into EEA Annexes.
- Art. 102 EEA — Joint Committee Decision procedure.
- Art. 103 EEA — constitutional reservations / parliamentary approval suspension.
- Art. 31 SCA (Surveillance and Court Agreement) — ESA monitoring mandate.

### Multilingualism
- Regulation 1/1958 — official language regime.
  ELI: `https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`
- CILFIT (Case C-283/81, ECLI:EU:C:1982:335) — equal authenticity of language versions.
- Codan (Case C-236/97, ECLI:EU:C:1998:208).
- EMU Tabac (Case C-296/95, ECLI:EU:C:1998:152).

### Methodology
- Better Regulation Toolbox 2023, Chapter 4 (Compliance, Implementation and Preparing Proposals):
  `https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`
- ECN+ Directive (EU) 2019/1 conformity assessment tender — published Commission template,
  Belgian PP ref [765714].
- HLG report on gold-plating (Commission, 2014):
  `https://ec.europa.eu/futurium/en/system/files/ged/hlg_16_0008_00_conclusions_and_recomendations_on_goldplating_final.pdf`
- UK BIS Gold-Plating Review (2013).
- CFA Society Poland — Gold-plating in EU Capital Markets (2024) — concrete examples
  across MiFID II / Prospectus / AIFMD.

### Sources / data feeds
- EUR-Lex Cellar SPARQL endpoint: `https://publications.europa.eu/webapi/rdf/sparql`
- EUR-Lex web service: `https://eur-lex.europa.eu/content/help/data-reuse/webservice.html`
- N-Lex (national execution measures): `https://eur-lex.europa.eu/collection/n-law/mne.html`
- OEIL Legislative Observatory: `https://oeil.europarl.europa.eu/oeil/`
- CURIA / InfoCuria: `https://curia.europa.eu/`
- EEA-Lex: `https://www.efta.int/eealaw`
- IATE (terminology, 24 languages): `https://iate.europa.eu/`
- Single Market Scoreboard (transposition + infringement): `https://single-market-scoreboard.ec.europa.eu/`
- ESA Internal Market Scoreboard: `https://www.efta.int/`
- National parliament APIs:
  - Riksdagen (SE): `https://data.riksdagen.se`
  - Storting (NO): `https://data.stortinget.no`
  - Folketinget (DK): `https://oda.ft.dk`
  - Althingi (IS): `https://www.althingi.is`
  - Bundestag (DE): `https://dip.bundestag.de`
  - Assemblée nationale (FR): `https://data.assemblee-nationale.fr`

### Standards
- Akoma Ntoso (OASIS LegalDocML 1.0, 2018) — Akn schema family with AKN4EU subschema for EU
  institutions. Used by LEOS, UK National Archives, Italian Senate, Senegalese parliament.
- ELI (European Legislation Identifier) — HTTP URI scheme for legislation:
  `https://eur-lex.europa.eu/eli-register/technical_information.html`
- ECLI (European Case Law Identifier) — analogous for case law.
- CELEX — Publications-Office identifier (e.g. `32016R0679` for GDPR).
- LegalRuleML (OASIS, 2021) — rule modelling for legal logic.

### Concrete worked examples (use throughout for illustrative purposes)
- **NIS2 Directive** (CELEX 32022L2555) — well-developed transposition record across MS.
- **AI Act** (CELEX 32024R1689) — recent, high salience, EEA relevance pending JCD.
- **CSRD** (CELEX 32022L2464) — extensively transposed with documented gold-plating.
- **CSDDD** (CELEX 32024L1760) — fresh, transposition deadline 26 July 2026.
- **DSA / DMA** (CELEX 32022R2065 / 32022R1925) — regulations (no transposition) for
  contrast.

## 14. What NOT to do

- Do not invent case numbers, CELEX, or ECLI.
- Do not write generic compliance prose. Every paragraph must be specific to EU process.
- Do not duplicate the reference pack content into each skill — cross-reference instead.
- Do not omit the persona-branching CLARIFY in Step 2.
- Do not omit AKN4EU + LegalRuleML stubs in the Output Format Template.
- Do not write a Step 1 that pre-judges the user's persona or operating mode.
- Do not use placeholder language like "[insert obligation here]" — supply real
  examples drawn from NIS2 / AI Act / CSRD / GDPR.
- Do not leave the "Provenance" section empty. List every primary source actually cited.
- Do not omit the **Glass Box audit trail** subsection (in Output Format Template) —
  every skill in the suite must produce a deterministic audit trail of decisions.
```
