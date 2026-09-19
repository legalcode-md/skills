---
name: legalcode-anti-gold-plating-is
description: 'Comprehensive section-by-section, word-by-word detection of gold-plating (gullhúðun) in
  Icelandic implementing legislation — identify where the local act imposes a more restrictive, more onerous,
  or more complicated regime than the original EU/EEA directive required, then trace each divergence back
  to its source in the legislative pre-law materials (frumvarp, greinargerð, athugasemdir við einstakar
  greinar, mat á áhrifum, samanburðartafla, samráðsgátt drög, umsagnir, nefndarálit, breytingartillögur,
  framsöguræða, 1./2./3. umræða, þingskjöl) via the current Legalcode MCP unified tool surface: legalcode_trace,
  legalcode_search, legalcode_fetch, legalcode_discover, and legalcode_analyze.'
metadata:
  jurisdiction: Iceland
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Comprehensive section-by-section, word-by-word detection of gold-plating (gullhúðun) in Icelandic implementing legislation — identify where the local act imposes a more restrictive, more onerous, or more complicated regime than the original EU/EEA directive required, then trace each divergence back to its source in the legislative pre-law materials (frumvarp, greinargerð, athugasemdir við einstakar greinar, mat á áhrifum, samanburðartafla, samráðsgátt drög, umsagnir, nefndarálit, breytingartillögur, framsöguræða, 1./2./3. umræða, þingskjöl) via the current Legalcode MCP unified tool surface: legalcode_trace, legalcode_search, legalcode_fetch, legalcode_discover, and legalcode_analyze. Applies the Davidson Five taxonomy (extending scope; declining derogations; stricter sanctions/burden of proof/procedure; early implementation; retaining stricter pre-existing rules) plus the Regelrådet sixth limb (heimasmíðuð additions / breach of hrein innleiðingarfrumvörp), against the EEA framework (Art. 7 EEA, Protocol 35, lög nr. 2/1993, EEA Joint Committee Decisions, EFTA Court homogeneity, CJEU C-52/00 max-harm presumption) and the Icelandic statutory disclosure framework (§8(b) Reglur forsætisnefndar um þinglega meðferð EES-mála; §37(1) lög nr. 55/1991 um þingsköp Alþingis; §13(3) Samþykkt ríkisstjórnarinnar um undirbúning og frágang stjórnarfrumvarpa). Diagnoses divergence through a 35-item linguistic and structural checklist (modal verbs skal/má/heimilt; quantifiers ávallt/eftir því sem við á; temporal triggers án tafar; personal-scope tighteners hver sá sem/sérhver; sanction escalation refsing vs stjórnvaldssektir; connector add-ons auk þess/enn fremur; flexibility-clause deletions). Compares the Icelandic enacted text against the authentic Icelandic translation in EES-viðbætir við Stjórnartíðindi ESB (never against EUR-Lex English), then walks every flagged divergence back through the pre-law record to identify (a) who introduced it (ministry, committee majority/minority, floor amendment), (b) where it first appeared (samráðsgátt drög vs introduced frumvarp vs committee amendment vs reglugerð), (c) what stakeholders (SA, SI, SFF, SVÞ, FA, Viðskiptaráð, ASÍ) said about it in umsagnir, and (d) whether the greinargerð disclosed and justified the divergence. Produces a per-article Gullhúðunarskýrsla with severity classification (🔴 CRITICAL unlawful max-harm divergence / 🟠 HIGH undisclosed min-harm divergence / 🟡 MEDIUM disclosed-unjustified / 🟢 LOW disclosed-justified), 5-level confidence scoring, Iron Law 7 counter-argument stress test for HIGH/CRITICAL findings, tiered remediation recommendations, complete pre-law citation chain, and Icelandic OSCOLA-adapted citations.
Use when reviewing an Icelandic implementing act for transposition over-reach, preparing a samráðsgátt umsögn flagging gold-plating, briefing utanríkismálanefnd or a sectoral standing committee on EEA-conformity issues, advising a regulated client on whether a stricter Icelandic rule traces back to the directive or to a domestic add-on, drafting a breytingartillaga to trim gold-plating from a pending frumvarp, preparing an ESA complaint, supporting a þingsályktunartillaga response to a JCD adaptation, or auditing a ministerial portfolio for systemic over-implementation following the 2024 Foreign Ministry task force on aðgerðir gegn gullhúðun. Iceland-specific (EEA EFTA context). Triggers on "check this Icelandic act for gold-plating," "find gullhúðun in lög nr. X/Y," "compare this Icelandic transposition to the directive," "trace this provision to the frumvarp," "did Iceland go further than the directive required," "review this bill for umframinnleiðing," "which stakeholders flagged gold-plating in this mál," or "build a Gullhúðunarskýrsla for lög nr. X/Y."


# Legalcode Anti-Gold-Plating Analysis — Iceland (gullhúðun við innleiðingu EES-gerða)

## Purpose and Scope

Comprehensive per-article audit of an Icelandic implementing act against the EU/EEA
instrument it transposes, with each flagged divergence traced back to a specific source in
the legislative pre-law record. Deliverable: a **Gullhúðunarskýrsla** usable for
umsagnargerð, breytingartillögugerð, ESA complaint preparation, or committee briefing.

**Applies to every Icelandic act that transposes an EEA-incorporated EU instrument**, whether the underlying EU instrument is a directive (full transposition discretion under Art. 7(b) EEA) or a regulation with Member-State-discretion areas (e.g. GDPR Arts. 6(2)/(3), 8, 9, 23, 84, 88, 89; Solvency II MS options; CSRD MS options; PSD2 national derogations). Worked examples throughout this file frequently use **lög nr. 90/2018 ↔ reglugerð (ESB) 2016/679 (GDPR)** because that pairing is the most-cited and best-documented gold-plating example in Icelandic practice, but **the skill is not scoped to data protection**. Substitute the matter's own act number, CELEX, supervisory authority, and sectoral context whenever you apply the skill. Where an example names a specific provision (e.g. _„fjárhagslegt tjón"_ in 51. gr. lög 90/2018), read it as: _"the analogous narrowing wording in the act you are auditing"_.

Indicative scope of acts this skill applies to in IS practice — every act on this non-exhaustive list has surfaced gold-plating findings in the post-2018 academic literature or the 2024 Foreign Ministry task-force report:

- Data protection — lög nr. 90/2018 (GDPR, reglugerð (ESB) 2016/679); lög nr. 75/2019 (LED, tilskipun (ESB) 2016/680)
- Financial services — lög nr. 115/2021 (MiFID II); lög nr. 140/2018 (AMLD); lög nr. 161/2002 (CRD); Solvency II implementation; lög nr. 50/2017 (CRA)
- Non-financial reporting — lög nr. 3/2006 (NFRD/CSRD)
- Cybersecurity — lög nr. 78/2019 (NIS/NIS2)
- Whistleblower protection — lög nr. 40/2020 (WBD, tilskipun (ESB) 2019/1937)
- Environmental — most environment-ministry portfolio acts (the Einarsdóttir 2024 study found gold-plating in 11/27 sampled bills)
- Consumer protection, product safety, employment law, telecommunications, energy, food safety — any sectoral act bearing a transposition footnote to an EEA-incorporated EU instrument is in scope.

The Davidson Five + Pattern G30 framework, the 35-item linguistic diagnostic, the EES-viðbætir comparison discipline, the §8(b) / §37(1) / §13(3) disclosure framework, and the pre-law tracing protocol are **all jurisdiction-Iceland-general** — not data-protection-specific. The Stage 6.2 impact buckets apply equally to a Persónuvernd-applied act and a Fjármálaeftirlitið-applied act.

**Covers**: Davidson Five + Regelrådet sixth limb; 35-item linguistic/structural diagnostic;
section-by-section comparison against EES-viðbætir authentic Icelandic translation; full
pre-law tracing (samráðsgátt → frumvarp → þingskjöl → umsagnir → nefndarálit → umræður);
identification of the introducing actor; stakeholder-objection mapping; reglugerð sweep;
ESA / EFTA Court / ECJ cross-verification; Iron Law 7 counter-argument stress test;
4-tier severity with 5-level confidence; Icelandic OSCOLA citations.

**Does not**:

- Draft new transposition legislation from scratch.
- Provide formal legal advice or guarantee enforcement outcomes.
- Cover purely domestic Icelandic acts (no directive baseline — gold-plating inapplicable).
- Cover EU regulations where there is no Member-State discretion (degrades to thin conformity check). For regulations with MS-discretion areas (e.g. GDPR Arts. 6(2)/(3), 8, 9, 23, 84, 88, 89), analyse only the discretion areas.
- Audit constitutional legality of stricter pre-existing IS rules.
- Resolve whether an EU act has been incorporated into the EEA Agreement.

---

## Icelandic Guidelines — Companion Reference

The deliverable-language rules live in `references/icelandic-guidelines.md`. Apply that file before drafting, during Stage 9e, and during Stage 10e. The report and any remediation bill must be written in professional Icelandic legal prose, with internal tooling references stripped from user-facing deliverables.

---

---

## Jurisdiction and Governing Law

**Framework citations** (full doctrinal treatment in `references/gold-plating-doctrine.md`):

- **EEA primary**: Art. 6 EEA (homogeneity), Art. 7 EEA (choice of form), Protocol 35
- **Icelandic transposition anchor**: lög nr. 2/1993, 3. gr. (EEA-conform interpretation)
- **Constitutional**: stjórnarskrá 65., 71., 72., 75. gr. (jafnræði, friðhelgi einkalífs, eignarréttur, atvinnufrelsi)
- **Parliamentary procedure**: lög nr. 55/1991, 37. gr. (hrein innleiðingarfrumvörp); Reglur forsætisnefndar um þinglega meðferð EES-mála, 8. gr. (b) (gold-plating disclosure); Samþykkt ríkisstjórnarinnar um undirbúning og frágang stjórnarfrumvarpa, 13. gr. mgr. 3 (bundling justification)
- **Executive guidance**: Handbók um undirbúning og frágang lagafrumvarpa (2007); Handbók um EES-skuldbindingar; utanríkisráðuneytið task-force report (31 May 2024)

**Institutional actors**:

| Body                        | Icelandic                | Role                       |
| --------------------------- | ------------------------ | -------------------------- |
| Foreign Affairs Committee   | utanríkismálanefnd       | EEA-conformity scrutiny    |
| Sectoral standing committee | varies                   | Substantive review         |
| Foreign Ministry            | utanríkisráðuneytið      | EEA coordination, JCD      |
| Prime Minister's Office     | forsætisráðuneytið       | Handbók custodian          |
| EFTA Surveillance Authority | ESA                      | Infringement enforcement   |
| EFTA Court                  | EFTA-dómstóllinn         | EFTA-pillar interpretation |
| EEA Joint Committee         | sameiginlega EES-nefndin | Adopts JCDs                |

---

## Doctrinal Framework — Operational Names

Full treatment in `references/gold-plating-doctrine.md`. Operational summary:

**Davidson Five** (Iceland-adapted):

1. **Davidson-1** — extending scope (lower thresholds, wider definitions, omitted carve-outs)
2. **Davidson-2** — declining derogations
3. **Davidson-3** — stricter sanctions / enforcement / procedure / burden of proof
4. **Davidson-4** — implementing earlier than the directive required
5. **Davidson-5** — retaining stricter pre-existing national rules
6. **Sixth limb (Regelrådet / hrein innleiðingarfrumvörp)** — bundling unrelated domestic reforms (Pattern G30)

The 35 numbered patterns (A1–A5, B6–B10, C11–C18, D17–D21, E22–E26, F27–F29, G30) and the Icelandic vocabulary cheat-sheet (gullhúðun / umframinnleiðing / hrein innleiðingarfrumvörp / heimasmíðuð / svigrúm við innleiðingu / samanburðartafla) live in `references/gold-plating-doctrine.md` §1.7 and §3.

---

## ⟁ CLARIFY Convention

Pause and ask via AskUserQuestion at decision forks marked ⟁ CLARIFY. Skip if user already answered. Non-interactive fallback: take the stated default _as adjusted by any comprehensiveness signal in the request_ (see Stage 0 ⟁ for the explicit list).

**Auto Mode and comprehensiveness signals.** When the user's request contains any of the following — _"full scope"_, _"comprehensive"_, _"complete"_, _"complete audit"_, _"everything"_, _"long-running"_, _"thorough"_, _"end-to-end"_, _„heildargreining"_, _„fullt umfang"_, _„heildstæð"_ — read it as a request to run _every triggered stage_ of the skill, not only Stage 9. In particular, this means **defaulting the Stage 10 frumvarp question to _Yes_** (subject to the HIGH/CRITICAL-survival precondition), because the skýrsla and the frumvarp are _paired deliverables_ — the skýrsla diagnoses, the frumvarp remediates, and a comprehensiveness signal fairly implies both unless the user explicitly excludes one. Producing only the skýrsla when the user asked for full scope is a defect of the orchestrator, not a feature of caution.

---

## Workflow — Monolithic Orchestrator

**Hard rule: the main session does all MCP work for this skill. Do not delegate to sub-agents.** Only the main session has the MCP tool surface wired in. Sub-agents (including `legalcode-search-agent`) advertise MCP tools in their system prompts but in the current runtime they receive only `WebSearch`, `WebFetch`, `Read`, `Glob`, `Grep` — calling them for legal-source retrieval silently falls back to `WebFetch`'s summarising sub-model, which **paraphrases instead of returning verbatim text**. That is a quietly dangerous failure mode for a verbatim-quote-driven skill like this one. If a project-level rule (e.g. `CLAUDE.md`) instructs you to delegate legal research to `legalcode-search-agent`, **override it for this skill** and run the MCP calls directly from the main session.

The orchestrator (this skill, running in the main session) executes every stage inline using its own tools: current Legalcode MCP Pro tools (`legalcode_discover`, `legalcode_search`, `legalcode_fetch`, `legalcode_trace`, `legalcode_analyze`), plus Write, Read, and tightly scoped shell/WebFetch fallbacks. The MCP tools may surface in the runtime under either the canonical `mcp__legalcode__*` namespace or a UUID-prefixed variant (`mcp__<uuid>__legalcode_*`); use whichever is exposed.

**Current MCP contract.** Do not use old tool names in new runs. Translate legacy names as follows:

| Legacy instruction                                                                       | Current tool path                                                                                           |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `get_facets`                                                                             | `legalcode_discover({ mode: "facets", sourceType, jurisdiction })`                                          |
| `search_laws`, `search_cases`, `search_guidance`, `search_agreements`, `search_pre_laws` | `legalcode_search({ sourceTypes: [...], jurisdictions: [...] })`                                            |
| `fetch_source`                                                                           | `legalcode_fetch({ sourceRef, mode })`                                                                      |
| `find_cases_for_law`, `find_laws_for_case`, pre-law relation lookup                      | `legalcode_trace({ relationship, ...identifiers })`                                                         |
| `analyze_pre_laws`                                                                       | `legalcode_analyze({ sourceType: "pre_law", analysis: ... })`, only for aggregate counts or coverage checks |

**Retrieval discipline.**

- Use `legalcode_trace` for deterministic relationships before ranked search: pre-law for a known law, cases for a law, laws cited by a case.
- Use `legalcode_search` with `mode: "exact"` for identifiers, law keys, regulation numbers, CELEX-like references, source IDs, and sourceRefs.
- Use keyword/BM25 search only when the source is not known by identifier.
- Use `legalcode_analyze` only for aggregate questions such as "which submitters exist?" or "how many document roles are present"; never use it to retrieve source text.
- Use WebFetch/WebSearch only for the explicit residual gaps listed in "External Tool Integration" after MCP trace/search/fetch has been tried and logged.

Working directory: `./gullhudun-{matter_id}/` with this layout:

```
gullhudun-{matter_id}/
├── sources/                # populated in Stage 1
│   ├── INDEX.md            # manifest of every downloaded file
│   ├── act/                # in-force IS act + metadata
│   ├── directive/          # EU directive EN + authentic IS translation
│   ├── pre-law/            # frumvarp, athugasemdir, nefndarálit, breytingartillögur, umræður, samanburðartafla
│   ├── umsagnir/           # one file per umsögn
│   ├── jcd/                # EEA Joint Committee Decision
│   ├── ecj/                # ECJ rulings (one per case)
│   ├── efta-court/         # EFTA Court rulings
│   ├── esa/                # ESA decisions / infringements
│   ├── is-case-law/        # IS cases interpreting the act
│   ├── is-guidance/        # FME / Persónuvernd / Stjórnarráðið guidance
│   ├── reglugerðir/        # secondary legislation under the act
│   ├── nordic/             # Norway/Sweden/Denmark/Finland comparators (if scope flag set)
│   └── is-constitutional/  # stjórnarskrá precedent (if relevant)
├── articles/               # per-article diagnostic blocks (Stage 3)
├── forensics/              # per-finding pre-law forensic blocks (Stages 4+5)
├── stress/                 # per-finding stress-test blocks (Stages 6+8)
├── revisions/              # one entry per 9d / 10c edit-on-fail iteration: {ISO-timestamp}-{iter}.md
├── validation-report.md    # Stage 8.5 gap list (must be empty before Stage 9)
├── Gullhudunarskyrsla-{act}-{date}.md    # source report (Stage 9)
├── Gullhudunarskyrsla-{act}-{date}.docx  # final Word deliverable (Stage 9f)
├── frumvarp-mapping.md     # Stage 10a — findings → amendments worklist (only if Stage 10 runs)
├── Frumvarp-{act}-{date}.md              # remediation bill (Stage 10) — only if Stage 10 runs
└── Frumvarp-{act}-{date}.docx            # final Word deliverable for the bill (Stage 10f)
```

### Stage 0 — Intake & Scoping

Parse the user request. Extract: act reference (lög nr. X/ÁÁÁÁ or pending þskj./mnr./ltg.), optional directive reference, user purpose, article scope.

Run five ⟁ CLARIFY prompts in a single AskUserQuestion batch:

- **Purpose**: Umsögn | Breytingartillaga | ESA complaint | Internal compliance | Academic | Other
- **Article scope**: All articles | Specific articles (list) | Specific topic | Triage first then deep-dive
- **Comparator Nordic**: Yes full | Norway only | No
- **Frumvarp draft**: Yes — produce a remediation breytingafrumvarp as Stage 10 | No — skýrsla only.

  **Default-selection rules, applied in this order:**
  1. If the user's stated purpose is _Breytingartillaga_, default to **Yes**.
  2. If the user's request contains any comprehensiveness signal (_"full scope"_, _"comprehensive"_, _"complete audit"_, _"everything"_, _"long-running"_, _"thorough"_, _"end-to-end"_, _„heildargreining"_, _„fullt umfang"_, _„heildstæð"_, or any equivalent), default to **Yes** — the skýrsla and the frumvarp are paired deliverables and a comprehensiveness signal fairly implies both unless the user explicitly excludes one.
  3. If the user's request explicitly names only _one_ deliverable (e.g. _"just write the report"_, _"only the skýrsla"_), default to **No**.
  4. Otherwise (purpose = Umsögn / ESA complaint / Internal compliance / Academic / Other, no comprehensiveness signal, no explicit single-deliverable instruction), default to **No** (skýrsla only).

  Stage 10 only runs when there is at least one HIGH/CRITICAL finding surviving Stage 8 — but for any Icelandic implementing act of an EEA-incorporated EU instrument (post-2018), surviving HIGH/CRITICAL findings are the _norm_, not the exception (the 2024 Foreign Ministry task-force report and the Einarsdóttir 2024 study both found gold-plating in roughly half of post-2018 implementations). The skill should therefore assume that the precondition will be met whenever Yes is the default.

- **Output destination**: Project root (default) | Matter path | Specific path | Chat only

If the user did not name the underlying directive(s), discover from the greinargerð in Stage 1 before proceeding to Stage 2.

### Stage 1 — Corpus Download

Load the current Legalcode MCP tools. Issue calls in efficient batches, but keep deterministic dependencies sequential: law identifier → `legalcode_trace pre_law_for_law` → flow document inventory → per-document `downloadUrl` → `curl` to local disk.

#### Retrieval principle — download URLs first, `legalcode_fetch` only when needed

Every search/trace result returned by the current MCP carries a signed `downloadUrl` plus a `nextAction` hint. For any document you intend to read end-to-end and persist into `sources/`, use the `downloadUrl` directly:

```bash
# generic pattern — copy the downloadUrl verbatim from search/trace output
curl -sL "<downloadUrl from result>" -o "sources/<subdir>/<filename>.md"
```

**The downloadUrl always returns Markdown.** The MCP normalises every document — PDFs, DOCX, HTML, scanned text — into UTF-8 Markdown at serve time. Save with `.md` regardless of any `format` field on the metadata. The `format` field describes the **upstream original** on althingi.is / EUR-Lex / EFTA, not what `curl` receives. Treating it as the output extension produces files named `*.pdf` that are actually Markdown text — a real confusion that has happened.

If a `curl` returns a tiny (~100-byte) JSON body instead of Markdown, the signed URL token has expired or was reused — re-run the originating `legalcode_search` / `legalcode_trace` for a fresh `downloadUrl` and retry. Do not retry the stale URL.

This is the canonical retrieval path. Enumerate via `legalcode_search` (`resultLevel: "document"` for pre-law) or `legalcode_trace`, take the `downloadUrl` field from each result, and `curl` it to disk.

`legalcode_fetch` is reserved for two narrow inspection uses:

- **`mode: "metadata"`** — listing the documents attached to a pre-law flow before you know their sourceRefs (the flow inventory), or sanity-checking one record before relying on it.
- **`mode: "excerpt"` with `q` or `sectionRef`** — targeted reads of a single article/section when you don't want the whole file.

Every document that goes into `sources/` comes via `downloadUrl + curl`.

**Standard download recipe per document:**

```bash
mkdir -p sources/<subdir>
curl -sL "<downloadUrl>" -o "sources/<subdir>/<filename>.md"
ls -la "sources/<subdir>/<filename>.md"                # confirm non-zero size
file   "sources/<subdir>/<filename>.md"                # confirms "UTF-8 Unicode text" (Markdown)
```

After every download, append a one-line entry to `sources/INDEX.md` recording `path | sourceRef | fetch_date | VERIFIED-MCP | byte_size`.

**Flow → documents recipe (the high-frequency case):**

```json
// step 1: trace the pre-law flow from the enacted law
{ "tool": "legalcode_trace",
  "args": { "relationship": "pre_law_for_law", "lawKey": "IS|LAW|90/2018" } }

// step 2: enumerate every attached document as a structured result with its own downloadUrl
{ "tool": "legalcode_search",
  "args": {
    "sourceTypes": ["pre_law"],
    "jurisdictions": ["IS"],
    "filters": [{ "field": "flowKey", "op": "eq", "value": "<flowKey from step 1>" }],
    "resultLevel": "document",
    "page": { "limit": 20 }
  } }

// step 3: for each result, curl its downloadUrl into sources/
//         no fetch_source needed.
```

Page through with `nextCursor` until `hasMore: false`. The MCP returns each attached document with its sourceRef, role, sender, publishedAt, format, and a signed `downloadUrl`. That's enough to curl every file.

**Identifier-first recipes.**

Use these exact shapes before free-text search. Substitute `{NN/YYYY}` with the matter's IS-act number-year, and `{CELEX}` with the underlying EU instrument's CELEX. The worked examples below use the lög 90/2018 ↔ GDPR pair for illustration only.

Current Icelandic implementing act by number/year:

```json
{
  "sourceTypes": ["law"],
  "jurisdictions": ["IS"],
  "mode": "exact",
  "filters": [{ "field": "lawKey", "op": "eq", "value": "{NN/YYYY}" }],
  "page": { "limit": 5 }
}
// worked example: value: "90/2018"
```

Pre-law flow for a known enacted law:

```json
{
  "relationship": "pre_law_for_law",
  "lawKey": "IS|LAW|{NN/YYYY}"
}
// worked example: "IS|LAW|90/2018"
```

Underlying EU instrument by CELEX (regulation, directive, or decision):

```json
{
  "sourceTypes": ["law"],
  "jurisdictions": ["EU"],
  "mode": "exact",
  "filters": [
    { "field": "lawKey", "op": "eq", "value": "{CELEX or number/year}" },
    {
      "field": "actType",
      "op": "eq",
      "value": "{REGULATION | DIRECTIVE | DECISION}"
    }
  ],
  "page": { "limit": 5 }
}
// worked example (GDPR): value: "2016/679", actType: "REGULATION", CELEX 32016R0679
// worked example (LED):  value: "2016/680", actType: "DIRECTIVE",  CELEX 32016L0680
// worked example (MiFID II): value: "2014/65", actType: "DIRECTIVE", CELEX 32014L0065
```

If the exact lookup of the underlying EU instrument does not return the instrument itself, do **not** rely on implementing decisions or other records that merely mention it. For Icelandic gold-plating comparison, the authentic Icelandic translation lives in the `Fylgiskjal` of the implementing Icelandic act for most directly-incorporated regulations (this is how 32016R0679 is preserved in lög nr. 90/2018, for example). For directives, the authentic Icelandic translation is published in the EES-viðbætir; retrieve it from there or via residual `curl` from EFTA — and log the EU-English source only as a supplemental comparator.

**Retrieval checklist** (each item → one or more MCP calls + Write to disk):

### Pre-law (mandatory — fetch all, not just a sample)

Pre-law material is the single most important corpus for this skill. Fetch comprehensively, not selectively:

All rows assume you have already enumerated the flow's documents with `legalcode_search resultLevel:"document"` (see "Flow → documents recipe" above) and have a list of `{sourceRef, role, downloadUrl, sender, documentNumber, format}` per attached document.

| Pre-law document                                     | Path                                                              | How to retrieve                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pre-law flow inventory                               | (in memory; optional `sources/pre-law/flow-metadata.md`)          | `legalcode_trace pre_law_for_law` with `lawKey` or `relatedNumberYear: "{NN}/{YYYY}"` → record `flowKey`. Then enumerate documents with `legalcode_search resultLevel:"document" filters:[{flowKey eq <flowKey>}]`, paging through `nextCursor`. Only use `legalcode_fetch mode:"metadata"` on the flow if you need a human-readable inventory dump.  |
| **Frumvarp + greinargerð** (introduced bill)         | `sources/pre-law/frumvarp.md`                                     | Pick the result with `role: ORIGINAL_BILL`. `curl -sL "<downloadUrl>" -o sources/pre-law/frumvarp.md`.                                                                                                                                                                                                                                                |
| **Per-article athugasemdir**                         | `sources/pre-law/athugasemdir/{N}-gr.md`                          | Split the downloaded frumvarp's "Athugasemdir við einstakar greinar" section into one file per article. Local processing only.                                                                                                                                                                                                                        |
| **Samanburðartafla** (if any)                        | `sources/pre-law/samanburdartafla.md`                             | After downloading the frumvarp, `grep -n "samanburðartafla\|Samanburðartafla" sources/pre-law/frumvarp.md`. If no hit, also run `legalcode_search resultLevel:"document" filters:[{flowKey eq <flowKey>}, {documentText text scope:"all" value:"samanburðartafla"}]`. If still none, write `[ENGIN SAMANBURÐARTAFLA Í FRUMVARPI]`.                    |
| **All umsagnir**                                     | `sources/umsagnir/{submitter-slug}-thskj-{NNNN}.md`               | From the enumerated documents, every result with `role: SUBMITTED_OPINION`. For each: `curl -sL "<downloadUrl>" -o "sources/umsagnir/<sender-slug>-thskj-<documentNumber>.md"`. Always `.md` — the MCP normalises to Markdown regardless of upstream `format`. Page through `nextCursor` until exhausted — do not stop at the first 20-document page. |
| **Targeted gullhúðun sweep**                         | `sources/umsagnir/_gold-plating-sweep.md`                         | `legalcode_search resultLevel:"document" filters:[{flowKey eq <flowKey>}, {documentText text scope:"submittedOpinion" value:"gullhúðun OR \"umfram lágmark\" OR \"gengur lengra\" OR íþyngjandi"}]`. Save the snippet/sender pairs locally. This is an index over the umsagnir you already downloaded, not a substitute for downloading all of them.  |
| **Nefndarálit meiri hluta** (and minni hluta if any) | `sources/pre-law/nefndarálit-{meiri,minni}-hluta-thskj-{NNNN}.md` | Results with `role: COMMITTEE_REPORT`. `curl -sL` each `downloadUrl`.                                                                                                                                                                                                                                                                                 |
| **Breytingartillögur**                               | `sources/pre-law/breytingartillögur/thskj-{NNNN}.md`              | Results with `role: AMENDMENT_PROPOSAL`. `curl -sL` each `downloadUrl`.                                                                                                                                                                                                                                                                               |
| **Final enacted text** (lög samhljóða)               | `sources/pre-law/lög-samhljóða-thskj-{NNNN}.md`                   | Results with `role: ENACTED_TEXT` or `BILL_AFTER_SECOND_READING`. `curl -sL` each `downloadUrl`. Useful for verbatim article text when the consolidated act is large or carries later amendments.                                                                                                                                                     |
| **Alþingi summary** (samantekt)                      | `sources/pre-law/alþingi-summary.md`                              | Result with `role: SUMMARY` if present; otherwise extract from the flow metadata.                                                                                                                                                                                                                                                                     |
| **Samráðsgátt drög** (pre-Alþingi)                   | `sources/pre-law/samradsgatt-drög.md`                             | Residual `curl` from `island.is/samradsgatt/mal/{caseId}` only after MCP sources do not identify the ministry draft; mark VERIFIED-WEB.                                                                                                                                                                                                               |
| **B-deild umræður** (parliamentary debates)          | `sources/pre-law/umraedur/{1,2,3}-umrada.md`                      | Residual `curl` from `althingi.is/altext/{ltg}/raeda/...` only after MCP sources do not include debate transcripts; mark VERIFIED-WEB.                                                                                                                                                                                                                |

**Verification before Stage 2**: confirm `sources/pre-law/` contains the frumvarp, the nefndarálit, the breytingartillögur, and at least the umsagnir from the standard stakeholders (Persónuvernd or equivalent regulator, SA, SI, SFF, Viðskiptaráð, Lögmannafélagið, plus any specialist body relevant to the topic). If any of these is missing, retry the retrieval before proceeding.

### In-force text, comparator, and case law

All rows follow the same pattern: run the listed `legalcode_search` or `legalcode_trace` to locate the result, then `curl -sL "<downloadUrl>" -o "<local path>"`. Use `legalcode_fetch mode:"metadata"` only to inspect one record before relying on it, never to bulk-download.

| Source class                                                                  | Path                                                                | Locator query (then curl the `downloadUrl`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| In-force IS act (consolidated)                                                | `sources/act/lög-NN-YYYY-current.md`                                | `legalcode_search sourceTypes:["law"] jurisdictions:["IS"] mode:"exact" filters:[{lawKey eq "NN/YYYY"}]`. The default returns the in-force version (`versionRole: "current"`). Do not pass `language`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| EU directive/regulation                                                       | `sources/directive/{CELEX}-en.md`                                   | `legalcode_search sourceTypes:["law"] jurisdictions:["EU"] mode:"exact" filters:[{lawKey eq "<CELEX>"}]`. CELEX (e.g. `32016R0679`) is the canonical lookup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Authentic IS translation (EES-viðbætir)                                       | `sources/directive/{CELEX}-is-ees-vidbaetir.md`                     | First inspect the implementing Icelandic act's embedded `Fylgiskjal` (the authentic IS translation lives there for most GDPR-era acts). Otherwise try exact Legalcode IS-law lookup with the translated-act key. Last resort: residual `curl` from `efta.int/sites/.../translated-acts/icelandic/i{CELEX}.pdf` — mark VERIFIED-WEB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| EEA Joint Committee Decision                                                  | `sources/jcd/jcd-{NN}-{YYYY}.md`                                    | `legalcode_search sourceTypes:["guidance"]` or `["law"]` with exact JCD number where available. EFTA `curl` fallback only after MCP miss.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ECJ jurisprudence                                                             | `sources/ecj/{case-ref}.md`                                         | `legalcode_trace relationship:"cases_for_law" lawKey:"EU\|REGULATION\|2016/679/EU" jurisdiction:"EU"`. For a known Curia citation (`C-300/21`) use `legalcode_search sourceTypes:["court_case"] mode:"exact" filters:[{citation eq "C-300/21"}]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| EFTA Court                                                                    | `sources/efta-court/{case-ref}.md`                                  | `legalcode_search sourceTypes:["court_case"]` for EFTA pillar terms/case numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ESA decisions                                                                 | `sources/esa/{ref}.md`                                              | `legalcode_search sourceTypes:["guidance"] jurisdictions:["IS"]` (or `["EU"]`) with agency/ESA terms.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IS regulatory guidance / supervisory-authority úrskurðir (orientation sample) | `sources/is-guidance/{authority-slug}-{ref}.md` (one per úrskurður) | `legalcode_trace relationship:"cases_for_law" lawKey:"IS\|LAW\|<NN/YYYY>" jurisdiction:"IS"` returns both `decisionBodyType: COURT` and `decisionBodyType: ADMINISTRATIVE_AUTHORITY`. Filter the latter into this directory. **Stage 1 retrieves an orientation sample only — the top 10–20 úrskurðir by recency, plus any úrskurður whose title or matter number signals high salience (sektarmál, leyfismál, the sectoral supervisory authority's flagship decisions). The _exhaustive_ per-finding retrieval happens in Stage 5.5, driven by the specific articles Stage 3 surfaces as gold-plated.** Sectoral supervisory authority varies by matter (Persónuvernd for data protection; Fjármálaeftirlitið for financial services; Samkeppniseftirlitið for competition; Fjölmiðlanefnd for audiovisual media; Neytendastofa for consumer protection; Matvælastofnun for food safety; Vinnueftirlitið for occupational safety). Curl each `downloadUrl`. |
| IS case law on the act (orientation sample)                                   | `sources/is-case-law/{court}-{ref}.md`                              | Same `legalcode_trace cases_for_law` call. Filter `decisionBodyType: COURT` into this directory. **Stage 1 retrieves an orientation sample only — the most recent Landsréttur and Hæstiréttur decisions plus any Héraðsdómur decision flagged as substantive (`fullDocumentTokens` > 5000 is a useful heuristic, since procedural orders and traffic-violation cases that incidentally cite the act run small).** A representative sample of 10–20 cases is the goal; do not try to page through 70+ cases here. Exhaustive per-finding retrieval comes in Stage 5.5. The reason: at Stage 1 you do not yet know which articles are gold-plated, so an exhaustive pull retrieves mostly noise. The case that decides your headline finding is almost certainly one that cites the specific gold-plated article in its operative reasoning — a query you can only construct _after_ Stage 3 names the article.                                                |
| **IS case law per-finding targeted retrieval** (Stage 5.5 — see below)        | `sources/is-case-law/_by-finding/{F##}/`                            | After Stage 3 surfaces the gold-plated articles, run MCP searches with the specific verbatim phrase from each finding (`legalcode_search sourceTypes:["court_case"] q:"{N}. gr. laga nr. {NN}/{YYYY}" "{verbatim phrase}"`). See Stage 5.5 for the protocol. This is the corpus that drives Stage 6.2 impact bucketing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Implementing reglugerðir                                                      | `sources/reglugerðir/{NN-YYYY}.md`                                  | `legalcode_search sourceTypes:["law"] jurisdictions:["IS"] filters:[{actType eq "REGULATION"}, {lawKey eq "<NN/YYYY>"} for known numbers]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Nordic comparators (if flag)                                                  | `sources/nordic/{NO,SE,DK,FI}-implementation.md`                    | `legalcode_search sourceTypes:["law"]`, relevant jurisdiction, `mode:"exact"` when the act identifier is known.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

**Coverage gaps that survive**: log to `sources/INDEX.md` and the report's technical `Takmarkanir` section. Reduce overall confidence one level if EES-viðbætir IS translation cannot be retrieved (downstream comparators must use EN, flag findings as "EN-comparison").

### Stage 2 — Harmonisation & Compliance-Architecture Map

Read all `sources/directive/`, `sources/pre-law/athugasemdir/`, `sources/ecj/`. Classify every directive article as **min-harm** / **max-harm** / **blended** / **presumed-max** (per CJEU C-52/00 _Commission v France_ — default presumption is max-harm absent textual indicator). Apply ECJ rulings on min-vs-max via EEA homogeneity (Art. 6 EEA).

**Icelandic vocabulary for the deliverable.** The four classes render in the §2 samræmingarkort and per-article blocks using _plain Icelandic legal terminology_, not literal calques of the EU-English vocabulary:

| Internal class          | Icelandic term in the deliverable                   | What it means in one sentence                                                                                                          |
| ----------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| max-harm                | **ófrávíkjanlegt** (adj.) / **ófrávíkjanleg grein** | Aðildarríki mega ekki víkja frá — hvorki bæta við né draga frá; gullhúðun er ólögmæt.                                                  |
| min-harm                | **lágmarksviðmið**                                  | Aðildarríki mega setja strangari reglur en mega ekki sleppa kjarna.                                                                    |
| blended                 | **blandað**                                         | Hluti greinarinnar er ófrávíkjanlegur, hluti er lágmarksviðmið.                                                                        |
| flexibility clause      | **svigrúmsákvæði**                                  | Tilgreint svið innan ófrávíkjanlegrar greinar þar sem aðildarríki hafa skilgreint svigrúm (sbr. GDPR Art. 6(2)/(3), Art. 23, Art. 84). |
| MS discretion (general) | **svigrúm aðildarríkja**                            | Almennara — það svigrúm sem gerðin í heild lætur eftir innleiðandi ríki.                                                               |

**Forbidden calques** (Stage 9e/9d strip these): _„hámark"_ standalone (means a _numeric_ ceiling in Icelandic, not the legislative-technique concept), _„hámarkssamræming"_ (direct calque from EU-English), _„sveigjanleikaklausa"_ (calque from _„flexibility clause"_ — the established term is _„svigrúmsákvæði"_), _„MS-svigrúm"_ (Anglo-IS hybrid — use _„svigrúm aðildarríkja"_). Full vocabulary table with rationale in `references/gold-plating-doctrine.md` §1.7.

For every IS article, identify its directive counterpart(s) from the athugasemdir. Record the **pairing shape**:

- one counterpart cited → `pairing: "one-to-one"`
- multiple counterparts cited or evident from topic → `pairing: "one-to-many"`, list all in `directive_article_refs`
- the same GDPR article maps to several IS articles → `pairing: "many-to-one"` (set on the IS article that carries the bulk; cross-reference the sister IS articles in `scope_notes`)
- no athugasemd citation, no topic match in the directive, the article addresses a wholly domestic regime → `pairing: "none"`, `no_counterpart: true`, `harmonisation: "n/a"`. **This is a Pattern G30 (heimasmíðuð) gold-plating finding; record it as such — do not treat it as a procedural exception.**

`silent_candidate` (the old single-bit flag) is superseded by `pairing` + `no_counterpart`. Combined/split articles are not silent candidates; only `pairing: "none"` articles are.

**The IS↔EU-instrument pairing is rarely one-to-one.** Iceland routinely combines several EU-instrument articles into a single IS article, splits one EU article across several IS articles, or introduces a domestic article with **no counterpart in the EU instrument at all**. The last case — a `heimasmíðuð` article — is itself a Pattern G30 gold-plating finding. The pairing exercise produces the finding; it isn't a precondition.

**Worked examples on lög nr. 90/2018 ↔ reglugerð (ESB) 2016/679 (GDPR)** — substitute the matter's actual articles when auditing other acts:

- _Combine_ (one-to-many): 9. gr. lög 90/2018 carries the heimildir of GDPR Art. 6(1) plus chunks of Art. 6(2)–(3).
- _Split_ (many-to-one): GDPR Art. 23 restrictions appear in 17.–19. gr. lög 90/2018.
- _Heimasmíðuð_ (none): _rafræn vöktun_ (14. gr.), _bannskrá Þjóðskrár_ (21. gr.), _fjárhagsmálefni og lánstraust_ (15. gr.), _dagsektir_ (45. gr.).

Equivalent patterns exist on every other IS implementation: e.g. MiFID II ↔ lög nr. 115/2021 has multiple split pairings; AMLD ↔ lög nr. 140/2018 has several heimasmíðuð articles around politically-exposed-person screening that go beyond directive minima.

Stage 2's job is to record every pairing shape honestly. Use this schema:

```yaml
articles:
  - is_article_ref: "47. gr."
    pairing: "one-to-one" # one-to-one | one-to-many | many-to-one | none
    directive_article_refs: ["Art. 84"] # always an array; empty when pairing = "none"
    harmonisation: "min"
    no_counterpart: false # true iff pairing = "none" — Pattern G30 candidate
    scope_notes: "Penalties — MS discretion (Art. 84 GDPR)"
  - is_article_ref: "14. gr."
    pairing: "none"
    directive_article_refs: []
    harmonisation: "n/a"
    no_counterpart: true
    scope_notes: "Rafræn vöktun — wholly domestic regime, no GDPR analogue; Pattern G30 candidate"
  - is_article_ref: "17. gr."
    pairing: "one-to-many"
    directive_article_refs:
      ["Art. 12", "Art. 13", "Art. 14", "Art. 15", "Art. 23"]
    harmonisation: "blended"
    no_counterpart: false
    scope_notes: "Transparency + restrictions combined; Art. 23 discretion exercised"

samanburðartafla_in_bill: true | false | "incomplete"
no_counterpart_count: <int> # count of pairing="none" rows
presumed_max_count: <int>
```

The legacy field name `silent_candidate` is renamed to `no_counterpart` for clarity — it always means _Pattern G30 candidate, no directive article to pair against_. Combined / split articles are **not** silent candidates; they have counterparts, just not a one-to-one one.

### Stage 3 — Section-by-Section Comparison

**Every IS article gets a diagnostic block — no silent omissions.** For every numbered article of the act (every `{N}. gr.` plus every Ákvæði til bráðabirgða), run the 14-substep diagnostic and write one block to `articles/{N}-gr.md` populated to `templates/findings-report.md §3` format.

Articles where the analysis finds no divergence still get a block: fill 3.{N}.7 with `N/A — no divergence`, 3.{N}.8 with `— (no finding)`, and leave 3.{N}.10 (counter-argument stress test) empty. Silently omitting an article is the same procedural failure as missing pre-law evidence — Stage 8.5 will catch it.

**Worklist binding.** The authoritative worklist for Stage 3 is `article-index.json` produced in Stage 2. One `articles/{N}-gr.md` per `articles[]` entry. At the end of Stage 3, `find articles/ -name "*-gr.md" | wc -l` must equal `jq '.articles | length' article-index.json`.

**Per-article directive pairing is mandatory but does not require a counterpart to exist.** Every `articles/{N}-gr.md` must populate template §3.{N}.2 (Directive counterpart) with one of the four pairing shapes recorded in `article-index.json`:

- **`one-to-one`** — name the specific GDPR/directive article (`Art. 84`, not "the sanctions article").
- **`one-to-many`** — list every GDPR article the IS article combines (`Art. 12, Art. 13, Art. 14, Art. 15, Art. 23`). Run the 3.{N}.5 word-by-word diagnostic against each, in the order they appear in the IS article.
- **`many-to-one`** — name the single GDPR article and note that the IS implementation splits across multiple IS articles (cross-reference the sister `articles/*-gr.md` blocks).
- **`none`** (heimasmíðuð) — fill §3.{N}.2 with `No GDPR counterpart — Pattern G30 candidate (heimasmíðuð)`. **This is itself the gold-plating finding** — proceed through 3.G/3.N substeps and classify severity normally; do not skip the block. The Davidson category is automatic: vehicle-integrity breach (Pattern G30). Explain in §3.{N}.6 what domestic regime the article carries and why no GDPR article addresses it.

Combined (`one-to-many`) and split (`many-to-one`) pairings are common in Icelandic transposition across every sector (GDPR Arts. 6, 9, 23, 32 split or merged in lög 90/2018; MiFID II Arts. 24–25 routinely split across lög 115/2021; AMLD Art. 13 customer-due-diligence rules combined in lög 140/2018). Heimasmíðuð (`none`) articles are the headline gold-plating cases on every IS transposition — the lög 90/2018 worked example surfaces _rafræn vöktun_ (14. gr.), _bannskrá Þjóðskrár_ (21. gr.), _fjárhagsmálefni og lánstraust_ (15. gr.), _dagsektir_ (45. gr.) — none of which has a GDPR counterpart, and that absence is the finding. Other acts will surface their own heimasmíðuð additions; the discipline is identical.

The 14 substeps:

- **3.A Citation check** — locate "Um {N}. gr." in greinargerð. Silent = Pattern G candidate.
- **3.B Scope (gildissvið)** — territorial/personal/material widening vs directive Art. 2 (Davidson-1).
- **3.C Definitions (skilgreiningar)** — substituted wider IS terms (Pattern A5).
- **3.D Numerical thresholds** — grep both texts; lower IS threshold = Davidson-1 / Pattern A1.
- **3.E Modal verbs** — skal/má/heimilt/ber að/óheimilt. Directive _may_ + IS **skal** = Davidson-2 / Pattern B6.
- **3.F Flexibility clauses** — _where appropriate / where necessary / without prejudice to_ preserved as _eftir því sem við á / eftir þörfum / með fyrirvara um_? Each deletion = Pattern E25.
- **3.G Quantifiers** — universal IS (öllum / sérhver / hver sá sem) replacing specific addressee = Davidson-1 / Pattern A2.
- **3.H Temporal triggers** — án tafar / tafarlaust / ársfjórðungslega / earlier date = Davidson-3 or Davidson-4 / Pattern C18.
- **3.I Procedural mechanics** — notification vs prior authorisation (C11); tech-neutral vs written/notarised (C12); burden reversed (C13); shorter transitions (C14); lower de minimis (C15); tighter filings (C16).
- **3.J Sanctions** — criminalisation vs administrative (Davidson-3 / Pattern D17); higher fine caps (D18); joint-and-several (D19); director liability (D20); fee/levy (D21).
- **3.K Transitional periods** — Davidson-4 if shorter.
- **3.L Exemptions/carve-outs** — omitted carve-out = Pattern A4.
- **3.M Connectors** — auk þess / enn fremur / jafnframt / þá skal einnig — check directive contemplates the addition. Pattern E22.
- **3.N Vehicle integrity (hrein innleiðingarfrumvörp)** — does article trace back to any directive article? If not, Pattern G30.

For each finding: propose severity (CRITICAL / HIGH / MEDIUM / LOW) and confidence (1-5). Disclosure is provisional here — Stage 4 confirms.

### Stage 4 — Pre-Law Source Forensics

For **each** HIGH/CRITICAL finding from Stage 3, write one forensic block to `forensics/{finding_id}.md` populated to `templates/findings-report.md §4` format. 10 substeps:

- **4.A Article note** — confirm "Um {N}. gr." wording.
- **4.B §8(b) disclosure test** — grep greinargerð for **"gengur lengra" / "umfram lágmark" / "nýtir heimild aðildarríkja" / "frávik frá"**. Classify: DISCLOSED | DISCLOSED-GENERAL | UNDISCLOSED.
- **4.C RIA test** — locate mat á áhrifum. Classify: QUANTIFIED | NARRATIVE | BOILERPLATE | ABSENT.
- **4.D Samráðsgátt drög→frumvarp diff** — read `sources/pre-law/samradsgatt-drög.md` if present. Origin: MINISTRY-INTRODUCED | POST-CONSULTATION-ADDED | NOT-IN-DRÖG.
- **4.E Stakeholder objection mapping** — grep `sources/umsagnir/*.md` for the article number + flagging language. Tabulate.
- **4.F Committee response** — read nefndarálit; did committee notice? amend?
- **4.G Amendment tracing** — list breytingartillögur per article.
- **4.H Umræður check** — grep `sources/pre-law/umraedur/*.md` for the article + minister name.
- **4.I Introducing actor** — synthesise 4.D + 4.F + 4.G. Origin: ministry | committee-majority | committee-minority | floor-amendment | late-amendment | sub-statutory.
- **4.J Disclosure classification** — DISCLOSED-JUSTIFIED | DISCLOSED-UNJUSTIFIED | UNDISCLOSED.

### Stage 5 — Reglugerð Sweep

For each reglugerð in `sources/reglugerðir/`, apply a thin Stage-3 diff (14 substeps), then attempt Stage-4 forensics with substitute sources (ministry press release, samráðsgátt consultation on the reglugerð draft, FOI memo). Write findings to `forensics/reglugerd-{NN-YYYY}.md`.

### Stage 5.5 — Per-Finding Impact-Corpus Retrieval (targeted MCP search)

**This is the most consequential retrieval stage of the skill.** Stage 1 pulled an orientation sample — useful for ambient grounding but biased toward the most recent and most frequently-cited cases, which are not necessarily the cases that bear on _the specific gold-plated articles you have now identified_. Stage 3 just surfaced those articles. Stage 6.2 is about to need the actual cases that engaged with the gold-plated wording. Stage 5.5 is the bridge: for each surviving HIGH/CRITICAL finding (and the strongest 🟡 candidates), run targeted MCP searches with the _specific verbatim phrase_ from Stage 3 and download the cases that match.

**Why this exists as a separate stage.** The original skill assumed that the broad `legalcode_trace cases_for_law` pull in Stage 1 plus a `grep` over the downloaded corpus would surface the cases that engage with each finding. In practice the broad pull misses the headline cases — the case that actually decides your CRITICAL finding is often (a) a Landsréttur or Hæstiréttur judgment that engages the gold-plated phrase in its operative reasoning, (b) ranked outside the top-N by the broad query, and (c) discoverable only by a phrase search against the _finding's exact wording_. `grep` cannot find a case you did not download. Stage 5.5 closes that loop.

#### 5.5.A Inputs

For each finding `F##` (HIGH/CRITICAL primarily; strongest 🟡 also worthwhile) collect from §3.{N}:

- The IS article reference (e.g. `51. gr.`).
- The full act reference (e.g. `laga nr. 90/2018`).
- The _specific gold-plated phrase_ from §3.{N}.1 — the exact Icelandic wording that diverges from the EU instrument (e.g. _„fjárhagslegt tjón"_, _„fangelsi allt að þremur árum"_, _„leyfi Persónuverndar"_, _„rafræn vöktun"_, _„bannskrá Þjóðskrár"_).
- The corresponding article in the EU instrument (e.g. `82. gr. reglugerðar`, `84. gr.`).

#### 5.5.B Query patterns

Run _all of these_ per finding, in this order. Each builds on the others — do not stop at the first non-empty result set.

1. **Article-citation search (IS courts)** — finds cases that cite the gold-plated IS article in their reasoning:

   ```json
   {
     "sourceTypes": ["court_case"],
     "jurisdictions": ["IS"],
     "q": "\"{N}. gr. laga nr. {NN}/{YYYY}\"",
     "page": { "limit": 20 }
   }
   ```

   Example for F07 (51. gr.): `q: "\"51. gr. laga nr. 90/2018\""`. This is the most direct query and usually surfaces the operative cases.

2. **Cross-article comparison search** — finds cases that compare the gold-plated IS article to the EU instrument's article (this is how _„túlkað fram hjá ákvæðinu"_ cases surface):

   ```json
   {
     "sourceTypes": ["court_case"],
     "jurisdictions": ["IS"],
     "q": "\"{N}. gr. laga nr. {NN}/{YYYY}\" OR \"{M}. gr. reglugerðar\"",
     "page": { "limit": 20 }
   }
   ```

   Example for F07: `q: "\"51. gr. laga nr. 90/2018\" OR \"82. gr. reglugerðar\""`. The case where a court _named the misræmi_ will be ranked high by phrase-proximity.

3. **Verbatim-phrase search** — finds cases that use the specific gold-plated wording itself, even when they do not cite the article by number:

   ```json
   {
     "sourceTypes": ["court_case"],
     "jurisdictions": ["IS"],
     "q": "\"{verbatim gold-plated phrase}\"",
     "page": { "limit": 20 }
   }
   ```

   Example for F01 (rafræn vöktun): `q: "\"rafræn vöktun\" \"14. gr. laga nr. 90/2018\""`. Example for F07: `q: "\"fjárhagslegt tjón\" \"persónuvernd\""`. This surfaces _„farið fram hjá ákvæðinu"_ cases where claimants routed around the IS article.

4. **Supervisory-authority decisions** — re-run the same three queries against `sourceTypes: ["case"]` filtered to `decisionBodyType: ADMINISTRATIVE_AUTHORITY`. The supervisory authority of the matter (Persónuvernd, Fjármálaeftirlitið, etc.) applies the act far more often than the courts; its úrskurðir are the densest impact signal.

5. **EU/ECJ counterpart-article retrieval** — for each finding's GDPR/directive article, retrieve the leading ECJ jurisprudence:

   ```json
   {
     "sourceTypes": ["court_case"],
     "jurisdictions": ["EU"],
     "q": "{counterpart article designator and instrument keywords}",
     "page": { "limit": 10 }
   }
   ```

   Example for F07: search for C-300/21, C-340/21, C-667/21, C-456/22 (Art. 82 GDPR damages line). Example for F06: search for C-807/21 _Deutsche Wohnen_ (Art. 83 sektir as sjálfstæð viðurlög).

#### 5.5.C Storage

Write retrieved cases into per-finding directories:

```
sources/is-case-law/_by-finding/F01/{court}-{ref}.md   # rafræn vöktun cases
sources/is-case-law/_by-finding/F07/{court}-{ref}.md   # bætur cases incl. Landsréttur 312/2025
sources/is-guidance/_by-finding/F01/{authority}-{ref}.md
sources/ecj/_by-finding/F07/{case-ref}.md              # C-300/21 etc.
```

Duplication with `sources/is-case-law/` (the Stage-1 orientation sample) is acceptable and expected — a case can both be in the orientation sample _and_ indexed under the finding it supports. The Stage-1 broad pull is "what's the landscape"; the Stage-5.5 per-finding pull is "what bears on this specific gold-plating".

#### 5.5.D Coverage check

After running the five query patterns for every HIGH/CRITICAL finding, write `sources/_by-finding-coverage.md` listing per finding: queries run, cases retrieved, and any _„engin þekkt mál"_ entries (with the queries that returned empty, dated). A finding with zero per-finding cases is acceptable for Stage 6.2 as _„No documented impact yet"_ — but the empty result must be the output of _targeted_ queries, not the silence of grep over a broad-but-incomplete corpus.

#### 5.5.E Common failure modes

- **Stopping at the first non-empty query**: query #1 returns a list and the orchestrator declares victory. The case that names the misræmi is often in query #2's result set, not #1. Run all five.
- **Missing the supervisory authority**: for matters applied primarily by Persónuvernd / Fjármálaeftirlitið / etc., the impact signal lives in administrative decisions, not court judgments. Always include query #4.
- **Forgetting the EU counterpart corpus**: Art. 6 EES homogeneity means ECJ jurisprudence directly shapes the EFTA-pillar interpretation. Without query #5 the Stage-8 stress test cannot run the _„EES homogeneity defence"_ properly.
- **Treating verbatim phrase search as redundant**: it is not. _„fjárhagslegt tjón"_ surfaces cases that _use_ the term without citing 51. gr. by number — i.e. cases where claimants worked around the gold-plated wording. These are the _„farið fram hjá ákvæðinu"_ impact bucket and matter for the strength assessment.

#### 5.5.F Output

Stage 5.5 hands Stage 6.2 a finding-indexed corpus. Stage 6.2 then classifies each finding into one of the five impact buckets (Applied as written / Read past / Judicially acknowledged / Routed around / No documented impact yet) with a leading citation drawn from the Stage-5.5 corpus. The two stages were previously fused; separating them makes the _retrieval_ explicit and the _analysis_ falsifiable.

### Stage 6 — Cross-Verification (EFTA Court, ECJ, ESA, Nordic, IS impact)

For each HIGH/CRITICAL finding, run two passes.

#### 6.1 European cross-verification

- `sources/efta-court/*.md` — any EFTA-pillar holding on this provision?
- `sources/ecj/*.md` — landmark interpretations? Apply via Art. 6 EEA homogeneity.
- `sources/esa/*.md` — infringement letter / reasoned opinion / EFTA Court referral?
- `sources/nordic/*.md` — did Norway/Sweden/Denmark/Finland transpose without this gold-plating?

#### 6.2 Icelandic in-country impact check (mandatory)

The gold-plating skill produces a _forward-looking_ compliance audit, but the substantive credibility of a finding depends heavily on whether the gold-plated wording has _already_ mattered in practice. **The corpus for this check is the per-finding directory built by Stage 5.5** (`sources/is-case-law/_by-finding/{F##}/` and `sources/is-guidance/_by-finding/{F##}/`), not the broad orientation sample from Stage 1. The orientation sample helps grounding but does not substitute for finding-targeted retrieval — see Stage 5.5 for the protocol and the reasoning.

If Stage 5.5 has not been run for a finding, **do not classify the impact bucket from the orientation sample alone**. Loop back to Stage 5.5 for that finding before proceeding. A bucket assignment without targeted retrieval behind it is an inference from absence-of-evidence, not evidence-of-absence, and Stage 8.5 will reject it.

Per-finding, scan both layers of Icelandic adjudication in the finding's directory:

1. **`sources/is-case-law/_by-finding/{F##}/`** — IS court decisions retrieved by Stage 5.5 queries #1–#3 (article-citation, cross-article comparison, verbatim phrase).
2. **`sources/is-guidance/_by-finding/{F##}/`** — administrative úrskurðir of the supervisory authority retrieved by Stage 5.5 query #4. Sectoral regulators apply their administering acts far more often than the courts do; their decisions are the densest impact signal. Examples by sector: **Persónuvernd** (data protection — lög 90/2018 / 75/2019), **Fjármálaeftirlitið** (financial services), **Samkeppniseftirlitið** (competition), **Fjölmiðlanefnd** (audiovisual media), **Neytendastofa** (consumer protection), **Matvælastofnun** (food safety), **Vinnueftirlitið** (occupational safety).

The **specific gold-plated wording** that drove the Stage 5.5 retrieval (e.g. _„fjárhagslegt tjón"_, _„fangelsi allt að þremur árum"_, _„leyfi Persónuverndar"_, _„rafræn vöktun"_, _„bannskrá Þjóðskrár"_ for the lög 90/2018 worked example) is also the phrase you grep within each retrieved decision to confirm which reasoning paragraphs are operative. Worked examples from the lög nr. 90/2018 illustration: _„fjárhagslegt tjón"_ in 51. gr., _„fangelsi allt að þremur árum"_ in 48. gr., _„leyfi Persónuverndar"_ in 15. gr. and 31. gr., _„rafræn vöktun"_ in 14. gr., _„bannskrá Þjóðskrár"_ in 21. gr. For other acts, identify the analogous gold-plated phrase from the finding itself. Classify the impact into one of five buckets, ordered roughly by evidentiary weight:

| Impact bucket                                | What it means                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Evidence shape                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Applied as written**                       | A court or the sectoral supervisory authority applied the gold-plated provision and the wording shaped the outcome. The over-implementation has _bitten_.                                                                                                                                                                                                                                                                                                                         | Citation to the IS article in the operative reasoning; outcome turns on the IS-specific wording.                                                                                                                                                                                                                                                         |
| **Read past via EEA-conform interpretation** | A court invoked 3. gr. lög 2/1993 (EEA-conform construction), the act's own regulation-supremacy clause where present (e.g. 3. mgr. 5. gr. lög 90/2018 — analogous clauses exist in other transposing acts), or direct effect of the underlying EU article to _override_ the gold-plated wording. The court named the divergence and resolved it against the IS text.                                                                                                             | Express discussion of IS vs EU-instrument wording in the judgment; reliance on the EU instrument's article over the IS article; CJEU / EFTA Court citation.                                                                                                                                                                                              |
| **Judicially acknowledged**                  | A court or the supervisory authority has _named the divergence between the IS provision and the underlying EU-instrument article_ in its reasoning — even in obiter, concurrence, dissent, or a passing remark — without needing to resolve the conflict on the facts of that case. The fact that adjudicators have looked at both texts and articulated the incongruity is itself strong evidence the gold-plating is on the legal community's radar and is likely to be tested. | Express comparison of the IS text and the EU-instrument text in the reasoning (e.g. _„ekki að öllu leyti sambærileg"_, _„gengur lengra en"_, _„er strangari en"_, _„hefur sérstöðu umfram"_); reference to the EES-viðbætir text or EUR-Lex; CJEU dicta cited without controlling the holding; commentary by sérfróður meðdómandi noted in the judgment. |
| **Routed around**                            | Parties or the supervisory authority chose a _different_ legal basis to avoid the gold-plated provision's limitation. The very existence of a workaround pattern is evidence the wording is creating routing distortions.                                                                                                                                                                                                                                                         | E.g. (lög 90/2018 illustration) claimants routing through skaðabótalög 50/1993 §26b for miskabætur because 51. gr. limits to _fjárhagslegt tjón_; or a supervisory authority citing the EU-instrument article directly while the IS counterpart goes uncited. Analogous routing patterns surface on every gold-plated act.                               |
| **No documented impact yet**                 | The per-article sweep returned no citations. Acceptable but must be stated and dated. Reduce confidence one tier if the finding is severity HIGH or CRITICAL.                                                                                                                                                                                                                                                                                                                     | `grep` returns empty; record search date and corpus size searched.                                                                                                                                                                                                                                                                                       |

**Note on overlap.** A single case can sit in more than one bucket — Landsréttur 312/2025 is both _Judicially acknowledged_ (it names the 51. gr. ↔ 82. gr. GDPR incongruity in ¶ 21) and _Read past_ (it applies Art. 82 directly in ¶ 22). When a case fits multiple buckets, record the highest-weight one (Applied > Read past > Judicially acknowledged > Routed around) and note the others in the operative quote.

Write the per-finding impact assessment to `forensics/{finding_id}.md` under a new section `### Impact in practice`. Quote the operative passage from the cited decision verbatim; cite by public reference (case number + court + date, or Persónuvernd úrskurður nr. + dagsetning). Where the impact bucket is _Read past_ or _Routed around_, this materially _strengthens_ the gold-plating finding — the gold-plated wording is documentably creating friction or being overridden.

Concrete examples of strong findings (for the lög 90/2018 example act):

- **51. gr. (bætur — _fjárhagslegt tjón_)**: Landsréttur 312/2025 named the divergence between 51. gr. and 82. gr. GDPR explicitly and applied Art. 82 directly via 3. mgr. 5. gr. lög 90/2018, citing CJEU C-300/21 _Österreichische Post_, C-340/21, C-667/21, C-182/22 og C-189/22 — _Read past_. Héraðsdómur E-5748/2024 awarded miskabætur via §26b skaðabótalaga 50/1993 with its higher _stórfellt gáleysi_ threshold — _Routed around_.
- **48. gr. (refsingar)**: search for criminal prosecutions under the article. Documented absence is itself meaningful — the criminal regime has never been used in 7 years, which speaks to whether the gold-plating is functional or symbolic.
- **14. gr. (rafræn vöktun)**: search Persónuvernd's úrskurðir for "rafræn vöktun" citations. High-volume — workplace-monitoring complaints are a Persónuvernd staple.

#### 6.3 Summary roll-up

Build `impact-summary.md`: one row per HIGH/CRITICAL finding showing finding ID, the gold-plated article, the impact bucket, the leading citation (or _engin þekkt mál_), and a one-sentence note. This feeds the §0.1 _Yfirlit niðurstaðna_ table at the top of the deliverable and the §4.{ID}.10 per-finding impact recap.

### Stage 7 — Severity Register

Severity matrix:

| Símbol | Stig (íslensk heiti, kynntri einu sinni í §0) | Criteria                                                                                  |
| ------ | --------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 🔴     | alvarlegt                                     | Divergence from max-harm or presumed-max provision; unlawful under EFTA Court homogeneity |
| 🟠     | hátt                                          | Undisclosed divergence from min-harm provision; breach of §8(b) and/or §37(1)             |
| 🟡     | miðlungs                                      | Disclosed but not substantively justified; §8(b) satisfied formally, no RIA               |
| 🟢     | lágt                                          | Disclosed AND justified (RIA-backed); flagged for stakeholder review                      |

**Style rule for the deliverable — symbol only, never the all-caps word.** In the report, the .docx, and every supporting file, severity is conveyed by the colored circle alone (`🔴` / `🟠` / `🟡` / `🟢`). The all-caps labels `ALVARLEG`, `HÁ`, `MIÐLUNGS`, `LÁG` are **forbidden as visual tokens** because they crowd table cells, dominate the reading order, and look like rubber stamps. The reader is told once, in §0 _Heildarfjöldi niðurstaðna_, what each color means (`9: 🔴 1 alvarleg — 🟠 4 háar — 🟡 3 miðlungs — 🟢 1 lág`) and from that point on the symbol carries the meaning. Concrete consequences:

- §0.1 _Yfirlit niðurstaðna_ table — _Alvarleiki_ column shows `🔴` (not `🔴 ALVARLEG`). Same for §3.0 _Yfirlitstafla yfir allar greinar_, §6 _Sjálfsprófun_, and `impact-summary.md`.
- §3.{N}.8 _Alvarleikastig_ field — the per-article block fills the field with the circle plus an explanatory clause in sentence-case prose if needed (`☑ 🔴. Mótbroti við 82. gr. reglugerðar ...`). Never `☑ 🔴 ALVARLEG`.
- §6 _Sjálfsprófun_ table — both _Upphafleg flokkun_ and _Endanleg flokkun_ columns are circles only.
- Stress-test files — `original severity: 🔴 → final severity: 🔴`, not `original severity: ALVARLEG`.
- Forensic-block titles — `Niðurstaða F05 — 51. gr. Bætur (🔴)`, not `... (ALVARLEG)`.
- Prose mentions where the severity is the subject of a sentence — use the sentence-case word in running prose (`alvarleikastig stendur 🔴`, or in narrative `niðurstaðan er alvarleg`); never the all-caps version.

Stage 9d adds a grep check:

```bash
grep -nE "\\b(ALVARLEG|MIÐLUNGS)\\b|\\bHÁ\\b|\\bLÁG\\b" Gullhudunarskyrsla-*.md | grep -vE "HÁMARK|háð|hámark|HÁMARKS"
```

A hit is a hard fail — replace each with the corresponding circle (or sentence-case word in prose) before delivery.

**Confidence levels**: Definite 95%+ | High 80–95% | Probable 60–80% | Possible 40–60% | Unlikely <40%. Report Possible only if 🔴/🟠; skip Unlikely. The confidence vocabulary (Mikill / Hár / Líklegur / Mögulegur / Ólíklegur) is independent of the severity vocabulary and uses sentence-case Icelandic words throughout — no caps, no symbols.

**Confidence drivers**: + EES-viðbætir available; + multiple corroborating umsagnir; + ESA action; + ECJ/EFTA Court holding; − reglugerð pending; − bill amending the act.

### Stage 8 — Iron Law 7 Counter-Argument Stress Test

**Mandatory for every HIGH/CRITICAL finding.** For each, construct the strongest counter-argument across six defence vectors. Write to `stress/{finding_id}.md`:

1. **JCD adaptation defence** — was divergence required by an EEA Joint Committee Decision adaptation (read `sources/jcd/`)?
2. **EEA homogeneity defence (Art. 6 EEA)** — does ECJ jurisprudence (read `sources/ecj/`) fix the "minimum required" baseline more strictly than directive text?
3. **Protocol 35 defence** — prevailing-EEA-rule mis-characterised as gold-plating?
4. **Constitutional defence** — required by stjórnarskrá (atvinnufrelsi 75. gr. / eignarréttur 72. gr. / friðhelgi einkalífs 71. gr. / jafnræðisregla 65. gr.)?
5. **Pre-existing-regime defence** — pre-EEA IS law preserved under directive "without prejudice to existing higher standards" clause?
6. **Policy-justification defence** — does greinargerð articulate legitimate distinct Icelandic-context rationale?

Outcome: **survives** (severity unchanged) | **downgrade** (one tier) | **remove** (defence dispositive, document and exit).

Record the outcome on the per-finding row in template §6 (Sjálfsprófun): original severity → final severity, and the single sentence of new evidence or counter-authority that drove the change. "No change, no new evidence" is an acceptable entry but must be stated explicitly. Every HIGH/CRITICAL finding gets a row; missing rows are a Stage 8.5 fail.

### Stage 8.5 — Findings-Register Validation

Before Stage 9 begins, verify that every HIGH/CRITICAL finding has the expected on-disk evidence package. This is a file-existence check, not new analysis.

For each finding listed in the in-memory register (and in `articles/_register.md` if maintained):

1. **Article coverage (run first)** — `find articles/ -name "*-gr.md" | wc -l` equals `jq '.articles | length' article-index.json`. Every IS article has a Stage 3 block, including no-finding articles. Any shortfall means Stage 3 was not completed — loop back to Stage 3 for the missing articles before continuing.
2. **Directive pairing per article** — every per-article block populates §3.{N}.2. `grep -L "Directive counterpart" articles/*-gr.md` returns nothing. A block is valid if it either (a) names one or more GDPR articles, or (b) declares `No GDPR counterpart — Pattern G30 candidate (heimasmíðuð)`. The second case is a finding, not a defect: a heimasmíðuð article without a Pattern G30 severity classification in §3.{N}.8 is the Stage 8.5 fail mode, not the absence of a counterpart. Verify: `grep -L "Pattern G30\|GDPR\|Art\\." articles/*-gr.md` returns nothing.
3. **Article block per finding** — `ls articles/{is-article-ref}-gr.md` exists for every entry in the findings register.
4. **Forensic block** — `ls forensics/{finding_id}.md` exists (HIGH/CRITICAL only).
5. **Stress block** — `ls stress/{finding_id}.md` exists (HIGH/CRITICAL only).
6. **Stress outcome recorded** — `grep -l "original severity:" stress/{finding_id}.md` returns a hit. The before/after row from Stage 8 must be in the file.
7. **Impact check recorded** — for every HIGH/CRITICAL finding, `grep -l "Impact in practice\|Impact bucket\|Áhrif í framkvæmd" forensics/{finding_id}.md` returns a hit. The finding lists one of the five impact buckets (Applied as written / Read past / Judicially acknowledged / Routed around / No documented impact yet) with the supporting citation or an explicit `Engin þekkt mál` after a dated search. Missing impact-check rows mean Stage 6.2 was not completed — loop back, do not proceed.
8. **Impact roll-up exists** — `ls impact-summary.md` and the file has one row per HIGH/CRITICAL finding. This roll-up feeds §0 of the deliverable.

Write `validation-report.md` listing any gaps. **Do not proceed to Stage 9 with gaps.** Re-run the missing stage for the affected finding before drafting.

This stage is procedural, not substantive — it confirms the trail of artifacts the deliverable will rely on actually exists. It is the cheapest possible insurance against silent omissions.

### Stage 9 — Output Generation

**The entire deliverable lives in Markdown until the very last step.** All substantive editing happens against `Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.md`. The Icelandic grammar/language pass is the **last markdown-editing step**. Only after that pass, and after a final verifier check, do we generate the `.docx`. Never edit the `.docx` directly.

The ordered substages are:

| #   | Substage                                                   | What it edits           | Format   |
| --- | ---------------------------------------------------------- | ----------------------- | -------- |
| 9a  | Draft the report                                           | new file                | markdown |
| 9b  | 3-pass Self-Interrogation (HIGH/CRITICAL)                  | substantive content     | markdown |
| 9c  | Post-draft source-grounding pass                           | substantive content     | markdown |
| 9d  | Verifier edit-on-fail loop                                 | substantive content     | markdown |
| 9e  | Icelandic language / grammar pass — **last markdown step** | prose / vocabulary only | markdown |
| 9f  | Render `.docx` (no further content edits)                  | new file                | docx     |

**9a — Draft the report.** Populate `templates/findings-report.md` end-to-end as `Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.md`. Apply Icelandic OSCOLA citations.

**9b — 3-pass Self-Interrogation on every HIGH or CRITICAL finding:**

1. Re-confirm divergence — re-read IS article + directive EN + EES-viðbætir IS + greinargerð.
2. Re-run stress test — confirm Stage 8 outcome.
3. Hostile-reviewer pass — steelman a senior partner at LEX / BBA//Fjeldco / LOGOS / LMB challenging the finding before utanríkismálanefnd.

Where any of the three passes reveals a flaw, **edit the draft to address it and record the change** in template §6 (Sjálfsprófun) (one sentence: what changed, why). A self-interrogation that produces no edits is acceptable only when explicitly stated as "endurskoðun staðfestir flokkun, engin ný gögn".

**9c — Post-draft source-grounding pass (mandatory).** Walk every material claim in the draft back to a stored source. The discipline is: read the draft top to bottom and for each finding's verbatim quote (§3.{N}.1, §3.{N}.2, §3.{N}.3, §4.{ID}.3, §4.{ID}.6) confirm it actually appears in the cited file under `sources/`.

Concrete steps:

1. **Per article block** — for each `articles/{is-article-ref}.md` claim, `grep -F "{quoted text}" sources/act/log-NN-YYYY-current.md` (or the equivalent file path). Hit required.
2. **Per directive comparator (authentic IS text)** — **mandatory; no model-generated translations permitted**. For every Icelandic verbatim quote of an EU-instrument provision (every blockquote attributed to _„reglugerðar"_, _„tilskipunar"_, _„ákvörðunar"_, or the like, and every cell of §3.{N}.5 / §4.{ID}.0 in the IS-translation row), the exact bytes of the quote must appear in one of the authentic sources, checked in this order:
   - **First**: the implementing Icelandic act's embedded `Fylgiskjal` — `grep -F "{quoted text}" sources/act/log-NN-YYYY-current.md` (this is where the authentic IS GDPR translation lives for lög 90/2018; analogous fylgiskjöl exist for other directly-incorporated regulations).
   - **Second**: the EES-viðbætir IS file if separately retrieved — `grep -F "{quoted text}" sources/directive/{CELEX}-is-ees-vidbaetir.md`.
   - **Last resort**: EUR-Lex EN with the `EN-comparison` flag preserved and the Icelandic quotation removed (the EN text replaces it; do not paraphrase to Icelandic).

   **A miss on both authentic-IS files means the IS quote was generated by the model.** That is a hard fail — replace the generated text with the actual fylgiskjal/EES-viðbætir bytes before proceeding. The most common failure mode is the model approximating with terms like _„efnislegt eða ófjárhagslegt tjón"_ when the authentic fylgiskjal uses _„eignatjón eða óefnislegt tjón"_; the analysis built on the approximated terms (Davidson classification, severity, recommendations) then misclassifies what the actual EEA-translation says. Always retrieve, never compose.

3. **Per umsögn snippet** — `grep -lr "{quoted text}" sources/umsagnir/` returns a file. The cited submitter must match the file's `sender:` metadata.
4. **Per greinargerð passage** — `grep -F "{quoted text}" sources/pre-law/frumvarp-*.txt` (or the equivalent converted file). Hit required.

Mark any claim that fails the grep with `[UNGROUNDED]` inline in the draft. **An `[UNGROUNDED]` tag is a Stage 9d fail trigger** — proceed to 9d, do not deliver.

**9d — Verifier edit-on-fail loop (mandatory).** Run the report against three checks:

1. **Stage 8.5 re-check** — every HIGH/CRITICAL finding still has the expected files? Re-run the file-existence pass.
2. **9c grounding re-check** — `grep -nE "\\[UNGROUNDED\\]|\\[VERIFY\\]" Gullhudunarskyrsla-*.md` returns no hits. Any hit is a fail.
3. **Counter-argument outcomes recorded** — every HIGH/CRITICAL finding has a row in the report's self-assessment changelog table with original severity, final severity, and the driving evidence sentence.
4. **Internal-tooling leak check** — run the full Stage-9e internal-tooling grep against the report. Zero hits required. Any tool name, skill name, sourceRef, flowKey, internal stage reference, or working-directory path remaining in the draft is a hard fail.
5. **Quoted-comparison check** — every HIGH/CRITICAL divergence claim shows both the IS text and the GDPR/directive text as verbatim blockquotes. `grep -A2 -E "🔴|🟠" Gullhudunarskyrsla-*.md | grep -c "^>"` should return at least twice the finding count.
6. **Severity-label style check (mandatory)** — severity is conveyed by the colored circle alone in the deliverable. The all-caps tokens `ALVARLEG`, `HÁ`, `MIÐLUNGS`, `LÁG` are not allowed as standalone visual labels in tables, headings, or assertions. Run:

   ```bash
   grep -nE "\\b(ALVARLEG|MIÐLUNGS)\\b|\\bHÁ\\b|\\bLÁG\\b" Gullhudunarskyrsla-*.md | grep -vE "HÁMARK|háð|hámark|HÁMARKS"
   ```

   Zero hits required. Replace each hit with the corresponding circle (in tables/headings) or with the sentence-case Icelandic word (in narrative prose). The legend in §0 _Heildarfjöldi niðurstaðna_ defines the colors once; no caps labels are needed elsewhere.

7. **Authentic-IS-translation grounding check (mandatory)** — every Icelandic blockquote that the report attributes to an EU instrument (reglugerð / tilskipun / ákvörðun) must literally appear in an authentic Icelandic source. Extract each candidate with:

   ```bash
   awk '/^> ?„/{print}' Gullhudunarskyrsla-*.md | grep -E "reglugerð|tilskipun|ákvörðun" -B1 -A0
   ```

   For each blockquote returned, run `grep -F "{stripped quote}" sources/act/log-NN-YYYY-current.md` (the fylgiskjal) and, if not found there, `grep -F "{stripped quote}" sources/directive/*-is-ees-vidbaetir.md`. Zero matches means the quote was model-generated rather than retrieved — hard fail. Edit the deliverable to substitute the actual fylgiskjal/EES-viðbætir bytes, then re-run all checks.

8. **§3.0 yfirlitstafla column-count check (mandatory)** — the scannability table at §3.0 must have exactly five columns: `IS-grein | Grein gerðar | Niðurstaða | Áreiðanleiki | Áhrif í framkvæmd`. A _Samsvörun_ column (einn-á-einn / einn-á-marga / heimasmíðuð) is redundant because the pairing shape is fully derivable from _Grein gerðar_. Run:

   ```bash
   awk '/^### 3\.0 Yfirlitstafla/{found=1} found && /^\| IS-grein/{print; exit}' Gullhudunarskyrsla-*.md \
     | tr -cd '|' | wc -c
   ```

   The expected output is **6** (five columns produce six `|` characters: leading, four interior, trailing). Any other number — and specifically 7, which means a _Samsvörun_ column slipped in — is a hard fail. Restructure the table to five columns, encoding pairing-shape and special-case metadata inside the _Grein gerðar_ cell directly (see anti-pattern nr. 22).

9. **Calque vocabulary check (mandatory)** — the harmonisation-class terminology must use the preferred Icelandic legal terms, not literal translations of the EU-English jargon. Run:

   ```bash
   grep -nE "\\bHámark\\b|\\bhámark\\b|Hámarkssamræm|hámarkssamræm|\\bsveigjanleikaklausa\\b|Sveigjanleikaklausu|MS-svigrúm" Gullhudunarskyrsla-*.md \
     | grep -vE "hámarksdagsekt|hámarkshraði|hámarksfjárhæð|hámarksregla"
   ```

   Zero hits required. Replace each with the preferred term from the Stage-2 vocabulary table (`ófrávíkjanlegt` / `lágmarksviðmið` / `svigrúmsákvæði` / `svigrúm aðildarríkja`). The grep deliberately allows _„hámarksdagsekt"_, _„hámarkshraði"_, _„hámarksfjárhæð"_ etc. because these are correct Icelandic uses of _„hámark"_ as a numeric-ceiling word, distinct from the legislative-technique concept the calque misappropriated.

For each failing check:

- (a) Read the relevant section against the failing finding,
- (b) **Edit the deliverable** to address it (not just the working files — the deliverable itself),
- (c) Re-run the three checks.

Repeat up to three iterations. If still failing after three, stop and flag the unresolved item in the final "Takmarkanir" section with the specific reason. Record every iteration as a one-line entry in `revisions/` (filename: `{ISO-timestamp}-{iter}.md`) stating `before → finding → after`.

A passing run produces an empty fourth iteration check — that is the signal to proceed to 9e. **Do not proceed to the language pass until all substantive checks pass** — polishing prose that may still change is wasted work.

**9e — Icelandic language / grammar pass (mandatory; last markdown-editing step).** Run the detailed prose, grammar, vocabulary, and internal-tooling sweep in `references/icelandic-guidelines.md` §9e. Substantive content is frozen by 9d; after this pass, the only remaining step is rendering to `.docx`.

**9f — Render the final `.docx` (last step).** Inputs: the frozen `Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.md`. Output: `Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.docx`. This step does not change content.

Renderer selection — prefer in this order:

**Typography (all renderers).** Compact, document-not-deck sizing:

| Element              | Point size | docx-js `size` (half-points) | Notes                |
| -------------------- | ---------- | ---------------------------- | -------------------- |
| Body / default       | **10pt**   | 20                           | Arial; tight leading |
| Heading 1            | **14pt**   | 28                           | bold                 |
| Heading 2            | **12pt**   | 24                           | bold                 |
| Heading 3            | **10pt**   | 20                           | bold                 |
| Heading 4            | **10pt**   | 20                           | bold italic          |
| Tables (cell text)   | **9pt**    | 18                           | one step below body  |
| Footnotes / captions | **8pt**    | 16                           |                      |

Page: US Letter or A4 with 1-inch (1440 DXA) margins. Line spacing: single. Paragraph spacing: 0pt before, 6pt after. Heading paragraph spacing: 12pt before, 4pt after.

Renderer selection — prefer in this order:

**Standalone-document requirement (mandatory; precedes renderer selection).** The `.docx` must be fully **self-contained** — opening it in Word, LibreOffice, or Pages must produce **zero** prompts about updating fields, missing templates, or external file references. The deliverable is a legal document filed with Alþingi committees, ESA, or regulated clients; a prompt like _"This document contains links that may refer to other files. Do you want to update this document with the data from the linked files?"_ signals to the reader that the document is not a finished product. Three concrete consequences for the renderer:

1. **No TOC field codes.** Word's `{ TOC \o ... }` field is the most common cause of the prompt — it asks Word to recompute the TOC against current headings on every open. **The skill produces a static, handwritten _Efnisyfirlit_ in the markdown source instead.** Insert it after the opening blurb and before §0 Samantekt as a plain bulleted list of section anchors. The TOC ships as ordinary prose; Word never asks to update it. Concrete consequence for pandoc: **do not pass `--toc`**.
2. **No `attachedTemplate` reference.** Pandoc's `--reference-doc=…` does _not_ by default insert `<w:attachedTemplate>` into `word/settings.xml`, but third-party templates and some Word workflows do. The post-render audit greps `word/settings.xml` for the string `attachedTemplate` — a hit is a hard fail; strip the element from `word/settings.xml` and re-zip before delivery.
3. **No external relationships.** `word/_rels/document.xml.rels` must contain zero `TargetMode="External"` entries pointing to local file paths (URLs to public dómafordæmi or þingskjöl on althingi.is are fine; relative file-system paths or `file://` URLs are not). The audit greps for `TargetMode="External"` and inspects each hit; only `http://` / `https://` targets to public public-record URLs are permitted.

Renderer selection — prefer in this order:

1. **Anthropic `docx` skill (`anthropic-skills:docx`) — preferred when available.** Invoke it via the Skill tool with this brief, verbatim: *"Convert `<absolute path to .md>` to `<absolute path to .docx>`. Use Arial as default font. Sizes: body 10pt (size: 20), Heading 1 14pt (size: 28, bold), Heading 2 12pt (size: 24, bold), Heading 3 10pt (size: 20, bold), table cell text 9pt (size: 18), footnotes 8pt (size: 16). US Letter, 1-inch margins. Paragraph spacing 0pt before / 6pt after; heading spacing 12pt before / 4pt after. Override built-in Heading1/Heading2/Heading3 styles with these exact sizes. \*\*Do NOT insert a Table of Contents field code — the markdown source already contains a static handwritten *Efnisyfirlit* section that should be rendered as ordinary headings and bullets.\*\* The output must be fully self-contained: no TOC fields, no attachedTemplate, no external relationships. Validate the output."* The skill handles heading-style overrides, bullet lists with `LevelFormat.BULLET`, table dual-width discipline, smart quotes, and runs its own validator.
2. **`pandoc` fallback** — typography requires a reference document; pandoc CLI flags do not control sizes on their own.
   ```bash
   # one-time setup: create reference-is.docx with the typography above; then reuse it.
   # NOTE: --toc is intentionally OMITTED. The markdown already contains a static Efnisyfirlit.
   pandoc -f gfm+smart -t docx \
     --metadata title="Gullhúðunarskýrsla — lög nr. {NN}/{YYYY}" \
     --metadata lang=is \
     --reference-doc=templates/reference-is.docx \
     -o "Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.docx" \
     "Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.md"
   ```
   If `templates/reference-is.docx` does not yet exist, generate it once with python-docx (see fallback 3), then reuse it.
3. **`python3` + `python-docx` final fallback** — set sizes explicitly:
   ```python
   from docx import Document
   from docx.shared import Pt, Inches
   doc = Document()
   styles = doc.styles
   styles["Normal"].font.name = "Arial"
   styles["Normal"].font.size = Pt(10)
   for name, size in [("Heading 1", 14), ("Heading 2", 12), ("Heading 3", 10), ("Heading 4", 10)]:
       styles[name].font.name = "Arial"
       styles[name].font.size = Pt(size)
       styles[name].font.bold = True
   # tables: set cell paragraph font to Pt(9) per cell after creation.
   for section in doc.sections:
       section.top_margin = section.bottom_margin = section.left_margin = section.right_margin = Inches(1)
   ```
   No tracked-changes / comments needed for this deliverable.

**Table borders (mandatory post-render step).** Pandoc renders markdown tables with no visible borders by default — every `<w:tbl>` inherits the bare _„Table"_ style and the result on screen is a grid of text floating without separators. The skill's deliverables routinely contain 10–20 tables (the metadata block, §0.5 verbatim-comparison, §1.1 lagaferill, §2 samræmingarkort, §3.0 yfirlitstafla, §3.{N}.5 reit-fyrir-reit greining for each finding, §6 self-assessment changelog, and the frumvarp's samanburðartafla). Without horizontal row separators these tables visually fuse and force the reader to count cells line-by-line.

Inject a thin (0.5pt, soft grey #999999) **top + bottom + insideH** border into every `<w:tbl>` after pandoc renders. **Left, right, and insideV are intentionally left blank** — only horizontal rules between rows are needed; vertical lines would over-decorate a legal document. Idempotent post-processing:

```python
# add-table-borders.py — run on every rendered .docx in Stage 9f and 10f.
import re, shutil, sys, tempfile, zipfile
from pathlib import Path

BORDER_XML = (
    '<w:tblBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    '<w:left w:val="nil"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    '<w:right w:val="nil"/>'
    '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    '<w:insideV w:val="nil"/>'
    '</w:tblBorders>'
)
TBLPR = re.compile(r'(<w:tblPr>(?:(?!</w:tblPr>).)*?)(</w:tblPr>)', re.DOTALL)

def inject(m):
    body, close = m.group(1), m.group(2)
    return m.group(0) if 'tblBorders' in body else body + BORDER_XML + close

in_path = Path(sys.argv[1])
out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else in_path
with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
    tmp_path = Path(tmp.name)
with zipfile.ZipFile(in_path, 'r') as zin, zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.namelist():
        data = zin.read(item)
        if item == 'word/document.xml':
            data = TBLPR.sub(inject, data.decode('utf-8')).encode('utf-8')
        zout.writestr(item, data)
shutil.move(str(tmp_path), str(out_path))
```

Run as `python3 add-table-borders.py <output.docx>`. Verify with `unzip -p <output.docx> word/document.xml | grep -c 'tblBorders'` — the count must equal the number of `<w:tbl>` elements (every table gets borders). Idempotent — re-running on a document that already has borders is a no-op.

If the Anthropic `docx` skill was used, append to the brief: _"Every table must have a thin (0.5pt) horizontal line between rows and on the top and bottom edge of the table. Left, right, and inside-vertical borders must remain blank. Color #999999."_ The skill's renderer applies that as a Table style override and the post-render helper above is not required.

Post-render checks (all renderers):

1. `test -s "$OUTPUT.docx"` — file exists and is non-zero.
2. `unzip -l "$OUTPUT.docx" | grep -q word/document.xml` — it is a valid ZIP / OOXML container.
3. If the docx skill was used, its `scripts/office/validate.py` already ran; record the result.
4. Open the `.docx` once with `pandoc -f docx -t plain "$OUTPUT.docx" | head -40` and confirm Icelandic characters survive (þ, ð, æ, ö visible). If any are mangled, the renderer is misconfigured — re-run with explicit `--metadata lang=is` for pandoc or `lang="is-IS"` style for python-docx.
5. **Table-border audit (mandatory).** Every `<w:tbl>` must have a `tblBorders` element. Run:

   ```bash
   F="$OUTPUT.docx"
   TBLS=$(unzip -p "$F" word/document.xml | grep -oc '<w:tbl>')
   BORDS=$(unzip -p "$F" word/document.xml | grep -oc 'tblBorders')
   [ "$TBLS" = "$BORDS" ] && echo "✓ borders on all $TBLS tables" || echo "✗ $BORDS/$TBLS tables have borders"
   ```

   A mismatch is a hard fail — re-run the post-render helper before delivery.

6. **Standalone-document audit (mandatory)** — the deliverable must produce **zero prompts** when opened in Word, LibreOffice, or Pages. Run the following grep gauntlet against the .docx:

   ```bash
   # Each of these must return 0. A non-zero count is a hard fail.
   F=Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.docx
   echo "instrText  (TOC/REF/HYPERLINK field code body):  $(unzip -p "$F" word/document.xml | grep -oc '<w:instrText')"
   echo "fldChar    (field begin/end markers):            $(unzip -p "$F" word/document.xml | grep -oc '<w:fldChar')"
   echo "fldSimple  (simple field code):                  $(unzip -p "$F" word/document.xml | grep -oc '<w:fldSimple')"
   echo "extern rel (file-system or template links):      $(unzip -p "$F" word/_rels/document.xml.rels | grep -oE 'TargetMode=\"External\"[^>]*Target=\"(file:|[A-Za-z]:|\\.)' | wc -l)"
   echo "attachedTpl (linked template — Word prompt):     $(unzip -p "$F" word/settings.xml | grep -oc 'attachedTemplate')"
   echo "linkStyles  (linked-styles — auto-update prompt):$(unzip -p "$F" word/settings.xml | grep -oc 'linkStyles[^/]*/>')"
   ```

   `http://` / `https://` external relationships (e.g. clickable links to althingi.is þingskjöl) are permitted because they do not trigger an open-time update prompt; only file-system or `file://` external targets do. **If any check returns non-zero, repair the docx before delivery**, either by re-rendering without the offending feature or by post-processing:
   - **TOC field hits**: ensure the markdown contains a static handwritten _Efnisyfirlit_ section, and that pandoc was invoked **without** `--toc`. Re-render.
   - **`attachedTemplate` hit**: unzip, edit `word/settings.xml` to remove the `<w:attachedTemplate r:id="..."/>` element, re-zip with `zip -j` (preserving the original mimetype-first ordering with `zip -X`).
   - **`linkStyles` hit**: edit `word/settings.xml` to remove the `<w:linkStyles/>` element.
   - **file-system external relationships**: convert the link to a public URL or remove it.

7. Display the 3-sentence Icelandic samantekt in chat.

If 9f surfaces a typo, fix it in the markdown, re-render. Do not edit the `.docx` directly.

**Do not include in the report:**

- A "Not legal advice" / "Requires lawyer review" disclaimer. The reader is a lawyer.
- An AI-disclosure section. Provenance is implicit from the working directory and the skill name.
- A Glass Box / audit-trail YAML block. Coverage gaps and methodology limitations belong in a single technical "Takmarkanir" (Limitations) section, written as substantive bullets — not as a YAML self-audit.

---

### Stage 10 — Remediation Frumvarp Draft (conditional — runs when triggered)

**Trigger.** Stage 10 runs when _both_ of the following are true:

1. The Stage 0 ⟁ CLARIFY answer to "Produce a frumvarp draft?" resolved to _Yes_ (either by explicit user answer, by the Breytingartillaga purpose default, or by the comprehensiveness-signal default — see Stage 0).
2. Stage 9 produced at least one finding at severity 🟠 HIGH or 🔴 CRITICAL that survived the Stage 8 counter-argument stress test.

When both conditions are met, the skill produces a full Icelandic _breytingafrumvarp_ (amending bill) that remediates the surviving findings by bringing the act into line with the underlying EU/EEA instrument.

**The frumvarp is the natural pair of the skýrsla, not an extra.** The skýrsla diagnoses; the frumvarp remediates. Both ship as separate deliverables. When the user asks for a comprehensive review of an Icelandic implementing act — _"full scope"_, _"long-running"_, _"complete audit"_, or equivalent — they are asking for _both_. Producing only the skýrsla in that case is an orchestrator defect, not a feature of caution. See the Stage 0 default-selection rules.

**If Stage 10 was skipped at first run and the user asks for the frumvarp afterward**, do not re-run the whole pipeline. The frumvarp depends only on the surviving HIGH/CRITICAL findings from the existing skýrsla — substages 10a → 10f can be executed cleanly against the existing register, the article blocks, the forensic blocks, the stress blocks, and the impact summary that the skýrsla left behind in the working directory.

**Reference.** Canonical structure, mandatory greinargerð kafla, standard amendment-text formulations, samanburðartafla format, and Icelandic style/form rules are in `references/frumvarp-structure.md`. Template skeleton: `templates/frumvarp.md`. Read both before starting Stage 10a.

#### Substage flow

The flow mirrors Stage 9: all substantive work happens against the Markdown file, the grammar pass is the last Markdown step, and the `.docx` is rendered last from a frozen Markdown.

| #   | Substage                                                   | What it edits           | Format   |
| --- | ---------------------------------------------------------- | ----------------------- | -------- |
| 10a | Map findings → amendments                                  | new file                | markdown |
| 10b | Draft the frumvarp                                         | substantive content     | markdown |
| 10c | Verifier edit-on-fail loop                                 | substantive content     | markdown |
| 10d | Samanburðartafla completeness check                        | substantive content     | markdown |
| 10e | Icelandic language / grammar pass — **last markdown step** | prose / vocabulary only | markdown |
| 10f | Render `.docx` (no further content edits)                  | new file                | docx     |

**10a — Map findings → amendments.** Read `Gullhúðunarskýrsla-{lög}-{ISO-dagsetning}.md`. For every finding at severity HIGH or CRITICAL that survived Stage 8 (column "Final severity" in template §6 (Sjálfsprófun) is not `removed`), choose the remediation operation:

| Finding type                                                    | Remediation operation                                                     | Standard amendment formulation (see `references/frumvarp-structure.md` §3.2)                        |
| --------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Pattern G30 / heimasmíðuð (no GDPR counterpart)                 | Delete the article entirely                                               | `X. gr. laganna fellur brott.`                                                                      |
| Davidson-3 — criminal sanction beyond GDPR Art. 84 discretion   | Strip the criminal-sanction clause; retain administrative-sanction regime | `Eftirfarandi breytingar verða á X. gr. laganna: a. 1. mgr. orðast svo: … b. 2. mgr. fellur brott.` |
| Davidson-2 — declined derogation reinstated                     | Reinsert the GDPR-permitted exemption                                     | `Á eftir 1. mgr. X. gr. laganna kemur ný málsgrein, svohljóðandi: …`                                |
| Davidson-1 — over-broad scope / lowered threshold               | Narrow back to GDPR scope                                                 | `Í stað orðanna „{old}" í 1. mgr. X. gr. laganna kemur: „{new}"`                                    |
| Under-implementation (e.g., 51. gr. — _fjárhagslegt tjón_ only) | Broaden to full GDPR scope                                                | `Í stað orðsins „fjárhagslegt" í 1. mgr. 51. gr. laganna kemur: „fjárhagslegt eða ófjárhagslegt"`   |

Write `frumvarp-mapping.md` — one row per surviving finding: `finding ID | severity | Davidson cat | Pattern | proposed amendment | controlling GDPR/CJEU authority`. This is the worklist for Stage 10b. Every HIGH/CRITICAL surviving finding must produce at least one amendment row.

**10b — Draft the frumvarp.** Populate `templates/frumvarp.md` into `Frumvarp-{lög}-{ISO-dagsetning}.md`. Follow the canonical structure precisely:

1. Heiti og flutningsmaður
2. I. KAFLI — amending articles (one per amendment from 10a) plus the closing gildistökuákvæði
3. Greinargerð — all six mandatory kafla (Inngangur / Tilefni og nauðsyn / Meginefni / Samræmi við stjórnarskrá og alþjóðlegar skuldbindingar / Samráð / Mat á áhrifum)
4. Athugasemdir við einstakar greinar frumvarpsins — one block per article of the bill, each citing its driving Stage 9 finding ID **and** the controlling GDPR / CJEU / EFTA Court authority
5. Fylgiskjal — Samanburðartafla

**10c — Verifier edit-on-fail loop** (same discipline as 9d). Three checks:

1. **Mapping completeness** — every surviving HIGH/CRITICAL finding in the Stage 9 self-assessment changelog is referenced in `frumvarp-mapping.md` and has at least one amending article in the bill. `grep -L "finding {finding-id}" Frumvarp-*.md` returns no missed finding IDs.
2. **Authority anchor** — every athugasemd at "Um {N}. gr." cites both a finding ID and a specific GDPR/directive article (or names it as a Pattern G30 deletion). `grep -L "reglugerðarinnar\|tilskipunarinnar\|Pattern G30" Frumvarp-*.md` returns no orphan athugasemd blocks.
3. **No ungrounded amendments** — `grep -nE "\\[UNGROUNDED\\]|\\[VERIFY\\]" Frumvarp-*.md` returns no hits.

For each failing check: (a) read against the failing item, (b) edit the bill markdown, (c) re-run all three checks. Up to three iterations; record each in `revisions/` as `{ISO-timestamp}-frumvarp-{iter}.md`.

**10d — Samanburðartafla completeness check.** The annex table is the single most important supporting document for an EEA-compliance bill. Verify:

1. One row per amending article of the bill (excluding the gildistökuákvæði).
2. Column (a) `Núgildandi ákvæði` — verbatim quote from the in-force `sources/act/log-NN-YYYY-current.md`. `grep -F "{column a text}" sources/act/log-NN-YYYY-current.md` returns a hit for every row.
3. Column (b) `Tillaga frumvarpsins` — either verbatim new text or `fellur brott`.
4. Column (c) `Samsvarandi ákvæði reglugerðar (ESB) 2016/679 (EES-viðbætir)` — verbatim authentic Icelandic from the EES-viðbætir-embedded fylgiskjal of the existing act, **never re-translated from English**. For Pattern G30 / heimasmíðuð articles, column (c) is the literal string `engin samsvarandi grein í reglugerð`.

Any gap is a 10c re-trigger.

**10e — Icelandic language / grammar pass (mandatory; last markdown step).** Run `references/icelandic-guidelines.md` §10e, including the frumvarp-specific drafting-language checks and internal-tooling sweep.

After 10e the frumvarp markdown is final.

After 10e the frumvarp markdown is final. Do not edit the markdown after this step except to fix a typo a 10f docx-rendering check uncovers.

**10f — Render the final `.docx` (last step).** Inputs: the frozen `Frumvarp-{lög}-{ISO-dagsetning}.md`. Output: `Frumvarp-{lög}-{ISO-dagsetning}.docx`. Same renderer-selection priority, typography (body 10pt / H1 14pt / H2 12pt / H3 10pt / tables 9pt / Arial / 1-inch margins), and post-render checks as Stage 9f. The Anthropic `docx` skill is preferred; pandoc and python-docx are fallbacks. Do not edit the `.docx` directly — if 10f surfaces a typo, fix it in the markdown and re-render.

The chat reply at the end of Stage 10f summarises in two Icelandic sentences: (1) the number of amending articles and the act they amend, (2) the count of surviving HIGH/CRITICAL findings each amendment maps to.

#### Do not include in the frumvarp

- A "Not legal advice" / "Requires lawyer review" disclaimer.
- An AI-disclosure section.
- Empty kafla — every kafli in the greinargerð (1.–6.) must have substantive content. If 6.4 (sveitarfélögin) genuinely has no impact, say so in one sentence; do not leave the heading bare.
- Tracked changes inside the introduced bill text. Tracked changes belong to the Alþingi committee phase, not the introduced text.
- Speculative ESA / CJEU citations — only authorities actually retrieved in Stage 1 and used in Stage 9 may appear.

---

## External Tool Integration

The orchestrator uses the current Legalcode MCP Pro tools:

| Source class                                                                                  | Current tool path                                                                                                                        |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Icelandic lög / reglugerðir                                                                   | `legalcode_search` sourceTypes `["law"]`, jurisdiction `IS`; exact `lawKey` first                                                        |
| Icelandic pre-law (frumvörp, þingskjöl, umsagnir, nefndarálit, breytingartillögur, summaries) | `legalcode_trace` relationship `pre_law_for_law`, then `legalcode_fetch` flow metadata and nested `pre_law/.../documents/...` sourceRefs |
| Icelandic case law                                                                            | `legalcode_trace` relationship `cases_for_law` plus `legalcode_search` sourceTypes `["court_case"]` or `["case"]`                        |
| Icelandic regulatory guidance (FME / Persónuvernd / Stjórnarráðið)                            | `legalcode_search` sourceTypes `["guidance"]`, jurisdiction `IS`                                                                         |
| EU directives / regulations                                                                   | `legalcode_search` sourceTypes `["law"]`, jurisdiction `EU`, `mode: "exact"` for identifiers                                             |
| ECJ jurisprudence                                                                             | `legalcode_trace` cases-for-law where supported plus `legalcode_search` sourceTypes `["court_case"]` or `["case"]`                       |
| ESA decisions                                                                                 | `legalcode_search` sourceTypes `["guidance"]`, agency/ESA terms                                                                          |
| Trade / tax agreements                                                                        | `legalcode_search` sourceTypes `["agreement"]`                                                                                           |
| Cross-reference law ↔ case                                                                    | `legalcode_trace` relationships `cases_for_law` / `laws_for_case`                                                                        |
| Aggregate pre-law statistics                                                                  | `legalcode_analyze` sourceType `pre_law`, group/trend only, never for source retrieval                                                   |

**Genuinely-uncovered residual** (WebFetch only here):

| Residual                              | URL                                                                                                                         |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| EES-viðbætir authentic IS translation | `efta.int/sites/default/files/media/documents/legal-texts/eea/other-legal-documents/translated-acts/icelandic/i{CELEX}.pdf` |
| EEA Joint Committee Decisions         | `efta.int/legal-text/eea-agreement-1327`                                                                                    |
| Samráðsgátt pre-Alþingi consultation  | `island.is/samradsgatt/mal/{caseId}` or `samradapi.island.is/api/Documents/{GUID}`                                          |
| B-deild umræður speech transcripts    | `althingi.is/altext/{ltg}/raeda/...`                                                                                        |

Mark MCP-fetched citations VERIFIED-MCP; WebFetch citations VERIFIED-WEB. Degraded mode (no MCP): WebFetch all primary sources; mark all `[VERIFY]`, reduce confidence one level, tell user explicitly.

**Hard fallback rule.** If an MCP result is awkward or incomplete, do not jump straight to WebFetch. Retry in this order:

1. `legalcode_discover` source_profile / facets / help, to confirm the right field and shape.
2. Exact `legalcode_search` by identifier (`lawKey`, `caseNumber`, `flowKey`, CELEX) with `mode: "exact"`.
3. `legalcode_trace` when the question is relational (`cases_for_law`, `pre_law_for_law`, `laws_for_case`).
4. **Signed `downloadUrl` with `curl`** — this is the standard retrieval path for any document you intend to persist; every search/trace result already carries one.
5. `legalcode_fetch mode:"metadata"` for human-readable inspection of one record, or `mode:"excerpt"` with `q`/`sectionRef` for a targeted section read.
6. WebFetch for the genuinely residual sources listed above (EES-viðbætir PDFs, JCDs, samráðsgátt drög, B-deild umræður).

The MCP help mode's own workflow says it: "Use `downloadUrl` when available for full-document review of long laws/cases." Treat that as the rule, not an exception.

**Word-document rendering (Stage 9f).** The skill prefers Anthropic's bundled `anthropic-skills:docx` via the `Skill` tool when present in the runtime — it handles OOXML heading styles, `LevelFormat.BULLET` lists, table dual-width discipline, smart quotes, Icelandic character escaping, and runs its own validator. Anthropic's docx skill is **not vendored** into this repo (its LICENSE prohibits extraction, copying, and derivative works); we invoke it in-runtime instead. Fallback chain: `pandoc -f gfm+smart -t docx --metadata lang=is`; then `python3 + python-docx`. Post-render checks: non-zero file, valid ZIP container with `word/document.xml`, Icelandic characters (þ ð æ ö) survive a `pandoc -f docx -t plain` round-trip. See Stage 9f for the full procedure.

---

## Citation Quality Gates

Every citation passes all five:

| Gate           | Criterion                                                            |
| -------------- | -------------------------------------------------------------------- |
| **Source**     | Primary authority (lög, reglugerð, frumvarp, dómur, JCD)             |
| **Format**     | Icelandic adapted OSCOLA; pinpoint to article + paragraph            |
| **Currency**   | Confirmed in-force at date of analysis                               |
| **Domain**     | Right jurisdiction and source type (EES-viðbætir IS, not Lovdata NO) |
| **Confidence** | VERIFIED-MCP / VERIFIED-WEB / [VERIFY]                               |

---

## Anti-Patterns — Substantive Interpretive Traps

1. **EUR-Lex EN comparison instead of EES-viðbætir authentic Icelandic translation, or model-generated Icelandic instead of verbatim authentic translation** — translation choices themselves shift scope, and a quotation that is _generated_ rather than _retrieved_ is not a quotation. This anti-pattern has two failure modes:

   **(a) Comparing IS act against EUR-Lex English.** The comparison must be IS act vs the authentic Icelandic translation of the EU instrument; only after that may the EN text be cross-referenced. Translation choices already shift scope (e.g. _„eignatjón"_ in the IS GDPR rendering vs _„material damage"_ in EN — narrower in IS legal use), and a finding built on the EN baseline misclassifies translation-level divergences as legislative gold-plating.

   **(b) Generating an Icelandic-looking translation rather than quoting the verbatim authentic text.** Every Icelandic quotation of an EU instrument in the deliverable (§0.1 row, §3.{N}.2, §3.{N}.5, §4.{ID}.0) must be a _byte-for-byte retrieval_ from the authentic Icelandic source, not a paraphrase that "looks Icelandic". The authentic IS text is sourced, in this order:
   - **First**: the `Fylgiskjal` of the implementing Icelandic act if the EU instrument is incorporated as such (this is how GDPR Art. 1–99 is preserved in lög nr. 90/2018; analogous fylgiskjöl exist for many other EEA-incorporated regulations).
   - **Second**: the EES-viðbætir IS PDF from `efta.int/.../translated-acts/icelandic/i{CELEX}.pdf` for directives.
   - **Never**: the model generating fluent-looking Icelandic that approximates the EN. Even when the generated text is _substantively_ faithful, the specific _terms_ are choices made by the EEA-translation service (e.g. _„eignatjón eða óefnislegt tjón"_, not _„efnislegt eða ófjárhagslegt tjón"_; _„skaðabótum"_, not _„að fá tjónið bætt"_) and the lawyer reading the report depends on those exact words to ground subsequent argument.

   **Mandatory verification before drafting any verbatim IS quotation of an EU instrument**: locate the candidate quote in the authentic source file with a literal `grep -F "<quote>" <authentic-source-path>`. A non-zero exit status means the quote is generated — discard it and retrieve the actual text. This check is part of Stage 9c source-grounding pass and is repeated by Stage 9d verifier (`grep -nE "‚.*reglug" Gullhudunarskyrsla-*.md | while read line; do verify against fylgiskjal; done`). An un-grounded EU-instrument quote in Icelandic is a Stage 9d hard fail; a verbatim quote that does not appear in the authentic source is treated identically to an `[UNGROUNDED]` tag.

2. **Treating missing tilskipun citation in athugasemdir as proving no gold-plating** — it often proves silent gold-plating. The 2024 Einarsdóttir study found ~half of gold-plated bills did not disclose.
3. **Calling every divergence "unlawful"** — most gold-plating is lawful-but-reviewable (min-harm). Only max-harm divergence is unlawful.
4. **Stopping at "the greinargerð says…"** — athugasemdir is just the start. Check samráðsgátt drög, umsagnir, nefndarálit, umræður.
5. **Conflating gold-plating with non-conformity** — gold-plating = MORE than required; non-conformity = wrong implementation. ESA chases the latter.
6. **Treating ESA silence as proof of conformity** — ESA does not actively police over-implementation.
7. **Quoting from minister speeches without checking the transcript** — umræður transcripts drift; always cite B-deild Alþt. with date.
8. **Skipping comparator Nordic implementations when the user opted in** — if Norway transposed without gold-plating and Iceland did, that's a powerful finding.
9. **Using "skal" rendering "may" as a single-finding test** — run all 14 substeps.
10. **Reporting LOW findings without flagging stakeholder review need** — disclosed-justified may still be policy-wrong.
11. **Omitting samanburðartafla recommendation when bill lacks one** — post-Jan 2024 task-force compliance requires it.
12. **Asserting threshold gold-plating without checking the recital** — recitals sometimes explain MS-discretion.
13. **Treating EFTA Court silence on a directive as meaning ECJ jurisprudence does not apply** — Art. 6 EEA homogeneity.
14. **Citing umsagnir without confirming `receivedAt`** — late-filed umsagnir have less weight.
15. **Padding the report with disclaimers, AI-disclosure prologues, or audit-trail YAML.** The reader is a qualified lawyer; treat them as one. Substantive limitations belong in a brief "Takmarkanir" section. The skill name in the matter directory is sufficient provenance.
16. **Discussing findings or recommendations without anchoring them to the IS article and its GDPR pairing shape.** Every divergence claim in §3, §4, §5, and the executive summary must name (a) the IS article (`48. gr.`) **and** (b) one of: the GDPR/directive counterpart (`GDPR Art. 84`), the combined counterparts (`GDPR Art. 12–15 og 23`), or — for heimasmíðuð articles — the explicit phrase `engin samsvarandi grein í GDPR (Pattern G30 / heimasmíðuð)`. "Criminal sanctions exceed GDPR" without naming Art. 84 is non-compliant. "Rafræn vöktun er íþyngjandi" without flagging _heimasmíðuð / Pattern G30_ is equally non-compliant — the absence of a GDPR counterpart **is** the finding and must be stated. The lawyer reading the report must be able to verify the pairing — or its deliberate absence — in seconds, without re-deriving it.
17. **Leaking internal tooling, skill mechanics, or working-file paths into the deliverable.** The report and the frumvarp are standalone legal documents. They must contain zero references to MCP tool names (`legalcode_search`, `legalcode_trace`, `cases_for_law`, `flowKey`, `sourceRef`, `downloadUrl`), skill identifiers (`legalcode-anti-gold-plating-is`, `Legalcode`, `Anthropic`), internal stage numbers or labels (`Stage 8`, `§8 of the skill`, `samkvæmt verkferli`, `Iron Law 7`), agent terminology (`agent`, `orchestrator`, `subagent`, `tool call`, `MCP`), or working-directory paths (`sources/`, `articles/`, `forensics/`, `article-index.json`, `frumvarp-mapping.md`). These are implementation details that have no place in a legal reference document. Cite evidence by public reference — þingskjal number, ákvörðun nr., dómsmál nr., umsögn submitter + date — and describe methods by their substance (e.g. "mótrökspróf gegn niðurstöðunni") never by the internal label. Stage 9e and Stage 10e run a mandatory grep sweep to catch every variant; an unsanitised draft is unfit for delivery to Alþingi, Persónuvernd, or any external reader.
18. **Stating a mismatch without quoting both sides.** Every divergence claim must show the IS text and the GDPR/directive text side by side, as verbatim blockquotes drawn from primary sources (the in-force IS act for the IS side, the EES-viðbætir authentic Icelandic for the GDPR side, EUR-Lex English as a cross-reference where helpful). "47. gr. is stricter than GDPR Art. 84" alone is insufficient — the reader must be able to see the divergence in the text itself without going to the underlying acts. The §3.{N} per-article block is structured to enforce this; §4 forensic blocks and the executive summary must follow the same discipline.
19. **Reporting a HIGH/CRITICAL finding without checking whether IS courts or Persónuvernd have engaged the gold-plated wording.** Every HIGH/CRITICAL finding must include an in-country impact check (Stage 6.2) classifying the wording into one of five buckets: _Applied as written_, _Read past via EEA-conform interpretation_, _Judicially acknowledged_, _Routed around_, or _No documented impact yet_. The impact bucket is recorded in template §3.{N}.11 and surfaced in the §0 executive summary's _Áhrif í framkvæmd_ column. A finding where a court has named and bypassed the divergence (e.g., Landsréttur 312/2025 on 51. gr. lög 90/2018 vs 82. gr. GDPR) is materially stronger than a theoretical finding; a finding where a court has merely _named_ the divergence without resolving it on the facts is _also_ strong evidence and must be flagged; a finding where the gold-plating has produced no friction in 7+ years carries less weight and may warrant a confidence reduction. _No documented impact yet_ is an acceptable answer — _no impact check performed_ is not.
20. **Using all-caps severity labels (`ALVARLEG`, `HÁ`, `MIÐLUNGS`, `LÁG`) as visual tokens in tables, headings, or assertions.** Severity is communicated by the colored circle alone — `🔴`, `🟠`, `🟡`, `🟢`. The all-caps words crowd table cells, dominate the reading order, and look like rubber stamps that pull attention away from the actual finding text. The legend in §0 _Heildarfjöldi niðurstaðna_ defines the colors once (_„9: 🔴 1 alvarleg — 🟠 4 háar — 🟡 3 miðlungs — 🟢 1 lág"_) and the symbol carries the meaning from then on. Wherever the severity is the _subject_ of a sentence in running prose, use the sentence-case Icelandic word (_„niðurstaðan er alvarleg"_, _„flokkast sem miðlungs"_) — never the all-caps version. Stage 9d enforces this with a grep check; a hit is a hard fail and must be edited to a circle (or to sentence-case prose) before delivery. The confidence vocabulary (Mikill / Hár / Líklegur / Mögulegur / Ólíklegur) is sentence-case throughout — no caps, no symbols.
21. **Using English-calque terminology for the harmonisation classification.** The §2 samræmingarkort and per-article blocks must use the preferred Icelandic legal vocabulary — _„ófrávíkjanlegt"_, _„lágmarksviðmið"_, _„blandað"_, _„svigrúmsákvæði"_, _„svigrúm aðildarríkja"_ — not literal translations of the EU-English jargon. Four calques specifically are forbidden:

    **(a) _„hámark"_ standalone for _maximum harmonisation_.** In Icelandic _hámark_ denotes a numeric ceiling (_hámarkshraði_, _hámarksdagsekt_, _hámarksfjárhæð_). Using it as a legislative-technique label confuses a quantitative limit with a regulatory-philosophy concept and reads to a native speaker as a literal calque of EU-English _„maximum"_. The legally precise term is **„ófrávíkjanlegt"** (cannot be deviated from) — a well-established Icelandic legal adjective. _„Fullsamræming"_ or _„tæmandi samræming"_ are acceptable in scholarly prose; _„hámarkssamræming"_ is borderline-acceptable in academic writing but should not appear in a table cell.

    **(b) _„lágmark"_ standalone for _minimum harmonisation_.** Same problem in mirror: _„lágmark"_ in Icelandic usually means a numeric floor. The preferred term in tables and headlines is **„lágmarksviðmið"** (minimum benchmark); _„lágmarkssamræming"_ is fine in scholarly prose.

    **(c) _„sveigjanleikaklausa"_ for _flexibility clause_.** A direct calque from EU-English. The established Icelandic legal term is **„svigrúmsákvæði"** — the clause within an otherwise binding rule that opens a defined area of MS discretion (GDPR Art. 6(2)/(3), Art. 23, Art. 84).

    **(d) _„MS-svigrúm"_ as Anglo-IS hybrid.** Use **„svigrúm aðildarríkja"** in full. _MS-_ prefix is a working-document shortcut, not finished legal prose.

    Stage 9d eftirlit nr. 8 runs a grep over the deliverable for these calques; a hit is a hard fail. The legal rationale matters: a reader who sees _„ófrávíkjanlegt"_ immediately understands that divergence is unlawful (max-harm doctrine), while _„hámark"_ invites the misreading that the EU rule sets a _ceiling on burden_ (which is the opposite of what max-harm means). The choice of term is not stylistic — it carries the legal effect.

22. **Including a _Samsvörun_-column in the §3.0 yfirlitstafla that duplicates the _Grein gerðar_-column.** The pairing shape (einn-á-einn / einn-á-marga / margir-á-einn / heimasmíðuð) is _fully derivable_ from the _Grein gerðar_ cell — one article number = one-to-one, multiple = one-to-many, _„engin"_ = heimasmíðuð. Carrying both columns is dead weight that crowds the table, makes every row read like it lists the same fact twice, and trains the reader to skim past both columns. The §3.0 yfirlitstafla uses **five columns, not six**:

    `| IS-grein | Grein gerðar | Niðurstaða | Áreiðanleiki | Áhrif í framkvæmd |`

    Special cases are encoded inside _Grein gerðar_ directly:
    - Heimasmíðuð (Pattern G30) → _„engin — heimasmíðuð (G30)"_
    - Svigrúmsákvæði → _„Art. 84 (svigrúmsákvæði)"_
    - Ófrávíkjanleg grein where the legal effect is the point → _„Art. 82 (ófrávíkjanleg)"_
    - Innleiðingar-/réttarfars-/stjórnarskrár-regla → _„—"_ með merkimiða í sviga á eftir IS-greininni: _„2. gr. (innleiðingarregla)"_
    - Margir-á-einn → _„Art. 23 (skipt í 17.–19. gr.)"_ með krossvísun í sister-greinar

    The pairing-shape classification (one-to-one / one-to-many / many-to-one / none) still lives in `article-index.json` and is referenced from the §3.{N}.2 forensic blocks where the classification is load-bearing for the analysis. It does **not** belong in the §3.0 scannability table where the reader is looking for _which articles diverge_ and _how seriously_ — questions answered by _Grein gerðar_, _Niðurstaða_, and _Áhrif_, not by a redundant pairing label.

    Stage 9d adds a column-count check on the §3.0 yfirlitstafla — six columns is a hard fail; the column header must read `| IS-grein | Grein gerðar | Niðurstaða | Áreiðanleiki | Áhrif í framkvæmd |`.

23. **Shipping a `.docx` that is not fully self-contained.** The deliverable is a legal document filed with Alþingi committees, ESA, or external clients. **Opening it must produce zero update prompts.** Three specific failure modes are forbidden:

    **(a) Table of Contents field codes (`{ TOC \o ... }`).** When a `.docx` contains a Word TOC field, Word and LibreOffice both prompt _"This document contains fields that may refer to other files. Do you want to update them?"_ on every open. **The skill produces a static handwritten _Efnisyfirlit_ in the markdown source** (a plain bulleted list of section names) and renders it as ordinary text. The pandoc command **must not** pass `--toc`; the `anthropic-skills:docx` brief **must** instruct the renderer to skip TOC generation. The `Efnisyfirlit` markdown bullets render as a normal heading + bullet list — no field codes, no Word prompt.

    **(b) Linked-template references (`<w:attachedTemplate>`).** If `word/settings.xml` contains a `<w:attachedTemplate r:id="..."/>` element, Word displays _"This document is attached to a template that is missing"_ or silently tries to fetch the template. The reference doc used to set typography (e.g. `templates/reference-is.docx`) must not propagate into the output as an attached template. Verify by `unzip -p $OUTPUT word/settings.xml | grep attachedTemplate` — zero hits required.

    **(c) Local-filesystem external relationships.** `word/_rels/document.xml.rels` must contain zero `TargetMode="External"` entries pointing to `file://`, drive letters (`C:\...`), or relative paths. Hyperlinks to public web URLs (althingi.is þingskjöl, EUR-Lex, dómafordæmi on domstolar.is) are permitted because they don't trigger an open-time prompt. Verify by `unzip -p $OUTPUT word/_rels/document.xml.rels | grep -E 'TargetMode="External"[^>]*Target="(file:|[A-Z]:|\\.)'` — zero hits required.

    The Stage 9f post-render audit runs all three checks; a non-zero count is a hard fail. **Never deliver a `.docx` that has not passed the audit.** If a check fails, either re-render without the offending feature or post-process the OOXML directly (`unzip` → edit `word/settings.xml` or `word/_rels/document.xml.rels` → `zip -X` re-pack) before delivery. The reader of the report should never see _"this document is connected to another file"_ — that text alone tells them the document is not finished work product.

24. **Shipping a §0 Samantekt that is just a metadata table plus a 3-sentence blurb.** §0 is the _one-pager executive summary_ of a long report — the part that lawyers, committee members, and clients actually read before deciding whether to drill in. A bare metadata table plus _„Niðurstaða í þremur setningum"_ is not enough work to count as a summary; it leaves the reader without findings, effects, or remediations until §3, §5 and §6, which is too late for an executive reader. **§0 must contain five substantive subsections in this fixed order, each one substantive prose (not just tables):**
    - **§0.1 — Niðurstaða í hnotskurn**: 250–400 orða narrative in two-to-three efnisgreinar (heildarmynd, sterkasta niðurstaða, afgangur). Not a single sentence; not a bullet list.
    - **§0.2 — Helstu niðurstöður í samhengi**: 300–600 orða narrative grouping the findings by málefnasvið (bótaréttur, viðurlög, leyfiskerfi, gildissvið o.fl.), each finding named by its ID (F01, F02…) and severity circle.
    - **§0.3 — Áhrif í framkvæmd**: 250–400 orða narrative summarising the Stage 6.2 impact buckets — _which findings have been litigated, which have been túlkað fram hjá by an EES-conform reading, which sit dormant_. Name the leading cases by number.
    - **§0.4 — Tillögur í hnotskurn**: 200–350 orða summary of §5 organised into Flokkur 1 / 2 / 3, with a closing sentence pointing at the companion frumvarp when Stage 10 ran.
    - **§0.5 — Yfirlit niðurstaðna**: the verbatim-comparison table previously called §0.1.

    The metadata table at the top of §0 and the three-line headline summary still stand, but they are followed by §0.1–§0.5 as a _real_ executive overview. **A reader who reads only §0 should know what the law does, what is gold-plated, what has bitten in practice, what to fix, and that a remediation bill is on the table.** Stage 9d adds a soft check: §0.1 + §0.2 + §0.3 + §0.4 together should be ≥ 1000 words. Falling short means §0 has been stamped out of a template rather than written.

25. **Shipping a `.docx` whose tables have no visible borders between rows.** Pandoc renders markdown tables with no `tblBorders` element by default, which means the reader sees rows of text floating in white space with no horizontal line separating them. In a long legal report with 10–20 tables — the §0 metadata block, the §0.5 verbatim-comparison, the §1.1 lagaferill block, the §2 samræmingarkort, the §3.0 yfirlitstafla over all articles, the §3.{N}.5 reit-fyrir-reit greining for each finding, the §6 self-assessment changelog, and the frumvarp's samanburðartafla — borderless rendering forces the reader to count cells across each line and produces a visually unprofessional document. **Every `<w:tbl>` in the delivered `.docx` must carry a `tblBorders` element with at minimum a thin (0.5pt, soft grey `#999999`) horizontal line between rows (`w:insideH`) and on the top and bottom edges of the table (`w:top` / `w:bottom`). Left, right, and inside-vertical borders must remain blank** — only horizontal rules between rows are needed; vertical lines would crowd the cells and over-decorate the document. The Stage 9f / 10f post-render helper `add-table-borders.py` injects these into every table that lacks them; the table-border audit (post-render check #5) hard-fails if `tblBorders` count ≠ `<w:tbl>` count. A borderless table in a delivered legal document signals to the reader that the file was generated rather than authored.

26. **Running Stage 6.2 impact bucketing against a broad-corpus pull instead of finding-targeted retrieval.** The original skill suggested a `grep` over the Stage-1 case corpus to classify each finding into the five impact buckets (Applied as written / Read past / Judicially acknowledged / Routed around / No documented impact yet). That workflow has a deep flaw: `grep` cannot find a case the orchestrator did not download, and the Stage-1 broad pull is ranked by _„all cases citing this law"_ — which is not the same ranking as _„cases that engage with this specific gold-plated article"_. In practice the headline case for any given CRITICAL finding (e.g. Landsréttur 312/2025 for 51. gr. lög 90/2018) is often outside the top-N of the broad pull and is reachable only by a phrase-targeted MCP query against the finding's exact verbatim wording. **Stage 5.5 — Per-Finding Impact-Corpus Retrieval — exists precisely to close this gap.** For every HIGH/CRITICAL finding (and the strongest 🟡), run the five Stage-5.5 query patterns (article-citation, cross-article comparison, verbatim-phrase, supervisory-authority decisions, EU/ECJ counterpart) and store results in `sources/is-case-law/_by-finding/{F##}/` and `sources/is-guidance/_by-finding/{F##}/`. Stage 6.2 then classifies the impact from that targeted corpus. **A Stage 6.2 bucket assignment that is not backed by Stage 5.5 retrieval is an inference from silence, not evidence**: the absence of a hit in your broad sample does not mean _„no impact"_; it means you did not query for impact. Stage 8.5 should reject any _„Engin þekkt mál"_ entry whose Stage 5.5 query log is empty for the finding.

27. **Skipping Stage 10 when the user asked for "full scope" or another comprehensiveness signal.** The skill's default-No for the frumvarp question is conservative: it fires whenever the user's stated purpose is not literally _Breytingartillaga_. That conservatism is wrong whenever the user has indicated they want comprehensive work. The trigger signals are: _"full scope"_, _"comprehensive"_, _"complete"_, _"complete audit"_, _"everything"_, _"long-running"_, _"thorough"_, _"end-to-end"_, _„heildargreining"_, _„fullt umfang"_, _„heildstæð"_, or any equivalent — these mean **default to Yes on the frumvarp question** (subject to the Stage 8 HIGH/CRITICAL-survival precondition, which is met for nearly every Icelandic EEA-implementation act). The skýrsla and the frumvarp are _paired deliverables_ — the skýrsla diagnoses, the frumvarp remediates — and a comprehensiveness signal fairly implies both unless the user explicitly excludes the frumvarp. Producing only the skýrsla in that case forces the user to ask twice for work the skill is built to do in one pass, and is a defect of the orchestrator, not a feature of caution. The Stage 0 default-selection rules and the ⟁ CLARIFY Convention now spell this out; failure to apply them when running in Auto Mode is the specific anti-pattern this rule names. If you find yourself about to deliver only the skýrsla after a "full scope" request, stop and run Stage 10 against the existing register before signing off.

---

## Writing Standards

- **Language**: Icelandic for report body (English glosses for EU technical terms on first occurrence). Switch only if user explicitly requests English.
- **Voice**: analytic and dispassionate. No "shockingly" / "egregiously". Facts and citations carry the argument.
- **Discipline**: one idea per sentence. Cite always; never assert from memory. Use "skv. þskj. NNNN" inline.
- **Per finding**: state (1) what diverged, (2) how, (3) where it came from, (4) what to do.

---

## Output Format

Report structure (`templates/findings-report.md`):

0. **Samantekt** — metadata-tafla, niðurstaða í þremur setningum, §0.1 Yfirlit niðurstaðna (verbatim samanburður + áhrif í framkvæmd)
1. **Bakgrunnur og lagaferill** — þingleg gögn, EES-samhengi, reglur um tilgreiningu frávika
2. **Samræmingarkort** — greinar gerðarinnar á móti íslenskum greinum, með svigrúmi og niðurstöðu
3. **Greining fyrir hverja grein** — §3.0 opnunarrölunarhjálp; §3.{N} ítarleg blokk fyrir hverja grein (stutt form fyrir engin frávik, fullt form með 11 undirreitum þegar frávik finnast). §3.{N}.11 inniheldur áhrifaflokk í framkvæmd.
4. **Heimildarrakning lagaferils** — fyrir HIGH/CRITICAL niðurstöður: lagaferill, umsagnir, nefndarálit, umræður, krosstékk (4.{ID}.9), áhrifa-samantekt (4.{ID}.10)
5. **Tillögur** — Flokkur 1 / 2 / 3, hver tillaga vísar í [Niðurstöðu {ID}], auk skilyrtra verklags- og samráðstillagna
6. **Sjálfsprófun fyrir háar og alvarlegar niðurstöður** — skyldubundin tafla, þrjár umferðir endurskoðunar
7. **Takmarkanir greiningarinnar** — efnislegar takmarkanir (sóttu ekki tilteknar heimildir o.s.frv.); ekki almenn boilerplate-fyrirvari
8. **Tilvitnanir og heimildir** — íslenskar heimildir; ESB og EES-heimildir; fræðirit og umsagnir

**Hvað skal EKKI vera í skýrslunni:**

- "Ekki lögfræðiráðgjöf" / "Krefst yfirferðar lögmanns" fyrirvari. Lesandinn er lögmaður.
- Yfirlýsing um aðstoð gervigreindar. Heitir möppunnar og verkfærisins gefa þetta til kynna.
- Glerkassi / YAML-endurskoðunarslóð. Tölfræði um MCP-kall og líkanið er ekki áhugaverð fyrir lesandann.

**Hvað skal EKKI vera í `.docx`-skjalinu:**

- TOC-svæði (Word „field code" `{ TOC \\o ... }`). Ef Word birtir gluggann _„Þetta skjal inniheldur svæði sem geta vísað í aðrar skrár. Viltu uppfæra þau?"_ þegar skjalið er opnað er það kunngerning um að skjalið sé ófullbúið. Skýrslan inniheldur í staðinn handsmíðað **Efnisyfirlit** í markdown-frumskjalinu sem birtist sem venjulegir punktalistar — engin svæði, engin uppfærsluvíxla.
- Tengd sniðmát (`<w:attachedTemplate>` í `word/settings.xml`). Word leitar að sniðmátinu á harða diskinum og varar notandann ef það finnst ekki.
- Skráarkerfistilvísanir í `word/_rels/document.xml.rels` (`TargetMode="External"` með `file://`, drifstaf eða venslapunkti). Almennar veftengingar (althingi.is, EUR-Lex, domstolar.is) eru í lagi vegna þess að þær valda ekki opnunaruppfærslugluggi.

---

## Provenance

- **Created**: 2026-05-24
- **Architecture**: Monolithic orchestrator. The skill executes every stage inline using current Legalcode MCP Pro tools (`legalcode_discover`, `legalcode_search`, `legalcode_fetch`, `legalcode_trace`, `legalcode_analyze`) plus Write, Read, tightly scoped WebFetch, and shell helpers for file conversion. No sub-agent delegation — sub-agents can't reliably be granted MCP and Write access in this environment, so the orchestrator owns the full pipeline.
- **Research basis**: two parallel research agents (gold-plating doctrine + Althingi pre-law materials); Davidson Review (HMSO 2006); Better Regulation Toolbox (2023/2025); Squintani (CUP 2019); utanríkisráðuneytið task-force report (31 May 2024); Einarsdóttir Jan 2024 systemic study; current Legalcode MCP unified tool schema
- **Model**: claude-opus-4-7
- **Quality bar**: 15 substantive anti-patterns; Iron Law 7 (counter-argument stress test) enforced for every HIGH/CRITICAL finding
- **Confidence**: HIGH — doctrinal reference deep, MCP integration concrete, pre-law tracing protocol exhaustive
- **Limitations** (the four MCP coverage gaps):
  - EES-viðbætir authentic Icelandic translations of directives
  - EEA Joint Committee Decisions and EFTA-specific adaptations
  - Samráðsgátt pre-Alþingi consultation (áform, drög, samráðsgátt umsagnir)
  - B-deild umræður speech transcripts
- **Future variants**: `legalcode-anti-gold-plating-no` (Norway), `-li` (Liechtenstein), `-eu-comparative` (multi-MS comparator)

---

**End of SKILL.md.**
