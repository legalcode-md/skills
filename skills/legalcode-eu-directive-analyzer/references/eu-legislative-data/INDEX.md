# EU Legislative Data Reference Pack — Index

This reference pack is the shared knowledge base for the seven-skill EU Legislative
Compliance suite (`legalcode-eu-directive-analyzer`, `legalcode-eu-transposition-tracker`,
`legalcode-eu-correlation-table-builder`, `legalcode-eu-conformity-assessment`,
`legalcode-eu-gold-plating-detector`, `legalcode-eea-incorporation-tracker`,
`legalcode-eu-infringement-procedure-tracker`). It is co-located with the foundation
skill at `skills/general/compliance/legalcode-eu-directive-analyzer/references/
eu-legislative-data/`. Sibling skills cross-reference the pack rather than duplicating
its contents — the pack is the single source of truth for canonical identifiers, source
data feeds, multilingualism doctrine, standards-based output formats, and worked
examples used to ground every workflow in the suite.

The pack is designed to be loaded selectively. A skill performing a transposition
gap analysis on the NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555) will
typically pull `identifier-playbook.md` (to validate CELEX/ELI/ECLI usage),
`source-playbook.md` (to query the Cellar SPARQL endpoint and N-Lex for the German
NIM citations), `worked-examples.md` (to ground its analysis in the published NIS2
transposition record), and `formats-playbook.md` (to emit a validating Akoma Ntoso
obligation register). A skill drafting a conformity verdict for a Maltese transposition
will additionally pull `multilingualism-playbook.md` to reconcile the Maltese
authentic version against the English working text under the equal-authenticity
doctrine anchored in *CILFIT* (Case C-283/81, ECLI:EU:C:1982:335).

## When to load each file

| If the skill is doing… | Load primarily | Load supporting |
|---|---|---|
| Extracting obligations from a directive | `identifier-playbook.md`, `formats-playbook.md` | `source-playbook.md`, `multilingualism-playbook.md` |
| Tracking national transposition status | `source-playbook.md`, `worked-examples.md` | `identifier-playbook.md` |
| Building a Commission-format correlation table | `formats-playbook.md`, `identifier-playbook.md` | `worked-examples.md` |
| Per-article conformity verdict | `multilingualism-playbook.md`, `identifier-playbook.md` | `worked-examples.md`, `formats-playbook.md` |
| Gold-plating detection | `worked-examples.md`, `source-playbook.md` | `identifier-playbook.md` |
| EEA Joint Committee Decision tracking | `source-playbook.md` (EEA-Lex section) | `identifier-playbook.md`, `multilingualism-playbook.md` |
| TFEU 258/260 infringement timeline | `source-playbook.md` (CURIA, OEIL) | `identifier-playbook.md`, `worked-examples.md` |

## Files in this pack

### `identifier-playbook.md` (~250 lines)
Canonical identifier reference. Defines the structure, validation rules, and
construction algorithm for **CELEX** (the Publications Office identifier — sector +
year + type + number, e.g. `32016R0679` for GDPR, `32022L2555` for NIS2), the
**European Legislation Identifier (ELI)** (HTTP URI scheme registered by the EU
Publications Office for legislation, with all 24 official-language `/oj/<lang>`
patterns), the **European Case Law Identifier (ECLI)** (jurisdiction codes including
EU for CJEU and EFTA for the EFTA Court, with worked examples drawn from
*Commission v Belgium* (Case C-543/17, ECLI:EU:C:2019:573) and *CILFIT* (Case
C-283/81, ECLI:EU:C:1982:335)), the **Official Journal reference format** (e.g. "OJ L
333, 27.12.2022, p. 80" for NIS2), national identifier formats for the seven
priority Member States plus EEA EFTA states (BGBl, JORF, Stortingsforhandlinger,
Stjórnartíðindi, Svensk författningssamling, Lovtidende, Dziennik Ustaw), and the
FRBR Work/Expression/Manifestation/Item levels in the Cellar Common Data Model.
Load this file first whenever a workflow step constructs, parses, or validates a
legal identifier — never invent a CELEX or ECLI.

### `source-playbook.md` (~300 lines)
Operational guide to the data sources the suite queries. Contains working SPARQL
queries against the **Cellar endpoint** at `https://publications.europa.eu/webapi/
rdf/sparql` (consolidated versions of a directive, language version listing,
National Implementing Measures notified for a directive, CJEU cases citing an act),
the **EUR-Lex web service** REST shape, **N-Lex/MNE database** queries for national
execution measures notified by Member States, **OEIL Legislative Observatory**
dossier structure (e.g. 2022/0066(COD) for NIS2 procedural file), **CURIA/InfoCuria**
structured search by ECLI/CELEX/procedure type, **EEA-Lex** for Joint Committee
Decisions and IS/NO/LI national status, **IATE** bulk export for 24-language
terminology alignment, **national parliament APIs** for SE/NO/DK/IS/DE/FR plus
operational notes for PL/NL/ES/IT/FI/EE/LV, and the **Single Market Scoreboard** +
ESA Internal Market Scoreboard. Closes with a coverage matrix showing which sources
are reachable through Legalcode MCP `search_laws`/`search_cases`/`search_guidance`
versus those requiring direct API access. Load this file whenever a workflow step
needs to fetch data — never quote a transposition fact without first sourcing it.

### `multilingualism-playbook.md` (~200 lines)
Authoritative guide to the equal-authenticity regime governing all 24 EU official
languages. Anchored in **Regulation 1/1958** (the original language regulation;
ELI `https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`), the **24 currently
authentic languages** (Croatian since accession in 2013; Irish since the derogation
under Regulation 920/2005 was lifted on 1 January 2022 by Regulation 2015/2264),
and the EEA addition of **Icelandic and Norwegian** (authentic for EEA EFTA states
under Art. 129(1) EEA, but never authentic in EU-internal litigation). Walks through
the operative reasoning of *CILFIT* (Case C-283/81), *Codan* (Case C-236/97),
*EMU Tabac* (Case C-296/95), and *Endendijk* (Case C-187/07), then sets out a
four-step reconciliation methodology with a worked NIS2 example. Closes with the
operational rule for the analyzer skill: extract obligations from the user's working
language, set an `eea-relevance` and `language-divergence-flag` whenever the user's
Member State is bound by a different authentic version. Load this file whenever a
conformity verdict turns on a definitional or scope term — never assume the English
text is canonical.

### `formats-playbook.md` (~250 lines)
The standards-based output guide. This is the suite's differentiator: every artefact
the suite emits (obligation register, NIM matrix, correlation table, conformity
verdict, gold-plating finding, infringement timeline) must round-trip into LEOS
(the EU Commission's Akoma Ntoso drafting tool), the Italian Senate workflow, the
UK National Archives platform, and policy-as-code engines that consume LegalRuleML.
Specifies **Akoma Ntoso (OASIS LegalDocML 1.0, 2018)** with its AKN4EU subschema
profile (root `<akomaNtoso>`, namespace `http://docs.oasis-open.org/legaldocml/ns/
akn/3.0`, document classes `<act>`, `<bill>`, `<judgment>`, `<doc>`), and
**LegalRuleML (OASIS, 2021)** with its deontic operators (`<lrml:Obligation>`,
`<lrml:Permission>`, `<lrml:Prohibition>`), `<lrml:Party>` for the addressee, and
`<lrml:Source>` referencing the directive ELI. Provides complete, validating XML
stubs for each artefact and a JSON Schema for each suite-internal artefact (these
schemas are the contracts between sibling skills). Load this file before emitting
any structured output — placeholders or non-validating XML are an anti-pattern the
brief explicitly forbids.

### `worked-examples.md` (~300 lines)
Concrete reference instruments used throughout the suite for illustration. Provides
short title, formal title, CELEX, ELI URI, OJ reference, transposition deadline (if
a directive), notable language-version issues, and the published transposition or
interpretation issues for: **NIS2 Directive** (CELEX 32022L2555 — five worked
obligations, transposition status across DE/FR/SE/PL/IS, gold-plating examples
flagged in the Linklaters tracker, ECLI cases interpreting the NIS1 precursor),
**AI Act** (CELEX 32024R1689 — regulation example with national-implementing-measure
obligations such as designated competent authorities and penalty regimes; EEA
relevance assessment status), **CSRD** (CELEX 32022L2464 — transposition deadline
6 July 2024, gold-plating examples in DE/FR/IT documented by Linklaters and Ropes &
Gray), **CSDDD** (CELEX 32024L1760 — transposition deadline 26 July 2026, live
exercise), **GDPR** (CELEX 32016R0679 — regulation contrast; Member State opening
clauses required NIMs), **DSA** (CELEX 32022R2065) and **DMA** (CELEX 32022R1925)
as further regulation contrasts. Load this file whenever a skill needs a concrete
exemplar — never illustrate a workflow with hypothetical "Directive 2024/XXXX".

## Dependencies between files

```
identifier-playbook.md  ←─ foundational; every other file references it
        ↑
        │
source-playbook.md  ──→  multilingualism-playbook.md
        │                          ↑
        ↓                          │
worked-examples.md  ──────────────→ formats-playbook.md
```

`identifier-playbook.md` has no upstream dependencies and must be loaded first
when a skill validates or constructs identifiers. `source-playbook.md` references
identifiers (CELEX in SPARQL queries, ECLI in CURIA queries) and feeds raw data to
`worked-examples.md` and `multilingualism-playbook.md`. `multilingualism-playbook.md`
defines the reconciliation methodology used when `formats-playbook.md` examples
include multi-language `<FRBRlanguage>` elements. `formats-playbook.md` provides
the JSON Schemas that govern the artefacts shown in `worked-examples.md`. The
worked examples are the concrete stress-test against which the rest of the pack
must remain consistent — if a CELEX in `worked-examples.md` does not validate
under `identifier-playbook.md`, the pack itself is wrong.

## What this pack is not

- It is not a substitute for the Better Regulation Toolbox 2023, Chapter 4
  (Compliance, Implementation and Preparing Proposals) — see
  `https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`
  for the Commission's official methodology.
- It is not a substitute for primary sources. Every CELEX, ELI, ECLI, and OJ
  reference cited here must be verified against EUR-Lex (`https://eur-lex.europa.eu`)
  or CURIA (`https://curia.europa.eu`) before use in regulatory submissions,
  infringement proceedings, or board reporting.
- It is not a static document. Transposition status, infringement procedures,
  consolidated text versions, and EEA Joint Committee Decisions change frequently;
  the worked examples capture the position as of late 2025/early 2026 and require
  re-verification before any analytical reliance.
