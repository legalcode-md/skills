# Identifier Playbook — CELEX, ELI, ECLI, OJ, National IDs, FRBR

This playbook is the canonical reference for legal identifiers used across the
seven-skill EU Legislative Compliance suite. Every workflow step that constructs,
parses, validates, or cites a legal identifier must use the rules below. Inventing
an identifier is an Anti-Pattern flagged in every skill in the suite — when in
doubt, dereference the URI against EUR-Lex (`https://eur-lex.europa.eu`) or CURIA
(`https://curia.europa.eu`) and confirm the document resolves.

---

## 1. CELEX — Publications Office identifier

CELEX (Communitatis Europeae LEX) is the Publications Office's stable, legacy
identifier for every act in the EU acquis. It is the single most-used cross-reference
in EUR-Lex and the Cellar Common Data Model.

### 1.1 Structure

CELEX is a fixed-width string composed of four positional fields:

```
[ Sector ][ Year ][ Type ][ Number ]
   1        4       1        4
```

- **Sector (1 char)** — top-level numbered sector. The values used by the suite are:
  - `1` Treaties (TFEU/TEU consolidated and historical versions)
  - `2` International agreements concluded by the Union
  - `3` Legal acts (regulations, directives, decisions, recommendations, opinions)
  - `4` Supplementary acts (e.g. Council acts under former third pillar)
  - `6` Case law (CJEU, General Court, Civil Service Tribunal)
  - `7` National Implementing Measures (NIMs notified under Art. 260(3) TFEU)
  - `8` References to national case law concerning Union law
  - `9` Parliamentary questions (used as evidence in OEIL dossiers)
  - `0` Consolidated texts (the consolidated version of a sector-3 act)
  - `C` OJ C-series notices (information and notices, not legally binding)
  - `E` EEA legal acts and Joint Committee Decisions
- **Year (4 chars)** — the year of the act. For directives and regulations this is
  the year of the act number (e.g. `2016` for GDPR (Regulation (EU) 2016/679)),
  not the year of OJ publication.
- **Type (1 char)** — the act type within the sector. Within sector 3:
  - `R` Regulation
  - `L` Directive (Latin *Lex*; the letter is fixed by Publications Office convention)
  - `D` Decision
  - `H` Recommendation
  - `O` Opinion
  - `G` Guideline (ECB) / Communication
  Within sector 6 (case law):
  - `J` Judgment of the Court of Justice
  - `T` Judgment of the General Court
  - `O` Order
  - `A` Advocate General's opinion
  - `C` Communication / view
- **Number (4 chars)** — the sequential number of the act within its year-and-type,
  zero-padded to four digits.

### 1.2 Validation rules

A CELEX validates if and only if:

1. The string is exactly 10 characters (or 11 for sector C/E) with no spaces.
2. Position 1 is one of the legal sector codes above.
3. Positions 2–5 are a four-digit year (1952 ≤ Y ≤ current year + 1; 1952 is the
   earliest sector 1 ECSC treaty).
4. Position 6 is a single uppercase letter valid for the declared sector.
5. Positions 7–10 are a four-digit decimal number, zero-padded, > 0000.
6. The CELEX dereferences via `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:<celex>`
   to a real document. (Construction without dereferencing is an Anti-Pattern.)

### 1.3 Worked examples

| Short title | CELEX | Sector | Year | Type | Number | Notes |
|---|---|---|---|---|---|---|
| GDPR | `32016R0679` | 3 | 2016 | R Regulation | 0679 | Regulation (EU) 2016/679 |
| NIS2 Directive | `32022L2555` | 3 | 2022 | L Directive | 2555 | Directive (EU) 2022/2555 |
| AI Act | `32024R1689` | 3 | 2024 | R Regulation | 1689 | Regulation (EU) 2024/1689 |
| CSRD | `32022L2464` | 3 | 2022 | L Directive | 2464 | Directive (EU) 2022/2464 |
| CSDDD | `32024L1760` | 3 | 2024 | L Directive | 1760 | Directive (EU) 2024/1760 |
| DSA | `32022R2065` | 3 | 2022 | R Regulation | 2065 | Regulation (EU) 2022/2065 |
| DMA | `32022R1925` | 3 | 2022 | R Regulation | 1925 | Regulation (EU) 2022/1925 |
| DORA | `32022R2554` | 3 | 2022 | R Regulation | 2554 | Regulation (EU) 2022/2554 |
| Whistleblower Directive | `32019L1937` | 3 | 2019 | L Directive | 1937 | Directive (EU) 2019/1937 |
| Reg. 1/1958 (languages) | `31958R0001` | 3 | 1958 | R Regulation | 0001 | Council Regulation No 1 |
| TFEU consolidated 2008 | `12008E/TXT` | 1 | 2008 | E TFEU | TXT | Sector 1 uses non-numeric tail |
| TFEU Art. 288 | `12008E288` | 1 | 2008 | E TFEU | 288 | Cited in every infringement skill |

### 1.4 Constructing a CELEX from a formal title

Given "Directive (EU) 2022/2555 of the European Parliament and of the Council of 14
December 2022 on measures for a high common level of cybersecurity across the Union":

1. Sector → `3` (legal act).
2. Year → `2022` (from the act number, not the date of adoption).
3. Type → `L` (Directive).
4. Number → `2555`, zero-padded to four digits.
5. Concatenate → `32022L2555`.

### 1.5 Treaty CELEX (sector 1)

Treaty articles use sector 1 with a non-standard tail. The most-cited TFEU articles
in the suite resolve as:

- `12008E288` — Art. 288 TFEU (instrument hierarchy: regulations directly applicable;
  directives binding as to result, leaving choice of form and method to MS;
  decisions binding in their entirety on those to whom addressed).
- `12008E258` — Art. 258 TFEU (Commission infringement procedure: letter of formal
  notice → reasoned opinion → referral to the Court of Justice).
- `12008E260` — Art. 260 TFEU (penalty payment under 260(2) after non-compliance
  with Art. 258 judgment; first-referral lump sum/penalty under 260(3) for failure
  to notify transposition of a legislative directive).

---

## 2. ELI — European Legislation Identifier

The European Legislation Identifier is the HTTP URI scheme registered by the EU
Publications Office and the Member States for legislation. ELI is dereferenceable:
the URI itself is the locator and the identifier. Technical information is
maintained at `https://eur-lex.europa.eu/eli-register/technical_information.html`.

### 2.1 EU-level URI template

```
https://eur-lex.europa.eu/eli/{type}/{year}/{number}[/{point-in-time}]/oj/{lang}
```

- `{type}` — `reg` (regulation), `dir` (directive), `dec` (decision), `rec`
  (recommendation), `treaty` (treaty), `agree` (international agreement).
- `{year}` — four-digit year of the act.
- `{number}` — sequential number, no zero-padding.
- `{point-in-time}` — optional ISO date (YYYY-MM-DD) for a consolidated version;
  omit to retrieve the act as adopted (the original Manifestation in CDM terms).
- `{lang}` — a three-letter ISO 639-2/B/T code from the 24 official EU languages.
  Special case: `oj` (no `/<lang>`) returns the language-neutral resource.

### 2.2 Worked ELI URIs

```
GDPR (English, original):    https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
NIS2 (English, original):    https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng
AI Act (English, original):  https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
CSRD (English, original):    https://eur-lex.europa.eu/eli/dir/2022/2464/oj/eng
CSDDD (English, original):   https://eur-lex.europa.eu/eli/dir/2024/1760/oj/eng
DSA  (English, original):    https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng
TFEU Art. 288 (English):     https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng
Reg. 1/1958 (English):       https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng
```

### 2.3 The 24 official-language `/oj/<lang>` patterns

| Language | ISO code | Example (NIS2) |
|---|---|---|
| Bulgarian | `bul` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/bul` |
| Croatian | `hrv` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/hrv` |
| Czech | `ces` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/ces` |
| Danish | `dan` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/dan` |
| Dutch | `nld` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/nld` |
| English | `eng` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng` |
| Estonian | `est` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/est` |
| Finnish | `fin` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/fin` |
| French | `fra` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/fra` |
| German | `deu` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/deu` |
| Greek | `ell` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/ell` |
| Hungarian | `hun` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/hun` |
| Irish | `gle` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/gle` |
| Italian | `ita` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/ita` |
| Latvian | `lav` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/lav` |
| Lithuanian | `lit` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/lit` |
| Maltese | `mlt` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/mlt` |
| Polish | `pol` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/pol` |
| Portuguese | `por` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/por` |
| Romanian | `ron` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/ron` |
| Slovak | `slk` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/slk` |
| Slovenian | `slv` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/slv` |
| Spanish | `spa` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/spa` |
| Swedish | `swe` | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/swe` |

The 24-language regime is the consequence of Regulation 1/1958 as amended by every
accession treaty since the 1973 enlargement. The Irish derogation under Council
Regulation 920/2005 was lifted on 1 January 2022 by Council Regulation 2015/2264;
since that date, every EU act of general application is published in Irish.

### 2.4 ELI registered properties (subset used by the suite)

The ELI ontology (CDM `eli` namespace) registers the following properties on
`http://data.europa.eu/eli/ontology#LegalResource` instances. These are the
properties most often queried by the suite:

- `eli:type_document` — instrument type (regulation/directive/decision).
- `eli:date_document` — adoption date.
- `eli:date_publication` — OJ publication date.
- `eli:passed_by` — adopting institution (Council, Parliament, Commission).
- `eli:in_force` — Boolean: in force / repealed.
- `eli:transposed_by` — backlink to a NIM (sector 7 CELEX).
- `eli:cites` — outbound citation to another ELI.
- `eli:basis_for` — outbound link to implementing/delegated acts.
- `eli:language` — ISO 639-2 code on each Manifestation.
- `eli:realizes_legal_resource` — the FRBR Work that a given Expression realises.

### 2.5 Dereferenceability and content negotiation

ELIs honour HTTP content negotiation. A request to
`https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng` with `Accept: text/html` returns
the EUR-Lex web page; with `Accept: application/rdf+xml` it returns CDM RDF; with
`Accept: application/xml` and the right format suffix, the AKN4EU XML (where
available — AKN4EU coverage is partial and trending upward).

---

## 3. ECLI — European Case Law Identifier

ECLI is the analogue of ELI for case law. Every CJEU, General Court, EFTA Court, and
participating national court judgment has an ECLI under Council Conclusions
2011/C 127/01.

### 3.1 Structure

```
ECLI:{country-code}:{court-code}:{year}:{ordinal}
```

- `{country-code}` — ISO 3166-1 alpha-2 with two EU-specific extensions:
  - `EU` — Court of Justice of the European Union (CJEU + General Court + Civil
    Service Tribunal historical).
  - `EFTA` — EFTA Court (Luxembourg seat; jurisdiction over the EFTA pillar of
    the EEA — IS, NO, LI).
  - Plus all 27 MS codes (`DE`, `FR`, `IT`, `ES`, `NL`, `SE`, `DK`, `FI`, `IE`,
    `BE`, `LU`, `AT`, `EL`, `PT`, `CY`, `MT`, `CZ`, `SK`, `SI`, `HR`, `EE`,
    `LV`, `LT`, `PL`, `HU`, `RO`, `BG`).
- `{court-code}` — for `EU` jurisdiction:
  - `C` — Court of Justice (judgments and orders).
  - `T` — General Court (formerly Court of First Instance).
  - `F` — Civil Service Tribunal (closed September 2016; historical only).
- `{year}` — four-digit year of the decision.
- `{ordinal}` — sequential within (jurisdiction, court, year).

### 3.2 Worked ECLI examples

| Case | Citation | Notes |
|---|---|---|
| *Commission v Belgium* | C-543/17, ECLI:EU:C:2019:573 | First Art. 260(3) TFEU lump sum for failure to notify transposition (telecoms framework directive). |
| *CILFIT* | C-283/81, ECLI:EU:C:1982:335 | Equal authenticity of language versions; *acte clair* doctrine. |
| *Codan* | C-236/97, ECLI:EU:C:1998:208 | Reconciliation methodology where language versions diverge. |
| *EMU Tabac* | C-296/95, ECLI:EU:C:1998:152 | Single language interpretation cannot prevail over the others. |
| *Endendijk* | C-187/07, ECLI:EU:C:2008:197 | Comparative-language interpretation in agricultural law. |
| *Francovich* | C-6/90, ECLI:EU:C:1991:428 | State liability for non-transposition. |

### 3.3 Validation

An ECLI validates if and only if:

1. It begins with the literal `ECLI:` prefix.
2. The country/jurisdiction code is one of the registered codes (`EU`, `EFTA`, or
   a participating national code).
3. For `EU`, the court code is `C`, `T`, or `F`.
4. The year is four digits within the court's lifetime.
5. The ECLI dereferences via CURIA: `https://curia.europa.eu/juris/liste.jsf?
   language=en&num=<case-number>` returns the case file, and the case file's
   metadata block lists the ECLI.

### 3.4 Court of First Instance / General Court legacy

Pre-October 2016 General Court cases used the Court of First Instance abbreviation
`T-` for the case number (e.g. *Microsoft* T-201/04, ECLI:EU:T:2007:289). After
the Civil Service Tribunal was abolished in September 2016, all `F-` cases were
either transferred to the General Court or closed. Historical ECLI:EU:F:* citations
remain valid but the court no longer exists.

---

## 4. Official Journal reference format

The OJ reference is the formal citation form required in every EU act preamble and
in Commission templates. Format:

```
OJ {series} {number}, {dd.mm.yyyy}, p. {first-page}
```

- `{series}` — `L` (legislation), `C` (information and notices), `S` (supplement
  for procurement), `A` (special edition for accession-related publications).
- `{number}` — the OJ issue number within the series and year.
- `{dd.mm.yyyy}` — date of publication, day-month-year separated by full stops.
- `{first-page}` — the page on which the act starts within that OJ issue.

Worked examples (verbatim style required by the suite's citation density rule):

- NIS2: **OJ L 333, 27.12.2022, p. 80**.
- GDPR: **OJ L 119, 4.5.2016, p. 1**.
- AI Act: **OJ L, 2024/1689, 12.7.2024**. (After 1 October 2023, OJ L moved to a
  daily-numbered scheme — `OJ L, YYYY/N, dd.mm.yyyy` — and dropped the per-issue
  page-number field. This is the format used for all post-October-2023 acts.)
- CSRD: **OJ L 322, 16.12.2022, p. 15**.
- CSDDD: **OJ L, 2024/1760, 5.7.2024**.
- DSA: **OJ L 277, 27.10.2022, p. 1**.
- DMA: **OJ L 265, 12.10.2022, p. 1**.

---

## 5. National identifier formats

Every Member State has a constitutional publication convention. The suite's
correlation table builder, transposition tracker, and conformity assessment skills
must cite the NIM in the form used by the national legislator. The table below
covers the seven priority MS plus EEA EFTA states.

| MS | Publication | Citation format | Example |
|---|---|---|---|
| Germany | *Bundesgesetzblatt* (BGBl.) Teil I/II | `BGBl. I {year} Nr. {issue}, S. {page}` or modern `BGBl. {year} I Nr. {sequential-id}` (since 2023 reform abandoning page numbers in the digital BGBl.) | `BGBl. 2024 I Nr. 244` (NIS2 Umsetzungsgesetz) |
| France | *Journal officiel de la République française* (JORF) | `JORF n° {issue}, {date}, texte n° {item}` and the parallel "NOR" identifier on each act | `JORF n° 0123 du 28 mai 2024, texte n° 5; NOR : INTX2400412L` |
| Norway | *Norsk Lovtidend* / *Stortingsforhandlinger* | `LOV-{year}-{date}-{number}` | `LOV-2024-06-14-30` |
| Iceland | *Stjórnartíðindi* (A series for laws, B series for regulations) | `Lög nr. {number}/{year}` | `Lög nr. 47/2024` |
| Sweden | *Svensk författningssamling* (SFS) | `SFS {year}:{number}` | `SFS 2024:1255` |
| Denmark | *Lovtidende* | `LOV nr {number} af {dd/mm/yyyy}` | `LOV nr 1212 af 18/06/2024` |
| Poland | *Dziennik Ustaw* (Dz.U.) | `Dz.U. {year} poz. {item}` | `Dz.U. 2024 poz. 1234` |
| Netherlands | *Staatsblad* (Stb.) | `Stb. {year}, {number}` | `Stb. 2024, 250` |
| Italy | *Gazzetta Ufficiale* (G.U.) | `G.U. Serie Generale n. {issue} del {date}` | `G.U. n. 156 del 5.7.2024` |
| Spain | *Boletín Oficial del Estado* (BOE) | `BOE núm. {issue}, de {date}` and parallel "BOE-A-{year}-{seq}" identifier | `BOE-A-2024-12345` |
| Finland | *Suomen säädöskokoelma* (SK) | `{number}/{year}` | `345/2024` |

Liechtenstein publishes in the *Liechtensteinisches Landesgesetzblatt* (LGBl.):
`LGBl. {year} Nr. {number}`. The format is identical in form to the German BGBl.
but the institution and citation context are distinct.

---

## 6. FRBR levels in the Cellar Common Data Model

The Cellar Common Data Model (CDM) implements the IFLA FRBR (Functional Requirements
for Bibliographic Records) hierarchy. Every act in the EU acquis is modelled as
four nested entities; understanding the level matters when fetching definitive
versus consolidated text.

| FRBR level | CDM class | What it represents | Why it matters |
|---|---|---|---|
| **Work** | `cdm:work` | The abstract intellectual creation — "Directive (EU) 2022/2555". One per act, language-neutral, version-neutral. | The Work is what `eli:realizes_legal_resource` points to. Use the Work URI when you need the canonical identity of the act independent of any particular text. |
| **Expression** | `cdm:expression` | A specific intellectual realisation — "the German consolidated version of NIS2 as at 14 December 2022". One per (language × point-in-time) combination. | The Expression is the level at which equal authenticity attaches under Reg. 1/1958: a German Expression and a French Expression of the same Work are equally authentic. When the suite does language-version reconciliation (see `multilingualism-playbook.md`), it compares Expressions. |
| **Manifestation** | `cdm:manifestation` | A physical realisation of an Expression — the OJ PDF, the AKN4EU XML, the HTML page. One Expression typically has several Manifestations (PDF, XHTML, RDF/XML, AKN4EU). | The Manifestation is what content negotiation against an ELI returns. When the suite emits an Akoma Ntoso obligation register (see `formats-playbook.md`), it is a new Manifestation of an analytical Expression, not of the act itself. |
| **Item** | `cdm:item` | A single instance of a Manifestation — one downloaded file. Rarely surfaced in the suite. | Used internally by Cellar for caching and access control; the suite does not normally distinguish Items from Manifestations. |

### 6.1 Definitive vs. consolidated text

The original adopted text is the Manifestation linked to the Expression with no
`eli:point-in-time` and `cdm:expression_belongs_to_first_realisation_of_work true`.
The consolidated text is a different Expression (or a chain of Expressions) with
explicit `eli:point-in-time` values. For infringement procedures and conformity
assessment, the **definitive text** is the relevant authority; for transposition
gap analysis on a directive that has been amended (e.g. AML Directive amendments
chaining back to 2015/849), the **consolidated text at the transposition deadline**
is the relevant authority. Always fetch with an explicit `eli:point-in-time` when
the act has been amended.

### 6.2 SPARQL fragment to walk the FRBR hierarchy

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?work ?expression ?language ?manifestation ?format
WHERE {
  ?work cdm:work_id_document "32022L2555" .
  ?expression cdm:expression_belongs_to_work ?work ;
              cdm:expression_uses_language ?language .
  ?manifestation cdm:manifestation_manifests_expression ?expression ;
                 cdm:manifestation_type ?format .
}
```

This walks NIS2 from the Work down to every (Expression × Manifestation) combination
and is the foundation of the Cellar query in `source-playbook.md`.
