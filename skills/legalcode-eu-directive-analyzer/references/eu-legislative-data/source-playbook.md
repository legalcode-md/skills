# Source Playbook — Cellar, EUR-Lex, N-Lex, OEIL, CURIA, EEA-Lex, IATE, National Parliaments

This playbook is the operational reference for every data source the seven-skill EU
Legislative Compliance suite queries. Every fact emitted by the suite — an obligation,
a transposition deadline, a NIM citation, an infringement reference number, an EEA
Joint Committee Decision date — must trace to one of the sources below. When a
Legalcode MCP `search_laws`/`search_cases`/`search_guidance` call covers the source,
prefer the MCP path; when it does not, use the direct API or web service shape
described here. The coverage matrix at the end of this file lists which sources are
reachable through which path.

---

## 1. Cellar SPARQL endpoint

The Cellar is the Publications Office's RDF-native repository for the EU acquis,
EUR-Lex content, and the OJ. The public SPARQL endpoint is at:

```
https://publications.europa.eu/webapi/rdf/sparql
```

It speaks SPARQL 1.1 over HTTP GET (URL-encoded `query=` parameter) or POST
(`application/sparql-query` body). Default result format is XML; pass
`Accept: application/sparql-results+json` for JSON.

### 1.1 Worked queries

#### (a) All consolidated versions of a directive (NIS2)

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX dct: <http://purl.org/dc/terms/>
SELECT ?expression ?pointInTime ?language
WHERE {
  ?work cdm:work_id_document "32022L2555" .
  ?expression cdm:expression_belongs_to_work ?work ;
              cdm:expression_uses_language ?language ;
              cdm:expression_belongs_to_consolidated_version ?consolidated .
  OPTIONAL { ?expression cdm:expression_date_creation_legacy ?pointInTime . }
}
ORDER BY ?pointInTime ?language
```

This returns one row per (consolidated version × language). For an act that has
not been amended (NIS2 is unamended as of late 2025), the result is the same set
of Expressions as the original adoption. For an amended act (e.g. AMLD chained
amendments), it returns one Expression per consolidation point.

#### (b) All language versions of an act (AI Act)

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?language ?manifestation ?format
WHERE {
  ?work cdm:work_id_document "32024R1689" .
  ?expression cdm:expression_belongs_to_work ?work ;
              cdm:expression_uses_language ?language .
  ?manifestation cdm:manifestation_manifests_expression ?expression ;
                 cdm:manifestation_type ?format .
  FILTER(?format IN ("pdf", "xhtml", "akn4eu", "fmx4"))
}
ORDER BY ?language ?format
```

This returns one row per (language × format) pair, useful when the analyzer skill
needs to decide whether an AKN4EU Manifestation exists (it does not for every act —
AKN4EU coverage is rolling out act-by-act).

#### (c) All NIMs notified for a given directive (CSRD)

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX dct: <http://purl.org/dc/terms/>
SELECT ?nim ?nimCelex ?member_state ?nimTitle
WHERE {
  ?directive cdm:work_id_document "32022L2464" .
  ?nim cdm:resource_legal_implements_resource_legal ?directive ;
       cdm:work_id_document ?nimCelex ;
       cdm:resource_legal_based_on_concept_country ?member_state ;
       dct:title ?nimTitle .
}
ORDER BY ?member_state
```

Sector 7 is the CELEX sector for NIMs. The result is the canonical Commission-side
record of national notifications — but note that the Cellar reflects what MS have
notified, not what is actually in force or fully transposed. Use N-Lex (§ 3) and
the published transposition trackers (§ 9) to cross-check.

#### (d) All CJEU cases citing a given act (GDPR)

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?case ?caseECLI ?date ?subject
WHERE {
  ?act cdm:work_id_document "32016R0679" .
  ?case cdm:case-law_cites_resource_legal ?act ;
        cdm:work_ecli ?caseECLI ;
        cdm:resource_legal_date_signature ?date .
  OPTIONAL { ?case cdm:case-law_subject_matter ?subject . }
}
ORDER BY DESC(?date)
LIMIT 100
```

This is the entry point for the infringement-procedure-tracker skill: every CJEU
judgment that cites the GDPR shows up here, whether as the primary instrument
under examination or as an interpretive reference.

### 1.2 Practical notes

- The Cellar endpoint enforces a soft 60-second query timeout. For large traversals,
  paginate via `LIMIT`/`OFFSET` and never run unbounded `SELECT *`.
- HTTP 503 under load is common during business hours; back off and retry with
  exponential intervals starting at 5 seconds, capped at 5 minutes.
- The Cellar's vocabulary documentation lives at
  `https://op.europa.eu/o/opportal-service/euvoc-download-handler` (see the design
  brief link). Resolve unfamiliar predicates against the EuroVoc and CDM ontologies
  before using them in production queries.

---

## 2. EUR-Lex web service

EUR-Lex publishes a SOAP web service alongside the Cellar SPARQL endpoint. The
authoritative documentation is at
`https://eur-lex.europa.eu/content/help/data-reuse/webservice.html`.

- **Endpoint shape**: SOAP 1.1 over HTTPS at
  `https://eur-lex.europa.eu/EURLexWebService?wsdl`.
- **Authentication**: free, but registration-required. A username and password
  obtained from the EUR-Lex registration form is passed in the SOAP header
  (`<sec:UsernameToken>`). The credentials may be revoked for abuse; respect the
  rate limits.
- **Rate limits**: published as 1 request/second, 250 requests/day per credentialed
  user. Treat as a strict ceiling — production workloads should cache aggressively
  or fall back to the Cellar SPARQL endpoint, which has no per-user quota.
- **Common operations**: `doQuery` (CQL search over EUR-Lex metadata),
  `searchExpression` (search by ELI Expression). `doQuery` returns up to 100
  results per call; pagination via `<page>`.
- **When to prefer over Cellar**: full-text search across the OJ. The Cellar
  exposes structured metadata; the web service exposes the OJ full-text index.

---

## 3. N-Lex / MNE database

The Member States Notifications (MNE) database — surfaced through the N-Lex portal
at `https://eur-lex.europa.eu/collection/n-law/mne.html` — records every National
Implementing Measure that a Member State has notified to the Commission for a given
directive under the obligation in Art. 260(3) TFEU.

### 3.1 Structure

For each (MS × directive) pair, the MNE record contains:
- the directive CELEX,
- the MS country code,
- one or more NIMs (sector 7 CELEX) with national identifier (BGBl./JORF/etc.),
- the date of notification,
- the date of entry into force of the NIM,
- a Boolean `complete-transposition` flag (set by the MS, not verified by the
  Commission).

### 3.2 Query shape

The MNE database does not publish a documented public API. The sustainable path is
the Cellar SPARQL query in §1.1(c), which surfaces the same data through CDM. The
N-Lex web UI is useful for ad-hoc verification: it accepts a directive CELEX and
returns a per-MS table.

### 3.3 Caveats

The "complete-transposition" flag is self-declared and does not equal conformity.
The conformity-assessment skill must treat MNE as a *necessary-but-not-sufficient*
input: an MS that has not notified is presumptively in breach of Art. 260(3) TFEU
and exposed to first-referral penalties (the *Commission v Belgium* C-543/17,
ECLI:EU:C:2019:573 line of authority); an MS that has notified may still face an
Art. 258 TFEU action for non-conformity even though the notification box is ticked.

---

## 4. OEIL — Legislative Observatory

The Legislative Observatory at `https://oeil.europarl.europa.eu/oeil/` is the
European Parliament's structured database of every legislative procedure, going
back to the entry into force of the Treaty of Rome.

### 4.1 Procedural file structure

Every procedure has a unique reference of the form:

```
{year}/{sequential}({procedure-type})
```

- `{procedure-type}` codes:
  - `COD` — Ordinary legislative procedure (Art. 294 TFEU; co-decision).
  - `NLE` — Non-legislative consultation procedure.
  - `APP` — Consent procedure (Art. 218(6)(a) TFEU).
  - `RPS` — Regulatory procedure with scrutiny (legacy; pre-Lisbon comitology).
  - `INI` — Own-initiative report.
  - `IMM` — Immunity procedure.

Worked dossier numbers used in the suite:

- **NIS2**: `2020/0359(COD)` — proposed by the Commission on 16 December 2020 and
  adopted as Directive (EU) 2022/2555 on 14 December 2022.
- **AI Act**: `2021/0106(COD)` — proposed 21 April 2021, adopted as Regulation (EU)
  2024/1689 on 13 June 2024.
- **CSRD**: `2021/0104(COD)` — proposed 21 April 2021, adopted 14 December 2022.
- **CSDDD**: `2022/0051(COD)` — proposed 23 February 2022, adopted 13 June 2024.
- **DSA**: `2020/0361(COD)` — proposed 15 December 2020, adopted 19 October 2022.

### 4.2 Extractable data per dossier

For each procedural file, OEIL exposes:
- the rapporteur (lead MEP) and shadow rapporteurs,
- the lead committee and opinion-providing committees,
- every reading stage (first reading, second reading, conciliation),
- vote tallies at each plenary stage,
- the negotiating mandate dates,
- the political-group amendments tabled,
- the final OJ publication reference and adopted-text link.

### 4.3 Query path

OEIL provides a stable URL pattern:
`https://oeil.europarl.europa.eu/oeil/popups/ficheprocedure.do?reference={dossier}&l=en`

There is no public JSON API; the page emits structured HTML that the suite parses
when needed. The Cellar exposes most of the structured data via
`cdm:procedure_*` predicates; prefer the Cellar path.

---

## 5. CURIA / InfoCuria

CURIA at `https://curia.europa.eu/` is the Court of Justice of the European Union's
official portal; InfoCuria is its structured search interface.

### 5.1 Structured search dimensions

InfoCuria accepts queries on:
- **ECLI** — direct lookup of a specific decision.
- **Case number** — e.g. `C-543/17` resolves to *Commission v Belgium*.
- **CELEX of the contested act** — returns every case in which the act was the
  subject of a request for preliminary ruling, action for annulment, or
  infringement.
- **Procedure type** — `Action for failure to fulfil obligations` (Art. 258 TFEU),
  `Reference for a preliminary ruling` (Art. 267 TFEU), `Action for annulment`
  (Art. 263 TFEU), `Action for damages` (Art. 268 TFEU), `Appeal`.
- **Date range** — useful for producing a chronological infringement timeline.

### 5.2 Query shape

InfoCuria's URL parameters are stable but not officially documented as an API.
The pattern is:

```
https://curia.europa.eu/juris/documents.jsf?
  oqp=&for=&mat=or&jge=&td=%3BALL%3B%3BPUB1%3BORDER_DATE%3B&jur=C
  &etat=clot&pcs=Oor&num=C-543%2F17&parties=&dates=
```

Where `num=` accepts the case number (`/` URL-encoded as `%2F`), `jur=C` filters
to the Court of Justice, and `etat=clot` filters to closed proceedings.

The sustainable path for programmatic access is the Cellar SPARQL endpoint
(query §1.1(d)): every CURIA judgment is mirrored to the Cellar with full ECLI,
CELEX, and citation graph metadata.

---

## 6. EEA-Lex (EFTA Surveillance and EEA Joint Committee)

EEA-Lex at `https://www.efta.int/eealaw` is the EFTA Secretariat's portal for the
EEA pillar. The data the suite needs lives in three corpora.

### 6.1 EEA Joint Committee Decisions (JCDs)

Every EU act incorporated into the EEA Annexes is incorporated by a JCD adopted
under Art. 102 EEA. JCDs are sector-E CELEX. EEA-Lex publishes the JCD register
indexed by:
- the incorporated EU act CELEX,
- the JCD number and date,
- the EEA Annex affected (Annex I–XXII),
- IS/NO/LI constitutional reservation status under Art. 103 EEA,
- entry-into-force date in each EEA EFTA state.

For NIS2 (CELEX 32022L2555), as of late 2025 the JCD process is ongoing — the act
is marked EEA-relevant but has not yet been formally incorporated. The EEA EFTA
Comments document published by the Standing Committee at
`https://www.efta.int/sites/default/files/documents/eea/eea-efta-comments`
records the position taken by IS/NO/LI before incorporation.

### 6.2 Art. 31 SCA cases (ESA infringement procedures)

The Surveillance and Court Agreement gives the EFTA Surveillance Authority a
mandate analogous to Commission Art. 258 TFEU action, addressed to the EFTA Court
under Art. 31 SCA. The suite's infringement-procedure-tracker skill consumes ESA
case data published at `https://www.eftasurv.int/cms/sites/default/files`.

### 6.3 IS / NO / LI national status

Each EEA EFTA state's transposition of an incorporated EU act is tracked in EEA-Lex
with the national identifier (Lög nr., LOV-, LGBl.) and entry-into-force date.

---

## 7. IATE — terminology

The InterActive Terminology for Europe at `https://iate.europa.eu/` is the
Publications Office's multilingual terminology bank, covering the 24 official EU
languages plus Icelandic, Norwegian, and several languages of accession candidates.

### 7.1 Bulk export

IATE provides a free, registration-required bulk export at
`https://iate.europa.eu/download-iate`. Format options:
- **TBX** (TermBase eXchange, ISO 30042) — XML, the canonical format.
- **CSV** — flattened, one row per (term × language), useful for joins.
- **JSON** — newer, exposes the full IATE record structure (definitions,
  reliability codes, domain assignments per EuroVoc).

### 7.2 Use case in the suite

When the conformity-assessment skill needs to verify that the German Expression's
*wesentliche Dienste* and the English Expression's *essential entities* refer to
the same NIS2 concept, IATE entry 3577712 (or the relevant active entry) is the
authoritative cross-language alignment. Always cite the IATE entry ID.

---

## 8. National parliament APIs

The transposition tracker, correlation table builder, and conformity assessment
skills need primary-source national legislative data. The seven-priority MS plus
EEA EFTA states publish open APIs.

### 8.1 Riksdagen (Sweden)

- Endpoint: `https://data.riksdagen.se`
- Format: REST/JSON (and RDF). Documentation at `https://data.riksdagen.se/dokumentation/`.
- Example: `https://data.riksdagen.se/dokumentlista/?sok=NIS2&doktyp=prop&utformat=json`
  returns government bills (proposition) matching "NIS2".
- Identifier mapping: `prop. {year}/{sequential}` → published in SFS as `SFS {year}:{number}`.

### 8.2 Storting (Norway)

- Endpoint: `https://data.stortinget.no`
- Format: REST/XML and JSON. Documentation at `https://data.stortinget.no/dokumentasjon-og-hjelp/`.
- Example: `https://data.stortinget.no/eksport/saker?sesjonid=2023-2024&format=json`
  returns all parliamentary cases for session 2023–2024.

### 8.3 Folketinget (Denmark)

- Endpoint: `https://oda.ft.dk`
- Format: OData v3, JSON or XML. Documentation at `https://www.ft.dk/da/dokumenter/aabne_data`.
- Example: `https://oda.ft.dk/api/Sag?$filter=titelkort eq 'NIS2'&$format=json`.

### 8.4 Althingi (Iceland)

- Endpoint: `https://www.althingi.is/altext/`
- Format: XML. The Open Data section publishes an XML feed of every parliamentary
  case (`mál`), bill (`frumvarp`), and government communication (`stjórnartillaga`).
- Example: `https://www.althingi.is/altext/154/s/{sequential}.html` for individual
  case files in the 154th legislative session.

### 8.5 Bundestag (Germany)

- Endpoint: `https://dip.bundestag.de`
- Format: REST/JSON. The Documentations- und Informationssystem (DIP) exposes
  every Drucksache, plenary protocol, and committee report.
- Example: `https://search.dip.bundestag.de/api/v1/vorgang?f.titel=NIS2&apikey={key}`.
- Documentation at `https://dip.bundestag.de/%C3%BCber-dip/hilfe/api`.

### 8.6 Assemblée nationale (France)

- Endpoint: `https://data.assemblee-nationale.fr`
- Format: JSON, RDF, OAI-PMH. Documentation at `https://data.assemblee-nationale.fr/documentation/`.
- Example: `https://data.assemblee-nationale.fr/static/openData/repository/16/loi/dossiers_legislatifs/Dossiers_Legislatifs_XVI.json.zip`
  is the bulk export of the 16th legislative period.

### 8.7 Other national parliaments (operational notes)

- **Sejm (Poland)** — `https://api.sejm.gov.pl`. REST/JSON, no authentication. Bills
  surface as `druk` (Drucksache equivalent) with eventual publication in `Dz.U.`.
- **Tweede Kamer (Netherlands)** — `https://opendata.tweedekamer.nl`. OData v4.
  Bills (Wetsvoorstellen) link to Staatsblad publication.
- **Cortes Generales (Spain)** — `https://www.congreso.es/opendata`. JSON. The
  Cortes site publishes Boletín Oficial de las Cortes Generales (BOCG) parallel
  to BOE publication of the adopted act.
- **Camera dei Deputati (Italy)** — `https://dati.camera.it/sparql`. SPARQL
  endpoint over linked-data publication of every legislative dossier.
- **Eduskunta (Finland)** — `https://avoindata.eduskunta.fi`. REST/JSON.
- **Riigikogu (Estonia)** — `https://api.riigikogu.ee` and the Riigi Teataja
  publication system at `https://www.riigiteataja.ee` for the OJ-equivalent.
- **Saeima (Latvia)** — `https://titania.saeima.lv` (HTML scraping; no documented
  public API). Latvijas Vēstnesis is the OJ-equivalent at `https://likumi.lv`.

---

## 9. Single Market Scoreboard / ESA Internal Market Scoreboard

### 9.1 Single Market Scoreboard (Commission)

At `https://single-market-scoreboard.ec.europa.eu/`. Refresh cadence:
- **Transposition deficit** — semi-annual (twice per calendar year).
- **Open infringement procedures** — semi-annual.
- **Conformity deficit** — annual.

Structured data exports are available as XLSX and CSV per indicator, dated to
the publication of the corresponding Single Market Scoreboard report. The suite's
gold-plating-detector and infringement-procedure-tracker skills consume the XLSX
exports as their authoritative quantitative baseline.

### 9.2 ESA Internal Market Scoreboard

The EFTA Surveillance Authority publishes a parallel Internal Market Scoreboard for
the EEA EFTA states (IS/NO/LI) at `https://www.efta.int/`. Refresh cadence:
twice yearly (May and November). It uses the same indicator definitions as the
Commission Scoreboard for comparability under the homogeneity principle of Art.
6 EEA.

---

## 10. Coverage matrix — Legalcode MCP vs. direct API

The matrix below tells each skill which fall-back path to use. "MCP" means the
source is reachable through Legalcode MCP `search_laws`/`search_cases`/
`search_guidance`; "Direct" means the skill must fall back to the API/SPARQL
shape described above.

| Source | `search_laws` | `search_cases` | `search_guidance` | Direct fallback |
|---|---|---|---|---|
| Cellar SPARQL (acts) | yes | — | — | §1 of this file |
| Cellar SPARQL (case-law graph) | — | yes | — | §1 of this file |
| EUR-Lex web service | partial | — | — | §2 |
| N-Lex / MNE | yes | — | — | §3 (via Cellar) |
| OEIL dossiers | — | — | partial | §4 (HTML parse + Cellar) |
| CURIA / InfoCuria | — | yes | — | §5 |
| EEA-Lex (JCDs) | partial | — | partial | §6 |
| ESA Art. 31 SCA cases | — | partial | — | §6.2 |
| IATE bulk | — | — | — | §7 (download required) |
| Riksdagen | — | — | partial | §8.1 |
| Storting | — | — | partial | §8.2 |
| Folketinget | — | — | partial | §8.3 |
| Althingi | — | — | partial | §8.4 |
| Bundestag DIP | — | — | partial | §8.5 |
| Assemblée nationale | — | — | partial | §8.6 |
| Single Market Scoreboard | — | — | partial | §9.1 (XLSX export) |
| ESA Internal Market Scoreboard | — | — | partial | §9.2 |

"Partial" means coverage exists for some but not all queries the suite issues;
the skill must check whether the MCP response addresses the specific question
before declaring it answered. Where the MCP path is "—", the skill must use the
direct fallback every time.

Per the project CLAUDE.md instruction, the suite never calls `mcp__legalcode__*`
tools directly from the main conversation — every research call goes through the
`legalcode-search-agent` subagent, which knows how to combine the MCP path with
the direct-API fallbacks above.
